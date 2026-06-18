<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Cross-Entropy Motion Planning

Topics include Motion planning, Cross-entropy method, Sampling-based planning, Sampling-based control, Stochastic optimal control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Applies the cross-entropy method (CEM) to motion planning, framing trajectory search as a distribution estimation problem where elite samples iteratively refine a sampling distribution toward low-cost trajectories.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper is concerned with motion planning for non-linear robotic systems operating in constrained environments. A method for computing high-quality trajectories is proposed building upon recent developments in sampling-based motion planning and stochastic optimization. The idea is to equip sampling-based methods with a probabilistic model that serves as a sampling distribution and to incrementally update the model during planning using data collected by the algorithm. At the core of the approach lies the cross-entropy method for the estimation of rare-event probabilities. The cross-entropy method is combined with recent optimal motion planning methods such as the rapidly exploring random trees (RRT*) in order to handle complex environments. The main goal is to provide a framework for consistent adaptive sampling that correlates the spatial structure of trajectories and their computed costs in order to improve the performance of existing planning methods.
