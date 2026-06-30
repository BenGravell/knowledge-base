"""arXiv fetch retry, throttling, and batch cache helpers."""

from __future__ import annotations

import random
import re
import time
from email.utils import parsedate_to_datetime
from pathlib import Path

import requests

from knowledge_base.utils.arxiv_utils import fetch_arxiv, fetch_arxiv_many, fetch_arxiv_oai, normalize_arxiv_id
from knowledge_base.utils.doi_utils import find_existing_by_arxiv_id
from knowledge_base.utils.prefill_template import REPO_ROOT, FieldMap, HaltPrefill
from knowledge_base.utils.prefill_utils import read_url_lines

# Duration in seconds between arXiv API requests.
# arXiv asks clients to make no more than one request every 3 seconds and
# use a single connection; keep this comfortably above that floor.
# https://info.arxiv.org/help/api/tou.html
BASE_DELAY = 3.25
MAX_RETRIES = 6
BACKOFF_BASE = 60.0
BACKOFF_MAX = 15 * 60.0
BATCH_SIZE = 20
OAI_BATCH_SIZE = 1
THROTTLE_STATE = REPO_ROOT / ".cache" / "prefill" / "arxiv_last_request.txt"
EXPORT_BLOCK_STATE = REPO_ROOT / ".cache" / "prefill" / "arxiv_export_blocked_until.txt"
EXPORT_BLOCK_COOLDOWN = 2 * 60 * 60
RETRY_STATUS_CODES = {429, 500, 502, 503, 504}
_PACING_NOTICE_SHOWN: set[str] = set()
ARXIV_URL_RE = re.compile(
    r"https?://(?:www\.)?(?:arxiv\.org|ar5iv\.labs\.arxiv\.org)/" r"(?:abs|pdf|html)/([^\s?#\])>]+)",
    flags=re.IGNORECASE,
)


class ArxivExportRateLimited(Exception):
    """Signal that the legacy export API is rate-limiting this client path."""


def extract_ids(path: Path) -> list[str]:
    seen: set[str] = set()
    ids: list[str] = []
    for line in read_url_lines(path):
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
    fallback = min(BACKOFF_BASE * (2**attempt), BACKOFF_MAX)
    wait = retry_after if retry_after is not None else fallback
    wait += random.uniform(0.0, min(BASE_DELAY, wait * 0.1))
    status = response.status_code if response is not None else "network"
    print(f"    {status} from arXiv - waiting {wait:.0f}s before retry {attempt + 2}/{MAX_RETRIES}")
    time.sleep(wait)


def read_timestamp(path: Path) -> float:
    try:
        return float(path.read_text(encoding="utf-8").strip())
    except (OSError, ValueError):
        return 0.0


def write_timestamp(path: Path, value: float) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"{value:.6f}\n", encoding="utf-8")


def export_blocked_for_seconds() -> float:
    return max(0.0, read_timestamp(EXPORT_BLOCK_STATE) - time.time())


def remember_export_block() -> None:
    write_timestamp(EXPORT_BLOCK_STATE, time.time() + EXPORT_BLOCK_COOLDOWN)


def wait_for_request_slot(label: str = "arXiv") -> None:
    """Persist a small delay between arXiv API requests, including across reruns."""
    last_request = read_timestamp(THROTTLE_STATE)
    wait = max(0.0, last_request + BASE_DELAY - time.time())
    if wait > 0.1:
        if label == "OAI-PMH":
            if label not in _PACING_NOTICE_SHOWN:
                print(f"    OAI-PMH pacing: waiting up to {BASE_DELAY:.2f}s between records")
                _PACING_NOTICE_SHOWN.add(label)
        else:
            print(f"    {label} throttle - waiting {wait:.0f}s before next request")
        time.sleep(wait)

    write_timestamp(THROTTLE_STATE, time.time())


def fetch_many_with_retry(arxiv_ids: list[str]) -> dict[str, FieldMap]:
    last_exc: Exception | None = None
    for attempt in range(MAX_RETRIES):
        wait_for_request_slot("export.arxiv.org")
        try:
            return fetch_arxiv_many(arxiv_ids)
        except requests.HTTPError as exc:
            response = exc.response
            if response is None or response.status_code not in RETRY_STATUS_CODES:
                raise
            if response.status_code == 429:
                remember_export_block()
                raise ArxivExportRateLimited from exc
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


