"""Author audit and repair helpers."""

import re
import unicodedata

from knowledge_base.scripts.audit_metadata.rules.author_data import (
    _AUTHOR_ASCII_TRANSLATION,
    _AUTHOR_SUFFIX_RE,
    _KNOWN_INDIVIDUAL_AUTHOR_NAMES,
    _KNOWN_SINGLE_AUTHOR_REPLACEMENTS,
    _NON_INDIVIDUAL_AUTHOR_PATTERNS,
)
from knowledge_base.scripts.audit_metadata.rules.encoding import (
    _decode_utf8_mojibake_text,
    _mojibake_examples,
    _suspicious_text_char_descriptions,
)
from knowledge_base.scripts.audit_metadata.support.text import _normalize_inline_text

_AUTHOR_MOJIBAKE_ISSUE_PREFIX = "Author entries contain suspicious Unicode character"
_AUTHOR_ASCII_NORMALIZATION_ISSUE_PREFIX = "Author entries are not ASCII-normalized"
_NON_INDIVIDUAL_AUTHOR_ISSUE_PREFIX = "Author entries appear to be non-individual names"


def _non_individual_author_reason(author: str) -> str | None:
    stripped = " ".join(author.split()).strip(" .")
    if not stripped:
        return None
    if stripped.casefold() in _KNOWN_INDIVIDUAL_AUTHOR_NAMES:
        return None
    for reason, pattern in _NON_INDIVIDUAL_AUTHOR_PATTERNS:
        if pattern.search(stripped):
            return reason
    if not re.search(r"[A-Za-z]", stripped):
        return "non-name author token"
    if len(stripped.split()) == 1:
        return "single-token author"
    return None


def _looks_like_author_suffix(segment: str) -> bool:
    cleaned = segment.strip().strip(".")
    return bool(cleaned and _AUTHOR_SUFFIX_RE.fullmatch(cleaned))


def _looks_like_last_first_author(author: str) -> bool:
    """Detect likely "Last, First" author entries while allowing suffix commas."""
    comma_parts = [part.strip() for part in author.split(",")]
    if len(comma_parts) < 2 or not comma_parts[0]:
        return False

    for part in comma_parts[1:]:
        if not part or _looks_like_author_suffix(part):
            continue
        return bool(re.search(r"[A-Za-z]", comma_parts[0]) and re.search(r"[A-Za-z]", part))

    return False


def _suspicious_author_char_descriptions(author: str) -> list[str]:
    return _suspicious_text_char_descriptions(author) + [
        f"likely mojibake {example!r}" for example in _mojibake_examples(author)
    ]


def _fold_author_name_to_ascii(author: str) -> str:
    translated = author.translate(_AUTHOR_ASCII_TRANSLATION)
    normalized = unicodedata.normalize("NFKD", translated)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    return _normalize_inline_text(ascii_text)


def _author_ascii_normalization(author: str) -> str:
    decoded_author, _ = _decode_utf8_mojibake_text(author)
    return _fold_author_name_to_ascii(decoded_author)


def _author_ascii_normalization_issues(authors: list[object]) -> dict[int, str]:
    normalization_issues: dict[int, str] = {}
    for i, author in enumerate(authors):
        if not isinstance(author, str):
            continue
        normalized = _author_ascii_normalization(author)
        if normalized and normalized != author:
            normalization_issues[i] = normalized
    return normalization_issues


def _looks_like_split_author_token(author: object) -> bool:
    if not isinstance(author, str):
        return False
    return bool(re.fullmatch(r"[A-Z][A-Za-z'-]*", author.strip()))


def _is_removable_collective_author(author: object) -> bool:
    if not isinstance(author, str):
        return False
    reason = _non_individual_author_reason(author)
    return bool(reason and reason != "single-token author")


def _repair_non_individual_author_list(authors_raw: list[object]) -> tuple[list[object], int]:
    authors: list[object] = []
    changed = 0
    index = 0
    while index < len(authors_raw):
        author = authors_raw[index]
        if isinstance(author, str) and author in _KNOWN_SINGLE_AUTHOR_REPLACEMENTS:
            authors.append(_KNOWN_SINGLE_AUTHOR_REPLACEMENTS[author])
            changed += 1
            index += 1
            continue

        if len(authors_raw) > 1 and _is_removable_collective_author(author):
            changed += 1
            index += 1
            continue

        if (
            index + 1 < len(authors_raw)
            and _looks_like_split_author_token(author)
            and _looks_like_split_author_token(authors_raw[index + 1])
        ):
            combined = f"{str(author).strip()} {str(authors_raw[index + 1]).strip()}"
            if _non_individual_author_reason(combined) is None:
                authors.append(combined)
                changed += 1
                index += 2
                continue

        authors.append(author)
        index += 1

    return authors, changed


__all__ = [
    "_AUTHOR_ASCII_NORMALIZATION_ISSUE_PREFIX",
    "_AUTHOR_MOJIBAKE_ISSUE_PREFIX",
    "_NON_INDIVIDUAL_AUTHOR_ISSUE_PREFIX",
    "_author_ascii_normalization",
    "_author_ascii_normalization_issues",
    "_fold_author_name_to_ascii",
    "_is_removable_collective_author",
    "_looks_like_author_suffix",
    "_looks_like_last_first_author",
    "_looks_like_split_author_token",
    "_non_individual_author_reason",
    "_repair_non_individual_author_list",
    "_suspicious_author_char_descriptions",
]
