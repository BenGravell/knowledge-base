<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Informed sampling-based planning algorithms exploit problem knowledge for better search performance. This knowledge is often expressed as heuristic estimates of solution cost and used to order the search. The practical improvement of this informed search depends on the accuracy of the heuristic. Selecting an appropriate heuristic is difficult. Heuristics applicable to an entire problem domain are often simple to define and inexpensive to evaluate but may not be beneficial for a specific problem instance. Heuristics specific to a problem instance are often difficult to define or expensive to evaluate but can make the search itself trivial. This paper presents Adaptively Informed Trees (AIT*), an almost-surely asymptotically optimal sampling-based planner based on BIT*. AIT* adapts its search to each problem instance by using an asymmetric bidirectional search to simultaneously estimate and exploit a problem-specific heuristic. This allows it to quickly find initial solutions and converge towards the optimum. AIT* solves the tested problems as fast as RRT-Connect while also converging towards the optimum.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Path planning is the problem of finding a continuous sequence of valid states between a start and goal specification. Sampling-based planners, such as Probabilistic Roadmaps (PRM), approximate the state space by sampling discrete states and connecting them with edges. The resulting structure can then be processed by graph-search algorithms to find a sequence of states that connects the start to the goal.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Informed graph-search algorithms, such as A\*, use knowledge about a problem domain to increase their efficiency. This knowledge is often captured in the form of a *heuristic function*, $\hat{h}$, which estimates cost-to-go, i.e., the cost to go from any state in the state space to the goal.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The properties of this heuristic directly affect the performance of the search algorithms. An *admissible* heuristic never overestimates the actual cost-to-go. A *consistent* heuristic satisfies a triangle-inequality, such that for any two states, $\mathbf{x}_{i},\mathbf{x}_{j}$, it satisfies ${\hat{h}\left( \mathbf{x}_{i} \right)} \leq {{p{(\mathbf{x}_{i},\mathbf{x}_{j})}} + {\hat{h}\left( \mathbf{x}_{j} \right)}}$, where $p{(\mathbf{x}_{i},\mathbf{x}_{j})}$ is the best cost of any path from $\mathbf{x}_{i}$ to $\mathbf{x}_{j}$. Note that by definition all consistent heuristics are also admissible.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A\* is guaranteed to find the optimal solution when provided with an admissible heuristic. If the provided heuristic is also consistent, then A\* expands the minimum number of states of any informed graph-search algorithm using that heuristic (i.e., it is *optimally efficient* ).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Improving the accuracy of a heuristic directly improves the performance of informed search algorithms, and the search becomes trivial when a perfect heuristic is available.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Designing and selecting effective heuristics is difficult for many problem domains. This is because heuristics are most effective when they are both accurate and computationally inexpensive to evaluate. Heuristics that are applicable to an entire problem domain are often inexpensive to evaluate but may not be accurate for a specific problem instance. Accurate heuristics can be designed for a specific problem instance during the search, but this can be computationally expensive and may diminish the overall search performance.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Computational cost directly influences the real-world performance of planning algorithms. Sampling-based planners contain a number of computationally expensive basic operations, including state expansions and edge evaluations. State expansions often require nearest neighbor searches that increase in computational cost with the number of samples. Edge evaluations require local planning between two states and detecting collisions on the resulting path.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Lazy sampling-based planners, such as Lazy PRM, reduce this computational cost by avoiding the evaluation of every edge. These algorithms first perform an inexpensive search on a simplified approximation without collision detection. This allows them to only evaluate the edges that are believed to be on an optimal path, and reduce the number of evaluated edges. This improves performance, especially for problems with computationally expensive edge evaluations, such as those considered in this paper.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper presents Adaptively Informed Trees (AIT\*), a lazy, almost-surely asymptotically optimal sampling-based planner that uses an asymmetric bidirectional search to simultaneously estimate and exploit an accurate, problem-specific heuristic. AIT\* estimates this heuristic by performing a lazy reverse search on the current sampling-based approximation. This heuristic is then used to order the forward search of this approximation while considering complete edge evaluations. The results of the computationally expensive edge evaluations performed by this forward search inform the reverse search, which creates increasingly accurate heuristics. This allows AIT\* to efficiently share information between the two individual searches.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Efficiently estimating and exploiting a problem-specific heuristic allows AIT\* to outperform existing sampling-based planning algorithms when edge evaluations are expensive. AIT\* finds initial solutions to the tested problems at least as fast as RRT-Connect while still almost-surely converging to the optimal solution, which RRT-Connect does not.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Improved Heuristics for Informed Search Algorithms", "weight": 1.0} -->

