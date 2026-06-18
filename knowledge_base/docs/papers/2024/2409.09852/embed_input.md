A Complete Algorithm for a Moving Target Traveling Salesman Problem with Obstacles

Topics include Traveling salesman problem, Moving targets, Obstacles, Complete algorithms, Motion planning, Combinatorial optimization.

Presents a complete algorithm for a moving-target traveling-salesman variant with obstacle avoidance and target time windows. The paper connects geometric motion planning with combinatorial routing by proving finite-time termination and handling the coupling between visit order, timing, and collision-free travel.

The moving target traveling salesman problem with obstacles (MT-TSP-O) is a generalization of the traveling salesman problem (TSP) where, as its name suggests, the targets are moving. A solution to the MT-TSP-O is a trajectory that visits each moving target during a certain time window(s), and this trajectory avoids stationary obstacles. We assume each target moves at a constant velocity during each of its time windows. The agent has a speed limit, and this speed limit is no smaller than any target's speed. This paper presents the first complete algorithm for finding feasible solutions to the MT-TSP-O. Our algorithm builds a tree where the nodes are agent trajectories intercepting a unique sequence of targets within a unique sequence of time windows. We generate each of a parent node's children by extending the parent's trajectory to intercept one additional target, each child corresponding to a different choice of target and time window. This extension consists of planning a trajectory from the parent trajectory's final point in space-time to a moving target....

## Introduction

Given a set of targets and the travel costs between every pair of targets, the traveling salesman problem (TSP) seeks an order of targets for an agent to visit that minimizes the agent's total travel cost. In the moving target traveling salesman problem (MT-TSP) \[\], the targets are moving through free space, and we seek not only an order of targets, but a trajectory for the agent intercepting each target. The agent's trajectory is subject to a speed limit and must intercept each target within a set of target-specific time intervals, called time windows....

Figure 1: Targets move along trajectories with piecewise-constant velocities, which can be intercepted by agent during time windows depicted in bold colored lines. Agent’s trajectory shown in dark blue avoids obstacles, intercepts each target within its time window, and returns to start location (depot).

## Conclusion

In this paper, we presented MTVG-TSP, a complete algorithm for the moving target traveling salesman problem with obstacles, leveraging a novel graph called a moving target visibility graph (MTVG). We showed that for a range of time window lengths, our algorithm takes less median and maximum time to find feasible solutions than prior methods. Future directions for this work are to incorporate kinodynamic constraints on the agent and involve multiple agents.

## Theoretical Analysis

### Remark 1

## Experiments

Two properties we desire for an MT-TSP-O algorithm are completeness^11^1Completeness refers to an algorithm's guarantee on finding a feasible solution when a problem instance is feasible or reporting infeasible in finite time otherwise. and optimality. No algorithm for the MT-TSP-O in the literature has either of these properties. Guaranteeing completeness is complicated by the fact that even the problem of finding a feasible solution is NP-complete, since the MT-TSP-O generalizes the TSP with time windows (TSP-TW) \[\]. In this paper, we present the first complete algorithm for the MT-TSP-O.

Simpler cases of the MT-TSP-O have been addressed in the literature, with completeness guarantees in some cases. For example, in the absence of obstacles, \[\] provides a complete and optimal solver for the MT-TSP assuming targets move at constant velocities. \[\] provides a complete and optimal method when targets have piecewise-constant velocities....
