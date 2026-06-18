<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

TinySDP: Real Time Semidefinite Optimization for Certifiable and Agile Edge Robotics

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Semidefinite programming (SDP) provides a principled framework for convex relaxations of nonconvex geometric constraints in motion planning, yet existing solvers are too computationally expensive for real-time control, particularly on resource-constrained embedded systems. To address this gap, we introduce TinySDP, the first semidefinite programming solver designed for embedded systems, enabling real-time model-predictive control (MPC) on microcontrollers for problems with nonconvex obstacle constraints. Our approach integrates positive-semidefinite cone projections into a cached-Riccati-based ADMM solver, leveraging computational structure for embedded tractability. We pair this solver with an a posteriori rank-1 certificate that converts relaxed solutions into explicit geometric guarantees at each timestep. On challenging benchmarks, e.g., cul-de-sac and dynamic obstacle avoidance scenarios that induce failures in local methods, TinySDP achieves collision-free navigation with up to 73% shorter paths than state-of-the-art baselines.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We validate our approach on a Crazyflie quadrotor, demonstrating that semidefinite constraints can be enforced at real-time rates for agile embedded robotics.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Safe motion planning and control in dynamic environments remains a challenge in robotics. Model-predictive control (MPC) is attractive for this setting due to its ability to reason about system dynamics and constraints (e.g., obstacle avoidance), and has been demonstrated on a wide range of robotic problems across numerous tasks and scenarios.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent advances in embedded optimization have expanded the scope of MPC on resource-constrained platforms, including the development of popular packages, e.g., OSQP, CVXGEN, ECOS, SCS. In particular, TinyMPC demonstrated that constrained quadratic MPC can be solved at high rates on microcontrollers by exploiting the Riccati structure through a combination of offline caching and first-order methods. Building on this foundation, subsequent work improved the robustness of the solver and added support for second-order cone constraints. Despite this progress, obstacle avoidance with formal guarantees remains an open problem in embedded MPC, particularly because obstacle constraints are inherently nonconvex. As such, existing real-time MPC implementations rely on conservative over-approximations or local convexifications that fail to capture global geometric structure and are fragile in practice (e.g., linearized distance constraints and tangent half-spaces ). This is because solutions that satisfy such approximations can still tunnel through obstacles, requiring extensive heuristic tuning of scenario-specific safety margins, and often still fail in the presence of narrow passages, cul-de-sacs, or dynamic obstacles.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Similarly, while barrier function based methods are also widely used for obstacle avoidance and collision avoidance, crafting effective barrier functions also relies on significant tuning. And, while Hamilton Jacobi (HJ) reachability tools can be used to construct tuning-free barrier functions, these tools do not scale well to high-dimensional systems. More recently, learning-based barrier functions leveraging neural networks have been developed to overcome the dual scalability and tuning challenges. However, deploying the resulting moderate-sized neural networks for real-time applications is often infeasible on embedded platforms.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, semidefinite programming (SDP) provides a principled way to pose nonconvex geometric constraints as convex by lifting quadratic or polynomial constraints into higher-dimensional positive semidefinite cones, and has been successfully applied in offline motion planning and trajectory optimization, globally optimal state estimation and localization, and sum-of-squares optimization with tools like SOSTOOLS. However, as with many of the prior techniques, general-purpose SDP solvers are computationally expensive and memory-intensive. As such, they are generally poorly suited for real-time receding horizon control, particularly for embedded applications.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we show that it is possible to overcome these challenges through careful exploitation of problem structure. We introduce TinySDP, the first semidefinite programming solver designed for real-time obstacle avoidance on embedded systems. Our approach uses a per-stage, convex, semidefinite relaxation of nonconvex, quadratic, disk-based obstacle avoidance constraints. These relaxations are small, structured, and compatible with Riccati-based MPC solvers, including cached variants. We pair this with a simple rank-1 certificate that converts the relaxed solution into an explicit geometric safety guarantee at every timestep. When the certificate holds, it provably certifies that the true robot position avoids all obstacles, despite the use of an efficient convex relaxation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our approach builds on prior observations that lifted convex relaxations are empirically tight in structured control problems. In particular, lifted semidefinite formulations of linear-quadratic control problems recover low-rank solutions, providing exact certificates of optimality.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate TinySDP on two challenging benchmark tasks that are designed to expose common failure modes for standard formulations: 1) a static U-shaped cul-de-sac and, 2) multiple dynamic moving-gap scenarios. Through systematic comparisons, we show that our method is less conservative, with path lengths up to 73% shorter than baseline approaches, while also remaining certifiably collision-free at each timestep through the use of our a posteriori rank-1 safety certificate. We also implement the full solver within the TinyMPC framework, and validate our algorithm through real-world hardware deployments on a Crazyflie 2.1 Brushless quadrotor at 25 Hz control rates, demonstrating that semidefinite constraints can be enforced at real-time rates for embedded robotic tasks.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Linear, Cached, and Riccati-Based MPC Solvers", "weight": 1.0} -->

