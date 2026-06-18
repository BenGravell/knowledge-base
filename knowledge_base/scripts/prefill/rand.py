"""Batch-prefill metadata.yml files from RAND URLs."""

from knowledge_base.utils.prefill_template import REPO_ROOT

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "RAND.md"


def accept_url(url: str) -> bool:
    return "rand.org/" in url
