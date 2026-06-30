"""Tag normalization and validation rules for metadata audits."""

# ruff: noqa: F811

from pathlib import Path
from typing import Any

from knowledge_base.scripts.audit_metadata.rules.tag_casing import (
    _author_last_name_tag_proper_words,
    _suggest_tag_capitalization,
    _suggest_tag_without_leading_article,
)
from knowledge_base.scripts.audit_metadata.rules.tag_data import (
    _DATABASE_DUPLICATE_TAG_MESSAGE_PREFIX,
    _MAX_TAG_WORDS,
    _PLURAL_DUPLICATE_TAG_MESSAGE_PREFIX,
    _TAG_DATABASE_ISSUE_PREFIX,
    _TAG_DATABASE_MISSING_ISSUE_PREFIX,
)
from knowledge_base.scripts.audit_metadata.rules.tag_database import (
    _MAX_TAG_WORDS,
    _TAG_DATABASE_MISSING_ISSUE_PREFIX,
    _author_last_name_tag_proper_words,
    _forbidden_tag_reason,
    _is_long_tag_allowed,
    _sentence_like_tag_reason,
    _suggest_tag_capitalization,
    _suggest_tag_without_leading_article,
    _tag_database_canonical,
    _tag_database_error,
    _tag_word_count,
)
from knowledge_base.scripts.audit_metadata.rules.tag_duplicates import (
    _database_duplicate_tag_fix_suggestion,
    _database_tag_duplicate_groups,
    _normalized_tag_for_duplicate_check,
    _plural_duplicate_tag_fix_suggestion,
    _plural_duplicate_tag_groups,
    _tag_database_canonical,
)
from knowledge_base.scripts.audit_metadata.rules.tag_text import (
    _forbidden_tag_reason,
    _is_long_tag_allowed,
    _normalized_tag_for_duplicate_check,
    _sentence_like_tag_reason,
    _tag_word_count,
)
from knowledge_base.scripts.audit_metadata.support.model import (
    RULE_DATABASE_DUPLICATE_TAG,
    RULE_DUPLICATE_TAG,
    RULE_FORBIDDEN_TAG,
    RULE_PLURAL_DUPLICATE_TAG,
    RULE_TAG_DATABASE_MISSING,
    RULE_TAG_VALUE,
    Issue,
    Path,
)
from knowledge_base.utils.normalization_db import expand_tag_acronyms


