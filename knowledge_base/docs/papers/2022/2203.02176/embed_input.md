ST-RRT*: Asymptotically-Optimal Bidirectional Motion Planning through Space-Time

Topics include Motion planning, Path planning, Robotics, Probabilistic models, Planning, OMPL.

We present a motion planner for planning through space-time with dynamic obstacles, velocity constraints, and unknown arrival time. Our algorithm, Space-Time RRT* (ST-RRT*), is a probabilistically complete, bidirectional motion planning algorithm, which is asymptotically optimal with respect to the shortest arrival time. We experimentally evaluate ST-RRT* in both abstract (2D disk, 8D disk in cluttered spaces, and on a narrow passage problem), and simulated robotic path planning problems (sequential planning of 8DoF mobile robots, and 7DoF robotic arms). The proposed planner outperforms RRT-Connect and RRT* on both initial solution time, and attained final solution cost. The code for ST-RRT* is available in the Open Motion Planning Library (OMPL).

## Introduction

Motion planning is a fundamental challenge in robotics. In many real-world applications, obstacles change positions over time and goals are only valid at specific times. For applications such as multi-robot assembly, multiple motion scheduling subproblems need to be solved. Assuming that obstacle trajectories are given a priori, the subproblems can be modelled as *navigation through dynamic environments*. Mathematically, this is formulated as planning through a space-time state space.

To address those challenges, we develop Space-Time RRT\* (ST-RRT\*). The basic operating principle of ST-RRT\* is illustrated in Fig. 1: (a) We compute an initial estimate of a feasible goal time (blue dashed line), and grow both a forward tree from the start state (blue), and a set of reverse trees from the goal regions (red). If no solution is found given a certain number of samples, the upper time limit in which we generate samples is increased (b). If a solution (orange) is found (c), the parts of the trees that can not lead to an improved solution are pruned.

Conditional Sampling: We develop a novel sampling method that prevents the sampling of states which cannot be part of a solution path due to velocity constraints.

## Conclusion

We proposed ST-RRT\*, a planning algorithm that is able to efficiently deal with unbounded time spaces and optimizes for arrival time in an environment with moving obstacles on known trajectories. We guarantee probabilistic completeness and asymptotic optimality by introducing progressive expansion of the goal space and generate new samples accordingly. Our algorithm efficiently deals with many goals and converges to the optimal path quickly by making use of conditional sampling and shrinking the goal spaces.

The current implementation of ST-RRT\* still has two limitations: the batch size and the expansion factor must be chosen in the beginning with a crude estimate of when the goal can be reached. In practice this is not a large limitation since real settings usually impose some upper limit on the acceptable maximum time to reach a goal state. Additionally, acceleration and more complex kinodynamic constraints (e.g. torque limits) are not taken into account. While this does not pose a problem in our applications, it would not be applicable to robots which have to be in quasi-static equilibrium.
