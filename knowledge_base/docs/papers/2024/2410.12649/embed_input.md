<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Faster Algorithms for Growing Collision-Free Convex Polytopes in Robot Configuration Space

Topics include Semidefinite programming, Linear programming, Trajectory optimization, Robotics, Graphs, Online algorithms, Optimization, Planning, Control, Sampling, IRIS-ZO, Configuration space, Convex polytope.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose two novel algorithms for constructing convex collision-free polytopes in robot configuration space. Finding these polytopes enables the application of stronger motion-planning frameworks such as trajectory optimization with Graphs of Convex Sets and is currently a major roadblock in the adoption of these approaches. In this paper, we build upon IRIS-NP (Iterative Regional Inflation by Semidefinite & Nonlinear Programming) to significantly improve tunability, runtimes, and scaling to complex environments. IRIS-NP uses nonlinear programming paired with uniform random initialization to find configurations on the boundary of the free configuration space. Our key insight is that finding near-by configuration-space obstacles using sampling is inexpensive and greatly accelerates region generation. We propose two algorithms using such samples to either employ nonlinear programming more efficiently (IRIS-NP2 ) or circumvent it altogether using a massively-parallel zero-order optimization strategy (IRIS-ZO). We also propose a termination condition that controls the probability of exceeding a user-specified permissible fraction-in-collision, eliminating a significant source of tuning difficulty in IRIS-NP.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We compare performance across eight robot environments, showing that IRIS-ZO achieves an order-of-magnitude speed advantage over IRIS-NP. IRISNP2, also significantly faster than IRIS-NP, builds larger polytopes using fewer hyperplanes, enabling faster downstream computation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A major challenge in robot motion planning is the need to simultaneously consider *task space*, the world in which the robot physically resides, and *configuration space*, $\mathcal{C}$, the set of all possible robot configurations. The planner must produce a trajectory in the configuration space, but many constraints are formulated in the task space. Collision avoidance is particularly challenging, because even geometrically simple obstacles in task space can have intractably complicated descriptions when transformed into configuration space through the robot's inverse kinematics. While there is work on constructing explicit configuration-space representations of workspace obstacles, these methods are intractable for the high degree-of-freedom (dof) robotic systems being used today.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The unavailability of obstacles' configuration-space descriptions has not prevented the development of a rich literature of motion planning algorithms. Many approaches approximate the set of collision-free configurations ($\mathcal{C}^{free}$) without explicitly constructing the individual obstacles. Interval analysis and cell decompositions can approximate $\mathcal{C}^{free}$ as the union of boxes \[7, §5-6\], but these methods are computationally intractable for high-dimensional configuration spaces. Perhaps the most widely used technique has been sampling-based planning, in which samples are drawn from $\mathcal{C}^{free}$ and connected into a graph structure.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

