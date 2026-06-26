<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fast Marching Tree: A Fast Marching Sampling-Based Method for Optimal Motion Planning in Many Dimensions

Topics include Motion planning, Optimal motion planning, Sampling-based planning, Asymptotic optimality, Fast marching tree, FMT, FMT*, Rapidly-exploring random tree star, Rapidly-exploring random tree, Graph search, Dynamic programming, Fast marching method.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

FMT* operates on a fundamentally different mechanism than RRT*, yet still achieves asymptotic optimality. FMT* can be faster than RRT* in certain planning regimes, and it is more amenable to parallelization (c.f. Group Marching Tree).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we present a novel probabilistic sampling-based motion planning algorithm called the Fast Marching Tree algorithm (FMT*). The algorithm is specifically aimed at solving complex motion planning problems in high-dimensional configuration spaces. This algorithm is proven to be asymptotically optimal and is shown to converge to an optimal solution faster than its state-of-the-art counterparts, chiefly PRM* and RRT*. The FMT* algorithm performs a "lazy" dynamic programming recursion on a predetermined number of probabilistically drawn samples to grow a tree of paths, which moves steadily outward in cost-to-arrive space. As such, this algorithm combines features of both single-query algorithms (chiefly RRT) and multiple-query algorithms (chiefly PRM), and is reminiscent of the Fast Marching Method for the solution of Eikonal equations. As a departure from previous analysis approaches that are based on the notion of almost sure convergence, the FMT* algorithm is analyzed under the notion of convergence in probability: the extra mathematical flexibility of this approach allows for convergence rate bounds—the first in the field of optimal sampling-based motion planning.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Specifically, for a certain selection of tuning parameters and configuration spaces, we obtain a convergence rate bound of order O(n^(-1/d+r), where n is the number of sampled points, d is the dimension of the configuration space, and r is an arbitrarily small constant. We go on to demonstrate asymptotic optimality for a number of variations on FMT*, namely when the configuration space is sampled non-uniformly, when the cost is not arc length, and when connections are made based on the number of nearest neighbors instead of a fixed connection radius. Numerical experiments over a range of dimensions and obstacle configurations confirm our theoretical and heuristic arguments by showing that FMT*, for a given execution time, returns substantially better solutions than either PRM* or RRT*, especially in high-dimensional configuration spaces and in scenarios where collision-checking is expensive.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Probabilistic sampling-based algorithms represent a particularly successful approach to robotic motion planning problems in high-dimensional configuration spaces, which naturally arise, e.g., when controlling the motion of high degree-of-freedom robots or planning under uncertainty. Accordingly, the design of rapidly converging sampling-based algorithms with sound performance guarantees has emerged as a central topic in robotic motion planning and represents the main thrust of this paper.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, the key idea behind probabilistic sampling-based algorithms is to avoid the explicit construction of the configuration space (which can be prohibitive in complex planning problems) and instead conduct a search that probabilistically probes the configuration space with a sampling scheme. This probing is enabled by a collision detection module, which the motion planning algorithm considers as a "black box". Probabilistic sampling-based algorithms may be classified into two categories: multiple-query and single-query. Multiple-query algorithms construct a topological graph called a roadmap, which allows a user to efficiently solve multiple initial-state/goal-state queries. This family of algorithms includes the probabilistic roadmap algorithm (PRM) and its variants, e.g., Lazy-PRM, dynamic PRM, and PRM$^{\ast}$. In single-query algorithms, on the other hand, a single initial-state/goal-state pair is given, and the algorithm must search until it finds a solution, or it may report early failure.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This family of algorithms includes the rapidly exploring random trees algorithm (RRT), the rapidly exploring dense trees algorithm (RDT), and their variants, e.g., RRT$^{\ast}$. Other notable sampling-based planners include expansive space trees (EST), sampling-based roadmap of trees (SRT), rapidly-exploring roadmap (RRM), and the "cross-entropy" planner. Analysis in terms of convergence to feasible or even optimal solutions for multiple-query and single-query algorithms is provided. A central result is that these algorithms provide *probabilistic completeness* guarantees in the sense that the probability that the planner fails to return a solution, if one exists, decays to zero as the number of samples approaches infinity. Recently, it has been proven that both RRT$^{\ast}$and PRM$^{\ast}$are asymptotically optimal, i.e., the cost of the returned solution converges almost surely to the optimum.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Building upon the results, the work in presents an algorithm with provable "sub-optimality" guarantees, which "trades" optimality with faster computation, while the work in presents a variant of RRT$^{\ast}$​, named RRT$^{\#}$​, that is also asymptotically optimal and aims to mitigate the "greediness" of RRT$^{\ast}$​.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Statement of Contributions*: The objective of this paper is to propose and analyze a novel probabilistic motion planning algorithm that is asymptotically optimal and improves upon state-of-the-art asymptotically-optimal algorithms, namely RRT$^{\ast}$and PRM$^{\ast}$. Improvement is measured in terms of the convergence rate to the optimal solution, where convergence rate is interpreted with respect to execution time. The algorithm, named the Fast Marching Tree algorithm ($\text{FMT}^{\ast}$​), is designed to reduce the number of obstacle collision-checks and is particularly efficient in high-dimensional environments cluttered with obstacles. $\text{FMT}^{\ast}$essentially performs a forward dynamic programming recursion on a predetermined number of probabilistically-drawn samples in the configuration space, see Figure 1. The recursion is characterized by three key features, namely it is *tailored* to disk-connected graphs, it *concurrently* performs graph construction and graph search, and it *lazily* skips collision-checks when evaluating local connections.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

This lazy collision-checking strategy may introduce suboptimal connections---the crucial property of $\text{FMT}^{\ast}$is that such suboptimal connections become vanishingly rare as the number of samples goes to infinity. $\text{FMT}^{\ast}$combines features of PRM and SRT (which is similar to RRM) and grows a tree of trajectories like RRT. Additionally, $\text{FMT}^{\ast}$is reminiscent of the Fast Marching Method, one of the main methods for solving stationary Eikonal equations. We refer the reader to and references therein for a recent overview of path planning algorithms inspired by the Fast Marching Method. As in the Fast Marching Method, the main idea is to exploit a heapsort technique to systematically locate the proper sample point to update and to incrementally build the solution in an "outward" direction, so that the algorithm needs never backtrack over previously evaluated sample points.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Such a *one-pass* property is what makes both the Fast Marching Method and $\text{FMT}^{\ast}$(in addition to its lazy strategy) particularly efficient^11^1We note, however, that the Fast Marching Method and $\text{FMT}^{\ast}$differ in a number of important aspects. Chiefly, the Fast Marching Method hinges upon upwind approximation schemes for the solution to the Eikonal equation over orthogonal grids or triangulated domains, while $\text{FMT}^{\ast}$hinges upon the application of the Bellman principle of optimality over a randomized grid within a sampling-based framework..

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The end product of the $\text{FMT}^{\ast}$algorithm is a tree, which, together with the connection to the Fast Marching Method, gives the algorithm its name. Our simulations across a variety of problem instances, ranging in obstacle clutter and in dimension from 2D to 7D, show that $\text{FMT}^{\ast}$outperforms state-of-the-art algorithms such as PRM$^{\ast}$and RRT$^{\ast}$​, often by a significant margin. The speedups are particularly prominent in higher dimensions and in scenarios where collision-checking is expensive, which is exactly the regime in which sampling-based algorithms excel. $\text{FMT}^{\ast}$also presents a number of "structural" advantages, such as maintaining a tree structure at all times and expanding in cost-to-arrive space, which have been recently leveraged to include differential constraints, to provide a bidirectional implementation, and to speed up the convergence rate even further via the inclusion of lower bounds on cost and heuristics.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is important to note that in this paper we use a notion of asymptotic optimality (AO) different from the one used. In, AO is defined through the notion of convergence almost everywhere (a.e.). Explicitly an algorithm is considered AO if the cost of the solution it returns converges a.e. to the optimal cost as the number of samples $n$ approaches infinity. This definition is apt when the algorithm is sequential in $n$, such as RRT$^{\ast}$, in the sense that it requires that with probability 1 the sequence of solutions converges to an optimal one, with the solution at $n + 1$ heavily related to that at $n$. However, for non-sequential algorithms such as PRM$^{\ast}$and $\text{FMT}^{\ast}$​, there is no connection between the solutions at $n$ and $n + 1$. Since these algorithms process all the samples at once, the solution at $n + 1$ is based on $n + 1$ new samples, sampled independently of those used in the solution at $n$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

This motivates the definition of AO used in this paper, which is that the cost of the solution returned by an algorithm must converge *in probability* to the optimal cost. Although convergence in probability is a mathematically weaker notion than convergence a.e. (the latter implies the former), in practice there is no distinction when an algorithm is only run on a predetermined, fixed number of samples. In this case, all that matters is that the probability that the cost of the solution returned by the algorithm is less than an $\varepsilon$ fraction greater than the optimal cost goes to 1 as $n\rightarrow\infty$, for any $\varepsilon > 0$, which is exactly the statement of convergence in probability. Since this convergence is a mathematically weaker, but practically identical condition, we sought to capitalize on the extra mathematical flexibility, and indeed find that our proof of AO for $\text{FMT}^{\ast}$allows for a tighter theoretical lower bound on the search radius of PRM$^{\ast}$than was found.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this regard, an additional important contribution of this paper is the analysis of AO under the notion of convergence in probability, which is of independent interest and could enable the design and analysis of other AO sampling-based algorithms.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most importantly, our proof of AO gives a *convergence rate bound* with respect to the number of sampled points both for $\text{FMT}^{\ast}$and PRM$^{\ast}$---the first in the field of optimal sampling-based motion planning. Specifically, for a certain selection of tuning parameters and configuration space, we derive a convergence rate bound of $O{(n^{{- {1/d}} + \rho})}$, where $n$ is the number of sampled points, $d$ is the dimension of the configuration space, and $\rho$ is an arbitrarily small constant. While the algorithms exhibit the slow convergence rate typical of sampling-based algorithms, the rate is at least a power of $n$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Organization*: This paper is structured as follows. In Section 2 we formally define the optimal path planning problem. In Section 3 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") we present a high-level description of $\text{FMT}^{\ast}$, describe the main intuition behind its correctness, conceptually compare it to existing AO algorithms, and discuss its implementation details. In Section 4 we prove the asymptotic optimality of $\text{FMT}^{\ast}$​, derive convergence rate bounds, and characterize its computational complexity.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 5 we extend $\text{FMT}^{\ast}$along three main directions, namely non-uniform sampling strategies, general cost functions, and a variant of the algorithm that relies on $k$-nearest-neighbor computations. In Section 6 we present results from numerical experiments supporting our statements. Finally, in Section 7, we draw some conclusions and discuss directions for future work.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

Let $\zeta_{d}$ denote the volume of the unit ball in $d$-dimensional Euclidean space. The cardinality of a set $S$ is written as ${card}S$. Given a set $\mathcal{X} \subseteq {\mathbb{R}}^{d}$, $\mu{(\mathcal{X})}$ denotes its $d$-dimensional Lebesgue measure. Finally, the complement of a probabilistic event $A$ is denoted by $A^{c}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

The problem formulation follows closely the problem formulation, with two subtle, yet important differences, namely a notion of regularity for goal regions and a refined definition of path clearance. Specifically, let $\mathcal{X} = {\lbrack 0,\, 1\rbrack}^{d}$ be the configuration space, where the dimension, $d$, is an integer larger than or equal to two. Let $\mathcal{X}_{\text{obs}}$ be the obstacle region, such that $\mathcal{X} \smallsetminus \mathcal{X}_{\text{obs}}$ is an open set (we consider ${\partial\mathcal{X}} \subset \mathcal{X}_{\text{obs}}$). The obstacle-free space is defined as $\mathcal{X}_{\text{free}} = {\text{cl}{({\mathcal{X} \smallsetminus \mathcal{X}_{\text{obs}}})}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

The initial condition $x_{init}$ is an element of $\mathcal{X}_{\text{free}}$, and the goal region $\mathcal{X}_{\text{goal}}$ is an open subset of $\mathcal{X}_{\text{free}}$. A path planning problem is denoted by a triplet $(\mathcal{X}_{\text{free}},x_{init},\mathcal{X}_{\text{goal}})$. A function $\sigma:{{\lbrack 0,1\rbrack}\rightarrow{\mathbb{R}}^{d}}$ is called a *path* if it is continuous and has *bounded variation*, see for a formal definition. In the setup of this paper, namely, for continuous functions on a bounded, one-dimensional domain, bounded variation is exactly equivalent to finite length.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

A goal region $\mathcal{X}_{\text{goal}}$ is said to be *regular* if there exists $\xi > 0$ such that ${\forall x} \in {\partial\mathcal{X}_{\text{goal}}}$, there exists a ball in the goal region, say ${B{(\overline{x};\xi)}} \subseteq \mathcal{X}_{\text{goal}}$, such that $x$ is on the boundary of the ball, i.e., $x \in {\partial{B{(\overline{x};\xi)}}}$. In other words, a regular goal region is a "well-behaved" set where the boundary has bounded curvature. We will say $\mathcal{X}_{\text{goal}}$ is $\xi$-regular if $\mathcal{X}_{\text{goal}}$ is regular for the parameter $\xi$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Such a notion of regularity, not present, is needed because to return a feasible solution, there must be samples in $\mathcal{X}_{\text{goal}}$, and for that solution to be near-optimal, some samples must be near the edge of $\mathcal{X}_{\text{goal}}$ where the optimal path meets it. The notion of $\xi$-regularity essentially formalizes the notion of $\mathcal{X}_{\text{goal}}$ having enough measure near this edge to ensure that points are sampled near it.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Let $\Sigma$ be the set of all paths. A cost function for the planning problem $(\mathcal{X}_{\text{free}},x_{init},\mathcal{X}_{\text{goal}})$ is a function $c:{\Sigma\rightarrow{\mathbb{R}}_{\geq 0}}$ from the set of paths to the set of nonnegative real numbers; in this paper we will mainly consider cost functions $c{(\sigma)}$ that are the *arc length* of $\sigma$ with respect to the Euclidean metric in $\mathcal{X}$ (recall that $\sigma$ is, by definition, rectifiable).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Extension to more general cost functions, potentially not satisfying the triangle inequality are discussed in Section 5.2. The optimal path planning problem is then defined as follows: > Optimal path planning problem: Given a path planning problem $(\mathcal{X}_{\text{free}},x_{init},\mathcal{X}_{\text{goal}})$ with a regular goal region and an arc length function $c:{\Sigma\rightarrow{\mathbb{R}}_{\geq 0}}$, find a feasible path $\sigma^{\ast}$ such that ${c{(\sigma^{\ast})}} = {\min{\{{{c{(\sigma)}}:{\sigma\text{~is feasible}}}\}}}$. If no such path exists, report failure.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Finally, we introduce some definitions concerning the *clearance* of a path, i.e., its "distance" from $\mathcal{X}_{\text{obs}}$. For a given $\delta > 0$, the $\delta$-interior of $\mathcal{X}_{\text{free}}$ is defined as the set of all points that are at least a distance $\delta$ away from any point in $\mathcal{X}_{\text{obs}}$. A collision-free path $\sigma$ is said to have strong $\delta$-clearance if it lies entirely inside the $\delta$-interior of $\mathcal{X}_{\text{free}}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Note this definition is slightly different mathematically than admitting a *robustly optimal solution* as, but the two are nearly identical in practice. Briefly, the difference is necessitated by the definition of a homotopy class only involving pointwise limits, as opposed to limits in bounded variation norm, making the conditions of a robustly optimal solution potentially vacuously satisfied.

<!-- chunk {"id": "body-0028", "role": "body", "section": "The Fast Marching Tree Algorithm ($\\text{FMT}^{\\ast}$​)", "weight": 1.0} -->

In this section we present the Fast Marching Tree algorithm ($\text{FMT}^{\ast}$​). In Section 3.1 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") we provide a high-level description.

<!-- chunk {"id": "body-0029", "role": "body", "section": "The Fast Marching Tree Algorithm ($\\text{FMT}^{\\ast}$​)", "weight": 1.0} -->

In Section 3.2 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") we present some basic properties and discuss the main intuition behind $\text{FMT}^{\ast}$​'s design.

<!-- chunk {"id": "body-0030", "role": "body", "section": "The Fast Marching Tree Algorithm ($\\text{FMT}^{\\ast}$​)", "weight": 1.0} -->

In Section 3.3 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") we conceptually compare $\text{FMT}^{\ast}$to existing AO algorithms and discuss its structural advantages.

<!-- chunk {"id": "body-0031", "role": "body", "section": "The Fast Marching Tree Algorithm ($\\text{FMT}^{\\ast}$​)", "weight": 1.0} -->

Finally, in Section 3.4 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") we provide a detailed description of $\text{FMT}^{\ast}$together with implementation details, which will be instrumental to the computational complexity analysis given in Section 4.3.

<!-- chunk {"id": "body-0032", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

The $\text{FMT}^{\ast}$algorithm performs a forward dynamic programming recursion over a predetermined number of sampled points and correspondingly generates a *tree of paths* by moving steadily outward in cost-to-arrive space (see Figure 1). The dynamic programming recursion performed by $\text{FMT}^{\ast}$is characterized by three key features: It is *tailored* to disk-connected graphs, where two samples are considered *neighbors*, and hence connectable, if their distance is below a given bound, referred to as the *connection radius*.

<!-- chunk {"id": "body-0033", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

It performs graph construction and graph search *concurrently*.

<!-- chunk {"id": "body-0034", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

For the evaluation of the immediate cost in the dynamic programming recursion, the algorithm "lazily" ignores the presence of obstacles, and whenever a locally-optimal (assuming no obstacles) connection to a new sample intersects an obstacle, that sample is simply skipped and left for later as opposed to looking for other connections in the neighborhood.

<!-- chunk {"id": "body-0035", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

The first feature concerns the fact that $\text{FMT}^{\ast}$exploits the structure of disk-connected graphs to run dynamic programming for shortest path computation, in contrast with successive approximation schemes (as employed, e.g., by label-correcting methods). This aspect of the algorithm is illustrated in Section 3.2 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."), in particular, in Theorem 3.2.

<!-- chunk {"id": "body-0036", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

‣ 3.2 Basic Properties and Intuition ‣ 3 The Fast Marching Tree Algorithm ("FMT"^∗​) ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") and Remark 3.3.

<!-- chunk {"id": "body-0037", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

‣ 3.2 Basic Properties and Intuition ‣ 3 The Fast Marching Tree Algorithm ("FMT"^∗​) ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."). An extension of $\text{FMT}^{\ast}$to $k$-nearest-neighbor graphs, which are structurally very similar to disk-connected graphs, is studied in Section 5.3 and numerically evaluated in Section 6. The last feature, which makes the algorithm "lazy" and represents the key innovation, dramatically reduces the number of costly collision-check computations. However, it may cause *suboptimal* connections.

<!-- chunk {"id": "body-0038", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

A central property of $\text{FMT}^{\ast}$is that the cases where a suboptimal connection is made become vanishingly rare as the number of samples goes to infinity, which is key in proving that the algorithm is AO (Sections 3.2 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") and 4).

<!-- chunk {"id": "body-0039", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

0: sample set V comprising of xinit and n samples in 𝒳free, at least one of which is also in 𝒳goal 1: Place xinit in Vopen and all other samples in Vunvisited; initialize tree with root node xinit 2: Find lowest-cost node z in Vopen 3: For each of z’s neighbors x in Vunvisited: 4: Find neighbor nodes y in Vopen 5: Find locally-optimal one-step connection to x from among nodes y 6: If that connection is collision-free, add edge to tree of paths 7: Remove successfully connected nodes x from Vunvisited and add them to Vopen 8: Remove z from Vopen and add it to Vclosed 9: Repeat until either: Vopen is empty ⇒ report failure Lowest-cost node z in Vopen is in 𝒳goal ⇒ return unique path to z and report success Algorithm 1 Fast Marching Tree Algorithm (FMT*​): Basics A basic pseudocode description of $\text{FMT}^{\ast}$is given in Algorithm 1 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium

<!-- chunk {"id": "body-0040", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.").

<!-- chunk {"id": "body-0041", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

The input to the algorithm, besides the path planning problem definition, i.e., ($\mathcal{X}_{\text{free}},x_{init},\mathcal{X}_{\text{goal}}$), is a sample set $V$ comprising $x_{init}$ and $n$ samples in $\mathcal{X}_{\text{free}}$ (line ‣ 1 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")). We refer to samples added to the tree of paths as nodes.

<!-- chunk {"id": "body-0042", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

Two samples ${u,v} \in V$ are considered *neighbors* if their Euclidean distance is smaller than where $\gamma > {2\left({1/d} \right)^{1/d}\left({{\mu{(\mathcal{X}_{\text{free}})}}/\zeta_{d}} \right)^{1/d}}$ is a tuning parameter. The algorithm makes use of a partition of $V$ into three subsets, namely $V_{unvisited}$, $V_{open}$, and $V_{closed}$. The set $V_{unvisited}$ consists of all of the samples that have not yet been considered for addition to the incrementally grown tree of paths.

<!-- chunk {"id": "body-0043", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

The set $V_{open}$ contains samples that are currently active, in the sense that they have already been added to the tree (i.e., a collision-free path from $x_{init}$ with a given cost-to-arrive has been found) and are candidates for further connections to samples in $V_{unvisited}$. The set $V_{closed}$ contains samples that have been added to the tree and are no longer considered for any new connections. Intuitively, these samples are not near enough to the edge of the expanding tree to actually have any new connections made with $V_{unvisited}$. Removing them from $V_{open}$ reduces the number of nodes that need to be considered as neighbors for sample $x$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

The $\text{FMT}^{\ast}$algorithm initially places $x_{init}$ into $V_{open}$ and all other samples in $V_{unvisited}$, while $V_{closed}$ is initially empty (line 1 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")).

<!-- chunk {"id": "body-0045", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

The algorithm then progresses by extracting the node with the lowest cost-to-arrive in $V_{open}$ (line 2 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."), Figure 2(a) ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")), call it

<!-- chunk {"id": "body-0046", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

$z$, and finds all its neighbors within $V_{unvisited}$, call them $x$ samples (line 3 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."), Figure 2(a) ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")).

<!-- chunk {"id": "body-0047", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

For each sample $x$, $\text{FMT}^{\ast}$finds all its neighbors within $V_{open}$, call them $y$ nodes (line 4 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."), Figure 2(b) ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and

<!-- chunk {"id": "body-0048", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

The algorithm then evaluates the cost of all paths to $x$ obtained by concatenating previously computed paths to nodes $y$ with straight lines connecting them to $x$, referred to as "local one-step" connections. Note that this step *lazily* ignores the presence of obstacles.

<!-- chunk {"id": "body-0049", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

$\text{FMT}^{\ast}$then picks the path with lowest cost-to-arrive to $x$ (line 5 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."), Figure 2(b) ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")).

<!-- chunk {"id": "body-0050", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

If the last edge of this path, i.e., the one connecting $x$ with one of its neighbors in $V_{open}$, is collision-free, then it is added to the tree (line 6 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."), Figure 2(c) ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of

<!-- chunk {"id": "body-0051", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

"FMT"^∗​, and a larger set of numerical experiments.")).

<!-- chunk {"id": "body-0052", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

When all samples $x$ have been considered, the ones that have been successfully connected to the tree are added to $V_{open}$ and removed from $V_{unvisited}$ (line 7 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."), Figure 2(d) ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of

<!-- chunk {"id": "body-0053", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

"FMT"^∗​, and a larger set of numerical experiments.")), while the others remain in $V_{unvisited}$ until a further iteration of the algorithm^22^2In this paper we consider a batch implementation, whereby all successfully connected $x$ are added to $V_{open}$ in batch *after* all the samples $x$ have been considered.

<!-- chunk {"id": "body-0054", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

It is easy to show that if, instead, each sample $x$ were added to $V_{open}$ as soon as its obstacle-free connection was found, then with probability 1, the algorithm would make all the same connections as in the batch setting, regardless of what order the $x$ were considered. Thus, since adding the samples $x$ serially or in batch makes no difference to the algorithm's output, we prefer the batch implementation for its simplicity and parallelizability..

<!-- chunk {"id": "body-0055", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

Additionally, node $z$ is inserted into $V_{closed}$ (line 8 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."), Figure 2(d) ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")), and

<!-- chunk {"id": "body-0056", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

$\text{FMT}^{\ast}$moves to the next iteration (an iteration comprises lines 2 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")--8 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")).

<!-- chunk {"id": "body-0057", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

The algorithm terminates when the lowest-cost node in $V_{open}$ is also in the goal region or when $V_{open}$ becomes empty. Note that at the beginning of each iteration every sample in $V$ is either in $V_{open}$ *or* in $V_{unvisited}$ *or* in $V_{closed}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

A few comments are in order. First, the choice of the connection radius relies on a trade-off between computational complexity (roughly speaking, more neighbors lead to more computation) and quality of the computed path (roughly speaking, more neighbors lead to more paths to optimize over), and is an important parameter in the analysis and implementation of $\text{FMT}^{\ast}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

This choice will be studied theoretically in Section 4 and numerically in Section 6.3.2. Second, as shown in Figure 2 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."), $\text{FMT}^{\ast}$concurrently performs graph construction and graph search, which is carried out via a dynamic programming recursion tailored to disk graphs (see Section 3.2 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to

<!-- chunk {"id": "body-0060", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")).

<!-- chunk {"id": "body-0061", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

This recursion lazily skips collision-checks and may indeed introduce *suboptimal* connections. In Section 3.2 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") we will intuitively discuss why such suboptimal connections are very rare and still allow the algorithm to asymptotically approach an optimal solution (Theorem 4.1.

<!-- chunk {"id": "body-0062", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

‣ 4.1 Asymptotic Optimality ‣ 4 Analysis of "FMT"^∗ ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")). Third, the lazy collision-checking strategy employed by $\text{FMT}^{\ast}$is fundamentally different from the one proposed in the past within the probabilistic roadmap framework,. Specifically, the lazy $PRM$ algorithm presented in first constructs a graph assuming that all connections are collision-free (refer to this graph as the *optimistic graph*). Then, it searches for a shortest *collision-free* path by repeatedly searching for a shortest path over the optimistic graph and then checking whether it is collision-free or not.

<!-- chunk {"id": "body-0063", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

Each time a collision is found, the corresponding edge is removed from the optimistic graph and a new shortest path is computed. The "Single-query, Bi-directional, Lazy in collision-checking" algorithm, $SBL$, implements a similar idea within the context of bidirectional search. In contrast to lazy $PRM$ and $SBL$, $\text{FMT}^{\ast}$*concurrently* performs graph construction and graph search, and as soon as a shortest path to the goal region is found, that path is guaranteed to be collision-free. This approach provides computational savings in especially cluttered environments, wherein lazy PRM-like algorithms will require a large number of attempts to find a collision-free shortest path.

<!-- chunk {"id": "body-0064", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

(a) Lines 2–3: FMT*selects the lowest-cost node z from set Vopen and finds its neighbors within Vunvisited.

<!-- chunk {"id": "body-0065", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

(b) Lines 4–5: given a neighboring node x, FMT*finds the neighbors of x within Vopen and searches for a locally-optimal one-step connection. Note that paths intersecting obstacles are also lazily considered.

<!-- chunk {"id": "body-0066", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

(c) Line 6: FMT*selects the locally-optimal one-step connection to x ignoring obstacles, and adds that connection to the tree if it is collision-free.

<!-- chunk {"id": "body-0067", "role": "body", "section": "High-Level Description", "weight": 1.0} -->

(d) Lines 7–8: After all neighbors of z in Vunvisited have been explored, FMT*adds successfully connected nodes to Vopen, places z in Vclosed, and moves to the next iteration.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Basic Properties and Intuition", "weight": 1.0} -->

This section discusses basic properties of the $\text{FMT}^{\ast}$algorithm and provides intuitive reasoning about its correctness and effectiveness. We start by showing that the algorithm terminates in at most $n$ steps, where $n$ is the number of samples.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 3.3 ( $\\text{FMT}^{\\ast}$​​, dynamic programming, and disk-graphs)", "weight": 1.0} -->

The functional equation (1 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")) does not constitute an algorithm, it only stipulates an optimality condition.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Remark 3.3 ( $\\text{FMT}^{\\ast}$​​, dynamic programming, and disk-graphs)", "weight": 1.0} -->

$\text{FMT}^{\ast}$implements equation (1 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")) by exploiting the structure of disk-connected graphs.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Remark 3.3 ( $\\text{FMT}^{\\ast}$​​, dynamic programming, and disk-graphs)", "weight": 1.0} -->

Specifically, in the obstacle-free case, the disk-connectivity structure ensures that $\text{FMT}^{\ast}$visits nodes in a ordering compatible with directly computing (1 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")), that is, while computing the left hand side of equation (1 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of

<!-- chunk {"id": "body-0072", "role": "body", "section": "Remark 3.3 ( $\\text{FMT}^{\\ast}$​​, dynamic programming, and disk-graphs)", "weight": 1.0} -->

"FMT"^∗​, and a larger set of numerical experiments.")) (i.e., the shortest path value $c{(v)}$), all the relevant shortest path values on the right hand side (i.e., the values $c{(u)}$) have already been computed (see proof of Invariant 2).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Remark 3.3 ( $\\text{FMT}^{\\ast}$​​, dynamic programming, and disk-graphs)", "weight": 1.0} -->

In this sense, $\text{FMT}^{\ast}$computes shortest paths by running direct dynamic programming, as opposed to performing successive approximations as done by label-setting or label-correcting algorithms, e.g., Dijkstra's algorithm or the Bellman--Ford algorithm. We refer the reader to Sniedovich for an in-depth discussion of the differences between direct dynamic programming methods (such as $\text{FMT}^{\ast}$​) and successive approximation methods (such as Dijkstra's algorithm) for shortest path computation. Such a direct approach is desirable since the cost-to-arrive value for each node is updated only once, and thus only one collision check is required per node in the obstacle-free case. When obstacles are introduced, $\text{FMT}^{\ast}$sacrifices the ability to return an exact solution on the obstacle-free disk graph in order to retain the computational efficiency of the direct approach. The suboptimality introduced in this way is slight, as we prove in Section 4, and only one collision check is required for the majority of nodes.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Remark 3.3 ( $\\text{FMT}^{\\ast}$​​, dynamic programming, and disk-graphs)", "weight": 1.0} -->

$\text{FMT}^{\ast}$​​'s strategy is reminiscent of the approach used for the computation of shortest paths over acyclic graphs. Indeed, the idea of leveraging graph structure to compute shortest paths over disk graphs is not new and was recently investigated in ---under the name of bounded leg shortest path problem---and. Both works, however, do not use "direct" dynamic programming arguments, but rather combine Dijkstra's algorithm with the concept of bichromatic closest pairs.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Remark 3.3 ( $\\text{FMT}^{\\ast}$​​, dynamic programming, and disk-graphs)", "weight": 1.0} -->

Theorem 3.2. ‣ 3.2 Basic Properties and Intuition ‣ 3 The Fast Marching Tree Algorithm ("FMT"^∗​) ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") shows that in the obstacle-free case $\text{FMT}^{\ast}$returns a shortest path, if one exists, over the $r_{n}$-disk graph induced by the sample set $V$. This statement no longer holds, however, when there are obstacles, as in this case $\text{FMT}^{\ast}$might make connections that are suboptimal, i.e., that do not satisfy the Bellman principle of optimality.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Remark 3.3 ( $\\text{FMT}^{\\ast}$​​, dynamic programming, and disk-graphs)", "weight": 1.0} -->

Specifically, $\text{FMT}^{\ast}$will make a suboptimal connection when exactly four conditions are satisfied. Let $u_{1}$ be the optimal parent of $x$ with respect to the $r_{n}$-disk graph where edges intersecting obstacles are removed. This graph is the "correct" graph $\text{FMT}^{\ast}$should plan over if it were not lazy.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Remark 3.3 ( $\\text{FMT}^{\\ast}$​​, dynamic programming, and disk-graphs)", "weight": 1.0} -->

The sample $x$ will not be connected to $u_{1}$ by $\text{FMT}^{\ast}$only if when $u_{1}$ is the lowest-cost node in $V_{open}$, there is another node $u_{2} \in V_{open}$ such that (a) $u_{2}$ is within a radius $r_{n}$ of $x$, (b) $u_{2}$ has greater cost-to-arrive than $u_{1}$, (c) obstacle-free connection of $x$ to $u_{2}$ would have lower cost-to-arrive than connection to $u_{1}$, and (d) $u_{2}$ is blocked from connecting to $x$ by an obstacle.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Remark 3.3 ( $\\text{FMT}^{\\ast}$​​, dynamic programming, and disk-graphs)", "weight": 1.0} -->

These four conditions are illustrated in Figure 3 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."). Condition (a) is required because in order for $u_{2}$ to be connected to $x$, it must be within the connection radius of $x$. Conditions (b), (c), and (d) combine as follows: condition (b) dictates that $u_{1}$ will be pulled from $V_{open}$ before $u_{2}$ is. Due to (c), $u_{2}$ will be chosen as the potential parent of $x$.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Remark 3.3 ( $\\text{FMT}^{\\ast}$​​, dynamic programming, and disk-graphs)", "weight": 1.0} -->

Condition (d) will cause the algorithm to discard the edge between them, and $u_{1}$ will be removed from $V_{open}$, never to be evaluated again. Thus, in the future, the algorithm will never realize that $u_{1}$ was a better parent for $x$. If condition (b) were to fail, then $u_{2}$ would be pulled from $V_{open}$ first, would unsuccessfully attempt to connect to $x$, and then would be removed from $V_{open}$, leaving $x$ free to connect to $u_{1}$ in a future iteration. If condition (c) were to fail, the algorithm would attempt to connect $x$ to $u_{1}$ instead of $u_{2}$ and would therefore find the optimal connection. If condition (d) were to fail, then $u_{2}$ would indeed be the optimal parent of $x$, and so the optimal connection would be formed.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Remark 3.3 ( $\\text{FMT}^{\\ast}$​​, dynamic programming, and disk-graphs)", "weight": 1.0} -->

Thus, if any of one these four conditions fail, then at some iteration (possibly not the first), $x$ will be connected optimally with respect to the "correct" graph. Note that the combination of conditions (a), (b), (c), and (d) make such suboptimal connections quite rare. Additionally, samples must be within distance $r_{n}$ of an obstacle to achieve joint satisfaction of conditions (a), (b), (c), and (d), and Lemma C.2. ‣ Proof of Theorem 4.7.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Remark 3.3 ( $\\text{FMT}^{\\ast}$​​, dynamic programming, and disk-graphs)", "weight": 1.0} -->

‣ Appendix C Proof of Computational Complexity ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") shows that the fraction of samples which lie within $r_{n}$ of an obstacle goes to zero as $n\rightarrow\infty$. Furthermore, Theorem 4.1.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Remark 3.3 ( $\\text{FMT}^{\\ast}$​​, dynamic programming, and disk-graphs)", "weight": 1.0} -->

‣ 4.1 Asymptotic Optimality ‣ 4 Analysis of "FMT"^∗ ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") shows that such suboptimal connections do not affect the AO of $\text{FMT}^{\ast}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Conceptual Comparison with Existing AO Algorithms and Advantages of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

When there are no obstacles, $\text{FMT}^{\ast}$reports the exact same solution or failure as PRM$^{\ast}$. This property follows from the fact that, without obstacles, $\text{FMT}^{\ast}$is indeed using dynamic programming to build the minimum-cost spanning tree, as shown in Theorem 3.2. ‣ 3.2 Basic Properties and Intuition ‣ 3 The Fast Marching Tree Algorithm ("FMT"^∗​) ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.").

<!-- chunk {"id": "body-0084", "role": "body", "section": "Conceptual Comparison with Existing AO Algorithms and Advantages of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

With obstacles, for a given sample set, $\text{FMT}^{\ast}$finds a path with a cost that is lower-bounded, and does not substantially exceed, the cost of the path found by PRM$^{\ast}$​, due to the suboptimal connections made by lazily ignoring obstacles in the dynamic programming recursion. However, as will be shown in Theorem 4.1.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Conceptual Comparison with Existing AO Algorithms and Advantages of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

‣ 4.1 Asymptotic Optimality ‣ 4 Analysis of "FMT"^∗ ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."), the cases where $\text{FMT}^{\ast}$makes a suboptimal connection are rare enough that as $n\rightarrow\infty$, $\text{FMT}^{\ast}$​, like PRM$^{\ast}$​, converges to an optimal solution. While lazy collision-checking might introduce suboptimal connections, it leads to a key computational advantage.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Conceptual Comparison with Existing AO Algorithms and Advantages of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

By only checking for collision on the locally-optimal (assuming no obstacles) one-step connection, as opposed to every possible connection as is done in PRM$^{\ast}$​, $\text{FMT}^{\ast}$saves a large number of costly collision-check computations. Indeed, the ratio of the number of collision-check computations in $\text{FMT}^{\ast}$to those in PRM$^{\ast}$goes to zero as the number of samples goes to infinity. Hence, we expect $\text{FMT}^{\ast}$to outperform PRM$^{\ast}$in terms of solution cost as a function of time.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Conceptual Comparison with Existing AO Algorithms and Advantages of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

A conceptual comparison to RRT$^{\ast}$is more difficult, given how differently RRT$^{\ast}$generates paths as compared with $\text{FMT}^{\ast}$​. The graph expansion procedure of RRT$^{\ast}$is fundamentally different from that of $\text{FMT}^{\ast}$​. While $\text{FMT}^{\ast}$samples points throughout the free space and makes connections independently of the order in which the samples are drawn, at each iteration RRT$^{\ast}$steers towards a new sample only from the regions it has reached up until that time. In problems where the solution path is necessarily long and winding it may take a long time for an ordered set of points traversing the path to present steering targets for RRT$^{\ast}$​. In this case, a lot of time can be wasted by steering in inaccessible directions before a feasible solution is found.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Conceptual Comparison with Existing AO Algorithms and Advantages of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

Additionally, even once the search trees for both algorithms have explored the whole space, one may expect $\text{FMT}^{\ast}$to show some improvement in solution quality per number of samples placed. This improvement comes from the fact that, for a given set of samples, $\text{FMT}^{\ast}$creates connections nearly optimally (exactly optimally when there are no obstacles) within the radius constraint, while RRT$^{\ast}$​, even with its rewiring step, is fundamentally a greedy algorithm. It is, however, hard to conceptually assess how long the algorithms might take to run on a given set of samples, although in terms of collision-check computations, we will show in Lemma C.2. ‣ Proof of Theorem 4.7.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Conceptual Comparison with Existing AO Algorithms and Advantages of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

‣ Appendix C Proof of Computational Complexity ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") that $\text{FMT}^{\ast}$performs $O{}$ collision-checks per sample, while RRT$^{\ast}$performs $O{({\log{(n)}})}$ per sample. In Section 6.2 we will present results from numerical experiments to make these conceptual comparisons concrete and assess the benefits of $\text{FMT}^{\ast}$over RRT$^{\ast}$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Conceptual Comparison with Existing AO Algorithms and Advantages of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

An effective approach to address the greedy behavior of RRT$^{\ast}$is to leverage *relaxation methods* for the exploitation of new connections. This approach is the main idea behind the RRT$^{\#}$algorithm, which constructs a spanning tree rooted at the initial condition and containing lowest-cost path information for nodes which have the potential to be part of a shortest path to the goal region. This approach is also very similar to what is done by $\text{FMT}^{\ast}$​.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Conceptual Comparison with Existing AO Algorithms and Advantages of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

However, RRT$^{\#}$grows the tree in a fundamentally different way, by interleaving the addition of new nodes and corresponding edges to the graph with a Gauss--Seidel relaxation of the Bellman equation (1 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")); it is essentially the same relaxation used in the ${LPA}^{\ast}$ algorithm. This last step propagates the new information gained with a node addition across the *whole* graph in order to improve the cost-to-arrive values of "promising" nodes.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Conceptual Comparison with Existing AO Algorithms and Advantages of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

In contrast, $\text{FMT}^{\ast}$directly implements the Bellman equation (1 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")) and, whenever a new node is added to the tree, considers only *local*, i.e. within a neighborhood, connections.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Conceptual Comparison with Existing AO Algorithms and Advantages of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

Furthermore, and perhaps most importantly, $\text{FMT}^{\ast}$implements a lazy collision-checking strategy, which on the practical side may significantly reduce the number of costly collision-checks, while on the theoretical side requires a careful analysis of possible suboptimal local connections (see Section 3.2 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") and Theorem 4.1.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Conceptual Comparison with Existing AO Algorithms and Advantages of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

‣ 4.1 Asymptotic Optimality ‣ 4 Analysis of "FMT"^∗ ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")). It is also worth mentioning that over $n$ samples $\text{FMT}^{\ast}$has a computational complexity that is $O{({n{\log n}})}$ (Theorem 4.7.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Conceptual Comparison with Existing AO Algorithms and Advantages of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

‣ 4.3 Computational Complexity ‣ 4 Analysis of "FMT"^∗ ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")), while RRT$^{\#}$has a computational complexity of $O{({n^{2}{\log n}})}$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Conceptual Comparison with Existing AO Algorithms and Advantages of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

Besides providing fast convergence to high quality solutions, $\text{FMT}^{\ast}$has some "structural" advantages with respect to its state-of-the-art counterparts. First, $\text{FMT}^{\ast}$​, like PRM$^{\ast}$​, relies on the choice of two parameters, namely the number of samples and the constant appearing in the connection radius in equation (3. ‣ 4.1 Asymptotic Optimality ‣ 4 Analysis of "FMT"^∗ ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")).

<!-- chunk {"id": "body-0097", "role": "body", "section": "Conceptual Comparison with Existing AO Algorithms and Advantages of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

In contrast, RRT$^{\ast}$requires the choice of four parameters, namely, the number of samples or termination time, the steering radius, the goal biasing, and the constant appearing in the connection radius. An advantage of $\text{FMT}^{\ast}$over PRM$^{\ast}$​, besides the reduction in the number of collision-checks (see Section 3.1 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")), is that $\text{FMT}^{\ast}$builds and maintains paths in a tree structure at *all times*, which is advantageous when differential constraints are added to the paths.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Conceptual Comparison with Existing AO Algorithms and Advantages of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

In particular, far fewer two-point boundary value problems need to be solved (see the recent work in ). Also, the fact that the tree grows in cost-to-arrive space simplifies a bidirectional implementation, as discussed. Finally, while $\text{FMT}^{\ast}$​, by running on a *predetermined* number of samples, is *not* an anytime algorithm (roughly speaking, an algorithm is called anytime if, given extra time, it continues to run and further improve its solution until time runs out---a notable example is RRT$^{\ast}$​), it can be cast into this framework by repeatedly adding batches of samples and carefully reusing previous computation until time runs out, as recently presented.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Conceptual Comparison with Existing AO Algorithms and Advantages of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

2 Vunvisited ← V ∖ {xinit}; Vopen ← {xinit}, Vclosed ← ⌀ 13 ymin ← arg miny ∈ Ynear{c (y) + Cost (y, x)} // dynamic programming equation 14 if CollisionFree (ymin, x) then 15 E ← E ∪ {(ymin, x)} // straight line joining ymin and x is collision-free 16 Vopen, new ← Vopen, new ∪ {x} 18 c (x) = c (ymin) + Cost (ymin, x) // cost-to-arrive from xinit in tree T = (Vopen ∪ Vclosed, E) 21 Vopen ← (Vopen ∪ Vopen, new) ∖ {z} 26 z ← arg miny ∈ Vopen{c (y)} 28 return Path (z, T = (Vopen ∪ Vclosed, E)) Algorithm 2 Fast Marching Tree Algorithm (FMT*): Details

<!-- chunk {"id": "body-0100", "role": "body", "section": "Detailed Description and Implementation Details", "weight": 1.0} -->

This section provides a detailed pseudocode description of Algorithm 1 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."), which highlights a number of implementation details that will be instrumental to the computational complexity analysis given in Section 4.3.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Detailed Description and Implementation Details", "weight": 1.0} -->

Let $\text{SampleFree}{(n)}$ be a function that returns a set of $n \in {\mathbb{N}}$ points (samples) sampled independently and identically from the uniform distribution on $\mathcal{X}_{\text{free}}$. We discuss the extension to non-uniform sampling distributions in Section 5.1. Let $V$ be a set of samples containing the initial state $x_{init}$ and a set of $n$ points sampled according to $\text{SampleFree}{(n)}$. Given a subset $V' \subseteq V$, and a sample $v \in V$, let $\text{Save}{(V',v)}$ be a function that stores in memory a set of samples $V'$ associated with sample $v$.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Detailed Description and Implementation Details", "weight": 1.0} -->

Given a set of samples $V$, a sample $v \in V$, and a positive number $r$, let $\text{Near}{(V,v,r)}$ be a function that returns the set of samples $\{{u \in V}:{{\|{u - v}\|} < r}\}$. Near checks first to see if the required set of samples has already been computed and saved using Save, in which case it loads the set from memory, otherwise it computes the required set from scratch. Paralleling the notation in the proof of Theorem 3.2.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Detailed Description and Implementation Details", "weight": 1.0} -->

‣ 3.2 Basic Properties and Intuition ‣ 3 The Fast Marching Tree Algorithm ("FMT"^∗​) ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."), given a tree $T = {(V',E)}$, where the node set $V' \subseteq V$ contains $x_{init}$ and $E$ is the edge set, and a node $v \in V'$, let $c{(v)}$ be the cost of the unique path in the graph $T$ from $x_{\text{init}}$ to $v$.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Detailed Description and Implementation Details", "weight": 1.0} -->

Given two samples ${u,v} \in V$, let $\text{Cost}{(u,v)}$ be the cost of the *straight line* joining $u$ and $v$ (in the current setup ${\text{Cost}{(u,v)}} = {\|{v - u}\|}$, more general costs will be discussed in Section 5.2). Note that $\text{Cost}{(u,v)}$ is well-defined regardless of the line joining $u$ and $v$ being collision-free. Given two samples ${u,v} \in V$, let $\text{CollisionFree}{(u,v)}$ denote the boolean function which is true if and only if the line joining $u$ and $v$ does not intersect an obstacle.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Detailed Description and Implementation Details", "weight": 1.0} -->

Given a tree $T = {(V',E)}$, where the node set $V' \subseteq V$ contains $x_{init}$ and $E$ is the edge set, and a node $v \in V'$, let $\text{Path}{(v,T)}$ be the function returning the unique path in the tree $T$ from $x_{\text{init}}$ to $v$. The detailed $\text{FMT}^{\ast}$ algorithm is given in Algorithm 2 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.").

<!-- chunk {"id": "body-0106", "role": "body", "section": "Detailed Description and Implementation Details", "weight": 1.0} -->

The set $V_{open}$ should be implemented as a binary min heap, ordered by cost-to-arrive, with a parallel set of nodes that exactly tracks the nodes in $V_{open}$ in no particular order, and that is used to efficiently carry out the intersection operation in line 12 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") of the algorithm.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Detailed Description and Implementation Details", "weight": 1.0} -->

Set $V_{{open},{new}}$ contains successfully connected $x$ samples that will be added to $V_{open}$ once all $x$ samples have been considered (compare with line 7 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") in Algorithm 1 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​,

<!-- chunk {"id": "body-0108", "role": "body", "section": "Detailed Description and Implementation Details", "weight": 1.0} -->

and a larger set of numerical experiments.")).

<!-- chunk {"id": "body-0109", "role": "body", "section": "Detailed Description and Implementation Details", "weight": 1.0} -->

At initialization (line 5 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")) and during the main while loop (line 11 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")), $\text{FMT}^{\ast}$saves the information regarding the nearest neighbor set

<!-- chunk {"id": "body-0110", "role": "body", "section": "Detailed Description and Implementation Details", "weight": 1.0} -->

This operation is needed to avoid unnecessary repeated computations of near neighbors by allowing the Near function to load from memory, and will be important for the characterization of the computational complexity of $\text{FMT}^{\ast}$in Theorem 4.7. ‣ 4.3 Computational Complexity ‣ 4 Analysis of "FMT"^∗ ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.").

<!-- chunk {"id": "body-0111", "role": "body", "section": "Detailed Description and Implementation Details", "weight": 1.0} -->

Substituting lines 10 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")--12 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") with the line

<!-- chunk {"id": "body-0112", "role": "body", "section": "Detailed Description and Implementation Details", "weight": 1.0} -->

$Y_{near}\leftarrow{\text{Near}{(V_{open},x,r_{n})}}$, while algorithmically correct, would cause a larger number of unnecessary near neighbor computations.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Detailed Description and Implementation Details", "weight": 1.0} -->

Additionally, for each node $u \in N_{v}$, one should also save the real value $\text{Cost}{(u,v)}$ and the boolean value $\text{CollisionFree}{(u,v)}$. Saving both of these values whenever they are first computed guarantees that $\text{FMT}^{\ast}$will never compute them more than once for a given pair of nodes.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Analysis of $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

In this section we characterize the asymptotic optimality of $\text{FMT}^{\ast}$(Section 4.1), provide a convergence rate to the optimal solution (Section 4.2), and finally characterize its computational complexity (Section 4.3).

<!-- chunk {"id": "body-0115", "role": "body", "section": "Asymptotic Optimality", "weight": 1.0} -->

The following theorem presents the main result of this paper.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Remark 4.5 (Application of Theorem 4.1. ‣ 4.1 Asymptotic Optimality ‣ 4 Analysis of \"FMT\"^∗ ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the \"FMT\"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of \"FMT\"^∗​, and a larger set of numerical experiments.\") to PRM$^{\\ast}$​)", "weight": 1.0} -->

Since the solution returned by $\text{FMT}^{\ast}$is never better than the one returned by PRM$^{\ast}$on a given set of nodes, the exact same result holds for PRM$^{\ast}$​. Note that this proof uses a $\gamma$ which is a factor of ${({d + 1})}^{1/d}$ smaller, and thus a $r_{n}$ which is ${({d + 1})}^{1/d}$ smaller, than that in Karaman and Frazzoli. Since the number of cost computations and collision-checks scales approximately as $r_{n}^{d}$, this factor should reduce run time substantially for a given number of nodes, especially in high dimensions. This reduction is due to the difference in definitions of AO mentioned earlier which, again, makes no practical difference for PRM$^{\ast}$or $\text{FMT}^{\ast}$.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Convergence Rate", "weight": 1.0} -->

In this section we provide a convergence rate bound for $\text{FMT}^{\ast}$(and thus also for PRM$^{\ast}$​), *assuming no obstacles*. As far as the authors are aware, this bound is the first such convergence rate result for an optimal sampling-based motion planning algorithm and represents an important step towards understanding the behavior of this class of algorithms. The proof is deferred to Appendix B.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Computational Complexity", "weight": 1.0} -->

The following theorem, proved in Appendix C, characterizes the computational complexity of $\text{FMT}^{\ast}$with respect to the number of samples. It shows that $\text{FMT}^{\ast}$requires $O{({n{\log{(n)}}})}$ operations in expectation, the same as PRM$^{\ast}$and RRT$^{\ast}$​. It also highlights the computational savings of $\text{FMT}^{\ast}$over PRM$^{\ast}$​, since in expectation $\text{FMT}^{\ast}$checks for edge collisions just $O{(n)}$ times, while PRM$^{\ast}$does so $O{({n{\log{(n)}}})}$ times. Ultimately, the most relevant complexity measure is how long it takes for an algorithm to return a solution of a certain quality. This measure, partially characterized in Section 4.2, will be studied numerically in Section 6.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Extensions", "weight": 1.0} -->

This section presents three extensions to the setup considered in the previous section, namely, non-uniform sampling strategies, general cost functions instead of arc length, and a version of $\text{FMT}^{\ast}$​, named $k$-nearest $\text{FMT}^{\ast}$​, in which connections are sought to $k$ nearest-neighbor nodes, rather than to nodes within a given distance.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Extensions", "weight": 1.0} -->

For all three cases we discuss the changes needed to the baseline $\text{FMT}^{\ast}$algorithm presented in Algorithm 2 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") and then argue how $\text{FMT}^{\ast}$with these changes retains AO in Appendices D--F. In the interest of brevity, we will only discuss the required modifications to existing theorems, rather than proving everything from scratch.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Overview", "weight": 1.0} -->

Sampling nodes from a non-uniform distribution can greatly help planning algorithms by incorporating outside knowledge of the optimal path into the algorithm itself. (Of course if no outside knowledge exists, the uniform distribution may be a natural choice.) Specifically, we consider the setup whereby $\text{SampleFree}{(n)}$ returns $n$ points sampled independently and identically from a probability density function $\varphi$ supported over $\mathcal{X}_{\text{free}}$. We assume that $\varphi$ is bounded below by a strictly positive number $\ell$. This lower bound on $\varphi$ allows us to make a connection between sampling from a non-uniform distribution and sampling from a uniform distribution, for which the proof of AO already exists (Theorem 4.1.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Overview", "weight": 1.0} -->

‣ 4.1 Asymptotic Optimality ‣ 4 Analysis of "FMT"^∗ ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")). This argument is worked through in Appendix D to show that $\text{FMT}^{\ast}$with non-uniform sampling is AO.

<!-- chunk {"id": "body-0123", "role": "body", "section": "General Costs", "weight": 1.0} -->

Another extension of interest is when the cost function is not as simple as arc length. We may, for instance, want to consider some regions as more costly to move through than others, or a cost that weights/treats movement along different dimensions differently. In the following subsections, we explain how $\text{FMT}^{\ast}$can be extended to other metric costs, as well as line integral costs, and why its AO still holds.

<!-- chunk {"id": "body-0124", "role": "body", "section": "General Costs", "weight": 1.0} -->

Broadly speaking, the main change that needs to happen to $\text{FMT}^{\ast}$​'s implementation is that it needs to consider *cost* instead of Euclidean distance when searching for nearby points. For metric costs besides Euclidean cost (Section 5.2.1), a few adjustments to the constants are all that is needed in order to ensure AO. This is because the proof of AO in Theorem 4.1. ‣ 4.1 Asymptotic Optimality ‣ 4 Analysis of "FMT"^∗ ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") relies on the cost being additive and obeying the triangle inequality.

<!-- chunk {"id": "body-0125", "role": "body", "section": "General Costs", "weight": 1.0} -->

The same can be said for line integral costs *if* $\text{FMT}^{\ast}$is changed to search along and connect points by cost-optimal paths instead of straight lines (Section 5.2.2). Since such an algorithm may be hard to implement in practice, we lastly show in Section 5.2.3 that by making some Lipschitz assumptions on the cost function, we get an approximate triangle inequality for straight-line, cost-weighted connections. We present an argument for why this approximation is sufficiently good to ensure that the suboptimality introduced in how parent nodes are chosen and in the edges themselves goes to zero asymptotically, and thus that AO is retained. All arguments for AO in this subsection are deferred to Appendix E.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Metric Costs", "weight": 1.0} -->

Overview: Consider as cost function any metric on $\mathcal{X}$, denoted by $\text{dist}:{{\mathcal{X} \times \mathcal{X}}\rightarrow{\mathbb{R}}}$. If the distance between points in $\mathcal{X}$ is measured according to dist, the $\text{FMT}^{\ast}$algorithm requires very minor modifications, namely just a modified version of the Near function. Generalized metric costs allow one to account, e.g., different weightings on different dimensions, or an angular dimension which wraps around at $2\pi$.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Metric Costs", "weight": 1.0} -->

Changes to $\text{FMT}^{\ast}$​'s implementation: Given two samples ${u,v} \in V$, ${\text{Cost}{(u,v)}} = {\text{dist}{(u,v)}}$. Accordingly, given a set of samples $V$, a sample $v \in V$, and a positive number $r$, $\text{Near}{(V,v,r)}$ returns the set of samples $\{{u \in V}:{{\text{Cost}{(u,v)}} < r}\}$. We refer to such sets as *cost balls*.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Metric Costs", "weight": 1.0} -->

Formally, everything else in Algorithm 2 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") stays the same, except $\zeta_{d}$ in the definition of $r_{n}$ needs to be defined as the Lebesgue measure of the unit cost-ball.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Line Integral Costs with Optimal-Path Connections", "weight": 1.0} -->

Overview: In some planning problems the cost function may not be a metric, i.e., it may not obey the triangle inequality. Specifically, consider the setup where $f:{\mathcal{X}\rightarrow{\mathbb{R}}}$ is such that $0 < f_{\text{lower}} \leq {f{(x)}} \leq f_{\text{upper}} < \infty$ for all $x \in \mathcal{X}$, and the cost of a path $\sigma$ is given by Note that in this setup a straight line is not generally the lowest-cost connection between two samples ${u,v} \in \mathcal{X}$. $\text{FMT}^{\ast}$​, however, relies on straight lines in two ways: adjacent nodes in the $\text{FMT}^{\ast}$tree are connected with a straight line, and two samples are considered to be within $r$ of one another if the straight line connecting them has cost less than $r$.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Line Integral Costs with Optimal-Path Connections", "weight": 1.0} -->

In this section we consider a version of $\text{FMT}^{\ast}$whereby two adjacent nodes in the $\text{FMT}^{\ast}$tree are connected with the *optimal* path between them, and two nodes are considered to be within $r$ of one another if the *optimal* path connecting them has cost less than $r$.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Line Integral Costs with Optimal-Path Connections", "weight": 1.0} -->

Changes to $\text{FMT}^{\ast}$​'s implementation: Given two nodes ${u,v} \in V$, where $\sigma'$ denotes a path connecting $u$ and $v$. Given a set of nodes $V$, a node $v \in V$, and a positive number $r$, $\text{Near}{(V,v,r)}$ returns the set of nodes $\{{u \in V}:{{\text{Cost}{(u,v)}} < r}\}$. Every time a node is added to a tree, its cost-optimal connection to its parent is also stored. Lastly, the definition of $r_{n}$ needs to be multiplied by a factor of $f_{\text{upper}}$.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Line Integral Costs with Straight-Line Connections", "weight": 1.0} -->

Overview: Computing an optimal path for a line integral cost for every connection, as considered in Section 5.2.2, may represent an excessive computational bottleneck. Two strategies to address this issue are precompute such optimal paths since their computation does not require knowledge of the obstacle set, or approximate such paths with cost-weighted, straight line paths and study the impact on AO. In this section we study the latter approach, and we argue that AO does indeed still hold, by appealing to asymptotics to show that the triangle inequality approximately holds, with this approximation going away as $n\rightarrow\infty$.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Line Integral Costs with Straight-Line Connections", "weight": 1.0} -->

Changes to $\text{FMT}^{\ast}$​'s implementation: Given two samples ${u,v} \in V$, Given a set of samples $V$, a sample $v \in V$, and a positive number $r$, $\text{Near}{(V,v,r)}$ returns the set of samples $\{{u \in V}:{{\text{Cost}{(u,v)}} < r}\}$. Lastly, the definition of $r_{n}$ needs to again be increased by a factor of $f_{\text{upper}}$.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Overview", "weight": 1.0} -->

A last variant of interest is to have a version of $\text{FMT}^{\ast}$which makes connections based on $k$-nearest-neighbors instead of a fixed cost radius. This variant, referred to as $k$-nearest $\text{FMT}^{\ast}$​, has the advantage of being more adaptive to different obstacle spaces than its cost-radius counterpart. This is because $\text{FMT}^{\ast}$will consider about half as many connections for a sample very near an obstacle surface as for a sample far from obstacles, since about half the measure of the obstacle-adjacent-sample's cost ball is inside the obstacle. $k$-nearest $\text{FMT}^{\ast}$​, on the other hand, will consider $k$ connections for *every* sample.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Overview", "weight": 1.0} -->

To prove AO for $k$-nearest $\text{FMT}^{\ast}$​ (in Appendix F), we will stray slightly from our main proof exposition in this paper and use the similarities between $\text{FMT}^{\ast}$and PRM$^{\ast}$to leverage a similar proof for $k$-nearest PRM$^{\ast}$.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Changes to $\\text{FMT}^{\\ast}$​'s Implementation", "weight": 1.0} -->

Two parts need to change in Algorithm 2 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."), both about how Near works.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Changes to $\\text{FMT}^{\\ast}$​'s Implementation", "weight": 1.0} -->

The first is in lines 4 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") and 8 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."), where $N_{z}$ should be all samples $v \in {V \smallsetminus {\{

<!-- chunk {"id": "body-0138", "role": "body", "section": "Changes to $\\text{FMT}^{\\ast}$​'s Implementation", "weight": 1.0} -->

We refer to this set as the *mutual* $k_{n}$-nearest-neighbor set of $z$.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Changes to $\\text{FMT}^{\\ast}$​'s Implementation", "weight": 1.0} -->

The second change is that in lines 10 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") and 12 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."), $N_{x}$ should be the usual $k_{n}$-nearest-neighbor set of $x$, namely

<!-- chunk {"id": "body-0140", "role": "body", "section": "Changes to $\\text{FMT}^{\\ast}$​'s Implementation", "weight": 1.0} -->

Finally, $k_{n}$ should be chosen so that With these changes, $k$-nearest $\text{FMT}^{\ast}$works by repeatedly applying Bellman's equation (1 ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")) over a $k$-nearest-neighbor graph, analogously to what is done in the disk-connected graph case (see Theorem 3.2.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Changes to $\\text{FMT}^{\\ast}$​'s Implementation", "weight": 1.0} -->

‣ 3.2 Basic Properties and Intuition ‣ 3 The Fast Marching Tree Algorithm ("FMT"^∗​) ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")). When we want to refer to the generic algorithm $k$-nearest $\text{FMT}^{\ast}$using the specific sequence $k_{n}$, and we want to make this use explicit, we will say $k_{n}$-nearest $\text{FMT}^{\ast}$​.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Numerical Experiments and Discussion", "weight": 1.0} -->

In this section we numerically investigate the advantages of $\text{FMT}^{\ast}$over previous AO sampling-based motion planning algorithms. Specifically, we compare $\text{FMT}^{\ast}$against RRT$^{\ast}$and PRM$^{\ast}$​, as these two algorithms are state-of-the-art within the class of AO planners, span the main ideas (e.g., roadmaps versus trees) in the field of sampling-based planning, and have open-source, high quality implementations. We first present in Section 6.1 a brief overview of the simulation setup.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Numerical Experiments and Discussion", "weight": 1.0} -->

We then compare $\text{FMT}^{\ast}$​, RRT$^{\ast}$​, and PRM$^{\ast}$in Section 6.2. Numerical experiments confirm our theoretical and heuristic arguments by showing that $\text{FMT}^{\ast}$​, for a given execution time, returns substantially better solutions than RRT$^{\ast}$and PRM$^{\ast}$in a variety of problem settings. $\text{FMT}^{\ast}$​'s main computational speedups come from performing fewer collision checks---the more expensive collision-checking is, the more $\text{FMT}^{\ast}$will excel. Finally, in Section 6.3, we study in-depth $\text{FMT}^{\ast}$and its extensions (e.g., general costs). In particular, we provide practical guidelines about how to implement and tune $\text{FMT}^{\ast}$​.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Simulation Setup", "weight": 1.0} -->

Simulations were written in a mix of C++ and Julia, and run using a Unix operating system with a 2.0 GHz processor and 8 GB of RAM. The C++ simulations were run through the Open Motion Planning Library (OMPL), from which the reference implementation of RRT$^{\ast}$was taken. We took the default values of RRT$^{\ast}$parameters from OMPL (unless otherwise noted below), in particular a steering parameter of 20% of the maximum extent of the configuration space, and a goal-bias probability of 5%.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Simulation Setup", "weight": 1.0} -->

Also, since the only OMPL implementation of RRT$^{\ast}$is a $k$-nearest implementation, we adapted a $k$-nearest version of PRM$^{\ast}$and implemented a $k$-nearest version of $\text{FMT}^{\ast}$​, both in OMPL; these are the versions used in Sections 6.1--6.2. In these two subsections, for notational simplicity, we will refer to the $k$-nearest versions of $\text{FMT}^{\ast}$​, RRT$^{\ast}$​, and PRM$^{\ast}$simply as $\text{FMT}^{\ast}$​, RRT$^{\ast}$​, and PRM$^{\ast}$​, respectively. The three algorithms were run on test problems drawn from the bank of standard rigid body motion planning problems given in the OMPL.app graphical user interface.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Simulation Setup", "weight": 1.0} -->

These problems, detailed below and depicted in Figure 5, are posed within the configuration spaces $\text{SE}{}$ and $\text{SE}{}$ which correspond to the kinematics (available translations and rotations) of a rigid body in 2D and 3D respectively. The dimension of the state space sampled by these planners is thus three in the case of $\text{SE}{}$ problems, and six in the case of $\text{SE}{}$ problems.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Simulation Setup", "weight": 1.0} -->

We chose the Julia programming language for the implementation of additional simulations because of its ease in accommodating the $\text{FMT}^{\ast}$extensions studied in Section 6.3. We constructed experiments with a robot modeled as a union of hyperrectangles in high-dimensional Euclidean space moving amongst hyperrectangular obstacles. We note that for both simulation setups, $\text{FMT}^{\ast}$​, RRT$^{\ast}$​, and PRM$^{\ast}$used the *exact same primitive routines* (e.g., nearest-neighbor search, collision-checking, data handling, etc.) to ensure a fair comparison. The choice of $k$ for the nearest-neighbor search phase of each of the planning algorithms is an important tuning parameter (discussed in detail for $\text{FMT}^{\ast}$in Section 6.3.2).

<!-- chunk {"id": "body-0148", "role": "body", "section": "Simulation Setup", "weight": 1.0} -->

This latter coefficient differs, and is indeed less than, the lower bound in our mathematical guarantee of asymptotic optimality for $k$-nearest $\text{FMT}^{\ast}$​, equation (note that $k_{0,{\text{RRT}^{\ast}}}$ is also below the theoretical lower-bound presented in Karaman and Frazzoli). We note, however, that for a fixed state space dimension $d$, the formula for $k_{n}$ differs only by a constant factor independent from the sample size $n$. Our choice of $k_{0,\text{FMT}^{\ast}}$ in the experiments may be understood as a constant factor $e$ greater than the expected number of possible connections that would lie in an obstacle-free ball with radius specified by the lower bound in Theorem 4.1.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Simulation Setup", "weight": 1.0} -->

‣ 4.1 Asymptotic Optimality ‣ 4 Analysis of "FMT"^∗ ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."), i.e., $\eta = {e^{1/d} - 1} > 0$ in equation (3.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Simulation Setup", "weight": 1.0} -->

‣ 4.1 Asymptotic Optimality ‣ 4 Analysis of "FMT"^∗ ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.")). In practice we found that these coefficients for RRT$^{\ast}$​, PRM$^{\ast}$​, and $\text{FMT}^{\ast}$worked well on the problem instances and sample size regimes of our experiments. Indeed, we note that the choice of $k_{0,{\text{RRT}^{\ast}}}$​, although taken directly from the OMPL reference implementation, stood up well against other values we tried when aiming to ensure a fair comparison.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Simulation Setup", "weight": 1.0} -->

The implementation of $\text{FMT}^{\ast}$and the code used for algorithm comparison are available: For each problem setup, we show a panel of six graphs. The first (top left) shows cost versus time, with a point on the graph for each simulation run. These simulations come in groups of 50, and within each group are run on the same number of samples. Note that this sample size is not necessarily the number of nodes in the graph constructed by each algorithm; it indicates iteration count in the case of RRT$^{\ast}$​, and free space sample count in the cases of $\text{FMT}^{\ast}$and PRM$^{\ast}$​. To be precise, RRT$^{\ast}$only keeps samples for which initial steering is collision-free. PRM$^{\ast}$does use all of the sampled points in constructing its roadmap, and while $\text{FMT}^{\ast}$nominally constructs a tree as a subgraph of this roadmap, it may terminate early if it finds a solution before all samples are considered.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Simulation Setup", "weight": 1.0} -->

There is also a line on the first plot tracing the mean solution cost of *successful* algorithm runs on a particular sample count (1-standard-error of the mean error-bars are given in both time and cost). Note that for a given algorithm, a group of simulations for a given sample count is only plotted if it is at least 50% successful at finding a feasible solution. The plot below this one (middle left) shows success rate as a function of time, with each point representing a set of simulations grouped again by algorithm and node count. In this plot, all sample counts are plotted for all algorithms, which is why the curves may start farther to the left than those in the first plot. The top right and middle right plots are the analogous plots to the first two, but with sample count on the $x$-axis. Finally, the bottom left plot shows execution time as a function of sample count, and the bottom right plot shows the number of collision-checks as a function of sample count. Note that every plot shows vertical error bars, and horizontal error bars where appropriate, of length one standard-error of the mean, although they are often too small to be distinguished from points.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Numerical Experiments in an $\\text{SE}{}$ Bug Trap", "weight": 1.0} -->

The first test case is the classic bug trap problem in $\text{SE}{}$ (Figure 5(a)), a prototypically challenging problem for sampling-based motion planners. The simulation results for this problem are depicted graphically in Figure 6. $\text{FMT}^{\ast}$takes about half and one tenth the time to reach similar quality solutions as RRT$^{\ast}$and PRM$^{\ast}$​, respectively, on average. Note that $\text{FMT}^{\ast}$also is by far the quickest to reach high success rates, achieving nearly 100% in about one second, while RRT$^{\ast}$takes about five seconds and PRM$^{\ast}$is still at 80% success rate after 14 seconds.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Numerical Experiments in an $\\text{SE}{}$ Bug Trap", "weight": 1.0} -->

The plot of solution cost as a function of sample count shows what we would expect: $\text{FMT}^{\ast}$and PRM$^{\ast}$return nearly identical-quality solutions for the same number of samples, with PRM$^{\ast}$very slightly better, while RRT$^{\ast}$​, due to its greediness, suffers in comparison. Similarly, $\text{FMT}^{\ast}$and PRM$^{\ast}$have similar success rates as a function of sample count, both substantially higher than RRT$^{\ast}$. The reason that RRT$^{\ast}$still beats PRM$^{\ast}$in terms of cost versus time is explained by the plot of execution time versus sample count: RRT$^{\ast}$is much faster per sample than PRM$^{\ast}$.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Numerical Experiments in an $\\text{SE}{}$ Bug Trap", "weight": 1.0} -->

However, RRT$^{\ast}$is still slightly slower per sample than $\text{FMT}^{\ast}$​, as explained by the plot of collision-checks versus sample count, which shows $\text{FMT}^{\ast}$performing fewer collision-checks per sample ($O{}$) than RRT$^{\ast}$($O{({\log{(n)}})}$).

<!-- chunk {"id": "body-0156", "role": "body", "section": "Numerical Experiments in an $\\text{SE}{}$ Bug Trap", "weight": 1.0} -->

The lower success rate for RRT$^{\ast}$may be explained as a consequence of its graph expansion process. When iterating to escape the bug trap, the closest tree node to a new sample outside the mouth of the trap will nearly always lie in one of the "dead end" lips, and thus present an invalid steering connection. Only when the new sample lies adjacent to the progress of the tree down the corridor will RRT$^{\ast}$be able to advance. For RRT$^{\ast}$to escape the bug trap, an *ordered sequence* of samples must be obtained that lead the tree through the corridor. $\text{FMT}^{\ast}$and PRM$^{\ast}$are not affected by this problem; their success rate is determined only by whether or not such a set of samples exists, not the order in which they are sampled by the algorithm.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Numerical Experiments in an $\\text{SE}{}$ Maze", "weight": 1.0} -->

Navigating a "maze" environment is another prototypical benchmark for path planners. This section, in particular, considers an $\text{SE}{}$ maze (portrayed in Figure 5(b)). The plots for this environment, given in Figure 7, tell a very similar story to those of the $\text{SE}{}$ bug trap. Again, $\text{FMT}^{\ast}$reaches given solution qualities faster than RRT$^{\ast}$and PRM$^{\ast}$by factors of about 2 and 10, respectively. Although the success rates of all the algorithms go to 100% quite quickly, $\text{FMT}^{\ast}$is still the fastest. All other heuristic relationships between algorithms in the other graphs remain the same as in the case of the $\text{SE}{}$ bug trap.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Numerical Experiments in an $\\text{SE}{}$ Maze", "weight": 1.0} -->

A new feature of the $\text{SE}{}$ maze is that RRT$^{\ast}$now runs faster per sample than $\text{FMT}^{\ast}$​, due to the fact that it performs fewer collision-checks per sample than $\text{FMT}^{\ast}$​. The reason for this has to do with the relative search radii of the two algorithms. Since they work very differently, it is not unreasonable to use different search radii, and although $\text{FMT}^{\ast}$will perform fewer collision-checks asymptotically, for finite sample sizes, the number of collision-checks is mainly influenced by connection radius and obstacle clutter. While RRT$^{\ast}$​'s radius has been smaller than $\text{FMT}^{\ast}$​'s in all simulations up to this point, the previous two setups had more clutter, forcing RRT$^{\ast}$to frequently draw a sample, collision-check its nearest-neighbor connection, and then remove it when this check fails.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Numerical Experiments in an $\\text{SE}{}$ Maze", "weight": 1.0} -->

As can be seen in Figure 5(c), the $\text{SE}{}$ maze is relatively open and contains fewer traps as compared to the previous two problems, thereby utilizing more of the samples that it runs collision-checks.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Numerical Experiments for 3D, 5D, and 7D Recursive Maze", "weight": 1.0} -->

In order to illustrate a "worst-case" planning scenario in high dimensional space, we constructed a recursive maze obstacle environment within the Euclidean unit hypercube. Essentially, each instance of the maze consists of two copies of the maze in the previous dimension separated by a divider and connected through the last dimension. See Figure 9 for the first two instances of the maze in two dimensions and three dimensions, respectively. This recursive nature has the effect of producing a problem environment with only one homotopy class of solutions, any element of which is necessarily long and features sections that are spatially close, but far away from each other in terms of their distance along the solution path. Our experiments investigated translating a rigid body from one end of the maze to the other. The results of simulations in 3, 5, and 7 dimensional recursive mazes are given in Figures 10, 11, and 12. $\text{FMT}^{\ast}$once again reaches lower-cost solutions in less time than RRT$^{\ast}$​, with the improvement increasing with dimension.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Numerical Experiments for 3D, 5D, and 7D Recursive Maze", "weight": 1.0} -->

The most notable trend between $\text{FMT}^{\ast}$and RRT$^{\ast}$​, however, is in success rate. While both algorithms reach 100% success rate almost instantly in 3D, $\text{FMT}^{\ast}$reaches 100% in under a second, while RRT$^{\ast}$takes closer to five seconds in 5D, and most significantly RRT$^{\ast}$was never able to find any solution in the time alotted in 7D. This can be understood through the geometry of the maze---the maze's complexity is exponentially increasing in dimension, and in 7D, so much of free space is blocked off from every other part of free space that RRT$^{\ast}$is stuck between two bad options: it can use a large steering radius, in which case nearly every sample fails to connect to its nearest-neighbor and is thrown out, or it can use a small steering radius, in which case connections are so short that the algorithm has to figuratively crawl through the maze.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Numerical Experiments for 3D, 5D, and 7D Recursive Maze", "weight": 1.0} -->

Even if the steering parameter were not an issue, the mere fact that RRT$^{\ast}$operates on a steering graph-expansion principle means that in order to traverse the maze, an ordered subsequence of $2^{7}$ nodes (corresponding to each turn of the maze) must be in the sample sequence before a solution may be found. While this is an extreme example, as the recursive maze is very complex in 7D (feasible solutions are at least 43 units long, and entirely contained in the unit cube), it accentuates $\text{FMT}^{\ast}$​'s advantages in highly cluttered environments.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Numerical Experiments for 3D, 5D, and 7D Recursive Maze", "weight": 1.0} -->

As compared to PRM$^{\ast}$​, $\text{FMT}^{\ast}$still presents a substantial improvement, but that improvement decreases with dimension. This can be understood by noting that the two algorithms achieve nearly identical costs for a given sample count, but $\text{FMT}^{\ast}$is much faster due to savings on collision-checks. However, as the plots show, the relative decrease in collision-checks from PRM$^{\ast}$to $\text{FMT}^{\ast}$decreases to only a factor of two once we reach 7D, and indeed we see that, when both algorithms achieve low cost, $\text{FMT}^{\ast}$does so in approximately half the time. This relative decrease in collision-checks comes from the aforementioned extreme obstacle clutter in the configuration space. $\text{FMT}^{\ast}$makes big savings over PRM$^{\ast}$when it connects many samples on their first consideration, but when most samples are close to obstacles, most samples will take multiple considerations to finally be connected.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Numerical Experiments for 3D, 5D, and 7D Recursive Maze", "weight": 1.0} -->

Both algorithms achieve 100% success rates in approximately the same amount of time.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Numerical Experiments for the $\\text{SE}{}$ Alpha Puzzle", "weight": 1.0} -->

Throughout our numerical evaluation of $\text{FMT}^{\ast}$​, we found only one planning problem where $\text{FMT}^{\ast}$does not consistently outperform RRT$^{\ast}$($\text{FMT}^{\ast}$outperformed PRM$^{\ast}$in all of our numerical tests). The problem is the famous 1.5 Alpha puzzle, which consists of two tubes, each twisted in an $\alpha$ shape. The objective is to separate the intertwined tubes by a sequence of translations and rotations, which leads to extremely narrow corridors in $\mathcal{X}_{\text{free}}$ through which the solution path must pass (see Figure 5(d)). Simulation results show that the problem presents two homotopy classes of paths (Figure 13).

<!-- chunk {"id": "body-0166", "role": "body", "section": "Numerical Experiments for the $\\text{SE}{}$ Alpha Puzzle", "weight": 1.0} -->

$\text{FMT}^{\ast}$converges to a 100% success rate more slowly than RRT$^{\ast}$(Figure 13), but when $\text{FMT}^{\ast}$finds a solution, that solution tends to be in the "right" homotopy class and of higher quality, see Figures 13 and 13. We note that in order to achieve this high success rate for RRT$^{\ast}$​, we adjusted the steering parameter to 1.5% of the maximum extent of the configuration space, down from 20%. Without this adjustment, RRT$^{\ast}$was unable to find feasible solutions at the upper range of the sample counts considered.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Numerical Experiments for the $\\text{SE}{}$ Alpha Puzzle", "weight": 1.0} -->

This behavior can be intuitively explained as follows. The Alpha puzzle presents "narrow corridors" in $\mathcal{X}_{\text{free}}$. When $\text{FMT}^{\ast}$reaches their entrance, if no sample is present in the corridors, $\text{FMT}^{\ast}$​ stops its expansion, while RRT$^{\ast}$keeps trying to extend its branches through the corridors, which explains its higher success rates at low sample counts. On the other hand, at high sample counts, samples are placed in the corridors with high probability, and when this happens the optimal (as opposed to greedy) way by which $\text{FMT}^{\ast}$grows the tree usually leads to the discovery of a better homotopy class and of a higher quality solution within it (Figure 13, execution times larger than $\sim 25$ seconds).

<!-- chunk {"id": "body-0168", "role": "body", "section": "Numerical Experiments for the $\\text{SE}{}$ Alpha Puzzle", "weight": 1.0} -->

As a result, RRT$^{\ast}$outperforms $\text{FMT}^{\ast}$for short execution times, while $\text{FMT}^{\ast}$outperforms RRT$^{\ast}$in the complementary case. Finally, we note that the extremely narrow but short corridors in the Alpha puzzle present a different challenge to these algorithms than the directional corridor of the $\text{SE}{}$ bug trap.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Numerical Experiments for the $\\text{SE}{}$ Alpha Puzzle", "weight": 1.0} -->

As discussed in Section 6.2.1 Bug Trap ‣ 6.2 Comparison with Other AO Planning Algorithms ‣ 6 Numerical Experiments and Discussion ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments."), the ordering of sampled points along the exit matters for RRT$^{\ast}$in the bug trap configuration, while for the Alpha puzzle the fact that there are no bug-trap-like "dead ends" to present false steering connections means that a less intricate sequence of nodes is required for success.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Numerical Experiments for the $\\text{SE}{}$ Alpha Puzzle", "weight": 1.0} -->

On the one hand, allowing $\text{FMT}^{\ast}$to sample new points around the leaves of its tree whenever it fails to find a solution (i.e., when $V_{open}$ becomes empty) might substantially improve its performance in the presence of extremely narrow corridors. In a sense, such a modification would introduce a notion of "anytimeness" and adaptive sampling into $\text{FMT}^{\ast}$​, which would effectively leverage the steadily outward direction by which the tree is constructed (see for a conceptually related idea). This is a promising area of future research (note that the theoretical foundations for non-uniform sampling strategies are provided in Section 5.1). On the other hand, planning problems with extremely narrow passages, such as the Alpha puzzle, do not usually arise in robotics applications as, fortunately, they tend to be *expansive*, i.e., they enjoy "good" visibility properties. Collectively, these considerations suggest the superior performance of $\text{FMT}^{\ast}$in most practical settings.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Comparison Between $\\text{FMT}^{\\ast}$and k-Nearest $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

Since we are now comparing both versions of $\text{FMT}^{\ast}$​, we will explicitly use radial-$\text{FMT}^{\ast}$to denote the version of $\text{FMT}^{\ast}$that uses a fixed Euclidean distance to determine neighbors, and return to referring to $k$-nearest $\text{FMT}^{\ast}$by its full name throughout this section. For this set of simulations, given in Figure 14, the formula for $k_{n}$ is still the same as in the rest of the simulations, and for comparison, the radius $r_{n}$ of the radial-$\text{FMT}^{\ast}$implementation is chosen so that the expected number of samples in a collision-free $r_{n}$-ball is exactly equal to $k_{n}$. Finally, as a caveat, we point out that since $k$-nearest-neighborhoods are fundamentally different from $r$-radius-neighborhoods, the two algorithms depicted now use *different* primitive procedures.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Comparison Between $\\text{FMT}^{\\ast}$and k-Nearest $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

Since computing neighbors in both algorithms takes a substantial fraction of the runtime, the cost versus time plots should be interpreted with caution, since the algorithms' relative runtimes could potentially change significantly with a better implementation of one or both neighbor-finding primitive procedures. With that said, we focus our attention more on the number of collision-checks as a proxy for algorithm speed. Since this problem has a relatively simple collision-checking module, we may expect that for more complex problems in which collision-checking dominates runtime, the number of collision-checks should approximate runtime well.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Comparison Between $\\text{FMT}^{\\ast}$and k-Nearest $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

While the number of collision-checks in free space is the same between the two algorithms, since all samples connect when they are first considered, some interesting behavior is exhibited in the same plot for the 5D maze. In particular, the number of collision checks for $k$-nearest $\text{FMT}^{\ast}$ increases quickly with sample count, then decreases again and starts to grow more like the linear curve for radial-$\text{FMT}^{\ast}$​. This hump in the curve corresponds to when the usual connection distance for $k$-nearest $\text{FMT}^{\ast}$ is greater than the width of the maze wall, meaning that for many of the points, some of their $k_{n}$-nearest-neighbors will be much farther along in the maze. Thus $k$-nearest $\text{FMT}^{\ast}$ tries to connect them to the tree, and fails because there is a wall in between.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Comparison Between $\\text{FMT}^{\\ast}$and k-Nearest $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

The same problem doesn't occur for radial-$\text{FMT}^{\ast}$because its radius stays smaller than the width of the maze wall. This is symptomatic of an advantage and disadvantage of $k$-nearest $\text{FMT}^{\ast}$​, namely that for samples near obstacles, connections may be attempted to farther-away samples. This is an advantage because for a point near an obstacle, there is locally less density around the point and thus fewer nearby options for connection, making it harder for radial-$\text{FMT}^{\ast}$to find a connection, let alone a good one. For small sample sizes relative to dimension however, this can cause a lot of extra collision-checks, as just described, having $k$-nearest $\text{FMT}^{\ast}$ attempt connections across walls.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Comparison Between $\\text{FMT}^{\\ast}$and k-Nearest $\\text{FMT}^{\\ast}$", "weight": 1.0} -->

As this disadvantage goes away with enough points, we still find that, although the difference in free space is very small, $k$-nearest $\text{FMT}^{\ast}$outperforms radial-$\text{FMT}^{\ast}$in both of the settings shown, as the relative advantage of $k$-nearest $\text{FMT}^{\ast}$ in solution cost per sample is greater than the relative disadvantage in number of collision-checks per sample.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Tuning the Radius Scale Factor", "weight": 1.0} -->

The choice of tuning parameters is a challenging and pervasive problem in the sampling-based motion planning literature. Throughout these numerical experiments, we have used the same neighbor scaling factor, which we found empirically to work well across a range of scenarios. In this section, we try to understand the relationship of $k$-nearest $\text{FMT}^{\ast}$ with this neighbor scaling parameter, in the example of the $\text{SE}{}$ maze.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Tuning the Radius Scale Factor", "weight": 1.0} -->

The results of running $k$-nearest $\text{FMT}^{\ast}$ with a range of tuning parameters on this problem are shown in Figure 15. The values in the legend correspond to a connection radius multiplier (RM) of $k_{0,\text{FMT}^{\ast}}$ as defined at the beginning of Section 6, i.e., a value of $\text{RM} = 1$ corresponds to using exactly $k_{0,\text{FMT}^{\ast}}$, and a value of $\text{RM} = 2$ corresponds to using $k_{0} = {2^{d} \cdot k_{0,\text{FMT}^{\ast}}}$. We point out that to reduce clutter, we have omitted error bars from the plot, but note that they are small compared to the differences between the curves.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Tuning the Radius Scale Factor", "weight": 1.0} -->

This graph clearly shows the tradeoff in the scaling factor, namely that for small values, $k$-nearest $\text{FMT}^{\ast}$ rapidly reaches a fixed solution quality and then plateaus, while for larger values, the solution takes a while to reach lower costs, but continues to show improvement for longer, eventually beating the solutions for small values. The fact that most of these curves cross one another tells us that the choice of this tuning parameter depends on available time and corresponding sample count. For this experimental setup, and for the other problems we tried, there appears to be a sweet spot around the value $\text{RM} = 1$. Indeed, this motivated our choice of $k_{0,\text{FMT}^{\ast}}$ in our simulations. We note that the curves for 0.7 through 0.9 start out at lower costs for very small execution times, and it appears that the curve for 1.1 is going to start to return better solutions than 1.0 before 35 seconds. That is, depending on the time/sample allowance, there are at least four regimes in which different scaling factors outperform the others.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Tuning the Radius Scale Factor", "weight": 1.0} -->

For a different problem instance, the optimal scaling profile may change, and for best performance some amount of manual tuning will be required. We note, however, that $\text{RM} = 1$ is never too far from the best in Figure 15, and should represent a safe default choice.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Improvement on Convergence Rate with Simple Heuristics", "weight": 1.0} -->

In any path planning problem, the optimal path tends to be quite smooth, with only a few non-differentiable points. However, sampling-based algorithms all locally-connect points with straight lines, resulting in some level of "jaggedness" in the returned paths. A popular post-processing heuristic for mitigating this problem is the ADAPTIVE-SHORTCUT smoothing heuristic described. In Figure 16, we show the effect of applying the ADAPTIVE-SHORTCUT heuristic to $k$-nearest $\text{FMT}^{\ast}$ solutions for the 5D recursive maze. We use a point robot for this simulation as it allowed us to easily compute the true optimal cost, and thus better place the improvement from the heuristic in context. The improvement is substantial, and we see that we can obtain a solution within 10% of the optimal with fewer than 1000 samples in this complicated 5D environment. Figure 16 also displays the fact that adding the ADAPTIVE-SHORTCUT heuristic only barely increases the number of collision-checks.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Improvement on Convergence Rate with Simple Heuristics", "weight": 1.0} -->

We place sample count on the $x$-axis because it is more absolute than time, which is more system-dependent, and because the ADAPTIVE-SHORTCUT heuristic runs so quickly compared to the overall algorithm that sample count is able to act as an accurate proxy for time across the two implementations of $k$-nearest $\text{FMT}^{\ast}$.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Experiment With General Cost", "weight": 1.0} -->

As a demonstration of the computationally-efficient $k$-nearest $\text{FMT}^{\ast}$ implementation described in Section 5.2.3, we set up three environments with non-constant cost-density over the configuration space. We have kept them in two dimensions so that they can be considered visually, see Figure 17. In Figure 17, there is a high-cost region near the root node and a low-cost region between it and the goal region. $k$-nearest $\text{FMT}^{\ast}$ correctly chooses the shorter path through the high-cost region instead of going around it, as the extra distance incurred by the latter option is greater than the extra cost incurred in the former. In Figure 17, we have increased the cost density of the high-cost region, and $k$-nearest $\text{FMT}^{\ast}$ now correctly chooses to go around it as much as possible.

<!-- chunk {"id": "body-0183", "role": "body", "section": "Experiment With General Cost", "weight": 1.0} -->

In Figure 17, the cost density function is inversely proportional to distance from the center, and $k$-nearest $\text{FMT}^{\ast}$ smoothly makes its way around the higher-cost center to reach the goal region. Note that in all three plots, since cost-balls are used for considering connections, the edges are shorter in higher-cost areas and longer in lower-cost areas.

<!-- chunk {"id": "body-0184", "role": "body", "section": "How to Best Use $\\text{FMT}^{\\ast}$​?", "weight": 1.0} -->

$\text{FMT}^{\ast}$relies on two parameters, namely the connection radius or number of neighbors, and the number of samples. As for the first parameter, numerical experiments showed that $k_{0,\text{FMT}^{\ast}} = {2^{d}{({e/d})}}$ represents an effective and fairly robust choice for the $k$-nearest version of $\text{FMT}^{\ast}$---this is arguably the value that should be used in most planning problems. Correspondingly, for the radial version of $\text{FMT}^{\ast}$​, one should choose a connection radius as specified in the lower bound in Theorem 4.1.

<!-- chunk {"id": "body-0185", "role": "body", "section": "How to Best Use $\\text{FMT}^{\\ast}$​?", "weight": 1.0} -->

‣ 4.1 Asymptotic Optimality ‣ 4 Analysis of "FMT"^∗ ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.") with $\eta = {e^{1/d} - 1}$ (see Section 6.1). Selecting the number of samples is a more contentious issue, as it is very problem-dependent. A system designer should experiment with a variety of sample sizes for a variety of "expected" obstacle configurations, and then choose the value that statistically performs the best within the available computational resources.

<!-- chunk {"id": "body-0186", "role": "body", "section": "How to Best Use $\\text{FMT}^{\\ast}$​?", "weight": 1.0} -->

Such a baseline choice could be adaptively adjusted via the resampling techniques discussed in or via the adaptive strategies discussed in and mentioned in Section 6.2.5 Alpha Puzzle ‣ 6.2 Comparison with Other AO Planning Algorithms ‣ 6 Numerical Experiments and Discussion ‣ Fast Marching Tree: a Fast Marching Sampling-Based Method for Optimal Motion Planning in Many DimensionsThis work was originally presented at the 16th International Symposium on Robotics Research, ISRR 2013. This revised version includes an extended description of the "FMT"^∗algorithm, proofs of all results, extended discussions about convergence rate and computational complexity, extensions to non-uniform sampling distributions and general costs, a 𝑘-nearest version of "FMT"^∗​, and a larger set of numerical experiments.").

<!-- chunk {"id": "body-0187", "role": "body", "section": "How to Best Use $\\text{FMT}^{\\ast}$​?", "weight": 1.0} -->

For the problem environments and sample sizes considered in our experiments, the extents of the neighbor sets ($k$-nearest or radial) are macroscopic with respect to the obstacles. The decrease in available connections for many samples when their radial neighborhoods significantly intersect the obstacle set seems to adversely affect algorithm performance (see Section 6.3.1). The $k$-nearest version of $\text{FMT}^{\ast}$avoids this issue by attempting connection to a fixed number of samples regardless of obstacle proximity. Thus $k$-nearest $\text{FMT}^{\ast}$should be considered the default, especially for obstacle cluttered environments. If the application has mostly open space to plan through, however, radial $\text{FMT}^{\ast}$may be worth testing and tuning.

<!-- chunk {"id": "body-0188", "role": "body", "section": "How to Best Use $\\text{FMT}^{\\ast}$​?", "weight": 1.0} -->

In problems with a general cost function, $\text{FMT}^{\ast}$provides a good standalone solution that provably converges to the optimum. In problems with a metric cost function, $\text{FMT}^{\ast}$(as also RRT$^{\ast}$and PRM$^{\ast}$​) should be considered as a backbone algorithm on top of which one should add a smoothing procedure such as ADAPTIVE-SHORTCUT. In this regard, $\text{FMT}^{\ast}$should be regarded as a fast "homotopy finder," reflecting its quick initial convergence rate to a good homotopy class, which then needs to be assisted by a smoothing procedure to offset its typical plateauing behavior, i.e., slow convergence to an optimum solution *within* a homotopy class.

<!-- chunk {"id": "body-0189", "role": "body", "section": "How to Best Use $\\text{FMT}^{\\ast}$​?", "weight": 1.0} -->

When combining $\text{FMT}^{\ast}$with a smoothing procedure one should consider values for the connection radius or number of neighbors most likely equal to about 80% or 90% of the previously suggested values, so as to ensure very fast initial rates of convergence (see Section 6.3.2). Additionally, non-uniform sampling strategies reflecting *prior* knowledge about the problem may also improve the speed of finding the optimal homotopy class. Finally, a bidirectional implementation is usually preferable.

<!-- chunk {"id": "body-0190", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper we have introduced and analyzed a novel probabilistic sampling-based motion planning algorithm called the Fast Marching Tree algorithm ($\text{FMT}^{\ast}$). This algorithm is asymptotically optimal and appears to converge *significantly* faster then its state-of-the-art counterparts for a wide range of challenging problem instances. We used the weaker notion of convergence in probability, as opposed to convergence almost surely, and showed that the extra mathematical flexibility allowed us to compute convergence rate bounds. Extensions (all retaining AO) to non-uniform sampling strategies, general costs, and a $k$-nearest-neighbor implementation were also presented.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Conclusions", "weight": 1.0} -->

This paper leaves numerous important extensions open for further research. First, it is of interest to extend the $\text{FMT}^{\ast}$algorithm to address problems with differential motion constraints; the work in and presents preliminary results in this direction (specifically, for systems with driftless differential constraints, and with drift constraints and linear affine dynamics, respectively). Second, we plan to explore further the convergence rate bounds provided by the proof of AO given here. Third, we plan to use this algorithm as the backbone for scalable stochastic planning algorithms. Fourth, we plan to extend the $\text{FMT}^{\ast}$algorithm for solving the Eikonal equation, and more generally for addressing problems characterized by partial differential equations. Fifth, as discussed, $\text{FMT}^{\ast}$requires the tuning of a scaling factor for either the search radius or the number of nearest-neighbors, and the selection of the number of samples. It is of interest to devise strategies whereby these parameters are "self regulating" (see Section 6.3.5 for some possible strategies), thus effectively making the algorithm parameter-free and anytime.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Finally, we plan to test the performance of $\text{FMT}^{\ast}$on mobile ground robots operating in dynamic environments.
