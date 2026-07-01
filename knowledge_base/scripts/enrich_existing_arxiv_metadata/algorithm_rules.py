"""Heuristics for cautious algorithm-name inference."""

from __future__ import annotations

import re

from knowledge_base.scripts.enrich_existing_arxiv_metadata.text import clean_space
from knowledge_base.utils.arxiv_utils import ArxivRecord

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
