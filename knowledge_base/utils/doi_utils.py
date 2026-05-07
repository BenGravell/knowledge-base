"""Shared helpers for DOI-based paper metadata prefill scripts.

Covers Crossref API fetching, metadata assembly, folder-name generation,
and HTML scraping for publisher-page DOI extraction (IEEE, Elsevier).
"""

import argparse
import re
import time
import unicodedata
from pathlib import Path

import requests
import yaml

from knowledge_base.apps.arxiv_utils import metadata_to_yaml
from knowledge_base.config import AUDIT_STATUS_FIELD, DEFAULT_AUDIT_STATUS

PAPERS_DIR = Path(__file__).parent.parent / "docs" / "papers"

CROSSREF_API = "https://api.crossref.org/works/{doi}"
CROSSREF_HEADERS = {
    "User-Agent": "knowledge-base-prefill/1.0",
}

_S2_API = "https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=abstract"
_OPENALEX_API = "https://api.openalex.org/works/https://doi.org/{doi}"
_OPENALEX_HEADERS = {"User-Agent": "knowledge-base-prefill/1.0"}

CROSSREF_TYPE_MAP = {
    "journal-article": "Journal Paper",
    "proceedings-article": "Conference Paper",
    "book-chapter": "Conference Paper",
    "monograph": "Other",
    "report": "Technical Report",
    "dissertation": "PhD Dissertation",
    "preprint": "Preprint",
}

# Seconds between successful Crossref requests
BASE_DELAY = 2.0
MAX_RETRIES = 5
BACKOFF_BASE = 10.0

# Browser-like headers for scraping publisher pages
_BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}


# ---------------------------------------------------------------------------
# Abstract fallbacks (Semantic Scholar → OpenAlex)
# ---------------------------------------------------------------------------

def _fetch_s2_abstract(doi: str) -> str:
    r = requests.get(_S2_API.format(doi=doi), timeout=30)
    if not r.ok:
        return ""
    return (r.json().get("abstract") or "").strip()


def _fetch_openalex_abstract(doi: str) -> str:
    r = requests.get(_OPENALEX_API.format(doi=doi), headers=_OPENALEX_HEADERS, timeout=30)
    if not r.ok:
        return ""
    inv = r.json().get("abstract_inverted_index") or {}
    if not inv:
        return ""
    tokens: list[tuple[int, str]] = [
        (pos, word) for word, positions in inv.items() for pos in positions
    ]
    return " ".join(w for _, w in sorted(tokens))


def _fetch_abstract_fallback(doi: str) -> str:
    """Try Semantic Scholar then OpenAlex when Crossref has no abstract."""
    time.sleep(1.0)  # S2 unauthenticated: ~1 req/s
    try:
        abstract = _fetch_s2_abstract(doi)
        if abstract:
            return abstract
    except Exception:
        pass
    try:
        abstract = _fetch_openalex_abstract(doi)
        if abstract:
            return abstract
    except Exception:
        pass
    return ""


# ---------------------------------------------------------------------------
# Crossref
# ---------------------------------------------------------------------------

def fetch_crossref(doi: str) -> dict:
    """Return paper fields from the Crossref API for *doi*."""
    doi = doi.strip()
    r = requests.get(CROSSREF_API.format(doi=doi), headers=CROSSREF_HEADERS, timeout=60)
    r.raise_for_status()
    msg = r.json()["message"]

    titles = msg.get("title") or []
    title = re.sub(r"\s+", " ", titles[0]).strip() if titles else ""

    authors: list[str] = []
    for a in msg.get("author") or []:
        given = (a.get("given") or "").strip()
        family = (a.get("family") or "").strip()
        name = f"{given} {family}".strip() if given else family
        if name:
            authors.append(name)

    published = (
        msg.get("published")
        or msg.get("published-print")
        or msg.get("issued")
        or {}
    )
    date_parts = published.get("date-parts") or [[0]]
    year = date_parts[0][0] if date_parts and date_parts[0] else 0

    abstract_raw = msg.get("abstract") or ""
    abstract = re.sub(r"<[^>]+>", "", abstract_raw)
    abstract = re.sub(r"\s+", " ", abstract).strip()
    if not abstract:
        abstract = _fetch_abstract_fallback(doi)

    containers = msg.get("container-title") or []
    source = containers[0].strip() if containers else ""

    paper_type = CROSSREF_TYPE_MAP.get(msg.get("type") or "other", "Other")

    return {
        "title": title,
        "authors": authors,
        "year": year,
        "abstract": abstract,
        "doi": doi,
        "source": source,
        "type": paper_type,
        "link": f"https://doi.org/{doi}",
    }


