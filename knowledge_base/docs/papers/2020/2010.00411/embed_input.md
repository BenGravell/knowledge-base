<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Feasibility-Driven Approach to Control-Limited DDP

Topics include Differential dynamic programming, Constrained optimization, Feasibility, Control limits, Legged robots.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces FDDP (Feasibility-Driven DDP) which enforces feasibility at each iteration rather than penalizing infeasibility, overcoming convergence issues in control-limited DDP.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Differential dynamic programming (DDP) is a direct single shooting method for trajectory optimization. Its efficiency derives from the exploitation of temporal structure (inherent to optimal control problems) and explicit roll-out/integration of the system dynamics. However, it suffers from numerical instability and, when compared to direct multiple shooting methods, it has limited initialization options (allows initialization of controls, but not of states) and lacks proper handling of control constraints. In this work, we tackle these issues with a feasibility-driven approach that regulates the dynamic feasibility during the numerical optimization and ensures control limits. Our feasibility search emulates the numerical resolution of a direct multiple shooting problem with only dynamics constraints. We show that our approach (named Box-FDDP) has better numerical convergence than Box-DDP (a single shooting method), and that its convergence rate and runtime performance are competitive with state-of-the-art direct transcription formulations solved using the interior point and active set algorithms available in Knitro. We further show that Box-FDDP decreases the dynamic feasibility error monotonically—as in state-of-the-art nonlinear programming algorithms. We demonstrate the benefits of our approach by generating complex and athletic motions for quadruped and humanoid robots.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, we highlight that Box-FDDP is suitable for model predictive control in legged robots.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Dynamic programming methods, which have their foundations in the calculus of variations as indirect methods, have once again attracted attention due to recent results on fast nonlinear model predictive control based on DDP (e.g., ). In particular, there is a significant interest in the iterative linear-quadratic regulator (iLQR) algorithm as its Gauss-Newton (GN) approximation reduces the computation time while having super-linear convergence. Both iLQR and DDP algorithms perform a Riccati sweep in the backward pass, which incorporates elements that are reminiscent of Pontryagin's maximum principle (PMP). For instance, at convergence, the gradient of the value function in the backward pass represents the costate; instead, the roll-out of the system dynamics describes the state integration step. This connection was recognized by Bellman's groundbreaking work that established the so-called Hamilton-Jacobi-Bellman (HJB) equation in the continuous-time domain. In contrast to classical direct collocation approaches, these approaches exploit the temporal/Markovian structure of the optimal control problem by solving a sequence of smaller sub-problems derived from Bellman's principle of optimality.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This leads to fast and cheap computations due to very small matrix factorizations and effective data cache accesses. Despite these advantages, both algorithms are unable to handle equality and inequality constraints efficiently. Furthermore, they have a poor basin of attraction for a good local optimum as it requires a good initialization in order to converge and are prone to numerical instability---commonly recognized challenges for single shooting approaches. These undesirable properties are mainly due to the fact that the iLQR/DDP algorithms implicitly enforce the dynamic feasibility through the system roll-out.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A Related work", "weight": 1.0} -->

Trade-offs between feasibility and optimality appear in most of the state-of-the-art nonlinear programming software. For instance, Ipopt includes a feasibility restoration phase which aims at reducing the constraint violation. In Knitro, the progress on both feasibility and optimality is achieved by adding an $\ell^{1}$-norm penalty term for the constraints in the merit function. In fact, by changing the merit function or the line search procedure, we can put emphasis on obtaining feasible solutions before trying to optimize them. Instead, the iLQR/DDP algorithms do not make this trade-off, as the backward and forward passes do not accept infeasible iterations. However, recent work on multiple shooting DDP has provided ways of handling dynamically infeasible iterations, which we elaborate below.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Related work", "weight": 1.0} -->

The multiple shooting variants in are rooted in dynamic programming. For instance, Giftthaler et al. introduced a lifted^11^1This name is coined, and we refer to gaps or defects produced between multiple shooting nodes. version of the algebraic Riccati equation that allows initialization of both state and control trajectories; it further accounts for the relinearization required by the dynamics gaps in the backward pass and uses a merit function to balance feasibility and optimality. In turn, in our previous work, we proposed a modification of the forward pass that numerically matches the gap contraction expected by a direct multiple shooting method subject to equality constraints only. It factorizes the KKT matrix via a Riccati recursion and defines the behavior of the defect constraints based on the first-order necessary condition (FONC) of optimality.^22^2For more details about the FONC of optimality see. These approaches improve numerical robustness against poor initialization, as they are able to use an initial guess for the state trajectory. Unfortunately, none of these methods handle inequality constraints such as control limits, with the exception of a recent work that computes squashed control sequences.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A Related work", "weight": 1.0} -->

There are two main strategies for incorporating arbitrary constraints: active set and penalization methods (as extensively described in ). In the robotics community, one of the first successful attempts to incorporate inequality constraints in DDP used an active set approach, which is based on -- a pioneering work in the control community. Concretely, this approach focused on handling control limits during the computation of the backward pass, i.e., in the minimization of the action-value function ($Q -$function),^33^3In the following section we formally describe the action-value function (i.e.,$Q -$function). which resembles the control Hamiltonian at convergence (see, Section 3.11). The method is popularly named Box-DDP, and the authors also showed a better convergence rate when compared with a squashing function approach. Later, Xie et al. included general inequality constraints into the $Q -$function and the forward pass. The method sacrifices the computational performance by including a second quadratic program, which is solved in the forward pass. However, it still remains faster than solving the same problem using direct collocation with Snopt as reported.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-A Related work", "weight": 1.0} -->

Generally speaking, active set methods are suitable for small-size problems (such as minimizing the $Q -$function described above) as their accuracy and speed often outperform other methods. However, the combinatorial complexity of finding the active set is prohibitive in large-scale optimization problems. This motivates the development of penalty-based methods, despite their numerical difficulties: ill-conditioning and slow convergence. To overcome these difficulties, Lantoine and Russell proposed a method that incorporates an augmented Lagrangian term. This method was studied in the context of robust thrust optimization, in which the dynamical system has fewer degrees of freedom compared to complex legged robots. Later, Howell et al. extended the augmented Lagrangian approach to handle arbitrary inequality constraints for aerial navigation and manipulation problems. Additionally, the algorithm incorporates an active set projection for solution polishing and is often faster than direct collocation solved with Ipopt or Snopt.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-A Related work", "weight": 1.0} -->

Our work proposes a feasibility-driven search for nonlinear optimal control problems with control limits. The main motivation of our approach is to increase the algorithm's basins of attraction, by focusing on feasibility instead of focusing solely on efficiency and optimality. Apart from the control limits and dynamics, we handle all remaining constraints (e.g., state and friction cone) through quadratic penalization, as described in the results section.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

