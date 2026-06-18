# TODO

## github.com/turbopuffer/alyze

My recommendation: do not integrate alyze for embeddings now. Do a small spike only if you want hybrid search. The minimal useful spike would be:
Build a tiny lexical inverted index from title, tags, summary, abstract, and embed_text.md.
Compare simple Python tokenization/BM25-ish scoring against alyze.
Keep alyze only if Unicode segmentation, stemming, or browser WASM speed visibly improves search quality.
One adjacent embedding improvement is worth considering first: chunk embed_text.md into passages, embed chunks, then aggregate or expose passage-level matches. all-MiniLM-L6-v2 is meant for sentences/short paragraphs and truncates long input, so feeding up to 60k characters as one paper vector is likely wasting useful full text.
Sources: turbopuffer/alyze README and source, Unicode UAX #29, FastEmbed docs, Transformers.js docs, Hugging Face model cards for mxbai-embed-large-v1 and all-MiniLM-L6-v2.


## perf

Tree and Timeline pages need major performance increase for handling large number of items.

## Taxonomy

```sh
poetry run python scripts/suggest_branch_subgroupings.py --max-results 1 --write-tree
```

```sh
poetry run python scripts/suggest_branch_subgroupings.py --branch "First-Order Methods" --write-tree
```

```sh
python scripts/list_branching_factor_violations.py --max-depth 4 --max-results 3 --ignore-too-few
```

```sh
python scripts/list_branching_factor_violations.py --max-depth 3 --max-results 3
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
  - notes: handwritten note from myself
  - algorithms: list instead of single entry
  - links: single list instead of primary + alt. maybe also include a specifier to indicate if the link leads to an open-able pdf or not

clarify distinction between year of first publication (typically arxiv preprint) and year of official publication

add other URIs besides DOI since not all papers have DOI e.g. dissertations, arxiv papers, PLMR and JMLR

## Quality of life

### Create a one-click site regen script

Should call:

- audit metadata
- embedding regen
- mkdocs build

Take an argument -g or --github to use gh-deploy mkdocs

### Create a one-click site ingest script

Set up an automation orchestration script to ingest from paper funnel, run prefill, ask ai for preliminary metadata fixup using audit script, generate map data, place papers in tree

## Paper Detail Pages

### Chat with paper

Add LLM ideation using a slim local model or call to external API, chat with the paper c.f. DeepWiki

### Creative Idea: procedurally generated visual image anchor/thumbnail

Use the LLM sentence embedding and map it into a vision-language model embedding space and generate a relevant thumbnail image for the paper. Then we can show the thumbnail in the hover tooltip in map, in tree, etc. everywhere the title string or other unique ID is used we can have the synthetic thumbnail too.

I am a visual learner, I use my eyes for cognition, so this would help me a lot.

### Related papers

Add a section with links to most closely related papers, either Top N or similarity threshold cutoff (variable N).

- Leverage the embeddings we already have, should be tied to the Map
- Make the Top N / cutoff threshold a dynamic slider widget.

## Reading plans

Hand-crafted

- guide users thru papers in a nice sequence, with rationale provided as a pre amble
- can have a "view from above" that just hits the most important papers
- can have "deep dives" that go into weeds on topics

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

### Data export

Add an export button to get a json or csv of all currently displayed items
CSV should include one item per row. Tree ancestry in a column.
JSON can use tree hierarchy natively.

## Search

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

## Ideas

<https://www.litmaps.com/about/us>

<https://chatgpt.com/share/69d55fa0-e2dc-8332-b847-357e80355305>
<https://chatgpt.com/share/69d41a6e-df98-8333-bc8f-429f7f8717c3>

### Creative idea

Turn the map into a generative game like a cave crawler or rogue-like

Encourage exploration between rooms or lands represented by research items

Collect points for clicking links, answering quiz questions.

### Metrics

Add scores/metrics:
Subjective importance
Novelty
Impact
Coolness

### Relations

- "generalizes": Ego paper provides some kind of result (algorithm, technique, proof, etc.) for which the result in the related paper is a special case, i.e. obtained by instantiating the general result with more specificity (e.g. parameters, mathematical space, problem regime, concepts, etc.)
- "criticizes": Ego paper asserts a claim that the result in the related paper is deficient in some way. Often this is found in the introductory literature review section. Ego paper is not obligated to improve on or resolve the criticisms (although many do).
- "improves on": Ego paper asserts a claim that its result is improved in some way (conceptually, empirically, numerically, theoretically, etc.) as compared with the result in the related paper.
- "synthesizes": Ego paper creates its result by using a literal result of the related paper as a smaller piece of a larger whole.
- "inspired by": Ego paper creates its result by using an idealogical result of the related paper. Directionally the same as the "synthesizes" relation, but weaker.
- “same family as”: Ego paper provides a result that shares key attributes ("DNA") with the result of the related paper.

“builds on X”
“similar to Y”
“competes with Z”

“extends”
“inspired by”
“compares to”
“same family as”
“uses idea”
“contradicts”

#### Use-cases, features enabled

“Show me all planning methods derived from DDP”
“Find shortest conceptual path between RRT and MPPI”

### Quiz questions

- phrase them like "knowledge checks"
- include content like concepts, experimental results, connections to other papers (differentials between papers to show incremental progress)
- add a difficulty indicator (easy, medium, hard)
- open ended responses for meditation
