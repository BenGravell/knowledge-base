"""Source registry for the table-driven prefill runner."""

from __future__ import annotations

from knowledge_base.config import REPO_ROOT
from knowledge_base.scripts.prefill.registry_sources import custom_source_specs
from knowledge_base.utils.prefill_template import SourceSpec


def _input(name: str):
    return REPO_ROOT / "todo" / "papers" / f"{name.upper()}.md"


def _simple_url_source(name: str, hint: str, needle: str) -> SourceSpec:
    return SourceSpec(
        name=name,
        description=f"Prefill metadata from {hint} URLs.",
        default_input=_input(name),
        mode="url_doi",
        entry_kind="URLs",
        source_hint=hint,
        accept_url=lambda url, needle=needle: needle in url,
    )


def source_specs() -> dict[str, SourceSpec]:
    sources = [
        _simple_url_source("annual_reviews", "Annual Reviews", "annualreviews.org/"),
        _simple_url_source("apa", "APA PsycNet", "psycnet.apa.org/"),
        _simple_url_source("imaging_science", "Imaging Science", "library.imaging.org/"),
        _simple_url_source("optica", "Optica", "opg.optica.org/"),
        _simple_url_source("sage", "SAGE", "journals.sagepub.com/"),
        _simple_url_source("science", "Science", "science.org/"),
        _simple_url_source("siam", "SIAM", "epubs.siam.org/"),
        _simple_url_source("wiley", "Wiley", "onlinelibrary.wiley.com/"),
        *custom_source_specs(_input),
    ]
    return {source.name: source for source in sources}
