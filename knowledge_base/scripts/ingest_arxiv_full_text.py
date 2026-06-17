"""Convert available arXiv HTML pages into public Markdown sidecars."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

import requests

from knowledge_base.catalog import Catalog, Entry
from knowledge_base.config import KB_DIR
from knowledge_base.utils.arxiv_utils import ARXIV_HEADERS, normalize_arxiv_id

METADATA_ROOT = KB_DIR / "docs" / "papers"
SIDECAR_NAME = "full_text.md"
DEFAULT_SLEEP_SECONDS = 3.0
MIN_MARKDOWN_CHARS = 1_000

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

HTML_HEADERS = {
    **ARXIV_HEADERS,
    "Accept": "text/html,application/xhtml+xml;q=0.9,*/*;q=0.8",
    "User-Agent": ARXIV_HEADERS["User-Agent"].replace("prefill", "full-text-ingest"),
}


@dataclass(frozen=True, slots=True)
class HtmlSource:
    label: str
    url: str


def arxiv_html_sources(arxiv_id: str) -> list[HtmlSource]:
    encoded = quote(normalize_arxiv_id(arxiv_id), safe="/")
    return [
        HtmlSource("arxiv-html", f"https://arxiv.org/html/{encoded}"),
        HtmlSource("ar5iv", f"https://ar5iv.labs.arxiv.org/html/{encoded}"),
    ]


def full_text_path(entry: Entry) -> Path:
    return entry.metadata_path.with_name(SIDECAR_NAME)


def candidates(catalog: Catalog, requested_ids: list[str]) -> list[Entry]:
    requested = {normalize_arxiv_id(arxiv_id) for arxiv_id in requested_ids}
    entries = [entry for entry in catalog.entries if entry.arxiv_id]
    if requested:
        entries = [entry for entry in entries if entry.arxiv_id in requested]
    return entries


def fetch_html(sources: list[HtmlSource], timeout: int) -> tuple[HtmlSource, str] | tuple[None, str]:
    errors = []
    for source in sources:
        try:
            response = requests.get(source.url, headers=HTML_HEADERS, timeout=timeout)
        except requests.RequestException as exc:
            errors.append(f"{source.label}: {exc}")
            continue
        if response.status_code == 200 and "<html" in response.text[:2048].casefold():
            return source, response.text
        errors.append(f"{source.label}: HTTP {response.status_code}")
    return None, "; ".join(errors)


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


def pandoc_convert(html: str, args: argparse.Namespace) -> str:
    with tempfile.TemporaryDirectory(prefix="kb-arxiv-html-") as tmp:
        input_path = Path(tmp) / "paper.html"
        input_path.write_text(remove_rich_content_from_html(html), encoding="utf-8")
        command = [
            args.pandoc,
            "--from",
            "html-native_divs-native_spans+tex_math_dollars+tex_math_single_backslash+tex_math_double_backslash",
            "--to",
            "markdown+tex_math_dollars+tex_math_single_backslash+tex_math_double_backslash",
            "--markdown-headings=atx",
            "--wrap=none",
        ]
        if args.pandoc_data_dir:
            command.extend(["--data-dir", args.pandoc_data_dir])
        command.append(str(input_path))
        result = subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    return remove_rich_content_from_markdown(result.stdout)


def sidecar_markdown(entry: Entry, source: HtmlSource, markdown: str) -> str:
    title = re.sub(r"\s+", " ", entry.title or entry.title_label or entry.id).strip()
    markdown = remove_rich_content_from_markdown(body_after_duplicate_title(markdown, title))
    return (
        f"# {title}\n\n"
        f"- arXiv ID: [{entry.arxiv_id}](https://arxiv.org/abs/{quote(entry.arxiv_id, safe='/')})\n"
        f"- HTML source: [{source.label}]({source.url})\n\n"
        f"{markdown}\n"
    )


def write_sidecar(path: Path, text: str, dry_run: bool) -> None:
    if dry_run:
        return
    path.write_text(text, encoding="utf-8")


def process_entry(entry: Entry, args: argparse.Namespace) -> str:
    path = full_text_path(entry)
    if path.exists() and not args.force:
        return f"skip existing {entry.id}"

    source, payload = fetch_html(arxiv_html_sources(entry.arxiv_id), args.timeout)
    if source is None:
        return f"skip no-html {entry.id}: {payload}"

    try:
        markdown = pandoc_convert(payload, args)
    except subprocess.CalledProcessError as exc:
        message = (exc.stderr or exc.stdout or str(exc)).strip().splitlines()
        return f"skip pandoc {entry.id}: {message[-1] if message else exc}"

    if readable_markdown_chars(markdown) < args.min_chars:
        return f"skip too-short {entry.id}: {source.label}"

    write_sidecar(path, sidecar_markdown(entry, source, markdown), args.dry_run)
    action = "would write" if args.dry_run else "wrote"
    return f"{action} {path.relative_to(KB_DIR)} from {source.label}"


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
    assert readable_markdown_chars("# A\n\nSome real words.") > 10


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", action="append", default=[], help="Only process this arXiv ID. Repeatable.")
    parser.add_argument("--limit", type=int, default=0, help="Maximum candidate entries to process.")
    parser.add_argument("--force", action="store_true", help=f"Overwrite existing {SIDECAR_NAME} files.")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and convert, but do not write files.")
    parser.add_argument("--sleep", type=float, default=DEFAULT_SLEEP_SECONDS, help="Delay between entries.")
    parser.add_argument("--timeout", type=int, default=60, help="HTTP timeout in seconds.")
    parser.add_argument("--min-chars", type=int, default=MIN_MARKDOWN_CHARS, help="Minimum readable output size.")
    parser.add_argument("--pandoc", default="pandoc", help="Pandoc executable.")
    parser.add_argument("--pandoc-data-dir", default="", help="Optional Pandoc data directory.")
    parser.add_argument("--self-test", action="store_true", help="Run lightweight internal assertions and exit.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.self_test:
        self_test()
        return 0

    if not shutil.which(args.pandoc):
        raise SystemExit(f"Pandoc executable not found: {args.pandoc}")

    catalog = Catalog.from_metadata_root(METADATA_ROOT)
    entries = candidates(catalog, args.id)
    if args.limit:
        entries = entries[: args.limit]

    for index, entry in enumerate(entries):
        print(process_entry(entry, args))
        if args.sleep and index < len(entries) - 1:
            time.sleep(args.sleep)
    print(f"processed {len(entries)} candidate(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
