<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Augmented Lagrangian Methods as Layered Control Architectures

Topics include Nonconvex optimization, Optimal control, Online algorithms, Planning, Control, Alternating-direction method of multipliers, Augmented Lagrangian method, Lagrange multiplier.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

For optimal control problems that involve planning and following a trajectory, two degree of freedom (2DOF) controllers are a ubiquitously used control architecture that decomposes the problem into a trajectory generation layer and a feedback control layer. However, despite the broad use and practical success of this layered control architecture, it remains a design choice that must be imposed a priori on the control policy. To address this gap, this paper seeks to initiate a principled study of the design of layered control architectures, with an initial focus on the 2DOF controller. We show that applying the Alternating Direction Method of Multipliers (ADMM) algorithm to solve a strategically rewritten optimal control problem results in solutions that are naturally layered, and composed of a trajectory generation layer and a feedback control layer. Furthermore, these layers are coupled via Lagrange multipliers that ensure dynamic feasibility of the planned trajectory. We instantiate this framework in the context of deterministic and stochastic linear optimal control problems, and show how our approach automatically yields a feedforward/feedback-based control policy that exactly solves the original problem. We then show that the simplicity of the resulting controller structure suggests natural heuristic algorithms for approximately solving nonlinear optimal control problems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We empirically demonstrate improved performance of these layered nonlinear optimal controllers as compared to iLQR, and highlight their flexibility by incorporating both convex and nonconvex constraints.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimal control has proven to be a key approach to solving problems across a wide range of fields, including economics, robotics, and communication systems. However, despite their significance, solving optimal control problems can be challenging due to nonlinear dynamics, high-dimensional state and control spaces, uncertainty, noise, and constraints. For optimal control problems that involve planning and following a trajectory, a ubiquitous *layered control architecture* \[1, Ch. 15\] commonly referred to as a *two degree of freedom (2DOF) controller* has emerged as the standard solution approach. This control architecture decomposes the problem into a trajectory generation layer, which generates the nominal trajectory the system should follow, and a feedback control layer, which corrects for errors between the actual system evolution and the planned trajectory. Indeed, this control architecture can be observed across linear control (feedforward/feedback control), robust model predictive control, and nonlinear control, and has led to significant practical impact across a wide variety of fields including robotics, power systems, communication networks, and biology.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We elaborate more on these different settings below, but highlight here that despite the ubiquity and practical success of the layered approach, this control structure does not emerge naturally from solving an optimal control problem, but rather must be imposed *a priori* on the control policy. To address this gap, we seek to initiate a principled study of the design of layered control architectures, with an initial focus on the 2DOF design pattern. Our starting point is the observation that Augmented Lagrangian-based optimization algorithms applied to optimal control problems can be naturally interpreted as two degree of freedom layered control architectures. We instantiate this observation in the context of linear and nonlinear optimal control problems, and show perhaps surprisingly that solutions obtained using the Alternating Direction Method of Multipliers (ADMM) algorithm to solve the original optimal control problem are naturally layered and composed of a trajectory generation layer and feedback control layer. In contrast to ad-hoc designs however, these two layers are coupled via Lagrange multipliers which ensure consistency between the planned trajectory and the tracking ability of the closed-loop feedback control layer.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Contributions:* This paper seeks to initiate the study of layered control architectures (LCAs) through the lens of optimization algorithms.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that strategically applying the ADMM algorithm to solve an optimal control problem results in a natural 2DOF layered control architecture composed of a trajectory generation layer and a feedback control layer. Importantly, the two layers are coupled via Lagrange multipliers that ensure dynamic feasibility of the planned trajectory.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the case of linear optimal control problems with convex but otherwise arbitrary cost functions, we show how this approach *automatically yields* a feedforward/feedback controller that exactly solves the original problem. We also show how this perspective allows us to seamlessly incorporate stochastic process noise into the problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the case of nonlinear optimal control problems, we exploit the structural simplicity of the resulting controller to propose a heuristic algorithm for *constrained nonlinear optimal control* that uses iLQR as a sub-routine. Although not the main focus of the paper, we emphasize the exciting possibilities that this novel perspective raises for nonlinear control design.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide empirical evaluations that demonstrate the benefits of layered control strategies in the context of nonlinear optimal control.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Related work---2DOF and Layered Control Architectures:* In linear control systems, 2DOF controllers decompose the control input into a feedforward term, which drives the system to the desired trajectory, and a feedback term, which compensates for errors. Analogous design patterns are observed in robust model predictive control (MPC). For example, tube-based MPC approaches broadly apply a control input of the form $u = {{K{({x - x_{d}})}} + u_{d}}$, where $(x_{d},u_{d})$ are nominal state and control inputs computed by solving an optimization problem online, and $K{({x - x_{d}})}$ is a feedback term compensating for errors between the actual system state $x$ and the reference state $x_{d}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