Improving the heuristic for informed graph-search algorithms has been shown to be effective for many problem domains, including path planning.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Improved Heuristics for Informed Search Algorithms", "weight": 1.0} -->

Pattern Databases are precomputed tables of exact solution costs to simplified subproblems of a problem domain. An informed algorithm can use this database during the search to create admissible heuristics. Additive Pattern Databases extend this approach to combine database entries into more accurate heuristics that are still admissible. This approach speeds up the search of problems for which simplified subproblems can be created and solved, but requires creating databases for every problem domain a priori to the search.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Improved Heuristics for Informed Search Algorithms", "weight": 1.0} -->

Heuristic accuracy can alternatively be improved by using the error in the heuristic values of states as they are discovered. Thayer et al. use the error of each state expansion to update the heuristic during the search. This can be applied to any problem domain and does not require any preprocessing, but the resulting heuristic is not guaranteed to be admissible.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Improved Heuristics for Informed Search Algorithms", "weight": 1.0} -->

Adaptive A\* is an incremental search algorithm that updates its heuristic function based on the cost-to-come values of previous searches of similar problems. This results in ever more accurate and admissible heuristics but can not be used for the initial search of a graph.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Improved Heuristics for Informed Search Algorithms", "weight": 1.0} -->

Kaindl. et al use the *Add method* to inform a forward search with a partial reverse search. The reverse search reveals errors in the heuristic values, the minimum of which is added to all unexpanded states. This results in a more informed but still admissible heuristic, but requires the user to specify how many states to expand during the reverse search and increases the heuristic uniformly for all unexpanded states. Wilt et al. present an updated version of this method which does not require a user-specified parameter.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Improved Heuristics for Informed Search Algorithms", "weight": 1.0} -->

Unlike these approaches, AIT\* does not need a predefined database, creates a consistent heuristic during the search, can be used on the initial search of a graph, and adaptively estimates the heuristic for each state individually.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Sampling-Based Planning with Heuristics", "weight": 1.0} -->

Heuristics have been used in sampling-based planning to guide the search and focus the approximation. RRT-Connect builds on Rapidly-exploring Random Trees (RRT) by incrementally growing two trees, one rooted in the start state and one in the goal state. These trees each explore the state space around them but are also guided towards each other by a *connect heuristic*. This approach can result in very fast initial solution times but is not almost-surely asymptotically optimal and does not improve the solution quality with more computational time.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Sampling-Based Planning with Heuristics", "weight": 1.0} -->

Informed RRT\* incorporates an ellipsoidal heuristic into the almost-surely asymptotically optimal RRT\*. This improves the convergence rate by focusing the incremental approximation to the relevant region of the state space but does not guide the search.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Sampling-Based Planning with Heuristics", "weight": 1.0} -->

Sakcak et al. incorporate a heuristic into a version of RRT\* which is based on motion-primitives. This can improve the performance for kinodynamic systems but requires preprocessing and relies on an a priori discretization which suffers from the curse of dimensionality.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Sampling-Based Planning with Heuristics", "weight": 1.0} -->

Batch Informed Trees (BIT\*) samples batches of states and views these sampled states as an increasingly dense edge-implicit random geometric graph (RGG). This allows BIT\* to use a series of informed graph-searches to process the states in order of potential solution quality. BIT\* efficiently reuses information from both previous searches and approximations by using incremental search techniques but does not update its heuristic during the search.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B Sampling-Based Planning with Heuristics", "weight": 1.0} -->

Unlike these approaches, AIT\* improves its solution quality with more computational time, uses its heuristic to guide the search, does not rely on an a priori discretization, and updates its heuristic during the search.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-C Sampling-Based Planning with Lazy Collision Detection", "weight": 1.0} -->

Path planning algorithms employ lazy collision detection to avoid spending computational resources on edges that are unlikely to be on an optimal path. Lazy PRM approximates the entire state space with an RGG without collision detection and searches this RGG for a path from the start state to a goal state. This path is then checked for collisions. If collisions are detected, then the corresponding edges and vertices are removed from the graph and a new search must be started from scratch. There also exist almost-surely asymptotically optimal variants of Lazy PRM.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-C Sampling-Based Planning with Lazy Collision Detection", "weight": 1.0} -->

