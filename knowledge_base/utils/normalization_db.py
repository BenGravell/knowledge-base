"""Shared helpers for author/source/tag normalization databases."""

from __future__ import annotations

import re
import unicodedata
from collections.abc import Callable
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

import yaml

ASCII_TRANSLATION = str.maketrans(
    {
        "Æ": "AE",
        "Ð": "D",
        "Ø": "O",
        "Þ": "Th",
        "ß": "ss",
        "æ": "ae",
        "ð": "d",
        "ø": "o",
        "þ": "th",
        "Đ": "D",
        "đ": "d",
        "ı": "i",
        "Ł": "L",
        "ł": "l",
        "Œ": "OE",
        "œ": "oe",
        "Ŋ": "N",
        "ŋ": "n",
    }
)

LAST_NAME_PARTICLES = {
    "da",
    "das",
    "de",
    "del",
    "della",
    "den",
    "der",
    "di",
    "do",
    "dos",
    "du",
    "la",
    "las",
    "le",
    "les",
    "los",
    "ten",
    "ter",
    "van",
    "von",
}

AUTHOR_SUFFIX_RE = re.compile(
    r"^(?:Jr\.?|Sr\.?|I{2,3}|IV|V|VI{0,3}|IX|X|Ph\.?D\.?|M\.?D\.?|DPhil|Esq\.?)$",
    re.I,
)
INITIAL_RE = re.compile(r"^[A-Za-z]\.?$")
YEAR_RE = re.compile(r"(?<!\d)(?:18|19|20)\d{2}(?!\d)")
SOURCE_ORDINAL_PREFIX_RE = re.compile(
    r"^\s*\d+(?:st|nd|rd|th)\s+(?:annual\s+)?",
    re.I,
)
TAG_SYMBOL_WORDS = {
    "*": " star ",
    "#": " sharp ",
    "+": " plus ",
}
TAG_ACRONYM_EXPANSIONS: dict[str, str] = {
    "A2C": "Advantage actor critic",
    "AD": "Automatic differentiation",
    "ADMM": "Alternating-direction method of multipliers",
    "AI": "Artificial intelligence",
    "BC": "Behavior cloning",
    "CBF": "Control barrier function",
    "CLF": "Control Lyapunov function",
    "CMA-ES": "Covariance matrix adaptation evolution strategy",
    "CNN": "Convolutional neural network",
    "CUDA": "Compute unified device architecture",
    "CVAR": "Conditional value at risk",
    "CVaR": "Conditional value at risk",
    "DDP": "Differential dynamic programming",
    "DDPG": "Deep deterministic policy gradient",
    "DMD": "Dynamic mode decomposition",
    "ES": "Evolution strategies",
    "ESDF": "Euclidean signed distance field",
    "FDDP": "Feasibility-driven differential dynamic programming",
    "FFT": "Fast Fourier transform",
    "GAN": "Generative adversarial network",
    "GCS": "Graphs of convex sets",
    "GNN": "Graph neural network",
    "GPU": "Graphics processing unit",
    "GRASP": "Greedy randomized adaptive search procedure",
    "IL": "Imitation learning",
    "ILQR": "Iterative linear quadratic regulator",
    "IMU": "Inertial measurement unit",
    "IRL": "Inverse reinforcement learning",
    "JPEG": "Joint photographic experts group",
    "LDS": "Linear dynamical system",
    "LIC": "Line integral convolution",
    "LLM": "Large language model",
    "LQ": "Linear quadratic",
    "LQG": "Linear quadratic Gaussian",
    "LQR": "Linear quadratic regulator",
    "MARL": "Multi-agent reinforcement learning",
    "MCTS": "Monte Carlo tree search",
    "MDP": "Markov decision process",
    "MIP": "Mixed-integer programming",
    "ML": "Machine learning",
    "MOESP": "Multivariable output-error state-space",
    "MPC": "Model predictive control",
    "MPCC": "Model predictive contouring control",
    "MPPI": "Model predictive path integral control",
    "NE": "Neuroevolution",
    "NMPC": "Nonlinear model predictive control",
    "ODE": "Ordinary differential equation",
    "OLS": "Ordinary least squares",
    "OT": "Optimal transport",
    "PAC": "Probably approximately correct",
    "PCA": "Principal component analysis",
    "PDE": "Partial differential equation",
    "PG": "Policy gradient",
    "POMDP": "Partially observable Markov decision process",
    "PPO": "Proximal policy optimization",
    "QP": "Quadratic programming",
    "RL": "Reinforcement learning",
    "RNN": "Recurrent neural network",
    "RRT": "Rapidly-exploring random tree",
    "RRT#": "Rapidly-exploring random tree sharp",
    "RRT*": "Rapidly-exploring random tree star",
    "SAC": "Soft actor critic",
    "SCP": "Sequential convex programming",
    "SDP": "Semidefinite programming",
    "SGD": "Stochastic gradient descent",
    "SIMD": "Single-instruction multiple-data",
    "SLAM": "Simultaneous localization and mapping",
    "SOCP": "Second-order cone programming",
    "SQP": "Sequential quadratic programming",
    "SSIM": "Structural similarity index measure",
    "SVD": "Singular value decomposition",
    "SVM": "Support vector machine",
    "TAMP": "Task and motion planning",
    "TRPO": "Trust region policy optimization",
    "TSP": "Traveling salesman problem",
    "UAV": "Uncrewed aerial vehicle",
    "VAE": "Variational autoencoder",
    "VLA": "Vision-language-action model",
    "VLM": "Vision-language model",
    "VQA": "Visual question answering",
    "VRP": "Vehicle routing problem",
    "XAI": "Explainable artificial intelligence",
}
TAG_EXACT_EXPANSIONS: dict[str, str] = {
    "3DGS": "3D Gaussian splatting",
    "DRA-MPPI": "Distributionally robust model predictive path integral control",
    "GPS-denied navigation": "Global positioning system-denied navigation",
    "Informed RRT*": "Informed rapidly-exploring random tree star",
    "Iterative LQG": "Iterative linear quadratic Gaussian",
    "Learning-based MPC": "Learning-based model predictive control",
    "Linear quadratic Gaussian (LQG)": "Linear quadratic Gaussian",
    "LQG control": "Linear quadratic Gaussian control",
    "LQR design": "Linear quadratic regulator design",
    "LQR heuristics": "Linear quadratic regulator heuristics",
    "LQR-trees": "Linear quadratic regulator trees",
    "Metric-semantic SLAM": "Metric-semantic simultaneous localization and mapping",
    "Model-based RL": "Model-based reinforcement learning",
    "MPPI-Belief": "Model predictive path integral belief",
    "PA-MPPI": "Predictive-action model predictive path integral control",
    "Proximal DDP": "Proximal differential dynamic programming",
    "Real-world scenarios. robust MPC": "Robust model predictive control",
    "RRT-Connect": "Rapidly-exploring random tree connect",
    "Sliding-window informed RRT*": "Sliding-window informed rapidly-exploring random tree star",
    "TD-MPC": "Temporal-difference model predictive control",
    "Tube MPC": "Tube model predictive control",
    "Wasserstein GAN": "Wasserstein generative adversarial network",
}