For nonlinear systems, trajectory generation and feedback control are typically decoupled, although approaches exist that do not explicitly make this separation, e.g., iLQR. A typical design pattern consists of generating a(n) (approximately) dynamically feasible and safe reference trajectory, e.g., by exploiting differential flatness or a reduced order model, and then applying locally stabilizing feedback control to ensure trajectory tracking, e.g., via linearization or control Lyapunov functions. Recent efforts from the robotics community show how to obtain "full-stack" safety/stability/performance guarantees for such layered architectures, see for example, by appropriately constraining planned trajectories to account for feedback control tracking error. In addition, work from formal methods solving discrete planning problems over continuous dynamics can be viewed as a layered approach, to solving a complementary planning and control problem. This body of work is exciting, as it treats layered control architectures as an object of study, and provides formal guarantees of correctness. We emphasize however that these papers impose the layered architecture *a priori*, and as such, do not address the question of how such layered architectures can be derived from first principles.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Related work---Theory of Layered Architectures:* Originally motivated by communication networks, the Layering as Optimization Decomposition (LAO) perspective has emerged as a promising quantitative theory of layered architectures. At a high-level, the LAO framework argues that layered architectures can be viewed as arising from a vertical decomposition of an optimization problem, wherein redundant variables are introduced across layers, and coordination enforced via Lagrange multipliers. LAO has been successfully applied to both communication and power systems, resulting in exciting breakthroughs in both fields. This work however focused on the solution of static optimization problems, e.g., Network Utility Maximization or Optimal Power Flow problems. To the best of our knowledge, the first extension of these ideas to optimal control problems can be found, where a LAO inspired relaxation is applied to a distributed linear optimal control problem in order to obtain a layered control architecture that approximately solves the original optimal control problem. A main contribution of this work was the *derivation* of a dynamics-aware trajectory planning layer, wherein the trajectory planning problem is augmented with a tracking penalty that characterizes the feedback control layer's ability to follow a given trajectory.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We then extend this approach to nonlinear systems, where we propose a data-driven approach to approximating the aforementioned tracking penalty for a fixed feedback controller. We note however that in both, layered architectures are only obtained by considering suitable *relaxations* of the original optimal control problem. In contrast, in this work we show how optimization algorithms used to directly solve the original problem can be interpreted as layered control architectures themselves.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Paper organization:* We show how ADMM applied to an optimal control problem results in a layered control architecture in Section 2. In Section 3, we instantiate our layered control architecture in the context of a deterministic and stochastic linear system. In Section 4, we discuss extensions to the nonlinear setting. We evaluate our proposed approach in several numerical examples in Section 5, and end with conclusions and future work in Section 6.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We consider the discrete-time finite-horizon optimal control problem (OCP) with initial condition $x_{0} = \xi$

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

While many approaches to solving OCP exist, our goal is to define a solution strategy which systematically generates 2DOF layered control architecture. Towards that end, we consider the equivalent OCP

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

obtained from through the introduction of a redundant "reference variable" ${\mathbf{r}} = {(r_{0},r_{1},\ldots,r_{N})}$ constrained to satisfy ${\mathbf{r}} = {\mathbf{x}}$. We now show how solving using ADMM naturally yields solutions with a 2DOF layered control architecture.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Alternating direction method of multipliers", "weight": 1.0} -->

The following is adapted. Consider the optimization problem

<!-- chunk {"id": "body-0020", "role": "body", "section": "Alternating direction method of multipliers", "weight": 1.0} -->

over the decision variables $r$ and $z$, with convex functions $f$ and $g$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Alternating direction method of multipliers", "weight": 1.0} -->

where $(r,z)$ are the primal variables, $v$ is the (scaled) dual variable associated with the equality constraint, and $\rho > 0$ is an algorithm parameter.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Alternating direction method of multipliers", "weight": 1.0} -->

Next, we describe the convergence properties of ADMM. Suppose optimization problem satisfies the two assumptions stated below, then the following theorem holds.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The standard Lagrangian for problem has a saddle point.

