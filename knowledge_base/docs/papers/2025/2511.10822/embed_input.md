<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

MIGHTY: Hermite Spline-based Efficient Trajectory Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Hard-constraint trajectory planners often rely on commercial solvers and demand substantial computational resources. Existing soft-constraint methods achieve faster computation, but either decouple spatial and temporal optimization or restrict the search space. To overcome these limitations, we introduce MIGHTY, a Hermite spline-based planner that performs spatiotemporal optimization while fully leveraging the continuous search space of a spline. In simulation, MIGHTY achieves a 9.3% reduction in computation time and a 13.1% reduction in travel time over state-of-the-art baselines, with a 100% success rate. In hardware, MIGHTY completes multiple high-speed flights up to 6.7 m/s in a cluttered static environment and long-duration flights with dynamically added obstacles.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Trajectory planning for autonomous navigation has been extensively studied with various parameterizations. Hard-constraint approaches explicitly enforce safety but require computationally intensive solvers unsuitable for high-frequency replanning. Soft-constraint planners (EGO-Planner, RAPTOR, SUPER ) achieve faster convergence. Some jointly optimize geometry and timing, while others decouple path and time allocation. Increasing decision variables improves performance but enlarges the problem. Building on these ideas, we introduce MIGHTY, a Hermite spline-based planner.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

endpoint derivs, time
limited polynomial+time space
direct but global

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

B-spline cntrl pts, time
limited polynomial+time space

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

B-spline cntrl pts
limited polynomial+time space

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

B-spline cntrl pts
limited polynomial+time space

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

limited polynomial+time space (MINCO class)

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hermite cntrl pts, time
full polynomial+time space
direct &amp; local

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-A Review of Unconstrained Frameworks", "weight": 1.0} -->

Differential flatness enables efficient optimization of quadrotor trajectories by parameterizing the flat output and their derivatives. Given fixed timestamps at trajectory waypoints, minimum control effort (e.g., jerk/snap) problems using piecewise polynomial representation can be formulated as quadratic programs (QPs), which are convex and can be solved efficiently. However, when segment durations are included as optimization variables (time allocation), the resulting joint problem becomes substantially more complex, yielding a nonlinear program (NLP) that is often ill-conditioned because of the coupling between spatial and temporal variables.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-A Review of Unconstrained Frameworks", "weight": 1.0} -->

Decoupling into two stages enables unconstrained formulations by replacing hard constraints with soft penalties. Richter et al. use 9^th^-order polynomials with endpoint derivatives: a QP minimizes snap, then gradient-based time allocation adjusts duration. Endpoint derivatives are decision variables, so there is direct derivative parameterization. However, the free derivatives are globally coupled, so there is no local control. Collision avoidance inserts mid-segment waypoints, triggering repeated solves. Extensions improve stability and enable real-time replanning via ESDF-based potential costs.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-A Review of Unconstrained Frameworks", "weight": 1.0} -->

Another standard unconstrained framework uses B-splines for trajectory representation, with time-related variables encoded in a knot vector. B-splines offer inherent smoothness and geometric local control: changing one control point affects only a bounded neighborhood of the curve. The convex hull property enables efficient collision checking and enforces dynamic feasibility. However, B-splines do not provide direct local control of higher-order derivatives. Derivatives at any curve point are implicit functions of multiple neighboring control points. One can bound derivatives efficiently via the convex hull property, but cannot independently prescribe a specific velocity or acceleration at a given knot through a single variable. This geometric local control property has been widely exploited for efficient trajectory refinement and replanning in cluttered environments. Zhou et al. parameterize trajectories as non-uniform cubic B-splines initialized from kinodynamic A\* paths. The nonlinear optimization minimizes the cost considering smoothness, a repulsive collision potential from a Euclidean distance field (EDF), and soft penalties on derivative control points exceeding maximum velocity and acceleration. Finally, an iterative time-adjustment method rescales knot spans of the non-uniform spline to guarantee dynamic feasibility.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-A Review of Unconstrained Frameworks", "weight": 1.0} -->

EGO-Planner and RAPTOR simplify the representation by using uniform B-splines with fixed knot spans, leveraging convex hull properties to enforce velocity, acceleration, and jerk constraints directly on control points. EGO-Planner optimizes trajectories via a quasi-Newton solver (L-BFGS) for fast gradient-based convergence, with an additional time-reallocation and anisotropic curve-fitting refinement stage that resizes knot spans and fits a new spline to ensure feasibility and smoothness. RAPTOR also employs a two-stage process: a closed-form QP warm-start for initial smoothness, followed by a nonlinear refinement phase that penalizes collision via an ESDF and ensures dynamic limits via control point constraints.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-A Review of Unconstrained Frameworks", "weight": 1.0} -->

