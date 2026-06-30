"""Cache and HTTP helpers for metadata refinement."""

from __future__ import annotations

import json
import time
from typing import Any

import requests

from knowledge_base.scripts.refine_staged_arxiv_metadata.constants import CACHE_PATH

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "knowledge-base metadata audit (mailto:none)"})


def load_cache() -> dict[str, Any]:
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    return {}


def save_cache(cache: dict[str, Any]) -> None:
    CACHE_PATH.write_text(json.dumps(cache, sort_keys=True), encoding="utf-8")


def fetch_json(cache: dict[str, Any], key: str, url: str) -> dict[str, Any]:
    if key in cache:
        return cache[key]
    response = SESSION.get(url, timeout=60)
    if response.status_code == 404:
        cache[key] = {}
    else:
        response.raise_for_status()
        cache[key] = response.json()
    save_cache(cache)
    time.sleep(0.25)
    return cache[key]
