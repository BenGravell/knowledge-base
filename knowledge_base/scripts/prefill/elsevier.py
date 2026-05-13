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
from pathlib import Path

if __package__ in (None, ""):
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.doi_utils import (
    fetch_doi_from_crossref_pii,
    fetch_page_html,
    scrape_doi_from_html,
)
from knowledge_base.utils.prefill_template import DoiPrefillScript, REPO_ROOT

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "ELSEVIER.md"

_SD_PII_RE = re.compile(r"sciencedirect\.com/science/article/(?:abs/|pii/)?pii/([A-Z0-9]+)", re.I)
_SD_PAGE_TMPL = "https://www.sciencedirect.com/science/article/pii/{pii}"


def extract_entries(path: Path, on_parse_failure=None) -> list[tuple[str, str]]:
    """Return (url, pii) pairs, deduplicated."""
    seen: set[str] = set()
    entries: list[tuple[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
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


class ElsevierPrefill(DoiPrefillScript[tuple[str, str]]):
    description = "Prefill metadata from ScienceDirect URLs."
    default_input = DEFAULT_INPUT
    entry_kind = "ScienceDirect PIIs"
    fetch_error_label = "fetching metadata"
    show_resolved_doi = True

    def extract_entries(self, path: Path) -> list[tuple[str, str]]:
        return extract_entries(path, self.record_parse_failure)

    def entry_label(self, entry: tuple[str, str]) -> str:
        _url, pii = entry
        return pii

    def resolve_doi(self, entry: tuple[str, str]) -> str:
        url, pii = entry
        return fetch_elsevier_doi(url, pii)


def main() -> None:
    ElsevierPrefill().run()


if __name__ == "__main__":
    main()