Wang et al. employ diffeomorphism between coefficients and derivatives with linear-complexity gradients. MINCO builds on this: coefficients are analytically determined by waypoints and durations, jointly optimized via linear-complexity solver for minimum jerk/snap. MINCO excels when minimum control effort dominates, but searches only the MINCO class. MINCO's waypoint positions are decision variables, but polynomial coefficients are determined through a banded linear system that couples adjacent segments, so there is no geometric local control. Higher-order derivatives are not decision variables, and they are analytically determined from waypoints and durations, so there is no direct higher-derivative control. Under added objectives, this restriction can yield suboptimal performance compared to more general representations. EGO-Swarm2 and SUPER adopt MINCO; SUPER adds exploratory/backup trajectories for safety.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-A Review of Unconstrained Frameworks", "weight": 1.0} -->

MIGHTY optimizes positions and derivatives at each knot and time durations as explicit variables, enabling local control of waypoints and higher-order dynamics.

<!-- chunk {"id": "body-0016", "role": "body", "section": "I-B MIGHTY Contributions", "weight": 1.0} -->

Table I summarizes the discussion above. Unconstrained higher-order polynomial representations are typically too slow for real-time planning. Uniform or non-uniform splines can generate trajectories faster compared to spatiotemporal joint optimization; however, they can generate sub-optimal trajectories due to decoupled time adjustment. Waypoint-and-duration-based parameterizations are restricted to the low-dimensional subspace induced by the MINCO parameterization, lack direct parameterization of higher-order derivatives at individual knots, and exhibit waypoint propagation where changes to one waypoint affect multiple segments through the globally coupled coefficient system. While these effects enable compact representation and analytical optimality for minimum-control objectives, they can complicate constraint/cost handling beyond minimum-control and limit local control of trajectory shape and higher-order dynamics.

<!-- chunk {"id": "body-0017", "role": "body", "section": "I-B MIGHTY Contributions", "weight": 1.0} -->

To address the limitations of existing soft-constraint planners, MIGHTY uses a Hermite-spline representation and an unconstrained nonlinear optimizer that searches directly over spatial waypoints, endpoint derivatives, and segment durations. A Hermite spline representation guarantees continuity without global coefficient coupling, which fundamentally enables direct local control over both positions and higher-order dynamics at each knot. These properties could be exploited for efficient trajectory refinement (as in B-spline methods ) but are not available in MINCO's globally coupled parameterization.

<!-- chunk {"id": "body-0018", "role": "body", "section": "I-B MIGHTY Contributions", "weight": 1.0} -->

Hermite Spline Planner: Joint spatiotemporal optimization in a single solve, with explicit parameterization of positions and derivatives at each knot. This representation enables local control of higher-order dynamics and trajectory shape, which the optimizer can leverage when needed. The approach, MIGHTY, achieves fast solve times and lower travel time than baselines.

<!-- chunk {"id": "body-0019", "role": "body", "section": "I-B MIGHTY Contributions", "weight": 1.0} -->

Comprehensive Simulation Study: We benchmark in both simple and complex scenes, comparing against state-of-the-art methods in static environments and validating safe behavior in dynamic environments. MIGHTY achieves $9.3\ \%$ reduction in computation time and $13.1\ \%$ reduction in travel time in trajectory representation benchmarking, and it achieves the shortest travel time and path length while maintaining the $100\ \%$ success rate.

<!-- chunk {"id": "body-0020", "role": "body", "section": "I-B MIGHTY Contributions", "weight": 1.0} -->

Extensive Hardware Experiments: Long-duration and high-speed flights, and dynamic obstacle avoidance scenarios using a LiDAR-based perception and localization system. MIGHTY achieves collision-free flights and a top speed of $6.7\ {m/s}$ in high-speed flight experiments.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Hermite Spline", "weight": 1.0} -->

