<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Efficient High-quality Motion Planning by Fast All-pairs R-nearest-neighbors

Topics include Motion planning, Sampling-based methods, Nearest neighbors, Planning, Sampling, NN, RTG.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sampling-based motion-planning algorithms typically rely on nearest-neighbor (NN) queries when constructing a roadmap. Recent results suggest that in various settings NN queries may be the computational bottleneck of such algorithms. Moreover, in several asymptotically-optimal algorithms these NN queries are of a specific form: Given a set of points and a radius r report all pairs of points whose distance is at most r. This calls for an application-specific NN data structure tailored to efficiently answering this type of queries. Randomly transformed grids (RTG) were recently proposed by Aiger et al. as a tool to answer such queries and have been shown to outperform common implementations of NN data structures in this context. In this work we employ RTG for sampling-based motion-planning algorithms and describe an efficient implementation of the approach. We show that for motion-planning, RTG allow for faster convergence to high-quality solutions when compared with existing NN data structures. Additionally, RTG enable significantly shorter construction times for batched-PRM variants; specifically, we demonstrate a speedup by a factor of two to three for some scenarios.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction and Related work", "weight": 1.5} -->

Given a robot moving in an environment cluttered with obstacles, motion-planning (MP) algorithms are used to efficiently plan a path for the robot, while avoiding collision with the obstacles. A common approach is to use *sampling-based* algorithms, which abstract the robot as a point in a high-dimensional space called the *configuration space* (C-space) and plan a path in this space. A point, or a configuration, in the C-space represents a placement of the robot that is either collision-free or not, subdividing the C-space $\mathcal{X}$ into the sets $\mathcal{X}_{\text{free}}$ and $\mathcal{X}_{\text{forb}}$, respectively. The structure of the C-space is then studied by constructing a graph, called a *roadmap*, that approximates the connectivity of $\mathcal{X}_{\text{free}}$. The nodes of the graph are collision-free configurations sampled at random. Two (nearby) nodes are connected by an edge if the straight line connecting their configurations is collision-free as well.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction and Related work", "weight": 1.5} -->

Sampling-based MP algorithms are implemented using two primitive operations: *Collision detection* (CD), which is used to asses if a configuration is collision-free or not, and *Nearest neighbor* (NN) search, which is used to efficiently return the neighbor (or neighbors) of a given configuration. The CD operation is also used to test if the straight line connecting two configurations lies in $\mathcal{X}_{\text{free}}$---a procedure referred to as *local planning*. While in theory the cost of NN exceeds that of local planning, in practice it is the latter that is the main computational bottleneck in sampling-based MP algorithms.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction and Related work", "weight": 1.5} -->

However, recent results (e.g. ) suggest that this may not always be the case. By carefully replacing many expensive calls to the local planner with NN queries, one may reduce the running time of different sampling-based MP algorithms. As a result, the computational overhead of NN queries plays a significant role in the running time of these algorithms. Moreover, existing algorithms that ensure *asymptotic optimality*^11^1An algorithm is said to be asymptotically optimal, if the cost of the solution produced by the algorithm asymptotically approaches the cost of the optimal solution. The notion of cost depends on the problem at hand and may be, e.g., path length, energy consumption along the path or minimal distance from the obstacles. such as PRM\*, FMT\* and MPLB or *asymptotic near-optimality*^22^2An algorithm is said to be asymptotically near-optimal, if given an approximation factor $\varepsilon$, the cost of the solution produced by the algorithm approaches a cost within a factor of $({1 + \varepsilon})$ of the optimal solution.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction and Related work", "weight": 1.5} -->

(such as ANO-MPLB ) can make use of *all-pairs $r$-nearest-neighbors* queries. That is, given a set $P$ of $n$ points and a radius $r = {r{(n)}}$ report all pairs of points ${p,q} \in P$ such that the distance between $p$ and $q$ is at most $r$. This calls for application-specific NN data structures tailored to efficiently answering this type of queries. Many implementations of efficient NN data structures exist, e.g., ANN, FLANN, and E2LSH. However, none of the above methods is tailored for these very specific NN queries that arise in the context of these motion-planning algorithms.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction and Related work", "weight": 1.5} -->

