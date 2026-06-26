<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimizing Trajectories with Closed-Loop Dynamic SQP

Topics include Trajectory optimization, Sequential quadratic programming, Closed-loop, Nonlinear optimization, Robot control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces closed-loop dynamic SQP, which integrates feedback gain computation within the SQP iteration structure, improving robustness and convergence for trajectory optimization compared to open-loop sequential approaches.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Indirect trajectory optimization methods such as Differential Dynamic Programming (DDP) have found considerable success when only planning under dynamic feasibility constraints. Meanwhile, nonlinear programming (NLP) has been the state-of-the-art approach when faced with additional constraints (e.g., control bounds, obstacle avoidance). However, a naïve implementation of NLP algorithms, e.g., shooting-based sequential quadratic programming (SQP), may suffer from slow convergence - caused from natural instabilities of the underlying system manifesting as poor numerical stability within the optimization. Re-interpreting the DDP closed-loop rollout policy as a sensitivity-based correction to a second-order search direction, we demonstrate how to compute analogous closedloop policies (i.e., feedback gains) for constrained problems. Our key theoretical result introduces a novel dynamic programmingbased constraint-set recursion that augments the canonical “cost-to-go” backward pass. On the algorithmic front, we develop a hybrid-SQP algorithm incorporating DDP-style closedloop rollouts, enabled via efficient parallelized computation of the feedback gains.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, we validate our theoretical and algorithmic contributions on a set of increasingly challenging benchmarks, demonstrating significant improvements in convergence speed over standard open-loop SQP.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Trajectory optimization forms the backbone of model-based optimal control with myriad applications in robot mobility and manipulation. The problem formulation is as follows: consider a robotic system with state $x \in {\mathbb{R}}^{n}$, control input $u \in {\mathbb{R}}^{m}$, subject to the discrete-time dynamics: Let $N \in {\mathbb{N}}_{> 0}$ be some fixed planning horizon. Given some initial state $x_{0}$, the trajectory optimization problem is as follows: where we use $({\mathbf{u}},{\mathbf{x}})$ to denote the concatenations $(u_{0},\ldots,u_{N - 1})$ and $(x_{0},\ldots,x_{N})$, respectively.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We assume that the control constraint encodes simple box constraints: $\underset{¯}{u} \leq u_{k} \leq \overline{u}$, though, the results in this paper may be generalized beyond this assumption.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Solution methods generally fall into one of two approaches: optimal control-based (indirect methods), or optimization-based (direct methods). The former leverages necessary conditions of optimality for optimal control, such as dynamic programming (DP), while the latter treats the problem as a pure mathematical optimization program. A further sub-categorization of the direct method distinguishes between a *Full* or a *Condensed* formulation, where the former treats both the states and controls as optimization variables, subject to dynamics equality constraints, while the latter optimizes only over the control variables, with the dynamics implicit.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Lacking constraints beyond dynamic feasibility, ubiquitous indirect methods such as Differential Dynamic Programming (DDP) and its Gauss-Newton relaxation, iterative Linear Quadratic Regulator (iLQR) rely upon the DP recursion to split the full-horizon planning problem into a sequence of one-step optimizations, and alternate between a backward and forward pass through the time-steps. The backward pass recursively forms quadratic expansions of the optimal cost-to-go function and computes a time-varying affine perturbation policy that is subsequently rolled out through the system's dynamics in the forward pass to yield the updated trajectory iterate. Under mild assumptions, DDP locally achieves quadratic convergence, and the proof relies upon establishing the close link between DDP and the Newton method, as applied to the *condensed* optimization-based formulation. The stability properties of the underlying nonlinear system manifest as numerical stability during the optimization process, and hence the *closed-loop* nature of the forward pass in DDP typically leads to better performance than Newton's method, which implements *open-loop* rollouts.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Computing DDP-style closed-loop updates within the *constrained* setting (beyond dynamics feasibility) is much more challenging, since quadratization of the cost and linearization of the dynamics and constraints yields *constrained* quadratic programs (QPs) with *piecewise-affine* optimal perturbation policies, and complexity growing exponentially in the number of constraints and horizon of the problem. Consequently, direct methods (featuring open-loop updates) are the prevailing solution approach, typically combined with interior-point or SQP algorithms. Aside from possessing more variables, the direct formulation must additionally resolve dynamic feasibility, which can be non-trivial and lead to slower convergence even for unconstrained systems, as compared to indirect methods. Moreover, while the condensed formulation yields smaller problems, instabilities have been observed due to divergences between the predicted step from the linearized dynamics, and the open-loop nonlinear rollout, leading to vanishing step-sizes.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Re-interpreting the canonical DDP closed-loop rollout as a *sensitivity-based correction to a second-order search direction*, we demonstrate how to compute a locally affine approximation to the constrained perturbation policies, i.e., a set of feedback gains similar to those employed by the DDP rollouts. Our key theoretical result states that in the constrained setting, one must first compute an optimal perturbation sequence about the current trajectory iterate by solving a full-horizon QP (as opposed to the one-step DP backward recursion), and then augment the canonical cost-to-go backward pass with a constraint-set recursion. We then demonstrate how to approximate the desired feedback gains using an efficient, parallelized algorithm, eliminating the backward pass. The closed-loop rollout is integrated into an SQP line-search, yielding a hybrid indirect/direct algorithm that combines the theoretical foundations of SQP for constrained optimization with the algorithmic efficiencies of DDP-style forward rollouts. The method is rigorously evaluated within several environments, where we confirm significant convergence speed improvements over naïve (i.e., open-loop) SQP.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related Work: Quasi-DDP methods for constrained trajectory optimization fall into one of three main categories: control-bounds only modified backward pass via KKT analysis, and augmented Lagrangian methods. We provide a comprehensive overview of these approaches in Appendix A^11^1All appendices referenced herein may be found in the online version of this work..

