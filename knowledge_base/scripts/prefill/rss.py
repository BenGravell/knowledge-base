"""Batch-prefill metadata.yml files from a list of RSS proceedings URLs.

Usage:
    python knowledge_base/scripts/prefill/rss.py [--input PATH] [--overwrite]

Defaults:
    --input      todo/papers/RSS.md
    --overwrite  False (skip entries whose metadata.yml already exists)

Accepts Robotics: Science and Systems PDF or HTML URLs. The script reads the
companion HTML page, extracts citation meta tags, the abstract, and the DOI
from the embedded BibTeX block when present.
"""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.doi_utils import fetch_page_html
from knowledge_base.utils.prefill_template import PagePrefillScript, REPO_ROOT
from knowledge_base.utils.prefill_utils import (
    absolutize_url,
    clean_text,
    first_element_text,
    first_meta,
    meta_contents,
    read_url_lines,
)

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "RSS.md"

_RSS_RE = re.compile(r"roboticsproceedings\.org/(rss\d{2})/(p\d+)\.(?:pdf|html)", re.I)
_BASE = "https://www.roboticsproceedings.org"


def extract_entries(path: Path) -> list[tuple[str, str, str]]:
    """Return deduplicated (html_url, pdf_url, key) tuples."""
    seen: set[str] = set()
    entries: list[tuple[str, str, str]] = []
    for url in read_url_lines(path):
        m = _RSS_RE.search(url)
        if not m:
            print(f"  WARN: could not parse RSS URL from: {url!r}")
            continue
        volume, paper = m.group(1).lower(), m.group(2)
        key = f"{volume}/{paper}"
        if key in seen:
            continue
        seen.add(key)
        html_url = f"{_BASE}/{volume}/{paper}.html"
        pdf_url = f"{_BASE}/{volume}/{paper}.pdf"
        entries.append((html_url, pdf_url, key))
    return entries


def extract_abstract(html: str) -> str:
    m = re.search(
        r"<b>\s*Abstract:\s*</b>\s*</p>\s*<p\b[^>]*>(.*?)</p>",
        html,
        flags=re.DOTALL | re.I,
    )
    return clean_text(m.group(1)) if m else ""


def extract_bibtex_doi(html: str) -> str:
    m = re.search(r"\bDOI\s*=\s*[{'\"]([^}'\"]+)[}'\"]", html, flags=re.I)
    return m.group(1).strip() if m else ""


def canonical_source(source: str) -> str:
    if source.startswith("Robotics: Science and Systems"):
        return "Robotics: Science and Systems"
    return source


def fetch_rss_fields(html_url: str, fallback_pdf_url: str) -> dict:
    html = fetch_page_html(html_url)
    title = first_meta(html, "citation_title") or first_element_text(html, "h3")
    authors = meta_contents(html, "citation_author")
    year_raw = first_meta(html, "citation_publication_date")
    year = int(year_raw[:4]) if year_raw[:4].isdigit() else 0
    source = canonical_source(first_meta(html, "citation_conference_title"))
    pdf_raw = first_meta(html, "citation_pdf_url")
    pdf_url = absolutize_url(html_url, pdf_raw) if pdf_raw else fallback_pdf_url
    doi = extract_bibtex_doi(html)
    abstract = extract_abstract(html)

    if not title or not authors or not year:
        raise ValueError(f"Incomplete RSS metadata at {html_url!r}")

    links_alt = [html_url]
    if doi:
        links_alt.append(f"https://doi.org/{doi}")

    return {
        "title": title,
        "authors": authors,
        "year": year,
        "source": source or "Robotics: Science and Systems",
        "type": "Conference Paper",
        "doi": doi or None,
        "abstract": abstract,
        "link": pdf_url,
        "links_alt": links_alt,
    }


class RssPrefill(PagePrefillScript[tuple[str, str, str]]):
    description = "Prefill metadata from RSS proceedings URLs."
    default_input = DEFAULT_INPUT
    entry_kind = "RSS papers"

    def extract_entries(self, path: Path) -> list[tuple[str, str, str]]:
        return extract_entries(path)

    def entry_label(self, entry: tuple[str, str, str]) -> str:
        _html_url, _pdf_url, key = entry
        return key

    def fetch_fields(self, entry: tuple[str, str, str], _context: dict) -> dict:
        html_url, pdf_url, _key = entry
        return fetch_rss_fields(html_url, pdf_url)


def main() -> None:
    RssPrefill().run()


if __name__ == "__main__":
    main()
