## Introduction

In the motion planning problem we are given a robot $r$, an environment $E$, and two configurations of $r$ in $E$, denoted $s$ and $t$, and are tasked with finding a *valid* set of motions of $r$ that would take it from configuration $s$ to $t$. A motion is valid (or collision-free) if it does not result in $r$ colliding with itself or any object in the environment.

The problem's intractability lead to the development of randomized sampling based approaches. These sampling based motion planning (SBMP) algorithms reduce the problem to finding an $(s,t)$-curve in the implicit *configuration space* (c-space) defined by $r$ and $E$ that does not contain any point representing an invalid configuration. These methods create a geometric graph in c-space, also known as a *roadmap*, by sampling random points (configurations) and using them to expand the graph. The problem is then reduced further to that of finding a $(s,t)$-path in the graph.

The process of expanding the geometric graph given a sampled point $p$ uses a *neighborhood finder* subroutine to find a set $N$ of candidate points. RRT and RRG extend new graph edges from every point in $q \in N$ towards $p$, but stop the extension process if an invalid configuration is found or a predetermined distance has been reached, and add an edge possibly spanning a partial trajectory between $q$ and $p$. The probabilistic roadmap (PRM) algorithm, on the other hand, will not add a partial edge, and will only connect $p$ and $q$ if the entire trajectory is collision-free, allowing users to opt for collision checking the edge in a non-linear fashion. As hinted by the names of the algorithms, RRT will use a neighborhood finder such that ${|N|} = 1$, creating a tree, while RRG and PRM require larger neighborhoods.

The neighborhood finder subroutine takes a c-space graph $G$ and a c-space point $c$ as arguments, and returns a discrete set of points ${N_{G}{(c)}} \subseteq G$ according to some heuristic, usually the $k$ nearest neighbors ($k{\mathtt{N}\mathtt{N}}$) according to a chosen distance metric. Existing neighborhood finders focus on returning a subset of the graph's vertices while ignoring its edges, even though these edges are often nothing more than a dense sequence of configurations individually checked for collision in a slow and expensive process.

This gap can be explained by two properties of the geometric space, c-space, in which this computation is performed, 1) it can be of arbitrarily high dimensionality, and 2) it can be a mixture of Euclidean and non-Euclidean dimensions. Standard algorithms and data structures applicable in those conditions are somewhat scarce. For example, the Computational Geometry Algorithms Library (CGAL), the most widely used computational geometry library, does not have off-the-shelf $d$-dimensional point-to-segment distance computation or a $d$-dimensional *axis-aligned bounding box tree* (AABB-tree) for segments when $d > 3$, and does not have a standard kernel for a mix of dimension types.

Using a neighborhood finder capable of returning arbitrary points on the tree's swath substitutes the simple Voronoi exploration bias of RRT, where tree vertex is extended with probability proportional to the measure of its cell in the Voronoi diagram of the tree's nodes, in a similar bias that extends from either an interior of an edge or from a vertex with probability proportional to the measure of the Voronoi cell of that object in the Voronoi diagram of points and segments induced by the graph. See Fig. 1 for an illustration of this difference for a 2D scenario.

(a) Heatmap of distance to nearest vertex.

(b) Heatmap of distance to nearest edge.

Figure 1: Heatmaps showing the nearest neighbor distances to a 2D geometric tree. In (a) the set of candidates is the vertices only, and in (b) it is the entire swath of the tree.

### Contribution

In this paper we present the edge-$\mathtt{N}\mathtt{N}$ neighborhood finder, which can return the point on a $d$-dimensional segment in ${\mathbb{R}}^{t} \times {\mathbb{T}}^{r}$, where ${\mathbb{T}}^{i}$ is the $i$-dimensional torus, closest to a query point. The neighborhood finder is based on mixed-$d$-dimensional distance computation primitives that form the basis for an AABB-tree capable of storing a set of segments $S \subseteq {{\mathbb{R}}^{r} \times {\mathbb{T}}^{t}}$ and answering approximate $k{\mathtt{N}\mathtt{N}}$ queries for query points.

We formally prove that this neighborhood finder is expected to produce c-space graphs with shorter edges when used to construct a geometric graph, and experimentally show improvement for RRT which performs less collision detection (CD) calls when using our method compared with neighborhood finders considering only graph vertices. This improvement can be attributed both to the shorter length of the graphs edges and to a superior exploration bias.

### Paper layout

We survey the relevant bodies of research at the end of this section (Section I-A). Important definitions and notations are given in Section II, the algorithmic machinery and the $k{\mathtt{N}\mathtt{N}}$ query of the edge-$\mathtt{N}\mathtt{N}$ neighborhood finder are described in Section III, and the theoretical analysis of edge-$\mathtt{N}\mathtt{N}$ versus the classical subroutine (vertex-$\mathtt{N}\mathtt{N}$) is in Section V. The experiments and the discussion of the results are in Section VI and Section VII respectively.

### I-A Related Work

In, the RRT algorithm is introduced as extending towards a sampled point from its nearest neighbor on the swath of the c-space tree built thus far. LaValle also discuss algorithmic details of such neighborhood finders for different c-spaces. An approximate solution which stores intermediates along edges in a $kD$-tree for the purpose of nearest neighbor queries is also suggested as a simple and effective compromise. In practice, implementations of RRT usually consider only tree vertices as candidates from which to extend new edges.

The RRG algorithm is a variant of RRT that, instead if extending a single edge at every iteration, extends such edges from all neighbor vertices within a certain distance of the sample, thus creating a roadmap graph instead of a tree.

Several nearest neighbor methods were created specifically for neighborhood finders for SBMP algorithms. These methods were designed for nearest neighbor queries in non-Euclidean spaces created by a mixture of positional and rotational degrees of freedom, e.g. SE or ${\mathbb{R}}^{2} \times S^{1}$, and even specifically for concurrent queries used in parallelized SBMP algorithm. In, the authors compare the effectiveness of different exact and approximate nearest neighbor methods for high dimensional motion planning problems.

