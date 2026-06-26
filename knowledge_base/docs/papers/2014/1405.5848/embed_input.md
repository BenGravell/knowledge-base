<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs

Topics include Motion planning, Sampling-based planning, Asymptotic optimality, Anytime planning, Heuristic search, Random geometric graphs, Graph search, Informed sampling.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

BIT* unifies graph- and sampling-based planning by treating a batch of random samples as an implicit random geometric graph (RGG) and searching it with an A*/LPA*-style ordered search focused on the informed ellipsoidal subset of states that can improve the current solution. Successive batches of increasing density are searched while reusing prior information, yielding a probabilistically complete, asymptotically optimal anytime planner that converges substantially faster than RRT* and FMT*, especially in high-dimensional spaces.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we present Batch Informed Trees (BIT*), a planning algorithm based on unifying graph- and sampling-based planning techniques. By recognizing that a set of samples describes an implicit random geometric graph (RGG), we are able to combine the efficient ordered nature of graph-based techniques, such as A*, with the anytime scalability of sampling-based algorithms, such as Rapidly-exploring Random Trees (RRT). BIT* uses a heuristic to efficiently search a series of increasingly dense implicit RGGs while reusing previous information. It can be viewed as an extension of incremental graph-search techniques, such as Lifelong Planning A* (LPA*), to continuous problem domains as well as a generalization of existing sampling-based optimal planners. It is shown that it is probabilistically complete and asymptotically optimal. We demonstrate the utility of BIT* on simulated random worlds in R^2 and R^8 and manipulation problems on CMU's HERB, a 14-DOF two-armed robot.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

On these problems, BIT* finds better solutions faster than RRT, RRT*, Informed RRT*, and Fast Marching Trees (FMT*) with faster anytime convergence towards the optimum, especially in high dimensions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Graph-search and sampling-based methods are two popular techniques for path planning in robotics. Graph-based searches, such as Dijkstra's algorithm and A\*, use dynamic programming to exactly solve a discrete approximation of a problem. These algorithms are not only *resolution complete* but also *resolution optimal*, always finding the optimal solution to the given problem at the chosen discretization, if one exists. A\* does this efficiently by using a heuristic to estimate the total cost of a solution constrained to pass through a state. The result is an algorithm that searches in order of decreasing solution quality and is *optimally efficient*. Any other optimal algorithm using the same heuristic will expand at least as many vertices as A\*.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The quality of the *continuous* solution found by these graph-search techniques depends heavily on the discretization of the problem. Finer discretization increases the quality of the solution, but also increases the computational effort necessary to find it. This becomes a significant problem in high-dimensional spaces, such as for manipulation planning (Fig. 1: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")), as the size of the discrete state space grows exponentially with the number of dimensions. Bellman referred to this problem as the curse of dimensionality. Graph-search techniques have still been successful as planning algorithms on a variety of graph types, including for nonholonomoic robots, kinodynamic planning, and manipulation planning.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Graph search has also been extended to *anytime* and *incremental* search. Anytime techniques quickly find a suboptimal path before completing the search for the optimum, while incremental techniques handle changes in a graph efficiently by reusing information.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sampling-based planners, such as [[PRM]](#id83.83.id83), [[RRT]](#id88.88.id88), and Expansive Space Trees, avoid the discretization problems of graph-search techniques by randomly sampling the continuous planning domain. This scales more effectively to high-dimensional problems, but makes their search probabilistic. They are *probabilistically complete*, having a probability of finding a solution, if one exists, that goes to one as the number of samples goes to infinity. Anytime algorithms, such as [[RRT]](#id88.88.id88) and [[EST]](#id75.75.id75), also have *anytime resolution*, a growing representation of the problem domain that becomes increasingly accurate as the number of iterations increases.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimal variants, such as [[RRT\*]](#id90.90.id90) and [[PRM\*]](#id84.84.id84), are also *asymptotically optimal*, converging asymptotically to the optimal solution with probability one as the number of samples goes to infinity (*almost sure* asymptotic convergence). While solutions improve with computational time, this does not guarantee a reasonable rate of convergence as the random sampling is inherently *unordered*.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

