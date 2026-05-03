import re
import xml.etree.ElementTree as ET
from pathlib import Path

import requests
import streamlit as st
import yaml

PAPERS_DIR = Path("docs/papers")
ARXIV_API = "https://export.arxiv.org/api/query?id_list={arxiv_id}"
ARXIV_NS = "http://www.w3.org/2005/Atom"

st.set_page_config(page_title="arXiv Paper Entry Generator", layout="wide")
st.title("Paper Entry Generator")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def fetch_arxiv(arxiv_id: str) -> dict:
    """Fetch basic metadata from the arXiv Atom API and return a dict."""
    url = ARXIV_API.format(arxiv_id=arxiv_id.strip())
    r = requests.get(url, timeout=60)
    r.raise_for_status()

    root = ET.fromstring(r.text)
    entry = root.find(f"{{{ARXIV_NS}}}entry")
    if entry is None:
        raise ValueError(f"No entry found for arXiv ID '{arxiv_id}'")

    def text(tag: str) -> str:
        el = entry.find(f"{{{ARXIV_NS}}}{tag}")
        return el.text.strip() if el is not None and el.text else ""

    title = re.sub(r"\s+", " ", text("title"))
    abstract = re.sub(r"\s+", " ", text("summary"))
    published = text("published")  # e.g. "2024-03-16T00:00:00Z"
    year = int(published[:4]) if published else 0

    authors = []
    for a in entry.findall(f"{{{ARXIV_NS}}}author"):
        name_el = a.find(f"{{{ARXIV_NS}}}name")
        if name_el is not None and name_el.text:
            authors.append(name_el.text.strip())

    return {
        "title": title,
        "authors": authors,
        "year": year,
        "abstract": abstract,
        "arxiv_id": arxiv_id.strip(),
        "link": f"https://arxiv.org/pdf/{arxiv_id.strip()}",
    }


def build_metadata(fields: dict) -> dict:
    """Return an ordered dict ready to serialise as YAML."""
    tags_raw: str = fields.get("tags_raw", "")
    tags = [t.strip() for t in tags_raw.splitlines() if t.strip()]

    links_alt_raw: str = fields.get("links_alt_raw", "")
    links_alt = [ln.strip() for ln in links_alt_raw.splitlines() if ln.strip()]

    return {
        "title": fields["title"],
        "algorithm": fields.get("algorithm") or None,
        "authors": fields["authors"],
        "year": fields["year"],
        "source": fields.get("source") or None,
        "type": fields.get("type", ""),
        "doi": fields.get("doi") or None,
        "arxiv_id": fields.get("arxiv_id") or None,
        "tags": tags,
        "abstract": fields.get("abstract", ""),
        "summary": fields.get("summary", ""),
        "link": fields.get("link", ""),
        "links_alt": links_alt,
    }


def metadata_to_yaml(metadata: dict) -> str:
    """Serialise metadata to a YAML string matching the project style."""
    lines: list[str] = []

    def add(key: str, value) -> None:
        if value is None:
            lines.append(f"{key}:")
        elif isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
        elif key == "arxiv_id":
            lines.append(f'{key}: "{value}"')
        elif isinstance(value, str) and len(value) > 80:
            # Block scalar for long strings
            lines.append(f"{key}: >")
            lines.append(f"  {value}")
        else:
            lines.append(yaml.dump({key: value}, default_flow_style=False).rstrip())

    for key, val in metadata.items():
        add(key, val)

    return "\n".join(lines) + "\n"


def target_path(arxiv_id: str, year: int) -> Path:
    return PAPERS_DIR / str(year) / arxiv_id / "metadata.yml"


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

PAPER_TYPES = [
    "Conference Paper",
    "Journal Paper",
    "Workshop Paper",
    "Preprint",
    "Technical Report",
    "Other",
]


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
type_index = PAPER_TYPES.index(current_type) if current_type in PAPER_TYPES else 0
st.session_state["paper_type"] = st.selectbox("Type *", PAPER_TYPES, index=type_index)
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