def fetch_with_retry(fetch_fn, *args, **kwargs):
    """Call *fetch_fn* with retry/backoff on HTTP 429."""
    delay = BACKOFF_BASE
    last_exc: Exception = RuntimeError("no attempts made")
    for attempt in range(MAX_RETRIES):
        try:
            return fetch_fn(*args, **kwargs)
        except requests.HTTPError as exc:
            last_exc = exc
            if exc.response is not None and exc.response.status_code == 429:
                if attempt + 1 == MAX_RETRIES:
                    break
                print(f"    429 – waiting {delay:.0f}s (attempt {attempt + 1}/{MAX_RETRIES})")
                time.sleep(delay)
                delay *= 2
            else:
                raise
    raise last_exc


# ---------------------------------------------------------------------------
# Metadata assembly
# ---------------------------------------------------------------------------

def build_doi_metadata(fields: dict) -> dict:
    """Return an ordered dict ready for metadata_to_yaml, from Crossref fields."""
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
        "links_alt": [],
        AUDIT_STATUS_FIELD: DEFAULT_AUDIT_STATUS,
    }


# ---------------------------------------------------------------------------
# Path / write helpers
# ---------------------------------------------------------------------------

def slugify(text: str, max_words: int = 5) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    words = re.findall(r"[a-z0-9]+", text.lower())
    return "_".join(words[:max_words])


def generate_folder_name(year: int, authors: list[str], title: str) -> str:
    if authors:
        author_slug = slugify(authors[0].split()[-1], max_words=1)
    else:
        author_slug = "unknown"
    return f"{year}.{author_slug}.{slugify(title)}"


def doi_target_path(year: int, folder: str) -> Path:
    return PAPERS_DIR / str(year) / folder / "metadata.yml"


def write_doi_metadata(year: int, folder: str, yaml_text: str) -> Path:
    path = doi_target_path(year, folder)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml_text, encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# HTML scraping (IEEE, Elsevier)
# ---------------------------------------------------------------------------

def scrape_abstract_from_html(html: str) -> str:
    """Extract a paper abstract from raw HTML using publisher-specific and generic patterns."""

    def _clean(s: str) -> str:
        s = re.sub(r"<[^>]+>", " ", s)
        return re.sub(r"\s+", " ", s).strip()

    MIN = 80  # shorter strings are unlikely to be real abstracts
    candidates: list[str] = []

    # Springer: <div id="Abs1-content">...</div>
    m = re.search(r'id="Abs1-content"[^>]*>(.*?)</div>', html, re.DOTALL | re.I)
    if m:
        candidates.append(_clean(m.group(1)))

    # Springer chapter fallback: first <p> inside id="Abs1" section
    if not any(len(c) >= MIN for c in candidates):
        m = re.search(r'id="Abs1"[^>]*>.*?<p[^>]*>(.*?)</p>', html, re.DOTALL | re.I)
        if m:
            candidates.append(_clean(m.group(1)))

    # ACM: class="abstractSection abstractInFull"
    m = re.search(r'class="abstractSection[^"]*"[^>]*>(.*?)</div>', html, re.DOTALL | re.I)
    if m:
        candidates.append(_clean(m.group(1)))

    # citation_abstract meta tag
    for pat in (
        r'<meta[^>]+name="citation_abstract"[^>]+content="([^"]+)"',
        r'<meta[^>]+content="([^"]+)"[^>]+name="citation_abstract"',
    ):
        m = re.search(pat, html, re.I)
        if m:
            candidates.append(m.group(1).strip())
            break

    # JSON-LD "description" (Elsevier, others)
    m = re.search(r'"description"\s*:\s*"((?:[^"\\]|\\.){' + str(MIN) + r',})"', html)
    if m:
        candidates.append(re.sub(r"\\n", " ", m.group(1).replace('\\"', '"')).strip())

    # dc.description / og:description meta (often truncated — last resort)
    for prop in ("dc.description", "DC.Description", "og:description", "description"):
        pat_a = rf'<meta[^>]+(?:name|property)="{re.escape(prop)}"[^>]+content="([^"]+)"'
        pat_b = rf'<meta[^>]+content="([^"]+)"[^>]+(?:name|property)="{re.escape(prop)}"'
        for pat in (pat_a, pat_b):
            m = re.search(pat, html, re.I)
            if m:
                candidates.append(m.group(1).strip())
                break
        else:
            continue
        break

    valid = [c for c in candidates if len(c) >= MIN]
    return max(valid, key=len) if valid else ""


