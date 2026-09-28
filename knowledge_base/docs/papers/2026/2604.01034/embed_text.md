<!-- arxiv-full-text:v1 {"arxiv_id": "2604.01034", "source": "arxiv-html"} -->

## INTRODUCTION

Control of dynamical systems under broad uncertainty remains a central challenge in modern control theory. In many applications, uncertainty arises from latent parameters in the system dynamics (i.e. mass, inertia, or geometry) that cannot be directly measured yet critically influence closed-loop performance. Classical robust control methods address this challenge by optimizing performance under worst-case parameter uncertainty, yielding performance guarantees at the expense of conservatively robust controllers. In contrast, stochastic and risk-sensitive control methods optimize expected performance subject to a prescribed distribution, but rely heavily on task-agnostic sampling methods that fail to accurately model task-relevant uncertainty in practice. Bridging this gap between robustness and control performance guarantees remains a fundamental open problem.

Distributionally Robust Control (DRO) provides a principled approach for reasoning about uncertainty by optimizing over a set of admissible probability distributions, typically defined through divergence-based ambiguity sets. While DRO provides theoretically-grounded control formulations to model uncertainty, the method relies heavily on restrictive assumptions: either the uncertainty distribution must be parametrized and estimated a-priori, or samples must be drawn from a predefined generative process. Moreover, classical DRO inherits a worst-case uncertainty design formulation that leads to overly conservative controls that subsequently degrade task performance.

Fig. 1: Autonomous Racing under Vehicle Inertial Uncertainty. Here, we apply our control framework to autonomous racing, minimizing lap time under significant uncertainty in the vehicle’s mass distribution (mass and inertia). We compare our approach to state-of-the-art baselines: Ensemble Model Predictive Control, classical Distributionally Robust Control, and nominal Model Predictive Control. Our approach quickly adapts to task-sensitive uncertainties faster than nominal baselines, enabling fast adaptation and convergence to the objective.

A guiding question is how we can relax the assumptions of DRO to avoid worst-case uncertainty modeling. Variational Inference (VI) methods have emerged as powerful tools that approximate complex probability distributions without committing to restrictive parametric families. Stein Variational Gradient Descent (SVGD), in particular, constructs a deterministic flow of particles that approximates a target distribution via functional gradient descent in a reproducing kernel Hilbert space. Unlike traditional VI, SVGD provides a nonparametric and computationally tractable mechanism to represent multimodal and task-dependent uncertainty. Despite its success in Bayesian inference and learning, its role in robust control synthesis remains largely unexplored.

Early work presented in introduced Stein Variational Inference (SVI) for jointly reasoning over controls and dynamics through brute-force parallelization, but fails to capture task-sensitivities that could be used to reduce computation. This work shows that Stein variational inference over task-sensitive parameters alone is sufficient to achieve distributional robustness within a model-predictive control paradigm under limited sensor feedback, thereby avoiding parallel inference over controls while yielding reliable, uncertainty-robust control synthesis.

The core idea is to replace static or worst-case uncertainty models with a *deterministic*, evolving set of particles that adapts to uncertainty via a *task-dependent* posterior over parameter uncertainty. Rather than optimizing over all admissible uncertainties, our method prioritizes uncertainty *most sensitive to task performance*, concentrating computation on uncertainties that most impact control. This approach leads to optimal control synthesis that is coupled and co-evolved with uncertainty propagation through a coupled, adversarial-based optimization. ^11^ 1 This is distinctly different from belief-space planning and experimental design related methods in that we never explicitly reduce uncertainty, rather just focus on task performance. Furthermore, we characterize how the induced controller is shaped by adapting over task-relevant uncertainty.

In summary, we present a recast of the robust control problem as an inference-driven process where control synthesis is actively shaped to improve decision making subject to task-sensitive uncertainties. The main contributions of this work are as follows: A non-parametric, deterministic approximation of task-dependent uncertainty in place of worst-case, conservative uncertainty design.

Derivation of theoretical guarantees for the existence, optimality, and convergence of the Stein variational approximation to the task-sensitive parameter distribution.

Demonstrations of improved performance/robustness tradeoffs of the proposed approach compared to classical and stochastic sampling methods.

## Problem Formulation

