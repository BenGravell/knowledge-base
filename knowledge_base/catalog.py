"""Canonical in-process catalog of metadata-backed papers."""

from __future__ import annotations

import hashlib
import re
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Literal
from urllib.parse import quote

import yaml
from pydantic import BaseModel, ConfigDict, ValidationError, field_validator

from knowledge_base.config import VALID_AUDIT_STATUSES, VALID_TYPES
from knowledge_base.utils.arxiv_utils import normalize_arxiv_id
from knowledge_base.utils.paper_ids import paper_id_from_metadata

YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
MetadataYear = int | str
UrlKey = Literal["detail", "tree", "map", "timeline", "search"]
EMBED_TEXT_SIDECAR = "embed_text.md"
LEGACY_FULL_TEXT_SIDECAR = "full_text.md"
# Loose storage safety valve; embedding backends may need chunking below this.
EMBED_TEXT_MAX_CHARS = 5_000_000

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
TAIL_HEADING_RE = re.compile(
    r"^(references|bibliography|acknowledg(?:e)?ments?|funding|appendix|supplementary)\b",
    re.IGNORECASE,
)
START_HEADING_RE = re.compile(r"^(introduction|abstract)\b", re.IGNORECASE)
NUMERIC_CITATION_RE = re.compile(r"\\?\[[\d,\s;:–—-]+\\?\]")
PAREN_NUMERIC_CITATION_RE = re.compile(r"\(\s*\d+(?:\s*[,;]\s*\d+)*\s*\)")
YEAR_CITATION_RE = re.compile(r"\([^()]{0,160}\b(?:19|20)\d{2}[a-z]?\b[^()]{0,160}\)")
COMPACT_CITATION_RE = re.compile(r"\b(?:[A-Z]{2,}|[A-Z][A-Za-z]+)[0-9]{2}[a-z]?\b")
LATEX_SPACE_RE = re.compile(r"\\hspace\{[^}]*\}")


def clean_scalar(value: Any) -> str:
    return str(value or "").strip()


def clean_inline(value: Any) -> str:
    return re.sub(r"[ \t\r\f\v]+", " ", clean_scalar(value))


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


def _clean_metadata_scalar(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, tuple, dict, set)):
        raise ValueError("expected a scalar value")
    return clean_scalar(value)


def _clean_metadata_tuple(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, (list, tuple)):
        items = value
    elif isinstance(value, (dict, set)):
        raise ValueError("expected a scalar value or list")
    else:
        items = (value,)

    cleaned: list[str] = []
    for item in items:
        if isinstance(item, (list, tuple, dict, set)):
            raise ValueError("expected scalar list entries")
        if text := clean_scalar(item):
            cleaned.append(text)
    return tuple(cleaned)


def _clean_metadata_year(value: Any) -> MetadataYear:
    if value is None:
        return ""
    if isinstance(value, (bool, list, tuple, dict, set)):
        raise ValueError("expected an integer year or year string")
    if isinstance(value, int):
        return value
    return clean_scalar(value)


class _MetadataRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    title: str = ""
    algorithm: str = ""
    authors: tuple[str, ...] = ()
    year: MetadataYear = ""
    source: str = ""
    type: str = ""
    doi: str = ""
    arxiv_id: str = ""
    tags: tuple[str, ...] = ()
    abstract: str = ""
    summary: str = ""
    link: str = ""
    links_alt: tuple[str, ...] = ()
    audit_status: str = ""

    @field_validator(
        "title",
        "algorithm",
        "source",
        "abstract",
        "summary",
        "link",
        mode="before",
    )
    @classmethod
    def clean_scalar_fields(cls, value: Any) -> str:
        return _clean_metadata_scalar(value)

    @field_validator("authors", "tags", "links_alt", mode="before")
    @classmethod
    def clean_tuple_fields(cls, value: Any) -> tuple[str, ...]:
        return _clean_metadata_tuple(value)

    @field_validator("year", mode="before")
    @classmethod
    def clean_year_field(cls, value: Any) -> MetadataYear:
        return _clean_metadata_year(value)

    @field_validator("doi", mode="before")
    @classmethod
    def clean_doi_field(cls, value: Any) -> str:
        return clean_doi(_clean_metadata_scalar(value))

    @field_validator("arxiv_id", mode="before")
    @classmethod
    def clean_arxiv_id_field(cls, value: Any) -> str:
        return normalize_arxiv_id(_clean_metadata_scalar(value))

    @field_validator("type", mode="before")
    @classmethod
    def clean_type_field(cls, value: Any) -> str:
        text = _clean_metadata_scalar(value)
        if text and text not in VALID_TYPES:
            raise ValueError(f"must be one of: {', '.join(VALID_TYPES)}")
        return text

    @field_validator("audit_status", mode="before")
    @classmethod
    def clean_audit_status_field(cls, value: Any) -> str:
        text = _clean_metadata_scalar(value)
        if text and text not in VALID_AUDIT_STATUSES:
            raise ValueError(f"must be one of: {', '.join(VALID_AUDIT_STATUSES)}")
        return text


