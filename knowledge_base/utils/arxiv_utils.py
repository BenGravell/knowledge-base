import os
import re
import xml.etree.ElementTree as ET
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import quote, unquote, urlparse

import requests
import yaml

from knowledge_base.config import AUDIT_STATUS_FIELD, DEFAULT_AUDIT_STATUS

PAPERS_DIR = Path("docs/papers")
ARXIV_API = "https://export.arxiv.org/api/query"
ARXIV_NS = "http://www.w3.org/2005/Atom"
ARXIV_SCHEMA_NS = "http://arxiv.org/schemas/atom"
ARXIV_OAI_API = "https://oaipmh.arxiv.org/oai"
OAI_NS = "http://www.openarchives.org/OAI/2.0/"
OAI_ARXIV_NS = "http://arxiv.org/OAI/arXiv/"
_ARXIV_NEW_RE = re.compile(r"^(?P<yy>\d{2})(?P<mm>\d{2})\.\d{4,5}(?:[vV]\d+)?$")
_ARXIV_OLD_RE = re.compile(r"^[A-Za-z][A-Za-z0-9-]*(?:\.[A-Z]{2})?/" r"(?P<yy>\d{2})(?P<mm>\d{2})\d{3}(?:[vV]\d+)?$")
# arXiv asks automated clients to identify themselves and stay contactable.
# https://info.arxiv.org/help/api/tou.html
ARXIV_CONTACT_EMAIL = os.environ.get("ARXIV_CONTACT_EMAIL", "bjgravell@gmail.com").strip()
ARXIV_HEADERS = {
    "Accept": "application/atom+xml, application/xml;q=0.9, */*;q=0.8",
    "From": ARXIV_CONTACT_EMAIL,
    "User-Agent": (f"knowledge-base-prefill/1.0 ({ARXIV_CONTACT_EMAIL}; https://github.com/bjgravell/knowledge-base)"),
}


@dataclass
class ArxivRecord:
    arxiv_id: str
    title: str
    authors: list[str]
    year: int
    abstract: str
    doi: str = ""
    journal_ref: str = ""
    comment: str = ""
    primary_category: str = ""
    categories: list[str] = field(default_factory=list)


def normalize_arxiv_id(arxiv_id: str | None) -> str:
    """Return a bare arXiv ID from an ID, arXiv URL, or ``arXiv:`` token."""
    text = str(arxiv_id or "").strip()
    text = re.sub(r"^arxiv:\s*", "", text, flags=re.IGNORECASE).strip()
    if not text:
        return ""

    parsed = urlparse(text)
    host = parsed.netloc.lower().removeprefix("www.")
    if parsed.scheme and host:
        parts = [unquote(part) for part in parsed.path.strip("/").split("/") if part]
        if host == "arxiv.org" and parts[:1] and parts[0].lower() in {"abs", "pdf", "html"}:
            parts = parts[1:]
            if len(parts) > 1 and parts[-1].lower() == "pdf":
                parts = parts[:-1]
            text = "/".join(parts)
        elif host == "ar5iv.labs.arxiv.org" and parts[:1] and parts[0].lower() == "html":
            text = "/".join(parts[1:])
        else:
            text = parsed.path.strip("/")

    text = text.strip().strip("<>()[]").rstrip("/")
    if text.lower().endswith("/pdf"):
        candidate = text[:-4].rstrip("/")
        if _ARXIV_NEW_RE.match(candidate) or _ARXIV_OLD_RE.match(candidate):
            text = candidate
    if text.lower().endswith(".pdf"):
        text = text[:-4]
    if _ARXIV_NEW_RE.match(text) or _ARXIV_OLD_RE.match(text):
        text = re.sub(r"[vV]\d+$", "", text)
    return text


