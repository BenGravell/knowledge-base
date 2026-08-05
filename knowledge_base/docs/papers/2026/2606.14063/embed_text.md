<!-- arxiv-full-text:v1 {"arxiv_id": "2606.14063", "source": "arxiv-html"} -->

## Introduction

Figure 1: A collision-free, C4-continuous, minimum-snap quadrotor trajectory through a cluttered field of spherical obstacles, planned by an RRT that uses our semidefinite relaxation as a convex steering function. Our relaxation considers both obstacle-avoidance and other trajectory constraints, while being fast and reliable enough to make optimization a viable inner loop. The color coding of the trajectory indicates velocity (red is slow, green is fast).

Collision-free motion planning -- the problem of finding a smooth trajectory between two configurations that avoids a set of obstacles -- is a fundamental challenge in robotics and autonomous systems. Even in simple settings, the problem is computationally difficult due to the nonconvexity of the obstacle avoidance constraints. In the case of a point robot navigating among sphere obstacles in $\mathbb{R}^{2}$, the minimum length path can be computed in polynomial time, but the problem becomes NP-hard in $\mathbb{R}^{3}$ for polyhedral obstacles, and the complexity for disjoint unit sphere obstacles in $\mathbb{R}^{3}$ remains an open problem \[3, Section 31.5\]. In robotics, however, minimum path length is rarely the only consideration; motion planning typically involves costs such as time, energy, or snap, subject to constraints such as boundary conditions, derivative bounds, and continuity constraints. For this more general problem setting, no efficient algorithm is known.

Several approaches have been proposed to solve collision-free motion planning in practice. Optimization-based methods parametrize the trajectory as a piecewise polynomial and naturally handle different costs and constraints. A popular approach is to use trajectory optimization with Nonlinear Programming (NLP), but nonconvex optimization can be brittle and sensitive to the initial guess. Another approach sidesteps the nonconvexity of obstacle avoidance by precomputing a convex decomposition of the free-space, which can itself be a hard problem, and then plan through the decomposition with convex optimization. This has proven particularly effective for multiquery planning in a single environment. On the other hand, sampling-based planners are capable of global reasoning, but are unable to naturally reason about trajectory constraints. An alternative is to combine sampling-based planners with local trajectory optimization, either by post-processing a sampled geometric path, by precomputing motion primitives offline, or by embedding a local solver as a steering function within the sampler. Geometric sampling with post-processing does not reason about dynamic feasibility during exploration, often making the sampled path a poor initialization for optimization. Using optimization as the steering function addresses this, but jointly reasoning about obstacles and trajectory constraints is typically nonconvex, and the resulting NLP solves can be brittle with highly variable solve times, often making this impractical.

In recent years, semidefinite relaxations have emerged as a powerful tool for solving certain classes of nonconvex optimization problems. Through the Sum-of-Squares (SOS)/moment hierarchy, one can construct a sequence of increasingly strong relaxations, at the cost of growing computational complexity. These relaxations use convex optimization, and therefore do not suffer from being brittle or relying on an initial guess. The application of semidefinite relaxations has seen success in estimation and perception problems such as point cloud registration, pose-graph SLAM and range-aided SLAM, and has lately been applied to some motion planning problems, such as planning through contact. However, the behavior of semidefinite relaxations for collision-free motion planning is poorly understood, and to our knowledge no theoretical analysis of their properties in this setting has been given.

In this paper, we study semidefinite relaxations for collision-free motion planning. In particular, we focus on the problem of a point robot navigating from a start to a goal in a field of spherical obstacles in $\mathbb{R}^{n}$, minimizing a squared derivative cost (such as minimum energy or minimum snap) subject to path continuity constraints and boundary conditions. This setting is conceptually simple yet captures the hardness of motion planning. We formulate this problem for polynomial curves exactly as a nonconvex problem, and present a natural semidefinite relaxation of it. Our core contribution is a geometric interpretation of the relaxation: we show it is equivalent to solving, to global optimality, a related collision-free motion planning problem in a space of potentially higher dimension than the original ambient space $\mathbb{R}^{n}$. This yields necessary and sufficient conditions for when the relaxation is exact, and a clear intuition for when the relaxation is loose.

Beyond the theoretical analysis, we show that the relaxation provides a fast and reliable convex subroutine for motion planning. This is enabled by two properties of our formulation. First, we use a classical result from SOS to certify exactly when a polynomial curve avoids a spherical obstacle, without the need for discretization. The resulting Linear Matrix Inequality (LMI) condition takes a particularly nice form, with PSD constraints that scale linearly with the polynomial trajectory degree $d$ and are independent of the ambient dimension $n$. Second, the LMI condition is nonconvex in the trajectory coefficients, so we formulate a first-order semidefinite relaxation to obtain a convex program. A naive application of the well-known Shor relaxation yields a large program, but we exploit symmetry to reduce the size of the PSD cone by a factor of $n$. Together, these properties yield a relaxation that is 10 to 100 times faster than direct nonlinear programming transcriptions solved with SNOPT and IPOPT, exhibits significantly lower variance in solve times, and reliably finds a locally optimal path. We demonstrate the effectiveness of using our method as a convex and robust steering function in an RRT, planning $C^{4}$ continuous, minimum-snap collision-free trajectories through highly cluttered environments.

## Related Works

In this section, we review relevant works on semidefinite relaxations for motion planning and optimal control. As discussed in the introduction, there is also a substantial body of work on semidefinite relaxations for perception and estimation problems, which we do not review here.

Several works apply semidefinite relaxations to motion planning and control problems and empirically observe tight relaxations, though without analyzing when or why they are tight. Teng et al. formulate kinodynamic motion planning for rigid body systems as exact polynomial optimization problems, using a variational integrator to discretize the dynamics on Lie groups. They apply the moment hierarchy and empirically find that tight solutions are obtained at the second order of the hierarchy for most systems they consider. Similarly, Häring et al. study minimum-energy control of the unicycle model and empirically show that the second-order relaxation is tight. In, Vega et al. formulate spacecraft maneuver planning with a single spherical keep-out zone (analogous to considering a single spherical obstacle) as a Quadratically Constrained Quadratic Program (QCQP) with linearized dynamics, and apply the Shor relaxation to obtain empirically tight solutions. Recently, a setting similar to ours was considered by Mahajan et al., who apply the Shor relaxation to collision-free MPC with spherical obstacles and discretized collision-avoidance constraints, focusing on developing a custom cached Riccati-based ADMM solver that enables real-time rates on embedded hardware.

A related line of work applies semidefinite relaxations to time-scaled optimal control. Yang et al. develop a tailored semidefinite relaxation for linear and piecewise-affine systems and combine it with convex decompositions of the free-space and Graph of Convex Sets (GCS) to jointly optimize mode sequences and time-optimal collision-free trajectories. Dong et al. apply a similar relaxation to jointly optimize trajectories and time allocations for optimal control problems with spatio-temporal constraints, such as a quadrotor required to pass through a sequence of known waypoints within specified time windows, and exploit the banded sparsity of the multiple shooting formulation.

Semidefinite relaxations have also been applied to contact-rich planning. Graesdal et al. relax the contact dynamics of planar pushing with the first-order semidefinite relaxation, strengthen the formulation with implied constraints, and use GCS to plan optimal contact mode sequences. Kang et al. apply the moment hierarchy to a broader class of contact-rich planning problems, encoding the discrete mode sequence directly in the hierarchy rather than through GCS, and leverage problem-specific sparsity to obtain solutions at the second or third order of the hierarchy. Finally, Wei and Dümbgen take a different approach: they sample trajectory rollouts and use KernelSOS, a global optimization technique that builds a nonparametric surrogate of the cost landscape and minimizes it using semidefinite optimization, to find promising regions of the search space that are then refined with a sampling-based local optimizer.

In contrast to these works, which apply semidefinite relaxations to various planning problems and observe tightness empirically, our goal is to understand *when* the relaxation is tight. We therefore study a deliberately simplified setting, rich enough to capture the core difficulty of collision-free planning yet simple enough to admit a precise analysis. This setting also reveals a symmetry that reduces the SDP to a size independent of the ambient dimension, which can be combined with the correlative sparsity exploited in prior work.

## Motion Planning

