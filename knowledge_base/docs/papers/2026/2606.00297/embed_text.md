## Introduction

Autonomous robots are of interest for real-time navigation in proximity to obstacles, humans, and other robots. Applications include aerial inspection, warehouse logistics, and autonomous mobility. These applications require that robots achieve performance objectives (e.g., way-point navigation, coordination, formation) while maintaining safety and respecting control input limits (e.g., actuator saturation). Safety can be formalized as forward invariance of a prescribed safe set $\mathcal{C}_{s} \subseteq {\mathbb{R}}^{n}$. Frameworks for enforcing forward invariance include Hamilton-Jacobi reachability analysis, model predictive control, and barrier functions.

Control barrier functions (CBFs) provide techniques for selecting controls that enforce forward invariance. For a control-affine system, the CBF condition is affine in the control. In this case, a quadratic program (QP) can be used to compute a minimum-intervention control that ensures forward invariance of the CBF's zero-superlevel set. Thus, safety enforcement is achieved using a computationally efficient, real-time safety filter that can be implemented in a hierarchical architecture. However, two limitations constrain applicability of this approach.

First, synthesizing a valid CBF on a large subset of $\mathcal{C}_{s}$ is challenging due to control input constraints. Existing methods based on Hamilton-Jacobi reachability and sum-of-squares programming are limited to low-dimensional systems or restricted dynamics.

Second, even if a valid CBF is available, pointwise CBF-based optimization is myopic. Specifically, the safety certificate is enforced pointwise in time and depends only on the current state, with no consideration of how the trajectory will evolve over a future time horizon. As a result, the CBF does not account for conflicts between safety and performance that develop over the horizon---this can lead to aggressive corrections, conservative behavior, poor performance, and infeasibility or constraint violations in real-world implementation.

Backup-CBF methods have been developed to address the challenge of synthesizing a CBF subject to input limits. Instead of relying on a valid CBF on $\mathcal{C}_{s}$, backup-CBF methods specify a backup controller $u_{b}$ together with a backup set $\mathcal{C}_{b} \subset \mathcal{C}_{s}$ that is forward invariant under $u_{b}$. Then, the implicit control-forward-invariant subset of $\mathcal{C}_{s}$ is defined as the set of states from which the trajectory under $u_{b}$ is in $\mathcal{C}_{s}$ over a finite horizon and ends in $\mathcal{C}_{b}$ at the terminal time. This construction is conservative because the backup controller $u_{b}$ that makes $\mathcal{C}_{b}$ forward invariant is also used to drive the state to $\mathcal{C}_{b}$ by the terminal time. Thus, the implicit control-forward-invariant set is often small relative to the maximal control-forward-invariant subset of $\mathcal{C}_{s}$. Recent work has sought to mitigate this conservatism by delaying the switch from the nominal controller to $u_{b}$ until the last time at which the backup trajectory reaches $\mathcal{C}_{b}$ without leaving $\mathcal{C}_{s}$, or by composing multiple backup sets and backup controllers to enlarge the implicit control-forward-invariant subset of $\mathcal{C}_{s}$. Nevertheless, these methods still rely on fixed backup controllers to drive the state toward $\mathcal{C}_{b}$, and thus, conservatism persists. Another shortcoming of backup-CBF approaches is that the finite-horizon prediction is used only for safety certification, not for performance optimization. Furthermore, the control is still determined by a pointwise condition on the current state, with no mechanism to optimize cost over the prediction horizon.

The myopic nature of pointwise CBF-based optimization has been addressed by incorporating finite-horizon prediction into the safety certificate. One approach is to compose a finite-horizon planner with a CBF-based safety filter in a layered architecture. The planner solves its own optimization with discrete CBF constraints to generate a reference, and the safety filter then enforces barrier constraints on the applied control through the CBF. This layered design introduces at least one additional optimization beyond the CBF and does not address the validity of the barrier function. Even if the safety filter is replaced by a backup CBF to recover validity, the planner and the backup controller each propagate the system dynamics on a finite horizon for different purposes---one for cost and the other for safety, and these propagations are decoupled with potentially conflicting goals. A second approach avoids the layered structure and addresses prediction and safety in a single optimization. Specifically, propagates a trajectory under a fixed nominal controller and encodes its future safety into a barrier condition that is affine in the current control; however, the certified safe set is determined by the nominal controller, and feasibility under input constraints is not guaranteed. The approach in parametrizes the control trajectory to address invariance in trajectory space; however, the resulting QP is not guaranteed to be feasible, and thus safety is not guaranteed. Motivated by embedding CBF constraints in a receding-horizon optimization, several methods improve tractability through iterative linearization, sampling-based trajectory optimization with a closed-form CBF filter, or quadratic approximation of the cost-to-go; however, the validity of the barrier function at each step is assumed rather than established, and the underlying pointwise CBF condition can become infeasible under input constraints. In summary, existing methods that incorporate prediction into the safety certificate either decouple prediction from certification across separate optimizations, or rely on a single optimization whose feasibility under input constraints is not guaranteed.

This article presents a non-myopic real-time optimal control for simultaneous safety and performance with guaranteed feasibility in the presences of input constraints. First, the article introduces predicted-flow control barrier functions (P-CBFs), which can be used to certify safety of a predicted flow over a finite prediction horizon. The P-CBF generalizes the CBF concept from a function of the current state to a functional of the predicted flow under a parametrized control plan. Specifically, the control plan is parametrized by a finite-dimensional variable $\theta$ over a prediction horizon $T$, and the dynamics are propagated over this horizon under the control plan to obtain the predicted flow $\varphi$. A logical candidate P-CBF is the minimum of $h_{s}{(\varphi)}$ over the prediction horizon, where the safe set $\mathcal{C}_{s}$ is the zero-superlevel set of $h_{s}$, which is not assumed to be a valid CBF. However, this candidate P-CBF suffers from the same challenge as standard candidate CBFs---namely, control constraints make it difficult to guarantee and verify that the set of controls satisfying the P-CBF condition is nonempty. A natural remedy is to add a terminal candidate P-CBF that requires the predicted flow to end in a backup safe set $\mathcal{C}_{b}$ at the terminal time. Still, it remains difficult to guarantee that this candidate P-CBF pair is a valid P-CBF pair under input constraints.

Figure 1: The schematic illustrates the safe set 𝒞s, the backup set 𝒞b, the closed-loop trajectory x (t), and the predicted flows φ (τ;x,θ,γ) along the planning time τ. At each time t, the predicted flow propagates over the prediction window [γ (t), T], remains within 𝒞s, and terminates in 𝒞b at τ = T. The planning-time shift γ (t) modulates the prediction window, providing the degree of freedom that guarantees feasibility.

To address validity/feasibility, this article introduces a scalar planning-time shift $\gamma$ that modulates the prediction window, providing an additional degree of freedom in the optimization (see Figure 1). The planning-time shift $\gamma$ and control-plan parameter $\theta$ are treated as dynamic states and combined with the system state $x$ to form an augmented state $(x,\theta,\gamma)$. The applied control $u$, update of $\theta$, and evolution of $\gamma$ are then determined jointly as the solution of a single convex optimization that is guaranteed to be feasible at every time and whose solution makes the associated safe set forward invariant. The resulting safe optimal flow control provides a safety certificate over the entire prediction horizon and unifies cost optimization with safety certification in a single convex optimization whose feasibility under input constraints is guaranteed. If control constraints are a convex polytope, then the optimization reduces to a QP, named FlowBarrier.

This article is organized as follows. Section 2 reviews directional derivatives, and Section 3 introduces directional CBFs, which extends the idea CBFs to functions that are directionally differentiable but not necessarily continuously differentiable. These directional CBFs are used in Section 4 to introduce P-CBFs and show that P-CBFs can be used to obtain forward invariance in trajectory space. Section 5 formulates the safe optimal control problem addressed in this article. Then, Section 6 presents the safe optimal flow control solution with guaranteed feasibility, and Section 7 presents the QP implementation, named FlowBarrier. Section 8 applies FlowBarrier to a nonholonomic ground robot and compares the algorithm to nonlinear model predictive control and two CBF-based safety filters paired with an iterative linear-quadratic regulator planner across 100 trials, where FlowBarrier achieves the highest goal-reaching rate, zero safety violations, and the lowest computation time. The source code for FlowBarrier and all comparison methods is publicly available in CBFJAX, an open-source library developed alongside this work that provides automatic differentiation, just-in-time compilation, and a unified benchmarking environment for safe optimal control methods.

## Directional Derivatives

Let $\mathcal{D} \subseteq {\mathbb{R}}^{n}$, and let $\mu:{\mathcal{D}\rightarrow{\mathbb{R}}}$ be continuous. The radial cone $R_{\mathcal{D}}:{\mathcal{D}\rightrightarrows{\mathbb{R}}^{n}}$ is defined by

Note that if $x \in {{int}\mathcal{D}}$, then ${R_{\mathcal{D}}{(x)}} = {\mathbb{R}}^{n}$. The function $\mu$ is right-side directionally differentiable on $\mathcal{D}$ if for all ${(x,\nu)} \in {{\mathcal{D} \times R_{\mathcal{D}}}{(x)}}$,

exists. If $\mu$ is differentiable on $\mathcal{D}$, then ${D_{\nu}\mu{(x)}} = {L_{\nu}\mu{(x)}}$, where ${L_{\nu}\mu{(x)}} \triangleq {\mu^{\prime}{(x)}\nu}$ is the Lie derivative of $\mu$ along $\nu$. This article is not concerned with functions that are left-side directionally differentiable (i.e., $\lim_{s \uparrow 0}$) but not differentiable. Thus, for brevity, we omit "right-side" for the remainder of the article.

The next result concerns the time derivative of $\mu{({y{(t)}})}$ from the right side.

### Lemma 1

Assume $\mu$ is locally Lipschitz and directionally differentiable on $\mathcal{D}$. Let $y:{{\lbrack 0,\infty)}\rightarrow\mathcal{D}}$ be differentiable such that for all $t \geq 0$, ${\overset{˙}{y}{(t)}} \in {R_{\mathcal{D}}{({y{(t)}})}}$. Then, for all $t \geq 0$,

### Proof

Since $y$ is differentiable, it follows from the Taylor expansion that there exists $o:{{\lbrack 0,\infty)}\rightarrow{\mathbb{R}}^{n}}$ such that ${y{({t + s})}} = {{y{(t)}} + {s\overset{˙}{y}{(t)}} + {o{(s)}}}$ and ${\lim_{s \downarrow 0}{{\|{o{(s)}}\|}/s}} = 0$. Note that

Since $\mu$ is locally Lipschitz, there exists $M > 0$ such that ${|{\eta{(s)}}|} \leq {{M{\|{o{(s)}}\|}}/s}$, which implies that ${\lim_{s \downarrow 0}{\eta{(s)}}} = 0$. Thus, taking the limit of and using yields

which confirms that $\frac{d^{+}}{dt}\mu{({y{(t)}})}$ exists and is given . ∎

## Directional Control Barrier Functions

where $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ and $g:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n \times m}}$ are continuously differentiable on ${\mathbb{R}}^{n}$, ${x{(t)}} \in {\mathbb{R}}^{n}$ is the state, ${x{}} = x_{0} \in {\mathbb{R}}^{n}$ is the initial condition, and ${u{(t)}} \in \mathcal{U} \subseteq {\mathbb{R}}^{m}$ is the control. The control $u$ is an admissible control if for all $t \geq 0$, ${u{(t)}} \in \mathcal{U}$. Each solution to that appears in this article is assumed to exist and be unique on $\lbrack 0,\infty)$. For notational convenience, we define

which is the right-hand side of.

Let $h:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ be continuous, and define the zero-superlevel set

which is assumed to be nonempty and contain no isolated points.

Let $u_{fi}:{\mathcal{C}\rightarrow\mathcal{U}}$. Then, $\mathcal{C}$ is forward invariant with respect to with $u = u_{fi}$ if for all $x_{0} \in \mathcal{C}$, the solution to with $u = u_{fi}$ is such that for all $t \in {\lbrack 0,\infty)}$, ${x{(t)}} \in \mathcal{C}$.

A continuous function $a:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ is an extended class-$\mathcal{K}$ function if it is strictly increasing and ${a{}} = 0$.

### Definition 1

Assume $h$ is continuously differentiable on $\mathcal{C}$. Then, $h$ is a control barrier function (CBF) for on $\mathcal{C}$ if there exists an extended class-$\mathcal{K}$ function $\alpha$ such that for all $x \in \mathcal{C}$,

Definition 1 requires that $h$ is continuously differentiable. The next definition extends the concept of CBF to functions that are directionally differentiable but not necessarily differentiable.

### Definition 2

Assume $h$ is locally Lipschitz and directionally differentiable on $\mathcal{C}$. Then, $h$ is a directional control barrier function (D-CBF) for on $\mathcal{C}$ if there exists an extended class-$\mathcal{K}$ function $\alpha$ such that for all $x \in \mathcal{C}$,

If $h$ is continuously differentiable, then ${D_{{f{(x)}} + {g{(x)}\hat{u}}}h{(x)}} = {{L_{f}h{(x)}} + {L_{g}h{(x)}\hat{u}}}$. In this case, is equivalent to, and Definition 2 reduces to Definition 1. The concept of CBF can be further generalized using Dini derivatives (see ); however, Definition 2 suffices for this article.