This section introduces the Hermite-spline notation used in MIGHTY's formulation. MIGHTY uses a degree-$d$ Hermite spline with $M$ segments. For odd degree $d = {{2\nu} + 1}$, each segment is parameterized by the knot values of the position and its derivatives up to order $\nu$. For example, a quintic Hermite spline ($d = 5$, $\nu = 2$) specifies position, velocity, and acceleration. Across knots, a Hermite spline automatically guarantees $\mathcal{C}^{\nu}$ continuity by sharing the knot values. Although Hermite splines apply in any dimension, we work in ${\mathbb{R}}^{3}$ for quadrotor planning and use $d = 5$ in this paper.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Decision Variables", "weight": 1.0} -->

To keep the optimization unconstrained while enforcing certain requirements (e.g., $T_{s} > 0$), we apply diffeomorphism, such as $T_{s} = {\phi{(\sigma_{s})}}$ with ${{{\phi{(\sigma)}} = e^{\sigma}},{\sigma_{s} \in {\mathbb{R}}}}.$ We also find that optimizing raw derivative knots $(\mathbf{v}_{i},\mathbf{a}_{i})$ can be numerically unstable. Sec. III-D introduces scalings that improve stability without changing the optimum. For clarity, the formulas below are written in terms of the original variables $(\mathbf{p}_{s},\mathbf{v}_{s},\mathbf{a}_{s},T_{s})$; applying a diffeomorphism only inserts chain-rule factors in the gradients.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Representations", "weight": 1.0} -->

Given the quintic Hermite segment in Eq., a smooth cost can be expressed in terms of the raw Hermite variables $(\mathbf{p}_{s},\mathbf{v}_{s},\mathbf{a}_{s},\mathbf{p}_{s + 1},\mathbf{v}_{s + 1},\mathbf{a}_{s + 1},T_{s})$. However, evaluating costs and gradients directly in Hermite form can be computationally expensive, and other representations, such as Bézier curve, can be more efficient.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Representations", "weight": 1.0} -->

For instance, a Bézier curve allows efficient evaluation of the trajectory and its derivatives at arbitrary sample points. A degree-$n$ Bézier segment is written as ${{{\mathbf{x}{(u)}} = {\sum_{i = 0}^{n}{B_{i}^{n}{(u)}\mathbf{c}_{i}}}},{u \in {\lbrack 0,1\rbrack}}},$ where the vectors $\mathbf{c}_{i}$ are the Bézier control points, and the Bernstein basis polynomials are ${{{B_{i}^{n}{(u)}} = {\binom{n}{i}u^{i}{({1 - u})}^{n - i}}},{i = {0,\ldots,n}}}.$ Because evaluation is just a weighted sum of control points with weights $B_{i}^{n}{(u)}$, sampling reduces to a few dot products with small, reusable tables.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Representations", "weight": 1.0} -->

Then each sample is a small dot product: positions use the $B_{i}^{5}$ table, and derivatives use the degree-reduced Bernstein weights. Since these tables are tiny and shared across iterations, and each dot product has only $6,5,4,3$ terms (for degree $5$ down to $2$), this is faster and numerically steadier than recomputing higher-order Hermite polynomials and their derivatives at every sample.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Representations", "weight": 1.0} -->

Although Bézier representation has these computational advantages, note that Bézier control points do not enforce cross-segment continuity by themselves. On the other hand, Hermite variables guarantee $\mathcal{C}^{k}$ continuity across segments by construction. Therefore, it is often advantageous to optimize in the Hermite parameterization while evaluating cost terms in the Bézier basis to exploit its computational benefits. In our simulations and hardware experiments, we optimize over Hermite and evaluate costs in Bézier; however, in general, MIGHTY does not require Bézier for cost evaluation.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Objective and Closed-Form Gradient", "weight": 1.0} -->

To make the formulation basis-independent, we express the objective and its gradients w.r.t. a generic control-point (or coefficient) vector $\mathbf{c}$, independent of the chosen parameterization (Hermite end states, Bézier control points, etc.). As a concrete example, the affine map between Hermite and Bézier on segment $s$ is

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-C Objective and Closed-Form Gradient", "weight": 1.0} -->

Note that the explicit time derivative $\left. {\partial{J_{s}/{\partial T_{s}}}} \right|_{\text{explicit}}$ comes from factors like $T_{s}^{5}$ in smoothness integrals. Using Eq., the entries of $C{(T_{s})}$ are simple constants, so Eq.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Objective and Closed-Form Gradient", "weight": 1.0} -->

