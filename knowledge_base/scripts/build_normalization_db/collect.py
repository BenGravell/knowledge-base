"""Collect observed normalization values from metadata."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

import yaml

from knowledge_base.config import PAPERS_DIR
from knowledge_base.utils.normalization_db import load_yaml


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def load_metadata(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data if isinstance(data, dict) else {}


def collect_values() -> tuple[Counter[str], Counter[str], Counter[str]]:
    authors: Counter[str] = Counter()
    sources: Counter[str] = Counter()
    tags: Counter[str] = Counter()
    for metadata_path in sorted(PAPERS_DIR.rglob("metadata.yml")):
        data = load_metadata(metadata_path)
        for author in as_list(data.get("authors")):
            author_text = str(author).strip()
            if author_text:
                authors[author_text] += 1

        source = str(data.get("source") or "").strip()
        if source:
            sources[source] += 1

        for tag in as_list(data.get("tags")):
            tag_text = str(tag).strip()
            if tag_text:
                tags[tag_text] += 1
    return authors, sources, tags


def existing_entries(path: Path, field: str) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    entries = load_yaml(path).get(field)
    return [entry for entry in entries if isinstance(entry, dict)] if isinstance(entries, list) else []
