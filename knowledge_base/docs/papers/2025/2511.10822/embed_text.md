## Introduction

Trajectory planning for autonomous navigation has been extensively studied with various parameterizations. Hard-constraint approaches explicitly enforce safety but require computationally intensive solvers unsuitable for high-frequency replanning. Soft-constraint planners (EGO-Planner, RAPTOR, SUPER ) achieve faster convergence. Some jointly optimize geometry and timing, while others decouple path and time allocation. Increasing decision variables improves performance but enlarges the problem. Building on these ideas, we introduce MIGHTY, a Hermite spline-based planner.

endpoint derivs, time
limited polynomial+time space
direct but global

B-spline cntrl pts, time
limited polynomial+time space

B-spline cntrl pts
limited polynomial+time space

B-spline cntrl pts
limited polynomial+time space

limited polynomial+time space (MINCO class)

Hermite cntrl pts, time
full polynomial+time space
direct &amp; local

TABLE I: State-of-the-art Unconstrained UAV Trajectory Planners

### I-A Review of Unconstrained Frameworks

Differential flatness enables efficient optimization of quadrotor trajectories by parameterizing the flat output and their derivatives. Given fixed timestamps at trajectory waypoints, minimum control effort (e.g., jerk/snap) problems using piecewise polynomial representation can be formulated as quadratic programs (QPs), which are convex and can be solved efficiently. However, when segment durations are included as optimization variables (time allocation), the resulting joint problem becomes substantially more complex, yielding a nonlinear program (NLP) that is often ill-conditioned because of the coupling between spatial and temporal variables.

Decoupling into two stages enables unconstrained formulations by replacing hard constraints with soft penalties. Richter et al. use 9^th^-order polynomials with endpoint derivatives: a QP minimizes snap, then gradient-based time allocation adjusts duration. Endpoint derivatives are decision variables, so there is direct derivative parameterization. However, the free derivatives are globally coupled, so there is no local control. Collision avoidance inserts mid-segment waypoints, triggering repeated solves. Extensions improve stability and enable real-time replanning via ESDF-based potential costs.

Another standard unconstrained framework uses B-splines for trajectory representation, with time-related variables encoded in a knot vector. B-splines offer inherent smoothness and geometric local control: changing one control point affects only a bounded neighborhood of the curve. The convex hull property enables efficient collision checking and enforces dynamic feasibility. However, B-splines do not provide direct local control of higher-order derivatives. Derivatives at any curve point are implicit functions of multiple neighboring control points. One can bound derivatives efficiently via the convex hull property, but cannot independently prescribe a specific velocity or acceleration at a given knot through a single variable. This geometric local control property has been widely exploited for efficient trajectory refinement and replanning in cluttered environments. Zhou et al. parameterize trajectories as non-uniform cubic B-splines initialized from kinodynamic A\* paths. The nonlinear optimization minimizes the cost considering smoothness, a repulsive collision potential from a Euclidean distance field (EDF), and soft penalties on derivative control points exceeding maximum velocity and acceleration. Finally, an iterative time-adjustment method rescales knot spans of the non-uniform spline to guarantee dynamic feasibility. EGO-Planner and RAPTOR simplify the representation by using uniform B-splines with fixed knot spans, leveraging convex hull properties to enforce velocity, acceleration, and jerk constraints directly on control points. EGO-Planner optimizes trajectories via a quasi-Newton solver (L-BFGS) for fast gradient-based convergence, with an additional time-reallocation and anisotropic curve-fitting refinement stage that resizes knot spans and fits a new spline to ensure feasibility and smoothness. RAPTOR also employs a two-stage process: a closed-form QP warm-start for initial smoothness, followed by a nonlinear refinement phase that penalizes collision via an ESDF and ensures dynamic limits via control point constraints.

Wang et al. employ diffeomorphism between coefficients and derivatives with linear-complexity gradients. MINCO builds on this: coefficients are analytically determined by waypoints and durations, jointly optimized via linear-complexity solver for minimum jerk/snap. MINCO excels when minimum control effort dominates, but searches only the MINCO class. MINCO's waypoint positions are decision variables, but polynomial coefficients are determined through a banded linear system that couples adjacent segments, so there is no geometric local control. Higher-order derivatives are not decision variables, and they are analytically determined from waypoints and durations, so there is no direct higher-derivative control. Under added objectives, this restriction can yield suboptimal performance compared to more general representations. EGO-Swarm2 and SUPER adopt MINCO; SUPER adds exploratory/backup trajectories for safety.

MIGHTY optimizes positions and derivatives at each knot and time durations as explicit variables, enabling local control of waypoints and higher-order dynamics.

### I-B MIGHTY Contributions

Table I summarizes the discussion above. Unconstrained higher-order polynomial representations are typically too slow for real-time planning. Uniform or non-uniform splines can generate trajectories faster compared to spatiotemporal joint optimization; however, they can generate sub-optimal trajectories due to decoupled time adjustment. Waypoint-and-duration-based parameterizations are restricted to the low-dimensional subspace induced by the MINCO parameterization, lack direct parameterization of higher-order derivatives at individual knots, and exhibit waypoint propagation where changes to one waypoint affect multiple segments through the globally coupled coefficient system. While these effects enable compact representation and analytical optimality for minimum-control objectives, they can complicate constraint/cost handling beyond minimum-control and limit local control of trajectory shape and higher-order dynamics.

To address the limitations of existing soft-constraint planners, MIGHTY uses a Hermite-spline representation and an unconstrained nonlinear optimizer that searches directly over spatial waypoints, endpoint derivatives, and segment durations. A Hermite spline representation guarantees continuity without global coefficient coupling, which fundamentally enables direct local control over both positions and higher-order dynamics at each knot. These properties could be exploited for efficient trajectory refinement (as in B-spline methods ) but are not available in MINCO's globally coupled parameterization. The key contributions of the paper are:

Hermite Spline Planner: Joint spatiotemporal optimization in a single solve, with explicit parameterization of positions and derivatives at each knot. This representation enables local control of higher-order dynamics and trajectory shape, which the optimizer can leverage when needed. The approach, MIGHTY, achieves fast solve times and lower travel time than baselines.

Comprehensive Simulation Study: We benchmark in both simple and complex scenes, comparing against state-of-the-art methods in static environments and validating safe behavior in dynamic environments. MIGHTY achieves $9.3\ \%$ reduction in computation time and $13.1\ \%$ reduction in travel time in trajectory representation benchmarking, and it achieves the shortest travel time and path length while maintaining the $100\ \%$ success rate.

Extensive Hardware Experiments: Long-duration and high-speed flights, and dynamic obstacle avoidance scenarios using a LiDAR-based perception and localization system. MIGHTY achieves collision-free flights and a top speed of $6.7\ {m/s}$ in high-speed flight experiments.

## Hermite Spline

This section introduces the Hermite-spline notation used in MIGHTY's formulation. MIGHTY uses a degree-$d$ Hermite spline with $M$ segments. For odd degree $d = {{2\nu} + 1}$, each segment is parameterized by the knot values of the position and its derivatives up to order $\nu$. For example, a quintic Hermite spline ($d = 5$, $\nu = 2$) specifies position, velocity, and acceleration. Across knots, a Hermite spline automatically guarantees $\mathcal{C}^{\nu}$ continuity by sharing the knot values. Although Hermite splines apply in any dimension, we work in ${\mathbb{R}}^{3}$ for quadrotor planning and use $d = 5$ in this paper. For each segment $s = {0,\ldots,{M - 1}}$, we define a normalized time variable $\tau_{s} \in {\lbrack 0,1\rbrack}$ on segment $s$ as ${\tau_{s} = {{({t - t_{s}})}/T_{s}} \in {\lbrack 0,1\rbrack}}.$ Then each segment can be denoted as: ${{{\mathbf{x}{(t)}} = {\mathbf{x}_{s}{(\tau_{s})}}},{t \in \left\lbrack t_{s},t_{s + 1} \right\rbrack}},$ where $t_{s}:={\sum_{r = 0}^{s - 1}T_{r}}$, and $T_{s}$ is the duration of segment $s$. Then we write

where ${{\mathbf{H}_{s,0} = \mathbf{p}_{s}},{{\mathbf{H}_{s,1} = {T_{s}\mathbf{v}_{s}}},{{\mathbf{H}_{s,2} = {\frac{1}{2}T_{s}^{2}\mathbf{a}_{s}}},{{\mathbf{H}_{s,3} = \mathbf{p}_{s + 1}},{{\mathbf{H}_{s,4} = {T_{s}\mathbf{v}_{s + 1}}},{\mathbf{H}_{s,5} = {\frac{1}{2}T_{s}^{2}\mathbf{a}_{s + 1}}}}}}}}.$ Here, $h_{k}{(\tau_{s})}$ are the standard quintic Hermite basis functions. The ${\mathbf{p}_{i},\mathbf{v}_{i},\mathbf{a}_{i}} \in {{\mathbb{R}}^{3}{({i = {0,\ldots,M}})}}$ and $T_{s} > {0{({s = {0,\ldots,{M - 1}}})}}$ are the interior knot positions, velocities, accelerations, and segment durations, respectively.

## MIGHTY

### III-A Decision Variables

As shown in Sec. II, the knot states $\mathbf{p}_{i},\mathbf{v}_{i},{\mathbf{a}_{i}{({i = {0,\ldots,M}})}}$ and segment durations $T_{s}{({s = {0,\ldots,{M - 1}}})}$ fully determine the trajectory. Thus we optimize the interior positions, velocities, accelerations, and per-segment durations:

with fixed boundary states $(\mathbf{p}_{0},\mathbf{v}_{0},\mathbf{a}_{0})$ and $(\mathbf{p}_{M},\mathbf{v}_{M},\mathbf{a}_{M})$.

To keep the optimization unconstrained while enforcing certain requirements (e.g., $T_{s} > 0$), we apply diffeomorphism, such as $T_{s} = {\phi{(\sigma_{s})}}$ with ${{{\phi{(\sigma)}} = e^{\sigma}},{\sigma_{s} \in {\mathbb{R}}}}.$ We also find that optimizing raw derivative knots $(\mathbf{v}_{i},\mathbf{a}_{i})$ can be numerically unstable. Sec. III-D introduces scalings that improve stability without changing the optimum. For clarity, the formulas below are written in terms of the original variables $(\mathbf{p}_{s},\mathbf{v}_{s},\mathbf{a}_{s},T_{s})$; applying a diffeomorphism only inserts chain-rule factors in the gradients.

### III-B Representations

Given the quintic Hermite segment in Eq., a smooth cost can be expressed in terms of the raw Hermite variables $(\mathbf{p}_{s},\mathbf{v}_{s},\mathbf{a}_{s},\mathbf{p}_{s + 1},\mathbf{v}_{s + 1},\mathbf{a}_{s + 1},T_{s})$. However, evaluating costs and gradients directly in Hermite form can be computationally expensive, and other representations, such as Bézier curve, can be more efficient.

For instance, a Bézier curve allows efficient evaluation of the trajectory and its derivatives at arbitrary sample points. A degree-$n$ Bézier segment is written as ${{{\mathbf{x}{(u)}} = {\sum_{i = 0}^{n}{B_{i}^{n}{(u)}\mathbf{c}_{i}}}},{u \in {\lbrack 0,1\rbrack}}},$ where the vectors $\mathbf{c}_{i}$ are the Bézier control points, and the Bernstein basis polynomials are ${{{B_{i}^{n}{(u)}} = {\binom{n}{i}u^{i}{({1 - u})}^{n - i}}},{i = {0,\ldots,n}}}.$ Because evaluation is just a weighted sum of control points with weights $B_{i}^{n}{(u)}$, sampling reduces to a few dot products with small, reusable tables. Then each sample is a small dot product: positions use the $B_{i}^{5}$ table, and derivatives use the degree-reduced Bernstein weights. Since these tables are tiny and shared across iterations, and each dot product has only $6,5,4,3$ terms (for degree $5$ down to $2$), this is faster and numerically steadier than recomputing higher-order Hermite polynomials and their derivatives at every sample.

