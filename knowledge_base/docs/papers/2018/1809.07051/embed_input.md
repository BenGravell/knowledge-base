Probabilistic Completeness of RRT for Geometric and Kinodynamic Planning with Forward Propagation

Topics include Probabilistic models, Sampling-based methods, Planning, Control, Sampling, Rapidly-exploring random tree, PC, Random tree, Motion planning.

The Rapidly-exploring Random Tree (RRT) algorithm has been one of the most prevalent and popular motion-planning techniques for two decades now. Surprisingly, in spite of its centrality, there has been an active debate under which conditions RRT is probabilistically complete. We provide two new proofs of probabilistic completeness (PC) of RRT with a reduced set of assumptions. The first one for the purely geometric setting, where we only require that the solution path has a certain clearance from the obstacles. For the kinodynamic case with forward propagation of random controls and duration, we only consider in addition mild Lipschitz-continuity conditions. These proofs fill a gap in the study of RRT itself. They also lay sound foundations for a variety of more recent and alternative sampling-based methods, whose PC property relies on that of RRT. Our original publication contains an error in the analysis of the case of the kinodynamic RRT. Here, we rectify the problem by modifying the proof of Theorem 2, which, in particular, necessitated a revision of Lemma 3. Briefly, the original (and erroneous) proof of Theorem 2 used a sequence of equal-size balls.

## Introduction

Two decades ago LaValle and Kuffner presented the *Rapidly-exploring Random Tree* (RRT) method for sampling-based motion planning. Even though numerous alternatives for motion planning have been proposed since then, RRT remains one of the most widely used techniques today. This is due to its simplicity and practical efficiency, especially when combined with simple heuristics.

RRT is especially useful in single-query settings, as it focuses on finding a single trajectory moving a robot from an initial state to a goal state (or region), rather than exploring the full state space of the problem, as roadmap methods do, such as PRM. To achieve this objective, RRT grows a tree, rooted at an initial state, which is periodically extended towards random state samples until the goal is reached.

Since its introduction, numerous variations and extensions of RRT have been proposed (see, e.g., ), to allow improved performance. While RRT is not asymptotically optimal (AO) and provably does not converge to the optimal solution, it forms the basis of many AO planners, including RRT^∗^ and RRG. In particular, the probabilistic completeness (PC) of most of the aforementioned RRT-based algorithms is derived from the PC properties of RRT.

Surprisingly, it is not completely obvious under what conditions RRT is probabilistically complete, especially when using forward propagation of controls for the kinodynamic case. Indeed there has been some debate on this issue in the literature. This paper aims to address this gap.

## Discussion

Although our proofs assume uniform samples, they can be easily extended to samples generated using a Poisson point process, which is preferable in certain settings. An immediate extension of this work is to verify whether our proofs hold when other sampling distributions are considered, e.g., Halton sequences (see ).

Another possible direction is to further relax some of the assumptions made for kinodynamic systems, such as Lipschitz continuity. Additionally, the work raises the following challenging research question: Is it possible to extend these proofs that have a reduced set of assumptions to other sampling-based planners, or informed variants of RRT.