Let $x_{t}\in\mathcal{X}$ be the system state, $u_{t}\in\mathcal{U}$ be the control input $\forall t\in[0,t_{h}]$ where $t_{h}$ is the discrete planning horizon, and $\theta\in\Theta$ be the system latent parameters for a nonlinear system of evolving dynamics $x_{t+1}=f(x_{t},u_{t},\theta)$. The objective is to solve the following control problem, | | $\displaystyle\min_{x_{0:t_{h}},u_{0:t_{h}}}$ | $\displaystyle\mathcal{J}(x_{0:t_{h}},u_{0:t_{h}},\theta)=m(x_{t_{h}},u_{t_{h}},\theta)+\sum_{t=0}^{t_{h}-1}\ell(x_{t},u_{t},\theta)$ | | \(1\) | | | $\displaystyle\text{s.t.}$ | $\displaystyle x_{0}\in\mathcal{X}_{0},\;u_{t}\in\mathcal{U},\;x_{t+1}=f(x_{t},u_{t},\theta)$ | | | where $x_{0}$ are the system initial conditions, $\ell(\cdot)$ is the stage cost, and $m(\cdot)$ is the terminal cost. The above optimization is iteratively solved for a single planning cycle $t\in[0,t_{h}]$ and the optimal first control input is administered to the system in a receding-horizon manner.

### Assumption 1 (Set Compactness and Measurability)

Let $n_{x},n_{u},n_{\theta}\in\mathbb{N}$. The state, input, and parameter spaces satisfy respectively where $\mathcal{B}(\mathbb{R}^{n})$ denotes the Borel $\sigma$-algebra on $\mathbb{R}^{n}$. Moreover, $\Theta$ is nonempty and compact.

### Remark 1

The uncertainty enters the control problem through both the dynamics and the performance index. Hence, for fixed $u_{0:t_{h}-1}$, the realized trajectory and realized cost are both functions of $\theta$.

### Proposition 1 (Existence of optimal state-control trajectory)

Given a fixed $\theta\in\Theta$, let the set of feasible trajectories be $\mathcal{X}_{0}$ and $\mathcal{U}$ are compact, $f(\cdot,\cdot,\theta)$ is continuous in $(x,u)$, $\ell(\cdot,\cdot,\theta)$ and $m(\cdot,\cdot,\theta)$ are lower semicontinuous in $(x,u)$.

Then the feasible set $\mathcal{T}$ is nonempty and compact, and $\exists\tau^{*}\in\mathcal{T}$ such that

### Proof

Since $f(\cdot,\cdot,\theta)$ is continuous, induction over $t$ shows that the trajectory $x_{0:t_{h}}$ is a continuous function of $(x_{0},u_{0:t_{h}-1})$. Hence the nonempty $\mathcal{T}$ is the image of the compact set $\mathcal{X}_{0}\times\mathcal{U}^{t_{h}}$ under a continuous map. Since finite sums preserve lower semicontinuity, $\mathcal{J}(\cdot,\theta)$ is lower semicontinuous on $\mathcal{T}$, and the Weierstrass extreme value theorem yields a minimizer $\tau^{*}\in\mathcal{T}$ of $\mathcal{J}(\cdot,\theta)$. ∎Note that we do not assume $\theta$ to be known when the control is synthesized. Instead, $\theta$ is modeled as an unknown element of $\Theta$, or more generally as a random variable on $\big(\Theta,\mathcal{B}(\Theta)\big)$. When prior information is available by a prior distribution $p_{0}(\theta)$, it is encoded by a reference measure $p\in\mathcal{P}(\Theta)$, where For any admissible $(x_{0:t_{h}},u_{0:t_{h}})$, the map $\theta\mapsto\mathcal{J}(x_{0:t_{h}},u_{0:t_{h}},\theta)$ is a random cost under any measure $p\in\mathcal{P}(\Theta)$. Thus, uncertainty about $\theta$ induces uncertainty about closed loop performance.

### II-A Uncertainty-Aware Optimal Control

This paper optimizes a control sequence $u_{0:T}$ with respect to the *variability* of $\theta\mapsto\mathcal{J}(\cdot,\theta)$ over $\Theta$, leading to functionals over measures $p\in\mathcal{P}(\Theta)$ and a class of uncertainty-aware optimal control problems of the form, where $\mathcal{A}\subseteq\mathcal{P}(\Theta)$ denotes a selected family of admissible distributions over the latent parameters. The formulation above highlights that robustness is defined with respect to distributions that capture parameter uncertainty in an adversarial manner, where the objective is to minimize an upper bound over the uncertainty defined over a family of probability distributions.

