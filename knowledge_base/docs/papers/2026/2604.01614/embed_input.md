<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Smooth Feedback Motion Planning with Reduced Curvature

Topics include Motion planning, Robotics, Safety, Robustness, Sampling-based methods, Optimization, Planning, Control, Sampling.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Feedback motion planning over cell decompositions provides a robust method for generating collision-free robot motion with formal guarantees. However, existing algorithms often produce paths with unnecessary bending, leading to slower motion and higher control effort. This paper presents a computationally efficient method to mitigate this issue for a given simplicial decomposition. A heuristic is introduced that systematically aligns and assigns local vector fields to produce more direct trajectories, complemented by a novel geometric algorithm that constructs a maximal star-shaped chain of simplexes around the goal. This creates a large ``funnel'' in which an optimal, direct-to-goal control law can be safely applied. Simulations demonstrate that our method generates measurably more direct paths, reducing total bending by an average of 91.40\% and LQR control effort by an average of 45.47\%. Furthermore, comparative analysis against sampling-based and optimization-based planners confirms the time efficacy and robustness of our approach.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

While the proposed algorithms work over any finite-dimensional simplicial complex embedded in the collision-free subset of the configuration space, the practical application focuses on low-dimensional (dle3) configuration spaces, where simplicial decomposition is computationally tractable.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Feedback motion planning synthesizes a vector field over $\mathcal{C}_{free}$, the collision-free subspace of the configuration space. This creates a closed-loop policy that robustly guides a robot to its goal from almost any admissible state, an essential feature for real-world applications. The framework introduced by Lindemann et al. provides a powerful method for generating such feedback plans by decomposing the space into cells and blending local vector fields. This approach constructs almost globally defined, $C^{\infty}$-smooth feedback laws that guarantee convergence and collision avoidance, nicely sidestepping the local minima that plague artificial potential fields and the high computational cost of global methods such as harmonic functions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The primary limitation of Lindemann et al. is that it lacks the ability to assign local vector fields in a way that generates higher-quality paths. The default assignments of local cell and face vectors, while satisfying theoretical convergence criteria, can produce integral curves with unnecessary bending, particularly when moving between cells. These inefficient paths lead to longer travel times, higher energy consumption, and increased control effort, diminishing the practical utility of the feedback law.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work presents a computationally efficient solution to this problem by systematically assigning local vector fields to produce more direct trajectories. We introduce a simple and efficient heuristic for aligning cell vector fields; by propagating a desired global direction of motion backward from the goal, our method systematically biases local vector fields to produce more direct integral curves. This is enhanced by the face-vector averaging technique that smooths transitions between cells, directly reducing path bending. Furthermore, we develop a novel geometric algorithm to construct a maximal star-shaped chain of simplexes around the goal, creating a large, geometrically verified "funnel" where a direct-to-goal control law can be safely applied for optimal, straight-line convergence. Demonstrations in maze, bug trap, and sparse environments show that our method generates qualitatively superior feedback laws, with trajectories exhibiting measurably lower total bending and reduced control effort compared to the baseline, all while preserving the foundational guarantees of smoothness and global convergence. Although simulations are demonstrated in two dimensions based on Constrained Delaunay Triangulation (CDT), the algorithm applies to any simplicial complex embedded in $\mathcal{C}_{free}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

While obtaining such complexes in higher dimensions is challenging, it is a tractable problem for 2D/3D configuration or workspace.

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-A Potential Fields, Navigation and Harmonic Functions", "weight": 1.0} -->

Artificial Potential Fields (APFs) offer a fast and reactive feedback policy, but suffer from local minima, oscillation, and poor performance in narrow passages. Therefore, enhancements have been proposed to mitigate these issues. Navigation Functions (NFs) are a special class of smooth APFs that ensure global convergence to a goal without local minima under certain assumptions. NFs have been extended to more general geometries or for non-holonomic and multiple robots. However, they are practically challenging to implement, especially in environments with complex obstacle geometries. Harmonic functions also overcome local minima by solving Laplace's equation over the free space. However, the computational cost of solving partial differential equations (PDEs) restricts their use in real-time or high-dimensional applications.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-B Feedback from Cell Decompositions and Bump Functions", "weight": 1.0} -->