In this section, we state the optimal collision-free motion planning problem exactly, as an optimization over curves where the entire curve must be collision-free. This problem is infinite-dimensional since the decision variable is a curve, and cannot be solved numerically as stated. To address this, we restrict the curves to polynomials and define the class of curve costs we consider. The result is a semi-infinite QCQP: the decision variables are finite-dimensional, but the obstacle-avoidance constraints must hold at every point along the curve. In the next section, we use SOS to reformulate the collision-avoidance constraint exactly as LMI conditions.

### III-A Problem Statement

We seek a collision-free path that minimizes the sum of the squared $\ell_{2}$-norm of its derivatives, such as velocity or snap, subject to boundary conditions and continuity constraints. Let the trajectory be represented as a curve $q:\rightarrow\mathbb{R}^{n}$. We require the trajectory $q$ to be $\eta$-times continuously differentiable, that is, $q\in\mathcal{C}^{\eta}$, and denote $q^{(i)}=(d^{i}/ds^{i})q$ as the $i$-th derivative. We consider $m$ spherical obstacles with centers $c_{j}\in\mathbb{R}^{n}$ and radii $r_{j}>0$, for $j=1,\ldots,m$. We formulate the motion planning problem as the following nonconvex optimization problem: where $k\in\mathbb{N}_{+}$ is the derivative order for the cost, and there are boundary conditions up to the $\ell$-th derivative on the curve. For motion planning, common choices for $k$ include $k=1$ (minimum energy), $k=2$ (minimum acceleration), and $k=4$ (minimum snap). The problem is nonconvex due to (1b). The problem is infinite-dimensional: the decision variable $q$ is a function in $C^{\eta}$, and for each obstacle $j$, the avoidance condition (1b) represents a continuum of nonconvex constraints indexed by $s\in$. As such, it is unclear how to solve problem numerically.

### III-B Polynomial Curves

We parametrize the curve as a piecewise polynomial, where each segment is a polynomial curve $\gamma:\rightarrow\mathbb{R}^{n}$ of degree $d$: where $b_{d}(s):\mathbb{R}\rightarrow\mathbb{R}^{d+1}$ is a basis of polynomials of degree less than or equal to $d$ in the variable $s$, and $\Gamma\in\mathbb{R}^{n\times(d+1)}$ is the corresponding coefficient matrix. With this parametrization, the decision variables for each segment reduce to the coefficient matrix $\Gamma$, and becomes an optimization problem with a finite number of variables, albeit still with an infinite number of constraints.

To keep the presentation clean, we develop all formulations for a single segment. This is not a restriction of the formulation, as the cost and collision-avoidance constraints in decompose across the polynomial segments, which are coupled only through linear continuity constraints, so the extension to multiple segments is straightforward. We likewise present these formulations in a basis-independent form, specializing to the Bernstein basis only for our numerical experiments and a few key results.

### III-C Curve Costs

For a polynomial curve $\gamma$ of degree $d$ as defined, the squared $\mathcal{L}_{2}$ norm of the $k$-th derivative can be expressed as is the $k$-th derivative Gram matrix of degree $d$, $D_{k}\in\mathbb{R}^{(d+1)\times(d+1-k)}$ is the differentiation matrix defined by $b^{(k)}_{d}(s)=D_{k}b_{d-k}(s)$, and is the basis-dependent Gram matrix of degree $d$. Both $G_{d}$ and $G^{(k)}_{d}$ can be computed analytically for any choice of basis. To keep notation light, we write $G$ and $G^{(k)}$ when the degree $d$ is clear from context. See subsection -D1 for explicit expressions for polynomials represented as Bézier curves, i.e. with the Bernstein basis.

The nullspace of $G^{(k)}_{d}$ characterizes the zero-cost directions of the polynomial trajectory, which we use in our theoretical analysis in Section VI. We present the following standard result on $G^{(k)}_{d}$ without proof:

### Lemma 1

$G^{(k)}_{d}$ has rank $d+1-k$, and its nullspace is the space of polynomials of degree at most $k-1$. That is, $G^{(k)}_{d}v=0$ if and only if $v^{T}b_{d}(s)$ is a polynomial of degree at most $k-1$.

### III-D Semi-Infinite QCQP Reformulation

We reformulate the motion planning problem in the polynomial coefficient matrix $\Gamma\in\mathbb{R}^{n\times(d+1)}$. The result is a semi-infinite QCQP, which has a finite number of decision variables, but obstacle avoidance must still hold point-wise for all $s\in$.

To keep notation light, we present the derivation for a single unit sphere centered at $c\in\mathbb{R}^{n}$. The condition that $\gamma$ avoids the sphere is equivalent to the polynomial nonnegativity condition: To write the nonnegativity condition in terms of the coefficient matrix $\Gamma$, we first express the shifted curve $\gamma(s)-c$ in the polynomial basis $b_{d}(s)$. We introduce a vector $u\in\mathbb{R}^{d+1}$ satisfying $u^{T}b_{d}(s)=1$, so that $\gamma(s)-c=\Gamma b_{d}(s)-c\cdot 1=(\Gamma-cu^{T})b_{d}(s)$. Using this, together with $1\cdot 1=b_{d}(s)^{T}uu^{T}b_{d}(s)$, can be rewritten as the quadratic form which is a univariate polynomial in $s$ of degree $2d$.

Combining the cost, the obstacle condition, and the boundary conditions, the polynomial motion planning problem is where $A$ and $B$ encode the boundary conditions (1d) and (1e) on the first $\ell$ derivatives: The problem is naturally written in matrix form. The cost and obstacle constraint are both quadratic in $\Gamma$, making the problem a semi-infinite QCQP.

## Certifying Collision-Avoidance

Condition is the nonnegativity of a univariate polynomial over an interval, which we know how to rewrite exactly using SOS. In this section, we show that the resulting conditions take a particularly nice form that is independent of the ambient dimension $n$ of the curve and scales linearly with the polynomial degree $d$. The conditions are quadratic in the polynomial coefficients $\Gamma$, so for a fixed trajectory, certifying collision-avoidance reduces to an SDP. When searching over trajectories, the conditions are nonconvex, which we address in the next section. We first derive the condition in a basis-free fashion, before presenting a concrete instance of it for the Bernstein basis.

### IV-A Basis-Independent Derivation

The key tool is the following classical result from real algebraic geometry:

### Theorem (Markov-Lukács \[39, §1.21\])

A univariate polynomial $p\in\mathbb{R}[s]$ of degree $2d$ is nonnegative over an interval $[a,b]$ if and only if where $\sigma_{0},\sigma_{1}$ are SOS with $\text{deg}(\sigma_{0})\leq 2d$ and $\text{deg}(\sigma_{1})\leq 2d-2$.

Applying this theorem to immediately gives:

### Lemma 2 (Collision avoidance for polynomial curves)

A polynomial curve $\gamma(s)=\Gamma b_{d}(s)$ of degree $d$ in $s$ lies entirely outside a unit sphere centered at $c$ if and only if there exist Gram matrices $Q_{0}\in\mathbb{S}^{d+1}_{+}$ and $Q_{1}\in\mathbb{S}^{d}_{+}$ such that where $\mathcal{L}$ is the linear map obtained by matching polynomial coefficients in the Markov-Lukács decomposition, and $u\in\mathbb{R}^{d+1}$ satisfies $u^{T}b_{d}(s)=1$.

### Proof

By the Markov-Lukács theorem, the nonnegativity condition is equivalent to where $\sigma_{0},\sigma_{1}$ are SOS polynomials of degree at most $2d$ and $2d-2$, respectively. Writing the SOS multipliers as quadratic forms $\sigma_{0}(s)=b_{d}(s)^{T}Q_{0}\,b_{d}(s)$ and $\sigma_{1}(s)=b_{d-1}(s)^{T}Q_{1}\,b_{d-1}(s)$ with $Q_{0}\succeq 0$ and $Q_{1}\succeq 0$, and matching polynomial coefficients defines the linear map $\mathcal{L}$. ∎ The condition is linear in $(\Gamma-cu^{T})^{T}(\Gamma-cu^{T})\in\mathbb{S}^{d+1}_{+}$ and therefore quadratic in $\Gamma$ itself. The extension to ellipsoidal obstacles is straightforward:

### Corollary 1 (Extension to ellipsoidal obstacles)

For a general ellipsoidal obstacle $\left\{x\in\mathbb{R}^{n}\mid(x-c)^{T}E(x-c)\leq 1\right\}$ where $E$ is a positive semidefinite matrix, Lemma 2. ‣ IV-A Basis-Independent Derivation ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning") extends to where $\mathcal{L}$, $Q_{0}$, and $Q_{1}$ are as in Lemma 2. ‣ IV-A Basis-Independent Derivation ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning").

