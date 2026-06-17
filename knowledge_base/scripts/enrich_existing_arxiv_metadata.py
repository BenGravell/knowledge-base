"""Enrich existing raw arXiv metadata.yml files from the arXiv Atom API.

This updates already-created metadata entries in place. It is intentionally
conservative: factual bibliographic fields come from arXiv, while tags are
derived from arXiv categories and abstracts.
"""

from __future__ import annotations

import argparse
import re
import textwrap
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import requests
import yaml

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[2]))

from knowledge_base.config import KB_DIR, VALID_FIELDS
from knowledge_base.utils.arxiv_utils import (
    ARXIV_API,
    ARXIV_HEADERS,
    ARXIV_NS,
    arxiv_abs_url,
    arxiv_html_url,
    arxiv_pdf_url,
    normalize_arxiv_id,
)

ARXIV_SCHEMA_NS = "http://arxiv.org/schemas/atom"
PAPERS_ROOT = KB_DIR / "docs" / "papers"
BASE_DELAY = 3.2

CATEGORY_TAGS = {
    "cs.AI": "Artificial intelligence",
    "cs.AR": "Computer architecture",
    "cs.CC": "Computational complexity",
    "cs.CE": "Computational engineering",
    "cs.CG": "Computational geometry",
    "cs.CL": "Natural language processing",
    "cs.CR": "Cryptography and security",
    "cs.CV": "Computer vision",
    "cs.CY": "Computers and society",
    "cs.DB": "Databases",
    "cs.DC": "Distributed computing",
    "cs.DL": "Digital libraries",
    "cs.DM": "Discrete mathematics",
    "cs.DS": "Data structures and algorithms",
    "cs.ET": "Emerging technologies",
    "cs.FL": "Formal languages",
    "cs.GL": "General literature",
    "cs.GR": "Computer graphics",
    "cs.GT": "Game theory",
    "cs.HC": "Human-computer interaction",
    "cs.IR": "Information retrieval",
    "cs.IT": "Information theory",
    "cs.LG": "Machine learning",
    "cs.LO": "Logic in computer science",
    "cs.MA": "Multiagent systems",
    "cs.MM": "Multimedia",
    "cs.MS": "Mathematical software",
    "cs.NA": "Numerical analysis",
    "cs.NE": "Neural computing",
    "cs.NI": "Networking",
    "cs.OH": "Other computer science",
    "cs.OS": "Operating systems",
    "cs.PF": "Performance",
    "cs.PL": "Programming languages",
    "cs.RO": "Robotics",
    "cs.SC": "Symbolic computation",
    "cs.SD": "Sound",
    "cs.SE": "Software engineering",
    "cs.SI": "Social and information networks",
    "cs.SY": "Systems and control",
    "eess.AS": "Audio and speech processing",
    "eess.IV": "Image and video processing",
    "eess.SP": "Signal processing",
    "eess.SY": "Systems and control",
    "math.OC": "Optimization and control",
    "math.NA": "Numerical analysis",
    "math.PR": "Probability",
    "math.ST": "Statistics theory",
    "stat.ML": "Machine learning",
    "stat.TH": "Statistics theory",
}

KEYWORD_TAGS = (
    ("reinforcement learning", "Reinforcement learning"),
    ("imitation learning", "Imitation learning"),
    ("inverse reinforcement learning", "Inverse reinforcement learning"),
    ("optimal control", "Optimal control"),
    ("model predictive control", "Model predictive control"),
    ("trajectory optimization", "Trajectory optimization"),
    ("motion planning", "Motion planning"),
    ("path planning", "Path planning"),
    ("diffusion", "Diffusion models"),
    ("transformer", "Transformers"),
    ("large language model", "Large language models"),
    ("foundation model", "Foundation models"),
    ("neural network", "Neural networks"),
    ("deep learning", "Deep learning"),
    ("graph neural", "Graph neural networks"),
    ("bayesian", "Bayesian methods"),
    ("convex optimization", "Convex optimization"),
    ("nonconvex", "Nonconvex optimization"),
    ("stochastic optimization", "Stochastic optimization"),
    ("linear quadratic", "Linear quadratic control"),
    ("lyapunov", "Lyapunov methods"),
    ("safety", "Safety"),
    ("safe", "Safety"),
    ("robust", "Robustness"),
    ("uncertainty", "Uncertainty"),
    ("gaussian process", "Gaussian processes"),
    ("markov decision process", "Markov decision processes"),
    ("mdp", "Markov decision processes"),
    ("partially observable", "Partial observability"),
    ("pompd", "Partial observability"),
    ("multi-agent", "Multi-agent systems"),
    ("multiagent", "Multi-agent systems"),
    ("autonomous driving", "Autonomous driving"),
    ("robot", "Robotics"),
    ("quadrotor", "Aerial robotics"),
    ("aerial", "Aerial robotics"),
    ("vehicle", "Vehicles"),
)