A large body of work is dedicated to determining which distance metric gives rise to good motion planning algorithms when used to determine the nearest neighbor. In, several workspace and c-space distance metrics are compared experimentally, compares different approximation algorithms for computing distance metrics for rotational DOFs in motion planning for rigid bodies, and examines different metrics for multi-agent motion planning problems. In, a new distance metric for mobile robots is suggested, which is based on decomposing the workspace and prioritizing neighbors in adjacent regions first.

Outside of the context of motion planning, nearest neighbor queries for a point among lines or line segments in high dimensions has been widely researched, with some additional work offering generalizations such as nearest neighbor flats in high dimensional spaces, a moving point query, or in an obstructed environment. Note that the last two papers only deal with the 2D case. Efficient open-source implementations of distance computation and data structures supporting nearest neighbor queries for a variety of geometric objects can be found in CGAL.

## Preliminaries

### II-A Configuration space using positional and cyclical coordinates

Here, we introduce notations necessary for the description and analysis of our algorithms and describe how to handle distances in a configuration space with a mix of translational and rotational coordinates.

### II-A1 Working in cyclical space -- Topological cover

Consider the case that all the coordinates in the configuration space are cyclical (that is, the robot has only rotational DOFs, and $d = r$), and assume for simplicity that each dimension is the interval $\lbrack 0,1\rbrack$. Thus, two points ${p,q} \in {\mathbb{R}}^{d}$ are equivalent as configurations if the fractional parts of their coordinates are equal. In particular, the space ${\mathbb{R}}^{d}$ now decomposes into the natural axis-aligned unit grid $\mathcal{G}$, with the cells being translated copies of ${\lbrack 0,1\rbrack}^{d}$. Thus, the grid forms a *cover* of the torus space ${\mathbb{T}}^{d}$, where each grid cell is a copy of ${\mathbb{T}}^{d}$. The copies of the origin in this cover are: The immediate neighboring copies of the origin (including itself) in this cover are For a point $p \in {\mathbb{R}}^{d}$, we have the following associated copies To be somewhat tediously explicit, all the points of $p_{\mathbb{Z}}$ correspond to a single point of ${\mathbb{T}}^{d}$. These definitions naturally extend to sets $P \subseteq {\mathbb{R}}^{d}$: The *tiling* of ${\mathbb{R}}^{d}$ associated with the point $p$, denoted by $\mathcal{G}_{p}$, is the natural grid $\mathcal{G}$ translated by $p$. Formally, $\mathcal{G}_{p} = {p + \mathcal{G}}$. Similarly, the *cluster* of $T$, denoted by $T_{\pm}$, is the set of $3^{d}$ cells adjacent to a grid cell $T \in \mathcal{G}$ (including itself). The cluster of the tile of $\mathcal{G}$ containing the origin is denoted $O_{\pm}$.

Consider two points ${p,q} \in {\mathbb{R}}^{d}$ in this cyclical space. The distance between them is the minimum distance between any two copies of them. Specifically, we have This naturally extends to distance between sets Figure 2: An illustration of a 2D c-space 𝒞space ⊆ ℝ × 𝕋 and the partial tiling V± associated with it. The translational DOF is marked by x, and the rotational DOF by θ. V± is a set of three copies of 𝒞space.

Consider two points ${p,q} \in {\mathbb{R}}^{d}$. The copy of $p$ in $p_{\mathbb{Z}}$ that is closest to $q$ (under the Euclidean distance) is denoted by ${\mathtt{N}\mathtt{N}}_{p_{\mathbb{Z}}}(q)$. For a point $p' \in p_{\mathbb{Z}}$, all the points $q \in {\mathbb{R}}^{d}$ such that ${{\mathtt{N}\mathtt{N}}_{p_{\mathbb{Z}}}(q)} = p'$, form the *Voronoi cell* of $p'$, denoted by $\mathcal{C}\left( p' \right)$. The collection of all such sets, denoted by $\mathcal{V}\mathcal{D}_{\mathbb{Z}}(p)$, form the *Voronoi diagram* of $p_{\mathbb{Z}}$.

### Observation 1

The Voronoi diagram $\mathcal{V}\mathcal{D}_{\mathbb{Z}}(p)$, being the Voronoi diagram of the vertices of a shifted grid $p_{\mathbb{Z}}$, is the shifted grid ${\mathcal{V}\mathcal{D}_{\mathbb{Z}}(p)} = {p + {\mathbf{1}/2} + \mathcal{G}}$, where $\mathbf{1} = {(1,\ldots,1)} \in {\mathbb{R}}^{d}$.

### Observation 2

A unit cube $C$ whose center lies in a cell $T \in \mathcal{G}_{q}$, can only intersect tiles in $T_{\pm}$.

### Corollary 1

For any two points ${p,q} \in {\mathbb{R}}^{d}$, with $p$ in a cell $T \in \mathcal{G}$, the distance $d(p,q)$, is determined by the copies of $q_{\mathbb{Z}}$ in $T_{\pm}$. That is

### Proof

We notice that $\operatorname{argmin}_{{p' \in p_{\mathbb{Z}}},{q' \in q_{\mathbb{Z}}}}\left\| {p' - q'} \right\|$ is the copy of $q$ in $q_{\mathbb{Z}}$ whose cell in $\mathcal{V}\mathcal{D}_{\mathbb{Z}}(q)$ contains $p$. From Observation 1 we immediately get that the Voronoi cell that contains $p$ must belong to a copy of $q$ found in a cell of $O_{\pm}$. ∎

### Corollary 2

For any two sets ${X,Y} \subseteq {\mathbb{R}}^{d}$ such that $X$ is in a tile $T \in \mathcal{G}$, it is enough to compute the distances between $X$ and the points of $T_{\pm}$ in order to compute $d(X,Y)$. Formally:

### II-A2 The configuration space

