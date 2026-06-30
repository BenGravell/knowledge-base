"""Crossref/OpenAlex source and link helpers."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

from knowledge_base.scripts.refine_staged_arxiv_metadata.cache import fetch_json
from knowledge_base.scripts.refine_staged_arxiv_metadata.constants import ARXIV_DOI_RE, ARXIV_URL_RE
from knowledge_base.scripts.refine_staged_arxiv_metadata.text import clean_space, normalize_title, title_similarity


def crossref_for_doi(cache: dict[str, Any], doi: str) -> dict[str, Any]:
    if not doi or ARXIV_DOI_RE.search(doi):
        return {}
    url = f"https://api.crossref.org/works/{quote(doi, safe='')}"
    payload = fetch_json(cache, f"crossref:{doi.lower()}", url)
    return payload.get("message") or {}


def openalex_for_title(cache: dict[str, Any], title: str) -> dict[str, Any]:
    url = f"https://api.openalex.org/works?search={quote(title)}&per-page=5"
    payload = fetch_json(cache, f"openalex:title:{normalize_title(title)}", url)
    results = payload.get("results") or []
    best: dict[str, Any] = {}
    best_score = 0.0
    for result in results:
        score = title_similarity(title, result.get("title") or result.get("display_name") or "")
        if score > best_score:
            best = result
            best_score = score
    return best if best_score >= 0.94 else {}


def official_location(work: dict[str, Any]) -> dict[str, Any]:
    locations = [work.get("primary_location") or {}, *(work.get("locations") or [])]
    for location in locations:
        source = location.get("source") or {}
        source_name = (source.get("display_name") or location.get("raw_source_name") or "").lower()
        source_type = (source.get("type") or "").lower()
        if source_type == "repository" or "arxiv" in source_name:
            continue
        if location.get("is_published") or location.get("version") == "publishedVersion":
            return location
    for location in locations:
        source = location.get("source") or {}
        source_name = (source.get("display_name") or location.get("raw_source_name") or "").lower()
        source_type = (source.get("type") or "").lower()
        if source_type != "repository" and "arxiv" not in source_name:
            return location
    return {}


def crossref_type_to_metadata(work: dict[str, Any]) -> tuple[str, str]:
    container = next(iter(work.get("container-title") or []), "")
    work_type = work.get("type") or ""
    name = container.lower()
    if "workshop" in name:
        item_type = "Workshop Paper"
    elif work_type == "journal-article":
        item_type = "Journal Paper"
    elif work_type == "proceedings-article" or "proceedings" in name or "conference" in name:
        item_type = "Conference Paper"
    elif work_type == "posted-content":
        item_type = "Preprint"
    else:
        item_type = "Other"
    return clean_space(container), item_type


def openalex_type_to_metadata(work: dict[str, Any], location: dict[str, Any]) -> tuple[str, str]:
    source = location.get("source") or {}
    source_name = clean_space(source.get("display_name") or location.get("raw_source_name") or "")
    source_type = (source.get("type") or "").lower()
    raw_type = (location.get("raw_type") or work.get("type_crossref") or work.get("type") or "").lower()
    name = source_name.lower()
    if "workshop" in name:
        item_type = "Workshop Paper"
    elif source_type == "journal" or raw_type == "journal-article":
        item_type = "Journal Paper"
    elif source_type == "conference" or raw_type == "proceedings-article" or "proceedings" in name:
        item_type = "Conference Paper"
    else:
        item_type = "Other"
    return clean_space(source_name), item_type


def official_links_from_crossref(work: dict[str, Any]) -> list[str]:
    links = [work.get("URL") or ""]
    resource = (work.get("resource") or {}).get("primary") or {}
    links.append(resource.get("URL") or "")
    for link in work.get("link") or []:
        url = link.get("URL") or ""
        if url:
            links.append(url)
    return clean_links(links)


def official_links_from_openalex(work: dict[str, Any], location: dict[str, Any]) -> list[str]:
    links = []
    doi = (work.get("doi") or "").replace("https://doi.org/", "")
    if doi and not ARXIV_DOI_RE.search(doi):
        links.append(f"https://doi.org/{doi}")
    links.extend(
        candidate
        for candidate in (
            location.get("landing_page_url"),
            location.get("pdf_url"),
            (work.get("primary_location") or {}).get("landing_page_url"),
        )
        if candidate
    )
    return clean_links(links)


def clean_links(links: list[str]) -> list[str]:
    cleaned: list[str] = []
    for link in links:
        link = clean_space(link)
        if not link or ARXIV_URL_RE.search(link):
            continue
        if link not in cleaned:
            cleaned.append(link)
    return cleaned