Contribution and paper organization. This paper adopts Randomly Transformed Grids (RTG), an algorithm by Aiger et al. for finding all-pairs $r$-nearest-neighbors, to sampling-based MP algorithms. We begin by identifying which algorithms can make use of all-pairs $r$-nearest-neighbors and review them in Section II. Specifically, we discuss the subtleties of using them in an anytime mode versus a batch mode. After an overview of existing NN data structures we present in Section III ‣ Efficient high-quality motion planning by fast all-pairs 𝑟-nearest-neighbors") the RTG algorithm together with a description of our efficient implementation. We then proceed with a series of experimental results comparing our implementation with different state-of-the-art implementations of NN data structures and show the speedup that is obtained by using our RTG implementation for all-pairs $r$-nearest-neighbors queries. To test the affect of RTG in MP algorithms, we present a series of simulations demonstrating that RTG allows to speed up the construction time of PRM-type roadmaps, the time to obtain an initial solution or to converge to high-quality solutions in complex scenarios.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction and Related work", "weight": 1.5} -->

For example, the construction time of PRM-type roadmaps in certain scenarios is reduced by a factor of between two and three. We conclude in Section V with a discussion of the current limitations of our approach together with suggestions for possible future work.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

Throughout this subsection we use the following procedures, which are standard procedures used in sampling-base MP algorithms. sample_free$(n)$ is a procedure returning $n$ random free configurations. nearest_neighbor$(x,V)$ and $r$-nearest_neighbors$(x,V,r)$ return the nearest neighbor and all nearest neighbors in a ball of radius $r$ of $x$ within the set $V$, respectively. Let steer$(x,y)$ return a configuration $z$ that is closer to $y$ than $x$ is. The procedure collision_free$(x,y)$ tests whether the straight-line segment connecting $x$ and $y$ is contained in $\mathcal{X}_{\text{free}}$, and dist$(x,y)$ returns the Euclidean distance of the straight-line path connecting $x$ and $y$. Let us denote by $\text{cost}_{\mathcal{G}}{(x)}$ the minimal cost^44^4In this paper, unless stated otherwise, we use Euclidean distance as the cost function.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

of reaching a node $x$ from $x_{init}$ using a roadmap $\mathcal{G}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

We begin by discussing the subtle difference between batch and anytime MP algorithms. We refer to an algorithm as a *batch* algorithm if it processes a predefined number of samples $n$ in one go. An algorithm is said to be *anytime* if it refines its solution as time progresses and may be run for any given amount of time. Observe that efficiently computing all-pairs $r$-nearest-neighbors is intrinsically a *batch* operation. We briefly describe a scheme to easily modify a batch algorithm into an anytime one (see, e.g., ). First, run the algorithm on an initial (small) set of $n$ samples. Then, as long as time permits, double $n$ and re-run the algorithm using the larger $n$. This way we obtain anytime algorithms, which rely on all-pairs $r$-nearest-neighbors---this in turn makes them amenable to the optimization that we propose in this paper. We note that between iterations, additional optimizations such as pruning, informed sampling, using lower bounds or relaxing optimality may be applied.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

Arguably, the best-known MP algorithm that makes use of all-pairs $r$-nearest-neighbors is PRM\*. PRM\*, outlined in Alg. 1, is a multi-query, batch, asymptotically-optimal algorithm that maintains a graph data structure as its roadmap. It samples $n$ collision-free configurations which are the vertices of the roadmap (line 1). Two configurations are connected by an edge if their distance is less than $r{(n)}$ and if the straight-line connecting them is collision-free (lines 2-5). Specifically, the radius used is

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

where $d$ is the dimension, $\mu{(\mathcal{X}_{\text{free}})}$ is the volume of the free space and $\zeta_{d}$ is the volume of a $d$-dimensional sphere of radius 1.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

1: V ← {xinit} ∪ sample_free (n); E ← ⌀; 𝒢 ← (V,E)
4: if (collision_free(x, y)) then

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