### IV-B Collision-Avoidance with Bézier Curves

Bézier curves, which are polynomial curves expressed in the Bernstein basis, are a common choice in motion planning. We instantiate the collision-avoidance conditions of Lemma 2. ‣ IV-A Basis-Independent Derivation ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning") in the closely related scaled Bernstein basis, which drops the binomial coefficients and yields simpler expressions. Our implementation uses the standard Bernstein basis for its better numerical conditioning, with the corresponding expressions given in Subsection -D2.

The $i$-th scaled Bernstein basis polynomial of degree $d$ is defined as for $s\in$. Recall from Lemma 2. ‣ IV-A Basis-Independent Derivation ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning") that we require a vector $u$ satisfying $u^{T}b_{d}(s)=1$. By the binomial theorem, so we take $u_{i}=\binom{d}{i}$ for $i=0,\ldots,d$.

We now make the collision-avoidance condition from Lemma 2. ‣ IV-A Basis-Independent Derivation ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning") explicit for the scaled Bernstein basis. The derivation follows standard SOS coefficient matching, which takes a particularly simple form in this basis due to the key identity which follows immediately from the definition of the scaled Bernstein basis polynomials. From this, a quadratic form in $b_{d}(s)$ (like the one in) can be expressed in the basis $b_{2d}(s)$ as where $\mathcal{S}_{d}:\mathbb{S}^{d+1}\rightarrow\mathbb{R}^{2d+1}$ sums along the anti-diagonals of $M$: the product $s(1-s)\cdot b_{d-1}(s)^{T}Mb_{d-1}(s)$ can be expressed in the basis $b_{2d}(s)$ as where $\mathcal{T}_{d}:\mathbb{S}^{d}\rightarrow\mathbb{R}^{2d+1}$ is a shifted version of $\mathcal{S}_{d-1}$: Using these maps, we can write the collision-avoidance condition from Lemma 2. ‣ IV-A Basis-Independent Derivation ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning") explicitly:

### Lemma 3 (Collision avoidance in the scaled Bernstein basis)

A polynomial curve $\gamma(s)=\Gamma b_{d}(s)$ of degree $d$ in the scaled Bernstein basis lies entirely outside a unit sphere centered at $c$ if and only if there exist $Q_{0}\in\mathbb{S}^{d+1}_{+}$ and $Q_{1}\in\mathbb{S}^{d}_{+}$ such that where $\mathcal{S}_{d}$ and $\mathcal{T}_{d}$ are the linear maps defined in and.

### Proof

Apply $\mathcal{S}_{d}$ and $\mathcal{T}_{d}$ to match coefficients in the basis $b_{2d}(s)$ in the proof of Lemma 2. ‣ IV-A Basis-Independent Derivation ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning"). ∎ For Bézier curves (i.e., the standard Bernstein basis), the same condition holds with $u=e$, the vector of ones, and the corresponding maps $\mathcal{S}_{d}$, $\mathcal{T}_{d}$ given in Subsection -D2.

### IV-C The Special Case of Line Segments

For line segments, the LMI condition reduces to a Rotated Second-Order Cone (RSOC) constraint, which is computationally much cheaper. The natural parameterization of a line segment from $\gamma_{0}$ to $\gamma_{1}$, is a Bézier curve of degree $d=1$, for which the scaled and standard Bernstein bases coincide with $b_{1}(s)=(1-s,s)$ and $\Gamma=\begin{bmatrix}\gamma_{0}&\gamma_{1}\end{bmatrix}$. Applying Lemma 3. ‣ IV-B Collision-Avoidance with Bézier Curves ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning") with $d=1$ gives:

### Corollary 2 (Collision avoidance for line segments)

A line segment from $\gamma_{0}$ to $\gamma_{1}$ lies entirely outside an ellipsoidal obstacle $\left\{x\in\mathbb{R}^{n}\mid(x-c)^{T}E(x-c)\leq 1\right\}$ if and only if there exists a scalar $\alpha\geq 0$ such that which is a $2\times 2$ PSD constraint that can be encoded as a RSOC constraint.

### Proof

Direct computation from Lemma 3. ‣ IV-B Collision-Avoidance with Bézier Curves ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning") with $d=1$, eliminating $Q_{0}$ and letting $\alpha=Q_{1}$. ∎

## Semidefinite Relaxation

Using the results of the previous section, we now rewrite the semi-infinite QCQP as a finite-dimensional nonconvex problem, before deriving a semidefinite relaxation of it.

### V-A Nonconvex Problem

Substituting the LMI condition of Lemma 2. ‣ IV-A Basis-Independent Derivation ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning") for the continuum constraint in the semi-infinite QCQP gives a finite-dimensional nonconvex problem: where the decision variables are $\Gamma\in\mathbb{R}^{n\times(d+1)}$, $Q_{0}\in\mathbb{S}^{d+1}$ and $Q_{1}\in\mathbb{S}^{d}$ (the SOS Gram matrices from (11. ‣ IV-A Basis-Independent Derivation ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning"))). The first constraint in (P) is a quadratic equality constraint in the polynomial coefficients, and is therefore nonconvex.

### V-B Forming the Relaxation

The nonconvexity in (P) comes from the first argument to $\mathcal{L}$, which expands as We define the Gram matrix of the polynomial coefficients as $X:=\Gamma^{T}\Gamma\in\mathbb{S}^{d+1}$. Substituting into, the right-hand side becomes affine in $X$ and $\Gamma$. Since $\mathcal{L}$ is a linear map, the constraint remains affine in the decision variables $X$, $\Gamma$, $Q_{0}$, and $Q_{1}$. The same substitution makes the cost linear in $X$: $\mathrm{tr}(G^{(k)}\Gamma^{T}\Gamma)=\mathrm{tr}(G^{(k)}X)$.

The only remaining nonconvexity is the constraint $X=\Gamma^{T}\Gamma$, which we relax into the convex constraint $X\succeq\Gamma^{T}\Gamma$. Using the Schur complement, we can rewrite the condition as an LMI: where $I_{n}$ is the $n$-dimensional identity matrix.

With this, the convex relaxation of (P) is: This is an SDP in the decision variables $\Gamma$, $X$, $Q_{0}$, and $Q_{1}$. The constraints $XA=\Gamma^{T}B$ are implied by $\Gamma A=B$ when $X=\Gamma^{T}\Gamma$ holds (left-multiply by $\Gamma^{T}$), so they are redundant for (P) but tighten the relaxation.

### V-C Strict Feasibility and Facial Reduction

Every feasible point of the SDP satisfies so the feasible set lies in a proper face of the PSD cone. As a result, the SDP is never strictly feasible, and solving it directly leads to numerical difficulties. In practice, we address this by eliminating the equality constraints before solving, which restricts the LMI to this face. This is a facial reduction where the reducing certificate is available in closed form. Eliminating the equality constraints amounts to parameterizing the affine subspace defined by $\Gamma A=B$ \[42, Section 10.1.2\], and for Bézier curves in the Bernstein basis, the boundary conditions admit a particularly simple parametrization. The derivatives at each endpoint depend in a triangular manner on the adjacent control points $\gamma=\gamma_{0}$, $\gamma^{\prime}$ depends on $\gamma_{0}$ and $\gamma_{1}$, $\gamma^{\prime\prime}$ on $\gamma_{0},\gamma_{1},\gamma_{2}$, and so on (and similarly at $s=1$, reading from the end). Prescribing derivatives up to $\ell$ at each endpoint therefore fixes the $\ell{+}1$ adjacent control points as known constants, leaving the remaining $d+1-2(\ell{+}1)$ control points free. We can therefore write $\Gamma=BD_{\text{fixed}}+\Gamma_{\text{free}}D_{\text{free}}$, where $\Gamma_{\text{free}}$ collects the free control points and $D_{\text{fixed}},D_{\text{free}}$ are constant matrices that place the boundary data and the free columns into the corresponding columns of $\Gamma$. Defining the smaller Gram matrix $X_{\text{free}}:=\Gamma_{\text{free}}^{T}\Gamma_{\text{free}}$ and relaxing it into $X_{\text{free}}\succeq\Gamma_{\text{free}}^{T}\Gamma_{\text{free}}$, the LMI reduces in size from $n+d+1$ to $n+d+1-2(\ell{+}1)$. The boundary and tightening constraints are then satisfied by construction, while the cost and collision-avoidance constraints remain linear in $(\Gamma_{\text{free}},X_{\text{free}})$.