def arxiv_year_from_id(arxiv_id: str | None) -> int:
    """Infer publication year from new- or old-style arXiv IDs when possible."""
    arxiv_id = normalize_arxiv_id(arxiv_id)
    match = _ARXIV_NEW_RE.match(arxiv_id) or _ARXIV_OLD_RE.match(arxiv_id)
    if not match:
        return 0

    yy = int(match.group("yy"))
    mm = int(match.group("mm"))
    if not 1 <= mm <= 12:
        return 0
    return 1900 + yy if yy >= 91 else 2000 + yy


def arxiv_abs_url(arxiv_id: str | None) -> str:
    encoded = quote(normalize_arxiv_id(arxiv_id), safe="/")
    return f"https://arxiv.org/abs/{encoded}"


def arxiv_pdf_url(arxiv_id: str | None) -> str:
    encoded = quote(normalize_arxiv_id(arxiv_id), safe="/")
    return f"https://arxiv.org/pdf/{encoded}"


def arxiv_html_url(arxiv_id: str | None) -> str:
    encoded = quote(normalize_arxiv_id(arxiv_id), safe="/")
    return f"https://ar5iv.labs.arxiv.org/html/{encoded}"


def _clean_space(text: str | None) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def _entry_text(entry: ET.Element, ns: str, tag: str) -> str:
    el = entry.find(f"{{{ns}}}{tag}")
    return _clean_space(el.text if el is not None else "")


def arxiv_record_to_fields(record: ArxivRecord) -> dict[str, Any]:
    fields: dict[str, Any] = {
        "title": record.title,
        "authors": record.authors,
        "year": record.year,
        "abstract": record.abstract,
        "arxiv_id": record.arxiv_id,
        "link": arxiv_pdf_url(record.arxiv_id),
    }
    if record.doi:
        fields["doi"] = record.doi
    return fields


def arxiv_atom_entry_record(entry: ET.Element, fallback_id: str = "") -> ArxivRecord:
    def atom_text(tag: str) -> str:
        return _entry_text(entry, ARXIV_NS, tag)

    def arxiv_text(tag: str) -> str:
        return _entry_text(entry, ARXIV_SCHEMA_NS, tag)

    arxiv_id = normalize_arxiv_id(atom_text("id")) or normalize_arxiv_id(fallback_id)
    published = atom_text("published")
    primary_el = entry.find(f"{{{ARXIV_SCHEMA_NS}}}primary_category")
    primary_category = primary_el.attrib.get("term", "") if primary_el is not None else ""
    categories = [
        category.attrib.get("term", "")
        for category in entry.findall(f"{{{ARXIV_NS}}}category")
        if category.attrib.get("term")
    ]
    if primary_category and primary_category not in categories:
        categories.insert(0, primary_category)

    return ArxivRecord(
        arxiv_id=arxiv_id,
        title=atom_text("title"),
        authors=[
            _clean_space(name.text)
            for author in entry.findall(f"{{{ARXIV_NS}}}author")
            if (name := author.find(f"{{{ARXIV_NS}}}name")) is not None and name.text
        ],
        year=int(published[:4]) if published else arxiv_year_from_id(arxiv_id),
        abstract=atom_text("summary"),
        doi=arxiv_text("doi"),
        journal_ref=arxiv_text("journal_ref"),
        comment=arxiv_text("comment"),
        primary_category=primary_category,
        categories=categories,
    )


def _entry_fields(entry: ET.Element, fallback_id: str = "") -> dict[str, Any]:
    return arxiv_record_to_fields(arxiv_atom_entry_record(entry, fallback_id))


def parse_arxiv_feed_records(feed_xml: str, fallback_id: str = "") -> dict[str, ArxivRecord]:
    root = ET.fromstring(feed_xml)
    records: dict[str, ArxivRecord] = {}
    for entry in root.findall(f"{{{ARXIV_NS}}}entry"):
        record = arxiv_atom_entry_record(entry, fallback_id)
        arxiv_id = normalize_arxiv_id(record.arxiv_id)
        if arxiv_id:
            records[arxiv_id] = record
    return records


