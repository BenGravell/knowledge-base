"""Map layout computation for paper and aggregate nodes.

UMAP positions are cached under the embedding cache's ``"umap"`` key. The
cache key covers paper IDs, embedding bytes, and UMAP parameters so any changed
layout input invalidates the entry.

Small append-only updates reuse existing coordinates and place new papers near
their nearest cached embedding neighbours. Removals, changed existing papers,
model changes, and larger additions fall back to full deterministic layout.
"""

from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np
from scipy.spatial import KDTree as cKDTree
from sklearn.preprocessing import normalize

from knowledge_base.components.map.pipeline.settings import (
    AGGREGATE_COLLISION_EPSILON,
    AGGREGATE_COLLISION_PADDING,
    AGGREGATE_EXTRA_AREA_FALLBACK_UNITS,
    AGGREGATE_EXTRA_AREA_UNITS_BY_LEVEL,
    AGGREGATE_FINAL_COLLISION_ITERATIONS,
    AGGREGATE_MIN_RADIUS_RATIO,
    AGGREGATE_POSITION_BIAS_BY_LEVEL,
    AGGREGATE_POSITION_OUTER_QUANTILE,
    DEFAULT_UMAP_SCALE,
    INCREMENTAL_LAYOUT_JITTER_RATIO,
    INCREMENTAL_LAYOUT_MAX_ADDED,
    INCREMENTAL_LAYOUT_MAX_ADDED_RATIO,
    INCREMENTAL_LAYOUT_NEIGHBORS,
    LEGACY_BRANCH_LEVEL_IDS,
    PAPER_NODE_RADIUS_TARGET,
    UNCATEGORIZED_CATEGORY,
)
from knowledge_base.embedding_workbench import save_embedding_cache
from knowledge_base.progress import emit_progress


def default_umap_params(embedding_count: int) -> dict[str, Any]:
    return {
        "scale": DEFAULT_UMAP_SCALE,
        "random_state": 42,
        "n_neighbors": min(50, embedding_count - 1),
        "min_dist": 0.05,
        "n_epochs": 500,
    }


