## Introduction

Popular path planning algorithms in robotics include graph-based searches, such as A^∗^ and Dijkstra's, and sampling-based planners, such as Rapidly-exploring Random Trees (RRT) and Probabilistic Roadmaps (PRM). Both graph- and sampling-based approaches have characteristic strengths and limitations. Previous work has separated search and approximation in single-query, almost-surely asymptotically optimal sampling-based planning to combine their strengths and mitigate their limitations. This separation can be leveraged to use advanced graph-based search techniques on an anytime sampling-based approximation to further improve performance.

An important strength of graph-based approaches is their strong theoretical guarantees. A\* is *resolution-optimal* (and *resolution-complete*) as well as *optimally efficient*. Any other algorithm guaranteed to find the optimal solution must expand at least as many vertices as A\*, given the same problem information. This efficiency is achieved by always expanding the state with the highest potential solution quality but requires an ordering of the search that does not provide any solutions until the optimum is found.

*Anytime* graph-search algorithms sacrifice the efficiency of A\* to find intermediate solutions faster. Anytime Repairing A\* (ARA\*) finds an initial, potentially suboptimal solution quickly and then uses any remaining computational time to improve it. ARA\* does this without duplicated search effort by starting with a heuristic that is inflated and then gradually decreasing this inflation while accounting for changes to state connections (i.e., inconsistent vertices).

Figure 1: ABIT* on NASA/JPL-Caltech’s Axel Rover System during a week-long field test in the Mojave Desert, California, USA (Section V-B).

These graph-based algorithms cannot be applied directly to planning problems with continuously valued state spaces and selecting appropriate a priori discretizations is difficult. Coarse resolutions are computationally inexpensive to search but may yield paths of poor quality in a continuous context. Fine resolutions contain paths of higher quality but the associated computational cost becomes prohibitively expensive in high dimensions (i.e., the curse of dimensionality ).

Sampling-based planners sample states incrementally to avoid picking a resolution a priori. Single-query planners such as RRT simultaneously build and search an anytime approximation that improves with computational time. This incremental sampling makes the search dependent on the sampling order and results in a randomly ordered search.

Ordering the search of an incremental planner in a solution-oriented manner requires either ordering the approximation or separating the search from the approximation. Batch Informed Trees (BIT\*) achieves the second by sampling batches of states and viewing them as an increasingly dense implicit random geometric graph (RGG). BIT\* uses incremental search techniques, similar to Lifelong Planning A\* (LPA\*), to process the sampled states in order of potential solution quality.

This paper extends BIT\* to further leverage the separation of search and approximation in sampling-based planning. Advanced BIT\* (ABIT\*) uses advanced graph-search techniques, such as inflation and truncation, to balance exploring and exploiting an increasingly dense RGG approximation. ABIT\* is almost-surely asymptotically optimal and outperforms existing single-query, almost-surely asymptotically optimal planners on random and artificially designed problems, especially in high dimensions. The benefits of ABIT\* were shown on real-world problems on NASA/JPL-Caltech's Axel (Fig. 1: Sampling-Based Planning with Advanced Graph-Search Techniques")) during a week-long field test in the Mojave Desert testing autonomous navigation on challenging terrain.

## Background

Multiquery algorithms, such as PRM and PRM\*, separate the approximation and the search in two phases. These algorithms first sample the entire collision-free state space to approximate it with a graph which is then searched to solve individual problems. This approximation is computationally expensive but justified by its reuse.

Lazy-PRM reduces the approximation cost by initially assuming that all vertices and edges are collision-free. A planning problem is then solved by searching this graph and checking the resulting path for collisions. If it contains collisions then the corresponding vertices and edges are removed and a new search is started on the updated graph.

Single-query problems only require an approximation of the state space relevant to the query. Expansive Space Trees (EST) avoids approximating the entire state space by incrementally growing trees from the start and goal. This focuses the approximation to the relevant region of the state space but couples the search with the approximation and results in a randomly ordered search.

RRT grows a single tree from the start to incrementally approximate the state space. It rapidly expands this tree by biasing its growth towards unexplored regions of the space (i.e., with Voronoi bias). The approximation and search are still coupled by the incremental sampling which also results in a randomly ordered search.

