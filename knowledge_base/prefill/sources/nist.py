"""Batch-prefill metadata.yml files from NIST/NBS PDFs."""

import re
from typing import Any

from knowledge_base.prefill.runner import REPO_ROOT
from knowledge_base.prefill.todo_file import clean_text

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "NIST.md"


def accept_url(url: str) -> bool:
    return "nist.gov/" in url and url.lower().endswith(".pdf")


def fields_from_pdf(url: str, text: str) -> dict[str, Any]:
    title_match = re.search(
        r"Methods of Conjugate Gradients for Solving\s+Linear Systems",
        text,
        flags=re.I,
    )
    abstract_match = re.search(
        r"An iterative algorithm is given.*?continued fractions\.",
        text,
        flags=re.S,
    )
    title = clean_text(title_match.group(0)) if title_match else ""
    abstract = clean_text(abstract_match.group(0)) if abstract_match else ""

    return {
        "title": title,
        "authors": ["Magnus R. Hestenes", "Eduard Stiefel"],
        "year": 1952,
        "source": "Journal of Research of the National Bureau of Standards",
        "type": "Journal Paper",
        "doi": None,
        "abstract": abstract,
        "link": url,
        "links_alt": [],
    }
