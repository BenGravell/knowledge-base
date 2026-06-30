"""Cue-pattern helpers for algorithm-label validation."""

import re
from functools import cache

from knowledge_base.scripts.audit_metadata.rules.algorithm_data import (
    _ALGORITHM_INTRO_VERB_RE,
    _ALGORITHM_RELATIONAL_CUES,
    _BROAD_ALGORITHM_FAMILY_CUES,
    _BROAD_ALGORITHM_FAMILY_LABELS,
)
from knowledge_base.scripts.audit_metadata.rules.algorithm_labels import (
    _algorithm_key,
    _algorithm_label_is_broad_family_name,
    _algorithm_reference_names,
    _cached_regex,
    _phrase_search_pattern,
    _text_mentions_algorithm,
)


@cache
def _algorithm_intro_patterns(algorithm: str) -> tuple[tuple[str, str, int], ...]:
    algorithm_is_broad = _algorithm_key(algorithm) in _BROAD_ALGORITHM_FAMILY_LABELS
    patterns: list[tuple[str, str, int]] = []
    for name in _algorithm_reference_names(algorithm):
        name_pattern = _phrase_search_pattern(name)
        patterns.extend(
            (
                ("title", rf"^\s*(?:the\s+)?{name_pattern}\s*$", re.I),
                (
                    "title",
                    rf"^\s*{name_pattern}\s*:\s*(?:a|an|the)?\s*"
                    rf"(?:new|novel)?\s*(?:algorithm|method|approach|optimizer|"
                    rf"planner|controller|framework|tool)\b",
                    re.I,
                ),
                ("title", rf"^\s*{name_pattern}\s*:", re.I),
            )
        )
        if not algorithm_is_broad:
            patterns.extend(
                (
                    (
                        "title",
                        rf"^\s*(?:[A-Z][A-Za-z0-9&./+-]*\s+){{1,3}}" rf"{name_pattern}\s*:",
                        0,
                    ),
                    (
                        "title",
                        rf"^\s*[^:\n]{{0,120}}\(\s*{name_pattern}\s*\)\s*:",
                        re.I,
                    ),
                    (
                        "title",
                        rf"^\s*(?:the\s+)?{name_pattern}\s+" rf"(?:for|in|via|using|with|to)\b",
                        re.I,
                    ),
                )
            )
        patterns.extend(
            (
                (
                    "title",
                    rf"^\s*(?:{_ALGORITHM_INTRO_VERB_RE})\s+"
                    rf"(?:(?:a|an|the|our|new|novel|simple|generalized)\s+)*"
                    rf"{name_pattern}\b",
                    re.I,
                ),
                (
                    "text",
                    rf"(?:^|[.!?]\s+)(?:{_ALGORITHM_INTRO_VERB_RE})\s+"
                    rf"(?:(?:a|an|the|our|new|novel|simple|generalized)\s+)*"
                    rf"{name_pattern}\b",
                    re.I,
                ),
                (
                    "text",
                    rf"\b(?:we|this\s+(?:paper|work|article|letter)|in\s+this\s+"
                    rf"(?:paper|work|article|letter|thesis))\s+(?:first\s+)?"
                    rf"(?:{_ALGORITHM_INTRO_VERB_RE})\s+"
                    rf"(?:(?:a|an|the|our|new|novel|simple|generalized)\s+)*"
                    rf"{name_pattern}\b",
                    re.I,
                ),
                (
                    "text",
                    rf"\b(?:we|this\s+(?:paper|work|article|letter)|in\s+this\s+"
                    rf"(?:paper|work|article|letter))\s+(?:first\s+)?"
                    rf"(?:{_ALGORITHM_INTRO_VERB_RE})\b"
                    rf"[^.\n]{{0,140}}\b(?:algorithm|method|approach|optimizer|"
                    rf"planner|controller|framework|tool|system)\s+(?:called\s+|named\s+)?"
                    rf"{name_pattern}\b",
                    re.I,
                ),
                (
                    "text",
                    rf"\b(?:we|this\s+(?:paper|work|article|letter)|in\s+this\s+"
                    rf"(?:paper|work|article|letter|thesis))\s+(?:first\s+)?"
                    rf"(?:{_ALGORITHM_INTRO_VERB_RE})\b[^.\n]{{0,220}}"
                    rf"\(\s*{name_pattern}\s*\)",
                    re.I,
                ),
                (
                    "text",
                    rf"{name_pattern}[^.\n]{{0,120}}\b(?:algorithm|method|approach|"
                    rf"optimizer|planner|controller|framework|tool|system)\b"
                    rf"[^.\n]{{0,80}}\b(?:is|are|was|were)\s+"
                    rf"(?:introduced|proposed|presented|developed|derived|formulated)\b",
                    re.I,
                ),
                ("text", rf"\b(?:called|named|coined)\s+{name_pattern}\b", re.I),
                ("text", rf"\bdenoted\s+by\s+{name_pattern}", re.I),
                (
                    "text",
                    rf"\b(?:which|that)\s+we\s+(?:call|name|coin)\b" rf"[^.\n]{{0,120}}\(\s*{name_pattern}\s*\)",
                    re.I,
                ),
            )
        )
        if not algorithm_is_broad:
            patterns.append(
                (
                    "text",
                    rf"\b(?:our|the)\s+[^.\n]{{0,100}}\(\s*{name_pattern}\s*\)",
                    re.I,
                )
            )
        patterns.append(
            (
                "text",
                rf"\b(?:the\s+)?result\s+is\s+{name_pattern}\s*,\s*(?:a|an)\s+"
                rf"[^.\n]{{0,120}}\b(?:algorithm|method|approach|framework|"
                rf"model|network|system)\b",
                re.I,
            )
        )
    return tuple(patterns)