To reduce the number of calls to the local planner, one can delay local planning to the query phase and test if two neighbors are connected only if they potentially lie on the shortest path to the goal. This lazy approach was originally suggested for the PRM algorithm. We apply this approach to the aforementioned batched PRM\* and call it LazyB-PRM\*. Somewhat similarly, Luo and Hauser have recently proposed an anytime, *single-query* variant for PRM\* called Lazy-PRM\* that relies on dynamic shortest path algorithms to efficiently update the roadmap.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

Janson and Pavone introduced the Fast Marching Tree algorithm (FMT\*). The single-query asymptotically-optimal algorithm, outlined in Alg. 2, maintains a tree as its roadmap. Similarly to PRM\*, FMT\* samples $n$ collision-free nodes $V$ (line 1). It then builds a minimum-cost spanning tree rooted at the initial configuration by maintaining two sets of nodes $H,W$ such that $H$ is the set of nodes added to the tree that may be expanded and $W$ is the set of nodes not in the tree yet (line 2). It then computes for each node the set of nearest neighbors^55^5The nearest-neighbor computation can be delayed and performed only when needed but we present the batched mode of computation to simplify the exposition. The delayed variant makes use of multiple $r$-nearest neighbors queries while the batched-mode variant makes use of all-pairs $r$-nearest neighbors queries. of radius $r{(n)}$ (line 4).

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

The algorithm repeats the following process: the node $z$ with the lowest cost-to-come value is chosen from $H$ (line 5 and 17). For each neighbor $x$ of $z$ that is not already in $H$, the algorithm finds its neighbor $y \in H$ such that the cost-to-come of $y$ added to the distance between $y$ and $x$ is minimal (lines 8-10). If the local path between $y$ and $x$ is free, $x$ is added to $H$ with $y$ as its parent (lines 11-13). At the end of each iteration $z$ is removed from $H$ (line 14). The algorithm runs until a solution is found or there are no more nodes to process. The algorithm, together with its bidirectional variant, were shown to converge to an optimal solution faster than PRM\* and RRT\*. The radius used by the FMT\* algorithm is

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

where $\eta > 0$ is some small constant. Moreover, Janson and Pavone show that PRM\* can also use the (smaller) radius defined in Eq. 2 while maintaining its asymptotic optimality.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

1: V ← {xinit} ∪ sample_free (n); E ← ⌀; 𝒯 ← (V,E)
10: ymin ← arg miny ∈ Ynear{cost𝒯 (y) + dist (y,x)}
11: if collision_free(ymin,x) then
17: z ← arg miny ∈ H{cost (y)}

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

Recently, we proposed a scheme to compute tight, effective lower bounds on the cost to reach the goal. Incorporating these bounds with the FMT\* algorithm, we introduced Motion Planning using Lower Bounds or MPLB. The algorithmic tools used by MPLB cause the weight of collision-detection to be negligible when compared to NN calls. Some of the experimental results suggest that more than 40% of the running time of the algorithm is spent on NN queries. MPLB uses the same radius as FMT\* (Eq. 2).

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

Both FMT\* and MPLB perform $r$-nearest-neighbors queries for a subset of the input points (we call this *multiple $r$-nearest-neighbors queries)*. On the other hand, the NN data structure we propose to use answers only all-pairs $r$-nearest-neighbors queries. This can easily be addressed by performing an all-pairs $r$-nearest-neighbors query once, and storing all such pairs. Multiple $r$-nearest-neighbors queries are then reduced to querying the stored set of pairs and returning the relevant ones. Clearly, this will only be efficient when the number of multiple $r$-nearest-neighbors queries is large. As demonstrated in Section IV this is indeed the case.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

RRT\* is a single-query asymptotically-optimal variant of the RRT algorithm. We first outline the RRT algorithm (lines 1-7 of Alg. 3) and then continue describing the RRT\* algorithm together with a variant which we call batched-RRT\*. The RRT algorithm maintains a tree as its roadmap. At each iteration a configuration $x_{rand}$ is sampled at random (line 3). Then, $x_{nearest}$, the nearest configuration to $x_{rand}$ in the roadmap is found (line 4) and extended in the direction of $x_{rand}$ to a new configuration $x_{new}$ (line 5). If the path between $x_{nearest}$ and $x_{new}$ is collision-free, then $x_{new}$ is added to the roadmap (lines 6-7).

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

