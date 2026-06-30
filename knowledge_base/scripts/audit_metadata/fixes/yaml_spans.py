"""Helpers for identifying top-level YAML scalar spans."""

import re

_BLOCK_SCALAR_HEADER_RE = re.compile(r"^[>|][0-9+-]*(?:\s+#.*)?$")
_TOP_LEVEL_SCALAR_FIELD_RE = re.compile(r"^(?P<key>[A-Za-z_][A-Za-z0-9_]*)\s*:\s*(?P<value>.*?)(?P<newline>\r?\n?)$")


def _is_block_scalar_header(value: str) -> bool:
    return bool(_BLOCK_SCALAR_HEADER_RE.match(value.strip()))


def _is_multiline_quoted_scalar_header(value: str) -> bool:
    stripped = value.lstrip()
    if not stripped or stripped[0] not in ("'", '"'):
        return False

    quote = stripped[0]
    escaped = False
    for char in stripped[1:]:
        if quote == '"' and char == "\\" and not escaped:
            escaped = True
            continue
        if char == quote and not escaped:
            return False
        escaped = False
    return True


def _has_indented_continuation(lines: list[str], start: int) -> bool:
    for line in lines[start + 1 :]:
        if not line.strip():
            continue
        return line.startswith((" ", "\t"))
    return False


def _top_level_field_span(lines: list[str], start: int) -> tuple[str, str, int] | None:
    match = _TOP_LEVEL_SCALAR_FIELD_RE.match(lines[start])
    if not match:
        return None

    field_name = match.group("key")
    value = match.group("value")
    end = start + 1
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

    return field_name, value, end


__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
