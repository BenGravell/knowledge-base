<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Semidefinite Relaxations for Collision-Free Motion Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study semidefinite relaxations for collision-free motion planning. We focus on a point robot moving from start to goal through spherical obstacles in R^(n), subject to path continuity constraints and squared derivative costs; a setting that is conceptually simple yet captures the hardness of collision-free motion planning. We formulate this problem exactly as a nonconvex problem over polynomial curves, and present a natural semidefinite relaxation. We contribute two key theoretical insights; to our knowledge this is the first theoretical analysis of semidefinite relaxations for collision-free motion planning. First, we show that solving the convex relaxation is equivalent to solving, to global optimality, a related motion planning problem in a potentially higher-dimensional space. This geometric interpretation yields necessary and sufficient conditions for tightness, and a clear intuition for when the relaxation is loose. Second, we show that the relaxation admits a symmetry reduction that makes it significantly smaller than one might expect, with positive semidefinite cone sizes that scale linearly with the polynomial degree and are independent of the ambient dimension.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The resulting relaxation is 10 to 100 times faster than direct nonlinear programming transcriptions solved with SNOPT and IPOPT, exhibits significantly lower variance in solve times, and reliably finds a locally optimal path for the original problem. We demonstrate its effectiveness as a convex steering function in an RRT planner for minimum-snap quadrotor planning with C^ continuous trajectories.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Collision-free motion planning -- the problem of finding a smooth trajectory between two configurations that avoids a set of obstacles -- is a fundamental challenge in robotics and autonomous systems. Even in simple settings, the problem is computationally difficult due to the nonconvexity of the obstacle avoidance constraints. In the case of a point robot navigating among sphere obstacles in $\mathbb{R}^{2}$, the minimum length path can be computed in polynomial time, but the problem becomes NP-hard in $\mathbb{R}^{3}$ for polyhedral obstacles, and the complexity for disjoint unit sphere obstacles in $\mathbb{R}^{3}$ remains an open problem \[3, Section 31.5\]. In robotics, however, minimum path length is rarely the only consideration; motion planning typically involves costs such as time, energy, or snap, subject to constraints such as boundary conditions, derivative bounds, and continuity constraints. For this more general problem setting, no efficient algorithm is known.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Several approaches have been proposed to solve collision-free motion planning in practice. Optimization-based methods parametrize the trajectory as a piecewise polynomial and naturally handle different costs and constraints. A popular approach is to use trajectory optimization with Nonlinear Programming (NLP), but nonconvex optimization can be brittle and sensitive to the initial guess. Another approach sidesteps the nonconvexity of obstacle avoidance by precomputing a convex decomposition of the free-space, which can itself be a hard problem, and then plan through the decomposition with convex optimization. This has proven particularly effective for multiquery planning in a single environment. On the other hand, sampling-based planners are capable of global reasoning, but are unable to naturally reason about trajectory constraints. An alternative is to combine sampling-based planners with local trajectory optimization, either by post-processing a sampled geometric path, by precomputing motion primitives offline, or by embedding a local solver as a steering function within the sampler. Geometric sampling with post-processing does not reason about dynamic feasibility during exploration, often making the sampled path a poor initialization for optimization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Using optimization as the steering function addresses this, but jointly reasoning about obstacles and trajectory constraints is typically nonconvex, and the resulting NLP solves can be brittle with highly variable solve times, often making this impractical.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, semidefinite relaxations have emerged as a powerful tool for solving certain classes of nonconvex optimization problems. Through the Sum-of-Squares (SOS)/moment hierarchy, one can construct a sequence of increasingly strong relaxations, at the cost of growing computational complexity. These relaxations use convex optimization, and therefore do not suffer from being brittle or relying on an initial guess. The application of semidefinite relaxations has seen success in estimation and perception problems such as point cloud registration, pose-graph SLAM and range-aided SLAM, and has lately been applied to some motion planning problems, such as planning through contact. However, the behavior of semidefinite relaxations for collision-free motion planning is poorly understood, and to our knowledge no theoretical analysis of their properties in this setting has been given.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we study semidefinite relaxations for collision-free motion planning. In particular, we focus on the problem of a point robot navigating from a start to a goal in a field of spherical obstacles in $\mathbb{R}^{n}$, minimizing a squared derivative cost (such as minimum energy or minimum snap) subject to path continuity constraints and boundary conditions. This setting is conceptually simple yet captures the hardness of motion planning. We formulate this problem for polynomial curves exactly as a nonconvex problem, and present a natural semidefinite relaxation of it. Our core contribution is a geometric interpretation of the relaxation: we show it is equivalent to solving, to global optimality, a related collision-free motion planning problem in a space of potentially higher dimension than the original ambient space $\mathbb{R}^{n}$. This yields necessary and sufficient conditions for when the relaxation is exact, and a clear intuition for when the relaxation is loose.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Beyond the theoretical analysis, we show that the relaxation provides a fast and reliable convex subroutine for motion planning. This is enabled by two properties of our formulation. First, we use a classical result from SOS to certify exactly when a polynomial curve avoids a spherical obstacle, without the need for discretization. The resulting Linear Matrix Inequality (LMI) condition takes a particularly nice form, with PSD constraints that scale linearly with the polynomial trajectory degree $d$ and are independent of the ambient dimension $n$. Second, the LMI condition is nonconvex in the trajectory coefficients, so we formulate a first-order semidefinite relaxation to obtain a convex program. A naive application of the well-known Shor relaxation yields a large program, but we exploit symmetry to reduce the size of the PSD cone by a factor of $n$. Together, these properties yield a relaxation that is 10 to 100 times faster than direct nonlinear programming transcriptions solved with SNOPT and IPOPT, exhibits significantly lower variance in solve times, and reliably finds a locally optimal path.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate the effectiveness of using our method as a convex and robust steering function in an RRT, planning $C^{4}$ continuous, minimum-snap collision-free trajectories through highly cluttered environments.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Related Works", "weight": 1.0} -->