Next, let ${h_{1},\ldots,h_{\ell}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ be continuous, and define

which is the intersection of the zero-superlevel sets of $h_{1},\ldots,h_{\ell}$. The next definition extends the concept of D-CBF to address multiple barrier functions and the intersection of their zero-superlevel sets.

### Definition 3

Assume $h_{1},\ldots,h_{\ell}$ are locally Lipschitz and directionally differentiable on $\mathcal{C}_{v}$. Then, $(h_{1},\ldots,h_{\ell})$ is a D-CBF $\ell$-tuple for on $\mathcal{C}_{v}$ if there exist extended class-$\mathcal{K}$ functions $\alpha_{1},\ldots,\alpha_{\ell}$ such that for all $x \in \mathcal{C}_{v}$, $K_{v}{(x)}$ is nonempty, where $K_{v}:{\mathcal{C}_{v}\rightrightarrows\mathcal{U}}$ is defined by

In the case where $\ell = 1$, $K_{v}{(x)}$ is nonempty if and only if with $h = h_{1}$ is satisfied. Thus, Definition 3 is equivalent to Definition 2 in the $\ell = 1$ case.

The next result shows that if $(h_{1},\ldots,h_{\ell})$ is a D-CBF $\ell$-tuple, then any control from $K_{v}{(x)}$ makes $\mathcal{C}_{v}$ forward invariant. This result extends the standard CBF result (e.g., \[2, Corollary 2\]) to D-CBFs.

### Theorem 1

Assume $(h_{1},\ldots,h_{\ell})$ is a D-CBF $\ell$-tuple for on $\mathcal{C}_{v}$, and let $u_{fi}:{\mathcal{C}_{v}\rightarrow\mathcal{U}}$ be such that for all $x \in \mathcal{C}_{v}$, ${u_{fi}{(x)}} \in {K_{v}{(x)}}$. Then, $\mathcal{C}_{v}$ is forward invariant with respect to with $u = u_{fi}$.

### Proof

Let $x_{0} \in \mathcal{C}_{v}$. For $i \in {\{ 1,\ldots,\ell\}}$, let $\eta_{i}:{{\lbrack 0,\infty)}\rightarrow{\mathbb{R}}}$ satisfy ${{\overset{˙}{\eta}}_{i}{(t)}} = {- {\alpha_{i}{({\eta_{i}{(t)}})}}}$, where ${\eta_{i}{}} = {h_{i}{(x_{0})}}$. Since ${h_{i}{(x_{0})}} \geq 0$ and $\alpha_{i}$ is an extended class-$\mathcal{K}$ function, it follows that for all $t \geq 0$, ${\eta_{i}{(t)}} \geq 0$.

Since $(h_{1},\ldots,h_{\ell})$ is a D-CBF $\ell$-tuple, Definition 3 implies that for all $x \in \mathcal{C}_{v}$, $K_{v}{(x)}$ is nonempty. Thus, Lemma 1 and imply that for all $i \in {\{ 1,\ldots,\ell\}}$ and all $t \geq 0$,

Hence, the comparison lemma \[20, Lemma 3.4\] implies that for all $i \in {\{ 1,\ldots,\ell\}}$ and all $t \geq 0$, ${h_{i}{({x{(t)}})}} \geq {\eta_{i}{(t)}} \geq 0$. Thus, for all $t \geq 0$, ${x{(t)}} \in \mathcal{C}_{v}$. ∎

## Predicted-Flow Control Barrier Functions

Let $T > 0$ be the planning-and-prediction horizon, and consider the control plan ${u_{p}{( \cdot;\theta)}}:{{\lbrack 0,T\rbrack}\rightarrow{\mathbb{R}}^{m}}$, which is parametrized by $\theta \in {\mathbb{R}}^{d}$. The control plan $u_{p}$ is continuous on ${\lbrack 0,T\rbrack} \times {\mathbb{R}}^{d}$, and for all $\tau \in {\lbrack 0,T\rbrack}$, $u_{p}{(\tau; \cdot )}$ is continuously differentiable on ${\mathbb{R}}^{d}$.

Let $k:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ be continuously differentiable, and define the admissible parameter set

where for all ${(\tau,\theta)} \in {{\lbrack 0,T\rbrack} \times \Theta}$, ${u_{p}{(\tau;\theta)}} \in \mathcal{U}$. The following example provides one construction for $u_{p}$.

### Example 1

Let ${\beta_{1},\ldots,\beta_{p}}:{{\lbrack 0,T\rbrack}\rightarrow{\mathbb{R}}}$ be continuous nonnegative functions such that for all $\tau \in {\lbrack 0,T\rbrack}$, ${\sum_{i = 1}^{p}{\beta_{i}{(\tau)}}} = 1$. Then, consider the control plan

where $\theta_{i} \in {\mathbb{R}}^{m}$, $\theta = {\lbrack{\theta_{1}^{\top}\theta_{2}^{\top}\ldots\theta_{p}^{\top}}\rbrack}^{\top} \in {\mathbb{R}}^{d}$, and $d = {pm}$. For each planning time $\tau$, the control plan is a convex combination of $\theta_{1},\ldots,\theta_{p}$. Thus, selecting $k$ such that $\Theta \subseteq \mathcal{U}^{p}$ is sufficient to satisfy the condition that for all ${(\tau,\theta)} \in {{\lbrack 0,T\rbrack} \times \Theta}$, ${u_{p}{(\tau;\theta)}} \in \mathcal{U}$. If $\mathcal{U}$ is a convex polytope, then it is possible to construct $k$ such that $\Theta \subseteq \mathcal{U}^{p}$ and $\Theta$ approximates $\mathcal{U}^{p}$. This construction is provided in Section 7.

One choice for $\beta_{1},\ldots,\beta_{p}$ are degree-one B-splines. Specifically, let $T_{p} \triangleq {T/{({p - 1})}}$, and for $i \in {\{ 1,\ldots,p\}}$, let

where $\sigma_{0} = 0$, and

Figure 2 illustrates the degree-one B-spline basis functions 10 and 11, and the resulting control plan. $▲$

Figure 2: First-degree B-spline basis functions β1, …, βp (top) and the resulting control plan ${u_{p}{(\tau;\theta)}} = {\sum_{i = 1}^{p}{\theta_{i}\beta_{i}{(\tau)}}}$ (bottom) on [0, T] with p = 4. At τ = (i−1) Tp, up equals θi, and up is piecewise linear.

The predicted flow ${\phi{( \cdot;x,\theta)}}:{{\lbrack 0,T\rbrack}\rightarrow{\mathbb{R}}^{n}}$ satisfies

which implies that $\phi{(\tau;x,\theta)}$ is the solution to at planning time $\tau \in {\lbrack 0,T\rbrack}$ with initial condition $x$ and $u = {u_{p}{( \cdot;\theta)}}$. In other words, $\phi{( \cdot;x,\theta)}$ is the flow of from state $x$ under the plan $u_{p}{( \cdot;\theta)}$ with parameter $\theta$. Differentiating with respect to $\tau$ yields

which is the evolution of the predicted flow $\phi$ given $(x,\theta)$.

At each time $t \geq 0$, the predicted flow $\phi{( \cdot;{x{(t)}},{\theta{(t)}})}$ depends on the current state $x{(t)}$ and parameter $\theta{(t)}$. The time evolution of $x$ is influenced by the control $u$. In order to influence the time evolution of $\theta$, we let $\theta:{{\lbrack 0,\infty)}\rightarrow{\mathbb{R}}^{d}}$ be the solution to

where ${\theta{}} = \theta_{0} \in {\mathbb{R}}^{d}$ and $\omega:{{\lbrack 0,\infty)}\rightarrow\Omega \subseteq {\mathbb{R}}^{d}}$ is the control input to the integrator.

Next, let ${H_{1},\ldots,H_{\ell}}:{{C{({\lbrack 0,T\rbrack},{\mathbb{R}}^{n})}}\rightarrow{\mathbb{R}}}$ be functionals such that for all $i \in {\{ 1,\ldots,\ell\}}$,

is locally Lipschitz and directionally differentiable on

Note that $\Psi$ is the set of $(x,\theta)$ such that the predicted flow $\phi$ mapped through each functional $H_{i}$ is nonnegative, and $\theta \in \Theta$, which implies that ${u_{p}{(\tau;\theta)}} \in \mathcal{U}$ for the entire planning horizon $\tau \in {\lbrack 0,T\rbrack}$.

We now introduce the concept of a predicted-flow CBF. This concept extends the notion of a D-CBF to address the $\ell$-tuple $(\psi_{1},\ldots,\psi_{\ell})$, where each $\psi_{i}$ is obtained by mapping $\phi$ through the functional $H_{i}$ and where $k$ defines the admissible parameters for the control plan.

### Definition 4

Assume $\psi_{1},\ldots,\psi_{\ell}$ given by are locally Lipschitz and directionally differentiable on $\Psi$. Then, $(\psi_{1},\ldots,\psi_{\ell})$ is a predicted-flow control barrier function (P-CBF) $\ell$-tuple for and on $\Psi$ given $u_{p}$ and $k$ if there exist extended class-$\mathcal{K}$ functions $\alpha_{1},\ldots,\alpha_{\ell},\beta$ such that for all ${(x,\theta)} \in \Psi$, $K_{\Psi}{(x,\theta)}$ is nonempty, where $K_{\Psi}:{\Psi\rightrightarrows{\mathcal{U} \times \Omega}}$ is defined by

The next result connects P-CBFs to D-CBFs.

### Proposition 1

$(\psi_{1},\ldots,\psi_{\ell})$ is a P-CBF $\ell$-tuple for and on $\Psi$ if and only if $(k,\psi_{1},\ldots,\psi_{\ell})$ is a D-CBF $({\ell + 1})$-tuple for and on $\Psi$.

### Proof

Since $k$ is continuously differentiable, note that

Thus, Definitions 3 and 4 imply that $(\psi_{1},\ldots,\psi_{\ell})$ is a P-CBF $\ell$-tuple on $\Psi$ given $k$ with associate point-to-set map $K_{\Psi}$ if and only if ${(h_{1},\ldots,h_{\ell},h_{\ell + 1})} = {(k,\psi_{1},\ldots,\psi_{\ell})}$ is a D-CBF $({\ell + 1})$-tuple on $\mathcal{C}_{v} = \Psi$ with associate map $K_{v} = K_{\Psi}$. ∎

### Remark 1

If there are no constraints on the control input (i.e., $\mathcal{U} = {\mathbb{R}}^{m}$), then $k$ can be selected as a positive constant. In this case, ${{k^{\prime}\hat{\omega}} + {\beta{(k)}}} = {\beta{(k)}} > 0$, which implies that the first inequality in is trivially satisfied. In this case, $(\psi_{1},\ldots,\psi_{\ell})$ is a P-CBF $\ell$-tuple on $\Psi$ if and only if $(\psi_{1},\ldots,\psi_{\ell})$ is a D-CBF $\ell$-tuple on $\Psi$.

The next result shows that if $(\psi_{1},\ldots,\psi_{\ell})$ is a P-CBF $\ell$-tuple on $\Psi$, then any control selected pointwise from $K_{\Psi}{(x,\theta)}$ makes $\Psi$ forward invariant. This result is a consequence of Theorem 1 and Proposition 1.

### Theorem 2

Assume $(\psi_{1},\ldots,\psi_{\ell})$ is a P-CBF $\ell$-tuple for and on $\Psi$, and let $K_{\Psi}{(x,\theta)}$ be given . Let $u_{fi}:{\Psi\rightarrow\mathcal{U}}$ and $\omega_{fi}:{\Psi\rightarrow\Omega}$ be such that for all ${(x,\theta)} \in \Psi$, ${({u_{fi}{(x,\theta)}},{\omega_{fi}{(x,\theta)}})} \in {K_{\Psi}{(x,\theta)}}$. Then, $\Psi$ is forward invariant with respect to and with ${(u,\omega)} = {(u_{fi},\omega_{fi})}$.

### Proof

Since $(\psi_{1},\ldots,\psi_{\ell})$ is a P-CBF $\ell$-tuple on $\Psi$, Proposition 1 implies that $(k,\psi_{1},\ldots,\psi_{\ell})$ is a D-CBF $({\ell + 1})$-tuple on $\Psi$. Since, in addition, ${({u_{fi}{(x,\theta)}},{\omega_{fi}{(x,\theta)}})} \in {K_{\Psi}{(x,\theta)}}$, it follows from Theorem 1 that $\Psi$ is forward invariant with respect to and with ${(u,\omega)} = {(u_{fi},\omega_{fi})}$. ∎

The following subsections present 2 useful candidate P-CBFs. These candidate P-CBFs are used in subsequent sections of this article.

### Minimum-Over-Prediction-Horizon P-CBF

We present a candidate P-CBF for the situation in which it is desirable for the predicted flow $\phi$ to be in a desired set throughout the prediction horizon $\lbrack 0,T\rbrack$. Specifically, let $h_{s}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ be continuously differentiable, and define

To determine whether $\phi$ is in $\mathcal{C}_{s}$ throughout the prediction horizon, consider the candidate P-CBF

