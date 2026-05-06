"""
generate_mind_map_data.py
=========================
Generate the Cytoscape.js mind-map data file for the knowledge-base site.

This script reads every paper's ``metadata.yml``, embeds each paper's
text using a high-quality embedding model, computes pairwise cosine
similarities, and writes ``knowledge_base/docs/javascripts/mind-map-data.js``
which the Cytoscape.js visualisation loads at runtime.

Incremental operation
---------------------
Embeddings are expensive to generate.  To avoid re-embedding every paper
each time a few new papers are added, the script maintains a local cache
file (``embedding_cache.json`` by default).  On each run it:

  1. Reads the cache (if it exists).
  2. For every paper computes a *content hash* over the text that will be
     embedded (title + tags + summary + abstract).
  3. Re-embeds only the papers whose hash differs from the cached value or
     which are entirely new.
  4. Writes the updated cache back to disk.
  5. Recomputes the full similarity matrix from the (now complete) set of
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
    python knowledge_base/mind_map/generate_mind_map_data.py

Force full re-embed (ignores cache):
    python knowledge_base/mind_map/generate_mind_map_data.py --force

Choose a specific backend explicitly:
    python generate_mind_map_data.py --backend voyage
    python generate_mind_map_data.py --backend fastembed

Custom similarity threshold and top-K guarantee:
    python knowledge_base/mind_map/generate_mind_map_data.py --threshold 0.82 --top-k 4

Custom paths:
    python knowledge_base/mind_map/generate_mind_map_data.py \\
        --cache knowledge_base/mind_map/my_cache.json \\
        --output knowledge_base/mind_map/mind-map-data.js

Output
------
``knowledge_base/mind_map/mind-map-data.js`` — a JS file that sets the
global ``mindMapData`` variable consumed by mind-map.js.  The MkDocs
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
import json
import math
import os
import re
import sys
import time
from pathlib import Path

import yaml
import numpy as np
from scipy.spatial import cKDTree
from sklearn.preprocessing import normalize

# ---------------------------------------------------------------------------
# Paths (relative to this script's location: knowledge_base/mind_map/)
# ---------------------------------------------------------------------------

MIND_MAP_DIR = Path(__file__).parent          # knowledge_base/mind_map/
KB_DIR       = MIND_MAP_DIR.parent            # knowledge_base/
REPO_ROOT    = KB_DIR.parent                  # repo root
DOCS_DIR     = KB_DIR / "docs"
METADATA_ROOT = DOCS_DIR / "papers"
MKDOCS_YML   = KB_DIR / "mkdocs.yml"
DEFAULT_CACHE  = MIND_MAP_DIR / "embedding_cache.json"
DEFAULT_OUTPUT = MIND_MAP_DIR / "mind-map-data.js"

# ---------------------------------------------------------------------------
# Graph construction parameters (overridable via CLI)
# ---------------------------------------------------------------------------

DEFAULT_THRESHOLD = 0.75   # Minimum cosine similarity to draw an edge
DEFAULT_TOP_K = 5          # Always connect each paper to its top-K neighbours
                           # even if their similarity falls below the threshold
                           # (floor-capped at 0.50 to avoid noisy edges)
ABSOLUTE_FLOOR = 0.50      # Hard minimum similarity; top-K edges below this
                           # are silently dropped

# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

def slugify(name: str) -> str:
    """Lowercase, collapse any run of non-alphanumeric chars to underscore."""
    return re.sub(r"[^a-zA-Z0-9]+", "_", name.lower()).strip("_")


def last_name(author: str) -> str:
    """Extract the last name from an author string."""
    author = author.strip()
    if "," in author:
        return author.split(",")[0].strip()
    parts = author.split()
    return parts[-1] if parts else author


def make_label(data: dict) -> str:
    """
    Node label: algorithm name if present, otherwise
    '<FirstAuthorLastName> [et al.] <year>'.
    """
    algorithm = (data.get("algorithm") or "").strip()
    if algorithm:
        return algorithm
    authors = data.get("authors") or []
    year = data.get("year")
    if not authors:
        return str(year or "")
    name = last_name(authors[0])
    et_al = " et al." if len(authors) > 1 else ""
    year_str = f" {year}" if year else ""
    return f"{name}{et_al}{year_str}"


def paper_id_from_file(metadata_file: Path, data: dict) -> str:
    """Reproduce the ID logic used by generate_papers.py."""
    if "id" in data:
        return slugify(data["id"])
    if metadata_file.stem != "metadata":
        return slugify(metadata_file.stem)
    return slugify(metadata_file.parent.name)


def content_hash(text: str) -> str:
    """SHA-256 of the embedding input text (first 16 hex chars is plenty)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def compute_umap_positions(
    embeddings: "np.ndarray",
    scale: float = 1000.0,
    random_state: int = 42,
    n_neighbors: int | None = None,
    min_dist: float = 0.05,
    n_epochs: int = 500,
) -> "np.ndarray":
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
        min_dist=min_dist,        # tighter packing within clusters
        n_epochs=n_epochs,        # more optimisation steps → better convergence
        random_state=random_state,
    )
    coords = reducer.fit_transform(embeddings).astype(np.float64)
    coords -= coords.mean(axis=0)
    spread = np.abs(coords).max()
    if spread > 0:
        coords = coords / spread * scale
    return coords


