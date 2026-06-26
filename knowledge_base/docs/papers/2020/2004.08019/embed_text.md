## Introduction

Model-based learning control, which encompasses classical system identification (e.g. ) and adaptive control (e.g. ) as well as branches of modern reinforcement learning (e.g. ), universally uses a stochastic data model, where a model is estimated from data corrupted by random noise. A salient perennial issue in these methods is ensuring stability despite the presence of concomitant model errors; this is the problem of *robustness*.

Traditional methods for designing robust controllers include $\mathcal{H}_{\infty}$ control design, which treats modeling error as a worst-case or adversarial disturbance, robust optimization over parametric state-space uncertainty sets, which typically involve searching for shared Lyapunov functions via convex semidefinite programming, and certainty-equivalent control, which utilizes only a nominal model and ignores modeling error entirely. However, since the robust design methods work with uncertainty sets, it is generally not straightforward to relate the uncertainty set descriptions to actual uncertainties arising from a stochastic data model.

Alternatively, in this paper we explore the connection between a special type of *stochastic stability* and *robust stability* and exploit this connection for robust control design. In particular, we use a *multiplicative noise* model where the noise is viewed as a representation of uncertainty in the nominal system model. This framework is naturally disposed toward trading off performance and robustness according to uncertainty directions and magnitudes which can be estimated from trajectory data during model-based learning control. The study of multiplicative noise models has a long history in control theory. In contrast with the well-known additive noise setting, multiplicative noise captures linear dependence of the noise on the state and control input, which occurs intrinsically in a diverse array of modern control systems such as robotics, networked systems with noisy communication channels, modern power networks with high penetration of intermittent renewables, turbulent fluid flow. Linear systems with multiplicative noise are particularly attractive as a stochastic modeling framework because they remain simple enough to admit closed-form expressions for stability and optimal control via generalized Lyapunov and Riccati equations. A multiplicative noise model also holds a distinct advantage of being sensitive to *structured* uncertainties in *specific directions directly related to data*, as opposed to generic sets governed by norm balls as .

In this paper we consider a fundamental question:\*What is the set of perturbations to the system matrix where the perturbed system can be guaranteed stable, given knowledge only of the nominal system dynamics and stochastic stability of a system with multiplicative noise?* This question was considered by for the continuous-time setting. Surprisingly, it was noted that the addition of multiplicative noise could actually *stabilize* a deterministically unstable system when interpreted in the sense of Stratonovich (rather than Itô). Despite this subtle difficulty, combining mean-square stability of a multiplicative noise system with a *right-shift* of the system dynamics, i.e., increasing the real parts of the eigenvalues of $A$ as $A\leftarrow{A + {cI}}$ was shown sufficient to ensure robust deterministic stability. Similarly, we develop conditions for discrete-time systems which combine mean-square stability of a multiplicative noise system with a *scaling* of the system dynamics, i.e., increasing the absolute value of eigenvalues of $A$ as $A\leftarrow{cA}$.

In this paper we make the following contributions: We develop a result utilizing shared Lyapunov functions that establishes robust stability of a set of deterministic systems given stochastic (mean-square) stability of another system with multiplicative noise (Theorem 3.2).

We develop a complementary result utilizing an auxiliary system with scaled dynamics matrices that similarly establishes robust stability of a set of deterministic systems given stochastic (mean-square) stability of another system with multiplicative noise (Theorem 4.1).

We show that both theorems yield robustness sets whose size increases monotonically with the multiplicative noise variances and collapse to zero in the case of zero noise.

We develop a corresponding pair of algorithms which efficiently compute controllers that simultaneously maximize robustness and minimize a quadratic cost.

We elaborate on the robust stability problem in Section 2, develop theorems in Sections 3 and 4, develop corresponding algorithms in Section 5, give numerical examples in Section 6, and conclude in Section 7.

## Problem formulation