In this section, we review relevant works on semidefinite relaxations for motion planning and optimal control. As discussed in the introduction, there is also a substantial body of work on semidefinite relaxations for perception and estimation problems, which we do not review here.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Related Works", "weight": 1.0} -->

Several works apply semidefinite relaxations to motion planning and control problems and empirically observe tight relaxations, though without analyzing when or why they are tight. Teng et al. formulate kinodynamic motion planning for rigid body systems as exact polynomial optimization problems, using a variational integrator to discretize the dynamics on Lie groups. They apply the moment hierarchy and empirically find that tight solutions are obtained at the second order of the hierarchy for most systems they consider. Similarly, Häring et al. study minimum-energy control of the unicycle model and empirically show that the second-order relaxation is tight. In, Vega et al. formulate spacecraft maneuver planning with a single spherical keep-out zone (analogous to considering a single spherical obstacle) as a Quadratically Constrained Quadratic Program (QCQP) with linearized dynamics, and apply the Shor relaxation to obtain empirically tight solutions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Related Works", "weight": 1.0} -->

Recently, a setting similar to ours was considered by Mahajan et al., who apply the Shor relaxation to collision-free MPC with spherical obstacles and discretized collision-avoidance constraints, focusing on developing a custom cached Riccati-based ADMM solver that enables real-time rates on embedded hardware.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Related Works", "weight": 1.0} -->

A related line of work applies semidefinite relaxations to time-scaled optimal control. Yang et al. develop a tailored semidefinite relaxation for linear and piecewise-affine systems and combine it with convex decompositions of the free-space and Graph of Convex Sets (GCS) to jointly optimize mode sequences and time-optimal collision-free trajectories. Dong et al. apply a similar relaxation to jointly optimize trajectories and time allocations for optimal control problems with spatio-temporal constraints, such as a quadrotor required to pass through a sequence of known waypoints within specified time windows, and exploit the banded sparsity of the multiple shooting formulation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Related Works", "weight": 1.0} -->

Semidefinite relaxations have also been applied to contact-rich planning. Graesdal et al. relax the contact dynamics of planar pushing with the first-order semidefinite relaxation, strengthen the formulation with implied constraints, and use GCS to plan optimal contact mode sequences. Kang et al. apply the moment hierarchy to a broader class of contact-rich planning problems, encoding the discrete mode sequence directly in the hierarchy rather than through GCS, and leverage problem-specific sparsity to obtain solutions at the second or third order of the hierarchy. Finally, Wei and Dümbgen take a different approach: they sample trajectory rollouts and use KernelSOS, a global optimization technique that builds a nonparametric surrogate of the cost landscape and minimizes it using semidefinite optimization, to find promising regions of the search space that are then refined with a sampling-based local optimizer.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Related Works", "weight": 1.0} -->

In contrast to these works, which apply semidefinite relaxations to various planning problems and observe tightness empirically, our goal is to understand *when* the relaxation is tight. We therefore study a deliberately simplified setting, rich enough to capture the core difficulty of collision-free planning yet simple enough to admit a precise analysis. This setting also reveals a symmetry that reduces the SDP to a size independent of the ambient dimension, which can be combined with the correlative sparsity exploited in prior work.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Motion Planning", "weight": 1.0} -->

In this section, we state the optimal collision-free motion planning problem exactly, as an optimization over curves where the entire curve must be collision-free. This problem is infinite-dimensional since the decision variable is a curve, and cannot be solved numerically as stated. To address this, we restrict the curves to polynomials and define the class of curve costs we consider. The result is a semi-infinite QCQP: the decision variables are finite-dimensional, but the obstacle-avoidance constraints must hold at every point along the curve. In the next section, we use SOS to reformulate the collision-avoidance constraint exactly as LMI conditions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Problem Statement", "weight": 1.0} -->

We seek a collision-free path that minimizes the sum of the squared $\ell_{2}$-norm of its derivatives, such as velocity or snap, subject to boundary conditions and continuity constraints. Let the trajectory be represented as a curve $q:\rightarrow\mathbb{R}^{n}$. We require the trajectory $q$ to be $\eta$-times continuously differentiable, that is, $q\in\mathcal{C}^{\eta}$, and denote $q^{(i)}=(d^{i}/ds^{i})q$ as the $i$-th derivative. We consider $m$ spherical obstacles with centers $c_{j}\in\mathbb{R}^{n}$ and radii $r_{j}>0$, for $j=1,\ldots,m$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Problem Statement", "weight": 1.0} -->

We formulate the motion planning problem as the following nonconvex optimization problem: where $k\in\mathbb{N}_{+}$ is the derivative order for the cost, and there are boundary conditions up to the $\ell$-th derivative on the curve. For motion planning, common choices for $k$ include $k=1$ (minimum energy), $k=2$ (minimum acceleration), and $k=4$ (minimum snap). The problem is nonconvex due to (1b). The problem is infinite-dimensional: the decision variable $q$ is a function in $C^{\eta}$, and for each obstacle $j$, the avoidance condition (1b) represents a continuum of nonconvex constraints indexed by $s\in$. As such, it is unclear how to solve problem numerically.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Polynomial Curves", "weight": 1.0} -->

