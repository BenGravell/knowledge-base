<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

ElastiQP: An Always-Feasible QP Solver for Constrained Robot Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

As robot capabilities increase, quadratic programming (QP)-based controllers must account for a similarly increasing number of constraints to ensure safe, reliable operation. Yet, with each added constraint, this introduces more chances of momentary conflict: in which case, a QP solver that returns an "infeasible" status leaves the controller with nothing to execute. To address this, we introduce ElastiQP, a modified dual active-set QP solver that relaxes every inequality constraint with an exact, per-constraint l1 penalty while keeping equality constraints (dynamics) hard. Notably, ElastiQP does so by folding the slack variables into the solver analytically, maintaining a constant size of the condensed linear system. On a suite of robot control benchmarks, ElastiQP achieves microsecond-level performance, matching or outperforming leading modern solvers on feasible problems. On infeasible problems, ElastiQP handles these gracefully, confining violations to strictly the conflicting inequality terms, returning a usable solution up to 40x faster than the best alternative solvers. ElastiQP is available as an open-source C++ header-only library, with Python and JAX interfaces, at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Quadratic programs (QPs) are a central part of model-based robot control, including whole-body control, safety filters, hierarchical control, legged locomotion, and inverse kinematic and dynamic methods more generally. Broadly speaking, QP-based controllers can be divided into two main categories: small, dense problems for real-time (single-timestep, high-frequency) control, and larger, more structured problems that consider a predictive horizon (e.g., model predictive control (MPC)). For real-time control, the target rate for such controllers is typically 1 kHz, to stabilize high-frequency dynamic modes. This necessitates a solver which can reliably deliver a solution in (ideally well under) 1 ms, for problems on the order of tens of decision variables.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The constraints in these QPs typically encode dynamics terms (equalities), or limits, tasks, and safety margins (usually, inequalities). For complex robots and environments, these constraints can easily number in the hundreds, often introducing edge cases where these are instantaneously inconsistent, particularly under unexpected disturbances. In this case, a solver that returns "infeasible" leaves the robot with no control to execute, a potentially dangerous state. Ideally, even in the case of conflict, the controller will always return a minimally-violating, best-effort command within the time budget.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fig. 1: Elastic QPs are at the core of hardware deployments of online safety filters and controllers, including on drones, manipulators, and humanoids. In each case, elasticity resolves momentary conflict between constraints (safety, actuator limits, and tasks) in a minimally-conservative manner, allowing the robot to operate reliably near its dynamic limits. ElastiQP now accelerates these same problems, for high-frequency deployment on even the most challenging highly-constrained and high-DoF systems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A formulation well-suited to this setting is an elastic QP: each constraint is relaxed with an exact $\ell_{1}$ penalty on violation (the "elastic mode" of SNOPT ). When the problem is feasible, and if elastic penalty terms are sufficiently high, the elastic solution is exactly the hard solution. Thus, for the majority of timesteps when no conflict occurs, the added reliability of the elastic structure costs nothing to the optimal control. When conflict does occur, the $\ell_{1}$ structure encourages sparsity in the constraint violation, restricting the relaxation to only the terms in conflict. Conversely, an $\ell_{2}$ relaxation spreads constraint violation across terms which were never in conflict, leading to undesired tradeoffs in these edge cases.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Remark: For robot control, we are interested in a specific type of elastic mode, where we allow for both hard equality constraints, and elastic inequality constraints. Dynamics constraints are posed as equalities, and these are always physically consistent with each other, and meaningless if relaxed (for instance, a solution where torques and accelerations are incompatible). If equalities are possibly-inconsistent, non-dynamics terms, these can always be made elastic via opposing elastic inequalities.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In general, the only way to pose an elastic QP to a general-purpose solver is to add a slack variable per constraint and solve over the expanded decision vector. With large numbers of constraints, the factorization cost is dominated by the slack variables, rather than the original decision variables, leading to difficulty meeting the 1 ms time budget for control. This is the case for ProxQP, PIQP, and DAQP, three of the leading solvers for problems at this scale. Alternatively, ProxQP and DAQP each offer a "closest feasible" or "soft" mode in the case of primal infeasibility, but these solve for the (undesirable) minimum $\ell_{2}$ shift in the constraints, require first detecting infeasibility, and cannot individually weight relaxation on a per-constraint basis. ProxQP and PIQP's sparse backends can also exploit the (considerable) sparsity that per-constraint slack variables introduces, but sparse backends are primarily designed for large-scale problems, and perform poorly in this small-scale high-frequency setting.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

