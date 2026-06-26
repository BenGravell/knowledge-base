## Introduction

Stochastic optimal control under partial observability is a central problem in robotics, autonomous navigation, and aerospace systems. When the state cannot be measured directly, the controller must reason over a *belief*---a probability distribution over possible states---and plan in belief space, leading to partially observable Markov decision processes (POMDPs) that are generally intractable in continuous state, action, and observation spaces.

A powerful class of methods for *fully observed* stochastic control is path integral control (PIC), introduced by Kappen and closely related to linearly-solvable MDPs. PIC relies on a restrictive condition---the *matching condition*---requiring that the noise covariance $HH^{\top}$ be proportional to the control authority $G(x)\,R^{-1}G(x)^{\top}$. When this holds, the nonlinear HJB equation can be linearized via the Cole--Hopf transform, yielding a Feynman--Kac representation and enabling Monte Carlo solution. This principle underlies model predictive path integral control (MPPI) and has been extended to state-dependent diffusion, constrained formulations, and risk-sensitive variants. All of these methods, however, rely on full state observation.

Under partial observability, the natural state is no longer the physical state but the belief. This raises a critical question that has received limited attention: *can the matching condition required for Cole--Hopf linearization be satisfied in belief space?* Existing approaches to partially observed MPPI are primarily implementation-driven and do not analyze whether the matching condition extends to belief space. Mohamed et al. apply MPPI with local costmaps for navigation in unknown cluttered environments; Abraham et al. extend path integral control to learned uncertain dynamics; and Hoshino et al. combine a particle filter with per-particle path integral controllers. In parallel, belief-space planning methods such as LQG-MP and maximum-likelihood belief planning exploit Gaussian structure for trajectory optimization, but do not connect this structure to the PIC matching and linearization framework. Thus, while filtering-based and particle-based approximations exist, whether the matching condition underlying PIC can be satisfied in belief space remains an open question.

This paper addresses this gap by extending PIC to Gaussian belief space and analyzing its validity under partial observability. The contributions are as follows: (i) We show that the PIC matching condition in belief space requires affine observations, establishing a general impossibility result for nonlinear observation models. (ii) Under a Gaussian approximation, the belief covariance evolves deterministically, reducing the problem to stochastic control of the belief mean. We derive necessary and sufficient range-space conditions under which the matching condition holds in this reduced space, leading to exact Cole--Hopf linearization. (iii) We obtain a Feynman--Kac representation yielding the MPPI-Belief controller (Algorithm 1) and introduce a risk-sensitive cost extension.

The paper is organized as follows. Section II formulates the partially observed control problem. Section III derives the belief dynamics and shows that the matching condition cannot be satisfied in full belief space under non-affine observations. Section IV develops a Gaussian belief-space reduction and distinguishes the exact and approximate regimes. Section V presents the main theoretical results. Section VI presents the MPPI-Belief algorithm, and Section VII provides numerical validation.

### I-A Notation

We write $\mathrm{range}(M)$ and $\mathrm{rank}(M)$ for the range and rank of a matrix $M$, respectively; $\mathbb{S}_{+}^{n}$ and $\mathbb{S}_{++}^{n}$ for the cones of $n\times n$ positive semidefinite (PSD) and positive definite (SPD) matrices; $M^{\dagger}$ for the Moore--Penrose pseudoinverse; and $\mathcal{N}(\mu,\Sigma)$ for the Gaussian distribution with mean $\mu$ and covariance $\Sigma$.

## Problem Formulation

We consider a control-affine stochastic system in continuous time and continuous space, where the state is measured through a noisy output.

