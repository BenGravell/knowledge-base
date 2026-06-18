<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Refined Analysis of Asymptotically-Optimal Kinodynamic Planning in the State-Cost Space

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a novel analysis of AO-RRT: a tree-based planner for motion planning with kinodynamic constraints, originally described by Hauser and Zhou. AO-RRT explores the state-cost space and has been shown to efficiently obtain high-quality solutions in practice without relying on the availability of a computationally-intensive two-point boundary-value solver. Our main contribution is an optimality proof for the single-tree version of the algorithm - a variant that was not analyzed before. Our proof only requires a mild and easily-verifiable set of assumptions on the problem and system: Lipschitz-continuity of the cost function and the dynamics. In particular, we prove that for any system satisfying these assumptions, any trajectory having a piecewise-constant control function and positive clearance from the obstacles can be approximated arbitrarily well by a trajectory found by AO-RRT. We also discuss practical aspects of AO-RRT and present experimental comparisons of variants of the algorithm.
