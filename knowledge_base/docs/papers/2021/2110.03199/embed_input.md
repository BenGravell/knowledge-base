<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Optimal Control Approach to Particle Filtering

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a novel particle filtering framework for continuous-time dynamical systems with continuous-time measurements. Our approach is based on the duality between estimation and optimal control, which allows reformulating the estimation problem over a fixed time window into an optimal control problem. The resulting optimal control problem has a cost function that depends on the measurements and the closed-loop dynamics under optimal control coincides with the posterior distribution over the trajectories for the corresponding estimation problem. This type of stochastic optimal control problem can be solved using a remarkable technique known as path integral control. By recursively solving these optimal control problems using path integral control as new measurements become available we obtain an optimal control-based particle filtering algorithm. A distinguishing feature of the proposed method is that it uses the measurements over a finite-length time window instead of a single measurement for the estimation at each time step, resembling the batch methods of filtering, and improving fault tolerance. The efficacy of our algorithm is illustrated with several numerical examples.
