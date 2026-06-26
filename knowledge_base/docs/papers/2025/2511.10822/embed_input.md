<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

MIGHTY: Hermite Spline-based Efficient Trajectory Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Hard-constraint trajectory planners often rely on commercial solvers and demand substantial computational resources. Existing soft-constraint methods achieve faster computation, but either decouple spatial and temporal optimization or restrict the search space. To overcome these limitations, we introduce MIGHTY, a Hermite spline-based planner that performs spatiotemporal optimization while fully leveraging the continuous search space of a spline. In simulation, MIGHTY achieves a 9.3% reduction in computation time and a 13.1% reduction in travel time over state-of-the-art baselines, with a 100% success rate. In hardware, MIGHTY completes multiple high-speed flights up to 6.7 m/s in a cluttered static environment and long-duration flights with dynamically added obstacles.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Trajectory planning for autonomous navigation has been extensively studied with various parameterizations. Hard-constraint approaches explicitly enforce safety but require computationally intensive solvers unsuitable for high-frequency replanning. Soft-constraint planners (EGO-Planner, RAPTOR, SUPER) achieve faster convergence. Some jointly optimize geometry and timing, while others decouple path and time allocation. Increasing decision variables improves performance but enlarges the problem. Building on these ideas, we introduce MIGHTY, a Hermite spline-based planner. endpoint derivs, time limited polynomial+time space direct but global B-spline cntrl pts, time limited polynomial+time space B-spline cntrl pts limited polynomial+time space B-spline cntrl pts limited polynomial+time space limited polynomial+time space (MINCO class) Hermite cntrl pts, time full polynomial+time space TABLE I: State-of-the-art Unconstrained UAV Trajectory Planners

<!-- chunk {"id": "body-0004", "role": "body", "section": "I-A Review of Unconstrained Frameworks", "weight": 1.0} -->

Differential flatness enables efficient optimization of quadrotor trajectories by parameterizing the flat output and their derivatives. Given fixed timestamps at trajectory waypoints, minimum control effort (e.g., jerk/snap) problems using piecewise polynomial representation can be formulated as quadratic programs (QPs), which are convex and can be solved efficiently. However, when segment durations are included as optimization variables (time allocation), the resulting joint problem becomes substantially more complex, yielding a nonlinear program (NLP) that is often ill-conditioned because of the coupling between spatial and temporal variables.

<!-- chunk {"id": "body-0005", "role": "body", "section": "I-A Review of Unconstrained Frameworks", "weight": 1.0} -->

Decoupling into two stages enables unconstrained formulations by replacing hard constraints with soft penalties. Richter et al. use 9^th^-order polynomials with endpoint derivatives: a QP minimizes snap, then gradient-based time allocation adjusts duration. Endpoint derivatives are decision variables, so there is direct derivative parameterization. However, the free derivatives are globally coupled, so there is no local control. Collision avoidance inserts mid-segment waypoints, triggering repeated solves. Extensions improve stability and enable real-time replanning via ESDF-based potential costs.

<!-- chunk {"id": "body-0006", "role": "body", "section": "I-A Review of Unconstrained Frameworks", "weight": 1.0} -->

Another standard unconstrained framework uses B-splines for trajectory representation, with time-related variables encoded in a knot vector. B-splines offer inherent smoothness and geometric local control: changing one control point affects only a bounded neighborhood of the curve. The convex hull property enables efficient collision checking and enforces dynamic feasibility. However, B-splines do not provide direct local control of higher-order derivatives. Derivatives at any curve point are implicit functions of multiple neighboring control points. One can bound derivatives efficiently via the convex hull property, but cannot independently prescribe a specific velocity or acceleration at a given knot through a single variable. This geometric local control property has been widely exploited for efficient trajectory refinement and replanning in cluttered environments. Zhou et al. parameterize trajectories as non-uniform cubic B-splines initialized from kinodynamic A\* paths. The nonlinear optimization minimizes the cost considering smoothness, a repulsive collision potential from a Euclidean distance field (EDF), and soft penalties on derivative control points exceeding maximum velocity and acceleration. Finally, an iterative time-adjustment method rescales knot spans of the non-uniform spline to guarantee dynamic feasibility.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A Review of Unconstrained Frameworks", "weight": 1.0} -->

