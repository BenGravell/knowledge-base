<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning

Topics include Policy gradients, Reinforcement learning, Optimal transport, Wasserstein distances, Entropy regularization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Analyzes Wasserstein policy gradient for entropy-regularized reinforcement learning, treating policy updates through optimal-transport geometry rather than standard Euclidean parameter steps. The result clarifies when this continuous-control-friendly policy-gradient flow converges globally.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Wasserstein policy gradient (WPG) is a policy optimization method for reinforcement learning (RL) that exploits the optimal-transport geometry of action distributions. For the entropy-regularized RL objective, WPG evolves each state-conditional policy by transporting it along the action gradient of the soft Q-function together with a Langevin-type diffusion. Despite its appeal for continuous-control problems, its global convergence properties remain poorly understood. Standard Langevin analyses do not directly apply, because the RL objective depends on the policy through the Bellman recursion rather than through a static convex functional, and the Langevin drift is determined by the soft Q-function, whose regularity must be controlled along the policy iterates. In this paper, we develop a global convergence theory for WPG by exploiting the Bellman structure of entropy-regularized RL. We show that the role usually played by convexity can be replaced by a Bellman-based argument: the soft Bellman residual admits a statewise KL representation with respect to a Gibbs policy; Bellman contraction relates this residual to the global optimality gap; and a Bellman resolvent identity connects value improvement to relative Fisher information.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Combined with a uniform log-Sobolev inequality (LSI) for the evolving Gibbs family, these ingredients yield a distributional Polyak-Łojasiewicz condition. We further establish the regularity and uniform bounds needed to control the discretization error, thereby obtaining geometric contraction up to a discretization bias. Conceptually, our analysis shows that although entropy-regularized RL is not convex in the usual flat sense, the Bellman recursion induces a favorable Polyak-Lojasiewicz-type (PL) geometry that supports global convergence of WPG.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy gradient (PG) methods are among the most widely used algorithms in reinforcement learning (RL). Beginning with REINFORCE and the policy gradient theorem, classical PG performs Euclidean gradient ascent over a parameterized policy class. While simple and scalable, Euclidean PG is sensitive to step sizes and parameterization, which has motivated geometry-aware alternatives. Natural policy gradient replaces the Euclidean metric with the information geometry induced by the Fisher information, and is closely related to trust-region (TR) methods. In deep RL, TRPO constrains the average KL divergence between successive policies, while PPO provides a practical surrogate through clipping or adaptive KL penalties. These developments underscore the central role of geometry in policy optimization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Beyond information geometry, optimal transport (OT) provides a different geometry for policy space, one that is particularly natural for distributions over continuous action spaces. Existing Wasserstein policy optimization methods can be viewed as different implementations or approximations of Wasserstein gradient flow: through JKO schemes and particle approximations, kernelized Wasserstein natural-gradient approximations, trust region formulations, and Wasserstein gradient updates projected onto explicit or implicit policy classes. These methods share the same underlying mechanism: policy improvement is driven by transport in action space.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Entropy regularization is another powerful scheme in modern continuous-control RL. Maximum-entropy RL augments reward maximization with an entropy term on the policy distribution over actions, promoting exploration and robustness and leading to soft Bellman operators and Gibbs-type policy improvements. From the OT perspective, this entropy term naturally induces diffusion. Consequently, Wasserstein policy optimization for the entropy-regularized objective takes the form of a drift-diffusion, or Fokker--Planck, equation, whose particle representation is a Langevin-type actor update. More concretely, the Wasserstein Policy Gradient (WPG) flow reads and its discrete-time Langevin counterpart is where $\pi_{k}(\cdot\mid s)=\mathrm{Law}(A_{k}^{s})$. Thus, each state-conditional policy is transported along the action gradient of the current soft Q-function, while entropy regularization contributes to the Langevin diffusion.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the algorithmic appeal of WPG, its global convergence behavior remains largely open. Existing global analyses of PG or natural PG typically rely on Euclidean or KL/Bregman geometry in policy space, using mirror-descent identity to relate policy updates to global suboptimality. These arguments do not transfer to Wasserstein geometry, which is non-Bregman and lacks the pointwise three-point structure underlying KL-based analyses. Existing OT-based convergence results also do not directly help for the Langevin WPG update. The convergence result in Zhang et al. is asymptotic and places the entropy regularization on the policy parameters rather than on state-conditional policy distributions. The trust-region analysis of Song et al. applies to finite tabular MDPs without entropy regularization, and Zhu et al. studies a JKO-type implicit proximal scheme. None of these analyses transfers to Langevin dynamics.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our analysis is closely related to the broader literature on mean-field Langevin dynamics, which has been used to study training dynamics of large interacting particle systems and over-parameterized neural networks. However, global convergence arguments in that literature typically rely on a convex objective and convexity-analysis based argument. RL objective has a different structure: the policy enters the objective through the Bellman recursion which destroys the convexity, and the soft Q-function entangles the reward and entropy term which make the regularity of the Langevin drift not taken for granted.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contribution", "weight": 1.0} -->