Let $E$ be a $d_{E}$-dimensional environment where $d_{E} \in {\{ 2,3\}}$. We assume without loss of generality that $E$ is a $d_{E}$-dimensional box. Let $r$ be a robot with $d$ degrees of freedom (DOFs), out of which $t$ are translational DOFs (i.e. $t > 0$ if the robot is mobile) and $r$ are rotational DOFs (i.e., cyclical), and let $\mathcal{C}_{space} \subseteq {{\mathbb{R}}^{t} \times {\mathbb{T}}^{r}}$ be the associated c-space. We treat this space as a product space.

For two points ${p,q} \in \mathcal{C}_{space}$, consider their components ${p = {({pt},{pr})}},{q = {({qt},{qr})} \in {{\mathbb{R}}^{t} \times {\mathbb{T}}^{r}}}$. Let $\ell t$ be the distance between $pt$ and $q_{t}$ in the translational space ${\mathbb{R}}^{t}$, and $\ell_{r}$ be the be the distance between $pr$ and $qr$ in the rotational space ${\mathbb{T}}^{r}$. The distance between $p$ and $q$ is the $L_{2}$-norm of the combined two distances. That is, ${d(p,q)} = \sqrt{\ell_{t}^{2} + \ell_{r}^{2}}$. See Fig. 2 for an example of a configuration space and the partial tiling $V_{\pm}$ associated with it.

## The new neighborhood finder

In this section, we describe the edge-$k{\mathtt{N}\mathtt{N}}$ neighborhood finder and its building blocks. As a reminder, the configuration space is $\mathcal{C}_{space} = {{\mathbb{R}}^{t} \times {\mathbb{T}}^{r}}$, and the input is a set of line segments $S \subseteq \mathcal{C}_{space}$. Our purpose is to build a data structure that stores $S$, and answers $({1 + \varepsilon})$-approximate $k{\mathtt{N}\mathtt{N}}$ point queries for a predetermined $\varepsilon > 0$. That is, given a point $p \in \mathcal{C}_{space}$ and an integer $k$, return a set of $k$ segments such that the distance of the $i$th segment $s_{i}$ from $p$, $d\left( p,s_{i} \right)$, is within a factor of $({1 + \varepsilon})$ from $p$'s $i$th nearest neighbor in $S$.

We first present the basic geometric operations modified to work in $\mathcal{C}_{space}$, and then use them to build an AABB-tree^11^1AABB = Axis-Aligned Bounding Box. for $\mathcal{C}_{space}$ segments that supports approximate $k{\mathtt{N}\mathtt{N}}$ queries for points of $\mathcal{C}_{space}$. This AABB-tree is the main component of our neighborhood finder, and can return a set of $k$ neighbors of a point $p \in \mathcal{C}_{space}$ such that $\mathcal{C}_{space}$ segments, edges of the c-space graph, may contain a single member of the neighbor set.

The AABB-tree is a modified $kd$-tree for storing segments, and answering nearest-neighbor and intersection queries. The wrinkle is that we need to support rotational coordinates, and we next describe the basic geometric primitives necessary to implement this efficiently. We describe the AABB-tree in more detail in Section III-B.

### III-A Basic Operations in $\mathcal{C}_{space}$

### Point-to-Point Distance

While Corollary 1 gives rise to a simple $O{(3^{d})}$ time operation, since the problem is decomposable we can get a straightforward $O{(d)}$ time algorithm by calculating a 1-dimensional distance in every dimension. The distance between two points ${a,b} \in {\mathbb{T}}^{1}$ is easily computed as follows. Assume without loss of generality that $a < b$, with ${a,b} \in {\mathbb{T}} = {\lbrack 0,1\rbrack}$, we have that For points ${p,q} \in \mathcal{C}_{space}$, we compute $\sqrt{\sum_{i = 1}^{d}{d\left({p{\lbrack i\rbrack}},{q{\lbrack i\rbrack}} \right)^{2}}}$, where the $d$ is either the Euclidean or cyclical distance, as appropriate for the coordinate under consideration.

### Point-to-AABB Distance

A similar strategy to that used for point-to-point distance computation can be employed when computing the distance between a point $p \in \mathcal{C}_{space}$ to an axis-aligned bounding box $b = {I_{1} \times \ldots \times I_{d}} \subseteq \mathcal{C}_{space}$. Since $b$ is axis-aligned, this problem is, again, decomposable, and can be presented as $d$ calculations of a $1$-dimensional point-to-interval distance. While the general case is slightly harder, our data structure contains only AABBs fully contained within a single tile of $\mathcal{G}$, namely ${}^{r}$, thus enabling us to simply check the signed distances ${{p{\lbrack i\rbrack}} - b}.{max{\lbrack i\rbrack}}$ and $b.{{min{\lbrack i\rbrack}} - {p{\lbrack i\rbrack}}}$ between the coordinate of the point and the appropriate interval in order to decide whether ${p{\lbrack i\rbrack}} \in I_{i}$ or get the true distance between the point and the interval.

### Point-to-Segment Distance

The task of computing the distance between a point $p \in \mathcal{C}_{space}$ and a segment $s \subseteq \mathcal{C}_{space}$ is somewhat trickier as it is not decomposable. However, for the simple case where $s \subseteq {{{\mathbb{R}}t} \times {}^{r}}$, i.e. $s$ does not "wrap around" any of the cyclic dimensions, we can avoid exponential dependence on the dimension by only computing point-to-segment distances between $s$ and $O{(d)}$ members of $p_{\mathbb{Z}}$ as we show in the following claim.

### Claim 1

For a point $p \in \mathcal{C}_{space}$ and a segment $s \subseteq {{\mathbb{R}}^{t} \times {}^{r}}$, there is a set of $O{(d)}$ points $X \subseteq p_{\mathbb{Z}}$, which can be computed efficiently, such that

### Proof