To overcome the limitations of global potential functions, Lindemann et al. proposed constructing local vector fields over a convex cell decomposition. In this framework, local vector fields are blended using smooth bump functions to create a feedback law with guaranteed convergence. While this approach is general and has been extended to shaped robots and nonholonomic systems, the assignment of the local vector fields to reduce path bending remains a critical open challenge that this paper addresses. Bump function blends have also been used to compose attractive/repulsive fields with strong safety guarantees.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-C Region-Based and Optimization-Based Planning", "weight": 1.0} -->

In sampling-based methods such as RRT\*, post-processing techniques such as B-spline or shortcutting are common to improve path quality. While these operate on a single path, our method, by construction, generates a $C^{\infty}$-smooth vector field and therefore integral curves. Advanced optimization-based methods, such as the Graph of Convex Sets (GCS) and Fast Path Planning (FPP), find smooth and high-quality paths by solving mathematical programs over convex decompositions. In contrast, our geometric approach avoids expensive optimization, constructing a smooth, computationally efficient feedback law over $\mathcal{C}_{free}$. Tedrake et al. developed the LQR-Trees framework, where stabilizing controllers are verified using sum-of-squares optimization to produce funnel-shaped regions of attraction around sampled trajectories. Later work by Reist et al. replaced the verification process with a simulation-based expansion, broadening the range of applicable systems. While these methods are powerful and optimal, they rely on computationally intensive procedures like sums-of-squares or semidefinite programming to derive regions of attraction.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-C Region-Based and Optimization-Based Planning", "weight": 1.0} -->

In motion planning, identifying large subsets of free space where simple control laws can safely guide the robot is a key strategy. A well-established method is to compute convex regions, either through exact decomposition or iterative expansion. For example, the IRIS algorithm expands large convex polytopes via alternating semidefinite and quadratic programs.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-C Region-Based and Optimization-Based Planning", "weight": 1.0} -->

Other works have explored maximum convex region extraction in triangulated spaces, where convex unions of adjacent triangles are found via dynamic programming. Although convexity simplifies controller design, it is often restrictive. This motivates using star-shaped regions, which we construct geometrically, avoiding dynamics-based verification.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-C Region-Based and Optimization-Based Planning", "weight": 1.0} -->

Our geometric construction of a maximal star-shaped region is conceptually similar to the "Triangular Expansion" algorithm used for computing visibility polygons, as both recursively explore adjacent triangles. However, a key difference lies in our objective. Instead of computing the exact boundary of the visibility polygon, our goal is simply to find the maximal set of simplexes that form a star-shaped region relative to the goal. This simpler objective allows for a more efficient visibility check that generalizes naturally to higher dimensions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We consider the motion planning problem for a robot navigating in a workspace $W \subset {\mathbb{R}}^{n}$ (where $n \in {\{ 2,3\}}$) with static obstacles $\mathcal{O}$. The robot's configuration is a point in its $d$-dimensional configuration space, $\mathcal{C}$, and all motion is restricted to the open collision-free subset, $\mathcal{C}_{free}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The task is to design a $C^{\infty}$-smooth vector field $V$ over $\mathcal{C}_{free}$ whose integral curves are guaranteed to converge to $x_{g} \in \mathcal{C}_{free}$ without collision. We note that $V$ is well-defined and smooth almost everywhere, except on a set of measure zero (the ($d - 2$)-dimensional boundaries of the cell faces, e.g., vertices in 2D) which the integral curves never traverse. To manage geometric complexity, a simplicial complex composed of a finite number of non-degenerate $d$-simplexes, $\mathcal{T} = {\{\Delta_{1},\ldots,\Delta_{N}\}}$, is embedded in $\mathcal{C}_{free}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In this paper's simulations, we use a point robot in 2D; hence, $\mathcal{C} = W \subset {\mathbb{R}}^{2}$ and obstacles are polygonal, and by employing CDT, we ensure that every $2$-simplex is non-degenerate.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We compute a discrete plan on $\mathcal{T}$ (with vertices at simplex centroids and edges connecting adjacent simplexes) by finding a shortest-path tree to the goal simplex $\Delta_{g}$ containing $x_{g}$. This provides a successor mapping, $s{(i)}$, for each simplex $\Delta_{i} \in \mathcal{T}$ that guides the robot toward the goal.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The global vector field is constructed from two local components for each simplex $\Delta_{i}$: 1) a single, constant cell vector field, $V_{c,i}$, respecting successor mapping, $s{(i)}$, and 2) a set of face vector fields, $\{ V_{f}\}$, defined on the boundary faces of the simplex. The final vector field $V{(x)}$ at any point $x \in \Delta_{i}$ is a smooth, weighted combination of $V_{c,i}$ and the vector field of the closest face, following the blending method.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

