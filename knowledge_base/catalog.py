"""Canonical in-process catalog of metadata-backed papers."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import hashlib
import re
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import quote

import yaml

from knowledge_base.utils.arxiv_utils import normalize_arxiv_id
from knowledge_base.utils.paper_ids import paper_id_from_metadata


YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def clean_scalar(value: Any) -> str:
    return str(value or "").strip()


def clean_inline(value: Any) -> str:
    return re.sub(r"[ \t\r\f\v]+", " ", clean_scalar(value))


def as_clean_tuple(value: Any) -> tuple[str, ...]:
    if isinstance(value, list):
        return tuple(text for item in value if (text := clean_scalar(item)))
    text = clean_scalar(value)
    return (text,) if text else ()


def year_as_int(value: Any) -> int | None:
    if isinstance(value, int):
        year = value
    else:
        match = re.search(r"\b([12][0-9]{3})\b", clean_scalar(value))
        if not match:
            return None
        year = int(match.group(1))

    if 1500 <= year <= date.today().year + 5:
        return year
    return None


def last_name(author: str) -> str:
    author = clean_inline(author)
    if "," in author:
        return author.split(",", 1)[0].strip()
    parts = author.split()
    return parts[-1] if parts else author


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def clean_doi(doi: Any) -> str:
    return re.sub(
        r"^https?://(?:dx\.)?doi\.org/",
        "",
        clean_scalar(doi),
        flags=re.IGNORECASE,
    )


def join_url(base_path: str, target: str) -> str:
    base = clean_scalar(base_path).rstrip("/")
    path = target.lstrip("/")
    return f"{base}/{path}" if base else path


@dataclass(frozen=True)
class Entry:
    metadata_path: Path
    id: str
    generated_path: Path
    generated_source: str
    title: str
    algorithm: str
    authors: tuple[str, ...]
    author_last_names: tuple[str, ...]
    year: Any
    year_text: str
    year_value: int | None
    source: str
    type: str
    doi: str
    arxiv_id: str
    tags: tuple[str, ...]
    abstract: str
    summary: str
    primary_link: str
    has_primary_link: bool
    alternate_links: tuple[str, ...]
    alternate_link_count: int
    audit_status: str
    identifiers: tuple[str, ...]
    label: str
    title_label: str
    author_short: str
    byline: str
    detail_path: str
    tree_path: str
    map_path: str
    timeline_path: str
    search_path: str
    embedding_text: str
    embedding_hash: str

    @classmethod
    def from_metadata(
        cls,
        metadata_path: Path,
        data: dict[str, Any],
        *,
        metadata_root: Path,
        generated_root: Path = Path("papers"),
    ) -> Entry:
        paper_id = paper_id_from_metadata(metadata_path, data, metadata_root)
        generated_path = generated_root / f"{paper_id}.md"
        generated_source = generated_path.as_posix()
        title = clean_scalar(data.get("title"))
        algorithm = clean_scalar(data.get("algorithm"))
        authors = as_clean_tuple(data.get("authors"))
        author_last_names = tuple(last_name(author) for author in authors)
        year = data.get("year") or ""
        year_text = clean_scalar(year)
        year_value = year_as_int(year)
        source = clean_scalar(data.get("source"))
        item_type = clean_scalar(data.get("type"))
        doi = clean_doi(data.get("doi"))
        arxiv_id = normalize_arxiv_id(data.get("arxiv_id"))
        tags = as_clean_tuple(data.get("tags"))
        abstract = clean_scalar(data.get("abstract"))
        summary = clean_scalar(data.get("summary"))
        primary_link = clean_scalar(data.get("link"))
        alternate_links = as_clean_tuple(data.get("links_alt"))
        audit_status = clean_scalar(data.get("audit_status"))
        identifiers = identifier_terms(
            paper_id,
            doi=doi,
            arxiv_id=arxiv_id,
            primary_link=primary_link,
            alternate_links=alternate_links,
        )
        label = paper_label(
            title=title,
            algorithm=algorithm,
            authors=authors,
            year=year,
        )
        title_label = algorithm or title or paper_id
        author_short = ", ".join(author_last_names[:3])
        byline_author = authors[0] + (" et al." if len(authors) > 1 else "") if authors else ""
        byline = " / ".join(part for part in (byline_author, year_text) if part)
        quoted_id = quote(paper_id, safe="")
        detail_path = f"papers/{quoted_id}/"
        tree_path = f"tree/#paper={quoted_id}"
        map_path = f"map/#paper={quoted_id}"
        timeline_path = f"timeline/#paper={quoted_id}"
        search_path = f"search/?paper={quoted_id}"
        embedding_text = build_embedding_text(
            title=title,
            tags=tags,
            summary=summary,
            abstract=abstract,
        )
        return cls(
            metadata_path=metadata_path,
            id=paper_id,
            generated_path=generated_path,
            generated_source=generated_source,
            title=title,
            algorithm=algorithm,
            authors=authors,
            author_last_names=author_last_names,
            year=year,
            year_text=year_text,
            year_value=year_value,
            source=source,
            type=item_type,
            doi=doi,
            arxiv_id=arxiv_id,
            tags=tags,
            abstract=abstract,
            summary=summary,
            primary_link=primary_link,
            has_primary_link=bool(primary_link),
            alternate_links=alternate_links,
            alternate_link_count=len(alternate_links),
            audit_status=audit_status,
            identifiers=identifiers,
            label=label,
            title_label=title_label,
            author_short=author_short,
            byline=byline,
            detail_path=detail_path,
            tree_path=tree_path,
            map_path=map_path,
            timeline_path=timeline_path,
            search_path=search_path,
            embedding_text=embedding_text,
            embedding_hash=content_hash(embedding_text),
        )

    def url(self, key: str, base_path: str = "..") -> str:
        paths = {
            "detail": self.detail_path,
            "tree": self.tree_path,
            "map": self.map_path,
            "timeline": self.timeline_path,
            "search": self.search_path,
        }
        return join_url(base_path, paths[key])


@dataclass(frozen=True)
class Catalog:
    entries: tuple[Entry, ...]
    by_id: dict[str, Entry]
    by_metadata_path: dict[Path, Entry]
    by_generated_path: dict[Path, Entry]

    @classmethod
    def from_metadata_root(
        cls,
        metadata_root: Path = Path("docs/papers"),
        *,
        generated_root: Path = Path("papers"),
    ) -> Catalog:
        entries: list[Entry] = []
        for metadata_path in sorted(metadata_root.rglob("metadata.yml")):
            with metadata_path.open("r", encoding="utf-8") as f:
                data = yaml.load(f, Loader=YAML_LOADER) or {}
            if not isinstance(data, dict):
                continue
            entries.append(
                Entry.from_metadata(
                    metadata_path,
                    data,
                    metadata_root=metadata_root,
                    generated_root=generated_root,
                )
            )
        return cls.from_entries(entries)

    @classmethod
    def from_entries(cls, entries: Iterable[Entry]) -> Catalog:
        ordered = tuple(entries)
        return cls(
            entries=ordered,
            by_id=unique_index(ordered, "id"),
            by_metadata_path=unique_index(ordered, "metadata_path"),
            by_generated_path=unique_index(ordered, "generated_path"),
        )


def unique_index(entries: tuple[Entry, ...], field_name: str) -> dict[Any, Entry]:
    index: dict[Any, Entry] = {}
    for entry in entries:
        key = getattr(entry, field_name)
        if key in index:
            raise ValueError(f"Duplicate Catalog {field_name}: {key}")
        index[key] = entry
    return index


def paper_label(
    *,
    title: str,
    algorithm: str,
    authors: tuple[str, ...],
    year: Any,
) -> str:
    if algorithm:
        return algorithm
    if authors:
        suffix = " et al." if len(authors) > 1 else ""
        year_suffix = f" {year}" if clean_scalar(year) else ""
        return f"{last_name(authors[0])}{suffix}{year_suffix}"
    return title or "Untitled"


def build_embedding_text(
    *,
    title: str,
    tags: tuple[str, ...],
    summary: str,
    abstract: str,
) -> str:
    parts = [
        f"Title: {title}",
        f"Tags: {', '.join(tags)}",
        f"Summary: {summary}",
    ]
    if abstract:
        parts.append(f"Abstract: {abstract}")
    return "\n".join(part for part in parts if part.split(": ", 1)[-1].strip())


def identifier_terms(
    paper_id: str,
    *,
    doi: str,
    arxiv_id: str,
    primary_link: str,
    alternate_links: tuple[str, ...],
) -> tuple[str, ...]:
    terms = [
        paper_id,
        doi,
        f"DOI:{doi}" if doi else "",
        f"DOI {doi}" if doi else "",
        f"https://doi.org/{doi}" if doi else "",
        arxiv_id,
        f"arXiv:{arxiv_id}" if arxiv_id else "",
        f"arXiv {arxiv_id}" if arxiv_id else "",
        f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else "",
        f"https://arxiv.org/pdf/{arxiv_id}" if arxiv_id else "",
        f"https://arxiv.org/html/{arxiv_id}" if arxiv_id else "",
        primary_link,
        *alternate_links,
    ]
    return tuple(dict.fromkeys(term for term in terms if term))
