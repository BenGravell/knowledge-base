from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.spatial.distance import pdist
from sklearn.preprocessing import normalize


APP_DIR = Path(__file__).resolve().parent
KB_DIR = APP_DIR.parent
MAP_DIR = KB_DIR / "map"
MAP_DATA = MAP_DIR / "map-data.js"
EMBEDDING_CACHE = MAP_DIR / "embedding_cache.json"


def _read_map_json(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"const\s+mapData\s*=\s*(\{.*\})\s*;?\s*$", text, re.S)
    if not match:
        raise ValueError(f"Could not find `const mapData = ...` in {path}")
    return json.loads(match.group(1))


@st.cache_data(show_spinner="Loading map data...")
def load_map() -> tuple[pd.DataFrame, np.ndarray, str]:
    map_data = _read_map_json(MAP_DATA)
    cache = json.loads(EMBEDDING_CACHE.read_text(encoding="utf-8"))

    embedding_by_id = {
        paper_id: paper["embedding"]
        for paper_id, paper in cache.get("papers", {}).items()
        if paper.get("embedding")
    }

    rows = []
    embeddings = []
    for node in map_data.get("nodes", []):
        data = node.get("data", {})
        paper_id = data.get("id")
        embedding = embedding_by_id.get(paper_id)
        if not paper_id or embedding is None:
            continue

        tags = data.get("tags") or []
        super_category = data.get("super_category") or "Uncategorized"
        category = data.get("category") or "Uncategorized"
        sub_category = data.get("sub_category") or ""
        rows.append(
            {
                "id": paper_id,
                "label": data.get("label") or paper_id,
                "title": data.get("title") or "",
                "authors": ", ".join(data.get("authors") or []),
                "year": data.get("year"),
                "super_category": super_category,
                "category": category,
                "sub_category": sub_category,
                "current_path": " / ".join(
                    part for part in [super_category, category, sub_category] if part
                ),
                "tags": ", ".join(tags),
                "summary": data.get("summary") or "",
                "x": node.get("position", {}).get("x", 0.0),
                "y": node.get("position", {}).get("y", 0.0),
            }
        )
        embeddings.append(embedding)

    if not rows:
        raise ValueError("No map nodes could be matched to cached embeddings.")

    df = pd.DataFrame(rows)
    matrix = normalize(np.asarray(embeddings, dtype=np.float32))
    return df, matrix, cache.get("model", "unknown")


@st.cache_data(show_spinner="Clustering embeddings...")
def cluster_embeddings(
    embeddings: np.ndarray,
    ids: tuple[str, ...],
    method: str,
    metric: str,
    n_clusters: int,
) -> tuple[np.ndarray, np.ndarray]:
    if len(ids) != len(embeddings):
        raise ValueError("IDs and embeddings are misaligned.")
    if len(ids) < 2:
        return np.empty((0, 4)), np.ones(len(ids), dtype=int)

    distance_metric = "euclidean" if method == "ward" else metric
    distances = pdist(embeddings, metric=distance_metric)
    tree = linkage(distances, method=method, optimal_ordering=len(ids) <= 750)
    labels = fcluster(tree, t=min(n_clusters, len(ids)), criterion="maxclust")
    return tree, labels


def describe_cluster(frame: pd.DataFrame) -> str:
    terms: Counter[str] = Counter()
    for column, weight in [("category", 3), ("sub_category", 2), ("tags", 1)]:
        for value in frame[column].dropna():
            pieces = [value] if column != "tags" else [p.strip() for p in value.split(",")]
            for piece in pieces:
                if piece:
                    terms[piece] += weight

    top_terms = [term for term, _ in terms.most_common(3)]
    return " · ".join(top_terms) if top_terms else "Mixed"


