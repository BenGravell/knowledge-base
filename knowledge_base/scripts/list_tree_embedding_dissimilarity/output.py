"""Output helpers for Tree embedding dissimilarity."""

from __future__ import annotations

import json

from knowledge_base.scripts.list_tree_embedding_dissimilarity.data import display_path, format_path, relative_to_kb
from knowledge_base.scripts.list_tree_embedding_dissimilarity.model import Finding, Scope


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
