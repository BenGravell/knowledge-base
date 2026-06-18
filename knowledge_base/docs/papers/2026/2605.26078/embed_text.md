## Introduction

Policy gradient (PG) methods are among the most widely used algorithms in reinforcement learning (RL). Beginning with REINFORCE and the policy gradient theorem, classical PG performs Euclidean gradient ascent over a parameterized policy class. While simple and scalable, Euclidean PG is sensitive to step sizes and parameterization, which has motivated geometry-aware alternatives. Natural policy gradient replaces the Euclidean metric with the information geometry induced by the Fisher information, and is closely related to trust-region (TR) methods. In deep RL, TRPO constrains the average KL divergence between successive policies, while PPO provides a practical surrogate through clipping or adaptive KL penalties. These developments underscore the central role of geometry in policy optimization.

Beyond information geometry, optimal transport (OT) provides a different geometry for policy space, one that is particularly natural for distributions over continuous action spaces. Existing Wasserstein policy optimization methods can be viewed as different implementations or approximations of Wasserstein gradient flow: through JKO schemes and particle approximations, kernelized Wasserstein natural-gradient approximations, trust region formulations, and Wasserstein gradient updates projected onto explicit or implicit policy classes. These methods share the same underlying mechanism: policy improvement is driven by transport in action space.

Entropy regularization is another powerful scheme in modern continuous-control RL. Maximum-entropy RL augments reward maximization with an entropy term on the policy distribution over actions, promoting exploration and robustness and leading to soft Bellman operators and Gibbs-type policy improvements. From the OT perspective, this entropy term naturally induces diffusion. Consequently, Wasserstein policy optimization for the entropy-regularized objective takes the form of a drift-diffusion, or Fokker--Planck, equation, whose particle representation is a Langevin-type actor update. More concretely, the Wasserstein Policy Gradient (WPG) flow reads

and its discrete-time Langevin counterpart is

where $\pi_{k}{( \cdot \mid s)} = {Law}{(A_{k}^{s})}$. Thus, each state-conditional policy is transported along the action gradient of the current soft Q-function, while entropy regularization contributes to the Langevin diffusion.

Despite the algorithmic appeal of WPG, its global convergence behavior remains largely open. Existing global analyses of PG or natural PG typically rely on Euclidean or KL/Bregman geometry in policy space, using mirror-descent identity to relate policy updates to global suboptimality. These arguments do not transfer to Wasserstein geometry, which is non-Bregman and lacks the pointwise three-point structure underlying KL-based analyses. Existing OT-based convergence results also do not directly help for the Langevin WPG update . The convergence result in Zhang et al. is asymptotic and places the entropy regularization on the policy parameters rather than on state-conditional policy distributions. The trust-region analysis of Song et al. applies to finite tabular MDPs without entropy regularization, and Zhu et al. studies a JKO-type implicit proximal scheme. None of these analyses transfers to Langevin dynamics.

Our analysis is closely related to the broader literature on mean-field Langevin dynamics, which has been used to study training dynamics of large interacting particle systems and over-parameterized neural networks. However, global convergence arguments in that literature typically rely on a convex objective and convexity-analysis based argument. RL objective has a different structure: the policy enters the objective through the Bellman recursion which destroys the convexity, and the soft Q-function entangles the reward and entropy term which make the regularity of the Langevin drift not taken for granted.

### Contribution

Our main contribution is a non-asymptotic global convergence analysis of WPG for entropy-regularized continuous-action RL. Rather than relying on the convex-analysis machinery commonly used in standard Mean-field Langevin dynamics, we exploit the Bellman structure of the RL objective. The analysis is built on the following ingredients.

*Value improvement-to-Fisher information via a Bellman resolvent identity.* We show that policy-space dissipation propagates through the Bellman equation via a resolvent identity. This allows us to lower bound value improvement by Fisher-information dissipation, replacing the standard energy-dissipation identity used in convex settings.

*Optimality gap-to-KL via Bellman residuals and contraction.* We represent the statewise soft Bellman residual as a KL divergence between the current policy and its associated Gibbs policy. Bellman contraction then relates this residual to the global optimality gap in sup-norm, replacing the entropy-sandwich arguments used in convex settings.

*Uniform control of the moving Gibbs family.* To exploit the commonly used uniform logarithmic Sobolev inequalities to connect the KL divergence (controlling the optimality gap) with the Fisher information (controlling value improvement), we establish uniform bound estimates along the WPG iterates.

We first illustrate these ideas in the continuous-time WPG flow, where the Bellman residual, contraction, resolvent mechanisms appear most transparently. Then we provide careful analysis for the discrete-time Langevin update, which requires additional regularity estimates for the Wasserstein gradient and a one-step interpolation argument to control time-discretization error. To this end, we establish refined uniform *a priori* bounds on value functions, soft $Q$-functions, drift Lipschitz constants, action moments, drift moments, and the relevant KL quantities. Combining these ingredients yields geometric contraction of the global optimality gap up to a discretization bias.

