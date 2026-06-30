"""Models for Tree embedding dissimilarity reports."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from knowledge_base.scripts.tree_report_data import ReportPaper as Paper
from knowledge_base.tree.model import TreeBranch as Branch

Scope = Literal["direct", "descendants"]


@dataclass(frozen=True)
class Outlier:
    paper: Paper
    mean_similarity_to_peers: float
    closest_peer_id: str | None
    closest_peer_title: str | None
    closest_peer_similarity: float | None


@dataclass(frozen=True)
class Finding:
    branch: Branch
    audited_ids: tuple[str, ...]
    mean_pairwise_similarity: float
    outliers: tuple[Outlier, ...]