Our main contribution is a non-asymptotic global convergence analysis of WPG for entropy-regularized continuous-action RL. Rather than relying on the convex-analysis machinery commonly used in standard Mean-field Langevin dynamics, we exploit the Bellman structure of the RL objective. The analysis is built on the following ingredients.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contribution", "weight": 1.0} -->

*Value improvement-to-Fisher information via a Bellman resolvent identity.* We show that policy-space dissipation propagates through the Bellman equation via a resolvent identity. This allows us to lower bound value improvement by Fisher-information dissipation, replacing the standard energy-dissipation identity used in convex settings.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contribution", "weight": 1.0} -->

*Optimality gap-to-KL via Bellman residuals and contraction.* We represent the statewise soft Bellman residual as a KL divergence between the current policy and its associated Gibbs policy. Bellman contraction then relates this residual to the global optimality gap in sup-norm, replacing the entropy-sandwich arguments used in convex settings.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contribution", "weight": 1.0} -->

*Uniform control of the moving Gibbs family.* To exploit the commonly used uniform logarithmic Sobolev inequalities to connect the KL divergence (controlling the optimality gap) with the Fisher information (controlling value improvement), we establish uniform bound estimates along the WPG iterates.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Contribution", "weight": 1.0} -->

We first illustrate these ideas in the continuous-time WPG flow, where the Bellman residual, contraction, resolvent mechanisms appear most transparently. Then we provide careful analysis for the discrete-time Langevin update, which requires additional regularity estimates for the Wasserstein gradient and a one-step interpolation argument to control time-discretization error. To this end, we establish refined uniform *a priori* bounds on value functions, soft $Q$-functions, drift Lipschitz constants, action moments, drift moments, and the relevant KL quantities. Combining these ingredients yields geometric contraction of the global optimality gap up to a discretization bias.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Organization", "weight": 1.0} -->

Section 2 introduces the entropy-regularized discounted RL model, the soft Bellman operators, and the Wasserstein/Langevin policy update. Section 3 presents the continuous-time analysis, isolating the core Bellman mechanisms underlying the proof. Section 4 proves the finite-time convergence theorem for the discrete-time update, with emphasis on the additional regularity estimates and discretization-error control. The appendices contain auxiliary results and detailed proofs.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Model Setup", "weight": 1.0} -->

We consider an infinite-horizon discounted Markov decision process where $\mathcal{S}$ is the state space, $\mathcal{A}$ is the action space, $\gamma\in$ is the discount factor, $\rho_{0}\in\mathcal{P}(\mathcal{S})$ is the initial state distribution, $P(\mathrm{d}s^{\prime}\mid s,a)$ is a Markov transition kernel on $\mathcal{S}$, and $r:\mathcal{S}\times\mathcal{A}\to\mathbb{R}$ is a measurable reward function. A (stationary Markov) policy is a conditional distribution $\pi(\mathrm{d}a\mid s)$ that admits a density, still denoted $\pi(a\mid s)$, with respect to Lebesgue measure on $\mathcal{A}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Model Setup", "weight": 1.0} -->

