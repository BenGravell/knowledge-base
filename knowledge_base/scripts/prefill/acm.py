"""Batch-prefill metadata.yml files from a list of ACM DL URLs.

Usage:
    python knowledge_base/scripts/prefill/acm.py [--input PATH] [--overwrite]

Defaults:
    --input      todo/papers/ACM.md
    --overwrite  False (skip entries whose metadata.yml already exists)

DOIs are extracted directly from ACM DL URLs, including URL-escaped DOI
characters, e.g.:
    https://dl.acm.org/doi/10.1145/3624480  →  10.1145/3624480
    https://dl.acm.org/doi/full/10.1145/...  →  10.1145/...
"""

from collections.abc import Callable
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests

from knowledge_base.utils.doi_utils import fetch_crossref, fetch_with_retry
from knowledge_base.utils.prefill_template import REPO_ROOT
from knowledge_base.utils.prefill_utils import extract_doi_from_url, read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "ACM.md"

Entry = tuple[str, str]

# ACM DL occasionally hosts legacy/imported records under 10.5555 pseudo-DOIs.
# Prefer the formal publisher DOI when it is known.
DOI_ALIASES = {
    "10.5555/3022473.3022494": "10.1609/aiide.v1i1.18726",
    "10.5555/2777421.2777434": "10.1287/opre.2014.1314",
    "10.5555/2095116.2095209": "10.1137/1.9781611973099.93",
}

LINK_OVERRIDES = {
    "10.5555/3022473.3022494": ("https://ojs.aaai.org/index.php/AIIDE/article/download/18726/18503"),
    "10.5555/2095116.2095209": ("https://people.csail.mit.edu/haitham/Papers/sFFT.pdf"),
}

