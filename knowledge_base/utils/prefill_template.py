"""Template Method machinery for paper metadata prefill scripts."""

from __future__ import annotations

import subprocess
import tempfile
import time
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Generic, TypeVar
from urllib.parse import quote

import requests

from knowledge_base.apps.arxiv_utils import metadata_to_yaml
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
)

EntryT = TypeVar("EntryT")
REPO_ROOT = Path(__file__).resolve().parents[2]


class HaltPrefill(Exception):
    """Signal that a prefill run should stop without treating it as a failure."""


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

    def run(self) -> None:
        args = make_parser(self.description, self.default_input).parse_args()
        entries = self.extract_entries(args.input)
        print(f"Found {len(entries)} unique {self.entry_kind} in {args.input}")

        context = self.prepare_context(args)
        if args.list_skipped:
            self.list_skipped(entries, context)
            return

        ok = skipped = failed = 0

        for i, entry in enumerate(entries, 1):
            prefix = f"[{i}/{len(entries)}] {self.entry_label(entry)}"

            existing = self.existing_for_entry(entry, context)
            if should_skip(existing, args):
                print(f"{prefix}  SKIP (exists: {existing})")
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
                skipped += 1
                continue

            metadata = self.build_metadata(entry, fields)
            yaml_text = metadata_to_yaml(metadata)
            out = self.write_metadata(entry, fields, yaml_text)
            print(self.success_message(prefix, entry, fields, out))
            ok += 1

            if args.first is not None and ok + failed >= args.first:
                break
            time.sleep(self.delay)

        print(f"\nDone: {ok} written, {skipped} skipped, {failed} failed")

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

    def prepare_context(self, _args: Any) -> dict[str, Any]:
        return {}

    @abstractmethod
    def extract_entries(self, path: Path) -> list[EntryT]:
        """Parse and deduplicate entries from the input file."""

    def entry_label(self, entry: EntryT) -> str:
        return str(entry)

    def existing_for_entry(self, _entry: EntryT, _context: dict[str, Any]) -> Path | None:
        return None

    def needs_fetch_for_list_skipped(self, _entry: EntryT, _context: dict[str, Any]) -> bool:
        return True

    @abstractmethod
    def fetch_fields(self, entry: EntryT, context: dict[str, Any]) -> dict:
        """Return normalized metadata fields for *entry*."""

    def existing_for_fields(self, _fields: dict, _context: dict[str, Any]) -> Path | None:
        return None

    @abstractmethod
    def build_metadata(self, entry: EntryT, fields: dict) -> dict:
        """Build an ordered metadata dict ready for YAML serialization."""

    @abstractmethod
    def write_metadata(self, entry: EntryT, fields: dict, yaml_text: str) -> Path:
        """Write *yaml_text* and return the target path."""

    def success_message(self, prefix: str, _entry: EntryT, _fields: dict, out: Path) -> str:
        return f"{prefix}  OK -> {out}"

    def skipped_list_message(
        self,
        entry: EntryT,
        _fields: dict | None,
        existing: Path,
    ) -> str:
        return f"{self.entry_label(entry)}  {existing}"


