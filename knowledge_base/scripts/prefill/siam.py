"""Batch-prefill metadata.yml files from SIAM URLs."""

from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import REPO_ROOT, UrlDoiPrefillScript

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "SIAM.md"


class SiamPrefill(UrlDoiPrefillScript):
    description = "Prefill metadata from SIAM URLs."
    default_input = DEFAULT_INPUT
    source_hint = "SIAM"

    def accept_url(self, url: str) -> bool:
        return "epubs.siam.org/" in url


def main() -> None:
    SiamPrefill().run()


if __name__ == "__main__":
    main()
