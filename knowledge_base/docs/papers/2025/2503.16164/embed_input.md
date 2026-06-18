Asymptotically Optimal Path Planning with an Approximation of the Omniscient Set

Topics include Path planning, Planning, Sampling.

The asymptotically optimal version of Rapidly-exploring Random Tree (RRT*) is often used to find optimal paths in a high-dimensional configuration space. The well-known issue of RRT* is its slow convergence towards the optimal solution. A possible solution is to draw random samples only from a subset of the configuration space that is known to contain configurations that can improve the cost of the path (omniscient set). A fast convergence rate may be achieved by approximating the omniscient with a low-volume set. In this letter, we propose new methods to approximate the omniscient set and methods for their effective sampling. First, we propose to approximate the omniscient set using several (small) hyperellipsoids defined by sections of the current best solution. The second approach approximates the omniscient set by a convex hull computed from the current solution. Both approaches ensure asymptotical optimality and work in a general n-dimensional configuration space. The experiments have shown superior performance of our approaches in multiple scenarios in 3D and 6D configuration spaces.

## Introduction

Figure 1: Examples of trees with 7, 000 nodes (red) with the current best solution (blue path). RRT* samples the whole space (a), and Informed-RRT* samples from one (blue) hyperellipsoid (b). Proposed PI-RRT* samples from multiple small hyperellipsoids (c) and proposed C-RRT* samples from a convex set around the current best solution (d).

The task of optimal path planning is to find a collision-free path with the lowest cost (e.g., path length) from a start configuration to a goal configuration. Low-dimensional configuration spaces can be discretized, and the optimal path can be searched using, e.g., A\*. Sampling-based motion planners, e.g., Rapidly-exploring Random Tree (RRT) \[\], search the configuration space using randomized sampling, and they are more suitable for searching high-dimensional spaces than the discretization methods. RRT\* \[\] is an asymptotically optimal variant of the RRT algorithm....

## Conclusion

The well-known issue of asymptotically optimal path planning using RRT\* is its slow convergence towards the optimal path. In this paper, we have proposed novel methods to approximate the omniscient set, i.e., the subset of the configuration space that is known to contain samples that can improve the quality of the path. The first proposed approach uses multiple hyperellipsoids that are defined by a subsection of the current best path. In the second approach, we construct a convex hull of the current best path. We describe how to sample these spaces. The proposed methods can be integrated into any RRT\*-based planner....

We modify the Graham scan using prior knowledge about the resulting hull of the set of points $V = {transf{({\mathcal{P} \cup {\{ o,t\}}})}}$. First, one edge of the convex hull is already known (it is the line segment $\overline{o,t}$). Second, all points are located only in one direction from this edge (all points of the slice have a positive $f{( \cdot )}$ value).

Figure 3: Visualization of one sj, k in blue on the path 𝒫.

To draw a random sample from $\mathcal{S}_{cl}$, first a random sample is generated in $\mathcal{S}_{l}$ (which is described in section V-A), and the sample is accepted only if it is also located in $\mathcal{S}_{c}$.

RRT\* samples the whole configuration space, which is not necessary, as there exist states that cannot possibly improve the existing solution....
