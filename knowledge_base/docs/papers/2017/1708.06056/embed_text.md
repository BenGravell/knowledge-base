<!-- arxiv-full-text:v1 {"arxiv_id": "1708.06056", "source": "ar5iv"} -->

## Introduction

A path planning algorithm finds a collision free path for a robot to follow in order to perform a task, for example to move a robot arm. Robots that perform tasks in uncontrolled environments, e.g. autonomous driving or agricultural tasks, must plan new paths online for each task, as they identify goals and obstacles to avoid. These path planners must be both computationally efficient, so they can plan paths with a limited time budget, and must find short fast-to-execute paths. Ideally, the planner should find paths that are as close to the shortest/optimal path that is possible.

A popular family of algorithms for planning paths for robot arms are randomized sampling-based path planners, e.g. Probabilistic Road Maps (PRMs) and Rapidly-exploring Random Trees (RRTs). Many of algorithms find feasible paths quickly but are not guaranteed to find the shortest path, regardless of time available. Recent work on optimal planning, e.g. RRT\* and PRM\*, extend these algorithms to guarantee asymptotic optimality, however, these algorithms may require a long time to find a good path. This paper considers speeding-up existing optimal planning algorithms for practical applications where the computation time available for planning is limited.

This paper evaluates optimal path planners for the problem of using a six degree-of-freedom robot arm to reach and prune (cut) a grape vine, and the problem of reaching into cubicles. We propose improving convergence speed by integrating a local 'short-cutting' optimiser to improve intermediate solutions. For these applications we demonstrate that combining RRTConnect\* (a bidirectional variation of RRT\*) and short-cutting results in substantially faster convergence.

One run of RRTConnect followed by short-cutting optimizer Multiple restarts of RRTConnect + short-cut where the best path is kept. A leading contemporary approach. See Fig. 2.

Asymptotically optimal RRTConnect. We also use the informed heuristics.

Our proposed approach. RRTConnect* with informed heuristics that uses short-cutting local optimizer.

Table 1: Summary of planners evaluated

## Background

Robot arm path planners often operate in the robot's *configuration space* to find collision free paths. The configuration space, $C$, can be split into $C_{\text{free}}$ and $C_{\text{obs}}$. $C_{\text{free}}$ is the set of all configurations where the robot is not in collision with the environment or itself. $C_{\text{obs}}$ is the set of configurations where the robot is in collision with itself or the environment. Computing an explicit representation of configuration space is prohibitively expensive for many robot arms.

Sampling based motion planners have become popular because they do not require an explicit representation of the robot's configuration space. These planners use a collision detector to classify sampled configurations as either in $C_{\text{free}}$ or $C_{\text{obs}}$. These planners explore the robot's configuration space and grow a graph. Some planners, e.g. PRM, construct a highly connected graph that can be used for multiple planning queries. Other planners, e.g. RRT, quickly grow a directed acyclic graph that can only be used for one planning query.

Path planners can be categorised as feasible planners, or optimizing planners. Feasible planners attempt to quickly find a solution and terminate as soon as one is found. Feasible planners can return poor, e.g. long, solutions because they do not perform optimization. Optimizing planners attempt to find high-quality, e.g. short, solutions within a set computation time or number of iterations. Some of these optimizing planners are asymptotically optimal and will converge to the optimal solution eventually. Other optimizing planners are asymptotically near-optimal and will converge to a near-optimal solution eventually. In this paper we propose an approach for speeding up the convergence of optimizing planners.

A key requirement for many popular asymptotically optimal path planners, e.g. Batch Informed Trees (BIT\*), RRT\*, PRM\*, is that when a new vertex $v$ is inserted into the planner's graph $G$, edges are formed between $v$ and vertices within its neighbourhood $V_{\text{nbh}}$. $V_{\text{nbh}}$ can be defined as all vertices in $G$ within a radius $r_{\text{nbh}}$ of $v$, or as the $k_{\text{nbh}}$ neighbours of $v$. Minimum values for $r_{\text{nbh}}$ and $k_{\text{nbh}}$ depend on the number of vertices in $G$. Some multiple query planners, e.g. PRM\*, form edges between $v$ and all its neighbours where a collision-free path exists. Single query planners perform a *rewiring* step that joins $v$ to a sub-set of it's neighbours without adding cycles their graph.

