<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Second-Order Policy Gradient Methods for the Linear Quadratic Regulator

Topics include Policy gradients, Reinforcement learning, Control, Learning, Linear quadratic regulator, Gradient method.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Policy gradient methods are a powerful family of reinforcement learning algorithms for continuous control that optimize a policy directly. However, standard first-order methods often converge slowly. Second-order methods can accelerate learning by using curvature information, but they are typically expensive to compute. The linear quadratic regulator (LQR) is a practical setting in which key quantities, such as the policy gradient, admit closed-form expressions. In this work, we develop second-order policy gradient algorithms for LQR by deriving explicit formulas for both the approximate and exact Hessians used in Gauss-Newton and Newton methods, respectively. Numerical experiments show a faster convergence rate for the proposed second-order approach over the standard first-order policy gradient baseline.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimal control problems play a fundamental role in diverse domains of engineering and science, with applications ranging from robotics and autonomous systems to economic systems. The objective is typically to design a feedback policy that minimizes a long-term cost while satisfying the dynamics of the underlying system.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy gradient methods optimize parameterized policies via estimated performance gradients and scale to continuous, high-dimensional action spaces. Conventional policy gradient methods typically use first-order optimization, which yields linear convergence and sensitivity to step size choices under ill-conditioning. Incorporating curvature via the performance Hessian can accelerate convergence to superlinear or quadratic rates. In reinforcement learning, this idea appears in natural policy gradients, trust-region methods, and quasi-Newton policy gradients.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A natural next step is to employ exact Newton methods that use the full Hessian of the performance function. However, computing the exact Hessian is typically challenging. It involves not only local curvature of the action-value function but also sensitivity of state distributions to the policy parameters. This distributional term couples the policy with the dynamics, and evaluating it requires differentiating through the transition kernel and the value function, which can be computationally expensive in general settings.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The linear quadratic regulator (LQR) provides a fundamental and analytically tractable setting for studying reinforcement learning algorithms. In this model, the dynamics are linear and the cost is quadratic, which ensures that the optimal policy is a linear state feedback. Crucially, in the LQR framework many quantities of interest, such as the value function, policy gradient, and even higher-order derivatives, admit closed-form expressions. This analytical structure makes it possible to compute not only the Gauss--Newton approximation but also the exact performance Hessian explicitly, thereby enabling efficient implementation of Newton-type methods that would be prohibitively costly in general reinforcement learning problems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we develop a second-order policy gradient framework for the LQR with known system matrices. We build on the recently developed performance Hessian theorem in Kordabad et al., formulated for general systems, and specialize it to the discounted LQR setting. This enables us to derive explicit closed-form expressions for the exact Hessian of the performance function. Moreover, we show that the approximate Hessian resulting from this formulation coincides with the Gauss--Newton structure studied in the literature. These closed-form characterizations provide curvature-aware updates that can be computed efficiently in LQR.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. The main contributions of this paper are threefold: i) we prove that the Gauss--Newton (approximate) Hessian obtained from the general decomposition coincides with the classical LQR Gauss--Newton form; ii) we derive an explicit closed-form for the exact performance Hessian in discounted LQR under mild regularity assumptions, making exact Newton updates practical; and iii) we demonstrate on benchmarks that these second-order methods improve the convergence rate and stability over first-order policy gradient.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Outline. The paper is organized as follows: Section 2 introduces the discounted LQR setup, notation, and the recent second-order policy gradient theorem we build upon. Section 3 derives closed-form expressions for the policy gradient, the Gauss--Newton Hessian, and the exact Hessian in the LQR setting. Section 4 presents a scalar analytical example and numerical experiments illustrating the convergence properties of the proposed methods. Finally, Section 5 concludes and outlines directions for future work.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $e_{m,i} \in {\mathbb{R}}^{m}$ and $e_{n,j} \in {\mathbb{R}}^{n}$ denote the $i$-th and $j$-th standard basis vectors, respectively (see e.g., Magnus and Neudecker ).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Assumption 1 (Regularity)", "weight": 1.0} -->

One can verify that for discounted LQR with dynamics, cost, and linear policy, the regularity conditions assumptions in Assumption 1 ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator") hold automatically. We next state the policy-gradient theorem and the associated Hessian decomposition.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Gradient and Hessian for LQR", "weight": 1.0} -->

A central contribution of this work is the evaluation of the general policy Hessian framework stated in Theorem 1 ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator") for the LQR problem. Leveraging the analytical structure of the LQR, we obtain an explicit, structured, and computationally tractable representation of the second-order policy gradient. This explicit characterization goes beyond the abstract formulations available in the general setting and provides novel theoretical insights into the geometry of the policy optimization landscape. We first state the differential identities for $Q_{\theta}$ and $\pi_{\theta}$ required in Theorem 1 ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator"). For $Q_{\theta}$,

