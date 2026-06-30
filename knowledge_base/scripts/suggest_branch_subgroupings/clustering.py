"""Embedding clustering and naming logic."""

import re
from collections import Counter

import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import normalize

from knowledge_base.scripts.suggest_branch_subgroupings.common import BROAD_TERMS
from knowledge_base.scripts.suggest_branch_subgroupings.model import Cluster, Paper, Suggestion
from knowledge_base.scripts.tree_report_data import CountMode, format_path
from knowledge_base.tree.model import TreeBranch as Branch
from knowledge_base.tree.model import TreeChild as ChildItem


def child_embedding(
    child: ChildItem,
    embeddings: dict[str, np.ndarray],
) -> np.ndarray | None:
    vectors = [embeddings[paper_id] for paper_id in child.paper_ids if paper_id in embeddings]
    if not vectors:
        return None
    matrix = np.vstack(vectors)
    vector = matrix.mean(axis=0)
    norm = np.linalg.norm(vector)
    if norm == 0:
        return None
    return vector / norm


def cluster_with_k(matrix: np.ndarray, k: int) -> np.ndarray:
    model = AgglomerativeClustering(
        n_clusters=k,
        metric="cosine",
        linkage="average",
    )
    return model.fit_predict(matrix)


def candidate_cluster_counts(
    item_count: int,
    *,
    maximum: int,
    max_groups: int | None,
) -> range:
    if item_count < 3:
        return range(0)
    inferred_max = maximum if max_groups is None else max_groups
    upper = min(item_count - 1, max(2, inferred_max))
    return range(2, upper + 1)


def score_labels(
    matrix: np.ndarray,
    labels: np.ndarray,
    *,
    minimum: int,
    maximum: int,
    sweet_spot: int,
) -> tuple[float, float]:
    silhouette = float(silhouette_score(matrix, labels, metric="cosine"))
    sizes = np.bincount(labels)
    oversized = sum(max(0, int(size) - maximum) for size in sizes) / len(labels)
    undersized = sum(1 for size in sizes if size < minimum) / len(sizes)
    mean_size = len(labels) / len(sizes)
    target_distance = min(2.0, abs(mean_size - sweet_spot) / max(1, sweet_spot))
    score = silhouette - 0.12 * oversized - 0.08 * undersized - 0.08 * target_distance
    return score, silhouette


def choose_labels(
    matrix: np.ndarray,
    *,
    minimum: int,
    maximum: int,
    sweet_spot: int,
    max_groups: int | None,
) -> tuple[np.ndarray, int, float, float] | None:
    best: tuple[float, float, int, np.ndarray] | None = None
    for k in candidate_cluster_counts(
        len(matrix),
        maximum=maximum,
        max_groups=max_groups,
    ):
        labels = cluster_with_k(matrix, k)
        if len(set(labels)) < 2 or len(set(labels)) >= len(labels):
            continue
        score, silhouette = score_labels(
            matrix,
            labels,
            minimum=minimum,
            maximum=maximum,
            sweet_spot=sweet_spot,
        )
        if best is None or score > best[0]:
            best = (score, silhouette, k, labels)

    if best is None:
        return None
    score, silhouette, k, labels = best
    return labels, k, silhouette, score


def normalize_phrase(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("\n", " ")).strip(" '\"`.,:;")


def add_phrase(
    terms: Counter[str],
    phrase: str,
    *,
    weight: int,
    parent_terms: set[str],
) -> None:
    phrase = normalize_phrase(phrase)
    key = phrase.lower()
    if not phrase or len(phrase) < 3:
        return
    if key in parent_terms or key in BROAD_TERMS:
        return
    terms[phrase] += weight


def suggest_cluster_name(
    children: tuple[ChildItem, ...],
    papers: dict[str, Paper],
    parent_path: tuple[str, ...],
) -> str:
    parent_terms = {part.lower() for part in parent_path}
    terms: Counter[str] = Counter()

    for child in children:
        if child.kind == "branch":
            add_phrase(terms, child.label, weight=8, parent_terms=parent_terms)
        for paper_id in child.paper_ids:
            paper = papers.get(paper_id)
            if paper is None:
                continue
            add_phrase(terms, paper.algorithm, weight=5, parent_terms=parent_terms)
            for tag in paper.tags:
                add_phrase(terms, tag, weight=3, parent_terms=parent_terms)

    if terms:
        return " / ".join(term for term, _ in terms.most_common(3))

    compact_labels = [child.label for child in children[:2]]
    return " / ".join(compact_labels) if compact_labels else "Mixed"


def mean_intra_similarity(matrix: np.ndarray, indices: list[int]) -> float:
    if len(indices) < 2:
        return 1.0
    submatrix = matrix[indices]
    similarities = submatrix @ submatrix.T
    upper = similarities[np.triu_indices(len(indices), k=1)]
    return float(np.mean(upper)) if len(upper) else 1.0


def build_suggestion(
    branch: Branch,
    *,
    children: tuple[ChildItem, ...],
    embeddings: dict[str, np.ndarray],
    papers: dict[str, Paper],
    minimum: int,
    maximum: int,
    sweet_spot: int,
    max_groups: int | None,
    min_embedded_children: int,
) -> Suggestion | None:
    embedded_children: list[ChildItem] = []
    vectors: list[np.ndarray] = []
    for child in children:
        vector = child_embedding(child, embeddings)
        if vector is None:
            continue
        embedded_children.append(child)
        vectors.append(vector)

    if len(embedded_children) < min_embedded_children:
        return None

    matrix = normalize(np.vstack(vectors), norm="l2")
    chosen = choose_labels(
        matrix,
        minimum=minimum,
        maximum=maximum,
        sweet_spot=sweet_spot,
        max_groups=max_groups,
    )
    if chosen is None:
        return None
    labels, k, silhouette, score = chosen

    clusters: list[Cluster] = []
    for cluster_id in sorted(set(labels), key=lambda label: min(np.where(labels == label)[0])):
        indices = [int(index) for index in np.where(labels == cluster_id)[0]]
        cluster_children = tuple(embedded_children[index] for index in indices)
        clusters.append(
            Cluster(
                name=suggest_cluster_name(cluster_children, papers, branch.path),
                children=cluster_children,
                mean_similarity=mean_intra_similarity(matrix, indices),
            )
        )

    return Suggestion(
        branch=branch,
        clustered_child_count=len(embedded_children),
        skipped_child_count=len(children) - len(embedded_children),
        k=k,
        silhouette=silhouette,
        score=score,
        clusters=tuple(clusters),
    )


def find_too_many_branches(
    branches: list[Branch],
    *,
    mode: CountMode,
    maximum: int,
    max_depth: int | None,
    branch_filter: str | None,
) -> list[Branch]:
    filtered = []
    branch_filter_lower = branch_filter.lower() if branch_filter else None
    for branch in branches:
        if max_depth is not None and branch.depth > max_depth:
            continue
        if branch.count_for(mode) <= maximum:
            continue
        if branch_filter_lower and branch_filter_lower not in format_path(branch.path).lower():
            continue
        filtered.append(branch)

    return sorted(
        filtered,
        key=lambda branch: (
            -(branch.count_for(mode) - maximum),
            format_path(branch.path),
        ),
    )


__all__ = [
    "build_suggestion",
    "find_too_many_branches",
    "suggest_cluster_name",
]
