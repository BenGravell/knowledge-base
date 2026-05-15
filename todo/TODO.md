# TODO

## Ingest

Perform agent task
"### Generate metadata for a group of papers"
for
todo/papers_misc/001_autonomous_driving_and_av_01.md

## Site

Use git-filter-repo. It is the modern, reliable way to remove a path from all reachable Git history.

Important caveat: this rewrites commit hashes. Everyone else should stop pushing, then reclone or hard-reset after you force-push. Also keep your gh-pages deploy branch conceptually separate: you want to remove knowledge_base/site/ from source history, not erase the deployed site branch.

Recommended flow:

# From somewhere outside your working repo

git clone --mirror <git@github.com>:USER/REPO.git knowledge-base-clean.git
cd knowledge-base-clean.git

# Install if needed

# pipx install git-filter-repo

# or: brew install git-filter-repo

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

## Paper Detail Pages

Paper details

- Add DOI link
- Add Google Scholar link
- Add <https://www.connectedpapers.com/> link
  - ex. <https://www.connectedpapers.com/main/4326d7e9933c77ff9dc53056c62ef6712d90c633/Sampling%20based-algorithms-for-optimal-motion-planning/graph>

Add links for each paper to app.

- Google Scholar
- <https://openalex.org/>
- <https://openknowledgemaps.org/>
- <https://www.researchrabbit.ai/>
- <https://incitefulmed.com/academic/>

Link direct to pdf instead of abstract for arxiv papers.

<https://arxiv.org/pdf/2210.01744>

Provide HTML link for paper Explorer.

<https://ar5iv.org/abs/2210.01744>

<https://ar5iv.labs.arxiv.org/html/2210.01744>

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

For the 'N items not displayed' make it clicksble to show more.

Paper by year
Make the bins start on 0 or 5 and end on 4 or 9

Each of the horizontal bars graphs should have the numeric count label placed above the bar (right justified), in line with the string label (left justified)

Flip the papers by year chart so it has horizontal bars. Also style them same as the other charts using the blue green gradient (not red pink). Use the red pink gradient for emphasizing the selected bar when mousing/hovering.

Place the most recent year at the top, oldest year at the bottom.

This is so it is consistent with the other charts and to give more space for bars especially on mobile.

Also put grid lines at the ticks where years are marked. This is to give a visual guide across multiple bars for easier eyeballing quantity comparison.

Rename "Content tree" section to "Categories" and remove the top n selector.

When clicking histogram bar, do not snap the hover tool tip to the top of the chart, put it in a stable constant position at the top of the bar.

Also make it possible to scroll over the bars when using finger touch on mobile site and have the hover tool tip follow

Rename "papers by year" to "items by year"

Perform same rename throughout the page, they are items not papers.

Get rid of title caption about number of items indexed since it is redundant, we already count it as the first big metric.

Rename big metric "papers" to "items"

Get rid of "unique" from the big metric labels for authors and tags, it is obvious from context just like the other metrics do not explicitly say unique.

## Timeline

Design inspiration:
https://pin.it/7kjN4B5KZ

## Content Tree

### Taxonomy guidance

Revise the content tree taxonomy

Use branching factor rule of 3 to 7, with sweet spot at 5.

Use clustering algorithm results (hierarchical agg) to help set new categories.

Balance or expand tree

Write a script to list insufficient subcategories.

## Mind Map

### UX

Revise the UX behavior.

Keep level of detail as it is - it should set the global level of detail/aggregation.

When clicking a branch node, it should show the children of the node (the branch disappears and is replaced by its children, one level of detail deeper) but keep the rest of the graph the same.

Make sure every branch goes 3 levels deep to sub category. This is a way to make the existing level of detail work properly in mind map. Otherwise it is unintuitive that when you click a node it might not split up.

Another way would be to skip lod expansion if node clicked has no child in the next overall lod

### Nodes style

https://bengravell.github.io/knowledge-base/mind-map/

Node disks at all levels of detail are a bit small, can bump up diameter probably 2x and look good. Paper level of detail should still enforce minimum disk clearance after the change. Higher level of detail can permit a small amount of overlap between disks.

### Rename

Rename "mind map" to "knowledge graph" because mind map is for a different concept that encode hierarchy in a flat way in one big graph

### True Mind Map (new feature)

Create a true mind map that shows the hierarchical relations directly in the graph. Super categories are big nodes and have edges to categories which have edges to subcategories which have edges to papers.

This can be tightly integrated with the content tree page since they share an identical hierarchy. The mind map can be shown on the side / top of the nav tree as a kind of minimap (Gran Turismo style). It should focus on the currently selected branch by zooming and centering on it (not discarding the upper levels of hierarchy, just letting ancestors and other non descendent parts of the tree go off screen).

Edges in the mind map are not based on the embedding similarity at all, only the hierarchy from the content tree.

### Ideas

<https://www.litmaps.com/about/us>

<https://chatgpt.com/share/69d55fa0-e2dc-8332-b847-357e80355305>
<https://chatgpt.com/share/69d41a6e-df98-8333-bc8f-429f7f8717c3>

### Sidebar

Add filters for item type (e.g. to exclude surveys)

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

### Edges

Edges opacity - autotune

edges still too bright on light mode

## Explainers

https://bengravell.github.io/knowledge-base/explainers/polyak_lojasiewicz/

Force equations to fit to container width, using scaling to achieve it. On mobile site with narrow width it induces a horizontal scroll bar which is undesirable.

https://bengravell.github.io/knowledge-base/explainers/pid/pid/

Bullet list for Ben Recht blog posts are not indenting properly.

Simulation of cartpole seems unrealistic when cart reaches world borders. It should rebound elastically on collision and not have any weird physical effects on the pole, forces should be transmitted properly.

## Metadata cleanup

Arxiv prefill script should strip off version number from url if present before fetching data.

Add checked in audit for dollar signs in abstract

https://bengravell.github.io/knowledge-base/papers/2015_nesterov_random_gradient_free_minimization_of/?h=spokoiny

Fix math notation, make plain text readable.

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


## Quality of life

### Get mkdocs rebuilds faster

Incremental? other stuff / caching?

Back by a DuckDB database?

### Create a one-click site regen script

Should call:

- audit metadata
- embedding regen
- mkdocs build

Take an argument -g or --github to use gh-deploy mkdocs

Set up an automation orchestration script to invest from paper funnel, run prefill, ask ai for preliminary metadata fixup using audit script, generate mind map data, place papers in content tree

## ConLab scrape

<https://labs.utdallas.edu/conlab/>

Pull content for portfolio

### Original research

<https://labs.utdallas.edu/conlab/learning-robust-control-for-lqr-systems-with-multiplicative-noise-via-policy-gradient/>
<https://labs.utdallas.edu/conlab/robust-learning-based-control-via-bootstrapped-multiplicative-noise/>
<https://labs.utdallas.edu/conlab/risk-averse-rrt-planning-with-nonlinear-steering-and-tracking-controllers-for-nonlinear-robotic-systems-under-uncertainty/>

### Resources

<https://labs.utdallas.edu/conlab/resources/>

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
