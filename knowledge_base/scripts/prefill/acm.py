"""Batch-prefill metadata.yml files from a list of ACM DL URLs.

Usage:
    python knowledge_base/scripts/prefill/acm.py [--input PATH] [--overwrite]

Defaults:
    --input      todo/papers/ACM.md
    --overwrite  False (skip entries whose metadata.yml already exists)

DOIs are extracted directly from ACM DL URLs, e.g.:
    https://dl.acm.org/doi/10.1145/3624480  →  10.1145/3624480
    https://dl.acm.org/doi/full/10.1145/...  →  10.1145/...
"""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys
    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import DoiPrefillScript

DEFAULT_INPUT = Path(__file__).parent.parent.parent.parent / "todo" / "papers" / "ACM.md"

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


class AcmPrefill(DoiPrefillScript[str]):
    description = "Prefill metadata from ACM DL URLs."
    default_input = DEFAULT_INPUT

    def extract_entries(self, path: Path) -> list[str]:
        return extract_dois(path)

    def entry_doi(self, entry: str) -> str:
        return entry


def main() -> None:
    AcmPrefill().run()


if __name__ == "__main__":
    main()