To further improve efficiency, we identify a maximal star-shaped chain of simplexes $\mathcal{C}_{g} \subseteq \mathcal{T}$ around the goal that forms a star-shaped region $R_{g} = {\bigcup_{\Delta \in \mathcal{C}_{g}}\Delta}$. A set $R$ is star-shaped with respect to $x_{g} \in R$ if for every $x \in R$, the line segment that connects $x$ and $x_{g}$ is contained in $R$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Smooth Feedback on Simplicial Decompositions", "weight": 1.0} -->

Our approach is based on the framework of for simplicial decomposition. The method involves computing a global vector field from local vector fields defined on individual cells and their faces, ensuring smoothness, collision avoidance, and global convergence to a designated goal state.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Smooth Feedback on Simplicial Decompositions", "weight": 1.0} -->

To precisely describe our method, we first recall several essential definitions and theorems.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Fundamental Definitions", "weight": 1.0} -->

To obtain smooth interpolation between local vector fields, we use a special class of smooth functions $b{(\sigma)}$, called bump functions, understood here as $C^{\infty}$ functions that provide a smooth transition between 0 and 1.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Heuristic Vector Field Alignment Method", "weight": 1.0} -->

Arbitrary vector field assignments, even those satisfying Theorem 5, can lead to unnecessary bending in integral curves. To mitigate this, we introduce a heuristic alignment strategy that adjusts each cell vector field to better align with the vector field of its successor(s), producing more direct trajectories.

<!-- chunk {"id": "body-0024", "role": "body", "section": "V-A Heuristic Alignment of Cell Vector Fields", "weight": 1.0} -->

First, we establish a global plan. Let $x_{g}$ be the goal point, and let $\Delta_{g}$ be the goal simplex. For each simplex $\Delta_{i}$, let $c_{i}$ be its centroid. We compute the shortest-path tree rooted at $\Delta_{g}$ on the connectivity graph, which provides a successor $s{(i)}$ and a hop-distance $l{(i)}$ (i.e., the minimum number of simplex transitions required to reach the goal simplex $\Delta_{g}$) for each simplex $\Delta_{i}$. For each non-goal cell $\Delta_{i}$, we identify its exit face $f_{\text{exit},i}$ and the corresponding opposite vertex $v_{{ov},i}$, as illustrated in Figure 1.

<!-- chunk {"id": "body-0025", "role": "body", "section": "V-A Heuristic Alignment of Cell Vector Fields", "weight": 1.0} -->

The core of our heuristic is to process cells in order of increasing hop-distance from the goal, propagating a desired direction backward.

<!-- chunk {"id": "body-0026", "role": "body", "section": "V-A Heuristic Alignment of Cell Vector Fields", "weight": 1.0} -->

in which $p_{v_{j}}$ are the coordinates of the vertices of the exit face $f_{\text{exit},i}$. We then assign the cell vector field $V_{c,i}$ as Algorithm 1.

<!-- chunk {"id": "body-0027", "role": "body", "section": "V-A Heuristic Alignment of Cell Vector Fields", "weight": 1.0} -->

