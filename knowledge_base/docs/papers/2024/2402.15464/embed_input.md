<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

CLIPPER+: A Fast Maximal Clique Algorithm for Robust Global Registration

Topics include Robotics, Robustness, Graphs, Computational complexity, Benchmarks, Accuracy, NP-hardness.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present CLIPPER+, an algorithm for finding maximal cliques in unweighted graphs for outlier-robust global registration. The registration problem can be formulated as a graph and solved by finding its maximum clique. This formulation leads to extreme robustness to outliers; however, finding the maximum clique is an NP-hard problem, and therefore approximation is required in practice for large-size problems. The performance of an approximation algorithm is evaluated by its computational complexity (the lower the runtime, the better) and solution accuracy (how close the solution is to the maximum clique). Accordingly, the main contribution of CLIPPER+ is outperforming the state-of-the-art in accuracy while maintaining a relatively low runtime. CLIPPER+ builds on prior work (CLIPPER and PMC ) and prunes the graph by removing vertices that have a small core number and cannot be a part of the maximum clique. This will result in a smaller graph, on which the maximum clique can be estimated considerably faster. We evaluate the performance of CLIPPER+ on standard graph benchmarks, as well as synthetic and real-world point cloud registration problems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

These evaluations demonstrate that CLIPPER+ has the highest accuracy and can register point clouds in scenarios where over 99% of associations are outliers. Our code and evaluation benchmarks are released at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Data association is broadly defined as the correspondence of identical/similar elements across sets of data, and is a key component of many robotics and computer vision applications, such as localization and mapping, point cloud registration, shape alignment, object detection, data fusion, and multi-object tracking. In these applications, it is crucial that data association is solved correctly and fast.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In point cloud registration, for example, we seek to find the rigid transformation (rotation/translation) that aligns two sets of 3D points. This requires associating points in one set with their corresponding points in the other set. Local registration techniques such as the Iterative Closest Point (ICP) algorithm associate points based on their nearest neighbor. These associations are generally wrong if the point clouds are not aligned well initially, leading to wrong registration. Better associations can be established by matching descriptors that are computed around each point in the point cloud and describe the local geometry and appearance of a point (e.g., classical FPFH or modern learning-based 3DMatch ). However, due to noise, repetitive patterns, small overlap between the point clouds, etc., these putative associations can have extreme outlier ratios (e.g., FPFH associations in Section V-C are $99\%$ outliers/wrong).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In these high-outlier regimes, existing outlier rejection techniques (such as the general RANSAC framework or specific frameworks for point cloud registration ) either return wrong results or have impractical runtime (e.g., RANSAC's runtime grows exponentially in outlier ratio ).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these issues, we present the CLIPPER+ algorithm. CLIPPER+ formulates the data association problem as a graph, in which the inlier/correct associations are the maximum clique. This formulation is robust to high outlier ratios and applicable to any problem that admits invariants (see Section III) such as point, line, and plane could registration. To address the high computational complexity of finding the maximum clique (NP-hardness), CLIPPER+ finds an approximate solution instead, which is obtained from combining an improved version of our prior work, CLIPPER, and the greedy maximal clique algorithm. CLIPPER+ runs in polynomial time and outperforms state-of-the-art algorithms in maximum clique estimation accuracy (Section V-A). Further, CLIPPER+ solutions are shown to be exact (i.e., the maximum clique) in over $99\%$ of the point cloud registration trials (Section V-C).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, this work's contributions are: An improved solver (Algorithm 2) leading to higher accuracy over our prior work CLIPPER.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The new CLIPPER+ algorithm as the combination of the greedy algorithm in and CLIPPER, further improving both runtime and accuracy.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Evaluations demonstrating superior accuracy of CLIPPER+ over state-of-the-art on maximum clique problems, and correct registration of real-world point clouds in regimes with over $99\%$ outliers.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Efficient C++ implementation of all algorithms (open-source code will be released).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Graph-Theoretic Robust Registration", "weight": 1.0} -->

The key idea for creating robustness to extreme outlier ratios is to find the largest set of jointly consistent data and/or associations. This problem can be formulated as a graph, in which this set is represented by the maximum clique. In what follows, we introduce this graph-theoretic framework and its use case for point cloud registration.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Graph-Theoretic Robust Registration", "weight": 1.0} -->

Point cloud registration: The objective of point cloud registration is to find the rigid transformation that aligns a set of points to their corresponding points in another set. The main challenge is finding the correct correspondences as usually only a subset of the points match, and, the points do not align perfectly due to noise. An outlier can be a point in one set that does not have a counterpart in the other set, or an association that matches wrong points across the sets. Our focus here is associations, and henceforth outliers imply outlier associations. Fig. 1 illustrates a point cloud registration example where we seek to find the blue bunny in the cluttered point cloud.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Graph-Theoretic Robust Registration", "weight": 1.0} -->

Maximum likelihood solution: In the absence of prior knowledge and when outliers are random, unbiased, and unstructured, the largest set of jointly consistent associations are inliers for the maximum likelihood solution. For point cloud registration, two associations are consistent if their endpoints are equidistant, and therefore can be aligned by a rigid transformation. In Fig 1, the green associations align $3$ points while the red associations align $2$ points. Thus, the green associations are the inliers and can be used to compute the correct maximum likelihood solution.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Graph-Theoretic Robust Registration", "weight": 1.0} -->

Graph formulation: Finding the largest set of jointly consistent associations can be formulated as a maximum clique problem. Given $n$ associations, the consistency graph is a graph of $n$ vertices where each vertex represents an association. An edge between two vertices indicates that the associations are consistent. In Fig. 1, an edge between two vertices of the consistency graph (shown on the right) indicates consistency of corresponding associations. For example, there is an edge between vertices/associations $2$ and $3$ as their endpoints are equidistant ($d = d'$), while there is no edge between vertices/associations $1$ and $3$. Given two associations with endpoint distances $d$ and $d'$, due to noise, often a consistency threshold $\epsilon$ is used where if ${|{d - d'}|} < \epsilon$, the associations are deemed consistent.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Graph-Theoretic Robust Registration", "weight": 1.0} -->

A clique is a subset of vertices where every pair of vertices within that subset is connected by an edge. The maximum clique is the clique with the largest number of vertices. A maximal clique is a clique that is not contained in a larger clique. The maximum clique in Fig. 1 consists of vertices $2$, $3$, and $5$. Vertices $1$ and $4$ form a maximal clique.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Graph-Theoretic Robust Registration", "weight": 1.0} -->

Invariants: The graph-theoretic framework can be applied to a broad array of data association problems in robotics. An invariant is a quantity that remains unchanged across the sets. The invariant used for the point cloud registration example above was the Euclidean distance between the endpoints. Invariants can be defined to register lines, planes, 2D-3D visual features, etc. Examples in this work, however, focus on point cloud registration.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Maximal Clique Algorithms", "weight": 1.0} -->

1:Input A: adjacency matrix; K: core numbers 2:Output C: vertices that form maximal clique 4:% Sort vertices by core number in descending order: 8: % Neighbors of vi with core numbers ≥ cmax: 10: (s1, …, sk)← sort si ∈ S descending by core number 12: for j = 1: k do % For each vertex in sorted S 15: if |C’| > cmax then % Found a larger clique 16: C ← C’; cmax ← |C′| % Update the output Algorithm 1 Degeneracy-Ordered Greedy Maximal Clique We present the main algorithmic contributions of this work in subsections IV-B and IV-C, where we discuss the maximal clique algorithms based on a continuous relaxation and CLIPPER+. Subsection IV-A is a review of the approach, and is not an algorithmic contribution. However, our C++ implementation of this algorithm improved the performance and accuracy compared to its original implementation.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Degeneracy-Ordered Greedy Maximal Clique Algorithm", "weight": 1.0} -->

Algorithm 1 presents a greedy approach for finding a maximal clique. Starting from an empty clique (line 3), we grow the clique one vertex at a time by looping through the vertices (line 6). For each vertex $v$ that this loop examines, the algorithm adds $v$ to the current clique if it is connected to every vertex that is already in the clique, and discards $v$ otherwise (lines 13-16). This algorithm has the overall runtime of $O{({\delta{|E|}})}$, where $\delta$ is the maximum vertex degree and $|E|$ is the number of edges.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Degeneracy-Ordered Greedy Maximal Clique Algorithm", "weight": 1.0} -->

The maximal clique returned by the greedy approach depends on the initial vertex chosen to grow the clique, and the ordering of vertices (as they are sequentially examined to be added to the current clique or discarded). A descending ordering of vertices by their core number greatly improves the odds of finding a large maximal clique (and possibly the maximum clique), as leveraged in Algorithm 1 (lines 5 and 10). Mathematically, the core number or degeneracy of a vertex $v$ is the largest integer $k$ such that the degree of $v$ remains non-zero when all vertices of degree less than $k$ are recursively removed from the graph. The core number of vertices can be computed efficiently in $O{({|E|})}$ by Batagelj and Zaversnik's algorithm.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Continuous-Relaxation Maximal Clique Algorithm", "weight": 1.0} -->

1:Input A: adjacency matrix; $\overline{u}$: initial guess 2:Output C: vertices that form maximal clique 4:M ← A + I % Add identity matrix I 5:$\overline{M}\leftarrow{\mathbf{1} - M}$ % Binary complement of M 6:$u\leftarrow{\max\left(\left. \overline{u}/\left\| \overline{u} \right\| \right.,0 \right)}$; d ← d0; α ← 1 7:while u not in binary state do 10: % Gradient projected on Sn tangent bundle: 13: while Δu ≮ tol or ΔF ≮ tol do 15: while Armijo = False do % Backtracking line search 22: if Armijo = False then 24: else $\alpha\leftarrow\left.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Continuous-Relaxation Maximal Clique Algorithm", "weight": 1.0} -->

\alpha/\sqrt{\beta} \right.$ % Increase α 27:C ← {i: ui > 0} % Vertices that form maximal clique Algorithm 2 Continuous-Relaxation Maximal Clique Optimization formulation: The maximum clique problem in an undirected and unweighted graph of $n$ vertices can be formulated as where $A \in {\{ 0,1\}}^{n \times n}$ is the adjacency matrix with ${A{(i,j)}} = 1$ if and only if vertices $u_{i}$ and $u_{j}$ are connected. The optimization variable $u$ is a binary vector of $n$ elements, where $1$ entries indicate vertices that form a clique. As $u$ is binary, the constraint ${u_{i}u_{j}} = 0$ if ${A{(i,j)}} = 0$ implies that if vertices $u_{i}$ or $u_{j}$ are disconnected, then at most one of them can be selected.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Continuous-Relaxation Maximal Clique Algorithm", "weight": 1.0} -->

For example, consider the graph in Fig. 1 with the adjacency matrix $A$ and solution candidates $u,\overline{u}$ as Both $u$ and $\overline{u}$ satisfy the constraints. Solution $u$ is the global optimum with the objective value of $3$ (the size of the maximum clique, and the number of $1$ entries in $u$), while $\overline{u}$ gives the objective value of $2$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Continuous-Relaxation Maximal Clique Algorithm", "weight": 1.0} -->

By defining $M\overset{\text{def}}{=}{A + I}$, where $I$ is the identity matrix of appropriate size, it is straightforward to show that problem is equivalent to This follows by observing that in and the constraints are identical in the sense that disconnected vertices cannot be selected jointly in the solution. Further, if $u^{*}$ is an optimal solution of and it has $m$ one entries, then the objective values of and will both be identical and equal to $m$ (e.g., $u$ and $\overline{u}$ in give objective values of $3$ and $2$ in).

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Continuous-Relaxation Maximal Clique Algorithm", "weight": 1.0} -->

Continuous relaxation: To overcome the NP-hardness of problem, an approximate solution can be obtained by a continuous relaxation, where the binary domain $u \in {\{ 0,1\}}^{n}$ is relaxed to the set of non-negative real numbers $u \in {\mathbb{R}}_{+}^{n}$. Gradient-based optimization routines with polynomial time complexity can solve the relaxed problem, and the relaxed solution can be projected/rounded to the nearest binary. The issue of this approach is that there is no guarantee that the binarized solution is a feasible solution that satisfies the constraints of the original problem.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Continuous-Relaxation Maximal Clique Algorithm", "weight": 1.0} -->

Our relaxation is inspired by Belachew and Gillis, which integrates the constraints in into using the matrix $M_{d}$. The difference of this work with is that in the relaxation $\min_{u \in {\mathbb{R}}_{+}^{n}}{\|{M_{d} - {uu^{\top}}}\|}_{F}^{2}$ is used. Intuitively, any entry ${M_{d}{(i,j)}} = {- d}$ penalizes joint selection of disconnected vertices $u_{i}$ and $u_{j}$ by the amount $- {2d}$ in the objective. Hence, as $d$ increases, the entries of $u$ that violate clique constraints converge to zero.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B Continuous-Relaxation Maximal Clique Algorithm", "weight": 1.0} -->

Optimality guarantees: When $d \geq n$ (see ), the optima of the proposed relaxation are theoretically guaranteed to correspond to the optima of the original maximum clique problem. That is, a local optimum of corresponds to a maximal clique, and a global optimum of corresponds to a maximum clique. It is by no means trivial to prove this statement, and the interested reader should refer to Theorems 3-5 in that prove this statement for the relaxation $\min_{u \in {\mathbb{R}}_{+}^{n}}{\|{M_{d} - {uu^{\top}}}\|}_{F}^{2}$, and Theorem 2 in that establishes connections to our proposed relaxation.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Continuous-Relaxation Maximal Clique Algorithm", "weight": 1.0} -->

It is interesting to point out that any solution of has a binary state (this follows from the analysis in ). That is, the entries of a solution vector $u^{*} \in {\mathbb{R}}_{+}^{n}$ are either $0$ or equal to a positive scalar $c > 0$. These positive entries are indicators of vertices that form a maximal clique. Noting that can be (locally) solved in polynomial time by using a gradient-based solver, and the one-to-one correspondence between the optima of and the (NP-hard) maximum clique problem, one may think that the maximum clique problem can be solved in polynomial time. Note, however, that is a nonlinear optimization problem, potentially with many local optima, and depending on the initial guess the solver can converge to a local optimum instead of the global optimum. Finding the global optimum of, hence, remains an NP-hard problem.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Continuous-Relaxation Maximal Clique Algorithm", "weight": 1.0} -->

1:Input A: adjacency matrix 2:Output C: vertices that form maximal clique 3:K← compute core number of vertices % From 4:C← Algorithm1(A, K) % Degeneracy-ordered greedy clique 5:ℐ ← {i: K(vi) ≥ |C|} % Vertices with core number ≥ greedy clique size 6:A’ ← A(ℐ, ℐ) % Prune graph (only keep vertices in ℐ) 7:if A’ = ⌀ then Terminate % Maximum clique found 8:% Binary complement of greedy clique in pruned graph: 9:$\overline{u}\leftarrow\left({\overline{u}}_{i}:{\overline{u}}_{i} = 0{if}i \in C,{else},{\overline{u}}_{i} = 1,\forall_{i \in \mathcal{I}} \right)$ 10:C′← Algorithm2($A',\overline{u}$) % Continuous-relaxation clique 11:if |C’| >

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Continuous-Relaxation Maximal Clique Algorithm", "weight": 1.0} -->

|C| then C ← C′ % Return larger clique n: Number of graph vertices.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Continuous-Relaxation Maximal Clique Algorithm", "weight": 1.0} -->

s: Graph sparsity. ωgt: Ground truth maximum clique size. t: Runtime (milliseconds); the lower, the better. r: Maximum clique accuracy ratio (ω̂/ωgt); the closer to 1, the better. TABLE I: Comparisons of the maximum clique estimation accuracy and runtime for CLIPPER+ on DIMACS benchmark (bold is best).

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Continuous-Relaxation Maximal Clique Algorithm", "weight": 1.0} -->

Optimization algorithm: We present a custom solver for based on a projected gradient ascent approach, as described in Algorithm 2. Our approach is similar to the algorithm in our previous work CLIPPER; however, compared to, Algorithm 2 is significantly improved and uses the Armijo procedure for selecting the appropriate step size, which leads to more accurate results (as we will show in the comparisons).

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B Continuous-Relaxation Maximal Clique Algorithm", "weight": 1.0} -->

Problem is nonlinear with many local optima in general (corresponding to maximal cliques). To improve the odds of finding the global optimum (maximum clique) and escape local optima, in Algorithm 2 we use a homotopy approach where we increase $d$ incrementally in an outerloop (lines 7-26). As the penalty parameter $d$ increases incrementally by $\Delta d$ in each iteration of the outerloop (line 26), the elements of $u$ that violate the clique constraints are penalized further and $u$ converges to a feasible solution. This process continues until $d$ is large enough ($d \geq n$) and $u$ converges to a binary state, corresponding to a maximal clique. The $\Delta d$ increments can be chosen as a small constant (as done in ), however, in our implementation, we use a greedy scheme where we increase $d$ until the smallest element of $u$ that violates the clique constraint goes to zero in the next iteration.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Continuous-Relaxation Maximal Clique Algorithm", "weight": 1.0} -->

In the final step (line 27), the vertices of the maximal clique are identified as the non-zero elements of $u$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Continuous-Relaxation Maximal Clique Algorithm", "weight": 1.0} -->

The innerloop (lines 13-25) ensures that for each $d$ increment enough iterations of the gradient ascent are performed for the solution $u$ to reach a steady state. Noting that the constraint manifold of the optimization problem is ${\mathbb{R}}_{+}^{n} \cap S^{n}$, where $S^{n}$ is the unit sphere, to speed up the convergence, we project the gradient ${{\nabla F}{(u)}}\overset{\text{def}}{=}{2M_{d}u}$ onto the tangent bundle of $S^{n}$ at $u$ and move along the orthogonal projection ${{\nabla F_{\perp}}{(u)}} = {2{({I - {uu^{\top}}})}M_{d}u}$ (line 11).

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Continuous-Relaxation Maximal Clique Algorithm", "weight": 1.0} -->

To find an appropriate step size $\alpha$ along the projected gradient, we use backtracking line search (lines 15-24) with the Armijo procedure (lines 21-24), which guarantees a sufficient increase in the objective at each innerloop iteration. The convergence of the algorithm to a first-order optimal point is guaranteed by the convergence property of the projected gradient with Armijo steps. The solution update is computed in line 16, retracted back onto the constraint manifold (line 17), and the gradient ascent continues until convergence.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Continuous-Relaxation Maximal Clique Algorithm", "weight": 1.0} -->

Computational Complexity: The worst-case complexity of Algorithm 2 is $O{(n^{4})}$. This is because the gradient computation (line 19) involves matrix-vector multiplications, which have $O{(n^{2})}$ complexity, and profiling shows this is where most of the time is spent. The number of backtracking iterations (line 15) and gradient ascent iterations (line 13) can vary depending on the parameters and the data matrix, but it is linear in problem size ($O{(n)}$) for quadratic objective ${F{(u)}} = {u^{\top}M_{d}u}$. Lastly, the number of outerloop iterations (line 7) depends on $\Delta d$ increments (line 26) required to reach $d \geq n$ (at which point the solution is guaranteed to converge to the binary state). This is also linear in problem size.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-C CLIPPER+ Maximal Clique Algorithm", "weight": 1.0} -->

Both Algorithms 1 and 2 are algorithms for finding maximal cliques. The greedy approach of Algorithm 1 runs fast but gives relatively less accurate estimates of the maximum clique size when the graph is not sparse. In contrast, the optimization approach of Algorithm 2 is relatively slower but more accurate. The main motivation of the proposed CLIPPER+ algorithm is to combine these two algorithms and thereby combine their relative benefits.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-C CLIPPER+ Maximal Clique Algorithm", "weight": 1.0} -->

The enable this combination, recall that the core number of a vertex is the largest integer $k$ such that the degree of the vertex remains non-zero when all vertices of degree less than $k$ are removed. If a graph contains a clique of size $k$, then each vertex in the clique must have a degree of $k - 1$ or larger, and therefore a core number of $k - 1$ or larger. For this reason, if we hope to find a larger clique, say of size $k + 1$, then only vertices that have a core number $k$ or higher can be candidates. Using this observation, CLIPPER+, detailed in Algorithm 3, first runs the greedy algorithm and obtains a maximal clique (line 4). Assuming this clique has size $k$, if the graph contains a larger clique, then vertices must have core numbers of $k$ or larger. Therefore, the algorithm prunes the graph by removing vertices with core numbers strictly less than $k$ (line 6). The pruning effectively limits the search space for the optimization (line 10) by reducing the number of vertices, which improves the runtime.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C CLIPPER+ Maximal Clique Algorithm", "weight": 1.0} -->

If the clique recovered by the greedy algorithm is the maximum clique, then pruning the graph removes all the vertices and therefore we can terminate early (line 7). This early termination particularly occurs when the graph is sparse, which leads to a significant speed-up over running the optimization-based algorithm on the original graph.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-C CLIPPER+ Maximal Clique Algorithm", "weight": 1.0} -->

When the optimization-based algorithm is required, the initial guess used for the optimization can be chosen strategically to improve the chance of finding the maximum clique. This can be done by choosing an initial guess vector that is a binary complement of the clique found from the greedy approach (line 9), and thus help the algorithm to converge to a different clique solution. Lastly, the best solution is selected as the largest clique (line 11).

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-C CLIPPER+ Maximal Clique Algorithm", "weight": 1.0} -->

Computational Complexity: The worst-cast complexity of Algorithm 3 is $O{(n^{4})}$. This is because it sequentially combines Algorithms 1 and 2, and thus inherits the highest worst-case complexity of its components (all other steps in Algorithm 3 have lower complexity). This basic worst-case complexity analysis is independent of any input graph structure. The numerical results in the experimental section provide a good indication of how the complexity translates to runtimes for various graph sizes in the practical applications.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experimental Evaluations", "weight": 1.0} -->

We evaluate the performance of CLIPPER+ (Algorithm 3) in terms of the maximum clique estimation accuracy and runtime. In addition, we provide ablation studies of CLIPPER+ by reporting the results of its standalone greedy (Algorithm 1) and optimization (Algorithm 2) components. We show that CLIPPER+ achieves a performance superior to these standalone components through combining them.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experimental Evaluations", "weight": 1.0} -->

Algorithms: We test both classical and state-of-the-art maximum clique estimation algorithms. Classical works include Pelillo and Ding et al. based on relaxations of the Motzkin-Straus formulation. State-of-the-art include our implementation of the greedy parallel maximum clique (PMC) algorithm in Algorithm 1 (which is theoretically equivalent to ROBIN ), the algorithm by Belachew and Gillis, and our prior CLIPPER algorithm.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Experimental Evaluations", "weight": 1.0} -->

Benchmarks: Our evaluations examine finding the maximum clique on general graphs, as well as graphs that result from the graph formulation of synthetic/real-world point cloud registration problems. While general graphs can have any structure, the registration graphs have certain patterns (e.g., sparsity) that significantly affect the results. Fortunately, as we will see, finding the maximum clique is empirically easier on graphs that result from registration.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experimental Evaluations", "weight": 1.0} -->

Platform and implementations: All benchmarks are run on a machine with an Intel Core i9 Processor and 32 GB RAM. The algorithms by Pelillo, Ding, and Belachew are implemented in Matlab by their original authors. Our prior work CLIPPER is also implemented in Matlab. The "Greedy" (Algorithm 1), "Optim" (Algorithm 2), and CLIPPER+ algorithms are implemented in C++, which interface to Matlab via binary MEX binders for benchmarking.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-A Maximum Clique Benchmark---DIMACS", "weight": 1.0} -->

Dataset: To evaluate the algorithms on general graphs, we use the DIMACS benchmark, which was introduced in 1996 and has been used widely since then to benchmark the maximum clique algorithms. The DIMACS dataset consists of graphs for which finding the maximum clique is challenging. In the interest of space, we present the result on a subset of smaller graphs in this dataset, shown in Table I. While DIMACS graphs are relatively small (100-4000 vertices), they are dense and contain more edges compared to graphs resulting from registration. Despite the dataset being around for more than 25 years, the maximum clique of some graphs is still unknown, demonstrating the difficulty of the problem. For instance, on the `C250.9` graph, the (multi-threaded) PMC exact algorithm, used in this work for ground truth generation and in TEASER for certifiable registration, took $28$ minutes on our machine to find the maximum clique.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-A Maximum Clique Benchmark---DIMACS", "weight": 1.0} -->

Evaluation: Table I compares the accuracy and runtime of algorithms. The graph sparsity is defined as $s\overset{\text{def}}{=}{1 - \frac{|E|}{|E_{\max}|}} \in {\lbrack 0,1\rbrack}$, where $|E|$ is the number of graph edges, and $|E_{\max}|$ is the maximum possible number of edges. The small values of $s$ show that DIMACS graphs are generally dense. The accuracy ratio is measured by $r\overset{\text{def}}{=}{\hat{\omega}/\omega_{gt}}$, where $\hat{\omega}$ is the clique size found by the algorithm, and $\omega_{gt}$ is the ground truth maximum clique size. The ratio of $1$ indicates that the maximum clique is found, hence, the closer $r$ is to $1$, the more accurate an algorithm is. CLIPPER+ outperforms all algorithms in the overall accuracy.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-A Maximum Clique Benchmark---DIMACS", "weight": 1.0} -->

Unsurprisingly, the greedy algorithm has the best overall runtime due to its low computational complexity; however, it has a lower accuracy. By combining the greedy and optimization algorithms, CLIPPER+ obtains high accuracy and better overall runtime compared to the optimization-only approach (e.g., a $\sim$`<!-- -->`{=html}10x reduction of runtime from $29.4$ to $3.6$ milliseconds on `brock200_2`).

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B Registration Benchmark---Stanford Bunny", "weight": 1.0} -->

N: Total number of overlapping point cloud scans on which registration is performed. $\overline{o⁢p}$: Mean of outlier percentages in putative associations. $\overline{n}$: Mean graph size. $\overline{s}$: Mean graph sparsity. $\overline{t}$: Mean runtime (milliseconds); the lower, the better. $\overline{r}$: Mean maximum-clique accuracy ratio (ω̂/ωgt); the closer to 1, the better. TABLE II: Comparisons of maximum clique estimation accuracy and runtime of CLIPPER+ on real-world point cloud registration datasets (bold is best).

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-B Registration Benchmark---Stanford Bunny", "weight": 1.0} -->

Using the Stanford Bunny point cloud, shown in Fig. 2, we evaluate CLIPPER+ as an algorithm for global point cloud registration in various outlier regimes.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-B Registration Benchmark---Stanford Bunny", "weight": 1.0} -->

Dataset: The (downsampled) Bunny point cloud consists of $1000$ points that fit in a cube of size $0.2m$. To generate a second point cloud, we add uniform noise in the range $\lbrack{- {\epsilon/2}},{\epsilon/2}\rbrack$ to all points, where $\epsilon$ is set as the mean distance of all points to their nearest neighbors in the Bunny point cloud. Additionally, $1000$ outlier points randomly drawn from a sphere of radius $1m$, centered at the bunny point cloud, are added to simulate clutter. From the set of all possible associations between the points in the two point clouds, $200$ associations are randomly selected from the set of inlier and outlier associations (we keep this number small to be able to find the ground truth maximum clique).

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-B Registration Benchmark---Stanford Bunny", "weight": 1.0} -->

We consider different outlier ratios (ranging from $0\%$ to $98\%$ in $2\%$ increments), to test scenarios with various data association accuracy, as shown in Fig. 2. We use the noise $\epsilon$ as the threshold to generate the consistency graph (according to Section III). The ground truth maximum clique is found by running the exact PMC algorithm. Evaluations of maximum clique estimation accuracy and runtime are performed across $50$ Monte Carlo runs/graphs for each increment of the outlier percentage.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-B Registration Benchmark---Stanford Bunny", "weight": 1.0} -->

Evaluation: Fig. 3 compares the accuracy ratio $r$ of algorithms across all runs and all outlier ratios. CLIPPER+ clearly demonstrates the highest accuracy because the distribution of $r$ is closest to $1$. Interestingly, while the greedy and optimization algorithms returned low-accuracy solutions in some instances, by combining these algorithms CLIPPER+ obtains an accuracy beyond these standalone components.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-B Registration Benchmark---Stanford Bunny", "weight": 1.0} -->

Fig. 4 shows the mean of the accuracy ratio $r$ (averaged across $50$ Monte Carlo runs at each outlier percentage increment) versus the outlier percentage. The accuracy of the greedy approach is low in low-outlier regimes (which have dense consistency graphs, see Fig. 2). As the outlier percentage increases and the graph becomes sparser, the accuracy of the greedy method improves. Both CLIPPER+ and optimization algorithms retain a high accuracy ratio across all outlier percentages.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-B Registration Benchmark---Stanford Bunny", "weight": 1.0} -->

The mean runtime of the algorithms is shown in Fig. 5. The runtime of the optimization method remains roughly the same, while the runtime of the greedy method improves as the outlier ratio grows and the graph becomes sparser. The runtime of CLIPPER+ in low outlier regimes is roughly equal to the compound runtimes of its greedy and optimization components because in such regimes pruning the graph based on core numbers does not remove a significant number of vertices (if any). However, as the outlier ratio increases and the graph becomes sparser, pruning removes more vertices and its speed-up effect becomes more apparent. This can be seen around the $20\%$ outlier ratio, where CLIPPER+ becomes faster than the optimization method, and its speed improves further as the outlier percentage increases.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-C Registration Benchmark---Real-World Point Clouds", "weight": 1.0} -->

Datasets: We use sequences in the real-world 7-Scenes, Sun3D, and ETH datasets (similar to 3DMatch and 3DSmoothNet evaluations). Sun3D and 7-Scenes are dense indoor RGB-D point clouds, while ETH is an outdoor LiDAR point cloud. In each sequence, we consider pairs of point clouds (or scans) that have an overlap. To increase registration speed, we downsample the point clouds by discretizing the 3D space into cubes of size $\epsilon = {0.05m}$ for 7-Scenes and Sun3D datasets, and $\epsilon = {0.1m}$ for the ETH dataset, and using the mean of the point coordinates in each cube as a single-point representative. For each downsampled point, FPFH descriptor vectors are computed and associated bilaterally based on their $l_{2}$ norm distance using the k-nearest neighbors algorithm. To generate the ground truth for our evaluations, we use the exact maximum clique algorithm of to find the largest set of geometrically consistent associations in these putative FPFH associations.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-C Registration Benchmark---Real-World Point Clouds", "weight": 1.0} -->

We store results if this maximum clique solution correctly registers the point clouds according to the ground truth provided by the datasets---the maximum clique/likelihood solution may register points wrongly due to practical limitations such as repetitive patterns (perceptual aliasing), insignificant overlap between the point clouds, and lack of any inlier associations caused by downsampling and FPFH inaccuracies. For evaluations, the consistency graph is generated according to Section III from putative FPFH associations, using the downsampling $\epsilon$ as the consistency threshold. An evaluation instance is shown in Fig. 6.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-C Registration Benchmark---Real-World Point Clouds", "weight": 1.0} -->

Evaluation: Table II presents the evaluation results for all datasets and algorithms. CLIPPER+ outperforms all algorithms in accuracy on all datasets/sequences. The greedy algorithm has the smallest runtime at the expense of the lowest overall accuracy. The standalone optimization algorithm has similar accuracy to CLIPPER+. However, except on the last sequence, it is around $2$x slower. This demonstrates the advantage of CLIPPER+ over its standalone greedy and optimization components.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-C Registration Benchmark---Real-World Point Clouds", "weight": 1.0} -->

Lastly, we point out the high outlier ratios of FPFH associations (e.g., on average, $99.4\%$ of associations in the `wood_autumn` sequence are outliers). Due to the maximum clique solution correctly registering the point clouds in our benchmark, the accuracy ratio $r$ shows the point cloud registration success rate. Thus, CLIPPER+ correctly registers the point clouds in $99\%$ of the trials despite extreme outlier percentages. This is what distinguishes CLIPPER+ from existing robust registration frameworks (such as RANSAC ), that can fail in these high-outlier regimes.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

We presented CLIPPER+, a maximal-clique-finding algorithm for unweighted graphs that enables robust global registration in robotics and computer vision applications. Future work includes investigating alternative optimization methods such as second-order or quasi-Newton methods, and an extension to the weighted graphs based on our previous work (designed for weighted graphs) and an extension of core numbers to weighted settings (studied in ). We also plan to integrate the algorithm in point cloud registration pipelines as the outlier rejection module to improve the runtime and outlier rejection capacity.
