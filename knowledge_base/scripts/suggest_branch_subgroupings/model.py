"""Data models for branch subgroup suggestions."""

from dataclasses import dataclass
from pathlib import Path

from knowledge_base.components.tree.model import TreeBranch as Branch
from knowledge_base.components.tree.model import TreeChild as ChildItem


@dataclass(frozen=True)
class Paper:
    id: str
    title: str
    algorithm: str
    tags: tuple[str, ...]
    metadata_path: Path


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
