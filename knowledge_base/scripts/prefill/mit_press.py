"""Batch-prefill metadata.yml files from MIT Press Direct URLs."""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import REPO_ROOT, UrlDoiPrefillScript

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "MIT_PRESS.md"

_MIT_ARTICLE_RE = re.compile(r"direct\.mit\.edu/([^/]+)/article/(\d+)/(\d+)/(\d+)/", re.I)
_KNOWN_DOIS_BY_KEY = {
    ("neco", "6", "1", "147"): "10.1162/neco.1994.6.1.147",
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
        return super().entry_doi(entry)


def main() -> None:
    MitPressPrefill().run()


if __name__ == "__main__":
    main()
