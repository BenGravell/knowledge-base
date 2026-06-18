<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

AORRTC: Almost-Surely Asymptotically Optimal Planning with RRT-Connect

Topics include Motion planning, Sampling-based planning, Asymptotic optimality, Anytime planning, Bidirectional search, Rapidly-exploring random tree connect, Single-instruction multiple-data, High-dimensional planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Applies the AO-x meta-algorithm to RRT-Connect, inheriting its fast initial solution times while adding almost-sure asymptotic optimality. With SIMD acceleration, AORRTC solves difficult high-DoF problems (Panda, Fetch robots) in milliseconds where other almost-surely asymptotically optimal planners failed to find solutions even with seconds of planning time.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finding high-quality solutions quickly is an important objective in motion planning. This is especially true for high-degree-of-freedom robots. Satisficing planners have traditionally found feasible solutions quickly but provide no guarantees on their optimality, while almost-surely asymptotically optimal (a.s.a.o.) planners have probabilistic guarantees on their convergence towards an optimal solution but are more computationally expensive. This paper uses the AO-x meta-algorithm to extend the satisficing RRT-Connect planner to optimal planning. The resulting Asymptotically Optimal RRT-Connect (AORRTC) finds initial solutions in similar times as RRT-Connect and uses any additional planning time to converge towards the optimal solution in an anytime manner. It is proven to be probabilistically complete and a.s.a.o. AORRTC was tested with the Panda (7 DoF) and Fetch (8 DoF) robotic arms on the MotionBenchMaker dataset. These experiments show that AORRTC finds initial solutions as fast as RRT-Connect and faster than the tested state-of-the-art a.s.a.o.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

algorithms while converging to better solutions faster. AORRTC finds solutions to difficult high-DoF planning problems in milliseconds where the other a.s.a.o. planners could not consistently find solutions in seconds. This performance was demonstrated both with and without single instruction/multiple data (SIMD) acceleration.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning seeks to quickly find high-quality solutions to a given problem, especially when planning for high degree-of-freedom (DoF) robots or in real time. Motion planning algorithms search a discrete approximation of the robot's continuous *configuration space* (i.e., search space).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning algorithms approximate the search space in different ways. Graph-based planners, such as Dijkstra's algorithm and A\*, require *a priori* discretization of the search space. High-resolution approximations generally contain high quality solutions but are computationally expensive to search, while low-resolution approximations are cheaper to search but may only contain a low quality solution, or no solution at all. Trajectory optimization methods, such as CHOMP and TrajOpt, are less dependent on their approximation but only provide local guarantees and may not find a solution when getting stuck in local minima on difficult planning problems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sampling-based planners, such as Probabilistic Roadmaps (PRM) and Rapidly-exploring Random Trees (RRT), avoid the need for an *a priori* approximation by incrementally sampling the search space. This allows them to search an increasingly accurate approximation of the underlying continuous space and has made them a popular and effective choice for high-dimensional problems. Sampling-based planners provide probabilistic guarantees. Algorithms are said to be probabilistically complete if their probability of finding a solution goes to one as their number of samples approaches infinity, if a solution exists. They are said to be a.s.a.o. if they have probability one of asymptotically converging towards the optimal solution with an infinite number of samples.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

RRT-Connect extends RRT to interleave searching for a feasible path from both the start and goal. This bidirectional satisficing planner is widely used because of its simple implementation and fast initial solution time. RRT-Connect provides no solution quality guarantees and does not improve its solution with more samples (i.e., it is not a.s.a.o.). Path smoothing or simplification can improve the cost of the often low-quality solutions found by RRT-Connect (Fig.˜1a) but provide no global quality guarantees.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Anytime a.s.a.o. planners, such as RRT\* and Batch Informed Trees (BIT\*), are probabilistically guaranteed to find a solution and then converge to the optimum. These algorithms use additional planning time to improve their current solution, but the overhead required to guarantee almost-sure asymptotic optimality can increase the time required to find an initial solution. Research has focused on how to improve initial solution times and the rate of convergence towards the optimum.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The AO-*x* meta-algorithm poses an alternative framing of the optimal planning problem. Instead of requiring planners to optimize the cost of a feasible path in configuration space, AO-*x* asks planners to find a feasible path through a search space that has been augmented to include an extra dimension. This extra dimension represents the cost to reach each configuration. Calling a satisficing planner on a *sequence* of these augmented search spaces with appropriately decreasing limits in the cost dimension has been proven to be a.s.a.o..

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

