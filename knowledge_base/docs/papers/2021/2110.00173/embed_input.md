Batch Belief Trees for Motion Planning under Uncertainty

Topics include Motion planning, Uncertainty, Graphs, Planning, Sampling, BBT, Batch belief trees.

In this work, we develop the Batch Belief Trees (BBT) algorithm for motion planning under motion and sensing uncertainties. The algorithm interleaves between batch sampling, building a graph of nominal trajectories in the state space, and searching over the graph to find belief space motion plans. By searching over the graph, BBT finds sophisticated plans that will visit (and revisit) information-rich regions to reduce uncertainty. One of the key benefits of this algorithm is the modified interplay between exploration and exploitation. Instead of an exhaustive search (exploitation) after one exploration step, the proposed algorithm uses batch samples to explore the state space and, in addition, does not require exhaustive search before the next iteration of batch sampling, which adds flexibility.The algorithm finds motion plans that converge to the optimal one as more samples are added to the graph. We test BBT in different planning environments. Our numerical investigation confirms that BBT finds non-trivial motion plans and is faster compared with previous similar methods.

## Introduction

For safe and reliable autonomous robot operation in a real-world environment, consideration of various uncertainties becomes necessary. These uncertainties may arise from an inaccurate motion model, actuation or sensor noise, partial sensing, and the presence of other agents moving in the same environment. In this paper, we study the safe motion planning problem of robot systems with nontrivial dynamics, motion uncertainty, and state-dependent measurement uncertainty, in an environment with non-convex obstacles.

Planning under uncertainties is referred to as belief space planning (BSP), where the state of the robot is characterized by a probability distribution function (pdf) over all possible states. This pdf is commonly referred to as the belief or information state. A BSP problem can be formulated as a partially observable Markov decision process (POMDP) problem. Solving POMDPs for continuous state, control, and observation spaces, is, however, intractable. Existing methods based on discretization are resolution-limited....

In this paper, we propose the Batch Belief Tree (BBT) algorithm for motion planning under uncertainties. The algorithm considers a robot that is partially observable, has motion uncertainty, and operates in a continuous domain. By searching over the graph, the algorithm finds sophisticated plans that will visit (and revisit) information-rich regions to reduce uncertainty. With intermittent batch sampling and delayed graph exploitation, BBT has good performance in terms of exploring the state space. BBT finds all non-dominated belief nodes within the graph and is asymptotic optimal....

Extensions of the BBT algorithm include, for example, adding informed state-space sampling. Also, heuristics could be used for ordering the belief nodes in $Q_{current}$, which will expand the promising beliefs first, thus helping with the convergence of the algorithm.

We use the partial ordering of belief nodes as in. Let $n_{a}$ and $n_{b}$ be two belief nodes of the same vertex $v$. We use $n_{a} < n_{b}$ to denote that belief node $n_{b}$ is dominated by $n_{a}$. $n_{a} < n_{b}$ is true if

We will consider this linear time-varying system hereafter. A Kalman filter is used for estimating ${\check{x}}_{k}$ and is given by
