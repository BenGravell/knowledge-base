"""Convert arXiv LaTeX sources and PDFs through Docling."""

from __future__ import annotations

import argparse
import gzip
import io
import os
import re
import subprocess
import tarfile
import tempfile
from contextlib import suppress
from pathlib import Path
from urllib.parse import quote

import requests

from knowledge_base.catalog import Entry
from knowledge_base.config import REPO_ROOT
from knowledge_base.scripts.arxiv_full_text.settings import HTML_HEADERS
from knowledge_base.scripts.arxiv_full_text.text import conversion_error, remove_rich_content_from_markdown
from knowledge_base.utils.arxiv_utils import arxiv_pdf_url, normalize_arxiv_id

LATEX_INCLUDE_RE = re.compile(r"\\(?:input|include)\*?\s*\{([^}]+)\}")
LATEX_BAD_ROOT_RE = re.compile(
    r"cover letter|reply to referees|response to reviewers|detailed reply|comments to the authors|resubmission",
    re.IGNORECASE,
)


def docling_env() -> dict[str, str]:
    env = os.environ.copy()
    cache_root = REPO_ROOT / ".cache" / "huggingface"
    cache_root.mkdir(parents=True, exist_ok=True)
    env.setdefault("HF_HOME", str(cache_root))
    env.setdefault("HUGGINGFACE_HUB_CACHE", str(cache_root / "hub"))
    return env


def docling_convert(source: str | Path, input_format: str, args: argparse.Namespace) -> str:
    with tempfile.TemporaryDirectory(prefix=f"kb-docling-{input_format}-") as tmp:
        output_dir = Path(tmp)
        command = [
            args.docling,
            "convert",
            "--from",
            input_format,
            "--to",
            "md",
            "--image-export-mode",
            "placeholder",
            "--output",
            str(output_dir),
            str(source),
        ]
        if args.docling_device:
            command.extend(["--device", args.docling_device])
        if args.docling_timeout:
            command.extend(["--document-timeout", str(args.docling_timeout)])

        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            env=docling_env(),
            text=True,
            timeout=(args.docling_timeout + 30) if args.docling_timeout else None,
        )
        markdown_paths = sorted(output_dir.rglob("*.md"), key=lambda path: path.stat().st_size, reverse=True)
        if markdown_paths:
            return remove_rich_content_from_markdown(markdown_paths[0].read_text(encoding="utf-8"))
        if result.stdout.strip():
            return remove_rich_content_from_markdown(result.stdout)
    raise RuntimeError(f"Docling did not produce markdown for {source}")


def docling_markdown(
    label: str, source: str | Path, input_format: str, args: argparse.Namespace
) -> tuple[str | None, str]:
    try:
        return docling_convert(source, input_format, args), ""
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, RuntimeError) as exc:
        return None, f"{label}: {conversion_error(exc)}"


def arxiv_eprint_url(arxiv_id: str) -> str:
    encoded = quote(normalize_arxiv_id(arxiv_id), safe="/")
    return f"https://arxiv.org/e-print/{encoded}"


def latex_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def latex_title(text: str) -> str:
    match = re.search(r"\\title(?:\[[^]]*])?\{([^{}]+)", text, re.DOTALL)
    return re.sub(r"\s+", " ", match.group(1)).strip() if match else ""


def latex_root_score(path: Path) -> tuple[bool, bool, bool, bool, int, int, int]:
    text = latex_text(path)
    bad_root = LATEX_BAD_ROOT_RE.search(path.name) or LATEX_BAD_ROOT_RE.search(latex_title(text))
    return (
        not bool(bad_root),
        r"\documentclass" in text,
        r"\begin{document}" in text,
        r"\begin{abstract}" in text,
        len(LATEX_INCLUDE_RE.findall(text)),
        -len(path.relative_to(path.anchor).parts),
        path.stat().st_size,
    )


