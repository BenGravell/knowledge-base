<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints

Topics include Motion planning, Robotics, Sampling-based methods, Nearest neighbors, Planning, Sampling, Nearest neighbor search, K-d tree.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Nearest-neighbor search dominates the asymptotic complexity of sampling-based motion planning algorithms and is often addressed with k-d tree data structures. While it is generally believed that the expected complexity of nearest-neighbor queries is O(log(N)) in the size of the tree, this paper reveals that when a classic k-d tree approach is used with sub-Riemannian metrics, the expected query complexity is in fact Theta(N^(p) log(N)) for a number p in [0, 1) determined by the degree of nonholonomy of the system. These metrics arise naturally in nonholonomic mechanical systems, including classic wheeled robot models. To address this negative result, we propose novel k-d tree build and query strategies tailored to sub-Riemannian metrics and demonstrate significant improvements in the running time of nearest-neighbor search queries.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sampling-Based algorithms such as Probabilistic Roadmaps (PRM), Rapidly exploring Random Trees (RRT) and their asymptotically optimal variants (PRM^∗^, RRT^∗^) are widely used in motion planning. These algorithms build a random graph of motions between points on the robot's configuration manifold.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

During the graph expansion, nearest-neighbor search is used to limit the computation to regions of the graph close to the new configurations and it is shown to dominate the asymptotic complexity of randomized planners. The notion of closeness appropriate for motion planning is induced by the length of the shortest paths between configurations, or in general, by the minimum cost of controlling a system between states.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

As compared to exhaustive linear search, efficient algorithms with reduced complexity have been studied in computational geometry and their use in motion planning has been highlighted as a factor of dramatic performance improvement. Among a variety of approaches, $k$-d trees are ideal due to their remarkable efficiency in low-dimensional spaces, typical of motion planning problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Classic $k$-d trees are shown to have logarithmic average case complexity for distance functions *strongly equivalent* to L-p metrics. While this requirement is reasonable for many applications, it does not apply to distances induced by the shortest paths of nonholonomic systems. Therefore, identifying nearest neighbors in the sense of a generic control cost remains an important open problem in sampling-based motion planning. In both literature and practical implementations, when searching for neighbors, randomized planners resort to distance functions that only approximate the true control cost. Arguably, the most common choices are Euclidean distance or quadratic forms. This ad-hoc approach can significantly slow down the convergence rate of sampling-based algorithms if an inappropriate metric is selected.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A number of heuristics have been proposed to resolve this issue, such as the *reachability* and *utility guided RRTs* which bias the tree expansion towards promising regions of the configuration space. Other approaches use the cost of linear quadratic regulators and learning techniques. In specific examples, these heuristics can significantly reduce the negative effects of finding nearest neighbors according to a metric inconsistent with the minimum cost path between configurations. However, the underlying inconsistency is not directly addressed. In contrast, a strong motivation to address it comes from recent research, which shows that a major speedup of sampling-based kynodinamic planners can be achieved by considering nonholonomy at the stage of nearest-neighbor search.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specialized $k$-d tree algorithms have been proposed to account for non-standard topologies of some configuration manifolds.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, no effort is known towards generalizing such algorithms to differential constraints.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we investigate the use of $k$-d trees for *exact* nearest-neighbor search in the presence of differential constraints. The main contributions can be summarized as follows: (i) we derive the expected complexity of nearest-neighbor queries with $k$-d trees built according to classic techniques and reveal that it is super-logarithmic (ii) we propose novel $k$-d tree build and query procedures tailored to sub-Riemannian metrics (iii) we provide numerical trials which verify our theoretical analysis and demonstrate the improvement afforded by the proposed algorithms as compared with popular open source software libraries, such as FLANN and OMPL.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 2, we review background material on sub-Riemannian geometries and show connections with nonholonomic systems, providing asymptotic bounds to their reachable sets. Based on these bounds, in Section 3 we propose a query procedure specialized for nonholonomic systems, after a brief review of the $k$-d tree algorithm. In Section 4, we study the expected complexity of $m$-nearest-neighbor queries on a classic $k$-d tree with sub-Riemannian metrics. Inspired by this analysis, in Section 5 we propose a novel incremental build procedure. Finally, in Section 6 we show positive experimental results for a nonholonomic mobile robot, which confirm our theoretical predictions and the effectiveness of the proposed algorithms.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Geometry of Nonholonomic Systems", "weight": 1.0} -->

