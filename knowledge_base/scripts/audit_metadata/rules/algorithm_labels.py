"""Algorithm-label text helpers."""

import re
from functools import cache
from pathlib import Path
from typing import Any

from knowledge_base.scripts.audit_metadata.rules.algorithm_data import (
    _ALGORITHM_DESCRIPTIVE_WORDS,
    _ALGORITHM_EXPANDED_NAMES,
    _BARE_ALGORITHM_LABEL_ALLOWED_ENTRIES,
    _BROAD_ALGORITHM_FAMILY_LABELS,
    _BROAD_ALGORITHM_FAMILY_ORIGIN_ENTRIES,
    _URL_RE,
)
from knowledge_base.scripts.audit_metadata.support.text import _normalize_inline_text
from knowledge_base.utils.paper_ids import paper_id_from_metadata


def _algorithm_tokens(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9+_.*-]+", text)


def _algorithm_key(text: str) -> str:
    return re.sub(r"[^a-z0-9*]+", "", text.casefold())


def _algorithm_token_is_method_like(token: str) -> bool:
    alpha = re.sub(r"[^A-Za-z]", "", token)
    if not alpha:
        return bool(re.search(r"[0-9+_*.-]", token))
    if len(alpha) > 1 and alpha == alpha.upper():
        return True
    if len(alpha) > 1 and any(char.isupper() for char in alpha[1:]):
        return True
    if re.search(r"[0-9+_*]", token):
        return True
    return alpha[:1].isupper() and len(alpha) >= 3


def _algorithm_token_is_abbreviation_like(token: str) -> bool:
    alpha = re.sub(r"[^A-Za-z]", "", token)
    if len(alpha) > 1 and alpha == alpha.upper():
        return True
    if len(alpha) > 1 and any(char.isupper() for char in alpha[1:]):
        return True
    return bool(re.search(r"[0-9+_*]", token))


def _algorithm_label_is_bare_method_name(algorithm: str) -> bool:
    tokens = _algorithm_tokens(algorithm)
    if not tokens or len(tokens) > 3:
        return False

    folded_tokens = [token.casefold() for token in tokens]
    if len(tokens) > 1 and any(token in _ALGORITHM_DESCRIPTIVE_WORDS for token in folded_tokens):
        return False

    if len(tokens) > 1 and not any(_algorithm_token_is_abbreviation_like(token) for token in tokens):
        return False

    return any(_algorithm_token_is_method_like(token) for token in tokens)


def _phrase_search_pattern(phrase: str) -> str:
    escaped = re.escape(phrase)
    escaped = escaped.replace(r"\ ", r"\s+")
    return rf"(?<![A-Za-z0-9]){escaped}(?![A-Za-z0-9])"


@cache
def _cached_regex(pattern: str, flags: int = 0) -> re.Pattern[str]:
    return re.compile(pattern, flags)


@cache
def _algorithm_reference_names(algorithm: str) -> tuple[str, ...]:
    names = [algorithm]
    names.extend(_ALGORITHM_EXPANDED_NAMES.get(_algorithm_key(algorithm), ()))

    deduped: list[str] = []
    seen: set[str] = set()
    for name in names:
        normalized = " ".join(name.split()).casefold()
        if not normalized or normalized in seen:
            continue
        deduped.append(name)
        seen.add(normalized)
    return tuple(deduped)


@cache
def _algorithm_mention_patterns(algorithm: str) -> tuple[re.Pattern[str], ...]:
    return tuple(re.compile(_phrase_search_pattern(name), re.I) for name in _algorithm_reference_names(algorithm))


def _text_mentions_algorithm(algorithm: str, text: str) -> bool:
    return any(pattern.search(text) for pattern in _algorithm_mention_patterns(algorithm))


def _algorithm_context_text(data: dict[str, Any]) -> tuple[str, str]:
    title = str(data.get("title") or "").strip()
    body = " ".join(str(data.get(field) or "") for field in ("title", "abstract", "summary"))
    body = _URL_RE.sub("", body)
    return title, _normalize_inline_text(body)


def _algorithm_label_is_broad_family_name(algorithm: str) -> bool:
    return _algorithm_key(algorithm) in _BROAD_ALGORITHM_FAMILY_LABELS


def _algorithm_label_is_known_origin_entry(
    path: Path,
    data: dict[str, Any],
    algorithm: str,
) -> bool:
    paper_id = paper_id_from_metadata(path, data)
    return (
        _algorithm_key(algorithm),
        paper_id,
    ) in _BROAD_ALGORITHM_FAMILY_ORIGIN_ENTRIES


def _algorithm_label_is_allowed_entry(
    path: Path,
    data: dict[str, Any],
    algorithm: str,
) -> bool:
    paper_id = paper_id_from_metadata(path, data)
    return (
        _algorithm_key(algorithm),
        paper_id,
    ) in _BARE_ALGORITHM_LABEL_ALLOWED_ENTRIES
