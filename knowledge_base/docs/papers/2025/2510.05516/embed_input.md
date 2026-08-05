<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

NeST-BO: Fast Local Bayesian Optimization via Newton-Step Targeting of Gradient and Hessian Information

Topics include Bayesian optimization, Newton's method, Gaussian processes, High-dimensional optimization, Hessian information, Black-box optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops a local Bayesian optimization method that targets an estimated Newton step by learning gradient and Hessian information with Gaussian-process surrogates. The paper is a curvature-aware alternative to broader global BO strategies, aiming for fast local convergence in expensive high-dimensional objectives.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Bayesian optimization (BO) is effective for expensive black-box problems but remains challenging in high dimensions. We propose NeST-BO, a curvature-aware local BO method that targets a (modified) Newton step by jointly learning gradient and Hessian information with Gaussian process (GP) surrogates, and selecting evaluations via a one-step lookahead bound on the Newton-step error. We show that this bound contracts with batch size, so NeST-BO drives the step error to zero; in well-behaved neighborhoods it recovers the fast local convergence behavior of inexact/modified Newton methods, while standard safeguards support global convergence to stationary points. To improve scaling with problem dimension, we optimize the acquisition in low-dimensional embedded subspaces (random or learned), reducing the dominant cost of learning curvature from O(d^) to O(m^) with m ll d while preserving step targeting. Across high-dimensional synthetic and real-world problems, including cases with thousands of variables and unknown active subspaces, NeST-BO consistently yields faster convergence and better final values than state-of-the-art local and high-dimensional BO baselines.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Bayesian optimization (BO) is a popular framework for optimizing expensive black-box functions because it often needs far fewer evaluations than alternative derivative-free methods [jones1998efficient, frazier2018tutorial, garnett2023bayesian]. BO has been applied successfully in automated machine learning [snoek2012practical, lindauer2022smac3], prompt optimization for LLMs [sabbatella2024bayesian], robotics and control [berkenkamp2023bayesian, paulson2023tutorial], process optimization [kudva2025multi], materials design [frazier2015bayesian, tang2024beacon], and more. However, as dimensionality grows, performance often deteriorates, with recent studies attributing this decline to degeneracies such as vanishing or uninformative gradients in the Gaussian process (GP) surrogate [williams2006gaussian] that make acquisition optimization brittle when length scales are poorly chosen [papenmeier2025understanding].

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This work develops a curvature-aware local BO approach and a practical way to make it scale to very high dimensions. We introduce NeST-BO (Newton-Step-Targeted BO), which uses the GP surrogate model to jointly learn gradient and Hessian information, and chooses new evaluations to shrink a one-step lookahead bound on the Newton-step error. Conceptually, NeST-BO targets the step rather than the derivatives themselves an approach that we find can learn the Newton direction with fewer samples than, e.g., finite difference methods would require.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

NeST-BO is not motivated by the idea that a vanilla Newton methods is a robust global solver for nonconvex objectives. Rather, it is designed as a local refinement routine: once we are in a neighborhood where the objective is reasonably smooth and the curvature is informative, modified Newton schemes can provide much faster local convergence than purely first-order updates. In practice, this hybrid behavior is typically enforced by standard safeguards (e.g., damping, line search), so that the method behaves like a gradient step when curvature is unreliable, while retaining rapid local convergence when it is helpful [nocedal2006numerical]. Because second-order (Newton-type) methods can be highly effective as local accelerators even on large, nonconvex objectives when suitably modified, e.g., [martens2010hessianfree], we conjecture targeting the step can substantially accelerate local BO.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

An important obstacle is the cost of Hessian-based terms, which grows as $O(d^2)$ with input dimension $d$. To address this, we instantiate NeST-BO inside lower-dimensional subspaces, using a nested subspace expansion strategy similar to BAxUS [papenmeier2022increasing]. This collapses the dominant cost to $O(m^2)$ for subspace dimension $m \ll d$while preserving the benefits of Newton-step targeting. We find that the local Newton step is also naturally robust to the non-stationarity in the mapping from the subspace to the objective function that can be introduced by subspace embeddings, which helps explain why our approach continues to perform well for some problems even as the ambient dimension reaches thousands or more.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Finally, we find that our acquisition includes a scale factor that balances gradient and Hessian learning whose optimal value must be estimated, e.g., Monte Carlo sampling; our empirical results show that performance is robust to the precise choice of this factor, and we use a simple default that avoids this extra computation. vanishing power-function condition showing that NeST-BO drives the Newton-step error to zero as batch size increases. As a result, the method fits squarely within the classical inexact/modified Newton viewpoint: once the step errors are sufficiently small, one recovers the standard fast local convergence behavior of Newton-type methods, while globalization via, e.g., dampling/line search safeguards yields the usual notion of global convergence to stationary points [nocedal2006numerical].

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

