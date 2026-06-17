"""Template Method machinery for paper metadata prefill scripts."""

from __future__ import annotations

import os
import random
import subprocess
import tempfile
import time
from abc import ABC, abstractmethod
from collections.abc import Callable
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any, Generic, TypeVar
from urllib.parse import quote

import requests
from typing_extensions import override

from knowledge_base.config import REPO_ROOT  # noqa: F401 - re-exported for source-specific prefill scripts
from knowledge_base.utils.arxiv_utils import metadata_to_yaml
from knowledge_base.utils.doi_utils import (
    BASE_DELAY,
    build_doi_index,
    build_doi_metadata,
    doi_target_path,
    fetch_crossref,
    fetch_page_html,
    fetch_with_retry,
    generate_folder_name,
    make_parser,
    scrape_abstract_from_html,
    scrape_doi_from_html,
    should_skip,
    write_doi_metadata,
)
from knowledge_base.utils.prefill_utils import (
    build_page_metadata,
    citation_doi,
    extract_doi_from_url,
    fetch_citation_page_fields,
    read_url_lines,
    source_row_token,
    write_text_atomic,
)

EntryT = TypeVar("EntryT")
FieldMap = dict[str, Any]


class HaltPrefill(Exception):
    """Signal that a prefill run should stop without treating it as a failure."""


class SourceFileCleanup:
    """Remove handled input rows by re-reading and atomically replacing the file."""

    def __init__(self, path: Path, key_for_token: Callable[[str], str | None]) -> None:
        self.path = path
        self.key_for_token = key_for_token

    def remove(self, handled_key: str) -> int:
        raw_lines = self.path.read_text(encoding="utf-8").splitlines(keepends=True)
        removed = 0
        kept_lines: list[str] = []

        for line in raw_lines:
            token = source_row_token(line)
            row_key = self.key_for_token(token) if token else None
            if row_key and row_key == handled_key:
                removed += 1
                continue
            kept_lines.append(line)

        if removed:
            write_text_atomic(self.path, "".join(kept_lines))
        return removed