The choice of selecting $\mathcal{A}$, however, remains a central challenge, as finding admissible distributions that characterize $\theta$ is difficult to obtain. In DRO theory, $\mathcal{P}$ is defined as the following ambiguity set, where $\mathbb{D}_{KL}[p\,\|\,q]:=\int_{\Theta}\log\big(\tfrac{dp}{dq}\big)\,dp$ denotes the Kullback--Leibler (KL) divergence between $p,q\in\mathcal{P}(\Theta)$ with $p$ absolutely continuous with respect to the unknown target distribution $q$ that captures the realization of the true parameter $\theta^{\ast}$. The surrogate $p$ is *KL-close* to $q$ whenever $\mathbb{D}_{KL}[p\,\|\,q]\leq\epsilon$. Since finding $\mathcal{P}$ such that element $p$ remains as KL-close to the target unknown distribution is challenging to obtain, DRO relaxes the min-max problem defined in to be the Risk-Averse Optimal Control Problem, where $\lambda\in\Lambda$ are the dual variables to. We can now show that the entropic objective above reduces to an expected-cost problem for sufficiently large $\lambda$.

### Lemma 1 (Entropic risk expansion)

Suppose $\theta\mapsto\mathcal{J}(x_{0:t_{h}},u_{0:t_{h}},\theta)$ is bounded on $\Theta$, with $\underline{J}\leq\mathcal{J}\leq\bar{J}$. Then for any $q\in\mathcal{P}(\Theta)$, where the first-order remainder is uniformly bounded as $\frac{1}{2\lambda}\mathbb{V}_{q}[\mathcal{J}]\leq\frac{(\bar{J}-\underline{J})^{2}}{8\lambda}$.

### Proof

Let $g(s):=\log\mathbb{E}_{q}[\exp(s\,\mathcal{J})]$ denote the cumulant generating function of $\mathcal{J}$ under $q$, which is finite and smooth for bounded $\mathcal{J}$, with $g=0$, $g^{\prime}=\mathbb{E}_{q}[\mathcal{J}]$, and $g^{\prime\prime}=\mathbb{V}_{q}[\mathcal{J}]$. A second-order Taylor expansion of $g$ about $s=0$ evaluated at $s=1/\lambda$ yields The uniform bound follows from Popoviciu's variance inequality, In prior work, constructing $\mathcal{P}$ requires a maximum-likelihood estimate of target $q$ and a KL-neighborhood around it, demanding parameter-space coverage and repeated system sampling that is unavailable for latent $\theta$. We instead assume minimal system feedback and shape uncertainty that is most critical to $\mathcal{J}$ via variational inference, avoiding explicitly choosing $\mathcal{P}$ entirely.

## Stein Variational Inference

Given a random variable $\theta\sim p_{0}(\theta)$ with prior law $p_{0}\in\mathcal{P}(\Theta)$, Variational Inference (VI) offers a powerful method that approximates an intractable, unknown target distribution $q$ by optimizing a surrogate $p\in\mathcal{P}(\Theta)$ chosen from a family of distributions that satisfy, through the following, where $p^{*}$ is the approximation of $q$, and $c$ is a constant that is often negligible in practice. As aforementioned, the choice of $\mathcal{P}$ remains a nontrivial challenge, and can negatively impact the performance of VI. As a solution, Stein Variational Inference, also referred to as Stein Variational Gradient Descent (SVGD), avoids the need of explicitly choosing $\mathcal{P}$ entirely. Instead, SVGD initializes a set of particles $\{\theta_{0}^{i}\}_{i=1}^{N}\sim p_{0}(\theta)$, and subsequently evolves them according to the mapping, where $\alpha$ is a step size parameter and $\phi_{p,q}^{*}(\theta_{t}^{i})$ is a smooth function that characterizes the $t^{th}$ steepest descent direction that minimizes the KL-divergence measure, and $T$ represents the total number of SVGD iterations. The gradient $\phi^{*}_{p,q}$ is the solution to the following steepest descent problem, where $\mathcal{A}_{q}(\cdot):\Xi\rightarrow\mathcal{S}_{\Xi}$ is Stein's identity computed for a universal positive definite kernel function $k:\Xi\times\Xi\rightarrow\mathbb{R}$ operating in a dense $\mathcal{H}^{d}$ in the space of continuous functions $C(\Xi,\mathbb{R}^{d})$, where $\mathcal{H}^{d}$ is the corresponding Reproducing Kernel Hilbert Space (RKHS). The closed form solution to is computed to be, where $p$ denotes the law of the current particles and $p^{\prime}$ is the tractable Boltzmann approximation to the target $q$, where $\int_{\Theta}p(\mathcal{O}|\theta)p_{0}(\theta)d\theta=\textrm{constant}$ and $\mathcal{O}$ is an observation output denoting an optimality criterion. Commonly, $\phi_{p,q}^{*}:\Theta\rightarrow\mathcal{S}_{\Theta}$ is approximated using Monte-Carlo samples over $\theta$, which are initialized at random and then updated deterministically. With sufficient samples $N$ and number of SVGD iterations, the evolved particles become a sufficient approximation of the target $q(\theta)$ and show provably strong convergence under regularity conditions.

