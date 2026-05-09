"""Batch-prefill metadata.yml files from OpenReview URLs."""

import re
from pathlib import Path
from urllib.parse import parse_qs, urlparse

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

import requests

from knowledge_base.utils.prefill_template import PagePrefillScript, REPO_ROOT
from knowledge_base.utils.prefill_utils import first_year, read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "OPENREVIEW.md"

_OPENREVIEW_API = "https://api2.openreview.net/notes?id={note_id}"
_OPENREVIEW_BASE = "https://openreview.net"


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


def extract_entries(path: Path) -> list[str]:
    seen: set[str] = set()
    entries: list[str] = []
    for url in read_url_lines(path):
        note_id = extract_note_id(url)
        if not note_id:
            print(f"  WARN: could not parse OpenReview note id from: {url!r}")
            continue
        if note_id not in seen:
            seen.add(note_id)
            entries.append(note_id)
    return entries


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
    r = requests.get(_OPENREVIEW_API.format(note_id=note_id), timeout=60)
    r.raise_for_status()
    notes = r.json().get("notes") or []
    if not notes:
        raise ValueError(f"No OpenReview note found for {note_id!r}")

    note = notes[0]
    content = note.get("content") or {}
    title = str(content_value(content, "title", "") or "")
    authors = list(content_value(content, "authors", []) or [])
    abstract = str(content_value(content, "abstract", "") or "")
    venue = str(content_value(content, "venue", "") or "")
    bibtex = str(content_value(content, "_bibtex", "") or "")
    year = first_year(bibtex, str(note.get("pdate") or ""), str(note.get("cdate") or ""))

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
        return extract_entries(path)

    def fetch_fields(self, entry: str, _context: dict) -> dict:
        return fetch_openreview_fields(entry)


def main() -> None:
    OpenReviewPrefill().run()


if __name__ == "__main__":
    main()
