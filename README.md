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
