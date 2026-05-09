"""Batch-prefill metadata.yml files from Annual Reviews URLs."""

from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import REPO_ROOT, UrlDoiPrefillScript

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "ANNUAL_REVIEWS.md"


class AnnualReviewsPrefill(UrlDoiPrefillScript):
    description = "Prefill metadata from Annual Reviews URLs."
    default_input = DEFAULT_INPUT
    source_hint = "Annual Reviews"

    def accept_url(self, url: str) -> bool:
        return "annualreviews.org/" in url


def main() -> None:
    AnnualReviewsPrefill().run()


if __name__ == "__main__":
    main()
