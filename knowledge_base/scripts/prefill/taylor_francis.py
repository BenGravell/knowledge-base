"""Batch-prefill metadata.yml files from a list of Taylor & Francis URLs.

Usage:
    python knowledge_base/scripts/prefill/taylor_francis.py [--input PATH] [--overwrite]

Defaults:
    --input      todo/papers/TAYLOR_FRANCIS.md
    --overwrite  False (skip entries whose metadata.yml already exists)

DOIs are extracted directly from Taylor & Francis URLs, e.g.:
    https://www.tandfonline.com/doi/abs/10.1080/00423119208969994
        -> 10.1080/00423119208969994
"""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))
from urllib.parse import unquote

from knowledge_base.utils.doi_utils import (
    fetch_page_html,
    scrape_abstract_from_html,
)
from knowledge_base.utils.prefill_template import DoiPrefillScript, REPO_ROOT
from knowledge_base.utils.prefill_utils import read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "TAYLOR_FRANCIS.md"

_TF_DOI_RE = re.compile(r"tandfonline\.com/doi/(?:abs/|full/|pdf/|epdf/)?([^\s?#]+)", re.I)


def extract_entries(path: Path, on_parse_failure=None) -> list[tuple[str, str]]:
    """Return (original_url, doi) pairs, deduplicated by DOI."""
    seen: set[str] = set()
    entries: list[tuple[str, str]] = []
    for url in read_url_lines(path):
        m = _TF_DOI_RE.search(url)
        if not m:
            message = f"could not parse Taylor & Francis DOI from: {url!r}"
            if on_parse_failure:
                on_parse_failure(message)
            else:
                print(f"  WARN: {message}")
            continue
        doi = unquote(m.group(1)).rstrip("/")
        if doi and doi.lower() not in seen:
            seen.add(doi.lower())
            entries.append((url, doi))
    return entries


class TaylorFrancisPrefill(DoiPrefillScript[tuple[str, str]]):
    description = "Prefill metadata from Taylor & Francis URLs."
    default_input = DEFAULT_INPUT
    entry_kind = "Taylor & Francis DOIs"

    def extract_entries(self, path: Path) -> list[tuple[str, str]]:
        return extract_entries(path, self.record_parse_failure)

    def entry_label(self, entry: tuple[str, str]) -> str:
        return entry[1]

    def entry_doi(self, entry: tuple[str, str]) -> str:
        return entry[1]

    def postprocess_crossref_data(self, entry: tuple[str, str], data: dict) -> dict:
        url, _doi = entry
        data = {**data, "link": url}
        if data["abstract"]:
            return data
        try:
            abstract = scrape_abstract_from_html(fetch_page_html(url))
        except Exception:
            return data
        return {**data, "abstract": abstract} if abstract else data

    def postprocess_metadata(self, entry: tuple[str, str], _fields: dict, metadata: dict) -> dict:
        _url, doi = entry
        return {**metadata, "links_alt": [f"https://doi.org/{doi}"]}


def main() -> None:
    TaylorFrancisPrefill().run()


if __name__ == "__main__":
    main()
