<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control

Topics include Control barrier functions, Safe optimal control, Receding horizon control, Predictive safety, Real-time control, Nonlinear systems.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Generalizes control barrier functions from current-state certificates to finite-horizon predicted-flow functionals inside a real-time optimal-control loop. The paper targets CBF myopia by certifying predicted trajectories while retaining pointwise safety constraints that can be used online.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Control barrier functions (CBFs) provide real-time safety guarantees through pointwise conditions on the state. However, synthesizing a valid CBF is difficult and the resulting controllers are myopic. To address myopia, this article introduces predicted-flow control barrier functions (P-CBFs), which generalize the CBF from a function of the current state to a functional of a predicted flow under a parametrized control plan over a finite prediction horizon. For safety, a P-CBF can certify that the predicted flow is in a safe set over the entire prediction horizon. However, candidate P-CBFs suffer from the same challenge as candidate CBFs, namely, control constraints make it difficult to guarantee that the P-CBF is valid. This article resolves this challenge by introducing a terminal candidate P-CBF requiring that the predicted flow end in a backup safe set at the terminal time, and a planning-time shift that modulates the prediction horizon, providing an additional degree of freedom to ensure feasibility.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The real-time control and the evolution of the control-plan parameter and planning-time shift are determined jointly by a single convex optimization that is guaranteed to be feasible and renders the associated safe set forward invariant. The resulting safe optimal flow control provides a safety certificate over the entire prediction horizon and unifies finite-horizon integral-cost optimization with safety certification. This optimization reduces to a quadratic program (QP) if the control constraints are a convex polytope. The QP implementation, termed FlowBarrier, is validated on a nonholonomic ground robot navigating a dense environment. FlowBarrier is compared to nonlinear model predictive control and two CBF-based safety filter methods across 100 trials, where FlowBarrier achieves the highest goal-reaching rate, zero safety violations, and the lowest computation time.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous robots are of interest for real-time navigation in proximity to obstacles, humans, and other robots. Applications include aerial inspection, warehouse logistics, and autonomous mobility. These applications require that robots achieve performance objectives (e.g., way-point navigation, coordination, formation) while maintaining safety and respecting control input limits (e.g., actuator saturation). Safety can be formalized as forward invariance of a prescribed safe set $\mathcal{C}_{s} \subseteq {\mathbb{R}}^{n}$. Frameworks for enforcing forward invariance include Hamilton-Jacobi reachability analysis, model predictive control, and barrier functions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Control barrier functions (CBFs) provide techniques for selecting controls that enforce forward invariance. For a control-affine system, the CBF condition is affine in the control. In this case, a quadratic program (QP) can be used to compute a minimum-intervention control that ensures forward invariance of the CBF's zero-superlevel set. Thus, safety enforcement is achieved using a computationally efficient, real-time safety filter that can be implemented in a hierarchical architecture. However, two limitations constrain applicability of this approach.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

First, synthesizing a valid CBF on a large subset of $\mathcal{C}_{s}$ is challenging due to control input constraints. Existing methods based on Hamilton-Jacobi reachability and sum-of-squares programming are limited to low-dimensional systems or restricted dynamics.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, even if a valid CBF is available, pointwise CBF-based optimization is myopic. Specifically, the safety certificate is enforced pointwise in time and depends only on the current state, with no consideration of how the trajectory will evolve over a future time horizon. As a result, the CBF does not account for conflicts between safety and performance that develop over the horizon---this can lead to aggressive corrections, conservative behavior, poor performance, and infeasibility or constraint violations in real-world implementation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Backup-CBF methods have been developed to address the challenge of synthesizing a CBF subject to input limits. Instead of relying on a valid CBF on $\mathcal{C}_{s}$, backup-CBF methods specify a backup controller $u_{b}$ together with a backup set $\mathcal{C}_{b} \subset \mathcal{C}_{s}$ that is forward invariant under $u_{b}$. Then, the implicit control-forward-invariant subset of $\mathcal{C}_{s}$ is defined as the set of states from which the trajectory under $u_{b}$ is in $\mathcal{C}_{s}$ over a finite horizon and ends in $\mathcal{C}_{b}$ at the terminal time. This construction is conservative because the backup controller $u_{b}$ that makes $\mathcal{C}_{b}$ forward invariant is also used to drive the state to $\mathcal{C}_{b}$ by the terminal time.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Thus, the implicit control-forward-invariant set is often small relative to the maximal control-forward-invariant subset of $\mathcal{C}_{s}$. Recent work has sought to mitigate this conservatism by delaying the switch from the nominal controller to $u_{b}$ until the last time at which the backup trajectory reaches $\mathcal{C}_{b}$ without leaving $\mathcal{C}_{s}$, or by composing multiple backup sets and backup controllers to enlarge the implicit control-forward-invariant subset of $\mathcal{C}_{s}$. Nevertheless, these methods still rely on fixed backup controllers to drive the state toward $\mathcal{C}_{b}$, and thus, conservatism persists. Another shortcoming of backup-CBF approaches is that the finite-horizon prediction is used only for safety certification, not for performance optimization. Furthermore, the control is still determined by a pointwise condition on the current state, with no mechanism to optimize cost over the prediction horizon.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The myopic nature of pointwise CBF-based optimization has been addressed by incorporating finite-horizon prediction into the safety certificate. One approach is to compose a finite-horizon planner with a CBF-based safety filter in a layered architecture. The planner solves its own optimization with discrete CBF constraints to generate a reference, and the safety filter then enforces barrier constraints on the applied control through the CBF. This layered design introduces at least one additional optimization beyond the CBF and does not address the validity of the barrier function. Even if the safety filter is replaced by a backup CBF to recover validity, the planner and the backup controller each propagate the system dynamics on a finite horizon for different purposes---one for cost and the other for safety, and these propagations are decoupled with potentially conflicting goals. A second approach avoids the layered structure and addresses prediction and safety in a single optimization. Specifically, propagates a trajectory under a fixed nominal controller and encodes its future safety into a barrier condition that is affine in the current control; however, the certified safe set is determined by the nominal controller, and feasibility under input constraints is not guaranteed.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The approach in parametrizes the control trajectory to address invariance in trajectory space; however, the resulting QP is not guaranteed to be feasible, and thus safety is not guaranteed. Motivated by embedding CBF constraints in a receding-horizon optimization, several methods improve tractability through iterative linearization, sampling-based trajectory optimization with a closed-form CBF filter, or quadratic approximation of the cost-to-go; however, the validity of the barrier function at each step is assumed rather than established, and the underlying pointwise CBF condition can become infeasible under input constraints. In summary, existing methods that incorporate prediction into the safety certificate either decouple prediction from certification across separate optimizations, or rely on a single optimization whose feasibility under input constraints is not guaranteed.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

