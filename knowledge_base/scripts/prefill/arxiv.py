"""Batch-prefill metadata.yml files from a list of arXiv URLs/IDs.

Usage:
    python knowledge_base/scripts/prefill/arxiv.py [--input PATH] [--overwrite]

Defaults:
    --input  todo/papers/ARXIV.md
    --overwrite  False (skip IDs whose metadata.yml already exists)
"""

import re
import random
import time
from email.utils import parsedate_to_datetime
from pathlib import Path

if __package__ in (None, ""):
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))

import requests

from knowledge_base.utils.arxiv_utils import (
    build_metadata,
    fetch_arxiv,
    normalize_arxiv_id,
    target_path,
    write_metadata,
)
from knowledge_base.utils.prefill_template import HaltPrefill, PrefillScript, REPO_ROOT
from knowledge_base.utils.doi_utils import find_existing_by_arxiv_id

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "ARXIV.md"
ARXIV_URL_RE = re.compile(
    r"https?://(?:www\.)?(?:arxiv\.org|ar5iv\.labs\.arxiv\.org)/"
    r"(?:abs|pdf|html)/([^\s?#\])>]+)",
    flags=re.IGNORECASE,
)

# Duration in seconds between successful requests.
# arXiv asks clients to make no more than one request every 3 seconds and
# use a single connection; keep this comfortably above that floor.
# https://info.arxiv.org/help/api/tou.html
BASE_DELAY = 5.0
MAX_RETRIES = 3
BACKOFF_BASE = 10.0
BACKOFF_MAX = 30.0
RETRY_STATUS_CODES = {429, 500, 502, 503, 504}


def extract_ids(path: Path) -> list[str]:
    seen: set[str] = set()
    ids: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = ARXIV_URL_RE.search(line)
        arxiv_id = m.group(1) if m else line
        arxiv_id = normalize_arxiv_id(arxiv_id)
        if arxiv_id and arxiv_id not in seen:
            seen.add(arxiv_id)
            ids.append(arxiv_id)
    return ids


def retry_after_seconds(response: requests.Response | None) -> float | None:
    """Return Retry-After as seconds, if the response supplies a usable value."""
    if response is None:
        return None
    raw = response.headers.get("Retry-After")
    if not raw:
        return None
    try:
        return max(float(raw), 0.0)
    except ValueError:
        try:
            retry_at = parsedate_to_datetime(raw)
        except (TypeError, ValueError):
            return None
        return max(retry_at.timestamp() - time.time(), 0.0)


def wait_for_retry(attempt: int, response: requests.Response | None) -> None:
    retry_after = retry_after_seconds(response)
    fallback = min(BACKOFF_BASE * (2 ** attempt), BACKOFF_MAX)
    wait = retry_after if retry_after is not None else fallback
    wait += random.uniform(0.0, min(BASE_DELAY, wait * 0.1))
    status = response.status_code if response is not None else "network"
    print(f"    {status} from arXiv - waiting {wait:.0f}s before retry {attempt + 2}/{MAX_RETRIES}")
    time.sleep(wait)


def fetch_with_retry(arxiv_id: str) -> dict:
    last_exc: Exception | None = None
    for attempt in range(MAX_RETRIES):
        try:
            return fetch_arxiv(arxiv_id)
        except requests.HTTPError as exc:
            response = exc.response
            if response is None or response.status_code not in RETRY_STATUS_CODES:
                raise
            last_exc = exc
            if attempt + 1 < MAX_RETRIES:
                wait_for_retry(attempt, response)
        except (requests.ConnectionError, requests.Timeout) as exc:
            last_exc = exc
            if attempt + 1 < MAX_RETRIES:
                wait_for_retry(attempt, None)

    raise HaltPrefill(
        "arXiv is still rate-limiting or unavailable after several polite retries. "
        "The run stopped so it can be resumed later without hammering the API."
    ) from last_exc


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
