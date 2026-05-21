"""Small helpers shared by source-specific metadata prefill scripts."""

from __future__ import annotations

import html
import re
from pathlib import Path
from urllib.parse import parse_qs, unquote, urljoin, urlparse

from knowledge_base.config import AUDIT_STATUS_FIELD, DEFAULT_AUDIT_STATUS
from knowledge_base.utils.doi_utils import (
    fetch_page_html,
    scrape_abstract_from_html,
    scrape_doi_from_html,
)

_DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"'<>]+", re.I)
_YEAR_RE = re.compile(r"\b(18|19|20)\d{2}\b")


def read_url_lines(path: Path) -> list[str]:
    """Return non-comment, non-empty URL tokens from a paper todo file."""
    lines: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            token = line.split()[0].strip()
            if token.startswith("<") and token.endswith(">"):
                token = token[1:-1].strip()
            lines.append(token)
    return lines


def clean_doi(raw: str) -> str:
    """Normalize a DOI extracted from a URL, query parameter, or HTML field."""
    doi = html.unescape(str(raw or "")).strip()
    doi = doi.split("?", 1)[0]
    doi = doi.split("#", 1)[0] if "%23" not in doi.lower() else doi
    doi = unquote(doi).strip().strip('"\'')
    doi = doi.removeprefix("doi:").removeprefix("DOI:")
    doi = doi.removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    doi = doi.strip()
    doi = doi.rstrip("/")
    if doi.endswith(".full"):
        doi = doi[: -len(".full")]
    return doi.rstrip(".,;)")


def extract_doi(text: str) -> str:
    """Return the first DOI-looking token in *text*, or an empty string."""
    for raw in (text, unquote(text)):
        m = _DOI_RE.search(raw)
        if m:
            return clean_doi(m.group(0))
    return ""


def extract_doi_from_url(url: str) -> str:
    """Extract a DOI from common publisher URL shapes."""
    parsed = urlparse(url)
    for key in ("doi", "DOI"):
        values = parse_qs(parsed.query).get(key)
        if values:
            return clean_doi(values[0])

    path = parsed.path
    m = re.search(
        r"/doi/(?:abs/|full/|pdf/|epdf/|pdfdirect/)?(.+)$",
        path,
        flags=re.I,
    )
    if m:
        return clean_doi(m.group(1))

    doi = extract_doi(path)
    return doi or extract_doi(url)


def first_year(*values: str) -> int:
    """Return the first 4-digit year found in *values*, or 0."""
    for value in values:
        m = _YEAR_RE.search(str(value or ""))
        if m:
            return int(m.group(0))
    return 0