## Parameter-induced Optimality Gap as Inference

This section outlines an approach that integrates the theoretical benefits of DRO combined with diverse, task-based parameter adaptation techniques via SVGD. We first define the Lagrangian of the optimization problem for a single planning cycle defined in as, where $\beta$ comprise the dual equality variables, $h(\cdot)$ are the equality constraints, and $x_{t}\in\mathcal{X}$ and $u_{t}\in\mathcal{U}$ are enforced.

### Assumption 2 (Lagrangian $\Theta$-Smoothness)

$\mathcal{L}$ is bounded and continuous on the compact set $\Theta$, and there exists $\bar{\epsilon}<\infty$ such that Because $\theta$ induces uncertainty about closed loop performance optimized by Lagrangian $\mathcal{L}:\mathcal{X}\times\mathcal{U}\times\Theta\rightarrow\mathbb{R}$, we define the optimality gap produced by a random variable $\theta$ as, where $\theta^{*}$ is the true parameter value. Referring back to and applying Lemma 1 ‣ II-A Uncertainty-Aware Optimal Control ‣ II Problem Formulation ‣ Stein Variational Uncertainty-Adaptive Model Predictive Control") with $\mathcal{J}$ replaced by the Lagrangian $\mathcal{L}$ in (which coincides with $\mathcal{J}$ on dynamics-consistent trajectories, since $h(\cdot)=0$), the expected Lagrangian is approximated via Monte-Carlo expectation as, where $\gamma$ is a design parameter such that $\gamma=1$ equates to the true Monte-Carlo approximation above. However, in practice, tuning $\gamma$ is desirable in order to control the trade-off between optimizing over the nominal parameters versus the variations of parameters.

Note that $\theta^{*}$ is unknown a-priori, and requires an additional approximation in order to implement. We choose the empirical posterior mean (particle mean) as a standard and consistent estimator in particle-based adaptation used in Stein-based control, which is shown to provide a stable, low-variance reference for defining the optimality gap. The optimization in is commonly used in current robust control methods, but a core challenge in implementation remains in *how the parameter samples $\{\theta^{i}\}_{i=1}^{N}$ are chosen*.

(a) Rocket example. Given its initial condition, the rocket system navigates to a landing pad safely. The top-heavy rocket system requires explicit reasoning over this uncertainty by modulating gimbal and thrust to maintain a stable configuration under uncertainty about its mass, inertia, and center of mass location.

(b) Cartpole example. A cartpole system achieves a swingup task from a downward-stable state. The system exploits oscillatory motions until SVGD converges to an approximate posterior, then robustly stabilizes the pole to the goal state under uncertainty over pole mass and length.

Fig. 2: Example Experimental Outcomes from Our Method. We demonstrate the efficacy of our approach on a two-dimensional rocket landing and cartpole swingup control tasks.

### IV-A Stein Variational Uncertainty Adaptation

We outline a principled, non-parametric approach that guides parameter particles $\theta^{i}$ towards task-critical uncertainties by contextualizing SVGD as an inference problem over uncertain parameters. We define the log posterior distribution given a parameter prior $p_{0}(\theta)$ as a Boltzmann posterior, where $p(\mathcal{O}|\theta)$ is the observation likelihood via an exponentiated optimality gap $p(\mathcal{O}\mid\theta)\propto\exp(\delta\mathcal{L}(x_{0:t_{h}},u_{0:t_{h}},\theta))$, commonly used in relevant Stein literature, in which we explicitly characterize model optimality variations induced by uncertain parameters that directly impacts the Stein flow. Also note that $z$ is a constant that is often ignored in the optimization. We utilize this posterior approximation to the target $q$ by evolving initialized Stein particles $\{\theta^{i}\}_{i=1}^{N}$ by computing steepest descent $\phi^{*}$ using Stein's identity given prior $p_{0}(\theta)$, where $k:\Theta\times\Theta\rightarrow\mathbb{R}$ is a universal positive definite kernel. Our approach evaluates parameter sensitivity through $t^{th}$ evolving estimators $\{\theta_{t}^{i}\}_{i=1}^{N}$, capturing the task-relevant deviations $\delta\mathcal{L}(x_{0:t_{h}},u_{0:t_{h}},\theta)$ and enabling control synthesis that explicitly counteracts the induced optimality gap. Note that Algorithm 1 performs a single SVGD update per planning cycle, so the Stein iteration index coincides with the time step $t$ and the total number of SVGD iterations equals the task duration $T$.

### Remark 2 (Consistency with the DRO relaxation)