# Some 10.5555 ACM DL records are not registered with Crossref/doi.org, and
# dl.acm.org currently blocks direct citation scraping. Keep narrow fallbacks
# for entries that are present in todo/papers/ACM.md and have stable public
# bibliographic metadata elsewhere.
FALLBACK_RECORDS = {
    "10.5555/645925.671516": {
        "title": "Similarity Search in High Dimensions via Hashing",
        "authors": [
            "Aristides Gionis",
            "Piotr Indyk",
            "Rajeev Motwani",
        ],
        "year": 1999,
        "source": "International Conference on Very Large Data Bases",
        "type": "Conference Paper",
        "doi": "10.5555/645925.671516",
        "abstract": "",
        "link": "https://www.vldb.org/conf/1999/P49.pdf",
        "links_alt": [
            "https://dl.acm.org/doi/10.5555/645925.671516",
            "https://dblp.org/rec/conf/vldb/GionisIM99",
        ],
    },
    "10.5555/1620270.1620297": {
        "title": "Maximum Entropy Inverse Reinforcement Learning",
        "authors": [
            "Brian D. Ziebart",
            "Andrew L. Maas",
            "J. Andrew Bagnell",
            "Anind K. Dey",
        ],
        "year": 2008,
        "source": "AAAI Conference on Artificial Intelligence",
        "type": "Conference Paper",
        "doi": "10.5555/1620270.1620297",
        "abstract": (
            "Recent research has shown the benefit of framing problems of imitation "
            "learning as solutions to Markov Decision Problems. This approach reduces "
            "learning to the problem of recovering a utility function that makes the "
            "behavior induced by a near-optimal policy closely mimic demonstrated "
            "behavior. In this work, we develop a probabilistic approach based on the "
            "principle of maximum entropy. Our approach provides a well-defined, "
            "globally normalized distribution over decision sequences, while providing "
            "the same performance guarantees as existing methods. We develop our "
            "technique in the context of modeling real-world navigation and driving "
            "behaviors where collected data is inherently noisy and imperfect. Our "
            "probabilistic approach enables modeling of route preferences as well as "
            "a powerful new approach to inferring destinations and routes based on "
            "partial trajectories."
        ),
        "link": "https://cdn.aaai.org/AAAI/2008/AAAI08-227.pdf",
        "links_alt": [
            "https://dl.acm.org/doi/10.5555/1620270.1620297",
            "https://dblp.org/rec/conf/aaai/ZiebartMBD08",
            "http://www.aaai.org/Library/AAAI/2008/aaai08-227.php",
        ],
    },
    "10.5555/3104482.3104578": {
        "title": "Clustering by Left-Stochastic Matrix Factorization",
        "authors": [
            "Raman Arora",
            "Maya R. Gupta",
            "Amol Kapila",
            "Maryam Fazel",
        ],
        "year": 2011,
        "source": "International Conference on Machine Learning",
        "type": "Conference Paper",
        "doi": "10.5555/3104482.3104578",
        "abstract": "",
        "link": "https://icml.cc/2011/papers/426_icmlpaper.pdf",
        "links_alt": [
            "https://dl.acm.org/doi/10.5555/3104482.3104578",
            "https://dblp.org/rec/conf/icml/AroraGKF11",
        ],
    },
    "10.5555/2283516.2283615": {
        "title": "Fast Approximate Nearest-Neighbor Search with k-Nearest Neighbor Graph",
        "authors": [
            "Kiana Hajebi",
            "Yasin Abbasi-Yadkori",
            "Hossein Shahbazi",
            "Hong Zhang",
        ],
        "year": 2011,
        "source": "International Joint Conference on Artificial Intelligence",
        "type": "Conference Paper",
        "doi": "10.5591/978-1-57735-516-8/IJCAI11-222",
        "abstract": "",
        "link": "https://www.ijcai.org/Proceedings/11/Papers/222.pdf",
        "links_alt": [
            "https://doi.org/10.5591/978-1-57735-516-8/IJCAI11-222",
            "https://dl.acm.org/doi/10.5555/2283516.2283615",
            "https://dblp.org/rec/conf/ijcai/HajebiASZ11",
        ],
    },
    "10.5555/645531.656005": {
        "title": "Approximately Optimal Approximate Reinforcement Learning",
        "authors": [
            "Sham M. Kakade",
            "John Langford",
        ],
        "year": 2002,
        "source": "International Conference on Machine Learning",
        "type": "Conference Paper",
        "doi": "10.5555/645531.656005",
        "abstract": "",
        "link": "https://mlanthology.org/icml/2002/kakade2002icml-approximately/",
        "links_alt": [
            "https://dl.acm.org/doi/10.5555/645531.656005",
            "https://dblp.org/rec/conf/icml/KakadeL02",
        ],
    },
    "10.5555/3008904.3009053": {
        "title": "The Asymptotic Convergence-Rate of Q-learning",
        "authors": [
            "Csaba Szepesvari",
        ],
        "year": 1997,
        "source": "Advances in Neural Information Processing Systems",
        "type": "Conference Paper",
        "doi": "10.5555/3008904.3009053",
        "abstract": "",
        "link": (
            "https://proceedings.neurips.cc/paper_files/paper/1997/file/cd0dce8fca267bf1fb86cf43e18d5598-Paper.pdf"
        ),
        "links_alt": [
            "https://dl.acm.org/doi/10.5555/3008904.3009053",
            "https://dblp.org/rec/conf/nips/Szepesvari97",
            (
                "https://proceedings.neurips.cc/paper_files/paper/1997/hash/"
                "cd0dce8fca267bf1fb86cf43e18d5598-Abstract.html"
            ),
        ],
    },
    "10.5555/2997189.2997253": {
        "title": "Error Propagation for Approximate Policy and Value Iteration",
        "authors": [
            "Amir Massoud Farahmand",
            "Remi Munos",
            "Csaba Szepesvari",
        ],
        "year": 2010,
        "source": "Advances in Neural Information Processing Systems",
        "type": "Conference Paper",
        "doi": "10.5555/2997189.2997253",
        "abstract": "",
        "link": (
            "https://proceedings.neurips.cc/paper_files/paper/2010/file/65cc2c8205a05d7379fa3a6386f710e1-Paper.pdf"
        ),
        "links_alt": [
            "https://dl.acm.org/doi/10.5555/2997189.2997253",
            "https://dblp.org/rec/conf/nips/FarahmandMS10",
            ("https://proceedings.neurips.cc/paper/2010/hash/65cc2c8205a05d7379fa3a6386f710e1-Abstract.html"),
        ],
    },
    "10.5555/2969442.2969525": {
        "title": "Minimax Time Series Prediction",
        "authors": [
            "Wouter M. Koolen",
            "Alan Malek",
            "Peter L. Bartlett",
            "Yasin Abbasi-Yadkori",
        ],
        "year": 2015,
        "source": "Advances in Neural Information Processing Systems",
        "type": "Conference Paper",
        "doi": "10.5555/2969442.2969525",
        "abstract": "",
        "link": (
            "https://proceedings.neurips.cc/paper_files/paper/2015/file/4dcf435435894a4d0972046fc566af76-Paper.pdf"
        ),
        "links_alt": [
            "https://dl.acm.org/doi/10.5555/2969442.2969525",
            "https://dblp.org/rec/conf/nips/KoolenMBA15",
            ("https://proceedings.neurips.cc/paper/2015/hash/4dcf435435894a4d0972046fc566af76-Abstract.html"),
        ],
    },
}

