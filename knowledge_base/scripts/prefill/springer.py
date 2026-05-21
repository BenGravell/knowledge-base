"""Batch-prefill metadata.yml files from a list of Springer/SpringerLink URLs.

Usage:
    python knowledge_base/scripts/prefill/springer.py [--input PATH] [--overwrite]

Defaults:
    --input      todo/papers/SPRINGER.md
    --overwrite  False (skip entries whose metadata.yml already exists)

DOIs are extracted directly from Springer URLs, e.g.:
    https://link.springer.com/article/10.1007/BF00115009  →  10.1007/BF00115009
    https://link.springer.com/chapter/10.1007/978-3-642-19457-3_1  →  10.1007/978-3-642-19457-3_1
"""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.doi_utils import (
    fetch_page_html,
    scrape_abstract_from_html,
)
from knowledge_base.utils.prefill_template import DoiPrefillScript, REPO_ROOT
from knowledge_base.utils.prefill_utils import read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "SPRINGER.md"

# Captures the DOI portion from article/ or chapter/ paths
_SPRINGER_DOI_RE = re.compile(r"link\.springer\.com/(?:article|chapter|book|referenceworkentry)/(\S+?)(?:\s|$)")


def extract_entries(path: Path, on_parse_failure=None) -> list[tuple[str, str]]:
    """Return (original_url, doi) pairs, deduplicated by DOI."""
    seen: set[str] = set()
    entries: list[tuple[str, str]] = []
    for url in read_url_lines(path):
        m = _SPRINGER_DOI_RE.search(url)
        if not m:
            message = f"could not parse Springer DOI from: {url!r}"
            if on_parse_failure:
                on_parse_failure(message)
            else:
                print(f"  WARN: {message}")
            continue
        doi = m.group(1).rstrip("/")
        if doi and doi not in seen:
            seen.add(doi)
            entries.append((url, doi))
    return entries


class SpringerPrefill(DoiPrefillScript[tuple[str, str]]):
    description = "Prefill metadata from Springer URLs."
    default_input = DEFAULT_INPUT

    def extract_entries(self, path: Path) -> list[tuple[str, str]]:
        return extract_entries(path, self.record_parse_failure)

    def entry_label(self, entry: tuple[str, str]) -> str:
        return entry[1]

    def entry_doi(self, entry: tuple[str, str]) -> str:
        return entry[1]

    def postprocess_crossref_data(self, entry: tuple[str, str], data: dict) -> dict:
        url, _doi = entry
        if data["abstract"]:
            return data
        try:
            abstract = scrape_abstract_from_html(fetch_page_html(url))
        except Exception:
            return data
        return {**data, "abstract": abstract} if abstract else data


def main() -> None:
    SpringerPrefill().run()


if __name__ == "__main__":
    main()