RRT-Connect grows trees from the start and goal and biases their growth both towards the unexplored space and each other. The greedy tree connection often results in fast initial solution times but the search of the unexplored space remains randomly ordered by the incremental sampling.

These algorithms provide no solution quality guarantee. RRT\* extends RRT to provide *almost-surely asymptotically optimal* solutions. Its solutions converge to the optimum with probability one given infinite computational time by locally rewiring the tree to ensure locally optimal connections. This search for the optimal local connection is performed immediately after each new state is sampled and the global search of the state space remains random.

Improving the convergence rate of RRT\* is an active area of research. Informed RRT\* and RRT\*-Smart are based on different sampling strategies. RRT^\#^ modifies the rewiring procedure to ensure globally optimal connections. Lower Bound Tree-RRT (LBT-RRT) is a near-optimal variant that allows for continuous interpolation between RRT and RRT\* by maintaining a tree which stores a lower bound on the cost-to-come to all vertices. These extensions modify how states are used but still process them individually and maintain the random search order of RRT\*.

Approximation and search can be separated by processing batches of multiple states. Fast Marching Tree (FMT\*) samples a user-specified number of states and uses a Fast Marching Method to grow a tree that connects them in order of increasing cost-to-come. FMT\* is not anytime and must be restarted from scratch if no suitable solution is found with the specified number of samples.

BIT\* samples multiple batches of states and views the resulting approximation as an increasingly dense edge-implicit RGG. It performs a search ordered on the potential solution quality of the implicit edges of this graph. It efficiently reuses previous search efforts by incorporating techniques from incremental graph-search approaches, similar to LPA\*. BIT\* is anytime but uses a nonanytime graph-search that only returns a single solution per approximation. This exploits the current approximation without considering that it will be updated once the search is finished, which may be inefficient.

Fast-BIT\* is a variation of BIT\* that finds initial solutions faster by ordering the initial search solely on cost-to-go. Once a solution is found, it reorders its queues with a full-solution heuristic and reprocesses all vertices. This maintains almost-sure asymptotic optimality but duplicates previous search effort unnecessarily. Fast-BIT\* then performs the same incremental search as BIT\* to fully exploit each subsequent approximation.

Unlike the multiquery planners, ABIT\* builds a problem-specific approximation of the state space. Unlike EST and the RRT-based approaches, ABIT\* separates approximation and search in a way that allows it to process states in order of (inflated) potential solution cost. Unlike FMT\*, ABIT\* improves its approximation in an anytime fashion. Unlike BIT\* and Fast-BIT\*, ABIT\* avoids wasting computational effort to find a resolution-optimal path in an inaccurate approximation that will change.

## Advanced Batch Informed Trees (ABIT\*)

BIT\* is an anytime, single-query planner that almost-surely asymptotically finds an optimal solution to a (continuously valued) planning problem. It focuses its approximation of the state space to the region that can improve the current solution using informed sampling. This approximation is separated from the search by sampling batches of states and viewing them as an increasingly dense edge-implicit RGG.

This perspective enables BIT\* to perform a series of informed graph-searches in which RGG edges are processed in order of their potential solution quality. This is achieved by sorting an edge queue according to the sum of the current cost-to-come from the start to the edge's parent state, an estimate of the edge cost, and an estimate of the cost-to-go from the edge's child state to a goal. BIT\* performs these searches efficiently by reusing information from both previous searches and approximations similar to incremental search algorithms, e.g. LPA\*. Full details are in.

BIT\*'s separation of approximation and search provides a direction for better single-query, almost-surely asymptotically optimal planning algorithms. ABIT\* builds on this separation by using more advanced graph-search techniques. It accelerates anytime performance without duplicating search effort, similar to anytime repairing graph-search algorithms, and avoids wasting effort to find the resolution-optimal solution in an approximation that will change, similar to truncated incremental graph-search algorithms.

