"""Batch-prefill metadata.yml files from ASME Digital Collection URLs."""

import re

from knowledge_base.utils.prefill_template import REPO_ROOT

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "ASME.md"

_ARTICLE_ID_RE = re.compile(r"/article/[^/]+/[^/]+/[^/]+/(\d+)/", re.I)
_KNOWN_DOIS_BY_ARTICLE_ID = {
    # ASME blocks straightforward HTML scraping for this legacy URL.
    "384566": "10.1115/1.4037838",
}


def accept_url(url: str) -> bool:
    return "asmedigitalcollection.asme.org/" in url


def entry_doi(entry: str) -> str | None:
    match = _ARTICLE_ID_RE.search(entry)
    if match and match.group(1) in _KNOWN_DOIS_BY_ARTICLE_ID:
        return _KNOWN_DOIS_BY_ARTICLE_ID[match.group(1)]
    return None
