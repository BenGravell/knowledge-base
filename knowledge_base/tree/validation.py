"""Validation helpers for the standalone Tree navigation source."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml

from knowledge_base.config import KB_DIR
from knowledge_base.tree.nav_source import (
    YAML_LOADER,
    metadata_source_path,
    tree_from_file,
)
from knowledge_base.utils.paper_ids import paper_id_from_metadata


DOCS_DIR = KB_DIR / "docs"
METADATA_ROOT = DOCS_DIR / "papers"
TREE_YML = KB_DIR / "tree.yml"


@dataclass(frozen=True)
class MetadataPaper:
    id: str
    title: str
    algorithm: str
    metadata_path: Path
    generated_path: str


@dataclass(frozen=True)
class TreeLeaf:
    label: str
    source: str
    nav_path: tuple[str, ...]


@dataclass(frozen=True)
class TreeIssue:
    code: str
    message: str
    tree_label: str | None = None
    algorithm: str | None = None
    source: str | None = None
    expected_path: Path | None = None
    metadata_path: Path | None = None
    generated_path: str | None = None
    nav_path: tuple[str, ...] = ()


@dataclass(frozen=True)
class TreeValidationReport:
    tree_path: Path
    docs_dir: Path
    metadata_root: Path
    checked_links: int
    metadata_count: int
    referenced_papers: int
    issues: tuple[TreeIssue, ...]

    @property
    def ok(self) -> bool:
        return not self.issues


def relative_to_kb(path: Path) -> str:
    try:
        return str(path.relative_to(KB_DIR))
    except ValueError:
        return str(path)


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def local_source_path(source: str) -> str:
    return urlparse(source.replace("\\", "/").strip()).path


def normalize_label(value: Any) -> str:
    return " ".join(str(value or "").split()).casefold()


def clean_text(value: Any) -> str:
    return " ".join(str(value or "").split())


def is_external_source(source: str) -> bool:
    parsed = urlparse(source)
    return bool(parsed.scheme and (parsed.netloc or parsed.scheme in {"mailto", "tel"}))


def is_generated_paper_page(source: str) -> bool:
    return source.startswith("papers/") and source.endswith(".md")


def generated_paper_id(source: str) -> str:
    return source.removeprefix("papers/").removesuffix(".md")


def doc_path_from_source(source: str, *, tree_dir: Path, docs_dir: Path) -> Path | None:
    source_path = local_source_path(source)
    if not source_path.endswith(".md"):
        return None
    if source_path.startswith("../knowledge_base/docs/"):
        return (tree_dir / source_path).resolve()
    if source_path.startswith("docs/"):
        return (tree_dir / source_path).resolve()
    return (docs_dir / source_path).resolve()


def iter_tree_leaves(node: Any, labels: tuple[str, ...] = ()) -> list[TreeLeaf]:
    leaves: list[TreeLeaf] = []

    def walk(child: Any, path: tuple[str, ...]) -> None:
        if isinstance(child, str):
            leaves.append(TreeLeaf(path[-1] if path else child, child, path or (child,)))
            return

        if isinstance(child, list):
            for item in child:
                walk(item, path)
            return

        if isinstance(child, dict):
            for label_raw, value in child.items():
                label = str(label_raw)
                next_path = path + (label,)
                if isinstance(value, str):
                    leaves.append(TreeLeaf(label, value, next_path))
                else:
                    walk(value, next_path)

    walk(node, labels)
    return leaves


def load_metadata_papers(metadata_root: Path) -> list[MetadataPaper]:
    papers: list[MetadataPaper] = []
    for metadata_file in sorted(metadata_root.rglob("metadata.yml")):
        with metadata_file.open("r", encoding="utf-8") as f:
            data = yaml.load(f, Loader=YAML_LOADER) or {}
        if not isinstance(data, dict):
            data = {}

        paper_id = paper_id_from_metadata(metadata_file, data, metadata_root)
        papers.append(
            MetadataPaper(
                id=paper_id,
                title=clean_text(data.get("title")),
                algorithm=clean_text(data.get("algorithm")),
                metadata_path=metadata_file.resolve(),
                generated_path=f"papers/{paper_id}.md",
            )
        )
    return papers


def validate_tree(
    tree_path: Path = TREE_YML,
    *,
    docs_dir: Path = DOCS_DIR,
    metadata_root: Path = METADATA_ROOT,
    check_algorithm_labels: bool = False,
) -> TreeValidationReport:
    tree_path = tree_path.resolve()
    tree_dir = tree_path.parent
    docs_dir = docs_dir.resolve()
    metadata_root = metadata_root.resolve()

    tree = tree_from_file(tree_path, normalize=False)
    metadata_papers = load_metadata_papers(metadata_root)
    papers_by_path = {paper.metadata_path: paper for paper in metadata_papers}
    papers_by_id: dict[str, list[MetadataPaper]] = {}
    for paper in metadata_papers:
        papers_by_id.setdefault(paper.id, []).append(paper)

    issues: list[TreeIssue] = []
    referenced_metadata_paths: set[Path] = set()
    referenced_paper_ids: set[str] = set()
    checked_links = 0

    for leaf in iter_tree_leaves(tree, ("Tree",)):
        source = leaf.source.replace("\\", "/").strip()
        if not source or source.startswith("#") or is_external_source(source):
            continue

        checked_links += 1
        source_path = local_source_path(source)
        metadata_file = metadata_source_path(source_path, tree_dir)
        if metadata_file is not None:
            metadata_file = metadata_file.resolve()
            if not metadata_file.exists():
                issues.append(
                    TreeIssue(
                        code="missing-linked-doc",
                        message="Tree metadata source does not exist.",
                        source=source,
                        expected_path=metadata_file,
                        nav_path=leaf.nav_path,
                    )
                )
                continue

            paper = papers_by_path.get(metadata_file)
            if paper is None:
                issues.append(
                    TreeIssue(
                        code="missing-linked-doc",
                        message="Tree metadata source is outside docs/papers.",
                        source=source,
                        expected_path=metadata_file,
                        nav_path=leaf.nav_path,
                    )
                )
                continue

            referenced_metadata_paths.add(paper.metadata_path)
            referenced_paper_ids.add(paper.id)
            if (
                check_algorithm_labels
                and paper.algorithm
                and normalize_label(leaf.label) != normalize_label(paper.algorithm)
            ):
                issues.append(
                    TreeIssue(
                        code="algorithm-label-mismatch",
                        message="Tree leaf label does not match metadata algorithm.",
                        tree_label=leaf.label,
                        algorithm=paper.algorithm,
                        source=source,
                        metadata_path=paper.metadata_path,
                        nav_path=leaf.nav_path,
                    )
                )
            continue

        if is_generated_paper_page(source_path):
            paper_id = generated_paper_id(source_path)
            matching_papers = papers_by_id.get(paper_id, [])
            if not matching_papers:
                issues.append(
                    TreeIssue(
                        code="missing-linked-doc",
                        message="Generated paper page has no source metadata.",
                        source=source,
                        expected_path=docs_dir / source_path,
                        nav_path=leaf.nav_path,
                    )
                )
                continue
            referenced_paper_ids.add(paper_id)
            paper = matching_papers[0]
            if (
                check_algorithm_labels
                and paper.algorithm
                and normalize_label(leaf.label) != normalize_label(paper.algorithm)
            ):
                issues.append(
                    TreeIssue(
                        code="algorithm-label-mismatch",
                        message="Tree leaf label does not match metadata algorithm.",
                        tree_label=leaf.label,
                        algorithm=paper.algorithm,
                        source=source,
                        metadata_path=paper.metadata_path,
                        nav_path=leaf.nav_path,
                    )
                )
            continue

        doc_path = doc_path_from_source(source, tree_dir=tree_dir, docs_dir=docs_dir)
        if doc_path is not None and not doc_path.exists():
            issues.append(
                TreeIssue(
                    code="missing-linked-doc",
                    message="Tree page source does not exist.",
                    source=source,
                    expected_path=doc_path,
                    nav_path=leaf.nav_path,
                )
            )

    referenced_paper_paths = set(referenced_metadata_paths)
    for paper_id in referenced_paper_ids:
        referenced_paper_paths.update(paper.metadata_path for paper in papers_by_id.get(paper_id, []))

    for paper in metadata_papers:
        if paper.metadata_path in referenced_paper_paths:
            continue
        issues.append(
            TreeIssue(
                code="unplaced-paper",
                message="Metadata-backed paper is not referenced in tree.yml.",
                metadata_path=paper.metadata_path,
                generated_path=paper.generated_path,
            )
        )

    return TreeValidationReport(
        tree_path=tree_path,
        docs_dir=docs_dir,
        metadata_root=metadata_root,
        checked_links=checked_links,
        metadata_count=len(metadata_papers),
        referenced_papers=len(referenced_paper_paths),
        issues=tuple(issues),
    )


def format_nav_path(nav_path: tuple[str, ...]) -> str:
    return " > ".join(nav_path)


def format_issue(issue: TreeIssue) -> str:
    if issue.code == "unplaced-paper":
        metadata_path = relative_to_kb(issue.metadata_path) if issue.metadata_path else "<unknown>"
        generated_path = issue.generated_path or "<unknown>"
        return f"{metadata_path} (generated {generated_path})"

    if issue.code == "algorithm-label-mismatch":
        location = format_nav_path(issue.nav_path) if issue.nav_path else "<unknown location>"
        metadata_path = relative_to_kb(issue.metadata_path) if issue.metadata_path else "<unknown>"
        return (
            f"{location}: tree label `{issue.tree_label}` should be "
            f"`{issue.algorithm}` ({metadata_path})"
        )

    location = format_nav_path(issue.nav_path) if issue.nav_path else "<unknown location>"
    source = issue.source or "<unknown source>"
    if issue.expected_path is None:
        return f"{location}: {source} ({issue.message})"
    return f"{location}: {source} (expected {relative_to_kb(issue.expected_path)})"


def format_tree_validation_report(
    report: TreeValidationReport,
    *,
    max_results: int | None = None,
) -> str:
    if report.ok:
        return "\n".join(
            [
                "Tree validation passed.",
                f"Checked {report.checked_links} local tree link(s).",
                f"Found {report.metadata_count} metadata-backed paper(s).",
            ]
        )

    lines = [
        f"Tree validation failed with {len(report.issues)} issue(s).",
        f"Checked {report.checked_links} local tree link(s).",
        f"Found {report.metadata_count} metadata-backed paper(s).",
    ]
    titles = {
        "missing-linked-doc": "Missing linked docs",
        "unplaced-paper": "Unplaced metadata-backed papers",
        "algorithm-label-mismatch": "Tree labels not matching metadata algorithm",
    }

    for code in ("missing-linked-doc", "unplaced-paper", "algorithm-label-mismatch"):
        group = [issue for issue in report.issues if issue.code == code]
        if not group:
            continue

        lines.append("")
        lines.append(f"{titles.get(code, code)} ({len(group)}):")
        shown = group if max_results is None else group[:max_results]
        for issue in shown:
            lines.append(f"- {format_issue(issue)}")
        if max_results is not None and len(group) > len(shown):
            lines.append(f"- ... {len(group) - len(shown)} more")

    return "\n".join(lines)
