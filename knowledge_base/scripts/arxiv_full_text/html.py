"""Read arXiv HTML/ar5iv and convert it with Pandoc."""

from __future__ import annotations

import argparse
import re
import subprocess
import tempfile
from dataclasses import dataclass
from html import unescape
from pathlib import Path
from urllib.parse import quote

import requests

from knowledge_base.catalog import Entry
from knowledge_base.scripts.arxiv_full_text.settings import HTML_HEADERS
from knowledge_base.scripts.arxiv_full_text.text import (
    conversion_error,
    remove_rich_content_from_html,
    remove_rich_content_from_markdown,
)
from knowledge_base.utils.arxiv_utils import normalize_arxiv_id

UNUSABLE_HTML_MARKERS = (
    "Conversion to HTML had a Fatal error",
    "Conversion to HTML failed",
    "SubSection/",
)
ARXIV_ABS_URL_RE = re.compile(r"^https?://(?:www\.)?arxiv\.org/abs/", re.IGNORECASE)
ARXIV_ABS_PAGE_MARKERS = ("abs-outer", "submission-history", "View PDF")
HTML_TITLE_RE = re.compile(r"<title\b[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)


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


def normalized_title(title: str) -> str:
    return "".join(character for character in unescape(title).casefold() if character.isalnum())


def html_matches_title(html: str, expected_title: str) -> bool:
    match = HTML_TITLE_RE.search(html)
    if not match:
        return False
    actual = normalized_title(re.sub(r"<[^>]+>", "", match.group(1)))
    expected = normalized_title(expected_title)
    return bool(expected and expected in actual)


def usable_html(html: str, final_url: str = "", expected_title: str = "") -> bool:
    if final_url and ARXIV_ABS_URL_RE.match(final_url):
        return False
    if all(marker in html for marker in ARXIV_ABS_PAGE_MARKERS):
        return False
    if expected_title and not html_matches_title(html, expected_title):
        return False
    return not any(marker in html for marker in UNUSABLE_HTML_MARKERS)


def fetch_html(
    sources: list[HtmlSource], timeout: int, expected_title: str = ""
) -> tuple[HtmlSource, str] | tuple[None, str]:
    errors = []
    for source in sources:
        try:
            response = requests.get(source.url, headers=HTML_HEADERS, timeout=timeout)
        except requests.RequestException as exc:
            errors.append(f"{source.label}: {exc}")
            continue
        if response.status_code == 200 and "<html" in response.text[:2048].casefold():
            if not usable_html(response.text, response.url, expected_title):
                errors.append(f"{source.label}: unusable HTML")
                continue
            return source, response.text
        errors.append(f"{source.label}: HTTP {response.status_code}")
    return None, "; ".join(errors)


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
            capture_output=True,
            text=True,
        )
    return remove_rich_content_from_markdown(result.stdout)


def arxiv_html_markdown(entry: Entry, args: argparse.Namespace) -> tuple[str | None, str | None, str]:
    if not args.has_pandoc:
        return None, None, "pandoc not found"

    source, payload = fetch_html(arxiv_html_sources(entry.arxiv_id), args.timeout, entry.title)
    if source is None:
        return None, None, f"no-html: {payload}"
    try:
        return source.label, pandoc_convert(payload, args), ""
    except subprocess.CalledProcessError as exc:
        return None, None, f"pandoc: {conversion_error(exc)}"


def self_test() -> None:
    assert not usable_html("<html>Conversion to HTML had a Fatal error</html>")
    assert not usable_html("<html><main class='abs-outer'>submission-history View PDF</main></html>")
    assert not usable_html("<html><main>Paper body</main></html>", "https://arxiv.org/abs/1203.3538")
