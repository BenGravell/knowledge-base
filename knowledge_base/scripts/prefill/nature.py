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
from collections.abc import Callable
from pathlib import Path
from typing import Any

from knowledge_base.utils.doi_utils import (
    fetch_crossref,
    fetch_page_html,
    fetch_with_retry,
    scrape_abstract_from_html,
    scrape_doi_from_html,
)
from knowledge_base.utils.prefill_template import REPO_ROOT
from knowledge_base.utils.prefill_utils import read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "NATURE.md"

_NATURE_ARTICLE_RE = re.compile(r"nature\.com/articles/([^/?#\s]+)", re.I)


def extract_entries(path: Path, on_parse_failure: Callable[[str], None] | None = None) -> list[tuple[str, str]]:
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


def fetch_nature_data(url: str, doi: str) -> dict[str, Any]:
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


def entry_label(entry: tuple[str, str]) -> str:
    return entry[1]


def entry_doi(entry: tuple[str, str]) -> str:
    return entry[1]


def source_key_for_token(token: str) -> str | None:
    match = _NATURE_ARTICLE_RE.search(token)
    if not match:
        return None
    return f"10.1038/{match.group(1).rstrip('/')}"


def fetch_fields(entry: tuple[str, str], context: dict[str, Any]) -> dict[str, Any]:
    _ = context
    url, doi = entry
    return fetch_nature_data(url, doi)
