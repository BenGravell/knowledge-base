"""Batch-prefill metadata.yml files from ASME Digital Collection URLs."""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import REPO_ROOT, UrlDoiPrefillScript

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "ASME.md"

_ARTICLE_ID_RE = re.compile(r"/article/[^/]+/[^/]+/[^/]+/(\d+)/", re.I)
_KNOWN_DOIS_BY_ARTICLE_ID = {
    # ASME blocks straightforward HTML scraping for this legacy URL.
    "384566": "10.1115/1.4037838",
}


class AsmePrefill(UrlDoiPrefillScript):
    description = "Prefill metadata from ASME Digital Collection URLs."
    default_input = DEFAULT_INPUT
    source_hint = "ASME"

    def accept_url(self, url: str) -> bool:
        return "asmedigitalcollection.asme.org/" in url

    def entry_doi(self, entry: str) -> str | None:
        match = _ARTICLE_ID_RE.search(entry)
        if match and match.group(1) in _KNOWN_DOIS_BY_ARTICLE_ID:
            return _KNOWN_DOIS_BY_ARTICLE_ID[match.group(1)]
        return super().entry_doi(entry)


def main() -> None:
    AsmePrefill().run()


if __name__ == "__main__":
    main()