The main contribution of this work is the first complete study of the numerical properties, behaviors, and guarantees of feasibility-driven search in differential dynamic programming. It relies on three technical contributions: an original and efficient optimal control algorithm that directly handles control limits (Box-FDDP), extensive comparisons against direct transcription and Box-DDP ^+^ (a single shooting method), a tutorial that connects the different branches of theory in optimal control, and an experimental validation of the dynamic feasibility evolution against interior point and active set algorithms for nonlinear programming.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

Our approach builds on top of our previous results on feasibility-driven search, for which we hereby propose to define two modes in our algorithm: feasibility-driven and control-bounded. It considers the dynamic feasibility in the forward pass and explicitly incorporates control limits, which does not require a merit function as. Additionally, our approach has outstanding numerical capabilities, which allow us to generate motions that go beyond state-of-the-art methods on optimal control or trajectory optimization in robotics, e.g., the athletic maneuver of a humanoid robot shown in Fig. 1.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Direct multiple shooting and differential dynamic programming", "weight": 1.0} -->

Before describing our approach, we introduce direct multiple shooting, and explain its numerical advantages when compared to single shooting methods such as DDP (Section II-A). Then, in Section II-B we present a unique tutorial that connects the various branches of theory: KKT, PMP, and HJB. Additionally, in Section II-C we describe the salient aspects of original Box-DDP proposed, and our variant Box-DDP ^+^. This section contains known material, although we believe it contributes (i) to unveil the underlying problems of differential dynamic programming, and (ii) to understand the theoretical foundations of our feasibility-driven approach.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Direct multiple shooting for optimal control", "weight": 1.0} -->

Eq. describes a nonlinear program as the system dynamics are transcribed into a set of algebraic equations with defects in each timestep. It is possible to extend this notation for cases where shooting segments contain multiple timesteps; however, as seen later, this does not provide any computational benefit, i.e., reduction in the computation time or better distribution of nonlinearities of the dynamics. Fig. 2 depicts the transcription process incorporating state and control trajectories $(\mathbf{x}_{s},\mathbf{u}_{s})$ as decision variables. This is in contrast to differential dynamic programming, which only transcribe the control sequence $\mathbf{u}_{s}$ and obtain $\mathbf{x}_{s}$ by integrating the system dynamics (i.e., a single shoot).

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A1 Numerical behavior of direct multiple shooting", "weight": 1.0} -->

Algorithms for nonlinear programming aim at finding the Karush-Kuhn-Tucker (KKT)conditions defined by the FONC of optimality. This process involves iteratively solving a KKT problem (i.e., linear system of equations) until satisfaction of a stopping criterion. In the line search strategy, the solution of this KKT problem provides a search direction $\delta\mathbf{w}_{k}$, and the selected step length $\alpha$ defines how much the current guess $\mathbf{w}_{k}$ moves along that direction, i.e., $\mathbf{w}_{k + 1} = {\mathbf{w}_{k} \oplus {\alpha\delta\mathbf{w}_{k}}}$. Note that the integrator operator $\oplus$ enables us to optimize over the manifold (as in ), however, it is a feature that general-purpose nonlinear programming libraries often does not have.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A1 Numerical behavior of direct multiple shooting", "weight": 1.0} -->

We can easily analyze the numerical behavior of direct multiple shooting formulations by focusing on the KKT problem for the shooting interval $k$ only. This is possible because of the temporal/Markovian structure of optimal control problems.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A1 Numerical behavior of direct multiple shooting", "weight": 1.0} -->

Therefore, when we apply the Newton method on this KKT sub-problem together with the Bellman's principle of optimality, we obtain: where Eq. defines the stationary condition (first and second rows) and the primal feasibility (third row) of the FONC of optimality, respectively; $\delta\mathbf{x}_{k}$, $\delta\mathbf{u}_{k}$ define the search direction for the primal variables; ${\mathbf{λ}}_{k + 1}^{+}$ is the updated Lagrangian multipliers; $\mathbf{\ell}_{\mathbf{x}_{k}}$, $\mathbf{\ell}_{\mathbf{u}_{k}}$, and $\mathbf{\ell}_{{\mathbf{x}\mathbf{x}}_{k}}$, $\mathbf{\ell}_{{\mathbf{x}\mathbf{u}}_{k}}$,

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A1 Numerical behavior of direct multiple shooting", "weight": 1.0} -->

$\mathbf{\ell}_{{\mathbf{u}\mathbf{u}}_{k}}$ are the Jacobians and Hessians of the cost function; $\mathbf{f}_{\mathbf{x}_{k}}$, $\mathbf{f}_{\mathbf{u}_{k}}$ are the Jacobians of the system dynamics; and $\mathcal{V}_{\mathbf{x}_{k}}$, $\mathcal{V}_{{\mathbf{x}\mathbf{x}}_{k}}$ are the gradient and Hessian of the value function. Note that we apply the Gauss-Newton (GN)approximation as we ignore the Hessian of the system dynamics to avoid expensive tensor-vector multiplications.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A1 Numerical behavior of direct multiple shooting", "weight": 1.0} -->

When we factorize this system of equations, the resulting search direction always satisfies the dynamics constraints if the Jacobians and Hessians are constant (i.e., a LQR problem). However, if we apply an $\alpha$-step, the gap of the dynamics closes by a factor of $({1 - \alpha})$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A1 Numerical behavior of direct multiple shooting", "weight": 1.0} -->

As described later in Section III, injecting this numerical behavior can be interpreted as a feasibility-driven approach for multiple shooting. However, our approach operates quite differently from classical multiple shooting approaches. For instance, it does not increase the computation time by defining extra state (decision) variables. But there is no such thing as a free lunch as our approach cannot temporarily increase the defects (e.g., to reduce the cost value) after taking its first full step ($\alpha = 1$).

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A2 Advantages of direct multiple shooting", "weight": 1.0} -->

The rationale for a direct multiple shooting approach (namely, adding $\mathbf{x}_{s}$ as decision variables) is to distribute the nonlinearities of the dynamics over the entire horizon. To illustrate this statement, we recognize that integrating over a horizon implies recursively calling integrator functions, i.e., | | | $=$ | $\mathbf{f}{({\mathbf{f}{(\mathbf{x}_{k - 1},\mathbf{u}_{k - 1})}},\mathbf{u}_{k})}$ | | | | | | $=$ | ${\mathbf{f}{({\mathbf{f}{({\cdots\mathbf{f}{(\mathbf{x}_{0},\mathbf{u}_{0})}},\mathbf{u}_{k - 1})}},\mathbf{u}_{k})}},$ | | | in which the nonlinearity increases along the horizon.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A2 Advantages of direct multiple shooting", "weight": 1.0} -->

