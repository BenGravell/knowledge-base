## Introduction

Sampling-Based algorithms such as Probabilistic Roadmaps (PRM), Rapidly exploring Random Trees (RRT) and their asymptotically optimal variants (PRM^∗^, RRT^∗^) are widely used in motion planning. These algorithms build a random graph of motions between points on the robot's configuration manifold.

During the graph expansion, nearest-neighbor search is used to limit the computation to regions of the graph close to the new configurations and it is shown to dominate the asymptotic complexity of randomized planners. The notion of closeness appropriate for motion planning is induced by the length of the shortest paths between configurations, or in general, by the minimum cost of controlling a system between states.

As compared to exhaustive linear search, efficient algorithms with reduced complexity have been studied in computational geometry and their use in motion planning has been highlighted as a factor of dramatic performance improvement. Among a variety of approaches, $k$-d trees are ideal due to their remarkable efficiency in low-dimensional spaces, typical of motion planning problems.

Classic $k$-d trees are shown to have logarithmic average case complexity for distance functions *strongly equivalent* to L-p metrics. While this requirement is reasonable for many applications, it does not apply to distances induced by the shortest paths of nonholonomic systems. Therefore, identifying nearest neighbors in the sense of a generic control cost remains an important open problem in sampling-based motion planning. In both literature and practical implementations, when searching for neighbors, randomized planners resort to distance functions that only approximate the true control cost. Arguably, the most common choices are Euclidean distance or quadratic forms. This ad-hoc approach can significantly slow down the convergence rate of sampling-based algorithms if an inappropriate metric is selected.

A number of heuristics have been proposed to resolve this issue, such as the *reachability* and *utility guided RRTs* which bias the tree expansion towards promising regions of the configuration space. Other approaches use the cost of linear quadratic regulators and learning techniques. In specific examples, these heuristics can significantly reduce the negative effects of finding nearest neighbors according to a metric inconsistent with the minimum cost path between configurations. However, the underlying inconsistency is not directly addressed. In contrast, a strong motivation to address it comes from recent research, which shows that a major speedup of sampling-based kynodinamic planners can be achieved by considering nonholonomy at the stage of nearest-neighbor search.

Specialized $k$-d tree algorithms have been proposed to account for non-standard topologies of some configuration manifolds.

However, no effort is known towards generalizing such algorithms to differential constraints.

In this work, we investigate the use of $k$-d trees for *exact* nearest-neighbor search in the presence of differential constraints. The main contributions can be summarized as follows: (i) we derive the expected complexity of nearest-neighbor queries with $k$-d trees built according to classic techniques and reveal that it is super-logarithmic (ii) we propose novel $k$-d tree build and query procedures tailored to sub-Riemannian metrics (iii) we provide numerical trials which verify our theoretical analysis and demonstrate the improvement afforded by the proposed algorithms as compared with popular open source software libraries, such as FLANN and OMPL.

In Section 2, we review background material on sub-Riemannian geometries and show connections with nonholonomic systems, providing asymptotic bounds to their reachable sets. Based on these bounds, in Section 3 we propose a query procedure specialized for nonholonomic systems, after a brief review of the $k$-d tree algorithm. In Section 4, we study the expected complexity of $m$-nearest-neighbor queries on a classic $k$-d tree with sub-Riemannian metrics. Inspired by this analysis, in Section 5 we propose a novel incremental build procedure. Finally, in Section 6 we show positive experimental results for a nonholonomic mobile robot, which confirm our theoretical predictions and the effectiveness of the proposed algorithms.

## Geometry of Nonholonomic Systems

Nonholonomic constraints are frequently encountered in robotics and describe mechanical systems whose local mobility is, in some sense, limited. Basic concepts from differential geometry, reviewed below, are used to clarify these limitations and discuss them quantitatively.

### Elements of Differential Geometry

A subset $\mathcal{M}$ of ${\mathbb{R}}^{n}$ is a *smooth $k$-dimensional manifold* if for all $p \in \mathcal{M}$ there exists a neighborhood $V$ of $\mathcal{M}$ such that $V \cap \mathcal{M}$ is diffeomorphic to an open subset of ${\mathbb{R}}^{k}$. A vector $v \in^{n}$ is said to be *tangent to $\mathcal{M}$ at point $p \in \mathcal{M}$* if there exists a smooth curve $\gamma:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{M}}$, such that ${\overset{˙}{\gamma}{}} = v$ and ${\gamma{}} = p$. The *tangent space* of $\mathcal{M}$ at $p$, denoted $T_{p}\mathcal{M}$, is the subspace of vectors tangent to $\mathcal{M}$ at $p$. A map $Y:{\mathcal{M}\rightarrow{\mathbb{R}}^{n}}$ is a *vector field* on $\mathcal{M}$ if for each $p \in \mathcal{M}$, ${Y{(p)}} \in {T_{p}\mathcal{M}}$. A smooth euclidean *vector bundle* of rank $r$ over $\mathcal{M}$ is defined as a set $E \subset \mathcal{M} \times^{l}$ such that the set $E_{p}:\left\{ v \in {}_{}^{}{(p,v)} \in E \right\}$ is an $r$-dimensional vector space for all $p \in \mathcal{M}$. $E_{p}$ is called the *fiber* of bundle $E$ at point $p$. Any set of $h$ linearly independent smooth vector fields $Y_{1},{\ldotsY_{h}}$ such that for all ${p \in \mathcal{M}},$ ${span{({Y_{1}{(p)}},\ldots,{Y_{h}{(p)}})}} = E_{p}$ is called a *basis* of $E$ and $Y_{i}$ are called *generator vector fields* of $E$. The *tangent bundle* of $\mathcal{M}$ is defined as the vector bundle $T\mathcal{M}$ whose fiber at each point $p$ is the tangent space at that point, $T_{p}\mathcal{M}$. A *distribution* $\mathcal{H}$ on a manifold is a subbundle of the tangent bundle, i.e., a vector bundle such that its fiber $\mathcal{H}_{p}$ at all points is a vector subspace of $T_{p}\mathcal{M}$.

### Connection with nonholonomic systems

Consider a nonholonomic system described by the differential constraint:

