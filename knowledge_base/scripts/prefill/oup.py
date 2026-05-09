"""Batch-prefill metadata.yml files from Oxford Academic URLs."""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import REPO_ROOT, UrlDoiPrefillScript

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "OUP.md"

_OUP_COMJNL_RE = re.compile(r"academic\.oup\.com/comjnl/article(?:-abstract)?/(\d+)/(\d+)/(\d+)/", re.I)


class OupPrefill(UrlDoiPrefillScript):
    description = "Prefill metadata from Oxford Academic URLs."
    default_input = DEFAULT_INPUT
    source_hint = "Oxford Academic"

    def accept_url(self, url: str) -> bool:
        return "academic.oup.com/" in url

    def entry_doi(self, entry: str) -> str | None:
        match = _OUP_COMJNL_RE.search(entry)
        if match:
            volume, issue, page = match.groups()
            return f"10.1093/comjnl/{int(volume)}.{int(issue)}.{int(page)}"
        return super().entry_doi(entry)


def main() -> None:
    OupPrefill().run()


if __name__ == "__main__":
    main()
