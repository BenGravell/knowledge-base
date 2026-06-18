<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Asymptotically Optimal Path Planning with an Approximation of the Omniscient Set

Topics include Path planning, Planning, Sampling.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The asymptotically optimal version of Rapidly-exploring Random Tree (RRT*) is often used to find optimal paths in a high-dimensional configuration space. The well-known issue of RRT* is its slow convergence towards the optimal solution. A possible solution is to draw random samples only from a subset of the configuration space that is known to contain configurations that can improve the cost of the path (omniscient set). A fast convergence rate may be achieved by approximating the omniscient with a low-volume set. In this letter, we propose new methods to approximate the omniscient set and methods for their effective sampling. First, we propose to approximate the omniscient set using several (small) hyperellipsoids defined by sections of the current best solution. The second approach approximates the omniscient set by a convex hull computed from the current solution. Both approaches ensure asymptotical optimality and work in a general n-dimensional configuration space. The experiments have shown superior performance of our approaches in multiple scenarios in 3D and 6D configuration spaces.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The task of optimal path planning is to find a collision-free path with the lowest cost (e.g., path length) from a start configuration to a goal configuration. Low-dimensional configuration spaces can be discretized, and the optimal path can be searched using, e.g., A\*. Sampling-based motion planners, e.g., Rapidly-exploring Random Tree (RRT), search the configuration space using randomized sampling, and they are more suitable for searching high-dimensional spaces than the discretization methods. RRT\* is an asymptotically optimal variant of the RRT algorithm. RRT\* continues the search even after the first feasible solution is found. Moreover, RRT\* uses a rewiring technique to optimize node connection within the tree, so the costs of the nodes decrease with the increasing number of samples. The rewiring process relies on nearest-neighbor search, and it becomes more computationally intensive with the increasing size of the tree, which leads to the well-known slow convergence of RRT\*.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

RRT\* samples the whole configuration space, which is not necessary, as there exist states that cannot possibly improve the existing solution. This was first observed where the "omniscient set" is defined. The omniscient set is a subset of the configuration space suitable for finding the optimal solution. In obstacle-free environments, it has a form of prolate n-dimensional hyperellipsoid. Drawing samples only from the hyperellipsoid has been shown to improve the convergence towards the optimal solution. However, for long zig-zag paths, the volume of the hyperellipsoid may still be too large, which causes Informed-RRT\* to perform similarly as RRT\*.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose two approaches to approximate the omniscient set. The first proposed approach employs multiple small hyperellipsoids defined by subsections of the current best solution. This set ensures asymptotic optimality. The second approach computes a convex hull of a path rotated along a line from start to goal. Finally, we combine these two approaches and show how to achieve asymptotic optimality with them. We show how to efficiently sample these sets. Both approaches can be extended to higher dimensions. In comparison to state-of-the-art methods, the proposed approaches converge faster towards the optimal solution.

<!-- chunk {"id": "body-0006", "role": "body", "section": "The Motivation behind Proposed Methods", "weight": 1.0} -->

The original RRT and RRT\* algorithms sample the whole configuration space $\mathcal{C}$ uniformly. We define the sampling space $\mathcal{S} \subseteq \mathcal{C}$ as the region from which the random samples are drawn (i.e., in RRT and RRT\*, $\mathcal{S} = \mathcal{C}$). As was shown, only a subset of the configuration space contains samples that can possibly improve the cost of the path $\mathcal{P}$ (and it is guaranteed that samples outside this set cannot improve the cost of the path $\mathcal{P}$).

<!-- chunk {"id": "body-0007", "role": "body", "section": "The Motivation behind Proposed Methods", "weight": 1.0} -->

where $\mathcal{P}_{to}$ is a path from $q_{start}$ to a configuration $q$ and $\mathcal{P}_{from}$ is a path from a configuration $q$ to $q_{goal}$. The lengths of the paths can be approximated with a heuristic. The Euclidean distance heuristic would lead to the "informed set" $S_{i}$, which is a prolate hyperellipsoid

<!-- chunk {"id": "body-0008", "role": "body", "section": "The Motivation behind Proposed Methods", "weight": 1.0} -->

