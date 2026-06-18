MADER: Trajectory Planner in Multi-Agent and Dynamic Environments

This paper presents MADER, a 3D decentralized and asynchronous trajectory planner for UAVs that generates collision-free trajectories in environments with static obstacles, dynamic obstacles, and other planning agents. Real-time collision avoidance with other dynamic obstacles or agents is done by performing outer polyhedral representations of every interval of the trajectories and then including the plane that separates each pair of polyhedra as a decision variable in the optimization problem. MADER uses our recently developed MINVO basis to obtain outer polyhedral representations with volumes 2.36 and 254.9 times, respectively, smaller than the Bernstein or B-Spline bases used extensively in the planning literature. Our decentralized and asynchronous algorithm guarantees safety with respect to other agents by including their committed trajectories as constraints in the optimization and then executing a collision check-recheck scheme.

## Introduction and related work

(a) Circle configuration: 32 agents, 25 static obstacles and 25 dynamic obstacles.

(b) Sphere configuration: 32 agents, 18 static obstacles and 52 dynamic obstacles.

While efficient and fast UAV trajectory planners for static worlds have been extensively proposed in the literature, a 3D real-time planner able to handle environments with static obstacles, dynamic obstacles *and* other planning agents still remains an open problem (see Fig. 1).

To be able to guarantee safety, the trajectory of the planning agent and the ones of other obstacles/agents need to be encoded in the optimization (see Fig. 2). A common representation of this trajectory in the optimization is via points discretized along the trajectory. However, this does not usually guarantee safety between two consecutive discretization points and alleviating that problem by using a fine discretization of the trajectory can lead to a very high computational burden.

The contributions of this paper are therefore summarized as follows (see also Fig.

Decentralized and asynchronous planning framework that solves the deconfliction between the agents by imposing as constraints the trajectories other agents have committed to, and then doing a collision check-recheck scheme to guarantee safety with respect to trajectories other agents have committed to during the optimization time.

Extensive simulations and comparisons with state-of-the-art baselines in cluttered environments. The results show up to a 33.9% reduction in the flight time, a 88.8% reduction in the number of stops (compared to Bernstein/B-Spline bases), shorter flight distances than centralized approaches, and shorter total times on average than synchronous decentralized approaches.
