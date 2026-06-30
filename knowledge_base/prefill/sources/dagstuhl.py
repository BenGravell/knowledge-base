"""Batch-prefill metadata.yml files from Dagstuhl/LIPIcs URLs."""

import re
from collections.abc import Callable
from pathlib import Path
from typing import Any

from knowledge_base.prefill.runner import REPO_ROOT
from knowledge_base.prefill.todo_file import read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "DAGSTUHL.md"

_LIPICS_RE = re.compile(r"/(LIPIcs\.[^/]+)\.pdf$", re.I)


def extract_entries(path: Path, on_parse_failure: Callable[[str], None] | None = None) -> list[tuple[str, str]]:
    seen: set[str] = set()
    entries: list[tuple[str, str]] = []
    for url in read_url_lines(path):
        match = _LIPICS_RE.search(url)
        if not match:
            message = f"could not parse Dagstuhl DOI from: {url!r}"
            if on_parse_failure:
                on_parse_failure(message)
            else:
                print(f"  WARN: {message}")
            continue
        doi = f"10.4230/{match.group(1)}"
        if doi.lower() not in seen:
            seen.add(doi.lower())
            entries.append((url, doi))
    return entries


def entry_label(entry: tuple[str, str]) -> str:
    return entry[1]


def entry_doi(entry: tuple[str, str]) -> str:
    return entry[1]


def source_key_for_token(token: str) -> str | None:
    match = _LIPICS_RE.search(token)
    if not match:
        return None
    return f"10.4230/{match.group(1)}"


def postprocess_crossref_data(entry: tuple[str, str], data: dict[str, Any]) -> dict[str, Any]:
    url, _doi = entry
    return {**data, "link": url}