Note that $\psi_{m}$ is nonnegative if and only if ${\phi{(\tau;x,\theta)}} \in \mathcal{C}_{s}$ for all prediction times $\tau \in {\lbrack 0,T\rbrack}$. Next, define

which is the set of $(x,\theta)$ such that ${\phi{(\tau;x,\theta)}} \in \mathcal{C}_{s}$ and ${u_{p}{(\tau;\theta)}} \in \mathcal{U}$ for all $\tau \in {\lbrack 0,T\rbrack}$.

The next result demonstrates that $\psi_{m}$ is locally Lipschitz and directionally differentiable, which implies that it satisfies the conditions in Definition 4 to be a candidate P-CBF. The result also provides an expression for the directional derivative of $\psi_{m}$, which depends on the following set

The proof is in the appendix.

### Proposition 2

Consider $\psi_{m}$ given , where $h_{s}$ is continuously differentiable on ${\mathbb{R}}^{n}$. Then, the following hold:

$\psi_{m}$ is locally Lipschitz on ${\mathbb{R}}^{n} \times {\mathbb{R}}^{d}$.

$\psi_{m}$ is directionally differentiable on ${\mathbb{R}}^{n} \times {\mathbb{R}}^{d}$, and

The next result shows that the directional derivative ((b) ‣ Proposition 2. ‣ 4.1 Minimum-Over-Prediction-Horizon P-CBF ‣ 4 Predicted-Flow Control Barrier Functions ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control")) of $\psi_{m}$ along the trajectories of and satisfies a given lower bound if and only if a family of related lower bounds are satisfied, where each is affine in the control variables $(\hat{u},\hat{\omega})$. This result is an immediate consequence of part (b) ‣ Proposition 2. ‣ 4.1 Minimum-Over-Prediction-Horizon P-CBF ‣ 4 Predicted-Flow Control Barrier Functions ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") of Proposition 2.

### Proposition 3

Let $c \in {\mathbb{R}}$, and let ${(x,\theta,\hat{u},\hat{\omega})} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}^{d} \times \mathcal{U} \times \Omega}$. Then,

if and only if for all $\tau \in {\mathcal{T}{(x,\theta)}}$,

### Remark 2

Proposition 3 implies that the control variables $(\hat{u},\hat{\omega})$ satisfy the directional derivative constraint

if and only if $(\hat{u},\hat{\omega})$ satisfy the family of affine constraints with $c = {- {\alpha{({\psi_{m}{(x,\theta)}})}}}$. Similar to standard CBFs, these affine constraints are useful for control synthesis.

### Terminal-Prediction-Time P-CBF

This subsection presents a candidate P-CBF for the situation in which it is desirable for the predicted flow $\phi$ to be in a desired set at the terminal prediction time (i.e., $\tau = T$). Specifically, let $h_{b}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ be continuously differentiable, and define

Then, consider the candidate P-CBF

and associate set

Note that $\Psi_{t}$ is the set of $(x,\theta)$ such that ${\phi{(T;x,\theta)}} \in \mathcal{C}_{b}$ and ${u_{p}{(\tau;\theta)}} \in \mathcal{U}$ for all $\tau \in {\lbrack 0,T\rbrack}$.

The next result demonstrates that $\psi_{t}$ is continuously differentiable. Thus, the directional derivative equals the Lie derivative, and the Lie derivative along the trajectories of 4 and 13 is affine in the control variables $(\hat{u},\hat{\omega})$.

### Proposition 4

Consider $\psi_{t}$ given , where $h_{b}$ is continuously differentiable on ${\mathbb{R}}^{n}$. Then, $\psi_{t}$ is continuously differentiable on ${\mathbb{R}}^{n} \times {\mathbb{R}}^{d}$, and

### Proof

Since $h_{b}$ is continuously differentiable and $\phi{(T;x,\theta)}$ is continuously differentiable on ${\mathbb{R}}^{n} \times {\mathbb{R}}^{d}$, it follows that ${\psi_{t}{(x,\theta)}} = {h_{b}{({\phi{(T;x,\theta)}})}}$ is continuously differentiable on ${\mathbb{R}}^{n} \times {\mathbb{R}}^{d}$. Thus, ${D_{\nu}\psi_{t}{(x,\theta)}} = {L_{\nu}\psi_{t}{(x,\theta)}}$. ∎

### Remark 3

Equations and are two useful candidate P-CBFs used in this article. However, mapping the predicted flow $\phi$ through other functionals can yield other potentially useful candidate P-CBFs. For example, consider the candidate P-CBF obtained by integrating a function of the flow over time, specifically, ${\psi_{int}{(x,\theta)}} = {a + {\int_{0}^{T}{b{({\phi{(\tau;x,\theta)}})}{d\tau}}}}$, where $a \in {\mathbb{R}}$ and $b:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is continuously differentiable. This candidate P-CBF can be used to capture the energy of the predicted flow.

## Problem Formulation

For the remainder of this article, we consider the problem of designing admissible feedback controls $(u,\omega)$ that minimize an integral cost of the predicted flow $\phi$ over the prediction horizon such that the predicted flow $\phi{( \cdot;{x{(t)}},{\theta{(t)}})}$ and actual state $x{(t)}$ are in a prescribed safe set $\mathcal{C}_{s}$ for all time $t \geq 0$. The safe set $\mathcal{C}_{s}$ is given , where $h_{s}$ is continuously differentiable and known. We assume the admissible control sets $\mathcal{U}$ and $\Omega$ are convex, and $0 \in \Omega$.

Notably, $h_{s}$ is not assumed to be a CBF for on $\mathcal{C}_{s}$. Similarly, $\psi_{m}$ given by is not assumed to be a P-CBF for 4 and 13 on $\Psi_{m}$, which is given . Thus, it is not necessarily possible to make $\mathcal{C}_{s}$ or $\Psi_{m}$ forward invariant.

Next, consider the cost $J:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}}$ given by

where $W:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ and $R:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}}$ are continuously differentiable. The objective is to minimize $J$ while ensuring the predicted flow is in $\mathcal{C}_{s}$ and the control and control-plan parameters are admissible. The objective is formalized as follows.

### Problem 1

Design feedback controls for ${u{(t)}} \in \mathcal{U}$ and ${\omega{(t)}} \in \Omega$ such that for each time $t \geq 0$, the receding horizon cost $J{({x{(t)}},{\theta{(t)}})}$ is optimized subject to the constraints:

For all ${(t,\tau)} \in {{\lbrack 0,\infty)} \times {\lbrack 0,T\rbrack}}$, ${\phi{(\tau;{x{(t)}},{\theta{(t)}})}} \in \mathcal{C}_{s}$.

For all $t \geq 0$, ${\theta{(t)}} \in \Theta$.

Constraints (C1) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") and (C2) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") can be re-framed in terms of forward invariance. Note that (C1) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") and (C2) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") are satisfied if and only if for all $t \geq 0$, ${({x{(t)}},{\theta{(t)}})} \in \Psi_{m}$. Thus, (C1) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") and (C2) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") are satisfied by designing ${u{(t)}} \in \mathcal{U}$ and ${\omega{(t)}} \in \Omega$ that make a subset of $\Psi_{m}$ forward invariant.

Since $h_{s}$ is not assumed to be a CBF, and $\psi_{m}$ is not assumed to be a P-CBF, it may not be possible to satisfy (C1) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") and (C2) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control"). To ensure the problem is well posed, we assume there exists a subset of $\mathcal{C}_{s}$ that can be made forward invariant with respect to. Specifically, consider a backup safe set $\mathcal{C}_{b} \subset \mathcal{C}_{s}$, which is given , where $h_{b}$ is continuously differentiable and known. We make the following assumption.

### Assumption 1

There exists a known extended class-$\mathcal{K}$ function $\alpha_{b}:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ such that for all $x \in \mathcal{C}_{b}$,

Assumption 1 implies that $h_{b}$ is a CBF for on $\mathcal{C}_{b}$. Thus, $\mathcal{C}_{b}$ can be made forward invariant with respect to. However, $\mathcal{C}_{b}$ may be small relative to $\mathcal{C}_{s}$. Thus, it is not desirable for the predicted flow $\phi{(\tau;{x{(t)}},{\theta{(t)}})}$ to be in $\mathcal{C}_{b}$ for all prediction times $\tau \in {\lbrack 0,T\rbrack}$ or for all real time $t \geq 0$. Such a restriction on $\phi$ can lead to large $J$, that is, poor performance. Instead, Assumption 1 is used to introduce a terminal-prediction-time condition on the predicted flow. Specifically, we consider the condition that for all time $t \geq 0$, the predicted flow $\phi{( \cdot;{x{(t)}},{\theta{(t)}})}$ at terminal prediction time $T$ is in $\mathcal{C}_{b}$. This condition can be re-framed in terms of forward invariance by considering $\psi_{t}$ and $\Psi_{t}$ given by and. Specifically, for all $t \geq 0$, ${\phi{(T;{x{(t)}},{\theta{(t)}})}} \in \mathcal{C}_{b}$ and ${\theta{(t)}} \in \Theta$ if and only if for all $t \geq 0$, ${({x{(t)}},{\theta{(t)}})} \in \Psi_{t}$. Thus, the terminal condition can be satisfied by designing controls ${u{(t)}} \in \mathcal{U}$ and ${\omega{(t)}} \in \Omega$ that make a subset of $\Psi_{t}$ forward invariant.

Since $J$ can be nonlinear and nonconvex, Problem 1 cannot necessarily be solved with a convex optimization. However, the time derivative of $J$ along the trajectories of and is

To make the time derivative of $J$ small, consider the quadratic cost

where $Q_{u} \in {\mathbb{R}}^{m \times m}$ and $Q_{\omega} \in {\mathbb{R}}^{d \times d}$ are positive definite. The first 2 terms of make $\frac{dJ}{dt}$ small, whereas the other 2 terms provide regularization that make strictly convex. Specifically, ${\hat{\omega}}^{\top}Q_{\omega}\hat{\omega}$ limits the rate of change of the control plan parameter $\theta$ and ${\lbrack{\hat{u} - {u_{p}{(0;\theta)}}}\rbrack}^{\top}Q_{u}{\lbrack{\hat{u} - {u_{p}{(0;\theta)}}}\rbrack}$ limits deviation of the executed control from the control plan. Hence, minimizing the quadratic cost $\mathcal{J}$ subject to (C1) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") and (C2) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") yields gradient flow that aims to decrease $J$ along the trajectories of and. Thus, we address Problem 1 by solving the following problem.

### Problem 2

Design feedback controls for ${u{(t)}} \in \mathcal{U}$ and ${\omega{(t)}} \in \Omega$ such that for each time $t \geq 0$, the quadratic cost $\mathcal{J}{(\hat{u},\hat{\omega};{x{(t)}},{\theta{(t)}})}$ is minimized subject to (C1) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") and (C2) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control").

The following subsections present solutions to Problem 2 in special circumstances: A. $\psi_{m}$ is a P-CBF, and B. $(\psi_{m},\psi_{t})$ is a P-CBF pair. These special circumstances can be difficult to satisfy and/or verify, which motivates the remainder of this article, where we present a solution to Problem 2 without these assumptions.

### Solution if $\psi_{m}$ is a P-CBF

This subsection addresses the case where $\psi_{m}$ is a P-CBF on $\Psi_{m}$ for and. In this case, Definition 4 implies that there exist extended class-$\mathcal{K}$ functions $\alpha,\beta$ such that for all ${(x,\theta)} \in \Psi_{m}$,

is nonempty. The next result shows that $\mathcal{J}$ has a unique global minimizer over the set $K_{m}{(x,\theta)}$.

### Proposition 5

Assume $\mathcal{U}$ and $\Omega$ are convex, and $\psi_{m}$ is a P-CBF on $\Psi_{m}$ for and. Then, for all ${(x,\theta)} \in \Psi_{m}$, $K_{m}{(x,\theta)}$ is convex, and $\mathcal{J}{(\hat{u},\hat{\omega};x,\theta)}$ has a unique global minimizer over $K_{m}{(x,\theta)}$.

### Proof

Since ${F{(x,\hat{u})}} = {{f{(x)}} + {g{(x)}\hat{u}}}$ is affine in $\hat{u}$, it follows from (5.1) and Proposition 3 that $K_{m}{(x,\theta)}$ is the intersection of the convex sets $\mathcal{U}$ and $\Omega$ with a family of affine half-spaces, and thus, it is convex.

Since $K_{m}{(x,\theta)}$ is nonempty and convex, and $\mathcal{J}$ is strictly convex in $(\hat{u},\hat{\omega})$, the minimizer exists and is unique. ∎

The next result solves Problem 2 where $\psi_{m}$ is a P-CBF.

### Corollary 1

Assume $\mathcal{U}$ and $\Omega$ are convex, and $\psi_{m}$ is a P-CBF on $\Psi_{m}$ for and. For all ${(x,\theta)} \in \Psi_{m}$, define

Then, $\Psi_{m}$ is forward invariant with respect to and with ${(u,\omega)} = {(u_{\ast},\omega_{\ast})}$. Furthermore, (C1) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") and (C2) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") are satisfied.

### Proof

