"""Refine staged arXiv metadata entries with official publication data."""

from __future__ import annotations

import json
import html
import re
import subprocess
import time
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any
from urllib.parse import quote

import requests
import yaml

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[2]))

from knowledge_base.scripts.enrich_existing_arxiv_metadata import dump_yaml

CACHE_PATH = Path("/tmp/kb_refine_staged_arxiv_metadata_cache.json")
SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "knowledge-base metadata audit (mailto:none)"})

ARXIV_URL_RE = re.compile(r"(?:arxiv\.org|ar5iv\.labs\.arxiv\.org)", re.IGNORECASE)
ARXIV_DOI_RE = re.compile(r"10\.48550/arxiv", re.IGNORECASE)


PHRASE_TAGS: tuple[tuple[str, str], ...] = (
    ("affine rank minimization", "Affine rank minimization"),
    ("rank minimization", "Rank minimization"),
    ("minimum rank", "Minimum rank"),
    ("low-rank", "Low-rank models"),
    ("low rank", "Low-rank models"),
    ("matrix completion", "Matrix completion"),
    ("matrix factorization", "Matrix factorization"),
    ("linear matrix equation", "Linear matrix equations"),
    ("nuclear norm", "Nuclear norm minimization"),
    ("restricted isometry", "Restricted isometry property"),
    ("compressed sensing", "Compressed sensing"),
    ("convex optimization", "Convex optimization"),
    ("convex relaxation", "Convex relaxation"),
    ("semidefinite", "Semidefinite programming"),
    ("linear programming", "Linear programming"),
    ("integer programming", "Integer programming"),
    ("nonconvex", "Nonconvex optimization"),
    ("stochastic optimization", "Stochastic optimization"),
    ("gradient descent", "Gradient descent"),
    ("stochastic gradient", "Stochastic gradients"),
    ("natural gradient", "Natural gradients"),
    ("mirror descent", "Mirror descent"),
    ("policy gradient", "Policy gradients"),
    ("reinforcement learning", "Reinforcement learning"),
    ("inverse reinforcement learning", "Inverse reinforcement learning"),
    ("imitation learning", "Imitation learning"),
    ("q-learning", "Q-learning"),
    ("markov decision process", "Markov decision processes"),
    ("partially observable", "Partial observability"),
    ("bellman", "Bellman equations"),
    ("policy iteration", "Policy iteration"),
    ("value iteration", "Value iteration"),
    ("multi-agent", "Multi-agent systems"),
    ("multiagent", "Multi-agent systems"),
    ("game theory", "Game theory"),
    ("bandit", "Bandits"),
    ("regret", "Regret bounds"),
    ("optimal control", "Optimal control"),
    ("model predictive control", "Model predictive control"),
    ("predictive control", "Predictive control"),
    ("trajectory optimization", "Trajectory optimization"),
    ("motion planning", "Motion planning"),
    ("path planning", "Path planning"),
    ("robot", "Robotics"),
    ("quadrotor", "Aerial robotics"),
    ("autonomous driving", "Autonomous driving"),
    ("vehicle", "Vehicles"),
    ("control barrier", "Control barrier functions"),
    ("control lyapunov", "Control Lyapunov functions"),
    ("lyapunov", "Lyapunov methods"),
    ("stability", "Stability analysis"),
    ("safe", "Safety"),
    ("safety", "Safety"),
    ("robust", "Robustness"),
    ("uncertainty", "Uncertainty"),
    ("gaussian process", "Gaussian processes"),
    ("kalman", "Kalman filtering"),
    ("system identification", "System identification"),
    ("state estimation", "State estimation"),
    ("neural network", "Neural networks"),
    ("deep learning", "Deep learning"),
    ("convolutional", "Convolutional networks"),
    ("recurrent neural", "Recurrent neural networks"),
    ("transformer", "Transformers"),
    ("attention", "Attention mechanisms"),
    ("graph neural", "Graph neural networks"),
    ("graph convolution", "Graph neural networks"),
    ("diffusion model", "Diffusion models"),
    ("diffusion", "Diffusion models"),
    ("generative adversarial", "Generative adversarial networks"),
    ("variational autoencoder", "Variational autoencoders"),
    ("autoencoder", "Autoencoders"),
    ("large language model", "Large language models"),
    ("language model", "Language models"),
    ("foundation model", "Foundation models"),
    ("vision-language", "Vision-language models"),
    ("vision language", "Vision-language models"),
    ("image generation", "Image generation"),
    ("computer vision", "Computer vision"),
    ("object detection", "Object detection"),
    ("semantic segmentation", "Semantic segmentation"),
    ("image segmentation", "Image segmentation"),
    ("pose estimation", "Pose estimation"),
    ("optical flow", "Optical flow"),
    ("representation learning", "Representation learning"),
    ("self-supervised", "Self-supervised learning"),
    ("semi-supervised", "Semi-supervised learning"),
    ("supervised learning", "Supervised learning"),
    ("unsupervised learning", "Unsupervised learning"),
    ("federated learning", "Federated learning"),
    ("meta-learning", "Meta-learning"),
    ("few-shot", "Few-shot learning"),
    ("transfer learning", "Transfer learning"),
    ("bayesian", "Bayesian methods"),
    ("probabilistic", "Probabilistic models"),
    ("causal", "Causal inference"),
    ("graph", "Graphs"),
    ("nearest neighbor", "Nearest neighbors"),
    ("clustering", "Clustering"),
    ("classification", "Classification"),
    ("regression", "Regression"),
    ("time series classification", "Time series classification"),
    ("time series", "Time series"),
    ("computational complexity", "Computational complexity"),
    ("convolutional kernel", "Convolutional kernels"),
    ("linear classifier", "Linear classifiers"),
    ("deterministic transform", "Deterministic transforms"),
    ("state-of-the-art", "State of the art"),
    ("ucr archive", "UCR archive"),
    ("classifier", "Classifiers"),
    ("dataset", "Datasets"),
    ("benchmark", "Benchmarks"),
    ("accuracy", "Accuracy"),
    ("scalability", "Scalability"),
    ("real-time", "Real-time systems"),
    ("online", "Online algorithms"),
    ("offline", "Offline algorithms"),
    ("sampling-based", "Sampling-based methods"),
    ("sampling based", "Sampling-based methods"),
    ("search tree", "Search trees"),
    ("nearest-neighbor", "Nearest neighbors"),
    ("collaborative filtering", "Collaborative filtering"),
    ("euclidean embedding", "Euclidean embedding"),
    ("information retrieval", "Information retrieval"),
    ("ranking", "Ranking"),
    ("privacy", "Privacy"),
    ("differential privacy", "Differential privacy"),
    ("security", "Security"),
    ("cryptograph", "Cryptography"),
    ("distributed", "Distributed systems"),
    ("parallel computing", "Parallel computing"),
    ("linear equality constraint", "Linear equality constraints"),
    ("minimum-rank solution", "Minimum-rank solutions"),
    ("linear transformation", "Linear transformations"),
    ("cardinality minimization", "Cardinality minimization"),
    ("random ensemble", "Random ensembles"),
    ("np-hard", "NP-hardness"),
    ("sample complexity", "Sample complexity"),
    ("generalization", "Generalization"),
    ("out-of-distribution", "Out-of-distribution generalization"),
    ("optimization", "Optimization"),
    ("planning", "Planning"),
    ("control", "Control"),
    ("learning", "Learning"),
    ("sampling", "Sampling"),
    ("monte carlo", "Monte Carlo methods"),
    ("variational inference", "Variational inference"),
    ("normalizing flow", "Normalizing flows"),
    ("optimal transport", "Optimal transport"),
    ("wasserstein", "Wasserstein distances"),
)

