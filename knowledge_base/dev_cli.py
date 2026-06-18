from __future__ import annotations

import subprocess
import sys
from pathlib import Path


COMMANDS: dict[str, tuple[str, ...]] = {
    "serve": ("mkdocs", "serve", "-f", "knowledge_base/mkdocs.yml"),
    "build": ("mkdocs", "build", "-f", "knowledge_base/mkdocs.yml"),
    "deploy": ("mkdocs", "gh-deploy", "-f", "knowledge_base/mkdocs.yml"),
    "refresh": ("python", "knowledge_base/scripts/refresh_offline_data.py"),
    "test": ("python", "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"),
    "lint": ("ruff", "check", "knowledge_base", "tests"),
    "format-check": ("ruff", "format", "--check", "knowledge_base", "tests"),
    "typecheck": ("pyrefly", "check"),
}


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in {"-h", "--help"}:
        names = ", ".join(sorted(COMMANDS))
        print(f"usage: kb <command> [args...]\n\ncommands: {names}")
        return 0

    name = args.pop(0)
    command = COMMANDS.get(name)
    if command is None:
        print(f"unknown command: {name}", file=sys.stderr)
        return 2
    executable = sys.executable if command[0] == "python" else str(Path(sys.executable).parent / command[0])
    return subprocess.call((executable, *command[1:], *args))


if __name__ == "__main__":
    raise SystemExit(main())
