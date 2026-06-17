"""Batch-prefill metadata.yml files from ResearchGate URLs."""

from collections.abc import Callable
from pathlib import Path
from typing import Any

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.doi_utils import fetch_crossref, fetch_with_retry
from knowledge_base.utils.prefill_template import REPO_ROOT
from knowledge_base.utils.prefill_utils import read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "RESEARCHGATE.md"

_KNOWN_FIELDS_BY_TOKEN: dict[str, dict[str, Any]] = {
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
    "New_stochastic_approximation_type_procedures": {
        "title": "New Stochastic Approximation Type Procedures",
        "authors": ["Boris T. Polyak"],
        "year": 1990,
        "source": "Avtomatika i Telemekhanika",
        "type": "Journal Paper",
        "doi": None,
        "abstract": "",
        "link": "https://www.researchgate.net/publication/236736759",
    },
    "Efficient_estimators_from_a_slowly_converging_robbins-monro_process": {
        "title": "Efficient Estimators from a Slowly Converging Robbins-Monro Process",
        "authors": ["David Ruppert"],
        "year": 1988,
        "source": "Cornell University School of Operations Research and Industrial Engineering Technical Report 781",
        "type": "Technical Report",
        "doi": None,
        "abstract": "",
        "link": "https://www.researchgate.net/publication/242608650",
    },
    "Beyond_Regression_New_Tools_for_Prediction_and_Analysis_in_the_Behavioral_Science": {
        "title": "Beyond Regression: New Tools for Prediction and Analysis in the Behavioral Sciences",
        "authors": ["Paul John Werbos"],
        "year": 1974,
        "source": "Harvard University",
        "type": "PhD Dissertation",
        "doi": None,
        "abstract": "",
        "link": "https://gwern.net/doc/ai/nn/1974-werbos.pdf",
    },
    "Path_Integral_Policy_Improvement_An_Information-Geometric_Optimization_Approach": {
        "title": "Path Integral Policy Improvement: An Information-Geometric Approach",
        "authors": ["Peter Varnai", "Dimos V. Dimarogonas"],
        "year": 2020,
        "source": "ResearchGate",
        "type": "Preprint",
        "doi": "10.13140/RG.2.2.13969.76645",
        "abstract": "",
        "link": "https://doi.org/10.13140/RG.2.2.13969.76645",
    },
}
_DOI_BY_TOKEN = {
    "The_BOSS_is_concerned_with_time_series_classification_in_the_presence_of_noise": ("10.1007/s10618-014-0377-7"),
}


def extract_entries(path: Path, on_parse_failure: Callable[[str], None] | None = None) -> list[str]:
    seen: set[str] = set()
    entries: list[str] = []
    for url in read_url_lines(path):
        if "researchgate.net/" not in url:
            message = f"could not parse ResearchGate URL from: {url!r}"
            if on_parse_failure:
                on_parse_failure(message)
            else:
                print(f"  WARN: {message}")
            continue
        if url not in seen:
            seen.add(url)
            entries.append(url)
    return entries


def fetch_researchgate_fields(url: str) -> dict[str, Any]:
    for token, fields in _KNOWN_FIELDS_BY_TOKEN.items():
        if token in url:
            link = fields.get("link") or url
            links_alt_raw = fields.get("links_alt")
            links_alt = list(links_alt_raw) if isinstance(links_alt_raw, list) else []
            if link != url:
                links_alt.append(url)
            if fields.get("doi"):
                links_alt.append(f"https://doi.org/{fields['doi']}")
            links_alt = list(dict.fromkeys(x for x in links_alt if x and x != link))
            return {**fields, "link": link, "links_alt": links_alt}

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


def fetch_fields(entry: str, context: dict[str, Any]) -> dict[str, Any]:
    _ = context
    return fetch_researchgate_fields(entry)
