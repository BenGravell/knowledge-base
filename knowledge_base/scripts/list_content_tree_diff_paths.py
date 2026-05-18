"""Print paper metadata paths touched by the content tree git diff.

The default output is absolute paths, which most IDE terminals render as
clickable file links.

Usage:
  python scripts/list_content_tree_diff_paths.py
  python scripts/list_content_tree_diff_paths.py --relative
  python scripts/list_content_tree_diff_paths.py --staged
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


KB_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = KB_DIR.parent
CONTENT_TREE = KB_DIR / "content_tree.yml"
CONTENT_TREE_FROM_REPO = CONTENT_TREE.relative_to(REPO_ROOT)
METADATA_PATH_RE = re.compile(r"\bdocs/papers/[^\s,'\"]+/metadata\.yml\b")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print metadata.yml paths touched by git diff in content_tree.yml."
    )
    parser.add_argument(
        "--relative",
        action="store_true",
        help="Print paths relative to knowledge_base/ instead of absolute paths.",
    )
    parser.add_argument(
        "--staged",
        action="store_true",
        help="Read the staged diff instead of the unstaged working-tree diff.",
    )
    parser.add_argument(
        "--added-only",
        action="store_true",
        help="Only print paths from added diff lines.",
    )
    parser.add_argument(
        "--removed-only",
        action="store_true",
        help="Only print paths from removed diff lines.",
    )
    return parser.parse_args()


def git_diff(staged: bool) -> str:
    cmd = ["git", "-C", str(REPO_ROOT), "diff"]
    if staged:
        cmd.append("--staged")
    cmd.extend(["--", str(CONTENT_TREE_FROM_REPO)])
    try:
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        print(exc.stderr, file=sys.stderr, end="")
        raise SystemExit(exc.returncode) from exc
    return result.stdout


def changed_metadata_paths(diff_text: str, *, added: bool, removed: bool) -> list[str]:
    paths: list[str] = []
    seen: set[str] = set()

    for line in diff_text.splitlines():
        if line.startswith("+++") or line.startswith("---"):
            continue

        is_added = line.startswith("+")
        is_removed = line.startswith("-")
        if not is_added and not is_removed:
            continue
        if added and not is_added:
            continue
        if removed and not is_removed:
            continue

        for match in METADATA_PATH_RE.finditer(line):
            path = match.group(0)
            if path not in seen:
                paths.append(path)
                seen.add(path)

    return paths


def main() -> int:
    args = parse_args()
    if args.added_only and args.removed_only:
        print("--added-only and --removed-only are mutually exclusive", file=sys.stderr)
        return 2

    paths = changed_metadata_paths(
        git_diff(args.staged),
        added=args.added_only,
        removed=args.removed_only,
    )
    for path in paths:
        print(path if args.relative else KB_DIR / path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