TAG_STOPWORDS = {
    "a",
    "an",
    "and",
    "as",
    "by",
    "for",
    "from",
    "in",
    "into",
    "of",
    "on",
    "or",
    "the",
    "to",
    "via",
    "with",
    "without",
}

GENERIC_OPENALEX_TAGS = {
    "algorithm",
    "algorithms",
    "artificial intelligence",
    "computer science",
    "engineering",
    "mathematics",
    "method",
    "methods",
    "physics",
}
SENTENCE_LIKE_TAG_START_RE = re.compile(
    r"^(?:"
    r"we\b|"
    r"i\b|"
    r"our\b|"
    r"this\s+(?:paper|work|article|study)\b|"
    r"the\s+(?:paper|work|article|study|authors?)\b|"
    r"in\s+this\s+(?:paper|work|article|study)\b"
    r")",
    re.IGNORECASE,
)
SENTENCE_LIKE_TAG_CLAUSE_RE = re.compile(
    r"\b(?:argue|argues|show|shows|prove|proves|demonstrate|demonstrates|"
    r"present|presents|propose|proposes|introduce|introduces|study|studies|"
    r"investigate|investigates|claim|claims)\s+that\b",
    re.IGNORECASE,
)


def load_cache() -> dict[str, Any]:
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    return {}


