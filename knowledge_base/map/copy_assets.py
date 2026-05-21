"""
MkDocs gen-files script: publish map JS assets into the served site.

Runs automatically during `mkdocs build` / `mkdocs serve` because it is
listed under ``gen-files.scripts`` in mkdocs.yml.

Copies files from ``map/`` into the virtual ``javascripts/`` path:

  map/map.js     → site/javascripts/map.js
  map/map-data.js→ site/javascripts/map-data.js
  map/vendor/*        → site/javascripts/vendor/*

If ``map-data.js`` has not yet been generated (i.e. the user has not
run ``generate_map_data.py`` yet), a minimal placeholder is written so
that the page loads without a JS error and shows a helpful message instead.
"""

from pathlib import Path
import mkdocs_gen_files

MAP_DIR = Path(__file__).resolve().parent

PLACEHOLDER_DATA = (
    "const mapData = {"
    'nodes:[], similarity:{scale:1, ids:[], rows:[]}, meta:{'
    'model:"none", total_papers:0'
    "}};\n"
)

for fname in ("map.js", "map-data.js"):
    src = MAP_DIR / fname
    if src.exists():
        content = src.read_text(encoding="utf-8")
    elif fname == "map-data.js":
        content = PLACEHOLDER_DATA
    else:
        continue

    with mkdocs_gen_files.open(f"javascripts/{fname}", "w") as out:
        out.write(content)

VENDOR_DIR = MAP_DIR / "vendor"
if VENDOR_DIR.exists():
    for src in sorted(VENDOR_DIR.iterdir()):
        if not src.is_file():
            continue
        with mkdocs_gen_files.open(f"javascripts/vendor/{src.name}", "w") as out:
            out.write(src.read_text(encoding="utf-8"))
