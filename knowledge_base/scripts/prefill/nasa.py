"""Batch-prefill metadata.yml files from NASA NTRS URLs."""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

import requests

from knowledge_base.utils.prefill_template import PagePrefillScript, REPO_ROOT
from knowledge_base.utils.prefill_utils import first_year, read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "NASA.md"

_NTRS_ID_RE = re.compile(r"ntrs\.nasa\.gov/(?:api/)?citations/(\d+)", re.I)
_NTRS_API = "https://ntrs.nasa.gov/api/citations/{citation_id}"
_NTRS_PAGE = "https://ntrs.nasa.gov/citations/{citation_id}"
_NTRS_BASE = "https://ntrs.nasa.gov"
_HEADERS = {
    "Accept": "application/json",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 Chrome/124.0.0.0 Safari/537.36"
    ),
}


def display_name(name: str) -> str:
    if "," not in name:
        return name.strip()
    family, given = [part.strip() for part in name.split(",", 1)]
    return f"{given} {family}".strip()


def extract_entries(path: Path, on_parse_failure=None) -> list[str]:
    seen: set[str] = set()
    entries: list[str] = []
    for url in read_url_lines(path):
        match = _NTRS_ID_RE.search(url)
        if not match:
            message = f"could not parse NASA NTRS citation ID from: {url!r}"
            if on_parse_failure:
                on_parse_failure(message)
            else:
                print(f"  WARN: {message}")
            continue
        citation_id = match.group(1)
        if citation_id not in seen:
            seen.add(citation_id)
            entries.append(citation_id)
    return entries


def fetch_nasa_fields(citation_id: str) -> dict:
    r = requests.get(_NTRS_API.format(citation_id=citation_id), headers=_HEADERS, timeout=60)
    r.raise_for_status()
    data = r.json()

    authors: list[str] = []
    for item in data.get("authorAffiliations") or []:
        name = (((item.get("meta") or {}).get("author") or {}).get("name") or "").strip()
        if name:
            authors.append(display_name(name))

    publication_dates = [
        str(item.get("publicationDate") or "")
        for item in data.get("publications") or []
    ]
    year = first_year(*publication_dates, data.get("submittedDate", ""), data.get("distributionDate", ""))

    downloads = data.get("downloads") or []
    pdf_path = ""
    if downloads:
        links = downloads[0].get("links") or {}
        pdf_path = links.get("pdf") or links.get("original") or ""
    link = _NTRS_BASE + pdf_path if pdf_path.startswith("/") else pdf_path

    meetings = data.get("meetings") or []
    source = ""
    for meeting in meetings:
        if meeting.get("startDate") or meeting.get("endDate"):
            source = str(meeting.get("name") or "")
            break

    if not data.get("title") or not authors or not year:
        raise ValueError(f"Incomplete NASA NTRS metadata for {citation_id!r}")

    return {
        "title": data["title"],
        "authors": authors,
        "year": year,
        "source": source or "NASA Technical Reports Server",
        "type": "Technical Report",
        "abstract": data.get("abstract") or "",
        "link": link or _NTRS_PAGE.format(citation_id=citation_id),
        "links_alt": [
            _NTRS_PAGE.format(citation_id=citation_id),
            _NTRS_API.format(citation_id=citation_id),
        ],
    }


class NasaPrefill(PagePrefillScript[str]):
    description = "Prefill metadata from NASA NTRS URLs."
    default_input = DEFAULT_INPUT
    entry_kind = "NASA NTRS citations"

    def extract_entries(self, path: Path) -> list[str]:
        return extract_entries(path, self.record_parse_failure)

    def fetch_fields(self, entry: str, _context: dict) -> dict:
        return fetch_nasa_fields(entry)


def main() -> None:
    NasaPrefill().run()


if __name__ == "__main__":
    main()
