"""Suggestion collection and ranking logic."""

from collections import Counter
from pathlib import Path
from typing import Any

from knowledge_base.scripts.suggest_tree_algorithm_labels.constants import (
    ACTION_ACCEPT_ALIAS,
    ACTION_REVIEW,
    ACTION_UPDATE_METADATA,
    ACTION_UPDATE_TREE,
    CONFIDENCE_HIGH,
    CONFIDENCE_LOW,
    CONFIDENCE_MEDIUM,
)
from knowledge_base.scripts.suggest_tree_algorithm_labels.edits import load_metadata
from knowledge_base.scripts.suggest_tree_algorithm_labels.label_text import (
    algorithm_in_metadata_text,
    algorithm_in_tags,
    algorithm_looks_invalid,
    alnum_key,
    audit_suggested_algorithm,
    clean_text,
    is_code_like,
    is_title_like,
    soft_equivalence_reason,
    text_introduces_algorithm,
    title_head,
    words,
)
from knowledge_base.scripts.suggest_tree_algorithm_labels.model import Suggestion
from knowledge_base.tree.validation import TreeIssue, validate_tree


def metadata_algorithm_counts(metadata_root: Path) -> Counter[str]:
    counts: Counter[str] = Counter()
    for metadata_path in sorted(metadata_root.rglob("metadata.yml")):
        data = load_metadata(metadata_path)
        algorithm = clean_text(data.get("algorithm"))
        if algorithm:
            counts[" ".join(words(algorithm))] += 1
    return counts


def make_suggestion(
    issue: TreeIssue,
    data: dict[str, Any],
    *,
    algorithm_count: int,
) -> Suggestion:
    tree_label = clean_text(issue.tree_label)
    algorithm = clean_text(issue.algorithm)
    title = clean_text(data.get("title"))
    audit_status = clean_text(data.get("audit_status")) or "<none>"
    metadata_path = issue.metadata_path or Path()

    alias_reason = soft_equivalence_reason(tree_label, algorithm)
    if alias_reason is not None:
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_ACCEPT_ALIAS,
            confidence=CONFIDENCE_HIGH,
            suggested_tree_label=None,
            suggested_metadata_algorithm=None,
            canonical_label=algorithm,
            reason=alias_reason,
        )

    if algorithm_looks_invalid(algorithm):
        replacement = title_head(title) or tree_label
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_UPDATE_METADATA,
            confidence=CONFIDENCE_HIGH,
            suggested_tree_label=None,
            suggested_metadata_algorithm=replacement,
            canonical_label=replacement,
            reason="Metadata algorithm looks generic, empty, too short, or like a part number.",
        )

    audit_replacement = audit_suggested_algorithm(data, metadata_path)
    if audit_replacement is not None:
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_UPDATE_METADATA,
            confidence=CONFIDENCE_MEDIUM,
            suggested_tree_label=None,
            suggested_metadata_algorithm=audit_replacement,
            canonical_label=audit_replacement,
            reason=(
                "Existing metadata audit says the algorithm field names an "
                "existing method rather than this paper's contribution."
            ),
        )

    duplicate_method = algorithm_count > 1
    broad_duplicate = duplicate_method and not is_code_like(algorithm)
    strong_method_signal = (
        is_code_like(algorithm) or algorithm_in_tags(algorithm, data) or text_introduces_algorithm(algorithm, data)
    ) and algorithm_in_metadata_text(algorithm, data)

    if duplicate_method and strong_method_signal:
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_REVIEW,
            confidence=CONFIDENCE_LOW,
            suggested_tree_label=None,
            suggested_metadata_algorithm=None,
            canonical_label=algorithm,
            reason=(
                f"Metadata algorithm is used by {algorithm_count} papers; "
                "the Tree label may intentionally disambiguate this item."
            ),
        )

    if audit_status == "reviewed" and strong_method_signal:
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_UPDATE_TREE,
            confidence=CONFIDENCE_HIGH,
            suggested_tree_label=algorithm,
            suggested_metadata_algorithm=None,
            canonical_label=algorithm,
            reason="Reviewed metadata has a strong method-name signal.",
        )

    if alnum_key(tree_label) == alnum_key(title) and strong_method_signal:
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_UPDATE_TREE,
            confidence=CONFIDENCE_MEDIUM,
            suggested_tree_label=algorithm,
            suggested_metadata_algorithm=None,
            canonical_label=algorithm,
            reason=(
                "Tree label is the paper title, while metadata contains a "
                "method-like algorithm mentioned in the metadata text."
            ),
        )

    if is_code_like(tree_label) and not is_code_like(algorithm):
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_UPDATE_METADATA,
            confidence=CONFIDENCE_MEDIUM,
            suggested_tree_label=None,
            suggested_metadata_algorithm=tree_label,
            canonical_label=tree_label,
            reason="Tree label is a compact code-like method name and metadata is expanded or descriptive.",
        )

    if clean_text(tree_label).casefold() in clean_text(algorithm).casefold():
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_UPDATE_METADATA,
            confidence=CONFIDENCE_MEDIUM,
            suggested_tree_label=None,
            suggested_metadata_algorithm=tree_label,
            canonical_label=tree_label,
            reason="Metadata algorithm wraps the existing Tree label in extra descriptive words.",
        )

    if broad_duplicate:
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_REVIEW,
            confidence=CONFIDENCE_LOW,
            suggested_tree_label=None,
            suggested_metadata_algorithm=None,
            canonical_label=None,
            reason=(
                f"Metadata algorithm is used by {algorithm_count} papers and is not a compact code-like method name."
            ),
        )

    if alnum_key(tree_label) == alnum_key(title) and not is_title_like(algorithm):
        return Suggestion(
            nav_path=issue.nav_path,
            tree_label=tree_label,
            algorithm=algorithm,
            title=title,
            audit_status=audit_status,
            source=issue.source or "",
            metadata_path=metadata_path,
            action=ACTION_REVIEW,
            confidence=CONFIDENCE_LOW,
            suggested_tree_label=None,
            suggested_metadata_algorithm=None,
            canonical_label=None,
            reason=(
                "Tree label is the paper title, but metadata algorithm is not strong enough to update automatically."
            ),
        )

    return Suggestion(
        nav_path=issue.nav_path,
        tree_label=tree_label,
        algorithm=algorithm,
        title=title,
        audit_status=audit_status,
        source=issue.source or "",
        metadata_path=metadata_path,
        action=ACTION_REVIEW,
        confidence=CONFIDENCE_LOW,
        suggested_tree_label=None,
        suggested_metadata_algorithm=None,
        canonical_label=None,
        reason="No conservative rule could choose a canonical label.",
    )


def collect_suggestions(tree_path: Path, metadata_root: Path) -> list[Suggestion]:
    algorithm_counts = metadata_algorithm_counts(metadata_root)
    report = validate_tree(
        tree_path,
        metadata_root=metadata_root,
        check_algorithm_labels=True,
    )
    suggestions: list[Suggestion] = []
    for issue in report.issues:
        if issue.code != "algorithm-label-mismatch" or issue.metadata_path is None:
            continue
        data = load_metadata(issue.metadata_path)
        algorithm_key = " ".join(words(clean_text(issue.algorithm)))
        suggestions.append(
            make_suggestion(
                issue,
                data,
                algorithm_count=algorithm_counts.get(algorithm_key, 0),
            )
        )
    return suggestions


__all__ = ["collect_suggestions", "make_suggestion", "metadata_algorithm_counts"]
