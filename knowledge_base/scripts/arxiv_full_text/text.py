"""Clean and validate converted paper text."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

from knowledge_base.catalog import Entry, clean_embedding_sidecar_text
from knowledge_base.config import KB_DIR
from knowledge_base.scripts.arxiv_full_text.settings import MIN_BODY_CHARS, SIDECAR_NAME

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


def remove_rich_content_from_html(html: str) -> str:
    html = HTML_FIGURE_IMAGE_RE.sub(r"<figure\1>\2</figure>", html)
    html = HTML_PICTURE_RE.sub("", html)
    return HTML_IMAGE_RE.sub("", html)


def strip_source_footer(markdown: str) -> str:
    markers = (
        r"\n\s*◄",
        r"\nExperimental support, please\b",
        r"\n## Instructions for reporting errors\b",
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


def usable_sidecar(entry: Entry, markdown: str, args: argparse.Namespace) -> tuple[str | None, str]:
    sidecar = sidecar_markdown(entry, markdown)
    if not has_paper_body(sidecar):
        return None, "no-body"
    if readable_markdown_chars(sidecar) < args.min_chars:
        return None, "too-short"
    return sidecar, ""


def write_sidecar(path: Path, text: str, dry_run: bool) -> None:
    if dry_run:
        return
    path.write_text(text, encoding="utf-8")


def write_converted_sidecar(
    entry: Entry, path: Path, markdown: str, source_label: str, args: argparse.Namespace
) -> str:
    sidecar, reason = usable_sidecar(entry, markdown, args)
    if sidecar is None:
        return f"skip {reason} {entry.id}: {source_label}"

    write_sidecar(path, sidecar, args.dry_run)
    action = "would write" if args.dry_run else "wrote"
    return f"{action} {path.relative_to(KB_DIR)} from {source_label}"


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
    assert "Feeling" not in remove_rich_content_from_markdown("Body\n\n◄ Feeling\\\nlucky?")
    assert "Toggle ar5iv" not in strip_source_footer('Body\n\n  ◄  Feeling\\\nlucky?\n\n "Toggle ar5iv color scheme")')
    assert "reporting errors" not in strip_source_footer("Body\n\n## Instructions for reporting errors\nNope")
    assert "view the build logs" not in strip_source_footer("Body\n\nExperimental support, please view the build logs")
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
