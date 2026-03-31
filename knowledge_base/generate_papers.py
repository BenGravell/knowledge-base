import yaml
import re
from pathlib import Path
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


def escape_markdown(text):
    """Escape all markdown special characters to render text verbatim."""
    chars = r"\`*_{}[]()#+-.!|>"
    return re.sub(r"([%s])" % re.escape(chars), r"\\\1", str(text))


# Set up Jinja2 environment with custom filter
env = Environment()
env.filters["escape_markdown"] = escape_markdown

# Iterate over all YAML files
for metadata_file in metadata_root.rglob("*.yml"):
    with open(metadata_file) as f:
        data = yaml.safe_load(f)

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
        f_out.write(template.render(**data))

    # # DEBUG: actually write out to real filesystem
    # output_path.parent.mkdir(parents=True, exist_ok=True)
    # with open(output_path, "w") as f_disk:
    #     f_disk.write(template.render(**data))
