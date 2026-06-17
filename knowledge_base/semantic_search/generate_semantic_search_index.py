"""Generate compact client-side assets for semantic paper search.

The browser search embeds a free-form query with the same sentence-transformer
model used here, then scores it against this static quantized vector table.
Run this script from ``knowledge_base/`` whenever paper metadata changes:

    python semantic_search/generate_semantic_search_index.py
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from fastembed import TextEmbedding

from knowledge_base.catalog import Catalog


KB_DIR = Path(__file__).resolve().parents[1]
DOCS_DIR = KB_DIR / "docs"
METADATA_ROOT = DOCS_DIR / "papers"
OUT_DIR = KB_DIR / "semantic_search"
DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_BROWSER_MODEL = "Xenova/all-MiniLM-L6-v2"
DEFAULT_CACHE = OUT_DIR / "embedding_cache.json"
DEFAULT_MANIFEST = OUT_DIR / "semantic-search-index.json"
DEFAULT_SETTINGS = OUT_DIR / "semantic-search-settings.json"
DEFAULT_VECTORS = OUT_DIR / "semantic-search-vectors.i8"
QUANTIZATION_SCALE = 127
THRESHOLD_GRID_STEP = 0.01
THRESHOLD_ROUNDING_STEP = 0.05
THRESHOLD_TARGET_RECALL = 0.85
DEFAULT_SCORE_THRESHOLD = 0.25


def clean_scalar(value: object) -> str:
    return str(value or "").strip()


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
    return [
        {
            "id": entry.id,
            "title": entry.title,
            "label": entry.title_label,
            "algorithm": entry.algorithm,
            "authors": entry.authors,
            "year": entry.year,
            "tags": entry.tags,
            "abstract": entry.abstract,
            "summary": entry.summary,
            "url": entry.url("detail"),
            "mapUrl": entry.url("map"),
            "treeUrl": entry.url("tree"),
            "timelineUrl": entry.url("timeline"),
            "searchUrl": entry.url("search"),
            "byline": entry.byline,
            "embed_text": entry.embedding_text,
            "hash": entry.embedding_hash,
        }
        for entry in Catalog.from_metadata_root(METADATA_ROOT).entries
    ]


def l2_normalize(matrix: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    return matrix / np.clip(norms, 1e-10, None)


def quantize_normalized(matrix: np.ndarray) -> np.ndarray:
    return np.clip(np.rint(matrix * QUANTIZATION_SCALE), -128, 127).astype(np.int8)


def normalize_tag(tag: object) -> str:
    return clean_scalar(tag).casefold()


def round_to_step(value: float, step: float = THRESHOLD_ROUNDING_STEP) -> float:
    rounded = np.floor((float(value) / step) + 0.5) * step
    return round(float(np.clip(rounded, 0.0, 1.0)), 2)


def threshold_metrics(scores: np.ndarray, labels: np.ndarray, threshold: float) -> dict[str, float]:
    predicted = scores >= threshold
    positives = labels
    negatives = ~labels
    tp = int(np.count_nonzero(predicted & positives))
    fp = int(np.count_nonzero(predicted & negatives))
    fn = int(np.count_nonzero(~predicted & positives))
    tn = int(np.count_nonzero(~predicted & negatives))

    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    fpr = fp / (fp + tn) if fp + tn else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if precision + recall else 0.0
    return {
        "threshold": float(threshold),
        "precision": precision,
        "recall": recall,
        "false_positive_rate": fpr,
        "f1": f1,
        "youden_j": recall - fpr,
    }


def best_threshold_at_recall(metrics: list[dict[str, float]], target_recall: float) -> dict[str, float]:
    candidates = [item for item in metrics if item["recall"] >= target_recall]
    if not candidates:
        return max(metrics, key=lambda item: item["recall"])
    return max(candidates, key=lambda item: (item["threshold"], item["precision"]))


def best_thresholds_for_shared_tags(matrix: np.ndarray, papers: list[dict]) -> dict:
    if len(papers) < 2:
        return {
            "scoreThreshold": DEFAULT_SCORE_THRESHOLD,
            "scoreThresholdCalibration": {
                "method": "shared-tag-proxy",
                "status": "default-not-enough-papers",
                "roundingStep": THRESHOLD_ROUNDING_STEP,
                "targetRecall": THRESHOLD_TARGET_RECALL,
            },
        }

    tags = [
        {normalize_tag(tag) for tag in paper.get("tags", []) if normalize_tag(tag)}
        for paper in papers
    ]
    row_idx, col_idx = np.triu_indices(len(papers), k=1)
    labels = np.asarray(
        [bool(tags[row] & tags[col]) for row, col in zip(row_idx, col_idx, strict=True)],
        dtype=bool,
    )
    if not labels.any() or labels.all():
        return {
            "scoreThreshold": DEFAULT_SCORE_THRESHOLD,
            "scoreThresholdCalibration": {
                "method": "shared-tag-proxy",
                "status": "default-degenerate-labels",
                "roundingStep": THRESHOLD_ROUNDING_STEP,
                "targetRecall": THRESHOLD_TARGET_RECALL,
            },
        }

    scores = (matrix @ matrix.T)[row_idx, col_idx]
    thresholds = np.arange(0.0, 1.0 + (THRESHOLD_GRID_STEP / 2), THRESHOLD_GRID_STEP)
    metrics = [threshold_metrics(scores, labels, threshold) for threshold in thresholds]
    recall_target = best_threshold_at_recall(metrics, THRESHOLD_TARGET_RECALL)
    balanced = max(metrics, key=lambda item: item["youden_j"])
    best_f1 = max(metrics, key=lambda item: item["f1"])
    rounded_recall = round_to_step(recall_target["threshold"])
    rounded_balanced = round_to_step(balanced["threshold"])
    rounded_f1 = round_to_step(best_f1["threshold"])
    score_threshold = min(rounded_recall, rounded_balanced, rounded_f1)

    return {
        "scoreThreshold": score_threshold,
        "scoreThresholdCalibration": {
            "method": "shared-tag-proxy",
            "status": "ok",
            "gridStep": THRESHOLD_GRID_STEP,
            "roundingStep": THRESHOLD_ROUNDING_STEP,
            "targetRecall": THRESHOLD_TARGET_RECALL,
            "recallTarget": {
                "threshold": round(recall_target["threshold"], 2),
                "roundedThreshold": rounded_recall,
                "precision": round(recall_target["precision"], 3),
                "recall": round(recall_target["recall"], 3),
                "falsePositiveRate": round(recall_target["false_positive_rate"], 3),
            },
            "balancedRoc": {
                "threshold": round(balanced["threshold"], 2),
                "roundedThreshold": rounded_balanced,
                "youdenJ": round(balanced["youden_j"], 3),
                "precision": round(balanced["precision"], 3),
                "recall": round(balanced["recall"], 3),
                "falsePositiveRate": round(balanced["false_positive_rate"], 3),
            },
            "bestF1": {
                "threshold": round(best_f1["threshold"], 2),
                "roundedThreshold": rounded_f1,
                "f1": round(best_f1["f1"], 3),
                "precision": round(best_f1["precision"], 3),
                "recall": round(best_f1["recall"], 3),
                "falsePositiveRate": round(best_f1["false_positive_rate"], 3),
            },
            "selected": "min(rounded recallTarget, rounded balancedRoc, rounded bestF1)",
        },
    }


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
    threshold_data = best_thresholds_for_shared_tags(matrix, papers)

    paper_records = []
    for paper in papers:
        paper_records.append(
            {
                key: paper[key]
                for key in (
                    "id",
                    "title",
                    "label",
                    "algorithm",
                    "authors",
                    "year",
                    "tags",
                    "abstract",
                    "summary",
                    "url",
                    "mapUrl",
                    "treeUrl",
                    "timelineUrl",
                    "searchUrl",
                    "byline",
                )
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
        **threshold_data,
        "papers": paper_records,
    }

    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(manifest, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    args.settings.write_text(
        json.dumps(
            {
                "model": args.model,
                "browserModel": args.browser_model,
                "count": len(papers),
                **threshold_data,
            },
            ensure_ascii=False,
            separators=(",", ":"),
        ),
        encoding="utf-8",
    )
    args.vectors.write_bytes(quantized.tobytes(order="C"))

    print(f"Manifest: {args.manifest} ({args.manifest.stat().st_size // 1024} KB)")
    print(f"Settings: {args.settings} ({args.settings.stat().st_size} bytes)")
    print(f"Vectors : {args.vectors} ({args.vectors.stat().st_size // 1024} KB)")
    print(f"Matrix  : {quantized.shape[0]} x {quantized.shape[1]} int8")
    print(f"Semantic score threshold: {threshold_data['scoreThreshold']:.2f}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"fastembed model name (default: {DEFAULT_MODEL})")
    parser.add_argument("--browser-model", default=DEFAULT_BROWSER_MODEL, help=f"Transformers.js model name (default: {DEFAULT_BROWSER_MODEL})")
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE, help=f"Embedding cache path (default: {DEFAULT_CACHE})")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST, help=f"Output JSON manifest (default: {DEFAULT_MANIFEST})")
    parser.add_argument("--settings", type=Path, default=DEFAULT_SETTINGS, help=f"Output search settings JSON (default: {DEFAULT_SETTINGS})")
    parser.add_argument("--vectors", type=Path, default=DEFAULT_VECTORS, help=f"Output int8 vector table (default: {DEFAULT_VECTORS})")
    parser.add_argument("--force", action="store_true", help="Re-embed all papers even when cached")
    return parser.parse_args()


if __name__ == "__main__":
    generate(parse_args())