where the configuration $x{(t)}$ and control $u{(t)}$ belong to the *smooth manifolds* $\mathcal{X}$ and $\mathcal{U}$ respectively. Each ${\mathfrak{u}}_{i} \in \mathcal{U}$ defines a *vector field* ${g_{i}{(z)}} = {f{(z,{\mathfrak{u}}_{i})}}$ on $\mathcal{X}$. Therefore, for a fixed configuration $z$, $f{(z,u)}$ has values in a vector space $\mathcal{H}_{z} ≔ {Span{({\{{g_{i}{(z)}}\}})}}$. In other words, the dynamics described by equation define a *distribution* $\mathcal{H}$ on the configuration manifold.

Throughout the paper, we will make use of the Reeds-Shepp vehicle as an illustrative example.

### Example (Configuration manifold of a Reeds-Shepp vehicle)

The configuration manifold for this vehicle model is $\mathcal{X} = {SE{}}$ with coordinates $x = {(x_{1},x_{2},x_{3})}$. The mobility of the system is given by ${{{\overset{˙}{x}}_{1} = {u_{1}{\cos{(x_{3})}}}},{{{\overset{˙}{x}}_{2} = {u_{1}{\sin{(x_{3})}}}},{{\overset{˙}{x}}_{3} = {u_{1}u_{2}}}}},$ where ${u_{1},u_{2}} \in {\lbrack{- 1},1\rbrack}$. The inputs ${\mathfrak{u}}_{1} = {}$ and ${\mathfrak{u}}_{2} = {}$ define the vector fields ${g_{1}{(x)}} = {({\cos{(x_{3})}},{\sin{(x_{3})}},0)}$ and ${g_{2}{(x)}} = {({\cos{(x_{3})}},{\sin{(x_{3})}},1)}$. At each $z \in {SE{}}$ the fiber of the Reeds-Shepp distribution $\mathcal{H}^{RS}$ is $Span{\{ g_{1}{(z)},}$ $g_{2}{(z)}\}$. Let ${\hat{f}{(x)}} = {({\cos{(x_{3})}},{\sin{(x_{3})}},0)}$, ${\hat{l}{(x)}} = {({- {\sin{(x_{3})}}},{\cos{(x_{3})}},0)}$ and ${\hat{\theta}{(x)}} = {}$. These vector fields indicate the body frame of the vehicle, i.e., its *front* $\hat{f}$, *lateral* $\hat{l}$ and *rotation* $\hat{\theta}$ axes. The Reeds-Shepp distribution is then equivalently defined by the fibers $\mathcal{H}_{z}^{RS} = {Span{\{{\hat{f}{(z)}},{\hat{\theta}{(z)}}\}}}$.

### Distances in a Sub-Riemannian Geometry

A *sub-Riemannian geometry* $\mathcal{G}$ on a manifold $\mathcal{M}$ is a tuple $\mathcal{G} = {(\mathcal{M},\mathcal{H},{\langle \cdot, \cdot \rangle}_{\mathcal{H}})}$, where $\mathcal{H}$ is a distribution on $\mathcal{M}$ whose fibers at all points $p$ are equipped with the inner product ${\langle \cdot, \cdot \rangle}_{\mathcal{H}}:{{\mathcal{H}_{p} \times \mathcal{H}_{p}}\rightarrow}$. The distribution $\mathcal{H}$ is referred to as the *horizontal distribution*. A smooth curve $\gamma:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{M}}$ is said to be *horizontal* if ${\overset{˙}{\gamma}{(t)}} \in \mathcal{H}_{\gamma{(t)}}$ for all $t \in {\lbrack 0,1\rbrack}$.

The length of smooth curves is defined ${\ell_{\mathcal{G}}{(\gamma)}}:={\int_{0}^{1}{\sqrt{{\langle{\overset{˙}{\gamma}{(t)}},{\overset{˙}{\gamma}{(t)}}\rangle}_{\mathcal{H}}}{dt}}}$. If $\Gamma_{a}^{b}$ denotes the set of horizontal curves between ${a,b} \in \mathcal{M}$, then ${d_{\mathcal{G}}{(a,b)}} ≔ {\inf_{\gamma \in \Gamma_{a}^{b}}{\ell_{\mathcal{G}}{(\gamma)}}}$ is a *sub-Riemannian metric* defined by the geometry. The ball centered at $p$ of radius $r$ with respect to the metric $d_{\mathcal{G}}$ is denoted $\mathcal{B}{(p,r)}$.

In control theory, the *attainable set* $\mathcal{A}{(x_{0},t)}$ is the subset of $\mathcal{X}$ such that for each $p \in {\mathcal{A}{(x_{0},t)}}$ there exists a $u:{{\lbrack 0,\tau\rbrack}\rightarrow\mathcal{U}}$ for which the solution to through ${x{}} = x_{0}$ satisfies ${x{(\tau)}} = p$ for some $\tau \leq t$. Solutions to are simply horizontal curves, so the attainable set $\mathcal{A}{(x_{0},t)}$ is equivalent to the ball $\mathcal{B}{(x_{0},t)}$ defined by the sub-Riemannian metric. This equivalence holds for systems with time-reversal symmetry, under the controllability condition stated in Theorem 2.1.

### Example (Sub-Riemannian geometry of a Reeds-Shepp vehicle)

The geometry associated with the Reeds-Shepp vehicle is $\mathcal{G}^{RS} = {({SE{}},\mathcal{H}^{RS},{\langle \cdot, \cdot \rangle}_{RS})}$, with the standard inner product ${\langle v,w\rangle}_{RS} = {v^{T}w}$. Horizontal curves for this geometry are feasible paths satisfying the differential constraints. Geodesics correspond to minimum-time paths between two configurations and are known in closed form.

### Iterated Lie Brackets and the Ball-box Theorem

A system is said to be *controllable* if any pair of configurations can be connected by a feasible (horizontal) path. Determining controllability of a nonholonomic system is nontrivial. For example, the Reeds-Shepp vehicle cannot move directly in the lateral direction, but intuition suggests that an appropriate sequence of motions can result in a lateral displacement (e.g., in parallel parking). Chow's Theorem and the Ball-box Theorem, reviewed below, are fundamental tools related to the controllability and the reachable sets of nonholonomic systems.

