"""
Suggest selected-node relevance filter defaults for the mind map.

The browser filter keeps a paper when both enabled criteria pass:

  semantic similarity >= semantic slider value
  tree proximity      >= tree proximity slider value

Tree proximity mirrors ``mind-map.js``: the content-tree distance between
two papers is mapped through a learned monotone lookup table.  The lookup
table quantile-matches the empirical tree-distance distribution to the
empirical semantic-similarity distribution, so tree proximity and semantic
similarity both live on a comparable 0..1 scale.

Usage:
    python mind_map/suggest_relevance_defaults.py
    python mind_map/suggest_relevance_defaults.py --primary-min-neighbors 3 --top 20
"""

from __future__ import annotations

import argparse
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import numpy as np
except ImportError:  # pragma: no cover - the script has a pure-Python fallback.
    np = None


DATA_FILE = Path(__file__).with_name("mind-map-data.js")
SEMANTIC_MIN = 0.0
SEMANTIC_MAX = 1.0
SEMANTIC_STEP = 0.01
CENTER_WEIGHT = 5.0
PRIMARY_MIN_NEIGHBORS = 3
PRIMARY_COVERAGE = 0.95
FALLBACK_MIN_NEIGHBORS = 1
FALLBACK_COVERAGE = 0.99
SOFT_MAX_P95 = 50
SOFT_MAX_P99 = 90
SLIDER_EXPANDED_THRESHOLD = 0.70
SLIDER_EXPANDED_POSITION = 0.20
SLIDER_EXPONENT = math.log(1 - SLIDER_EXPANDED_THRESHOLD) / math.log(1 - SLIDER_EXPANDED_POSITION)
UNCATEGORIZED_CATEGORY = "Uncategorized"


@dataclass(frozen=True)
class Candidate:
    threshold: float
    p01_neighbors: float
    p05_neighbors: float
    median_count: float
    mean_count: float
    min_count: int
    p95_count: float
    p99_count: float
    max_count: int
    lower_tail_deficit: float
    broadness_penalty: float
    centeredness: float
    score: float