class DoiPrefillScript(PrefillScript[EntryT], ABC):
    """Template Method specialization for DOI/Crossref-backed sources."""

    entry_kind = "DOIs"
    show_resolved_doi = False

    def prepare_context(self, _args: Any) -> dict[str, Any]:
        return {"doi_index": build_doi_index()}

    def entry_doi(self, _entry: EntryT) -> str | None:
        """Return a DOI known from the input entry, if available before fetching."""
        return None

    def resolve_doi(self, entry: EntryT) -> str:
        doi = self.entry_doi(entry)
        if doi:
            return doi
        raise NotImplementedError("Subclasses must implement resolve_doi() or entry_doi().")

    def existing_for_entry(self, entry: EntryT, context: dict[str, Any]) -> Path | None:
        doi = self.entry_doi(entry)
        return context["doi_index"].get(doi.lower()) if doi else None

    def needs_fetch_for_list_skipped(self, entry: EntryT, _context: dict[str, Any]) -> bool:
        return self.entry_doi(entry) is None

    def fetch_fields(self, entry: EntryT, _context: dict[str, Any]) -> dict:
        doi = self.resolve_doi(entry)
        data = fetch_with_retry(fetch_crossref, doi)
        return self.postprocess_crossref_data(entry, data)

    def postprocess_crossref_data(self, _entry: EntryT, data: dict) -> dict:
        return data

    def existing_for_fields(self, fields: dict, context: dict[str, Any]) -> Path | None:
        doi = str(fields.get("doi") or "").strip()
        return context["doi_index"].get(doi.lower()) if doi else None

    def build_metadata(self, entry: EntryT, fields: dict) -> dict:
        return self.postprocess_metadata(entry, fields, build_doi_metadata(fields))

    def postprocess_metadata(self, _entry: EntryT, _fields: dict, metadata: dict) -> dict:
        return metadata

    def write_metadata(self, _entry: EntryT, fields: dict, yaml_text: str) -> Path:
        folder = generate_folder_name(fields["year"], fields["authors"], fields["title"])
        return write_doi_metadata(fields["year"], folder, yaml_text)

    def output_path(self, fields: dict) -> Path:
        folder = generate_folder_name(fields["year"], fields["authors"], fields["title"])
        return doi_target_path(fields["year"], folder)

    def success_message(self, prefix: str, entry: EntryT, fields: dict, out: Path) -> str:
        if self.show_resolved_doi or self.entry_doi(entry) is None:
            return f"{prefix}  OK doi={fields['doi']} -> {out}"
        return super().success_message(prefix, entry, fields, out)

    def skipped_list_message(
        self,
        entry: EntryT,
        fields: dict | None,
        existing: Path,
    ) -> str:
        doi = str(fields.get("doi") or "") if fields else self.entry_doi(entry)
        return f"{self.entry_label(entry)} ({doi})  {existing}" if fields else f"{doi}  {existing}"


class PagePrefillScript(PrefillScript[EntryT], ABC):
    """Template Method specialization for proceedings pages without Crossref."""

    entry_kind = "entries"

    def prepare_context(self, _args: Any) -> dict[str, Any]:
        return {"doi_index": build_doi_index()}

    def existing_for_fields(self, fields: dict, context: dict[str, Any]) -> Path | None:
        doi = str(fields.get("doi") or "").strip()
        if doi:
            existing = context["doi_index"].get(doi.lower())
            if existing:
                return existing
        out = self.output_path(fields)
        return out if out.exists() else None

    def build_metadata(self, _entry: EntryT, fields: dict) -> dict:
        return build_page_metadata(fields)

    def output_path(self, fields: dict) -> Path:
        folder = generate_folder_name(fields["year"], fields["authors"], fields["title"])
        return doi_target_path(fields["year"], folder)

    def write_metadata(self, _entry: EntryT, fields: dict, yaml_text: str) -> Path:
        folder = generate_folder_name(fields["year"], fields["authors"], fields["title"])
        return write_doi_metadata(fields["year"], folder, yaml_text)


