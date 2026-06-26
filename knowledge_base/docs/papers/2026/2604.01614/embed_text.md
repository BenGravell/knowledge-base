## Introduction

Feedback motion planning synthesizes a vector field over ${\cal C}_{free}$, the collision-free subspace of the configuration space. This creates a closed-loop policy that robustly guides a robot to its goal from almost any admissible state, an essential feature for real-world applications. The framework introduced by Lindemann et al. provides a powerful method for generating such feedback plans by decomposing the space into cells and blending local vector fields. This approach constructs almost globally defined, ${C^{\infty}}$-smooth feedback laws that guarantee convergence and collision avoidance, nicely sidestepping the local minima that plague artificial potential fields and the high computational cost of global methods such as harmonic functions.

The primary limitation of Lindemann et al. is that it lacks the ability to assign local vector fields in a way that generates higher-quality paths. The default assignments of local cell and face vectors, while satisfying theoretical convergence criteria, can produce integral curves with unnecessary bending, particularly when moving between cells. These inefficient paths lead to longer travel times, higher energy consumption, and increased control effort, diminishing the practical utility of the feedback law.

This work presents a computationally efficient solution to this problem by systematically assigning local vector fields to produce more direct trajectories. We introduce a simple and efficient heuristic for aligning cell vector fields; by propagating a desired global direction of motion backward from the goal, our method systematically biases local vector fields to produce more direct integral curves. This is enhanced by the face-vector averaging technique that smooths transitions between cells, directly reducing path bending. Furthermore, we develop a novel geometric algorithm to construct a maximal star-shaped chain of simplexes around the goal, creating a large, geometrically verified "funnel" where a direct-to-goal control law can be safely applied for optimal, straight-line convergence. Demonstrations in maze, bug trap, and sparse environments show that our method generates qualitatively superior feedback laws, with trajectories exhibiting measurably lower total bending and reduced control effort compared to the baseline, all while preserving the foundational guarantees of smoothness and global convergence. Although simulations are demonstrated in two dimensions based on Constrained Delaunay Triangulation (CDT), the algorithm applies to any simplicial complex embedded in ${\cal C}_{free}$. While obtaining such complexes in higher dimensions is challenging, it is a tractable problem for 2D/3D configuration or workspace.

## Related Work

Our work is based on established methods in feedback motion planning and computational geometry. We situate our contributions in relation to these key areas: classical potential-based methods, feedback laws on cell decompositions, and modern optimization-based and region-based planning.

### II-A Potential Fields, Navigation and Harmonic Functions

Artificial Potential Fields (APFs) offer a fast and reactive feedback policy, but suffer from local minima, oscillation, and poor performance in narrow passages. Therefore, enhancements have been proposed to mitigate these issues. Navigation Functions (NFs) are a special class of smooth APFs that ensure global convergence to a goal without local minima under certain assumptions. NFs have been extended to more general geometries or for non-holonomic and multiple robots. However, they are practically challenging to implement, especially in environments with complex obstacle geometries. Harmonic functions also overcome local minima by solving Laplace's equation over the free space. However, the computational cost of solving partial differential equations (PDEs) restricts their use in real-time or high-dimensional applications.

### II-B Feedback from Cell Decompositions and Bump Functions

To overcome the limitations of global potential functions, Lindemann et al. proposed constructing local vector fields over a convex cell decomposition. In this framework, local vector fields are blended using smooth bump functions to create a feedback law with guaranteed convergence. While this approach is general and has been extended to shaped robots and nonholonomic systems, the assignment of the local vector fields to reduce path bending remains a critical open challenge that this paper addresses. Bump function blends have also been used to compose attractive/repulsive fields with strong safety guarantees.

### II-C Region-Based and Optimization-Based Planning

In sampling-based methods such as RRT\*, post-processing techniques such as B-spline or shortcutting are common to improve path quality. While these operate on a single path, our method, by construction, generates a ${C^{\infty}}$-smooth vector field and therefore integral curves. Advanced optimization-based methods, such as the Graph of Convex Sets (GCS) and Fast Path Planning (FPP), find smooth and high-quality paths by solving mathematical programs over convex decompositions. In contrast, our geometric approach avoids expensive optimization, constructing a smooth, computationally efficient feedback law over $\mathcal{C}_{free}$. Tedrake et al. developed the LQR-Trees framework, where stabilizing controllers are verified using sum-of-squares optimization to produce funnel-shaped regions of attraction around sampled trajectories. Later work by Reist et al. replaced the verification process with a simulation-based expansion, broadening the range of applicable systems. While these methods are powerful and optimal, they rely on computationally intensive procedures like sums-of-squares or semidefinite programming to derive regions of attraction.