### V-D Extension to Multiple Segments

For $N$ segments with polynomial coefficient matrices $\Gamma_{1},\ldots,\Gamma_{N}$ and $\mathcal{C}^{\eta}$ continuity, the relaxation is derived analogously. Specifically, it introduces per-segment Gram matrices $X_{i}$ and cross-Gram matrices $X_{i,i+1}$ between consecutive segments, relaxing the nonconvex constraint via an LMI analogous to: Boundary conditions remain unchanged, and $\mathcal{C}^{\eta}$ continuity between adjacent segments introduces additional linear constraints on $\Gamma_{i}$ of the form $\Gamma_{i}A_{1}=\Gamma_{i+1}A_{0}$, where $A_{1},A_{0}\in\mathbb{R}^{(d+1)\times(\eta+1)}$ collect the endpoint values of the Bernstein basis derivatives at $s=1$ and $s=0$ respectively. Every such linear constraint implies additional tightening constraints on $X_{i}$ and $X_{i,i+1}$, obtained by left-multiplying by $\Gamma_{i}^{T}$ or $\Gamma_{i+1}^{T}$. The facial reduction from the previous subsection extends directly to this setting: continuity contributes $\eta{+}1$ additional dependent columns to each pairwise LMI, reducing its size from $n+2(d{+}1)$ to $n+2(d{+}1)-(\eta{+}1)$ at interior junctions, with a further $\ell{+}1$ removed at pairs containing a global endpoint.

## Theoretical Results

We now present our main theoretical results. We first give a geometric interpretation of the relaxation: solving (SDP) is equivalent to solving, to global optimality, a planning problem in a higher-dimensional space. We then use this interpretation to characterize exactly when the relaxation is tight, and give geometric conditions under which the minimizer of the original nonconvex problem is recovered. Finally, we show that our relaxation is a symmetry-reduced version of the Shor relaxation of (P) under an $O(n)$ symmetry. As the rest of the paper can be understood without this last result, we defer it to Subsection -A.

### VI-A Geometric Interpretation

Recall that (SDP) is obtained by an algebraic lift, replacing the nonconvex term $\Gamma^{T}\Gamma$ in (P) with the matrix variable $X\succeq\Gamma^{T}\Gamma$. We now give this lift a geometric interpretation. We introduce a family of higher-dimensional, nonconvex problems (P~ρ~), $\rho\in\mathbb{N}$, that allow the path $\rho$ extra spatial dimensions beyond the original $n$ ambient dimensions, while the obstacles and boundary conditions remain in $\mathbb{R}^{n}$. We then show that (SDP) attains the optimal cost over this family, and that an optimal $(n+\rho)$-dimensional path can be recovered from any minimizer.

Consider extending the problem (P) from $\mathbb{R}^{n}$ to $\mathbb{R}^{n+\rho}$, for some $\rho\in\mathbb{N}$, in the following sense: Let $v(s)=Vb_{d}(s)\in\mathbb{R}^{\rho}$ be a polynomial curve in the extra $\rho$ dimensions, with coefficient matrix $V\in\mathbb{R}^{\rho\times(d+1)}$ so the full curve is $(\gamma(s),v(s))\in\mathbb{R}^{n+\rho}$. Let the obstacle be a sphere in $\mathbb{R}^{n+\rho}$ centered at $(c,0)$. The squared distance to the obstacle center then splits as $\|\gamma(s)-c\|^{2}+\|v(s)\|^{2}$, so the quadratic form extends with an additional $V^{T}V$ term. We require $v$ and its first $\ell$ derivatives to vanish at the boundary: $v^{(i)}=v^{(i)}=0$ for $i=0,\ldots,\ell$, or equivalently $VA=0$. The resulting problem, with $\Gamma$ as in (P), is: This is still a nonconvex problem, and (P~ρ~) reduces to (P) for $\rho=0$. Figure 2 (a) and figure 2 (b) show two different examples with (P) (left) and (P~ρ=1~) (right).

We now present three results connecting (SDP) to the lifted problems (P~ρ~). First, the optimal cost of (P~ρ~) is monotonically nonincreasing in $\rho$. Second, (SDP) lower-bounds the optimal cost of every (P~ρ~). Third, this lower bound is attained: from any minimizer of (SDP), we can construct a $\rho$ and a pair $(\Gamma,V)$ that minimizes (P~ρ~). Let $c_{\text{P}}^{*}$, $c_{\text{P}_{\rho}}^{*}$, and $c_{\text{SDP}}^{*}$ denote the optimal costs of (P), (P~ρ~), and (SDP). The SOS certificates $Q_{0},Q_{1}$ appear identically in all three programs, so we omit them from feasible points to keep notation light.

Our first result formalizes the intuition that (P~ρ~) gets easier as $\rho$ increases, since every path feasible for (P~ρ~) remains feasible for (P~ρ+1~):

### Theorem 1

The optimal costs of (P~ρ~) are monotonically nonincreasing: $c_{\text{P}_{\rho}}^{*}\geq c_{\text{P}_{\rho+1}}^{*}$ for all $\rho\in\mathbb{N}$.

However, these costs cannot decrease indefinitely, as (SDP) lower-bounds the entire family:

### Theorem 2

For all $\rho\in\mathbb{N}$, $c_{\text{P}_{\rho}}^{*}\geq c_{\text{SDP}}^{*}$.

Our third result shows that this lower bound is attained at a finite $\rho$, constructed from any minimizer of (SDP):

### Theorem 3

Let $(\Gamma^{*},X^{*})$ be optimal for (SDP) and let $\rho=\operatorname{rank}(X^{*}-(\Gamma^{*})^{T}\Gamma^{*})$. Then for any $V^{*}$ satisfying $(V^{*})^{T}V^{*}=X^{*}-(\Gamma^{*})^{T}\Gamma^{*}$, the pair $(\Gamma^{*},V^{*})$ is optimal for (P~ρ~), and $c_{\textnormal{P}_{\rho}}^{*}=c_{\textnormal{SDP}}^{*}$.

Together, Theorems 1, 2 and 3 give a clean geometric interpretation of the relaxation: (SDP) solves the easiest problem in the family of higher-dimensional problems, in the sense that it attains the lowest optimal cost, $c_{\text{SDP}}^{*}=\min_{\rho\in\mathbb{N}}c_{\text{P}_{\rho}}^{*}$. A numerical example for $\mathbb{R}^{2}$ is shown in Figure 2.

While the number of extra dimensions used by the lifted problem, $\rho=\operatorname{rank}(X-\Gamma^{T}\Gamma)$, is already bounded by $d+1$ since $X-\Gamma^{T}\Gamma\in\mathbb{S}^{d+1}$, the boundary conditions give a tighter bound:

### Lemma 4

The dimension $\rho$ in Theorem 3 satisfies $\rho\leq(d+1)-2(\ell+1)$, the number of free control points.

In practice, we find $\rho$ to be smaller. In section VII, we show that across experiments in $\mathbb{R}^{2}$, $\mathbb{R}^{3}$, and $\mathbb{R}^{5}$, we never observe $\rho>1$, suggesting that, for the random instances we solve, a single extra dimension already attains the lowest cost in the family.

(b) Not tight example.

Figure 2: Geometric interpretation of the relaxation for two examples in ℝ2. Each example shows the trajectory defined by the polynomial coefficients Γ from the solution to the relaxation in the original ambient space ℝ2 (left), and the lifted trajectory defined by (Γ, V) recovered from any factorization VTV = X − ΓTΓ, following Theorem 3 (right). (a) Tight: X = ΓTΓ, so V = 0 and the lifted trajectory coincides with the optimal ℝ2 trajectory. (b) Not tight: ρ = rank (X − ΓTΓ) = 1, so V ∈ ℝ1 × (d + 1) is nonzero and the lifted trajectory uses the extra dimension to find a lower-cost trajectory that, when projected back to ℝ2, passes through the obstacles. The two trajectories shown are the two factorizations ±V of X − ΓTΓ.

### VI-B When is the Relaxation Tight?

We now present a necessary and sufficient condition for tightness, which follows immediately from the geometric interpretation: since (SDP) attains the minimum cost over the higher-dimensional problems (P~ρ~), $\rho\in\mathbb{N}$, it is tight exactly when this minimum equals the cost of (P).

### Theorem 4

