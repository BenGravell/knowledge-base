"""Canonical in-process catalog of metadata-backed papers."""

from __future__ import annotations

import hashlib
import html
import json
import re
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date
from functools import lru_cache
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
EMBED_INPUT_SIDECAR = "embed_input.md"

# Loose storage safety valve; embedding backends may need chunking below this.
EMBED_TEXT_MAX_CHARS = 5_000_000

# Strictest downstream embedding model today is all-MiniLM-L6-v2 via fastembed.
EMBEDDING_CHUNK_MAX_TOKENS = 256
EMBEDDING_CHUNK_MAX_CHARS = 2_000
EMBEDDING_MIN_CHUNK_CHARS = 160
EMBEDDING_TOKENIZER_VOCAB = Path(__file__).with_name("tokenizers") / "all-MiniLM-L6-v2-vocab.txt"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
EMBEDDING_INPUT_CHUNK_RE = re.compile(r"^<!-- chunk (\{.*\}) -->\s*$", re.MULTILINE)
TAIL_HEADING_RE = re.compile(
    r"^(references|bibliography|acknowledg(?:e)?ments?|funding|appendix|supplementary)\b",
    re.IGNORECASE,
)
START_HEADING_RE = re.compile(r"^(introduction|abstract)\b", re.IGNORECASE)
FRONT_MATTER_HEADING_RE = re.compile(r"^(contents|preface|chapter\s+0\b)", re.IGNORECASE)
BODY_START_HEADING_RE = re.compile(r"^(?:chapter\s+)?[1-9]\d*\b", re.IGNORECASE)
PLAIN_INTRODUCTION_RE = re.compile(r"^(?:[0-9]+(?:\.[0-9]+)*[).]?\s*)?introduction\b", re.IGNORECASE)
PLAIN_TAIL_MARKER_RE = re.compile(
    r"^(?:references(?: and notes)?|bibliography|acknowledg(?:e)?ments?|funding)\.?$"
    r"|^(?:appendix|appendices|supplementary(?: material)?)(?:\s+[a-z0-9]+)?$",
    re.IGNORECASE,
)
NUMERIC_CITATION_RE = re.compile(r"\\?\[[\d,\s;:–—-]+\\?\]")
PAREN_NUMERIC_CITATION_RE = re.compile(r"\(\s*\d+(?:\s*[,;]\s*\d+)*\s*\)")
YEAR_CITATION_RE = re.compile(r"\([^()]{0,160}\b(?:19|20)\d{2}[a-z]?\b[^()]{0,160}\)")
COMPACT_CITATION_RE = re.compile(r"\b(?:[A-Z]{2,}|[A-Z][A-Za-z]+)[0-9]{2}[a-z]?\b")
LATEX_SPACE_RE = re.compile(r"\\hspace\{[^}]*\}")
LATEX_BARE_URL_RE = re.compile(r"\\+urlhttps?://\S+")
LATEX_URL_RE = re.compile(r"\\+url\{[^}]*\}")
LATEX_URL_COMMAND_RE = re.compile(r"\\+url\b")
LATEX_CITATION_COMMAND_RE = re.compile(r"\\(?:cite\w*|supercite)\*?(?:\[[^\]]*])*(?:\s*\{[^}]*\})?")
LATEX_REF_COMMAND_RE = re.compile(r"\\(?:ref|eqref|autoref|cref|Cref)\*?\{([^}]*)\}")
NESTED_URL_CITATION_RE = re.compile(r"\([^()]*\([^()]*https?://[^)]*\)[^()]*\)")
PAREN_URL_RE = re.compile(r"\([^()]*https?://[^)]*\)")
MARKDOWN_LINK_RE = re.compile(r"\[([^]]+)]\((?:https?://|#)[^)]+\)")
URL_RE = re.compile(r"https?://\S+")
INLINE_MATH_SPAN_RE = re.compile(r"(?<!\$)\$([^$\n]+)\$(?!\$)")
URL_POINTER_BOILERPLATE_RE = re.compile(
    r"\s*(?:"
    r"(?:the\s+)?(?:published|final|journal|official|peer-reviewed)\s+version"
    r"(?:\s+of\s+(?:this|the)\s+(?:draft|paper|article|work|preprint))?"
    r"|(?:this|the)\s+(?:draft|paper|article|work|preprint)"
    r")\s+(?:is\s+)?available\s+(?:at|from|online\s+at)\b.*$",
    re.IGNORECASE,
)
BROKEN_PDF_TEXT_REPLACEMENTS = (
    (re.compile(r"\bErd\s+os\b"), "Erd\u0151s"),
    (re.compile(r"\bErdos\b"), "Erd\u0151s"),
    (re.compile(r"\bRenyi\b"), "R\u00e9nyi"),
)
EMBEDDING_SENTENCE_ABBREVIATIONS = (
    "e.g.",
    "i.e.",
    "cf.",
    "viz.",
    "vs.",
    "etc.",
    "et al.",
    "Fig.",
    "Eq.",
    "Sec.",
    "No.",
    "Nos.",
    "MS.",
    "MSS.",
    "Mr.",
    "Mrs.",
    "Ms.",
    "Dr.",
    "Prof.",
    "St.",
)
EMBEDDING_TRAILING_ABBREVIATION_RE = re.compile(
    r"(?:^|\s)(?:cf|viz|vs|etc|Fig|Eq|Sec|No|Nos|MS|MSS|Mr|Mrs|Ms|Dr|Prof|St)\.$"
)
EMBEDDING_FIELD_PREFIX_RE = re.compile(
    r"^(?:title|tags|summary|abstract|content|results|contributions?|"
    r"limitation and future work|limitations?|future work):\s*",
    re.IGNORECASE,
)
EMBEDDING_PREFERRED_SECTION_RE = re.compile(
    r"^(abstract|introduction|conclusion|discussion|limitations?|future work)\b",
    re.IGNORECASE,
)
EMBEDDING_SKIP_SECTION_RE = re.compile(
    r"^(related work|background|preliminaries|notation|proof|lemma|theorem|definition|"
    r"corollary|proposition|appendix|supplementary|references|bibliography)\b",
    re.IGNORECASE,
)
EMBEDDING_HIGH_SIGNAL_RE = re.compile(
    r"\b(we propose|we introduce|we present|we develop|we show|we prove|we demonstrate|"
    r"we evaluate|this paper|our method|our approach|results show|outperform|improve|"
    r"converges?|guarantee|our framework|our algorithm|our model)\b",
    re.IGNORECASE,
)
EMBEDDING_LOW_SIGNAL_RE = re.compile(
    r"^(the rest of this paper|notation\.|we use .+ to denote|for simplicity|table\s+\w*:|figure\s+\d+:)",
    re.IGNORECASE,
)


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


