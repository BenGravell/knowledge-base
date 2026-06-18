<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Variance-Reduced Model Predictive Path Integral via Quadratic Model Approximation

Topics include Benchmarks, Online algorithms, Sampling-based methods, Optimization, Control, Sampling, Model predictive path integral, Model predictive path integral control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sampling-based controllers, such as Model Predictive Path Integral (MPPI) methods, offer substantial flexibility but often suffer from high variance and low sample efficiency. To address these challenges, we introduce a hybrid variance-reduced MPPI framework that integrates a prior model into the sampling process. Our key insight is to decompose the objective function into a known approximate model and a residual term. Since the residual captures only the discrepancy between the model and the objective, it typically exhibits a smaller magnitude and lower variance than the original objective. Although this principle applies to general modeling choices, we demonstrate that adopting a quadratic approximation enables the derivation of a closed-form, model-guided prior that effectively concentrates samples in informative regions. Crucially, the framework is agnostic to the source of geometric information, allowing the quadratic model to be constructed from exact derivatives, structural approximations (e.g., Gauss- or Quasi-Newton), or gradient-free randomized smoothing. We validate the approach on standard optimization benchmarks, a nonlinear, underactuated cart-pole control task, and a contact-rich manipulation problem with non-smooth dynamics.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Across these domains, we achieve faster convergence and superior performance in low-sample regimes compared to standard MPPI. These results suggest that the method can make sample-based control strategies more practical in scenarios where obtaining samples is expensive or limited.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Formulating control, estimation, and motion planning as optimization problems has become a standard paradigm in automatic control and robotics. Traditionally, these problems are posed in their primal form: one seeks a single optimal configuration or trajectory $x^{\ast}$ that minimizes a cost function $f{(x)}$. Standard approaches to solving this problem, such as gradient descent or Newton's method, rely on local first- or second-order information. While efficient, these methods assume $f$ is smooth and can converge to local minima when $f$ is non-convex. To overcome these limitations, an alternative viewpoint elevates the problem to the *space of probability measures*. Here, the objective is to minimize the expected cost under a distribution $\mu$. This measure-theoretic formulation unifies several powerful frameworks in global optimization, stochastic control, and sampling-based motion planning.\

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Within this distributional approach, two complementary families of methods have emerged. The first relies on convex relaxations of the infinite-dimensional measure optimization problem. Lasserre's Moment--Sum-of-Squares (SOS) hierarchy, and its algebraic counterpart by Parrilo, provides a systematic sequence of semidefinite programming (SDP) relaxations whose solutions converge to the global optimum under mild regularity assumptions. These methods offer strong theoretical guarantees but remain limited in practice as the size of the SDPs grows rapidly with the dimensionality and polynomial degree of the underlying problem. Recent extensions, such as KernelSOS, address these limitations by replacing polynomial bases with reproducing kernels, enabling the treatment of non-polynomial objectives and infinite-dimensional function spaces. While such approaches significantly broaden the expressive power of SOS relaxations, they still require solving large-scale SDPs, which makes real-time use in high-frequency control loops impractical.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The second family originates from information-theoretic or KL-regularized formulations of stochastic optimal control. Here, the optimal control distribution is expressed as a Boltzmann distribution over trajectories, obtained by introducing an entropy or KL penalty on the control. This reformulation naturally leads to sampling-based algorithms, most notably the Model Predictive Path Integral (MPPI) control algorithm. MPPI offers compelling practical advantages: it is derivative-free, accommodates non-smooth costs (e.g., contact events), and parallelizes efficiently on modern hardware accelerators. However, unlike convex relaxation methods, MPPI approximates the optimal distribution via Monte Carlo sampling, which introduces a central challenge: high estimator variance. Standard isotropic sampling fails to adapt to landscape geometry, resulting in poor sample efficiency and slow convergence in high-dimensional spaces. While recent work has shown that incorporating curvature information by reconstructing local Jacobians and performing Gauss--Newton updates can partially mitigate these effects, such approaches remain in a high-sample regime. Consequently, state-of-the-art implementations often rely on thousands of parallel rollouts to achieve stable performance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Variance reduction is a well-studied topic in broader stochastic optimization. CMA-ES and the Cross-Entropy Method adapt covariance matrices based on elite samples, while classical techniques like importance sampling, control variates, or baseline subtraction in reinforcement learning, explicitly target variance reduction in Monte-Carlo estimators. Similar ideas appear in large-scale stochastic optimization, where variance-reduced gradient methods and curvature-aware updates are known to accelerate convergence.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Across domains, incorporating structural information consistently improves the efficiency of noisy estimators. This suggests that similar ideas may also benefit sampling-based control. Yet, unlike many large-scale optimization settings, real-time control imposes strict computational budgets, forcing algorithms to operate in a low-sample regime. These observations raise an important question: *Can we retain the flexibility of sampling-based control while achieving faster convergence with significantly fewer samples?*\

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we introduce a hybrid approach that guides sampling using a local model of the objective function, thereby accelerating the overall convergence of MPPI-based methods. Our main contributions are as follows: (i) we derive a variance-reduced MPPI framework by decomposing the objective into a known model and a residual term, (ii) we propose a specific instantiation using a quadratic model approximation, deriving a closed-form, model-guided proposal distribution, (iii) we show that this quadratic model can be computed via either exact derivatives, structural approximations, or a gradient-free randomized smoothing scheme, and (iv) we validate the approach numerically, showing superior convergence in low-sample regimes compared to standard baselines.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows. Section II formalizes the optimization problem and the standard MPPI derivation. Section III details the derivation of the quadratic model approximation. Section IV presents the numerical results, and Section V concludes the paper.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Methodology", "weight": 1.0} -->