def save_cache(cache: dict[str, Any]) -> None:
    CACHE_PATH.write_text(json.dumps(cache, sort_keys=True), encoding="utf-8")


def clean_space(text: str | None) -> str:
    return re.sub(r"\s+", " ", html.unescape(text or "")).strip()


def sentence_like_tag(text: str) -> bool:
    text = clean_space(text)
    if not text:
        return False
    if SENTENCE_LIKE_TAG_START_RE.search(text):
        return True
    if SENTENCE_LIKE_TAG_CLAUSE_RE.search(text):
        return True
    words = re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text)
    return len(words) >= 7 and bool(
        re.search(r"\b(?:that|because|while|although|where|which|who|whose|when)\b", text, re.IGNORECASE)
    )


def bare_arxiv_id(arxiv_id: str | None) -> str:
    return re.sub(r"v\d+$", "", clean_space(arxiv_id))


def normalize_title(text: str | None) -> str:
    return re.sub(r"[^a-z0-9]+", " ", clean_space(text).lower()).strip()


def title_similarity(left: str, right: str) -> float:
    return SequenceMatcher(None, normalize_title(left), normalize_title(right)).ratio()


def fetch_json(cache: dict[str, Any], key: str, url: str) -> dict[str, Any]:
    if key in cache:
        return cache[key]
    response = SESSION.get(url, timeout=60)
    if response.status_code == 404:
        cache[key] = {}
    else:
        response.raise_for_status()
        cache[key] = response.json()
    save_cache(cache)
    time.sleep(0.25)
    return cache[key]


def crossref_for_doi(cache: dict[str, Any], doi: str) -> dict[str, Any]:
    if not doi or ARXIV_DOI_RE.search(doi):
        return {}
    url = f"https://api.crossref.org/works/{quote(doi, safe='')}"
    payload = fetch_json(cache, f"crossref:{doi.lower()}", url)
    return payload.get("message") or {}


def openalex_for_title(cache: dict[str, Any], title: str) -> dict[str, Any]:
    url = f"https://api.openalex.org/works?search={quote(title)}&per-page=5"
    payload = fetch_json(cache, f"openalex:title:{normalize_title(title)}", url)
    results = payload.get("results") or []
    best: dict[str, Any] = {}
    best_score = 0.0
    for result in results:
        score = title_similarity(title, result.get("title") or result.get("display_name") or "")
        if score > best_score:
            best = result
            best_score = score
    return best if best_score >= 0.94 else {}


def official_location(work: dict[str, Any]) -> dict[str, Any]:
    locations = [work.get("primary_location") or {}, *(work.get("locations") or [])]
    for location in locations:
        source = location.get("source") or {}
        source_name = (source.get("display_name") or location.get("raw_source_name") or "").lower()
        source_type = (source.get("type") or "").lower()
        if source_type == "repository" or "arxiv" in source_name:
            continue
        if location.get("is_published") or location.get("version") == "publishedVersion":
            return location
    for location in locations:
        source = location.get("source") or {}
        source_name = (source.get("display_name") or location.get("raw_source_name") or "").lower()
        source_type = (source.get("type") or "").lower()
        if source_type != "repository" and "arxiv" not in source_name:
            return location
    return {}