Lazy Shortest Path (LazySP) is a class of algorithms that reduces the number of edges checked for collisions. It first finds a path from the start to the goal using an inexpensive estimate of the edge costs. Once a path is found, it uses an edge selector function which determines the order in which these edges are checked for collision. An example of a LazySP algorithm is Lazy Receding Horizon A\* (LRHA\*).

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-C Sampling-Based Planning with Lazy Collision Detection", "weight": 1.0} -->

Unlike these approaches, AIT\* does not restart its search from scratch upon detecting collisions, and uses admissible heuristics to focus its approximation.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Adaptively Informed Trees (AIT\\*)", "weight": 1.0} -->

BIT\* is an almost-surely asymptotically optimal sampling-based planner that builds a discrete approximation of a state space by sampling batches of states. This approximation can be focused to the region of the state space that can possibly improve a current solution with informed sampling.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Adaptively Informed Trees (AIT\\*)", "weight": 1.0} -->

BIT\* views the states it samples as an increasingly dense, edge-implicit RGG. It processes the implicit RGG edges in order of potential solution quality, similar to an edge-queue version of Lifelong Planning A\* (LPA\*). The true edge costs are evaluated lazily by maintaining a queue ordered by the sum of the current cost-to-come from the start to the edge's parent state, a heuristic of the edge cost, and a heuristic of the cost-to-go from the edge's child state to the goal state. Full details of BIT\* are.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Adaptively Informed Trees (AIT\\*)", "weight": 1.0} -->

AIT\* builds on BIT\* by improving the accuracy of the used heuristic, which improves performance on problems with expensive edge evaluations. It uses an asymmetric bidirectional search to efficiently estimate and exploit an accurate heuristic for each problem instance (Fig. 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")). The forward search is the same as in BIT\* but uses the heuristic provided by a computationally inexpensive reverse search. This heuristic can be updated efficiently when the forward search reveals that it contains errors by using an incremental algorithm, such as LPA\*, on the reverse search. Algorithm 1 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics") presents a conceptual overview of BIT\* and AIT\*.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Adaptively Informed Trees (AIT\\*)", "weight": 1.0} -->

The full algorithmic details are provided in Algorithms 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")--6 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics").

<!-- chunk {"id": "body-0031", "role": "body", "section": "Adaptively Informed Trees (AIT\\*)", "weight": 1.0} -->

Since BIT\* is almost-surely asymptotically optimal when given an admissible heuristic and the reverse search of AIT\* results in an admissible heuristic for each approximation, AIT\* is almost-surely asymptotically optimal as well.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Notation", "weight": 1.0} -->

The state space of the planning problem is denoted by ${X = {\mathbb{R}}^{n}},{n \in {\mathbb{N}}}$, the start by $\mathbf{x}_{init} \in X$, and the goals by $X_{goal} \in X$. The sampled states are denoted by $X_{sampled}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A Notation", "weight": 1.0} -->

The forward and reverse search trees are denoted by $\mathcal{F} = {(V_{\mathcal{F}},E_{\mathcal{F}})}$, and $\mathcal{R} = {(V_{\mathcal{R}},E_{\mathcal{R}})}$, respectively. The vertices in these trees, denoted by $V_{\mathcal{F}}$ and $V_{\mathcal{R}}$, are associated with valid states. The edges in the forward tree, $E_{\mathcal{F}} \subseteq {V_{\mathcal{F}} \times V_{\mathcal{F}}}$, represent valid connections between states, while the edges in the reverse tree, $E_{\mathcal{R}} \subseteq {V_{\mathcal{R}} \times V_{\mathcal{R}}}$, can lead through invalid regions of the problem domain.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A Notation", "weight": 1.0} -->

Let ${\mathbb{R}}_{\geq 0}^{\infty}$ denote the union of the nonnegative real numbers with infinity. The function $\hat{g}:{X\rightarrow{\mathbb{R}}_{\geq 0}^{\infty}}$ represents an admissible heuristic of the cost-to-come from the start to a state. The function $g_{\mathcal{F}}:{X\rightarrow{\mathbb{R}}_{\geq 0}^{\infty}}$ represents the cost-to-come from the start state to a state through the current forward tree. This cost is taken to be infinite for any state without an associated vertex in the forward tree.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A Notation", "weight": 1.0} -->

