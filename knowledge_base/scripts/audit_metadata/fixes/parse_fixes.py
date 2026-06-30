"""Raw YAML parse-recovery fix helpers."""

import re

from knowledge_base.scripts.audit_metadata.rules.encoding import _decode_utf8_mojibake_controls
from knowledge_base.scripts.audit_metadata.rules.string_fields import _HTML_ENTITY_RE, _html_unescape_repeated

_EMPTY_YAML_LIST_KEY_RE = re.compile(r"^[ \t]*-\s*:\s*(?:#.*)?\r?\n?", re.M)


def _fix_escaped_sequences_in_yaml(raw: str) -> tuple[str, int]:
    new_raw = _html_unescape_repeated(raw)
    return new_raw, len(_HTML_ENTITY_RE.findall(raw))


def _remove_empty_yaml_list_keys(raw: str) -> tuple[str, int]:
    return _EMPTY_YAML_LIST_KEY_RE.subn("", raw)


def _fix_high_confidence_parse_errors_in_yaml(raw: str) -> tuple[str, list[str]]:
    messages: list[str] = []

    raw, removed_empty_items = _remove_empty_yaml_list_keys(raw)
    if removed_empty_items:
        messages.append(f"  removed {removed_empty_items} empty YAML list item(s)")

    raw, decoded_mojibake = _decode_utf8_mojibake_controls(raw)
    if decoded_mojibake:
        messages.append(f"  decoded {decoded_mojibake} UTF-8 mojibake sequence(s)")

    return raw, messages


__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