Since $\psi_{m}$ is a P-CBF and ${({u_{\ast}{(x,\theta)}},{\omega_{\ast}{(x,\theta)}})} \in {K_{m}{(x,\theta)}}$, Theorem 2 implies that $\Psi_{m}$ is forward invariant with respect to and with ${(u,\omega)} = {(u_{\ast},\omega_{\ast})}$.

Since ${({x{(t)}},{\theta{(t)}})} \in \Psi_{m}$ implies ${\psi_{m}{({x{(t)}},{\theta{(t)}})}} \geq 0$ and ${k{({\theta{(t)}})}} \geq 0$, it follows from 18 and 8 that (C1) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") and (C2) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") are satisfied. ∎

### Remark 4

If $\mathcal{U}$ and $\Omega$ are convex polytopes, then Proposition 3 implies that all constraints that define $K_{m}{(x,\theta)}$ are affine. In this case, the optimal control can be obtained efficiently from a QP that depends on the predicted flow. Section 7 addresses implementation of these QPs.

### Remark 5

Corollary 1 requires that $\psi_{m}$ is a P-CBF, which is generally difficult to satisfy and verify because it requires that for each ${(x,\theta)} \in \Psi_{m}$, there exist ${(\hat{u},\hat{\omega})} \in {\mathcal{U} \times \Omega}$ that satisfies both constraints in $K_{m}{(x,\theta)}$. In general, control input constraints (i.e., $\mathcal{U}$ and $\Omega$) can lead to points where $K_{m}{(x,\theta)}$ is empty. Even if $\psi_{m}$ is a P-CBF, it may be difficult to determine the class-$\mathcal{K}$ functions $\alpha,\beta$ such that $K_{m}{(x,\theta)}$ is nonempty for all ${(x,\theta)} \in \Psi_{m}$.

### Solution if $(\psi_{m},\psi_{t})$ is a P-CBF pair

This subsection addresses the case where $(\psi_{m},\psi_{t})$ is a P-CBF pair on $\Psi_{mt} \triangleq {\Psi_{m} \cap \Psi_{t}}$, which is a subset of $\Psi_{m}$ created by imposing the condition that the predicted flow $\phi$ is in the backup safe set at the terminal prediction time. Since $(\psi_{m},\psi_{t})$ is a P-CBF pair, Definition 4 implies that there exist extended class-$\mathcal{K}$ functions $\alpha_{1},\alpha_{2},\beta$ such that for all ${(x,\theta)} \in \Psi_{mt}$,

is nonempty. The next result shows that $\mathcal{J}$ has a unique global minimizer over $K_{mt}{(x,\theta)}$. The proof is similar to that of Proposition 5.

### Proposition 6

Assume $\mathcal{U}$ and $\Omega$ are convex, and $(\psi_{m},\psi_{t})$ is a P-CBF pair on $\Psi_{mt}$ for and. Then, for all ${(x,\theta)} \in \Psi_{mt}$, $K_{mt}{(x,\theta)}$ is convex, and $\mathcal{J}{(\hat{u},\hat{\omega};x,\theta)}$ has a unique global minimizer over $K_{mt}{(x,\theta)}$.

The following result solves Problem 2 where $(\psi_{m},\psi_{t})$ is a P-CBF pair. The proof is similar to that of Corollary 1.

### Corollary 2

Assume $\mathcal{U}$ and $\Omega$ are convex, and $(\psi_{m},\psi_{t})$ is a P-CBF pair on $\Psi_{mt}$ for and. For all ${(x,\theta)} \in \Psi_{mt}$, define

Then, $\Psi_{mt}$ is forward invariant with respect to and with ${(u,\omega)} = {(u_{\ast},\omega_{\ast})}$. Furthermore, (C1) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") and (C2) ‣ Problem 1. ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") are satisfied.

### Remark 6

Similar to Remark 4, if $\mathcal{U}$ and $\Omega$ are convex polytopes, then Proposition 3 implies that all constraints that define $K_{mt}{(x,\theta)}$ are affine. In this case, the optimal control (32 is a P-CBF pair ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control")) is the solution to a QP.

### Remark 7

The optimal control (32 is a P-CBF pair ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control")) in this subsection makes $\Psi_{mt}$ forward invariant in the case where $(\psi_{m},\psi_{t})$ is a P-CBF pair. It is worth noting that $\Psi_{mt} \subset \Psi_{m}$ because (32 is a P-CBF pair ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control")) is concerned not only with keeping the predicted flow $\phi{( \cdot;{x{(t)}},{\theta{(t)}})}$ in the safe set $\mathcal{C}_{s}$ but also with keeping the predicted flow $\phi{(T;{x{(t)}},{\theta{(t)}})}$ at the terminal prediction time $T$ in the backup safe set $\mathcal{C}_{b}$. This terminal-prediction constraint focuses on achieving forward invariance for the subset $\Psi_{mt}$ because $\Psi_{m}$ cannot generally be made forward invariant if $\psi_{m}$ is not a P-CBF. Intuitively, it may seem more likely that $\Psi_{mt}$ can be made forward invariant than $\Psi_{m}$. However, the constraints in $K_{mt}$ are also more restrictive than those in $K_{m}$. Similar to Remark 5, it is generally difficult to satisfy and/or verify the condition that $(\psi_{m},\psi_{t})$ is a P-CBF pair. Even if $(\psi_{m},\psi_{t})$ is a P-CBF pair, it may be difficult to determine the class-$\mathcal{K}$ functions $\alpha_{1},\alpha_{2},\beta$ such that $K_{mt}{(x,\theta)}$ is nonempty for all ${(x,\theta)} \in \Psi_{mt}$.

The optimal controls in Corollaries 1 and 2 is a P-CBF pair ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") rely on assumptions that are difficult to satisfy and/or verify. The following section addresses these challenges by introducing a planning-time shift that guarantees feasibility of a convex optimization used to obtain optimal controls without requiring that $\psi_{m}$ is a P-CBF or that $(\psi_{m},\psi_{t})$ is a P-CBF pair. Moreover, this convex optimization is a QP in the case where $\mathcal{U}$ and $\Omega$ are convex polytopes.

## Safe Optimal Flow Control

This section solves Problem 2 by introducing a planning-time shift that guarantees feasibility of the optimization that determines $(u,\omega)$. The key idea is to augment the state with a planning-time shift, which allows the prediction horizon to shrink as necessary to guarantee feasibility.

### Predicted Flow with Planning Time Shift

We extend the definition for the predicted flow $\phi{( \cdot;x,\theta)}$ to allow for a time shift in the control plan $u_{p}{( \cdot;\theta)}$. Let $\gamma \in {\lbrack 0,T\rbrack}$ be the planning-time shift, and let the predicted flow ${\varphi{( \cdot;x,\theta,\gamma)}}:{{\lbrack\gamma,T\rbrack}\rightarrow{\mathbb{R}}^{n}}$ satisfy

For $\gamma = 0$, $\varphi{(\tau;x,\theta,0)}$ reduces to. In other words, $\varphi{(\tau;x,\theta,0)}$ is the solution to at planning time $\tau$, where $x$ is the initial condition and ${u{(t)}} = {u_{p}{(t;\theta)}}$. For $\gamma \in {(0,T\rbrack}$, $\varphi{(\tau;x,\theta,\gamma)}$ is the solution to at planning time $\tau - \gamma$, where $x$ is the initial condition and ${u{(t)}} = {u_{p}{({t + \gamma};\theta)}}$, which implies that the control plan is shifted by $\gamma$. Differentiating with respect to $\tau$ yields

which is the evolution of the predicted flow $\varphi$ given $(x,\theta,\gamma)$.

The planning-time shift $\gamma$ is the continuous-time analogue to shrinking the horizon in discrete-time receding-horizon control. In this work, we use the planning-time shift $\gamma$ to guarantee feasibility of an optimization that is used to generate the control and update the control plan. This can be viewed as the continuous-time analogue to the recursive-feasibility approach in discrete-time MPC. As $\gamma$ increases, the remaining prediction window $\lbrack\gamma,T\rbrack$ shrinks.

Similar to the approach used with $\theta$, we introduce dynamics to influence the time evolution of $\gamma$. Specifically, let $\gamma:{{\lbrack 0,\infty)}\rightarrow{\mathbb{R}}}$ be the solution to

where ${\gamma{}} = \gamma_{0} \in {\lbrack 0,T\rbrack}$, $z:{{\lbrack 0,\infty)}\rightarrow\mathcal{Z}}$ is the control input to the integrator, $\mathcal{Z} \subseteq {\mathbb{R}}$ is a closed interval, and $1 \in \mathcal{Z}$.

For notational convenience, we write and as

where $\overline{n} \triangleq {n + d + 1}$ and $\overline{m} \triangleq {m + d + 1}$.

### Control Forward Invariant Set

Consider predicted-flow barrier functions

which are analogous to and but incorporate the planning-time shift. Next, define

which is the set of $\overline{x}$ such that the predicted flow satisfies ${\varphi{(\tau;\overline{x})}} \in \mathcal{C}_{s}$ for all prediction times $\tau \in {\lbrack\gamma,T\rbrack}$; the predicted flow satisfies the terminal condition ${\varphi{(T;\overline{x})}} \in \mathcal{C}_{b}$; the control-plan parameter $\theta$ is in the admissible set $\Theta$; and the planning-time shift $\gamma$ is in the admissible set $\lbrack 0,T\rbrack$. Note that $\overline{\Psi}$ is analogous to $\Psi_{mt}$ but incorporates the planning-time shift.

The remainder of this subsection focuses on demonstrating that there exists a control $\overline{u}$ that makes $\overline{\Psi}$ forward invariant. Consider the backup control $u_{b}:{\mathcal{C}_{b}\rightarrow\mathcal{U}}$ defined by

which exists and is unique because ${\|\hat{u}\|}^{2}$ is strictly convex, and $K_{b}{(x)}$ is nonempty and convex. The next result demonstrates that $u_{b}$ makes $\mathcal{C}_{b}$ forward invariant. The proof is in the appendix.

### Proposition 7

Assume Assumption 1 is satisfied. Then, $\mathcal{C}_{b}$ is forward invariant with respect to with $u = u_{b}$. Furthermore, if $\mathcal{U}$ is compact, then $u_{b}$ is continuous on $\mathcal{C}_{b}$.

Let ${\overline{u}}_{fb}:{\overline{\Psi}\rightarrow{\mathcal{U} \times \Omega \times \mathcal{Z}}}$ be given by

where ${{\overline{u}}_{p},{\overline{u}}_{b}}:{\overline{\Psi}\rightarrow{\mathcal{U} \times \Omega \times \mathcal{Z}}}$ are given by

It follows from 13, 34, 42, and 43 that the control $\overline{u} = {\overline{u}}_{fb}$ results in constant control-plan parameters, that is, ${\theta{(t)}} = \theta_{0}$, and a planning-time shift that increases linearly with time until it reaches $T$, specifically, ${\gamma{(t)}} = {\min{\{{t + \gamma_{0}},T\}}}$. Thus, ${\overline{u}}_{fb}$ results in control $u$ that follows the control plan $u_{p}$ for $t \in {\lbrack 0,{T - \gamma_{0}})}$ and switches to the backup control $u_{b}$ at $t = {T - \gamma_{0}}$. The next result shows that ${\overline{u}}_{fb}$ makes $\overline{\Psi}$ forward invariant.

### Proposition 8

Assume Assumption 1 is satisfied. Then, $\overline{\Psi}$ is forward invariant with respect to 35, 36, and 37 with $\overline{u} = {\overline{u}}_{fb}$. Furthermore, for all ${\overline{x}}_{0} \in \overline{\Psi}$, the following hold:

For all $t \in {\lbrack{T - \gamma_{0}},\infty)}$, ${x{(t)}} \in \mathcal{C}_{b}$.

If $\mathcal{U}$ is compact, then ${\overline{u}}_{fb}{({\overline{x}{( \cdot )}})}$ is continuous on ${\lbrack 0,\infty)} \smallsetminus {\{{T - \gamma_{0}}\}}$.

### Proof

Let ${\overline{x}}_{0} \in \overline{\Psi}$. Since $\overline{u} = {\overline{u}}_{fb}$, it follows from 13, 34, 42, and 43 that ${\theta{(t)}} = \theta_{0}$, ${\gamma{(t)}} = {\min{\{{t + \gamma_{0}},T\}}}$, and

where $t_{s} \triangleq {T - \gamma_{0}}$. To show forward invariance of $\overline{\Psi}$, we consider the time intervals $\lbrack 0,t_{s}\rbrack$ and $(t_{s},\infty)$.

First, we show that for all $t \in {\lbrack 0,t_{s}\rbrack}$, ${\overline{x}{(t)}} \in \overline{\Psi}$. Note that 4, 33, and 44 imply that for all $t \in {\lbrack 0,t_{s}\rbrack}$, ${x{(t)}} = {\varphi{({t + \gamma_{0}};{\overline{x}}_{0})}}$. Thus, implies that for all $t \in {\lbrack 0,t_{s}\rbrack}$ and all $\tau \in {\lbrack{t + \gamma_{0}},T\rbrack}$,

Hence, 38 implies that for all $t \in {\lbrack 0,t_{s}\rbrack}$,

and 39 implies that for all $t \in {\lbrack 0,t_{s}\rbrack}$,

