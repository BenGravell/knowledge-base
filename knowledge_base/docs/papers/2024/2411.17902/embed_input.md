<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Nearest-Neighbourless Asymptotically Optimal Motion Planning with Fully Connected Informed Trees (FCIT*)

Topics include Motion planning, Sampling-based planning, High-dimensional planning, Anytime planning, Asymptotic optimality, FCIT*, BIT*, Single-instruction multiple-data, Hardware acceleration.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Use SIMD instructions to evaluate edge costs to every neighbor (hence eliminating expensive nearest neighbor routine) in Informed RRT*. Gives huge empirical computational end-to-end planning time.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Improving the performance of motion planning algorithms for high-degree-of-freedom robots usually requires reducing the cost or frequency of computationally expensive operations. Traditionally, and especially for asymptotically optimal sampling-based motion planners, the most expensive operations are local motion validation and querying the nearest neighbours of a configuration. Recent advances have significantly reduced the cost of motion validation by using single instruction/multiple data (SIMD) parallelism to improve solution times for satisficing motion planning problems. These advances have not yet been applied to asymptotically optimal motion planning. This paper presents Fully Connected Informed Trees (FCIT*), the first fully connected, informed, anytime almost-surely asymptotically optimal (ASAO) algorithm. FCIT* exploits the radically reduced cost of edge evaluation via SIMD parallelism to build and search fully connected graphs. This removes the need for nearest-neighbours structures, which are a dominant cost for many sampling-based motion planners, and allows it to find initial solutions faster than state-of-the-art ASAO (VAMP, OMPL) and satisficing (OMPL) algorithms on the MotionBenchMaker dataset while converging towards optimal plans in an anytime manner.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Planning low-cost motions for high- degree-of-freedom robots quickly is a fundamental area of research in robotics. These high-[[DoF]] robots are described by a continuous *configuration space*, but motion planning requires both a discrete approximation of this space and the ability to efficiently search this approximation. Graph-based planners, such as Dijkstra's algorithm and A\*, require the configuration space (i.e., search space) to be discretized a priori, and both their planning time and the quality of their solution depends on the resolution of this discretization.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sampling-based motion planners, such as Probabilistic Roadmaps, Rapidly-exploring Random Trees, and RRT-Connect, avoid this a priori discretization by incrementally sampling the search space which constructs a random geometric graph online as a discrete approximation of this search space. Anytime [[ASAO]] sampling-based motion planners, such as RRT\* and Batch Informed Trees, extend sampling-based motion planning by continually improving their sampled approximations even after finding an initial solution in order to converge probabilistically towards an optimal solution. This search in [[BIT\*]] is ordered by potential solution cost, minimizing the required number of edge evaluations (i.e., local motion validations).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

If connectivity in a planner's sampled approximation is too low, then the graph maintained by the planner almost never (i.e., with probability zero) contains a solution, but if it is too high, the graph becomes expensive to search due to the high branching factor and resulting high number of edges. As such, although incremental sampling avoids the need for a priori approximations, sampling-based [[ASAO]] planners still require a user-defined connectivity metric between samples (e.g., connection radius) for efficiency.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A significant body of work has refined the bounds necessary for almost-sure connectivity, but using these bounds has practical tradeoffs. Considering only a subset of possible edges requires fewer edge evaluations but makes *incomplete* use of the set of samples, potentially lowering the quality of the best solution that can be found without additional sampling. Implementing a partially connected [[RGG]] also requires nearest-neighbours structures to more efficiently query the incident edges of a given sample. These edge evaluations and nearest-neighbour queries traditionally dominate execution time in sampling-based motion planning.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Vector-Accelerated Motion Planning has reduced the computational cost of edge evaluations using [[SIMD]] parallelism, drastically accelerating solution times for feasible (i.e., satisficing) motion planning ^11^1 The tracing compiler used in VAMP to generate interleaved collision checking code is applicable to any system with analytic forward kinematics, although the performance gain may vary based upon the application or system in question., with RRT-Connect performing up to 500x faster than the previous state of the art.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The original [[VAMP]] work did not address [[ASAO]] motion planning. This paper shows that its radically decreased edge evaluation cost can also guide algorithmic advances on this class of problems. Specifically, we revisit the assumptions that edge evaluations are computationally expensive, and consequently that fully connected graphs are prohibitively expensive to search because of their high branching factor and the resulting large number of edges to evaluate.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

