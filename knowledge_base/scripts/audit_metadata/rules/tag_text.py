"""Small tag text helpers."""

import re

from knowledge_base.scripts.audit_metadata.rules.tag_data import (
    _FORBIDDEN_TAGS,
    _LONG_TAG_ALLOWLIST,
    _SENTENCE_LIKE_TAG_CLAUSE_RE,
    _SENTENCE_LIKE_TAG_START_RE,
)
from knowledge_base.scripts.audit_metadata.support.model import Issue


def _issue_rule_or_legacy(issue: Issue, rule: str, legacy_match: bool) -> bool:
    return issue.rule == rule or (issue.rule is None and legacy_match)


def _tag_issue_index(issue: Issue) -> int | None:
    if issue.index is not None:
        return issue.index
    match = re.search(r"tags\[(\d+)\]", issue.message)
    if not match:
        return None
    return int(match.group(1))


def _tag_word_count(tag: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", tag))


def _sentence_like_tag_reason(tag: str) -> str | None:
    stripped = " ".join(tag.split())
    if not stripped:
        return None

    if _SENTENCE_LIKE_TAG_START_RE.search(stripped):
        return "starts like prose copied from an abstract"
    if _SENTENCE_LIKE_TAG_CLAUSE_RE.search(stripped):
        return "contains a sentence-like claim clause"
    if stripped.endswith((".", "!", "?")) and _tag_word_count(stripped) >= 4:
        return "ends like a sentence"
    if _tag_word_count(stripped) >= 7 and re.search(
        r"\b(?:that|because|while|although|where|which|who|whose|when)\b",
        stripped,
        re.IGNORECASE,
    ):
        return "looks like a long clause, not a tag"

    return None


def _normalized_tag_for_duplicate_check(tag: str) -> str:
    return " ".join(tag.split()).casefold()


def _normalized_tag_for_forbidden_check(tag: str) -> str:
    return re.sub(r"[\s-]+", " ", tag).strip().casefold()


def _forbidden_tag_reason(tag: str) -> str | None:
    return _FORBIDDEN_TAGS.get(_normalized_tag_for_forbidden_check(tag))


def _is_long_tag_allowed(tag: str) -> bool:
    return _normalized_tag_for_duplicate_check(tag) in _LONG_TAG_ALLOWLIST


def _tag_part_is_abbreviation_or_mixed(core: str) -> bool:
    alpha = re.sub(r"[^A-Za-z]", "", core)
    if not alpha:
        return True
    if core != alpha:
        return True
    if len(alpha) > 1 and alpha == alpha.upper():
        return True
    return len(alpha) > 1 and any(char.isupper() for char in alpha[1:])


__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