These representations of $\mathcal{C}^{free}$ are popular due to their simplicity and versatility. However, they all struggle with the "curse of dimensionality" -- the memory use of the representation may grow exponentially with the dimension of the configuration space. This has led the motion planning community to explore volumetric approximations of $\mathcal{C}^{free}$ such as the union of spheres used by Yang and LaValle or the polytopes constructed by Deits and Tedrake. In contrast to the grid- or sampling-based approaches, the individual sets used in these approaches describe free-space regions rather than points. Although these sets are harder to construct, they often enable a more concise approximation of $\mathcal{C}^{free}$ and yield convex (probabilistic) collision-avoidance constraints.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning algorithms such as trajectory optimization with leverage these representations to quickly produce high-quality, collision-free trajectories for high-dimensional robotic systems. However, the performance of these planners is highly dependent on the properties of the convex sets. It is desirable for these sets to have large volumes in order to reduce the number of sets required to approximate $\mathcal{C}^{free}$, while retaining simple descriptions to make downstream planning more efficient. While creating perfectly collision-free sets is very costly, practical algorithms should provide a straightforward way to trade off between precision and runtime.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent results for planning with leverage the IRIS-NP algorithm. IRIS-NP takes in a collision-free *seed* configuration and attempts to construct a convex, collision-free polytope containing it. IRIS-NP, however, falls short of meeting the aforementioned criteria in practice. Its runtime is substantial and trading off between runtime and correctness (how much of the region is collision-free) proves challenging. IRIS-NP only terminates after failing to solve a user-specified number of nonlinear programs in succession, a time-consuming process dependent on this user-specified parameter acting as a proxy for correctness, when the actual relationship is unclear. Furthermore, these nonlinear programs must be run separately for every object in the scene, causing IRIS-NP to scale poorly with environment complexity.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we improve upon IRIS-NP, focusing on a key subroutine that constructs hyperplanes to separate the seed point from obstacles. Our improvements leverage the fact that we can evaluate thousands of configurations for collisions in the time it takes to solve a single nonlinear optimization problem. We employ random sampling and collision checking to estimate the proportion of the polytope that is collision-free, providing a rigorous probabilistic certificate, and enabling intuitive tradeoffs between region correctness and computation times. We further present two algorithms that utilize sampling and collision checking to improve polytope generation: IRIS-ZO rapidly generates polytopes using a simple parallelized zero-order optimization strategy that requires no gradient computations and is easy to implement. IRIS-NP2 uses sampled collisions to seed nonlinear optimizations, increasing search success, and dramatically reducing the required number of programs. We demonstrate that both algorithms outperform IRIS-NP in terms of computation time and region quality.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In this section, we introduce the problem formulation and discuss the required inputs and provided outputs of our proposed algorithms.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We aim to generate large convex polytopes in configuration space whose fraction in collision is less than a user-provided constant. More precisely, let $\lambda$ denote the Lebesgue measure in the free configuration space $\mathcal{C}^{free}$. Given a user-specified admissible fraction in collision $\varepsilon \in {}$ and confidence $\delta \in {}$, we will compute positive-volume convex polytopes $\mathcal{R} \subseteq \mathcal{C}$ such that Since obtaining a closed-form description of $\mathcal{C}^{free}$ is intractable for general robotic systems \[13, §4.3.3\],\[7, §3\], our algorithms utilize a task-space description. Such descriptions are readily provided via common robot description formats such as URDFs or SDFs. We expect the robot to be described as $M$ sets $\mathcal{G}_{i} \subseteq {\mathbb{R}}^{N_{\text{ts}}}$ representing collision geometries in task space.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Here, $N_{\text{ts}} \in {\{ 2,3\}}$ is the dimension of the task space, and $q \in \mathcal{C}$ is the configuration. The sets $\mathcal{G}_{i}$ are represented in their body frame $B_{i}$. Using the monogram notation of \[16, §3.1\], each $\mathcal{G}_{i}$ is paired with a configuration-dependent rigid-body transformation ${{{}_{}^{W}X_{}^{B_{i}}}{(q)}} \in {SE{(N_{\text{ts}})}}$ that defines the forward kinematics of $\mathcal{G}_{i}$ in the world frame $W$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

For a configuration $q$, the system is *in collision* if there exists a *valid*^11^1Typically, only a subset of all collision pairs is considered for practical reasons. pair of collision geometries ${{\mathcal{A}{(q)}},{\mathcal{B}{(q)}}} \in {\mathcal{G}{(q)}}$ such that ${{\mathcal{A}{(q)}} \cap {\mathcal{B}{(q)}}} \neq \varnothing$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

For a valid collision pair ${{\mathcal{A}{(q)}},{\mathcal{B}{(q)}}} \in {\mathcal{G}{(q)}}$, the corresponding *configuration-space obstacle* $\mathcal{O}^{\mathcal{A}\mathcal{B}}{(q)}$ is implicitly defined as We avoid explicitly describing $\mathcal{O}^{\mathcal{A}\mathcal{B}}$ by using nonconvex task-space constraints, as.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Related Works", "weight": 1.0} -->