This accelerated performance is achieved by inflating the cost-to-go estimate in ABIT\*'s edge queue. This sacrifices resolution-optimality but achieves faster initial solution times compared to the incremental search used by BIT\*. ABIT\*'s initial (potentially suboptimal) solution is subsequently repaired without duplicating search effort by tracking inconsistent states, similar to ARA\*. A state is considered inconsistent if its cost-to-come has decreased since its outgoing edges were last inserted into the queue.

Fully exploiting every RGG approximation by finding the resolution-optimal path is computationally expensive. ABIT\* avoids this by truncating its search as soon as it can guarantee that it has found a solution whose cost is within a factor of the resolution-optimal cost. This allows ABIT\* to balance the exploitation of its approximation (i.e., repairing the search) with the exploration of the state space (i.e., increasing the density of the approximation).

### III-A Notation

The state space of the planning problem is denoted by $X$, the start state by $\mathbf{x}_{start} \in X$, and the goal states by $X_{goal} \subset X$. The current search is stored as a tree, $\mathcal{T} = {(V,E)}$, with vertices, $V$, and edges, $E \subset {V \times V}$. Vertices in the tree are associated with valid states and edges in the tree represent valid connections between states. An edge consists of a parent state, $\mathbf{x}_{p}$, and a child state, $\mathbf{x}_{c}$, and is denoted as $(\mathbf{x}_{p},\mathbf{x}_{c})$. The set of inconsistent states is denoted by $V_{inconsistent}$ and the states that are not in the tree make up the set $X_{unconnected}$.

Let ${\mathbb{R}}_{\geq 0}^{\infty}$ denote the union of all nonnegative real numbers with infinity. The function $\hat{g}:{X\rightarrow{\mathbb{R}}_{\geq 0}^{\infty}}$ represents an admissible estimate (i.e., a lower bound) of the cost-to-come from the start to a state, $\mathbf{x} \in X$. The function $g_{\mathcal{T}}:{X\rightarrow{\mathbb{R}}_{\geq 0}^{\infty}}$ represents the cost-to-come from the start to a state, $\mathbf{x} \in X$, through the current search tree, $\mathcal{T}$. This cost is taken to be infinite for any state with no associated vertex in the tree.

The function $\hat{h}:{X\rightarrow{\mathbb{R}}_{\geq 0}^{\infty}}$ represents an admissible estimate of the cost-to-go from a state to a goal. The function $\hat{f}:{X\rightarrow{\mathbb{R}}_{\geq 0}^{\infty}}$ represents an admissible estimate of the cost of a path from the start to a goal constrained to go through a state, e.g., $\hat{f}{(\mathbf{x})} = \hat{g}{(\mathbf{x})} + \hat{h}{(\mathbf{x})}$. This estimate defines the informed set of states that could provide a better solution, $X_{\hat{f}} = {\{\mathbf{x} \in X|\hat{f}{(\mathbf{x})} \leq c_{current}\}}$, where $c_{current}$ is the current solution cost. The function $c:{{X \times X}\rightarrow{\mathbb{R}}_{\geq 0}^{\infty}}$ denotes the true edge cost between two states. The function $\hat{c}:{{X \times X}\rightarrow{\mathbb{R}}_{\geq 0}^{\infty}}$ is an admissible estimate of this cost.

Let $A$ be any set and let $B$ and $C$ be subsets of $A$, i.e., ${B,C} \subseteq A$. The notation $B\overset{+}{\leftarrow}C$ is used for $B\leftarrow{B \cup C}$ and $B\overset{-}{\leftarrow}C$ for $B\leftarrow{B \smallsetminus C}$. The cardinality of a set is denoted by $| \cdot |$ and the minimum of an empty set is taken to be infinity. The Lebesgue measure of a set is denoted by $\lambda{( \cdot )}$, and the Lebesgue measure of an $n$-dimensional unit ball by $\zeta_{n}$. The number of states per batch is denoted by $m$.

