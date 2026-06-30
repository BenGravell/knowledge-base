"""Data models for branch subgroup suggestions."""

from dataclasses import dataclass

from knowledge_base.scripts.tree_report_data import ReportPaper as Paper
from knowledge_base.tree.model import TreeBranch as Branch
from knowledge_base.tree.model import TreeChild as ChildItem


@dataclass(frozen=True)
class Cluster:
    name: str
    children: tuple[ChildItem, ...]
    mean_similarity: float


@dataclass(frozen=True)
class Suggestion:
    branch: Branch
    clustered_child_count: int
    skipped_child_count: int
    k: int
    silhouette: float
    score: float
    clusters: tuple[Cluster, ...]


__all__ = ["Cluster", "Paper", "Suggestion"]
