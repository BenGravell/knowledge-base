## Introduction

Optimal control problems play a fundamental role in diverse domains of engineering and science, with applications ranging from robotics and autonomous systems to economic systems. The objective is typically to design a feedback policy that minimizes a long-term cost while satisfying the dynamics of the underlying system.

Policy gradient methods optimize parameterized policies via estimated performance gradients and scale to continuous, high-dimensional action spaces. Conventional policy gradient methods typically use first-order optimization, which yields linear convergence and sensitivity to step size choices under ill-conditioning. Incorporating curvature via the performance Hessian can accelerate convergence to superlinear or quadratic rates. In reinforcement learning, this idea appears in natural policy gradients, trust-region methods, and quasi-Newton policy gradients.

A natural next step is to employ exact Newton methods that use the full Hessian of the performance function. However, computing the exact Hessian is typically challenging. It involves not only local curvature of the action-value function but also sensitivity of state distributions to the policy parameters. This distributional term couples the policy with the dynamics, and evaluating it requires differentiating through the transition kernel and the value function, which can be computationally expensive in general settings.

The linear quadratic regulator (LQR) provides a fundamental and analytically tractable setting for studying reinforcement learning algorithms. In this model, the dynamics are linear and the cost is quadratic, which ensures that the optimal policy is a linear state feedback. Crucially, in the LQR framework many quantities of interest, such as the value function, policy gradient, and even higher-order derivatives, admit closed-form expressions. This analytical structure makes it possible to compute not only the Gauss--Newton approximation but also the exact performance Hessian explicitly, thereby enabling efficient implementation of Newton-type methods that would be prohibitively costly in general reinforcement learning problems.

In this paper, we develop a second-order policy gradient framework for the LQR with known system matrices. We build on the recently developed performance Hessian theorem in Kordabad et al., formulated for general systems, and specialize it to the discounted LQR setting. This enables us to derive explicit closed-form expressions for the exact Hessian of the performance function. Moreover, we show that the approximate Hessian resulting from this formulation coincides with the Gauss--Newton structure studied in the literature. These closed-form characterizations provide curvature-aware updates that can be computed efficiently in LQR.

Contributions. The main contributions of this paper are threefold: i) we prove that the Gauss--Newton (approximate) Hessian obtained from the general decomposition coincides with the classical LQR Gauss--Newton form; ii) we derive an explicit closed-form for the exact performance Hessian in discounted LQR under mild regularity assumptions, making exact Newton updates practical; and iii) we demonstrate on benchmarks that these second-order methods improve the convergence rate and stability over first-order policy gradient.

Outline. The paper is organized as follows: Section 2 introduces the discounted LQR setup, notation, and the recent second-order policy gradient theorem we build upon. Section 3 derives closed-form expressions for the policy gradient, the Gauss--Newton Hessian, and the exact Hessian in the LQR setting. Section 4 presents a scalar analytical example and numerical experiments illustrating the convergence properties of the proposed methods. Finally, Section 5 concludes and outlines directions for future work.

Notation. We denote by $\mathbb{N}$, ${\mathbb{N}}_{\geq 0}$, and $\mathbb{R}$ the sets of positive integers, non-negative integers, and real numbers, respectively. For a symmetric matrix $A$, $A \succeq 0$ (resp. $A \succ 0$) indicates positive semidefiniteness (resp. definiteness). We write $I_{m}$ for the $m \times m$ identity matrix. The normal vector to a set $\Omega \subseteq {\mathbb{R}}^{n}$ at $x \in {\partial\Omega}$ is denoted by ${\mathbf{n}}{(x)}$. The Frobenius and induced-2 norms are denoted by $\parallel \cdot \parallel_{F}$ and $\parallel \cdot \parallel$, respectively. For $X \in {\mathbb{R}}^{m \times n}$, we define ${{vec}{(X)}} ≔ {\lbrack X_{1}^{\mathsf{T}},\ldots,X_{n}^{\mathsf{T}}\rbrack}^{\mathsf{T}}$, where $X_{i}$ is the $i$-th column of matrix $X$. $\rho{(X)}$ denotes the spectral radius of $X$. The Kronecker product is denoted by $\otimes$, where for $A \in {\mathbb{R}}^{m \times n}$ and $B \in {\mathbb{R}}^{p \times q}$ the matrix ${A \otimes B} \in {\mathbb{R}}^{{{mp} \times n}q}$ is defined entrywise by ${({A \otimes B})}_{{{{({i - 1})}p} + r},{{{({j - 1})}q} + s}} = {a_{ij}b_{rs}}$. The commutation matrix $K_{mn} \in {\mathbb{R}}^{{{mn} \times m}n}$ admits the explicit representation

