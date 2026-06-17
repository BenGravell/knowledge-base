"""Suggest one new Tree sub-grouping level for overfull branches.

Usage:
  python scripts/suggest_branch_subgroupings.py
  python scripts/suggest_branch_subgroupings.py --max-results 5
  python scripts/suggest_branch_subgroupings.py --branch "First-Order Methods"
  python scripts/suggest_branch_subgroupings.py --format json
  python scripts/suggest_branch_subgroupings.py --branch "First-Order Methods" --write-tree

The script is read-only unless ``--write-tree`` is passed. It uses cached paper
text embeddings from ``map/embedding_cache.json`` and proposes natural
direct-child groupings for branches that would be reported as "too many" by
``list_branching_factor_violations.py``.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

import numpy as np
import yaml
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import normalize


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from knowledge_base.config import KB_DIR  # noqa: E402
from knowledge_base.tree.nav_source import TREE_YML  # noqa: E402
from knowledge_base.tree.model import (  # noqa: E402
    TreeBranch as Branch,
    TreeChild as ChildItem,
    load_tree_model,
)
from knowledge_base.utils.paper_ids import paper_id_from_metadata  # noqa: E402


DOCS_DIR = KB_DIR / "docs"
METADATA_ROOT = DOCS_DIR / "papers"
EMBEDDING_CACHE = KB_DIR / "map" / "embedding_cache.json"
LANDING_PAGES = {"tree.md", "tree/index.md"}
CountMode = Literal["all", "branches"]

BROAD_TERMS = {
    "algorithm",
    "algorithms",
    "analysis",
    "applications",
    "control",
    "deep learning",
    "learning",
    "machine learning",
    "method",
    "methods",
    "model",
    "models",
    "optimization",
    "planning",
    "reinforcement learning",
    "robotics",
    "survey",
    "surveys",
    "theory",
}


@dataclass(frozen=True)
class Paper:
    id: str
    title: str
    algorithm: str
    tags: tuple[str, ...]
    metadata_path: Path


@dataclass(frozen=True)
class Cluster:
    name: str
    children: tuple[ChildItem, ...]
    mean_similarity: float


@dataclass(frozen=True)
class Suggestion:
    branch: Branch
    clustered_child_count: int
    skipped_child_count: int
    k: int
    silhouette: float
    score: float
    clusters: tuple[Cluster, ...]


@dataclass(frozen=True)
class LineItem:
    label: str | None
    start: int
    end: int
    lines: tuple[str, ...]
    is_landing: bool


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def display_path(path: tuple[str, ...]) -> tuple[str, ...]:
    return path if path == ("Tree",) else ("Tree", *path)


def tree_yml_path(path: tuple[str, ...]) -> tuple[str, ...]:
    return display_path(path)


def format_path(path: tuple[str, ...]) -> str:
    return " > ".join(display_path(path))


def relative_to_kb(path: Path) -> str:
    try:
        return str(path.relative_to(KB_DIR))
    except ValueError:
        return str(path)


def is_landing_item(label: str, child: Any) -> bool:
    return isinstance(child, str) and (
        child in LANDING_PAGES
        or (label.strip().lower() == "overview" and child in LANDING_PAGES)
    )


def load_papers(metadata_root: Path = METADATA_ROOT) -> dict[str, Paper]:
    papers: dict[str, Paper] = {}
    for metadata_file in sorted(metadata_root.rglob("metadata.yml")):
        with metadata_file.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        if not isinstance(data, dict):
            continue
        paper_id = paper_id_from_metadata(metadata_file, data, metadata_root)
        tags = tuple(str(tag).strip() for tag in as_list(data.get("tags")) if str(tag).strip())
        papers[paper_id] = Paper(
            id=paper_id,
            title=" ".join(str(data.get("title") or paper_id).split()),
            algorithm=" ".join(str(data.get("algorithm") or "").split()),
            tags=tags,
            metadata_path=metadata_file,
        )
    return papers


def load_embeddings(cache_path: Path = EMBEDDING_CACHE) -> dict[str, np.ndarray]:
    if not cache_path.exists():
        raise FileNotFoundError(f"Embedding cache not found: {cache_path}")

    with cache_path.open("r", encoding="utf-8") as f:
        cache = json.load(f)

    embeddings: dict[str, np.ndarray] = {}
    papers = cache.get("papers", {})
    if not isinstance(papers, dict):
        return embeddings

    for paper_id, entry in papers.items():
        if not isinstance(entry, dict) or not isinstance(entry.get("embedding"), list):
            continue
        vector = np.asarray(entry["embedding"], dtype=np.float32)
        if vector.ndim == 1 and np.linalg.norm(vector) > 0:
            embeddings[str(paper_id)] = vector
    return embeddings


def collect_branches(tree_path: Path, *, include_root: bool) -> list[Branch]:
    model = load_tree_model(
        tree_path,
        base_dir=tree_path.parent,
        metadata_root=METADATA_ROOT,
    )
    return [model.root, *model.branches] if include_root else list(model.branches)


def child_embedding(
    child: ChildItem,
    embeddings: dict[str, np.ndarray],
) -> np.ndarray | None:
    vectors = [embeddings[paper_id] for paper_id in child.paper_ids if paper_id in embeddings]
    if not vectors:
        return None
    matrix = np.vstack(vectors)
    vector = matrix.mean(axis=0)
    norm = np.linalg.norm(vector)
    if norm == 0:
        return None
    return vector / norm


def cluster_with_k(matrix: np.ndarray, k: int) -> np.ndarray:
    try:
        model = AgglomerativeClustering(
            n_clusters=k,
            metric="cosine",
            linkage="average",
        )
    except TypeError:
        model = AgglomerativeClustering(
            n_clusters=k,
            affinity="cosine",
            linkage="average",
        )
    return model.fit_predict(matrix)


def candidate_cluster_counts(
    item_count: int,
    *,
    maximum: int,
    max_groups: int | None,
) -> range:
    if item_count < 3:
        return range(0)
    if max_groups is None:
        inferred_max = maximum
    else:
        inferred_max = max_groups
    upper = min(item_count - 1, max(2, inferred_max))
    return range(2, upper + 1)


def score_labels(
    matrix: np.ndarray,
    labels: np.ndarray,
    *,
    minimum: int,
    maximum: int,
    sweet_spot: int,
) -> tuple[float, float]:
    silhouette = float(silhouette_score(matrix, labels, metric="cosine"))
    sizes = np.bincount(labels)
    oversized = sum(max(0, int(size) - maximum) for size in sizes) / len(labels)
    undersized = sum(1 for size in sizes if size < minimum) / len(sizes)
    mean_size = len(labels) / len(sizes)
    target_distance = min(2.0, abs(mean_size - sweet_spot) / max(1, sweet_spot))
    score = silhouette - 0.12 * oversized - 0.08 * undersized - 0.08 * target_distance
    return score, silhouette


def choose_labels(
    matrix: np.ndarray,
    *,
    minimum: int,
    maximum: int,
    sweet_spot: int,
    max_groups: int | None,
) -> tuple[np.ndarray, int, float, float] | None:
    best: tuple[float, float, int, np.ndarray] | None = None
    for k in candidate_cluster_counts(
        len(matrix),
        maximum=maximum,
        max_groups=max_groups,
    ):
        labels = cluster_with_k(matrix, k)
        if len(set(labels)) < 2 or len(set(labels)) >= len(labels):
            continue
        score, silhouette = score_labels(
            matrix,
            labels,
            minimum=minimum,
            maximum=maximum,
            sweet_spot=sweet_spot,
        )
        if best is None or score > best[0]:
            best = (score, silhouette, k, labels)

    if best is None:
        return None
    score, silhouette, k, labels = best
    return labels, k, silhouette, score


def normalize_phrase(value: str) -> str:
    value = re.sub(r"\s+", " ", value.replace("\n", " ")).strip(" '\"`.,:;")
    return value


def add_phrase(
    terms: Counter[str],
    phrase: str,
    *,
    weight: int,
    parent_terms: set[str],
) -> None:
    phrase = normalize_phrase(phrase)
    key = phrase.lower()
    if not phrase or len(phrase) < 3:
        return
    if key in parent_terms or key in BROAD_TERMS:
        return
    terms[phrase] += weight


def suggest_cluster_name(
    children: tuple[ChildItem, ...],
    papers: dict[str, Paper],
    parent_path: tuple[str, ...],
) -> str:
    parent_terms = {part.lower() for part in parent_path}
    terms: Counter[str] = Counter()

    for child in children:
        if child.kind == "branch":
            add_phrase(terms, child.label, weight=8, parent_terms=parent_terms)
        for paper_id in child.paper_ids:
            paper = papers.get(paper_id)
            if paper is None:
                continue
            add_phrase(terms, paper.algorithm, weight=5, parent_terms=parent_terms)
            for tag in paper.tags:
                add_phrase(terms, tag, weight=3, parent_terms=parent_terms)

    if terms:
        return " / ".join(term for term, _ in terms.most_common(3))

    compact_labels = [child.label for child in children[:2]]
    return " / ".join(compact_labels) if compact_labels else "Mixed"


def mean_intra_similarity(matrix: np.ndarray, indices: list[int]) -> float:
    if len(indices) < 2:
        return 1.0
    submatrix = matrix[indices]
    similarities = submatrix @ submatrix.T
    upper = similarities[np.triu_indices(len(indices), k=1)]
    return float(np.mean(upper)) if len(upper) else 1.0


def build_suggestion(
    branch: Branch,
    *,
    children: tuple[ChildItem, ...],
    embeddings: dict[str, np.ndarray],
    papers: dict[str, Paper],
    minimum: int,
    maximum: int,
    sweet_spot: int,
    max_groups: int | None,
    min_embedded_children: int,
) -> Suggestion | None:
    embedded_children: list[ChildItem] = []
    vectors: list[np.ndarray] = []
    for child in children:
        vector = child_embedding(child, embeddings)
        if vector is None:
            continue
        embedded_children.append(child)
        vectors.append(vector)

    if len(embedded_children) < min_embedded_children:
        return None

    matrix = normalize(np.vstack(vectors), norm="l2")
    chosen = choose_labels(
        matrix,
        minimum=minimum,
        maximum=maximum,
        sweet_spot=sweet_spot,
        max_groups=max_groups,
    )
    if chosen is None:
        return None
    labels, k, silhouette, score = chosen

    clusters: list[Cluster] = []
    for cluster_id in sorted(set(labels), key=lambda label: min(np.where(labels == label)[0])):
        indices = [int(index) for index in np.where(labels == cluster_id)[0]]
        cluster_children = tuple(embedded_children[index] for index in indices)
        clusters.append(
            Cluster(
                name=suggest_cluster_name(cluster_children, papers, branch.path),
                children=cluster_children,
                mean_similarity=mean_intra_similarity(matrix, indices),
            )
        )

    return Suggestion(
        branch=branch,
        clustered_child_count=len(embedded_children),
        skipped_child_count=len(children) - len(embedded_children),
        k=k,
        silhouette=silhouette,
        score=score,
        clusters=tuple(clusters),
    )


def find_too_many_branches(
    branches: list[Branch],
    *,
    mode: CountMode,
    maximum: int,
    max_depth: int | None,
    branch_filter: str | None,
) -> list[Branch]:
    filtered = []
    branch_filter_lower = branch_filter.lower() if branch_filter else None
    for branch in branches:
        if max_depth is not None and branch.depth > max_depth:
            continue
        if branch.count_for(mode) <= maximum:
            continue
        if branch_filter_lower and branch_filter_lower not in format_path(branch.path).lower():
            continue
        filtered.append(branch)

    return sorted(
        filtered,
        key=lambda branch: (
            -(branch.count_for(mode) - maximum),
            format_path(branch.path),
        ),
    )


def print_markdown(
    suggestions: list[Suggestion],
    *,
    total_too_many: int,
    mode: CountMode,
    maximum: int,
    shown_items: int,
) -> None:
    print("# Branch Subgrouping Suggestions\n")
    print(
        "Method: agglomerative clustering over cosine-normalized cached "
        "text embeddings, choosing the cluster count by silhouette score "
        "with a soft preference for useful group sizes."
    )
    print(f"Counting mode: `{mode}`. Too-many threshold: more than {maximum}.")
    print(f"{len(suggestions)} suggestion(s) shown for {total_too_many} overfull branch(es).\n")

    for suggestion in suggestions:
        branch = suggestion.branch
        print(f"## `{format_path(branch.path)}`\n")
        print(
            f"{branch.count_for(mode)} direct child "
            f"{'branches' if mode == 'branches' else 'items'}; "
            f"clustered {suggestion.clustered_child_count}, "
            f"skipped {suggestion.skipped_child_count} without embeddings."
        )
        print(
            f"Suggested groups: {suggestion.k} "
            f"(silhouette {suggestion.silhouette:.3f}, score {suggestion.score:.3f}).\n"
        )
        for cluster in suggestion.clusters:
            print(
                f"- `{cluster.name}` ({len(cluster.children)} items; "
                f"mean similarity {cluster.mean_similarity:.3f})"
            )
            for child in cluster.children[:shown_items]:
                kind = "branch" if child.kind == "branch" else "leaf"
                print(f"  - {child.label} [{kind}]")
            remaining = len(cluster.children) - shown_items
            if remaining > 0:
                print(f"  - ... {remaining} more")
        print()


def suggestion_to_json(suggestion: Suggestion, *, mode: CountMode) -> dict[str, Any]:
    return {
        "path": list(display_path(suggestion.branch.path)),
        "count": suggestion.branch.count_for(mode),
        "branch_count": suggestion.branch.branch_count,
        "leaf_count": suggestion.branch.leaf_count,
        "clustered_child_count": suggestion.clustered_child_count,
        "skipped_child_count": suggestion.skipped_child_count,
        "suggested_group_count": suggestion.k,
        "silhouette": round(suggestion.silhouette, 6),
        "score": round(suggestion.score, 6),
        "groups": [
            {
                "suggested_label": cluster.name,
                "size": len(cluster.children),
                "mean_similarity": round(cluster.mean_similarity, 6),
                "children": [
                    {
                        "label": child.label,
                        "kind": child.kind,
                        "paper_ids": list(child.paper_ids),
                        "source": child.source,
                    }
                    for child in cluster.children
                ],
            }
            for cluster in suggestion.clusters
        ],
    }


def split_list_mapping_line(line: str) -> tuple[int, str | None, str | None] | None:
    stripped = line.lstrip(" ")
    if not stripped.startswith("- "):
        return None

    indent = len(line) - len(stripped)
    body = stripped[2:].rstrip("\n")
    separator_index: int | None = None

    if body.startswith(('"', "'")):
        quote = body[0]
        escaped = False
        index = 1
        while index < len(body):
            char = body[index]
            if quote == '"' and escaped:
                escaped = False
            elif quote == '"' and char == "\\":
                escaped = True
            elif quote == "'" and char == "'" and index + 1 < len(body) and body[index + 1] == "'":
                index += 1
            elif char == quote:
                following = body[index + 1 :].lstrip()
                if following.startswith(":"):
                    separator_index = index + 1 + (len(body[index + 1 :]) - len(following))
                break
            index += 1
    else:
        for index, char in enumerate(body):
            if char == ":" and (index + 1 == len(body) or body[index + 1].isspace()):
                separator_index = index
                break

    if separator_index is not None:
        raw_label = body[:separator_index].strip()
        rest = body[separator_index + 1 :].strip()
        try:
            loaded_label = yaml.safe_load(raw_label)
        except yaml.YAMLError:
            loaded_label = raw_label
        return indent, str(loaded_label), rest

    return indent, None, body.strip()


def line_indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def block_end(lines: list[str], start: int, indent: int) -> int:
    for index in range(start + 1, len(lines)):
        if lines[index].strip() and line_indent(lines[index]) <= indent:
            return index
    return len(lines)


def find_branch_line(lines: list[str], path: tuple[str, ...]) -> tuple[int, int, int]:
    search_start = 0
    search_end = len(lines)
    expected_indent = 0

    for label in path:
        found: tuple[int, int] | None = None
        for index in range(search_start, search_end):
            parsed = split_list_mapping_line(lines[index])
            if parsed is None:
                continue
            indent, parsed_label, _ = parsed
            if indent == expected_indent and parsed_label == label:
                found = (index, indent)
                break

        if found is None:
            raise ValueError(f"Could not find branch path in tree.yml: {format_path(path)}")

        line_index, indent = found
        search_start = line_index + 1
        search_end = block_end(lines, line_index, indent)
        expected_indent = indent + 2

    return search_start - 1, search_end, expected_indent - 2


def scalar_leaf_label(source: str) -> str:
    return source.removesuffix(".md").replace("-", " ").replace("_", " ").title()


def collect_direct_line_items(
    lines: list[str],
    *,
    child_start: int,
    child_end: int,
    child_indent: int,
) -> list[LineItem]:
    starts: list[int] = []
    for index in range(child_start, child_end):
        parsed = split_list_mapping_line(lines[index])
        if parsed is not None and parsed[0] == child_indent:
            starts.append(index)

    items: list[LineItem] = []
    for offset, start in enumerate(starts):
        end = starts[offset + 1] if offset + 1 < len(starts) else child_end
        parsed = split_list_mapping_line(lines[start])
        if parsed is None:
            continue
        _, label, scalar = parsed
        display_label = label if label is not None else scalar_leaf_label(scalar or "")
        items.append(
            LineItem(
                label=display_label,
                start=start,
                end=end,
                lines=tuple(lines[start:end]),
                is_landing=is_landing_item(display_label, scalar or ""),
            )
        )
    return items


def yaml_key(label: str) -> str:
    if (
        label
        and label == label.strip()
        and not label.startswith(("-", "?", "@", "`"))
        and not re.search(r"[:#{}\[\],&*!|>%\"']", label)
        and label.lower() not in {"null", "true", "false", "yes", "no", "on", "off"}
    ):
        return label
    return json.dumps(label, ensure_ascii=False)


def apply_tree_suggestion(tree_path: Path, suggestion: Suggestion) -> None:
    text = tree_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    had_trailing_newline = text.endswith("\n")

    branch_line, branch_end, branch_indent = find_branch_line(
        lines,
        tree_yml_path(suggestion.branch.path),
    )
    child_indent = branch_indent + 2
    line_items = collect_direct_line_items(
        lines,
        child_start=branch_line + 1,
        child_end=branch_end,
        child_indent=child_indent,
    )
    snippets_by_label: dict[str, list[LineItem]] = {}
    for item in line_items:
        if item.label is not None:
            snippets_by_label.setdefault(item.label, []).append(item)

    used_ids: set[int] = set()
    cluster_lines: list[str] = []
    for cluster in suggestion.clusters:
        cluster_lines.append(f"{' ' * child_indent}- {yaml_key(cluster.name)}:\n")
        for child in cluster.children:
            candidates = snippets_by_label.get(child.label, [])
            item = next((candidate for candidate in candidates if id(candidate) not in used_ids), None)
            if item is None:
                raise ValueError(f"Could not find child item in tree.yml: {child.label}")
            used_ids.add(id(item))
            cluster_lines.extend(f"  {line}" for line in item.lines)

    landing_lines: list[str] = []
    skipped_lines: list[str] = []
    for item in line_items:
        if id(item) in used_ids:
            continue
        if item.is_landing:
            landing_lines.extend(item.lines)
        else:
            skipped_lines.extend(item.lines)

    new_lines = lines[: branch_line + 1]
    new_lines.extend(landing_lines)
    new_lines.extend(cluster_lines)
    new_lines.extend(skipped_lines)
    new_lines.extend(lines[branch_end:])

    new_text = "".join(new_lines)
    if had_trailing_newline and not new_text.endswith("\n"):
        new_text += "\n"

    yaml.safe_load(new_text)
    tree_path.write_text(new_text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Suggest one new Tree sub-grouping level for branches with too many "
            "direct children, using cached text embeddings."
        )
    )
    parser.add_argument("--min", dest="minimum", type=int, default=2)
    parser.add_argument("--max", dest="maximum", type=int, default=7)
    parser.add_argument("--sweet-spot", type=int, default=5)
    parser.add_argument(
        "--count",
        choices=("all", "branches"),
        default="all",
        help="Match list_branching_factor_violations.py counting mode.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format.",
    )
    parser.add_argument(
        "--branch",
        default=None,
        help="Only suggest for branches whose formatted path contains this text.",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=None,
        help="Only consider branches through this depth; Tree is depth 0.",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=10,
        help="Maximum number of overfull branches to suggest.",
    )
    parser.add_argument(
        "--max-groups",
        type=int,
        default=None,
        help="Maximum candidate group count. Defaults to an automatic range.",
    )
    parser.add_argument(
        "--show-items",
        type=int,
        default=12,
        help="Markdown: show up to N children per suggested group.",
    )
    parser.add_argument(
        "--min-embedded-children",
        type=int,
        default=4,
        help="Skip branches with fewer than N embeddable direct children.",
    )
    parser.add_argument(
        "--exclude-root",
        action="store_true",
        help="Do not consider the synthetic Tree root branch.",
    )
    parser.add_argument(
        "--write-tree",
        action="store_true",
        help=(
            "Write exactly one suggested regrouping into tree.yml. "
            "Use --branch or --max-results 1 to select a single target."
        ),
    )
    parser.add_argument(
        "--tree-yml",
        type=Path,
        default=TREE_YML,
        help="Tree YAML file to read and optionally write. Defaults to knowledge_base/tree.yml.",
    )
    args = parser.parse_args()

    if args.minimum < 0 or args.maximum < 1:
        sys.exit("--min must be non-negative and --max must be at least 1.")
    if args.minimum > args.maximum:
        sys.exit("--min cannot be greater than --max.")
    if args.sweet_spot < 1:
        sys.exit("--sweet-spot must be at least 1.")
    if args.max_depth is not None and args.max_depth < 0:
        sys.exit("--max-depth must be at least 0.")
    if args.max_groups is not None and args.max_groups < 2:
        sys.exit("--max-groups must be at least 2.")

    tree_path = args.tree_yml
    branches = collect_branches(
        include_root=not args.exclude_root,
        tree_path=tree_path,
    )
    too_many = find_too_many_branches(
        branches,
        mode=args.count,
        maximum=args.maximum,
        max_depth=args.max_depth,
        branch_filter=args.branch,
    )

    papers = load_papers()
    embeddings = load_embeddings()
    suggestions: list[Suggestion] = []
    for branch in too_many:
        suggestion = build_suggestion(
            branch,
            children=branch.children_for(args.count),
            embeddings=embeddings,
            papers=papers,
            minimum=args.minimum,
            maximum=args.maximum,
            sweet_spot=args.sweet_spot,
            max_groups=args.max_groups,
            min_embedded_children=args.min_embedded_children,
        )
        if suggestion is not None:
            suggestions.append(suggestion)
        if args.max_results is not None and len(suggestions) >= args.max_results:
            break

    wrote_tree = False
    if args.write_tree:
        if not suggestions:
            sys.exit("--write-tree found no suggestion to write.")
        if len(suggestions) > 1:
            sys.exit(
                "--write-tree needs exactly one suggestion. "
                "Narrow with --branch or pass --max-results 1."
            )
        apply_tree_suggestion(tree_path, suggestions[0])
        wrote_tree = True

    if args.format == "json":
        print(
            json.dumps(
                {
                    "too_many_branch_count": len(too_many),
                    "suggestion_count": len(suggestions),
                    "wrote_tree": wrote_tree,
                    "tree_yml": relative_to_kb(tree_path),
                    "suggestions": [
                        suggestion_to_json(suggestion, mode=args.count)
                        for suggestion in suggestions
                    ],
                },
                indent=2,
                ensure_ascii=False,
            )
        )
    else:
        if wrote_tree:
            print(f"Wrote suggested subgrouping to {relative_to_kb(tree_path)}.\n")
        print_markdown(
            suggestions,
            total_too_many=len(too_many),
            mode=args.count,
            maximum=args.maximum,
            shown_items=args.show_items,
        )


if __name__ == "__main__":
    main()
