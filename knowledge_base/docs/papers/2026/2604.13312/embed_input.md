<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Path Integral Control in Gaussian Belief Space for Partially Observed Systems

Topics include Bellman equations, Diffusion models, Control, Model predictive path integral belief, PIC.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper extends path integral control (PIC) to partially observed systems by formulating the problem in Gaussian belief space. PIC relies on the diffusion being proportional to the control channel - the so-called matching condition - to linearize the Hamilton-Jacobi-Bellman equation via the Cole-Hopf transform; we show that this condition fails in infinite-dimensional belief space under non-affine observations. Restricting to Gaussian beliefs yields a finite-dimensional approximation with deterministic covariance evolution, reducing the problem to stochastic control of the belief mean. We derive necessary and sufficient conditions for matching in this reduced space, obtain an exact Cole-Hopf linearization with a Feynman-Kac representation, and develop the MPPI-Belief algorithm. Numerical experiments on a navigation task with state-dependent observation noise demonstrate the effectiveness of MPPI-Belief relative to certainty-equivalent and particle-filter-based baselines.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochastic optimal control under partial observability is a central problem in robotics, autonomous navigation, and aerospace systems. When the state cannot be measured directly, the controller must reason over a *belief*---a probability distribution over possible states---and plan in belief space, leading to partially observable Markov decision processes (POMDPs) that are generally intractable in continuous state, action, and observation spaces.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A powerful class of methods for *fully observed* stochastic control is path integral control (PIC), introduced by Kappen and closely related to linearly-solvable MDPs. PIC relies on a restrictive condition---the *matching condition*---requiring that the noise covariance $HH^{\top}$ be proportional to the control authority $G(x)\,R^{-1}G(x)^{\top}$. When this holds, the nonlinear HJB equation can be linearized via the Cole--Hopf transform, yielding a Feynman--Kac representation and enabling Monte Carlo solution. This principle underlies model predictive path integral control (MPPI) and has been extended to state-dependent diffusion, constrained formulations, and risk-sensitive variants. All of these methods, however, rely on full state observation.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Under partial observability, the natural state is no longer the physical state but the belief. This raises a critical question that has received limited attention: *can the matching condition required for Cole--Hopf linearization be satisfied in belief space?* Existing approaches to partially observed MPPI are primarily implementation-driven and do not analyze whether the matching condition extends to belief space. Mohamed et al. apply MPPI with local costmaps for navigation in unknown cluttered environments; Abraham et al. extend path integral control to learned uncertain dynamics; and Hoshino et al. combine a particle filter with per-particle path integral controllers. In parallel, belief-space planning methods such as LQG-MP and maximum-likelihood belief planning exploit Gaussian structure for trajectory optimization, but do not connect this structure to the PIC matching and linearization framework. Thus, while filtering-based and particle-based approximations exist, whether the matching condition underlying PIC can be satisfied in belief space remains an open question.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper addresses this gap by extending PIC to Gaussian belief space and analyzing its validity under partial observability. The contributions are as follows: (i) We show that the PIC matching condition in belief space requires affine observations, establishing a general impossibility result for nonlinear observation models. (ii) Under a Gaussian approximation, the belief covariance evolves deterministically, reducing the problem to stochastic control of the belief mean. We derive necessary and sufficient range-space conditions under which the matching condition holds in this reduced space, leading to exact Cole--Hopf linearization. (iii) We obtain a Feynman--Kac representation yielding the MPPI-Belief controller (Algorithm 1) and introduce a risk-sensitive cost extension.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is organized as follows. Section II formulates the partially observed control problem. Section III derives the belief dynamics and shows that the matching condition cannot be satisfied in full belief space under non-affine observations. Section IV develops a Gaussian belief-space reduction and distinguishes the exact and approximate regimes. Section V presents the main theoretical results. Section VI presents the MPPI-Belief algorithm, and Section VII provides numerical validation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Notation", "weight": 1.0} -->

