"""Batch-prefill metadata.yml files from Society for Imaging Science URLs."""

from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import REPO_ROOT, UrlDoiPrefillScript

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "IMAGING_SCIENCE.md"


class ImagingSciencePrefill(UrlDoiPrefillScript):
    description = "Prefill metadata from Society for Imaging Science URLs."
    default_input = DEFAULT_INPUT
    source_hint = "Imaging Science"

    def accept_url(self, url: str) -> bool:
        return "library.imaging.org/" in url


def main() -> None:
    ImagingSciencePrefill().run()


if __name__ == "__main__":
    main()
