"""Suggestion model for tree algorithm labels."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Suggestion:
    nav_path: tuple[str, ...]
    tree_label: str
    algorithm: str
    title: str
    audit_status: str
    source: str
    metadata_path: Path
    action: str
    confidence: str
    suggested_tree_label: str | None
    suggested_metadata_algorithm: str | None
    canonical_label: str | None
    reason: str


__all__ = ["Suggestion"]