def umap_cache_key(
    paper_ids: "list[str]",
    embeddings: "np.ndarray",
    **umap_params,
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
    umap_coords: "np.ndarray",
    embeddings: "np.ndarray",
    **force_params,
) -> str:
    """Stable hash over inputs that fully determine the force layout result."""
    h = hashlib.sha256()
    h.update(umap_coords.tobytes())
    h.update(embeddings.tobytes())
    h.update(json.dumps(force_params, sort_keys=True).encode("utf-8"))
    return h.hexdigest()[:24]


def force_layout_postprocess(
    umap_coords: "np.ndarray",
    embeddings: "np.ndarray",
    *,
    anchor_strength: float = 0.85,
    sim_threshold: float = 0.75,
    sim_top_k: int = 10,
    sim_attraction_strength: float = 0.4,
    gap_factor: float = 2.0,
    collision_radius_factor: float = 0.45,
    collision_iterations: int = 3,
    iterations: int = 120,
    initial_alpha: float = 0.3,
    alpha_decay: float = 0.98,
    post_scale: float = 2.0,
    verbose: bool = True,
    random_seed: int = 42,
) -> "np.ndarray":
    """Post-process UMAP coordinates with a constrained force simulation.

    Three forces act each iteration:

    1. **Anchor** — every node is pulled back toward its original UMAP position
       with strength *anchor_strength*, keeping the global topology intact.
    2. **Similarity attraction** — pairs that are semantically close
       (cosine similarity ≥ *sim_threshold*) but spatially far apart in UMAP
       space (distance > *gap_factor* x median nearest-neighbour distance) are
       pulled together.  Only the *sim_top_k* most similar neighbours per node
       are considered, so the cost is O(N · sim_top_k) per iteration.
    3. **Collision resolution** — after each integration step, overlapping nodes
       are pushed apart until no two nodes are closer than ``2 * collision_radius``,
       where ``collision_radius = sqrt(canvas_area / N) * collision_radius_factor``.

    The step size decays as ``alpha *= alpha_decay`` each iteration, so the
    simulation cools and converges rather than oscillating indefinitely.

    Parameters
    ----------
    umap_coords:
        (N, 2) array of 2-D positions from UMAP, in whatever coordinate scale
        UMAP produced (e.g. ±1000 px).
    embeddings:
        (N, D) array of raw embedding vectors; L2-normalised internally for
        cosine similarity computation.
    anchor_strength:
        Weight of the anchor force pulling nodes back to their UMAP home.
        Higher values preserve UMAP topology more faithfully (range: 0-1).
    sim_threshold:
        Minimum cosine similarity for a pair to receive an attraction force.
    sim_top_k:
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
    random_seed:
        NumPy random seed for reproducibility.

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
    np.random.seed(random_seed)
    N = len(umap_coords)

    if verbose:
        print(f"    [force_layout] N={N}, iterations={iterations}, alpha0={initial_alpha}")

    emb_norm = normalize(embeddings.astype(np.float32))
    home = umap_coords.copy().astype(np.float64)
    pos  = umap_coords.copy().astype(np.float64)

    canvas = np.ptp(pos, axis=0)
    area   = canvas[0] * canvas[1]
    collision_radius = np.sqrt(area / N) * collision_radius_factor
    if verbose:
        print(f"    [force_layout] collision_radius = {collision_radius:.4f}")

    tree_home = cKDTree(home)
    nn_dists, _ = tree_home.query(home, k=2)
    median_nn_dist = np.median(nn_dists[:, 1])
    gap_threshold = gap_factor * median_nn_dist
    if verbose:
        print(f"    [force_layout] median nn dist = {median_nn_dist:.4f}, "
              f"gap threshold = {gap_threshold:.4f}")

    attract_pairs = _build_attraction_pairs(
        emb_norm, home, sim_top_k, sim_threshold, gap_threshold, verbose
    )

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
            print(f"    [force_layout] iter {it:4d}  alpha={alpha:.4f}  "
                  f"mean drift from UMAP = {drift:.4f}")

    if verbose:
        elapsed = time.time() - t0
        final_drift = np.mean(np.linalg.norm(pos - home, axis=1))
        print(f"    [force_layout] done in {elapsed:.2f}s  "
              f"final mean drift = {final_drift:.4f}")

    centroid = pos.mean(axis=0)
    pos = centroid + (pos - centroid) * post_scale
    return pos


def _build_attraction_pairs(
    emb_norm: "np.ndarray",
    home: "np.ndarray",
    top_k: int,
    sim_threshold: float,
    gap_threshold: float,
    verbose: bool,
) -> "np.ndarray":
    N = len(emb_norm)
    sim_matrix = emb_norm @ emb_norm.T

    pairs = []
    for i in range(N):
        sims = sim_matrix[i]
        sims[i] = -1.0
        top_idx = np.argpartition(sims, -top_k)[-top_k:]
        for j in top_idx:
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
    pos: "np.ndarray",
    pairs: "np.ndarray",
    strength: float,
    forces: "np.ndarray",
) -> None:
    i_idx = pairs[:, 0].astype(int)
    j_idx = pairs[:, 1].astype(int)
    weights = pairs[:, 2]

    delta = pos[j_idx] - pos[i_idx]
    dist  = np.linalg.norm(delta, axis=1, keepdims=True) + 1e-8
    unit  = delta / dist
    mag   = strength * weights[:, None]

    np.add.at(forces, i_idx,  mag * unit)
    np.add.at(forces, j_idx, -mag * unit)


def _resolve_collisions(pos: "np.ndarray", radius: float) -> None:
    tree = cKDTree(pos)
    pairs = tree.query_pairs(r=2 * radius, output_type="ndarray")

    if len(pairs) == 0:
        return

    i_idx = pairs[:, 0]
    j_idx = pairs[:, 1]

    delta = pos[i_idx] - pos[j_idx]
    dist  = np.linalg.norm(delta, axis=1, keepdims=True) + 1e-8
    overlap = np.maximum(2 * radius - dist, 0)
    unit  = delta / dist
    correction = 0.5 * overlap * unit

    np.add.at(pos, i_idx,  correction)
    np.add.at(pos, j_idx, -correction)


def build_embed_text(data: dict) -> str:
    """Construct the text that represents a paper for embedding purposes."""
    parts = [
        f"Title: {data.get('title', '')}",
        f"Tags: {', '.join(data.get('tags') or [])}",
        f"Summary: {(data.get('summary') or '').strip()}",
    ]
    abstract = (data.get("abstract") or "").strip()
    if abstract:
        parts.append(f"Abstract: {abstract}")
    return "\n".join(p for p in parts if p.split(": ", 1)[-1].strip())


# ---------------------------------------------------------------------------
# Navigation parsing — paper_id → top-level category
# ---------------------------------------------------------------------------

PLANNING_CATEGORY = "Motion Planning"  # top-level category that receives sub-categories

# Nav sections that act as transparent grouping wrappers: their children are
# treated as top-level categories rather than the wrapper itself.
TRANSPARENT_NAV_SECTIONS = {"Content Tree"}


def parse_nav_categories(config: dict) -> dict[str, dict]:
    """
    Recursively walk the mkdocs ``nav`` tree and record which top-level
    section each paper belongs to, plus a sub-category for Motion Planning
    derived from the 2nd-level nav sections in mkdocs.yml.

    Sections listed in TRANSPARENT_NAV_SECTIONS (e.g. "Content Tree") are
    treated as invisible wrappers: their children are promoted to top-level
    categories instead.

    Returns a dict mapping paper_id → {"category": str, "sub_category": str | None}.
    sub_category is only set for Motion Planning papers; it is None for all others.
    """
    mapping: dict[str, dict] = {}

    def walk(node: object, category: str | None = None, sub_category: str | None = None) -> None:
        if isinstance(node, str):
            if node.startswith("papers/") and node.endswith(".md"):
                pid = node[len("papers/"):-len(".md")]
                if pid not in mapping:          # first occurrence wins
                    mapping[pid] = {"category": category or "Other", "sub_category": sub_category}
        elif isinstance(node, list):
            for item in node:
                walk(item, category, sub_category)
        elif isinstance(node, dict):
            for key, value in node.items():
                if category is None:
                    if key in TRANSPARENT_NAV_SECTIONS:
                        walk(value, None, None)   # skip wrapper, keep looking for real category
                    else:
                        walk(value, key, None)
                elif category == PLANNING_CATEGORY and sub_category is None:
                    # Second level under Motion Planning → becomes sub_category
                    walk(value, category, key)
                else:
                    walk(value, category, sub_category)

    for item in config.get("nav", []):
        if isinstance(item, dict):
            for section, content in item.items():
                if section in TRANSPARENT_NAV_SECTIONS:
                    walk(content, None, None)
                else:
                    walk(content, section, None)

    return mapping


def parse_nav_category_order(config: dict) -> dict:
    """
    Walk the mkdocs nav tree and return the ordered lists of categories and
    sub-categories as they appear in mkdocs.yml (not alphabetically).

    Returns:
        {
            "categories": [str, ...],
            "subCategoryOrder": {"<category>": [str, ...], ...},
        }
    """
    categories: list[str] = []
    sub_category_order: dict[str, list[str]] = {}

    def walk(node: object, category: str | None = None) -> None:
        if isinstance(node, list):
            for item in node:
                walk(item, category)
        elif isinstance(node, dict):
            for key, value in node.items():
                if category is None:
                    if key in TRANSPARENT_NAV_SECTIONS:
                        walk(value, None)
                    else:
                        if key not in categories:
                            categories.append(key)
                        walk(value, key)
                elif category == PLANNING_CATEGORY:
                    if category not in sub_category_order:
                        sub_category_order[category] = []
                    if key not in sub_category_order[category]:
                        sub_category_order[category].append(key)
                    walk(value, category)
                # else: deeper nesting — no new categories to record

    for item in config.get("nav", []):
        if isinstance(item, dict):
            for section, content in item.items():
                if section in TRANSPARENT_NAV_SECTIONS:
                    walk(content, None)
                else:
                    if section not in categories:
                        categories.append(section)
                    walk(content, section)

    return {"categories": categories, "subCategoryOrder": sub_category_order}


# ---------------------------------------------------------------------------
# Embedding backends
# ---------------------------------------------------------------------------

def embed_voyage(texts: list[str], model: str = "voyage-3-large") -> "np.ndarray":
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
) -> "np.ndarray":
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


def choose_backend(requested: str | None) -> tuple[str, callable]:
    """
    Select the embedding backend.

    Returns (backend_name, embed_function).  The embed function has the
    signature: ``fn(texts: list[str]) -> np.ndarray``.
    """
    if requested == "voyage" or (requested is None and os.environ.get("VOYAGE_API_KEY")):
        try:
            import voyageai  # noqa: F401
        except ImportError:
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

def load_cache(cache_path: Path) -> dict:
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
        with open(cache_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"model": None, "papers": {}}


def save_cache(cache_path: Path, cache: dict) -> None:
    """Persist the full cache dict (embeddings + umap) to disk."""
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(cache, f, separators=(",", ":"))
    size_kb = cache_path.stat().st_size // 1024
    print(f"Cache saved: {cache_path}  ({size_kb} KB)")


# ---------------------------------------------------------------------------
# Cosine similarity
# ---------------------------------------------------------------------------

def cosine_similarity_matrix(embeddings: "np.ndarray") -> "np.ndarray":
    """Return the (n × n) pairwise cosine similarity matrix."""
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    normalised = embeddings / np.clip(norms, 1e-10, None)
    return (normalised @ normalised.T).astype(np.float32)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Cytoscape.js mind-map data from paper embeddings.",
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
        "--threshold",
        type=float,
        default=DEFAULT_THRESHOLD,
        metavar="T",
        help=f"Minimum cosine similarity to draw an edge (default: {DEFAULT_THRESHOLD}).",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=DEFAULT_TOP_K,
        metavar="K",
        dest="top_k",
        help=(
            f"Always connect each paper to its top-K most similar neighbours "
            f"even if their similarity is below --threshold (default: {DEFAULT_TOP_K}). "
            f"Edges below {ABSOLUTE_FLOOR} are still dropped."
        ),
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
    print("Knowledge Base — Mind Map Data Generator")
    print("=" * 60)

    # ---- load config -------------------------------------------------------
    with open(MKDOCS_YML, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    paper_to_category = parse_nav_categories(config)
    nav_order = parse_nav_category_order(config)

    # ---- collect papers ----------------------------------------------------
    print("\n[1/7] Collecting paper metadata…")
    papers: list[dict] = []
    for metadata_file in sorted(METADATA_ROOT.rglob("*.yml")):
        with open(metadata_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        pid = paper_id_from_file(metadata_file, data)
        title = data.get("title", "")
        summary = (data.get("summary") or "").strip()
        tags = data.get("tags") or []
        authors = data.get("authors") or []
        year = data.get("year")
        embed_text = build_embed_text(data)

        cat_info = paper_to_category.get(pid, {"category": "Other", "sub_category": None})
        papers.append({
            "id": pid,
            "title": title,
            "label": make_label(data),
            "authors": [last_name(a) for a in authors[:3]],
            "year": year,
            "category": cat_info["category"],
            "sub_category": cat_info["sub_category"],
            "tags": tags,
            "summary": summary,
            "embed_text": embed_text,
            "hash": content_hash(embed_text),
        })

    print(f"    Found {len(papers)} papers")

    # ---- choose backend ----------------------------------------------------
    print("\n[2/7] Selecting embedding backend…")
    model_name, embed_fn = choose_backend(args.backend)

    # ---- load cache and find which papers need (re-)embedding --------------
    print("\n[3/7] Checking embedding cache…")
    cache = load_cache(args.cache)

    # Invalidate entire cache if the model changed
    if cache.get("model") and cache["model"] != model_name:
        print(
            f"    Model changed ({cache['model']} → {model_name}). "
            "Discarding cache and re-embedding all papers."
        )
        cache = {"model": model_name, "papers": {}}

    cached_papers: dict[str, dict] = cache.get("papers", {})

    # Determine which papers need new embeddings
    to_embed: list[int] = []   # indices into `papers`
    for i, p in enumerate(papers):
        cached = cached_papers.get(p["id"])
        if args.force or cached is None or cached.get("hash") != p["hash"]:
            to_embed.append(i)

    if to_embed:
        print(f"    {len(to_embed)} paper(s) need (re-)embedding  "
              f"({len(papers) - len(to_embed)} cached)")
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
    else:
        print("    (nothing to do)")

    # Assemble full embedding matrix in paper order
    embedding_list = [cached_papers[p["id"]]["embedding"] for p in papers]
    embeddings = np.array(embedding_list, dtype=np.float32)
    print(f"    Embedding matrix: {embeddings.shape}")

    # ---- UMAP layout -------------------------------------------------------
    print("\n[5/7] Computing UMAP 2-D layout…")

    umap_params = dict(
        scale=1000.0,
        random_state=42,
        n_neighbors=min(50, len(embeddings) - 1),
        min_dist=0.05,
        n_epochs=500,
    )
    key = umap_cache_key([p["id"] for p in papers], embeddings, **umap_params)
    umap_entry = cache.get("umap", {})

    if not args.force and umap_entry.get("key") == key:
        print("    UMAP layout loaded from cache (embeddings unchanged)")
        umap_coords = np.array(umap_entry["coords"], dtype=np.float64)
    else:
        umap_coords = compute_umap_positions(embeddings, **umap_params)
        cache["umap"] = {"key": key, "coords": umap_coords.tolist()}
        save_cache(args.cache, cache)

    print(f"    UMAP coords: {umap_coords.shape}  range x=[{umap_coords[:,0].min():.0f}, {umap_coords[:,0].max():.0f}]  y=[{umap_coords[:,1].min():.0f}, {umap_coords[:,1].max():.0f}]")

    # ---- force-directed layout post-processing -----------------------------
    print("\n[6/7] Force-directed layout post-processing…")

    force_params = dict(
        anchor_strength=0.85,
        sim_threshold=0.75,
        sim_top_k=10,
        sim_attraction_strength=0.4,
        gap_factor=2.0,
        collision_radius_factor=0.2,
        collision_iterations=3,
        iterations=120,
        initial_alpha=0.3,
        alpha_decay=0.98,
        post_scale=2.0,
        random_seed=42,
    )

    if args.skip_force_layout:
        print("    Skipped (--skip-force-layout)")
        layout_coords = umap_coords
    else:
        fkey = force_cache_key(umap_coords, embeddings, **force_params)
        force_entry = cache.get("force", {})

        if not args.force and force_entry.get("key") == fkey:
            print("    Force layout loaded from cache (UMAP + embeddings unchanged)")
            layout_coords = np.array(force_entry["coords"], dtype=np.float64)
        else:
            layout_coords = force_layout_postprocess(
                umap_coords, embeddings, verbose=True, **force_params
            )
            cache["force"] = {"key": fkey, "coords": layout_coords.tolist()}
            save_cache(args.cache, cache)

        print(f"    Force coords: {layout_coords.shape}  range x=[{layout_coords[:,0].min():.0f}, {layout_coords[:,0].max():.0f}]  y=[{layout_coords[:,1].min():.0f}, {layout_coords[:,1].max():.0f}]")

    # ---- build graph -------------------------------------------------------
    print("\n[7/7] Building graph and writing output…")

    sim = cosine_similarity_matrix(embeddings)
    n = len(papers)

    nodes = [
        {
            "data": {
                "id": p["id"],
                "label": p["label"],
                "title": p["title"],
                "authors": p["authors"],
                "year": p["year"],
                "category": p["category"],
                "sub_category": p["sub_category"],
                "tags": p["tags"],
                "summary": p["summary"],
            },
            "position": {
                "x": round(float(layout_coords[i, 0]), 1),
                "y": round(float(layout_coords[i, 1]), 1),
            },
        }
        for i, p in enumerate(papers)
    ]

    edges: list[dict] = []
    edge_set: set[tuple[str, str]] = set()

    for i in range(n):
        row = sim[i].copy()
        row[i] = -1.0  # exclude self-similarity

        # Candidates: all above threshold
        above = set(int(j) for j in np.where(row >= args.threshold)[0])

        # Plus top-K neighbours (guarantees connectivity even for outlier papers)
        top_k_idx = np.argpartition(row, -args.top_k)[-args.top_k :]
        above.update(int(j) for j in top_k_idx)

        for j in above:
            if j <= i:
                continue
            sim_val = float(sim[i, j])
            if sim_val < ABSOLUTE_FLOOR:
                continue
            id_i, id_j = papers[i]["id"], papers[j]["id"]
            key = (min(id_i, id_j), max(id_i, id_j))
            if key in edge_set:
                continue
            edge_set.add(key)
            edges.append({
                "data": {
                    "id": f"e{len(edges)}",
                    "source": id_i,
                    "target": id_j,
                    "weight": round(sim_val, 4),
                }
            })

    # Bake per-edge opacity based on node degree (high-degree hubs → more transparent)
    degree: dict[str, int] = {}
    for e in edges:
        degree[e["data"]["source"]] = degree.get(e["data"]["source"], 0) + 1
        degree[e["data"]["target"]] = degree.get(e["data"]["target"], 0) + 1
    max_deg = max(degree.values(), default=1)
    for e in edges:
        d = max(degree.get(e["data"]["source"], 1), degree.get(e["data"]["target"], 1))
        t = math.log(d) / math.log(max_deg) if max_deg > 1 else 0.0
        e["data"]["edgeAlpha"] = round(0.50 - t * (0.50 - 0.06), 3)

    graph_data = {
        "nodes": nodes,
        "edges": edges,
        "meta": {
            "model": model_name,
            "threshold": args.threshold,
            "top_k": args.top_k,
            "total_papers": len(papers),
            "total_edges": len(edges),
            "categoryOrder": nav_order["categories"],
            "subCategoryOrder": nav_order["subCategoryOrder"],
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    js = f"const mindMapData = {json.dumps(graph_data, indent=2, ensure_ascii=False)};\n"
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(js)

    print(f"    Nodes : {len(nodes)}")
    print(f"    Edges : {len(edges)}  (threshold={args.threshold}, top_k={args.top_k})")
    print(f"    Output: {args.output}")
    print("\nDone!")


if __name__ == "__main__":
    main()