def scrape_doi_from_html(html: str) -> str:
    """Extract a DOI from raw HTML using several fallback patterns."""
    patterns = [
        # Standard citation_doi meta tag (attribute order variants)
        r'<meta[^>]+name=["\']citation_doi["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']citation_doi["\']',
        # JSON field (e.g. embedded XHR payload or JSON-LD)
        r'"doi"\s*:\s*"(10\.\d{4,}/[^"]+)"',
        # Bare doi.org link
        r'doi\.org/(10\.\d{4,}/[^\s"\'<>&]+)',
    ]
    for pat in patterns:
        m = re.search(pat, html, re.I)
        if m:
            doi = m.group(1).strip().rstrip(".,;)")
            if doi.startswith("10."):
                return doi
    raise ValueError("Could not find a DOI in the page HTML")


_CROSSREF_BY_ALT_ID = "https://api.crossref.org/works?filter=alternative-id:{alt_id}&rows=1"


def fetch_doi_from_crossref_pii(pii: str) -> str:
    """Return the DOI for *pii* using Crossref's alternative-id filter.

    Elsevier registers PII values as alternative IDs in Crossref, so this
    avoids scraping ScienceDirect (which blocks non-browser requests).
    Raises ValueError when no result is found.
    """
    r = requests.get(
        _CROSSREF_BY_ALT_ID.format(alt_id=pii),
        headers=CROSSREF_HEADERS,
        timeout=60,
    )
    r.raise_for_status()
    items = (r.json().get("message") or {}).get("items") or []
    if not items:
        raise ValueError(f"No Crossref hit for PII {pii!r}")
    doi = (items[0].get("DOI") or "").strip()
    if not doi:
        raise ValueError(f"Crossref returned an item but no DOI for PII {pii!r}")
    return doi


def fetch_page_html(url: str, extra_headers: dict | None = None) -> str:
    headers = dict(_BROWSER_HEADERS)
    if extra_headers:
        headers.update(extra_headers)
    r = requests.get(url, headers=headers, timeout=60)
    r.raise_for_status()
    return r.text


# ---------------------------------------------------------------------------
# Shared CLI helpers
# ---------------------------------------------------------------------------

def needs_reingest(path: Path) -> bool:
    """Return True if an existing metadata.yml has an empty abstract."""
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        return not str(data.get("abstract") or "").strip()
    except Exception:
        return True


def build_doi_index(papers_dir: Path | None = None) -> dict[str, Path]:
    """Return {doi_lowercase: metadata_path} for every existing metadata.yml with a doi field."""
    base = papers_dir if papers_dir is not None else PAPERS_DIR
    index: dict[str, Path] = {}
    for meta_path in base.rglob("metadata.yml"):
        try:
            data = yaml.safe_load(meta_path.read_text(encoding="utf-8")) or {}
            doi = str(data.get("doi") or "").strip()
            if doi:
                index[doi.lower()] = meta_path
        except Exception:
            pass
    return index


def find_existing_by_arxiv_id(arxiv_id: str, papers_dir: Path | None = None) -> Path | None:
    """Return the path to an existing metadata.yml for *arxiv_id*, or None."""
    base = papers_dir if papers_dir is not None else PAPERS_DIR
    matches = list(base.glob(f"*/{arxiv_id}/metadata.yml"))
    return matches[0] if matches else None


def make_parser(description: str, default_input: Path) -> argparse.ArgumentParser:
    """Return a pre-configured ArgumentParser shared by all prefill scripts."""
    p = argparse.ArgumentParser(description=description)
    p.add_argument("--input", type=Path, default=default_input)
    p.add_argument("--overwrite", action="store_true",
                   help="Overwrite existing metadata.yml files")
    p.add_argument("--reingest", action="store_true",
                   help="Re-fetch and overwrite entries whose existing abstract is empty")
    p.add_argument("--first", type=int, default=None, metavar="N",
                   help="Stop after N processed (written + failed) entries; skips do not count")
    p.add_argument("--list-skipped", action="store_true",
                   help="Print items from the input that already exist locally, then exit without fetching or writing")
    return p
