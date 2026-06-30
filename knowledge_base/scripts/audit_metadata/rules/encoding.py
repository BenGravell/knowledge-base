"""Encoding and suspicious-character audit helpers."""

import re
import unicodedata
from pathlib import Path

from knowledge_base.scripts.audit_metadata.support.model import RULE_TEXT_MOJIBAKE, Issue

_MOJIBAKE_RE = re.compile(
    r"(?:[\u00c2-\u00df][\u0080-\u00bf]|"
    r"[\u00e0-\u00ef][\u0080-\u00bf]{2}|"
    r"[\u00f0-\u00f4][\u0080-\u00bf]{3}|"
    r"Ã(?=\s|$)|Â[\u0080-\u00ff]?|â[\u0080-\uffff]{1,2}|�)"
)
_C1_CONTROL_CHAR_RE = re.compile(r"[\u0080-\u009f]")
_TEXT_MOJIBAKE_ISSUE_PREFIX = "Contains likely mojibake/encoding artifact(s)"


def _is_unicode_noncharacter(char: str) -> bool:
    codepoint = ord(char)
    return 0xFDD0 <= codepoint <= 0xFDEF or codepoint & 0xFFFE == 0xFFFE


def _suspicious_text_char_descriptions(text: str) -> list[str]:
    descriptions: list[str] = []
    for char in text:
        if char in "\n\r\t":
            continue
        if char == "\ufffd":
            descriptions.append("U+FFFD REPLACEMENT CHARACTER")
            continue
        if _is_unicode_noncharacter(char):
            descriptions.append(f"U+{ord(char):04X} NONCHARACTER")
            continue

        category = unicodedata.category(char)
        if category in {"Cc", "Cf", "Cs", "Co", "Cn"}:
            name = unicodedata.name(char, "UNNAMED")
            descriptions.append(f"U+{ord(char):04X} {name}")

    return descriptions


def _mojibake_examples(text: str, *, limit: int = 5) -> list[str]:
    examples: list[str] = []
    seen: set[str] = set()
    for match in _MOJIBAKE_RE.finditer(text):
        value = match.group(0)
        if value in seen:
            continue
        examples.append(value)
        seen.add(value)
        if len(examples) >= limit:
            break
    return examples


def find_weird_text_character_issues(
    path: Path,
    field: str,
    text: str,
) -> list[Issue]:
    issues: list[Issue] = []
    char_descriptions = sorted(set(_suspicious_text_char_descriptions(text)))
    if char_descriptions:
        examples = ", ".join(char_descriptions[:5])
        if len(char_descriptions) > 5:
            examples += f", ... ({len(char_descriptions)} total)"
        issues.append(
            Issue(
                path,
                field,
                f"Contains suspicious Unicode character(s): {examples}",
                "Replace mojibake, replacement, private-use, zero-width, or control characters with clean text.",
            )
        )

    mojibake = _mojibake_examples(text)
    if mojibake:
        examples = ", ".join(repr(example) for example in mojibake)
        issues.append(
            Issue(
                path,
                field,
                f"{_TEXT_MOJIBAKE_ISSUE_PREFIX}: {examples}",
                "Replace with the correctly decoded source text.",
                rule=RULE_TEXT_MOJIBAKE,
            )
        )

    return issues


def _mojibake_byte(char: str) -> int | None:
    codepoint = ord(char)
    if codepoint <= 0xFF:
        return codepoint
    try:
        encoded = char.encode("cp1252")
    except UnicodeError:
        return None
    return encoded[0] if len(encoded) == 1 else None


def _decode_utf8_mojibake_text(text: str) -> tuple[str, int]:
    if not _mojibake_examples(text):
        return text, 0

    pieces: list[str] = []
    decoded = 0
    index = 0
    while index < len(text):
        leading_byte = _mojibake_byte(text[index])
        if leading_byte is None:
            byte_count = 0
        elif 0xC2 <= leading_byte <= 0xDF:
            byte_count = 2
        elif 0xE0 <= leading_byte <= 0xEF:
            byte_count = 3
        elif 0xF0 <= leading_byte <= 0xF4:
            byte_count = 4
        else:
            byte_count = 0

        token = text[index : index + byte_count]
        token_bytes = [byte for char in token for byte in [_mojibake_byte(char)] if byte is not None]
        if (
            byte_count
            and len(token) == byte_count
            and len(token_bytes) == byte_count
            and all(0x80 <= byte <= 0xBF for byte in token_bytes[1:])
        ):
            try:
                replacement = bytes(token_bytes).decode("utf-8")
            except UnicodeError:
                replacement = ""
            if replacement and not _C1_CONTROL_CHAR_RE.search(replacement):
                pieces.append(replacement)
                decoded += 1
                index += byte_count
                continue

        pieces.append(text[index])
        index += 1

    fixed = "".join(pieces)
    fixed, orphaned_grave_a = re.subn(r"Ã(?=\s|$)", "à", fixed)
    return fixed, decoded + orphaned_grave_a


def _decode_utf8_mojibake_controls(raw: str) -> tuple[str, int]:
    if not _C1_CONTROL_CHAR_RE.search(raw):
        return raw, 0
    return _decode_utf8_mojibake_text(raw)


__all__ = [
    "_C1_CONTROL_CHAR_RE",
    "_MOJIBAKE_RE",
    "_TEXT_MOJIBAKE_ISSUE_PREFIX",
    "_decode_utf8_mojibake_controls",
    "_decode_utf8_mojibake_text",
    "_is_unicode_noncharacter",
    "_mojibake_byte",
    "_mojibake_examples",
    "_suspicious_text_char_descriptions",
    "find_weird_text_character_issues",
]
