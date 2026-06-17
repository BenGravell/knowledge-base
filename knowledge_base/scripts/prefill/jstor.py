"""Batch-prefill metadata.yml files from JSTOR stable URLs."""

import re
from collections.abc import Callable
from pathlib import Path
from typing import Any

from typing_extensions import override

if __package__ in (None, ""):
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[3]))

from knowledge_base.utils.prefill_template import REPO_ROOT, DoiPrefillScript
from knowledge_base.utils.prefill_utils import read_url_lines

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "JSTOR.md"

_STABLE_RE = re.compile(r"jstor\.org/stable/([^/?#\s]+)", re.I)
_DOI_BY_STABLE_ID = {
    "2238545": "10.1214/aoms/1177703591",
    "23358653": "10.1287/moor.1120.0566",
    "43633451": "10.1090/qam/10666",
    "43633461": "10.1090/qam/10667",
}


def doi_for_stable_id(stable_id: str) -> str:
    return _DOI_BY_STABLE_ID.get(stable_id, f"10.2307/{stable_id}")


def extract_entries(path: Path, on_parse_failure: Callable[[str], None] | None = None) -> list[tuple[str, str, str]]:
    seen: set[str] = set()
    entries: list[tuple[str, str, str]] = []
    for url in read_url_lines(path):
        match = _STABLE_RE.search(url)
        if not match:
            message = f"could not parse JSTOR stable URL from: {url!r}"
            if on_parse_failure:
                on_parse_failure(message)
            else:
                print(f"  WARN: {message}")
            continue
        stable_id = match.group(1)
        doi = doi_for_stable_id(stable_id)
        if doi.lower() not in seen:
            seen.add(doi.lower())
            entries.append((url, stable_id, doi))
    return entries


class JstorPrefill(DoiPrefillScript[tuple[str, str, str]]):
    description = "Prefill metadata from JSTOR stable URLs."
    default_input = DEFAULT_INPUT
    entry_kind = "JSTOR stable URLs"

    @override
    def extract_entries(self, path: Path) -> list[tuple[str, str, str]]:
        return extract_entries(path, self.record_parse_failure)

    @override
    def entry_label(self, entry: tuple[str, str, str]) -> str:
        _url, stable_id, _doi = entry
        return stable_id

    @override
    def entry_doi(self, entry: tuple[str, str, str]) -> str:
        _url, _stable_id, doi = entry
        return doi

    @override
    def source_key_for_token(self, token: str) -> str | None:
        match = _STABLE_RE.search(token)
        return self.normalize_source_key(match.group(1)) if match else None

    @override
    def postprocess_crossref_data(self, entry: tuple[str, str, str], data: dict[str, Any]) -> dict[str, Any]:
        url, _stable_id, _doi = entry
        return {**data, "link": url}

    @override
    def postprocess_metadata(
        self, entry: tuple[str, str, str], fields: dict[str, Any], metadata: dict[str, Any]
    ) -> dict[str, Any]:
        _url, _stable_id, _doi = entry
        return {**metadata, "links_alt": [f"https://doi.org/{fields['doi']}"]}


def main() -> None:
    JstorPrefill().run()


if __name__ == "__main__":
    main()
