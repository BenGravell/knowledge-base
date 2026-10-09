"""Authoritative paper metadata fields, normalization, and audit requirements."""

from __future__ import annotations

import re
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator

from knowledge_base.utils.arxiv_ids import normalize_arxiv_id

MetadataYear = int | str

# Valid values for the "type" field of a research item.
VALID_TYPES: list[str] = [
    "Conference Paper",
    "Journal Paper",
    "Workshop Paper",
    "Preprint",
    "Technical Report",
    "PhD Dissertation",
    "Master's Thesis",
    "Survey Paper",
    "Book",
    "Patent",
    "Blog Post",
    "Other",
]

# Audit status lifecycle for metadata.yml files.
AUDIT_STATUS_FIELD = "audit_status"

# Audit lifecycle statuses (in order):
#  raw       - auto-generated/imported, never manually reviewed
#  partial   - some fields manually reviewed or corrected, but not complete
#  reviewed  - all key fields verified, good summary present
VALID_AUDIT_STATUSES: tuple[str, ...] = ("raw", "partial", "reviewed")

DEFAULT_AUDIT_STATUS = "raw"


def clean_scalar(value: Any) -> str:
    return str(value or "").strip()


def clean_doi(doi: Any) -> str:
    return re.sub(
        r"^https?://(?:dx\.)?doi\.org/",
        "",
        clean_scalar(doi),
        flags=re.IGNORECASE,
    )


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


class MetadataRecord(BaseModel):
    """Normalized metadata with tolerant defaults for incomplete records."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    title: str = Field(
        default="",
        description="Full paper title, copied verbatim and written in title case. Use a double-quoted YAML string.",
        json_schema_extra={"audit_required": True},
    )
    algorithm: str = Field(
        default="",
        description="Short name of the primary algorithm, technique, or method introduced by the paper.",
    )
    authors: tuple[str, ...] = Field(
        default=(),
        description="Authors in paper order. Use full names, including middle initials when available; prefer English letters for search.",
        json_schema_extra={"audit_required": True},
    )
    year: MetadataYear = Field(
        default="",
        description="Year of first publication, using the earliest arXiv version when available. This is not necessarily the formal venue publication year, which has no separate field yet.",
        json_schema_extra={"audit_required": True},
    )
    source: str = Field(
        default="",
        description="Most official venue, usually a conference or journal name. Omit years.",
    )
    type: str = Field(
        default="",
        description="Research item type.",
        json_schema_extra={"audit_required": True, "enum": ["", *VALID_TYPES]},
    )
    doi: str = Field(
        default="",
        description="DOI of the formally published item, never the arXiv DOI. DOI URL prefixes are removed when loading.",
    )
    arxiv_id: str = Field(
        default="",
        description="Bare arXiv ID as a double-quoted YAML string, or blank if no clear match exists. Loading removes URL prefixes and version suffixes and preserves old-style archive prefixes.",
    )
    tags: tuple[str, ...] = Field(
        default=(),
        description="Short, commonly searched phrases, one per line. Aim for 5–20 tags and capitalize the first word.",
    )
    abstract: str = Field(
        default="",
        description="Full verbatim abstract. Prefer arXiv, then the formal publication, then another available source. Leave blank only when no abstract exists.",
        json_schema_extra={"audit_required": True},
    )
    summary: str = Field(
        default="",
        description="Short external-observer summary of the main contributions and important secondary contributions.",
    )
    link: str = Field(
        default="",
        description="Primary paper link. Prefer the arXiv PDF when available, then another freely openable paper link; use a paywalled link as a last resort.",
    )
    links_alt: tuple[str, ...] = Field(
        default=(),
        description="Alternate links, with freely openable paper links before paywalled links. May also include supporting code, packages, and project pages.",
    )
    audit_status: str = Field(
        default="",
        description="Audit lifecycle: raw means imported and not manually reviewed; partial means some fields checked or corrected; reviewed means all key fields verified with a good summary. Agents may set raw or partial, never reviewed.",
        json_schema_extra={"audit_required": True, "enum": ["", *VALID_AUDIT_STATUSES]},
    )

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


# Preserve field order for YAML writers and derive audit requirements from the model.
VALID_FIELDS: tuple[str, ...] = tuple(MetadataRecord.model_fields)
REQUIRED_FIELDS: tuple[str, ...] = tuple(
    name
    for name, field in MetadataRecord.model_fields.items()
    if isinstance(field.json_schema_extra, dict) and field.json_schema_extra.get("audit_required")
)