There is a long history of adding graph-search concepts to sampling-based planners. Algorithms have used heuristics to refine the [[RRT]](#id88.88.id88) search, including by biasing the sampling procedure, and to define a series of subplanning problems given the current solution. Similarly, focusing techniques have also been used to limit the search of optimal ([[RRT\*]](#id90.90.id90)) once it finds a solution. While these techniques can improve the initial solution and/or the convergence rate to the optimum, their [[RRT]](#id88.88.id88)-based search is still unordered.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Other algorithms order the search at the expense of anytime resolution. [[FMT\*]](#id76.76.id76) uses a marching method to process a single set of samples. The resulting search is ordered on cost-to-come but must be restarted if a higher resolution is needed. The Motion Planning Using Lower Bounds ([[MPLB]](#id79.79.id79)) algorithm extends [[FMT\*]](#id76.76.id76) to quasi-anytime resolution and an ordering given by estimating the cost of solutions constrained to pass through each state. The quasi-anytime resolution is achieved by solving a series of independent problems with an increasing number of samples. It is stated that this can be done efficiently by reusing information, but no specific methods are presented.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Still other algorithms attempt to extend graph-search directly to continuous planning problems. In Randomized A\* ([[RA\*]](#id85.85.id85)) and Sampling-based A\* ([[SBA\*]](#id92.92.id92)) a tree is grown towards solutions by sampling near heuristically selected vertices. This biases the growth of the tree towards good solutions but requires methods to avoid local minima. [[RA\*]](#id85.85.id85) defines a minimum-allowed distance between vertices, limiting the number of times a vertex can be expanded but also limiting the final resolution. [[SBA\*]](#id92.92.id92) includes a measure of local sample density in the vertex expansion heuristic. This decreases the priority of sampling near frequently expanded vertices, but requires methods to estimate local sample density.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present [[BIT\*]](#id72.72.id72), a planning algorithm that balances the benefits of graph-search and sampling-based techniques. It uses batches of samples to perform an ordered search on a continuous planning domain while maintaining anytime performance. By processing samples in batches, its search can be ordered around the minimum solution proposed by a heuristic, as in A\*. By processing multiple batches of samples, it converges asymptotically towards the global optimum with anytime resolution, as in [[RRT\*]](#id90.90.id90). This is done efficiently by using incremental search techniques to incorporate the new samples into the existing search, as in [[LPA\*]](#id78.78.id78). The multiple batches also allow subsequent searches to be focused on the subproblem that could contain a better solution, as in Informed [[RRT\*]](#id90.90.id90).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

The performance of [[BIT\*]](#id72.72.id72) is demonstrated both on random experiments in ${\mathbb{R}}^{2}$ and ${\mathbb{R}}^{8}$ and manipulation problems on the [[CMU]](#id2.2.id2) Personal Robotic Lab's Home Exploring Robot Butler ([[HERB]](#id93.93.id93)). The results show that [[BIT\*]](#id72.72.id72) consistently outperformed both nonasymptotically and asymptotitcally optimal planners ([[RRT]](#id88.88.id88), [[RRT\*]](#id90.90.id90), Informed [[RRT\*]](#id90.90.id90), and [[FMT\*]](#id76.76.id76)).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

It was more likely to have found a solution at a given computational time and converged towards the optimum faster. The same held in difficult planning problems on [[HERB]](#id93.93.id93), where collision checking is expensive. [[BIT\*]](#id72.72.id72) was nearly twice as likely to find a solution to a difficult two-arm problem (Fig. 1: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")) and found better solutions on easier one-arm problems (Fig. 6: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")). The only planner tested that found solutions faster was [[RRT]](#id88.88.id88)-Connect, which does not converge towards the optimum.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows. Section II: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs") presents further background and Section III ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs") presents a description of the algorithm. Section IV: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs") presents an initial theoretical analysis of [[BIT\*]](#id72.72.id72), while Section V: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs") presents the experimental results in detail. Finally, Section VI: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs") presents a discussion on the algorithm and related future work and Section VII: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs") provides a conclusion.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Definition 1 (Optimal Planning)", "weight": 1.0} -->

Let $X \subseteq {\mathbb{R}}^{n}$ be the state space of the planning problem, $X_{obs} \subset X$ be the states in collision with obstacles, and $X_{free} = {X \smallsetminus X_{obs}}$ be the resulting set of permissible states. Let $\mathbf{x}_{start} \in X_{free}$ be the initial state and $X_{goal} \subset X_{free}$ be the set of desired final states. Let $\sigma:{\lbrack 0,1\rbrack\mapsto X}$ be a sequence of states (a path) and $\Sigma$ be the set of all nontrivial paths.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Definition 1 (Optimal Planning)", "weight": 1.0} -->

The optimal solution is the path, $\sigma^{\ast}$, that minimizes a chosen cost function, $s:{\Sigma\mapsto{\mathbb{R}}_{\geq 0}}$, while connecting $\mathbf{x}_{start}$ to any $\mathbf{x}_{goal} \in X_{goal}$ through free space, where ${\mathbb{R}}_{\geq 0}$ is the set of non-negative real numbers. We denote the cost of this optimal path as $s^{\ast}$. ∎ A discrete set of states in this state space, $X_{samples} \subset X$, can be viewed as a graph whose edges are given algorithmically by a transition function (an *implicit* graph).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Definition 1 (Optimal Planning)", "weight": 1.0} -->

When these states are sampled randomly, $X_{samples} = \left\{ {\mathbf{x} \sim {\mathcal{U}(X)}} \right\}$, the properties of the graph can be described by a probabilistic model known as a [[RGG]](#id59.59.id59).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Definition 1 (Optimal Planning)", "weight": 1.0} -->

In an [[RGG]](#id59.59.id59), the connections (edges) between states (vertices) depend on their relative geometric position. Common [[RGGs]](#id59.59.id59) have edges to a specific number of each state's nearest neighbours (a $k$-nearest graph ) or to all neighbours within a specific distance (an $r$-disc graph ). [[RGG]](#id59.59.id59) theory provides probabilistic relationships between the number and distribution of samples, the $k$ or $r$ defining the graph, and specific graph properties such as connectivity or relative cost through the graph.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Definition 1 (Optimal Planning)", "weight": 1.0} -->

Sampling-based planners can therefore be viewed as algorithms to construct an implicit [[RGG]](#id59.59.id59) and an explicit spanning tree in the free space of the planning problem. Much like graph-search techniques, the performance of an algorithm will depend on the quality of the [[RGG]](#id59.59.id59) representation and the efficiency of the search.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Definition 1 (Optimal Planning)", "weight": 1.0} -->

Karaman and Frazzoli use [[RGG]](#id59.59.id59) theory in [[RRT\*]](#id90.90.id90) to limit graph complexity while maintaining probabilistic bounds on the representation, but the graph is constructed and searched simultaneously, resulting in a randomly ordered anytime search. Janson and Pavone similarly use [[RGG]](#id59.59.id59) theory in [[FMT\*]](#id76.76.id76), but for a constant number of samples, resulting in an ordered but nonanytime (in solution or resolution) search. Recently, Salzman and Halperin have given [[FMT\*]](#id76.76.id76) quasi-anytime performance by independently solving increasingly dense [[RGGs]](#id59.59.id59) in their [[MPLB]](#id79.79.id79) algorithm.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem Definition 1 (Optimal Planning)", "weight": 1.0} -->

Heuristics order and focus the search, but solutions are only returned when an [[RGG]](#id59.59.id59) is completely searched.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem Definition 1 (Optimal Planning)", "weight": 1.0} -->

In contrast, [[BIT\*]](#id72.72.id72) uses *incremental* search techniques on increasingly dense [[RGGs]](#id59.59.id59). This balances the benefits of heuristically ordered search with anytime performance and asymptotic optimality. The tuning parameters are the choice of the heuristic, an [[RGG]](#id59.59.id59) constant, and the number of samples per batch. [[BIT\*]](#id72.72.id72) can be viewed as an extension of [[LPA\*]](#id78.78.id78) to continuous problems and as a generalization of existing sampling-based optimal planners (Fig. 2: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem Definition 1 (Optimal Planning)", "weight": 1.0} -->

With batches of one sample, it is a version of Informed [[RRT\*]](#id90.90.id90), and with a single batch and the zero heuristic, a version of [[FMT\*]](#id76.76.id76).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Batch Informed Trees ([[BIT\\*]](#id72.72.id72))", "weight": 1.0} -->

Informally, [[BIT\*]](#id72.72.id72) works as follows. An initial [[RGG]](#id59.59.id59) with *implicit* edges is defined by uniformly distributed random samples from the free space and the start and goal. The [[RGG]](#id59.59.id59) parameter ($r$ or $k$) is chosen to reduce graph complexity while maintaining asymptotic optimality requirements as a function of the number of samples. An *explicit* tree is then built outwards from the start towards the goal by a heuristic search (Fig. 3: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")a). This tree includes only collision-free edges and its construction stops when a solution is found or it can no longer be expanded (Fig. 3: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")b). This concludes a *batch*.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Batch Informed Trees ([[BIT\\*]](#id72.72.id72))", "weight": 1.0} -->

To start a new batch, a denser implicit [[RGG]](#id59.59.id59) is constructed by adding more samples and updating $r$ (or $k$). If a solution has been found, these samples are limited to the subproblem that could contain a better solution (e.g., an ellipse for path length ). The tree is then updated using [[LPA\*]](#id78.78.id78)-style incremental search techniques that reuse existing information (Fig. 3: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")c). As before, the construction of the tree stops when the solution cannot be improved or when there are no more collision-free edges to traverse (Fig. 3: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")d). The process continues with new batches as time allows.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A Notation", "weight": 1.0} -->

The functions $\hat{g}(\mathbf{x})$ and $\hat{h}(\mathbf{x})$ represent admissible estimates of the cost-to-come to a state, $\mathbf{x} \in X$, from the start and the cost-to-go from a state to the goal, respectively (i.e., they bound the true costs from below). The function, $\hat{f}(\mathbf{x})$, represents an admissible estimate of the cost of a path from $\mathbf{x}_{start}$ to $X_{goal}$ constrained to pass through $\mathbf{x}$, i.e., ${\hat{f}(\mathbf{x})}:={{\hat{g}(\mathbf{x})} + {\hat{h}(\mathbf{x})}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Notation", "weight": 1.0} -->

This estimate defines a subset of states, $X_{\hat{f}}:=\left\{ {\mathbf{x} \in X} \middle| {{\hat{f}(\mathbf{x})} \leq c_{best}} \right\}$, that could provide a solution better than the current best solution cost, $c_{best}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Notation", "weight": 1.0} -->

Let $\mathcal{T}:=(V,E)$ be an *explicit* tree with a set of vertices, $V \subset X_{free}$, and edges, $E = \left\{ (\mathbf{v},\mathbf{w}) \right\}$ for some ${\mathbf{v},\mathbf{w}} \in V$. The function $g_{\mathcal{T}}(\mathbf{x})$ represents the cost-to-come to a state $\mathbf{x} \in X$ from the start vertex given the current tree, $\mathcal{T}$. We assume a state not in the tree, or otherwise unreachable from the start, has a cost-to-come of infinity.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Notation", "weight": 1.0} -->

It is important to recognize that these two functions will always bound the unknown true optimal cost to a state, $g( \cdot )$, i.e., ${{\forall\mathbf{x}} \in X},{{\hat{g}(\mathbf{x})} \leq {g(\mathbf{x})} \leq {g_{\mathcal{T}}(\mathbf{x})}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Notation", "weight": 1.0} -->

The functions $\hat{c}(\mathbf{x},\mathbf{y})$ and $c(\mathbf{x},\mathbf{y})$ represent an admissible estimate of the cost of an edge and the true cost of an edge between states ${\mathbf{x},\mathbf{y}} \in X$, respectively. We assume that edges that intersect the obstacle set have a cost of infinity, and therefore ${{{\forall\mathbf{x}},\mathbf{y}} \in X},{{\hat{c}(\mathbf{x},\mathbf{y})} \leq {c(\mathbf{x},\mathbf{y})} \leq \infty}$. It is important to recognize that calculating $c(\mathbf{x},\mathbf{y})$ can be expensive (e.g., collision detection, differential constraints, etc.) and using a heuristic estimate for edge cost has the effect of delaying this calculation until necessary.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A Notation", "weight": 1.0} -->

The function $\lambda( \cdot )$ represents the Lebesgue measure of a set (e.g., the volume), and $\zeta_{n}$ represent the Lebesgue measure of an $n$-dimensional unit ball. The cardinality of a set is denoted by $| \cdot |$. We use the notation $X\overset{+}{\leftarrow}\left\{ \mathbf{x} \right\}$ and $X\overset{-}{\leftarrow}\left\{ \mathbf{x} \right\}$ to compactly represent the compounding operations $X\leftarrow{X \cup \left\{ \mathbf{x} \right\}}$ and $X\leftarrow{X \smallsetminus \left\{ \mathbf{x} \right\}}$, respectively. As is customary, we take the minimum of an empty set to be infinity.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B Algorithm", "weight": 1.0} -->

[[BIT\*]](#id72.72.id72) is presented in Algs. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")--3 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"). For simplicity, we limit our discussion to a search from the start to a single goal state using an $r$-disc [[RGG]](#id59.59.id59), but the formulation is similar for searches from a goal state, with a goal set, or with a $k$-nearest [[RGG]](#id59.59.id59). The algorithm starts with a given initial state, $\mathbf{x}_{start}$, in the tree, $\mathcal{T}$, and the goal state, $\mathbf{x}_{goal}$, in the set of unconnected samples, $X_{samples}$ (Alg.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Algorithm", "weight": 1.0} -->

1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")). The tree is grown towards $\mathbf{x}_{goal}$ from $\mathbf{x}_{start}$ by processing a queue of [[RGG]](#id59.59.id59) edges, $\mathcal{Q}_{E}$. This edge queue is populated by a vertex expansion queue, $\mathcal{Q}_{V}$ (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")).

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B1 Batch creation (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

A new batch begins when the queues are empty. The samples and spanning tree are pruned of states that cannot improve the solution (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"); Alg. 3 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")). A new set of $m$ samples is then added to the [[RGG]](#id59.59.id59) from the subproblem containing a better solution (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")).

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-B1 Batch creation (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

This can be accomplished by rejection sampling or, for some cost functions, direct sampling. The vertices in the tree are labelled so that only connections to new states will be considered (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")) and requeued for expansion (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")). The radius of the underlying $r$-disc [[RGG]](#id59.59.id59) is updated to reflect its size, $q$, (Alg.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-B1 Batch creation (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")), where $\eta \geq 1$ is a tuning parameter.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-B1 Batch creation (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

{\mathbf{v} \in V} \middle| {{g_{\mathcal{T}}(\mathbf{v})} \equiv \infty} \right\}$; Algorithm 3 Prune(c ∈ missing R ≥ 0) Figure 4: An example of RRT*, Informed RRT*, FMT* (m = 2500), and BIT* run on a random ℝ2 world.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-B1 Batch creation (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

Each algorithm was run until it found a equivalent solution to FMT* (c = 1.39) regardless of homotopy class. BIT*’s use of heuristics allows it to find such a solution faster (t = 0.072s) than RRT* (t = 0.487s), FMT* (t = 0.141s) and Informed RRT* (t = 0.144s) by performing its search in a principled manner that initially investigates low-cost solutions and focuses the search for improvements. Animated results are available in the attached video.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-B2 Edge selection (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

The tree is built by processing the queue of edges, $\mathcal{Q}_{E}$, in order of increasing estimated cost of a solution constrained to pass through the edge, $(\mathbf{v},\mathbf{x})$, given the current tree, ${g_{\mathcal{T}}(\mathbf{v})} + {\hat{c}(\mathbf{v},\mathbf{x})} + {\hat{h}(\mathbf{x})}$. Ties are broken in favour of the edge with the lowest current cost-to-come to the source vertex, $g_{\mathcal{T}}(\mathbf{v})$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-B2 Edge selection (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

The cost of creating the edge queue is delayed by using a vertex expansion queue, $\mathcal{Q}_{V}$. This vertex queue is ordered on the estimated cost of a solution constrained to pass through the vertex given the current tree, ${g_{\mathcal{T}}(\mathbf{v})} + {\hat{h}(\mathbf{v})}$. This value is a lower bound estimate of the edge-queue values from a vertex; therefore, vertices only need to be expanded into the edge queue when their vertex-queue value is less than the best edge-queue value. The function ${\mathtt{B}\mathtt{e}\mathtt{s}\mathtt{t}\mathtt{I}\mathtt{n}\mathtt{Q}\mathtt{u}\mathtt{e}\mathtt{u}\mathtt{e}}\left( \mathcal{Q}_{V} \right)$ returns the best vertex in the vertex queue given this ordering.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-B2 Edge selection (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

Before selecting the next edge in the queue to process, any vertices that could have a better outgoing edge (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")) are expanded (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"); Alg. 2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")). The best edge in the queue, $\left( \mathbf{v}_{m},\mathbf{x}_{m} \right)$, is then removed for processing (Alg.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-B2 Edge selection (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")). As edges are only added to the edge queue by expanding their source vertex, and each vertex is only expanded once per batch, each edge is guaranteed to only be processed once per batch.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-B3 Edge processing (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

Heuristics are used to accelerate the processing of edges and delay the calculation of the true edge cost. The edge being processed, $\left( \mathbf{v}_{m},\mathbf{x}_{m} \right)$, is first checked to see if it can improve the current solution given the current tree (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")). If it cannot, then by construction no other edges in the queue can and both queues are cleared to start a new batch (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")).

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-B3 Edge processing (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

The true edge cost is then calculated by performing collision checks and solving any differential constraints. This may be expensive, so the edge is processed if it could *ever* improve the current solution, regardless of the current state of the tree (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")). If it cannot, than it is discarded.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-B3 Edge processing (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

Finally, the edge is checked to see if it improves the cost-to-come of its target vertex (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")), noting that disconnected vertices have an infinite cost. If it does, it is added to the tree.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-B3 Edge processing (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

If the target vertex, $\mathbf{x}_{m}$, is in the tree (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")), then the edge represents a *rewiring*, otherwise it is an *expansion*. Rewirings require removing the edge to the target vertex from the tree (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")). Expansions require moving the target vertex from the set of unconnected samples to the set of vertices and queueing it for expansion (Alg.

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-B3 Edge processing (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")).

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-B3 Edge processing (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

The new edge is then added to the tree (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")) and the edge queue is pruned to remove edges that cannot improve the cost-to-come of the vertex (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")).

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-B4 Vertex Expansion (Alg. 2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

The function, $\mathtt{E}\mathtt{x}\mathtt{p}\mathtt{a}\mathtt{n}\mathtt{d}$-${\mathtt{V}\mathtt{e}\mathtt{r}\mathtt{t}\mathtt{e}\mathtt{x}}(\mathbf{v})$, removes a vertex, $\mathbf{v} \in \mathcal{Q}_{V} \subseteq V$, from the vertex queue (Alg. 2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")) and adds outgoing edges from the vertex to the edge queue.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-B4 Vertex Expansion (Alg. 2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

In the [[RGG]](#id59.59.id59), a vertex is connected to all states within a radius, $r$. Edges to unconnected states (Alg. 2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")) are always added to edge queue if they could be part of a better solution (Alg. 2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")). Edges to connected states are only added if the source vertex was added to the tree during this batch (Alg.

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-B4 Vertex Expansion (Alg. 2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")). This prevents repeatedly checking edges between vertices in the tree. These rewiring edges (Alg. 2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")) are added to the edge queue if, in addition to possibly providing a better solution, they are not already in the tree and could improve the path to the target vertex given the current tree (Alg.

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-B4 Vertex Expansion (Alg. 2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")).

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-B5 Graph Pruning (Alg. 3 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

The function, ${\mathtt{P}\mathtt{r}\mathtt{u}\mathtt{n}\mathtt{e}}(c)$, removes states that cannot provide a solution better than the given cost, $c \in {\mathbb{R}}_{\geq 0}$. Unconnected samples are removed (Alg. 3 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 3 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")), while vertices in the tree are removed and disconnected (Alg.

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-B5 Graph Pruning (Alg. 3 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

3 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Lines 3 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")--3 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")). To maintain uniform sample density in the subproblem being searched, disconnected descendents that could still provide a better solution are returned to the unconnected sample set (Alg.

<!-- chunk {"id": "body-0057", "role": "body", "section": "III-B5 Graph Pruning (Alg. 3 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs\"))", "weight": 1.0} -->

3 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Lines 3 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")--3 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")).

<!-- chunk {"id": "body-0058", "role": "body", "section": "III-C Practical Considerations", "weight": 1.0} -->

Algs. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")--3 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs") describe [[BIT\*]](#id72.72.id72) without considering implementation, leaving room for practical improvements. Pruning (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")) is expensive and should only occur when a new solution has been found. It can even be limited to *significant* changes in solution cost without altering behaviour.

<!-- chunk {"id": "body-0059", "role": "body", "section": "III-C Practical Considerations", "weight": 1.0} -->

Searches (e.g., Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"); Alg. 2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 2 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"); Alg.

<!-- chunk {"id": "body-0060", "role": "body", "section": "III-C Practical Considerations", "weight": 1.0} -->

3 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Line 3 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"); etc.) can be implemented efficiently with appropriate datastructures, e.g., $k$-d trees or indexed containers, that do not require an exhaustive global search.

<!-- chunk {"id": "body-0061", "role": "body", "section": "III-C Practical Considerations", "weight": 1.0} -->

Ordered containers provide an efficient edge queue (Alg. 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), Lines 1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")--1 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")). While rewirings will change the order of some elements, we found little experimental difference between an approximately sorted and a strictly sorted queue.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Analysis", "weight": 1.0} -->

For brevity, we only present a proof of almost sure asymptotic optimality (Theorem 1 ‣ IV Analysis ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")) and note that this implies probabilistic completeness. We also present a discussion on the relationship between [[BIT\*]](#id72.72.id72)'s edge queue and [[LPA\*]](#id78.78.id78)'s vertex queue (Remark 1 ‣ IV Analysis ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Remark 1 (Equivalence to [[LPA\\*]](#id78.78.id78) vertex queue)", "weight": 1.0} -->

[[BIT\*]](#id72.72.id72)'s edge queue is an extension of [[LPA\*]](#id78.78.id78)'s vertex queue to include a heuristic estimate of edge cost.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 1 (Equivalence to [[LPA\\*]](#id78.78.id78) vertex queue)", "weight": 1.0} -->

Explanation: [[LPA\*]](#id78.78.id78) uses a queue of vertices ordered lexicographically first on the solution cost constrained to go through the vertex and then the cost-to-come to the vertex. Both these terms are calculated for a vertex, $\mathbf{v} \in V$, considering all the incoming edges (rhs-value in [[LPA\*]](#id78.78.id78)), i.e., where $E$ is the set of edges.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 1 (Equivalence to [[LPA\\*]](#id78.78.id78) vertex queue)", "weight": 1.0} -->

This minimum requires the calculation of the true edge cost between a vertex and all of its possible parents. This calculation is expensive in sampling-based planning (e.g., collision checking, differential constraints, etc.), and reducing its calculation is desirable. This can be done by using an admissible heuristic estimate of edge cost and calculating (2: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")) incrementally. A running minimum is calculated by processing edges in order of increasing *estimated* cost. The process finishes, and the true minimum is found, when the estimated cost through the next edge is higher than the current value. [[BIT\*]](#id72.72.id72) combines these individual minima calculations into a single edge queue. In doing so, it simultaneously calculates the minimum cost-to-come for each vertex while expanding vertices in order of increasing estimated solution cost. ∎

<!-- chunk {"id": "body-0066", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

[[BIT\*]](#id72.72.id72) was tested against existing algorithms in both simulated random worlds (Section V-A: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")) and real-world manipulation problems (Section V-B: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")) using publicly available Open Motion Planning Library ([[OMPL]](#id96.96.id96)) implementations. All tests and algorithms used an [[RGG]](#id59.59.id59) constant (e.g., $\eta$ in (1 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"))) of $1.1$ and approximated $\lambda\left( X_{free} \right)$ with $\lambda(X)$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

[[RRT]](#id88.88.id88)-based algorithms used a goal bias of $5\%$. [[BIT\*]](#id72.72.id72) used $100$ samples per batch, Euclidean distance between states for heuristics, and direct informed sampling. Graph pruning was limited to changes in the solution cost greater than $1\%$ and we used an approximately sorted queue.

<!-- chunk {"id": "body-0068", "role": "body", "section": "V-A Simulated Random Worlds", "weight": 1.0} -->

[[BIT\*]](#id72.72.id72) was compared to existing sampling-based algorithms on random problems minimizing path length in ${\mathbb{R}}^{2}$ and ${\mathbb{R}}^{8}$. The problems consisted of a (hyper)cube of width $2$ populated with random axis-aligned (hyper)rectangular obstacles such that at most one third of the environment was obstructed. The initial state was in the centre of the world and the goal was $(0.9,0.9,\ldots,0.9)$ away (Fig. 4 ‣ III-B Algorithm ‣ III Batch Informed Trees ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")).

<!-- chunk {"id": "body-0069", "role": "body", "section": "V-A Simulated Random Worlds", "weight": 1.0} -->

[[BIT\*]](#id72.72.id72) was compared to the [[OMPL]](#id96.96.id96) implementations of [[RRT]](#id88.88.id88), [[RRT]](#id88.88.id88)-Connect, [[RRT\*]](#id90.90.id90), Informed [[RRT\*]](#id90.90.id90), and [[FMT\*]](#id76.76.id76). The [[RRT]](#id88.88.id88)-based planners used a maximum edge length of $0.2$ and $1.25$ in ${\mathbb{R}}^{2}$ and ${\mathbb{R}}^{8}$, respectively. All algorithm parameters were chosen in good faith to maximize performance on a separate training set of random worlds.

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-A Simulated Random Worlds", "weight": 1.0} -->

For each state dimension, $10$ different random worlds were generated and the planners were tested with $50$ different pseudo-random seeds on each. The solution cost of each planner was recorded every $1$ millisecond by a separate thread^11^1Simulations were run on a MacBook Pro with $4$ GB of RAM and an Intel i7-620M processor running a $64$-bit version of Ubuntu 12.04.. For each world, median solution cost was calculated for a planner by interpolating each trial at a period of $1$ millisecond. As the true optima for these problems are different and unknown, there is no meaningful way to compare the results across problems. Instead, results from a representative problem are presented in Fig. 5 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), where the percent of trials solved and the median solution cost are plotted versus computational time.

<!-- chunk {"id": "body-0071", "role": "body", "section": "V-A Simulated Random Worlds", "weight": 1.0} -->

These experiments show that in both ${\mathbb{R}}^{2}$ (Figs. 5 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")a, 5 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")c) and ${\mathbb{R}}^{8}$ (Figs. 5 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")b, 5 ‣ Batch Informed Trees (BIT*): Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")d), [[BIT\*]](#id72.72.id72) generally finds better solutions faster than other sampling-based optimal planners and [[RRT]](#id88.88.id88). It has a higher likelihood of having found a solution at a given computational time than these planners, and converges faster towards the optimum.

<!-- chunk {"id": "body-0072", "role": "body", "section": "V-A Simulated Random Worlds", "weight": 1.0} -->

The only planner tested that found solutions faster than [[BIT\*]](#id72.72.id72) was [[RRT]](#id88.88.id88)-Connect, a nonasymptotically optimal planner.

<!-- chunk {"id": "body-0073", "role": "body", "section": "V-B Motion Planning for Manipulation", "weight": 1.0} -->

To evaluate the performance of [[BIT\*]](#id72.72.id72) on real-world high-dimensional problems, it was tested on [[HERB]](#id93.93.id93). Experiments consisted of both dual-arm and one-arm planning problems for manipulation with a goal of minimizing the path length through configuration space. Parameter values for [[BIT\*]](#id72.72.id72) and [[RRT]](#id88.88.id88)-based planners were chosen from the results of Section V-A: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs"), and the number of [[FMT\*]](#id76.76.id76) samples was chosen to use the majority of the available computational time. Once again, [[BIT\*]](#id72.72.id72) outperformed all planners other than [[RRT]](#id88.88.id88)-Connect.

<!-- chunk {"id": "body-0074", "role": "body", "section": "V-B Motion Planning for Manipulation", "weight": 1.0} -->

For the dual-arm planning problem, [[HERB]](#id93.93.id93) started with both arms extended under a table from the elbow onward. The task was to plan a trajectory for both arms to place the hands in position to open a bottle (Fig. 1: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")). [[HERB]](#id93.93.id93)'s proximity to the table and starting position created a narrow passage for the arms around the table. Coupled with the $14$- degree-of-freedom ([[DOF]](#id32.32.id32)) configuration space, this made for a challenging problem.

<!-- chunk {"id": "body-0075", "role": "body", "section": "V-B Motion Planning for Manipulation", "weight": 1.0} -->

Given $2.5$ minutes^22^2[[HERB]](#id93.93.id93) experiments were run on a Dell T3500 with $12$ GB of RAM and an Intel W3565 processor running a $64$-bit version of Ubuntu 12.04. of planning time, [[BIT\*]](#id72.72.id72) was almost twice as likely to find a solution than [[RRT]](#id88.88.id88), Informed [[RRT\*]](#id90.90.id90), or [[FMT\*]](#id76.76.id76). Over $25$ trials, [[BIT\*]](#id72.72.id72) was $68\%$ successful with a median solution cost of $17.4$. [[RRT]](#id88.88.id88)-Connect was $100\%$ successful, but had a median solution cost of $22.1$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "V-B Motion Planning for Manipulation", "weight": 1.0} -->

[[RRT]](#id88.88.id88) was $8\%$ successful with a median solution cost of $31.1$ and Informed [[RRT\*]](#id90.90.id90) was $8\%$ successful with a median solution cost of $25.3$. [[FMT\*]](#id76.76.id76) with $m = 500$ was $36\%$ successful with a median solution cost of $17.2$. All [[RRT]](#id88.88.id88)-based planners used a maximum edge length of $3$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "V-B Motion Planning for Manipulation", "weight": 1.0} -->

An easier one-arm planning problem was also tested. [[HERB]](#id93.93.id93) started with its left arm folded at the elbow and held at approximately the table level of a table. The task was to plan a trajectory to place the left hand in position to grasp a box (Fig. 6: Sampling-based Optimal Planning via the Heuristically Guided Search of Implicit Random Geometric Graphs")). The smaller configuration space, $7$ [[DOF]](#id32.32.id32), and a starting position partially clear of the table made this an easier planning problem. In the given $5$ seconds of computational time, both [[BIT\*]](#id72.72.id72) and [[RRT]](#id88.88.id88)-Connect found a solution in all $25$ trials.

<!-- chunk {"id": "body-0078", "role": "body", "section": "V-B Motion Planning for Manipulation", "weight": 1.0} -->

[[BIT\*]](#id72.72.id72) had a median solution cost of $6.8$ while [[RRT]](#id88.88.id88)-Connect had a median solution cost of $10.6$. [[RRT]](#id88.88.id88) was $88\%$ successful with a median solution cost of $11.2$ and Informed [[RRT\*]](#id90.90.id90) was $88\%$ successful with a median solution cost of $10.6$. [[FMT\*]](#id76.76.id76) with $m = 50$ was $52\%$ successful with a median solution cost of $9.0$. All [[RRT]](#id88.88.id88)-based planners used a a maximum edge length of $1.25$.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Discussion & Future Work", "weight": 1.5} -->

[[BIT\*]](#id72.72.id72) demonstrates that anytime sampling-based planners can be designed by combining incremental graph-search techniques with [[RGG]](#id59.59.id59) theory. We hope that this work will motivate further unification of these two planning paradigms.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Discussion & Future Work", "weight": 1.5} -->

A fundamental component of [[BIT\*]](#id72.72.id72) is the application of heuristic estimates to *all* aspects of path cost. Doing so allows the algorithm to account for future graph improvements (cost-to-come), avoid unnecessary collision checks and boundary-value problems (edge cost), and order and focus the search (solution cost). As always, the benefit of these heuristics will depend on their suitability for the specific problem, but we feel that they are an important tool to reduce the curse of dimensionality. Note that while direct sampling of the subproblem is possible for some cost functions, rejection sampling is applicable. Also note that, as with other heuristically guided searches (e.g., A\*), [[BIT\*]](#id72.72.id72) works with the trivial *zero* heuristic (e.g., Dijkstra's algorithm); however, more conservative heuristics provide less benefit to the search.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Discussion & Future Work", "weight": 1.5} -->

In describing [[BIT\*]](#id72.72.id72) as an extension of [[LPA\*]](#id78.78.id78) to continuous planning problems, it is important to note a key difference in how they reuse information. In [[LPA\*]](#id78.78.id78), updating the cost-to-come of a vertex requires reconsidering the cost-to-come of all possibly descendent vertices. This is a step that becomes prohibitively expensive in anytime resolution planners as graph size increases quickly. The results of [[RRT\*]](#id90.90.id90) demonstrate that this is unnecessary for the planner to almost surely converge asymptotically to the optimum as the number of samples approaches infinity.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Discussion & Future Work", "weight": 1.5} -->

While the efficiency of graph-search techniques is well understood, this area remains understudied for sampling-based planners. We are actively investigating whether [[BIT\*]](#id72.72.id72)'s use of graph-search techniques and [[RGG]](#id59.59.id59) theory can be used to probabilistically evaluate its efficiency.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Discussion & Future Work", "weight": 1.5} -->

Also of interest are possible improvements to [[BIT\*]](#id72.72.id72), including the fact that [[BIT\*]](#id72.72.id72) does not remove samples when connection attempts fail. This is a requirement of the uniform sample distribution used in [[RGG]](#id59.59.id59) theory, but leaves edges in the implicit [[RGG]](#id59.59.id59) that are known to be unusable.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Discussion & Future Work", "weight": 1.5} -->

Finding an efficient method to avoid these edges would improve [[BIT\*]](#id72.72.id72), and there are multiple potential ways to accomplish this. Failed edges could be tracked and prevented from reentering the queue, but initial attempts have proven too computational expensive. Samples that fail multiple connection attempts could be removed, but doing so will require [[RGG]](#id59.59.id59) theory for nonuniform distributions. Our current focus is on the adaptively varying batch size to increase the rate at which these edges are removed from the [[RGG]](#id59.59.id59).

<!-- chunk {"id": "body-0085", "role": "body", "section": "Discussion & Future Work", "weight": 1.5} -->

We are also interested in more general extensions to [[BIT\*]](#id72.72.id72). Its expanding search is well suited for large or unbounded planning problems, and we have had initial success with a version that generates samples as needed and avoids the a priori definition of state space limits. Its relationship to incremental search techniques also suggests it may be well suited for planning problems in changing environments. We are also investigating the use of other graph-search techniques, including anytime or bidirectional searches to decrease the time required to find an initial solution. Finally, we are investigating combining [[BIT\*]](#id72.72.id72)'s global search with local searches, such as path-smoothing.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we attempt to unify graph-search and sampling-based planning techniques through [[RGG]](#id59.59.id59) theory. By recognizing that a set of samples defines an implicit [[RGG]](#id59.59.id59) and using incremental-search techniques, we are able to combine the efficient search of algorithms such as A\*, with the anytime scalability of sampling-based algorithms such as [[RRT\*]](#id90.90.id90). The resulting algorithm, [[BIT\*]](#id72.72.id72), uses heuristics for all aspects of path cost in order to prioritize the search of high-quality paths and focus the search for improvements.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Conclusion", "weight": 1.5} -->

As demonstrated on both simulated and real-world experiments, [[BIT\*]](#id72.72.id72) outperforms existing sampling-based optimal planners and [[RRT]](#id88.88.id88), especially in high dimensions. For a given computational time, [[BIT\*]](#id72.72.id72) has a higher likelihood of finding a solution and generally finds solutions of equivalent quality sooner. It also converges towards the optimum faster than other asymptotic optimal planners, and has recently been shown to perform well on problems with differential constraints. Information on the [[OMPL]](#id96.96.id96) implementation of [[BIT\*]](#id72.72.id72) is available at
