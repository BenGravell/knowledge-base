"""Command-line entry point for staged arXiv metadata refinement."""

from __future__ import annotations

import yaml

from knowledge_base.scripts.refine_staged_arxiv_metadata.cache import load_cache
from knowledge_base.scripts.refine_staged_arxiv_metadata.refine import refine, staged_metadata_files


def main() -> None:
    cache = load_cache()
    files = staged_metadata_files()
    updated = 0
    official = 0
    for idx, path in enumerate(files, 1):
        changed = refine(path, cache)
        after = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if changed:
            updated += 1
        if after.get("source") != "arXiv" or after.get("type") != "Preprint":
            official += 1
        if idx % 25 == 0:
            print(f"{idx}/{len(files)} processed; {updated} updated; {official} official venues")
    print(f"Done: {len(files)} processed, {updated} updated, {official} with official venue/type")
