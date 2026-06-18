<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust Control Design for Linear Systems via Multiplicative Noise

Topics include Robust control, Multiplicative noise, Linear systems, Stochastic systems, Uncertainty descriptions.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Algorithms for synthesizing robust controllers for linear systems using multiplicative noise as a design-time device. Leverages theoretical results on the equivalence of robustness to structured determinstic and stochastic uncertainties.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robust stability and stochastic stability have separately seen intense study in control theory for many decades. In this work we establish relations between these properties for discrete-time systems and employ them for robust control design. Specifically, we examine a multiplicative noise framework which models the inherent uncertainty and variation in the system dynamics which arise in model-based learning control methods such as adaptive control and reinforcement learning. We provide results which guarantee robustness margins in terms of perturbations on the nominal dynamics as well as algorithms which generate maximally robust controllers.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model-based learning control, which encompasses classical system identification (e.g. ) and adaptive control (e.g. ) as well as branches of modern reinforcement learning (e.g. ), universally uses a stochastic data model, where a model is estimated from data corrupted by random noise. A salient perennial issue in these methods is ensuring stability despite the presence of concomitant model errors; this is the problem of *robustness*.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Traditional methods for designing robust controllers include $\mathcal{H}_{\infty}$ control design, which treats modeling error as a worst-case or adversarial disturbance, robust optimization over parametric state-space uncertainty sets, which typically involve searching for shared Lyapunov functions via convex semidefinite programming, and certainty-equivalent control, which utilizes only a nominal model and ignores modeling error entirely. However, since the robust design methods work with uncertainty sets, it is generally not straightforward to relate the uncertainty set descriptions to actual uncertainties arising from a stochastic data model.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Alternatively, in this paper we explore the connection between a special type of *stochastic stability* and *robust stability* and exploit this connection for robust control design. In particular, we use a *multiplicative noise* model where the noise is viewed as a representation of uncertainty in the nominal system model. This framework is naturally disposed toward trading off performance and robustness according to uncertainty directions and magnitudes which can be estimated from trajectory data during model-based learning control. The study of multiplicative noise models has a long history in control theory. In contrast with the well-known additive noise setting, multiplicative noise captures linear dependence of the noise on the state and control input, which occurs intrinsically in a diverse array of modern control systems such as robotics, networked systems with noisy communication channels, modern power networks with high penetration of intermittent renewables, turbulent fluid flow. Linear systems with multiplicative noise are particularly attractive as a stochastic modeling framework because they remain simple enough to admit closed-form expressions for stability and optimal control via generalized Lyapunov and Riccati equations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A multiplicative noise model also holds a distinct advantage of being sensitive to *structured* uncertainties in *specific directions directly related to data*, as opposed to generic sets governed by norm balls as.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we consider a fundamental question:\
*What is the set of perturbations to the system matrix where the perturbed system can be guaranteed stable, given knowledge only of the nominal system dynamics and stochastic stability of a system with multiplicative noise?*

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

This question was considered by for the continuous-time setting. Surprisingly, it was noted that the addition of multiplicative noise could actually *stabilize* a deterministically unstable system when interpreted in the sense of Stratonovich (rather than Itô). Despite this subtle difficulty, combining mean-square stability of a multiplicative noise system with a *right-shift* of the system dynamics, i.e., increasing the real parts of the eigenvalues of $A$ as $A\leftarrow{A + {cI}}$ was shown sufficient to ensure robust deterministic stability. Similarly, we develop conditions for discrete-time systems which combine mean-square stability of a multiplicative noise system with a *scaling* of the system dynamics, i.e., increasing the absolute value of eigenvalues of $A$ as $A\leftarrow{cA}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop a result utilizing shared Lyapunov functions that establishes robust stability of a set of deterministic systems given stochastic (mean-square) stability of another system with multiplicative noise (Theorem 3.2).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop a complementary result utilizing an auxiliary system with scaled dynamics matrices that similarly establishes robust stability of a set of deterministic systems given stochastic (mean-square) stability of another system with multiplicative noise (Theorem 4.1).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that both theorems yield robustness sets whose size increases monotonically with the multiplicative noise variances and collapse to zero in the case of zero noise.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop a corresponding pair of algorithms which efficiently compute controllers that simultaneously maximize robustness and minimize a quadratic cost.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We elaborate on the robust stability problem in Section 2, develop theorems in Sections 3 and 4, develop corresponding algorithms in Section 5, give numerical examples in Section 6, and conclude in Section 7.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Consider a discrete-time linear time-invariant (LTI) system

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

