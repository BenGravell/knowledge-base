"""Helpers for stable generated paper IDs."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


def slugify_paper_id(name: str) -> str:
    """Match the generated paper page naming convention."""
    return re.sub(r"[^a-zA-Z0-9]+", "_", str(name).lower()).strip("_")


def metadata_slug_source(
    metadata_file: Path,
    metadata_root: Path | None = None,
) -> str:
    """Return the source slug path under ``docs/papers/<YEAR>/``.

    Old-style arXiv IDs contain a slash, e.g. ``cond-mat/0112110``.  Those are
    stored as nested directories, so the generated page ID must be based on the
    full slug path rather than only the immediate parent directory.
    """
    parent = metadata_file.parent
    roots: list[Path] = []
    if metadata_root is not None:
        roots.append(metadata_root)
    roots.append(Path("docs/papers"))

    for root in roots:
        try:
            rel = parent.relative_to(root)
        except ValueError:
            continue
        parts = rel.parts
        if len(parts) >= 2 and re.fullmatch(r"\d{4}", parts[0]):
            return "/".join(parts[1:])

    parts = metadata_file.parts
    try:
        papers_idx = next(i for i, part in enumerate(parts) if part == "papers")
    except StopIteration:
        return parent.name

    slug_parts = parts[papers_idx + 2 : -1]
    return "/".join(slug_parts) if slug_parts else parent.name


def paper_id_from_metadata(
    metadata_file: Path,
    data: dict[str, Any] | None = None,
    metadata_root: Path | None = None,
) -> str:
    """Return the generated page ID for a metadata-backed paper."""
    data = data or {}
    if "id" in data:
        return slugify_paper_id(str(data["id"]))
    if metadata_file.stem != "metadata":
        return slugify_paper_id(metadata_file.stem)
    return slugify_paper_id(metadata_slug_source(metadata_file, metadata_root))