class PrefillScript(ABC, Generic[EntryT]):
    """Base Template Method for all metadata prefill scripts.

    Subclasses provide the primitive operations: read input entries, fetch
    fields, build metadata, and write the final YAML. The invariant CLI,
    skip/list/error/retry counters, and pacing live here.
    """

    description: str
    default_input: Path
    entry_kind: str = "entries"
    delay: float = BASE_DELAY
    fetch_error_label: str = "fetching metadata"

    def __init__(self) -> None:
        self.parse_failures: list[str] = []

    def run(self) -> None:
        args = make_parser(self.description, self.default_input).parse_args()
        self.parse_failures = []
        entries = self.extract_entries(args.input)
        print(f"Found {len(entries)} unique {self.entry_kind} in {args.input}")

        context = self.prepare_context(args)
        if args.list_skipped:
            self.list_skipped(entries, context)
            return

        ok = skipped = failed = 0
        source_removed = 0
        parse_failed = len(self.parse_failures)
        source_cleanup = SourceFileCleanup(args.input, self.source_key_for_token)

        for i, entry in enumerate(entries, 1):
            prefix = f"[{i}/{len(entries)}] {self.entry_label(entry)}"

            existing = self.existing_for_entry(entry, context)
            if should_skip(existing, args):
                print(f"{prefix}  SKIP (exists: {existing})")
                source_removed += self.remove_handled_source_rows(source_cleanup, entry, prefix)
                skipped += 1
                continue

            try:
                fields = self.fetch_fields(entry, context)
            except HaltPrefill as exc:
                print(prefix)
                print(exc)
                break
            except Exception as exc:
                print(f"{prefix}  ERROR {self.fetch_error_label}: {exc}")
                failed += 1
                time.sleep(self.delay)
                if args.first is not None and ok + failed >= args.first:
                    break
                continue

            existing = existing or self.existing_for_fields(fields, context)
            if should_skip(existing, args):
                print(f"{prefix}  SKIP (exists: {existing})")
                source_removed += self.remove_handled_source_rows(source_cleanup, entry, prefix)
                skipped += 1
                time.sleep(self.delay)
                continue

            metadata = self.build_metadata(entry, fields)
            yaml_text = metadata_to_yaml(metadata)
            out = self.write_metadata(entry, fields, yaml_text)
            print(self.success_message(prefix, entry, fields, out))
            source_removed += self.remove_handled_source_rows(source_cleanup, entry, prefix)
            ok += 1

            if args.first is not None and ok + failed >= args.first:
                break
            time.sleep(self.delay)

        failed += parse_failed
        if parse_failed:
            print(
                f"\nDone: {ok} written, {skipped} skipped, {failed} failed "
                f"({parse_failed} parse), {source_removed} source row(s) removed"
            )
        else:
            print(f"\nDone: {ok} written, {skipped} skipped, {failed} failed, {source_removed} source row(s) removed")

    def record_parse_failure(self, message: str) -> None:
        self.parse_failures.append(message)
        print(f"  WARN: {message}")

    def list_skipped(self, entries: list[EntryT], context: dict[str, Any]) -> None:
        for entry in entries:
            existing = self.existing_for_entry(entry, context)
            if existing:
                print(self.skipped_list_message(entry, None, existing))
                continue
            if not self.needs_fetch_for_list_skipped(entry, context):
                continue
            try:
                fields = self.fetch_fields(entry, context)
            except HaltPrefill as exc:
                print(self.entry_label(entry))
                print(exc)
                break
            except Exception as exc:
                print(f"{self.entry_label(entry)}  ERROR {self.fetch_error_label}: {exc}")
                time.sleep(self.delay)
                continue
            existing = self.existing_for_fields(fields, context)
            if existing:
                print(self.skipped_list_message(entry, fields, existing))
            time.sleep(self.delay)

    def prepare_context(self, args: Any) -> dict[str, Any]:
        _ = args
        return {}

    def normalize_source_key(self, value: str) -> str:
        return str(value).strip().lower()

    def source_key_for_entry(self, entry: EntryT) -> str | None:
        label = self.entry_label(entry)
        return self.normalize_source_key(label) if label else None

    def source_key_for_token(self, token: str) -> str | None:
        return self.normalize_source_key(token) if token else None

    def remove_handled_source_rows(
        self,
        source_cleanup: SourceFileCleanup,
        entry: EntryT,
        prefix: str,
    ) -> int:
        key = self.source_key_for_entry(entry)
        if not key:
            return 0
        try:
            removed = source_cleanup.remove(key)
        except Exception as exc:
            raise RuntimeError(
                f"Metadata for {self.entry_label(entry)!r} was handled, but "
                f"{source_cleanup.path} could not be updated safely."
            ) from exc
        if removed:
            print(f"{prefix}  SOURCE -{removed} row(s)")
        return removed

    @abstractmethod
    def extract_entries(self, path: Path) -> list[EntryT]:
        """Parse and deduplicate entries from the input file."""

    def entry_label(self, entry: EntryT) -> str:
        return str(entry)

    def existing_for_entry(self, entry: EntryT, context: dict[str, Any]) -> Path | None:
        _ = entry, context
        return None

    def needs_fetch_for_list_skipped(self, entry: EntryT, context: dict[str, Any]) -> bool:
        _ = entry, context
        return True

    @abstractmethod
    def fetch_fields(self, entry: EntryT, context: dict[str, Any]) -> FieldMap:
        """Return normalized metadata fields for *entry*."""

    def existing_for_fields(self, fields: FieldMap, context: dict[str, Any]) -> Path | None:
        _ = fields, context
        return None

    @abstractmethod
    def build_metadata(self, entry: EntryT, fields: FieldMap) -> FieldMap:
        """Build an ordered metadata dict ready for YAML serialization."""

    @abstractmethod
    def write_metadata(self, entry: EntryT, fields: FieldMap, yaml_text: str) -> Path:
        """Write *yaml_text* and return the target path."""

    def success_message(self, prefix: str, entry: EntryT, fields: FieldMap, out: Path) -> str:
        _ = entry, fields
        return f"{prefix}  OK -> {out}"

    def skipped_list_message(
        self,
        entry: EntryT,
        fields: FieldMap | None,
        existing: Path,
    ) -> str:
        _ = fields
        return f"{self.entry_label(entry)}  {existing}"


