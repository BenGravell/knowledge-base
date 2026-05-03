import streamlit as st

from arxiv_utils import build_metadata, fetch_arxiv, metadata_to_yaml, target_path
from knowledge_base.config import VALID_TYPES

# ---------------------------------------------------------------------------
# Session state defaults
# ---------------------------------------------------------------------------

FIELD_DEFAULTS: dict = {
    "title": "",
    "algorithm": "",
    "authors": [],
    "year": 2008,
    "source": "",
    "paper_type": "Conference Paper",
    "doi": "",
    "arxiv_id": "",
    "tags_raw": "",
    "abstract": "",
    "summary": "",
    "link": "",
    "links_alt_raw": "",
}

for key, default in FIELD_DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = default


# ---------------------------------------------------------------------------
# Step 1 - fetch from arXiv
# ---------------------------------------------------------------------------

st.header("Fetch from arXiv")


raw_id = st.text_input("arXiv ID", placeholder="e.g. 2403.10745")

fetch_clicked = st.button("Fetch", use_container_width=False)

data = {}
if fetch_clicked and raw_id.strip():
    with st.spinner("Fetching from arXiv…"):
        try:
            data = fetch_arxiv(raw_id.strip())
            st.session_state.update(
                {
                    "title": data["title"],
                    "authors": data["authors"],
                    "year": data["year"],
                    "abstract": data["abstract"],
                    "arxiv_id": data["arxiv_id"],
                    "link": data["link"],
                }
            )
            st.success("Fetched successfully.")
        except Exception as exc:
            st.error(f"Failed to fetch: {exc}")

if link := data.get("link"):
    st.link_button("arXiv Link", link)

# ---------------------------------------------------------------------------
# Step 2 - edit fields
# ---------------------------------------------------------------------------

st.header("Edit Fields")

st.session_state["title"] = st.text_input("Title *", value=st.session_state["title"])
st.session_state["algorithm"] = st.text_input(
    "Algorithm / Short name", value=st.session_state["algorithm"]
)
st.session_state["year"] = st.number_input(
    "Year *", value=st.session_state["year"], step=1, format="%d"
)
st.session_state["arxiv_id"] = st.text_input(
    "arXiv ID", value=st.session_state["arxiv_id"]
)
st.session_state["doi"] = st.text_input(
    "DOI", value=st.session_state["doi"], placeholder="10.1109/…"
)
st.session_state["link"] = st.text_input("Primary link", value=st.session_state["link"])

st.session_state["source"] = st.text_input(
    "Venue / Source *",
    value=st.session_state["source"],
    placeholder="IEEE International Conference on Robotics and Automation (ICRA)",
)
current_type = st.session_state["paper_type"]
type_index = VALID_TYPES.index(current_type) if current_type in VALID_TYPES else 0
st.session_state["paper_type"] = st.selectbox("Type *", VALID_TYPES, index=type_index)
authors_text = st.text_area(
    "Authors * (one per line)",
    value="\n".join(st.session_state["authors"]),
    height=120,
)
st.session_state["authors"] = [
    a.strip() for a in authors_text.splitlines() if a.strip()
]

st.session_state["tags_raw"] = st.text_area(
    "Tags (one per line)",
    value=st.session_state["tags_raw"],
    height=120,
    placeholder="Motion planning\nRRT\nKinodynamic",
)
st.session_state["links_alt_raw"] = st.text_area(
    "Alternative links (one per line)",
    value=st.session_state["links_alt_raw"],
    height=120,
)


st.session_state["abstract"] = st.text_area(
    "Abstract", value=st.session_state["abstract"], height=180
)
st.session_state["summary"] = st.text_area(
    "Summary (your one-paragraph digest)",
    value=st.session_state["summary"],
    height=120,
    placeholder="Briefly describe the key contribution and why it matters…",
)

# ---------------------------------------------------------------------------
# Step 3 - preview YAML
# ---------------------------------------------------------------------------

st.header("Preview")

metadata = build_metadata(
    {
        "title": st.session_state["title"],
        "algorithm": st.session_state["algorithm"],
        "authors": st.session_state["authors"],
        "year": int(st.session_state["year"]),
        "source": st.session_state["source"],
        "type": st.session_state["paper_type"],
        "doi": st.session_state["doi"],
        "arxiv_id": st.session_state["arxiv_id"],
        "tags_raw": st.session_state["tags_raw"],
        "abstract": st.session_state["abstract"],
        "summary": st.session_state["summary"],
        "link": st.session_state["link"],
        "links_alt_raw": st.session_state["links_alt_raw"],
    }
)

yaml_preview = metadata_to_yaml(metadata)
st.code(yaml_preview, language="yaml")

out_path = target_path(
    st.session_state["arxiv_id"] or "UNKNOWN",
    int(st.session_state["year"]),
)
st.caption(f"Will write to: `{out_path}`")

# ---------------------------------------------------------------------------
# Step 4 - write to disk
# ---------------------------------------------------------------------------

st.header("Write Entry")

ready = bool(
    st.session_state["title"]
    and st.session_state["authors"]
    and st.session_state["year"]
)

if not ready:
    st.info("Fill in at least Title, Authors, and Year before writing.")

if out_path.exists():
    st.warning(f"`{out_path}` already exists - writing will overwrite it.")

write_clicked = st.button("Write metadata.yml", disabled=not ready, type="primary")

if write_clicked:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(yaml_preview, encoding="utf-8")
    st.success(f"Written to `{out_path}`")