This insight leads us to [[FCIT\*]], an [[ASAO]] planning algorithm that accelerates motion planning by searching a fully connected graph. It does this efficiently by leveraging [[SIMD]] parallelism to reduce the cost of edge evaluations and using a distributed edge queue to address the high branching factor of fully connected graphs. These inexpensive edge evaluations allow [[FCIT\*]] to build an approximation with maximum connectivity (i.e., a fully connected, or complete, graph) instead of limiting connections to near a theoretical lower bound required for probabilistic guarantees. This removes the need for costly nearest-neighbours structures and improves convergence. The benefits of [[FCIT\*]] are demonstrated on the MotionBenchMaker dataset, where it finds better solutions faster than all tested non-[[VAMP]] [[ASAO]] algorithms (e.g., Fig. 1")) and solves more problems, with better solutions, than all tested [[VAMP]] [[ASAO]] algorithms (Tbl. I")).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Fully Connected Informed Trees", "weight": 1.0} -->

[[FCIT\*]] extends the [[BIT\*]] algorithm by leveraging the hardware-accelerated parallelized approach to edge validation of [[VAMP]] and revisiting the assumption that a high branching factor and the high cost of edge evaluation makes fully connected graphs prohibitively expensive to construct and search. It builds and searches a fully connected approximation of the continuous search space, as opposed to relying on a sparsely connected approximation built using nearest-neighbours structures as in [[BIT\*]]. Building a fully connected approximation makes complete use of all placed samples, potentially containing a higher quality solution than could be found in an approximation with connectivity near a theoretical lower bound.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Fully Connected Informed Trees", "weight": 1.0} -->

Constructing and searching a fully connected graph also removes the need to maintain expensive nearest-neighbours structures by instead considering all possible edges between sampled states. These edges *may* all be evaluated in the limit, but in practice many will not be because they exist in disconnected components, or belong to a more expensive path than the current best solution. [[FCIT\*]]'s search is ordered by potential solution quality (Alg. 1") Alg. 1")) as in [[BIT\*]]. Unlike [[BIT\*]], it distributes its ordered queue of unprocessed (i.e., open) edges across a set of local queues stored by each vertex (Alg. 1") Alg. 1")). Only the most promising edges from each local queue are added to the global queue and sorted (Alg. 1") Alg. 1")), resulting in a more efficient search. Pseudocode for [[FCIT\*]] is provided in Algs. 1") and 2").

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Notation and Preliminaries", "weight": 1.0} -->

We store the search as a tree, $T = {(V,E)}$, comprising a set of vertices from the sampled states, $V \subseteq X_{\text{smpl}}$, and a set of edges, $E \subseteq {V \times V}$. Each edge connects two states, ${x_{p},x_{c}} \in X_{\text{smpl}}$, which we refer to as the edge's parent and child, respectively.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Notation and Preliminaries", "weight": 1.0} -->

The planner also tracks the set of invalidated edges, denoted by $E_{\text{invalid}} \subseteq {V \times X_{\text{smpl}}}$, and maintains a queue of open edges denoted as $Q_{\text{open}} \subseteq {V \times X_{\text{smpl}}}$. Each vertex, $x \in V$, has an associated local outgoing edge queue stored in a lookup table, $Q_{\text{local}}{(x)}$, such that ${Q_{\text{local}}{(x)}} ≔ \left. \{{({{x,y} \in X_{\text{smpl}}})} \middle| {y \neq x}\} \right.$. The functions $p{(x)}$ and $g_{T}{(x)}$ respectively calculate the parent and cost-to-come from the start through the tree, $T$, for a state $x \in X_{\text{smpl}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Notation and Preliminaries", "weight": 1.0} -->

These functions return infinity if the state is not in the tree, i.e., $x \notin V$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Notation and Preliminaries", "weight": 1.0} -->

Following the formulation in [[BIT\*]], the function $c:{{X \times X}\rightarrow{\lbrack 0,\infty)}}$ represents the computed edge cost between two states. The function $\hat{c}:{{X \times X}\rightarrow{\lbrack 0,\infty)}}$ is an admissible estimate of this edge cost, where ${{{\forall x},y} \in X},{{\hat{c}{(x,y)}} \leq {c{(x,y)}}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Notation and Preliminaries", "weight": 1.0} -->

The function $\hat{h}:{X\rightarrow{\lbrack 0,\infty)}}$ represents the estimated cost-to-go from the state $x$ to the goal, e.g., ${\hat{h}{(x)}} = {\min_{x_{g} \in X_{g}}{({\hat{c}{(x,x_{g})}})}}$. The function $\hat{f}:{{V \times X}\rightarrow{\lbrack 0,\infty)}}$ represents an admissible heuristic estimate of the cost of a solution constrained to pass through an edge given the current tree.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Notation and Preliminaries", "weight": 1.0} -->