The state and observation equations are described by the stochastic differential equations where $x_{t}\in\mathbb{R}^{n}$ is the state, $u_{t}\in\mathbb{R}^{\ell}$ is the control input, and $y_{t}\in\mathbb{R}^{p}$ is the observation. The function $f:\mathbb{R}^{n}\to\mathbb{R}^{n}$ describes the uncontrolled drift, $G:\mathbb{R}^{n}\to\mathbb{R}^{n\times\ell}$ is the control input matrix, and $c:\mathbb{R}^{n}\to\mathbb{R}^{p}$ is the observation function. The matrix $H\in\mathbb{R}^{n\times m}$ determines the process noise channel, and $\sigma_{o}\in\mathbb{R}^{p\times p}$ is the observation noise matrix, assumed to be invertible. The Brownian motions $w_{t}\in\mathbb{R}^{m}$ and $\nu_{t}\in\mathbb{R}^{p}$ are mutually independent. We define the process noise covariance $Q:=HH^{\top}\in\mathbb{S}_{+}^{n}$ and the observation noise covariance $R_{o}:=\sigma_{o}\sigma_{o}^{\top}\in\mathbb{S}_{++}^{p}$.

Let $\mathcal{F}_{t}^{y}:=\sigma\{y_{s}:0\leq s\leq t\}$ denote the $\sigma$-algebra generated by the observation history up to time $t$. An *admissible control* is an $\mathcal{F}_{t}^{y}$-adapted, square-integrable process $\{u_{t}\}_{t\in[0,T]}$. This means that the control at time $t$ is determined based on the history of noisy observations $\{y_{s}\}_{0\leq s\leq t}$, rather than the system state $x_{t}$. The cost functional is given by where $\bar{\phi}:\mathbb{R}^{n}\to\mathbb{R}$ and $\bar{q}:\mathbb{R}^{n}\to\mathbb{R}$ are the terminal and running state costs, assumed to be non-negative, and $R\in\mathbb{S}_{++}^{\ell}$ is the control cost weight.

The partially observed control problem is formulated as follows.

### Problem 1

Consider the state and observation equations (1a)--(1b) and the cost functional. Find an admissible control $\{u_{t}\}_{t\in[0,T]}$ that minimizes the cost, given only the observation history $\{y_{s}\}_{0\leq s\leq t}$.

This problem is more challenging than the fully observed counterpart, since the controller cannot access the state $x_{t}$ directly and must instead reason over a probability distribution conditioned on the observation history.

Since $x_{t}$ is not directly accessible, the cost must be expressed in terms of the conditional distribution of the state given the observations, commonly referred to as the *belief*. The belief-space formulation applies to general partially observed systems and does not require Gaussianity. The Gaussian restriction introduced in Section IV is a computational choice that enables the finite-dimensional reduction used in the path integral construction below. Under a Gaussian belief $\pi_{t}=\mathcal{N}(\mu_{t},\Sigma_{t})$, we define the expected running cost and the analogous terminal cost $\phi(\mu,\Sigma)$. For quadratic $\bar{q}(x)=\tfrac{1}{2}\|x-x^{\mathrm{ref}}\|_{Q^{x}}^{2}$, this yields Thus, the expected cost decomposes into a term evaluated at the belief mean and a term that penalizes state uncertainty through the covariance. Dropping the trace term recovers the certainty-equivalent approach of planning on the mean alone, which underestimates the true expected cost whenever $\Sigma$ is non-trivial.

### Remark 1 (Classical PIC Matching)

For the fully observed system (1a) with cost, the *matching condition* requires $Q=\lambda\,G(x)\,R^{-1}G(x)^{\top}$ for some $\lambda>0$. This means that the process noise and the control input act through the same subspace of the state space. When matching holds, the associated HJB equation admits a Cole--Hopf linearization, which yields a linear PDE with a Feynman--Kac representation and enables Monte Carlo solution. Without matching, this linearization is not available. This structure underlies MPPI; when matching is only approximately satisfied, practical strategies such as importance-sampling corrections and modified cost formulations have been proposed.

## Belief Dynamics and Matching Impossibility