We parametrize the curve as a piecewise polynomial, where each segment is a polynomial curve $\gamma:\rightarrow\mathbb{R}^{n}$ of degree $d$: where $b_{d}(s):\mathbb{R}\rightarrow\mathbb{R}^{d+1}$ is a basis of polynomials of degree less than or equal to $d$ in the variable $s$, and $\Gamma\in\mathbb{R}^{n\times(d+1)}$ is the corresponding coefficient matrix. With this parametrization, the decision variables for each segment reduce to the coefficient matrix $\Gamma$, and becomes an optimization problem with a finite number of variables, albeit still with an infinite number of constraints.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Polynomial Curves", "weight": 1.0} -->

To keep the presentation clean, we develop all formulations for a single segment. This is not a restriction of the formulation, as the cost and collision-avoidance constraints in decompose across the polynomial segments, which are coupled only through linear continuity constraints, so the extension to multiple segments is straightforward. We likewise present these formulations in a basis-independent form, specializing to the Bernstein basis only for our numerical experiments and a few key results.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-C Curve Costs", "weight": 1.0} -->

For a polynomial curve $\gamma$ of degree $d$ as defined, the squared $\mathcal{L}_{2}$ norm of the $k$-th derivative can be expressed as is the $k$-th derivative Gram matrix of degree $d$, $D_{k}\in\mathbb{R}^{(d+1)\times(d+1-k)}$ is the differentiation matrix defined by $b^{(k)}_{d}(s)=D_{k}b_{d-k}(s)$, and is the basis-dependent Gram matrix of degree $d$. Both $G_{d}$ and $G^{(k)}_{d}$ can be computed analytically for any choice of basis. To keep notation light, we write $G$ and $G^{(k)}$ when the degree $d$ is clear from context. See subsection -D1 for explicit expressions for polynomials represented as Bézier curves, i.e. with the Bernstein basis.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Curve Costs", "weight": 1.0} -->

The nullspace of $G^{(k)}_{d}$ characterizes the zero-cost directions of the polynomial trajectory, which we use in our theoretical analysis in Section VI.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-D Semi-Infinite QCQP Reformulation", "weight": 1.0} -->

We reformulate the motion planning problem in the polynomial coefficient matrix $\Gamma\in\mathbb{R}^{n\times(d+1)}$. The result is a semi-infinite QCQP, which has a finite number of decision variables, but obstacle avoidance must still hold point-wise for all $s\in$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-D Semi-Infinite QCQP Reformulation", "weight": 1.0} -->

To keep notation light, we present the derivation for a single unit sphere centered at $c\in\mathbb{R}^{n}$. The condition that $\gamma$ avoids the sphere is equivalent to the polynomial nonnegativity condition: To write the nonnegativity condition in terms of the coefficient matrix $\Gamma$, we first express the shifted curve $\gamma(s)-c$ in the polynomial basis $b_{d}(s)$. We introduce a vector $u\in\mathbb{R}^{d+1}$ satisfying $u^{T}b_{d}(s)=1$, so that $\gamma(s)-c=\Gamma b_{d}(s)-c\cdot 1=(\Gamma-cu^{T})b_{d}(s)$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-D Semi-Infinite QCQP Reformulation", "weight": 1.0} -->

Using this, together with $1\cdot 1=b_{d}(s)^{T}uu^{T}b_{d}(s)$, can be rewritten as the quadratic form which is a univariate polynomial in $s$ of degree $2d$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-D Semi-Infinite QCQP Reformulation", "weight": 1.0} -->

Combining the cost, the obstacle condition, and the boundary conditions, the polynomial motion planning problem is where $A$ and $B$ encode the boundary conditions (1d) and (1e) on the first $\ell$ derivatives: The problem is naturally written in matrix form. The cost and obstacle constraint are both quadratic in $\Gamma$, making the problem a semi-infinite QCQP.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Certifying Collision-Avoidance", "weight": 1.0} -->

Condition is the nonnegativity of a univariate polynomial over an interval, which we know how to rewrite exactly using SOS. In this section, we show that the resulting conditions take a particularly nice form that is independent of the ambient dimension $n$ of the curve and scales linearly with the polynomial degree $d$. The conditions are quadratic in the polynomial coefficients $\Gamma$, so for a fixed trajectory, certifying collision-avoidance reduces to an SDP. When searching over trajectories, the conditions are nonconvex, which we address in the next section. We first derive the condition in a basis-free fashion, before presenting a concrete instance of it for the Bernstein basis.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Collision-Avoidance with Bézier Curves", "weight": 1.0} -->

Bézier curves, which are polynomial curves expressed in the Bernstein basis, are a common choice in motion planning. We instantiate the collision-avoidance conditions of Lemma 2. ‣ IV-A Basis-Independent Derivation ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning") in the closely related scaled Bernstein basis, which drops the binomial coefficients and yields simpler expressions. Our implementation uses the standard Bernstein basis for its better numerical conditioning, with the corresponding expressions given in Subsection -D2.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Collision-Avoidance with Bézier Curves", "weight": 1.0} -->

The $i$-th scaled Bernstein basis polynomial of degree $d$ is defined as for $s\in$. Recall from Lemma 2. ‣ IV-A Basis-Independent Derivation ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning") that we require a vector $u$ satisfying $u^{T}b_{d}(s)=1$. By the binomial theorem, so we take $u_{i}=\binom{d}{i}$ for $i=0,\ldots,d$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Collision-Avoidance with Bézier Curves", "weight": 1.0} -->

