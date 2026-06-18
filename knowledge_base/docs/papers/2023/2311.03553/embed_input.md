iDb-A*: Iterative Search and Optimization for Optimal Kinodynamic Motion Planning

Topics include Trajectory optimization, Motion planning, Robotics, Benchmarks, Sampling-based methods, Optimization, Planning, Control, Sampling.

Motion planning for robotic systems with complex dynamics is a challenging problem. While recent sampling-based algorithms achieve asymptotic optimality by propagating random control inputs, their empirical convergence rate is often poor, especially in high-dimensional systems such as multirotors. An alternative approach is to first plan with a simplified geometric model and then use trajectory optimization to follow the reference path while accounting for the true dynamics. However, this approach may fail to produce a valid trajectory if the initial guess is not close to a dynamically feasible trajectory. In this paper, we present Iterative Discontinuity Bounded A* (iDb-A*), a novel kinodynamic motion planner that combines search and optimization iteratively. The search step utilizes a finite set of short trajectories (motion primitives) that are interconnected while allowing for a bounded discontinuity between them. The optimization step locally repairs the discontinuities with trajectory optimization. By progressively reducing the allowed discontinuity and incorporating more motion primitives, our algorithm achieves asymptotic optimality with excellent any-time performance.

## Introduction

Kinodynamic motion planning for robots remains a challenging task, particularly when the objective is to compute time-optimal plans. Fig. 1 showcases four interesting problems: obstacle-free recovery motions from unstable configurations with low-power quadcopters (Fig. 1(d)), swing-up motions with acrobatic pole-copters among obstacles (Fig. 1(c)), maneuvering an Ackermann steering car with a trailer through a tight corridor (Fig. 1(b)), and a unicycle with asymmetric angular speed bounds and a positive minimum velocity (Fig. 1(a)).

Current planning approaches are sampling-based, search-based, optimization-based, or hybrid. Each of these methods has its strengths and weaknesses. Sampling-based planners can find initial solutions quickly and have strong guarantees for asymptotic convergence to an optimal solution in theory. In practice, the initial solutions are far from optimal; the convergence rate is low, and the solutions typically require post-processing.

Our algorithm is implemented in C++ and is publicly available. Our second contribution is an open-source benchmark that compares the three major kinodynamic motion planning techniques on the same problem instances. While we focus in our evaluation on time optimality, our approach supports other cost functions that are additive and non-negative (e.g., energy or squared acceleration).

## Conclusion

We present iDb-A\*, a new kinodynamic motion planner that combines a novel graph-search method with trajectory optimization iteratively. For the graph search, we introduce Db-A\*, a generalization of A\* that reuses motion primitives to compute trajectories with bounded discontinuity, which are later used as a warm start for trajectory optimization.

iDb-A\* amalgamates the ideas and advantages of sampling-based, search-based, and optimization-based kinodynamic motion planners: it converges asymptotically to the optimal solution, rapidly finds a near-optimal solution, and does not require any additional post-processing.

We evaluate iDb-A\* on a diverse set of challenging, time-optimal kinodynamic motion planning problems, from obstacle avoidance with car-like robots to highly dynamic maneuvers with quadcopters. iDb-A\* consistently outperforms other algorithms on these benchmarks and solves problems that were beyond the capabilities of previous motion planners.