Although Bézier representation has these computational advantages, note that Bézier control points do not enforce cross-segment continuity by themselves. On the other hand, Hermite variables guarantee $\mathcal{C}^{k}$ continuity across segments by construction. Therefore, it is often advantageous to optimize in the Hermite parameterization while evaluating cost terms in the Bézier basis to exploit its computational benefits. In our simulations and hardware experiments, we optimize over Hermite and evaluate costs in Bézier; however, in general, MIGHTY does not require Bézier for cost evaluation.

### III-C Objective and Closed-Form Gradient

To make the formulation basis-independent, we express the objective and its gradients w.r.t. a generic control-point (or coefficient) vector $\mathbf{c}$, independent of the chosen parameterization (Hermite end states, Bézier control points, etc.). As a concrete example, the affine map between Hermite and Bézier on segment $s$ is

Let $\mathbf{c}_{s} = {\lbrack{\mathbf{c}_{s,0}^{\top}\cdots\mathbf{c}_{s,5}^{\top}}\rbrack}^{\top}$ and $\mathbf{y}_{s} = {\lbrack\mathbf{p}_{s}^{\top},\mathbf{v}_{s}^{\top},\mathbf{a}_{s}^{\top},\mathbf{p}_{s + 1}^{\top},\mathbf{v}_{s + 1}^{\top},\mathbf{a}_{s + 1}^{\top}\rbrack}^{\top}$, so $\mathbf{c}_{s} = {C{(T_{s})}\mathbf{y}_{s}}$. Let the total objective be ${{J{(\mathbf{z})}} = {\sum_{s = 0}^{M - 1}{J_{s}\left( \mathbf{c}_{s} \right)}}}.$ To obtain $\partial{J/{\partial\mathbf{z}}}$, we first compute the derivatives w.r.t $\mathbf{y}_{s}$ and $T_{s}$, then apply the chain rule back to $\mathbf{z}$. Denote $\mathbf{g}_{\mathbf{c}_{s}} \equiv {\partial{J_{s}/{\partial\mathbf{c}_{s}}}}$ and the explicit time derivative ${{\partial{J_{s}/{\partial T_{s}}}}|}_{\text{explicit}}.$ Since ${\partial{\mathbf{c}_{s}/{\partial\mathbf{y}_{s}}}} = {C{(T_{s})}}$, the chain rule yields

Note that the explicit time derivative $\left. {\partial{J_{s}/{\partial T_{s}}}} \right|_{\text{explicit}}$ comes from factors like $T_{s}^{5}$ in smoothness integrals. Using Eq., the entries of $C{(T_{s})}$ are simple constants, so Eq. expands to the following closed-form expressions:

The coefficient gradient $\partial{\mathbf{c}_{s}/{\partial T_{s}}}$ ($= {\nabla_{T_{s}}\mathbf{c}_{s}}$) used in the coefficient path in Eq. can be computed in closed form as

Therefore, to obtain the gradient, we need to compute $\mathbf{g}_{\mathbf{c}_{s}}$ and $\left. {\partial{J_{s}/{\partial T_{s}}}} \right|_{\text{explicit}}.$ Here we present two types of cost terms: cost terms defined on control points, and cost terms defined via sampled states along the trajectory, and their gradients used in Sec. IV.

### III-C1 Cost on Control Points

We first consider cost terms that are expressed directly in terms of the coefficients/control points, such as integrated squared jerk. For a quintic Bézier segment $s$ with control points ${\mathbf{c}_{s,0},\ldots,\mathbf{c}_{s,5}} \in {\mathbb{R}}^{3}$, obtained from the Hermite endpoint states via Eq., the third forward differences are: ${{\Delta_{s,m} = {{{\mathbf{c}_{s,{m + 3}} - {3\mathbf{c}_{s,{m + 2}}}} + {3\mathbf{c}_{s,{m + 1}}}} - \mathbf{c}_{s,m}}},{m \in {\{ 0,1,2\}}}}.$ Then, the integrated squared jerk on segment $s$ is

where $C_{s} = {3600T_{s}^{- 5}}$. Define the (scalar) Bernstein-quadratic Gram matrix $G \in {\mathbb{R}}^{3 \times 3}$ by $G_{mn} \triangleq \int_{0}^{1}B_{m}^{2}{(\tau_{s})}B_{n}^{2}{(\tau_{s})}d\tau_{s}\quad{(m,n = 0,1,2)},$ so that, with $\Delta_{s} \triangleq {\lbrack\Delta_{s,0}^{\top},\Delta_{s,1}^{\top},\Delta_{s,2}^{\top}\rbrack}^{\top} \in {\mathbb{R}}^{9}$,

(Explicitly, $G$ is symmetric positive definite with constants ${G_{00} = G_{22} = \frac{1}{5}},{{G_{11} = \frac{2}{15}},{G_{01} = G_{12} = \frac{1}{10}}},{G_{02} = \frac{1}{30}}$.)