We now make the collision-avoidance condition from Lemma 2. ‣ IV-A Basis-Independent Derivation ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning") explicit for the scaled Bernstein basis. The derivation follows standard SOS coefficient matching, which takes a particularly simple form in this basis due to the key identity which follows immediately from the definition of the scaled Bernstein basis polynomials.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Collision-Avoidance with Bézier Curves", "weight": 1.0} -->

From this, a quadratic form in $b_{d}(s)$ (like the one in) can be expressed in the basis $b_{2d}(s)$ as where $\mathcal{S}_{d}:\mathbb{S}^{d+1}\rightarrow\mathbb{R}^{2d+1}$ sums along the anti-diagonals of $M$: the product $s(1-s)\cdot b_{d-1}(s)^{T}Mb_{d-1}(s)$ can be expressed in the basis $b_{2d}(s)$ as where $\mathcal{T}_{d}:\mathbb{S}^{d}\rightarrow\mathbb{R}^{2d+1}$ is a shifted version of $\mathcal{S}_{d-1}$: Using these maps, we can write the collision-avoidance condition from Lemma 2.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-C The Special Case of Line Segments", "weight": 1.0} -->

For line segments, the LMI condition reduces to a Rotated Second-Order Cone (RSOC) constraint, which is computationally much cheaper. The natural parameterization of a line segment from $\gamma_{0}$ to $\gamma_{1}$, is a Bézier curve of degree $d=1$, for which the scaled and standard Bernstein bases coincide with $b_{1}(s)=(1-s,s)$ and $\Gamma=\begin{bmatrix}\gamma_{0}&\gamma_{1}\end{bmatrix}$. Applying Lemma 3.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Semidefinite Relaxation", "weight": 1.0} -->

Using the results of the previous section, we now rewrite the semi-infinite QCQP as a finite-dimensional nonconvex problem, before deriving a semidefinite relaxation of it.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A Nonconvex Problem", "weight": 1.0} -->

Substituting the LMI condition of Lemma 2. ‣ IV-A Basis-Independent Derivation ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning") for the continuum constraint in the semi-infinite QCQP gives a finite-dimensional nonconvex problem: where the decision variables are $\Gamma\in\mathbb{R}^{n\times(d+1)}$, $Q_{0}\in\mathbb{S}^{d+1}$ and $Q_{1}\in\mathbb{S}^{d}$ (the SOS Gram matrices from (11. ‣ IV-A Basis-Independent Derivation ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning"))). The first constraint in (P) is a quadratic equality constraint in the polynomial coefficients, and is therefore nonconvex.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-B Forming the Relaxation", "weight": 1.0} -->

The nonconvexity in (P) comes from the first argument to $\mathcal{L}$, which expands as We define the Gram matrix of the polynomial coefficients as $X:=\Gamma^{T}\Gamma\in\mathbb{S}^{d+1}$. Substituting into, the right-hand side becomes affine in $X$ and $\Gamma$. Since $\mathcal{L}$ is a linear map, the constraint remains affine in the decision variables $X$, $\Gamma$, $Q_{0}$, and $Q_{1}$. The same substitution makes the cost linear in $X$: $\mathrm{tr}(G^{(k)}\Gamma^{T}\Gamma)=\mathrm{tr}(G^{(k)}X)$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-B Forming the Relaxation", "weight": 1.0} -->

The only remaining nonconvexity is the constraint $X=\Gamma^{T}\Gamma$, which we relax into the convex constraint $X\succeq\Gamma^{T}\Gamma$. Using the Schur complement, we can rewrite the condition as an LMI: where $I_{n}$ is the $n$-dimensional identity matrix.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-B Forming the Relaxation", "weight": 1.0} -->

With this, the convex relaxation of (P) is: This is an SDP in the decision variables $\Gamma$, $X$, $Q_{0}$, and $Q_{1}$. The constraints $XA=\Gamma^{T}B$ are implied by $\Gamma A=B$ when $X=\Gamma^{T}\Gamma$ holds (left-multiply by $\Gamma^{T}$), so they are redundant for (P) but tighten the relaxation.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-C Strict Feasibility and Facial Reduction", "weight": 1.0} -->

Every feasible point of the SDP satisfies so the feasible set lies in a proper face of the PSD cone. As a result, the SDP is never strictly feasible, and solving it directly leads to numerical difficulties. In practice, we address this by eliminating the equality constraints before solving, which restricts the LMI to this face. This is a facial reduction where the reducing certificate is available in closed form. Eliminating the equality constraints amounts to parameterizing the affine subspace defined by $\Gamma A=B$ \[42, Section 10.1.2\], and for Bézier curves in the Bernstein basis, the boundary conditions admit a particularly simple parametrization. The derivatives at each endpoint depend in a triangular manner on the adjacent control points $\gamma=\gamma_{0}$, $\gamma^{\prime}$ depends on $\gamma_{0}$ and $\gamma_{1}$, $\gamma^{\prime\prime}$ on $\gamma_{0},\gamma_{1},\gamma_{2}$, and so on (and similarly at $s=1$, reading from the end).

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-C Strict Feasibility and Facial Reduction", "weight": 1.0} -->