1: if (collision_free(xp o t e n t i a l _ p a r e n t, xc h i l d)) then
3: if (cost𝒯(xp o t e n t i a l _ p a r e n t) + c &lt; cost𝒯(xc h i l d)) then
Algorithm 4 rewire_RRT∗(xp o t e n t i a l _ p a r e n t, xc h i l d)

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

RRT\* follows the same steps as the RRT algorithm but has an additional stage after an edge is added to the tree (lines 8-12 of Alg. 3): a set $X_{near}$ of the $r$-nearest neighbors of $x_{new}$ is considered and a *rewiring* step (see Alg. 4) occurs twice: first, it is used to find the node $x_{near} \in X_{near}$ which will minimize the cost to reach $x_{new}$; then, the procedure is used to attempt to minimize the cost to reach every node $x_{near} \in X_{near}$ by considering $x_{new}$ as its parent. We note that RRT\* uses two types of NN queries: both nearest-neighbor and multiple $r$-nearest_neighbors. Moreover, the original formulation of RRT\* uses at step $i$ a radius of $r_{{RRT} \ast}{(i)}$ where

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

However, to ensure asymptotic optimality, a radius of $r{(n)}$ may be used at each stage of the algorithm (see proof of Thm. 38 in ).

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

We propose a batch variant of RRT\* that stems from the FMT\* framework. Instead of using $n$ uniformly sampled configurations, one may use the $n$ nodes constructed by an RRT algorithm and build the FMT\*-tree using these nodes. This variant benefits from (i) the fast exploration of the configuration space due to the Voronoi-bias that RRT has and (ii) the efficient construction of the shortest-path spanning tree due to the Dijkstra-like pass that FMT\* has. We call this variant batched-RRT\*.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-A Sampling-based motion-planning algorithms", "weight": 1.0} -->

We summarize the different algorithms in Table I together with the type of NN queries that they use.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B Review of existing nearest-neighbor data structures", "weight": 1.0} -->

As nearest-neighbors search is widely used in various domains there exists a wide range of methods allowing efficient proximity queries, differing in their space requirement and time complexity. Such methods include the $kd$-trees, geometric near-neighbor access trees (GNAT), locality sensitive hashing (LSH), and others.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-B Review of existing nearest-neighbor data structures", "weight": 1.0} -->

$kd$-trees, which work best for rather low dimensions, are often used in motion-planning settings. A $kd$-tree is a binary tree storing the input points in its leaves, where each node $v$ defines an axis-aligned hyper-rectangle containing the points stored in the subtree rooted at $v$. Given a query point $q$, NN search is performed in two phases: the first locates the leaf node with the hyper-rectangle containing $q$, and the second traverses the tree backwards searching for closer sibling nodes. Given a $d$-dimensional point set of size $n$, construction takes $O{({dn{\log n}})}$ time. Friedman et al. showed that under mild assumptions the expected time for a single nearest-neighbor query is $O{({\log n})}$. For $r$-nearest-neighbors queries, the expected complexity is at least $\Omega{({{\log n} + k})}$, where $k$ is the number of reported neighbors (the worst-case bounds are much worse ).

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-B Review of existing nearest-neighbor data structures", "weight": 1.0} -->

Another recursive structure that is frequently used in motion-planning algorithms is GNAT. The input point set is recursively divided into smaller subsets and each subset is then represented using a subtree. Searching the structure is done recursively, while the recursion call continues to child nodes that have not yet been pruned. As claimed, typically only linear space is required and the construction takes $O{({dn{\log n}})}$ time.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-B Review of existing nearest-neighbor data structures", "weight": 1.0} -->