qpax performs competitively here: its elastic mode introduced a trick for slack variable elimination in interior point methods, which inspired this work. However, this elastic mode does not support equality constraints or warm-starting, its speed falls short of 1 kHz rates on humanoid-scale problems, and it tends to fail to achieve tight tolerance on even moderately ill-conditioned problems. FlexQP adopts a similar $\ell_{1}$ relaxation on both inequality and equality constraints, within an OSQP-style ADMM method. This work targets hyperparameter learning and batched solves on GPU at loose tolerances, rather than tight, warm-started solves at control rates. FlexQP also converges at first-order rates, and iterates over the slacks and duals, rather than eliminating these in closed form.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-A Statement of Contributions", "weight": 1.0} -->

We present ElastiQP, an always-feasible QP solver for constrained robot control. ElastiQP is a modified dual active-set method, designed for hard equality constraints, $\ell_{1}$ elastic inequality constraints, and strong warm-starting performance across the repetitive structure of control loops. Notably, ElastiQP solves these problems through an exact elimination of the elastic slacks, significantly reducing the computational cost of solving an $\ell_{1}$-relaxed QP as compared to carrying these as decision variables. In dual active-set methods, this reduces to a simple $[0,w]$ box constraint on the dual variables, with a corresponding update to the working-set solve to account for the saturated terms. We also provide an open-source, header-only C++/Eigen implementation of ElastiQP, along with Python and JAX interfaces, at

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-B Paper Organization", "weight": 1.0} -->

In Section II, we define the elastic QP and its key properties. Section III then introduces the elastic solver, and characterizes the differences from traditional active-set methods. In Section IV, we then study where conflicts arise in robotics problems, and how the solution to an elastic QP is well-suited to balance conflicts. Additionally, we extensively benchmark ElastiQP against other leading solvers on relevant feasible and infeasible robotics scenarios, and in Section V, on a broader suite of challenging problems.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The Elastic Quadratic Program", "weight": 1.0} -->

Fig. 2: When conflict between constraints is inevitable, what solution should be returned? Consider a 2D double-integrator robot which has been backed into a corner, with a dynamic obstacle moving towards it. Inherently, this leads to a conflict between three safety constraints: stay within the two boundaries of the workspace, and avoid collision with moving obstacle. In edge cases like this, we would prefer a solver which returns a reasonable balance between conflicts, rather than returning an infeasible status. Here, the balance can be set via the magnitude of the penalty terms, w. For wwall > wobs (left), the optimal action is to accept collision with the obstacle while avoiding the walls, whereas for wwall < wobs, the robot accepts violating the workspace boundary to avoid collision with the dynamic obstacle. In either case, when conflict occurs, the optimal dual z for the relaxed constraint reaches its corresponding cap w, allowing the elastic slack t to grow when the conflict is active.

<!-- chunk {"id": "body-0013", "role": "body", "section": "The Elastic Quadratic Program", "weight": 1.0} -->

Introducing multipliers $y\in\mathbb{R}^{m}$ for $Ax=b$, and $z_{t},z\in\mathbb{R}^{p}$ for $t\geq 0$ and $Gx-t\leq h$ respectively, stationarity in $t$ gives $w-z_{t}-z=0$, and yields two key properties: Bounded multipliers. At any optimum, $0\leq z\leq w$ elementwise, with $z_{t}=w-z$. The bound is the dual expression of the $\ell_{1}$ penalty: swapping the infinite wall of a hard constraint for a ramp of slope $w_{i}$ clips the corresponding multiplier from $[0,\infty)$ to $[0,w_{i}]$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "The Elastic Quadratic Program", "weight": 1.0} -->