@dataclass
class ArxivRecord:
    arxiv_id: str
    title: str
    authors: list[str]
    year: int
    abstract: str
    doi: str
    journal_ref: str
    comment: str
    primary_category: str
    categories: list[str]


def clean_space(text: str | None) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def bare_arxiv_id(arxiv_id: str | None) -> str:
    return re.sub(r"v\d+$", "", normalize_arxiv_id(arxiv_id))


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def dump_yaml(data: dict[str, Any]) -> str:
    lines: list[str] = []

    def add_scalar(key: str, value: Any) -> None:
        if value is None:
            lines.append(f"{key}:")
        elif key == "arxiv_id" and value:
            lines.append(f'{key}: "{value}"')
        elif isinstance(value, str) and ("\n" in value or len(value) > 80):
            lines.append(f"{key}: >")
            lines.extend(
                f"  {line}" for line in textwrap.wrap(value, width=100, break_long_words=False, break_on_hyphens=False)
            )
        elif isinstance(value, str):
            dumped = yaml.safe_dump({key: value}, sort_keys=False, allow_unicode=True).strip()
            lines.extend(dumped.splitlines())
        else:
            lines.append(f"{key}: {value}")

    for key in VALID_FIELDS:
        value = data.get(key)
        if isinstance(value, list):
            lines.append(f"{key}:")
            lines.extend(f"  - {item}" for item in value)
        else:
            add_scalar(key, value)

    return "\n".join(lines) + "\n"


TOP_LEVEL_FIELD_RE = re.compile(r"^(?P<key>[A-Za-z_][A-Za-z0-9_]*):(?P<value>[^\n\r]*)(?P<newline>\r?\n?)$")


def top_level_field_span(lines: list[str], start: int) -> tuple[str, str, int] | None:
    match = TOP_LEVEL_FIELD_RE.match(lines[start])
    if not match:
        return None

    field_name = match.group("key")
    value = match.group("value")
    end = start + 1
    if value.lstrip().startswith(("|", ">")) or (end < len(lines) and lines[end].startswith((" ", "\t"))):
        while end < len(lines):
            next_line = lines[end]
            if next_line.strip() and not next_line.startswith((" ", "\t")):
                break
            end += 1

    return field_name, value, end


def format_scalar_line(field_name: str, value: object, newline: str = "\n") -> str:
    if value is None or value == "":
        return f"{field_name}:{newline}"

    dumped = yaml.safe_dump(
        {field_name: value},
        sort_keys=False,
        allow_unicode=True,
        width=1_000_000_000,
    ).strip()
    return f"{dumped}{newline}"


def replace_scalar_field(raw: str, field_name: str, value: object) -> str:
    lines = raw.splitlines(keepends=True)
    for start, line in enumerate(lines):
        parsed = top_level_field_span(lines, start)
        if parsed is None:
            continue

        current_field, _current_value, end = parsed
        if current_field != field_name:
            continue

        match = TOP_LEVEL_FIELD_RE.match(line)
        newline = match.group("newline") if match else "\n"
        replacement = format_scalar_line(field_name, value, newline or "\n")
        return "".join([*lines[:start], replacement, *lines[end:]])

    prefix = raw if raw.endswith("\n") or not raw else f"{raw}\n"
    return f"{prefix}{format_scalar_line(field_name, value)}"