Since, in addition, ${k{({\theta{(t)}})}} = {k{(\theta_{0})}} \geq 0$ and ${\gamma{(t)}} \in {\lbrack 0,T\rbrack}$, it follows from (6.2) that for all $t \in {\lbrack 0,t_{s}\rbrack}$, ${\overline{x}{(t)}} \in \overline{\Psi}$.

Next, we show that for all $t \in {\lbrack t_{s},\infty)}$, ${\overline{x}{(t)}} \in \overline{\Psi}$. Since ${\overline{x}{(t_{s})}} \in \overline{\Psi}$ and ${\gamma{(t_{s})}} = T$, it follows from that ${h_{b}{({x{(t_{s})}})}} = {{\overline{\psi}}_{t}{({\overline{x}{(t_{s})}})}} \geq 0$, which implies ${x{(t_{s})}} \in \mathcal{C}_{b}$. Since ${x{(t_{s})}} \in \mathcal{C}_{b}$ and ${u{(t)}} = {u_{b}{({x{(t)}})}}$, Proposition 7 implies that for all $t \in {\lbrack t_{s},\infty)}$, ${x{(t)}} \in \mathcal{C}_{b}$, which confirms (a) ‣ Proposition 8. ‣ 6.2 A Control Forward Invariant Set ‣ 6 Safe Optimal Flow Control ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control"). Since, in addition, $\mathcal{C}_{b} \subset \mathcal{C}_{s}$, and for all $t \in {\lbrack t_{s},\infty)}$, ${\theta{(t)}} = \theta_{0}$ and ${\gamma{(t)}} = T$, it follows from 38 and 39 that for all $t \in {\lbrack t_{s},\infty)}$, ${{\overline{\psi}}_{m}{({\overline{x}{(t)}})}} = {h_{s}{({x{(t)}})}} \geq 0$, and ${{\overline{\psi}}_{t}{({\overline{x}{(t)}})}} = {h_{b}{({x{(t)}})}} \geq 0$. Thus, for all $t \in {\lbrack t_{s},\infty)}$, ${\overline{x}{(t)}} \in \overline{\Psi}$, which confirms that $\overline{\Psi}$ is forward invariant.

To prove (b) ‣ Proposition 8. ‣ 6.2 A Control Forward Invariant Set ‣ 6 Safe Optimal Flow Control ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control"), Proposition 7 implies that $u_{b}$ is continuous on $\mathcal{C}_{b}$. Since, in addition, $u_{p}{( \cdot;\theta_{0})}$ is continuous on $\lbrack 0,T\rbrack$, it follows from that $u$ is continuous on ${\lbrack 0,\infty)} \smallsetminus {\{ t_{s}\}}$, which combined with 42 and 43 confirms (b) ‣ Proposition 8. ‣ 6.2 A Control Forward Invariant Set ‣ 6 Safe Optimal Flow Control ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control"). ∎

### Controls that Make $\overline{\Psi}$ Forward Invariant

Although ${\overline{u}}_{fb}$ makes $\overline{\Psi}$ forward invariant, this control does not generally optimize the cost. Thus, this section provides a set of controls $\overline{u}$ that make $\overline{\Psi}$ forward invariant. In fact, this section shows that $\overline{\Psi}$ is made forward invariant by any control that satisfies P-CBF-like constraints, which are similar to section 5.2 is a P-CBF pair ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control").

First, we extend Proposition 2 to address the planning-time shift. The result demonstrates that ${\overline{\psi}}_{m}$ is locally Lipschitz and directionally differentiable, and provides an expression for the directional derivative of ${\overline{\psi}}_{m}$, which depends on the following set

The proof is in the appendix.

### Proposition 9

Consider ${\overline{\psi}}_{m}$ given , where $h_{s}$ is continuously differentiable on ${\mathbb{R}}^{n}$. Then, the following hold:

${\overline{\psi}}_{m}$ is locally Lipschitz on $\overline{\Psi}$.

${\overline{\psi}}_{m}$ is directionally differentiable on $\{{\overline{x} \in \overline{\Psi}}:{\gamma \neq T}\}$, and for all $\overline{x} \in {\{{\overline{x} \in \overline{\Psi}}:{\gamma \neq T}\}}$,

where $\mathbf{1}_{\{{\tau = \gamma}\}}$ is the indicator function.

### Remark 8

The directional derivative ((b) ‣ Proposition 9. ‣ 6.3 Controls that Make Ψ̄ Forward Invariant ‣ 6 Safe Optimal Flow Control ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control")) differs from ((b) ‣ Proposition 2. ‣ 4.1 Minimum-Over-Prediction-Horizon P-CBF ‣ 4 Predicted-Flow Control Barrier Functions ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control")) because the planning-time shift $\gamma$ appears in the left end point of the feasible set $\lbrack\gamma,T\rbrack$ for the minimization. In contrast, the minimization without the planning-time shift is over the constant feasible set $\lbrack 0,T\rbrack$. The inclusion of $\gamma$ results in the extra term $\mathbf{1}_{\{{\tau = \gamma}\}}\frac{\partial\varphi}{\partial\tau}\frac{\partial\gamma}{\partial\overline{x}}$, which impacts the directional derivative if and only if the minimizer is at the left endpoint $\gamma$ and accounts for the effect of moving the feasible set $\lbrack\gamma,T\rbrack$ on ${\overline{\psi}}_{m}$.

The next result extends Proposition 3 to address the planning-time shift. This result is an immediate consequence of part (b) ‣ Proposition 9. ‣ 6.3 Controls that Make Ψ̄ Forward Invariant ‣ 6 Safe Optimal Flow Control ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") of Proposition 9.

### Proposition 10

Let $\overline{x} \in \overline{\Psi}$ with $\gamma \in {\lbrack 0,T)}$, $\hat{\overline{u}} \in {\mathcal{U} \times \Omega \times \mathcal{Z}}$, and $c \in {\mathbb{R}}$. Then,

if and only if for all $\tau \in {\overline{\mathcal{T}}{(\overline{x})}}$,

### Remark 9

Proposition 10 implies that the control variable $\hat{\overline{u}}$ satisfies the directional derivative constraint

if and only if $\hat{\overline{u}}$ satisfies the family of affine constraints with $c = {- {\alpha_{m}{({{\overline{\psi}}_{m}{(\overline{x})}})}}}$.

The directional derivative of ${\overline{\psi}}_{m}$ along the trajectories of 35, 36, and 37 depends on the sensitivity

where differentiating with respect to $x$, $\theta$, and $\gamma$ yields

Section 7 addresses numerically efficient computation of these sensitivities using the adjoint method.

Next, we define a control constraint set that is similar to section 5.2 is a P-CBF pair ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") but addresses the planning-time shift. Let $\alpha_{m},\alpha_{\theta},\alpha_{\gamma}$ be extended class-$\mathcal{K}$ functions, and for all $\overline{x} \in {\{{\overline{x} \in \overline{\Psi}}:{\gamma \neq T}\}}$, consider $\overline{K}:{\overline{\Psi}\rightrightarrows{\mathcal{U} \times \Omega \times \mathcal{Z}}}$ defined by

Corollary 2 is a P-CBF pair ‣ 5 Problem Formulation ‣ Predicted-Flow Control Barrier Functions for Real-Time Safe Optimal Control") requires that $(\psi_{m},\psi_{t})$ is a P-CBF pair to guarantee that the control constraint set $K_{mt}{(x,\theta)}$ is nonempty. Moreover, implementation of the constraint set requires knowledge of specific class-$\mathcal{K}$ functions that make $K_{mt}{(x,\theta)}$ nonempty. The next result shows that $\overline{K}{(\overline{x})}$ is nonempty. The result does not require that $({\overline{\psi}}_{m},{\overline{\psi}}_{t})$ is a P-CBF pair, and it holds for any choice of extended class-$\mathcal{K}$ functions $\alpha_{m},\alpha_{\theta},\alpha_{\gamma}$.

### Theorem 3

For all $\overline{x} \in {\{{\overline{x} \in \overline{\Psi}}:{\gamma \neq T}\}}$, $\overline{K}{(\overline{x})}$ is nonempty.

### Proof

Let ${\overline{x}}_{e} \in {\{{\overline{x} \in \overline{\Psi}}:{\gamma \neq T}\}}$, and we write its components as ${\overline{x}}_{e} = {\lbrack{x_{e}^{\top}\theta_{e}^{\top}\gamma_{e}}\rbrack}^{\top}$. It follows from that ${{\overline{u}}_{p}{({\overline{x}}_{e})}} = {\lbrack{u_{e}^{\top}\omega_{e}^{\top}z_{e}}\rbrack}^{\top}$, where

We show that ${{\overline{u}}_{p}{({\overline{x}}_{e})}} \in {\overline{K}{({\overline{x}}_{e})}}$. To do so, define

First, since ${\overline{x}}_{e} \in \overline{\Psi}$, $\omega_{e} = 0_{d \times 1}$, and $z_{e} = 1$, it follows that

To show that $c_{3} \geq 0$, define

and using 47, 48, 49, 36, and 37 yields

Next, 47 and 49 imply that ${\eta{(\gamma_{e})}} = 0$ and

Since ${\eta{(\gamma_{e})}} = 0$, it follows from that for all $\tau \in {\lbrack\gamma_{e},T\rbrack}$, ${\eta{(\tau)}} = 0$. Using ${\eta{(T)}} = 0$, and ${\overline{x}}_{e} \in \overline{\Psi}$, it follows that

To show that $c_{4} \geq 0$, it follows from 36 and 37 that ${\frac{\partial\gamma}{\partial\overline{x}}{({{\overline{f}{({\overline{x}}_{e})}} + {\overline{g}{({\overline{x}}_{e})}{\overline{u}}_{p}{({\overline{x}}_{e})}}})}} = z_{e} = 1$. Since, in addition, ${\eta{(\tau)}} = 0$ for all $\tau \in {\lbrack\gamma_{e},T\rbrack}$, it follows from Proposition 9 that

We consider 2 cases: $\gamma_{e} \in {\overline{\mathcal{T}}{({\overline{x}}_{e})}}$ and $\gamma_{e} \notin {\overline{\mathcal{T}}{({\overline{x}}_{e})}}$. First, consider $\gamma_{e} \in {\overline{\mathcal{T}}{({\overline{x}}_{e})}}$, which implies that $\gamma_{e}$ is a minimizer of $h_{s}{({\varphi{(\tau;{\overline{x}}_{e})}})}$ at the left endpoint of $\lbrack\gamma_{e},T\rbrack$. Thus, ${h_{s}^{\prime}{({\varphi{(\gamma_{e};{\overline{x}}_{e})}})}F{({\varphi{(\gamma_{e};{\overline{x}}_{e})}},{u_{p}{(\gamma_{e};\theta_{e})}})}} \geq 0$. Since, in addition, ${\overline{x}}_{e} \in \overline{\Psi}$, it follows from (6.2) that $c_{4} \geq {\alpha_{m}{({{\overline{\psi}}_{m}{({\overline{x}}_{e})}})}} \geq 0$. Next, consider $\gamma_{e} \notin {\overline{\mathcal{T}}{({\overline{x}}_{e})}}$, and it follows from (6.2) that $c_{4} = {\alpha_{m}{({{\overline{\psi}}_{m}{({\overline{x}}_{e})}})}} \geq 0$.

Finally, since ${c_{1},c_{2},c_{3},c_{4}} \geq 0$, it follows from 51, 52, 53, 54, and 6.3 that ${{\overline{u}}_{p}{({\overline{x}}_{e})}} \in {\overline{K}{({\overline{x}}_{e})}}$. ∎

Theorem 3 shows that for all $\overline{x} \in {\{{\overline{x} \in \overline{\Psi}}:{\gamma \neq T}\}}$, the constraints in (6.3) are feasible. The next result can be viewed as an extension of Theorem 2 that uses the planning-time shift to remove the assumption that $({\overline{\psi}}_{m},{\overline{\psi}}_{t})$ is a P-CBF pair. The result shows that $\overline{\Psi}$ is made forward invariant by any control selected pointwise from $\overline{K}{(\overline{x})}$ for all $\overline{x} \in {\{{\overline{x} \in \overline{\Psi}}:{\gamma \neq T}\}}$ and equal to ${\overline{u}}_{b}{(\overline{x})}$ for all $\overline{x} \in {\{{\overline{x} \in \overline{\Psi}}:{\gamma = T}\}}$.

### Theorem 4

Assume Assumption 1 is satisfied. Let ${\overline{u}}_{fi}:{\overline{\Psi}\rightarrow{\mathcal{U} \times \Omega \times \mathcal{Z}}}$ be such that for all $\overline{x} \in {\{{\overline{x} \in \overline{\Psi}}:{\gamma \neq T}\}}$, ${{\overline{u}}_{fi}{(\overline{x})}} \in {\overline{K}{(\overline{x})}}$, and for all $\overline{x} \in {\{{\overline{x} \in \overline{\Psi}}:{\gamma = T}\}}$, ${{\overline{u}}_{fi}{(\overline{x})}} = {{\overline{u}}_{b}{(\overline{x})}}$. Then, $\overline{\Psi}$ is forward invariant with respect to with $\overline{u} = {\overline{u}}_{fi}$.

