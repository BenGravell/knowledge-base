"""MkDocs gen-files script: publish semantic-search assets."""

from pathlib import Path

import mkdocs_gen_files


ASSET_DIR = Path(__file__).resolve().parent

PLACEHOLDER_MANIFEST = (
    '{"model":"none","browserModel":"Xenova/all-MiniLM-L6-v2",'
    '"dimension":0,"count":0,"vectors":"semantic-search-vectors.i8",'
    '"quantization":{"type":"int8","scale":127,"normalized":true},'
    '"scoreThreshold":0.25,'
    '"scoreThresholdCalibration":{"method":"shared-tag-proxy","status":"placeholder"},'
    '"papers":[]}'
)

TEXT_ASSETS = {
    "semantic-search-index.json": PLACEHOLDER_MANIFEST,
    "semantic-search-settings.json": (
        '{"model":"none","browserModel":"Xenova/all-MiniLM-L6-v2","count":0,'
        '"scoreThreshold":0.25,'
        '"scoreThresholdCalibration":{"method":"shared-tag-proxy","status":"placeholder"}}'
    ),
}

BINARY_ASSETS = {
    "semantic-search-vectors.i8": b"",
}

for name, placeholder in TEXT_ASSETS.items():
    path = ASSET_DIR / name
    content = path.read_text(encoding="utf-8") if path.exists() else placeholder
    with mkdocs_gen_files.open(f"javascripts/{name}", "w") as out:
        out.write(content)

for name, placeholder in BINARY_ASSETS.items():
    path = ASSET_DIR / name
    content = path.read_bytes() if path.exists() else placeholder
    with mkdocs_gen_files.open(f"javascripts/{name}", "wb") as out:
        out.write(content)