The function $\hat{h}:{X\rightarrow{\mathbb{R}}_{\geq 0}^{\infty}}$ represents an admissible heuristic of the cost-to-go from a state to a goal. The function $\hat{f}:{X\rightarrow{\mathbb{R}}_{\geq 0}^{\infty}}$ represents an admissible estimate of the cost of a path from the start to a goal constrained to go through a state, e.g., ${\hat{f}(\mathbf{x})}:={{\hat{g}(\mathbf{x})} + {\hat{h}(\mathbf{x})}}$. This estimate defines the informed set of states that could provide a better solution, $X_{\hat{f}}:=\left.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A Notation", "weight": 1.0} -->

Let $A$ be a set and let $B$, $C$ be subsets of $A$. The notation $B\overset{+}{\leftarrow}C$ is used for $B\leftarrow{B \cup C}$ and $B\overset{-}{\leftarrow}C$ for $B\leftarrow{B \smallsetminus C}$. The number of states sampled per batch is denoted by $m$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A Notation", "weight": 1.0} -->

1 initialize search, queue, and approximation 2 update the heuristic 4 get and remove the best edge from the queue 5 if the edge can possibly improve the solution 6 if the edge is valid 7 compute the true cost of the edge 8 update the search tree with the edge 11 update the heuristic 15 update the approximation 16 update the heuristic 17 populate the queue Algorithm 1 Concept of BIT* with changes for AIT*

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-B Approximation", "weight": 1.0} -->

AIT\* samples batches of states to build a discrete approximation of the state space. It uses informed sampling to focus its approximation to the region of the state space that can possibly improve the current solution (Alg. 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), line 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")).

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-B Approximation", "weight": 1.0} -->

States that are within a radius, $r$, of each other are treated as neighbors (Alg. 4 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), line 4 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")). Graph complexity is limited as states are sampled by decreasing this radius as, using the measure of the informed set, as, where $q$ is the number of sampled states in the informed set, $\eta > 1$ is a tuning parameter, and $\lambda{(X_{\hat{f}})}$ and $\zeta_{n}$ are the Lebesgue measures of the informed set and an $n$-dimensional unit ball, respectively. Faster-decreasing radii are provided in but are not used in AIT\* for fairer comparison to existing algorithms as they are presented in the literature.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-B Approximation", "weight": 1.0} -->

AIT\* always includes the existing connections in both the forward and the reverse search trees in its approximation (Alg. 4 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), lines 4 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), 4 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")), and removes invalid edges, regardless of the distance (Alg. 5 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), line 5 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"); Alg.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-B Approximation", "weight": 1.0} -->

4 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), line 4 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")).

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-C Reverse Search", "weight": 1.0} -->

AIT\* estimates a heuristic specific to the current approximation by performing a lazy reverse search with LPA\* (Alg. 5 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics") and Alg. 6 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")). This search uses a vertex-queue, $\mathcal{Q}_{R}$, which sorts states according to a lexicographical key, where ${\hat{h}}_{con}\lbrack\mathbf{x}\rbrack$ denotes the cost-to-go of $\mathbf{x}$ when it was last connected to the reverse tree and ${\hat{h}}_{\exp}\lbrack\mathbf{x}\rbrack$ denotes the cost-to-go of $\mathbf{x}$ when it was last expanded in the reverse search.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-C Reverse Search", "weight": 1.0} -->

These are the $g$ and $v$ values in a forward LPA\* search.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-C Reverse Search", "weight": 1.0} -->

If Algorithm 5 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics") is called without an argument (Alg. 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), lines 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")), it sets the ${\hat{h}}_{con}$ and ${\hat{h}}_{\exp}$ values of all states except the goals to infinity and inserts the goal states into the queue (Alg.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-C Reverse Search", "weight": 1.0} -->

5 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), lines 5 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")--5 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")). This restarts LPA\*, which is more efficient than repairing the search when large changes in the graph are expected. LPA\*'s initial search is equivalent to A\* and results in a consistent and admissible estimate of the heuristic in the current approximation.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-C Reverse Search", "weight": 1.0} -->

If Algorithm 5 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics") is called with an invalid edge (Alg. 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), line 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")), then it adds the edge to the set of invalid edges, $E_{invalid}$, and updates the cost-to-go of the parent state (Alg. 5 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), lines 5 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), 5 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")).

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-C Reverse Search", "weight": 1.0} -->

LPA\* then repairs the reverse search tree and increases the cost-to-go values, ${\hat{h}}_{con}$, as necessary. This results in an updated heuristic which is still admissible for the current approximation and can be used by the forward search. Full details of LPA\* are available.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-D Forward Search", "weight": 1.0} -->

