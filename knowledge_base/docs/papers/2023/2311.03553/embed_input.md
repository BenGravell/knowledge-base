iDb-A*: Iterative Search and Optimization for Optimal Kinodynamic Motion Planning

Topics include Trajectory optimization, Motion planning, Robotics, Benchmarks, Sampling-based methods, Optimization, Planning, Control, Sampling.

Motion planning for robotic systems with complex dynamics is a challenging problem. While recent sampling-based algorithms achieve asymptotic optimality by propagating random control inputs, their empirical convergence rate is often poor, especially in high-dimensional systems such as multirotors. An alternative approach is to first plan with a simplified geometric model and then use trajectory optimization to follow the reference path while accounting for the true dynamics. However, this approach may fail to produce a valid trajectory if the initial guess is not close to a dynamically feasible trajectory. In this paper, we present Iterative Discontinuity Bounded A* (iDb-A*), a novel kinodynamic motion planner that combines search and optimization iteratively. The search step utilizes a finite set of short trajectories (motion primitives) that are interconnected while allowing for a bounded discontinuity between them. The optimization step locally repairs the discontinuities with trajectory optimization. By progressively reducing the allowed discontinuity and incorporating more motion primitives, our algorithm achieves asymptotic optimality with excellent any-time performance....

## Introduction

Figure 1: Examples of kinodynamic motion planning problems. Start and goal configurations are shown in green and red, respectively, while gray boxes represent obstacles. We display some trajectories found by our algorithm, iDb-A*, in blue. (a) A unicycle with asymmetric angular speed bounds and a positive minimum velocity. (b) A car pulling a trailer. (c) Acrobatics with a planar multirotor with an underactuated pendulum. (d) A recovery flight with a quadrotor with a very limited thrust-to-weight ratio.

Kinodynamic motion planning for robots remains a challenging task, particularly when the objective is to compute time-optimal plans. Fig. 1 showcases four interesting problems: obstacle-free recovery motions from unstable configurations with low-power quadcopters (Fig. 1(d)), swing-up motions with acrobatic pole-copters among obstacles (Fig. 1(c)), maneuvering an Ackermann steering car with a trailer through a tight corridor (Fig. 1(b)), and a unicycle with asymmetric angular speed bounds and a positive minimum velocity (Fig. 1(a))....

The main limitation is that the number of motion primitives required grows exponentially with the state dimension, which poses a challenge to systems with higher dimensionality.

Finally, we believe that our combination of search, sampling, and optimization lays the foundation for novel kinodynamic planners for robotic manipulation and contact planning.

### Assumption 1

## Trajectory Optimization

We evaluate iDb-A\* on 43 problems that include 8 different dynamical systems in various environments. Most of the problems and systems are selected from previous work in kinodynamic motion planning. Additionally, we include several problems that require dynamic and agile maneuvers with multirotors.

Current planning approaches are sampling-based, search-based, optimization-based, or hybrid. Each of these methods has its strengths and weaknesses. Sampling-based planners can find initial solutions quickly and have strong guarantees for asymptotic convergence to an optimal solution in theory. In practice, the initial solutions are far from optimal; the convergence rate is low, and the solutions typically require post-processing.

Search-based approaches can remedy some of those shortcomings by connecting precomputed trajectories, so-called *motion primitives*, using A\* or related graph search algorithms....