Fig. 1 illustrates how RRT\* rewires a new vertex $v$ into its graph $G$ (Fig. 1a). The new vertex is initially connected to its nearest neighbour in $G$ (Fig. 1b). The neighbourhood of $v$ in $G$ is computed, $v$ is then connected to a different vertex to minimise the cost to arrive from the start vertex (Fig. 1c). The edges of neighbouring vertices are changed if the path through $v$ provides smaller cost to arrive at that particular neighbour (Fig. 1d). This rewiring approach is guaranteed not to introduce cycles into $G$.

Figure 1: RRT* insertion of the yellow vertex. The start vertex is shown in red and the goal vertex is shown in green. rn denotes the neighbourhood radius and vertices within this neighbourhood are shown with a white fill.

As optimising planners converge to the optimal solution they can spend more time processing samples that cannot possibly be used to improve on the best solution. This can be remedied by focussing the planner's search to useful regions of configuration space and rejecting new samples that cannot be used to improve on the planner's best solution without sacrificing the optimality properties of the planner. In this paper we test RRTConnect\* with these heuristics enabled.

Local optimization algorithms can be used with path planners to quickly improve path quality, e.g. length. These algorithms often rely on a path planner to provide an initial solution. This initial solution influences the quality of the optimised path because these algorithms only optimize locally. Short-cutting for reducing path length and sequential convex optimization approaches have been shown to work well on robot arms.

A common approach to finding short paths is to find an initial collision-free solution with a feasible planner, e.g. RRTConnect (a bidirectional RRT), and to optimise this path with a local optimiser e.g. short-cutting. Another approach is to perform multiple restarts of the feasible planner, optimise each solution and return the best solution as shown in Fig. 2. This has been shown to work well in empirical experiments when compared to asymptotically optimal planners. We compare our approach of RRTConnect\* integrated with short-cutting to multiple restarts of RRTConnect with short-cutting, as well as one run of RRTConnect with short-cutting.

1:function MRRTConnect+S(vstart, Vgoal, termination_condition) 5: p ← RRTConnect(vstart, Vgoal) 12: while not termination_condition Figure 2: Multiple restarts of RRTConnect with short-cutting.

There has been some recent interest in combining asymptotically optimal path planners with local optimisers to speed up convergence to optimal solutions. Choudhury et. al. use the CHOMP local optimiser to avoid collisions in edges between vertices in their Regionally Accelerated Batch Informed Trees (RABIT\*) planner. This differs from our work because our approach uses a local optimiser to improve a complete path.

A recent preprint proposed 'interleaving' the use of a global asymptotically optimal path planner with a local optimiser. The global planner is used to explore the robot's configuration space and the local optimiser is used to quickly improve solutions. The local optimiser is invoked every time the global planner finds a better solution. The optimised path is then placed into the planner's graph without forming edges to existing vertices within the graph i.e. no rewiring step is performed. This means that the interleaving approach is only asymptotically optimal for some planners, e.g. PRM\*, and special consideration must be given to only include vertices added by the global planner when calculating the neighbourhood size.

In this paper we build on the interleaving approach in two ways: Firstly, optimised paths are rewired back into the planner's graph to preserve the asymptotic optimality of the global planner. Secondly, we only invoke the local optimiser when the global planner has substantially improved on the last optimised path. This prevents the local optimiser being invoked every time the global planner has made a small incremental improvement to the last optimised path.

## Integrating RRTConnect\* with a short-cutting local optimiser

