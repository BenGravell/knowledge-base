# knowledge-base

Curated research you can actually navigate.

The public site is published at <https://bengravell.github.io/knowledge-base/>.

## Setup

See [docs/SETUP.md](docs/SETUP.md)

## Workflows

See [docs/WORKFLOWS.md](docs/WORKFLOWS.md)

## Development

See [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md)

## Repo layout

- `knowledge_base/` contains the published site source and supporting tools.
  - `docs/` contains the Zensical source pages and paper metadata.
    - `papers/**/metadata.yml` drives generated paper pages.
    - `papers/**/embed_text.md` contains cleaned arXiv full-text conversions for embeddings.
  - `tree.yml` is the editable Tree navigation and classification source.
  - `components/` contains browser component source and Map/Search adapters.
  - `tree/` contains the Tree model, validation, and generated Tree/Timeline/Analytics projections.
  - `publishing/` contains generated-site contracts, paper page generation, and shared asset publishing.
  - `prefill/` contains the metadata prefill workflow and source adapters.
  - `scripts/` contains maintenance, audit, placement, and prefill entrypoints.
  - `utils/` contains small shared helpers.
- `dev_apps/` contains Streamlit apps and other human-facing development tools.
- `./dev` is the Pixi wrapper command.
- `knowledge_base/components/map/`, `knowledge_base/tree/`, and
  `knowledge_base/components/semantic_search/` derive Map, Timeline, Tree, and
  Semantic Search from `docs/papers/**/metadata.yml` plus `tree.yml`.
- `todo/PAPERS_FUNNEL.md` and `todo/papers/*.md` hold incoming paper URLs before ingest.
- `docs/` contains repository docs for users and maintainers; it is not the published site content.