def fetch_oai_with_retry(arxiv_id: str) -> FieldMap:
    last_exc: Exception | None = None
    for attempt in range(MAX_RETRIES):
        wait_for_request_slot("OAI-PMH")
        try:
            return fetch_arxiv_oai(arxiv_id)
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
        "arXiv OAI-PMH is still rate-limiting or unavailable after several polite retries. "
        "The run stopped so it can be resumed later without hammering the API."
    ) from last_exc


def fetch_many_via_oai(arxiv_ids: list[str]) -> dict[str, FieldMap]:
    records: dict[str, FieldMap] = {}
    for arxiv_id in arxiv_ids:
        try:
            fields = fetch_oai_with_retry(arxiv_id)
        except ValueError as exc:
            print(f"    OAI-PMH missing {arxiv_id}: {exc}")
            continue
        records[normalize_arxiv_id(fields.get("arxiv_id"))] = fields
    return records


def fetch_with_retry(arxiv_id: str) -> FieldMap:
    last_exc: Exception | None = None
    for attempt in range(MAX_RETRIES):
        wait_for_request_slot("export.arxiv.org")
        try:
            return fetch_arxiv(arxiv_id)
        except requests.HTTPError as exc:
            response = exc.response
            if response is None or response.status_code not in RETRY_STATUS_CODES:
                raise
            if response.status_code == 429:
                remember_export_block()
                print("    export.arxiv.org returned 429; switching this request to OAI-PMH")
                return fetch_oai_with_retry(arxiv_id)
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


class ArxivBatchCache:
    """Fetch nearby todo rows together and serve later entries from memory."""

    def __init__(self, entries: list[str], batch_size: int = BATCH_SIZE) -> None:
        self.entries = [normalize_arxiv_id(entry) for entry in entries]
        self.index = {entry: i for i, entry in enumerate(self.entries)}
        self.batch_size = batch_size
        self.cache: dict[str, FieldMap] = {}
        self.missing: set[str] = set()
        self.use_oai = export_blocked_for_seconds() > 0.0
        self.printed_oai_cooldown = False

    def fetch(self, entry: str) -> FieldMap:
        arxiv_id = normalize_arxiv_id(entry)
        if arxiv_id in self.cache:
            return self.cache[arxiv_id]
        if arxiv_id in self.missing:
            raise ValueError(f"No entry found for arXiv ID '{arxiv_id}'")

        batch = self.next_batch(arxiv_id)
        records, attempted = self.fetch_batch(batch)
        self.cache.update(records)
        self.missing.update(arxiv_id for arxiv_id in attempted if arxiv_id not in records)

        if arxiv_id not in self.cache:
            raise ValueError(f"No entry found for arXiv ID '{arxiv_id}'")
        return self.cache[arxiv_id]

    def next_batch(self, arxiv_id: str) -> list[str]:
        start = self.index.get(arxiv_id, 0)
        batch: list[str] = []
        for candidate in self.entries[start:]:
            if len(batch) >= self.batch_size:
                break
            if candidate in self.cache or candidate in self.missing:
                continue
            if candidate != arxiv_id and find_existing_by_arxiv_id(candidate):
                continue
            batch.append(candidate)
        return batch or [arxiv_id]

    def fetch_batch(self, batch: list[str]) -> tuple[dict[str, FieldMap], list[str]]:
        if self.use_oai:
            if not self.printed_oai_cooldown:
                blocked_for = export_blocked_for_seconds()
                if blocked_for > 0.0:
                    print(f"    export.arxiv.org is in local cooldown ({blocked_for / 3600:.1f}h left); using OAI-PMH")
                self.printed_oai_cooldown = True
            attempted = batch[:OAI_BATCH_SIZE]
            return fetch_many_via_oai(attempted), attempted
        try:
            return fetch_many_with_retry(batch), batch
        except ArxivExportRateLimited:
            self.use_oai = True
            print("    export.arxiv.org returned 429 on a cold request; switching to OAI-PMH for this run")
            attempted = batch[:OAI_BATCH_SIZE]
            return fetch_many_via_oai(attempted), attempted
