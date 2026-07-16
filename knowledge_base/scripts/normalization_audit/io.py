"""Normalization audit file loading."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from knowledge_base.config import KB_DIR
from knowledge_base.utils.normalization_db import load_yaml

NORMALIZATION_DIR = KB_DIR / "normalization"
AUTHORS_DB = NORMALIZATION_DIR / "authors.yml"
SOURCES_DB = NORMALIZATION_DIR / "sources.yml"
TAGS_DB = NORMALIZATION_DIR / "tags.yml"


def load_metadata(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data if isinstance(data, dict) else {}


def load_entries(path: Path, field: str) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(path)
    entries = load_yaml(path).get(field)
    return [entry for entry in entries if isinstance(entry, dict)] if isinstance(entries, list) else []