Algorithms for computing positive-volume subsets of $\mathcal{C}^{free}$ can be divided into two categories: those which require explicit descriptions of the obstacles in configuration space, and those that can use implicit descriptions. Explicit descriptions of obstacles are generally only available for robots with simple kinematics (e.g. only prismatic joints).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Related Works", "weight": 1.0} -->

If descriptions of all obstacles are given as convex sets, the original IRIS algorithm can construct large collision-free polytopes about a seed points using a series of convex optimizations. Such descriptions can be obtained from arbitrary meshes via approximate convex decomposition techniques. Wu et. al. use a similar approach to grow convex polytopes around an existing trajectory, towards producing a shorter, collision-free path.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Related Works", "weight": 1.0} -->

Due to the complex kinematics of robotic manipulators, obstacles in configuration space are frequently given by implicit descriptions. Yang and LaValle leveraged the kinematic Jacobian to relate motion in configuration-space and task space, allowing the construction of collision-free ellipsoids. Unfortunately, large numbers of ellipsoids are required to approximate even simple, low-dimensional configuration spaces.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Related Works", "weight": 1.0} -->

The original IRIS algorithm has been extended to handle such implicit descriptions in two ways. IRIS-NP uses nonlinear programming to find multiple locally separating hyperplanes to each obstacle, until the program becomes infeasible -- an imprecise termination condition that often leaves some obstacle volume in regions. Jaitly and Farzan modified IRIS-NP to use a nonuniform sampling strategy to seed the collision search program. The other option is to use a rational reparametrization of the kinematics to construct regions that are rigorously certified to be collision-free with sums-of-squares programming. However, such optimizations are computationally expensive, and the regions are grown in a stereographic projection of configuration space, which distorts distances.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Related Works", "weight": 1.0} -->

Alternatively, directly decomposes three-dimensional spaces into polytopes only using sample-based collision-checking. Unfortunately, this approach requires dense sampling of the configuration space to produce large sets which is intractable in all but the simplest cases.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IRIS with Convex Obstacles", "weight": 1.0} -->

IRIS, takes as input $N_{o}$ convex obstacles $\mathcal{O}_{i}$ and a collision-free seed point $s \in \mathcal{C}^{free}$. IRIS then computes a large collision-free polytope by alternating between two convex optimizations: the SeparatingPlanes step, that produces a polytope conditioned on an initial ellipsoid, and the InscribedEllipsoid step, which updates the ellipsoid to the maximum-volume inscribed ellipsoid (MVIE) \[21, §8.4.2\] in the current polytope. These alternations guarantee the containment of the ellipsoid, and hence, guarantee that the volume of the MVIE is monotonically increasing across alternations. To understand the upcoming modifications to IRIS-NP, we review the SeparatingPlanes step in detail.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IRIS with Convex Obstacles", "weight": 1.0} -->

The SeparatingPlanes step starts with a collision-free ellipsoid $\mathcal{E}$, that is centered at $c$ with a symmetric, positive-definite matrix $E$. For each of the $N_{o}$ obstacles, IRIS computes a hyperplane that separates $c$ from $\mathcal{O}_{i}$ and passes through the point in $\mathcal{O}_{i}$ that lies closest to the ellipsoid center $c$ in the metric of the ellipsoid. This is done by solving where ${\| x\|}_{E}^{2}:={x^{T}Ex}$. Given the optimum $x_{i}^{\star}$, the hyperplane separates $c$ from $\mathcal{O}_{i}$ and does not intersect $\mathcal{E}$ \[9, §3.5\]. This step is performed for each obstacle.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IRIS with Convex Obstacles", "weight": 1.0} -->

Finally, the intersection of the halfspaces ${a_{i}^{T}x} \leq b_{i}$ yields an updated collision-free polytope.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Computing Separating Planes in Robot Configuration Space", "weight": 1.0} -->