The forward search of AIT\* uses an edge-queue, $\mathcal{Q}_{F}$, which sorts edges according to a lexicographical key, where the cost-to-go values from the reverse search are used as heuristic for the forward search, i.e., ${\hat{h}(\mathbf{x})}:={{\hat{h}}_{con}\lbrack\mathbf{x}\rbrack}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-D Forward Search", "weight": 1.0} -->

5 for all xgoal ∈ Xgoal do 11 $E_{invalid}\overset{+}{\leftarrow}\left(\mathbf{x}_{p},\mathbf{x}_{c} \right)$ 14while minx ∈ 𝒬R{R (x)} < R (xinit) 15 or ĥexp [xinit] < ĥcon [xinit] 16 or 𝒬F contains an edge with an unprocessed vertex do Algorithm 5 update_heuristic ((xp, xc)) 2 xp ← arg min xi ∈ neighbors (x){ĥexp [xi] + ĉ (xi, x)} 6 $\mathcal{Q}_{R}\overset{+}{\leftarrow}\mathbf{x}$ 9 $\mathcal{Q}_{R}\overset{-}{\leftarrow}\mathbf{x}$ Algorithm 6 update_state (x) An iteration begins by getting the best edge from the queue and checking whether it can possibly improve the current solution (Alg.

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-D Forward Search", "weight": 1.0} -->

2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), line 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")). If it can and is already part of the forward tree, its child state is expanded (Alg. 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), line 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")).

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-D Forward Search", "weight": 1.0} -->

If it is not in the forward tree but can possibly improve it (Alg. 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), line 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")), then the edge is checked for validity (Alg. 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), line 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")). If the edge is invalid, then the heuristic is updated by the reverse search (Alg.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-D Forward Search", "weight": 1.0} -->

2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), line 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"); Alg 5 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")). If the edge is valid, then it is completely evaluated. The search then checks whether it can actually improve the current solution and the forward tree (Alg. 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), lines 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")).

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-D Forward Search", "weight": 1.0} -->

The child state of a new edge that can improve the current solution and the forward tree is added to the tree if it is not already in the tree (Alg. 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), line 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")). If it is, then the new edge is a rewiring and the old edge is removed (Alg. 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), line 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")). The new edge is added to the tree and its child state is expanded in both cases (Alg.

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-D Forward Search", "weight": 1.0} -->

2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), lines 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")).

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-D Forward Search", "weight": 1.0} -->

The iteration finishes by updating the current solution cost (Alg. 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), line 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")). In practice this is done efficiently by only checking the goal states in the forward search tree.

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-D Forward Search", "weight": 1.0} -->

If the forward search processes an edge that can not possibly improve the current solution, then a new search on a refined approximation is started (Alg. 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), lines 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics"), 2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")--2 ‣ Adaptively Informed Trees (AIT*): Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

AIT\* was compared against the Open Motion Planning Library (OMPL) implementations of RRT-Connect, RRT\*, RRT^\#^, and BIT\* on simulated problems^11^1The performances were measured with OMPL v1.4.1 on a laptop with 16 GB of RAM and an Intel i7-4910MQ processor running Ubuntu 18.04.. RRT\* and RRT^\#^ used a goal bias of 5% and RRT^\#^ used rejection sampling. All RRT-based algorithms used maximum edge lengths of 0.5, 1.25, and 3.0 in ${\mathbb{R}}^{4},{\mathbb{R}}^{8}$, and ${\mathbb{R}}^{16}$, respectively. BIT\* and AIT\* sampled 100 states per batch regardless of dimension and used the Euclidean norm for all a priori heuristics. The RGG constant $\eta$ was 1.001 for all planners.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-A Abstract Problems", "weight": 1.0} -->

The planners were tested on two abstract problems with different obstacle configurations in ${\mathbb{R}}^{4},{\mathbb{R}}^{8}$, and ${\mathbb{R}}^{16}$ (Fig. 3: Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")). Each planner was run 100 times with different random seeds on each instantiation. Planners were given one second to solve problems in ${\mathbb{R}}^{4}$, ten seconds in ${\mathbb{R}}^{8}$, and 100 seconds in ${\mathbb{R}}^{16}$. The collision detection resolution was set to $10^{- 6}$ to make evaluating edge costs computationally expensive. The optimization objective was path length. Figure 4: Fast Asymptotically Optimal Path Planning through Adaptive Heuristics") shows the achieved preformances of all tested planners on all problems.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-A Abstract Problems", "weight": 1.0} -->

