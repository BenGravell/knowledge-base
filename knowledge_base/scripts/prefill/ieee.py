"""Batch-prefill metadata.yml files from a list of IEEE Xplore URLs.

Usage:
    python knowledge_base/scripts/prefill/ieee.py [--input PATH] [--overwrite]

Defaults:
    --input      todo/papers/IEEE.md
    --overwrite  False (skip entries whose metadata.yml already exists)

Strategy:
  1. Extract the article number from each IEEE Xplore URL.
  2. Fetch the IEEE Xplore page for that article and scrape the DOI from
     embedded metadata (citation_doi meta tag or JSON payload).
  3. Query Crossref with the DOI for full, structured metadata.
  4. Write metadata.yml.
"""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.doi_utils import (
    fetch_page_html,
    scrape_doi_from_html,
)
from knowledge_base.utils.prefill_template import DoiPrefillScript

DEFAULT_INPUT = Path(__file__).parent.parent.parent.parent / "todo" / "papers" / "IEEE.md"

_IEEE_ARTICLE_RE = re.compile(r"ieeexplore\.ieee\.org/document/(\d+)")

# IEEE Xplore internal REST endpoint used by their own website
_IEEE_REST_TMPL = "https://ieeexplore.ieee.org/rest/document/{article_id}/metadata"
_IEEE_PAGE_TMPL = "https://ieeexplore.ieee.org/document/{article_id}"


def extract_articles(path: Path) -> list[tuple[str, str]]:
    """Return (url, article_id) pairs, deduplicated."""
    seen: set[str] = set()
    entries: list[tuple[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = _IEEE_ARTICLE_RE.search(line)
        if not m:
            print(f"  WARN: could not parse IEEE article ID from: {line!r}")
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
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 Chrome/124.0.0.0 Safari/537.36"
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


class IeeePrefill(DoiPrefillScript[tuple[str, str]]):
    description = "Prefill metadata from IEEE Xplore URLs."
    default_input = DEFAULT_INPUT
    entry_kind = "IEEE articles"
    fetch_error_label = "fetching metadata"
    show_resolved_doi = True

    def extract_entries(self, path: Path) -> list[tuple[str, str]]:
        return extract_articles(path)

    def entry_label(self, entry: tuple[str, str]) -> str:
        _url, article_id = entry
        return article_id

    def resolve_doi(self, entry: tuple[str, str]) -> str:
        _url, article_id = entry
        return fetch_ieee_doi(article_id)


def main() -> None:
    IeeePrefill().run()


if __name__ == "__main__":
    main()
