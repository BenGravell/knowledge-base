"""Batch-prefill metadata.yml files from a list of PMLR/MLR URLs.

Usage:
    python knowledge_base/scripts/prefill/mlr.py [--input PATH] [--overwrite]

Defaults:
    --input      todo/papers/MLR.md
    --overwrite  False (skip entries whose metadata.yml already exists)

The script scrapes PMLR citation meta tags and abstract text, then writes a
raw metadata.yml entry using the repository's non-arXiv folder convention.
"""

from pathlib import Path

if __package__ in (None, ""):
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.doi_utils import (
    fetch_page_html,
)
from knowledge_base.utils.prefill_template import PagePrefillScript
from knowledge_base.utils.prefill_utils import (
    absolutize_url,
    clean_text,
    element_text_by_id,
    first_element_text,
    first_meta,
    meta_contents,
    read_url_lines,
)

DEFAULT_INPUT = Path(__file__).parent.parent.parent.parent / "todo" / "papers" / "MLR.md"


def normalize_url(url: str) -> str:
    """Normalize a PMLR paper URL to the HTML page."""
    url = url.rstrip("/")
    if not url.endswith(".html"):
        url = f"{url}.html"
    return url


def extract_entries(path: Path) -> list[str]:
    """Return deduplicated normalized PMLR URLs."""
    seen: set[str] = set()
    entries: list[str] = []
    for url in read_url_lines(path):
        if "proceedings.mlr.press/" not in url:
            print(f"  WARN: could not parse PMLR URL from: {url!r}")
            continue
        normalized = normalize_url(url)
        if normalized not in seen:
            seen.add(normalized)
            entries.append(normalized)
    return entries


def fetch_mlr_fields(url: str) -> dict:
    html = fetch_page_html(url)
    title = first_meta(html, "citation_title") or first_element_text(html, "h1")
    authors = meta_contents(html, "citation_author")
    year_raw = first_meta(html, "citation_publication_date")
    year = int(year_raw[:4]) if year_raw[:4].isdigit() else 0
    source = first_meta(html, "citation_conference_title", "citation_inbook_title")

    abstract = element_text_by_id(html, "abstract")
    if not abstract:
        abstract = clean_text(first_meta(html, "citation_abstract", "description"))

    pdf_url = first_meta(html, "citation_pdf_url")
    link = absolutize_url(url, pdf_url) if pdf_url else url
    links_alt = [url] if link != url else []

    if not title or not authors or not year:
        raise ValueError(f"Incomplete PMLR metadata at {url!r}")

    return {
        "title": title,
        "authors": authors,
        "year": year,
        "source": source or "Proceedings of Machine Learning Research",
        "type": "Conference Paper",
        "abstract": abstract,
        "link": link,
        "links_alt": links_alt,
    }


class MlrPrefill(PagePrefillScript[str]):
    description = "Prefill metadata from PMLR/MLR URLs."
    default_input = DEFAULT_INPUT
    entry_kind = "PMLR URLs"

    def extract_entries(self, path: Path) -> list[str]:
        return extract_entries(path)

    def fetch_fields(self, entry: str, _context: dict) -> dict:
        return fetch_mlr_fields(entry)


def main() -> None:
    MlrPrefill().run()


if __name__ == "__main__":
    main()