This means that the local prediction, constructed by the derivatives of the nonlinear system in the KKT problem, becomes more inaccurate as the horizon increases. This is a well recognized drawback of single shooting approaches, and certainly a numerical limitation of the Box-DDP ^+^ algorithm described below.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Connection between KKT, PMP and HJB branches", "weight": 1.0} -->

The fourth row of Eq. connects the value function with the Lagrange multipliers associated with the state equations. By definition, this multiplier corresponds to the next costate value at node $k$, which reveals an interesting connection with the PMP used in indirect multiple shooting methods and the KKT approach, i.e.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B Connection between KKT, PMP and HJB branches", "weight": 1.0} -->

This might be not surprising if we realize that the PMP or KKT approach write the optimal control in term of the costate, while HJB expresses it in terms of the value function. Eq. is also at the heart of direct single shooting approaches such as DDP if each dynamics gap ${\overline{\mathbf{f}}}_{k + 1}$ vanishes, therefore this connection holds for single shooting settings as well.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B Connection between KKT, PMP and HJB branches", "weight": 1.0} -->

Different interpretations can arise from this connection. For instance, DDP or our approach can be interpreted as iterative methods for solving the PMP in discrete-time optimal control problems under single and multiple shooting settings, respectively. Furthermore, under the context of linear dynamics and quadratic cost, DDP or our approach can be classified as global methods as they compute an optimal policy (i.e., a closed-loop solution).

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-C1 Riccati sweep", "weight": 1.0} -->

The LQ approximation of the action-value function $Q_{k}$ is computed recursively, backwards in time, as follows where $\mathcal{V}_{\mathbf{x}_{k + 1}}$, $\mathcal{V}_{{\mathbf{x}\mathbf{x}}_{k + 1}}$ are obtained by solving the following algebraic Riccati equations at $k + 1$: with ${\hat{\mathbf{Q}}}_{{\mathbf{u}\mathbf{u}},\text{f}_{k + 1}}$ as the control Hessian in the free space, which we will describe below. Additionally, we use the gradient and Hessian of the value function to find a local search direction as described below.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-C1 Riccati sweep", "weight": 1.0} -->