To improve the length of the path, it is sufficient to draw random samples only from the informed set $\mathcal{S}_{i}$, as no configurations outside $\mathcal{S}_{i}$ can improve the cost of the path. This is the core of Informed-RRT\* which draws random samples only from $\mathcal{S}_{i}$, and where the set $\mathcal{S}_{i}$ is defined using the length of the current best path.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The Motivation behind Proposed Methods", "weight": 1.0} -->

However, the volume of $\mathcal{S}_{i}$ can still be quite high (especially for long zig-zag paths), which is depicted in Fig.. Moreover, it is not guaranteed that all configurations from the informed set $\mathcal{S}_{i}$ can improve the path.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The Motivation behind Proposed Methods", "weight": 1.0} -->

(a) Sampling space 𝒮 of Informed-RRT* for a given path.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The Motivation behind Proposed Methods", "weight": 1.0} -->

(b) Sampling space 𝒮 of one of our proposed planners for the same path.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The Motivation behind Proposed Methods", "weight": 1.0} -->

The smaller the volume of $\mathcal{S}$, the less time will be spent sampling non-improving configurations. Ideally, the sampling space would be exactly the desired optimal path (i.e., $\mathcal{S} = \mathcal{P}_{opt}$). However, $\mathcal{P}_{opt}$ is not known in advance.

<!-- chunk {"id": "body-0013", "role": "body", "section": "The Motivation behind Proposed Methods", "weight": 1.0} -->

To reduce the number of samples that do not improve the solution, we propose several approaches to approximate the omniscient set $\mathcal{O}$, and we propose methods for their sampling.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Locally Informed Sampling Space", "weight": 1.0} -->

The first proposed sampling space is a modification of $\mathcal{S}_{i}$ of Informed-RRT\*. Instead of constructing a hyperellipsoid from the whole path, many smaller hyperellipsoids are constructed from various subsections of the path.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Locally Informed Sampling Space", "weight": 1.0} -->

$s_{j,k}$ constructed in this manner is guaranteed to contain the shortest path from $p_{j}$ to $p_{k}$ as proven in the original Informed-RRT\* paper, section III.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Locally Informed Sampling Space", "weight": 1.0} -->

With $\mathcal{S}_{l}$, the sampling approach of Informed-RRT\* gets applied to parts of the current shortest found path, as can be seen in Fig.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Locally Informed Sampling Space", "weight": 1.0} -->

The parameter $c$ controls the explore-exploit tradeoff. With the parameter $c = n$, sampling from $\mathcal{S}_{l}$ is equivalent to sampling from $\mathcal{S}_{i}$ (i.e., in the same manner as in the Informed-RRT\* planner). High values of $c$ lead to exploration, as the set $\mathcal{S}_{l}$ contains only the larger hyperellipsoids, and it supports the discovery of new alternative optimal solutions. In contrast, with the low values of $c$, the set $\mathcal{S}_{l}$ contains more small hyperellipsoids (computed from path subsections $\mathcal{P}_{j,k}$ of cardinality at least $c$), which leads to the exploitation of the current best solution (i.e., smoothing).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Locally Informed Sampling Space", "weight": 1.0} -->

Setting the parameter $c$ high (close to the $n$ of the initially found path) can lead to a premature halt of the smoothing and the use of $\mathcal{S}_{i}$ on a path not yet smoothed out.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Locally Informed Sampling Space", "weight": 1.0} -->

In the following subsection, we show how to efficiently sample $\mathcal{S}_{l}$ without explicitly constructing all the hyperellipsoids, which would be computationally very demanding.

<!-- chunk {"id": "body-0020", "role": "body", "section": "V-A Drawing random samples from $\\mathcal{S}_{l}$", "weight": 1.0} -->

To draw a random sample from $\mathcal{S}_{l}$, a random length of the subpath $\mathcal{P}_{j,k}$ is selected from range $\lbrack c,n\rbrack$, then the beginning of the path $j$ is selected randomly, the ellipsoid $s_{j,k}$ is constructed, and the random sample is generated from this ellipsoid (similarly, as Informed-RRT\* does). The random sampling of $\mathcal{S}_{l}$ is summarized in Alg. (we use symbol $U{(a,b)}$ for uniform sampling in the inverval $\lbrack a,b\rbrack$). This procedure is repeated for each new random sample.

<!-- chunk {"id": "body-0021", "role": "body", "section": "V-A Drawing random samples from $\\mathcal{S}_{l}$", "weight": 1.0} -->