EGO-Planner and RAPTOR simplify the representation by using uniform B-splines with fixed knot spans, leveraging convex hull properties to enforce velocity, acceleration, and jerk constraints directly on control points. EGO-Planner optimizes trajectories via a quasi-Newton solver (L-BFGS) for fast gradient-based convergence, with an additional time-reallocation and anisotropic curve-fitting refinement stage that resizes knot spans and fits a new spline to ensure feasibility and smoothness. RAPTOR also employs a two-stage process: a closed-form QP warm-start for initial smoothness, followed by a nonlinear refinement phase that penalizes collision via an ESDF and ensures dynamic limits via control point constraints.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Review of Unconstrained Frameworks", "weight": 1.0} -->

Wang et al. employ diffeomorphism between coefficients and derivatives with linear-complexity gradients. MINCO builds on this: coefficients are analytically determined by waypoints and durations, jointly optimized via linear-complexity solver for minimum jerk/snap. MINCO excels when minimum control effort dominates, but searches only the MINCO class. MINCO's waypoint positions are decision variables, but polynomial coefficients are determined through a banded linear system that couples adjacent segments, so there is no geometric local control. Higher-order derivatives are not decision variables, and they are analytically determined from waypoints and durations, so there is no direct higher-derivative control. Under added objectives, this restriction can yield suboptimal performance compared to more general representations. EGO-Swarm2 and SUPER adopt MINCO; SUPER adds exploratory/backup trajectories for safety.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A Review of Unconstrained Frameworks", "weight": 1.0} -->

MIGHTY optimizes positions and derivatives at each knot and time durations as explicit variables, enabling local control of waypoints and higher-order dynamics.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-B MIGHTY Contributions", "weight": 1.0} -->

Table I summarizes the discussion above. Unconstrained higher-order polynomial representations are typically too slow for real-time planning. Uniform or non-uniform splines can generate trajectories faster compared to spatiotemporal joint optimization; however, they can generate sub-optimal trajectories due to decoupled time adjustment. Waypoint-and-duration-based parameterizations are restricted to the low-dimensional subspace induced by the MINCO parameterization, lack direct parameterization of higher-order derivatives at individual knots, and exhibit waypoint propagation where changes to one waypoint affect multiple segments through the globally coupled coefficient system. While these effects enable compact representation and analytical optimality for minimum-control objectives, they can complicate constraint/cost handling beyond minimum-control and limit local control of trajectory shape and higher-order dynamics.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-B MIGHTY Contributions", "weight": 1.0} -->

To address the limitations of existing soft-constraint planners, MIGHTY uses a Hermite-spline representation and an unconstrained nonlinear optimizer that searches directly over spatial waypoints, endpoint derivatives, and segment durations. A Hermite spline representation guarantees continuity without global coefficient coupling, which fundamentally enables direct local control over both positions and higher-order dynamics at each knot. These properties could be exploited for efficient trajectory refinement (as in B-spline methods) but are not available in MINCO's globally coupled parameterization. The key contributions of the paper are: Hermite Spline Planner: Joint spatiotemporal optimization in a single solve, with explicit parameterization of positions and derivatives at each knot. This representation enables local control of higher-order dynamics and trajectory shape, which the optimizer can leverage when needed. The approach, MIGHTY, achieves fast solve times and lower travel time than baselines.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-B MIGHTY Contributions", "weight": 1.0} -->

Comprehensive Simulation Study: We benchmark in both simple and complex scenes, comparing against state-of-the-art methods in static environments and validating safe behavior in dynamic environments. MIGHTY achieves $9.3\text{\,}\%$ reduction in computation time and $13.1\text{\,}\%$ reduction in travel time in trajectory representation benchmarking, and it achieves the shortest travel time and path length while maintaining the $100\text{\,}\%$ success rate.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-B MIGHTY Contributions", "weight": 1.0} -->

Extensive Hardware Experiments: Long-duration and high-speed flights, and dynamic obstacle avoidance scenarios using a LiDAR-based perception and localization system. MIGHTY achieves collision-free flights and a top speed of $6.7\text{\,}\mathrm{m}\mathrm{/}\mathrm{s}$ in high-speed flight experiments.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Hermite Spline", "weight": 1.0} -->

