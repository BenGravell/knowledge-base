"""Metadata file discovery and update operations."""

from __future__ import annotations

from pathlib import Path

from knowledge_base.scripts.enrich_existing_arxiv_metadata.algorithm_rules import (
    GENERIC_ALGORITHMS,
    algorithm_like,
    infer_algorithm,
)
from knowledge_base.scripts.enrich_existing_arxiv_metadata.constants import PAPERS_ROOT
from knowledge_base.scripts.enrich_existing_arxiv_metadata.tag_rules import build_tags
from knowledge_base.scripts.enrich_existing_arxiv_metadata.text import bare_arxiv_id, title_case_ascii
from knowledge_base.scripts.enrich_existing_arxiv_metadata.yaml_io import dump_yaml, load_yaml, replace_scalar_field
from knowledge_base.utils.arxiv_utils import (
    ArxivRecord,
    arxiv_abs_url,
    arxiv_html_url,
    arxiv_pdf_url,
    normalize_arxiv_id,
)


def target_files(refresh_derived: bool = False) -> list[Path]:
    paths: list[Path] = []
    for path in sorted(PAPERS_ROOT.rglob("metadata.yml")):
        data = load_yaml(path)
        if data.get("audit_status") != "raw":
            continue
        arxiv_id = bare_arxiv_id(data.get("arxiv_id"))
        if not arxiv_id:
            continue
        if data.get("type") not in ("", "Preprint"):
            continue
        if not refresh_derived and data.get("source") and data.get("summary") and data.get("links_alt"):
            continue
        paths.append(path)
    return paths


def enrich(path: Path, record: ArxivRecord) -> bool:
    data = load_yaml(path)
    before = dump_yaml(data)

    data["title"] = title_case_ascii(record.title) if record.title else data.get("title")
    data["authors"] = record.authors or data.get("authors") or []
    data["year"] = record.year or data.get("year")
    data["source"] = data.get("source") or "arXiv"
    data["type"] = "Preprint"
    data["doi"] = data.get("doi") or record.doi or None
    data["arxiv_id"] = normalize_arxiv_id(record.arxiv_id or data.get("arxiv_id")) or None
    data["abstract"] = record.abstract or data.get("abstract") or ""
    data["summary"] = data.get("summary") or ""
    data["link"] = arxiv_pdf_url(data["arxiv_id"])

    links = list(data.get("links_alt") or [])
    for link in (
        arxiv_abs_url(data["arxiv_id"]),
        arxiv_html_url(data["arxiv_id"]),
        f"https://doi.org/{data['doi']}" if data.get("doi") else "",
    ):
        if link and link not in links and link != data["link"]:
            links.append(link)
    data["links_alt"] = links

    tags = list(data.get("tags") or [])
    for tag in build_tags(record):
        if tag not in tags:
            tags.append(tag)
    data["tags"] = tags

    if not data.get("algorithm"):
        data["algorithm"] = infer_algorithm(record) or None

    data["audit_status"] = "raw"

    after = dump_yaml(data)
    if after != before:
        path.write_text(after, encoding="utf-8")
        return True
    return False


def refresh_derived(path: Path, *, dry_run: bool = False) -> bool:
    data = load_yaml(path)
    record = ArxivRecord(
        arxiv_id=data.get("arxiv_id") or "",
        title=data.get("title") or "",
        authors=data.get("authors") or [],
        year=data.get("year") or 0,
        abstract=data.get("abstract") or "",
        doi=data.get("doi") or "",
        journal_ref="",
        comment="",
        primary_category="",
        categories=[],
    )

    algorithm = data.get("algorithm") or ""
    inferred = infer_algorithm(record)
    if (
        algorithm.lower() in GENERIC_ALGORITHMS
        or (algorithm and len(algorithm) <= 2 and not algorithm_like(algorithm))
        or not algorithm
    ):
        new_algorithm = inferred or None
    else:
        new_algorithm = algorithm or None

    if new_algorithm == (algorithm or None):
        return False

    if not dry_run:
        raw = path.read_text(encoding="utf-8")
        path.write_text(
            replace_scalar_field(raw, "algorithm", new_algorithm),
            encoding="utf-8",
        )
        return True
    return True
