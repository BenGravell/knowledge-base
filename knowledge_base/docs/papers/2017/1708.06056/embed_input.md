<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Integrating Asymptotically-optimal Path Planning with Local Optimization

Topics include Path planning, Robotics, Online algorithms, Optimization, Planning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Many robots operating in unpredictable environments require an online path planning algorithm that can quickly compute high quality paths. Asymptotically optimal planners are capable of finding the optimal path, but can be slow to converge. Local optimisation algorithms are capable of quickly improving a solution, but are not guaranteed to converge to the optimal solution. In this paper we develop a new way to integrate an asymptotically optimal planners with a local optimiser. We test our approach using RRTConnect* with a short-cutting local optimiser. Our approach results in a significant performance improvement when compared with the state-of-the-art RRTConnect* asymptotically optimal planner and computes paths that are 31\% faster to execute when both are given 3 seconds of planning time.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A path planning algorithm finds a collision free path for a robot to follow in order to perform a task, for example to move a robot arm. Robots that perform tasks in uncontrolled environments, e.g. autonomous driving or agricultural tasks, must plan new paths online for each task, as they identify goals and obstacles to avoid. These path planners must be both computationally efficient, so they can plan paths with a limited time budget, and must find short fast-to-execute paths. Ideally, the planner should find paths that are as close to the shortest/optimal path that is possible.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A popular family of algorithms for planning paths for robot arms are randomized sampling-based path planners, e.g. Probabilistic Road Maps (PRMs) and Rapidly-exploring Random Trees (RRTs). Many of algorithms find feasible paths quickly but are not guaranteed to find the shortest path, regardless of time available. Recent work on optimal planning, e.g. RRT\* and PRM\*, extend these algorithms to guarantee asymptotic optimality, however, these algorithms may require a long time to find a good path. This paper considers speeding-up existing optimal planning algorithms for practical applications where the computation time available for planning is limited.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper evaluates optimal path planners for the problem of using a six degree-of-freedom robot arm to reach and prune (cut) a grape vine, and the problem of reaching into cubicles. We propose improving convergence speed by integrating a local 'short-cutting' optimiser to improve intermediate solutions. For these applications we demonstrate that combining RRTConnect\* (a bidirectional variation of RRT\*) and short-cutting results in substantially faster convergence.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

One run of RRTConnect followed by short-cutting optimizer Multiple restarts of RRTConnect + short-cut where the best path is kept. A leading contemporary approach. See Fig. 2.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Asymptotically optimal RRTConnect. We also use the informed heuristics.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our proposed approach. RRTConnect* with informed heuristics that uses short-cutting local optimizer.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Integrating RRTConnect\\* with a short-cutting local optimiser", "weight": 1.0} -->

Our approach speeds up RRTConnect\* by integrating a short-cutting local optimiser. Good intermediate solutions found by RRTConnect\* are shortcut and inserted into RRTConnect\*'s graph as shown in Fig. 3. $v_{\text{start}}$ and $V_{\text{goal}}$ represent the start vertex and goal vertices for the planning query. Planning continues until the termination_condition expires, e.g. this could be an iteration count or a timeout.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Integrating RRTConnect\\* with a short-cutting local optimiser", "weight": 1.0} -->

1:function RRTConnect*+S(vstart, Vgoal, opt_threshold, termination_condition) 4: G ← RRTConnect*(vstart, Vgoal, G) // One iteration 5: best_path ← Best cost path from vstart to Vgoal through G 6: Cbest ← Cost of best_path 7: if $\frac{C_{\text{last_opt}} - C_{\text{best}}}{C_{\text{last_opt}}} >$ opt_threshold then 8: poptimized ← Shortcut(pshortest) 9: G ← InsertPath(G, poptimised, vstart) 10: Clast_optimized ← Cshortest 12: while not termination_condition 13: return Lowest cost path from vstart to Vgoal through G Figure 3: RRTConnect* with short-cutting. The blue lines show our proposed changes to RRTConnect*.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Integrating RRTConnect\\* with a short-cutting local optimiser", "weight": 1.0} -->

To maintain asymptotic optimality, vertices from the short-cut path are rewired into RRTConnect\*'s graph. To ensure that the short-cut path is recoverable through RRTConnect\*'s graph, the neighbourhood of each of the path's vertices is expanded to include the path's previous vertex as shown in Fig. 4. After path insertion the cost of the best path through the planner's graph $C_{\text{best}}'$ is: Where $C_{\text{path}}$ is the cost of the path that was inserted and $C_{\text{best}}$ is the cost of the best cost path before the new path was inserted. In our experiments we terminate the Shortcut routine after a fixed number of iterations.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Integrating RRTConnect\\* with a short-cutting local optimiser", "weight": 1.0} -->

(a) Planner’s existing graph G with one solution.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Integrating RRTConnect\\* with a short-cutting local optimiser", "weight": 1.0} -->

(c) Neighbourhood of vertex 2 of p that has been extended to include previous vertex from path.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Integrating RRTConnect\\* with a short-cutting local optimiser", "weight": 1.0} -->

(d) The vertex is added to G and its neighbourhood is rewired.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Integrating RRTConnect\\* with a short-cutting local optimiser", "weight": 1.0} -->

(e) Neighbourhood of vertex 3 from p that has been extended to include previous vertex from path.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Integrating RRTConnect\\* with a short-cutting local optimiser", "weight": 1.0} -->

