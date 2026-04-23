#!/usr/bin/env python3
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

Because the similarity matrix is O(n²) dot products over small vectors it
is always fast to recompute, so only the embedding step is cached.

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

After running this script, rebuild or re-serve the MkDocs site:
    cd knowledge_base && mkdocs serve

Requirements
------------
Always required:
    pyyaml numpy

For Voyage AI backend:
    voyageai

For fastembed backend:
    fastembed
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

import yaml

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

DEFAULT_THRESHOLD = 0.80   # Minimum cosine similarity to draw an edge
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

def parse_nav_categories(config: dict) -> dict[str, str]:
    """
    Recursively walk the mkdocs ``nav`` tree and record which top-level
    section each paper belongs to.

    Returns a dict mapping paper_id (filename without .md) → category name.
    """
    mapping: dict[str, str] = {}

    def walk(node: object, category: str | None = None) -> None:
        if isinstance(node, str):
            if node.startswith("papers/") and node.endswith(".md"):
                pid = node[len("papers/"):-len(".md")]
                if pid not in mapping:          # first occurrence wins
                    mapping[pid] = category or "Other"
        elif isinstance(node, list):
            for item in node:
                walk(item, category)
        elif isinstance(node, dict):
            for key, value in node.items():
                walk(value, category or key)

    for item in config.get("nav", []):
        if isinstance(item, dict):
            for section, content in item.items():
                walk(content, section)

    return mapping


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
    import numpy as np

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
    import numpy as np
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
          }
        }
    """
    if cache_path.exists():
        with open(cache_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"model": None, "papers": {}}


def save_cache(cache_path: Path, model_name: str, paper_data: dict) -> None:
    """
    Persist the embedding cache to disk.

    ``paper_data`` maps paper_id → {"hash": str, "embedding": list[float]}.
    """
    cache = {"model": model_name, "papers": paper_data}
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(cache, f, separators=(",", ":"))
    size_kb = cache_path.stat().st_size // 1024
    print(f"Cache saved: {cache_path}  ({size_kb} KB)")


# ---------------------------------------------------------------------------
# Cosine similarity
# ---------------------------------------------------------------------------

def cosine_similarity_matrix(embeddings: "np.ndarray") -> "np.ndarray":
    """Return the (n × n) pairwise cosine similarity matrix."""
    import numpy as np
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
    args = parser.parse_args()

    import numpy as np

    print("=" * 60)
    print("Knowledge Base — Mind Map Data Generator")
    print("=" * 60)

    # ---- load config -------------------------------------------------------
    with open(MKDOCS_YML, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    paper_to_category = parse_nav_categories(config)

    # ---- collect papers ----------------------------------------------------
    print("\n[1/5] Collecting paper metadata…")
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

        papers.append({
            "id": pid,
            "title": title,
            "label": title[:60] + "…" if len(title) > 60 else title,
            "authors": authors[:3],
            "year": year,
            "category": paper_to_category.get(pid, "Other"),
            "tags": tags,
            "summary": (summary[:400] + "…") if len(summary) > 400 else summary,
            "embed_text": embed_text,
            "hash": content_hash(embed_text),
        })

    print(f"    Found {len(papers)} papers")

    # ---- choose backend ----------------------------------------------------
    print("\n[2/5] Selecting embedding backend…")
    model_name, embed_fn = choose_backend(args.backend)

    # ---- load cache and find which papers need (re-)embedding --------------
    print("\n[3/5] Checking embedding cache…")
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
    print("\n[4/5] Generating embeddings…")
    if to_embed:
        texts = [papers[i]["embed_text"] for i in to_embed]
        new_embeddings = embed_fn(texts)

        for idx, paper_idx in enumerate(to_embed):
            p = papers[paper_idx]
            cached_papers[p["id"]] = {
                "hash": p["hash"],
                "embedding": new_embeddings[idx].tolist(),
            }

        save_cache(args.cache, model_name, cached_papers)
    else:
        print("    (nothing to do)")

    # Assemble full embedding matrix in paper order
    embedding_list = [cached_papers[p["id"]]["embedding"] for p in papers]
    embeddings = np.array(embedding_list, dtype=np.float32)
    print(f"    Embedding matrix: {embeddings.shape}")

    # ---- build graph -------------------------------------------------------
    print("\n[5/5] Building graph and writing output…")

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
                "tags": p["tags"],
                "summary": p["summary"],
            }
        }
        for p in papers
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

    graph_data = {
        "nodes": nodes,
        "edges": edges,
        "meta": {
            "model": model_name,
            "threshold": args.threshold,
            "top_k": args.top_k,
            "total_papers": len(papers),
            "total_edges": len(edges),
        },
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    js = f"const mindMapData = {json.dumps(graph_data, indent=2, ensure_ascii=False)};\n"
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(js)

    print(f"    Nodes : {len(nodes)}")
    print(f"    Edges : {len(edges)}  (threshold={args.threshold}, top_k={args.top_k})")
    print(f"    Output: {args.output}")
    print("\nDone!  Rebuild or re-serve the site:")
    print("    cd knowledge_base && mkdocs serve")


if __name__ == "__main__":
    main()