@dataclass(frozen=True, slots=True)
class CatalogLoadIssue:
    metadata_path: Path
    message: str


class CatalogLoadError(ValueError):
    issues: tuple[CatalogLoadIssue, ...]

    def __init__(self, issues: Iterable[CatalogLoadIssue]) -> None:
        self.issues = tuple(issues)
        super().__init__(_format_catalog_load_issues(self.issues))

    @classmethod
    def from_validation_error(
        cls,
        metadata_path: Path,
        error: ValidationError,
    ) -> CatalogLoadError:
        return cls(CatalogLoadIssue(metadata_path, _validation_issue_message(issue)) for issue in error.errors())


def _validation_issue_message(issue: Any) -> str:
    location = ".".join(str(part) for part in issue.get("loc", ())) or "metadata"
    return f"{location}: {issue.get('msg', 'Invalid value')}"


def _format_catalog_load_issues(issues: tuple[CatalogLoadIssue, ...]) -> str:
    count = len(issues)
    header = f"Failed to load Catalog ({count} issue{'s' if count != 1 else ''})"
    lines = [header]
    lines.extend(f"- {issue.metadata_path}: {issue.message}" for issue in issues)
    return "\n".join(lines)


def _validate_metadata_record(metadata_path: Path, data: dict[str, Any]) -> _MetadataRecord:
    try:
        return _MetadataRecord.model_validate(data)
    except ValidationError as exc:
        raise CatalogLoadError.from_validation_error(metadata_path, exc) from exc


@dataclass(frozen=True, slots=True)
class Entry:
    metadata_path: Path
    id: str
    generated_path: Path
    generated_source: str
    title: str
    algorithm: str
    authors: tuple[str, ...]
    author_last_names: tuple[str, ...]
    year: MetadataYear
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
        record = _validate_metadata_record(metadata_path, data)
        paper_id = paper_id_from_metadata(metadata_path, data, metadata_root)
        generated_path = generated_root / f"{paper_id}.md"
        generated_source = generated_path.as_posix()
        title = record.title
        algorithm = record.algorithm
        authors = record.authors
        author_last_names = tuple(last_name(author) for author in authors)
        year = record.year
        year_text = clean_scalar(year)
        year_value = year_as_int(year)
        source = record.source
        item_type = record.type
        doi = record.doi
        arxiv_id = record.arxiv_id
        tags = record.tags
        abstract = record.abstract
        summary = record.summary
        primary_link = record.link
        alternate_links = record.links_alt
        audit_status = record.audit_status
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
            metadata_path=metadata_path,
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

    def url(self, key: UrlKey, base_path: str = "..") -> str:
        paths = {
            "detail": self.detail_path,
            "tree": self.tree_path,
            "map": self.map_path,
            "timeline": self.timeline_path,
            "search": self.search_path,
        }
        return join_url(base_path, paths[key])


@dataclass(frozen=True, slots=True)
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
        issues: list[CatalogLoadIssue] = []
        for metadata_path in sorted(metadata_root.rglob("metadata.yml")):
            try:
                with metadata_path.open("r", encoding="utf-8") as f:
                    data = yaml.load(f, Loader=YAML_LOADER) or {}
            except yaml.YAMLError as exc:
                issues.append(CatalogLoadIssue(metadata_path, str(exc)))
                continue
            if not isinstance(data, dict):
                issues.append(
                    CatalogLoadIssue(
                        metadata_path,
                        f"metadata.yml must contain a mapping, got {type(data).__name__}",
                    )
                )
                continue
            try:
                entries.append(
                    Entry.from_metadata(
                        metadata_path,
                        data,
                        metadata_root=metadata_root,
                        generated_root=generated_root,
                    )
                )
            except CatalogLoadError as exc:
                issues.extend(exc.issues)
        if issues:
            raise CatalogLoadError(issues)
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
            raise ValueError(
                f"Duplicate Catalog {field_name}: {key} ({index[key].metadata_path} and {entry.metadata_path})"
            )
        index[key] = entry
    return index