def crossref_type_to_metadata(work: dict[str, Any]) -> tuple[str, str]:
    container = next(iter(work.get("container-title") or []), "")
    work_type = work.get("type") or ""
    name = container.lower()
    if "workshop" in name:
        item_type = "Workshop Paper"
    elif work_type == "journal-article":
        item_type = "Journal Paper"
    elif work_type == "proceedings-article" or "proceedings" in name or "conference" in name:
        item_type = "Conference Paper"
    elif work_type == "posted-content":
        item_type = "Preprint"
    else:
        item_type = "Other"
    return clean_space(container), item_type


def openalex_type_to_metadata(work: dict[str, Any], location: dict[str, Any]) -> tuple[str, str]:
    source = location.get("source") or {}
    source_name = clean_space(source.get("display_name") or location.get("raw_source_name") or "")
    source_type = (source.get("type") or "").lower()
    raw_type = (location.get("raw_type") or work.get("type_crossref") or work.get("type") or "").lower()
    name = source_name.lower()
    if "workshop" in name:
        item_type = "Workshop Paper"
    elif source_type == "journal" or raw_type == "journal-article":
        item_type = "Journal Paper"
    elif source_type == "conference" or raw_type == "proceedings-article" or "proceedings" in name:
        item_type = "Conference Paper"
    else:
        item_type = "Other"
    return clean_space(source_name), item_type


def official_links_from_crossref(work: dict[str, Any]) -> list[str]:
    links = [work.get("URL") or ""]
    resource = (work.get("resource") or {}).get("primary") or {}
    links.append(resource.get("URL") or "")
    for link in work.get("link") or []:
        url = link.get("URL") or ""
        if url:
            links.append(url)
    return clean_links(links)


def official_links_from_openalex(work: dict[str, Any], location: dict[str, Any]) -> list[str]:
    links = []
    doi = (work.get("doi") or "").replace("https://doi.org/", "")
    if doi and not ARXIV_DOI_RE.search(doi):
        links.append(f"https://doi.org/{doi}")
    for candidate in (
        location.get("landing_page_url"),
        location.get("pdf_url"),
        (work.get("primary_location") or {}).get("landing_page_url"),
    ):
        if candidate:
            links.append(candidate)
    return clean_links(links)


def clean_links(links: list[str]) -> list[str]:
    cleaned: list[str] = []
    for link in links:
        link = clean_space(link)
        if not link or ARXIV_URL_RE.search(link):
            continue
        if link not in cleaned:
            cleaned.append(link)
    return cleaned


def add_unique(items: list[str], item: str) -> None:
    item = clean_space(item)
    if item and item not in items:
        items.append(item)


def display_to_tag(display: str) -> str:
    display = re.sub(r"\s*\([^)]*\)", "", clean_space(display))
    return display[:1].upper() + display[1:] if display else ""


def openalex_literal_tags(work: dict[str, Any], title: str, abstract: str) -> list[str]:
    corpus = normalize_title(f"{title} {abstract}")
    tags: list[str] = []
    candidates: list[str] = []
    for keyword in work.get("keywords") or []:
        candidates.append(keyword.get("display_name") or "")
    for topic in work.get("topics") or []:
        candidates.append(topic.get("display_name") or "")
    primary_topic = work.get("primary_topic") or {}
    candidates.append(primary_topic.get("display_name") or "")

    for candidate in candidates:
        tag = display_to_tag(candidate)
        needle = normalize_title(tag)
        if not needle or needle in GENERIC_OPENALEX_TAGS:
            continue
        if len(needle.split()) < 2 and not re.fullmatch(r"[A-Z0-9+_.-]{2,}", tag):
            continue
        if needle in corpus:
            add_unique(tags, tag)
    return tags[:10]