Input: 𝒫: current best path; c: minimal length of the path segment
size ← U(c,|𝒫|) ∈ ℤ; // uniform interval sample
j ← U(1,|𝒫| − size) ∈ ℤ;\Hy@raisedlink\hyper@anchorstartAlgoLine0.1\hyper@anchorend
k ← j + size;\Hy@raisedlink\hyper@anchorstartAlgoLine0.2\hyper@anchorend
path ← (pj,…,pk); // selected segment of 𝒫
sample ← informed_sample(pj,pk,len(path)); // see, Sec. IV
return sample;\Hy@raisedlink\hyper@anchorstartAlgoLine0.3\hyper@anchorend
Algorithm 1 Local Informed Sampling

<!-- chunk {"id": "body-0022", "role": "body", "section": "Convex Sampling Space", "weight": 1.0} -->

The second proposed sampling space is obtained as a convex hull of revolution of $\mathcal{P}$ around the axis connecting $q_{start}$ and $q_{goal}$ (we refer to this axis as the SG-axis (start-goal-axis) in the rest of the paper) (Fig. 4a, 4b). We denote this sampling space as $\mathcal{S}_{c}$. Computing $\mathcal{S}_{c}$ of the rotated path (a convex hull of an infinite set) would be complicated and unnecessary. Since the resulting hull is axially symmetric along the SG-axis, we can utilize that knowledge to represent $\mathcal{S}_{c}$ by a two-dimensional slice.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Convex Sampling Space", "weight": 1.0} -->

We can define a "slice" of the convex hull, which is an intersection of $\mathcal{S}_{c}$ and a plane going through the SG-axis (Fig. 4c). Such a slice is two-dimensional, allowing us to represent $\mathcal{S}_{c}$ in 2D. A point inside the slice can be represented by the distance along the SG-axis and the distance from the axis to the point. Defining the slice and its coordinate system enables us to generate random points inside $\mathcal{S}_{c}$ by first drawing a random sample inside the slice and then distributing the sample into the volume of $\mathcal{S}_{c}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Convex Sampling Space", "weight": 1.0} -->

Let $A$ be the orthogonal projection matrix onto the SG-axis. For a configuration $q \in \mathcal{C}$, we define the distance along the SG-axis $a{(q)}$ and the distance from the axis $f{(q)}$ as

<!-- chunk {"id": "body-0025", "role": "body", "section": "VI-A Slice computation", "weight": 1.0} -->

We project each configuration $p_{i}$ of the path $\mathcal{P}$ onto the SG-axis using $A$ and denote the first and the last projected configurations $o$ and $t$, respectively (the projections are ordered by their scalar projection on the SG-axis, i.e., according to their distance $a{( \cdot )}$ along the axis). Note that ${transf{(o)}} = {}$. The coordinate system of the slice is depicted in Fig..

<!-- chunk {"id": "body-0026", "role": "body", "section": "VI-A Slice computation", "weight": 1.0} -->

Computation of the slice. Let $transf{({\mathcal{P} \cup {\{ o,t\}}})}$ denote a set of 2D points obtained by applying the transformation to each point of the path $\mathcal{P}$ and to the points $o$ and $t$. As all these points now lie on a 2D plane, we can compute their 2D convex hull and obtain the set of extremal points of the hull that we denote $V$. The points $v_{i} \in V$ then define the shape (polygon) of the slice, and the whole $\mathcal{S}_{c}$ would be achieved by rotating this polygon around the SG-axis. Computing the 2D convex hull of $m$ points (here, $m = {n + 2}$, i.e., number of waypoints plus two points $o$ and $t$) has time complexity $\mathcal{O}{({m{\log m}})}$. Practically, the method can be slightly sped up.

<!-- chunk {"id": "body-0027", "role": "body", "section": "VI-A Slice computation", "weight": 1.0} -->

Efficient computation of the slice. The efficient computation of the convex hull of the slice points is based on a modified Graham scan. Graham scan decides whether the point lies within the hull (and therefore can not be an extremal point) by checking whether three consecutive points form a right or a left turn.

<!-- chunk {"id": "body-0028", "role": "body", "section": "VI-A Slice computation", "weight": 1.0} -->