def clean_text(text: str) -> str:
    """Strip HTML and normalize whitespace in scraped text."""
    text = re.sub(r"<script\b.*?</script>", " ", text, flags=re.DOTALL | re.I)
    text = re.sub(r"<style\b.*?</style>", " ", text, flags=re.DOTALL | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def meta_contents(page_html: str, name: str) -> list[str]:
    """Return all meta tag content values for a name or property."""
    values: list[str] = []
    for tag in re.findall(r"<meta\b[^>]*>", page_html, flags=re.I):
        name_match = re.search(r'\b(?:name|property)=["\']([^"\']+)["\']', tag, flags=re.I)
        if not name_match or name_match.group(1).lower() != name.lower():
            continue
        content_match = re.search(r'\bcontent=["\']([^"\']*)["\']', tag, flags=re.I)
        if content_match:
            values.append(clean_text(content_match.group(1)))
    return values


def first_meta(page_html: str, *names: str) -> str:
    """Return the first non-empty meta content value for any of *names*."""
    for name in names:
        for value in meta_contents(page_html, name):
            if value:
                return value
    return ""


def element_text_by_id(page_html: str, element_id: str) -> str:
    """Return text inside the first element with id=*element_id*."""
    pat = rf'<(?P<tag>[a-z0-9]+)\b[^>]*\bid=["\']{re.escape(element_id)}["\'][^>]*>(?P<body>.*?)</(?P=tag)>'
    m = re.search(pat, page_html, flags=re.DOTALL | re.I)
    return clean_text(m.group("body")) if m else ""


def first_element_text(page_html: str, tag: str, class_name: str | None = None) -> str:
    """Return text inside the first matching tag, optionally constrained by class."""
    if class_name is None:
        pat = rf"<{tag}\b[^>]*>(.*?)</{tag}>"
    else:
        pat = rf'<{tag}\b[^>]*\bclass=["\'][^"\']*\b{re.escape(class_name)}\b[^"\']*["\'][^>]*>(.*?)</{tag}>'
    m = re.search(pat, page_html, flags=re.DOTALL | re.I)
    return clean_text(m.group(1)) if m else ""


def absolutize_url(base_url: str, maybe_relative_url: str) -> str:
    """Resolve a possibly relative URL and prefer HTTPS for known proceedings hosts."""
    url = urljoin(base_url, html.unescape(maybe_relative_url).strip())
    if url.startswith("http://proceedings.mlr.press/"):
        return "https://" + url.removeprefix("http://")
    if url.startswith("http://www.roboticsproceedings.org/"):
        return "https://" + url.removeprefix("http://")
    return url


def citation_authors(page_html: str) -> list[str]:
    """Extract authors from common citation metadata fields."""
    authors = meta_contents(page_html, "citation_author")
    if authors:
        return authors
    for name in ("dc.creator", "DC.Creator", "author", "parsely-author"):
        values = meta_contents(page_html, name)
        if not values:
            continue
        if len(values) > 1:
            return values
        if ";" in values[0]:
            return [part.strip() for part in values[0].split(";") if part.strip()]
        return [values[0]]
    return []


def citation_doi(page_html: str, url: str = "") -> str:
    """Extract a DOI from URL and citation metadata."""
    doi = extract_doi_from_url(url) if url else ""
    if doi:
        return doi
    for name in ("citation_doi", "dc.identifier", "DC.Identifier", "prism.doi", "doi"):
        for value in meta_contents(page_html, name):
            doi = extract_doi(value) or clean_doi(value)
            if doi.startswith("10."):
                return doi
    try:
        return scrape_doi_from_html(page_html)
    except Exception:
        return extract_doi(page_html)


def fetch_citation_page_fields(
    url: str,
    *,
    source_fallback: str = "",
    type_fallback: str = "Journal Paper",
    page_html: str | None = None,
) -> dict:
    """Fetch a publisher page and return normalized metadata fields."""
    page_html = fetch_page_html(url) if page_html is None else page_html

    title = (
        first_meta(page_html, "citation_title", "dc.title", "DC.Title", "og:title", "twitter:title")
        or first_element_text(page_html, "h1")
    )
    authors = citation_authors(page_html)
    publication_date = first_meta(
        page_html,
        "citation_publication_date",
        "citation_online_date",
        "citation_year",
        "dc.date",
        "DC.Date",
        "article:published_time",
        "date",
    )
    year = first_year(publication_date, url)

    source = first_meta(
        page_html,
        "citation_journal_title",
        "citation_conference_title",
        "citation_inbook_title",
        "citation_publisher",
        "dc.publisher",
        "DC.Publisher",
    )
    paper_type = "Conference Paper" if first_meta(page_html, "citation_conference_title") else type_fallback

    abstract = first_meta(
        page_html,
        "citation_abstract",
        "dc.description",
        "DC.Description",
        "og:description",
        "description",
    )
    if not abstract:
        abstract = element_text_by_id(page_html, "abstract") or first_element_text(page_html, "section", "abstract")
    if not abstract:
        abstract = scrape_abstract_from_html(page_html)

    doi = citation_doi(page_html, url)
    pdf_url = first_meta(page_html, "citation_pdf_url")
    link = absolutize_url(url, pdf_url) if pdf_url else url

    links_alt: list[str] = []
    html_url = first_meta(page_html, "citation_fulltext_html_url")
    if html_url:
        links_alt.append(absolutize_url(url, html_url))
    if link != url:
        links_alt.append(url)
    if doi:
        links_alt.append(f"https://doi.org/{doi}")

    links_alt = list(dict.fromkeys(x for x in links_alt if x and x != link))

    if not title or not authors or not year:
        raise ValueError(f"Incomplete citation metadata at {url!r}")

    return {
        "title": title,
        "authors": authors,
        "year": year,
        "source": source or source_fallback,
        "type": paper_type,
        "doi": doi or None,
        "abstract": abstract,
        "link": link,
        "links_alt": links_alt,
    }


def build_page_metadata(fields: dict) -> dict:
    """Return an ordered metadata dict for non-Crossref proceedings pages."""
    return {
        "title": fields["title"],
        "algorithm": None,
        "authors": fields["authors"],
        "year": fields["year"],
        "source": fields.get("source") or None,
        "type": fields.get("type", ""),
        "doi": fields.get("doi") or None,
        "arxiv_id": None,
        "tags": [],
        "abstract": fields.get("abstract", ""),
        "summary": "",
        "link": fields.get("link", ""),
        "links_alt": fields.get("links_alt", []),
        AUDIT_STATUS_FIELD: DEFAULT_AUDIT_STATUS,
    }