The *Lie derivative* of a vector field $Y$ at $p \in \mathcal{M}$ in the direction $v \in {T_{p}\mathcal{M}}$ is defined as ${dY{(p)}v} = \left. {\frac{d}{dt}Y{({\gamma{(t)}})}} \right|_{t = 0}$, where $\gamma$ is a smooth curve starting in $p = {\gamma{}}$ with velocity $v = {\overset{˙}{\gamma}{}}$. Given two vector fields $Y_{1},Y_{2}$ on $\mathcal{M}$, the *Lie bracket* $\lbrack Y_{1},Y_{2}\rbrack$ is a vector field on $\mathcal{M}$ defined as ${{\lbrack Y_{1},Y_{2}\rbrack}{(p)}} = {{dY_{2}{(p)}Y_{1}{(p)}} - {dY_{1}{(p)}Y_{2}{(p)}}}$.

From the horizontal distribution $\mathcal{H}$, one can construct a sequence of distributions by iterating the Lie brackets of the generating vector fields, $Y_{1},{Y_{2}\ldotsY_{h}}$, with $h \leq k$. Recursively, this sequence is defined as: $\mathcal{H}^{1} = \mathcal{H}$, $\mathcal{H}^{i + 1} = {\mathcal{H}^{i} \cup {\lbrack\mathcal{H},\mathcal{H}^{i}\rbrack}}$, where $\lbrack\mathcal{H},\mathcal{H}^{i}\rbrack$ denotes the distribution given by the Lie brackets of each generating vector field of $\mathcal{H}$ with those of $\mathcal{H}^{i}$. Note that the Lie bracket of two vector fields can be linearly independent from the original fields, hence $\mathcal{H}^{i} \subseteq \mathcal{H}^{i + 1}$. The *Lie hull*, denoted $Lie{(H)}$, is the limit of the sequence $\mathcal{H}^{i}$ as $i\rightarrow\infty$. A distribution $\mathcal{H}$ is said to be *bracket-generating* if ${Lie{(\mathcal{H})}} = {T\mathcal{M}}$.

### Theorem 2.1