Consider a discrete-time linear time-invariant (LTI) system where the entries of ${bar}A$ and ${bar}B$ are unknown constants and are approximated (perhaps from noisy trajectory data) by the known nominal matrices $A$ and $B$ leading to the nominal model where $x_{t} \in {\mathbb{R}}^{n}$ is the system state, $u_{t} \in {\mathbb{R}}^{m}$ is the control input, $A \in {\mathbb{R}}^{n \times n}$ is the dynamics matrix and $B \in {\mathbb{R}}^{n \times m}$ is the input matrix. In order to stabilize the system, we use linear state feedback $u_{t} = {Kx_{t}}$ with gain matrix $K \in {\mathbb{R}}^{m \times n}$; classical results show that if the pair $(A,B)$ is controllable, then the closed-loop eigenvalues of $A + {BK}$ can be placed arbitrarily by choosing suitable gains. A robust stabilization problem is to find a linear state-feedback control $u_{t} = {Kx_{t}}$ such that the closed-loop nominal system remains stable under fixed perturbations of $A$ and $B$ i.e. that is stable for some set of perturbations ${\DeltaA} \in \mathcal{A}$ and ${\DeltaB} \in \mathcal{B}$, ideally containing the true matrices ${bar}A$ and ${bar}B$.

As a parallel development, consider an LTI system with multiplicative noise with dynamics Multiplicative noise terms are modeled by the i.i.d. across time (white), zero-mean, mutually independent scalar random variables $\gamma_{ti}$ and $\delta_{tj}$, which have variances $\alpha_{i}$ and $\beta_{j}$, respectively. The matrices $A_{i} \in {\mathbb{R}}^{n \times n}$ and $B_{i} \in {\mathbb{R}}^{n \times m}$ specify how each scalar noise term affects the dynamics and input matrices.

Stability of such a system depends on the behavior of the second moments (covariance) of the state over time as formalized by the notion of *mean-square stability*, a form of robust stability which is stricter than stabilizability of the nominal system $(A,B)$ and limits the size of the multiplicative noise variances:

### Definition 2.1 (Mean-square stability)

The system in is mean-square stable if and only if In order to stabilize the system, we again use linear state feedback $u_{t} = {Kx_{t}}$; mean-square stability of the closed-loop system with this control is equivalently characterized by the solution of a *generalized Lyapunov equation* (GLE):

### Lemma 2.2

The system in is mean-square stable in closed-loop with state feedback $u_{t} = {Kx_{t}}$ if and only if for any $Q \succ 0$ there exists $P \succ 0$ satisfying

### Corollary 2.3

In the discrete-time setting, mean-square stability of with control $u_{t} = {Kx_{t}}$ implies deterministic stability of with the same control $u_{t} = {Kx_{t}}$.

### Proof

From, strict mean-square stability implies existence of $P \succ 0$ such that which ensures stability of $A + {BK}$. ∎ One mean-square stabilizing control arises by solving the infinite-horizon multiplicative noise LQR problem where $Q \succeq 0$ and $R \succ 0$. We assume that the problem data $A$, $B$, $\alpha_{i}$, $A_{i}$, $\beta_{j}$, and $B_{j}$ permit the existence of a finite solution, in which case the system is called *mean-square stabilizable*. Dynamic programming can be used to show that the optimal policy is linear state feedback $u_{t} = {K^{\ast}x_{t}}$, where $K^{\ast} \in {\mathbb{R}}^{m \times n}$ denotes the optimal gain matrix, and the resulting optimal cost $V{(x_{0})}$ for a fixed initial state $x_{0}$ is quadratic, i.e., ${V{(x_{0})}} = {x_{0}^{\intercal}Px_{0}}$, where $P \in {\mathbb{R}}^{n \times n}$ is a symmetric positive definite matrix. The optimal cost is given by the solution of the *generalized algebraic Riccati equation* (GARE) which can be derived similarly to the GARE given by for continuous-time systems. The solution $P = {{gare}{(A,B,Q,R,\alpha_{i},\beta_{j},A_{i},B_{j})}}$ can be obtained via the value iteration recursion with $P_{0} = Q$ or via semidefinite programming formulations. The optimal gain is then

### Generalized eigenvalues and semidefiniteness

The following lemmas regarding generalized eigenvalue problems and semidefiniteness will be needed later:

### Lemma 2.4

If $\lambda_{\max}$ is the maximum generalized eigenvalue which solves ${Av} = {\lambdaBv}$, then ${\lambda_{\max}B} \succeq A$.

### Corollary 2.5

If $B$ is singular, then $\lambda_{\max}$ becomes infinite.

We omit the proofs since these results are widely known; they follow readily from the method of Lagrange multipliers and Rayleigh quotients.

