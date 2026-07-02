"""Refine staged metadata files."""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any

import yaml

from knowledge_base.scripts.enrich_existing_arxiv_metadata.yaml_io import dump_yaml
from knowledge_base.scripts.refine_staged_arxiv_metadata.constants import ARXIV_DOI_RE, ARXIV_URL_RE
from knowledge_base.scripts.refine_staged_arxiv_metadata.sources import (
    clean_links,
    crossref_for_doi,
    crossref_type_to_metadata,
    official_links_from_crossref,
    official_links_from_openalex,
    official_location,
    openalex_for_title,
    openalex_type_to_metadata,
)
from knowledge_base.scripts.refine_staged_arxiv_metadata.tags import phrase_tags
from knowledge_base.scripts.refine_staged_arxiv_metadata.text import bare_arxiv_id


def staged_metadata_files() -> list[Path]:
    output = subprocess.check_output(
        ["git", "diff", "--cached", "--name-only", "--", "knowledge_base/docs/papers/**/metadata.yml"],
        text=True,
    )
    return [Path(line) for line in output.splitlines() if line.strip()]


def refine(path: Path, cache: dict[str, Any]) -> bool:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    before = dump_yaml(data)

    arxiv_id = bare_arxiv_id(data.get("arxiv_id"))
    data["arxiv_id"] = arxiv_id or None
    if arxiv_id and ARXIV_URL_RE.search(str(data.get("link") or "")):
        data["link"] = f"https://arxiv.org/pdf/{arxiv_id}"
    data["links_alt"] = clean_links(list(data.get("links_alt") or []))

    title = data.get("title") or ""
    abstract = data.get("abstract") or ""
    doi = data.get("doi") or ""
    official_source = ""
    official_type = ""
    official_links: list[str] = []

    crossref = crossref_for_doi(cache, doi)
    if crossref:
        official_source, official_type = crossref_type_to_metadata(crossref)
        official_links = official_links_from_crossref(crossref)
        official_doi = crossref.get("DOI")
        if official_doi and not ARXIV_DOI_RE.search(official_doi):
            data["doi"] = official_doi

    openalex = openalex_for_title(cache, title)
    if not official_source:
        location: dict[str, Any] = official_location(openalex) if openalex else {}
        if location:
            official_source, official_type = openalex_type_to_metadata(openalex, location)
            official_links = official_links_from_openalex(openalex, location)
            official_doi = (openalex.get("doi") or "").replace("https://doi.org/", "")
            if official_doi and not ARXIV_DOI_RE.search(official_doi):
                data["doi"] = official_doi

    if official_source and official_type:
        data["source"] = official_source
        data["type"] = official_type
    elif not data.get("source"):
        data["source"] = "arXiv"
        data["type"] = "Preprint"

    tags = phrase_tags(title, abstract, data.get("algorithm"), openalex)
    data["tags"] = tags or list(data.get("tags") or [])

    links = list(data.get("links_alt") or [])
    for link in official_links:
        if link not in links:
            links.append(link)
    data["links_alt"] = clean_links(links)
    data["audit_status"] = "raw"

    after = dump_yaml(data)
    if after != before:
        path.write_text(after, encoding="utf-8")
        return True
    return False
