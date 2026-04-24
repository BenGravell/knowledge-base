# knowledge-base

Distilled knowledge on a variety of topics.

## Setup

Install dependencies with

```bash
poetry install
```

## Usage

Activate the env with

```bash
poetry shell
```

Serve the site locally with

```bash
cd knowledge_base
mkdocs serve
```

Deploy to GitHub Pages with

```bash
mkdocs gh-deploy
```

## Mind Map

Mind Map uses similarity between LLM embeddings of paper core content (title, abstracts, tags, and summary) to form edges between papers and displays the resulting graph using [Cytoscape.js](https://js.cytoscape.org/)

(Re)generate embeddings with

```bash
cd knowledge_base
python mind_map/generate_mind_map_data.py
```

## Experimental

Streamlit app for analyzing the knowledge base:

```bash
cd knowledge_base
streamlit run app.py
```

Streamlit app for generating new entries from arXiv:

```bash
cd knowledge_base
streamlit run generator_app.py
```
