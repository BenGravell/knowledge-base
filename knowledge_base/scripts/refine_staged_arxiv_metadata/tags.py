"""Tag derivation for staged metadata refinement."""

from __future__ import annotations

import re
from typing import Any

from knowledge_base.scripts.refine_staged_arxiv_metadata.constants import GENERIC_OPENALEX_TAGS, PHRASE_TAGS
from knowledge_base.scripts.refine_staged_arxiv_metadata.text import clean_space, normalize_title, sentence_like_tag


def add_unique(items: list[str], item: str) -> None:
    item = clean_space(item)
    if item and item not in items:
        items.append(item)


def display_to_tag(display: str) -> str:
    display = re.sub(r"\s*\([^)]*\)", "", clean_space(display))
    return display[:1].upper() + display[1:] if display else ""


def openalex_literal_tags(work: dict[str, Any], title: str, abstract: str) -> list[str]:
    corpus = normalize_title(f"{title} {abstract}")
    tags: list[str] = []
    candidates = [keyword.get("display_name") or "" for keyword in work.get("keywords") or []]
    candidates.extend(topic.get("display_name") or "" for topic in work.get("topics") or [])
    primary_topic = work.get("primary_topic") or {}
    candidates.append(primary_topic.get("display_name") or "")

    for candidate in candidates:
        tag = display_to_tag(candidate)
        needle = normalize_title(tag)
        if not needle or needle in GENERIC_OPENALEX_TAGS:
            continue
        if len(needle.split()) < 2 and not re.fullmatch(r"[A-Z0-9+_.-]{2,}", tag):
            continue
        if needle in corpus:
            add_unique(tags, tag)
    return tags[:10]


def phrase_tags(title: str, abstract: str, algorithm: str | None, openalex: dict[str, Any] | None = None) -> list[str]:
    corpus = f"{title} {abstract}".lower()
    tags: list[str] = []
    for needle, tag in PHRASE_TAGS:
        if needle in corpus and tag not in tags:
            tags.append(tag)

    if algorithm and algorithm not in tags and re.search(rf"\b{re.escape(algorithm.lower())}\b", corpus):
        tags.append(algorithm)

    for long_name, acronym in re.findall(
        r"([A-Za-z][A-Za-z0-9+_. -]{3,80}?)\s*\(([A-Z][A-Z0-9+_.-]{1,16})\)", f"{title} {abstract}"
    ):
        long_name = clean_space(long_name).strip(" ,.;:")
        if 2 <= len(long_name.split()) <= 7 and not sentence_like_tag(long_name):
            tag = long_name[:1].upper() + long_name[1:]
            if tag not in tags:
                tags.append(tag)
        if acronym not in tags:
            tags.append(acronym)

    if openalex:
        for tag in openalex_literal_tags(openalex, title, abstract):
            add_unique(tags, tag)

    return tags[:20]