<!-- chunk {"id": "body-0012", "role": "body", "section": "Shooting SQP", "weight": 1.0} -->

We detail below the core algorithmic steps for SQP, as applied to the shooting formulation of problem, i.e., where dynamics are treated implicitly and we optimize only over the control sequence $\mathbf{u}$. The three steps are: (i) solving a QP sub-problem to compute a search direction, i.e., a sequence of control perturbations ${{\mathbf{δ}}{\mathbf{u}}} = {({\deltau_{0}},\ldots,{\deltau_{N - 1}})}$, (ii) performing line-search along ${\mathbf{δ}}{\mathbf{u}}$ using a merit function, and (iii) monitoring termination conditions. We provide some details regarding (i) and (ii) here, and refer the reader to Appendices B and C for the rest.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Dynamic Programming SQP", "weight": 1.0} -->

Implicit within the line-search is the *open-loop* rollout along the search direction ${\mathbf{δ}}{\mathbf{u}}^{\ast}$, i.e., ${{\mathbf{x}}{\lbrack\alpha\rbrack}} = {{\mathbf{x}}{\lbrack{{\mathbf{u}} + {\alpha{\mathbf{δ}}{\mathbf{u}}^{\ast}}}\rbrack}}$. For unstable nonlinear systems, this state trajectory may differ significantly from ${\mathbf{x}} + {{\mathbf{δ}}{\mathbf{x}}^{\ast}}$, the "predicted" sequence from the QP sub-problem, forcing the line-search to take sub-optimal step-sizes and slowing convergence. This observation is corroborated in in context of comparing DDP and Newton methods for unconstrained problems, and within in the constrained context.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Dynamic Programming SQP", "weight": 1.0} -->

Our objective therefore, is to efficiently compute a set of feedback gains to perform DDP-style *closed-loop* rollouts within the SQP line-search. We hypothesize that such an enhancement will (i) improve the numerical stability of the line-search, and (ii) accelerate convergence of Shooting SQP. We first demonstrate how the classical DP recursion is ill-posed in the context of constrained trajectory optimization, and propose a correction inspired from sensitivity analysis.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Sensitivity-Based Dynamic Programming", "weight": 1.0} -->

The starting point for the derivation of iLQR and DDP algorithms for unconstrained problems is with the Bellman form of the optimal cost-to-go function: where $\pi_{k}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$ is a policy for time-step $k$, mapping states to controls.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Since $\delta{\breve{\pi}}_{k}^{\ast}{({\deltax_{k}})}$ is the solution of an unconstrained convex quadratic, the argument $0$ is redundant for the sensitivity matrix $K_{k}$. This will not be the case in the constrained setting.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Notice that since $\deltaV_{k + 1}$ is the optimal value of a *constrained* QP, $\delta\pi_{k}^{\ast}{}$ and the sensitivity matrix $\partial{{\delta\pi_{k}^{\ast}{}}/{\partial{\deltax_{k}}}}$ (paralleling the terms defined in ) may be *ill-defined*, for instance when the tail sub-problem is infeasible at ${\deltax_{k}} = 0$. This is a consequence of the linearized constraints, irrespective of the objective function used to define the DP recursion.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Instead, consider the following equivalent re-arrangement of the *unconstrained* DDP control law: where, the sequence $({{\mathbf{δ}}{\mathbf{x}}^{L}},{{\mathbf{δ}}{\mathbf{u}}^{L}})$ is defined by the rollout of $\delta{\breve{\pi}}_{k}^{\ast}$ via the linearized dynamics: In light of the homogeneity of the above recursion (i.e., the sequence $\alpha{\mathbf{δ}}{\mathbf{u}}^{L}$ rolled out via the linear dynamics yields $\alpha{\mathbf{δ}}{\mathbf{x}}^{L}$), eq.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 1", "weight": 1.0} -->