This section introduces the Hermite-spline notation used in MIGHTY's formulation. MIGHTY uses a degree-$d$ Hermite spline with $M$ segments. For odd degree $d=2\nu+1$, each segment is parameterized by the knot values of the position and its derivatives up to order $\nu$. For example, a quintic Hermite spline ($d=5$, $\nu=2$) specifies position, velocity, and acceleration. Across knots, a Hermite spline automatically guarantees $\mathcal{C}^{\nu}$ continuity by sharing the knot values. Although Hermite splines apply in any dimension, we work in $\mathbb{R}^{3}$ for quadrotor planning and use $d=5$ in this paper.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Hermite Spline", "weight": 1.0} -->

The $\mathbf{p}_{i},\mathbf{v}_{i},\mathbf{a}_{i}\in\mathbb{R}^{3}\;(i=0,\dots,M)$ and $T_{s}>0\;(s=0,\dots,M-1)$ are the interior knot positions, velocities, accelerations, and segment durations, respectively.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Decision Variables", "weight": 1.0} -->

As shown in Sec. II, the knot states $\mathbf{p}_{i},\mathbf{v}_{i},\mathbf{a}_{i}(i=0,\dots,M)$ and segment durations $T_{s}(s=0,\dots,M-1)$ fully determine the trajectory. Thus we optimize the interior positions, velocities, accelerations, and per-segment durations: with fixed boundary states $(\mathbf{p}_{0},\mathbf{v}_{0},\mathbf{a}_{0})$ and $(\mathbf{p}_{M},\mathbf{v}_{M},\mathbf{a}_{M})$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Decision Variables", "weight": 1.0} -->

To keep the optimization unconstrained while enforcing certain requirements (e.g., $T_{s}>0$), we apply diffeomorphism, such as $T_{s}\;=\;\phi(\sigma_{s})$ with $\phi(\sigma)=e^{\sigma},\ \sigma_{s}\in\mathbb{R}.$ We also find that optimizing raw derivative knots $(\mathbf{v}_{i},\mathbf{a}_{i})$ can be numerically unstable. Sec. III-D introduces scalings that improve stability without changing the optimum. For clarity, the formulas below are written in terms of the original variables $(\mathbf{p}_{s},\mathbf{v}_{s},\mathbf{a}_{s},T_{s})$; applying a diffeomorphism only inserts chain-rule factors in the gradients.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Representations", "weight": 1.0} -->

Given the quintic Hermite segment in Eq., a smooth cost can be expressed in terms of the raw Hermite variables $(\mathbf{p}_{s},\mathbf{v}_{s},\mathbf{a}_{s},\mathbf{p}_{s+1},\mathbf{v}_{s+1},\mathbf{a}_{s+1},T_{s})$. However, evaluating costs and gradients directly in Hermite form can be computationally expensive, and other representations, such as Bézier curve, can be more efficient.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Representations", "weight": 1.0} -->

For instance, a Bézier curve allows efficient evaluation of the trajectory and its derivatives at arbitrary sample points. A degree-$n$ Bézier segment is written as $\mathbf{x}(u)=\sum_{i=0}^{n}B_{i}^{n}(u)\,\mathbf{c}_{i},u\,$ where the vectors $\mathbf{c}_{i}$ are the Bézier control points, and the Bernstein basis polynomials are $B_{i}^{n}(u)\;=\;\binom{n}{i}\,u^{\,i}\,(1-u)^{\,n-i},i=0,\dots,n.$ Because evaluation is just a weighted sum of control points with weights $B_{i}^{n}(u)$, sampling reduces to a few dot products with small, reusable tables. Then each sample is a small dot product: positions use the $B_{i}^{5}$ table, and derivatives use the degree-reduced Bernstein weights.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Representations", "weight": 1.0} -->

Since these tables are tiny and shared across iterations, and each dot product has only $6,5,4,3$ terms (for degree $5$ down to $2$), this is faster and numerically steadier than recomputing higher-order Hermite polynomials and their derivatives at every sample.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Representations", "weight": 1.0} -->