1:Set of simplexes 𝒯, goal point xg.
2:Cell vector field Vc, i for all Δi ∈ 𝒯.
3:Compute centroids ci, graph G, successors s (i), and hop-distances l (i) for all Δi.
4:for each non-goal simplex Δi in ascending order of l (i) do
5: Let {bi, j} be the set of boundary vectors forming the conical region 𝒦i.
12: if vcand, i is not in the conical region 𝒦i then
13: Find bi, j* that minimizes the angle with vcand, i.
Algorithm 1 Heuristic Alignment of Cell Vector Fields

<!-- chunk {"id": "body-0028", "role": "body", "section": "V-A Heuristic Alignment of Cell Vector Fields", "weight": 1.0} -->

To formally check if a candidate vector $v_{\text{cand},i}$ lies within the conical region formed by the basis vectors $\{ b_{i,j}\}$, we must determine if it can be expressed as a non-negative linear combination of them.

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-A Heuristic Alignment of Cell Vector Fields", "weight": 1.0} -->

If a solution for $\{\alpha_{j}\}$ exists, the vector is inside the conical region. If this feasibility problem has no solution, the candidate vector lies outside the cone. In this case, we project it to the closest boundary vector (the one minimizing the angle), a computationally simple choice that guarantees the vector remains within the valid conical region. While this requires solving a small LP for each simplex, the problem is computationally inexpensive as the number of variables ($d$) equals the dimension of the space. This check is efficient enough for precomputation and does not impede the real-time evaluation of the feedback law.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-A Heuristic Alignment of Cell Vector Fields", "weight": 1.0} -->

Although it does not guarantee a globally optimal path, in practice, it yields significantly straighter and more uniform trajectories compared to unaligned cell fields. The effectiveness of the alignment heuristic extends beyond local smoothing. The heuristic encourages consecutive cell vector fields, $V_{c,i}$ and $V_{c,{s{(i)}}}$, to adopt a similar direction. By then defining the exit face vector field as the average of these two vectors, our method naturally creates conditions where adjacent cells with a coherent flow functionally merge. This process forms larger regions of consistent flow, guiding the robot along globally straighter paths.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-B Assignment of Face Vector Fields and Proof of Validity", "weight": 1.0} -->

For each non-exit face $f \in {F_{i} \smallsetminus {\{ f_{\text{exit},i}\}}}$, we modify the standard inward-pointing normal to better align with the cell's flow.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-B Assignment of Face Vector Fields and Proof of Validity", "weight": 1.0} -->

We must ensure these assignments satisfy Definition 3, guaranteeing the robot exits strictly through the exit face.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-C Blending the Vector Fields", "weight": 1.0} -->

Finally, within each cell $\Delta_{i}$, a single smooth vector field $V{(x)}$ is synthesized by interpolating between the cell vector $V_{c,i}$ and the vector of the closest face.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-C Blending the Vector Fields", "weight": 1.0} -->

For any point $x \in \Delta_{i}$, we first identify its closest face, $f^{\ast} \in F_{i}$, by computing the perpendicular distance $d{(x,f)}$ to every face $f$ of the cell. The region of influence of $f^{\ast}$ (its Voronoi region) consists of all points for which $f^{\ast}$ is the closest face.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-C Blending the Vector Fields", "weight": 1.0} -->

Within this region, we use the smooth bump function $b{(\sigma)}$ from Definition 1. The parameter $\sigma \in {\lbrack 0,1\rbrack}$ must be 0 on the face $f^{\ast}$ and 1 on the GVD surface (the boundary of the region of influence).

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-C Blending the Vector Fields", "weight": 1.0} -->

This construction guarantees that the vector field is identical to the face vector on the cell boundary, ensuring continuity across cells, and smoothly transitions to the cell vector field toward the interior of the cell.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Constructing the Maximal Star-shaped Chain of Simplexes", "weight": 1.0} -->