Sampling-based control methods like MPPI offer substantial flexibility but often suffer from high variance and low sample efficiency. To address these limitations, we propose a hybrid MPPI approach that incorporates geometric information into the sampling process via a local approximation of the objective function. The key insight is to decompose the objective into an approximate model term and a residual term. The resulting model-based information biases the sampling distribution toward informative regions, reducing the variance of the underlying gradient estimators and thereby accelerating convergence relative to the classic MPPI updates. The remainder of this section details the formulation, the construction of the approximation, and stability mechanisms.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Model-guided distribution update", "weight": 1.0} -->

Consider the problem of finding the optimal distribution $p^{\ast}{(x)}$ at iteration $k + 1$, given a prior estimate $p_{\theta^{k}}{(x)}$ obtained at iteration $k$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Model-guided distribution update", "weight": 1.0} -->

At iteration $k$, we decompose the objective function $f$ into a model $m^{k}$ and a residual term $r^{k}$, such that ${f{(x)}} = {{m^{k}{(x)}} + {r^{k}{(x)}}}$. Here, $m^{k}$ acts as a control variate intended to capture the dominant landscape geometry, while $r^{k}$ accounts for unmodeled discrepancies.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Model-guided distribution update", "weight": 1.0} -->

Equation reveals a fundamental separation of concerns. The term in brackets, called model-guided prior, combines the previous prior with the explicit model to form a new intermediate distribution, which we denote as the *model-guided prior* ${\overset{\sim}{p}}_{\theta^{k}}{(x)}$. Rather than sampling from an uninformative prior and weighing by the full complex objective $f$ as done classically in MPPI-based approaches, we sample from the structurally informed ${\overset{\sim}{p}}_{\theta^{k}}$ and weight only by the residual $r^{k}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Model-guided distribution update", "weight": 1.0} -->

Importantly, this formulation is valid for *any* choice of model. This generality offers a powerful degree of freedom: we can design $m^{k}$ such that the resulting model-guided prior ${\overset{\sim}{p}}_{\theta^{k}}$ admits a closed-form solution. By selecting a model structure compatible with the prior, we ensure that the new sampling distribution remains analytically tractable.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Closed-form model-guided prior via quadratic model approximation", "weight": 1.0} -->

Input: Initial mean ${\overline{x}}^{0}$ and covariance Σ0, samples N, temperature λ
// 1. Construct quadratic model analytically or via RS using Eq.,
Obtain gradient gk and hessian Hk
// 2. Compute guided prior using Eq.,
Compute guided covariance ${\overset{\sim}{\Sigma}}^{k}$ and mean ${\overset{\sim}{x}}^{k}$

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B Closed-form model-guided prior via quadratic model approximation", "weight": 1.0} -->

Algorithm 1 MPPI with Quadratic Model

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Closed-form model-guided prior via quadratic model approximation", "weight": 1.0} -->

