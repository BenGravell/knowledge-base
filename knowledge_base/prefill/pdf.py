"""PDF text extraction for prefill handlers."""

from __future__ import annotations

import subprocess
import tempfile

import requests


def pdf_text_from_url(url: str, *, first_pages: int = 2) -> str:
    """Download a PDF URL and extract leading text using pdftotext."""
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    with tempfile.NamedTemporaryFile(suffix=".pdf") as tmp:
        tmp.write(response.content)
        tmp.flush()
        proc = subprocess.run(
            ["pdftotext", "-f", "1", "-l", str(first_pages), tmp.name, "-"],
            check=True,
            capture_output=True,
            text=True,
        )
    return proc.stdout
