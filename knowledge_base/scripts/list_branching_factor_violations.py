"""List Tree branches whose immediate child count is outside guidance.

Usage:
  python scripts/list_branching_factor_violations.py
  python scripts/list_branching_factor_violations.py --count branches
  python scripts/list_branching_factor_violations.py --max-depth 2
  python scripts/list_branching_factor_violations.py --format json
  python scripts/list_branching_factor_violations.py --ignore-too-few
  python scripts/list_branching_factor_violations.py --fail-on-violations
"""

from __future__ import annotations

import argparse
import sys
from typing import Any

from knowledge_base.components.tree.model import TreeModel
from knowledge_base.components.tree.nav_source import load_tree
from knowledge_base.scripts.branching_factor_violations.model import Branch, CountMode, Violation
from knowledge_base.scripts.branching_factor_violations.output import format_path, print_json, print_markdown


def collect_branches(nav: Any, *, include_root: bool) -> list[Branch]:
    model = TreeModel.from_tree(nav)
    return [model.root, *model.branches] if include_root else list(model.branches)


def find_violations(
    branches: list[Branch],
    *,
    mode: CountMode,
    minimum: int,
    maximum: int,
    sweet_spot: int,
    check_too_few: bool,
) -> list[Violation]:
    violations: list[Violation] = []
    for branch in branches:
        count = branch.count_for(mode)
        if check_too_few and count < minimum:
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


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "List Tree branches whose immediate child count is below or above the taxonomy branching-factor guidance."
        )
    )
    parser.add_argument(
        "--min",
        dest="minimum",
        type=int,
        default=2,
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
        "--ignore-too-few",
        action="store_true",
        help="Do not report branches with fewer than --min children.",
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
        help=("Only audit branches through depth N. Tree is depth 0, top-level categories are depth 1."),
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
        branches = [branch for branch in branches if branch.depth <= args.max_depth]
    violations = find_violations(
        branches,
        mode=args.count,
        minimum=args.minimum,
        maximum=args.maximum,
        sweet_spot=args.sweet_spot,
        check_too_few=not args.ignore_too_few,
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
            check_too_few=not args.ignore_too_few,
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
            check_too_few=not args.ignore_too_few,
            show_children=args.show_children,
        )
        if args.max_results is not None and len(violations) > len(display):
            print(f"{len(violations) - len(display)} more violation(s) not shown.")

    if args.fail_on_violations and violations:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
