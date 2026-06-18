<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control

Topics include Trajectory optimization, Differential dynamic programming, Multi-contact, Legged robots, Optimal control, Feasibility-driven differential dynamic programming, Open source.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces Crocoddyl, an open-source multi-contact trajectory optimization library built on Feasibility-driven DDP (FDDP). FDDP accepts infeasible initial trajectories and keeps shooting gaps open during early iterations, achieving faster convergence and higher reliability than standard DDP for legged robot tasks.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce Crocoddyl (Contact RObot COntrol by Differential DYnamic Library), an open-source framework tailored for efficient multi-contact optimal control. Crocoddyl efficiently computes the state trajectory and the control policy for a given predefined sequence of contacts. Its efficiency is due to the use of sparse analytical derivatives, exploitation of the problem structure, and data sharing. It employs differential geometry to properly describe the state of any geometrical system, e.g. floating-base systems. Additionally, we propose a novel optimal control algorithm called Feasibility-driven Differential Dynamic Programming (FDDP). Our method does not add extra decision variables which often increases the computation time per iteration due to factorization. FDDP shows a greater globalization strategy compared to classical Differential Dynamic Programming (DDP) algorithms. Concretely, we propose two modifications to the classical DDP algorithm. First, the backward pass accepts infeasible state-control trajectories. Second, the rollout keeps the gaps open during the early "exploratory" iterations (as expected in multiple-shooting methods with only equality constraints). We showcase the performance of our framework using different tasks.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

With our method, we can compute highly-dynamic maneuvers (e.g. jumping, front-flip) within few milliseconds.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multi-contact optimal control promises to generate whole-body motions and control policies that allow legged robots to robustly react to unexpected events in real-time. It has several advantages compared with state-of-the-art frameworks (e.g. ) in which a whole-body controller (e.g. ) compliantly tracks an optimized Centroidal dynamics trajectory (e.g. ) with optionally an optimized contact plan (e.g. ). For instance, they cannot properly handle the robot orientation, particularly during flight phases due to the nonholonomic effect on the dynamics, and to regulate the angular momentum to zero leads to tracking errors even in walking motions. Furthermore, it is well-known that instantaneous time-invariant control (i.e. instantaneous whole-body control) cannot properly track nonholonomic systems. Indeed, in our previous work, we have shown that whole-body planning produces more efficient motions, with lower forces and impacts.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent work on optimal control has shown that nonlinear Model Predictive Control (MPC) is plausible for controlling legged robots in real-time. All these methods have in common that they solve the nonlinear Optimal Control (OC) problem by iteratively building and solving a Linear-Quadratic Regulator (LQR) problem (i.e. DDP with Gauss-Newton approximation ). These frameworks use numerical or automatic differentiation which is often inefficient compared to sparse and analytical derivatives. Furthermore, they do not explicitly handle the geometric structure of legged systems which include elements of ${\mathbb{S}}{\mathbb{E}}{}$. DDP has proven to efficiently solve nonlinear OC problems due to its intrinsic sparse structure. However, it has poor globalization strategy and struggles to handle infeasible warm-start^11^1An infeasible warm-start refers to state and control trajectories that are not consistent with the system dynamics.. In this vein, Giftthaler et al. proposed a variant of the DDP algorithm for multiple-shooting OC, which has a better convergence rate than DDP.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nonetheless, the gap contraction rate does not numerically match the Karush-Kuhn-Tucker (KKT) problem applied to the multiple-shooting formulation with only equality constraints. In this work, we address these drawbacks by computing highly-dynamic maneuvers as shown in Fig. 1.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Contribution", "weight": 1.0} -->

We propose a novel and efficient framework for multi-contact OC called Crocoddyl. Our framework efficiently solves this problem by employing sparse and analytical derivatives of the contact and impulse dynamics. The OC solver properly handles the geometry of rigid bodies using dedicated numerical routines for Lie groups and their derivatives. Indeed, we model the floating-base as a ${\mathbb{S}}{\mathbb{E}}{}$ element, needed for example for the generation of front-flip motions. Additionally, we propose a variant of the DDP algorithm that matches the behavior of the Newton method applied to the KKT conditions of a direct multiple-shooting formulation with only equality constraints. Our algorithm is called Feasibility-driven Differential Dynamic Programming (FDDP)^22^2We also refer as feasibility-prone DDP. as it handles infeasible guesses that occur whenever there is a gap between subsequent nodes in the trajectory. FDDP has a greater globalization strategy compared to classical DDP, allowing us to solve complex maneuvers in few iterations.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Multi-contact Optimal Control", "weight": 1.0} -->