In motion planning, identifying large subsets of free space where simple control laws can safely guide the robot is a key strategy. A well-established method is to compute convex regions, either through exact decomposition or iterative expansion. For example, the IRIS algorithm expands large convex polytopes via alternating semidefinite and quadratic programs.

Other works have explored maximum convex region extraction in triangulated spaces, where convex unions of adjacent triangles are found via dynamic programming. Although convexity simplifies controller design, it is often restrictive. This motivates using star-shaped regions, which we construct geometrically, avoiding dynamics-based verification.

Our geometric construction of a maximal star-shaped region is conceptually similar to the "Triangular Expansion" algorithm used for computing visibility polygons, as both recursively explore adjacent triangles. However, a key difference lies in our objective. Instead of computing the exact boundary of the visibility polygon, our goal is simply to find the maximal set of simplexes that form a star-shaped region relative to the goal. This simpler objective allows for a more efficient visibility check that generalizes naturally to higher dimensions.

## Problem Formulation

We consider the motion planning problem for a robot navigating in a workspace $W\subset\mathbb{R}^{n}$ (where $n\in\{2,3\}$) with static obstacles $\mathcal{O}$. The robot's configuration is a point in its $d$-dimensional configuration space, ${\cal C}$, and all motion is restricted to the open collision-free subset, ${\cal C}_{free}$.

The task is to design a ${C^{\infty}}$-smooth vector field $V$ over ${\cal C}_{free}$ whose integral curves are guaranteed to converge to $x_{g}\in{\cal C}_{free}$ without collision. We note that $V$ is well-defined and smooth almost everywhere, except on a set of measure zero (the ($d-2$)-dimensional boundaries of the cell faces, e.g., vertices in 2D) which the integral curves never traverse. To manage geometric complexity, a simplicial complex composed of a finite number of non-degenerate $d$-simplexes, $\mathcal{T}=\{\Delta_{1},...,\Delta_{N}\}$, is embedded in ${\cal C}_{free}$. In this paper's simulations, we use a point robot in 2D; hence, ${\cal C}=W\subset\mathbb{R}^{2}$ and obstacles are polygonal, and by employing CDT, we ensure that every $2$-simplex is non-degenerate.

We compute a discrete plan on $\mathcal{T}$ (with vertices at simplex centroids and edges connecting adjacent simplexes) by finding a shortest-path tree to the goal simplex $\Delta_{g}$ containing $x_{g}$. This provides a successor mapping, $s(i)$, for each simplex $\Delta_{i}\in\mathcal{T}$ that guides the robot toward the goal.

The global vector field is constructed from two local components for each simplex $\Delta_{i}$: 1) a single, constant cell vector field, $V_{c,i}$, respecting successor mapping, $s(i)$, and 2) a set of face vector fields, $\{V_{f}\}$, defined on the boundary faces of the simplex. The final vector field $V(x)$ at any point $x\in\Delta_{i}$ is a smooth, weighted combination of $V_{c,i}$ and the vector field of the closest face, following the blending method .

To further improve efficiency, we identify a maximal star-shaped chain of simplexes $\mathcal{C}_{g}\subseteq\mathcal{T}$ around the goal that forms a star-shaped region $R_{g}=\bigcup_{\Delta\in\mathcal{C}_{g}}\Delta$. A set $R$ is star-shaped with respect to $x_{g}\in R$ if for every $x\in R$, the line segment that connects $x$ and $x_{g}$ is contained in $R$. Within this "funnel" region $R_{g}$, the control law is simplified: the cell vector field $V_{c,i}$ for every $\Delta_{i}\in\mathcal{C}_{g}$ is set to point directly toward the goal $V_{c,i}(x)=\text{normalize}(x_{g}-x)$, where $\text{normalize}(v)=v/\|v\|$ for any non-zero vector $v$.

## Smooth Feedback on Simplicial Decompositions

Our approach is based on the framework of for simplicial decomposition. The method involves computing a global vector field from local vector fields defined on individual cells and their faces, ensuring smoothness, collision avoidance, and global convergence to a designated goal state.

To precisely describe our method, we first recall several essential definitions and theorems .

### IV-A Fundamental Definitions

To obtain smooth interpolation between local vector fields, we use a special class of smooth functions $b(\sigma)$, called bump functions, understood here as ${C^{\infty}}$ functions that provide a smooth transition between 0 and 1.

### Definition 1