@dataclass(frozen=True)
class ParsedAuthor:
    original: str
    ascii_name: str
    parts: tuple[str, ...]
    first: str
    middle: tuple[str, ...]
    last: str

    @property
    def first_is_initial(self) -> bool:
        return bool(INITIAL_RE.fullmatch(self.first))

    @property
    def last_is_initial(self) -> bool:
        return bool(INITIAL_RE.fullmatch(self.last))

    @property
    def first_initial(self) -> str:
        return first_alpha(self.first)[:1].casefold()

    @property
    def last_key(self) -> str:
        return compact_key(self.last)

    @property
    def initial_last_key(self) -> str:
        if not self.first_initial or not self.last_key:
            return ""
        return f"{self.first_initial}:{self.last_key}"


def ascii_fold(text: str) -> str:
    text = text.translate(ASCII_TRANSLATION)
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")


def clean_spaces(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = text.replace(r"\&", "&")
    text = re.sub(r"[\u2010-\u2015]", "-", text)
    return re.sub(r"\s+", " ", text).strip()


def ascii_clean(text: str) -> str:
    return clean_spaces(ascii_fold(text))


def compact_key(text: str) -> str:
    text = ascii_clean(text).casefold()
    text = re.sub(r"(?<=[a-z])['’](?=[a-z])", "", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def first_alpha(text: str) -> str:
    match = re.search(r"[A-Za-z]", text)
    return match.group(0) if match else ""


def _name_parts(name: str) -> list[str]:
    cleaned = ascii_clean(name)
    cleaned = cleaned.replace(",", " ")
    parts = re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)*\.?", cleaned)
    while parts and AUTHOR_SUFFIX_RE.fullmatch(parts[-1]):
        parts.pop()
    return parts


def parse_author(name: str) -> ParsedAuthor | None:
    parts = _name_parts(name)
    if not parts:
        return None

    last_start = len(parts) - 1
    while last_start > 0:
        particle = parts[last_start - 1].strip(".").casefold()
        if particle not in LAST_NAME_PARTICLES:
            break
        last_start -= 1

    return ParsedAuthor(
        original=name,
        ascii_name=ascii_clean(name),
        parts=tuple(parts),
        first=parts[0],
        middle=tuple(parts[1:last_start]),
        last=" ".join(parts[last_start:]),
    )


def author_key(name: str) -> str:
    return compact_key(name)


def _format_middle_initial(part: str) -> str | None:
    alpha = first_alpha(part)
    if not alpha:
        return None
    return f"{alpha.upper()}."


def canonical_author_display(name: str) -> str:
    parsed = parse_author(name)
    if parsed is None:
        return ascii_clean(name)

    pieces = [parsed.first]
    for middle_part in parsed.middle:
        middle = _format_middle_initial(middle_part)
        if middle:
            pieces.append(middle)
    pieces.append(parsed.last)
    return clean_spaces(" ".join(pieces))


def author_uses_first_or_last_initial(name: str) -> bool:
    parsed = parse_author(name)
    return bool(parsed and (parsed.first_is_initial or parsed.last_is_initial))


def author_initial_last_key(name: str) -> str:
    parsed = parse_author(name)
    return parsed.initial_last_key if parsed else ""


def source_key(source: str) -> str:
    source = ascii_clean(source)
    source = YEAR_RE.sub("", source)
    source = SOURCE_ORDINAL_PREFIX_RE.sub("", source)
    source = source.replace("&", " and ")
    source = re.sub(r"\b(?:proceedings|proc)\.?\b", "", source, flags=re.I)
    source = re.sub(r"\bthe\b", "", source, flags=re.I)
    source = re.sub(r"[^A-Za-z0-9]+", " ", source)
    return " ".join(source.casefold().split())


def canonical_source_display(source: str) -> str:
    source = ascii_clean(source)
    source = YEAR_RE.sub("", source)
    source = SOURCE_ORDINAL_PREFIX_RE.sub("", source)
    source = re.sub(r"\s+([,;:])", r"\1", source)
    source = re.sub(r"\s{2,}", " ", source)
    return source.strip(" ,;:-")


def _tag_acronym_pattern() -> re.Pattern[str]:
    keys = sorted(TAG_ACRONYM_EXPANSIONS, key=len, reverse=True)
    body = "|".join(re.escape(key) for key in keys)
    return re.compile(rf"(?<![A-Za-z0-9-])(?:{body})(?![A-Za-z0-9-])")


TAG_ACRONYM_RE = _tag_acronym_pattern()


def _match_case_for_tag_expansion(expansion: str, *, at_start: bool) -> str:
    if at_start:
        return expansion
    return expansion[:1].casefold() + expansion[1:]


def expand_tag_acronyms(tag: str) -> str:
    """Expand known acronym tokens in a tag into full-spelling phrases."""

    tag = clean_spaces(tag)
    if not tag:
        return tag

    exact = TAG_EXACT_EXPANSIONS.get(tag)
    if exact:
        return exact

    def replace(match: re.Match[str]) -> str:
        expansion = TAG_ACRONYM_EXPANSIONS[match.group(0)]
        prefix = tag[: match.start()]
        at_start = not re.search(r"[A-Za-z0-9]", prefix)
        return _match_case_for_tag_expansion(expansion, at_start=at_start)

    return clean_spaces(TAG_ACRONYM_RE.sub(replace, tag))


def _tag_symbol_key_text(text: str) -> str:
    for symbol, word in TAG_SYMBOL_WORDS.items():
        text = text.replace(symbol, word)
    return text


def tag_key(tag: str) -> str:
    tag = ascii_clean(tag)
    tag = _tag_symbol_key_text(tag)
    tag = tag.replace("&", " and ")
    tag = re.sub(r"(?<=[a-z])['’](?=[a-z])", "", tag)
    tag = re.sub(r"[^A-Za-z0-9]+", " ", tag)
    return " ".join(tag.casefold().split())


_TAG_NON_PLURAL_S_ENDINGS = ("ss", "us", "is", "ics")
_TAG_NON_PLURAL_S_WORDS = {
    "bias",
    "canvas",
    "chaos",
    "cosmos",
    "kinematics",
    "mathematics",
    "physics",
    "robotics",
    "semantics",
    "statistics",
}


def _tag_part_is_abbreviation_or_mixed(core: str) -> bool:
    alpha = re.sub(r"[^A-Za-z]", "", core)
    if not alpha:
        return True
    if core != alpha:
        return True
    if len(alpha) > 1 and alpha == alpha.upper():
        return True
    return len(alpha) > 1 and any(char.isupper() for char in alpha[1:])


def _singularize_tag_word(word: str) -> str:
    folded = word.casefold()
    if not folded or _tag_part_is_abbreviation_or_mixed(word):
        return folded
    if folded in _TAG_NON_PLURAL_S_WORDS:
        return folded
    if len(folded) <= 3:
        return folded
    if folded.endswith("ies") and len(folded) > 4:
        return folded[:-3] + "y"
    if folded.endswith(("sses", "ches", "shes", "xes", "zes")) and len(folded) > 4:
        return folded[:-2]
    if folded.endswith("s") and not folded.endswith(_TAG_NON_PLURAL_S_ENDINGS):
        return folded[:-1]
    return folded


def tag_dedupe_key(tag: str) -> str:
    expanded = expand_tag_acronyms(tag)
    key = tag_key(expanded)
    key = re.sub(
        r"[A-Za-z]+",
        lambda match: _singularize_tag_word(match.group(0)),
        key,
    )
    return " ".join(key.split()).casefold()


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data if isinstance(data, dict) else {}


def dump_yaml(path: Path, data: dict[str, Any], *, header: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = yaml.safe_dump(
        data,
        sort_keys=False,
        allow_unicode=False,
        width=1_000_000_000,
    )
    path.write_text(header.rstrip() + "\n\n" + raw, encoding="utf-8")


def entry_aliases(entry: dict[str, Any]) -> list[str]:
    aliases = entry.get("aliases")
    if not isinstance(aliases, list):
        return []
    return [str(alias) for alias in aliases if str(alias).strip()]


@dataclass
class NormalizationIndex:
    canonical_by_key: dict[str, str]
    entries: list[dict[str, Any]]

    def lookup(self, key: str) -> str | None:
        return self.canonical_by_key.get(key)

    def fuzzy(self, key: str, *, threshold: float = 0.92) -> str | None:
        best_score = 0.0
        best: str | None = None
        for candidate_key, canonical in self.canonical_by_key.items():
            score = SequenceMatcher(None, key, candidate_key).ratio()
            if score > best_score:
                best_score = score
                best = canonical
        return best if best_score >= threshold else None


def build_index(entries: list[dict[str, Any]], *, key_fn: Callable[[str], str]) -> NormalizationIndex:
    canonical_by_key: dict[str, str] = {}
    for entry in entries:
        canonical = str(entry.get("canonical") or "").strip()
        if not canonical:
            continue
        for value in [canonical, *entry_aliases(entry)]:
            key = key_fn(value)
            if key:
                canonical_by_key.setdefault(key, canonical)
    return NormalizationIndex(canonical_by_key=canonical_by_key, entries=entries)
