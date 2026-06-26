<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

CLIPPER: A Graph-Theoretic Framework for Robust Data Association

Topics include Robustness, Graphs, Accuracy, Optimization, CLIPPER.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present CLIPPER (Consistent LInking, Pruning, and Pairwise Error Rectification), a framework for robust data association in the presence of noise and outliers. We formulate the problem in a graph-theoretic framework using the notion of geometric consistency. State-of-the-art techniques that use this framework utilize either combinatorial optimization techniques that do not scale well to large-sized problems, or use heuristic approximations that yield low accuracy in high-noise, high-outlier regimes. In contrast, CLIPPER uses a relaxation of the combinatorial problem and returns solutions that are guaranteed to correspond to the optima of the original problem. Low time complexity is achieved with an efficient projected gradient ascent approach. Experiments indicate that CLIPPER maintains a consistently low runtime of 15 ms where exact methods can require up to 24 s at their peak, even on small-sized problems with 200 associations. When evaluated on noisy point cloud registration problems, CLIPPER achieves 100% precision and 98% recall in 90% outlier regimes while competing algorithms begin degrading by 70% outliers.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In an instance of associating noisy points of the Stanford Bunny with 990 outlier associations and only 10 inlier associations, CLIPPER successfully returns 8 inlier associations with 100% precision in 138 ms. Code is available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Finding correct one-to-one correspondences between two sets of objects $\mathcal{A}\overset{\text{def}}{=}{\{ a_{1},\ldots,a_{n}\}}$ and $\mathcal{A}'\overset{\text{def}}{=}{\{ a_{1}',\ldots,a_{m}'\}}$ is a fundamental problem in robotics, arising in a wide range of perception and estimation pipelines. In practice, observations of objects are "noisy" and "partial", i.e., when an unknown number of objects in $\mathcal{A}$ do not correspond to any object in $\mathcal{A}'$ (outliers). The traditional linear assignment approach based on corresponding objects of high similarity, e.g., using the Hungarian or auction algorithms, is not robust to high-noise, high-outlier regimes, leading to incorrect correspondences.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this work, we propose the CLIPPER (Consistent LInking, Pruning, and Pairwise Error Rectification) framework which leverages the notion of geometric consistency between object pairs to find correct correspondences in these extreme regimes. Our primary motivation is robust perception with applications such as those shown in Fig. 1, SLAM/loop closure, point cloud registration, shape alignment, object detection, and multiple object tracking. However, our framework is general and applicable to other pairwise data association problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

When an attribute between objects in set $\mathcal{A}$ is the same as the attribute between their correctly associated objects in $\mathcal{A}'$, these objects are considered geometrically consistent (e.g., see Fig. 2). Incorporating geometric consistency in data association ultimately leads to a combinatorial optimization, such as maximum clique, maximum consensus, or quadratic assignment formulations. Relaxations of this NP-hard problem exist, but exhibit poor performance in high-outlier regimes or for large problem size. In contrast, CLIPPER maintains high precision with low runtime across various outlier-regimes and problem sizes.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

(a) Scaled point cloud registration (b) Line cloud registration (c) Plane registration (top-down view) (d) Planar patch registration Figure 1: Applications were the CLIPPER framework is used for robust data association: (a) noisy point cloud registration with unknown scale and outliers; (b) noisy line cloud registration; (c) plane cloud registration for LiDAR sensor calibration in outdoor, urban environment (planes indicated by colored points, sensor scans are correctly registered); (d) planar patch registration (extracted from LiDAR scans of). In (a), (b), (c) magenta and green lines indicate incorrect and correct associations, respectively. Input associations can be generated from an external matching procedure or an all-to-all hypothesis in the case of no prior information. Each setting generates a consistency graph that CLIPPER operates on to identify which of the input associations are the most geometrically consistent.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

CLIPPER incorporates the concept of geometric consistency in a graph-theoretic framework, and proposes finding consistent association (inliers) by finding the densest subgraph. This formulation is particularly suited to weighted graphs and improves precision compared to maximum clique frameworks which are limited to binary graphs. CLIPPER uses the continuous relaxation technique introduced in to guarantee that the recovered solution corresponds to a dense subgraph. Using projected gradient ascent with backtracking line search, CLIPPER achieves a consistently low runtime as compared to other algorithms. Further, our experiments show that CLIPPER is capable of attaining 100% precision even in high outlier regimes where other algorithms breakdown.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In summary, the contributions of this work include: An optimization formulation for selecting inlier associations suitable for both binary and weighted graphs.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