We modify the Graham scan using prior knowledge about the resulting hull of the set of points $V = {transf{({\mathcal{P} \cup {\{ o,t\}}})}}$. First, one edge of the convex hull is already known (it is the line segment $\overline{o,t}$). Second, all points are located only in one direction from this edge (all points of the slice have a positive $f{( \cdot )}$ value).

<!-- chunk {"id": "body-0029", "role": "body", "section": "VI-A Slice computation", "weight": 1.0} -->

With the mentioned constraints, we can simplify the Graham scan as follows. Let $V = {transf{({\mathcal{P} \cup {\{ o,t\}}})}}$ and we sort points in $V$ by their $a{( \cdot )}$ values. As the set $V$ is sorted, we can define the previous point $v_{p} \in V$ and the following point $v_{f} \in V$ for a given point $v \in V$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "VI-A Slice computation", "weight": 1.0} -->

We can use the already known distance from the known edge (the $f{( \cdot )}$ value) and omit from $V$ all such points $v$ that are located between the known edge (SG-axis) and the line segment $\overline{v_{p},v_{f}}$ since they lie inside the convex hull and can not be extremal. The algorithm for omitting non-extremal points of the two-dimensional convex hull is listed in Alg. and the process of deciding if a single point can be extremal is in Alg..

<!-- chunk {"id": "body-0031", "role": "body", "section": "VI-A Slice computation", "weight": 1.0} -->

Global params.: SG-axis
V ← sortV by scalar projection on SG-axis;\Hy@raisedlink\hyper@anchorstartAlgoLine0.1\hyper@anchorend
i ← 2; // start processing the first triplet
while True do if inside_hull(vi − 1,vi,vi + 1) then V ← V ∖ {vi}; // Not extremal
i ← 2; // go back to the start
continue;\Hy@raisedlink\hyper@anchorstartAlgoLine0.2\hyper@anchorend
if i = |V| − 1 then return V; \Hy@raisedlink\hyper@anchorstartAlgoLine0.3\hyper@anchorend
i ← i + 1;\Hy@raisedlink\hyper@anchorstartAlgoLine0.4\hyper@anchorend

<!-- chunk {"id": "body-0032", "role": "body", "section": "VI-A Slice computation", "weight": 1.0} -->

Global params.: qstart start configuration; qgoal goal configuration; SG-axis
l ← linesegmentfromvptovf;\Hy@raisedlink\hyper@anchorstartAlgoLine0.1\hyper@anchorend
SG ← linesegmentfromqstarttoqgoal;\Hy@raisedlink\hyper@anchorstartAlgoLine0.2\hyper@anchorend
if vquery is between SG and l then return True; // Inside
else return False; // Not inside

<!-- chunk {"id": "body-0033", "role": "body", "section": "VI-B Inlier query", "weight": 1.0} -->

To check if a configuration $q \in \mathcal{C}$ lies inside $\mathcal{S}_{c}$, we construct set $R = {{\{{transf{(q)}}\}} \cup V}$ and order the elements of $R$ by their scalar projection into the SG-axis (i.e., according to their distance $a{( \cdot )}$ along the axis). Then we proceed to find $v_{p} \in R$ and $v_{f} \in R$ for the query configuration $q$. With these points, we can use Alg. to decide whether $transf{(q)}$ lies inside the slice of $\mathcal{S}_{c}$. If $transf{(q)}$ lies inside the slice, then $q \in \mathcal{S}_{c}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "VI-C Drawing random samples from $\\mathcal{S}_{c}$", "weight": 1.0} -->

We can sample the set $\mathcal{S}_{c}$ either directly or with rejection sampling. The rejection sampling approach is simple to implement but less efficient for high dimensional $\mathcal{C}$ or if the volume of $\mathcal{S}_{c}$ is low (in comparison to the volume of the whole $\mathcal{C}$). Sampling $\mathcal{S}_{c}$ in higher dimensions (or when the volume of $\mathcal{S}_{c}$ is low) can be efficiently achieved using the direct sampling.

<!-- chunk {"id": "body-0035", "role": "body", "section": "VI-C Drawing random samples from $\\mathcal{S}_{c}$", "weight": 1.0} -->

