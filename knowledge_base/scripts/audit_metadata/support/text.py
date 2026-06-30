"""Small shared text helpers for metadata audit modules."""

import re


def _normalize_inline_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()