This section derives the belief dynamics for the partially observed system (1a)--(1b) and analyzes the structure of the resulting control and diffusion channels in belief space.

Since the state $x_{t}$ is not directly accessible, the controller must reason over the conditional distribution $\pi_{t}(\cdot):=\mathbb{P}(x_{t}\in\cdot\mid\mathcal{F}_{t}^{y})$, which is a measure-valued stochastic process. Its evolution is governed by the Kushner--Stratonovich equation (KSE): where $\mathcal{L}_{t}^{u*}$ is the Fokker--Planck operator associated with the controlled dynamics (1a), and $d\tilde{y}_{t}:=dy_{t}-\pi_{t}(c)\,dt$ is the *innovation process*, whose whitened form $R_{o}^{-1/2}d\tilde{y}_{t}$ is a standard $\mathcal{F}_{t}^{y}$-Brownian motion (see).

To examine whether the structure underlying path integral control in the fully observed setting (Remark 1. ‣ II Problem Formulation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")) extends to belief space, we rewrite the belief dynamics in the form $d\pi=a^{u}(\pi)\,dt+b(\pi)\,d\tilde{y}$. In particular, this yields Thus, (6a) shows that the drift depends on the control through the divergence term $-\nabla\cdot(G(x)\,u\;\pi(x))$, whereas (6b) shows that the diffusion is independent of $u$.

In the fully observed setting (Remark 1. ‣ II Problem Formulation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")), matching requires that the diffusion and control channels be aligned. An analogous condition in belief space would require that the observation-driven diffusion (6b) be proportional to the control-induced perturbation (6a). If such a condition held, the corresponding belief-space HJB equation would admit a Cole--Hopf linearization, yielding a Feynman--Kac representation and enabling sampling-based control, as in the fully observed case. The following result characterizes when this is possible.

### Theorem 1 (Affine Observation Characterization)

Consider the system (1a)--(1b) with constant $G\in\mathbb{R}^{n\times\ell}$ and observation function $c:\mathbb{R}^{n}\to\mathbb{R}^{p}$. Restrict the belief to the Gaussian family $\{\pi_{\mu}=\mathcal{N}(\mu,\Sigma):\mu\in\mathbb{R}^{n}\}$ with fixed $\Sigma\succ 0$. Then the observation-driven diffusion lies in the tangent space of this Gaussian mean manifold if and only if for some matrix-valued function $A(\mu)\in\mathbb{R}^{p\times n}$. Moreover, this holds if and only if $c$ is affine: $c(x)=Ax+b$ for some constant matrix $A\in\mathbb{R}^{p\times n}$ and vector $b\in\mathbb{R}^{p}$.

### Proof

Under the Gaussian family $\pi_{\mu}=\mathcal{N}(\mu,\Sigma)$ with fixed $\Sigma\succ 0$, the mean-tangent direction is proportional to $\Sigma^{-1}(x-\mu)\,\pi_{\mu}(x)$, while the observation-induced diffusion (6b) is proportional to $\pi_{\mu}(x)\bigl(c(x)-\bar{c}(\mu)\bigr)$, where $\bar{c}(\mu):=\mathbb{E}_{\pi_{\mu}}[c(x)]$. Thus, the observation-driven diffusion lies in the Gaussian mean tangent space if and only if $c(x)-\bar{c}(\mu)=A(\mu)(x-\mu)$ for some $A(\mu)\in\mathbb{R}^{p\times n}$. Evaluating at $\mu_{1}\neq\mu_{2}$ and subtracting: The left-hand side is independent of $x$, so $A(\mu_{1})=A(\mu_{2})$. Since $\mu_{1},\mu_{2}$ are arbitrary, $A(\mu)\equiv A$ is constant. Substituting back gives $c(x)=Ax+(\bar{c}(\mu)-A\mu)$; since the left-hand side is independent of $\mu$, the quantity $\bar{c}(\mu)-A\mu$ is constant, yielding $c(x)=Ax+b$. The converse is immediate. ∎ The restriction to fixed $\Sigma$ in Theorem 1. ‣ III Belief Dynamics and Matching Impossibility ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems") isolates the role of the observation function $c$; the time-varying covariance case is addressed in Section IV, where matching feasibility is analyzed for the resulting time-varying diffusion $D_{t}$ (Proposition 3. ‣ V-B Matching Condition and Feasibility ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")). For state-dependent $G(x)$, the same difficulty persists, as the observation and control channels are generically misaligned.