This article presents a non-myopic real-time optimal control for simultaneous safety and performance with guaranteed feasibility in the presences of input constraints. First, the article introduces predicted-flow control barrier functions (P-CBFs), which can be used to certify safety of a predicted flow over a finite prediction horizon. The P-CBF generalizes the CBF concept from a function of the current state to a functional of the predicted flow under a parametrized control plan. Specifically, the control plan is parametrized by a finite-dimensional variable $\theta$ over a prediction horizon $T$, and the dynamics are propagated over this horizon under the control plan to obtain the predicted flow $\varphi$. A logical candidate P-CBF is the minimum of $h_{s}{(\varphi)}$ over the prediction horizon, where the safe set $\mathcal{C}_{s}$ is the zero-superlevel set of $h_{s}$, which is not assumed to be a valid CBF.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, this candidate P-CBF suffers from the same challenge as standard candidate CBFs---namely, control constraints make it difficult to guarantee and verify that the set of controls satisfying the P-CBF condition is nonempty. A natural remedy is to add a terminal candidate P-CBF that requires the predicted flow to end in a backup safe set $\mathcal{C}_{b}$ at the terminal time. Still, it remains difficult to guarantee that this candidate P-CBF pair is a valid P-CBF pair under input constraints.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address validity/feasibility, this article introduces a scalar planning-time shift $\gamma$ that modulates the prediction window, providing an additional degree of freedom in the optimization (see Figure 1). The planning-time shift $\gamma$ and control-plan parameter $\theta$ are treated as dynamic states and combined with the system state $x$ to form an augmented state $(x,\theta,\gamma)$. The applied control $u$, update of $\theta$, and evolution of $\gamma$ are then determined jointly as the solution of a single convex optimization that is guaranteed to be feasible at every time and whose solution makes the associated safe set forward invariant. The resulting safe optimal flow control provides a safety certificate over the entire prediction horizon and unifies cost optimization with safety certification in a single convex optimization whose feasibility under input constraints is guaranteed. If control constraints are a convex polytope, then the optimization reduces to a QP, named FlowBarrier.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

This article is organized as follows. Section 2 reviews directional derivatives, and Section 3 introduces directional CBFs, which extends the idea CBFs to functions that are directionally differentiable but not necessarily continuously differentiable. These directional CBFs are used in Section 4 to introduce P-CBFs and show that P-CBFs can be used to obtain forward invariance in trajectory space. Section 5 formulates the safe optimal control problem addressed in this article. Then, Section 6 presents the safe optimal flow control solution with guaranteed feasibility, and Section 7 presents the QP implementation, named FlowBarrier. Section 8 applies FlowBarrier to a nonholonomic ground robot and compares the algorithm to nonlinear model predictive control and two CBF-based safety filters paired with an iterative linear-quadratic regulator planner across 100 trials, where FlowBarrier achieves the highest goal-reaching rate, zero safety violations, and the lowest computation time. The source code for FlowBarrier and all comparison methods is publicly available in CBFJAX, an open-source library developed alongside this work that provides automatic differentiation, just-in-time compilation, and a unified benchmarking environment for safe optimal control methods.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Directional Derivatives", "weight": 1.0} -->

exists. If $\mu$ is differentiable on $\mathcal{D}$, then ${D_{\nu}\mu{(x)}} = {L_{\nu}\mu{(x)}}$, where ${L_{\nu}\mu{(x)}} \triangleq {\mu^{\prime}{(x)}\nu}$ is the Lie derivative of $\mu$ along $\nu$. This article is not concerned with functions that are left-side directionally differentiable (i.e., $\lim_{s \uparrow 0}$) but not differentiable. Thus, for brevity, we omit "right-side" for the remainder of the article.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Directional Derivatives", "weight": 1.0} -->

The next result concerns the time derivative of $\mu{({y{(t)}})}$ from the right side.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Directional Control Barrier Functions", "weight": 1.0} -->

Let $h:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ be continuous, and define the zero-superlevel set

<!-- chunk {"id": "body-0020", "role": "body", "section": "Directional Control Barrier Functions", "weight": 1.0} -->

which is assumed to be nonempty and contain no isolated points.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Directional Control Barrier Functions", "weight": 1.0} -->

A continuous function $a:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ is an extended class-$\mathcal{K}$ function if it is strictly increasing and ${a{}} = 0$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Predicted-Flow Control Barrier Functions", "weight": 1.0} -->

Let $k:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ be continuously differentiable, and define the admissible parameter set

<!-- chunk {"id": "body-0023", "role": "body", "section": "Predicted-Flow Control Barrier Functions", "weight": 1.0} -->

where for all ${(\tau,\theta)} \in {{\lbrack 0,T\rbrack} \times \Theta}$, ${u_{p}{(\tau;\theta)}} \in \mathcal{U}$. The following example provides one construction for $u_{p}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example 1", "weight": 1.0} -->

which implies that $\phi{(\tau;x,\theta)}$ is the solution to at planning time $\tau \in {\lbrack 0,T\rbrack}$ with initial condition $x$ and $u = {u_{p}{( \cdot;\theta)}}$. In other words, $\phi{( \cdot;x,\theta)}$ is the flow of from state $x$ under the plan $u_{p}{( \cdot;\theta)}$ with parameter $\theta$. Differentiating with respect to $\tau$ yields

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example 1", "weight": 1.0} -->

which is the evolution of the predicted flow $\phi$ given $(x,\theta)$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example 1", "weight": 1.0} -->

At each time $t \geq 0$, the predicted flow $\phi{( \cdot;{x{(t)}},{\theta{(t)}})}$ depends on the current state $x{(t)}$ and parameter $\theta{(t)}$. The time evolution of $x$ is influenced by the control $u$. In order to influence the time evolution of $\theta$, we let $\theta:{{\lbrack 0,\infty)}\rightarrow{\mathbb{R}}^{d}}$ be the solution to

<!-- chunk {"id": "body-0027", "role": "body", "section": "Example 1", "weight": 1.0} -->

is locally Lipschitz and directionally differentiable on

<!-- chunk {"id": "body-0028", "role": "body", "section": "Example 1", "weight": 1.0} -->

Note that $\Psi$ is the set of $(x,\theta)$ such that the predicted flow $\phi$ mapped through each functional $H_{i}$ is nonnegative, and $\theta \in \Theta$, which implies that ${u_{p}{(\tau;\theta)}} \in \mathcal{U}$ for the entire planning horizon $\tau \in {\lbrack 0,T\rbrack}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Example 1", "weight": 1.0} -->

We now introduce the concept of a predicted-flow CBF. This concept extends the notion of a D-CBF to address the $\ell$-tuple $(\psi_{1},\ldots,\psi_{\ell})$, where each $\psi_{i}$ is obtained by mapping $\phi$ through the functional $H_{i}$ and where $k$ defines the admissible parameters for the control plan.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 1", "weight": 1.0} -->

If there are no constraints on the control input (i.e., $\mathcal{U} = {\mathbb{R}}^{m}$), then $k$ can be selected as a positive constant. In this case, ${{k^{\prime}\hat{\omega}} + {\beta{(k)}}} = {\beta{(k)}} > 0$, which implies that the first inequality in is trivially satisfied. In this case, $(\psi_{1},\ldots,\psi_{\ell})$ is a P-CBF $\ell$-tuple on $\Psi$ if and only if $(\psi_{1},\ldots,\psi_{\ell})$ is a D-CBF $\ell$-tuple on $\Psi$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The next result shows that if $(\psi_{1},\ldots,\psi_{\ell})$ is a P-CBF $\ell$-tuple on $\Psi$, then any control selected pointwise from $K_{\Psi}{(x,\theta)}$ makes $\Psi$ forward invariant. This result is a consequence of Theorem 1 and Proposition 1.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Minimum-Over-Prediction-Horizon P-CBF", "weight": 1.0} -->

