"""Batch-prefill metadata.yml files from MIT Press Direct URLs."""

import re
from typing import Any

from knowledge_base.prefill.runner import REPO_ROOT

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "MIT_PRESS.md"

_MIT_ARTICLE_RE = re.compile(r"direct\.mit\.edu/([^/]+)/article/(\d+)/(\d+)/(\d+)/", re.I)
_MIT_ARTICLE_DOI_RE = re.compile(r"direct\.mit\.edu/[^?#]+/article/doi/(10\.\d{4,9}/[^/?#]+)/", re.I)
_MIT_BOOK_RE = re.compile(r"direct\.mit\.edu/books/(?:book|monograph)/(\d+)/", re.I)
_MIT_LEGACY_BOOK_RE = re.compile(r"mitpress\.mit\.edu/(\d{10,13})/", re.I)
_KNOWN_DOIS_BY_KEY = {
    ("neco", "6", "1", "147"): "10.1162/neco.1994.6.1.147",
    ("evco", "9", "2", "159"): "10.1162/106365601750190398",
}
_KNOWN_DOIS_BY_BOOK_ID = {
    "2574": "10.7551/mitpress/1090.001.0001",
    "3132": "10.7551/mitpress/11301.001.0001",
}
_KNOWN_DOIS_BY_ISBN = {
    "9780262630221": "10.7551/mitpress/11301.001.0001",
}


def accept_url(url: str) -> bool:
    return "direct.mit.edu/" in url or "mitpress.mit.edu/" in url


def entry_doi(entry: str) -> str | None:
    match = _MIT_ARTICLE_DOI_RE.search(entry)
    if match:
        return match.group(1)
    match = _MIT_ARTICLE_RE.search(entry)
    if match:
        key = match.groups()
        if key in _KNOWN_DOIS_BY_KEY:
            return _KNOWN_DOIS_BY_KEY[key]
    match = _MIT_BOOK_RE.search(entry)
    if match and match.group(1) in _KNOWN_DOIS_BY_BOOK_ID:
        return _KNOWN_DOIS_BY_BOOK_ID[match.group(1)]
    match = _MIT_LEGACY_BOOK_RE.search(entry)
    if match and match.group(1) in _KNOWN_DOIS_BY_ISBN:
        return _KNOWN_DOIS_BY_ISBN[match.group(1)]
    return None


def postprocess_crossref_data(entry: str, data: dict[str, Any]) -> dict[str, Any]:
    if _MIT_BOOK_RE.search(entry) or _MIT_LEGACY_BOOK_RE.search(entry):
        return {**data, "source": data.get("source") or "MIT Press", "type": "Book"}
    return data
