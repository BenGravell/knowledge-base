"""Metadata path and slug audit helpers."""

import re
from pathlib import Path
from typing import Any

from knowledge_base.scripts.audit_metadata.support.model import Issue
from knowledge_base.scripts.audit_metadata.support.slugs import expected_slug


def find_path_issues(
    path: Path,
    data: dict[str, Any],
    authors: list[Any],
    title: str,
    arxiv_id: str,
) -> tuple[list[Issue], bool]:
    issues: list[Issue] = []
    parts = path.parts
    try:
        papers_idx = next(i for i, p in enumerate(parts) if p == "papers")
        path_year_str = parts[papers_idx + 1]
        path_slug = "/".join(parts[papers_idx + 2 : -1])
    except (StopIteration, IndexError):
        return [Issue(path, "path", "Cannot locate papers/YEAR/SLUG in path")], True

    if not path_slug:
        return [Issue(path, "path", "Cannot locate papers/YEAR/SLUG in path")], True

    if not re.match(r"^\d{4}$", path_year_str):
        return [Issue(path, "path", f"YEAR component {path_year_str!r} is not 4 digits")], True

    path_year = int(path_year_str)
    meta_year = data.get("year")
    try:
        meta_year_int = int(meta_year) if meta_year is not None else None
    except (TypeError, ValueError):
        meta_year_int = None
    if meta_year_int is not None and meta_year_int != path_year:
        issues.append(
            Issue(
                path,
                "path",
                f"Metadata year {meta_year!r} does not match path year {path_year}",
            )
        )

    author_strs = [str(a) for a in (authors or [])]
    if author_strs and title:
        exp = expected_slug(path_year, arxiv_id, title, author_strs)
        if path_slug != exp:
            issues.append(
                Issue(
                    path,
                    "path",
                    f"Slug {path_slug!r} does not match expected {exp!r}",
                    exp,
                )
            )

    return issues, False


__all__ = ["find_path_issues"]
