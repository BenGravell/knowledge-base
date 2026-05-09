"""Batch-prefill metadata.yml files from BMVA archive PDFs."""

from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import PdfTextPrefillScript, REPO_ROOT
from knowledge_base.utils.prefill_utils import clean_text, extract_doi

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "BMVA.md"


def split_authors(raw: str) -> list[str]:
    return [part.strip() for part in raw.replace(" and ", " & ").split("&") if part.strip()]


class BmvaPrefill(PdfTextPrefillScript):
    description = "Prefill metadata from BMVA archive PDFs."
    default_input = DEFAULT_INPUT
    source_hint = "BMVA"

    def accept_url(self, url: str) -> bool:
        return "bmva-archive.org.uk/" in url and url.lower().endswith(".pdf")

    def fields_from_pdf(self, url: str, text: str) -> dict:
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        title = clean_text(lines[0]).title() if lines else ""
        authors = split_authors(lines[1]) if len(lines) > 1 else []
        doi = extract_doi(text)

        abstract = ""
        if "1988" in text:
            blocks = [block.strip() for block in text.split("1988", 1)[1].split("\n\n") if block.strip()]
            if blocks:
                abstract = clean_text(blocks[0])

        if not title or not authors:
            raise ValueError(f"Incomplete BMVA PDF metadata for {url!r}")

        return {
            "title": title,
            "authors": authors,
            "year": 1988,
            "source": "Alvey Vision Conference",
            "type": "Conference Paper",
            "doi": doi or None,
            "abstract": abstract,
            "link": url,
            "links_alt": [f"https://doi.org/{doi}"] if doi else [],
        }


def main() -> None:
    BmvaPrefill().run()


if __name__ == "__main__":
    main()