Prescribing derivatives up to $\ell$ at each endpoint therefore fixes the $\ell{+}1$ adjacent control points as known constants, leaving the remaining $d+1-2(\ell{+}1)$ control points free. We can therefore write $\Gamma=BD_{\text{fixed}}+\Gamma_{\text{free}}D_{\text{free}}$, where $\Gamma_{\text{free}}$ collects the free control points and $D_{\text{fixed}},D_{\text{free}}$ are constant matrices that place the boundary data and the free columns into the corresponding columns of $\Gamma$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-C Strict Feasibility and Facial Reduction", "weight": 1.0} -->

Defining the smaller Gram matrix $X_{\text{free}}:=\Gamma_{\text{free}}^{T}\Gamma_{\text{free}}$ and relaxing it into $X_{\text{free}}\succeq\Gamma_{\text{free}}^{T}\Gamma_{\text{free}}$, the LMI reduces in size from $n+d+1$ to $n+d+1-2(\ell{+}1)$. The boundary and tightening constraints are then satisfied by construction, while the cost and collision-avoidance constraints remain linear in $(\Gamma_{\text{free}},X_{\text{free}})$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-D Extension to Multiple Segments", "weight": 1.0} -->

For $N$ segments with polynomial coefficient matrices $\Gamma_{1},\ldots,\Gamma_{N}$ and $\mathcal{C}^{\eta}$ continuity, the relaxation is derived analogously. Specifically, it introduces per-segment Gram matrices $X_{i}$ and cross-Gram matrices $X_{i,i+1}$ between consecutive segments, relaxing the nonconvex constraint via an LMI analogous to: Boundary conditions remain unchanged, and $\mathcal{C}^{\eta}$ continuity between adjacent segments introduces additional linear constraints on $\Gamma_{i}$ of the form $\Gamma_{i}A_{1}=\Gamma_{i+1}A_{0}$, where $A_{1},A_{0}\in\mathbb{R}^{(d+1)\times(\eta+1)}$ collect the endpoint values of the Bernstein basis derivatives at $s=1$ and $s=0$ respectively.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-D Extension to Multiple Segments", "weight": 1.0} -->

Every such linear constraint implies additional tightening constraints on $X_{i}$ and $X_{i,i+1}$, obtained by left-multiplying by $\Gamma_{i}^{T}$ or $\Gamma_{i+1}^{T}$. The facial reduction from the previous subsection extends directly to this setting: continuity contributes $\eta{+}1$ additional dependent columns to each pairwise LMI, reducing its size from $n+2(d{+}1)$ to $n+2(d{+}1)-(\eta{+}1)$ at interior junctions, with a further $\ell{+}1$ removed at pairs containing a global endpoint.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Theoretical Results", "weight": 1.0} -->

We now present our main theoretical results. We first give a geometric interpretation of the relaxation: solving (SDP) is equivalent to solving, to global optimality, a planning problem in a higher-dimensional space. We then use this interpretation to characterize exactly when the relaxation is tight, and give geometric conditions under which the minimizer of the original nonconvex problem is recovered. Finally, we show that our relaxation is a symmetry-reduced version of the Shor relaxation of (P) under an $O(n)$ symmetry. As the rest of the paper can be understood without this last result, we defer it to Subsection -A.

<!-- chunk {"id": "body-0045", "role": "body", "section": "VI-A Geometric Interpretation", "weight": 1.0} -->

Recall that (SDP) is obtained by an algebraic lift, replacing the nonconvex term $\Gamma^{T}\Gamma$ in (P) with the matrix variable $X\succeq\Gamma^{T}\Gamma$. We now give this lift a geometric interpretation. We introduce a family of higher-dimensional, nonconvex problems (P~ρ~), $\rho\in\mathbb{N}$, that allow the path $\rho$ extra spatial dimensions beyond the original $n$ ambient dimensions, while the obstacles and boundary conditions remain in $\mathbb{R}^{n}$. We then show that (SDP) attains the optimal cost over this family, and that an optimal $(n+\rho)$-dimensional path can be recovered from any minimizer.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VI-A Geometric Interpretation", "weight": 1.0} -->

Consider extending the problem (P) from $\mathbb{R}^{n}$ to $\mathbb{R}^{n+\rho}$, for some $\rho\in\mathbb{N}$, in the following sense: Let $v(s)=Vb_{d}(s)\in\mathbb{R}^{\rho}$ be a polynomial curve in the extra $\rho$ dimensions, with coefficient matrix $V\in\mathbb{R}^{\rho\times(d+1)}$ so the full curve is $(\gamma(s),v(s))\in\mathbb{R}^{n+\rho}$. Let the obstacle be a sphere in $\mathbb{R}^{n+\rho}$ centered at $(c,0)$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VI-A Geometric Interpretation", "weight": 1.0} -->

The squared distance to the obstacle center then splits as $\|\gamma(s)-c\|^{2}+\|v(s)\|^{2}$, so the quadratic form extends with an additional $V^{T}V$ term. We require $v$ and its first $\ell$ derivatives to vanish at the boundary: $v^{(i)}=v^{(i)}=0$ for $i=0,\ldots,\ell$, or equivalently $VA=0$. The resulting problem, with $\Gamma$ as in (P), is: This is still a nonconvex problem, and (P~ρ~) reduces to (P) for $\rho=0$. Figure 2 (a) and figure 2 (b) show two different examples with (P) (left) and (P~ρ=1~) (right).

<!-- chunk {"id": "body-0048", "role": "body", "section": "VI-A Geometric Interpretation", "weight": 1.0} -->

