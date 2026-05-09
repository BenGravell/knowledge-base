"""Batch-prefill metadata.yml files from Wiley Online Library URLs."""

from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import REPO_ROOT, UrlDoiPrefillScript

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "WILEY.md"


class WileyPrefill(UrlDoiPrefillScript):
    description = "Prefill metadata from Wiley Online Library URLs."
    default_input = DEFAULT_INPUT
    source_hint = "Wiley"

    def accept_url(self, url: str) -> bool:
        return "onlinelibrary.wiley.com/" in url


def main() -> None:
    WileyPrefill().run()


if __name__ == "__main__":
    main()