Every symmetric matrix $S$ can be split into positive and negative semidefinite parts via eigendecomposition as where $\lambda_{i}$ and $\lambda_{j}$ are positive and negative eigenvalues respectively with associated eigenvectors $v_{i}$ and $v_{j}$.

## Robustness via shared Lyapunov functions

We begin by ignoring the contribution of feedback control; we will introduce the control again in Sec. 5. We also restrict our search over $\DeltaA$ to the set The $\theta_{i}$ are scalars that represent the relative amount of uncertainty in each direction, while $y$ is a scalar governing the maximum magnitude of the perturbations. The $\theta_{i}$ and $y$ can be estimated from statistics of sampled trajectory data, e.g., using bootstrap resampling methods. This approach is intuitive; mean-square stability under stochastic instantaneous perturbations in specific directions $A_{i}$ ought to ensure deterministic stability under constant shifts of the dynamics in those same directions. Note the number of linearly independent uncertainty directions $p$ is limited by the number of entries of $A$ i.e. $p \leq n^{2}$. Consider the problem of finding the largest deviation scalar $y^{\ast}$ which can be tolerated while still guaranteeing stability of the perturbed deterministic system based on mean-square stability of the stochastic system with ${{\mathbb{E}}{\lbrack\gamma_{ti}\rbrack}} = 0$, ${{\mathbb{E}}{\lbrack\gamma_{ti}^{2}\rbrack}} = \alpha_{i} > 0$.

### Scalar case

First, we treat the scalar case where $n = p = 1$ so $A_{1} = 1$ and $\theta_{1} = 1$ without loss of generality.

### Lemma 3.1

is mean-square stable where $A$, $x_{t}$, $\gamma_{t}$ are scalars with ${{\mathbb{E}}{\lbrack\gamma_{t}^{2}\rbrack}} = \alpha > 0$. Then, the perturbed deterministic system is stable for any fixed perturbation ${|y|} \leq {\sqrt{A^{2} + \alpha} - {|A|}}$.

### Proof

The GLE in reduces to where $P$, $Q$ are scalars with solution which is positive only when $\sqrt{A^{2} + \alpha} < 1$. By assumption the system is mean-square stable, so Lemma 2.2 implies that the solution $P > 0$ and thus indeed $\sqrt{A^{2} + \alpha} < 1$. By the restriction on $y$ and the triangle inequality This simple example demonstrates that the robustness margin increases monotonically with the multiplicative noise variance and when $\alpha = 0$, i.e. ${|a|}\rightarrow 1$, the bound collapses and no robustness is guaranteed.

### Multivariate case

The optimal bound $y^{\ast}$ is found by solving the program i.e. maximizing $y$ while ensuring that there exists a $P$ which generates a Lyapunov function which guarantees both mean-square stability of the stochastic system and deterministic stability of the perturbed deterministic system. Here we have arbitrarily chosen $Q = I$ e.g. as in without loss of generality since the constraints pertain only to stability, which is invariant to the choice of $Q$. Since the program is quasiconvex in $y$, it can be solved by bisection over $y$ and solving a feasibility SDP for each fixed $y$, with the solution being the largest $y$ which admits a feasible solution to the SDP.

The set of constraints in the second line of form corners of a convex box polytope in the space of $n \times n$ matrices, which is necessary and sufficient to guarantee stability of. Thus, from the perspective of verifying stability of $A + {\DeltaA}$ this procedure no better than simply solving the same program with the first constraint deleted, which has a larger feasible set and thus will achieve at least as good a bound as. However, the solution of defines a hard upper limit on the following bounds we develop in this section which are based on a shared Lyapunov function, since gives the optimal bound. The bounds we develop in this section trade optimality (conservativeness) for the assurance that $P$ guarantees stability of the perturbed deterministic system without explicitly using the Lyapunov inequality $P \succeq {{({A + {\DeltaA}})}^{\intercal}P{({A + {\DeltaA}})}}$.

Giving up optimization over $P$ and instead choosing $Q$ arbitrarily (later in Sec. 5, $Q$ will be chosen as the cost matrix of an LQR control design) and calculating the associated $P$, we obtain the following result:

### Theorem 3.2