def _text_introduces_algorithm_label(algorithm: str, title: str, text: str) -> bool:
    for target, pattern, flags in _algorithm_intro_patterns(algorithm):
        if _cached_regex(pattern, flags).search(title if target == "title" else text):
            return True
    return False


@cache
def _algorithm_issue_cue_patterns(algorithm: str) -> tuple[tuple[str, str, str], ...]:
    return tuple(
        (
            reason,
            suggestion_template,
            pattern_template.replace("{name}", _phrase_search_pattern(name)),
        )
        for name in _algorithm_reference_names(algorithm)
        for reason, pattern_template, suggestion_template in _ALGORITHM_RELATIONAL_CUES
    )


def _algorithm_issue_cue(
    algorithm: str,
    title: str,
    context: str,
    *,
    mentions_algorithm: bool | None = None,
) -> tuple[str, str] | None:
    if mentions_algorithm is None:
        mentions_algorithm = _text_mentions_algorithm(algorithm, context)
    if not mentions_algorithm:
        return None

    search_chunks = [title, context]
    for reason, suggestion_template, pattern in _algorithm_issue_cue_patterns(algorithm):
        compiled = _cached_regex(pattern, re.I)
        if any(compiled.search(chunk) for chunk in search_chunks):
            return reason, suggestion_template.format(algorithm=algorithm)

    return None


@cache
def _broad_algorithm_family_cue_patterns(algorithm: str) -> tuple[tuple[str, str], ...]:
    return tuple(
        (
            reason,
            pattern_template.replace("{name}", _phrase_search_pattern(name)),
        )
        for name in _algorithm_reference_names(algorithm)
        for reason, pattern_template in _BROAD_ALGORITHM_FAMILY_CUES
    )


def _broad_algorithm_family_issue_cue(
    algorithm: str,
    title: str,
    context: str,
    *,
    mentions_algorithm: bool | None = None,
) -> str | None:
    if not _algorithm_label_is_broad_family_name(algorithm):
        return None
    if mentions_algorithm is None:
        mentions_algorithm = _text_mentions_algorithm(algorithm, context)
    if not mentions_algorithm:
        return None
    if _text_introduces_algorithm_label(algorithm, title, context):
        return None

    search_chunks = [title, context]
    for reason, pattern in _broad_algorithm_family_cue_patterns(algorithm):
        compiled = _cached_regex(pattern, re.I)
        if any(compiled.search(chunk) for chunk in search_chunks):
            return reason

    return None