Although Bézier representation has these computational advantages, note that Bézier control points do not enforce cross-segment continuity by themselves. On the other hand, Hermite variables guarantee $\mathcal{C}^{k}$ continuity across segments by construction. Therefore, it is often advantageous to optimize in the Hermite parameterization while evaluating cost terms in the Bézier basis to exploit its computational benefits. In our simulations and hardware experiments, we optimize over Hermite and evaluate costs in Bézier; however, in general, MIGHTY does not require Bézier for cost evaluation.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-C1 Cost on Control Points", "weight": 1.0} -->

Since $C_{s}=3600\,T_{s}^{-5}$, the first contribution is Using Eqs. and, we derive the second term of Eq. and obtain a closed-form expression.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C2 Cost on Sampled States", "weight": 1.0} -->

^11^1If an explicit time term is desired, then $\ell=\ell(\mathbf{x},\mathbf{v},\mathbf{a},\mathbf{j};T_{s})$ and an extra $\partial\ell/\partial T_{s}$ term would be added when differentiating w.r.t. $T_{s}$. Then, holding $T_{s}$ fixed, the gradient w.r.t. the $k$th control point is where we omit the argument of the Bernstein basis polynomials $B(\tau_{s,j})$ for clarity. Note that $B_{r}^{n}(\cdot)=0$ if $r\notin\{0,\dots,n\}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C2 Cost on Sampled States", "weight": 1.0} -->

Stacking over $k=0,\ldots,5$ gives $\mathbf{g}_{\mathbf{c}_{s}}=\partial J_{\text{samp},s}/\partial\mathbf{c}_{s}$, which is then pulled back (chain rule) and accumulated into the Hermite variables via Eq..

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C2 Cost on Sampled States", "weight": 1.0} -->

Changing $T_{s}$ affects the sampled cost in two ways. First, (a) state-scaling: Even if we hold the Bézier control points fixed (i.e., keep the curve in normalized time $\tau$ unchanged), rescaling $T_{s}$ changes the physical derivatives via $t=t_{s}+\tau_{s}\,T_{s}$. Second, (b) coefficients: In Hermite parameterizations the control points themselves depend on $T_{s}$ via the Hermite$\to$Bézier map. The two items below compute the partial derivative $\partial J_{\text{samp},s}/\partial T_{s}$ for both contributions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-D Reparameterizations for Derivative Variables", "weight": 1.0} -->

Each segment with duration $T_{s}$ is parameterized by normalized time $\tau_{s}\in$; by the chain rule, Optimizing raw knot derivatives $\{\mathbf{v}_{i},\mathbf{a}_{i}\}$ together with $\{T_{s}\}$ introduces explicit $1/T_{s}$ and $1/T_{s}^{2}$ factors in the gradients, so short segments have larger influence. We therefore optimize scaled knot derivatives.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-D Reparameterizations for Derivative Variables", "weight": 1.0} -->

At the endpoints, the scaling uses the adjacent segment duration (no averaging), while at interior knots we use the local average duration to balance the influence of the two neighboring segments; in that case, the inverse-duration effects are mitigated but cannot be canceled for both segments simultaneously unless their durations match. Our ablation study in Sec. IV-E confirms the expected improvement in performance.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

All simulations were run on an AlienWare Aurora R8 with an Intel^®^ Core^TM^ i9-9900K CPU and 64 GB RAM, using Ubuntu 22.04 LTS and ROS 2 Humble.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Representation Benchmarking: Simple Case", "weight": 1.0} -->

We first benchmark MIGHTY against GCOPTER (which uses MINCO ) on a simple corner-avoidance task with fixed start and goal (Fig. 1). For a fair comparison, we implement GCOPTER's optimization cost in MIGHTY and use the same optimizer (L-BFGS ) and stopping tolerances. Both methods start from the same initial guess.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Representation Benchmarking: Simple Case", "weight": 1.0} -->

GCOPTER represents each segment as a fifth-order polynomial, so MINCO minimizes jerk (third-order effort) by construction. MIGHTY uses a fifth-order Hermite spline to match the polynomial degree. GCOPTER applies diffeomorphic parameterizations for waypoints and durations (waypoints remain inside the overlap of safe flight corridors (SFCs); durations stay positive). The only difference is that MIGHTY includes an explicit jerk smoothness term (Sec. III-C1), while GCOPTER does not add a separate smoothness cost because MINCO already minimizes jerk.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Representation Benchmarking: Simple Case", "weight": 1.0} -->

