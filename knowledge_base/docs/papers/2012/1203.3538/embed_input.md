<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RAPID: A Reachable Anytime Planner for Imprecisely-Sensed Domains

Topics include Partially observable planning, Factored dynamics, POMDPs, Anytime planning, State envelopes, Tutoring systems, Reachability analysis.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents RAPID, an anytime planner for structured POMDPs that first builds a compact envelope of states reachable under the fully observable optimal policy, then expands that envelope as computation permits. The paper's key value is exploiting topological structure inside factored dynamics, allowing a tutoring-scale domain with enormous flat state space to get useful partially observable plans without enumerating the full model.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Despite the intractability of generic optimal partially observable Markov decision process planning, there exist important problems that have highly structured models. Previous researchers have used this insight to construct more efficient algorithms for factored domains, and for domains with topological structure in the flat state dynamics model. In our work, motivated by findings from the education community relevant to automated tutoring, we consider problems that exhibit a form of topological structure in the factored dynamics model. Our Reachable Anytime Planner for Imprecisely-sensed Domains (RAPID) leverages this structure to efficiently compute a good initial envelope of reachable states under the optimal MDP policy in time linear in the number of state variables. RAPID performs partially-observable planning over the limited envelope of states, and slowly expands the state space considered as time allows. RAPID performs well on a large tutoring-inspired problem simulation with 122 state variables, corresponding to a flat state space of over 10^30 states.
