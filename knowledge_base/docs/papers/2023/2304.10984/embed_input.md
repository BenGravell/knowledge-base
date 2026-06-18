IBBT: Informed Batch Belief Trees for Motion Planning under Uncertainty

Topics include Motion planning under uncertainty, Belief-space planning, Batch planning, Sampling-based planning, POMDPs, State estimation, Risk-aware planning.

Introduces Informed Batch Belief Trees for planning in belief space, using batch expansion and informed sampling to search efficiently under state uncertainty. The contribution sits between sampling-based motion planning and POMDP-style planning, with emphasis on reducing wasted exploration in high-dimensional belief spaces.

In this work, we propose the Informed Batch Belief Trees (IBBT) algorithm for motion planning under motion and sensing uncertainties. The original stochastic motion planning problem is divided into a deterministic motion planning problem and a graph search problem. We solve the deterministic planning problem using sampling-based methods such as PRM or RRG to construct a graph of nominal trajectories. Then, an informed cost-to-go heuristic for the original problem is computed based on the nominal trajectory graph. Finally, we grow a belief tree by searching over the graph using the proposed heuristic. IBBT interleaves between batch state sampling, nominal trajectory graph construction, heuristic computing, and search over the graph to find belief space motion plans. IBBT is an anytime, incremental algorithm. With an increasing number of batches of samples added to the graph, the algorithm finds motion plans that converge to the optimal one. IBBT is efficient by reusing results between sequential iterations. The belief tree searching is an ordered search guided by an informed heuristic. We test IBBT in different planning environments....

## Introduction

For safe and reliable autonomous robot operation in a real-world environment, consideration of various uncertainties becomes necessary. These uncertainties may arise from an inaccurate motion model, actuation or sensor noise, partial sensing, and the presence of other agents moving in the same environment. In this paper, we study the safe motion planning problem for robot systems with nontrivial dynamics, motion uncertainty, and state-dependent measurement uncertainty in an environment with non-convex obstacles.

Planning under uncertainty is referred to as belief space planning (BSP), where the state of the robot is characterized by a probability distribution function (pdf) over all possible states. This pdf is commonly referred to as the belief or information state. A BSP problem can be formulated as a partially observable Markov decision process (POMDP) problem. Solving POMDPs for continuous state, control, and observation spaces, is, however, intractable. Existing methods based on discretization are resolution-limited....

## Conclusion

We developed an online, anytime, incremental algorithm, IBBT, for motion planning under uncertainties. The algorithm considers a robot that is partially observable, has motion uncertainty, and operates in a continuous domain. The algorithm interleaves between batch sampling, building a graph of nominal trajectories in the state space, and searches over the graph to grow a belief tree. The heuristic cost-to-go is computed using the nominal trajectory graph along with value iteration. This cost-to-go along with the cost-to-come provides an informed heuristic to guide the belief tree search....

The Informed Batch Belief Tree algorithm repeatedly performs two main operations: It first builds a graph of nominal trajectories to explore the state space of the robot, and then it searches over this graph to grow a belief tree in the belief space. The IBBT algorithm is given by Algorithm 2 and Algorithm 3.

## Informed Batch Belief Tree Algorithm

## Experimental Results

Planning in infinite-dimensional distributional (e.g., belief) spaces can become more tractable by using sampling-based methods. For example, belief roadmap methods build a belief roadmap to reduce estimation uncertainty; the rapidly-exploring random belief trees (RRBT) algorithm has been proposed to grow a tree in the belief space....
