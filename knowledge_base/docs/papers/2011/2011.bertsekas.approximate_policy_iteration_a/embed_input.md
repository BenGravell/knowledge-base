<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Approximate Policy Iteration: A Survey and Some New Methods

Topics include Approximate dynamic programming, Policy iteration, Reinforcement learning, Temporal difference, Aggregation, Projected equations, Policy oscillation, Survey paper.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Surveys approximate policy iteration with an emphasis on what can go wrong when policy evaluation is approximate. The paper is useful because it compares projected-equation/TD and aggregation viewpoints, explains chattering and policy-oscillation pathologies, and points to regularized and aggregation-based fixes.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the classical policy iteration method of dynamic programming (DP), where approximations and simulation are used to deal with the curse of dimensionality. We survey a number of issues: convergence and rate of convergence of approximate policy evaluation methods, singularity and susceptibility to simulation noise of policy evaluation, exploration issues, constrained and enhanced policy iteration, policy oscillation and chattering, and optimistic and distributed policy iteration. Our discussion of policy evaluation is couched in general terms and aims to unify the available methods in the light of recent research developments and to compare the two main policy evaluation approaches: projected equations and temporal differences (TD), and aggregation. In the context of these approaches, we survey two different types of simulation-based algorithms: matrix inversion methods, such as least-squares temporal difference (LSTD), and iterative methods, such as least-squares policy evaluation (LSPE) and TD (λ), and their scaled variants. We discuss a recent method, based on regression and regularization, which rectifies the unreliability of LSTD for nearly singular projected Bellman equations.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

An iterative version of this method belongs to the LSPE class of methods and provides the connecting link between LSTD and LSPE. Our discussion of policy improvement focuses on the role of policy oscillation and its effect on performance guarantees. We illustrate that policy evaluation when done by the projected equation/TD approach may lead to policy oscillation, but when done by aggregation it does not. This implies better error bounds and more regular performance for aggregation, at the expense of some loss of generality in cost function representation capability. Hard aggregation provides the connecting link between projected equation/TD-based and aggregation-based policy evaluation, and is characterized by favorable error bounds.