We highlight the components of the generic finite-horizon MPC problem that prevent a closed-form solution.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Linear, Cached, and Riccati-Based MPC Solvers", "weight": 1.0} -->

Consider a discrete-time linear time-invariant system with state $x_{k} \in {\mathbb{R}}^{n}$ and control input $u_{k} \in {\mathbb{R}}^{m}$ at timestep $k$,

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Linear, Cached, and Riccati-Based MPC Solvers", "weight": 1.0} -->

Given a horizon length $N$, and assuming quadratic stage and terminal costs, for $Q \succeq 0$, $R \succ 0$, and $Q_{f} \succeq 0$, define

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Linear, Cached, and Riccati-Based MPC Solvers", "weight": 1.0} -->

The presence of constraints destroys this structure, necessitating a numerical approach. To overcome this challenge, recent approaches have leveraged the alternating direction method of multipliers (ADMM), to separate the inequality constraints from the remainder of the problem, enabling the reintroduction of the efficient Riccati recursion. This is done by first introducing auxiliary variables, $z_{k}$, into the problem.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Linear, Cached, and Riccati-Based MPC Solvers", "weight": 1.0} -->

For clarity, and without loss of generality, we assume that the only inequality constraints in our MPC problem are on the controls, $u$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Linear, Cached, and Riccati-Based MPC Solvers", "weight": 1.0} -->

We then perform alternating minimization on $\mathcal{L}_{\rho}$ with respect to $x,u,z$, arriving at the three-step ADMM iteration,

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Linear, Cached, and Riccati-Based MPC Solvers", "weight": 1.0} -->

where the last step is a gradient-ascent update on the duals. These steps can be iterated until a desired convergence tolerance is achieved. Importantly, the primal problem 5a now reduces to the Riccati Recursion, the slack update is a projection, and the dual update is simply a vector addition.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Linear, Cached, and Riccati-Based MPC Solvers", "weight": 1.0} -->

The key observation that makes this whole framework efficient is that many common convex constraint sets admit simple, closed-form projection operators to solve (5b).

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A Linear, Cached, and Riccati-Based MPC Solvers", "weight": 1.0} -->

Cache-based solvers, like TinyMPC, go one step further and fix and cache key values offline that reduce the computational complexity of the primal Riccati recursion even further. These computational savings both reduce the latency of the solver as well as its memory requirements, enabling high-rate MPC on resource-constrained platforms.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A Linear, Cached, and Riccati-Based MPC Solvers", "weight": 1.0} -->

In particular, for sufficiently long horizons, the Riccati recursion converges to the infinite-horizon LQR solution, where the time-varying matrices $K_{k}$ and $P_{k}$ are approximated by steady-state quantities $K_{\infty}$ and $P_{\infty}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Semidefinite Relaxations of Quadratic Constraints", "weight": 1.0} -->

Many geometric safety constraints encountered in robotics are quadratic and nonconvex.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Semidefinite Relaxations of Quadratic Constraints", "weight": 1.0} -->

where $c_{j} \in {\mathbb{R}}^{2}$ is the center and $r_{j} > 0$ the radius of obstacle $j$. Note that Equation is nonconvex.^11^1The same lifting idea extends directly to a $d$-dimensional geometric subspace $p_{k} \in {\mathbb{R}}^{d}$, with disks replaced by Euclidean balls and the lifted moment block growing accordingly.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B Semidefinite Relaxations of Quadratic Constraints", "weight": 1.0} -->

In this paper, we adopt the standard semidefinite lifting of the geometric state. Specifically, we introduce the lifted matrix,

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Semidefinite Relaxations of Quadratic Constraints", "weight": 1.0} -->

which allows quadratic terms in $p_{k}$ to be expressed linearly.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B Semidefinite Relaxations of Quadratic Constraints", "weight": 1.0} -->

Such semidefinite relaxations are widely used in offline trajectory optimization, sum-of-squares programming, and safety verification. However, general-purpose semidefinite programming (SDP) solvers scale poorly with problem dimension and horizon length, making them unsuitable for real-time control and embedded deployment.