where $e_{m,i} \in {\mathbb{R}}^{m}$ and $e_{n,j} \in {\mathbb{R}}^{n}$ denote the $i$-th and $j$-th standard basis vectors, respectively (see e.g., Magnus and Neudecker ).

## Preliminaries and Background

In this paper, we consider discrete-time stochastic linear systems described by

where $s_{k} \in {\mathbb{R}}^{n}$ denotes the system state at time step $k$, $a_{k} \in {\mathbb{R}}^{m}$ is the control input and $A \in {\mathbb{R}}^{n \times n}$, $B \in {\mathbb{R}}^{n \times m}$ are fixed known system matrices. The sequence ${\{ w_{k}\}}_{k = 0}^{\infty}$ represents independent and identically distributed (i.i.d.) random variables from a fixed distribution $w_{k} \sim {p_{w}{( \cdot )}}$ with zero mean and fixed covariance $\Sigma_{w}$, i.e., ${{\mathbb{E}}{\lbrack w_{k}\rbrack}} = 0$ and ${{\mathbb{E}}{\lbrack{w_{k}w_{k}^{\mathsf{T}}}\rbrack}} = \Sigma_{w}$, whose support is contained in a known set $\mathcal{W} \subseteq {\mathbb{R}}^{n}$. The initial state $s_{0}$ is drawn from a known distribution $\rho_{0}$ with ${{\mathbb{E}}{\lbrack{s_{0}s_{0}^{\mathsf{T}}}\rbrack}} = \Sigma_{0}$.

In reinforcement learning, the dynamics are commonly represented by a transition kernel $p:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m} \times {\mathbb{R}}^{n}}\rightarrow{\lbrack 0,1\rbrack}}$. In particular, $p{(\left. s^{\prime} \middle| {s,a} \right.)}$ denotes the conditional distribution of the successor state $s^{\prime}$ when a control input $a$ is applied to the system at state $s$. For the linear system , this can be evaluated as follows:

where $\delta{( \cdot )}$ denotes the Dirac measure. The stage-wise cost $\ell:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}}$ at a given state-input pair $(s,a)$ is given by the following quadratic function:

where $Q \succeq 0$ and $R \succ 0$. A deterministic policy $\pi:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$ maps each state $s$ to an input $a$. We consider a family of parametrized policies $\pi_{\theta}$. For the linear system with quadratic cost, it is well-known that a linear state feedback policy of the form

can be optimal for a cumulative stage-wise cost for a suitable choice of $K$. We parameterize the policy by $\theta ≔ {{vec}{(K)}}$.

The value function $V_{\theta}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ corresponding to the linear policy at a given state $s$ is defined as the expectation of discounted infinite-horizon sum of the stage costs $\ell{(s_{k},a_{k})}$ under this policy, starting from the initial state $s_{0} = s$, i.e.,

where $\gamma \in {}$ is the discount factor. The expectation ${\mathbb{E}}_{\tau_{\theta}}{\lbrack \cdot \rbrack}$ is taken over the state-action trajectory generated by the underlying system dynamics, and the policy. The action-value function $Q_{\theta}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}}$ is also defined using the Bellman equation as

In the following, we introduce stabilization notions for the described discounted LQR problem that enable us to provide well-defined value functions for a given linear control policy.

### Definition 1 (Stabilization notions)

For the linear system, the linear policy is *$\gamma$-stabilizing* if ${\rho{({\sqrt{\gamma}A_{\theta}})}} < 1$, where $A_{\theta} ≔ {A - {BK}}$ is the closed-loop matrix. Moreover, the pair $(A,B)$ is *$\gamma$-stabilizable* if there exists a $\gamma$-stabilizing policy in the form of ${\pi_{\theta}{(s)}} = {- {Ks}}$.

