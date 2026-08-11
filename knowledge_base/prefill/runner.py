"""Table-driven runner for paper metadata prefill sources."""

from __future__ import annotations

import argparse
import sys
import time
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from knowledge_base.config import REPO_ROOT  # re-exported for old handler imports
from knowledge_base.prefill.doi import (
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
from knowledge_base.prefill.pdf import pdf_text_from_url
from knowledge_base.prefill.todo_file import (
    build_page_metadata,
    citation_doi,
    extract_doi_from_url,
    fetch_citation_page_fields,
    read_source_rows,
    read_url_lines,
    source_row_token,
    write_text_atomic,
)
from knowledge_base.scripts.arxiv_full_text.ingest import main as ingest_arxiv
from knowledge_base.utils.arxiv_utils import metadata_to_yaml
from knowledge_base.utils.paper_ids import paper_id_from_metadata

FieldMap = dict[str, Any]
Entry = Any
ParseFailure = Callable[[str], None]


class HaltPrefill(Exception):
    """Signal that a prefill run should stop without treating it as a failure."""


@dataclass(frozen=True)
class SourceSpec:
    name: str
    description: str
    default_input: Path
    mode: str
    entry_kind: str = "entries"
    source_hint: str = "source"
    delay: float = BASE_DELAY
    fetch_error_label: str = "fetching metadata"
    show_resolved_doi: bool = False
    source_fallback: str = ""
    type_fallback: str = "Journal Paper"
    first_pages: int = 2
    accept_url: Callable[[str], bool] | None = None
    normalize_url: Callable[[str], str] | None = None
    entry_label: Callable[[Entry], str] | None = None
    entry_doi: Callable[[Entry], str | None] | None = None
    resolve_doi: Callable[[Entry], str] | None = None
    extract_entries: Callable[[Path, ParseFailure], list[Entry]] | None = None
    source_key_for_entry: Callable[[Entry], str | None] | None = None
    source_key_for_token: Callable[[str], str | None] | None = None
    prepare_context: Callable[[list[Entry], argparse.Namespace], dict[str, Any]] | None = None
    existing_for_entry: Callable[[Entry, dict[str, Any]], Path | None] | None = None
    existing_for_fields: Callable[[FieldMap, dict[str, Any]], Path | None] | None = None
    needs_fetch_for_list_skipped: Callable[[Entry, dict[str, Any]], bool] | None = None
    fetch_fields: Callable[[Entry, dict[str, Any]], FieldMap] | None = None
    fields_from_pdf: Callable[[str, str], FieldMap] | None = None
    postprocess_crossref_data: Callable[[Entry, FieldMap], FieldMap] | None = None
    build_metadata: Callable[[Entry, FieldMap], FieldMap] | None = None
    postprocess_metadata: Callable[[Entry, FieldMap, FieldMap], FieldMap] | None = None
    write_metadata: Callable[[Entry, FieldMap, str], Path] | None = None
    success_message: Callable[[str, Entry, FieldMap, Path], str] | None = None
    doi_link_alt: bool = False


def _input(name: str) -> Path:
    return REPO_ROOT / "todo" / "papers" / f"{name.upper()}.md"


def _normalize_key(value: str) -> str:
    return str(value).strip().lower()


def _accept(spec: SourceSpec, url: str) -> bool:
    return spec.accept_url(url) if spec.accept_url else True


def _entry_doi(spec: SourceSpec, entry: Entry) -> str | None:
    if spec.entry_doi:
        doi = spec.entry_doi(entry)
        if doi:
            return doi
    if spec.mode == "url_doi" and isinstance(entry, str):
        return extract_doi_from_url(entry) or None
    return None


def _entry_label(spec: SourceSpec, entry: Entry) -> str:
    if spec.entry_label:
        return spec.entry_label(entry)
    if spec.mode == "url_doi" and isinstance(entry, str):
        return _entry_doi(spec, entry) or entry
    return str(entry)


def _url_doi_key(spec: SourceSpec, url: str) -> str:
    return (_entry_doi(spec, url) or url).lower()


def _extract_url_doi_entries(spec: SourceSpec, path: Path, record_parse_failure: ParseFailure) -> list[str]:
    seen: set[str] = set()
    entries: list[str] = []
    for url in read_url_lines(path):
        if not _accept(spec, url):
            record_parse_failure(f"could not parse {spec.source_hint} URL from: {url!r}")
            continue
        key = _url_doi_key(spec, url)
        if key not in seen:
            seen.add(key)
            entries.append(url)
    return entries


def _extract_citation_entries(spec: SourceSpec, path: Path, record_parse_failure: ParseFailure) -> list[str]:
    seen: set[str] = set()
    entries: list[str] = []
    for url in read_url_lines(path):
        if not _accept(spec, url):
            record_parse_failure(f"could not parse {spec.source_hint} URL from: {url!r}")
            continue
        key = spec.normalize_url(url) if spec.normalize_url else url
        if key not in seen:
            seen.add(key)
            entries.append(key)
    return entries


def _extract_pdf_entries(spec: SourceSpec, path: Path, record_parse_failure: ParseFailure) -> list[str]:
    seen: set[str] = set()
    entries: list[str] = []
    for url in read_url_lines(path):
        if not _accept(spec, url):
            record_parse_failure(f"could not parse {spec.source_hint} PDF URL from: {url!r}")
            continue
        if url not in seen:
            seen.add(url)
            entries.append(url)
    return entries


def _extract_entries(spec: SourceSpec, path: Path, record_parse_failure: ParseFailure) -> list[Entry]:
    if spec.extract_entries:
        return spec.extract_entries(path, record_parse_failure)
    if spec.mode == "url_doi":
        return _extract_url_doi_entries(spec, path, record_parse_failure)
    if spec.mode == "citation":
        return _extract_citation_entries(spec, path, record_parse_failure)
    if spec.mode == "pdf":
        return _extract_pdf_entries(spec, path, record_parse_failure)
    raise NotImplementedError(f"{spec.name} needs an extract_entries handler")


def _source_key_for_entry(spec: SourceSpec, entry: Entry) -> str | None:
    if spec.source_key_for_entry:
        key = spec.source_key_for_entry(entry)
        return _normalize_key(key) if key else None
    if spec.mode == "url_doi" and isinstance(entry, str):
        return _normalize_key(_url_doi_key(spec, entry))
    doi = _entry_doi(spec, entry)
    if doi:
        return _normalize_key(doi)
    label = _entry_label(spec, entry)
    return _normalize_key(label) if label else None


def _source_key_for_token(spec: SourceSpec, token: str) -> str | None:
    if spec.source_key_for_token:
        key = spec.source_key_for_token(token)
        return _normalize_key(key) if key else None
    if spec.mode == "url_doi":
        if not _accept(spec, token):
            return None
        return _normalize_key(_url_doi_key(spec, token))
    if spec.mode in {"citation", "pdf"}:
        if not _accept(spec, token):
            return None
        token = spec.normalize_url(token) if spec.normalize_url else token
        return _normalize_key(token)
    doi = extract_doi_from_url(token)
    return _normalize_key(doi) if doi else _normalize_key(token)


def _remove_source_rows(path: Path, handled_key: str, key_for_token: Callable[[str], str | None]) -> int:
    raw_lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    removed = 0
    kept_lines: list[str] = []
    for line in raw_lines:
        token = source_row_token(line)
        row_key = key_for_token(token) if token else None
        if row_key and row_key == handled_key:
            removed += 1
            continue
        kept_lines.append(line)
    if removed:
        write_text_atomic(path, "".join(kept_lines))
    return removed


def _remove_handled_source_rows(spec: SourceSpec, source_path: Path, entry: Entry, prefix: str) -> int:
    key = _source_key_for_entry(spec, entry)
    if not key:
        return 0
    try:
        removed = _remove_source_rows(source_path, key, lambda token: _source_key_for_token(spec, token))
    except Exception as exc:
        raise RuntimeError(
            f"Metadata for {_entry_label(spec, entry)!r} was handled, but {source_path} could not be updated safely."
        ) from exc
    if removed:
        print(f"{prefix}  SOURCE -{removed} row(s)")
    return removed


def _default_context(spec: SourceSpec, entries: list[Entry], args: argparse.Namespace) -> dict[str, Any]:
    if spec.prepare_context:
        return spec.prepare_context(entries, args)
    return {"doi_index": build_doi_index()}


def _existing_for_entry(spec: SourceSpec, entry: Entry, context: dict[str, Any]) -> Path | None:
    if spec.existing_for_entry:
        return spec.existing_for_entry(entry, context)
    doi = _entry_doi(spec, entry)
    return context.get("doi_index", {}).get(doi.lower()) if doi else None


def _output_path(fields: FieldMap) -> Path:
    folder = generate_folder_name(fields["year"], fields["authors"], fields["title"])
    return doi_target_path(fields["year"], folder)


def _existing_for_fields(spec: SourceSpec, fields: FieldMap, context: dict[str, Any]) -> Path | None:
    if spec.existing_for_fields:
        return spec.existing_for_fields(fields, context)
    if spec.mode == "custom":
        return None
    doi = str(fields.get("doi") or "").strip()
    if doi:
        existing = context.get("doi_index", {}).get(doi.lower())
        if existing:
            return existing
    out = _output_path(fields)
    return out if out.exists() else None


def _needs_fetch_for_list_skipped(spec: SourceSpec, entry: Entry, context: dict[str, Any]) -> bool:
    if spec.needs_fetch_for_list_skipped:
        return spec.needs_fetch_for_list_skipped(entry, context)
    if spec.mode in {"doi", "url_doi"}:
        return _entry_doi(spec, entry) is None
    return True


def _resolve_doi(spec: SourceSpec, entry: Entry) -> str:
    if spec.resolve_doi:
        return spec.resolve_doi(entry)
    doi = _entry_doi(spec, entry)
    if doi:
        return doi
    if spec.mode == "url_doi" and isinstance(entry, str):
        html = fetch_page_html(entry)
        try:
            return scrape_doi_from_html(html)
        except Exception:
            doi = citation_doi(html, entry)
            if doi:
                return str(doi)
    raise ValueError(f"Could not resolve DOI for {_entry_label(spec, entry)!r}")


def _postprocess_crossref_data(spec: SourceSpec, entry: Entry, data: FieldMap) -> FieldMap:
    if spec.mode == "url_doi" and isinstance(entry, str):
        data = {**data, "link": entry}
        if not data["abstract"]:
            try:
                abstract = scrape_abstract_from_html(fetch_page_html(entry))
            except Exception:
                abstract = ""
            if abstract:
                data = {**data, "abstract": abstract}
    if spec.postprocess_crossref_data:
        return spec.postprocess_crossref_data(entry, data)
    return data


def _fetch_fields(spec: SourceSpec, entry: Entry, context: dict[str, Any]) -> FieldMap:
    if spec.fetch_fields:
        return spec.fetch_fields(entry, context)
    if spec.mode == "citation" and isinstance(entry, str):
        return fetch_citation_page_fields(
            entry,
            source_fallback=spec.source_fallback,
            type_fallback=spec.type_fallback,
        )
    if spec.mode == "semantic":
        from knowledge_base.prefill.sources import semantic_scholar

        fallback_url = entry.removeprefix("URL:") if isinstance(entry, str) and entry.startswith("URL:") else ""
        fields = semantic_scholar.fields(str(entry), fallback_url)
        if not fields.get("source"):
            fields["source"] = spec.source_fallback or "Semantic Scholar"
        return fields
    if spec.mode == "pdf" and isinstance(entry, str):
        if not spec.fields_from_pdf:
            raise NotImplementedError(f"{spec.name} needs fields_from_pdf")
        return spec.fields_from_pdf(entry, pdf_text_from_url(entry, first_pages=spec.first_pages))
    doi = _resolve_doi(spec, entry)
    data = fetch_with_retry(fetch_crossref, doi)
    return _postprocess_crossref_data(spec, entry, data)


def _with_doi_alt(metadata: FieldMap, doi: str) -> FieldMap:
    if not doi:
        return metadata
    links_alt = list(metadata.get("links_alt") or [])
    links_alt.append(f"https://doi.org/{doi}")
    links_alt = list(dict.fromkeys(x for x in links_alt if x and x != metadata.get("link")))
    return {**metadata, "links_alt": links_alt}


def _build_metadata(spec: SourceSpec, entry: Entry, fields: FieldMap) -> FieldMap:
    if spec.build_metadata:
        metadata = spec.build_metadata(entry, fields)
    elif spec.mode in {"doi", "url_doi"}:
        metadata = build_doi_metadata(fields)
    else:
        metadata = build_page_metadata(fields)

    if spec.mode == "url_doi":
        doi = str(fields.get("doi") or _entry_doi(spec, entry) or "").strip()
        metadata = _with_doi_alt(metadata, doi)
    if spec.doi_link_alt:
        metadata = _with_doi_alt(metadata, str(fields.get("doi") or _entry_doi(spec, entry) or "").strip())
    if spec.postprocess_metadata:
        metadata = spec.postprocess_metadata(entry, fields, metadata)
    return metadata


def _write_metadata(spec: SourceSpec, entry: Entry, fields: FieldMap, yaml_text: str) -> Path:
    if spec.write_metadata:
        return spec.write_metadata(entry, fields, yaml_text)
    folder = generate_folder_name(fields["year"], fields["authors"], fields["title"])
    return write_doi_metadata(fields["year"], folder, yaml_text)


def _success_message(spec: SourceSpec, prefix: str, entry: Entry, fields: FieldMap, out: Path) -> str:
    if spec.success_message:
        return spec.success_message(prefix, entry, fields, out)
    if spec.mode in {"doi", "url_doi"} and (spec.show_resolved_doi or _entry_doi(spec, entry) is None):
        return f"{prefix}  OK doi={fields['doi']} -> {out}"
    return f"{prefix}  OK -> {out}"


def _ingest_embed_text(metadata: FieldMap, out: Path) -> None:
    if not str(metadata.get("arxiv_id") or "").strip():
        return
    paper_id = paper_id_from_metadata(out, metadata)
    ingest_arxiv(["--paper-id", paper_id, "--sleep", "0"])


def _skipped_list_message(spec: SourceSpec, entry: Entry, fields: FieldMap | None, existing: Path) -> str:
    if spec.mode in {"doi", "url_doi"}:
        doi = str(fields.get("doi") or "") if fields else _entry_doi(spec, entry)
        return f"{_entry_label(spec, entry)} ({doi})  {existing}" if fields else f"{doi}  {existing}"
    return f"{_entry_label(spec, entry)}  {existing}"


def _list_skipped(spec: SourceSpec, entries: list[Entry], context: dict[str, Any]) -> None:
    for entry in entries:
        existing = _existing_for_entry(spec, entry, context)
        if existing:
            print(_skipped_list_message(spec, entry, None, existing))
            continue
        if not _needs_fetch_for_list_skipped(spec, entry, context):
            continue
        try:
            fields = _fetch_fields(spec, entry, context)
        except HaltPrefill as exc:
            print(_entry_label(spec, entry))
            print(exc)
            break
        except Exception as exc:
            print(f"{_entry_label(spec, entry)}  ERROR {spec.fetch_error_label}: {exc}")
            time.sleep(spec.delay)
            continue
        existing = _existing_for_fields(spec, fields, context)
        if existing:
            print(_skipped_list_message(spec, entry, fields, existing))
        time.sleep(spec.delay)


def run_source(source: str, argv: Sequence[str] | None = None) -> None:
    from knowledge_base.prefill.sources.registry import source_specs

    specs = source_specs()
    key = source.lower().replace("-", "_")
    if key not in specs:
        available = ", ".join(sorted(specs))
        raise SystemExit(f"Unknown prefill source {source!r}. Available sources: {available}")

    spec = specs[key]
    args = make_parser(spec.description, spec.default_input).parse_args(argv)
    parse_failures: list[str] = []

    def record_parse_failure(message: str) -> None:
        parse_failures.append(message)
        print(f"  WARN: {message}")

    entries = _extract_entries(spec, args.input, record_parse_failure)
    print(f"Found {len(entries)} unique {spec.entry_kind} in {args.input}")

    context = _default_context(spec, entries, args)
    if args.list_skipped:
        _list_skipped(spec, entries, context)
        return

    ok = skipped = failed = source_removed = 0
    parse_failed = len(parse_failures)

    for i, entry in enumerate(entries, 1):
        prefix = f"[{i}/{len(entries)}] {_entry_label(spec, entry)}"

        existing = _existing_for_entry(spec, entry, context)
        if should_skip(existing, args):
            print(f"{prefix}  SKIP (exists: {existing})")
            source_removed += _remove_handled_source_rows(spec, args.input, entry, prefix)
            skipped += 1
            continue

        try:
            fields = _fetch_fields(spec, entry, context)
        except HaltPrefill as exc:
            print(prefix)
            print(exc)
            break
        except Exception as exc:
            print(f"{prefix}  ERROR {spec.fetch_error_label}: {exc}")
            failed += 1
            time.sleep(spec.delay)
            if args.first is not None and ok + failed >= args.first:
                break
            continue

        existing = existing or _existing_for_fields(spec, fields, context)
        if should_skip(existing, args):
            print(f"{prefix}  SKIP (exists: {existing})")
            source_removed += _remove_handled_source_rows(spec, args.input, entry, prefix)
            skipped += 1
            time.sleep(spec.delay)
            continue

        metadata = _build_metadata(spec, entry, fields)
        out = _write_metadata(spec, entry, fields, metadata_to_yaml(metadata))
        print(_success_message(spec, prefix, entry, fields, out))
        source_removed += _remove_handled_source_rows(spec, args.input, entry, prefix)
        _ingest_embed_text(metadata, out)
        ok += 1

        if args.first is not None and ok + failed >= args.first:
            break
        time.sleep(spec.delay)

    failed += parse_failed
    if parse_failed:
        print(
            f"\nDone: {ok} written, {skipped} skipped, {failed} failed "
            f"({parse_failed} parse), {source_removed} source row(s) removed"
        )
    else:
        print(f"\nDone: {ok} written, {skipped} skipped, {failed} failed, {source_removed} source row(s) removed")


def run_populated_sources(specs: dict[str, SourceSpec]) -> None:
    queued: list[tuple[str, int]] = []
    for name, spec in sorted(specs.items()):
        count = len(read_source_rows(spec.default_input)) if spec.default_input.is_file() else 0
        if count:
            queued.append((name, count))
    if not queued:
        print("No populated prefill sources found in todo/papers/.")
        return

    print(f"Prefilling {len(queued)} populated source(s): {', '.join(name for name, _ in queued)}")
    for name, count in queued:
        print(f"\n== {name} ({count} queued) ==")
        run_source(name)


def main(argv: Sequence[str] | None = None) -> None:
    from knowledge_base.prefill.sources.registry import source_specs

    args = list(sys.argv[1:] if argv is None else argv)
    specs = source_specs()
    if not args:
        run_populated_sources(specs)
        return
    if args[0] in {"-h", "--help"}:
        print("usage: prefill [SOURCE [prefill-options]]\n")
        print("With no SOURCE, run every populated todo/papers queue.\n")
        print("sources:")
        for name in sorted(specs):
            print(f"  {name}")
        return
    source, *source_args = args
    if source_args[:1] == ["--"]:
        source_args = source_args[1:]
    run_source(source, source_args)
