"""Batch-prefill metadata.yml files from a list of RSS proceedings URLs.

Usage:
    python -m knowledge_base.prefill rss [--input PATH] [--overwrite]

Defaults:
    --input      todo/papers/RSS.md
    --overwrite  False (skip entries whose metadata.yml already exists)

Accepts Robotics: Science and Systems PDF or HTML URLs. The script reads the
companion HTML page, extracts citation meta tags, the abstract, and the DOI
from the embedded BibTeX block when present.
"""

import re
from collections.abc import Callable
from pathlib import Path
from typing import Any

from knowledge_base.prefill.doi import fetch_page_html
from knowledge_base.prefill.runner import REPO_ROOT
from knowledge_base.prefill.todo_file import (
    absolutize_url,
    clean_text,
    first_element_text,
    first_meta,
    meta_contents,
    read_url_lines,
)

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "RSS.md"

_RSS_RE = re.compile(r"roboticsproceedings\.org/(rss\d{2})/(p\d+)\.(?:pdf|html)", re.I)
_RSS_PROGRAM_RE = re.compile(r"roboticsconference\.org/program/papers/(\d+)", re.I)
_BASE = "https://www.roboticsproceedings.org"


def extract_entries(path: Path, on_parse_failure: Callable[[str], None] | None = None) -> list[tuple[str, str, str]]:
    """Return deduplicated (html_url, pdf_url, key) tuples."""
    seen: set[str] = set()
    entries: list[tuple[str, str, str]] = []
    for url in read_url_lines(path):
        m = _RSS_RE.search(url)
        if not m:
            program_match = _RSS_PROGRAM_RE.search(url)
            if program_match:
                paper_id = program_match.group(1)
                key = f"program/papers/{paper_id}"
                if key not in seen:
                    seen.add(key)
                    entries.append((f"https://roboticsconference.org/program/papers/{paper_id}/", "", key))
                continue
            message = f"could not parse RSS URL from: {url!r}"
            if on_parse_failure:
                on_parse_failure(message)
            else:
                print(f"  WARN: {message}")
            continue
        volume, paper = m.group(1).lower(), m.group(2)
        key = f"{volume}/{paper}"
        if key in seen:
            continue
        seen.add(key)
        html_url = f"{_BASE}/{volume}/{paper}.html"
        pdf_url = f"{_BASE}/{volume}/{paper}.pdf"
        entries.append((html_url, pdf_url, key))
    return entries


def extract_abstract(html: str) -> str:
    m = re.search(r"<b\b[^>]*>\s*Abstract:\s*</b>\s*(?:</p>\s*<p\b[^>]*>)?(.*?)</p>", html, re.DOTALL | re.I)
    return clean_text(m.group(1)) if m else ""


def extract_bibtex_doi(html: str) -> str:
    m = re.search(r"\bDOI\s*=\s*[{'\"]([^}'\"]+)[}'\"]", html, flags=re.I)
    return m.group(1).strip() if m else ""


def canonical_source(source: str) -> str:
    if source.startswith("Robotics: Science and Systems"):
        return "Robotics: Science and Systems"
    return source


def fetch_rss_fields(html_url: str, fallback_pdf_url: str) -> dict[str, Any]:
    html = fetch_page_html(html_url)
    title = first_meta(html, "citation_title") or first_element_text(html, "h3")
    authors = meta_contents(html, "citation_author")
    if not authors:
        author_match = re.search(
            r'<div\b[^>]*class=["\'][^"\']*paper-author-name[^"\']*["\'][^>]*>(.*?)</div>', html, re.DOTALL | re.I
        )
        if author_match:
            authors = [author.strip() for author in clean_text(author_match.group(1)).split(",") if author.strip()]
    year_raw = first_meta(html, "citation_publication_date")
    year = int(year_raw[:4]) if year_raw[:4].isdigit() else 0
    if not year:
        year_match = re.search(r"\bRSS\s+((?:19|20)\d{2})\b", first_meta(html, "description"), re.I)
        year = int(year_match.group(1)) if year_match else 0
    source = canonical_source(first_meta(html, "citation_conference_title"))
    pdf_raw = first_meta(html, "citation_pdf_url")
    if not pdf_raw:
        pdf_match = re.search(r'href=["\']([^"\']*roboticsproceedings\.org/[^"\']+\.pdf)["\']', html, re.I)
        pdf_raw = pdf_match.group(1) if pdf_match else ""
    pdf_url = absolutize_url(html_url, pdf_raw) if pdf_raw else fallback_pdf_url
    doi = extract_bibtex_doi(html)
    abstract = extract_abstract(html)

    if not title or not authors or not year:
        raise ValueError(f"Incomplete RSS metadata at {html_url!r}")

    links_alt = [html_url]
    if doi:
        links_alt.append(f"https://doi.org/{doi}")

    return {
        "title": title,
        "authors": authors,
        "year": year,
        "source": source or "Robotics: Science and Systems",
        "type": "Conference Paper",
        "doi": doi or None,
        "abstract": abstract,
        "link": pdf_url,
        "links_alt": links_alt,
    }


def entry_label(entry: tuple[str, str, str]) -> str:
    _html_url, _pdf_url, key = entry
    return key


def source_key_for_token(token: str) -> str | None:
    match = _RSS_RE.search(token)
    if match:
        return f"{match.group(1).lower()}/{match.group(2)}"
    program_match = _RSS_PROGRAM_RE.search(token)
    return f"program/papers/{program_match.group(1)}" if program_match else None


def fetch_fields(entry: tuple[str, str, str], context: dict[str, Any]) -> dict[str, Any]:
    _ = context
    html_url, pdf_url, _key = entry
    return fetch_rss_fields(html_url, pdf_url)