We present a candidate P-CBF for the situation in which it is desirable for the predicted flow $\phi$ to be in a desired set throughout the prediction horizon $\lbrack 0,T\rbrack$. Specifically, let $h_{s}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ be continuously differentiable, and define

<!-- chunk {"id": "body-0033", "role": "body", "section": "Minimum-Over-Prediction-Horizon P-CBF", "weight": 1.0} -->

To determine whether $\phi$ is in $\mathcal{C}_{s}$ throughout the prediction horizon, consider the candidate P-CBF

<!-- chunk {"id": "body-0034", "role": "body", "section": "Minimum-Over-Prediction-Horizon P-CBF", "weight": 1.0} -->

Note that $\psi_{m}$ is nonnegative if and only if ${\phi{(\tau;x,\theta)}} \in \mathcal{C}_{s}$ for all prediction times $\tau \in {\lbrack 0,T\rbrack}$. Next, define

<!-- chunk {"id": "body-0035", "role": "body", "section": "Minimum-Over-Prediction-Horizon P-CBF", "weight": 1.0} -->

The next result demonstrates that $\psi_{m}$ is locally Lipschitz and directionally differentiable, which implies that it satisfies the conditions in Definition 4 to be a candidate P-CBF. The result also provides an expression for the directional derivative of $\psi_{m}$, which depends on the following set

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Proposition 3 implies that the control variables $(\hat{u},\hat{\omega})$ satisfy the directional derivative constraint

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 2", "weight": 1.0} -->

if and only if $(\hat{u},\hat{\omega})$ satisfy the family of affine constraints with $c = {- {\alpha{({\psi_{m}{(x,\theta)}})}}}$. Similar to standard CBFs, these affine constraints are useful for control synthesis.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Terminal-Prediction-Time P-CBF", "weight": 1.0} -->

This subsection presents a candidate P-CBF for the situation in which it is desirable for the predicted flow $\phi$ to be in a desired set at the terminal prediction time (i.e., $\tau = T$). Specifically, let $h_{b}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ be continuously differentiable, and define

<!-- chunk {"id": "body-0039", "role": "body", "section": "Terminal-Prediction-Time P-CBF", "weight": 1.0} -->

Then, consider the candidate P-CBF

<!-- chunk {"id": "body-0040", "role": "body", "section": "Terminal-Prediction-Time P-CBF", "weight": 1.0} -->

The next result demonstrates that $\psi_{t}$ is continuously differentiable. Thus, the directional derivative equals the Lie derivative, and the Lie derivative along the trajectories of 4 and 13 is affine in the control variables $(\hat{u},\hat{\omega})$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Equations and are two useful candidate P-CBFs used in this article. However, mapping the predicted flow $\phi$ through other functionals can yield other potentially useful candidate P-CBFs. For example, consider the candidate P-CBF obtained by integrating a function of the flow over time, specifically, ${\psi_{int}{(x,\theta)}} = {a + {\int_{0}^{T}{b{({\phi{(\tau;x,\theta)}})}{d\tau}}}}$, where $a \in {\mathbb{R}}$ and $b:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is continuously differentiable. This candidate P-CBF can be used to capture the energy of the predicted flow.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

For the remainder of this article, we consider the problem of designing admissible feedback controls $(u,\omega)$ that minimize an integral cost of the predicted flow $\phi$ over the prediction horizon such that the predicted flow $\phi{( \cdot;{x{(t)}},{\theta{(t)}})}$ and actual state $x{(t)}$ are in a prescribed safe set $\mathcal{C}_{s}$ for all time $t \geq 0$. The safe set $\mathcal{C}_{s}$ is given, where $h_{s}$ is continuously differentiable and known. We assume the admissible control sets $\mathcal{U}$ and $\Omega$ are convex, and $0 \in \Omega$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Notably, $h_{s}$ is not assumed to be a CBF for on $\mathcal{C}_{s}$. Similarly, $\psi_{m}$ given by is not assumed to be a P-CBF for 4 and 13 on $\Psi_{m}$, which is given. Thus, it is not necessarily possible to make $\mathcal{C}_{s}$ or $\Psi_{m}$ forward invariant.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

where $W:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ and $R:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}}$ are continuously differentiable. The objective is to minimize $J$ while ensuring the predicted flow is in $\mathcal{C}_{s}$ and the control and control-plan parameters are admissible. The objective is formalized as follows.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Constraints (C1) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") and (C2) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") can be re-framed in terms of forward invariance. Note that (C1) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") and (C2) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") are satisfied if and only if for all $t \geq 0$, ${({x{(t)}},{\theta{(t)}})} \in \Psi_{m}$. Thus, (C1) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") and (C2) ‣ Problem 1.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Problem 1", "weight": 1.0} -->

‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") are satisfied by designing ${u{(t)}} \in \mathcal{U}$ and ${\omega{(t)}} \in \Omega$ that make a subset of $\Psi_{m}$ forward invariant.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Since $h_{s}$ is not assumed to be a CBF, and $\psi_{m}$ is not assumed to be a P-CBF, it may not be possible to satisfy (C1) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") and (C2) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control"). To ensure the problem is well posed, we assume there exists a subset of $\mathcal{C}_{s}$ that can be made forward invariant with respect to. Specifically, consider a backup safe set $\mathcal{C}_{b} \subset \mathcal{C}_{s}$, which is given, where $h_{b}$ is continuously differentiable and known. We make the following assumption.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Assumption 1 implies that $h_{b}$ is a CBF for on $\mathcal{C}_{b}$. Thus, $\mathcal{C}_{b}$ can be made forward invariant with respect to. However, $\mathcal{C}_{b}$ may be small relative to $\mathcal{C}_{s}$. Thus, it is not desirable for the predicted flow $\phi{(\tau;{x{(t)}},{\theta{(t)}})}$ to be in $\mathcal{C}_{b}$ for all prediction times $\tau \in {\lbrack 0,T\rbrack}$ or for all real time $t \geq 0$. Such a restriction on $\phi$ can lead to large $J$, that is, poor performance. Instead, Assumption 1 is used to introduce a terminal-prediction-time condition on the predicted flow.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Specifically, we consider the condition that for all time $t \geq 0$, the predicted flow $\phi{( \cdot;{x{(t)}},{\theta{(t)}})}$ at terminal prediction time $T$ is in $\mathcal{C}_{b}$. This condition can be re-framed in terms of forward invariance by considering $\psi_{t}$ and $\Psi_{t}$ given by and. Specifically, for all $t \geq 0$, ${\phi{(T;{x{(t)}},{\theta{(t)}})}} \in \mathcal{C}_{b}$ and ${\theta{(t)}} \in \Theta$ if and only if for all $t \geq 0$, ${({x{(t)}},{\theta{(t)}})} \in \Psi_{t}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Thus, the terminal condition can be satisfied by designing controls ${u{(t)}} \in \mathcal{U}$ and ${\omega{(t)}} \in \Omega$ that make a subset of $\Psi_{t}$ forward invariant.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Since $J$ can be nonlinear and nonconvex, Problem 1 cannot necessarily be solved with a convex optimization. However, the time derivative of $J$ along the trajectories of and is

