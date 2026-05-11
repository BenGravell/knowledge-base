"""Batch-prefill metadata.yml files from a list of arXiv URLs/IDs.

Usage:
    python knowledge_base/scripts/prefill/arxiv.py [--input PATH] [--overwrite]

Defaults:
    --input  todo/papers/ARXIV.md
    --overwrite  False (skip IDs whose metadata.yml already exists)
"""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))

import requests

from knowledge_base.apps.arxiv_utils import (
    build_metadata,
    fetch_arxiv,
    target_path,
    write_metadata,
)
from knowledge_base.utils.prefill_template import HaltPrefill, PrefillScript, REPO_ROOT
from knowledge_base.utils.doi_utils import find_existing_by_arxiv_id

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "ARXIV.md"
ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/([^\s/?#]+)")

# Duration in seconds between successful requests
# Set to 5 seconds, well above 3 seconds required by arXiv Terms of Use (which requries 3 seconds)
# https://info.arxiv.org/help/api/tou.html
BASE_DELAY = 5.0      
# Max number of retries for transient (non-HTTP) errors
MAX_RETRIES = 5


def extract_ids(path: Path) -> list[str]:
    seen: set[str] = set()
    ids: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = ARXIV_ID_RE.search(line)
        arxiv_id = m.group(1) if m else line
        arxiv_id = arxiv_id.rstrip("/")
        if arxiv_id and arxiv_id not in seen:
            seen.add(arxiv_id)
            ids.append(arxiv_id)
    return ids


def fetch_with_retry(arxiv_id: str) -> dict:
    for _attempt in range(MAX_RETRIES):
        try:
            return fetch_arxiv(arxiv_id)
        except requests.HTTPError as exc:
            if exc.response is not None and exc.response.status_code == 429:
                raise HaltPrefill(
                    "Bailing out! 429 errors tend to be unrecoverable even with retry. Try running the script again later."
                ) from exc
            raise


class ArxivPrefill(PrefillScript[str]):
    description = "Prefill arXiv metadata files."
    default_input = DEFAULT_INPUT
    entry_kind = "arXiv IDs"
    delay = BASE_DELAY
    fetch_error_label = "fetching"

    def extract_entries(self, path: Path) -> list[str]:
        return extract_ids(path)

    def existing_for_entry(self, entry: str, _context: dict) -> Path | None:
        return find_existing_by_arxiv_id(entry)

    def needs_fetch_for_list_skipped(self, _entry: str, _context: dict) -> bool:
        return False

    def fetch_fields(self, entry: str, _context: dict) -> dict:
        return fetch_with_retry(entry)

    def build_metadata(self, _entry: str, fields: dict) -> dict:
        return build_metadata(fields)

    def write_metadata(self, entry: str, fields: dict, yaml_text: str) -> Path:
        return write_metadata(entry, fields["year"], yaml_text)

    def success_message(self, prefix: str, entry: str, fields: dict, _out: Path) -> str:
        return f"{prefix}  OK -> {target_path(entry, fields['year'])}"


def main() -> None:
    ArxivPrefill().run()


if __name__ == "__main__":
    main()
