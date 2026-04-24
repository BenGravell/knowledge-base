"""
MkDocs gen-files script: publish mind-map JS assets into the served site.

Runs automatically during `mkdocs build` / `mkdocs serve` because it is
listed under ``gen-files.scripts`` in mkdocs.yml.

Copies files from ``mind_map/`` into the virtual ``javascripts/`` path:

  mind_map/mind-map.js              → site/javascripts/mind-map.js
  mind_map/mind-map-data.js         → site/javascripts/mind-map-data.js
  mind_map/vendor/layout-base.js    → site/javascripts/vendor/layout-base.js
  mind_map/vendor/cose-base.js      → site/javascripts/vendor/cose-base.js
  mind_map/vendor/cytoscape-fcose.js→ site/javascripts/vendor/cytoscape-fcose.js

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
        content = PLACEHOLDER_DATA
    else:
        continue

    with mkdocs_gen_files.open(f"javascripts/{fname}", "w") as out:
        out.write(content)

# Vendor libraries (fcose and its deps) — served locally to avoid CDN issues.
VENDOR_DIR = MIND_MAP_DIR / "vendor"
for vname in ("layout-base.js", "cose-base.js", "cytoscape-fcose.js"):
    src = VENDOR_DIR / vname
    if src.exists():
        with mkdocs_gen_files.open(f"javascripts/vendor/{vname}", "w") as out:
            out.write(src.read_text(encoding="utf-8"))
