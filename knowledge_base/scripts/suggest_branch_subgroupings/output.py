"""Output formatting for branch subgroup suggestions."""

from typing import Any

from knowledge_base.scripts.suggest_branch_subgroupings.common import CountMode, display_path, format_path
from knowledge_base.scripts.suggest_branch_subgroupings.model import Suggestion


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
            print(f"- `{cluster.name}` ({len(cluster.children)} items; mean similarity {cluster.mean_similarity:.3f})")
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


__all__ = ["print_markdown", "suggestion_to_json"]