1 V ← {xstart}; E ← ⌀; 𝒯 ← (V,E); Xunconnected ← Xgoal
2 q ← |V| + |Xunconnected|; εinfl ← ∞; εtrunc ← ∞
4 𝒬 ← expand ({xstart},𝒯,Xunconnected,∞)
8 prune (𝒯,Xunconnected,Xgoal)
9 $X_{unconnected}\overset{+}{\leftarrow}\text{sample}\left( m,X_{goal} \right)$
11 𝒬 ← expand ({xstart},𝒯,Xunconnected,r (q))
14 $\mathcal{Q}\overset{+}{\leftarrow}\text{expand}\left( V_{inconsistent},\mathcal{T},X_{unconnected},{r(q)} \right)$
16 εinfl ← update_inflation_factor ()
17 εtrunc ← update_truncation_factor ()
19 mark_search_unfinished ()
22 $\left( \mathbf{x}_{p},\mathbf{x}_{c} \right)\leftarrow{\underset{{(\mathbf{x}_{i},\mathbf{x}_{j})} \in \mathcal{Q}}{\arg\min}\left\{ {{g_{\mathcal{T}}\left( \mathbf{x}_{i} \right)} + {\hat{c}\left( \mathbf{x}_{i},\mathbf{x}_{j} \right)} + {\varepsilon_{infl}\hat{h}\left( \mathbf{x}_{j} \right)}} \right\}}$
24 $\mathcal{Q}\overset{-}{\leftarrow}\left( \mathbf{x}_{p},\mathbf{x}_{c} \right)$
27 $V_{inconsistent}\overset{+}{\leftarrow}\mathbf{x}_{c}$
30 $\mathcal{Q}\overset{+}{\leftarrow}\text{expand}\left( \left\{ \mathbf{x}_{c} \right\},\mathcal{T},X_{unconnected},{r(q)} \right)$
31 $V_{closed}\overset{+}{\leftarrow}\mathbf{x}_{c}$
34 else if ${\varepsilon_{trunc}\left( {{g_{\mathcal{T}}{(\mathbf{x}_{p})}} + {\hat{c}{(\mathbf{x}_{p},\mathbf{x}_{c})}} + {\hat{h}{(\mathbf{x}_{c})}}} \right)} \leq {\min\limits_{\mathbf{x} \in X_{goal}}\left\{ {g_{\mathcal{T}}{(\mathbf{x})}} \right\}}$
36 if ${{g_{\mathcal{T}}{(\mathbf{x}_{p})}} + {c{(\mathbf{x}_{p},\mathbf{x}_{c})}} + {\hat{h}{(\mathbf{x}_{c})}}} &lt; {\min\limits_{\mathbf{x} \in X_{goal}}\left\{ {g_{\mathcal{T}}{(\mathbf{x})}} \right\}}$
39 $E\overset{-}{\leftarrow}\left\{ {\left( \mathbf{x}_{prev},\mathbf{x}_{c} \right) \in E} \right\}$
42 $X_{unconnected}\overset{-}{\leftarrow}\mathbf{x}_{c}$
43 $V\overset{+}{\leftarrow}\mathbf{x}_{c}$
45 $E\overset{+}{\leftarrow}\left( \mathbf{x}_{p},\mathbf{x}_{c} \right)$
47 $V_{inconsistent}\overset{+}{\leftarrow}\mathbf{x}_{c}$
50 $\mathcal{Q}\overset{+}{\leftarrow}\text{expand}\left( \left\{ \mathbf{x}_{c} \right\},\mathcal{T},X_{unconnected},{r(q)} \right)$
51 $V_{closed}\overset{+}{\leftarrow}\mathbf{x}_{c}$
57 else mark_search_finished ()
Algorithm 1 ABIT(xstart,Xgoal,m)

### III-B Initialization (Algorithm 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques"), Lines 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")-1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques"))

ABIT\* starts by initializing the search tree with the start state as its root. The set of unconnected states initially only contains the goal states (line 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")). The inflation factor, $\varepsilon_{infl} \geq 1$, and the truncation factor, $\varepsilon_{trunc} \geq 1$, are initialized to be infinitely large (line 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")). The edge-queue, $\mathcal{Q}$, holds all edges from the start state to the goal states (line 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")).

### III-C Approximation (Algorithm 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques"), Lines 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")-1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques"))

ABIT\* uses informed sampling to focus its RGG approximation on the relevant region of the state space. The accuracy of this approximation increases with the number of sampled states but so does its complexity. This complexity is reduced by pruning states that cannot improve the current solution (line 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques") and Alg. 3 ‣ III Advanced Batch Informed Trees (ABIT*) ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")) and shrinking the connection radius as more states are sampled. The radius, $r$, is updated as in, using the measure of the informed set, as in,

