"""Models for unplaced-paper reporting."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Paper:
    id: str
    title: str
    algorithm: str
    metadata_path: Path
    generated_path: str
    abstract: str
    tags: tuple[str, ...]
