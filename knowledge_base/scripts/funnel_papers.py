#!/usr/bin/env python3
"""Funnel URLs from todo/PAPERS_FUNNEL.md into topic-specific todo/papers/ files or PAPERS_MISC.md.

High-confidence items (URL domain matches a known academic publisher) go to the
corresponding todo/papers/<PUBLISHER>.md file.  Everything else goes to todo/PAPERS_MISC.md.

URLs already present in the destination file are skipped.

Usage:
    python funnel_papers.py [--dry-run]
"""

import argparse
import sys
from pathlib import Path
from urllib.parse import urlparse

from knowledge_base.config import REPO_ROOT

FUNNEL_FILE = REPO_ROOT / "todo" / "PAPERS_FUNNEL.md"
MISC_FILE = REPO_ROOT / "todo" / "PAPERS_MISC.md"
PAPERS_DIR = REPO_ROOT / "todo" / "papers"

# (domain_suffix, file_stem) — more-specific entries must come before broader ones
DOMAIN_RULES: list[tuple[str, str]] = [
    # arXiv
    ("arxiv.org", "ARXIV"),
    # IEEE
    ("ieeexplore.ieee.org", "IEEE"),
    # ACM
    ("dl.acm.org", "ACM"),
    ("acm.org", "ACM"),
    # NeurIPS / NIPS
    ("proceedings.neurips.cc", "NEURIPS"),
    ("papers.neurips.cc", "NEURIPS"),
    ("papers.nips.cc", "NEURIPS"),
    ("proceedings.nips.cc", "NEURIPS"),
    ("nips.cc", "NEURIPS"),
    # PMLR
    ("proceedings.mlr.press", "MLR"),
    # JMLR
    ("jmlr.csail.mit.edu", "JMLR"),
    ("jmlr.org", "JMLR"),
    # OpenReview
    ("openreview.net", "OPENREVIEW"),
    # Springer
    ("link.springer.com", "SPRINGER"),
    ("springer.com", "SPRINGER"),
    # Elsevier / ScienceDirect
    ("sciencedirect.com", "ELSEVIER"),
    ("linkinghub.elsevier.com", "ELSEVIER"),
    # Wiley (including society sub-sites)
    ("onlinelibrary.wiley.com", "WILEY"),
    ("wiley.com", "WILEY"),
    # SAGE
    ("journals.sagepub.com", "SAGE"),
    ("sagepub.com", "SAGE"),
    # Taylor & Francis
    ("tandfonline.com", "TAYLOR_FRANCIS"),
    ("taylorandfrancis.com", "TAYLOR_FRANCIS"),
    # JSTOR
    ("jstor.org", "JSTOR"),
    # ResearchGate
    ("researchgate.net", "RESEARCHGATE"),
    # Semantic Scholar
    ("semanticscholar.org", "SEMANTIC_SCHOLAR"),
    # MDPI
    ("mdpi.com", "MDPI"),
    # Oxford University Press
    ("academic.oup.com", "OUP"),
    ("oup.com", "OUP"),
    # SIAM
    ("epubs.siam.org", "SIAM"),
    ("siam.org", "SIAM"),
    # SPIE
    ("spiedigitallibrary.org", "IMAGING_SCIENCE"),
    ("spie.org", "IMAGING_SCIENCE"),
    # Annual Reviews
    ("annualreviews.org", "ANNUAL_REVIEWS"),
    # APA
    ("psycnet.apa.org", "APA"),
    ("apa.org", "APA"),
    # ASME
    ("asmedigitalcollection.asme.org", "ASME"),
    ("asme.org", "ASME"),
    # BMVA
    ("bmva.org", "BMVA"),
    # Dagstuhl
    ("drops.dagstuhl.de", "DAGSTUHL"),
    ("dagstuhl.de", "DAGSTUHL"),
    # MIT Press
    ("mitpress.mit.edu", "MIT_PRESS"),
    ("direct.mit.edu", "MIT_PRESS"),
    # MSP (Mathematical Sciences Publishers)
    ("msp.org", "MSP"),
    # Nature / NPG
    ("nature.com", "NATURE"),
    # NIST
    ("nist.gov", "NIST"),
    # Optica (formerly OSA)
    ("opg.optica.org", "OPTICA"),
    ("optica.org", "OPTICA"),
    ("osa.org", "OPTICA"),
    ("osapublishing.org", "OPTICA"),
    # Project Euclid
    ("projecteuclid.org", "PROJECT_EUCLID"),
    # RAND
    ("rand.org", "RAND"),
    # RSS (Robotics: Science and Systems)
    ("roboticsproceedings.org", "RSS"),
    ("roboticsconference.org", "RSS"),
    # Science / AAAS
    ("science.org", "SCIENCE"),
    ("sciencemag.org", "SCIENCE"),
    # USENIX
    ("usenix.org", "USENIX"),
    # NASA
    ("nasa.gov", "NASA"),
]


def classify(url: str) -> str | None:
    """Return the file stem for a high-confidence URL, else None."""
    try:
        netloc = urlparse(url).netloc.lower().removeprefix("www.")
    except Exception:
        return None
    for domain, stem in DOMAIN_RULES:
        if netloc == domain or netloc.endswith("." + domain):
            return stem
    return None


def load_url_set(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()}


def append_to_file(path: Path, urls: list[str], dry_run: bool) -> None:
    if dry_run:
        return
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    if existing and not existing.endswith("\n"):
        existing += "\n"
    path.write_text(existing + "\n".join(urls) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Print plan without writing files")
    args = parser.parse_args()

    raw_lines = FUNNEL_FILE.read_text(encoding="utf-8").splitlines()
    funnel_urls = [ln.strip() for ln in raw_lines if ln.strip()]

    if not funnel_urls:
        print("PAPERS_FUNNEL.md is empty — nothing to do.")
        return

    # Pre-load all existing URL sets for deduplication
    existing: dict[str, set[str]] = {"PAPERS_MISC": load_url_set(MISC_FILE)}
    for md in PAPERS_DIR.glob("*.md"):
        existing[md.stem] = load_url_set(md)

    routed: dict[str, list[str]] = {}
    skipped = 0

    seen_in_run: set[str] = set()  # dedup within this run
    for url in funnel_urls:
        if url in seen_in_run:
            skipped += 1
            continue
        seen_in_run.add(url)

        stem = classify(url)
        dest = stem if stem is not None else "PAPERS_MISC"

        if url in existing.get(dest, set()):
            skipped += 1
            continue

        routed.setdefault(dest, []).append(url)
        existing.setdefault(dest, set()).add(url)

    if not routed:
        print(f"Nothing new to funnel ({skipped} already present or duplicate).")
        return

    for dest, urls in sorted(routed.items()):
        target = MISC_FILE if dest == "PAPERS_MISC" else PAPERS_DIR / f"{dest}.md"
        tag = "[DRY RUN] " if args.dry_run else ""
        print(f"{tag}{dest} ({target.relative_to(REPO_ROOT)}): +{len(urls)}")
        for u in urls:
            print(f"    {u}")
        append_to_file(target, urls, args.dry_run)

    total = sum(len(v) for v in routed.values())
    mode = " (dry run — no files written)" if args.dry_run else ""
    print(f"\nFunneled {total} URL(s) across {len(routed)} file(s), skipped {skipped}{mode}.")


if __name__ == "__main__":
    main()
