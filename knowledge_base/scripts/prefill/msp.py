"""Batch-prefill metadata.yml files from Mathematical Sciences Publishers URLs."""

import re
from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import DoiPrefillScript, REPO_ROOT
from knowledge_base.utils.prefill_utils import read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "MSP.md"

_MSP_RE = re.compile(
    r"msp\.org/(?P<journal>[^/]+)/(?P<year>\d{4})/(?P<volume>\d+)-\d+/"
    r"[^/]+-p(?P<page>\d+)-p\.pdf$",
    re.I,
)


def extract_entries(path: Path) -> list[tuple[str, str]]:
    seen: set[str] = set()
    entries: list[tuple[str, str]] = []
    for url in read_url_lines(path):
        match = _MSP_RE.search(url)
        if not match:
            print(f"  WARN: could not parse MSP DOI from: {url!r}")
            continue
        doi = "10.2140/{journal}.{year}.{volume}.{page}".format(
            journal=match.group("journal"),
            year=match.group("year"),
            volume=int(match.group("volume")),
            page=int(match.group("page")),
        )
        if doi.lower() not in seen:
            seen.add(doi.lower())
            entries.append((url, doi))
    return entries


class MspPrefill(DoiPrefillScript[tuple[str, str]]):
    description = "Prefill metadata from MSP URLs."
    default_input = DEFAULT_INPUT
    entry_kind = "MSP DOIs"

    def extract_entries(self, path: Path) -> list[tuple[str, str]]:
        return extract_entries(path)

    def entry_label(self, entry: tuple[str, str]) -> str:
        return entry[1]

    def entry_doi(self, entry: tuple[str, str]) -> str:
        return entry[1]

    def postprocess_crossref_data(self, entry: tuple[str, str], data: dict) -> dict:
        url, _doi = entry
        return {**data, "link": url}

    def postprocess_metadata(self, entry: tuple[str, str], fields: dict, metadata: dict) -> dict:
        _url, _doi = entry
        return {**metadata, "links_alt": [f"https://doi.org/{fields['doi']}"]}


def main() -> None:
    MspPrefill().run()


if __name__ == "__main__":
    main()