IRIS requires convex obstacles to ensure the convexity of. However, configuration-space obstacles are generally non-convex. IRIS-NP generalizes the closest-point-in-obstacle program for the configuration-space obstacle $\mathcal{O}^{\mathcal{A}\mathcal{B}}$. To avoid intractable descriptions of $\mathcal{O}^{\mathcal{A}\mathcal{B}}$, the collision constraint is encoded in task space.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Computing Separating Planes in Robot Configuration Space", "weight": 1.0} -->

Optimization variables represent a point in each of the collision geometries, $t_{\mathcal{A}} \in \mathcal{A}$, $t_{\mathcal{B}} \in \mathcal{B}$, in their body frames, constrained by ${{{}_{}^{W}X_{}^{B_{\mathcal{A}}}}t_{\mathcal{A}}} = {{{}_{}^{W}X_{}^{B_{\mathcal{B}}}}t_{\mathcal{B}}}$, to coincide in task space when transformed through the forward kinematics. For clarity, in this paper, we write this as requiring a single point $t$ to lie in the intersection of the associated pair of collision geometries in task space. This is shown in Fig. 1. In order to ensure that new hyperplanes address obstacles still relevant to the current polytope $\mathcal{P}$, IRIS-NP requires the found points in collision to lie inside $\mathcal{P}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Computing Separating Planes in Robot Configuration Space", "weight": 1.0} -->

The full nonlinear program then reads: Because configuration-space obstacles are generally non-convex, multiple hyperplanes may be necessary to separate $c$ from $\mathcal{O}^{\mathcal{A}\mathcal{B}}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Computing Separating Planes in Robot Configuration Space", "weight": 1.0} -->

To construct the separating hyperplanes for the collision pair $(\mathcal{A},\mathcal{B})$, IRIS-NP repeatedly finds locally optimal solutions $q^{\star}$ to, adding the hyperplane to $\mathcal{P}$ for each of the found points $q^{\star}$ in collision. More precisely, the polytope $\mathcal{P}$ is updated by intersecting $\mathcal{P}$ with the halfspace $\left. \{ q \middle| {{a_{i}^{T}q} \leq {b_{i} - \Delta}}\} \right.$, where $\Delta > 0$ is a user-specified stepback. This stepback ensures that the collision configuration $q^{\star}$ is excluded from $\mathcal{P}$, and prevents the need for an infinite number of hyperplanes to exclude a non-convex obstacle. This is repeated until a fixed number of attempted solves of fail; IRIS-NP interprets this failure as a suggestion that $\mathcal{P}$ is sufficiently collision-free.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Computing Separating Planes in Robot Configuration Space", "weight": 1.0} -->

However, note that due to the local nature of nonlinear programming, a single failed solve often provides inconclusive information about the feasibility of the overall program.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Computing Separating Planes in Robot Configuration Space", "weight": 1.0} -->

To summarize, the IRIS-NP strategy to approximating SeparatingPlanes in robot configuration space is to create a list of all valid collision pairs ordered by their task-space distance, and, for each collision pair, repeatedly find locally optimal solutions to and update $\mathcal{P}$ until a user-specified number of consecutive solve attempts fail. Through this procedure, IRIS-NP strives to make $\mathcal{P}$ collision-free with respect to all valid collision pairs. See Fig. 2 for an illustration.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Improving the Separating Hyperplanes Routine", "weight": 1.0} -->

This section discusses how we leverage sampling to produce a rigorous termination condition for SeparatingPlanes in robot configuration space (see sec. 4.2), and two improved approaches for solving the step, yielding the new algorithms IRIS-ZO and IRIS-NP2, whose parameters are given in Tab. 1. Both of these new formulations follow the same alternation scheme as IRIS-NP, given in Alg. 1.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Improving the Separating Hyperplanes Routine", "weight": 1.0} -->

