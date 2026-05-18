import html
import json
import re
import yaml
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote, unquote, urlparse
import mkdocs_gen_files
from jinja2 import Environment
from knowledge_base.utils.arxiv_utils import (
    arxiv_abs_url,
    arxiv_html_url,
    arxiv_pdf_url,
    normalize_arxiv_id,
)
from knowledge_base.utils.paper_ids import paper_id_from_metadata

try:
    import numpy as np
except Exception:  # pragma: no cover - build fallback for environments without numpy
    np = None

# Root folder for metadata
metadata_root = Path("docs/papers")
template_file = Path("docs/templates/paper_template.md")
generated_root = Path("papers")
embedding_cache_file = Path("mind_map/embedding_cache.json")
related_result_limit = 36

# Read template
template_text = template_file.read_text()

def paper_id_for(metadata_file: Path, data: dict) -> str:
    return paper_id_from_metadata(metadata_file, data, metadata_root)


def normalize_tag_key(tag: str) -> str:
    return re.sub(r"\s+", " ", clean_scalar(tag)).casefold()


def metadata_text_html(text):
    """Render metadata text as HTML paragraphs without Markdown/math parsing."""
    text = str(text or "").strip()
    if not text:
        return ""

    paragraphs = re.split(r"\n\s*\n", text)
    rendered = []
    for paragraph in paragraphs:
        lines = [html.escape(line.strip(), quote=False) for line in paragraph.splitlines()]
        body = "<br>\n".join(line for line in lines if line)
        if body:
            rendered.append(f"<p>{body}</p>")
    return "\n".join(rendered)


def clean_scalar(value) -> str:
    return str(value or "").strip()


def as_links(value) -> list[str]:
    if isinstance(value, list):
        return [clean_scalar(item) for item in value if clean_scalar(item)]
    text = clean_scalar(value)
    return [text] if text else []


def normalize_url_key(url: str) -> str:
    parsed = urlparse(clean_scalar(url))
    if not parsed.scheme or not parsed.netloc:
        return clean_scalar(url).rstrip("/")
    path = parsed.path.rstrip("/")
    query = f"?{parsed.query}" if parsed.query else ""
    return f"{parsed.scheme.lower()}://{parsed.netloc.lower().removeprefix('www.')}{path}{query}"


def clean_doi(doi: str | None) -> str:
    text = clean_scalar(doi)
    text = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", text, flags=re.IGNORECASE)
    return text


def clean_arxiv_id(arxiv_id: str | None) -> str:
    return normalize_arxiv_id(arxiv_id)