To create more direct trajectories, we identify a large funnel where the robot can safely bypass conservative cell-by-cell transitions. While standard algorithms can compute the exact visibility polytope, they are often computationally intensive as they must construct a precise geometric boundary. Our simplex-based expansion is therefore chosen for its efficiency and simplicity; it relies on a series of simple local visibility tests to incrementally grow the funnel. We acknowledge that this construction is conservative and the resulting region $\mathcal{R}_{g}$ is strictly contained within the true visibility polytope of the goal. The expansion is sensitive to the simplicial complex; for example, Steiner points introduced for mesh quality can prevent the chain expansion even where a simplex is completely visible to the goal. However, this approach is sufficient for our purpose and naturally extends to higher dimensions.

<!-- chunk {"id": "body-0038", "role": "body", "section": "VI-A Geometric Criteria for Star-shaped", "weight": 1.0} -->

Our method incrementally grows a star-shaped region, $\mathcal{R}_{g}$, starting from the goal simplex, $\Delta_{g}$. Consider a region $\mathcal{R} \subset {\mathbb{R}}^{d}$ known to be star-shaped with respect to $x_{g}$. We wish to add an adjacent $d$-simplex, $\Delta_{T}$, which shares a $({d - 1})$-dimensional face $\mathcal{S}$ with $\mathcal{R}$'s boundary. The union $\mathcal{R} \cup \Delta_{T}$ remains star-shaped if the new vertex of $\Delta_{T}$ not on $\mathcal{S}$, denoted $v_{\text{new}}$, is visible from $x_{g}$. See Figure 2 for an illustration. We propose two equivalent geometric criteria for this test.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Criterion 1 (Visibility Cone from Goal)", "weight": 1.0} -->

A visibility cone is formed at the goal $x_{g}$ by the vectors pointing from $x_{g}$ to the vertices of the shared face $\mathcal{S}$. The region $\mathcal{R} \cup \Delta_{T}$ is star-shaped if the vector $v_{\text{new}} - x_{g}$ lies strictly inside this cone.

<!-- chunk {"id": "body-0040", "role": "body", "section": "VI-B Algorithm for Growing the Star-Shaped Chain", "weight": 1.0} -->

We find the maximal chain of simplexes, $\mathcal{C}_{g}$, that satisfy the visibility criterion by searching outward from the goal simplex $\Delta_{g}$. The general geometric search is detailed in Algorithm 2. For our experiments, this search was constrained to only explore backward along the precomputed discrete plan to ensure a fair comparison with the baseline. Within the resulting region $\mathcal{R}_{g} = {\bigcup_{\Delta_{i} \in \mathcal{C}_{g}}\Delta_{i}}$, for any cell $\Delta_{i} \in \mathcal{C}_{g}$, its cell vector field $V_{c,i}$, as well as its internal face vectors (not on the boundary of $\mathcal{R}_{g}$), are set to point directly to the goal.

<!-- chunk {"id": "body-0041", "role": "body", "section": "VI-B Algorithm for Growing the Star-Shaped Chain", "weight": 1.0} -->

To ensure a smooth transition at the boundary of $\mathcal{R}_{g}$, we keep the face vectors assigned to each face and smoothly blend them with the new direct-to-goal $V_{c,i}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VI-B Algorithm for Growing the Star-Shaped Chain", "weight": 1.0} -->

1:Set of simplexes 𝒯, goal point xg.
2:The set of simplexes 𝒞g forming the star-shaped region.
3:Let Δg be the simplex containing xg.
4:Initialize queue Q with Δg.
5:Initialize 𝒞g = {Δg} and a set of visited simplexes, Vs = {Δg}.
6:while Q is not empty do
8: for each neighbor Δj of Δi not in Vs do
9: Let 𝒮 be the shared face between Δi and Δj.
10: Let vnew be the vertex of Δj not on 𝒮.
11: if Vertex vnew lies in the visibility cone from xg through 𝒮 then
Algorithm 2 Construction of the Maximal Star-Shaped Chain

