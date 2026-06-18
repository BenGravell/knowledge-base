Integrating Asymptotically-optimal Path Planning with Local Optimization

Topics include Path planning, Robotics, Online algorithms, Optimization, Planning.

Many robots operating in unpredictable environments require an online path planning algorithm that can quickly compute high quality paths. Asymptotically optimal planners are capable of finding the optimal path, but can be slow to converge. Local optimisation algorithms are capable of quickly improving a solution, but are not guaranteed to converge to the optimal solution. In this paper we develop a new way to integrate an asymptotically optimal planners with a local optimiser. We test our approach using RRTConnect* with a short-cutting local optimiser. Our approach results in a significant performance improvement when compared with the state-of-the-art RRTConnect* asymptotically optimal planner and computes paths that are 31\% faster to execute when both are given 3 seconds of planning time.

## Introduction

A path planning algorithm finds a collision free path for a robot to follow in order to perform a task, for example to move a robot arm. Robots that perform tasks in uncontrolled environments, e.g. autonomous driving or agricultural tasks, must plan new paths online for each task, as they identify goals and obstacles to avoid. These path planners must be both computationally efficient, so they can plan paths with a limited time budget, and must find short fast-to-execute paths. Ideally, the planner should find paths that are as close to the shortest/optimal path that is possible.

A popular family of algorithms for planning paths for robot arms are randomized sampling-based path planners, e.g. Probabilistic Road Maps (PRMs) and Rapidly-exploring Random Trees (RRTs). Many of algorithms find feasible paths quickly but are not guaranteed to find the shortest path, regardless of time available. Recent work on optimal planning, e.g. RRT\* and PRM\*, extend these algorithms to guarantee asymptotic optimality, however, these algorithms may require a long time to find a good path....

## Conclusion

We presented an approach to integrating an asymptotically optimal path planner with a local optimiser. In our experiments we saw that integrating a short-cutting local optimiser significantly improved the performance of RRTConnect\* in two robot arm tasks. Our approach resulted in a significant performance improvement when compared with the state-of-the-art RRTConnect\* asymptotically optimal planner and computes paths that are 31% faster to execute when both are given 3 seconds of planning time.

(c) Neighbourhood of vertex 2 of p that has been extended to include previous vertex from path.

1:function MRRTConnect+S(vstart, Vgoal, termination_condition)
5: p ← RRTConnect(vstart, Vgoal)
12: while not termination_condition
Figure 2: Multiple restarts of RRTConnect with short-cutting.

To test our approach, we compare the performances of the planners in Tab. 1 to RRTConnect\* integrated with a short-cutting local optimiser. We test these planners on two robots, one for pruning grape vines (Fig. 5) and one for reaching into cubicles (Fig. 6).

This paper evaluates optimal path planners for the problem of using a six degree-of-freedom robot arm to reach and prune (cut) a grape vine, and the problem of reaching into cubicles....
