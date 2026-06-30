"""Semantic Scholar prefill handler."""

from __future__ import annotations

import os
import random
import time
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import quote

import requests

from knowledge_base.prefill.runner import FieldMap, HaltPrefill, ParseFailure
from knowledge_base.prefill.todo_file import build_page_metadata, read_url_lines

_FIELDS = ",".join(
    [
        "title",
        "authors",
        "year",
        "abstract",
        "venue",
        "publicationTypes",
        "externalIds",
        "url",
        "openAccessPdf",
    ]
)
_BY_ID = "https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields={fields}"
_RETRY_STATUS_CODES = {429, 500, 502, 503, 504}
_HEADERS = {"User-Agent": "knowledge-base-prefill/1.0"}


def _env_int(name: str, default: int) -> int:
    try:
        return max(1, int(os.environ.get(name, str(default))))
    except ValueError:
        return default


def _env_float(name: str, default: float) -> float:
    try:
        return max(0.0, float(os.environ.get(name, str(default))))
    except ValueError:
        return default


_MAX_RETRIES = _env_int("SEMANTIC_SCHOLAR_MAX_RETRIES", 5)
_BACKOFF_BASE = _env_float("SEMANTIC_SCHOLAR_BACKOFF_BASE", 10.0)
_BACKOFF_MAX = _env_float("SEMANTIC_SCHOLAR_BACKOFF_MAX", 90.0)


def _headers() -> dict[str, str]:
    headers = dict(_HEADERS)
    for env_name in ("SEMANTIC_SCHOLAR_API_KEY", "S2_API_KEY"):
        api_key = os.environ.get(env_name, "").strip()
        if api_key:
            headers["x-api-key"] = api_key
            break
    return headers


def _retry_after_seconds(response: requests.Response | None) -> float | None:
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


def _wait_for_retry(attempt: int, response: requests.Response | None) -> None:
    retry_after = _retry_after_seconds(response)
    fallback = min(_BACKOFF_BASE * (2**attempt), _BACKOFF_MAX)
    wait = retry_after if retry_after is not None else fallback
    wait += random.uniform(0.0, min(5.0, wait * 0.1))
    status = response.status_code if response is not None else "network"
    print(f"    {status} from Semantic Scholar - waiting {wait:.0f}s before retry {attempt + 2}/{_MAX_RETRIES}")
    time.sleep(wait)


def _rate_limit_message() -> str:
    hint = "Set SEMANTIC_SCHOLAR_API_KEY or S2_API_KEY to use an individual Semantic Scholar API key."
    return (
        "Semantic Scholar is still rate-limiting this run after several polite "
        f"retries. {hint} The run stopped so it can be resumed later without "
        "marking the remaining papers as failed."
    )


def _get_json(url: str) -> FieldMap:
    headers = _headers()
    last_exc: Exception | None = None
    for attempt in range(_MAX_RETRIES):
        try:
            response = requests.get(url, headers=headers, timeout=60)
        except (requests.ConnectionError, requests.Timeout) as exc:
            last_exc = exc
            if attempt + 1 < _MAX_RETRIES:
                _wait_for_retry(attempt, None)
                continue
            raise HaltPrefill(
                "Semantic Scholar did not respond after several retries. The run stopped so it can be resumed later."
            ) from exc

        if response.status_code in _RETRY_STATUS_CODES:
            last_exc = requests.HTTPError(response=response)
            if attempt + 1 < _MAX_RETRIES:
                _wait_for_retry(attempt, response)
                continue
            if response.status_code == 429:
                raise HaltPrefill(_rate_limit_message()) from last_exc

        response.raise_for_status()
        return response.json()

    raise HaltPrefill(_rate_limit_message()) from last_exc


def paper_type(publication_types: list[str] | None) -> str:
    values = {str(t).lower() for t in publication_types or []}
    if any("review" in t for t in values):
        return "Survey Paper"
    if any("conference" in t for t in values):
        return "Conference Paper"
    if any("journal" in t for t in values):
        return "Journal Paper"
    return "Other"


def fields(identifier: str, fallback_url: str = "") -> FieldMap:
    """Return normalized metadata for a Semantic Scholar paper id or URL lookup."""
    if identifier.startswith("URL:"):
        paper_id = "URL:" + quote(identifier.removeprefix("URL:"), safe="")
    else:
        paper_id = quote(identifier, safe="")
    url = _BY_ID.format(paper_id=paper_id, fields=_FIELDS)
    data = _get_json(url)

    title = str(data.get("title") or "").strip()
    authors = [
        str(author.get("name") or "").strip()
        for author in data.get("authors") or []
        if str(author.get("name") or "").strip()
    ]
    year = int(data.get("year") or 0)
    external = data.get("externalIds") or {}
    open_pdf = data.get("openAccessPdf") or {}
    link = open_pdf.get("url") or data.get("url") or fallback_url
    alt = [x for x in [fallback_url, data.get("url")] if x and x != link]

    if not title or not authors or not year:
        raise ValueError(f"Incomplete Semantic Scholar metadata for {identifier!r}")

    return {
        "title": title,
        "authors": authors,
        "year": year,
        "source": data.get("venue") or "Semantic Scholar",
        "type": paper_type(data.get("publicationTypes")),
        "doi": external.get("DOI") or None,
        "arxiv_id": external.get("ArXiv") or None,
        "abstract": data.get("abstract") or "",
        "link": link,
        "links_alt": list(dict.fromkeys(alt)),
    }


def identifier_for_url(url: str) -> str:
    if "semanticscholar.org/paper/" in url:
        return url.rstrip("/").split("/")[-1]
    return f"URL:{url}"


def extract_entries(path: Path, record_parse_failure: ParseFailure) -> list[str]:
    seen: set[str] = set()
    entries: list[str] = []
    for url in read_url_lines(path):
        identifier = identifier_for_url(url)
        if not identifier:
            record_parse_failure(f"could not parse Semantic Scholar identifier from: {url!r}")
            continue
        if identifier not in seen:
            seen.add(identifier)
            entries.append(identifier)
    return entries


def source_key_for_token(token: str) -> str | None:
    return identifier_for_url(token)


def entry_label(entry: str) -> str:
    return entry.removeprefix("URL:")


def build_metadata(entry: str, fields: FieldMap) -> FieldMap:
    _ = entry
    metadata = build_page_metadata(fields)
    if fields.get("arxiv_id"):
        metadata["arxiv_id"] = fields["arxiv_id"]
    return metadata