def _parse_arxiv_feed(feed_xml: str, fallback_id: str = "") -> dict[str, dict[str, Any]]:
    return {
        arxiv_id: arxiv_record_to_fields(record)
        for arxiv_id, record in parse_arxiv_feed_records(feed_xml, fallback_id).items()
    }


def _element_text(element: ET.Element | None, ns: str, tag: str) -> str:
    if element is None:
        return ""
    child = element.find(f"{{{ns}}}{tag}")
    return _clean_space(child.text if child is not None else "")


def _parse_oai_author(author: ET.Element) -> str:
    forenames = _element_text(author, OAI_ARXIV_NS, "forenames")
    keyname = _element_text(author, OAI_ARXIV_NS, "keyname")
    suffix = _element_text(author, OAI_ARXIV_NS, "suffix")
    return " ".join(part for part in (forenames, keyname, suffix) if part).strip()


def parse_arxiv_oai_record(record_xml: str, fallback_id: str = "") -> ArxivRecord:
    root = ET.fromstring(record_xml)
    error = root.find(f"{{{OAI_NS}}}error")
    if error is not None:
        code = error.attrib.get("code", "unknown")
        message = error.text.strip() if error.text else "No OAI-PMH record returned"
        raise ValueError(f"arXiv OAI error {code}: {message}")

    record = root.find(f".//{{{OAI_NS}}}record")
    metadata = record.find(f"{{{OAI_NS}}}metadata") if record is not None else None
    entry = metadata.find(f"{{{OAI_ARXIV_NS}}}arXiv") if metadata is not None else None
    if entry is None:
        raise ValueError(f"No OAI-PMH entry found for arXiv ID '{fallback_id}'")

    arxiv_id = normalize_arxiv_id(_element_text(entry, OAI_ARXIV_NS, "id")) or normalize_arxiv_id(fallback_id)
    created = _element_text(entry, OAI_ARXIV_NS, "created")
    year_match = re.search(r"\b(?:19|20)\d{2}\b", created)
    id_year = arxiv_year_from_id(arxiv_id)
    return ArxivRecord(
        arxiv_id=arxiv_id,
        title=_element_text(entry, OAI_ARXIV_NS, "title"),
        authors=[
            author
            for author in (_parse_oai_author(author_el) for author_el in entry.findall(f".//{{{OAI_ARXIV_NS}}}author"))
            if author
        ],
        year=id_year or (int(year_match.group(0)) if year_match else 0),
        abstract=_element_text(entry, OAI_ARXIV_NS, "abstract"),
        doi=_element_text(entry, OAI_ARXIV_NS, "doi"),
        categories=[],
    )


def _parse_arxiv_oai_record(record_xml: str, fallback_id: str = "") -> dict[str, Any]:
    return arxiv_record_to_fields(parse_arxiv_oai_record(record_xml, fallback_id))


def fetch_arxiv_oai_record(arxiv_id: str) -> ArxivRecord:
    """Fetch metadata for one arXiv ID from arXiv's OAI-PMH endpoint."""
    arxiv_id = normalize_arxiv_id(arxiv_id)
    r = requests.get(
        ARXIV_OAI_API,
        params={
            "verb": "GetRecord",
            "identifier": f"oai:arXiv.org:{arxiv_id}",
            "metadataPrefix": "arXiv",
        },
        headers=ARXIV_HEADERS,
        timeout=60,
    )
    r.raise_for_status()
    return parse_arxiv_oai_record(r.text, fallback_id=arxiv_id)


def fetch_arxiv_oai(arxiv_id: str) -> dict[str, Any]:
    """Fetch metadata for one arXiv ID from arXiv's OAI-PMH endpoint."""
    return arxiv_record_to_fields(fetch_arxiv_oai_record(arxiv_id))