def load_data(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8").strip()
    text = re.sub(r"^const\s+mindMapData\s*=\s*", "", text)
    text = text.rstrip(";").rstrip()
    data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError(f"{path} did not contain a mindMapData object")
    return data


def paper_nav_path(attrs: dict[str, Any]) -> tuple[str, ...]:
    raw_path = attrs.get("nav_path")
    if not isinstance(raw_path, list):
        raw_path = [
            attrs.get("super_category"),
            attrs.get("category"),
            attrs.get("sub_category"),
        ]

    path = tuple(str(part).strip() for part in raw_path if str(part or "").strip())
    return path or (UNCATEGORIZED_CATEGORY,)


def common_prefix_length(a: tuple[str, ...], b: tuple[str, ...]) -> int:
    count = 0
    for left, right in zip(a, b):
        if left != right:
            break
        count += 1
    return count


def tree_distance(a: tuple[str, ...], b: tuple[str, ...]) -> int:
    common = common_prefix_length(a, b)
    return (len(a) - common) + (len(b) - common)


def percentile(sorted_values: list[int], pct: float) -> float:
    if not sorted_values:
        return math.nan
    if len(sorted_values) == 1:
        return float(sorted_values[0])

    position = (len(sorted_values) - 1) * pct
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return float(sorted_values[lower])

    fraction = position - lower
    return sorted_values[lower] * (1 - fraction) + sorted_values[upper] * fraction


def semantic_thresholds(minimum: float, maximum: float, step: float) -> list[float]:
    if step <= 0:
        raise ValueError("--semantic-step must be positive")

    start = round(minimum * 100)
    stop = round(maximum * 100)
    increment = max(1, round(step * 100))
    return [value / 100 for value in range(start, stop + 1, increment)]


def build_similarity_matrix(data: dict[str, Any], ids: list[str]) -> list[list[float]]:
    similarity = data.get("similarity") or {}
    scale = float(similarity.get("scale") or data.get("meta", {}).get("similarityScale") or 1)
    similarity_ids = similarity.get("ids") or []
    rows = similarity.get("rows") or []
    index_by_id = {str(paper_id): index for index, paper_id in enumerate(similarity_ids)}

    matrix: list[list[float]] = []
    for ego_id in ids:
        ego_index = index_by_id.get(ego_id)
        ego_row: list[float] = []
        for paper_id in ids:
            if ego_id == paper_id:
                ego_row.append(1.0)
                continue

            paper_index = index_by_id.get(paper_id)
            value = None
            if ego_index is not None and paper_index is not None and ego_index < len(rows):
                row = rows[ego_index]
                if isinstance(row, list) and paper_index < len(row):
                    value = row[paper_index]

            try:
                numeric = float(value)
            except (TypeError, ValueError):
                numeric = -1.0
            else:
                numeric = numeric / scale if scale else numeric
            ego_row.append(numeric)
        matrix.append(ego_row)
    return matrix


def build_similarity_array(data: dict[str, Any], ids: list[str]) -> "np.ndarray":
    similarity = data.get("similarity") or {}
    scale = float(similarity.get("scale") or data.get("meta", {}).get("similarityScale") or 1)
    similarity_ids = [str(paper_id) for paper_id in similarity.get("ids") or []]
    rows = np.array(similarity.get("rows") or [], dtype=float)
    if rows.ndim != 2:
        rows = np.empty((0, 0), dtype=float)
    if scale:
        rows = rows / scale

    matrix = np.full((len(ids), len(ids)), -1.0)
    index_by_id = {paper_id: index for index, paper_id in enumerate(similarity_ids)}
    source_indexes = []
    target_indexes = []
    for target_index, paper_id in enumerate(ids):
        source_index = index_by_id.get(paper_id)
        if source_index is None or source_index >= rows.shape[0] or source_index >= rows.shape[1]:
            continue
        source_indexes.append(source_index)
        target_indexes.append(target_index)

    if source_indexes:
        source = np.array(source_indexes)
        target = np.array(target_indexes)
        matrix[np.ix_(target, target)] = rows[np.ix_(source, source)]

    np.fill_diagonal(matrix, 1.0)
    return matrix


def build_tree_distance_matrix(paths: list[tuple[str, ...]]) -> list[list[int]]:
    return [
        [tree_distance(ego_path, paper_path) for paper_path in paths]
        for ego_path in paths
    ]


def learn_tree_proximity_scale(
    semantic_values: list[float],
    tree_distances: list[int],
    max_tree_distance: int,
) -> list[float]:
    values = sorted(min(max(value, 0.0), 1.0) for value in semantic_values if math.isfinite(value))
    distance_counts = [0] * (max_tree_distance + 1)
    for distance in tree_distances:
        if 0 <= distance <= max_tree_distance:
            distance_counts[distance] += 1

    if not values or not any(distance_counts):
        return [
            1 - distance / max_tree_distance if max_tree_distance else 1.0
            for distance in range(max_tree_distance + 1)
        ]

    total = sum(distance_counts)
    scale = [0.0] * (max_tree_distance + 1)
    closer_count = 0
    for distance, count in enumerate(distance_counts):
        midpoint = closer_count + count / 2
        quantile = 1 - midpoint / total
        scale[distance] = min(max(percentile(values, quantile), 0.0), 1.0)
        closer_count += count

    scale[0] = 1.0
    for distance in range(1, len(scale)):
        scale[distance] = min(scale[distance], scale[distance - 1])
    return scale


def kl_divergence(
    reference_values: list[float],
    candidate_values: list[float],
    *,
    bins: int = 101,
    epsilon: float = 1e-12,
) -> float:
    def histogram(values: list[float]) -> list[int]:
        counts = [0] * bins
        for value in values:
            if not math.isfinite(value):
                continue
            clipped = min(max(value, 0.0), 1.0)
            index = min(int(clipped * bins), bins - 1)
            counts[index] += 1
        return counts

    reference = histogram(reference_values)
    candidate = histogram(candidate_values)

    reference_total = sum(reference) + epsilon * bins
    candidate_total = sum(candidate) + epsilon * bins
    total = 0.0
    for ref_count, cand_count in zip(reference, candidate):
        p = (ref_count + epsilon) / reference_total
        q = (cand_count + epsilon) / candidate_total
        total += p * math.log(p / q)
    return total


def precomputed_tree_proximity_scale(data: dict[str, Any]) -> list[float] | None:
    tree_meta = (data.get("meta") or {}).get("treeProximity") or {}
    raw_scale = tree_meta.get("scale")
    if not isinstance(raw_scale, list) or not raw_scale:
        return None

    scale: list[float] = []
    for value in raw_scale:
        try:
            numeric = float(value)
        except (TypeError, ValueError):
            return None
        if not math.isfinite(numeric):
            return None
        scale.append(min(max(numeric, 0.0), 1.0))

    return scale


def match_counts(
    similarity_matrix: list[list[float]],
    tree_proximity_matrix: list[list[float]],
    threshold: float,
) -> list[int]:
    counts = []
    for similarities, proximities in zip(similarity_matrix, tree_proximity_matrix):
        count = sum(
            1
            for similarity, proximity in zip(similarities, proximities)
            if similarity >= threshold and proximity >= threshold
        )
        counts.append(count)
    return counts


def score_candidate(
    threshold: float,
    counts: list[int],
    *,
    primary_min_neighbors: int,
    primary_coverage: float,
    fallback_min_neighbors: int,
    fallback_coverage: float,
    soft_max_p95: int,
    soft_max_p99: int,
    semantic_min: float,
    semantic_max: float,
    center_weight: float,
) -> Candidate:
    sorted_counts = sorted(counts)
    sorted_neighbors = sorted(max(0, count - 1) for count in counts)
    median_count = percentile(sorted_counts, 0.50)
    mean_count = sum(sorted_counts) / len(sorted_counts)
    p01_neighbors = percentile(sorted_neighbors, 1 - fallback_coverage)
    p05_neighbors = percentile(sorted_neighbors, 1 - primary_coverage)
    p95_count = percentile(sorted_counts, 0.95)
    p99_count = percentile(sorted_counts, 0.99)

    semantic_mid = (semantic_min + semantic_max) / 2
    semantic_half_range = max((semantic_max - semantic_min) / 2, 1e-9)
    centeredness = ((threshold - semantic_mid) / semantic_half_range) ** 2

    lower_tail_deficit = (
        max(0, primary_min_neighbors - p05_neighbors)
        + max(0, fallback_min_neighbors - p01_neighbors)
    )
    broadness_penalty = (
        max(0, p95_count - soft_max_p95) * 2
        + max(0, p99_count - soft_max_p99) * 4
    )
    score = (
        lower_tail_deficit * 1000
        + broadness_penalty
        + centeredness * center_weight
    )
    return Candidate(
        threshold=threshold,
        p01_neighbors=p01_neighbors,
        p05_neighbors=p05_neighbors,
        median_count=median_count,
        mean_count=mean_count,
        min_count=sorted_counts[0],
        p95_count=p95_count,
        p99_count=p99_count,
        max_count=sorted_counts[-1],
        lower_tail_deficit=lower_tail_deficit,
        broadness_penalty=broadness_penalty,
        centeredness=centeredness,
        score=score,
    )


def suggest_defaults(
    data: dict[str, Any],
    *,
    primary_min_neighbors: int,
    primary_coverage: float,
    fallback_min_neighbors: int,
    fallback_coverage: float,
    soft_max_p95: int,
    soft_max_p99: int,
    semantic_min: float,
    semantic_max: float,
    semantic_step: float,
    center_weight: float,
) -> tuple[Candidate, list[Candidate], int, int, list[float], float]:
    nodes = [node for node in data.get("nodes", []) if isinstance(node.get("data"), dict)]
    ids = [str(node["data"].get("id")) for node in nodes if node["data"].get("id")]
    data_by_id = {str(node["data"].get("id")): node["data"] for node in nodes if node["data"].get("id")}
    paths = [paper_nav_path(data_by_id[paper_id]) for paper_id in ids]
    max_tree_distance = max(1, max(len(path) for path in paths) * 2)
    tree_distance_matrix = build_tree_distance_matrix(paths)
    precomputed_scale = precomputed_tree_proximity_scale(data)

    candidates = []
    thresholds = semantic_thresholds(semantic_min, semantic_max, semantic_step)

    if np is not None:
        similarity_array = build_similarity_array(data, ids)
        tree_distance_array = np.array(tree_distance_matrix, dtype=int)
        valid = np.isfinite(similarity_array) & (similarity_array >= 0)
        semantic_values = similarity_array[valid].clip(0, 1).tolist()
        if precomputed_scale:
            tree_scale = precomputed_scale
        else:
            tree_distances = tree_distance_array[valid].astype(int).tolist()
            tree_scale = learn_tree_proximity_scale(semantic_values, tree_distances, max_tree_distance)
        tree_indexes = np.clip(tree_distance_array, 0, len(tree_scale) - 1)
        tree_proximity_array = np.take(np.array(tree_scale), tree_indexes)
        tree_kl = kl_divergence(
            semantic_values,
            tree_proximity_array[valid].tolist(),
        )
    else:
        similarity_matrix = build_similarity_matrix(data, ids)
        semantic_values = []
        tree_distances = []
        for similarities, distances in zip(similarity_matrix, tree_distance_matrix):
            for similarity, distance in zip(similarities, distances):
                if math.isfinite(similarity) and similarity >= 0:
                    semantic_values.append(min(max(similarity, 0.0), 1.0))
                    tree_distances.append(distance)
        tree_scale = precomputed_scale or learn_tree_proximity_scale(
            semantic_values,
            tree_distances,
            max_tree_distance,
        )
        tree_proximity_matrix = [
            [tree_scale[min(max(distance, 0), len(tree_scale) - 1)] for distance in distances]
            for distances in tree_distance_matrix
        ]
        tree_kl = kl_divergence(
            semantic_values,
            [value for row in tree_proximity_matrix for value in row],
        )

    for threshold in thresholds:
        if np is not None:
            counts = (
                (similarity_array >= threshold)
                & (tree_proximity_array >= threshold)
            ).sum(axis=1).astype(int).tolist()
        else:
            counts = match_counts(
                similarity_matrix,
                tree_proximity_matrix,
                threshold,
            )
        candidates.append(
            score_candidate(
                threshold,
                counts,
                primary_min_neighbors=primary_min_neighbors,
                primary_coverage=primary_coverage,
                fallback_min_neighbors=fallback_min_neighbors,
                fallback_coverage=fallback_coverage,
                soft_max_p95=soft_max_p95,
                soft_max_p99=soft_max_p99,
                semantic_min=semantic_min,
                semantic_max=semantic_max,
                center_weight=center_weight,
            )
        )

    candidates.sort(key=lambda candidate: candidate.score)
    return candidates[0], candidates, len(ids), max_tree_distance, tree_scale, tree_kl


def format_count(value: float) -> str:
    value = float(value)
    if value.is_integer():
        return str(int(value))
    return f"{value:.1f}"


def threshold_to_slider_position(threshold: float) -> float:
    threshold = min(max(float(threshold), 0.0), 1.0)
    if threshold >= 1:
        return 1.0
    return 1 - ((1 - threshold) ** (1 / SLIDER_EXPONENT))


def print_candidates(candidates: list[Candidate]) -> None:
    print(
        "rank  threshold  "
        "p01_nbr  p05_nbr  median  p95  p99  mean   min-max  broad  score"
    )
    for index, candidate in enumerate(candidates, start=1):
        print(
            f"{index:>4}  "
            f"{candidate.threshold:>9.2f}  "
            f"{format_count(candidate.p01_neighbors):>7}  "
            f"{format_count(candidate.p05_neighbors):>7}  "
            f"{format_count(candidate.median_count):>6}  "
            f"{format_count(candidate.p95_count):>3}  "
            f"{format_count(candidate.p99_count):>3}  "
            f"{candidate.mean_count:>5.1f}  "
            f"{candidate.min_count:>3}-{candidate.max_count:<3}  "
            f"{candidate.broadness_penalty:>5.1f}  "
            f"{candidate.score:>5.1f}"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DATA_FILE, help="Path to mind-map-data.js")
    parser.add_argument("--top", type=int, default=10, help="Number of ranked candidates to print")
    parser.add_argument(
        "--primary-min-neighbors",
        type=int,
        default=PRIMARY_MIN_NEIGHBORS,
        help="Minimum non-self neighbors at the primary coverage",
    )
    parser.add_argument(
        "--primary-coverage",
        type=float,
        default=PRIMARY_COVERAGE,
        help="Fraction of selected papers that should reach --primary-min-neighbors",
    )
    parser.add_argument(
        "--fallback-min-neighbors",
        type=int,
        default=FALLBACK_MIN_NEIGHBORS,
        help="Minimum non-self neighbors at the fallback coverage",
    )
    parser.add_argument(
        "--fallback-coverage",
        type=float,
        default=FALLBACK_COVERAGE,
        help="Fraction of selected papers that should reach --fallback-min-neighbors",
    )
    parser.add_argument(
        "--soft-max-p95",
        type=int,
        default=SOFT_MAX_P95,
        help="Soft upper target for the 95th percentile displayed match count",
    )
    parser.add_argument(
        "--soft-max-p99",
        type=int,
        default=SOFT_MAX_P99,
        help="Soft upper target for the 99th percentile displayed match count",
    )
    parser.add_argument("--semantic-min", type=float, default=SEMANTIC_MIN)
    parser.add_argument("--semantic-max", type=float, default=SEMANTIC_MAX)
    parser.add_argument("--semantic-step", type=float, default=SEMANTIC_STEP)
    parser.add_argument(
        "--center-weight",
        type=float,
        default=CENTER_WEIGHT,
        help="Small secondary penalty for moving away from slider centers",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data = load_data(args.data)
    best, candidates, paper_count, max_tree_distance, tree_scale, tree_kl = suggest_defaults(
        data,
        primary_min_neighbors=args.primary_min_neighbors,
        primary_coverage=args.primary_coverage,
        fallback_min_neighbors=args.fallback_min_neighbors,
        fallback_coverage=args.fallback_coverage,
        soft_max_p95=args.soft_max_p95,
        soft_max_p99=args.soft_max_p99,
        semantic_min=args.semantic_min,
        semantic_max=args.semantic_max,
        semantic_step=args.semantic_step,
        center_weight=args.center_weight,
    )

    print(f"Data: {args.data}")
    print(f"Papers: {paper_count}")
    print(
        "Primary neighbor coverage: "
        f"{args.primary_coverage:.0%} should show at least "
        f"{args.primary_min_neighbors} non-self neighbors"
    )
    print(
        "Fallback neighbor coverage: "
        f"{args.fallback_coverage:.0%} should show at least "
        f"{args.fallback_min_neighbors} non-self neighbor"
    )
    print(
        "Soft upper targets: "
        f"p95 <= {args.soft_max_p95}, p99 <= {args.soft_max_p99}"
    )
    print(f"Shared threshold range: {args.semantic_min:.2f}-{args.semantic_max:.2f}")
    print(
        "Slider curve: "
        f"{SLIDER_EXPANDED_POSITION:.0%} position maps to "
        f"{SLIDER_EXPANDED_THRESHOLD:.2f} threshold"
    )
    print(f"Raw tree distance range: 0-{max_tree_distance}")
    print(
        "Learned tree proximity: "
        + ", ".join(f"d{distance}={value:.2f}" for distance, value in enumerate(tree_scale))
    )
    print(f"Tree-proximity KL divergence vs semantic distribution: {tree_kl:.4f}")
    print()
    print("Recommended defaults")
    print(f"  shared threshold:    {best.threshold:.2f}")
    print(f"  slider position:     {threshold_to_slider_position(best.threshold):.0%}")
    print(f"  semantic similarity: {best.threshold:.2f}")
    print(f"  tree proximity:      {best.threshold:.2f}")
    print(
        "  expected matches:    "
        f"median {format_count(best.median_count)}, "
        f"p95 {format_count(best.p95_count)}, p99 {format_count(best.p99_count)}, "
        f"range {best.min_count}-{best.max_count}"
    )
    print(
        "  expected neighbors:  "
        f"p01 {format_count(best.p01_neighbors)}, "
        f"p05 {format_count(best.p05_neighbors)}"
    )
    print()
    print_candidates(candidates[: max(args.top, 0)])


if __name__ == "__main__":
    main()