The only points in $p_{\mathbb{Z}}$ that might define $d(p,s)$ are those points whose Voronoi cell in $\mathcal{V}\mathcal{D}_{\mathbb{Z}}(p)$ intersects $s$, i.e. $\left\{ {p' \in p_{\mathbb{Z}}} \middle| {{{\mathcal{C}\left( p' \right)} \cap s} \neq \varnothing} \right\}$. Let $s = {ab}$. By Observation 2, the sequence of Voronoi cells of $\mathcal{V}\mathcal{D}_{\mathbb{Z}}(p)$ encountered by continuously moving from $a$ to $b$ along $s$ all belong to a single cluster. This sequence starts with the (grid/Voronoi cell) $\mathcal{C}\left( {{\mathtt{N}\mathtt{N}}_{p_{\mathbb{Z}}}{(a)}} \right)$, and ends with $\mathcal{C}\left( {{\mathtt{N}\mathtt{N}}_{p_{\mathbb{Z}}}{(b)}} \right)$. The current cell changes, only when this moving point crosses a bisector of the Voronoi diagram. The Voronoi diagram in this case being the shifted grid, has bisectors that are hyperplanes orthogonal to the axes. In particular, as $s$ extent in each rotational dimension is at most $1$, it follows that $s$ can cross at most one bisection that is orthogonal to a specific dimension. Thus, $s$ crosses at most $d$ bisectors, and overall visits at most $d + 1$ cells.

To this end, we compute the $2d$ intersections of the line supporting $s$ with the (at most) $2d$ (or being more careful, the $d$ relevant ones) hyperplanes bounding its cell. By sorting them along $s$, we can then perform this traversal in $O{({d{\log d}})}$ time.

See Algorithm 1 for the pseudocode. ∎ input: Point p, segment s = ab ⊆ r 5 b ← get_next_bisector(curr, v, VD) 6 P ← P ∪ get_point_from_bisector(b) 7 curr ← advance_to_next_bisector(curr, v, b) Algorithm 1 Point to Segment Distance In order to be able to use Algorithm 1 we break down every graph edge into sub-segments that are contained in ${}^{r}$. See Fig. 3 for an illustrations. Similar reasoning to that of Claim 1 gives us that a segment that corresponds to the shortest distance between its two $\mathcal{C}_{space}$ endpoints will only be broken down into $O{(d)}$ segments, and an algorithm similar to Algorithm 1 can be used to compute these segments.

Figure 3: The shortest segment between the points marked a and b in a 𝒞space composed of two rotational DOFs. The segment is divided into three segments marked s1, s2, and s3.

Figure 4: An illustration of a point-to-segment distance calculation between p and s in a 2D c-space 𝒞space = 𝕋2. The two rotational DOFs are marked by θ1 and θ2, and V± is a set of 9 copies of 𝒞space. Marked in orange are the points in p± that give rise to the bisectors required for the point-to-segment distance, and the bisectors forming the Voronoi diagram 𝒱𝒟ℤ(p). The three points for which we check the distance to s are denoted p1, p2, and p3, and their Voronoi cells, visited by s, are highlighted.

Finally, since we have reduced the point-to-segment problem to $O{(d^{2})}$ point-to-segment distance computations in ${\mathbb{R}}^{d}$, we can use a simple subroutine that returns the Euclidean distance as well as the point on $s$ closest to $p$, that is ${\mathtt{N}\mathtt{N}}_{s}{(p)}$.

### Computing segment-AABB intersection

By storing only boxes and segments contained in ${}^{r}$ we can use a simple Euclidean subroutine in order to check box-segment intersections.

### III-B Edge-$k{\mathtt{N}\mathtt{N}}$ neighborhood finder

Using the simple operations described above we construct an AABB-tree to store the $d$-dimensional segments and answer approximate $k{\mathtt{N}\mathtt{N}}$ queries using a simplified version of the well known algorithm by Arya et al..

Our tree is built by recursively splitting an AABB containing a set of segments into at most three children nodes, starting at the root with an AABB the full list. When splitting a node we define an axis-parallel hyperplane that splits the segments into three roughly equal groups, two sets that are fully contained in either sides, and one set of all segments that intersect the hyperplane.

The set of segments is created by "cutting" the graph's edges as described above, and maintains a mapping between these and their "parent" graph edge. The $k{\mathtt{N}\mathtt{N}}$ query makes sure to only keep at most one "child" of each edge in the heap containing the nearest neighbors, while still checking children of an edge even if another child is already in the heap.

Upon finishing the $k{\mathtt{N}\mathtt{N}}$ query with a set of c-space segments and the points on these segments closest to $p$, the data structure uses the mapping to get the corresponding set of edges and returns both the edge IDs and the closest points to the SBMP algorithm, so that it could test for a connection/extension between them and the sampled point $p$. Note that some of the edges might be degenerated, meaning vertices of the $\mathcal{C}_{space}$ graph, but otherwise the edge is split in two at the endpoint of the newly added edge.

The tree is parameterized by several quantities: $n_{{leaf}_{thresh}}$ is the threshold for the number of segments that will trigger a further split (as opposed to making the node a leaf). $n_{buff}$ is the size of the buffer for edge insertion. When the buffer is full the tree is rebuilt with all of the previous edges and the ones stored in the buffer. $n_{{leaf}_{ratio}}$ is the threshold ratio between the number of segments stored in the child node to that stored in the parent. If a child contains more than $n_{leaf_ ratio}$ times the number of segments in its parent it becomes a leaf. This parameter is crucial to deal with edge cases in which a set of segments cannot be even somewhat evenly split by any axis-parallel hyperplane.

The tree also supports deletions using a deletion buffer that prevents deleted segments from being considered as neighbors and from being included when the tree is rebuilt.

## cobweb-RRG: Motion planning algorithm

### IV-A The cobweb algorithm

The exploration bias of the edge-$\mathtt{N}\mathtt{N}$ neighborhood finder provides us with a simple heuristic for finding narrow passages in c-space using extensions. In the presence of a narrow passage, RRT requires a vertex of the tree relatively close to the passage, and a sample in the "right" direction that would lead to an extension of an edge into the passage.

However, as illustrated in Fig. 5a, the vertices of the tree might not be situated in "useful" locations. Namely, the region from which a sample must be drawn can be of a tiny measure. When using edge-$\mathtt{N}\mathtt{N}$, an edge of the tree shooting across the narrow passage is enough to give rise to a set of bigger measure of beneficial samples, as Fig. 5b illustrates.

