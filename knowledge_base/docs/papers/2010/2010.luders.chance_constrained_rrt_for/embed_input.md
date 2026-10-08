<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Chance Constrained RRT for Probabilistic Robustness to Environmental Uncertainty

Topics include Motion planning, Chance constraints, Sampling-based planning, Uncertainty, Linear systems.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Combines chance constraints with sampling-based planning to construct probabilistically feasible trajectories for uncertain linear systems. Handles process noise and uncertain dynamic obstacles using Gaussian state propagation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

For motion planning problems involving many or unbounded forms of uncertainty, it may not be possible to identify a path guaranteed to be feasible, requiring consideration of the trade-off between planner conservatism and the risk of infeasibility. This paper presents a novel real-time planning algorithm, chance constrained rapidly-exploring random trees (CC-RRT), which uses chance constraints to guarantee probabilistic feasibility for linear systems subject to process noise and/or uncertain, possibly dynamic obstacles. By using RRT, the algorithm enjoys the computational benefits of sampling-based algorithms, such as trajectory-wise constraint checking and incorporation of heuristics, while explicitly incorporating uncertainty within the formulation. Under the assumption of Gaussian noise, probabilistic feasibility at each time step can be established through simple simulation of the state conditional mean and the evaluation of linear constraints. Alternatively, a small amount of additional computation can be used to explicitly compute a less conservative probability bound at each time step. Simulation results show that this algorithm can be used for efficient identification and execution of probabilistically safe paths in real time.