Nonholonomic constraints are frequently encountered in robotics and describe mechanical systems whose local mobility is, in some sense, limited. Basic concepts from differential geometry, reviewed below, are used to clarify these limitations and discuss them quantitatively.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Elements of Differential Geometry", "weight": 1.0} -->

A subset $\mathcal{M}$ of ${\mathbb{R}}^{n}$ is a *smooth $k$-dimensional manifold* if for all $p \in \mathcal{M}$ there exists a neighborhood $V$ of $\mathcal{M}$ such that $V \cap \mathcal{M}$ is diffeomorphic to an open subset of ${\mathbb{R}}^{k}$. A vector $v \in^{n}$ is said to be *tangent to $\mathcal{M}$ at point $p \in \mathcal{M}$* if there exists a smooth curve $\gamma:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{M}}$, such that ${\overset{˙}{\gamma}{}} = v$ and ${\gamma{}} = p$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Elements of Differential Geometry", "weight": 1.0} -->

$E_{p}$ is called the *fiber* of bundle $E$ at point $p$. Any set of $h$ linearly independent smooth vector fields $Y_{1},{\ldotsY_{h}}$ such that for all ${p \in \mathcal{M}},$ ${span{({Y_{1}{(p)}},\ldots,{Y_{h}{(p)}})}} = E_{p}$ is called a *basis* of $E$ and $Y_{i}$ are called *generator vector fields* of $E$. The *tangent bundle* of $\mathcal{M}$ is defined as the vector bundle $T\mathcal{M}$ whose fiber at each point $p$ is the tangent space at that point, $T_{p}\mathcal{M}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Elements of Differential Geometry", "weight": 1.0} -->

A *distribution* $\mathcal{H}$ on a manifold is a subbundle of the tangent bundle, i.e., a vector bundle such that its fiber $\mathcal{H}_{p}$ at all points is a vector subspace of $T_{p}\mathcal{M}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Connection with nonholonomic systems", "weight": 1.0} -->

where the configuration $x{(t)}$ and control $u{(t)}$ belong to the *smooth manifolds* $\mathcal{X}$ and $\mathcal{U}$ respectively. Each ${\mathfrak{u}}_{i} \in \mathcal{U}$ defines a *vector field* ${g_{i}{(z)}} = {f{(z,{\mathfrak{u}}_{i})}}$ on $\mathcal{X}$. Therefore, for a fixed configuration $z$, $f{(z,u)}$ has values in a vector space $\mathcal{H}_{z} ≔ {Span{({\{{g_{i}{(z)}}\}})}}$. In other words, the dynamics described by equation define a *distribution* $\mathcal{H}$ on the configuration manifold.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Connection with nonholonomic systems", "weight": 1.0} -->

Throughout the paper, we will make use of the Reeds-Shepp vehicle as an illustrative example.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Distances in a Sub-Riemannian Geometry", "weight": 1.0} -->

A *sub-Riemannian geometry* $\mathcal{G}$ on a manifold $\mathcal{M}$ is a tuple $\mathcal{G} = {(\mathcal{M},\mathcal{H},{\langle \cdot, \cdot \rangle}_{\mathcal{H}})}$, where $\mathcal{H}$ is a distribution on $\mathcal{M}$ whose fibers at all points $p$ are equipped with the inner product ${\langle \cdot, \cdot \rangle}_{\mathcal{H}}:{{\mathcal{H}_{p} \times \mathcal{H}_{p}}\rightarrow}$. The distribution $\mathcal{H}$ is referred to as the *horizontal distribution*.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Distances in a Sub-Riemannian Geometry", "weight": 1.0} -->

In control theory, the *attainable set* $\mathcal{A}{(x_{0},t)}$ is the subset of $\mathcal{X}$ such that for each $p \in {\mathcal{A}{(x_{0},t)}}$ there exists a $u:{{\lbrack 0,\tau\rbrack}\rightarrow\mathcal{U}}$ for which the solution to through ${x{}} = x_{0}$ satisfies ${x{(\tau)}} = p$ for some $\tau \leq t$. Solutions to are simply horizontal curves, so the attainable set $\mathcal{A}{(x_{0},t)}$ is equivalent to the ball $\mathcal{B}{(x_{0},t)}$ defined by the sub-Riemannian metric. This equivalence holds for systems with time-reversal symmetry, under the controllability condition stated in Theorem 2.1.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example (Sub-Riemannian geometry of a Reeds-Shepp vehicle)", "weight": 1.0} -->