<!-- chunk {"id": "body-0052", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

To make the time derivative of $J$ small, consider the quadratic cost

<!-- chunk {"id": "body-0053", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

where $Q_{u} \in {\mathbb{R}}^{m \times m}$ and $Q_{\omega} \in {\mathbb{R}}^{d \times d}$ are positive definite. The first 2 terms of make $\frac{dJ}{dt}$ small, whereas the other 2 terms provide regularization that make strictly convex. Specifically, ${\hat{\omega}}^{\top}Q_{\omega}\hat{\omega}$ limits the rate of change of the control plan parameter $\theta$ and ${\lbrack{\hat{u} - {u_{p}{(0;\theta)}}}\rbrack}^{\top}Q_{u}{\lbrack{\hat{u} - {u_{p}{(0;\theta)}}}\rbrack}$ limits deviation of the executed control from the control plan. Hence, minimizing the quadratic cost $\mathcal{J}$ subject to (C1) ‣ Problem 1.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") and (C2) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") yields gradient flow that aims to decrease $J$ along the trajectories of and. Thus, we address Problem 1 by solving the following problem.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Problem 2", "weight": 1.0} -->

Design feedback controls for ${u{(t)}} \in \mathcal{U}$ and ${\omega{(t)}} \in \Omega$ such that for each time $t \geq 0$, the quadratic cost $\mathcal{J}{(\hat{u},\hat{\omega};{x{(t)}},{\theta{(t)}})}$ is minimized subject to (C1) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") and (C2) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control").

<!-- chunk {"id": "body-0056", "role": "body", "section": "Problem 2", "weight": 1.0} -->

The following subsections present solutions to Problem 2 in special circumstances: A. $\psi_{m}$ is a P-CBF, and B. $(\psi_{m},\psi_{t})$ is a P-CBF pair. These special circumstances can be difficult to satisfy and/or verify, which motivates the remainder of this article, where we present a solution to Problem 2 without these assumptions.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Solution if $\\psi_{m}$ is a P-CBF", "weight": 1.0} -->

This subsection addresses the case where $\psi_{m}$ is a P-CBF on $\Psi_{m}$ for and. In this case, Definition 4 implies that there exist extended class-$\mathcal{K}$ functions $\alpha,\beta$ such that for all ${(x,\theta)} \in \Psi_{m}$,

<!-- chunk {"id": "body-0058", "role": "body", "section": "Solution if $\\psi_{m}$ is a P-CBF", "weight": 1.0} -->

is nonempty. The next result shows that $\mathcal{J}$ has a unique global minimizer over the set $K_{m}{(x,\theta)}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 4", "weight": 1.0} -->

If $\mathcal{U}$ and $\Omega$ are convex polytopes, then Proposition 3 implies that all constraints that define $K_{m}{(x,\theta)}$ are affine. In this case, the optimal control can be obtained efficiently from a QP that depends on the predicted flow. Section 7 addresses implementation of these QPs.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Corollary 1 requires that $\psi_{m}$ is a P-CBF, which is generally difficult to satisfy and verify because it requires that for each ${(x,\theta)} \in \Psi_{m}$, there exist ${(\hat{u},\hat{\omega})} \in {\mathcal{U} \times \Omega}$ that satisfies both constraints in $K_{m}{(x,\theta)}$. In general, control input constraints (i.e., $\mathcal{U}$ and $\Omega$) can lead to points where $K_{m}{(x,\theta)}$ is empty. Even if $\psi_{m}$ is a P-CBF, it may be difficult to determine the class-$\mathcal{K}$ functions $\alpha,\beta$ such that $K_{m}{(x,\theta)}$ is nonempty for all ${(x,\theta)} \in \Psi_{m}$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Solution if $(\\psi_{m},\\psi_{t})$ is a P-CBF pair", "weight": 1.0} -->

This subsection addresses the case where $(\psi_{m},\psi_{t})$ is a P-CBF pair on $\Psi_{mt} \triangleq {\Psi_{m} \cap \Psi_{t}}$, which is a subset of $\Psi_{m}$ created by imposing the condition that the predicted flow $\phi$ is in the backup safe set at the terminal prediction time. Since $(\psi_{m},\psi_{t})$ is a P-CBF pair, Definition 4 implies that there exist extended class-$\mathcal{K}$ functions $\alpha_{1},\alpha_{2},\beta$ such that for all ${(x,\theta)} \in \Psi_{mt}$,

<!-- chunk {"id": "body-0062", "role": "body", "section": "Solution if $(\\psi_{m},\\psi_{t})$ is a P-CBF pair", "weight": 1.0} -->

is nonempty. The next result shows that $\mathcal{J}$ has a unique global minimizer over $K_{mt}{(x,\theta)}$. The proof is similar to that of Proposition 5.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Remark 6", "weight": 1.0} -->

Similar to Remark 4, if $\mathcal{U}$ and $\Omega$ are convex polytopes, then Proposition 3 implies that all constraints that define $K_{mt}{(x,\theta)}$ are affine. In this case, the optimal control (32 is a P-CBF pair ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control")) is the solution to a QP.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 7", "weight": 1.0} -->

The optimal control (32 is a P-CBF pair ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control")) in this subsection makes $\Psi_{mt}$ forward invariant in the case where $(\psi_{m},\psi_{t})$ is a P-CBF pair. It is worth noting that $\Psi_{mt} \subset \Psi_{m}$ because (32 is a P-CBF pair ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control")) is concerned not only with keeping the predicted flow $\phi{( \cdot;{x{(t)}},{\theta{(t)}})}$ in the safe set $\mathcal{C}_{s}$ but also with keeping the predicted flow $\phi{(T;{x{(t)}},{\theta{(t)}})}$ at the terminal prediction time $T$ in the backup safe set $\mathcal{C}_{b}$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 7", "weight": 1.0} -->

This terminal-prediction constraint focuses on achieving forward invariance for the subset $\Psi_{mt}$ because $\Psi_{m}$ cannot generally be made forward invariant if $\psi_{m}$ is not a P-CBF. Intuitively, it may seem more likely that $\Psi_{mt}$ can be made forward invariant than $\Psi_{m}$. However, the constraints in $K_{mt}$ are also more restrictive than those in $K_{m}$. Similar to Remark 5, it is generally difficult to satisfy and/or verify the condition that $(\psi_{m},\psi_{t})$ is a P-CBF pair.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 7", "weight": 1.0} -->

Even if $(\psi_{m},\psi_{t})$ is a P-CBF pair, it may be difficult to determine the class-$\mathcal{K}$ functions $\alpha_{1},\alpha_{2},\beta$ such that $K_{mt}{(x,\theta)}$ is nonempty for all ${(x,\theta)} \in \Psi_{mt}$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 7", "weight": 1.0} -->

The optimal controls in Corollaries 1 and 2 is a P-CBF pair ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") rely on assumptions that are difficult to satisfy and/or verify. The following section addresses these challenges by introducing a planning-time shift that guarantees feasibility of a convex optimization used to obtain optimal controls without requiring that $\psi_{m}$ is a P-CBF or that $(\psi_{m},\psi_{t})$ is a P-CBF pair. Moreover, this convex optimization is a QP in the case where $\mathcal{U}$ and $\Omega$ are convex polytopes.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Safe Optimal Flow Control", "weight": 1.0} -->