In the case of Box-DDP ^+^, our adaptation of Box-DDP to allow initialization with state trajectories, the gradient of the value function in the first iteration is relinearized by the initialization infeasibility ${\overline{\mathbf{f}}}_{k + 1}^{0}$ as $\mathcal{V}_{\mathbf{x}_{k + 1}} + {\mathcal{V}_{{\mathbf{x}\mathbf{x}}_{k + 1}}{\overline{\mathbf{f}}}_{k + 1}^{0}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-C2 Control-bounded direction", "weight": 1.0} -->

With these indexes, we sort and partition the control Hessian as: and compute ${\hat{\mathbf{Q}}}_{{\mathbf{u}\mathbf{u}},\text{f}_{k}}^{- 1}$ internally based on the factorization of $\mathbf{Q}_{{\mathbf{u}\mathbf{u}},\text{f}_{k}}^{- 1}$. This is what our Box-QP program does to solve the feed-forward sub-problem efficiently via the Projected-Newton QP algorithm. This algorithm quickly identifies the active set and moves along the free subspace of the Newton step. It also has a similar computational cost to the unconstrained QP if the active set remains unchanged. Thus, the runtime performance is similar to the DDP algorithm. However, it requires a feasible initialization $\delta\mathbf{u}_{k}^{0}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-C2 Control-bounded direction", "weight": 1.0} -->

Again, by using a Projected-Newton QP algorithm, we further efficiently obtain the control Hessian of the free subspace $\mathbf{Q}_{{\mathbf{u}\mathbf{u}},\text{f}_{k}}^{- 1}$ as the algorithm computes it internally when it moves along the free subspace of the Newton step. With it, we compute a state feedback gain that generates corrections within the control limits. This is an important feature for controlling the robot as well as for rolling-out the nonlinear dynamics in the forward pass. For more details about the Projected-Newton QP algorithm see.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-C3 State integration", "weight": 1.0} -->

In any DDP algorithm such as Box-DDP, we perform a state integration using the locally-linear policy as where ${\hat{\mathbf{x}}}_{k}$, ${\hat{\mathbf{u}}}_{k}$ are the new state and control at node $k$ generated using a step length $\alpha$. The feedback gain helps to distribute the nonlinearities; however, as seen in the previous section, it does not resemble the numerical behavior described by the FONC of optimality in direct multiple shooting. This different numerical behavior stems from the state integration procedure closing the gaps, i.e., ${\overline{\mathbf{f}}}_{k} = \mathbf{0}$, ${\forall k} = {\{ 0,1,\cdots,N\}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-C4 Expected improvement", "weight": 1.0} -->

When solving the algebraic Riccati equations, we obtain the expected improvement as Below, we elaborate the proposed algorithm based on the aforementioned description.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Box-FDDP: a feasibility-driven approach for multiple shooting", "weight": 1.0} -->

We now introduce a novel algorithm that combines a feasibility-driven search (Section II-A) with an active set treatment of the control limits (Section II-C) named Box-FDDP. The Box-FDDP algorithm comprises two modes: feasibility-driven and control-bounded modes, one of which is chosen for a given iteration (Algorithm 1). The feasibility-driven^44^4Here, feasibility concerns the dynamics of the system, not the feasibility of other problem constraints. mode mimics the numerical resolution of a direct multiple shooting problem with only dynamics constraints when computing the search direction and step length (lines 1-1 and 1-1, respectively). This mode neglects the control limits of the system as its focuses on dynamic feasibility only. In contrast, the control-bounded mode projects the search direction onto the feasible control region whenever the dynamics constraint is feasible (line 1). In both modes, the applied controls in the forward pass are projected onto their feasible box (line 1), causing dynamically-infeasible iterations to reach the control box. With this strategy, our solver focuses on feasibility early, which increases its basins of attraction, and later on optimality.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Box-FDDP: a feasibility-driven approach for multiple shooting", "weight": 1.0} -->

Technical descriptions of both modes are elaborated in Sections III-A and III-B. Note that the existence of feasible descent directions are introduced later in Section III-C.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Box-FDDP: a feasibility-driven approach for multiple shooting", "weight": 1.0} -->

1compute LQ approximation of the cost and dynamics 2 if infeasible iterate then 3 compute the gaps, Eq. 6 update the feasibility-driven Q−function, Eq. (III-A2) 7 if infeasible iterate then 8 compute feasibility-driven direction, Eq. 11 project Box-QP warm start, Eq. 12 compute control-bounded direction, Eq. - 15 for $\alpha \in \left\{ 1,\frac{1}{2},\cdots,\frac{1}{2^{n}} \right\}$ do 17 project control onto the feasible box, Eq. 18 if infeasible iterate or α ≠ 1 then 19 update the gaps, Eq. 22 close the gaps, fk = 0 ∀k ∈ {0, ⋯, N − 1} 24 perform step, Eq. (III-B3) 26 compute the expected improvement, Eq. 27 if success step then Algorithm 1 Control-limited FDDP (Box-FDDP)

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A Search direction", "weight": 1.0} -->

In the standard Box-DDP algorithm, an initial forward pass is performed to obtain the initial state trajectory $\mathbf{x}_{s}$. This trajectory enforces the dynamics explicitly; thus, the gaps are zero, i.e., ${\overline{\mathbf{f}}}_{k} = \mathbf{0}$ for all $k = {\{ 0,1,\cdots,{N - 1}\}}$. Instead, our multiple shooting variant, Box-FDDP, computes the gaps once at each iteration (line 1), which are used to find the search direction and to compute the expected improvement. However, if the iteration is dynamically feasible, then the search direction procedure is the same as in the standard Box-DDP. Below, we describe the steps performed to compute the search direction.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A1 Computing the gaps", "weight": 1.0} -->

Given a current iterate $(\mathbf{x}_{s},\mathbf{u}_{s})$, we perform a nonlinear roll-out to compute the gaps as where $\mathbf{f}{(\mathbf{x}_{k},\mathbf{u}_{k})}$ is the roll-out state at interval $k + 1$, $\mathbf{x}_{k + 1}$ is the next shooting state, and $\ominus$ is the difference operator.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-A2 Action-value function of direct multiple shooting formulation", "weight": 1.0} -->

In direct multiple shooting settings, linearization of the system dynamics includes a drift term as there are gaps in the dynamics term ${\overline{\mathbf{f}}}_{k + 1}$ produced between subsequent shooting segments (q.v. Fig. 2). Then, the Riccati sweep needs to be adapted as follows: is the gradient of the value function after the deflection produced by ${\overline{\mathbf{f}}}_{k + 1}$ (also described above as relinearization). Note that the Hessian of the value function remains unchanged as DDP approximates the value function through a LQ model. Additionally, this modification affects the values of the Riccati equations, Eq., and expected improvement, Eq., as they depend on the gradient of the value function.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-A3 Feasibility-driven direction", "weight": 1.0} -->

Our approach is equivalent to opening the control bounds during dynamically-infeasible iterates.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-A4 Control-bounded direction", "weight": 1.0} -->

We warm-start the Box-QP using the feed-forward term $\mathbf{k}_{k}$ computed in the previous iteration. However, if the algorithm is switching from feasibility to control-bounded mode (i.e., the previous iteration is infeasible), then $\mathbf{k}_{k}$ might fall outside the feasible box and ${\underset{¯}{\mathbf{u}} - \mathbf{u}_{k}} \leq \mathbf{k}_{k} \leq {\overline{\mathbf{u}} - \mathbf{u}_{k}}$ do not hold. This violates the assumption of the previously-described Box-QP, for which a feasible initial point needs to be provided.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-A4 Control-bounded direction", "weight": 1.0} -->

To handle infeasible iterates, we propose to project the warm-start of the Box-QP (line 1) as where $\underset{¯}{\mathbf{u}}$, $\overline{\mathbf{u}}$ are the lower and upper bounds of the feed-forward sub-problem, Eq., respectively.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-A4 Control-bounded direction", "weight": 1.0} -->

Once we project the warm-start $\mathbf{k}_{k}$, we solve the feed-forward and feedback sub-problems as explained in Section II-C2. Furthermore, we solve the Box-QP using a Projected-Newton method, which handles box constraints efficiently as described above.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-B Step length", "weight": 1.0} -->

As far as we know, the standard Box-DDP modifies only the search direction (i.e., backward pass) to handle the control limits. However, it is also important to project the controls onto the feasible box during the forward pass. We do this by finding a step length that minimizes the cost.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-B1 Projecting the roll-out towards the feasible box", "weight": 1.0} -->

We propose to project the controls onto the feasible box in the nonlinear roll-out (line 1), i.e., where ${\hat{\mathbf{u}}}_{k}$ is the updated control from the control policy. Our method does not require to solve another QP problem or to project the linear search direction given the gaps on the dynamics. Furthermore, the control policy considers a gap prediction that guarantees a feasible descent direction. We formally describe the technical details of this procedure in Section III-B3.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-B2 Updating the gaps", "weight": 1.0} -->

As analyzed earlier, the evolution of the gaps in direct multiple shooting is affected by the selected step length. For an optimal control problem without control limits, this evolution is defined as where $\alpha$ is the step-length found by the line-search procedure (line 1-1). Note that a full step $({\alpha = 1})$ closes the gaps completely. We described this gap contraction rate in Section II-A1.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-B3 Nonlinear step", "weight": 1.0} -->

With a nonlinear roll-out^55^5In this work, a nonlinear roll-out is also referred to as a nonlinear step. (line 1), we avoid the linear prediction error of the dynamics that is typically handled by a merit function in general-purpose NLP algorithms, as explained. If we keep the gap-contraction rate of Eq., then we obtain where ${\hat{\mathbf{x}}}_{k}$, ${\hat{\mathbf{u}}}_{k}$ are the next state and control along an $\alpha$-step; $\mathbf{k}_{k}$ and $\mathbf{K}_{k}$ are the feed-forward term and feedback gains computed by Eq. or Eq. -.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-B3 Nonlinear step", "weight": 1.0} -->

Furthermore, the initial condition of the roll-out is defined as ${\hat{\mathbf{x}}}_{0} = {{\overset{\sim}{\mathbf{x}}}_{0} \oplus {{({\alpha - 1})}{\overline{\mathbf{f}}}_{0}}}$. Note that this is in contrast to the standard Box-DDP, in which the gaps are always closed, even for $\alpha < 1$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-B3 Nonlinear step", "weight": 1.0} -->

Avoiding the use of a merit function helps the algorithm to check the search direction more accurately. Indeed, it has been shown that the nonlinear roll-out is more effective than a standard line search procedure as it reduces the number of iterations.

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-B4 Expected improvement", "weight": 1.0} -->

It is critical to properly evaluate the success of a trial step. Given the current dynamics gaps ${\overline{\mathbf{f}}}_{k}$, Box-FDDP computes the expected improvement of a computed search direction as where ${\hat{\mathbf{Q}}}_{{\mathbf{u}\mathbf{u}},\text{f}_{k}}$ is the control Hessian of the free space, ${\delta{\hat{\mathbf{x}}}_{k}} = {{\hat{\mathbf{x}}}_{k} \ominus \mathbf{x}_{k}}$, and $J$ is the total cost of a given state-control trajectory ($\mathbf{x}_{s}$, $\mathbf{u}_{s}$). We use this expected improvement model for both modes. Note that, in the feasibility-driven mode, the free space spans the entire control space; instead, in the control-bounded mode, the gaps are zero.

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-B4 Expected improvement", "weight": 1.0} -->

We obtain this expression by computing the cost from a linear roll-out of the current control policy as described in Eq. (III-B3). We also accept ascent directions when evaluating the trial step, our approach is inspired by the Goldstein condition \[26, Chapter 3\]: where $b_{1}$, $b_{2}$ are adjustable parameters, we used in this paper $b_{1} = 0.1$ and $b_{2} = 2$. Ascent directions improve the algorithm convergence as it helps to reduce the feasibility error through a moderate increment in the cost.

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-B5 Regularization", "weight": 1.0} -->

We regularize the $\mathbf{Q}_{\mathbf{u}\mathbf{u}}$ and $\mathcal{V}_{\mathbf{x}\mathbf{x}}$ terms through a Levenberg-Marquardt scheme. Concretely, we increase the damping value $\mu$ when the computation of the feed-forward sub-problem---formulated in Eq. ---fails, or when the forward pass accepts a step length smaller than $\alpha_{0} = 0.01$. Moreover, we decrease the damping value if the iteration accepts a step larger than $\alpha_{1} = 0.5$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-B5 Regularization", "weight": 1.0} -->

Both regularization procedures modify the values of the $\mathbf{Q}_{\mathbf{u}\mathbf{u}}$ and $\mathcal{V}_{\mathbf{x}\mathbf{x}}$ terms during the Riccati sweep computation as where $\beta_{i}$ and $\beta_{d}$ are the factors^66^6 $\beta_{i,d}$ commonly range between $2$--$10$. We set $\beta_{i,d} = 10$ in this work. used to increase or decrease the current damping value $\mu$, respectively; $\mu'$ is the newly-computed damping value; and $\mathbf{I}$ is the identity matrix. Additionally, we start the regularization procedure with an initial, and user-defined, damping value.^77^7We use $10^{- 9}$ as the initial regularization value.

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-B5 Regularization", "weight": 1.0} -->

We also define minimum and maximum damping values to avoid increasing or decreasing the damping value unnecessarily.^88^8We use $10^{- 16}$ and $10^{12}$ as the minimum and maximum damping values, respectively. Note that $10^{- 16}$ is approximately the resolution of a double number.

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-B5 Regularization", "weight": 1.0} -->

Both regularizations significantly increase the robustness of the algorithm and ensures convergence, as it moves from Newton direction to steepest-descent, and vice versa. The Newton direction, which occurs with $\mu = 0$, provides fast convergence and is robust against scaling because it exploits the Hessian of the problem. However, it does not always produce valid descent directions as $\mathbf{Q}_{\mathbf{u}\mathbf{u}}$ might be indefine and the problem nonconvex. In such cases, increasing the damping value guarantees that $\mathbf{Q}_{\mathbf{u}\mathbf{u}}$ is positive-define which, in turn, computes a search direction closer to the steepest-descent one. Instead, $\mathcal{V}_{\mathbf{x}\mathbf{x}}$ enforces the state trajectory to be closer to the one previously computed. It will also not result in vanishing feedback gains even for large damping values.

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-C Existence of feasible descent directions", "weight": 1.0} -->

As described above, our approach has two main modes: feasibility-driven and control-bounded. During the feasibility-driven phase, we compute a search direction to drive the next guess towards dynamic feasibility and try a step while keeping the control within the box constraints. This projection procedure can be seen as a nonlinear term in our dynamics, but we assume its effect is negligible for finding a feasible direction. On the other hand, our algorithm computes a search direction that considers the box constraints after the dynamic feasibility has been achieved. This is needed to improve the next current guess by taking control constraints into account when computing the feedback gains along the free subspace.

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-C Existence of feasible descent directions", "weight": 1.0} -->

As analyzed in Section II-A1, the feasibility-driven direction is computed by mimicking the numerical behavior of a nonlinear program during the resolution of a direct multiple shooting problem with only dynamics constraints. It implies that the feasibility-driven search produces a descent direction, and eventually the algorithm converges, if the cost Hessian is a positive definite matrix. Indeed, the positiveness is always guaranteed by our regularization procedure as described before. Furthermore, the feasibility-driven step aims at reducing the nonlinearities produced by a single shooting formulation (e.g., DDP algorithm). When the dynamics are feasible, we apply a control-bounded search which also produces a descent direction as it boils down to a QP program.

<!-- chunk {"id": "body-0057", "role": "body", "section": "III-C Existence of feasible descent directions", "weight": 1.0} -->

In the next section, we present a series of results that demonstrate the benefits of our feasibility-driven approach.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Results", "weight": 1.0} -->

We analyze Box-FDDP across a wide range of optimal control problems (briefly introduced in Section IV-A) as follows. First, in Section IV-B, we show the benefits of the feasibility mode by analyzing the gap contraction and its connection with the nonlinearities in the dynamics. Second, we compare our algorithm against a direct transcription formulation in Section IV-D. Concretely, we compare the dynamic feasibility and optimality evolutions, runtime performance, and robustness to different initial guesses against the interior point and active set algorithms available in Knitro. Finally, in Section IV-E, we report the results of a squashing approach for solving the control bounds as it demonstrates the numerical performance of having two modes.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-A Optimal control problems", "weight": 1.0} -->

To provide empirical evidence on the benefits of the feasibility-driven approach, we developed a range of different optimal control problems: 1) an under-actuated double pendulum (pend); 2) a quadcopter navigating towards a goal (goal) or through a narrow passage (narrow) and looping (loop); 3) various gaits, aggressive jumps (jump) and unstable hopping (hop) in a quadruped robot; 4) whole-body manipulation (man), hand control while balancing in single leg (taichi), dip on parallel bars (dip) and a pull-up bar task (pullup) in a humanoid robot. Fig. 3 shows snapshots of motions computed by Box-FDDP for some of these problems, and the accompanying video shows the entire motion sequences.^99^9Supplementary video: We describe the cost functions, dynamics, control limits, penalization terms, and initialization of each optimal control problem in Appendix A. Finally, some of these problems, as well as our implementation of the Box-FDDP algorithm, are publicly available in the Crocoddyl repository.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-B Advantages of the feasibility-driven mode", "weight": 1.0} -->

