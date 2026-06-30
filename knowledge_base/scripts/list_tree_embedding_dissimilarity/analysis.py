"""Outlier detection for Tree embedding categories."""

from __future__ import annotations

from knowledge_base.components.tree.model import TreeBranch as Branch
from knowledge_base.scripts.list_tree_embedding_dissimilarity.data import format_path
from knowledge_base.scripts.list_tree_embedding_dissimilarity.model import Finding, Outlier, Paper, Scope


def cosine(left: tuple[float, ...], right: tuple[float, ...]) -> float:
    return sum(a * b for a, b in zip(left, right, strict=False))


def category_ids(branch: Branch, scope: Scope) -> tuple[str, ...]:
    if scope == "descendants":
        return branch.descendant_paper_ids
    return branch.direct_paper_ids


def branch_depth(branch: Branch) -> int:
    return branch.depth


def find_branch_outliers(
    branch: Branch,
    *,
    papers: dict[str, Paper],
    embeddings: dict[str, tuple[float, ...]],
    scope: Scope,
    min_items: int,
    min_similarity: float,
    min_drop_from_mean: float,
    max_outliers_per_branch: int,
) -> Finding | None:
    ids = tuple(paper_id for paper_id in category_ids(branch, scope) if paper_id in embeddings)
    if len(ids) < min_items:
        return None

    vectors = {paper_id: embeddings[paper_id] for paper_id in ids}
    pairwise: dict[tuple[str, str], float] = {}
    pair_values: list[float] = []
    for i, left_id in enumerate(ids):
        for right_id in ids[i + 1 :]:
            value = cosine(vectors[left_id], vectors[right_id])
            pairwise[(left_id, right_id)] = value
            pairwise[(right_id, left_id)] = value
            pair_values.append(value)

    if not pair_values:
        return None
    mean_pairwise = sum(pair_values) / len(pair_values)

    outliers: list[Outlier] = []
    for paper_id in ids:
        peer_scores = [(other_id, pairwise[(paper_id, other_id)]) for other_id in ids if other_id != paper_id]
        mean_to_peers = sum(score for _, score in peer_scores) / len(peer_scores)
        closest_peer_id, closest_score = max(peer_scores, key=lambda item: item[1])
        if mean_to_peers >= min_similarity and mean_pairwise - mean_to_peers < min_drop_from_mean:
            continue
        outliers.append(
            Outlier(
                paper=papers[paper_id],
                mean_similarity_to_peers=mean_to_peers,
                closest_peer_id=closest_peer_id,
                closest_peer_title=papers[closest_peer_id].title,
                closest_peer_similarity=closest_score,
            )
        )

    if not outliers:
        return None
    outliers = sorted(outliers, key=lambda item: item.mean_similarity_to_peers)
    return Finding(
        branch=branch,
        audited_ids=ids,
        mean_pairwise_similarity=mean_pairwise,
        outliers=tuple(outliers[:max_outliers_per_branch]),
    )


def find_outliers(
    branches: list[Branch],
    *,
    papers: dict[str, Paper],
    embeddings: dict[str, tuple[float, ...]],
    scope: Scope,
    min_items: int,
    min_similarity: float,
    min_drop_from_mean: float,
    max_depth: int | None,
    branch_filter: str | None,
    max_outliers_per_branch: int,
) -> list[Finding]:
    branch_filter_folded = branch_filter.casefold() if branch_filter else None
    findings: list[Finding] = []
    for branch in branches:
        if max_depth is not None and branch_depth(branch) > max_depth:
            continue
        if branch_filter_folded and branch_filter_folded not in format_path(branch.path).casefold():
            continue
        finding = find_branch_outliers(
            branch,
            papers=papers,
            embeddings=embeddings,
            scope=scope,
            min_items=min_items,
            min_similarity=min_similarity,
            min_drop_from_mean=min_drop_from_mean,
            max_outliers_per_branch=max_outliers_per_branch,
        )
        if finding is not None:
            findings.append(finding)

    return sorted(
        findings,
        key=lambda finding: (
            finding.outliers[0].mean_similarity_to_peers,
            format_path(finding.branch.path),
        ),
    )
