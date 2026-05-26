"""Shared helpers for author/source normalization databases."""

from __future__ import annotations

import re
import unicodedata
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


def build_index(entries: list[dict[str, Any]], *, key_fn) -> NormalizationIndex:
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