where $q$ is the number of sampled states in the informed set, $\eta > 1$ is a tuning parameter, and $n$ is the state space dimension. Faster-decreasing radii are provided in but are not used in this paper to isolate the reasons for ABIT\*'s improved performance relative to existing algorithms.

### III-D Search (Algorithm 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques"), Lines 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")-1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques"))

ABIT\* delays expensive computation of true edge cost (e.g., collision checks) with a lazy search similar to an edge-queue version of Anytime Truncated D\* (ATD\*). This queue is ordered lexicographically by (inflated) potential solution cost and then cost-to-come. A search iteration starts by removing the edge with the lowest queue value from the queue (line 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")). If this edge is part of the search tree, then the child state is expanded (i.e., its outgoing edges are added to the queue) if it has not already been expanded during the current search (lines 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")--1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques") and Alg. 2 ‣ III Advanced Batch Informed Trees (ABIT*) ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")). ABIT\* otherwise checks if the new edge can possibly contribute to a solution better than the current one (lines 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")--1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")).

An edge that passes these checks improves the cost-to-come of the child state and possibly the current solution. If the child state is already part of the tree, adding this edge constitutes a rewiring (line 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")). Otherwise, this state is removed from the set of unconnected states (line 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")) and added to the search tree (line 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")). In both cases, the edge is added to the search tree (line 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")).

After adding an edge, the child state is expanded unless it has already been expanded during the current search, in which case it is added to the set of inconsistent vertices (lines 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")--1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")).

3 $E_{out}\overset{+}{\leftarrow}\left\{ {\left( \mathbf{x}_{p},\mathbf{x}_{c} \right) \in E} \right\}$
5 if ${{\hat{g}{(\mathbf{x}_{p})}} + {\hat{c}{(\mathbf{x}_{p},\mathbf{x}_{c})}} + {\hat{h}{(\mathbf{x}_{c})}}} \leq {\min\limits_{\mathbf{x} \in X_{goal}}\left\{ {g_{\mathcal{T}}{(\mathbf{x})}} \right\}}$
7 $E_{out}\overset{+}{\leftarrow}\left( \mathbf{x}_{p},\mathbf{x}_{c} \right)$
Algorithm 2 expand({xi},𝒯,Xunconnected,r)

1 $X_{unconnected}\overset{-}{\leftarrow}\left\{ {\mathbf{x} \in X_{unconnected}} \middle| {{\hat{f}{(\mathbf{x})}} \geq {\min\limits_{\mathbf{x} \in X_{goal}}\left\{ {g_{\mathcal{T}}{(\mathbf{x})}} \right\}}} \right\}$
2 $V\overset{-}{\leftarrow}\left\{ {\mathbf{x} \in V} \middle| {{\hat{f}(\mathbf{x})} &gt; {\min\limits_{\mathbf{x} \in X_{goal}}\left\{ {g_{\mathcal{T}}(\mathbf{x})} \right\}}} \right\}$
3 $E\overset{-}{\leftarrow}\left\{ {\left( \mathbf{x}_{p},\mathbf{x}_{c} \right) \in E} \middle| {{\hat{f}\left( \mathbf{x}_{p} \right)} &gt; {{\min\limits_{\mathbf{x} \in X_{goal}}\left\{ {g_{\mathcal{T}}(\mathbf{x})} \right\}}{\mathbf{o}\mathbf{r}}\hat{f}\left( \mathbf{x}_{c} \right)} &gt; {\min\limits_{\mathbf{x} \in X_{goal}}\left\{ {g_{\mathcal{T}}(\mathbf{x})} \right\}}} \right\}$
4 $X_{unconnected}\overset{+}{\leftarrow}\left\{ {\mathbf{x}_{c} \in V} \middle| {{\nexists\mathbf{x}_{p}} \in {V\text{~s.~t.~}\left( \mathbf{x}_{p},\mathbf{x}_{c} \right)} \in E} \right\}$
5 $V\overset{-}{\leftarrow}\left\{ {\mathbf{x}_{c} \in V} \middle| {{\nexists\mathbf{x}_{p}} \in {V\text{~s.~t.~}\left( \mathbf{x}_{p},\mathbf{x}_{c} \right)} \in E} \right\}$
Algorithm 3 prune (𝒯,Xunconnected,Xgoal)