def phrase_tags(title: str, abstract: str, algorithm: str | None, openalex: dict[str, Any] | None = None) -> list[str]:
    corpus = f"{title} {abstract}".lower()
    tags: list[str] = []
    for needle, tag in PHRASE_TAGS:
        if needle in corpus and tag not in tags:
            tags.append(tag)

    if algorithm and algorithm not in tags:
        if re.search(rf"\b{re.escape(algorithm.lower())}\b", corpus):
            tags.append(algorithm)

    for long_name, acronym in re.findall(r"([A-Za-z][A-Za-z0-9+_. -]{3,80}?)\s*\(([A-Z][A-Z0-9+_.-]{1,16})\)", f"{title} {abstract}"):
        long_name = clean_space(long_name).strip(" ,.;:")
        if 2 <= len(long_name.split()) <= 7 and not sentence_like_tag(long_name):
            tag = long_name[:1].upper() + long_name[1:]
            if tag not in tags:
                tags.append(tag)
        if acronym not in tags:
            tags.append(acronym)

    if openalex:
        for tag in openalex_literal_tags(openalex, title, abstract):
            add_unique(tags, tag)

    return tags[:20]


def staged_metadata_files() -> list[Path]:
    output = subprocess.check_output(
        ["git", "diff", "--cached", "--name-only", "--", "knowledge_base/docs/papers/**/metadata.yml"],
        text=True,
    )
    return [Path(line) for line in output.splitlines() if line.strip()]


def refine(path: Path, cache: dict[str, Any]) -> bool:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    before = dump_yaml(data)

    arxiv_id = bare_arxiv_id(data.get("arxiv_id"))
    data["arxiv_id"] = arxiv_id or None
    if arxiv_id and ARXIV_URL_RE.search(str(data.get("link") or "")):
        data["link"] = f"https://arxiv.org/pdf/{arxiv_id}"
    data["links_alt"] = clean_links(list(data.get("links_alt") or []))

    title = data.get("title") or ""
    abstract = data.get("abstract") or ""
    doi = data.get("doi") or ""
    official_source = ""
    official_type = ""
    official_links: list[str] = []

    crossref = crossref_for_doi(cache, doi)
    if crossref:
        official_source, official_type = crossref_type_to_metadata(crossref)
        official_links = official_links_from_crossref(crossref)
        official_doi = crossref.get("DOI")
        if official_doi and not ARXIV_DOI_RE.search(official_doi):
            data["doi"] = official_doi

    openalex = openalex_for_title(cache, title)
    if not official_source:
        location = official_location(openalex) if openalex else {}
        if location:
            official_source, official_type = openalex_type_to_metadata(openalex, location)
            official_links = official_links_from_openalex(openalex, location)
            official_doi = (openalex.get("doi") or "").replace("https://doi.org/", "")
            if official_doi and not ARXIV_DOI_RE.search(official_doi):
                data["doi"] = official_doi

    if official_source and official_type:
        data["source"] = official_source
        data["type"] = official_type
    elif not data.get("source"):
        data["source"] = "arXiv"
        data["type"] = "Preprint"

    tags = phrase_tags(title, abstract, data.get("algorithm"), openalex)
    data["tags"] = tags or list(data.get("tags") or [])

    links = list(data.get("links_alt") or [])
    for link in official_links:
        if link not in links:
            links.append(link)
    data["links_alt"] = clean_links(links)
    data["audit_status"] = "raw"

    after = dump_yaml(data)
    if after != before:
        path.write_text(after, encoding="utf-8")
        return True
    return False


def main() -> None:
    cache = load_cache()
    files = staged_metadata_files()
    updated = 0
    official = 0
    for idx, path in enumerate(files, 1):
        before = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        changed = refine(path, cache)
        after = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if changed:
            updated += 1
        if after.get("source") != "arXiv" or after.get("type") != "Preprint":
            official += 1
        if idx % 25 == 0:
            print(f"{idx}/{len(files)} processed; {updated} updated; {official} official venues")
    print(f"Done: {len(files)} processed, {updated} updated, {official} with official venue/type")


if __name__ == "__main__":
    main()