<!-- chunk {"id": "body-0026", "role": "body", "section": "TinySDP", "weight": 1.0} -->

Despite their success in embedded settings, Riccati-based MPC solvers are typically limited to constraint classes that preserve stage-wise structure and admit efficient proximal/projection steps (e.g., linear and second-order cone constraints). While semidefinite programming is also a form of conic optimization, it is considered incompatible with real-time MPC as general-purpose SDP methods require repeated large matrix factorizations with per-iteration costs that scale cubically in the semidefinite matrix variable dimensions.

<!-- chunk {"id": "body-0027", "role": "body", "section": "TinySDP", "weight": 1.0} -->

We show that, by introducing a structured lifting that preserves the computational structure needed for efficient Riccati-based MPC, these tractability barriers can be bypassed, enabling real-time, certifiable safety for embedded robotics.

<!-- chunk {"id": "body-0028", "role": "body", "section": "TinySDP", "weight": 1.0} -->

We consider the MPC problem with the following inequality constraints.

<!-- chunk {"id": "body-0029", "role": "body", "section": "TinySDP", "weight": 1.0} -->

Second, safety is enforced via obstacle avoidance constraints on a selected geometric subspace of the state. In our deployed setting, we specialize to the planar position and let $p_{k} \in {\mathbb{R}}^{2}$ denote the planar position component of the state, i.e., $p_{k} = {C_{p}x_{k}}$ for a known selection matrix $C_{p} \in {\mathbb{R}}^{2 \times n_{x}}$. We model obstacles as unions of disks,

<!-- chunk {"id": "body-0030", "role": "body", "section": "TinySDP", "weight": 1.0} -->

and enforce safety via per-timestep keep-out constraints using. Such constraints are inherently nonconvex and present a central challenge for real-time MPC. Our goal is therefore to design a receding-horizon MPC controller that enforces with explicit safety guarantees, while remaining compatible with embedded solvers based on Riccati recursion.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A1 Lifted Dynamics and Costs", "weight": 1.0} -->

which we lift to SDP constraints analogously to. We define the lifted state, input, and initial condition as,

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A1 Lifted Dynamics and Costs", "weight": 1.0} -->

noting that the lifted initial state is rank-consistent at initialization (as required by the rank-1 certificate introduced later).

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A1 Lifted Dynamics and Costs", "weight": 1.0} -->

Using the following identities and expansion,

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A1 Lifted Dynamics and Costs", "weight": 1.0} -->

We can then define the projection matrices,

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A2 Lifted Geometric Constraints", "weight": 1.0} -->

While we specialize to $p_{k} \in {\mathbb{R}}^{2}$ for the planar obstacle-avoidance setting studied in this paper, the same construction applies to any $d$-dimensional geometric subspace by taking $X_{k}^{(p)}:={C_{p}X_{k}C_{p}^{\top}} \in {\mathbb{R}}^{d \times d}$ and replacing disks with Euclidean balls defined over the corresponding geometric coordinates.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A2 Lifted Geometric Constraints", "weight": 1.0} -->

The nonconvex disk obstacle avoidance constraints can also thus be expanded as,

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A3 Per-Stage PSD Constraint", "weight": 1.0} -->

In the exact (non-relaxed) case, $M_{k}$ is rank-1. Relaxing to $M_{k} \succeq 0$ yields a convex relaxation that permits $X_{k} \neq {x_{k}x_{k}^{\top}}$ (and similarly for $XU_{k}$, $UX_{k}$, $UU_{k}$) when obstacle constraints are active. In our approach, the tightness of the relaxation is assessed a posteriori using the certificate in Section III-D. The physical variables $x_{k}$ and $u_{k}$ remain explicit decision variables in the MPC and are not reconstructed from the lifted moment.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-A4 Lifted MPC Problem", "weight": 1.0} -->

The resulting MPC problem is posed over lifted variables ${\{{\overline{x}}_{k}\}}_{k = 0}^{N}$ and ${\{{\overline{u}}_{k}\}}_{k = 0}^{N - 1}$: (i) linear lifted dynamics, (ii) lifted costs, (iii) input bounds on the physical inputs $u_{k}$, (iv) lifted geometric inequalities, and (v) per-stage PSD constraints. This problem is convex but includes per-stage semidefinite constraints, which are not directly supported by existing embedded solvers. We next show how to solve this problem efficiently using ADMM while preserving Riccati structure.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-B Riccati--ADMM Solver for PSD-Relaxed Lifted MPC", "weight": 1.0} -->