### Organization

Section 2 introduces the entropy-regularized discounted RL model, the soft Bellman operators, and the Wasserstein/Langevin policy update. Section 3 presents the continuous-time analysis, isolating the core Bellman mechanisms underlying the proof. Section 4 proves the finite-time convergence theorem for the discrete-time update, with emphasis on the additional regularity estimates and discretization-error control. The appendices contain auxiliary results and detailed proofs.

## Model Setup

We consider an infinite-horizon discounted Markov decision process

where $\mathcal{S}$ is the state space, $\mathcal{A}$ is the action space, $\gamma \in {}$ is the discount factor, $\rho_{0} \in {\mathcal{P}{(\mathcal{S})}}$ is the initial state distribution, $P{({{ds^{\prime}} \mid {s,a}})}$ is a Markov transition kernel on $\mathcal{S}$, and $r:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ is a measurable reward function. A (stationary Markov) policy is a conditional distribution $\pi{({{da} \mid s})}$ that admits a density, still denoted $\pi{({a \mid s})}$, with respect to Lebesgue measure on $\mathcal{A}$. Given $\pi$, a trajectory ${(s_{n},a_{n})}_{n \geq 0}$ is generated by $s_{0} \sim \rho_{0}$, $a_{n} \sim \pi{( \cdot \mid s_{n})}$, and $s_{n + 1} \sim P{( \cdot \mid s_{n},a_{n})}$. We write ${\mathbb{E}}_{\rho_{0},\pi}{\lbrack \cdot \rbrack}$ for expectations under this rollout distribution. The normalized discounted state occupancy of $\pi$ is the probability measure $d^{\pi} \in {\mathcal{P}{(\mathcal{S})}}$ defined by

We assume throughout that the initial distribution $\rho_{0}$ has full support on $\mathcal{S}$. Hence, for every policy $\pi$,

Thus $d^{\pi}$ has full support whenever $\rho_{0}$ does. This ensures that the statewise policy-gradient updates below are specified on the same state space on which the sup-norm value bounds are proved. We use the following standing measurability convention. The model kernels and their action derivatives admit jointly measurable versions such that all displayed integrals are jointly measurable. Under this convention, Bellman fixed points are selected as bounded measurable fixed points of contraction maps, and Gibbs and WPG kernels are taken in their induced jointly measurable versions.

We work with an action space $\mathcal{A} = {\mathbb{R}}^{d}$. We consider the regularized reward

where $\beta > 0$ is the quadratic action penalty. This penalty term stabilizes the training, and is also exploited in standard mean-field Langevin dynamics analysis, closely related to the dissipativity condition that helps to control the KL divergence along the trajectory. Fix a temperature $\tau > 0$, we study the discounted regularized objective

restricting attention to policies for which the above expectation is finite. The quadratic action penalty is essential on the unbounded action space. Without this term, the entropy bonus can be made arbitrarily large by spreading the policy mass over larger regions of ${\mathbb{R}}^{d}$, so the entropy-regularized policy-improvement objective may be unbounded above. The quadratic penalty rules out this degeneracy. Equivalently, the quadratic term induces the Gaussian reference

For the discrete-time result, we work on the admissible class

Finite relative entropy gives finite second moments; see Lemma E.25 ‣ E.1 Gaussian entropy, smoothing, and bounded perturbations ‣ Appendix E Standard analytic tools ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") in Appendix E.

### Soft value functions and Bellman operators

Given a policy $\pi$, define the soft value function

so that ${J{(\pi)}} = {\int_{\mathcal{S}}{V^{\pi}{(s)}\rho_{0}{({ds})}}}$ whenever the integral is well-defined. Define the state-action value function

Then $V^{\pi}$ satisfies the soft Bellman identity

For a fixed policy $\pi$, define the policy evaluation operator acting on bounded measurable $V:{\mathcal{S}\rightarrow{\mathbb{R}}}$ by

Under standard measurability and integrability conditions, $\mathcal{T}^{\pi}$ is a $\gamma$-contraction in $\parallel \cdot \parallel_{\infty}$ and its unique fixed point is $V^{\pi} = {\mathcal{T}^{\pi}V^{\pi}}$. For a bounded candidate value $V$, write

Define the soft optimality operator by

where the supremum ranges over action densities for which the expression is finite. The supremum is attained uniquely at a Gibbs density, and therefore