Let ${\lambda_{\min},\lambda_{\max}} > 0$ be the smallest and largest eigenvalues of $G$. Since $Q = {G \otimes I_{3}}$, the eigenvalues of $Q$ are the eigenvalues of $G$, each repeated three times. Hence ${{\lambda_{\min}{\|\Delta_{s}\|}^{2}} \leq {\Delta_{s}^{\top}Q\Delta_{s}} \leq {\lambda_{\max}{\|\Delta_{s}\|}^{2}}}.$ Therefore a computationally cheap surrogate is the diagonally weighted form ${{\overset{\sim}{J}}_{\text{smooth}} = {\sum_{s = 0}^{M - 1}{C_{s}{\sum_{m = 0}^{2}{w_{m}{\|\Delta_{s,m}\|}^{2}}}}}},$ with fixed positive weights $w_{m}$, which is equivalent to the exact cost up to a constant factor bounded by $\lambda_{\min}$ and $\lambda_{\max}$.

Now we derive $\partial{J_{\text{smooth}}/{\partial\mathbf{c}}}$: Each $\Delta_{s,m}$ is an affine combination of four consecutive control points with coefficients $\alpha_{j,m} \in {\{{- 1},3,{- 3},1\}}$ at indices $j = {m,\ldots,{m + 3}}$. Hence, ${\partial{J_{\text{smooth}}/{\partial\Delta_{s,m}}}} = {2C_{s}\Delta_{s,m}}$ ${{\partial{J_{\text{smooth}}/{\partial\mathbf{c}_{s,j}}}} = {2C_{s}{\sum_{m = 0}^{2}{\alpha_{j,m}\Delta_{s,m}}}}}.$ Stacking, we obtain

We can now derive $\partial{J_{\text{smooth}}/{\partial T_{s}}}$. Eq. has two contributions. Since $C_{s} = {3600T_{s}^{- 5}}$, the first contribution is

Using Eqs. and, we derive the second term of Eq. and obtain a closed-form expression.

### III-C2 Cost on Sampled States

Now we consider cost terms that are evaluated on sampled states of the trajectory. Fix a set of sample points ${\{\tau_{s,j}\}}_{j = 0}^{\kappa_{s}} \subset {\lbrack 0,1\rbrack}$ for segment $s$. Define a generic per-sample cost $\ell:{{{\mathbb{R}}^{3} \times {\mathbb{R}}^{3} \times {\mathbb{R}}^{3} \times {\mathbb{R}}^{3} \times {\mathbb{R}}_{> 0}}\rightarrow{\mathbb{R}}}$, $\ell{(\mathbf{x},\mathbf{v},\mathbf{a},\mathbf{j};T)}$. The sampled cost on segment $s$ is

Let the sample Jacobians at $\tau_{s,j}$ be $\ell_{\mathbf{x}} = {\partial{\ell/{\partial\mathbf{x}}}}$, $\ell_{\mathbf{v}} = {\partial{\ell/{\partial\mathbf{v}}}}$, $\ell_{\mathbf{a}} = {\partial{\ell/{\partial\mathbf{a}}}}$, $\ell_{\mathbf{j}} = {\partial{\ell/{\partial\mathbf{j}}}}$. Typically $\ell$ has no explicit $T_{s}$ (as above), so $T_{s}$ appears only via time-scaling and quadrature weights. ^11^1If an explicit time term is desired, then $\ell = {\ell{(\mathbf{x},\mathbf{v},\mathbf{a},\mathbf{j};T_{s})}}$ and an extra $\partial{\ell/{\partial T_{s}}}$ term would be added when differentiating w.r.t. $T_{s}$. Then, holding $T_{s}$ fixed, the gradient w.r.t. the $k$th control point is

where we omit the argument of the Bernstein basis polynomials $B{(\tau_{s,j})}$ for clarity. Note that ${B_{r}^{n}{( \cdot )}} = 0$ if $r \notin {\{ 0,\ldots,n\}}$. Stacking over $k = {0,\ldots,5}$ gives $\mathbf{g}_{\mathbf{c}_{s}} = {\partial{J_{\text{samp},s}/{\partial\mathbf{c}_{s}}}}$, which is then pulled back (chain rule) and accumulated into the Hermite variables via Eq..

Changing $T_{s}$ affects the sampled cost in two ways. First, (a) state-scaling: Even if we hold the Bézier control points fixed (i.e., keep the curve in normalized time $\tau$ unchanged), rescaling $T_{s}$ changes the physical derivatives via $t = {t_{s} + {\tau_{s}T_{s}}}$. Second, (b) coefficients: In Hermite parameterizations the control points themselves depend on $T_{s}$ via the Hermite$\rightarrow$Bézier map. The two items below compute the partial derivative $\partial{J_{\text{samp},s}/{\partial T_{s}}}$ for both contributions.

State-scaling (fix $\mathbf{c}_{s}$). Holding $\mathbf{c}_{s}$ fixed means $\mathbf{x}{(\tau)}$ is unchanged at each sample $\tau_{s,j}$, but ${{\frac{\partial\mathbf{v}}{\partial T_{s}} = {- {\frac{1}{T_{s}}\mathbf{v}}}},{{\frac{\partial\mathbf{a}}{\partial T_{s}} = {- {\frac{2}{T_{s}}\mathbf{a}}}},{\frac{\partial\mathbf{j}}{\partial T_{s}} = {- {\frac{3}{T_{s}}\mathbf{j}}}}}}.$ Thus,

Coefficient. In Hermite parameterizations, the Bézier control points depend on $T_{s}$ (e.g., tangent/curvature control points include factors of $T_{s}$ and $T_{s}^{2}$). Using Eq. gives ${\left. \frac{\partial J_{\text{samp},s}}{\partial T_{s}} \right|_{\text{coeff}} = {\mathbf{g}_{c_{s}}^{\top}\frac{\partial\mathbf{c}_{s}}{\partial T_{s}}}}.$

Thus, combining (a) & (b) above yields, ${\frac{\partial J_{\text{samp},s}}{\partial T_{s}} = {\left. \frac{\partial J_{\text{samp},s}}{\partial T_{s}} \right|_{\text{states}} + \left. \frac{\partial J_{\text{samp},s}}{\partial T_{s}} \right|_{\text{coeff}}}}.$ Note that since generally sampling cost $\ell$ does not depend on $T_{s}$ explicitly, ${{\partial{J_{s}/{\partial T_{s}}}}|}_{\text{explicit}} = 0$.