The geometry associated with the Reeds-Shepp vehicle is $\mathcal{G}^{RS} = {({SE{}},\mathcal{H}^{RS},{\langle \cdot, \cdot \rangle}_{RS})}$, with the standard inner product ${\langle v,w\rangle}_{RS} = {v^{T}w}$. Horizontal curves for this geometry are feasible paths satisfying the differential constraints. Geodesics correspond to minimum-time paths between two configurations and are known in closed form.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Iterated Lie Brackets and the Ball-box Theorem", "weight": 1.0} -->

A system is said to be *controllable* if any pair of configurations can be connected by a feasible (horizontal) path. Determining controllability of a nonholonomic system is nontrivial. For example, the Reeds-Shepp vehicle cannot move directly in the lateral direction, but intuition suggests that an appropriate sequence of motions can result in a lateral displacement (e.g., in parallel parking). Chow's Theorem and the Ball-box Theorem, reviewed below, are fundamental tools related to the controllability and the reachable sets of nonholonomic systems.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Iterated Lie Brackets and the Ball-box Theorem", "weight": 1.0} -->

From the horizontal distribution $\mathcal{H}$, one can construct a sequence of distributions by iterating the Lie brackets of the generating vector fields, $Y_{1},{Y_{2}\ldotsY_{h}}$, with $h \leq k$. Recursively, this sequence is defined as: $\mathcal{H}^{1} = \mathcal{H}$, $\mathcal{H}^{i + 1} = {\mathcal{H}^{i} \cup {\lbrack\mathcal{H},\mathcal{H}^{i}\rbrack}}$, where $\lbrack\mathcal{H},\mathcal{H}^{i}\rbrack$ denotes the distribution given by the Lie brackets of each generating vector field of $\mathcal{H}$ with those of $\mathcal{H}^{i}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Iterated Lie Brackets and the Ball-box Theorem", "weight": 1.0} -->

Note that the Lie bracket of two vector fields can be linearly independent from the original fields, hence $\mathcal{H}^{i} \subseteq \mathcal{H}^{i + 1}$. The *Lie hull*, denoted $Lie{(H)}$, is the limit of the sequence $\mathcal{H}^{i}$ as $i\rightarrow\infty$. A distribution $\mathcal{H}$ is said to be *bracket-generating* if ${Lie{(\mathcal{H})}} = {T\mathcal{M}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example (Lie hull of a Reeds-Shepp vehicle)", "weight": 1.0} -->

This coincides with the body frame lateral axis $\hat{l}{(x)}$ of the vehicle. Therefore, the second order distribution $\mathcal{H}_{x}^{2} = {Span{\{{\hat{f}{(x)}},{\hat{\theta}{(x)}},{{\lbrack\hat{f},\hat{\theta}\rbrack}{(x)}}\}}}$ spans the tangent bundle of $SE{}$, and thus the Lie hull is obtained in the second step. By Theorem 2.1, there is a feasible motion connecting any two configurations which is consistent with one's intuition about the wheeled robot.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example (Lie hull of a Reeds-Shepp vehicle)", "weight": 1.0} -->

Above, we have shown that from a basis $Y_{1}\ldotsY_{h}$ of a bracket-generating distribution $\mathcal{H}$, one can define a basis $y_{1},{\ldotsy_{k}}$ of $T\mathcal{M}$. Specifically $y_{i} = Y_{i}$ for $i \leq h$, while the remaining $d - h$ fields are obtained with Lie brackets. The vector fields $\{ y_{i}\}$ are called *privileged directions*. Define the *weight* $w_{i}$ of the privileged direction $y_{i}$ as the smallest order of Lie brackets required to generate $y_{i}$ from the original basis. More formally, $w_{i}$ is such that $y_{i} \notin \mathcal{H}^{w_{i} - 1}$ and $y_{i} \in \mathcal{H}^{w_{i}}$ for all $i$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example (Ball-Box Theorem visualized for a Reeds-Shepp vehicle)", "weight": 1.0} -->

From the Lie hull construction in the previous example, we know that ${{\hat{f}{(x)}},{\hat{\theta}{(x)}}} \in \mathcal{H}^{1}$ so the corresponding weights are $w_{\hat{f}} = w_{\hat{\theta}} = 1$. Conversely, $\hat{l}{(x)}$ first appears in $\mathcal{H}^{2}$, so its weight is $w_{\hat{l}} = 2$. Theorem 2.2. ‣ 2.3 Iterated Lie Brackets and the Ball-box Theorem ‣ 2 Geometry of Nonholonomic Systems ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints") states the existence of inner and outer bounding boxes for reachable sets as $t\rightarrow 0$ and predicts the infinitesimal order of each side of these boxes, as shown in figure 1. Higher order Lie brackets correspond to sides that approach zero at a faster asymptotic rate.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Example (Ball-Box Theorem visualized for a Reeds-Shepp vehicle)", "weight": 1.0} -->