Let $A$ and $B$ be two sets. The notation $A\overset{+}{\leftarrow}B$ is shorthand for the operation $A\leftarrow{A \cup B}$, and $A\overset{-}{\leftarrow}B$ is shorthand for the operation $A\leftarrow{A \smallsetminus B}$. The number of states sampled in each batch is denoted by $n$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Local Edge Queue", "weight": 1.0} -->

[[FCIT\*]] maintains a sorted open queue of edges to be expanded, $Q_{\text{open}}$, ordered by potential solution cost. This open queue has to be sorted each time a new edge is added to it. As more edges are added, it becomes longer and takes more time to sort. To reduce the computational cost of this frequent sort, [[FCIT\*]] distributes the total set of open edges such that each vertex, $x \in V$, keeps its own local queue of outgoing edges, $Q_{\text{local}}{(x)}$. These local edge queues are sorted *once* each by the admissible heuristic estimate of solution cost, $\hat{f}$, through each edge. The open queue, $Q_{\text{open}}$, is then populated with the most promising edge from each vertex's local edge queue (Alg. 1") Alg. 1")).

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Local Edge Queue", "weight": 1.0} -->

The open queue is thus the ordered set of only the *best* open edge outgoing from each vertex, $Q_{\text{open}} ≔ {\{{{(x,y)} \in {V \times X_{\text{smpl}}}}\mid{{(x,y)} \leq {\operatorname{argmin}_{{(x,y)} \in {Q_{\text{local}}{(x)}}}{\{{\hat{f}{(x,y)}}\}}}}\}}$. When an edge outgoing from a vertex is removed from the open queue, it is replaced by the next best outgoing edge from that vertex's local queue that could potentially improve the current tree (Alg. 1") Alg. 1"), Alg. 2")). This ensures that the open queue always contains the most promising unevaluated outgoing edges from all the vertices in the search tree.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Local Edge Queue", "weight": 1.0} -->

Each vertex in a fully connected RGG has a number of potential outgoing edges equal to ${|X_{\text{smpl}}|} - 1$, where $| \cdot |$ is the cardinality of a set. Expanding vertices in the tree quickly inflates the total number of open edges, in the worst case increasing it to ${|X_{\text{smpl}}|}^{2}$ elements. These local queues reduce the worst case size of the open queue from ${|X_{\text{smpl}}|}^{2}$ to $|X_{\text{smpl}}|$. Expanding a new vertex only adds one new edge to the open queue to be frequently sorted, storing the other ${|X_{\text{smpl}}|} - 2$ edges in that vertex's local queue and sorting them only once.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Local Edge Queue", "weight": 1.0} -->

The frequent cost of sorting the open queue, $Q_{\text{open}}$, is thus reduced, and the one-time cost of sorting a given vertex's local queue, $Q_{\text{local}}{(x)}$, is amortized over the runtime of the planner.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B1 Nearest-Neighbours Structures", "weight": 1.0} -->

The set of outgoing edges from a given vertex is determined by the connectivity of the graph, i.e., the neighbouring vertices with which it shares edges. In contrast to traditional algorithms, which typically maintain an expensive nearest-neighbours structure, finding neighbours is trivial in a fully connected graph since the neighbours of any given vertex are every other sampled state in the graph. [[FCIT\*]] therefore iterates over all sampled points, $X_{\text{smpl}}$, when populating a vertex's local edge queue, ${Q_{\text{local}}{(x)}} ≔ \left. \{{({{x,y} \in X_{\text{smpl}}})} \middle| {y \neq x}\} \right.$, avoiding the computational cost of maintaining a nearest-neighbours structure and reducing planning time.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C Analysis", "weight": 1.0} -->

This paper uses Definition 24 in as the definition of almost-sure asymptotic optimality. Note that any sampling-based planner is almost-surely asymptotically optimal if (i) its underlying graph almost-surely contains an asymptotically optimal path, and (ii) its underlying graph-search is resolution optimal. These conditions are sufficient but not necessary.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Analysis", "weight": 1.0} -->

Since there is a non-zero probability of sampling every state in the search space, the probability that the solution found by [[FCIT\*]] will asymptotically converge to the optimum approaches one as the number of samples approaches infinity, regardless of whether the sampling used is pseudorandom or deterministic. This holds true for a fully connected graph since it trivially satisfies the lower bound on connectivity, as demonstrated by the simplified-[[PRM]] [[ASAO]] proof with an infinite r-disc graph. Since the search is performed in an informed order as in [[BIT\*]], it is also *resolution optimal*, finding the best possible solution with respect to the current approximation. [[FCIT\*]] is therefore almost surely asymptotically optimal.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-D Implementation", "weight": 1.0} -->