In particular, we still initialize the ellipsoid with a small ball of radius $r_{\text{start}}$ and employ the same overall termination conditions for the alternations as \[2, §II.D\], such as the seed point $s$ no longer being contained in $\mathcal{P}$, reaching a maximum number of alternations, or achieving convergence of the ellipsoid volume. Our proposed termination condition for SeparatingPlanes decides when $\mathcal{P}$ meets a correctness criterion based on polytope fraction in collision, not when to terminate the alternations. We discuss the proposed termination condition in Sec. 5.1, before discussing IRIS-ZO in Sec. 5.2, and IRIS-NP2 in Sec. 5.3.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Improving the Separating Hyperplanes Routine", "weight": 1.0} -->

Admissible fraction of the region in collision Max admissible uncertainty Configuration margin, i.e.“step back” Number of optimized particles per inner iteration Number of bisection steps Max number of hyperplanes added per inner iteration Table 1: Glossary of algorithm parameters.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Improving the Separating Hyperplanes Routine", "weight": 1.0} -->

Input: Domain 𝒟 ⊆ 𝒞, collision-free seed s ∈ 𝒟, options O. Algorithm: ℰ ← Ball(s, rstart), i ← 1 while not done do 𝒫 ← SeparatingPlanes(𝒟, ℰ, i, O) ⊳ employs new term. cond. Algorithm 1 Template for the new IRIS algorithms

<!-- chunk {"id": "body-0033", "role": "body", "section": "Termination Condition for the Separating Planes Step", "weight": 1.0} -->

In this section, we discuss a termination condition that allows a user to specify a desired bound on the fraction of the volume of the polytope $\mathcal{P}$ in collision. In the following, let $\varepsilon_{tr}:={{{\lambda{({\mathcal{P} \smallsetminus \mathcal{C}^{free}})}}/\lambda}{(\mathcal{P})}}$ denote the true fraction in collision of $\mathcal{P}$, where $\lambda$ is the Lebesgue measure over $\mathcal{C}^{free}$, and $\varepsilon$ is the specified admissible fraction in collision. A naive approach may be to sample uniformly in the polytope $\mathcal{P}$, estimate the fraction of $\mathcal{P}$ in collision $\hat{\varepsilon}$ to be equal to the fraction of these samples that are in collision, and terminate if $\hat{\varepsilon} \leq \varepsilon$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Termination Condition for the Separating Planes Step", "weight": 1.0} -->

However, each time we perform this check, there is some chance of underestimating $\varepsilon_{tr}$ such that we incorrectly terminate with a polytope with $\varepsilon_{tr} > \varepsilon$. The probability of false termination accumulates over the multiple evaluations of this condition.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Termination Condition for the Separating Planes Step", "weight": 1.0} -->

Instead, we propose a statistical test that controls the probability of falsely claiming a polytope is sufficiently collision-free and terminating. For some user-specified uncertainty $\delta$, a correct termination condition allows a region with $\varepsilon_{tr} > \varepsilon$ to be returned with probability at most $\delta$. To accomplish this, we pair union bounds with a simple statistical test based on a Chernoff bound.

<!-- chunk {"id": "body-0036", "role": "body", "section": "The IRIS-ZO Algorithm", "weight": 1.0} -->

The IRIS-ZO algorithm uses a simple parallelized zero-order optimization strategy to directly solve SeparatingPlanes in Alg. 1 for all collision pairs simultaneously. We call this subroutine ZeroOrderSeparatingPlanes and summarize it in Alg. 2. Fig. 3 illustrates how ZeroOrderSeparatingPlanes optimizes hyperplanes.

<!-- chunk {"id": "body-0037", "role": "body", "section": "The IRIS-ZO Algorithm", "weight": 1.0} -->