A common practice for speeding up algorithms that use NN queries but do not require exact results (such as MP algorithms) is to use *approximate* NN queries. Different types of approximate $r$-nearest-neighbors methods exists: some (e.g., ) return with high probability most neighbors of a given query point $q$, while others return a neighbor within a distance $r{({1 + \epsilon})}$ if a neighbor at distance of at most $r$ from $q$ exists.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-B Review of existing nearest-neighbor data structures", "weight": 1.0} -->

Locally sensitive hashing (LSH), presented by Indyk and Motwani, is an approximate nearest-neighbor method for $d$-dimensional point sets. As opposed to many other methods, its $O{({dn^{\frac{1}{1 + \epsilon}}})}$ query time does not depend exponentially on the dimension. LSH uses a subset of $t$ hash functions from a family of locally sensitive hash functions for mapping the data into buckets. That is, with high probability two close points will be mapped to the same bucket. Given a query point $q$, the algorithm maps $q$ using the set of hash functions to a set of buckets and collects all data points that were mapped to these buckets. The required neighbor is then found within this set of collected candidates.

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-B Review of existing nearest-neighbor data structures", "weight": 1.0} -->

An algorithm for finding all nearest-neighbors in a given fixed $d$-dimensional point set under the $L_{\infty}$-metric was originally presented by Lenhof and Smid. The algorithm uses a fixed uniform grid for inspecting pairs of points that lie in the same grid cell or in two adjacent ones. Its time complexity is linear in both the input size and the output size. A simplified variant was later presented by Chan.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Randomly Transformed Grids (RTG)", "weight": 1.0} -->

Aiger et al. suggest two simple randomized algorithms for approximately answering all-pairs $r$-nearest-neighbors queries given a set $P$ of $n$ points in a $d$-dimensional Euclidean space.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Randomly Transformed Grids (RTG)", "weight": 1.0} -->

The first algorithm, outlined in Alg. 5 ‣ Efficient high-quality motion planning by fast all-pairs 𝑟-nearest-neighbors"), conceptually places a $d$-dimensional axis-parallel grid of cell size^66^6 The cell size $c$ should be slightly larger than the radius $r$. Thus, to specify the cell size, one needs to specify a constant, which we call the cell-size factor, ${\overset{\sim}{c}{(r,d)}} > 1$, such that $c = {\overset{\sim}{c} \cdot r}$. $c$, which is shifted according to a randomly chosen uniform shift (line 2). This grid defines a partition of the points in $P$ into cells, and each point is associated to the cell $u$ containing it (lines 4-7). For each non-empty grid cell, the distance between every two points associated to the cell is computed. A pair inside a cell is then reported if the computed distance is at most $r$ (lines 8-9).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Randomly Transformed Grids (RTG)", "weight": 1.0} -->

The process is repeated $m$ times to guarantee that, with high probability, most pairs of points at Euclidean distance at most $r$ will be reported. The second algorithm follows the same approach adding a random orientation to each randomly shifted grid.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Randomly Transformed Grids (RTG)", "weight": 1.0} -->

2: Choose a random shift for a grid of cell size c
5: Compute the grid cell u that p lies in
9: Go over all pairs of points in u and report those of Euclidean distance at most r
Algorithm 5 Randomly Shifted Grids (P, r, c, m )

<!-- chunk {"id": "body-0038", "role": "body", "section": "Randomly Transformed Grids (RTG)", "weight": 1.0} -->

Assuming a constant-cost implementation of the floor function and of hashing, Aiger et al. show that for appropriate choices of $c$ and $m$, with high probability, the algorithm reports every pair at distance at most $r$ with time $O{({{({n + k})}{\log n}})}$, where $k$ is the number of pairs at distance at most $r$. Note that the hidden constant depends exponentially on the dimension $d$. When only randomly shifted grids are used, the constant is roughly ${(\sqrt{d}})}^{d}$. However, when both rotations and translations are used, it is roughly $6.74^{d}$. For input sets lying in a subset of the space that has low doubling dimension, much tighter bounds can be obtained.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Randomly Transformed Grids (RTG)", "weight": 1.0} -->

