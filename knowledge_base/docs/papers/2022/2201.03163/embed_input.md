Continuous-Curvature Target Tree Algorithm for Path Planning in Complex Parking Environments

Topics include Path planning, Parking, Clothoid, Curvature continuity, Rapidly-exploring random tree, Target tree, Autonomous vehicles.

Extends the target tree algorithm - “Model-based decision making with imagination for autonomous parking” by Feng, Chen, Chen, and Zheng - for autonomous parking by replacing circular/straight path segments with clothoid curves to achieve continuous curvature (G2). Introduces an obstacle-aware cost function for target tree construction to reduce planning time in complex environments. Combined with RRT* and shortest-path selection, yields near-optimal continuous-curvature parking solutions.

Rapidly-exploring random tree (RRT) has been applied for autonomous parking due to quickly solving high-dimensional motion planning and easily reflecting constraints. However, planning time increases by the low probability of extending toward narrow parking spots without collisions. To reduce the planning time, the target tree algorithm was proposed, substituting a parking goal in RRT with a set (target tree) of backward parking paths. However, it consists of circular and straight paths, and an autonomous vehicle cannot park accurately because of curvature-discontinuity. Moreover, the planning time increases in complex environments; backward paths can be blocked by obstacles. Therefore, this paper introduces the continuous-curvature target tree algorithm for complex parking environments. First, a target tree includes clothoid paths to address such curvature-discontinuity. Second, to reduce the planning time further, a cost function is defined to construct a target tree that considers obstacles....

## Introduction

Path planning is a key component in autonomous parking tasks. Path planning methods for parking need to satisfy the following conditions. First, a collision-free path should be planned considering various obstacles around the parking spot. Second, the parking path should be obtained within a short planning time, even in complex parking situations. Third, the path needs to be a continuous-curvature path for the autonomous vehicle to track and park accurately. In other words, the method needs to consider the vehicle's kinematic constraints, such as minimum turning radius and maximum steering velocity.

Various path planning methods take the abovementioned conditions into account, such as geometric, optimization-based, grid search-based, and sampling-based methods. A geometric method plans the parking path in a short planning time by a combination of simple geometric curves that considers the vehicle's constraints. However, this approach may fail to find the path in complex parking environments where the road is narrow due to obstacles near the parking spot. Optimization-based methods have been applied in various parking situations; they formulate the path planning problem as an optimization problem....

## Conclusion

This paper introduces the continuous-curvature target tree algorithm for complex parking, which addresses the limitations of the original target tree algorithm. The proposed algorithm uses a continuous-curvature target tree that additionally considers the vehicle's steering velocity. The algorithm then searches the target tree, thereby possibly reducing the planning time further in complex parking environments. Integrated with RRT\* and minimum-length path selection, the proposed algorithm finds a shorter parking path within a given sampling time....

The minimum-length path selection step replaces lines 10 and 11 in Algorithm 1. First, several candidate goals of the target tree reached by the RRT\* tree, $T$, are stored within the sampling time. This is because, even after the first parking path is obtained, RRT\* paths that reach other candidate goals may be found during the additional time for a tree-rewiring step. Lines 10 and 11 in Algorithm 1 are replaced by,

The continuous-curvature target tree is divided into perpendicular and parallel parking cases (see Fig. 2)....