The result in Fig. 2 shows that MIGHTY achieves a shorter travel time, with slightly faster computation and shorter path than GCOPTER. While GCOPTER produces smoother trajectories with lower jerk due to its constraint within the MINCO class, MIGHTY explores a larger search space to identify faster and more effective trajectories. This flexibility enables MIGHTY to achieve superior performance, and Sec. IV-B further investigates the jerk-performance trade-off.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Smooth Weight Sweep Benchmarking", "weight": 1.0} -->

Fig. 2 shows MIGHTY yields higher jerk than GCOPTER while achieving better travel time. To quantify this trade-off, we sweep $w_{\mathrm{smooth}}\in\{${10}^{-5}$,\ldots,${10}^{3}$\}$ in the same scenario. Fig. 3 shows that as $w_{\mathrm{smooth}}$ increases, MIGHTY progressively reduces jerk, eventually surpassing GCOPTER's levels of smoothness. At $w_{\mathrm{smooth}}=${10}^{2}$$, MIGHTY matches GCOPTER's jerk while maintaining better performance and lower computation time, demonstrating that MIGHTY's higher jerk is a tunable design choice rather than an inherent limitation.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-C Local Control of Higher-Order Dynamics", "weight": 1.0} -->

MINCO-based planners lack direct parameterization of higher-order derivatives at individual knots; these quantities are derived from a globally coupled coefficient system (Sec. I-A). While GCOPTER can add derivative constraints as soft penalties, MIGHTY's Hermite parameterization treats knot positions and velocities as explicit optimization variables. To evaluate this difference, we extend the simple corner-avoidance scenario (Fig. 1) with soft reference tracking terms for position and velocity at the penultimate knot, which is relevant for waypoint velocity specification and hover-at-goal behaviors.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-C Local Control of Higher-Order Dynamics", "weight": 1.0} -->

We augment the objective function with soft position and velocity reference terms where $\mathbf{p}_{\text{ref}}$ and $\mathbf{v}_{\text{ref}}$ are desired position and velocity at knot $k$, and $w_{\mathbf{p}_{\text{ref}}}$ and $w_{\mathbf{v}_{\text{ref}}}$ are penalty weights. For this benchmark, we set $k$ to the penultimate knot (one knot before the goal), $\mathbf{v}_{\text{ref}}=\,$\mathrm{m}\mathrm{/}\mathrm{s}$$ to enforce near-hover at the goal, and $\mathbf{p}_{\text{ref}}$ to the goal position.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-C Local Control of Higher-Order Dynamics", "weight": 1.0} -->

We use $w_{\mathbf{p}_{\text{ref}}}=$1\text{\times}{10}^{3}$$ and $w_{\mathbf{v}_{\text{ref}}}=$1\text{\times}{10}^{3}$$, with $v_{\max}=$2.0\text{\,}\mathrm{m}\mathrm{/}\mathrm{s}$$ and $w_{\mathrm{smooth}}=${10}^{-5}$$ for MIGHTY. All other settings match those in Sec. IV-F. We evaluate both GCOPTER and MIGHTY across 100 runs in the same simple corner-avoidance environment. Fig. 4 shows example trajectories from both planners, and Table II summarizes the results.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-C Local Control of Higher-Order Dynamics", "weight": 1.0} -->

MIGHTY achieves substantially better tracking: lower position error ($0.0041\text{\,}\mathrm{m}$ vs. $0.017\text{\,}\mathrm{m}$), 6.5$\times$ lower velocity error ($0.16\text{\,}\mathrm{m}\mathrm{/}\mathrm{s}$ vs. $1.0\text{\,}\mathrm{m}\mathrm{/}\mathrm{s}$), and 25.1% shorter travel time ($14.8\text{\,}\mathrm{s}$ vs. $19.7\text{\,}\mathrm{s}$). GCOPTER is faster ($7.4\text{\,}\mathrm{m}\mathrm{s}$ vs. $10.6\text{\,}\mathrm{m}\mathrm{s}$), though both meet real-time budgets.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-C Local Control of Higher-Order Dynamics", "weight": 1.0} -->