We write $\mathrm{range}(M)$ and $\mathrm{rank}(M)$ for the range and rank of a matrix $M$, respectively; $\mathbb{S}_{+}^{n}$ and $\mathbb{S}_{++}^{n}$ for the cones of $n\times n$ positive semidefinite (PSD) and positive definite (SPD) matrices; $M^{\dagger}$ for the Moore--Penrose pseudoinverse; and $\mathcal{N}(\mu,\Sigma)$ for the Gaussian distribution with mean $\mu$ and covariance $\Sigma$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We consider a control-affine stochastic system in continuous time and continuous space, where the state is measured through a noisy output.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The state and observation equations are described by the stochastic differential equations where $x_{t}\in\mathbb{R}^{n}$ is the state, $u_{t}\in\mathbb{R}^{\ell}$ is the control input, and $y_{t}\in\mathbb{R}^{p}$ is the observation. The function $f:\mathbb{R}^{n}\to\mathbb{R}^{n}$ describes the uncontrolled drift, $G:\mathbb{R}^{n}\to\mathbb{R}^{n\times\ell}$ is the control input matrix, and $c:\mathbb{R}^{n}\to\mathbb{R}^{p}$ is the observation function.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Let $\mathcal{F}_{t}^{y}:=\sigma\{y_{s}:0\leq s\leq t\}$ denote the $\sigma$-algebra generated by the observation history up to time $t$. An *admissible control* is an $\mathcal{F}_{t}^{y}$-adapted, square-integrable process $\{u_{t}\}_{t\in[0,T]}$. This means that the control at time $t$ is determined based on the history of noisy observations $\{y_{s}\}_{0\leq s\leq t}$, rather than the system state $x_{t}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The cost functional is given by where $\bar{\phi}:\mathbb{R}^{n}\to\mathbb{R}$ and $\bar{q}:\mathbb{R}^{n}\to\mathbb{R}$ are the terminal and running state costs, assumed to be non-negative, and $R\in\mathbb{S}_{++}^{\ell}$ is the control cost weight.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The partially observed control problem is formulated as follows.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Consider the state and observation equations (1a)--(1b) and the cost functional. Find an admissible control $\{u_{t}\}_{t\in[0,T]}$ that minimizes the cost, given only the observation history $\{y_{s}\}_{0\leq s\leq t}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem 1", "weight": 1.0} -->

This problem is more challenging than the fully observed counterpart, since the controller cannot access the state $x_{t}$ directly and must instead reason over a probability distribution conditioned on the observation history.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Since $x_{t}$ is not directly accessible, the cost must be expressed in terms of the conditional distribution of the state given the observations, commonly referred to as the *belief*. The belief-space formulation applies to general partially observed systems and does not require Gaussianity. The Gaussian restriction introduced in Section IV is a computational choice that enables the finite-dimensional reduction used in the path integral construction below. Under a Gaussian belief $\pi_{t}=\mathcal{N}(\mu_{t},\Sigma_{t})$, we define the expected running cost and the analogous terminal cost $\phi(\mu,\Sigma)$. For quadratic $\bar{q}(x)=\tfrac{1}{2}\|x-x^{\mathrm{ref}}\|_{Q^{x}}^{2}$, this yields Thus, the expected cost decomposes into a term evaluated at the belief mean and a term that penalizes state uncertainty through the covariance.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Dropping the trace term recovers the certainty-equivalent approach of planning on the mean alone, which underestimates the true expected cost whenever $\Sigma$ is non-trivial.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 1 (Classical PIC Matching)", "weight": 1.0} -->

For the fully observed system (1a) with cost, the *matching condition* requires $Q=\lambda\,G(x)\,R^{-1}G(x)^{\top}$ for some $\lambda>0$. This means that the process noise and the control input act through the same subspace of the state space. When matching holds, the associated HJB equation admits a Cole--Hopf linearization, which yields a linear PDE with a Feynman--Kac representation and enables Monte Carlo solution. Without matching, this linearization is not available. This structure underlies MPPI; when matching is only approximately satisfied, practical strategies such as importance-sampling corrections and modified cost formulations have been proposed.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Belief Dynamics and Matching Impossibility", "weight": 1.0} -->