A relaxation of the resulting NP-hard optimization problem with optimality guarantees (see Sec III-A).

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

A polynomial-time algorithm for solving the relaxed formulation based on projected gradient ascent, scalable to large-sized data association problems.

<!-- chunk {"id": "body-0012", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Additionally, we include a discussion on the application of geometric consistency to various observation types (e.g., points, lines, planes) commonly found in robotic perception. Finally, we benchmark CLIPPER against the state of the art when finding associations between two point clouds. We find that CLIPPER is able to achieve 100% precision in 99% outlier regimes, where the performance of competing algorithms begin to degrade.

<!-- chunk {"id": "body-0013", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Related works most pertinent to this work include Bailey et al., where geometric consistency is leveraged for 2D LiDAR scan matching. Formulated as a maximum common subgraph problem, their technique resulted in a binary consistency graph for which the maximum clique indicated the correct data association. Leordeanu and Hebert built on this graph-theoretic idea and instead constructed a weighted consistency graph, where edge weights represent the geometric consistency of associations. Enqvist et al. noted the suboptimality of and proposed a vertex covering formulation, essentially an alternative to the maximum clique formulation of. Parra et al. proposed a practical maximum clique algorithm for geometric consistency based on branch and bound and graph coloring. Recent algorithms leveraging these ideas for estimation tasks include PCM, where maximum cliques correspond to the largest set of pairwise-consistent loop closure measurements, and TEASER, where maximum cliques correspond to inlier associations for point cloud registration, further formalized in ROBIN. CLIPPER advances these works with a continuous relaxation applicable to weighted graphs.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Graph-Theoretic Formulation", "weight": 1.0} -->

A standard approach for robust data association in the presence of noise and outliers is to find the largest set of geometrically consistent associations. This problem can be formulated in a graph-theoretic framework. In this section, we review the consistency graph framework and the construction of the affinity matrix.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Consistency Graph", "weight": 1.0} -->

The consistency of associations can be assessed and represented in the graph-theoretic framework of the consistency graph. The consistency graph $\mathcal{G}$ of $n$ associations consists of $n$ vertices, where each vertex represents an association. Edges between the vertices of $\mathcal{G}$ show that their corresponding associations are consistent. The example in Fig. 2b illustrates the consistency graph for the associations in Fig. 2a. Since rotation and translation are distance-preserving transformations, the distance between the points in one set should be identical (in the noiseless setting) to their counterparts in the other set when associations are correct. This attribute can be used to assess the geometric consistency of two associations, where an edge between two vertices of $\mathcal{G}$ indicates that the distances between the points matched by the associations are the same. The largest set of mutually consistent associations is given by the largest fully connected subgraph (maximum clique), which consists of vertices $u_{1},u_{2},u_{4}$ in the example of Fig. 2b.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Affinity Matrix", "weight": 1.0} -->

The affinity matrix $M$ of a consistency graph with $n$ vertices is an $n \times n$ symmetric matrix with entries in the interval $\lbrack 0,1\rbrack$. The diagonal entries $M{(i,i)}$ measure the similarity of the data points that association $i$ matches, e.g., based on the similarity of point "descriptors" (for instance, the FPFH descriptors for point clouds ). Scores of $0$ and $1$ indicate the lowest and the highest similarity, respectively. The diagonal entries of $M$ are set to $1$ when similarity information is not available. In this case, $M = {A + I}$, where $A$ is the (weighted) adjacency matrix of the consistency graph and $I$ is the identity matrix. The off-diagonal entries $M{(i,j)}$ measure the geometric consistency of association pairs $i$ and $j$, and similarly range from $0$ to $1$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Affinity Matrix", "weight": 1.0} -->

For example, in the point cloud registration problem, the distance between two points $a,b$ matched to $a',b'$ by associations $u_{i}$ and $u_{j}$ can be used to measure the consistency as ${M{(i,j)}}\overset{\text{def}}{=}{s\left( {{\|{a\text{-}b}\|}\text{-}{\|{a'\text{-}b'}\|}} \right)} \in {\lbrack 0,1\rbrack}$. Here, $s:{{\mathbb{R}}\rightarrow{\lbrack 0,1\rbrack}}$ is a scoring function such that ${s{}} = 1$ and ${s{(x)}} = 0$ for ${|x|} > \epsilon$, as illustrated in Fig 2c. The threshold $\epsilon$ is based on a bounded noise model with a noise range of $\epsilon/2$ on the point coordinates.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Affinity Matrix", "weight": 1.0} -->

Hence, if the distance between the points differs more than this threshold, the associations are considered inconsistent. Another source of inconsistency, referred to as the distinctness constraint, is when correct associations are expected to be one-to-one. Hence, for any two associations $i$ and $j$ that originate or terminate at the same point, ${M{(i,j)}}\overset{\text{def}}{=}0$ to indicate mutual inconsistency of associations. Lastly, we note that a binary scoring function, e.g., ${r{(x)}}:{{\mathbb{R}}\rightarrow{\{ 0,1\}}}$ in Fig. 2c, can be used. This will lead to a binary affinity matrix, shown in Fig. 2d.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Optimization Formulation of CLIPPER", "weight": 1.0} -->

Given the consistency graph $\mathcal{G}$ with $n$ vertices representing associations (all-to-all or putative), and its $n \times n$, symmetric affinity matrix $M$, we propose the problem for finding the densest subset of consistent associations. Here, the optimization variable $u$ is a binary vector of size $n$, with $1$ elements indicating associations that are selected as inliers, and $0$'s otherwise. Since $u$ is binary, the constraint ${u_{i}u_{j}} = 0$ ensures that if ${M{(i,j)}} = 0$, then at most one of the associations $u_{i}$ or $u_{j}$ is selected in the answer.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Optimization Formulation of CLIPPER", "weight": 1.0} -->

When $M$ is binary (e.g., obtained by using the scoring function $r{(x)}$ in Fig. 2c) and has one diagonal entries, it is straightforward to show that simplifies to Problem is known as the maximum clique problem (MCP), and its solution gives the largest set of consistent associations. The MCP framework is used frequently in the literature for data association in the presence of noise and a large number of outliers, where the vertices/associations in the maximum clique are considered as the correct/inlier correspondences. The justification for this consideration is based on the assumption that the noise and outlier points are random, unbiased, and unstructured, thus they are not expected to form a large clique in the consistency graph. We note that MCP is a well-known NP-hard problem in its full generality, hence, algorithms that rely on solving become computationally intractable as the problem size grows.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimization Formulation of CLIPPER", "weight": 1.0} -->

The density of a graph is defined as the total sum of edge weights divided by the number of vertices. The densest subgraph is the subset of graph vertices and their corresponding edges that have the highest density. Given a graph $\mathcal{G}'$ with affinity matrix $M'$ (with 1 diagonal entries), the densest subgraph of $\mathcal{G}'$ is found from where elements $u_{i} = 1$ in the solution correspond to the vertices in the densest subgraph. Noting the similarity of the objectives in and, problem can be interpreted as finding the densest, fully connected subgraph of $\mathcal{G}$. The full connectivity requirement is due to the constraints, which prohibit the selection of vertices $u_{i},u_{j}$ that are not connected, i.e., ${M{(i,j)}} = 0$. The densest-subgraph objective in is crucial in the weighted case, and sets it apart from the maximum edge weighted clique problem.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Optimization Formulation of CLIPPER", "weight": 1.0} -->

For example, consider a weighted matrix $M$ and two solution candidates $u,\overline{u}$ as The MCP objective, or the unnormalized objective of $u^{\top}Mu$, returns $\overline{u}$ as the optimum solution, whereas the block of $M$ corresponding to $\overline{u}$ has low consistency scores of $0.2$ between the vertices/associations. On the other hand, the normalized objective of takes values of $2$ and $1.4$ for $u$ and $\overline{u}$, respectively, leading to selection of the smaller, but more consistent subgraph. Example further highlights the importance of choosing a weighted scheme over binary in the affinity matrix, since the maximum clique formulation returns $\overline{u}$ as a solution. While this problem can be avoided by choosing a smaller $\epsilon$, a conservative threshold leads to classifying correct associations as outliers (i.e., lower output recall). Further, a weighted scheme can resolve symmetric cases where two binary cliques have the same size.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Continuous Relaxation", "weight": 1.0} -->

The main challenges in solving are the combinatorial complexity of the problem due to its binary domain and the nonlinearity of the objective in $u$. This makes it intractable to solve the problem to global optimality in real time, even for small-sized data association problems. A standard workaround is to relax the domain and the constraints of to obtain a continuous problem amenable to fast solution, followed by projecting this solution back to the domain and constraint manifold of the original problem. Among the relaxation strategies that can be considered, the main advantage of the following approach is that the solutions obtained from the relaxed problem correspond to optima of the original problem, as will be discussed shortly.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Continuous Relaxation", "weight": 1.0} -->

We propose the relaxation of as where ${\mathbb{R}}_{+}$ is the set of non-negative reals, $\parallel \cdot \parallel$ is the $\ell_{2}$ vector norm, and where $d > 0$ is a positive scalar. This approach is inspired, which directly integrates the constraints of the original problem into the continuous formulation of via the matrix $M_{d}$. Intuitively, when ${M_{d}{(i,j)}} = {- d}$, the scalar $d$ penalizes joint selection of $u_{i},u_{j}$ in the objective by the amount $- {2du_{i}u_{j}}$. Hence, as $d$ increases the entries of solution $u$ that violate the constraints are pushed to zero.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Continuous Relaxation", "weight": 1.0} -->

When $d \geq n$, (local or global) optima of satisfy the constraints in the original problem, i.e., ${u_{i}u_{j}} = 0$ if ${M{(i,j)}} = 0$. This fact has been shown in for the case when $M$ is a binary matrix. While we have extended the proof to the weighted case, this discussion is beyond the space constraints of this paper and will be presented in a subsequent journal submission. We remark that since is an NP-hard problem, depending on the initial condition an optimization algorithm used for solving may converge to a local optima. To guarantee finding the global optima, it would be required to search the entire space of solutions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Continuous Relaxation", "weight": 1.0} -->

Given a solution $u$ of with $d \geq n$, let $\mathcal{G}' \subseteq \mathcal{G}$ represent the subgraph that corresponds to the nonzero elements of $u$, and $M'$ be the submatrix of $M$ that corresponds to $\mathcal{G}'$. Noting that $u$, and therefore $\mathcal{G}'$, satisfies the constraints, problem reduces to binarizing $u$ such that the objective is maximized. This is equivalent to the densest subgraph problem of, where the goal is to find $\mathcal{G}^{\operatorname{\prime\prime}} \subseteq \mathcal{G}'$ that has the maximum density.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Continuous Relaxation", "weight": 1.0} -->

The densest subgraph problem can be solved in polynomial time using existing algorithms, but a good approximate answer can be obtained immediately by selecting the $\hat{\omega}\overset{\text{def}}{=}{{round}{({u^{\top}Mu})}}$ largest elements of $u$ as vertices of $\mathcal{G}^{\operatorname{\prime\prime}}$. The justification follows from the well-known facts that $u^{\top}Mu$, which is the spectral radius of $\mathcal{G}'$, is a tight upper bound for the graph's density and nonzero elements of $u$, which form the principal eigenvector of $M'$, represent centrality of their corresponding vertices, which is a measure of connectivity for a vertex in the graph.

<!-- chunk {"id": "body-0028", "role": "body", "section": "CLIPPER Algorithm", "weight": 1.0} -->

The CLIPPER algorithm consists of 1) obtaining a solution $u$ of via a projected gradient ascent approach with backtracking line search; and 2) estimating the densest cluster in $u$ by selecting the $\hat{\omega}$ largest elements.

