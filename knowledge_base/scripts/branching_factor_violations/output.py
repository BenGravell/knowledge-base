"""Output helpers for branching-factor audits."""

from __future__ import annotations

import json

from knowledge_base.scripts.branching_factor_violations.model import Branch, CountMode, Violation


def display_path(path: tuple[str, ...]) -> tuple[str, ...]:
    return path if path == ("Tree",) else ("Tree", *path)


def format_path(path: tuple[str, ...]) -> str:
    return " > ".join(display_path(path))


def child_labels(branch: Branch, *, show_children: int) -> list[str]:
    if show_children <= 0:
        return []
    labels = [child.label for child in branch.children[:show_children]]
    remaining = len(branch.children) - len(labels)
    if remaining > 0:
        labels.append(f"... {remaining} more")
    return labels


def print_markdown(
    violations: list[Violation],
    *,
    branch_count: int,
    total_violation_count: int,
    max_depth: int | None,
    mode: CountMode,
    minimum: int,
    maximum: int,
    sweet_spot: int,
    check_too_few: bool,
    show_children: int,
) -> None:
    print("# Tree Branching Factor Violations\n")
    count_label = "branches" if mode == "branches" else "items"
    if check_too_few:
        print(f"Guidance: {minimum} to {maximum} direct child {count_label}; sweet spot {sweet_spot}.")
    else:
        print(f"Guidance: at most {maximum} direct child {count_label}; sweet spot {sweet_spot}.")
        print("Too-few check: disabled.")
    print(f"Counting mode: `{mode}`.")
    if max_depth is not None:
        print(f"Depth filter: through depth {max_depth}, counting `Tree` as depth 0.")
    print(f"{total_violation_count} violating branch(es) out of {branch_count} audited.\n")

    for reason in ("too many", "too few"):
        group = [violation for violation in violations if violation.reason == reason]
        if not group:
            continue
        print(f"## {reason.title()}\n")
        for violation in group:
            branch = violation.branch
            print(
                f"- `{format_path(branch.path)}`: {violation.count} "
                f"({'sub-branches' if mode == 'branches' else 'children'}; "
                f"{branch.branch_count} branches, {branch.leaf_count} leaves)"
            )
            labels = child_labels(branch, show_children=show_children)
            if labels:
                print(f"  - Children: {', '.join(labels)}")
        print()


def print_json(
    violations: list[Violation],
    *,
    branch_count: int,
    total_violation_count: int,
    max_depth: int | None,
    mode: CountMode,
    minimum: int,
    maximum: int,
    sweet_spot: int,
    check_too_few: bool,
) -> None:
    payload = {
        "guidance": {
            "min": minimum,
            "max": maximum,
            "sweet_spot": sweet_spot,
            "count_mode": mode,
            "max_depth": max_depth,
            "check_too_few": check_too_few,
        },
        "audited_branch_count": branch_count,
        "violation_count": total_violation_count,
        "displayed_violation_count": len(violations),
        "violations": [
            {
                "path": list(display_path(violation.branch.path)),
                "count": violation.count,
                "reason": violation.reason,
                "branch_count": violation.branch.branch_count,
                "leaf_count": violation.branch.leaf_count,
                "distance_from_sweet_spot": violation.distance_from_sweet_spot,
                "children": [{"label": child.label, "kind": child.kind} for child in violation.branch.children],
            }
            for violation in violations
        ],
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False))


__all__ = ["child_labels", "display_path", "format_path", "print_json", "print_markdown"]