The function $b:\mathbb{R}\to$ is a ${C^{\infty}}$ smooth function defined as: where the auxiliary function $\lambda(\sigma)$ is defined as: with the property that all derivatives of $\lambda(\sigma)$ are zero at the endpoints ($\sigma=0$ and $\sigma=1$) and therefore any derivative of $b(\sigma)$ is zero at these endpoints.

To guide the robot through the cell, we define a cell vector that guarantees reaching the exit face (a shared face between the current cell and its successor cell). To formally define the region of influence for each ($d-1$)-dimensional face, we refer to the Generalized Voronoi Diagram (GVD). Within a convex set, the GVD is the set of all points equidistant to at least two faces, which divides the cell into distinct regions of influence for each face.

### Definition 2

For a convex cell $\Delta_{i}$ with an exit face $f_{\text{exit},i}$, a cell vector field $V_{c,i}$ is a smooth unit vector field on $\Delta_{i}$ that satisfies three conditions: For each point $x\in\Delta_{i}$, there exists $y\in f_{\text{exit},i}$ and $\alpha\in\mathbb{R}$ such that $V_{c,i}(x)=\alpha(y-x)$.

Let $h$ be a GVD face with normal vector $n$. If $V_{c,i}(x)\cdot n=0$ for some $x\in h$, then $V_{c,i}(x)\cdot n=0$ for all $x\in h$.

The directed transition graph induced by this choice of vector fields is acyclic, and every path through this graph terminates at the node corresponding to the exit face.

To ensure that the robot crosses the exit face and avoids collisions with obstacles, we define face vector fields.

### Definition 3

A face vector field $V_{f}$ corresponding to a face $f$ of a cell $\Delta_{i}$ is a smooth unit vector field satisfying: For each point $p\in f$, the vector field $V_{f}(p)$ satisfies $V_{f}(p)\cdot n>0$, where $n$ is the inward-pointing normal vector for $f\in F_{i}\setminus\{f_{\text{exit},i}\}$, and outward-pointing normal vector for $f=f_{\text{exit},i}$.

For each non-exit face $f\in F_{i}\setminus\{f_{\text{exit},i}\}$, let $b_{f}$ denote the hyperplane equidistant from $f$ and $f_{\text{exit},i}$ with unit normal $n_{b_{f}}$ oriented such that $n_{b_{f}}\cdot n_{x}>0$, where $n_{x}$ is the outward normal of $f_{\text{exit},i}$. Then $V_{f}(p)\cdot n_{b_{f}}>0$ holds for every $p$ in the closure of the region of influence of $f$.

### IV-B Essential Theorems

The framework of provides the following guarantees, which our method inherits (detailed proofs of these theorems can be found there):

### Theorem 1

All integral curves generated by the smoothly interpolated cell and face vector fields within any intermediate cell reach the designated exit face of that cell in finite time.

### Theorem 2

All integral curves within the goal cell asymptotically converge to the designated goal point.

### Theorem 3

The integral curves defined over the entire decomposed cells asymptotically converge to the goal state from any initial state located within the decomposed cells.

### Theorem 4

The integral curves generated by the combined local vector fields remain $C^{\infty}$-smooth throughout the entire domain, including across the GVD surface within each cell and face boundaries.

While the general framework allows for vector fields converging to a specific point, we utilize constant cell vector fields for simplicity and uniformity. This choice prevents trajectories from bunching together around the designated point, such as the exit face centroid, and simplifies the alignment process. In our method, we impose boundary constraints (boundary vectors) for the constant cell vector fields. Each $d$-simplex has $d+1$ vertices, and each $(d-1)$-dimensional face has $d$ vertices corresponding to it, meaning that for each $(d-1)$-dimensional face, there exists one opposite vertex. Therefore, when selecting an exit face for the cell, a corresponding opposite vertex exists (Let us call it $v_{ov}$). We define boundary vectors that connect this $v_{ov}$ vertex to each of the vertices of the exit face. The cell vector field must be chosen within the wedge defined by these $d$ boundary vectors (for $d$-simplex). Geometrically, this results in a conical region oriented toward the exit face. Constraining the constant vector field to this conical region is sufficient to guarantee the validity conditions of Definition 2.

### Theorem 5

A constant cell vector field $V_{c,i}$ that is chosen to point within the conical region defined by the boundary vectors satisfies the conditions of Definition 2.

### Proof

