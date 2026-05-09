"""Batch-prefill metadata.yml files from a list of NeurIPS/NIPS URLs.

Usage:
    python knowledge_base/scripts/prefill/neurips.py [--input PATH] [--overwrite]

Defaults:
    --input      todo/papers/NEURIPS.md
    --overwrite  False (skip entries whose metadata.yml already exists)

Accepts both abstract-page and paper-PDF URLs. Metadata is fetched from the
NeurIPS ``-Metadata.json`` file beside each PDF, with HTML fallbacks.
"""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))

import requests

from knowledge_base.utils.doi_utils import fetch_page_html
from knowledge_base.utils.prefill_template import PagePrefillScript
from knowledge_base.utils.prefill_utils import (
    clean_text,
    first_element_text,
    first_meta,
    meta_contents,
    read_url_lines,
)

DEFAULT_INPUT = Path(__file__).parent.parent.parent.parent / "todo" / "papers" / "NEURIPS.md"

_ABSTRACT_RE = re.compile(
    r"(?:proceedings\.neurips\.cc|papers\.neurips\.cc|papers\.nips\.cc)/(?:paper|paper_files/paper)/(\d{4})/hash/([0-9a-f]+)-Abstract\.html",
    re.I,
)
_FILE_RE = re.compile(
    r"(?:proceedings\.neurips\.cc|papers\.neurips\.cc|papers\.nips\.cc)/paper_files/paper/(\d{4})/file/([0-9a-f]+)-",
    re.I,
)
_BASE = "https://proceedings.neurips.cc"


def extract_entries(path: Path) -> list[tuple[str, str]]:
    """Return deduplicated (year, hash) pairs."""
    seen: set[tuple[str, str]] = set()
    entries: list[tuple[str, str]] = []
    for url in read_url_lines(path):
        m = _ABSTRACT_RE.search(url) or _FILE_RE.search(url)
        if not m:
            print(f"  WARN: could not parse NeurIPS URL from: {url!r}")
            continue
        key = (m.group(1), m.group(2).lower())
        if key not in seen:
            seen.add(key)
            entries.append(key)
    return entries


def abstract_url(year: str, paper_hash: str) -> str:
    return f"{_BASE}/paper/{year}/hash/{paper_hash}-Abstract.html"


def pdf_url(year: str, paper_hash: str) -> str:
    return f"{_BASE}/paper_files/paper/{year}/file/{paper_hash}-Paper.pdf"


def metadata_url(year: str, paper_hash: str) -> str:
    return f"{_BASE}/paper_files/paper/{year}/file/{paper_hash}-Metadata.json"


def fetch_metadata_json(url: str) -> dict:
    r = requests.get(url, timeout=60)
    if not r.ok:
        return {}
    try:
        return r.json()
    except ValueError:
        return {}


def authors_from_json(payload: dict) -> list[str]:
    authors: list[str] = []
    for author in payload.get("authors") or []:
        given = str(author.get("given_name") or "").strip()
        family = str(author.get("family_name") or "").strip()
        name = f"{given} {family}".strip() if given else family
        if name:
            authors.append(name)
    return authors


def abstract_from_full_text(text: str) -> str:
    """Extract the leading abstract paragraph from NeurIPS full_text."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    m = re.search(r"\bAbstract\s*\n+", text, flags=re.I)
    if not m:
        return ""
    tail = text[m.end():]
    end_positions = []
    for pat in (
        r"\n\s*1(?:\.|\s)+(?:Introduction|Overview)\b",
        r"\n\s*Introduction\s*\n",
        r"\n\s*1\s+[A-Z][^\n]{0,80}\n",
    ):
        match = re.search(pat, tail)
        if match:
            end_positions.append(match.start())
    end = min(end_positions) if end_positions else min(len(tail), 1800)
    abstract = tail[:end].replace("\f", " ")
    return re.sub(r"\s+", " ", abstract).strip()


def fetch_neurips_fields(year: str, paper_hash: str) -> dict:
    meta_url = metadata_url(year, paper_hash)
    abs_url = abstract_url(year, paper_hash)
    paper_url = pdf_url(year, paper_hash)

    payload = fetch_metadata_json(meta_url)
    html = ""

    title = clean_text(str(payload.get("title") or ""))
    authors = authors_from_json(payload)
    abstract = clean_text(str(payload.get("abstract") or ""))
    source = clean_text(str(payload.get("book") or ""))

    if not abstract:
        abstract = abstract_from_full_text(str(payload.get("full_text") or ""))

    if not title or not authors or not abstract or not source:
        html = fetch_page_html(abs_url)
        title = title or first_meta(html, "citation_title") or first_element_text(html, "h1", "paper-title")
        authors = authors or meta_contents(html, "citation_author")
        if not authors:
            authors_raw = first_element_text(html, "p", "paper-authors")
            authors = [a.strip() for a in authors_raw.split(",") if a.strip()]
        abstract = abstract or first_element_text(html, "p", "paper-abstract")
        source = source or first_meta(html, "citation_journal_title") or "Advances in Neural Information Processing Systems"

    if not title or not authors:
        raise ValueError(f"Incomplete NeurIPS metadata for {paper_hash}")

    return {
        "title": title,
        "authors": authors,
        "year": int(year),
        "source": source or "Advances in Neural Information Processing Systems",
        "type": "Conference Paper",
        "abstract": abstract,
        "link": paper_url,
        "links_alt": [abs_url, meta_url],
    }


class NeuripsPrefill(PagePrefillScript[tuple[str, str]]):
    description = "Prefill metadata from NeurIPS/NIPS URLs."
    default_input = DEFAULT_INPUT
    entry_kind = "NeurIPS papers"

    def extract_entries(self, path: Path) -> list[tuple[str, str]]:
        return extract_entries(path)

    def entry_label(self, entry: tuple[str, str]) -> str:
        year, paper_hash = entry
        return f"{year}/{paper_hash}"

    def fetch_fields(self, entry: tuple[str, str], _context: dict) -> dict:
        year, paper_hash = entry
        return fetch_neurips_fields(year, paper_hash)

    def skipped_list_message(
        self,
        entry: tuple[str, str],
        _fields: dict | None,
        existing: Path,
    ) -> str:
        _year, paper_hash = entry
        return f"{paper_hash}  {existing}"


def main() -> None:
    NeuripsPrefill().run()


if __name__ == "__main__":
    main()