To understand the benefits of the feasibility-driven mode, we analyze the resulting total cost, number of iterations and total computation time obtained in both algorithms: Box-FDDP and Box-DDP^+^ using the same initial guess. Box-DDP^+^ is an improved version of the standard Box-DDP proposed, which it accepts initialization for both: state and control trajectories as described above. This version accepts infeasible warm-starts as in Eq. (III-A2), and it is available in the Crocoddyl repository. Without this modification, the standard Box-DDP could easily diverge (and not converge at all) when we initialize it using quasi-static torques in problems with medium to longer horizons.

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-B1 Larger basin of attraction and convergence", "weight": 1.0} -->

In our experiments, Box-DDP^+^ was unable to generate jumping and hopping motions for quadrupeds, as well as pull-ups for humanoids, i.e., it failed to solve our jump, hop, and pullup task specifications (marked by the ✗ in Table I). Box-DDP^+^ failed to generate such aggressive motions because trajectories satisfying all the specifications of those tasks are significantly distant from the initial guess provided to the solver. Box-DDP^+^ behaves poorly as it computes solution with higher cost value and computation time, which is critical drawback in model predictive control applications.

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-B1 Larger basin of attraction and convergence", "weight": 1.0} -->

In contrast, our approach (Box-FDDP) was able to solve all of the tasks, and it did so with fewer iterations and lower total cost (see Table I and Fig. 4). Furthermore, Box-FDDP and Box-DDP^+^ have the same algorithmic complexity, but since our approach requires fewer iterations than Box-DDP^+^, the total computation time of our approach is lower. These results are a direct consequence of the feasibility-driven mode in our approach, which is able to find control sequences even when faced with poor initial guesses. The infeasible iterations ensure convergence from remote initial guesses through a balance between optimality and feasibility.

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-B1 Larger basin of attraction and convergence", "weight": 1.0} -->