Given $\pi$, a trajectory $(s_{n},a_{n})_{n\geq 0}$ is generated by $s_{0}\sim\rho_{0}$, $a_{n}\sim\pi(\cdot\mid s_{n})$, and $s_{n+1}\sim P(\cdot\mid s_{n},a_{n})$. We write $\mathbb{E}_{\rho_{0},\pi}[\cdot]$ for expectations under this rollout distribution. The normalized discounted state occupancy of $\pi$ is the probability measure $d^{\pi}\in\mathcal{P}(\mathcal{S})$ defined by We assume throughout that the initial distribution $\rho_{0}$ has full support on $\mathcal{S}$. Hence, for every policy $\pi$, Thus $d^{\pi}$ has full support whenever $\rho_{0}$ does.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Model Setup", "weight": 1.0} -->

This ensures that the statewise policy-gradient updates below are specified on the same state space on which the sup-norm value bounds are proved. We use the following standing measurability convention. The model kernels and their action derivatives admit jointly measurable versions such that all displayed integrals are jointly measurable. Under this convention, Bellman fixed points are selected as bounded measurable fixed points of contraction maps, and Gibbs and WPG kernels are taken in their induced jointly measurable versions.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Model Setup", "weight": 1.0} -->

We work with an action space $\mathcal{A}=\mathbb{R}^{d}$. We consider the regularized reward where $\beta>0$ is the quadratic action penalty. This penalty term stabilizes the training, and is also exploited in standard mean-field Langevin dynamics analysis, closely related to the dissipativity condition that helps to control the KL divergence along the trajectory. Fix a temperature $\tau>0$, we study the discounted regularized objective restricting attention to policies for which the above expectation is finite. The quadratic action penalty is essential on the unbounded action space. Without this term, the entropy bonus can be made arbitrarily large by spreading the policy mass over larger regions of $\mathbb{R}^{d}$, so the entropy-regularized policy-improvement objective may be unbounded above. The quadratic penalty rules out this degeneracy.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Model Setup", "weight": 1.0} -->

Equivalently, the quadratic term induces the Gaussian reference For the discrete-time result, we work on the admissible class Finite relative entropy gives finite second moments; see Lemma E.25 ‣ E.1 Gaussian entropy, smoothing, and bounded perturbations ‣ Appendix E Standard analytic tools ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") in Appendix E.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Soft value functions and Bellman operators", "weight": 1.0} -->

Given a policy $\pi$, define the soft value function so that $J(\pi)=\int_{\mathcal{S}}V^{\pi}(s)\rho_{0}(\mathrm{d}s)$ whenever the integral is well-defined. Define the state-action value function Then $V^{\pi}$ satisfies the soft Bellman identity For a fixed policy $\pi$, define the policy evaluation operator acting on bounded measurable $V:\mathcal{S}\to\mathbb{R}$ by Under standard measurability and integrability conditions, $\mathcal{T}^{\pi}$ is a $\gamma$-contraction in $\|\cdot\|_{\infty}$ and its unique fixed point is $V^{\pi}=\mathcal{T}^{\pi}V^{\pi}$. For a bounded candidate value $V$, write Define the soft optimality operator by where the supremum ranges over action densities for which the expression is finite.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Soft value functions and Bellman operators", "weight": 1.0} -->

For each $(\pi,s)$, define the Gibbs density by The following identity relates the Bellman residual to the KL divergence between the current policy and the Gibbs density.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Wasserstein Policy Gradient", "weight": 1.0} -->

