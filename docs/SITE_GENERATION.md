# Site generation and derived features

Commands in this file run from `knowledge_base/` unless noted otherwise.

## MkDocs site

Serve the site locally:

```bash
mkdocs serve
```

Build the static site:

```bash
mkdocs build
```

Deploy to GitHub Pages:

```bash
mkdocs gh-deploy
```

During `mkdocs serve` and `mkdocs build`, MkDocs runs these gen-files scripts
automatically:

- `generate_papers.py` renders generated paper pages from `docs/papers/**/metadata.yml`.
- `map/copy_assets.py` publishes Map JavaScript and vendor assets.
- `semantic_search/copy_assets.py` publishes the Semantic Search index and vector table.
- `tree/generate_tree_data.py` publishes Tree browser data.

`mkdocs.yml` loads `tree.yml` through the local `tree-nav` plugin. For the
in-process Tree model design, see
[knowledge_base/tree/README.md](../knowledge_base/tree/README.md).

## Map

The Map embeds paper core content, computes semantic similarity and positions,
and renders the resulting node map with Sigma.js and Graphology.

Regenerate embeddings and graph data:

```bash
python map/generate_map_data.py
```

Useful variants:

```bash
python map/generate_map_data.py --force
python map/generate_map_data.py --backend fastembed
python map/generate_map_data.py --backend voyage
python map/generate_map_data.py --skip-force-layout
```

Preview the layout quickly with Plotly:

```bash
python map/preview_map.py
python map/preview_map.py --serve
python map/preview_map.py --out preview.html
```

Smoke-test the served MkDocs Map page in headless Chrome:

```bash
python scripts/verify_map_view.py --url http://127.0.0.1:8000/map/
```

Measure the Tree page default-load plus top-level branch-click timing:

```bash
mkdocs build
python scripts/measure_tree_view.py
python scripts/measure_tree_view.py --runs 7 --viewport 1366x900
python scripts/measure_tree_view.py --reduced-motion
```

## Semantic Search

Semantic Search is a client-side exploratory search page for finding papers by
meaning rather than exact keywords. In the UX, open **Semantic Search**, type a
phrase such as "safe motion planning with uncertainty" or "diffusion policies
for robot manipulation", and the page returns the nearest papers.

Internally, the search page loads a static paper manifest and compact int8
vector table from `semantic_search/`, embeds the user's query in the browser
with Transformers.js, normalizes the query vector, and computes dot products
against all stored paper vectors in a Web Worker. This keeps the site compatible
with GitHub Pages: there is no search server, vector database, or API key at
runtime.

Regenerate the Semantic Search index after paper metadata changes:

```bash
python semantic_search/generate_semantic_search_index.py
```

Semantic Search intentionally uses `sentence-transformers/all-MiniLM-L6-v2` /
`Xenova/all-MiniLM-L6-v2` instead of the Map's heavier embedding model. The Map
can afford a larger offline model because embeddings are generated ahead of
time and only the resulting graph data is served. Semantic Search also embeds
arbitrary user queries on the client, so the model must be small, fast, and
browser-compatible.