We now present three results connecting (SDP) to the lifted problems (P~ρ~). First, the optimal cost of (P~ρ~) is monotonically nonincreasing in $\rho$. Second, (SDP) lower-bounds the optimal cost of every (P~ρ~). Third, this lower bound is attained: from any minimizer of (SDP), we can construct a $\rho$ and a pair $(\Gamma,V)$ that minimizes (P~ρ~). Let $c_{\text{P}}^{*}$, $c_{\text{P}_{\rho}}^{*}$, and $c_{\text{SDP}}^{*}$ denote the optimal costs of (P), (P~ρ~), and (SDP). The SOS certificates $Q_{0},Q_{1}$ appear identically in all three programs, so we omit them from feasible points to keep notation light.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VI-B When is the Relaxation Tight?", "weight": 1.0} -->

We now present a necessary and sufficient condition for tightness, which follows immediately from the geometric interpretation: since (SDP) attains the minimum cost over the higher-dimensional problems (P~ρ~), $\rho\in\mathbb{N}$, it is tight exactly when this minimum equals the cost of (P).

<!-- chunk {"id": "body-0050", "role": "body", "section": "VI-C Recovering a Minimizer", "weight": 1.0} -->

Theorem 4 characterizes when the relaxation achieves the correct optimal cost, but does not say anything about the minimizer returned by the relaxation.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Empirical Analysis", "weight": 1.0} -->

Median speedup over baseline (ℝ3, ℝ5) Figure 4: Empirical comparison of the relaxation against SNOPT and IPOPT across random problem instances (see subsection VII-A). (a) Solve times (log scale); grey bars indicate all instances timed out. (b) Median speedup over each baseline, reported as (ℝ3, ℝ5). (c) Outcome breakdown against each baseline (left) and the distribution of the relaxation tightness (measured by ρ = rank (X − ΓTΓ), see section VI) (right). The relaxation is 1–2 orders of magnitude faster than the local solvers with 1–3 orders of magnitude smaller variance.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Empirical Analysis", "weight": 1.0} -->

We empirically evaluate the tightness and computational cost of the relaxation. We compare against multiple NLP baselines, e.g. direct transcriptions of the same nonconvex problem solved with local nonlinear solvers, and generally find that the relaxation is 1--2 orders of magnitude faster with 2--3 orders of magnitude lower variance in solve times. Further, when the strongest NLP baseline succeeds the relaxation is typically also tight, suggesting it captures primarily local information.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Empirical Analysis", "weight": 1.0} -->

We compare against SNOPT and IPOPT using two strategies for enforcing that each polynomial segment is collision-free. The discretization approach enforces eq. 6 at $20$ uniformly spaced values of $s\in$ per segment, yielding a nonconvex quadratic constraint at each sample. The exact approach uses the exact condition in eq. 11. ‣ IV-A Basis-Independent Derivation ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning"). For the latter approach we enforce $M\succeq 0$ through the factorization $M=LL^{T}$ for a lower triangular matrix $L$, as neither of the solvers support PSD constraints.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Empirical Analysis", "weight": 1.0} -->

We compare across the problem configurations in Table I, matching the classical setup of. We evaluate the methods on 100 randomly generated instances in $\mathbb{R}^{3}$ (15 obstacles) and $\mathbb{R}^{5}$ (30 obstacles), with obstacle radii in $[0.3,1.0]$ placed in the box $^{n}$. We apply the procedure in subsection V-C to similarly reduce the number of free variables for both the relaxation, SNOPT, and IPOPT. We initialize SNOPT and IPOPT with a straight-line initial guess, reduce their feasibility tolerance to $10^{-4}$, and enforce a timeout of $30$ seconds.

<!-- chunk {"id": "body-0055", "role": "body", "section": "VII-A Computational Cost", "weight": 1.0} -->

We now compare solve times between the methods. Against the discretization approach, the relaxation is 1--2 orders of magnitude faster across all polynomial degrees and both dimensions. Against the exact approach, the gap is even larger: for $d\geq 3$, SNOPT times out on nearly all instances, and IPOPT solves with median solve times that grow steeply with the degree (reaching tens of seconds), while the relaxation solves with medians of 17--33 ms in $\mathbb{R}^{3}$ and 24--63 ms in $\mathbb{R}^{5}$. The SDP relaxation also has a far smaller interquartile range: 1--4 ms in $\mathbb{R}^{3}$ and 1--12 ms in $\mathbb{R}^{5}$, 1--3 orders of magnitude smaller than the local solvers, whose interquartile ranges span 0.1--4.4 s for the discretization approach and 0.07--6.9 s for the exact approach (instances that reached the time limit excluded).

<!-- chunk {"id": "body-0056", "role": "body", "section": "VII-B Empirical Tightness", "weight": 1.0} -->

By Theorem 4, the relaxation is tight when extending the problem to higher dimensions does not reduce the cost, which empirically seems to approximately coincide with cases where local reasoning suffices to find the globally optimal path. Further, we empirically observe values of $\rho=\operatorname{rank}(X-\Gamma^{T}\Gamma)$ of only $0$ (tight) or $1$ (not tight) and never higher, suggesting that the original nonconvex problems in both $\mathbb{R}^{3}$ and $\mathbb{R}^{5}$ do not get any easier after extending them by one extra dimension (in the sense defined in section VI, e.g. (P~ρ=1~) might have lower cost than (P), but the problems (P~ρ≥1~) all have the same cost).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Kinodynamic Motion Planning", "weight": 1.0} -->

We illustrate how the relaxation can serve as a convex subroutine within a higher-level planner. Specifically, we use it as the local steering procedure in the Extend step of RRT, applied to minimum-snap quadrotor planning with degree 9, $C^{4}$-continuous trajectories.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Kinodynamic Motion Planning", "weight": 1.0} -->

