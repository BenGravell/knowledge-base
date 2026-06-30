"""Semantic and Tree proximity matrices for the Map pipeline."""

from __future__ import annotations

from typing import Any

import numpy as np

from knowledge_base.components.map.pipeline.settings import TREE_PROXIMITY_HISTOGRAM_BINS, UNCATEGORIZED_CATEGORY
from knowledge_base.tree.model import common_prefix_length as tree_common_prefix_length
from knowledge_base.tree.model import tree_distance as tree_model_distance


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