The longitudinal and angular sides --- along $\hat{f}$ and $\hat{\theta}$ --- scale with $\Theta{(t)}$, while the lateral one --- along $\hat{l}$ --- with $\Theta{(t^{2})}$. Therefore, both boxes become increasingly elongated along $\hat{f}$ and $\hat{\theta}$ and flattened along $\hat{l}$ as $t\rightarrow 0$. Intuitively, this geometric feature of boxes reflects the well known fact that a small lateral displacement of a car requires more time than an equivalent longitudinal one.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Example (Ball-Box Theorem visualized for a Reeds-Shepp vehicle)", "weight": 1.0} -->

For the Reeds-Shepp vehicle, the sides of both boxes can be computed explicitly with geometric considerations on special manoeuvers that maximize or minimize the displacement along each axis. In particular, we get the values ${C_{\hat{f}} = C_{\hat{\theta}} = c_{\hat{\theta}} = 1},{{C_{\hat{l}} = {1/2}},{{c_{\hat{f}} = {\sqrt{3/2} - 1}},{c_{\hat{l}} = {1/8}}}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "The $k$-d tree Data Structure", "weight": 1.0} -->

A $k$-d tree $\mathcal{T}$ is a binary tree organizing a *finite* subset $X \subset \mathcal{M}$, called a *database*, with its elements $x_{i} \in X$ called *data points*. We would like to find the $m$ points in $X$ closest to a given *query point* $q$ on the manifold. Each point $x_{i} \in X$ is put in relation with a normal vector $n_{i} \in^{n}$. Together, the pair $v_{i} = {(x_{i},n_{i})}$ defines a *vertex* of the binary tree. The set of vertices is denoted with $\mathcal{V}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "The $k$-d tree Data Structure", "weight": 1.0} -->

The fundamental property of $k$-d trees is that *left children belong to the negative halfspace defined by their parents and right children to the positive halfspace*. Recursively, a vertex belongs to the parent halfspaces of all its ancestors. As a result, a $k$-d tree defines a *partition* of $\mathcal{M}$ into non-overlapping polyhedra, called *buckets*, that cover the entire manifold. In the sequel, we let $\mathcal{B}_{\mathcal{T}}$ denote the set of buckets for a given $k$-d tree $\mathcal{T}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "The $k$-d tree Data Structure", "weight": 1.0} -->

Buckets are associated with the leaves of $\mathcal{T}$ and with parents of only-child leaves (i.e., leaves without a sibling). For any given point $q \in \mathcal{M}$, we denote with ${\mathfrak{b}}_{q}$ the unique bucket containing $q$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "$m$-nearest-neighbor query algorithm", "weight": 1.0} -->

The computational efficiency afforded by the algorithm comes from the following observation: let $q$ be the query point and suppose that among the distance evaluations computed thus far, the $m$ closest points to $q$ are within a distance $d_{m}$ away. Now consider a vertex $(x,n)$ and suppose the query point $q$ is contained in ${\mathfrak{h}}^{+}{(x,n)}$ and ${\mathcal{B}{(q,d_{m})}} \subset {{\mathfrak{h}}^{+}{(x,n)}}$. The data points represented by the sibling of $(x,n)$ and all of its descendants are contained in ${\mathfrak{h}}^{-}{(r,c)}$ and are therefore at a distance greater than $d_{m}$. Thus, the corresponding subtree can be omitted from the search. The following primitives will be used to define the query procedure presented in Algorithm 1.

<!-- chunk {"id": "body-0033", "role": "body", "section": "$m$-nearest-neighbor query algorithm", "weight": 1.0} -->

Queue. For an $m$-nearest-neighbor query, the algorithm maintains a *Bounded Priority Queue*, $Q$ of size $m$ to collect the results. The queue can be thought of as a sequence $Q = {\lbrack q_{1},q_{2},{\ldotsq_{m}}\rbrack}$, where each element $q_{i}$ is defined as a distance-vertex pair $q_{i}:{(d_{i},v_{i})},d_{i} \in {}_{\geq 0}^{}v_{i} \in \mathcal{V}$. The property $d_{1} \leq d_{2} \leq \cdots \leq d_{m}$ is an invariant of the data structure.

