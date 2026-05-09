"""Batch-prefill metadata.yml files from JSTOR stable URLs."""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import DoiPrefillScript, REPO_ROOT
from knowledge_base.utils.prefill_utils import read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "JSTOR.md"

_STABLE_RE = re.compile(r"jstor\.org/stable/([^/?#\s]+)", re.I)
_DOI_BY_STABLE_ID = {
    "43633451": "10.1090/qam/10666",
    "43633461": "10.1090/qam/10667",
}


def doi_for_stable_id(stable_id: str) -> str:
    return _DOI_BY_STABLE_ID.get(stable_id, f"10.2307/{stable_id}")


def extract_entries(path: Path) -> list[tuple[str, str, str]]:
    seen: set[str] = set()
    entries: list[tuple[str, str, str]] = []
    for url in read_url_lines(path):
        match = _STABLE_RE.search(url)
        if not match:
            print(f"  WARN: could not parse JSTOR stable URL from: {url!r}")
            continue
        stable_id = match.group(1)
        doi = doi_for_stable_id(stable_id)
        if doi.lower() not in seen:
            seen.add(doi.lower())
            entries.append((url, stable_id, doi))
    return entries


class JstorPrefill(DoiPrefillScript[tuple[str, str, str]]):
    description = "Prefill metadata from JSTOR stable URLs."
    default_input = DEFAULT_INPUT
    entry_kind = "JSTOR stable URLs"

    def extract_entries(self, path: Path) -> list[tuple[str, str, str]]:
        return extract_entries(path)

    def entry_label(self, entry: tuple[str, str, str]) -> str:
        _url, stable_id, _doi = entry
        return stable_id

    def entry_doi(self, entry: tuple[str, str, str]) -> str:
        _url, _stable_id, doi = entry
        return doi

    def postprocess_crossref_data(self, entry: tuple[str, str, str], data: dict) -> dict:
        url, _stable_id, _doi = entry
        return {**data, "link": url}

    def postprocess_metadata(self, entry: tuple[str, str, str], fields: dict, metadata: dict) -> dict:
        _url, _stable_id, _doi = entry
        return {**metadata, "links_alt": [f"https://doi.org/{fields['doi']}"]}


def main() -> None:
    JstorPrefill().run()


if __name__ == "__main__":
    main()