By the Donsker-Varadhan variational formula, for any bounded $\mathcal{L}$ and any reference measure $p_{0}\in\mathcal{P}(\Theta)$, where the supremum is attained at $\tfrac{dp^{\star}}{dp_{0}}(\theta)\propto\exp\big(\mathcal{L}(\tau,\theta)/\lambda\big)$. The left-hand side of (25 ‣ IV-A Stein Variational Uncertainty Adaptation ‣ IV Parameter-induced Optimality Gap as Inference ‣ Stein Variational Uncertainty-Adaptive Model Predictive Control")) is, up to the constant $\lambda\epsilon$, the entropic objective of, while the right-hand side is the Lagrangian form of the inner adversarial maximization. Since $\delta\mathcal{L}(\tau,\theta)$ and $\mathcal{L}(\tau,\theta)$ differ by a $\theta$-independent constant, coincides with the least-favorable distribution $p^{\star}$ at $\lambda=1$. Coefficient $\lambda$ merely scales the exponent in by $1/\lambda$. The Stein flow therefore targets precisely the maximizer of the KL-regularized distributionally robust objective by transporting particles toward highly sensitive regions of the task-based posterior as the ensemble-based controller seeks the best response against the particles via.

1: planning horizon th, initial trajectory (x0: th, u0: th) parameter prior p0(θ), N total number of particles, SVGD step size α, design parameter γ, initial particles {θ0i}i = 1N ∼ p0(θ), dynamics f(xt, ut, θ), total time duration T. 4: $\tau^{*}\leftarrow\textrm{eq:exp_approx}$ 5: Apply first control u* via MPC Algorithm 1 Stein Variational Uncertainty-Adaptive MPC

### Lemma 2 (Continuity of the Stein potential)

Given a feasible state-control pair $(x_{0:t_{h}},u_{0:t_{h}})$, let Suppose Assumption 2 ‣ IV Parameter-induced Optimality Gap as Inference ‣ Stein Variational Uncertainty-Adaptive Model Predictive Control") holds and $p_{0}(\theta)$ is strictly positive and continuous on $\Theta$. Then $V$ is continuous on $\Theta$.

### Proof

Since $\theta^{\ast}$ is fixed, the scalar is constant with respect to $\theta$. Therefore, Because $p_{0}$ is strictly positive and continuous on $\Theta$, the function $\log p_{0}(\theta)$ is continuous on $\Theta$. Therefore, $V(\theta)=-\delta\mathcal{L}(x_{0:t_{h}},u_{0:t_{h}},\theta)-\log p_{0}(\theta)$ is the sum of two continuous functions on $\Theta$, and is thus continuous. ∎

### Theorem 1 (Posterior Convergence in $\Theta$ )

Given an initial prior $p_{0}(\theta)$, let $V(\theta)=-\delta\mathcal{L}(x_{0:t_{h}},u_{0:t_{h}},\theta)-\log p_{0}(\theta)$ be the continuous (hence lower semi-continuous), task-dependent value function on the compact space $\Theta$, $k(\cdot,\theta)$ is a universal positive definite kernel in $\Theta$, and let $KSD_{p^{\prime}}(\mu_{i})=\|\phi^{*}(\mu_{i})\|_{\mathcal{H}^{\Theta}}^{2}$ be the kernel Stein discrepancy over the posterior $p^{\prime}$. Then, $\exists\kappa>0$ such that, where $c_{\kappa}$ is a $\kappa$-parameterized term \[8, Corollary 6\].

Thus, for sufficient $T$ number of SVGD iterations, the approximated posterior $p^{\prime}$ sufficiently represents the intractable target posterior $q$ which we show in Section V.

### Theorem 2 (Convergence of optimality gap)

Let $q\in\mathcal{P}(\Theta)$ denote the intractable target posterior over parameters, and let $\{p_{T}^{\prime}\}_{T>0}\subset\mathcal{P}(\Theta)$ denote the sequence of empirical Stein particle measures (posteriors) generated by the SVGD updates for $T$ iterations . Given Assumption 1 ‣ II Problem Formulation ‣ Stein Variational Uncertainty-Adaptive Model Predictive Control") holds true, the conditions in Theorem 1 ‣ Proof: ‣ IV-A Stein Variational Uncertainty Adaptation ‣ IV Parameter-induced Optimality Gap as Inference ‣ Stein Variational Uncertainty-Adaptive Model Predictive Control") are satisfied, and the mapping $\theta\mapsto\mathcal{L}(x_{0:t_{h}},u_{0:t_{h}},\theta)$ is bounded and continuous for fixed state control pairs $(x_{0:t_{h}},u_{0:t_{h}})$. Then for any $\varepsilon>0$, $\exists T\in\mathbb{Z}_{+}$ such that,

