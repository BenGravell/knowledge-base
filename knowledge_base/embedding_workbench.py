"""Shared embedding cache work for generated knowledge-base assets."""

from __future__ import annotations

import json
from collections import Counter
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np


@dataclass(frozen=True)
class EmbeddingRow:
    id: str
    text: str
    content_hash: str


@dataclass(frozen=True)
class EmbeddingRefresh:
    cache: dict[str, Any]
    matrix: np.ndarray
    changed_count: int
    pruned_ids: tuple[str, ...]
    model_changed: bool
    previous_model: str | None


EmbedTexts = Callable[[list[str]], Sequence[Sequence[float]] | np.ndarray]


def load_embedding_cache(path: Path) -> dict[str, Any]:
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


def save_embedding_cache(path: Path, cache: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cache, separators=(",", ":")), encoding="utf-8")
    print(f"Cache saved: {path} ({path.stat().st_size // 1024} KB)")


def refresh_embedding_cache(
    rows: Sequence[EmbeddingRow],
    *,
    cache_path: Path,
    model: str,
    embed_texts: EmbedTexts,
    force: bool = False,
    invalidate_keys: Sequence[str] = (),
) -> EmbeddingRefresh:
    ordered_rows = _validate_rows(rows)
    cache = load_embedding_cache(cache_path)
    previous_model = cache.get("model") if isinstance(cache.get("model"), str) else None
    model_changed = bool(previous_model and previous_model != model)
    if model_changed:
        cache = {"model": model, "papers": {}}

    cached_papers = _cached_papers(cache)
    active_ids = {row.id for row in ordered_rows}
    pruned_ids = tuple(sorted(set(cached_papers) - active_ids))
    for paper_id in pruned_ids:
        del cached_papers[paper_id]

    changed_rows = [
        row
        for row in ordered_rows
        if force or row.id not in cached_papers or cached_papers[row.id].get("hash") != row.content_hash
    ]

    if changed_rows:
        vectors = _embedding_matrix(embed_texts([row.text for row in changed_rows]), len(changed_rows))
        for row, vector in zip(changed_rows, vectors, strict=True):
            cached_papers[row.id] = {
                "hash": row.content_hash,
                "embedding": vector.astype(np.float32).tolist(),
            }

    saved = bool(changed_rows or pruned_ids or model_changed)
    if saved:
        for key in invalidate_keys:
            cache.pop(key, None)
        cache["model"] = model
        cache["papers"] = cached_papers
        save_embedding_cache(cache_path, cache)

    matrix = _ordered_matrix(ordered_rows, cached_papers)
    return EmbeddingRefresh(
        cache=cache,
        matrix=matrix,
        changed_count=len(changed_rows),
        pruned_ids=pruned_ids,
        model_changed=model_changed,
        previous_model=previous_model,
    )


def _validate_rows(rows: Sequence[EmbeddingRow]) -> list[EmbeddingRow]:
    ordered_rows = list(rows)
    counts = Counter(row.id for row in ordered_rows)
    duplicate_ids = sorted(paper_id for paper_id, count in counts.items() if count > 1)
    if duplicate_ids:
        raise ValueError(f"Duplicate embedding row id(s): {', '.join(duplicate_ids)}")
    return ordered_rows


def _cached_papers(cache: dict[str, Any]) -> dict[str, dict[str, Any]]:
    cached_raw = cache.get("papers")
    cached = (
        {str(paper_id): dict(entry) for paper_id, entry in cached_raw.items() if isinstance(entry, dict)}
        if isinstance(cached_raw, dict)
        else {}
    )
    cache["papers"] = cached
    return cached


def _embedding_matrix(vectors: Sequence[Sequence[float]] | np.ndarray, expected_rows: int) -> np.ndarray:
    matrix = np.asarray(vectors, dtype=np.float32)
    if expected_rows == 1 and matrix.ndim == 1:
        matrix = matrix.reshape(1, -1)
    if matrix.ndim != 2 or matrix.shape[0] != expected_rows:
        raise ValueError(f"Embedder returned {matrix.shape[0] if matrix.ndim else 0} row(s); expected {expected_rows}")
    return matrix


def _ordered_matrix(rows: Sequence[EmbeddingRow], cached_papers: dict[str, dict[str, Any]]) -> np.ndarray:
    if not rows:
        return np.empty((0, 0), dtype=np.float32)
    return np.asarray([cached_papers[row.id]["embedding"] for row in rows], dtype=np.float32)