- A curvature-aware local BO algorithm that explicitly targets the Newton step via a tractable and theoretically-sound acquisition function. - A scalable instantiation that runs NeST-BO in enlarging subspaces, reducing computation from $O(d^2)$ to $O(m^2)$, where $d$ and $m$ are the ambient and maximum subspace dimensions. - Theoretical guarantees showing that NeST-BO drives Newton-step error to zero and thus inherits the convergence behavior of modified Newton methods. - Extensive empirical results on more than 12 synthetic and real-world problems (ranging from 20d to $>$7000d), where NeST-BO variants yield large performance improvements over six state-of-the-art high-dimensional BO baselines.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Setup & Bayesian Optimization", "weight": 1.0} -->

We consider the following zeroth-order optimization problem over a \bs{x}^\star \in \argmin_{\bs{x} \in \mathcal{X}} f(\bs{x}), \qquad \mathcal{X} \subseteq \mathbb{R}^d, where the expensive function $f$ can only be accessed through noisy queries $y = f(\bs{x}) + \epsilon$ with i.i.d. Gaussian noise $\epsilon \sim \mathcal{N}(0,\sigma^2)$. Bayesian optimization (BO) tackles [eq:true-opt] by fitting a probabilistic surrogate $p(f|\mathcal{D})$ over available data $\mathcal{D}$ and uses it to select new evaluations by maximizing an acquisition function $\alpha(\bs{x}|\mathcal{D})$ that trades off exploration and exploitation. After exhausting the budget, the recommended solution is either the best observed point or the minimizer of the surrogate mean.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Setup & Bayesian Optimization", "weight": 1.0} -->

Many acquisitions have been proposed including expected improvement (EI) [jones1998efficient], upper confidence bound (UCB) [srinivas2010gaussian], knowledge gradient (KG) [frazier2008knowledge], and entropy-based methods [hennig2012entropy]. We refer readers to [garnett2023bayesian]for a full tutorial.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Gaussian Processes and their Derivatives", "weight": 1.0} -->

We use Gaussian processes (GPs) [williams2006gaussian] as surrogates, which is the most popular surrogate model class in BO. A GP prior $f \sim \mathcal{GP}(\mu,k)$ induces a joint Gaussian belief over any finite set of inputs; conditioning on the dataset $\mathcal{D}$ yields a posterior GP $f | \mathcal{D} \sim \mathcal{GP}(\mu_\mathcal{D}, k_\mathcal{D})$ with closed-form posterior mean $\mu_\mathcal{D}$ and covariance (or kernel) function $k_\mathcal{D}$. A key property we repeatedly use in this work is that derivatives of a GP remain GPs because differentiation is a linear operator [de2021high].

<!-- chunk {"id": "body-0013", "role": "body", "section": "Gaussian Processes and their Derivatives", "weight": 1.0} -->

Thus, the gradient $\bs{g}(\bs{x}) = \nabla f(\bs{x})$ and Hessian $\bs{H}(\bs{x}) = \nabla^2 f(\bs{x})$ have analytic posterior means and covariances obtained by differentiating the kernel in the appropriate arguments. We collect the explicit formulas for $f$, $\bs{g}$, and $\bs{H}$ posteriors in Appendix [app:gp-expressions].

<!-- chunk {"id": "body-0014", "role": "body", "section": "Local BO using Gradients", "weight": 1.0} -->

Learning a globally accurate surrogate becomes data-hungry as $d$ grows because regret bounds for global BO (e.g., GP-UCB) scale exponentially with dimension unless strong structural assumptions hold [srinivas2010gaussian]. Local BO addresses this by focusing search near the incumbent and updating the model with more locally collected data. Gradient-informed methods refine this idea by explicitly selecting evaluations that reduce uncertainty about the local descent direction. A prominent example is the Gradient Information (GI) acquisition that underlies GIBO [muller2021local]. Let $\bs{x}_t$ be the current iterate and $\bs{Z} \in \mathbb{R}^{b_t\times d}$ a batch of candidates.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Local BO using Gradients", "weight": 1.0} -->

The key observation is, since posterior covariances do not depend on the observed targets $\bs{y}$, this simplifies to minimizing a (squared) power function for the gradient defined as the trace of the posterior covariance: \tilde{\alpha}_{\mathrm{GI}}(\bs{Z}|\bs{x}_t,\mathcal{D}) =\tr\!\big(\Sigma^{\bs g}_{\mathcal{D}\cup \bs{Z}}(\bs{x}_t)\big) This criterion encourages sampling along directions that most reduce gradient uncertainty, after which the algorithm steps along the GP posterior mean gradient. Theoretical analysis of GIBO showed that the convergence rate to a stationary point scales linearly in $d$, which is better than rates at which global optimization can find the global optimum [wu2023behavior].

<!-- chunk {"id": "body-0016", "role": "body", "section": "Local BO using Gradients", "weight": 1.0} -->

[nguyen2022local] revisit the GIBO template and show that the GP posterior mean gradient is not, in general, the direction that maximizes the posterior probability of descent, which motivates MPD: an acquisition that targets an upper bound on the one-step maximum descent probability together with updates along the most-probable descent direction. We include MPD as a strong baseline; NeST-BO builds on the same local gradient-learning viewpoint as GIBO but targets a second-orderNewton step rather than a first-order descent direction.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Newton's Method for Optimization", "weight": 1.0} -->