This section solves Problem 2 by introducing a planning-time shift that guarantees feasibility of the optimization that determines $(u,\omega)$. The key idea is to augment the state with a planning-time shift, which allows the prediction horizon to shrink as necessary to guarantee feasibility.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Predicted Flow with Planning Time Shift", "weight": 1.0} -->

We extend the definition for the predicted flow $\phi{( \cdot;x,\theta)}$ to allow for a time shift in the control plan $u_{p}{( \cdot;\theta)}$. Let $\gamma \in {\lbrack 0,T\rbrack}$ be the planning-time shift, and let the predicted flow ${\varphi{( \cdot;x,\theta,\gamma)}}:{{\lbrack\gamma,T\rbrack}\rightarrow{\mathbb{R}}^{n}}$ satisfy

<!-- chunk {"id": "body-0070", "role": "body", "section": "Predicted Flow with Planning Time Shift", "weight": 1.0} -->

For $\gamma = 0$, $\varphi{(\tau;x,\theta,0)}$ reduces to. In other words, $\varphi{(\tau;x,\theta,0)}$ is the solution to at planning time $\tau$, where $x$ is the initial condition and ${u{(t)}} = {u_{p}{(t;\theta)}}$. For $\gamma \in {(0,T\rbrack}$, $\varphi{(\tau;x,\theta,\gamma)}$ is the solution to at planning time $\tau - \gamma$, where $x$ is the initial condition and ${u{(t)}} = {u_{p}{({t + \gamma};\theta)}}$, which implies that the control plan is shifted by $\gamma$. Differentiating with respect to $\tau$ yields

<!-- chunk {"id": "body-0071", "role": "body", "section": "Predicted Flow with Planning Time Shift", "weight": 1.0} -->

which is the evolution of the predicted flow $\varphi$ given $(x,\theta,\gamma)$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Predicted Flow with Planning Time Shift", "weight": 1.0} -->

The planning-time shift $\gamma$ is the continuous-time analogue to shrinking the horizon in discrete-time receding-horizon control. In this work, we use the planning-time shift $\gamma$ to guarantee feasibility of an optimization that is used to generate the control and update the control plan. This can be viewed as the continuous-time analogue to the recursive-feasibility approach in discrete-time MPC. As $\gamma$ increases, the remaining prediction window $\lbrack\gamma,T\rbrack$ shrinks.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Predicted Flow with Planning Time Shift", "weight": 1.0} -->

Similar to the approach used with $\theta$, we introduce dynamics to influence the time evolution of $\gamma$. Specifically, let $\gamma:{{\lbrack 0,\infty)}\rightarrow{\mathbb{R}}}$ be the solution to

<!-- chunk {"id": "body-0074", "role": "body", "section": "Predicted Flow with Planning Time Shift", "weight": 1.0} -->

For notational convenience, we write and as

<!-- chunk {"id": "body-0075", "role": "body", "section": "Predicted Flow with Planning Time Shift", "weight": 1.0} -->

where $\overline{n} \triangleq {n + d + 1}$ and $\overline{m} \triangleq {m + d + 1}$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Control Forward Invariant Set", "weight": 1.0} -->

which are analogous to and but incorporate the planning-time shift. Next, define

<!-- chunk {"id": "body-0077", "role": "body", "section": "Control Forward Invariant Set", "weight": 1.0} -->

which is the set of $\overline{x}$ such that the predicted flow satisfies ${\varphi{(\tau;\overline{x})}} \in \mathcal{C}_{s}$ for all prediction times $\tau \in {\lbrack\gamma,T\rbrack}$; the predicted flow satisfies the terminal condition ${\varphi{(T;\overline{x})}} \in \mathcal{C}_{b}$; the control-plan parameter $\theta$ is in the admissible set $\Theta$; and the planning-time shift $\gamma$ is in the admissible set $\lbrack 0,T\rbrack$. Note that $\overline{\Psi}$ is analogous to $\Psi_{mt}$ but incorporates the planning-time shift.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Control Forward Invariant Set", "weight": 1.0} -->

The remainder of this subsection focuses on demonstrating that there exists a control $\overline{u}$ that makes $\overline{\Psi}$ forward invariant. Consider the backup control $u_{b}:{\mathcal{C}_{b}\rightarrow\mathcal{U}}$ defined by

<!-- chunk {"id": "body-0079", "role": "body", "section": "Control Forward Invariant Set", "weight": 1.0} -->

which exists and is unique because ${\|\hat{u}\|}^{2}$ is strictly convex, and $K_{b}{(x)}$ is nonempty and convex. The next result demonstrates that $u_{b}$ makes $\mathcal{C}_{b}$ forward invariant. The proof is in the appendix.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Controls that Make $\\overline{\\Psi}$ Forward Invariant", "weight": 1.0} -->

Although ${\overline{u}}_{fb}$ makes $\overline{\Psi}$ forward invariant, this control does not generally optimize the cost. Thus, this section provides a set of controls $\overline{u}$ that make $\overline{\Psi}$ forward invariant. In fact, this section shows that $\overline{\Psi}$ is made forward invariant by any control that satisfies P-CBF-like constraints, which are similar to section 5.2 is a P-CBF pair ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control").

<!-- chunk {"id": "body-0081", "role": "body", "section": "Controls that Make $\\overline{\\Psi}$ Forward Invariant", "weight": 1.0} -->

First, we extend Proposition 2 to address the planning-time shift. The result demonstrates that ${\overline{\psi}}_{m}$ is locally Lipschitz and directionally differentiable, and provides an expression for the directional derivative of ${\overline{\psi}}_{m}$, which depends on the following set

<!-- chunk {"id": "body-0082", "role": "body", "section": "Remark 8", "weight": 1.0} -->

The directional derivative ((b) ‣ Proposition 9. ‣ 6.3 Controls that Make Ψ̄ Forward Invariant ‣ 6 Safe Optimal Flow Control ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control")) differs from ((b) ‣ Proposition 2. ‣ 4.1 Minimum-Over-Prediction-Horizon P-CBF ‣ 4 Predicted-Flow Control Barrier Functions ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control")) because the planning-time shift $\gamma$ appears in the left end point of the feasible set $\lbrack\gamma,T\rbrack$ for the minimization. In contrast, the minimization without the planning-time shift is over the constant feasible set $\lbrack 0,T\rbrack$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Remark 8", "weight": 1.0} -->

The inclusion of $\gamma$ results in the extra term $\mathbf{1}_{\{{\tau = \gamma}\}}\frac{\partial\varphi}{\partial\tau}\frac{\partial\gamma}{\partial\overline{x}}$, which impacts the directional derivative if and only if the minimizer is at the left endpoint $\gamma$ and accounts for the effect of moving the feasible set $\lbrack\gamma,T\rbrack$ on ${\overline{\psi}}_{m}$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Remark 8", "weight": 1.0} -->

The next result extends Proposition 3 to address the planning-time shift. This result is an immediate consequence of part (b) ‣ Proposition 9. ‣ 6.3 Controls that Make Ψ̄ Forward Invariant ‣ 6 Safe Optimal Flow Control ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") of Proposition 9.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Remark 9", "weight": 1.0} -->

Proposition 10 implies that the control variable $\hat{\overline{u}}$ satisfies the directional derivative constraint

