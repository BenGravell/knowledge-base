"""Batch-prefill metadata.yml files from Optica Publishing Group URLs."""

from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import REPO_ROOT, UrlDoiPrefillScript

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "OPTICA.md"


class OpticaPrefill(UrlDoiPrefillScript):
    description = "Prefill metadata from Optica Publishing Group URLs."
    default_input = DEFAULT_INPUT
    source_hint = "Optica"

    def accept_url(self, url: str) -> bool:
        return "opg.optica.org/" in url


def main() -> None:
    OpticaPrefill().run()


if __name__ == "__main__":
    main()