The optimal cost of the relaxation equals the true optimal cost, $c_{\text{SDP}}^{*}=c_{\text{P}}^{*}$, if and only if $c_{\text{P}}^{*}=c_{\text{P}_{\rho}}^{*}$ for all $\rho\in\mathbb{N}$.

In other words, the relaxation is tight exactly when extending the original problem (P) to a higher dimension cannot produce a cheaper collision-free path.

### VI-C Recovering a Minimizer

Theorem 4 characterizes when the relaxation achieves the correct optimal cost, but does not say anything about the minimizer returned by the relaxation. The next result says that when a unique trajectory is optimal for all the higher-dimensional problems (P~ρ~), the relaxation recovers it exactly:

### Theorem 5

If for all $\rho\in\mathbb{N}$, every minimizer of (P~ρ~) has $\Gamma=\Gamma^{*}$ and $V=0$, then every minimizer of (SDP) has $\Gamma=\Gamma^{*}$ and $X=(\Gamma^{*})^{T}\Gamma^{*}$.

The hypothesis implies $c_{\text{P}_{\rho}}^{*}=c_{\text{P}}^{*}$ for all $\rho$, i.e., the relaxation is tight by Theorem 4. The uniqueness assumption is stronger but additionally guarantees recovery of the correct minimizer. It requires uniqueness only in $\Gamma$ and $V$, and $Q_{0}$ and $Q_{1}$ need not be unique.

The hypothesis of Theorem 5 can fail even when the relaxation is tight. We identify two sufficient conditions for non-uniqueness of (P~ρ~). The first is that the obstacle-free problem has multiple minimizers. Without obstacle constraints, (P~ρ~) reduces to a convex QP over $\Gamma$ (since $V=0$ is then optimal), whose cost has zero-cost directions, which by Lemma 1 are the polynomials of degree below $k$. The QP has a unique minimizer when the boundary conditions eliminate these directions, which holds when $k\leq 2(\ell+1)$. This is a standard result in polynomial trajectory optimization, and follows from the uniqueness condition for convex QPs \[42, Section 10.1.1\] and the Hermite interpolation theorem \[43, Section 2.1.5\]. The second is the obstacle geometry: even when the obstacle-free problem has a unique minimizer, the nonconvex collision-avoidance constraints can create multiple isolated optima, such as symmetric paths around an obstacle. In practice, a small random perturbation to the problem geometry typically breaks this symmetry.

## Empirical Analysis

Figure 3: Numerical evaluation of where the relaxation is tight and where it is loose for some representative obstacle configurations. The green region shows the set of reachable positions from the dark dot for which the relaxation is tight, and the red region shows where it is loose. The green lines show the trajectories obtained from solving the relaxation. Results are shown for minimum-energy cost with degree 3 polynomial trajectories.

Median speedup over baseline (ℝ3, ℝ5) Figure 4: Empirical comparison of the relaxation against SNOPT and IPOPT across random problem instances (see subsection VII-A). (a) Solve times (log scale); grey bars indicate all instances timed out. (b) Median speedup over each baseline, reported as (ℝ3, ℝ5). (c) Outcome breakdown against each baseline (left) and the distribution of the relaxation tightness (measured by ρ = rank (X − ΓTΓ), see section VI) (right). The relaxation is 1–2 orders of magnitude faster than the local solvers with 1–3 orders of magnitude smaller variance.

We empirically evaluate the tightness and computational cost of the relaxation. We compare against multiple NLP baselines, e.g. direct transcriptions of the same nonconvex problem solved with local nonlinear solvers, and generally find that the relaxation is 1--2 orders of magnitude faster with 2--3 orders of magnitude lower variance in solve times. Further, when the strongest NLP baseline succeeds the relaxation is typically also tight, suggesting it captures primarily local information.

We compare against SNOPT and IPOPT using two strategies for enforcing that each polynomial segment is collision-free. The discretization approach enforces eq. 6 at $20$ uniformly spaced values of $s\in$ per segment, yielding a nonconvex quadratic constraint at each sample. The exact approach uses the exact condition in eq. 11. ‣ IV-A Basis-Independent Derivation ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning"). For the latter approach we enforce $M\succeq 0$ through the factorization $M=LL^{T}$ for a lower triangular matrix $L$, as neither of the solvers support PSD constraints.

We compare across the problem configurations in Table I, matching the classical setup of. We evaluate the methods on 100 randomly generated instances in $\mathbb{R}^{3}$ (15 obstacles) and $\mathbb{R}^{5}$ (30 obstacles), with obstacle radii in $[0.3,1.0]$ placed in the box $^{n}$. We apply the procedure in subsection V-C to similarly reduce the number of free variables for both the relaxation, SNOPT, and IPOPT. We initialize SNOPT and IPOPT with a straight-line initial guess, reduce their feasibility tolerance to $10^{-4}$, and enforce a timeout of $30$ seconds.

TABLE I: Bézier curve configurations. Cost minimizes ∫∥γ(k)(t)∥2 dt, polynomial degree is 2k − 1, continuity is Ck (C0 for k = 1 to avoid overconstraining the problem), and BC order is the highest derivative fixed to zero at the endpoints.

### VII-A Computational Cost

We now compare solve times between the methods. Against the discretization approach, the relaxation is 1--2 orders of magnitude faster across all polynomial degrees and both dimensions. Against the exact approach, the gap is even larger: for $d\geq 3$, SNOPT times out on nearly all instances, and IPOPT solves with median solve times that grow steeply with the degree (reaching tens of seconds), while the relaxation solves with medians of 17--33 ms in $\mathbb{R}^{3}$ and 24--63 ms in $\mathbb{R}^{5}$. The SDP relaxation also has a far smaller interquartile range: 1--4 ms in $\mathbb{R}^{3}$ and 1--12 ms in $\mathbb{R}^{5}$, 1--3 orders of magnitude smaller than the local solvers, whose interquartile ranges span 0.1--4.4 s for the discretization approach and 0.07--6.9 s for the exact approach (instances that reached the time limit excluded).

### VII-B Empirical Tightness

Figure 3 gives geometric intuition for when the relaxation is tight, showing the regions of tightness and looseness for a single start position across the workspace under different obstacle configurations. Further, there is a strong correlation between when the relaxation is tight and when the strongest NLP baseline succeeds. In figure 4 (c), we show an outcome breakdown comparing the relaxation with each baseline, considering only instances where the relaxation is tight or the baseline succeeds. Against the strongest baseline, both methods succeed with matching costs on 91% of instances. On the remaining instances, either only one of the two methods succeeds, or both succeed but the relaxation reaches the global optimum while the baseline finds a suboptimal local solution. Against the other baselines, this gap widens. On a growing fraction of instances the relaxation finds the global optimum where the baseline returns only a local one, or succeeds where the baseline fails or times out.

By Theorem 4, the relaxation is tight when extending the problem to higher dimensions does not reduce the cost, which empirically seems to approximately coincide with cases where local reasoning suffices to find the globally optimal path. Further, we empirically observe values of $\rho=\operatorname{rank}(X-\Gamma^{T}\Gamma)$ of only $0$ (tight) or $1$ (not tight) and never higher, suggesting that the original nonconvex problems in both $\mathbb{R}^{3}$ and $\mathbb{R}^{5}$ do not get any easier after extending them by one extra dimension (in the sense defined in section VI, e.g. (P~ρ=1~) might have lower cost than (P), but the problems (P~ρ≥1~) all have the same cost).

## Kinodynamic Motion Planning

Figure 5: Minimum-snap trajectories (C4 continuous, degree 9 polynomials) found on 10 randomly generated ℝ2 environments with 40 obstacles, by our RRT implementation that uses the SDP relaxation as the steering procedure in the Extend step and post-processes with a small convex program. Each subplot title reports the total planning time. Trajectories are colored by speed, from green (fast) to red (slow).

We illustrate how the relaxation can serve as a convex subroutine within a higher-level planner. Specifically, we use it as the local steering procedure in the Extend step of RRT, applied to minimum-snap quadrotor planning with degree 9, $C^{4}$-continuous trajectories.

We show that the semidefinite relaxation is well-suited as the steering function in an RRT. By default, RRT uses straight-line steering that ignores the smoothness and dynamic constraints that motion planning typically requires. A solution to this is to solve the two-point Boundary Value Problem (BVP) analytically, but this applies only to certain systems and costs, and ignores state and input constraints. Another approach plans collision-free waypoints and smooths them, or uses a local nonlinear solver as the steering function, but these inherit the brittleness of local solvers: reliance on an initial guess, high solve-time variance, and discretized collision avoidance. On the other hand, the relaxation finds a collision-free, cost-optimal trajectory in a single convex solve, enforces collision avoidance exactly along the entire trajectory, requires no initial guess, has fast and consistent solve times, and naturally handles state and input constraints such as velocity and acceleration limits.