Finally, we would like to emphasize that the feasibility-driven mode of Box-FDDP can not only solve tasks that Box-DDP^+^ is unable to solve, but also improve the solutions of tasks that Box-DDP^+^ is able to solve. For instance, consider the quadcopter tasks goal, narrow, and loop: In the accompanying video, we show that our approach generates concise and smooth quadcopter trajectories, whereas Box-DDP^+^ generates jerky motions and with unnecessary loops, due to early projection of the control commands.

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-B1 Larger basin of attraction and convergence", "weight": 1.0} -->

✗ algorithm does not find a solution. TABLE I: Number of iterations, total cost, and average total computation time over 100 trials.

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-B2 Gap contraction and nonlinearities", "weight": 1.0} -->

We observed that the gap contraction rate is highly influenced by the nonlinearities of the system dynamics (see Fig. 5). When compared to the dynamics, the nonlinearities of the task often have a smaller effect (e.g., dip vs pullup). Indeed, the gap contraction speed followed the order: humanoid, quadruped, double pendulum, and quadcopter.

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-B2 Gap contraction and nonlinearities", "weight": 1.0} -->

Propagation errors due to the dynamics linearization have an important effect on the algorithm progress as Riccati recursions maintain a local quadratic approximation of the value function. The prediction of the expected improvement is indeed more accurate for systems with less nonlinearities, which is the reason why the algorithm tends to accept larger steps that result in higher gap contractions. Indeed, the effect of having a feasibility search is more significant in problems with very nonlinear dynamics as it reduces the total cost faster due to the nonlinearity distribution motivated in Section II-A2 (see Fig. 4 and 5). It also produces a low cost reduction rate during the gap contraction phase as the algorithm is first focusing on achieving dynamic feasibility.

<!-- chunk {"id": "body-0067", "role": "body", "section": "IV-B3 Highly-dynamic and complex maneuvers", "weight": 1.0} -->

The Box-FDDP algorithm can solve a wide range of motions: from unstable and consecutive hops to aggressive and complex motor behaviors. In Fig. 6, we show the joint torques and velocities of a single leg for the ANYmal's jumping problem (depicted in Fig. 3c). The motion consisted of three phases: jumping ($0$--$300$ $ms$), flying ($300$--$700$ $ms$), and landing ($700$--$1000$ $ms$). We used $0.7$ as a friction coefficient and reduced the real joint limits of the ANYmal robot: from $40$ to $32$ $N\ m$ (torque limits) and from $15$ to $7.5$ $rad$/$s$ (velocity limits). Thus, generating a $30$ $cm$ jump becomes a very challenging task. Furthermore, in this experiment, the velocity limit violations appeared since we used quadratic penalization (with constant weights) to enforce them, and the swing phases are likely too short for such a large jump.

<!-- chunk {"id": "body-0068", "role": "body", "section": "IV-B3 Highly-dynamic and complex maneuvers", "weight": 1.0} -->

Note that if we use constant weights, it might turn out that, for some cases, these weights are not big enough. Nonetheless, we only encountered these violations in very constrained problems. For instance, we did not find velocity violations for the walking, trotting, pacing, and bounding gaits (reported in the accompanying video). For these cases, Box-FDDP converged approximately with the same number of iterations achieved by the FDDP solver (i.e., a fully unconstrained case). This is due to the fact that the robot could generate those gaits without reaching its torque limits.

<!-- chunk {"id": "body-0069", "role": "body", "section": "IV-B3 Highly-dynamic and complex maneuvers", "weight": 1.0} -->

Surprisingly, naturally looking behaviors emerged during the computation of the dip and pullup problems on the Talos humanoid robot. We did not include any heuristic that could have helped the algorithm to generate these undefined behaviors. For instance, the balancing and leg-crossing on the bars emerge if we allocate a significant amount of time in that motion phase. Similarly, the pull-up motion emerges if we significantly increase the maximum torque limits on the arms.

<!-- chunk {"id": "body-0070", "role": "body", "section": "IV-C Experimental trials", "weight": 1.0} -->

We demonstrated the capabilities of our Box-FDDP algorithm in a model predictive control application for the ANYmal C quadruped robot. The Box-FDDP algorithm computed reference motions in real-time and its efficiency enables our predictive controller to run in excess of $100\ {Hz}$ computation frequency with a horizon of $1.25\ s$. Fig. 7 shows snapshots of the forward trotting gait computed with the Box-FDDP algorithm. It also displays the contact-force tracking and updates of the swing-foot reference trajectories. In this experiment, we predefined the timings for the swing-feet motions and the foothold locations.

<!-- chunk {"id": "body-0071", "role": "body", "section": "IV-D Box-FDDP vs a direct transcription formulation", "weight": 1.0} -->

