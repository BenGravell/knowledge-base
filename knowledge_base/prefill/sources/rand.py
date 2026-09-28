"""Batch-prefill metadata.yml files from RAND URLs."""

import re

from knowledge_base.prefill.runner import REPO_ROOT
from knowledge_base.prefill.todo_file import fetch_citation_page_fields

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "RAND.md"


def accept_url(url: str) -> bool:
    return "rand.org/" in url


def fetch_fields(entry: str, context: dict) -> dict:
    _ = context
    match = re.search(r"/P(\d+)\.pdf$", entry, re.I)
    if not match:
        raise ValueError(f"No RAND publication number in {entry!r}")
    page_url = f"https://www.rand.org/pubs/papers/P{match.group(1)}.html"
    fields = fetch_citation_page_fields(
        page_url, source_fallback="RAND Corporation", type_fallback="Technical Report"
    )
    authors = [
        f"{given.strip()} {family.strip()}" if given else family.strip()
        for author in fields["authors"]
        for family, _, given in [author.partition(",")]
    ]
    return {**fields, "authors": authors, "link": entry, "links_alt": [page_url]}
