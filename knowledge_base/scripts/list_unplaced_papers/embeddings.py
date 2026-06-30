"""Embedding helpers for suggesting Tree placements."""

from __future__ import annotations

import math
from pathlib import Path


def load_embeddings(cache_path: Path) -> dict[str, list[float]]:
    if not cache_path.exists():
        return {}
    from knowledge_base.embedding_workbench import load_embedding_table

    return {paper_id: vector.tolist() for paper_id, vector in load_embedding_table(cache_path).by_id().items()}


def nearest_placed_neighbors(
    missing_id: str,
    placed_ids: set[str],
    embeddings: dict[str, list[float]],
    *,
    top_k: int,
) -> list[tuple[str, float]]:
    if top_k <= 0 or missing_id not in embeddings:
        return []

    missing = embeddings[missing_id]
    missing_norm = math.sqrt(sum(value * value for value in missing))
    if missing_norm == 0.0:
        return []

    rows: list[tuple[str, float]] = []
    for placed_id in placed_ids:
        vector = embeddings.get(placed_id)
        if vector is None:
            continue
        placed_norm = math.sqrt(sum(value * value for value in vector))
        if placed_norm == 0.0:
            continue
        score = sum(a * b for a, b in zip(missing, vector, strict=False)) / (missing_norm * placed_norm)
        rows.append((placed_id, score))

    return sorted(rows, key=lambda item: item[1], reverse=True)[:top_k]
