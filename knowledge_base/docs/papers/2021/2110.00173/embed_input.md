Batch Belief Trees for Motion Planning under Uncertainty

Topics include Motion planning, Uncertainty, Graphs, Planning, Sampling, BBT, Batch belief trees.

In this work, we develop the Batch Belief Trees (BBT) algorithm for motion planning under motion and sensing uncertainties. The algorithm interleaves between batch sampling, building a graph of nominal trajectories in the state space, and searching over the graph to find belief space motion plans. By searching over the graph, BBT finds sophisticated plans that will visit (and revisit) information-rich regions to reduce uncertainty. One of the key benefits of this algorithm is the modified interplay between exploration and exploitation. Instead of an exhaustive search (exploitation) after one exploration step, the proposed algorithm uses batch samples to explore the state space and, in addition, does not require exhaustive search before the next iteration of batch sampling, which adds flexibility.The algorithm finds motion plans that converge to the optimal one as more samples are added to the graph. We test BBT in different planning environments. Our numerical investigation confirms that BBT finds non-trivial motion plans and is faster compared with previous similar methods.

## Introduction

For safe and reliable autonomous robot operation in a real-world environment, consideration of various uncertainties becomes necessary. These uncertainties may arise from an inaccurate motion model, actuation or sensor noise, partial sensing, and the presence of other agents moving in the same environment. In this paper, we study the safe motion planning problem of robot systems with nontrivial dynamics, motion uncertainty, and state-dependent measurement uncertainty, in an environment with non-convex obstacles.

In this paper, we focus on sampling-based approaches similar to. One challenge of sampling-based algorithms for planning under uncertainty is the lack of the optimal substructure property, which has been discussed . The lack of optimal substructure property is further explained by the lack of total ordering on paths based on cost. Specifically, it is not enough to only minimize the usual cost function -- explicitly finding paths that reduce the uncertainty of the robot is also important (see Figure 1(a)).

## Conclusion

In this paper, we propose the Batch Belief Tree (BBT) algorithm for motion planning under uncertainties. The algorithm considers a robot that is partially observable, has motion uncertainty, and operates in a continuous domain. By searching over the graph, the algorithm finds sophisticated plans that will visit (and revisit) information-rich regions to reduce uncertainty. With intermittent batch sampling and delayed graph exploitation, BBT has good performance in terms of exploring the state space. BBT finds all non-dominated belief nodes within the graph and is asymptotic optimal.

Extensions of the BBT algorithm include, for example, adding informed state-space sampling. Also, heuristics could be used for ordering the belief nodes in $Q_{current}$, which will expand the promising beliefs first, thus helping with the convergence of the algorithm.