Input: Domain 𝒟 ⊆ 𝒞, ellipsoid ℰ = (E, c), current outer iteration i ∈ ℕ. Output: Polytope 𝒫 ⊆ 𝒟 satisfying for (ε, δi). If UnadaptiveTest(δi, k, ε, τ) returns accept then break. 𝒮col⋆ ← UpdatePointsViaBisection(𝒮col, c) The ZeroOrderSeparatingPlanes step constructs a probabilistically collision-free polytope $\mathcal{P}$ by repeating 5 steps until the statistical test passes. We take as input the domain $\mathcal{D}$, the current ellipsoid $\mathcal{E}$, the current outer iteration $i$ and options that are summarized in Tab. 1. Here, we assume that the center of the current ellipsoid is collision-free. We then initialize $\mathcal{P}$ with the domain $\mathcal{D} = \left.

<!-- chunk {"id": "body-0038", "role": "body", "section": "The IRIS-ZO Algorithm", "weight": 1.0} -->

The first step is to uniformly sample a batch of configurations $\mathcal{S}$ in $\mathcal{P}$ via hit-and-run sampling with a batch size of $\text{max}{\{ M,N_{p}\}}$. Then, we find all configurations $\mathcal{S}_{\text{col}} \subseteq \mathcal{S}$ that are in collision by running a collision checker. These samples are used to check the termination condition by running the unadaptive test, returning $\mathcal{P}$ if it accepts. More precisely, counting the collisions $|\mathcal{S}_{\text{col}}^{M}|$ in the first $M$ samples in $\mathcal{S}$ and accepting if ${|\mathcal{S}_{\text{col}}^{M}|} \leq {M{({1 - \tau})}\varepsilon}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "The IRIS-ZO Algorithm", "weight": 1.0} -->

If the probabilistic test fails, we then add hyperplanes to the polytope. We produce candidate solutions for the closest point in collision program based on the first $N_{\text{p}}$ configurations $q$ in $\mathcal{S}_{\text{col}}$. For each $q$, we use bisection search to step toward the center $c$ of the ellipsoid, while ensuring that $q$ is still in collision. In practice, we bisect a fixed number $N_{b}$ of times and pick the configuration $q^{\star}$ that is closest to $c$ and still in collision. This yields our updated batch $\mathcal{S}^{\star}$. This strategy is guaranteed to converge to the boundary of an obstacle for each configuration $q$, but not necessarily the obstacle containing the original $q$ or the one that is closest to $c$. Because this optimization procedure is gradient-free and only relies on a collision checker, it is highly parallel and its performance scales with available computational resources.

<!-- chunk {"id": "body-0040", "role": "body", "section": "The IRIS-ZO Algorithm", "weight": 1.0} -->

Finally, we order all candidates $q^{\star} \in \mathcal{S}_{\text{col}}^{\star}$ by ellipsoidal metric in ascending order. We repeatedly pick the closest candidate $q^{\star}$ in the polytope and add a hyperplane at that point tangent to the ellipsoid, until we hit $N_{f}$ non-redundant hyperplanes or run out of candidates.

<!-- chunk {"id": "body-0041", "role": "body", "section": "The IRIS-NP2 Algorithm", "weight": 1.0} -->

The IRIS-NP2 algorithm (Alg. 3) places hyperplanes more carefully than IRIS-ZO, increasing runtime in favor of larger regions with fewer hyperplanes, while still improving upon IRIS-NP runtimes. Like IRIS-NP, IRIS-NP2 uses nonlinear programming, solving to find separating hyperplanes. In contrast to IRIS-NP, IRIS-NP2 always initializes NLP searches with feasible initial guesses $q_{0}$, prioritizing initial guesses with lower ellipsoid metric ${\|{q_{0} - c}\|}_{E}^{2}$. These initial guesses, along with the corresponding pair of bodies in collision, $(\mathcal{A},\mathcal{B})$ such that ${{\mathcal{A}{(q)}} \cap {\mathcal{B}{(q)}}} \neq \varnothing$, are obtained via a subroutine GetConfigInCollision, two options for which are outlined at the end of this section.

