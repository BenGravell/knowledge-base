# TODO

## Claude instructions (skills?)

### mkdocs content tree

Run

cd "c:\Users\bjgra\GitHub\knowledge-base\knowledge_base" && python scripts/list_raw_papers.py --max-results 5

and insert the entries into the Content Tree in knowledge_base\mkdocs.yml at appropriate places. Attempt to use the existing categories as much as possible, but create new categories if the entry does not fit cleanly conceptually.

### Generate new metadata

Fill the metadata for each of the papers in todo\reinforcement_learning.md using knowledge_base\docs\templates\metadata.yml as the template from which to create the new files. Use the subsection headers to guide where to add an entry for each paper in the hierarchy in knowledge_base\mkdocs.yml.

Each new metadata file should be placed in the path location knowledge_base\docs\papers\YEAR\SLUG\metadata.yml where

- YEAR is the 4 digit year in which the earliest version of the paper was published
- SLUG is either the arXiv ID like YYMM.NNNNN if the arXiv ID exists, or YEAR.first_author_last_name_lowercase.title_first_four_words if not.

Leave the "abstract" field blank with a placeholder ">" and newline in the value.

Normalize the title so that it uses capitalized words in title case.

### Prep raw metadata for review

Run scripts\list_raw_papers.py and pipe the output to scripts\audit_metadata.py and attempt to resolve all the issues.

## Metadata cleanup

- go thru all the handwritten notes and make sure they end up in the docs metadata

- revise the metadata schema:
  - notes: handwritten note from myself
  - algorithms: list instead of single entry
  - links: single list instead of primary + alt. maybe also include a specifier to indicate if the link leads to an open-able pdf or not

clarify distinction between year of first publication (typically arxiv preprint) and year of official publication

add other URIs besides DOI since not all papers have DOI e.g. dissertations, arxiv papers, PLMR and JMLR

- Add validation on mkdocs.yml
  - ensure every linked doc actually exists
  - ensure every paper in the docs source has a reference in mkdocs.yml (no dead data)

- Autogenerate the key for papers
  - policy: use algorithm if non-null, else use the paper name

## Quality of life

Create a one-click site regen script.

Should call:

- audit metadata
- embedding regen
- mkdocs build

Take an argument -g or --github to use gh-deploy mkdocs

Work on using AI automation to prefill the manual touch tasks:

1. Tags
2. Summary
3. Alt links
4. Placement in content tree

## Content tree

feature: Create a large form thing for the Content Tree landing page that enables users to ergonomically traverse the tree.
Key mechanism is hiding branches that are not on the currently node ancestor chain and emphasizing the current node over ancestors and successors

Add a verbiage info statement that the content tree is just my personal interpretation of organizing items in a hierarchical way, and that multiple alternative organizations are possible, and that content does not literally have a tree structure and other associations exist in a more general graph.

Then what is the value of a tree if the true info associations are more general?
- It provides structure for newcomers and encode some opinion (my own) about the most relevant/important connections

## Mind Map

Sluggish performance, laggy feeling when hovering and clicking on nodes and edges



Sidebar

Sort categories by their original order from the mkdocs content tree, not alphabetical order

Split large categories further until the number of entries in each leaf is no more than N, take N=16.



### Tune the edge threshold.

GRPO should be connected to PPO.


1312.0041 should be connected to the 1985 ERA paper by Juang and Pappa
Also to Identification of Observer/Kalman Filter Markov Parameters: Theory and Experiments" by Juang, Phan, Horta & Longman, 1993

Tune edge weight threshold or revisit the text fed to embedding model, maybe we need more than the abstract.

Define a reference set of known connected/disconnected items and use that to tune the threshold


Make layout less busy, too cluttered in motion planning cluster
Do something about the unreadable clumps on motion planning


Use title case instead of all caps for "MOTION PLANNING" in the sidebar

Start with all supercategories (like Motion Planning) collapsed

Add a checkbox for supercategories (like Motion Planning) that can control aggregate active/inactive of its children, keeping all the checkboxes for the subcategories in sync automatically/dynamically

Add filters for paper type (exclude surveys)


### Creative idea

Turn the mind map into a generative game like a cave crawler or rogue-like

Encourage exploration between rooms or lands represented by research items

Collect points for clicking links, answering quiz questions.

## Knowledge Explorer

<https://www.litmaps.com/about/us>

<https://chatgpt.com/share/69d55fa0-e2dc-8332-b847-357e80355305>
<https://chatgpt.com/share/69d41a6e-df98-8333-bc8f-429f7f8717c3>

## Paper Deep Dive App

Paper details

- Add DOI link
- Add Google Scholar link
- Add https://www.connectedpapers.com/ link
    - ex. https://www.connectedpapers.com/main/4326d7e9933c77ff9dc53056c62ef6712d90c633/Sampling%20based-algorithms-for-optimal-motion-planning/graph

Add links for each paper to app.

- Google Scholar
- https://openalex.org/
- https://openknowledgemaps.org/
- https://www.researchrabbit.ai/
- https://incitefulmed.com/academic/

Link direct to pdf instead of abstract for arxiv papers.

<https://arxiv.org/pdf/2210.01744>

Provide HTML link for paper Explorer.

<https://ar5iv.org/abs/2210.01744>

<https://ar5iv.labs.arxiv.org/html/2210.01744>

## Analytics Explorer

- Streamlit app? Marimo notebook? backed by a DuckDB database?
- Details for individual paper pages
  - Try to render arXiv in the app window natively as much as possible
  - Add LLM ideation using a slim local model or call to external API, chat with the paper c.f. DeepWiki
- dashboard page with aggregation stats like papers by year, by topic, tag
- Add graph linking between papers to enhance cross-ideation grabbing ideas
- Add paper harvesting - which techniques come out on top based on reported results?


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



use-cases

“Show me all planning methods derived from DDP”
“Find shortest conceptual path between RRT and MPPI”


## Reading plans

- guide users thru papers in a nice sequence, with rationale provided as a pre amble
- can have a "view from above" that just hits the most important papers
- can have "deep dives" that go into weeds on topics

## Quiz questions

- phrase them like "knowledge checks"
- include content like concepts, experimental results, connections to other papers (differentials between papers to show incremental progress)
- add a difficulty indicator (easy, medium, hard)
- open ended responses for meditation
