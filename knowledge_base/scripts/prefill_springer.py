"""Batch-prefill metadata.yml files from a list of Springer/SpringerLink URLs.

Usage:
    python prefill_springer.py [--input PATH] [--overwrite]

Defaults:
    --input      ../../todo/SPRINGER_PAPERS.md
    --overwrite  False (skip entries whose metadata.yml already exists)

DOIs are extracted directly from Springer URLs, e.g.:
    https://link.springer.com/article/10.1007/BF00115009  →  10.1007/BF00115009
    https://link.springer.com/chapter/10.1007/978-3-642-19457-3_1  →  10.1007/978-3-642-19457-3_1
"""

import re
import time
from pathlib import Path

from knowledge_base.apps.arxiv_utils import metadata_to_yaml
from knowledge_base.utils.doi_utils import (
    BASE_DELAY,
    PAPERS_DIR,
    build_doi_index,
    build_doi_metadata,
    doi_target_path,
    fetch_crossref,
    fetch_page_html,
    fetch_with_retry,
    generate_folder_name,
    make_parser,
    needs_reingest,
    scrape_abstract_from_html,
    write_doi_metadata,
)

DEFAULT_INPUT = Path(__file__).parent.parent.parent / "todo" / "SPRINGER_PAPERS.md"

# Captures the DOI portion from article/ or chapter/ paths
_SPRINGER_DOI_RE = re.compile(r"link\.springer\.com/(?:article|chapter|book|referenceworkentry)/(\S+?)(?:\s|$)")


def extract_entries(path: Path) -> list[tuple[str, str]]:
    """Return (original_url, doi) pairs, deduplicated by DOI."""
    seen: set[str] = set()
    entries: list[tuple[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = _SPRINGER_DOI_RE.search(line)
        if not m:
            print(f"  WARN: could not parse Springer DOI from: {line!r}")
            continue
        doi = m.group(1).rstrip("/")
        if doi and doi not in seen:
            seen.add(doi)
            entries.append((line.split()[0], doi))
    return entries


def main() -> None:
    args = make_parser("Prefill metadata from Springer URLs.", DEFAULT_INPUT).parse_args()

    entries = extract_entries(args.input)
    print(f"Found {len(entries)} unique DOIs in {args.input}")

    if args.list_skipped:
        doi_index = build_doi_index()
        for _url, doi in entries:
            existing = doi_index.get(doi.lower())
            if existing:
                print(f"{doi}  {existing}")
        return

    ok = skipped = failed = 0

    for i, (url, doi) in enumerate(entries, 1):
        prefix = f"[{i}/{len(entries)}] {doi}"

        try:
            data = fetch_with_retry(fetch_crossref, doi)
        except Exception as exc:
            print(f"{prefix}  ERROR fetching Crossref: {exc}")
            failed += 1
            time.sleep(BASE_DELAY)
            if args.first is not None and ok + failed >= args.first:
                break
            continue

        # Springer page scrape when Crossref + S2 + OpenAlex all missed the abstract
        if not data["abstract"]:
            try:
                abstract = scrape_abstract_from_html(fetch_page_html(url))
                if abstract:
                    data = {**data, "abstract": abstract}
            except Exception:
                pass

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
        print(f"{prefix}  OK -> {out}")
        ok += 1

        if args.first is not None and ok + failed >= args.first:
            break
        time.sleep(BASE_DELAY)

    print(f"\nDone: {ok} written, {skipped} skipped, {failed} failed")


if __name__ == "__main__":
    main()
