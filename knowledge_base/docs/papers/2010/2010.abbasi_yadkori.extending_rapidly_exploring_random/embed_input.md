<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Extending Rapidly-exploring Random Trees for Asymptotically Optimal Anytime Motion Planning

Topics include Motion planning, Anytime planning, Rapidly-exploring trees, Asymptotic optimality, Kinodynamic planning, Nonlinear dynamics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes RRT++, an anytime extension of RRT intended to quickly find feasible trajectories and then improve toward optimality with more computation. The paper sits in the transition from feasibility-focused sampling planners toward asymptotically optimal motion planning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the problem of anytime planning in continuous state and action spaces with non-linear deterministic dynamics. We review the existing approaches to this problem and find no algorithms that both quickly find feasible solutions and also eventually approach optimal solutions with additional time. The state-of-the-art solution to this problem is the rapidly-exploring random tree (RRT) algorithm that quickly finds a feasible solution. However, the RRT algorithm does not return better results with additional time. We introduce RRT ++, an anytime extension of the basic RRT algorithm. We show that the new algorithm has desirable theoretical properties and experimentally show that it efficiently finds near optimal solutions.