The coefficient gradient $\partial{\mathbf{c}_{s}/{\partial T_{s}}}$ ($= {\nabla_{T_{s}}\mathbf{c}_{s}}$) used in the coefficient path in Eq. can be computed in closed form as

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C Objective and Closed-Form Gradient", "weight": 1.0} -->

Therefore, to obtain the gradient, we need to compute $\mathbf{g}_{\mathbf{c}_{s}}$ and $\left. {\partial{J_{s}/{\partial T_{s}}}} \right|_{\text{explicit}}.$ Here we present two types of cost terms: cost terms defined on control points, and cost terms defined via sampled states along the trajectory, and their gradients used in Sec. IV.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-C1 Cost on Control Points", "weight": 1.0} -->

We first consider cost terms that are expressed directly in terms of the coefficients/control points, such as integrated squared jerk. For a quintic Bézier segment $s$ with control points ${\mathbf{c}_{s,0},\ldots,\mathbf{c}_{s,5}} \in {\mathbb{R}}^{3}$, obtained from the Hermite endpoint states via Eq., the third forward differences are: ${{\Delta_{s,m} = {{{\mathbf{c}_{s,{m + 3}} - {3\mathbf{c}_{s,{m + 2}}}} + {3\mathbf{c}_{s,{m + 1}}}} - \mathbf{c}_{s,m}}},{m \in {\{ 0,1,2\}}}}.$ Then, the integrated squared jerk on segment $s$ is

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-C1 Cost on Control Points", "weight": 1.0} -->

Using Eqs. and, we derive the second term of Eq. and obtain a closed-form expression.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-C2 Cost on Sampled States", "weight": 1.0} -->

where we omit the argument of the Bernstein basis polynomials $B{(\tau_{s,j})}$ for clarity. Note that ${B_{r}^{n}{( \cdot )}} = 0$ if $r \notin {\{ 0,\ldots,n\}}$. Stacking over $k = {0,\ldots,5}$ gives $\mathbf{g}_{\mathbf{c}_{s}} = {\partial{J_{\text{samp},s}/{\partial\mathbf{c}_{s}}}}$, which is then pulled back (chain rule) and accumulated into the Hermite variables via Eq..

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-C2 Cost on Sampled States", "weight": 1.0} -->

Changing $T_{s}$ affects the sampled cost in two ways. First, (a) state-scaling: Even if we hold the Bézier control points fixed (i.e., keep the curve in normalized time $\tau$ unchanged), rescaling $T_{s}$ changes the physical derivatives via $t = {t_{s} + {\tau_{s}T_{s}}}$. Second, (b) coefficients: In Hermite parameterizations the control points themselves depend on $T_{s}$ via the Hermite$\rightarrow$Bézier map. The two items below compute the partial derivative $\partial{J_{\text{samp},s}/{\partial T_{s}}}$ for both contributions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-D Reparameterizations for Derivative Variables", "weight": 1.0} -->

Each segment with duration $T_{s}$ is parameterized by normalized time $\tau_{s} \in {\lbrack 0,1\rbrack}$; by the chain rule,

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-D Reparameterizations for Derivative Variables", "weight": 1.0} -->

Optimizing raw knot derivatives $\{\mathbf{v}_{i},\mathbf{a}_{i}\}$ together with $\{ T_{s}\}$ introduces explicit $1/T_{s}$ and $1/T_{s}^{2}$ factors in the gradients, so short segments have larger influence. We therefore optimize scaled knot derivatives. Define an averaged local time as

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-D Reparameterizations for Derivative Variables", "weight": 1.0} -->

At the endpoints, the scaling uses the adjacent segment duration (no averaging), while at interior knots we use the local average duration to balance the influence of the two neighboring segments; in that case, the inverse-duration effects are mitigated but cannot be canceled for both segments simultaneously unless their durations match. Our ablation study in Sec. IV-E confirms the expected improvement in performance.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

All simulations were run on an AlienWare Aurora R8 with an Intel^®^ Core^TM^ i9-9900K CPU and 64 GB RAM, using Ubuntu 22.04 LTS and ROS 2 Humble.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-A Representation Benchmarking: Simple Case", "weight": 1.0} -->

We first benchmark MIGHTY against GCOPTER (which uses MINCO ) on a simple corner-avoidance task with fixed start and goal (Fig. 1). For a fair comparison, we implement GCOPTER's optimization cost in MIGHTY and use the same optimizer (L-BFGS ) and stopping tolerances. Both methods start from the same initial guess.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-A Representation Benchmarking: Simple Case", "weight": 1.0} -->