<!-- chunk {"id": "body-0024", "role": "body", "section": "ADMM yields 2DOF layered control architectures", "weight": 1.0} -->

The ADMM iterates, when instantiated on OCP, become

<!-- chunk {"id": "body-0025", "role": "body", "section": "ADMM yields 2DOF layered control architectures", "weight": 1.0} -->

where $\mathcal{R}^{N}:={\mathcal{R} \times \cdots \times \mathcal{R}}$ is the Cartesian product of the constraint set $\mathcal{R}$ over the time horizon $N$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "ADMM yields 2DOF layered control architectures", "weight": 1.0} -->

Trajectory generation layer (6a): The $\mathbf{r}$-update step (6a) is naturally interpreted as a trajectory generation layer, wherein an updated reference trajectory $\mathbf{r}$ is obtained by optimizing the utility cost $C_{x}{({\mathbf{r}})}$ subject to state constraints ${\mathbf{r}} \in \mathcal{R}^{N}$. While the reference trajectory is not explicitly constrained to be dynamically feasible a trust-region-like penalty $\frac{\rho}{2}{\|{{\mathbf{x}^{k} - \mathbf{r}} + \mathbf{v}^{k}}\|}_{2}^{2}$ arising from the augmented Lagrangian regularizes the reference trajectory to be approximately consistent with the current (dynamically feasible) state trajectory ${\mathbf{x}}^{k}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "ADMM yields 2DOF layered control architectures", "weight": 1.0} -->

Feedback control layer (6b): We immediately recognize the $({\mathbf{x}},{\mathbf{u}})$-update step (6b) as a reference tracking optimal control problem, with reference given by ${\mathbf{r}}^{k + 1} - {\mathbf{v}}^{k}$. Depending on the problem setting, exact or approximate optimal feedback controllers can be obtained to this update step.

<!-- chunk {"id": "body-0028", "role": "body", "section": "ADMM yields 2DOF layered control architectures", "weight": 1.0} -->

Dual update (6c): Finally, the dual variables $\mathbf{v}$ are updated according to equation (6c). We notice that the dual variable $\mathbf{v}$ can be seen as a protocol between the trajectory generation and feedback control layers that ensure that the planned reference trajectories converge to dynamically feasible behaviors (and vice versa).

<!-- chunk {"id": "body-0029", "role": "body", "section": "ADMM yields 2DOF layered control architectures", "weight": 1.0} -->

In the next sections, we instantiate this framework in the context of linear and nonlinear optimal control problems. For linear optimal control problems with convex costs, we show that the solution produced by the updates in is a 2DOF optimal controller with a trajectory generator along with feedforward and feedback control terms. For nonlinear optimal control problems, we show a natural separation between planning and control that isolates challenging lower-layer nonlinear feedback control from higher-layer trajectory generation and planning.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Layered Control Architectures for Linear Systems", "weight": 1.0} -->

In this section, we instantiate the ADMM updates in deterministic and stochastic linear OCPs, and show convergence to the optimal solution when the cost function is convex.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Deterministic linear system", "weight": 1.0} -->

We recognize that the feedback control layer update problem (7b) is an LQR reference tracking problem, with the reference trajectory $\mathbf{r}^{k + 1}$ which can be solved via dynamic programming. We first expand the square to isolate the tracking error term $x_{t} - r_{t}^{k + 1}$ to obtain the following OCP

<!-- chunk {"id": "body-0032", "role": "body", "section": "Deterministic linear system", "weight": 1.0} -->

for suitably defined matrices ${\overline{A}}_{t}$, ${\overline{B}}_{t}$, and $z_{0}$. This is a finite horizon LQR optimal control problem with quadratic and affine stage-wise cost terms, which can be solved by dynamic programming.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Deterministic linear system", "weight": 1.0} -->

We consider a cost-to-go function of the form

<!-- chunk {"id": "body-0034", "role": "body", "section": "Deterministic linear system", "weight": 1.0} -->

Plugging $v^{\star}$ into the cost-to-go function and simplifying further, we observe that the recursions for the matrices

<!-- chunk {"id": "body-0035", "role": "body", "section": "Deterministic linear system", "weight": 1.0} -->

follow the usual discrete Algebraic Riccati recursion, and

<!-- chunk {"id": "body-0036", "role": "body", "section": "Deterministic linear system", "weight": 1.0} -->

