"""Audit (and optionally fix) metadata.yml files under knowledge_base/docs/papers/."""

import argparse
import html
import json
import re
import shutil
import sys
import unicodedata
from dataclasses import dataclass
from dataclasses import field as dc_field
from enum import Enum
from functools import lru_cache
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import yaml
from rich.console import Console

from knowledge_base.config import AUDIT_STATUS_FIELD, KB_DIR, REQUIRED_FIELDS, VALID_AUDIT_STATUSES, VALID_FIELDS, VALID_TYPES
from knowledge_base.utils.normalization_db import (
    build_index,
    dump_yaml,
    expand_tag_acronyms,
    load_yaml,
    tag_key,
)
from knowledge_base.utils.paper_ids import paper_id_from_metadata

console = Console(highlight=False)
err_console = Console(stderr=True, highlight=False)

# Minor words that stay lowercase unless first/last in title (Chicago style)
_LOWERCASE_TITLE_WORDS = {
    # articles
    "a",
    "an",
    "the",
    # coordinating conjunctions
    "and",
    "but",
    "or",
    "nor",
    "for",
    "yet",
    "so",
    # prepositions
    "as",
    "at",
    "by",
    "in",
    "of",
    "on",
    "to",
    "up",
    "via",
    "per",
    "vs",
    "from",
    "into",
    "like",
    "near",
    "off",
    "onto",
    "out",
    "over",
    "plus",
    "since",
    "than",
    "about",
    "above",
    "across",
    "after",
    "against",
    "along",
    "amid",
    "amidst",
    "among",
    "amongst",
    "around",
    "before",
    "behind",
    "below",
    "beneath",
    "beside",
    "besides",
    "between",
    "beyond",
    "despite",
    "down",
    "during",
    "inside",
    "outside",
    "through",
    "throughout",
    "till",
    "under",
    "until",
    "unto",
    "upon",
    "versus",
    "within",
    "without",
    "with",
}