def fetch_arxiv_records_many(arxiv_ids: Iterable[str], *, timeout: int = 60) -> dict[str, ArxivRecord]:
    """Fetch parsed arXiv records for several IDs in one Atom API request."""
    ids = [normalize_arxiv_id(arxiv_id) for arxiv_id in arxiv_ids]
    ids = list(dict.fromkeys(arxiv_id for arxiv_id in ids if arxiv_id))
    if not ids:
        return {}

    r = requests.get(
        ARXIV_API,
        params={"id_list": ",".join(ids), "max_results": len(ids)},
        headers=ARXIV_HEADERS,
        timeout=timeout,
    )
    r.raise_for_status()
    return parse_arxiv_feed_records(r.text)


def fetch_arxiv_many(arxiv_ids: Iterable[str]) -> dict[str, dict[str, Any]]:
    """Fetch basic metadata for several arXiv IDs in one Atom API request."""
    return {
        arxiv_id: arxiv_record_to_fields(record) for arxiv_id, record in fetch_arxiv_records_many(arxiv_ids).items()
    }


def fetch_arxiv_record(arxiv_id: str) -> ArxivRecord:
    """Fetch one parsed arXiv Atom record."""
    arxiv_id = normalize_arxiv_id(arxiv_id)
    records = fetch_arxiv_records_many([arxiv_id])
    if arxiv_id not in records:
        raise ValueError(f"No entry found for arXiv ID '{arxiv_id}'")
    return records[arxiv_id]


def fetch_arxiv(arxiv_id: str) -> dict[str, Any]:
    """Fetch basic metadata from the arXiv Atom API and return a dict."""
    return arxiv_record_to_fields(fetch_arxiv_record(arxiv_id))


def build_metadata(fields: dict[str, Any]) -> dict[str, Any]:
    """Return an ordered dict ready to serialise as YAML."""
    tags_raw: str = fields.get("tags_raw", "")
    tags = [t.strip() for t in tags_raw.splitlines() if t.strip()]

    links_alt_raw: str = fields.get("links_alt_raw", "")
    links_alt = [ln.strip() for ln in links_alt_raw.splitlines() if ln.strip()]
    arxiv_id = normalize_arxiv_id(fields.get("arxiv_id"))

    return {
        "title": fields["title"],
        "algorithm": fields.get("algorithm") or None,
        "authors": fields["authors"],
        "year": fields["year"],
        "source": fields.get("source") or None,
        "type": fields.get("type", ""),
        "doi": fields.get("doi") or None,
        "arxiv_id": arxiv_id or None,
        "tags": tags,
        "abstract": fields.get("abstract", ""),
        "summary": fields.get("summary", ""),
        "link": fields.get("link", ""),
        "links_alt": links_alt,
        AUDIT_STATUS_FIELD: DEFAULT_AUDIT_STATUS,
    }


def metadata_to_yaml(metadata: dict[str, Any]) -> str:
    """Serialise metadata to a YAML string matching the project style."""
    lines: list[str] = []

    def add(key: str, value: Any) -> None:
        if value is None:
            lines.append(f"{key}:")
        elif isinstance(value, list):
            lines.append(f"{key}:")
            lines.extend(f"  - {item}" for item in value)
        elif key == "arxiv_id":
            lines.append(f'{key}: "{value}"')
        elif isinstance(value, str) and len(value) > 80:
            lines.append(f"{key}: >")
            lines.append(f"  {value}")
        else:
            lines.append(yaml.dump({key: value}, default_flow_style=False).rstrip())

    for key, val in metadata.items():
        add(key, val)

    return "\n".join(lines) + "\n"


def target_path(arxiv_id: str, year: int) -> Path:
    arxiv_id = normalize_arxiv_id(arxiv_id)
    return PAPERS_DIR / str(year) / arxiv_id / "metadata.yml"


def write_metadata(arxiv_id: str, year: int, yaml_text: str) -> Path:
    """Write yaml_text to the canonical metadata.yml path, creating dirs as needed."""
    path = target_path(arxiv_id, year)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml_text, encoding="utf-8")
    return path