### III-D Reparameterizations for Derivative Variables

Each segment with duration $T_{s}$ is parameterized by normalized time $\tau_{s} \in {\lbrack 0,1\rbrack}$; by the chain rule,

Optimizing raw knot derivatives $\{\mathbf{v}_{i},\mathbf{a}_{i}\}$ together with $\{ T_{s}\}$ introduces explicit $1/T_{s}$ and $1/T_{s}^{2}$ factors in the gradients, so short segments have larger influence. We therefore optimize scaled knot derivatives. Define an averaged local time as

and set ${{{\hat{\mathbf{v}}}_{i} = {{\overline{T}}_{i}\mathbf{v}_{i}}},{{\hat{\mathbf{a}}}_{i} = {{\overline{T}}_{i}^{2}\mathbf{a}_{i}}}}.$ This reparameterization aims to reduce the explicit $1/T_{s}$ and $1/T_{s}^{2}$ factors' effect in the gradients w.r.t. the derivative decision variables by optimizing the scaled variables $\{{\hat{\mathbf{v}}}_{i},{\hat{\mathbf{a}}}_{i}\}$ instead of $\{\mathbf{v}_{i},\mathbf{a}_{i}\}$. At the endpoints, the scaling uses the adjacent segment duration (no averaging), while at interior knots we use the local average duration to balance the influence of the two neighboring segments; in that case, the inverse-duration effects are mitigated but cannot be canceled for both segments simultaneously unless their durations match. Our ablation study in Sec. IV-E confirms the expected improvement in performance.

## Simulation Results

All simulations were run on an AlienWare Aurora R8 with an Intel^®^ Core^TM^ i9-9900K CPU and 64 GB RAM, using Ubuntu 22.04 LTS and ROS 2 Humble.

### IV-A Representation Benchmarking: Simple Case

We first benchmark MIGHTY against GCOPTER (which uses MINCO ) on a simple corner-avoidance task with fixed start and goal (Fig. 1). For a fair comparison, we implement GCOPTER's optimization cost in MIGHTY and use the same optimizer (L-BFGS ) and stopping tolerances. Both methods start from the same initial guess.

GCOPTER represents each segment as a fifth-order polynomial, so MINCO minimizes jerk (third-order effort) by construction. MIGHTY uses a fifth-order Hermite spline to match the polynomial degree. GCOPTER applies diffeomorphic parameterizations for waypoints and durations (waypoints remain inside the overlap of safe flight corridors (SFCs); durations stay positive). The only difference is that MIGHTY includes an explicit jerk smoothness term (Sec. III-C1), while GCOPTER does not add a separate smoothness cost because MINCO already minimizes jerk.

Figure 1: Benchmarking environment for a simple corner avoidance scenario. The blue-shaded polygons show the SFC. MIGHTY’s trajectory is colored by speed (warmer colors indicate faster speeds).

Figure 2: Benchmarking results for MIGHTY and GCOPTER for simple corner avoidance scenario in Fig. 1. MIGHTY achieves lower computation time, travel time, and path length, while GCOPTER yields lower jerk.

We enforce max velocity, $v_{\max} = {1.0\ {m/s}}$, max tilt angle, $\theta_{\max} = {1.05\ {rad}}$ ($\approx {60\ {^\circ}}$), max angular velocity, $\omega_{\max} = {2.1\ {{rad}/s}}$ ($\approx {120\ {{^\circ}/s}}$), max $f_{\max} = {12.0\ N}$ and min $f_{\min} = {2.0\ N}$ thrust. We set $w_{T} = {10^{2}}$, $w_{\text{SFC}} = {10^{4}}$, $w_{v} = {10^{4}}$, $w_{\theta} = {10^{4}}$, $w_{\omega} = {10^{4}}$, and $w_{f} = {10^{5}}$ for both MIGHTY and GCOPTER, where $w_{T}$, $w_{\text{SFC}}$, $w_{v}$, $w_{\theta}$, $w_{\omega}$, and $w_{f}$ are weights for time, SFC, velocity, angle, angular velocity, and thrust penalties, respectively. These match GCOPTER's default values in their code except $w_{T}$ (default $20$). We use $w_{T} = {10^{2}}$ because $w_{T} = {10^{3}}$ caused occasional constraint violations ($> {1\%}$) in GCOPTER. For MIGHTY, we set the jerk smoothness weight to $w_{smooth} = {10^{- 5}}$. GCOPTER sets yaw to the direction of motion, so yaw and yaw rate are determined by $\mathbf{p}$. Accordingly, although neither GCOPTER nor MIGHTY optimizes yaw directly, both penalize tilt angle and angular velocity. We configure MIGHTY this way solely for fair comparison with GCOPTER. Outside this benchmark (see Sec. IV-F), MIGHTY can use a different cost design.

The result in Fig. 2 shows that MIGHTY achieves a shorter travel time, with slightly faster computation and shorter path than GCOPTER. While GCOPTER produces smoother trajectories with lower jerk due to its constraint within the MINCO class, MIGHTY explores a larger search space to identify faster and more effective trajectories. This flexibility enables MIGHTY to achieve superior performance, and Sec. IV-B further investigates the jerk-performance trade-off.

### IV-B Smooth Weight Sweep Benchmarking

Fig. 2 shows MIGHTY yields higher jerk than GCOPTER while achieving better travel time. To quantify this trade-off, we sweep $w_{smooth} \in {\{{10^{- 5}},\ldots,{10^{3}}\}}$ in the same scenario. Fig. 3 shows that as $w_{smooth}$ increases, MIGHTY progressively reduces jerk, eventually surpassing GCOPTER's levels of smoothness. At $w_{smooth} = {10^{2}}$, MIGHTY matches GCOPTER's jerk while maintaining better performance and lower computation time, demonstrating that MIGHTY's higher jerk is a tunable design choice rather than an inherent limitation.