Moreover, $\mathcal{T}^{\star}$ is a $\gamma$-contraction in $\parallel \cdot \parallel_{\infty}$ and has a unique bounded fixed point $V^{\star} = {\mathcal{T}^{\star}V^{\star}}$. We set $Q^{\star}:=Q_{V^{\star}}$ and $\pi^{\star}:={\mathcal{G}{\lbrack V^{\star}\rbrack}}$.

For each $(\pi,s)$, define the Gibbs density by

The following identity relates the Bellman residual to the KL divergence between the current policy and the Gibbs density.

### Lemma 2.0 (Bellman residual identity)

For every $s \in \mathcal{S}$,

where $p_{s}^{\pi}$ is the Gibbs density defined .

### Wasserstein Policy Gradient

Fix a policy $\pi$. The first-variation calculation in Appendix A.2 shows that, for statewise transport perturbations of the action law, the ascent direction is

The discounted occupancy $d^{\pi}$ enters this calculation through the usual policy-gradient weighting over states, as in the policy-gradient theorem and trust-region/natural-gradient policy methods. Taking the Wasserstein gradient of this first variation state by state gives the Wasserstein policy-gradient flow

Using the Gibbs density $p_{s}^{\pi_{t}}$ , this can be rewritten as

From an equivalent particle viewpoint, for each fixed state $s$, the above Fokker--Planck equation can be viewed formally as the forward equation of the nonlinear Langevin diffusion

Applying an explicit Euler--Maruyama step to this statewise Langevin diffusion gives the discrete-time update below.

The discrete-time counterpart of (WPGF) is the Langevin policy update

where $A_{k}^{s} \sim \pi_{k}{( \cdot \mid s)}$ and

Thus WPGD is a statewise policy-space update specified for every $s \in \mathcal{S}$. Under the full-support convention above, the discounted occupancy weighting does not remove any state from the gradient calculation, and the convergence theorem below controls the resulting value gap in sup-norm over the same state space.

## Continuous-Time Analysis: Bellman Geometry

This section presents a formal continuous-time analysis of the Wasserstein policy gradient flow (WPGF). Its purpose is to make transparent the Bellman mechanisms that replace the standard mean-field Langevin dynamics proof chain. We do not claim here a complete well-posedness theorem for the nonlinear Fokker--Planck equation. Instead, the identities below are stated under a smooth-flow regularity convention that supplies the differentiability, integrability, and boundary-decay properties needed for the calculation.

### Why the standard mean-field Langevin dynamics proof chain does not directly apply

For a mean-field Langevin dynamics problem, exponential convergence is often proved through the schematic chain:

where (a) is the gradient-flow dissipation identity, (b) follows from a uniform LSI, and (c) is through a convex-analysis based comparison from local KL to global suboptimality. In entropy-regularized RL, these relationships do not hold in these forms. First, (a) is altered by the Bellman recursion: differentiating $V^{\pi_{t}}$ also differentiates $Q^{\pi_{t}}$ through the value function, so the value derivative is not merely a statewise Fisher-information dissipation. Lemma 3.4 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") replaces this step by the value-resolvent identity ${{({I - {\gammaP^{\pi_{t}}}})}{\overset{˙}{V}}^{\pi_{t}}} = g_{t}$, with $g_{t}$ proportional to a statewise Fisher-information term. Second, (b) is not directly available from a convex functional, because the RL objective is nonconvex due to the Bellman recursion of the state-dependent policy distribution. Lemma 3.5 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") and 3.6 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") will derive a uniform LSI from uniform value/$Q$ bounds. Third, (c) cannot be obtained from convexity due to the nonconvexity and aggregation over states in the RL objective. Instead, Lemma 2.1 ‣ 2.1 Soft value functions and Bellman operators ‣ 2 Model Setup ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") identifies $\tau{KL}{(\pi_{t}{( \cdot \mid s)} \parallel p_{s}^{\pi_{t}})}$ with the statewise Bellman residual, and Bellman contraction in the proof of Theorem 3.7 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") will compare this residual at the worst state directly with the $\parallel \cdot \parallel_{\infty}$-value gap.

*Smooth-flow regularity convention.* Throughout this section only, the flow (WPGF) is considered for smooth positive solutions $\pi_{t}{( \cdot \mid s)}$ satisfying the following properties on every finite time interval. For each state $s$, $t\mapsto{V^{\pi_{t}}{(s)}}$ is locally absolutely continuous, the density $\pi_{t}{( \cdot \mid s)}$ has the moments, entropy, Fisher information, and decay at infinity needed for all displayed integrations by parts, and $a\mapsto{Q^{\pi_{t}}{(s,a)}}$ is sufficiently smooth. Differentiation under the action/state integrals is assumed valid. These assumptions are used only for the formal PDE calculation in this section for illustration and will not be used in the discrete-time analysis in Section 4.

### Assumption 3.1 (Boundedness and initialization)