Rejection Sampling of $\mathcal{S}_{c}$. Let $r \in \mathcal{C}$ be a random sample from $\mathcal{C}$, and $v^{\prime} = {transf{(r)}}$. We accept the sample $r$ as being in $\mathcal{S}_{c}$ if the point $v^{\prime}$ is located inside the 2D convex hull of the slice.

<!-- chunk {"id": "body-0036", "role": "body", "section": "VI-C Drawing random samples from $\\mathcal{S}_{c}$", "weight": 1.0} -->

Direct sampling of $\mathcal{S}_{c}$. First sample $a^{\prime}$ from interval $\lbrack 0,{\parallel{o - t}\parallel}\rbrack$ (see definitions in subsection VI-A), the sampling should be weighted by $f_{max}$ ($2f_{max}$ is the width of the slice of $\mathcal{S}_{c}$ for a given value of $a{( \cdot )}$) at each $a^{\prime}$. The sampled value of $a^{\prime}$ determines the maximal value $f_{max}$ that $f^{\prime}$ can obtain. Then, sample $f^{\prime}$ uniformly from the interval $\lbrack 0,f_{max}\rbrack$. This forms a random sample $g = {(a^{\prime},f^{\prime})}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "VI-C Drawing random samples from $\\mathcal{S}_{c}$", "weight": 1.0} -->

The random configuration $q \in \mathcal{C}$ is computed as: $q = {{a^{\prime}\overset{\rightarrow}{d}} + {f^{\prime}\overset{\rightarrow}{r}}}$, where $\overset{\rightarrow}{d}$ is a unit vector in direction from $q_{start}$ to $q_{goal}$, and $\overset{\rightarrow}{r}$ is a random unit vector perpendicular to $\overset{\rightarrow}{d}$. The reconstruction process is illustrated in Fig..

<!-- chunk {"id": "body-0038", "role": "body", "section": "Locally Informed Convex Sampling Space", "weight": 1.0} -->

The previously defined sampling spaces $\mathcal{S}_{l}$ and $\mathcal{S}_{c}$ can be combined; this leads to another sampling space $\mathcal{S}_{cl} = {\mathcal{S}_{l} \cap \mathcal{S}_{c}}$. While $\mathcal{S}_{c}$ will bring down the volume of the sampling space, $\mathcal{S}_{l}$ will put more weight on sampling in the proximity of the found path, locally smoothing out the fast converging solution. Example of the space $\mathcal{S}_{cl}$ is depicted in Fig..

<!-- chunk {"id": "body-0039", "role": "body", "section": "VII-A Drawing random samples from $\\mathcal{S}_{cl}$", "weight": 1.0} -->

To draw a random sample from $\mathcal{S}_{cl}$, first a random sample is generated in $\mathcal{S}_{l}$ (which is described in section V-A), and the sample is accepted only if it is also located in $\mathcal{S}_{c}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Discussion", "weight": 1.5} -->

The proposed approximations of the omniscient set and methods for their sampling can be integrated into any RRT\*-based planner (instead of drawing random samples from the whole $\mathcal{C}$, the planner draws random samples from $\mathcal{S}_{l}$, $\mathcal{S}_{c}$ or $\mathcal{S}_{cl}$). Similarly to Informed-RRT\*, where the set $\mathcal{S}_{i}$ is updated when a new (shorter) path is found, the proposed sets $\mathcal{S}_{l}$, $\mathcal{S}_{c}$, and $\mathcal{S}_{cl}$ can be updated every time a new path is found.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Discussion", "weight": 1.5} -->

Sampling from $\mathcal{S}_{l}$ (Section V-A) is computationally not demanding. It only requires selecting a subsection of the current best solution and defining the hyperellipsoid using its first and last configurations. Therefore, sampling from $\mathcal{S}_{l}$ has the same complexity $\mathcal{O}{}$ as sampling in Informed-RRT\*.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Discussion", "weight": 1.5} -->

Drawing random samples from $\mathcal{S}_{c}$ (and also from $\mathcal{S}_{cl}$) is computationally more demanding. Every time a new solution is found, it is required to apply transformation in Eq. to all points of the current best solution $\mathcal{P}$ and to compute the convex hull as described in section VI-C. The time complexity of the convex hull computation is $\mathcal{O}{({n{\log n}})}$ for a path $\mathcal{P}$ with $n$ waypoints. More frequent hull reconstruction will result in a faster decrease of $\mathcal{S}_{c}$ volume. However, reconstructing the hull too often can slow down the planning, without much improving the convergence. We observed that it is not necessary to construct $\mathcal{S}_{c}$ every time the current best solution is improved, but it is satisfactory to update it in every $m$ iterations (in our experiments, we used $m = {1,000}$).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Discussion", "weight": 1.5} -->