We next discuss the effect of the algorithm's parameters, outline several tradeoffs, and describe an efficient implementation of the algorithm.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-A The key parameters", "weight": 1.0} -->

RTG requires the user to set the cell size $c$ and the number $m$ of randomly shifted grids. These two parameters have a major impact on the performance of the algorithm. When a very small $c$ or $m$ is used, the set of reported pairs might be small compared to the true number of neighboring pairs. However, when a large value of $c$ is used, the algorithm may output the whole set of true neighbors at the cost of performing several inefficient brute-force searches. Obviously, the more iterations performed (larger $m$) the better the results are. Therefore, a tradeoff between the running time and the quality of the results exists, and any subtle change to either $c$ or $m$ may affect both measures. Experiments supporting this observation are detailed in Subsec. IV-A.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-B Implementation details", "weight": 1.0} -->

Implementing the algorithm in a naïve manner is straightforward. One has to store the non-empty cells and their associated points. All pairs of points within a cell are examined in a brute force manner, computing the distance of a pair in $O{(d)}$ time and reporting the pair if relevant.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-B Implementation details", "weight": 1.0} -->

Note that a certain pair of points may be associated to the same cell in several different grids. Thus, in order to report every neighboring pair only once, an auxiliary data structure for storing the already reported pairs is needed. If such a structure allows efficient query operations as well as efficient insertions, it can be utilized to avoid costly distance computations by filtering out many potential pairs. As a result, the running time of the algorithm can be significantly reduced at the cost of storing the auxiliary pairs structure.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-B Implementation details", "weight": 1.0} -->

Let $P = {\{ p_{1},\ldots,p_{n}\}}$ be the set of input points. A possible auxiliary structure would be an array of unordered sets, where the $i$th cell of the array stores all indices $j > i$ such that $(p_{i},p_{j})$ is a reported pair. The space complexity of such a structure is linear in the size of the output (the number of reported pairs), whereas the expected query time and update time are constant. On the other hand, one can use a different auxiliary structure, whose space complexity is $O{(n^{2})}$, and experience much better query and update times. For instance, a bit array representing a two-dimensional matrix, where the cell $(i,j)$ is set to one if the pair $(p_{i},p_{j})$ is a reported pair, is a possible structure (notice that only half of the array needs to be stored due to symmetry). It supports constant-time insert and constant-time query operations.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-B Implementation details", "weight": 1.0} -->

Nevertheless, both the space and the query time complexity do not depend on the output size. However, such a solution is restricted to a limited number of input points, depending on the machine on which the query is executed. We refer to this structure as a flattened two-dimensional bit array.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-B Implementation details", "weight": 1.0} -->

Our C++ implementation supports either auxiliary data structures discussed. The array of unordered sets is implemented as a vector of boost::unordered_set-s, while boost::dynamic_bitset is used for implementing the flattened bit-array. Although the latter typically exhibits running times that are twice as fast as the former (for dimensions six and above), it is highly non-scalable with respect to memory consumption, thus only applicable to settings where a limited number of samples is required. In the rest of the paper we report on results of the first variant only, namely an array of unordered sets.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-B Implementation details", "weight": 1.0} -->

As we construct one grid at a time, and since each new grid may introduce new neighboring pairs, the pairs are reported in an unordered manner. Therefore, only all-pairs $r$-nearest-neighbors queries are supported. Yet, the structures can be extended such that they support multiple $r$-nearest-neighbors as well. In order to do so, the auxiliary structure should store every pair twice. Then, after finding all pairs, multiple $r$-nearest-neighbors queries can be easily answered.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-B Implementation details", "weight": 1.0} -->

We have also implemented the second algorithm proposed by Aiger et al. that adds random orientations to the constructed grids. Our implementation, which uses the Eigen C++ library, did not achieve significant improvement in running time and quality of the results, comparing to the first RTG algorithm. Therefore, we do not report on these results here. We leave it for further research to understand the gap between the optimistic theoretical prediction and the effect of orientation in practice.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experimental results", "weight": 1.0} -->