def paper_label(
    *,
    title: str,
    algorithm: str,
    authors: tuple[str, ...],
    year: MetadataYear,
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
    metadata_path: Path | None = None,
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
    content = embedding_sidecar_text(metadata_path) if metadata_path else ""
    if content:
        parts.append(f"Content: {content}")
    return "\n".join(part for part in parts if part.split(": ", 1)[-1].strip())


def embedding_sidecar_path(metadata_path: Path) -> Path | None:
    for name in (EMBED_TEXT_SIDECAR, LEGACY_FULL_TEXT_SIDECAR):
        path = metadata_path.with_name(name)
        if path.is_file():
            return path
    return None


def embedding_sidecar_text(metadata_path: Path) -> str:
    path = embedding_sidecar_path(metadata_path)
    if path is None:
        return ""
    return clean_embedding_sidecar_text(path.read_text(encoding="utf-8"))


def clean_embedding_sidecar_text(markdown: str) -> str:
    lines = drop_leading_author_blocks(strip_sidecar_header(markdown)).splitlines()
    start = content_start_index(lines)
    end = content_end_index(lines, start)
    text = "\n".join(clean_embedding_lines(lines[start:end]))
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if text and not any(line.startswith("#") for line in text.splitlines()):
        text = f"## Paper Body\n\n{text}"
    if len(text) > EMBED_TEXT_MAX_CHARS:
        text = text[:EMBED_TEXT_MAX_CHARS].rsplit("\n\n", 1)[0].strip()
    return text


def strip_sidecar_header(markdown: str) -> str:
    lines = markdown.replace("\r\n", "\n").splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    match = HEADING_RE.match(lines[0].strip()) if lines else None
    if match and match.group(1) == "#":
        lines.pop(0)
    while lines and (
        not lines[0].strip()
        or lines[0].startswith("- arXiv ID:")
        or lines[0].startswith("- HTML source:")
    ):
        lines.pop(0)
    return "\n".join(lines)


def drop_leading_author_blocks(markdown: str) -> str:
    paragraphs = re.split(r"\n\s*\n", markdown.lstrip(), maxsplit=3)
    while paragraphs and authorish_paragraph(paragraphs[0]):
        paragraphs.pop(0)
    return "\n\n".join(paragraphs)


def authorish_paragraph(text: str) -> bool:
    lowered = text.lower()
    return "@" in text or any(token in lowered for token in ("department of", "university", "institute", "equal contribution"))


def content_start_index(lines: list[str]) -> int:
    fallback = 0
    for index, line in enumerate(lines):
        match = HEADING_RE.match(line.strip())
        if not match:
            continue
        heading = embedding_heading_key(match.group(2))
        if re.match(r"^introduction\b", heading, re.IGNORECASE):
            return index
        if fallback == 0 and re.match(r"^abstract\b", heading, re.IGNORECASE):
            fallback = index
    return fallback


def content_end_index(lines: list[str], start: int) -> int:
    for index, line in enumerate(lines[start + 1 :], start + 1):
        match = HEADING_RE.match(line.strip())
        if match and TAIL_HEADING_RE.match(embedding_heading_key(match.group(2))):
            return index
        if plain_tail_marker(line):
            return index
    return len(lines)


def plain_tail_marker(line: str) -> bool:
    text = line.strip().strip("# ").casefold()
    return bool(
        re.match(
            r"^(references(?: and notes)?|bibliography|acknowledg(?:e)?ments?|funding|appendix|supplementary)\b",
            text,
        )
    )


def embedding_heading_key(heading: str) -> str:
    heading = heading.strip()
    heading = re.sub(r"^(?:[0-9]+(?:\.[0-9]+)*|[IVXLCDM]+)[).:]?\s+", "", heading, flags=re.IGNORECASE)
    heading = re.sub(r"^[A-Za-z](?:\.\d+)*(?:[).:]\s*|\s+)(?=[A-Z][A-Za-z-]{2,}\b)", "", heading)
    return heading.strip(" .:-")


def normalized_embedding_heading(line: str) -> str:
    match = HEADING_RE.match(line)
    if not match:
        return ""
    marker, heading = match.groups()
    heading = re.sub(r"\s+", " ", embedding_heading_key(heading)).strip(": ")
    if not heading:
        return ""
    level = "###" if len(marker) > 2 and heading.casefold() != "abstract" else "##"
    return f"{level} {heading}"


def clean_embedding_lines(lines: list[str]) -> list[str]:
    cleaned: list[str] = []
    skipping_block = False
    for line in lines:
        stripped = line.strip()
        heading = normalized_embedding_heading(stripped)
        if heading:
            cleaned.append(heading)
            continue
        if table_separator_line(stripped):
            skipping_block = True
            continue
        if skipping_block and not stripped:
            skipping_block = False
            cleaned.append("")
            continue
        if skipping_block:
            continue

        line = clean_embedding_line(line)
        if keep_embedding_line(line):
            cleaned.append(line)
    return cleaned


def clean_embedding_line(line: str) -> str:
    line = LATEX_SPACE_RE.sub("", line)
    line = NUMERIC_CITATION_RE.sub("", line)
    line = PAREN_NUMERIC_CITATION_RE.sub("", line)
    line = YEAR_CITATION_RE.sub("", line)
    line = COMPACT_CITATION_RE.sub("", line)
    line = re.sub(r"(?:\s*[;,]\s*){2,}", " ", line)
    line = re.sub(r"\s+([.,;:])", r"\1", line)
    line = re.sub(r"\s+", " ", line).strip()
    return line


def table_separator_line(line: str) -> bool:
    return bool(line) and len(line) > 8 and set(line) <= {"-", " ", "|", ":"}


def keep_embedding_line(line: str) -> bool:
    if not line:
        return True
    if line.startswith("#") and not line.lstrip("#").strip():
        return False
    if line.startswith("#"):
        return True
    words = re.findall(r"[A-Za-z][A-Za-z-]{2,}", line)
    if len(words) < 3 and not line.lower().startswith("keywords:"):
        return False
    if len(line) > 80:
        alpha = sum(char.isalpha() for char in line)
        if alpha / max(len(line), 1) < 0.35:
            return False
    return True


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