(Chow's Theorem \[13, p. 44\] ). If ${Lie{(\mathcal{H})}} = {T\mathcal{M}}$ on a connected manifold $\mathcal{M}$, then any ${a,b} \in \mathcal{M}$ can be joined by a horizontal curve.

### Example (Lie hull of a Reeds-Shepp vehicle)

Consider the Lie hull of $\mathcal{H}^{RS}$ generated by $\{{\hat{f}{(x)}},{\hat{\theta}{(x)}}\}$. For every $x \in {SE{}}$, these vectors span a two-dimensional subspace of $T_{x}{({SE{}})}$. The first order Lie bracket is given by

This coincides with the body frame lateral axis $\hat{l}{(x)}$ of the vehicle. Therefore, the second order distribution $\mathcal{H}_{x}^{2} = {Span{\{{\hat{f}{(x)}},{\hat{\theta}{(x)}},{{\lbrack\hat{f},\hat{\theta}\rbrack}{(x)}}\}}}$ spans the tangent bundle of $SE{}$, and thus the Lie hull is obtained in the second step. By Theorem 2.1, there is a feasible motion connecting any two configurations which is consistent with one's intuition about the wheeled robot.

Above, we have shown that from a basis $Y_{1}\ldotsY_{h}$ of a bracket-generating distribution $\mathcal{H}$, one can define a basis $y_{1},{\ldotsy_{k}}$ of $T\mathcal{M}$. Specifically $y_{i} = Y_{i}$ for $i \leq h$, while the remaining $d - h$ fields are obtained with Lie brackets. The vector fields $\{ y_{i}\}$ are called *privileged directions*. Define the *weight* $w_{i}$ of the privileged direction $y_{i}$ as the smallest order of Lie brackets required to generate $y_{i}$ from the original basis. More formally, $w_{i}$ is such that $y_{i} \notin \mathcal{H}^{w_{i} - 1}$ and $y_{i} \in \mathcal{H}^{w_{i}}$ for all $i$. The *weighted box* at $p$ of size $\epsilon$, weights $w \in {\mathbb{N}}_{> 0}^{k}$ and multipliers $\mu \in_{> 0}^{k}$ is defined as:

### Theorem 2.2 (The ball-box Theorem)

Let $\mathcal{H}$ be a distribution on a manifold $\mathcal{M}$ satisfying the assumptions of Chow's Theorem. Then, there exist constants $\epsilon_{0} \in_{> 0}$ and $c,C \in_{> 0}^{k}$ such that for all $\epsilon < \epsilon_{0}$ and for all $p \in \mathcal{M}$:

where ${Box}_{i}^{w}$ and ${Box}_{o}^{w}$ are referred to as the inner and outer bounding boxes for the sub-Riemannian ball $\mathcal{B}$, respectively.

### Example (Ball-Box Theorem visualized for a Reeds-Shepp vehicle)

From the Lie hull construction in the previous example, we know that ${{\hat{f}{(x)}},{\hat{\theta}{(x)}}} \in \mathcal{H}^{1}$ so the corresponding weights are $w_{\hat{f}} = w_{\hat{\theta}} = 1$. Conversely, $\hat{l}{(x)}$ first appears in $\mathcal{H}^{2}$, so its weight is $w_{\hat{l}} = 2$. Theorem 2.2. ‣ 2.3 Iterated Lie Brackets and the Ball-box Theorem ‣ 2 Geometry of Nonholonomic Systems ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints") states the existence of inner and outer bounding boxes for reachable sets as $t\rightarrow 0$ and predicts the infinitesimal order of each side of these boxes, as shown in figure 1. Higher order Lie brackets correspond to sides that approach zero at a faster asymptotic rate. The longitudinal and angular sides --- along $\hat{f}$ and $\hat{\theta}$ --- scale with $\Theta{(t)}$, while the lateral one --- along $\hat{l}$ --- with $\Theta{(t^{2})}$. Therefore, both boxes become increasingly elongated along $\hat{f}$ and $\hat{\theta}$ and flattened along $\hat{l}$ as $t\rightarrow 0$. Intuitively, this geometric feature of boxes reflects the well known fact that a small lateral displacement of a car requires more time than an equivalent longitudinal one.

Figure 1: Reachable sets and bounding boxes for a Reeds-Shepp vehicle around a configuration q and for different values of t. The lengths of the box sides are highlighted. For both the inner and outer boxes, as t → 0, the sides along the front f̂ and heading θ̂ axes are linear in t, while the side along the lateral axis l̂ is quadratic in t.

For the Reeds-Shepp vehicle, the sides of both boxes can be computed explicitly with geometric considerations on special manoeuvers that maximize or minimize the displacement along each axis. In particular, we get the values ${C_{\hat{f}} = C_{\hat{\theta}} = c_{\hat{\theta}} = 1},{{C_{\hat{l}} = {1/2}},{{c_{\hat{f}} = {\sqrt{3/2} - 1}},{c_{\hat{l}} = {1/8}}}}$.

## The $k$-d tree Data Structure

A $k$-d tree $\mathcal{T}$ is a binary tree organizing a *finite* subset $X \subset \mathcal{M}$, called a *database*, with its elements $x_{i} \in X$ called *data points*. We would like to find the $m$ points in $X$ closest to a given *query point* $q$ on the manifold. Each point $x_{i} \in X$ is put in relation with a normal vector $n_{i} \in^{n}$. Together, the pair $v_{i} = {(x_{i},n_{i})}$ defines a *vertex* of the binary tree. The set of vertices is denoted with $\mathcal{V}$. A vertex defines a partition of ${\mathbb{R}}^{n}$ into two halfspaces, referred to as the *positive* and *negative halfspace*, and respectively described algebraically:

An *edge* is an ordered pair of vertices $e = {(v_{i},v_{j})}$. A binary tree is defined as $\mathcal{T} ≔ {(\mathcal{V},\mathcal{E}^{-},\mathcal{E}^{+})}$, with $\mathcal{V}$ set of vertices, $\mathcal{E}^{-}$ set of left edges and $\mathcal{E}^{+}$ set of right edges. Given one edge $e = {(v_{i},v_{j})}$, vertex $v_{j}$ is referred to as the *left child* of $v_{i}$ if $e \in \mathcal{E}^{-}$, or the *right child* if $e \in \mathcal{E}^{+}$. Let ${{\mathtt{p}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{n}\mathtt{t}}{({v_{i} \in \mathcal{V}})}} = v_{j} \in \mathcal{V}$ s.t. ${(v_{i},v_{j})} \in {\mathcal{E}^{-} \cup \mathcal{E}^{+}}$. By convention, ${{\mathtt{p}\mathtt{a}\mathtt{r}\mathtt{e}\mathtt{n}\mathtt{t}}{(v_{i})}} = \varnothing$ if such $v_{j}$ does not exist and $v_{i}$ is called the *root* of $\mathcal{T}$, denoted $v_{i} = {{\mathtt{r}\mathtt{o}\mathtt{o}\mathtt{t}}{(\mathcal{T})}}$. Let ${{\mathtt{c}\mathtt{h}\mathtt{i}\mathtt{l}\mathtt{d}}{({{v_{i} \in \mathcal{V}},{s \in {\{ -, + \}}}})}} = v_{j} \in \mathcal{V}$ s.t. ${(v_{i},v_{j})} \in \mathcal{E}^{s}$, or otherwise $\varnothing$ if such $v_{j}$ does not exist.

The fundamental property of $k$-d trees is that *left children belong to the negative halfspace defined by their parents and right children to the positive halfspace*. Recursively, a vertex belongs to the parent halfspaces of all its ancestors. As a result, a $k$-d tree defines a *partition* of $\mathcal{M}$ into non-overlapping polyhedra, called *buckets*, that cover the entire manifold. In the sequel, we let $\mathcal{B}_{\mathcal{T}}$ denote the set of buckets for a given $k$-d tree $\mathcal{T}$.

Buckets are associated with the leaves of $\mathcal{T}$ and with parents of only-child leaves (i.e., leaves without a sibling). For any given point $q \in \mathcal{M}$, we denote with ${\mathfrak{b}}_{q}$ the unique bucket containing $q$.

### $m$-nearest-neighbor query algorithm

The computational efficiency afforded by the algorithm comes from the following observation: let $q$ be the query point and suppose that among the distance evaluations computed thus far, the $m$ closest points to $q$ are within a distance $d_{m}$ away. Now consider a vertex $(x,n)$ and suppose the query point $q$ is contained in ${\mathfrak{h}}^{+}{(x,n)}$ and ${\mathcal{B}{(q,d_{m})}} \subset {{\mathfrak{h}}^{+}{(x,n)}}$. The data points represented by the sibling of $(x,n)$ and all of its descendants are contained in ${\mathfrak{h}}^{-}{(r,c)}$ and are therefore at a distance greater than $d_{m}$. Thus, the corresponding subtree can be omitted from the search. The following primitives will be used to define the query procedure presented in Algorithm 1.

Side of hyperplane. A procedure `sideOf`${(x,p,n)}\rightarrow{\{ -, + \}}$, with ${x,p} \in \mathcal{M}$, $n \in^{n}$. Returns + iff $x \in {{\mathfrak{h}}^{+}{(p,n)}}$ and $-$ otherwise. For convenience, define ${{\mathtt{o}\mathtt{p}\mathtt{p}\mathtt{o}\mathtt{s}\mathtt{i}\mathtt{t}\mathtt{e}}{( + )}} = -$ and vice-versa.

Queue. For an $m$-nearest-neighbor query, the algorithm maintains a *Bounded Priority Queue*, $Q$ of size $m$ to collect the results. The queue can be thought of as a sequence $Q = {\lbrack q_{1},q_{2},{\ldotsq_{m}}\rbrack}$, where each element $q_{i}$ is defined as a distance-vertex pair $q_{i}:{(d_{i},v_{i})},d_{i} \in {}_{\geq 0}^{}v_{i} \in \mathcal{V}$. The property $d_{1} \leq d_{2} \leq \cdots \leq d_{m}$ is an invariant of the data structure. When an element $(d_{new},n_{new})$ is inserted in the queue, if $d_{new} < d_{m}$, then $q_{m}$ is discarded and the indices of the remaining elements are rearranged to maintain the order.

Ball-Hyperplane Intersection. A procedure that determines whether a ball and a hyperplane intersect. Precisely, `ballHyperplane`$(x,R,p,n)$, with $x \in \mathcal{M}$ and $R \geq 0$, returns true if ${{\mathcal{B}{(x,R)}} \cap {{\mathfrak{h}}{(p,n)}}} \neq \varnothing$. Note that it does not need to return false otherwise.

In the classic analysis of $k$-d trees \[4, eq. 14\] the distance is assumed to be a sum of component-wise terms, called *coordinate distance functions*. Namely:

When this holds, e.g., for L-p metrics, the ball-hyperplane intersection procedure reduces to the direct comparison of two numbers.

However, this property does not hold for other notions of distance and in general sub-Riemannian balls can have nontrivial shapes. For these cases, the procedure can be implemented by checking that ${{V_{o}{(x,R)}} \cap {{\mathfrak{h}}{(p,n)}}} \neq \varnothing$, where $V_{o}$ is an "outer set" with a convenient geometry, i.e., a set such that ${V_{o}{(x,R)}} \supseteq {\mathcal{B}{(x,R)}}$ for all ${x \in \mathcal{M}},{R > 0}$ and such that intersections with hyperplanes are easy to verify. Clearly, ${{{{vol}{({V_{o}{(x,R)}})}}/{vol}}{({\mathcal{B}{(x,R)}})}} \geq 1$ and it is desirable that this ratio stays as small as possible.

A crucial consequence of Theorem 2.2. ‣ 2.3 Iterated Lie Brackets and the Ball-box Theorem ‣ 2 Geometry of Nonholonomic Systems ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints") is that the choice ${V_{o}{(x,R)}} = {{Box}_{o}^{w}{(x,R)}}$ offers *optimal asymptotical behavior*, since the volume of the outer set scales with the smallest possible order, namely: ${{vol}{({{Box}_{o}^{w}{(x,R)}})}} \in {\Theta{\lbrack{{vol}{({\mathcal{B}{(x,R)}})}}\rbrack}}$. This fact is fundamental to devise efficient query algorithms for nonholonomic systems.

### Example (Ball-hyperplane intersection for a Reeds-Shepp vehicle)

The reachable sets shown in figure 1 have a nontrivial geometry. Let us consider two possible implementations of the ball-hyperplane intersection procedure:

*Euclidean bound* (EB). Define the set ${\mathcal{C}{(p,R)}} = \left. \{{x \in {SE{}}} \middle| {{{{({x_{1} - p_{1}})}^{2} + {({x_{2} - p_{2}})}^{2}} \leq R^{2}},{{|{x_{3} - p_{3}}|} \leq {2R}}}\} \right.$, i.e., a cylinder in the configuration space with axis along $\hat{\theta}$. Since the Euclidean distance $\|{a - b}\|$ is a lower bound to $d_{RS}{(a,b)}$, then ${\mathcal{B}{(x,R)}} \subset {\mathcal{C}{(x,R)}}$ and `ballHyperplane` can be correctly implemented by checking ${{\mathcal{C}{(x,R)}} \cap {h{(p,n)}}} \neq \varnothing$

*Outer Box Bound* (BB). In this case, the procedure checks ${{{Box}_{o}^{w}{(x,R)}} \cap {h{(p,n)}}} \neq \varnothing$. A simple implementation is to test whether all vertices of the box (8 in this case) are on the same halfspace defined by ${\mathfrak{h}}{(p,n)}$.

While Euclidean bounds (EB) are a simple choice, the Outer Box Bound (BB) method approximates the sub-Riemannian ball tightly. In fact, as $R\rightarrow 0$, ${{vol}{({\mathcal{C}{(p,R)}})}} \in {\Theta{(R^{3})}}$, while ${{vol}{({{Box}_{o}^{w}{(p,R)}})}} \in {\Theta{(R^{4})}}$ and therefore the volume of the cylinder tends to be infinitely larger than the volume of the outer box. As a result, method (BB) yields an asymptotically unbounded speedup in the algorithm compared to (EB), as confirmed by our experimental results in Section 6. In addition, any other implementation of the procedure will at most provide a constant factor improvement with respect to method (BB).

5 // caller reached leaf s ← sideOf (q, xi, ni);
// descend to child containing q
// add vertex to the queue
8 if ballHyperplane (q, dk, xi, ni) then // check for intersections
querySubtree (q, child(vi,opposite(s)));
// start recursion from root
Algorithm 1 k-d tree query

### $k$-d tree build algorithms

The performance of nearest-neighbor queries is heavily dependant on how the $k$-d tree is constructed. In the sequel, we describe two popular approaches to construct $k$-d trees: *batch* (or static) and *incremental* (or dynamic).

In the batch algorithm, all data points are processed at once and statistics of the database determine the vertices of the tree at each depth. This algorithm guarantees a balanced tree, but the insertion of new points is not possible without re-building the tree. Conversely, in the incremental version, the tree is updated on the fly as points are inserted, however, the tree balance guarantee is lost.

Both algorithms find applications in motion planning: the batch version can be used to efficiently build roadmaps for off-line, multiple-query techniques such as PRMs, while the incremental is suitable for anytime algorithms such as RRTs.

### Batch $k$-d tree build algorithm

The following primitive procedures will be used to describe the batch construction of $k$-d trees, defined in Algorithm 2. The range of a set $S$ along direction $\hat{d}$ is defined as ${\text{rng~}_{\hat{d}}{(S)}} = {{\sup_{x \in S}{\langle x,\hat{d}\rangle}} - {\inf_{x \in S}{\langle x,\hat{d}\rangle}}}$.

Maximum range. Let ${\mathtt{m}\mathtt{a}\mathtt{x}\mathtt{R}\mathtt{a}\mathtt{n}\mathtt{g}\mathtt{e}}:2^{X}\rightarrow^{n}$. Given a subset $D \in 2^{X}$ of the data points, `maxRange` determines a direction $l$ along which the range of data is maximal. We consider the formulation in, where $l$ is chosen among the cardinal directions ${\{{\hat{e}}_{i}\}}_{i \in {\lbrack 0,{{\ldotsk} - 1}\rbrack}}$, so that ${{\mathtt{m}\mathtt{a}\mathtt{x}\mathtt{R}\mathtt{a}\mathtt{n}\mathtt{g}\mathtt{e}}{(D)}} = {\arg{\max_{{\hat{e}}_{i}}{\lbrack{\text{rng~}_{{\hat{e}}_{i}}{(D)}}\rbrack}}}$.

Median element. Let ${\mathtt{m}\mathtt{e}\mathtt{d}\mathtt{i}\mathtt{a}\mathtt{n}}:2^{X} \times {}_{}^{}D$. Given a subset $D \in 2^{X}$ of the data points and a direction $l$, `median` returns the median element of $D$ along direction $l$.

5 // caller reached leaf nn e w ← maxRange (D); xn e w ← median (D, nn e w);
Algorithm 2 Batch k-d tree build

### Incremental $k$-d tree build algorithm

A key operation to build a $k$-d tree incrementally is to pick splitting hyperplanes on the fly as new data points are inserted. This is achieved with a *splitting sequence*, which we define as:

Splitting sequence. A map $\mathcal{Z}_{\mathcal{M}}:{\mathbb{N}}_{\geq 0} \times \mathcal{M}\rightarrow^{n}$ that, given an integer $d \geq 0$ and a point $p \in \mathcal{M}$, returns a normal vector $n$ associated with them.

When dealing with $k$-dimensional data, one usually chooses a basis of *cardinal axes* ${\{{\hat{e}}_{i}\}}_{i \in {\lbrack{{0\ldotsk} - 1}\rbrack}}$. The normal of the hyperplane associated with a vertex $v$ is typically picked by cycling through the cardinal axes based on the depth of $v$ in the binary tree. Let "$a\operatorname{mod}b$" denote the remainder of the division of integer $a$ by integer $b$. Then, the *classic splitting (CS) sequence* is defined as:

4 if 𝒱 = ⌀ then // if tree is empty...
6 side ← sideOf (xn e w, xi, ni); c ← child (vi, side);
Algorithm 3 Incremental k-d tree build.
Insert in k-d tree 𝒯 = (𝒱,ℰ+,ℰ−), start recursion with insert(xn e w, root(𝒯)).

## Complexity Analysis

In this section, we discuss the expected asymptotic complexity of $m$-nearest-neighbor queries in a $k$-d tree built according to Algorithm 2. The complexity of the nearest-neighbor query procedure (Algorithm 1) is measured in terms of the number $n_{v}$ of vertices examined. Let $\mathcal{B}{(q,d_{m})}$ be the ball containing the $m$ nearest neighbors to $q$. For the soundness of the algorithm, all the vertices contained in this ball must be examined, and therefore, all the buckets overlapping with it. As we recall from Section 3, buckets are associated with leaves, and therefore the algorithm will visit as many leaves as the number of such buckets, formally: $n_{l} \in {\Theta{({|\beta|})}}$, where $\beta ≔ \left. \{{b \in \mathcal{B}_{\mathcal{T}}} \middle| {{b \cap {\mathcal{B}{(q,d_{m})}}} \neq \varnothing}\} \right.$ and $n_{l}$ denotes the number of leaves visited by the algorithm.

If the asymptotic order of visited leaves is known, proofs rely on the following fact: since the batch algorithm guarantees a balanced tree, descending into $n_{l}$ leaves from the root requires visiting $n_{v} \in {\Theta{({n_{l}{\log N}})}}$ vertices, where $N$ is the cardinality of the database $X$. Thus the expected query complexity is given by:

Lemma 1. ‣ 4 Complexity Analysis ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints") reviews the seminal result, originally from, that the expected asymptotic complexity for a Minkowski (i.e., L-p) distance is logarithmic. Our main theoretical contribution is the negative result described in Theorem 4.1, where we reveal that the expected complexity for sub-Riemannian metrics is in fact super-logarithmic. In the sequel, assume that data points are randomly sampled from $\mathcal{M}$ with probability distribution $p{(x)}$.

### Lemma 1 (\[4\])

If the distance function used for the nearest-neighbor query is induced by a $p$-norm, then the expected complexity of the nearest-neighbor search on a $k$-d tree built with Algorithm 2 is $O{({\log{(N)}})}$ as $N\rightarrow\infty$.

For the detailed proof, we suggest reading the original work by Friedman et al., while here we report key facts used in our next result. In \[4, pg. 214\], it is shown that:

with no assumptions on the metric and the probability distribution $p{(x)}$.

In a batch-built $k$-d tree, the expected asymptotic shape of the bucket ${\mathfrak{b}}_{q}$ containing the query point $q$ is assumed hyper-cubical. From equation with $m = 1$, ${{\mathbb{E}}{({{vol}{({\mathfrak{b}}_{q})}})}} \approx {\frac{1}{({N + 1})}\frac{1}{p{(q)}}}$. Thus, hyper-cubes in a neighborhood of $q$ have sides of expected length ${E{(l_{q})}} = {\lbrack{{({N + 1})}p{(q)}}\rbrack}^{- {1/k}}$. Using these facts, it is then shown that the expected number of visited leaves is asymptotically constant with the size of the database, ${E{(n_{l})}} \in {\Theta{}}$ and therefore the average query complexity is logarithmic, as per equation.

### Theorem 4.1

Let the distance function used for the nearest-neighbor query be a sub-Riemannian metric on a smooth connected manifold $\mathcal{M}$ with a bracket-generating horizontal distribution of dimension $h$ and weights $\{ w_{i}\}$. Then the expected complexity of the nearest-neighbor query on a $k$-d tree built with Algorithm 2 is $\Theta{({N^{p}{\log{(N)}}})}$ as $N\rightarrow\infty$, where the expression for $p$ is:

### Proof

For $N$ large enough, Theorem 2.2. ‣ 2.3 Iterated Lie Brackets and the Ball-box Theorem ‣ 2 Geometry of Nonholonomic Systems ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints") ensures the existence of inner and outer bounding boxes to the sub-Riemannian ball $\mathcal{B}{(q,d_{m})}$.

From equations (4. ‣ 2.3 Iterated Lie Brackets and the Ball-box Theorem ‣ 2 Geometry of Nonholonomic Systems ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints")) and, we get:

where $W ≔ {\sum_{i}w_{i}}$. Therefore, the expected distance to the $m$-th nearest neighbor scales asymptotically as ${{\mathbb{E}}{(d_{m})}} \in {\Theta{(N^{- {1/W}})}}$ for $N\rightarrow\infty$. Recall that a bucket ${\mathfrak{b}}_{q}$ has sides of expected length $l_{q} = \sqrt[k]{1/\left\lbrack {{({N + 1})}p{(q)}} \right\rbrack}$ or equivalently, $l_{q} \in {\Theta{(N^{- {1/k}})}}$. We are now interested in the asymptotic order of the number of buckets overlapping with a weighted box of size $d_{m}$. Let $n_{h}{(d,l_{q})}$ the number of hypercubes intersected by a segment of length $d$ embedded in a grid of ${\mathbb{R}}^{k}$ with side $l_{q}$. It can be shown that $\left\lceil {{(\sqrt{k})}^{- 1}{({d/l_{q}})}} \right\rceil \leq {n_{h}{(d,l_{q})}} \leq {k + {\sqrt{k}{\lceil{d/l_{q}}\rceil}}}$. Then, asymptotically, ${n_{h}{(d,l_{q})}} \in {\Theta{({\lceil{d/l_{q}}\rceil})}}$ as ${(d,l_{q})}\rightarrow 0$. Since a box has $k$ orthogonal sides, each with expected length ${\mathbb{E}}{(d_{m})}^{w_{i}}$, the expected number of visited buckets, is:

In the latter product, only the factors with exponent $> 0$ contribute to the complexity of the algorithm, while the other terms tend to $1$, as $N\rightarrow\infty$. In other words, the query complexity is determined only by low order Lie brackets up until $w_{i} \leq {W/k}$. In fact, along the direction of higher order Lie brackets, reachable sets shrink to zero faster than the side of a $k$-d tree bucket. Following up from equation, we get:

From equation it follows that the expected complexity of the query algorithm is given by ${{\mathbb{E}}{(n_{v})}} \in {\Theta{({N^{p}{\log N}})}}$ as $N\rightarrow\infty$.

### Remark

For holonomic systems, the query complexity is logarithmic, in accordance with Lemma 1. ‣ 4 Complexity Analysis ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints"). In fact, for holonomic systems, $w_{1} = w_{2} = \cdots = w_{k} = 1$, then $W = k$ and $p = 0$ from equation.

### Remark

The query complexity is always between logarithmic and linear. Since $W \geq k$ by definition, for all $i$ such that $w_{i} \leq {W/k}$, one can state $0 < {w_{i}/W} \leq {1/k} \leq 1$. It follows that $0 \leq {\frac{1}{k} - \frac{w_{i}}{W}} < \frac{1}{k}$. Then $p$ can be bounded with:

### Example

For the Reeds-Shepp car, $k = {\dim{\lbrack{SE{}}\rbrack}} = 3$, $w_{\hat{f}} = w_{\hat{\theta}} = 1$, $w_{\hat{l}} = 2$ and ${W = {w_{\hat{f}} + w_{\hat{\theta}} + w_{\hat{l}}} = 4}.$ Only $w_{\hat{f}}$ and $w_{\hat{\theta}}$ satisfy $w_{i} \leq {W/k}$, therefore, according to Theorem 4.1, the expected query complexity of a batch kd-tree is $\Theta\left( {\sqrt{N}{\log N}} \right)$. We confirm this prediction with experiments in section 6.

## The Lie splitting strategy

The basic working principle of $k$-d trees is the ability to discard subtrees without loss of information during a query. For each visited node $v = {(x,n)}$, the algorithm checks whether the current biggest ball in the queue, $\mathcal{B}{(q,d_{m})}$ intersects ${\mathfrak{h}}{(x,n)}$. If such an intersection exists, the algorithm visits both children of $v$, otherwise one child is discarded and so is the entire subtree rooted in it. To reduce complexity, it is thus desirable that during query, a $k$-d tree presents as few ball-hyperplane intersections as possible.

(a) Classic k-d tree construction

(b) Lie k-d tree splitting strategy

Figure 2: Qualitative comparison of a classic k-d tree with its counterpart built with the proposed Lie splitting strategy. For nonholonomic systems, reachable sets (red, blue, green) are elongated along configuration-dependent privileged directions. The smaller the sets, the more pronounced their aspect ratios. The Lie splitting strategy adapts the hyperplanes locally to the balls and decreases the expected number of ball-hyperplane intersections, thus reducing the expected asymptotic query complexity.

In the classic splitting strategy, hyperplanes are chosen cycling through a globally defined set of cardinal axes. However, we have shown that nonholonomic systems have a set of locally-defined *privileged axes* and that the reachable sets have different infinitesimal orders along each of them. When the metric comes from a nonholonomic system, the hyperplanes in a classic $k$-d tree are not aligned with reachable sets and the buckets have different asymptotic properties than reachable sets. This can make intersections frequent, as shown in figure 2(a) ‣ Figure 2 ‣ 5 The Lie splitting strategy ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints").

Ideally, to minimize the number of ball-hyperplane intersections, the buckets in a $k$-d tree should *approximate the bounding boxes for the reachable sets* of the dynamical system, as depicted in figure 2(b) ‣ Figure 2 ‣ 5 The Lie splitting strategy ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints"). To achieve this, we propose a novel splitting rule, named the *Lie splitting strategy*, which exploits the differential geometric properties of a system and the asymptotic scaling of its reachable sets. The Lie splitting strategy is based on the following two principles:

The splitting normal associated with each data point $x_{i}$ is along one of the privileged axes in that point, i.e., ${\mathcal{Z}_{\mathcal{M}}{(d,x_{i})}} \in {\{{y_{1}{(x_{i})}},{y_{2}{(x_{i})}\ldotsy_{k}{(x_{i})}}\}}$.

The buckets of the $k$-d tree, in expectation, scale asymptotically according to the weighted box along all privileged axes as $t\rightarrow 0$. Formally, for all $q \in \mathcal{M}$ and for all pairs of privileged axes ${y_{i}{(q)}},{y_{j}{(q)}}$,

Requirement 2 prescribes the asymptotic behavior of the sequence $\mathcal{Z}_{\mathcal{M}}$ as $d\rightarrow\infty$, which can be formalized as follows: let ${n_{i}{(d)}} = \left| {\{{n < d}:{{\mathcal{Z}_{\mathcal{M}}{(n,x)}} = {y_{i}{(x)}}}\}} \right|$, i.e., the total number of splits in the sequence $\mathcal{Z}_{\mathcal{M}}$ along axis $y_{i}$ before index $d$.

As $d\rightarrow\infty$, the expected bucket size along $y_{i}$ after $n_{i}{(d)}$ splits has asymptotic order ${{\mathbb{E}}\left\lbrack {\text{rng~}_{y_{i}{(q)}}{({\mathfrak{b}}_{q})}} \right\rbrack} \in {\Theta{\lbrack e^{- {n_{i}{(d)}}}\rbrack}}$. Then, in terms of the number of splits, equation yields:

Simply put, each privileged direction should be picked as a splitting normal with a frequency proportional to its weight. Note that this is only relevant *asymptotically*, i.e., as $d\rightarrow\infty$.

### Example

For the Reeds-Shepp vehicle, a valid Lie splitting sequence is:

It is easy to verify that this satisfies equation. In fact, lateral splits occur in the sequence twice as often as longitudinal and lateral splits.

## Experimental results

In this section, we validate our results and compare the performance of our algorithms with different methods from widely used open-source libraries. Query performances are averaged over 1000 randomly drawn query points. The same insertion and query sequences are used across all the analyzed algorithms and generated from a uniform distribution.

### Experiment 1

In this experiment, we confirm the theoretical contributions presented in Section 4. In figure 3(a) ‣ Figure 3 ‣ Experiment 1. ‣ 6 Experimental results ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints") we show the average number of leaves visited when querying a batch $k$-d tree with Euclidean (blue) and Reeds-Shepp metrics (solid red). While the blue curve settles to a constant value, in accordance with Lemma 1. ‣ 4 Complexity Analysis ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints"), the red curve exhibits exponential growth. When normalizing this curve by $\sqrt{N}$ (dashed red), we observe a constant asymptotic behavior, consistent with the rate determined by Theorem 4.1. For comparison, we report the average time for Euclidean queries on an incremental $k$-d tree (black), which tends to visit more vertices than its batch, balanced counterpart (blue).

(a) Average leaves visited (query)

(b) Total distance evaluations

(d) Average query time (μ s)

Figure 3: (a) Experiment 1: Average number of leaves visited during Euclidean (blue) and Reeds-Shepp (red, solid) queries of a batch k-d tree. (b-d) Experiment 2: Performance of different algorithms. In the legends, dE and dR S indicate Euclidean and Reeds-Shepp queries, E B and B B indicate Euclidean Bound and outer Box Bound for ball-hyperplane intersections, 𝒵c l a s s i c and 𝒵R SL i e indicate the splitting sequence.

### Experiment 2

In this experiment (figures figs. 3(b), 3(c) ‣ Figure 3 ‣ Experiment 1. ‣ 6 Experimental results ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints") and 3(d) ‣ Figure 3 ‣ Experiment 1. ‣ 6 Experimental results ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints")), we plot the total number of distance evaluations and the running times observed with different combinations of build and query algorithms. Figure 3(d) ‣ Figure 3 ‣ Experiment 1. ‣ 6 Experimental results ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints") reveals that the proposed outer Box Bound (BB) ball-hyperplane intersection method (yellow, purple, green) reduces the query time significantly as compared to Euclidean bounds (EB) (blue, red), in accordance with our predictions in Section 3.1.

