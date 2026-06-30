"""Text helpers for staged metadata refinement."""

from __future__ import annotations

import html
import re
from difflib import SequenceMatcher

from knowledge_base.scripts.refine_staged_arxiv_metadata.constants import (
    SENTENCE_LIKE_TAG_CLAUSE_RE,
    SENTENCE_LIKE_TAG_START_RE,
)


def clean_space(text: str | None) -> str:
    return re.sub(r"\s+", " ", html.unescape(text or "")).strip()


def sentence_like_tag(text: str) -> bool:
    text = clean_space(text)
    if not text:
        return False
    if SENTENCE_LIKE_TAG_START_RE.search(text):
        return True
    if SENTENCE_LIKE_TAG_CLAUSE_RE.search(text):
        return True
    words = re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text)
    return len(words) >= 7 and bool(
        re.search(r"\b(?:that|because|while|although|where|which|who|whose|when)\b", text, re.IGNORECASE)
    )


def bare_arxiv_id(arxiv_id: str | None) -> str:
    return re.sub(r"v\d+$", "", clean_space(arxiv_id))


def normalize_title(text: str | None) -> str:
    return re.sub(r"[^a-z0-9]+", " ", clean_space(text).lower()).strip()


def title_similarity(left: str, right: str) -> float:
    return SequenceMatcher(None, normalize_title(left), normalize_title(right)).ratio()