In practice, each vertex locally stores its set of invalid edges, similar to its local edge queue, instead of maintaining a global list. The cost-to-come function, $g_{T}{(x)}$, and parent function, $p{(x)}$, are implemented as lookups, storing and updating the values to reduce time per iteration. The open and local queues are both implemented as sorted structures.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

[[FCIT\*]] was evaluated against Open Motion Planning Library and VAMP baselines. We compared to [[OMPL]] implementations of RRT-Connect, RRT\*, BIT\*, and AIT\*, as well as VAMP implementations of RRT-Connect, RRT\*, and BIT\*. Note that the VAMP implementation of BIT\* uses the same local edge queue presented in Sec. III-B ‣ Nearest-Neighbourless Asymptotically Optimal Motion Planning with Fully Connected Informed Trees (FCIT*)"), but performs a traditional $r$-disc nearest-neighbours search rather than using a fully connected graph. The VAMP implementation of RRT-Connect is a dynamic domain balanced RRT-Connect. The reported initial solution costs and times for RRT-Connect include path smoothing with randomized shortcutting and B-spline smoothing.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments", "weight": 1.0} -->

The planners were tested on the [[MBM]] dataset, which consists of 7 difficult planning environments each containing 100 pregenerated problems. These environments cover a range of planning problems, including reaching (bookshelf tall, bookshelf small, and bookshelf thin), highly constrained reaching (box and cage), and tabletop manipulation (table pick and table under pick)^22^2One of the problems in table pick is invalid with respect to the robot simulation and is disregarded, giving these experiments 699 total problems.. table under pick Table I: Summary of all planning results. The top results in each row are for the VAMP implementation of the given planner, while the bottom results are for the OMPL implementation of that planner. The only tested planner that solves more problems than FCIT* is RRT-Connect, which is not an ASAO algorithm and cannot improve its initial solution with additional computational time. Only VAMP RRT-Connect reliably finds initial solutions faster than FCIT*. Each result indicates the percentage of problems solved in the given environment (bold), the median initial solution time across all problems on that environment, and the median initial path length across all problems on that environment.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

All experiments were run using a simulated 7-[[DoF]] Panda robotic arm. Each problem was evaluated 5 times by each planner to mitigate the effect of machine noise on the results^33^3All tests were run in Ubuntu 22.04 on a Intel i7-9750H CPU with 32GB of RAM, and the planning algorithms are implemented in C++17.. All planners use the default VAMP and [[OMPL]] samplers with different seeding for each trial. Planners were all given the same time constraints to evaluate each problem in a given environment. The time constraints per environment were 10 seconds on *box*, *table pick*, *table under pick*, *bookshelf thin*, and *bookshelf tall*; and 100 seconds on *bookshelf small* and *cage*.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

Experimental results for all problems in a given environment are shown in Figs. 1") and 2 ‣ Nearest-Neighbourless Asymptotically Optimal Motion Planning with Fully Connected Informed Trees (FCIT*)"), and are summarized in Tbl. I"). The time axis for all figures is in logarithmic scale. Results for each environment are presented separately because all the environments in the [[MBM]] dataset pose significantly different planning problems from each other. While Tbl. I") includes initial solution results for all planners across all environments, Figs. 1") and 2 ‣ Nearest-Neighbourless Asymptotically Optimal Motion Planning with Fully Connected Informed Trees (FCIT*)") show results for all problems in *cage*, *table pick*, and *bookshelf small*. These results were chosen because they are the most indicative of relative qualitative planner performance. Fig. 3 ‣ Nearest-Neighbourless Asymptotically Optimal Motion Planning with Fully Connected Informed Trees (FCIT*)") shows convergence results for 100 trials of each VAMP planner on a single problem from both the *cage* and *bookshelf small* environments.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

This figure omits [[OMPL]] planner convergence results because [[FCIT\*]] finds initial solutions significantly faster and of higher quality than *all* ASAO [[OMPL]] planners (Fig. 1"), 2 ‣ Nearest-Neighbourless Asymptotically Optimal Motion Planning with Fully Connected Informed Trees (FCIT*)")a, and 2 ‣ Nearest-Neighbourless Asymptotically Optimal Motion Planning with Fully Connected Informed Trees (FCIT*)")c).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Discussion", "weight": 1.5} -->