We propose the Cobweb algorithm (cobweb-RRG), a variant of RRG designed to take advantage of the properties of edge-$\mathtt{N}\mathtt{N}$. cobweb-RRG mimics RRT in open regions of c-space, and span webs of edges across regions of *contact-space*, the boundary between free-space and obstacle-space, the subsets of c-space that form the natural partition to valid and invalid configurations respectively, where the openings of narrow passages may exist. See Fig. 5c for an illustration of the intuition -- the idea is to create a net-like structure (i.e., cobweb) that can cover the entry of a (potentially narrow) tunnel. Then, a sample that leads from the net into the tunnel would facilitate finding a solution (hopefully quickly).

(a) Extensions with vertex-NN (b) Extensions with edge-NN (c) Intuition for cobweb-RRG Figure 5: Illustration of intuition for cobweb-RRG. The edge uv and the environment in (a) and (b) are identical, and in each one we denote in red, blue, and green the Voronoi regions of the vertices and the interior of the edge respectively, and in darker shades the subsets of samples that are “useful” in the effort of finding the passage. Several examples of successful and failed extensions are also depicted. In (c) we give an illustration of the intuition behind the algorithm as described in Section IV-A.

### IV-B Algorithm

The pseudocode for the cobweb-RRG algorithm is shown in Algorithm 2. The algorithm mimics RRT while maintaining $P_{CS}$, the set of contact-space points add to the graph so far, and iterates over a simple loop of sampling and extending. We specify that the neighborhood finder used in line 2 is edge-$\mathtt{N}\mathtt{N}$ since this algorithm was specifically designed to take advantage of its properties, while an RRT can use many different subroutines without forfeiting its power. After every successful extension (line 2), we check if the new endpoint lies in contact-space (line 2). In our implementation, an extension that stops before reaching the maximum allowed extension length is immediately marked as a contact-space point. If the new vertex is in contact space, we call a $\mathtt{c}\mathtt{o}\mathtt{n}\mathtt{n}\mathtt{e}\mathtt{c}\mathtt{t}$ subroutine, which PRM's equivalent of the $\mathtt{e}\mathtt{x}\mathtt{t}\mathtt{e}\mathtt{n}\mathtt{d}$ operation, which connects a configuration to a set of candidates according to some heuristic. In this case we do not require that the connector used is edge-$k{\mathtt{N}\mathtt{N}}$, as it is not integral to the algorithm's approach. the algorithm finishes, as most SBMP algorithms do, when the goal configuration is successfully added to the graph, and returns an $(s,t)$-path found by some SSSP algorithm (line 2). input: Robot r, Environment E, Configurations (s, t) 2 PCS ← ⌀ # The set of contact space points 6 if is_contact_space(q) then 7 G.connect(q, PCS) # connects to kNN from candidate set PCS

## Theoretical analysis

The intuition regarding the use edge nearest neighbors is straightforward. Choosing the nearest neighbor from a much larger set of candidates, in this case a large set of intermediate points on the edges, will result in shorter edges, which in turn leads to less CD calls and faster runtimes. See Fig. 1 for a 2D illustration. For $n\longrightarrow\infty$, $n$ being the number of sampled configurations, this intuition is true in any motion planning scenario, but for a given $n$ we cannot prove a catch-all lemma guaranteeing a reduction of overall edge lengths due to pathological cases, e.g. a c-space consisting of a narrow 2-dimensional annulus. Instead, we prove a lemma that formalizes the aforementioned intuition and captures many reasonable motion planning scenarios.

Let $B$ be the $d$-dimensional box, and let $P \subseteq B$ be a sequence $(p_{1},\ldots,p_{n})$ of $n$ points chosen uniformly at random from $B$. Consider Algorithm 3, a simple algorithm for the creation of a geometric tree using $P$ by iteratively adding points and connecting them to the tree. input: Point set P = {pi}i = 1n ⊆ ℝd, Function connect(⋅, ⋅) Algorithm 3 Build Geometric Tree Let $T$ be the tree returned by Algorithm 3 for the input $P$, ${\mathtt{v}\mathtt{e}\mathtt{r}\mathtt{t}\mathtt{e}\mathtt{x}\mathtt{N}\mathtt{N}}{(\cdot, \cdot)}$, where the latter a function that connects a point to its nearest tree vertex, and let $T'$ be the tree returned for the input $P$, ${\mathtt{t}\mathtt{r}\mathtt{e}\mathtt{e}\mathtt{N}\mathtt{N}}{(\cdot, \cdot)}$, the latter being a function that connects a point to the nearest point in the tree swath, i.e. a vertex or any point on an edge.