The locally informed sampling space $\mathcal{S}_{l}$ enables more frequent sampling close to the current best-known path. The planners using $\mathcal{S}_{l}$ tend to have a faster convergence rate than ones using $\mathcal{S}_{c}$ in environments where less topologically distinct paths are present (for example, the Hard, Comb, and 3Dcomb environments) and slower in the opposite case. The $\mathcal{S}_{cl}$ can be used as a compromise when there is not enough information about the environment. Sampling from $\mathcal{S}_{l}$ preserves asymptotic optimality.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Discussion", "weight": 1.5} -->

Proof: The equation is satisfied by all subpaths of cardinality from the interval $\lbrack c,n\rbrack$. Therefore, there are ${n - c} + 1$ possible cardinalities of subpaths, including the whole path with the cardinality $n$. When generating a random sample from $\mathcal{S}_{l}$, we first randomly (uniformly) select a cardinality from the interval $\lbrack c,n\rbrack$. Therefore, with the probability $\frac{1}{{n - c} + 1}$, we select the subpath of the cardinality $n$. The hyperellipsoid defined by $\mathcal{P}$ is $\mathcal{S}_{i}$. Therefore, when sampling from $\mathcal{S}_{l}$, we sample from $\mathcal{S}_{i}$ with probability $\frac{1}{{n - c} + 1}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Discussion", "weight": 1.5} -->

In section III, it was proven that sampling of $\mathcal{S}_{i}$ leads to asymptotically optimal planning. Since sampling of $\mathcal{S}_{i}$ guarantees asymptotic optimality and we perform it with nonzero probability, sampling of $\mathcal{S}_{l}$ also guarantees asymptotic optimality. $\blacksquare$

<!-- chunk {"id": "body-0046", "role": "body", "section": "Discussion", "weight": 1.5} -->

On the contrary, the spaces $\mathcal{S}_{c}$ and $\mathcal{S}_{cl}$ do not guarantee to fully cover the omniscient set as $\mathcal{S}_{i}$ and $\mathcal{S}_{l}$ do, and drawing random samples only from these would result in a planner that does not ensure asymptotic optimality. Therefore, to ensure asymptotic optimality when using $\mathcal{S}_{c}$ or $\mathcal{S}_{cl}$, random samples should also be generated from $\mathcal{S}_{i}$ with a non-zero probability. This is an often adopted trick that combines Informed-RRT\* (which samples from $\mathcal{S}_{i}$) with other methods because the combination preserves asymptotic optimality.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

The proposed approximations of the omniscient set (and their sampling) were implemented and integrated in state-of-the-art planners. A method with the prefix 'PI-' (partially informed) generates the random samples from $\mathcal{S}_{l}$ (Section V-A), the prefix 'C-' (convex) denotes sampling from the convex hull $\mathcal{S}_{c}$ (Section VI-C), and finally, the prefix 'PIC-' (partially informed convex) denotes the combination of 'PI-' and 'C-' methods $\mathcal{S}_{cl}$ (the procedure of generating the samples for 'PIC-' planners is described in VII-A). We integrated our approaches into RRT\* and BIT\* methods (e.g., PI-RRT\* is the RRT\* planner that generates the samples from $\mathcal{S}_{l}$).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

The methods were tested on path planning for a rectangle object in four 2D environments (Comb, Hard, Wall, Maze) of size $500 \times 500$, i.e., in 3D configuration space as the robot can translate and rotate. The size of the object is $10 \times 10$ units in Comb, Wall, and Maze environments. The Hard environment (Fig. 10b) was designed specifically to pose a challenge to methods utilizing $\mathcal{S}_{c}$. In this case, the robot size is $50 \times 50$, and the environment contains two distinct homotopy classes: one is the bottom 'zig-zag' path, and the other one is the top path. When the convex set $\mathcal{S}_{c}$ is computed from either path, it will not fully cover the other path. Therefore, the 'C-' planners should have a worse average performance in this case.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