<!-- chunk {"id": "body-0034", "role": "body", "section": "$m$-nearest-neighbor query algorithm", "weight": 1.0} -->

When an element $(d_{new},n_{new})$ is inserted in the queue, if $d_{new} < d_{m}$, then $q_{m}$ is discarded and the indices of the remaining elements are rearranged to maintain the order.

<!-- chunk {"id": "body-0035", "role": "body", "section": "$m$-nearest-neighbor query algorithm", "weight": 1.0} -->

Ball-Hyperplane Intersection. A procedure that determines whether a ball and a hyperplane intersect. Precisely, `ballHyperplane`$(x,R,p,n)$, with $x \in \mathcal{M}$ and $R \geq 0$, returns true if ${{\mathcal{B}{(x,R)}} \cap {{\mathfrak{h}}{(p,n)}}} \neq \varnothing$. Note that it does not need to return false otherwise.

<!-- chunk {"id": "body-0036", "role": "body", "section": "$m$-nearest-neighbor query algorithm", "weight": 1.0} -->

In the classic analysis of $k$-d trees \[4, eq. 14\] the distance is assumed to be a sum of component-wise terms, called *coordinate distance functions*.

<!-- chunk {"id": "body-0037", "role": "body", "section": "$m$-nearest-neighbor query algorithm", "weight": 1.0} -->

When this holds, e.g., for L-p metrics, the ball-hyperplane intersection procedure reduces to the direct comparison of two numbers.

<!-- chunk {"id": "body-0038", "role": "body", "section": "$m$-nearest-neighbor query algorithm", "weight": 1.0} -->

However, this property does not hold for other notions of distance and in general sub-Riemannian balls can have nontrivial shapes. For these cases, the procedure can be implemented by checking that ${{V_{o}{(x,R)}} \cap {{\mathfrak{h}}{(p,n)}}} \neq \varnothing$, where $V_{o}$ is an "outer set" with a convenient geometry, i.e., a set such that ${V_{o}{(x,R)}} \supseteq {\mathcal{B}{(x,R)}}$ for all ${x \in \mathcal{M}},{R > 0}$ and such that intersections with hyperplanes are easy to verify. Clearly, ${{{{vol}{({V_{o}{(x,R)}})}}/{vol}}{({\mathcal{B}{(x,R)}})}} \geq 1$ and it is desirable that this ratio stays as small as possible.

<!-- chunk {"id": "body-0039", "role": "body", "section": "$m$-nearest-neighbor query algorithm", "weight": 1.0} -->

A crucial consequence of Theorem 2.2. ‣ 2.3 Iterated Lie Brackets and the Ball-box Theorem ‣ 2 Geometry of Nonholonomic Systems ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints") is that the choice ${V_{o}{(x,R)}} = {{Box}_{o}^{w}{(x,R)}}$ offers *optimal asymptotical behavior*, since the volume of the outer set scales with the smallest possible order, namely: ${{vol}{({{Box}_{o}^{w}{(x,R)}})}} \in {\Theta{\lbrack{{vol}{({\mathcal{B}{(x,R)}})}}\rbrack}}$. This fact is fundamental to devise efficient query algorithms for nonholonomic systems.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example (Ball-hyperplane intersection for a Reeds-Shepp vehicle)", "weight": 1.0} -->

The reachable sets shown in figure 1 have a nontrivial geometry.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example (Ball-hyperplane intersection for a Reeds-Shepp vehicle)", "weight": 1.0} -->

*Outer Box Bound* (BB). In this case, the procedure checks ${{{Box}_{o}^{w}{(x,R)}} \cap {h{(p,n)}}} \neq \varnothing$. A simple implementation is to test whether all vertices of the box (8 in this case) are on the same halfspace defined by ${\mathfrak{h}}{(p,n)}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example (Ball-hyperplane intersection for a Reeds-Shepp vehicle)", "weight": 1.0} -->

While Euclidean bounds (EB) are a simple choice, the Outer Box Bound (BB) method approximates the sub-Riemannian ball tightly. In fact, as $R\rightarrow 0$, ${{vol}{({\mathcal{C}{(p,R)}})}} \in {\Theta{(R^{3})}}$, while ${{vol}{({{Box}_{o}^{w}{(p,R)}})}} \in {\Theta{(R^{4})}}$ and therefore the volume of the cylinder tends to be infinitely larger than the volume of the outer box. As a result, method (BB) yields an asymptotically unbounded speedup in the algorithm compared to (EB), as confirmed by our experimental results in Section 6. In addition, any other implementation of the procedure will at most provide a constant factor improvement with respect to method (BB).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example (Ball-hyperplane intersection for a Reeds-Shepp vehicle)", "weight": 1.0} -->

