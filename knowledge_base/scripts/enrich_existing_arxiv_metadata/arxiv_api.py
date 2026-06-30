"""arXiv Atom API parsing and fetching."""

from __future__ import annotations

import xml.etree.ElementTree as ET

import requests

from knowledge_base.scripts.enrich_existing_arxiv_metadata.constants import ARXIV_SCHEMA_NS
from knowledge_base.scripts.enrich_existing_arxiv_metadata.model import ArxivRecord
from knowledge_base.scripts.enrich_existing_arxiv_metadata.text import bare_arxiv_id, clean_space
from knowledge_base.utils.arxiv_utils import ARXIV_API, ARXIV_HEADERS, ARXIV_NS, normalize_arxiv_id


def parse_entry(entry: ET.Element, requested_id: str) -> ArxivRecord:
    def atom_text(tag: str) -> str:
        el = entry.find(f"{{{ARXIV_NS}}}{tag}")
        return clean_space(el.text if el is not None else "")

    def arxiv_text(tag: str) -> str:
        el = entry.find(f"{{{ARXIV_SCHEMA_NS}}}{tag}")
        return clean_space(el.text if el is not None else "")

    arxiv_id = requested_id
    id_url = atom_text("id")
    if id_url:
        arxiv_id = normalize_arxiv_id(id_url)

    authors: list[str] = []
    for author in entry.findall(f"{{{ARXIV_NS}}}author"):
        name = author.find(f"{{{ARXIV_NS}}}name")
        if name is not None and name.text:
            authors.append(clean_space(name.text))

    published = atom_text("published")
    primary_el = entry.find(f"{{{ARXIV_SCHEMA_NS}}}primary_category")
    primary_category = primary_el.attrib.get("term", "") if primary_el is not None else ""
    categories = [
        cat.attrib.get("term", "") for cat in entry.findall(f"{{{ARXIV_NS}}}category") if cat.attrib.get("term")
    ]
    if primary_category and primary_category not in categories:
        categories.insert(0, primary_category)

    return ArxivRecord(
        arxiv_id=arxiv_id,
        title=atom_text("title"),
        authors=authors,
        year=int(published[:4]) if published else 0,
        abstract=atom_text("summary"),
        doi=arxiv_text("doi"),
        journal_ref=arxiv_text("journal_ref"),
        comment=arxiv_text("comment"),
        primary_category=primary_category,
        categories=categories,
    )


def fetch_batch(ids: list[str]) -> dict[str, ArxivRecord]:
    response = requests.get(
        ARXIV_API,
        params={"id_list": ",".join(ids), "max_results": len(ids)},
        headers=ARXIV_HEADERS,
        timeout=90,
    )
    response.raise_for_status()
    root = ET.fromstring(response.text)
    records: dict[str, ArxivRecord] = {}
    for entry in root.findall(f"{{{ARXIV_NS}}}entry"):
        record = parse_entry(entry, "")
        records[bare_arxiv_id(record.arxiv_id)] = record
    return records