We show that the semidefinite relaxation is well-suited as the steering function in an RRT. By default, RRT uses straight-line steering that ignores the smoothness and dynamic constraints that motion planning typically requires. A solution to this is to solve the two-point Boundary Value Problem (BVP) analytically, but this applies only to certain systems and costs, and ignores state and input constraints. Another approach plans collision-free waypoints and smooths them, or uses a local nonlinear solver as the steering function, but these inherit the brittleness of local solvers: reliance on an initial guess, high solve-time variance, and discretized collision avoidance. On the other hand, the relaxation finds a collision-free, cost-optimal trajectory in a single convex solve, enforces collision avoidance exactly along the entire trajectory, requires no initial guess, has fast and consistent solve times, and naturally handles state and input constraints such as velocity and acceleration limits.

<!-- chunk {"id": "body-0059", "role": "body", "section": "VIII-A RRT Implementation", "weight": 1.0} -->

We compare three methods, which we refer to as SDP-RRT, NLP-RRT, and Geometric RRT. SDP-RRT uses the relaxation as the steering function, enforcing collision avoidance exactly along the entire trajectory. NLP-RRT is an otherwise identical RRT that uses an optimized NLP trajectory optimizer as its steering function. We enforce collision avoidance with Drake's MinimumDistanceLowerBoundConstraint (a smoothed signed-distance formulation), and apply several optimizations: inflate the obstacles to reduce the number of collision samples, loosen the tolerances, and switch between SNOPT and IPOPT depending on problem size. Geometric RRT first uses straight-line geometric RRT to find collision-free waypoints, then smooths them with the same NLP trajectory optimizer. We sample only in the space of positions, and thus for SDP-RRT and NLP-RRT we implement a partial-state RRT that leaves the derivatives free.

<!-- chunk {"id": "body-0060", "role": "body", "section": "VIII-A RRT Implementation", "weight": 1.0} -->

These derivatives can grow rapidly as the tree deepens, and point-to-point steering functions cannot re-optimize across waypoints to control them, relying instead on heuristics such as terminal penalties. As a convex program, our SDP steering function instead optimizes directly over the free derivatives across multiple waypoints, removing the need for such heuristics. In practice we re-optimize only the last two segments on each extension, which we find produces near-identical trajectories to re-optimizing the entire path back to the root, at much lower cost. When connecting to the goal, the derivatives are fixed to enforce the boundary conditions.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VIII-B Trajectory Post-Processing", "weight": 1.0} -->

After the RRT planners find a path, we post-process it to reduce cost. For Geometric RRT and NLP-RRT, the path initializes a nonlinear program over the full trajectory. For SDP-RRT, we use a cutting-plane procedure motivated by the geometric interpretation of the relaxation: since the relaxation finds the cheapest trajectory across a family of higher-dimensional problems, we add linear cuts that force this trajectory into the original subspace. We sample points along the trajectory, add separating cuts between them and the obstacles, re-optimize, and repeat until the solution is collision-free, then resample to reduce cost further. Because dense cuts leave the LMI obstacle constraints rarely active, we drop them, reducing each iteration to a convex Quadratic Program (QP) that solves in a few milliseconds. This is a heuristic post-processing step, and the method recently proposed in provides a more principled approach to a similar idea.

<!-- chunk {"id": "body-0062", "role": "body", "section": "VIII-C Numerical Results", "weight": 1.0} -->

As shown in figure 6, with example trajectories in figure 5, SDP-RRT achieves the best performance across all metrics. NLP-RRT shares our ability to reason about additional trajectory constraints, but its nonconvex steering is slow and brittle: it is over an order of magnitude slower, less reliable, and often falls back to the unrefined RRT path, yielding far higher-cost trajectories. Geometric RRT, in contrast, is fast and reliable on this benchmark, which has no dynamic or input constraints, and SDP-RRT matches its solve time at a slightly higher success rate and comparable cost. Crucially however, Geometric RRT decouples geometric planning from trajectory optimization and cannot incorporate constraints such as dynamics or input limits, whereas our convex steering can enforce additional convex constraints during exploration.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion", "weight": 1.5} -->

While the relaxation is fast and reliable, our empirical analysis shows that it captures primarily local information and can be loose on instances where global reasoning is required. A potentially interesting direction of research is to develop higher-order relaxations from the moment-SOS hierarchy that can tighten the relaxation on such instances, and whether the symmetry reduction extends naturally to higher levels of the hierarchy. Relatedly, since we never observe $\rho>1$ in our experiments, an open question is to prove tighter bounds on $\rho$. Another direction is to extend the framework and analysis to richer obstacle and robot geometries described by polynomials. Further, since the relaxation is convex, it readily accommodates other convex constraints, extending the method to systems with linear dynamics and state or input constraints. Finally, another promising direction is to develop a custom solver that exploits the highly structured nature of our formulation, which could potentially speed up the relaxation further.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Connection To the Shor Relaxation", "weight": 1.0} -->

In this section, we show that our relaxation (SDP) is mathematically equivalent to the Shor relaxation, i.e. the first level of the moment hierarchy, of (P). The Shor relaxation lifts the full vector of decision variables $y\in\mathbb{R}^{n(d+1)}$ to a symmetric matrix $Y\in\mathbb{S}^{n(d+1)}$ that replaces the outer product $yy^{T}$, rendering each (potentially nonconvex) quadratic term linear, $y^{T}Hy=\left<H,Y\right>$, and relaxes the nonconvex lifting equality $Y=yy^{T}$ to the convex constraint $Y\succeq yy^{T}$. Our relaxation (SDP) follows the same recipe, but instead lifts to the smaller Gram matrix $X=\Gamma^{T}\Gamma\in\mathbb{S}^{d+1}$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Connection To the Shor Relaxation", "weight": 1.0} -->

