<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust Sampling-Based Motion Planning with Asymptotic Optimality Guarantees

Topics include Motion planning, Chance constraints, Sampling-based planning, Uncertainty, Linear systems.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Combines chance constraints with sampling-based planning to construct probabilistically feasible trajectories for uncertain linear systems. Extends RRT* with asymptotic optimality and a risk-aware objective.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a novel sampling-based planner, CC-RRT*, which generates robust, asymptotically optimal trajectories in real-time for linear Gaussian systems subject to process noise, localization error, and uncertain environmental constraints. CC-RRT* provides guaranteed probabilistic feasibility, both at each time step and along the entire trajectory, by using chance constraints to efficiently approximate the risk of constraint violation. This algorithm expands on existing results by utilizing the framework of RRT* to provide guarantees on asymptotic optimality of the lowest-cost probabilistically feasible path found. A novel risk-based objective function, shown to be admissible within RRT*, allows the user to trade-off between minimizing path duration and risk-averse behavior. This enables the modeling of soft risk constraints simultaneously with hard probabilistic feasibility bounds. Simulation results demonstrate that CC-RRT* can efficiently identify smooth, robust trajectories for a variety of uncertainty scenarios and dynamics.