is mean-square stable with ${{\mathbb{E}}{\lbrack\gamma_{ti}\rbrack}} = 0$, ${{\mathbb{E}}{\lbrack\gamma_{ti}^{2}\rbrack}} = \alpha_{i} > 0$.\Fix a $Q \succeq I$ and the solution $P \succ 0$ to Let $\eta_{i} > 0$ be scalars which satisfy Then the deterministic system is deterministically stable for any

### Proof

It is evident that valid $\eta_{i} > 0$ exist since ${pQ} + {\sum_{i = 1}^{p}{\alpha_{i}A_{i}^{\intercal}PA_{i}}}$ is strictly positive definite. Rearranging to ${{pQ} + {\sum_{i = 1}^{p}{\alpha_{i}A_{i}^{\intercal}PA_{i}}}} = {P - {A^{\intercal}PA}}$ and substituting gives which proves stability of. ∎

### Remark 3.3

The unidirectional bound in of Thm. 3.2 can be made bidirectional by replacing with yielding the bidirectional bound ${|\mu_{i}|} < \eta_{i}$.

### Remark 3.4

Let $\theta_{i} \geq 0$ be scalars such that ${\sum_{i = 1}^{p}\theta_{i}} = 1$; these denote relative uncertainty in directions $A_{i}$. The largest robust stability bounds with respect to this choice of $\theta_{i}$ are obtained by setting $\eta_{i} = {y\theta_{i}}$ and maximizing the scalar $y$, which can be accomplished via bisection. As discussed earlier, optimizing a bidirectional bound over $P$, $Q$, and $y$ is equivalent to solving the full program .

For $p = 1$, the Theorem 3.2 reduces as follows:

### Corollary 3.5

is mean-square stable with ${{\mathbb{E}}{\lbrack\gamma_{t1}\rbrack}} = 0$, ${{\mathbb{E}}{\lbrack\gamma_{t1}^{2}\rbrack}} = \alpha_{1} > 0$.\Fix a $Q \succeq I$ and the solution $P \succ 0$ to Let $\zeta_{1} > 0$ be a scalar which satisfies Then the deterministic system is deterministically stable for any where $\eta_{1} > 0$ is a scalar uniquely determined by $\zeta_{1}$ as Also, $\eta_{1}$ satisfies in accordance with Thm. 3.2.

### Proof

Multiplying both sides of by $\eta_{1}$ and using\$\eta_{1} = {\sqrt{\zeta_{1}^{2} + \alpha_{1}} - \zeta_{1}}$ gives Rearranging $\eta_{1} = {\sqrt{\zeta_{1}^{2} + \alpha_{1}} - \zeta_{1}}$ gives $\alpha_{1} = {\eta_{1}^{2} + {2\eta_{1}\zeta_{1}}}$. Adding $2\eta_{1}^{2}A_{1}^{\intercal}PA_{1}$ to both sides of and substituting $\alpha_{1} = {\eta_{1}^{2} + {2\eta_{1}\zeta_{1}}}$ gives exactly. Thus the condition of Thm. 3.2 is satisfied by $\eta_{1} = {\sqrt{\zeta_{1}^{2} + \alpha_{1}} - \zeta_{1}}$. Applying Thm. 3.2 completes the proof. ∎ If all robustness bounds $\eta_{i}$ in Theorem 3.2 are chosen proportional to $\sqrt{\zeta_{i}^{2} + \alpha_{i}} - \zeta_{i}$ (like in Cor. 3.5), we obtain the following corollary:

### Corollary 3.6

Suppose the system in is mean-square stable with ${{\mathbb{E}}{\lbrack\gamma_{ti}\rbrack}} = 0$, ${{\mathbb{E}}{\lbrack\gamma_{ti}^{2}\rbrack}} = \alpha_{i} > 0$. Fix a $Q \succeq I$ and the solution $P \succ 0$ to. Let $\eta_{i} > 0$ be scalars which satisfy and are chosen proportional to $\sqrt{\zeta_{i}^{2} + \alpha_{i}} - \zeta_{i}$ where $\zeta_{i}$ are scalars which marginally satisfy Then the deterministic system in is stable for any $0 \leq \mu_{i} < \eta_{i}$ where the $\eta_{i}$ are upper bounded by

### Proof