def add_cluster_summaries(frame: pd.DataFrame) -> pd.DataFrame:
    frame = frame.copy()
    descriptions = {
        cluster: describe_cluster(group)
        for cluster, group in frame.groupby("cluster", sort=True)
    }
    sizes = frame["cluster"].value_counts().to_dict()
    frame["cluster_name"] = frame["cluster"].map(
        lambda c: f"{int(c):02d}: {descriptions[c]} ({sizes[c]})"
    )
    return frame


def centroid_dendrogram(
    frame: pd.DataFrame,
    embeddings: np.ndarray,
    method: str,
    metric: str,
    max_leaves: int,
) -> object | None:
    groups = list(frame.groupby("cluster", sort=True).groups.items())
    if len(groups) < 2:
        return None

    centroids = []
    labels = []
    for cluster, indices in groups:
        cluster_frame = frame.loc[indices]
        centroids.append(embeddings[list(indices)].mean(axis=0))
        labels.append(f"{int(cluster):02d} ({len(indices)}): {describe_cluster(cluster_frame)}")

    centroids = normalize(np.asarray(centroids, dtype=np.float32))
    if len(centroids) > max_leaves:
        sizes = frame["cluster"].value_counts()
        keep = set(sizes.head(max_leaves).index)
        mask = [cluster in keep for cluster, _ in groups]
        centroids = centroids[mask]
        labels = [label for label, keep_label in zip(labels, mask) if keep_label]

    distance_metric = "euclidean" if method == "ward" else metric

    def distfun(values: np.ndarray) -> np.ndarray:
        return pdist(values, metric=distance_metric)

    def linkagefun(distances: np.ndarray) -> np.ndarray:
        return linkage(distances, method=method, optimal_ordering=True)

    fig = ff.create_dendrogram(
        centroids,
        labels=labels,
        orientation="left",
        distfun=distfun,
        linkagefun=linkagefun,
    )
    fig.update_layout(
        height=max(520, 18 * len(labels)),
        margin=dict(l=20, r=20, t=30, b=20),
        xaxis_title="Embedding distance",
        yaxis_title="Cluster",
    )
    return fig


def filter_frame(frame: pd.DataFrame) -> pd.Series:
    mask = pd.Series(True, index=frame.index)

    query = st.sidebar.text_input("Search", placeholder="title, label, tag, summary")
    if query.strip():
        needle = query.strip().lower()
        haystack = (
            frame["label"].fillna("")
            + " "
            + frame["title"].fillna("")
            + " "
            + frame["tags"].fillna("")
            + " "
            + frame["summary"].fillna("")
        ).str.lower()
        mask &= haystack.str.contains(re.escape(needle), regex=True)

    super_categories = sorted(frame["super_category"].dropna().unique())
    selected_supers = st.sidebar.multiselect(
        "Super categories",
        super_categories,
        default=super_categories,
    )
    if selected_supers:
        mask &= frame["super_category"].isin(selected_supers)

    available_categories = sorted(frame.loc[mask, "category"].dropna().unique())
    selected_categories = st.sidebar.multiselect("Categories", available_categories)
    if selected_categories:
        mask &= frame["category"].isin(selected_categories)

    year_min = int(frame["year"].dropna().min())
    year_max = int(frame["year"].dropna().max())
    year_range = st.sidebar.slider("Year range", year_min, year_max, (year_min, year_max))
    mask &= frame["year"].between(year_range[0], year_range[1], inclusive="both")

    return mask


st.set_page_config(page_title="Map Clustering", layout="wide")
st.title("Map Hierarchical Clustering")

try:
    base_df, base_embeddings, embedding_model = load_map()
except Exception as exc:
    st.error(f"Failed to load map data: {exc}")
    st.stop()

st.sidebar.header("Scope")
display_mask = filter_frame(base_df)
cluster_filtered_only = st.sidebar.checkbox(
    "Cluster only filtered papers",
    value=False,
    help="When off, clusters are computed for the full corpus and filters only change what is shown.",
)

