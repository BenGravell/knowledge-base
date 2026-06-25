"""Shared settings for arXiv full-text ingest."""

import shutil
import sys
from pathlib import Path

from knowledge_base.config import KB_DIR
from knowledge_base.utils.arxiv_utils import ARXIV_HEADERS

METADATA_ROOT = KB_DIR / "docs" / "papers"
SIDECAR_NAME = "embed_text.md"
DEFAULT_SLEEP_SECONDS = 3.0
MIN_MARKDOWN_CHARS = 1_000
MIN_BODY_CHARS = 500

HTML_HEADERS = {
    **ARXIV_HEADERS,
    "Accept": "text/html,application/xhtml+xml;q=0.9,*/*;q=0.8",
    "User-Agent": ARXIV_HEADERS["User-Agent"].replace("prefill", "full-text-ingest"),
}


def python_env_executable(name: str) -> str:
    return str(Path(sys.executable).with_name(name))


def executable_available(executable: str) -> bool:
    return shutil.which(executable) is not None