<!-- chunk {"id": "body-0086", "role": "body", "section": "Remark 9", "weight": 1.0} -->

The directional derivative of ${\overline{\psi}}_{m}$ along the trajectories of 35, 36, and 37 depends on the sensitivity

<!-- chunk {"id": "body-0087", "role": "body", "section": "Remark 9", "weight": 1.0} -->

where differentiating with respect to $x$, $\theta$, and $\gamma$ yields

<!-- chunk {"id": "body-0088", "role": "body", "section": "Remark 9", "weight": 1.0} -->

Section 7 addresses numerically efficient computation of these sensitivities using the adjoint method.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Remark 9", "weight": 1.0} -->

Next, we define a control constraint set that is similar to section 5.2 is a P-CBF pair ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") but addresses the planning-time shift. Let $\alpha_{m},\alpha_{\theta},\alpha_{\gamma}$ be extended class-$\mathcal{K}$ functions, and for all $\overline{x} \in {\{{\overline{x} \in \overline{\Psi}}:{\gamma \neq T}\}}$, consider $\overline{K}:{\overline{\Psi}\rightrightarrows{\mathcal{U} \times \Omega \times \mathcal{Z}}}$ defined by

<!-- chunk {"id": "body-0090", "role": "body", "section": "Remark 9", "weight": 1.0} -->

Corollary 2 is a P-CBF pair ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") requires that $(\psi_{m},\psi_{t})$ is a P-CBF pair to guarantee that the control constraint set $K_{mt}{(x,\theta)}$ is nonempty. Moreover, implementation of the constraint set requires knowledge of specific class-$\mathcal{K}$ functions that make $K_{mt}{(x,\theta)}$ nonempty. The next result shows that $\overline{K}{(\overline{x})}$ is nonempty. The result does not require that $({\overline{\psi}}_{m},{\overline{\psi}}_{t})$ is a P-CBF pair, and it holds for any choice of extended class-$\mathcal{K}$ functions $\alpha_{m},\alpha_{\theta},\alpha_{\gamma}$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Optimization-Based Control", "weight": 1.0} -->

This section presents the safe optimal flow control that optimizes the integral cost while guaranteeing that ${\overline{x}{(t)}} \in \overline{\Psi}$ for all $t \geq 0$. Consider the cost $\overline{J}:{{\mathbb{R}}^{\overline{n}}\rightarrow{\mathbb{R}}}$ given by

<!-- chunk {"id": "body-0092", "role": "body", "section": "Optimization-Based Control", "weight": 1.0} -->

which is analogous to except $\phi$ is replaced by $\varphi$. For $\gamma = 0$, $\overline{J}{(\overline{x})}$ reduces to $J{(x,\theta)}$. To make the time derivative of $\overline{J}$ small, we consider a quadratic cost that is analogous to. Specifically, consider the quadratic cost

<!-- chunk {"id": "body-0093", "role": "body", "section": "Optimization-Based Control", "weight": 1.0} -->

where $Q_{z} > 0$ and $\lambda \geq 0$. Similar to, the first 3 terms make $\frac{d\overline{J}}{dt}$ small, and the next 3 terms provide regularization that make (6.4) strictly convex. The final term $\lambda\hat{z}$ penalizes increasing $\gamma$. In other words, this incentivizes a large planning horizon $T - \gamma$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Remark 10", "weight": 1.0} -->

Since $\overline{J}$ involves an integral over $\lbrack\gamma,T\rbrack$, it follows that increasing $\gamma$ shrinks the prediction window, which can decrease $\overline{J}$. Consequently, the term $\frac{\partial\overline{J}}{\partial\gamma}\hat{z}$ in (6.4) can incentivize increasing $\gamma$ to reduce $\overline{J}$. This effect is not generally desirable; rather it is desirable for $\gamma$ to increase if and only if needed for feasibility. This work includes the $\lambda\hat{z}$ with relatively large $\lambda$ to mitigate this effect. The effect can also be mitigated by omitting $\frac{\partial\overline{J}}{\partial\gamma}\hat{z}$ from (6.4) and/or multiplying the integral in by $\frac{T}{T - \gamma}$ to provide normalization. All 3 methods are effective in simulation.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Remark 10", "weight": 1.0} -->

The next result extends Proposition 5 and shows that $\overline{\mathcal{J}}$ has a unique global minimizer over $\overline{K}{(\overline{x})}$. The proof is similar to that of Proposition 5.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Remark 11", "weight": 1.0} -->

Similar to Remark 4, if $\mathcal{U}$, $\Omega$, and $\mathcal{Z}$ are convex polytopes, then Proposition 10 implies that all constraints that define $\overline{K}{(\overline{x})}$ are affine. In this case, the optimal control can be obtained efficiently from a QP that depends on the predicted flow $\varphi$. Section 7 presents implementation of this QP.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Remark 11", "weight": 1.0} -->

Finally, consider the safe optimal flow control ${\overline{u}}_{\ast}:{\overline{\Psi}\rightarrow{\mathcal{U} \times \Omega \times \mathcal{Z}}}$ defined by

<!-- chunk {"id": "body-0098", "role": "body", "section": "Remark 11", "weight": 1.0} -->

The term $\lambda\hat{z}$ in (6.4) incentivizes $\gamma$ to be close to zero; however, it does not prevent $\gamma = T$. The constraint set $\overline{K}{(\overline{x})}$ is not well defined for $\gamma = T$ because the directional derivative of ${\overline{\psi}}_{m}$ does not necessarily exist. Hence, if $\gamma = T$, then control ${\overline{u}}_{\ast}$ switches to ${\overline{u}}_{b}$.

<!-- chunk {"id": "body-0099", "role": "body", "section": "QP Implementation of Safe Optimal Flow Control", "weight": 1.0} -->

This section presents a QP implementation of the safe optimal flow control. For this section, we assume $\mathcal{U}$, $\Omega$, and $\mathcal{Z}$ are convex polytopes.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Numerical Implementation", "weight": 1.0} -->

Proposition 10 implies that the constraint on ${\overline{\psi}}_{m}$ in (6.3) is equivalent to the family of affine constraints. Thus, can be expressed as

<!-- chunk {"id": "body-0101", "role": "body", "section": "Numerical Implementation", "weight": 1.0} -->

All constraints in are affine. However, (64c) may constitute infinitely many affine constraints because $\overline{\mathcal{T}}{(\overline{x})}$ may contain infinitely many points. Thus, is a semi-infinite QP, which can be solved with a variety of approaches; see. This article uses a discretization method over the planning time, where $\overline{\mathcal{T}}{(\overline{x})}$ is approximated with a finite set.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Numerical Implementation", "weight": 1.0} -->

Let $N$ be a positive integer, and define $T_{d} \triangleq \frac{T - \gamma}{N}$. Then, consider the set

<!-- chunk {"id": "body-0103", "role": "body", "section": "Remark 13", "weight": 1.0} -->

In practice, $h_{s}{({\varphi{( \cdot;\overline{x})}})}$ often has a unique global minimizer over $\lbrack\gamma,T\rbrack$. In this case, (64c) reduces to a single affine constraint.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Remark 13", "weight": 1.0} -->

