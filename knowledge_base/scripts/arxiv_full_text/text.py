"""Clean and validate converted paper text."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any

from knowledge_base.catalog import Entry, clean_embedding_sidecar_text
from knowledge_base.config import KB_DIR
from knowledge_base.scripts.arxiv_full_text.settings import MIN_BODY_CHARS, SIDECAR_NAME
from knowledge_base.utils.arxiv_utils import normalize_arxiv_id

IMAGE_MARKDOWN_RE = re.compile(r"!\[[^\]]*]\([^)]*\)")
HTML_IMAGE_RE = re.compile(r"<(?:img|source)\b[^>]*>", re.IGNORECASE)
HTML_PICTURE_RE = re.compile(r"<picture\b.*?</picture>", re.IGNORECASE | re.DOTALL)
HTML_FIGURE_IMAGE_RE = re.compile(r"<figure\b([^>]*)>\s*<img\b[^>]*>(.*?)</figure>", re.IGNORECASE | re.DOTALL)
MARKDOWN_ATTR_RE = re.compile(r"\{[#.][^}\n]*\}")
LATEXML_FOOTER_RE = re.compile(r"^Generated on .*?LaTeXML.*$", re.MULTILINE)
LOCAL_MARKDOWN_LINK_RE = re.compile(r"\[([^]]*)]\((?:#[^)]+|/[^)]*)\)")
EMPTY_MARKDOWN_LINK_RE = re.compile(r"\[]\([^)]+\)")
HTML_TAG_RE = re.compile(r"</?[A-Za-z][A-Za-z0-9:-]*(?:\s[^>]*)?>")
BLANK_LINES_RE = re.compile(r"\n{3,}")
DISPLAY_MATH_RE = re.compile(r"(?<!\\)\$\$")
SIDECAR_MARKER = "arxiv-full-text:v1"
SIDECAR_MARKER_RE = re.compile(r"^<!--\s*arxiv-full-text:v1\s+(\{.*\})\s*-->\s*$")
NON_BODY_HEADING_RE = re.compile(
    r"^(?:"
    r"abstract|title:|authors?:|quick links|submission history|access paper|current browse context|"
    r"subjects?:|comments?:|journal reference|report number|cite as|view a pdf|"
    r"arxiv-issued doi|computer science\b|mathematics\b|physics\b|statistics\b|"
    r"electrical engineering and systems science\b|economics\b|quantitative biology\b|"
    r"quantitative finance\b"
    r")",
    re.IGNORECASE,
)


def embed_text_path(entry: Entry) -> Path:
    return entry.metadata_path.with_name(SIDECAR_NAME)


def sidecar_provenance(entry: Entry, source_label: str) -> str:
    return json.dumps(
        {
            "arxiv_id": entry.arxiv_id,
            "source": source_label,
        },
        ensure_ascii=False,
        sort_keys=True,
    )


def sidecar_header(entry: Entry, source_label: str) -> str:
    return f"<!-- {SIDECAR_MARKER} {sidecar_provenance(entry, source_label)} -->"


def parsed_sidecar_provenance(text: str) -> dict[str, Any] | None:
    first_line = next((line.strip() for line in text.splitlines() if line.strip()), "")
    match = SIDECAR_MARKER_RE.match(first_line)
    if not match:
        return None
    try:
        raw = json.loads(match.group(1))
    except json.JSONDecodeError:
        return None
    return raw if isinstance(raw, dict) else None


def sidecar_current_for_entry(entry: Entry, path: Path) -> bool:
    if not path.exists():
        return False
    provenance = parsed_sidecar_provenance(path.read_text(encoding="utf-8"))
    if provenance is None:
        return True
    return normalize_arxiv_id(str(provenance.get("arxiv_id") or "")) == entry.arxiv_id


def remove_rich_content_from_html(html: str) -> str:
    html = HTML_FIGURE_IMAGE_RE.sub(r"<figure\1>\2</figure>", html)
    html = HTML_PICTURE_RE.sub("", html)
    return HTML_IMAGE_RE.sub("", html)


def strip_source_footer(markdown: str) -> str:
    markers = (
        r"\n\s*◄",
        r"\nExperimental support, please\b",
        r"\n## Instructions for reporting errors\b",
        r"\n#+\s*SECOND LEVEL HEADING\b",
        r"\n#+\s*CITATIONS, FIGURES, REFERENCES\b",
        r"\n#+\s*Citations in Text\b",
        r"\nSample Figure Caption\b",
    )
    return re.split("|".join(markers), markdown, maxsplit=1)[0]


def remove_rich_content_from_markdown(markdown: str) -> str:
    markdown = IMAGE_MARKDOWN_RE.sub("", markdown)
    markdown = HTML_IMAGE_RE.sub("", markdown)
    markdown = MARKDOWN_ATTR_RE.sub("", markdown)
    markdown = LATEXML_FOOTER_RE.sub("", markdown)
    markdown = strip_source_footer(markdown)
    markdown = LOCAL_MARKDOWN_LINK_RE.sub(r"\1", markdown)
    markdown = EMPTY_MARKDOWN_LINK_RE.sub("", markdown)
    markdown = HTML_TAG_RE.sub("", markdown)
    return BLANK_LINES_RE.sub("\n\n", markdown).strip()


def readable_markdown_chars(markdown: str) -> int:
    text = re.sub(r"`{1,3}[^`]*`{1,3}", "", markdown)
    text = re.sub(r"\[[^]]*]\([^)]*\)", "", text)
    text = re.sub(r"[#*_>{}\[\]()`~\\|:-]", "", text)
    return len(re.sub(r"\s+", "", text))


def has_balanced_display_math(markdown: str) -> bool:
    return len(DISPLAY_MATH_RE.findall(markdown)) % 2 == 0


def rejects_unbalanced_display_math(source_label: str, markdown: str) -> bool:
    return source_label == "arxiv-latex" and not has_balanced_display_math(markdown)


def normalized_heading(text: str) -> str:
    text = re.sub(r"^#+", "", text).strip()
    return re.sub(r"\s+", " ", text).casefold()


def remove_duplicate_title(markdown: str, title: str) -> str:
    lines = markdown.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and lines[0].startswith("# ") and normalized_heading(lines[0]) == normalized_heading(title):
        lines = lines[1:]
    return "\n".join(lines).lstrip()


def body_after_duplicate_title(markdown: str, title: str) -> str:
    lines = markdown.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("# ") and normalized_heading(line) == normalized_heading(title):
            return "\n".join(lines[index + 1 :]).lstrip()
    return markdown


def sidecar_markdown(entry: Entry, markdown: str) -> str:
    title = re.sub(r"\s+", " ", entry.title or entry.title_label or entry.id).strip()
    markdown = remove_rich_content_from_markdown(body_after_duplicate_title(markdown, title))
    return f"{clean_embedding_sidecar_text(markdown)}\n"


def paper_body_markdown(markdown: str) -> str:
    body: list[str] = []
    keep = False
    for line in markdown.splitlines():
        if line.startswith("#"):
            heading = normalized_heading(line).strip(": ")
            keep = bool(heading and not NON_BODY_HEADING_RE.match(heading))
        if keep:
            body.append(line)
    return "\n".join(body)


def has_paper_body(markdown: str, min_chars: int = MIN_BODY_CHARS) -> bool:
    body = paper_body_markdown(markdown)
    if not body and not any(line.startswith("#") for line in markdown.splitlines()):
        body = markdown
    return readable_markdown_chars(body) >= min_chars


def usable_sidecar(entry: Entry, markdown: str, source_label: str, args: argparse.Namespace) -> tuple[str | None, str]:
    sidecar = sidecar_markdown(entry, markdown)
    if rejects_unbalanced_display_math(source_label, sidecar):
        return None, "unbalanced-math"
    if not has_paper_body(sidecar):
        return None, "no-body"
    if readable_markdown_chars(sidecar) < args.min_chars:
        return None, "too-short"
    return sidecar, ""


def write_sidecar(path: Path, text: str, dry_run: bool) -> None:
    if dry_run:
        return
    path.write_text(text, encoding="utf-8")


def display_path(path: Path) -> Path:
    try:
        return path.relative_to(KB_DIR)
    except ValueError:
        return path


def write_converted_sidecar(
    entry: Entry, path: Path, markdown: str, source_label: str, args: argparse.Namespace
) -> str:
    sidecar, reason = usable_sidecar(entry, markdown, source_label, args)
    if sidecar is None:
        return f"skip {reason} {entry.id}: {source_label}"

    write_sidecar(path, f"{sidecar_header(entry, source_label)}\n\n{sidecar}", args.dry_run)
    action = "would write" if args.dry_run else "wrote"
    return f"{action} {display_path(path)} from {source_label}"


def wrote(message: str) -> bool:
    return message.startswith(("wrote ", "would write "))


def conversion_error(exc: BaseException) -> str:
    if isinstance(exc, subprocess.CalledProcessError):
        lines = (exc.stderr or exc.stdout or str(exc)).strip().splitlines()
        return lines[-1] if lines else str(exc)
    return str(exc)


def self_test() -> None:
    assert remove_rich_content_from_html("<figure><img src='x'><figcaption>Figure 1</figcaption></figure>")
    assert "img" not in remove_rich_content_from_markdown("before ![x](http://example.test/x.png) after")
    assert "{.ltx_ref}" not in remove_rich_content_from_markdown("[1](#bib){.ltx_ref}")
    assert remove_rich_content_from_markdown("[1](#bib) [home](/)") == "1 home"
    assert remove_rich_content_from_markdown("<figcaption>Caption</figcaption>") == "Caption"
    assert has_balanced_display_math("before $$x$$ after")
    assert not has_balanced_display_math("before $$x after")
    assert rejects_unbalanced_display_math("arxiv-latex", "before $$x after")
    assert not rejects_unbalanced_display_math("ar5iv", "before $$x after")
    assert "Feeling" not in remove_rich_content_from_markdown("Body\n\n◄ Feeling\\\nlucky?")
    assert "Toggle ar5iv" not in strip_source_footer('Body\n\n  ◄  Feeling\\\nlucky?\n\n "Toggle ar5iv color scheme")')
    assert "reporting errors" not in strip_source_footer("Body\n\n## Instructions for reporting errors\nNope")
    assert "view the build logs" not in strip_source_footer("Body\n\nExperimental support, please view the build logs")
    assert "Sample Figure Caption" not in strip_source_footer("Body\n\n### SECOND LEVEL HEADING\nSample Figure Caption")
    assert remove_duplicate_title("# Same\n\nBody", "Same") == "Body"
    assert body_after_duplicate_title("UI\n\n# Same\n\nBody", "Same") == "Body"
    assert not has_paper_body(
        "## Abstract\n\nOnly abstract text.\n\n## Submission history\n\nNo paper body.", min_chars=20
    )
    assert has_paper_body(
        "## Abstract\n\nOnly abstract text.\n\n## Introduction\n\nThis section contains enough paper body words.",
        min_chars=20,
    )
    cleaned = clean_embedding_sidecar_text(
        "# Paper\n\n- arXiv ID: [x](https://arxiv.org/abs/x)\n- HTML source: [ar5iv](https://ar5iv.test)\n\n"
        "Alice Example University\n\n###### Abstract\n\nUseful idea [12].\n\n"
        "## 1 Introduction\n\nThe method solves the real problem (Smith, 2020).\n\n"
        "### A) Model Details\n\nDetails stay readable.\n\n"
        "  -- -------- --\n noisy 123 456\n\n## References\n\n[1] Noise"
    )
    assert "Alice Example" not in cleaned
    assert "References" not in cleaned
    assert "Smith" not in cleaned
    assert "## Introduction" in cleaned
    assert "### Model Details" in cleaned
    assert "### A)" not in cleaned
    assert "The method solves the real problem" in cleaned
    assert clean_embedding_sidecar_text("First useful paragraph.\n\nSecond useful paragraph.").startswith(
        "## Paper Body"
    )
    assert "extra proof" not in clean_embedding_sidecar_text(
        "## Introduction\n\nMain idea.\n\n## Appendix A\n\nextra proof"
    )
    assert readable_markdown_chars("# A\n\nSome real words.") > 10
    assert has_paper_body("A headingless conversion can still contain enough real paper body words.", min_chars=20)
    assert parsed_sidecar_provenance('<!-- arxiv-full-text:v1 {"arxiv_id":"2401.00001"} -->') == {
        "arxiv_id": "2401.00001"
    }