We formulated an efficient direct transcription problem with dynamics defects constraints in each node. The formulation is conceptually similar to our feasible descent direction introduced in Section III-C. We transcribed the dynamics using a symplectic Euler scheme, the same integration scheme also used in Box-FDDP. We solved the direct transcription problem using different optimization algorithms provided by Knitro. These available algorithms are: Interior/Direct, Interior/CG, active set and sequential quadratic programming (SQP) algorithms. Below we briefly describe each of Knitro's algorithms, and then report the comparison results with Box-FDDP.

<!-- chunk {"id": "body-0072", "role": "body", "section": "IV-D Box-FDDP vs a direct transcription formulation", "weight": 1.0} -->

The Interior/Direct (Knitro-IDIR) algorithm replaces the NLP problem with a series of barrier sub-problems. In each iteration, it solves the primal-dual KKT problem using a line search procedure.^1010^10For more details about interior point methods, the authors suggest the reader to see. Instead, Interior/CG (Knitro-ICG) solves the primal-dual KKT problem using a projected conjugate gradient method. This method uses exact second derivatives, without explicitly storing the Hessian matrix, through a tailored trust region procedure. Interior/Direct also invokes this trust region procedure if the line search iteration converges to a non-stationary point. In contrast to the interior point methods, the active set algorithm (Knitro-SLQP) replaces the NLP problem with a sequence of quadratic programs to form a sequential linear-quadratic programming algorithm. This algorithm selects a set of active constraints in each iteration, and produces a more exterior path (i.e., along the constraints) to the solution.

<!-- chunk {"id": "body-0073", "role": "body", "section": "IV-D Box-FDDP vs a direct transcription formulation", "weight": 1.0} -->

Finally, Knitro's SQP algorithm (Knitro-SQP) is also an active set method designed for small to medium scale problems with expensive function evaluations. Both active set approaches are often preferable to interior point methods on small- to medium-sized problems when we can provide a good initial guess. However, the problems in robotics are often large with many inequality constraints. Indeed, the benefits of interior point methods have been pointed out in the context of direct methods.

<!-- chunk {"id": "body-0074", "role": "body", "section": "IV-D1 Optimality vs feasibility", "weight": 1.0} -->

We compared the total cost, number of iterations, and total computation time against the different algorithms implemented in Knitro over 100 trials. For the comparison, we solved the double pendulum problem (pend), as it requires discovery of a swing-up maneuver. With this, we can clearly compare the trade-off between optimality and feasibility across the different algorithms. Note that, as described earlier, we used a single-thread for both Knitro and Box-FDDP despite our algorithm supporting multithreading.

<!-- chunk {"id": "body-0075", "role": "body", "section": "IV-D1 Optimality vs feasibility", "weight": 1.0} -->

Table II reports three different formulations used in the Knitro algorithms. The first one (pen) emulates exactly the optimal control formulation used in Box-FDDP, i.e., control constraints, regularization terms, and a terminal quadratic cost. The second case (regconst) uses a terminal constraint to impose the desired up-ward position together with the regularization terms. The third case (const) uses only the terminal constraints. Below we summarize the obtained results for each formulation.

<!-- chunk {"id": "body-0076", "role": "body", "section": "IV-D1 Optimality vs feasibility", "weight": 1.0} -->

Box-FDDP converges faster (w.r.t. time) than Knitro algorithms in all of the above formulations. However, Knitro-ICG is as fast as our approach with the const formulation. On the other hand, when it comes to optimality, Knitro produces more optimal solutions if we use the regconst formulation. Indeed, in our experience, Knitro generally has a better behavior when the formulation is dominated by constraint functions. Note that we do not report the cost values for the const formulation as this boils down to a feasibility problem, i.e., a problem with only constraints.

<!-- chunk {"id": "body-0077", "role": "body", "section": "IV-D1 Optimality vs feasibility", "weight": 1.0} -->

We used the regconst formulation to be able to compare both: cost and feasibility evolution. The dynamic infeasibility decreased monotonically for all the algorithms as plotted in Fig. 8 (top). Box-FDDP shows a fast resolution of the dynamics feasibility as interior point algorithms that, generally speaking, require fewer iterations than active set approaches. The cost evolution is also similar to the interior point algorithms, where the total costs are reported as regconst cases in Table II.

<!-- chunk {"id": "body-0078", "role": "body", "section": "IV-D2 Computation time", "weight": 1.0} -->

Box-FDDP had a better runtime performance than the Knitro algorithms for the double pendulum problem (cf. Table II). However, to answer the runtime performance scalability to higher-dimensional optimal control problems, we analyzed the problem of generating a forward jumping maneuver with the ANYmal robot (i.e., jump).

<!-- chunk {"id": "body-0079", "role": "body", "section": "IV-D2 Computation time", "weight": 1.0} -->

We used the same phase timings, joint limits and friction coefficient reported in Section IV-B3. The results reported with Knitro and Box-FDDP cases are based on slightly different optimal control formulations. The idea is to define the most suitable formulation for each algorithm. For instance, we use quadratic penalization terms to impose the desired foothold placement, joint velocity limits and friction cone constraints for the Box-FDDP algorithm. Instead, for the Knitro algorithms, we substitute these penalization terms by general equality and inequality constraints. To further reduce the computation time of Knitro cases, we also impose a constraint for the terminal position of the trunk. Note that we did not include any cost term since it negatively affects the convergence rate of Knitro, i.e., we treated it as a feasibility problem.

<!-- chunk {"id": "body-0080", "role": "body", "section": "IV-D2 Computation time", "weight": 1.0} -->

Table III reports the runtime performance over $100$ trials for the Knitro-IDIR algorithm only. The other methods (i.e., Knitro-ICG, Knitro-SLQP and Knitro-SQP) were unable to solve this problem. We used 5 different initial trunk heights, and we initialized the algorithms using their corresponding joint posture (as described in Appendix A-C) and no controls (i.e., $\mathbf{u}_{s}^{0} = {\{\mathbf{0},\cdots,\mathbf{0}\}}$). As in the double pendulum case, Box-FDDP also solved this problem faster than Knitro algorithms, even though it required a significant number of extra---computationally inexpensive---iterations. We suspect that this increment in the number of iterations is due to the use of penalization terms in the contact placement, friction cone and state limits constraints.

<!-- chunk {"id": "body-0081", "role": "body", "section": "IV-D3 Robustness against different initial guesses", "weight": 1.0} -->

We compared the robustness against different initial guesses for the double pendulum (pend) and quadrupedal jump (jump) problems. In both problems, we generated random joint postures---around the nominal state---and used them to define an initial guess for the state trajectory $\mathbf{x}_{\mathbf{s}}^{0}$. In addition to the robot's joint postures, we also generated random joint velocities around the zero-velocity condition for the double pendulum case only. We used this single random posture and velocity for each node in $\mathbf{x}_{\mathbf{s}}^{0}$, and initialized the control sequence with zeros. We used the most suitable formulations for Box-FDDP and Knitro algorithms as justified above.