<!-- chunk {"id": "body-0042", "role": "body", "section": "The IRIS-NP2 Algorithm", "weight": 1.0} -->

Input: Domain 𝒟 ⊆ 𝒞, ellipsoid ℰ = (E, c), current outer iteration i ∈ ℕ Output: Polytope 𝒫 ⊆ 𝒟 satisfying for (ε, δi). if q0 is not None then q*← solve with initial guess q0, with pair (𝒜, ℬ) Add hyperplane defined by (a, b) to 𝒫 until UnadaptiveTest(δi, k, ε, τ) returns accept; This strategy of always using a feasible initial guess presents a major advantage over IRIS-NP, as IRIS-NP spends substantial time in NLP solves that return infeasible. In part, this property of IRIS-NP is due to initializing NLP searches with uniform samples $q_{0}$, in the hopes that the nonlinear program solver can pull those $q_{0}$ not in collision into collision to return feasible optimized solutions $q^{\star}$. In practice, this frequently fails even when the polytope does contain collisions. Furthermore, as discussed in Sec. 4.2, IRIS-NP requires that many consecutive NLP solves return infeasible in order to terminate.

<!-- chunk {"id": "body-0043", "role": "body", "section": "The IRIS-NP2 Algorithm", "weight": 1.0} -->

Assessing termination readiness via the Bernoulli trials is faster, allowing the NLP, which is slow to solve, to be used only to construct hyperplanes. Another advantage of this strategy is it scales better with environment complexity. IRIS-NP must solve a minimum number of NLPs for every valid collision pair. This quantity grows quickly with scene complexity, while many of these pairs never actually collide, resulting in infeasible NLPs and wasted computation time. IRIS-NP2 only considers pairs known to collide, and hence solves only feasible NLPs. We present two options for GetConfigInCollision, with differing costs and benefits.

<!-- chunk {"id": "body-0044", "role": "body", "section": "The IRIS-NP2 Algorithm", "weight": 1.0} -->

For the *Greedy Collision Finder*, all samples from the Bernoulli trial that are in collision are aggregated and sorted in ascending order of distances to the center point of the ellipsoid, w.r.t. the ellipsoidal metric. (In effect, $N_{p}$ is dynamically set to equal the number of collision particles.) When queried, this subroutine returns the sample with the next-lowest ellipsoid metric, until all in-collision samples from the Bernoulli trial have been exhausted. If a sample is not in the polytope (due to new hyperplanes from an earlier sample), it would no longer be a feasible initial guess for Equation 6, so None is returned.

<!-- chunk {"id": "body-0045", "role": "body", "section": "The IRIS-NP2 Algorithm", "weight": 1.0} -->

The *Ray Collision Finder* (Fig. 4) prioritizes the quality of the constructed hyperplanes via an inexpensive line search to find configurations in collision near the ellipsoid center. The ray collision finder takes a subset of the samples drawn for the Bernoulli trial, and, for each sample, steps outward in discrete steps along the ray from the ellipsoid center through the sample. The first step in collision is returned. If a step has exited the polytope, None is returned. This discrete search serves a purpose similar to the objective of: to limit the hyperplanes needed, we desire to add hyperplanes at the closest (in the ellipsoid metric) points in collision. Because the discrete search is not restricted to a specific collision pair, it may find configuration-space obstacles closer than. In contrast to the bisection search performed by IRIS-ZO, this line search sweeps monotonically outward from the ellipsoid center in an attempt to find the closest collision; the IRIS-ZO bisection search steps inward from the sample, finding a point on a boundary of a configuration-space obstacle. (The ray may pass through several such boundaries.)

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experiments", "weight": 1.0} -->

To evaluate our proposed changes to the IRIS-NP algorithm, we designed a comprehensive benchmark. This benchmark includes eight different robotic systems, described in Fig. 5. For each benchmark, we select 10 seed configurations manually, placing the robot in a variety of configurations in its environment. Each experiment is run for a single outer iteration, to isolate performance differences in the SeparatingPlanes steps.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experiments", "weight": 1.0} -->