### Remark 2

In particular, every scalar linear-Gaussian system ($c(x)=ax+b$, $G\neq 0$) satisfies Theorem 1. ‣ III Belief Dynamics and Matching Impossibility ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems") and, provided $D_{t}\neq 0$, also satisfies the range condition of Proposition 3. ‣ V-B Matching Condition and Feasibility ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems"). Thus, belief-space PIC applies exactly in this case.

This motivates restricting the belief to a finite-dimensional family of distributions.

## Gaussian Belief-Space Approximation

In this section, we focus on the Gaussian family $\pi_{t}=\mathcal{N}{(\mu_{t},\Sigma_{t})}$ and derive the resulting mean and covariance dynamics.

We state the following classical result explicitly, as the deterministic evolution of $\Sigma_{t}$ is the property that enables the belief-space PIC reduction developed in Section V.

### Proposition 2 (Deterministic Covariance: Linear Case)

For the linear system $f(x)=Ax$, $G(x)=B$, and $c(x)=Cx$ in (1a)--(1b), the conditional distribution $\pi_{t}=\mathcal{N}(\mu_{t},\Sigma_{t})$ is exactly Gaussian, with where $K_{t}:=\Sigma_{t}C^{\top}R_{o}^{-1}$ is the Kalman gain. The innovation process in specializes to $d\tilde{y}_{t}=dy_{t}-C\mu_{t}\,dt$ in the linear-Gaussian case, since $\pi_{t}(c)=C\mu_{t}$. The Riccati equation (8b. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")) is a deterministic ODE, independent of both the observations and the control input.

### Proof

The exact Gaussianity of $\pi_{t}$ and the dynamics (8. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")) follow from Kalman--Bucy filtering theory. The Riccati equation (8b. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")) is deterministic by construction. ∎ A key consequence of Proposition 2. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems") is that the stochastic component of the mean dynamics is driven entirely by the innovation process, with effective covariance The matrix $D_{t}$ quantifies the strength of the innovation-driven fluctuations in the belief mean: larger values of $D_{t}$ indicate that new observations have a stronger effect on the state estimate, whereas $D_{t}=0$ implies that the belief mean is not updated by the observations. Let $r_{t}:=\mathrm{rank}(D_{t})$ and let $L_{t}\in\mathbb{R}^{n\times r_{t}}$ satisfy $D_{t}=L_{t}L_{t}^{\top}$.

Since the quadratic variation of $K_{t}\,d\tilde{y}_{t}$ is $D_{t}\,dt$, factoring $D_{t}=L_{t}L_{t}^{\top}$ and defining $\beta_{t}$ through the innovation process allow the mean dynamics (8a. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")) to be written as where $\beta_{t}\in\mathbb{R}^{r_{t}}$ is a standard Brownian motion adapted to $\mathcal{F}_{t}^{y}$. Since $\Sigma_{t}$ is deterministic, both $D_{t}$ and $L_{t}$ are deterministic functions of time, so is a standard SDE driven by the innovation Brownian motion.

### Remark 3 (Nonlinear Case: EKF Approximation)

For nonlinear systems (1a)--(1b), linearizing $f$ and $c$ about a nominal trajectory $\bar{\mu}_{t}$ with $A_{t}:=\partial f/\partial x|_{\bar{\mu}_{t}}$ and $C_{t}:=\partial c/\partial x|_{\bar{\mu}_{t}}$ yields the EKF analogue of (8b. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")): which is a deterministic ODE once $\bar{\mu}_{t}$ is specified. This follows from a first-order Taylor expansion of the drift and observation functions, under which the KSE reduces formally to the Kalman--Bucy form (8. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")) with time-varying Jacobians $A_{t}$ and $C_{t}$ (see, e.g.,). The neglected residual is formally second-order in $\|\mu_{t}-\bar{\mu}_{t}\|$, with constants depending on the local curvature of $f$ and $c$; a rigorous bound is beyond the scope of this paper.

