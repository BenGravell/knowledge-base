"""
MkDocs gen-files script: publish mind-map JS assets into the served site.

Runs automatically during `mkdocs build` / `mkdocs serve` because it is
listed under ``gen-files.scripts`` in mkdocs.yml.

Copies files from ``mind_map/`` into the virtual ``javascripts/`` path:

  mind_map/mind-map.js     → site/javascripts/mind-map.js
  mind_map/mind-map-data.js→ site/javascripts/mind-map-data.js
  mind_map/vendor/*        → site/javascripts/vendor/*

If ``mind-map-data.js`` has not yet been generated (i.e. the user has not
run ``generate_mind_map_data.py`` yet), a minimal placeholder is written so
that the page loads without a JS error and shows a helpful message instead.
"""

from pathlib import Path
import mkdocs_gen_files

MIND_MAP_DIR = Path(__file__).resolve().parent

PLACEHOLDER_DATA = (
    "const mindMapData = {"
    'nodes:[], similarity:{scale:1, ids:[], rows:[]}, meta:{'
    'model:"none", total_papers:0'
    "}};\n"
)

for fname in ("mind-map.js", "mind-map-data.js"):
    src = MIND_MAP_DIR / fname
    if src.exists():
        content = src.read_text(encoding="utf-8")
    elif fname == "mind-map-data.js":
        content = PLACEHOLDER_DATA
    else:
        continue

    with mkdocs_gen_files.open(f"javascripts/{fname}", "w") as out:
        out.write(content)

VENDOR_DIR = MIND_MAP_DIR / "vendor"
if VENDOR_DIR.exists():
    for src in sorted(VENDOR_DIR.iterdir()):
        if not src.is_file():
            continue
        with mkdocs_gen_files.open(f"javascripts/vendor/{src.name}", "w") as out:
            out.write(src.read_text(encoding="utf-8"))
