"""Title cleanup and YAML rewrite helpers."""

import html
import re

import yaml

from knowledge_base.scripts.audit_metadata.fixes.yaml_rewrite import _format_metadata_scalar_line
from knowledge_base.scripts.audit_metadata.fixes.yaml_spans import (
    _has_indented_continuation,
    _is_block_scalar_header,
    _is_multiline_quoted_scalar_header,
)
from knowledge_base.scripts.audit_metadata.rules.title import (
    _PLACEHOLDER_PREFIX,
    _normalize_title_spacing,
    to_title_case,
)
from knowledge_base.scripts.audit_metadata.support.yaml_support import _yaml_safe_load

_TITLE_HTML_TAG_RE = re.compile(r"</?\s*[A-Za-z][^>]*>")
_TITLE_MATH_SPAN_RE = re.compile(r"\$(?P<math>[^$]+)\$")
_TITLE_LATEX_COMMAND_RE = re.compile(r"\\(?:mathcal|mathrm|mathbf|mathit|operatorname)\{([^{}]+)\}")
_TITLE_LINE_RE = re.compile(r"^title\s*:\s*(?P<value>.*?)(?P<newline>\r?\n?)$")


def _format_title_line(new_title: str, line_ending: str = "\n") -> str:
    return _format_metadata_scalar_line("title", new_title, line_ending)


def _plain_multiline_title_parts(raw: str) -> tuple[str, str] | None:
    lines = raw.splitlines(keepends=True)
    for start, line in enumerate(lines):
        m = _TITLE_LINE_RE.match(line)
        if not m:
            continue

        value = m.group("value")
        if _is_block_scalar_header(value) or not _has_indented_continuation(lines, start):
            return None

        end = start + 1
        continuation_lines = []
        while end < len(lines):
            next_line = lines[end]
            if next_line.strip() and not next_line.startswith((" ", "\t")):
                break
            if next_line.strip():
                continuation_lines.append(next_line.strip())
            end += 1

        header = value.strip()
        try:
            parsed = _yaml_safe_load(f"title: {header}\n")
            header = str(parsed.get("title", header)) if isinstance(parsed, dict) else header
        except yaml.YAMLError:
            header = header.strip("'\"")

        continuation = " ".join(continuation_lines)
        return header, continuation

    return None


def _normalize_for_duplicate_title_check(title: str) -> str:
    return " ".join(title.split()).casefold()


def _title_has_garbage(title: str) -> bool:
    return bool(
        _TITLE_HTML_TAG_RE.search(title) or _TITLE_MATH_SPAN_RE.search(title) or _TITLE_LATEX_COMMAND_RE.search(title)
    )


def _plain_latex_math(text: str) -> str:
    text = text.replace(r"\left", "")
    text = text.replace(r"\right", "")
    text = re.sub(r"\\frac\{([^{}]+)\}\{([^{}]+)\}", r"\1/\2", text)
    text = _TITLE_LATEX_COMMAND_RE.sub(r"\1", text)
    text = text.replace(r"\infty", "∞")
    text = text.replace(r"\times", "x")
    text = re.sub(r"\{([^{}]+)\}", r"\1", text)
    text = re.sub(r"_\{?([^{}\s]+)\}?", r"\1", text)
    return text.replace("\\", "")


def _protect_title_spans(title: str) -> tuple[str, list[str], bool]:
    protected: list[str] = []
    changed = False

    def protect(value: str) -> str:
        protected.append(value)
        return f"{_PLACEHOLDER_PREFIX}{len(protected) - 1}"

    def replace_math(m: re.Match[str]) -> str:
        nonlocal changed
        changed = True
        return protect(_plain_latex_math(m.group("math")))

    title = _TITLE_MATH_SPAN_RE.sub(replace_math, title)

    def replace_paired_tag(m: re.Match[str]) -> str:
        nonlocal changed
        changed = True
        inner = _TITLE_HTML_TAG_RE.sub("", m.group("inner"))
        return protect(html.unescape(inner))

    paired_tag_re = re.compile(
        r"<\s*(?P<tag>i|em|b|strong|sub|sup)\b[^>]*>"
        r"(?P<inner>.*?)"
        r"</\s*(?P=tag)\s*>",
        re.I,
    )
    title = paired_tag_re.sub(replace_paired_tag, title)
    return title, protected, changed


def _restore_title_spans(title: str, protected: list[str]) -> str:
    for i, value in enumerate(protected):
        title = title.replace(f"{_PLACEHOLDER_PREFIX}{i}", value)
    return title


def _prepare_title_garbage_fix(title: str) -> tuple[str, list[str], bool]:
    title = html.unescape(title)
    title, protected, changed = _protect_title_spans(title)

    if _TITLE_HTML_TAG_RE.search(title):
        changed = True
        title = _TITLE_HTML_TAG_RE.sub("", title)

    if _TITLE_LATEX_COMMAND_RE.search(title):
        changed = True
        title = _plain_latex_math(title)

    if changed:
        # Removing inline markup can join neighboring tokens, e.g.
        # "to<i>H</i><sub>∞</sub>control" -> "toH∞control".
        title = re.sub(rf"(?<=[a-z])(?={_PLACEHOLDER_PREFIX}\d+)", " ", title)
        title = re.sub(
            rf"({_PLACEHOLDER_PREFIX}\d+)(?!{_PLACEHOLDER_PREFIX})(?=[A-Za-z])",
            r"\1 ",
            title,
        )
        title = re.sub(r"(?<=[a-z])(?=[A-Z∞])", " ", title)
        title = re.sub(r"(?<=[∞])(?=[A-Za-z])", " ", title)
        title = _normalize_title_spacing(title)

    return title, protected, changed


def _suggest_title_fix(raw: str, title: str) -> str:
    title_to_fix = title
    parts = _plain_multiline_title_parts(raw)
    if parts is not None:
        header, continuation = parts
        if (
            header
            and continuation
            and _normalize_for_duplicate_title_check(header) == _normalize_for_duplicate_title_check(continuation)
        ):
            title_to_fix = header

    title_to_fix, protected, _ = _prepare_title_garbage_fix(title_to_fix)
    fixed = to_title_case(title_to_fix)
    return _restore_title_spans(fixed, protected)


def _fix_title_in_yaml(raw: str, new_title: str) -> str:
    """Replace the title value in raw YAML text."""
    lines = raw.splitlines(keepends=True)
    for start, line in enumerate(lines):
        m = _TITLE_LINE_RE.match(line)
        if not m:
            continue

        end = start + 1
        value = m.group("value")
        if (
            _is_block_scalar_header(value)
            or _is_multiline_quoted_scalar_header(value)
            or _has_indented_continuation(lines, start)
        ):
            while end < len(lines):
                next_line = lines[end]
                if next_line.strip() and not next_line.startswith((" ", "\t")):
                    break
                end += 1

        replacement = _format_title_line(new_title, m.group("newline"))
        return "".join([*lines[:start], replacement, *lines[end:]])

    return raw


__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