Exactness. If the hard-constrained QP (with $t\equiv 0$ enforced) is feasible with an optimal inequality multiplier $z^{\star}$ satisfying $z^{\star}_{i}<w_{i}$ for all $i$, then every solution of has $t=0$ and its $x$ solves the hard-constrained QP \[15, Thm. 17.3\].

<!-- chunk {"id": "body-0015", "role": "body", "section": "The Elastic Quadratic Program", "weight": 1.0} -->

Exactness is what distinguishes this relaxation from generic soft constraints, which trade constraint satisfaction against the objective on every solve. When elastic constraints are compatible (and when the penalties $w$ are set greater than the optimal duals $z$), the relaxation has no impact on the optimal solution, and activates only under conflict.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Relaxation: Why $\\ell_{1}$ and not $\\ell_{2}$", "weight": 1.0} -->

When constraints do conflict, $\ell_{1}$ and $\ell_{2}$ relaxations differ considerably in how violations are distributed. The $\ell_{1}$ penalty is exact, with a sparse violation structure: only the constraints that cannot be jointly satisfied are relaxed, while all other constraints hold exactly. Whereas, a quadratic $\ell_{2}$ penalty is inexact and diffuse, spreading small violations across many constraints, even those that were not in conflict in the first place. Even on feasible problems, an $\ell_{2}$ relaxation can lead to small constraint violations, as the cost to violate these vanishes at zero.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Relaxation: Why $\\ell_{1}$ and not $\\ell_{2}$", "weight": 1.0} -->

Consider, for instance, a robot controller where the inequality terms encode both task and actuator limits. If the robot is operating at high speeds, a task constraint may be inconsistent with actuator limits (the robot cannot physically produce a torque that satisfies the task). In this setting, the desirable behavior is for only the task to be relaxed. With an $\ell_{1}$ structure, setting the per-constraint penalty values $w_{i}$ according to the desired relaxation hierarchy $w_{\text{task}}<w_{\text{actuator}}$ provides exactly this outcome. We further discuss and quantify the difference between an $\ell_{2}$-relaxed baseline in Section IV-D, and provide a visual example of constraint conflict in Fig. 2.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Equality constraints: Hard versus elastic", "weight": 1.0} -->

ElastiQP considers elastic inequalities with hard equalities, specifically to match the typical structure of robot control QPs. In these problems, equality terms typically encode dynamics and are consistent by construction, so the hardness assumption here retains the persistent feasibility benefits of the elastic inequalities. An alternative structure would be to similarly relax the dynamics equalities, encoding them as elastic rows with large penalties. However, this introduces additional concerns, the main being that the guarantee that the returned control is dynamically consistent is lost, despite these constraints never being the sole source of conflict. In our experiments, we find that by keeping these constraints hard, even when inequalities are in conflict, these terms hold to tight tolerance (Table IV).

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Equality constraints: Hard versus elastic", "weight": 1.0} -->

If, however, equality terms correspond to softer tasks which may be relaxed in the case of inconsistency, ElastiQP does support elastic equalities, via pairs of opposing elastic inequality constraints $\beta\leq a^{\top}x\leq\beta$ with corresponding penalty terms $w_{E}$. In general, this structure should be reserved only for the case where equalities may be soft, due to the additional cost imposed by adding two inequalities for every equality.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The Elastic Condensation", "weight": 1.0} -->

Before noting the adjustments required to make a reliable elastic solver, consider first a hard-constrained QP (equivalent to with the elastic slacks $t$ fixed at 0): | | $\displaystyle\min_{x}$ | $\displaystyle\tfrac{1}{2}x^{\top}Qx+q^{\top}x$ | | \(3\) | | | $\displaystyle\text{s.t.}$ | $\displaystyle Ax=b$ | | | A general-purpose QP solver which targets this problem structure can always solve the elastic problem by appending the elastic slacks $t$ to the primal variables $x$ as a new, expanded decision vector. This creates a problem with $n+p$ unknowns and $2p$ inequality constraints, leading to the most expensive part of the solver (factorizations) similarly growing as $p$ increases. In robot control, $p$ is typically several times $n$, and as such, adding elasticity in this expanded form significantly increases computational cost.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The Elastic Condensation", "weight": 1.0} -->