FIELD_OVERRIDES = {
    "10.1609/aiide.v1i1.18726": {
        "source": "AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment",
        "type": "Conference Paper",
    },
    "10.1137/1.9781611973099.93": {
        "source": "ACM-SIAM Symposium on Discrete Algorithms",
    },
    "10.1016/0005-1098(73)90073-3": {
        "title": "On Self-Tuning Regulators",
        "authors": [
            "Karl Johan Astrom",
            "Bjorn Wittenmark",
        ],
        "abstract": (
            "The problem of controlling a system with constant but unknown parameters "
            "is considered. The analysis is restricted to discrete time single-input "
            "single-output systems. An algorithm obtained by combining a least squares "
            "estimator with a minimum variance regulator computed from the estimated "
            "model is analysed. The main results are two theorems which characterize "
            "the closed loop system obtained under the assumption that the parameter "
            "estimates converge. The first theorem states that certain covariances of "
            "the output and certain cross-covariances of the control variable and the "
            "output will vanish under weak assumptions on the system to be controlled. "
            "In the second theorem it is assumed that the system to be controlled is a "
            "general linear stochastic nth order system. It is shown that if the "
            "parameter estimates converge the control law obtained is in fact the "
            "minimum variance control law that could be computed if the parameters of "
            "the system were known. This is somewhat surprising since the least squares "
            "estimate is biased. Some practical implications of the results are "
            "discussed. In particular it is shown that the algorithm can be feasibly "
            "implemented on a small process computer."
        ),
    },
}


def is_acm_dl_url(url: str) -> bool:
    host = urlparse(url).netloc.lower().removeprefix("www.")
    return host == "dl.acm.org"


def extract_entries(path: Path, on_parse_failure: Callable[[str], None] | None = None) -> list[Entry]:
    seen: set[str] = set()
    entries: list[Entry] = []
    for url in read_url_lines(path):
        if not is_acm_dl_url(url):
            message = f"could not parse ACM DL URL from: {url!r}"
            if on_parse_failure:
                on_parse_failure(message)
            else:
                print(f"  WARN: {message}")
            continue
        doi = extract_doi_from_url(url)
        if not doi:
            message = f"could not parse DOI from ACM DL URL: {url!r}"
            if on_parse_failure:
                on_parse_failure(message)
            else:
                print(f"  WARN: {message}")
            continue
        key = doi.lower()
        if key not in seen:
            seen.add(key)
            entries.append((url, doi))
    return entries


def extract_dois(path: Path, on_parse_failure: Callable[[str], None] | None = None) -> list[str]:
    """Backward-compatible DOI-only view for callers/tests."""
    return [doi for _url, doi in extract_entries(path, on_parse_failure)]


def entry_label(entry: Entry) -> str:
    _url, doi = entry
    return doi


def entry_doi(entry: Entry) -> str:
    _url, doi = entry
    return DOI_ALIASES.get(doi.lower(), doi)


def source_key_for_entry(entry: Entry) -> str | None:
    _url, doi = entry
    return doi


def postprocess_crossref_data(entry: Entry, data: dict[str, Any]) -> dict[str, Any]:
    url, input_doi = entry
    link = LINK_OVERRIDES.get(input_doi.lower(), url)
    return {**data, "link": link}


def fetch_fields(entry: Entry, context: dict[str, Any]) -> dict[str, Any]:
    _ = context
    url, input_doi = entry
    doi_key = input_doi.lower()
    if doi_key in FALLBACK_RECORDS:
        return {**FALLBACK_RECORDS[doi_key], "link": FALLBACK_RECORDS[doi_key]["link"]}

    try:
        fields = fetch_with_retry(fetch_crossref, entry_doi(entry))
        fields = postprocess_crossref_data(entry, fields)
    except requests.HTTPError as exc:
        if exc.response is None or exc.response.status_code != 404:
            raise
        alias = DOI_ALIASES.get(doi_key)
        if not alias:
            raise
        fields = fetch_with_retry(fetch_crossref, alias)
        fields = {**fields, "link": url}
    overrides = FIELD_OVERRIDES.get(str(fields.get("doi") or "").lower())
    return {**fields, **overrides} if overrides else fields


def postprocess_metadata(entry: Entry, fields: dict[str, Any], metadata: dict[str, Any]) -> dict[str, Any]:
    _url, input_doi = entry
    doi = str(fields.get("doi") or entry_doi(entry) or "").strip()
    links_alt = list(metadata.get("links_alt") or [])
    links_alt.extend(fields.get("links_alt") or [])
    if doi and input_doi.lower() not in FALLBACK_RECORDS:
        links_alt.append(f"https://doi.org/{doi}")
    if input_doi != doi and input_doi.startswith("10."):
        links_alt.append(f"https://dl.acm.org/doi/{input_doi}")
    links_alt = list(dict.fromkeys(x for x in links_alt if x and x != metadata.get("link")))
    return {**metadata, "links_alt": links_alt}