suggests interpreting ${\mathbf{δ}}{\mathbf{u}}^{L}$ as a *search-direction*, $\alpha{\mathbf{δ}}{\mathbf{u}}^{L}$ as the search step, and the feedback term as a sensitivity-based correction. Thus, we may interpret the DDP rollout as a *local sensitivity-based correction to the Newton search direction (${\mathbf{δ}}\mathbf{u}^{L}$)*. Generalizing this interpretation to the constrained setting, consider the following control law: where similarly to, ${\mathbf{δ}}{\mathbf{x}}^{L}$ is obtained from rolling-out ${\{{\delta\pi_{k}^{\ast}{({\deltax_{k}^{L}})}}\}}_{k = 0}^{N - 1}$ through the linearized dynamics.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Thus, the final control law for $\deltau_{k}{\lbrack\alpha\rbrack}$ becomes Given that $\delta\pi_{k}^{\ast}$, as defined, is implicitly the solution of a *variable-horizon* optimization, it is computationally prohibitive to compute the sensitivity matrices above via explicit differentiation. Instead, we next define a DP recursion to exactly compute these sensitivities about the *fixed* sequence ${\mathbf{δ}}{\mathbf{x}}^{\ast}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Since problem is a multi-parametric QP in $\deltax_{k}$, $\delta\pi_{k}^{\ast}$ is a piecewise-affine function of $\deltax_{k}$. Thus, for $\alpha = 1$, the expression inside the brackets in lies within $\delta\mathcal{U}_{k}$ only for $\deltax_{k}{\lbrack 1\rbrack}$ in a local region around $\deltax_{k}^{\ast}$, thereby necessitating the clipping operation (i.e., projection onto $\delta\mathcal{U}_{k}$).

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B DP Recursion for Computing Sensitivity Gains", "weight": 1.0} -->

We outline the DP recursion first and characterize its correctness in Theorem 1.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 3", "weight": 1.0} -->

A notable consequence of Theorem 1 is that the canonical cost-to-go recursion is ill-posed in the presence of constraints. One must back-propagate both the cost-to-go terms and a set of constraints (i.e., the sets $\{{\mathcal{C}\mathcal{R}_{k}}\}$) that define the regions where the quadratic models of the cost-to-go functions are precise.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Despite the exactness of the DP recursion, there are some computational drawbacks. First, one must solve both the "full-horizon" QP defined in and the one-step QPs defined, serially. Second, back-propagating sets $\{{\mathcal{C}\mathcal{R}_{k}}\}$ is not numerically robust, particularly if the sensitivity $K_{k}^{y}$ is ill-defined. This occurs when the LICQ condition fails and the resulting matrix solve computation for the sensitivities is singular. Thus, in the next section, we outline a parallelized and tuneable approximation to the sensitivity gains, derived from the viewpoint of interior point methods.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Approximating the Sensitivity Gains", "weight": 1.0} -->

For $k = {{N - 1},\ldots,0}$, define problem $\mathcal{P}_{k \multimap}{({\deltax})}$ as the tail portion of QP sub-problem, starting at time-step $k$ at $\deltax$. Let ${\mathbf{δ}}{\mathbf{u}}_{k \multimap}^{\ast}{({\deltax})}$ represent the optimal solution as a function of $\deltax$, i.e., the optimal control perturbation sequence starting at time-step $k$. Notice that $\delta\pi_{k}^{\ast}{({\deltax})}$, as defined, corresponds to the first element of the sequence ${\mathbf{δ}}{\mathbf{u}}_{k \multimap}^{\ast}{({\deltax})}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Approximating the Sensitivity Gains", "weight": 1.0} -->