for $\tau \in {{\overline{\mathcal{T}}}_{e}{(\overline{x})}}$. These can be computed using a forward sensitivity approach, where $\frac{\partial\varphi}{\partial\overline{x}}{(\tau;\overline{x})}$ is obtained by solving -- forward in prediction time alongside the predicted flow. However, this approach requires integrating a system of ordinary differential equations with dimension $n{({n + d + 1})}$, which is quadratic in $n$ and scales with the number of plan parameters $d$.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Remark 13", "weight": 1.0} -->

Alternatively, the adjoint approach is a more computationally efficient method to compute. The advantage is that each adjoint ordinary differential equation has dimension $n$. Specifically, since $\overline{J}$, ${\overline{\psi}}_{t}$, and $h_{s}{({\varphi{(\tau;\overline{x})}})}$ are scalar functions of $\overline{x}$, each gradient in can be computed with an adjoint $n$-dimensional backward integration. The gradients of $\overline{J}$ and ${\overline{\psi}}_{t}$ require backward integration from $T$ to $\gamma$, while the gradient of $h_{s}{({\varphi{(\tau;\overline{x})}})}$ at each $\tau \in {{\overline{\mathcal{T}}}_{e}{(\overline{x})}}$ requires backward integration from $\tau$ to $\gamma$.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Remark 13", "weight": 1.0} -->

Thus, all gradients are computed by integrating $2 + n_{e}$ different $n$-dimensional ordinary differential equations, where $n_{e}$ is the number of elements in ${\overline{\mathcal{T}}}_{e}{(\overline{x})}$. Hence, the complexity is linear in $n$ and does not increase with $d$, which implies that the adjoint method has significant computational benefit for large $n$ and/or large $d$. We also note that the $2 + n_{e}$ differential equations are decoupled from one another and can be solved in parallel.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Remark 13", "weight": 1.0} -->

Algorithm 1 summarizes FlowBarrier, which is the QP implementation of the safe optimal flow control where ${\deltat} > 0$ is the time increment for a zero-order hold on the control ${\overline{u}}_{\ast}$. We write the components of ${\overline{u}}_{\ast}$ as $\left. {\overline{u}}_{\ast} = {\left\lbrack \begin{matrix}
\end{matrix} \right.} \right\rbrack$.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Remark 13", "weight": 1.0} -->

At each time step, Algorithm 1 has 4 steps: (i) forward integration of to obtain the predicted flow $\varphi$, and evaluate ${\overline{\psi}}_{m}$, ${\overline{\psi}}_{t}$, and $k$; (ii) backward integration of the $2 + n_{e}$ parallel adjoint ordinary differential equations to obtain; (iii) solve QP with ${\overline{\mathcal{T}}}_{e}$ replacing $\overline{\mathcal{T}}$ to obtain ${\overline{u}}_{p \ast}$; and (iv) execute control $u_{\ast}$ and update $\theta$ and $\gamma$ by integrating optimal derivatives $\omega_{\ast}$ and $z_{\ast}$ over time increment $\deltat$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Remark 13", "weight": 1.0} -->

If $\gamma = T$, then steps (ii) and (iii) are replaced by solving the QP to obtain the backup ${\overline{u}}_{b}$.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Remark 14", "weight": 1.0} -->

If $\overline{K}{(\overline{x})}$ is empty, then slack variables can be used to ensure the QP is feasible while trying to drive $\overline{x}$ back to $\overline{\Psi}$.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Remark 15", "weight": 1.0} -->

If there is a time $t_{1} \geq 0$ such that ${\gamma{(t_{1})}} = T$, then the control results in $u_{\ast} = u_{b}$ and $\gamma = T$ for all $t \geq t_{1}$. Thus, does not have a mechanism to decrease $\gamma$ and recover the prediction window. Simulations suggest that it may be unlikely that $\gamma$ increases to $T$; however, if this occurs, then there is a practical approach to recover the prediction window. To explain, consider the QP

<!-- chunk {"id": "body-0112", "role": "body", "section": "Soft-Minimum Construction for $h_{s}$, $h_{b}$, and $k$", "weight": 1.0} -->

In this article, the safe set $\mathcal{C}_{s}$, backup set $\mathcal{C}_{b}$, and admissible parameter set $\Theta$ are each defined as the zero-superlevel set of one function (i.e., $h_{s}$, $h_{b}$, and $k$, respectively). In practice, it can be useful to define each set as the intersection of zero-superlevel sets of multiple functions. The approaches and analysis in this article extend directly to the case where $\mathcal{C}_{s}$, $\mathcal{C}_{b}$, and $\Theta$ are the intersection of zero-superlevel sets of multiple functions. In this case, $\overline{K}$ includes a constraint for each function, which increases complexity of the QP. An alternative approach is to use the log-sum-exponential soft minimum to compose multiple barrier functions into a single one.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Soft-Minimum Construction for $h_{s}$, $h_{b}$, and $k$", "weight": 1.0} -->