The proof proceeds by contradiction. Suppose From and using an argument identical to Corollary 3.5 we have Summing over all the noises, Substituting $\alpha_{i} = {\eta_{i}^{2} + {2\eta_{i}\zeta_{i}}}$, the matrix inequality in reduces to which is a contradiction; we need the additional terms on the right-hand side of in order to match in Theorem 3.2, which shows that the bounds $\eta_{i}$ must be less than $\sqrt{\zeta_{i}^{2} + \alpha_{i}} - \zeta_{i}$. ∎ Corollaries 3.5 and 3.6 go towards showing the functional dependence of upper bounds of the robustness margins on the multiplicative noise variance, namely a $\sqrt{\alpha_{i}}$ relation. Significantly, the robustness margins collapse to nothing when the variances are all zero and increase monotonically with increasing noise variances.

### Conservative simplifications

It can be shown that $\frac{1}{\sqrt{\zeta_{i}^{2} + \alpha_{i}} - \zeta_{i}}$ is convex in $\zeta_{i}$, so any linearization (first-order Taylor series expansion) will be a global underestimator of this function. Thus a conservative solution can be found by linearization, yielding a convex semidefinite constraint which can be expressed as a generalized eigenvalue problem which can be solved efficiently. For example, linearizing $\frac{1}{\sqrt{\zeta_{i}^{2} + \alpha_{i}} - \zeta_{i}}$ about $\zeta_{i} = 0$ yields $\frac{1}{\sqrt{\alpha_{i}}} + {\frac{1}{\alpha_{i}}\zeta_{i}}$. This is worked out in the following lemma:

### Lemma 3.7

Define $A$, $A_{i}$, $\alpha_{i}$, $P$, $Q$ as in Cor. 3.6. Let $\lambda_{i}$ be the maximum generalized eigenvalue which solves Then $\zeta_{i} \geq \lambda_{i}$ satisfies.

### Proof

By Lemma 2.4 we have the semidefinite bound Since $\frac{1}{\sqrt{\lambda_{i}^{2} + \alpha_{i}} - \lambda_{i}}$ is a convex function of $\lambda_{i}$, which is exactly the constraint in with $\zeta_{i} = \lambda_{i}$. Noting that $\frac{1}{\sqrt{\zeta_{i}^{2} + \alpha_{i}} - \zeta_{i}}$ is nondecreasing in $\zeta_{i}$ completes the proof. ∎ Similarly, an even more conservative bound is obtained by neglecting the contribution of $2\zeta_{i}A_{i}^{\intercal}PA_{i}$, again resulting in a generalized eigenvalue problem.

### Lemma 3.8

Define $A$, $A_{i}$, $\alpha_{i}$, $P$, $Q$ as in Cor. 3.6. Let $\lambda_{i}$ be the maximum generalized eigenvalue which solves Then $\zeta_{i} \geq {\frac{1}{2}\left({{\alpha\lambda_{i}} - \frac{1}{\lambda_{i}}} \right)}$ satisfies.

### Proof

By Lemma 2.4 we have the semidefinite bound and rearranging yields Adding ${2\zeta_{i}A_{i}^{\intercal}PA_{i}} \succeq 0$ to the left side gives exactly the constraint. ∎

## Robustness via stability of auxiliary systems

Now, instead of requiring the same Lyapunov function to ensure mean-square stability of a stochastic system and stability of a perturbed deterministic system with the same nominal $A$, we construct auxiliary stochastic systems whose mean-square stability implies deterministic stability of the "target" perturbed deterministic system. Such an approach can be fundamentally more flexible than using a shared Lyapunov function since the open-loop dynamics of the auxiliary system are permitted to be significantly less stable.

### Theorem 4.1

Suppose the stochastic system with ${{\mathbb{E}}{\lbrack\gamma_{ti}^{2}\rbrack}} = \alpha_{i} \geq {\eta_{i}\left({1 + {\sum_{j = 1}^{p}\eta_{j}}} \right)}$, $\eta_{i} \geq 0$ is mean-square stable. Then the deterministic system is stable for all ${|\mu_{i}|} < \eta_{i}$.

### Proof

