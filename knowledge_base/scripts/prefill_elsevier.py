"""Batch-prefill metadata.yml files from a list of ScienceDirect (Elsevier) URLs.

Usage:
    python prefill_elsevier.py [--input PATH] [--overwrite]

Defaults:
    --input      ../../todo/ELSEVIER_PAPERS.md
    --overwrite  False (skip entries whose metadata.yml already exists)

Strategy:
  1. Extract the PII from each ScienceDirect URL.
  2. Fetch the ScienceDirect page and scrape the DOI from the citation_doi
     meta tag or embedded JSON metadata.
  3. Query Crossref with the DOI for full, structured metadata.
  4. Write metadata.yml.
"""

import re
import time
from pathlib import Path

from knowledge_base.apps.arxiv_utils import metadata_to_yaml
from knowledge_base.utils.doi_utils import (
    BASE_DELAY,
    build_doi_index,
    build_doi_metadata,
    doi_target_path,
    fetch_crossref,
    fetch_doi_from_crossref_pii,
    fetch_page_html,
    fetch_with_retry,
    generate_folder_name,
    make_parser,
    needs_reingest,
    scrape_doi_from_html,
    write_doi_metadata,
)

DEFAULT_INPUT = Path(__file__).parent.parent.parent / "todo" / "ELSEVIER_PAPERS.md"

_SD_PII_RE = re.compile(r"sciencedirect\.com/science/article/(?:abs/|pii/)?pii/([A-Z0-9]+)", re.I)
_SD_PAGE_TMPL = "https://www.sciencedirect.com/science/article/pii/{pii}"


def extract_entries(path: Path) -> list[tuple[str, str]]:
    """Return (url, pii) pairs, deduplicated."""
    seen: set[str] = set()
    entries: list[tuple[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = _SD_PII_RE.search(line)
        if not m:
            print(f"  WARN: could not parse ScienceDirect PII from: {line!r}")
            continue
        pii = m.group(1).upper()
        url = _SD_PAGE_TMPL.format(pii=pii)
        if pii not in seen:
            seen.add(pii)
            entries.append((url, pii))
    return entries


def fetch_elsevier_doi(url: str, pii: str) -> str:
    """Return the DOI for a ScienceDirect article.

    Tries Crossref's alternative-id filter first (avoids scraping ScienceDirect,
    which blocks non-browser requests). Falls back to HTML scraping if needed.
    """
    try:
        return fetch_doi_from_crossref_pii(pii)
    except Exception:
        pass
    html = fetch_page_html(
        url,
        extra_headers={
            "Referer": "https://www.sciencedirect.com/",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    return scrape_doi_from_html(html)


def main() -> None:
    args = make_parser("Prefill metadata from ScienceDirect URLs.", DEFAULT_INPUT).parse_args()

    entries = extract_entries(args.input)
    print(f"Found {len(entries)} unique ScienceDirect PIIs in {args.input}")

    if args.list_skipped:
        doi_index = build_doi_index()
        for url, pii in entries:
            try:
                doi = fetch_elsevier_doi(url, pii)
            except Exception as exc:
                print(f"{pii}  ERROR getting DOI: {exc}")
                time.sleep(BASE_DELAY)
                continue
            existing = doi_index.get(doi.lower())
            if existing:
                print(f"{pii} ({doi})  {existing}")
            time.sleep(BASE_DELAY)
        return

    ok = skipped = failed = 0

    for i, (url, pii) in enumerate(entries, 1):
        prefix = f"[{i}/{len(entries)}] {pii}"

        # Step 1: scrape DOI from Elsevier page
        try:
            doi = fetch_elsevier_doi(url, pii)
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