Figure 3: Effect of jerk-smoothness weighting in the simple corner-avoidance scenario (Fig. 1). As wsmooth increases, MIGHTY’s jerk decreases toward GCOPTER’s jerk (orange dotted reference). At wsmooth = 102 (vertical red line), MIGHTY matches GCOPTER’s jerk with comparable performance and lower computation time.

### IV-C Local Control of Higher-Order Dynamics

MINCO-based planners lack direct parameterization of higher-order derivatives at individual knots; these quantities are derived from a globally coupled coefficient system (Sec. I-A). While GCOPTER can add derivative constraints as soft penalties, MIGHTY's Hermite parameterization treats knot positions and velocities as explicit optimization variables. To evaluate this difference, we extend the simple corner-avoidance scenario (Fig. 1) with soft reference tracking terms for position and velocity at the penultimate knot, which is relevant for waypoint velocity specification and hover-at-goal behaviors.

Figure 4: Local control of higher-order dynamics: position and velocity reference tracking. GCOPTER and MIGHTY trajectories are color-mapped by speed. Both planners enforce a velocity reference vref = m/s and position reference at the penultimate knot (one knot before the goal). As shown, MIGHTY achieves better reference tracking accuracy.

We augment the objective function with soft position and velocity reference terms

where $\mathbf{p}_{\text{ref}}$ and $\mathbf{v}_{\text{ref}}$ are desired position and velocity at knot $k$, and $w_{\mathbf{p}_{\text{ref}}}$ and $w_{\mathbf{v}_{\text{ref}}}$ are penalty weights. For this benchmark, we set $k$ to the penultimate knot (one knot before the goal), $\mathbf{v}_{\text{ref}} = {{}{m/s}}$ to enforce near-hover at the goal, and $\mathbf{p}_{\text{ref}}$ to the goal position. We use $w_{\mathbf{p}_{\text{ref}}} = {1\text{×}10^{3}}$ and $w_{\mathbf{v}_{\text{ref}}} = {1\text{×}10^{3}}$, with $v_{\max} = {2.0\ {m/s}}$ and $w_{smooth} = {10^{- 5}}$ for MIGHTY. All other settings match those in Sec. IV-F. We evaluate both GCOPTER and MIGHTY across 100 runs in the same simple corner-avoidance environment. Fig. 4 shows example trajectories from both planners, and Table II summarizes the results.

TABLE II: Local control of higher-order dynamics benchmark. We added position/velocity soft penalties on both GCOPTER and MIGHTY and evaluated performance. Best results are in green.

MIGHTY achieves substantially better tracking: lower position error ($0.0041\ m$ vs. $0.017\ m$), 6.5$\times$ lower velocity error ($0.16\ {m/s}$ vs. $1.0\ {m/s}$), and 25.1% shorter travel time ($14.8\ s$ vs. $19.7\ s$). GCOPTER is faster ($7.4\ {ms}$ vs. $10.6\ {ms}$), though both meet real-time budgets. This demonstrates MIGHTY's advantage: while GCOPTER adds derivative constraints as soft penalties on MINCO-derived velocities, MIGHTY directly optimizes knot positions and velocities as explicit Hermite variables, enabling superior local control of higher-order dynamics.

### IV-D Representation Benchmarking: Complex Case

Figure 5: Complex-scene benchmarking setup. MIGHTY’s trajectory is color-mapped by speed (warm=fast), and GCOPTER’s trajectory is blue. The blue-shaded polygons show the SFC. The start is at (0,0,0.5) m, and 24 goals lie on a grid with x, y ∈ [−15, 15] m and z = 2.5 m.

TABLE III: Complex-scene benchmark across 24 goals and five speed limits (vmax ∈ {1, 2, 3, 4, 5} m/s). GC = GCOPTER, MI = MIGHTY.

We further evaluate MIGHTY in a complex environment (Fig. 5) with start at ${(0,0,0.5)}m$ and 24 goals at ${x,y} \in {{\lbrack{- 15},15\rbrack}m}$ and $z = {2.5m}$. Optimization settings are identical to the simple case for both methods. We report the following metrics: $v_{\max}$ \[m/s\]: Speed limit, $T_{comp}$ \[ms\]: Computation time, $T_{trav}$ \[s\]: Travel time, $L_{path}$ \[m\]: Path length, $\int{{\parallel{\mathbf{j}{(t)}}\parallel}{dt}}$ \[m/s^2^\]: Jerk smoothness integral, and $\rho_{viol}$ \[%\]: Fraction of time violating dynamic bounds.

Overall, Table III shows MIGHTY reduces computation time by 9.3%, travel time by 13.1%, and path length by 1.4%. GCOPTER yields lower jerk, while MIGHTY's higher jerk reflects more aggressive maneuvers, enabled by smaller $w_{smooth} = {10^{- 5}}$ and its larger search space. Both planners keep $\rho_{viol} \leq {1.0\ \%}$.

### IV-E Ablation Study on Scaled and Unscaled Variables

Figure 6: Ablation study comparing MIGHTY with scaled and unscaled variables in the complex benchmarking scenario. The scaled version shows ≈ 2× faster computation time, with lower jerk and slightly shorter path length, while travel time is nearly identical.

As discussed in Sec. III-D, we optimize over scaled variables to improve numerical stability. We evaluate this via ablation using the same complex benchmarking setup. Fig. 6 shows the scaled variant is $\approx 2 \times$ faster with lower jerk, while path length and travel time are nearly identical, confirming that scaling improves efficiency without degrading quality.

### IV-F Benchmarking in Static Environments

Figure 7: (Top) Static obstacle environment used for benchmarking. (Bottom) Top view of the point cloud and path generated by MIGHTY in the static environment. The warmer colors indicate faster speeds.