class DoiPrefillScript(PrefillScript[EntryT], ABC):
    """Template Method specialization for DOI/Crossref-backed sources."""

    entry_kind = "DOIs"
    show_resolved_doi = False

    @override
    def prepare_context(self, args: Any) -> dict[str, Any]:
        _ = args
        return {"doi_index": build_doi_index()}

    def entry_doi(self, entry: EntryT) -> str | None:
        """Return a DOI known from the input entry, if available before fetching."""
        _ = entry
        return None

    def resolve_doi(self, entry: EntryT) -> str:
        doi = self.entry_doi(entry)
        if doi:
            return doi
        raise NotImplementedError("Subclasses must implement resolve_doi() or entry_doi().")

    @override
    def existing_for_entry(self, entry: EntryT, context: dict[str, Any]) -> Path | None:
        doi = self.entry_doi(entry)
        return context["doi_index"].get(doi.lower()) if doi else None

    @override
    def needs_fetch_for_list_skipped(self, entry: EntryT, context: dict[str, Any]) -> bool:
        _ = context
        return self.entry_doi(entry) is None

    @override
    def fetch_fields(self, entry: EntryT, context: dict[str, Any]) -> FieldMap:
        _ = context
        doi = self.resolve_doi(entry)
        data = fetch_with_retry(fetch_crossref, doi)
        return self.postprocess_crossref_data(entry, data)

    def postprocess_crossref_data(self, entry: EntryT, data: FieldMap) -> FieldMap:
        _ = entry
        return data

    @override
    def existing_for_fields(self, fields: FieldMap, context: dict[str, Any]) -> Path | None:
        doi = str(fields.get("doi") or "").strip()
        return context["doi_index"].get(doi.lower()) if doi else None

    @override
    def source_key_for_entry(self, entry: EntryT) -> str | None:
        if isinstance(entry, tuple) and len(entry) >= 2:
            return self.normalize_source_key(str(entry[1]))
        doi = self.entry_doi(entry)
        if doi:
            return self.normalize_source_key(doi)
        return super().source_key_for_entry(entry)

    @override
    def source_key_for_token(self, token: str) -> str | None:
        doi = extract_doi_from_url(token)
        if doi:
            return self.normalize_source_key(doi)
        return super().source_key_for_token(token)

    @override
    def build_metadata(self, entry: EntryT, fields: FieldMap) -> FieldMap:
        return self.postprocess_metadata(entry, fields, build_doi_metadata(fields))

    def postprocess_metadata(self, entry: EntryT, fields: FieldMap, metadata: FieldMap) -> FieldMap:
        _ = entry, fields
        return metadata

    @override
    def write_metadata(self, entry: EntryT, fields: FieldMap, yaml_text: str) -> Path:
        _ = entry
        folder = generate_folder_name(fields["year"], fields["authors"], fields["title"])
        return write_doi_metadata(fields["year"], folder, yaml_text)

    def output_path(self, fields: FieldMap) -> Path:
        folder = generate_folder_name(fields["year"], fields["authors"], fields["title"])
        return doi_target_path(fields["year"], folder)

    @override
    def success_message(self, prefix: str, entry: EntryT, fields: FieldMap, out: Path) -> str:
        if self.show_resolved_doi or self.entry_doi(entry) is None:
            return f"{prefix}  OK doi={fields['doi']} -> {out}"
        return super().success_message(prefix, entry, fields, out)

    @override
    def skipped_list_message(
        self,
        entry: EntryT,
        fields: FieldMap | None,
        existing: Path,
    ) -> str:
        doi = str(fields.get("doi") or "") if fields else self.entry_doi(entry)
        return f"{self.entry_label(entry)} ({doi})  {existing}" if fields else f"{doi}  {existing}"


