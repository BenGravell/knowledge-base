"""Batch-prefill metadata.yml files from OpenReview URLs."""

import random
import re
import time
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import parse_qs, urlparse

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

import requests

from knowledge_base.utils.prefill_template import HaltPrefill, PagePrefillScript, REPO_ROOT
from knowledge_base.utils.prefill_utils import first_year, read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "OPENREVIEW.md"

_OPENREVIEW_APIS = (
    ("OpenReview API2", "https://api2.openreview.net/notes?id={note_id}"),
    ("OpenReview legacy API", "https://api.openreview.net/notes?id={note_id}"),
)
_OPENREVIEW_BASE = "https://openreview.net"
_OPENREVIEW_HEADERS = {
    "User-Agent": "knowledge-base-prefill/1.0",
    "Accept": "application/json",
}

MAX_RETRIES = 4
BACKOFF_BASE = 10.0
BACKOFF_MAX = 90.0
RETRY_STATUS_CODES = {429, 500, 502, 503, 504}
LEGACY_FALLBACK_STATUS_CODES = {404}


def content_value(content: dict, key: str, default=None):
    value = content.get(key, default)
    if isinstance(value, dict) and "value" in value:
        return value["value"]
    return value


def extract_note_id(url: str) -> str:
    parsed = urlparse(url)
    values = parse_qs(parsed.query).get("id")
    if values:
        return values[0]
    parts = [part for part in parsed.path.split("/") if part]
    return parts[-1] if parts else ""


def extract_entries(path: Path, on_parse_failure=None) -> list[str]:
    seen: set[str] = set()
    entries: list[str] = []
    for url in read_url_lines(path):
        note_id = extract_note_id(url)
        if not note_id:
            message = f"could not parse OpenReview note id from: {url!r}"
            if on_parse_failure:
                on_parse_failure(message)
            else:
                print(f"  WARN: {message}")
            continue
        if note_id not in seen:
            seen.add(note_id)
            entries.append(note_id)
    return entries


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


def wait_for_retry(label: str, attempt: int, response: requests.Response | None) -> None:
    retry_after = retry_after_seconds(response)
    fallback = min(BACKOFF_BASE * (2**attempt), BACKOFF_MAX)
    wait = retry_after if retry_after is not None else fallback
    wait += random.uniform(0.0, min(3.0, wait * 0.1))
    status = response.status_code if response is not None else "network"
    print(
        f"    {status} from {label} - "
        f"waiting {wait:.0f}s before retry {attempt + 2}/{MAX_RETRIES}"
    )
    time.sleep(wait)


def fetch_openreview_json(label: str, url: str) -> dict:
    last_exc: Exception | None = None
    for attempt in range(MAX_RETRIES):
        try:
            r = requests.get(url, headers=_OPENREVIEW_HEADERS, timeout=60)
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as exc:
            response = exc.response
            if response is None or response.status_code not in RETRY_STATUS_CODES:
                raise
            last_exc = exc
            if attempt + 1 < MAX_RETRIES:
                wait_for_retry(label, attempt, response)
        except (requests.ConnectionError, requests.Timeout) as exc:
            last_exc = exc
            if attempt + 1 < MAX_RETRIES:
                wait_for_retry(label, attempt, None)

    raise HaltPrefill(
        f"{label} is still rate-limiting or unavailable after several polite retries. "
        "The run stopped so it can be resumed later without hammering OpenReview."
    ) from last_exc


def fetch_openreview_notes(note_id: str) -> list[dict]:
    for index, (label, api) in enumerate(_OPENREVIEW_APIS):
        try:
            data = fetch_openreview_json(label, api.format(note_id=note_id))
        except requests.HTTPError as exc:
            response = exc.response
            can_fallback = (
                index + 1 < len(_OPENREVIEW_APIS)
                and response is not None
                and response.status_code in LEGACY_FALLBACK_STATUS_CODES
            )
            if can_fallback:
                print(f"    {label} had no note for {note_id}; trying legacy API")
                continue
            raise

        notes = data.get("notes") or []
        if notes:
            return notes
        if index + 1 < len(_OPENREVIEW_APIS):
            print(f"    {label} returned no notes for {note_id}; trying legacy API")

    return []


