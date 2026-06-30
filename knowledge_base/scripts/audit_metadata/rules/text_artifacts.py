"""Misspelling and OCR artifact constants."""

import re

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
_COMMON_MISSPELLING_CORRECTIONS = {typo.casefold(): correction for typo, correction in _COMMON_MISSPELLINGS.items()}
_COMMON_MISSPELLING_RE = re.compile(
    r"(?<![A-Za-z])("
    + "|".join(re.escape(typo.casefold()) for typo in sorted(_COMMON_MISSPELLINGS, key=len, reverse=True))
    + r")(?![A-Za-z])"
)
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
_HIGH_CONFIDENCE_OCR_ARTIFACT_ISSUE_PREFIX = "Contains high-confidence OCR artifact(s):"
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
_VALID_HYPHENATED_OCR_SPLITS = {
    ("nonconvex", 3),  # non-convex is a standard alternate spelling.
}
_OCR_SPLIT_RE = re.compile(
    r"\b(?:"
    + "|".join(
        re.escape(word[:split_at]) + r"(?:\s+|-\s*)" + re.escape(word[split_at:])
        for word in sorted(_OCR_SPLIT_WORDS)
        for split_at in range(3, len(word) - 2)
    )
    + r")\b",
    re.I,
)
_OCR_SPLIT_PARTS_RE = re.compile(r"^(?P<head>[A-Za-z]+)(?P<sep>\s+|-\s*)(?P<tail>[A-Za-z]+)$", re.I)


_LINEBREAK_HYPHEN_RE = re.compile(r"\b(?P<head>[A-Za-z]{3,})-\s+(?P<tail>[A-Za-z]{3,})\b")
_SUSPENDED_HYPHEN_JOINERS = {"and", "nor", "or"}

__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