### Assumption 1 (Deterministic Gain Schedule)

Over $[0,T]$, the quantities $K_{t}$, $\Sigma_{t}$, and $D_{t}:=K_{t}R_{o}K_{t}^{\top}$ are assumed to be predetermined deterministic functions of time, obtained by solving (8b. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")) in the linear case or (11. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")) in the nonlinear case about a nominal trajectory. For nonlinear systems, we write $\bar{G}_{t}:=G(\bar{\mu}_{t})$. For linear systems, $\bar{G}_{t}=B$ for all $t$.

Under Assumption 1. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems"), the belief-mean dynamics are approximated by where $D_{t}=L_{t}L_{t}^{\top}$ is deterministic. Since $\Sigma_{t}$ is a known function of time, the covariance contribution to the cost becomes a deterministic time-dependent term. Accordingly, we define the *reduced running cost* $q_{t}(\mu):=q(\mu,\Sigma(t))$ and the *reduced terminal cost* $\phi_{T}(\mu):=\phi(\mu,\Sigma(T))$.

## Path Integral Control in Gaussian Belief Space

This section develops the main theoretical results in Gaussian belief space: matching feasibility, Cole--Hopf linearization, and the Feynman--Kac representation. While the Cole--Hopf and Feynman--Kac machinery is classical in fully observed PIC, the present setting is different because the reduced belief-mean dynamics are driven by the diffusion $D_{t}$ induced by the observation channel rather than by the process noise. Accordingly, the belief-space matching condition involves the observation-driven diffusion $D_{t}$ rather than the process noise $Q$, and its feasibility is characterized by Proposition 3. ‣ V-B Matching Condition and Feasibility ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems").

### V-A HJB Equation for the Belief Mean

Since $\Sigma_{t}$ is deterministic under Assumption 1. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems"), the stochastic optimal control problem for the belief-mean dynamics under the reduced costs $q_{t}$ and $\phi_{T}$ reduces to a standard finite-dimensional problem. Let $V(t,\mu)$ denote the corresponding optimal cost-to-go, which satisfies the HJB equation: with $V(T,\mu)=\phi_{T}(\mu)$. First-order optimality yields $u^{*}=-R^{-1}\bar{G}_{t}^{\top}\,\nabla_{\mu}V$, and substitution into gives the minimized HJB: The quadratic gradient term in renders the equation nonlinear. The next subsection identifies conditions under which this term can be removed by the Cole--Hopf transformation.

### V-B Matching Condition and Feasibility

In the fully observed setting (Remark 1. ‣ II Problem Formulation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")), the Cole--Hopf transformation requires that the diffusion covariance equal a scaled version of the control authority matrix $GR^{-1}G^{\top}$. We now state the analogous requirement for the belief-mean dynamics. Given this condition, the Cole--Hopf linearization follows by the same algebraic mechanism as in the fully observed case. The non-trivial question is whether and when this condition can be satisfied in belief space; this is addressed by Proposition 3. ‣ V-B Matching Condition and Feasibility ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems") below.

### Assumption 2 (Scheduled Matching)

The belief-mean diffusion matrix $D_{t}$ and the scheduled control matrix $\bar{G}_{t}$ satisfy, for each $t\in[0,T]$, where $\lambda>0$ is the path integral temperature.

