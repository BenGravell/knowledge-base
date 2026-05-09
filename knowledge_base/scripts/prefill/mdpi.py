"""Batch-prefill metadata.yml files from MDPI URLs."""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import REPO_ROOT, UrlDoiPrefillScript

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "MDPI.md"

_MDPI_ARTICLE_RE = re.compile(r"mdpi\.com/(?P<issn>\d{4}-\d{3}[\dX])/(?P<volume>\d+)/(?P<issue>\d+)/(?P<article>\d+)", re.I)
_JOURNAL_BY_ISSN = {
    "2413-8851": "urbansci",
}


class MdpiPrefill(UrlDoiPrefillScript):
    description = "Prefill metadata from MDPI URLs."
    default_input = DEFAULT_INPUT
    source_hint = "MDPI"

    def accept_url(self, url: str) -> bool:
        return "mdpi.com/" in url

    def entry_doi(self, entry: str) -> str | None:
        match = _MDPI_ARTICLE_RE.search(entry)
        if match and match.group("issn") in _JOURNAL_BY_ISSN:
            journal = _JOURNAL_BY_ISSN[match.group("issn")]
            volume = int(match.group("volume"))
            issue = int(match.group("issue"))
            article = int(match.group("article"))
            return f"10.3390/{journal}{volume}{issue:02d}{article:04d}"
        return super().entry_doi(entry)


def main() -> None:
    MdpiPrefill().run()


if __name__ == "__main__":
    main()
