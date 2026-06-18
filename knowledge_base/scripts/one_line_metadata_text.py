"""Put metadata abstract and summary values on one YAML line.

The script rewrites only the `abstract` and `summary` fields in metadata.yml
files. It parses each file with PyYAML to get the field value, collapses
internal whitespace to single spaces, and replaces the original YAML scalar
with a single-line scalar.
"""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path
from typing import Any

import yaml

from knowledge_base.config import KB_DIR

TEXT_FIELDS = ("abstract", "summary")


def collapse_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def scalar_line(key: str, value: str) -> str:
    if not value:
        return f"{key}:"
    return yaml.safe_dump(
        {key: value},
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=1_000_000_000,
    ).strip()


def replace_field(raw: str, key: str, value: str) -> str:
    lines = raw.splitlines(keepends=True)
    start = None
    indent = ""
    for idx, line in enumerate(lines):
        match = re.match(rf"^(\s*){re.escape(key)}\s*:", line)
        if match:
            start = idx
            indent = match.group(1)
            break
    if start is None:
        return raw

    end = start + 1
    while end < len(lines):
        line = lines[end]
        if line.strip() and not line.startswith((" ", "\t")):
            break
        end += 1

    replacement = f"{indent}{scalar_line(key, value)}\n"
    return "".join([*lines[:start], replacement, *lines[end:]])


def process_file(path: Path, *, check: bool = False) -> bool:
    raw = path.read_text(encoding="utf-8")
    data = yaml.safe_load(raw) or {}
    new_raw = raw
    for key in TEXT_FIELDS:
        if key in data:
            new_raw = replace_field(new_raw, key, collapse_text(data.get(key)))

    changed = new_raw != raw
    if changed and not check:
        path.write_text(new_raw, encoding="utf-8")
    return changed


def staged_metadata_files() -> list[Path]:
    output = subprocess.check_output(
        ["git", "diff", "--cached", "--name-only", "--", "knowledge_base/docs/papers/**/metadata.yml"],
        text=True,
    )
    return [Path(line) for line in output.splitlines() if line.strip()]


def all_metadata_files() -> list[Path]:
    return sorted((KB_DIR / "docs" / "papers").rglob("metadata.yml"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--staged", action="store_true", help="Process metadata files currently staged in git.")
    scope.add_argument("--all", action="store_true", help="Process every paper metadata.yml file.")
    parser.add_argument("--check", action="store_true", help="Exit non-zero if any file would change.")
    parser.add_argument("paths", nargs="*", type=Path, help="Specific metadata.yml files to process.")
    args = parser.parse_args()

    if args.paths:
        paths = args.paths
    elif args.staged:
        paths = staged_metadata_files()
    else:
        paths = all_metadata_files()

    changed = [path for path in paths if process_file(path, check=args.check)]
    action = "would change" if args.check else "updated"
    print(f"{len(changed)} file(s) {action} out of {len(paths)} checked.")
    if args.check and changed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
