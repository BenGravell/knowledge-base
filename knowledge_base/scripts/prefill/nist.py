"""Batch-prefill metadata.yml files from NIST/NBS PDFs."""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import PdfTextPrefillScript, REPO_ROOT
from knowledge_base.utils.prefill_utils import clean_text

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "NIST.md"


class NistPrefill(PdfTextPrefillScript):
    description = "Prefill metadata from NIST/NBS PDFs."
    default_input = DEFAULT_INPUT
    source_hint = "NIST"

    def accept_url(self, url: str) -> bool:
        return "nist.gov/" in url and url.lower().endswith(".pdf")

    def fields_from_pdf(self, url: str, text: str) -> dict:
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


def main() -> None:
    NistPrefill().run()


if __name__ == "__main__":
    main()
