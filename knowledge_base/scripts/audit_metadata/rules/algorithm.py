"""Algorithm-label validation rules for metadata audits."""

from pathlib import Path
from typing import Any

from knowledge_base.scripts.audit_metadata.rules.algorithm_cues import (
    _algorithm_issue_cue,
    _broad_algorithm_family_issue_cue,
    _text_introduces_algorithm_label,
)
from knowledge_base.scripts.audit_metadata.rules.algorithm_data import _GENERIC_ALGORITHM_VALUES
from knowledge_base.scripts.audit_metadata.rules.algorithm_labels import (
    _algorithm_context_text,
    _algorithm_label_is_allowed_entry,
    _algorithm_label_is_bare_method_name,
    _algorithm_label_is_broad_family_name,
    _algorithm_label_is_known_origin_entry,
    _text_mentions_algorithm,
)
from knowledge_base.scripts.audit_metadata.support.model import Issue, Severity


def find_algorithm_issues(path: Path, data: dict[str, Any]) -> list["Issue"]:
    algorithm = str(data.get("algorithm") or "").strip()
    if not algorithm:
        return []

    folded = algorithm.casefold()
    if folded in _GENERIC_ALGORITHM_VALUES:
        return [
            Issue(
                path,
                "algorithm",
                f"Generic algorithm label: {algorithm!r}",
                "Leave algorithm blank unless the paper gives a specific method, system, or technique name.",
            )
        ]

    title, context = _algorithm_context_text(data)
    if _algorithm_label_is_allowed_entry(path, data, algorithm):
        return []

    if _algorithm_label_is_known_origin_entry(path, data, algorithm):
        return []

    is_broad_family_name = _algorithm_label_is_broad_family_name(algorithm)
    is_bare_method_name = _algorithm_label_is_bare_method_name(algorithm)
    if not is_broad_family_name and not is_bare_method_name:
        return []

    mentions_algorithm = _text_mentions_algorithm(algorithm, context)

    broad_family_cue = (
        _broad_algorithm_family_issue_cue(
            algorithm,
            title,
            context,
            mentions_algorithm=mentions_algorithm,
        )
        if is_broad_family_name
        else None
    )
    if broad_family_cue is not None:
        return [
            Issue(
                path,
                "algorithm",
                (f"Overly broad algorithm label {algorithm!r} appears to describe {broad_family_cue}"),
                ("Use the paper's specific method, variant, or contribution phrase instead of the broad family name."),
                severity=Severity.WARNING,
            )
        ]

    if not is_bare_method_name or not mentions_algorithm:
        return []

    if _text_introduces_algorithm_label(algorithm, title, context):
        return []

    cue = _algorithm_issue_cue(algorithm, title, context, mentions_algorithm=mentions_algorithm)
    if cue is not None:
        reason, suggested_label = cue
        return [
            Issue(
                path,
                "algorithm",
                f"Bare algorithm label {algorithm!r} appears to be {reason}, not the original proposing paper",
                (f"Use a descriptive contribution phrase instead, for example {suggested_label!r}."),
                severity=Severity.WARNING,
            )
        ]

    return []
