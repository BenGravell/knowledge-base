"""Text normalization helpers."""

from __future__ import annotations

import re

from knowledge_base.utils.arxiv_utils import normalize_arxiv_id


def clean_space(text: str | None) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def bare_arxiv_id(arxiv_id: str | None) -> str:
    return re.sub(r"v\d+$", "", normalize_arxiv_id(arxiv_id))


def title_case_ascii(title: str) -> str:
    # Keep acronyms/math-ish tokens intact while matching the repository's
    # title-case expectation closely enough for audit.
    small = {
        "a",
        "an",
        "and",
        "as",
        "at",
        "by",
        "for",
        "from",
        "in",
        "into",
        "of",
        "on",
        "or",
        "the",
        "to",
        "via",
        "with",
        "without",
    }
    words = re.split(r"(\s+)", clean_space(title))
    cased: list[str] = []
    word_positions = [i for i, token in enumerate(words) if token.strip()]
    first_last = {word_positions[0], word_positions[-1]} if word_positions else set()
    for i, token in enumerate(words):
        if not token.strip():
            cased.append(token)
            continue
        bare = token.strip(",:;()[]{}")
        if any(ch.isupper() for ch in bare[1:]) or any(ch.isdigit() for ch in bare) or "\\" in bare or "$" in bare:
            cased.append(token)
            continue
        lower = token.lower()
        if i not in first_last and lower in small:
            cased.append(lower)
        else:
            cased.append(token[:1].upper() + token[1:].lower())
    return "".join(cased)