One abstract problem consisted of a wall with a narrow gap, such that in all dimensions only two homotopy classes exist (Fig. 3: Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")). This shows AIT\*'s performance on a problem containing a hard-to-find optimal homotopy class (Figs. 4: Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")--4: Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")).

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-A Abstract Problems", "weight": 1.0} -->

The other abstract problem consisted of a hollow, axis-aligned hyperrectangle enclosing the goal state configured such that even in higher dimensions the goal can only be reached through the face of the hyperrectangle farthest from the start state (Fig. 3: Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")). This problem is challenging for AIT\* because there are many invalid edges close to the root of the reverse search tree which means that often large parts of it must be repaired (Figs. 4: Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")--4: Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")).

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-B Planning for Axel", "weight": 1.0} -->

The benefits of AIT\*'s asymmetric bidirectional search were also tested on simulated planning problems for NASA/JPL-Caltech's Axel Rover System (Fig. 1: Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")), which is specialized for challenging terrain. These problems require sequences of ${SE}{}$ poses settled on the surface manifold of the terrain. This makes edge evaluations expensive, as every state along an edge has to be projected onto the manifold.

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-B Planning for Axel", "weight": 1.0} -->

BIT\* and AIT\* were run 100 times to plan a path down a steep slope with a line-of-sight distance of 30.97 meters between the start and goal positions (Fig. 5: Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")). The linear and angular collision detection resolutions were set to 2 cm and 0.1 rad, respectively. BIT\* and AIT\* optimized for path length and roll. Figure 5: Fast Asymptotically Optimal Path Planning through Adaptive Heuristics") shows the achieved performances.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Discussion & Future Work", "weight": 1.5} -->

AIT\* was designed for planning problems with expensive edge evaluations. These often occur when the search has to consider dynamic constraints (e.g., two-point boundary value problems) or complex robot and obstacle interactions (e.g., difficult collision detection) for each edge, as found on NASA/JPL-Caltech's Axel. In future work, Axel will consider tether-terrain interaction and physics-based stability checks based on the anchor history of the tether, which will further increase the edge evaluation cost.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Discussion & Future Work", "weight": 1.5} -->

These expensive edge evaluations were simulated in the abstract problems by increasing the collision detection resolution, providing a simple way to increase the edge evaluation cost and evaluate AIT\* on illustrative obstacle configurations.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Discussion & Future Work", "weight": 1.5} -->

The adaptive heuristic of AIT\* is less effective when the lazy reverse search connects many states through invalid edges, especially if these edges are near the root of the reverse search tree. This was illustrated with the goal enclosure experiment (Fig. 3: Fast Asymptotically Optimal Path Planning through Adaptive Heuristics")). Future work could use sparse collision detection on the reverse search to mitigate this problem.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Discussion & Future Work", "weight": 1.5} -->

The reverse search of AIT\* could also be used to estimate the search effort instead of the solution cost. The forward search could then be replaced with an anytime search that explicitly tries to minimize the time to the next solution, similar to, which could speed up initial solution times.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Discussion & Future Work", "weight": 1.5} -->

Another way to speed up initial solution times of AIT\* would be to inflate the heuristic term in the key of the forward queue, as in Advanced BIT\* (ABIT\*).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Informed sampling-based algorithms use heuristic knowledge about a problem domain to improve their performance. Heuristics that are applicable to all problems in a domain are often simple to define and inexpensive to evaluate but seldom accurate for a specific problem instance. Problem-specific heuristics can be very accurate but the computational cost to estimate and/or evaluate them can often outweigh the improved search efficiency.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presents AIT\*, an almost-surely asymptotically optimal sampling-based planner that simultaneously estimates and exploits an accurate heuristic specific to each problem instance. AIT\* uses an asymmetric bidirectional search to efficiently share information between the individual searches. The computationally inexpensive reverse search informs the expensive forward search by providing accurate heuristics specific to the current approximation of each problem instance. The forward search informs the reverse search by providing information about invalid edges, which results in ever more accurate heuristics. This is done efficiently by using LPA\* as the reverse search algorithm.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This approach is promising for path planning problems with expensive edge evaluations, such as those posed by NASA/JPL-Caltech's Axel. AIT\* outperforms existing sampling-based algorithms on the tested abstract problems by finding an initial solution quickly and converging to the optimum in an anytime manner. These problems show the robustness of AIT\* with respect to expensive edge evaluations and encourage more thorough evaluations of states which could be used in more advanced optimization objectives.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Information on the OMPL implementation of AIT\* is available at