TABLE IV: Benchmarking results (safety, computation time, performance, and constraint violation). We mark in green the best value in each column considering only configurations with Rsucc = 100%; configurations with Rsucc &lt; 100% are excluded from best highlighting. For EGO-Swarm2, we evaluated both its default sensor, depth camera, and a LiDAR (as used by SUPER and MIGHTY) and report results as “camera” | “LiDAR”. We also tested EGO-Swarm with LiDAR, but its performance was substantially worse, so we omit it from the table for clarity. For SUPER, computation time is reported as “exploratory” &amp; “safe”. The data are shaded red if they have unsuccessful rates Rsucc &lt; 100%.

To thoroughly evaluate MIGHTY, we benchmark it in an obstacle-rich environment (Fig. 7) against EGO-Swarm, EGO-Swarm2, and SUPER. Static cylindrical obstacles are placed randomly with radii sampled in $\lbrack{1.0\ m},{1.5\ m}\rbrack$ and height $6.0\ m$, occupying a ${300\ m} \times {40\ m}$ area. The agent starts at ${}m$ and the goal is ${}m$. We constrain velocity, acceleration, and jerk to $v_{\max} = {4.0\ {m/s}}$, $a_{\max} = {10.0\ {m/s^{2}}}$, and $j_{\max} = {30.0\ {m/s^{3}}}$. For global planning we run A\*, then build an SFC for local optimization. The intermediate waypoints for A\* are projected from the terminal goal onto the local occupancy map centered on the drone. The average computation time for A\* and SFC generation is $0.26\ {ms}$ and $0.48\ {ms}$, respectively.

For soft constraints we use a smooth hinge $\phi_{\mu}{( \cdot )}$. Time integrals are evaluated by trapezoidal quadrature with $\kappa$ samples per segment unless a closed form is available. SFCs are modeled per segment $s$ as the intersection of halfspaces

where $H_{s}$ is the number of halfspaces on segment $s$, and $C_{\text{SFC}} = 0.2$ is a safety margin. The total objective is

where ${J_{\text{SFC}} = {\sum_{s}{\int_{0}^{T_{s}}{\sum_{h = 1}^{H_{s}}{\phi_{\mu}\left( {{{\mathbf{n}_{s,h}^{\top}\mathbf{x}{(t)}} - b_{s,h}} + C_{\text{SFC}}} \right)dt}}}}},$ penalizes leaving the SFC, $J_{v} = {\sum_{s}{\int_{0}^{T_{s}}{\phi_{\mu}{({{\|{\mathbf{v}{(t)}}\|}^{2} - v_{\max}^{2}})}{dt}}}}$, $J_{a} = {\sum_{s}{\int_{0}^{T_{s}}{\phi_{\mu}{({{\|{\mathbf{a}{(t)}}\|}^{2} - a_{\max}^{2}})}{dt}}}}$, and $J_{j} = {\sum_{s}{\int_{0}^{T_{s}}{\phi_{\mu}{({{\|{\mathbf{j}{(t)}}\|}^{2} - j_{\max}^{2}})}{dt}}}}$. Note that the jerk smoothness cost ${\overset{\sim}{J}}_{\text{smooth}}$ uses the closed form given in Eq., which avoids per-sample recomputation. MIGHTY's weights are $w_{T} = {5\text{×}10^{2}}$, $w_{smooth} = {10^{- 1}}$, $w_{\text{SFC}} = {10^{3}}$, $w_{v} = {10^{3}}$, $w_{a} = {10^{3}}$, $w_{j} = {10^{3}}$. We run 10 trials per method. Metrics: $R_{succ}$ \[%\] (success rate; collision-free, reaches goal); $T_{opt}$ \[ms\] (local optimization time); $T_{total}$ \[ms\] (total planning time); $T_{trav}$ \[s\] (travel time); $L_{path}$ \[m\] (path length); $S_{jerk} = {\int{{\parallel{\mathbf{j}{(t)}}\parallel}{dt}}}$ \[m/s^2^\] (smoothness); ${\overline{S}}_{jerk} = \sqrt{\frac{1}{T}{\int{{\parallel{\mathbf{j}{(t)}}\parallel}^{2}{dt}}}}$ \[m/s^3^\] (RMS jerk; time-normalized); $\rho_{vel},\rho_{acc},\rho_{jerk}$ \[%\] (velocity/acceleration/jerk violations). We report ${\overline{S}}_{jerk}$ to account for differing travel times across methods.

Fig. 7 illustrates the environment and one MIGHTY trajectory (in red in the bottom plot), and Table IV gives the full results. We evaluate each method with its default sensor; for methods whose default is not LiDAR (EGO-Swarm, EGO-Swarm2), we also run a LiDAR variant to align with SUPER and MIGHTY (both LiDAR-based). Note that EGO-Swarm with LiDAR performed substantially worse, so Table IV omits those data for clarity. For EGO-Swarm, $v_{\max} = {4.0\ {m/s}}$ yielded a $40\ \%$ success rate; reducing $v_{\max}$ to ${3.0\ {m/s}}\text{~to~}{1.0\ {m/s}}$ improved safety, reaching up to $90\ \%$ at $1.0\ {m/s}$. For EGO-Swarm2, with depth-camera input, it achieves $100\ \%$ success and low compute time at both obstacle weights $w_{\text{obst}} \in {\{{1\text{×}10^{4}},{5\text{×}10^{4}}\}}$. With LiDAR input, the success rates are $20\ \%$ and $70\ \%$ at the same weights. For SUPER, $w_{t} = {10^{4}}$ gave $20\ \%$ success, and reducing $w_{t}$ to $10^{1}$ achieved $100\ \%$. Note that SUPER applies a soft penalty on the distance between the trajectory and points in the overlap of successive SFC segments, with weight $5\text{×}10^{6}$, which is the largest among all cost terms. Summarizing the results, we see that EGO-Swarm2 is the fastest in local optimization and total replanning time ($1.2\ {ms}$ and $1.7\ {ms}$), whereas MIGHTY achieves the shortest travel time ($79.0\ s$) and path length ($310.9\ m$). The jerk of MIGHTY is higher ($S_{jerk} = {522.2\ {m/s^{2}}}$, ${\overline{S}}_{jerk} = {9.4\ {m/s^{3}}}$); however, this is consistent with prior observations of the trade-off between performance and smoothness.