### Proof

Let ${\overline{x}}_{0} \in \overline{\Psi}$, and consider two cases: (i) ${\gamma{(t)}} < T$ for all $t \geq 0$; and (ii) there exists $t_{1} \geq 0$ such that ${\gamma{(t_{1})}} = T$.

For case (i), since ${\gamma{(t)}} < T$ for all $t \geq 0$, it follows that ${{\overline{u}}_{fi}{({\overline{x}{(t)}})}} \in {\overline{K}{({\overline{x}{(t)}})}}$ for all $t \geq 0$. Since ${{\overline{u}}_{fi}{(\overline{x})}} \in {\overline{K}{(\overline{x})}}$ satisfies (6.3), ${\overline{\psi}}_{m}$ is locally Lipschitz and directionally differentiable by Proposition 9, and ${\overline{\psi}}_{t}$ and $k$ are continuously differentiable, it follows from Lemma 1 that

Let ${\eta_{m},\eta_{t},\eta_{\theta},\eta_{\gamma}}:{{\lbrack 0,\infty)}\rightarrow{\mathbb{R}}}$ satisfy ${\overset{˙}{\eta}}_{m} = {- {\alpha_{m}{(\eta_{m})}}}$, ${\overset{˙}{\eta}}_{t} = {- {\alpha_{b}{(\eta_{t})}}}$, ${\overset{˙}{\eta}}_{\theta} = {- {\alpha_{\theta}{(\eta_{\theta})}}}$, ${\overset{˙}{\eta}}_{\gamma} = {- {\alpha_{\gamma}{(\eta_{\gamma})}}}$, where ${\eta_{m}{}} = {{\overline{\psi}}_{m}{({\overline{x}}_{0})}}$, ${\eta_{t}{}} = {{\overline{\psi}}_{t}{({\overline{x}}_{0})}}$, ${\eta_{\theta}{}} = {k{(\theta_{0})}}$, ${\eta_{\gamma}{}} = \gamma_{0}$. Since ${\overline{x}}_{0} \in \overline{\Psi}$ implies ${\eta_{m}{}} \geq 0$, ${\eta_{t}{}} \geq 0$, ${\eta_{\theta}{}} \geq 0$, and ${\eta_{\gamma}{}} \geq 0$, and each $\alpha_{m}$, $\alpha_{b}$, $\alpha_{\theta}$, $\alpha_{\gamma}$ is an extended class-$\mathcal{K}$ function, it follows that for all $t \geq 0$, ${\eta_{m}{(t)}} \geq 0$, ${\eta_{t}{(t)}} \geq 0$, ${\eta_{\theta}{(t)}} \geq 0$, and ${\eta_{\gamma}{(t)}} \geq 0$. It follows from 56, 57, 58, and 59 and the comparison lemma \[20, Lemma 3.4\] that for all $t \geq 0$, ${{\overline{\psi}}_{m}{({\overline{x}{(t)}})}} \geq {\eta_{m}{(t)}} \geq 0$, ${{\overline{\psi}}_{t}{({\overline{x}{(t)}})}} \geq {\eta_{t}{(t)}} \geq 0$, ${k{({\theta{(t)}})}} \geq {\eta_{\theta}{(t)}} \geq 0$, and ${\gamma{(t)}} \geq {\eta_{\gamma}{(t)}} \geq 0$. Since ${\gamma{(t)}} < T$ for all $t \geq 0$, it follows that ${\gamma{(t)}} \in {\lbrack 0,T\rbrack}$ for all $t \geq 0$. Since ${\overline{K}{(\overline{x})}} \subseteq {\mathcal{U} \times \Omega \times \mathcal{Z}}$ implies ${u{(t)}} \in \mathcal{U}$ for all $t \geq 0$, it follows that ${\overline{x}{(t)}} \in \overline{\Psi}$ for all $t \geq 0$.

For case (ii), since ${\gamma{(t)}} < T$ for all $t \in {\lbrack 0,t_{1})}$, it follows from case (i) that for all $t \in {\lbrack 0,t_{1})}$, ${\overline{x}{(t)}} \in \overline{\Psi}$. Since ${\overline{x}{(t_{1})}} \in \overline{\Psi}$ and ${\gamma{(t_{1})}} = T$, it follows from that ${h_{b}{({x{(t_{1})}})}} = {{\overline{\psi}}_{t}{({\overline{x}{(t_{1})}})}} \geq 0$, which implies ${x{(t_{1})}} \in \mathcal{C}_{b}$. Since ${x{(t_{1})}} \in \mathcal{C}_{b}$ and ${{\overline{u}}_{fi}{(\overline{x})}} = {{\overline{u}}_{b}{(\overline{x})}}$ for $\gamma = T$, it follows from that ${u{(t)}} = {u_{b}{({x{(t)}})}}$ for all $t \geq t_{1}$. Since ${x{(t_{1})}} \in \mathcal{C}_{b}$, Proposition 7 implies that for all $t \in {\lbrack t_{1},\infty)}$, ${x{(t)}} \in \mathcal{C}_{b}$. Since, in addition, $\mathcal{C}_{b} \subset \mathcal{C}_{s}$, and for all $t \in {\lbrack t_{1},\infty)}$, ${\gamma{(t)}} = T$, it follows from 38 and 39 that for all $t \in {\lbrack t_{1},\infty)}$, ${{\overline{\psi}}_{m}{({\overline{x}{(t)}})}} = {h_{s}{({x{(t)}})}} \geq 0$ and ${{\overline{\psi}}_{t}{({\overline{x}{(t)}})}} = {h_{b}{({x{(t)}})}} \geq 0$. Thus, for all $t \geq 0$, ${\overline{x}{(t)}} \in \overline{\Psi}$. ∎

### Optimization-Based Control

This section presents the safe optimal flow control that optimizes the integral cost while guaranteeing that ${\overline{x}{(t)}} \in \overline{\Psi}$ for all $t \geq 0$. Consider the cost $\overline{J}:{{\mathbb{R}}^{\overline{n}}\rightarrow{\mathbb{R}}}$ given by

which is analogous to except $\phi$ is replaced by $\varphi$. For $\gamma = 0$, $\overline{J}{(\overline{x})}$ reduces to $J{(x,\theta)}$. To make the time derivative of $\overline{J}$ small, we consider a quadratic cost that is analogous to. Specifically, consider the quadratic cost

where $Q_{z} > 0$ and $\lambda \geq 0$. Similar to, the first 3 terms make $\frac{d\overline{J}}{dt}$ small, and the next 3 terms provide regularization that make (6.4) strictly convex. The final term $\lambda\hat{z}$ penalizes increasing $\gamma$. In other words, this incentivizes a large planning horizon $T - \gamma$.

### Remark 10

Since $\overline{J}$ involves an integral over $\lbrack\gamma,T\rbrack$, it follows that increasing $\gamma$ shrinks the prediction window, which can decrease $\overline{J}$. Consequently, the term $\frac{\partial\overline{J}}{\partial\gamma}\hat{z}$ in (6.4) can incentivize increasing $\gamma$ to reduce $\overline{J}$. This effect is not generally desirable; rather it is desirable for $\gamma$ to increase if and only if needed for feasibility. This work includes the $\lambda\hat{z}$ with relatively large $\lambda$ to mitigate this effect. The effect can also be mitigated by omitting $\frac{\partial\overline{J}}{\partial\gamma}\hat{z}$ from (6.4) and/or multiplying the integral in by $\frac{T}{T - \gamma}$ to provide normalization. All 3 methods are effective in simulation.

The next result extends Proposition 5 and shows that $\overline{\mathcal{J}}$ has a unique global minimizer over $\overline{K}{(\overline{x})}$. The proof is similar to that of Proposition 5.

### Proposition 11

Assume $\mathcal{U}$, $\Omega$, and $\mathcal{Z}$ are convex. Then, for all $\overline{x} \in {\{{\overline{x} \in \overline{\Psi}}:{\gamma \neq T}\}}$, the following hold:

${\operatorname{argmin}\limits_{\hat{\overline{u}} \in {\overline{K}{(\overline{x})}}}\overline{\mathcal{J}}}{(\hat{\overline{u}};\overline{x})}$ exists and is unique.

$\overline{K}{(\overline{x})}$ is convex.

For all $\overline{x} \in {\{{\overline{x} \in \overline{\Psi}}:{\gamma \neq T}\}}$, define

where it follows from Proposition 11 that ${\overline{u}}_{p \ast}{(\overline{x})}$ exists and is unique.

### Remark 11

Similar to Remark 4, if $\mathcal{U}$, $\Omega$, and $\mathcal{Z}$ are convex polytopes, then Proposition 10 implies that all constraints that define $\overline{K}{(\overline{x})}$ are affine. In this case, the optimal control can be obtained efficiently from a QP that depends on the predicted flow $\varphi$. Section 7 presents implementation of this QP.

Finally, consider the safe optimal flow control ${\overline{u}}_{\ast}:{\overline{\Psi}\rightarrow{\mathcal{U} \times \Omega \times \mathcal{Z}}}$ defined by

The term $\lambda\hat{z}$ in (6.4) incentivizes $\gamma$ to be close to zero; however, it does not prevent $\gamma = T$. The constraint set $\overline{K}{(\overline{x})}$ is not well defined for $\gamma = T$ because the directional derivative of ${\overline{\psi}}_{m}$ does not necessarily exist. Hence, if $\gamma = T$, then control ${\overline{u}}_{\ast}$ switches to ${\overline{u}}_{b}$.

The next result shows that the safe optimal flow control ${\overline{u}}_{\ast}$ makes $\overline{\Psi}$ forward invariant. This result is an immediate consequence of Theorem 4 because ${{\overline{u}}_{\ast}{(\overline{x})}} \in {\overline{K}{(\overline{x})}}$ for all $\overline{x} \in {\{{\overline{x} \in \overline{\Psi}}:{\gamma \neq T}\}}$ and ${{\overline{u}}_{\ast}{(\overline{x})}} = {{\overline{u}}_{b}{(\overline{x})}}$ for all $\overline{x} \in {\{{\overline{x} \in \overline{\Psi}}:{\gamma = T}\}}$.

### Corollary 3

Assume $\mathcal{U}$, $\Omega$, and $\mathcal{Z}$ are convex, and assume Assumption 1 is satisfied. Then, $\overline{\Psi}$ is forward invariant with respect to with $\overline{u} = {\overline{u}}_{\ast}$.

Corollary 3 implies that for all ${(t,\tau)} \in {{\lbrack 0,\infty)} \times {\lbrack{\gamma{(t)}},T\rbrack}}$, ${\varphi{(\tau;{\overline{x}{(t)}})}} \in \mathcal{C}_{s}$; and for all $t \geq 0$, ${\varphi{(T;{\overline{x}{(t)}})}} \in \mathcal{C}_{b}$ and ${\theta{(t)}} \in \Theta$. Thus, ${\overline{u}}_{\ast}$ guarantees that the predicted flow $\varphi{( \cdot;{\overline{x}{(t)}})}$ and actual state $x{(t)}$ are in the safe set $\mathcal{C}_{s}$ for all time $t \geq 0$, while minimizing $\overline{\mathcal{J}}$, which aims to decrease the receding-horizon cost $\overline{J}$ along the trajectories of.

## QP Implementation of Safe Optimal Flow Control

This section presents a QP implementation of the safe optimal flow control. For this section, we assume $\mathcal{U}$, $\Omega$, and $\mathcal{Z}$ are convex polytopes.

### Numerical Implementation

Proposition 10 implies that the constraint on ${\overline{\psi}}_{m}$ in (6.3) is equivalent to the family of affine constraints. Thus, can be expressed as

${{\overline{u}}_{p \ast}{(\overline{x})}} = {{\operatorname{argmin}\limits_{\hat{\overline{u}} \in {\mathcal{U} \times \Omega \times \mathcal{Z}}}\overline{\mathcal{J}}}{(\hat{\overline{u}};\overline{x})}}$ (64a)
${{{k^{\prime}{(\theta)}\hat{\omega}} + {\alpha_{\theta}{({k{(\theta)}})}}} \geq 0},$ (64b)
$h_{s}^{\prime}{({\varphi{(\tau;\overline{x})}})}\left\lbrack {{\frac{\partial\varphi}{\partial\overline{x}}{(\tau;\overline{x})}} + {\mathbf{1}_{\{{\tau = \gamma}\}}\frac{\partial\varphi}{\partial\tau}{(\tau;\overline{x})}\frac{\partial\gamma}{\partial\overline{x}}}} \right\rbrack$
$\times {(\overline{f}{(\overline{x})} + \overline{g}{(\overline{x})}\hat{\overline{u}})} + \alpha_{m}{({\overline{\psi}}_{m}{(\overline{x})})} \geq 0,\forall\tau \in \overline{\mathcal{T}}{(\overline{x})},$ (64c)
${{{L_{\overline{f}}{\overline{\psi}}_{t}{(\overline{x})}} + {L_{\overline{g}}{\overline{\psi}}_{t}{(\overline{x})}\hat{\overline{u}}} + {\alpha_{b}{({{\overline{\psi}}_{t}{(\overline{x})}})}}} \geq 0},$ (64d)
${{\hat{z} + {\alpha_{\gamma}{(\gamma)}}} \geq 0}.$ (64e)

