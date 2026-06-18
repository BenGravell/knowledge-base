Sampling-based Optimal Kinodynamic Planning with Motion Primitives

Topics include Kinodynamic planning, Trajectory planning, Asymptotic optimality, Sampling-based, Rapidly-exploring random tree star, Motion primitives, Precomputed, Lookup table, Grid.

Integrates a grid of states and offline precomputed connecting motion primitives into RRT*. Moves the computational burden of trajectory generation to an offline phase, trading runtime efficiency for memory usage and some optimality degradation tied to grid resolution.

This paper proposes a novel sampling-based motion planner, which integrates in Rapidly exploring Random Tree star (RRT*) a database of pre-computed motion primitives to alleviate its computational load and allow for motion planning in a dynamic or partially known environment. The database is built by considering a set of initial and final state pairs in some grid space, and determining for each pair an optimal trajectory that is compatible with the system dynamics and constraints, while minimizing a cost. Nodes are progressively added to the tree of feasible trajectories in the RRT* algorithm by extracting at random a sample in the gridded state space and selecting the best obstacle-free motion primitive in the database that joins it to an existing node. The tree is rewired if some nodes can be reached from the new sampled state through an obstacle-free motion primitive with lower cost. The computationally more intensive part of motion planning is thus moved to the preliminary offline phase of the database construction at the price of some performance degradation due to gridding. Grid resolution can be tuned so as to compromise between (sub)optimality and size of the database....

## Introduction

Motion planning is one of the fundamental problems in robotics, and consists of guiding the robot from an initial state to a final one along a collision-free path.

For many robots, focusing only on kinematics could result in collision-free paths that are impossible to be executed by the actual system. In particular, for systems that are differentially constrained, such a decoupled approach makes it difficult to turn a collision-free path into a feasible trajectory. In order to tackle this problem, Donald et al proposed the idea of *kinodynamic planning*, which combines the search for a collision-free path with the underlying dynamics of the system, so that the resulting trajectory would be feasible.

## CONCLUSIONS

In this paper, a variant of RRT^⋆^, named ${{\mathtt{R}\mathtt{R}\mathtt{T}}^{\star}\ {\mathtt{M}\mathtt{o}\mathtt{t}\mathtt{i}\mathtt{o}\mathtt{n}}} -$ $\mathtt{P}\mathtt{r}\mathtt{i}\mathtt{m}\mathtt{i}\mathtt{t}\mathtt{i}\mathtt{v}\mathtt{e}\mathtt{s}$, that allows to introduce motion primitives in the RRT^⋆^ planning framework is presented. In particular, a set of pre-computed trajectories, named motion primitives, is used to substitute the computationally challenging step of solving for a steering action....

As the number of iterations goes to infinity the cost of the trajectory returned by ${\mathtt{R}\mathtt{R}\mathtt{T}}^{\star}\ {\mathtt{M}\mathtt{o}\mathtt{t}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{P}\mathtt{r}\mathtt{i}\mathtt{m}\mathtt{i}\mathtt{t}\mathtt{i}\mathtt{v}\mathtt{e}\mathtt{s}}$ converges to the resolution optimal $\Delta$-cost with a probability equal to 1, i.e.,

(c) inverse transformation and edge design

Given a trajectory ${\sigma{(t)}}:{{\lbrack 0,T\rbrack}\rightarrow Q_{free}}$ which has $\epsilon$ obstacle clearance, if for any pair of time instants $t_{1},t_{2}$, such that $0 \leq t_{1} < t_{2} \leq T$, there exists a set of states inside a ball of radius $\alpha\epsilon$, with $0 < \alpha \leq 1$, centered at $\sigma{(t_{2})}$ that are reachable from $\sigma{(t_{1})}$ according to dynamics without leaving the $\epsilon$-free space around $\sigma{(t)}$, then $\sigma$ has $\epsilon$-dynamic clearance.

For most robotic applications, the solution to the planning problem should not only be feasible and collision-free, but also satisfy some properties such as, e.g., reaching the goal in minimum...
