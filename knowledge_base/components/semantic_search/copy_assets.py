"""Generated-file script: publish semantic-search assets."""

from __future__ import annotations

from pathlib import Path

from knowledge_base.catalog import Catalog
from knowledge_base.publishing.generated_assets import (
    SEMANTIC_SEARCH_INDEX,
    SEMANTIC_SEARCH_PLACEHOLDER_MANIFEST,
    SEMANTIC_SEARCH_PLACEHOLDER_SETTINGS,
    SEMANTIC_SEARCH_SETTINGS,
    SEMANTIC_SEARCH_VECTORS,
    load_json_object,
    validate_semantic_search_contract,
)
from knowledge_base.publishing.generated_files import open_generated

ASSET_DIR = Path(__file__).resolve().parent
KB_DIR = ASSET_DIR.parents[1]
METADATA_ROOT = KB_DIR / "docs" / "papers"
RUN_GENERATE_SEMANTIC_SEARCH = "python knowledge_base/components/semantic_search/generate_semantic_search_index.py"

TEXT_ASSETS = {
    SEMANTIC_SEARCH_INDEX.name: SEMANTIC_SEARCH_INDEX.dumps(
        SEMANTIC_SEARCH_PLACEHOLDER_MANIFEST,
        separators=(",", ":"),
    ),
    SEMANTIC_SEARCH_SETTINGS.name: SEMANTIC_SEARCH_SETTINGS.dumps(
        SEMANTIC_SEARCH_PLACEHOLDER_SETTINGS,
        separators=(",", ":"),
    ),
}

BINARY_ASSETS = {
    SEMANTIC_SEARCH_VECTORS.name: b"",
}


def validate_semantic_assets() -> tuple[dict[str, str], dict[str, bytes]]:
    manifest_path = ASSET_DIR / SEMANTIC_SEARCH_INDEX.name
    settings_path = ASSET_DIR / SEMANTIC_SEARCH_SETTINGS.name
    vector_stem = SEMANTIC_SEARCH_VECTORS.name.removesuffix(".i8")
    vector_candidates = [path for path in ASSET_DIR.glob(f"{vector_stem}*.i8") if path.is_file()]

    if not manifest_path.exists():
        if settings_path.exists() or any(path.stat().st_size for path in vector_candidates):
            raise RuntimeError(f"Semantic Search assets are partial; run {RUN_GENERATE_SEMANTIC_SEARCH}")
        return TEXT_ASSETS, BINARY_ASSETS

    manifest = load_json_object(manifest_path, run_hint=RUN_GENERATE_SEMANTIC_SEARCH)
    current_ids = [entry.id for entry in Catalog.from_metadata_root(METADATA_ROOT).entries]

    if not settings_path.exists():
        raise RuntimeError(f"Missing {settings_path}; run {RUN_GENERATE_SEMANTIC_SEARCH}")
    settings = load_json_object(settings_path, run_hint=RUN_GENERATE_SEMANTIC_SEARCH)

    try:
        contract = validate_semantic_search_contract(
            manifest,
            settings,
            asset_dir=ASSET_DIR,
            current_ids=current_ids,
        )
    except ValueError as exc:
        raise RuntimeError(f"{exc}; run {RUN_GENERATE_SEMANTIC_SEARCH}") from exc

    return (
        {
            SEMANTIC_SEARCH_INDEX.name: manifest_path.read_text(encoding="utf-8"),
            SEMANTIC_SEARCH_SETTINGS.name: settings_path.read_text(encoding="utf-8"),
        },
        {contract.vector_sidecar.name: contract.vector_sidecar.path.read_bytes()},
    )


text_assets, binary_assets = validate_semantic_assets()

for name, content in text_assets.items():
    with open_generated(f"javascripts/{name}", "w") as out:
        out.write(content)

for name, content in binary_assets.items():
    with open_generated(f"javascripts/{name}", "wb") as out:
        out.write(content)
