"""Whitespace and dash audit constants."""

import re

_BIG_WHITESPACE_RE = re.compile(r" {3,}")
_TIGHT_LETTER_PAREN_RE = re.compile(r"\b(?P<left>[A-Za-z][A-Za-z0-9-]*)" r"\((?P<inner>[A-Za-z][A-Za-z0-9+/-]{1,31})\)")
_ASCII_MULTI_DASH_RE = re.compile(r"-{2,}")
_BIG_WHITESPACE_ISSUE_PREFIX = "Contains 3+ consecutive spaces"
_TIGHT_LETTER_PAREN_ISSUE_PREFIX = "Contains tight letter-parenthetical spacing"
_ASCII_MULTI_DASH_ISSUE_PREFIX = "Contains ASCII multi-dash punctuation"

_TEXT_SPACING_EXCLUDED_FIELDS = {
    "arxiv_id",
    "doi",
    "link",
    "links_alt",
}
_TIGHT_PAREN_ALLOWED_PREFIXES = {
    "argmax",
    "argmin",
    "cos",
    "det",
    "exp",
    "frac",
    "log",
    "max",
    "min",
    "poly",
    "rank",
    "sigma",
    "sigmoid",
    "sin",
    "softmax",
    "sqrt",
    "tan",
    "tanh",
    "tr",
    "trace",
}

__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