ElastiQP instead condenses the problem: $t$ is eliminated analytically, maintaining a constant $n\times n$ factorization size and strong solver performance even as $p\gg n$. Critically, we find that this condensation strategy is not unique to any one solver method: similar condensation strategies can be efficiently implemented across the three main families of QP solvers (interior point (IPM), augmented Lagrangian (ALM), and active set methods (ASM)).

<!-- chunk {"id": "body-0022", "role": "body", "section": "The Elastic Condensation", "weight": 1.0} -->

In short, the relationship between condensation strategies across solver families stems from Property 1: in each case, the inequality multipliers $z$ are restricted to $[0,w]$ as opposed to $[0,\infty)$. Whereas each hard-constrained solver (implicitly or explicitly) classifies an inequality as inactive or active, a condensed elastic solver introduces a new state, saturated.

<!-- chunk {"id": "body-0023", "role": "body", "section": "The Elastic Condensation", "weight": 1.0} -->

If, then, an efficient elastic condensation can be posed for each solver family, which of IPM/ALM/ASM is best-suited to the robot control domain? We find that active-set methods consistently outperform IPM and ALM for these problems, and as such, in the following subsection, we focus our discussion on the elastic condensation strategy for ASMs. However, we include the condensations for IPMs and ALMs in the Appendix, sections -A and -B: these strategies form the basis of our ElastiQP-IPM and ElastiQP-PDAL variants, which we evaluate in Section IV.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Preliminaries: Active-Set Methods", "weight": 1.0} -->

At the solution of, some inequality constraints are tight (holding with equality), and the rest are inactive. If the set of tight constraints, the active set, were known in advance, the inequalities could be dropped or converted to equalities, and the QP would reduce to an equality-constrained QP: one fast linear solve. An active-set method searches for this set. These methods maintain a working set, $\mathcal{W}$ (an estimate of the active set), solve the equality-constrained QP in which the constraints in $\mathcal{W}$ hold with equality, and use the result to revise $\mathcal{W}$. A constraint is added to $\mathcal{W}$ when the current iterate violates it, and removed when its multiplier is negative.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Preliminaries: Active-Set Methods", "weight": 1.0} -->

This method has good properties for robot control, particularly when considering warm-starting. Because each iteration changes $\mathcal{W}$ by one row, the factorization can be updated rather than fully recomputed, and the cost of a solve is proportional to the number of changes to the working set. When warm-starting from a previous solution in consecutive timesteps, the active set is generally quite stable, and the iteration count for the warm solve is only the number of constraints whose status (active/inactive) has changed. In control, this is often zero or one. Conversely, this same property can lead to long iteration times on a cold-start, where the number of updates to $\mathcal{W}$ is as large as the number of initial active constraints.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Preliminaries: Active-Set Methods", "weight": 1.0} -->

A primal active-set method maintains a primal-feasible iterate, which requires a feasible starting point, and iteratively adds a constraint to $\mathcal{W}$ when a step would otherwise violate it. A dual active-set method maintains a dual-feasible iterate instead, satisfying primal feasibility only at termination. Compared to primal methods, a dual ASM does not require a primal-feasible starting point, so when warm starting, the previous working set and multipliers can be reused without first restoring feasibility under the new data. Standard dual methods do require $Q\succ 0$ so that $x$ can be eliminated in closed-form, but this can be resolved with proximal point iterations to handle the semidefinite case.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Preliminaries: Active-Set Methods", "weight": 1.0} -->

Dual ASMs operate on the dual problem, | | $\displaystyle\max_{\lambda=[y;\,z]}$ | $\displaystyle-\tfrac{1}{2}\left\lVert M^{\top}\lambda\right\rVert^{2}-d^{\top}\lambda$ | | \(4\) | | | $\displaystyle\text{s.t.}$ | $\displaystyle z\geq 0$ | | | Here, we introduce the following intermediate terms: $C=[A;\,G]$ and $c=[b;\,h]$ are the stacked constraint terms, $R$ is a Cholesky factor of $Q$ (upper triangular with $R^{\top}R=Q$), $\lambda=[y;\,z]$ are the multipliers, and we have $M=CR^{-1}$, $v=R^{-\top}q$ and $d=c+Mv$, similarly to.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A Preliminaries: Active-Set Methods", "weight": 1.0} -->

