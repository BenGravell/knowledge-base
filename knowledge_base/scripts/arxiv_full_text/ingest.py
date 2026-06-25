"""CLI and orchestration for arXiv full-text ingest."""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from knowledge_base.catalog import Catalog, Entry
from knowledge_base.scripts.arxiv_full_text.docling import arxiv_latex_markdown, arxiv_pdf_markdown
from knowledge_base.scripts.arxiv_full_text.docling import self_test as docling_self_test
from knowledge_base.scripts.arxiv_full_text.html import arxiv_html_markdown
from knowledge_base.scripts.arxiv_full_text.html import self_test as html_self_test
from knowledge_base.scripts.arxiv_full_text.settings import (
    DEFAULT_SLEEP_SECONDS,
    METADATA_ROOT,
    MIN_MARKDOWN_CHARS,
    SIDECAR_NAME,
    executable_available,
    python_env_executable,
)
from knowledge_base.scripts.arxiv_full_text.text import (
    embed_text_path,
    write_converted_sidecar,
    wrote,
)
from knowledge_base.scripts.arxiv_full_text.text import (
    self_test as text_self_test,
)
from knowledge_base.utils.arxiv_utils import arxiv_pdf_url, normalize_arxiv_id


def candidates(
    catalog: Catalog,
    requested_ids: list[str],
    requested_paper_ids: list[str],
) -> list[Entry]:
    requested = {normalize_arxiv_id(arxiv_id) for arxiv_id in requested_ids}
    requested_papers = {paper_id.strip() for paper_id in requested_paper_ids if paper_id.strip()}
    entries = [entry for entry in catalog.entries if entry.arxiv_id]
    if requested:
        entries = [entry for entry in entries if entry.arxiv_id in requested]
    if requested_papers:
        entries = [entry for entry in entries if entry.id in requested_papers]
    return entries


def write_if_markdown(
    entry: Entry,
    path: Path,
    source_label: str | None,
    markdown: str | None,
    message: str,
    args: argparse.Namespace,
) -> str:
    if markdown is None or source_label is None:
        return message
    return write_converted_sidecar(entry, path, markdown, source_label, args)


def try_arxiv_html(entry: Entry, path: Path, args: argparse.Namespace) -> str:
    return write_if_markdown(entry, path, *arxiv_html_markdown(entry, args), args)


def try_arxiv_latex(entry: Entry, path: Path, args: argparse.Namespace) -> str:
    markdown, message = arxiv_latex_markdown(entry, args)
    return write_if_markdown(entry, path, "arxiv-latex", markdown, message, args)


def try_arxiv_pdf(entry: Entry, path: Path, args: argparse.Namespace) -> str:
    markdown, message = arxiv_pdf_markdown(entry, args)
    return write_if_markdown(entry, path, "arxiv-pdf", markdown, message, args)


def process_entry(entry: Entry, args: argparse.Namespace) -> str:
    path = embed_text_path(entry)
    if path.exists() and not args.force:
        return f"skip existing {entry.id}"
    if not entry.arxiv_id:
        return f"skip no-arxiv-id {entry.id}"

    messages = [try_arxiv_html(entry, path, args)]
    if wrote(messages[-1]):
        return messages[-1]
    if not args.has_docling:
        messages.append("docling not found")
    else:
        for attempt in (try_arxiv_latex, try_arxiv_pdf):
            messages.append(attempt(entry, path, args))
            if wrote(messages[-1]):
                return messages[-1]
    return f"skip metadata-only {entry.id}: {'; '.join(messages)}"


def self_test() -> None:
    text_self_test()
    html_self_test()
    docling_self_test()
    assert arxiv_pdf_url("2401.00001") == "https://arxiv.org/pdf/2401.00001"
    assert Path(python_env_executable("pandoc")).parent == Path(sys.executable).parent
    assert Path(python_env_executable("docling")).parent == Path(sys.executable).parent


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", action="append", default=[], help="Only process this arXiv ID. Repeatable.")
    parser.add_argument(
        "--paper-id", action="append", default=[], help="Only process this arXiv-backed catalog paper ID."
    )
    parser.add_argument("--limit", type=int, default=0, help="Maximum candidate entries to process.")
    parser.add_argument("--force", action="store_true", help=f"Overwrite existing {SIDECAR_NAME} files.")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and convert, but do not write files.")
    parser.add_argument("--sleep", type=float, default=DEFAULT_SLEEP_SECONDS, help="Delay between entries.")
    parser.add_argument("--timeout", type=int, default=60, help="HTTP timeout in seconds.")
    parser.add_argument("--min-chars", type=int, default=MIN_MARKDOWN_CHARS, help="Minimum readable output size.")
    parser.add_argument(
        "--pandoc", default=python_env_executable("pandoc"), help="Pandoc executable from the Python environment."
    )
    parser.add_argument("--pandoc-data-dir", default="", help="Optional Pandoc data directory.")
    parser.add_argument(
        "--docling",
        default=python_env_executable("docling"),
        help="Docling executable from the Python environment for LaTeX/PDF fallbacks.",
    )
    parser.add_argument("--docling-device", default="", help="Optional Docling device, such as cpu or cuda.")
    parser.add_argument("--docling-timeout", type=int, default=300, help="Docling document timeout in seconds.")
    parser.add_argument("--self-test", action="store_true", help="Run lightweight internal assertions and exit.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.self_test:
        self_test()
        return 0

    args.has_pandoc = executable_available(args.pandoc)
    args.has_docling = executable_available(args.docling)

    entries = candidates(Catalog.from_metadata_root(METADATA_ROOT), args.id, args.paper_id)
    if args.limit:
        entries = entries[: args.limit]

    for index, entry in enumerate(entries):
        print(process_entry(entry, args))
        if args.sleep and index < len(entries) - 1:
            time.sleep(args.sleep)
    print(f"processed {len(entries)} candidate(s)")
    return 0