The optimal control action at time $t$ is then specified by $u_{t} = {{- {K_{t}z_{t}}} - \nu_{t}}$, which is further decomposed as

<!-- chunk {"id": "body-0037", "role": "body", "section": "Deterministic linear system", "weight": 1.0} -->

Feedforward term $K_{t}^{ff}\mu_{t}$: this term applies control actions to drive the system towards the desired reference trajectory, as encoded in the look-ahead state $\mu_{t} = {(r_{t}^{k + 1},\ldots,r_{N}^{k + 1},0,\ldots,0)}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Deterministic linear system", "weight": 1.0} -->

Feedback term $K_{t}^{fb}e_{t}$: this term stabilizes the system around the nominal trajectory by applying a feedback term based on the error $e_{t} = {({x_{t} - r_{t}^{k + 1}})}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Deterministic linear system", "weight": 1.0} -->

Coordination term $\nu_{t}$: The correction term $\nu_{t}$, which can be seen to be a linear function of the dual variable ${\mathbf{v}}^{k}$, coordinates the feedback layer behavior with that of planning layer, ensuring convergence to zero tracking error (i.e., that ${\mathbf{x}} = {\mathbf{r}}^{k + 1}$) as $k\rightarrow\infty$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Deterministic linear system", "weight": 1.0} -->

We emphasize that the 2DOF structure of the controller was not imposed a priori, and rather naturally emerged from the ADMM algorithm applied to solving OCP. Further, in contrast to prior work that relied on relaxing the original OCP, the 2DOF layered controller obtained here is optimal.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Deterministic linear system", "weight": 1.0} -->

Convergence: If $C_{x}$ is a closed, proper, and a convex function and $\mathcal{R}^{N}$ is a convex set, Assumption 1 is satisfied. Further, if the linear OCP satisfies strong duality, e.g., if Slater's condition holds, then Assumption 2 is satisfied. This is true, if for example, the state constraint $\mathcal{R}$ is a polytope, or if it contains the origin in its interior. It therefore follows by Theorem 1 ‣ 2.1 Alternating direction method of multipliers ‣ 2 Problem Formulation ‣ Augmented Lagrangian Methods as Layered Control Architectures") that residual, objective, and dual variable convergence are guaranteed.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Stochastic linear system with process noise", "weight": 1.0} -->

We extend the analysis of the previous section to stochastic linear systems of the form

<!-- chunk {"id": "body-0043", "role": "body", "section": "Stochastic linear system with process noise", "weight": 1.0} -->

where $w_{t} \sim {{\mathcal{N}{(0,I)}},{\forall t}}$ are i.i.d. zero mean Gaussian with identity covariance.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Stochastic linear system with process noise", "weight": 1.0} -->

We note that enforcing the constraint in expectation, i.e., ${{\mathbb{E}}_{w}x_{t}} \in \mathcal{R}$, could be replaced with suitable chance constraints or moment constraints, but we consider this form of stochastic OCP for simplicity. Prior to applying the approach of the previous section, we recall that due to linear superposition, the evolution of the stochastic dynamics can be decomposed into deterministic and zero-mean stochastic components, i.e., if we write

<!-- chunk {"id": "body-0045", "role": "body", "section": "Stochastic linear system with process noise", "weight": 1.0} -->

We now apply the approach of the previous section, but introduce redundant reference variables to track only the deterministic component of the dynamics, i.e.,

<!-- chunk {"id": "body-0046", "role": "body", "section": "Stochastic linear system with process noise", "weight": 1.0} -->

Applying ADMM to the deterministic component of the optimal control problem yields identical iterates to those found in equation, and the stochastic component reduces to a standard stochastic LQR problem with cost matrices $(C_{x},R)$. The resulting solution thus inherits the 2DOF layered architecture of the deterministic setting, with $u_{t}^{d}$ having the feedforward/feedback structure defined in equation (3.1), and $u_{t}^{s} = {- {K_{LQR}x_{t}^{s}}}$, for $K_{LQR}$ the standard LQR controller defined by the solution to the discrete Algebraic Riccati equation defined in terms of cost matrices $(C_{x},R)$ and dynamics $(A,B)$. Thus, by appropriately applying ADMM to solve stochastic OCP, we show that for quadratic state and control costs, a 2DOF layered control architecture with certainty equivalent trajectory generation and feedback control is optimal.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Low-order reference trajectories", "weight": 1.0} -->