5 // caller reached leaf s ← sideOf (q, xi, ni);
// descend to child containing q
// add vertex to the queue
8 if ballHyperplane (q, dk, xi, ni) then // check for intersections
querySubtree (q, child(vi,opposite(s)));
// start recursion from root
Algorithm 1 k-d tree query

<!-- chunk {"id": "body-0044", "role": "body", "section": "$k$-d tree build algorithms", "weight": 1.0} -->

The performance of nearest-neighbor queries is heavily dependant on how the $k$-d tree is constructed. In the sequel, we describe two popular approaches to construct $k$-d trees: *batch* (or static) and *incremental* (or dynamic).

<!-- chunk {"id": "body-0045", "role": "body", "section": "$k$-d tree build algorithms", "weight": 1.0} -->

In the batch algorithm, all data points are processed at once and statistics of the database determine the vertices of the tree at each depth. This algorithm guarantees a balanced tree, but the insertion of new points is not possible without re-building the tree. Conversely, in the incremental version, the tree is updated on the fly as points are inserted, however, the tree balance guarantee is lost.

<!-- chunk {"id": "body-0046", "role": "body", "section": "$k$-d tree build algorithms", "weight": 1.0} -->

Both algorithms find applications in motion planning: the batch version can be used to efficiently build roadmaps for off-line, multiple-query techniques such as PRMs, while the incremental is suitable for anytime algorithms such as RRTs.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Batch $k$-d tree build algorithm", "weight": 1.0} -->

The following primitive procedures will be used to describe the batch construction of $k$-d trees, defined in Algorithm 2. The range of a set $S$ along direction $\hat{d}$ is defined as ${\text{rng~}_{\hat{d}}{(S)}} = {{\sup_{x \in S}{\langle x,\hat{d}\rangle}} - {\inf_{x \in S}{\langle x,\hat{d}\rangle}}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Batch $k$-d tree build algorithm", "weight": 1.0} -->

Median element. Let ${\mathtt{m}\mathtt{e}\mathtt{d}\mathtt{i}\mathtt{a}\mathtt{n}}:2^{X} \times {}_{}^{}D$. Given a subset $D \in 2^{X}$ of the data points and a direction $l$, `median` returns the median element of $D$ along direction $l$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Batch $k$-d tree build algorithm", "weight": 1.0} -->

5 // caller reached leaf nn e w ← maxRange (D); xn e w ← median (D, nn e w);
Algorithm 2 Batch k-d tree build

<!-- chunk {"id": "body-0050", "role": "body", "section": "Incremental $k$-d tree build algorithm", "weight": 1.0} -->

A key operation to build a $k$-d tree incrementally is to pick splitting hyperplanes on the fly as new data points are inserted.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Incremental $k$-d tree build algorithm", "weight": 1.0} -->

Splitting sequence. A map $\mathcal{Z}_{\mathcal{M}}:{\mathbb{N}}_{\geq 0} \times \mathcal{M}\rightarrow^{n}$ that, given an integer $d \geq 0$ and a point $p \in \mathcal{M}$, returns a normal vector $n$ associated with them.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Incremental $k$-d tree build algorithm", "weight": 1.0} -->

When dealing with $k$-dimensional data, one usually chooses a basis of *cardinal axes* ${\{{\hat{e}}_{i}\}}_{i \in {\lbrack{{0\ldotsk} - 1}\rbrack}}$. The normal of the hyperplane associated with a vertex $v$ is typically picked by cycling through the cardinal axes based on the depth of $v$ in the binary tree. Let "$a\operatorname{mod}b$" denote the remainder of the division of integer $a$ by integer $b$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Incremental $k$-d tree build algorithm", "weight": 1.0} -->

4 if 𝒱 = ⌀ then // if tree is empty...
6 side ← sideOf (xn e w, xi, ni); c ← child (vi, side);
Algorithm 3 Incremental k-d tree build.
Insert in k-d tree 𝒯 = (𝒱,ℰ+,ℰ−), start recursion with insert(xn e w, root(𝒯)).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Complexity Analysis", "weight": 1.0} -->

In this section, we discuss the expected asymptotic complexity of $m$-nearest-neighbor queries in a $k$-d tree built according to Algorithm 2. The complexity of the nearest-neighbor query procedure (Algorithm 1) is measured in terms of the number $n_{v}$ of vertices examined. Let $\mathcal{B}{(q,d_{m})}$ be the ball containing the $m$ nearest neighbors to $q$. For the soundness of the algorithm, all the vertices contained in this ball must be examined, and therefore, all the buckets overlapping with it. As we recall from Section 3, buckets are associated with leaves, and therefore the algorithm will visit as many leaves as the number of such buckets, formally: $n_{l} \in {\Theta{({|\beta|})}}$, where $\beta ≔ \left.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Complexity Analysis", "weight": 1.0} -->

If the asymptotic order of visited leaves is known, proofs rely on the following fact: since the batch algorithm guarantees a balanced tree, descending into $n_{l}$ leaves from the root requires visiting $n_{v} \in {\Theta{({n_{l}{\log N}})}}$ vertices, where $N$ is the cardinality of the database $X$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Complexity Analysis", "weight": 1.0} -->

Lemma 1. ‣ 4 Complexity Analysis ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints") reviews the seminal result, originally, that the expected asymptotic complexity for a Minkowski (i.e., L-p) distance is logarithmic. Our main theoretical contribution is the negative result described in Theorem 4.1, where we reveal that the expected complexity for sub-Riemannian metrics is in fact super-logarithmic. In the sequel, assume that data points are randomly sampled from $\mathcal{M}$ with probability distribution $p{(x)}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark", "weight": 1.0} -->

