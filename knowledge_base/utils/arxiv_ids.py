"""Pure arXiv identifier normalization, year inference, and URL construction."""

import re
from urllib.parse import quote, unquote, urlparse

_ARXIV_NEW_RE = re.compile(r"^(?P<yy>\d{2})(?P<mm>\d{2})\.\d{4,5}(?:[vV]\d+)?$")
_ARXIV_OLD_RE = re.compile(r"^[A-Za-z][A-Za-z0-9-]*(?:\.[A-Z]{2})?/" r"(?P<yy>\d{2})(?P<mm>\d{2})\d{3}(?:[vV]\d+)?$")


def normalize_arxiv_id(arxiv_id: str | None) -> str:
    """Return a bare arXiv ID from an ID, arXiv URL, or ``arXiv:`` token."""
    text = str(arxiv_id or "").strip()
    text = re.sub(r"^arxiv:\s*", "", text, flags=re.IGNORECASE).strip()
    if not text:
        return ""

    parsed = urlparse(text)
    host = parsed.netloc.lower().removeprefix("www.")
    if parsed.scheme and host:
        parts = [unquote(part) for part in parsed.path.strip("/").split("/") if part]
        if host == "arxiv.org" and parts[:1] and parts[0].lower() in {"abs", "pdf", "html"}:
            parts = parts[1:]
            if len(parts) > 1 and parts[-1].lower() == "pdf":
                parts = parts[:-1]
            text = "/".join(parts)
        elif host == "ar5iv.labs.arxiv.org" and parts[:1] and parts[0].lower() == "html":
            text = "/".join(parts[1:])
        else:
            text = parsed.path.strip("/")

    text = text.strip().strip("<>()[]").rstrip("/")
    text = re.sub(r"^([A-Za-z][A-Za-z0-9-]*)\.[A-Za-z]{2}/", r"\1/", text)
    if text.lower().endswith("/pdf"):
        candidate = text[:-4].rstrip("/")
        if _ARXIV_NEW_RE.match(candidate) or _ARXIV_OLD_RE.match(candidate):
            text = candidate
    if text.lower().endswith(".pdf"):
        text = text[:-4]
    if _ARXIV_NEW_RE.match(text) or _ARXIV_OLD_RE.match(text):
        text = re.sub(r"[vV]\d+$", "", text)
    return text


def arxiv_year_from_id(arxiv_id: str | None) -> int:
    """Infer publication year from new- or old-style arXiv IDs when possible."""
    arxiv_id = normalize_arxiv_id(arxiv_id)
    match = _ARXIV_NEW_RE.match(arxiv_id) or _ARXIV_OLD_RE.match(arxiv_id)
    if not match:
        return 0

    yy = int(match.group("yy"))
    mm = int(match.group("mm"))
    if not 1 <= mm <= 12:
        return 0
    return 1900 + yy if yy >= 91 else 2000 + yy


def arxiv_abs_url(arxiv_id: str | None) -> str:
    encoded = quote(normalize_arxiv_id(arxiv_id), safe="/")
    return f"https://arxiv.org/abs/{encoded}"


def arxiv_pdf_url(arxiv_id: str | None) -> str:
    encoded = quote(normalize_arxiv_id(arxiv_id), safe="/")
    return f"https://arxiv.org/pdf/{encoded}"


def arxiv_html_url(arxiv_id: str | None) -> str:
    encoded = quote(normalize_arxiv_id(arxiv_id), safe="/")
    return f"https://ar5iv.labs.arxiv.org/html/{encoded}"
