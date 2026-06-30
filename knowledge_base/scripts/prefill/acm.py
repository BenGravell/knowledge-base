"""Batch-prefill metadata.yml files from a list of ACM DL URLs.

Usage:
    python knowledge_base/scripts/prefill/acm.py [--input PATH] [--overwrite]

Defaults:
    --input      todo/papers/ACM.md
    --overwrite  False (skip entries whose metadata.yml already exists)

DOIs are extracted directly from ACM DL URLs, including URL-escaped DOI
characters, e.g.:
    https://dl.acm.org/doi/10.1145/3624480  →  10.1145/3624480
    https://dl.acm.org/doi/full/10.1145/...  →  10.1145/...
"""

from collections.abc import Callable
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests

from knowledge_base.scripts.prefill.acm_data import DOI_ALIASES, FALLBACK_RECORDS, FIELD_OVERRIDES, LINK_OVERRIDES
from knowledge_base.utils.doi_utils import fetch_crossref, fetch_with_retry
from knowledge_base.utils.prefill_template import REPO_ROOT
from knowledge_base.utils.prefill_utils import extract_doi_from_url, read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "ACM.md"

Entry = tuple[str, str]

# ACM DL occasionally hosts legacy/imported records under 10.5555 pseudo-DOIs.
# Prefer the formal publisher DOI when it is known.


def is_acm_dl_url(url: str) -> bool:
    host = urlparse(url).netloc.lower().removeprefix("www.")
    return host == "dl.acm.org"


def extract_entries(path: Path, on_parse_failure: Callable[[str], None] | None = None) -> list[Entry]:
    seen: set[str] = set()
    entries: list[Entry] = []
    for url in read_url_lines(path):
        if not is_acm_dl_url(url):
            message = f"could not parse ACM DL URL from: {url!r}"
            if on_parse_failure:
                on_parse_failure(message)
            else:
                print(f"  WARN: {message}")
            continue
        doi = extract_doi_from_url(url)
        if not doi:
            message = f"could not parse DOI from ACM DL URL: {url!r}"
            if on_parse_failure:
                on_parse_failure(message)
            else:
                print(f"  WARN: {message}")
            continue
        key = doi.lower()
        if key not in seen:
            seen.add(key)
            entries.append((url, doi))
    return entries


def extract_dois(path: Path, on_parse_failure: Callable[[str], None] | None = None) -> list[str]:
    """Backward-compatible DOI-only view for callers/tests."""
    return [doi for _url, doi in extract_entries(path, on_parse_failure)]


def entry_label(entry: Entry) -> str:
    _url, doi = entry
    return doi


def entry_doi(entry: Entry) -> str:
    _url, doi = entry
    return DOI_ALIASES.get(doi.lower(), doi)


def source_key_for_entry(entry: Entry) -> str | None:
    _url, doi = entry
    return doi


def postprocess_crossref_data(entry: Entry, data: dict[str, Any]) -> dict[str, Any]:
    url, input_doi = entry
    link = LINK_OVERRIDES.get(input_doi.lower(), url)
    return {**data, "link": link}


def fetch_fields(entry: Entry, context: dict[str, Any]) -> dict[str, Any]:
    _ = context
    url, input_doi = entry
    doi_key = input_doi.lower()
    if doi_key in FALLBACK_RECORDS:
        return {**FALLBACK_RECORDS[doi_key], "link": FALLBACK_RECORDS[doi_key]["link"]}

    try:
        fields = fetch_with_retry(fetch_crossref, entry_doi(entry))
        fields = postprocess_crossref_data(entry, fields)
    except requests.HTTPError as exc:
        if exc.response is None or exc.response.status_code != 404:
            raise
        alias = DOI_ALIASES.get(doi_key)
        if not alias:
            raise
        fields = fetch_with_retry(fetch_crossref, alias)
        fields = {**fields, "link": url}
    overrides = FIELD_OVERRIDES.get(str(fields.get("doi") or "").lower())
    return {**fields, **overrides} if overrides else fields


def postprocess_metadata(entry: Entry, fields: dict[str, Any], metadata: dict[str, Any]) -> dict[str, Any]:
    _url, input_doi = entry
    doi = str(fields.get("doi") or entry_doi(entry) or "").strip()
    links_alt = list(metadata.get("links_alt") or [])
    links_alt.extend(fields.get("links_alt") or [])
    if doi and input_doi.lower() not in FALLBACK_RECORDS:
        links_alt.append(f"https://doi.org/{doi}")
    if input_doi != doi and input_doi.startswith("10."):
        links_alt.append(f"https://dl.acm.org/doi/{input_doi}")
    links_alt = list(dict.fromkeys(x for x in links_alt if x and x != metadata.get("link")))
    return {**metadata, "links_alt": links_alt}
