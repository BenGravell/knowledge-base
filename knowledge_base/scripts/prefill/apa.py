"""Batch-prefill metadata.yml files from APA PsycNet URLs."""

from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import REPO_ROOT, UrlDoiPrefillScript

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "APA.md"


class ApaPrefill(UrlDoiPrefillScript):
    description = "Prefill metadata from APA PsycNet URLs."
    default_input = DEFAULT_INPUT
    source_hint = "APA PsycNet"

    def accept_url(self, url: str) -> bool:
        return "psycnet.apa.org/" in url


def main() -> None:
    ApaPrefill().run()


if __name__ == "__main__":
    main()