def title_case_ascii(title: str) -> str:
    # Keep acronyms/math-ish tokens intact while matching the repository's
    # title-case expectation closely enough for audit.
    small = {
        "a",
        "an",
        "and",
        "as",
        "at",
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
    words = re.split(r"(\s+)", clean_space(title))
    cased: list[str] = []
    word_positions = [i for i, token in enumerate(words) if token.strip()]
    first_last = {word_positions[0], word_positions[-1]} if word_positions else set()
    for i, token in enumerate(words):
        if not token.strip():
            cased.append(token)
            continue
        bare = token.strip(",:;()[]{}")
        if any(ch.isupper() for ch in bare[1:]) or any(ch.isdigit() for ch in bare) or "\\" in bare or "$" in bare:
            cased.append(token)
            continue
        lower = token.lower()
        if i not in first_last and lower in small:
            cased.append(lower)
        else:
            cased.append(token[:1].upper() + token[1:].lower())
    return "".join(cased)


def build_tags(record: ArxivRecord) -> list[str]:
    tags: list[str] = []
    for category in record.categories:
        tag = CATEGORY_TAGS.get(category)
        if tag and tag not in tags:
            tags.append(tag)
    corpus = f"{record.title} {record.abstract}".lower()
    for needle, tag in KEYWORD_TAGS:
        if needle in corpus and tag not in tags:
            tags.append(tag)
    return tags[:12]


GENERIC_ALGORITHMS = {
    "ai",
    "algorithm",
    "algorithms",
    "approach",
    "architecture",
    "basis",
    "conservative",
    "constraints",
    "control",
    "deployment",
    "descent",
    "design",
    "did",
    "different",
    "efficient",
    "estimation",
    "fast",
    "feedback",
    "flow",
    "framework",
    "gradient",
    "guarantee",
    "hessian",
    "inference",
    "interface",
    "iteration",
    "learning",
    "metric",
    "method",
    "methods",
    "mixing",
    "model",
    "models",
    "need",
    "noising",
    "optimization",
    "past",
    "planning",
    "plus",
    "policy",
    "regret",
    "robotics",
    "scale",
    "search",
    "sparsity",
    "space",
    "stability",
    "strategy",
    "survey",
    "systems",
    "tasks",
    "transforms",
    "transport",
    "vehicles",
    "work",
}
TITLE_PREFIX_REJECT_WORDS = {
    "a",
    "all",
    "an",
    "and",
    "as",
    "beyond",
    "by",
    "for",
    "from",
    "in",
    "is",
    "of",
    "on",
    "the",
    "this",
    "to",
    "toward",
    "towards",
    "under",
    "using",
    "via",
    "when",
    "with",
    "without",
    "you",
}


def _algorithm_tokens(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9+_.*-]+", text)


def _is_strong_algorithm_token(token: str) -> bool:
    token = token.strip(".,;:()[]{}")
    if not token or token.lower() in GENERIC_ALGORITHMS:
        return False
    return bool(
        re.fullmatch(r"[A-Z][A-Z0-9+_.-]{2,16}", token)
        or re.search(r"[a-z][A-Z]", token)
        or ("*" in token and re.search(r"[A-Za-z]", token))
        or ("+" in token and re.search(r"[A-Za-z]", token))
    )


def algorithm_like(text: str) -> bool:
    text = clean_space(text)
    if text.lower() in GENERIC_ALGORITHMS:
        return False
    tokens = _algorithm_tokens(text)
    if not tokens:
        return False

    if any(_is_strong_algorithm_token(token) for token in tokens):
        return True

    # Allow compact named releases such as "Llama 2", but do not let digits or
    # hyphens inside broad title phrases make the whole phrase look algorithmic.
    return bool(len(tokens) <= 2 and any(any(ch.isdigit() for ch in token) for token in tokens))


def title_prefix_like_algorithm(text: str) -> bool:
    text = clean_space(text)
    tokens = _algorithm_tokens(text)
    if not tokens or len(tokens) > 6:
        return False

    folded_tokens = [token.casefold() for token in tokens]
    if any(token in TITLE_PREFIX_REJECT_WORDS for token in folded_tokens):
        return False
    if text.casefold() in GENERIC_ALGORITHMS:
        return False
    if algorithm_like(text):
        return True

    if len(tokens) <= 4:
        has_specific_token = False
        for token in tokens:
            stripped = token.strip(".,;:()[]{}")
            if stripped.casefold() in GENERIC_ALGORITHMS:
                continue
            if re.fullmatch(r"[A-Z][A-Za-z0-9+_.-]{1,24}", stripped):
                has_specific_token = True
                continue
            if len(tokens) == 1 and re.fullmatch(r"[a-z][a-z0-9+_.-]{2,24}", stripped):
                has_specific_token = True
                continue
            return False
        return has_specific_token

    return False


def extract_named_method(text: str) -> str:
    match = re.search(
        r"\b(?:introduce|introduces|propose|proposes|present|presents|develop|develops)\s+"
        r"(?:a|an|the)?\s*([A-Za-z][A-Za-z0-9+_. -]{3,90}?)\s*\(([A-Z][A-Z0-9+_.-]{1,16})\)",
        text,
    )
    if not match:
        return ""
    acronym = match.group(2).strip()
    return acronym if algorithm_like(acronym) else ""


def infer_algorithm(record: ArxivRecord) -> str:
    title = clean_space(record.title)
    abstract = clean_space(record.abstract)
    named_method = extract_named_method(f"{title} {abstract}")
    if named_method:
        return named_method
    for pattern in (r"\b(?:introduce|introduces|propose|proposes|present|presents)\s+([A-Z][A-Za-z0-9+_-]{1,24})\b",):
        match = re.search(pattern, title)
        if match and algorithm_like(match.group(1)):
            return match.group(1).strip()
    if ":" in title:
        head = title.split(":", 1)[0].strip()
        if not head.lower().startswith(("a ", "an ", "the ")) and title_prefix_like_algorithm(head):
            return head
    return ""


def parse_entry(entry: ET.Element, requested_id: str) -> ArxivRecord:
    def atom_text(tag: str) -> str:
        el = entry.find(f"{{{ARXIV_NS}}}{tag}")
        return clean_space(el.text if el is not None else "")

    def arxiv_text(tag: str) -> str:
        el = entry.find(f"{{{ARXIV_SCHEMA_NS}}}{tag}")
        return clean_space(el.text if el is not None else "")

    arxiv_id = requested_id
    id_url = atom_text("id")
    if id_url:
        arxiv_id = normalize_arxiv_id(id_url)

    authors: list[str] = []
    for author in entry.findall(f"{{{ARXIV_NS}}}author"):
        name = author.find(f"{{{ARXIV_NS}}}name")
        if name is not None and name.text:
            authors.append(clean_space(name.text))

    published = atom_text("published")
    primary_el = entry.find(f"{{{ARXIV_SCHEMA_NS}}}primary_category")
    primary_category = primary_el.attrib.get("term", "") if primary_el is not None else ""
    categories = [
        cat.attrib.get("term", "") for cat in entry.findall(f"{{{ARXIV_NS}}}category") if cat.attrib.get("term")
    ]
    if primary_category and primary_category not in categories:
        categories.insert(0, primary_category)

    return ArxivRecord(
        arxiv_id=arxiv_id,
        title=atom_text("title"),
        authors=authors,
        year=int(published[:4]) if published else 0,
        abstract=atom_text("summary"),
        doi=arxiv_text("doi"),
        journal_ref=arxiv_text("journal_ref"),
        comment=arxiv_text("comment"),
        primary_category=primary_category,
        categories=categories,
    )


def fetch_batch(ids: list[str]) -> dict[str, ArxivRecord]:
    response = requests.get(
        ARXIV_API,
        params={"id_list": ",".join(ids), "max_results": len(ids)},
        headers=ARXIV_HEADERS,
        timeout=90,
    )
    response.raise_for_status()
    root = ET.fromstring(response.text)
    records: dict[str, ArxivRecord] = {}
    for entry in root.findall(f"{{{ARXIV_NS}}}entry"):
        record = parse_entry(entry, "")
        records[bare_arxiv_id(record.arxiv_id)] = record
    return records


def target_files(refresh_derived: bool = False) -> list[Path]:
    paths: list[Path] = []
    for path in sorted(PAPERS_ROOT.rglob("metadata.yml")):
        data = load_yaml(path)
        if data.get("audit_status") != "raw":
            continue
        arxiv_id = bare_arxiv_id(data.get("arxiv_id"))
        if not arxiv_id:
            continue
        if data.get("type") not in ("", "Preprint"):
            continue
        if not refresh_derived and data.get("source") and data.get("summary") and data.get("links_alt"):
            continue
        paths.append(path)
    return paths


def enrich(path: Path, record: ArxivRecord) -> bool:
    data = load_yaml(path)
    before = dump_yaml(data)

    data["title"] = title_case_ascii(record.title) if record.title else data.get("title")
    data["authors"] = record.authors or data.get("authors") or []
    data["year"] = record.year or data.get("year")
    data["source"] = data.get("source") or "arXiv"
    data["type"] = "Preprint"
    data["doi"] = data.get("doi") or record.doi or None
    data["arxiv_id"] = normalize_arxiv_id(record.arxiv_id or data.get("arxiv_id")) or None
    data["abstract"] = record.abstract or data.get("abstract") or ""
    data["summary"] = data.get("summary") or ""
    data["link"] = arxiv_pdf_url(data["arxiv_id"])

    links = list(data.get("links_alt") or [])
    for link in (
        arxiv_abs_url(data["arxiv_id"]),
        arxiv_html_url(data["arxiv_id"]),
        f"https://doi.org/{data['doi']}" if data.get("doi") else "",
    ):
        if link and link not in links and link != data["link"]:
            links.append(link)
    data["links_alt"] = links

    tags = list(data.get("tags") or [])
    for tag in build_tags(record):
        if tag not in tags:
            tags.append(tag)
    data["tags"] = tags

    if not data.get("algorithm"):
        data["algorithm"] = infer_algorithm(record) or None

    data["audit_status"] = "raw"

    after = dump_yaml(data)
    if after != before:
        path.write_text(after, encoding="utf-8")
        return True
    return False


def refresh_derived(path: Path, *, dry_run: bool = False) -> bool:
    data = load_yaml(path)
    record = ArxivRecord(
        arxiv_id=data.get("arxiv_id") or "",
        title=data.get("title") or "",
        authors=data.get("authors") or [],
        year=data.get("year") or 0,
        abstract=data.get("abstract") or "",
        doi=data.get("doi") or "",
        journal_ref="",
        comment="",
        primary_category="",
        categories=[],
    )

    algorithm = data.get("algorithm") or ""
    inferred = infer_algorithm(record)
    if (
        algorithm.lower() in GENERIC_ALGORITHMS
        or (algorithm and len(algorithm) <= 2 and not algorithm_like(algorithm))
        or not algorithm
    ):
        new_algorithm = inferred or None
    else:
        new_algorithm = algorithm or None

    if new_algorithm == (algorithm or None):
        return False

    if not dry_run:
        raw = path.read_text(encoding="utf-8")
        path.write_text(
            replace_scalar_field(raw, "algorithm", new_algorithm),
            encoding="utf-8",
        )
        return True
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, default=80)
    parser.add_argument("--delay", type=float, default=BASE_DELAY)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--refresh-derived",
        action="store_true",
        help="Refresh cautious algorithm labels from existing local metadata.",
    )
    args = parser.parse_args()

    paths = target_files(refresh_derived=args.refresh_derived)
    if args.limit:
        paths = paths[: args.limit]
    if args.refresh_derived:
        updated = 0
        for path in paths:
            if refresh_derived(path, dry_run=args.dry_run):
                updated += 1
        print(f"Done: {updated} refreshed")
        return

    by_id = {bare_arxiv_id(load_yaml(path).get("arxiv_id")): path for path in paths}
    ids = list(by_id)
    print(f"Found {len(ids)} raw arXiv-backed metadata files")

    updated = missing = failed = 0
    for start in range(0, len(ids), args.batch_size):
        chunk = ids[start : start + args.batch_size]
        print(f"Fetching {start + 1}-{start + len(chunk)} / {len(ids)}")
        try:
            records = fetch_batch(chunk)
        except Exception as exc:
            print(f"  ERROR batch fetch failed: {exc}")
            failed += len(chunk)
            time.sleep(BASE_DELAY)
            continue

        for arxiv_id in chunk:
            record = records.get(arxiv_id)
            if not record:
                print(f"  MISSING {arxiv_id}")
                missing += 1
                continue
            if args.dry_run or enrich(by_id[arxiv_id], record):
                updated += 1
        time.sleep(args.delay)

    print(f"Done: {updated} updated, {missing} missing, {failed} failed")


if __name__ == "__main__":
    main()
