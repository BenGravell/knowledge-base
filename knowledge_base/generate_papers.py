import html
import re
import yaml
from pathlib import Path
from urllib.parse import urlparse
import mkdocs_gen_files
from jinja2 import Environment

# Root folder for metadata
metadata_root = Path("docs/papers")
template_file = Path("docs/templates/paper_template.md")
generated_root = Path("papers")

# Read template
template_text = template_file.read_text()

def slugify(name: str) -> str:
    """Simple slugify: lower case, replace spaces and non-alphanumerics with underscore."""
    return re.sub(r"[^a-zA-Z0-9]+", "_", name.lower()).strip("_")


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
    text = clean_scalar(arxiv_id)
    text = re.sub(r"^arxiv:\s*", "", text, flags=re.IGNORECASE)
    return text


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
        return "Hugging Face"
    if "zenodo.org" in host:
        return "Zenodo"
    if lower_path.endswith(".pdf"):
        return f"{host} PDF" if host else "PDF"
    return host or url


def make_link(label: str, url: str, detail: str = "", variant: str = "secondary") -> dict[str, str]:
    return {
        "label": label,
        "url": url,
        "detail": detail,
        "variant": variant,
    }


def build_link_sections(data: dict) -> list[dict]:
    primary = clean_scalar(data.get("link"))
    arxiv_id = clean_arxiv_id(data.get("arxiv_id"))
    doi = clean_doi(data.get("doi"))
    sections = []

    if primary:
        sections.append(
            {
                "title": "Primary",
                "kind": "primary",
                "links": [make_link("Paper", primary, link_domain(primary), "primary")],
            }
        )

    standard_links = []
    standard_seen = set()

    def add_standard(label: str, url: str, detail: str) -> None:
        key = normalize_url_key(url)
        if key not in standard_seen:
            standard_seen.add(key)
            standard_links.append(make_link(label, url, detail, "standard"))

    if arxiv_id:
        add_standard("arXiv Abstract", f"https://arxiv.org/abs/{arxiv_id}", arxiv_id)
        add_standard("arXiv PDF", f"https://arxiv.org/pdf/{arxiv_id}", arxiv_id)
        add_standard("arXiv HTML", f"https://arxiv.org/html/{arxiv_id}", arxiv_id)
    if doi:
        add_standard("DOI", f"https://doi.org/{doi}", doi)

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
            make_link(alternate_link_label(url), url, link_domain(url), "alternate")
        )

    if alternate_links:
        sections.append({"title": "Alternate", "kind": "alternate", "links": alternate_links})

    return sections


# Set up Jinja2 environment with custom filter
env = Environment()
env.filters["metadata_text_html"] = metadata_text_html

# Iterate over all YAML files
for metadata_file in metadata_root.rglob("*.yml"):
    with open(metadata_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        continue

    if "id" in data:
        filename = f"{slugify(data['id'])}.md"
    elif metadata_file.stem != "metadata":
        filename = f"{slugify(metadata_file.stem)}.md"
    else:
        filename = f"{slugify(metadata_file.parent.name)}.md"

    output_path = generated_root / filename

    mkdocs_gen_files.set_edit_path(output_path, metadata_file)
    with mkdocs_gen_files.open(output_path, "w") as f_out:
        template = env.from_string(template_text)
        data["link_sections"] = build_link_sections(data)
        f_out.write(template.render(**data))

    # # DEBUG: actually write out to real filesystem
    # output_path.parent.mkdir(parents=True, exist_ok=True)
    # with open(output_path, "w") as f_disk:
    #     f_disk.write(template.render(**data))