def timestamp_year(value) -> str:
    if value in (None, ""):
        return ""
    text = str(value).strip()
    if re.fullmatch(r"(18|19|20)\d{2}", text):
        return text
    if re.fullmatch(r"(18|19|20)\d{6}", text):
        return text[:4]
    try:
        timestamp = float(text)
    except (TypeError, ValueError):
        return text
    if timestamp > 10_000_000_000:
        timestamp /= 1000.0
    try:
        return str(datetime.fromtimestamp(timestamp, tz=UTC).year)
    except (OSError, OverflowError, ValueError):
        return text


def source_from_bibtex(bibtex: str, venue: str) -> str:
    for key in ("journal", "booktitle"):
        match = re.search(rf"\b{key}\s*=\s*[{{\"]([^}}\"]+)", bibtex, flags=re.I)
        if match:
            return match.group(1).strip()
    if "TMLR" in venue:
        return "Transactions on Machine Learning Research"
    return venue or "OpenReview"


def type_from_source(source: str, venue: str) -> str:
    text = f"{source} {venue}".lower()
    if "transactions on machine learning research" in text or "journal" in text:
        return "Journal Paper"
    if any(name in text for name in ("iclr", "neurips", "nips", "conference")):
        return "Conference Paper"
    return "Other"


def fetch_openreview_fields(note_id: str) -> dict:
    notes = fetch_openreview_notes(note_id)
    if not notes:
        raise ValueError(f"No OpenReview note found for {note_id!r}")

    note = notes[0]
    content = note.get("content") or {}
    title = str(content_value(content, "title", "") or "").strip()
    authors = list(content_value(content, "authors", []) or [])
    abstract = str(content_value(content, "abstract", "") or "").strip()
    venue = str(content_value(content, "venue", "") or "").strip()
    bibtex = str(content_value(content, "_bibtex", "") or "").strip()
    year = first_year(
        bibtex,
        timestamp_year(note.get("pdate")),
        timestamp_year(note.get("cdate")),
    )

    pdf = str(content_value(content, "pdf", "") or "")
    link = _OPENREVIEW_BASE + pdf if pdf.startswith("/") else pdf
    forum = f"{_OPENREVIEW_BASE}/forum?id={note.get('forum') or note_id}"
    supplement = str(content_value(content, "supplementary_material", "") or "")
    if supplement.startswith("/"):
        supplement = _OPENREVIEW_BASE + supplement

    source = source_from_bibtex(bibtex, venue)

    if not title or not authors or not year:
        raise ValueError(f"Incomplete OpenReview metadata for {note_id!r}")

    return {
        "title": title,
        "authors": authors,
        "year": year,
        "source": source,
        "type": type_from_source(source, venue),
        "abstract": abstract,
        "link": link or forum,
        "links_alt": [x for x in [forum, supplement] if x],
    }


class OpenReviewPrefill(PagePrefillScript[str]):
    description = "Prefill metadata from OpenReview URLs."
    default_input = DEFAULT_INPUT
    entry_kind = "OpenReview notes"

    def extract_entries(self, path: Path) -> list[str]:
        return extract_entries(path, self.record_parse_failure)

    def source_key_for_entry(self, entry: str) -> str | None:
        return self.normalize_source_key(entry)

    def source_key_for_token(self, token: str) -> str | None:
        note_id = extract_note_id(token)
        return self.normalize_source_key(note_id) if note_id else None

    def fetch_fields(self, entry: str, _context: dict) -> dict:
        return fetch_openreview_fields(entry)


def main() -> None:
    OpenReviewPrefill().run()


if __name__ == "__main__":
    main()