where the entries of ${bar}A$ and ${bar}B$ are unknown constants and are approximated (perhaps from noisy trajectory data) by the known nominal matrices $A$ and $B$ leading to the nominal model

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

where $x_{t} \in {\mathbb{R}}^{n}$ is the system state, $u_{t} \in {\mathbb{R}}^{m}$ is the control input, $A \in {\mathbb{R}}^{n \times n}$ is the dynamics matrix and $B \in {\mathbb{R}}^{n \times m}$ is the input matrix. In order to stabilize the system, we use linear state feedback $u_{t} = {Kx_{t}}$ with gain matrix $K \in {\mathbb{R}}^{m \times n}$; classical results show that if the pair $(A,B)$ is controllable, then the closed-loop eigenvalues of $A + {BK}$ can be placed arbitrarily by choosing suitable gains.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

A robust stabilization problem is to find a linear state-feedback control $u_{t} = {Kx_{t}}$ such that the closed-loop nominal system remains stable under fixed perturbations of $A$ and $B$ i.e. that

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

is stable for some set of perturbations ${\DeltaA} \in \mathcal{A}$ and ${\DeltaB} \in \mathcal{B}$, ideally containing the true matrices ${bar}A$ and ${bar}B$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

As a parallel development, consider an LTI system with multiplicative noise with dynamics

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Multiplicative noise terms are modeled by the i.i.d. across time (white), zero-mean, mutually independent scalar random variables $\gamma_{ti}$ and $\delta_{tj}$, which have variances $\alpha_{i}$ and $\beta_{j}$, respectively. The matrices $A_{i} \in {\mathbb{R}}^{n \times n}$ and $B_{i} \in {\mathbb{R}}^{n \times m}$ specify how each scalar noise term affects the dynamics and input matrices.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Robustness via shared Lyapunov functions", "weight": 1.0} -->

We begin by ignoring the contribution of feedback control; we will introduce the control again in Sec. 5. We also restrict our search over $\DeltaA$ to the set

<!-- chunk {"id": "body-0023", "role": "body", "section": "Robustness via shared Lyapunov functions", "weight": 1.0} -->

The $\theta_{i}$ are scalars that represent the relative amount of uncertainty in each direction, while $y$ is a scalar governing the maximum magnitude of the perturbations. The $\theta_{i}$ and $y$ can be estimated from statistics of sampled trajectory data, e.g., using bootstrap resampling methods. This approach is intuitive; mean-square stability under stochastic instantaneous perturbations in specific directions $A_{i}$ ought to ensure deterministic stability under constant shifts of the dynamics in those same directions. Note the number of linearly independent uncertainty directions $p$ is limited by the number of entries of $A$ i.e. $p \leq n^{2}$. Consider the problem of finding the largest deviation scalar $y^{\ast}$ which can be tolerated while still guaranteeing stability of the perturbed deterministic system

<!-- chunk {"id": "body-0024", "role": "body", "section": "Robustness via shared Lyapunov functions", "weight": 1.0} -->

based on mean-square stability of the stochastic system

<!-- chunk {"id": "body-0025", "role": "body", "section": "Scalar case", "weight": 1.0} -->

First, we treat the scalar case where $n = p = 1$ so $A_{1} = 1$ and $\theta_{1} = 1$ without loss of generality.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Multivariate case", "weight": 1.0} -->

The optimal bound $y^{\ast}$ is found by solving the program

<!-- chunk {"id": "body-0027", "role": "body", "section": "Multivariate case", "weight": 1.0} -->

i.e. maximizing $y$ while ensuring that there exists a $P$ which generates a Lyapunov function which guarantees both mean-square stability of the stochastic system and deterministic stability of the perturbed deterministic system. Here we have arbitrarily chosen $Q = I$ e.g. as in without loss of generality since the constraints pertain only to stability, which is invariant to the choice of $Q$. Since the program is quasiconvex in $y$, it can be solved by bisection over $y$ and solving a feasibility SDP for each fixed $y$, with the solution being the largest $y$ which admits a feasible solution to the SDP.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Multivariate case", "weight": 1.0} -->