This demonstrates MIGHTY's advantage: while GCOPTER adds derivative constraints as soft penalties on MINCO-derived velocities, MIGHTY directly optimizes knot positions and velocities as explicit Hermite variables, enabling superior local control of higher-order dynamics.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-D Representation Benchmarking: Complex Case", "weight": 1.0} -->

We further evaluate MIGHTY in a complex environment (Fig. 5) with start at $(0,0,0.5)\,$\mathrm{m}$$ and 24 goals at $x,y\in\,$\mathrm{m}$$ and $z=2.5\,$\mathrm{m}$$. Optimization settings are identical to the simple case for both methods. We report the following metrics: $v_{\max}$ \[m/s\]: Speed limit, $T_{\mathrm{comp}}$ \[ms\]: Computation time, $T_{\mathrm{trav}}$ \[s\]: Travel time, $L_{\mathrm{path}}$ \[m\]: Path length, $\int\lVert\mathbf{j}(t)\rVert\,dt$ \[m/s^2^\]: Jerk smoothness integral, and $\rho_{\mathrm{viol}}$ \[%\]: Fraction of time violating dynamic bounds.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-D Representation Benchmarking: Complex Case", "weight": 1.0} -->

Overall, Table III shows MIGHTY reduces computation time by 9.3%, travel time by 13.1%, and path length by 1.4%. GCOPTER yields lower jerk, while MIGHTY's higher jerk reflects more aggressive maneuvers, enabled by smaller $w_{\mathrm{smooth}}=${10}^{-5}$$ and its larger search space. Both planners keep $\rho_{\mathrm{viol}}\leq$1.0\text{\,}\mathrm{\char 37\relax}$$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-E Ablation Study on Scaled and Unscaled Variables", "weight": 1.0} -->

As discussed in Sec. III-D, we optimize over scaled variables to improve numerical stability. We evaluate this via ablation using the same complex benchmarking setup. Fig. 6 shows the scaled variant is $\approx 2\times$ faster with lower jerk, while path length and travel time are nearly identical, confirming that scaling improves efficiency without degrading quality.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-F Benchmarking in Static Environments", "weight": 1.0} -->

To thoroughly evaluate MIGHTY, we benchmark it in an obstacle-rich environment (Fig. 7) against EGO-Swarm, EGO-Swarm2, and SUPER. Static cylindrical obstacles are placed randomly with radii sampled in $[\,$1.0\text{\,}\mathrm{m}$,$1.5\text{\,}\mathrm{m}$\,]$ and height $6.0\text{\,}\mathrm{m}$, occupying a $$300\text{\,}\mathrm{m}$\times$40\text{\,}\mathrm{m}$$ area. The agent starts at \mathrm{m}$$ and the goal is \mathrm{m}$$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-F Benchmarking in Static Environments", "weight": 1.0} -->

We constrain velocity, acceleration, and jerk to $v_{\max}=$4.0\text{\,}\mathrm{m}\mathrm{/}\mathrm{s}$$, $a_{\max}=$10.0\text{\,}\mathrm{m}\mathrm{/}\mathrm{s}^{2}$$, and $j_{\max}=$30.0\text{\,}\mathrm{m}\mathrm{/}\mathrm{s}^{3}$$. For global planning we run A\*, then build an SFC for local optimization. The intermediate waypoints for A\* are projected from the terminal goal onto the local occupancy map centered on the drone. The average computation time for A\* and SFC generation is $0.26\text{\,}\mathrm{m}\mathrm{s}$ and $0.48\text{\,}\mathrm{m}\mathrm{s}$, respectively.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-F Benchmarking in Static Environments", "weight": 1.0} -->

Fig. 7 illustrates the environment and one MIGHTY trajectory (in red in the bottom plot), and Table IV gives the full results. We evaluate each method with its default sensor; for methods whose default is not LiDAR (EGO-Swarm, EGO-Swarm2), we also run a LiDAR variant to align with SUPER and MIGHTY (both LiDAR-based). Note that EGO-Swarm with LiDAR performed substantially worse, so Table IV omits those data for clarity.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-F Benchmarking in Static Environments", "weight": 1.0} -->