Newton’s method (NM) is a classical algorithm for (unconstrained) local minimization of twice continuously differentiable objectives. Starting from $\bs{x}_0 \in \mathbb{R}^d$, it makes the following updates: \bs{x}_{t+1} = \bs{x}_t - \gamma_t \bs{H}(\bs{x}_t)^{-1} \bs{g}(\bs{x}_t), \qquad t=0,1,\ldots, where $\gamma_t > 0$ denotes the step size at iteration $t$. NM re-scales and rotates the gradient using local curvature. On well-behaved landscapes (e.g., in a neighborhood where $\bs{H}$ is positive definite), this makes progress far less sensitive to conditioning than first-order methods and yields local quadratic convergence near a (nondegenerate) minimizer, in contrast to the linear or sublinear rates typical of gradient schemes under comparable assumptions [nocedal2006numerical].

<!-- chunk {"id": "body-0018", "role": "body", "section": "Newton's Method for Optimization", "weight": 1.0} -->

In the BO context, we do not get to directly observe $\bs{g}$ or $\bs{H}$, but their GP posteriors (implicitly) define a distribution over the Newton step $\bs{d}(\bs{x})=\bs{H}(\bs{x})^{-1}\bs{g}(\bs{x})$. NeST-BO is built around actively reducing the posterior uncertainty of the step $\bs{d}(\bs{x})$, rather than estimating $\bs{g}(\bs{x})$ and $\bs{H}(\bs{x})$separately. The thought is that, when the Newton step gets close to a local solution, the iteration advantage of NM can outweigh the per-step cost of learning curvature, yielding stronger sample efficiency than gradient-only methods like GIBO.

<!-- chunk {"id": "body-0019", "role": "body", "section": "An Acquisition for the Newton Step", "weight": 1.0} -->

$\bs{x}_t$ be the current iterate and $\bs{Z}\!\in\!\mathbb{R}^{b_t \times d}$ a batch of candidates at which we might evaluate $f$. Our goal is to learn the Newton step $\bs d(\bs x)=\bs H(\bs x)^{-1}\bs g(\bs x)$ at $\bs{x}_t$ under the GP posterior. Because $\bs{d}(\bs{x})$ is non-Gaussian, its posterior covariance is not available in closed form; instead we derive a Reproducing Kernel Hilbert Space (RKHS) error bound (inspired by the results derived in [wu2023behavior]).

<!-- chunk {"id": "body-0020", "role": "body", "section": "An Acquisition for the Newton Step", "weight": 1.0} -->

Let the gradient and (vectorized) Hessian (squared) power functions at $\bs{x}$ be denoted by $\pi^{\bs g}_{\mathcal D}(\bs x)=\tr\left(\Sigma^{\bs g}_{\mathcal D}(\bs x)\right)$ and $\pi^{\bs H}_{\mathcal D}(\bs x)=\tr\big(\Sigma^{\mathrm{vec}(\bs H)}_{\mathcal D}(\bs x)\big)$. Also, let $\mathcal{H}$ be the RKHS on $\mathcal{X}$ equipped with a reproducing kernel $k(\cdot,\cdot)$ and RKHS norm $\| \cdot \|_\mathcal{H}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "An Acquisition for the Newton Step", "weight": 1.0} -->

Motivated by the Newton-step error bound in Theorem [thm:newton-bound], our design goal at iteration $t$ is simple: choose a batch $\bs Z$ that will make the post-batch bound on the error as small as possible (in expectation) over the unobserved outcomes at $\bs Z$. Concretely, let $B_{\mathcal D}(\bs x_t) = \pi^{\bs g}_{\mathcal D}(\bs x_t) + s_{\mathcal D}(\bs x_t)\,\pi^{\bs H}_{\mathcal D}(\bs x_t)$, so that [eq:newton-step-bound] is $\varepsilon_{\mathcal D}(\bs x_t)\le C_{\bs x_t}\sqrt{B_{\mathcal D}(\bs x_t)}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "An Acquisition for the Newton Step", "weight": 1.0} -->

Since $C_{\bs x_t}$ is independent of the data, minimizing an upper bound on the expected step error is naturally achieved: \mathbb{E}_{\bs y \mid \mathcal D,\bs Z} This is the direct analogue of GI, which chooses points to minimize a lookahead bound on the gradient error, as shown in [wu2023behavior]. The objective in [eq:nest-objective-start]is doing the same thing but on a lookahead bound for the error in the Newton step.

<!-- chunk {"id": "body-0023", "role": "body", "section": "An Acquisition for the Newton Step", "weight": 1.0} -->

The remaining step is to simplify [eq:nest-objective-start]. Under a GP with Gaussian observation noise, the posterior covariances of derivatives at $\bs x_t$ after conditioning on $\mathcal D\cup(\bs Z,\bs y)$ do not depend on the realized values $\bs y$; they depend only on the locations $\bs Z$, so the only term in [eq:nest-objective-start] that requires a lookahead expectation is $s_{\mathcal D\cup(\bs Z,\bs y)}(\bs x_t)$, which depends on posterior means through $\widehat{\bs g}$ and $\widehat{\bs H}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "An Acquisition for the Newton Step", "weight": 1.0} -->

