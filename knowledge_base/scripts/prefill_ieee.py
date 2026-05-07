"""Batch-prefill metadata.yml files from a list of IEEE Xplore URLs.

Usage:
    python prefill_ieee.py [--input PATH] [--overwrite]

Defaults:
    --input      ../../todo/IEEE_PAPERS.md
    --overwrite  False (skip entries whose metadata.yml already exists)

Strategy:
  1. Extract the article number from each IEEE Xplore URL.
  2. Fetch the IEEE Xplore page for that article and scrape the DOI from
     embedded metadata (citation_doi meta tag or JSON payload).
  3. Query Crossref with the DOI for full, structured metadata.
  4. Write metadata.yml.
"""

import re
import time
from pathlib import Path

from knowledge_base.apps.arxiv_utils import metadata_to_yaml
from knowledge_base.utils.doi_utils import (
    BASE_DELAY,
    BACKOFF_BASE,
    MAX_RETRIES,
    build_doi_index,
    build_doi_metadata,
    doi_target_path,
    fetch_crossref,
    fetch_page_html,
    fetch_with_retry,
    generate_folder_name,
    make_parser,
    needs_reingest,
    scrape_doi_from_html,
    write_doi_metadata,
)

DEFAULT_INPUT = Path(__file__).parent.parent.parent / "todo" / "IEEE_PAPERS.md"

_IEEE_ARTICLE_RE = re.compile(r"ieeexplore\.ieee\.org/document/(\d+)")

# IEEE Xplore internal REST endpoint used by their own website
_IEEE_REST_TMPL = "https://ieeexplore.ieee.org/rest/document/{article_id}/metadata"
_IEEE_PAGE_TMPL = "https://ieeexplore.ieee.org/document/{article_id}"


def extract_articles(path: Path) -> list[tuple[str, str]]:
    """Return (url, article_id) pairs, deduplicated."""
    seen: set[str] = set()
    entries: list[tuple[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = _IEEE_ARTICLE_RE.search(line)
        if not m:
            print(f"  WARN: could not parse IEEE article ID from: {line!r}")
            continue
        article_id = m.group(1)
        url = _IEEE_PAGE_TMPL.format(article_id=article_id)
        if article_id not in seen:
            seen.add(article_id)
            entries.append((url, article_id))
    return entries


def fetch_ieee_doi(article_id: str) -> str:
    """Return the DOI for an IEEE Xplore article, trying REST then HTML."""
    rest_url = _IEEE_REST_TMPL.format(article_id=article_id)
    page_url = _IEEE_PAGE_TMPL.format(article_id=article_id)

    # Try the internal REST API first (JSON, no JS required)
    try:
        import requests
        r = requests.get(
            rest_url,
            headers={
                "Accept": "application/json, */*",
                "Referer": page_url,
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 Chrome/124.0.0.0 Safari/537.36"
                ),
            },
            timeout=60,
        )
        if r.ok:
            payload = r.json()
            # The payload is typically a list; first item has the doi
            item = payload[0] if isinstance(payload, list) else payload
            doi = (item.get("doi") or item.get("doiLink") or "").strip()
            if doi and doi.startswith("10."):
                return doi
    except Exception:
        pass  # fall through to HTML scraping

    # Fall back: fetch the full HTML page and scrape
    html = fetch_page_html(page_url, extra_headers={"Referer": "https://ieeexplore.ieee.org/"})
    return scrape_doi_from_html(html)


def main() -> None:
    args = make_parser("Prefill metadata from IEEE Xplore URLs.", DEFAULT_INPUT).parse_args()

    entries = extract_articles(args.input)
    print(f"Found {len(entries)} unique IEEE articles in {args.input}")

    if args.list_skipped:
        doi_index = build_doi_index()
        for _url, article_id in entries:
            try:
                doi = fetch_ieee_doi(article_id)
            except Exception as exc:
                print(f"{article_id}  ERROR getting DOI: {exc}")
                time.sleep(BASE_DELAY)
                continue
            existing = doi_index.get(doi.lower())
            if existing:
                print(f"{article_id} ({doi})  {existing}")
            time.sleep(BASE_DELAY)
        return

    ok = skipped = failed = 0

    for i, (url, article_id) in enumerate(entries, 1):
        prefix = f"[{i}/{len(entries)}] {article_id}"

        # Step 1: get DOI from IEEE
        try:
            doi = fetch_ieee_doi(article_id)
        except Exception as exc:
            print(f"{prefix}  ERROR getting DOI: {exc}")
            failed += 1
            time.sleep(BASE_DELAY)
            if args.first is not None and ok + failed >= args.first:
                break
            continue

        # Step 2: fetch full metadata from Crossref
        try:
            data = fetch_with_retry(fetch_crossref, doi)
        except Exception as exc:
            print(f"{prefix}  ERROR fetching Crossref for doi={doi}: {exc}")
            failed += 1
            time.sleep(BASE_DELAY)
            if args.first is not None and ok + failed >= args.first:
                break
            continue

        folder = generate_folder_name(data["year"], data["authors"], data["title"])
        out = doi_target_path(data["year"], folder)

        if out.exists() and not args.overwrite:
            if args.reingest and needs_reingest(out):
                pass  # abstract is empty — fall through to re-fetch
            else:
                print(f"{prefix}  SKIP (exists: {out})")
                skipped += 1
                continue

        metadata = build_doi_metadata(data)
        yaml_text = metadata_to_yaml(metadata)
        write_doi_metadata(data["year"], folder, yaml_text)
        print(f"{prefix}  OK doi={doi} -> {out}")
        ok += 1

        if args.first is not None and ok + failed >= args.first:
            break
        time.sleep(BASE_DELAY)

    print(f"\nDone: {ok} written, {skipped} skipped, {failed} failed")


if __name__ == "__main__":
    main()