Fix a policy $\pi$. The first-variation calculation in Appendix A.2 shows that, for statewise transport perturbations of the action law, the ascent direction is The discounted occupancy $d^{\pi}$ enters this calculation through the usual policy-gradient weighting over states, as in the policy-gradient theorem and trust-region/natural-gradient policy methods. Taking the Wasserstein gradient of this first variation state by state gives the Wasserstein policy-gradient flow Using the Gibbs density $p_{s}^{\pi_{t}}$, this can be rewritten as From an equivalent particle viewpoint, for each fixed state $s$, the above Fokker--Planck equation can be viewed formally as the forward equation of the nonlinear Langevin diffusion Applying an explicit Euler--Maruyama step to this statewise Langevin diffusion gives the discrete-time update below.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Wasserstein Policy Gradient", "weight": 1.0} -->

The discrete-time counterpart of (WPGF) is the Langevin policy update where $A_{k}^{s}\sim\pi_{k}(\cdot\mid s)$ and Thus WPGD is a statewise policy-space update specified for every $s\in\mathcal{S}$. Under the full-support convention above, the discounted occupancy weighting does not remove any state from the gradient calculation, and the convergence theorem below controls the resulting value gap in sup-norm over the same state space.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Continuous-Time Analysis: Bellman Geometry", "weight": 1.0} -->

This section presents a formal continuous-time analysis of the Wasserstein policy gradient flow (WPGF). Its purpose is to make transparent the Bellman mechanisms that replace the standard mean-field Langevin dynamics proof chain. We do not claim here a complete well-posedness theorem for the nonlinear Fokker--Planck equation. Instead, the identities below are stated under a smooth-flow regularity convention that supplies the differentiability, integrability, and boundary-decay properties needed for the calculation.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Why the standard mean-field Langevin dynamics proof chain does not directly apply", "weight": 1.0} -->

For a mean-field Langevin dynamics problem, exponential convergence is often proved through the schematic chain: where (a) is the gradient-flow dissipation identity, (b) follows from a uniform LSI, and (c) is through a convex-analysis based comparison from local KL to global suboptimality. In entropy-regularized RL, these relationships do not hold in these forms. First, (a) is altered by the Bellman recursion: differentiating $V^{\pi_{t}}$ also differentiates $Q^{\pi_{t}}$ through the value function, so the value derivative is not merely a statewise Fisher-information dissipation. Lemma 3.4 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Why the standard mean-field Langevin dynamics proof chain does not directly apply", "weight": 1.0} -->

‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") replaces this step by the value-resolvent identity $(I-\gamma P^{\pi_{t}})\dot{V}^{\pi_{t}}=g_{t}$, with $g_{t}$ proportional to a statewise Fisher-information term. Second, (b) is not directly available from a convex functional, because the RL objective is nonconvex due to the Bellman recursion of the state-dependent policy distribution. Lemma 3.5 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") and 3.6 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") will derive a uniform LSI from uniform value/$Q$ bounds.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Why the standard mean-field Langevin dynamics proof chain does not directly apply", "weight": 1.0} -->

Third, (c) cannot be obtained from convexity due to the nonconvexity and aggregation over states in the RL objective. Instead, Lemma 2.1 ‣ 2.1 Soft value functions and Bellman operators ‣ 2 Model Setup ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") identifies $\tau\mathrm{KL}(\pi_{t}(\cdot\mid s)\|p_{s}^{\pi_{t}})$ with the statewise Bellman residual, and Bellman contraction in the proof of Theorem 3.7 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") will compare this residual at the worst state directly with the $\|\cdot\|_{\infty}$-value gap.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Why the standard mean-field Langevin dynamics proof chain does not directly apply", "weight": 1.0} -->

*Smooth-flow regularity convention.* Throughout this section only, the flow (WPGF) is considered for smooth positive solutions $\pi_{t}(\cdot\mid s)$ satisfying the following properties on every finite time interval. For each state $s$, $t\mapsto V^{\pi_{t}}(s)$ is locally absolutely continuous, the density $\pi_{t}(\cdot\mid s)$ has the moments, entropy, Fisher information, and decay at infinity needed for all displayed integrations by parts, and $a\mapsto Q^{\pi_{t}}(s,a)$ is sufficiently smooth. Differentiation under the action/state integrals is assumed valid. These assumptions are used only for the formal PDE calculation in this section for illustration and will not be used in the discrete-time analysis in Section 4.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 3.1 (Boundedness and initialization)", "weight": 1.0} -->

