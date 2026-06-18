"""Shared embedding cache work for generated knowledge-base assets."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np

FORMAT_VERSION = "embedding-workbench-v2"


@dataclass(frozen=True)
class EmbeddingRow:
    id: str
    text: str
    content_hash: str
    paper_id: str | None = None
    weight: float = 1.0


@dataclass(frozen=True)
class EmbeddingRefresh:
    cache: dict[str, Any]
    matrix: np.ndarray
    changed_count: int
    pruned_ids: tuple[str, ...]
    model_changed: bool
    previous_model: str | None


@dataclass(frozen=True)
class EmbeddingTable:
    model: str | None
    ids: tuple[str, ...]
    matrix: np.ndarray
    hashes: dict[str, str]

    def by_id(self, *, normalize_rows: bool = False) -> dict[str, np.ndarray]:
        matrix = self.matrix.astype(np.float32, copy=False)
        if normalize_rows:
            norms = np.linalg.norm(matrix, axis=1, keepdims=True)
            matrix = matrix / np.clip(norms, 1e-10, None)
        return {paper_id: matrix[index] for index, paper_id in enumerate(self.ids)}


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
    _write_text_atomic(path, json.dumps(cache, separators=(",", ":")))
    print(f"Cache saved: {path} ({path.stat().st_size // 1024} KB)")


def load_embedding_table(path: Path, *, mmap_mode: str | None = None, aggregate: bool = True) -> EmbeddingTable:
    """Load cached embeddings from the v2 binary format or legacy JSON caches."""
    cache = load_embedding_cache(path)
    papers = _cached_papers(cache)
    model = cache.get("model") if isinstance(cache.get("model"), str) else None

    if cache.get("format") == FORMAT_VERSION:
        vectors_path = _vectors_path(path, cache)
        try:
            matrix = np.load(vectors_path, mmap_mode=mmap_mode, allow_pickle=False)
        except OSError:
            return EmbeddingTable(model=model, ids=(), matrix=np.empty((0, 0), dtype=np.float32), hashes={})

        ordered: list[tuple[int, str, str, str, float]] = []
        for row_id, entry in papers.items():
            row = entry.get("row")
            if isinstance(row, int) and 0 <= row < len(matrix):
                ordered.append(
                    (
                        row,
                        row_id,
                        str(entry.get("hash") or ""),
                        str(entry.get("paper_id") or row_id),
                        _entry_weight(entry),
                    )
                )
        ordered.sort()
        indexes = [row for row, _, _, _, _ in ordered]
        ids = tuple(row_id for _, row_id, _, _, _ in ordered)
        hashes = {row_id: content_hash for _, row_id, content_hash, _, _ in ordered}
        if indexes and indexes != list(range(len(indexes))):
            matrix = matrix[indexes]
        if matrix.dtype != np.float32:
            matrix = matrix.astype(np.float32)
        table = EmbeddingTable(
            model=model,
            ids=ids,
            matrix=matrix,
            hashes=hashes,
        )
        if not aggregate:
            return table
        rows = [
            EmbeddingRow(row_id, "", content_hash, paper_id=paper_id, weight=weight)
            for _, row_id, content_hash, paper_id, weight in ordered
        ]
        return _aggregate_table(table, rows)

    ids: list[str] = []
    vectors: list[np.ndarray] = []
    hashes: dict[str, str] = {}
    for paper_id, entry in papers.items():
        raw_vector = entry.get("embedding")
        if not isinstance(raw_vector, list):
            continue
        vector = np.asarray(raw_vector, dtype=np.float32)
        if vector.ndim != 1:
            continue
        ids.append(paper_id)
        vectors.append(vector)
        hashes[paper_id] = str(entry.get("hash") or "")

    matrix = np.vstack(vectors).astype(np.float32, copy=False) if vectors else np.empty((0, 0), dtype=np.float32)
    return EmbeddingTable(model=model, ids=tuple(ids), matrix=matrix, hashes=hashes)


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
    table = (
        EmbeddingTable(model=None, ids=(), matrix=np.empty((0, 0), dtype=np.float32), hashes={})
        if model_changed
        else load_embedding_table(cache_path, aggregate=False)
    )
    vector_by_id = table.by_id()
    active_ids = {row.id for row in ordered_rows}
    pruned_ids = tuple(sorted(set(cached_papers) - active_ids))
    for paper_id in pruned_ids:
        del cached_papers[paper_id]
        vector_by_id.pop(paper_id, None)

    changed_rows = [
        row
        for row in ordered_rows
        if force
        or row.id not in cached_papers
        or row.id not in vector_by_id
        or cached_papers[row.id].get("hash") != row.content_hash
    ]

    if changed_rows:
        vectors = _embedding_matrix(embed_texts([row.text for row in changed_rows]), len(changed_rows))
        for row, vector in zip(changed_rows, vectors, strict=True):
            vector_by_id[row.id] = vector.astype(np.float32, copy=False)
            cached_papers[row.id] = {
                "hash": row.content_hash,
            }

    row_matrix = _ordered_matrix(ordered_rows, vector_by_id)
    matrix = _aggregate_rows(ordered_rows, vector_by_id)
    needs_v2_write = cache.get("format") != FORMAT_VERSION or not _vectors_path(cache_path, cache).exists()
    saved = bool(changed_rows or pruned_ids or model_changed or needs_v2_write)
    if saved:
        for key in invalidate_keys:
            cache.pop(key, None)
        _save_embedding_table(cache_path, cache, ordered_rows, row_matrix, model)

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


def _entry_weight(entry: dict[str, Any]) -> float:
    try:
        weight = float(entry.get("weight") or 1.0)
    except (TypeError, ValueError):
        return 1.0
    return weight if np.isfinite(weight) else 1.0


def _embedding_matrix(vectors: Sequence[Sequence[float]] | np.ndarray, expected_rows: int) -> np.ndarray:
    matrix = np.asarray(vectors, dtype=np.float32)
    if expected_rows == 1 and matrix.ndim == 1:
        matrix = matrix.reshape(1, -1)
    if matrix.ndim != 2 or matrix.shape[0] != expected_rows:
        raise ValueError(f"Embedder returned {matrix.shape[0] if matrix.ndim else 0} row(s); expected {expected_rows}")
    return matrix


def _ordered_matrix(rows: Sequence[EmbeddingRow], vector_by_id: dict[str, np.ndarray]) -> np.ndarray:
    if not rows:
        return np.empty((0, 0), dtype=np.float32)
    return np.asarray([vector_by_id[row.id] for row in rows], dtype=np.float32)


def _aggregate_rows(rows: Sequence[EmbeddingRow], vector_by_id: dict[str, np.ndarray]) -> np.ndarray:
    if not rows:
        return np.empty((0, 0), dtype=np.float32)

    groups: dict[str, list[EmbeddingRow]] = {}
    for row in rows:
        groups.setdefault(_row_paper_id(row), []).append(row)

    vectors: list[np.ndarray] = []
    for group_rows in groups.values():
        group_matrix = np.asarray([vector_by_id[row.id] for row in group_rows], dtype=np.float32)
        if len(group_rows) == 1:
            vectors.append(group_matrix[0])
            continue
        weights = np.asarray([max(float(row.weight), 0.0) for row in group_rows], dtype=np.float32)
        if float(weights.sum()) <= 0:
            weights = np.ones(len(group_rows), dtype=np.float32)
        normalized = _normalize_rows(group_matrix)
        aggregate = (normalized * (weights / weights.sum())[:, None]).sum(axis=0)
        aggregate_norm = np.linalg.norm(aggregate)
        if aggregate_norm > 1e-10:
            aggregate = aggregate / aggregate_norm
        vectors.append(aggregate.astype(np.float32, copy=False))
    return np.vstack(vectors).astype(np.float32, copy=False)


def _aggregate_table(table: EmbeddingTable, rows: Sequence[EmbeddingRow]) -> EmbeddingTable:
    paper_ids = _ordered_paper_ids(rows)
    if table.ids == paper_ids:
        return table
    vector_by_id = table.by_id()
    return EmbeddingTable(
        model=table.model,
        ids=paper_ids,
        matrix=_aggregate_rows(rows, vector_by_id),
        hashes=_aggregate_hashes(rows),
    )


def _ordered_paper_ids(rows: Sequence[EmbeddingRow]) -> tuple[str, ...]:
    ids: list[str] = []
    seen: set[str] = set()
    for row in rows:
        paper_id = _row_paper_id(row)
        if paper_id not in seen:
            ids.append(paper_id)
            seen.add(paper_id)
    return tuple(ids)


def _aggregate_hashes(rows: Sequence[EmbeddingRow]) -> dict[str, str]:
    grouped: dict[str, list[str]] = {}
    for row in rows:
        grouped.setdefault(_row_paper_id(row), []).append(row.content_hash)
    return {
        paper_id: hashes[0] if len(hashes) == 1 else _short_hash("\n".join(hashes))
        for paper_id, hashes in grouped.items()
    }


def _row_paper_id(row: EmbeddingRow) -> str:
    return row.paper_id or row.id


def _short_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def _normalize_rows(matrix: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    return matrix / np.clip(norms, 1e-10, None)


def _vectors_path(cache_path: Path, cache: dict[str, Any]) -> Path:
    configured = cache.get("vectors")
    if isinstance(configured, str) and configured:
        return cache_path.parent / configured
    return cache_path.with_name(f"{cache_path.stem}.vectors.npy")


def _write_text_atomic(path: Path, content: str) -> None:
    tmp = path.with_name(f".{path.name}.tmp")
    tmp.write_text(content, encoding="utf-8")
    tmp.replace(path)


def _save_embedding_table(
    path: Path,
    cache: dict[str, Any],
    rows: Sequence[EmbeddingRow],
    matrix: np.ndarray,
    model: str,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    vectors_path = path.with_name(f"{path.stem}.vectors.npy")
    matrix = np.asarray(matrix, dtype=np.float32)
    vectors_tmp = vectors_path.with_name(f".{vectors_path.name}.tmp")
    with vectors_tmp.open("wb") as out:
        np.save(out, matrix, allow_pickle=False)
    vectors_tmp.replace(vectors_path)

    cache["format"] = FORMAT_VERSION
    cache["model"] = model
    cache["vectors"] = vectors_path.name
    cache["papers"] = {
        row.id: {
            "hash": row.content_hash,
            "paper_id": _row_paper_id(row),
            "row": index,
            "weight": row.weight,
        }
        for index, row in enumerate(rows)
    }
    save_embedding_cache(path, cache)