All constraints in are affine. However, (64c) may constitute infinitely many affine constraints because $\overline{\mathcal{T}}{(\overline{x})}$ may contain infinitely many points. Thus, is a semi-infinite QP, which can be solved with a variety of approaches; see. This article uses a discretization method over the planning time, where $\overline{\mathcal{T}}{(\overline{x})}$ is approximated with a finite set.

Let $N$ be a positive integer, and define $T_{d} \triangleq \frac{T - \gamma}{N}$. Then, consider the set

which contains the discrete prediction times in ${\{{\gamma + {iT_{d}}}\}}_{i = 0}^{N}$ at which $h_{s}{({\varphi{( \cdot;\overline{x})}})}$ attains its minimum. The approximation ${\overline{\mathcal{T}}}_{e}{(\overline{x})}$ converges to $\overline{\mathcal{T}}{(\overline{x})}$ as $N\rightarrow\infty$. Furthermore, replacing $\overline{\mathcal{T}}{(\overline{x})}$ with ${\overline{\mathcal{T}}}_{e}{(\overline{x})}$ in (64c) yields a QP with a finite number of affine constraints.

### Remark 12

The approximation can be improved by using the sign changes of ${\frac{d}{d\tau}h_{s}{({\varphi{(\tau;\overline{x})}})}} = {h_{s}^{\prime}{({\varphi{(\tau;\overline{x})}})}F{({\varphi{(\tau;\overline{x})}},{u_{p}{(\tau;\theta)}})}}$ evaluated at $\tau \in {\{{\gamma + {iT_{d}}}\}}_{i = 0}^{N}$ to bracket local critical points. Then, the discretization time step can be refined (e.g., midpoint refinement or bisection) in the appropriate intervals.

### Remark 13

In practice, $h_{s}{({\varphi{( \cdot;\overline{x})}})}$ often has a unique global minimizer over $\lbrack\gamma,T\rbrack$. In this case, (64c) reduces to a single affine constraint.

The QP requires the gradients

for $\tau \in {{\overline{\mathcal{T}}}_{e}{(\overline{x})}}$. These can be computed using a forward sensitivity approach, where $\frac{\partial\varphi}{\partial\overline{x}}{(\tau;\overline{x})}$ is obtained by solving -- forward in prediction time alongside the predicted flow. However, this approach requires integrating a system of ordinary differential equations with dimension $n{({n + d + 1})}$, which is quadratic in $n$ and scales with the number of plan parameters $d$.

Alternatively, the adjoint approach is a more computationally efficient method to compute. The advantage is that each adjoint ordinary differential equation has dimension $n$. Specifically, since $\overline{J}$, ${\overline{\psi}}_{t}$, and $h_{s}{({\varphi{(\tau;\overline{x})}})}$ are scalar functions of $\overline{x}$, each gradient in can be computed with an adjoint $n$-dimensional backward integration. The gradients of $\overline{J}$ and ${\overline{\psi}}_{t}$ require backward integration from $T$ to $\gamma$, while the gradient of $h_{s}{({\varphi{(\tau;\overline{x})}})}$ at each $\tau \in {{\overline{\mathcal{T}}}_{e}{(\overline{x})}}$ requires backward integration from $\tau$ to $\gamma$. Thus, all gradients are computed by integrating $2 + n_{e}$ different $n$-dimensional ordinary differential equations, where $n_{e}$ is the number of elements in ${\overline{\mathcal{T}}}_{e}{(\overline{x})}$. Hence, the complexity is linear in $n$ and does not increase with $d$, which implies that the adjoint method has significant computational benefit for large $n$ and/or large $d$. We also note that the $2 + n_{e}$ differential equations are decoupled from one another and can be solved in parallel.

Algorithm 1 summarizes FlowBarrier, which is the QP implementation of the safe optimal flow control where ${\deltat} > 0$ is the time increment for a zero-order hold on the control ${\overline{u}}_{\ast}$. We write the components of ${\overline{u}}_{\ast}$ as $\left. {\overline{u}}_{\ast} = {\left\lbrack \begin{matrix}
\end{matrix} \right.} \right\rbrack$. At each time step, Algorithm 1 has 4 steps: (i) forward integration of to obtain the predicted flow $\varphi$, and evaluate ${\overline{\psi}}_{m}$, ${\overline{\psi}}_{t}$, and $k$; (ii) backward integration of the $2 + n_{e}$ parallel adjoint ordinary differential equations to obtain; (iii) solve QP with ${\overline{\mathcal{T}}}_{e}$ replacing $\overline{\mathcal{T}}$ to obtain ${\overline{u}}_{p \ast}$; and (iv) execute control $u_{\ast}$ and update $\theta$ and $\gamma$ by integrating optimal derivatives $\omega_{\ast}$ and $z_{\ast}$ over time increment $\deltat$. If $\gamma = T$, then steps (ii) and (iii) are replaced by solving the QP to obtain the backup ${\overline{u}}_{b}$.

4 $\overline{x}\leftarrow\left\lbrack {x^{\top}\theta^{\top}\gamma} \right\rbrack^{\top}$
5 Solve for $\left\{ {\varphi\left( {\gamma + {iT_{d}}};\overline{x} \right)} \right\}_{i = 0}^{N}$
6 ${\overline{\psi}}_{m}\leftarrow{\text{(}\text{)}}$, ${\overline{\psi}}_{t}\leftarrow{\text{(}\text{)}}$, ${\overline{\mathcal{T}}}_{e}\leftarrow{\text{(}\text{)}}$
13 Compute $\frac{\partial\overline{J}}{\partial\overline{x}}$, $\frac{\partial{\overline{\psi}}_{t}}{\partial\overline{x}}$, and $\frac{\partial}{\partial\overline{x}}h_{s}\left( {\varphi\left( \tau;\overline{x} \right)} \right)$ for all $\tau \in {\overline{\mathcal{T}}}_{e}$
14 [u*⊤ ω*⊤ z*]⊤← solution to with ${\overline{\mathcal{T}}}_{e}$ replacing $\overline{\mathcal{T}}$
// Update control plan

### Remark 14

Although external disturbances, model uncertainties, or sampled-data effects can cause $\overline{x}$ to leave $\overline{\Psi}$, it follows from Theorem 3 that ${\{{\overline{x} \in \overline{\Psi}}:{\gamma \neq T}\}} \subseteq {\{\overline{x}:{{\overline{K}{(\overline{x})}} \neq \varnothing}\}}$. Thus, may be feasible for $\overline{x} \notin \overline{\Psi}$. If $\overline{x} \notin \overline{\Psi}$ and $\overline{K}{(\overline{x})}$ is nonempty, then ${\overline{u}}_{p \ast}{(\overline{x})}$ drives $\overline{x}$ back to $\overline{\Psi}$. If $\overline{K}{(\overline{x})}$ is empty, then slack variables can be used to ensure the QP is feasible while trying to drive $\overline{x}$ back to $\overline{\Psi}$.

### Remark 15

If there is a time $t_{1} \geq 0$ such that ${\gamma{(t_{1})}} = T$, then the control results in $u_{\ast} = u_{b}$ and $\gamma = T$ for all $t \geq t_{1}$. Thus, does not have a mechanism to decrease $\gamma$ and recover the prediction window. Simulations suggest that it may be unlikely that $\gamma$ increases to $T$; however, if this occurs, then there is a practical approach to recover the prediction window. To explain, consider the QP

${{\min\limits_{\substack{\hat{\overline{u}} \in {\mathcal{U} \times \Omega \times \mathcal{Z}} \\ {{\hat{\delta}}_{m},{\hat{\delta}}_{t}} \in {\mathbb{R}}}}\overline{\mathcal{J}}}{(\hat{\overline{u}};\overline{x})}} + {Q_{\delta}{({{\hat{\delta}}_{m}^{2} + {\hat{\delta}}_{t}^{2}})}} + {\lambda_{\delta}{({{\hat{\delta}}_{m} + {\hat{\delta}}_{t}})}}$ (67a)
${{{k^{\prime}{(\theta)}\hat{\omega}} + {\alpha_{\theta}{({k{(\theta)}})}}} \geq 0},$ (67c)
${{{D_{{\overline{f}{(\overline{x})}} + {\overline{g}{(\overline{x})}\hat{\overline{u}}}}{\overline{\psi}}_{m}{(\overline{x})}} + {\hat{\delta}}_{m}} \geq 0},$ (67d)
${{{L_{\overline{f}}{\overline{\psi}}_{t}{(\overline{x})}} + {L_{\overline{g}}{\overline{\psi}}_{t}{(\overline{x})}\hat{\overline{u}}} + {\hat{\delta}}_{t}} \geq 0},$ (67e)
${{\hat{z} + {\alpha_{\gamma}{(\gamma)}}} \geq 0},$ (67f)

where $Q_{\delta} > 0$ and $\lambda_{\delta} \geq 0$. For all $\overline{x} \in {\overline{\mathcal{C}}}_{b} \triangleq {\{\overline{x}:{{x \in \mathcal{C}_{b}},{{\theta \in \Theta},{\gamma \in {\lbrack 0,T)}}}}\}}$, the constraints 67b, 67c, 67d, 67e, and 67f are feasible. Specifically, $\overline{x} \in {\overline{\mathcal{C}}}_{b}$, $\hat{\omega} = 0$ and $\hat{z} = 0$ satisfy 67c and 67f; Assumption 1 implies that there exists $\hat{u} \in \mathcal{U}$ satisfying (67b); and the slack variables ${\hat{\delta}}_{m}$ and ${\hat{\delta}}_{t}$ can be selected to satisfy 67d and 67e. Since, in addition, (67a) is strictly convex, it follows that for all $\overline{x} \in {\overline{\mathcal{C}}}_{b}$, the QP has a unique solution, which we denoted by $\left. {\left( {\overline{u}}_{r}{(\overline{x})},\delta_{m}{(\overline{x})},\delta_{t}{(\overline{x})} \right.} \right)$.

If there is a time $t_{1} \geq 0$ such that ${\gamma{(t_{1})}} = T$, then the prediction window may be recovered with the following procedure. First, set ${\gamma{(t_{1})}} = 0$, select ${\theta{(t_{1})}} \in \Theta$, and let ${\overline{u}{(\overline{x})}} = {{\overline{u}}_{r}{(\overline{x})}}$, which attempts to drive $\overline{x}$ to $\overline{\Psi}$ while making $\mathcal{C}_{b}$ forward invariant. Next, if there exists a time $t_{2} > t_{1}$ such that ${\overline{x}{(t_{2})}} \in \overline{\Psi}$, then switch the control back to.

### Soft-Minimum Construction for $h_{s}$, $h_{b}$, and $k$

In this article, the safe set $\mathcal{C}_{s}$, backup set $\mathcal{C}_{b}$, and admissible parameter set $\Theta$ are each defined as the zero-superlevel set of one function (i.e., $h_{s}$, $h_{b}$, and $k$, respectively). In practice, it can be useful to define each set as the intersection of zero-superlevel sets of multiple functions. The approaches and analysis in this article extend directly to the case where $\mathcal{C}_{s}$, $\mathcal{C}_{b}$, and $\Theta$ are the intersection of zero-superlevel sets of multiple functions. In this case, $\overline{K}$ includes a constraint for each function, which increases complexity of the QP. An alternative approach is to use the log-sum-exponential soft minimum to compose multiple barrier functions into a single one. Specifically, let $\rho > 0$, and consider $\text{softmin}_{\rho}:{{\mathbb{R}}^{n_{sm}}\rightarrow{\mathbb{R}}}$ defined by

The soft minimum provides a continuously differentiable lower bound on the minimum (e.g., ), that is, ${\text{softmin}_{\rho}{(z_{1},\ldots,z_{n_{sm}})}} \leq {\min{\{ z_{1},\ldots,z_{n_{sm}}\}}}$.