AORRTC^11^1Pronounced aortic ($\overline{\text{a}}$-\'$\overset{˙}{\text{o}}$r-tik). applies the ideas of AO-*x* and RRT-Connect to perform a bidirectional search in a cost-augmented search space. This finds initial solutions as fast as RRT-Connect and converges towards high-quality solutions orders of magnitudes faster than other a.s.a.o. algorithms. The performance of AORRTC is tested with both Open Motion Planning Library (OMPL) and Vector-Accelerated Motion Planning (VAMP) implementations. These demonstrate the effectiveness of the approach with and without SIMD acceleration and specifically show that AORRTC can converge close to the optimum of high-dimensional planning problems in microseconds with SIMD acceleration.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Both implementations of AORRTC were evaluated on the 7 DoF Panda and 8 DoF Fetch planning problems from the MotionBenchMaker (MBM) dataset. AORRTC found initial solutions as fast as RRT-Connect and faster than all tested a.s.a.o. planners while consistently solving more problems (Figs.˜1 and 2). It also converged to better solutions faster than the tested a.s.a.o. planners. These relative performances held for both OMPL and VAMP implementations of AORRTC (Sec.˜V).

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Almost-Surely Asymptotically Optimal Planning", "weight": 1.0} -->

Anytime a.s.a.o. planners use additional planning time to improve their approximation of the search space and find better solutions. These planners asymptotically converge to the optimal solution with probability one (i.e., almost surely).

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Almost-Surely Asymptotically Optimal Planning", "weight": 1.0} -->

Nearest neighbour lookups and edge evaluations are major computational costs for sampling-based motion planning. These computationally expensive operations are often performed more frequently in a.s.a.o. planners to guarantee almost-sure asymptotic optimality which can make them slower to find initial solutions than satisficing planners.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Almost-Surely Asymptotically Optimal Planning", "weight": 1.0} -->

Anytime a.s.a.o. planners, such as RRT\* and BIT\*, iteratively sample the search space to improve both their approximation and solution. RRT\* incrementally rewires new vertices to reduce path costs while BIT\* searches a batch of samples in an order informed by heuristics to consider states in order of potential solution quality. These planners require computational effort to maintain their a.s.a.o. guarantees and significant work has focused on improving their performance.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Almost-Surely Asymptotically Optimal Planning", "weight": 1.0} -->

Several RRT\* extensions have improved the planner's convergence to an optimal solution. RRT^\#^ builds a search tree that contains information about the best cost-to-come to all vertices that could possibly belong to an optimal solution instead of only locally rewiring vertices. RRT\*-Smart and Informed RRT\* instead improve the planner's performance by leveraging problem specific information. These planners use information from prior search efforts to generate samples more intelligently in order to reduce planning time when improving a solution but this informed sampling cannot help find an initial solution.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Almost-Surely Asymptotically Optimal Planning", "weight": 1.0} -->

Fully Connected Informed Trees (FCIT\*) leverages the reduced cost of edge evaluations enabled by VAMP's SIMD parallelism to search a fully connected graph. This fully exploits the approximation of the search space and avoids the need to maintain costly nearest neighbour structures. FCIT\* finds high-quality solutions faster than non SIMD-accelerated planners, including RRT-Connect, but cannot find solutions as fast as SIMD-accelerated RRT-Connect.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Almost-Surely Asymptotically Optimal Planning", "weight": 1.0} -->

AORRTC is a.s.a.o. like RRT\* and BIT\* and improves the quality of its found solution given additional planning time, but finds initial solutions as fast as RRT-Connect. Unlike RRT\* or RRT^\#^, AORRTC does not have to rewire its tree to maintain its a.s.a.o. guarantees, instead randomly sampling lower cost bounds when adding a new vertex to potentially connect it to a lower-cost parent. AORRTC leverages informed sampling as is done in Informed RRT\*, but restarts its search after finding a solution rather than continuing to plan with the same tree.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Bidirectional Planning", "weight": 1.0} -->

Bidirectional sampling-based planners, such as RRT-Connect, explore the search space by extending a tree from both the start and goal vertices and trying to connect these trees. RRT-Connect finds initial solutions significantly faster than other planning algorithms on most real-world manipulation problems but offers no guarantees on solution quality and often finds low quality solutions.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Bidirectional Planning", "weight": 1.0} -->

Some bidirectional a.s.a.o. planners, such as Bidirectional RRT\* (B-RRT\*) and RRT\*-Connect, extend the fast bidirectional search of RRT-Connect with the a.s.a.o. guarantees of RRT\*. These algorithms require RRT\*-style rewiring throughout the entire search in order to guarantee almost-surely asymptotic optimality. This increase in computational cost increases the time required to find an initial solution relative to RRT-Connect.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Bidirectional Planning", "weight": 1.0} -->

Other bidirectional a.s.a.o. planners, such as Adaptively Informed Trees (AIT\*) and Effort Informed Trees (EIT\*)\*, instead use an asymmetric bidirectional search where information is shared between the reverse and forward searches. The lightweight reverse search calculates heuristics from the current distribution of samples to inform the computationally expensive forward search. The forward search efficiently finds a solution and passes collision checking information to the reverse search to update the heuristics. This reduces edge evaluation costs but its utility depends on the cost of edge evaluations relative to nearest neighbour lookups.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Bidirectional Planning", "weight": 1.0} -->

AORRTC performs an a.s.a.o. bidirectional search similar to B-RRT\* and RRT\*-Connect but does not require RRT\*-style rewiring to maintain its a.s.a.o. guarantees. Unlike AIT\* and EIT\*, AORRTC grows both trees and tries to connect them instead of using the reverse search to calculate heuristics.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-C Augmented Search Spaces", "weight": 1.0} -->

Augmented search spaces have been used in other planners to improve planning. Time-based RRT (TB-RRT) augments the configuration space with a time dimension for planning with dynamic obstacles or goals. This time-augmented space transforms dynamic obstacles in the original problem into static obstacles in the time-augmented search space and simplifies planning in dynamic environments but offers no guarantees for solution time or quality.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-C Augmented Search Spaces", "weight": 1.0} -->

Other planners, such as Windowed Heirarchical Cooperative A\* (WHCA\*) and Safe Interval Path Planning (SIPP), abstract a time-augmented search space to reduce planning time. WHCA\* plans in the time-augmented search space up to a user-specified threshold and then excludes the time dimension and any dynamic obstacles for later times. SIPP discretizes the continuous time dimension into discrete *safe intervals*, which describe a duration during which a configuration is considered valid, and plans in this simplified state-*safe interval* augmented search space. These search space abstractions help improve planner performance, but offer no guarantees on solution quality.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-C Augmented Search Spaces", "weight": 1.0} -->

Some bidirectional planners, such as Space-Time RRT\* (ST-RRT\*) and Safe-Interval RRT (SI-RRT), extend RRT-Connect to search in a time-augmented search space. ST-RRT\* searches an incrementally increasing range in the time dimension to quickly find initial solutions in unbounded time spaces but requires RRT\*-style rewiring to maintain its guarantees on solution quality. SI-RRT instead searches in a simplified state-*safe interval* augmented search space to quickly find initial solutions in high-dimensional dynamic environments but offers no guarantees on solution quality.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-C Augmented Search Spaces", "weight": 1.0} -->

The meta-algorithm AO-*x* extends satisficing kinodynamic planners to include a.s.a.o. guarantees through the use of a cost-augmented search space. This search space consists of the $n$ dimensions of the configuration space and a $\left( {n + 1} \right)^{\text{th}}$ dimension that describes the cost to reach each state. Satisficing planners can almost-surely converge asymptotically to the optimal solution by finding a series of feasible plans in this augmented search space when the cost function and the dynamics of the robot are Lipschitz continuous. This meta-algorithm has been applied to the Expansive Space Tree (EST) and RRT.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-C Augmented Search Spaces", "weight": 1.0} -->

AORRTC searches in an augmented space, like TB-RRT and ST-RRT\*, but this space is augmented with a cost dimension instead of a time dimension. Unlike WHCA\*, SIPP, and SI-RRT, AORRTC does not search an abstraction of its augmented search space.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

5 σbest ← σ0; cmin ← c (σ0); ϵ ← ϵinit; 8 σi←simplify(rrt-connect(cmin)); 26 crand ∼ U ((ĝTa (xrand),cmax − ĥTa (xrand))); 28 xnear←nearest(Ta,xrand,crand); 29 xnew←steer(xrand,xnear); 32 cnew←extend(Ta,xnear,xnew); 48 crand ∼ U ((ĝT (xnew),cnew)); 49 xnear←nearest(T,xnew,crand); 51 until x ≡ x or not validate(x,x); 53 $E\overset{+}{\leftarrow}{(x_{\text{p}},x_{\text{new}})}$; 54 $V\overset{+}{\leftarrow}{(x_{\text{new}},c_{\text{new}})}$; 61

<!-- chunk {"id": "body-0029", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

xnear←nearest(Tb,x,cmax − c); 62 xnew←steer(x,xnear); 65 extend(Tb,xnear,xnew); 68 until x ≡ x or not validate(x,x);

<!-- chunk {"id": "body-0030", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

AORRTC applies the ideas of AO-*x* and RRT-Connect to create an anytime a.s.a.o. planner that finds initial solutions as fast as RRT-Connect and asymptotically converges towards the optimal solution with additional planning time in an anytime manner. Pseudocode for AORRTC is presented in Alg.˜1 with changes to RRT-Connect (Algs. 1 to 1) marked in red.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

AORRTC runs RRT-Connect iteratively on a series of problems in the augmented search space with an open upper-bound on solution cost. This bound is first determined by RRT-Connnect's initial solution after path simplification techniques (*e.g.*, randomized shortcutting and B-spline smoothing ) have been applied (Alg.˜1). AORRTC then uses this bound to pose a new planning problem where the cost-dimension of the augmented space is limited by the cost of the current best solution (Alg.˜1). This bound is lowered each time a better solution is found (Algs. 1 to 1).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

AORRTC grows trees from the start and goal vertices in the augmented search space where each vertex consists of a configuration and its cost-to-come in the respective tree (Algs.˜1 and 1). The current tree is grown towards a random sample from the augmented search space consisting of a random configuration (Alg.˜1) and a randomly sampled cost bound (Alg.˜1). This sampled cost bound is the upper limit on cost for a connection to the sample and limits connections to only those that could contribute to a solution that is higher-quality than the current best solution. After a vertex is connected to a tree its sampled cost bound is randomly resampled from a lower range to see if the vertex can be easily connected with lower cost (Algs. 1 to 1).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

The underlying RRT-Connect search finds incrementally higher-quality solutions by forcing samples to only attempt connections that would satisfy their randomly sampled cost bound (Alg.˜1). Once a solution has been found it is simplified and a new upper bound on solution cost is determined. The search is then restarted with this tighter cost bound. This restricts each subsequent search to paths with higher quality than the current solution and allows the planner to almost-surely asymptotically converge to an optimal solution even if its underlying search is not a.s.a.o.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

llllXXXlXX \CodeBefore[cols=3-10,restart] \Body Planner bookshelf small bookshelf tall bookshelf thin table pick table under pick box cage

<!-- chunk {"id": "body-0035", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

We denote the configuration space by X ⊆ ℝn and the invalid and valid subsets as Xinvalid ⊆ X and Xvalid ≔ closure (X∖Xinvalid), respectively. Let x ∈ X be a configuration, xstart ∈ Xvalid be the starting configuration, and xgoal ∈ Xvalid be the goal configuration. Let c ∈ ℝ+ be the cost of an edge or set of consecutive edges (i.e., a path) in configuration space. We store the searches as trees, T ≔ (V,E), each comprising a set of vertices, V ⊆ ℝn + 1, and a set of edges, E ⊆ V × V. Each edge, e ≔ (vp,vc) ∈ V × V, connects two vertices which we refer to as the edge’s parent and child, respectively. We denote a solution as the sequence of edges, σ = (xs,v0), (v0,v1), (v1,v2), …, (vq,xg), where (vi,vj) ∈ E.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

The function c: X × X → [0, ∞) computes the edge cost between two configurations or, with a slight abuse of notation, the cost of a given solution. The function ĉ: X × X → [0, ∞) is an admissible estimate of the edge cost, i.e., ∀xp, xc ∈ X, ĉ (xp,xc) ≤ c (xp,xc). The function gT: VT → [0, ∞) represents the cost-to-come through a tree, T, from the root to the given vertex, v. The function ĝT: X → [0, ∞) represents an admissible estimate of this cost-to-come, i.e., ∀x ∈ X, ĝT (x) ≤ gT (x). The function ĥT: X → [0, ∞) represents the estimated cost-to-go from the configuration, x, to the goal of the tree, T. Note that the goal of one tree, Ta, is the root of the other, Tb, i.e., ∀x ∈ X, ĥTa (x) ≡ ĝTb (x). Let A and B be two sets.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

The notation U (A) is shorthand for drawing a sample uniformly from a set, A. The notation $A\overset{+}{\leftarrow}B$ is shorthand for the set compounding operation, A ← A ∪ B. III-B Augmented Search Space
AORRTC searches an augmented (n+1)-dimensional search space where the first n dimensions are the configuration space and the (n+1)th dimension is the cost to reach that configuration. New configurations are sampled uniformly from configuration space (Alg.˜1). The upper bound on the cost of a new state, crand, is randomly sampled uniformly between the minimum and maximum possible cost of a solution passing through the state such that the state is feasible and useful, i.e., ĝ (x) + ĥ (x) ≤ crand &lt; cmax (Alg.˜1). This cost is an upper bound for a connection to the configuration to be considered valid in the augmented space and the true cost of a configuration will be calculated from its parent configuration. The nearest neighbour in the augmented search space is defined as the state closest in both configuration and cost (Alg.˜1).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

This distance function means samples with high cost bounds are closest to vertices with high costs-to-come. This results in short edges that make valid connections more likely and facilitates expansion into unexplored space but can inflate the cost of reaching the new configuration. To address this, the cost of a newly added vertex is resampled to search for lower cost neighbours after it is added to the tree (Algs. 1 to 1). This resampling continues until an invalid edge or the same parent is found. The cost of a new vertex, v, in the tree is the cost-to-come through its parent vertex, vp, i.e., gT (v) = gT (vp) + c (vp,v).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

The AO-x meta-algorithm has been proven by to be a.s.a.o. when the cost function and robot dynamics are Lipschitz continuous and the planner used on the augmented search space is probabilistically complete. AORRTC is therefore a.s.a.o. if the version of RRT-Connect it uses is probabilistically complete. The original RRT-Connect is probabilistically complete and the added cost resampling (Algs. 1 to 1) in AORRTC does not change the vertices in the trees but only the cost of their connections. This maintains the probabilistic completeness of RRT-Connect and AORRTC is therefore probabilistically complete and a.s.a.o. with respect to the original planning problem. III-D Anytime RRT-Connects
A naïve approach to making RRT-Connect an anytime a.s.a.o. planner would be to run it iteratively with informed sampling to try and find higher-quality solutions. This bidirectional extension of Anytime RRTs converges to a reasonable solution on many problems but is provably not a.s.a.o..

<!-- chunk {"id": "body-0040", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

The performance of this Anytime RRT-Connects is presented in Fig.˜3, even though it provides no formal optimality guarantees despite its practical performance. Alg.˜1 describes a conceptual version of AORRTC that leaves room for a number of practical improvements. AORRTC should sample configurations using informed sampling when available and should use a balanced bidirectional search. Nearest neighbour structures and lookups should be used where appropriate.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

OMPL and VAMP implementations of AORRTC were evaluated against OMPL implementations of RRT-Connect, RRT*, BIT*, and AIT* and VAMP implementations of RRT-Connect, RRT*, BIT*, and FCIT*. We also show results for a VAMP implementation of Anytime RRT-Connects (Sec.˜III-E) in Fig.˜3. The reported solution costs and times for AORRTC include the computational costs of randomized shortcutting and B-spline smoothing. The reported solution costs and times for the implementations of RRT-Connect do not include simplification but these can be inferred from the initial solution time and cost of AORRTC since this is a single simplified RRT-Connect search. Both RRT-Connect and AORRTC used a balanced bidirectional search. The planners were tested on the MBM dataset, which contains 7 planning environments for different robots where each environment has 100 different planning problems222Some of the problems are invalid for the Panda and Fetch robots resulting in 699 and 679 total problems, respectively..

<!-- chunk {"id": "body-0042", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

These environments cover a range of manipulation planning scenarios, including reaching (bookshelf tall, bookshelf small, and bookshelf thin), constrained reaching (box and cage), and tabletop manipulation (table pick and table under pick). The OMPL and VAMP planners were run on the 7 DoF Panda robotic arm MBM problems while only the VAMP planners and OMPL versions of AORRTC and RRT-Connect were run on the harder 8 DoF Fetch MBM problems. The OMPL planners were not tested on the harder Fetch problems because they were not able to reliably find solutions in the available planning time. All tests were run in Ubuntu 22.04 on a Intel i7-9750H CPU with 32GB of RAM, and the planning algorithms are implemented in C++17. All planners use the default VAMP and OMPL samplers with different seeding for each trial. The OMPL planners use VAMP’s collision checking backend. The planners were given 10 seconds to evaluate each problem. The time and cost axes for all figures are in logarithmic scale. The success rate for all problems in a given environment are shown in Figs.˜1 and 2.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

Fig.˜3 shows the success rate and median solution cost over time for 100 trials of each planner on a single problem for the Panda and Fetch robotic arms. Fig.˜4 shows the success rate and median time to converge to a near-optimal solution for 5 trials of each planner on 100 problems from the cage, bookshelf small, and table pick environments for the Panda robotic arm. These results compare the number of problems where a solution was found that falls within a suboptimality factor, ε, of an empirical estimate of the optimum cost, $\hat{c^{\ast}}$, as well as the median time to find a solution that satisfies that bound. The empirical optimum for a given problem was taken as the minimum cost found across more than 700 trials during development and experiments. The VAMP implementation of AORRTC outperforms all other tested a.s.a.o. planners and finds initial solutions in significantly less time on all environments (Sec.˜III). None of the tested a.s.a.o. planners converge to higher quality solutions than those found by VAMP AORRTC (Fig.˜3).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

OMPL AORRTC outperformed all OMPL a.s.a.o. and some VAMP a.s.a.o. planners but FCIT* was able to find solutions faster on some environments (Fig.˜2). This is because of the performance improvements of VAMP’s SIMD-accelerated edge evaluation. The only planner with similar performance to the VAMP and OMPL implementations of AORRTC were the VAMP and OMPL implementations of RRT-Connect, respectively. RRT-Connect found initial solutions microseconds faster than AORRTC but cannot improve this solution given additional planning time. This is expected because the RRT-Connect results do not include the computational cost of path simplification while the initial result found by AORRTC is equivalent to a simplified solution found by RRT-Connect. OMPL and VAMP AORRTC were the only tested a.s.a.o. planners that found solutions to all Panda problems. VAMP AORRTC was also the only tested a.s.a.o. planner that found solutions to all Fetch problems. The other tested VAMP a.s.a.o. planners struggled to find solutions on the difficult Fetch problems.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

VAMP RRT-Connect also found solutions to all tested problems, but is not a.s.a.o. Although OMPL AORRTC was not able to find solutions to all the Fetch problems in the allowed time, it found solutions to significantly more Fetch problems and found initial solutions to these problems in less time than all tested VAMP planners other than AORRTC and RRT-Connect. OMPL and VAMP AORRTC converged to better solutions in significantly less time than all other tested planners (Fig.˜4). Both implementations of AORRTC reliably converged to solutions that were close to the empirical optimum within milliseconds, even on the difficult cage problems. Both implementations of AORRTC also converged to these solutions in less time than any other planner. VAMP AORRTC finds a given suboptimal solution faster than OMPL AORRTC as a result of VAMP’s SIMD-accelerated edge evaluation. AORRTC uses the ideas of the AO-x meta-algorithm and RRT-Connect to design a bidirectional anytime a.s.a.o. algorithm that quickly finds initial solutions and then converges towards the optimal solution.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

AORRTC searches an (n+1)-dimensional augmented search space, where the first n dimensions are the configuration space and the (n+1)th dimension is its cost-to-come. It calls a satisficing planner on a sequence of these augmented search spaces with the cost dimension bounded by the current best solution cost to iteratively find higher-quality solutions. This has been proven to be a.s.a.o.. AORRTC finds initial solutions on the same order of magnitude as RRT-Connect, which is faster than other a.s.a.o. planning algorithms. It then uses the remaining planning time to find higher quality solutions than other tested a.s.a.o. algorithms in an anytime manner. This is demonstrated with and without SIMD-acceleration on hundreds of problems across seven different planning environments for both the 7 DoF Panda and 8 DoF Fetch robotic arms. AORRTC represents a different approach to a.s.a.o. planning. The majority of previous a.s.a.o.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Asymptotically Optimal RRT-Connect", "weight": 1.0} -->

algorithms approximated the continuously valued search space with increasing accuracy in order to find better solutions with additional planning time and almost-surely asymptotically converge towards the optimum. AORRTC instead quickly samples from the set of feasible solutions that could provide a better solution than the current one. This avoids the computational cost of maintaining high-resolution approximations of the search space and allows AORRTC to find initial solutions quickly and then rapidly converge towards the optimum. AORRTC shows the promise of this alternative approach to a.s.a.o. planning and we expect that future work will explore its full implications. Future work will investigate ways to further accelerate the convergence of AORRTC. This could include inflating the cost bound to allow for worse intermediate solutions that may be within the cost bound after simplification. Other work will explore the performance of different distance functions and apply AORRTC to optimize cost functions other than path length, including multivariate cost functions. Information on the implementation of AORRTC is available at