Using this fact, [eq:nest-objective-start] reduces to our following proposed Newton Step Targeting (NeST) acquisition function: & \tilde{\alpha}_{\mathrm{NeST}}(\bs Z | \bs x_t,\mathcal D) \\\notag + \mathbb{E}_{\bs y \mid \mathcal D,\bs Z}\left\lbrace s_{\mathcal D\cup(\bs Z,\bs y)}(\bs x_t) \right\rbrace NeST is composed of three main terms: (i) $\pi^{\bs g}_{\mathcal D\cup\bs Z}(\bs x_t)$ is the trace of the covariance of the one-step lookahead gradient at $\bs{x}_t$, (ii) $\pi^{\bs H}_{\mathcal D\cup\bs Z}(\bs x_t)$ is the trace of the covariance of the one-step lookahead vectorized Hessian, and (iii)

<!-- chunk {"id": "body-0025", "role": "body", "section": "An Acquisition for the Newton Step", "weight": 1.0} -->

$\mathbb{E}_{\bs y \mid \mathcal D,\bs Z}\left\lbrace s_{\mathcal D\cup(\bs Z,\bs y)}(\bs x_t) \right\rbrace$ is a scale factor that weights these two terms.

<!-- chunk {"id": "body-0026", "role": "body", "section": "An Acquisition for the Newton Step", "weight": 1.0} -->

We can interpret (i) and (ii) as measures of the information content about quantities of interest (mainly gradient and Hessian at our current point) and (iii) as a term that adaptively balances gradient and Hessian information. Note that, since $\| \bs{H}^{-1}(\bs{x}) \bs{g}(\bs{x}) \| \leq \| \bs{H}^{-1}(\bs{x}) \| \| \bs{g}(\bs{x}) \|$, we can also think of this term as a conservative proxy for the squared step length and thus upweights Hessian information when NM may take large steps.

<!-- chunk {"id": "body-0027", "role": "body", "section": "An Acquisition for the Newton Step", "weight": 1.0} -->

The expectation over the scale factor in [eq:nest-rearranged] does not have a simple closed-form expression and thus would need to be estimated using Monte Carlo (MC) sampling in practice (see Appendix [app:mc-est-scale] for details). This is mainly due to the fact that $s_{\mathcal D\cup(\bs Z,\bs y)}$ is a nonlinear function of $\bs{y}$ and thus non-Gaussian in general.

<!-- chunk {"id": "body-0028", "role": "body", "section": "An Acquisition for the Newton Step", "weight": 1.0} -->

Through some empirical testing shown in Appendix [app:scale-factor], we observed relatively low sensitivity in performance to the precise scale factor, which motivates the following computationally cheaper acquisition: \widehat{\alpha}_{\mathrm{NeST}}(\bs Z | \bs x_t,\mathcal D, \widehat{s}_t) = \pi^{\bs g}_{\mathcal D\cup\bs Z}(\bs x_t) + \widehat{s}_t \,\pi^{\bs H}_{\mathcal D\cup\bs Z}(\bs x_t), with a pre-determined $\widehat{s}_t > 0$ that is independent of $\bs{Z}$. This recovers GI when $\widehat{s}_t = 0$ and focuses more on curvature as $\widehat{s}_t$ increases.

<!-- chunk {"id": "body-0029", "role": "body", "section": "An Acquisition for the Newton Step", "weight": 1.0} -->

In Section [subsec:theoretical-analysis], we show the NeST samples can drive the bound in [eq:newton-step-bound]to zero as the batch size increases for any choice of scale factor.

<!-- chunk {"id": "body-0030", "role": "body", "section": "The NeST-BO Algorithm", "weight": 1.0} -->

[alg:NeSTBO] summarizes the simple version of the loop. At iterate $\bs{x}_t$, choose a batch $\bs{X}_t$ by minimizing [eq:nest-approx] at $\bs{x}_t$; update the GP with the new observations; then move along the predicted Newton step with some step size. Note there are a number of practical implementation details, which we discuss more in the next section.

<!-- chunk {"id": "body-0031", "role": "body", "section": "The NeST-BO Algorithm", "weight": 1.0} -->

Since we are attempting to learn both the gradient and Hessian at $\bs{x}_t$, one can in fact easily adapt this algorithm to use a step direction from any form of, e.g., damped NM [hanzely2022damped] or NM with line search [shea2025greedy]. We do not attempt to systematically compare different options in this work; instead we go with a standard hybridimplementation that uses Newton steps when they well-behaved and otherwise revert to gradient steps.

<!-- chunk {"id": "body-0032", "role": "body", "section": "The NeST-BO Algorithm", "weight": 1.0} -->