Mean-square stability implies $\exists P$ such that By symmetry of the terms ${\sum_{i = 1}^{p}{\eta_{i}A^{\intercal}PA}} + {\sum_{i = 1}^{p}{\eta_{i}A_{i}^{\intercal}PA_{i}}}$, the same argument can be applied for each sign combination of $\eta_{i}$ i.e. ${\pm \eta_{1}},{\pm \eta_{2}},\ldots,{\pm \eta_{p}}$ from onward, which together prove stability of $A + {\sum_{i = 1}^{p}{k_{i}\eta_{i}A_{i}}}$ for any $k_{i} \in {\{{- 1},{+ 1}\}}$ with the same Lyapunov matrix $P$. By an argument from Schur complements (see e.g.), this is necessary and sufficient for any convex combination of $A + {\sum_{i = 1}^{p}{k_{i}\eta_{i}A_{i}}}$ to be also stable using $P$, completing the proof. ∎

### Remark 4.2

The condition ${{\mathbb{E}}{\lbrack\gamma_{ti}^{2}\rbrack}} = \alpha_{i} \geq {\eta_{i}\left({1 + {\sum_{j = 1}^{p}\eta_{j}}} \right)}$ places an upper bound on the robustness margins $\eta_{i}$ which is related to the multiplicative noise variances $\alpha_{i}$. In the case of $p = 1$, this reduces to ${\eta_{1} < {\frac{1}{2}\left({\sqrt{1 + {4\alpha_{1}}} - 1} \right)}}.$ At first glance the condition of Thm. 3.2 may seem overly restrictive since it requires mean-square stability with a *scaled* $A$ matrix; indeed such a procedure is somewhat limiting in the open-loop setting since this can make the plant unstable. However, in the control design setting this *essentially does not matter* since the gain can be made larger to compensate, and because a simple scaling of $A$ does not affect controllability of the pair $(A,B)$; to see this, simply note that the rank of the controllability matrix $\begin{bmatrix} \end{bmatrix}$ is unaffected by a nonzero scaling of $A$. The work of similarly leverages this fact.

## Input uncertainties and robust control design algorithms