This section derives the belief dynamics for the partially observed system (1a)--(1b) and analyzes the structure of the resulting control and diffusion channels in belief space.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Belief Dynamics and Matching Impossibility", "weight": 1.0} -->

Since the state $x_{t}$ is not directly accessible, the controller must reason over the conditional distribution $\pi_{t}(\cdot):=\mathbb{P}(x_{t}\in\cdot\mid\mathcal{F}_{t}^{y})$, which is a measure-valued stochastic process. Its evolution is governed by the Kushner--Stratonovich equation (KSE): where $\mathcal{L}_{t}^{u*}$ is the Fokker--Planck operator associated with the controlled dynamics (1a), and $d\tilde{y}_{t}:=dy_{t}-\pi_{t}(c)\,dt$ is the *innovation process*, whose whitened form $R_{o}^{-1/2}d\tilde{y}_{t}$ is a standard $\mathcal{F}_{t}^{y}$-Brownian motion (see).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Belief Dynamics and Matching Impossibility", "weight": 1.0} -->

To examine whether the structure underlying path integral control in the fully observed setting (Remark 1. ‣ II Problem Formulation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")) extends to belief space, we rewrite the belief dynamics in the form $d\pi=a^{u}(\pi)\,dt+b(\pi)\,d\tilde{y}$. In particular, this yields Thus, (6a) shows that the drift depends on the control through the divergence term $-\nabla\cdot(G(x)\,u\;\pi(x))$, whereas (6b) shows that the diffusion is independent of $u$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Belief Dynamics and Matching Impossibility", "weight": 1.0} -->

In the fully observed setting (Remark 1. ‣ II Problem Formulation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")), matching requires that the diffusion and control channels be aligned. An analogous condition in belief space would require that the observation-driven diffusion (6b) be proportional to the control-induced perturbation (6a). If such a condition held, the corresponding belief-space HJB equation would admit a Cole--Hopf linearization, yielding a Feynman--Kac representation and enabling sampling-based control, as in the fully observed case. The following result characterizes when this is possible.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 2", "weight": 1.0} -->

In particular, every scalar linear-Gaussian system ($c(x)=ax+b$, $G\neq 0$) satisfies Theorem 1. ‣ III Belief Dynamics and Matching Impossibility ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems") and, provided $D_{t}\neq 0$, also satisfies the range condition of Proposition 3. ‣ V-B Matching Condition and Feasibility ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems"). Thus, belief-space PIC applies exactly in this case.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 2", "weight": 1.0} -->

This motivates restricting the belief to a finite-dimensional family of distributions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Gaussian Belief-Space Approximation", "weight": 1.0} -->

In this section, we focus on the Gaussian family $\pi_{t}=\mathcal{N}{(\mu_{t},\Sigma_{t})}$ and derive the resulting mean and covariance dynamics.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Gaussian Belief-Space Approximation", "weight": 1.0} -->

We state the following classical result explicitly, as the deterministic evolution of $\Sigma_{t}$ is the property that enables the belief-space PIC reduction developed in Section V.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 3 (Nonlinear Case: EKF Approximation)", "weight": 1.0} -->

For nonlinear systems (1a)--(1b), linearizing $f$ and $c$ about a nominal trajectory $\bar{\mu}_{t}$ with $A_{t}:=\partial f/\partial x|_{\bar{\mu}_{t}}$ and $C_{t}:=\partial c/\partial x|_{\bar{\mu}_{t}}$ yields the EKF analogue of (8b. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")): which is a deterministic ODE once $\bar{\mu}_{t}$ is specified. This follows from a first-order Taylor expansion of the drift and observation functions, under which the KSE reduces formally to the Kalman--Bucy form (8. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")) with time-varying Jacobians $A_{t}$ and $C_{t}$ (see, e.g.,).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 3 (Nonlinear Case: EKF Approximation)", "weight": 1.0} -->

The neglected residual is formally second-order in $\|\mu_{t}-\bar{\mu}_{t}\|$, with constants depending on the local curvature of $f$ and $c$; a rigorous bound is beyond the scope of this paper.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 1 (Deterministic Gain Schedule)", "weight": 1.0} -->

