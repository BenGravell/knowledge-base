"""
generate_map_data.py
=========================
Generate the Sigma.js map data file for the knowledge-base site.

This script reads every paper's ``metadata.yml``, embeds each paper's
text using a high-quality embedding model, computes pairwise cosine
similarities, and writes ``knowledge_base/map/map-data.js``
which the Sigma.js visualisation loads at runtime.

Incremental operation
---------------------
Embeddings are expensive to generate.  To avoid re-embedding every paper
each time a few new papers are added, the script maintains a local cache
file (``embedding_cache.json`` by default).  On each run it:

  1. Reads the cache (if it exists).
  2. For every paper computes a *content hash* over the text that will be
     embedded (title + tags + summary + abstract).
  3. Removes cached entries for papers whose ``metadata.yml`` no longer exists.
  4. Re-embeds only the papers whose hash differs from the cached value or
     which are entirely new.
  5. Writes the updated cache back to disk.
  6. Recomputes the full similarity matrix from the (now complete) set of
     embeddings and rewrites the JS output file.

UMAP positions are also cached in the same file (under a ``"umap"`` key).
The UMAP cache is keyed by a SHA-256 hash of the paper IDs (in order),
the embedding matrix bytes, and the UMAP hyperparameters, so it is
automatically invalidated whenever any paper is added/removed/changed or
the parameters change.

Embedding backends
------------------
Two backends are supported, tried in order of quality:

  1. **Voyage AI** ``voyage-3-large`` (1024-d, state-of-the-art quality).
     Requires the ``voyageai`` Python package and a ``VOYAGE_API_KEY``
     environment variable.  Get a key at https://www.voyageai.com/.

  2. **fastembed** ``mixedbread-ai/mxbai-embed-large-v1`` (1024-d, top
     open-source model on the MTEB benchmark, runs fully locally with no
     API key via ONNX).  Requires the ``fastembed`` Python package:
         pip install fastembed

Set ``VOYAGE_API_KEY`` in your environment to use Voyage AI.  Without it
the script falls back to fastembed automatically.

Usage
-----
Basic (auto-selects backend, incremental):
    python knowledge_base/map/generate_map_data.py

Force full re-embed (ignores cache):
    python knowledge_base/map/generate_map_data.py --force

Choose a specific backend explicitly:
    python generate_map_data.py --backend voyage
    python generate_map_data.py --backend fastembed

Custom paths:
    python knowledge_base/map/generate_map_data.py \\
        --cache knowledge_base/map/my_cache.json \\
        --output knowledge_base/map/map-data.js

Output
------
``knowledge_base/map/map-data.js`` — a JS file that sets the
global ``mapData`` variable consumed by map.js.  The MkDocs
gen-files script ``copy_assets.py`` publishes this file into the served
site automatically at build time.

Requirements
------------
Always required:
    pyyaml numpy umap-learn

For Voyage AI backend:
    voyageai

For fastembed backend:
    fastembed
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import sys
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np
import yaml
from scipy.spatial import KDTree as cKDTree
from sklearn.preprocessing import normalize

from knowledge_base.catalog import Catalog
from knowledge_base.tree.model import (
    TreeModel,
)
from knowledge_base.tree.model import (
    common_prefix_length as tree_common_prefix_length,
)
from knowledge_base.tree.model import (
    tree_distance as tree_model_distance,
)
from knowledge_base.tree.nav_source import load_tree

# ---------------------------------------------------------------------------
# Paths (relative to this script's location: knowledge_base/map/)
# ---------------------------------------------------------------------------

MAP_DIR = Path(__file__).parent  # knowledge_base/map/
KB_DIR = MAP_DIR.parent  # knowledge_base/
REPO_ROOT = KB_DIR.parent  # repo root
DOCS_DIR = KB_DIR / "docs"
METADATA_ROOT = DOCS_DIR / "papers"
MKDOCS_YML = KB_DIR / "mkdocs.yml"
DEFAULT_CACHE = MAP_DIR / "embedding_cache.json"
DEFAULT_OUTPUT = MAP_DIR / "map-data.js"

DEFAULT_UMAP_SCALE = 1500.0  # Base UMAP coordinate extent; formerly 1000 px.
SIMILARITY_EXPORT_SCALE = 1000  # Store cosine similarities as compact rounded integers.
TREE_PROXIMITY_HISTOGRAM_BINS = 101

LEGACY_BRANCH_LEVEL_IDS = ["super_category", "category", "sub_category"]
NODE_DIAMETER_SCALE = 2
PAPER_NODE_RADIUS_TARGET = 12 * NODE_DIAMETER_SCALE
AGGREGATE_EXTRA_AREA_UNITS_BY_LEVEL = [18, 12, 8, 5, 3]
AGGREGATE_EXTRA_AREA_FALLBACK_UNITS = 2
AGGREGATE_MIN_RADIUS_RATIO = 1.7
AGGREGATE_POSITION_OUTER_QUANTILE = 0.84
AGGREGATE_POSITION_BIAS_BY_LEVEL = [0.68, 0.52, 0.36, 0.24]
AGGREGATE_COLLISION_PADDING = 0.75
AGGREGATE_FINAL_COLLISION_ITERATIONS = 240
AGGREGATE_COLLISION_EPSILON = 1e-3

# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------


def compute_umap_positions(
    embeddings: np.ndarray,
    scale: float = DEFAULT_UMAP_SCALE,
    random_state: int = 42,
    n_neighbors: int | None = None,
    min_dist: float = 0.05,
    n_epochs: int = 500,
) -> np.ndarray:
    """Project high-dimensional embeddings to 2-D UMAP coords scaled to pixel-space.

    The result is centred at the origin and scaled so the largest axis spans
    ±scale pixels.
    """
    import umap

    if n_neighbors is None:
        n_neighbors = min(50, len(embeddings) - 1)

    reducer = umap.UMAP(
        n_components=2,
        metric="cosine",
        n_neighbors=n_neighbors,  # large neighbourhood → global structure
        min_dist=min_dist,  # tighter packing within clusters
        n_epochs=n_epochs,  # more optimisation steps → better convergence
        random_state=random_state,
    )
    coords = reducer.fit_transform(embeddings).astype(np.float64)
    coords -= coords.mean(axis=0)
    spread = np.abs(coords).max()
    if spread > 0:
        coords = coords / spread * scale
    return coords


def umap_cache_key(
    paper_ids: list[str],
    embeddings: np.ndarray,
    **umap_params: Any,
) -> str:
    """Stable hash over inputs that fully determine the UMAP result."""
    h = hashlib.sha256()
    h.update(json.dumps(paper_ids).encode("utf-8"))
    h.update(embeddings.tobytes())
    h.update(json.dumps(umap_params, sort_keys=True).encode("utf-8"))
    return h.hexdigest()[:24]


# ---------------------------------------------------------------------------
# Force-directed layout post-processing
# ---------------------------------------------------------------------------


def force_cache_key(
    umap_coords: np.ndarray,
    embeddings: np.ndarray,
    **force_params: Any,
) -> str:
    """Stable hash over inputs that fully determine the force layout result."""
    h = hashlib.sha256()
    h.update(umap_coords.tobytes())
    h.update(embeddings.tobytes())
    h.update(json.dumps(force_params, sort_keys=True).encode("utf-8"))
    return h.hexdigest()[:24]


def force_layout_postprocess(
    umap_coords: np.ndarray,
    embeddings: np.ndarray,
    *,
    pre_layout_scale: float = 1.0,
    anchor_strength: float = 0.85,
    sim_threshold: float = 0.75,
    sim_candidate_limit: int = 10,
    sim_attraction_strength: float = 0.4,
    gap_factor: float = 2.0,
    collision_radius_factor: float = 0.45,
    collision_iterations: int = 3,
    iterations: int = 120,
    initial_alpha: float = 0.3,
    alpha_decay: float = 0.98,
    post_scale: float = 2.0,
    verbose: bool = True,
) -> np.ndarray:
    """Post-process UMAP coordinates with a constrained force simulation.

    Three forces act each iteration:

    1. **Anchor** — every node is pulled back toward its original UMAP position
       with strength *anchor_strength*, keeping the global topology intact.
    2. **Similarity attraction** — pairs that are semantically close
       (cosine similarity ≥ *sim_threshold*) but spatially far apart in UMAP
       space (distance > *gap_factor* x median nearest-neighbour distance) are
       pulled together.  Only the *sim_candidate_limit* most similar neighbours
       per node are considered, so the cost is O(N · sim_candidate_limit) per
       iteration.
    3. **Collision resolution** — after each integration step, overlapping nodes
       are pushed apart until no two nodes are closer than ``2 * collision_radius``,
       where ``collision_radius = sqrt(canvas_area / N) * collision_radius_factor``.

    The step size decays as ``alpha *= alpha_decay`` each iteration, so the
    simulation cools and converges rather than oscillating indefinitely.

    Parameters
    ----------
    umap_coords:
        (N, 2) array of 2-D positions from UMAP, in whatever coordinate scale
        UMAP produced (e.g. ±1500 px).
    embeddings:
        (N, D) array of raw embedding vectors; L2-normalised internally for
        cosine similarity computation.
    anchor_strength:
        Weight of the anchor force pulling nodes back to their UMAP home.
        Higher values preserve UMAP topology more faithfully (range: 0-1).
    pre_layout_scale:
        Before simulation, scale UMAP positions outward from their centroid by
        this factor.  This lets the force and collision passes operate on a
        roomier starting layout.
    sim_threshold:
        Minimum cosine similarity for a pair to receive an attraction force.
    sim_candidate_limit:
        Number of nearest embedding-space neighbours to consider per node when
        building the attraction pair list.
    sim_attraction_strength:
        Magnitude of the similarity attraction force, scaled by cosine similarity.
    gap_factor:
        A pair is only attracted if their current UMAP distance exceeds
        ``gap_factor x median_nn_dist``.  Prevents attracting already-close nodes.
    collision_radius_factor:
        Hard exclusion radius per node is computed as
        ``sqrt(canvas_area / N) * collision_radius_factor``, where
        *canvas_area* is the bounding-box area of the UMAP positions.
        The default of ``0.45`` fills roughly 60 % of a unit-density grid cell.
    collision_iterations:
        Sub-steps of collision resolution applied after each force integration.
    iterations:
        Total number of simulation steps.
    initial_alpha:
        Starting step size.
    alpha_decay:
        Multiplicative decay applied to alpha each iteration.
    verbose:
        Print per-iteration progress to stdout.
    post_scale:
        After the simulation, all coordinates are scaled by this factor
        outward from the centroid.  ``2.0`` doubles inter-node spacing.
        Set to ``1.0`` to disable.

    Returns
    -------
    np.ndarray
        (N, 2) array of adjusted coordinates, scaled *post_scale*× outward
        from the centroid relative to the post-simulation positions.
    """
    N = len(umap_coords)

    if verbose:
        print(f"    [force_layout] N={N}, iterations={iterations}, alpha0={initial_alpha}")

    emb_norm = normalize(embeddings.astype(np.float32))
    home = scale_positions_about_centroid(
        umap_coords.astype(np.float64),
        pre_layout_scale,
    )
    pos = home.copy()

    canvas = np.ptp(pos, axis=0)
    area = canvas[0] * canvas[1]
    collision_radius = np.sqrt(area / N) * collision_radius_factor
    if verbose:
        print(f"    [force_layout] collision_radius = {collision_radius:.4f}")

    tree_home = cKDTree(home)
    nn_dists, _ = tree_home.query(home, k=2)
    median_nn_dist = np.median(nn_dists[:, 1])
    gap_threshold = gap_factor * median_nn_dist
    if verbose:
        print(f"    [force_layout] median nn dist = {median_nn_dist:.4f}, gap threshold = {gap_threshold:.4f}")

    attract_pairs = _build_attraction_pairs(emb_norm, home, sim_candidate_limit, sim_threshold, gap_threshold, verbose)

    alpha = initial_alpha
    t0 = time.time()

    for it in range(iterations):
        forces = np.zeros_like(pos)

        delta_anchor = home - pos
        forces += anchor_strength * delta_anchor

        if len(attract_pairs) > 0:
            _apply_attraction(pos, attract_pairs, sim_attraction_strength, forces)

        pos += alpha * forces

        for _ in range(collision_iterations):
            _resolve_collisions(pos, collision_radius)

        alpha *= alpha_decay

        if verbose and (it % 20 == 0 or it == iterations - 1):
            drift = np.mean(np.linalg.norm(pos - home, axis=1))
            print(f"    [force_layout] iter {it:4d}  alpha={alpha:.4f}  mean drift from UMAP = {drift:.4f}")

    if verbose:
        elapsed = time.time() - t0
        final_drift = np.mean(np.linalg.norm(pos - home, axis=1))
        print(f"    [force_layout] done in {elapsed:.2f}s  final mean drift = {final_drift:.4f}")

    centroid = pos.mean(axis=0)
    return centroid + (pos - centroid) * post_scale


def scale_positions_about_centroid(coords: np.ndarray, scale: float) -> np.ndarray:
    """Return coordinates scaled outward from their centroid."""
    numeric_scale = float(scale)
    if not np.isfinite(numeric_scale) or numeric_scale <= 0:
        numeric_scale = 1.0
    if numeric_scale == 1.0:
        return coords.copy()

    centroid = coords.mean(axis=0)
    return centroid + (coords - centroid) * numeric_scale


def _build_attraction_pairs(
    emb_norm: np.ndarray,
    home: np.ndarray,
    candidate_limit: int,
    sim_threshold: float,
    gap_threshold: float,
    verbose: bool,
) -> np.ndarray:
    N = len(emb_norm)
    candidate_limit = min(max(candidate_limit, 0), N - 1)
    if candidate_limit == 0:
        if verbose:
            print("    [force_layout] similarity attraction pairs: 0")
        return np.empty((0, 3))

    sim_matrix = emb_norm @ emb_norm.T

    pairs: list[tuple[int, int, float]] = []
    for i in range(N):
        sims = sim_matrix[i]
        sims[i] = -1.0
        candidate_idx = np.argpartition(sims, -candidate_limit)[-candidate_limit:]
        for j in candidate_idx:
            if j <= i:
                continue
            s = sims[j]
            if s < sim_threshold:
                continue
            umap_dist = np.linalg.norm(home[i] - home[j])
            if umap_dist < gap_threshold:
                continue
            pairs.append((i, j, float(s)))

    result = np.array(pairs, dtype=np.float64) if pairs else np.empty((0, 3))
    if verbose:
        print(f"    [force_layout] similarity attraction pairs: {len(result)}")
    return result


def _apply_attraction(
    pos: np.ndarray,
    pairs: np.ndarray,
    strength: float,
    forces: np.ndarray,
) -> None:
    i_idx = pairs[:, 0].astype(int)
    j_idx = pairs[:, 1].astype(int)
    weights = pairs[:, 2]

    delta = pos[j_idx] - pos[i_idx]
    dist = np.linalg.norm(delta, axis=1, keepdims=True) + 1e-8
    unit = delta / dist
    mag = strength * weights[:, None]

    np.add.at(forces, i_idx, mag * unit)
    np.add.at(forces, j_idx, -mag * unit)


def _resolve_collisions(pos: np.ndarray, radius: float) -> None:
    tree = cKDTree(pos)
    pairs = tree.query_pairs(r=2 * radius, output_type="ndarray")

    if len(pairs) == 0:
        return

    i_idx = pairs[:, 0]
    j_idx = pairs[:, 1]

    delta = pos[i_idx] - pos[j_idx]
    dist = np.linalg.norm(delta, axis=1, keepdims=True) + 1e-8
    overlap = np.maximum(2 * radius - dist, 0)
    unit = delta / dist
    correction = 0.5 * overlap * unit

    np.add.at(pos, i_idx, correction)
    np.add.at(pos, j_idx, -correction)


@dataclass
class AggregateLayoutGroup:
    level: str
    label: str
    path: list[str]
    path_index: int
    parent: AggregateLayoutGroup | None = None
    children: list[AggregateLayoutGroup] = field(default_factory=list)
    child_map: dict[str, AggregateLayoutGroup] = field(default_factory=dict)
    leaf_indices: list[int] = field(default_factory=list)
    x: float = 0.0
    y: float = 0.0
    leaf_points: list[tuple[float, float]] = field(default_factory=list)
    layout_x: float | None = None
    layout_y: float | None = None
    centroid_x: float | None = None
    centroid_y: float | None = None


def aggregate_branch_levels(papers: list[dict[str, Any]], nav_order: dict[str, Any]) -> list[dict[str, int | str]]:
    data_depth = max((len(p.get("nav_path") or []) for p in papers), default=0)
    max_depth = max(4, int(nav_order.get("maxBranchDepth") or 0), data_depth)
    return [
        {
            "id": LEGACY_BRANCH_LEVEL_IDS[i] if i < len(LEGACY_BRANCH_LEVEL_IDS) else f"branch_{i + 1}",
            "path_index": i,
        }
        for i in range(max_depth)
    ]


def aggregate_node_size(count: int, level: str, level_indices: dict[str, int]) -> float:
    n = max(int(count) if count else 1, 1)
    index = max(level_indices.get(level, 0), 0)
    extra_area_units = (
        AGGREGATE_EXTRA_AREA_UNITS_BY_LEVEL[index]
        if index < len(AGGREGATE_EXTRA_AREA_UNITS_BY_LEVEL)
        else AGGREGATE_EXTRA_AREA_FALLBACK_UNITS
    )
    radius = PAPER_NODE_RADIUS_TARGET * np.sqrt(n + extra_area_units)
    min_radius = PAPER_NODE_RADIUS_TARGET * AGGREGATE_MIN_RADIUS_RATIO
    return float(max(radius, min_radius))


def padded_aggregate_nav_path(path: list[str], branch_depth: int) -> list[str]:
    clean_path = [str(part).strip() for part in (path or []) if str(part or "").strip()]
    if not clean_path:
        clean_path = [UNCATEGORIZED_CATEGORY]

    padded = list(clean_path)
    fallback = clean_path[-1]
    while len(padded) < branch_depth:
        padded.append(fallback)
    return padded[:branch_depth]


def quantile_value(values: list[float], q: float) -> float | None:
    finite = sorted(value for value in values if np.isfinite(value))
    if not finite:
        return None
    if len(finite) == 1:
        return finite[0]

    index = float(np.clip(q, 0.0, 1.0)) * (len(finite) - 1)
    lower = int(np.floor(index))
    upper = int(np.ceil(index))
    t = index - lower
    return finite[lower] * (1 - t) + finite[upper] * t


def hierarchy_group_centroid(group: AggregateLayoutGroup) -> tuple[float, float]:
    count = len(group.leaf_indices) or 1
    return group.x / count, group.y / count


def aggregate_position_bias(group: AggregateLayoutGroup) -> float:
    index = max(int(group.path_index), 0)
    if index < len(AGGREGATE_POSITION_BIAS_BY_LEVEL):
        return AGGREGATE_POSITION_BIAS_BY_LEVEL[index]
    return 0.18


def biased_aggregate_position(
    group: AggregateLayoutGroup,
    reference_point: tuple[float, float] | None,
) -> tuple[float, float]:
    centroid_x, centroid_y = hierarchy_group_centroid(group)
    if len(group.leaf_points) < 2 or reference_point is None:
        return centroid_x, centroid_y

    dx = centroid_x - reference_point[0]
    dy = centroid_y - reference_point[1]
    distance = float(np.hypot(dx, dy))
    if not np.isfinite(distance) or distance < 1e-6:
        return centroid_x, centroid_y

    ux = dx / distance
    uy = dy / distance
    centroid_projection = dx * ux + dy * uy
    outer_projection = quantile_value(
        [
            (point_x - reference_point[0]) * ux + (point_y - reference_point[1]) * uy
            for point_x, point_y in group.leaf_points
        ],
        AGGREGATE_POSITION_OUTER_QUANTILE,
    )

    if outer_projection is None or not np.isfinite(outer_projection) or outer_projection <= centroid_projection:
        return centroid_x, centroid_y

    offset = (outer_projection - centroid_projection) * aggregate_position_bias(group)
    return centroid_x + ux * offset, centroid_y + uy * offset


def aggregate_group_key(path: list[str]) -> str:
    return json.dumps([str(part or "") for part in path], ensure_ascii=False, separators=(",", ":"))


def deterministic_pair_unit(i: int, j: int) -> tuple[float, float]:
    angle = (((i + 1) * 12.9898) + ((j + 1) * 78.233)) % (np.pi * 2)
    return float(np.cos(angle)), float(np.sin(angle))


def _resolve_variable_collisions(
    pos: np.ndarray,
    radii: np.ndarray,
    padding: float = 0.0,
    pair_indices: tuple[np.ndarray, np.ndarray] | None = None,
) -> float:
    n = len(pos)
    if n < 2:
        return 0.0

    i_idx, j_idx = pair_indices if pair_indices is not None else np.triu_indices(n, k=1)
    delta = pos[i_idx] - pos[j_idx]
    dist = np.linalg.norm(delta, axis=1)
    min_dist = radii[i_idx] + radii[j_idx] + padding
    overlap = min_dist - dist
    mask = np.isfinite(dist) & (overlap > AGGREGATE_COLLISION_EPSILON)

    if not np.any(mask):
        return 0.0

    active_i = i_idx[mask]
    active_j = j_idx[mask]
    active_delta = delta[mask].copy()
    active_dist = dist[mask].copy()
    active_overlap = overlap[mask]

    zero_mask = active_dist < 1e-8
    if np.any(zero_mask):
        for zero_index in np.flatnonzero(zero_mask):
            unit = deterministic_pair_unit(
                int(active_i[zero_index]),
                int(active_j[zero_index]),
            )
            active_delta[zero_index] = unit
            active_dist[zero_index] = 1.0

    correction = 0.5 * active_overlap[:, None] * (active_delta / active_dist[:, None])
    np.add.at(pos, active_i, correction)
    np.add.at(pos, active_j, -correction)
    return float(active_overlap.max())


def aggregate_force_layout_postprocess(
    home_coords: np.ndarray,
    aggregate_embeddings: np.ndarray,
    radii: np.ndarray,
    *,
    anchor_strength: float = 0.85,
    sim_threshold: float = 0.75,
    sim_candidate_limit: int = 10,
    sim_attraction_strength: float = 0.4,
    gap_factor: float = 2.0,
    collision_padding: float = AGGREGATE_COLLISION_PADDING,
    collision_iterations: int = 3,
    final_collision_iterations: int = AGGREGATE_FINAL_COLLISION_ITERATIONS,
    iterations: int = 120,
    initial_alpha: float = 0.3,
    alpha_decay: float = 0.98,
    verbose: bool = False,
) -> np.ndarray:
    """Apply the item-level anchor/similarity force pass to aggregate disks."""
    n = len(home_coords)
    if n < 2:
        return home_coords.copy()

    emb_norm = normalize(aggregate_embeddings.astype(np.float32))
    pos = home_coords.astype(np.float64).copy()
    pair_indices = np.triu_indices(n, k=1)

    tree_home = cKDTree(home_coords)
    nn_dists, _ = tree_home.query(home_coords, k=2)
    median_nn_dist = np.median(nn_dists[:, 1])
    gap_threshold = gap_factor * median_nn_dist
    attract_pairs = _build_attraction_pairs(
        emb_norm,
        home_coords.astype(np.float64),
        sim_candidate_limit,
        sim_threshold,
        gap_threshold,
        verbose,
    )

    alpha = initial_alpha
    for _ in range(iterations):
        forces = np.zeros_like(pos)
        forces += anchor_strength * (home_coords - pos)

        if len(attract_pairs) > 0:
            _apply_attraction(pos, attract_pairs, sim_attraction_strength, forces)

        pos += alpha * forces

        for _ in range(collision_iterations):
            _resolve_variable_collisions(pos, radii, collision_padding, pair_indices)

        alpha *= alpha_decay

    for _ in range(final_collision_iterations):
        overlap = _resolve_variable_collisions(pos, radii, collision_padding, pair_indices)
        if overlap <= AGGREGATE_COLLISION_EPSILON:
            break

    return pos


def build_aggregate_layouts(
    papers: list[dict[str, Any]],
    paper_coords: np.ndarray,
    embeddings: np.ndarray,
    nav_order: dict[str, Any],
    force_params: dict[str, Any],
) -> dict[str, dict[str, list[float]]]:
    """Precompute aggregate LOD positions so the browser avoids layout work."""
    branch_levels = aggregate_branch_levels(papers, nav_order)
    level_indices = {str(level["id"]): int(level["path_index"]) for level in branch_levels}
    branch_depth = len(branch_levels)
    roots: list[AggregateLayoutGroup] = []
    root_map: dict[str, AggregateLayoutGroup] = {}
    groups_by_level: dict[str, list[AggregateLayoutGroup]] = {str(level["id"]): [] for level in branch_levels}
    embedding_norm = normalize(embeddings.astype(np.float32))

    def ensure_group(
        parent: AggregateLayoutGroup | None,
        label: str,
        level: str,
        path: list[str],
        path_index: int,
    ) -> AggregateLayoutGroup:
        group_map = parent.child_map if parent else root_map
        if label in group_map:
            return group_map[label]

        group = AggregateLayoutGroup(
            level=level,
            label=label,
            path=path,
            path_index=path_index,
            parent=parent,
        )
        group_map[label] = group
        groups_by_level[level].append(group)
        if parent:
            parent.children.append(group)
        else:
            roots.append(group)
        return group

    for paper_index, paper in enumerate(papers):
        path = padded_aggregate_nav_path(paper.get("nav_path") or [], branch_depth)
        parent = None

        for level_index, level_info in enumerate(branch_levels):
            label = path[level_index] or path[-1] or UNCATEGORIZED_CATEGORY
            path_prefix = path[: level_index + 1]
            level = str(level_info["id"])
            group = ensure_group(parent, label, level, path_prefix, level_index)

            x = float(paper_coords[paper_index, 0])
            y = float(paper_coords[paper_index, 1])
            group.leaf_indices.append(paper_index)
            group.x += x
            group.y += y
            group.leaf_points.append((x, y))
            parent = group

    root_total_x = sum(group.x for group in roots)
    root_total_y = sum(group.y for group in roots)
    root_count = sum(len(group.leaf_indices) for group in roots)
    global_centroid = (root_total_x / root_count, root_total_y / root_count) if root_count else (0.0, 0.0)

    def visit(group: AggregateLayoutGroup, parent_centroid: tuple[float, float] | None = None) -> None:
        reference_point = parent_centroid or global_centroid
        layout_x, layout_y = biased_aggregate_position(group, reference_point)
        centroid_x, centroid_y = hierarchy_group_centroid(group)
        group.layout_x = layout_x
        group.layout_y = layout_y
        group.centroid_x = centroid_x
        group.centroid_y = centroid_y

        for child in group.children:
            visit(child, (centroid_x, centroid_y))

    for root in roots:
        visit(root)

    for groups in groups_by_level.values():
        if len(groups) < 2:
            continue

        home_coords = np.array(
            [[group.layout_x, group.layout_y] for group in groups],
            dtype=np.float64,
        )
        radii = np.array(
            [aggregate_node_size(len(group.leaf_indices), group.level, level_indices) for group in groups],
            dtype=np.float64,
        )
        aggregate_embeddings = np.vstack([embedding_norm[group.leaf_indices].mean(axis=0) for group in groups])
        layout_coords = aggregate_force_layout_postprocess(
            home_coords,
            aggregate_embeddings,
            radii,
            **force_params,
        )

        for group, coords in zip(groups, layout_coords, strict=False):
            group.layout_x = float(coords[0])
            group.layout_y = float(coords[1])

    return {
        level: {
            aggregate_group_key(group.path): [
                round(group.layout_x if group.layout_x is not None else group.x, 1),
                round(group.layout_y if group.layout_y is not None else group.y, 1),
            ]
            for group in groups
        }
        for level, groups in groups_by_level.items()
    }


# ---------------------------------------------------------------------------
# Navigation parsing — paper_id → tree category
# ---------------------------------------------------------------------------

UNCATEGORIZED_CATEGORY = "Uncategorized"


def find_tree_nav(config: dict[str, Any]) -> object | None:
    """Return the nav subtree under ``Tree`` if present."""
    return load_tree(config)


def parse_nav_categories(config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """
    Recursively walk the mkdocs ``Tree`` nav and record each paper's
    full tree branch path, plus legacy category fields used by the
    existing map filters and colour palette.

    The first branch level under ``Tree`` is the super-category level:

        Tree → Decision-Making → Optimization → Toolboxes & Solvers → ...

    This keeps the Map hierarchy synchronized with the MkDocs Tree instead
    of maintaining a separate list of super-categories.

    Returns a dict mapping paper_id to:

        {
            "super_category": str | None,
            "category": str,
            "sub_category": str | None,
            "nav_path": [str, ...],
        }
    """
    tree = find_tree_nav(config)
    if tree is None:
        return {}
    return TreeModel.from_tree(tree).placement_fields_by_paper_id()


def parse_nav_category_order(config: dict[str, Any]) -> dict[str, Any]:
    """
    Walk the mkdocs ``Tree`` nav and return ordered hierarchy lists as
    they appear in mkdocs.yml (not alphabetically).

    Returns:
        {
            "superCategories": [str, ...],
            "categories": [str, ...],
            "categorySuperCategory": {"<category>": "<super-category>" | None, ...},
            "subCategoryOrder": {"<category>": [str, ...], ...},
            "navPathOrder": [["<branch>", ...], ...],
            "maxBranchDepth": int,
        }
    """
    tree = find_tree_nav(config)
    if tree is None:
        return TreeModel.from_tree([]).order.category_order_fields()
    return TreeModel.from_tree(tree).order.category_order_fields()


# ---------------------------------------------------------------------------
# Embedding backends
# ---------------------------------------------------------------------------


def embed_voyage(texts: list[str], model: str = "voyage-3-large") -> np.ndarray:
    """
    Embed *texts* using the Voyage AI API.

    Requires:
        pip install voyageai
        export VOYAGE_API_KEY=va-...

    The API is called in batches of up to 128 texts (the per-request limit).
    """
    import voyageai  # type: ignore[import]

    api_key = os.environ["VOYAGE_API_KEY"]
    client = voyageai.Client(api_key=api_key)

    batch_size = 128
    all_embeddings: list[list[float]] = []
    n_batches = (len(texts) - 1) // batch_size + 1

    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        batch_num = i // batch_size + 1
        print(f"    Voyage AI batch {batch_num}/{n_batches} ({len(batch)} texts)…")
        result = client.embed(batch, model=model, input_type="document")
        all_embeddings.extend(result.embeddings)

    return np.array(all_embeddings, dtype=np.float32)


def embed_fastembed(
    texts: list[str],
    model: str = "mixedbread-ai/mxbai-embed-large-v1",
) -> np.ndarray:
    """
    Embed *texts* using fastembed (local ONNX inference, no API key needed).

    Requires:
        pip install fastembed

    The model is downloaded from HuggingFace on first use and cached in
    ``~/.cache/fastembed``.  Subsequent runs use the cached copy.

    ``mixedbread-ai/mxbai-embed-large-v1`` (1024-d) is the default because
    it is at the top of the open-source MTEB leaderboard for semantic
    similarity as of 2025 and produces embeddings competitive with many
    commercial APIs.
    """
    from fastembed import TextEmbedding  # type: ignore[import]

    print(f"    Loading fastembed model: {model}")
    print("    (First run downloads the model; subsequent runs use the cache.)")
    embedder = TextEmbedding(model)
    print(f"    Embedding {len(texts)} texts…")
    vecs = list(embedder.embed(texts, batch_size=32))
    return np.array(vecs, dtype=np.float32)


def choose_backend(requested: str | None) -> tuple[str, Callable[[list[str]], np.ndarray]]:
    """
    Select the embedding backend.

    Returns (backend_name, embed_function).  The embed function has the
    signature: ``fn(texts: list[str]) -> np.ndarray``.
    """
    if requested == "voyage" or (requested is None and os.environ.get("VOYAGE_API_KEY")):
        if importlib.util.find_spec("voyageai") is None:
            print("WARNING: voyageai package not installed. Falling back to fastembed.")
            print("         Install with: pip install voyageai")
        else:
            print("Backend: Voyage AI voyage-3-large")
            return "voyage-3-large", embed_voyage

    if requested == "voyage":
        sys.exit("ERROR: --backend voyage requested but VOYAGE_API_KEY is not set or voyageai is not installed.")

    # fastembed fallback
    try:
        import fastembed  # noqa: F401
    except ImportError:
        sys.exit(
            "ERROR: Neither Voyage AI nor fastembed is available.\n"
            "  Install fastembed:  pip install fastembed\n"
            "  Or set VOYAGE_API_KEY and install voyageai: pip install voyageai"
        )

    model = "mixedbread-ai/mxbai-embed-large-v1"
    print(f"Backend: fastembed {model} (local ONNX)")
    return model, lambda texts: embed_fastembed(texts, model)


# ---------------------------------------------------------------------------
# Cache helpers
# ---------------------------------------------------------------------------


def load_cache(cache_path: Path) -> dict[str, Any]:
    """
    Load the embedding cache from disk.

    Cache schema::

        {
          "model": "<model name>",
          "papers": {
            "<paper_id>": {
              "hash": "<16-char hex>",
              "embedding": [<float>, ...]
            }
          },
          "umap": {
            "key": "<24-char hex — hash of paper IDs + embeddings + UMAP params>",
            "coords": [[x, y], ...]
          },
          "force": {
            "key": "<24-char hex — hash of UMAP coords + embeddings + force params>",
            "coords": [[x, y], ...]
          }
        }
    """
    if cache_path.exists():
        with open(cache_path, encoding="utf-8") as f:
            return json.load(f)
    return {"model": None, "papers": {}}


def save_cache(cache_path: Path, cache: dict[str, Any]) -> None:
    """Persist the full cache dict (embeddings + umap) to disk."""
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(cache, f, separators=(",", ":"))
    size_kb = cache_path.stat().st_size // 1024
    print(f"Cache saved: {cache_path}  ({size_kb} KB)")


def prune_missing_papers_from_cache(cache: dict[str, Any], active_paper_ids: set[str]) -> list[str]:
    """
    Remove embeddings for papers that no longer have a metadata.yml file.

    The derived layout caches depend on the active paper set, so they are
    invalidated whenever an embedding entry is pruned.
    """
    cached_papers = cache.get("papers")
    if not isinstance(cached_papers, dict):
        cache["papers"] = dict[str, Any]()
        cache.pop("umap", None)
        cache.pop("force", None)
        return []

    stale_ids = sorted(set(cached_papers) - active_paper_ids)
    for paper_id in stale_ids:
        del cached_papers[paper_id]

    if stale_ids:
        cache.pop("umap", None)
        cache.pop("force", None)

    return stale_ids


# ---------------------------------------------------------------------------
# Cosine similarity
# ---------------------------------------------------------------------------


def cosine_similarity_matrix(embeddings: np.ndarray) -> np.ndarray:
    """Return the (n × n) pairwise cosine similarity matrix."""
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    normalised = embeddings / np.clip(norms, 1e-10, None)
    return (normalised @ normalised.T).astype(np.float32)


def quantile_unitize_similarity_matrix(similarity: np.ndarray) -> tuple[np.ndarray, dict[str, object]]:
    """
    Map raw cosine similarities to empirical quantile scores in [0, 1].

    This is a nonparametric monotone transform.  Each distinct cosine value is
    mapped to the midpoint of its empirical rank interval, with the smallest
    observed value forced to 0 and the largest observed value forced to 1.  The
    exported semantic similarity therefore spans the full slider range and has
    an approximately uniform marginal distribution.
    """
    flat = np.asarray(similarity, dtype=np.float64).ravel()
    finite = flat[np.isfinite(flat)]
    if finite.size == 0:
        mapped = np.zeros_like(similarity, dtype=np.float32)
        return mapped, {
            "method": "empirical-quantile",
            "source": "cosine",
            "sourceMin": None,
            "sourceMax": None,
        }

    unique, counts = np.unique(finite, return_counts=True)
    if unique.size == 1:
        mapped = np.ones_like(similarity, dtype=np.float32)
        return mapped, {
            "method": "empirical-quantile",
            "source": "cosine",
            "sourceMin": round(float(unique[0]), 6),
            "sourceMax": round(float(unique[0]), 6),
        }

    starts = np.cumsum(counts) - counts
    quantiles = (starts + (counts - 1) / 2) / (finite.size - 1)
    quantiles[0] = 0.0
    quantiles[-1] = 1.0

    mapped = np.interp(flat, unique, quantiles).reshape(similarity.shape)
    mapped = np.clip(mapped, 0.0, 1.0).astype(np.float32)
    return mapped, {
        "method": "empirical-quantile",
        "source": "cosine",
        "sourceMin": round(float(unique[0]), 6),
        "sourceMax": round(float(unique[-1]), 6),
    }


# ---------------------------------------------------------------------------
# Tree proximity scale
# ---------------------------------------------------------------------------


def common_prefix_length(a: list[str], b: list[str]) -> int:
    """Return the number of matching leading path components."""
    return tree_common_prefix_length(tuple(a), tuple(b))


def tree_distance(a: list[str], b: list[str]) -> int:
    """Return tree distance between two nav paths."""
    return tree_model_distance(tuple(a), tuple(b))


def learn_tree_proximity_scale(
    semantic_values: np.ndarray,
    tree_distances: np.ndarray,
    max_tree_distance: int,
) -> list[float]:
    """
    Learn a monotone distance→proximity lookup by quantile matching.

    Distances are discrete, so each distance bucket receives the semantic
    similarity quantile at the midpoint of that bucket's empirical mass.
    This nonparametric transform makes the marginal tree-proximity
    distribution as close as a discrete monotone lookup can get to the
    semantic-similarity distribution.
    """
    semantic_values = np.asarray(semantic_values, dtype=np.float64)
    semantic_values = semantic_values[np.isfinite(semantic_values)]
    semantic_values = np.clip(semantic_values, 0.0, 1.0)

    tree_distances = np.asarray(tree_distances, dtype=np.int16)
    distance_counts = np.bincount(
        np.clip(tree_distances, 0, max_tree_distance),
        minlength=max_tree_distance + 1,
    )

    if semantic_values.size == 0 or not int(distance_counts.sum()):
        return [
            round(1 - distance / max_tree_distance, 4) if max_tree_distance else 1.0
            for distance in range(max_tree_distance + 1)
        ]

    total = int(distance_counts.sum())
    scale: list[float] = []
    closer_count = 0
    for count in distance_counts:
        midpoint = closer_count + int(count) / 2
        quantile = 1 - midpoint / total
        scale.append(float(np.quantile(semantic_values, np.clip(quantile, 0.0, 1.0))))
        closer_count += int(count)

    scale[0] = 1.0
    for distance in range(1, len(scale)):
        scale[distance] = min(scale[distance], scale[distance - 1])

    return [round(float(np.clip(value, 0.0, 1.0)), 4) for value in scale]


def kl_divergence(
    reference_values: np.ndarray,
    candidate_values: np.ndarray,
    bins: int = TREE_PROXIMITY_HISTOGRAM_BINS,
    epsilon: float = 1e-12,
) -> float:
    """Return KL(reference || candidate) over fixed 0..1 histogram bins."""
    reference_hist, _ = np.histogram(
        np.clip(reference_values, 0.0, 1.0),
        bins=bins,
        range=(0.0, 1.0),
    )
    candidate_hist, _ = np.histogram(
        np.clip(candidate_values, 0.0, 1.0),
        bins=bins,
        range=(0.0, 1.0),
    )
    p = reference_hist.astype(np.float64) + epsilon
    q = candidate_hist.astype(np.float64) + epsilon
    p /= p.sum()
    q /= q.sum()
    return float(np.sum(p * np.log(p / q)))


def tree_proximity_metadata(
    papers: list[dict[str, Any]],
    similarity_rows: np.ndarray,
    similarity_scale: int,
) -> dict[str, object]:
    """Build precomputed tree-proximity metadata consumed by the browser."""
    paths = [p.get("nav_path") or [UNCATEGORIZED_CATEGORY] for p in papers]
    max_tree_distance = max(1, max(len(path) for path in paths) * 2)
    n = len(paths)

    tree_distances = np.empty((n, n), dtype=np.int16)
    for i, left in enumerate(paths):
        for j, right in enumerate(paths):
            tree_distances[i, j] = tree_distance(left, right)

    semantic_values = np.clip(
        similarity_rows.astype(np.float64) / similarity_scale,
        0.0,
        1.0,
    )
    scale = learn_tree_proximity_scale(
        semantic_values.ravel(),
        tree_distances.ravel(),
        max_tree_distance,
    )
    proximity_values = np.take(np.array(scale, dtype=np.float64), tree_distances)

    return {
        "scale": scale,
        "maxDistance": max_tree_distance,
        "method": "quantile-matched-tree-distance",
        "histogramBins": TREE_PROXIMITY_HISTOGRAM_BINS,
        "klDivergence": round(
            kl_divergence(semantic_values.ravel(), proximity_values.ravel()),
            6,
        ),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Sigma.js map data from paper embeddings.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--backend",
        choices=["voyage", "fastembed"],
        default=None,
        help="Force a specific embedding backend (default: auto-select).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Ignore the embedding cache and re-embed every paper.",
    )
    parser.add_argument(
        "--cache",
        type=Path,
        default=DEFAULT_CACHE,
        help=f"Path to the embedding cache file (default: {DEFAULT_CACHE}).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Path to the output JS file (default: {DEFAULT_OUTPUT}).",
    )
    parser.add_argument(
        "--skip-force-layout",
        action="store_true",
        dest="skip_force_layout",
        help="Skip the force-directed post-processing step after UMAP.",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("Knowledge Base — Map Data Generator")
    print("=" * 60)

    # ---- load config -------------------------------------------------------
    with open(MKDOCS_YML, encoding="utf-8") as f:
        config = yaml.safe_load(f)
    paper_to_category = parse_nav_categories(config)
    nav_order = parse_nav_category_order(config)

    # ---- collect papers ----------------------------------------------------
    print("\n[1/7] Collecting paper metadata…")
    papers: list[dict[str, Any]] = []
    catalog = Catalog.from_metadata_root(METADATA_ROOT)
    for entry in catalog.entries:
        pid = entry.id

        cat_info = paper_to_category.get(
            pid,
            {
                "super_category": None,
                "category": UNCATEGORIZED_CATEGORY,
                "sub_category": None,
                "nav_path": [UNCATEGORIZED_CATEGORY],
            },
        )
        papers.append(
            {
                "id": pid,
                "title": entry.title,
                "label": entry.label,
                "authors": list(entry.author_last_names[:3]),
                "year": entry.year,
                "item_type": entry.type or "Unspecified",
                "super_category": cat_info["super_category"],
                "category": cat_info["category"],
                "sub_category": cat_info["sub_category"],
                "nav_path": cat_info.get("nav_path") or [cat_info["category"]],
                "tags": list(entry.tags),
                "summary": entry.summary,
                "abstract": entry.abstract,
                "link": entry.primary_link,
                "embed_text": entry.embedding_text,
                "hash": entry.embedding_hash,
            }
        )

    print(f"    Found {len(papers)} papers")

    # ---- choose backend ----------------------------------------------------
    print("\n[2/7] Selecting embedding backend…")
    model_name, embed_fn = choose_backend(args.backend)

    # ---- load cache and find which papers need (re-)embedding --------------
    print("\n[3/7] Checking embedding cache…")
    cache: dict[str, Any] = load_cache(args.cache)

    # Invalidate entire cache if the model changed
    if cache.get("model") and cache["model"] != model_name:
        print(f"    Model changed ({cache['model']} → {model_name}). Discarding cache and re-embedding all papers.")
        cache = {"model": model_name, "papers": dict[str, dict[str, Any]]()}

    cached_papers_raw = cache.get("papers")
    cached_papers: dict[str, dict[str, Any]] = (
        {str(paper_id): dict(entry) for paper_id, entry in cached_papers_raw.items() if isinstance(entry, dict)}
        if isinstance(cached_papers_raw, dict)
        else {}
    )
    active_paper_ids = {p["id"] for p in papers}
    pruned_ids = prune_missing_papers_from_cache(cache, active_paper_ids)
    if pruned_ids:
        print(f"    Removed {len(pruned_ids)} stale cached paper(s) with no metadata.yml")
        cached_papers_raw = cache.get("papers")
        cached_papers = (
            {str(paper_id): dict(entry) for paper_id, entry in cached_papers_raw.items() if isinstance(entry, dict)}
            if isinstance(cached_papers_raw, dict)
            else {}
        )

    # Determine which papers need new embeddings
    to_embed: list[int] = []  # indices into `papers`
    for i, p in enumerate(papers):
        cached = cached_papers.get(p["id"])
        if args.force or cached is None or cached.get("hash") != p["hash"]:
            to_embed.append(i)

    if to_embed:
        print(f"    {len(to_embed)} paper(s) need (re-)embedding  ({len(papers) - len(to_embed)} cached)")
    else:
        print(f"    All {len(papers)} papers are cached — skipping embedding API call")

    # ---- generate embeddings -----------------------------------------------
    print("\n[4/7] Generating embeddings…")
    if to_embed:
        texts = [papers[i]["embed_text"] for i in to_embed]
        new_embeddings = embed_fn(texts)

        for idx, paper_idx in enumerate(to_embed):
            p = papers[paper_idx]
            cached_papers[p["id"]] = {
                "hash": p["hash"],
                "embedding": new_embeddings[idx].tolist(),
            }

        cache["model"] = model_name
        cache["papers"] = cached_papers
        # Invalidate UMAP cache whenever embeddings change
        cache.pop("umap", None)
        cache.pop("force", None)
        save_cache(args.cache, cache)
    elif pruned_ids:
        cache["model"] = model_name
        cache["papers"] = cached_papers
        save_cache(args.cache, cache)
    else:
        print("    (nothing to do)")

    # Assemble full embedding matrix in paper order
    embedding_list = [cached_papers[p["id"]]["embedding"] for p in papers]
    embeddings = np.array(embedding_list, dtype=np.float32)
    print(f"    Embedding matrix: {embeddings.shape}")

    # ---- UMAP layout -------------------------------------------------------
    print("\n[5/7] Computing UMAP 2-D layout…")

    umap_params: dict[str, Any] = {
        "scale": DEFAULT_UMAP_SCALE,
        "random_state": 42,
        "n_neighbors": min(50, len(embeddings) - 1),
        "min_dist": 0.05,
        "n_epochs": 500,
    }
    key = umap_cache_key([p["id"] for p in papers], embeddings, **umap_params)
    umap_entry_raw = cache.get("umap")
    umap_entry: dict[str, Any] = umap_entry_raw if isinstance(umap_entry_raw, dict) else dict[str, Any]()

    if not args.force and umap_entry.get("key") == key:
        print("    UMAP layout loaded from cache (embeddings unchanged)")
        umap_coords = np.array(umap_entry["coords"], dtype=np.float64)
    else:
        umap_coords = compute_umap_positions(embeddings, **umap_params)
        cache["umap"] = {"key": key, "coords": umap_coords.tolist()}
        save_cache(args.cache, cache)

    print(
        f"    UMAP coords: {umap_coords.shape}  range x=[{umap_coords[:, 0].min():.0f}, {umap_coords[:, 0].max():.0f}]  y=[{umap_coords[:, 1].min():.0f}, {umap_coords[:, 1].max():.0f}]"
    )

    # ---- force-directed layout post-processing -----------------------------
    print("\n[6/7] Force-directed layout post-processing…")

    force_params: dict[str, Any] = {
        "pre_layout_scale": 2.0,
        "anchor_strength": 0.85,
        "sim_threshold": 0.75,
        "sim_candidate_limit": 10,
        "sim_attraction_strength": 0.4,
        "gap_factor": 2.0,
        "collision_radius_factor": 0.2,
        "collision_iterations": 3,
        "iterations": 120,
        "initial_alpha": 0.3,
        "alpha_decay": 0.98,
        "post_scale": 1.0,
    }

    if args.skip_force_layout:
        print("    Skipped (--skip-force-layout)")
        layout_coords = umap_coords
    else:
        fkey = force_cache_key(umap_coords, embeddings, **force_params)
        force_entry_raw = cache.get("force")
        force_entry: dict[str, Any] = force_entry_raw if isinstance(force_entry_raw, dict) else dict[str, Any]()

        if not args.force and force_entry.get("key") == fkey:
            print("    Force layout loaded from cache (UMAP + embeddings unchanged)")
            layout_coords = np.array(force_entry["coords"], dtype=np.float64)
        else:
            layout_coords = force_layout_postprocess(umap_coords, embeddings, verbose=True, **force_params)
            cache["force"] = {"key": fkey, "coords": layout_coords.tolist()}
            save_cache(args.cache, cache)

        print(
            f"    Force coords: {layout_coords.shape}  range x=[{layout_coords[:, 0].min():.0f}, {layout_coords[:, 0].max():.0f}]  y=[{layout_coords[:, 1].min():.0f}, {layout_coords[:, 1].max():.0f}]"
        )

    # ---- build browser data -----------------------------------------------
    print("\n[7/7] Building map data and writing output…")

    raw_sim = cosine_similarity_matrix(embeddings)
    sim, similarity_transform = quantile_unitize_similarity_matrix(raw_sim)
    similarity_rows = np.clip(
        np.rint(sim * SIMILARITY_EXPORT_SCALE),
        0,
        SIMILARITY_EXPORT_SCALE,
    ).astype(np.int16)
    tree_proximity = tree_proximity_metadata(
        papers,
        similarity_rows,
        SIMILARITY_EXPORT_SCALE,
    )

    nodes = [
        {
            "data": {
                "id": p["id"],
                "label": p["label"],
                "title": p["title"],
                "authors": p["authors"],
                "year": p["year"],
                "item_type": p["item_type"],
                "super_category": p["super_category"],
                "category": p["category"],
                "sub_category": p["sub_category"],
                "nav_path": p["nav_path"],
                "tags": p["tags"],
                "summary": p["summary"],
                "abstract": p["abstract"],
                "link": p["link"],
            },
            "position": {
                "x": round(float(layout_coords[i, 0]), 1),
                "y": round(float(layout_coords[i, 1]), 1),
            },
        }
        for i, p in enumerate(papers)
    ]

    print("    Precomputing aggregate LOD layouts…")
    node_coords = np.array(
        [[node["position"]["x"], node["position"]["y"]] for node in nodes],
        dtype=np.float64,
    )
    aggregate_force_params = {
        "anchor_strength": force_params["anchor_strength"],
        "sim_threshold": force_params["sim_threshold"],
        "sim_candidate_limit": force_params["sim_candidate_limit"],
        "sim_attraction_strength": force_params["sim_attraction_strength"],
        "gap_factor": force_params["gap_factor"],
        "collision_padding": AGGREGATE_COLLISION_PADDING,
        "collision_iterations": force_params["collision_iterations"],
        "final_collision_iterations": AGGREGATE_FINAL_COLLISION_ITERATIONS,
        "iterations": force_params["iterations"],
        "initial_alpha": force_params["initial_alpha"],
        "alpha_decay": force_params["alpha_decay"],
    }
    aggregate_layouts = build_aggregate_layouts(
        papers,
        node_coords,
        embeddings,
        nav_order,
        aggregate_force_params,
    )

    graph_data = {
        "nodes": nodes,
        "similarity": {
            "scale": SIMILARITY_EXPORT_SCALE,
            "ids": [p["id"] for p in papers],
            "rows": similarity_rows.tolist(),
        },
        "meta": {
            "model": model_name,
            "similarityScale": SIMILARITY_EXPORT_SCALE,
            "similarityTransform": similarity_transform,
            "total_papers": len(papers),
            "itemTypeOrder": sorted({p["item_type"] for p in papers}),
            "superCategoryOrder": nav_order["superCategories"],
            "categoryOrder": nav_order["categories"],
            "categorySuperCategory": nav_order["categorySuperCategory"],
            "subCategoryOrder": nav_order["subCategoryOrder"],
            "navPathOrder": nav_order["navPathOrder"],
            "maxBranchDepth": nav_order["maxBranchDepth"],
            "aggregateLayouts": aggregate_layouts,
            "treeProximity": tree_proximity,
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    js = f"const mapData={json.dumps(graph_data, ensure_ascii=False, separators=(',', ':'))};\n"
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(js)

    print(f"    Nodes : {len(nodes)}")
    print(
        f"    Similarity matrix: exported ({similarity_transform['method']} {similarity_transform['source']} → [0, 1])"
    )
    print(f"    Tree proximity scale: exported (KL={tree_proximity['klDivergence']})")
    print(f"    Output: {args.output}")
    print("\nDone!")


if __name__ == "__main__":
    main()