def find_tag_issues(path: Path, data: dict[str, Any]) -> list["Issue"]:
    tags = data.get("tags")
    if tags in (None, ""):
        return []
    if not isinstance(tags, list):
        return [Issue(path, "tags", "Must be a list")]

    issues: list[Issue] = []
    tag_indexes: dict[str, list[int]] = {}
    tag_display: dict[str, str] = {}
    proper_name_words = _author_last_name_tag_proper_words(data)
    tag_db_error = _tag_database_error()
    if tag_db_error is not None:
        issues.append(
            Issue(
                path,
                "tags",
                tag_db_error,
                "Run `python knowledge_base/scripts/build_normalization_db.py --only tags` from the repo root.",
            )
        )
    for index, tag_raw in enumerate(tags):
        tag = str(tag_raw).strip()
        normalized_tag = _normalized_tag_for_duplicate_check(tag)
        if normalized_tag:
            tag_indexes.setdefault(normalized_tag, []).append(index)
            tag_display.setdefault(normalized_tag, tag)

        if normalized_tag and tag_db_error is None:
            canonical_tag = _tag_database_canonical(tag)
            if canonical_tag is None:
                expanded = expand_tag_acronyms(tag)
                suggestion = (
                    expanded
                    if expanded != tag
                    else f"Add {tag!r} to normalization/tags.yml as a canonical tag or alias."
                )
                issues.append(
                    Issue(
                        path,
                        "tags",
                        f"{_TAG_DATABASE_MISSING_ISSUE_PREFIX} at tags[{index}]: {tag!r}",
                        suggestion,
                        rule=RULE_TAG_DATABASE_MISSING,
                        index=index,
                    )
                )
            elif canonical_tag != tag:
                issues.append(
                    Issue(
                        path,
                        "tags",
                        f"{_TAG_DATABASE_ISSUE_PREFIX} at tags[{index}]: {tag!r}",
                        canonical_tag,
                        rule=RULE_TAG_VALUE,
                        index=index,
                    )
                )

        forbidden_reason = _forbidden_tag_reason(tag)
        if forbidden_reason:
            issues.append(
                Issue(
                    path,
                    "tags",
                    f"Forbidden tag at tags[{index}]: {tag!r} ({forbidden_reason})",
                    "Remove this tag.",
                    rule=RULE_FORBIDDEN_TAG,
                    index=index,
                )
            )
            continue

        word_count = _tag_word_count(tag)
        if word_count > _MAX_TAG_WORDS and not _is_long_tag_allowed(tag):
            issues.append(
                Issue(
                    path,
                    "tags",
                    f"Wordy tag at tags[{index}] has {word_count} words: {tag!r}",
                    f"Shorten to {_MAX_TAG_WORDS} words or fewer.",
                )
            )

        without_article = _suggest_tag_without_leading_article(tag, proper_name_words)
        if without_article is not None:
            issues.append(
                Issue(
                    path,
                    "tags",
                    f"Tag starts with an article at tags[{index}]: {tag!r}",
                    without_article,
                    rule=RULE_TAG_VALUE,
                    index=index,
                )
            )
        else:
            suggested_tag = _suggest_tag_capitalization(tag, proper_name_words)
            if suggested_tag != tag:
                issues.append(
                    Issue(
                        path,
                        "tags",
                        f"Tag is not in capital case at tags[{index}]: {tag!r}",
                        suggested_tag,
                        rule=RULE_TAG_VALUE,
                        index=index,
                    )
                )

        reason = _sentence_like_tag_reason(tag)
        if reason:
            issues.append(
                Issue(
                    path,
                    "tags",
                    f"Sentence-like debris in tags[{index}]: {tag!r} ({reason})",
                    "Replace with a short pattern-matched phrase, or remove the tag.",
                )
            )

    duplicate_tags = {key: indexes for key, indexes in tag_indexes.items() if len(indexes) > 1}
    if duplicate_tags:
        examples = ", ".join(
            f"{tag_display[key]!r} at indexes {indexes}" for key, indexes in list(duplicate_tags.items())[:6]
        )
        if len(duplicate_tags) > 6:
            examples += f", ... ({len(duplicate_tags)} total)"
        issues.append(
            Issue(
                path,
                "tags",
                f"Duplicate tag value(s): {examples}",
                "Remove duplicate tags or merge near-identical spellings into one canonical tag.",
                rule=RULE_DUPLICATE_TAG,
            )
        )

    plural_duplicate_tags = _plural_duplicate_tag_groups(tags)
    if plural_duplicate_tags:
        examples = ", ".join(
            ", ".join(f"{str(tags[index]).strip()!r} at index {index}" for index in indexes)
            for indexes in list(plural_duplicate_tags.values())[:6]
        )
        if len(plural_duplicate_tags) > 6:
            examples += f", ... ({len(plural_duplicate_tags)} total)"
        issues.append(
            Issue(
                path,
                "tags",
                f"{_PLURAL_DUPLICATE_TAG_MESSAGE_PREFIX}: {examples}",
                _plural_duplicate_tag_fix_suggestion(tags, plural_duplicate_tags),
                rule=RULE_PLURAL_DUPLICATE_TAG,
            )
        )

    if tag_db_error is None:
        database_duplicate_tags = _database_tag_duplicate_groups(tags)
        if database_duplicate_tags:
            examples = ", ".join(
                ", ".join(f"{str(tags[index]).strip()!r} at index {index}" for index in indexes)
                for indexes in list(database_duplicate_tags.values())[:6]
            )
            if len(database_duplicate_tags) > 6:
                examples += f", ... ({len(database_duplicate_tags)} total)"
            issues.append(
                Issue(
                    path,
                    "tags",
                    f"{_DATABASE_DUPLICATE_TAG_MESSAGE_PREFIX}: {examples}",
                    _database_duplicate_tag_fix_suggestion(tags, database_duplicate_tags),
                    rule=RULE_DATABASE_DUPLICATE_TAG,
                )
            )

    return issues


__all__ = [name for name in globals() if not (name.startswith("__") and name.endswith("__"))]
