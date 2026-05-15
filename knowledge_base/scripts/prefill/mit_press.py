"""Batch-prefill metadata.yml files from MIT Press Direct URLs."""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import REPO_ROOT, UrlDoiPrefillScript

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "MIT_PRESS.md"

_MIT_ARTICLE_RE = re.compile(r"direct\.mit\.edu/([^/]+)/article/(\d+)/(\d+)/(\d+)/", re.I)
_MIT_BOOK_RE = re.compile(r"direct\.mit\.edu/books/(?:book|monograph)/(\d+)/", re.I)
_KNOWN_DOIS_BY_KEY = {
    ("neco", "6", "1", "147"): "10.1162/neco.1994.6.1.147",
    ("evco", "9", "2", "159"): "10.1162/106365601750190398",
}
_KNOWN_DOIS_BY_BOOK_ID = {
    "2574": "10.7551/mitpress/1090.001.0001",
}


class MitPressPrefill(UrlDoiPrefillScript):
    description = "Prefill metadata from MIT Press Direct URLs."
    default_input = DEFAULT_INPUT
    source_hint = "MIT Press"

    def accept_url(self, url: str) -> bool:
        return "direct.mit.edu/" in url

    def entry_doi(self, entry: str) -> str | None:
        match = _MIT_ARTICLE_RE.search(entry)
        if match:
            key = match.groups()
            if key in _KNOWN_DOIS_BY_KEY:
                return _KNOWN_DOIS_BY_KEY[key]
        match = _MIT_BOOK_RE.search(entry)
        if match and match.group(1) in _KNOWN_DOIS_BY_BOOK_ID:
            return _KNOWN_DOIS_BY_BOOK_ID[match.group(1)]
        return super().entry_doi(entry)


def main() -> None:
    MitPressPrefill().run()


if __name__ == "__main__":
    main()
