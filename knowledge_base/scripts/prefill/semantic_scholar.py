"""Batch-prefill metadata.yml files from Semantic Scholar URLs."""

from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import REPO_ROOT, SemanticScholarPrefillScript

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "SEMANTIC_SCHOLAR.md"


class SemanticScholarPrefill(SemanticScholarPrefillScript):
    description = "Prefill metadata from Semantic Scholar URLs."
    default_input = DEFAULT_INPUT


def main() -> None:
    SemanticScholarPrefill().run()


if __name__ == "__main__":
    main()