In the case where there are uncertainties in the input matrix $B$ under closed-loop state feedback, Theorems 3.2 and 4.1 are easily modified by simply substituting yielding a set of $p + q$ robustness bounds ${\{\eta_{i}'\}} = {{\{\eta_{i}\}} \cup {\{\psi_{j}\}}}$ which ensure stability of where $0 \leq \mu_{i} < \eta_{i}$, $0 \leq \nu_{j} < \psi_{j}$ (bounds in negative directions also assured for Thm. 4.1). These results are formulated as Algorithms 1 and 2 for generating optimal, maximally robust controllers. Note that Algorithm 1 gives unidirectional bounds while Algorithm 2 gives bidirectional bounds; it is useful to retain the unidirectional bounds of Algorithm 1 in order to realize the potentially larger robustness margins in opposing directions.

Input: Controllable nominal pair (A, B), cost matrices Q ≻ 0, R ≻ 0, uncertainty directions Ai, Bj and magnitudes θi > 0, ϕj > 0. Output: Gain matrix K and margins ηi, ψj such that is stable for all 0 ≤ μi < ηi, 0 ≤ νj < ψj. Define scalar z and scaled multiplicative noise variances αi = θi × z, and βj = ϕj × z Find the largest z* which still admits a solution to P = gare(A, B, Q, R, αi, βj, Ai, Bj) via bisection Define scalar y and scaled uncertainty magnitudes ηi = θi × y, ψj = ϕj × y Find the largest scaling y* via bisection which satisfies $Q + {K^{\intercal}RK} + {\sum\limits_{i = 1}^{p + q}{\alpha_{i}'A_{i}^{' \intercal}PA_{i}'}}$ $\succeq {\sum\limits_{i = 1}^{p + q}{\eta_{i}'\left({{A_{i}^{' \intercal}P{({A + {BK}})}} + {{({A + {BK}})}^{\intercal}PA_{i}'}} \right)^{+}}}$ $+ {\sum\limits_{i = 1}^{p + q}{\sum\limits_{j = 1}^{p + q}{\eta_{i}'\eta_{j}'\left({{A_{i}^{' \intercal}PA_{j}'} + {A_{j}^{' \intercal}PA_{i}'}} \right)^{+}}}}$ Return control law $K = {- {\left({R + {B^{\intercal}PB} + {z^{\ast}{\sum_{j = 1}^{q}{\phi_{j}B_{j}^{\intercal}PB_{j}}}}} \right)^{- 1}B^{\intercal}PA}}$ Algorithm 1 Robust control design Input: Controllable nominal pair (A, B), cost matrices Q ≻ 0, R ≻ 0, uncertainty directions Ai, Bj and magnitudes θi > 0, ϕj > 0. Output: Gain matrix K and robustness margins ηi, ψj such that is stable for all |μi| < ηi, |νj| < ψj. Define scalar y and scaled uncertainty magnitudes ηi = θi × y, ψj = ϕj × y Define scaled multiplicative noise variances $\alpha_{i} = {\eta_{i}\left({1 + {\sum_{j = 1}^{p}\eta_{j}} + {\sum_{k = 1}^{q}\psi_{k}}} \right)}$, and $\beta_{j} = {\psi_{i}\left({1 + {\sum_{i = 1}^{p}\eta_{i}} + {\sum_{k = 1}^{q}\psi_{k}}} \right)}$ Define scalar ${z{(y)}} = \sqrt{1 + {\sum_{i = 1}^{p}\eta_{i}} + {\sum_{j = 1}^{q}\psi_{i}}}$, and scaled system matrices Az = A × z, Bz = B × z Find the largest y* which still admits a solution to P = gare(Az, Bz, Q, R, αi, βj, Ai, Bj) via bisection Return control law $K = {- {\left({R + {B_{z}^{\intercal}PB_{z}} + {\sum_{j = 1}^{q}{\beta_{j}B_{j}^{\intercal}PB_{j}}}} \right)^{- 1}B_{z}^{\intercal}PA_{z}}}$ where quantities P, βj and z are evaluated at y*, and margins ηi = θi × y*, ψj = ϕj × y* Algorithm 2 Robust control design

## Numerical results

Here we consider an inverted pendulum with a torque-producing actuator whose dynamics have been linearized about the vertical equilibrium. In continuous-time the dynamics are where $m_{c}$ is a normalized mass constant. A forward Euler discretization with step size $\Deltat$ yields Uncertainty on the mass constant $m_{c}$ corresponds to uncertainty on the $$ entry of $A$. We consider an example where the true mass constant is ${{bar}m_{c}} = 10$, but the nominal model underestimates it as $m_{c} = 5$; such a situation could easily arise during the initial phase of system identification in adaptive control with noisy measurements, or in time-varying scenarios such as a robot arm picking up a heavy load. We take a step size ${\Deltat} = 0.1$. The problem data is then Applying Algorithms 1, 2, and certainty-equivalent control design, we obtained the results in Table 1. We found the sets of true ${bar}A$ matrices stabilized by the controls from Algos. 1 and 2 were ${{bar}A} \in \begin{bmatrix} \end{bmatrix}$ where ${|\mu_{1}|} < 3.970$ and ${|\mu_{1}|} < 6.997$ respectively. Stability of all systems within these sets was empirically verified by a fine grid search using 10000 samples of $\mu_{1}$ in each interval. Both robustness sets happened to include the true matrix ${bar}A$, so the robust controls were guaranteed to stabilize the true system, confirmed by ${\rho{({{{bar}A} + {{bar}BK}})}} < 1$. By contrast, the certainty-equivalent control failed to stabilize the true system. This can be understood intuitively; the pendulum had a larger mass in reality than in the nominal model, so a larger control effort was necessary to stabilize the pendulum and prevent it from falling over. Although on this particular example Algorithm 1 gave a larger (unidirectional) robustness margin, in general this not need hold; certain problem instances admit much larger robustness margins using Algorithm 2 relative to Algorithm 1. Thus, our two algorithms may be considered complementary from a control design standpoint.

Code which implements this example is available:\$\max\limits_{0\leq\mu_{1}<\eta_{1}}\rho{({A + {BK} + {\mu_{1}A_{1}}})}$ Table 1. Stability results for robust control of an inverted pendulum.

## Conclusion and Future Work

This work gives an effective methodology for certifying robustness and designing robust controllers with favorable properties and flexibility relative to competing approaches.

Direct extensions to this work include finding sharper bounds, e.g., via alternate auxiliary systems analogous to the one used in Section 4, and handling nonlinear dependence of the dynamics and/or noise on states and inputs. Future work will integrate the results of this work with adaptive model-based learning control for an end-to-end control framework which gracefully transitions from maximal robustness to maximal performance according to empirical uncertainties.