class PagePrefillScript(PrefillScript[EntryT], ABC):
    """Template Method specialization for proceedings pages without Crossref."""

    entry_kind = "entries"

    @override
    def prepare_context(self, args: Any) -> dict[str, Any]:
        _ = args
        return {"doi_index": build_doi_index()}

    @override
    def existing_for_fields(self, fields: FieldMap, context: dict[str, Any]) -> Path | None:
        doi = str(fields.get("doi") or "").strip()
        if doi:
            existing = context["doi_index"].get(doi.lower())
            if existing:
                return existing
        out = self.output_path(fields)
        return out if out.exists() else None

    @override
    def build_metadata(self, entry: EntryT, fields: FieldMap) -> FieldMap:
        _ = entry
        return build_page_metadata(fields)

    def output_path(self, fields: FieldMap) -> Path:
        folder = generate_folder_name(fields["year"], fields["authors"], fields["title"])
        return doi_target_path(fields["year"], folder)

    @override
    def write_metadata(self, entry: EntryT, fields: FieldMap, yaml_text: str) -> Path:
        _ = entry
        folder = generate_folder_name(fields["year"], fields["authors"], fields["title"])
        return write_doi_metadata(fields["year"], folder, yaml_text)


class UrlDoiPrefillScript(DoiPrefillScript[str]):
    """Template Method specialization for source files that contain publisher URLs."""

    entry_kind = "URLs"
    source_hint = "publisher"

    @override
    def extract_entries(self, path: Path) -> list[str]:
        seen: set[str] = set()
        entries: list[str] = []
        for url in read_url_lines(path):
            if not self.accept_url(url):
                self.record_parse_failure(f"could not parse {self.source_hint} URL from: {url!r}")
                continue
            key = self.entry_key(url)
            if key not in seen:
                seen.add(key)
                entries.append(url)
        return entries

    def accept_url(self, url: str) -> bool:
        _ = url
        return True

    def entry_key(self, url: str) -> str:
        return (self.entry_doi(url) or url).lower()

    @override
    def source_key_for_entry(self, entry: str) -> str | None:
        return self.normalize_source_key(self.entry_key(entry))

    @override
    def source_key_for_token(self, token: str) -> str | None:
        if not self.accept_url(token):
            return None
        return self.normalize_source_key(self.entry_key(token))

    @override
    def entry_label(self, entry: str) -> str:
        return self.entry_doi(entry) or entry

    @override
    def entry_doi(self, entry: str) -> str | None:
        return extract_doi_from_url(entry) or None

    @override
    def resolve_doi(self, entry: str) -> str:
        doi = self.entry_doi(entry)
        if doi:
            return doi
        html = fetch_page_html(entry)
        try:
            return scrape_doi_from_html(html)
        except Exception:
            doi = citation_doi(html, entry)
            if doi:
                return str(doi)
            raise

    @override
    def postprocess_crossref_data(self, entry: str, data: FieldMap) -> FieldMap:
        data = {**data, "link": entry}
        if data["abstract"]:
            return data
        try:
            abstract = scrape_abstract_from_html(fetch_page_html(entry))
        except Exception:
            return data
        return {**data, "abstract": abstract} if abstract else data

    @override
    def postprocess_metadata(self, entry: str, fields: FieldMap, metadata: FieldMap) -> FieldMap:
        links_alt = list(metadata.get("links_alt") or [])
        doi = str(fields.get("doi") or self.entry_doi(entry) or "").strip()
        if doi:
            links_alt.append(f"https://doi.org/{doi}")
        links_alt = list(dict.fromkeys(x for x in links_alt if x and x != metadata.get("link")))
        return {**metadata, "links_alt": links_alt}


class CitationPagePrefillScript(PagePrefillScript[str]):
    """Template Method specialization for pages exposing citation meta tags."""

    entry_kind = "URLs"
    source_fallback = ""
    type_fallback = "Journal Paper"
    source_hint = "citation"

    @override
    def extract_entries(self, path: Path) -> list[str]:
        seen: set[str] = set()
        entries: list[str] = []
        for url in read_url_lines(path):
            if not self.accept_url(url):
                self.record_parse_failure(f"could not parse {self.source_hint} URL from: {url!r}")
                continue
            key = self.normalize_url(url)
            if key not in seen:
                seen.add(key)
                entries.append(key)
        return entries

    def accept_url(self, url: str) -> bool:
        _ = url
        return True

    def normalize_url(self, url: str) -> str:
        return url

    @override
    def source_key_for_entry(self, entry: str) -> str | None:
        return self.normalize_source_key(entry)

    @override
    def source_key_for_token(self, token: str) -> str | None:
        if not self.accept_url(token):
            return None
        return self.normalize_source_key(self.normalize_url(token))

    @override
    def fetch_fields(self, entry: str, context: dict[str, Any]) -> FieldMap:
        _ = context
        return fetch_citation_page_fields(
            entry,
            source_fallback=self.source_fallback,
            type_fallback=self.type_fallback,
        )