### Proof

Since the Stein kernel $k$ is universal on compact $\Theta$, Theorem 1 ‣ Proof: ‣ IV-A Stein Variational Uncertainty Adaptation ‣ IV Parameter-induced Optimality Gap as Inference ‣ Stein Variational Uncertainty-Adaptive Model Predictive Control") shows convergence on the associated empirical measures, For a fixed trajectory $(x_{0:t_{h}},u_{0:t_{h}})$, we define the following function, By Assumption 2 ‣ IV Parameter-induced Optimality Gap as Inference ‣ Stein Variational Uncertainty-Adaptive Model Predictive Control"), $f$ is bounded and continuous on $\Theta$. Therefore, invoking Portmanteau Theorem, By the definition of convergence of a sequence, for any $\varepsilon>0$, $\exists T\in\mathbb{Z}_{+}$, thus completing the proof. ∎

### Proposition 2 (Performance per-cycle upper bound)

Let $\gamma\in$ , and let Assumptions 1 ‣ II Problem Formulation ‣ Stein Variational Uncertainty-Adaptive Model Predictive Control") and 2 ‣ IV Parameter-induced Optimality Gap as Inference ‣ Stein Variational Uncertainty-Adaptive Model Predictive Control") hold with $\Theta$ convex, so that $\mathcal{L}(\tau,\cdot)$ is $\bar{\epsilon}$-Lipschitz on $\Theta$ for every feasible $\tau$. Let $p^{\prime}$ denote the empirical Stein particle measure with mean $\bar{\theta}$ as , let $\tau^{\star}$ denote the minimizer of, and let $\hat{\tau}(\hat{\theta})$ denote the certainty-equivalent MPC solution for an arbitrary fixed $\hat{\theta}\in\Theta$ over the same feasible set. Then,

### Proof

The objective of can be rewritten as By the Lipschitz property, $|\mathcal{L}(\tau,\theta^{i})-\mathcal{L}(\tau,\theta^{*})|\leq\bar{\epsilon}\|\theta^{i}-\theta^{*}\|$, and by Jensen's inequality $\|\bar{\theta}-\theta^{*}\|\leq\rho$. Hence, for feasible $\tau$ and $\gamma\in$. Since $\hat{\tau}(\hat{\theta})$ is feasible and $\tau^{\star}$ minimizes $F$,

### Remark 3

Per planning cycle, the controller performs no worse than certainty-equivalent MPC with any, possibly incorrect, $\hat{\theta}$, up to slack $2\bar{\epsilon}\rho$ governed by posterior concentration around $\theta^{*}$; taking $\hat{\theta}=\theta^{*}$ shows the cost approaches that of true-parameter MPC as $\rho\to 0$. The bound holds at every cycle, hence recursively along the receding-horizon execution.

TABLE I: Performance comparison on cartpole swing-up and rocket landing tasks. Our method consistently achieves the highest success rates on both problems, while also exhibiting substantially faster convergence on the cartpole task ( ≈ 2× relative speedup), at the occasional slight cost of increased completion time.

## Results

We evaluate the proposed controller on three nonlinear control problems with latent parameters under broad uncertainty with distinct tasks: Cartpole Swingup. Swing the pole upright from a downward-oriented initial state.

Rocket Landing. Navigate a 2D rocket to a landing pad.

Autonomous Racing. Complete a lap of a 2D track as quickly as possible.

All control problems are given the following general stage and terminal cost structure based, where $\mathbf{Q},\mathbf{R},\mathbf{Q_{f}}\succeq 0$, and $r(\cdot)$ is a problem-specific additional terminal cost. Note $r(\cdot)=0$ unless otherwise specified.

TABLE II: Implementation details. All ensemble-based experiments use N = 5 particles, γ = 0.5, and uniform priors {θi}i = 1N ∼ 𝒰(θmin, θmax).

We compare our Stein Variational uncertainty-adaptive Model Predictive Control to the following three comparative baselines: Ensemble MPC (EMPPI). Samples control sequences and propagates them across a parameter ensemble via task-agnostic (uniform random) sampling.

Standard DRO. Optimizes the ambiguity-set objective against a worst-case parameter distribution.

Standard MPC. Solves the finite-horizon problem with the nominal parameter, ignoring parametric uncertainty.

Each example is evaluated over $32$ trials with different seeds initializing the particles $\{\theta^{i}\}_{i=1}^{N}\sim\mathcal{U}(\theta_{\min},\theta_{\max})$. Unless otherwise stated, we use the RBF kernel $k(\theta,\hat{\theta})=\exp(-\|\theta-\hat{\theta}\|^{2}/h)$ with bandwidth $h=1$.