We assume the following throughout:

${|{r{(s,a)}}|} \leq R_{\max}$ for all ${(s,a)} \in {\mathcal{S} \times \mathcal{A}}$.

$\sup_{s \in \mathcal{S}}{KL}{(\pi_{0}{( \cdot \mid s)} \parallel \rho_{\beta})} \leq K_{0}$, where ${\rho_{\beta}{(a)}} \propto {\exp\left( {- {\frac{\beta}{2\tau}{\| a\|}^{2}}} \right)}$.

Our proof proceeds in three steps. First, we establish a resolvent identity for the value derivative along the flow (Lemma 3.4 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")), which reveals a dissipation given by Fisher information relative to the moving Gibbs family $p_{s}^{\pi_{t}}$ and yields monotone value improvement. Second, we use this monotonicity together with bounded rewards and the initialization condition to obtain uniform-in-time bounds on $V^{\pi_{t}}$ and $Q^{\pi_{t}}$ (Lemma 3.5 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")); these bounds imply that each $p_{s}^{\pi_{t}}$ is a bounded perturbation of a Gaussian, enabling a uniform log-Sobolev inequality along the optimization trajectory via Holley-Stroock Perturbation Lemma (Lemma 3.6 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")). Third, we combine the uniform LSI with the Bellman-residual identity, Lemma 2.1 ‣ 2.1 Soft value functions and Bellman operators ‣ 2 Model Setup ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"), and Bellman contraction to convert KL dissipation into an exponential-decay estimate for the optimality gap (Theorem 3.7 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")).

Note that RL policy differs from the standard mean-field Langevin dynamics in that it is concerned with a family of state-dependent policy distributions ${\{\pi{( \cdot \mid s)}\}}_{s \in \mathcal{S}}$ rather than a single distribution. Thus, adapting the usual proof chain to RL settings requires choosing how to aggregate statewise quantities. Another possible route is to aggregate the KL terms in (c) by a discounted state-visitation distribution via the performance difference lemma A.16 ‣ A.1 Entropy-Regularized Performance Difference Lemma ‣ Appendix A Auxiliary Results ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"), as in occupancy-weighted policy-gradient analyses. However, this creates a mismatch between the state distribution used to measure the optimality gap and the state aggregation naturally induced by the value derivative or resolvent identity in (a). Closing this gap typically requires density-ratio or coverage assumptions between state distributions. Our argument above circumvents this route by keeping the Bellman residual identity statewise and using Bellman contraction to lower bound the residual in terms of the sup-norm value gap, and thus does not require additional coverage assumptions.

For a policy $\pi$, define the induced state kernel

### Definition 3.0 (KL divergence and relative Fisher information)

Let $\mu$ and $\nu$ be probability measures on ${\mathbb{R}}^{d}$ with $\mu \ll \nu$. The Kullback--Leibler divergence of $\mu$ from $\nu$ is defined by

The relative Fisher information of $\mu$ with respect to $\nu$ is defined by

### Definition 3.0 (Log-Sobolev inequality)

Let $\nu$ be a probability measure on ${\mathbb{R}}^{d}$ with positive density. We say that $\nu$ satisfies a log-Sobolev inequality with constant $\alpha > 0$, or $\alpha$-LSI, if

for every probability measure $\mu$ for which the two sides are well-defined.

We first establish an identity for the time derivative of $V^{\pi_{t}}$ along the flow (WPGF).

### Lemma 3.0 (Monotonicity of $V^{\pi_{t}}$)

Under Assumption 3.1 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") and the smooth-flow regularity convention, for every $t \geq 0$,

where $\mathcal{I}\left( \pi_{t}{( \cdot \mid s)} \parallel p_{s}^{\pi_{t}} \right)$ is the relative Fisher information. Moreover,

Lemma 3.4 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") shows that the value derivative satisfies

and is therefore pointwise nonnegative along the flow (WPGF). Note that this identity can be viewed as the statewise resolvent form of the entropy-regularized performance-difference lemma: integrating it against an initial distribution recovers the usual occupancy-weighted performance-difference formula, whereas keeping it pointwise is what enables the subsequent sup-norm contraction argument in below without introducing state-distribution mismatch coefficients. Based on Lemma 3.4 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"), we derive uniform-in-time bounds on the value function, which further imply uniform bounds on the action-value Q-function.

### Lemma 3.0 (Uniform bounds on $V^{\pi_{t}}$ and $Q^{\pi_{t}}$)

Under Assumption 3.1 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") and the smooth-flow regularity convention above, for all $t \geq 0$,

Consequently, for all $t \geq 0$, $s \in \mathcal{S}$, and $a \in \mathcal{A}$,

Thanks to the bound (20 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")) on the Q-function, the Gibbs densities $p_{s}^{\pi_{t}}$ are bounded perturbations of Gaussian densities, and thus satisfy log-Sobolev inequalities with uniform constants along the optimization trajectory due to the Holley-Stroock perturbation lemma.

### Lemma 3.0 (Trajectory-uniform LSI for Gibbs policies)

Then for every $t \geq 0$ and $s \in \mathcal{S}$, the Gibbs density $p_{s}^{\pi_{t}}$ satisfies the log-Sobolev inequality

with the uniform constant

We now state the exponential-decay consequence of the preceding identities. Let $V^{\star}$ be the unique fixed point of $\mathcal{T}^{\star}$, and let $\pi^{\star}$ denote the optimal Gibbs policy attaining $V^{\star}$. Since $V^{\star}$ is the optimal value function and the flow remains in the admissible policy class, ${V^{\star}{(s)}} \geq {V^{\pi_{t}}{(s)}}$ for all $s,t$. Define the residual

By Lemma 2.1 ‣ 2.1 Soft value functions and Bellman operators ‣ 2 Model Setup ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"),

Since $V^{\star} = {\mathcal{T}^{\star}V^{\star}}$, $\mathcal{T}^{\star}$ is monotone, and $\mathcal{T}^{\star}$ is a $\gamma$-contraction in $\parallel \cdot \parallel_{\infty}$,

### Theorem 3.7 (Exponential convergence along the smooth WPG flow)

Under Assumption 3.1 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") and the smooth-flow regularity convention above, for all $t \geq 0$,

Proof By Lemma 3.4 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"), specifically (16 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")) and (17 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")), for almost every $t$,

By Lemma 3.6 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") and,

Next, using the definition of $W_{t}$ and $R_{t}$,

Combining and gives the pointwise differential inequality

for almost every $t$.

Multiplying by the integrating factor $e^{2\alpha\taut}$ and integrating from $0$ to $t$ yields

Taking the supremum over $s \in \mathcal{S}$ in gives

Multiplying by $e^{2\alpha\taut}$ gives

Finally, since $\rho_{0}$ is a probability measure and $W_{t} \geq 0$ pointwise,

This proves the theorem. \

Theorem 3.7 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") is a formal continuous-time convergence for smooth solutions of (WPGF). It identifies the rate obtained from the value-resolvent identity, uniform value/$Q$ bounds, the uniform LSI, and the statewise Bellman-residual identity. Its role is explanatory: it isolates the Bellman-residual mechanism and motivates the discrete-time argument.

After the first version of this paper was submitted for review, we became aware of a closely related note by Šiška and Zhang. Their analysis and resulting guarantee are structurally different from ours. In their cost-minimization notation, the argument uses an entropy-sandwich inequality to control the scalar distributional gap ${V^{\pi_{t}}{(\rho)}} - {V^{\pi^{\star}}{(\rho)}}$ and states a bound of the form

where $\overline{\kappa}:={\sup_{s \in \mathcal{S}}{\frac{d\rho}{dd_{\rho}^{\pi^{\star}}}{(s)}}}$, ${\kappa:={\inf_{s \in \mathcal{S}}{\frac{d\rho}{dd_{\rho}^{\pi^{\star}}}{(s)}}} \leq 1}.$ Thus their estimate is distribution-dependent and requires coverage-type density-ratio control, in particular $\kappa > 0$, to obtain a positive exponential rate. By contrast, Theorem 3.7 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") proves a state-uniform bound and therefore controls ${J{(\pi^{\star})}} - {J{(\pi_{t})}}$ for any initial state distribution. The proof mechanisms are also different: rather than passing through an occupancy-weighted entropy sandwich, we use the exact statewise Bellman-residual identity and Bellman contraction to compare the residual directly with the $\parallel \cdot \parallel_{\infty}$-optimality gap. This removes the density-ratio constants $\kappa$ from the exponential convergence rate, although with a different initial gap. Finally, both their and our analyses involve formal calculations; the main rigorous guarantee in the present paper is the discrete-time Langevin analysis in Section 4.

## Discrete-Time Global Convergence Analysis

This section proves the non-asymptotic convergence guarantee for the explicit Langevin update (WPGD). The continuous-time section isolates the Bellman residual/resolvent mechanism. Apart from their counterparts in discrete time, an additional task is to control the finite-step Langevin discretization and the policy-dependent drift uniformly along the iterates.

### Assumptions

The assumptions below are the quantitative inputs for the finite-step analysis. To apply the one step drift interpolation argument, we need uniform control of the drift Lipschitz constants, action moments, drift second moments, finite KL quantities, and the LSI constants of the Gibbs family. Since

these constants cannot be read off from the Wasserstein gradient of a static functional; they must be derived from the Bellman recursion and propagated along the WPG iterates. Assumptions 4.1 ‣ 4.1 Assumptions ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")-4.2 ‣ 4.1 Assumptions ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"), together with the a priori bounds that will be proved in Proposition 4.14 ‣ 4.2.2 Drift regularity and the discretization error ‣ 4.2 Proof sketch and main theorem ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"), provide this uniform control.

