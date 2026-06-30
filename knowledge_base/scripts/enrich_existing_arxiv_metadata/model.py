"""Data model for arXiv Atom records."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ArxivRecord:
    arxiv_id: str
    title: str
    authors: list[str]
    year: int
    abstract: str
    doi: str
    journal_ref: str
    comment: str
    primary_category: str
    categories: list[str]