def default_force_params() -> dict[str, Any]:
    return {
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


def aggregate_force_params(force_params: dict[str, Any]) -> dict[str, Any]:
    return {
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


def paper_hashes(papers: list[dict[str, Any]]) -> dict[str, str]:
    return {str(paper["id"]): str(paper["hash"]) for paper in papers}


def cache_ids(entry: dict[str, Any]) -> list[str]:
    ids = entry.get("ids")
    return [str(paper_id) for paper_id in ids] if isinstance(ids, list) else []


def cache_hashes(entry: dict[str, Any]) -> dict[str, str]:
    hashes = entry.get("hashes")
    return {str(paper_id): str(value) for paper_id, value in hashes.items()} if isinstance(hashes, dict) else {}


def added_only_cache_hit(
    entry: dict[str, Any],
    papers: list[dict[str, Any]],
) -> tuple[list[str], list[str]] | None:
    previous_ids = cache_ids(entry)
    previous_hashes = cache_hashes(entry)
    if not previous_ids or not previous_hashes:
        return None

    current_ids = [str(paper["id"]) for paper in papers]
    current_hashes = paper_hashes(papers)
    previous_set = set(previous_ids)
    current_set = set(current_ids)
    if not previous_set < current_set:
        return None
    if any(current_hashes.get(paper_id) != previous_hashes.get(paper_id) for paper_id in previous_ids):
        return None

    added_ids = [paper_id for paper_id in current_ids if paper_id not in previous_set]
    max_added = max(1, min(INCREMENTAL_LAYOUT_MAX_ADDED, int(len(previous_ids) * INCREMENTAL_LAYOUT_MAX_ADDED_RATIO)))
    if not added_ids or len(added_ids) > max_added:
        return None
    return previous_ids, added_ids


def deterministic_layout_jitter(paper_id: str, scale: float) -> tuple[float, float]:
    digest = hashlib.sha256(paper_id.encode("utf-8")).digest()
    angle_seed = int.from_bytes(digest[:8], "little") / 2**64
    radius_seed = int.from_bytes(digest[8:16], "little") / 2**64
    angle = angle_seed * np.pi * 2
    radius = scale * (0.45 + 0.55 * radius_seed)
    return float(np.cos(angle) * radius), float(np.sin(angle) * radius)


def median_neighbor_distance(coords: np.ndarray) -> float:
    if len(coords) < 2:
        return 20.0
    tree = cKDTree(coords)
    nn_dists, _ = tree.query(coords, k=2)
    value = float(np.median(nn_dists[:, 1]))
    return value if np.isfinite(value) and value > 0 else 20.0


def incremental_neighbor_positions(
    *,
    current_ids: list[str],
    embeddings: np.ndarray,
    previous_ids: list[str],
    previous_coords: np.ndarray,
) -> np.ndarray:
    """Keep previous coordinates and place new IDs near embedding neighbours."""
    current_index = {paper_id: index for index, paper_id in enumerate(current_ids)}
    previous_index = {paper_id: index for index, paper_id in enumerate(previous_ids)}
    previous_embedding_indexes = [current_index[paper_id] for paper_id in previous_ids if paper_id in current_index]
    if not previous_embedding_indexes:
        raise ValueError("Incremental layout needs at least one previous embedding")

    previous_embeddings = normalize(embeddings[previous_embedding_indexes].astype(np.float32))
    old_coords = np.asarray(previous_coords, dtype=np.float64)
    coords = np.empty((len(current_ids), 2), dtype=np.float64)
    jitter_scale = median_neighbor_distance(old_coords) * INCREMENTAL_LAYOUT_JITTER_RATIO

    for paper_id, target_index in current_index.items():
        old_index = previous_index.get(paper_id)
        if old_index is not None:
            coords[target_index] = old_coords[old_index]
            continue

        query = normalize(embeddings[target_index : target_index + 1].astype(np.float32))[0]
        similarities = previous_embeddings @ query
        k = min(INCREMENTAL_LAYOUT_NEIGHBORS, len(similarities))
        neighbor_indexes = np.argpartition(similarities, -k)[-k:]
        weights = np.clip(similarities[neighbor_indexes], 0.0, None).astype(np.float64)
        if not np.any(weights):
            weights = np.ones(k, dtype=np.float64)
        base = np.average(old_coords[neighbor_indexes], axis=0, weights=weights)
        jitter = deterministic_layout_jitter(paper_id, jitter_scale)
        coords[target_index] = base + jitter

    return coords


def coord_range(label: str, coords: np.ndarray) -> str:
    return (
        f"    {label} coords: {coords.shape}  "
        f"range x=[{coords[:, 0].min():.0f}, {coords[:, 0].max():.0f}]  "
        f"y=[{coords[:, 1].min():.0f}, {coords[:, 1].max():.0f}]"
    )


def layout_cache_entry(
    *,
    key: str,
    paper_ids: list[str],
    hashes: dict[str, str],
    coords: np.ndarray,
    placement: str,
) -> dict[str, Any]:
    return {
        "key": key,
        "ids": paper_ids,
        "hashes": hashes,
        "coords": coords.tolist(),
        "placement": placement,
    }


def backfill_layout_cache_entry(
    cache: dict[str, Any],
    cache_path: Path,
    name: str,
    entry: dict[str, Any],
    paper_ids: list[str],
    hashes: dict[str, str],
    placement: str,
) -> None:
    if cache_ids(entry) and cache_hashes(entry):
        return
    cache[name] = {
        **entry,
        "ids": paper_ids,
        "hashes": hashes,
        "placement": entry.get("placement") or placement,
    }
    save_embedding_cache(cache_path, cache)


def load_or_build_umap_layout(
    *,
    cache: dict[str, Any],
    cache_path: Path,
    papers: list[dict[str, Any]],
    embeddings: np.ndarray,
    force: bool,
) -> np.ndarray:
    params = default_umap_params(len(embeddings))
    paper_ids = [str(paper["id"]) for paper in papers]
    current_hashes = paper_hashes(papers)
    key = umap_cache_key(paper_ids, embeddings, **params)
    entry_raw = cache.get("umap")
    entry: dict[str, Any] = entry_raw if isinstance(entry_raw, dict) else dict[str, Any]()

    if not force and entry.get("key") == key:
        print("    UMAP layout loaded from cache (embeddings unchanged)")
        coords = np.array(entry["coords"], dtype=np.float64)
        backfill_layout_cache_entry(cache, cache_path, "umap", entry, paper_ids, current_hashes, "umap")
        print(coord_range("UMAP", coords))
        return coords

    incremental = None if force else added_only_cache_hit(entry, papers)
    if incremental is not None:
        previous_ids, added_ids = incremental
        print(f"    UMAP layout incrementally extended for {len(added_ids)} added paper(s)")
        coords = incremental_neighbor_positions(
            current_ids=paper_ids,
            embeddings=embeddings,
            previous_ids=previous_ids,
            previous_coords=np.array(entry["coords"], dtype=np.float64),
        )
    else:
        coords = compute_umap_positions(embeddings, **params)

    cache["umap"] = layout_cache_entry(
        key=key,
        paper_ids=paper_ids,
        hashes=current_hashes,
        coords=coords,
        placement="incremental-nearest-neighbors" if incremental is not None else "umap",
    )
    save_embedding_cache(cache_path, cache)
    print(coord_range("UMAP", coords))
    return coords


def load_or_build_force_layout(
    *,
    cache: dict[str, Any],
    cache_path: Path,
    papers: list[dict[str, Any]],
    umap_coords: np.ndarray,
    embeddings: np.ndarray,
    force: bool,
    force_params: dict[str, Any],
) -> np.ndarray:
    paper_ids = [str(paper["id"]) for paper in papers]
    current_hashes = paper_hashes(papers)
    key = force_cache_key(umap_coords, embeddings, **force_params)
    entry_raw = cache.get("force")
    entry: dict[str, Any] = entry_raw if isinstance(entry_raw, dict) else dict[str, Any]()

    if not force and entry.get("key") == key:
        print("    Force layout loaded from cache (UMAP + embeddings unchanged)")
        coords = np.array(entry["coords"], dtype=np.float64)
        backfill_layout_cache_entry(cache, cache_path, "force", entry, paper_ids, current_hashes, "force")
        print(coord_range("Force", coords))
        return coords

    incremental = None if force else added_only_cache_hit(entry, papers)
    if incremental is not None:
        previous_ids, added_ids = incremental
        print(f"    Force layout incrementally extended for {len(added_ids)} added paper(s)")
        coords = incremental_neighbor_positions(
            current_ids=paper_ids,
            embeddings=embeddings,
            previous_ids=previous_ids,
            previous_coords=np.array(entry["coords"], dtype=np.float64),
        )
    else:
        coords = force_layout_postprocess(umap_coords, embeddings, verbose=True, **force_params)

    cache["force"] = layout_cache_entry(
        key=key,
        paper_ids=paper_ids,
        hashes=current_hashes,
        coords=coords,
        placement="incremental-nearest-neighbors" if incremental is not None else "force",
    )
    save_embedding_cache(cache_path, cache)
    print(coord_range("Force", coords))
    return coords


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

        if verbose and (it % 10 == 0 or it == iterations - 1):
            drift = np.mean(np.linalg.norm(pos - home, axis=1))
            print(f"    [force_layout] iter {it:4d}  alpha={alpha:.4f}  mean drift from UMAP = {drift:.4f}")
            emit_progress(it + 1, iterations, "Force layout iterations")

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
    for iteration in range(iterations):
        forces = np.zeros_like(pos)
        forces += anchor_strength * (home_coords - pos)

        if len(attract_pairs) > 0:
            _apply_attraction(pos, attract_pairs, sim_attraction_strength, forces)

        pos += alpha * forces

        for _ in range(collision_iterations):
            _resolve_variable_collisions(pos, radii, collision_padding, pair_indices)

        alpha *= alpha_decay
        if verbose and (iteration % 20 == 0 or iteration == iterations - 1):
            print(f"    [aggregate_layout] iter {iteration:4d}/{iterations}")
            emit_progress(iteration + 1, iterations, "Aggregate layout iterations")

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
    *,
    verbose: bool = False,
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

    layout_levels = [(level, groups) for level, groups in groups_by_level.items() if len(groups) >= 2]
    for level_index, (level, groups) in enumerate(layout_levels, start=1):
        if len(groups) < 2:
            continue
        if verbose:
            print(f"    Aggregate layout {level_index}/{len(layout_levels)}: {level} ({len(groups)} group(s))")

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
            verbose=verbose,
        )

        for group, coords in zip(groups, layout_coords, strict=False):
            group.layout_x = float(coords[0])
            group.layout_y = float(coords[1])
        emit_progress(level_index, len(layout_levels), "Aggregate layout levels")

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