### Proposition 3 (Matching Feasibility)

*(i)* There exists a symmetric matrix $W\succeq 0$ such that $D_{t}=\lambda\,\bar{G}_{t}W\bar{G}_{t}^{\top}$ if and only if $\mathrm{range}(D_{t})\subseteq\mathrm{range}(\bar{G}_{t})$.

*(ii)* There exists $R\succ 0$ satisfying (15. ‣ V-B Matching Condition and Feasibility ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")) if and only if $\mathrm{range}(D_{t})=\mathrm{range}(\bar{G}_{t})$.

### Proof

For part (i), note that $\mathrm{range}(\bar{G}_{t}W\bar{G}_{t}^{\top})\subseteq\mathrm{range}(\bar{G}_{t})$ for any $W$, so the range inclusion is necessary. Conversely, if $\mathrm{range}(D_{t})\subseteq\mathrm{range}(\bar{G}_{t})$, then $D_{t}^{1/2}$ admits a factorization $D_{t}^{1/2}=\bar{G}_{t}M$ for some matrix $M$, and setting $W=MM^{\top}/\lambda$ yields the result.

For part (ii), if $R\succ 0$ then $R^{-1}\succ 0$, so $\mathrm{range}(\bar{G}_{t}R^{-1}\bar{G}_{t}^{\top})=\mathrm{range}(\bar{G}_{t})$, which forces range equality.Conversely, given $\mathrm{range}(D_{t})=\mathrm{range}(\bar{G}_{t})$, one can construct an SPD matrix $R^{-1}$ by solving on $\mathrm{range}(\bar{G}_{t})$ via the SVD and extending to a full-rank matrix using a positive multiple of the projector onto $\ker(\bar{G}_{t})$. ∎ Here $R\succ 0$ is the fixed control cost weight. Since $D_{t}$ and $\bar{G}_{t}$ vary with $t$, the condition (15. ‣ V-B Matching Condition and Feasibility ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")) is verified pointwise; $W$ in part (i) is an auxiliary existence variable, not a design parameter.

### V-C Cole--Hopf Linearization

Define the *desirability function* $\Psi(t,\mu):=\exp(-V(t,\mu)/\lambda)$, so that $V(t,\mu)=-\lambda\log\Psi(t,\mu)$.

### Theorem 4 (Exact Linearization via Cole--Hopf)

Under Assumptions 1. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems") and 2. ‣ V-B Matching Condition and Feasibility ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems"), the substitution $V(t,\mu)=-\lambda\log\Psi(t,\mu)$ converts the HJB equation into the linear PDE with terminal condition, $\Psi(T,\mu)=\exp(-\phi_{T}(\mu)/\lambda).$

### Proof

From $V=-\lambda\log\Psi$, direct computation gives Substituting into, the Hessian trace produces $(\lambda/2\Psi^{2})(\nabla_{\mu}\Psi)^{\top}D_{t}\nabla_{\mu}\Psi$, while the quadratic control term yields $-(\lambda^{2}/2\Psi^{2})(\nabla_{\mu}\Psi)^{\top}\bar{G}_{t}R^{-1}\bar{G}_{t}^{\top}\nabla_{\mu}\Psi$. Under the matching condition (15. ‣ V-B Matching Condition and Feasibility ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")), these cancel exactly, giving (16. ‣ V-C Cole–Hopf Linearization ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")). ∎ Since (16. ‣ V-C Cole–Hopf Linearization ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")) is linear, the desirability admits the following stochastic representation.

### Corollary 5 (Belief-Space Feynman--Kac Representation)

Under Assumptions 1. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems") and 2. ‣ V-B Matching Condition and Feasibility ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems"), let $\mathbb{Q}$ denote the probability measure corresponding to the uncontrolled belief-mean dynamics. Then This expresses the desirability as an expectation over uncontrolled belief-mean trajectories, enabling Monte Carlo approximation.