(a) Planner stuck in the upper homotopy class

<!-- chunk {"id": "body-0050", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

(b) Planner stuck in the lower homotopy class

<!-- chunk {"id": "body-0051", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

We also tested the performance in two 3D environments: Random (size $215 \times 215 \times 215)$, which is cluttered with many random obstacles, and 3D Comb (size $110 \times 160 \times 160$) containing walls. Planning was realized for a cubic robot of size ($10 \times 10 \times 10$). The 3D environments are depicted in Fig.. As the robot can rotate and translate in 3D, the path planning leads to a search in 6D configuration space.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

We compared our planners (PI-RRT\*, C-RRT\*, PIC-RRT\*, PI-BIT\*, C-BIT\*, PIC-BIT\*) with state-of-the-art asymptotically optimal path planners from the OMPL benchmark: Informed-RRT\*, RRT\*, RRTX, RRT#. Despite OMPL also containing the BIT\* planner, we did not use it due to its poor performance. Therefore, we used our implementation of BIT\* (with batch size 1,000) for the comparison. We run each planner for $10^{5}$ iterations. In the case of 'PI-' planners, the random samples are drawn solely from the set $\mathcal{S}_{l}$, as this set ensures asymptotical optimality.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

In the case of planners with 'C-' and 'PIC-' prefix (i.e., drawing random samples from $\mathcal{S}_{c}$ and $\mathcal{S}_{cl}$, respectively), we also generated random samples from $\mathcal{S}_{i}$ with the the probability $10^{- 5}$. Each planner was run 100 times in each planning scenario. The parameter $c$ was set to $5$, and goal region $Q_{goal}$ was represented by a box of size $10$ units in 3D environments and of size $5$ units in 2D environments, respectively.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

The convergence graph in Fig. shows the performance of the state-of-the-art planners and our planner PIC-RRT\* in the Random 3D environment. For visibility reasons, we omitted the curves of our other planners from the graph. From the tested planner, PIC-RRT\* achieved the fastest convergence to the optimal solution.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

The results achieved in the 6D configuration space are summarized in Tab. I. The table shows the average path length (column 'Avg'), standard deviation (column 'Std'), and median absolute deviation (column 'Mad'). The proposed methods (the upper part of the table) found shorter paths at the given time (ten seconds of computation).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

The performance (the convergence towards the optimal solution) of the planners in the Hard 2D environment is depicted in Fig.. The graph shows convergence curves for state-of-the-art planners and for our PI-RRT\* planner. We omitted our other planners ('PI-' and 'PIC-') from this graph due to visibility.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

The length of the paths found by the tested planners in 2D environments is summarized in Tab. II. The table shows the path length after six seconds of runtime (after this time, most of the planners do not improve their path length). The best average path lengths (shown in boldface in the table) were found by the proposed methods. In the tested environments, the start and goal can be connected using topologically distinct paths. In such cases, the first path found by the sampling-based planners may be different in each trial, and it may take a longer time to converge to the optimal one. This is indicated by the high standard deviation, especially for Maze and Wall environments, which contain many possible ways to connect the start and goal. Yet, our planners showed a smaller standard deviation in finding paths than the other methods. The progress of PI-RRT\* and C-RRT\* is visualized in Fig..

<!-- chunk {"id": "body-0058", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

In comparison to state-of-the-art planners, the C-RRT\* and C-BIT\* planners had the worst relative performance in the Hard environment, as expected. However, in other environments, sampling in the space $\mathcal{S}_{c}$ (C-RRT\* and C-BIT\*) enabled to find better paths than were found by other state-of-the-art planners.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

In all tested 2D and 3D environments, the proposed methods outperformed the state-of-the-art planners: they have a faster rate of convergence and provide shorter paths.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The well-known issue of asymptotically optimal path planning using RRT\* is its slow convergence towards the optimal path. In this paper, we have proposed novel methods to approximate the omniscient set, i.e., the subset of the configuration space that is known to contain samples that can improve the quality of the path. The first proposed approach uses multiple hyperellipsoids that are defined by a subsection of the current best path. In the second approach, we construct a convex hull of the current best path. We describe how to sample these spaces. The proposed methods can be integrated into any RRT\*-based planner. The experiments show the superior performance of our methods in comparison to the state-of-the-art planners from the OMPL benchmark.