Our proof proceeds in three steps. First, we establish a resolvent identity for the value derivative along the flow (Lemma 3.4 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")), which reveals a dissipation given by Fisher information relative to the moving Gibbs family $p_{s}^{\pi_{t}}$ and yields monotone value improvement. Second, we use this monotonicity together with bounded rewards and the initialization condition to obtain uniform-in-time bounds on $V^{\pi_{t}}$ and $Q^{\pi_{t}}$ (Lemma 3.5 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 3.1 (Boundedness and initialization)", "weight": 1.0} -->

‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")); these bounds imply that each $p_{s}^{\pi_{t}}$ is a bounded perturbation of a Gaussian, enabling a uniform log-Sobolev inequality along the optimization trajectory via Holley-Stroock Perturbation Lemma (Lemma 3.6 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply. ‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")). Third, we combine the uniform LSI with the Bellman-residual identity, Lemma 2.1 ‣ 2.1 Soft value functions and Bellman operators ‣ 2 Model Setup ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"), and Bellman contraction to convert KL dissipation into an exponential-decay estimate for the optimality gap (Theorem 3.7 ‣ Why the standard mean-field Langevin dynamics proof chain does not directly apply.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 3.1 (Boundedness and initialization)", "weight": 1.0} -->

‣ 3 Continuous-Time Analysis: Bellman Geometry ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption 3.1 (Boundedness and initialization)", "weight": 1.0} -->

Note that RL policy differs from the standard mean-field Langevin dynamics in that it is concerned with a family of state-dependent policy distributions $\{\pi(\cdot\mid s)\}_{s\in\mathcal{S}}$ rather than a single distribution. Thus, adapting the usual proof chain to RL settings requires choosing how to aggregate statewise quantities. Another possible route is to aggregate the KL terms in (c) by a discounted state-visitation distribution via the performance difference lemma A.16 ‣ A.1 Entropy-Regularized Performance Difference Lemma ‣ Appendix A Auxiliary Results ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"), as in occupancy-weighted policy-gradient analyses. However, this creates a mismatch between the state distribution used to measure the optimality gap and the state aggregation naturally induced by the value derivative or resolvent identity in (a). Closing this gap typically requires density-ratio or coverage assumptions between state distributions.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption 3.1 (Boundedness and initialization)", "weight": 1.0} -->

Our argument above circumvents this route by keeping the Bellman residual identity statewise and using Bellman contraction to lower bound the residual in terms of the sup-norm value gap, and thus does not require additional coverage assumptions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption 3.1 (Boundedness and initialization)", "weight": 1.0} -->

For a policy $\pi$, define the induced state kernel

<!-- chunk {"id": "body-0036", "role": "body", "section": "Discrete-Time Global Convergence Analysis", "weight": 1.0} -->

This section proves the non-asymptotic convergence guarantee for the explicit Langevin update (WPGD). The continuous-time section isolates the Bellman residual/resolvent mechanism. Apart from their counterparts in discrete time, an additional task is to control the finite-step Langevin discretization and the policy-dependent drift uniformly along the iterates.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumptions", "weight": 1.0} -->

The assumptions below are the quantitative inputs for the finite-step analysis. To apply the one step drift interpolation argument, we need uniform control of the drift Lipschitz constants, action moments, drift second moments, finite KL quantities, and the LSI constants of the Gibbs family. Since these constants cannot be read off from the Wasserstein gradient of a static functional; they must be derived from the Bellman recursion and propagated along the WPG iterates. Assumptions 4.1 ‣ 4.1 Assumptions ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")-4.2 ‣ 4.1 Assumptions ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"), together with the a priori bounds that will be proved in Proposition 4.14 ‣ 4.2.2 Drift regularity and the discretization error ‣ 4.2 Proof sketch and main theorem ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning"), provide this uniform control.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption 4.1 (Bounded rewards and initialization)", "weight": 1.0} -->