<!-- chunk {"id": "body-0029", "role": "body", "section": "CLIPPER Algorithm", "weight": 1.0} -->

Algorithm 1 seeks a feasible subgraph by incrementally increasing the penalty parameter $d$ (Line 13) and solving via gradient ascent (Lines 7-12). Noting that any optimal solution $u$ lies on the boundary of ${\| u\|} \leq 1$, the constraint manifold can be reduced to ${\mathbb{R}}_{+}^{n} \cap S^{n}$, where $S^{n}$ is the unit sphere. Instead of moving directly along the gradient ${{\nabla F}{(u)}}\overset{\text{def}}{=}{2M_{d}u}$, we first project onto the tangent space of $S^{n}$ at $u$ (Line 9) and move according to this orthogonal projection ${\nabla F_{\perp}}{(u)}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "CLIPPER Algorithm", "weight": 1.0} -->

To move quickly in the search space, the step size $\alpha$ is chosen greedily so that if there is a $u_{i}$ to be penalized (i.e., ${\nabla F_{\perp}} < 0$ and $u > 0$), a gradient step would cause $u$ to hit the boundary of the positive orthant (Line 10). If no such $u_{i}$ exists, then $\alpha$ is set such that the gradient update step gracefully degrades into a power iteration. In either case, if $\alpha$ is chosen too large, backtracking line search is used to find an appropriate step (Line 11). The solution is projected back onto the constraint manifold (Line 12) and gradient ascent continues. Once $u$ has converged for the current value of $M_{d}$, $d$ is incrementally increased (Line 13) and gradient ascent runs again with new objective ${F{(u)}} = {u^{\top}M_{d}u}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "CLIPPER Algorithm", "weight": 1.0} -->