<!-- chunk {"id": "body-0013", "role": "body", "section": "Gradient and Hessian for LQR", "weight": 1.0} -->

and for the linear policy, we obtain

<!-- chunk {"id": "body-0014", "role": "body", "section": "Gradient and Hessian for LQR", "weight": 1.0} -->

These equations provide all ingredients for substitution into (11a ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator"))--(11b ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Policy Gradient in LQR", "weight": 1.0} -->

We now evaluate the policy gradient (10a ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")) for the LQR setting. Substituting the action and policy derivatives from (12a) and yields

<!-- chunk {"id": "body-0016", "role": "body", "section": "Policy Gradient in LQR", "weight": 1.0} -->

Matrix $\Sigma_{\theta}$ is the discounted state second-moment matrix under policy $\pi_{\theta}$ and is defined as,

<!-- chunk {"id": "body-0017", "role": "body", "section": "Policy Gradient in LQR", "weight": 1.0} -->

This is the discounted state correlation matrix, also called the discounted state-occupancy measure. The next lemma gives a closed form characterization of $\Sigma_{\theta}$ for discounted LQR.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Quasi-Newton Policy Gradient in LQR", "weight": 1.0} -->

We derive an approximation of the Hessian of the performance function for discounted LQR by adapting the *general* second-order formulations (11a ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")). From (11a ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")), and since ${{\nabla_{\theta}^{2}\pi_{\theta}}{(s)}} = 0$ for linear policies, the first term vanishes.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Quasi-Newton Policy Gradient in LQR", "weight": 1.0} -->

using the Kronecker mixed-product rule.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Most Gauss--Newton LQR derivations treat deterministic, *undiscounted* LQR. Here we instantiate (11a ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")) for $\gamma \in {}$ with nonzero additive noise. When $\gamma\rightarrow 1$, applying to recovers the classical update along with standard convergence guarantees. Thus, the treatment both extends discounted stochastic LQR and unifies with established formulations.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Exact Hessian in LQR", "weight": 1.0} -->

To leverage second-order methods beyond Gauss--Newton, one must capture the state distribution gradients with respect to the policy parameters in (10b ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")). In general RL this coupling is what makes exact Newton steps impractical. Our key insight is that, for discounted LQR, this coupling admits an explicit form with modest assumptions on the disturbance.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Exact Hessian in LQR", "weight": 1.0} -->

We begin with a mild regularity requirement ensuring that boundary contributions vanish when differentiating through the transition kernel. This condition is satisfied by essentially most of the distributions used in control, including Gaussian and sub-Gaussian distributions.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 2 (Vanishing boundary flux)", "weight": 1.0} -->

Under Assumption 2 ‣ 3.3 Exact Hessian in LQR ‣ 3 Gradient and Hessian for LQR ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator"), boundary terms vanish, yielding a closed-form transition contribution to the policy Hessian. The assumption holds for standard disturbances (see remark 2). With this assumption and the regularity conditions of Theorem 1 ‣ 2 Preliminaries and Background ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator"), the exact Hessian admits a closed form in LQR.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Analytical Example and Simulations", "weight": 1.0} -->

We first analyze a one-dimensional instance to validate the derivations. We next present numerical experiments on two benchmarks: an inverted-pendulum linearization and a high-dimensional seismic shear-building model, both with strongly anisotropic objective landscapes. Numerical results demonstrate the advantages of exact second-order information for Newton-type policy optimization, with and without line search.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Analytical example: scalar LQR", "weight": 1.0} -->

Consider the following scalar discounted LQR

<!-- chunk {"id": "body-0026", "role": "body", "section": "Analytical example: scalar LQR", "weight": 1.0} -->

