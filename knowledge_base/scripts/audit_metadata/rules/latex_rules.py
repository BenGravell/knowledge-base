"""LaTeX and plain-math cleanup helpers."""

import re

from knowledge_base.scripts.audit_metadata.rules.latex_data import (
    _DISPLAY_MATH_SPAN_RE,
    _INLINE_MATH_SPAN_RE,
    _LATEX_FRAC_RE,
    _LATEX_NAMED_SYMBOLS,
    _LATEX_SPACED_WORD_SYMBOLS,
    _PLAIN_LATEX_CAL_ARTIFACT_RE,
    _PLAIN_LATEX_ELL_ARTIFACT_RE,
    _PLAIN_LATEX_EMPH_ARTIFACT_RE,
    _PLAIN_LATEX_GREEK_IN_ARTIFACT_RE,
    _PLAIN_LATEX_LIMIT_INFINITY_ARTIFACT_RE,
    _PLAIN_LATEX_MATHBB_ARTIFACT_RE,
    _PLAIN_LATEX_MATHSCR_ARTIFACT_RE,
    _PLAIN_LATEX_STAR_ARTIFACT_RE,
    _PLAIN_LATEX_SUBSET_ARTIFACT_RE,
    _PLAIN_LATEX_TEXTIT_ARTIFACT_RE,
    _PLAIN_LATEX_VARIABLE_IN_ARTIFACT_RE,
    _PLAIN_LATEX_WIDETILDE_ARTIFACT_RE,
    _PLAIN_LATEX_WORD_OPERATOR_ARTIFACT_RE,
    _TEXT_LATEX_COMMAND_RE,
    _UNICODE_MATH_SYMBOLS,
)
from knowledge_base.scripts.audit_metadata.support.text import _normalize_inline_text


def _spaced_compact_exponent(exponent: str) -> str:
    exponent = exponent.strip()
    if re.fullmatch(r"[A-Za-z]{2}", exponent):
        return f"{exponent[0]} {exponent[1]}"
    return exponent


def _replace_latex_symbol_command(match: re.Match[str]) -> str:
    name = match.group("name")
    replacement = _LATEX_NAMED_SYMBOLS.get(name, name)
    if replacement in _LATEX_SPACED_WORD_SYMBOLS:
        return f" {replacement} "
    return replacement


def _plain_text_latex_math(math: str) -> str:
    text = math.strip().translate(_UNICODE_MATH_SYMBOLS)
    text = text.replace(r"\left", "")
    text = text.replace(r"\right", "")
    text = re.sub(r"\\[,;:! ]", " ", text)
    text = text.replace(r"\%", "%")
    text = text.replace(r"\times", "x")
    text = text.replace(r"\cdot", "*")
    text = re.sub(r"\\sqrt\{([^{}]+)\}", r"sqrt(\1)", text)

    while True:
        text, frac_count = _LATEX_FRAC_RE.subn(r"\1/\2", text)
        if not frac_count:
            break

    text = _TEXT_LATEX_COMMAND_RE.sub(r"\1", text)
    text = re.sub(
        r"\\(?P<name>[A-Za-z]+)(?![A-Za-z])",
        _replace_latex_symbol_command,
        text,
    )
    text = re.sub(
        r"\bO\(\s*([A-Za-z][A-Za-z0-9]*)\s*\^\s*\{\s*-1\s*/\s*2\s*\}\s*\)",
        r"O(1/sqrt(\1))",
        text,
    )

    def replace_exp_bound(match: re.Match[str]) -> str:
        exponent = _spaced_compact_exponent(match.group("exponent"))
        return f"O(exp(-{exponent}))"

    text = re.sub(
        r"\bO\(\s*e\s*\^\s*\{\s*-\s*(?P<exponent>[A-Za-z]{1,8})\s*\}\s*\)",
        replace_exp_bound,
        text,
    )

    def replace_exp(match: re.Match[str]) -> str:
        exponent = _spaced_compact_exponent(match.group("exponent"))
        return f"exp(-{exponent})"

    text = re.sub(
        r"\be\s*\^\s*\{\s*-\s*(?P<exponent>[A-Za-z]{1,8})\s*\}",
        replace_exp,
        text,
    )
    text = re.sub(r"\s*\^\s*\\?\*", "-star", text)
    text = re.sub(r"\{([^{}]+)\}", r"\1", text)
    text = re.sub(r"\b([A-Za-z])\^([A-Za-z]+)_([A-Za-z]+)\b", r"\1-\2-\3", text)
    text = re.sub(r"\^\s*(-?\d+(?:/\d+)?)", r"^(\1)", text)
    text = re.sub(r"\^\s*([A-Za-z][A-Za-z0-9]*)", r"^(\1)", text)
    text = re.sub(r"_\s*([A-Za-z0-9]+)", r"_\1", text)
    text = re.sub(r"\blim_([A-Za-z0-9]+)\s+to\s+", r"lim \1 to ", text)
    text = re.sub(r",\s*", ", ", text)
    text = re.sub(r"\s*([<>]=?|=|!=)\s*", r" \1 ", text)
    text = text.replace("< ~", "<~").replace("> ~", ">~")
    text = text.replace("\\", "")
    return re.sub(r"\s+", " ", text).strip()


