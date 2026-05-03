# knowledge-base

Distilled knowledge on a variety of topics.

## Setup

Install dependencies with

```bash
poetry install
```

## Usage

### Python env

Activate the env with

```bash
poetry shell
```

### MkDocs

Unless otherwise specified, all commands are assumed to be run from the `knowledge_base` directory.

Serve the site locally with

```bash
mkdocs serve
```

Build the site locally with

```bash
mkdocs build
```

Deploy to GitHub Pages with

```bash
mkdocs gh-deploy
```

## Mind Map

Mind Map uses similarity between LLM embeddings of paper core content (title, abstracts, tags, and summary) to form edges between papers and displays the resulting graph using [Cytoscape.js](https://js.cytoscape.org/)

(Re)generate embeddings with

```bash
python mind_map/generate_mind_map_data.py
```

## Dev Tools

Streamlit app for analyzing the knowledge base:

```bash
streamlit run apps/analyzer_app.py
```

Streamlit app for generating new entries from arXiv:

```bash
streamlit run apps/generator_app.py
```
