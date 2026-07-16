from __future__ import annotations

import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
KB_DIR = REPO_ROOT / "knowledge_base"
IGNORED_TEST_DIRS = {"__pycache__", ".generated", "docs", "site"}


def module_name(path: Path) -> str:
    return ".".join(path.relative_to(REPO_ROOT).with_suffix("").parts)


def is_test_path(path: Path) -> bool:
    return path.suffix == ".py" and path.name.endswith("_test.py")


def all_test_modules() -> list[str]:
    return sorted(
        module_name(path)
        for path in KB_DIR.rglob("*_test.py")
        if IGNORED_TEST_DIRS.isdisjoint(path.relative_to(KB_DIR).parts)
    )


def selected_test_modules(paths: list[str]) -> list[str]:
    tests = set()
    saw_python = False

    for raw_path in paths:
        path = (REPO_ROOT / raw_path).resolve()
        if path.suffix != ".py":
            continue

        saw_python = True
        if is_test_path(path):
            tests.add(module_name(path))
            continue

        adjacent_test = path.with_name(f"{path.stem}_test.py")
        if adjacent_test.is_file():
            tests.add(module_name(adjacent_test))
            continue

        return all_test_modules()

    if not saw_python or not tests:
        return all_test_modules()
    return sorted(tests)


def main(argv: list[str] | None = None) -> int:
    modules = selected_test_modules(list(sys.argv[1:] if argv is None else argv))
    suite = unittest.defaultTestLoader.loadTestsFromNames(modules)
    result = unittest.TextTestRunner(buffer=True).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
