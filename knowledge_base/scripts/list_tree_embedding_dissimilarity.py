"""Soft-audit Tree categories for embedding outliers.

Usage:
  python scripts/list_tree_embedding_dissimilarity.py
  python scripts/list_tree_embedding_dissimilarity.py --scope descendants --max-depth 4
  python scripts/list_tree_embedding_dissimilarity.py --format json
  python scripts/list_tree_embedding_dissimilarity.py --fail-on-findings

The script is read-only. It uses cached paper embeddings from
map/embedding_cache.json and reports papers whose mean cosine similarity to
other papers in the same Tree category is low.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from knowledge_base.config import KB_DIR  # noqa: E402
from knowledge_base.tree.nav_source import (  # noqa: E402
    TREE_YML,
    tree_from_file,
)
from knowledge_base.tree.model import (  # noqa: E402
    TreeBranch as Branch,
    TreeModel,
    resolve_metadata_or_generated_source,
)
from knowledge_base.utils.paper_ids import paper_id_from_metadata  # noqa: E402


METADATA_ROOT = KB_DIR / "docs" / "papers"
EMBEDDING_CACHE = KB_DIR / "map" / "embedding_cache.json"
Scope = Literal["direct", "descendants"]


@dataclass(frozen=True)
class Paper:
    id: str
    title: str
    metadata_path: Path


@dataclass(frozen=True)
class Outlier:
    paper: Paper
    mean_similarity_to_peers: float
    closest_peer_id: str | None
    closest_peer_title: str | None
    closest_peer_similarity: float | None


@dataclass(frozen=True)
class Finding:
    branch: Branch
    audited_ids: tuple[str, ...]
    mean_pairwise_similarity: float
    outliers: tuple[Outlier, ...]


def relative_to_kb(path: Path) -> str:
    try:
        return str(path.relative_to(KB_DIR))
    except ValueError:
        return str(path)


def display_path(path: tuple[str, ...]) -> tuple[str, ...]:
    return path if path == ("Tree",) else ("Tree", *path)


def format_path(path: tuple[str, ...]) -> str:
    return " > ".join(display_path(path))


def load_metadata(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data if isinstance(data, dict) else {}


def load_papers() -> dict[str, Paper]:
    by_id: dict[str, Paper] = {}
    for metadata_path in sorted(METADATA_ROOT.rglob("metadata.yml")):
        data = load_metadata(metadata_path)
        paper_id = paper_id_from_metadata(metadata_path, data, METADATA_ROOT)
        by_id[paper_id] = Paper(
            id=paper_id,
            title=" ".join(str(data.get("title") or paper_id).split()),
            metadata_path=metadata_path,
        )
    return by_id


def collect_branches(nav: Any) -> list[Branch]:
    model = TreeModel.from_tree(
        nav,
        resolve_source=lambda source: resolve_metadata_or_generated_source(
            source,
            base_dir=KB_DIR,
            metadata_root=METADATA_ROOT,
        ),
    )
    return list(model.branches)


def load_embeddings(path: Path = EMBEDDING_CACHE) -> dict[str, tuple[float, ...]]:
    with path.open("r", encoding="utf-8") as f:
        cache = json.load(f)
    papers = cache.get("papers", {})
    if not isinstance(papers, dict):
        return {}

    embeddings: dict[str, tuple[float, ...]] = {}
    for paper_id, entry in papers.items():
        if not isinstance(entry, dict) or not isinstance(entry.get("embedding"), list):
            continue
        vector = tuple(float(value) for value in entry["embedding"])
        norm = math.sqrt(sum(value * value for value in vector))
        if norm == 0:
            continue
        embeddings[str(paper_id)] = tuple(value / norm for value in vector)
    return embeddings


def cosine(left: tuple[float, ...], right: tuple[float, ...]) -> float:
    return sum(a * b for a, b in zip(left, right))


def category_ids(branch: Branch, scope: Scope) -> tuple[str, ...]:
    if scope == "descendants":
        return branch.descendant_paper_ids
    return branch.direct_paper_ids


def branch_depth(branch: Branch) -> int:
    return branch.depth


def find_branch_outliers(
    branch: Branch,
    *,
    papers: dict[str, Paper],
    embeddings: dict[str, tuple[float, ...]],
    scope: Scope,
    min_items: int,
    min_similarity: float,
    min_drop_from_mean: float,
    max_outliers_per_branch: int,
) -> Finding | None:
    ids = tuple(paper_id for paper_id in category_ids(branch, scope) if paper_id in embeddings)
    if len(ids) < min_items:
        return None

    vectors = {paper_id: embeddings[paper_id] for paper_id in ids}
    pairwise: dict[tuple[str, str], float] = {}
    pair_values: list[float] = []
    for i, left_id in enumerate(ids):
        for right_id in ids[i + 1 :]:
            value = cosine(vectors[left_id], vectors[right_id])
            pairwise[(left_id, right_id)] = value
            pairwise[(right_id, left_id)] = value
            pair_values.append(value)

    if not pair_values:
        return None
    mean_pairwise = sum(pair_values) / len(pair_values)

    outliers: list[Outlier] = []
    for paper_id in ids:
        peer_scores = [
            (other_id, pairwise[(paper_id, other_id)])
            for other_id in ids
            if other_id != paper_id
        ]
        mean_to_peers = sum(score for _, score in peer_scores) / len(peer_scores)
        closest_peer_id, closest_score = max(peer_scores, key=lambda item: item[1])
        if mean_to_peers >= min_similarity and mean_pairwise - mean_to_peers < min_drop_from_mean:
            continue
        outliers.append(
            Outlier(
                paper=papers[paper_id],
                mean_similarity_to_peers=mean_to_peers,
                closest_peer_id=closest_peer_id,
                closest_peer_title=papers[closest_peer_id].title,
                closest_peer_similarity=closest_score,
            )
        )

    if not outliers:
        return None
    outliers = sorted(outliers, key=lambda item: item.mean_similarity_to_peers)
    return Finding(
        branch=branch,
        audited_ids=ids,
        mean_pairwise_similarity=mean_pairwise,
        outliers=tuple(outliers[:max_outliers_per_branch]),
    )


def find_outliers(
    branches: list[Branch],
    *,
    papers: dict[str, Paper],
    embeddings: dict[str, tuple[float, ...]],
    scope: Scope,
    min_items: int,
    min_similarity: float,
    min_drop_from_mean: float,
    max_depth: int | None,
    branch_filter: str | None,
    max_outliers_per_branch: int,
) -> list[Finding]:
    branch_filter_folded = branch_filter.casefold() if branch_filter else None
    findings: list[Finding] = []
    for branch in branches:
        if max_depth is not None and branch_depth(branch) > max_depth:
            continue
        if branch_filter_folded and branch_filter_folded not in format_path(branch.path).casefold():
            continue
        finding = find_branch_outliers(
            branch,
            papers=papers,
            embeddings=embeddings,
            scope=scope,
            min_items=min_items,
            min_similarity=min_similarity,
            min_drop_from_mean=min_drop_from_mean,
            max_outliers_per_branch=max_outliers_per_branch,
        )
        if finding is not None:
            findings.append(finding)

    return sorted(
        findings,
        key=lambda finding: (
            finding.outliers[0].mean_similarity_to_peers,
            format_path(finding.branch.path),
        ),
    )


def print_markdown(
    findings: list[Finding],
    *,
    total_findings: int,
    scope: Scope,
    min_items: int,
    min_similarity: float,
    min_drop_from_mean: float,
    max_depth: int | None,
) -> None:
    print("# Tree Embedding Dissimilarity Audit\n")
    print(
        f"Scope: `{scope}`. Reporting branches with at least {min_items} embedded "
        f"paper(s), item mean similarity below {min_similarity:.2f}, or drop from "
        f"category mean at least {min_drop_from_mean:.2f}."
    )
    if max_depth is not None:
        print(f"Depth filter: through depth {max_depth}, counting `Tree` as depth 0.")
    print(f"{total_findings} branch(es) have possible embedding outliers.\n")

    for finding in findings:
        print(
            f"- `{format_path(finding.branch.path)}` "
            f"({len(finding.audited_ids)} embedded items; "
            f"mean pairwise similarity {finding.mean_pairwise_similarity:.3f})"
        )
        for outlier in finding.outliers:
            closest = "unavailable"
            if outlier.closest_peer_id is not None and outlier.closest_peer_similarity is not None:
                closest = (
                    f"`{outlier.closest_peer_id}` ({outlier.closest_peer_similarity:.3f})"
                    f" {outlier.closest_peer_title or ''}"
                )
            print(
                f"  - `{outlier.paper.id}` ({outlier.mean_similarity_to_peers:.3f} mean-to-peers): "
                f"{outlier.paper.title}"
            )
            print(f"    - Closest in category: {closest}")
            print(f"    - Metadata: `{relative_to_kb(outlier.paper.metadata_path)}`")


def print_json(findings: list[Finding]) -> None:
    payload = [
        {
            "branch_path": list(display_path(finding.branch.path)),
            "item_count": len(finding.audited_ids),
            "mean_pairwise_similarity": round(finding.mean_pairwise_similarity, 6),
            "outliers": [
                {
                    "id": outlier.paper.id,
                    "title": outlier.paper.title,
                    "metadata_path": relative_to_kb(outlier.paper.metadata_path),
                    "mean_similarity_to_peers": round(outlier.mean_similarity_to_peers, 6),
                    "closest_peer_id": outlier.closest_peer_id,
                    "closest_peer_similarity": (
                        round(outlier.closest_peer_similarity, 6)
                        if outlier.closest_peer_similarity is not None
                        else None
                    ),
                    "closest_peer_title": outlier.closest_peer_title,
                }
                for outlier in finding.outliers
            ],
        }
        for finding in findings
    ]
    print(json.dumps(payload, indent=2, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Soft-audit Tree categories for embedding outliers."
    )
    parser.add_argument(
        "--scope",
        choices=("direct", "descendants"),
        default="direct",
        help="Compare direct leaf papers in each branch or all descendant papers (default: direct).",
    )
    parser.add_argument(
        "--min-items",
        type=int,
        default=3,
        help="Minimum embedded papers required before auditing a branch (default: 3).",
    )
    parser.add_argument(
        "--min-similarity",
        type=float,
        default=0.35,
        help="Flag items whose mean similarity to category peers is below this value (default: 0.35).",
    )
    parser.add_argument(
        "--min-drop-from-mean",
        type=float,
        default=0.15,
        help="Flag items this far below the category mean pairwise similarity (default: 0.15).",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=None,
        help="Only audit branches through this depth, counting Tree as depth 0.",
    )
    parser.add_argument(
        "--branch",
        help="Only audit branches whose path contains this text.",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=50,
        help="Maximum number of branches to print (default: 50).",
    )
    parser.add_argument(
        "--max-outliers-per-branch",
        type=int,
        default=3,
        help="Maximum number of outlier papers to print per branch (default: 3).",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format (default: markdown).",
    )
    parser.add_argument(
        "--fail-on-findings",
        action="store_true",
        help="Exit with status 1 when any possible outliers are found.",
    )
    args = parser.parse_args()

    if args.min_items < 2:
        parser.error("--min-items must be at least 2")
    if args.max_results < 1:
        parser.error("--max-results must be at least 1")
    if args.max_outliers_per_branch < 1:
        parser.error("--max-outliers-per-branch must be at least 1")

    papers = load_papers()
    embeddings = load_embeddings()
    branches = collect_branches(tree_from_file(TREE_YML, normalize=False))
    findings = find_outliers(
        branches,
        papers=papers,
        embeddings=embeddings,
        scope=args.scope,
        min_items=args.min_items,
        min_similarity=args.min_similarity,
        min_drop_from_mean=args.min_drop_from_mean,
        max_depth=args.max_depth,
        branch_filter=args.branch,
        max_outliers_per_branch=args.max_outliers_per_branch,
    )
    displayed = findings[: args.max_results]

    if args.format == "json":
        print_json(displayed)
    else:
        print_markdown(
            displayed,
            total_findings=len(findings),
            scope=args.scope,
            min_items=args.min_items,
            min_similarity=args.min_similarity,
            min_drop_from_mean=args.min_drop_from_mean,
            max_depth=args.max_depth,
        )
        if len(findings) > len(displayed):
            print(f"\n... {len(findings) - len(displayed)} more branch(es) not shown.")
    return 1 if args.fail_on_findings and findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