To derive an efficient closed-form algorithm, we instantiate the general framework using Gaussian approximations. We assume the current estimate is a Gaussian distribution ${p_{\theta^{k}}{(x)}} = {\mathcal{N}{(\left. x \middle| {{\overline{x}}^{k},\Sigma^{k}} \right.)}}$ parametrized by $\theta^{k} = {\{{\overline{x}}^{k},\Sigma^{k}\}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Closed-form model-guided prior via quadratic model approximation", "weight": 1.0} -->

where $g^{k}$ and $H^{k}$ denote the gradient and Hessian parameters at the expansion point, see Sec. III-C for details. Since the product of a Gaussian PDF and the exponential of a quadratic function is itself a Gaussian, the model-guided prior ${\overset{\sim}{p}}_{\theta^{k}}$ derived in remains in the Gaussian family. We can therefore solve for its parameters ${\overset{\sim}{\theta}}^{k} = {\{{\overset{\sim}{x}}^{k},{\overset{\sim}{\Sigma}}^{k}\}}$ analytically. The guided prior ${{\overset{\sim}{p}}_{\theta^{k}}{(x)}} = {\mathcal{N}{(\left.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Closed-form model-guided prior via quadratic model approximation", "weight": 1.0} -->

To guarantee a valid positive-definite covariance matrix ${\overset{\sim}{\Sigma}}^{k}$, appropriate regularization or convexification is applied to $H^{k}$ whenever it is indefinite.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Closed-form model-guided prior via quadratic model approximation", "weight": 1.0} -->

Interestingly, this reformulation naturally lends itself to applying MPPI on the residual function $r^{k}$ while sampling trajectories ${\{ x^{(i)}\}}_{i = 1}^{N}$ from the model-guided prior ${\overset{\sim}{p}}_{\theta^{k}}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Closed-form model-guided prior via quadratic model approximation", "weight": 1.0} -->

Compared to vanilla MPPI, which samples directly from $p_{\theta}^{k}$, this model-guided approach fundamentally alters the update mechanism. First, the analytical shift to ${\overset{\sim}{p}}_{\theta^{k}}$ integrates geometry information, blending the prior mean ${\overline{x}}^{k}$ with a Newton-like step derived from the model $m^{k}$. Second, the sampling process is reserved for exploring the residual error $r^{k}$ around this new center, rather than exploring the full cost $f$. This procedure is summarized in Algorithm 1.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Quadratic model approximations", "weight": 1.0} -->

To implement the update rules above, we require $g^{k}$ and $H^{k}$ to construct the model. A strength of the proposed framework is that it decouples the sampling mechanism from the source of geometric information, allowing the practitioner to select the most appropriate approximation strategy based on the available computational budget and problem structure.\

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C Quadratic model approximations", "weight": 1.0} -->

Analytical second-order approximations. If $f$ is differentiable and smooth, $g^{k}$ and $H^{k}$ can be exact analytical derivatives. In this exact *local model*, the resulting guided prior ${\overset{\sim}{p}}_{\theta^{k}}$ acts as a precise local Newton step. This maximizes convergence speed near the optimum but risks guiding the sampling distribution into shallow local minima if the current estimate is far from the global solution.\

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Quadratic model approximations", "weight": 1.0} -->

Gauss-Newton approximations. Beyond exact derivatives, our framework accommodates strategies that exploit specific problem structures. For instance, many control objectives are formulated as non-linear least-squares problems: ${f{(x)}} = {\frac{1}{2}{\|{R{(x)}}\|}^{2}}$, where residual $R{(x)}$ stacks error terms such as state deviations and control penalties. In such cases, the Hessian can be approximated via the Gauss-Newton approximation as $H^{k} \approx {J{(x)}^{\top}J{(x)}}$, where $J{(x)}$ is the Jacobian of $R{(x)}$. This avoids computing the full Hessian while ensuring a positive-semidefinite approximation that seamlessly integrates into our quadratic model update. Recent work can be viewed as an instantiation of this principle, in which curvature information is reconstructed from black-box residuals via randomized smoothing.\

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Quadratic model approximations", "weight": 1.0} -->

Quasi-Newton approximations. Similarly, when second-order information is prohibitively expensive or unavailable, one can employ Quasi-Newton methods such as BFGS or L-BFGS. These techniques iteratively build a curvature estimate $H^{k}$ from only a history of gradient updates, enabling our model-guided framework to be applied in settings where only first-order derivatives are available.\

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Quadratic model approximations", "weight": 1.0} -->

Randomized smoothing approximations. In the most general case where $f$ is non-smooth or black-box, we employ Randomized Smoothing (RS) to estimate the model parameters. This allows us to recover zeroth-order estimators for the gradient and Hessian using only function evaluations. While RS is a general framework compatible with various smoothing distributions, we use a Gaussian kernel in this work. This defines the smoothed surrogate as the Gaussian convolution ${f_{\sigma}{(x)}} = {{\mathbb{E}}_{z \sim {\mathcal{N}{(0,{\sigma^{2}I})}}}{\lbrack{f{({x + z})}}\rbrack}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-C Quadratic model approximations", "weight": 1.0} -->

With a small noise scale ($\sigma\rightarrow 0$), the smoothed surrogate $f_{\sigma}$ closely approximates the original objective $f$. The estimators, capture fine-scale curvature information, behaving similarly to analytical derivatives. We refer to this as the *fine model* (Fig. 2b). As $\sigma$ increases, RS aggregates objective information over larger neighborhoods around the current iterate. The gradient and Hessian are based on global structure rather than local details, allowing the algorithm to step over small obstacles that might trap a local optimizer. We refer to this as the *coarse model* (Fig. 2a). The induced quadratic approximation biases the guided prior toward regions that appear promising under wider exploratory variations, encouraging exploration while filtering out fine local structure.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-D Incremental update formulation", "weight": 1.0} -->

Although formulated above in terms of full iterations, the update mechanism can equivalently be expressed in terms of incremental steps. Consider a perturbation $\epsilon$ such that $x = {{\overline{x}}^{k} + \epsilon}$. A second-order expansion of the objective yields

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-D Incremental update formulation", "weight": 1.0} -->

where the quadratic terms define the local model $m^{k}$ and $r^{k}$ accounts for unmodeled effects. As in Sec. III-B, combining the quadratic model with the $k$-th Gaussian exploration prior ${p{(\epsilon)}} = {\mathcal{N}{(0,\Sigma_{0k})}}$ induces a guided Gaussian distribution

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-D Incremental update formulation", "weight": 1.0} -->

where ${\overset{\sim}{\delta}}^{k}$ represents the model-guided incremental update step mean. As before, we regularize $H^{k}$ if necessary to ensure ${\overset{\sim}{\Sigma}}^{k}$ is positive-definite. The optimal update step distribution is then obtained by reweighting this guided Gaussian by the residual,

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-D Incremental update formulation", "weight": 1.0} -->

This is the direct update-step analogue of the iterate-level distribution. Yet, this formulation choice exposes the prior covariance $\Sigma_{0k}$ as a tunable parameter in the algorithm design, a feature that will be exploited in the next section III-E to adequately control the variance.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-D Incremental update formulation", "weight": 1.0} -->

Since $p^{\ast}$ is available only up to a normalizing constant, we estimate this expectation via self-normalized importance sampling using ${\overset{\sim}{p}}_{\theta^{k}}$ as the proposal.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-E Stability and variance control of the model-guided prior", "weight": 1.0} -->

While the update rules in and directly incorporate curvature, they can lead to variance collapse since they can only decrease variance. In regions where the Hessian $H^{k}$ has large positive eigenvalues, the resulting guided covariance ${\overset{\sim}{\Sigma}}^{k}$ may shrink excessively, hindering the exploration required to resolve the residual $r^{k}$. To mitigate this, we use regularization strategies that ensure stability and maintain a minimum exploration width.\

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-E Stability and variance control of the model-guided prior", "weight": 1.0} -->

Polyak/Juditsky averaging. To smooth the evolution of the sampling distribution and prevent abrupt jumps caused by noisy gradient or Hessian estimates, we apply exponential moving averages to the model-guided parameters.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-E Stability and variance control of the model-guided prior", "weight": 1.0} -->

Variance control. While the above averaging acts as a temporal filter, it does not guarantee a lower bound on the variance. To strictly prevent collapse, we use a scaling strategy that regulates the distribution's magnitude while preserving its geometry. By applying a scalar gain, we maintain the anisotropic structure (eigenvectors and relative aspect ratios) derived from the Hessian, ensuring the sampling ellipsoid remains aligned with the landscape curvature even when inflated to a safe minimum volume.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-E Stability and variance control of the model-guided prior", "weight": 1.0} -->

We derive the required input noise $\sigma_{0k}^{2}$ by analyzing the covariance update in the principal directions of the local curvature. Starting from the update rule in Eq.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-E Stability and variance control of the model-guided prior", "weight": 1.0} -->

Since $H^{k}$ is symmetric, we can analyze the update along its principal axes. Let $\kappa_{i}$ denote the eigenvalues of $H^{k}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-E Stability and variance control of the model-guided prior", "weight": 1.0} -->

We see that the variance is most compressed in the direction of maximum positive curvature.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-E Stability and variance control of the model-guided prior", "weight": 1.0} -->

This ensures that the sampling distribution maintains a desired width in the most constrained direction, thereby guaranteeing that variance in all other directions exceeds the threshold without distorting the curvature information.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments", "weight": 1.0} -->

We investigate how incorporating a quadratic model into MPPI affects convergence speed, solution quality, and robustness in low-sample regimes. In particular, we study how the *locality* and *fidelity* of the quadratic model approximation $m^{k}$ influence performance. To isolate specific algorithmic properties, we consider problems with increasing difficulty. We begin with static optimization benchmarks to validate the core optimization mechanism. Then, we examine continuous control in the context of cart-pole control, a smooth but underactuated, nonlinear dynamical system, exploiting analytical derivatives and assessing the performance of Gauss-Newton and Quasi-Newton approximations. Finally, we aim to evaluate robustness to non-smooth dynamics (Single-Finger Sphere Manipulation) in contact-rich scenarios using randomized smoothing.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

As baselines, we consider (i) vanilla MPPI, which samples from a fixed Gaussian prior and evaluates trajectories using the objective $f$, without exploiting any explicit local structure, and (ii) CMA-ES, implemented using the pycma Python library, a state-of-the-art derivative-free optimizer that adapts a full covariance matrix. We compare this against several model-guided MPPI variants that adopt the incremental update formulation and differ only in how the quadratic approximation in is constructed.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our experiments highlight three different key effects of model guidance: (i) accelerated and more accurate convergence when reliable analytical information is available, (ii) increased robustness in low-sample regimes, where purely sampling-based methods suffer from weight degeneracy, and (iii) the complementary roles of coarse and fine quadratic models in capturing global structure versus local precision.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-A Illustration of quadratic model guidance", "weight": 1.0} -->

We first show the mechanism on a 2D narrow-valley objective illustrated in Fig. 1. This visualizes how second-order information reshapes the sampling distribution to align with the cost geometry. By effectively performing a Newton-like update for the distribution mean, Model-Guided MPPI concentrates samples in high-probability regions.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-A Illustration of quadratic model guidance", "weight": 1.0} -->

To evaluate sample quality, we use the effective sample size (ESS), a standard diagnostic for importance sampling that quantifies the weight degeneracy induced by the sampling distribution.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A Illustration of quadratic model guidance", "weight": 1.0} -->

The ESS measures the number of effectively contributing samples; larger values indicate lower variance in the importance weights. In the context of MPPI, a higher ESS corresponds to more informative samples. Using the same parameters ($N = 100$, $\lambda = 0.1$, $\sigma = 0.2$) in Fig. 1, vanilla MPPI collapses to an ESS of $1.1$, indicating severe weight degeneracy. In contrast, our method maintains an ESS of $23.4$, demonstrating efficient coverage of the relevant state space.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B Performance with analytical gradients", "weight": 1.0} -->

We first validate the method in a setting where exact gradient and Hessian information are available. Here, the quadratic model $m^{k}$ accurately captures local curvature for smooth functions, allowing us to isolate and analyze the benefits of the update rule from errors in gradient estimation.\

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-B Performance with analytical gradients", "weight": 1.0} -->

Static benchmarks. Tab. I reports the number of iterations required by each method to reach the global optimum within a specified infinity-norm distance using $100$ samples. Initializations were set to ${\overline{x}}^{0} = {}$ (Rosenbrock, Styblinski--Tang), $(2.0,2.0)$ (Ackley), and $(1.9,1.7)$ (Rastrigin). The results confirm the efficacy of the model guidance: our framework consistently converges faster than the baselines and, crucially, exhibits lower variance across the 100 random seeds. For instance, on the Rastrigin benchmark, we achieve a tight convergence distribution ($3.0 \pm 1.1$ iterations), whereas Vanilla MPPI ($6.9 \pm 6.4$) and CMA-ES ($5.5 \pm 4.6$) display higher volatility, reflecting their sensitivity to the stochasticity of the sampling process.\

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-B Performance with analytical gradients", "weight": 1.0} -->

Continuous control. To assess our method on a continuous control problem, we consider a nonlinear, underactuated cart-pole swing-up task with a horizon length of $2.5s$ and a time step of $50{ms}$. The objective is formulated as a finite-horizon trajectory optimization problem over a sequence of continuous controls.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-B Performance with analytical gradients", "weight": 1.0} -->

(a) Convergence speed. Median distance to the Newton-optimal solution over iterations. Shaded areas indicate the interquartile range (IQR) over 20 seeds.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-B Performance with analytical gradients", "weight": 1.0} -->

(b) Variance analysis in low-sample regime. Box-plot of the final distance to the optimum after 1000 iterations. The log-scale highlights the variance and error increase for baselines when N &lt; 64.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-B Performance with analytical gradients", "weight": 1.0} -->

We leverage open-source tools to implement the cart-pole dynamics and cost function using the Pinocchio library, and CasADi. This provides access to exact analytical expressions for the trajectory cost, its gradient, and Hessian with respect to the control sequence through automatic differentiation. As a reference for the true optimum over the given horizon and discretization, we compute a locally optimal control sequence using a Newton solver with a line search.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-B Performance with analytical gradients", "weight": 1.0} -->

We evaluate convergence behavior across a wide range of sampling budgets $N \in {\{ 2,\ldots,1024\}}$ in Fig. 3. In the high-sample regime ($N = 1024$), both CMA-ES and Model-Guided MPPI converge rapidly to the optimum ($< 10^{- 4}$ error), whereas Vanilla MPPI requires significantly more iterations. However, the baselines are sensitive as the number of samples is reduced. Vanilla MPPI exhibits increasingly slow convergence and high variance, while CMA-ES becomes unstable below $N = 64$. In contrast, our method demonstrates sample invariance by leveraging an analytical quadratic model to effectively decouple performance from the sampling budget. As shown in Fig. 3(a), the convergence trajectories from $N = 2$ to $1024$ collapse onto a single curve. Fig. 3(b) further quantifies this robustness: while the baselines suffer from large variance in the low-sample regime, Model-Guided MPPI maintains negligible variance and consistent high-precision convergence even with as few as $N = 2$ samples.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-B Performance with analytical gradients", "weight": 1.0} -->

This confirms that when reliable second-order information is available, the quadratic model successfully guides optimization, reducing reliance on massive parallel rollouts.\

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-B Performance with analytical gradients", "weight": 1.0} -->

Hessian approximations. While the previous results leverage exact analytical Hessians, we now investigate the impact of approximation quality. Following the strategies in Sec. III-C, we compare the exact local model against Gauss-Newton (GN), iterative BFGS approximations, and an Adam-based approximation (interpreting the second moment as a diagonal Hessian), alongside a vanilla MPPI baseline on the same cart-pole task using $8$ samples.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-B Performance with analytical gradients", "weight": 1.0} -->

As shown in Fig. 4, the fidelity of the curvature information is critical. While the Adam-based model-guidance improves upon the baseline, its diagonal approximation proves insufficient to achieve high precision. In contrast, variants that capture dense curvature information, such as exact, GN, or BFGS, achieve high-precision convergence. Notably, the GN approximation exploits the least-squares structure of the cost and closely matches the analytical Hessian. The BFGS variant, despite relying solely on iterative gradient updates, maintains a similar trajectory for most of the optimization, with only a minor performance gap emerging as it approaches the higher-precision regime ($< 10^{- 3}$).

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-C Coarse and fine quadratic model approximations", "weight": 1.0} -->

We next evaluate how the locality of the quadratic model, controlled by the smoothing scale, affects performance on nonconvex objectives. To build intuition, we consider a one-dimensional illustrative example in Fig. 2, in which the convex objective is corrupted by sinusoidal noise. Here, the trade-off becomes visible: a coarse model (large $\sigma$) filters out high-frequency perturbations to recover the dominant global geometry. This prevents the optimizer from being trapped in local minima and guides exploration toward the correct basin of attraction. Once the iterate is in the vicinity of the optimum, a fine model (small $\sigma$) is used to resolve accurate local curvature for high-precision convergence.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-C Coarse and fine quadratic model approximations", "weight": 1.0} -->

This intuition extends to higher-dimensional challenges, such as the Rastrigin function with initial guess $(1.9,1.7)$. By starting with a large noise kernel ($\sigma = 1.5$), Model-Guided MPPI discovers the global basin of attraction around $$. Transitioning to a finer kernel ($\sigma = 0.1$), then employs a Newton-like update step to achieve high-precision optimization in just 3 iterations with $100$ samples.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-D Randomized smoothing on non-smooth dynamics", "weight": 1.0} -->

To demonstrate the versatility of our framework, we apply it to a challenging contact-rich manipulation task. Contact dynamics introduce discontinuities that make standard analytical gradients uninformative. In this setting, we use randomized smoothing to extract quadratic model-guidance for a black-box physics simulator.\

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-D Randomized smoothing on non-smooth dynamics", "weight": 1.0} -->

Benchmark task. We use a single-finger and sphere manipulation scenario as a minimal proxy for contact-rich manipulation. The system comprises two spheres in a static environment with walls, as shown in Fig. 6. While geometrically simple, this task captures the core complexity of manipulation planning: non-smooth dynamics and underactuation. The actuated "finger" (blue sphere) must navigate to a target while manipulating a passive object (orange sphere), requiring the optimizer to manage frequent contact-making and breaking to transfer momentum.\

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-D Randomized smoothing on non-smooth dynamics", "weight": 1.0} -->

Experimental setup. This task is implemented within the robotic library, a framework for manipulation planning and constrained optimization which interfaces with the MuJoCo physics engine. The simulation handles system dynamics, including friction and contact impulses at a timestep of $1\text{ms}$. We parameterize the robot's motion as a spline trajectory defined by 4 control points over a fixed horizon of $1.0\text{s}$, where the optimization variables are the spline control points.\

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-D Randomized smoothing on non-smooth dynamics", "weight": 1.0} -->

Evaluation protocol. We generate $200$ diverse problem instances with challenging contact configurations via NLP sampling and compare methods using performance profiles of the normalized optimality gap after a fixed budget of $30$ iterations. We enforce a fixed planning budget of $64$ trajectory samples per iteration for all methods. For our model-guided approach, we use randomized smoothing with $128$ auxiliary samples to estimate the quadratic model approximation. We treat this estimation step as a surrogate for an analytical gradient oracle. It represents the cost of obtaining model information in a non-differentiable setting, while the planning update itself respects the same sample constraint as the baselines.\

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-D Randomized smoothing on non-smooth dynamics", "weight": 1.0} -->

Metric and results. Since the global optimum is unknown, we define the best solution $f^{\ast}$ as the minimum cost found by any method for a given task. The normalized optimality gap is then defined as $\tau = {{({f_{\text{final}} - f^{\ast}})}/{({f_{\text{init}} - f^{\ast}})}}$. A value of $\tau = 0$ indicates that the method matched the best-performing method, while $\tau = 1$ implies no improvement.

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-D Randomized smoothing on non-smooth dynamics", "weight": 1.0} -->

The performance profile, depicted in Fig. 5, reports the fraction of tasks where a method achieves a solution within a threshold $\tau$ of the best performance. Model-Guided MPPI consistently achieves low normalized optimality gaps across a large fraction of problem instances, indicating reliable convergence, whereas Vanilla MPPI exhibits higher variability. CMA-ES demonstrates competitive performance in most instances but shows slightly reduced consistency across the full task distribution. While this benchmark serves as a first step, the results confirm that the proposed formulation can handle the hybrid dynamics inherent to rich-contact manipulation scenarios. This suggests a promising path toward applying variance-reduced MPPI to full-scale dexterous manipulation tasks in future work.

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-E Computational analysis", "weight": 1.0} -->

Finally, we examine how model construction and residual sampling contribute to the per-iteration cost across our three setups. Vanilla MPPI incurs the same sampling cost but evaluates the full objective $f$ rather than the residual $r^{k}$, so the overhead of our method is entirely concentrated in model construction, whose magnitude depends on the chosen approximation strategy.

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-E Computational analysis", "weight": 1.0} -->

Tab. II reports per-iteration timings, measured on an Intel Core i7-11850H. (i) Static benchmarks (SB): model construction is negligible ($12\%$ vs. $88\%$) since derivatives are available in closed form. The timings are averaged over the four functions. (ii) Cart-pole (CP): using AD-based exact derivatives, model construction cost is constant and independent of the sample budget $N$, while residual sampling grows linearly. The model share consequently decreases from $75\%$ at $N = 2$ to $9\%$ at $N = 1024$. We use AD here to validate the variance-reduction principle under an exact model, not for wall-clock efficiency. (iii) Single-finger (SF): model construction dominates ($68\%$ vs. $32\%$), since we use $128$ auxiliary samples (twice the planning budget) for randomized smoothing.

<!-- chunk {"id": "body-0067", "role": "body", "section": "IV-E Computational analysis", "weight": 1.0} -->

Overall, the method is most attractive when the quadratic model is already available or cheap relative to rollouts. When it must be estimated from scratch, the trade-off becomes a balance between the additional estimation cost and the gain in sample efficiency. The framework remains agnostic to this choice, supporting cheaper structured approximations such as Gauss--Newton or BFGS that closely track the exact model (Fig. 4) at a fraction of the cost.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

In this work, we introduced a variance-reduced, accelerated extension of MPPI based on a model--residual decomposition of the objective. By factoring the Boltzmann update into a model-guided prior and a residual correction, the method injects structural information into the sampling process while retaining the flexibility of sampling-based control. When instantiated with a quadratic model, this decomposition yields a closed-form Gaussian guided prior whose mean and covariance encode first- and second-order information, resulting in a Newton-like update at the distribution level. A key strength is that the framework is agnostic to the source of curvature information, seamlessly accommodating analytical Hessians, structural approximations (e.g., Gauss- or Quasi-Newton), and gradient-free randomized smoothing. Across benchmark optimization problems, nonlinear, underactuated, and non-smooth control tasks, the proposed method demonstrates faster convergence, a higher effective sample size, and greater robustness in low-sample regimes compared to vanilla MPPI and CMA-ES. These results show that exploiting model structure can improve the efficiency of sampling-based control under tight computational budgets.\

<!-- chunk {"id": "body-0069", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

While our method improves sample efficiency, it introduces some trade-offs. First, constructing the quadratic model incurs an additional computational cost (see Tab. II). The magnitude of this overhead depends on the approximation strategy. With the development of fast differentiable physics engines, obtaining first-order gradients is becoming increasingly negligible, effectively mitigating the cost of analytical or Gauss-Newton approximations. In non-differentiable settings that require randomized smoothing, the overhead is distinct. While these evaluations are fully parallelizable, they incur a per-iteration computational cost that exceeds that of Vanilla MPPI. Second, the impact of the quality of the quadratic approximation on performance can be quantified through the residual. When the model $m^{k}$ accurately captures the local geometry, the residual $r^{k}$ has smaller magnitude and lower variance than $f$, the importance weights $\exp{({- {r^{k}/\lambda}})}$ are more uniform, and the effective sample size (ESS, Eq. ) increases. This is the regime in which our method provides the largest benefit.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

Conversely, when the model is less informative (poor curvature estimates or mismatched smoothing scale), $r^{k}$ becomes larger and more variable, the weights concentrate, and ESS drops. The sampler then corrects for a poor proposal rather than exploiting a good one, and performance degrades toward vanilla MPPI. As an illustration, in Fig. 2, a too local model would guide the proposal toward the nearest valley, leading to limited benefits or oscillatory behavior. An appropriately coarse model instead smooths out local irregularities and steers iterations toward the correct basin before switching to a finer model for high-precision convergence.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

We will focus on reducing computational overheads and expanding the applicability of our model-guided MPPI. We plan to investigate adaptive smoothing strategies in which the noise scale $\sigma$ and temperature $\lambda$ are adapted online based on the residual variance, thereby removing the need for manual heuristic tuning. Furthermore, we aim to integrate learned models using data-driven priors to guide efficient sampling and to scale this method to high-dimensional, contact-rich domains such as dexterous manipulation, where the cost of exploration is prohibitively high.