In the above, we enforced that ${\mathbf{r}} = {\mathbf{x}}$, i.e., we introduced a reference trajectory of the same dimension as the original state. In practice, planning is often done using a lower-order reference trajectory such that $r_{t} = {Cx_{t}}$ for $C \in {\mathbb{R}}^{q \times n}$ with $q < n$. For example, in robotics applications, the state $x = {(q,\overset{˙}{q})}$ is composed of generalized coordinates and velocities, it is common to plan only in $r = q$ coordinates. This is trivially incorporated in the above framework by suitably modifying the redundant equality constraint to enforce ${\mathbf{r}} = {{\mathbf{C}}{\mathbf{x}}}$ and subsequently applying ADMM.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Input constraints", "weight": 1.0} -->

In the above, we did not consider constraints on the control input of the form $u_{t} \in \mathcal{U}$, for $\mathcal{U}$ a convex control input constraint set. We note however that by similarly introducing a redundant control action variable constrained to satisfy ${\mathbf{a}} = {\mathbf{u}}$, and enforcing that $a_{t} \in \mathcal{U}$ in the trajectory generation layer (6a) problem, now over decision variables $({\mathbf{r}},{\mathbf{a}})$, will ensure input constraint satisfaction.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Layered control architectures for nonlinear systems", "weight": 1.0} -->

We now revisit the general nonlinear OCP and corresponding ADMM iterate updates. If the cost functions $\mathcal{C}_{x}$ and $\mathcal{C}_{u}$, as well as the constraint set $\mathcal{R}$, are convex, then the only nonconvex component of the problem is the *unconstrained* nonlinear optimal control problem found in the feedback control layer (6b). By isolating the nonconvexity of the problem to this update step, we can leverage existing techniques from nonlinear optimization and optimal control to approximately solve this update step by applying e.g., iLQR, which is guaranteed to rapidly converge to a locally optimal solution under fairly benign assumptions.In the next section, we demonstrate the usefulness of this decoupling of unconstrained nonlinear optimal control and constrained planning by empirically demonstrating that our ADMM-based LCA converges to better solutions more reliably than vanilla iLQR.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Layered control architectures for nonlinear systems", "weight": 1.0} -->

We also show that the modularity of the approach enables more complex constraints, such as obstacle avoidance encoded via integer programming, to be seamlessly integrated into the trajectory generation layer subproblem (6a).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

In this section, we present experiments^22^2All code needed to reproduce these experiments can be found at on a $2 -$D linear system in both deterministic and stochastic settings and three nonlinear systems to evaluate our proposed methods. In all of the following, we use the $\rho$-update rule described in \[4, §3.4.1, equation (3.13)\] to improve convergence of the ADMM algorithm, and use cvxpy for solving the convex $\mathbf{r}$-update problems. For more details on experiment design, refer to Appendix A.

<!-- chunk {"id": "body-0052", "role": "body", "section": "2-D linear system", "weight": 1.0} -->

As shown in Figure 1(a) ‣ Figure 1 ‣ 5.1 2-D linear system ‣ 5 Numerical Examples ‣ Augmented Lagrangian Methods as Layered Control Architectures"), our approach recovers the optimal solution in the deterministic setting when $w_{t} = {0,{\forall t}}$. In the disturbance setting, our approach as shown in Figure 1(b) ‣ Figure 1 ‣ 5.1 2-D linear system ‣ 5 Numerical Examples ‣ Augmented Lagrangian Methods as Layered Control Architectures") recovers the deterministic solution and provides a feedback controller with feedforward and feedback structure. The feedback component from the controller stabilizes the system in the presence of disturbances. We emphasize that in the linear setting, the behavior of these controllers is expected, and hence no exhaustive evaluations or comparisons are necessary. It is rather the 2DOF structure that emerges as a property of the solution that is of interest here.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Nonlinear systems", "weight": 1.0} -->

To evaluate our proposed methods for nonlinear systems, we consider three case studies. The first task is the stabilization of pole dynamics on a moving cart, the second is the navigation of a non-holonomic car-like robot to a goal in the presence of corridor, input and nonconvex obstacle contraints and the last task is to navigate a quadrotor to a goal in 3D. In the following, we use the trajax implementation of iLQR. We reserve the term "convergence" if there is primal and dual feasibility from running our ADMM-based nonlinear LCA. We reserve the term "success rate" to measure the percentage of trials in which the terminal state from the executed trajectory reaches within a ball of radius $0.5$ from the goal. Refer to Appendix A for additional details on experiment design.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Nonlinear systems", "weight": 1.0} -->