GCOPTER represents each segment as a fifth-order polynomial, so MINCO minimizes jerk (third-order effort) by construction. MIGHTY uses a fifth-order Hermite spline to match the polynomial degree. GCOPTER applies diffeomorphic parameterizations for waypoints and durations (waypoints remain inside the overlap of safe flight corridors (SFCs); durations stay positive). The only difference is that MIGHTY includes an explicit jerk smoothness term (Sec. III-C1), while GCOPTER does not add a separate smoothness cost because MINCO already minimizes jerk.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A Representation Benchmarking: Simple Case", "weight": 1.0} -->

We use $w_{T} = {10^{2}}$ because $w_{T} = {10^{3}}$ caused occasional constraint violations ($> {1\%}$) in GCOPTER. For MIGHTY, we set the jerk smoothness weight to $w_{smooth} = {10^{- 5}}$. GCOPTER sets yaw to the direction of motion, so yaw and yaw rate are determined by $\mathbf{p}$. Accordingly, although neither GCOPTER nor MIGHTY optimizes yaw directly, both penalize tilt angle and angular velocity. We configure MIGHTY this way solely for fair comparison with GCOPTER. Outside this benchmark (see Sec. IV-F), MIGHTY can use a different cost design.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A Representation Benchmarking: Simple Case", "weight": 1.0} -->

The result in Fig. 2 shows that MIGHTY achieves a shorter travel time, with slightly faster computation and shorter path than GCOPTER. While GCOPTER produces smoother trajectories with lower jerk due to its constraint within the MINCO class, MIGHTY explores a larger search space to identify faster and more effective trajectories. This flexibility enables MIGHTY to achieve superior performance, and Sec. IV-B further investigates the jerk-performance trade-off.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B Smooth Weight Sweep Benchmarking", "weight": 1.0} -->

Fig. 2 shows MIGHTY yields higher jerk than GCOPTER while achieving better travel time. To quantify this trade-off, we sweep $w_{smooth} \in {\{{10^{- 5}},\ldots,{10^{3}}\}}$ in the same scenario. Fig. 3 shows that as $w_{smooth}$ increases, MIGHTY progressively reduces jerk, eventually surpassing GCOPTER's levels of smoothness. At $w_{smooth} = {10^{2}}$, MIGHTY matches GCOPTER's jerk while maintaining better performance and lower computation time, demonstrating that MIGHTY's higher jerk is a tunable design choice rather than an inherent limitation.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Local Control of Higher-Order Dynamics", "weight": 1.0} -->

MINCO-based planners lack direct parameterization of higher-order derivatives at individual knots; these quantities are derived from a globally coupled coefficient system (Sec. I-A). While GCOPTER can add derivative constraints as soft penalties, MIGHTY's Hermite parameterization treats knot positions and velocities as explicit optimization variables. To evaluate this difference, we extend the simple corner-avoidance scenario (Fig. 1) with soft reference tracking terms for position and velocity at the penultimate knot, which is relevant for waypoint velocity specification and hover-at-goal behaviors.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C Local Control of Higher-Order Dynamics", "weight": 1.0} -->

We augment the objective function with soft position and velocity reference terms

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-C Local Control of Higher-Order Dynamics", "weight": 1.0} -->

We use $w_{\mathbf{p}_{\text{ref}}} = {1\text{×}10^{3}}$ and $w_{\mathbf{v}_{\text{ref}}} = {1\text{×}10^{3}}$, with $v_{\max} = {2.0\ {m/s}}$ and $w_{smooth} = {10^{- 5}}$ for MIGHTY. All other settings match those in Sec. IV-F. We evaluate both GCOPTER and MIGHTY across 100 runs in the same simple corner-avoidance environment. Fig. 4 shows example trajectories from both planners, and Table II summarizes the results.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-C Local Control of Higher-Order Dynamics", "weight": 1.0} -->

MIGHTY achieves substantially better tracking: lower position error ($0.0041\ m$ vs. $0.017\ m$), 6.5$\times$ lower velocity error ($0.16\ {m/s}$ vs. $1.0\ {m/s}$), and 25.1% shorter travel time ($14.8\ s$ vs. $19.7\ s$). GCOPTER is faster ($7.4\ {ms}$ vs. $10.6\ {ms}$), though both meet real-time budgets. This demonstrates MIGHTY's advantage: while GCOPTER adds derivative constraints as soft penalties on MINCO-derived velocities, MIGHTY directly optimizes knot positions and velocities as explicit Hermite variables, enabling superior local control of higher-order dynamics.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-D Representation Benchmarking: Complex Case", "weight": 1.0} -->

