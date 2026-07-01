"""arXiv Atom API parsing and fetching."""

from __future__ import annotations

import xml.etree.ElementTree as ET

from knowledge_base.scripts.enrich_existing_arxiv_metadata.text import bare_arxiv_id
from knowledge_base.utils.arxiv_utils import ArxivRecord, arxiv_atom_entry_record, fetch_arxiv_records_many


def parse_entry(entry: ET.Element, requested_id: str) -> ArxivRecord:
    return arxiv_atom_entry_record(entry, requested_id)


def fetch_batch(ids: list[str]) -> dict[str, ArxivRecord]:
    return {bare_arxiv_id(record.arxiv_id): record for record in fetch_arxiv_records_many(ids, timeout=90).values()}