In this section, we first introduce the multi-contact optimal control problem for multibody systems under physical constraints (Section II-A). We simplify the problem by modeling contacts as holonomic constraints (Section II-B). With this method, we derive tailored analytical and sparse derivatives for fast computation. The calculation of derivatives typically represents the main computation carried out by optimal control solvers.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Formulation of the optimal control problem", "weight": 1.0} -->

We focus on an efficient formulation of the multi-contact optimal control problem.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Formulation of the optimal control problem", "weight": 1.0} -->

where the state $\mathbf{x} = {(\mathbf{q},\mathbf{v})} \in X$ lies on a differential manifold formed by the configuration point $\mathbf{q}$ and its tangent vector $\mathbf{v}$ and is described by a $n_{x}$-tuple, the control $\mathbf{u} = {({\mathbf{τ}},{\mathbf{λ}})} \in {\mathbb{R}}^{n_{u}}$ composed by input torque commands $\mathbf{τ}$ and contact forces $\mathbf{λ}$, $\overset{˙}{\mathbf{x}} \in {T_{\mathbf{x}}X}$ lies in the tangent space of the state manifold and it is described by a $n_{dx}$-tuple, and $\mathcal{X}$, $\mathcal{U}$ represent the state and control admissible sets, respectively,

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Formulation of the optimal control problem", "weight": 1.0} -->

${\overset{˙}{\mathbf{v}}}_{free}$ is the unconstrained acceleration in generalized coordinates, and $\mathbf{M}$ is the joint-space inertia matrix.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Formulation of the optimal control problem", "weight": 1.0} -->

This problem can be seen as a bilevel optimization, where the lower-level optimization uses the Gauss principle of least constraint to describe the physical constraints as described. State and control admissible sets can belong to the lower-level optimization (e.g., joint limits and force friction constraints) as well as to the upper-level one (e.g., task-related constraints and collision with the environment).

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Contacts as holonomic constraints", "weight": 1.0} -->