def choose_latex_root(paths: list[Path]) -> Path | None:
    candidates = []
    for path in paths:
        try:
            score = latex_root_score(path)
        except OSError:
            continue
        candidates.append((score, path))
    return max(candidates)[1] if candidates else None


def latex_include_path(source_path: Path, include_name: str) -> Path | None:
    candidate = (source_path.parent / include_name).with_suffix(Path(include_name).suffix or ".tex")
    return candidate if candidate.is_file() else None


def inline_latex_inputs(source_path: Path, seen: set[Path] | None = None) -> str:
    seen = seen or set()
    resolved = source_path.resolve()
    if resolved in seen:
        return ""
    seen.add(resolved)

    def replace(match: re.Match[str]) -> str:
        include_path = latex_include_path(source_path, match.group(1).strip())
        if include_path is None:
            return match.group(0)
        return inline_latex_inputs(include_path, seen)

    return LATEX_INCLUDE_RE.sub(replace, latex_text(source_path))


def flattened_latex_source(source_path: Path, work_dir: Path) -> Path:
    flattened_path = work_dir / f"{source_path.stem}-flattened.tex"
    flattened_path.write_text(inline_latex_inputs(source_path), encoding="utf-8")
    return flattened_path


def arxiv_latex_root(arxiv_id: str, args: argparse.Namespace, work_dir: Path) -> tuple[Path | None, str]:
    try:
        response = requests.get(arxiv_eprint_url(arxiv_id), headers=HTML_HEADERS, timeout=args.timeout)
        response.raise_for_status()
    except requests.RequestException as exc:
        return None, f"arxiv-latex: {exc}"

    content = response.content
    source_dir = work_dir / "source"
    source_dir.mkdir()
    try:
        with tarfile.open(fileobj=io.BytesIO(content), mode="r:*") as archive:
            archive.extractall(source_dir, filter="data")
    except tarfile.TarError:
        with suppress(gzip.BadGzipFile):
            content = gzip.decompress(content)
        text = content.decode("utf-8", errors="ignore")
        if r"\documentclass" not in text and r"\begin{document}" not in text:
            return None, "arxiv-latex: no TeX source"
        source_path = source_dir / "source.tex"
        source_path.write_text(text, encoding="utf-8")
        return source_path, ""

    source_path = choose_latex_root(list(source_dir.rglob("*.tex")))
    if source_path is None:
        return None, "arxiv-latex: no TeX source"
    return source_path, ""


def arxiv_latex_markdown(entry: Entry, args: argparse.Namespace) -> tuple[str | None, str]:
    with tempfile.TemporaryDirectory(prefix="kb-arxiv-latex-") as tmp:
        work_dir = Path(tmp)
        source_path, message = arxiv_latex_root(entry.arxiv_id, args, work_dir)
        if source_path is None:
            return None, message
        return docling_markdown("arxiv-latex", flattened_latex_source(source_path, work_dir), "latex", args)


def arxiv_pdf_markdown(entry: Entry, args: argparse.Namespace) -> tuple[str | None, str]:
    return docling_markdown("arxiv-pdf", arxiv_pdf_url(entry.arxiv_id), "pdf", args)


def self_test() -> None:
    with tempfile.TemporaryDirectory(prefix="kb-arxiv-latex-test-") as tmp:
        root = Path(tmp) / "main.tex"
        child = Path(tmp) / "section.tex"
        reply = Path(tmp) / "reply.tex"
        root.write_text(
            r"\documentclass{article}\title{Real Paper}\begin{document}\input{section}\end{document}",
            encoding="utf-8",
        )
        child.write_text(r"\section{Body} Included text.", encoding="utf-8")
        reply.write_text(
            r"\documentclass{article}\title{Cover Letter for our Resubmission}\begin{document}Nope\end{document}"
            + ("x" * 200),
            encoding="utf-8",
        )
        assert choose_latex_root([reply, root]) == root
        assert r"\section{Body} Included text." in inline_latex_inputs(root)
