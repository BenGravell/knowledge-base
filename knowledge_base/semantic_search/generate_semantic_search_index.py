"""Generate compact client-side assets for semantic paper search.

The browser search embeds a free-form query with the same sentence-transformer
model used here, then scores it against this static quantized vector table.
Run this script from ``knowledge_base/`` whenever paper metadata changes:

    python semantic_search/generate_semantic_search_index.py
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import quote

import numpy as np
import yaml
from fastembed import TextEmbedding

from knowledge_base.utils.paper_ids import paper_id_from_metadata


KB_DIR = Path(__file__).resolve().parents[1]
DOCS_DIR = KB_DIR / "docs"
METADATA_ROOT = DOCS_DIR / "papers"
OUT_DIR = KB_DIR / "semantic_search"
DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_BROWSER_MODEL = "Xenova/all-MiniLM-L6-v2"
DEFAULT_CACHE = OUT_DIR / "embedding_cache.json"
DEFAULT_MANIFEST = OUT_DIR / "semantic-search-index.json"
DEFAULT_VECTORS = OUT_DIR / "semantic-search-vectors.i8"
QUANTIZATION_SCALE = 127


def clean_scalar(value: object) -> str:
    return str(value or "").strip()


def as_clean_list(value: object) -> list[str]:
    if isinstance(value, list):
        return [clean_scalar(item) for item in value if clean_scalar(item)]
    text = clean_scalar(value)
    return [text] if text else []


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def build_embed_text(data: dict) -> str:
    parts = [
        f"Title: {data.get('title', '')}",
        f"Tags: {', '.join(data.get('tags') or [])}",
        f"Summary: {(data.get('summary') or '').strip()}",
    ]
    abstract = (data.get("abstract") or "").strip()
    if abstract:
        parts.append(f"Abstract: {abstract}")
    return "\n".join(p for p in parts if p.split(": ", 1)[-1].strip())


def paper_byline(authors: list[str], year: object) -> str:
    author = ""
    if authors:
        author = authors[0] + (" et al." if len(authors) > 1 else "")
    return " / ".join(part for part in (author, clean_scalar(year)) if part)


def load_cache(path: Path) -> dict:
    if not path.exists():
        return {"model": None, "papers": {}}
    try:
        cache = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {"model": None, "papers": {}}
    if not isinstance(cache, dict):
        return {"model": None, "papers": {}}
    if not isinstance(cache.get("papers"), dict):
        cache["papers"] = {}
    return cache


def save_cache(path: Path, cache: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cache, separators=(",", ":")), encoding="utf-8")
    print(f"Cache saved: {path} ({path.stat().st_size // 1024} KB)")


def load_papers() -> list[dict]:
    papers = []
    for metadata_file in sorted(METADATA_ROOT.rglob("metadata.yml")):
        with metadata_file.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        if not isinstance(data, dict):
            continue

        paper_id = paper_id_from_metadata(metadata_file, data, METADATA_ROOT)
        title = clean_scalar(data.get("title"))
        algorithm = clean_scalar(data.get("algorithm"))
        authors = as_clean_list(data.get("authors"))
        tags = as_clean_list(data.get("tags"))
        summary = clean_scalar(data.get("summary"))
        year = data.get("year") or ""
        embed_text = build_embed_text({**data, "tags": tags})

        papers.append(
            {
                "id": paper_id,
                "title": title,
                "label": algorithm or title or paper_id,
                "authors": authors,
                "year": year,
                "tags": tags,
                "summary": summary,
                "url": f"../papers/{quote(paper_id, safe='')}/",
                "mapUrl": f"../map/#paper={quote(paper_id, safe='')}",
                "treeUrl": f"../tree/#paper={quote(paper_id, safe='')}",
                "byline": paper_byline(authors, year),
                "embed_text": embed_text,
                "hash": content_hash(embed_text),
            }
        )
    return papers


def l2_normalize(matrix: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    return matrix / np.clip(norms, 1e-10, None)


def quantize_normalized(matrix: np.ndarray) -> np.ndarray:
    return np.clip(np.rint(matrix * QUANTIZATION_SCALE), -128, 127).astype(np.int8)


def generate(args: argparse.Namespace) -> None:
    papers = load_papers()
    print(f"Found {len(papers)} papers")

    cache = load_cache(args.cache)
    if cache.get("model") and cache.get("model") != args.model:
        print(f"Model changed ({cache.get('model')} -> {args.model}); rebuilding cache")
        cache = {"model": args.model, "papers": {}}

    cached_papers: dict[str, dict] = cache.setdefault("papers", {})
    active_ids = {paper["id"] for paper in papers}
    for paper_id in sorted(set(cached_papers) - active_ids):
        del cached_papers[paper_id]

    to_embed = [
        paper
        for paper in papers
        if args.force
        or paper["id"] not in cached_papers
        or cached_papers[paper["id"]].get("hash") != paper["hash"]
    ]

    if to_embed:
        print(f"Embedding {len(to_embed)} changed paper(s) with {args.model}")
        embedder = TextEmbedding(args.model)
        vectors = list(embedder.embed([paper["embed_text"] for paper in to_embed], batch_size=32))
        for paper, vector in zip(to_embed, vectors, strict=True):
            cached_papers[paper["id"]] = {
                "hash": paper["hash"],
                "embedding": np.asarray(vector, dtype=np.float32).tolist(),
            }
        cache["model"] = args.model
        save_cache(args.cache, cache)
    else:
        print("All paper embeddings are cached")

    matrix = np.asarray([cached_papers[paper["id"]]["embedding"] for paper in papers], dtype=np.float32)
    matrix = l2_normalize(matrix)
    quantized = quantize_normalized(matrix)

    paper_records = []
    for paper in papers:
        paper_records.append(
            {
                key: paper[key]
                for key in ("id", "title", "label", "authors", "year", "tags", "summary", "url", "mapUrl", "treeUrl", "byline")
            }
        )

    manifest = {
        "model": args.model,
        "browserModel": args.browser_model,
        "dimension": int(matrix.shape[1]),
        "count": len(papers),
        "vectors": args.vectors.name,
        "quantization": {
            "type": "int8",
            "scale": QUANTIZATION_SCALE,
            "normalized": True,
        },
        "papers": paper_records,
    }

    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(manifest, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    args.vectors.write_bytes(quantized.tobytes(order="C"))

    print(f"Manifest: {args.manifest} ({args.manifest.stat().st_size // 1024} KB)")
    print(f"Vectors : {args.vectors} ({args.vectors.stat().st_size // 1024} KB)")
    print(f"Matrix  : {quantized.shape[0]} x {quantized.shape[1]} int8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"fastembed model name (default: {DEFAULT_MODEL})")
    parser.add_argument("--browser-model", default=DEFAULT_BROWSER_MODEL, help=f"Transformers.js model name (default: {DEFAULT_BROWSER_MODEL})")
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE, help=f"Embedding cache path (default: {DEFAULT_CACHE})")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST, help=f"Output JSON manifest (default: {DEFAULT_MANIFEST})")
    parser.add_argument("--vectors", type=Path, default=DEFAULT_VECTORS, help=f"Output int8 vector table (default: {DEFAULT_VECTORS})")
    parser.add_argument("--force", action="store_true", help="Re-embed all papers even when cached")
    return parser.parse_args()


if __name__ == "__main__":
    generate(parse_args())