Our approach speeds up RRTConnect\* by integrating a short-cutting local optimiser. Good intermediate solutions found by RRTConnect\* are shortcut and inserted into RRTConnect\*'s graph as shown in Fig. 3. $v_{\text{start}}$ and $V_{\text{goal}}$ represent the start vertex and goal vertices for the planning query. Planning continues until the termination_condition expires, e.g. this could be an iteration count or a timeout.

1:function RRTConnect*+S(vstart, Vgoal, opt_threshold, termination_condition) 4: G ← RRTConnect*(vstart, Vgoal, G) // One iteration 5: best_path ← Best cost path from vstart to Vgoal through G 6: Cbest ← Cost of best_path 7: if $\frac{C_{\text{last_opt}} - C_{\text{best}}}{C_{\text{last_opt}}} >$ opt_threshold then 8: poptimized ← Shortcut(pshortest) 9: G ← InsertPath(G, poptimised, vstart) 10: Clast_optimized ← Cshortest 12: while not termination_condition 13: return Lowest cost path from vstart to Vgoal through G Figure 3: RRTConnect* with short-cutting. The blue lines show our proposed changes to RRTConnect*.

To maintain asymptotic optimality, vertices from the short-cut path are rewired into RRTConnect\*'s graph. To ensure that the short-cut path is recoverable through RRTConnect\*'s graph, the neighbourhood of each of the path's vertices is expanded to include the path's previous vertex as shown in Fig. 4. After path insertion the cost of the best path through the planner's graph $C_{\text{best}}'$ is: Where $C_{\text{path}}$ is the cost of the path that was inserted and $C_{\text{best}}$ is the cost of the best cost path before the new path was inserted. In our experiments we terminate the Shortcut routine after a fixed number of iterations.

(a) Planner’s existing graph G with one solution.

(b) Path to be inserted, p, into G.

(c) Neighbourhood of vertex 2 of p that has been extended to include previous vertex from path.

(d) The vertex is added to G and its neighbourhood is rewired.

(e) Neighbourhood of vertex 3 from p that has been extended to include previous vertex from path.

(f) The vertex is added and its neighbourhood is rewired.

(g) The final vertex of p is inserted into G, but no edges change.

(h) G after p has been added, the new minimum cost path shown in yellow.

Figure 4: Insertion of a path p into a planner’s graph G using RRT*’s insertion procedure for the objective of minimising Euclidean path length. The start vertex in G is red and the goal vertex is green. Vertices and the edges that are added/modified are shown in yellow, except for (h) where the final path is shown in yellow. Vertices part of a yellow vertex’s neighbourhood have a white fill. rn is the radius that defines the neighbourhood of the yellow vertex.

Our approach can be extended to other planners by changing the planner used in Fig. 3 (line 4). The InsertPath method may have to be altered for use with planners such as PRM\* that do not perform rewiring.

## Experiments

To test our approach, we compare the performances of the planners in Tab. 1 to RRTConnect\* integrated with a short-cutting local optimiser. We test these planners on two robots, one for pruning grape vines (Fig. 5) and one for reaching into cubicles (Fig. 6).

In both trials, RRTConnect\* with and without short-cutting was configured to minimise Euclidean path length. Planner parameters are in Appendix 8 along with how we arrived at these choices. We also tested with RRT\* (with and without local optimisation) but it was unable to find initial solutions, which is consistent with previous results when using a robot arm.

(b) The robot arm in a cutting position.

Figure 5: Vine pruning scenario.

(a) Robot arm with gripper model.

(b) Robot arm reaching into a cubicle.

Figure 6: Cubicle picking scenario.

On the vine pruning robot, the planners were tasked with moving the robot arm to cut positions on the vine. This task involves planning fine motions around thin obstacles. We used a collision detector that was specialised for use in this problem.