Over $[0,T]$, the quantities $K_{t}$, $\Sigma_{t}$, and $D_{t}:=K_{t}R_{o}K_{t}^{\top}$ are assumed to be predetermined deterministic functions of time, obtained by solving (8b. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")) in the linear case or (11. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")) in the nonlinear case about a nominal trajectory. For nonlinear systems, we write $\bar{G}_{t}:=G(\bar{\mu}_{t})$. For linear systems, $\bar{G}_{t}=B$ for all $t$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 1 (Deterministic Gain Schedule)", "weight": 1.0} -->

Under Assumption 1. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems"), the belief-mean dynamics are approximated by where $D_{t}=L_{t}L_{t}^{\top}$ is deterministic. Since $\Sigma_{t}$ is a known function of time, the covariance contribution to the cost becomes a deterministic time-dependent term. Accordingly, we define the *reduced running cost* $q_{t}(\mu):=q(\mu,\Sigma(t))$ and the *reduced terminal cost* $\phi_{T}(\mu):=\phi(\mu,\Sigma(T))$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Path Integral Control in Gaussian Belief Space", "weight": 1.0} -->

This section develops the main theoretical results in Gaussian belief space: matching feasibility, Cole--Hopf linearization, and the Feynman--Kac representation. While the Cole--Hopf and Feynman--Kac machinery is classical in fully observed PIC, the present setting is different because the reduced belief-mean dynamics are driven by the diffusion $D_{t}$ induced by the observation channel rather than by the process noise. Accordingly, the belief-space matching condition involves the observation-driven diffusion $D_{t}$ rather than the process noise $Q$, and its feasibility is characterized by Proposition 3. ‣ V-B Matching Condition and Feasibility ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems").

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-A HJB Equation for the Belief Mean", "weight": 1.0} -->

Since $\Sigma_{t}$ is deterministic under Assumption 1. ‣ IV Gaussian Belief-Space Approximation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems"), the stochastic optimal control problem for the belief-mean dynamics under the reduced costs $q_{t}$ and $\phi_{T}$ reduces to a standard finite-dimensional problem. Let $V(t,\mu)$ denote the corresponding optimal cost-to-go, which satisfies the HJB equation: with $V(T,\mu)=\phi_{T}(\mu)$. First-order optimality yields $u^{*}=-R^{-1}\bar{G}_{t}^{\top}\,\nabla_{\mu}V$, and substitution into gives the minimized HJB: The quadratic gradient term in renders the equation nonlinear. The next subsection identifies conditions under which this term can be removed by the Cole--Hopf transformation.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-B Matching Condition and Feasibility", "weight": 1.0} -->

In the fully observed setting (Remark 1. ‣ II Problem Formulation ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems")), the Cole--Hopf transformation requires that the diffusion covariance equal a scaled version of the control authority matrix $GR^{-1}G^{\top}$. We now state the analogous requirement for the belief-mean dynamics. Given this condition, the Cole--Hopf linearization follows by the same algebraic mechanism as in the fully observed case. The non-trivial question is whether and when this condition can be satisfied in belief space; this is addressed by Proposition 3. ‣ V-B Matching Condition and Feasibility ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems") below.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption 2 (Scheduled Matching)", "weight": 1.0} -->

The belief-mean diffusion matrix $D_{t}$ and the scheduled control matrix $\bar{G}_{t}$ satisfy, for each $t\in[0,T]$, where $\lambda>0$ is the path integral temperature.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-C Cole--Hopf Linearization", "weight": 1.0} -->

Define the *desirability function* $\Psi(t,\mu):=\exp(-V(t,\mu)/\lambda)$, so that $V(t,\mu)=-\lambda\log\Psi(t,\mu)$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 4 (Risk-Sensitive Extension)", "weight": 1.0} -->

The expected cost $q(\mu,\Sigma)=\mathbb{E}[\bar{q}(x)]$ can be replaced by $q_{\mathrm{RS}}=\mathbb{E}[\bar{q}(x)]+\frac{\theta}{2}\mathrm{Var}[\bar{q}(x)]$, obtained from the cumulant expansion of the entropic risk measure. The parameter $\theta>0$ controls risk aversion, and $\theta=0$ recovers the risk-neutral cost. The PIC structure is preserved since only the running cost is modified.