*Computational cost.* Per planning cycle, our method requires $N$ parallel trajectory rollouts to evaluate $\delta\mathcal{L}(\tau,\theta^{i})$ per SVGD update, each requiring $\mathcal{O}(N^{2}n_{\theta})$ kernel evaluations, where $n_{\theta}=|\theta|$, for a total per-cycle complexity of $\mathcal{O}(Nt_{h}+N^{2}n_{\theta})$, compared with $\mathcal{O}(t_{h})$ for nominal MPC and $\mathcal{O}(Nt_{h})$ for EMPPI. The rollouts dominate and parallelize identically to EMPPI's ensemble, so the SVGD loop adds only marginal overhead for small $N$. Measured per-cycle solve times are reported in Table III, and all methods remain within the receding-horizon replanning budget.

TABLE III: Per-cycle solve times (ms, mean ± std across all planning cycles of the 32 trials per task) measured on the GPU (NVIDIA GeForce RTX 3080).

### V-A Cartpole Swingup

### V-A1 Problem Formulation

Let $\mathbf{x^{cp}}_{t}=[x_{t},\varphi_{t},v_{t},\omega_{t}]^{\top}\in\mathbb{R}^{4}$ denote the cart position, the pole angle measured from the downward vertical, and their respective velocities, with force input $\mathbf{u^{cp}}_{t}\in\mathbb{R}$ along the translational axis. Starting from rest with the pole hanging down, the objective is to swing the pole upright. The uncertain parameters are the pole mass $m_{\textrm{pole}}\in\mathbb{R}$ and length $\ell_{\textrm{pole}}\in\mathbb{R}$, and all numerical parameters are listed in Table II.

### V-A2 Results

Fig. 2b shows an example trajectory of a cartpole exploiting oscillatory motions until SVGD converges to an approximate posterior of the target to robustly stabilize the pole to the goal state. Results across all $32$ trials are reported in Table I.

Our method achieves $\approx 2\times$ faster completion with consistently lower variance across all parameter initializations. EMPPI's *task-agnostic* sampling drives inefficient exploration, while DRO enforces uniformly *worst-case* robustness irrespective of task relevance. Stein-based posterior updates instead reshape the parameter distribution via the optimality gap, suppressing task-irrelevant parameter variations and amplifying performance-critical ones, eliminating unnecessary exploration.

Fig. 3: Autonomous Racing Lap Time Completions. We report track completion over time for the autonomous racing task under uncertainty in vehicle mass and inertia. We achieve faster and more consistent progress by reasoning over task-sensitive regions of the parameter posterior that most affect control performance.

### V-B 2D Rocket Landing

### V-B1 Problem Formulation

Let $\mathbf{x^{r}}_{t}\in\mathcal{X}_{t}^{\textrm{rocket}}=\mathbb{R}^{6}$ be the rocket system state, defined as $\mathbf{x^{r}}_{t}=[x_{t},y_{t},\varphi_{t},\dot{x}_{t},\dot{y}_{t},\omega_{t}]^{\top}$, where $x_{t}$ and $y_{t}$ are the translational world coordinates of the system, $\varphi_{t}$ is the measured rocket angle with respect to the world vertical axis (with world frame positioned at '\*' on the landing pad shown in Fig. 2a), and $\dot{x}_{t}$, $\dot{y}_{t}$, and $\omega_{t}$ are translational and angular velocities, respectively. Let $\mathbf{u^{r}}_{t}\in\mathcal{U}_{\textrm{rocket}}=\mathbb{R}^{2}$ be the thrust and gimbal control of the rocket, where the thrust is exerted along the gimbal axis. The goal state is placed a lateral distance from the rocket, so the system cannot trivially descend vertically and must instead execute careful lateral motion to land safely. The uncertain parameters are the rocket mass $m_{\textrm{rocket}}$, inertia $I_{\textrm{rocket}}$, and center-of-mass location $\ell_{\mathrm{COM}}$ measured along the body axis, with $\theta_{\max,3}=h_{\mathrm{rocket}}=1.0$ the rocket height; all numerical parameters are listed in Table II.

### V-B2 Results

Fig. 2a shows an example trajectory, where the task succeeds only if the rocket lands within a safe tolerance of the pad with its body axis upright. Since the goal is a lateral distance from the rocket, the system must move laterally without tipping the high-positioned center of mass, and the resulting behavior is a gradual gimbal-thrust forcing that translates the rocket without capsizing it. Results across $32$ trials are reported in Table I.