To evaluate our implementation, we first report on a set of experiments aiming both to demonstrate the sensitivity of the RTG algorithm to the parameters used and to determine the better (ideally, optimal) ones. Using these computed parameters, we first compare our implementation with several state-of-the-art implementations of NN data structures and show the speedup that may be obtained by using our RTG implementation for all-pairs $r$-nearest-neighbors queries. Finally, to test the effect of RTG in MP algorithms, we present a series of simulations that demonstrate that RTG allows to speed up the construction time of a PRM-type roadmap, the time to obtain an initial solution or to converge to high-quality solutions. All experiments were executed on a 2.8GHz Intel Core i7 processor with 8GB of RAM.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-A Parameter tuning", "weight": 1.0} -->

Recall that given a set of $n$ points in a $d$-dimensional space and a radius $r = {r{(n)}}$ (as in Eq. 2), the RTG algorithm has two parameters that should be set: the cell size $c$ and the number $m$ of grids to construct. As discussed in Sec. III ‣ Efficient high-quality motion planning by fast all-pairs 𝑟-nearest-neighbors"), the algorithm is rather sensitive with respect to either parameter. Therefore, we conducted the following experiments in the unit $d$-dimensional hypercube: we executed our RTG implementation using increasing values of $c$ and $m$ and measured both the time for running all-pairs $r$-nearest-neighbor and the success-rate, that is, the ratio between the number of reported pairs and the ground truth. We repeated the experiment for different values of $n$ and $d$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-A Parameter tuning", "weight": 1.0} -->

Fig. 1a shows that for a given cell-size factor $\overset{\sim}{c}$ (recall that $\overset{\sim}{c} = \frac{c}{r}$), increasing the number $m$ of grids results in both an increase in the success rate of the algorithm as well as a linear growth in the running time. Similar behavior was observed for a given $m$, when $\overset{\sim}{c}$ gradually increases (Fig. 1b).

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-A Parameter tuning", "weight": 1.0} -->

Requiring a success rate of at least 98%, we chose for each $d$ and $n$ the values of $m$ and $\overset{\sim}{c}$ (and thus the value of $c$) that yielded the best running times. Our results are summarized in Table II. We note that similar behavior and results were obtained when running the same experiment on a point set sampled in an environment cluttered with obstacles.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-A Parameter tuning", "weight": 1.0} -->

Throughout the next set of experiments, the values for $c$ and $m$ are selected according to the aforementioned table. Note that Aiger et al. use completely different values for $c$ and $m$, which we found too crude for our setting. The difference lies in the smaller radius used in their experiments, causing the output size to be very small with respect to $n$. This is not surprising as their data comes from an application of completely different nature.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-B Comparison with existing NN libraries", "weight": 1.0} -->

We compared our RTG implementation with the following state-of-the-art NN methods: FLANN $kd$-tree, ANN $kd$-tree, and LSH in Euclidean metric spaces (E2LSH). For ANN we set the bucket size to $\log n$, where $n$ is the number of input points, and allowed an error bound of $\varepsilon = 0.5$ in the query phase. We mark that this had no major effect on the number of reported pairs. For consistency reasons, we used the same error bound in FLANN. For E2LSH we had to empirically estimate the optimal parameters for our point set. Therefore, we used a training set and selected the parameters that minimize the running time on the training set while still reporting a true neighbor with probability at least 0.9. As mentioned, for RTG we chose $c$ and $m$ according to Table II.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-B Comparison with existing NN libraries", "weight": 1.0} -->

For each method we measured the time for answering an all-pairs $r$-nearest-neighbors queries^77^7Recall that for some of the methods finding all pairs requires $n$ single $r$-nearest-neighbors calls, with each of the $n$ points as an input. for $n$ random uniform samples from the unit $d$-dimensional hypercube. The radius $r = {r{(n)}}$ was defined as in Eq. 2. We used point sets, of increasing sizes, of dimensions $d = {3,6,9,{\text{~and~}12}}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-B Comparison with existing NN libraries", "weight": 1.0} -->

