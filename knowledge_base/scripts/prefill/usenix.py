"""Batch-prefill metadata.yml files from USENIX PDFs."""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import PdfTextPrefillScript, REPO_ROOT
from knowledge_base.utils.prefill_utils import clean_text

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "USENIX.md"


def split_authors(raw: str) -> list[str]:
    return [part.strip() for part in raw.split(",") if part.strip()]


class UsenixPrefill(PdfTextPrefillScript):
    description = "Prefill metadata from USENIX PDFs."
    default_input = DEFAULT_INPUT
    source_hint = "USENIX"

    def accept_url(self, url: str) -> bool:
        return "usenix.org/" in url and url.lower().endswith(".pdf")

    def fields_from_pdf(self, url: str, text: str) -> dict:
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        title = clean_text(lines[0]) if lines else ""
        author_lines: list[str] = []
        for line in lines[1:]:
            if line.startswith("{") or line == "Google, Inc.":
                break
            author_lines.append(line)
        authors = split_authors(", ".join(author_lines))

        abstract_match = re.search(r"\bAbstract\s+(.*?)\s+1 Introduction\b", text, flags=re.S)
        abstract = clean_text(abstract_match.group(1)) if abstract_match else ""

        if not title or not authors:
            raise ValueError(f"Incomplete USENIX PDF metadata for {url!r}")

        return {
            "title": title,
            "authors": authors,
            "year": 2006,
            "source": "USENIX Symposium on Operating Systems Design and Implementation",
            "type": "Conference Paper",
            "doi": None,
            "abstract": abstract,
            "link": url,
            "links_alt": [],
        }


def main() -> None:
    UsenixPrefill().run()


if __name__ == "__main__":
    main()