<!-- chunk {"id": "body-0043", "role": "body", "section": "Results and Analysis", "weight": 1.0} -->

To evaluate the proposed method, we first compare its trajectory quality against the foundational baseline. We then conduct an ablation study to isolate and quantify the contribution of the star-shaped region. Finally, we compare our approach against four other motion planners and analyze its overall computational efficiency.

<!-- chunk {"id": "body-0044", "role": "body", "section": "VII-A Comparison with Baseline Feedback Law", "weight": 1.0} -->

The baseline method offers to simply assign each cell vector field as the unit vector pointing from the current point to the midpoint of the exit face, and defines face vector fields as unit vectors normal (perpendicular) to the faces, pointing inward for non-exit faces and outward for the exit face. The comparison was performed in three distinct environments, and to evaluate the robustness of the proposed method, we chose the centroid of every cell in the triangulation as a goal state, generating and analyzing a total of over 20000 integral curves for each environment. We quantified path quality using a set of geometric and dynamics-based metrics. For a path with curvature $\kappa{(s)}$, we measured the Total Bending, $E_{B} = {\int_{0}^{L}{\kappa{(s)}^{2}{ds}}}$, and the Total Turning, $E_{T} = {\int_{0}^{L}{{|{\kappa{(s)}}|}{ds}}}$, which measures cumulative heading change.

<!-- chunk {"id": "body-0045", "role": "body", "section": "VII-A Comparison with Baseline Feedback Law", "weight": 1.0} -->

We also measured path length, maximum curvature, and dynamic feasibility by simulating a 2D double integrator with state vector ${\lbrack p_{x},{\overset{˙}{p}}_{x},p_{y},{\overset{˙}{p}}_{y}\rbrack}^{T}$, using an LQR controller to find the travel time and total control effort with the cost matrices $Q = {\text{diag}{({\lbrack 100,1,100,1\rbrack})}}$ and $R = I_{2}$ to heavily penalize position error.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VII-A Comparison with Baseline Feedback Law", "weight": 1.0} -->

The quantitative results are summarized in Table I. The table includes a 'Win Rate' metric, which indicates the percentage of paired trajectories (starting from the same initial point) for which the proposed method achieved a better score on the given metric. For a fair and direct comparison, the underlying discrete plan was computed once and held constant for both methods.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VII-A Comparison with Baseline Feedback Law", "weight": 1.0} -->

The results (Table I, Figure 3) demonstrate a significant improvement over the baseline method. The primary goal of this work was to address the unnecessary trajectory bending inherent in arbitrary vector field assignments, a problem most directly captured by the total bending and total turning metrics. The proposed method achieved a remarkable 84.33-95.88% reduction in total bending across all scenarios, with a win rate for total turning reaching 99.89% in the Bug Trap environment. This geometric smoothness translated directly into improved dynamic performance, as evidenced by a 30.24-59.16% reduction in LQR control effort, confirming that the generated paths are more energy-efficient and easier for a physical system to follow. These results strongly validate the effectiveness of the heuristic vector alignment and face-vector averaging techniques. While the proposed heuristic improves path quality, we cannot guarantee a lower maximum curvature in all cases, particularly when the underlying plan requires sharp changes in cell vector fields, as the heuristic's projection can itself induce a sharp turn.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VII-B Ablation Study of Star-Shaped Region", "weight": 1.0} -->

To quantify the specific contribution of the star-shaped region, we performed an ablation study evaluating a comprehensive set of goals (one per simplex) across all three environments, comparing our full method against using only heuristic alignment. The results indicate that while the star-shaped region depends on the goal position, environment, and simplicial complex, it plays an important role in generating smoother integral curves near the goal. Specifically, it reduced total bending by 74.35% and total turning by 44.07% in the Sparse environment, with a 34.77% reduction of total bending in the Maze, and 20.01% in the Bug Trap. This confirms that the star-shaped region effectively exploits local open space to generate more direct paths.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VII-C Comparative Analysis", "weight": 1.0} -->