### IV-G Dynamic Environments

Figure 8: Benchmarking scenario with 100 dynamic obstacles following smooth trefoil-knot trajectories. The image shows the agent’s trajectory (color-mapped by speed) navigating through the dynamic obstacles.

Figure 9: Benchmarking scenario with 50 dynamic obstacles and static obstacles. The top left image illustrates the Gazebo simulation environment. The main image and bottom right image show the point cloud (pink-orange) and agent’s trajectory (color-mapped by speed) navigating through both static and dynamic obstacles.

We further evaluate MIGHTY in two dynamic scenarios: only dynamic obstacles, and dynamic & static obstacles. For both, in addition to the cost terms described in Sec. IV-F, we add a dynamic-obstacle avoidance cost ${J_{\text{dyn}} = {\int_{0}^{\sum_{s}T_{s}}{\left( {C_{\text{dyn}}^{2} - {\|{{\mathbf{x}{(t)}} - {\mathbf{k}{(t)}}}\|}^{2}} \right)_{+}^{3}{dt}}}}.$ where $\mathbf{k}{(t)}$ is the position of a dynamic obstacle at time $t$, and ${( \cdot )}_{+} = {\max{(0, \cdot )}}$. We set the weight $w_{\text{dyn}} = {10^{1}}$ and use a soft barrier radius $C_{\text{dyn}} = {3.0\ m}$. Note that $C_{\text{dyn}}$ is where the penalty activates, not a hard safety distance. The robot collision radius is $0.1\ m$. The start and goal are ${}m$ and ${}m$, and, in this more complex environment, the dynamic constraints are set to $v_{\max} = {2.0\ {m/s}}$, $a_{\max} = {5.0\ {m/s^{2}}}$, and $j_{\max} = {30.0\ {m/s^{3}}}$.

Dynamic-only environment: We generate 100 dynamic obstacles following smooth trefoil-knot trajectories, with initial positions $x \in {{\lbrack 0,100\rbrack}m}$, $y \in {{\lbrack{- 10},10\rbrack}m}$, $z \in {{\lbrack 1,6\rbrack}m}$. Fig. 8 shows an example of the environment and the trajectory. MIGHTY avoids all obstacles in 10/10 trials. The minimum nearest-obstacle distance is $0.8\ m$, above the $0.1\ m$ safety threshold.

Dynamic & static environment: We add 50 dynamic obstacles (same motion model) to the static forest as shown in Fig. 9 and run 10 trials. MIGHTY avoids all obstacles in all trials. The minimum is $1.0\ m$, above the $0.1\ m$ collision radius.

## Hardware Experiments

We also evaluated MIGHTY in three hardware experiments: long-duration flights at $v_{\max} \in {{\{ 1,2,3,4\}}{m/s}}$, high-speed flights up to $v_{\max} = {7{m/s}}$, and flights with obstacles introduced during the mission. The perception uses a Livox Mid-360 LiDAR, and localization is provided by DLIO. Planning runs onboard on an Intel^™^ NUC 13, and low-level control uses PX4 on a Pixhawk flight controller. All perception, planning, and control run in real time onboard.

Figure 10: Long-duration experiment with vmax ∈ {1, 2, 3, 4} m/s. Top: action sequence at vmax = 4.0 m/s. Bottom: trajectory histories overlaid on the recorded LiDAR point cloud. Warmer colors indicate higher speed (red: vmax, blue: 0.0 m/s); white points are the onboard point cloud.

Long-Duration Flight Experiment: To assess reliability over extended operations, the vehicle repeatedly traverses a space with multiple obstacles (Fig. 10). Six goal positions are placed opposite the start, inducing repeated out-and-back motions through the environment. For $v_{\max} \in {{\{ 1,2,3,4\}}{m/s}}$, all flights completed without collision.

Figure 11: High-speed experiments at vmax = 5.0, 6.0, 7.0 m/s. Each panel shows the action sequence with trajectory history over the recorded point cloud.

High-Speed Flight Experiment: We further evaluate performance at higher speeds. As shown in Sec. IV, MIGHTY tends to produce higher-jerk trajectories; when constraints are satisfied, these trajectories remain safe while enabling faster motion. We test $v_{\max} = {{5.0\ {m/s}},{6.0\ {m/s}},{7.0\ {m/s}}}$. Fig. 11 shows the resulting histories. All flights completed without collision, demonstrating that the MIGHTY planner and DLIO state estimation operate effectively at high speed. At $v_{\max} = {7.0\ {m/s}}$, the vehicle reached $6.7\ {m/s}$ peak speed.

Figure 12: Dynamic-environment experiment at vmax = 1.0 m/s. The red circle shows the UAV; obstacles are introduced and moved during flight.

Dynamic Obstacle Flight Experiment: To assess robustness to changes in the environment, we introduce and move obstacles during the mission (Fig. 12). We track a person carrying obstacles and incorporate the estimates into the trajectory optimization; see Sec. IV-G for details. The agent successfully reaches the goal without collision over $490\ s$.

## Conclusions

We presented MIGHTY, a Hermite-spline trajectory planner for joint spatiotemporal optimization. By optimizing path geometry and time together with local derivative control, MIGHTY generates smooth, collision-free, and dynamically feasible trajectories for high-performance maneuvers. Benchmarks and hardware tests show MIGHTY outperforms baselines in travel time while satisfying constraints.