### Assumption 4.1 (Bounded rewards and initialization)

${|{r{(s,a)}}|} \leq R_{\max}$ for all ${(s,a)} \in {\mathcal{S} \times {\mathbb{R}}^{d}}$.

$\sup_{s \in \mathcal{S}}{KL}{(\pi_{0}{( \cdot \mid s)} \parallel \rho_{\beta})} \leq K_{0}$.

For constants used later, set

This quantity is finite by Lemma E.25 ‣ E.1 Gaussian entropy, smoothing, and bounded perturbations ‣ Appendix E Standard analytic tools ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") applied uniformly in $s$. In particular, applying that lemma with $c = {\beta/{({4\tau})}}$ and using Assumption 4.1 ‣ 4.1 Assumptions ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")(ii) gives

### Assumption 4.2 (Action regularity)

There is a $\sigma$-finite reference measure $\lambda$ on $\mathcal{S}$ such that ${P{({{ds^{\prime}} \mid {s,a}})}} = {p{({s^{\prime} \mid {s,a}})}\lambda{({ds^{\prime}})}}$. There are finite constants $L_{r},L_{p},G_{r},G_{p}$ such that:

For every $s \in \mathcal{S}$, the map $a\mapsto{r{(s,a)}}$ is continuously differentiable and

For every $s \in \mathcal{S}$ and $\lambda$-a.e. $s^{\prime} \in \mathcal{S}$, the map $a\mapsto{p{({s^{\prime} \mid {s,a}})}}$ is continuously differentiable, and

