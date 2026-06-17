"""Batch-prefill metadata.yml files from RAND URLs."""

from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import REPO_ROOT

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "RAND.md"


def accept_url(url: str) -> bool:
    return "rand.org/" in url