This process continues until $d \geq n$ and $u$ has converged. The convergence of the algorithm is guaranteed by the convergence property of the projected gradient approach.

<!-- chunk {"id": "body-0032", "role": "body", "section": "CLIPPER Algorithm", "weight": 1.0} -->

The final step of CLIPPER selects the densest component of the subgraph $\mathcal{G}'$ (Lines 14-15), as explained in Section III-A. Since for all ${M_{d}{(i,j)}} = {- d}$ elements $u_{i},u_{j}$ in the solution $u$ satisfy ${u_{i}u_{j}} = 0$, then ${u^{\top}Mu} = {u^{\top}M_{d}u}$. The vertices of the densest component are then identified as the largest $\hat{\omega}$ elements of $u$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "CLIPPER Algorithm", "weight": 1.0} -->

1:Input affinity matrix M ∈ n × n of 𝒢 2:Output 𝒢'', densest component of feasible subgraph 𝒢′ ⊆ 𝒢 3:u ← rand (n, 1) % initialize with uniform random in 5:while d not large enough do 7: while u not converged do 10: $\alpha = {\min\left\{ {{\alpha_{i}\overset{\text{def}}{=}\left| u_{i}/\left({\nabla F_{\perp}} \right)_{i} \right|}:{{\left({\nabla F_{\perp}} \right)_{i} < 0},{u_{i} > 0}}} \right\}}$ 11: u ← u + α ∇F⟂ (u) % α via backtracking line search 12: u ← max (u/∥u∥, 0) % project back onto ℝ+n ∩ Sn 14:ω̂ ← round (u⊤ Md u) % estimate cluster size using max eig 15:𝒢''← vertices corresponding to largest ω̂ elements of u

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Computational Considerations", "weight": 1.0} -->