Cartpole: We consider the stabilization task of the pole on a cart and compare the performance of our approach with iLQR.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Nonlinear systems", "weight": 1.0} -->

The system state is given by ${(q,\overset{˙}{q})} \in {\mathbb{R}}^{4}$ and the control input is the force applied to the cart in the horizontal direction. We apply Euler discretization to the continuous time system with sampling time ${dt} = 0.1$, and use the discrete-time dynamics for the rest of the evaluation.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Nonlinear systems", "weight": 1.0} -->

We apply the approach proposed in Section 4 using iLQR to solve the feedback control layer problem (6b) until the ADMM algorithm has converged. For the iLQR step in our ADMM algorithm, we set the maximum number of iterations to $10$, resulting in only approximate (locally optimal) solutions at each iterate update. To compare the performance of our approach, we run iLQR to stabilize the pole around the equilibrium point at $(0,\pi,0,0)$ with the maximum number of iterations set to $200$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Nonlinear systems", "weight": 1.0} -->

We sampled $20$ random initial conditions from a standard uniform distribution and tested our approach against iLQR over a horizon of $40$ time steps and report the results in Table 1. We note that our approach converged to the equilibrium point for every initial condition while iLQR successfully reaches within the goal radius only for $2$ out of $20$ trials. Qualitatively representative traces of an initial condition for which iLQR fails but our approach succeeds are found in Figs. 2(a) ‣ Figure 2 ‣ 5.2 Nonlinear systems ‣ 5 Numerical Examples ‣ Augmented Lagrangian Methods as Layered Control Architectures") and 2(b) ‣ Figure 2 ‣ 5.2 Nonlinear systems ‣ 5 Numerical Examples ‣ Augmented Lagrangian Methods as Layered Control Architectures"). We compute the total number of iterations for our approach as $\sum_{{it} = 1}^{K}{({1 + i_{it}})}$ where $K$ is the number of ADMM outer loops, and $i_{it}$ is the number of iLQR iterations per update step where $i_{it} \leq 10$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Nonlinear systems", "weight": 1.0} -->

We also count every $\mathbf{r}$-update step, and thus we are comparing the number of convex optimization oracle calls needed by each algorithm. As can be observed, the ADMM algorithm appears to demonstrate more favorable performance properties, but as expected, requires more iterations. We note however that we use a stopping criterion of primal residual error ${\|{{\mathbf{x}} - {\mathbf{r}}}\|}_{2}^{2} \leq 10^{- 2}$, but we observed that this can be substantially relaxed while still yielding acceptable solutions: we leave optimizing the algorithm for computational efficiency for future work.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Nonlinear systems", "weight": 1.0} -->

Unicycle: Next, we consider the navigation task of the continuous time unicycle dynamics given by

<!-- chunk {"id": "body-0060", "role": "body", "section": "Nonlinear systems", "weight": 1.0} -->

where ${(x_{1},x_{2})} \in {\mathbb{R}}^{2}$ are the system's Cartesian coordinates, $\theta$ is the heading angle, and $v$, $\omega$ are the instantaneous linear and angular velocities, respectively. We apply Euler discretization to the continuous time dynamical system for the rest of the evaluation as done previously for the cartpole. In addition to dynamics constraints, we include corridor constraints as state constraints and linear speed constraints as input constraints in the nonlinear optimal control problem.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Nonlinear systems", "weight": 1.0} -->

We apply our proposed approach from Section 4 using iLQR to solve the feedback control layer problem (6b) and set the maximum number of iterations to $10$. We compare the performance of our approach against iLQR solving the global nonlinear optimal control problem to navigate the car-like robot to a fixed goal at $$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Nonlinear systems", "weight": 1.0} -->

We sampled $20$ random initial conditions from a standard normal distribution and tested our approach against iLQR over a horizon of $20$ time steps. As discussed in Section 4, we repeat our experiments with lower order reference trajectories planned over $x,y$ positions, and include input constraints on maximum forward and reverse speeds while solving the trajectory generation layer (6a). Additionally, we also evaluated our approach by applying corridor state constraints by switching between affine constraints and also nonconvex obstacle constraints A in the planning layer (6a). We report the results in Table 2 for the different test cases. We note that our approach, in both cases with and without constraints, successfully reached the goal for every initial condition. In contrast, iLQR successfully reached within the goal radius only $4$ out of $20$ trials without state or input constraints. We show a qualitative comparison of our approach and iLQR in Figs.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Nonlinear systems", "weight": 1.0} -->

