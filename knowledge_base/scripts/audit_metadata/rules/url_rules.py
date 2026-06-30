"""URL, source-year, and garbled-markup audit helpers."""

import html
import re
from pathlib import Path
from typing import Any

from knowledge_base.scripts.audit_metadata.rules.field_data import _URL_DISALLOWED_FIELDS
from knowledge_base.scripts.audit_metadata.rules.string_fields import _walk_string_values
from knowledge_base.scripts.audit_metadata.support.model import RULE_GARBLED_MARKUP, Issue
from knowledge_base.scripts.audit_metadata.support.text import _normalize_inline_text

_SOURCE_YEAR_RE = re.compile(r"(?<!\d)(?:18|19|20)\d{2}(?!\d)")
_URL_RE = re.compile(r"\b(?:https?://|ftp://|www\.)[^\s<>()]+", re.IGNORECASE)
_GARBLED_MARKUP_RE = re.compile(
    r"<\s*/?\s*(?:sub|sup|math|mml:[A-Za-z0-9_-]+)\b[^>]*>|"
    r"<[^>]*\bxmlns(?::[A-Za-z0-9_-]+)?=",
    re.I,
)
_XML_URI_TAG_RE = re.compile(
    r"<\s*(?:[A-Za-z0-9_.-]+:)?uri\b[^>]*>(?P<inner>.*?)"
    r"</\s*(?:[A-Za-z0-9_.-]+:)?uri\s*>",
    re.I | re.S,
)
_XML_HTML_TAG_RE = re.compile(
    r"</?\s*[A-Za-z][A-Za-z0-9_.:-]*\b[^>]*>",
    re.I,
)


def _clean_garbled_markup_text(text: str) -> str:
    text = html.unescape(text)
    text = _XML_URI_TAG_RE.sub(lambda match: match.group("inner").strip(), text)
    text = _XML_HTML_TAG_RE.sub("", text)
    return _normalize_inline_text(text)


def find_garbled_markup_issues(path: Path, data: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    for field_name, value in _walk_string_values(data, ""):
        if not value:
            continue
        has_garbled_markup = bool(_GARBLED_MARKUP_RE.search(value))
        is_link_field = field_name == "link" or field_name.startswith("links_alt[")
        has_link_markup = is_link_field and ("<" in value or ">" in value)
        if not has_garbled_markup and not has_link_markup:
            continue

        example = _normalize_inline_text(value)
        if len(example) > 160:
            example = example[:157] + "..."
        issues.append(
            Issue(
                path,
                field_name,
                f"Contains likely garbled HTML/XML markup: {example!r}",
                "Replace with clean plain text or a plain URL.",
                rule=RULE_GARBLED_MARKUP,
            )
        )
    return issues


def _strip_years_from_source(source: str) -> str:
    """Remove publication-year tokens from a venue/source name."""
    source = re.sub(r"\s+", " ", source).strip()
    source = _SOURCE_YEAR_RE.sub("", source)

    # Remove punctuation left behind by year-only parentheticals/brackets.
    source = re.sub(r"\(\s*([^)]*?)\s+\)", r"(\1)", source)
    source = re.sub(r"\[\s*([^\]]*?)\s+\]", r"[\1]", source)
    source = re.sub(r"\{\s*([^}]*?)\s+\}", r"{\1}", source)
    source = re.sub(r"\(\s*\)", "", source)
    source = re.sub(r"\[\s*\]", "", source)
    source = re.sub(r"\{\s*\}", "", source)

    # Clean common separators around the removed year.
    source = re.sub(r",\s*\.\s*", ", ", source)
    source = re.sub(r"\s+([,;:])", r"\1", source)
    source = re.sub(r"([,;:])\s*([,;:])+", r"\1", source)
    source = re.sub(r"\s*[-–—]\s*(?=,|;|:|$)", "", source)
    source = re.sub(r"(?<=^)\s*[-–—]\s*", "", source)
    source = re.sub(r"\s{2,}", " ", source)
    source = re.sub(r"\b(?:on|at|in|of)\s*$", "", source, flags=re.IGNORECASE)
    return source.strip(" ,;:-–—")


def _looks_like_url(text: str) -> bool:
    return bool(_URL_RE.match(text))


def _find_urls(text: object) -> list[str]:
    return _URL_RE.findall(str(text))


def find_disallowed_url_issues(path: Path, data: dict[str, Any]) -> list["Issue"]:
    issues: list[Issue] = []
    for field_name in sorted(_URL_DISALLOWED_FIELDS):
        if field_name not in data:
            continue

        value = data.get(field_name)
        if isinstance(value, list):
            for index, item in enumerate(value):
                urls = _find_urls(item)
                if urls:
                    issues.append(
                        Issue(
                            path,
                            field_name,
                            f"URL detected in {field_name}[{index}]: {urls[0]!r}",
                        )
                    )
            continue

        urls = _find_urls(value)
        if urls:
            issues.append(
                Issue(
                    path,
                    field_name,
                    f"URL detected in {field_name}: {urls[0]!r}",
                )
            )

    return issues