For holonomic systems, the query complexity is logarithmic, in accordance with Lemma 1. ‣ 4 Complexity Analysis ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints"). In fact, for holonomic systems, $w_{1} = w_{2} = \cdots = w_{k} = 1$, then $W = k$ and $p = 0$ from equation.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark", "weight": 1.0} -->

The query complexity is always between logarithmic and linear. Since $W \geq k$ by definition, for all $i$ such that $w_{i} \leq {W/k}$, one can state $0 < {w_{i}/W} \leq {1/k} \leq 1$. It follows that $0 \leq {\frac{1}{k} - \frac{w_{i}}{W}} < \frac{1}{k}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "The Lie splitting strategy", "weight": 1.0} -->

The basic working principle of $k$-d trees is the ability to discard subtrees without loss of information during a query. For each visited node $v = {(x,n)}$, the algorithm checks whether the current biggest ball in the queue, $\mathcal{B}{(q,d_{m})}$ intersects ${\mathfrak{h}}{(x,n)}$. If such an intersection exists, the algorithm visits both children of $v$, otherwise one child is discarded and so is the entire subtree rooted in it. To reduce complexity, it is thus desirable that during query, a $k$-d tree presents as few ball-hyperplane intersections as possible.

<!-- chunk {"id": "body-0060", "role": "body", "section": "The Lie splitting strategy", "weight": 1.0} -->

(b) Lie k-d tree splitting strategy

<!-- chunk {"id": "body-0061", "role": "body", "section": "The Lie splitting strategy", "weight": 1.0} -->

In the classic splitting strategy, hyperplanes are chosen cycling through a globally defined set of cardinal axes. However, we have shown that nonholonomic systems have a set of locally-defined *privileged axes* and that the reachable sets have different infinitesimal orders along each of them. When the metric comes from a nonholonomic system, the hyperplanes in a classic $k$-d tree are not aligned with reachable sets and the buckets have different asymptotic properties than reachable sets. This can make intersections frequent, as shown in figure 2(a) ‣ Figure 2 ‣ 5 The Lie splitting strategy ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints").

<!-- chunk {"id": "body-0062", "role": "body", "section": "The Lie splitting strategy", "weight": 1.0} -->

Ideally, to minimize the number of ball-hyperplane intersections, the buckets in a $k$-d tree should *approximate the bounding boxes for the reachable sets* of the dynamical system, as depicted in figure 2(b) ‣ Figure 2 ‣ 5 The Lie splitting strategy ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints"). To achieve this, we propose a novel splitting rule, named the *Lie splitting strategy*, which exploits the differential geometric properties of a system and the asymptotic scaling of its reachable sets.

<!-- chunk {"id": "body-0063", "role": "body", "section": "The Lie splitting strategy", "weight": 1.0} -->

The buckets of the $k$-d tree, in expectation, scale asymptotically according to the weighted box along all privileged axes as $t\rightarrow 0$. Formally, for all $q \in \mathcal{M}$ and for all pairs of privileged axes ${y_{i}{(q)}},{y_{j}{(q)}}$,

