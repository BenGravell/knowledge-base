"""Tag casing and article suggestions."""

import re
from typing import Any

from knowledge_base.scripts.audit_metadata.rules.tag_data import (
    _COMMON_SHORT_TAG_WORDS,
    _TAG_LEADING_ARTICLES,
    _TAG_PROPER_NAME_WORDS,
)
from knowledge_base.scripts.audit_metadata.rules.tag_text import _tag_part_is_abbreviation_or_mixed
from knowledge_base.scripts.audit_metadata.rules.title import _split_token_punctuation
from knowledge_base.scripts.audit_metadata.support.slugs import _extract_last_name


def _author_last_name_tag_proper_words(data: dict[str, Any]) -> dict[str, str]:
    authors = data.get("authors")
    if not isinstance(authors, list):
        return {}

    proper_words: dict[str, str] = {}
    for author in authors:
        last_name = _extract_last_name(str(author).strip())
        for word in re.findall(r"[A-Za-z]+", last_name):
            if not word:
                continue
            proper_words.setdefault(word.casefold(), word[:1].upper() + word[1:])
    return proper_words


def _tag_proper_name_casing(
    core: str,
    proper_name_words: dict[str, str] | None = None,
) -> str | None:
    folded = core.casefold()
    if proper_name_words is not None and folded in proper_name_words:
        return proper_name_words[folded]
    return _TAG_PROPER_NAME_WORDS.get(folded)


def _tag_part_is_ordinary_english(
    core: str,
    proper_name_words: dict[str, str] | None = None,
) -> bool:
    if _tag_proper_name_casing(core, proper_name_words) is not None:
        return False
    if _tag_part_is_abbreviation_or_mixed(core):
        return False
    folded = core.casefold()
    return len(folded) >= 5 or folded in _COMMON_SHORT_TAG_WORDS


def _case_tag_part(
    core: str,
    *,
    seen_any_word: bool,
    proper_name_words: dict[str, str] | None = None,
) -> str:
    proper_name = _tag_proper_name_casing(core, proper_name_words)
    if proper_name is not None:
        return proper_name
    if not _tag_part_is_ordinary_english(core, proper_name_words):
        return core
    if seen_any_word:
        return core.casefold()
    return core[:1].upper() + core[1:].casefold()


def _tag_token_has_nonordinary_hyphen_part(token: str) -> bool:
    if "-" not in token:
        return False
    for part in token.split("-"):
        _, core, _ = _split_token_punctuation(part)
        if core and _tag_part_is_abbreviation_or_mixed(core):
            return True
    return False


def _suggest_tag_capitalization(
    tag: str,
    proper_name_words: dict[str, str] | None = None,
) -> str:
    tokens = tag.split()
    if not tokens:
        return tag

    cased_tokens: list[str] = []
    seen_any_word = False
    for token in tokens:
        if _tag_token_has_nonordinary_hyphen_part(token):
            lead, core, _ = _split_token_punctuation(token)
            if re.search(r"[A-Za-z]", core):
                seen_any_word = True
            cased_tokens.append(token)
            continue

        pieces = re.split(r"(-)", token)
        cased_pieces: list[str] = []
        for piece in pieces:
            if piece == "-":
                cased_pieces.append(piece)
                continue
            lead, core, tail = _split_token_punctuation(piece)
            if not core:
                cased_pieces.append(piece)
                continue

            cased_core = _case_tag_part(
                core,
                seen_any_word=seen_any_word,
                proper_name_words=proper_name_words,
            )
            if re.search(r"[A-Za-z]", core):
                seen_any_word = True
            cased_pieces.append(lead + cased_core + tail)

        cased_tokens.append("".join(cased_pieces))

    return " ".join(cased_tokens)


def _suggest_tag_without_leading_article(
    tag: str,
    proper_name_words: dict[str, str] | None = None,
) -> str | None:
    match = re.match(
        r"^(?P<article>a|an|and|as|i|in|or|recent|such|the|we)\b\s+(?P<rest>.+)$",
        tag,
        re.I,
    )
    if not match:
        return None
    article = match.group("article").casefold()
    if article not in _TAG_LEADING_ARTICLES:
        return None
    rest = match.group("rest").strip()
    return _suggest_tag_capitalization(rest, proper_name_words) if rest else None


__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