_S2_FIELDS = ",".join(
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
_S2_BY_ID = "https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields={fields}"
_S2_RETRY_STATUS_CODES = {429, 500, 502, 503, 504}
_S2_HEADERS = {"User-Agent": "knowledge-base-prefill/1.0"}


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


_S2_MAX_RETRIES = _env_int("SEMANTIC_SCHOLAR_MAX_RETRIES", 5)
_S2_BACKOFF_BASE = _env_float("SEMANTIC_SCHOLAR_BACKOFF_BASE", 10.0)
_S2_BACKOFF_MAX = _env_float("SEMANTIC_SCHOLAR_BACKOFF_MAX", 90.0)


def _semantic_scholar_headers() -> dict[str, str]:
    headers = dict(_S2_HEADERS)
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


def _wait_for_semantic_scholar_retry(
    attempt: int,
    response: requests.Response | None,
) -> None:
    retry_after = _retry_after_seconds(response)
    fallback = min(_S2_BACKOFF_BASE * (2**attempt), _S2_BACKOFF_MAX)
    wait = retry_after if retry_after is not None else fallback
    wait += random.uniform(0.0, min(5.0, wait * 0.1))
    status = response.status_code if response is not None else "network"
    print(f"    {status} from Semantic Scholar - waiting {wait:.0f}s before retry {attempt + 2}/{_S2_MAX_RETRIES}")
    time.sleep(wait)


def _semantic_scholar_rate_limit_message() -> str:
    hint = "Set SEMANTIC_SCHOLAR_API_KEY or S2_API_KEY to use an individual Semantic Scholar API key."
    return (
        "Semantic Scholar is still rate-limiting this run after several polite "
        f"retries. {hint} The run stopped so it can be resumed later without "
        "marking the remaining papers as failed."
    )


def _semantic_scholar_get_json(url: str) -> FieldMap:
    headers = _semantic_scholar_headers()
    last_exc: Exception | None = None

    for attempt in range(_S2_MAX_RETRIES):
        try:
            response = requests.get(url, headers=headers, timeout=60)
        except (requests.ConnectionError, requests.Timeout) as exc:
            last_exc = exc
            if attempt + 1 < _S2_MAX_RETRIES:
                _wait_for_semantic_scholar_retry(attempt, None)
                continue
            raise HaltPrefill(
                "Semantic Scholar did not respond after several retries. The run stopped so it can be resumed later."
            ) from exc

        if response.status_code in _S2_RETRY_STATUS_CODES:
            last_exc = requests.HTTPError(response=response)
            if attempt + 1 < _S2_MAX_RETRIES:
                _wait_for_semantic_scholar_retry(attempt, response)
                continue
            if response.status_code == 429:
                raise HaltPrefill(_semantic_scholar_rate_limit_message()) from last_exc

        response.raise_for_status()
        return response.json()

    raise HaltPrefill(_semantic_scholar_rate_limit_message()) from last_exc


def semantic_scholar_type(publication_types: list[str] | None) -> str:
    values = {str(t).lower() for t in publication_types or []}
    if any("review" in t for t in values):
        return "Survey Paper"
    if any("conference" in t for t in values):
        return "Conference Paper"
    if any("journal" in t for t in values):
        return "Journal Paper"
    return "Other"


def semantic_scholar_fields(identifier: str, fallback_url: str = "") -> FieldMap:
    """Return normalized metadata for a Semantic Scholar paper id or URL lookup."""
    if identifier.startswith("URL:"):
        paper_id = "URL:" + quote(identifier.removeprefix("URL:"), safe="")
    else:
        paper_id = quote(identifier, safe="")
    url = _S2_BY_ID.format(paper_id=paper_id, fields=_S2_FIELDS)
    data = _semantic_scholar_get_json(url)

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
        "type": semantic_scholar_type(data.get("publicationTypes")),
        "doi": external.get("DOI") or None,
        "arxiv_id": external.get("ArXiv") or None,
        "abstract": data.get("abstract") or "",
        "link": link,
        "links_alt": list(dict.fromkeys(alt)),
    }