### III-E Approximation, Inflation, and Truncation Update Policies

The approximation is updated when a desired bound on the resolution optimality is achieved, which depends on the inflation and truncation factors (line 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")). These factors are updated after each search of the current RGG (lines 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques") and 1 ‣ Advanced BIT* (ABIT*): Sampling-Based Planning with Advanced Graph-Search Techniques")). A high inflation factor biases the search towards the goal and decreases solution times but results in loose bounds on the solution quality. A low inflation factor results in a search that requires more computational effort to complete but achieves tighter bounds on the solution quality. A high truncation factor promotes exploration of the region of the state space that could potentially contain better solutions by truncating the search once a loose bound on the solution quality is achieved, which facilitates adding more samples. A low truncation factor promotes exploiting the current approximation of the state space as the search is not truncated until a tight bound on the solution quality is guaranteed.

The update policies of these two factors are user-tuned parameters that balance exploiting the current RGG with exploring the state space. Section V: Sampling-Based Planning with Advanced Graph-Search Techniques") presents the specific policies used for the experimental results.

## Formal Analysis

This paper uses Definition 24 in as the definition of almost-sure asymptotic optimality. Note that any sampling-based planner is almost-surely asymptotically optimal if (i) its underlying graph almost-surely contains an asymptotically optimal path, and (ii) its underlying graph-search is asymptotically resolution-optimal. These conditions are sufficient but not necessary.

### IV-A Almost-Sure Existence of an Asymptotically Optimal Path

ABIT\* uses the same increasingly dense RGG approximation as BIT\*. Since BIT\* is an almost-surely asymptotically optimal algorithm, this approximation must almost-surely contain an asymptotically optimal path.

### IV-B Asymptotically Resolution-Optimal Search

Theorem 1: Sampling-Based Planning with Advanced Graph-Search Techniques") states that ABIT\*'s search processes at least all of the edges processed by ATD\*, which is an anytime, incremental search algorithm that finds a solution within $\varepsilon_{trunc}\varepsilon_{infl}$ of the optimum. Since ABIT\* updates the cost-to-come of any vertex under the same condition as ATD\*, ABIT\* also finds a solution whose cost is within $\varepsilon_{trunc}\varepsilon_{infl}$ of the optimum. ABIT\* therefore asymptotically finds a resolution-optimal path when the product $\varepsilon_{trunc}\varepsilon_{infl}$ tends to one as the number of samples approaches infinity,

### Theorem 1

ABIT\*'s search processes at least all of the edges that would be processed by ATD\* for a given RGG.

### Proof

ATD\* can handle improved and worsened state connections, but adding states and edges to a graph can only improve connections. Therefore only states with improved cost-to-come (called overconsistent in ) are considered.

ATD\*'s vertex queue is first converted to a compatible edge queue and it is then shown that ATD\*'s termination criterion is stricter than that of ABIT\*.

ATD\* computes a sort key for every state, $\mathbf{x}$, in its queue,

The cost-to-come label, $g_{p}{\lbrack\mathbf{x}\rbrack}$, is recursively defined as

where $X_{p}{(\mathbf{x})}$ denotes the discovered potential parents of $\mathbf{x}$ and the base case is ${g_{p}{\lbrack\mathbf{x}_{start}\rbrack}} = 0$. ATD\* processes vertices in its vertex queue, $\mathcal{Q}_{{ATD}^{\ast}}^{V}$, in order of ascending key values,