We provide an illustration and visual comparison of NeST-BO (top) to GIBO (bottom) in Figure [fig:Illustrative], which demonstrates the advantages of simultaneously learning gradient and Hessian (curvature) information.

<!-- chunk {"id": "body-0033", "role": "body", "section": "The NeST-BO Algorithm", "weight": 1.0} -->

Top: NeST-BO’s acquisition $\tilde{\alpha}_{\mathrm{NeST}}$; Bottom: GIBO's acquisition $\tilde{\alpha}_{\mathrm{GI}}$ on a 2D test function at iterate $\bs{x}_t$ (blue circle). Darker background indicates larger acquisition value. Red square: location of the true Newton step. Blue triangle: GP-predicted Newton step. Orange star: acquisition minimizer. Black crosses: Past evaluation points. NeST-BO places samples away from $\bs{x}_t$ along directions informative for curvature, rapidly shrinking the Newton-step error bound; GI tends to oversample near $\bs{x}_t$, slowing curvature identification.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

[alg:NeSTBO] describes an idealized NeST-BO loop used for exposition. In practice, just as vanilla NM can be brittle without safeguards, we found it helpful to use a slightly hardened variant for all experiments. The key point is that NeST-BO’s value is in where it samples at each iteration (i.e., producing high-quality local gradient/Hessian information), so we can borrow standard Newton-style safeguards without changing the core idea. For completeness, the full pseudocode for our practical implementation is given in Appendix[app:practical-nestbo]. We summarize the main choices here.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

In most applications, kernel hyperparameters are not known a priori. We thus need to fit the GP by maximizing the marginal log likelihood, which is standard in the BO literature. Our method does not rely on this specific estimator; any hyperparameter learning procedure can be used.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

NeST-BO is meant to behave like a local Newton-type method once it enters a well-behaved neighborhood. When $\widehat{\bs H}_{\mathcal D}(\bs x_t)$ is positive definite (and not too ill-conditioned), this is a descent direction for the GP mean and typically behaves as expected. If $\widehat{\bs H}_{\mathcal D}(\bs x_t)$ is indefinite or numerically unstable to invert, we interpret this as a signal that we are not yet in a regime where Newton steps are reliable, and we revert to a length-scale-normalized gradient step [muller2021local]. This is a simple and robust fallback; many other Newton safeguards (e.g., damping/regularization or trust-region updates) could also be used, but we did not attempt to exhaustively test (or internally tune) these variants, which would be valuable future work.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Batch versus sequential selection. Although [eq:nest-approx] supports joint batch optimization, we select points greedily. After choosing each point, we update the posterior covariance deterministically (note that the power functions do not depend on the realized outcomes), and then re-optimize to choose the next point. This replaces a single $b_t d$-dimensional search with $b_t$ separate $d$-dimensional searches and naturally discourages near-duplicate selections, since conditioning on a chosen location reduces posterior variance around it. In our preliminary tests, greedy selection closely matched joint optimization.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

We use a standard Armijo backtracking line search on the GP mean $\mu_{\mathcal D}$ along the chosen direction. This gives a lightweight safeguard against overly aggressive steps without requiring additional function evaluations, and we cap the number of backtracking iterations using standard defaults [bertsekas2016nonlinear]. There has been recent work on greedy NM [shea2025greedy], which suggests it can be advantageous to allow for step sizes larger than 1, but we do not consider that here.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

The scale $\widehat{s}_t$ in [eq:nest-approx] controls how strongly (approximate) NeST emphasizes curvature (Hessian) uncertainty relative to gradient uncertainty. For the main experiments, we use a simple deterministic proxy $\widehat{s}_t = 1$, which performed reliably across problems and dimensions. Appendix[app:comparison-scale] provides a broader comparison over $\widehat{s}_t$ choices. We also tested a plug-in variant $\widehat{s}_t = s_{\mathcal D}(\bs x_t)$ that neglects the lookahead dependence on $(\bs Z,\bs y)$ (Appendix[app:plugin-vs-s1]); performance was very similar between these options, so we default to $\widehat{s}_t=1$for simplicity.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

$\varepsilon_t = \varepsilon_{\mathcal{D}_{t+1}}(\bs{x}_t)$ denote the Newton-step error after iteration $t$. By Theorem[thm:newton-bound], $\varepsilon_t$ is controlled by posterior uncertainty in the local derivatives at $\bs{x}_t$; specifically, the power functions appearing in [eq:newton-step-bound]. This motivates a simple designability condition: Vanishing power-function condition (VPC). The NeST design objective $\pi^{\bs{g}}_{\mathcal{D}_{t+1}}(\bs{x}_t) + \widehat{s}_t\,\pi^{\bs{H}}_{\mathcal{D}_{t+1}}(\bs{x}_t)$ can be made arbitrarily small as $b_t$increases.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

VPC is not an abstract assumption on $\varepsilon_t$; it ties the step error to concrete, design-controllable posterior covariances. A key subtlety is that NeST-BO cannot directly minimize the right-hand side of [eq:newton-step-bound] because the scale term $s_{\mathcal{D}_{t+1}}(\bs{x}_t)$ is only revealed after the batch is observed. Nevertheless, the bound applies to the realized step error under any sampling rule, and VPC can be verified constructively for NeST. We state the main idea informally below; the complete statement and proof are in Appendix[app:proof-vpc].

