"""Metadata field-style audit constants."""

_TITLE_CHARACTER_ESCAPE_ISSUE_PREFIX = "Contains escaped YAML character sequence(s) in title"
_URL_DISALLOWED_FIELDS = {
    "title",
    "algorithm",
    "authors",
    "year",
    "source",
    "type",
    "doi",
    "arxiv_id",
    "tags",
    "audit_status",
}
_FOLDED_TEXT_FIELDS = {
    "title",
    "abstract",
    "summary",
}
_FOLDED_TEXT_FIELD_ISSUE_PREFIX = "Long text field should use folded YAML block style"
_FOLDED_TEXT_FIELD_MULTILINE_ISSUE_PREFIX = "Folded text field should use a single YAML content line"
_FOLDED_TEXT_FIELD_BLANK_LINE_ISSUE_PREFIX = "Folded text field contains blank YAML content line"
_MULTILINE_FORBIDDEN_FIELDS = {
    "algorithm",
    "year",
    "source",
    "type",
    "doi",
    "arxiv_id",
    "link",
    "audit_status",
}

__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
