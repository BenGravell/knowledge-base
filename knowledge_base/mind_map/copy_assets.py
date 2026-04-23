"""
MkDocs gen-files script: publish mind-map JS assets into the served site.

Runs automatically during `mkdocs build` / `mkdocs serve` because it is
listed under ``gen-files.scripts`` in mkdocs.yml.

It copies two files from ``mind_map/`` (next to this script, relative to
the mkdocs root) into the virtual ``javascripts/`` path that MkDocs serves:

  mind_map/mind-map.js        → site/javascripts/mind-map.js
  mind_map/mind-map-data.js   → site/javascripts/mind-map-data.js

If ``mind-map-data.js`` has not yet been generated (i.e. the user has not
run ``generate_mind_map_data.py`` yet), a minimal placeholder is written so
that the page loads without a JS error and shows a helpful message instead.
"""

from pathlib import Path
import mkdocs_gen_files

# gen-files scripts run with CWD = the mkdocs root (the directory that
# contains mkdocs.yml), which is knowledge_base/.
MIND_MAP_DIR = Path("mind_map")

PLACEHOLDER_DATA = (
    "const mindMapData = {"
    'nodes:[], edges:[], meta:{'
    'model:"none", threshold:0.80, top_k:5, '
    'total_papers:0, total_edges:0'
    "}};\n"
)

for fname in ("mind-map.js", "mind-map-data.js"):
    src = MIND_MAP_DIR / fname
    if src.exists():
        content = src.read_text(encoding="utf-8")
    elif fname == "mind-map-data.js":
        # Data not yet generated — use placeholder so the page doesn't crash.
        content = PLACEHOLDER_DATA
    else:
        # mind-map.js is required; skip silently if somehow missing.
        continue

    with mkdocs_gen_files.open(f"javascripts/{fname}", "w") as out:
        out.write(content)