A concrete example satisfying the transition part of Assumption 4.2 ‣ 4.1 Assumptions ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") is the following additive-noise model. Let $\mathcal{S} = {\mathbb{R}}^{m}$, let $\lambda$ be Lebesgue measure, and suppose

where $\sigma \in {\mathbb{R}}^{m \times m}$ is invertible and $\zeta$ has a smooth density $q$. Write

for the density of $\sigma\zeta$, and assume

Assume further that, uniformly in $s$,

satisfies Assumption 4.2 ‣ 4.1 Assumptions ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")(ii). Indeed,

so one may take

Nondegenerate Gaussian noise is a special case, since its first derivative and Hessian are integrable. Together with the reward condition in Assumption 4.2 ‣ 4.1 Assumptions ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")(i), this gives a concrete class of controlled transition models covered by the theorem. Deterministic or degenerate-noise dynamics are not covered by this example.

With these assumptions in place, write

and define the current-policy Langevin drift

The current-policy Gibbs stationarity condition is

### Proof sketch and main theorem

### Bellman residual-to-optimality gap mechanism and uniform LSI

We first record the discrete counterparts of the residual and resolvent mechanisms from Section 3. They show that the KL to the current-policy Gibbs law is exactly the Bellman residual, that this residual controls the worst-state value gap, and that decreasing the same KL produces value improvement after applying the Bellman resolvent.

### Lemma 4.0 (Bellman contraction of the residual)

Fix $k \geq 0$. Let $R_{k}:={{({\mathcal{T}^{\star}V^{\pi_{k}}})} - V^{\pi_{k}}}$. Then, for every $s \in \mathcal{S}$,

### Lemma 4.0 (Discrete Bellman resolvent)

Fix $k \geq 0$. Suppose $\pi_{k}$ and the WPG update $\pi_{k + 1}$ are admissible, with measurability covered by the convention in Section 2, and the KL terms below are finite. Then

and, for every $s \in \mathcal{S}$,

As a consequence of these two lemmas, once $p_{s}^{\pi_{k}}$ satisfies an LSI with constant $\overline{\alpha}$, the Bellman residual yields the following PŁ-type residual-to-gap inequality at an $\varepsilon$-maximizer of $W_{k}$:

This is a PŁ inequality for the Bellman gap, not a consequence of flat convexity of $J$.

The LSI used in follows from the same Gaussian perturbation mechanism as in continuous time, but it must be made uniform along the discrete trajectory. The a priori bounds prove a uniform value bound; once ${\| V^{\pi_{k}}\|}_{\infty} \leq V_{\max}$,

The perturbation $\psi_{k,s}$ may be nonconvex, but bounded rewards and the value bound give ${\|\psi_{k,s}\|}_{\infty} \leq {{({R_{\max} + {\gammaV_{\max}}})}/\tau}$ and hence ${{osc}{(\psi_{k,s})}} \leq {{2{({R_{\max} + {\gammaV_{\max}}})}}/\tau}$. The Holley-Stroock bounded-perturbation principle then transfers the Gaussian LSI of $\rho_{\beta}$ to every $p_{s}^{\pi_{k}}$ uniformly.

