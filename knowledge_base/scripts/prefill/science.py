"""Batch-prefill metadata.yml files from Science/AAAS URLs."""

from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import REPO_ROOT, UrlDoiPrefillScript

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "SCIENCE.md"


class SciencePrefill(UrlDoiPrefillScript):
    description = "Prefill metadata from Science/AAAS URLs."
    default_input = DEFAULT_INPUT
    source_hint = "Science"

    def accept_url(self, url: str) -> bool:
        return "science.org/" in url


def main() -> None:
    SciencePrefill().run()


if __name__ == "__main__":
    main()