Note that SUPER applies a soft penalty on the distance between the trajectory and points in the overlap of successive SFC segments, with weight $5\text{\times}{10}^{6}$, which is the largest among all cost terms. Summarizing the results, we see that EGO-Swarm2 is the fastest in local optimization and total replanning time ($1.2\text{\,}\mathrm{m}\mathrm{s}$ and $1.7\text{\,}\mathrm{m}\mathrm{s}$), whereas MIGHTY achieves the shortest travel time ($79.0\text{\,}\mathrm{s}$) and path length ($310.9\text{\,}\mathrm{m}$).

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-G Dynamic Environments", "weight": 1.0} -->

Dynamic-only environment: We generate 100 dynamic obstacles following smooth trefoil-knot trajectories, with initial positions $x\in\,$\mathrm{m}$$, $y\in\,$\mathrm{m}$$, $z\in\,$\mathrm{m}$$. Fig. 8 shows an example of the environment and the trajectory. MIGHTY avoids all obstacles in 10/10 trials. The minimum nearest-obstacle distance is $0.8\text{\,}\mathrm{m}$, above the $0.1\text{\,}\mathrm{m}$ safety threshold.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-G Dynamic Environments", "weight": 1.0} -->

Dynamic & static environment: We add 50 dynamic obstacles (same motion model) to the static forest as shown in Fig. 9 and run 10 trials. MIGHTY avoids all obstacles in all trials. The minimum is $1.0\text{\,}\mathrm{m}$, above the $0.1\text{\,}\mathrm{m}$ collision radius.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Hardware Experiments", "weight": 1.0} -->

We also evaluated MIGHTY in three hardware experiments: long-duration flights at $\,v_{\max}\in\{1,2,3,4\}\,$\mathrm{m}\mathrm{/}\mathrm{s}$$, high-speed flights up to $\,v_{\max}=7\,$\mathrm{m}\mathrm{/}\mathrm{s}$$, and flights with obstacles introduced during the mission. The perception uses a Livox Mid-360 LiDAR, and localization is provided by DLIO. Planning runs onboard on an Intel^™^ NUC 13, and low-level control uses PX4 on a Pixhawk flight controller. All perception, planning, and control run in real time onboard.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Hardware Experiments", "weight": 1.0} -->

Long-Duration Flight Experiment: To assess reliability over extended operations, the vehicle repeatedly traverses a space with multiple obstacles (Fig. 10). Six goal positions are placed opposite the start, inducing repeated out-and-back motions through the environment. For $\,v_{\max}\in\{1,2,3,4\}\,$\mathrm{m}\mathrm{/}\mathrm{s}$$, all flights completed without collision.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Hardware Experiments", "weight": 1.0} -->

High-Speed Flight Experiment: We further evaluate performance at higher speeds. As shown in Sec. IV, MIGHTY tends to produce higher-jerk trajectories; when constraints are satisfied, these trajectories remain safe while enabling faster motion. We test $\,v_{\max}=$5.0\text{\,}\mathrm{m}\mathrm{/}\mathrm{s}$,$6.0\text{\,}\mathrm{m}\mathrm{/}\mathrm{s}$,$7.0\text{\,}\mathrm{m}\mathrm{/}\mathrm{s}$$. Fig. 11 shows the resulting histories. All flights completed without collision, demonstrating that the MIGHTY planner and DLIO state estimation operate effectively at high speed.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Hardware Experiments", "weight": 1.0} -->

Dynamic Obstacle Flight Experiment: To assess robustness to changes in the environment, we introduce and move obstacles during the mission (Fig. 12). We track a person carrying obstacles and incorporate the estimates into the trajectory optimization; see Sec. IV-G for details. The agent successfully reaches the goal without collision over $490\text{\,}\mathrm{s}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We presented MIGHTY, a Hermite-spline trajectory planner for joint spatiotemporal optimization. By optimizing path geometry and time together with local derivative control, MIGHTY generates smooth, collision-free, and dynamically feasible trajectories for high-performance maneuvers. Benchmarks and hardware tests show MIGHTY outperforms baselines in travel time while satisfying constraints.