scope_mask = display_mask if cluster_filtered_only else pd.Series(True, index=base_df.index)
scope_df = base_df.loc[scope_mask].reset_index(drop=True)
scope_indices = base_df.index[scope_mask].to_numpy()
scope_embeddings = base_embeddings[scope_indices]

if len(scope_df) < 2:
    st.warning("Select at least two papers to cluster.")
    st.stop()

st.sidebar.header("Clustering")
method = st.sidebar.selectbox("Linkage", ["ward", "average", "complete", "single"])
metric = st.sidebar.selectbox(
    "Distance",
    ["cosine", "euclidean"],
    disabled=method == "ward",
    help="Ward linkage always uses Euclidean distance on normalized embeddings.",
)
max_clusters = min(80, len(scope_df))
default_clusters = min(24, max_clusters)
n_clusters = st.sidebar.slider("Cut into clusters", 2, max_clusters, default_clusters)
max_dendrogram_leaves = st.sidebar.slider("Dendrogram leaves", 10, 80, 50)

tree, cluster_labels = cluster_embeddings(
    scope_embeddings,
    tuple(scope_df["id"]),
    method,
    metric,
    n_clusters,
)
scope_df["cluster"] = cluster_labels

cluster_by_id = dict(zip(scope_df["id"], scope_df["cluster"]))
display_df = base_df.loc[display_mask].copy()
display_df["cluster"] = display_df["id"].map(cluster_by_id)
display_df = display_df.dropna(subset=["cluster"])
display_df["cluster"] = display_df["cluster"].astype(int)
display_df = add_cluster_summaries(display_df)

clustered_scope_df = add_cluster_summaries(scope_df)

st.caption(
    f"{len(display_df):,} displayed papers · {len(scope_df):,} clustered papers · "
    f"{n_clusters} clusters · embedding model: `{embedding_model}`"
)

tab_scatter, tab_dendrogram, tab_table = st.tabs(
    ["Map", "Hierarchy", "Cluster Table"]
)

with tab_scatter:
    fig = px.scatter(
        display_df,
        x="x",
        y="y",
        color="cluster_name",
        symbol="super_category",
        hover_name="label",
        hover_data={
            "title": True,
            "year": True,
            "current_path": True,
            "tags": True,
            "x": False,
            "y": False,
            "cluster_name": False,
        },
        height=760,
    )
    fig.update_traces(marker=dict(size=9, opacity=0.82), selector=dict(mode="markers"))
    fig.update_layout(
        legend_title_text="Cluster",
        margin=dict(l=10, r=10, t=20, b=10),
        xaxis=dict(visible=False),
        yaxis=dict(visible=False, scaleanchor="x", scaleratio=1),
    )
    st.plotly_chart(fig, width="stretch")

with tab_dendrogram:
    st.caption(
        "Dendrogram leaves are cluster centroids, so it stays readable while still "
        "showing how the cut clusters relate to one another."
    )
    dendrogram = centroid_dendrogram(
        clustered_scope_df,
        scope_embeddings,
        method,
        metric,
        max_dendrogram_leaves,
    )
    if dendrogram is None:
        st.info("Need at least two clusters for a dendrogram.")
    else:
        st.plotly_chart(dendrogram, width="stretch")

with tab_table:
    cluster_options = sorted(display_df["cluster_name"].unique())
    selected_cluster_name = st.selectbox("Inspect cluster", cluster_options)
    selected_cluster = int(selected_cluster_name.split(":", 1)[0])
    selected = display_df[display_df["cluster"] == selected_cluster].sort_values(
        ["current_path", "year", "label"],
        ascending=[True, True, True],
    )

    st.metric("Papers in selected cluster", len(selected))
    st.write(describe_cluster(selected))
    st.dataframe(
        selected[
            [
                "label",
                "title",
                "year",
                "current_path",
                "tags",
                "id",
            ]
        ],
        width="stretch",
        hide_index=True,
    )
