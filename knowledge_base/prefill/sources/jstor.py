"""Batch-prefill metadata.yml files from JSTOR stable URLs."""

import re
from collections.abc import Callable
from pathlib import Path
from typing import Any

from knowledge_base.prefill.runner import REPO_ROOT
from knowledge_base.prefill.todo_file import read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "JSTOR.md"

_STABLE_RE = re.compile(r"jstor\.org/stable/([^/?#\s]+)", re.I)
_DOI_BY_STABLE_ID = {
    "2238545": "10.1214/aoms/1177703591",
    "23358653": "10.1287/moor.1120.0566",
    "43633451": "10.1090/qam/10666",
    "43633461": "10.1090/qam/10667",
}


def doi_for_stable_id(stable_id: str) -> str:
    return _DOI_BY_STABLE_ID.get(stable_id, f"10.2307/{stable_id}")


def extract_entries(path: Path, on_parse_failure: Callable[[str], None] | None = None) -> list[tuple[str, str, str]]:
    seen: set[str] = set()
    entries: list[tuple[str, str, str]] = []
    for url in read_url_lines(path):
        match = _STABLE_RE.search(url)
        if not match:
            message = f"could not parse JSTOR stable URL from: {url!r}"
            if on_parse_failure:
                on_parse_failure(message)
            else:
                print(f"  WARN: {message}")
            continue
        stable_id = match.group(1)
        doi = doi_for_stable_id(stable_id)
        if doi.lower() not in seen:
            seen.add(doi.lower())
            entries.append((url, stable_id, doi))
    return entries


def entry_label(entry: tuple[str, str, str]) -> str:
    _url, stable_id, _doi = entry
    return stable_id


def entry_doi(entry: tuple[str, str, str]) -> str:
    _url, _stable_id, doi = entry
    return doi


def source_key_for_token(token: str) -> str | None:
    match = _STABLE_RE.search(token)
    return match.group(1) if match else None


def source_key_for_entry(entry: tuple[str, str, str]) -> str | None:
    _url, stable_id, _doi = entry
    return stable_id


def postprocess_crossref_data(entry: tuple[str, str, str], data: dict[str, Any]) -> dict[str, Any]:
    url, _stable_id, _doi = entry
    return {**data, "link": url}