Let $\mathcal{K}_{i}$ be the conical region. Any constant vector $V_{c,i}$ within $\mathcal{K}_{i}$ can be expressed as a positive linear combination of the boundary vectors. Every boundary vector $b_{i,j}$ points from the opposite vertex $v_{ov,i}$ towards a point on the exit face $f_{\text{exit},i}$. Therefore, any positive linear combination of these vectors, and thus $V_{c,i}$, will point towards $f_{\text{exit},i}$. Let $h$ be a face of the GVD with a constant normal vector $n$. The dot product is $V_{c,i}\cdot n$. Since both $V_{c,i}$ and $n$ are constant vectors, their dot product is a constant value everywhere. Therefore, if $V_{c,i}\cdot n=0$ for some point on $h$, it is zero for all points on $h$. Since $V_{c,i}$ points towards the exit face, any trajectory starting in $\Delta_{i}$ will proceed monotonically toward $f_{\text{exit},i}$ and is guaranteed to intersect it. The path cannot curve back on itself or form a cycle. This ensures that the induced graph of the transitions is acyclic. ∎ Hence, selecting a constant vector field within this conical region guarantees its validity under the framework of.

## Heuristic Vector Field Alignment Method

Arbitrary vector field assignments, even those satisfying Theorem 5, can lead to unnecessary bending in integral curves. To mitigate this, we introduce a heuristic alignment strategy that adjusts each cell vector field to better align with the vector field of its successor(s), producing more direct trajectories.

### V-A Heuristic Alignment of Cell Vector Fields

First, we establish a global plan. Let $x_{g}$ be the goal point, and let $\Delta_{g}$ be the goal simplex. For each simplex $\Delta_{i}$, let $c_{i}$ be its centroid. We compute the shortest-path tree rooted at $\Delta_{g}$ on the connectivity graph, which provides a successor $s(i)$ and a hop-distance $l(i)$ (i.e., the minimum number of simplex transitions required to reach the goal simplex $\Delta_{g}$) for each simplex $\Delta_{i}$. For each non-goal cell $\Delta_{i}$, we identify its exit face $f_{\text{exit},i}$ and the corresponding opposite vertex $v_{ov,i}$, as illustrated in Figure 1.

Figure 1: Geometric construction of valid vector fields for 2-simplex (triangle). The conical region, constructed by boundary vectors bi, j, illustrates the set of valid constant cell vector fields Vc, i that satisfy the conditions of Definition 2. The diagram visualizes the geometric constraints for face vector fields (Definition 3), showing the face inward normal nin, f, the exit face outward normal nx, and the hyperplane normal nbf. The dashed lines are the GVD surface.

The core of our heuristic is to process cells in order of increasing hop-distance from the goal, propagating a desired direction backward. For each non-goal cell $\Delta_{i}$, we first define its $d$ unit boundary vectors $\{b_{i,j}\}$ which form its conical region $\mathcal{K}_{i}$: in which $p_{v_{j}}$ are the coordinates of the vertices of the exit face $f_{\text{exit},i}$. We then assign the cell vector field $V_{c,i}$ as Algorithm 1.

1:Set of simplexes 𝒯, goal point xg. 2:Cell vector field Vc, i for all Δi ∈ 𝒯. 3:Compute centroids ci, graph G, successors s(i), and hop-distances l(i) for all Δi. 4:for each non-goal simplex Δi in ascending order of l(i) do 5: Let {bi, j} be the set of boundary vectors forming the conical region 𝒦i. 12: if vcand, i is not in the conical region 𝒦i then 13: Find bi, j* that minimizes the angle with vcand, i. Algorithm 1 Heuristic Alignment of Cell Vector Fields To formally check if a candidate vector $v_{\text{cand},i}$ lies within the conical region formed by the basis vectors $\{b_{i,j}\}$, we must determine if it can be expressed as a non-negative linear combination of them. This can be formulated as a standard linear programming (LP) feasibility problem, where we seek to find coefficients $\alpha_{j}\geq 0$ such that: If a solution for $\{\alpha_{j}\}$ exists, the vector is inside the conical region. If this feasibility problem has no solution, the candidate vector lies outside the cone. In this case, we project it to the closest boundary vector (the one minimizing the angle), a computationally simple choice that guarantees the vector remains within the valid conical region. While this requires solving a small LP for each simplex, the problem is computationally inexpensive as the number of variables ($d$) equals the dimension of the space. This check is efficient enough for precomputation and does not impede the real-time evaluation of the feedback law.

Although it does not guarantee a globally optimal path, in practice, it yields significantly straighter and more uniform trajectories compared to unaligned cell fields. The effectiveness of the alignment heuristic extends beyond local smoothing. The heuristic encourages consecutive cell vector fields, $V_{c,i}$ and $V_{c,s(i)}$, to adopt a similar direction. By then defining the exit face vector field as the average of these two vectors, our method naturally creates conditions where adjacent cells with a coherent flow functionally merge. This process forms larger regions of consistent flow, guiding the robot along globally straighter paths.

