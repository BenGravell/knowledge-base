"""arXiv ID and expected metadata slug helpers."""

import re
import unicodedata

# arXiv ID patterns (version suffix optional)
_ARXIV_NEW_RE = re.compile(r"^\d{4}\.\d{4,5}(v\d+)?$")  # e.g. 2401.09241
_ARXIV_OLD_RE = re.compile(  # e.g. math.CO/0701001
    r"^[a-z]+(-[a-z]+)?(\.[A-Z]{2})?/\d{7}(v\d+)?$"
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

# ---------------------------------------------------------------------------
# arXiv helpers
# ---------------------------------------------------------------------------


def is_valid_arxiv_id(arxiv_id: str) -> bool:
    return bool(_ARXIV_NEW_RE.match(arxiv_id) or _ARXIV_OLD_RE.match(arxiv_id))


def strip_arxiv_version(arxiv_id: str) -> str:
    return re.sub(r"v\d+$", "", arxiv_id)


# ---------------------------------------------------------------------------
# Slug helpers
# ---------------------------------------------------------------------------


def _normalize_slug_separators(text: str) -> str:
    """Preserve Unicode dash word breaks before ASCII folding removes them."""
    return "".join("-" if unicodedata.category(ch) == "Pd" or ch == "\N{MINUS SIGN}" else ch for ch in text)


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
    last_name = _slugify(_collapse_intra_word_apostrophes(_extract_last_name(first_author)))
    # First four slug-bearing words of title; punctuation separates words except
    # inside dotted terms such as C4.5.
    title_tokens = _title_slug_tokens(title)[:4]
    title_part = "_".join(title_tokens)
    return f"{year}.{last_name}.{title_part}"
