"""Batch-prefill metadata.yml files from RAND URLs."""

from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import CitationPagePrefillScript, REPO_ROOT

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "RAND.md"


class RandPrefill(CitationPagePrefillScript):
    description = "Prefill metadata from RAND URLs."
    default_input = DEFAULT_INPUT
    source_fallback = "RAND Corporation"
    type_fallback = "Technical Report"
    source_hint = "RAND"

    def accept_url(self, url: str) -> bool:
        return "rand.org/" in url


def main() -> None:
    RandPrefill().run()


if __name__ == "__main__":
    main()