class UrlDoiPrefillScript(DoiPrefillScript[str]):
    """Template Method specialization for source files that contain publisher URLs."""

    entry_kind = "URLs"
    source_hint = "publisher"

    def extract_entries(self, path: Path) -> list[str]:
        seen: set[str] = set()
        entries: list[str] = []
        for url in read_url_lines(path):
            if not self.accept_url(url):
                print(f"  WARN: could not parse {self.source_hint} URL from: {url!r}")
                continue
            key = self.entry_key(url)
            if key not in seen:
                seen.add(key)
                entries.append(url)
        return entries

    def accept_url(self, _url: str) -> bool:
        return True

    def entry_key(self, url: str) -> str:
        return (self.entry_doi(url) or url).lower()

    def entry_label(self, entry: str) -> str:
        return self.entry_doi(entry) or entry

    def entry_doi(self, entry: str) -> str | None:
        return extract_doi_from_url(entry) or None

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

    def postprocess_crossref_data(self, entry: str, data: dict) -> dict:
        data = {**data, "link": entry}
        if data["abstract"]:
            return data
        try:
            abstract = scrape_abstract_from_html(fetch_page_html(entry))
        except Exception:
            return data
        return {**data, "abstract": abstract} if abstract else data

    def postprocess_metadata(self, entry: str, fields: dict, metadata: dict) -> dict:
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

    def extract_entries(self, path: Path) -> list[str]:
        seen: set[str] = set()
        entries: list[str] = []
        for url in read_url_lines(path):
            if not self.accept_url(url):
                print(f"  WARN: could not parse {self.source_hint} URL from: {url!r}")
                continue
            key = self.normalize_url(url)
            if key not in seen:
                seen.add(key)
                entries.append(key)
        return entries

    def accept_url(self, _url: str) -> bool:
        return True

    def normalize_url(self, url: str) -> str:
        return url

    def fetch_fields(self, entry: str, _context: dict) -> dict:
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


def semantic_scholar_type(publication_types: list[str] | None) -> str:
    values = {str(t).lower() for t in publication_types or []}
    if any("review" in t for t in values):
        return "Survey Paper"
    if any("conference" in t for t in values):
        return "Conference Paper"
    if any("journal" in t for t in values):
        return "Journal Paper"
    return "Other"


def semantic_scholar_fields(identifier: str, fallback_url: str = "") -> dict:
    """Return normalized metadata for a Semantic Scholar paper id or URL lookup."""
    if identifier.startswith("URL:"):
        paper_id = "URL:" + quote(identifier.removeprefix("URL:"), safe="")
    else:
        paper_id = quote(identifier, safe="")
    url = _S2_BY_ID.format(paper_id=paper_id, fields=_S2_FIELDS)
    for attempt in range(4):
        r = requests.get(url, timeout=60)
        if r.status_code != 429 or attempt == 3:
            break
        time.sleep(5 * (attempt + 1))
    r.raise_for_status()
    data = r.json()

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

    def extract_entries(self, path: Path) -> list[str]:
        seen: set[str] = set()
        entries: list[str] = []
        for url in read_url_lines(path):
            identifier = self.identifier_for_url(url)
            if not identifier:
                print(f"  WARN: could not parse Semantic Scholar identifier from: {url!r}")
                continue
            if identifier not in seen:
                seen.add(identifier)
                entries.append(identifier)
        return entries

    def identifier_for_url(self, url: str) -> str:
        if "semanticscholar.org/paper/" in url:
            return url.rstrip("/").split("/")[-1]
        return f"URL:{url}"

    def entry_label(self, entry: str) -> str:
        return entry.removeprefix("URL:")

    def fetch_fields(self, entry: str, _context: dict) -> dict:
        fallback_url = entry.removeprefix("URL:") if entry.startswith("URL:") else ""
        fields = semantic_scholar_fields(entry, fallback_url)
        if not fields.get("source"):
            fields["source"] = self.source_fallback
        return fields

    def build_metadata(self, _entry: str, fields: dict) -> dict:
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

    def extract_entries(self, path: Path) -> list[str]:
        seen: set[str] = set()
        entries: list[str] = []
        for url in read_url_lines(path):
            if not self.accept_url(url):
                print(f"  WARN: could not parse {self.source_hint} PDF URL from: {url!r}")
                continue
            if url not in seen:
                seen.add(url)
                entries.append(url)
        return entries

    def accept_url(self, url: str) -> bool:
        return url.lower().endswith(".pdf")

    def fetch_fields(self, entry: str, _context: dict) -> dict:
        return self.fields_from_pdf(entry, pdf_text_from_url(entry, first_pages=self.first_pages))

    @abstractmethod
    def fields_from_pdf(self, url: str, text: str) -> dict:
        """Return normalized metadata fields from extracted PDF text."""
