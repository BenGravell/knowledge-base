"""Batch-prefill metadata.yml files from JMLR URLs."""

import re

from knowledge_base.utils.prefill_template import REPO_ROOT

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "JMLR.md"

_JMLR_PDF_RE = re.compile(
    r"(?:www\.)?(?:jmlr\.org|jmlr\.csail\.mit\.edu)/papers/"
    r"(?:volume|v)(\d+)/([^/]+)/[^/]+\.pdf$",
    re.I,
)


def accept_url(url: str) -> bool:
    return "jmlr.org/" in url or "jmlr.csail.mit.edu/" in url


def normalize_url(url: str) -> str:
    match = _JMLR_PDF_RE.search(url)
    if match:
        volume, slug = match.groups()
        return f"https://jmlr.org/papers/v{volume}/{slug}.html"
    if url.endswith(".pdf"):
        return url[:-4] + ".html"
    return url