A solution to the primal problem can be recovered from the dual optimum as Though is itself a QP, the constraints ($z\geq 0$) are simple to handle for an active-set method.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Preliminaries: Active-Set Methods", "weight": 1.0} -->

This yields an unconstrained problem whose maximizer is the solution of the linear system A full iteration of the dual ASM is, therefore: Compute the multipliers $\lambda^{\star}_{\mathcal{W}}$ that maximize the dual over the working set,.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Preliminaries: Active-Set Methods", "weight": 1.0} -->

If moving from the current multipliers to $\lambda^{\star}_{\mathcal{W}}$ would push one of them negative, stop at the first to reach zero, remove that index from $\mathcal{W}$, and go back to step 1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Preliminaries: Active-Set Methods", "weight": 1.0} -->

Otherwise accept $\lambda^{\star}_{\mathcal{W}}$, evaluate the constraints at $x(\lambda^{\star})$, and add the most violated row to $\mathcal{W}$. If none is violated, that point is optimal.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Preliminaries: Active-Set Methods", "weight": 1.0} -->

In the hard-constrained case, if the dual is unbounded, the primal is infeasible.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B An Elastic Condensation for Dual Active-Set Methods", "weight": 1.0} -->

An efficient implementation of the $\ell_{1}$-relaxed elastic form for dual ASMs is a single change to the dual problem: in addition to the non-negativity bound on the inequality multipliers $z$, we simply add an upper bound at the penalty values, $w$. then becomes | | $\displaystyle\max_{\lambda=[y;\,z]}$ | $\displaystyle-\tfrac{1}{2}\left\lVert M^{\top}\lambda\right\rVert^{2}-d^{\top}\lambda$ | | \(8\) | | | $\displaystyle\text{s.t.}$ | $\displaystyle 0\leq z\leq w$ | | | directly following from Property 1 (bounded multipliers).

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B An Elastic Condensation for Dual Active-Set Methods", "weight": 1.0} -->

To solve, this requires very small changes to the iteration, mainly, that we introduce a saturated set $\mathcal{S}$ containing the inequality constraint indices where $\lambda_{i}=w_{i}$. With this, the unconstrained problem of then becomes whose maximizer is the solution of the elastic linear system, An iteration of the elastic dual ASM is very similar to the non-elastic case: Compute the multipliers $\lambda^{\star}_{\mathcal{W}}$ that maximize the dual over the working set,.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B An Elastic Condensation for Dual Active-Set Methods", "weight": 1.0} -->

If moving from the current multipliers to $\lambda^{\star}_{\mathcal{W}}$ would push one of them out of the $[0,w_{i}]$ box, stop at the first to reach the bound, remove that index from $\mathcal{W}$, add it to $\mathcal{S}$ if it reached $w_{i}$, and go back to step 1.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B An Elastic Condensation for Dual Active-Set Methods", "weight": 1.0} -->

Otherwise accept $\lambda^{\star}_{\mathcal{W}}$ and evaluate the constraints at $x(\lambda^{\star})$. An index outside $\mathcal{W}$ is wrong if the corresponding constraint is inactive but violated, or saturated but strictly satisfied; add the constraint index that is wrong by the largest amount to $\mathcal{W}$. If no index is wrong, that point is optimal.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-B An Elastic Condensation for Dual Active-Set Methods", "weight": 1.0} -->

In short, in step 1 we replace, and in steps 2 and 3 we account for the saturated set $\mathcal{S}$ and the box bounds in the working set update.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-B An Elastic Condensation for Dual Active-Set Methods", "weight": 1.0} -->

In the elastic case, the dual can only become unbounded through the equality multipliers $y$, and thus the elastic dual ASM will always return a solution whenever the equality constraints are consistent (as they are in robot dynamics).

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-B An Elastic Condensation for Dual Active-Set Methods", "weight": 1.0} -->