### V-B Assignment of Face Vector Fields and Proof of Validity

For each non-exit face $f\in F_{i}\setminus\{f_{\text{exit},i}\}$, we modify the standard inward-pointing normal to better align with the cell's flow. The face vector $V_{f}$ is defined as the normalized sum of the face's inward-pointing unit normal, $n_{\text{in},f}$, and the cell's own vector field, $V_{c,i}$: For the unique exit face $f_{\text{exit},i}$, we average the cell vectors of the current cell $\Delta_{i}$ and its successor $\Delta_{j}$ (where $j=s(i)$) to promote a smooth passage between cells: We must ensure these assignments satisfy Definition 3, guaranteeing the robot exits strictly through the exit face.

### Proposition 1

The modified non-exit face vector field $V_{f}=\mathrm{normalize}(n_{\text{in},f}+V_{c,i})$ satisfies the conditions of Definition 3 for a non-exit face.

### Proof

First, we show $V_{f}\cdot n_{\text{in},f}>0$. The dot product of the unnormalized sum, $(n_{\text{in},f}+V_{c,i})\cdot n_{\text{in},f}$, expands to $1+(V_{c,i}\cdot n_{\text{in},f})$ since $n_{\text{in},f}$ is a unit vector. As $V_{c,i}$ points toward the exit face restricted to be within its conical region, its dot product with the inward normal of any other face is non-negative ($V_{c,i}\cdot n_{\text{in},f}\geq 0$). The entire expression is therefore $\geq 1$, satisfying the first condition. Since the dot product is strictly positive, the vector sum $(n_{\text{in},f}+V_{c,i})$ cannot be the zero vector, and thus the normalization is always well-defined.

Second, we must show $V_{f}\cdot n_{b_{f}}>0$, where $n_{b_{f}}=n_{x}+n_{\text{in},f}$ is the normal to the equidistant hyperplane. We prove that $(n_{\text{in},f}+V_{c,i})\cdot n_{b_{f}}>0$ by analyzing two components: 1) The cell vector component, $V_{c,i}\cdot n_{b_{f}}$, which expands to $(V_{c,i}\cdot n_{x})+(V_{c,i}\cdot n_{\text{in},f})$. The first term, $V_{c,i}\cdot n_{x}$, is strictly positive because the conical region for $V_{c,i}$ is oriented toward the exit face. The second term, $V_{c,i}\cdot n_{\text{in},f}$, is non-negative because $V_{c,i}$ does not point into any non-exit faces. The sum of a strictly positive and a non-negative term is therefore strictly positive. 2) The geometric component is $n_{\text{in},f}\cdot n_{b_{f}}=(n_{\text{in},f}\cdot n_{x})+(n_{\text{in},f}\cdot n_{\text{in},f})$. Since $n_{\text{in},f}$ is a unit vector, this simplifies to $(n_{\text{in},f}\cdot n_{x})+1$. For any two distinct faces of a simplex, their respective inward and outward unit normals cannot be anti-parallel, meaning their dot product is strictly greater than $-1$. This guarantees the term is strictly positive. The sum of these two strictly positive components is therefore strictly positive, and the proposition holds. ∎

### Proposition 2

The averaged exit face vector field $V_{f}(f_{\text{exit},i})=\mathrm{normalize}(V_{c,i}+V_{c,j})$ satisfies the conditions of Definition 3 for an exit face.

### Proof

We show that $V_{f}(f_{\text{exit},i})\cdot n_{x}>0$. As established in the proof of Proposition 1, since $V_{c,i}$ is chosen from its conical region $\mathcal{K}_{i}$, it is guaranteed that $V_{c,i}\cdot n_{x}>0$. Now consider the successor's cell vector, $V_{c,j}$. This vector is chosen to be within the conical region $\mathcal{K}_{j}$ of cell $\Delta_{j}$, which points towards its own exit face, $f_{\text{exit},j}$. This only guarantees that $V_{c,j}$ points away from its entrance face ($f_{\text{exit},i}$). Therefore, its component along $n_{x}$ is non-negative: $V_{c,j}\cdot n_{x}\geq 0$. The dot product of the sum is $(V_{c,i}+V_{c,j})\cdot n_{x}=(V_{c,i}\cdot n_{x})+(V_{c,j}\cdot n_{x})$. The sum of a strictly positive and a non-negative term is strictly positive, satisfying the condition. ∎

### V-C Blending the Vector Fields

Finally, within each cell $\Delta_{i}$, a single smooth vector field $V(x)$ is synthesized by interpolating between the cell vector $V_{c,i}$ and the vector of the closest face.