<!-- chunk {"id": "body-0082", "role": "body", "section": "IV-D3 Robustness against different initial guesses", "weight": 1.0} -->

Table IV reports the number of successful resolutions over $100$ trials. We considered a problem to be successfully solved if the gradient of the Box-FDDP or the feasibility of the Knitro algorithms are lower than $5 \times 10^{- 5}$ (absolute feasibility tolerance). Note that this includes the cases where Knitro found a feasible approximate solution.^1111^11For further detail, we suggest the reader to consult the Knitro manual: Furthermore, we considered a problem resolution unsuccessful if the problem does not converge within $70\ s$, which is enough time as we can see above. For each problem, we used two different maximum values of the random initialization, which their maximum magnitude are described using the $\ell^{\infty}$ norm (i.e., $\parallel \cdot \parallel_{\infty}$). We added this additive noise to the default initial guess (described in Appendix A) used for the state trajectory.

<!-- chunk {"id": "body-0083", "role": "body", "section": "IV-D3 Robustness against different initial guesses", "weight": 1.0} -->

As expected, the Knitro interior point methods performed better than the active set ones. For the double pendulum problem, the interior point algorithms (i.e., Knitro-IDIR and Knitro-ICG) perform better than Box-FDDP if the warm-starting point is close to the initial condition. Despite that, Box-FDDP shows more robustness to initial guesses as its percentage of successful resolutions is consistent. Furthermore, we observed a significant increment in the number of successful resolutions for the jump problem. Indeed, Knitro was not able to solve this problem at all for random magnitudes bigger than ${\| 0.01\|}_{\infty}$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "IV-D3 Robustness against different initial guesses", "weight": 1.0} -->

✗ algorithm does not find a solution. TABLE IV: Percentage of successful resolutions from random initial guesses.

<!-- chunk {"id": "body-0085", "role": "body", "section": "IV-E Box-FDDP, Box-DDP, and squashing approach in nonlinear problems", "weight": 1.0} -->

To evaluate the numerical performance of having two modes, we compared the Box-FDDP (with two modes depending on the dynamics feasibility), Box-DDP^+^ (using a single mode) and DDP ^+^ with a squashing function (using a single mode) for three scenarios with the IRIS quadcopter: reaching goal (goal), looping maneuver (loop), and traversing a narrow passage (narrow). We used a sigmoidal element-wise squashing function of the form: in which the sigmoid is approximated through two smooth-abs functions, $\gamma$ defines its smoothness, and ${\underset{¯}{\mathbf{u}}}^{i}$, ${\overline{\mathbf{u}}}^{i}$ are the element-wise lower and upper control bounds, respectively.

<!-- chunk {"id": "body-0086", "role": "body", "section": "IV-E Box-FDDP, Box-DDP, and squashing approach in nonlinear problems", "weight": 1.0} -->

We introduced this squashing function on the system controls as: $\mathbf{x}_{k + 1} = {\mathbf{f}{(\mathbf{x}_{k},{\mathbf{s}{(\mathbf{u}_{k})}})}}$. We used $\gamma = 2$ for all the experiments presented in this section.

<!-- chunk {"id": "body-0087", "role": "body", "section": "IV-E Box-FDDP, Box-DDP, and squashing approach in nonlinear problems", "weight": 1.0} -->

Fig. 9 shows that Box-FDDP converged faster than the other approaches. As reported in the accompanying video, Box-FDDP did not generate undesired loops and jerky motions as in the other cases. Indeed, the solutions with Box-FDDP have the lowest cost values (cf. Table I). We also observed that the squashing approach often converges sooner compared to Box-DDP^+^. The main reason is due to the early saturation of the controls performed by Box-DDP^+^.

<!-- chunk {"id": "body-0088", "role": "body", "section": "IV-E Box-FDDP, Box-DDP, and squashing approach in nonlinear problems", "weight": 1.0} -->

In Fig. 10, we show the cost evolution for $10$ different initial configurations of the reaching goal task. The target and initial configurations are $$ and $({{- 0.3} \pm 0.6},0,0)$ $m$, respectively. Infeasible iterations, in Box-FDDP, produce a very low cost in the first iterations. The squashing approach is the most sensitive to initial conditions. However, on average, it produces slightly better solutions than Box-DDP^+^. This is in contrast to the reported results, where the performance was analyzed only for the linear-quadratic regulator problem.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We proposed a feasibility-driven approach whose search is primarily driven by the dynamics feasibility of the optimal control problem. The dynamically-infeasible iterations, which mimic a direct multiple shooting approach, allowed us to solve a wide range of optimal control problems despite it being provided with a poor initialization. The benefits of our approach are crystallized over a set of athletic and highly-dynamic maneuvers computed for the Talos humanoid and the ANYmal quadruped robots, respectively. Its improvement on the basin of attraction for a good local optimum has been a key factor to optimize such kind of complex maneuvers while considering the robot's full rigid body dynamics, joint limits and friction cone constraints. Indeed, Box-FDDP has shown an increment in the robustness against different initial guesses compared with advanced Knitro algorithms.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have provided evidence that our algorithm produces descent search directions. For instance, we have observed that the feasibility contraction decreases monotonically as often happens in the advanced nonlinear programming algorithms available in Knitro. Our approach has also shown to quickly reduce the dynamic infeasibility as observed in the most competitive Knitro algorithms. A similar effect is observed in the cost evolution as well. Our results suggest that the gap contraction rate is influenced by the nonlinearities of the system dynamics.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The runtime performance of Box-FDDP is often superior to direct transcription solved using state-of-the-art Knitro algorithms despite the increase in number of iterations due to the use of quadratic penalization terms. However, when comparing the computation time per iteration, our approach is between $2$ to $10$ times faster, which makes it suitable for model predictive control applications. Indeed, we demonstrated that our Box-FDDP algorithm can generate trotting gaits on the ANYmal C robot in a predictive control fashion. One additional remark is that we have not considered the runtime reduction due to code generation support in Crocoddyl via CppADCodeGen and CppAD. According to our experience, code generation can lead to a computation time reduction between ${30\ \%}\text{~to~}{60\ \%}$ as can be seen in our public benchmarks.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have developed and reported the results for a wide range of optimal control problems in robotics. These problems cover an important part of the spectrum of robotics applications. The comparison across all these problems is unusual, and it represents an important contribution to the research community since we have open sourced many of these examples, as well as the Box-FDDP algorithm, in the Crocoddyl repository. Our feasibility-driven approach enabled model predictive control applications on the ANYmal C robot, however, it can potentially be used in other applications such as in humanoid robotics, robot co-design, and learning.
