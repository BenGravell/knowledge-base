import re
import xml.etree.ElementTree as ET
from pathlib import Path

import requests
import yaml

PAPERS_DIR = Path("docs/papers")
ARXIV_API = "https://export.arxiv.org/api/query?id_list={arxiv_id}"
ARXIV_NS = "http://www.w3.org/2005/Atom"


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
            lines.append(f"{key}: >")
            lines.append(f"  {value}")
        else:
            lines.append(yaml.dump({key: value}, default_flow_style=False).rstrip())

    for key, val in metadata.items():
        add(key, val)

    return "\n".join(lines) + "\n"


def target_path(arxiv_id: str, year: int) -> Path:
    return PAPERS_DIR / str(year) / arxiv_id / "metadata.yml"


def write_metadata(arxiv_id: str, year: int, yaml_text: str) -> Path:
    """Write yaml_text to the canonical metadata.yml path, creating dirs as needed."""
    path = target_path(arxiv_id, year)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml_text, encoding="utf-8")
    return path
