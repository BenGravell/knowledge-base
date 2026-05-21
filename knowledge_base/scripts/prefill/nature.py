"""Batch-prefill metadata.yml files from a list of nature.com article URLs.

Usage:
    python knowledge_base/scripts/prefill/nature.py [--input PATH] [--overwrite]

Defaults:
    --input      todo/papers/NATURE.md
    --overwrite  False (skip entries whose metadata.yml already exists)

Nature article URLs map directly to Springer Nature DOIs, e.g.:
    https://www.nature.com/articles/s43588-023-00503-5
        -> 10.1038/s43588-023-00503-5
"""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.doi_utils import (
    fetch_crossref,
    fetch_page_html,
    fetch_with_retry,
    scrape_abstract_from_html,
    scrape_doi_from_html,
)
from knowledge_base.utils.prefill_template import DoiPrefillScript, REPO_ROOT
from knowledge_base.utils.prefill_utils import read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "NATURE.md"

_NATURE_ARTICLE_RE = re.compile(r"nature\.com/articles/([^/?#\s]+)", re.I)


def extract_entries(path: Path, on_parse_failure=None) -> list[tuple[str, str]]:
    """Return (original_url, doi) pairs, deduplicated by DOI."""
    seen: set[str] = set()
    entries: list[tuple[str, str]] = []
    for url in read_url_lines(path):
        m = _NATURE_ARTICLE_RE.search(url)
        if not m:
            message = f"could not parse Nature article ID from: {url!r}"
            if on_parse_failure:
                on_parse_failure(message)
            else:
                print(f"  WARN: {message}")
            continue
        doi = f"10.1038/{m.group(1).rstrip('/')}"
        if doi.lower() not in seen:
            seen.add(doi.lower())
            entries.append((url, doi))
    return entries


def fetch_nature_data(url: str, doi: str) -> dict:
    """Fetch Crossref metadata, with Nature-page DOI and abstract fallbacks."""
    try:
        data = fetch_with_retry(fetch_crossref, doi)
    except Exception:
        html = fetch_page_html(url)
        doi = scrape_doi_from_html(html)
        data = fetch_with_retry(fetch_crossref, doi)
        if not data["abstract"]:
            abstract = scrape_abstract_from_html(html)
            if abstract:
                data = {**data, "abstract": abstract}
    else:
        if not data["abstract"]:
            try:
                abstract = scrape_abstract_from_html(fetch_page_html(url))
                if abstract:
                    data = {**data, "abstract": abstract}
            except Exception:
                pass
    data["link"] = url
    return data


class NaturePrefill(DoiPrefillScript[tuple[str, str]]):
    description = "Prefill metadata from nature.com URLs."
    default_input = DEFAULT_INPUT
    entry_kind = "Nature DOIs"
    show_resolved_doi = True

    def extract_entries(self, path: Path) -> list[tuple[str, str]]:
        return extract_entries(path, self.record_parse_failure)

    def entry_label(self, entry: tuple[str, str]) -> str:
        return entry[1]

    def entry_doi(self, entry: tuple[str, str]) -> str:
        return entry[1]

    def fetch_fields(self, entry: tuple[str, str], _context: dict) -> dict:
        url, doi = entry
        return fetch_nature_data(url, doi)

    def postprocess_metadata(self, _entry: tuple[str, str], fields: dict, metadata: dict) -> dict:
        return {**metadata, "links_alt": [f"https://doi.org/{fields['doi']}"]}


def main() -> None:
    NaturePrefill().run()


if __name__ == "__main__":
    main()