# arXiv ID patterns (version suffix optional)
_ARXIV_NEW_RE = re.compile(r"^\d{4}\.\d{4,5}(v\d+)?$")  # e.g. 2401.09241
_ARXIV_OLD_RE = re.compile(  # e.g. math.CO/0701001
    r"^[a-z]+(-[a-z]+)?(\.[A-Z]{2})?/\d{7}(v\d+)?$"
)
_HTML_ENTITY_RE = re.compile(
    r"&(?:#[0-9]+|#x[0-9A-Fa-f]+|[A-Za-z][A-Za-z0-9]+);"
)
_YAML_CHARACTER_ESCAPE_RE = re.compile(
    r"\\(?:x[0-9A-Fa-f]{2}|u[0-9A-Fa-f]{4}|U[0-9A-Fa-f]{8})"
)
_SOURCE_YEAR_RE = re.compile(r"(?<!\d)(?:18|19|20)\d{2}(?!\d)")
_URL_RE = re.compile(r"\b(?:https?://|ftp://|www\.)[^\s<>()]+", re.IGNORECASE)
_TITLE_HTML_TAG_RE = re.compile(r"</?\s*[A-Za-z][^>]*>")
_TITLE_MATH_SPAN_RE = re.compile(r"\$(?P<math>[^$]+)\$")
_TITLE_LATEX_COMMAND_RE = re.compile(
    r"\\(?:mathcal|mathrm|mathbf|mathit|operatorname)\{([^{}]+)\}"
)
_GARBLED_MARKUP_RE = re.compile(
    r"<\s*/?\s*(?:sub|sup|math|mml:[A-Za-z0-9_-]+)\b[^>]*>|"
    r"<[^>]*\bxmlns(?::[A-Za-z0-9_-]+)?=",
    re.I,
)
_XML_URI_TAG_RE = re.compile(
    r"<\s*(?:[A-Za-z0-9_.-]+:)?uri\b[^>]*>(?P<inner>.*?)"
    r"</\s*(?:[A-Za-z0-9_.-]+:)?uri\s*>",
    re.I | re.S,
)
_XML_HTML_TAG_RE = re.compile(
    r"</?\s*[A-Za-z][A-Za-z0-9_.:-]*\b[^>]*>",
    re.I,
)
_ABSTRACT_WORD_RE = re.compile(r"\babstract\b", re.I)
_DOLLAR_SIGN_RE = re.compile(r"\$")
_MOJIBAKE_RE = re.compile(
    r"(?:[\u00c2-\u00df][\u0080-\u00bf]|"
    r"[\u00e0-\u00ef][\u0080-\u00bf]{2}|"
    r"[\u00f0-\u00f4][\u0080-\u00bf]{3}|"
    r"Ã(?=\s|$)|Â[\u0080-\u00ff]?|â[\u0080-\uffff]{1,2}|�)"
)
_BIG_WHITESPACE_RE = re.compile(r" {3,}")
_BIG_WHITESPACE_ISSUE_PREFIX = "Contains 3+ consecutive spaces"
_AUTHOR_MOJIBAKE_ISSUE_PREFIX = "Author entries contain suspicious Unicode character"
_AUTHOR_ASCII_NORMALIZATION_ISSUE_PREFIX = "Author entries are not ASCII-normalized"
_TEXT_MOJIBAKE_ISSUE_PREFIX = "Contains likely mojibake/encoding artifact(s)"
_NON_INDIVIDUAL_AUTHOR_ISSUE_PREFIX = (
    "Author entries appear to be non-individual names"
)
_EMPTY_ABSTRACT_ISSUE_PREFIX = "Empty abstract"
_EMPTY_SUMMARY_ISSUE_PREFIX = "Missing or empty"
_LOW_SIGNAL_SUMMARY_ISSUE_PREFIX = "Low-signal generated summary"
_LOW_SIGNAL_SUMMARY_PHRASE = (
    "It is useful as a compact reference for the problem formulation, "
    "main assumptions, and evaluation setting behind the contribution."
)
CHECK_UNKNOWN = "unknown"
CHECK_REQUIRED = "required"
CHECK_TITLE = "title"
CHECK_ALGORITHM = "algorithm"
CHECK_AUTHORS = "authors"
CHECK_TAGS = "tags"
CHECK_YEAR = "year"
CHECK_ARXIV = "arxiv"
CHECK_ABSTRACT = "abstract"
CHECK_ESCAPE = "escape"
CHECK_URL = "url"
CHECK_MULTILINE = "multiline"
CHECK_SOURCE = "source"
CHECK_TYPE = "type"
CHECK_STATUS = "status"
CHECK_PATH = "path"
CHECK_SUMMARY = "summary"
CHECK_OPTIONAL = "optional"
CHECK_WHITESPACE = "whitespace"
CHECKS: tuple[str, ...] = (
    CHECK_UNKNOWN,
    CHECK_REQUIRED,
    CHECK_TITLE,
    CHECK_ALGORITHM,
    CHECK_AUTHORS,
    CHECK_TAGS,
    CHECK_YEAR,
    CHECK_ARXIV,
    CHECK_ABSTRACT,
    CHECK_ESCAPE,
    CHECK_URL,
    CHECK_MULTILINE,
    CHECK_SOURCE,
    CHECK_TYPE,
    CHECK_STATUS,
    CHECK_PATH,
    CHECK_SUMMARY,
    CHECK_OPTIONAL,
    CHECK_WHITESPACE,
)
_NEAR_EMPTY_ABSTRACT_CHAR_LIMIT = 120
_NEAR_EMPTY_ABSTRACT_WORD_LIMIT = 20
_LONG_ABSTRACT_CHAR_LIMIT = 6000
_SUMMARY_ABSTRACT_OVERLAP_MIN_RUN_WORDS = 18
_SUMMARY_ABSTRACT_OVERLAP_MIN_COVERED_WORDS = 24
_SUMMARY_ABSTRACT_OVERLAP_MIN_COVERAGE = 0.45
_SUMMARY_ABSTRACT_OVERLAP_ISSUE_PREFIX = "Substantial verbatim overlap with abstract:"
_SUMMARY_ABSTRACT_WORD_RE = re.compile(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*")
_PDF_TEXT_ARTIFACT_RE = re.compile(r"\(cid:\d+\)")
_PLACEHOLDER_ABSTRACT_RE = re.compile(
    r"^(?:n/?a|none|no abstract(?: available)?|not available|abstract unavailable|"
    r"to be added|todo|tbd|unknown)\.?$",
    re.I,
)
_SCRAPED_ABSTRACT_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "journal navigation text",
        re.compile(r"\bPrevious article\s*Next article\b", re.I),
    ),
    (
        "publisher section toolbar",
        re.compile(r"PDF\s*Bib\s*TeX?\s*Sections\b", re.I),
    ),
    (
        "publisher tool links",
        re.compile(
            r"Tools\s*Add to favorites\s*Export Citation\s*Track Citations\s*Email Sections",
            re.I,
        ),
    ),
    (
        "references/cited-by section",
        re.compile(r"References\s*Cited By\s*Details\b", re.I),
    ),
    (
        "page abstract heading",
        re.compile(r"About\s*Abstract[A-Z]", re.I),
    ),
    (
        "related/references section",
        re.compile(r"Figures\s*Related\s*References\b", re.I),
    ),
    (
        "publisher author/profile chrome",
        re.compile(r"(?:Authors Info & Claims|View Profile)\b", re.I),
    ),
    (
        "publisher metrics/citation controls",
        re.compile(
            r"(?:Publication History|Get Citation Alerts|Save to Binder|Metrics\s*Total Citations)\b",
            re.I,
        ),
    ),
    (
        "publisher access controls",
        re.compile(r"Publisher Site\s*(?:Get Access|eReaderPDF)?\b", re.I),
    ),
)
_PUBLISHER_MARK_ABSTRACT_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "copyright notice",
        re.compile(
            "(?:"
            r"\N{COPYRIGHT SIGN}\s*(?:18|19|20)\d{2}[^.]{0,120}\.?|"
            r"\bcopyright\s*(?:\N{COPYRIGHT SIGN})?\s*(?:18|19|20)\d{2}[^.]{0,120}\.?|"
            r"\(c\)\s*(?:18|19|20)\d{2}[^.]{0,120}\.?"
            ")",
            re.I,
        ),
    ),
    (
        "rights-reserved notice",
        re.compile(r"\ball\s+rights\s+reserved\.?", re.I),
    ),
)
_PUBLISHER_MARK_ABSTRACT_ISSUE_PREFIX = (
    "Contains publisher/copyright notice in the abstract:"
)
_TITLE_CHARACTER_ESCAPE_ISSUE_PREFIX = (
    "Contains escaped YAML character sequence(s) in title"
)
_URL_DISALLOWED_FIELDS = {
    "title",
    "algorithm",
    "authors",
    "year",
    "source",
    "type",
    "doi",
    "arxiv_id",
    "tags",
    "audit_status",
}
_FOLDED_TEXT_FIELDS = {
    "title",
    "abstract",
    "summary",
}
_FOLDED_TEXT_FIELD_ISSUE_PREFIX = (
    "Long text field should use folded YAML block style"
)
_FOLDED_TEXT_FIELD_MULTILINE_ISSUE_PREFIX = (
    "Folded text field should use a single YAML content line"
)
_MULTILINE_FORBIDDEN_FIELDS = {
    "algorithm",
    "year",
    "source",
    "type",
    "doi",
    "arxiv_id",
    "link",
    "audit_status",
}
_GENERIC_ALGORITHM_VALUES = {
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
    "series",
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
_ALGORITHM_DESCRIPTIVE_WORDS = {
    "analysis",
    "application",
    "applications",
    "benchmark",
    "benchmarking",
    "case",
    "comparison",
    "comparative",
    "convergence",
    "control",
    "controller",
    "extension",
    "framework",
    "improvement",
    "interpretation",
    "learning",
    "method",
    "modification",
    "optimization",
    "robust",
    "robustness",
    "sampling",
    "scheme",
    "study",
    "survey",
    "template",
    "templates",
    "theory",
    "variant",
    "variants",
}
_ALGORITHM_EXPANDED_NAMES = {
    "adam": ("adam",),
    "ddp": ("differential dynamic programming",),
    "ddpg": ("deep deterministic policy gradient",),
    "ddpm": ("denoising diffusion probabilistic models",),
    "dqn": ("deep q-network", "deep q network"),
    "ilqr": ("iterative linear quadratic regulator",),
    "mppi": (
        "model predictive path integral",
        "model predictive path integral control",
    ),
    "mpc": ("model predictive control",),
    "mpcc": ("model predictive contouring control",),
    "ppo": ("proximal policy optimization",),
    "rrt": ("rapidly-exploring random tree", "rapidly-exploring random trees"),
    "rrt*": ("rrt*", "rapidly-exploring random tree star"),
    "sac": ("soft actor-critic", "soft actor critic"),
    "td3": ("twin delayed deep deterministic policy gradient",),
}
_ALGORITHM_RELATIONAL_CUES: tuple[tuple[str, str, str], ...] = (
    (
        "preconditioned-gradient interpretation",
        r"{name}[^.\n]{0,140}\bas\s+(?:a\s+)?preconditioned\s+gradient\s+descent\b|"
        r"\bpreconditioned\s+gradient\s+descent\b[^.\n]{0,140}{name}",
        "{algorithm} preconditioned-gradient analysis",
    ),
    (
        "low-frequency sampling",
        r"\blow[-\s]+frequency\s+sampling\b[^.\n]{0,100}{name}|"
        r"{name}[^.\n]{0,100}\blow[-\s]+frequency\s+sampling\b",
        "{algorithm} low-frequency sampling",
    ),
    (
        "learning-based optimization",
        r"\blearning\s+to\s+optimi[sz]e\b[^.\n]{0,100}{name}|"
        r"{name}[^.\n]{0,100}\blearn(?:ed|ing)?\s+(?:optimizer|update|controller|control)\b",
        "{algorithm} learning-based optimization",
    ),
    (
        "transformer-based variant",
        r"\btransformer-based\b[^.\n]{0,100}{name}|"
        r"{name}[^.\n]{0,100}\btransformer-based\b",
        "Transformer-based {algorithm}",
    ),
    (
        "convergence analysis",
        r"\b(?:convergence|convergent|non[-\s]?convergence|analysis|study)\s+"
        r"(?:of|for|in|on)\s+{name}|"
        r"{name}(?:'s)?[^.\n]{0,120}\b(?:convergence|convergent|converges?|"
        r"non[-\s]?convergence|stationarity|descent guarantees?|regret bounds?)\b",
        "{algorithm} convergence analysis",
    ),
    (
        "stability analysis",
        r"\b(?:stability|stabilization|stable|stabilizing)\s+(?:of|for|in|on)\s+{name}|"
        r"{name}[^.\n]{0,120}\b(?:stability|stabilization|stable|stabilizing)\b",
        "{algorithm} stability analysis",
    ),
    (
        "robust variant or analysis",
        r"\b(?:robust|robustness|uncertain|uncertainty-aware)\b[^.\n]{0,120}{name}|"
        r"{name}[^.\n]{0,120}\b(?:robust|robustness|uncertainty|disturbance)\b",
        "Robust {algorithm}",
    ),
    (
        "existing-method discussion",
        r"\b(?:widely\s+used|classical|standard|existing|established|"
        r"recently\s+proposed)\b[^.\n]{0,120}{name}|"
        r"{name}[^.\n]{0,120}\b(?:widely\s+used|classical|standard|existing|"
        r"established|recently\s+proposed)\b",
        "{algorithm} analysis",
    ),
)
_SENTENCE_LIKE_TAG_START_RE = re.compile(
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
_SENTENCE_LIKE_TAG_CLAUSE_RE = re.compile(
    r"\b(?:argue|argues|show|shows|prove|proves|demonstrate|demonstrates|"
    r"present|presents|propose|proposes|introduce|introduces|study|studies|"
    r"investigate|investigates|claim|claims)\s+that\b",
    re.IGNORECASE,
)
_AUTHOR_SUFFIX_RE = re.compile(
    r"^(?:"
    r"Jr\.?|Sr\.?|"
    r"I{2,3}|IV|V|VI{0,3}|IX|X|"
    r"Ph\.?D\.?|M\.?D\.?|DPhil|Esq\.?"
    r")$",
    re.I,
)
_LAST_NAME_PARTICLES = {
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
_NON_INDIVIDUAL_AUTHOR_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "known organization author",
        re.compile(
            r"^(?:"
            r"OpenAI|"
            r"Google(?:\s+(?:Research|Brain|DeepMind))?|"
            r"DeepMind|"
            r"Anthropic|"
            r"Meta(?:\s+AI)?|"
            r"Facebook(?:\s+(?:AI|Research|AI\s+Research))?|"
            r"Microsoft(?:\s+Research)?|"
            r"Apple|"
            r"Amazon|"
            r"DeepSeek(?:-AI)?|"
            r"Alibaba(?:\s+(?:Cloud|Group))?|"
            r"Qwen|"
            r"Baidu|"
            r"Tencent|"
            r"NVIDIA|"
            r"IBM(?:\s+Research)?"
            r")$",
            re.I,
        ),
    ),
    ("team author", re.compile(r"\bteam\b", re.I)),
    ("collaboration author", re.compile(r"\bcollaboration\b", re.I)),
    ("consortium author", re.compile(r"\bconsortium\b", re.I)),
    ("working-group author", re.compile(r"\bworking\s+group\b", re.I)),
    ("committee author", re.compile(r"\bcommittee\b", re.I)),
    ("task-force author", re.compile(r"\btask\s+force\b", re.I)),
    ("lab/laboratory author", re.compile(r"\b(?:lab|laboratory|labs)\b", re.I)),
    ("institutional author", re.compile(r"\b(?:institute|university|department|center|centre)\b", re.I)),
    ("project/community author", re.compile(r"\b(?:project|initiative|community|contributors|developers)\b", re.I)),
    ("placeholder author", re.compile(r"^(?:anonymous|various|various authors|unknown|et\s+al\.?)$", re.I)),
)
_KNOWN_INDIVIDUAL_AUTHOR_NAMES = {
    "angela center",
}
_COMMON_MISSPELLINGS: dict[str, str] = {
    "acommodate": "accommodate",
    "accomodate": "accommodate",
    "adress": "address",
    "adresses": "addresses",
    "acheive": "achieve",
    "acheives": "achieves",
    "acheived": "achieved",
    "acheiving": "achieving",
    "alogrithm": "algorithm",
    "algoritm": "algorithm",
    "algoritms": "algorithms",
    "aproach": "approach",
    "approches": "approaches",
    "approximatly": "approximately",
    "artifical": "artificial",
    "assymetric": "asymmetric",
    "availabe": "available",
    "behaviourial": "behavioral",
    "caluculate": "calculate",
    "comparision": "comparison",
    "computional": "computational",
    "concensus": "consensus",
    "constriant": "constraint",
    "constriants": "constraints",
    "convergece": "convergence",
    "definately": "definitely",
    "dependance": "dependence",
    "descrete": "discrete",
    "developement": "development",
    "differentiatiable": "differentiable",
    "effecient": "efficient",
    "enviroment": "environment",
    "enviroments": "environments",
    "evalution": "evaluation",
    "existance": "existence",
    "experimentaly": "experimentally",
    "expermental": "experimental",
    "gaurantee": "guarantee",
    "gaurantees": "guarantees",
    "guarentee": "guarantee",
    "heirarchical": "hierarchical",
    "immediatly": "immediately",
    "implmentation": "implementation",
    "independant": "independent",
    "intergrated": "integrated",
    "intergration": "integration",
    "langauge": "language",
    "maintainance": "maintenance",
    "manuever": "maneuver",
    "manuevers": "maneuvers",
    "minmization": "minimization",
    "neccessary": "necessary",
    "occured": "occurred",
    "occuring": "occurring",
    "paramter": "parameter",
    "paramters": "parameters",
    "performace": "performance",
    "postion": "position",
    "postions": "positions",
    "preceed": "precede",
    "preceeded": "preceded",
    "preceeding": "preceding",
    "recieve": "receive",
    "recieved": "received",
    "recieves": "receives",
    "recieving": "receiving",
    "relevent": "relevant",
    "represention": "representation",
    "resistence": "resistance",
    "seperate": "separate",
    "seperated": "separated",
    "similiar": "similar",
    "stablity": "stability",
    "stocastic": "stochastic",
    "succesful": "successful",
    "sucessful": "successful",
    "teh": "the",
    "thier": "their",
    "tranjectory": "trajectory",
    "unkown": "unknown",
    "usefull": "useful",
}
_HIGH_CONFIDENCE_OCR_ARTIFACTS: tuple[tuple[str, re.Pattern[str], str], ...] = (
    ("solution", re.compile(r"\bso[-\s]*Iutio+n\b"), "solution"),
    ("conventional", re.compile(r"\bcorwen[-\s]*tional\b"), "conventional"),
    (
        "conventional",
        re.compile(r"\bcorwent\s+i\s*o\s*n\s*a\s*l\b"),
        "conventional",
    ),
    ("techniques", re.compile(r"\btechniqucs\b"), "techniques"),
    (
        "techniques",
        re.compile(r"\bt\s+e\s+c\s+h\s+n\s+i\s+q\s+u\s+e\s+s\b"),
        "techniques",
    ),
    ("particular", re.compile(r"\bpt~rticular\b"), "particular"),
)
_HIGH_CONFIDENCE_OCR_ARTIFACT_ISSUE_PREFIX = (
    "Contains high-confidence OCR artifact(s):"
)
_OCR_SPLIT_WORDS = {
    "acceleration",
    "algorithm",
    "algorithms",
    "approximation",
    "autonomous",
    "classification",
    "computational",
    "constraint",
    "constraints",
    "continuous",
    "controller",
    "controllers",
    "convergence",
    "decomposition",
    "demonstrate",
    "differential",
    "differentiable",
    "dimension",
    "dynamical",
    "environment",
    "environments",
    "estimation",
    "evaluation",
    "experiment",
    "experimental",
    "experiments",
    "function",
    "functions",
    "gradient",
    "gradients",
    "implementation",
    "information",
    "learning",
    "minimization",
    "nonconvex",
    "optimization",
    "parameter",
    "parameters",
    "performance",
    "planning",
    "probabilistic",
    "reinforcement",
    "representation",
    "robustness",
    "simulation",
    "stochastic",
    "trajectory",
    "trajectories",
    "vehicle",
    "vehicles",
}
_COMMON_SHORT_TAG_WORDS = {
    "agent",
    "agents",
    "bandit",
    "code",
    "color",
    "cost",
    "data",
    "deep",
    "edge",
    "end",
    "few",
    "filter",
    "game",
    "graph",
    "high",
    "in",
    "image",
    "lane",
    "long",
    "loop",
    "low",
    "map",
    "maps",
    "model",
    "motion",
    "of",
    "off",
    "on",
    "one",
    "open",
    "out",
    "path",
    "policy",
    "pose",
    "real",
    "risk",
    "robot",
    "robots",
    "safe",
    "safety",
    "scene",
    "search",
    "short",
    "shot",
    "state",
    "states",
    "time",
    "to",
    "tree",
    "trees",
    "value",
    "values",
    "vision",
    "zero",
}
_TAG_LEADING_ARTICLES = {"a", "an", "and", "as", "i", "in", "or", "recent", "such", "the", "we"}
_MAX_TAG_WORDS = 4
_PLURAL_DUPLICATE_TAG_MESSAGE_PREFIX = (
    "Duplicate tag value(s) after trivial plural normalization"
)
_DUPLICATE_TAG_MESSAGE_PREFIX = "Duplicate tag value(s)"
_DATABASE_DUPLICATE_TAG_MESSAGE_PREFIX = (
    "Duplicate tag value(s) after tag database normalization"
)
_TAG_DATABASE_ISSUE_PREFIX = "Tag differs from normalization database"
_TAG_DATABASE_MISSING_ISSUE_PREFIX = "Tag is missing from normalization database"
_FORBIDDEN_TAGS = {
    "state of the art": "too generic to be useful as a tag",
}
_LONG_TAG_ALLOWLIST = {
    "alternating-direction method of multipliers",
    "covariance matrix adaptation evolution strategy",
    "distributionally robust model predictive path integral control",
    "global positioning system-denied navigation",
    "graph-based simultaneous localization and mapping",
    "greedy randomized adaptive search procedure",
    "informed rapidly-exploring random tree star",
    "joint photographic experts group 2000",
    "law of the iterated logarithm",
    "metric-semantic simultaneous localization and mapping",
    "model predictive path integral belief",
    "model predictive path integral control",
    "partially observable markov decision process",
    "predictive-action model predictive path integral control",
    "sliding-window informed rapidly-exploring random tree star",
    "structural similarity index measure",
    "trust region policy optimization",
    "worst-case conditional value at risk",
}
_TAGS_DB = KB_DIR / "normalization" / "tags.yml"
_TAGS_DB_HEADER = """# Tag normalization database.
# Canonical tags should use full spelling instead of acronyms. Add observed
# variants, abbreviations, plural/singular forms, and casing variants under aliases.
# Generated by scripts/build_normalization_db.py; edit by hand as needed."""
_NON_PLURAL_S_ENDINGS = ("ss", "us", "is", "ics")
_NON_PLURAL_S_WORDS = {
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
_TAG_PROPER_NAME_WORDS = {
    "aitken": "Aitken",
    "arnoldi": "Arnoldi",
    "bayes": "Bayes",
    "bayesian": "Bayesian",
    "bellman": "Bellman",
    "broyden": "Broyden",
    "carlo": "Carlo",
    "chebyshev": "Chebyshev",
    "delaunay": "Delaunay",
    "dijkstra": "Dijkstra",
    "euclidean": "Euclidean",
    "euler": "Euler",
    "floyd": "Floyd",
    "ford": "Ford",
    "frank": "Frank",
    "franka": "Franka",
    "gauss": "Gauss",
    "gaussian": "Gaussian",
    "hamilton": "Hamilton",
    "hamiltonian": "Hamiltonian",
    "jacobi": "Jacobi",
    "kalman": "Kalman",
    "krylov": "Krylov",
    "kutta": "Kutta",
    "lagrange": "Lagrange",
    "lagrangian": "Lagrangian",
    "laplace": "Laplace",
    "levenberg": "Levenberg",
    "levy": "Levy",
    "liapunov": "Liapunov",
    "lyapunov": "Lyapunov",
    "markov": "Markov",
    "markovian": "Markovian",
    "marquardt": "Marquardt",
    "monte": "Monte",
    "newton": "Newton",
    "newtonian": "Newtonian",
    "pontryagin": "Pontryagin",
    "riccati": "Riccati",
    "runge": "Runge",
    "schur": "Schur",
    "warshall": "Warshall",
    "wolfe": "Wolfe",
}


# ---------------------------------------------------------------------------
# Author helpers
# ---------------------------------------------------------------------------


def _is_unicode_noncharacter(char: str) -> bool:
    codepoint = ord(char)
    return 0xFDD0 <= codepoint <= 0xFDEF or codepoint & 0xFFFE == 0xFFFE


def _suspicious_text_char_descriptions(text: str) -> list[str]:
    descriptions: list[str] = []
    for char in text:
        if char in "\n\r\t":
            continue
        if char == "\ufffd":
            descriptions.append("U+FFFD REPLACEMENT CHARACTER")
            continue
        if _is_unicode_noncharacter(char):
            descriptions.append(f"U+{ord(char):04X} NONCHARACTER")
            continue

        category = unicodedata.category(char)
        if category in {"Cc", "Cf", "Cs", "Co", "Cn"}:
            name = unicodedata.name(char, "UNNAMED")
            descriptions.append(f"U+{ord(char):04X} {name}")

    return descriptions


def _mojibake_examples(text: str, *, limit: int = 5) -> list[str]:
    examples: list[str] = []
    seen: set[str] = set()
    for match in _MOJIBAKE_RE.finditer(text):
        value = match.group(0)
        if value in seen:
            continue
        examples.append(value)
        seen.add(value)
        if len(examples) >= limit:
            break
    return examples


def find_weird_text_character_issues(
    path: Path,
    field: str,
    text: str,
) -> list["Issue"]:
    issues: list[Issue] = []
    char_descriptions = sorted(set(_suspicious_text_char_descriptions(text)))
    if char_descriptions:
        examples = ", ".join(char_descriptions[:5])
        if len(char_descriptions) > 5:
            examples += f", ... ({len(char_descriptions)} total)"
        issues.append(
            Issue(
                path,
                field,
                f"Contains suspicious Unicode character(s): {examples}",
                "Replace mojibake, replacement, private-use, zero-width, or control characters with clean text.",
            )
        )

    mojibake = _mojibake_examples(text)
    if mojibake:
        examples = ", ".join(repr(example) for example in mojibake)
        issues.append(
            Issue(
                path,
                field,
                f"Contains likely mojibake/encoding artifact(s): {examples}",
                "Replace with the correctly decoded source text.",
            )
        )

    return issues


def _non_individual_author_reason(author: str) -> str | None:
    stripped = " ".join(author.split()).strip(" .")
    if not stripped:
        return None
    if stripped.casefold() in _KNOWN_INDIVIDUAL_AUTHOR_NAMES:
        return None
    for reason, pattern in _NON_INDIVIDUAL_AUTHOR_PATTERNS:
        if pattern.search(stripped):
            return reason
    if not re.search(r"[A-Za-z]", stripped):
        return "non-name author token"
    if len(stripped.split()) == 1:
        return "single-token author"
    return None


def _looks_like_author_suffix(segment: str) -> bool:
    cleaned = segment.strip().strip(".")
    return bool(cleaned and _AUTHOR_SUFFIX_RE.fullmatch(cleaned))


def _looks_like_last_first_author(author: str) -> bool:
    """Detect likely "Last, First" author entries while allowing suffix commas."""
    comma_parts = [part.strip() for part in author.split(",")]
    if len(comma_parts) < 2 or not comma_parts[0]:
        return False

    for part in comma_parts[1:]:
        if not part or _looks_like_author_suffix(part):
            continue
        return bool(
            re.search(r"[A-Za-z]", comma_parts[0])
            and re.search(r"[A-Za-z]", part)
        )

    return False


def _suspicious_author_char_descriptions(author: str) -> list[str]:
    return _suspicious_text_char_descriptions(author) + [
        f"likely mojibake {example!r}" for example in _mojibake_examples(author)
    ]


def _author_ascii_normalization(author: str) -> str:
    decoded_author, _ = _decode_utf8_mojibake_text(author)
    return _fold_author_name_to_ascii(decoded_author)


def _author_ascii_normalization_issues(authors: list[object]) -> dict[int, str]:
    normalization_issues: dict[int, str] = {}
    for i, author in enumerate(authors):
        if not isinstance(author, str):
            continue
        normalized = _author_ascii_normalization(author)
        if normalized and normalized != author:
            normalization_issues[i] = normalized
    return normalization_issues


# ---------------------------------------------------------------------------
# Title-case helpers
# ---------------------------------------------------------------------------


def _cap_first(s: str) -> str:
    """Uppercase only the first character; leave the rest unchanged.

    Unlike str.capitalize(), this preserves mixed-case words like 'WestWorld'.
    """
    return s[0].upper() + s[1:] if s else s


_PROTECTED_TITLE_TOKENS = {
    "db-a*": "db-A*",
    "k-means++": "k-means++",
    "sos-convex": "sos-convex",
    "t-sne": "t-SNE",
}
_SCIENTIFIC_BINOMIALS = {
    "drosophila melanogaster",
}
_NON_BOUNDARY_PERIOD_TOKENS = {
    "e.g",
    "i.e",
    "mr",
    "mrs",
    "ms",
    "dr",
    "prof",
    "sr",
    "jr",
    "vs",
}
_PLACEHOLDER_PREFIX = "TITLEPROTECTED"


def _split_token_punctuation(token: str) -> tuple[str, str, str]:
    m = re.match(r"^([\"'“‘([{]*)(.*?)([\"'”’)\]},:;!?.]*)$", token)
    return (m.group(1), m.group(2), m.group(3)) if m else ("", token, "")


def _canonical_protected_token(core: str) -> str | None:
    return _PROTECTED_TITLE_TOKENS.get(core.casefold())


def _is_placeholder_token(core: str) -> bool:
    return bool(re.fullmatch(rf"{_PLACEHOLDER_PREFIX}\d+", core))


def _is_intentional_mixed_case(alpha: str) -> bool:
    return len(alpha) > 1 and any(c.isupper() for c in alpha[1:])


def _is_identifier_like_hyphenated_core(core: str) -> bool:
    if "-" not in core:
        return False

    parts = core.split("-")
    if len(parts) < 2:
        return False

    first = parts[0]
    if len(first) == 1 and first.islower():
        return True

    first_alpha = re.sub(r"[^a-zA-Z]", "", first)
    return bool(
        first_alpha
        and (
            first_alpha == first_alpha.upper()
            or first_alpha[0].isupper()
            or _is_intentional_mixed_case(first_alpha)
        )
    )


def _is_lowercase_leading_label(core: str, tail: str, is_first: bool) -> bool:
    """Preserve stylized one-token method names in titles like "frax: ..."."""
    return bool(
        is_first
        and tail == ":"
        and re.fullmatch(r"[a-z][a-z0-9_+.-]{1,24}", core)
        and core.casefold() not in _LOWERCASE_TITLE_WORDS
    )


def _is_scientific_binomial_epithet(previous_core: str | None, core: str) -> bool:
    """Preserve the lowercase species epithet in known binomial names."""
    if previous_core is None:
        return False

    return f"{previous_core} {core}".casefold() in _SCIENTIFIC_BINOMIALS


def _ends_title_segment(core: str, tail: str) -> bool:
    """Return whether trailing punctuation should force-cap the next word."""
    if ":" in tail or "!" in tail or "?" in tail:
        return True
    if "." not in tail:
        return False

    folded = core.casefold()
    if folded in _NON_BOUNDARY_PERIOD_TOKENS:
        return False
    return not re.fullmatch(r"[A-Za-z]", core)


def _case_token(token: str, force_cap: bool) -> str:
    """Apply title-case rules to a single word token (no hyphens)."""
    # Separate punctuation for classification, reattach after.
    lead, core, tail = _split_token_punctuation(token)

    alpha = re.sub(r"[^a-zA-Z]", "", core)
    protected = _canonical_protected_token(core)
    if protected is not None:
        return lead + protected + tail
    if _is_placeholder_token(core):
        return token
    # All-uppercase: acronym (e.g. MPPI, GPU, G1) — preserve as-is
    if alpha and alpha == alpha.upper():
        return token
    # Mixed-case: uppercase beyond the first character signals an intentional
    # capitalization pattern (e.g. pRRTC, iPhone, WestWorld) — preserve as-is
    if _is_intentional_mixed_case(alpha):
        return token

    if force_cap or core.lower() not in _LOWERCASE_TITLE_WORDS:
        return lead + _cap_first(core) + tail
    return lead + core.lower() + tail


def _normalize_title_spacing(title: str) -> str:
    title = re.sub(r"([:;!?])(?=\S)", r"\1 ", title)
    return " ".join(title.split())


def to_title_case(title: str) -> str:
    title = _normalize_title_spacing(title)
    words = title.split()
    if not words:
        return title
    result = []
    after_title_segment = False
    previous_core: str | None = None
    for i, word in enumerate(words):
        is_first = i == 0
        is_last = i == len(words) - 1
        force = is_first or is_last or after_title_segment

        lead, core, tail = _split_token_punctuation(word)
        # Track whether the next word follows a subtitle/sentence boundary.
        after_title_segment = _ends_title_segment(core, tail)
        protected = _canonical_protected_token(core)
        if protected is not None:
            result.append(lead + protected + tail)
        elif _is_scientific_binomial_epithet(previous_core, core):
            result.append(word)
        elif _is_lowercase_leading_label(core, tail, is_first):
            result.append(word)
        elif _is_identifier_like_hyphenated_core(core):
            result.append(word)
        elif "-" in core:
            # Hyphenated compound: case the first part normally; preserve
            # existing case on subsequent parts (e.g. "Sampling-based" stays
            # "Sampling-based", not "Sampling-Based").
            parts = core.split("-")
            cased_parts = [_case_token(parts[0], force)] + parts[1:]
            result.append(lead + "-".join(cased_parts) + tail)
        else:
            result.append(_case_token(word, force))
        previous_core = core

    return " ".join(result)


def is_title_case(title: str) -> bool:
    return title == to_title_case(title)


# ---------------------------------------------------------------------------
# arXiv helpers
# ---------------------------------------------------------------------------


def is_valid_arxiv_id(arxiv_id: str) -> bool:
    return bool(_ARXIV_NEW_RE.match(arxiv_id) or _ARXIV_OLD_RE.match(arxiv_id))


def strip_arxiv_version(arxiv_id: str) -> str:
    return re.sub(r"v\d+$", "", arxiv_id)


# ---------------------------------------------------------------------------
# Escaped-sequence helpers
# ---------------------------------------------------------------------------


def _html_unescape_repeated(text: str, max_rounds: int = 3) -> str:
    """Decode HTML entities, including values that were escaped more than once."""
    current = text
    for _ in range(max_rounds):
        decoded = _HTML_ENTITY_RE.sub(lambda m: html.unescape(m.group(0)), current)
        if decoded == current:
            break
        current = decoded.replace("\xa0", " ")
    return current


def _walk_string_values(value, field_name: str):
    if isinstance(value, str):
        yield field_name, value
    elif isinstance(value, list):
        for i, item in enumerate(value):
            yield from _walk_string_values(item, f"{field_name}[{i}]")
    elif isinstance(value, dict):
        for key, item in value.items():
            nested = f"{field_name}.{key}" if field_name else str(key)
            yield from _walk_string_values(item, nested)


def _big_whitespace_examples(text: str, *, limit: int = 5) -> list[str]:
    examples: list[str] = []
    seen: set[str] = set()
    for match in _BIG_WHITESPACE_RE.finditer(text):
        left = _normalize_inline_text(
            text[max(0, match.start() - 40) : match.start()]
        )
        right = _normalize_inline_text(text[match.end() : match.end() + 40])
        example = f"{left} [{len(match.group(0))} spaces] {right}".strip()
        if example in seen:
            continue
        examples.append(example)
        seen.add(example)
        if len(examples) >= limit:
            break
    return examples


def find_big_whitespace_issues(path: Path, data: dict) -> list["Issue"]:
    issues: list[Issue] = []
    for field_name, value in _walk_string_values(data, ""):
        examples = _big_whitespace_examples(value)
        if not examples:
            continue

        message = _BIG_WHITESPACE_ISSUE_PREFIX
        if examples:
            message += ": " + "; ".join(repr(example) for example in examples)
        issues.append(
            Issue(
                path,
                field_name,
                message,
                "Collapse accidental spacing to one space unless the spacing is "
                "semantically meaningful.",
            )
        )
    return issues


def find_escaped_sequence_issues(path: Path, data: dict) -> list["Issue"]:
    issues: list[Issue] = []
    for field_name, value in _walk_string_values(data, ""):
        matches = sorted(set(_HTML_ENTITY_RE.findall(value)))
        if not matches:
            continue

        examples = ", ".join(matches[:5])
        if len(matches) > 5:
            examples += f", ... ({len(matches)} total)"
        decoded_examples = ", ".join(
            f"{match} decodes to {_html_unescape_repeated(match)!r}"
            for match in matches[:3]
        )
        issues.append(
            Issue(
                path,
                field_name,
                f"Contains escaped HTML/entity sequence(s): {examples}",
                decoded_examples,
            )
        )
    return issues


# ---------------------------------------------------------------------------
# Slug helpers
# ---------------------------------------------------------------------------


def _normalize_slug_separators(text: str) -> str:
    """Preserve Unicode dash word breaks before ASCII folding removes them."""
    return "".join(
        "-" if unicodedata.category(ch) == "Pd" or ch == "\N{MINUS SIGN}" else ch
        for ch in text
    )


def _ascii_fold(text: str) -> str:
    text = _normalize_slug_separators(text)
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")


def _slugify(text: str) -> str:
    """Lowercase; replace runs of non-alphanumeric chars with single underscore."""
    s = _ascii_fold(text)
    s = _collapse_intra_word_apostrophes(s).lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")


def _title_slug_tokens(title: str) -> list[str]:
    s = _collapse_intra_word_apostrophes(_ascii_fold(title))
    raw_tokens = re.findall(r"[A-Za-z0-9]+(?:\.[A-Za-z0-9]+)*", s)
    return [slug for token in raw_tokens if (slug := _slugify(token))]


def _collapse_intra_word_apostrophes(text: str) -> str:
    """Keep names like D'Andrea or O'Neill together for author slugs."""
    return re.sub(r"(?<=[A-Za-z0-9])['’](?=[A-Za-z0-9])", "", text)


def _extract_last_name(author: str) -> str:
    """Best-effort extraction of last name from a full name string."""
    # Strip generational/title suffix after comma: "Reeds, III" -> "Reeds"
    if "," in author:
        author = author[: author.index(",")]
    parts = author.strip().split()
    if not parts:
        return author

    last_name_start = len(parts) - 1
    while last_name_start > 0:
        particle = parts[last_name_start - 1].strip(".").lower()
        if particle not in _LAST_NAME_PARTICLES:
            break
        last_name_start -= 1

    return " ".join(parts[last_name_start:])


def expected_slug(year: int, arxiv_id: str, title: str, authors: list[str]) -> str:
    if arxiv_id:
        return strip_arxiv_version(arxiv_id)
    first_author = authors[0] if authors else ""
    last_name = _slugify(
        _collapse_intra_word_apostrophes(_extract_last_name(first_author))
    )
    # First four slug-bearing words of title; punctuation separates words except
    # inside dotted terms such as C4.5.
    title_tokens = _title_slug_tokens(title)[:4]
    title_part = "_".join(title_tokens)
    return f"{year}.{last_name}.{title_part}"


# ---------------------------------------------------------------------------
# Issue dataclass
# ---------------------------------------------------------------------------


class Severity(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


_SEVERITY_RANK = {
    Severity.INFO: 0,
    Severity.WARNING: 1,
    Severity.ERROR: 2,
}


@dataclass
class Issue:
    path: Path
    field: str
    message: str
    suggestion: str | None = None
    severity: Severity = dc_field(default=Severity.ERROR)


@dataclass
class PathFix:
    old_path: Path
    new_path: Path
    old_rel: str
    new_rel: str


@dataclass(frozen=True)
class TagCanonicalFix:
    canonical: str
    aliases: tuple[str, ...] = ()


# ---------------------------------------------------------------------------
# Abstract-quality helpers
# ---------------------------------------------------------------------------


def _normalize_inline_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _abstract_word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text))


def _overlap_words(text: str) -> list[str]:
    return [
        match.group(0).casefold()
        for match in _SUMMARY_ABSTRACT_WORD_RE.finditer(text)
    ]


def _longest_common_word_run(left: list[str], right: list[str]) -> tuple[int, int]:
    previous = [0] * (len(right) + 1)
    best_len = 0
    best_left_end = 0

    for left_index, left_word in enumerate(left, 1):
        current = [0] * (len(right) + 1)
        for right_index, right_word in enumerate(right, 1):
            if left_word != right_word:
                continue
            current[right_index] = previous[right_index - 1] + 1
            if current[right_index] > best_len:
                best_len = current[right_index]
                best_left_end = left_index
        previous = current

    return best_len, best_left_end - best_len


def _shared_shingle_coverage(
    summary_words: list[str],
    abstract_words: list[str],
    *,
    size: int = 8,
) -> float:
    if len(summary_words) < size or len(abstract_words) < size:
        return 0.0

    abstract_shingles = {
        tuple(abstract_words[index : index + size])
        for index in range(len(abstract_words) - size + 1)
    }
    covered = [False] * len(summary_words)
    for index in range(len(summary_words) - size + 1):
        if tuple(summary_words[index : index + size]) in abstract_shingles:
            for covered_index in range(index, index + size):
                covered[covered_index] = True

    return sum(covered) / len(summary_words)


def find_summary_abstract_overlap_issues(
    path: Path,
    summary: str,
    abstract: str,
) -> list[Issue]:
    summary_words = _overlap_words(summary)
    abstract_words = _overlap_words(abstract)
    if not summary_words or not abstract_words:
        return []

    longest_run, run_start = _longest_common_word_run(summary_words, abstract_words)
    shingle_coverage = _shared_shingle_coverage(summary_words, abstract_words)
    covered_words = round(shingle_coverage * len(summary_words))
    run_coverage = longest_run / len(summary_words)

    has_long_run = longest_run >= _SUMMARY_ABSTRACT_OVERLAP_MIN_RUN_WORDS
    has_dominant_run = longest_run >= 12 and run_coverage >= 0.45
    has_broad_overlap = (
        covered_words >= _SUMMARY_ABSTRACT_OVERLAP_MIN_COVERED_WORDS
        and shingle_coverage >= _SUMMARY_ABSTRACT_OVERLAP_MIN_COVERAGE
    )
    if not (has_long_run or has_dominant_run or has_broad_overlap):
        return []

    snippet = " ".join(summary_words[run_start : run_start + longest_run])
    if len(snippet) > 120:
        snippet = snippet[:117] + "..."
    return [
        Issue(
            path,
            "summary",
            (
                f"{_SUMMARY_ABSTRACT_OVERLAP_ISSUE_PREFIX} "
                f"{longest_run} consecutive word(s) "
                f"({run_coverage:.0%} of summary); "
                f"{covered_words} word(s) covered by shared 8-word phrases "
                f"({shingle_coverage:.0%} of summary). Example: {snippet!r}"
            ),
            "Rewrite the summary in original observer-language instead of reusing abstract phrasing.",
        )
    ]


def find_low_signal_summary_issues(path: Path, summary: str) -> list[Issue]:
    text = _normalize_inline_text(summary)
    if _LOW_SIGNAL_SUMMARY_PHRASE not in text:
        return []

    return [
        Issue(
            path,
            "summary",
            f"{_LOW_SIGNAL_SUMMARY_ISSUE_PREFIX}: contains generic boilerplate",
            (
                "Replace with a paper-specific observer-language summary, or leave "
                "the field blank until one can be written from the source."
            ),
        )
    ]


def _format_labeled_text_hits(hits: list[tuple[str, str]]) -> str:
    examples: list[str] = []
    seen: set[tuple[str, str]] = set()
    for label, snippet in hits:
        snippet = _normalize_inline_text(snippet)
        if len(snippet) > 90:
            snippet = f"{snippet[:87]}..."
        key = (label, snippet)
        if key in seen:
            continue
        seen.add(key)
        examples.append(f"{label} ({snippet!r})")
        if len(examples) >= 4:
            break

    suffix = f", ... ({len(hits)} total)" if len(hits) > len(examples) else ""
    return ", ".join(examples) + suffix


def find_malformed_abstract_issues(
    path: Path,
    abstract: str,
    *,
    allow_short: bool = False,
) -> list[Issue]:
    issues: list[Issue] = []
    text = _normalize_inline_text(abstract)
    if not text:
        return issues

    word_count = _abstract_word_count(text)
    if _PLACEHOLDER_ABSTRACT_RE.fullmatch(text):
        issues.append(
            Issue(
                path,
                "abstract",
                f"Placeholder abstract: {text!r}",
                "Replace with the full source abstract, or leave blank only when no abstract truly exists.",
            )
        )
    elif (
        not allow_short
        and (
            len(text) < _NEAR_EMPTY_ABSTRACT_CHAR_LIMIT
            or word_count < _NEAR_EMPTY_ABSTRACT_WORD_LIMIT
        )
    ):
        issues.append(
            Issue(
                path,
                "abstract",
                f"Near-empty abstract ({len(text)} characters, {word_count} words)",
                "Replace with the full source abstract, or verify that the source abstract is genuinely this short.",
            )
        )

    scraped_hits = [
        label
        for label, pattern in _SCRAPED_ABSTRACT_PATTERNS
        if pattern.search(text)
    ]
    if scraped_hits:
        examples = ", ".join(scraped_hits[:4])
        if len(scraped_hits) > 4:
            examples += f", ... ({len(scraped_hits)} total)"
        issues.append(
            Issue(
                path,
                "abstract",
                f"Looks like scraped page text mixed into the abstract: {examples}",
                "Replace with only the source abstract; remove navigation, references, metrics, and cited-by text.",
            )
        )

    publisher_mark_hits = [
        (label, match.group(0))
        for label, pattern in _PUBLISHER_MARK_ABSTRACT_PATTERNS
        for match in pattern.finditer(text)
    ]
    if publisher_mark_hits:
        issues.append(
            Issue(
                path,
                "abstract",
                f"{_PUBLISHER_MARK_ABSTRACT_ISSUE_PREFIX} "
                f"{_format_labeled_text_hits(publisher_mark_hits)}",
                "Remove publisher notices, copyright footers, and rights-reserved text; keep only the source abstract.",
            )
        )

    if _PDF_TEXT_ARTIFACT_RE.search(text):
        issues.append(
            Issue(
                path,
                "abstract",
                "Contains PDF extraction artifacts like '(cid:173)'",
                "Replace OCR/PDF text artifacts with clean source abstract text.",
            )
        )

    abstract_word_matches = _ABSTRACT_WORD_RE.findall(text)
    if abstract_word_matches:
        count = len(abstract_word_matches)
        issues.append(
            Issue(
                path,
                "abstract",
                f"Contains the word 'abstract' {count} time(s)",
                "Verify that an 'Abstract' heading, page chrome, or commentary was not copied into the abstract field.",
                severity=Severity.WARNING,
            )
        )

    dollar_count = len(_DOLLAR_SIGN_RE.findall(text))
    if dollar_count:
        issues.append(
            Issue(
                path,
                "abstract",
                f"Contains {dollar_count} dollar sign(s), likely from inline/display math",
                "Rewrite math notation as readable plain text, for example O(n/k) instead of LaTeX dollar math.",
                severity=Severity.WARNING,
            )
        )

    if not scraped_hits and len(text) > _LONG_ABSTRACT_CHAR_LIMIT:
        issues.append(
            Issue(
                path,
                "abstract",
                f"Unusually long ({len(text)} characters); verify this is only the abstract",
                severity=Severity.WARNING,
            )
        )

    return issues


def find_likely_misspelling_issues(
    path: Path,
    field: str,
    text: str,
) -> list[Issue]:
    hits: list[tuple[str, str]] = []
    folded = text.casefold()
    for typo, correction in _COMMON_MISSPELLINGS.items():
        pattern = rf"(?<![A-Za-z]){re.escape(typo.casefold())}(?![A-Za-z])"
        if re.search(pattern, folded):
            hits.append((typo, correction))

    if not hits:
        return []

    examples = ", ".join(f"{typo!r} -> {correction!r}" for typo, correction in hits[:6])
    if len(hits) > 6:
        examples += f", ... ({len(hits)} total)"
    return [
        Issue(
            path,
            field,
            f"Contains likely misspelling(s): {examples}",
            "Review against the source text and fix only genuine typos.",
            severity=Severity.WARNING,
        )
    ]


def _apply_high_confidence_ocr_replacements(text: str) -> tuple[str, int]:
    fixed = text
    changed = 0
    for _label, pattern, replacement in _HIGH_CONFIDENCE_OCR_ARTIFACTS:
        fixed, count = pattern.subn(replacement, fixed)
        changed += count
    return fixed, changed


def find_high_confidence_ocr_artifact_issues(
    path: Path,
    field: str,
    text: str,
) -> list[Issue]:
    hits: list[tuple[str, str]] = []
    for label, pattern, _replacement in _HIGH_CONFIDENCE_OCR_ARTIFACTS:
        for match in pattern.finditer(text):
            hits.append((match.group(0), label))

    if not hits:
        return []

    examples = ", ".join(
        f"{artifact!r} -> {replacement!r}" for artifact, replacement in hits[:6]
    )
    if len(hits) > 6:
        examples += f", ... ({len(hits)} total)"
    return [
        Issue(
            path,
            field,
            f"{_HIGH_CONFIDENCE_OCR_ARTIFACT_ISSUE_PREFIX} {examples}",
            "Replace exact OCR artifacts with their clean source words.",
            severity=Severity.WARNING,
        )
    ]


def _ocr_split_examples(text: str, *, limit: int = 8) -> list[str]:
    examples: list[str] = []
    seen: set[str] = set()
    for word in sorted(_OCR_SPLIT_WORDS):
        for split_at in range(3, len(word) - 2):
            left = re.escape(word[:split_at])
            right = re.escape(word[split_at:])
            pattern = re.compile(rf"\b{left}(?:\s+|-\s*){right}\b", re.I)
            match = pattern.search(text)
            if not match:
                continue
            example = f"{match.group(0)!r} -> {word!r}"
            if example in seen:
                continue
            examples.append(example)
            seen.add(example)
            if len(examples) >= limit:
                return examples
    return examples


_LINEBREAK_HYPHEN_RE = re.compile(r"\b[A-Za-z]{3,}-\s+[A-Za-z]{3,}\b")


def find_ocr_spacing_issues(path: Path, field: str, text: str) -> list[Issue]:
    examples = _ocr_split_examples(text)
    linebreak_examples = []
    for match in _LINEBREAK_HYPHEN_RE.finditer(text):
        value = match.group(0)
        if value not in linebreak_examples:
            linebreak_examples.append(value)
        if len(linebreak_examples) >= 5:
            break

    if not examples and not linebreak_examples:
        return []

    fragments: list[str] = []
    if examples:
        fragments.append(", ".join(examples[:5]))
    if linebreak_examples:
        fragments.append(
            "line-break hyphenation: "
            + ", ".join(repr(example) for example in linebreak_examples[:5])
        )
    return [
        Issue(
            path,
            field,
            "Contains likely OCR word-splitting artifact(s): " + "; ".join(fragments),
            "Join accidentally split words and remove line-break hyphenation when the source word is not hyphenated.",
            severity=Severity.WARNING,
        )
    ]


def find_garbled_markup_issues(path: Path, data: dict) -> list[Issue]:
    issues: list[Issue] = []
    for field_name, value in _walk_string_values(data, ""):
        if not value:
            continue
        has_garbled_markup = bool(_GARBLED_MARKUP_RE.search(value))
        is_link_field = field_name == "link" or field_name.startswith("links_alt[")
        has_link_markup = is_link_field and ("<" in value or ">" in value)
        if not has_garbled_markup and not has_link_markup:
            continue

        example = _normalize_inline_text(value)
        if len(example) > 160:
            example = example[:157] + "..."
        issues.append(
            Issue(
                path,
                field_name,
                f"Contains likely garbled HTML/XML markup: {example!r}",
                "Replace with clean plain text or a plain URL.",
            )
        )
    return issues


def _strip_years_from_source(source: str) -> str:
    """Remove publication-year tokens from a venue/source name."""
    source = re.sub(r"\s+", " ", source).strip()
    source = _SOURCE_YEAR_RE.sub("", source)

    # Remove punctuation left behind by year-only parentheticals/brackets.
    source = re.sub(r"\(\s*([^)]*?)\s+\)", r"(\1)", source)
    source = re.sub(r"\[\s*([^\]]*?)\s+\]", r"[\1]", source)
    source = re.sub(r"\{\s*([^}]*?)\s+\}", r"{\1}", source)
    source = re.sub(r"\(\s*\)", "", source)
    source = re.sub(r"\[\s*\]", "", source)
    source = re.sub(r"\{\s*\}", "", source)

    # Clean common separators around the removed year.
    source = re.sub(r",\s*\.\s*", ", ", source)
    source = re.sub(r"\s+([,;:])", r"\1", source)
    source = re.sub(r"([,;:])\s*([,;:])+", r"\1", source)
    source = re.sub(r"\s*[-–—]\s*(?=,|;|:|$)", "", source)
    source = re.sub(r"(?<=^)\s*[-–—]\s*", "", source)
    source = re.sub(r"\s{2,}", " ", source)
    source = re.sub(r"\b(?:on|at|in|of)\s*$", "", source, flags=re.IGNORECASE)
    source = source.strip(" ,;:-–—")
    return source


def _looks_like_url(text: str) -> bool:
    return bool(_URL_RE.match(text))


def _find_urls(text: object) -> list[str]:
    return _URL_RE.findall(str(text))


def find_disallowed_url_issues(path: Path, data: dict) -> list["Issue"]:
    issues: list[Issue] = []
    for field_name in sorted(_URL_DISALLOWED_FIELDS):
        if field_name not in data:
            continue

        value = data.get(field_name)
        if isinstance(value, list):
            for index, item in enumerate(value):
                urls = _find_urls(item)
                if urls:
                    issues.append(
                        Issue(
                            path,
                            field_name,
                            f"URL detected in {field_name}[{index}]: {urls[0]!r}",
                        )
                    )
            continue

        urls = _find_urls(value)
        if urls:
            issues.append(
                Issue(
                    path,
                    field_name,
                    f"URL detected in {field_name}: {urls[0]!r}",
                )
            )

    return issues


def _algorithm_tokens(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9+_.*-]+", text)


def _algorithm_key(text: str) -> str:
    return re.sub(r"[^a-z0-9*]+", "", text.casefold())


def _algorithm_token_is_method_like(token: str) -> bool:
    alpha = re.sub(r"[^A-Za-z]", "", token)
    if not alpha:
        return bool(re.search(r"[0-9+_*.-]", token))
    if len(alpha) > 1 and alpha == alpha.upper():
        return True
    if len(alpha) > 1 and any(char.isupper() for char in alpha[1:]):
        return True
    if re.search(r"[0-9+_*]", token):
        return True
    return alpha[:1].isupper() and len(alpha) >= 3


def _algorithm_token_is_abbreviation_like(token: str) -> bool:
    alpha = re.sub(r"[^A-Za-z]", "", token)
    if len(alpha) > 1 and alpha == alpha.upper():
        return True
    if len(alpha) > 1 and any(char.isupper() for char in alpha[1:]):
        return True
    return bool(re.search(r"[0-9+_*]", token))


def _algorithm_label_is_bare_method_name(algorithm: str) -> bool:
    tokens = _algorithm_tokens(algorithm)
    if not tokens or len(tokens) > 3:
        return False

    folded_tokens = [token.casefold() for token in tokens]
    if len(tokens) > 1 and any(
        token in _ALGORITHM_DESCRIPTIVE_WORDS for token in folded_tokens
    ):
        return False

    if len(tokens) > 1 and not any(
        _algorithm_token_is_abbreviation_like(token) for token in tokens
    ):
        return False

    return any(_algorithm_token_is_method_like(token) for token in tokens)


def _phrase_search_pattern(phrase: str) -> str:
    escaped = re.escape(phrase)
    escaped = escaped.replace(r"\ ", r"\s+")
    return rf"(?<![A-Za-z0-9]){escaped}(?![A-Za-z0-9])"


def _algorithm_reference_names(algorithm: str) -> list[str]:
    names = [algorithm]
    names.extend(_ALGORITHM_EXPANDED_NAMES.get(_algorithm_key(algorithm), ()))

    deduped: list[str] = []
    seen: set[str] = set()
    for name in names:
        normalized = " ".join(name.split()).casefold()
        if not normalized or normalized in seen:
            continue
        deduped.append(name)
        seen.add(normalized)
    return deduped


def _text_mentions_algorithm(algorithm: str, text: str) -> bool:
    return any(
        re.search(_phrase_search_pattern(name), text, re.I)
        for name in _algorithm_reference_names(algorithm)
    )


def _text_introduces_algorithm_label(algorithm: str, title: str, text: str) -> bool:
    for name in _algorithm_reference_names(algorithm):
        name_pattern = _phrase_search_pattern(name)
        if re.search(
            rf"^\s*{name_pattern}\s*:\s*(?:a|an|the)?\s*"
            rf"(?:new|novel)?\s*(?:algorithm|method|approach|optimizer|"
            rf"planner|controller|framework|tool)\b",
            title,
            re.I,
        ):
            return True
        if re.search(rf"^\s*{name_pattern}\s*:", title, re.I):
            return True
        if re.search(
            rf"^\s*(?:introducing|introduce|propose|present|develop)\s+"
            rf"(?:(?:a|an|the|our|new|novel|simple|generalized)\s+)*"
            rf"{name_pattern}\b",
            title,
            re.I,
        ):
            return True
        if re.search(
            rf"\b(?:we|this\s+(?:paper|work|article|letter)|in\s+this\s+"
            rf"(?:paper|work|article|letter))\s+(?:first\s+)?"
            rf"(?:introduce|propose|present|develop|derive|formulate)\s+"
            rf"(?:(?:a|an|the|our|new|novel|simple|generalized)\s+)*"
            rf"{name_pattern}\b",
            text,
            re.I,
        ):
            return True
        if re.search(
            rf"\b(?:we|this\s+(?:paper|work|article|letter)|in\s+this\s+"
            rf"(?:paper|work|article|letter))\s+(?:first\s+)?"
            rf"(?:introduce|propose|present|develop|derive|formulate)\b"
            rf"[^.\n]{{0,140}}\b(?:algorithm|method|approach|optimizer|"
            rf"planner|controller|framework|tool|system)\s+(?:called\s+|named\s+)?"
            rf"{name_pattern}\b",
            text,
            re.I,
        ):
            return True
        if re.search(
            rf"\b(?:called|named|coined)\s+{name_pattern}\b",
            text,
            re.I,
        ):
            return True
    return False


def _algorithm_context_text(data: dict) -> tuple[str, str]:
    title = str(data.get("title") or "").strip()
    body = " ".join(
        str(data.get(field) or "")
        for field in ("title", "abstract", "summary")
    )
    body = _URL_RE.sub("", body)
    return title, _normalize_inline_text(body)


def _algorithm_issue_cue(
    algorithm: str,
    title: str,
    context: str,
) -> tuple[str, str] | None:
    if not _text_mentions_algorithm(algorithm, context):
        return None

    search_chunks = [title, context]
    for name in _algorithm_reference_names(algorithm):
        name_pattern = _phrase_search_pattern(name)
        for reason, pattern_template, suggestion_template in _ALGORITHM_RELATIONAL_CUES:
            pattern = re.compile(pattern_template.replace("{name}", name_pattern), re.I)
            if any(pattern.search(chunk) for chunk in search_chunks):
                return reason, suggestion_template.format(algorithm=algorithm)

    return None


def find_algorithm_issues(path: Path, data: dict) -> list["Issue"]:
    algorithm = str(data.get("algorithm") or "").strip()
    if not algorithm:
        return []

    folded = algorithm.casefold()
    if folded in _GENERIC_ALGORITHM_VALUES:
        return [
            Issue(
                path,
                "algorithm",
                f"Generic algorithm label: {algorithm!r}",
                "Leave algorithm blank unless the paper gives a specific method, system, or technique name.",
            )
        ]

    if not _algorithm_label_is_bare_method_name(algorithm):
        return []

    title, context = _algorithm_context_text(data)
    if _text_introduces_algorithm_label(algorithm, title, context):
        return []

    cue = _algorithm_issue_cue(algorithm, title, context)
    if cue is not None:
        reason, suggested_label = cue
        return [
            Issue(
                path,
                "algorithm",
                f"Bare algorithm label {algorithm!r} appears to be {reason}, not the original proposing paper",
                (
                    "Use a descriptive contribution phrase instead, for example "
                    f"{suggested_label!r}."
                ),
                severity=Severity.WARNING,
            )
        ]

    return []


def _tag_word_count(tag: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", tag))


def _sentence_like_tag_reason(tag: str) -> str | None:
    stripped = " ".join(tag.split())
    if not stripped:
        return None

    if _SENTENCE_LIKE_TAG_START_RE.search(stripped):
        return "starts like prose copied from an abstract"
    if _SENTENCE_LIKE_TAG_CLAUSE_RE.search(stripped):
        return "contains a sentence-like claim clause"
    if stripped.endswith((".", "!", "?")) and _tag_word_count(stripped) >= 4:
        return "ends like a sentence"
    if _tag_word_count(stripped) >= 7 and re.search(
        r"\b(?:that|because|while|although|where|which|who|whose|when)\b",
        stripped,
        re.IGNORECASE,
    ):
        return "looks like a long clause, not a tag"

    return None


def _normalized_tag_for_duplicate_check(tag: str) -> str:
    return " ".join(tag.split()).casefold()


def _normalized_tag_for_forbidden_check(tag: str) -> str:
    return re.sub(r"[\s-]+", " ", tag).strip().casefold()


def _forbidden_tag_reason(tag: str) -> str | None:
    return _FORBIDDEN_TAGS.get(_normalized_tag_for_forbidden_check(tag))


def _is_long_tag_allowed(tag: str) -> bool:
    return _normalized_tag_for_duplicate_check(tag) in _LONG_TAG_ALLOWLIST


@lru_cache(maxsize=1)
def _tag_normalization_index():
    try:
        data = load_yaml(_TAGS_DB)
    except FileNotFoundError:
        return None, f"Missing tag normalization database: {_TAGS_DB}"
    except yaml.YAMLError as exc:
        return None, f"Could not parse tag normalization database {_TAGS_DB}: {exc}"

    entries = data.get("tags")
    if not isinstance(entries, list):
        return None, f"Tag normalization database has no list field: {_TAGS_DB}"
    tag_entries = [entry for entry in entries if isinstance(entry, dict)]
    return build_index(tag_entries, key_fn=tag_key), None


def _tag_database_error() -> str | None:
    _, error = _tag_normalization_index()
    return error


def _tag_database_canonical(tag: str) -> str | None:
    index, error = _tag_normalization_index()
    if error is not None or index is None:
        return None

    canonical = index.lookup(tag_key(tag))
    if canonical:
        return canonical

    expanded = expand_tag_acronyms(tag)
    if expanded != tag:
        return index.lookup(tag_key(expanded))
    return None


def _is_tag_database_missing_issue(issue: Issue) -> bool:
    return (
        issue.field == "tags"
        and issue.message.startswith(_TAG_DATABASE_MISSING_ISSUE_PREFIX)
    )


def _tag_entry_aliases(entry: dict) -> list[str]:
    aliases = entry.get("aliases")
    if not isinstance(aliases, list):
        return []
    return [str(alias).strip() for alias in aliases if str(alias).strip()]


def _tag_entry_known_keys(entries: list[dict]) -> set[str]:
    keys: set[str] = set()
    for entry in entries:
        canonical = str(entry.get("canonical") or "").strip()
        values = [canonical, *_tag_entry_aliases(entry)]
        for value in values:
            key = tag_key(value)
            if key:
                keys.add(key)
    return keys


def _missing_tag_canonical_fix(
    tag: str,
    data: dict,
    existing_keys: set[str],
) -> TagCanonicalFix | None:
    observed = _normalize_inline_text(tag)
    if not observed:
        return None

    canonical = _normalize_inline_text(expand_tag_acronyms(observed))
    if not canonical:
        return None

    canonical_key = tag_key(canonical)
    if not canonical_key or canonical_key in existing_keys:
        return None

    proper_name_words = _author_last_name_tag_proper_words(data)
    if _URL_RE.search(canonical):
        return None
    if _forbidden_tag_reason(canonical):
        return None
    if _sentence_like_tag_reason(canonical):
        return None
    if _suggest_tag_without_leading_article(canonical, proper_name_words) is not None:
        return None
    if _suggest_tag_capitalization(canonical, proper_name_words) != canonical:
        return None
    if (
        _tag_word_count(canonical) > _MAX_TAG_WORDS
        and not _is_long_tag_allowed(canonical)
    ):
        return None

    aliases: tuple[str, ...] = ()
    observed_key = tag_key(observed)
    if observed != canonical and observed_key and observed_key != canonical_key:
        aliases = (observed,)

    return TagCanonicalFix(canonical=canonical, aliases=aliases)


def _merge_tag_canonical_fix(
    existing: TagCanonicalFix,
    candidate: TagCanonicalFix,
) -> TagCanonicalFix:
    aliases: list[str] = list(existing.aliases)
    seen = {tag_key(alias) for alias in aliases}
    for alias in candidate.aliases:
        key = tag_key(alias)
        if key and key not in seen:
            aliases.append(alias)
            seen.add(key)
    return TagCanonicalFix(existing.canonical, tuple(aliases))


def _collect_missing_tag_canonical_fixes(
    results: list[tuple[Path, list[Issue]]],
) -> dict[str, TagCanonicalFix]:
    try:
        data = load_yaml(_TAGS_DB)
    except (FileNotFoundError, yaml.YAMLError):
        return {}

    entries = data.get("tags")
    if not isinstance(entries, list):
        return {}

    tag_entries = [entry for entry in entries if isinstance(entry, dict)]
    existing_keys = _tag_entry_known_keys(tag_entries)
    fixes: dict[str, TagCanonicalFix] = {}

    for path, issues in results:
        missing_issues = [
            issue for issue in issues if _is_tag_database_missing_issue(issue)
        ]
        if path.name != "metadata.yml" or not missing_issues:
            continue

        try:
            metadata = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except (OSError, yaml.YAMLError):
            continue
        if not isinstance(metadata, dict):
            continue

        tags = metadata.get("tags")
        if not isinstance(tags, list):
            continue

        for issue in missing_issues:
            index = _tag_issue_index(issue)
            if index is None or index < 0 or index >= len(tags):
                continue
            tag = str(tags[index]).strip()
            candidate = _missing_tag_canonical_fix(tag, metadata, existing_keys)
            if candidate is None:
                continue

            key = tag_key(candidate.canonical)
            if key in fixes:
                fixes[key] = _merge_tag_canonical_fix(fixes[key], candidate)
            else:
                fixes[key] = candidate

    return fixes


def _write_missing_tag_canonical_fixes(
    fixes: dict[str, TagCanonicalFix],
) -> dict[str, TagCanonicalFix]:
    if not fixes:
        return {}

    data = load_yaml(_TAGS_DB)
    entries = data.get("tags")
    if not isinstance(entries, list):
        return {}

    tag_entries = [entry for entry in entries if isinstance(entry, dict)]
    existing_keys = _tag_entry_known_keys(tag_entries)
    added: dict[str, TagCanonicalFix] = {}

    for key, fix in sorted(fixes.items(), key=lambda item: tag_key(item[1].canonical)):
        canonical_key = tag_key(fix.canonical)
        if not canonical_key or canonical_key in existing_keys:
            continue

        aliases = [
            alias
            for alias in fix.aliases
            if tag_key(alias)
            and tag_key(alias) != canonical_key
            and tag_key(alias) not in existing_keys
        ]
        entry: dict[str, object] = {"canonical": fix.canonical}
        if aliases:
            entry["aliases"] = aliases
        entries.append(entry)

        existing_keys.add(canonical_key)
        existing_keys.update(tag_key(alias) for alias in aliases if tag_key(alias))
        added[key] = TagCanonicalFix(fix.canonical, tuple(aliases))

    if not added:
        return {}

    entries.sort(key=lambda entry: tag_key(str(entry.get("canonical") or "")))
    data["tags"] = entries
    dump_yaml(_TAGS_DB, data, header=_TAGS_DB_HEADER)
    _tag_normalization_index.cache_clear()
    return added


def _database_tag_duplicate_groups(tags: list[object]) -> dict[str, list[int]]:
    tag_indexes: dict[str, list[int]] = {}
    for index, tag_raw in enumerate(tags):
        tag = str(tag_raw).strip()
        if not tag:
            continue
        canonical = _tag_database_canonical(tag) or tag
        key = tag_key(canonical)
        if not key:
            continue
        tag_indexes.setdefault(key, []).append(index)

    return {
        key: indexes
        for key, indexes in tag_indexes.items()
        if len(indexes) > 1
        and len({_normalized_tag_for_duplicate_check(str(tags[index]).strip()) for index in indexes}) > 1
    }


def _preferred_database_duplicate_tag_index(tags: list[object], indexes: list[int]) -> int:
    def score(index: int) -> tuple[int, int]:
        tag = str(tags[index]).strip()
        canonical = _tag_database_canonical(tag)
        is_canonical = canonical is not None and tag == canonical
        return (0 if is_canonical else 1, index)

    return min(indexes, key=score)


def _database_duplicate_tag_removal_indexes(tags: list[object]) -> set[int]:
    remove_indexes: set[int] = set()
    for indexes in _database_tag_duplicate_groups(tags).values():
        keep_index = _preferred_database_duplicate_tag_index(tags, indexes)
        remove_indexes.update(index for index in indexes if index != keep_index)
    return remove_indexes


def _database_duplicate_tag_fix_suggestion(
    tags: list[object],
    groups: dict[str, list[int]],
) -> str:
    suggestions: list[str] = []
    for indexes in groups.values():
        keep_index = _preferred_database_duplicate_tag_index(tags, indexes)
        removals = [
            f"{str(tags[index]).strip()!r} at index {index}"
            for index in indexes
            if index != keep_index
        ]
        canonical = _tag_database_canonical(str(tags[keep_index]).strip())
        canonical_note = f" as {canonical!r}" if canonical else ""
        suggestions.append(
            f"keep {str(tags[keep_index]).strip()!r} at index {keep_index}{canonical_note}; "
            f"remove {', '.join(removals)}"
        )
    return "Resolve aliases through normalization/tags.yml: " + "; ".join(suggestions)


def _duplicate_tag_groups(tags: list[object]) -> dict[str, list[int]]:
    tag_indexes: dict[str, list[int]] = {}
    for index, tag_raw in enumerate(tags):
        normalized = _normalized_tag_for_duplicate_check(str(tag_raw).strip())
        if normalized:
            tag_indexes.setdefault(normalized, []).append(index)

    return {
        key: indexes
        for key, indexes in tag_indexes.items()
        if len(indexes) > 1
    }


def _duplicate_tag_removal_indexes(tags: list[object]) -> set[int]:
    remove_indexes: set[int] = set()
    for indexes in _duplicate_tag_groups(tags).values():
        remove_indexes.update(indexes[1:])
    return remove_indexes


def _tag_part_is_abbreviation_or_mixed(core: str) -> bool:
    alpha = re.sub(r"[^A-Za-z]", "", core)
    if not alpha:
        return True
    if core != alpha:
        return True
    if len(alpha) > 1 and alpha == alpha.upper():
        return True
    return len(alpha) > 1 and any(char.isupper() for char in alpha[1:])


def _singularize_trivial_plural_word(word: str) -> str:
    folded = word.casefold()
    if not folded or _tag_part_is_abbreviation_or_mixed(word):
        return folded
    if folded in _NON_PLURAL_S_WORDS:
        return folded
    if len(folded) <= 3:
        return folded
    if folded.endswith("ies") and len(folded) > 4:
        return folded[:-3] + "y"
    if folded.endswith(("sses", "ches", "shes", "xes", "zes")) and len(folded) > 4:
        return folded[:-2]
    if folded.endswith("s") and not folded.endswith(_NON_PLURAL_S_ENDINGS):
        return folded[:-1]
    return folded


def _plural_insensitive_tag_key(tag: str) -> str:
    key = re.sub(
        r"[A-Za-z]+",
        lambda match: _singularize_trivial_plural_word(match.group(0)),
        tag,
    )
    return " ".join(key.split()).casefold()


def _plural_duplicate_tag_groups(tags: list[object]) -> dict[str, list[int]]:
    plural_tag_indexes: dict[str, list[int]] = {}
    normalized_tag_by_index: dict[int, str] = {}

    for index, tag_raw in enumerate(tags):
        tag = str(tag_raw).strip()
        normalized_tag = _normalized_tag_for_duplicate_check(tag)
        if not normalized_tag:
            continue

        normalized_tag_by_index[index] = normalized_tag
        plural_key = _plural_insensitive_tag_key(tag)
        if plural_key:
            plural_tag_indexes.setdefault(plural_key, []).append(index)

    return {
        key: indexes
        for key, indexes in plural_tag_indexes.items()
        if len(indexes) > 1
        and len({normalized_tag_by_index[index] for index in indexes}) > 1
    }


def _preferred_plural_duplicate_tag_index(
    tags: list[object],
    plural_key: str,
    indexes: list[int],
) -> int:
    def score(index: int) -> tuple[int, int, int]:
        normalized = _normalized_tag_for_duplicate_check(str(tags[index]).strip())
        is_singular = normalized == plural_key
        return (0 if is_singular else 1, len(normalized), index)

    return min(indexes, key=score)


def _plural_duplicate_tag_removal_indexes(tags: list[object]) -> set[int]:
    remove_indexes: set[int] = set()
    for plural_key, indexes in _plural_duplicate_tag_groups(tags).items():
        keep_index = _preferred_plural_duplicate_tag_index(tags, plural_key, indexes)
        remove_indexes.update(index for index in indexes if index != keep_index)
    return remove_indexes


def _plural_duplicate_tag_fix_suggestion(
    tags: list[object],
    groups: dict[str, list[int]],
) -> str:
    suggestions: list[str] = []
    for plural_key, indexes in groups.items():
        keep_index = _preferred_plural_duplicate_tag_index(tags, plural_key, indexes)
        removals = [
            f"{str(tags[index]).strip()!r} at index {index}"
            for index in indexes
            if index != keep_index
        ]
        suggestions.append(
            f"keep {str(tags[keep_index]).strip()!r} at index {keep_index}; "
            f"remove {', '.join(removals)}"
        )

    return "Prefer singular spelling: " + "; ".join(suggestions)


def _author_last_name_tag_proper_words(data: dict) -> dict[str, str]:
    authors = data.get("authors")
    if not isinstance(authors, list):
        return {}

    proper_words: dict[str, str] = {}
    for author in authors:
        last_name = _extract_last_name(str(author).strip())
        for word in re.findall(r"[A-Za-z]+", last_name):
            if not word:
                continue
            proper_words.setdefault(word.casefold(), word[:1].upper() + word[1:])
    return proper_words


def _tag_proper_name_casing(
    core: str,
    proper_name_words: dict[str, str] | None = None,
) -> str | None:
    folded = core.casefold()
    if proper_name_words is not None and folded in proper_name_words:
        return proper_name_words[folded]
    return _TAG_PROPER_NAME_WORDS.get(folded)


def _tag_part_is_ordinary_english(
    core: str,
    proper_name_words: dict[str, str] | None = None,
) -> bool:
    if _tag_proper_name_casing(core, proper_name_words) is not None:
        return False
    if _tag_part_is_abbreviation_or_mixed(core):
        return False
    folded = core.casefold()
    return len(folded) >= 5 or folded in _COMMON_SHORT_TAG_WORDS


def _case_tag_part(
    core: str,
    *,
    seen_any_word: bool,
    proper_name_words: dict[str, str] | None = None,
) -> str:
    proper_name = _tag_proper_name_casing(core, proper_name_words)
    if proper_name is not None:
        return proper_name
    if not _tag_part_is_ordinary_english(core, proper_name_words):
        return core
    if seen_any_word:
        return core.casefold()
    return core[:1].upper() + core[1:].casefold()


def _tag_token_has_nonordinary_hyphen_part(token: str) -> bool:
    if "-" not in token:
        return False
    for part in token.split("-"):
        _, core, _ = _split_token_punctuation(part)
        if core and _tag_part_is_abbreviation_or_mixed(core):
            return True
    return False


def _suggest_tag_capitalization(
    tag: str,
    proper_name_words: dict[str, str] | None = None,
) -> str:
    tokens = tag.split()
    if not tokens:
        return tag

    cased_tokens: list[str] = []
    seen_any_word = False
    for token in tokens:
        if _tag_token_has_nonordinary_hyphen_part(token):
            lead, core, _ = _split_token_punctuation(token)
            if re.search(r"[A-Za-z]", core):
                seen_any_word = True
            cased_tokens.append(token)
            continue

        pieces = re.split(r"(-)", token)
        cased_pieces: list[str] = []
        for piece in pieces:
            if piece == "-":
                cased_pieces.append(piece)
                continue
            lead, core, tail = _split_token_punctuation(piece)
            if not core:
                cased_pieces.append(piece)
                continue

            cased_core = _case_tag_part(
                core,
                seen_any_word=seen_any_word,
                proper_name_words=proper_name_words,
            )
            if re.search(r"[A-Za-z]", core):
                seen_any_word = True
            cased_pieces.append(lead + cased_core + tail)

        cased_tokens.append("".join(cased_pieces))

    return " ".join(cased_tokens)


def _suggest_tag_without_leading_article(
    tag: str,
    proper_name_words: dict[str, str] | None = None,
) -> str | None:
    match = re.match(
        r"^(?P<article>a|an|and|as|i|in|or|recent|such|the|we)\b\s+(?P<rest>.+)$",
        tag,
        re.I,
    )
    if not match:
        return None
    article = match.group("article").casefold()
    if article not in _TAG_LEADING_ARTICLES:
        return None
    rest = match.group("rest").strip()
    return _suggest_tag_capitalization(rest, proper_name_words) if rest else None


def find_tag_issues(path: Path, data: dict) -> list["Issue"]:
    tags = data.get("tags")
    if tags in (None, ""):
        return []
    if not isinstance(tags, list):
        return [Issue(path, "tags", "Must be a list")]

    issues: list[Issue] = []
    tag_indexes: dict[str, list[int]] = {}
    tag_display: dict[str, str] = {}
    proper_name_words = _author_last_name_tag_proper_words(data)
    tag_db_error = _tag_database_error()
    if tag_db_error is not None:
        issues.append(
            Issue(
                path,
                "tags",
                tag_db_error,
                "Run `python scripts/build_normalization_db.py --only tags` from knowledge_base/.",
            )
        )
    for index, tag_raw in enumerate(tags):
        tag = str(tag_raw).strip()
        normalized_tag = _normalized_tag_for_duplicate_check(tag)
        if normalized_tag:
            tag_indexes.setdefault(normalized_tag, []).append(index)
            tag_display.setdefault(normalized_tag, tag)

        if normalized_tag and tag_db_error is None:
            canonical_tag = _tag_database_canonical(tag)
            if canonical_tag is None:
                expanded = expand_tag_acronyms(tag)
                suggestion = (
                    expanded
                    if expanded != tag
                    else f"Add {tag!r} to normalization/tags.yml as a canonical tag or alias."
                )
                issues.append(
                    Issue(
                        path,
                        "tags",
                        f"{_TAG_DATABASE_MISSING_ISSUE_PREFIX} at tags[{index}]: {tag!r}",
                        suggestion,
                    )
                )
            elif canonical_tag != tag:
                issues.append(
                    Issue(
                        path,
                        "tags",
                        f"{_TAG_DATABASE_ISSUE_PREFIX} at tags[{index}]: {tag!r}",
                        canonical_tag,
                    )
                )

        forbidden_reason = _forbidden_tag_reason(tag)
        if forbidden_reason:
            issues.append(
                Issue(
                    path,
                    "tags",
                    f"Forbidden tag at tags[{index}]: {tag!r} ({forbidden_reason})",
                    "Remove this tag.",
                )
            )
            continue

        word_count = _tag_word_count(tag)
        if word_count > _MAX_TAG_WORDS and not _is_long_tag_allowed(tag):
            issues.append(
                Issue(
                    path,
                    "tags",
                    f"Wordy tag at tags[{index}] has {word_count} words: {tag!r}",
                    f"Shorten to {_MAX_TAG_WORDS} words or fewer.",
                )
            )

        without_article = _suggest_tag_without_leading_article(tag, proper_name_words)
        if without_article is not None:
            issues.append(
                Issue(
                    path,
                    "tags",
                    f"Tag starts with an article at tags[{index}]: {tag!r}",
                    without_article,
                )
            )
        else:
            suggested_tag = _suggest_tag_capitalization(tag, proper_name_words)
            if suggested_tag != tag:
                issues.append(
                    Issue(
                        path,
                        "tags",
                        f"Tag is not in capital case at tags[{index}]: {tag!r}",
                        suggested_tag,
                    )
                )

        reason = _sentence_like_tag_reason(tag)
        if reason:
            issues.append(
                Issue(
                    path,
                    "tags",
                    f"Sentence-like debris in tags[{index}]: {tag!r} ({reason})",
                    "Replace with a short pattern-matched phrase, or remove the tag.",
                )
            )

    duplicate_tags = {
        key: indexes for key, indexes in tag_indexes.items() if len(indexes) > 1
    }
    if duplicate_tags:
        examples = ", ".join(
            f"{tag_display[key]!r} at indexes {indexes}"
            for key, indexes in list(duplicate_tags.items())[:6]
        )
        if len(duplicate_tags) > 6:
            examples += f", ... ({len(duplicate_tags)} total)"
        issues.append(
            Issue(
                path,
                "tags",
                f"Duplicate tag value(s): {examples}",
                "Remove duplicate tags or merge near-identical spellings into one canonical tag.",
            )
        )

    plural_duplicate_tags = _plural_duplicate_tag_groups(tags)
    if plural_duplicate_tags:
        examples = ", ".join(
            ", ".join(f"{str(tags[index]).strip()!r} at index {index}" for index in indexes)
            for indexes in list(plural_duplicate_tags.values())[:6]
        )
        if len(plural_duplicate_tags) > 6:
            examples += f", ... ({len(plural_duplicate_tags)} total)"
        issues.append(
            Issue(
                path,
                "tags",
                f"{_PLURAL_DUPLICATE_TAG_MESSAGE_PREFIX}: {examples}",
                _plural_duplicate_tag_fix_suggestion(tags, plural_duplicate_tags),
            )
        )

    if tag_db_error is None:
        database_duplicate_tags = _database_tag_duplicate_groups(tags)
        if database_duplicate_tags:
            examples = ", ".join(
                ", ".join(f"{str(tags[index]).strip()!r} at index {index}" for index in indexes)
                for indexes in list(database_duplicate_tags.values())[:6]
            )
            if len(database_duplicate_tags) > 6:
                examples += f", ... ({len(database_duplicate_tags)} total)"
            issues.append(
                Issue(
                    path,
                    "tags",
                    f"{_DATABASE_DUPLICATE_TAG_MESSAGE_PREFIX}: {examples}",
                    _database_duplicate_tag_fix_suggestion(tags, database_duplicate_tags),
                )
            )

    return issues


_TOP_LEVEL_SCALAR_FIELD_RE = re.compile(
    r"^(?P<key>[A-Za-z_][A-Za-z0-9_]*)\s*:\s*(?P<value>.*?)(?P<newline>\r?\n?)$"
)


def _top_level_field_span(lines: list[str], start: int) -> tuple[str, str, int] | None:
    match = _TOP_LEVEL_SCALAR_FIELD_RE.match(lines[start])
    if not match:
        return None

    field_name = match.group("key")
    value = match.group("value")
    end = start + 1
    if (
        _is_block_scalar_header(value)
        or _is_multiline_quoted_scalar_header(value)
        or _has_indented_continuation(lines, start)
    ):
        while end < len(lines):
            next_line = lines[end]
            if next_line.strip() and not next_line.startswith((" ", "\t")):
                break
            end += 1

    return field_name, value, end


def _is_folded_scalar_header(value: str) -> bool:
    return value.lstrip().startswith(">")


def _nonblank_content_line_count(lines: list[str], start: int, end: int) -> int:
    return sum(1 for line in lines[start + 1 : end] if line.strip())


def find_multiline_field_issues(path: Path, raw: str, data: dict) -> list["Issue"]:
    issues: list[Issue] = []
    lines = raw.splitlines(keepends=True)
    for index, line in enumerate(lines):
        parsed = _top_level_field_span(lines, index)
        if parsed is None:
            continue

        field_name, value, end = parsed
        if field_name in _FOLDED_TEXT_FIELDS:
            field_value = data.get(field_name)
            if (
                isinstance(field_value, str)
                and field_value.strip()
                and not _is_folded_scalar_header(value)
            ):
                issues.append(
                    Issue(
                        path,
                        field_name,
                        f"{_FOLDED_TEXT_FIELD_ISSUE_PREFIX}: {field_name}",
                        "Use the `field: >` newline pattern with indented text.",
                    )
                )
            elif (
                isinstance(field_value, str)
                and field_value.strip()
                and _is_folded_scalar_header(value)
            ):
                content_line_count = _nonblank_content_line_count(lines, index, end)
                if content_line_count > 1:
                    issues.append(
                        Issue(
                            path,
                            field_name,
                            (
                                f"{_FOLDED_TEXT_FIELD_MULTILINE_ISSUE_PREFIX}: "
                                f"{field_name} spans {content_line_count} YAML "
                                "content line(s)"
                            ),
                            f"Collapse the text to one indented line under `{field_name}: >`.",
                        )
                    )
            continue

        if field_name not in _MULTILINE_FORBIDDEN_FIELDS:
            continue

        if end > index + 1 or _is_block_scalar_header(value):
            issues.append(
                Issue(
                    path,
                    field_name,
                    f"Field must be a single-line scalar but spans {end - index} YAML line(s)",
                )
            )

    return issues


def _top_level_field_raw(raw: str, target_field: str) -> str | None:
    lines = raw.splitlines(keepends=True)
    index = 0
    while index < len(lines):
        parsed = _top_level_field_span(lines, index)
        if parsed is None:
            index += 1
            continue

        field_name, _, end = parsed
        if field_name == target_field:
            return "".join(lines[index:end])
        index = end

    return None


def _decode_yaml_character_escape(sequence: str) -> str | None:
    prefix = sequence[1]
    digits = sequence[2:]
    if prefix not in {"x", "u", "U"}:
        return None

    try:
        codepoint = int(digits, 16)
        return chr(codepoint)
    except ValueError:
        return None


def find_title_character_escape_issues(
    path: Path,
    raw: str,
    fixed_title: str,
) -> list["Issue"]:
    title_raw = _top_level_field_raw(raw, "title")
    if title_raw is None:
        return []

    matches = sorted(set(_YAML_CHARACTER_ESCAPE_RE.findall(title_raw)))
    if not matches:
        return []

    examples = ", ".join(matches[:5])
    if len(matches) > 5:
        examples += f", ... ({len(matches)} total)"

    decoded = []
    for match in matches[:3]:
        decoded_char = _decode_yaml_character_escape(match)
        if decoded_char is None:
            decoded.append(f"{match} is not a valid Unicode scalar value")
        else:
            decoded.append(f"{match} decodes to {decoded_char!r}")
    decoded_note = f" ({'; '.join(decoded)})" if decoded else ""

    return [
        Issue(
            path,
            "title",
            f"{_TITLE_CHARACTER_ESCAPE_ISSUE_PREFIX}: {examples}{decoded_note}",
            fixed_title,
        )
    ]


# ---------------------------------------------------------------------------
# Per-file audit
# ---------------------------------------------------------------------------


def audit_file(
    path: Path,
    *,
    selected_checks: set[str] | None = None,
) -> tuple[dict, list[Issue]]:
    issues: list[Issue] = []

    def should_check(check: str) -> bool:
        return selected_checks is None or check in selected_checks

    try:
        raw = path.read_text(encoding="utf-8")
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        issues.append(Issue(path, "parse", f"YAML parse error: {exc}"))
        return {}, issues

    if not isinstance(data, dict):
        issues.append(Issue(path, "parse", "Root YAML value is not a mapping"))
        return {}, issues

    if should_check(CHECK_ESCAPE):
        issues.extend(find_escaped_sequence_issues(path, data))

    if should_check(CHECK_URL):
        issues.extend(find_disallowed_url_issues(path, data))
        issues.extend(find_garbled_markup_issues(path, data))

    if should_check(CHECK_MULTILINE):
        issues.extend(find_multiline_field_issues(path, raw, data))

    if should_check(CHECK_WHITESPACE):
        issues.extend(find_big_whitespace_issues(path, data))

    # -- unknown fields --
    if should_check(CHECK_UNKNOWN):
        _valid_set = set(VALID_FIELDS)
        for key in data:
            if key not in _valid_set:
                issues.append(Issue(path, key, f"Unknown field {key!r}"))

    # -- required fields presence --
    missing = {f for f in REQUIRED_FIELDS if data.get(f) is None}
    if should_check(CHECK_REQUIRED):
        for f in sorted(missing):
            issues.append(Issue(path, f, "Missing required field"))

    # -- title --
    title_raw = data.get("title")
    title = str(title_raw).strip() if title_raw not in (None, "") else ""
    title_corrected = title
    if title and should_check(CHECK_TITLE):
        title_corrected = _suggest_title_fix(raw, title)
    if title and (should_check(CHECK_TITLE) or should_check(CHECK_ESCAPE)):
        issues.extend(find_title_character_escape_issues(path, raw, title_corrected))
    if should_check(CHECK_TITLE) and "title" not in missing:
        if not title:
            issues.append(Issue(path, "title", "Empty"))
        else:
            issues.extend(find_weird_text_character_issues(path, "title", title))
            issues.extend(find_likely_misspelling_issues(path, "title", title))
            issues.extend(
                find_high_confidence_ocr_artifact_issues(path, "title", title)
            )
            if title != title_corrected:
                message = (
                    f"Contains title markup/math garbage: {title!r}"
                    if _title_has_garbage(title)
                    else f"Not in title case: {title!r}"
                )
                issues.append(
                    Issue(
                        path,
                        "title",
                        message,
                        title_corrected,
                    )
                )

    # -- algorithm --
    if should_check(CHECK_ALGORITHM):
        issues.extend(find_algorithm_issues(path, data))

    # -- authors --
    authors = data.get("authors")
    if should_check(CHECK_AUTHORS) and "authors" not in missing:
        if not isinstance(authors, list):
            issues.append(Issue(path, "authors", "Must be a list"))
            authors = []
        elif len(authors) == 0:
            issues.append(
                Issue(path, "authors", "List is empty -- at least one entry required")
            )
        else:
            blank = [i for i, a in enumerate(authors) if not str(a).strip()]
            if blank:
                issues.append(
                    Issue(path, "authors", f"Blank entries at index(es): {blank}")
                )
            last_first = [
                i
                for i, a in enumerate(authors)
                if _looks_like_last_first_author(str(a))
            ]
            if last_first:
                examples = ", ".join(repr(str(authors[i])) for i in last_first[:3])
                if len(last_first) > 3:
                    examples += f", ... ({len(last_first)} total)"
                issues.append(
                    Issue(
                        path,
                        "authors",
                        "Author entries appear to use 'Last, First' order at index(es): "
                        f"{last_first}",
                        f"Use first-name last-name order; review: {examples}",
                    )
                )
            non_individual = {
                i: _non_individual_author_reason(str(a))
                for i, a in enumerate(authors)
            }
            non_individual = {
                i: reason for i, reason in non_individual.items() if reason is not None
            }
            if non_individual:
                examples = ", ".join(
                    f"{i}: {repr(str(authors[i]))} ({reason})"
                    for i, reason in list(non_individual.items())[:4]
                )
                if len(non_individual) > 4:
                    examples += f", ... ({len(non_individual)} total)"
                issues.append(
                    Issue(
                        path,
                        "authors",
                        "Author entries appear to be non-individual names at index(es): "
                        f"{list(non_individual)}",
                        f"Replace organizations, team/institution placeholders, and one-token names with individual human authors where available; review: {examples}",
                    )
                )
            suspicious_chars = {}
            for i, a in enumerate(authors):
                char_descriptions = _suspicious_author_char_descriptions(str(a))
                if char_descriptions:
                    suspicious_chars[i] = sorted(set(char_descriptions))
            if suspicious_chars:
                examples = ", ".join(
                    f"{i}: {repr(str(authors[i]))} ({', '.join(chars[:3])})"
                    for i, chars in list(suspicious_chars.items())[:3]
                )
                if len(suspicious_chars) > 3:
                    examples += f", ... ({len(suspicious_chars)} total)"
                issues.append(
                    Issue(
                        path,
                        "authors",
                        "Author entries contain suspicious Unicode character(s) at index(es): "
                        f"{list(suspicious_chars)}",
                        f"Replace mojibake/control characters with clean author names; review: {examples}",
                    )
                )
            ascii_normalization = _author_ascii_normalization_issues(authors)
            if ascii_normalization:
                examples = ", ".join(
                    f"{i}: {repr(str(authors[i]))} -> {normalized!r}"
                    for i, normalized in list(ascii_normalization.items())[:4]
                )
                if len(ascii_normalization) > 4:
                    examples += f", ... ({len(ascii_normalization)} total)"
                issues.append(
                    Issue(
                        path,
                        "authors",
                        "Author entries are not ASCII-normalized at index(es): "
                        f"{list(ascii_normalization)}",
                        (
                            "Normalize author names to the native 26 English "
                            f"letters for centralized author matching; review: {examples}"
                        ),
                    )
                )
    else:
        authors = authors if isinstance(authors, list) else []

    # -- tags --
    if should_check(CHECK_TAGS):
        issues.extend(find_tag_issues(path, data))

    # -- year --
    if should_check(CHECK_YEAR) and "year" not in missing:
        meta_year_raw = data.get("year")
        if not isinstance(meta_year_raw, int) or not (1000 <= meta_year_raw <= 9999):
            issues.append(Issue(path, "year", f"Must be a 4-digit integer; got {meta_year_raw!r}"))

    # -- arxiv_id --
    arxiv_raw = data.get("arxiv_id")
    arxiv_id = str(arxiv_raw).strip() if arxiv_raw not in (None, "") else ""
    if should_check(CHECK_ARXIV) and arxiv_id and not is_valid_arxiv_id(arxiv_id):
        issues.append(Issue(path, "arxiv_id", f"Invalid arXiv ID format: {arxiv_id!r}"))

    # -- source --
    if should_check(CHECK_SOURCE):
        source_raw = data.get("source")
        source = str(source_raw).strip() if source_raw not in (None, "") else ""
        if source and not _looks_like_url(source):
            source_without_years = _strip_years_from_source(source)
            if source_without_years != source:
                issues.append(
                    Issue(
                        path,
                        "source",
                        f"Contains year in source field: {source!r}",
                        source_without_years,
                    )
                )

    # -- abstract --
    if should_check(CHECK_ABSTRACT) and "abstract" not in missing:
        abstract = data.get("abstract")
        abstract_str = str(abstract)
        if not abstract_str.strip():
            issues.append(
                Issue(
                    path,
                    "abstract",
                    _EMPTY_ABSTRACT_ISSUE_PREFIX,
                    "Fill from the source when an abstract exists; leave blank only after verifying the source has no abstract.",
                    severity=Severity.WARNING,
                )
            )
        else:
            issues.extend(find_weird_text_character_issues(path, "abstract", abstract_str))
            issues.extend(find_likely_misspelling_issues(path, "abstract", abstract_str))
            issues.extend(
                find_high_confidence_ocr_artifact_issues(
                    path,
                    "abstract",
                    abstract_str,
                )
            )
            issues.extend(find_ocr_spacing_issues(path, "abstract", abstract_str))
            audit_status = str(data.get(AUDIT_STATUS_FIELD) or "").strip()
            issues.extend(
                find_malformed_abstract_issues(
                    path,
                    abstract_str,
                    allow_short=audit_status == "reviewed",
                )
            )

    # -- type --
    if should_check(CHECK_TYPE) and "type" not in missing:
        paper_type = data.get("type")
        type_str = str(paper_type).strip() if paper_type not in (None, "") else ""
        if type_str not in VALID_TYPES:
            type_suggestion = None
            link = str(data.get("link") or "")
            if not type_str and (arxiv_id or "arxiv.org" in link.casefold()):
                type_suggestion = "Preprint"
            issues.append(
                Issue(
                    path,
                    "type",
                    f"Invalid value {type_str!r}; must be one of: {sorted(VALID_TYPES)}",
                    type_suggestion,
                )
            )

    # -- audit_status --
    if should_check(CHECK_STATUS) and "audit_status" not in missing:
        audit_status = data.get(AUDIT_STATUS_FIELD)
        status_str = str(audit_status).strip() if audit_status not in (None, "") else ""
        if status_str not in VALID_AUDIT_STATUSES:
            issues.append(
                Issue(
                    path,
                    AUDIT_STATUS_FIELD,
                    f"Invalid value {status_str!r}; must be one of: {VALID_AUDIT_STATUSES}",
                )
            )

    # -- path structure --
    if should_check(CHECK_PATH):
        parts = path.parts
        try:
            papers_idx = next(i for i, p in enumerate(parts) if p == "papers")
            path_year_str = parts[papers_idx + 1]
            path_slug = "/".join(parts[papers_idx + 2 : -1])
        except (StopIteration, IndexError):
            issues.append(Issue(path, "path", "Cannot locate papers/YEAR/SLUG in path"))
            return data, issues

        if not path_slug:
            issues.append(Issue(path, "path", "Cannot locate papers/YEAR/SLUG in path"))
            return data, issues

        if not re.match(r"^\d{4}$", path_year_str):
            issues.append(
                Issue(path, "path", f"YEAR component {path_year_str!r} is not 4 digits")
            )
            return data, issues

        path_year = int(path_year_str)

        # Year in metadata should match path year
        meta_year = data.get("year")
        try:
            meta_year_int = int(meta_year) if meta_year is not None else None
        except (TypeError, ValueError):
            meta_year_int = None
        if meta_year_int is not None and meta_year_int != path_year:
            issues.append(
                Issue(
                    path,
                    "path",
                    f"Metadata year {meta_year!r} does not match path year {path_year}",
                )
            )

        # Slug check (only when we have enough data)
        author_strs = [str(a) for a in (authors or [])]
        if author_strs and title:
            exp = expected_slug(path_year, arxiv_id, title, author_strs)
            if path_slug != exp:
                issues.append(
                    Issue(
                        path,
                        "path",
                        f"Slug {path_slug!r} does not match expected {exp!r}",
                        exp,
                    )
                )

    # -- summary --
    if should_check(CHECK_SUMMARY):
        summary = data.get("summary")
        if not summary or not str(summary).strip():
            issues.append(
                Issue(
                    path,
                    "summary",
                    _EMPTY_SUMMARY_ISSUE_PREFIX,
                    severity=Severity.WARNING,
                )
            )
        else:
            issues.extend(find_low_signal_summary_issues(path, str(summary)))
            issues.extend(
                find_likely_misspelling_issues(path, "summary", str(summary))
            )
            issues.extend(
                find_high_confidence_ocr_artifact_issues(
                    path,
                    "summary",
                    str(summary),
                )
            )
            if "abstract" not in missing:
                issues.extend(
                    find_summary_abstract_overlap_issues(
                        path,
                        str(summary),
                        str(data.get("abstract") or ""),
                    )
                )

    # -- optional field completeness (info) --
    if should_check(CHECK_OPTIONAL):
        audit_status_val = str(data.get(AUDIT_STATUS_FIELD) or "").strip()
        if audit_status_val == "raw":
            issues.append(Issue(path, AUDIT_STATUS_FIELD, "raw; skipping optional field checks", severity=Severity.INFO))
        else:
            for f in VALID_FIELDS:
                if f in REQUIRED_FIELDS or f == "summary":
                    continue  # already covered by required-check or summary-warning above
                val = data.get(f)
                is_empty = val is None or (isinstance(val, (str, list)) and not val)
                if is_empty:
                    if f == "arxiv_id":
                        link = str(data.get("link") or "").strip()
                        if link and "arxiv.org" not in link:
                            continue
                    issues.append(Issue(path, f, "Not populated", severity=Severity.INFO))

    return data, issues


# ---------------------------------------------------------------------------
# Global path audit
# ---------------------------------------------------------------------------


_MAP_DATA_DECL_RE = re.compile(r"^\s*const\s+mapData\s*=\s*(?P<json>.*?);\s*$", re.S)


def _format_id_examples(ids: set[str] | list[str], limit: int = 8) -> str:
    ordered = sorted(ids)
    examples = ", ".join(ordered[:limit])
    if len(ordered) > limit:
        examples += f", ... ({len(ordered)} total)"
    return examples


def _load_json_file(path: Path) -> tuple[object | None, str | None]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except FileNotFoundError:
        return None, "Missing file"
    except json.JSONDecodeError as exc:
        return None, f"JSON parse error: {exc}"
    except OSError as exc:
        return None, f"Could not read file: {exc}"


def _load_map_data_js(path: Path) -> tuple[dict | None, str | None]:
    try:
        raw = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None, "Missing file"
    except OSError as exc:
        return None, f"Could not read file: {exc}"

    match = _MAP_DATA_DECL_RE.match(raw)
    if not match:
        return None, "Expected JavaScript assignment like 'const mapData={...};'"

    try:
        data = json.loads(match.group("json"))
    except json.JSONDecodeError as exc:
        return None, f"mapData JSON parse error: {exc}"
    if not isinstance(data, dict):
        return None, "mapData root is not an object"
    return data, None


def _canonical_metadata_ids(targets: list[Path], kb_root: Path) -> tuple[dict[str, Path], list[Issue]]:
    metadata_root = kb_root / "docs" / "papers"
    expected: dict[str, Path] = {}
    issues: list[Issue] = []
    collisions: dict[str, list[Path]] = {}

    for path in targets:
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        if not isinstance(data, dict):
            continue

        paper_id = paper_id_from_metadata(path, data, metadata_root)
        if paper_id in expected:
            collisions.setdefault(paper_id, [expected[paper_id]]).append(path)
        else:
            expected[paper_id] = path

    for paper_id, paths in sorted(collisions.items()):
        path_list = ", ".join(str(path) for path in paths)
        issues.append(
            Issue(
                kb_root / "map" / "map-data.js",
                CHECK_PATH,
                f"Canonical metadata ID {paper_id!r} is produced by multiple metadata files: {path_list}",
            )
        )

    return expected, issues


def _audit_id_set(
    *,
    path: Path,
    label: str,
    actual_ids: set[str],
    expected_ids: set[str],
    report_stale: bool,
) -> list[Issue]:
    issues: list[Issue] = []
    missing = expected_ids - actual_ids
    if missing:
        issues.append(
            Issue(
                path,
                CHECK_PATH,
                f"{label} missing {len(missing)} metadata-backed paper ID(s): {_format_id_examples(missing)}",
                "Regenerate map data, or run --fix after a metadata path change.",
            )
        )

    stale = actual_ids - expected_ids
    if report_stale and stale:
        issues.append(
            Issue(
                path,
                CHECK_PATH,
                f"{label} contains {len(stale)} stale paper ID(s) with no metadata.yml: {_format_id_examples(stale)}",
                "Regenerate map data, or run --fix after a metadata path change.",
            )
        )
    return issues


def _duplicate_values(values: list[str]) -> set[str]:
    seen: set[str] = set()
    dupes: set[str] = set()
    for value in values:
        if value in seen:
            dupes.add(value)
        seen.add(value)
    return dupes


def audit_map_data_paths(
    targets: list[Path],
    *,
    kb_root: Path,
    report_stale: bool,
) -> list[tuple[Path, list[Issue]]]:
    expected_by_id, setup_issues = _canonical_metadata_ids(targets, kb_root)
    expected_ids = set(expected_by_id)
    grouped: dict[Path, list[Issue]] = {}
    for issue in setup_issues:
        grouped.setdefault(issue.path, []).append(issue)

    map_data_path = kb_root / "map" / "map-data.js"
    map_data, error = _load_map_data_js(map_data_path)
    if error:
        grouped.setdefault(map_data_path, []).append(Issue(map_data_path, CHECK_PATH, error))
    elif map_data is not None:
        nodes = map_data.get("nodes")
        if not isinstance(nodes, list):
            grouped.setdefault(map_data_path, []).append(
                Issue(map_data_path, CHECK_PATH, "mapData.nodes is not a list")
            )
            node_ids: list[str] = []
        else:
            node_ids = []
            bad_nodes = 0
            for node in nodes:
                data = node.get("data") if isinstance(node, dict) else None
                node_id = data.get("id") if isinstance(data, dict) else None
                if isinstance(node_id, str) and node_id:
                    node_ids.append(node_id)
                else:
                    bad_nodes += 1
            if bad_nodes:
                grouped.setdefault(map_data_path, []).append(
                    Issue(map_data_path, CHECK_PATH, f"mapData.nodes has {bad_nodes} node(s) without data.id")
                )

        duplicate_node_ids = _duplicate_values(node_ids)
        if duplicate_node_ids:
            grouped.setdefault(map_data_path, []).append(
                Issue(
                    map_data_path,
                    CHECK_PATH,
                    f"mapData.nodes has duplicate paper ID(s): {_format_id_examples(duplicate_node_ids)}",
                )
            )

        grouped.setdefault(map_data_path, []).extend(
            _audit_id_set(
                path=map_data_path,
                label="mapData.nodes",
                actual_ids=set(node_ids),
                expected_ids=expected_ids,
                report_stale=report_stale,
            )
        )

        similarity = map_data.get("similarity")
        if not isinstance(similarity, dict):
            grouped.setdefault(map_data_path, []).append(
                Issue(map_data_path, CHECK_PATH, "mapData.similarity is not an object")
            )
        else:
            similarity_ids_raw = similarity.get("ids")
            if not isinstance(similarity_ids_raw, list) or not all(isinstance(item, str) for item in similarity_ids_raw):
                grouped.setdefault(map_data_path, []).append(
                    Issue(map_data_path, CHECK_PATH, "mapData.similarity.ids is not a string list")
                )
                similarity_ids: list[str] = []
            else:
                similarity_ids = similarity_ids_raw
                grouped.setdefault(map_data_path, []).extend(
                    _audit_id_set(
                        path=map_data_path,
                        label="mapData.similarity.ids",
                        actual_ids=set(similarity_ids),
                        expected_ids=expected_ids,
                        report_stale=report_stale,
                    )
                )
                if node_ids and similarity_ids != node_ids:
                    grouped.setdefault(map_data_path, []).append(
                        Issue(
                            map_data_path,
                            CHECK_PATH,
                            "mapData.similarity.ids does not exactly match mapData.nodes order",
                            "Regenerate map data.",
                        )
                    )

            rows = similarity.get("rows")
            if isinstance(rows, list) and similarity_ids:
                bad_row_count = len(rows) != len(similarity_ids)
                bad_row_width = any(not isinstance(row, list) or len(row) != len(similarity_ids) for row in rows)
                if bad_row_count or bad_row_width:
                    grouped.setdefault(map_data_path, []).append(
                        Issue(
                            map_data_path,
                            CHECK_PATH,
                            "mapData.similarity.rows shape does not match similarity.ids",
                            "Regenerate map data.",
                        )
                    )

        meta = map_data.get("meta")
        if report_stale and isinstance(meta, dict) and meta.get("total_papers") != len(expected_ids):
            grouped.setdefault(map_data_path, []).append(
                Issue(
                    map_data_path,
                    CHECK_PATH,
                    f"mapData.meta.total_papers is {meta.get('total_papers')!r}; expected {len(expected_ids)}",
                    "Regenerate map data.",
                )
            )

    cache_path = kb_root / "map" / "embedding_cache.json"
    cache, error = _load_json_file(cache_path)
    if error:
        grouped.setdefault(cache_path, []).append(Issue(cache_path, CHECK_PATH, error))
    elif isinstance(cache, dict):
        cached_papers = cache.get("papers")
        if not isinstance(cached_papers, dict):
            grouped.setdefault(cache_path, []).append(
                Issue(cache_path, CHECK_PATH, "embedding_cache.json papers field is not an object")
            )
        else:
            grouped.setdefault(cache_path, []).extend(
                _audit_id_set(
                    path=cache_path,
                    label="embedding_cache.json papers",
                    actual_ids=set(str(key) for key in cached_papers),
                    expected_ids=expected_ids,
                    report_stale=report_stale,
                )
            )
    else:
        grouped.setdefault(cache_path, []).append(
            Issue(cache_path, CHECK_PATH, "embedding_cache.json root is not an object")
        )

    return [(path, issues) for path, issues in grouped.items() if issues]


# ---------------------------------------------------------------------------
# Fix helpers
# ---------------------------------------------------------------------------

_TITLE_LINE_RE = re.compile(r"^title\s*:\s*(?P<value>.*?)(?P<newline>\r?\n?)$")
_BLOCK_SCALAR_HEADER_RE = re.compile(r"^[>|][0-9+-]*(?:\s+#.*)?$")
_EMPTY_YAML_LIST_KEY_RE = re.compile(r"^[ \t]*-\s*:\s*(?:#.*)?\r?\n?", re.M)
_C1_CONTROL_CHAR_RE = re.compile(r"[\u0080-\u009f]")
_AUTHOR_ASCII_TRANSLATION = str.maketrans(
    {
        "ß": "ss",
        "ẞ": "SS",
        "Æ": "AE",
        "æ": "ae",
        "Œ": "OE",
        "œ": "oe",
        "Ø": "O",
        "ø": "o",
        "Đ": "D",
        "đ": "d",
        "Ð": "D",
        "ð": "d",
        "Þ": "Th",
        "þ": "th",
        "Ł": "L",
        "ł": "l",
        "ı": "i",
        "İ": "I",
        "Ŋ": "N",
        "ŋ": "n",
        "Ħ": "H",
        "ħ": "h",
        "‐": "-",
        "‑": "-",
        "‒": "-",
        "–": "-",
        "—": "-",
        "―": "-",
        "’": "'",
        "‘": "'",
        "ʼ": "'",
        "ʹ": "'",
        "ˈ": "'",
        "´": "'",
    }
)


def _format_title_line(new_title: str, line_ending: str = "\n") -> str:
    return _format_metadata_scalar_line("title", new_title, line_ending)


def _is_block_scalar_header(value: str) -> bool:
    return bool(_BLOCK_SCALAR_HEADER_RE.match(value.strip()))


def _is_multiline_quoted_scalar_header(value: str) -> bool:
    stripped = value.lstrip()
    if not stripped or stripped[0] not in ("'", '"'):
        return False

    quote = stripped[0]
    escaped = False
    for char in stripped[1:]:
        if quote == '"' and char == "\\" and not escaped:
            escaped = True
            continue
        if char == quote and not escaped:
            return False
        escaped = False
    return True


def _has_indented_continuation(lines: list[str], start: int) -> bool:
    for line in lines[start + 1 :]:
        if not line.strip():
            continue
        return line.startswith((" ", "\t"))
    return False


def _plain_multiline_title_parts(raw: str) -> tuple[str, str] | None:
    lines = raw.splitlines(keepends=True)
    for start, line in enumerate(lines):
        m = _TITLE_LINE_RE.match(line)
        if not m:
            continue

        value = m.group("value")
        if _is_block_scalar_header(value) or not _has_indented_continuation(
            lines, start
        ):
            return None

        end = start + 1
        continuation_lines = []
        while end < len(lines):
            next_line = lines[end]
            if next_line.strip() and not next_line.startswith((" ", "\t")):
                break
            if next_line.strip():
                continuation_lines.append(next_line.strip())
            end += 1

        header = value.strip()
        try:
            parsed = yaml.safe_load(f"title: {header}\n")
            header = str(parsed.get("title", header)) if isinstance(parsed, dict) else header
        except yaml.YAMLError:
            header = header.strip("'\"")

        continuation = " ".join(continuation_lines)
        return header, continuation

    return None


def _normalize_for_duplicate_title_check(title: str) -> str:
    return " ".join(title.split()).casefold()


def _title_has_garbage(title: str) -> bool:
    return bool(
        _TITLE_HTML_TAG_RE.search(title)
        or _TITLE_MATH_SPAN_RE.search(title)
        or _TITLE_LATEX_COMMAND_RE.search(title)
    )


def _plain_latex_math(text: str) -> str:
    text = text.replace(r"\left", "")
    text = text.replace(r"\right", "")
    text = re.sub(r"\\frac\{([^{}]+)\}\{([^{}]+)\}", r"\1/\2", text)
    text = _TITLE_LATEX_COMMAND_RE.sub(r"\1", text)
    text = text.replace(r"\infty", "∞")
    text = text.replace(r"\times", "x")
    text = re.sub(r"\{([^{}]+)\}", r"\1", text)
    text = re.sub(r"_\{?([^{}\s]+)\}?", r"\1", text)
    text = text.replace("\\", "")
    return text


def _protect_title_spans(title: str) -> tuple[str, list[str], bool]:
    protected: list[str] = []
    changed = False

    def protect(value: str) -> str:
        protected.append(value)
        return f"{_PLACEHOLDER_PREFIX}{len(protected) - 1}"

    def replace_math(m: re.Match[str]) -> str:
        nonlocal changed
        changed = True
        return protect(_plain_latex_math(m.group("math")))

    title = _TITLE_MATH_SPAN_RE.sub(replace_math, title)

    def replace_paired_tag(m: re.Match[str]) -> str:
        nonlocal changed
        changed = True
        inner = _TITLE_HTML_TAG_RE.sub("", m.group("inner"))
        return protect(html.unescape(inner))

    paired_tag_re = re.compile(
        r"<\s*(?P<tag>i|em|b|strong|sub|sup)\b[^>]*>"
        r"(?P<inner>.*?)"
        r"</\s*(?P=tag)\s*>",
        re.I,
    )
    title = paired_tag_re.sub(replace_paired_tag, title)
    return title, protected, changed


def _restore_title_spans(title: str, protected: list[str]) -> str:
    for i, value in enumerate(protected):
        title = title.replace(f"{_PLACEHOLDER_PREFIX}{i}", value)
    return title


def _prepare_title_garbage_fix(title: str) -> tuple[str, list[str], bool]:
    title = html.unescape(title)
    title, protected, changed = _protect_title_spans(title)

    if _TITLE_HTML_TAG_RE.search(title):
        changed = True
        title = _TITLE_HTML_TAG_RE.sub("", title)

    if _TITLE_LATEX_COMMAND_RE.search(title):
        changed = True
        title = _plain_latex_math(title)

    if changed:
        # Removing inline markup can join neighboring tokens, e.g.
        # "to<i>H</i><sub>∞</sub>control" -> "toH∞control".
        title = re.sub(rf"(?<=[a-z])(?={_PLACEHOLDER_PREFIX}\d+)", " ", title)
        title = re.sub(
            rf"({_PLACEHOLDER_PREFIX}\d+)(?!{_PLACEHOLDER_PREFIX})(?=[A-Za-z])",
            r"\1 ",
            title,
        )
        title = re.sub(r"(?<=[a-z])(?=[A-Z∞])", " ", title)
        title = re.sub(r"(?<=[∞])(?=[A-Za-z])", " ", title)
        title = _normalize_title_spacing(title)

    return title, protected, changed


def _suggest_title_fix(raw: str, title: str) -> str:
    title_to_fix = title
    parts = _plain_multiline_title_parts(raw)
    if parts is not None:
        header, continuation = parts
        if (
            header
            and continuation
            and _normalize_for_duplicate_title_check(header)
            == _normalize_for_duplicate_title_check(continuation)
        ):
            title_to_fix = header

    title_to_fix, protected, _ = _prepare_title_garbage_fix(title_to_fix)
    fixed = to_title_case(title_to_fix)
    return _restore_title_spans(fixed, protected)


def _fix_title_in_yaml(raw: str, new_title: str) -> str:
    """Replace the title value in raw YAML text.

    Titles are usually single-line scalars, but older metadata can use folded or
    literal block scalars. In that case the title node spans the `title: >` line
    plus the following indented lines, so replacing only the first line leaves a
    dangling duplicate continuation line behind.
    """
    lines = raw.splitlines(keepends=True)
    for start, line in enumerate(lines):
        m = _TITLE_LINE_RE.match(line)
        if not m:
            continue

        end = start + 1
        value = m.group("value")
        if (
            _is_block_scalar_header(value)
            or _is_multiline_quoted_scalar_header(value)
            or _has_indented_continuation(lines, start)
        ):
            while end < len(lines):
                next_line = lines[end]
                if next_line.strip() and not next_line.startswith((" ", "\t")):
                    break
                end += 1

        replacement = _format_title_line(new_title, m.group("newline"))
        return "".join(lines[:start] + [replacement] + lines[end:])

    return raw


def _is_escaped_sequence_issue(issue: Issue) -> bool:
    return issue.message.startswith("Contains escaped HTML/entity sequence")


def _is_garbled_markup_issue(issue: Issue) -> bool:
    return issue.message.startswith("Contains likely garbled HTML/XML markup")


def _is_big_whitespace_issue(issue: Issue) -> bool:
    return issue.message.startswith(_BIG_WHITESPACE_ISSUE_PREFIX)


def _is_author_mojibake_issue(issue: Issue) -> bool:
    return issue.field == "authors" and issue.message.startswith(
        _AUTHOR_MOJIBAKE_ISSUE_PREFIX
    )


def _is_author_ascii_normalization_issue(issue: Issue) -> bool:
    return issue.field == "authors" and issue.message.startswith(
        _AUTHOR_ASCII_NORMALIZATION_ISSUE_PREFIX
    )


def _is_fixable_author_name_issue(issue: Issue) -> bool:
    return _is_author_mojibake_issue(issue) or _is_author_ascii_normalization_issue(issue)


def _is_fixable_non_individual_author_issue(issue: Issue) -> bool:
    return issue.field == "authors" and issue.message.startswith(
        _NON_INDIVIDUAL_AUTHOR_ISSUE_PREFIX
    )


def _is_publisher_mark_abstract_issue(issue: Issue) -> bool:
    return (
        issue.field == "abstract"
        and issue.message.startswith(_PUBLISHER_MARK_ABSTRACT_ISSUE_PREFIX)
    )


def _is_text_mojibake_issue(issue: Issue) -> bool:
    return issue.message.startswith(_TEXT_MOJIBAKE_ISSUE_PREFIX)


def _is_type_fix_issue(issue: Issue) -> bool:
    return issue.field == "type" and issue.suggestion in VALID_TYPES


def _is_clearable_summary_issue(issue: Issue) -> bool:
    return issue.field == "summary" and (
        issue.message.startswith(_SUMMARY_ABSTRACT_OVERLAP_ISSUE_PREFIX)
        or issue.message.startswith(_LOW_SIGNAL_SUMMARY_ISSUE_PREFIX)
    )


def _is_high_confidence_ocr_artifact_issue(issue: Issue) -> bool:
    return issue.message.startswith(_HIGH_CONFIDENCE_OCR_ARTIFACT_ISSUE_PREFIX)


def _mojibake_byte(char: str) -> int | None:
    codepoint = ord(char)
    if codepoint <= 0xFF:
        return codepoint
    try:
        encoded = char.encode("cp1252")
    except UnicodeError:
        return None
    return encoded[0] if len(encoded) == 1 else None


def _fold_author_name_to_ascii(author: str) -> str:
    translated = author.translate(_AUTHOR_ASCII_TRANSLATION)
    normalized = unicodedata.normalize("NFKD", translated)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    return _normalize_inline_text(ascii_text)


def _delete_publisher_marks_from_abstract(abstract: str) -> tuple[str, int]:
    cleaned = abstract
    removed = 0
    for _, pattern in _PUBLISHER_MARK_ABSTRACT_PATTERNS:
        cleaned, count = pattern.subn("", cleaned)
        removed += count

    if removed:
        cleaned = _normalize_inline_text(cleaned)
        cleaned = re.sub(r"\s+([,.;:])", r"\1", cleaned)
    return cleaned, removed


def _fix_escaped_sequences_in_yaml(raw: str) -> tuple[str, int]:
    new_raw = _html_unescape_repeated(raw)
    return new_raw, len(_HTML_ENTITY_RE.findall(raw))


def _decode_utf8_mojibake_text(text: str) -> tuple[str, int]:
    if not _mojibake_examples(text):
        return text, 0

    pieces: list[str] = []
    decoded = 0
    index = 0
    while index < len(text):
        leading_byte = _mojibake_byte(text[index])
        if leading_byte is None:
            byte_count = 0
        elif 0xC2 <= leading_byte <= 0xDF:
            byte_count = 2
        elif 0xE0 <= leading_byte <= 0xEF:
            byte_count = 3
        elif 0xF0 <= leading_byte <= 0xF4:
            byte_count = 4
        else:
            byte_count = 0

        token = text[index : index + byte_count]
        token_bytes = [
            byte for char in token for byte in [_mojibake_byte(char)] if byte is not None
        ]
        if (
            byte_count
            and len(token) == byte_count
            and len(token_bytes) == byte_count
            and all(0x80 <= byte <= 0xBF for byte in token_bytes[1:])
        ):
            try:
                replacement = bytes(token_bytes).decode("utf-8")
            except UnicodeError:
                replacement = ""
            if replacement and not _C1_CONTROL_CHAR_RE.search(replacement):
                pieces.append(replacement)
                decoded += 1
                index += byte_count
                continue

        pieces.append(text[index])
        index += 1

    fixed = "".join(pieces)
    fixed, orphaned_grave_a = re.subn(r"Ã(?=\s|$)", "à", fixed)
    return fixed, decoded + orphaned_grave_a


def _decode_utf8_mojibake_controls(raw: str) -> tuple[str, int]:
    if not _C1_CONTROL_CHAR_RE.search(raw):
        return raw, 0
    return _decode_utf8_mojibake_text(raw)


def _remove_empty_yaml_list_keys(raw: str) -> tuple[str, int]:
    return _EMPTY_YAML_LIST_KEY_RE.subn("", raw)


def _fix_high_confidence_parse_errors_in_yaml(raw: str) -> tuple[str, list[str]]:
    messages: list[str] = []

    raw, removed_empty_items = _remove_empty_yaml_list_keys(raw)
    if removed_empty_items:
        messages.append(f"  removed {removed_empty_items} empty YAML list item(s)")

    raw, decoded_mojibake = _decode_utf8_mojibake_controls(raw)
    if decoded_mojibake:
        messages.append(f"  decoded {decoded_mojibake} UTF-8 mojibake sequence(s)")

    return raw, messages


def _collapse_big_whitespace_after_indent(line: str) -> tuple[str, int]:
    match = re.match(
        r"^(?P<indent>[ \t]*)(?P<body>.*?)(?P<newline>\r?\n?)$",
        line,
    )
    if not match:
        return line, 0

    body = match.group("body")
    collapsed, count = _BIG_WHITESPACE_RE.subn(" ", body)
    if count == 0:
        return line, 0

    return match.group("indent") + collapsed + match.group("newline"), count


def _fix_big_whitespace_in_yaml(raw: str, fields: set[str]) -> tuple[str, int]:
    lines = raw.splitlines(keepends=True)
    changed = 0
    index = 0
    while index < len(lines):
        parsed = _top_level_field_span(lines, index)
        if parsed is None:
            index += 1
            continue

        field_name, _value, end = parsed
        if field_name not in fields:
            index = end
            continue

        for line_index in range(index, end):
            lines[line_index], count = _collapse_big_whitespace_after_indent(
                lines[line_index]
            )
            changed += count

        index = end

    return "".join(lines), changed


def _clean_garbled_markup_text(text: str) -> str:
    text = html.unescape(text)
    text = _XML_URI_TAG_RE.sub(lambda match: match.group("inner").strip(), text)
    text = _XML_HTML_TAG_RE.sub("", text)
    return _normalize_inline_text(text)


def _fix_garbled_markup_in_yaml(raw: str) -> tuple[str, int]:
    changed = 0
    data = yaml.safe_load(raw)
    if not isinstance(data, dict):
        return raw, 0

    replacements: list[tuple[str, str]] = []
    for _, value in _walk_string_values(data, ""):
        if not isinstance(value, str) or not _GARBLED_MARKUP_RE.search(value):
            continue
        cleaned = _clean_garbled_markup_text(value)
        if cleaned and cleaned != value:
            replacements.append((value, cleaned))

    new_raw = raw
    for old, new in replacements:
        new_raw_next = new_raw.replace(old, new)
        if new_raw_next != new_raw:
            changed += new_raw.count(old)
            new_raw = new_raw_next

    return new_raw, changed


def _format_source_line(source: str, newline: str = "\n") -> str:
    dumped = yaml.safe_dump(
        {"source": source},
        sort_keys=False,
        allow_unicode=True,
        width=1_000_000_000,
    ).strip()
    return dumped + newline


def _fix_source_in_yaml(raw: str, new_source: str) -> str:
    lines = raw.splitlines(keepends=True)
    for start, line in enumerate(lines):
        match = re.match(
            r"^(?P<indent>\s*)source\s*:\s*(?P<value>.*?)(?P<newline>\r?\n)?$",
            line,
        )
        if not match:
            continue

        end = start + 1
        value = match.group("value")
        if (
            _is_block_scalar_header(value)
            or _is_multiline_quoted_scalar_header(value)
            or _has_indented_continuation(lines, start)
        ):
            while end < len(lines):
                next_line = lines[end]
                if next_line.strip() and not next_line.startswith((" ", "\t")):
                    break
                end += 1

        replacement = match.group("indent") + _format_source_line(
            new_source, match.group("newline") or "\n"
        )
        return "".join(lines[:start] + [replacement] + lines[end:])

    return raw


def _is_source_year_issue(issue: Issue) -> bool:
    return (
        issue.field == "source"
        and issue.suggestion is not None
        and issue.message.startswith("Contains year")
    )


def _is_multiline_field_issue(issue: Issue) -> bool:
    return (
        issue.field in _MULTILINE_FORBIDDEN_FIELDS
        and issue.message.startswith("Field must be a single-line scalar")
    )


def _is_folded_text_field_issue(issue: Issue) -> bool:
    return (
        issue.field in _FOLDED_TEXT_FIELDS
        and issue.message.startswith(
            (
                _FOLDED_TEXT_FIELD_ISSUE_PREFIX,
                _FOLDED_TEXT_FIELD_MULTILINE_ISSUE_PREFIX,
            )
        )
    )


def _is_plural_duplicate_tag_issue(issue: Issue) -> bool:
    return (
        issue.field == "tags"
        and issue.message.startswith(_PLURAL_DUPLICATE_TAG_MESSAGE_PREFIX)
    )


def _is_database_duplicate_tag_issue(issue: Issue) -> bool:
    return (
        issue.field == "tags"
        and issue.message.startswith(_DATABASE_DUPLICATE_TAG_MESSAGE_PREFIX)
    )


def _is_duplicate_tag_issue(issue: Issue) -> bool:
    return (
        issue.field == "tags"
        and issue.message.startswith(_DUPLICATE_TAG_MESSAGE_PREFIX)
        and not _is_plural_duplicate_tag_issue(issue)
        and not _is_database_duplicate_tag_issue(issue)
    )


def _is_forbidden_tag_issue(issue: Issue) -> bool:
    return issue.field == "tags" and issue.message.startswith("Forbidden tag at tags[")


def _is_fixable_missing_tag_canonical_replacement(
    issue: Issue,
    added_canonical_tag_keys: set[str],
) -> bool:
    if not _is_tag_database_missing_issue(issue):
        return False
    if issue.suggestion is None or issue.suggestion.startswith("Add "):
        return False
    return tag_key(issue.suggestion) in added_canonical_tag_keys


def _is_fixable_tag_issue(issue: Issue) -> bool:
    if (
        _is_duplicate_tag_issue(issue)
        or _is_plural_duplicate_tag_issue(issue)
        or _is_database_duplicate_tag_issue(issue)
        or _is_forbidden_tag_issue(issue)
    ):
        return True

    return (
        issue.field == "tags"
        and issue.suggestion is not None
        and (
            issue.message.startswith("Tag is not in capital case")
            or issue.message.startswith("Tag starts with an article")
            or issue.message.startswith(_TAG_DATABASE_ISSUE_PREFIX)
        )
    )


def _tag_issue_index(issue: Issue) -> int | None:
    match = re.search(r"tags\[(\d+)\]", issue.message)
    if not match:
        return None
    return int(match.group(1))


def _format_folded_scalar_field(field_name: str, value: str, newline: str) -> str:
    text = _normalize_inline_text(value)
    if not text:
        return f"{field_name}:{newline}"
    return f"{field_name}: >{newline}  {text}{newline}"


def _format_metadata_scalar_line(
    field_name: str,
    value: object,
    newline: str = "\n",
) -> str:
    if value is None or value == "":
        return f"{field_name}:{newline}"

    if isinstance(value, str):
        value = _normalize_inline_text(value)
        if field_name in _FOLDED_TEXT_FIELDS:
            return _format_folded_scalar_field(field_name, value, newline)
        if field_name == "arxiv_id":
            return f"{field_name}: {json.dumps(value, ensure_ascii=False)}{newline}"

    dumped = yaml.safe_dump(
        {field_name: value},
        sort_keys=False,
        allow_unicode=True,
        width=1_000_000_000,
    ).strip()
    return dumped + newline


def _fix_metadata_scalar_field_in_yaml(raw: str, field_name: str, new_value: object) -> str:
    lines = raw.splitlines(keepends=True)
    for start, _line in enumerate(lines):
        parsed = _top_level_field_span(lines, start)
        if parsed is None:
            continue

        current_field_name, _value, end = parsed
        if current_field_name != field_name:
            continue

        match = _TOP_LEVEL_SCALAR_FIELD_RE.match(lines[start])
        newline = match.group("newline") if match else "\n"
        replacement = _format_metadata_scalar_line(
            field_name,
            new_value,
            newline or "\n",
        )
        return "".join(lines[:start] + [replacement] + lines[end:])

    return raw


def _fix_high_confidence_ocr_artifacts_in_yaml(
    raw: str,
    data: dict,
    fields: set[str],
) -> tuple[str, int]:
    fixed_raw = raw
    changed = 0
    for field_name in sorted(fields):
        value = data.get(field_name)
        if not isinstance(value, str):
            continue

        fixed_value, count = _apply_high_confidence_ocr_replacements(value)
        if not count or fixed_value == value:
            continue

        fixed_raw = _fix_metadata_scalar_field_in_yaml(
            fixed_raw,
            field_name,
            fixed_value,
        )
        data[field_name] = fixed_value
        changed += count

    return fixed_raw, changed


def _fix_multiline_fields_in_yaml(
    raw: str,
    data: dict,
    fields: set[str],
) -> tuple[str, int]:
    lines = raw.splitlines(keepends=True)
    changed = 0
    index = 0
    while index < len(lines):
        parsed = _top_level_field_span(lines, index)
        if parsed is None:
            index += 1
            continue

        field_name, value, end = parsed
        if (
            field_name in fields
            and field_name in _MULTILINE_FORBIDDEN_FIELDS
            and (end > index + 1 or _is_block_scalar_header(value))
        ):
            match = _TOP_LEVEL_SCALAR_FIELD_RE.match(lines[index])
            newline = match.group("newline") if match else "\n"
            replacement = _format_metadata_scalar_line(
                field_name,
                data.get(field_name),
                newline or "\n",
            )
            lines[index:end] = [replacement]
            changed += 1
            index += 1
            continue

        index = end

    return "".join(lines), changed


def _fix_folded_text_fields_in_yaml(
    raw: str,
    data: dict,
    fields: set[str],
) -> tuple[str, list[str]]:
    fixed_raw = raw
    changed_fields: list[str] = []
    for field_name in sorted(fields):
        value = data.get(field_name)
        if not isinstance(value, str) or not value.strip():
            continue
        new_raw = _fix_metadata_scalar_field_in_yaml(fixed_raw, field_name, value)
        if new_raw != fixed_raw:
            fixed_raw = new_raw
            changed_fields.append(field_name)
    return fixed_raw, changed_fields


def _format_authors_block(authors: list[object], newline: str = "\n") -> str:
    if not authors:
        return f"authors:{newline}"

    lines = ["authors:"]
    for author in authors:
        if author is None or author == "":
            lines.append("  -")
            continue
        dumped = yaml.safe_dump(
            [author],
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
            width=1_000_000_000,
        ).strip()
        item = dumped.removeprefix("-").strip()
        lines.append(f"  - {item}")
    return newline.join(lines) + newline


def _fix_author_names_in_yaml(raw: str, data: dict) -> tuple[str, int, int]:
    authors_raw = data.get("authors")
    if not isinstance(authors_raw, list):
        return raw, 0, 0

    authors = list(authors_raw)
    changed_authors = 0
    decoded_sequences = 0
    for index, author in enumerate(authors):
        if not isinstance(author, str):
            continue

        decoded_author, count = _decode_utf8_mojibake_text(author)
        fixed_author = _fold_author_name_to_ascii(decoded_author)
        if not fixed_author or fixed_author == author:
            continue

        authors[index] = fixed_author
        changed_authors += 1
        decoded_sequences += count

    if changed_authors == 0:
        return raw, 0, 0

    lines = raw.splitlines(keepends=True)
    for start, line in enumerate(lines):
        match = re.match(
            r"^(?P<indent>\s*)authors\s*:\s*(?P<value>.*?)(?P<newline>\r?\n)?$",
            line,
        )
        if not match:
            continue

        end = start + 1
        value = match.group("value")
        if (
            _is_block_scalar_header(value)
            or _is_multiline_quoted_scalar_header(value)
            or _has_indented_continuation(lines, start)
        ):
            while end < len(lines):
                next_line = lines[end]
                if next_line.strip() and not next_line.startswith((" ", "\t")):
                    break
                end += 1

        replacement = match.group("indent") + _format_authors_block(
            authors,
            match.group("newline") or "\n",
        )
        return (
            "".join(lines[:start] + [replacement] + lines[end:]),
            changed_authors,
            decoded_sequences,
        )

    return raw, 0, 0


_KNOWN_SINGLE_AUTHOR_REPLACEMENTS = {
    "IEEE": "IEEE Standards Association",
    "Lozano-Perez": "Tomas Lozano-Perez",
}


def _looks_like_split_author_token(author: object) -> bool:
    if not isinstance(author, str):
        return False
    return bool(re.fullmatch(r"[A-Z][A-Za-z'-]*", author.strip()))


def _is_removable_collective_author(author: object) -> bool:
    if not isinstance(author, str):
        return False
    reason = _non_individual_author_reason(author)
    return bool(reason and reason != "single-token author")


def _repair_non_individual_author_list(authors_raw: list[object]) -> tuple[list[object], int]:
    authors: list[object] = []
    changed = 0
    index = 0
    while index < len(authors_raw):
        author = authors_raw[index]
        if isinstance(author, str) and author in _KNOWN_SINGLE_AUTHOR_REPLACEMENTS:
            authors.append(_KNOWN_SINGLE_AUTHOR_REPLACEMENTS[author])
            changed += 1
            index += 1
            continue

        if len(authors_raw) > 1 and _is_removable_collective_author(author):
            changed += 1
            index += 1
            continue

        if (
            index + 1 < len(authors_raw)
            and _looks_like_split_author_token(author)
            and _looks_like_split_author_token(authors_raw[index + 1])
        ):
            combined = f"{str(author).strip()} {str(authors_raw[index + 1]).strip()}"
            if _non_individual_author_reason(combined) is None:
                authors.append(combined)
                changed += 1
                index += 2
                continue

        authors.append(author)
        index += 1

    return authors, changed


def _fix_non_individual_authors_in_yaml(raw: str, data: dict) -> tuple[str, int]:
    authors_raw = data.get("authors")
    if not isinstance(authors_raw, list):
        return raw, 0
    authors, changed = _repair_non_individual_author_list(authors_raw)
    if not changed:
        return raw, 0

    lines = raw.splitlines(keepends=True)
    for start, line in enumerate(lines):
        match = re.match(
            r"^(?P<indent>\s*)authors\s*:\s*(?P<value>.*?)(?P<newline>\r?\n)?$",
            line,
        )
        if not match:
            continue

        end = start + 1
        value = match.group("value")
        if (
            _is_block_scalar_header(value)
            or _is_multiline_quoted_scalar_header(value)
            or _has_indented_continuation(lines, start)
        ):
            while end < len(lines):
                next_line = lines[end]
                if next_line.strip() and not next_line.startswith((" ", "\t")):
                    break
                end += 1

        replacement = match.group("indent") + _format_authors_block(
            authors,
            match.group("newline") or "\n",
        )
        return "".join(lines[:start] + [replacement] + lines[end:]), changed

    return raw, 0


def _fix_mojibake_text_fields_in_yaml(
    raw: str,
    data: dict,
    fields: set[str],
) -> tuple[str, int]:
    fixed_raw = raw
    changed = 0
    for field_name in sorted(fields):
        value = data.get(field_name)
        if not isinstance(value, str):
            continue
        fixed_value, count = _decode_utf8_mojibake_text(value)
        if not count or fixed_value == value:
            continue
        fixed_raw = _fix_metadata_scalar_field_in_yaml(
            fixed_raw,
            field_name,
            fixed_value,
        )
        data[field_name] = fixed_value
        changed += count
    return fixed_raw, changed


def _format_tags_block(tags: list[object], newline: str = "\n") -> str:
    if not tags:
        return f"tags:{newline}"

    lines = ["tags:"]
    for tag in tags:
        if tag is None or tag == "":
            lines.append("  -")
            continue
        dumped = yaml.safe_dump(
            [tag],
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
            width=1_000_000_000,
        ).strip()
        item = dumped.removeprefix("-").strip()
        lines.append(f"  - {item}")
    return newline.join(lines) + newline


def _fix_tags_in_yaml(
    raw: str,
    data: dict,
    tag_fixes: list[Issue],
) -> tuple[str, int]:
    tags_raw = data.get("tags")
    if not isinstance(tags_raw, list):
        return raw, 0

    tags = list(tags_raw)
    changed = 0
    for issue in tag_fixes:
        if (
            _is_duplicate_tag_issue(issue)
            or _is_plural_duplicate_tag_issue(issue)
            or _is_database_duplicate_tag_issue(issue)
            or _is_forbidden_tag_issue(issue)
        ):
            continue

        index = _tag_issue_index(issue)
        if index is None or index < 0 or index >= len(tags):
            continue
        if tags[index] == issue.suggestion:
            continue
        tags[index] = issue.suggestion
        changed += 1

    forbidden_tag_indexes = {
        index
        for issue in tag_fixes
        if _is_forbidden_tag_issue(issue)
        for index in [_tag_issue_index(issue)]
        if index is not None and 0 <= index < len(tags)
    }
    for index in sorted(forbidden_tag_indexes, reverse=True):
        del tags[index]
        changed += 1

    if any(_is_duplicate_tag_issue(issue) for issue in tag_fixes):
        for index in sorted(_duplicate_tag_removal_indexes(tags), reverse=True):
            del tags[index]
            changed += 1

    if any(_is_plural_duplicate_tag_issue(issue) for issue in tag_fixes):
        for index in sorted(_plural_duplicate_tag_removal_indexes(tags), reverse=True):
            del tags[index]
            changed += 1

    if any(_is_database_duplicate_tag_issue(issue) for issue in tag_fixes):
        for index in sorted(_duplicate_tag_removal_indexes(tags), reverse=True):
            del tags[index]
            changed += 1
        for index in sorted(_database_duplicate_tag_removal_indexes(tags), reverse=True):
            del tags[index]
            changed += 1

    if changed == 0:
        return raw, 0

    lines = raw.splitlines(keepends=True)
    for start, line in enumerate(lines):
        match = re.match(
            r"^(?P<indent>\s*)tags\s*:\s*(?P<value>.*?)(?P<newline>\r?\n)?$",
            line,
        )
        if not match:
            continue

        end = start + 1
        value = match.group("value")
        if (
            _is_block_scalar_header(value)
            or _is_multiline_quoted_scalar_header(value)
            or _has_indented_continuation(lines, start)
        ):
            while end < len(lines):
                next_line = lines[end]
                if next_line.strip() and not next_line.startswith((" ", "\t")):
                    break
                end += 1
        elif not value.strip():
            while end < len(lines):
                next_line = lines[end]
                if not next_line.strip():
                    end += 1
                    continue
                if re.match(r"^-\s+", next_line):
                    end += 1
                    continue
                break

        replacement = match.group("indent") + _format_tags_block(
            tags,
            match.group("newline") or "\n",
        )
        return "".join(lines[:start] + [replacement] + lines[end:]), changed

    return raw, 0


_REFERENCE_SKIP_DIRS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "node_modules",
    "site",
}
_REFERENCE_TEXT_SUFFIXES = {
    ".css",
    ".html",
    ".js",
    ".json",
    ".md",
    ".py",
    ".txt",
    ".yaml",
    ".yml",
}


def _path_parts(path: Path) -> tuple[Path, str, str] | None:
    parts = path.parts
    try:
        papers_idx = next(i for i, p in enumerate(parts) if p == "papers")
        papers_root = Path(*parts[: papers_idx + 1])
        path_year_str = parts[papers_idx + 1]
        path_slug = "/".join(parts[papers_idx + 2 : -1])
    except (StopIteration, IndexError):
        return None
    if not path_slug:
        return None
    return papers_root, path_year_str, path_slug


def _path_fix_for(path: Path, kb_root: Path) -> PathFix | None:
    try:
        raw = path.read_text(encoding="utf-8")
        data = yaml.safe_load(raw)
    except Exception:
        return None
    if not isinstance(data, dict):
        return None

    parsed = _path_parts(path)
    if parsed is None:
        return None
    papers_root, path_year_str, path_slug = parsed

    meta_year = data.get("year")
    try:
        year = int(meta_year)
    except (TypeError, ValueError):
        if not re.match(r"^\d{4}$", path_year_str):
            return None
        year = int(path_year_str)

    if not (1000 <= year <= 9999):
        return None

    title = str(data.get("title") or "").strip()
    authors_raw = data.get("authors")
    authors = [str(author) for author in authors_raw] if isinstance(authors_raw, list) else []
    arxiv_id = str(data.get("arxiv_id") or "").strip()
    if not title or not authors:
        return None

    new_slug = expected_slug(year, arxiv_id, title, authors)
    if path_year_str == str(year) and path_slug == new_slug:
        return None

    new_path = papers_root / str(year) / Path(new_slug) / path.name
    old_resolved = path.resolve()
    new_resolved = new_path.resolve()
    if old_resolved == new_resolved:
        return None

    try:
        old_rel = old_resolved.relative_to(kb_root.resolve()).as_posix()
        new_rel = new_resolved.relative_to(kb_root.resolve()).as_posix()
    except ValueError:
        old_rel = path.as_posix()
        new_rel = new_path.as_posix()

    return PathFix(path, new_path, old_rel, new_rel)


def _replacement_search_root(kb_root: Path) -> Path:
    parent = kb_root.resolve().parent
    if kb_root.name == "knowledge_base" and (parent / "README.md").exists():
        return parent
    return kb_root


def _should_scan_reference_file(path: Path) -> bool:
    if any(part in _REFERENCE_SKIP_DIRS for part in path.parts):
        return False
    return path.is_file() and path.suffix.lower() in _REFERENCE_TEXT_SUFFIXES


def _reference_replacements(path_fix: PathFix) -> list[tuple[str, str]]:
    old_abs = path_fix.old_path.resolve().as_posix()
    new_abs = path_fix.new_path.resolve().as_posix()
    old_rel = path_fix.old_rel
    new_rel = path_fix.new_rel
    old_slug = old_rel.removeprefix("docs/papers/").removesuffix("/metadata.yml")
    new_slug = new_rel.removeprefix("docs/papers/").removesuffix("/metadata.yml")
    if "/" in old_slug:
        old_slug = "/".join(old_slug.split("/")[1:])
    if "/" in new_slug:
        new_slug = "/".join(new_slug.split("/")[1:])
    old_id = re.sub(r"[^a-zA-Z0-9]+", "_", old_slug.lower()).strip("_")
    new_id = re.sub(r"[^a-zA-Z0-9]+", "_", new_slug.lower()).strip("_")
    replacements = [
        (old_abs, new_abs),
        (old_rel, new_rel),
    ]
    if old_id and new_id and old_id != new_id:
        replacements.extend(
            [
                (f"papers/{old_id}.md", f"papers/{new_id}.md"),
                (old_id, new_id),
            ]
        )
    if not old_rel.startswith("./"):
        replacements.append((f"./{old_rel}", f"./{new_rel}"))
    if old_rel.startswith("docs/papers/"):
        replacements.append(
            (
                f"../knowledge_base/{old_rel}",
                f"../knowledge_base/{new_rel}",
            )
        )
    return replacements


def _rewrite_path_references(path_fix: PathFix, kb_root: Path) -> int:
    changed = 0
    search_root = _replacement_search_root(kb_root)
    replacements = _reference_replacements(path_fix)
    for candidate in search_root.rglob("*"):
        if not _should_scan_reference_file(candidate):
            continue
        try:
            raw = candidate.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        new_raw = raw
        for old, new in replacements:
            new_raw = new_raw.replace(old, new)
        if new_raw == raw:
            continue
        candidate.write_text(new_raw, encoding="utf-8")
        changed += 1
    return changed


def _prune_empty_dirs(start: Path, stop: Path) -> None:
    current = start
    stop = stop.resolve()
    while current.resolve() != stop and current.exists():
        try:
            current.rmdir()
        except OSError:
            return
        current = current.parent


def _apply_path_fix(path_fix: PathFix, kb_root: Path) -> bool:
    old_dir = path_fix.old_path.parent
    new_dir = path_fix.new_path.parent
    if path_fix.new_path.exists():
        err_console.print(
            f"[red]Error fixing path {path_fix.old_path}:[/] destination already exists: {path_fix.new_path}"
        )
        return False

    try:
        new_dir.parent.mkdir(parents=True, exist_ok=True)
        moved_whole_dir = not new_dir.exists()
        if new_dir.exists():
            shutil.move(str(path_fix.old_path), str(path_fix.new_path))
        else:
            shutil.move(str(old_dir), str(new_dir))
        references_changed = _rewrite_path_references(path_fix, kb_root)
        parsed = _path_parts(path_fix.old_path)
        if parsed is not None:
            papers_root, path_year_str, _ = parsed
            prune_start = old_dir.parent if moved_whole_dir else old_dir
            _prune_empty_dirs(prune_start, papers_root / path_year_str)
        console.print(f"[green]Moved:[/] {path_fix.old_rel} [green]->[/] {path_fix.new_rel}")
        console.print(f"  updated references in {references_changed} file(s)")
        return True
    except Exception as exc:
        err_console.print(f"[red]Error fixing path {path_fix.old_path}:[/] {exc}")
        return False


def apply_fixes(
    results: list[tuple[Path, list[Issue]]],
    *,
    kb_root: Path,
    fix_paths: bool = True,
) -> dict[Path, Path]:
    fixed = 0
    path_replacements: dict[Path, Path] = {}
    metadata_paths_seen: set[Path] = set()
    added_tag_canonical_fixes = _write_missing_tag_canonical_fixes(
        _collect_missing_tag_canonical_fixes(results)
    )
    added_canonical_tag_keys = set(added_tag_canonical_fixes)
    if added_tag_canonical_fixes:
        console.print("[green]Updated:[/] normalization/tags.yml")
        console.print(
            f"  added {len(added_tag_canonical_fixes)} canonical tag entr"
            f"{'y' if len(added_tag_canonical_fixes) == 1 else 'ies'}"
        )

    for path, issues in results:
        if path.name == "metadata.yml":
            metadata_paths_seen.add(path)
        has_parse_fixes = any(i.field == "parse" for i in issues)
        title_fixes = [
            i
            for i in issues
            if i.field == "title"
            and i.suggestion is not None
            and not _is_multiline_field_issue(i)
            and not _is_folded_text_field_issue(i)
        ]
        source_year_fixes = [i for i in issues if _is_source_year_issue(i)]
        tag_fixes = [
            i
            for i in issues
            if _is_fixable_tag_issue(i)
            or _is_fixable_missing_tag_canonical_replacement(
                i,
                added_canonical_tag_keys,
            )
        ]
        abstract_publisher_fixes = [
            i for i in issues if _is_publisher_mark_abstract_issue(i)
        ]
        author_name_fixes = [i for i in issues if _is_fixable_author_name_issue(i)]
        non_individual_author_fixes = [
            i for i in issues if _is_fixable_non_individual_author_issue(i)
        ]
        type_fixes = [i for i in issues if _is_type_fix_issue(i)]
        summary_clear_fixes = [i for i in issues if _is_clearable_summary_issue(i)]
        mojibake_text_fields = {
            i.field for i in issues if _is_text_mojibake_issue(i)
        }
        ocr_artifact_fields = {
            i.field for i in issues if _is_high_confidence_ocr_artifact_issue(i)
        }
        multiline_fields = {i.field for i in issues if _is_multiline_field_issue(i)}
        folded_text_fields = {
            i.field for i in issues if _is_folded_text_field_issue(i)
        }
        has_escaped_sequence_fixes = any(_is_escaped_sequence_issue(i) for i in issues)
        has_garbled_markup_fixes = any(_is_garbled_markup_issue(i) for i in issues)
        whitespace_fields = {
            re.split(r"[.\[]", i.field, maxsplit=1)[0]
            for i in issues
            if _is_big_whitespace_issue(i)
        }
        if (
            not has_parse_fixes
            and not title_fixes
            and not source_year_fixes
            and not tag_fixes
            and not abstract_publisher_fixes
            and not author_name_fixes
            and not non_individual_author_fixes
            and not type_fixes
            and not summary_clear_fixes
            and not mojibake_text_fields
            and not ocr_artifact_fields
            and not multiline_fields
            and not folded_text_fields
            and not has_escaped_sequence_fixes
            and not has_garbled_markup_fixes
            and not whitespace_fields
        ):
            continue
        try:
            raw = path.read_text(encoding="utf-8")
            new_raw = raw
            messages = []

            if has_parse_fixes:
                new_raw, parse_messages = _fix_high_confidence_parse_errors_in_yaml(
                    new_raw
                )
                messages.extend(parse_messages)

            if title_fixes:
                new_title = title_fixes[0].suggestion
                old_title = (yaml.safe_load(new_raw) or {}).get("title", "")
                new_raw = _fix_title_in_yaml(new_raw, new_title)
                messages.append(f"  title: {old_title!r} [green]->[/] {new_title!r}")

            if source_year_fixes:
                old_source = yaml.safe_load(new_raw).get("source", "")
                new_source = source_year_fixes[0].suggestion
                new_raw = _fix_source_in_yaml(new_raw, new_source)
                messages.append(f"  source: {old_source!r} [green]->[/] {new_source!r}")

            if abstract_publisher_fixes:
                parsed = yaml.safe_load(new_raw) or {}
                old_abstract = str(parsed.get("abstract") or "")
                new_abstract, n_removed_marks = _delete_publisher_marks_from_abstract(
                    old_abstract
                )
                if n_removed_marks and new_abstract != old_abstract:
                    new_raw = _fix_metadata_scalar_field_in_yaml(
                        new_raw,
                        "abstract",
                        new_abstract,
                    )
                    messages.append(
                        "  removed "
                        f"{n_removed_marks} publisher/copyright notice(s) from abstract"
                    )

            if author_name_fixes:
                parsed = yaml.safe_load(new_raw) or {}
                (
                    new_raw,
                    n_fixed_authors,
                    n_decoded_author_sequences,
                ) = _fix_author_names_in_yaml(new_raw, parsed)
                if n_fixed_authors:
                    if n_decoded_author_sequences:
                        messages.append(
                            "  decoded "
                            f"{n_decoded_author_sequences} author mojibake sequence(s) "
                            f"and ASCII-normalized {n_fixed_authors} name(s)"
                        )
                    else:
                        messages.append(
                            f"  ASCII-normalized {n_fixed_authors} author name(s)"
                        )

            if non_individual_author_fixes:
                parsed = yaml.safe_load(new_raw) or {}
                new_raw, n_repaired_authors = _fix_non_individual_authors_in_yaml(
                    new_raw,
                    parsed,
                )
                if n_repaired_authors:
                    messages.append(
                        f"  repaired {n_repaired_authors} non-individual author entry(s)"
                    )

            if type_fixes:
                parsed = yaml.safe_load(new_raw) or {}
                old_type = parsed.get("type", "")
                new_type = type_fixes[0].suggestion
                new_raw = _fix_metadata_scalar_field_in_yaml(new_raw, "type", new_type)
                messages.append(f"  type: {old_type!r} [green]->[/] {new_type!r}")

            if summary_clear_fixes:
                new_raw = _fix_metadata_scalar_field_in_yaml(new_raw, "summary", "")
                messages.append("  cleared copied or low-signal summary")

            if mojibake_text_fields:
                parsed = yaml.safe_load(new_raw) or {}
                new_raw, n_decoded_text = _fix_mojibake_text_fields_in_yaml(
                    new_raw,
                    parsed,
                    mojibake_text_fields,
                )
                if n_decoded_text:
                    fields = ", ".join(sorted(mojibake_text_fields))
                    messages.append(
                        f"  decoded {n_decoded_text} text mojibake sequence(s): {fields}"
                    )

            if ocr_artifact_fields:
                parsed = yaml.safe_load(new_raw) or {}
                new_raw, n_fixed_ocr = _fix_high_confidence_ocr_artifacts_in_yaml(
                    new_raw,
                    parsed,
                    ocr_artifact_fields,
                )
                if n_fixed_ocr:
                    fields = ", ".join(sorted(ocr_artifact_fields))
                    messages.append(
                        "  fixed "
                        f"{n_fixed_ocr} high-confidence OCR artifact(s): {fields}"
                    )

            if multiline_fields:
                parsed = yaml.safe_load(new_raw) or {}
                new_raw, n_single_lined = _fix_multiline_fields_in_yaml(
                    new_raw,
                    parsed,
                    multiline_fields,
                )
                if n_single_lined:
                    fields = ", ".join(sorted(multiline_fields))
                    messages.append(f"  single-lined {n_single_lined} field(s): {fields}")

            if folded_text_fields:
                parsed = yaml.safe_load(new_raw) or {}
                new_raw, folded_fields = _fix_folded_text_fields_in_yaml(
                    new_raw,
                    parsed,
                    folded_text_fields,
                )
                if folded_fields:
                    fields = ", ".join(folded_fields)
                    messages.append(
                        f"  folded {len(folded_fields)} text field(s): {fields}"
                    )

            if tag_fixes:
                parsed = yaml.safe_load(new_raw) or {}
                new_raw, n_fixed_tags = _fix_tags_in_yaml(
                    new_raw,
                    parsed,
                    tag_fixes,
                )
                if n_fixed_tags:
                    messages.append(f"  fixed {n_fixed_tags} tag(s)")

            if has_escaped_sequence_fixes:
                new_raw, n_decoded = _fix_escaped_sequences_in_yaml(new_raw)
                if n_decoded:
                    messages.append(f"  decoded {n_decoded} escaped sequence(s)")

            if has_garbled_markup_fixes:
                new_raw, n_cleaned_markup = _fix_garbled_markup_in_yaml(new_raw)
                if n_cleaned_markup:
                    messages.append(f"  cleaned {n_cleaned_markup} markup fragment(s)")

            if whitespace_fields:
                new_raw, n_collapsed_spaces = _fix_big_whitespace_in_yaml(
                    new_raw,
                    whitespace_fields,
                )
                if n_collapsed_spaces:
                    fields = ", ".join(sorted(whitespace_fields))
                    messages.append(
                        "  collapsed "
                        f"{n_collapsed_spaces} large whitespace run(s): {fields}"
                    )

            if new_raw == raw:
                err_console.print(f"  [dim](no change written for {path})[/]")
                continue
            yaml.safe_load(new_raw)
            path.write_text(new_raw, encoding="utf-8")
            console.print(f"[green]Fixed:[/] {path}")
            for message in messages:
                console.print(message)
            fixed += 1
        except Exception as exc:
            err_console.print(f"[red]Error fixing {path}:[/] {exc}")

    moved = 0
    for path in sorted(metadata_paths_seen):
        if not fix_paths or not path.exists():
            continue
        path_fix = _path_fix_for(path, kb_root)
        if path_fix is None:
            continue
        if _apply_path_fix(path_fix, kb_root):
            path_replacements[path] = path_fix.new_path
            moved += 1

    tag_entry_summary = (
        f"; {len(added_tag_canonical_fixes)} canonical tag entr"
        f"{'y' if len(added_tag_canonical_fixes) == 1 else 'ies'} added"
        if added_tag_canonical_fixes
        else ""
    )
    console.print(
        f"\n[green]{fixed} file(s) fixed; {moved} path(s) moved"
        f"{tag_entry_summary}.[/]"
    )
    return path_replacements


def _flatten_check_args(check_args: list[list[str]] | None) -> list[str]:
    if not check_args:
        return []
    return [name for group in check_args for name in group]


def _normalize_check_names(names: list[str]) -> tuple[set[str], list[str]]:
    selected: set[str] = set()
    invalid: list[str] = []
    valid = set(CHECKS)
    for name in names:
        if name in valid:
            selected.add(name)
        else:
            invalid.append(name)
    return selected, invalid


def _audit_status(data: dict) -> str:
    return str(data.get(AUDIT_STATUS_FIELD) or "").strip()


def _read_audit_status(path: Path) -> str | None:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return None
    if not isinstance(data, dict):
        return None
    return _audit_status(data)


def _filter_targets_by_audit_status(
    targets: list[Path],
    audit_status: str,
) -> tuple[list[Path], int]:
    filtered: list[Path] = []
    unreadable = 0
    for path in targets:
        status = _read_audit_status(path)
        if status is None:
            unreadable += 1
            continue
        if status == audit_status:
            filtered.append(path)
    return filtered, unreadable


def _skip_reviewed_errors(data: dict, issues: list[Issue]) -> tuple[list[Issue], int]:
    if _audit_status(data) != "reviewed":
        return issues, 0

    kept = [issue for issue in issues if issue.severity != Severity.ERROR]
    return kept, len(issues) - len(kept)


def _filter_results_by_severity(
    results: list[tuple[Path, list[Issue]]],
    *,
    minimum: Severity,
) -> list[tuple[Path, list[Issue]]]:
    minimum_rank = _SEVERITY_RANK[minimum]
    filtered: list[tuple[Path, list[Issue]]] = []
    for path, issues in results:
        kept = [
            issue
            for issue in issues
            if _SEVERITY_RANK[issue.severity] >= minimum_rank
        ]
        if kept:
            filtered.append((path, kept))
    return filtered


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit metadata.yml files under knowledge_base/docs/papers/.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Checks performed on each metadata.yml:
  unknown   - ERROR for any field not in the VALID_FIELDS schema
  required  - ERROR if any of title, authors, year, abstract, type, audit_status missing
  title     - ERROR if empty; ERROR if not in title case; ERROR for raw YAML character escapes like \\u2014; ERROR/WARN for corrupt characters or likely misspellings
  algorithm - ERROR if the algorithm label is generic; WARN if a bare concrete method label appears to describe analysis/application of an existing method rather than the proposing paper
  authors   - ERROR if not a non-empty list of non-blank strings; ERROR if entries look like Last, First order, single-token names, known organization names, other non-individual names, suspicious Unicode corruption/control characters, or names that are not normalized to the native 26 English letters
  tags      - ERROR if tags are missing from normalization/tags.yml, differ from its canonical full-spelling form, duplicate after database or plural normalization, contain forbidden generic values, leading articles, more than 4 words, non-capital-case ordinary English words, or sentence-like prose debris copied from an abstract
  year      - ERROR if not a 4-digit integer
  arxiv     - ERROR if arxiv_id is present but not a valid arXiv ID
  abstract  - ERROR if placeholder-like, contains scraped page text, publisher/copyright notices, or PDF extraction artifacts; ERROR if near-empty unless audit_status is reviewed; WARN if empty, or for dollar math, copied "abstract" headings, likely misspellings, high-confidence OCR artifacts, or OCR word splits
  escape    - ERROR if string fields contain HTML/entity escapes like &#39; or &amp;, or if title contains raw YAML character escapes like \\u2014
  url       - ERROR if URLs appear in title, algorithm, authors, year, source, type, doi, arxiv_id, tags, or audit_status; ERROR if links contain garbled HTML/XML markup
  multiline - ERROR if one-line scalar fields span multiple YAML lines, or if title/abstract/summary do not use folded `>` YAML style with a single content line
  source    - ERROR if the source/venue field contains a publication year
  type      - ERROR if not a recognised paper type
  status    - ERROR if audit_status is not one of: raw, partial, reviewed
  path      - ERROR if YEAR/SLUG do not match metadata or expected slug format; ERROR if map-data.js or embedding_cache.json IDs are stale, missing, malformed, or inconsistent
  summary   - ERROR if it has substantial verbatim overlap with the abstract or known low-signal generated boilerplate; WARN if missing, empty, or likely misspelled
  optional  - INFO for each optional field that is not populated
  whitespace - ERROR if any string field contains 3 or more consecutive spaces

By default, every check runs. Use --check to opt into a smaller set:
  --check abstract escape

Use --severity to filter reported issues by severity threshold:
  --severity error    # ERROR only
  --severity warning  # WARNING and ERROR
  --severity info     # INFO, WARNING, and ERROR

Available --check names:
  unknown required title algorithm authors tags year arxiv abstract escape url multiline source type status path summary optional whitespace
""",
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Repository root (default: current directory)",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help=(
            "Auto-fix title-case, tag database aliases/casing/leading articles/duplicate tags, "
            "high-confidence missing tag canonical entries, "
            "abstract publisher/copyright notices, high-confidence OCR artifacts, "
            "escaped HTML/entity/markup issues, author-name mojibake/diacritics, "
            "text-field mojibake, obvious collective/split author entries, "
            "blank arXiv-backed type fields, copied or low-signal summaries, "
            "high-confidence parse artifacts, "
            "multiline scalar fields, folded text-field style/content, large whitespace runs, "
            "source years, and path slugs; path fixes move metadata directories "
            "after metadata edits and update direct references"
        ),
    )
    parser.add_argument(
        "--file",
        metavar="PATH",
        help="Audit a single metadata.yml instead of the whole tree",
    )
    parser.add_argument(
        "--audit-status",
        choices=VALID_AUDIT_STATUSES,
        metavar="STATUS",
        help=(
            "Audit only metadata files whose audit_status matches STATUS. "
            "Choices: " + ", ".join(VALID_AUDIT_STATUSES)
        ),
    )
    parser.add_argument(
        "--check",
        nargs="+",
        action="append",
        metavar="NAME",
        dest="check_names",
        help="Run only the named checks. Names: " + ", ".join(CHECKS),
    )
    parser.add_argument(
        "--skip-reviewed-errors",
        action="store_true",
        help="Do not report or fail on ERROR issues for metadata with audit_status: reviewed",
    )
    parser.add_argument(
        "--severity",
        choices=[severity.value for severity in Severity],
        default=Severity.INFO.value,
        metavar="LEVEL",
        help=(
            "Minimum severity to report: error shows ERROR only; warning shows "
            "WARNING and ERROR; info shows INFO, WARNING, and ERROR (default: info)"
        ),
    )
    args = parser.parse_args()
    selected_names, invalid_names = _normalize_check_names(
        _flatten_check_args(args.check_names)
    )
    if invalid_names:
        parser.error(
            "unknown --check value(s): "
            + ", ".join(sorted(set(invalid_names)))
            + "\nvalid values: "
            + ", ".join(CHECKS)
        )
    selected_checks = selected_names or None

    if args.file:
        targets = [Path(args.file)]
    else:
        papers_root = Path(args.root) / "docs" / "papers"
        if not papers_root.exists():
            sys.exit(f"Papers directory not found: {papers_root}")
        targets = sorted(papers_root.rglob("metadata.yml"))
    kb_root = Path(args.root)
    if args.audit_status:
        targets, unreadable_status_count = _filter_targets_by_audit_status(
            targets,
            args.audit_status,
        )
        if unreadable_status_count:
            console.print(
                f"[dim]Skipped {unreadable_status_count} file(s) whose "
                f"{AUDIT_STATUS_FIELD} could not be read while applying "
                f"--audit-status {args.audit_status}.[/]"
            )
        if not targets:
            console.print(
                f"[yellow]No metadata.yml file(s) matched "
                f"{AUDIT_STATUS_FIELD}: {args.audit_status}.[/]"
            )
            return

    skipped_reviewed_errors = 0
    results: list[tuple[Path, list[Issue]]] = []
    checked_file_count = len(targets)
    checked_map_data = selected_checks is None or CHECK_PATH in selected_checks
    report_stale_map_ids = not args.file and args.audit_status is None
    for p in targets:
        data, issues = audit_file(p, selected_checks=selected_checks)
        if args.skip_reviewed_errors:
            issues, skipped_count = _skip_reviewed_errors(data, issues)
            skipped_reviewed_errors += skipped_count
        if issues:
            results.append((p, issues))
    if checked_map_data:
        checked_file_count += 2
        results.extend(
            audit_map_data_paths(
                targets,
                kb_root=kb_root,
                report_stale=report_stale_map_ids,
            )
        )

    minimum_severity = Severity(args.severity)
    results = _filter_results_by_severity(results, minimum=minimum_severity)

    all_issues = [i for _, issues in results for i in issues]
    n_errors = sum(1 for i in all_issues if i.severity == Severity.ERROR)
    n_warnings = sum(1 for i in all_issues if i.severity == Severity.WARNING)
    n_infos = sum(1 for i in all_issues if i.severity == Severity.INFO)

    if not all_issues:
        if checked_map_data:
            console.print(
                f"[green]All {len(targets)} metadata.yml file(s) and map data pass audit.[/]"
            )
        else:
            console.print(f"[green]All {len(targets)} metadata.yml file(s) pass audit.[/]")
        if skipped_reviewed_errors:
            console.print(
                f"[dim]Skipped {skipped_reviewed_errors} error(s) from reviewed metadata.[/]"
            )
        return

    parts = []
    if n_errors:
        parts.append(f"[bold red]{n_errors} error(s)[/]")
    if n_warnings:
        parts.append(f"[bold yellow]{n_warnings} warning(s)[/]")
    if n_infos:
        parts.append(f"[bold cyan]{n_infos} info(s)[/]")
    console.print(
        ", ".join(parts) + f" across {len(results)} / {checked_file_count} file(s):\n"
    )
    if skipped_reviewed_errors:
        console.print(
            f"[dim]Skipped {skipped_reviewed_errors} error(s) from reviewed metadata.[/]\n"
        )

    for path, issues in results:
        console.print(f"[bold]{path}[/]")
        for issue in issues:
            if issue.severity == Severity.ERROR:
                badge = "[bold red]ERROR[/]"
            elif issue.severity == Severity.WARNING:
                badge = "[bold yellow]WARN [/]"
            else:
                badge = "[bold cyan]INFO [/]"
            console.print(f"  {badge} [bold]\\[{issue.field}][/] {issue.message}")
            if issue.suggestion is not None:
                console.print(f"         [dim]-> {issue.suggestion}[/]")
        console.print()

    if args.fix:
        path_replacements = apply_fixes(
            results,
            kb_root=kb_root,
            fix_paths=checked_map_data,
        )
        if path_replacements:
            targets = [path_replacements.get(p, p) for p in targets]
        remaining_errors = 0
        for p in targets:
            data, issues = audit_file(p, selected_checks=selected_checks)
            if args.skip_reviewed_errors:
                issues, _ = _skip_reviewed_errors(data, issues)
            remaining_errors += sum(1 for i in issues if i.severity == Severity.ERROR)
        if checked_map_data:
            map_results = audit_map_data_paths(
                targets,
                kb_root=kb_root,
                report_stale=report_stale_map_ids,
            )
            remaining_errors += sum(
                1
                for _, issues in map_results
                for issue in issues
                if issue.severity == Severity.ERROR
            )
        sys.exit(1 if remaining_errors else 0)

    sys.exit(1 if n_errors else 0)


if __name__ == "__main__":
    main()
