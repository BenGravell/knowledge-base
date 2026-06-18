RAPID: A Reachable Anytime Planner for Imprecisely-Sensed Domains

Topics include Partially observable planning, Factored dynamics, POMDPs, Anytime planning, State envelopes, Tutoring systems, Reachability analysis.

Presents RAPID, an anytime planner for structured POMDPs that first builds a compact envelope of states reachable under the fully observable optimal policy, then expands that envelope as computation permits. The paper's key value is exploiting topological structure inside factored dynamics, allowing a tutoring-scale domain with enormous flat state space to get useful partially observable plans without enumerating the full model.

Despite the intractability of generic optimal partially observable Markov decision process planning, there exist important problems that have highly structured models. Previous researchers have used this insight to construct more efficient algorithms for factored domains, and for domains with topological structure in the flat state dynamics model. In our work, motivated by findings from the education community relevant to automated tutoring, we consider problems that exhibit a form of topological structure in the factored dynamics model. Our Reachable Anytime Planner for Imprecisely-sensed Domains (RAPID) leverages this structure to efficiently compute a good initial envelope of reachable states under the optimal MDP policy in time linear in the number of state variables. RAPID performs partially-observable planning over the limited envelope of states, and slowly expands the state space considered as time allows. RAPID performs well on a large tutoring-inspired problem simulation with 122 state variables, corresponding to a flat state space of over 10^30 states.

Learn about arXiv becoming an independent nonprofit.{target="_blank"}

We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate

All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text

## quick links

## Computer Science \> Artificial Intelligence

## Title:RAPID: A Reachable Anytime Planner for Imprecisely-sensed Domains

Authors:Emma Brunskill{rel="nofollow"}, Stuart Russell{rel="nofollow"}

View a PDF of the paper titled RAPID: A Reachable Anytime Planner for Imprecisely-sensed Domains, by Emma Brunskill and 1 other authors

> Abstract:Despite the intractability of generic optimal partially observable Markov decision process planning, there exist important problems that have highly structured models. Previous researchers have used this insight to construct more efficient algorithms for factored domains, and for domains with topological structure in the flat state dynamics model. In our work, motivated by findings from the education community relevant to automated tutoring, we consider problems that exhibit a form of topological structure in the factored dynamics model. Our Reachable Anytime Planner for Imprecisely-sensed Domains (RAPID) leverages this structure to efficiently compute a good initial envelope of reachable states under the optimal MDP policy in time linear in the number of state variables. RAPID performs partially-observable planning over the limited envelope of states, and slowly expands the state space considered as time allows. RAPID performs well on a large tutoring-inspired problem simulation with 122 state variables, corresponding to a flat state space of over 10\^30 states.

## Submission history

From: Emma Brunskill \[view email{rel="nofollow"}\] \[via AUAI proxy\]\
**\[v1\]** Thu, 15 Mar 2012 11:25:52 UTC (297 KB)\

## Access Paper

### Current browse context
