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

- `knowledge_base/publishing/generate_papers.py` renders generated paper pages from `knowledge_base/docs/papers/**/metadata.yml`.
- `knowledge_base/publishing/browser_assets.py` publishes shared browser component JavaScript.
- `knowledge_base/components/map/pipeline/copy_assets.py` publishes Map JavaScript and vendor assets.
- `knowledge_base/components/semantic_search/copy_assets.py` publishes the Semantic Search index and vector table.
- `knowledge_base/tree/generate_tree_data.py` publishes Tree browser data.

The staging step intentionally skips `knowledge_base/docs/papers/`; generated
paper pages are written from `metadata.yml` entries, so embed sidecars are never
handed to Zensical as source pages.

`knowledge_base/zensical.yml` is the source Zensical site config. Tree data is
generated directly from `knowledge_base/tree.yml`. For the in-process
Tree model design, see
[knowledge_base/tree/README.md](../knowledge_base/tree/README.md).

## Map

The Map embeds paper core content, computes semantic similarity and positions,
and renders the resulting node map with Sigma.js and Graphology.

Regenerate embeddings and graph data:

```bash
python -m knowledge_base.components.map.pipeline.generate_data
```

Useful variants:

```bash
python -m knowledge_base.components.map.pipeline.generate_data --force
python -m knowledge_base.components.map.pipeline.generate_data --backend fastembed
python -m knowledge_base.components.map.pipeline.generate_data --skip-force-layout
```

Smoke-test the served Zensical Map page in headless Chrome:

```bash
python -m knowledge_base.scripts.verify_map_view --url http://127.0.0.1:8000/map/
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
vector table from `components/semantic_search/`, embeds the user's query in the browser
with Transformers.js, normalizes the query vector, and computes dot products
against all stored paper vectors in a Web Worker. This keeps the site compatible
with GitHub Pages: there is no search server, vector database, or API key at
runtime.

Regenerate the Semantic Search index after paper metadata changes:

```bash
python knowledge_base/components/semantic_search/generate_semantic_search_index.py
```

Semantic Search intentionally uses `sentence-transformers/all-MiniLM-L6-v2` /
`Xenova/all-MiniLM-L6-v2` instead of the Map's heavier embedding model. The Map
can afford a larger offline model because embeddings are generated ahead of
time and only the resulting graph data is served. Semantic Search also embeds
arbitrary user queries on the client, so the model must be small, fast, and
browser-compatible.

The checked-in WordPiece vocabulary at
`knowledge_base/tokenizers/all-MiniLM-L6-v2-vocab.txt` is kept intentionally.
`Catalog` uses it to count MiniLM tokens while chunking paper text before
embedding, so long inputs stay under the model limit instead of being truncated
later by FastEmbed.
The vocabulary is a model asset, not something the model name or package
definition can reconstruct.
Vendoring this small file keeps site generation deterministic and offline
instead of depending on a Hugging Face cache or network download.