Neglecting constant factors, the computational cost of Algorithm 1 is $\mathcal{O}{({|E|})}$ per iteration, where $|E|$ is the number of edges in the graph $\mathcal{G}$. Note that the orthogonal projection in Line 9 should be implemented as ${{\nabla F}{(u)}} - {u{\langle u,{{\nabla F}{(u)}}\rangle}}$, which costs $\mathcal{O}{({|V|})}$ operations, where $|V|$ is the number of vertices in the graph $\mathcal{G}$. Most of the time is spent computing the matrix-vector product ${{\nabla F}{(u)}} = {M_{d}u}$. All other operations run in at most $\mathcal{O}{({|V|})}$ operations.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Constructing The Consistency Graph for Common Robotics Applications", "weight": 1.0} -->

CLIPPER can be applied to a broad array of data association problems found in robotics. All that is required is to identify a geometric invariant in the data, i.e., a quantity that is invariant under transformation. This invariant feature is then used to score geometric consistency for which a consistency graph $\mathcal{G}$ can be constructed and CLIPPER can be used to quickly remove outlier associations. We briefly review how to score geometric consistency for the application examples in Fig. 1.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Constructing The Consistency Graph for Common Robotics Applications", "weight": 1.0} -->

Point Clouds In Section II-A we described how two points seen in each cloud will have the same pairwise distance if the association is correct. This idea can be extended to scaled point clouds by using three point correspondences to form triangles for which correct associations will preserve the ratio of side lengths. This leads to a tensor formulation which can be marginalized into an $n \times n$ affinity matrix.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Constructing The Consistency Graph for Common Robotics Applications", "weight": 1.0} -->

