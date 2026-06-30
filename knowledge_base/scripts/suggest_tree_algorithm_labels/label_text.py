"""Text heuristics for algorithm/tree label suggestions."""

import re
from pathlib import Path
from typing import Any

from knowledge_base.scripts.audit_metadata import find_algorithm_issues
from knowledge_base.scripts.suggest_tree_algorithm_labels.constants import (
    GENERIC_ALGORITHM_LABELS,
    ROMAN_PART_LABELS,
    STOP_WORDS,
    TYPE_WORDS,
    WORD_RE,
)


def clean_text(value: Any) -> str:
    return " ".join(str(value or "").split())


def words(value: str) -> list[str]:
    return WORD_RE.findall(clean_text(value).casefold())


def content_words(value: str) -> list[str]:
    return [word for word in words(value) if word not in STOP_WORDS]


def alnum_key(value: str) -> str:
    return "".join(words(value))


def stripped_type_words(value: str) -> list[str]:
    return [word for word in content_words(value) if word not in TYPE_WORDS]


def without_trailing_parenthetical(value: str) -> str:
    return re.sub(r"\s*\([^)]*\)\s*$", "", clean_text(value))


def is_title_like(value: str) -> bool:
    text = clean_text(value)
    return len(content_words(text)) >= 5 or ":" in text or "?" in text


def is_code_like(value: str) -> bool:
    text = clean_text(value)
    if not text or " " in text:
        return False

    core = re.sub(r"[^A-Za-z0-9]", "", text)
    if not core or len(core) > 14:
        return False

    alpha = [char for char in text if char.isalpha()]
    uppercase = [char for char in alpha if char.isupper()]
    if len(alpha) > 1 and len(uppercase) >= max(2, int(len(alpha) * 0.6)):
        return True
    if re.search(r"[0-9+_*]", text):
        return True
    return bool(len(alpha) > 1 and any(char.isupper() for char in alpha[1:]))


def algorithm_looks_invalid(algorithm: str) -> bool:
    text = clean_text(algorithm)
    folded = " ".join(words(text))
    core = re.sub(r"[^A-Za-z0-9]", "", text)
    tokens = words(text)
    if not core:
        return True
    if tokens and tokens[0] in STOP_WORDS:
        return True
    if folded in GENERIC_ALGORITHM_LABELS:
        return True
    if folded in ROMAN_PART_LABELS and text.isupper():
        return True
    return bool(len(core) <= 2 and not is_code_like(text))


def soft_equivalence_reason(tree_label: str, algorithm: str) -> str | None:
    if alnum_key(tree_label) == alnum_key(algorithm):
        return "Labels differ only by punctuation, case, or lightweight markup."

    if stripped_type_words(tree_label) == stripped_type_words(algorithm):
        return "Labels differ only by generic type words such as algorithm or method."

    tree_base = without_trailing_parenthetical(tree_label)
    if tree_base != clean_text(tree_label) and (
        alnum_key(tree_base) == alnum_key(algorithm) or stripped_type_words(tree_base) == stripped_type_words(algorithm)
    ):
        return "Tree label adds a parenthetical disambiguator to an otherwise equivalent label."

    return None


def phrase_in_text(phrase: str, text: str) -> bool:
    phrase = clean_text(phrase)
    if not phrase:
        return False
    escaped = re.escape(phrase).replace(r"\ ", r"\s+")
    return re.search(rf"(?<![A-Za-z0-9]){escaped}(?![A-Za-z0-9])", text, re.I) is not None


def algorithm_in_metadata_text(algorithm: str, data: dict[str, Any]) -> bool:
    tags = " ".join(str(tag) for tag in data.get("tags") or [])
    body = " ".join(clean_text(data.get(field)) for field in ("title", "abstract", "summary"))
    return phrase_in_text(algorithm, f"{body} {tags}")


def algorithm_in_tags(algorithm: str, data: dict[str, Any]) -> bool:
    return any(alnum_key(str(tag)) == alnum_key(algorithm) for tag in data.get("tags") or [])


def title_head(value: str) -> str | None:
    head = clean_text(value).split(":", 1)[0].strip()
    if head and head != clean_text(value) and len(content_words(head)) <= 6:
        return head
    return None


def text_introduces_algorithm(algorithm: str, data: dict[str, Any]) -> bool:
    text = " ".join(clean_text(data.get(field)) for field in ("title", "abstract", "summary"))
    algorithm_pattern = re.escape(clean_text(algorithm)).replace(r"\ ", r"\s+")
    intro = (
        r"\b(?:we|this\s+(?:paper|work|article|letter)|in\s+this\s+"
        r"(?:paper|work|article|letter))\s+(?:first\s+)?"
        r"(?:introduce|propose|present|develop|derive|formulate)\b"
    )
    method_word = r"(?:algorithm|method|approach|optimizer|planner|controller|" r"framework|tool|system)"
    patterns = (
        rf"^\s*{algorithm_pattern}\s*:",
        rf"{intro}[^.\n]{{0,180}}\b{algorithm_pattern}\b",
        rf"{intro}[^.\n]{{0,180}}\b{method_word}\s+" rf"(?:called\s+|named\s+)?{algorithm_pattern}\b",
        rf"\b(?:called|named|coined)\s+{algorithm_pattern}\b",
    )
    return any(re.search(pattern, text, re.I) for pattern in patterns)


def audit_suggested_algorithm(data: dict[str, Any], metadata_path: Path) -> str | None:
    for issue in find_algorithm_issues(metadata_path, data):
        if not issue.suggestion:
            continue
        match = re.search(r"for example '([^']+)'", issue.suggestion)
        if match:
            return match.group(1)
    return None


__all__ = [name for name in globals() if not (name.startswith("__") and name.endswith("__"))]