### Remark 4 (Risk-Sensitive Extension)

The expected cost $q(\mu,\Sigma)=\mathbb{E}[\bar{q}(x)]$ can be replaced by $q_{\mathrm{RS}}=\mathbb{E}[\bar{q}(x)]+\frac{\theta}{2}\mathrm{Var}[\bar{q}(x)]$, obtained from the cumulant expansion of the entropic risk measure. The parameter $\theta>0$ controls risk aversion, and $\theta=0$ recovers the risk-neutral cost. The PIC structure is preserved since only the running cost is modified.

## MPPI-Belief Algorithm

This section develops a discrete-time Monte Carlo approximation of the belief-space control law and presents the resulting MPPI-Belief algorithm.

Under an Euler--Maruyama discretization of the uncontrolled belief-mean dynamics with $u_{t}\equiv 0$ at times $t_{k}=k\Delta t$, the transitions are where $L_{k}L_{k}^{\top}=D_{t_{k}}$ and $r_{k}:=\mathrm{rank}(D_{t_{k}})$.

### Theorem 6 (Discrete-Time Control Law)

Under Assumptions 1. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")--2. ‣ V-B Matching Condition and Feasibility ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems"), and freezing the coefficients over the first time step (standard in MPPI), the control law at step $k=0$ is where $\bar{G}_{0}:=G(\bar{\mu}_{0})$, the normalized importance weights are $\tilde{w}^{(i)}:=w^{(i)}/\sum_{j}w^{(j)}$ with $w^{(i)}:=\exp(-S^{(i)}/\lambda)$, and $S^{(i)}$ is the path cost of trajectory $i$. For rank-deficient $D_{0}$, the pseudoinverse restricts the score to $\mathrm{range}(D_{0})$, ensuring well-posedness for underactuated systems.

### Proof

From the first-order optimality condition $u^{*}=-R^{-1}\bar{G}_{t}^{\top}\nabla_{\mu}V$ and $\nabla_{\mu}V=-(\lambda/\Psi)\nabla_{\mu}\Psi$, By the Feynman--Kac representation (Corollary 5. ‣ V-C Cole–Hopf Linearization ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")), the quantity $\nabla_{\mu_{0}}\log\Psi$ can be written as a cost-weighted expectation of the score function of the uncontrolled transition density. For the discrete transition with covariance $D_{0}\Delta t$, the score restricted to $\mathrm{range}(D_{0})$ is $D_{0}^{\dagger}L_{0}\epsilon_{0}/\Delta t$. Substituting the matching condition $D_{0}=\lambda\bar{G}_{0}R^{-1}\bar{G}_{0}^{\top}$ gives Approximating the resulting expectation with $N$ Monte Carlo samples yields (19. ‣ VI MPPI-Belief Algorithm ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")). ∎ The complete MPPI-Belief algorithm is given in Algorithm 1.

0: Belief (μ0, Σ0), number of samples N, horizon length H = T/Δt, step size Δt, temperature λ 1: Precompute {Σk, Kk, Dk, Lk}k = 0H by solving the Riccati equation along the nominal trajectory μ̄ In practice, Algorithm 1 is applied in a receding-horizon fashion: at each time step, the belief $(\mu_{0},\Sigma_{0})$ is updated from the latest filter estimate, and only the control $u_{0}^{*}$ is applied before replanning. In contrast to particle-filter-based methods such as PIPF, which combine filtering particles with per-particle path integral sampling, MPPI-Belief operates on a single belief-mean trajectory with $N$ samples.

## Numerical Validation