<!-- chunk {"id": "body-0064", "role": "body", "section": "The Lie splitting strategy", "weight": 1.0} -->

Simply put, each privileged direction should be picked as a splitting normal with a frequency proportional to its weight. Note that this is only relevant *asymptotically*, i.e., as $d\rightarrow\infty$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Example", "weight": 1.0} -->

It is easy to verify that this satisfies equation. In fact, lateral splits occur in the sequence twice as often as longitudinal and lateral splits.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Experimental results", "weight": 1.0} -->

In this section, we validate our results and compare the performance of our algorithms with different methods from widely used open-source libraries. Query performances are averaged over 1000 randomly drawn query points. The same insertion and query sequences are used across all the analyzed algorithms and generated from a uniform distribution.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Experiment 1", "weight": 1.0} -->

In this experiment, we confirm the theoretical contributions presented in Section 4. In figure 3(a) ‣ Figure 3 ‣ Experiment 1. ‣ 6 Experimental results ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints") we show the average number of leaves visited when querying a batch $k$-d tree with Euclidean (blue) and Reeds-Shepp metrics (solid red). While the blue curve settles to a constant value, in accordance with Lemma 1. ‣ 4 Complexity Analysis ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints"), the red curve exhibits exponential growth. When normalizing this curve by $\sqrt{N}$ (dashed red), we observe a constant asymptotic behavior, consistent with the rate determined by Theorem 4.1. For comparison, we report the average time for Euclidean queries on an incremental $k$-d tree (black), which tends to visit more vertices than its batch, balanced counterpart (blue).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Experiment 2", "weight": 1.0} -->

In this experiment (figures figs. 3(b), 3(c) ‣ Figure 3 ‣ Experiment 1. ‣ 6 Experimental results ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints") and 3(d) ‣ Figure 3 ‣ Experiment 1. ‣ 6 Experimental results ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints")), we plot the total number of distance evaluations and the running times observed with different combinations of build and query algorithms. Figure 3(d) ‣ Figure 3 ‣ Experiment 1. ‣ 6 Experimental results ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints") reveals that the proposed outer Box Bound (BB) ball-hyperplane intersection method (yellow, purple, green) reduces the query time significantly as compared to Euclidean bounds (EB) (blue, red), in accordance with our predictions in Section 3.1.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Experiment 2", "weight": 1.0} -->

Additionally, Lie splitting (green) further improves query time, as compared with the classic splitting (yellow). The corresponding incremental Lie $k$-d tree also outperforms a classic batch-built one (purple), guaranteed to be balanced.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Experiment 2", "weight": 1.0} -->

More important speedups emerge when comparing the proposed $k$-d trees with different techniques, such as Hierarchical Clustering from FLANN and Geometric Near-neighbor Access Tree (GNAT) from OMPL. Interestingly, off-the-shelf implementations of $k$-d trees offered by FLANN and other tools are unusable with nonholonomic metrics altogether, since they are limited to distances of the form of equation. Therefore a comparison is not possible.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Experiment 2", "weight": 1.0} -->

All the tested $k$-d trees visibly outperform Hierarchical Clustering (cyan) both in build time and query time. In contrast, GNAT offers competitive query times. However, its insertion is $\sim 100 \times$ slower than incremental k-d trees, since a significant number of distances are evaluated in the build phase, while $k$-d trees only evaluate distances during query. This is reflected in a noticeably higher asymptotic rate of distance evaluations, revealed in figure 3(b) ‣ Figure 3 ‣ Experiment 1. ‣ 6 Experimental results ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints").

<!-- chunk {"id": "body-0072", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Motivated by applications in sampling-based motion planning, we investigated $k$-d trees for efficient nearest-neighbor search with distances defined by the length of paths of controllable nonholonomic systems. We have shown that for sub-Riemannian metrics, the query complexity of a classic batch-built $k$-d tree is $\Theta{({N^{p}{\log N}})}$, where $p \in {\lbrack 0,1)}$ depends on the properties of the system. In addition, we have proposed improved build and query algorithms for $k$-d trees that account for differential constraints. The proposed methods proved superior over classic ones in numerical experiments carried out with a Reeds-Shepp vehicle.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Future work will analyze whether logarithmic complexity is achieved for nonholonomic systems. In addition, the proposed algorithms are exact and rely on explicit distance evaluations. Since distances cannot be generally computed in closed form, we are interested in investigating approximate nearest-neighbor search algorithms with provable correctness bounds that do not require explicit distance computations.
