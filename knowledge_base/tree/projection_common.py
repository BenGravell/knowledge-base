"""Shared helpers for generated Tree projections."""

from __future__ import annotations

import re
from pathlib import PurePosixPath
from typing import Any

from knowledge_base.catalog import Catalog
from knowledge_base.config import KB_DIR, PAPERS_DIR

SITE_CONFIG = KB_DIR / "zensical.yml"
TREE_YML = KB_DIR / "tree.yml"
METADATA_ROOT = PAPERS_DIR
UNCATEGORIZED_CATEGORY = "Uncategorized"


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def slugify_id(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return slug or "node"


def page_url(source: str) -> str:
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", source):
        return source
    if not source.endswith(".md"):
        return source

    path = PurePosixPath(source.removesuffix(".md"))
    if path.name == "index":
        path = path.parent

    target = str(path).strip("/")
    return "../" if not target else f"../{target}/"


def clean_text(value: Any) -> str:
    text = str(value or "").strip()
    return re.sub(r"[ \t\r\f\v]+", " ", text)


def collect_paper_details() -> dict[str, dict[str, Any]]:
    details: dict[str, dict[str, Any]] = {}
    for entry in Catalog.from_metadata_root(METADATA_ROOT).entries:
        source = entry.generated_source
        details[source] = {
            "id": entry.id,
            "label": entry.label,
            "title": clean_text(entry.title),
            "algorithm": clean_text(entry.algorithm),
            "authors": list(entry.authors),
            "year": entry.year,
            "yearValue": entry.year_value,
            "sourceName": clean_text(entry.source),
            "type": clean_text(entry.type),
            "doi": clean_text(entry.doi),
            "arxivId": clean_text(entry.arxiv_id),
            "primaryLink": entry.primary_link,
            "hasPrimaryLink": entry.has_primary_link,
            "alternateLinkCount": entry.alternate_link_count,
            "auditStatus": clean_text(entry.audit_status),
            "authorShort": entry.author_short,
            "tags": [clean_text(tag) for tag in entry.tags if clean_text(tag)],
            "abstract": clean_text(entry.abstract),
            "summary": clean_text(entry.summary),
            "mapUrl": entry.url("map"),
            "timelineUrl": entry.url("timeline"),
            "searchUrl": entry.url("search"),
        }
    return details