Whenever a better connection to a state in the queue is found, the key of this state is updated and the queue is resorted.

The queue could alternatively contain multiple instances of the same state, each with a different parent and key value. Selecting the minimum from this queue would ensure that the best discovered connection for each state is considered first. This would be equivalent to an edge version of ATD\* where the next connection from the edge queue, $\mathcal{Q}_{{ATD}^{\ast}}^{E}$, is

ATD\*'s inner loop terminates if for any goal $\mathbf{x}_{goal} \in X_{goal}$

ABIT\*'s search terminates if for any goal $\mathbf{x}_{goal} \in X_{goal}$

This is less strict, as the heuristic, $\hat{c}$, is admissible, the inflation factor, $\varepsilon_{infl}$, is greater than or equal to one, and for all states, $\mathbf{x}_{i} \in X$, it holds that ${g_{p}{\lbrack\mathbf{x}_{i}\rbrack}} \geq {g_{\mathcal{T}}{(\mathbf{x}_{i})}}$ as rewirings can only improve the cost-to-come to states. ABIT\* therefore considers at least all edges that ATD\* would consider. ∎

Figure 2: A 2D illustration of the simulated planning problems used in Section V. The state space, X ⊂ ℝn, is bounded by a hypercube of width two for both problems. Ten different instantiations of the random rectangles experiment were tested. The results are presented in Fig. 3.

## Experimental Results

ABIT\* was compared against the Open Motion Planning Library (OMPL) versions of RRT-Connect, RRT\*, RRT^\#^, LBT-RRT, and BIT\* on simulated problems in ${\mathbb{R}}^{4}$ and ${\mathbb{R}}^{8}$ (Fig. 2: Sampling-Based Planning with Advanced Graph-Search Techniques"))^11^1The performances were measured with OMPL v1.4.1 on a laptop with 16 GB of RAM and an Intel i7-4910MQ processor running Ubuntu 18.04.. The objective for the almost-surely asymptotically optimal planners was to minimize path length. The RGG constant $\eta$ was set to 1.1 for all planners. LBT-RRT used the default value of 0.4 as the approximation factor. RRT^\#^ sampled the entire state space. RRT-based algorithms used a goal bias of 5% and maximum edge lengths of 0.5 and 1.25 in ${\mathbb{R}}^{4}$ and ${\mathbb{R}}^{8}$, respectively. BIT\* and ABIT\* sampled 100 states per batch regardless of the state space dimension, had graph pruning turned off, and used Euclidean distance as a heuristic. ABIT\* was configured to search each RGG twice. First with a highly inflated heuristic, $\varepsilon_{infl} = 10^{6}$, and then again with a lower factor, $\varepsilon_{infl} = {1 + {10/q}}$. A single truncation factor, $\varepsilon_{trunc} = {1 + {5/q}}$ was used for all searches. All parameters were tuned to optimize planner performance on test problems.

### V-A Experimental Problems