To solve this optimization problem in real-time, we need to efficiently handle (a) the high-dimensionality of the search-space and (b) the instabilities, discontinuities, and non-convexity of the system dynamics (lower-level optimization), among others. One way of reducing the complexity of the OC problem is by solving the lower-level optimization analytically, e.g.. Indeed, we have implemented the contact model using holonomic scleronomic constraints on the frame placement (i.e.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Contacts as holonomic constraints", "weight": 1.0} -->

where $\mathbf{J}_{c}$ is expressed in the local frame, and $\mathbf{a}_{0} \in {\mathbb{R}}^{n_{f}}$ is the desired acceleration in the constraint space. Eq. allows us to express the contact forces in terms of the state and torques, and it has a unique solution if $\mathbf{J}_{c}$ is full-rank.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Contacts as holonomic constraints", "weight": 1.0} -->

where $\mathbf{v}_{\lambda{(c)}}$, $\mathbf{a}_{\lambda{(c)}}$ are the spatial velocity and acceleration at the parent body of the contact $\lambda{(c)}$, respectively, $\alpha$ and $\beta$ are the stabilization gains, and ${{}_{}^{}{}_{\lambda{(c)}}^{ref}} \ominus^{o}M_{\lambda{(c)}}$ is the ${\mathbb{S}}{\mathbb{E}}{}$ inverse composition between the reference contact placement and the current one.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Contacts as holonomic constraints", "weight": 1.0} -->

As Eq. neglects the friction-cone constraints and the joint limits, the dynamics describe an equality constraint and we can use an unconstrained DDP solver. Nonetheless, inequality constraints can still be included in DDP-like solvers, i.e. using penalization, active-set, or Augmented Lagrangian strategy.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B1 Efficient rollout and derivative computation", "weight": 1.0} -->

We do not need to invert the entire KKT matrix in Eq. during the numerical integration of the dynamics.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B1 Efficient rollout and derivative computation", "weight": 1.0} -->

If we analytically derive Eq. by applying the chain rule, then we can describe the Jacobians of $\mathbf{y}{( \cdot )}$ and $\mathbf{g}{( \cdot )}$ with respect to the derivatives of the Recursive Newton-Euler Algorithm (RNEA) algorithm and kinematics, i.e.:

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B1 Efficient rollout and derivative computation", "weight": 1.0} -->

where $\frac{\partial{\mathbf{τ}}}{\partial\mathbf{x}}$, $\frac{\partial{\mathbf{τ}}}{\partial\mathbf{u}}$ are the RNEA derivatives, and $\frac{\partial\mathbf{a}_{0}}{\partial\mathbf{x}}$, $\frac{\partial\mathbf{a}_{0}}{\partial\mathbf{u}}$ are the kinematics derivatives of the frame acceleration. We use a LDU decomposition to invert the blockwise matrix^33^3Note that this is the KKT matrix. in Eq..

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B2 Impulse dynamics", "weight": 1.0} -->

We can similarly describe the impulse dynamics of a multibody system^44^4Transitions from non-contact to contact condition.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B2 Impulse dynamics", "weight": 1.0} -->

where $e \in {\lbrack 0,1\rbrack}$ is the restitution coefficient that considers compression / expansion, $\mathbf{\Lambda}$ is the contact impulse and, $\mathbf{v}^{-}$ and $\mathbf{v}^{+}$ are the discontinuous changes in the generalized velocity (i.e., velocity before and after impact, respectively). Perfect inelastic collision produces a contact velocity equal to zero, i.e., $e = 0$. Similarly, we use the Cholesky decomposition to efficiently compute the impulse dynamics and its derivatives.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Feasibility-prone Differential Dynamic Programming", "weight": 1.0} -->

In this section, we describe our novel solver for multiple-shooting OC called Feasibility-driven Differential Dynamic Programming (FDDP). First, we briefly describe the DDP algorithm (Section III-A). Then, we analyze the numerical behavior of classical multiple-shooting methods (Section III-B). With this in mind, we propose a modification of the forward and the backward passes in Section III-C and III-D, respectively. Finally, we propose a new model for the expected reduction cost and line-search procedure based on the Goldstein condition (Section III-E).

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Differential dynamic programming", "weight": 1.0} -->

DDP belongs to the family of OC and indirect trajectory optimization methods. It locally approximates the optimal flow (i.e., the Value function) around $({\delta\mathbf{x}_{k}},{\delta\mathbf{u}_{k}})$ as

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Differential dynamic programming", "weight": 1.0} -->

which breaks the OC problem into a sequence of simpler subproblems by using "Bellman's principle of optimality", i.e.:

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Differential dynamic programming", "weight": 1.0} -->

Note that $l_{k}{( \cdot )}$, $\mathbf{f}_{k}{( \cdot )}$ are the Linear Quadratic (LQ) approximation of the cost and dynamics functions, respectively; $\delta\mathbf{x}_{k}$, $\delta\mathbf{u}_{k}$ reflects the fact that we linearize the problem around a guess $(\mathbf{x}_{k}^{i},\mathbf{u}_{k}^{i})$. This remark is particularly important to understand our FDDP algorithm and to deal with the geometric structure of dynamical systems^55^5The configuration point lies on a manifold $Q$ (e.g., a Lie group) and the system derivatives lies in its tangent space. (e.g. using symplectic integrators ).

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Differential dynamic programming", "weight": 1.0} -->

The $\mathbf{Q}_{\ast \ast}$ terms represent the LQ approximation of the control Hamiltonian function $\mathbf{H}{( \cdot )}$. The solution of the entire OC problem is computed through the Riccati recursion formed by sequentially solving Eq.. This procedure provides the feed-forward term $\mathbf{k}_{k}$ and feedback gains $\mathbf{K}_{k}$ at each discretization point $k$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B The role of gaps in multiple-shooting", "weight": 1.0} -->

The multiple-shooting OC formulation introduces intermediate states $\mathbf{x}_{k}$ (i.e., shooting nodes) as additional decision variables to the numerical optimization problem with extra equality constraints that attend to close the gaps^66^6It is also called defects in multiple-shooting literature., i.e.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B The role of gaps in multiple-shooting", "weight": 1.0} -->

where ${\overline{\mathbf{f}}}_{k + 1}$ represents the gap in the dynamics, $\mathbf{f}{(\mathbf{x}_{k},\mathbf{u}_{k})}$ is the rollout state at interval $k + 1$, and $\mathbf{x}_{k + 1}$ is the next shooting state (decision variable). For the remainder of this paper, we assume that there is a shooting node for each integration step along the trajectory.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B The role of gaps in multiple-shooting", "weight": 1.0} -->

By approaching the direct multiple-shooting formulation as a Sequential Quadratic Programming (SQP) problem, one can describe a single Quadratic Programming (QP) iteration as

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B The role of gaps in multiple-shooting", "weight": 1.0} -->

where the SQP sequentially builds and solves a single QP problem until it reaches the convergence criteria. The solution of Eq. provides us a search direction. Then, we can find a step length $\alpha$ for updating the next guess $(\mathbf{X}_{i + 1},\mathbf{U}_{i + 1})$ as

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B The role of gaps in multiple-shooting", "weight": 1.0} -->

where the new guess trajectory $\left( \mathbf{X}_{i + 1},\mathbf{U}_{i + 1} \right)$ does not necessarily close the gaps as we explain below.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B1 KKT problem of the multiple-shooting formulation", "weight": 1.0} -->

To understand the behavior of the gaps, we formulate the KKT problem in Eq.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B1 KKT problem of the multiple-shooting formulation", "weight": 1.0} -->

where Eq., are the dual and primal feasibility of the First-order Necessary Condition (FONC) of optimality, respectively. The Jacobians and Hessians of the cost function (LQ approximation) are $\mathbf{l}_{\mathbf{x}}$, $\mathbf{l}_{\mathbf{u}}$, and $\mathbf{l}_{\mathbf{x}\mathbf{x}}$, $\mathbf{l}_{\mathbf{x}\mathbf{u}}$, $\mathbf{l}_{\mathbf{u}\mathbf{u}}$, respectively. The Lagrangian multipliers of the KKT problem are $({\mathbf{λ}}_{k},{\mathbf{λ}}_{k + 1})$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B1 KKT problem of the multiple-shooting formulation", "weight": 1.0} -->

in which we note that a $\alpha$-step closes the gap at $k$ by a factor of ${({1 - \alpha})}{\overline{\mathbf{f}}}_{k}$, while only a full-step $({\alpha = 1})$ can close the gap completely. Below, we explain how to ensure this multiple-shooting behavior in the forward-pass.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-C Nonlinear rollout avoids merit function", "weight": 1.0} -->

SQP often requires a *merit* function to compensate the errors that arise from the local approximation of the classical line-search. Defining a suitable merit function is often challenging, which is why we do not follow this approach. Instead, we avoid (a) the linear-prediction error of the dynamics -- i.e. search direction defined by Eq. -- with a nonlinear rollout and (b) the requirement of a merit function.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-C Nonlinear rollout avoids merit function", "weight": 1.0} -->

and we maintain the same gap contraction rate of the search direction Eq..

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-C Nonlinear rollout avoids merit function", "weight": 1.0} -->

where $\mathbf{k}_{k}$ and $\mathbf{K}_{k}$ are the feed-forward term and feedback gains computed during the backward pass, respectively. Note that the forward pass of the classical DDP always closes the gaps, and with $\alpha = 1$, the FDDP forward pass behaves exactly as the classical DDP one.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-D Backward pass under an infeasible guess trajectory", "weight": 1.0} -->

Gaps in the dynamics and infeasible warm-starts generate derivatives at different points. The Riccati recursion updates the Value and Hamiltonian functions based on these derivatives. The classical DDP algorithm overcomes this problem by first performing an initial forward pass. However, from a theoretical point, it corresponds to only being able to warm-start the solver with the control trajectory $\mathbf{U}_{0}$, which is not convenient in practice^77^7It is straight-forward to obtain a state trajectory $\mathbf{X}_{0}$ that provides an initial guess for the OC solver, however, establishing a corresponding control trajectory $\mathbf{U}_{0}$ beyond quasi-static maneuvers is a limiting factor..

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-D Backward pass under an infeasible guess trajectory", "weight": 1.0} -->

We adapt the backward pass to accept infeasible guesses as proposed. It assumes a LQ approximation of the Value function, i.e. the Hessian is constant and the Jacobian varies linearly. We use this fact to map the Jacobians and Hessian of the Value function from the next shooting-node to the current one.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-E Accepting a step", "weight": 1.0} -->

The expectation of the total cost reduction proposed by does not consider the deflection introduced by the gaps. This is a critical point to evaluate the success of a trial step during the numerical optimization.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-E Accepting a step", "weight": 1.0} -->

where, by closing the gaps as predicted in Eq.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-E Accepting a step", "weight": 1.0} -->

Note that if all gaps are closed, then this expectation model matches the one reported.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-E Accepting a step", "weight": 1.0} -->

We use the Goldstein condition to check for the trial step, instead of the Armijo condition typically used in classical DDP algorithms, e.g.,. The reason is due to the fact that $\DeltaJ$ might be an ascent direction, for instance, during the infeasible iterations.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-E Accepting a step", "weight": 1.0} -->

where $b_{1}$, $b_{2}$ are adjustable parameters, we used in this paper $b_{1} = 0.1$ and $b_{2} = 2$. This critical mathematical aspect has not been considered.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Results", "weight": 1.0} -->

In this section, we show the capabilities of our multi-contact optimal control framework. We first compute various legged gaits for both quadruped and biped robots (Section IV-A). As our formulation is simple and does not depend on a good initial guess, it can be used easily with different legged robots. Next, we analyze the performance of the FDDP with the generation of highly-dynamic maneuvers such as jumps and front-flips. These motions are computed within a few iterations and milliseconds as reported. We have deliberately ignored friction-cone constraints and torque limits for the sake of evaluating the FDDP, however, it is possible to include those inequality constraints through quadratic penalization as shown in the cover clip of accompanying video. The accompanying video^88^8 highlights all different motions reported in this section.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-A Various legged gaits", "weight": 1.0} -->

We computed different gaits --- walking, trotting, pacing, and bounding --- with our FDDP algorithm in the order of milliseconds. All these gaits are a direct outcome of our algorithm given a predefined sequence of contacts and step timings. These motions are computed in around 12 iterations. We used the same weight values and cost functions for all the quadrupedal gaits, and similar weight values for the bipedal walking.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-A Various legged gaits", "weight": 1.0} -->

The cost function is composed of the Center of Mass (CoM) and the foot placement tracking costs together with regularization terms for the state and control. We used piecewise-linear functions to describe the reference trajectory for the swing foot. Additionally, we strongly penalize footstep deviation from the reference placement. We warm-start our solver using a linear interpolation between the nominal body postures of a sequence of contact configurations. This provides us a set of body postures together with the nominal joint postures as state warm-start $\mathbf{X}_{0}$. Then, the control warm-start $\mathbf{U}_{0}$ is obtained by applying the quasi-static assumption^99^9The quasi-static torques are numerically computed through Newton steps using the reference posture as an equilibrium point. along $\mathbf{X}_{0}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-A Various legged gaits", "weight": 1.0} -->

In each switching phase^1010^10In this work, with "switching phases" we refer to contact gain., we use the impulse dynamics to ensure the contact velocity equals zero, see Eq.. We observed that the use of impulse models improves the algorithm convergence compared to penalizing the contact velocity. We used a weighted least-squares function to regularize the state with respect to the nominal robot posture, and quadratic functions for the tracking costs and control regularization.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-B Highly-dynamic maneuvers", "weight": 1.0} -->

Our FDDP algorithm is able to compute highly-dynamic maneuvers such as front-flip and jumping in the order of milliseconds (Fig. 3). These motions are often computed in between 12--36 iterations with a naïve and infeasible $\mathbf{X}_{0},\mathbf{U}_{0}$ warm-start. We used the same initialization, weight values and cost functions reported in Section IV-A, with a slightly incremented weight for the state regularization during the impact phases (i.e. $w_{xReg} = 10$). Additionally, and for simplicity, we included a cost that penalizes the body orientation in the ICub jumps. Similarly to other cost functions, we used a quadratic penalization with a weight value of $10^{4}$. Note that a more elaborate cost function could be incorporated: arm motions, angular momentum regulation, etc.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-B Highly-dynamic maneuvers", "weight": 1.0} -->

The advantage of our FDDP algorithm is clearly evident in the generation of highly-dynamic maneuvers, where feasible rollouts might produce trajectories that are unstable and far from the solution. The classical DDP has a poor globalization strategy that comes from inappropriate feasible rollouts in the first iterations; it struggles to solve these kind of problems.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-C Runtime, contraction, and convergence", "weight": 1.0} -->

We analyzed the gaps contraction and convergence rates for all the presented motions. To easily compare the results, we normalize the gaps and cost values per each iteration as shown in Fig. 2. We use the L2-norm of the total gaps and plot the applied step-length for the jumping motions (ajump-4f and ajump-2f). These results show that keeping the gaps open is particularly important for highly-dynamic maneuvers such as jumping. Indeed, in the jumping motions, FDDP keeps the gaps open for few iterations. Additionally, we often observed in practice super-linear convergence of the FDDP algorithm after closing the gaps. This is expected since the FDDP forward-pass behaves as the DDP forward pass when the gaps are closed, which is defined by the search direction of a multiple-shooting formulation with only equality constraints (Section III-B1).

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-C Runtime, contraction, and convergence", "weight": 1.0} -->

Highly-dynamic maneuvers have a lower rate of improvement in the first iterations, cf. Fig. 2 (bottom). The same occurs in the quadrupedal walking case (walk-4f), in which the four-feet support phases have a very short duration (${\Deltat} = 2$ $ms$). Our FDDP algorithm, together with the impact models, shows competitive convergence rates when compared to the reported results, respectively.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-C Runtime, contraction, and convergence", "weight": 1.0} -->

The motions converge within 10 to 34 iterations, with an overall computation time of less than $0.5\ s$. The numerical integration step size is often ${\deltat} = {1 \times 10^{- 2}}$ $s$, with the exception of the biped walking ${\deltat} = {3 \times 10^{- 2}}$ $s$, and the number of nodes are typically between 60 to 115. Therefore, the optimized trajectories have a horizon of between ${0.6\ s}\text{~to~}{3\ s}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-C Runtime, contraction, and convergence", "weight": 1.0} -->

We also benchmark the computation time for a single iteration using our solver. The number of contacts does not affect the computation time; it scales linearly with respect to the number of nodes. With multi-threading, our efficient implementation of contact dynamics achieves computation rates up to $859.6\ {Hz}$ (jump-4f on i9-9900K, 60 nodes). We parallelize only the computation of the derivatives, and roughly speaking, we reduce the computation time in half using four to eight threads (cf. Fig. 4).

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-C Runtime, contraction, and convergence", "weight": 1.0} -->

To understand the performance of Crocoddyl, we have run 50000 trials, for each of the benchmark motions, on four different Intel PCs with varying levels of parallelization^1111^11*PC1*: i7-6700K @ ${4.00{GHz}} \times 8$ with 32 $GB$ $2133{MHz}$ RAM, *PC2*: i7-7700K @ ${4.20{GHz}} \times 8$ with 16 $GB$ $2666{MHz}$ RAM, *PC3*: i9-9900K @ ${3.60{GHz}} \times 16$ with 64 $GB$ $3000{MHz}$ RAM, and *PC4*: i7-9900XE @ ${3.00{GHz}} \times 36$ with 128 $GB$ $2666{MHz}$ RAM.. We used the optimal number of threads for each PC as identified in Fig. 4. The computation frequency per one iteration is reported in Fig. 5.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented a novel and efficient framework for multi-contact optimal control. The gap contraction of FDDP is equivalent to direct multiple-shooting formulations with only equality constraints (i.e. the Newton method applied to the KKT conditions). However, and in contrast to classical multiple-shooting, FDDP does not add extra decision variables which often increases the computation time per iteration due to factorization; it has cubic complexity in matrix dimension. FDDP also improves the poor globalization strategy of classical DDP methods. This allows us to solve highly-dynamic maneuvers such as jumping and front-flip in the order of milliseconds. Thanks to our efficient method for computing the contact dynamics and their derivatives, we can solve the optimal control problem at high frequencies. Finally, we demonstrated the benefits of using impact models for contact gain phases. Our core idea about feasibility could incorporate inequality constraints in the form of penalization terms. Future work will focus on feasibility under inequality constraints such as torque limits, and friction cone. Those inequalities constraints can be handled using interior-point or Augmented Lagrangian methods.