Hence, given the natural incorporation of elasticity into dual ASMs, and the strong performance of DAQP on feasible robot problems, we build ElastiQP's core solver methods using DAQP as our primary reference. In the following section, we evaluate this choice against not only DAQP, but also equivalent strategies and solvers within the IPM and ALM families, to exhaustively validate and identify the best method for elastic robot control.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Robot Control", "weight": 1.0} -->

Two 6-DoF arms, rigid grasp 28-DoF humanoid, 2 foot contacts TABLE II: Robot Control Problem Structures (n variables, m equalities, p inequalities).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Robot Control", "weight": 1.0} -->

Feasible control loops Infeasible control loops ✗ No usable solution at any timestep; times reported are the average time to termination.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Robot Control", "weight": 1.0} -->

† Convergence or certification failures occurred on some but not all timesteps.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Robot Control", "weight": 1.0} -->

* qpax struggles to converge at ϵabs = 10−6. For these tests only, we run at qpax’s (looser) default tolerance of ϵabs = 10−5.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-A Problem Setup", "weight": 1.0} -->

Of the three problems, the simplest is the task-space inverse dynamics of a single 6-DoF arm. Here, we solve for the joint torques to achieve a given end-effector acceleration, with upper/lower limits on the joint velocities and torques. Next, we consider bimanual differential inverse kinematics with two 6-DoF arms, with an equality constraint between the end-effector motions mimicking a rigid grasp constraint, and upper/lower limits on the joint positions and velocities. This more than doubles the problem size compared to the single arm, and adds hard equality constraints to better evaluate the mixed hard/elastic setting. Our most challenging setting is humanoid whole-body control: for a 28-DoF humanoid robot with a floating root, we optimize over the generalized accelerations $\ddot{q}$ and the contact wrenches $f$ for each foot, assuming planar double-support contact. The equality constraints enforce the underactuated dynamics and contacts, and the inequalities handle the upper/lower limits on the joint velocities and torques, as well as the linearized wrench cones for the feet.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-A Problem Setup", "weight": 1.0} -->

Offline, for each problem, we pre-solve a 500-timestep closed-loop trajectory using Pinocchio for the kinematics and dynamics terms, and cache the resulting QP matrices at each timestep. Then, during benchmarking, we replay the cached QP sequence, allowing us to isolate the timing of the QP solve from the kinematics and dynamics computation, while maintaining a representative slowly-drifting control-loop setting. We also set the actuator limits such that for each problem, approximately 50% of the timesteps are constrained at the optimum, to ensure that both unconstrained and constrained states are represented in the timing. When constructing the infeasible timesteps, we take the feasible QP and tighten a single inequality constraint past what is admissible from the other constraints -- this also allows us to clearly observe if a solution violated more than the one necessary constraint.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-B Evaluation", "weight": 1.0} -->

For comparison, we evaluate ElastiQP against three leading solvers for the small, dense problem setting: DAQP, PIQP and ProxQP, as well as qpax, which implements an efficient condensed elastic mode similar to ElastiQP. Additionally, to properly evaluate "which family of solvers is best-suited to elastic robot control problems?", we compare ElastiQP's active set method against our own elastic PDAL and IPM variants (further detailed in the Appendix).

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B Evaluation", "weight": 1.0} -->

Across each of these solvers, we also consider five different formulations of the problem. Elastic indicates an $\ell_{1}$-relaxed inequality constraint structure with analytical condensation of the elastic slack variables: the main strategy of ElastiQP and of qpax's elastic form. Hard solves the standard hard-constrained problem, with no additional protection against infeasibility. Slack indicates an expanded $\ell_{1}$-relaxed form where both $x$ and $t$ are stacked into the decision vector, for persistent feasibility even when solved with a hard-constrained routine. Closest refers to ProxQP's closest-feasible mode, an $\ell_{2}$-relaxed problem form similar to DAQP's soft form. Finally, sparse indicates solving the expanded $\ell_{1}$ form with a sparse matrix backend (to potentially take advantage of the sparsity of elastic slacks). For solvers that support warm-starting (ElastiQP, DAQP, and ProxQP), we report timing values for both cold and warm solves.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-B Evaluation", "weight": 1.0} -->

