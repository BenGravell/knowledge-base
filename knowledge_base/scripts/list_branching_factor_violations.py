
"""List Tree branches whose immediate child count is outside guidance.

Usage:
  python scripts/list_branching_factor_violations.py
  python scripts/list_branching_factor_violations.py --count branches
  python scripts/list_branching_factor_violations.py --max-depth 2
  python scripts/list_branching_factor_violations.py --format json
  python scripts/list_branching_factor_violations.py --fail-on-violations
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from knowledge_base.tree.nav_source import load_tree  # noqa: E402


LANDING_PAGES = {"tree.md", "tree/index.md"}
CountMode = Literal["all", "branches"]


@dataclass(frozen=True)
class Child:
    label: str
    kind: Literal["branch", "leaf"]


@dataclass(frozen=True)
class Branch:
    path: tuple[str, ...]
    children: tuple[Child, ...]

    @property
    def branch_count(self) -> int:
        return sum(1 for child in self.children if child.kind == "branch")

    @property
    def leaf_count(self) -> int:
        return sum(1 for child in self.children if child.kind == "leaf")

    def count_for(self, mode: CountMode) -> int:
        if mode == "branches":
            return self.branch_count
        return len(self.children)


@dataclass(frozen=True)
class Violation:
    branch: Branch
    count: int
    reason: Literal["too few", "too many"]
    distance_from_sweet_spot: int


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def leaf_label(source: str) -> str:
    return source.removesuffix(".md").replace("-", " ").replace("_", " ").title()


def is_landing_item(label: str, child: Any) -> bool:
    return isinstance(child, str) and (
        child in LANDING_PAGES
        or (label.strip().lower() == "overview" and child in LANDING_PAGES)
    )


def collect_branches(nav: Any, *, include_root: bool) -> list[Branch]:
    branches: list[Branch] = []

    def walk(items: list[Any], path: tuple[str, ...]) -> tuple[Child, ...]:
        children: list[Child] = []
        for item in items:
            if isinstance(item, str):
                if item in LANDING_PAGES:
                    continue
                children.append(Child(label=leaf_label(item), kind="leaf"))
                continue

            if not isinstance(item, dict):
                continue

            for raw_label, child in item.items():
                label = str(raw_label)
                if is_landing_item(label, child):
                    continue
                if isinstance(child, list):
                    child_path = path + (label,)
                    branch_children = walk(child, child_path)
                    branches.append(Branch(path=child_path, children=branch_children))
                    children.append(Child(label=label, kind="branch"))
                elif isinstance(child, str):
                    children.append(Child(label=label, kind="leaf"))

        return tuple(children)

    root_children = walk(as_list(nav), ("Tree",))
    if include_root:
        branches.append(Branch(path=("Tree",), children=root_children))
    return branches


def find_violations(
    branches: list[Branch],
    *,
    mode: CountMode,
    minimum: int,
    maximum: int,
    sweet_spot: int,
) -> list[Violation]:
    violations: list[Violation] = []
    for branch in branches:
        count = branch.count_for(mode)
        if count < minimum:
            violations.append(
                Violation(
                    branch=branch,
                    count=count,
                    reason="too few",
                    distance_from_sweet_spot=abs(count - sweet_spot),
                )
            )
        elif count > maximum:
            violations.append(
                Violation(
                    branch=branch,
                    count=count,
                    reason="too many",
                    distance_from_sweet_spot=abs(count - sweet_spot),
                )
            )
    return violations


def format_path(path: tuple[str, ...]) -> str:
    return " > ".join(path)


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
    show_children: int,
) -> None:
    print("# Tree Branching Factor Violations\n")
    print(
        f"Guidance: {minimum} to {maximum} direct child "
        f"{'branches' if mode == 'branches' else 'items'}; sweet spot {sweet_spot}."
    )
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
) -> None:
    payload = {
        "guidance": {
            "min": minimum,
            "max": maximum,
            "sweet_spot": sweet_spot,
            "count_mode": mode,
            "max_depth": max_depth,
        },
        "audited_branch_count": branch_count,
        "violation_count": total_violation_count,
        "displayed_violation_count": len(violations),
        "violations": [
            {
                "path": list(violation.branch.path),
                "count": violation.count,
                "reason": violation.reason,
                "branch_count": violation.branch.branch_count,
                "leaf_count": violation.branch.leaf_count,
                "distance_from_sweet_spot": violation.distance_from_sweet_spot,
                "children": [
                    {"label": child.label, "kind": child.kind}
                    for child in violation.branch.children
                ],
            }
            for violation in violations
        ],
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False))


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "List Tree branches whose immediate child count is below "
            "or above the taxonomy branching-factor guidance."
        )
    )
    parser.add_argument(
        "--min",
        dest="minimum",
        type=int,
        default=3,
        help="Minimum acceptable branching factor.",
    )
    parser.add_argument(
        "--max",
        dest="maximum",
        type=int,
        default=7,
        help="Maximum acceptable branching factor.",
    )
    parser.add_argument(
        "--sweet-spot",
        type=int,
        default=5,
        help="Preferred branching factor used for sorting by severity.",
    )
    parser.add_argument(
        "--count",
        choices=("all", "branches"),
        default="all",
        help="Count all direct children or only direct sub-branches.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json", "paths"),
        default="markdown",
        help="Output format.",
    )
    parser.add_argument(
        "--show-children",
        type=int,
        default=8,
        metavar="N",
        help="Show up to N direct child labels for each markdown result. Use 0 to hide.",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=None,
        metavar="N",
        help=(
            "Only audit branches through depth N. "
            "Tree is depth 0, top-level categories are depth 1."
        ),
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=None,
        metavar="N",
        help="Limit the number of violations displayed.",
    )
    parser.add_argument(
        "--exclude-root",
        action="store_true",
        help="Do not audit the synthetic Tree root branch.",
    )
    parser.add_argument(
        "--fail-on-violations",
        action="store_true",
        help="Exit with status 1 when any violations are found.",
    )
    args = parser.parse_args()

    if args.minimum < 0 or args.maximum < 0:
        sys.exit("--min and --max must be non-negative.")
    if args.minimum > args.maximum:
        sys.exit("--min cannot be greater than --max.")
    if args.max_depth is not None and args.max_depth < 0:
        sys.exit("--max-depth must be at least 0.")

    branches = collect_branches(load_tree(), include_root=not args.exclude_root)
    if args.max_depth is not None:
        branches = [branch for branch in branches if len(branch.path) - 1 <= args.max_depth]
    violations = find_violations(
        branches,
        mode=args.count,
        minimum=args.minimum,
        maximum=args.maximum,
        sweet_spot=args.sweet_spot,
    )
    violations = sorted(
        violations,
        key=lambda violation: (
            violation.reason != "too many",
            -violation.distance_from_sweet_spot,
            format_path(violation.branch.path),
        ),
    )
    display = violations[: args.max_results] if args.max_results is not None else violations

    if args.format == "paths":
        for violation in display:
            print(f"{violation.count}\t{violation.reason}\t{format_path(violation.branch.path)}")
    elif args.format == "json":
        print_json(
            display,
            branch_count=len(branches),
            total_violation_count=len(violations),
            max_depth=args.max_depth,
            mode=args.count,
            minimum=args.minimum,
            maximum=args.maximum,
            sweet_spot=args.sweet_spot,
        )
    else:
        print_markdown(
            display,
            branch_count=len(branches),
            total_violation_count=len(violations),
            max_depth=args.max_depth,
            mode=args.count,
            minimum=args.minimum,
            maximum=args.maximum,
            sweet_spot=args.sweet_spot,
            show_children=args.show_children,
        )
        if args.max_results is not None and len(violations) > len(display):
            print(f"{len(violations) - len(display)} more violation(s) not shown.")

    if args.fail_on_violations and violations:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