@dataclass(frozen=True, slots=True)
class EmbeddingContentBlock:
    section: str
    text: str
    index: int


@dataclass(frozen=True, slots=True)
class EmbeddingInputChunk:
    id: str
    role: str
    section: str
    weight: float
    text: str


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
    embedding_chunks: tuple[EmbeddingInputChunk, ...]
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
        write_embedding_input_sidecar: bool = False,
        refresh_embedding_input_sidecar: bool = False,
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
        cached_embedding_chunks = (
            () if refresh_embedding_input_sidecar else embedding_input_sidecar_chunks(metadata_path)
        )
        embedding_chunks = cached_embedding_chunks or build_embedding_chunks(
            metadata_path=metadata_path,
            title=title,
            tags=tags,
            summary=summary,
            abstract=abstract,
        )
        embedding_text = render_embedding_input_chunks(embedding_chunks)
        if (write_embedding_input_sidecar or refresh_embedding_input_sidecar) and not cached_embedding_chunks:
            write_text_if_changed(
                embedding_input_sidecar_path(metadata_path), embedding_chunks_sidecar_text(embedding_chunks)
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
            embedding_chunks=embedding_chunks,
            embedding_text=embedding_text,
            embedding_hash=content_hash(embedding_chunks_sidecar_text(embedding_chunks)),
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
        write_embedding_input_sidecars: bool = False,
        refresh_embedding_input_sidecars: bool = False,
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
                        write_embedding_input_sidecar=write_embedding_input_sidecars,
                        refresh_embedding_input_sidecar=refresh_embedding_input_sidecars,
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
    return render_embedding_input_chunks(
        build_embedding_chunks(
            metadata_path=metadata_path,
            title=title,
            tags=tags,
            summary=summary,
            abstract=abstract,
        )
    )


def build_embedding_chunks(
    *,
    metadata_path: Path | None = None,
    title: str,
    tags: tuple[str, ...],
    summary: str,
    abstract: str,
) -> tuple[EmbeddingInputChunk, ...]:
    chunks: list[EmbeddingInputChunk] = []

    def add(role: str, section: str, weight: float, text: str) -> None:
        for piece in chunk_embedding_text(clean_embedding_chunk_text(text)):
            if role == "body" and not keep_embedding_paragraph(piece):
                continue
            chunks.append(
                EmbeddingInputChunk(
                    id=f"{role}-{len(chunks) + 1:04d}",
                    role=role,
                    section=section,
                    weight=weight,
                    text=piece,
                )
            )

    parts = [clean_inline(title)]
    if tags:
        parts.append(f"Topics include {', '.join(tags)}.")
    add("metadata", "Metadata", 3.0, "\n\n".join(parts))
    add("summary", "Summary", 2.0, summary)
    add("abstract", "Abstract", 2.0, abstract)

    content = embedding_sidecar_text(metadata_path) if metadata_path else ""
    if content:
        for block in embedding_content_blocks(content):
            if not keep_embedding_block(block):
                continue
            section = clean_inline(block.section)
            weight = 1.5 if EMBEDDING_PREFERRED_SECTION_RE.match(section) else 1.0
            text = clean_embedding_chunk_text(block.text)
            if not keep_embedding_paragraph(text):
                continue
            add("body", section or "Paper Body", weight, text)

    return tuple(chunk for chunk in chunks if chunk.text.strip())


def embedding_sidecar_path(metadata_path: Path) -> Path | None:
    path = metadata_path.with_name(EMBED_TEXT_SIDECAR)
    if path.is_file():
        return path
    return None


def embedding_input_sidecar_path(metadata_path: Path) -> Path:
    return metadata_path.with_name(EMBED_INPUT_SIDECAR)


def embedding_input_sidecar_text(metadata_path: Path) -> str:
    return render_embedding_input_chunks(embedding_input_sidecar_chunks(metadata_path))


def embedding_input_sidecar_chunks(metadata_path: Path) -> tuple[EmbeddingInputChunk, ...]:
    path = embedding_input_sidecar_path(metadata_path)
    if not path.is_file():
        return ()
    return parse_embedding_input_sidecar(path.read_text(encoding="utf-8"))


def parse_embedding_input_sidecar(text: str) -> tuple[EmbeddingInputChunk, ...]:
    raw = text.strip()
    if not raw:
        return ()

    matches = list(EMBEDDING_INPUT_CHUNK_RE.finditer(raw))
    if not matches:
        return (EmbeddingInputChunk(id="cached-0000", role="cached", section="", weight=1.0, text=raw),)

    chunks: list[EmbeddingInputChunk] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(raw)
        chunk_text = raw[start:end].strip()
        if not chunk_text:
            continue
        metadata: dict[str, Any]
        try:
            raw_metadata = json.loads(match.group(1))
        except json.JSONDecodeError:
            metadata = dict[str, Any]()
        else:
            metadata = (
                {str(key): value for key, value in raw_metadata.items()}
                if isinstance(raw_metadata, dict)
                else dict[str, Any]()
            )
        try:
            weight = float(metadata.get("weight") or 1.0)
        except (TypeError, ValueError):
            weight = 1.0
        chunks.append(
            EmbeddingInputChunk(
                id=clean_scalar(metadata.get("id")) or f"cached-{index:04d}",
                role=clean_scalar(metadata.get("role")) or "cached",
                section=clean_scalar(metadata.get("section")),
                weight=weight,
                text=chunk_text,
            )
        )
    return tuple(chunks)


def render_embedding_input_chunks(chunks: Iterable[EmbeddingInputChunk]) -> str:
    return "\n\n".join(chunk.text.strip() for chunk in chunks if chunk.text.strip()).strip()


def embedding_chunks_sidecar_text(chunks: Iterable[EmbeddingInputChunk]) -> str:
    parts = ["<!-- embedding-input:v1 -->"]
    for chunk in chunks:
        text = chunk.text.strip()
        if not text:
            continue
        metadata = json.dumps(
            {
                "id": chunk.id,
                "role": chunk.role,
                "section": chunk.section,
                "weight": chunk.weight,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
        parts.append(f"<!-- chunk {metadata} -->\n\n{text}")
    return "\n\n".join(parts).rstrip() + "\n"


def write_text_if_changed(path: Path, text: str) -> None:
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return
    path.write_text(text, encoding="utf-8")


def embedding_sidecar_text(metadata_path: Path) -> str:
    path = embedding_sidecar_path(metadata_path)
    if path is None:
        return ""
    return clean_embedding_sidecar_text(path.read_text(encoding="utf-8"))


def clean_embedding_chunk_text(text: str) -> str:
    lines: list[str] = []
    for line in clean_scalar(text).splitlines():
        stripped = line.strip()
        if not stripped:
            lines.append("")
        elif stripped.startswith("#"):
            lines.append(normalized_embedding_heading(stripped) or stripped)
        else:
            lines.append(clean_embedding_line(stripped))
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def chunk_embedding_text(
    text: str,
    *,
    max_tokens: int = EMBEDDING_CHUNK_MAX_TOKENS,
    max_chars: int = EMBEDDING_CHUNK_MAX_CHARS,
    min_chars: int = EMBEDDING_MIN_CHUNK_CHARS,
) -> list[str]:
    text = text.strip()
    if not text:
        return []
    if embedding_chunk_fits(text, max_tokens=max_tokens, max_chars=max_chars):
        return [clean_excerpt_boundary(text)]

    chunks: list[str] = []
    current = ""
    for unit in embedding_chunk_units(text):
        if not embedding_chunk_fits(unit, max_tokens=max_tokens, max_chars=max_chars):
            if current:
                chunks.append(current)
                current = ""
            chunks.extend(split_oversized_embedding_unit(unit, max_tokens=max_tokens, max_chars=max_chars))
            continue
        separator = "\n\n" if current.startswith("#") and "\n\n" not in current else " "
        candidate = f"{current}{separator}{unit}".strip()
        if not current or embedding_chunk_fits(candidate, max_tokens=max_tokens, max_chars=max_chars):
            current = candidate
        else:
            chunks.append(current)
            current = unit
    if current:
        chunks.append(current)

    if len(chunks) > 1 and len(chunks[-1]) < min_chars:
        merged = f"{chunks[-2]} {chunks[-1]}".strip()
        if embedding_chunk_fits(merged, max_tokens=max_tokens, max_chars=max_chars):
            chunks[-2:] = [merged]

    return [clean_excerpt_boundary(chunk) for chunk in chunks if chunk.strip()]


def embedding_chunk_units(text: str) -> list[str]:
    units: list[str] = []
    for paragraph in re.split(r"\n\s*\n", text):
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        if paragraph.startswith("#"):
            units.append(paragraph)
            continue
        units.extend(sentence.strip() for sentence in split_embedding_sentences(paragraph) if sentence.strip())
    return units


def split_oversized_embedding_unit(
    text: str,
    *,
    max_tokens: int = EMBEDDING_CHUNK_MAX_TOKENS,
    max_chars: int = EMBEDDING_CHUNK_MAX_CHARS,
) -> list[str]:
    pieces: list[str] = []
    current = ""
    for word in text.split():
        candidate = f"{current} {word}".strip() if current else word
        if embedding_chunk_fits(candidate, max_tokens=max_tokens, max_chars=max_chars):
            current = candidate
            continue
        if current:
            prefix, suffix = split_trailing_embedding_abbreviation(current)
            if suffix:
                if prefix:
                    pieces.append(prefix)
                current = suffix
                candidate = f"{current} {word}".strip()
                if embedding_chunk_fits(candidate, max_tokens=max_tokens, max_chars=max_chars):
                    current = candidate
                    continue
            pieces.append(current)
            current = ""
        if embedding_chunk_fits(word, max_tokens=max_tokens, max_chars=max_chars):
            current = word
        else:
            pieces.extend(split_oversized_embedding_word(word, max_tokens=max_tokens, max_chars=max_chars))
    if current:
        pieces.append(current)
    return pieces


def split_trailing_embedding_abbreviation(text: str) -> tuple[str, str]:
    if not EMBEDDING_TRAILING_ABBREVIATION_RE.search(text):
        return text, ""
    prefix, separator, suffix = text.rpartition(" ")
    if not separator:
        return text, ""
    return prefix.strip(), suffix.strip()


def split_oversized_embedding_word(
    text: str,
    *,
    max_tokens: int = EMBEDDING_CHUNK_MAX_TOKENS,
    max_chars: int = EMBEDDING_CHUNK_MAX_CHARS,
) -> list[str]:
    pieces: list[str] = []
    remaining = text
    while remaining:
        cut = min(len(remaining), max_chars)
        while cut > 1 and not embedding_chunk_fits(remaining[:cut], max_tokens=max_tokens, max_chars=max_chars):
            cut //= 2
        pieces.append(remaining[:cut])
        remaining = remaining[cut:]
    return pieces


def embedding_chunk_fits(
    text: str,
    *,
    max_tokens: int = EMBEDDING_CHUNK_MAX_TOKENS,
    max_chars: int = EMBEDDING_CHUNK_MAX_CHARS,
) -> bool:
    return len(text) <= max_chars and embedding_token_count(text) <= max_tokens


@lru_cache(maxsize=65_536)
def embedding_token_count(text: str) -> int:
    return len(embedding_tokenizer().encode(text).ids)


@lru_cache(maxsize=1)
def embedding_tokenizer() -> Any:
    from tokenizers import Tokenizer
    from tokenizers.models import WordPiece
    from tokenizers.normalizers import BertNormalizer
    from tokenizers.pre_tokenizers import BertPreTokenizer
    from tokenizers.processors import TemplateProcessing

    tokenizer = Tokenizer(WordPiece.from_file(str(EMBEDDING_TOKENIZER_VOCAB), unk_token="[UNK]"))
    tokenizer.normalizer = BertNormalizer(lowercase=True)
    tokenizer.pre_tokenizer = BertPreTokenizer()
    cls_id = tokenizer.token_to_id("[CLS]")
    sep_id = tokenizer.token_to_id("[SEP]")
    tokenizer.post_processor = TemplateProcessing(
        single="[CLS] $A [SEP]",
        pair="[CLS] $A [SEP] $B:1 [SEP]:1",
        special_tokens=[("[CLS]", cls_id), ("[SEP]", sep_id)],
    )
    return tokenizer


def compact_inline_for_embedding(text: str, max_chars: int) -> str:
    return truncate_embedding_text(clean_embedding_line(clean_inline(text)), max_chars)


def compact_embedding_content(markdown: str, max_chars: int = EMBEDDING_CHUNK_MAX_CHARS) -> str:
    blocks = [
        block
        for block in (compact_embedding_block(block) for block in embedding_content_blocks(markdown))
        if block is not None
    ]
    if not blocks:
        return ""

    filtered = render_embedding_blocks(blocks)
    if len(filtered) <= max_chars:
        return filtered

    selected: list[EmbeddingContentBlock] = []
    selected_indexes: set[int] = set()

    def try_add(block: EmbeddingContentBlock) -> None:
        if block.index in selected_indexes:
            return
        candidate = sorted([*selected, block], key=lambda item: item.index)
        if len(render_embedding_blocks(candidate)) <= max_chars:
            selected.append(block)
            selected_indexes.add(block.index)

    intro = [block for block in blocks if section_matches(block, "introduction") or section_matches(block, "abstract")]
    preferred = [block for block in blocks if EMBEDDING_PREFERRED_SECTION_RE.match(block.section)]
    conclusion = [
        block
        for block in blocks
        if re.match(r"^(conclusion|discussion|limitations?|future work)\b", block.section, re.IGNORECASE)
    ]

    for block in intro[:1]:
        try_add(block)
    for block in high_signal_blocks(intro, limit=2):
        try_add(block)
    for block in conclusion[:2]:
        try_add(block)
    if len({block.section for block in blocks}) <= 1:
        try_add(blocks[-1])
    for block in intro[1:3]:
        try_add(block)
    for block in high_signal_blocks(preferred, limit=4):
        try_add(block)
    for block in blocks[:4]:
        try_add(block)
    if not selected:
        for block in blocks:
            try_add(block)
            if selected:
                break

    return render_embedding_blocks(sorted(selected, key=lambda item: item.index))


def embedding_content_blocks(markdown: str) -> list[EmbeddingContentBlock]:
    blocks: list[EmbeddingContentBlock] = []
    section = ""
    for part in (part.strip() for part in re.split(r"\n\s*\n", markdown.strip())):
        if not part:
            continue
        lines = part.splitlines()
        heading = normalized_embedding_heading(lines[0].strip()) if len(lines) == 1 else ""
        if heading:
            section = heading.lstrip("#").strip()
            continue
        if keep_embedding_paragraph(part):
            blocks.append(EmbeddingContentBlock(section=section, text=part, index=len(blocks)))
    return blocks


def compact_embedding_block(block: EmbeddingContentBlock) -> EmbeddingContentBlock | None:
    if not keep_embedding_block(block):
        return None
    text = compact_embedding_block_text(block.text)
    if not text:
        return None
    return EmbeddingContentBlock(section=block.section, text=text, index=block.index)


def keep_embedding_block(block: EmbeddingContentBlock) -> bool:
    if EMBEDDING_SKIP_SECTION_RE.match(block.section):
        return False
    text = block.text.strip()
    if EMBEDDING_LOW_SIGNAL_RE.match(text):
        return False
    return not text.startswith(("TABLE ", "Figure "))


def compact_embedding_block_text(text: str, max_chars: int = EMBEDDING_CHUNK_MAX_CHARS) -> str:
    text = text.strip()
    if len(text) <= max_chars:
        return clean_excerpt_boundary(text)
    sentences = split_embedding_sentences(text)
    selected: list[str] = []
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        candidate = " ".join([*selected, sentence]) if selected else sentence
        if len(candidate) <= max_chars:
            selected.append(sentence)
        elif selected:
            break
    return clean_excerpt_boundary(" ".join(selected))


def render_embedding_blocks(blocks: Iterable[EmbeddingContentBlock]) -> str:
    parts: list[str] = []
    current_section = ""
    for block in blocks:
        if block.section and block.section != current_section:
            parts.append(f"## {block.section}")
            current_section = block.section
        parts.append(block.text)
    return "\n\n".join(parts).strip()


def section_matches(block: EmbeddingContentBlock, name: str) -> bool:
    return bool(re.match(rf"^{re.escape(name)}\b", block.section, re.IGNORECASE))


def high_signal_blocks(blocks: Iterable[EmbeddingContentBlock], limit: int) -> list[EmbeddingContentBlock]:
    selected: list[EmbeddingContentBlock] = []
    for block in blocks:
        if EMBEDDING_HIGH_SIGNAL_RE.search(block.text):
            selected.append(block)
            if len(selected) >= limit:
                break
    return selected


def truncate_embedding_text(text: str, max_chars: int) -> str:
    text = text.strip()
    if max_chars <= 0 or len(text) <= max_chars:
        return clean_excerpt_boundary(text)
    sentences = split_embedding_sentences(text)
    selected: list[str] = []
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        candidate = " ".join([*selected, sentence]) if selected else sentence
        if len(candidate) <= max_chars:
            selected.append(sentence)
        elif selected:
            break
    if selected:
        return clean_excerpt_boundary(" ".join(selected))
    cut = text[:max_chars].rstrip()
    word = cut.rfind(" ")
    if word >= max_chars // 2:
        cut = cut[:word]
    return clean_excerpt_boundary(cut)


def clean_excerpt_boundary(text: str) -> str:
    text = re.sub(r"\s+[^.?!]*:\s*$", "", text.strip())
    return re.sub(r"\.{3,}$", ".", text).strip()


def split_embedding_sentences(text: str) -> list[str]:
    protected = text
    replacements = {source: source.replace(".", "<dot>") for source in EMBEDDING_SENTENCE_ABBREVIATIONS}
    for source, target in replacements.items():
        protected = protected.replace(source, target)
    protected = re.sub(r"\b([A-Z])\.", r"\1<dot>", protected)
    protected = re.sub(r"\b(\d+)\.\s+(?=[A-Z])", r"\1<dot> ", protected)
    sentences = re.split(r"(?<=[.!?])\s+", protected)
    for source, target in replacements.items():
        sentences = [sentence.replace(target, source) for sentence in sentences]
    return [sentence.replace("<dot>", ".") for sentence in sentences]


def clean_embedding_sidecar_text(markdown: str) -> str:
    lines = drop_leading_author_blocks(strip_sidecar_header(markdown)).splitlines()
    start = content_start_index(lines)
    end = content_end_index(lines, start)
    text = "\n".join(reflow_embedding_lines(clean_embedding_lines(lines[start:end])))
    text = repair_broken_pdf_text(text)
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
        not lines[0].strip() or lines[0].startswith("- arXiv ID:") or lines[0].startswith("- HTML source:")
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
    return "@" in text or any(
        token in lowered for token in ("department of", "university", "institute", "equal contribution")
    )


def content_start_index(lines: list[str]) -> int:
    abstract_index: int | None = None
    body_index: int | None = None
    plain_intro_index: int | None = None
    saw_front_matter = False
    for index, line in enumerate(lines):
        stripped = line.strip()
        if plain_intro_index is None and plain_introduction_marker(stripped):
            plain_intro_index = index
        match = HEADING_RE.match(stripped)
        if not match:
            continue
        raw_heading = match.group(2).strip()
        heading = embedding_heading_key(raw_heading)
        if re.match(r"^introduction\b", heading, re.IGNORECASE):
            return index
        if abstract_index is None and re.match(r"^abstract\b", heading, re.IGNORECASE):
            abstract_index = index
        if body_index is None and BODY_START_HEADING_RE.match(raw_heading):
            body_index = index
        if FRONT_MATTER_HEADING_RE.match(heading):
            saw_front_matter = True
    if abstract_index is not None:
        return abstract_index
    if plain_intro_index is not None:
        return plain_intro_index
    if body_index is not None:
        return body_index
    return len(lines) if saw_front_matter else 0


def content_end_index(lines: list[str], start: int) -> int:
    for index, line in enumerate(lines[start + 1 :], start + 1):
        match = HEADING_RE.match(line.strip())
        if match and TAIL_HEADING_RE.match(embedding_heading_key(match.group(2))):
            return index
        if plain_tail_marker(line):
            return index
    return len(lines)


def plain_tail_marker(line: str) -> bool:
    return bool(PLAIN_TAIL_MARKER_RE.match(line.strip().strip("# ").strip()))


def plain_introduction_marker(line: str) -> bool:
    text = line.strip().strip("# ").strip()
    if not text:
        return False
    return bool(PLAIN_INTRODUCTION_RE.match(text))


def embedding_heading_key(heading: str) -> str:
    heading = heading.strip()
    heading = re.sub(r"^(?:[0-9]+(?:\.[0-9]+)*|[IVXLCDM]+)[).:]?\s+", "", heading, flags=re.IGNORECASE)
    heading = re.sub(r"^[A-Za-z](?:\.\d+)*(?:[).:]\s*|\s+)(?=[A-Z][A-Za-z-]{2,}\b)", "", heading)
    heading = repeated_heading_prefix(heading)
    return heading.strip(" .:-")


def repeated_heading_prefix(heading: str) -> str:
    if not re.search(r"\s*[.:-]\s+", heading):
        return heading
    for separator in re.finditer(r"\s*[.:-]\s+", heading):
        left = heading[: separator.start()].strip()
        right = heading[separator.end() :].strip()
        if left and heading_phrase_key(left) == heading_phrase_key(right):
            return left
    left, _separator, right = re.split(r"\s*([.:-])\s+", heading, maxsplit=1)
    if left and heading_phrase_key(left) == heading_phrase_key(right):
        return left
    return heading


def heading_phrase_key(heading: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", heading.casefold()).strip()


def normalized_embedding_heading(line: str) -> str:
    match = HEADING_RE.match(line)
    if not match:
        return ""
    marker, heading = match.groups()
    heading = clean_embedding_line(embedding_heading_key(heading))
    heading = re.sub(r"\s+", " ", heading).strip(": ")
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


def reflow_embedding_lines(lines: list[str]) -> list[str]:
    reflowed: list[str] = []
    paragraph = ""
    pending_blank = False

    def flush() -> None:
        nonlocal paragraph
        if paragraph:
            reflowed.append(paragraph)
            paragraph = ""

    for line in lines:
        if not line:
            pending_blank = True
            continue
        if line.startswith("#"):
            flush()
            if reflowed and reflowed[-1]:
                reflowed.append("")
            reflowed.extend([line, ""])
            pending_blank = False
            continue
        if (
            pending_blank
            and not paragraph
            and len(reflowed) >= 2
            and reflowed[-1] == ""
            and reflowed[-2].startswith("#")
        ):
            fixed_heading = split_broken_embedding_heading(reflowed[-2], line)
            if fixed_heading:
                reflowed[-2], line = fixed_heading
                if not line:
                    pending_blank = False
                    continue
        if paragraph and pending_blank and not artificial_paragraph_break(paragraph, line):
            flush()
            reflowed.append("")
        paragraph = join_embedding_text(paragraph, line)
        pending_blank = False

    flush()
    while reflowed and not reflowed[-1]:
        reflowed.pop()
    return reflowed


def split_broken_embedding_heading(heading_line: str, following: str) -> tuple[str, str] | None:
    match = HEADING_RE.match(heading_line)
    continuation = re.match(r"^(.+?\.)\s+(?=[A-Z])(.*)$", following.strip())
    if not match or not continuation or not following[:1].islower():
        return None

    marker, heading = match.groups()
    completed_heading = f"{heading} {continuation.group(1).rstrip('.')}"
    rest = continuation.group(2).strip()
    if not heading_phrase_key(rest).startswith(heading_phrase_key(completed_heading)):
        return None

    prefix = re.escape(completed_heading).replace(r"\ ", r"\s+")
    rest = re.sub(rf"^{prefix}\.?\s*", "", rest, count=1, flags=re.IGNORECASE)
    return f"{marker} {completed_heading.strip(' .:-')}", rest


def artificial_paragraph_break(previous: str, following: str) -> bool:
    previous = previous.rstrip()
    following = following.lstrip()
    if following.startswith(("- ", "* ", "+ ")):
        return False
    if previous.endswith(("(", "[", ",", "-", "/", "\\")):
        return True
    if re.search(r"\b(?:Sec|Fig|Eq|Ref|Refs|No|Nos)\.$", previous) and re.match(r"^[IVXLCDM\d]", following):
        return True
    if following.startswith("$") and not following.startswith("$$"):
        return True
    if following[:1].islower() or re.match(r"^(?:[,.;:)\]]|\d+[),.]|\[[^\]]+\])", following):
        return True
    if not re.search(r"[.!?][\"')\]]*$", previous):
        return True
    return bool(
        re.search(
            r"\b(?:a|an|and|are|as|at|be|been|being|between|by|can|could|did|do|does|during|for|from|"
            r"in|including|into|is|may|might|not|of|on|only|or|should|that|the|to|using|was|were|"
            r"which|while|will|with|without|would)$",
            previous,
            re.IGNORECASE,
        )
    )


def join_embedding_text(previous: str, following: str) -> str:
    following = following.strip()
    if not previous:
        return following
    if previous.endswith("-") and following[:1].islower():
        text = f"{previous[:-1]}{following}"
    elif previous.endswith(("(", "[", "/", "\\")) or following[:1] in ")]},.;:%":
        text = f"{previous}{following}"
    else:
        text = f"{previous} {following}"
    text = re.sub(r"([([])\s+", r"\1", text)
    text = re.sub(r"\s+([)\]])", r"\1", text)
    text = re.sub(r"\s+([,.;:])", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def clean_embedding_line(line: str) -> str:
    line = html.unescape(line)
    line = repair_broken_pdf_text(line)
    line = clean_embedding_math_spans(line)
    line = LATEX_SPACE_RE.sub("", line)
    line = LATEX_BARE_URL_RE.sub("", line)
    line = LATEX_URL_RE.sub("", line)
    line = LATEX_URL_COMMAND_RE.sub("", line)
    line = LATEX_CITATION_COMMAND_RE.sub("", line)
    line = LATEX_REF_COMMAND_RE.sub(r"\1", line)
    line = MARKDOWN_LINK_RE.sub(r"\1", line)
    line = NESTED_URL_CITATION_RE.sub("", line)
    line = PAREN_URL_RE.sub("", line)
    line = URL_RE.sub("", line)
    line = URL_POINTER_BOILERPLATE_RE.sub("", line)
    line = NUMERIC_CITATION_RE.sub("", line)
    line = PAREN_NUMERIC_CITATION_RE.sub("", line)
    line = YEAR_CITATION_RE.sub("", line)
    line = COMPACT_CITATION_RE.sub("", line)
    line = EMBEDDING_FIELD_PREFIX_RE.sub("", line)
    line = re.sub(r"\b(?:on|in|at|by|for|from|with)\s+\\?\[\s*\\?\]", "", line)
    line = re.sub(r"\\?\[\s*\\?\]", "", line)
    line = re.sub(r"\(\s*[,;:]?\s*\)", "", line)
    line = re.sub(r"(?:\s*[;,]\s*){2,}", " ", line)
    line = re.sub(r"\s+([.,;:])", r"\1", line)
    line = re.sub(r"\b(?:on|in|at|by|for|from|with)([.,;:])", r"\1", line)
    line = re.sub(r"\b(?:on|in|at|by|for|from|with)\s+([.,;:])", r"\1", line)
    return re.sub(r"\s+", " ", line).strip()


def repair_broken_pdf_text(text: str) -> str:
    for pattern, replacement in BROKEN_PDF_TEXT_REPLACEMENTS:
        text = pattern.sub(replacement, text)
    return text


def clean_embedding_math_spans(line: str) -> str:
    line = line.replace(r"$\,$", " ")

    def replace(match: re.Match[str]) -> str:
        inner = match.group(1).replace(r"\_", "_")
        return f"${inner}$"

    return INLINE_MATH_SPAN_RE.sub(replace, line)


def table_separator_line(line: str) -> bool:
    return bool(line) and len(line) > 8 and set(line) <= {"-", " ", "|", ":"}


def keep_embedding_line(line: str) -> bool:
    if not line:
        return True
    lowered = line.casefold()
    if lowered.startswith("image:") or "mailto:" in lowered or "footnote-" in lowered:
        return False
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


def keep_embedding_paragraph(paragraph: str) -> bool:
    text = re.sub(r"\s+", " ", paragraph).strip()
    if not text:
        return False
    if text.startswith("#"):
        return True
    words = re.findall(r"[A-Za-z][A-Za-z-]{2,}", text)
    if len(words) < 5 and not text.casefold().startswith("keywords:"):
        return False
    if reference_like_paragraph(text):
        return False
    alpha = sum(char.isalpha() for char in text)
    digits = sum(char.isdigit() for char in text)
    math_symbols = sum(char in "$\\{}_^=<>|" for char in text)
    length = max(len(text), 1)
    if alpha / length < 0.45:
        return False
    if digits / length > 0.25:
        return False
    return not math_symbols / length > 0.20


def reference_like_paragraph(text: str) -> bool:
    if not re.match(r"^(?:\[\d+\]|\d+[.)])\s+", text):
        return False
    return bool(re.search(r"\b(?:19|20)\d{2}[a-z]?\b", text) or re.search(r"\bdoi\b|https?://", text, re.I))


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