Note that if a policy is $\gamma$-stabilizing, then it is also $\gamma_{0}$-stabilizing for all $\gamma_{0} \leq \gamma$, while the reverse may not hold. Moreover, any policy can be $\gamma$-stabilizing for sufficiently small $\gamma$. Therefore, requiring a policy to be $\gamma$-stabilizing is a more relaxed condition than requiring it to be $1$-stabilizing, which corresponds to the classical notion of stability without a discount factor. Introducing a proper discount factor thus relaxes the classical stability requirement.

Now we provide a lemma that gives explicit expressions for the value functions of LQR in the discounted setting.

### Lemma 1

For the linear system with quadratic stage cost, the value function $V_{\theta}$ and action-value function $Q_{\theta}$ corresponding to a $\gamma$-stabilizing linear policy ${\pi_{\theta}{(s)}} = {- {Ks}}$ are obtained as follows:

$V_{\theta}{(s)}$ ${= {{s^{\mathsf{T}}P_{\theta}s} + q_{\theta}}},$ (5a)
$Q_{\theta}{(s,a)}$ $= {{s^{\mathsf{T}}\left( {Q + {\gammaA^{\mathsf{T}}P_{\theta}A}} \right)s} + {2\gammas^{\mathsf{T}}A^{\mathsf{T}}P_{\theta}Ba}}$
${{+ {a^{\mathsf{T}}\left( {R + {\gammaB^{\mathsf{T}}P_{\theta}B}} \right)a}} + q_{\theta}}.$ (5b)

$P_{\theta}$ ${= {Q + {K^{\mathsf{T}}RK} + {\gammaA_{\theta}^{\mathsf{T}}P_{\theta}A_{\theta}}}},$ (6a)
$q_{\theta}$ ${= {\frac{\gamma}{1 - \gamma}{{tr}{({P_{\theta}\Sigma_{w}})}}}}.$ (6b)

The result for (5a) and (5b) follows from the discounted Bellman equation by adapting the classical undiscounted LQR derivations to the discounted setting. In infinite-horizon stochastic LQR with additive noise, a finite value requires $\gamma < 1$, since (6b) diverges at $\gamma = 1$.

The performance (or objective) function $J{(\theta)}$ for policy parameter $\theta$ is defined as the expected value of the value function $V_{\theta}$ under the initial state distribution $\rho_{0}$, i.e.,

The optimal value function and the optimal parameter vector are defined as follows:

Under the standard assumption that $(A,B)$ is $\gamma$-stabilizable in Definition 1 ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator"), there exists an optimal policy of the form. The optimal linear feedback gain is

see, e.g., Anderson and Moore; Bertsekas; Tedrake. The corresponding optimal value function is ${V^{\star}{(s)}} = {{s^{\mathsf{T}}P^{\star}s} + q^{\star}}$, where $P^{\star}$ and $q^{\star}$ are obtained by substituting $K = K^{\star}$ into (6a) and (6b).

At first sight, appears to resolve the optimal control problem, but it is an implicit characterization: it depends on $P^{\star}$, the solution of the discounted Lyapunov equation (6a). Thus, computing $K^{\star}$ still requires solving that matrix equation. Even with known $(A,B,Q,R)$, direct policy optimization is meaningful; as $J{(\theta)}$ is nonconvex and finite only on the stabilizing set, yet it satisfies a global convergence of first-order methods under suitable step sizes.

These considerations motivate preconditioned, gradient-based policy optimization. A generic update is

where $P_{k} \succ 0$ is a preconditioner and $\alpha_{k} > 0$ is a step size. Standard choices are: $P_{k} = I$, the common first-order policy gradient method; $P_{k} = F_{k}$, where $F_{k}$ is the Fisher information matrix, the natural gradient; and $P_{k} = {{\nabla_{\theta}^{2}J}{(\theta_{k})}}$, Newton's method. Because exact Hessians are expensive and often nontrivial in RL, one often uses $P_{k} = H_{k}$ with a tractable surrogate $H_{k} \approx {{\nabla_{\theta}^{2}J}{(\theta_{k})}}$ (e.g., Gauss--Newton). Under standard smoothness and stabilizability assumptions, such quasi-Newton choices retain strong local convergence while avoiding full second-order computation cost.

