# TODO

## Ingest

Perform agent task
"### Generate metadata for a group of papers"
for
todo/papers_misc/001_autonomous_driving_and_av_01.md

## ConLab scrape

<https://labs.utdallas.edu/conlab/>

Pull content for portfolio

### Original research

<https://labs.utdallas.edu/conlab/learning-robust-control-for-lqr-systems-with-multiplicative-noise-via-policy-gradient/>
<https://labs.utdallas.edu/conlab/robust-learning-based-control-via-bootstrapped-multiplicative-noise/>
<https://labs.utdallas.edu/conlab/risk-averse-rrt-planning-with-nonlinear-steering-and-tracking-controllers-for-nonlinear-robotic-systems-under-uncertainty/>

### Resources

<https://labs.utdallas.edu/conlab/resources/>

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

## Quality of life

### Create a one-click site regen script

Should call:

- audit metadata
- embedding regen
- mkdocs build

Take an argument -g or --github to use gh-deploy mkdocs

Set up an automation orchestration script to invest from paper funnel, run prefill, ask ai for preliminary metadata fixup using audit script, generate mind map data, place papers in content tree

### Get mkdocs rebuilds faster

Incremental? other stuff / caching?

Back by a DuckDB database?

## Paper Detail Pages

### Links

- Google Scholar link
- <https://www.connectedpapers.com/>
  - ex. <https://www.connectedpapers.com/main/4326d7e9933c77ff9dc53056c62ef6712d90c633/Sampling%20based-algorithms-for-optimal-motion-planning/graph>
- <https://openalex.org/>
- <https://openknowledgemaps.org/>
- <https://www.researchrabbit.ai/>
- <https://incitefulmed.com/academic/>

Try to render arXiv in the app window natively as much as possible (using HTML when available)

### Chat with paper

Add LLM ideation using a slim local model or call to external API, chat with the paper c.f. DeepWiki

### Creative Idea: procedurally generated visual image anchor/thumbnail

Use the LLM sentence embedding and map it into a vision-language model embedding space and generate a relevant thumbnail image for the paper. Then we can show the thumbnail in the hover tooltip in mind map, in content tree, etc. everywhere the title string or other unique ID is used we can have the synthetic thumbnail too.

I am a visual learner, I use my eyes for cognition, so this would help me a lot.

### Related papers

Add a section with links to most closely related papers, either Top N or similarity threshold cutoff (variable N).

- Leverage the embeddings we already have, should be tied to the Mind Map
- Make the Top N / cutoff threshold a dynamic slider widget.

## Reading plans

Hand-crafted

- guide users thru papers in a nice sequence, with rationale provided as a pre amble
- can have a "view from above" that just hits the most important papers
- can have "deep dives" that go into weeds on topics

## Analytics

### UX

## Timeline

### Design inspiration

<https://pin.it/7kjN4B5KZ>

## Content Tree

### UX

### Targeted edits

Prediction horizon section has mjscategorized lane change scenarios item. Reorganize and remove prediction horizon,  move to safety/eval?

### Taxonomy guidance

Balance or expand tree to fix all issues reported by python scripts/list_branching_factor_violations.py

Use clustering algorithm results (hierarchical agg) to help set new categories.

## Mind Map

### UX

### Sidebar

Add filters for item type (e.g. to exclude surveys)

#### Branches

Make sure every branch goes 3 levels deep to sub category. This is a way to make the existing level of detail work properly in mind map. Otherwise it is unintuitive that when you click a node it might not split up.

## Knowledge Studio (new feature)

Tightly integrate the Mind Map, Timeline, and Content Tree into a single multi-panel studio.
They share an identical hierarchy.
The mind map can be shown on the side / top of the nav tree as a kind of minimap (Gran Turismo style).
It should focus on the currently selected branch by zooming and centering on it (not discarding the upper levels of hierarchy, just letting ancestors and other non descendent parts of the tree go off screen).

Edges in the mind map are not based on the embedding similarity at all, only the hierarchy from the content tree.

### Ideas

<https://www.litmaps.com/about/us>

<https://chatgpt.com/share/69d55fa0-e2dc-8332-b847-357e80355305>
<https://chatgpt.com/share/69d41a6e-df98-8333-bc8f-429f7f8717c3>

### Tune the edge threshold

GRPO should be connected to PPO.

1312.0041 should be connected to the 1985 ERA paper by Juang and Pappa
Also to Identification of Observer/Kalman Filter Markov Parameters: Theory and Experiments" by Juang, Phan, Horta & Longman, 1993

Tune edge weight threshold or revisit the text fed to embedding model, maybe we need more than the abstract.

Define a reference set of known connected/disconnected items and use that to tune the threshold

### Creative idea

Turn the mind map into a generative game like a cave crawler or rogue-like

Encourage exploration between rooms or lands represented by research items

Collect points for clicking links, answering quiz questions.

## Explainers

## Metadata cleanup

### scripts

Write audit script to check for identical content tree key label and algorithm field in metadata. Flag violations with both sides for manual resolution.

Write audit script to check for multiple metadata items claiming the same algorithm. Flag violations for manual resolution.

#### dollar sign / math

Add checked in audit for dollar signs in abstract

<https://bengravell.github.io/knowledge-base/papers/2015_nesterov_random_gradient_free_minimization_of/?h=spokoiny>

Fix math notation, make plain text readable.

### prefill

Arxiv prefill script should strip off version number from url if present before fetching data.

## normalization and de-duplication

Normalized authors to remove differently spelled duplicates. Align them to a central database of unique authors in the repo.

Eliminate initials in the author names for first and last name (middle initial ok and preferred).

Do same for source field (venues).

Create scripts for automatically creating the databases the first time, and for auditong and suggesting fix based on pattern matching

Audit the algorithm field.
It should only use an abbreviation representing a concrete algorithm if it was the first paper to propose thr algorithm. If it merely analyzes an existing algorithm, then it should be a phrase like "Adam convergence analysis"

### Add validation on mkdocs.yml

- ensure every linked doc actually exists
- ensure every paper in the docs source has a reference in mkdocs.yml (no dead data)

- Ensure every tail branch in tree has more than one leaf node / item. Use sparse tail branches to guide exploration

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

- Autogenerate the key for papers
  - policy: use algorithm if non-null, else use the paper name

## Metrics

Add scores/metrics:
Subjective importance
Novelty
Impact
Coolness

## Relations

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

### Use-cases, features enabled

“Show me all planning methods derived from DDP”
“Find shortest conceptual path between RRT and MPPI”

## Quiz questions

- phrase them like "knowledge checks"
- include content like concepts, experimental results, connections to other papers (differentials between papers to show incremental progress)
- add a difficulty indicator (easy, medium, hard)
- open ended responses for meditation
