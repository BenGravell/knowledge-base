"""Batch-prefill metadata.yml files from Mathematical Sciences Publishers URLs."""

import re
from collections.abc import Callable
from pathlib import Path
from typing import Any

from knowledge_base.utils.prefill_template import REPO_ROOT
from knowledge_base.utils.prefill_utils import read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "MSP.md"

_MSP_RE = re.compile(
    r"msp\.org/(?P<journal>[^/]+)/(?P<year>\d{4})/(?P<volume>\d+)-\d+/" r"[^/]+-p(?P<page>\d+)-p\.pdf$",
    re.I,
)


def extract_entries(path: Path, on_parse_failure: Callable[[str], None] | None = None) -> list[tuple[str, str]]:
    seen: set[str] = set()
    entries: list[tuple[str, str]] = []
    for url in read_url_lines(path):
        match = _MSP_RE.search(url)
        if not match:
            message = f"could not parse MSP DOI from: {url!r}"
            if on_parse_failure:
                on_parse_failure(message)
            else:
                print(f"  WARN: {message}")
            continue
        doi = "10.2140/{journal}.{year}.{volume}.{page}".format(
            journal=match.group("journal"),
            year=match.group("year"),
            volume=int(match.group("volume")),
            page=int(match.group("page")),
        )
        if doi.lower() not in seen:
            seen.add(doi.lower())
            entries.append((url, doi))
    return entries


def entry_label(entry: tuple[str, str]) -> str:
    return entry[1]


def entry_doi(entry: tuple[str, str]) -> str:
    return entry[1]


def source_key_for_token(token: str) -> str | None:
    match = _MSP_RE.search(token)
    if not match:
        return None
    return "10.2140/{journal}.{year}.{volume}.{page}".format(
        journal=match.group("journal"),
        year=match.group("year"),
        volume=int(match.group("volume")),
        page=int(match.group("page")),
    )


def postprocess_crossref_data(entry: tuple[str, str], data: dict[str, Any]) -> dict[str, Any]:
    url, _doi = entry
    return {**data, "link": url}