<!-- chunk {"id": "body-0037", "role": "body", "section": "MPPI-Belief Algorithm", "weight": 1.0} -->

This section develops a discrete-time Monte Carlo approximation of the belief-space control law and presents the resulting MPPI-Belief algorithm.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

We evaluate on a 2D double-integrator with state $x=[p_{x},p_{y},v_{x},v_{y}]^{\top}$, control $u\in\mathbb{R}^{2}$, and position-only observations ($C=[I_{2}\;0_{2\times 2}]$). The observation noise is $\sigma_{o}(p_{x})=|p_{x}-x_{\text{light}}|/\sqrt{2}+0.1$ with $x_{\text{light}}=5$ m, producing a light region where observations are most accurate. Two obstacles at $(3,\pm 1)$ m with radius $0.65$ m form a corridor in a high-noise region; process noise is $\sigma_{w}=0.30$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

We compare MPPI-Belief with the risk-sensitive cost of Remark 4. ‣ V-C Cole–Hopf Linearization ‣ V Path Integral Control in Gaussian Belief Space ‣ Path Integral Control in Gaussian Belief Space for Partially Observed Systems") ($\theta{=}1$) against EKF-iLQG, CE-MPPI ($\theta{=}0$), and PIPF ($K{=}50$ particles, $L{=}200$ samples). All sampling-based baselines share the same cost function, temperature, and horizon, while differing primarily in planning and filtering architecture.^11^1Our PIPF uses a bootstrap particle filter and the same MPPI importance weighting as CE-MPPI, rather than the KL-optimal proposal of; thus, our implementation should be viewed as a simplified PIPF-style baseline rather than an exact reproduction.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

Table I and Fig. 1 show that MPPI-Belief is the only method achieving zero collisions over 200 trials, while the baselines incur 18--25%. The risk-sensitive belief cost couples obstacle proximity with covariance, encouraging detours through the informative region before traversing the corridor. The optimized matching residual is $\varepsilon^{*}=0.79$, indicating that useful performance is retained despite approximate matching.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

In Fig. 2, we sweep the planning obstacle penalty weight $w_{\mathrm{obs}}\in[10^{2},10^{4}]$ for each method to test whether the safety improvement is merely a tuning artifact. The results show that increasing $w_{\mathrm{obs}}$ across two orders of magnitude has little effect on the baselines, which remain between 11% and 33% collision rate, whereas MPPI-Belief drops below 1% by $w_{\mathrm{obs}}{=}500$ and reaches 0% at 2500. No baseline reaches 0% at any weight tested, indicating that collisions are driven by estimation uncertainty rather than insufficient obstacle penalty.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

Finally, we isolate the role of the risk-sensitive parameter by sweeping $\theta\in\{0,0.5,1,2,5\}$ over 200 trials per setting (detailed results omitted for brevity). At $\theta{=}0$ (expected cost only), the collision rate is 23.0% with mean clearance 0.11 m. Even moderate risk aversion ($\theta{=}0.5$) reduces collisions to 2.5% and increases clearance to 0.80 m. The best performance occurs at $\theta{=}1$, achieving 0% collisions and 0.82 m clearance with modest cost increase ($56.6$ vs. $51.3$). For $\theta\geq 2$, collision rates rise slightly (0.5--1.5%), suggesting that excessive risk aversion can induce over-conservatism. The variance penalty $(\theta/2)\mathrm{Var}[\bar{q}]$ is thus the primary driver of safe behavior, amplifying obstacle costs in high-uncertainty regions.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper studied path integral control for partially observed systems via a Gaussian belief-space approximation. We showed that the matching condition generally fails in full belief space, and characterized when it can hold in the reduced Gaussian setting. This yields a belief-space path integral formulation and the MPPI-Belief algorithm. Numerical experiments showed improved safety relative to certainty-equivalent and particle-filter-based baselines at practical computational cost. Future work will consider nonlinear observation models, non-Gaussian belief representations, and hardware validation.
