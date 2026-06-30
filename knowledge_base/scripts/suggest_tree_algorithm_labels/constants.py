"""Constants for tree algorithm label suggestions."""

import re

ACTION_UPDATE_TREE = "update-tree-label"
ACTION_UPDATE_METADATA = "update-metadata-algorithm"
ACTION_ACCEPT_ALIAS = "accept-alias"
ACTION_REVIEW = "review"
ACTIONS = (
    ACTION_UPDATE_TREE,
    ACTION_UPDATE_METADATA,
    ACTION_ACCEPT_ALIAS,
    ACTION_REVIEW,
)

CONFIDENCE_HIGH = "high"
CONFIDENCE_MEDIUM = "medium"
CONFIDENCE_LOW = "low"
CONFIDENCES = (CONFIDENCE_HIGH, CONFIDENCE_MEDIUM, CONFIDENCE_LOW)
CONFIDENCE_RANK = {
    CONFIDENCE_LOW: 0,
    CONFIDENCE_MEDIUM: 1,
    CONFIDENCE_HIGH: 2,
}

WORD_RE = re.compile(r"[A-Za-z0-9]+")

STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "by",
    "for",
    "from",
    "in",
    "into",
    "is",
    "of",
    "on",
    "or",
    "the",
    "to",
    "toward",
    "towards",
    "using",
    "via",
    "with",
}

TYPE_WORDS = {
    "algorithm",
    "algorithms",
    "approach",
    "approaches",
    "framework",
    "frameworks",
    "method",
    "methods",
    "model",
    "models",
    "rule",
    "rules",
    "scheme",
    "schemes",
    "technique",
    "techniques",
    "theorem",
    "theorems",
}

GENERIC_ALGORITHM_LABELS = {
    "algorithm",
    "algorithms",
    "analysis",
    "control",
    "learning",
    "method",
    "methods",
    "model",
    "optimization",
    "planning",
}

ROMAN_PART_LABELS = {"i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"}

__all__ = [name for name in globals() if name.isupper()]