All results were recorded on a laptop with an Intel Core Ultra 7 258V CPU, and (for C++ solvers) compiled with gcc 13.3 and -O3 optimization. Note that compiling with -march=native tends to give an additional $\sim 1.5\times$ performance gain on larger-scale problems, so the reported numbers are conservative. qpax is a purely JAX/Python library, and values reflect the JIT-compiled CPU performance using a recent JAX version (0.11.0), and double precision.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-C Feasible Control Loops", "weight": 1.0} -->

From Table III, ElastiQP demonstrates extremely fast (microsecond-level) performance on both feasible and infeasible domains, with even cold-started solves on the hardest infeasible problems (hum-wbc) falling comfortably below the 1 ms target required for 1 kHz control. Warm-starting reliably delivers an additional 2-4x in performance improvement on larger-scale problems, making ElastiQP the most reliable, always-feasible method for delivering high-frequency solves on challenging control problems.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-C Feasible Control Loops", "weight": 1.0} -->

In the strictly-feasible setting, DAQP is the fastest method for solving these problems, with ElastiQP following closely behind. Active set methods (such as DAQP or ElastiQP) perform very strongly in this setting on both cold and warm starts -- there are relatively few constraints active at the optimum (fast cold starts) and the active set is relatively stable across timesteps (fast warm starts). The additional handing for elasticity costs only a few microseconds at these problem scales; an acceptable trade for the reliability of an always-feasible method. The PDAL variants (ProxQP, ElastiQP-PDAL) also exhibit good warm-started performance, but fall behind the active-set variants, particularly on the smaller-scale problems.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-C Feasible Control Loops", "weight": 1.0} -->

Compared to the expanded slack form of DAQP, we can clearly see the benefits of ElastiQP's condensation (an improvement of over 40x). For ElastiQP's PDAL and IPM variants, the condensation improves performance by 10x and 20x, respectively, with this gap increasing to over 250x when looking at cold-started PDAL. ElastiQP is also 30-80x faster than qpax, our main elastic-condensed baseline.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-D Infeasible Control Loops", "weight": 1.0} -->