### VIII-A RRT Implementation

We compare three methods, which we refer to as SDP-RRT, NLP-RRT, and Geometric RRT. SDP-RRT uses the relaxation as the steering function, enforcing collision avoidance exactly along the entire trajectory. NLP-RRT is an otherwise identical RRT that uses an optimized NLP trajectory optimizer as its steering function. We enforce collision avoidance with Drake's MinimumDistanceLowerBoundConstraint (a smoothed signed-distance formulation), and apply several optimizations: inflate the obstacles to reduce the number of collision samples, loosen the tolerances, and switch between SNOPT and IPOPT depending on problem size. Geometric RRT first uses straight-line geometric RRT to find collision-free waypoints, then smooths them with the same NLP trajectory optimizer. We sample only in the space of positions, and thus for SDP-RRT and NLP-RRT we implement a partial-state RRT that leaves the derivatives free. These derivatives can grow rapidly as the tree deepens, and point-to-point steering functions cannot re-optimize across waypoints to control them, relying instead on heuristics such as terminal penalties. As a convex program, our SDP steering function instead optimizes directly over the free derivatives across multiple waypoints, removing the need for such heuristics. In practice we re-optimize only the last two segments on each extension, which we find produces near-identical trajectories to re-optimizing the entire path back to the root, at much lower cost. When connecting to the goal, the derivatives are fixed to enforce the boundary conditions.

### VIII-B Trajectory Post-Processing

After the RRT planners find a path, we post-process it to reduce cost. For Geometric RRT and NLP-RRT, the path initializes a nonlinear program over the full trajectory. For SDP-RRT, we use a cutting-plane procedure motivated by the geometric interpretation of the relaxation: since the relaxation finds the cheapest trajectory across a family of higher-dimensional problems, we add linear cuts that force this trajectory into the original subspace. We sample points along the trajectory, add separating cuts between them and the obstacles, re-optimize, and repeat until the solution is collision-free, then resample to reduce cost further. Because dense cuts leave the LMI obstacle constraints rarely active, we drop them, reducing each iteration to a convex Quadratic Program (QP) that solves in a few milliseconds. This is a heuristic post-processing step, and the method recently proposed in provides a more principled approach to a similar idea.

### VIII-C Numerical Results

Figure 1 shows a collision-free quadrotor trajectory in $\mathbb{R}^{3}$. We evaluate the full pipeline on 100 randomly generated $\mathbb{R}^{2}$ environments, each with 40 spherical obstacles of radius $1\,\text{m}$ in a $15\times 15\,\text{m}$ square, comparing all three methods on pipeline success rate, total solve time (including refinement), steer time, and trajectory cost. A run is successful if it produces a feasible, collision-free trajectory. For Geometric RRT this requires the NLP refinement to succeed, while NLP-RRT and SDP-RRT have a feasible trajectory once the RRT finds a path. Steer time is the cumulative optimization time, excluding program construction overhead, which can be eliminated by pre-compiling the convex optimization programs with a tool such as CVXGEN.

As shown in figure 6, with example trajectories in figure 5, SDP-RRT achieves the best performance across all metrics. NLP-RRT shares our ability to reason about additional trajectory constraints, but its nonconvex steering is slow and brittle: it is over an order of magnitude slower, less reliable, and often falls back to the unrefined RRT path, yielding far higher-cost trajectories. Geometric RRT, in contrast, is fast and reliable on this benchmark, which has no dynamic or input constraints, and SDP-RRT matches its solve time at a slightly higher success rate and comparable cost. Crucially however, Geometric RRT decouples geometric planning from trajectory optimization and cannot incorporate constraints such as dynamics or input limits, whereas our convex steering can enforce additional convex constraints during exploration.

Figure 6: Aggregate statistics showing median and interquartile ranges over 100 random environments for Geometric RRT, NLP-RRT, and SDP-RRT (ours), with costs and solve times reported over successful runs (n per bar). SDP-RRT substantially outperforms NLP-RRT, and performs similar to Geometric RRT (with slightly higher success rate), which importantly, unlike our method, cannot incorporate additional constraints such as dynamics or input limits.

## Conclusion

While the relaxation is fast and reliable, our empirical analysis shows that it captures primarily local information and can be loose on instances where global reasoning is required. A potentially interesting direction of research is to develop higher-order relaxations from the moment-SOS hierarchy that can tighten the relaxation on such instances, and whether the symmetry reduction extends naturally to higher levels of the hierarchy. Relatedly, since we never observe $\rho>1$ in our experiments, an open question is to prove tighter bounds on $\rho$. Another direction is to extend the framework and analysis to richer obstacle and robot geometries described by polynomials. Further, since the relaxation is convex, it readily accommodates other convex constraints, extending the method to systems with linear dynamics and state or input constraints. Finally, another promising direction is to develop a custom solver that exploits the highly structured nature of our formulation, which could potentially speed up the relaxation further.

### A Connection To the Shor Relaxation

In this section, we show that our relaxation (SDP) is mathematically equivalent to the Shor relaxation, i.e. the first level of the moment hierarchy, of (P). The Shor relaxation lifts the full vector of decision variables $y\in\mathbb{R}^{n(d+1)}$ to a symmetric matrix $Y\in\mathbb{S}^{n(d+1)}$ that replaces the outer product $yy^{T}$, rendering each (potentially nonconvex) quadratic term linear, $y^{T}Hy=\left<H,Y\right>$, and relaxes the nonconvex lifting equality $Y=yy^{T}$ to the convex constraint $Y\succeq yy^{T}$. Our relaxation (SDP) follows the same recipe, but instead lifts to the smaller Gram matrix $X=\Gamma^{T}\Gamma\in\mathbb{S}^{d+1}$. Specifically, we show that (SDP) is a symmetry-reduced version of the Shor relaxation, where we exploit an $O(n)$ symmetry inherent to (P) to reformulate the problem over a PSD cone that is smaller by a factor of $n$, the ambient dimension. We derive the Shor relaxation in vectorized form to match the existing literature, but note that since (P) is a matrix problem, one could equivalently derive it directly in matrix form. All proofs are in subsection -C.

The first step to deriving the Shor relaxation of (P) is to rewrite (P) in a vectorized form. Define $y=\mathrm{vec}(\Gamma)=(\gamma_{0},\ldots,\gamma_{d})\in\mathbb{R}^{n(d+1)}$ as the vector of vertically stacked polynomial coefficients. Using the Kronecker product $\otimes$, we rewrite the linear constraints directly in terms of $y$. Applying the vectorization identity for Kronecker products, $\mathrm{vec}(LMN)=(N^{T}\otimes L)\mathrm{vec}(M)$, the boundary conditions $\Gamma A=B$ become $(A^{T}\otimes I_{n})y=\mathrm{vec}(B)$.

Next, we rewrite the cost and the arguments to $\mathcal{L}$ in terms of $yy^{T}$ and $y$. Define the partial trace $\mathrm{tr}_{n}:\mathbb{S}^{n(d+1)}\rightarrow\mathbb{S}^{d+1}$ by $[\mathrm{tr}_{n}(M)]_{ij}=\mathrm{tr}(M_{ij})$, where $M_{ij}\in\mathbb{R}^{n\times n}$ is the $(i,j)$ block of $M$. The partial trace will let us translate between the outer products that arise from vectorization and the Gram matrices that appear in (P). Specifically, a direct computation shows that for any $M,N\in\mathbb{R}^{n\times(d+1)}$, Applying to the arguments of $\mathcal{L}$ in (P) gives all the substitutions we need to vectorize the problem. Setting $(M,N)$ to $(\Gamma,\Gamma)$, $(\Gamma,cu^{T})$, and $(cu^{T},cu^{T})$ yields $\Gamma^{T}\Gamma=\mathrm{tr}_{n}(yy^{T})$, $\Gamma^{T}cu^{T}=\mathrm{tr}_{n}(y(u\otimes c)^{T})$, and $(c^{T}c)\,uu^{T}=\mathrm{tr}_{n}((uu^{T})\otimes(cc^{T}))$, respectively, where we used $\mathrm{vec}(cu^{T})=u\otimes c$ and the Kronecker mixed-product rule. The vectorized form of (P) is then with $y\in\mathbb{R}^{n(d+1)}$ and $Q_{0},Q_{1}$ unchanged from (P).

