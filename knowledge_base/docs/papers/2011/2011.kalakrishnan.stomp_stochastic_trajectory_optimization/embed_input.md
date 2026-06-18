<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

STOMP: Stochastic Trajectory Optimization for Motion Planning

Topics include Motion planning, Path planning, Path optimization, Stochastic optimization, Path integral, Sampling, STOMP.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

STOMP improves a trajectory by rolling out a large batch of noisy samples and computing a weighted average (based on a Boltzmann distribution i.e. exponentiated negative with a temperature parameter) over their costs. Effectively a path-space analogue of MPPI. Does not require cost gradients. Noise helps STOMP jiggle out of local minima that CHOMP can get stuck , a similar mechanism and phenomenon as in general stochastic/perturbed gradient descent.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a new approach to motion planning using a stochastic trajectory optimization framework. The approach relies on generating noisy trajectories to explore the space around an initial (possibly infeasible) trajectory, which are then combined to produced an updated trajectory with lower cost. A cost function based on a combination of obstacle and smoothness cost is optimized in each iteration. No gradient information is required for the particular optimization algorithm that we use and so general costs for which derivatives may not be available (e.g. costs corresponding to constraints and motor torques) can be included in the cost function. We demonstrate the approach both in simulation and on a mobile manipulation system for unconstrained and constrained tasks. We experimentally show that the stochastic nature of STOMP allows it to overcome local minima that gradient-based methods like CHOMP can get stuck .