The results for different dimensions, averaged over ten different runs, are presented in Fig. 2, 3 and 4. Clearly, as the number of samples increases (exactly where NN dominates the running times of MP algorithms) the gap in running time between our RTG implementation and the other methods grows. Similar results (see Fig. 5) were obtained when the environment was cluttered with obstacles.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-C RTG in motion-planning algorithms", "weight": 1.0} -->

We integrated our RTG implementation within the OMPL framework, which uses GNAT as its primary NN structure. This allowed us to compare the two NN data structures in different MP algorithms. The scenarios we used are depicted in Fig. 6. Each result is averaged over 50 runs.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-C RTG in motion-planning algorithms", "weight": 1.0} -->

We first tested the construction time of the multi-query algorithms PRM\* and LazyB-PRM\* on the Z-tunnel scenario^88^8Scenario based on the Z tunnel scenario by the Parasol MP Group, CS Dept, Texas A&M University (Fig. 6a) in a three-dimensional Euclidean C-space of a robot translating in space. Fig. 7 reports on the construction time as a function of the number $n$ of samples in the roadmap. One can clearly see that as $n$ grows, using RTG becomes more advantageous. To test the quality of the roadmap obtained, we performed a query for finding a path from one side of the Z-tunnel to the other (see green and red robots in Fig. 6a). Both roadmaps yielded similar success rates in finding a solution.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-C RTG in motion-planning algorithms", "weight": 1.0} -->

Next, we tested the single-query MPLB algorithm on the 3D Grid scenario (Fig. 6b) in a six-dimensional C-space consisting of two translating robots in space. The distance metric we used, which we refer to as MR-metric, computes the sum of the distances that each robot travels. Fig. 8 presents the quality of the solution obtained as a function of time. One can see that RTG allows to find higher quality solutions faster than GNAT. Even though the analysis of Aiger et al. regarding the quality of RTG's results holds only in Euclidean spaces, the MR-metric is more natural in multi-robot settings. We repeated the same test for the Euclidean metric. The results, presented in Fig. 9, demonstrate similar trends to those presented for the MR-metric.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-C RTG in motion-planning algorithms", "weight": 1.0} -->

Finally, we report on the success rate of finding a solution in the Cubicles scenario^99^9The Cubicles scenario is provided with the OMPL distribution. (Fig. 6c). We first performed the experiment for a six-dimensional Euclidean C-space consisting of two translating robots. The results, depicted in Fig. 10, demonstrate that RTG allows to reduce the time to find an initial solution in complex scenarios. Fig. 11 presents similar results using the MR-metric.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Discussion and future work", "weight": 1.5} -->

Many possible enhancements can be applied to our RTG implementation in order to easily use it in sampling-based MP algorithms. One obvious requirement is to automatically tune the two parameters $c$ and $m$ defining the grid cell size and the number of constructed grids, respectively.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Discussion and future work", "weight": 1.5} -->

Our RTG implementation is much faster when the flattened bit-array is used for storing the pairs, however this structure has a quadratic space complexity. Thus, a potential solution may introduce a hybrid data structure that for small number of samples uses the bit-array and for large inputs uses the array of unordered sets. Nevertheless, as the array of unordered sets is output sensitive in its memory consumption, when the number of true neighboring pairs is very large, cache faults occur and the program slows down drastically. Thus, we seek to have an IO-efficient RTG implementation in order to overcome these limitations.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Discussion and future work", "weight": 1.5} -->

Similar to the work, one can implement RTG differently such that a single $r$-nearest-neighbors query, as opposed to all-pairs $r$-nearest-neighbors, is answered efficiently. Such implementation should store all $m$ constructed grids. At query phase, given a query point $q$, the $m$ cells containing $q$ are examined, and the set of neighboring points among all potential candidates within the cells is found. For small values of $m$, this implementation may be efficient.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Discussion and future work", "weight": 1.5} -->

Another interesting extension is parallelizing the algorithm. A possible approach may be to partition the grid into overlapping portions and run the algorithm on each portion separately. Finally, we wish to devise an RTG variant applicable to non-Euclidean C-spaces, a much needed data structure in asymptotically-optimal sampling-based MP algorithms.