Specifically, we show that (SDP) is a symmetry-reduced version of the Shor relaxation, where we exploit an $O(n)$ symmetry inherent to (P) to reformulate the problem over a PSD cone that is smaller by a factor of $n$, the ambient dimension. We derive the Shor relaxation in vectorized form to match the existing literature, but note that since (P) is a matrix problem, one could equivalently derive it directly in matrix form. All proofs are in subsection -C.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Connection To the Shor Relaxation", "weight": 1.0} -->

The first step to deriving the Shor relaxation of (P) is to rewrite (P) in a vectorized form. Define $y=\mathrm{vec}(\Gamma)=(\gamma_{0},\ldots,\gamma_{d})\in\mathbb{R}^{n(d+1)}$ as the vector of vertically stacked polynomial coefficients. Using the Kronecker product $\otimes$, we rewrite the linear constraints directly in terms of $y$. Applying the vectorization identity for Kronecker products, $\mathrm{vec}(LMN)=(N^{T}\otimes L)\mathrm{vec}(M)$, the boundary conditions $\Gamma A=B$ become $(A^{T}\otimes I_{n})y=\mathrm{vec}(B)$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Connection To the Shor Relaxation", "weight": 1.0} -->

Next, we rewrite the cost and the arguments to $\mathcal{L}$ in terms of $yy^{T}$ and $y$. Define the partial trace $\mathrm{tr}_{n}:\mathbb{S}^{n(d+1)}\rightarrow\mathbb{S}^{d+1}$ by $[\mathrm{tr}_{n}(M)]_{ij}=\mathrm{tr}(M_{ij})$, where $M_{ij}\in\mathbb{R}^{n\times n}$ is the $(i,j)$ block of $M$. The partial trace will let us translate between the outer products that arise from vectorization and the Gram matrices that appear in (P). Specifically, a direct computation shows that for any $M,N\in\mathbb{R}^{n\times(d+1)}$, Applying to the arguments of $\mathcal{L}$ in (P) gives all the substitutions we need to vectorize the problem.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Connection To the Shor Relaxation", "weight": 1.0} -->

The vectorized form of (P) is then with $y\in\mathbb{R}^{n(d+1)}$ and $Q_{0},Q_{1}$ unchanged from (P).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Connection To the Shor Relaxation", "weight": 1.0} -->

The Shor relaxation is then formed by introducing $Y\in\mathbb{S}^{n(d+1)}$ with the constraint $Y=yy^{T}$, and relaxing this nonconvex equality into $Y\succeq yy^{T}$. The resulting relaxation is: We have included the implied constraint $(A^{T}\otimes I_{n})Y=\mathrm{vec}(B)\,y^{T}$, which is redundant when $Y=yy^{T}$ but tightens the relaxation, analogously to $XA=\Gamma^{T}B$ in (SDP). The PSD variables of the two relaxations are related by $\mathrm{tr}_{n}(Y)=X$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Connection To the Shor Relaxation", "weight": 1.0} -->

We now show how (SDP) is a symmetry-reduced version of (Shor). To expose the symmetry, we decompose $Y=yy^{T}+S$, where $S\succeq 0$ is a positive semidefinite slack variable. Since $(A^{T}\otimes I_{n})y=\mathrm{vec}(B)$, the implied constraint reduces to $(A^{T}\otimes I_{n})S=0$. With this substitution, (Shor) becomes The key observation to see the symmetry in the problem is that both the cost and the linear map constraint depend on $S$ only through $\mathrm{tr}_{n}(S)\in\mathbb{S}^{d+1}$, a much smaller matrix than $S\in\mathbb{S}^{n(d+1)}$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Proofs for the Theoretical Results", "weight": 1.0} -->

In the proofs below, $Q_{0}$ and $Q_{1}$ are carried over unchanged between the programs, so we omit them from feasible points.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Bézier Curves and the Bernstein Basis", "weight": 1.0} -->

In our implementation, we use the standard Bernstein basis, which differs from the scaled Bernstein basis used in the main text by a binomial scaling. The $i$-th standard Bernstein basis polynomial of degree $d$ is defined as for $i=0,\ldots,d$ and $s\in$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "D1 Curve Costs for Bézier Curves", "weight": 1.0} -->

Derivatives of Bézier curves are Bézier curves of reduced degree: where $D_{d}^{(k)}:=D_{d}D_{d-1}\cdots D_{d-k+1}\in\mathbb{R}^{(d+1)\times(d-k+1)}$ and $D_{d}\in\mathbb{R}^{(d+1)\times d}$ is the forward difference matrix with $-1$ on the diagonal and $1$ on the subdiagonal. The Gram matrix $G_{d}$ from has entries which follows from the product rule and $\int_{0}^{1}B_{i}^{d}(s)\,ds=1/(d+1)$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "D2 Collision Avoidance for Bézier Curves", "weight": 1.0} -->

We now write the collision-avoidance condition from Lemma 3. ‣ IV-B Collision-Avoidance with Bézier Curves ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning") for Bézier curves, i.e., in the standard Bernstein basis. The derivation follows exactly as in the main body, with the standard Bernstein basis replacing the scaled one.