We further evaluate MIGHTY in a complex environment (Fig. 5) with start at ${(0,0,0.5)}m$ and 24 goals at ${x,y} \in {{\lbrack{- 15},15\rbrack}m}$ and $z = {2.5m}$. Optimization settings are identical to the simple case for both methods. We report the following metrics: $v_{\max}$ \[m/s\]: Speed limit, $T_{comp}$ \[ms\]: Computation time, $T_{trav}$ \[s\]: Travel time, $L_{path}$ \[m\]: Path length, $\int{{\parallel{\mathbf{j}{(t)}}\parallel}{dt}}$ \[m/s^2^\]: Jerk smoothness integral, and $\rho_{viol}$ \[%\]: Fraction of time violating dynamic bounds.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-D Representation Benchmarking: Complex Case", "weight": 1.0} -->

Overall, Table III shows MIGHTY reduces computation time by 9.3%, travel time by 13.1%, and path length by 1.4%. GCOPTER yields lower jerk, while MIGHTY's higher jerk reflects more aggressive maneuvers, enabled by smaller $w_{smooth} = {10^{- 5}}$ and its larger search space. Both planners keep $\rho_{viol} \leq {1.0\ \%}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-E Ablation Study on Scaled and Unscaled Variables", "weight": 1.0} -->

As discussed in Sec. III-D, we optimize over scaled variables to improve numerical stability. We evaluate this via ablation using the same complex benchmarking setup. Fig. 6 shows the scaled variant is $\approx 2 \times$ faster with lower jerk, while path length and travel time are nearly identical, confirming that scaling improves efficiency without degrading quality.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-F Benchmarking in Static Environments", "weight": 1.0} -->

To thoroughly evaluate MIGHTY, we benchmark it in an obstacle-rich environment (Fig. 7) against EGO-Swarm, EGO-Swarm2, and SUPER. Static cylindrical obstacles are placed randomly with radii sampled in $\lbrack{1.0\ m},{1.5\ m}\rbrack$ and height $6.0\ m$, occupying a ${300\ m} \times {40\ m}$ area. The agent starts at ${}m$ and the goal is ${}m$. We constrain velocity, acceleration, and jerk to $v_{\max} = {4.0\ {m/s}}$, $a_{\max} = {10.0\ {m/s^{2}}}$, and $j_{\max} = {30.0\ {m/s^{3}}}$. For global planning we run A\*, then build an SFC for local optimization. The intermediate waypoints for A\* are projected from the terminal goal onto the local occupancy map centered on the drone.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-F Benchmarking in Static Environments", "weight": 1.0} -->

The average computation time for A\* and SFC generation is $0.26\ {ms}$ and $0.48\ {ms}$, respectively.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-F Benchmarking in Static Environments", "weight": 1.0} -->

For soft constraints we use a smooth hinge $\phi_{\mu}{( \cdot )}$. Time integrals are evaluated by trapezoidal quadrature with $\kappa$ samples per segment unless a closed form is available. SFCs are modeled per segment $s$ as the intersection of halfspaces

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-F Benchmarking in Static Environments", "weight": 1.0} -->

where $H_{s}$ is the number of halfspaces on segment $s$, and $C_{\text{SFC}} = 0.2$ is a safety margin. The total objective is

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-F Benchmarking in Static Environments", "weight": 1.0} -->

Fig. 7 illustrates the environment and one MIGHTY trajectory (in red in the bottom plot), and Table IV gives the full results. We evaluate each method with its default sensor; for methods whose default is not LiDAR (EGO-Swarm, EGO-Swarm2), we also run a LiDAR variant to align with SUPER and MIGHTY (both LiDAR-based). Note that EGO-Swarm with LiDAR performed substantially worse, so Table IV omits those data for clarity. For EGO-Swarm, $v_{\max} = {4.0\ {m/s}}$ yielded a $40\ \%$ success rate; reducing $v_{\max}$ to ${3.0\ {m/s}}\text{~to~}{1.0\ {m/s}}$ improved safety, reaching up to $90\ \%$ at $1.0\ {m/s}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-F Benchmarking in Static Environments", "weight": 1.0} -->