The cubicle picking environment was designed to be similar to that used in previous research and the 2015 Amazon Picking Challenge. The planner had to compute plans so that the robot arm would reach from its start position in one cubicle into another. Exiting the start cubicle and entering the goal cubicle both required fine motion plans. We used the Flexible Collision Library (FCL) for collision detection. An analytical IK solver for the UR5 was used to generate the robot arm configurations to reach the arm into the centre of each cubicle with a fixed end-effector orientation.

## Results

For both experiments we recorded the Euclidean length (sum of Euclidean lengths of each path segment, in radians), execution time (how long it would take the robot arm to follow the path), the number of local optimisations and the cycle time (computation time plus execution time). These measurements were taken from the planner in a separate thread as to not interfere with the planner's performance. Values for length, and execution time of the shortest found path taken before the first solution was found were later calculated using the first solution that the planner found. The total time is the planning time plus execution time, where planning is terminated after $t$ seconds, or once a solution is found if this takes longer.

Integrating RRTConnect\* with a short-cut local optimiser resulted in significant speed-ups as shown in Fig. 7 and Fig. 8. It resulted in a 24% reduction in cycle time for the vine pruning robot, and a 21% decrease in cycle time for the cubicle picking robot. MRRTConnect+S also performed well in both experiments. These speed-ups result in lower robot cycle times because the computation and execution times are of similar magnitude.

Figure 7: Means for 304 successful grape vine planning queries. Error bars show the 95% confidence interval. MRRTConnect+S averaged 905 local optimisations after 30 seconds of planning, it was truncated for clarity. For a fixed time budget RRTConnect*+S found paths that were faster to execute than RRTConnect*, allowing the robot to have a shorter cycle time.

Figure 8: Means for 144 cubicles queries. Error bars show the 95% confidence interval. MRRTConnect+S averaged 42.3 local optimisations after 30 seconds of planning, it was truncated for clarity. For a fixed time budget RRTConnect*+S found paths that were faster to execute than RRTConnect*, allowing the robot to have a shorter cycle time.

## Discussion

Integrating RRTConnect\* with a short-cut local optimiser resulted in shorter paths being found more quickly compared to not using the short-cut optimiser as shown in Fig. 7 and Fig. 8. This is consistent with the results of a recent preprint where BIT\* and PRM\* were interleaved with a Lagrangian local optimiser.

In the cubicles experiment the RRTConnect\*+S planner only performed around one local optimisation. This is because it tended to find short solutions after one local optimisation and could not improve these solutions enough to invoke the local optimiser again. RRTConnect+S also performed well on this experiment. This suggests that the configuration space for the cubicles experiment is very sparse and optimising a wide range of initial paths could result in a short path.

RRTConnect\*+S was sparing with its use of the local optimiser in both experiments as shown in Fig. 7 and Fig. 8. This is because the local optimiser is only invoked when RRTConnect\* has improved the path by a certain threshold (Fig. 3). MRRTConnect+S made a lot of calls to the local optimiser because it was called every time a new path was found. We might also expect the interleaving optimiser to make a lot of calls to the local optimiser because it is invoked every time the global planner (even slightly) improves the path. MRRTConnect+S and the interleaving approach may spend a lot of time in local optimisation if a slow local optimiser is used.

The short-cut optimiser was a good fit for both the experiments as shown by the good performance of MRRTConnect+S in both experiments. This could be caused by the robots having sparse configuration spaces in both experiments. The short-cut optimiser is not a good fit for all problems, especially those where the triangle inequality does not hold. In these spaces it is possible that short-cutting a path may lead to it becoming longer. Our path insertion method (see Sec. 3) guarantees that the insertion of a poor path does not degrade the quality of any other paths found by the planner.

## Conclusion

We presented an approach to integrating an asymptotically optimal path planner with a local optimiser. In our experiments we saw that integrating a short-cutting local optimiser significantly improved the performance of RRTConnect\* in two robot arm tasks. Our approach resulted in a significant performance improvement when compared with the state-of-the-art RRTConnect\* asymptotically optimal planner and computes paths that are 31% faster to execute when both are given 3 seconds of planning time.