class SemanticScholarPrefillScript(PagePrefillScript[str]):
    """Template Method specialization for Semantic Scholar identifiers or URL lookups."""

    entry_kind = "Semantic Scholar papers"
    source_fallback = "Semantic Scholar"

    @override
    def extract_entries(self, path: Path) -> list[str]:
        seen: set[str] = set()
        entries: list[str] = []
        for url in read_url_lines(path):
            identifier = self.identifier_for_url(url)
            if not identifier:
                self.record_parse_failure(f"could not parse Semantic Scholar identifier from: {url!r}")
                continue
            if identifier not in seen:
                seen.add(identifier)
                entries.append(identifier)
        return entries

    def identifier_for_url(self, url: str) -> str:
        if "semanticscholar.org/paper/" in url:
            return url.rstrip("/").split("/")[-1]
        return f"URL:{url}"

    @override
    def source_key_for_entry(self, entry: str) -> str | None:
        return self.normalize_source_key(entry)

    @override
    def source_key_for_token(self, token: str) -> str | None:
        identifier = self.identifier_for_url(token)
        return self.normalize_source_key(identifier) if identifier else None

    @override
    def entry_label(self, entry: str) -> str:
        return entry.removeprefix("URL:")

    @override
    def fetch_fields(self, entry: str, context: dict[str, Any]) -> FieldMap:
        _ = context
        fallback_url = entry.removeprefix("URL:") if entry.startswith("URL:") else ""
        fields = semantic_scholar_fields(entry, fallback_url)
        if not fields.get("source"):
            fields["source"] = self.source_fallback
        return fields

    @override
    def build_metadata(self, entry: str, fields: FieldMap) -> FieldMap:
        _ = entry
        metadata = build_page_metadata(fields)
        if fields.get("arxiv_id"):
            metadata["arxiv_id"] = fields["arxiv_id"]
        return metadata


def pdf_text_from_url(url: str, *, first_pages: int = 2) -> str:
    """Download a PDF URL and extract leading text using pdftotext."""
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    with tempfile.NamedTemporaryFile(suffix=".pdf") as tmp:
        tmp.write(response.content)
        tmp.flush()
        proc = subprocess.run(
            ["pdftotext", "-f", "1", "-l", str(first_pages), tmp.name, "-"],
            check=True,
            capture_output=True,
            text=True,
        )
    return proc.stdout


class PdfTextPrefillScript(PagePrefillScript[str], ABC):
    """Template Method specialization for older PDF-only archives."""

    entry_kind = "PDF URLs"
    source_hint = "PDF"
    first_pages = 2

    @override
    def extract_entries(self, path: Path) -> list[str]:
        seen: set[str] = set()
        entries: list[str] = []
        for url in read_url_lines(path):
            if not self.accept_url(url):
                self.record_parse_failure(f"could not parse {self.source_hint} PDF URL from: {url!r}")
                continue
            if url not in seen:
                seen.add(url)
                entries.append(url)
        return entries

    def accept_url(self, url: str) -> bool:
        return url.lower().endswith(".pdf")

    @override
    def source_key_for_entry(self, entry: str) -> str | None:
        return self.normalize_source_key(entry)

    @override
    def source_key_for_token(self, token: str) -> str | None:
        if not self.accept_url(token):
            return None
        return self.normalize_source_key(token)

    @override
    def fetch_fields(self, entry: str, context: dict[str, Any]) -> FieldMap:
        _ = context
        return self.fields_from_pdf(entry, pdf_text_from_url(entry, first_pages=self.first_pages))

    @abstractmethod
    def fields_from_pdf(self, url: str, text: str) -> FieldMap:
        """Return normalized metadata fields from extracted PDF text."""
