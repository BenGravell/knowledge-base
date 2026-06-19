from __future__ import annotations

import os
import shlex
import shutil
import subprocess
import sys
import time
from collections.abc import Callable
from pathlib import Path

import yaml

from knowledge_base.generated_assets import render_app_script_blocks

REPO_ROOT = Path(__file__).resolve().parent.parent
KB_DIR = Path(__file__).resolve().parent
SOURCE_DOCS_DIR = KB_DIR / "docs"
STAGED_DOCS_DIR = KB_DIR / ".generated" / "docs"
ZENSICAL_CONFIG = KB_DIR / ".zensical.generated.yml"
ZENSICAL_SOURCE_CONFIG = KB_DIR / "zensical.yml"
GENERATED_DOCS_DIR_ENV = "KB_GENERATED_DOCS_DIR"

GENERATED_FILE_SCRIPTS = (
    ("paper pages and search data", KB_DIR / "generate_papers.py"),
    ("map assets", KB_DIR / "map" / "copy_assets.py"),
    ("semantic search assets", KB_DIR / "semantic_search" / "copy_assets.py"),
    ("tree, analytics, and timeline data", KB_DIR / "tree" / "generate_tree_data.py"),
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


def rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def log(message: str) -> None:
    print(f"kb: {message}", file=sys.stderr, flush=True)


def elapsed_text(start: float) -> str:
    return f"{time.perf_counter() - start:.1f}s"


def run_step(label: str, action: Callable[[], object]) -> None:
    start = time.perf_counter()
    log(f"{label}...")
    try:
        action()
    except Exception:
        log(f"{label} failed after {elapsed_text(start)}")
        raise
    log(f"{label} done in {elapsed_text(start)}")


def copy_docs_ignore(directory: str, names: list[str]) -> set[str]:
    ignored = {"__pycache__"} & set(names)
    if Path(directory) == SOURCE_DOCS_DIR and "papers" in names:
        ignored.add("papers")
    if Path(directory) == SOURCE_DOCS_DIR and "templates" in names:
        ignored.add("templates")
    return ignored


def write_zensical_config() -> None:
    config = yaml.safe_load(ZENSICAL_SOURCE_CONFIG.read_text(encoding="utf-8"))
    if not isinstance(config, dict):
        raise RuntimeError(f"{rel(ZENSICAL_SOURCE_CONFIG)} must contain a mapping")

    config["docs_dir"] = ".generated/docs"

    ZENSICAL_CONFIG.write_text(yaml.safe_dump(config, sort_keys=False), encoding="utf-8")


def render_staged_app_script_blocks() -> None:
    for path in STAGED_DOCS_DIR.rglob("*.md"):
        source = path.read_text(encoding="utf-8")
        rendered = render_app_script_blocks(source, path.relative_to(STAGED_DOCS_DIR).as_posix())
        if rendered != source:
            path.write_text(rendered, encoding="utf-8")


def materialize_generated_docs() -> None:
    log(f"preparing {rel(STAGED_DOCS_DIR)}")
    if STAGED_DOCS_DIR.exists():
        run_step(f"clear {rel(STAGED_DOCS_DIR)}", lambda: shutil.rmtree(STAGED_DOCS_DIR))
    run_step(
        f"copy {rel(SOURCE_DOCS_DIR)} to {rel(STAGED_DOCS_DIR)}",
        lambda: shutil.copytree(SOURCE_DOCS_DIR, STAGED_DOCS_DIR, ignore=copy_docs_ignore),
    )
    run_step("render app script blocks", render_staged_app_script_blocks)
    run_step(f"write {rel(ZENSICAL_CONFIG)}", write_zensical_config)

    env = os.environ.copy()
    env[GENERATED_DOCS_DIR_ENV] = str(STAGED_DOCS_DIR)
    for label, script in GENERATED_FILE_SCRIPTS:
        script_path = rel(script)
        command = (sys.executable, script_path)
        run_step(
            f"generate {label} ({script_path})",
            lambda command=command: subprocess.run(command, cwd=REPO_ROOT, env=env, check=True),
        )


def run_zensical(command: str, args: list[str]) -> int:
    materialize_generated_docs()
    command_line = (executable("zensical"), command, "-f", rel(ZENSICAL_CONFIG), *args)
    start = time.perf_counter()
    log(f"start {shlex.join(command_line)}")
    result = subprocess.call(command_line)
    status = "finished" if result == 0 else f"exited with {result}"
    log(f"zensical {command} {status} after {elapsed_text(start)}")
    return result


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