TABLE IV: Kernel Ablation Study. Comparison of our method for the rocket landing system using RBF, IMQ, and k(⋅, θ̂) = 1 kernels. The IMQ kernel achieves the highest success rate with slightly slower completion due to the kernel’s prevention of mode collapse and preservation of particle diversity for more reliable inference.

While EMPPI attains the lowest average completion time, it also has the lowest success rate among all methods. Our method achieves the highest reliability at near-negligible added time. By 'probing' the rocket through subtle tilts that stop short of tipping, our approach generates the exploration SVGD needs to approximate the target posterior via task-sensitive inference.

### V-C Autonomous Racing

### V-C1 Problem Formulation

Let $\mathbf{x^{c}}_{t}\in\mathcal{X}_{t}^{\textrm{car}}=\mathbb{R}^{5}$ be the vehicle system state, defined as $\mathbf{x^{c}}_{t}=[x_{t},y_{t},\varphi_{t},v_{t},\omega_{t}]^{\top}$, where $x_{t}$ and $y_{t}$ are the translational world coordinates of the system (with world frame oriented at the center of the racetrack), $\varphi_{t}$ is the measured vehicle angle with respect to the body forward axis, $v_{t}$ is the forward directional velocity with respect to the body axis, and $\omega_{t}$is the angular velocities, respectively. Let $\mathbf{u^{c}}_{t}\in\mathcal{U}_{\textrm{car}}=\mathbb{R}^{2}$ be the throttle and steering control of the vehicle. We define the dimensions of the racetrack as a track length of $5.0$ and a track radius of $2.0$. We initialize the vehicle state in world coordinates at the starting line of the racetrack, $\mathbf{x^{c}}_{0}=[-2.5,-2.0,0.0,0.0,0.0]^{\top}$, with the objective of completing a single lap along the track as quickly as possible, where $\mathbf{x^{c}}_{\textrm{des}}$ is a reference spline along the central spline of the racetrack. To promote progress along the track, we add the terminal reward where $[\cdot]_{j}$ denotes the $j$-th entry, and $\varepsilon_{r}=0.001$ avoids division by zero. The uncertain parameters are the vehicle mass $m_{\textrm{car}}$ and inertia $I_{\textrm{car}}$. Additional details are listed in Table II.

### V-C2 Results

Fig. 1 shows example trajectories of our controller adapting to the target parameter posterior to produce dynamically consistent trajectories that track the reference spline, maintaining high-speed traversal with minimal corrective action and achieving the fastest lap time of $4.408$ s. As shown in Fig. 3, our method completes the track faster and with reduced variance relative to EMPPI and MPC, while standard DRO fails to reliably complete the track. EMPPI's task-agnostic sampling induces redundant exploration, nominal MPC neglects parameter uncertainty, and DRO's worst-case design yields overly conservative, unstable behavior. Adapting to the task-dependent posterior via the optimality gap instead yields trajectories that are simultaneously aggressive, stable, and robust, achieving faster laps.

### V-D Kernel Ablation Study

To demonstrate kernel sensitivity to task performance, Table IV evaluates our approach on the rocket landing problem over three kernels: the RBF kernel used above, the Inverse Multi-Quadratic (IMQ) kernel, $k(\theta,\hat{\theta})=(\psi^{2}+\|\theta-\hat{\theta}\|^{2})^{-\zeta}$ with bandwidth $\psi$ and decay factor $\zeta$, and the constant kernel $k(\cdot,\hat{\theta})=1$, which reduces SVGD to parallel gradient descent over the parameters. The IMQ kernel yields the most reliable control at the cost of slightly longer completion times. RBF's exponential decay limits long-range particle interactions and can induce clustering or degeneracy, whereas IMQ's long-range repulsion preserves particle diversity and prevents mode collapse. We also found that overly large step sizes $\alpha\geq 0.1$ destabilize the particle flow.

Although our experiments involve $n_{\theta}\leq 3$ uncertain parameters, the per-iteration cost of SVGD scales linearly in $n_{\theta}$ and quadratically in $N$, and the principal high-dimensional failure mode (particle collapse under RBF kernels) is mitigated by IMQ's repulsion (Table IV) and further alleviated by structured or message-passing Stein updates, suggesting a viable path toward higher-dimensional parameter spaces.

## Conclusions

We introduce a Stein variational uncertainty-adaptive model predictive controller for nonlinear systems with latent parameter uncertainty. By constructing a task-dependent posterior and coupling Stein variational inference with control synthesis, we compute task-sensitive robust controllers without the conservatism of worst-case uncertainty design, achieving improved performance and robustness to uncertainty over task-agnostic sampling and overly conservative classical approaches.
