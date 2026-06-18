Integrating Asymptotically-optimal Path Planning with Local Optimization

Topics include Path planning, Robotics, Online algorithms, Optimization, Planning.

Many robots operating in unpredictable environments require an online path planning algorithm that can quickly compute high quality paths. Asymptotically optimal planners are capable of finding the optimal path, but can be slow to converge. Local optimisation algorithms are capable of quickly improving a solution, but are not guaranteed to converge to the optimal solution. In this paper we develop a new way to integrate an asymptotically optimal planners with a local optimiser. We test our approach using RRTConnect* with a short-cutting local optimiser. Our approach results in a significant performance improvement when compared with the state-of-the-art RRTConnect* asymptotically optimal planner and computes paths that are 31\% faster to execute when both are given 3 seconds of planning time.

## Introduction

A path planning algorithm finds a collision free path for a robot to follow in order to perform a task, for example to move a robot arm. Robots that perform tasks in uncontrolled environments, e.g. autonomous driving or agricultural tasks, must plan new paths online for each task, as they identify goals and obstacles to avoid. These path planners must be both computationally efficient, so they can plan paths with a limited time budget, and must find short fast-to-execute paths. Ideally, the planner should find paths that are as close to the shortest/optimal path that is possible.

A popular family of algorithms for planning paths for robot arms are randomized sampling-based path planners, e.g. Probabilistic Road Maps (PRMs) and Rapidly-exploring Random Trees (RRTs). Many of algorithms find feasible paths quickly but are not guaranteed to find the shortest path, regardless of time available. Recent work on optimal planning, e.g. RRT\* and PRM\*, extend these algorithms to guarantee asymptotic optimality, however, these algorithms may require a long time to find a good path.

This paper evaluates optimal path planners for the problem of using a six degree-of-freedom robot arm to reach and prune (cut) a grape vine, and the problem of reaching into cubicles. We propose improving convergence speed by integrating a local 'short-cutting' optimiser to improve intermediate solutions. For these applications we demonstrate that combining RRTConnect\* (a bidirectional variation of RRT\*) and short-cutting results in substantially faster convergence.

## Discussion

Integrating RRTConnect\* with a short-cut local optimiser resulted in shorter paths being found more quickly compared to not using the short-cut optimiser as shown in Fig. 7 and Fig. 8. This is consistent with the results of a recent preprint where BIT\* and PRM\* were interleaved with a Lagrangian local optimiser.

In the cubicles experiment the RRTConnect\*+S planner only performed around one local optimisation. This is because it tended to find short solutions after one local optimisation and could not improve these solutions enough to invoke the local optimiser again. RRTConnect+S also performed well on this experiment. This suggests that the configuration space for the cubicles experiment is very sparse and optimising a wide range of initial paths could result in a short path.
