"""Batch-prefill metadata.yml files from ResearchGate URLs."""

from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.doi_utils import fetch_crossref, fetch_with_retry
from knowledge_base.utils.prefill_template import PagePrefillScript, REPO_ROOT
from knowledge_base.utils.prefill_utils import read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "RESEARCHGATE.md"

_KNOWN_FIELDS_BY_TOKEN = {
    "An_Isotropic_3x3_Image_Gradient_Operator": {
        "title": "An Isotropic 3x3 Image Gradient Operator",
        "authors": ["Irwin Sobel", "Gary Feldman"],
        "year": 2015,
        "source": "ResearchGate",
        "type": "Other",
        "doi": "10.13140/RG.2.1.1912.4965",
        "abstract": (
            "We would like to document the derivation of a simple, computationally "
            "efficient, gradient operator which we developed in 1968. This operator "
            "has been frequently used and referenced since that time."
        ),
    },
    "On-Line_Q-Learning_Using_Connectionist_Systems": {
        "title": "On-Line Q-Learning Using Connectionist Systems",
        "authors": ["G. A. Rummery", "Mahesan Niranjan"],
        "year": 1994,
        "source": "Technical Report CUED/F-INFENG/TR 166",
        "type": "Technical Report",
        "doi": None,
        "abstract": "",
    },
    "Near_optimal_hierarchical_path-finding_HPA": {
        "title": "Near Optimal Hierarchical Path-Finding",
        "authors": ["Adi Botea", "Martin Mueller", "Jonathan Schaeffer"],
        "year": 2004,
        "source": "AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment",
        "type": "Conference Paper",
        "doi": None,
        "abstract": "",
    },
}
_DOI_BY_TOKEN = {
    "The_BOSS_is_concerned_with_time_series_classification_in_the_presence_of_noise": (
        "10.1007/s10618-014-0377-7"
    ),
}


def extract_entries(path: Path) -> list[str]:
    seen: set[str] = set()
    entries: list[str] = []
    for url in read_url_lines(path):
        if "researchgate.net/" not in url:
            print(f"  WARN: could not parse ResearchGate URL from: {url!r}")
            continue
        if url not in seen:
            seen.add(url)
            entries.append(url)
    return entries


def fetch_researchgate_fields(url: str) -> dict:
    for token, fields in _KNOWN_FIELDS_BY_TOKEN.items():
        if token in url:
            links_alt = [f"https://doi.org/{fields['doi']}"] if fields.get("doi") else []
            return {**fields, "link": url, "links_alt": links_alt}

    for token, doi in _DOI_BY_TOKEN.items():
        if token in url:
            data = fetch_with_retry(fetch_crossref, doi)
            return {
                "title": data["title"],
                "authors": data["authors"],
                "year": data["year"],
                "source": data.get("source") or "ResearchGate",
                "type": data.get("type") or "Journal Paper",
                "doi": data.get("doi") or doi,
                "abstract": data.get("abstract", ""),
                "link": url,
                "links_alt": [f"https://doi.org/{data.get('doi') or doi}"],
            }

    raise ValueError(f"No known ResearchGate metadata strategy for {url!r}")


class ResearchGatePrefill(PagePrefillScript[str]):
    description = "Prefill metadata from ResearchGate URLs."
    default_input = DEFAULT_INPUT
    entry_kind = "ResearchGate URLs"

    def extract_entries(self, path: Path) -> list[str]:
        return extract_entries(path)

    def fetch_fields(self, entry: str, _context: dict) -> dict:
        return fetch_researchgate_fields(entry)


def main() -> None:
    ResearchGatePrefill().run()


if __name__ == "__main__":
    main()