In the infeasible setting, ElastiQP dramatically outperforms all alternative solvers and strategies for posing the relaxed problem. As expected, standard hard-constrained solvers (DAQP, PIQP, ProxQP, and qpax's hard form) fail to solve an infeasible problem, and we note that reporting infeasibility can sometimes take a (dangerously) long time. Consider a warm-started controller, using ProxQP: if even a single timestep is momentarily infeasible, it could take upwards of 93 milliseconds to report infeasibility and manage this, compared to the nominal 1 millisecond budget.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-D Infeasible Control Loops", "weight": 1.0} -->

ProxQP's $\ell_{2}$-relaxed "closest-feasible" mode does report a solution, but not in a reasonable amount of time for control. Additionally, this $\ell_{2}$ mode exhibits the undesirable relaxation structure, as discussed in Section II-A and seen in Table IV. This mode results in small violations to 29 constraints when only 1 was in conflict, and no longer holds the equality constraints to tight tolerances, whereas all other $\ell_{1}$-based methods successfully achieve a minimally-relaxed problem. DAQP's soft $\ell_{2}$ returns a solution much faster than ProxQP's closest-feasible mode, and keeps equalities consistent, but at the cost of significantly higher $\ell_{1}$ violation than necessary.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-D Infeasible Control Loops", "weight": 1.0} -->

The second-best solver to ElastiQP in this setting is ProxQP's sparse backend, solving the expanded slack form, but only when warm-started. Even still, this method is not fast enough for reliable 1 kHz control on humanoid-scale problems, and is around 20-40x slower than ElastiQP. The other alternatives, ProxQP-slack and PIQP-slack, fall further behind in speed. qpax is unreliable at $10^{-6}$ precision, frequently failing to converge on these problems. Even after reducing the tolerance to $10^{-5}$, we still observe convergence failures on the harder biman-ik and hum-wbc problems, when constraint conflict appears. While qpax's elastic backend has previously demonstrated good performance on smaller, single-arm problems (see), it should not be relied on for larger control problems that may be momentarily infeasible.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Maros--Mészáros", "weight": 1.0} -->

Fig. 3: Maros–Mészáros performance profiles: 36-problem n ≤ 200 subset (left) and 107-problem n ≤ 10, 000 subset (right), ϵabs = 10−6. In settings well outside of the robotics domain, ElastiQP is competitive with the best general-purpose solvers, in both speed and reliability, even on the ill-conditioned, large, and sparse problems of this set.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Maros--Mészáros", "weight": 1.0} -->

While robot control is ElastiQP's primary focus, the Maros--Mészáros test set provides a complementary benchmark on poorly-scaled, challenging problems. The test set contains a wide range of problem sizes and sparsity, many of which are out of scope for a solver targeted towards small, dense problems. Despite this, we find it insightful to evaluate ElastiQP on these problems, to identify any potential robustness issues, to determine if the $\ell_{1}$ relaxation has led to noticeable performance reduction, and to identify trends between solver families (IPM, ALM, ASM). We divide our analysis into two subsets: the $n\leq 200$ subset allows us to compare performance on small-to-medium-sized ill-conditioned problems, while the $n\leq 10,000$ subset pushes the limits of our dense solver. As these problems are known to be feasible, for elastic solvers (ElastiQP, qpax), we set the penalties above the optimal dual required for the problem so that by exactness (Property 2) the elastic and hard solutions coincide.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Maros--Mészáros", "weight": 1.0} -->

As seen in Figure. 3, we see that (as anticipated) ElastiQP is not the best solver for these problems: DAQP wins on the smaller-scale set, while PIQP comfortably wins at larger scales. However, this test does reveal key properties of ElastiQP: most importantly, that the elastic condensation does not degrade the solver's performance for general-purpose problems. In both the small and large subsets, ElastiQP performs comparably to the best solvers, and ElastiQP even solves some problems that DAQP and ProxQP do not -- for instance, on the $n\leq 200$ subset, ProxQP reports a (premature) infeasible status on the QRECIPE problem. The only baseline that implements the condensed elastic form, qpax, trails significantly behind ElastiQP in both speed and reliability.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Additional Design Notes", "weight": 1.0} -->

When working with ElastiQP (and $\ell_{1}$ relaxations more broadly), the value of the elastic penalty, $w$, must be set by the user prior to solving the problem. By exactness (Property 2), if the problem is feasible and the penalty is greater than the optimal dual of the hard-constrained problem, then the hard solution will be recovered. This is the desired behavior for control: on feasible timesteps, the elastic relaxation should be effectively invisible. How then, should $w$ be set without a priori knowledge of the solution? arm-osc, biman-ik, hum-wbc TABLE V: Maximum Duals for Benchmark Problems In general, this will be problem-dependent, but the robot control problems from our benchmarks (Section IV) typically have very small duals, often $\leq 1$ (Table V). Empirically, we find that around $w=1e3$ is a reasonable default for control -- striking a balance between being sufficiently high to ensure there is no unnecessary relaxation, but not too high that it interferes with the numerical conditioning of the problem.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Additional Design Notes", "weight": 1.0} -->

Other problem domains may require higher penalties: within the Maros subset from Section V, 50% of the problems would be exact with a $1e3$ penalty, 89% with $1e6$, and the remainder requiring higher values. Very few problems (e.g. QPCBOEI2) had an optimal dual above $1e8$; above this value is where conditioning becomes a concern.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we have presented ElastiQP, a QP solver designed for robot control, with the implicit reliability of elastic, $\ell_{1}$-relaxed inequality constraints for times where persistent feasibility of the controller cannot be guaranteed. ElastiQP is intended for immediate integration into existing controllers and safety layers for robotics, providing reliable, fast solve times even when compute is limited, or when high-DoF robots necessitate larger, highly-constrained QPs. Initial work towards differentiability is in progress, with GPU acceleration for batched QP solves as the next step. In future work, we envision ElastiQP applied as a fast, elastic inner solver for SQP pipelines, particularly for global inverse kinematics and retargeting. The condensation can also be expanded to a block-sparse form, for incorporating elastic constraints into highly-structured MPC and trajectory optimization problems.