We compare the approaches for two different settings: a "fast" setting, where we request the region to be $90\%$ collision-free, with $90\%$ confidence, and a "precise" setting, where we request the region to be $99\%$ collision-free with $95\%$ confidence. IRIS-NP cannot take these arguments directly, so we hand-tune the required number of consecutive infeasible solves to roughly match the average collision fractions achieved by our algorithms. For IRIS-NP2, we tuned the algorithm hyperparameters of Tab. 1 on a per-experiment basis.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experiments", "weight": 1.0} -->

To mitigate the effects of randomness of the algorithms in our comparisons, we constructed regions around each seed point 10 times. This yields 100 trials per robot environment, or 800 total, for each algorithm. For the parallelized components of the algorithms, an Intel Core i9-10850K (10 cores, 20 threads) is used. All convex programs are solved using MOSEK and the nonlinear programs are solved using SNOPT. The volume of the maximum-volume inscribed ellipsoid is used as a proxy for polytope volume. We report these volumes normalized by the averaged IRIS-NP results.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Experiments", "weight": 1.0} -->

For each algorithm and robotic system, we include the runtime, number of hyperplanes, volume, and proportion of the region in collision, averaged over all trials on all seed points in Tab. 2. Region volume and number of hyperplanes are both dependent on the seed configuration -- if the robot is in a narrow passageway, the region may be small, and if it is near obstacles, many hyperplanes may be required. In Fig. 6, we visualize the runtime and hyperplane data across the 10 trials for the 8 corresponding seed configurations shown in Fig. 5. Our algorithms show significant improvements relative to IRIS-NP in runtime and number of hyperplanes. In particular, IRIS-ZO gains approximately an order-of-magnitude time advantage with a comparable number of hyperplanes. While IRIS-NP2 is slower than IRIS-ZO, it generally remains faster than IRIS-NP and uses significantly fewer hyperplanes.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Discussion", "weight": 1.5} -->

In recent years, region generation has posed a major roadblock for the adoption of new motion planning approaches such as. Toward alleviating this roadblock, we have presented significant improvements to the IRIS-NP algorithm, reducing its runtime, making it more user-friendly, and increasing the quality of the resulting regions. We derive a probabilistic test for the proportion of a given region that is collision-free, allowing the user to more directly trade off algorithmic precision and speed. We have also presented new approaches to the SeparatingPlanes subroutine, which show significantly better performance than IRIS-NP, while consistently achieving the user-specified collision-free threshold. IRIS-NP2 is generally faster and requires fewer hyperplanes to define the polytopes. IRIS-ZO is easy to implement is around 15 times faster and often uses fewer hyperplanes than IRIS-NP, although the regions are smaller. Furthermore, these new approaches scale more favorably with the complexity of the environment. As they are deployed in environments with increasingly many collision geometries, we anticipate the performance gap will grow even further. Besides the quantitative improvements, the hyperparameters are straightforward to tune and have clear effects on the behavior of the algorithm.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Discussion", "weight": 1.5} -->

There are myriad directions for future research. Better parallelization is a promising direction to speed up both new approaches -- beyond CPU-level multithreading, SIMD instructions and GPU programming have shown great promise for collision-checking. In particular, we regard better hardware usage for IRIS-ZO particularly promising, as both the sampling and the particle updates are trivially parallelizeable and currently bottle-necked by the number of threads in the CPU. Furthermore, using samples that are almost in-collision to initialize IRIS-NP2 might aid in finding small obstacles when requesting regions with a very small proportion in collision. Finally, we have focused on runtime and number of hyperplanes as our primary objectives, but more closely examining the relationship between the generated regions and the downstream motion planning algorithms will be essential for further improving the results. In particular, we aim to investigate how to improve efficient cover generation as.
