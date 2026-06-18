Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints

Topics include Motion planning, Robotics, Sampling-based methods, Nearest neighbors, Planning, Sampling, Nearest neighbor search, K-d tree.

Nearest-neighbor search dominates the asymptotic complexity of sampling-based motion planning algorithms and is often addressed with k-d tree data structures. While it is generally believed that the expected complexity of nearest-neighbor queries is O(log(N)) in the size of the tree, this paper reveals that when a classic k-d tree approach is used with sub-Riemannian metrics, the expected query complexity is in fact Theta(N^(p) log(N)) for a number p in [0, 1) determined by the degree of nonholonomy of the system. These metrics arise naturally in nonholonomic mechanical systems, including classic wheeled robot models. To address this negative result, we propose novel k-d tree build and query strategies tailored to sub-Riemannian metrics and demonstrate significant improvements in the running time of nearest-neighbor search queries.

## Introduction

Sampling-Based algorithms such as Probabilistic Roadmaps (PRM), Rapidly exploring Random Trees (RRT) and their asymptotically optimal variants (PRM^∗^, RRT^∗^) are widely used in motion planning. These algorithms build a random graph of motions between points on the robot's configuration manifold.

During the graph expansion, nearest-neighbor search is used to limit the computation to regions of the graph close to the new configurations and it is shown to dominate the asymptotic complexity of randomized planners. The notion of closeness appropriate for motion planning is induced by the length of the shortest paths between configurations, or in general, by the minimum cost of controlling a system between states.

In Section 2, we review background material on sub-Riemannian geometries and show connections with nonholonomic systems, providing asymptotic bounds to their reachable sets. Based on these bounds, in Section 3 we propose a query procedure specialized for nonholonomic systems, after a brief review of the $k$-d tree algorithm. In Section 4, we study the expected complexity of $m$-nearest-neighbor queries on a classic $k$-d tree with sub-Riemannian metrics. Inspired by this analysis, in Section 5 we propose a novel incremental build procedure.

## Conclusion

Motivated by applications in sampling-based motion planning, we investigated $k$-d trees for efficient nearest-neighbor search with distances defined by the length of paths of controllable nonholonomic systems. We have shown that for sub-Riemannian metrics, the query complexity of a classic batch-built $k$-d tree is $\Theta{({N^{p}{\log N}})}$, where $p \in {\lbrack 0,1)}$ depends on the properties of the system. In addition, we have proposed improved build and query algorithms for $k$-d trees that account for differential constraints.

Future work will analyze whether logarithmic complexity is achieved for nonholonomic systems. In addition, the proposed algorithms are exact and rely on explicit distance evaluations. Since distances cannot be generally computed in closed form, we are interested in investigating approximate nearest-neighbor search algorithms with provable correctness bounds that do not require explicit distance computations.