[[FCIT\*]] revisits fundamental assumptions about [[ASAO]] planning in light of the computationally inexpensive local motion validation introduced by [[VAMP]]. Planners traditionally seek to reduce the number of edges in their approximation by setting connectivity near a theoretical lower bound. This requires maintaining a computationally expensive nearest-neighbours structure. Moreover, this limits the connectivity of the resulting graph, preventing solutions from being found without additional sampling. [[FCIT\*]] is able to avoid this lower bound because of the reduced cost of edge evaluation, instead searching a fully connected approximation. This removes the need for maintaining a nearest-neighbours structure, instead considering all possible edges in the graph in an informed order. It uses this fully connected [[RGG]] approximation to find better solutions with fewer required samples. [[FCIT\*]] outperforms all other tested ASAO planners, both VAMP and [[OMPL]], on the difficult *cage* environment (Fig. 1")).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Discussion", "weight": 1.5} -->

The only tested planners that finds initial solutions faster than [[FCIT\*]] in this environment are the VAMP and [[OMPL]] implementations of RRT-Connect, which do not converge towards an optimal solution given additional planning time. [[FCIT\*]] demonstrates better performance than other tested VAMP ASAO planners. [[FCIT\*]] consistently outperforms the VAMP BIT\* planner in all environments, finding better initial solutions in less time (Fig. 2 ‣ Nearest-Neighbourless Asymptotically Optimal Motion Planning with Fully Connected Informed Trees (FCIT*)")) by fully exploiting the samples. VAMP RRT\* shows similar initial solution times to [[FCIT\*]] on the simpler environments, but consistently yields lower quality solutions, and performs much worse than [[FCIT\*]] in the difficult *cage* environment, only solving 72% of problems (Tbl. I")). [[FCIT\*]] solves more problems than any other tested planner barring the two implementations of RRT-Connect, only occasionally failing to solve one difficult problem in the *bookshelf small* environment.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Discussion", "weight": 1.5} -->

It also outperforms [[OMPL]] RRT-Connect on all environments other than *cage*, finding faster initial solutions with additional ASAO guarantees. The initial solution time for [[FCIT\*]] is consistently within an order of magnitude of that of [[VAMP]] RRT-Connect on all environments except for the difficult *cage* environment (Tbl. I")). This environment seems well suited for bidirectional planners, as also evidenced by the performance of AIT\* relative to the other [[OMPL]] [[ASAO]] planners. [[FCIT\*]] outperforms all tested [[OMPL]] [[ASAO]] planners on all environments, finding higher quality solutions in less time. All tested [[OMPL]] planners show a delay before finding initial solutions (Fig. 2 ‣ Nearest-Neighbourless Asymptotically Optimal Motion Planning with Fully Connected Informed Trees (FCIT*)")). This can be attributed to overhead in [[OMPL]], even though only planning time is reported for these planners.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Discussion", "weight": 1.5} -->

We believe that the introduction of VAMP poses an open question of how to best leverage trivialized edge evaluation, since so much existing planning research has focused on avoiding these operations on the assumption that they are computationally expensive. [[FCIT\*]] is an initial answer to this question, but it is clear there is further research to be done on the topic. We are particularly interested in finding ways to apply the benefits of bidirectional search to [[FCIT\*]], potentially closing the gap to RRT-Connect's performance on difficult environments.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Motion planning is an ongoing and important area of research in robotics. This paper leverages VAMP to reduce the cost of edge evaluation and presents [[FCIT\*]], the first fully connected, informed, anytime almost-surely asymptotically optimal planner. [[FCIT\*]] leverages inexpensive edge evaluations to build and search a fully connected graph instead of limiting connections to near a theoretical lower bound. This allows it to fully exploit all samples in a given approximation without requiring nearest-neighbours structures, instead considering every possible edge in the approximation and yielding better solutions in less time and with fewer samples placed.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusions", "weight": 1.0} -->

The benefits of leveraging VAMP to search a fully connected graph are demonstrated on hundreds of problems across seven different planning environments. [[FCIT\*]] demonstrates performance comparable to that of the fastest planner, VAMP's RRT-Connect, on almost all environments tested and with additional guarantees. It outperforms all other tested VAMP and [[OMPL]] ASAO planners, finding initial solutions faster, of higher quality, and more consistently, and outperforms [[OMPL]]'s RRT-Connect on all but the most difficult class of problems tested, all while maintaining ASAO guarantees.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Information on the implementation of FCIT\* is available at