The planners were tested on two problems in ${\mathbb{R}}^{4}$ and ${\mathbb{R}}^{8}$. The first consisted of a wall with a narrow gap such that valid paths can only be in one of two homotopy classes (Fig. 2a: Sampling-Based Planning with Advanced Graph-Search Techniques")). Each planner was run 100 times for one second with different random seeds. Figures 3a and 3d show the achieved success rates and median path lengths of all tested planners.

The second consisted of axis-aligned hyperrectangles of random widths placed randomly in the state space (e.g., Fig. 2b: Sampling-Based Planning with Advanced Graph-Search Techniques")). Ten different random problems were generated for each state space dimension and planners were run 100 times on each instantiation. The runtime was limited to one and 40 seconds for problems in ${\mathbb{R}}^{4}$ and ${\mathbb{R}}^{8}$, respectively. Figures 3b, 3c, 3e, and 3f show the achieved success rates and median path costs of all tested planners for the two problems that resulted in the best and worst performances of ABIT\*, as defined by its initial solution time relative to RRT-Connect.

### V-B Planning for Axel

The benefits of ABIT\*'s advanced graph-search techniques were also demonstrated on real-world robotic planning problems during a week-long NASA/JPL-Caltech field test in the Mojave Desert with the Axel Rover System (Fig. 1: Sampling-Based Planning with Advanced Graph-Search Techniques")). Axel is a tethered robotic platform designed for near-vertical surfaces and other challenging or unstable terrain. The complexity of the terrain and its interaction with the tether make for challenging planning problems because state evaluations are computationally expensive. ABIT\* typically found initial solutions to these problems in under two seconds. This allowed it to spend the remaining computational time to improve this solution by repairing its search and increasing the density of its approximation. This resulted in 95.12% autonomy by distance, despite the challenging terrain.

Figure 3: Results from the experiments described in Section V-A. The results from the wall gap experiment are shown in the plots (a) and (d) for ℝ4 and ℝ8, respectively. The plots (b) and (c) show the best and worst instances of ten random rectangles experiments in ℝ4. The plots (e) and (f) show the best and worst instances in ℝ8. The squares in the cost plots show the median initial costs and times while the lines show the median cost over time for almost-surely asymptotically optimal planners (unsuccessful runs were taken as infinite costs). The error bars show a nonparametric 99% confidence interval on the solution cost and time. Note that in plot (f) less than 50 trials of LBT-RRT, RRT* and RRT# succeeded, so their median cost is infinity.

## Discussion & Conclusion

ABIT\* demonstrates that the perspective of separate approximation and search in single-query almost-surely asymptotically optimal sampling-based planning can be used to design algorithms with improved anytime performance. Figure 3: Sampling-Based Planning with Advanced Graph-Search Techniques") shows that ABIT\* outperforms other single-query, almost-surely asymptotically optimal planners by finding initial solutions quickly and converging to an optimal solution in an anytime manner without wasting computational effort. The only tested planner that finds initial solutions faster than ABIT\* is RRT-Connect, which is not an almost-surely asymptotically optimal algorithm and cannot improve its initial solution when given more computational time.

ABIT\* relies on admissible heuristic estimates of edge-costs between states and the cost-to-go from states to a goal. If no heuristics are available, ABIT\* can be run with the trivial heuristic, i.e., ${{\forall\mathbf{x}_{i}},\mathbf{x}_{j}} \in X$, ${\hat{h}{(\mathbf{x}_{i})}} \equiv {\hat{c}{(\mathbf{x}_{i},\mathbf{x}_{j})}} \equiv 0$. An asymmetric bidirectional search could alternatively be used to simultaneously estimate and exploit a problem-specific heuristic, as in Adaptively Informed Trees (AIT\*).

If ABIT\* is run with unit inflation and truncation factors, it can be viewed as a simplified but equally performant version of BIT\* that cascades rewirings. ABIT\* uses a single edge queue instead of BIT\*'s dual vertex and edge queues and avoids repeated collision checks by caching checked edges in an object-oriented manner instead of labelling states *old* or *new* as in BIT\*. This clarifies the conceptual ideas behind these algorithms and simplifies their implementation without adding any practically significant computational costs.

This improved implementation allows ABIT\* to balance exploiting its current approximation of the state space with exploring the relevant regions of the state space. This is achieved using advanced graph-search techniques similar to anytime repairing and truncated search algorithms.

An inflated heuristic biases ABIT\*'s search towards the goal and finds initial solutions quickly. Truncating the search once a sufficient bound on the solution quality of the current solution is achieved avoids wasting computational effort fully exploiting an approximation that will change. Flexible update policies of the inflation and truncation factors ensure that ABIT\* can leverage high and low inflation and truncation depending on the accuracy of its approximation. ABIT\* is not very sensitive to the exact form of these policies. Results comparable to the ones presented in this paper are achieved whenever the initial search is conducted with a very high inflation factor and both factors asymptotically tend to one as the number of sampled states approaches infinity.

ABIT\* also shows the benefits of using advanced graph-search techniques in sampling-based planning on real-world path planning problems posed by Axel, a NASA/JPL-Caltech rover specialized for navigation on challenging terrain.

Information on the OMPL implementation of ABIT\* is available at [https://robotic-esp.com/code/](https://robotic-esp.com/code/).