def link_domain(url: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc.lower().removeprefix("www.")
    return host or url


def alternate_link_label(url: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc.lower().removeprefix("www.")
    path = parsed.path.strip("/")
    lower_path = path.lower()

    if "github.com" in host:
        parts = [part for part in path.split("/") if part]
        if len(parts) >= 2:
            return f"GitHub: {parts[0]}/{parts[1]}"
        return "GitHub"
    if "wikipedia.org" in host:
        parts = [part for part in path.split("/") if part]
        if len(parts) >= 2 and parts[0].lower() == "wiki":
            article = unquote(parts[1]).replace("_", " ")
            return f"Wikipedia: {article}"
        return "Wikipedia"
    if "doi.org" in host:
        return "DOI"
    if "arxiv.org" in host:
        if lower_path.startswith("abs/"):
            return "arXiv Abstract"
        if lower_path.startswith("pdf/"):
            return "arXiv PDF"
        if lower_path.startswith("html/"):
            return "arXiv HTML"
        return "arXiv"
    if "ar5iv" in host:
        return "ar5iv HTML"
    if "openreview.net" in host:
        return "OpenReview"
    if "openalex.org" in host:
        return "OpenAlex"
    if "huggingface.co" in host:
        parts = [part for part in path.split("/") if part]
        if len(parts) >= 2:
            return f"Hugging Face: {parts[0]}/{parts[1]}"
        return "Hugging Face"
    if "zenodo.org" in host:
        return "Zenodo"
    if lower_path.endswith(".pdf"):
        return f"{host} PDF" if host else "PDF"
    return host or url


def make_link(
    label: str,
    url: str,
    detail: str = "",
    variant: str = "secondary",
    external: bool = True,
) -> dict[str, str | bool]:
    return {
        "label": label,
        "url": url,
        "detail": detail,
        "variant": variant,
        "external": external,
    }


def build_tag_links(tags: list[str], paper_id: str) -> list[dict[str, str]]:
    links = []
    quoted_paper_id = quote(paper_id, safe="")
    for tag in tags or []:
        label = clean_scalar(tag)
        if not label:
            continue
        links.append(
            {
                "label": label,
                "url": f"../../tag-search/?paper={quoted_paper_id}&tag={quote(label, safe='')}",
            }
        )
    return links


def build_link_sections(data: dict, paper_id: str) -> list[dict]:
    primary = clean_scalar(data.get("link"))
    arxiv_id = clean_arxiv_id(data.get("arxiv_id"))
    doi = clean_doi(data.get("doi"))
    sections = []
    quoted_paper_id = quote(paper_id, safe="")

    sections.append(
        {
            "title": "Knowledge Base",
            "kind": "internal",
            "links": [
                make_link(
                    "Open in Content Tree",
                    f"../../content-tree/#paper={quoted_paper_id}",
                    "",
                    "internal",
                    False,
                ),
                make_link(
                    "Open in Mind Map",
                    f"../../mind-map/#paper={quoted_paper_id}",
                    "",
                    "internal",
                    False,
                ),
            ],
        }
    )

    if primary:
        sections.append(
            {
                "title": "Primary",
                "kind": "primary",
                "links": [make_link("Paper", primary, "", "primary")],
            }
        )

    standard_links = []
    standard_seen = set()

    def add_standard(label: str, url: str) -> None:
        key = normalize_url_key(url)
        if key not in standard_seen:
            standard_seen.add(key)
            standard_links.append(make_link(label, url, "", "standard"))

    if arxiv_id:
        add_standard(f"arXiv Abstract: {arxiv_id}", arxiv_abs_url(arxiv_id))
        add_standard(f"arXiv PDF: {arxiv_id}", arxiv_pdf_url(arxiv_id))
        add_standard(f"arXiv HTML: {arxiv_id}", arxiv_html_url(arxiv_id))
    if doi:
        add_standard(f"DOI: {doi}", f"https://doi.org/{doi}")

    if standard_links:
        sections.append({"title": "Standard", "kind": "standard", "links": standard_links})

    alternate_links = []
    alternate_seen = {normalize_url_key(primary)} if primary else set()
    alternate_seen.update(standard_seen)
    for url in as_links(data.get("links_alt")):
        key = normalize_url_key(url)
        if key in alternate_seen:
            continue
        alternate_seen.add(key)
        alternate_links.append(
            make_link(alternate_link_label(url), url, "", "alternate")
        )

    if alternate_links:
        sections.append({"title": "Alternate", "kind": "alternate", "links": alternate_links})

    return sections


def paper_record(data: dict, paper_id: str) -> dict:
    authors = data.get("authors") or []
    if not isinstance(authors, list):
        authors = [clean_scalar(authors)] if clean_scalar(authors) else []
    tags = data.get("tags") or []
    if not isinstance(tags, list):
        tags = [clean_scalar(tags)] if clean_scalar(tags) else []
    return {
        "id": paper_id,
        "title": clean_scalar(data.get("title")),
        "label": clean_scalar(data.get("algorithm")) or clean_scalar(data.get("title")) or paper_id,
        "authors": [clean_scalar(author) for author in authors if clean_scalar(author)],
        "year": data.get("year") or "",
        "tags": [clean_scalar(tag) for tag in tags if clean_scalar(tag)],
        "summary": clean_scalar(data.get("summary")),
        "url": f"../papers/{paper_id}/",
        "contentTreeUrl": f"../content-tree/#paper={quote(paper_id, safe='')}",
        "mindMapUrl": f"../mind-map/#paper={quote(paper_id, safe='')}",
    }


def load_embedding_cache() -> dict[str, list[float]]:
    if not embedding_cache_file.exists():
        return {}
    try:
        cache = json.loads(embedding_cache_file.read_text(encoding="utf-8"))
    except Exception:
        return {}
    papers = cache.get("papers") if isinstance(cache, dict) else None
    if not isinstance(papers, dict):
        return {}
    embeddings = {}
    for paper_id, entry in papers.items():
        embedding = entry.get("embedding") if isinstance(entry, dict) else None
        if isinstance(embedding, list) and embedding:
            embeddings[str(paper_id)] = embedding
    return embeddings


def build_tag_search_data(records: list[dict]) -> dict:
    record_by_id = {record["id"]: record for record in records}
    tag_members: dict[str, list[str]] = defaultdict(list)
    tag_labels: dict[str, str] = {}

    for record in records:
        seen = set()
        for tag in record["tags"]:
            key = normalize_tag_key(tag)
            if not key or key in seen:
                continue
            seen.add(key)
            tag_members[key].append(record["id"])
            tag_labels.setdefault(key, tag)

    embeddings = load_embedding_cache()
    related: dict[str, list[dict[str, str | float]]] = {}

    if np is not None and embeddings:
        embedded_ids = [record["id"] for record in records if record["id"] in embeddings]
        if embedded_ids:
            matrix = np.asarray([embeddings[paper_id] for paper_id in embedded_ids], dtype=np.float32)
            norms = np.linalg.norm(matrix, axis=1, keepdims=True)
            norms[norms == 0] = 1.0
            matrix = matrix / norms
            row_for_id = {paper_id: i for i, paper_id in enumerate(embedded_ids)}

            for tag_key, ids in tag_members.items():
                embedded_tag_ids = [paper_id for paper_id in ids if paper_id in row_for_id]
                if len(embedded_tag_ids) < 2:
                    continue
                rows = np.asarray([row_for_id[paper_id] for paper_id in embedded_tag_ids])
                sim = matrix[rows] @ matrix[rows].T
                for local_i, ego_id in enumerate(embedded_tag_ids):
                    order = np.argsort(-sim[local_i])
                    items = []
                    for local_j in order:
                        other_id = embedded_tag_ids[int(local_j)]
                        if other_id == ego_id:
                            continue
                        items.append(
                            {
                                "id": other_id,
                                "score": round(float(sim[local_i, int(local_j)]), 4),
                            }
                        )
                        if len(items) >= related_result_limit:
                            break
                    related[f"{ego_id}::{tag_key}"] = items

    for tag_key, ids in tag_members.items():
        ordered = sorted(
            ids,
            key=lambda paper_id: (
                -int(record_by_id[paper_id]["year"] or 0)
                if str(record_by_id[paper_id]["year"]).isdigit()
                else 0,
                record_by_id[paper_id]["label"].casefold(),
            ),
        )
        for ego_id in ids:
            key = f"{ego_id}::{tag_key}"
            if key in related:
                continue
            related[key] = [
                {"id": paper_id}
                for paper_id in ordered
                if paper_id != ego_id
            ][:related_result_limit]

    return {
        "papers": record_by_id,
        "tags": tag_labels,
        "related": related,
        "meta": {
            "resultLimit": related_result_limit,
            "ranking": "sentence-embedding cosine similarity when available",
        },
    }


# Set up Jinja2 environment with custom filter
env = Environment()
env.filters["metadata_text_html"] = metadata_text_html

paper_records = []

# Iterate over all YAML files
for metadata_file in metadata_root.rglob("*.yml"):
    with open(metadata_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        continue

    paper_id = paper_id_for(metadata_file, data)
    filename = f"{paper_id}.md"

    output_path = generated_root / filename

    mkdocs_gen_files.set_edit_path(output_path, metadata_file)
    with mkdocs_gen_files.open(output_path, "w") as f_out:
        template = env.from_string(template_text)
        data["link_sections"] = build_link_sections(data, paper_id)
        data["tag_links"] = build_tag_links(data.get("tags") or [], paper_id)
        f_out.write(template.render(**data))

    paper_records.append(paper_record(data, paper_id))

    # # DEBUG: actually write out to real filesystem
    # output_path.parent.mkdir(parents=True, exist_ok=True)
    # with open(output_path, "w") as f_disk:
    #     f_disk.write(template.render(**data))

with mkdocs_gen_files.open("javascripts/tag-search-data.js", "w") as out:
    out.write("window.tagSearchData = ")
    out.write(json.dumps(build_tag_search_data(paper_records), indent=2, ensure_ascii=False))
    out.write(";\n")
