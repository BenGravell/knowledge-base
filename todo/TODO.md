# TODO

## map

I think we lost the semantic similarity and tree similarity filters for selected node filters. That was a powerful tool that had good tunings. Restore it.

## fix

https://bengravell.github.io/knowledge-base/papers/1993_donald_kinodynamic_motion_planning/

Description is garbled, ocr garbage



## ingest

Need to find a way to represent and ingest all the numerous items in

todo/papers_misc

## perf

Tree and Timeline pages need major performance increase for handling large number of items.

## ux

Timeline
Settings
1. re-use the branch selector widget from Tree, Map pages. get rid of nested multiselector. combine branch selector with level of detail widget, including lockout for LoD coarser than selected branch (same as Map page settings)
2. streamline settings, make it more minimal like the Map page settings bar.

## Taxonomy

```sh
python -m knowledge_base.scripts.suggest_branch_subgroupings --max-results 1 --write-tree
```

```sh
python -m knowledge_base.scripts.suggest_branch_subgroupings --branch "First-Order Methods" --write-tree
```

```sh
python knowledge_base/scripts/list_branching_factor_violations.py --max-depth 4 --max-results 3 --ignore-too-few
```

```sh
python knowledge_base/scripts/list_branching_factor_violations.py --max-depth 3 --max-results 3
```

## Site

Use git-filter-repo. It is the modern, reliable way to remove a path from all reachable Git history.

Important caveat: this rewrites commit hashes. Everyone else should stop pushing, then reclone or hard-reset after you force-push. Also keep your gh-pages deploy branch conceptually separate: you want to remove knowledge_base/site/ from source history, not erase the deployed site branch.

Recommended flow:

### From somewhere outside your working repo

git clone --mirror <git@github.com>:USER/REPO.git knowledge-base-clean.git
cd knowledge-base-clean.git

### Install if needed

pipx install git-filter-repo
or:
brew install git-filter-repo

git filter-repo --path knowledge_base/site/ --invert-paths

git push --force --mirror
That removes knowledge_base/site/ from every branch and tag in the mirror’s history.

Then in your normal working clone, easiest is to reclone. If you keep the existing clone:

git fetch --all --prune
git reset --hard origin/main
Make sure .gitignore contains:

knowledge_base/site/
Then verify:

git rev-list --objects --all | rg 'knowledge_base/site/'
No output means the path is gone from reachable local history.

One more reality check: “completely” means removed from refs you control. Old clones, forks, PR refs, and GitHub’s internal unreachable-object cache may still retain it for a while. If this was just build-output cleanup, that’s fine. If it contained secrets, rotate them and contact GitHub Support to purge cached objects.

## Metadata cleanup

### Schema

Define the schema in a single source of truth doc.

- use pydantic?
- human-readable

- revise the metadata schema:
  - links: single list instead of primary + alt. maybe also include a specifier to indicate if the link leads to an open-able pdf or not

clarify distinction between year of first publication (typically arxiv preprint) and year of official publication

add other URIs besides DOI since not all papers have DOI e.g. dissertations, arxiv papers, PLMR and JMLR

## Quality of life

### Create a one-click site ingest script

Set up an automation orchestration script+skill to ingest from paper funnel, run prefill, ask ai for preliminary metadata fixup using audit script, generate map data, place papers in tree

## Map

### UX

#### filters

Selected node filter

Include more filters utilizing as many metadata fields as possible.

- author match
- Year range (plus and minus away from year of selected item)
- Tag (only show other items that have a tag in common)
- Source (only show other items that have thr same source)

Global filters

- author
- venue
- tag
- arxiv available
- doi available
Etc.

Tweak the settings ui for the selected node filter section. Checkmarks should not be so big, maybe use a more elegant toggle.

Clean up the settings menu ux layout. Fewer labels? Smaller buttons for single touch buttons like node labels vis, fit view.

## Data export (new feature)

Add an export button to get a json or csv of all currently displayed items
CSV should include one item per row. Tree ancestry in a column.
JSON can use tree hierarchy natively.

## Reading plans (new feature)

Hand-crafted

- guide users thru papers in a nice sequence, with rationale provided as a pre amble
- can have a "view from above" that just hits the most important papers
- can have "deep dives" that go into weeds on topics

## Quiz questions (new feature)

- phrase them like "knowledge checks"
- include content like concepts, experimental results, connections to other papers (differentials between papers to show incremental progress)
- add a difficulty indicator (easy, medium, hard)
- open ended responses for meditation

## Chain (New feature)

User picks two items and we show the graph chain of hops linking them.

- Using semantic similarity neighbor graph. edges only for nodes whose embedding cosine distance is below a certain threshold (which represents the notion of 'related papers'). shortest path solve.
- Tree taxonomy

## Dissertations page (new feature)

Create a special page (like a corner of a physical library) just for Dissertations and Theses. They belong in their own isolated section because

1. Dissertations usually just wrap several previously published papers together in a nice package, and hence are redundant and less useful for the primary corpus in Knowledge Base.
2. We want to honor the work of the authors.

For this page, the UX should operate more like a gallery or a bookshelf. Each dissertation should get rendered in a nice card with emphasis placed on the title, author, and year.

Include a link to the Advanced Search page for the selected dissertation's author.