We evaluated the proposed method against four baselines: RRT\* (sampling-based), A\* (grid-based), FPP (optimization-based), and APFs (feedback-based). To demonstrate practical utility in realistic scenarios, we used the Moving AI Lab benchmarks, specifically the "Boston" city map, alongside our Maze environment. Baselines were implemented using PythonRobotics and the FPP library with quadtree decomposition. We evaluated more than 10 distinct start-goal configuration pairs for each environment. Due to its stochastic nature, RRT\* was executed 10 times per pair (with a maximum of 5200 iterations), and failures were reported if no path was found. As detailed in Table II and Figure 4, the proposed method, A\*, and FPP achieved 100% success across both environments, whereas the APFs method struggled to find feasible paths. Although the proposed method can yield slightly longer paths, it operates in the sub-90 ms range, making it an efficient and robust feedback planner. We acknowledge that the performance of baseline methods could potentially be improved through further code optimization or extensive parameter tuning; however, these results reflect their performance using standard, widely accessible implementations.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VII-D Computational Efficiency", "weight": 1.0} -->

Our method splits the computation into offline and online phases for efficiency. The offline phase includes simplicial decomposition, which in 2D (for polygonal obstacles and by CDT), can be performed in $O{({n{\log n}})}$ time, where $n$ is the number of obstacle vertices.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VII-D Computational Efficiency", "weight": 1.0} -->

A discrete plan can be computed via Dijkstra's algorithm on the connectivity graph. The successor of each simplex can be found in $O{({m{\log m}})}$ time, in which $m$ is the number of $d$-simplexes. However, recent theoretical advances have produced even faster algorithms for this problem. Heuristic alignment and star-shaped funnel construction add minimal linear overhead via local geometric checks per simplex. Online execution is lightweight. If the robot's current cell is unknown, a point-location query can be performed in logarithmic time (in 2D) with preprocessing, but can be more expensive in higher dimensions. In a given $d$-simplex, the computation is minimal, requiring only distance checks to its $d + 1$ faces followed by the vector field blending.

<!-- chunk {"id": "body-0052", "role": "body", "section": "VII-D Computational Efficiency", "weight": 1.0} -->

On a system with an AMD Ryzen 9 8945HS CPU and 32 GB of RAM, using the triangle library for CDT, the offline precomputation (including triangulation, discrete plan, heuristic alignment, and funnel construction) required about 6-9 ms for the standard environments (Maze, Bug Trap, Sparse). For larger and more complex environments, such as the "Boston" benchmark, the precomputation time naturally scales with the number of obstacle vertices and the resulting simplexes. Although the implementation could be further optimized, for planar navigation, the system can handle dynamic environments via global recomputation at about 100 Hz. The online execution is lightweight; evaluating the vector field $V{(x)}$ at any point $x$ took on average about 0.07 ms, which allows the robot to find a feedback policy in real time (about $15$ kHz update rate). We acknowledge that for higher-dimensional $\mathcal{C}$, precomputation time would increase, and local mesh repair (if the whole environment does not change) can be a valuable approach.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We introduced a computationally efficient method to reduce unnecessary bending in feedback motion plans on a simplicial complex embedded in $\mathcal{C}_{free}$. We acknowledge that computing a simplicial complex in higher dimensions can be intractable. However, for $d \leq 3$, algorithms like CDT (e.g. triangle for 2D, Tetgen for 3D) exist, making this method effective and tractable for mobile robots and UAVs. Our approach combines a novel heuristic for aligning local vector fields with a geometric algorithm that constructs a maximal star-shaped funnel around the goal, resulting in more efficient trajectories with significantly lower bending. A natural extension, forming a promising direction for future research, is to cover the entire free space with a set of such star-shaped regions, each with its own local waypoint. This could lead to a highly efficient, global feedback planning framework. Further work will also focus on adapting the alignment heuristics for systems with nonholonomic constraints and validating the framework on physical robot platforms.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Furthermore, a promising direction involves co-optimizing the discrete cell-path with our vector field alignment to achieve more globally optimal trajectories.