<!-- chunk {"id": "body-0042", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

Fix an iteration $t$ and the current iterate $\bs{x}_t$. For a batch $\bs{Z}=(\bs{z}_1,\dots,\bs{z}_{b_t})\in\mathcal{X}^{b_t}$, let $\Phi_t(\bs{Z}) = \widehat{\alpha}_{\mathrm{NeST}}(\bs Z | \bs x_t,\mathcal D, \widehat{s}_t)$ be short for the approximate NeST acquisition function with $\widehat{s}_t > 0$. Under mild domain and kernel regularity conditions, the following hold. $b^\star=d^2+d+1$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

Then, in the noiseless setting, the optimal NeST design value can be driven to zero: $$\inf_{\bs{Z}\in\mathcal{X}^{b_t}} \Phi_t(\bs{Z}) = 0 ~ \text{(as an infimum) for all } b_t\ge b^\star.$$ Equivalently, for every $\epsilon>0$ and every $b_t\ge b^\star$, there exists a batch $\bs{Z}_\epsilon$ such that $\Phi_t(\bs{Z}_\epsilon)\le \epsilon$. Moreover, one explicit candidate design achieving this is a symmetric $b^\star$-point centered-difference stencil at radius $h$, for which $\Phi_t(\bs{Z}_h) \lesssim h^4$ as $h\to 0$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

Gaussian noise of variance $\sigma^2$, using $m$ replicates per location is equivalent to observing averaged responses with variance $\sigma^2/m$. Thus, for every $\epsilon>0$ there exist $h$ and $m$ such that the corresponding replicated design satisfies An important consequence is that, once NeST-BO is operating in a neighborhood where NM is well-conditioned, VPC implies $\varepsilon_t \to 0$ as the batch size increases, and NeST-BO asymptotically inherits the local quadratic convergence rate of NM (full statement and proof in Appendix[app:local-quadratic-conv]). Finally, the VPC statement itself does not depend on the particular choice of scale factor beyond requiring $\widehat{s}_t>0$. Thus, the simplified acquisition in [eq:nest-approx] retains the same asymptotic guarantee, with the caveat that the argument is inherently for large enough batches.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Scaling NeST-BO via Subspaces", "weight": 1.0} -->

The main computational bottleneck for NeST-BO in high ambient dimension $d$ is the Hessian term $\pi^{\bs{H}}_{\mathcal{D} \cup \bs{Z}}(\bs{x}_t)$, which scales quadratically in $d$. We propose to address this by instantiating NeST-BO inside embedded subspaces $\bs{v} \in \mathbb{R}^m$ of size $m \ll d$. We adopt the nested, sparse random-embedding scheme of BAxUS bins of input coordinates are hashed into $m$ target coordinates with random signs, and the target dimension is increased over time by splitting bins while retaining observations across embeddings [papenmeier2022increasing]. This approach preserves past data under splits and increases the probability that the subspace contains an optimizer as $m$grows.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Scaling NeST-BO via Subspaces", "weight": 1.0} -->

We run NeST-BO in the subspace $\bs{v}$, map the candidates back to the ambient dimension $\bs{x} = \bs{S}^\top \bs{v}$ (where $\bs{S}^\top \in \mathbb{R}^{d \times m}$ is the projection matrix) for evaluation, and update the GP in the embedded subspace coordinates. This reduces the per-candidate curvature cost from $O(d^2)$ to $O(m^2)$ while preserving the step-targeting principle. Compared to the original BAxUS algorithm, which couples its embedding with a variant of TuRBO, our version replaces TuRBO with NeST-BO; in problems where curvature matters, we find that this can can substantially accelerate optimization progress (see results in Section [sec:experiments]).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Scaling NeST-BO via Subspaces", "weight": 1.0} -->

Lastly, note that our theoretical results related to VPC are proved only for NeST-BO in the original $d$-dimensional space, and they do not directly extend to the subspace variant. Intuitively, the VPC proof relies on constructing $d$-dimensional designs that can drive the full gradient and Hessian power functions at $\bs{x}_t$ to zero, whereas a fixed low-dimensional embedding only controls derivative information within the embedded coordinates and may not capture curvature directions relevant in $\mathbb{R}^d$. The BAxUS-style embedding should thus be viewed as a practical scalability heuristic that leverages the NeST sampling principle.

<!-- chunk {"id": "body-0048", "role": "body", "section": "RESULTS", "weight": 1.0} -->

We now benchmark NeST-BO and its subspace variant, labeled NeST-BO-sub, against strong local and global BO baselines: TuRBO [eriksson2019scalable], GIBO[muller2021local], MPD[nguyen2022local], MinUCB[fan2024minimizing], BAxUS[papenmeier2022increasing], and a vanilla GP-BO configured with dimensionally calibrated priors and LogEI (we label this D-scaled LogEI)[hvarfner2024vanilla]. We also include Sobol sampling as a non-model baseline.

<!-- chunk {"id": "body-0049", "role": "body", "section": "RESULTS", "weight": 1.0} -->

Unless a global minimizer is known, we report the minimum observed value; otherwise we show simple regret (in log scale). Curves display the median across $10$ independent replicates with $\pm$ one standard error as the shaded band. Implementation details (e.g., models, hyperparameter updates, acquisition optimization, and the precise evaluation budgets for each task) are provided in Appendix[app:experiment-details]. In short, we used a common SE kernel across methods and standard GP training and acquisition optimizers from BoTorch [balandat2020botorch]; hyperparameters and method-specific settings follow prior work and are held consistent across tasks to keep comparisons fair. Due to space limitations, additional ablations and diagnostics appear in Appendix[app:add-experiments].

<!-- chunk {"id": "body-0050", "role": "body", "section": "Synthetic Test Functions", "weight": 1.0} -->

We consider two regimes relevant to our method.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Synthetic Test Functions", "weight": 1.0} -->

Moderate dimension ($d=20$): Sphere, Griewank, and Ackley. High dimension with sparse structure ($d=1000$ with $d_\text{eff}=30$ relevant variables): Griewank, Ackley, and Rosenbrock; the remaining coordinates are dummies and the algorithms are not told which ones are active. These are commonly chosen test problems in the BO literature; formal definitions are given in Appendix[app:synthetic-details]. Figure[fig:main results] (first six panels in the top two rows) summarizes the results.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Synthetic Test Functions", "weight": 1.0} -->

Summary of performance versus evaluations for all synthetic and real-world problems and all methods. Each panel shows either simple regret (log scale; when the global minimizer is known) or the minimum observed value (otherwise). Curves are medians across $10$ runs; shading is $\pm$ one standard error. Top two rows: synthetic problems (20d and 1000d with 30 active variables). Bottom two rows: real-world tasks (control, planning, and high-dimensional model selection). See Appendixapp:experiment-details for the full protocol and Appendixapp:add-experiments for extended studies. $d=20$ problems, NeST-BO consistently matches or outperforms all non-subspace baselines. A common pattern is an initial period with slower progress when far from a minimizer (before curvature is accurately estimated) followed by a steep drop once the iterate enters a well-behaved neighborhood. As several steps accumulate, the estimated Newton step better aligns with the true local geometry, further accelerating progress consistent with our Newton-step error bound, which tightens as the gradient and Hessian power functions shrink.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Synthetic Test Functions", "weight": 1.0} -->

Subspace methods start from stronger initial values by design (they restrict the initial design and acquisitions), but NeST-BO-sub ultimately achieves the lowest regret and, notably, improves over BAxUS across all three problems. These results indicate that howone moves inside a subspace matters, i.e., curvature-aware Newton updates can be more effective than trust-region moves, even when both operate in the same embedding space. $d=1000$ sparse suite, subspaces are essential. Methods that attempt to learn gradients and/or Hessians in the ambient space require $O(d)$queries per iteration and cannot meaningfully progress under our fixed budgets (e.g., 200 evaluations), so we do not include them here. NeST-BO-sub clearly dominates BAxUS, D-scaled LogEI, and TuRBO, achieving substantially lower regret on both Ackley and Griewank.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Synthetic Test Functions", "weight": 1.0} -->

TuRBO’s trust-region strategy is disadvantaged in very high dimensions, where large local diameters push pairwise distances into regimes that degrade GP fit and acquisition gradients; in contrast, NeST-BO-sub converts a handful of targeted samples near the iterate into accurate Newton steps inside the selected subspace (that can expand as iterations proceed), which drives fast local improvement.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Mid- to High-Dim. Real-World Tasks", "weight": 1.0} -->

We evaluate six real-world benchmarks spanning reinforcement learning (RL) control, robotic planning, and large-scale hyperparameter tuning.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Mid- to High-Dim. Real-World Tasks", "weight": 1.0} -->

Control: Lunar Lander ($d=12$) and Swimmer ($d=16$) from OpenAI Gymnasium; the objective is the negative episodic return (reward sign flipped)[towers2024gymnasium]. Planning: Robot Pushing ($d=14$) and Rover Trajectory ($d=60$) from [wang2018batched,eriksson2019scalable], both optimized as negative reward. Very high-dimension: Ant ($d=888$) a MuJoCo quadruped with 8-dimensional action space and 111-dimensional observations, yielding a linear state-feedback policy with 888 parameters and Leukemia ($d=7129$), a weighted Lasso problem with 7129 hyperparameters from LassoBench[vsehic2022lassobench]. Task definitions, bounds, and initialization protocols are summarized in Appendix[app:real-world-details]. Figure[fig:main results] (last six panels in bottom two rows) reports median performance with $\pm$one standard error bands.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Mid- to High-Dim. Real-World Tasks", "weight": 1.0} -->

In the mid-dimensional group ($d \leq 60$), NeST-BO is consistently state of the art or competitive, achieving the lowest average value in the fewest iterations for Lunar Lander, Robot Pushing, and Swimmer. On Rover Trajectory, NeST-BO-sub edges out NeST-BO, aligning with the intuition that embeddings can capture useful structure as dimensionality and coupling grow. On Lunar Lander and Swimmer, however, subspaces can slightly hurt performance, suggesting most coordinates contribute and the ambient space is preferable.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Mid- to High-Dim. Real-World Tasks", "weight": 1.0} -->

In the very high-dimensional group, NeST-BO-sub is again the best-performing method. On Ant ($d=888$), D-scaled LogEI and TuRBO show little-to-no improvement over their starting values, while BAxUS improves but plateaus well above NeST-BO-sub. The Ant landscape is both non-stationary and ill-conditioned; length-scale calibration alone (as in D-scaled LogEI) can over-smooth such objectives, and trust-region steps struggle to adapt their geometry. On Leukemia ($d=7129$), NeST-BO-sub continues to improve throughout the budget and achieves the best final objective, whereas other methods stagnate early.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Other Methods in Same Subspace", "weight": 1.0} -->

A natural question raised by our subspace results in Figure [fig:main results] is whether NeST-BO’s gains are primarily due to the embedding, or whether targeting the local Newton step continues to matter once we restrict the search to lower-dimensional subspaces. To isolate these effects, we compare NeST-BO-sub to two strong baselines that use the same subspace machinery: (i) GIBO-sub, i.e., GIBO run in the subspace using its length-scale-normalized gradient step [muller2021local] and (ii) D-scaled LogEI-sub, i.e., standard LogEI run in the subspace using the GP prior from [hvarfner2024vanilla]. For context, we also include BAxUS. Figure [fig:subspace] shows the embedding is not the whole story. NeST-BO-sub drives regret down by several orders of magnitude relative to GIBO-sub and D-scaled LogEI-sub (the latter two plateau near $\sim 10^{0}$ on the log scale), while NeST-BO-sub continues improving throughout the budget.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Other Methods in Same Subspace", "weight": 1.0} -->

On Ackley, the same pattern holds: NeST-BO-sub reaches substantially lower regret and converges faster, while the other subspace methods level off earlier.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Other Methods in Same Subspace", "weight": 1.0} -->

Optimization of $1000$-dimensional Griewank and Ackley with $30$ active variables. All -sub variants operate using the same BAxUS-style embedding approach. Median simple regret (log scale) with $\pm$ one standard error shading across 10 runs.

<!-- chunk {"id": "body-0062", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

This work presents NeST-BO, a curvature-aware local Bayesian optimization (BO) method that selects samples to shrink a one-step lookahead bound on Newton-step error and then moves with a damped Newton update. Theoretical analysis establishes a vanishing power-function condition that holds under NeST-BO sampling, implying the algorithm inherits (inexact) Newton guarantees while our experiments show consistent gains over state-of-the-art local and high-dimensional BO baselines on synthetic and real-world problems, including tasks with several thousands of variables (when combined with a subspace variant to enhance scalability). Looking ahead, two promising directions for future research include investigating improved subspace embedding strategies and improving numerical efficiency of the acquisition optimization by better exploiting kernel structure and sparsity for derivative-aware GPs.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Checklist", "weight": 1.0} -->

- For all models and algorithms presented, check if you include: - A clear description of the mathematical setting, assumptions, algorithm, and/or model. [Yes] - An analysis of the properties and complexity (time, space, sample size) of any algorithm. [Yes] - (Optional) Anonymized source code, with specification of all dependencies, including external libraries. [Yes] - For any theoretical claim, check if you include: - Statements of the full set of assumptions of all theoretical results. [Yes] - Complete proofs of all theoretical results. [Yes] - Clear explanations of any assumptions. [Yes] - For all figures and tables that present empirical results, check if you include: - The code, data, and instructions needed to reproduce the main experimental results (either in the supplemental material or as a URL). [Yes] - All the training details (e.g., data splits, hyperparameters, how they were chosen). [Yes] - A clear definition of the specific measure or statistics and error bars (e.g., with respect to the random seed after running experiments multiple times). [Yes] - A description of the computing infrastructure used.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Checklist", "weight": 1.0} -->

(e.g., type of GPUs, internal cluster, or cloud provider). [Yes] - If you are using existing assets (e.g., code, data, models) or curating/releasing new assets, check if you include: - Citations of the creator If your work uses existing assets. [Yes] - The license information of the assets, if applicable. [Not Applicable] - New assets either in the supplemental material or as a URL, if applicable. [Yes] - Information about consent from data providers/curators. [Not Applicable] - Discussion of sensible content if applicable, e.g., personally identifiable information or offensive content. [Not Applicable] - If you used crowdsourcing or conducted research with human subjects, check if you include: - The full text of instructions given to participants and screenshots. [Not Applicable] - Descriptions of potential participant risks, with links to Institutional Review Board (IRB) approvals if applicable. [Not Applicable] - The estimated hourly wage paid to participants and the total amount spent on participant compensation. [Not Applicable]