We next recall the deterministic policy gradient theorem and its Hessian extension. The following assumptions ensure that the performance function $J{(\theta)}$ is twice differentiable.

### Assumption 1 (Regularity)

The maps $p{(\left. s^{\prime} \middle| {s,a} \right.)}$, $\pi_{\theta}{(s)}$, $\ell{(s,a)}$, $\rho_{0}{(s)}$ and the derivatives ${\nabla_{a}p}{(\left. s^{\prime} \middle| {s,a} \right.)}$, ${\nabla_{\theta}\pi_{\theta}}{(s)}$, ${\nabla_{a}\ell}{(s,a)}$, ${\nabla_{a}^{2}p}{(\left. s^{\prime} \middle| {s,a} \right.)}$, ${\nabla_{\theta}^{2}\pi_{\theta}}{(s)}$, ${\nabla_{a}^{2}\ell}{(s,a)}$ are continuous in their arguments. $\rho_{0}$ and $p$ are uniformly bounded, and $\nabla_{a}\ell$, $\nabla_{a}p$, $\nabla_{a}^{2}p$, $\nabla_{a}^{2}\ell$ are uniformly bounded for some constants.

One can verify that for discounted LQR with dynamics, cost, and linear policy, the regularity conditions assumptions in Assumption 1 ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator") hold automatically. We next state the policy-gradient theorem and the associated Hessian decomposition.

### Theorem 1 (Policy Gradient and Hessian)

For dynamics with transition kernel and under Assumption 1 ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator"), the policy gradient and Hessian admit the following expressions:

${\nabla_{\theta}J}{(\theta)}$ ${= {{\mathbb{E}}_{\tau_{\theta}}\left\lbrack \left. {{\nabla_{\theta}\pi_{\theta}}{(s)}{\nabla_{a}Q_{\theta}}{(s,a)}} \right|_{a = {\pi_{\theta}{(s)}}} \right\rbrack}},$ (10a)
${\nabla_{\theta}^{2}J}{(\theta)}$ ${= {{H{(\theta)}} + {\gamma\Lambda{(\theta)}}}},$ (10b)

$H{(\theta)} ≔ {\mathbb{E}}_{\tau_{\theta}}\lbrack$ $\left. {{{{\nabla_{\theta}^{2}\pi_{\theta}}{(s)}} \otimes {\nabla_{a}Q_{\theta}}}{(s,a)}} \right|_{a = {\pi_{\theta}{(s)}}} +$
$\left. \nabla_{\theta}\pi_{\theta}{(s)}\nabla_{a}^{2}Q_{\theta}{(s,a)} \middle| {}_{a = {\pi_{\theta}{(s)}}}\nabla_{\theta}\pi_{\theta}{(s)}^{\mathsf{T}} \right\rbrack,$ (11a)
$\Lambda{(\theta)} ≔ {\mathbb{E}}_{\tau_{\theta}}\lbrack$ ${\int{{\nabla_{\theta}p}{(\left. s^{\prime} \middle| {s,{\pi_{\theta}{(s)}}} \right.)}{\nabla_{\theta}V_{\theta}}{(s^{\prime})}^{\mathsf{T}}{ds^{\prime}}}} +$
$\left. \int\nabla_{\theta}V_{\theta}{(s^{\prime})}\nabla_{\theta}p{(s^{\prime}|s,\pi_{\theta}{(s)})}^{\mathsf{T}}ds^{\prime} \right\rbrack.$ (11b)

Under Assumption 1 ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator"), the deterministic policy gradient theorem, (10a ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")) holds. Differentiating (10a ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")) yields (10b ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")) together with (11a ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator"))--(11b ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")); see Kordabad et al. for the derivation. $\blacksquare$

Note that Theorem 1 ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator") applies to general dynamics. The performance Hessian decomposes as (10b ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")), where $H{(\theta)}$ is a tractable curvature term and $\Lambda{(\theta)}$ captures distributional effects. The surrogate $H{(\theta)}$ is readily computable and is exact at the optimum, i.e., ${H{(\theta^{\star})}} = {{\nabla_{\theta}^{2}J}{(\theta^{\star})}}$ (see Theorem 3 in Kordabad et al. ), which justifies Gauss--Newton updates. In contrast, $\Lambda{(\theta)}$ is typically costly to evaluate because it depends on the transition kernel.

