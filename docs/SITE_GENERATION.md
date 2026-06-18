# Site generation and derived features

Commands in this file run from the repository root.

## Zensical site

Serve the site locally:

```bash
kb serve
```

Build the static site:

```bash
kb build
```

Build the static files for GitHub Pages:

```bash
kb build
```

Before `zensical serve` and `zensical build`, `kb` materializes
`knowledge_base/.generated/docs/` from `knowledge_base/docs/`, then runs these
generated-file scripts:

- `knowledge_base/generate_papers.py` renders generated paper pages from `knowledge_base/docs/papers/**/metadata.yml`.
- `knowledge_base/map/copy_assets.py` publishes Map JavaScript and vendor assets.
- `knowledge_base/semantic_search/copy_assets.py` publishes the Semantic Search index and vector table.
- `knowledge_base/tree/generate_tree_data.py` publishes Tree browser data.

`knowledge_base/zensical.yml` is the source Zensical site config. Tree data is
generated directly from `knowledge_base/tree.yml`. For the in-process
Tree model design, see
[knowledge_base/tree/README.md](../knowledge_base/tree/README.md).

## Map

The Map embeds paper core content, computes semantic similarity and positions,
and renders the resulting node map with Sigma.js and Graphology.

Regenerate embeddings and graph data:

```bash
python knowledge_base/map/generate_map_data.py
```

Useful variants:

```bash
python knowledge_base/map/generate_map_data.py --force
python knowledge_base/map/generate_map_data.py --backend fastembed
python knowledge_base/map/generate_map_data.py --backend voyage
python knowledge_base/map/generate_map_data.py --skip-force-layout
```

Preview the layout quickly with Plotly:

```bash
python knowledge_base/map/preview_map.py
python knowledge_base/map/preview_map.py --serve
python knowledge_base/map/preview_map.py --out preview.html
```

Smoke-test the served Zensical Map page in headless Chrome:

```bash
python knowledge_base/scripts/verify_map_view.py --url http://127.0.0.1:8000/map/
```

Measure the Tree page default-load plus top-level branch-click timing:

```bash
kb build
python knowledge_base/scripts/measure_tree_view.py
python knowledge_base/scripts/measure_tree_view.py --runs 7 --viewport 1366x900
python knowledge_base/scripts/measure_tree_view.py --reduced-motion
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
python knowledge_base/semantic_search/generate_semantic_search_index.py
```

Semantic Search intentionally uses `sentence-transformers/all-MiniLM-L6-v2` /
`Xenova/all-MiniLM-L6-v2` instead of the Map's heavier embedding model. The Map
can afford a larger offline model because embeddings are generated ahead of
time and only the resulting graph data is served. Semantic Search also embeds
arbitrary user queries on the client, so the model must be small, fast, and
browser-compatible.