We evaluate on a 2D double-integrator with state $x=[p_{x},p_{y},v_{x},v_{y}]^{\top}$, control $u\in\mathbb{R}^{2}$, and position-only observations ($C=[I_{2}\;0_{2\times 2}]$). The observation noise is $\sigma_{o}(p_{x})=|p_{x}-x_{\text{light}}|/\sqrt{2}+0.1$ with $x_{\text{light}}=5$ m, producing a light region where observations are most accurate. Two obstacles at $(3,\pm 1)$ m with radius $0.65$ m form a corridor in a high-noise region; process noise is $\sigma_{w}=0.30$. All sampling-based methods use $N{=}500$ samples, $H{=}30$, $\Delta t{=}0.1$ s, and $\lambda{=}1$.

We compare MPPI-Belief with the risk-sensitive cost of Remark 4. ‣ V-C Cole–Hopf Linearization ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems") ($\theta{=}1$) against EKF-iLQG, CE-MPPI ($\theta{=}0$), and PIPF ($K{=}50$ particles, $L{=}200$ samples). All sampling-based baselines share the same cost function, temperature, and horizon, while differing primarily in planning and filtering architecture.^11^1Our PIPF uses a bootstrap particle filter and the same MPPI importance weighting as CE-MPPI, rather than the KL-optimal proposal of; thus, our implementation should be viewed as a simplified PIPF-style baseline rather than an exact reproduction.

TABLE I: Comparative performance of four controllers on the gradient light-dark domain (200 Monte Carlo trials).

Table I and Fig. 1 show that MPPI-Belief is the only method achieving zero collisions over 200 trials, while the baselines incur 18--25%. The risk-sensitive belief cost couples obstacle proximity with covariance, encouraging detours through the informative region before traversing the corridor. The optimized matching residual is $\varepsilon^{*}=0.79$, indicating that useful performance is retained despite approximate matching.

Figure 1: Sample trajectories (50 per method) on the gradient light-dark domain. Background shading indicates observation noise σo(px); the light region near px = 5 m provides accurate observations.

Figure 2: Obstacle-weight sweep (200 trials per point). (a) Collision rate versus wobs. (b) Base cost excluding obstacle penalties. MPPI-Belief attains zero collisions at sufficiently large wobs, unlike the baselines.

In Fig. 2, we sweep the planning obstacle penalty weight $w_{\mathrm{obs}}\in[10^{2},10^{4}]$ for each method to test whether the safety improvement is merely a tuning artifact. The results show that increasing $w_{\mathrm{obs}}$ across two orders of magnitude has little effect on the baselines, which remain between 11% and 33% collision rate, whereas MPPI-Belief drops below 1% by $w_{\mathrm{obs}}{=}500$ and reaches 0% at 2500. No baseline reaches 0% at any weight tested, indicating that collisions are driven by estimation uncertainty rather than insufficient obstacle penalty.

Finally, we isolate the role of the risk-sensitive parameter by sweeping $\theta\in\{0,0.5,1,2,5\}$ over 200 trials per setting (detailed results omitted for brevity). At $\theta{=}0$ (expected cost only), the collision rate is 23.0% with mean clearance 0.11 m. Even moderate risk aversion ($\theta{=}0.5$) reduces collisions to 2.5% and increases clearance to 0.80 m. The best performance occurs at $\theta{=}1$, achieving 0% collisions and 0.82 m clearance with modest cost increase ($56.6$ vs. $51.3$). For $\theta\geq 2$, collision rates rise slightly (0.5--1.5%), suggesting that excessive risk aversion can induce over-conservatism. The variance penalty $(\theta/2)\mathrm{Var}[\bar{q}]$ is thus the primary driver of safe behavior, amplifying obstacle costs in high-uncertainty regions.

## Conclusion

This paper studied path integral control for partially observed systems via a Gaussian belief-space approximation. We showed that the matching condition generally fails in full belief space, and characterized when it can hold in the reduced Gaussian setting. This yields a belief-space path integral formulation and the MPPI-Belief algorithm. Numerical experiments showed improved safety relative to certainty-equivalent and particle-filter-based baselines at practical computational cost. Future work will consider nonlinear observation models, non-Gaussian belief representations, and hardware validation.
