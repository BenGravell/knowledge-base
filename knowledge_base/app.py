from typing import Any
from pathlib import Path
import yaml
import requests

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


PAPERS_DIR = Path("docs/papers")

st.set_page_config(layout="wide")


def load_metadata(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_papers_metadata(papers_dir: Path) -> pd.DataFrame:
    rows = []
    for path in papers_dir.glob("*/*/metadata.yml"):
        content = load_metadata(path)

        # Extract structure info from path
        year = path.parent.parent.name
        slug = path.parent.name

        # Flatten into a single row
        row = {"year": year, "slug": slug, **content}

        rows.append(row)

    df = pd.DataFrame(rows)
    return df


@st.cache_data
def fetch_pdf(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.content


def show_paper(metadata: dict) -> None:
    title = metadata.get("title", "Untitled")
    algorithm = metadata.get("algorithm")
    authors = metadata.get("authors", [])
    year = metadata.get("year", "")
    source = metadata.get("source", "")
    type_ = metadata.get("type", "")
    doi = metadata.get("doi")
    arxiv_id = metadata.get("arxiv_id")
    tags = metadata.get("tags", [])
    abstract = metadata.get("abstract", "")
    summary = metadata.get("summary", "")
    link = metadata.get("link")
    links_alt = metadata.get("links_alt", [])

    heading = f"{algorithm}: {title}" if algorithm else title
    st.header(heading)

    lines = [
        ("Authors", ", ".join(authors), None),
        ("Year", str(year), None),
    ]
    if source:
        lines.append(("Source", f"{source} ({type_})", None))
    if doi:
        lines.append(("DOI", doi, f"https://doi.org/{doi}"))
    if arxiv_id:
        lines.append(("arXiv", arxiv_id, f"https://arxiv.org/abs/{arxiv_id}"))

    rows_html = ""
    for field, value, url in lines:
        cell = f'<a href="{url}" target="_blank">{value}</a>' if url else value
        rows_html += f"<tr><td style='padding-right:1.5em;font-weight:600;white-space:nowrap'>{field}</td><td>{cell}</td></tr>"

    st.markdown(f"<table>{rows_html}</table>", unsafe_allow_html=True)

    if tags:
        tag = st.pills("Tags", tags)

    if summary:
        st.subheader("Summary")
        st.write(summary)

    if abstract:
        with st.expander("Abstract"):
            st.write(abstract)

    all_links = ([link] if link else []) + links_alt
    if all_links:
        st.subheader("Links")
        for url in all_links:
            st.write(f"- {url}")


def format_arxiv(arxiv_id):
    row = stuff.loc[arxiv_id]
    title = row["title"]
    algorithm = row["algorithm"]

    title_with_algorithm = title

    if not pd.isna(algorithm):
        if not title_with_algorithm.startswith(f"{algorithm}: "):
            title_with_algorithm = f"{algorithm}: {title}"

    return f"{title_with_algorithm} (arXiv:{arxiv_id})"


# DATA LOADING
df = load_papers_metadata(PAPERS_DIR)

stuff = df[["title", "algorithm", "arxiv_id"]]
stuff["arxiv_id"] = stuff["arxiv_id"].astype(str)
stuff = stuff.dropna(axis="index", subset=["arxiv_id"]).set_index("arxiv_id")


# UI
agg_tab, detail_tab = st.tabs(
    ["Aggregate", ":material/menu_book: arXiv Paper Inspector"]
)

with agg_tab:
    st.metric("Total Number of Papers Indexed", value=len(df))

    st.write(df)

    fig = px.histogram(df, x="year")
    st.plotly_chart(fig)

with detail_tab:
    arxiv_id = st.selectbox(
        "Select Paper", options=stuff.index, format_func=format_arxiv
    )

    cols = st.columns(4)
    with cols[0]:
        st.link_button(
            "View arXiv page",
            f"https://arxiv.org/abs/{arxiv_id}",
            icon=":material/open_in_new:",
            use_container_width=True,
        )
    with cols[1]:
        st.link_button(
            "View arXiv PDF",
            f"https://arxiv.org/pdf/{arxiv_id}",
            icon=":material/open_in_new:",
            use_container_width=True,
        )
    with cols[2]:
        st.link_button(
            "View arXiv HTML",
            f"https://ar5iv.org/abs/{arxiv_id}",
            icon=":material/open_in_new:",
            use_container_width=True,
        )
    with cols[3]:
        st.link_button(
            "View HuggingFace page",
            f"https://huggingface.co/papers/{arxiv_id}",
            icon=":material/open_in_new:",
            use_container_width=True,
        )

    year = f"20{arxiv_id[0:2]}"
    path = PAPERS_DIR / f"{year}/{arxiv_id}/metadata.yml"
    metadata = load_metadata(path)

    show_paper(metadata)

    st.header("PDF Viewer")
    pdf_bytes = fetch_pdf(f"https://arxiv.org/pdf/{arxiv_id}.pdf")
    st.pdf(pdf_bytes, height=800)
