# knowledge-base

Distilled knowledge on a variety of topics.

## Setup

Install dependencies from the repository root:

```bash
poetry install
```

Activate the environment:

```bash
poetry shell
```

## Development Checks

Lint and type-check Python code from the repository root:

```bash
poetry run ruff check knowledge_base tests
poetry run ruff format --check knowledge_base tests
poetry run pyrefly check --baseline .pyrefly-baseline.json
```

Run unit tests from the repository root (`~/knowledge-base`, not `knowledge_base/`):

```bash
poetry run python -m unittest discover -s tests -p 'test_*.py'
```

Install the pre-commit hooks once:

```bash
pre-commit install
```

Run all pre-commit hooks manually:

```bash
pre-commit run --all-files
```

Unless otherwise noted, run the commands below from the `knowledge_base/` directory.

## MkDocs Site

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

During `mkdocs serve` and `mkdocs build`, MkDocs runs these Python gen-files
scripts automatically:

- `generate_papers.py` renders generated paper pages from `docs/papers/**/metadata.yml`.
- `map/copy_assets.py` publishes Map JavaScript and vendor assets.
- `semantic_search/copy_assets.py` publishes the Semantic Search index and vector table.
- `tree/generate_tree_data.py` publishes Tree browser data.

The Tree nav itself is edited in `tree.yml`. `mkdocs.yml`
loads that standalone file through the local `tree-nav` plugin.
Paper entries in `tree.yml` should use their literal metadata paths,
such as `docs/papers/2025/2506.11513/metadata.yml`; the build converts those
paths to generated `papers/<slug>.md` pages behind the scenes.
For the in-process Tree model design, see
[knowledge_base/tree/README.md](knowledge_base/tree/README.md).

## Local generated data

Refresh all local generated data and validate the site is self-consistent:

```bash
python scripts/refresh_offline_data.py
```

Use `--force` to recompute cached embeddings, or `--strict` to also fail on
Tree algorithm-label drift and MkDocs warnings.

## Streamlit Apps

Generate and edit a `metadata.yml` entry from an arXiv ID:

```bash
streamlit run apps/generator_app.py
```

## Item Ingest

The starting point for adding new items into the Knowledge Base is ingestion.

You can ingest manually by creating a new directory in `docs/papers/` and a `metadata.yml` file.

An easier way to get started is to collect a batch of URLs and follow the automated workflow below.

### Funnel Items

Place a batch of URLs in `todo/PAPERS_FUNNEL.md`, one URL per line.

Route URLs from `todo/PAPERS_FUNNEL.md` into source-specific files under `todo/papers/`, or into `todo/PAPERS_MISC.md` when the source is unknown:

```bash
python scripts/funnel_papers.py --dry-run
python scripts/funnel_papers.py
```

### Source Prefill Scripts

Source-specific prefill scripts read URL or ID lists from `todo/papers/*.md`, fetch initial metadata, and write `docs/papers/<YEAR>/<SLUG>/metadata.yml`.

Generated metadata starts as `audit_status: raw` and should be reviewed with `scripts/audit_metadata.py`.

Run a prefill script with its default input file:

```bash
python scripts/prefill/arxiv.py
python scripts/prefill/ieee.py
```

Common options shared by the prefill scripts:

```bash
python scripts/prefill/<source>.py --input ../todo/papers/<SOURCE>.md
python scripts/prefill/<source>.py --first 5
python scripts/prefill/<source>.py --list-skipped
python scripts/prefill/<source>.py --overwrite
python scripts/prefill/<source>.py --reingest
```

## Paper Metadata Scripts

Audit all paper metadata files:

```bash
python scripts/audit_metadata.py
```

Audit only entries marked `audit_status: partial`:

```bash
python scripts/audit_metadata.py --audit-status partial
```

List entries still marked `audit_status: raw`:

```bash
python scripts/list_raw_papers.py
```

Add `audit_status` to older metadata files that do not have it yet:

```bash
python scripts/add_audit_status.py --dry-run
python scripts/add_audit_status.py
```

Validate `tree.yml` local links and paper placement:

```bash
python scripts/validate_tree.py
python scripts/validate_tree.py --check-algorithm-labels
```

Suggest likely fixes for Tree/metadata algorithm-label disagreements:

```bash
python scripts/suggest_tree_algorithm_labels.py
python scripts/suggest_tree_algorithm_labels.py --min-confidence high
python scripts/suggest_tree_algorithm_labels.py --format json
streamlit run apps/tree_label_review_app.py
```

Find generated paper pages that are missing from the `Tree` nav:

```bash
python scripts/list_unplaced_papers.py --neighbors 3
python scripts/list_unplaced_papers.py --format paths
python scripts/list_unplaced_papers.py --neighbors 0 --fail-on-missing
```

Measure the Tree page default-load plus top-level branch-click timing:

```bash
mkdocs build
python scripts/measure_tree_view.py
python scripts/measure_tree_view.py --runs 7 --viewport 1366x900
python scripts/measure_tree_view.py --reduced-motion
```

## Map

The Map embeds paper core content, computes semantic similarity and positions, and renders the resulting node map with [Sigma.js](https://www.sigmajs.org/) and [Graphology](https://graphology.github.io/).

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

## Semantic Search

Semantic Search is a client-side exploratory search page for finding papers by meaning rather than exact keywords. In the UX, open **Semantic Search**, type a phrase such as "safe motion planning with uncertainty" or "diffusion policies for robot manipulation", and the page returns the nearest papers.

Internally, the search page loads a static paper manifest and compact int8 vector table from `semantic_search/`, embeds the user's query in the browser with Transformers.js, normalizes the query vector, and computes cosine-like dot products against all stored paper vectors in a Web Worker. This keeps the site compatible with GitHub Pages: there is no search server, vector database, or API key at runtime.

Regenerate the Semantic Search index after paper metadata changes:

```bash
python semantic_search/generate_semantic_search_index.py
```

Semantic Search intentionally uses `sentence-transformers/all-MiniLM-L6-v2` / `Xenova/all-MiniLM-L6-v2` instead of the Map's heavier embedding model. The Map can afford a larger offline model because embeddings are generated ahead of time and only the resulting graph data is served. Semantic Search also needs to embed arbitrary user queries on the client, so the model must be small, fast, and browser-compatible. MiniLM gives a practical first-load and query-time tradeoff while preserving real semantic behavior.

## Repo Layout

`knowledge_base` contains the following:

- `apps/` contains Streamlit apps.
- `scripts/` contains maintenance, audit, placement, and prefill entrypoints.
- `scripts/prefill/` contains source-specific paper metadata importers.
- `map/` contains graph generation, preview, and MkDocs asset publishing.
- `semantic_search/` contains client-side semantic search index generation and MkDocs asset publishing.
- `tree/` contains the Tree model, validation helpers, MkDocs nav plugin, and Tree data generator.
  Start with [tree/README.md](knowledge_base/tree/README.md).
- `utils/` contains shared DOI, arXiv, and prefill helpers used by the scripts.
