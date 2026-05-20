"""
Suggest selected-node relevance filter defaults for the mind map.

The browser filter keeps a paper when both enabled criteria pass:

  semantic similarity >= semantic slider value
  tree proximity      >= tree proximity slider value

Tree proximity mirrors ``mind-map.js``: the content-tree distance between
two papers is converted to ``max_tree_distance - distance`` so that larger
values mean "closer in the tree".

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
SEMANTIC_MIN = 0.50
SEMANTIC_MAX = 0.95
SEMANTIC_STEP = 0.01
CENTER_WEIGHT = 5.0
PRIMARY_MIN_NEIGHBORS = 3
PRIMARY_COVERAGE = 0.95
FALLBACK_MIN_NEIGHBORS = 1
FALLBACK_COVERAGE = 0.99
SOFT_MAX_P95 = 50
SOFT_MAX_P99 = 90
UNCATEGORIZED_CATEGORY = "Uncategorized"


@dataclass(frozen=True)
class Candidate:
    semantic: float
    tree_proximity: int
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


def build_tree_proximity_matrix(paths: list[tuple[str, ...]], max_tree_distance: int) -> list[list[int]]:
    return [
        [max_tree_distance - tree_distance(ego_path, paper_path) for paper_path in paths]
        for ego_path in paths
    ]


def match_counts(
    similarity_matrix: list[list[float]],
    tree_matrix: list[list[int]],
    semantic_threshold: float,
    tree_threshold: int,
) -> list[int]:
    counts = []
    for similarities, proximities in zip(similarity_matrix, tree_matrix):
        count = sum(
            1
            for similarity, proximity in zip(similarities, proximities)
            if similarity >= semantic_threshold and proximity >= tree_threshold
        )
        counts.append(count)
    return counts


def score_candidate(
    semantic: float,
    tree_proximity: int,
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
    max_tree_distance: int,
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
    tree_mid = max_tree_distance / 2
    tree_half_range = max(max_tree_distance / 2, 1)
    centeredness = (
        ((semantic - semantic_mid) / semantic_half_range) ** 2
        + ((tree_proximity - tree_mid) / tree_half_range) ** 2
    )

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
        semantic=semantic,
        tree_proximity=tree_proximity,
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
) -> tuple[Candidate, list[Candidate], int, int]:
    nodes = [node for node in data.get("nodes", []) if isinstance(node.get("data"), dict)]
    ids = [str(node["data"].get("id")) for node in nodes if node["data"].get("id")]
    data_by_id = {str(node["data"].get("id")): node["data"] for node in nodes if node["data"].get("id")}
    paths = [paper_nav_path(data_by_id[paper_id]) for paper_id in ids]
    max_tree_distance = max(1, max(len(path) for path in paths) * 2)

    tree_matrix = build_tree_proximity_matrix(paths, max_tree_distance)

    candidates = []
    semantic_values = semantic_thresholds(semantic_min, semantic_max, semantic_step)

    if np is not None:
        similarity_array = build_similarity_array(data, ids)
        tree_array = np.array(tree_matrix)
        paper_indexes = np.repeat(np.arange(len(ids)), len(ids))
        semantic_bins = np.floor(similarity_array * 100 + 1e-9).astype(int).clip(0, 100)
        tree_bins = tree_array.astype(int).clip(0, max_tree_distance)
        histogram = np.zeros((len(ids), 101, max_tree_distance + 1), dtype=np.int32)
        np.add.at(
            histogram,
            (paper_indexes, semantic_bins.ravel(), tree_bins.ravel()),
            1,
        )
        match_count_cube = (
            histogram[:, ::-1, ::-1]
            .cumsum(axis=1)
            .cumsum(axis=2)[:, ::-1, ::-1]
        )
    else:
        similarity_matrix = build_similarity_matrix(data, ids)
        match_count_cube = None

    for semantic in semantic_values:
        for tree_proximity in range(0, max_tree_distance + 1):
            if match_count_cube is not None:
                semantic_bin = round(semantic * 100)
                counts = match_count_cube[:, semantic_bin, tree_proximity].tolist()
            else:
                counts = match_counts(
                    similarity_matrix,
                    tree_matrix,
                    semantic,
                    tree_proximity,
                )
            candidates.append(
                score_candidate(
                    semantic,
                    tree_proximity,
                    counts,
                    primary_min_neighbors=primary_min_neighbors,
                    primary_coverage=primary_coverage,
                    fallback_min_neighbors=fallback_min_neighbors,
                    fallback_coverage=fallback_coverage,
                    soft_max_p95=soft_max_p95,
                    soft_max_p99=soft_max_p99,
                    semantic_min=semantic_min,
                    semantic_max=semantic_max,
                    max_tree_distance=max_tree_distance,
                    center_weight=center_weight,
                )
            )

    candidates.sort(key=lambda candidate: candidate.score)
    return candidates[0], candidates, len(ids), max_tree_distance


def format_count(value: float) -> str:
    value = float(value)
    if value.is_integer():
        return str(int(value))
    return f"{value:.1f}"


def print_candidates(candidates: list[Candidate], max_tree_distance: int) -> None:
    print(
        "rank  semantic  tree_prox  js_tree_distance  "
        "p01_nbr  p05_nbr  median  p95  p99  mean   min-max  broad  score"
    )
    for index, candidate in enumerate(candidates, start=1):
        js_tree_distance = max_tree_distance - candidate.tree_proximity
        print(
            f"{index:>4}  "
            f"{candidate.semantic:>8.2f}  "
            f"{candidate.tree_proximity:>9}  "
            f"{js_tree_distance:>16}  "
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
    best, candidates, paper_count, max_tree_distance = suggest_defaults(
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
    print(f"Semantic slider range: {args.semantic_min:.2f}-{args.semantic_max:.2f}")
    print(f"Tree proximity slider range: 0-{max_tree_distance}")
    print()
    print("Recommended defaults")
    print(f"  semantic similarity: {best.semantic:.2f}")
    print(f"  tree proximity:      {best.tree_proximity}")
    print(f"  JS tree distance:    {max_tree_distance - best.tree_proximity}")
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
    print_candidates(candidates[: max(args.top, 0)], max_tree_distance)


if __name__ == "__main__":
    main()
