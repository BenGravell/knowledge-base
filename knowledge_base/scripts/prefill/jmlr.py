"""Batch-prefill metadata.yml files from JMLR URLs."""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import CitationPagePrefillScript, REPO_ROOT

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "JMLR.md"

_JMLR_PDF_RE = re.compile(r"jmlr\.csail\.mit\.edu/papers/volume(\d+)/([^/]+)/[^/]+\.pdf", re.I)


class JmlrPrefill(CitationPagePrefillScript):
    description = "Prefill metadata from JMLR URLs."
    default_input = DEFAULT_INPUT
    source_fallback = "Journal of Machine Learning Research"
    type_fallback = "Journal Paper"
    source_hint = "JMLR"

    def accept_url(self, url: str) -> bool:
        return "jmlr.org/" in url or "jmlr.csail.mit.edu/" in url

    def normalize_url(self, url: str) -> str:
        match = _JMLR_PDF_RE.search(url)
        if match:
            volume, slug = match.groups()
            return f"https://jmlr.org/papers/v{volume}/{slug}.html"
        if url.endswith(".pdf"):
            return url[:-4] + ".html"
        return url


def main() -> None:
    JmlrPrefill().run()


if __name__ == "__main__":
    main()