The set of constraints in the second line of form corners of a convex box polytope in the space of $n \times n$ matrices, which is necessary and sufficient to guarantee stability of. Thus, from the perspective of verifying stability of $A + {\DeltaA}$ this procedure no better than simply solving the same program with the first constraint deleted, which has a larger feasible set and thus will achieve at least as good a bound as. However, the solution of defines a hard upper limit on the following bounds we develop in this section which are based on a shared Lyapunov function, since gives the optimal bound. The bounds we develop in this section trade optimality (conservativeness) for the assurance that $P$ guarantees stability of the perturbed deterministic system without explicitly using the Lyapunov inequality $P \succeq {{({A + {\DeltaA}})}^{\intercal}P{({A + {\DeltaA}})}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Multivariate case", "weight": 1.0} -->

Giving up optimization over $P$ and instead choosing $Q$ arbitrarily (later in Sec.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

The unidirectional bound in of Thm. 3.2 can be made bidirectional by replacing with

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

Let $\theta_{i} \geq 0$ be scalars such that ${\sum_{i = 1}^{p}\theta_{i}} = 1$; these denote relative uncertainty in directions $A_{i}$. The largest robust stability bounds with respect to this choice of $\theta_{i}$ are obtained by setting $\eta_{i} = {y\theta_{i}}$ and maximizing the scalar $y$, which can be accomplished via bisection. As discussed earlier, optimizing a bidirectional bound over $P$, $Q$, and $y$ is equivalent to solving the full program.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Conservative simplifications", "weight": 1.0} -->

It can be shown that $\frac{1}{\sqrt{\zeta_{i}^{2} + \alpha_{i}} - \zeta_{i}}$ is convex in $\zeta_{i}$, so any linearization (first-order Taylor series expansion) will be a global underestimator of this function. Thus a conservative solution can be found by linearization, yielding a convex semidefinite constraint which can be expressed as a generalized eigenvalue problem which can be solved efficiently. For example, linearizing $\frac{1}{\sqrt{\zeta_{i}^{2} + \alpha_{i}} - \zeta_{i}}$ about $\zeta_{i} = 0$ yields $\frac{1}{\sqrt{\alpha_{i}}} + {\frac{1}{\alpha_{i}}\zeta_{i}}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Robustness via stability of auxiliary systems", "weight": 1.0} -->

Now, instead of requiring the same Lyapunov function to ensure mean-square stability of a stochastic system and stability of a perturbed deterministic system with the same nominal $A$, we construct auxiliary stochastic systems whose mean-square stability implies deterministic stability of the "target" perturbed deterministic system. Such an approach can be fundamentally more flexible than using a shared Lyapunov function since the open-loop dynamics of the auxiliary system are permitted to be significantly less stable.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

At first glance the condition of Thm. 3.2 may seem overly restrictive since it requires mean-square stability with a *scaled* $A$ matrix; indeed such a procedure is somewhat limiting in the open-loop setting since this can make the plant unstable. However, in the control design setting this *essentially does not matter* since the gain can be made larger to compensate, and because a simple scaling of $A$ does not affect controllability of the pair $(A,B)$; to see this, simply note that the rank of the controllability matrix $\begin{bmatrix}
\end{bmatrix}$ is unaffected by a nonzero scaling of $A$. The work of similarly leverages this fact.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Input uncertainties and robust control design algorithms", "weight": 1.0} -->

In the case where there are uncertainties in the input matrix $B$ under closed-loop state feedback, Theorems 3.2 and 4.1 are easily modified by simply substituting

<!-- chunk {"id": "body-0036", "role": "body", "section": "Input uncertainties and robust control design algorithms", "weight": 1.0} -->

where $0 \leq \mu_{i} < \eta_{i}$, $0 \leq \nu_{j} < \psi_{j}$ (bounds in negative directions also assured for Thm. 4.1). These results are formulated as Algorithms 1 and 2 for generating optimal, maximally robust controllers. Note that Algorithm 1 gives unidirectional bounds while Algorithm 2 gives bidirectional bounds; it is useful to retain the unidirectional bounds of Algorithm 1 in order to realize the potentially larger robustness margins in opposing directions.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Input uncertainties and robust control design algorithms", "weight": 1.0} -->

Input: Controllable nominal pair (A,B), cost matrices Q ≻ 0, R ≻ 0, uncertainty directions Ai, Bj and magnitudes θi &gt; 0, ϕj &gt; 0.
Output: Gain matrix K and margins ηi, ψj such that is stable for all 0 ≤ μi &lt; ηi, 0 ≤ νj &lt; ψj.
Define scalar z and scaled multiplicative noise variances αi = θi × z, and βj = ϕj × z
Find the largest z* which still admits a solution to P = gare(A,B,Q,R,αi,βj,Ai,Bj) via bisection
Define scalar y and scaled uncertainty magnitudes ηi = θi × y, ψj = ϕj × y
Find the largest scaling y* via bisection which satisfies

<!-- chunk {"id": "body-0038", "role": "body", "section": "Input uncertainties and robust control design algorithms", "weight": 1.0} -->

Input: Controllable nominal pair (A,B), cost matrices Q ≻ 0, R ≻ 0, uncertainty directions Ai, Bj and magnitudes θi &gt; 0, ϕj &gt; 0. Output: Gain matrix K and robustness margins ηi, ψj such that is stable for all |μi| &lt; ηi, |νj| &lt; ψj.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Input uncertainties and robust control design algorithms", "weight": 1.0} -->

still admits a solution to P = gare(Az,Bz,Q,R,αi,βj,Ai,Bj) via bisection Return control law $K = {- {\left( {R + {B_{z}^{\intercal}PB_{z}} + {\sum_{j = 1}^{q}{\beta_{j}B_{j}^{\intercal}PB_{j}}}} \right)^{- 1}B_{z}^{\intercal}PA_{z}}}$ where quantities P, βj and z are evaluated at y*, and margins ηi = θi × y*, ψj = ϕj × y* Algorithm 2 Robust control design

<!-- chunk {"id": "body-0040", "role": "body", "section": "Numerical results", "weight": 1.0} -->

Here we consider an inverted pendulum with a torque-producing actuator whose dynamics have been linearized about the vertical equilibrium. In continuous-time the dynamics are

<!-- chunk {"id": "body-0041", "role": "body", "section": "Numerical results", "weight": 1.0} -->

where $m_{c}$ is a normalized mass constant. A forward Euler discretization with step size $\Deltat$ yields

<!-- chunk {"id": "body-0042", "role": "body", "section": "Numerical results", "weight": 1.0} -->

Uncertainty on the mass constant $m_{c}$ corresponds to uncertainty on the $$ entry of $A$. We consider an example where the true mass constant is ${{bar}m_{c}} = 10$, but the nominal model underestimates it as $m_{c} = 5$; such a situation could easily arise during the initial phase of system identification in adaptive control with noisy measurements, or in time-varying scenarios such as a robot arm picking up a heavy load. We take a step size ${\Deltat} = 0.1$. The problem data is then

<!-- chunk {"id": "body-0043", "role": "body", "section": "Numerical results", "weight": 1.0} -->

Applying Algorithms 1, 2, and certainty-equivalent control design, we obtained the results in Table 1. We found the sets of true ${bar}A$ matrices stabilized by the controls from Algos. 1 and 2 were ${{bar}A} \in \begin{bmatrix}
\end{bmatrix}$ where ${|\mu_{1}|} < 3.970$ and ${|\mu_{1}|} < 6.997$ respectively. Stability of all systems within these sets was empirically verified by a fine grid search using 10000 samples of $\mu_{1}$ in each interval. Both robustness sets happened to include the true matrix ${bar}A$, so the robust controls were guaranteed to stabilize the true system, confirmed by ${\rho{({{{bar}A} + {{bar}BK}})}} < 1$. By contrast, the certainty-equivalent control failed to stabilize the true system.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Numerical results", "weight": 1.0} -->

This can be understood intuitively; the pendulum had a larger mass in reality than in the nominal model, so a larger control effort was necessary to stabilize the pendulum and prevent it from falling over. Although on this particular example Algorithm 1 gave a larger (unidirectional) robustness margin, in general this not need hold; certain problem instances admit much larger robustness margins using Algorithm 2 relative to Algorithm 1. Thus, our two algorithms may be considered complementary from a control design standpoint.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Numerical results", "weight": 1.0} -->

Code which implements this example is available:\

<!-- chunk {"id": "body-0046", "role": "body", "section": "Numerical results", "weight": 1.0} -->

Table 1. Stability results for robust control of an inverted pendulum.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

This work gives an effective methodology for certifying robustness and designing robust controllers with favorable properties and flexibility relative to competing approaches.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Direct extensions to this work include finding sharper bounds, e.g., via alternate auxiliary systems analogous to the one used in Section 4, and handling nonlinear dependence of the dynamics and/or noise on states and inputs. Future work will integrate the results of this work with adaptive model-based learning control for an end-to-end control framework which gracefully transitions from maximal robustness to maximal performance according to empirical uncertainties.