Plane Clouds A plane $\pi:{(n,d)}$ is given by its normal $n \in {\mathbb{R}}^{3}$ and distance from the origin $d$. An invariant feature of four planes is the four-way intersection point. However, the requirement of choosing four plane correspondences increases computational complexity. Instead, the simpler invariant of angle between normals $n_{i},n_{j}$ can be used resulting in the same consistency score as for line clouds.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Constructing The Consistency Graph for Common Robotics Applications", "weight": 1.0} -->

Patch Clouds A cloud of planar patches, e.g., extracted from LiDAR using, additionally provides the centroid and area of each patch. Although neither the centroid nor area are guaranteed to be invariant across views (e.g., partial view), these values can be used to assign a similarity score to corresponding planar patches by weighting the diagonal entries of the affinity matrix $M$. Geometric consistency is scored based on pairs of normals as with plane clouds.

<!-- chunk {"id": "body-0039", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

We first present precision and runtime comparisons of CLIPPER as an approximate maximum clique solver on binary graphs. Then, we demonstrate CLIPPER's ability to perform data association in different outlier regimes and its strengths as a dense subgraph solver against the state of the art. Comparisons are performed against Leordeanu & Hebert and Belachew & Gillis, which can also operate on weighted graphs. The exact parallel maximum clique (PMCx) solver and its initial heuristic (PMCh) step are also compared against, as it has recently been used for data association. We include results for CLIPPER when given a binary graph (CLIPPERb). Experiments are run in MATLAB on an i9-7920, 64 GB RAM with a C++ interface to PMC. We allowed 12 threads for PMC.

<!-- chunk {"id": "body-0040", "role": "body", "section": "VI-A Maximum Clique Finding in Synthetic Data", "weight": 1.0} -->

Given a data association problem and a scoring function $r{(x)}$ (see Fig. 2c), factors such as noise and outlier statistics result in consistency graphs ranging from dense to sparse. For example, in low outlier regimes, many associations are consistent and $\mathcal{G}$ is dense; conversely, in high outlier regimes with few consistent associations $\mathcal{G}$ is sparse. In this section, we evaluate CLIPPER against the state of the art as an approximate MC solver on graphs of varying sparsity. Graphs are generated from a complete graph that has increasingly more randomly selected edges removed according to the desired sparsity. Evaluations of precision and runtime are given across $50$ Monte Carlo trials. We emphasize that in this synthetic analysis, we are disregarding the ability of CLIPPER to find dense subgraphs in weighted graphs.

<!-- chunk {"id": "body-0041", "role": "body", "section": "VI-A Maximum Clique Finding in Synthetic Data", "weight": 1.0} -->

Fig. 3 shows the average clique size error of the approximate algorithms compared to the true clique size as provided by PMCx. Positive error indicates overestimation. In our evaluations, the graph size is limited to $n = 200$ due to the high runtime of PMCx (see Fig. 4). We observe that Leordeanu underestimates the clique size the most, while CLIPPERb and Belachew have the least average error across the entire sparsity range. An algorithm's ability to find the largest clique (or densest subgraph) in a consistency graph directly affects its precision and recall in data association.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VI-A Maximum Clique Finding in Synthetic Data", "weight": 1.0} -->

Fig. 4 shows the corresponding runtime of each algorithm. While PMCx (using 12 threads) is fast for sparser graphs, its runtime peaks in the low sparsity range due to the NP-hardness of exactly recovering the maximum clique. As low graph sparsity corresponds to data association scenarios with few outliers, this runaway of runtime is problematic for a robot operating in varying conditions. PMCh and Leordeanu acheive the fastest overall runtime, but as observed in Fig. 3, underestimate the clique size the most on average. CLIPPERb and Belachew strike a balance of precision and runtime across the sparsity range of binary graphs, with CLIPPERb performing consistently around $15\ {ms}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "VI-B Data Association for Bunny Dataset", "weight": 1.0} -->