### Lemma 4.0 (Uniform LSI)

Fix $k \geq 0$ and suppose ${\| V^{\pi_{k}}\|}_{\infty} \leq V_{\max}$. Then, for every $s \in \mathcal{S}$, the current-policy Gibbs density $p_{s}^{\pi_{k}}$ satisfies

### Drift regularity and the discretization error

We now control the finite-step error introduced by the Langevin discretization. As explained in Section 4.1, the drift Langevin interpolation requires uniform action-Lipschitz and dissipativity estimates for the policy-dependent drift. The following lemma converts the action-regularity assumptions and a value bound into those estimates.

### Lemma 4.0 (Bellman drift regularity)

Assume Assumption 4.2 ‣ 4.1 Assumptions ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"). Fix $k \geq 0$ and suppose ${\| V^{\pi_{k}}\|}_{\infty} \leq V_{\max} < \infty$. Then, for every $s \in \mathcal{S}$,

Moreover, for all ${a,\overline{a}} \in {\mathbb{R}}^{d}$,

The Lipschitz bound controls the Euler interpolation error; the dissipative decomposition controls the second moment and hence the squared drift moment. Together with the LSI from Lemma 4.10 ‣ 4.2.1 Bellman residual-to-optimality gap mechanism and uniform LSI ‣ 4.2 Proof sketch and main theorem ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"), they give the only place where discrete time loses exact monotonicity. The analytic part of the next lemma is based on a one-step fixed-drift interpolation. The full calculation is given in Appendix D.2.

### Lemma 4.0 (One-step KL contraction with discretization error)

Fix $k \geq 0$ and $s \in \mathcal{S}$. Suppose $p_{s}^{\pi_{k}} > 0$, ${\log p_{s}^{\pi_{k}}} \in {C^{1}{({\mathbb{R}}^{d})}}$, $p_{s}^{\pi_{k}}$ satisfies an LSI with constant $\alpha > 0$, and the Gibbs-score identity

holds. Suppose also that $b_{k}{(s, \cdot )}$ is $L_{b}$-Lipschitz and

### Lemma 4.0 (From KL contraction to Bellman improvement)

Fix $k \geq 0$ and $s \in \mathcal{S}$. Suppose the admissibility and finite-KL hypotheses of Lemma 4.9 ‣ 4.2.1 Bellman residual-to-optimality gap mechanism and uniform LSI ‣ 4.2 Proof sketch and main theorem ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") hold for $(\pi_{k},\pi_{k + 1})$. If, for some $c \in {\lbrack 0,1\rbrack}$ and $\delta \geq 0$,

then, with $R_{k}{(s)} = \tau{KL}{(\pi_{k}{( \cdot \mid s)} \parallel p_{s}^{\pi_{k}})}$ and $g_{k}$ as in Lemma 4.9 ‣ 4.2.1 Bellman residual-to-optimality gap mechanism and uniform LSI ‣ 4.2 Proof sketch and main theorem ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"),

In particular, Lemma 4.12 ‣ 4.2.2 Drift regularity and the discretization error ‣ 4.2 Proof sketch and main theorem ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") supplies (39 ‣ 4.2.2 Drift regularity and the discretization error ‣ 4.2 Proof sketch and main theorem ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")) with $c = {1 - e^{- {\alpha\tau\eta}}}$ and $\delta = {\delta_{\eta}{(L_{b},B^{2})}}$ whenever its analytic hypotheses also hold.

With the uniform constants supplied by Proposition 4.14 ‣ 4.2.2 Drift regularity and the discretization error ‣ 4.2 Proof sketch and main theorem ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"), the preceding lemmas yield a closed one-step recursion for the sup-norm gap. Throughout this argument, $\overline{\alpha}$ denotes the trajectory-uniform LSI constant, ${\overline{L}}_{b}$ the uniform Lipschitz constant of the drift, ${\overline{B}}^{2}$ the uniform second-moment bound for the drift, and ${\overline{\delta}}_{\eta}$ the corresponding one-step Langevin discretization error. Set

Then, for every $s \in \mathcal{S}$, the estimates compose as follows:

