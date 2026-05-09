"""Batch-prefill metadata.yml files from SAGE Journals URLs."""

from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import REPO_ROOT, UrlDoiPrefillScript

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "SAGE.md"


class SagePrefill(UrlDoiPrefillScript):
    description = "Prefill metadata from SAGE Journals URLs."
    default_input = DEFAULT_INPUT
    source_hint = "SAGE"

    def accept_url(self, url: str) -> bool:
        return "journals.sagepub.com/" in url


def main() -> None:
    SagePrefill().run()


if __name__ == "__main__":
    main()