The Shor relaxation is then formed by introducing $Y\in\mathbb{S}^{n(d+1)}$ with the constraint $Y=yy^{T}$, and relaxing this nonconvex equality into $Y\succeq yy^{T}$. The resulting relaxation is: We have included the implied constraint $(A^{T}\otimes I_{n})Y=\mathrm{vec}(B)\,y^{T}$, which is redundant when $Y=yy^{T}$ but tightens the relaxation, analogously to $XA=\Gamma^{T}B$ in (SDP). The PSD variables of the two relaxations are related by $\mathrm{tr}_{n}(Y)=X$.

We now show how (SDP) is a symmetry-reduced version of (Shor). To expose the symmetry, we decompose $Y=yy^{T}+S$, where $S\succeq 0$ is a positive semidefinite slack variable. Since $(A^{T}\otimes I_{n})y=\mathrm{vec}(B)$, the implied constraint reduces to $(A^{T}\otimes I_{n})S=0$. With this substitution, (Shor) becomes The key observation to see the symmetry in the problem is that both the cost and the linear map constraint depend on $S$ only through $\mathrm{tr}_{n}(S)\in\mathbb{S}^{d+1}$, a much smaller matrix than $S\in\mathbb{S}^{n(d+1)}$. Let $O(n):=\{Q\in\mathbb{R}^{n\times n}\mid Q^{T}Q=I_{n}\}$ denote the orthogonal group.

### Lemma 5

(Shor^′^) is invariant under the transformation for any $Q\in O(n)$. That is, if $(y,S)$ is feasible, then so is $(y,T_{Q}(S))$ with the same cost.

Since (Shor^′^) is invariant under the action of $O(n)$ on $S$, and the feasible set is convex in $S$ for any fixed $y$, we can restrict $S$ to the fixed-point subspace defined as $\{S:T_{Q}(S)=S\text{ for all }Q\in O(n)\}$ without loss of optimality. This follows from the standard averaging argument for symmetry reduction of semidefinite programs; see, e.g., for details.

### Lemma 6

The fixed-point subspace of the transformation is i.e., the set of matrices satisfying $T_{Q}(S)=S$ for all $Q\in O(n)$.

### Theorem 6

(SDP) is the symmetry-reduced version of (Shor). Specifically, restricting $S$ in (Shor^′^) to the fixed-point subspace recovers (SDP).

The symmetry reduction thus replaces the PSD variable $S\in\mathbb{S}^{n(d+1)}$ with $\Lambda\in\mathbb{S}^{d+1}$, reducing the size of the PSD cone by a factor of $n$.

### B Proofs for the Theoretical Results

In the proofs below, $Q_{0}$ and $Q_{1}$ are carried over unchanged between the programs, so we omit them from feasible points.

### Proof of Theorem 1

Start by noticing that the cost in (P~ρ~) is unchanged by $\rho$, and thus all (P~ρ~) share the same cost (to see this, consider introducing $X=\Gamma^{T}\Gamma+V^{T}V$). Let $\mathcal{F}_{\text{P}_{\rho}}$ be the feasible set of (P~ρ~), and let $\Pi_{\rho}$ be the operator that projects a set onto the variables from (P~ρ~). As the cost is shared across (P~ρ~), it is enough to show $\mathcal{F}_{\text{P}_{\rho}}\subseteq\Pi_{\rho}(\mathcal{F}_{\text{P}_{\rho+1}})$ to show that the cost is monotonically decreasing as we increase $\rho$. Let $(\Gamma^{\prime},V^{\prime})$ be any feasible point to (P~ρ~), where $V^{\prime}\in\mathbb{R}^{\rho\times(d+1)}$. Then $(\Gamma^{\prime},(V^{\prime},0))$ is feasible for $(\text{P}_{\rho+1})$, where $(V^{\prime},0)\in\mathbb{R}^{(\rho+1)\times(d+1)}$. ∎

### Proof of Theorem 2

Start by defining a semidefinite relaxation for the lifted program (P~ρ~) for each $\rho\in\mathbb{N}$ (by following the same procedure in section V), but with $X=\Gamma^{T}\Gamma+V^{T}V$, as: The collision avoidance constraint in (SDP~ρ~) is identical to the one in (SDP), and the last constraint can equivalently be expressed as an LMI via the Schur complement, as. Because (SDP~ρ~) is a convex relaxation of (P~ρ~) we immediately have $c_{\text{SDP}_{\rho}}^{*}\leq c_{\text{P}_{\rho}}^{*}$. It remains to show $c_{\text{SDP}_{\rho}}^{*}=c_{\text{SDP}}^{*}$ for all $\rho$. Let $\mathcal{F}_{\text{SDP}_{\rho}}$ be the feasible set of (SDP~ρ~) and $\Pi(\mathcal{F}_{\text{SDP}_{\rho}})$ its projection onto the variables from (SDP). The cost for (SDP) and (SDP~ρ~) is the same, so we will show that $\mathcal{F}_{\text{SDP}}=\Pi(\mathcal{F}_{\text{SDP}_{\rho}})$. First, let $(\Gamma^{\prime},X^{\prime})$ be any feasible point to (SDP). Then $(\Gamma^{\prime},V^{\prime}=0,X^{\prime})$ is feasible to (SDP~ρ~): the collision avoidance, tightening, and boundary constraints for $\Gamma$ carry over directly, $V^{\prime}A=0$ is trivially satisfied, and $X^{\prime}\succeq(\Gamma^{\prime})^{T}\Gamma^{\prime}=(\Gamma^{\prime})^{T}\Gamma^{\prime}+0$ satisfies the last constraint in (SDP~ρ~). For the other direction, let $(\Gamma^{\prime},V^{\prime},X^{\prime})$ be feasible to (SDP~ρ~), where $\Gamma^{\prime}\in\mathbb{R}^{n\times(d+1)}$ and $V^{\prime}\in\mathbb{R}^{\rho\times(d+1)}$. We show that $(\Gamma^{\prime},X^{\prime})$ is feasible to (SDP). The boundary constraint $\Gamma^{\prime}A=B$ and tightening constraint $X^{\prime}A=(\Gamma^{\prime})^{T}B$ carry over directly from (SDP~ρ~). Finally, from the Schur complement of the LMI in (SDP~ρ~), we have $X^{\prime}\succeq(\Gamma^{\prime})^{T}\Gamma^{\prime}+(V^{\prime})^{T}V^{\prime}\succeq(\Gamma^{\prime})^{T}\Gamma^{\prime}$, which satisfies the constraint in (SDP). ∎

### Proof of Theorem 3

Let $(\Gamma^{*},X^{*})$ be an optimal solution to (SDP), and let $\rho=\text{rank}(X^{*}-(\Gamma^{*})^{T}\Gamma^{*})$. First, consider the case when $\rho=0$, i.e. $X^{*}=(\Gamma^{*})^{T}\Gamma^{*}$. In this case, $\Gamma^{*}$ is immediately feasible for $(\text{P})$, and since $c_{\text{SDP}}^{*}$ provides a lower bound that is attained by this feasible point, it must be optimal. Next, consider the case when $\rho>0$. From we have $X^{*}-(\Gamma^{*})^{T}\Gamma^{*}\succeq 0$, so we can factorize where $V^{*}\in\mathbb{R}^{\rho\times(d+1)}$, $V^{*}\neq 0$. By construction, $(\Gamma^{*},V^{*})^{T}(\Gamma^{*},V^{*})=(\Gamma^{*})^{T}\Gamma^{*}+(V^{*})^{T}V^{*}=X^{*}$. We now show that $(\Gamma^{*},V^{*})$ is optimal for $(\text{P}_{\rho})$. First, we show feasibility. The collision avoidance constraint in $(\text{P}_{\rho})$ is satisfied because $(\Gamma^{*},V^{*})^{T}(\Gamma^{*},V^{*})=X^{*}$ so the constraint reduces to the one in (SDP). For the boundary constraint, we have from (SDP) that $\Gamma^{*}A=B$ and $X^{*}A=(\Gamma^{*})^{T}B$, which gives so $(V^{*})^{T}V^{*}A=0$, implying $V^{*}A=0$. This shows that the tightening constraints $X^{*}A=(\Gamma^{*})^{T}B$ in (SDP) are necessary to ensure that $V^{*}$ satisfies the boundary conditions $V^{*}A=0$ in (P~ρ~). Finally, we show optimality. By Theorem 2, we have $c_{\text{SDP}}^{*}\leq c_{\text{P}_{\rho}}^{*}$. By construction, $c_{\text{SDP}}^{*}=\mathrm{tr}(G^{(k)}X^{*})=\mathrm{tr}(G^{(k)}((\Gamma^{*})^{T}\Gamma^{*}+(V^{*})^{T}V^{*}))$. As $(\Gamma^{*},V^{*})$ is feasible for $(\text{P}_{\rho})$ and attains the lower bound, it must be optimal. ∎