Invoking (20 ‣ 3.3 Exact Hessian in LQR ‣ 3 Gradient and Hessian for LQR ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")), the derivative of $P_{\theta}$ with respect to $\theta$ is

<!-- chunk {"id": "body-0027", "role": "body", "section": "Analytical example: scalar LQR", "weight": 1.0} -->

Using, the policy gradient in one dimension is

<!-- chunk {"id": "body-0028", "role": "body", "section": "Analytical example: scalar LQR", "weight": 1.0} -->

Likewise the quasi-Hessian in one dimension is

<!-- chunk {"id": "body-0029", "role": "body", "section": "Analytical example: scalar LQR", "weight": 1.0} -->

Using (19 ‣ 3.3 Exact Hessian in LQR ‣ 3 Gradient and Hessian for LQR ‣ Second-Order Policy Gradient Methods for the Linear Quadratic Regulator")), the transition contribution to the Hessian is

<!-- chunk {"id": "body-0030", "role": "body", "section": "Analytical example: scalar LQR", "weight": 1.0} -->

Moreover, differentiate once more to obtain the exact Hessian analytically

<!-- chunk {"id": "body-0031", "role": "body", "section": "Analytical example: scalar LQR", "weight": 1.0} -->

where $H{(\theta)}$ and $\Lambda{(\theta)}$ are given in and, respectively. This confirms that the derived expressions for $H{(\theta)}$ and $\Lambda{(\theta)}$ correctly recover the exact Hessian in one dimension. One can verify that the result in Kordabad et al. is a special case of this derivation with $a = b = 1$ and $Q = R = 0.5$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Inverted Pendulum Control", "weight": 1.0} -->

We study the discretization of the upright linearization of a planar inverted pendulum. The dynamics are in the form of with $A$ and $B$ given as

<!-- chunk {"id": "body-0033", "role": "body", "section": "Inverted Pendulum Control", "weight": 1.0} -->

where $g = {{9.81m}/s^{2}}$ is the gravitational constant, $l = {1m}$ is the pendulum length, and $m = {1{kg}}$ is the mass. Process noise is i.i.d. Gaussian with covariance $\Sigma_{w} = I_{2}$, and the initial state covariance is $\Sigma_{0} = {0.1I_{2}}$. Performance is evaluated under an infinite-horizon discounted cost with discount factor $\gamma = 0.9$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Inverted Pendulum Control", "weight": 1.0} -->

The state penalty is strongly anisotropic with eigenvalues ${(\lambda_{1},\lambda_{2})} = {(10^{5},10^{- 4})}$ rotated by $\psi = 40^{\circ}$, implemented via $Q = {C{diag}{(\lambda_{1},\lambda_{2})}C^{\mathsf{T}}}$ where $C$ is the rotation matrix. The input penalty is $R = 0.1$. Policy gradient schemes are initialized at a common stabilizing gain $K_{0}$ computed with dlqr. Step sizes are selected by backtracking line search. Figure 1 displays the discounted LQR objective $J{(\theta)}$ with parameters $(\theta_{1},\theta_{2})$ slice with the corresponding trajectories. Newton follows the rotated, anisotropic valley to the optimal solution in a few steps, whereas the first order policy gradient oscillates, highlighting the benefit of curvature information.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Inverted Pendulum Control", "weight": 1.0} -->

Curvature-based preconditioning aligns updates with principal directions, yielding larger per-iteration decreases in $J{(\theta)}$ and more stable iterates.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Seismic Shear-Building Benchmark", "weight": 1.0} -->

We evaluate a multi-story shear-building benchmark under base excitation. The stacked state is $s_{k} = {\lbrack q_{k}^{\mathsf{T}},{\overset{˙}{q}}_{k}^{\mathsf{T}}\rbrack}^{\mathsf{T}} \in {\mathbb{R}}^{48}$ with interstory displacements $q_{k} \in {\mathbb{R}}^{24}$ and velocities ${\overset{˙}{q}}_{k} \in {\mathbb{R}}^{24}$. The control input $a_{k}$ applies base actuation. A discrete-time model of the form is obtained by first-order augmentation and zero-order-hold discretization with $T_{s} = {0.01s}$; see A.C. Antoulas and Gugercin for the resulting matrices.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Seismic Shear-Building Benchmark", "weight": 1.0} -->

where $V \in {\mathbb{R}}^{48 \times 48}$ is a orthogonal basis, $0 < \lambda_{lo} \ll \lambda_{hi}$ and $R = 0.01$. The initial stabilizing gain $K_{0}$ is computed using dlqr. Step sizes are set to $\alpha_{GN} = 0.5$ for Gauss--Newton, in accordance with convergence results in Fazel et al., and to $\alpha_{N} = 1$ for Newton, selected by a single tuning pass and then kept constant. Figure 2 reports ${\|{K_{k} - K^{\star}}\|}_{F}$ as a function of the iteration index. The plot indicates that Newton achieves quadratic local convergence, while Gauss--Newton attains superlinear rates, both substantially outperforming first-order policy gradient.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We presented a curvature-aware policy optimization framework for discounted stochastic LQR that yields explicit formulas for both the Gauss--Newton surrogate and the exact performance Hessian. The surrogate coincides with the classical LQR Gauss--Newton matrix; the exact Hessian augments it with a distributional term evaluable under mild boundary conditions. Future work includes model-free curvature estimation (actor--critic, off-policy) with finite-sample guarantees and robust under model uncertainty.