Now define the QP problem $\mathcal{P}_{k}{({\deltax})}$ as QP sub-problem, subject to an *additional equality constraint*: ${\deltax_{k}} = {\deltax}$, and let ${\mathbf{δ}}{\mathbf{u}}_{k:}^{\ast}{({\deltax})}$ represent the optimal tail control perturbation sequence starting at time-step $k$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Approximating the Sensitivity Gains", "weight": 1.0} -->

Note the distinction: the sensitivity $\partial{{\delta{\hat{\pi}}_{k}^{\ast}}/{\partial{\deltax}}}$ corresponds to the Jacobian of the solution of a *fixed-horizon* QP (problem $\mathcal{P}_{k}{({\deltax})}$) w.r.t. a parameter ($\deltax$) that defines the equality constraint ${\deltax_{k}} = {\deltax}$. In comparison, the sensitivity $\partial{{\delta\pi_{k}^{\ast}}/{\partial{\deltax}}}$ corresponds to the Jacobian of the solution of a *variable-horizon* QP (problem $\mathcal{P}_{k \multimap}{({\deltax})}$) w.r.t. a parameter ($\deltax$) that defines the "initial condition." The former computation is easily parallelized.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-C Approximating the Sensitivity Gains", "weight": 1.0} -->

Leveraging a recent result, we approximate $\partial{{\delta{\hat{\pi}}_{k}^{\ast}{({\deltax_{k}^{\ast}})}}/{\partial{\deltax}}}$ by the Jacobian of the solution of the following unconstrained barrier re-formulation of problem $\mathcal{P}_{k}{({\deltax})}$ w.r.t. $\deltax$ at ${\deltax} = {\deltax_{k}^{\ast}}$: subject to the linear dynamics in (4b); where $\gamma > 0$ is the barrier constant. Denote $K_{k}^{u}{(\gamma)}$ to be the barrier-based Jacobian with parameter $\gamma$ and let $K_{k}^{u}$ be the true Jacobian.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Approximating the Sensitivity Gains", "weight": 1.0} -->

Under appropriate conditions on the solution of QP sub-problem, ${K_{k}^{u}{(\gamma)}}\rightarrow K_{k}^{u}$ as $\gamma\rightarrow 0$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C Approximating the Sensitivity Gains", "weight": 1.0} -->

Practically, we compute the Jacobians $K_{k}^{u}{(\gamma)}$ efficiently using iLQR and a straightforward application of the Implicit Function Theorem. We initialized the solver with the QP sub-problem solution ${\mathbf{δ}}{\mathbf{u}}^{\ast}$, and found only a handful of iterations were needed to converge, particularly since problem (III-C) is convex.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-D Hybrid SQP Algorithm", "weight": 1.0} -->

We formally state the Hybrid SQP algorithm as a line-search modification of Shooting SQP, introduced in Section II. Thus, at the current primal-dual iterate $({\mathbf{u}},{{\mathbf{x}}{\lbrack{\mathbf{u}}\rbrack}},{\mathbf{y}})$: *Step 1*: Solve QP-subproblem to obtain the optimal perturbation sequence pair $({{\mathbf{δ}}{\mathbf{u}}^{\ast}},{{\mathbf{δ}}{\mathbf{x}}^{\ast}})$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-D Hybrid SQP Algorithm", "weight": 1.0} -->

*Step 2*: Compute the sensitivity gains ${\{ K_{k}\}}_{k = 0}^{N - 1}$, using either the DP recursion in Section III-B (i.e., $K_{k} = K_{k}^{u}$), or the smoothed approximation method in Section III-C (i.e., $K_{k} = {K_{k}^{u}{(\gamma)}}$ for some $\gamma > 0$).

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-D Hybrid SQP Algorithm", "weight": 1.0} -->

*Step 3*: Perform line-search using, where ${{\mathbf{x}}{\lbrack\alpha\rbrack}}:={{\mathbf{x}} + {{\mathbf{δ}}{\mathbf{x}}{\lbrack\alpha\rbrack}}}$ is now defined by the *closed-loop* rollout: Notice that if $\alpha = 1$, the rollout corresponds with the ideal DDP rollout, while for $\alpha < 1$, we end up with an approximation^22^2As the sensitivity gains are only valid in a neighborhood of ${\mathbf{δ}}{\mathbf{x}}^{\ast}$, it is possible (though rare in our experiments) that the computed step-length $\alpha$ falls below the user-set threshold $\underset{¯}{\alpha}$ for a specific iteration.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-D Hybrid SQP Algorithm", "weight": 1.0} -->