For EGO-Swarm2, with depth-camera input, it achieves $100\ \%$ success and low compute time at both obstacle weights $w_{\text{obst}} \in {\{{1\text{×}10^{4}},{5\text{×}10^{4}}\}}$. With LiDAR input, the success rates are $20\ \%$ and $70\ \%$ at the same weights. For SUPER, $w_{t} = {10^{4}}$ gave $20\ \%$ success, and reducing $w_{t}$ to $10^{1}$ achieved $100\ \%$. Note that SUPER applies a soft penalty on the distance between the trajectory and points in the overlap of successive SFC segments, with weight $5\text{×}10^{6}$, which is the largest among all cost terms.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-F Benchmarking in Static Environments", "weight": 1.0} -->

Summarizing the results, we see that EGO-Swarm2 is the fastest in local optimization and total replanning time ($1.2\ {ms}$ and $1.7\ {ms}$), whereas MIGHTY achieves the shortest travel time ($79.0\ s$) and path length ($310.9\ m$). The jerk of MIGHTY is higher ($S_{jerk} = {522.2\ {m/s^{2}}}$, ${\overline{S}}_{jerk} = {9.4\ {m/s^{3}}}$); however, this is consistent with prior observations of the trade-off between performance and smoothness.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-G Dynamic Environments", "weight": 1.0} -->

Dynamic-only environment: We generate 100 dynamic obstacles following smooth trefoil-knot trajectories, with initial positions $x \in {{\lbrack 0,100\rbrack}m}$, $y \in {{\lbrack{- 10},10\rbrack}m}$, $z \in {{\lbrack 1,6\rbrack}m}$. Fig. 8 shows an example of the environment and the trajectory. MIGHTY avoids all obstacles in 10/10 trials. The minimum nearest-obstacle distance is $0.8\ m$, above the $0.1\ m$ safety threshold.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-G Dynamic Environments", "weight": 1.0} -->

Dynamic & static environment: We add 50 dynamic obstacles (same motion model) to the static forest as shown in Fig. 9 and run 10 trials. MIGHTY avoids all obstacles in all trials. The minimum is $1.0\ m$, above the $0.1\ m$ collision radius.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Hardware Experiments", "weight": 1.0} -->

We also evaluated MIGHTY in three hardware experiments: long-duration flights at $v_{\max} \in {{\{ 1,2,3,4\}}{m/s}}$, high-speed flights up to $v_{\max} = {7{m/s}}$, and flights with obstacles introduced during the mission. The perception uses a Livox Mid-360 LiDAR, and localization is provided by DLIO. Planning runs onboard on an Intel^™^ NUC 13, and low-level control uses PX4 on a Pixhawk flight controller. All perception, planning, and control run in real time onboard.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Hardware Experiments", "weight": 1.0} -->

Long-Duration Flight Experiment: To assess reliability over extended operations, the vehicle repeatedly traverses a space with multiple obstacles (Fig. 10). Six goal positions are placed opposite the start, inducing repeated out-and-back motions through the environment. For $v_{\max} \in {{\{ 1,2,3,4\}}{m/s}}$, all flights completed without collision.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Hardware Experiments", "weight": 1.0} -->

High-Speed Flight Experiment: We further evaluate performance at higher speeds. As shown in Sec. IV, MIGHTY tends to produce higher-jerk trajectories; when constraints are satisfied, these trajectories remain safe while enabling faster motion. We test $v_{\max} = {{5.0\ {m/s}},{6.0\ {m/s}},{7.0\ {m/s}}}$. Fig. 11 shows the resulting histories. All flights completed without collision, demonstrating that the MIGHTY planner and DLIO state estimation operate effectively at high speed. At $v_{\max} = {7.0\ {m/s}}$, the vehicle reached $6.7\ {m/s}$ peak speed.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Hardware Experiments", "weight": 1.0} -->

Dynamic Obstacle Flight Experiment: To assess robustness to changes in the environment, we introduce and move obstacles during the mission (Fig. 12). We track a person carrying obstacles and incorporate the estimates into the trajectory optimization; see Sec. IV-G for details. The agent successfully reaches the goal without collision over $490\ s$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We presented MIGHTY, a Hermite-spline trajectory planner for joint spatiotemporal optimization. By optimizing path geometry and time together with local derivative control, MIGHTY generates smooth, collision-free, and dynamically feasible trajectories for high-performance maneuvers. Benchmarks and hardware tests show MIGHTY outperforms baselines in travel time while satisfying constraints.