Here the KL terms are statewise, $R_{k} = {{\mathcal{T}^{\star}V^{\pi_{k}}} - V^{\pi_{k}}}$, and $E_{k} = {\|{V^{\star} - V^{\pi_{k}}}\|}_{\infty}$. The substantive RL step is the middle of: a local KL decrease becomes a global value-gap contraction through the Bellman residual and the value resolvent, not through flat convexity of a probability functional. The implications in reduce the convergence proof to estimates that hold uniformly along the WPGD trajectory. The constants entering this recursion are policy dependent, since both $p_{s}^{\pi_{k}}$ and $b_{k}$ are defined through $Q^{\pi_{k}}$ and hence through the Bellman fixed point $V^{\pi_{k}}$. The next proposition supplies the required a priori estimates. Approximate value monotonicity controls the lower value envelope, the quadratic action penalty gives uniform action-moment bounds, and these estimates feed back into uniform drift regularity, finite KL controls, and a trajectory-uniform LSI for the moving Gibbs family.

### Proposition 4.0 (Uniform a priori bounds for the WPGD iterates)

Under Assumptions 4.1 ‣ 4.1 Assumptions ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") and 4.2 ‣ 4.1 Assumptions ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"), there exist explicit finite constants

depending only on the problem data and the initialization such that, for every $0 < \eta \leq \eta_{0}$, the WPG iterates are admissible and, for all $k \geq 0$,

Moreover, $a\mapsto{{\nabla_{a}Q^{\pi_{k}}}{(s,a)}}$ is ${\overline{L}}_{b}$-Lipschitz uniformly in $(k,s)$, every current-policy Gibbs density $p_{s}^{\pi_{k}}$ satisfies LSI with constant at least $\overline{\alpha}$, and the generated policies satisfy

All constants and the feasible step-size range are given in Appendix C.

Proposition 4.14 ‣ 4.2.2 Drift regularity and the discretization error ‣ 4.2 Proof sketch and main theorem ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") provides the uniform constants needed to run the one-step recursion in at every iteration. The value bound yields a common Holley--Stroock perturbation bound and hence a uniform LSI constant $\overline{\alpha}$; the drift Lipschitz and second-moment estimates give a uniform discretization error ${\overline{\delta}}_{\eta} = {O{(\eta^{2})}}$; and the admissibility and finite-KL bounds ensure that the resolvent identity and the one step drift interpolation estimate apply throughout the trajectory. Substituting these uniform estimates into gives a closed scalar recursion for the sup-norm optimality gap, which yields the geometric contraction up to the accumulated Langevin discretization bias stated in the main theorem.

### Theorem 4.15 (Global convergence of WPGD up to discretization bias)

Under Assumptions 4.1 ‣ 4.1 Assumptions ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") and 4.2 ‣ 4.1 Assumptions ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"), there exist explicit finite constants ${\overline{\alpha},C_{\delta},\eta_{0}} > 0$, such that for every $0 < \eta \leq \eta_{0}$ and every $k \geq 0$,

Theorem 4.15 ‣ 4.2.2 Drift regularity and the discretization error ‣ 4.2 Proof sketch and main theorem ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") gives a finite-step geometric contraction for the WPGD update (WPGD), up to a fixed-step discretization bias. The drift KL estimate has an additive error ${\overline{\delta}}_{\eta} = {O{(\eta^{2})}}$, and the scalar gap recursion divides this error by ${1 - e^{- {\overline{\alpha}\tau\eta}}} \asymp {\overline{\alpha}\tau\eta}$. The proof in Appendix D.4 keeps the sharper quantity ${\overline{\delta}}_{\eta}$ throughout and substitutes ${\overline{\delta}}_{\eta} \leq {C_{\delta}\eta^{2}}$ only at the end.

The theorem is closest in form to discrete-time mean-field Langevin guarantees, but the source of the contraction is different. Mean-field convex analyses convert KL decrease to objective decrease through flat convexity of a distributional objective. Here the Gibbs law $p_{s}^{\pi_{k}}$ moves with the policy through the soft Bellman equation that depends on both the policy gradient and the KL regularization. The required PŁ-type relation is therefore reconstructed from the RL-specific ingredients.

The result is also complementary to entropy-regularized natural policy gradient and policy mirror descent, where KL/Bregman geometry gives a closed-form policy-improvement step and Bellman monotonicity. WPGD instead uses Wasserstein geometry: local progress is Fisher-information dissipation in action space, and the main technical burden is to show that this transport-based dissipation remains uniformly controlled under the policy-dependent Bellman recursion and relate it to the global optimality gap.

## Conclusion

We developed a convergence analysis framework for Wasserstein policy gradient in entropy-regularized discounted RL with continuous actions. The proof combines Bellman-residual identities, value-resolvent relation, one-step interpolation, uniform value/Q-function and moment bounds, and uniform LSI for the iterated Gibbs family. These ingredients yield exponential convergence for the continuous-time WPG flow and geometric convergence for the discrete-time WPG Langevin dynamics up to a discretization bias. An important direction for future work is to integrate these policy-space guarantees with practical approximations, such as projection onto parametric policy classes and finite-sample critic estimation.