Using the Stanford Bunny, seen in Fig. 5, we evaluate CLIPPER as a data association algorithm in varying outlier regimes. The Bunny model is first scaled to fit in a $1\ m$ cube and $1000$ points are randomly sampled. These points are arbitrarily rotated and translated into a second view, where noise uniformly sampled from $\lbrack{{- 1}\ {cm}},{1\ {cm}}\rbrack$ is added. For a model scale of $1\ m$, this level of noise could reasonably be expected from a sensor. Additionally, 200 outlier points randomly drawn from a $1\ m$ radius sphere are added in view 2 to simulate clutter. From the set of all-to-all associations, associations are randomly drawn according to the desired outlier ratio. This process creates putative associations that could have been generated from feature matching or, in the case of no prior information, an all-to-all hypothesis. Note that this is in stark contrast to ICP, which performs poorly unless good initial information is provided.

<!-- chunk {"id": "body-0044", "role": "body", "section": "VI-B Data Association for Bunny Dataset", "weight": 1.0} -->

To generate the consistency graph, pairwise consistency scores are computed as described in Section II-B. Weighted algorithms use the affinity matrix defined by ${s{(x)}}\overset{\text{def}}{=}{\exp{({- {\frac{1}{2}\frac{x^{2}}{\sigma^{2}}}})}}$ for ${|x|} \leq \epsilon$, and 0 otherwise. Binary algorithms use the affinity matrix defined by ${r{(x)}}\overset{\text{def}}{=}1$ for ${|x|} \leq \epsilon$, and 0 otherwise. To study the effects of outliers, we choose $\epsilon = {8\ {cm}}$ and $\sigma = {3\ {cm}}$ small enough so that all algorithms have 100% precision in the 0% outlier regime.

<!-- chunk {"id": "body-0045", "role": "body", "section": "VI-B Data Association for Bunny Dataset", "weight": 1.0} -->

By definition, precision $p \in {\lbrack 0,1\rbrack}$ is the ratio of correct associations to the total number of associations returned by an algorithm, and recall $r \in {\lbrack 0,1\rbrack}$ is the ratio of correct associations in an algorithm's output to the total number of associations in the ground truth. The best performance is achieved when both precision and recall are high. For many data association scenarios, precision is particularly important because a single outlier can have disastrous effects (e.g., loop closure in SLAM ). Precision, recall, and timing results vs outlier ratio are reported in Fig. 6, with precision/recall results called out in Table I. CLIPPER maintains 100% precision up to 90% outliers, leading in precision up to 99% outliers. We observe that CLIPPER and Leordeanu have a recall of 97% at 0% outliers, due to their use of the weighted scoring function $s{(x)}$. CLIPPER performs as expected in runtime, at about $150\ {ms}$ on average.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VI-B Data Association for Bunny Dataset", "weight": 1.0} -->

Belachew, however, takes significantly longer, requiring $10\ s$ at 0% outliers and at least $1\ s$ until a much sparser graph at 97% outliers.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VI-B Data Association for Bunny Dataset", "weight": 1.0} -->

A timing comparison is given in Fig. 7 with varying number of associations. The Bunny dataset is used with a randomly sampled outlier ratio in $0$--$10$% and is averaged across 5 Monte Carlo iterations. While PMC quickly achieves the maximum clique for sparse problems (see Fig. 4), its runtime can increase without bound in large, dense problem domains.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VI-B Data Association for Bunny Dataset", "weight": 1.0} -->

Fig. 8 illustrates the benefit gained by having a weighted affinity matrix, which is the flexibility to shape the scoring function $s{(x)}$ as opposed to the rigidity of using $r{(x)}$. By varying the shape of $s{(x)}$, the user can trade off recall for precision in very high outlier regimes. Fig. 5 shows CLIPPER removing all outlier associations in this regime.

<!-- chunk {"id": "body-0049", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

We presented CLIPPER, a graph-theoretic framework for robust data association using the notion of geometric consistency. CLIPPER was shown to consistently execute with low runtime and to outperform the state of the art, achieving 100% precision, 80% recall in 99% outlier regimes. These gains were found by implementing an efficient projected gradient descent algorithm and by formulating the data association problem on weighted graphs rather than binary.
