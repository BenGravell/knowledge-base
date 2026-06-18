"""Generated docs writer used by the Zensical build wrapper."""

from __future__ import annotations

import os
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path, PurePosixPath
from typing import IO

GENERATED_DOCS_DIR_ENV = "KB_GENERATED_DOCS_DIR"


def _staged_path(name: str | Path) -> Path | None:
    root = os.environ.get(GENERATED_DOCS_DIR_ENV)
    if not root:
        return None

    relative = PurePosixPath(str(name))
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError(f"Generated path must stay under docs_dir: {name}")
    return Path(root).resolve().joinpath(*relative.parts)


@contextmanager
def open_generated(
    name: str | Path,
    mode: str,
    buffering: int = -1,
    encoding: str | None = None,
    *args: object,
    **kwargs: object,
) -> Iterator[IO]:
    staged = _staged_path(name)
    if staged is None:
        raise RuntimeError("Generated files must be written through `kb build` or `kb serve`.")

    staged.parent.mkdir(parents=True, exist_ok=True)
    open_kwargs = dict(kwargs)
    if "b" not in mode and encoding is None:
        encoding = "utf-8"
    if encoding is not None:
        open_kwargs["encoding"] = encoding
    with staged.open(mode, buffering, *args, **open_kwargs) as out:
        yield out


def set_edit_path(name: str | Path, edit_name: str | Path | None) -> None:
    _ = (name, edit_name)
