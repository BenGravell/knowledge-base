<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Informed RRT*: Optimal Sampling-based Path Planning Focused via Direct Sampling of an Admissible Ellipsoidal Heuristic

Topics include Motion planning, Sampling-based planning, Asymptotic optimality, Informed rapidly-exploring random tree star, Rapidly-exploring random tree star, Heuristic search, Informed set.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Informed RRT* accelerates convergence of RRT* by restricting sampling to the prolate hyperspheroid (ellipsoidal) subset of the state space that can possibly improve the current best solution, rather than sampling the entire domain. This focused sampling preserves RRT*'s probabilistic completeness and asymptotic optimality guarantees while significantly improving convergence rate and final solution quality, especially in high-dimensional spaces or large environments. However, the ellipsoidal region is only valid for path planning where the cost is the Euclidean path length; for other costs or kindodynamic planning the informed set has some other geometry that is not generally known to be computable in closed form.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Rapidly-exploring random trees (RRTs) are popular in motion planning because they find solutions efficiently to single-query problems. Optimal RRTs (RRT*s) extend RRTs to the problem of finding the optimal solution, but in doing so asymptotically find the optimal path from the initial state to every state in the planning domain. This behaviour is not only inefficient but also inconsistent with their single-query nature. For problems seeking to minimize path length, the subset of states that can improve a solution can be described by a prolate hyperspheroid. We show that unless this subset is sampled directly, the probability of improving a solution becomes arbitrarily small in large worlds or high state dimensions. In this paper, we present an exact method to focus the search by directly sampling this subset. The advantages of the presented sampling technique are demonstrated with a new algorithm, Informed RRT*. This method retains the same probabilistic guarantees on completeness and optimality as RRT* while improving the convergence rate and final solution quality. We present the algorithm as a simple modification to RRT* that could be further extended by more advanced path-planning algorithms.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We show experimentally that it outperforms RRT* in rate of convergence, final solution cost, and ability to find difficult passages while demonstrating less dependence on the state dimension and range of the planning problem.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The motion-planning problem is commonly solved by first discretizing the continuous state space with either a grid for graph-based searches or through random sampling for stochastic incremental searches. Graph-based searches, such as A\*, are often *resolution complete* and *resolution optimal*. They are guaranteed to find the optimal solution, if a solution exists, and return failure otherwise (up to the resolution of the discretization). These graph-based algorithms do not scale well with problem size (e.g., state dimension or problem range).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochastic searches, such as [[RRTs]](#id75.75.id75), [[PRMs]](#id71.71.id71), and Expansive Space Trees, use sampling-based methods to avoid requiring a discretization of the state space. This allows them to scale more effectively with problem size and to directly consider kinodynamic constraints; however, the result is a less-strict completeness guarantee. [[RRTs]](#id75.75.id75) are *probabilistically complete*, guaranteeing that the probability of finding a solution, if one exists, approaches unity as the number of iterations approaches infinity.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Until recently, these sampling-based algorithms made no claims about the optimality of the solution. Urmson and Simmons had found that using a heuristic to bias sampling improved [[RRT]](#id75.75.id75) solutions, but did not formally quantify the effects. Ferguson and Stentz recognized that the length of a solution bounds the possible improvements from above, and demonstrated an iterative anytime [[RRT]](#id75.75.id75) method to solve a series of subsequently smaller planning problems. Karaman and Frazzoli later showed that [[RRTs]](#id75.75.id75) return a suboptimal path with probability one, demonstrating that all [[RRT]](#id75.75.id75)-based methods will almost surely be suboptimal and presented a new class of optimal planners.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

