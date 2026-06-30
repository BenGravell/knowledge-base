"""Normalization audit model and rule constants."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

TAG_DATABASE_ISSUE_PREFIX = "Tag differs from normalization database"
TAG_DATABASE_MISSING_PREFIX = "Tag is missing from normalization database"

RULE_AUTHOR_VALUE = "authors.value"
RULE_SOURCE_VALUE = "source.value"
RULE_TAG_VALUE = "tags.value"
RULE_TAG_DATABASE_MISSING = "tags.database-missing"


@dataclass(frozen=True)
class Issue:
    path: Path
    field: str
    message: str
    suggestion: str | None = None
    rule: str | None = None
    index: int | None = None
