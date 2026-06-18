from __future__ import annotations

import os
import shutil
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
KB_DIR = Path(__file__).resolve().parent
SOURCE_DOCS_DIR = KB_DIR / "docs"
STAGED_DOCS_DIR = KB_DIR / ".generated" / "docs"
ZENSICAL_CONFIG = KB_DIR / ".zensical.generated.yml"
GENERATED_DOCS_DIR_ENV = "KB_GENERATED_DOCS_DIR"

GENERATED_FILE_SCRIPTS = (
    KB_DIR / "generate_papers.py",
    KB_DIR / "map" / "copy_assets.py",
    KB_DIR / "semantic_search" / "copy_assets.py",
    KB_DIR / "tree" / "generate_tree_data.py",
)


EXTERNAL_COMMANDS: dict[str, tuple[str, ...]] = {
    "refresh": ("python", "knowledge_base/scripts/refresh_offline_data.py"),
    "test": ("python", "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"),
    "lint": ("ruff", "check", "knowledge_base", "tests"),
    "format-check": ("ruff", "format", "--check", "knowledge_base", "tests"),
    "typecheck": ("pyrefly", "check"),
}


def executable(name: str) -> str:
    if name == "python":
        return sys.executable
    return str(Path(sys.executable).parent / name)


def copy_docs_ignore(directory: str, names: list[str]) -> set[str]:
    ignored = {"__pycache__"} & set(names)
    if Path(directory) == SOURCE_DOCS_DIR and "papers" in names:
        ignored.add("papers")
    return ignored


def write_zensical_config() -> None:
    config = yaml.safe_load((KB_DIR / "mkdocs.yml").read_text(encoding="utf-8"))
    if not isinstance(config, dict):
        raise RuntimeError("knowledge_base/mkdocs.yml must contain a mapping")

    config["docs_dir"] = ".generated/docs"
    theme = dict(config.get("theme") or {})
    theme["name"] = "zensical"
    config["theme"] = theme
    config["plugins"] = [{"macros": {"render_by_default": False}}]

    ZENSICAL_CONFIG.write_text(yaml.safe_dump(config, sort_keys=False), encoding="utf-8")


def materialize_generated_docs() -> None:
    if STAGED_DOCS_DIR.exists():
        shutil.rmtree(STAGED_DOCS_DIR)
    shutil.copytree(SOURCE_DOCS_DIR, STAGED_DOCS_DIR, ignore=copy_docs_ignore)
    write_zensical_config()

    env = os.environ.copy()
    env[GENERATED_DOCS_DIR_ENV] = str(STAGED_DOCS_DIR)
    for script in GENERATED_FILE_SCRIPTS:
        subprocess.run((sys.executable, str(script.relative_to(REPO_ROOT))), cwd=REPO_ROOT, env=env, check=True)


def run_zensical(command: str, args: list[str]) -> int:
    materialize_generated_docs()
    return subprocess.call((executable("zensical"), command, "-f", str(ZENSICAL_CONFIG.relative_to(REPO_ROOT)), *args))


CUSTOM_COMMANDS: dict[str, Callable[[list[str]], int]] = {
    "serve": lambda args: run_zensical("serve", args),
    "build": lambda args: run_zensical("build", args),
}


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in {"-h", "--help"}:
        names = ", ".join(sorted(EXTERNAL_COMMANDS | CUSTOM_COMMANDS))
        print(f"usage: kb <command> [args...]\n\ncommands: {names}")
        return 0

    name = args.pop(0)
    custom = CUSTOM_COMMANDS.get(name)
    if custom is not None:
        return custom(args)

    command = EXTERNAL_COMMANDS.get(name)
    if command is None:
        print(f"unknown command: {name}", file=sys.stderr)
        return 2
    return subprocess.call((executable(command[0]), *command[1:], *args))


if __name__ == "__main__":
    raise SystemExit(main())