def _tidy_plain_math_surrounding_text(text: str) -> str:
    text = re.sub(r"(?<=\d)(?=(?:mm|cm|km|kg|ms|Hz|kHz|MHz|GHz|m|s)\b)", " ", text)
    text = re.sub(r",\s*(?=\S)", ", ", text)
    text = re.sub(r"\b(in|to)\s*(?=[\[(])", r"\1 ", text)
    text = re.sub(r"\bnot\s+in\s*(?=[\[(])", "not in ", text)
    text = re.sub(r"\s+([,.;:])", r"\1", text)
    return _normalize_inline_text(text)


def _replace_dollar_math_in_text(text: str) -> tuple[str, int]:
    changed = 0

    def replace_math(match: re.Match[str]) -> str:
        nonlocal changed
        changed += 1
        return _plain_text_latex_math(match.group("math"))

    fixed = _DISPLAY_MATH_SPAN_RE.sub(replace_math, text)
    fixed = _INLINE_MATH_SPAN_RE.sub(replace_math, fixed)
    if changed:
        fixed = _tidy_plain_math_surrounding_text(fixed)
    return fixed, changed


def _plain_latex_math_artifact_count(text: str) -> int:
    return (
        len(_PLAIN_LATEX_ELL_ARTIFACT_RE.findall(text))
        + len(_PLAIN_LATEX_GREEK_IN_ARTIFACT_RE.findall(text))
        + len(_PLAIN_LATEX_VARIABLE_IN_ARTIFACT_RE.findall(text))
        + len(_PLAIN_LATEX_STAR_ARTIFACT_RE.findall(text))
        + len(_PLAIN_LATEX_LIMIT_INFINITY_ARTIFACT_RE.findall(text))
        + len(_PLAIN_LATEX_EMPH_ARTIFACT_RE.findall(text))
        + len(_PLAIN_LATEX_MATHSCR_ARTIFACT_RE.findall(text))
        + len(_PLAIN_LATEX_MATHBB_ARTIFACT_RE.findall(text))
        + len(_PLAIN_LATEX_SUBSET_ARTIFACT_RE.findall(text))
        + len(_PLAIN_LATEX_WORD_OPERATOR_ARTIFACT_RE.findall(text))
        + len(_PLAIN_LATEX_CAL_ARTIFACT_RE.findall(text))
        + len(_PLAIN_LATEX_WIDETILDE_ARTIFACT_RE.findall(text))
        + len(_PLAIN_LATEX_TEXTIT_ARTIFACT_RE.findall(text))
    )


def _replace_plain_latex_math_artifacts_in_text(text: str) -> tuple[str, int]:
    fixed = text
    changed = 0

    fixed, count = re.subn(r"\bell_([A-Za-z0-9]+)\b", r"l_\1", fixed)
    changed += count

    fixed, count = _PLAIN_LATEX_GREEK_IN_ARTIFACT_RE.subn(
        r"\g<var> in",
        fixed,
    )
    changed += count

    fixed, count = _PLAIN_LATEX_VARIABLE_IN_ARTIFACT_RE.subn(
        r"\g<var> in",
        fixed,
    )
    changed += count

    fixed, count = _PLAIN_LATEX_STAR_ARTIFACT_RE.subn(r"\g<var>-star", fixed)
    changed += count

    fixed, count = _PLAIN_LATEX_LIMIT_INFINITY_ARTIFACT_RE.subn(
        r"lim \g<var> to infinity \g<expr>",
        fixed,
    )
    changed += count

    def replace_emph_artifact(match: re.Match[str]) -> str:
        return match.group("braced") or match.group("command") or ""

    fixed, count = _PLAIN_LATEX_EMPH_ARTIFACT_RE.subn(
        replace_emph_artifact,
        fixed,
    )
    changed += count

    fixed, count = _PLAIN_LATEX_MATHSCR_ARTIFACT_RE.subn("", fixed)
    changed += count

    fixed, count = _PLAIN_LATEX_MATHBB_ARTIFACT_RE.subn("", fixed)
    changed += count

    fixed, count = _PLAIN_LATEX_SUBSET_ARTIFACT_RE.subn(" subset", fixed)
    changed += count

    fixed, count = re.subn(r"\btriangleq\b", "defined as", fixed)
    changed += count

    fixed, count = re.subn(r"\blesssim\b", "<~", fixed)
    changed += count

    fixed, count = re.subn(r"\bgtrsim\b", ">~", fixed)
    changed += count

    fixed, count = _PLAIN_LATEX_CAL_ARTIFACT_RE.subn(r"\g<symbol>", fixed)
    changed += count

    fixed, count = _PLAIN_LATEX_WIDETILDE_ARTIFACT_RE.subn(r"\g<symbol>~", fixed)
    changed += count

    fixed, count = _PLAIN_LATEX_TEXTIT_ARTIFACT_RE.subn(r"\g<word>", fixed)
    changed += count

    if changed:
        fixed = _tidy_plain_math_surrounding_text(fixed)
    return fixed, changed