## Gradient and Hessian for LQR

A central contribution of this work is the evaluation of the general policy Hessian framework stated in Theorem 1 ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator") for the LQR problem. Leveraging the analytical structure of the LQR, we obtain an explicit, structured, and computationally tractable representation of the second-order policy gradient. This explicit characterization goes beyond the abstract formulations available in the general setting and provides novel theoretical insights into the geometry of the policy optimization landscape. We first state the differential identities for $Q_{\theta}$ and $\pi_{\theta}$ required in Theorem 1 ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator"). For $Q_{\theta}$,

${{{\nabla_{a}Q_{\theta}}{(s,a)}} = {{2\left( {R + {\gammaB^{\mathsf{T}}P_{\theta}B}} \right)a} + {2\gammaB^{\mathsf{T}}P_{\theta}As}}},$
$\Rightarrow$ ${\left. {{\nabla_{a}Q_{\theta}}{(s,a)}} \right|_{a = {- {Ks}}} = {- {2\left( {{RK} - {\gammaB^{\mathsf{T}}P_{\theta}A_{\theta}}} \right)s}}},$ (12a)
$\Rightarrow$ ${{{\nabla_{a}^{2}Q_{\theta}}{(s,a)}} = {2\left( {R + {\gammaB^{\mathsf{T}}P_{\theta}B}} \right)}},$ (12b)

and for the linear policy, we obtain

These equations provide all ingredients for substitution into (11a ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator"))--(11b ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")).

### Policy Gradient in LQR

We now evaluate the policy gradient (10a ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")) for the LQR setting. Substituting the action and policy derivatives from (12a) and yields

where we use ${{vec}{({vs^{\mathsf{T}}})}} = {{({s \otimes I_{m}})}v}$ in the third equality.

Matrix $\Sigma_{\theta}$ is the discounted state second-moment matrix under policy $\pi_{\theta}$ and is defined as,

This is the discounted state correlation matrix, also called the discounted state-occupancy measure. The next lemma gives a closed form characterization of $\Sigma_{\theta}$ for discounted LQR.

### Lemma 2 (Discounted State Correlation Matrix)

For any $\gamma$-stabilizing gain $K$ in Definition 1 ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator"), the series in converges and $\Sigma_{\theta}$ satisfies the discounted Lyapunov equation

See Appendix A. $\blacksquare$

The covariance matrix $\Sigma_{\theta}$ appears explicitly in the policy gradient expression and, as will be shown subsequently, also arises in both the exact and quasi-Hessian formulations.

### Quasi-Newton Policy Gradient in LQR

We derive an approximation of the Hessian of the performance function for discounted LQR by adapting the *general* second-order formulations (11a ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")). From (11a ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")), and since ${{\nabla_{\theta}^{2}\pi_{\theta}}{(s)}} = 0$ for linear policies, the first term vanishes. Using (12b) and, we can rewrite $H{(\theta)}$ as follows:

using the Kronecker mixed-product rule.

### Remark 1

