from __future__ import annotations

import os
import signal
import sys
import time
import unittest
from collections.abc import Generator
from contextlib import contextmanager
from pathlib import Path
from types import FrameType

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
    stream = sys.stderr
    started = time.perf_counter()
    phase_name = "startup"
    phase_started = started

    def report(message: str) -> None:
        print(f"unit-tests: {message}", file=stream, flush=True)

    @contextmanager
    def phase(name: str) -> Generator[None]:
        nonlocal phase_name, phase_started
        phase_name, phase_started = name, time.perf_counter()
        report(f"{name} started")
        try:
            yield
        finally:
            report(f"{name}: {time.perf_counter() - phase_started:.3f}s")

    def timed_out(_signum: int, _frame: FrameType | None) -> None:
        report(f"TIMEOUT during {phase_name}: {time.perf_counter() - phase_started:.3f}s")
        report(f"Python runner total: {time.perf_counter() - started:.3f}s")
        # unittest catches SystemExit; terminate immediately to preserve the hook's deadline.
        os._exit(124)

    previous_handler = signal.signal(signal.SIGTERM, timed_out)
    try:
        if hook_started := os.environ.get("KB_TEST_STARTED_AT"):
            report(f"environment and Python startup: {time.time() - float(hook_started):.3f}s")
        with phase("test selection"):
            modules = selected_test_modules(list(sys.argv[1:] if argv is None else argv))
        report(f"selected {len(modules)} module(s)")
        suite = unittest.TestSuite()
        for module in modules:
            with phase(f"load {module}"):
                suite.addTests(unittest.defaultTestLoader.loadTestsFromName(module))
        with phase("test execution"):
            result = unittest.TextTestRunner(stream=stream, buffer=True, verbosity=2).run(suite)
        return 0 if result.wasSuccessful() else 1
    finally:
        report(f"Python runner total: {time.perf_counter() - started:.3f}s")
        signal.signal(signal.SIGTERM, previous_handler)


if __name__ == "__main__":
    raise SystemExit(main())
