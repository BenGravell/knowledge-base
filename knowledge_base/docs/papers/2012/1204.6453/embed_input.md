<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Role of Vertex Consistency in Sampling-based Algorithms for Optimal Motion Planning

Topics include Motion planning, Optimal motion planning, Sampling-based planning, Asymptotic optimality, Rapidly-exploring random tree sharp, Rapidly-exploring random tree star, Rapidly-exploring random tree, RRG, Graph search, Dynamic programming, Vertex consistency, Consistent tree.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

RRT# is based on RRG, just like RRT*, but is aimed at obtaining faster convergence to the optimal cost compared to RRT* by maintaining better estimates of nodal costs. There is also some interesting commentary in Section 5 of the arXiv preprint where the authors discuss the "relevant region" as an elliptic region which could be "used to implement more intelligent sampling strategies"; it would seem this idea was picked up on and formalized by Gammell et al. in the "Informed RRT*" paper.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Several variants of incremental sampling-based algorithms have been recently proposed in order to optimally solve motion planning problems. Popular examples include the RRT* and the PRM* algorithms. These algorithms are asymptotically optimal and thus provide high quality solutions. However, the convergence rate to the optimal solution may still be slow. Borrowing from ideas used in the well-known LPA* algorithm, in this paper we present a new incremental sampling-based motion planning algorithm based on Rapidly-exploring Random Graphs (RRG), denoted by RRT# (RRT "sharp"), which also guarantees asymptotic optimality, but, in addition, it also ensures that the constructed spanning tree rooted at the initial state contains lowest-cost path information for vertices which have the potential to be part of the optimal solution. This implies that the best possible solution is readily computed if there are some vertices in the current graph that are already in the goal region.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning problems are crucial for the realization of truly autonomous vehicles and robots. Many approaches have been proposed in the literature (see for example, the excellent books by LaValle and Choset et al ). A bottleneck in most motion planning problems, especially those involving systems with high state dimensionality, is the computational overhead associated with discretizing (i.e., gridding) the state space. Hence, deterministic searches are impractical for high dimensional state spaces. Probabilistic roadmap methods, \[1, Ch. 7\], as well as methods that use rapidly exploring random trees (RRTs), are among the most popular. They can address the vehicle's kinematic and dynamic constraints during motion planning in high dimensional state spaces. In these methods, random samples of the obstacle-free space are connected to each other by feasible trajectories, and the resulting graph is searched for a sequence of connected samples from the initial state to the goal state. Sampling-based algorithms require efficient low-level collision detection and trajectory planning algorithms to find collision-free trajectories between different samples.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Incremental sampling-based algorithms were first proposed by Kavraki during the late 1990s. The so-called Probabilistic Road Map ($PRM$) was successfully implemented to solve multi-query motion planning problems and gained a lot of attention, both in industry and academia. In $PRM$ a graph of the environment is constructed by taking random samples from the configuration space of the robot and testing them to determine whether they belong to the free space. The $PRM$ algorithm uses a local planner that attempts to find a feasible path between the sampled points. Once a reasonable graph is constructed, the initial and the goal states are added to the graph, and the optimal path is computed using a graph search algorithm.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another important class of incremental sampled-based motion planning algorithm is the Rapidly-exploring Random Tree ($RRT$) and its numerous variants. RRTs have achieved great success in solving single-query motion planning problems in many real-time applications. However, the quality of RRT-based algorithms is often poor (i.e., highly suboptimal). As a result, a lot of effort has been devoted to the development of heuristic techniques in order to refine the quality of the solution obtained from RRTs. However, it has been recently shown that the best path returned by RRTs when the algorithm converges is almost always (i.e., with probability one) far from optimal. This has renewed the interest to develop incremental sampled-based algorithms for motion-planning problems with optimality guarantees. In the authors proposed the Rapidly-exploring Random Graphs ($RRG$) algorithm, which has asymptotic optimality properties, that is, it ensures that the optimal path will be found as the number of samples tends to infinity.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Based on $RRG$, the same authors later proposed a new algorithm, namely ${RRT}^{\ast}$ that extracts a tree from the graph constructed by $RRG$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we present a new incremental sampling-based motion planning algorithm based on $RRG$, denoted ${RRT}^{\#}$(RRT "sharp"), which also guarantees asymptotic optimality but, in addition, it also ensures that, at each step, the constructed spanning tree of the graph is consistent. Vertex consistency (see Section 2) implies that the accumulated cost-to-come of each vertex equals to the optimal cost-to-come. This allows us classify the vertices according to their potential of being part of the optimal path, and thus to quickly identify the region where the optimal solution is more likely to be found. This information can be subsequently used to improve the speed of convergence of the standard ${RRT}^{\ast}$ algorithm, as well as in order to more efficiently explore the obstacle-free space. Three variants of the baseline ${RRT}^{\#}$ algorithm are proposed that take advantage of this vertex classification to speed up convergence.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The organization of the paper is as follows: The problem formulation is given in the next section. In Section 3, an overview of the ${RRT}^{\#}$ algorithm is introduced. The fundamental concepts and primitive functions used in the ${RRT}^{\#}$ algorithm are explained. In Section 4, each step of the proposed approach is explained in detail, along with the pseudo-code of the algorithm and the main procedures used in the main algorithm. In Sections 5, simulation results are used to compare the solutions of the proposed approach with the well-known ${RRT}^{\ast}$ algorithm. In Section 6, several variants of the baseline algorithm are presented by using simple vertex rejection techniques and improvements are demonstrated by doing extensive simulations in the subsequent section. We conclude the paper with some possible extensions for future work.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

