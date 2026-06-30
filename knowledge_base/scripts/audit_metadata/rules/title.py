"""Title casing helpers for paper metadata."""

import re

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
        and (first_alpha == first_alpha.upper() or first_alpha[0].isupper() or _is_intentional_mixed_case(first_alpha))
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
        elif (
            _is_scientific_binomial_epithet(previous_core, core)
            or _is_lowercase_leading_label(core, tail, is_first)
            or _is_identifier_like_hyphenated_core(core)
        ):
            result.append(word)
        elif "-" in core:
            # Hyphenated compound: case the first part normally; preserve
            # existing case on subsequent parts (e.g. "Sampling-based" stays
            # "Sampling-based", not "Sampling-Based").
            parts = core.split("-")
            cased_parts = [_case_token(parts[0], force), *parts[1:]]
            result.append(lead + "-".join(cased_parts) + tail)
        else:
            result.append(_case_token(word, force))
        previous_core = core

    return " ".join(result)


def is_title_case(title: str) -> bool:
    return title == to_title_case(title)
