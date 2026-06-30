"""Batch-prefill metadata.yml files from a list of IEEE Xplore URLs.

Usage:
    python -m knowledge_base.prefill ieee [--input PATH] [--overwrite]

Defaults:
    --input      todo/papers/IEEE.md
    --overwrite  False (skip entries whose metadata.yml already exists)

Strategy:
  1. Extract the article number from each IEEE Xplore URL.
     Supports both /document/<id> and /abstract/document/<id> forms.
  2. Fetch the IEEE Xplore page for that article and scrape the DOI from
     embedded metadata (citation_doi meta tag or JSON payload).
  3. Query Crossref with the DOI for full, structured metadata.
  4. Write metadata.yml.
"""

import re
from collections.abc import Callable
from pathlib import Path

from knowledge_base.prefill.doi import (
    fetch_page_html,
    scrape_doi_from_html,
)
from knowledge_base.prefill.runner import REPO_ROOT
from knowledge_base.prefill.todo_file import read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "IEEE.md"

_IEEE_ARTICLE_RE = re.compile(
    r"ieeexplore\.ieee\.org/(?:abstract/)?document/(\d+)",
    re.I,
)

# IEEE Xplore internal REST endpoint used by their own website
_IEEE_REST_TMPL = "https://ieeexplore.ieee.org/rest/document/{article_id}/metadata"
_IEEE_PAGE_TMPL = "https://ieeexplore.ieee.org/document/{article_id}"


def extract_articles(path: Path, on_parse_failure: Callable[[str], None] | None = None) -> list[tuple[str, str]]:
    """Return (url, article_id) pairs, deduplicated."""
    seen: set[str] = set()
    entries: list[tuple[str, str]] = []
    for line in read_url_lines(path):
        m = _IEEE_ARTICLE_RE.search(line)
        if not m:
            message = f"could not parse IEEE article ID from: {line!r}"
            if on_parse_failure:
                on_parse_failure(message)
            else:
                print(f"  WARN: {message}")
            continue
        article_id = m.group(1)
        url = _IEEE_PAGE_TMPL.format(article_id=article_id)
        if article_id not in seen:
            seen.add(article_id)
            entries.append((url, article_id))
    return entries


def fetch_ieee_doi(article_id: str) -> str:
    """Return the DOI for an IEEE Xplore article, trying REST then HTML."""
    rest_url = _IEEE_REST_TMPL.format(article_id=article_id)
    page_url = _IEEE_PAGE_TMPL.format(article_id=article_id)

    # Try the internal REST API first (JSON, no JS required)
    try:
        import requests

        r = requests.get(
            rest_url,
            headers={
                "Accept": "application/json, */*",
                "Referer": page_url,
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0.0.0 Safari/537.36"
                ),
            },
            timeout=60,
        )
        if r.ok:
            payload = r.json()
            # The payload is typically a list; first item has the doi
            item = payload[0] if isinstance(payload, list) else payload
            doi = (item.get("doi") or item.get("doiLink") or "").strip()
            if doi and doi.startswith("10."):
                return doi
    except Exception:
        pass  # fall through to HTML scraping

    # Fall back: fetch the full HTML page and scrape
    html = fetch_page_html(page_url, extra_headers={"Referer": "https://ieeexplore.ieee.org/"})
    return scrape_doi_from_html(html)


def extract_entries(path: Path, on_parse_failure: Callable[[str], None] | None = None) -> list[tuple[str, str]]:
    return extract_articles(path, on_parse_failure)


def entry_label(entry: tuple[str, str]) -> str:
    _url, article_id = entry
    return article_id


def source_key_for_token(token: str) -> str | None:
    match = _IEEE_ARTICLE_RE.search(token)
    return match.group(1) if match else None


def resolve_doi(entry: tuple[str, str]) -> str:
    _url, article_id = entry
    return fetch_ieee_doi(article_id)
