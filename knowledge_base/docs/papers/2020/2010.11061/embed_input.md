MADER: Trajectory Planner in Multi-Agent and Dynamic Environments

This paper presents MADER, a 3D decentralized and asynchronous trajectory planner for UAVs that generates collision-free trajectories in environments with static obstacles, dynamic obstacles, and other planning agents. Real-time collision avoidance with other dynamic obstacles or agents is done by performing outer polyhedral representations of every interval of the trajectories and then including the plane that separates each pair of polyhedra as a decision variable in the optimization problem. MADER uses our recently developed MINVO basis to obtain outer polyhedral representations with volumes 2.36 and 254.9 times, respectively, smaller than the Bernstein or B-Spline bases used extensively in the planning literature. Our decentralized and asynchronous algorithm guarantees safety with respect to other agents by including their committed trajectories as constraints in the optimization and then executing a collision check-recheck scheme....

## Introduction and related work

(a) Circle configuration: 32 agents, 25 static obstacles and 25 dynamic obstacles.

(b) Sphere configuration: 32 agents, 18 static obstacles and 52 dynamic obstacles.

## Conclusions

This work presented MADER, a decentralized and asynchronous planner that handles static obstacles, dynamic obstacles and other agents. By using the MINVO basis, MADER obtains outer polyhedral representations of the trajectories that are 2.36 and 254.9 times smaller than the volumes achieved using the Bernstein and B-Spline bases. To ensure non-conservative, collision-free constraints with respect to other obstacles and agents, MADER includes as decision variables the planes that separate each pair of outer polyhedral representations....

For the final condition, we use a final stop condition imposing the constraints ${\mathbf{v}{(t_{\text{f}})}} = \mathbf{v}_{f} = \mathbf{0}$ and ${\mathbf{a}{(t_{\text{f}})}} = \mathbf{a}_{f} = \mathbf{0}$. These conditions require ${\mathbf{q}}_{n - 2} = {\mathbf{q}}_{n - 1} = {\mathbf{q}}_{n}$, so the control points ${\mathbf{q}}_{n - 1}$ and ${\mathbf{q}}_{n}$ can also be excluded from the set of decision variables. The final position is included as a penalty cost $\left\| {{\mathbf{q}}_{n - 2} - {\mathbf{g}}} \right\|_{2}^{2}$ in the objective function, weighted with a parameter $\omega \geq 0$....

## Assumptions

The Optimization period happens during $t \in {(t_{1},t_{2}\rbrack}$. The optimization problem will include the polyhedral outer representations of the trajectories ${{p_{i}{(t)}},i} \in I$ in the constraints. All the trajectories other agents commit to during the Optimization period are stored.

Figure 1: 32 agents using MADER to plan trajectories in a decentralized and asynchronous way in an environment with dynamic obstacles (light brown boxes and horizontal poles), static obstacles (dark brown pillars) and other agents.

While efficient and fast UAV trajectory planners for static worlds have been extensively proposed in the literature, a 3D real-time planner able to handle environments with static obstacles, dynamic obstacles *and* other planning agents still remains an open problem (see Fig. 1).

To be able to guarantee safety, the trajectory of the planning agent and the ones of other obstacles/agents need to be encoded in the optimization (see Fig. 2)....