3(a) ‣ Figure 3 ‣ 5.2 Nonlinear systems ‣ 5 Numerical Examples ‣ Augmented Lagrangian Methods as Layered Control Architectures") and 3(b) ‣ Figure 3 ‣ 5.2 Nonlinear systems ‣ 5 Numerical Examples ‣ Augmented Lagrangian Methods as Layered Control Architectures") respectively where iLQR fails while our approach succeeds in reaching the goal. Next, we show our approach in Figs. 4 and 5(a) ‣ Figure 5 ‣ 5.2 Nonlinear systems ‣ 5 Numerical Examples ‣ Augmented Lagrangian Methods as Layered Control Architectures") finding a feasible path satisfying the non-holonomic behavior of the system, while bringing it to the goal in the presence of tight corridor constraints. In addition, we plot the reference and actual velocities in Fig. 5(b) ‣ Figure 5 ‣ 5.2 Nonlinear systems ‣ 5 Numerical Examples ‣ Augmented Lagrangian Methods as Layered Control Architectures") to show the satisfaction of input constraints.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Nonlinear systems", "weight": 1.0} -->

We do a similar computation of the total number of iterations as explained previously and plot the primal residual error for our approach as shown in Figs. 6(a) ‣ Figure 6 ‣ 5.2 Nonlinear systems ‣ 5 Numerical Examples ‣ Augmented Lagrangian Methods as Layered Control Architectures") and 6(b) ‣ Figure 6 ‣ 5.2 Nonlinear systems ‣ 5 Numerical Examples ‣ Augmented Lagrangian Methods as Layered Control Architectures"). Using a stopping criterion of primal residual error ${\|{{\mathbf{x}} - {\mathbf{r}}}\|}_{2}^{2} \leq 10^{- 2}$, we observed that our method converges in as few as $12$ ADMM outer-loop iterations when there are no state constraints and around $26$ iterations on average with corridor constraints.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Nonlinear systems", "weight": 1.0} -->

Ours (low order, corr., vel constr)

<!-- chunk {"id": "body-0066", "role": "body", "section": "Nonlinear systems", "weight": 1.0} -->

Quadrotor: Lastly, we consider the navigation task of a quadrotor to a goal with control-affine dynamics from \[24, Ch. 2\] where the quadrotor states are given by its position, velocity, roll, pitch, yaw and angular velocity in the world frame, and control inputs are given by the collective motor thrusts and body moment torques. Making a simplifying assumption that the angular body rates are equal to the angular velocity in the world frame leads to a control-affine system. We evaluate our proposed approach against iLQR to navigate the quadrotor to a fixed goal at $(3,2,1.5)$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Nonlinear systems", "weight": 1.0} -->

We simulate with a horizon of $20$ time steps by sampling $20$ initial conditions from a standard normal distribution. We report the results in Table 3 from running our approach on the full order and lower order(consisting of $x,y,z$ positions) reference trajectories. We note that iLQR failed to reach the goal for all initial conditions while our approach found a dynamically feasible trajectory to the goal for both the lower order and full order trajectory planning problems as shown in Figs. 7(a) ‣ Figure 7 ‣ 5.2 Nonlinear systems ‣ 5 Numerical Examples ‣ Augmented Lagrangian Methods as Layered Control Architectures") and 7(b) ‣ Figure 7 ‣ 5.2 Nonlinear systems ‣ 5 Numerical Examples ‣ Augmented Lagrangian Methods as Layered Control Architectures"). We leave optimizing our approach for computational efficiency and including state and input constraints from real hardware platforms for future work.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We showed that by introducing a redundant reference variable to an optimal control problem and subsequently applying ADMM, optimal controllers with a layered structure are obtained. We instantiated this approach in the context of linear optimal control problems, and recovered a feedforward/feedback-based optimal controller. In the context of nonlinear optimal control, we empirically demonstrated the benefits of separating trajectory generation from feedback control in terms of both convergence (as compared to vanilla iLQR) and flexibility (by seamlessly incorporating both convex and nonconvex constraints). Exciting directions of future work include developing convergence guarantees for the proposed nonlinear control scheme by making connections to the nonconvex ADMM literature, as well as considering alternative planning problems, such as those based on semantic specifications.