For constants used later, set This quantity is finite by Lemma E.25 ‣ E.1 Gaussian entropy, smoothing, and bounded perturbations ‣ Appendix E Standard analytic tools ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") applied uniformly in $s$. In particular, applying that lemma with $c=\beta/(4\tau)$ and using Assumption 4.1 ‣ 4.1 Assumptions ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")(ii) gives

<!-- chunk {"id": "body-0039", "role": "body", "section": "Assumption 4.2 (Action regularity)", "weight": 1.0} -->

There is a $\sigma$-finite reference measure $\lambda$ on $\mathcal{S}$ such that $P(\mathrm{d}s^{\prime}\mid s,a)=p(s^{\prime}\mid s,a)\lambda(\mathrm{d}s^{\prime})$. There are finite constants $L_{r},L_{p},G_{r},G_{p}$ such that: For every $s\in\mathcal{S}$, the map $a\mapsto r(s,a)$ is continuously differentiable and For every $s\in\mathcal{S}$ and $\lambda$-a.e.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Assumption 4.2 (Action regularity)", "weight": 1.0} -->

$s^{\prime}\in\mathcal{S}$, the map $a\mapsto p(s^{\prime}\mid s,a)$ is continuously differentiable, and A concrete example satisfying the transition part of Assumption 4.2 ‣ 4.1 Assumptions ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning") is the following additive-noise model. Let $\mathcal{S}=\mathbb{R}^{m}$, let $\lambda$ be Lebesgue measure, and suppose where $\sigma\in\mathbb{R}^{m\times m}$ is invertible and $\zeta$ has a smooth density $q$. Write for the density of $\sigma\zeta$, and assume Assume further that, uniformly in $s$, satisfies Assumption 4.2 ‣ 4.1 Assumptions ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")(ii).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Assumption 4.2 (Action regularity)", "weight": 1.0} -->

Indeed, so one may take Nondegenerate Gaussian noise is a special case, since its first derivative and Hessian are integrable. Together with the reward condition in Assumption 4.2 ‣ 4.1 Assumptions ‣ 4 Discrete-Time Global Convergence Analysis ‣ Global Convergence of Wasserstein Policy Gradient for Entropy-Regularized Reinforcement Learning")(i), this gives a concrete class of controlled transition models covered by the theorem. Deterministic or degenerate-noise dynamics are not covered by this example.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Assumption 4.2 (Action regularity)", "weight": 1.0} -->

With these assumptions in place, write and define the current-policy Langevin drift The current-policy Gibbs stationarity condition is

<!-- chunk {"id": "body-0043", "role": "body", "section": "Bellman residual-to-optimality gap mechanism and uniform LSI", "weight": 1.0} -->

We first record the discrete counterparts of the residual and resolvent mechanisms from Section 3. They show that the KL to the current-policy Gibbs law is exactly the Bellman residual, that this residual controls the worst-state value gap, and that decreasing the same KL produces value improvement after applying the Bellman resolvent.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Drift regularity and the discretization error", "weight": 1.0} -->

We now control the finite-step error introduced by the Langevin discretization. As explained in Section 4.1, the drift Langevin interpolation requires uniform action-Lipschitz and dissipativity estimates for the policy-dependent drift. The following lemma converts the action-regularity assumptions and a value bound into those estimates.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We developed a convergence analysis framework for Wasserstein policy gradient in entropy-regularized discounted RL with continuous actions. The proof combines Bellman-residual identities, value-resolvent relation, one-step interpolation, uniform value/Q-function and moment bounds, and uniform LSI for the iterated Gibbs family. These ingredients yield exponential convergence for the continuous-time WPG flow and geometric convergence for the discrete-time WPG Langevin dynamics up to a discretization bias. An important direction for future work is to integrate these policy-space guarantees with practical approximations, such as projection onto parametric policy classes and finite-sample critic estimation.