(f) The vertex is added and its neighbourhood is rewired.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Integrating RRTConnect\\* with a short-cutting local optimiser", "weight": 1.0} -->

(g) The final vertex of p is inserted into G, but no edges change.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Integrating RRTConnect\\* with a short-cutting local optimiser", "weight": 1.0} -->

(h) G after p has been added, the new minimum cost path shown in yellow.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Integrating RRTConnect\\* with a short-cutting local optimiser", "weight": 1.0} -->

Our approach can be extended to other planners by changing the planner used in Fig. 3 (line 4). The InsertPath method may have to be altered for use with planners such as PRM\* that do not perform rewiring.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Experiments", "weight": 1.0} -->

To test our approach, we compare the performances of the planners in Tab. 1 to RRTConnect\* integrated with a short-cutting local optimiser. We test these planners on two robots, one for pruning grape vines (Fig. 5) and one for reaching into cubicles (Fig. 6).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experiments", "weight": 1.0} -->

In both trials, RRTConnect\* with and without short-cutting was configured to minimise Euclidean path length. Planner parameters are in Appendix 8 along with how we arrived at these choices. We also tested with RRT\* (with and without local optimisation) but it was unable to find initial solutions, which is consistent with previous results when using a robot arm.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experiments", "weight": 1.0} -->

(b) The robot arm in a cutting position.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experiments", "weight": 1.0} -->

(a) Robot arm with gripper model.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experiments", "weight": 1.0} -->

(b) Robot arm reaching into a cubicle.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experiments", "weight": 1.0} -->

On the vine pruning robot, the planners were tasked with moving the robot arm to cut positions on the vine. This task involves planning fine motions around thin obstacles. We used a collision detector that was specialised for use in this problem.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

The cubicle picking environment was designed to be similar to that used in previous research and the 2015 Amazon Picking Challenge. The planner had to compute plans so that the robot arm would reach from its start position in one cubicle into another. Exiting the start cubicle and entering the goal cubicle both required fine motion plans. We used the Flexible Collision Library (FCL) for collision detection. An analytical IK solver for the UR5 was used to generate the robot arm configurations to reach the arm into the centre of each cubicle with a fixed end-effector orientation.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Results", "weight": 1.0} -->

For both experiments we recorded the Euclidean length (sum of Euclidean lengths of each path segment, in radians), execution time (how long it would take the robot arm to follow the path), the number of local optimisations and the cycle time (computation time plus execution time). These measurements were taken from the planner in a separate thread as to not interfere with the planner's performance. Values for length, and execution time of the shortest found path taken before the first solution was found were later calculated using the first solution that the planner found. The total time is the planning time plus execution time, where planning is terminated after $t$ seconds, or once a solution is found if this takes longer.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Results", "weight": 1.0} -->

Integrating RRTConnect\* with a short-cut local optimiser resulted in significant speed-ups as shown in Fig. 7 and Fig. 8. It resulted in a 24% reduction in cycle time for the vine pruning robot, and a 21% decrease in cycle time for the cubicle picking robot. MRRTConnect+S also performed well in both experiments. These speed-ups result in lower robot cycle times because the computation and execution times are of similar magnitude.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Discussion", "weight": 1.5} -->

Integrating RRTConnect\* with a short-cut local optimiser resulted in shorter paths being found more quickly compared to not using the short-cut optimiser as shown in Fig. 7 and Fig. 8. This is consistent with the results of a recent preprint where BIT\* and PRM\* were interleaved with a Lagrangian local optimiser.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Discussion", "weight": 1.5} -->

In the cubicles experiment the RRTConnect\*+S planner only performed around one local optimisation. This is because it tended to find short solutions after one local optimisation and could not improve these solutions enough to invoke the local optimiser again. RRTConnect+S also performed well on this experiment. This suggests that the configuration space for the cubicles experiment is very sparse and optimising a wide range of initial paths could result in a short path.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Discussion", "weight": 1.5} -->

RRTConnect\*+S was sparing with its use of the local optimiser in both experiments as shown in Fig. 7 and Fig. 8. This is because the local optimiser is only invoked when RRTConnect\* has improved the path by a certain threshold (Fig. 3). MRRTConnect+S made a lot of calls to the local optimiser because it was called every time a new path was found. We might also expect the interleaving optimiser to make a lot of calls to the local optimiser because it is invoked every time the global planner (even slightly) improves the path. MRRTConnect+S and the interleaving approach may spend a lot of time in local optimisation if a slow local optimiser is used.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Discussion", "weight": 1.5} -->

The short-cut optimiser was a good fit for both the experiments as shown by the good performance of MRRTConnect+S in both experiments. This could be caused by the robots having sparse configuration spaces in both experiments. The short-cut optimiser is not a good fit for all problems, especially those where the triangle inequality does not hold. In these spaces it is possible that short-cutting a path may lead to it becoming longer. Our path insertion method (see Sec. 3) guarantees that the insertion of a poor path does not degrade the quality of any other paths found by the planner.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented an approach to integrating an asymptotically optimal path planner with a local optimiser. In our experiments we saw that integrating a short-cutting local optimiser significantly improved the performance of RRTConnect\* in two robot arm tasks. Our approach resulted in a significant performance improvement when compared with the state-of-the-art RRTConnect\* asymptotically optimal planner and computes paths that are 31% faster to execute when both are given 3 seconds of planning time.
