"""Output helpers for tree algorithm label suggestions."""

from collections import Counter
from typing import Any

from knowledge_base.scripts.suggest_tree_algorithm_labels.constants import ACTIONS, CONFIDENCE_RANK, CONFIDENCES
from knowledge_base.scripts.suggest_tree_algorithm_labels.model import Suggestion
from knowledge_base.tree.validation import format_nav_path, relative_to_kb


def suggestion_to_dict(suggestion: Suggestion) -> dict[str, Any]:
    return {
        "action": suggestion.action,
        "confidence": suggestion.confidence,
        "canonical_label": suggestion.canonical_label,
        "suggested_tree_label": suggestion.suggested_tree_label,
        "suggested_metadata_algorithm": suggestion.suggested_metadata_algorithm,
        "reason": suggestion.reason,
        "tree_label": suggestion.tree_label,
        "metadata_algorithm": suggestion.algorithm,
        "title": suggestion.title,
        "audit_status": suggestion.audit_status,
        "source": suggestion.source,
        "metadata_path": relative_to_kb(suggestion.metadata_path),
        "nav_path": list(suggestion.nav_path),
    }


def filter_suggestions(
    suggestions: list[Suggestion],
    *,
    action: str | None,
    min_confidence: str,
) -> list[Suggestion]:
    minimum = CONFIDENCE_RANK[min_confidence]
    return [
        suggestion
        for suggestion in suggestions
        if (action is None or suggestion.action == action) and CONFIDENCE_RANK[suggestion.confidence] >= minimum
    ]


def print_markdown(suggestions: list[Suggestion], *, total: int, max_results: int) -> None:
    action_counts = Counter(suggestion.action for suggestion in suggestions)
    confidence_counts = Counter(suggestion.confidence for suggestion in suggestions)
    shown_count = min(len(suggestions), max_results)

    print("# Tree Algorithm Label Suggestions\n")
    print(f"{shown_count} of {total} suggestion(s) shown.\n")
    if suggestions:
        print("## Summary\n")
        for action in ACTIONS:
            if action_counts[action]:
                print(f"- `{action}`: {action_counts[action]}")
        for confidence in CONFIDENCES:
            if confidence_counts[confidence]:
                print(f"- `{confidence}` confidence: {confidence_counts[confidence]}")
        print()

    for suggestion in suggestions[:max_results]:
        print(f"- `{suggestion.action}` ({suggestion.confidence})")
        print(f"  - Tree: `{suggestion.tree_label}`")
        print(f"  - Metadata algorithm: `{suggestion.algorithm}`")
        if suggestion.canonical_label:
            print(f"  - Canonical: `{suggestion.canonical_label}`")
        if suggestion.suggested_tree_label:
            print(f"  - Suggested tree label: `{suggestion.suggested_tree_label}`")
        if suggestion.suggested_metadata_algorithm:
            print(f"  - Suggested metadata algorithm: `{suggestion.suggested_metadata_algorithm}`")
        print(f"  - Reason: {suggestion.reason}")
        print(f"  - Audit status: `{suggestion.audit_status}`")
        print(f"  - Title: {suggestion.title}")
        print(f"  - Metadata: `{relative_to_kb(suggestion.metadata_path)}`")
        print(f"  - Nav: `{format_nav_path(suggestion.nav_path)}`")
    if len(suggestions) > max_results:
        print(f"\n... {len(suggestions) - max_results} more suggestion(s) not shown.")


__all__ = ["filter_suggestions", "print_markdown", "suggestion_to_dict"]
