"""Batch-prefill metadata.yml files from Project Euclid URLs."""

from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.doi_utils import fetch_crossref, fetch_with_retry
from knowledge_base.utils.prefill_template import PagePrefillScript, REPO_ROOT
from knowledge_base.utils.prefill_utils import extract_doi_from_url, read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "PROJECT_EUCLID.md"

_KNOWN_FIELDS_BY_TOKEN = {
    # Project Euclid's old Berkeley Symposium pages sit behind a bot challenge,
    # so keep the stable bibliographic record for the listed chapter here.
    "bsmsp/1200512992": {
        "title": "Some Methods for Classification and Analysis of Multivariate Observations",
        "authors": ["James MacQueen"],
        "year": 1967,
        "source": "Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability",
        "type": "Conference Paper",
        "doi": None,
        "abstract": "",
    },
}


def extract_entries(path: Path) -> list[str]:
    seen: set[str] = set()
    entries: list[str] = []
    for url in read_url_lines(path):
        if "projecteuclid.org/" not in url:
            print(f"  WARN: could not parse Project Euclid URL from: {url!r}")
            continue
        if url not in seen:
            seen.add(url)
            entries.append(url)
    return entries


def fetch_project_euclid_fields(url: str) -> dict:
    for token, fields in _KNOWN_FIELDS_BY_TOKEN.items():
        if token in url:
            return {**fields, "link": url, "links_alt": []}

    doi = extract_doi_from_url(url)
    if not doi:
        raise ValueError(f"Could not find a DOI or known Project Euclid record for {url!r}")

    data = fetch_with_retry(fetch_crossref, doi)
    return {
        "title": data["title"],
        "authors": data["authors"],
        "year": data["year"],
        "source": data.get("source") or "Project Euclid",
        "type": data.get("type") or "Journal Paper",
        "doi": data.get("doi") or doi,
        "abstract": data.get("abstract", ""),
        "link": url,
        "links_alt": [f"https://doi.org/{data.get('doi') or doi}"],
    }


class ProjectEuclidPrefill(PagePrefillScript[str]):
    description = "Prefill metadata from Project Euclid URLs."
    default_input = DEFAULT_INPUT
    entry_kind = "Project Euclid URLs"

    def extract_entries(self, path: Path) -> list[str]:
        return extract_entries(path)

    def fetch_fields(self, entry: str, _context: dict) -> dict:
        return fetch_project_euclid_fields(entry)


def main() -> None:
    ProjectEuclidPrefill().run()


if __name__ == "__main__":
    main()
