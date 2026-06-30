"""Shared data types for branching-factor audits."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from knowledge_base.components.tree.model import TreeBranch as Branch

CountMode = Literal["all", "branches"]


@dataclass(frozen=True)
class Violation:
    branch: Branch
    count: int
    reason: Literal["too few", "too many"]
    distance_from_sweet_spot: int


__all__ = ["Branch", "CountMode", "Violation"]