The proposed ${RRT}^{\#}$ algorithm solves the following motion planning problem: Given a bounded and connected open set $\mathcal{X} \subset {\mathbb{R}}^{d}$, and the sets $\mathcal{X}_{free}$ and $\mathcal{X}_{obs} = {\mathcal{X}\backslash\mathcal{X}_{free}}$, and given an initial point $x_{init} \in \mathcal{X}_{free}$ and a goal region $\mathcal{X}_{goal} \subset \mathcal{X}_{free}$, find the minimum-cost path connecting $x_{init}$ to the goal region $\mathcal{X}_{goal}$. If no such path exists, then report that no solution is possible.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Overview", "weight": 1.0} -->

A brief description of each function used in the ${RRT}^{\#}$ algorithm is given below.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Overview", "weight": 1.0} -->

*Sampling*: ${\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}}:{{\mathbb{N}}\rightarrow\mathcal{X}_{free}}$ is a function that returns independent, identically distributed (i.i.d) samples from $\mathcal{X}_{free}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Overview", "weight": 1.0} -->

*Nearest neighbor*: $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{s}\mathtt{t}$ is a function that returns a point from a given finite set $V$, which is the closest to a given point $x$ in terms of a given distance function.

<!-- chunk {"id": "body-0014", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Overview", "weight": 1.0} -->

*Near vertices*: $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}$ is a function that returns $n$ number of points from a given finite set $V$, which is the closest to a given point $x$ in terms of a given distance function.

<!-- chunk {"id": "body-0015", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Overview", "weight": 1.0} -->

*Steering*: $\mathtt{S}\mathtt{t}\mathtt{e}\mathtt{e}\mathtt{r}$ is a function that returns the closest point in a ball centered around a given state $x$ to another given point $x_{new}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Overview", "weight": 1.0} -->

*Collision checking*: Given two points, the Boolean function $\mathtt{O}\mathtt{b}\mathtt{s}\mathtt{t}\mathtt{a}\mathtt{c}\mathtt{l}\mathtt{e}\mathtt{F}\mathtt{r}\mathtt{e}\mathtt{e}$ checks whether the minimum distance path connecting these two points belongs to $\mathcal{X}_{free}$. It returns $\mathtt{T}\mathtt{r}\mathtt{u}\mathtt{e}$ if the line segment is a subset of the $\mathcal{X}_{free}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Overview", "weight": 1.0} -->

*Tree extension*: $\mathtt{E}\mathtt{x}\mathtt{t}\mathtt{e}\mathtt{n}\mathtt{d}$ is a function that extends the nearest vertex of the tree $\mathcal{T}$ towards the randomly sampled point $x_{rand}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Overview", "weight": 1.0} -->

${\mathtt{R}\mathtt{e}\mathtt{d}\mathtt{u}\mathtt{c}\mathtt{e}\mathtt{I}\mathtt{n}\mathtt{c}\mathtt{o}\mathtt{n}\mathtt{s}\mathtt{i}\mathtt{s}\mathtt{t}\mathtt{e}\mathtt{n}\mathtt{c}\mathtt{y}}:{{(\mathcal{G},\mathcal{T},\mathcal{X}_{goal})}\mapsto{(\mathcal{G},\mathcal{T}')}}$ operates on the inconsistent vertices of the tree $\mathcal{T}$ iteratively, and continues until the tree becomes consistent, that is, all vertices of the tree that are promising (see Section 4) are consistent.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Overview", "weight": 1.0} -->

The $\mathtt{R}\mathtt{e}\mathtt{d}\mathtt{u}\mathtt{c}\mathtt{e}\mathtt{I}\mathtt{n}\mathtt{c}\mathtt{o}\mathtt{n}\mathtt{s}\mathtt{i}\mathtt{s}\mathtt{t}\mathtt{e}\mathtt{n}\mathtt{c}\mathtt{y}$ function is used to propagate the effects of the topological changes in the graph $\mathcal{G}$ as new vertices are added with each iteration.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Overview", "weight": 1.0} -->

A priority queue is used to sort all of the inconsistent vertices of the tree $\mathcal{T}$ based on their respective key values. The following functions are defined to manage the priority queue.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Overview", "weight": 1.0} -->

*Update queue*: Given a vertex $v \in V$, the function $\mathtt{U}\mathtt{p}\mathtt{d}\mathtt{a}\mathtt{t}\mathtt{e}\mathtt{Q}\mathtt{u}\mathtt{e}\mathtt{u}\mathtt{e}$ changes the content of the queue based on the g- and lmc-values of the vertex $v$. If the vertex $v$ is inconsistent, then it is either inserted into the queue or its priority in the queue is updated based on its up-to-date key value if it is already inside the queue. Otherwise, the vertex is removed from the queue if it is a consistent vertex.

<!-- chunk {"id": "body-0022", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Overview", "weight": 1.0} -->

*Find minimum*: The function $findmin{}$ returns the vertex with the highest priority of all vertices in the queue, i.e., the vertex of minimum key value.

<!-- chunk {"id": "body-0023", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Overview", "weight": 1.0} -->

*Remove a vertex*: Given a vertex $v \in V$, the function $remove{}$ deletes the vertex $v$ from content of the queue.

<!-- chunk {"id": "body-0024", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Overview", "weight": 1.0} -->

*Update priority*: Given a vertex $v \in V$, and a key value $k$, the function $update{}$ changes the priority of the vertex $v$ in priority queue $q$, i.e., it reassigns the key value of the vertex $v$ with the new given key value $k$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Overview", "weight": 1.0} -->

*Inserting a vertex*: Given a vertex $v \in V$, and a key $k$, the function $insert{}$ adds the vertex $v$ with the key value $k$ into queue.

<!-- chunk {"id": "body-0026", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Details", "weight": 1.0} -->

The body of the ${RRT}^{\#}$ algorithm is given in Algorithm 1 and it is similar to the other RRT-variants ($RRT$, $RRG$, ${RRT}^{\ast}$, etc) with the notable exception that it keeps track of vertex consistency using the key values of all current vertices in the graph. One of the important difference between the ${RRT}^{\ast}$ and ${RRT}^{\#}$ algorithms is that all vertices in the tree computed by the ${RRT}^{\ast}$ algorithm have a uniform type based on their finite cost-to-come value, whereas in the ${RRT}^{\#}$ algorithm the vertices have different types based on their pair of estimates of the cost-to-come value.

<!-- chunk {"id": "body-0027", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Details", "weight": 1.0} -->

In the ${RRT}^{\#}$ algorithm, each vertex $v$ can be classified in one of the following four categories based on the values of its $({\mathtt{g}{(v)}},{{\mathtt{l}\mathtt{m}\mathtt{c}}{(v)}})$ pair.

<!-- chunk {"id": "body-0028", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Details", "weight": 1.0} -->

4 RRT#(xinit, 𝒳goal, 𝒳) Algorithm 1 Body of the RRT# Algorithm The algorithm starts by adding the initial point $x_{init}$ into the vertex set of the underlying graph. Then, it incrementally grows the graph in $\mathcal{X}_{free}$ by sampling a random point $x_{rand}$ from $\mathcal{X}_{free}$ and extending some parts of the graph towards $x_{rand}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Details", "weight": 1.0} -->

Later, the $\mathtt{R}\mathtt{e}\mathtt{d}\mathtt{u}\mathtt{c}\mathtt{e}\mathtt{I}\mathtt{n}\mathtt{c}\mathtt{o}\mathtt{n}\mathtt{s}\mathtt{i}\mathtt{s}\mathtt{t}\mathtt{e}\mathtt{n}\mathtt{c}\mathtt{y}$ procedure, which is provided in Algorithm 3, propagates the new information due to the extension across the whole graph in order to improve the estimate of the cost-to-come value of the promising vertices in the graph. All computations due to the sampling and extension steps, followed by information propagation (Lines 1-1 of Algorithm 1), form a single *iteration* of the algorithm. The process is repeated for a given fixed number of iterations, and the consistent spanning tree of the final graph is returned at the end.

<!-- chunk {"id": "body-0030", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Details", "weight": 1.0} -->

The key difference between the ${RRT}^{\#}$ algorithm and other RRT-variants is that a unique consistent spanning tree of the graph is maintained at the end of the each iteration of the algorithm. Since this tree is consistent, it contains information of the lowest-cost path, which can be achieved on the current graph, for each promising vertex of the graph. In addition, the g-value of the promising vertices equals to their respective optimal cost-to-come value that can be achieved through the edges of the tree. Therefore, each new vertex is initialized with the minimum possible estimate of its respective optimal cost-to-come value during extension (since all of its promising neighbor vertices have the lowest g-value), and this estimate keeps improving to the best possible value whenever new information becomes available on any part of the graph. Hence, the g-value of each promising vertex of the graph converges to its optimal cost-to-come value very quickly.

<!-- chunk {"id": "body-0031", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Details", "weight": 1.0} -->

9 xnew ← Steer (xnearest, x); 10 if (xnearest, xnew) then 12 lmc (xnew) = g (xnearest) + c (xnearest, xnew); 13 parent (xnew) = xnearest; 14 𝒳near ← Near (𝒢, xnew, |V|); 15 foreach xnear ∈ 𝒳near do 16 if (xnear, xnew) then 17 if (xnew) > (xnear) + (xnear, xnew) then 18 lmc (xnew) = g (xnear) + c (xnear, xnew); 19 parent (xnew) = xnear; 21 E′ ← E′ ∪ {(xnear, xnew), (xnew, xnear)}; Algorithm 2 Extend Procedure for RRT# Algorithm The $\mathtt{E}\mathtt{x}\mathtt{t}\mathtt{e}\mathtt{n}\mathtt{d}$ procedure for the

<!-- chunk {"id": "body-0032", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Details", "weight": 1.0} -->

${RRT}^{\#}$ algorithm is given in Algorithm 2. During each iteration, the $\mathtt{E}\mathtt{x}\mathtt{t}\mathtt{e}\mathtt{n}\mathtt{d}$ procedure tries to extend the graph towards the randomly sampled point $x_{rand} \in \mathcal{X}_{free}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Details", "weight": 1.0} -->

First, the closest vertex in the graph $x_{nearest}$ is found in Line 3, then $x_{nearest}$ is steered towards the randomly sampled point $x_{rand}$ in the next line. If the line segment connecting the steered point $x_{new}$ and $x_{nearest}$ is feasible, then the new point $x_{new}$ is prepared for inclusion to the vertex set of the graph. First, its cost-to-come estimate, i.e., the g-value and lmc-values, and the parent vertex are initialized by using information of the nearest vertex $x_{nearest}$. Then, a local search is performed in some neighborhood of $x_{new}$, i.e., the set of vertices returned by the $\mathtt{N}\mathtt{e}\mathtt{a}\mathtt{r}$ procedure, in order to find the local minimum cost-to-come estimate value in Lines 10-15 and the corresponding parent vertex.

<!-- chunk {"id": "body-0034", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Details", "weight": 1.0} -->

The new vertex $x_{new}$ and all extensions resulting in feasible trajectories are added to the vertex and edge set of the graph in Lines 16-17, respectively. In the end, the new vertex is decided to be inserted in the priority queue or not based on its consistency in the $\mathtt{U}\mathtt{p}\mathtt{d}\mathtt{a}\mathtt{t}\mathtt{e}\mathtt{Q}\mathtt{u}\mathtt{e}\mathtt{u}\mathtt{e}$ procedure.

<!-- chunk {"id": "body-0035", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Details", "weight": 1.0} -->

Algorithm 3 ReduceInconsistency Procedure 13 else if (x) ≠ (x) and x ∉ q then 15 else if (x) = (x) and x ∈ q then 22 gmin = min (g (x), lmc (x)); Algorithm 4 Auxiliary Procedures Inclusion of each new vertex may result in an inconsistent vertex in the graph if a finite lmc-value is achieved. Therefore, consistency of the spanning tree needs to be checked, and appropriate operations must be performed in order to make it consistent, if necessary.

<!-- chunk {"id": "body-0036", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Details", "weight": 1.0} -->

The $\mathtt{R}\mathtt{e}\mathtt{d}\mathtt{u}\mathtt{c}\mathtt{e}\mathtt{I}\mathtt{n}\mathtt{c}\mathtt{o}\mathtt{n}\mathtt{s}\mathtt{i}\mathtt{s}\mathtt{t}\mathtt{e}\mathtt{n}\mathtt{c}\mathtt{y}$ procedure, which is provided in Algorithm 3, is called to make the spanning tree consistent by operating on the inconsistent and promising vertices of the graph, iteratively. It simply pops the most promising inconsistent vertex from the priority queue, if there are any, and this inconsistent vertex is made consistent by assigning its lmc-value to its g-value. Then, its new g-value information is propagated among its neighbors in order to improve their lmc-values in Lines 7-11. However, this information propagation may also cause some vertices to be inconsistent; therefore, all resulting inconsistent vertices are inserted in the priority queue as well.

<!-- chunk {"id": "body-0037", "role": "body", "section": "The ${RRT}^{\\#}$ Algorithm - Details", "weight": 1.0} -->

This process continues until a consistent spanning tree is computed, that is, there is no inconsistent promising vertex left in the priority queue.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Numerical Simulations 1", "weight": 1.0} -->

The ${RRT}^{\#}$ algorithm was developed in C++ and run on a computer with a 2.40 GHz processor and 12GB RAM running the Ubuntu 11.10 Linux operating system. A Fibonacci heap was implemented as priority queue to store inconsistent vertices during the search. Extensive simulations were run to compare the performance of the ${RRT}^{\#}$ algorithm with the ${RRT}^{\ast}$ algorithm, whose C implementation is available to download from the ${RRT}^{\ast}$ authors' website.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Numerical Simulations 1", "weight": 1.0} -->

Both ${RRT}^{\#}$ and ${RRT}^{\ast}$ algorithms were run on three different problem types with the same sample sequence in order to demonstrate the difference in their behavior while growing the tree. All problems tested require finding an optimal path in a square environment minimizing the Euclidean path length. The heuristic value of a vertex is the Euclidean distance from the vertex to the goal. In the first problem type, there are no obstacles in the environment, whereas there are some box-like obstacles in the second and third problem types. In the third problem type, the environment is more cluttered than the one in the second problem type, containing many widely distributed small obstacles.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Numerical Simulations 1", "weight": 1.0} -->

For the first problem type, the trees computed by both algorithms at different stages are shown in Figure 1. The initial state is plotted as a yellow square and the goal region is shown in blue with magenta border (upper right). The minimal-length path is shown in red. As shown in Figure 1, the best path computed by the ${RRT}^{\#}$ algorithm converges to the optimal path. As mentioned earlier, one of the important differences between the ${RRT}^{\ast}$ and ${RRT}^{\#}$ algorithms is that the latter classifies the vertices in one of the following four categories based on the values of its $({\mathtt{g}{(v)}},{{\mathtt{l}\mathtt{m}\mathtt{c}}{(v)}})$ pair: Consistent with finite key value (shown in green), consistent with infinite key value (shown in black), inconsistent with finite key value (shown in blue), and inconsistent with infinite g-value and finite lmc-value (shown in red).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Numerical Simulations 1", "weight": 1.0} -->

Since only the points in the relevant region $\mathcal{X}_{rel}$ have the potential to be part of the optimal path, the ${RRT}^{\#}$ algorithm tries to approximate $\mathcal{X}_{rel}$ with the set of promising vertices $V_{prom}$ and tends to stop rewiring the parts of the tree which lie outside of the $\mathcal{X}_{rel}$ as iterations go to infinity. As seen in Figure 1, for this particular scenario, $\mathcal{X}_{rel}$ is an elliptic region, which is much smaller than the whole $\mathcal{X}_{free}$. Therefore, uniform random sampling on $\mathcal{X}_{free}$ results in too many vertices of different types (green, black, red, and blue vertices) outside of the relevant region during the search. The estimate of $\mathcal{X}_{rel}$ can be used to implement more intelligent sampling strategies, if needed, although this possibility was not pursued in this paper, where all sampling was uniform.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Numerical Simulations 1", "weight": 1.0} -->

In the second problem type, the same experiment was carried out and both algorithms were run in an environment with several obstacles. The configuration of the trees for both the ${RRT}^{\ast}$ and ${RRT}^{\#}$ algorithms at different stages are shown in Figure 3.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Numerical Simulations 1", "weight": 1.0} -->

In the third problem type, both algorithms were run in a more cluttered environment, where there are many different homotopy classes containing the local minimum solution for the problem. As shown in Figure 5, both algorithms switch between paths which have locally best cost, eventually converging to the optimal solution.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Numerical Simulations 1", "weight": 1.0} -->

Finally, in the fourth problem type, both algorithms were run in a obstacle-free environment where there are different cost zones. The cost coefficient of each zone from top to bottom is 1.5, 0.75, 2.5, 0.75, and 1.5, respectively and 1 elsewhere. As seen in Figure 7, both algorithms compute the optimal path which has longer segments in low-cost zones.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Variants of the ${RRT}^{\\#}$ Algorithm", "weight": 1.0} -->

Too many non-promising vertices are included in the tree computed by the ${RRT}^{\#}$ algorithm as observed in the previous simulations. This is owing to the fact that the ${RRT}^{\#}$ algorithm includes all new vertices in the graph regardless of their type. A simple vertex selection criterion can be used in the $\mathtt{E}\mathtt{x}\mathtt{t}\mathtt{e}\mathtt{n}\mathtt{d}$ procedure in order to prevent the algorithm from growing the tree towards the region outside $\mathcal{X}_{rel}$. However, being over-selective on vertex inclusion may degrade the performance of the algorithm -- and thus lead to a suboptimal solution -- since the cost-to-come value of all vertices, which is used to decide if a new vertex is promising or not, is an estimate of the optimal one.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Variants of the ${RRT}^{\\#}$ Algorithm", "weight": 1.0} -->

In this section, we propose three variants of the baseline ${RRT}^{\#}$ algorithm.:: In the first variant, which is given in Algorithm 5, if a new vertex happens to be consistent with infinite key value (black vertex), it is not included in the graph. This situation can happen if all of the neighbor vertices of the new vertex happen to be inconsistent with infinite g-value and finite lmc-value (red vertices). First, the estimates of the cost-to-come-value of the new vertex $x_{new}$ are initialized with infinite cost, and its parent vertex is set to 'null' in Line 6. Then, a better value for the lmc-value of the new vertex is searched among its neighbor vertices.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Variants of the ${RRT}^{\\#}$ Algorithm", "weight": 1.0} -->

During this search, the parent of the new vertex remains unassigned only if there are no any neighboring vertices with finite g-value.:: In the second variant, the algorithm becomes more selective on vertices to be added to the graph and the "${{\mathtt{p}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{n}\mathtt{t}}{(x_{new})}} \neq {\varnothing \land {{\mathtt{K}\mathtt{e}\mathtt{y}}{({{\mathtt{p}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{n}\mathtt{t}}{(x_{new})}})}}} \prec {{\mathtt{K}\mathtt{e}\mathtt{y}}{(x_{goal}^{\ast})}}$" condition is checked in Line 5. Simply, a new vertex is included to the graph only if its parent is a promising

<!-- chunk {"id": "body-0048", "role": "body", "section": "Variants of the ${RRT}^{\\#}$ Algorithm", "weight": 1.0} -->

vertex.:: Lastly, the third variant is most selective on vertex for inclusion and ${{\mathtt{K}\mathtt{e}\mathtt{y}}{(x_{new})}} \prec {{\mathtt{K}\mathtt{e}\mathtt{y}}{(x_{goal}^{\ast})}}$ condition is checked, that is, only promising new vertices are included in the graph.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Variants of the ${RRT}^{\\#}$ Algorithm", "weight": 1.0} -->

9 xnew ← Steer (xnearest, x); 10 if (xnearest, xnew) then 12 𝒳near ← Near (𝒢, xnew, |V|); 13 foreach xnear ∈ 𝒳near do 14 if (xnear, xnew) then 15 if (xnew) > (xnear) + (xnear, xnew) then 16 lmc (xnew) = g (xnear) + c (xnear, xnew); 17 parent (xnew) = xnear; 19 E′ ← E′ ∪ {(xnear, xnew), (xnew, xnear)}; Algorithm 5 Extend Procedure for RRTV 1#Algorithm

<!-- chunk {"id": "body-0050", "role": "body", "section": "Numerical Simulations 2", "weight": 1.0} -->

The same experiments as before were carried out for the three variants of the ${RRT}^{\#}$ algorithm. As seen in the figures below, all variants successfully prevent the inclusion of vertices which lie in the unfavorable regions of the search space. As seen in Figures 9, 12, 15, and 18, the ${RRT}_{V1}^{\#}$ algorithm does not include any black vertices in the tree (these are the vertices that are consistent with infinite key value, hence non-promising), but still computes a solution to the problem, which is as good as the one computed by the ${RRT}^{\ast}$ and ${RRT}^{\#}$ algorithms. However, there are still many red (i.e., non-promising and inconsistent with infinite g-value and finite lmc-value) vertices included in the tree. This is owing to the fact that they are never made consistent until the last iteration, since they mostly lie outside of $\mathcal{X}_{rel}$. Therefore, they remain in the priority queue and need to be sorted during each iteration.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Numerical Simulations 2", "weight": 1.0} -->

This makes the $\mathtt{R}\mathtt{e}\mathtt{d}\mathtt{u}\mathtt{c}\mathtt{e}\mathtt{I}\mathtt{n}\mathtt{c}\mathtt{o}\mathtt{n}\mathtt{s}\mathtt{i}\mathtt{s}\mathtt{t}\mathtt{e}\mathtt{n}\mathtt{c}\mathtt{y}$ procedure slower. In the ${RRT}_{V2}^{\#}$ algorithm, the number of red vertices included into the tree is reduced by simply enforcing to have a promising parent vertex for the new vertex that is considered for extension. Red vertices are mostly included into the branches of the tree that are formed outside of the $\mathcal{X}_{rel}$ during exploration phase.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Numerical Simulations 2", "weight": 1.0} -->

As seen in Figures 9, 12, 15, and 18, the ${RRT}_{V2}^{\#}$ algorithm tends not to include vertices into the branches of the tree which are very far away from the optimal solution. Lastly, the ${RRT}_{V3}^{\#}$ algorithm includes a new vertex into the tree only if it is a promising one. Therefore, all vertices in the tree, other than the goal vertices, are either green or blue, which are located around the boundary of $\mathcal{X}_{rel}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Numerical Simulations 2", "weight": 1.0} -->

The convergence rate and variance in the computation of the best path for all algorithms are shown in Figures 11, 14, 17, and 20. Since this is a two-dimensional problem, the optimal path for each problem type can be computed visually and the cost of the paths for each algorithm is normalized with respect to the cost of the optimal solution. The ratio of the cost of the best path over the optimal cost for the ${RRT}^{\ast}$, ${RRT}^{\#}$, ${RRT}_{V1}^{\#}$, ${RRT}_{V2}^{\#}$, and ${RRT}_{V3}^{\#}$ algorithms is shown in red, blue, green, magenta, and black colors, respectively.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Numerical Simulations 2", "weight": 1.0} -->

A Monte-Carlo study was performed in order to compare the convergence rate and variance in the trials of all algorithms in a high dimensional search space. All algorithms were run up until 4 million iterations 100 times in a 5-dimensional search space for Problem types 1 and 2. In the second problem type, several 5-dimensional hypercubes of different size were randomly placed in the environment in order to represent obstacles. As shown in Figures 21 and 22, the ${RRT}_{V2}^{\#}$ and ${RRT}_{V3}^{\#}$ algorithms find the solution in a similar amount of time, and they are faster than the other algorithms. In addition, they compute solutions of lower cost than the other algorithms with smaller variance in the trials.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Numerical Simulations 2", "weight": 1.0} -->

The execution times of all algorithms were also compared. Results of the ${RRT}^{\#}$, ${RRT}_{V1}^{\#}$, ${RRT}_{V2}^{\#}$, and ${RRT}_{V3}^{\#}$ are plotted in blue, green, magenta, and black, respectively. All algorithms were run in a 2D and a 5D environment with no obstacles for up to 750,000 and 4,000,000 iterations, respectively. The execution time of the ${RRT}^{\#}$ and its variant algorithms is normalized over that of the ${RRT}^{\ast}$algorithm and is plotted versus the number of iterations averaged over 50 trials for the 2D search space in Figure 23. A similar plot is also created for 100 trials in the 5D search space and shown in Figure 23.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, a new incremental sampling-based algorithm, denoted by ${RRT}^{\#}$ is presented, which offers asymptotically optimal solutions for solving motion planning problems. The ${RRT}^{\#}$ algorithm relies heavily on the random geometric graph data structure and the $RRG$ algorithm, which is also known to have asymptotic optimality properties. A bottleneck of optimal sampling-based algorithms is the slow convergence to the optimal solution, although sampling-based algorithms are capable of finding a feasible solution, often almost in real-time. By incorporating consistency information of all current vertices in the tree (essentially by comparing the current cost-to-come values of the vertices with the cost-to-come values via one of the neighboring vertices) we can have more informed estimates of the optimal values of the potential paths, thus speeding up convergence. Furthermore, once a feasible path has been found, vertex consistency can be used to estimate the region where the optimal solution should be found. This results in an initial convergence rate that is better than the one of the ${RRT}^{\ast}$ algorithm.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have also introduced three variants to improve the convergence rate of the baseline ${RRT}^{\#}$ algorithm by implementing two key features: preventing the expansion of the tree towards unfavorable regions in search space, and propagating new information throughout the tree in an efficient way. The first feature allows us to limit the number of vertices in the tree, thus resulting to the algorithm running faster. The second feature allows us to compute solutions with a less number of vertices in the tree since any new information is exploited to the highest degree. As a result, the convergence rate of the baseline ${RRT}^{\#}$ can be improved significantly. Extensive numerical results have verified these observations in several simulation scenarios.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The work in this paper can be extended in several directions. First, a thorough theoretical analysis is warranted in order to provide strict bounds on the convergence rate of ${RRT}^{\#}$. Second, since ${RRT}^{\#}$ decomposes the vertex set into "promising" and "non-promising" ones, smarter sampling strategies can be developed to exploit this information. It is also crucial for the algorithm to reach the target set as early as possible in order to converge to the optimal solution faster. In that respect, a bi-directional version of the ${RRT}^{\#}$ (like the RRT-connect in ) can be developed in order to shorten the first time-to-connect to the goal set.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion", "weight": 1.5} -->

A possible implementation would be to have multiple threads implementing the $\mathtt{E}\mathtt{x}\mathtt{t}\mathtt{e}\mathtt{n}\mathtt{d}$ procedure and single thread implementing the $\mathtt{R}\mathtt{e}\mathtt{d}\mathtt{u}\mathtt{c}\mathtt{e}\mathtt{I}\mathtt{n}\mathtt{c}\mathtt{o}\mathtt{n}\mathtt{s}\mathtt{i}\mathtt{s}\mathtt{t}\mathtt{e}\mathtt{n}\mathtt{c}\mathtt{y}$. Finally, the algorithm can be modified to solve motion planning problems for vehicles with complex dynamics (ground vehicles, aircraft, helicopters etc) by implementing specific local steering functions.