### Proof of Lemma 4

Let $M=X-\Gamma^{T}\Gamma$ for an optimal $(\Gamma,X)$, so $\rho=\operatorname{rank}(M)$. By the boundary constraint $\Gamma A=B$ and the tightening constraint $XA=\Gamma^{T}B$, we have $MA=XA-\Gamma^{T}\Gamma A=0$, so $\operatorname{col}(A)\subseteq\ker M$ and $\rho\leq(d+1)-\operatorname{rank}(A)=(d+1)-2(\ell+1)$, as $\operatorname{rank}(A)=2(\ell+1)$ since the boundary conditions are independent Hermite interpolation conditions. ∎

### Proof of Theorem 4

We start by showing necessity. Suppose $c_{\text{P}}^{*}=c_{\text{P}_{\rho}}^{*}$ for all $\rho\in\mathbb{N}$. Then Theorem 3 immediately gives us a $\rho$ such that $c_{\text{SDP}}^{*}=c_{\text{P}_{\rho}}^{*}=c_{\text{P}}^{*}$. Next, we show sufficiency. Suppose $c_{\text{SDP}}^{*}=c_{\text{P}}^{*}$. Theorem 2 gives $c_{\text{P}}^{*}=c_{\text{SDP}}^{*}\leq c_{\text{P}_{\rho}}^{*}$ for all $\rho\in\mathbb{N}$. The reverse inequality follows immediately from Theorem 1, and equality must hold. ∎

### Proof of Theorem 5

Let $(\Gamma,X)$ be any optimal solution to (SDP). We consider two cases. First, suppose $X=\Gamma^{T}\Gamma$. Then $\Gamma$ is feasible for (P) with cost $\mathrm{tr}(G^{(k)}\Gamma^{T}\Gamma)=c_{\text{SDP}}^{*}=c_{\text{P}}^{*}$, so $\Gamma$ achieves the lower bound of the relaxation and must therefore also be optimal for (P). By the uniqueness assumption (with $\rho=0$), $\Gamma=\Gamma^{*}$, and therefore $X=(\Gamma^{*})^{T}\Gamma^{*}$. Second, suppose $X\neq\Gamma^{T}\Gamma$. Let $\rho=\operatorname{rank}(X-\Gamma^{T}\Gamma)>0$ and factor $V^{T}V=X-\Gamma^{T}\Gamma$, where $V\neq 0$ due to $\rho>0$. By Theorem 3, $(\Gamma,V)$ is optimal for (P~ρ~). By the uniqueness assumption, $(\Gamma,V)=(\Gamma^{*},0)$, which contradicts $V\neq 0$. Therefore, every optimal solution to (SDP) equals $(\Gamma^{*},(\Gamma^{*})^{T}\Gamma^{*})$. ∎

### C Proofs for Symmetry Reduction

### Proof of Lemma 5

Let $\tilde{S}=(I_{d+1}\otimes Q^{T})S(I_{d+1}\otimes Q)$. Writing $S$ in terms of its $n\times n$ blocks $S_{ij}$, the transformation acts as $S_{ij}\mapsto Q^{T}S_{ij}Q$. By the cyclic property of the trace, $\mathrm{tr}(Q^{T}S_{ij}Q)=\mathrm{tr}(S_{ij})$, so the partial trace is invariant under this transformation, $\mathrm{tr}_{n}(\tilde{S})=\mathrm{tr}_{n}(S)$, and the cost and linear map constraint are preserved. For the boundary constraint, the mixed-product property of Kronecker products gives $(A^{T}\otimes I_{n})(I_{d+1}\otimes Q^{T})=A^{T}\otimes Q^{T}=(I\otimes Q^{T})(A^{T}\otimes I_{n})$, so $(A^{T}\otimes I_{n})\tilde{S}=(I_{p}\otimes Q^{T})(A^{T}\otimes I_{n})S(I_{d+1}\otimes Q)=0$ (by the implied boundary constraint). Finally, $\tilde{S}\succeq 0$ since it is a congruence of $S\succeq 0$. ∎

### Proof of Lemma 6

The transformation acts independently on each $n\times n$ block as $\bar{S}_{ij}\mapsto Q^{T}\bar{S}_{ij}Q$, so invariance requires $Q^{T}\bar{S}_{ij}Q=\bar{S}_{ij}$ for all $Q\in O(n)$. It is a standard result that this implies $\bar{S}_{ij}=(1/n)\lambda_{ij}I_{n}$ for some $\lambda_{ij}\in\mathbb{R}$. Collecting these scalars into $\Lambda=[\lambda_{ij}]\in\mathbb{S}^{d+1}$ gives $\bar{S}=\frac{1}{n}\Lambda\otimes I_{n}$. ∎

### Proof of Theorem 6

We substitute $S=\frac{1}{n}\Lambda\otimes I_{n}$ into (Shor^′^) and define $X=\Gamma^{T}\Gamma+\Lambda$. Since $\mathrm{tr}_{n}(S)=\Lambda$ and $\mathrm{tr}_{n}(yy^{T})=\Gamma^{T}\Gamma$, we have $\mathrm{tr}_{n}(yy^{T}+S)=X$, recovering the cost and linear map constraint of (SDP). The boundary condition $\Gamma A=B$ is unchanged, and $(A^{T}\otimes I_{n})S=0$ becomes $\Lambda A=0$, so $XA=(\Gamma^{T}\Gamma+\Lambda)A=\Gamma^{T}B$. Finally, $S\succeq 0$ if and only if $\Lambda\succeq 0$, since the eigenvalues of $\Lambda\otimes I_{n}$ are exactly those of $\Lambda$, each with multiplicity $n$, which is equivalent to $X\succeq\Gamma^{T}\Gamma$, i.e., $\begin{bmatrix}I_{n}&\Gamma\\\Gamma^{T}&X\end{bmatrix}\succeq 0$. ∎

### D Bézier Curves and the Bernstein Basis

In our implementation, we use the standard Bernstein basis, which differs from the scaled Bernstein basis used in the main text by a binomial scaling. The $i$-th standard Bernstein basis polynomial of degree $d$ is defined as for $i=0,\ldots,d$ and $s\in$. We use the following identities, which follow from the basis definition:

### D1 Curve Costs for Bézier Curves

Derivatives of Bézier curves are Bézier curves of reduced degree: where $D_{d}^{(k)}:=D_{d}D_{d-1}\cdots D_{d-k+1}\in\mathbb{R}^{(d+1)\times(d-k+1)}$ and $D_{d}\in\mathbb{R}^{(d+1)\times d}$ is the forward difference matrix with $-1$ on the diagonal and $1$ on the subdiagonal. The Gram matrix $G_{d}$ from has entries which follows from the product rule and $\int_{0}^{1}B_{i}^{d}(s)\,ds=1/(d+1)$. Substituting into the cost integral gives $\int_{0}^{1}\|\gamma^{(k)}(s)\|_{2}^{2}\,ds=\mathrm{tr}(G^{(k)}\Gamma^{T}\Gamma)$, where

### D2 Collision Avoidance for Bézier Curves

We now write the collision-avoidance condition from Lemma 3. ‣ IV-B Collision-Avoidance with Bézier Curves ‣ IV Certifying Collision-Avoidance ‣ Semidefinite Relaxations for Collision-Free Motion Planning") for Bézier curves, i.e., in the standard Bernstein basis. The derivation follows exactly as in the main body, with the standard Bernstein basis replacing the scaled one.

The partition of unity property of the standard Bernstein basis immediately gives $u=e$: From the product rule, the map $\mathcal{S}_{d}:\mathbb{S}^{d+1}\rightarrow\mathbb{R}^{2d+1}$ is given: Similarly, using, $\mathcal{T}_{d}:\mathbb{S}^{d}\rightarrow\mathbb{R}^{2d+1}$ is given:
