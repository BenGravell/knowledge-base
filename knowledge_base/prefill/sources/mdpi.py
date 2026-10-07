"""Resolve MDPI articles using publisher-deposited Crossref metadata."""

import re
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests

from knowledge_base.prefill.doi import CROSSREF_HEADERS

DEFAULT_INPUT = Path(__file__).resolve().parents[3] / "todo" / "papers" / "MDPI.md"

_MDPI_ARTICLE_RE = re.compile(
    r"/(?P<issn>\d{4}-\d{3}[\dX])/(?P<volume>\d+)/(?P<issue>\d+)/(?P<article>\d+)" r"(?:/(?:pdf|htm|xml))?/?", re.I
)


def accept_url(url: str) -> bool:
    return urlparse(url).hostname in {"mdpi.com", "www.mdpi.com"}


def article_coordinates(url: str) -> dict[str, str]:
    match = _MDPI_ARTICLE_RE.fullmatch(urlparse(url).path) if accept_url(url) else None
    if not match:
        raise ValueError(f"Cannot verify MDPI article identity from URL {url!r}")
    return {key: value.upper() if key == "issn" else str(int(value)) for key, value in match.groupdict().items()}


def resolve_doi(entry: str) -> str:
    expected = article_coordinates(entry)
    response = requests.get(
        f"https://api.crossref.org/journals/{expected['issn']}/works",
        params={
            "query.bibliographic": " ".join(expected[key] for key in ("volume", "issue", "article")),
            "rows": 10,
            "select": "DOI,resource",
        },
        headers=CROSSREF_HEADERS,
        timeout=60,
    )
    response.raise_for_status()
    matches = set()
    # ponytail: inspect ten candidates; unmatched articles stay queued for review.
    # Exact publisher URLs establish identity, not search rank or DOI spelling.
    for item in response.json()["message"]["items"]:
        url = (item.get("resource") or {}).get("primary", {}).get("URL", "")
        try:
            same_article = article_coordinates(url) == expected
        except ValueError:
            continue
        doi = str(item.get("DOI") or "").strip().casefold()
        if same_article and doi.startswith("10."):
            matches.add(doi)
    if len(matches) != 1:
        raise ValueError(f"Expected one matching Crossref DOI for {entry!r}; found {len(matches)}")
    return matches.pop()


def postprocess_crossref_data(entry: str, data: dict[str, Any]) -> dict[str, Any]:
    """Check the fetched DOI record before the runner writes or skips an entry."""
    expected = article_coordinates(entry)
    actual = {key: str(int(data.get(key) or "")) for key in ("volume", "issue", "article")}
    issns = {str(issn).upper() for issn in data.get("issn", [])}
    actual["issn"] = expected["issn"] if expected["issn"] in issns else ""
    if actual != expected or article_coordinates(str(data.get("resource_url") or "")) != expected:
        raise ValueError(f"Crossref DOI {data.get('doi')!r} does not identify MDPI article {entry!r}")
    return data