Additionally, Lie splitting (green) further improves query time, as compared with the classic splitting (yellow). The corresponding incremental Lie $k$-d tree also outperforms a classic batch-built one (purple), guaranteed to be balanced.

More important speedups emerge when comparing the proposed $k$-d trees with different techniques, such as Hierarchical Clustering from FLANN and Geometric Near-neighbor Access Tree (GNAT) from OMPL. Interestingly, off-the-shelf implementations of $k$-d trees offered by FLANN and other tools are unusable with nonholonomic metrics altogether, since they are limited to distances of the form of equation. Therefore a comparison is not possible.

All the tested $k$-d trees visibly outperform Hierarchical Clustering (cyan) both in build time and query time. In contrast, GNAT offers competitive query times. However, its insertion is $\sim 100 \times$ slower than incremental k-d trees, since a significant number of distances are evaluated in the build phase, while $k$-d trees only evaluate distances during query. This is reflected in a noticeably higher asymptotic rate of distance evaluations, revealed in figure 3(b) ‣ Figure 3 ‣ Experiment 1. ‣ 6 Experimental results ‣ Efficient Nearest-Neighbor Search for Dynamical Systems with Nonholonomic Constraints").

## Conclusion

Motivated by applications in sampling-based motion planning, we investigated $k$-d trees for efficient nearest-neighbor search with distances defined by the length of paths of controllable nonholonomic systems. We have shown that for sub-Riemannian metrics, the query complexity of a classic batch-built $k$-d tree is $\Theta{({N^{p}{\log N}})}$, where $p \in {\lbrack 0,1)}$ depends on the properties of the system. In addition, we have proposed improved build and query algorithms for $k$-d trees that account for differential constraints. The proposed methods proved superior over classic ones in numerical experiments carried out with a Reeds-Shepp vehicle.

Future work will analyze whether logarithmic complexity is achieved for nonholonomic systems. In addition, the proposed algorithms are exact and rely on explicit distance evaluations. Since distances cannot be generally computed in closed form, we are interested in investigating approximate nearest-neighbor search algorithms with provable correctness bounds that do not require explicit distance computations.
