<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

AIT* and EIT*: Asymmetric Bidirectional Sampling-based Path Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Optimal path planning is the problem of finding a valid sequence of states between a start and goal that optimizes an objective. Informed path planning algorithms order their search with problem-specific knowledge expressed as heuristics and can be orders of magnitude more efficient than uninformed algorithms. Heuristics are most effective when they are both accurate and computationally inexpensive to evaluate, but these are often conflicting characteristics. This makes the selection of appropriate heuristics difficult for many problems. This paper presents two almost-surely asymptotically optimal sampling-based path planning algorithms to address this challenge, Adaptively Informed Trees (AIT*) and Effort Informed Trees (EIT*). These algorithms use an asymmetric bidirectional search in which both searches continuously inform each other. This allows AIT* and EIT* to improve planning performance by simultaneously calculating and exploiting increasingly accurate, problem-specific heuristics. The benefits of AIT* and EIT* relative to other sampling-based algorithms are demonstrated on twelve problems in abstract, robotic, and biomedical domains optimizing path length and obstacle clearance.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The experiments show that AIT* and EIT* outperform other algorithms on problems optimizing obstacle clearance, where a priori cost heuristics are often ineffective, and still perform well on problems minimizing path length, where such heuristics are often effective.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Path planning algorithms aim to find a sequence of valid states, called a path, that connects a start to a goal. Sampling-based planners, such as PRM PRMPRM, find paths by randomly sampling valid states and connecting nearby states when these local connections are valid. The resulting structure can be viewed as a graph embedded in a state space, where each vertex represents a valid state and each edge a sequence of valid states connecting two vertices. Multiple planning problems can be solved by adding starts and goals to this embedded graph and then finding a path between them with a A single planning problem is often solved more efficiently with incremental sampling-based planners, such as RRT RRTRRT and its asymptotically optimal variant, RRT*[karaman\_rss2010,karaman\_ijrr2011]. These planners build a search tree of valid paths rooted at the start by incrementally sampling and connecting states when these local connections are valid. This avoids having to specify the sampling resolution a priori, but results in a randomly ordered search that spends computational effort on paths that are never part of a solution.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Best-first graph-search algorithms, such as Dijkstra's [dijkstra\_nm1959], can search problems more efficiently by ordering their search on partial solution cost. Informed graph-search algorithms, such as A*[hart\_tssc1968], can further increase search efficiency by leveraging problem-specific information to order their search on total potential solution cost. This information is often expressed as a heuristic function that estimates the cost to connect any two vertices in a graph. A heuristic is called admissible if it never overestimates the true cost and consistent if it satisfies a specific triangle inequality. Given an admissible cost heuristic, A* finds an optimal solution, and given a consistent cost heuristic, A* does so optimally efficiently with respect to the number of expanded vertices[hart\_tssc1968].

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The efficient search order of A* is combined with the incremental sampling of RRT* in informed sampling-based planners, such as BIT* BIT*BIT*. This improves planning performance, but only when effective cost heuristics are available. A heuristic is most effective when it is both accurate and computationally inexpensive to evaluate relative to other search operations. Such heuristics may not exist for some problems, because they are inaccurate for a given obstacle configuration or computationally expensive due to complex optimization objectives, or may not be admissible, which is often required for theoretical performance guarantees of informed planners.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Problem-specific information not expressible as admissible cost heuristics can be exploited by more advanced informed graph-search algorithms, such as AEES AEESAEES and AC@A-MHA*@used A-MHA* A-MHA*A-MHA*. These algorithms decouple search order from solution quality guarantees, which allows them to balance search efficiency with anytime performance. This is especially important for robotic systems that operate under hard time constraints.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper presents techniques to inexpensively calculate accurate, admissible, and problem-specific heuristics and exploit them with sampling-based planning algorithms. This is achieved with an asymmetric bidirectional search that considers different information in the forward and reverse searches. These two searches continuously inform each other by sharing complementary information in both directions. Algorithm [alg:conceptual]provides a conceptual overview The reverse search calculates heuristics for the current sampling-based approximation of a planning problem. It exploits problem-specific information implicit in the observed distribution of valid states by combining a prioriheuristics between multiple states into more accurate heuristics between each state and the goal. The reverse search is computationally inexpensive because it only combines edge heuristics and avoids full collision detection and true edge cost evaluation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The forward search finds valid paths in the current sampling-based approximation of a planning problem. It does this effectively by exploiting the accurate, problem-specific heuristics calculated by the reverse search. The forward search informs the reverse search when invalid edges were used to calculate the heuristic, causing the reverse search to update the heuristic. The forward search is computationally expensive because it performs full collision detection and edge cost evaluation, but focused on connections likely to yield a solution by the calculated heuristics (Figure This paper presents two almost-surely asymptotically optimal sampling-based planning algorithms informed by an asymmetric bidirectional search, and EIT*. AIT* calculates an increasingly accurate, admissible cost heuristic with its reverse search and exploits this heuristic with its forward search. This results in fast initial solution times even when the admissible cost heuristic available a priori is not accurate. The full details of AIT* are presented in [Section]sec:adaptively-informed-trees.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

EIT* builds on AIT* by calculating an additional cost and effort heuristic with its reverse search and exploiting all three heuristics with its forward search. This results in fast initial solution times even when no admissible cost heuristic is available. The full details of EIT* are presented in [Section]sec:effort-informed-trees.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The benefits of simultaneously calculating and exploiting adaptive heuristics are demonstrated on twelve problems in abstract, robotic, and biomedical [Section]sec:experimental-results. All domains are tested with the path-length objective, where informative admissible heuristics are available a priori, and the obstacle-clearance objective, where informative admissible heuristics are not always available a priori. The results show that EIT* outperforms all other asymptotically optimal planners on all problems in all domains when optimizing obstacle clearance. AIT* and EIT*also perform well when minimizing path length in comparison to the tested planners when considering success rates, median initial solution times, and median solution quality over time.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Statement of Contributions", "weight": 1.0} -->

This paper expands on ideas first published as [strub\_icra2020b].

<!-- chunk {"id": "body-0013", "role": "body", "section": "Statement of Contributions", "weight": 1.0} -->

- Presents EIT* as an extension of AIT* to optimization objectives that are computationally expensive or difficult to approximate with an admissible a priori cost heuristic[Section]sec:effort-informed-trees. - Proves the almost-sure asymptotic optimality of these algorithms by building on results from the path-planning and graph-search literature[Section]sec:analysis. - Demonstrates the effectiveness of these algorithms accross multiple domains and optimization objectives, including problems of robotic manipulation and problems with continuous goal regions[Section]sec:experimental-results.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

There are two widely studied versions of the path planning problem. The feasible path planning problem is the task of finding a sequence of valid states, i.e., a path, that leads from a start to a goal. Many feasible problems have many solutions. The optimal path planning problem is the task of finding the best among these solutions, i.e., a valid path that is optimal with respect to a given optimization objective. Many optimal problems have a unique solution. The optimal path planning problem is formally defined in Definition[def:optimal-planning].

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

Let the state space of a planning problem be denoted by \(X \), the subset of invalid states by \(X\_{\mathrm{invalid}} \subset X \), and the subset of \(X\_{\mathrm{valid}} \coloneqq \mathop{\mathrm{closure}} \left(X \setminus X\_{\mathrm{invalid}} \right) \). Let the start state and the set of goal \(\bm{\mathrm{x}}\_{\mathrm{start}} \in X\_{\mathrm{valid}} \) and \(X\_{\mathrm{goal}} \subset X\_{\mathrm{valid}} \), respectively. Let \(\sigma \colon \to X\_{\mathrm{valid}} \) be a continuous function with bounded total variation, i.e., a valid path, and let the set of all valid paths be denoted by \(\Sigma \).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

Let the optimization objective be defined by a cost function, \(c \colon \Sigma \to [0, \infty) \), that maps each path to a nonnegative real number.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

The optimal path planning problem is the task of finding a path, \(\sigma^{*} \in \Sigma \), from the start to the goal with minimum cost, $$\sigma^{*} \coloneqq \mathop{\arg\min}_{\sigma \in \Sigma} \set*{ c(\sigma) \nonscript\:\delimsize\vert\nonscript\:\mathopen{} \sigma = \bm{\mathrm{x}}_{\mathrm{start}}, \sigma \in X_{\mathrm{goal}}},$$ or reporting failure if no such path exists.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

Sampling-based planners are often evaluated probabilistically as a function of the number of samples over all possible realizations of a distribution. Algorithms whose probability of solving the feasible path planning problem approaches one as the number of samples approaches infinity probabilistically complete. Algorithms that asymptotically solve the optimal planning problem as the number of samples approaches infinity with a probability of one are called almost-surely asymptotically optimal[karaman\_ijrr2011]. Almost-sure asymptotic optimality implies probabilistic completeness and is formally defined in Definition[def:asymptotic-optimality].

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

A sampling-based path planning algorithm is called almost-surely asymptotically optimal if it has a unity probability of asymptotically solving the optimal path planning problem as the number of samples approaches infinity (if an optimal solution exists), $$P\left(\adjustlimits{\mathop{\lim\,\sup}}_{{q \to \infty}}{\;\min}_{\;\sigma \in \Sigma_{q}} \{ c(\sigma) \} = c^{*} \right) = 1,$$ where \(q \) is the number of samples, \(\Sigma\_{q} \subset \Sigma \) is the set of valid paths from the start to the goal found by the planner from those samples, \(c \colon \Sigma \to [0, \infty) \) is the cost function, and \(c^{*} \) is the optimal solution cost.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

Sampling-based planners can also use deterministic sampling [branicky\_icra2001, lavalle\_ijrr2004], which can result in deterministic optimality guarantees[janson\_ijrr2018]. The finite-time properties of asymptotically optimal planners are analyzed by [dobson\_iros2013], [janson\_ijrr2018], and [tsao\_icra2020].

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

Formally analyzing sampling-based planners requires assumptions about the path planning problem [gammell\_arcras2021]. The analysis of AIT* and EIT* builds on the probabilistic results of [karaman\_ijrr2011] and makes the same assumptions (Sections[sec:state-space-assumptions][sec:solution-assumptions]).

<!-- chunk {"id": "body-0022", "role": "body", "section": "State Space Assumption", "weight": 1.0} -->

The state space of the planning problem is assumed to be an open, \)-dimensional unit (hyper)cube, \(X \coloneqq ^{n} \), but problems with other state spaces can also be searched[kleinbort\_wafr2016, kleinbort\_afr2020].