Most Gauss--Newton LQR derivations treat deterministic, *undiscounted* LQR. Here we instantiate (11a ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")) for $\gamma \in {}$ with nonzero additive noise. When $\gamma\rightarrow 1$, applying to recovers the classical update along with standard convergence guarantees. Thus, the treatment both extends discounted stochastic LQR and unifies with established formulations.

### Exact Hessian in LQR

To leverage second-order methods beyond Gauss--Newton, one must capture the state distribution gradients with respect to the policy parameters in (10b ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")). In general RL this coupling is what makes exact Newton steps impractical. Our key insight is that, for discounted LQR, this coupling admits an explicit form with modest assumptions on the disturbance.

We begin with a mild regularity requirement ensuring that boundary contributions vanish when differentiating through the transition kernel. This condition is satisfied by essentially most of the distributions used in control, including Gaussian and sub-Gaussian distributions.

### Assumption 2 (Vanishing boundary flux)

Assume one of the following holds:

Bounded support: $\mathcal{W}$ is a Lipschitz domain and ${p_{w}{(w)}} = 0$ for all $w \in {\partial\mathcal{W}}$; or

Unbounded support: $\mathcal{W} = {\mathbb{R}}^{n}$ and

Under Assumption 2 ‣ 3.3 Exact Hessian in LQR ‣ 3 Gradient and Hessian for LQR ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator"), boundary terms vanish, yielding a closed-form transition contribution to the policy Hessian. The assumption holds for standard disturbances (see remark 2). With this assumption and the regularity conditions of Theorem 1 ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator"), the exact Hessian admits a closed form in LQR.

### Theorem 2 (Exact Hessian in LQR)

Under Assumption 2 ‣ 3.3 Exact Hessian in LQR ‣ 3 Gradient and Hessian for LQR ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator"), the exact Hessian of the performance function for LQR is obtained as ${{\nabla_{\theta}^{2}J}{(\theta)}} = {{H{(\theta)}} + {\gamma\Lambda{(\theta)}}}$ where $H{(\theta)}$ is evaluated from and

and where the Jacobian of $P_{\theta}$ with respect to $\theta$ is

See Appendix B. $\blacksquare$ The term $\Lambda{(\theta)}$ captures the second-order sensitivity of the value-function gradient to policy-induced changes in the transition kernel via its coupling with ${\nabla_{\theta}V_{\theta}}{(s^{\prime})}$. The representation in Theorem 2 ‣ 3.3 Exact Hessian in LQR ‣ 3 Gradient and Hessian for LQR ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator") enables efficient evaluation in exact Newton methods for LQR, which has second-order global convergence. To compute the exact Hessian, evaluate the gradient ; solve (6a) for $P_{\theta}$ and (16 ‣ 3.1 Policy Gradient in LQR ‣ 3 Gradient and Hessian for LQR ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")) for $\Sigma_{\theta}$; build the Jacobian (20 ‣ 3.3 Exact Hessian in LQR ‣ 3 Gradient and Hessian for LQR ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")) using (21 ‣ 3.3 Exact Hessian in LQR ‣ 3 Gradient and Hessian for LQR ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")); assemble $H{(\theta)}$ via and $\Lambda{(\theta)}$ via (19 ‣ 3.3 Exact Hessian in LQR ‣ 3 Gradient and Hessian for LQR ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")).

Therefore, Theorem 2 ‣ 3.3 Exact Hessian in LQR ‣ 3 Gradient and Hessian for LQR ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator") extends Gauss--Newton to exact Newton treatments by providing a closed-form expression for the exact Hessian, thereby enabling true Newton steps for stochastic LQR that remain computationally practical.

## Analytical Example and Simulations

We first analyze a one-dimensional instance to validate the derivations. We next present numerical experiments on two benchmarks: an inverted-pendulum linearization and a high-dimensional seismic shear-building model, both with strongly anisotropic objective landscapes. Numerical results demonstrate the advantages of exact second-order information for Newton-type policy optimization, with and without line search.

### Analytical example: scalar LQR

Consider the following scalar discounted LQR

with $a_{k} = {- {\thetas_{k}}}$, $w_{k} \sim {\mathcal{N}{(0,\sigma^{2})}}$ and $s_{0} \sim {\mathcal{N}{(0,\sigma_{0}^{2})}}$. The resulting closed-loop dynamics are $s_{k + 1} = {{A_{\theta}s_{k}} + w_{k}}$. If $\theta$ is $\gamma$-stabilizing, then using (6a) and, we obtain the closed-form expressions

Invoking (20 ‣ 3.3 Exact Hessian in LQR ‣ 3 Gradient and Hessian for LQR ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")), the derivative of $P_{\theta}$ with respect to $\theta$ is

Using, the policy gradient in one dimension is

Likewise, , the quasi-Hessian in one dimension is

Using (19 ‣ 3.3 Exact Hessian in LQR ‣ 3 Gradient and Hessian for LQR ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")), the transition contribution to the Hessian is

Moreover, differentiate once more to obtain the exact Hessian analytically

where $H{(\theta)}$ and $\Lambda{(\theta)}$ are given in and, respectively. This confirms that the derived expressions for $H{(\theta)}$ and $\Lambda{(\theta)}$ correctly recover the exact Hessian in one dimension. One can verify that the result in Kordabad et al. is a special case of this derivation with $a = b = 1$ and $Q = R = 0.5$.

### Inverted Pendulum Control

Figure 1: Left: 3-D surface of the cost function J (θ) with trajectories. Right: Heatmap of the same region. The Newton PG (green) proceeds directly toward the optimal parameters, whereas the first order PG (red) fluctuates. Darker blue indicates lower cost.

We study the discretization of the upright linearization of a planar inverted pendulum. The dynamics are in the form of with $A$ and $B$ given as

where $g = {{9.81m}/s^{2}}$ is the gravitational constant, $l = {1m}$ is the pendulum length, and $m = {1{kg}}$ is the mass. Process noise is i.i.d. Gaussian with covariance $\Sigma_{w} = I_{2}$, and the initial state covariance is $\Sigma_{0} = {0.1I_{2}}$. Performance is evaluated under an infinite-horizon discounted cost with discount factor $\gamma = 0.9$.

The state penalty is strongly anisotropic with eigenvalues ${(\lambda_{1},\lambda_{2})} = {(10^{5},10^{- 4})}$ rotated by $\psi = 40^{\circ}$, implemented via $Q = {C{diag}{(\lambda_{1},\lambda_{2})}C^{\mathsf{T}}}$ where $C$ is the rotation matrix. The input penalty is $R = 0.1$. Policy gradient schemes are initialized at a common stabilizing gain $K_{0}$ computed with dlqr. Step sizes are selected by backtracking line search. Figure 1 displays the discounted LQR objective $J{(\theta)}$ with parameters $(\theta_{1},\theta_{2})$ slice with the corresponding trajectories. Newton follows the rotated, anisotropic valley to the optimal solution in a few steps, whereas the first order policy gradient oscillates, highlighting the benefit of curvature information. Curvature-based preconditioning aligns updates with principal directions, yielding larger per-iteration decreases in $J{(\theta)}$ and more stable iterates.

### Seismic Shear-Building Benchmark

We evaluate a multi-story shear-building benchmark under base excitation. The stacked state is $s_{k} = {\lbrack q_{k}^{\mathsf{T}},{\overset{˙}{q}}_{k}^{\mathsf{T}}\rbrack}^{\mathsf{T}} \in {\mathbb{R}}^{48}$ with interstory displacements $q_{k} \in {\mathbb{R}}^{24}$ and velocities ${\overset{˙}{q}}_{k} \in {\mathbb{R}}^{24}$. The control input $a_{k}$ applies base actuation. A discrete-time model of the form is obtained by first-order augmentation and zero-order-hold discretization with $T_{s} = {0.01s}$; see A.C. Antoulas and Gugercin for the resulting matrices. We set $w_{k} \sim {\mathcal{N}{(0,{10^{- 4}I_{48}})}}$ and $s_{0} \sim {\mathcal{N}{(0,{10^{- 2}I_{48}})}}$ and neglect measurement noise. The state penalty is strongly anisotropic,

where $V \in {\mathbb{R}}^{48 \times 48}$ is a orthogonal basis, $0 < \lambda_{lo} \ll \lambda_{hi}$ and $R = 0.01$. The initial stabilizing gain $K_{0}$ is computed using dlqr. Step sizes are set to $\alpha_{GN} = 0.5$ for Gauss--Newton, in accordance with convergence results in Fazel et al., and to $\alpha_{N} = 1$ for Newton, selected by a single tuning pass and then kept constant. Figure 2 reports ${\|{K_{k} - K^{\star}}\|}_{F}$ as a function of the iteration index. The plot indicates that Newton achieves quadratic local convergence, while Gauss--Newton attains superlinear rates, both substantially outperforming first-order policy gradient.

Figure 2: The Frobenius-norm policy error, ∥Kk − K⋆∥F, versus iteration index k for natural policy gradient, Gauss–Newton, and Newton. All algorithms are initialized at the same stabilizing gain K0.

## Conclusions

We presented a curvature-aware policy optimization framework for discounted stochastic LQR that yields explicit formulas for both the Gauss--Newton surrogate and the exact performance Hessian. The surrogate coincides with the classical LQR Gauss--Newton matrix; the exact Hessian augments it with a distributional term evaluable under mild boundary conditions. Future work includes model-free curvature estimation (actor--critic, off-policy) with finite-sample guarantees and robust under model uncertainty.
