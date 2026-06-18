"""Batch-prefill metadata.yml files from a list of ScienceDirect (Elsevier) URLs.

Usage:
    python knowledge_base/scripts/prefill/elsevier.py [--input PATH] [--overwrite]

Defaults:
    --input      todo/papers/ELSEVIER.md
    --overwrite  False (skip entries whose metadata.yml already exists)

Strategy:
  1. Extract the PII from each ScienceDirect URL.
  2. Fetch the ScienceDirect page and scrape the DOI from the citation_doi
     meta tag or embedded JSON metadata.
  3. Query Crossref with the DOI for full, structured metadata.
  4. Write metadata.yml.
"""

import re
from collections.abc import Callable
from pathlib import Path

from knowledge_base.utils.doi_utils import (
    fetch_doi_from_crossref_pii,
    fetch_page_html,
    scrape_doi_from_html,
)
from knowledge_base.utils.prefill_template import REPO_ROOT
from knowledge_base.utils.prefill_utils import read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "ELSEVIER.md"

_SD_PII_RE = re.compile(r"sciencedirect\.com/science/article/(?:abs/|pii/)?pii/([A-Z0-9]+)", re.I)
_SD_PAGE_TMPL = "https://www.sciencedirect.com/science/article/pii/{pii}"


def extract_entries(path: Path, on_parse_failure: Callable[[str], None] | None = None) -> list[tuple[str, str]]:
    """Return (url, pii) pairs, deduplicated."""
    seen: set[str] = set()
    entries: list[tuple[str, str]] = []
    for line in read_url_lines(path):
        m = _SD_PII_RE.search(line)
        if not m:
            message = f"could not parse ScienceDirect PII from: {line!r}"
            if on_parse_failure:
                on_parse_failure(message)
            else:
                print(f"  WARN: {message}")
            continue
        pii = m.group(1).upper()
        url = _SD_PAGE_TMPL.format(pii=pii)
        if pii not in seen:
            seen.add(pii)
            entries.append((url, pii))
    return entries


def fetch_elsevier_doi(url: str, pii: str) -> str:
    """Return the DOI for a ScienceDirect article.

    Tries Crossref's alternative-id filter first (avoids scraping ScienceDirect,
    which blocks non-browser requests). Falls back to HTML scraping if needed.
    """
    try:
        return fetch_doi_from_crossref_pii(pii)
    except Exception:
        pass
    html = fetch_page_html(
        url,
        extra_headers={
            "Referer": "https://www.sciencedirect.com/",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    return scrape_doi_from_html(html)


def entry_label(entry: tuple[str, str]) -> str:
    _url, pii = entry
    return pii


def source_key_for_token(token: str) -> str | None:
    match = _SD_PII_RE.search(token)
    return match.group(1).upper() if match else None


def resolve_doi(entry: tuple[str, str]) -> str:
    url, pii = entry
    return fetch_elsevier_doi(url, pii)
