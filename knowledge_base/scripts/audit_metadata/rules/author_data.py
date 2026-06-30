"""Author audit and repair constants."""

import re

_AUTHOR_SUFFIX_RE = re.compile(
    r"^(?:" r"Jr\.?|Sr\.?|" r"I{2,3}|IV|V|VI{0,3}|IX|X|" r"Ph\.?D\.?|M\.?D\.?|DPhil|Esq\.?" r")$",
    re.I,
)

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

_KNOWN_SINGLE_AUTHOR_REPLACEMENTS = {
    "IEEE": "IEEE Standards Association",
    "Lozano-Perez": "Tomas Lozano-Perez",
}

__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