For any point $x\in\Delta_{i}$, we first identify its closest face, $f^{*}\in F_{i}$, by computing the perpendicular distance $d(x,f)$ to every face $f$ of the cell. The region of influence of $f^{*}$ (its Voronoi region) consists of all points for which $f^{*}$ is the closest face.

Within this region, we use the smooth bump function $b(\sigma)$ from Definition 1. The parameter $\sigma\in$ must be 0 on the face $f^{*}$ and 1 on the GVD surface (the boundary of the region of influence). The formula to achieve this is: Let $V_{f^{*}}$ be the face vector for the closest face $f^{*}$. The final vector field at point $x$ is the normalized, weighted average: This construction guarantees that the vector field is identical to the face vector on the cell boundary, ensuring continuity across cells, and smoothly transitions to the cell vector field toward the interior of the cell.

## Constructing the Maximal Star-shaped Chain of Simplexes

To create more direct trajectories, we identify a large funnel where the robot can safely bypass conservative cell-by-cell transitions. While standard algorithms can compute the exact visibility polytope, they are often computationally intensive as they must construct a precise geometric boundary. Our simplex-based expansion is therefore chosen for its efficiency and simplicity; it relies on a series of simple local visibility tests to incrementally grow the funnel. We acknowledge that this construction is conservative and the resulting region $\mathcal{R}_{g}$ is strictly contained within the true visibility polytope of the goal. The expansion is sensitive to the simplicial complex; for example, Steiner points introduced for mesh quality can prevent the chain expansion even where a simplex is completely visible to the goal. However, this approach is sufficient for our purpose and naturally extends to higher dimensions.

### VI-A Geometric Criteria for Star-shaped

Our method incrementally grows a star-shaped region, $\mathcal{R}_{g}$, starting from the goal simplex, $\Delta_{g}$. Consider a region $\mathcal{R}\subset\mathbb{R}^{d}$ known to be star-shaped with respect to $x_{g}$. We wish to add an adjacent $d$-simplex, $\Delta_{T}$, which shares a $(d-1)$-dimensional face $\mathcal{S}$ with $\mathcal{R}$'s boundary. The union $\mathcal{R}\cup\Delta_{T}$ remains star-shaped if the new vertex of $\Delta_{T}$ not on $\mathcal{S}$, denoted $v_{\text{new}}$, is visible from $x_{g}$. See Figure 2 for an illustration. We propose two equivalent geometric criteria for this test.

### Criterion 1 (Visibility Cone from Goal)

A visibility cone is formed at the goal $x_{g}$ by the vectors pointing from $x_{g}$ to the vertices of the shared face $\mathcal{S}$. The region $\mathcal{R}\cup\Delta_{T}$ is star-shaped if the vector $v_{\text{new}}-x_{g}$ lies strictly inside this cone.

### Theorem 6

Criterion 1. ‣ VI-A Geometric Criteria for Star-shaped ‣ VI Constructing the Maximal Star-shaped Chain of Simplexes ‣ Smooth Feedback Motion Planning with Reduced Curvature") guarantees preservation of the star-shaped property.

### Proof

Assume vector $v_{\text{new}}-x_{g}$ lies strictly within the visibility cone at $x_{g}$ formed by the vertices of face $\mathcal{S}$. The segment $[x_{g},v_{\text{new}}]$ is, by definition, contained within this cone. Because region $\mathcal{R}$ is star-shaped, no other boundaries of $\mathcal{R}$ can obstruct this cone. The segment $[x_{g},v_{\text{new}}]$ therefore passes unobstructed into $\Delta_{T}$. By convexity of $\Delta_{T}$, all segments from $x_{g}$ to any interior point of $\Delta_{T}$ remain fully within the extended region. Thus, $\mathcal{R}\cup\Delta_{T}$ is star-shaped. ∎ Similar to the check in Section V-A, this geometric condition can be formulated as a computationally inexpensive LP feasibility problem. We seek to determine if $v_{\text{new}}-x_{g}$ can be expressed as a non-negative linear combination of the vectors forming the visibility cone.

Figure 2: Geometric test for expanding the star-shaped region ℛ with an adjacent simplex ΔT (in 2D). (Left) A valid addition where the new vertex vnew lies within the visibility cone from xg (Criterion 1). (Right) An invalid addition where visibility is obstructed.

### VI-B Algorithm for Growing the Star-Shaped Chain

