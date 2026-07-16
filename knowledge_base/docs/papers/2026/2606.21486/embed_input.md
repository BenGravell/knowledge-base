<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Reference-Free, Long-Horizon Trajectory Optimization for Aggressive Autonomous Driving in Milliseconds

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous vehicles must generate long-horizon and dynamically feasible trajectories in real time-even when operating at the limits of vehicle handling-to ensure safe operation in adverse conditions. However, existing work rarely quantifies the computational demands of generating such trajectories without prior references, warm starts and often defaults to low-fidelity models, compromising accuracy and control authority. We investigate the modeling and solver design choices that enable real-time solution of long-horizon, reference-free optimal control problems (OCPs) using full vehicle dynamics. To this end, we analyze vehicle stiffness properties to justify the OCP's integration scheme and show that lower-order A-stable methods consistently outperform alternatives, with solve time differences reaching two orders of magnitude. We show that robust nonlinear solver performance hinges on understanding barrier parameter update strategies and safeguarding techniques for Hessian indefiniteness, inherent in some interior point methods. Lastly, we propose a computationally efficient method for generating initial guesses using dynamic equilibrium, unlocking real-time performance and reducing initial infeasibility by up to four orders of magnitude.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Extensive benchmarking and high-fidelity BeamNG simulation demonstrate compute times as low as 55 ms over a 260 m horizon, including high-speed obstacle avoidance scenarios where drifting emerges as a necessary component of feasible trajectory generation.