We solve the PSD-relaxed lifted MPC problem using a Riccati-based ADMM, extending the TinyMPC framework to incorporate per-stage semidefinite constraints while preserving its computational structure.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-B Riccati--ADMM Solver for PSD-Relaxed Lifted MPC", "weight": 1.0} -->

We introduce a PSD slack variable $S_{k} \in {\mathbb{S}}_{+}^{p}$ and a scaled dual variable $H_{k} \in {\mathbb{S}}^{p}$ for the coupling constraint, which are both stored using the $\sqrt{2}$-scaled half-vectorization operator ${svec}{( \cdot )}$, with inverse mapping ${smat}{( \cdot )}$, to further reduce the memory requirements of our approach, while ensuring that Frobenius inner products are preserved under vectorization. We then define $M_{k}{({\overline{x}}_{k},{\overline{u}}_{k})}$ as the per-stage state--input moment matrix defined in and $p:={1 + n_{x} + n_{u}}$,

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-B Riccati--ADMM Solver for PSD-Relaxed Lifted MPC", "weight": 1.0} -->

Using the scaled form of ADMM, each iteration alternates between a primal update, a PSD projection, and a dual update. To simplify notation, we define the augmented stage cost,

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-B Riccati--ADMM Solver for PSD-Relaxed Lifted MPC", "weight": 1.0} -->

The ADMM updates are thus given,

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-B Riccati--ADMM Solver for PSD-Relaxed Lifted MPC", "weight": 1.0} -->