We find the maximal chain of simplexes, $\mathcal{C}_{g}$, that satisfy the visibility criterion by searching outward from the goal simplex $\Delta_{g}$. The general geometric search is detailed in Algorithm 2. For our experiments, this search was constrained to only explore backward along the precomputed discrete plan to ensure a fair comparison with the baseline. Within the resulting region $\mathcal{R}_{g}=\bigcup_{\Delta_{i}\in\mathcal{C}_{g}}\Delta_{i}$, for any cell $\Delta_{i}\in\mathcal{C}_{g}$, its cell vector field $V_{c,i}$, as well as its internal face vectors (not on the boundary of $\mathcal{R}_{g}$), are set to point directly to the goal. To ensure a smooth transition at the boundary of $\mathcal{R}_{g}$, we keep the face vectors assigned to each face and smoothly blend them with the new direct-to-goal $V_{c,i}$.

1:Set of simplexes 𝒯, goal point xg. 2:The set of simplexes 𝒞g forming the star-shaped region. 3:Let Δg be the simplex containing xg. 4:Initialize queue Q with Δg. 5:Initialize 𝒞g = {Δg} and a set of visited simplexes, Vs = {Δg}. 6:while Q is not empty do 8: for each neighbor Δj of Δi not in Vs do 9: Let 𝒮 be the shared face between Δi and Δj. 10: Let vnew be the vertex of Δj not on 𝒮. 11: if Vertex vnew lies in the visibility cone from xg through 𝒮 then Algorithm 2 Construction of the Maximal Star-Shaped Chain

## Results and Analysis

To evaluate the proposed method, we first compare its trajectory quality against the foundational baseline. We then conduct an ablation study to isolate and quantify the contribution of the star-shaped region. Finally, we compare our approach against four other motion planners and analyze its overall computational efficiency.

### VII-A Comparison with Baseline Feedback Law

The baseline method offers to simply assign each cell vector field as the unit vector pointing from the current point to the midpoint of the exit face, and defines face vector fields as unit vectors normal (perpendicular) to the faces, pointing inward for non-exit faces and outward for the exit face. The comparison was performed in three distinct environments, and to evaluate the robustness of the proposed method, we chose the centroid of every cell in the triangulation as a goal state, generating and analyzing a total of over 20000 integral curves for each environment. We quantified path quality using a set of geometric and dynamics-based metrics. For a path with curvature $\kappa(s)$, we measured the Total Bending, $E_{B}=\int_{0}^{L}\kappa(s)^{2}ds$, and the Total Turning, $E_{T}=\int_{0}^{L}|\kappa(s)|ds$, which measures cumulative heading change. We also measured path length, maximum curvature, and dynamic feasibility by simulating a 2D double integrator with state vector $[p_{x},\dot{p}_{x},p_{y},\dot{p}_{y}]^{T}$, using an LQR controller to find the travel time and total control effort with the cost matrices $Q=\text{diag}$ and $R=I_{2}$ to heavily penalize position error.

The quantitative results are summarized in Table I. The table includes a 'Win Rate' metric, which indicates the percentage of paired trajectories (starting from the same initial point) for which the proposed method achieved a better score on the given metric. For a fair and direct comparison, the underlying discrete plan was computed once and held constant for both methods.

LQR Travel Time LQR Control Effort LQR Travel Time LQR Control Effort LQR Travel Time LQR Control Effort TABLE I: Quantitative Comparison of Methods. NG: Number of Goal Cells tested, NP: Total Integral Curves evaluated.

(c) Baseline: Bug Trap (d) Proposed: Bug Trap Figure 3: Qualitative comparison of integral curves for the baseline and proposed methods across three environments. The maximal star-shaped region is highlighted in brown. Notably, in the Bug Trap environment, Steiner points were introduced to generate closer to equilateral triangles and avoid skewed triangles.

The results (Table I, Figure 3) demonstrate a significant improvement over the baseline method. The primary goal of this work was to address the unnecessary trajectory bending inherent in arbitrary vector field assignments, a problem most directly captured by the total bending and total turning metrics. The proposed method achieved a remarkable 84.33-95.88% reduction in total bending across all scenarios, with a win rate for total turning reaching 99.89% in the Bug Trap environment. This geometric smoothness translated directly into improved dynamic performance, as evidenced by a 30.24-59.16% reduction in LQR control effort, confirming that the generated paths are more energy-efficient and easier for a physical system to follow. These results strongly validate the effectiveness of the heuristic vector alignment and face-vector averaging techniques. While the proposed heuristic improves path quality, we cannot guarantee a lower maximum curvature in all cases, particularly when the underlying plan requires sharp changes in cell vector fields, as the heuristic's projection can itself induce a sharp turn.

### VII-B Ablation Study of Star-Shaped Region