<!-- chunk {"id": "body-0023", "role": "body", "section": "Cost Function Assumptions", "weight": 1.0} -->

The cost of any path, \(\sigma = (\sigma\_{1} | \sigma\_{2}) \in \Sigma \), is assumed to be lower bounded by the cost of any of its segments, $$\forall\; \sigma_{1}, \sigma_{2} \text{ s.t. } \sigma = (\sigma_{1} | \sigma_{2}), \quad c(\sigma) \geq \max\{ and upper bounded by a multiple of its total variation, $$\exists k \in [0, \infty), \quad c(\sigma) \leq k \mathop{\mathrm{TV}}(\sigma),$$ where \(\mathrm{TV}(\sigma) \) denotes the total variation of the path\(\sigma \)[karaman\_ijrr2011].

<!-- chunk {"id": "body-0024", "role": "body", "section": "Cost Function Assumptions", "weight": 1.0} -->

It is also assumed that only trivial paths consisting of a single state can have zero cost, $$c(\sigma) = 0 \iff \forall\; t \, \sigma(t) = \sigma.$$

<!-- chunk {"id": "body-0025", "role": "body", "section": "Obstacle Assumption", "weight": 1.0} -->

The obstacle configuration of the optimal path planning problem is assumed to allow for a valid path from the start to the goal that remains a fixed \(\delta > 0 \), from its nearest obstacles for its entire length, $$\exists\; \sigma \in \Sigma, \delta \in (0, \infty), \; \text{s.t.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Optimal Solution Assumption", "weight": 1.0} -->

At least one solution of the optimal path planning problem, \(\sigma^{*} \in \Sigma \), is assumed to be homotopic to a path, \(\sigma\_{\delta} \in \Sigma \), with strong \(\delta \)-clearance, $$\exists\; H \colon \to \Sigma, \quad H = \sigma^{*}, H = \sigma_{\delta},$$ where \(H \) is a homotopic map whose image is the set of all valid paths from the start to the goal. Such a solution is said to have weak

<!-- chunk {"id": "body-0027", "role": "body", "section": "Literature Review", "weight": 1.0} -->

Almost-surely asymptotically optimal planning is a popular area of [gammell\_arcras2021]. This section focuses on sampling-based and graph-search techniques to calculate and/or exploit heuristics to improve performance. Sampling-based planners that use heuristics to guide the sampling and/or order the search are reviewed in [Section]sec:sampling-based-planning-with-heuristics. Approaches that calculate and exploit accurate cost heuristics for graph-search algorithms are reviewed in [Section]sec:improved-heuristics-for-informed-search and algorithms that use effort heuristics in [Section]sec:effort-and-distance-based-heuristics-in-informed-search. Using heuristics in sampling-based planning has parallels with lazy collision detection, which is reviewed in [Section]sec:sampling-based-planning-with-lazy-collision-detection.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Heuristics in Sampling-Based Planning", "weight": 1.0} -->

Sampling-based planning algorithms can improve their performance by using heuristics to bias their sampling and guide their search.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Heuristics in Sampling-Based Planning", "weight": 1.0} -->

RRT-Connect[kuffner\_icra2000] builds on RRT by growing two trees, one rooted in the start and one in the goal state. These trees each explore the state space around them, but are also guided towards each other with a connect heuristic. This approach can result in very fast initial solution times, but does not consider the solution cost and can consequently not improve the solution given more computational time. Almost-surely asymptotically optimal variants of RRT-Connect exist[akgun\_iros2011,jordan\_tr2013,klemm\_robio2015,qureshi\_ras2015,burget\_iros2016]but the connect heuristic does not guide the search beyond finding an initial solution. hRRT hRRThRRT and AC@GBRRT@used GBRRT GBRRTGBRRT bias the growth of their trees with cost heuristics. hRRT uses a priori heuristics to weigh the Voronoi regions of RRT.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Heuristics in Sampling-Based Planning", "weight": 1.0} -->

GBRRT is a bidirectional version of RRTthat guides the forward tree with heuristics computed by the reverse tree. These algorithms have improved performance but do not provide any bounds on the quality of their solution.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Heuristics in Sampling-Based Planning", "weight": 1.0} -->

RRT*[gammell\_iros2014, gammell\_tro2018] builds on RRT* by using an admissible cost heuristic to ensure that only states that can improve the current solution are processed. This improves RRT*'s convergence rate and retains its almost-sure asymptotic optimality, but does not guide the search with the heuristic, does not improve the accuracy of the heuristic as the search progresses, and does not provide any benefits until an initial solution is found. [kunz\_icra2016] and [yi\_icra2018] extend informed sampling to kinodynamic systems. [joshi\_icra2019] present a variant of Informed RRT*that uses previous collision detection results and available information in the graph structure to guide the search.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Heuristics in Sampling-Based Planning", "weight": 1.0} -->

RRTsharp[arslan\_icra2013, arslan\_icra2015] builds on RRT* by ensuring that all samples are optimally connected to the search tree after each iteration. It does this efficiently by using an admissible cost heuristic to update the connections of suboptimally connected samples in order of their total potential solution cost. This again improves RRT*'s convergence rate and retains its almost-sure asymptotic optimality, but can also not improve the accuracy of the heuristic as the search progresses and does not provide any benefits until an initial solution is found. [sakcak\_lcss2020] present a method that incorporates a heuristic into a version of RRT* that is based on motion primitives[sakcak\_ar2019]. This can improve the performance on kinodynamic problems but uses a discretization of the state space that suffers from the curse of dimensionality[bellman\_book1957].

<!-- chunk {"id": "body-0033", "role": "body", "section": "Heuristics in Sampling-Based Planning", "weight": 1.0} -->

IST ISTIST, A*-RRT[li\_icra2011], the \(f \)-biasing method[kiesel\_socs2012], P-PRM[le\_iros2014], and RIOT RIOTRIOT all search a simplified approximation of the state space to calculate an accurate cost heuristic, which is then used to guide a sampling-based planner. These approaches improve planning performance but require a preprocessing step.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Heuristics in Sampling-Based Planning", "weight": 1.0} -->

BEAST BEASTBEAST is similar to these methods in that it runs PRMon a simplified abstraction of the problem and uses the resulting graph to calculate an effort heuristic for the samples in the simplified space. If searching the original space reveals that regions in the abstract space cannot easily be connected, then this effort heuristic is updated in a Bayesian manner. BEAST tends to find initial solutions faster than other planners but does not provide any guarantees on the quality of its solutions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Heuristics in Sampling-Based Planning", "weight": 1.0} -->

QMP QMPQMP,AC@QRRT@used QRRT QRRTQRRT, and their asymptotically optimal variants QMP* and QRRT*[orthey\_arxiv2020b]solve planning problems with sequences of admissible lower-dimensional simplifications of increasing dimensionality. Paths in lower-dimensional simplifications can guide the sampling of states in higher dimensional simplifications and can be seen as admissible heuristics. This can improve performance by orders of magnitude, especially for high-dimensional problems, but requires the user to manually specify the sequence of lower-dimensional simplifications for each problem.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Heuristics in Sampling-Based Planning", "weight": 1.0} -->

MPLB MPLBMPLB is an anytime adaption of FMT*[janson\_isrr2013, janson\_ijrr2015] that incorporates admissible cost heuristics. MPLBuses two passes of Dijkstra's algorithm to restrict the set of samples to be searched and another pass of Dijkstra's to calculate an admissible cost heuristic for these samples, all without detecting collisions. It then uses the resulting cost heuristic in a forward search with collision detection to find a path. This approach can result in accurate, admissible cost heuristics and requires few collision detections but does not update the heuristic when the forward search detects collisions on edges that were used to compute the heuristic.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Heuristics in Sampling-Based Planning", "weight": 1.0} -->

BIT* samples batches of states and views these states as an increasingly dense edge-implicit AC@RGG@used RGG RGGRGG. It uses an admissible cost heuristic to search this graph in order of potential solution quality with techniques similar to AC@LPA*@used LPA* {koenig\_ai2004, likhachev\_icaps2005b, aine\_ai2016}aine\_ai2016LPA*LPA* {koenig\_ai2004, likhachev\_icaps2005b, aine\_ai2016}. AC@ABIT*@used ABIT* ABIT*ABIT* speeds up initial solution times by inflating its heuristic, similar to AC@ARA*@used ARA* ARA*ARA*, and balances exploring the state space with exploiting the current RGG approximation by truncating its search, similar to TLPA* TLPA*TLPA*.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Heuristics in Sampling-Based Planning", "weight": 1.0} -->

Both algorithms work best when the cost of a path correlates well with the computational effort required to validate it and when accurate cost heuristics are available a priori, but require that these heuristics are admissible and do not improve their accuracy as the search AIT* and EIT*, the methods in this section use heuristics to improve the performance of sampling-based planning algorithms. In contrast to AIT* and EIT*, these methods either do not apply heuristics to all aspects of the search, do not provide any bounds on the quality of their solution, require a preprocessing step, do not calculate problem-specific heuristics, or do not improve the accuracy of the heuristic as the search

<!-- chunk {"id": "body-0039", "role": "body", "section": "Improved Heuristics in Graph-Search", "weight": 1.0} -->

Developing and exploiting accurate heuristics is an important area of research in informed graph-search algorithms. Techniques to calculate more accurate heuristics have improved performance in various problem domains, e.g., [culberson\_cscsi1996], Rubik's Cube[korf\_ncai1997], and robot vacuum on a grid[thayer\_icaps2011b]. [culberson\_cscsi1996, korf\_ncai1997, culberson\_ci1998] are precomputed tables of exact solution costs to potentially simplified subproblems of a problem domain. The highest solution cost of any remaining subproblem in an ongoing search can be used as an accurate heuristic for an informed search. Additive pattern databases[felner\_jair2004]are constructed such that the heuristic remains admissible when the solution costs of all remaining subproblems are combined, which can result in more accurate heuristics. This increased accuracy can significantly improve performance, but is confined to problem domains for which pattern databases can be generated.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Improved Heuristics in Graph-Search", "weight": 1.0} -->

HA* HA*HA* uses homomorphic transformations of the state space to create abstractions in which multiple states of the original space are mapped to a single state in abstract space. These abstractions are then searched to calculate a heuristic for the original state space. This can result in fewer expanded states, but the presented technique is only shown to work for graphs with uniform edge costs. AC@HCA*@used HCA* HCA*HCA* and AC@WHCA*@used WHCA* WHCA*WHCA* are multiagent versions of HA* that use AC@RRA*@used RRA* RRA*RRA* to search the abstraction from the goal to the start. The cost of the optimal paths to states from the goal in the abstract space is used as the heuristic for the corresponding states in the original space. If the search in the original space processes a state whose abstract representation has not been processed by RRA*, then RRA*is resumed until it finds the optimal path to an abstract state that corresponds to the state being processed by the search in the original space.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Improved Heuristics in Graph-Search", "weight": 1.0} -->

This results in lower cost paths and better success rates than alternative multi-agent search algorithms, but cannot directly be applied to single-agent planning in continuous spaces.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Improved Heuristics in Graph-Search", "weight": 1.0} -->

AA* AA*AA* is an incremental search algorithm that calculates an increasingly accurate, admissible cost heuristic for subsequent searches of a graph with the same goal but different start states. After each search, the heuristic cost-to-go value of each closed state is updated to be the difference between the solution cost and the cost-to-come value of that state. This results in increasingly efficient searches of any problem domain but does not provide any benefits for the initial search of a graph. [thayer\_icaps2011b] also generates more accurate heuristics for any domain. It uses a relationship between the cost-to-go of a state and the cost-to-go of its best child to define a single-step errorin the cost heuristic. The mean single-step error in this heuristic is then calculated either globally or per branch and used to adjust the heuristic accordingly. This approach can be used in the initial search but is not guaranteed to produce admissible heuristics.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Improved Heuristics in Graph-Search", "weight": 1.0} -->

Add method[kaindl\_jair1997] uses a bidirectional search in which a partial reverse search generates heuristics that inform the forward search. The reverse search reveals errors in the heuristic values of the processed states, the minimum of which is added to the heuristic values of all unexpanded states in the forward search. This results in a more informed heuristic that remains admissible, but increases the heuristic value for all unexpanded states uniformly and requires a user-defined parameter that specifies how many states to expand in the reverse search. A version without this parameter is presented by [wilt\_cai2013].

<!-- chunk {"id": "body-0044", "role": "body", "section": "Improved Heuristics in Graph-Search", "weight": 1.0} -->

AIT* and EIT*, the methods in this section generate increasingly accurate heuristics that result in increasingly efficient searches. In contrast to AIT* and EIT*, these methods either require preprocessing, cannot be used for the initial search of a graph, result in inadmissible heuristics, or increase the heuristic value for all unexpanded states uniformly and only order by estimated solution cost.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Effort Heuristics in Graph-Search", "weight": 1.0} -->

Ordering the search based on (inflated) cost heuristics improves anytime performance the most when the cost of a path correlates well with the computational effort required to find it [wilt\_socs2012]. Directly ordering the search on the computational effort of a path can instead improve performance even when this is not the case. The graph-search literature often uses the number of states that must be expanded to find a solution as a proxy for the total search effort.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Effort Heuristics in Graph-Search", "weight": 1.0} -->

DWA* DWA*DWA* aims to improve performance by ordering its search in a manner that rewards progress away from the start. It multiplies an admissible cost heuristic by a weighting factor that decreases with increasing depth in the search tree. This is shown to reduce the number of expanded states on some problem domains, but requires an a priori estimate of the solution depth and implicitly assumes that every step away from the start is a step closer to the goal. Revised DWA*[thayer\_icaps2009] removes this assumption, but still requires an a prioriestimate of the solution \(\_{\varepsilon}^{*}\)[pearl\_pami1982]aims to expand states that are as close to the goal as possible and could be part of a solution whose cost is within a user-specified factor of the optimal cost. It always expands the node with the least number of states left to be expanded, provided it could be part of a solution within the suboptimality bound according to an admissible cost heuristic.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Effort Heuristics in Graph-Search", "weight": 1.0} -->

This works well if loose suboptimality bounds are acceptable or a very accurate cost heuristic is available, but otherwise forces the search to expand states with a large estimate of states left to be expanded just to increase the lower bound on the optimal solution cost.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Effort Heuristics in Graph-Search", "weight": 1.0} -->

EES EESEES aims to always expand the node which most quickly leads to a solution whose cost is within a user-specified bound of the optimal cost. It uses an admissible cost heuristic to guarantee the bound on the suboptimality and inadmissible cost and effort heuristics to guide its search. This significantly improves search performance in domains where solution cost and depth can differ, but introduces computational overhead and algorithmic complexity because EES must maintain three queues ordered on three different quantities. AEES is an anytime version of EES and provides the foundation of the forward search of EIT*, which is discussed in [Section]sec:eit-forward-search.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Effort Heuristics in Graph-Search", "weight": 1.0} -->

AIT* and EIT*, the methods in this section use estimates of the computational effort required to discover a solution to guide the search and improve performance. In contrast to AIT* and EIT*, these methods do not increase the accuracy of their heuristics as the search progresses.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Lazy Collision Detection", "weight": 1.0} -->

A byproduct of using heuristics in sampling-based planning to bias the sampling and guide the search is often that fewer edges have to be fully evaluated [Figure]fig:evaluated-edges. This relates informed path planning algorithms to algorithms with lazy collision detection that explicitly aim to minimize the number of collision detections.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Lazy Collision Detection", "weight": 1.0} -->

PRM[bohlin\_icra2000] and Fuzzy PRM[nielsen\_iros2000] take similar approaches to minimizing computational effort through lazy collision detection. Both algorithms initially connect samples without performing any collision detection on the edges. The resulting graph is processed with an informed graph-search algorithm to find a path that connects the start and goal states, and only checked for collision once a path is found. If collisions are detected, then the corresponding vertices and edges are removed from the graph and the updated graph is processed again to find a new path between the start and goal states. This results in few fully evaluated edges and improved planning performance, but Lazy PRM and Fuzzy PRM do not provide any guarantee on the quality of its solution and do not improve the accuracy of the heuristic used in their graph-search algorithm. Almost-surely asymptotically optimal variants of similar approaches exist[hauser\_icra2015, kim\_icra2018]but these algorithms also do not improve the accuracy of their heuristics as the search SBL planner[sanchez\_rr2003] combines lazy collision detection with ideas from RRT-Connect.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Lazy Collision Detection", "weight": 1.0} -->

It grows two trees, similar to RRT-Connect, but only checks collisions on edges that it believes to be on a path connecting the start and goal states, like Lazy PRM and Fuzzy PRM. SBLachieves fast solution times, but does also not provide any guarantees on the quality of its solution and does not improve its solution given more computational time.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Lazy Collision Detection", "weight": 1.0} -->

LBT-RRT LBT-RRTLBT-RRT extends RRT* with a graph whose edges are not fully evaluated and uses this graph to determine which edges to evaluate next. LBT-RRT is almost-surely asymptotically near-optimal and allows for continuous interpolation between RRT and RRG RRGRRG by only rewiring states that are \(\varepsilon \)-inconsistent. A similar approach is used for replanning in RRTX[otte\_afr2015,otte\_ijrr2016]. Interpolating LBT-RRT between RRT and RRG allows for balancing exploration with exploitation, but LBT-RRTcan only optimize path length.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Lazy Collision Detection", "weight": 1.0} -->

LazySP Framework[dellin\_icaps2016] explicitly aims to minimize the number of edges that are checked for collision. It first finds a path from the start to the goal using a heuristic for the edge cost and then uses an edge selector to determine the order in which the edges on the potential solution path are checked for collision. This often results in few fully evaluated edges, but is not asymptotically optimal and restarts the search every time an edge is found to be invalid. GLS GLSGLS builds on LazySP by presenting a framework that can algorithmically balance edge evaluation with continuing the search, but is also not asymptotically optimal. LRHA* LRHA*LRHA* is an example algorithm that fits within the LazySP and GLSframeworks.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Lazy Collision Detection", "weight": 1.0} -->

AIT* and EIT*, the methods in this section improve performance by reducing the number of full edge evaluations. In contrast to AIT* and EIT*, these methods either do not use heuristics, do not improve the accuracy of their heuristics, do not guarantee any bounds on the quality of their solution, do not improve their solution given more computation time, or can only optimize path length.

<!-- chunk {"id": "body-0056", "role": "body", "section": "AIT* and EIT*", "weight": 1.0} -->

AIT* and EIT* are almost-surely asymptotically optimal path planning algorithms that build on BIT*. BIT* approximates the state space with a batch of samples, which it views as an edge-implicit RGG. BIT* searches this RGG in order of the total potential solution quality of its edges until it can guarantee that it has found the resolution-optimal solution, i.e., the optimal solution in the current approximation of the state space. Once the search is finished, BIT* improves its RGG approximation by adding a new batch of samples. In this way, BIT* approximates and searches a continuously valued state space by building and searching a series of increasingly dense, edge-implicit RGG.

<!-- chunk {"id": "body-0057", "role": "body", "section": "AIT* and EIT*", "weight": 1.0} -->

BIT* processes the implicit edges of its current RGG approximation in order of their total potential solution cost, using incremental search techniques similar to an edge-queue version of TLPA*. It estimates the total potential solution cost of an edge as the sum of the current cost to come to the source of the edge, a heuristic estimate of the edge cost, and a heuristic estimate of the cost to go from the target of the edge. The formal guarantees of BIT*require that these cost heuristics AIT* and EIT* extend BIT* with an asymmetric bidirectional search that unifies many of the benefits reviewed in [Section]sec:literature-review by leveraging information implicit in the observed distribution of valid states [Figure]fig:benefits-of-adaptive-heuristics. The reverse searches of AIT* and EIT*calculate accurate heuristics which are exploited by their forward searches. The forward searches in turn inform the reverse searches if they used invalid edges to compute the heuristic. In this way, both searches continuously inform each other with complementary information.

<!-- chunk {"id": "body-0058", "role": "body", "section": "AIT* and EIT*", "weight": 1.0} -->

The reverse searches of AIT* and EIT* evaluate edges approximately and are therefore computationally inexpensive. The forward searches of AIT* and EIT* evaluate edges fully and are therefore computationally expensive, but focused by the calculated problem-specific heuristics. This computational asymmetry avoids the inefficiency of naive symmetric bidirectional informed search, where frontiers of expensive searches pass each other[pohl\_phd1969].

<!-- chunk {"id": "body-0059", "role": "body", "section": "AIT* and EIT*", "weight": 1.0} -->

An overview of the search algorithms used in AIT* and EIT* is provided in [Table]tbl:forward-and-reverse-searches. The rest of this section presents the notation used in this paper [Section]sec:notation, the algorithmic details of AIT* and EIT* (Sections[sec:adaptively-informed-trees] and[sec:effort-informed-trees]), and the formal analysis of their asymptotic optimality [Section]sec:analysis.

<!-- chunk {"id": "body-0060", "role": "body", "section": "EIT*-specific Notation", "weight": 1.0} -->

Potentially inadmissible effort heuristics between two states are denoted by \(\bar{e}\colon X \times X \to [0, \infty) \). These heuristics estimate the computational effort required to find and validate a path between two states, e.g., the number of necessary collision detections on the path. Potentially inadmissible effort heuristics between each state and the start are denoted by the function \(\bar{d}\colon X \to [0, \infty) \) and often defined as \(\bar{d}\left(\bm{\mathrm{x}} \right) \coloneqq \bar{e}\left(\bm{\mathrm{x}}, \bm{\mathrm{x}}\_{\mathrm{start}} \right) \). Potentially inadmissible cost heuristics between two states are denoted by the function \(\bar{c}\colon X \times X \to [0, \infty) \).

<!-- chunk {"id": "body-0061", "role": "body", "section": "AIT*", "weight": 1.0} -->

AIT* improves on BIT* by using the same increasingly dense RGG approximation but searching it with an asymmetric bidirectional search which calculates and exploits a more accurate cost heuristic that is specific to each RGG approximation [Figure]fig:aitstar-step-by-step. This results in a more efficient search with fewer evaluated edges when an admissible cost heuristic is available a priori (Figures[fig:example-bitstar-path-length],fig:example-aitstar-path-length, and can improve initial solution times and convergence rates.

<!-- chunk {"id": "body-0062", "role": "body", "section": "AIT*", "weight": 1.0} -->

AIT* consists of three high-level steps: [(i), itemjoin= itemjoin*=; and] improving the RGG approximation (sampling; [Section]sec:ait-approximation) updating the heuristic (reverse search; [Section]sec:ait-reverse-search) finding valid paths in the current RGG approximation (forward search; [Section]sec:ait-forward-search), as shown by Algorithm[alg:conceptual]. The full technical details of AIT* are given in Algorithms[alg:aitstar:technical][alg:aitstar:prune].

<!-- chunk {"id": "body-0063", "role": "body", "section": "AIT*", "weight": 1.0} -->

The reverse search of AIT* is a version of LPA* that calculates accurate cost heuristics by combining an admissible cost heuristic between multiple states into a more accurate cost heuristic between each state and the goal. The calculated cost heuristic is admissible for the current RGGand leverages information implicit in the observed distribution of valid states. This reverse search is computationally inexpensive because it does not perform collision detection on the edges.

<!-- chunk {"id": "body-0064", "role": "body", "section": "AIT*", "weight": 1.0} -->

If the reverse search finishes without reaching the start, then the start and goal are not in the same connected component of the current approximation. AIT* skips the forward search in this case and directly improves the RGG approximation. This ensures that AIT*does not spend computational effort searching a graph that it knows cannot contain a solution.

<!-- chunk {"id": "body-0065", "role": "body", "section": "AIT*", "weight": 1.0} -->

The forward search of AIT* is an edge-queue version of A* which efficiently exploits the calculated heuristic and evaluates few edges that do not contribute to a solution when admissible cost heuristic are available a priori. If the forward search detects a collision on an edge in the reverse search tree, then LPA* updates the heuristic by efficiently repairing this tree. The forward search then continues with the updated heuristic until the optimal solution on the current RGG approximation is found or another collision is detected on an edge in the reverse search tree. This process is repeated as time allows to almost-surely asymptotically converge towards the optimal solution in an anytime manner [Figure]fig:aitstar-step-by-step.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Approximation", "weight": 1.0} -->

AIT* incrementally approximates the state space by sampling batches of \(m \) valid states(Alg.[alg:aitstar:technical], line[alg:aitstar:improve-approximation:sample]). States are sampled uniformly in the informed set, using informed sampling[gammell\_tro2018] when possible. These samples are viewed as a series of increasingly dense, edge-implicit RGGs where bidirectional edges are defined either by a connection radius, \(r \), or by the mutual \(k \)-nearest neighbors[janson\_ijrr2015].

<!-- chunk {"id": "body-0067", "role": "body", "section": "Approximation", "weight": 1.0} -->

\frac{1}{n} \right) \log\left(q \right), where \(q \) is the number of sampled states in the informed set, \(\eta > 1 \) is a tuning parameter, \(\lambda(\cdot) \) denotes the Lebesgue measure, and \(B\_{1, n} \) is the \(n \)-dimensional unit ball.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Approximation", "weight": 1.0} -->

\(r \)-disc strategy can result in better performance than the \(k \)-nearest version but the computation of the \(r \)-disc radius must be adjusted to the properties of the state space[kleinbort\_wafr2016, Faster-decreasing radii are presented in[janson\_ijrr2015, janson\_ijrr2018], [solovey\_ijrr2020], and [tsao\_icra2020], but are not used in AIT* and EIT*for direct comparison to existing algorithms as they are presented in the literature.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Approximation", "weight": 1.0} -->

AIT* considers the combination of both this RGG definition and any existing connections in the forward search tree and ignores edges known to be invalid(Alg.[alg:aitstar:neighbors], lines[alg:aitstar:neighbors:forward-children] and[alg:aitstar:neighbors:invalid]). RGG complexity is reduced by pruning samples that are not in the informed set(Alg.[alg:aitstar:technical], line[alg:aitstar:improve-approximation:prune] and Alg.[alg:aitstar:prune]).

<!-- chunk {"id": "body-0070", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

AIT* calculates an accurate cost heuristic between each processed state and the goal that is admissible for the current RGG approximation. It does this by calculating the a priori admissible cost heuristic, \( \hat{c}\left( \,\cdot\ \,\cdot\, \right) \), over the connectivity of this approximation.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

This is achieved by processing the RGG approximation with a version of LPA* that is rooted at the goal and uses the admissible a priori cost heuristics, \(\hat{c}\left(\,\cdot\ \,\cdot\, \right) \), as edge costs without detecting collisions on the edges. The resulting reverse search tree can be updated efficiently because LPA* stores the cost of a state when it was first connected or last rewired and when it was last expanded, denoted by \(\hat{h}\_{\mathrm{con}}[\bm{\mathrm{x}}] \) and \(\hat{h}\_{\mathrm{exp}}[\bm{\mathrm{x}}] \), respectively. These are the \(g \) and \(v \) values in a forward LPA* search[aine\_ai2016].

<!-- chunk {"id": "body-0072", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

\(\hat{g}(\bm{\mathrm{x}}) \) denotes an admissible a priori cost heuristic between a state, \(\bm{\mathrm{x}} \), and the start.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

This key is used to extract the next edge from the reverse queue (Alg.[alg:aitstar:technical], lines[alg:aitstar:iterate-reverse-search:get-best-vertex] and[alg:aitstar:iterate-reverse-search:pop-best-vertex]).

<!-- chunk {"id": "body-0074", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

An uninitialized LPA* search is used to calculate the heuristic on the first batch of samples and after each new batch is added. This is more efficient than incrementally updating the heuristic with LPA* for the large changes in the graph that result from increasing its resolution[koenig\_ai2004, likhachev\_icaps2005b, aine\_ai2016].

<!-- chunk {"id": "body-0075", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

An uninitialized LPA* search is started by clearing the reverse search tree (except for the goals), setting the \(\hat{h}\_{\mathrm{con}} \) and \(\hat{h}\_{\mathrm{exp}} \) values of all states to infinity (again, except for the goals), and inserting the goal states into the reverse queue(Alg.[alg:aitstar:technical], lines[alg:aitstar:technical:initialize-reverse],[alg:aitstar:technical:reinitialize-reverse-tree-begin], and[alg:aitstar:technical:reinitialize-reverse-tree-end]).

<!-- chunk {"id": "body-0076", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

The heuristic is updated whenever an edge in the reverse search tree is found to be invalid by removing this edge from the RGG approximation and repairing the reverse search tree with LPA*. This is accomplished by updating the cost-to-go of the source state of the invalid edge and then running LPA* to update the cost of all affected states as necessary(Alg.[alg:aitstar:technical], lines[alg:aitstar:iterate-reverse-search:get-best-vertex][alg:aitstar:iterate-reverse-search:end] and[alg:aitstar:iterate-forward-search:blacklist][alg:aitstar:iterate-forward-search:invalidate-reverse-branch] and Alg.[alg:aitstar:invalidate-reverse-branch]).

<!-- chunk {"id": "body-0077", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

The reverse search is suspended when the total potential solution cost of the best state in the reverse queue is greater than or equal to that of the best edge in the forward queue and the target of the best edge in the forward queue is consistent (Alg. [alg:aitstar:technical] lines[alg:aitstar:technical:continue-reverse-search-1] and[alg:aitstar:technical:continue-reverse-search-2]). This guarantees that no other edge in the forward queue would be better if the reverse search was continued[strub\_phd2021]. The reverse search is also suspended when the reverse or forward queue is empty or when all edges in the forward queue have consistent targets with a reverse-key value less than or equal to the minimum reverse-key in the reverse queue, but these conditions are omitted from Algorithm[alg:aitstar:technical]for clearer structure.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Forward Search", "weight": 1.0} -->

A forward search iteration begins by testing if the forward queue contains an edge that can possibly improve the current solution (Alg. [alg:aitstar:technical], line[alg:aitstar:technical:continue-forward-search]). If it does, then the edge with the lowest \(\mathtt{key}\_{\mathcal{F}}^{\text{AIT*}} \)-value is extracted from the forward queue(Alg.[alg:aitstar:technical], lines[alg:aitstar:iterate-forward-search:get-best-edge] and[alg:aitstar:iterate-forward-search:pop-best-edge]). If this edge is already in the forward tree, then its target is expanded into the forward queue and the iteration is complete(Alg.[alg:aitstar:technical], lines[alg:aitstar:iterate-forward-search:is-edge-in-tree] and[alg:aitstar:iterate-forward-search:expand-edge-in-tree]).

<!-- chunk {"id": "body-0079", "role": "body", "section": "Forward Search", "weight": 1.0} -->

If the edge is not in the forward tree but can possibly improve it, then it is checked for validity which is computationally expensive (Alg.[alg:aitstar:technical], lines[alg:aitstar:iterate-forward-search:can-edge-possibly-improve-tree] and[alg:aitstar:iterate-forward-search:collision-detection]).

<!-- chunk {"id": "body-0080", "role": "body", "section": "Forward Search", "weight": 1.0} -->

If the edge is invalid, then it is added to the set of invalid edges (Alg.[alg:aitstar:technical], line[alg:aitstar:iterate-forward-search:blacklist]) and if it is also part of the reverse tree, then the heuristic is updated with the reverse search(Alg.[alg:aitstar:technical], lines[alg:aitstar:iterate-reverse-search:get-best-vertex][alg:aitstar:iterate-reverse-search:end],[alg:aitstar:iterate-forward-search:reverse-tree-check],[alg:aitstar:iterate-forward-search:invalidate-reverse-branch], and Alg.[alg:aitstar:invalidate-reverse-branch]).

<!-- chunk {"id": "body-0081", "role": "body", "section": "Forward Search", "weight": 1.0} -->

If the edge is valid, then its true cost is evaluated which may also be computationally expensive and it is checked whether the edge can actually improve the current solution and forward tree(Alg.[alg:aitstar:technical], lines[alg:aitstar:iterate-forward-search:can-edge-actually-improve-solution] and[alg:aitstar:iterate-forward-search:can-edge-actually-improve-tree]).

<!-- chunk {"id": "body-0082", "role": "body", "section": "Forward Search", "weight": 1.0} -->

If the edge can improve the current solution and forward search tree, then its target is added to this tree if it is not already in it (Alg.[alg:aitstar:technical], lines[alg:aitstar:iterate-forward-search:add-state-to-tree-begin] and[alg:aitstar:iterate-forward-search:add-state-to-tree-end]). If it is already in the forward search tree, then the new edge constitutes a rewiring and the old edge is removed from the tree(Alg.[alg:aitstar:technical], line[alg:aitstar:iterate-forward-search:rewiring]). The new edge is added to the forward tree and its target is expanded regardless of whether the target was already in the tree or not(Alg.[alg:aitstar:technical], lines[alg:aitstar:iterate-forward-search:add-edge-to-tree] and [alg:aitstar:iterate-forward-search:expand-child-state]).

<!-- chunk {"id": "body-0083", "role": "body", "section": "Forward Search", "weight": 1.0} -->

A forward search iteration finishes by updating the current solution cost (Alg.[alg:aitstar:technical], line[alg:aitstar:iterate-forward-search:update-solution-cost]). In practice this is done efficiently by only checking the goals in the forward tree.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Forward Search", "weight": 1.0} -->

The entire forward search terminates when it is guaranteed that the optimal solution in the current RGG approximation is found. This occurs when no edge in the forward queue can possibly improve the current solution(Alg.[alg:aitstar:technical], alg:aitstar:technical:continue-forward-search). The forward search also terminates when the start and goal are not in the same connected component of the RGG approximation. This occurs when the reverse search tree does not reach any edge in the forward queue, but this condition is omitted from Algorithm[alg:aitstar:technical]for clearer structure.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Forward Search", "weight": 1.0} -->

The three steps of AIT*, i.e., improving the RGG approximation, updating the heuristic with the reverse search, and finding valid paths with the forward search, are repeated for as long as computational time allows or until a suitable solution is found. This results in increasingly accurate cost heuristics for increasingly efficient searches of increasingly accurate RGG approximations and will almost-surely asymptotically converge to the optimal solution in the limit of infinite samples [Section]sec:ait-analysis.

<!-- chunk {"id": "body-0086", "role": "body", "section": "EIT*", "weight": 1.0} -->

Informed planning algorithms guided by admissible cost heuristics, such as BIT*, ABIT*, and AIT*, need effective a priori admissible cost heuristics to provide benefits over uninformed algorithms. Such heuristics may not exist because the available admissible cost heuristics may be too computationally expensive or too inaccurate to be effective, even for AIT*. EIT* builds on AIT* by exploiting problem-specific information in a way that leverages informative admissible cost heuristics when they are available but can still search problems effectively when they are not. It achieves this by leveraging additional types of problem-specific information, including information on the computational effort required to validate a path.

<!-- chunk {"id": "body-0087", "role": "body", "section": "EIT*", "weight": 1.0} -->

This generalizes asymptotically optimal informed path planning algorithms to a broader class of problems that include those without effective EIT* consists of the same three high-level steps as AIT*: [(i), itemjoin= itemjoin*=; and] improving the RGG approximation (sampling; [Section]sec:ait-approximation) updating the heuristics (reverse search; [Section]sec:eit-reverse-search) finding valid paths in the current RGG approximation (forward search; [Section]sec:eit-forward-search), as shown in Algorithm[alg:conceptual]. Identically to AIT*, EIT* also approximates the state space with a series of increasingly dense RGGs and skips the forward search if the reverse search terminates without reaching the start. In contrast to AIT*, the reverse search of EIT* includes adaptive sparse collision detection on the edges and calculates both problem-specific path-cost and search-effort heuristics which are exploited in an anytime manner by the forward search of EIT*.

<!-- chunk {"id": "body-0088", "role": "body", "section": "EIT*", "weight": 1.0} -->

The full technical details of EIT* are given in Algorithms[alg:eitstar:technical] and[alg:eitstar:get-best-forward-edge] using the same \(\neighborstates*{} \), \(\expandstate*{} \), and \(\prunestates*{} \) subroutines as AIT* (Algs.[alg:aitstar:neighbors],[alg:aitstar:expand-edge], and[alg:aitstar:prune]).

<!-- chunk {"id": "body-0089", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

EIT* calculates an admissible cost heuristic, an inadmissible cost heuristic, and an inadmissible effort heuristic for each RGG approximation. The calculated admissible cost heuristic is a lower bound on the optimal cost of a path from a state to the goal and is denoted by the label \(\hat{h}[\,\cdot\,] \). The calculated inadmissible cost heuristic approximates the cost of an optimal path from a state to the goal and is denoted by the label \(\bar{h}[\,\cdot\,] \). This inadmissible cost heuristic is often more accurate than its admissible analogue because it can capture more problem-specific knowledge, including information that may overestimate the true cost. The calculated inadmissible effort heuristic approximates the computational effort required to find and validate a path from a state to the goal and is denoted by the label \(\bar{e}[\,\cdot\,] \).

<!-- chunk {"id": "body-0090", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

An example of such a heuristic is the number of collision checks required to validate a path, which is available and informative for all planning problems as it only depends on path length and collision detection resolution and not on the optimization These heuristics are computed as in AIT* with a reverse search that combines a priori heuristics between multiple states into more accurate heuristics between each state and the goal. The calculated admissible cost heuristic, \(\hat{h}[\,\cdot\,] \), is computed by combining a priori admissible cost heuristics, \(\hat{c}(\,\cdot\ \,\cdot\,) \), with a reverse search that preserves the admissibility of the heuristic between each state and the goal.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

The calculated inadmissible cost and effort heuristics, \(\bar{h}[\,\cdot\,] \) and \(\bar{e}[\,\cdot\,] \), are similarly computed with the inadmissible a priori cost and effort heuristics, \(\bar{c}\left(\,\cdot\ \,\cdot\,\right) \) and \(\bar{e}\left(\,\cdot\ \,\cdot\,\right) \). All three heuristics always have a value of zero for any goal state.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

The reverse search of EIT* is an edge-queue version of A* with adaptive sparse collision detection. Collision detection is traditionally considered a computationally expensive operation in sampling-based planning[hauser\_icra2015, kleinbort\_afr2020] but this is due to the computational cost of validating valid edges[sanchez\_rr2003]. Detecting invalid edges with sparse collision detection is computationally cheaper and was found to be of similar computational cost to other operations in the reverse search when solving the problems presented in [Section]sec:experimental-results.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

The two parts of the key represent the total potential solution cost of a path through an edge and the total potential computational effort required to validate a path through an edge, respectively. The first part of the key ensures the admissibility of the calculated cost heuristic and the second part of the key ensures tiebreaks in favor of lower estimated effort, which is important if only the trivially admissible cost heuristic is available, i.e., \(\forall \bm{\mathrm{x}}, \bm{\mathrm{x}}^{\prime} \in X, \hat{c}(\bm{\mathrm{x}}, \bm{\mathrm{x}}^{\prime}) \equiv \hat{g}(New heuristics are calculated when the RGG approximation is initialized or improved and updated when the forward search detects that the heuristics were calculated with an invalid edge.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

If the heuristics are calculated because of an initialized or improved approximation, then the resolution of the adaptive sparse collision detection is reset to a user-specified parameter (Alg.[alg:eitstar:technical], lines[alg:eitstar:technical:initialize-cd-resolution] and[alg:eitstar:improve-approximation:reinitialize-cd-resolution]). If they are updated because of an invalid edge, then the resolution of the sparse collision detection in the reverse search is increased(Alg.[alg:eitstar:technical], line[alg:eitstar:iterate-forward-search:update-cd-resolution]).

<!-- chunk {"id": "body-0095", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

Each iteration of the reverse search extracts the edge with the lowest \mathtt{key}\_{\mathcal{R}}^{\text{EIT*}} \)-value from the reverse queue (Alg.[alg:eitstar:technical], lines[alg:eitstar:iterate-reverse-search:get-best-rev-edge] and[alg:eitstar:iterate-reverse-search:remove-best-rev-edge]) and checks \(d \) evenly distributed states along this edge for collision (Alg.[alg:eitstar:technical], line[alg:eitstar:iterate-reverse-search:could-be-valid]).

<!-- chunk {"id": "body-0096", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

If a collision is found, then the edge is added to the set of invalid edges (Alg.[alg:eitstar:technical], line[alg:eitstar:iterate-reverse-search:remember-invalid-edge]), otherwise it is used to improve the inadmissible cost- and effort heuristics, if possible (Alg.[alg:eitstar:technical], lines[alg:eitstar:iterate-reverse-search:update-inad-cost] and[alg:eitstar:iterate-reverse-search:update-inad-effort]).

<!-- chunk {"id": "body-0097", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

The edge is then checked if it can improve the admissible cost heuristic of its target (Alg.[alg:eitstar:technical], line[alg:eitstar:iterate-reverse-search:admissible-cost-test]). If it can, then the heuristic is updated and the target is either rewired or added to the reverse search tree(Alg.[alg:eitstar:technical], lines[alg:eitstar:iterate-reverse-search:admissible-cost-update][alg:eitstar:iterate-reverse-search:insert-state-in-tree]). The reverse search iteration is completed by expanding the outgoing edges of the target into the reverse queue.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Reverse Search", "weight": 1.0} -->

AIT*, the reverse search is suspended when the total potential solution cost of the best edge in the reverse queue is greater than or equal to that of the best edge in the forward queue and the target of the best edge in the forward queue is closed(Alg.[alg:eitstar:technical] lines[alg:eitstar:technical:continue-reverse-search-1] and[alg:eitstar:technical:continue-reverse-search-2]). This guarantees that no other edge in the forward queue would be better if the reverse search was continued[strub\_phd2021]. The reverse search is also suspended when the reverse or forward queue is empty, when all edges in the forward queue have closed targets, or when the inflation factor is infinity and any edge in the forward queue has a target in the reverse tree, but these conditions are omitted from Algorithm[alg:eitstar:technical]for clearer structure.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Forward Search", "weight": 1.0} -->

The forward search of EIT* is an edge-queue version of AEES which exploits the cost and effort heuristics calculated by the reverse search of EIT* in an anytime manner. It leverages problem-specific cost and effort information and results in effective searches with fast initial solution times even when no admissible cost heuristics are available a priori ([Figures]fig:evaluated-edgesfig:example-eitstar-path-length,fig:example-eitstar-obstacle-clearance, AEES searches the same RGG approximation multiple times with successively tighter suboptimality bounds. It initially prioritizes quickly finding any solution over efficiently finding the resolution-optimum, which improves anytime performance. AEES is especially useful when no informative admissible cost heuristic is available a priori because it can exploit an effort heuristic to guide its search. Once an initial solution is found, EIT*uses both the calculated admissible and inadmissible cost heuristics to improve the tree until it finds the resolution-optimum.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Forward Search", "weight": 1.0} -->

The forward search of EIT* orders its queue by considering [(i), itemjoin= itemjoin*=; and] a lower bound on the optimal solution cost an estimate of the optimal solution cost and an estimate of the minimum remaining effort to validate a solution within the current suboptimality bound.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Forward Search", "weight": 1.0} -->

EIT* first checks if the queue contains an edge that could improve the current solution (Alg.[alg:eitstar:technical], line[alg:eitstar:technical:continue-forward-search]). If none of the edges in the forward queue can, then the RGG approximation is improved by pruning states that are not in the informed set and sampling more states (Alg.[alg:aitstar:prune] and Alg.[alg:eitstar:technical], lines[alg:eitstar:improve-approximation:prune] and[alg:eitstar:improve-approximation:sample]).

<!-- chunk {"id": "body-0102", "role": "body", "section": "Forward Search", "weight": 1.0} -->

The reverse search tree and set of closed vertices are then reset (Alg.[alg:eitstar:technical], line[alg:eitstar:technical:reinitialize-reverse-tree]) and the forward and reverse search queues are reinitialized by inserting the outgoing edges of the start and goals, respectively(Alg.[alg:eitstar:technical], line[alg:eitstar:reinitialize-queues:expand-start-and-goals]).

<!-- chunk {"id": "body-0103", "role": "body", "section": "Forward Search", "weight": 1.0} -->

If at least one edge in the forward queue could improve the current solution, then the edge that is estimated to lead to the fastest improvement of the current solution is extracted from the queue (Alg. [alg:eitstar:technical], lines[alg:eitstar:iterate-forward-search:get-best-edge] and[alg:eitstar:iterate-forward-search:pop-best-edge], and Alg.[alg:eitstar:get-best-forward-edge]).

<!-- chunk {"id": "body-0104", "role": "body", "section": "Forward Search", "weight": 1.0} -->

(Alg.[alg:eitstar:get-best-forward-edge], lines[alg:eitstar:get-best-forward-edge:best-effort-test] and[alg:eitstar:get-best-forward-edge:best-effort-return]).

<!-- chunk {"id": "body-0105", "role": "body", "section": "Forward Search", "weight": 1.0} -->

This edge likely improves the current solution with the least amount of computational effort.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Forward Search", "weight": 1.0} -->

(Alg.[alg:eitstar:get-best-forward-edge], lines[alg:eitstar:get-best-forward-edge:best-cost-test] and[alg:eitstar:get-best-forward-edge:best-cost-return]).

<!-- chunk {"id": "body-0107", "role": "body", "section": "Forward Search", "weight": 1.0} -->

This edge likely steps towards the resolution-optimal solution. - Otherwise the edge that provides the lower bound on the optimal solution cost in the current RGG approximation, \(\left(\bm{\mathrm{x}}\_{\mathrm{s}}^{\hat{s}}, \bm{\mathrm{x}}\_{\mathrm{t}}^{\hat{s}} \right) \), is selected. This raises the lower bound on the optimal solution cost in the current RGG approximation and increases the number of candidates available to steps 1 and 2 in the next iteration(Alg.[alg:eitstar:get-best-forward-edge], lines[alg:eitstar:get-best-forward-edge:lower-bound-cost-else] and[alg:eitstar:get-best-forward-edge:lower-bound-cost-return]).

<!-- chunk {"id": "body-0108", "role": "body", "section": "Forward Search", "weight": 1.0} -->

The forward search in EIT* then proceeds similarly to AIT*. If the selected edge is in the forward search tree, then its target state is expanded and the forward search iteration is complete(Alg.[alg:eitstar:technical], lines[alg:eitstar:iterate-forward-search:is-edge-in-tree] and[alg:eitstar:iterate-forward-search:expand-edge-in-tree]). If the selected edge is not part of the forward search tree but can possibly improve it, then it is checked for collisions(Alg.[alg:eitstar:technical], lines[alg:eitstar:iterate-forward-search:can-edge-possibly-improve-tree] and[alg:eitstar:iterate-forward-search:collision-detection]).

<!-- chunk {"id": "body-0109", "role": "body", "section": "Forward Search", "weight": 1.0} -->

If collisions are detected, then the edge is added to the invalid edges (Alg. [alg:eitstar:technical], line[alg:eitstar:iterate-forward-search:blacklist]) and if it is in the reverse search tree, then the reverse search tree and queue are reset and the sparse collision detection resolution is updated, which will improve the accuracy of the heuristic computed by restarting the reverse search (Alg.[alg:eitstar:technical], lines[alg:eitstar:iterate-forward-search:reverse-tree-check][alg:eitstar:iterate-forward-search:reexpand-goal-states]). If no collisions are detected, then the true cost of the edge is evaluated to check whether it actually improves the current solution and forward search tree (Alg.[alg:eitstar:technical], lines[alg:eitstar:iterate-forward-search:can-edge-actually-improve-solution] and[alg:eitstar:iterate-forward-search:can-edge-actually-improve-tree]).

<!-- chunk {"id": "body-0110", "role": "body", "section": "Forward Search", "weight": 1.0} -->

If the edge improves the current solution and forward search tree, then its target state is added to the tree if it is not already in it [alg:eitstar:technical], lines[alg:eitstar:iterate-forward-search:forward-tree-check] and[alg:eitstar:iterate-forward-search:add-state-to-tree]). If the target state is already in the tree, then the edge causes a rewiring and the edge from the old parent is removed from the tree (Alg.[alg:eitstar:technical], lines[alg:eitstar:iterate-forward-search:rewiring-else] and[alg:eitstar:iterate-forward-search:rewiring]).

<!-- chunk {"id": "body-0111", "role": "body", "section": "Forward Search", "weight": 1.0} -->

The new edge is then added to the tree, its target state is expanded into the forward queue, and the solution cost is updated (Alg.[alg:eitstar:technical], lines[alg:eitstar:iterate-forward-search:add-edge-to-tree][alg:eitstar:iterate-forward-search:update-solution-cost]). If the edge results in an improved solution, then the suboptimality factor is changed according to a user-specified update policy (Alg.[alg:eitstar:technical], lines[alg:eitstar:iterate-forward-search:update-inflation-factor]). Section[sec:experimental-results] presents the update policy used in the experimental evaluation of EIT*.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Forward Search", "weight": 1.0} -->

The entire forward search terminates when it is guaranteed that the optimal solution in the current RGG approximation is found. This occurs when no edge in the forward queue can possibly improve the current solution(Alg.[alg:eitstar:technical],alg:eitstar:technical:continue-forward-search). The forward search also terminates when the start and goal are not in the same connected component of the RGG approximation. This occurs when the reverse search tree does not reach any edge in the forward queue, but this condition is omitted from Algorithm[alg:eitstar:technical]for clearer AIT*, the three steps of EIT*, i.e., improving the RGG approximation, updating the heuristic with the reverse search, and finding valid paths with the forward search, are repeated for as long as computational time allows or until a suitable solution is found. This results in increasingly accurate cost and effort heuristics for increasingly efficient and effective searches of increasingly accurate approximations and will also almost-surely asymptotically converge to the optimal solution in the limit of infinite samples[Section]sec:eit-analysis.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Analysis", "weight": 1.0} -->

Any path planning algorithm that processes a sampling-based approximation with a graph-search algorithm is almost-surely asymptotically optimal if the approximation almost-surely contains an asymptotically optimal solution and the graph-search algorithm is resolution-optimal. This is a sufficient but not necessary condition. The almost-sure asymptotic optimality of EIT* follows from proven properties of their RGGapproximations and

<!-- chunk {"id": "body-0114", "role": "body", "section": "AIT*", "weight": 1.0} -->

RGG approximation constructed by AIT* almost-surely contains an asymptotically optimal solution because it contains all the edges in PRM* for any set of samples and PRM* is almost-surely asymptotically optimal[karaman\_ijrr2011]. AIT*'s forward search is resolution-optimal because A* is a resolution-optimal algorithm if it is provided with an admissible cost heuristic[hart\_tssc1968]. AIT*'s reverse search without collision detection results in an admissible cost-heuristic because LPA* is also a resolution-optimal algorithm[aine\_ai2016] and because adding collision detection cannot decrease path cost. AIT*is therefore almost-surely asymptotically optimal.

<!-- chunk {"id": "body-0115", "role": "body", "section": "EIT*", "weight": 1.0} -->

RGG approximation constructed by EIT* almost-surely contains an asymptotically optimal solution because like AIT* it also contains all the edges in PRM* and PRM* is almost-surely asymptotically optimal[karaman\_ijrr2011]. EIT*'s forward search is resolution-optimal because AEES is a resolution-optimal algorithm when the cost heuristic is admissible and the suboptimality factor is one[thayer\_icaps2011a]. EIT*'s reverse search with sparse collision detection results in an admissible cost heuristic because denser collision detection cannot decrease path cost and A* is a resolution-optimal graph-search algorithm when provided with an admissible cost heuristic[hart\_tssc1968]. EIT*is therefore also almost-surely

<!-- chunk {"id": "body-0116", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

The benefits of an asymmetric bidirectional search are shown on abstract, robotic manipulator, and knee replacement dislocation problems [sec:abstract-problems][sec:knee-implants]). AIT* and EIT* were compared against the AC@OMPL@used OMPL OMPLOMPL implementations of RRT, RRT-Connect, RRT*, LBT-RRT, LazyPRM*, FMT*, BIT*, and \({}^{1}\)Using OMPL v1.5.0 on a laptop with 16 GB of RAM and an Intel i7-4910MQ (2.9 GHz) processor running Ubuntu 18.04 The planners were tested when optimizing path length and obstacle clearance. Path length was optimized by minimizing the arc length of the path in state space.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Obstacle clearance was optimized by minimizing the reciprocal of clearance integrated over the arc length of the path, c(\sigma) &\coloneqq \int_{0}^{l} \frac{ 1 }{ \delta\left(\sigma(\nicefrac{s}{l}) \right) } \,\mathrm{d}s, where \(\delta\colon X \to [10^{-6}, \infty) \) is the distance of a state to the nearest obstacle, limited to be no smaller than \(10^{-6} \), \delta\left(\bm{\mathrm{x}} \right) \coloneqq \max \left\{ \mathop{\mathrm{clearance}}(\bm{\mathrm{x}}), 10^{-6} \right\}.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

The lower limit on \(\delta \) ensures numerical stability and that the cost of a path is bounded by a multiple of its total variation as in [Section]sec:cost-function-assumptions. This optimization objective balances the clearance and length of a path and is similar to the objectives presented by [wein\_ijrr2008] and [agarwal\_ta2018].

<!-- chunk {"id": "body-0119", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

The admissible cost heuristic, \(\hat{c} \), used by informed planners was the Euclidean distance for path length and the trivial zero-heuristic for obstacle clearance. The possibly inadmissible cost heuristic, \(\bar{c} \), used by EIT* was again the Euclidean distance for path length and the reciprocal of the average clearance of the two end states for obstacle clearance, \bar{c}\left(\bm{\mathrm{x}}_{i}, \bm{\mathrm{x}}_{j} \right) \coloneqq \frac{2}{\delta\left(\bm{\mathrm{x}}_{i} \right) + \delta\left(The effort heuristic, \(\bar{e}(\,\cdot\ \,\cdot\,) \), used by EIT*was the number of collision checks required to validate a path for both objectives. It was computed by dividing the Euclidean distance between two states by the collision detection resolution.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

The inflation factor update policy in EIT* was configured to have an infinite inflation factor until the initial solution is found and then switch to a unity inflation factor. This results in fast initial solutions and efficient subsequent searches to improve them. The sparse collision detection resolution update policy used in EIT*was configured to initially search each batch with a single collision check and then double the resolution if the forward search detects a collision on an edge used in the reverse search tree.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

RRT-based planners used maximum edge lengths of 0.3, 0.9, 1.25, 1.25, 2.4, and 3.0 in \(\mathbb{R}^{2}, \mathrm{SE}, \mathbb{R}^{7}, \mathbb{R}^{8}, \mathbb{R}^{14} \), and \(\mathbb{R}^{16} \), respectively. RRT* used informed sampling and LBT-RRT used the default approximation factor of 0.4 but was not tested on obstacle clearance problems as it can only optimize path length. BIT*-based planners used a batch size of \(100 \) samples and the \(k \)-nearest connection strategy with an RGG connection parameter of \(\eta = 1.001 \)regardless of problem dimension.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

FMT* is not an anytime algorithm and requires the user to specify the number of samples in advance. All experiments presented in this section tested FMT* with 10, 50, 100, 500, 1000, and 5000 samples. There are multiple lines for FMT*in the presented plots because median solution times and costs were computed separately for each configuration and the results of all configurations that were able to solve a specific problem were plotted.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Abstract Problem", "weight": 1.5} -->

State space obstacles have complex shapes even for relatively simple [das\_tro2020]. This complexity often makes it difficult to gain insight about the underlying reason for a planner's performance on a given problem. Directly designing abstract state space obstacles from basic geometries provides intuition on the performance of a planner for a given obstacle configuration and helps the algorithmic design The basic geometries of these simple obstacle configurations make collision detection computationally much less expensive than in real-world problems. A simple way to simulate the more expensive collision detection of real-world problems in this abstract setting is to increase the collision detection resolution. The collision detection resolution was set to which on the tested hardware makes evaluating a valid edge in this abstract setting as computationally expensive as evaluating a valid edge on a dual-arm manipulation problem[Section]sec:manipulator-arms. While admissible cost heuristics exist for these abstract problems with clearance in state space[strub\_tr2021], such heuristics often do not exist for real-world problems with clearance in work space and therefore no heuristics were used for the clearance objective in these abstract problems either.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Abstract Problem", "weight": 1.5} -->

The abstract obstacle configuration on which the planners were tested consists of a wall with a narrow gap between the start and goal states [Figure]fig:results:wall-gap. This obstacle configuration illustrates the speed with which planners find a hard-to-find optimal homotopy class when optimizing path length. When optimizing obstacle clearance, this configuration illustrates the challenges of searching in the absence of informative heuristics and ordering the search according to the total potential solution Three versions of the wall gap obstacle configuration in dimensions \(\mathbb{R}^{2}, \mathbb{R}^{8} \), and \(\mathbb{R}^{16} \) were tested for both objectives. The obstacle configuration shown in [Figure]fig:results:wall-gapwas adapted to higher dimensions by extending the obstacle such that only two homotopy classes exist for all problems. [Figure]fig:results:wall-gap-results shows the performance of all algorithms on all six instances of the problem when optimizing path length and obstacle clearance.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Abstract Problem", "weight": 1.5} -->

When optimizing path length, AIT* and EIT* perform similarly to Lazy PRM*, BIT*, and ABIT* and find initial solutions at least as fast as RRT-Connect and significantly faster than RRT* and LBT-RRT(Figures[fig:results:wall-gap-path-length-r2], fig:results:wall-gap-path-length-r8, and fig:results:wall-gap-path-length-r16). When optimizing obstacle clearance, EIT* outperforms all other tested asymptotically optimal planners, including AIT*, by again finding initial solutions as fast as RRT-Connect, which has a computational advantage because it does not calculate path cost (e.g., obstacle clearance, Figures[fig:results:wall-gap-clearance-r2], fig:results:wall-gap-clearance-r8, and fig:results:wall-gap-clearance-r16).

<!-- chunk {"id": "body-0126", "role": "body", "section": "Manipulator Problems", "weight": 1.0} -->

The algorithms were also tested on path planning problems for Barrett arms in the AC@OpenRAVE@used OpenRAVE OpenRAVEOpenRAVE. OpenRAVE was configured to use the AC@FCL@used FCL FCLFCL for collision detection and clearance computation, using AC@OBB@used OBB OBBOBB tree and AC@RSS@used volume representations, respectively. The collision detection and clearance computation resolution was set to \(3.6 \cdot 10^{-3} \), which resulted in a 1%false-negative collision detection rate for invalid edges on representative

<!-- chunk {"id": "body-0127", "role": "body", "section": "Single-Arm Manipulator Problem", "weight": 1.0} -->

Robotic manipulator arms are commonly used in pick-and-place tasks. In the single-arm experiment, the algorithms were instructed to find paths for a WAM arm with seven degrees of freedom to place a small cube into a box [Figure]fig:results:one-manipulator-arm. [Figure]fig:results:one-arm-results shows the performance of all algorithms when optimizing path length and obstacle clearance. When optimizing path length, AIT* and EIT* perform similarly to Lazy PRM*, BIT*, and ABIT*, which all find initial solutions nearly as fast as RRT-Connect and significantly faster than RRT* and LBT-RRT [Figure]fig:results:one-arm-path-length. When optimizing obstacle clearance, AIT* and EIT* outperform all other tested asymptotically optimal planners but do not find initial solutions as fast as RRT-Connect, which again has a computational advantage because it does not calculate path cost [Figure]fig:results:one-arm-clearance.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Dual-Arm Manipulator Problem", "weight": 1.0} -->

In the dual-arm planning experiment, the algorithms were instructed to find paths for two Barret WAM arms with a total of 14 degrees of freedom from a start configuration at the bottom shelf to a goal configuration at the top shelf [Figure]fig:results:two-manipulator-arms. [Figure]fig:results:two-arm-results shows the performance of all algorithms when optimizing path length and obstacle clearance. When optimizing path length, AIT* performs similarly to BIT* and ABIT* which perform better than Lazy PRM* and EIT* and find initial solutions nearly as fast as RRT-Connect and significantly faster than RRT* and LBT-RRT [Figure]fig:results:two-arm-path-length. When optimizing obstacle clearance, AIT* and EIT* again outperform all tested asymptotically optimal planners but do not find initial solutions as fast as RRT-Connect, which still has a computational advantage because it does not calculate path cost [Figure]fig:results:two-arm-clearance.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Knee Replacement Dislocation Problem", "weight": 1.0} -->

Calculating heuristics with an asymmetric bidirectional search can also improve performance on the feasible planning problem by guiding the search towards the goal. The knee replacement dislocation problem evaluates the potential of medial dislocation for the Oxford Domed Lateral UKR[pandit\_knee2010] \({}^{2}\)This experiment used an approximation of the Oxford Domed Lateral UKR due to copyright restrictions.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Knee Replacement Dislocation Problem", "weight": 1.0} -->

UKRby searching for a path to free the mobile bearing.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Knee Replacement Dislocation Problem", "weight": 1.0} -->

The Oxford Domed Lateral UKR consists of metal femoral and tibial components which are fixed to the bone and a mobile polythylene bearing which separates the metal components[gunther\_knee1996]. Medial dislocation occurs when there is enough space between the tibial and femoral components for the mobile bearing to move onto the tibial-component wall where it may be trapped by the femoral component. The dislocation risk for different relative poses of the femoral and tibial components has been analyzed by using planning algorithms to search for paths that allow the bearing to reach a region representative of dislocation[yang\_caos2020, yang\_bors2021]. [Figures]fig:results:knee-approximation andfig:results:knee-goal-region respectively illustrate the start state and goal region of the mobile bearing and the fixed poses of the tibial and femoral components used in this experiment. The state space of this problem is \(\mathrm{SE} \), and the mobile bearing is free to move and rotate in any direction not in collision with the fixed parts.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Knee Replacement Dislocation Problem", "weight": 1.0} -->

[Figure]fig:results:knee-results shows the performance of all planners when optimizing path length and obstacle clearance. When optimizing path length, EIT* outperforms all other tested planners. AIT* is the second best performing algorithm followed by FMT*, BIT*, and ABIT*. The OMPL implementations of LBT-RRT and RRT-Connect did not allow goals to be defined as a region and were replaced with RRT for this experiment. When optimizing obstacle clearance, EIT* again outperforms all other tested planners and is the only planner that achieved a success rate of 100%.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Discussion", "weight": 1.5} -->

The experiments presented in [Section]sec:experimental-results demonstrate the benefits of sampling-based path planning with an asymmetric bidirectional search. This section discusses the results of these experiments, elaborates on the algorithmic differences between AIT* and EIT*, and presents possible extensions to asymmetric bidirectional algorithms in sampling-based path planning and beyond. [Section]sec:experimental-results shows the performance of AIT*, EIT*, and eight other sampling-based algorithms on a diverse set of twelve problems optimizing two objectives. When optimizing path length, the experiments show that AIT* and EIT*are competitive to the other tested planners in terms of initial solution times, success rates, and solution quality over time.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Discussion", "weight": 1.5} -->

When optimizing obstacle clearance, the experiments show that outperforms all other tested asymptotically optimal planners by finding initial solutions faster, reaching 100% success rates sooner, and providing the highest quality solution for most of the time. AIT* is often the second-best performing planner on this objective and even competitive to EIT*on the robotic arm experiments.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Discussion", "weight": 1.5} -->

The batch size of AIT* and EIT* was kept constant for all presented experiments, while the performance of RRT-based planners was tuned to the problem dimension by adjusting the maximum edge length. This shows that AIT* and EIT*can perform well without problem-specific batch sizes but can also motivate future research to investigate advanced batch-size calculations, including variable and adaptive batch sizes.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Discussion", "weight": 1.5} -->

The experiments presented in [Section]sec:experimental-results keep the collision detection resolution constant within each problem. This resolution determines the false negative collision rate, i.e., the percentage of edges that are considered valid but in reality are not. What is considered an acceptable false negative collision rate depends on the application of the planning algorithm. Experiments not presented in this paper showed that the relative performance of AIT* and EIT* compared to other algorithms improves as edge evaluation becomes more computationally expensive, e.g., due to finer collision detection resolution or more complex analysis. This may be because AIT* and EIT* often fully evaluate fewer edges than other algorithms and their performance is therefore not as sensitive to the collision detection resolution. If edge evaluation is computationally inexpensive, e.g., due to coarse collision detection resolution, then the benefits of the accurate heuristics calculated in AIT* and EIT*may not justify the computational cost required to calculate them and other sampling-based planners may perform better in these cases.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Discussion", "weight": 1.5} -->

Edge evaluation is also computationally expensive for systems with kinodynamic constraints, when full edge evaluation requires solving a two-point The accurate heuristics calculated by AIT* and EIT* can reduce the number of BVP solved, but AIT* and EIT* require exact solutions to the BVP. Other almost-surely asymptotically optimal algorithms do not require exact BVP solutions even for problems with kinodynamic constraints[li\_ijrr2016, hauser\_tro2016, kleinbort\_icra2020, shome\_icra2021].

<!-- chunk {"id": "body-0138", "role": "body", "section": "Discussion", "weight": 1.5} -->

AIT* and EIT* use different algorithms for the reverse and forward searches of their asymmetric bidirectional search(Table[tbl:forward-and-reverse-searches]). The change in forward search algorithms from A* in AIT* to AEES in EIT* is motivated by the benefits of effort heuristics, which cannot be exploited with A*, and justify the computational overhead induced by the increased complexity of AEES. The change in reverse search algorithms from LPA* in AIT* to A* in EIT* is motivated by the observations that repairing the reverse search tree with LPA* is only more efficient than restarting A* for small changes in the search tree[aine\_ai2016], and that detecting invalid edges with the forward search often results in larger changes in the reverse search tree. Implementing increasingly dense collision detection in an LPA*reverse search would additionally require either further bookkeeping to keep track of which portion of the tree was checked with which resolution or result in duplicated collision detection effort on some of the edges.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Discussion", "weight": 1.5} -->

The presented asymmetric bidirectional approach in which two searches inform each other with complementary information can potentially be beneficial in all problem domains where full edge evaluation is computationally expensive, e.g., because of computationally expensive true edge cost computation or complex collision detection. If this edge cost computation can inexpensively be approximated by a heuristic, then the reverse search can combine such heuristics between multiple states into more accurate heuristics between each state and the goal, similar to AIT* and EIT*.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Informed path planning algorithms can use problem-specific knowledge in the form of heuristics to improve their performance, but selecting appropriate heuristics is difficult. This is because heuristics are most effective when they are both accurate and computationally inexpensive to evaluate, which are often conflicting characteristics. Many informed planners additionally can only use problem-specific knowledge if it is expressible as admissible heuristics, which is not always possible for all optimization objectives.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presents two almost-surely asymptotically optimal path planning algorithms that address these challenges by using asymmetric bidirectional searches that simultaneously calculate and exploit accurate, problem-specific AIT* uses an inexpensive reverse search to combine admissible a priori cost heuristics between two states into a more accurate but still admissible cost heuristic between each state and the goal. This heuristic is exploited to make AIT*'s forward search more efficient and repaired whenever the forward search detects that it uses invalid edges. In this way, information is passed between both directions of the bidirectional search, as each search informs the other.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Conclusion", "weight": 1.5} -->

EIT* builds on AIT* by additionally calculating inadmissible cost and effort heuristics with its reverse search. This additional knowledge about the computational effort to validate a path can be calculated for any optimization objective and exploited by EIT*'s forward search to order its search in a solution-oriented manner. This improves anytime performance when the cost of a path does not correlate well with the computational effort required to validate it and allows EIT*to find initial solutions quickly, even if an admissible cost heuristic is not available for an optimization objective.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The benefits of simultaneously calculating and exploiting ever more accurate heuristics through an asymmetric bidirectional search are demonstrated on twelve diverse problems in abstract, robotic, and biomedical domains. outperforms all other tested asymptotically optimal planners when optimizing obstacle clearance and performs competitively when optimizing path length. AIT*is often the second best performing asymptotically optimal planner when optimizing obstacle clearance and also performs competitively when optimizing path length.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Conclusion", "weight": 1.5} -->

OMPL implementations of AIT* and EIT* as well as the software framework for running the experiments and creating the corresponding plots will be available at