To illustrate a soft minimum of $h_{s}$, consider $n_{s}$ continuously differentiable barrier functions ${b_{1},\ldots,b_{n_{s}}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$. The set where all constraints are satisfied is

<!-- chunk {"id": "body-0114", "role": "body", "section": "Soft-Minimum Construction for $h_{s}$, $h_{b}$, and $k$", "weight": 1.0} -->

which is the intersection of the zero-superlevel sets of $b_{1},\ldots,b_{n_{s}}$. Then, consider the safe set $\mathcal{C}_{s}$, where

<!-- chunk {"id": "body-0115", "role": "body", "section": "Soft-Minimum Construction for $h_{s}$, $h_{b}$, and $k$", "weight": 1.0} -->

and it follows from that $\mathcal{C}_{s} \subseteq \mathcal{S}_{s}$, and $\mathcal{C}_{s}\rightarrow\mathcal{S}_{s}$ as $\rho_{s}\rightarrow\infty$. Furthermore, the worst case conservativeness of the soft-minimum approximation of the minimum is ${({\ln n_{s}})}/\rho_{s}$. Thus, $\rho_{s}$ can be selected to limit conservativeness based on $n_{s}$. If $\rho_{s}$ is small, then the soft minimum is a conservative approximation of the minimum. However, if $\rho_{s}$ is large, then the magnitude of $h_{s}^{\prime}$ is large at points where the minimum is not differentiable.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Soft-Minimum Construction for $h_{s}$, $h_{b}$, and $k$", "weight": 1.0} -->

Thus, selecting $\rho_{s}$ is a trade-off between the conservativeness of $\mathcal{C}_{s}$ and the magnitude of $h_{s}^{\prime}$. A similar approach can be used to construct $h_{b}$.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Soft-Minimum Construction for $h_{s}$, $h_{b}$, and $k$", "weight": 1.0} -->

The soft minimum can also be used to construct $k$. Since $\mathcal{U}$ is a convex polytope, it can be expressed as

<!-- chunk {"id": "body-0118", "role": "body", "section": "Application to a Ground Robot", "weight": 1.0} -->

Consider the nonholonomic ground robot modeled, where

<!-- chunk {"id": "body-0119", "role": "body", "section": "Application to a Ground Robot", "weight": 1.0} -->

Since $\mathcal{U}$ is a convex polytope, the admissible parameter set $\Theta$ is constructed using (7.2) with $\rho_{k} = 50$. Let $\Omega = {\mathbb{R}}^{d}$, which is convex and satisfies $0 \in \Omega$. Let $\mathcal{Z} = {({- \infty},1\rbrack}$, which is a convex polytope in $\mathbb{R}$ and satisfies $1 \in \mathcal{Z}$. The upper bound $z \leq 1$ ensures that $\overset{˙}{\gamma} = z \leq 1$, so the planning-time shift $\gamma$ does not advance faster than real time.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Application to a Ground Robot", "weight": 1.0} -->

Consider the map shown in Figure 3, which has $46$ circles and a wall. For $i \in {\{ 1,\ldots,46\}}$, the area outside the $i$th obstacle is modeled as the zero-superlevel set of

<!-- chunk {"id": "body-0121", "role": "body", "section": "Application to a Ground Robot", "weight": 1.0} -->

where $c_{i} \in {\mathbb{R}}^{2}$ and $r_{i} > 0$ are the center and radius of the $i$th circle. Similarly, the area inside the wall is modeled as the zero-superlevel set of

<!-- chunk {"id": "body-0122", "role": "body", "section": "Application to a Ground Robot", "weight": 1.0} -->

where $a > 0$ specifies the half-width of the square wall. The bounds on speed $v$ are modeled as the zero-superlevel sets of

<!-- chunk {"id": "body-0123", "role": "body", "section": "Application to a Ground Robot", "weight": 1.0} -->

The backup safe set $\mathcal{C}_{b}$ is given, where

<!-- chunk {"id": "body-0124", "role": "body", "section": "Application to a Ground Robot", "weight": 1.0} -->

The control objective is for the robot to move from its initial state to a desired state $x_{d} \triangleq \begin{bmatrix}
\end{bmatrix}^{\top} \in {\mathbb{R}}^{4}$ without violating safety (i.e., hitting an obstacle or violating speed bounds). To accomplish this objective, consider the cost function given, where

<!-- chunk {"id": "body-0125", "role": "body", "section": "Application to a Ground Robot", "weight": 1.0} -->

Minimizing the cost function drives the state toward the desired state $x_{d}$. The quadratic program includes the cost gradient as a linear term in the objective, which encourages ${\overline{u}}_{p \ast}$ to reduce the cost along the predicted trajectory. Thus, minimizing the quadratic program objective drives the state toward the minimizer of $\overline{J}$ while satisfying the safety constraints. This approach eliminates the need for an explicit reference control, unlike standard CBF methods where a desired control input must be specified.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Application to a Ground Robot", "weight": 1.0} -->

For comparison, we present simulation results with alternative control approaches. Specifically, we compare the proposed FlowBarrier method with nonlinear model predictive control (NMPC), and a constrained iterative linear quadratic regulator (CiLQR) paired with two different safety filters: a control barrier function filter (CiLQR-CBF) and a backup control barrier function filter (CiLQR-BCBF).

<!-- chunk {"id": "body-0127", "role": "body", "section": "Application to a Ground Robot", "weight": 1.0} -->

The NMPC approach solves a finite-horizon optimal control problem that minimizes the cost functional, where $R$ and $W$ are given, subject to the state constraint ${h_{s}{(x)}} \geq 0$ along the prediction horizon, the terminal constraint ${h_{b}{({x{(T)}})}} \geq 0$, and the input constraints $u \in \mathcal{U}$. The prediction horizon $T$ and discretization time step $T_{d}$ are set equal to those used in the FlowBarrier method. Since the terminal constraint enforces that the predicted terminal state lies within the forward invariant backup safe set $\mathcal{C}_{b}$, recursive feasibility of the NMPC is guaranteed.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Application to a Ground Robot", "weight": 1.0} -->

The CiLQR-CBF approach consists of two stages. First, a constrained iterative linear quadratic regulator is employed to compute a nominal control trajectory that minimizes the cost functional with $R$ and $W$ given, where the state constraint ${h_{s}{(x)}} \geq 0$ and the input constraints $u \in \mathcal{U}$ are enforced via an augmented Lagrangian method. The prediction horizon $T$ and discretization time step $T_{d}$ are set equal to those used in the FlowBarrier method. The resulting nominal control serves as the desired control input for a CBF safety filter, which solves a quadratic program that minimally modifies the desired control to enforce safety and input constraints (see for details).

<!-- chunk {"id": "body-0129", "role": "body", "section": "Application to a Ground Robot", "weight": 1.0} -->

The CiLQR-BCBF approach employs the same constrained iterative linear quadratic regulator to generate the desired control. However, instead of the standard CBF, a backup control barrier function (BCBF) method is used as the safety filter.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Application to a Ground Robot", "weight": 1.0} -->

The BCBF uses a backup controller that drives the robot to rest and solves a quadratic program that minimally modifies the desired control while ensuring the predicted trajectory under the backup controller remains in the safe set along the prediction horizon and satisfies a terminal safety condition, subject to input constraints $u \in \mathcal{U}$ (see for details).

<!-- chunk {"id": "body-0131", "role": "body", "section": "Application to a Ground Robot", "weight": 1.0} -->

All simulations are performed in Python on a laptop computer with an Intel Core i9-14900HX CPU and 32 GB of RAM. All methods are implemented using the CBFJAX framework, which is built on JAX and provides automatic differentiation and just-in-time compilation. Within the CBFJAX framework, the NMPC problem is solved using do-mpc with IPOPT, and the CiLQR problem is solved using trajax. All numerical ODE integration and adjoint computations are performed using Diffrax, and quadratic programming problems are solved using JaxOpt with OSQP.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Application to a Ground Robot", "weight": 1.0} -->

To compare methods across diverse conditions, we conduct $100$ navigation tasks constructed from a grid of initial and goal configurations. Specifically, $10$ initial states are uniformly sampled along the line from $x_{0} = {\lbrack{{- 8} - 8\;0\;0}\rbrack}^{\top}$ to ${\lbrack{\, 8 - {8\;0\pi}}\rbrack}^{\top}$, and $10$ goal states are uniformly sampled along the line from $x_{d} = {\lbrack{- 8\;8\;0\;0}\rbrack}^{\top}$ to ${\lbrack\, 8\;8\;0\;0\rbrack}^{\top}$, yielding $100$ distinct navigation tasks by pairing each initial state with each goal state. Each simulation is run for $20s$.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Application to a Ground Robot", "weight": 1.0} -->

For fair comparison, all methods employ the same running cost $R$ and terminal cost $W$ given, the same prediction horizon $T = {4s}$ and discretization time step $T_{d} = {0.05s}$, with the control trajectory initialized to zero. Parameters shared across all methods are set to identical values, while method-specific parameters are individually selected to achieve best performance for each approach.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Application to a Ground Robot", "weight": 1.0} -->

Trajectories are categorized as *reached* if they successfully arrive at the goal with ${\|{x - x_{d}}\|} \leq 0.5$ within $20s$, *stuck* if they fail to make progress, or *failed* if they violate safety constraints. Figure 3 shows the resulting trajectories for all methods. FlowBarrier achieves $88$ reached, $12$ stuck, and $0$ failed. NMPC achieves competitive performance with $85$ reached, $15$ stuck, and $0$ failed. CiLQR-CBF and CiLQR-BCBF demonstrate lower success rates, achieving $37$ reached, $55$ stuck, and $8$ failed, and $44$ reached, $55$ stuck, and $0$ failed, respectively.