To quantify the specific contribution of the star-shaped region, we performed an ablation study evaluating a comprehensive set of goals (one per simplex) across all three environments, comparing our full method against using only heuristic alignment. The results indicate that while the star-shaped region depends on the goal position, environment, and simplicial complex, it plays an important role in generating smoother integral curves near the goal. Specifically, it reduced total bending by 74.35% and total turning by 44.07% in the Sparse environment, with a 34.77% reduction of total bending in the Maze, and 20.01% in the Bug Trap. This confirms that the star-shaped region effectively exploits local open space to generate more direct paths.

### VII-C Comparative Analysis

We evaluated the proposed method against four baselines: RRT\* (sampling-based), A\* (grid-based), FPP (optimization-based), and APFs (feedback-based). To demonstrate practical utility in realistic scenarios, we used the Moving AI Lab benchmarks, specifically the "Boston" city map, alongside our Maze environment. Baselines were implemented using PythonRobotics and the FPP library with quadtree decomposition. We evaluated more than 10 distinct start-goal configuration pairs for each environment. Due to its stochastic nature, RRT\* was executed 10 times per pair (with a maximum of 5200 iterations), and failures were reported if no path was found. As detailed in Table II and Figure 4, the proposed method, A\*, and FPP achieved 100% success across both environments, whereas the APFs method struggled to find feasible paths. Although the proposed method can yield slightly longer paths, it operates in the sub-90 ms range, making it an efficient and robust feedback planner. We acknowledge that the performance of baseline methods could potentially be improved through further code optimization or extensive parameter tuning; however, these results reflect their performance using standard, widely accessible implementations.

TABLE II: Quantitative comparison of different algorithms in two different environments. Results report the mean ± standard deviation.

Figure 4: Qualitative comparison of paths for the baselines across the maze and sparse environments.

### VII-D Computational Efficiency

Our method splits the computation into offline and online phases for efficiency. The offline phase includes simplicial decomposition, which in 2D (for polygonal obstacles and by CDT), can be performed in $O(n\log n)$ time, where $n$ is the number of obstacle vertices.

A discrete plan can be computed via Dijkstra's algorithm on the connectivity graph. The successor of each simplex can be found in $O(m\log m)$ time, in which $m$ is the number of $d$-simplexes. However, recent theoretical advances have produced even faster algorithms for this problem. Heuristic alignment and star-shaped funnel construction add minimal linear overhead via local geometric checks per simplex. Online execution is lightweight. If the robot's current cell is unknown, a point-location query can be performed in logarithmic time (in 2D) with preprocessing, but can be more expensive in higher dimensions. In a given $d$-simplex, the computation is minimal, requiring only distance checks to its $d+1$ faces followed by the vector field blending.

On a system with an AMD Ryzen 9 8945HS CPU and 32 GB of RAM, using the triangle library for CDT, the offline precomputation (including triangulation, discrete plan, heuristic alignment, and funnel construction) required about 6-9 ms for the standard environments (Maze, Bug Trap, Sparse). For larger and more complex environments, such as the "Boston" benchmark, the precomputation time naturally scales with the number of obstacle vertices and the resulting simplexes. Although the implementation could be further optimized, for planar navigation, the system can handle dynamic environments via global recomputation at about 100 Hz. The online execution is lightweight; evaluating the vector field $V(x)$ at any point $x$ took on average about 0.07 ms, which allows the robot to find a feedback policy in real time (about $15$ kHz update rate). We acknowledge that for higher-dimensional ${\cal C}$, precomputation time would increase, and local mesh repair (if the whole environment does not change) can be a valuable approach.

## Conclusion and Future Work

We introduced a computationally efficient method to reduce unnecessary bending in feedback motion plans on a simplicial complex embedded in ${\cal C}_{free}$. We acknowledge that computing a simplicial complex in higher dimensions can be intractable. However, for $d\leq 3$, algorithms like CDT (e.g. triangle for 2D, Tetgen for 3D) exist, making this method effective and tractable for mobile robots and UAVs. Our approach combines a novel heuristic for aligning local vector fields with a geometric algorithm that constructs a maximal star-shaped funnel around the goal, resulting in more efficient trajectories with significantly lower bending. A natural extension, forming a promising direction for future research, is to cover the entire free space with a set of such star-shaped regions, each with its own local waypoint. This could lead to a highly efficient, global feedback planning framework. Further work will also focus on adapting the alignment heuristics for systems with nonholonomic constraints and validating the framework on physical robot platforms. Furthermore, a promising direction involves co-optimizing the discrete cell-path with our vector field alignment to achieve more globally optimal trajectories.
