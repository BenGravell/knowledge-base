"""Batch-prefill metadata.yml files from a list of ACM DL URLs.

Usage:
    python prefill_acm.py [--input PATH] [--overwrite]

Defaults:
    --input      ../../todo/ACM_PAPERS.md
    --overwrite  False (skip entries whose metadata.yml already exists)

DOIs are extracted directly from ACM DL URLs, e.g.:
    https://dl.acm.org/doi/10.1145/3624480  →  10.1145/3624480
    https://dl.acm.org/doi/full/10.1145/...  →  10.1145/...
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
    fetch_with_retry,
    generate_folder_name,
    make_parser,
    should_skip,
    write_doi_metadata,
)

DEFAULT_INPUT = Path(__file__).parent.parent.parent / "todo" / "ACM_PAPERS.md"

# Captures the DOI portion after /doi/ (with optional /full/, /abs/, etc.)
_ACM_DOI_RE = re.compile(r"dl\.acm\.org/doi/(?:full/|abs/)?(\S+?)(?:\s|$)")


def extract_dois(path: Path) -> list[str]:
    seen: set[str] = set()
    dois: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = _ACM_DOI_RE.search(line)
        if not m:
            print(f"  WARN: could not parse ACM DOI from: {line!r}")
            continue
        doi = m.group(1).rstrip("/")
        if doi and doi not in seen:
            seen.add(doi)
            dois.append(doi)
    return dois


def main() -> None:
    args = make_parser("Prefill metadata from ACM DL URLs.", DEFAULT_INPUT).parse_args()

    dois = extract_dois(args.input)
    print(f"Found {len(dois)} unique DOIs in {args.input}")

    if args.list_skipped:
        doi_index = build_doi_index()
        for doi in dois:
            existing = doi_index.get(doi.lower())
            if existing:
                print(f"{doi}  {existing}")
        return

    ok = skipped = failed = 0
    doi_index = build_doi_index()

    for i, doi in enumerate(dois, 1):
        prefix = f"[{i}/{len(dois)}] {doi}"

        existing = doi_index.get(doi.lower())
        if should_skip(existing, args):
            print(f"{prefix}  SKIP (exists: {existing})")
            skipped += 1
            continue

        try:
            data = fetch_with_retry(fetch_crossref, doi)
        except Exception as exc:
            print(f"{prefix}  ERROR fetching Crossref: {exc}")
            failed += 1
            time.sleep(BASE_DELAY)
            if args.first is not None and ok + failed >= args.first:
                break
            continue

        folder = generate_folder_name(data["year"], data["authors"], data["title"])
        out = doi_target_path(data["year"], folder)
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