We denote the expected sum of edge lengths of a geometric graph $G$ by $\left\| G \right\|$, and claim that, under certain conditions, ${{\mathbb{E}}\left\lbrack \left\| T' \right\| \right\rbrack} \leq {{c_{d} \cdot {\mathbb{E}}}\left\lbrack \left\| T \right\| \right\rbrack}$ for some dimension dependent constant factor $c_{d} < 1$. In other words the expected "length" of $T$ is larger than that of $T'$ by a constant factor that depends on the dimension $d$.

The condition we use here is likely stronger than the weakest possible condition, and it is that for any point $p_{i} \in P$, the direction of the segment connecting $p_{i}$ to $T$ or $T'$ is uniformly distributed. Since we also assume the operation $\mathtt{c}\mathtt{o}\mathtt{n}\mathtt{n}\mathtt{e}\mathtt{c}\mathtt{t}$ is always successful these settings are obviously not realistic, but at the same time assuming that directions of connection/extension attempts of SBMP algorithms are distributed somewhat uniformly, even in the presence of obstacles, seems reasonable.

We now state and prove the lemma.

### Lemma 1

Let $P = {\{ p_{1},\ldots,p_{n}\}}$ be a set of points sampled uniformly at random from $B$, let $T$ and $T'$ be the output of Algorithm 3 on the inputs $\left( P,{{\mathtt{v}\mathtt{e}\mathtt{r}\mathtt{t}\mathtt{e}\mathtt{x}\mathtt{N}\mathtt{N}}{( \cdot, \cdot )}} \right)$, and $\left( P,{{\mathtt{t}\mathtt{r}\mathtt{e}\mathtt{e}\mathtt{N}\mathtt{N}}{( \cdot, \cdot )}} \right)$ respectively, and assume that for any point $p_{i} \in P$ the direction of the segment connecting $p_{i}$ to $T$ or $T'$ is uniformly distributed. Then there exists a constant $c_{d} < 1$ such that ${\mathbb{E}\left\lbrack \left\| T' \right\| \right\rbrack} \leq {c_{d}{\mathbb{E}\left\lbrack \left\| T \right\| \right\rbrack}}$.

### Proof

Let $\ell_{i}$ and $\ell_{i}'$ be the segments added to $T$ and $T'$ respectively in the $i$th iteration of Algorithm 3. We will show that ${\mathbb{E}\left\lbrack \left\| \ell_{i}' \right\| \right\rbrack} \leq {c_{d} \cdot {\mathbb{E}\left\lbrack \left\| \ell_{i} \right\| \right\rbrack}}$ where by some abuse of notation $\left. \parallel \cdot \parallel \right.$ is the length of segment operator. This immediately implies the claim of the lemma.

We first define some terms and notations. We denote the set ${\{ p_{1},\ldots,p_{k}\}} \subseteq P$ by $P_{k}$, and the induced trees ${T{\lbrack P_{k}\rbrack}},{T'{\lbrack P_{k}\rbrack}}$ created by the algorithm after $k$ iterations by $T_{k}$ and $T_{k}'$ respectively. Let $p_{j} = {{\mathtt{N}\mathtt{N}}_{P_{i - 1}}{(p_{i})}}$.

Note that since $T_{k}'$ considers a superset of $P_{k - 1}$ as nearest neighbor candidates when connecting $p_{i}$ to the tree, we have that $\left\| \ell_{k} \right\| \leq \left\| \ell_{k}' \right\|$ for every $k \in \left. ⟦n \right.⟧$. One of the cases in which we have a strong inequality is when some edge $p_{j}p_{l}$ incident to $p_{j}$ has its other vertex in the general direction of $p_{i}$, which makes the distance from $p_{i}$ to that edge shorter than $\ell_{i}$.

Consider the $d$-dimensional sphere centered at $p_{j}$. $p_{j}$ has at least one neighbor in $T_{j}'$, namely ${{\mathtt{N}\mathtt{N}}_{T_{j - 1}'}{(p_{j})}},$ which we denote $p_{l}$. We can show that with some constant probability $\left\| {p_{j}p_{l}} \right\| \geq \left\| {p_{j}p_{i}} \right\|$ (see Lemma 2 for full details), and since by our assumption the direction of the vector ${p_{l}} - p_{j}$ is uniformly distributed, we can compute a bound on the expected length of $\ell_{i}'$ by a mostly straightforward computation of the expected value $\int_{p \in {\mathbb{S}}_{d}}{f{(p)}\left\| {p_{i} - {p_{j}p}} \right\|{dp}}$ where ${\mathbb{S}}_{d}$ is the $d$-dimensional unit sphere, and $\left\| {p_{i} - {p_{j}p}} \right\| = {\min_{q \in {p_{j}p}}\left\| {p_{i} - q} \right\|}$.

We assume without loss of generality that $p_{j}$ is the origin, $\left\| \ell_{i} \right\| = 1$, and $p_{i}$ is the "north pole" $(\overset{d - 1}{\overbrace{0,0,{\ldots ⁢0}}},1)$. See Fig. 6 for an illustration.

Let $\alpha_{d}$ be the surface area of ${\mathbb{S}}_{d}$. Observe that the surface area of a ball of radius $r$ is $\alpha_{d}r^{d - 1}$. It is well known that we have the formula Which, intuitively adds the "slices" of a sphere, which are lower dimensional spheres, to compute its surface or volume. The red sweep line in Fig. 6 defines a "slice" of the 2D sphere which is a 1D sphere of length $\sqrt{1 - y^{2}}$. If a point $p$ on the sphere has negative $x_{d}$ coordinate, then $\left\| \ell_{i}' \right\|$ is $1$, but otherwise, we have that the average distance is since $\sqrt{1 - x_{d}^{2}}$ is the distance from $p_{i}$ to a segment created by the slice with distance $x_{d}$ from $p_{j}$, see the blue segment marked $x$ in Fig. 6, and ${\alpha_{d - 1} \cdot \left(\sqrt{1 - x_{d}^{2}} \right)^{d - 2}}\frac{1}{\alpha_{d}}$ is the measure of the sphere "slice" normalized as a fraction of the whole sphere.

Thus, the overall expected distance of $p_{i}$ to a random segment $p_{j}p$ such that $p$ on the sphere is $\Delta = {F + {1/2}}$. It is known that ${\alpha_{d} = \frac{2\pi^{d/2}}{\Gamma{({d/2})}}},$ where Thus, if $d = {{2k} + 1}$ is odd, we have By the definition of the double factorial, we have And thus, we have it is known that ${\binom{2k}{k} \leq {\frac{2^{2k}}{\sqrt{\pi k}}\left({1 - \frac{1}{7k}} \right)}}.$ And thus, we have This readily implies that $\Delta = {F + {1/2}} \leq {1 - {{1/6}k}}$. The case where $d$ is even is similar.

This implies that with constant probability $\left\| \ell_{i}' \right\| \leq {c_{d} \cdot \left\| \ell_{i} \right\|}$ for some dimension dependent constant $c_{d} < 1$, and since $\left\| \ell_{i}' \right\| \leq \left\| \ell_{i} \right\|$ we have that ${\mathbb{E}\left\lbrack \left\| \ell_{i}' \right\| \right\rbrack} \leq {c_{d} \cdot {\mathbb{E}\left\lbrack \left\| \ell_{i} \right\| \right\rbrack}}$ which immediately implies ${\mathbb{E}\left\lbrack \left\| T' \right\| \right\rbrack} \leq {c_{d} \cdot {\mathbb{E}\left\lbrack \left\| T \right\| \right\rbrack}}$. ∎ Figure 6: Illustration of the proof of Lemma 1

## Experiments

In this section we provide experimental results supporting the claims that using the Edge-$k{\mathtt{N}\mathtt{N}}$ neighborhood finder results in shorter edges, and provides improved exploration properties when used by an RRT search in $\mathcal{C}_{space}$. The experiments are all run in simulation, and include mobile robots (simple 3 and 6 DOF polyhedral robots) and fixed-base manipulators (7 DOF manipulator with revolute joints).

In Section VI-A we compare roadmaps created by RRT and PRM algorithms on empty environments using our neighborhood finder compared with a common vertex-$\mathtt{N}\mathtt{N}$ one in order to provide experimental verification to the intuition and theoretic analysis regarding the overall length of c-space graphs.

In Section VI-B we test the exploration properties of RRT in several motion planning scenarios and compare its effectiveness when using vertex-$\mathtt{N}\mathtt{N}$ and edge-$\mathtt{N}\mathtt{N}$ neighborhood finders for solving motion planning tasks.

*An important note:* In each of the experimental settings where an algorithm was run $N$ times with vertex-$\mathtt{N}\mathtt{N}$ and $N$ times with edge-$\mathtt{N}\mathtt{N}$ using the same parameters, we randomly generated a list of $N$ seeds that were then used for both sequences of runs. The seeds are used in the code when generating random samples, and thus the comparisons between the two neighborhood finders can be seen as a collection of head-to-head comparisons of the algorithms when given the exact same set of samples during runtime.

Also, in the bar plots showcasing the results of the experiments (Fig. 7a, Fig. 8a, Fig. 9a) some outliers were removed from the visualization for the sake of image clarity. These values were not removed from the computations of the average, mean, standard deviation, min, and max values, and all of the data are stored by the authors.

### VI-A Roadmap length

In this experiment we run RRT and PRM with four different robots in empty environments, and report the number of CD checks performed in order to construct and validate the graph and the overall edge length. This is despite the fact that these two quantities are closely correlated in empty environments as almost no edges are invalid, meaning that most CD calls are translated directly to edge length.

For every combination of robot-environment and $k$ we ran RRT/PRM 100 times with each neighborhood finder.

A summary of the results can be found in Table VI-A.

—c—c—c—c—c—c—c— \CodeBefore\rectanglecolorlightgray3-24-2 \rectanglecolorlightergray3-33-7 \rectanglecolorlightgray4-34-7 \rectanglecolorlightblue5-26-2 \rectanglecolorlighterblue5-35-7 \rectanglecolorlightblue6-36-7 \rectanglecolorlightgray7-28-2 \rectanglecolorlightergray7-37-7 \rectanglecolorlightgray8-38-7 \rectanglecolorlightblue9-210-2 \rectanglecolorlighterblue9-39-7 \rectanglecolorlightblue10-310-7 \rectanglecolorlightgray11-212-2 \rectanglecolorlightergray11-311-7 \rectanglecolorlightgray12-312-7 \rectanglecolorlightblue13-214-2 \rectanglecolorlighterblue13-313-7 \rectanglecolorlightblue14-314-7 \Bodyk Metric (Avg.) NF DOF composition 3Pos.+0Rot. 3Pos.+3Rot. 7 Revolute 10 Revolute

#CD calls

#CD calls

#CD calls

VI-B Exploration quality In this experiment we run RRT on four motion planning instances. Three instances, the simple passage, z-shaped passage, and cluttered space, are for a 6DOF mobile robot, and the fourth instance is for a 7DOF manipulator arm. We solve every instance using either edge-NN or vertex-NN as a neighborhood finder and report results of three metrics, the number of CD calls, runtime, and number of RRT iterations required to solve the task. In the rest of this section we describe each of the motion planning tasks in greater detail, and provide important information on the settings in which the experiments were conducted. The results are summarized in Table VII. VI-C Motion planning tasks An environment of size 10 × 10 × 10 divided by a wall perpendicular to the z-axis with a single passage going through it. The passage is a rectangular hole in the wall with a clearance of 0.9 at its center. The robot, a 6DOF 2 × 1 × 1 rectangular prism, can fit through the passage only if properly oriented and moving in a specific direction. The motion planning task requires the robot to get from a configuration on one side of the environment to the other. See Fig. 6b for an illustration of the scene.

Figure 7: In (a) we present the results of the simple passage motion planning experiment (200 RRT runs). The green line and yellow marker emphasize the median and the mean respectively. In (b) we see an illustration of the simple passage environment with the robot halfway through the passage to showcase the tight fit.

An environment of size 20 × 20 × 20 similar in flavor to the simple passage one. it too is divided by a wall perpendicular to the z-axis with a single passage going through it. The passage is rectangular with a clearance of 1.4 along its medial axis, but it is not simply a hole but rather a corridor. Its opening and exit have the same y-coordinates, but are shifted along the x-axis, thus requiring two turns in opposite directions - right, and then left. The robot is the same 6DOF 2 × 1 × 1 rectangular prism used in the simple passage experiment, but it can fit through the z-passage in any orientation if well centered. We originally considered a tighter fitting passage, but the runtime, averaging several minutes even in the current settings, quickly became unreasonable as we shrunk the passage. The motion planning, similarly to the simple passage task, requires the robot to cross the wall using the passage. See Fig. 7b for an illustration of the scene.

Figure 8: In (a) we present the results of the z-passage motion planning experiment (200 RRT runs). The green line and yellow marker emphasize the median and the mean respectively. In (b) we see an illustration of the z-passage environment.

A 10 × 10 × 10 environment containing a 3D grid of 5 × 5 × 5 cubes of sidelength 0.8 with centers on grid vertices and arbitrary orientations. Two diagonally opposing cubes on the 5 × 5 × 5 grid are missing, and the motion planning task requires the robot, a 6DOF cube of sidelength 0.8, to get from the location of one missing cube to that of the diagonally opposing missing cube. See Fig. 8b for an illustration of the scene.

Figure 9: In (a) we present the results of the clutter motion planning experiment (500 RRT runs). The green line and yellow marker emphasize the median and the mean respectively. In (b) we see an illustration of the clutter motion planning task.

A 50 × 50 × 50 environment with four rectangular pillars perpendicular to the xy-plane and spanning from one side of the environment to the other, and a 7DOF manipulator with base fixed at the center of the floor of the environment (at the center of the xy-plane and with a z-coordinate of 0). The manipulator has 7 revolute joints and a conic end-effector. The motion planning task requires the manipulator to move from a configuration entangled with two of the pillars to one symmetrically entangled with the other two pillars. See Fig. 9b for an illustration of the scene including the start and goal configurations.

Figure 10: In (a) we present the results of the 7DOF manipulator motion planning experiment (500 RRT runs). The green line and yellow marker emphasize the median and the mean respectively. In (b) we see an illustration of the 7DOF manipulator motion planning task with the outlines of the start and goal configurations shown in blue and red respectively.

The experiments included RRT 200 runs (with each neighborhood finder) on the simple passage and z-passage tasks, and 500 runs (with each neighborhood finder) on the clutter and 7DOF manipulator tasks. VI-D System and implementation details All of the experiment code relies on the C++ Parasol Planning Library (PPL) RRT and PRM implementations. RRT was run with minimum and maximum extension parameters set to 0.01 and 4.0 respectively, the goal was sampled once in every 100 iterations, and an attempt to connect the tree to the goal was also made whenever a node that was added to the tree was within a Euclidean distance of 3.0 units from the goal. PRM sampled a maximum of 10 times in an attempt to add 5 nodes the roadmap in every iteration. Collision detection was done using GAMMA’s PQP algorithm. The simple passage and z-passage motion planning experiments were run on a desktop using Intel i7-10700 CPU 2.90GHz, with 32GB of RAM. All other experiments were run on a laptop using Intel i7-11800H CPU 2.30GHz, with 32GB of RAM. Unsurprisingly, the results of the roadmap length experiments conducted in empty environments described in Section VI-A corroborate the simple intuition, and, to a certain degree, the theoretic findings proven in Section V. The variance in these experiments was low, meaning that the results shown in Table VI-A truthfully represent the gap between using vertex-NN and edge-NN. As expected, as the number of DOFs grows, the effect of using our algorithm diminishes, but when using PRM and as the number of connections (k) increases, the advantage becomes well pronounced. A curious finding not shown in the data, is that even though in every iteration of RRT the neighbor found with edge-NN is closer to the sample than that found by vertex-NN, using the same seed of course and thus the same sample, in many iterations the extension distance achieved using the former neighborhood finder was greater. The motion planning experiments described in Section VI-B contain several interesting results. First, we see that edge-NN provides superior exploration guidance in the presence of narrow passages, where its advantage is so pronounced that it meaningfully affects the runtime of RRT regardless of the longer runtime required by its NN function. However, this advantage can be seen in all of the experiments, and expresses itself also in the lower number of iterations required to complete all of the motion planning tasks, and this is - as a reminder, even though the different neighborhood finders compete using the same random seeds. However, the cost of using a more complex neighborhood finder is reflected in worse runtimes for easier motion planning tasks in simple environments, i.e. where the combinatorial complexity of the robot and the set of obstacles is relatively low.

—c—c—c—c—c—c—c—c—c—c—c— \CodeBefore\rectanglecolorlightgray2-23-2 \rectanglecolorlightergray2-32-8 \rectanglecolorlightgray3-23-8 \rectanglecolorlightblue4-25-2 \rectanglecolorlighterblue4-34-8 \rectanglecolorlightblue5-25-8 \rectanglecolortan6-27-2 \rectanglecolorlighttan6-36-8 \rectanglecolortan7-27-8 \rectanglecolorlightgray8-29-2 \rectanglecolorlightergray8-38-8 \rectanglecolorlightgray9-29-8 \rectanglecolorlightblue10-211-2 \rectanglecolorlighterblue10-310-8 \rectanglecolorlightblue11-211-8 \rectanglecolortan12-213-2 \rectanglecolorlighttan12-312-8 \rectanglecolortan13-213-8 \rectanglecolorlightgray14-215-2 \rectanglecolorlightergray14-314-8 \rectanglecolorlightgray15-215-8 \rectanglecolorlightblue16-217-2 \rectanglecolorlighterblue16-316-8 \rectanglecolorlightblue17-217-8 \rectanglecolortan18-219-2 \rectanglecolorlighttan18-318-8 \rectanglecolortan19-219-8 \rectanglecolorlightgray20-221-2 \rectanglecolorlightergray20-320-8 \rectanglecolorlightgray21-221-8 \rectanglecolorlightblue22-223-2 \rectanglecolorlighterblue22-322-8 \rectanglecolorlightblue23-223-8 \rectanglecolortan24-225-2 \rectanglecolorlighttan24-324-8 \rectanglecolortan25-225-8 \BodyExperiment Metric NF Average Median STD min max Runtime (sec.) Edge-NN 207 39.1 536 0.17 4760

#Iterations Edge-NN 0.38 × 105 0.22 × 105 0.43 × 105 221 2.5 × 105

Runtime (sec.) Edge-NN 169 192 126 6.23 2290.0

#Iterations Edge-NN 19877 17170 15497 251 1.5 × 105

clutter (500 runs) #CD calls Edge-NN 34162 28948 19584 6027 1.16 × 105 Runtime (sec.) Edge-NN 1.66 1.05 1.37 0.21 6.45

#Iterations Edge-NN 1041 572 914 161 3384

manip. (500 runs) #CD calls Edge-NN 38050 28848 33078 421 2.29 × 105 Runtime (sec.) Edge-NN 4.31 2.66 5.17 0.05 50.1

#Iterations Edge-NN 4031 2878 6102 88 1.16 × 105