where $\rho_{psd} > 0$ is the penalty parameter, and $\gamma_{psd} \in {(0,1\rbrack}$ is an optional under-relaxation factor.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-B Riccati--ADMM Solver for PSD-Relaxed Lifted MPC", "weight": 1.0} -->

Note that this projection has an analytic solution,

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-B1 Primal Update (Riccati Step)", "weight": 1.0} -->

With the slack and dual variables fixed, the primal subproblem (19a) is an equality-constrained quadratic program with linear dynamics and the lifted quadratic stage cost defined. The PSD-augmented term in Eq.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-B1 Primal Update (Riccati Step)", "weight": 1.0} -->

Crucially, the system dynamics remain unchanged, so the resulting primal problem is still a lifted LQR problem. As in TinyMPC, it can therefore be solved efficiently by a backward-forward Riccati sweep using the cached steady-state Riccati quantities computed offline (as described in Section II).

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-B2 PSD Projection and Dual Update", "weight": 1.0} -->

At each ADMM iteration, the slack update (19b) is computed via, followed by the scaled dual update (19c).

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-B2 PSD Projection and Dual Update", "weight": 1.0} -->

1:function TinySDP_Offline(Lifted Model &amp; Costs) 2: Construct lifted dynamics $(\overline{A},\overline{B})$ via 3: Construct lifted quadratic costs $(\overline{Q},\overline{R})$ via 4: Compute and cache lifted Riccati quantities via 5: return Cached solver data 𝒞 7:function TinySDP_Online(xk, Obstacles 𝒪k, Cache 𝒞) 8: Lift current state: ${\overline{x}}_{0}\leftarrow{\lbrack x_{k}^{\top},{{vec}{({x_{k}x_{k}^{\top}})}^{\top}}\rbrack}^{\top}$ 9: Initialize slack and dual variables 10: while residual &gt; ε and iter &lt; Kmax do 11: // Primal Update (Riccati Step) 12: qk, rk← Update linear costs via adjoint mapping 13: dk, pk← Backward Riccati recursion via

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-B2 PSD Projection and Dual Update", "weight": 1.0} -->

14: ${\overline{x},\overline{u}}\leftarrow$ Forward rollout via 15: // PSD Projection and Dual Update 17: Form moment matrix $M_{k}{({\overline{x}}_{k},{\overline{u}}_{k})}$ via 18: Sk← PSD Projection via (19b) 19: Hk← Dual Update via (19c) 22: return $({\overline{x}}_{k:{k + N}},{\overline{u}}_{k:{{k + N} - 1}})$ Algorithm 1 TinySDP: PSD-Relaxed Lifted MPC

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-B2 PSD Projection and Dual Update", "weight": 1.0} -->

1:function TinySDP_Step(xk, 𝒪k, 𝒞, uhover)
2: // Solve with TinySDP
3: ${{\overline{x}}_{k:{k + N}},{\overline{u}}_{k:{{k + N} - 1}}}\leftarrow{\text{TinySDP\_Online}{(x_{k},\mathcal{O}_{k},\mathcal{C})}}$
4: // Verify solution quality
5: Δk← Compute trace gap via
6: ηkmin ← minjηk, j via
7: if ηkmin ≥ 0 and |Δk| ≤ ηkmin then
8: $u_{k}\leftarrow{\overline{u}}_{k}$ ⊳ First control in optimized sequence
10: uk ← uhover ⊳ Fallback Policy (brake and hover)
Algorithm 2 TinySDP with Online Certificate

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-C Overall TinySDP Algorithm", "weight": 1.0} -->

TinySDP (Algorithm 1) adapts a standard receding-horizon MPC loop. Offline, the lifted dynamics, costs, and steady-state Riccati quantities for the lifted primal subproblem are computed and stored in a cache, $\mathcal{C}:={\{ K_{\infty},P_{\infty},C_{1},C_{2},\ldots\}}$. Online, at each control timestep $k$, the current measured state $x_{k}$ and obstacle set $\mathcal{O}_{k}$ are used to solve the finite-horizon PSD-relaxed lifted MPC problem. Within each ADMM iteration, the cached infinite-horizon Riccati quantities are used for efficiency. The solver returns a finite-horizon state/input sequence. The first control input is then applied and the problem is re-solved at the next control step using updated state and obstacle information.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Trace Gap and Lifted Margin", "weight": 1.0} -->

For clarity, we state the certificate for the planar case $p_{k} \in {\mathbb{R}}^{2}$, but the same argument extends directly to any $d$-dimensional geometric subspace by replacing $X_{k}^{(p)} \in {\mathbb{R}}^{2 \times 2}$ with $X_{k}^{(p)} \in {\mathbb{R}}^{d \times d}$. Let $p_{k} \in {\mathbb{R}}^{2}$ be the position at time $k$ and $X_{k}^{(p)} \in {\mathbb{R}}^{2 \times 2}$ be the position block of the lifted moment matrix. We define the *trace gap* as

<!-- chunk {"id": "body-0053", "role": "body", "section": "Trace Gap and Lifted Margin", "weight": 1.0} -->

This scalar measures the mismatch between the relaxed lifted variable and the exact rank-1 moment induced by the physical state $p_{k}$. In particular, $\Delta_{k} = 0$ implies that the lifted position block is consistent with the exact physical second moment, while $\Delta_{k} > 0$ indicates that the relaxed lifted second moment occupies more volume than the physical state. Similarly, for obstacle $j$ with center $c_{j}$ and radius $r_{j}$, the *lifted margin* is

<!-- chunk {"id": "body-0054", "role": "body", "section": "Trace Gap and Lifted Margin", "weight": 1.0} -->

which corresponds to the linear obstacle-avoidance constraint enforced by the solver.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Certification Logic", "weight": 1.0} -->

then $\delta_{k,j} \geq 0$ for all $j$, certifying that $x_{k}$ is collision-free.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Certification Logic", "weight": 1.0} -->

The rank-1 condition is *sufficient*, but not necessary. A certification failure occurs when either the lifted margin is negative ($\eta_{k}^{\min} < 0$) or the relaxation gap exceeds the available lifted margin (${|\Delta_{k}|} > \eta_{k}^{\min}$). However, we note that, even when the relaxation is not exactly rank-1, this simple trace-based certificate suffices to certify geometric clearance from obstacles. When the certificate fails, the relaxation may be too loose, and while the physical state $p_{k}$ might still be safe, we cannot provide a mathematical guarantee.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Online Safety Monitor", "weight": 1.0} -->

To enhance robustness in deployed settings, we integrate a runtime safety monitor into the control loop (Algorithm 2). If the solver produces a solution that fails, the system discards the planned update and executes a fallback stop-and-hover policy. This ensures that uncertified control inputs are never applied to the physical system. While this monitor provides a rigorous check on the deployed state, it serves as a reactive failsafe rather than a formal closed-loop guarantee under extreme conditions, such as high-velocity obstacles or significant modeling errors.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Experiments", "weight": 1.0} -->

We designed our experiments to evaluate both static and dynamic obstacle avoidance under known challenging geometries for state-of-the-art methods. In the static setting, we consider a concave U-shaped obstacle, a cul-de-sac, with the goal located beyond the obstacle, a canonical cause of deadlock and failure modes for local and reactive methods. In the dynamic setting, we construct a scenario consisting of a static obstacle directly in front of the agent together with two moving obstacles that periodically close a narrow passage, resulting in a three-obstacle interaction that requires continuous updates to the obstacle avoidance strategy, rather than one-shot reactive planning. We finally deploy our approach on a Crazyflie to evaluate our method's real-world feasibility.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Experiments", "weight": 1.0} -->

TinyMPC-LIN: linearized tangent half-space constraints as per the original TinyMPC paper,

<!-- chunk {"id": "body-0060", "role": "body", "section": "Experiments", "weight": 1.0} -->

TinyMPC-HOCBF: relative-degree-2 control barrier function constraints with TinyMPC, inspired,

<!-- chunk {"id": "body-0061", "role": "body", "section": "Experiments", "weight": 1.0} -->

RPCBF, a state-of-the-art sampling-based policy safety filter implemented outside TinyMPC.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Experiments", "weight": 1.0} -->

For all our experiments, all methods use identical discrete-time dynamics, input bounds, horizon length, and obstacle geometry, unless otherwise specified. Additionally, to ensure a fair comparison, we evaluate TinyMPC-LIN and TinyMPC-HOCBF with a zero safety margin, benchmarking against TinySDP which inherently requires no additional margin. For RPCBF, we similarly use zero safety margin but tune the underlying $\alpha$ parameters to achieve the best possible performance. Additionally, to provide a "best-case" analysis for the linearized baselines, we performed a grid search to determine the minimum safety margin required for TinyMPC-LIN and TinyMPC-HOCBF to successfully navigate the benchmarks. Our ablation studies reveal that these methods require a minimum safety margin of $1.5m$ to avoid collision. We note that such margins are highly impractical for our target domain of embedded, small-scale robotic platforms, which have widths roughly equal to $100{mm}$, resulting in artificial inflation of the collision footprint by over $17 \times$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-A Simulation: Static U-Shape Cul-de-Sac", "weight": 1.0} -->

We first evaluate TinySDP against the baseline methods using a static U-shaped obstacle composed of overlapping disks. Four representative initial conditions are considered: starting inside the cul-de-sac, outside the center opening, near the upper edge, and near the lower edge. Figure 2 visualizes the resulting trajectories, and Table I summarizes performance across path length, distance to goal, and collision status.

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-A Simulation: Static U-Shape Cul-de-Sac", "weight": 1.0} -->

TinyMPC-LIN and TinyMPC-HOCBF with a safety margin of $0$ collide for every start scenario. Failures in TinyMPC-LIN arise from its reliance on nominal-dependent tangent half-space constraints, which do not impose a global geometric keep-out condition and may remain inactive until the system is already in an inevitable collision state. Similarly, TinyMPC-HOCBF enforces a continuous-time barrier condition evaluated only at discrete sampling instants; in the presence of bounded inputs and concave, trap-like geometries, this local reactive formulation fails to prevent collisions.

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-A Simulation: Static U-Shape Cul-de-Sac", "weight": 1.0} -->

While TinyMPC-LIN can navigate the cul-de-sac with a safety margin of $3.1m$, this buffer is approximately $30 \times$ the Crazyflie diameter, rendering the approach impractical for real-world deployment. Moreover, the inflated obstacle boundaries overlap with the goal region, forcing the solver to terminate approximately $1.4m$ away from the target. TinyMPC-HOCBF fails to avoid collisions *regardless of the safety margin*, highlighting the limitations of local reactive methods.

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-A Simulation: Static U-Shape Cul-de-Sac", "weight": 1.0} -->

RPCBF is the strongest baseline and also remains collision-free in all cases with a 0m margin. However, it produces significantly longer, conservative trajectories.

<!-- chunk {"id": "body-0067", "role": "body", "section": "IV-A Simulation: Static U-Shape Cul-de-Sac", "weight": 1.0} -->

Overall, TinySDP achieves $31\text{–}{73\%}$ shorter paths than RPCBF and $2\text{–}{59\%}$ shorter paths than the tuned TinyMPC-LIN. TinySDP also consistently reaches within $0.02m$ of the goal across all scenarios, making it $4\text{–}15 \times$ more precise than RPCBF and $70 \times$ more precise than TinyMPC-LIN.

<!-- chunk {"id": "body-0068", "role": "body", "section": "IV-B Simulation: Dynamic Obstacles", "weight": 1.0} -->

We next evaluate all methods in a dynamic obstacle scenario consisting of a static disk at the start, followed by moving disks that periodically open and close a narrow passage. This task requires continuous updates to the obstacle avoidance strategy, rather than one-shot reactive planning.

<!-- chunk {"id": "body-0069", "role": "body", "section": "IV-B Simulation: Dynamic Obstacles", "weight": 1.0} -->

Quantitative results are summarized in Table II, with representative trajectories shown in Figure 3. As illustrated, TinySDP successfully reaches the goal while maintaining positive clearance and remaining rank-1 at every timestep. In contrast, TinyMPC-LIN and TinyMPC-HOCBF with no safety margin both collide early, as local linearizations and discrete-time barrier evaluations are insufficient for fast-moving geometries. While these methods can be made safe using margins of $1.5m$ and $3m$ respectively, such values are $17\text{–}30 \times$ the size of the drone and are therefore impractical for real dynamic environments with narrow corridors. RPCBF again remains collision-free with significantly longer, conservative paths.

<!-- chunk {"id": "body-0070", "role": "body", "section": "IV-B Simulation: Dynamic Obstacles", "weight": 1.0} -->

Quantitatively, TinySDP achieves $30\%$ shorter paths than RPCBF and $43\%$ shorter paths than the tuned TinyMPC-HOCBF ($3m$ margin). While the tuned TinyMPC-LIN ($1.5m$ margin) produces the shortest path at $13.61m$, TinySDP converges $1.3 \times$ closer to the goal ($0.018m$ vs $0.023m$) and is $3.8\text{–}4.3 \times$ more precise than RPCBF and TinyMPC-HOCBF, respectively. The shorter path length of the tuned TinyMPC-LIN could be attributed to its specific trajectory, which curves from below and arrives at the intersection only after the moving obstacle has passed. This timing allows the solver to effectively, and luckily, bypass the active avoidance maneuver. In contrast, TinySDP actively deviates to negotiate the obstacle while it is still blocking the path, ensuring certified safety at the cost of a slightly longer trajectory in this specific case.

<!-- chunk {"id": "body-0071", "role": "body", "section": "IV-C Simulation: Extension to 3D Obstacle Avoidance Demos", "weight": 1.0} -->

As noted earlier, the proposed lifting is not inherently limited to planar obstacles. In a 3D setting, lifting the position state ${\lbrack 1,x,y,z\rbrack}^{\top}$ yields a $4 \times 4$ moment matrix, so the same lifted semidefinite obstacle-avoidance formulation and applied-state certificate structure extend naturally to spherical obstacles and other quadratic sets (e.g., ellipsoids, cylinders).

<!-- chunk {"id": "body-0072", "role": "body", "section": "IV-C Simulation: Extension to 3D Obstacle Avoidance Demos", "weight": 1.0} -->

Of course, these richer geometric formulations require larger PSD cones and therefore more expensive projections, inducing tighter embedded compute and memory tradeoffs.

<!-- chunk {"id": "body-0073", "role": "body", "section": "IV-C Simulation: Extension to 3D Obstacle Avoidance Demos", "weight": 1.0} -->

To illustrate this extension, we consider two dynamic 3D scenarios. In *Sweeping Barrier*, two moving spheres sweep laterally across the route while a third upstream sphere blocks the direct start-to-goal path, requiring an early nonplanar deviation rather than a purely reactive planar sidestep. In *Vertical Gate*, two static side spheres together with a centrally located sphere oscillating in height create a time-varying 3D passage, forcing a timed ascent-descent maneuver rather than a planar bypass. Representative trajectories are shown in Figure 4. In both scenarios, TinySDP reaches the goal without collisions.

<!-- chunk {"id": "body-0074", "role": "body", "section": "IV-D Real World Deployment: Dynamic Obstacles", "weight": 1.0} -->

To validate real-world feasibility on resource-constrained platforms, we deploy TinySDP on a Crazyflie 2.1 Brushless quadrotor, powered by an STM32F405 microcontroller (168 MHz with only 192 KB of SRAM). We apply the semidefinite relaxation strictly to the planar position of the quadrotor's 12-dimensional state, $(p_{x},p_{y})$, yielding a $3 \times 3$ moment matrix,

<!-- chunk {"id": "body-0075", "role": "body", "section": "IV-D Real World Deployment: Dynamic Obstacles", "weight": 1.0} -->

where the PSD constraint $M_{k} \succeq 0$ is enforced via projection within the ADMM solver. Since the nonconvex obstacle constraints depend only on planar position, this corresponds to the minimal task-induced lift sufficient to certify geometric clearance. The remaining state variables (altitude, velocity, attitude) are handled via box constraints as in prior work.

<!-- chunk {"id": "body-0076", "role": "body", "section": "IV-D Real World Deployment: Dynamic Obstacles", "weight": 1.0} -->

The solver runs onboard at 25 Hz with a 20-step horizon. In the deployed implementation, ADMM is capped at 5 iterations per control update to guarantee timing. In the latest logged hardware run, the solver executed all 5 iterations and reported a total MPC solve time of $14.842{ms}$, leaving approximately $25.2{ms}$ of margin within the $40{ms}$ control period. The compiled firmware footprint is $272.4{KB}$ of flash and $139.0{KB}$ of on-chip RAM ($83.5{KB}$ main SRAM and $55.6{KB}$ CCM). The PSD-specific overhead is modest, adding approximately $1.47{KB}$ of fixed static memory, about $720B$ of peak additional stack usage along the PSD projection path, and an estimated $2.5$--$3.4{KB}$ of flash.

<!-- chunk {"id": "body-0077", "role": "body", "section": "IV-D Real World Deployment: Dynamic Obstacles", "weight": 1.0} -->

Since the lifted variable is only a symmetric $3 \times 3$ matrix over $\lbrack 1,p_{x},p_{y}\rbrack$, the PSD projection is implemented using a specialized small-matrix eigendecomposition with eigenvalue clamping and is not a practical bottleneck in this planar setting.

<!-- chunk {"id": "body-0078", "role": "body", "section": "IV-D Real World Deployment: Dynamic Obstacles", "weight": 1.0} -->

A low-level PID controller tracks the planned trajectory at 500 Hz. We validate the approach in a dynamic obstacle avoidance scenario where the Crazyflie flies 1 m forward while a robotic arm sweeps horizontally across its path. As shown in Figure 1, the drone successfully anticipates the moving obstacle, autonomously deviating to maintain safety before converging to the goal. Notably, as shown in Figure 5, the online safety certificate (Section III-D) remained valid^22^2The certificate is evaluated with a small numerical tolerance ($\varepsilon = 10^{- 2}$) to account for finite-precision arithmetic on the embedded hardware platform. ($\Delta_{k} \approx 0$) at every control step throughout the flight for five independent trials, confirming that the rank-1 geometry was preserved even under real-world disturbances.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Limitations", "weight": 1.5} -->

While TinySDP achieved zero failures across all hardware trials, several limitations warrant discussion. Most fundamentally, our trace-gap certificate provides a rigorous per-timestep geometric check on the applied state, but does not constitute a formal closed-loop guarantee. In particular, we do not prove recursive feasibility over the full predicted horizon, although offline analysis confirms horizon-wide certificate satisfaction on our nominal trajectories, this remains an empirical observation rather than a property of the closed-loop system itself. While simulations show our lifting framework extends naturally to 3D spherical obstacles, onboard deployment reveals a computational tradeoff. The 3x3 moment matrix used in our planar hardware demonstration keeps PSD projections tractable; however, higher dimensions or complex geometries expand the lifted block, driving up per-iteration eigendecomposition costs. Transitioning this full 3D capability to microcontrollers remains a key focus for future work. Finally, as established in our discussion of the online safety monitor III-D, the fallback policy acts solely as a reactive failsafe. Extreme conditions such as sufficiently fast-moving obstacles, large modeling errors, or severe external disturbances could in principle outpace this fallback.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Limitations", "weight": 1.5} -->

Extending the framework with forward reachability analysis to provide proactive rather than purely reactive recovery guarantees is a natural next step.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

We introduced TinySDP, a PSD-relaxed lifted MPC framework that enables certifiable obstacle avoidance on embedded platforms while preserving cached-Riccati-based computational structure. By integrating per-stage semidefinite lifting with an ADMM-based solver, we establish a methodological pathway for incorporating semidefinite relaxations into embedded MPC. Furthermore, by exploiting per-stage structure and separating optimization from certification, we show that SDP-based safety constraints are not inherently incompatible with real-time receding-horizon control. This perspective bridges the gap between offline semidefinite planning and practical embedded deployment, and suggests that richer convex safety models can be integrated into high-rate controllers when solver design respects MPC structure. Future work includes extending the framework to more challenging hardware demonstrations and richer obstacle representations to identify where our relaxations are loose. More broadly, we hope this work motivates the development of more low-compute and low-memory footprint solvers for real-time control.