To illustrate a soft minimum of $h_{s}$, consider $n_{s}$ continuously differentiable barrier functions ${b_{1},\ldots,b_{n_{s}}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$. The set where all constraints are satisfied is

which is the intersection of the zero-superlevel sets of $b_{1},\ldots,b_{n_{s}}$. Then, consider the safe set $\mathcal{C}_{s}$, where

and it follows from that $\mathcal{C}_{s} \subseteq \mathcal{S}_{s}$, and $\mathcal{C}_{s}\rightarrow\mathcal{S}_{s}$ as $\rho_{s}\rightarrow\infty$. Furthermore, the worst case conservativeness of the soft-minimum approximation of the minimum is ${({\ln n_{s}})}/\rho_{s}$. Thus, $\rho_{s}$ can be selected to limit conservativeness based on $n_{s}$. If $\rho_{s}$ is small, then the soft minimum is a conservative approximation of the minimum. However, if $\rho_{s}$ is large, then the magnitude of $h_{s}^{\prime}$ is large at points where the minimum is not differentiable. Thus, selecting $\rho_{s}$ is a trade-off between the conservativeness of $\mathcal{C}_{s}$ and the magnitude of $h_{s}^{\prime}$. A similar approach can be used to construct $h_{b}$.

The soft minimum can also be used to construct $k$. Since $\mathcal{U}$ is a convex polytope, it can be expressed as

where ${a_{1},\ldots,a_{r}} \in {\mathbb{R}}^{m}$ and ${d_{1},\ldots,d_{r}} \in {\mathbb{R}}$. Let the control plan $u_{p}$ be given , which implies that for each $\tau \in {\lbrack 0,T\rbrack}$, $u_{p}{(\tau;\theta)}$ is a convex combination of $\theta_{1},\ldots,\theta_{p}$. Hence, if ${(\theta_{1},\ldots,\theta_{p})} \in \mathcal{U}^{p}$, then for all $\tau \in {\lbrack 0,T\rbrack}$, ${u_{p}{(\tau;\theta)}} \in \mathcal{U}$. Thus, the admissible parameter set $\Theta$ can be constructed with

where $\rho_{k} > 0$. Similar to above, it follows from that $\Theta \subseteq \mathcal{U}^{p}$, and $\Theta\rightarrow\mathcal{U}^{p}$ as $\rho_{k}\rightarrow\infty$.

## Application to a Ground Robot

Figure 3: Closed-loop trajectories for FlowBarrier, NMPC, CiLQR-CBF, and CiLQR-BCBF across 100 navigation trials in a dense obstacle environment. Trajectories are color-coded by task outcome: reached (green), stuck (purple), and failed (red). The highlighted black trajectory in FlowBarrier corresponds to the navigation task from initial state x0 = [−8 − 8 0 0]⊤ to goal state xd = ⊤.

Consider the nonholonomic ground robot modeled , where

and $q \triangleq {\lbrack q_{x}\quad q_{y}\rbrack}^{\top}$ is the robot's position in an orthogonal coordinate system, $v$ is the speed, and $\vartheta$ is the direction of the velocity vector (i.e., the angle from ${\lbrack\, 1\quad 0\rbrack}^{\top}$ to ${\lbrack{\overset{˙}{q}}_{x}\quad{\overset{˙}{q}}_{y}\rbrack}^{\top}$). Let ${\overline{u}}_{1} = 2$, ${\overline{u}}_{2} = 1$, and

Since $\mathcal{U}$ is a convex polytope, the admissible parameter set $\Theta$ is constructed using (7.2) with $\rho_{k} = 50$. Let $\Omega = {\mathbb{R}}^{d}$, which is convex and satisfies $0 \in \Omega$. Let $\mathcal{Z} = {({- \infty},1\rbrack}$, which is a convex polytope in $\mathbb{R}$ and satisfies $1 \in \mathcal{Z}$. The upper bound $z \leq 1$ ensures that $\overset{˙}{\gamma} = z \leq 1$, so the planning-time shift $\gamma$ does not advance faster than real time.

Consider the map shown in Figure 3, which has $46$ circles and a wall. For $i \in {\{ 1,\ldots,46\}}$, the area outside the $i$th obstacle is modeled as the zero-superlevel set of

where $c_{i} \in {\mathbb{R}}^{2}$ and $r_{i} > 0$ are the center and radius of the $i$th circle. Similarly, the area inside the wall is modeled as the zero-superlevel set of

where $a > 0$ specifies the half-width of the square wall. The bounds on speed $v$ are modeled as the zero-superlevel sets of

The safe set $\mathcal{C}_{s}$ is given by and with $n_{s} = 49$ and $\rho_{s} = 20$. The safe set $\mathcal{C}_{s}$ projected into the $q_{x}$-$q_{y}$ plane is shown in Figure 3. Note that $\mathcal{C}_{s}$ is also bounded in speed $v$, specifically, for all $x \in \mathcal{C}_{s}$, $v \in {\lbrack{- 2},2\rbrack}$.

The backup safe set $\mathcal{C}_{b}$ is given , where

To verify Assumption 1, consider the control ${{\overset{\sim}{u}}_{b}{(x)}} \triangleq {\lbrack{- {{\overline{u}}_{1}{{sgn}{(v)}}\;\;0}}\rbrack}^{\top}$, which applies maximum deceleration. It can be shown by direct computation that ${{L_{f}h_{b}{(x)}} + {L_{g}h_{b}{(x)}{\overset{\sim}{u}}_{b}{(x)}}} \geq 0$ for all $x \in \mathcal{C}_{b}$. Thus, ${{\overset{\sim}{u}}_{b}{(x)}} \in {K_{b}{(x)}}$ for any extended class-$\mathcal{K}$ function $\alpha_{b}$, which implies that Assumption 1 is satisfied.

The control objective is for the robot to move from its initial state to a desired state $x_{d} \triangleq \begin{bmatrix}
\end{bmatrix}^{\top} \in {\mathbb{R}}^{4}$ without violating safety (i.e., hitting an obstacle or violating speed bounds). To accomplish this objective, consider the cost function given , where

Minimizing the cost function drives the state toward the desired state $x_{d}$. The quadratic program includes the cost gradient as a linear term in the objective, which encourages ${\overline{u}}_{p \ast}$ to reduce the cost along the predicted trajectory. Thus, minimizing the quadratic program objective drives the state toward the minimizer of $\overline{J}$ while satisfying the safety constraints. This approach eliminates the need for an explicit reference control, unlike standard CBF methods where a desired control input must be specified.

We implement Algorithm 1 with ${\alpha_{m}{({\overline{\psi}}_{m})}} = {10{\overline{\psi}}_{m}}$, ${\alpha_{b}{({\overline{\psi}}_{t})}} = {\overline{\psi}}_{t}$, ${\alpha_{\theta}{(k)}} = {10k}$, ${\alpha_{\gamma}{(\gamma)}} = {0.1\gamma}$, $T = {4s}$, $T_{d} = {0.05s}$, $p = 80$, $Q_{u} = {10^{6}I_{m}}$, $Q_{\omega} = {30I_{d}}$, $Q_{z} = 10^{- 6}$, $\lambda = 1000$, $N = 80$, ${\deltat} = {0.005s}$, and $u_{p}$ given by with $\beta_{i}$ from Example 1.

Figure 4: Time histories of robot states (qx,qy,v,ϑ), control inputs (u1,u2), and barrier functions ${\overline{\psi}}_{m}$, ${\overline{\psi}}_{t}$, and k for x0 = [−8 − 8 0 0]⊤ and xd = ⊤.

Figure 5: Time histories of control parameters θ, parameter rate ω, planning-time shift γ, and planning-time shift rate z for x0 = [−8 − 8 0 0]⊤ and xd = ⊤.

Figure 3 highlights in black a closed-loop trajectory of FlowBarrier on a navigation task from ${\overline{x}}_{0} = {\lbrack{{- 8} - {8\;0\;0\;0_{d}\;0}}\rbrack}^{\top}$ to goal state $x_{d} = {\lbrack\, 8\;8\;0\;0\rbrack}^{\top}$. Figure 4 shows time histories of the robot states $(q_{x},q_{y},v,\vartheta)$, control inputs $(u_{1},u_{2})$, and barrier functions ${\overline{\psi}}_{m}$, ${\overline{\psi}}_{t}$, and $k$. The barrier functions remain nonnegative throughout the trajectory, confirming that $\overline{x} \in \overline{\Psi}$ for all $t \geq 0$. Figure 5 shows the evolution of control parameters $\theta$, parameter rate $\omega$, planning-time shift $\gamma$, and planning-time shift rate $z$ during safe navigation through the obstacle field.

For comparison, we present simulation results with alternative control approaches. Specifically, we compare the proposed FlowBarrier method with nonlinear model predictive control (NMPC), and a constrained iterative linear quadratic regulator (CiLQR) paired with two different safety filters: a control barrier function filter (CiLQR-CBF) and a backup control barrier function filter (CiLQR-BCBF).

The NMPC approach solves a finite-horizon optimal control problem that minimizes the cost functional, where $R$ and $W$ are given , subject to the state constraint ${h_{s}{(x)}} \geq 0$ along the prediction horizon, the terminal constraint ${h_{b}{({x{(T)}})}} \geq 0$, and the input constraints $u \in \mathcal{U}$. The prediction horizon $T$ and discretization time step $T_{d}$ are set equal to those used in the FlowBarrier method. Since the terminal constraint enforces that the predicted terminal state lies within the forward invariant backup safe set $\mathcal{C}_{b}$, recursive feasibility of the NMPC is guaranteed.

The CiLQR-CBF approach consists of two stages. First, a constrained iterative linear quadratic regulator is employed to compute a nominal control trajectory that minimizes the cost functional with $R$ and $W$ given , where the state constraint ${h_{s}{(x)}} \geq 0$ and the input constraints $u \in \mathcal{U}$ are enforced via an augmented Lagrangian method. The prediction horizon $T$ and discretization time step $T_{d}$ are set equal to those used in the FlowBarrier method. The resulting nominal control serves as the desired control input for a CBF safety filter, which solves a quadratic program that minimally modifies the desired control to enforce safety and input constraints (see for details).

The CiLQR-BCBF approach employs the same constrained iterative linear quadratic regulator to generate the desired control. However, instead of the standard CBF, a backup control barrier function (BCBF) method is used as the safety filter.

The BCBF uses a backup controller that drives the robot to rest and solves a quadratic program that minimally modifies the desired control while ensuring the predicted trajectory under the backup controller remains in the safe set along the prediction horizon and satisfies a terminal safety condition, subject to input constraints $u \in \mathcal{U}$ (see for details).

All simulations are performed in Python on a laptop computer with an Intel Core i9-14900HX CPU and 32 GB of RAM. All methods are implemented using the CBFJAX framework, which is built on JAX and provides automatic differentiation and just-in-time compilation. Within the CBFJAX framework, the NMPC problem is solved using do-mpc with IPOPT, and the CiLQR problem is solved using trajax. All numerical ODE integration and adjoint computations are performed using Diffrax, and quadratic programming problems are solved using JaxOpt with OSQP.

To compare methods across diverse conditions, we conduct $100$ navigation tasks constructed from a grid of initial and goal configurations. Specifically, $10$ initial states are uniformly sampled along the line from $x_{0} = {\lbrack{{- 8} - 8\;0\;0}\rbrack}^{\top}$ to ${\lbrack{\, 8 - {8\;0\pi}}\rbrack}^{\top}$, and $10$ goal states are uniformly sampled along the line from $x_{d} = {\lbrack{- 8\;8\;0\;0}\rbrack}^{\top}$ to ${\lbrack\, 8\;8\;0\;0\rbrack}^{\top}$, yielding $100$ distinct navigation tasks by pairing each initial state with each goal state. Each simulation is run for $20s$. For fair comparison, all methods employ the same running cost $R$ and terminal cost $W$ given , the same prediction horizon $T = {4s}$ and discretization time step $T_{d} = {0.05s}$, with the control trajectory initialized to zero. Parameters shared across all methods are set to identical values, while method-specific parameters are individually selected to achieve best performance for each approach.

Trajectories are categorized as *reached* if they successfully arrive at the goal with ${\|{x - x_{d}}\|} \leq 0.5$ within $20s$, *stuck* if they fail to make progress, or *failed* if they violate safety constraints. Figure 3 shows the resulting trajectories for all methods. FlowBarrier achieves $88$ reached, $12$ stuck, and $0$ failed. NMPC achieves competitive performance with $85$ reached, $15$ stuck, and $0$ failed. CiLQR-CBF and CiLQR-BCBF demonstrate lower success rates, achieving $37$ reached, $55$ stuck, and $8$ failed, and $44$ reached, $55$ stuck, and $0$ failed, respectively.

Figure 6 presents detailed statistical comparisons of time to goal $\text{TTG} \triangleq {\min{\{{\hat{t}:{{{\text{for all~}t} \geq \hat{t}},{{\|{{x{(t)}} - x_{d}}\|} \leq 0.5}}}\}}}$, cumulative cost $J_{\text{cum}} \triangleq {\int_{0}^{20}{R{({x{(t)}})}{dt}}}$, computation time, minimum barrier over time ${\min_{t \in {\lbrack 0,20\rbrack}}h_{s}}{({x{(t)}})}$, minimum barrier over prediction horizon ${\min_{{t \in {\lbrack 0,20\rbrack}},{\tau \in {\lbrack 0,T\rbrack}}}h_{s}}{({\varphi{(\tau;{\overline{x}{(t)}})}})}$, and prediction violations. FlowBarrier achieves competitive time to goal and cumulative cost while maintaining the lowest computation time among all methods. The minimum barrier over time remains nonnegative for FlowBarrier, NMPC, and CiLQR-BCBF across all trials, while CiLQR-CBF exhibits $8$ safety violations due to infeasibility of the CBF quadratic program. Most critically, FlowBarrier is the only method with zero prediction violations across all $100$ trials, demonstrating formal safety guarantees not only on the executed trajectory but also on the planned trajectory.

Figure 6: Statistical comparison of performance metrics across 100 navigation trials for FlowBarrier, NMPC, CiLQR-CBF, and CiLQR-BCBF. Metrics include time to goal, cumulative cost, computation time, minimum barrier over time mint ∈ hs (x (t)), minimum barrier over prediction horizon ${\min_{{t \in {\lbrack 0,20\rbrack}},{\tau \in {\lbrack 0,T\rbrack}}}h_{s}}{({\varphi{(\tau;{\overline{x}{(t)}})}})}$, and prediction violations.