They named their optimal variants of [[RRTs]](#id75.75.id75) and [[PRMs]](#id71.71.id71), [[RRT\*]](#id77.77.id77) and [[PRM\*]](#id72.72.id72), respectively. These algorithms are shown to be *asymptotically optimal*, with the probability of finding the optimal solution approaching unity as the number of iterations approaches infinity.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present the *focused* optimal planning problem as it relates to the minimization of path length in ${\mathbb{R}}^{n}$. For such problems, a necessary condition to improve the solution at any iteration is the addition of states from an ellipsoidal subset of the planning domain,. We show that the probability of adding such states through uniform sampling becomes arbitrarily small as the size of the planning problem increases or the solution approaches the theoretical minimum, and present an exact method to sample the ellipsoidal subset directly. It is also shown that with strict assumptions (i.e., no obstacles) that this direct sampling results in linear convergence to the optimal solution.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

This direct-sampling method allows for the creation of informed-sampling planners. Such a planner, Informed [[RRT\*]](#id77.77.id77), is presented to demonstrate the advantages of *informed* incremental search (Fig. 1). Informed [[RRT\*]](#id77.77.id77) behaves as [[RRT\*]](#id77.77.id77) until a first solution is found, after which it only samples from the subset of states defined by an admissible heuristic to possibly improve the solution. This subset implicitly balances exploitation versus exploration and requires no additional tuning (i.e., there are no additional parameters) or assumptions (i.e., all relevant homotopy classes are searched). While heuristics may not always improve the search, their prominence in real-world planning demonstrates their practicality.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In situations where they provide no additional information (e.g., when the informed subset includes the entire planning problem), Informed [[RRT\*]](#id77.77.id77) is equivalent to [[RRT\*]](#id77.77.id77).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Informed [[RRT\*]](#id77.77.id77) is a simple modification to [[RRT\*]](#id77.77.id77) that demonstrates a clear improvement. In simulation, it performs as well as existing [[RRT\*]](#id77.77.id77) algorithms on simple configurations, and demonstrates order-of-magnitude improvements as the configurations become more difficult (Fig. 2). As a result of its focused search, the algorithm has less dependence on the dimension and domain of the planning problem as well as the ability to find better topologically distinct paths sooner. It is also capable of finding solutions within tighter tolerances of the optimum than [[RRT\*]](#id77.77.id77) with equivalent computation, and in the absence of obstacles can find the optimal solution to within machine zero in finite time (Fig. 3). It could also be used in combination with other algorithms, such as path-smoothing, to further reduce the search space.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows. Section II presents a formal definition of the focused optimal planning problem and reviews the existing literature. Section III presents a closed-form estimate of the subset of states that can improve a solution for problems seeking to minimize path length in ${\mathbb{R}}^{n}$ and analyzes the implications on [[RRT\*]](#id77.77.id77)-style algorithms. Section IV presents a method to sample this subset directly. Section V presents the Informed [[RRT\*]](#id77.77.id77) algorithm and Section VI presents simulation results comparing [[RRT\*]](#id77.77.id77) and Informed [[RRT\*]](#id77.77.id77) on simple planning problems of various size and configuration and random problems of various dimension. Section VII concludes the paper with a discussion of the technique and some related ongoing work.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Problem Definition", "weight": 1.0} -->

We define the optimal planning problem similarly to. Let $X \subseteq {\mathbb{R}}^{n}$ be the state space of the planning problem. Let $X_{obs} \subsetneq X$ be the states in collision with obstacles and $X_{free} = {X \smallsetminus X_{obs}}$ be the resulting set of permissible states. Let $\mathbf{x}_{start} \in X_{free}$ be the initial state and $\mathbf{x}_{goal} \in X_{free}$ be the desired final state. Let $\sigma:{\lbrack 0,1\rbrack\mapsto X}$ be a sequence of states (a path) and $\Sigma$ be the set of all nontrivial paths.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Problem Definition", "weight": 1.0} -->

The optimal planning problem is then formally defined as the search for the path, $\sigma^{\ast}$, that minimizes a given cost function, $c:{\Sigma\mapsto{\mathbb{R}}_{\geq 0}}$, while connecting $\mathbf{x}_{start}$ to $\mathbf{x}_{goal}$ through free space, where ${\mathbb{R}}_{\geq 0}$ is the set of non-negative real numbers.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Problem Definition", "weight": 1.0} -->

Let $f(\mathbf{x})$ be the cost of an optimal path from $\mathbf{x}_{start}$ to $\mathbf{x}_{goal}$ constrained to pass through $\mathbf{x}$. Then the subset of states that can improve the current solution, $X_{f} \subseteq X$, can be expressed in terms of the current solution cost, $c_{best}$, The problem of focusing [[RRT\*]](#id77.77.id77)'s search in order to increase the convergence rate is equivalent to increasing the probability of adding a random state from $X_{f}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Problem Definition", "weight": 1.0} -->

As $f( \cdot )$ is generally unknown, a heuristic function, $\hat{f}( \cdot )$, may be used as an estimate. This heuristic is referred to as *admissible* if it never overestimates the true cost of the path, i.e., ${{\forall\mathbf{x}} \in X},{{\hat{f}(\mathbf{x})} \leq {f(\mathbf{x})}}$. An estimate of $X_{f}$, $X_{\hat{f}}$, can then be defined analogously to. For admissible heuristics, this estimate is guaranteed to completely contain the true set, $X_{\hat{f}} \supseteq X_{f}$, and thus inclusion in the estimated set is also a necessary condition to improving the current solution.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Prior Work", "weight": 1.0} -->

Prior work to focus [[RRT]](#id75.75.id75) and [[RRT\*]](#id77.77.id77) has relied on sample biasing, heuristic-based sample rejection, heuristic-based graph pruning, and/or iterative searches.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B1 Sample Biasing", "weight": 1.0} -->

Sample biasing attempts to increase the frequency that states are sampled from $X_{f}$ by biasing the distribution of samples drawn from $X$. This continues to add states from outside of $X_{f}$ that cannot improve the solution. It also results in a nonuniform density over the problem being searched, violating a key [[RRT\*]](#id77.77.id77) assumption.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Heuristic-biased Sampling", "weight": 1.0} -->

Heuristic-biased sampling attempts to increase the probability of sampling $X_{f}$ by weighting the sampling of $X$ with a heuristic estimate of each state. It is used to improve the quality of a regular [[RRT]](#id75.75.id75) by Urmson and Simmons in the Heuristically Guided ([[hRRT]](#id76.76.id76)) by selecting states with a probability inversely proportional to their heuristic cost. The [[hRRT]](#id76.76.id76) was shown to find better solutions than [[RRT]](#id75.75.id75); however, the use of RRTs means that the solution is almost surely suboptimal.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Heuristic-biased Sampling", "weight": 1.0} -->

Kiesel et al. use a two-stage process to create an [[RRT\*]](#id77.77.id77) heuristic in their *f-biasing* technique. A coarse abstraction of the planning problem is initially solved to provide a heuristic cost for each discrete state. [[RRT\*]](#id77.77.id77) then samples new states by randomly selecting a discrete state and sampling inside it with a continuous uniform distribution. The discrete sampling is biased such that states belonging to the abstracted solution have the highest probability of selection. This technique provides a heuristic bias for the full duration of the [[RRT\*]](#id77.77.id77) algorithm; however, to account for the discrete abstraction it maintains a nonzero probability of selecting every state. As a result, states that cannot improve the current solution are still sampled.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Path Biasing", "weight": 1.0} -->

Path-biased sampling attempts to increase the frequency of sampling $X_{f}$ by sampling around the current solution path. This assumes that the current solution is either homotopic to the optimum or separated only by small obstacles. As this assumption is not generally true, path-biasing algorithms must also continue to sample globally to avoid local optima. The ratio of these two sampling methods is frequently a user-tuned parameter.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Path Biasing", "weight": 1.0} -->

Alterovitz et al. use path biasing to develop the Rapidly-exploring Roadmap ([[RRM]](#id74.74.id74)). Once an initial solution is found, each iteration of the [[RRM]](#id74.74.id74) either samples a new state or selects an existing state from the current solution and refines it. Path refinement occurs by connecting the selected state to its neighbours resulting in a graph instead of a tree.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Path Biasing", "weight": 1.0} -->

Akgun and Stilman use path biasing in their dual-tree version of [[RRT\*]](#id77.77.id77). Once an initial solution is found, the algorithm spends a user-specified percentage of its iterations refining the current solution. It does this by randomly selecting a state from the solution path and then explicitly sampling from its Voronoi region. This increases the probability of improving the current path at the expense of exploring other homotopy classes. Their algorithm also employs sample rejection in exploring the state space (Section II-B2).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Path Biasing", "weight": 1.0} -->

Nasir et al. combine path biasing with smoothing in their [[RRT\*]](#id77.77.id77)-Smart algorithm. When a solution is found, [[RRT\*]](#id77.77.id77)-Smart first smooths and reduces the path to its minimum number of states before using these states as biases for further sampling. This adds the complexity of a path-smoothing algorithm to the planner while still requiring global sampling to avoid local optima. While the path smoothing quickly reduces the cost of the current solution, it may also reduce the probability of finding a different homotopy class by removing the number of bias points about which samples are drawn and further violates the [[RRT\*]](#id77.77.id77) assumption of uniform density.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Path Biasing", "weight": 1.0} -->

Kim et al. use a visibility analysis to generate an initial bias in their Cloud RRT\* algorithm. This bias is updated as a solution is found to further concentrate sampling near the path.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B2 Heuristic-based Sample Rejection", "weight": 1.0} -->

Heuristic-based sample rejection attempts to increase the real-time rate of sampling $X_{f}$ by using rejection sampling on $X$ to sample $X_{\hat{f}}$. Samples drawn from a larger distribution are either kept or rejected based on their heuristic value. Akgun and Stilman use such a technique in their algorithm. While this is computationally inexpensive for a single iteration, the number of iterations necessary to find a single state in $X_{\hat{f}}$ is proportional to its size relative to the sampling domain. This becomes nontrivial as the solution approaches the theoretical minimum or the planning domain grows.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B2 Heuristic-based Sample Rejection", "weight": 1.0} -->

Otte and Correll draw samples from a subset of the planning domain in their parallelized C-FOREST algorithm. This subset is defined as the hyperrectangle that bounds the prolate hyperspheroidal informed subset. While this improves the performance of sample rejection, its utility decreases as the dimension of the problem increases (Remark 2 ‣ III Analysis of the Ellipsoidal Informed Subset ‣ Informed RRT*: Optimal Sampling-based Path Planning Focused via Direct Sampling of an Admissible Ellipsoidal Heuristic")).

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-B3 Graph Pruning", "weight": 1.0} -->

Graph pruning attempts to increase the real-time exploration of $X_{f}$ by using a heuristic function to limit the graph to $X_{\hat{f}}$. States in the planning graph with a heuristic cost greater than the current solution are periodically removed while global sampling is continued. The space-filling nature of [[RRTs]](#id75.75.id75) biases the expansion of the pruned graph towards the perimeter of $X_{\hat{f}}$. After the subset is filled, only samples from within $X_{\hat{f}}$ itself can add new states to the graph. In this way, graph pruning becomes a rejection-sampling method after greedily filling the target subset. As adding a new state to an [[RRT]](#id75.75.id75) requires a call to a nearest-neighbour algorithm, graph pruning will be more computationally expensive than simple sample rejection while still suffering from the same probabilistic limitations.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-B3 Graph Pruning", "weight": 1.0} -->

Karaman et al. use graph pruning to implement an anytime version of [[RRT\*]](#id77.77.id77) that improves solutions during execution. They use the current vertex cost plus a heuristic estimate of the cost from the vertex to the goal to periodically remove states from the tree that cannot improve the current solution. As [[RRT\*]](#id77.77.id77) asymptotically approaches the optimal cost of a vertex *from above*, this is an inadmissible heuristic for the cost of a solution through a vertex (Section III). This can overestimate the heuristic cost of a vertex resulting in erroneous removal, especially early in the algorithm when the tree is coarse. Jordan and Perez use the same inadmissible heuristic in their bidirectional [[RRT\*]](#id77.77.id77) algorithm.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-B3 Graph Pruning", "weight": 1.0} -->

Arslan and Tsiotras use a graph structure and lifelong planning A\* ([[LPA\*]](#id67.67.id67)) techniques in the [[RRT]](#id75.75.id75)\# algorithm to prune the existing graph. Each existing state is given a [[LPA\*]](#id67.67.id67)-style key that is updated after the addition of each new state. Only keys that are less than the current best solution are updated, and only up-to-date keys are available for connection with newly drawn samples.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-B4 Anytime [[RRTs]](#id75.75.id75)", "weight": 1.0} -->

Ferguson and Stentz recognized that a solution bounds the subset of states that can provide further improvement from above. Their iterative [[RRT]](#id75.75.id75) method, Anytime [[RRTs]](#id75.75.id75), solves a series of independent planning problems whose domains are defined by the previous solution. They represent these domains as ellipses \[6, Fig. 2\], but do not discuss how to generate samples. Restricting the planning domain encourages each [[RRT]](#id75.75.id75) to find a better solution than the previous; however, to do so they must discard the states already found in $X_{\hat{f}}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-B4 Anytime [[RRTs]](#id75.75.id75)", "weight": 1.0} -->

The algorithm presented in this paper calculates $X_{\hat{f}}$ explicitly and samples from it directly. Unlike path biasing it makes no assumptions about the homotopy class of the optimum and unlike heuristic biasing does not explore states that cannot improve the solution. As it is based on [[RRT\*]](#id77.77.id77), it is able to keep all states found in $X_{\hat{f}}$ for the duration of the search, unlike Anytime [[RRTs]](#id75.75.id75). By sampling $X_{\hat{f}}$ directly, it always samples potential improvements regardless of the relative size of $X_{\hat{f}}$ to $X$. This allows it to work effectively regardless of the size of the planning problem or the relative cost of the current solution to the theoretical minimum, unlike sample rejection and graph pruning methods. In problems where the heuristic does not provide any additional information, it performs identically to [[RRT\*]](#id77.77.id77).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Analysis of the Ellipsoidal Informed Subset", "weight": 1.0} -->

Given a positive cost function, the cost of an optimal path from $\mathbf{x}_{start}$ to $\mathbf{x}_{goal}$ constrained to pass through $\mathbf{x} \in X$, $f(\mathbf{x})$, is equal to the cost of the optimal path from $\mathbf{x}_{start}$ to $\mathbf{x}$, $g(\mathbf{x})$, plus the cost of the optimal path from $\mathbf{x}$ to $\mathbf{x}_{goal}$, $h(\mathbf{x})$. As [[RRT\*]](#id77.77.id77)-based algorithms asymptotically approach the optimal path to every state *from above*, an admissible heuristic estimate, $\hat{f}( \cdot )$, must estimate both these terms.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Analysis of the Ellipsoidal Informed Subset", "weight": 1.0} -->

A sufficient condition for admissibility is that the components, $\hat{g}( \cdot )$ and $\hat{h}( \cdot )$, are individually admissible heuristics of $g( \cdot )$ and $h( \cdot )$, respectively.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Analysis of the Ellipsoidal Informed Subset", "weight": 1.0} -->

For problems seeking to minimize path length in ${\mathbb{R}}^{n}$, Euclidean distance is an admissible heuristic for both terms (even with motion constraints). This *informed* subset of states that may improve the current solution, $X_{\hat{f}} \supseteq X_{f}$, can then be expressed in closed form in terms of the cost of the current solution, $c_{best}$, as which is the general equation of an $n$-dimensional prolate hyperspheroid (i.e., a special hyperellipsoid). The focal points are $\mathbf{x}_{start}$ and $\mathbf{x}_{goal}$, the transverse diameter is $c_{best}$, and the conjugate diameters are $\sqrt{c_{best}^{2} - c_{\min}^{2}}$ (Fig. 4).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Analysis of the Ellipsoidal Informed Subset", "weight": 1.0} -->

Admissibility of $\hat{f}(\cdot)$ makes adding a state in $X_{\hat{f}}$ a necessary condition to improve the solution. With the space-filling nature of [[RRT]](#id75.75.id75), the probability of adding such a state quickly becomes the probability of sampling such a state^11^1States may be added to $X_{\hat{f}}$ with a sample from outside the subset until it is filled to within the [[RRT]](#id75.75.id75) growth-limiting parameter, $\eta$, of its boundary..

<!-- chunk {"id": "body-0038", "role": "body", "section": "Analysis of the Ellipsoidal Informed Subset", "weight": 1.0} -->

Thus, the probability of improving the solution at any iteration by uniformly sampling a larger subset, ${\mathbf{x}^{i + 1} \sim {\mathcal{U}\left(X_{s} \right)}},{X_{s} \supseteq X_{\hat{f}}}$, is less than or equal to the ratio of set measures $\lambda(\cdot)$, Using the volume of a prolate hyperspheroid in ${\mathbb{R}}^{n}$ gives with $\zeta_{n}$ being the volume of a unit $n$-ball.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 1 (Rejection sampling)", "weight": 1.0} -->

From it can be observed that the probability of improving a solution through uniform sampling becomes arbitrarily small for large subsets (e.g., global sampling) or as the solution approaches the theoretical minimum.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 2 (Rectangular rejection sampling)", "weight": 1.0} -->

Let $X_{s}$ be a hyperrectangle that tightly bounds the informed subset (i.e., the widths of each side correspond to the diameters of the prolate hyperspheroid). From, the probability that a sample drawn uniformly from $X_{s}$ will be in $X_{\hat{f}}$ is then $\frac{\zeta_{n}}{2^{n}}$, which decreases rapidly with $n$. For example, with $n = 6$ this gives a maximum $8\%$ probability of improving a solution at each iteration through rejection sampling regardless of the specific solution, problem, or algorithm parameters.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Direct Sampling of an Ellipsoidal Subset", "weight": 1.0} -->

This transformation can be calculated by Cholesky decomposition of the hyperellipsoid matrix, $\mathbf{S} \in {\mathbb{R}}^{n \times n}$, with $\mathbf{S}$ having eigenvectors corresponding to the axes of the hyperellipsoid, $\left\{ \mathbf{a}_{i} \right\}$, and eigenvalues corresponding to the squares of its radii, $\left\{ r_{i}^{2} \right\}$. The transformation, $\mathbf{L}$, maintains the uniform distribution in $X_{ellipse}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Direct Sampling of an Ellipsoidal Subset", "weight": 1.0} -->

For prolate hyperspheroids, such as $X_{\hat{f}}$, the transformation can be calculated from just the transverse axis and the radii. The hyperellipsoid matrix in a coordinate system aligned with the transverse axis is the diagonal matrix with a resulting decomposition of where $\operatorname{diag}\left\{ \cdot \right\}$ denotes a diagonal matrix.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Direct Sampling of an Ellipsoidal Subset", "weight": 1.0} -->

The rotation from the hyperellipsoid frame to the world frame, $\mathbf{C} \in {SO(n)}$, can be solved directly as a general Wahba problem. It has been shown that a valid solution can be found even when the problem is underspecified. The rotation matrix is given by where $\det(\cdot)$ is the matrix determinant and $\mathbf{U} \in {\mathbb{R}}^{n \times n}$ and $\mathbf{V} \in {\mathbb{R}}^{n \times n}$ are unitary matrices such that ${\mathbf{U}\mathbf{\Sigma}\mathbf{V}^{T}} \equiv \mathbf{M}$ via singular value decomposition.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Direct Sampling of an Ellipsoidal Subset", "weight": 1.0} -->

The matrix $\mathbf{M}$ is given by the outer product of the transverse axis in the world frame, $\mathbf{a}_{1}$, and the first column of the identity matrix, $\mathbf{1}_{1}$, A state uniformly distributed in the informed subset, $\mathbf{x}_{\hat{f}} \sim {\mathcal{U}\left(X_{\hat{f}} \right)}$, can thus be calculated from a sample drawn uniformly from a unit $n$-ball, $\mathbf{x}_{ball} \sim {\mathcal{U}\left(X_{ball} \right)}$, through a transformation, rotation, and translation, This procedure is presented algorithmically in Alg. 2.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Direct Sampling of an Ellipsoidal Subset", "weight": 1.0} -->

6 cbest ← minxsoln ∈ Xsoln{Cost (xsoln)}; 7 xrand ← Sample (xstart, xgoal, cbest); 8 xnearest ← Nearest (𝒯, xrand); 9 xnew ← Steer (xnearest, xrand); 10 if CollisionFree (xnearest, xnew) then 12 Xnear ← Near (𝒯, xnew, rRRT*); 14 cmin ← Cost (xmin) + c ⋅ Line (xnearest, xnew); 15 for ∀xnear ∈ Xnear do 16 cnew ← Cost (xnear) + c ⋅ Line (xnear, xnew); 17 if cnew < cmin then 18 if CollisionFree (xnear, xnew) then 26 for ∀xnear ∈ Xnear do 27 cnear ← Cost (xnear); 28 cnew ← Cost (xnew) + c ⋅ Line (xnew, xnear); 29 if cnew < cnear then 30 if CollisionFree (xnew, xnear) then 31 xparent ← Parent (xnear); 38

<!-- chunk {"id": "body-0046", "role": "body", "section": "Direct Sampling of an Ellipsoidal Subset", "weight": 1.0} -->

if InGoalRegion (xnew) then 39 Xsoln ← Xsoln ∪ {xnew}; Algorithm 1 Informed RRT*(xstart, xgoal)

<!-- chunk {"id": "body-0047", "role": "body", "section": "Informed [[RRT\\*]](#id77.77.id77)", "weight": 1.0} -->

An example algorithm using direct informed sampling, Informed [[RRT\*]](#id77.77.id77), is presented in Algs. 1 and 2. It is identical to [[RRT\*]](#id77.77.id77) as presented, with the addition of lines 1, 1, 1, 1, and 1. Like [[RRT\*]](#id77.77.id77), it searches for the optimal path, $\sigma^{\ast}$, to a planning problem by incrementally building a tree in state space, $\mathcal{T} = (V,E)$, consisting of a set of vertices, $V \subseteq X_{free}$, and edges, $E \subseteq {X_{free} \times X_{free}}$. New vertices are added by growing the graph in free space towards randomly selected states. The graph is rewired with each new vertex such that the cost of the nearby vertices are minimized.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Informed [[RRT\\*]](#id77.77.id77)", "weight": 1.0} -->

The algorithm differs from [[RRT\*]](#id77.77.id77) in that once a solution is found, it focuses the search on the part of the planning problem that can improve the solution. It does this through direct sampling of the ellipsoidal heuristic. As solutions are found (line 1), Informed [[RRT\*]](#id77.77.id77) adds them to a list of possible solutions (line 1). It uses the minimum of this list (line 1) to calculate and sample $X_{\hat{f}}$ directly (line 1). As is conventional, we take the minimum of an empty set to be infinity.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Informed [[RRT\\*]](#id77.77.id77)", "weight": 1.0} -->

The new subfunctions are described below, while descriptions of subfunctions common to [[RRT\*]](#id77.77.id77) can be found: Sample: Given two poses, ${\mathbf{x}_{from},\mathbf{x}_{to}} \in X_{free}$ and a maximum heuristic value, $c_{\max} \in {\mathbb{R}}$, the function ${\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}}\left(\mathbf{x}_{from},\mathbf{x}_{to},c_{\max} \right)$ returns independent and identically distributed ([[i.i.d.]](#id52.52.id52)) samples from the state space, $\mathbf{x}_{new} \in X$, such that the cost of an optimal path between

<!-- chunk {"id": "body-0050", "role": "body", "section": "Informed [[RRT\\*]](#id77.77.id77)", "weight": 1.0} -->

$\mathbf{x}_{from}$ and $\mathbf{x}_{to}$ that is constrained to go through $\mathbf{x}_{new}$ is less than $c_{\max}$ as described in Section III and Alg.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Informed [[RRT\\*]](#id77.77.id77)", "weight": 1.0} -->

2. In most planning problems, $\mathbf{x}_{from} \equiv \mathbf{x}_{start}$, $\mathbf{x}_{to} \equiv \mathbf{x}_{goal}$, and lines 2 to 2 of Alg. 2 can be calculated once at the start of the problem.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Informed [[RRT\\*]](#id77.77.id77)", "weight": 1.0} -->

hyperellipsoid-aligned frame to the world frame as per. As previously discussed, in most planning problems this rotation matrix only needs to be calculated at the beginning of the problem.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Informed [[RRT\\*]](#id77.77.id77)", "weight": 1.0} -->

SampleUnitNBall: The function, $\mathtt{S}\mathtt{a}\mathtt{m}\mathtt{p}\mathtt{l}\mathtt{e}\mathtt{U}\mathtt{n}\mathtt{i}\mathtt{t}\mathtt{N}\mathtt{B}\mathtt{a}\mathtt{l}\mathtt{l}$ returns a uniform sample from the volume of an $n$-ball of unit radius centred at the origin, i.e. $\mathbf{x}_{ball} \sim {\mathcal{U}\left( X_{ball} \right)}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Informed [[RRT\\*]](#id77.77.id77)", "weight": 1.0} -->

2 cmin ← ∥xgoal − xstart∥2; 3 xcentre ← (xstart + xgoal)/2; 4 C ← RotationToWorldFrame (xstart, xgoal); 6 $\left\{ r_{i} \right\}_{i = {2,\ldots,n}}\leftarrow\left. \left(\sqrt{c_{\max}^{2} - c_{\min}^{2}} \right)/2 \right.$; 9 xrand ← (CLxball + xcentre) ∩ X; Algorithm 2 Sample (xstart, xgoal, cmax)

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-A Calculating the Rewiring Radius", "weight": 1.0} -->

At each iteration, the rewiring radius, $r_{{RRT}^{\ast}}$, must be large enough to guarantee almost-sure asymptotic convergence while being small enough to only generate a tractable number of rewiring candidates. Karaman and Frazzoli present a lower-bound for this rewiring radius in terms of the measure of the problem space and the number of vertices in the graph. Their expression assumes a uniform distribution of samples of a unit square. As Informed [[RRT\*]](#id77.77.id77) uniformly samples the *subset* of the planning problem that can improve the solution, a rewiring radius can be calculated from the measure of this informed subset and the related vertices inside it. This updated radius reduces the amount of rewiring necessary and further improves the performance of Informed [[RRT\*]](#id77.77.id77). Ongoing work is focused on finding the exact form of this expression, but the radius provided by appears appropriate. There also exists a $k$-nearest neighbour version of this expression.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Simulations", "weight": 1.0} -->

Informed [[RRT\*]](#id77.77.id77) was compared to [[RRT\*]](#id77.77.id77) on a variety of simple planning problems (Figs. 5 to 7) and randomly generated worlds (e.g., Figs. 1, 2). Simple problems were used to test specific challenges, while the random worlds were used to provide more challenging problems in a variety of state dimensions.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Simulations", "weight": 1.0} -->

Fig. 5(a) was used to examine the effects of the problem range and the ability to find paths within a specified tolerance of the true optimum, with the width of the obstacle, $w$, selected randomly. Fig. 5(b) was used to demonstrate Informed [[RRT\*]](#id77.77.id77)'s ability to find topologically distinct solutions, with the position of the narrow passage, $y_{g}$, selected randomly. For these toy problems, experiments were ended when the planner found a solution cost within the target tolerance of the optimum. Random worlds, as in Fig. 2, were used to test Informed [[RRT\*]](#id77.77.id77) on more complicated problems and in higher state dimensions by giving the algorithms $60$ seconds to improve their initial solutions.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Simulations", "weight": 1.0} -->

For each variation of every experiment, $100$ different runs of both [[RRT\*]](#id77.77.id77) and Informed [[RRT\*]](#id77.77.id77) were performed with a common pseudo-random seed and map.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Simulations", "weight": 1.0} -->

The algorithms share the same unoptimized code, allowing for the comparison of relative computational time^22^2Experiments were run in Ubuntu 12.04 on an Intel i5-2500K CPU with 8GB of RAM.. While further optimization would reduce the effect of graph size on the computational cost and reduce the difference between the two planners, as they have approximately the same cost per iteration it will not effect the order. To minimize the effects of the steer parameter on our results, we set it equal to the [[RRT\*]](#id77.77.id77) rewiring radius at each iteration calculated from $\gamma_{RRT} = {1.1\gamma_{RRT}^{\ast}}$, a choice we found improved the performance of [[RRT\*]](#id77.77.id77). As discussed in Section V-A, for Informed [[RRT\*]](#id77.77.id77) we calculated the rewiring radius for the subproblem defined by the current solution using the expression.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Simulations", "weight": 1.0} -->

Experiments varying the width of the problem range, $l$, while keeping a fixed distance between the start and goal show that Informed [[RRT\*]](#id77.77.id77) finds a suitable solution in approximately the same time regardless of the relative size of the problem (Fig. 8). As a result of considering only the informed subset once an initial solution is found, the size of the search space is independent of the planning range (Fig. 6). In contrast, the time needed by [[RRT\*]](#id77.77.id77) to find a similar solution increases as the problem range grows as proportionately more time is spent searching states that cannot improve the solution (Fig. 8).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Simulations", "weight": 1.0} -->

Experiments varying the target solution cost show that Informed [[RRT\*]](#id77.77.id77) is capable of finding near-optimal solutions in significantly fewer iterations than [[RRT\*]](#id77.77.id77) (Fig. 9). The direct sampling of the informed subset increases density around the optimal solution faster than global sampling and therefore increases the probability of improving the solution and further focusing the search. In contrast, [[RRT\*]](#id77.77.id77) has uniform density across the entire planning domain and improving the solution actually *decreases* the probability of finding further improvements (Fig. 6).

<!-- chunk {"id": "body-0062", "role": "body", "section": "Simulations", "weight": 1.0} -->

Experiments varying the height of $h_{g}$ in Fig. 5(b) demonstrate that Informed [[RRT\*]](#id77.77.id77) finds difficult passages that improve the current solution, regardless of their homotopy class, quicker than [[RRT\*]](#id77.77.id77) (Fig. 10). Once again, the result of considering only the informed subset is an increased state density in the region of the planning problem that includes the optimal solution. Compared to global sampling, this increases the probability of sampling within difficult passages, such as narrow gaps between obstacles, decreasing the time necessary to find such solutions (Fig. 7).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Simulations", "weight": 1.0} -->

Finally, experiments on random worlds demonstrate that the improvements of Informed [[RRT\*]](#id77.77.id77) apply to a wide range of planning problems and state dimensions (Fig. 11).

<!-- chunk {"id": "body-0064", "role": "body", "section": "Discussion & Conclusion", "weight": 1.5} -->

In this paper, we discuss that a necessary condition for [[RRT\*]](#id77.77.id77) algorithms to improve a solution is the addition of a state from a subset of the planning problem, $X_{f} \subseteq X$. For problems seeking to minimize path length in ${\mathbb{R}}^{n}$, this subset can be estimated, $X_{\hat{f}} \supseteq X_{f}$, by a prolate hyperspheroid (a special type of hyperellipsoid) with the initial and goal states as focal points. It is shown that the probability of adding a new state from this subset through rejection sampling of a larger set becomes arbitrarily small as the dimension of the problem increases, the size of the sampled set increases, or the solution approaches the theoretical minimum. A simple method to sample $X_{\hat{f}}$ directly is presented that allows for the creation of informed-sampling planners, such as Informed [[RRT\*]](#id77.77.id77).

<!-- chunk {"id": "body-0065", "role": "body", "section": "Discussion & Conclusion", "weight": 1.5} -->

It is shown that Informed [[RRT\*]](#id77.77.id77) outperforms [[RRT\*]](#id77.77.id77) in the ability to find near-optimal solutions in finite time regardless of state dimension without requiring any assumptions about the optimal homotopy class.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Discussion & Conclusion", "weight": 1.5} -->

Informed [[RRT\*]](#id77.77.id77) uses heuristics to shrink the planning problem to subsets of the original domain. This makes it inherently dependent on the current solution cost, as it cannot focus the search when the associated prolate hyperspheroid is larger than the planning problem itself. Similarly, it can only shrink the subset down to the lower bound defined by the optimal solution. We are currently investigating techniques to focus the search without requiring an initial solution. These techniques, such as Batch Informed Trees ([[BIT\*]](#id62.62.id62)), incrementally *increase* the search subset. By doing so, they prioritize the initial search of low-cost solutions.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Discussion & Conclusion", "weight": 1.5} -->

An open motion planning library ([[OMPL]](#id82.82.id82)) implementation of Informed [[RRT\*]](#id77.77.id77) is described at