As a backup, we compute a set of TV-LQR gains $\{ K_{k}^{lqr}\}$ using the linearized dynamics and the Hessian of the objective function $\mathcal{J}{({\mathbf{u}},{\mathbf{x}})}$, and perform the closed-loop rollout with these gains. This strategy is motivated by the goal of tracking the perturbation $\alpha{\mathbf{δ}}{\mathbf{x}}^{\ast}$ during the rollout. stemming from using a fixed gain matrix.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

We compare the naïve, open-loop, Shooting SQP implementation introduced in Section II (referred to as OL) with the DDP-style closed-loop variation developed in Section III (referred to as CL and $\text{CL}_{\gamma}$) on two environments. The identifiers CL and $\text{CL}_{\gamma}$ distinguish between the exact DP recursion and the smoothed barrier-based approximation for computing the forward rollout gains. Please see Appendix E for details regarding problem setup, SQP hyperparameters, additional plots, and an extra worked example.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Motion Planning for a Car", "weight": 1.0} -->

The first example is taken, featuring a 2D car ($n = 4$, $m = 2$) moving within the obstacle-ridden environment shown in Figure 2. The objective is to drive to the goal position $$ with final velocity $0$ and orientation aligned with the horizontal axis in $N = 40$ steps, while avoiding the obstacles.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Motion Planning for a Car", "weight": 1.0} -->

In Figure 3, we plot the re-construction error $\|{{\delta{\hat{\pi}}_{k}^{\ast}{({\deltax_{k}^{\ast}})}} - {\deltau_{k}^{\ast}}}\|$ for CL and $\text{CL}_{\gamma}$ over the course of the SQP iterations. Observe that for most iterations, the error is negligible for CL, with occasional spikes resulting from the numerical instability of the *constrained* DP recursion. In contrast, the error remains sufficiently low for *all* iterations of $\text{CL}_{\gamma}$, even leading to a better quality (lower objective) solution for Case #2. We hypothesize that the better numerical stability of $\text{CL}_{\gamma}$ stems from a *smoothing* of the computed Jacobians (i.e., feedback gains), courtesy of the unconstrained barrier re-formulation.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Motion Planning for a Car", "weight": 1.0} -->

Finally, a notable advantage of $\text{CL}_{\gamma}$ over CL is the computation time. While CL involves differentiating through the KKT conditions of one-step horizon QPs, this computation must happen serially in the backward pass. In contrast, $\text{CL}_{\gamma}$ computes the required Jacobians across all time-steps in parallel using an efficient adjoint recursion associated with problem (III-C). Consequently, the computation times-*per iteration* are much closer together for OL and $\text{CL}_{\gamma}$ than for OL and CL. For the remaining experiments, we only compare OL and $\text{CL}_{\gamma}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Quad-Pendulum", "weight": 1.0} -->

Consider a quadrotor with an attached pendulum ($n = 8$, $m = 2$) moving within an obstacle-cluttered 2D vertical plane, subject to viscous friction at the pendulum joint. The system is subject to operational constraints on the state and control input, as well as obstacle avoidance constraints. The task involves planning a trajectory starting at rest with the pendulum at the stable equilibrium, to a goal location, with the pendulum upright and both quadrotor and pendulum stationary. Table II provides the solver statistics for $\text{CL}_{\gamma}$ and OL (up until the algorithm stalls due to infeasibility of the QP sub-problem). Figure 1 shows a timelapse of the solution for the more difficult of the two cases, highlighting the ability of $\text{CL}_{\gamma}$ in solving challenging planning tasks.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this work, we re-interpret DDP rollout policies from a perspective of sensitivity-based corrections, and use this insight to develop algorithms for computing analogous policies for constrained problems. We incorporate the resulting closed-loop rollouts within a shooting-based SQP framework, and demonstrate significant improvements in convergence speed over a standard SQP implementation using open-loop rollouts.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Our work opens several avenues for future research. First, a key bottleneck of SQP involves solving the QP sub-problem at each iteration to compute a "nominal" perturbation sequence. This may be achieved with fast, but potentially, less-accurate unconstrained solvers (e.g., augmented-Lagrangian iLQR), that additionally compute the desired sensitivity gains using an efficient Riccati recursion. Second, leveraging recent results on differentiating through the solution of *general* convex problems, the sensitivity-based computations may be applied to the sequential-*convex*-programming algorithm. Finally, while the SQP algorithm was studied in the shooting context, recent work has demonstrated how to incorporate nonlinear rollouts with both states and controls as optimization variables, albeit in an otherwise unconstrained setting. The sensitivity-based gain computation can be extended to this setting, potentially boosting the efficiency of "full" direct methods.
