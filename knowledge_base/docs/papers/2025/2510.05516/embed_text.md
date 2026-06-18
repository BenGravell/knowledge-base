## INTRODUCTION

Bayesian optimization (BO) is a popular framework for optimizing expensive black-box functions because it often needs far fewer evaluations than alternative derivative-free methods. BO has been applied successfully in automated machine learning, prompt optimization for LLMs, robotics and control, process optimization, materials design, and more. However, as dimensionality grows, performance often deteriorates, with recent studies attributing this decline to degeneracies such as vanishing or uninformative gradients in the Gaussian process (GP) surrogate that make acquisition optimization brittle when length scales are poorly chosen.

This work develops a curvature-aware local BO approach and a practical way to make it scale to very high dimensions. We introduce NeST-BO (Newton-Step-Targeted BO), which uses the GP surrogate model to jointly learn gradient and Hessian information, and chooses new evaluations to shrink a one-step lookahead bound on the Newton-step error. Conceptually, NeST-BO targets the step rather than the derivatives themselves -- an approach that we find can learn the Newton direction with fewer samples than, e.g., finite difference methods would require.

NeST-BO is not motivated by the idea that a vanilla Newton methods is a robust global solver for nonconvex objectives. Rather, it is designed as a local refinement routine: once we are in a neighborhood where the objective is reasonably smooth and the curvature is informative, modified Newton schemes can provide much faster local convergence than purely first-order updates. In practice, this "hybrid" behavior is typically enforced by standard safeguards (e.g., damping, line search), so that the method behaves like a gradient step when curvature is unreliable, while retaining rapid local convergence when it is helpful. Because second-order (Newton-type) methods can be highly effective as local accelerators even on large, nonconvex objectives when suitably modified, e.g. we conjecture targeting the step can substantially accelerate local BO.

An important obstacle is the cost of Hessian-based terms, which grows as $O{(d^{2})}$ with input dimension $d$. To address this, we instantiate NeST-BO inside lower-dimensional subspaces, using a nested subspace expansion strategy similar to BAxUS. This collapses the dominant cost to $O{(m^{2})}$ for subspace dimension $m \ll d$ while preserving the benefits of Newton-step targeting. We find that the local Newton step is also naturally robust to the non-stationarity in the mapping from the subspace to the objective function that can be introduced by subspace embeddings, which helps explain why our approach continues to perform well for some problems even as the ambient dimension reaches thousands or more.

Finally, we find that our acquisition includes a scale factor that balances gradient and Hessian learning whose optimal value must be estimated , e.g., Monte Carlo sampling; our empirical results show that performance is robust to the precise choice of this factor, and we use a simple default that avoids this extra computation. We prove a "vanishing power-function condition" showing that NeST-BO drives the Newton-step error to zero as batch size increases. As a result, the method fits squarely within the classical inexact/modified Newton viewpoint: once the step errors are sufficiently small, one recovers the standard fast local convergence behavior of Newton-type methods, while globalization via, e.g., dampling/line search safeguards yields the usual notion of global convergence to stationary points.

In summary, our key contributions are:

A curvature-aware local BO algorithm that explicitly targets the Newton step via a tractable and theoretically-sound acquisition function.

A scalable instantiation that runs NeST-BO in enlarging subspaces, reducing computation from $O{(d^{2})}$ to $O{(m^{2})}$, where $d$ and $m$ are the ambient and maximum subspace dimensions.

Theoretical guarantees showing that NeST-BO drives Newton-step error to zero and thus inherits the convergence behavior of modified Newton methods.

Extensive empirical results on more than 12 synthetic and real-world problems (ranging from 20d to $>$`<!-- -->`{=html}7000d), where NeST-BO variants yield large performance improvements over six state-of-the-art high-dimensional BO baselines.

## RELATED WORK

### Linear subspaces and embeddings

A common strategy for high-dimensional BO is to assume the objective varies mainly in a lower-dimensional subspace and reduce model complexity accordingly. REMBO projects the search into a random linear subspace and optimizes there, with guarantees when the effective dimension is small. ALEBO improves robustness by using a Mahalanobis kernel and linear constraints on the acquisition to respect the original box. HeSBO replaces dense projections with count-sketch-style sparse embeddings that preserve structure with negligible overhead. BAxUS introduces nested random subspaces that expand during the run and a mechanism to carry observations across enlargements, providing improved success probabilities and practical robustness. In this paper, to improve the scalability of our method, we adopt the BAxUS embedding and enlargement schedule but replace its trust-region-based optimizer with NeST-BO.

### Learning sparse structure

Another interesting strategy for tackling high-dimensional problems is to adaptively learn space substructure. SAASBO places a sparsity-promoting prior on inverse GP length-scales. This can be very effective when the active set is small and axis-aligned, but the fully Bayesian inference of the kernel hyperparameters makes the inference cost scale cubically with the number of evaluations, which greatly limit its ability to scale beyond fairly small sampling budgets.

### Local BO

Local BO restricts search to neighborhoods around the incumbent to mitigate the curse of dimensionality. TuRBO, a trust-region variant, maintains multiple local regions with adaptive sizes. Another line of work is directional local BO, which uses a GP to define a local step rule. GIBO reduces gradient posterior uncertainty and moves along the mean gradient, while MPD chooses the direction maximizing the posterior probability of descent. MinUCB forgoes direct gradient inference and instead minimizes the upper confidence bound (UCB) objective as a local step. Our approach differs by explicitly targeting the Newton step, which uses both gradient and Hessian predictions from the GP.

### "Vanilla BO works" in high dimensions

Several recent works show that standard BO can be competitive in high dimensions when properly designed. Hvarfner et al. scale a log-normal length-scale prior with dimension, yielding a strong "D-scaled" LogEI baseline. Xu et al. argue that poor length-scale initialization induces vanishing gradients in GPs with squared exponential (SE) kernels and show Matérn kernels or robust initialization can avoid this pathology. Papenmeier et al. analyze why such settings succeed, attributing gains to low effective dimensionality or benign benchmark structure rather than a general cure for high-dimensional problems. We include such strong "vanilla" baselines in our experiments to reflect these practices.

## PRELIMINARIES

### Problem Setup & Bayesian Optimization

We consider the following zeroth-order optimization problem over a $d$-dimensional space:

where the expensive function $f$ can only be accessed through noisy queries $y = {{f{({\mathbf{x}})}} + \epsilon}$ with i.i.d. Gaussian noise $\epsilon \sim {\mathcal{N}{(0,\sigma^{2})}}$. Bayesian optimization (BO) tackles by fitting a probabilistic surrogate $p{(\left. f \middle| \mathcal{D} \right.)}$ over available data $\mathcal{D}$ and uses it to select new evaluations by maximizing an acquisition function $\alpha{(\left. {\mathbf{x}} \middle| \mathcal{D} \right.)}$ that trades off exploration and exploitation. After exhausting the budget, the recommended solution is either the best observed point or the minimizer of the surrogate mean. Many acquisitions have been proposed including expected improvement (EI), upper confidence bound (UCB), knowledge gradient (KG), and entropy-based methods. We refer readers to Garnett for a full tutorial.

### Gaussian Processes and their Derivatives

We use Gaussian processes (GPs) as surrogates, which is the most popular surrogate model class in BO. A GP prior $f \sim {\mathcal{G}\mathcal{P}{(\mu,k)}}$ induces a joint Gaussian belief over any finite set of inputs; conditioning on the dataset $\mathcal{D}$ yields a posterior GP $\left. f \middle| \mathcal{D} \right. \sim {\mathcal{G}\mathcal{P}{(\mu_{\mathcal{D}},k_{\mathcal{D}})}}$ with closed-form posterior mean $\mu_{\mathcal{D}}$ and covariance (or kernel) function $k_{\mathcal{D}}$. A key property we repeatedly use in this work is that derivatives of a GP remain GPs because differentiation is a linear operator. Thus, the gradient ${{\mathbf{g}}{({\mathbf{x}})}} = {{\nabla f}{({\mathbf{x}})}}$ and Hessian ${{\mathbf{H}}{({\mathbf{x}})}} = {{\nabla^{2}f}{({\mathbf{x}})}}$ have analytic posterior means and covariances obtained by differentiating the kernel in the appropriate arguments. We collect the explicit formulas for $f$, $\mathbf{g}$, and $\mathbf{H}$ posteriors in Appendix A.

### Local BO using Gradients

Learning a globally accurate surrogate becomes data-hungry as $d$ grows because regret bounds for global BO (e.g., GP-UCB) scale exponentially with dimension unless strong structural assumptions hold. Local BO addresses this by focusing search near the incumbent and updating the model with more locally collected data. Gradient-informed methods refine this idea by explicitly selecting evaluations that reduce uncertainty about the local descent direction. A prominent example is the Gradient Information (GI) acquisition that underlies GIBO. Let ${\mathbf{x}}_{t}$ be the current iterate and ${\mathbf{Z}} \in {\mathbb{R}}^{b_{t} \times d}$ a batch of candidates. GI selects $\mathbf{Z}$ to maximally reduce the expected posterior covariance of the gradient at ${\mathbf{x}}_{t}$ given current data $\mathcal{D}$ after observing a new batch of points $({\mathbf{Z}},{\mathbf{y}})$:

The key observation is, since posterior covariances do not depend on the observed targets $\mathbf{y}$, this simplifies to minimizing a (squared) "power function" for the gradient defined as the trace of the posterior covariance:

This criterion encourages sampling along directions that most reduce gradient uncertainty, after which the algorithm steps along the GP posterior mean gradient. Theoretical analysis of GIBO showed that the convergence rate to a stationary point scales linearly in $d$, which is better than rates at which global optimization can find the global optimum.

Nguyen et al. revisit the GIBO template and show that the GP posterior mean gradient is not, in general, the direction that maximizes the posterior probability of descent, which motivates MPD: an acquisition that targets an upper bound on the one-step maximum descent probability together with updates along the most-probable descent direction. We include MPD as a strong baseline; NeST-BO builds on the same local gradient-learning viewpoint as GIBO but targets a second-order Newton step rather than a first-order descent direction.

### Newton's Method for Optimization

Newton's method (NM) is a classical algorithm for (unconstrained) local minimization of twice continuously differentiable objectives. Starting from ${\mathbf{x}}_{0} \in {\mathbb{R}}^{d}$, it makes the following updates:

where $\gamma_{t} > 0$ denotes the step size at iteration $t$. NM re-scales and rotates the gradient using local curvature. On well-behaved landscapes (e.g., in a neighborhood where $\mathbf{H}$ is positive definite), this makes progress far less sensitive to conditioning than first-order methods and yields local quadratic convergence near a (nondegenerate) minimizer, in contrast to the linear or sublinear rates typical of gradient schemes under comparable assumptions.

In the BO context, we do not get to directly observe $\mathbf{g}$ or $\mathbf{H}$, but their GP posteriors (implicitly) define a distribution over the Newton step ${{\mathbf{d}}{({\mathbf{x}})}} = {{\mathbf{H}}{({\mathbf{x}})}^{- 1}{\mathbf{g}}{({\mathbf{x}})}}$. NeST-BO is built around actively reducing the posterior uncertainty of the step ${\mathbf{d}}{({\mathbf{x}})}$, rather than estimating ${\mathbf{g}}{({\mathbf{x}})}$ and ${\mathbf{H}}{({\mathbf{x}})}$ separately. The thought is that, when the Newton step gets close to a local solution, the iteration advantage of NM can outweigh the per-step cost of learning curvature, yielding stronger sample efficiency than gradient-only methods like GIBO.

## NEWTON-STEP-TARGETED BAYESIAN OPTIMIZATION

### An Acquisition for the Newton Step

Let ${\mathbf{x}}_{t}$ be the current iterate and ${\mathbf{Z}} \in {\mathbb{R}}^{b_{t} \times d}$ a batch of candidates at which we might evaluate $f$. Our goal is to learn the Newton step ${{\mathbf{d}}{({\mathbf{x}})}} = {{\mathbf{H}}{({\mathbf{x}})}^{- 1}{\mathbf{g}}{({\mathbf{x}})}}$ at ${\mathbf{x}}_{t}$ under the GP posterior. Because ${\mathbf{d}}{({\mathbf{x}})}$ is non-Gaussian, its posterior covariance is not available in closed form; instead we derive a Reproducing Kernel Hilbert Space (RKHS) error bound (inspired by the results derived in ). Let the gradient and (vectorized) Hessian (squared) power functions at $\mathbf{x}$ be denoted by ${\pi_{\mathcal{D}}^{\mathbf{g}}{({\mathbf{x}})}} = {\operatorname{tr}\left( {\Sigma_{\mathcal{D}}^{\mathbf{g}}{({\mathbf{x}})}} \right)}$ and ${\pi_{\mathcal{D}}^{\mathbf{H}}{({\mathbf{x}})}} = {\operatorname{tr}\left( {\Sigma_{\mathcal{D}}^{{vec}{({\mathbf{H}})}}{({\mathbf{x}})}} \right)}$. Also, let $\mathcal{H}$ be the RKHS on $\mathcal{X}$ equipped with a reproducing kernel $k{( \cdot, \cdot )}$ and RKHS norm $\parallel \cdot \parallel_{\mathcal{H}}$. We can establish the following bound (see Appendix B for the proof):

### Theorem 1 (Newton-step error bound)

Let ${\varepsilon_{\mathcal{D}}{(\mathbf{x})}} = {\|{{\mathbf{d}{(\mathbf{x})}} - {{\hat{\mathbf{d}}}_{\mathcal{D}}{(\mathbf{x})}}}\|}$ denote the Newton-step error at $\mathbf{x}$ given data $\mathcal{D}$ with ${{\hat{\mathbf{d}}}_{\mathcal{D}}{(\mathbf{x})}} = {{\hat{\mathbf{H}}}_{\mathcal{D}}{(\mathbf{x})}^{- 1}{\hat{\mathbf{g}}}_{\mathcal{D}}{(\mathbf{x})}}$ where $\parallel \cdot \parallel$ is the standard Euclidean norm. Assume the kernel $k$ is stationary and four-times differentiable and that $\|{\mathbf{H}{(\mathbf{x})}^{- 1}}\|$ exists and is finite. For any $f \in \mathcal{H}$ (from the RKHS with reproducing kernel $k$) with ${\| f\|}_{\mathcal{H}} \leq B$, $\mathbf{x} \in \mathcal{X}$, and $\mathcal{D}$, the following bound holds:

where ${s_{\mathcal{D}}{(\mathbf{x})}} = {{\|{{\hat{\mathbf{H}}}_{\mathcal{D}}{(\mathbf{x})}^{- 1}}\|}^{2}{\|{{\hat{\mathbf{g}}}_{\mathcal{D}}{(\mathbf{x})}}\|}^{2}}$ is a scale factor that trades off gradient and Hessian information and $C_{\mathbf{x}} = {\sqrt{2}B{\|{\mathbf{H}{(\mathbf{x})}^{- 1}}\|}}$ is independent of $\mathcal{D}$.

Motivated by the Newton-step error bound in Theorem 1. ‣ 4.1 An Acquisition for the Newton Step ‣ 4 NEWTON-STEP-TARGETED BAYESIAN OPTIMIZATION"), our design goal at iteration $t$ is simple: choose a batch $\mathbf{Z}$ that will make the post-batch bound on the error as small as possible (in expectation) over the unobserved outcomes at $\mathbf{Z}$. Concretely, let ${B_{\mathcal{D}}{({\mathbf{x}}_{t})}} = {{\pi_{\mathcal{D}}^{\mathbf{g}}{({\mathbf{x}}_{t})}} + {s_{\mathcal{D}}{({\mathbf{x}}_{t})}\pi_{\mathcal{D}}^{\mathbf{H}}{({\mathbf{x}}_{t})}}}$, so that (5. ‣ 4.1 An Acquisition for the Newton Step ‣ 4 NEWTON-STEP-TARGETED BAYESIAN OPTIMIZATION")) is ${\varepsilon_{\mathcal{D}}{({\mathbf{x}}_{t})}} \leq {C_{{\mathbf{x}}_{t}}\sqrt{B_{\mathcal{D}}{({\mathbf{x}}_{t})}}}$. Since $C_{{\mathbf{x}}_{t}}$ is independent of the data, minimizing an upper bound on the expected step error is naturally achieved :

This is the direct analogue of GI, which chooses points to minimize a lookahead bound on the gradient error, as shown . The objective in is doing the same thing but on a lookahead bound for the error in the Newton step.

The remaining step is to simplify. Under a GP with Gaussian observation noise, the posterior covariances of derivatives at ${\mathbf{x}}_{t}$ after conditioning on $\mathcal{D} \cup {({\mathbf{Z}},{\mathbf{y}})}$ do not depend on the realized values $\mathbf{y}$; they depend only on the locations $\mathbf{Z}$, so the only term in that requires a lookahead expectation is $s_{\mathcal{D} \cup {({\mathbf{Z}},{\mathbf{y}})}}{({\mathbf{x}}_{t})}$, which depends on posterior means through $\hat{\mathbf{g}}$ and $\hat{\mathbf{H}}$. Using this fact, reduces to our following proposed Newton Step Targeting (NeST) acquisition function:

NeST is composed of three main terms: (i) $\pi_{\mathcal{D} \cup {\mathbf{Z}}}^{\mathbf{g}}{({\mathbf{x}}_{t})}$ is the trace of the covariance of the one-step lookahead gradient at ${\mathbf{x}}_{t}$, (ii) $\pi_{\mathcal{D} \cup {\mathbf{Z}}}^{\mathbf{H}}{({\mathbf{x}}_{t})}$ is the trace of the covariance of the one-step lookahead vectorized Hessian, and (iii) ${\mathbb{E}}_{{\mathbf{y}} \mid {\mathcal{D},{\mathbf{Z}}}}\left\{ {s_{\mathcal{D} \cup {({\mathbf{Z}},{\mathbf{y}})}}{({\mathbf{x}}_{t})}} \right\}$ is a scale factor that weights these two terms. We can interpret (i) and (ii) as measures of the information content about quantities of interest (mainly gradient and Hessian at our current point) and (iii) as a term that adaptively balances gradient and Hessian information. Note that, since ${\|{{\mathbf{H}}^{- 1}{({\mathbf{x}})}{\mathbf{g}}{({\mathbf{x}})}}\|} \leq {{\|{{\mathbf{H}}^{- 1}{({\mathbf{x}})}}\|}{\|{{\mathbf{g}}{({\mathbf{x}})}}\|}}$, we can also think of this term as a conservative proxy for the squared step length and thus upweights Hessian information when NM may take large steps.

### A practical family

The expectation over the scale factor in does not have a simple closed-form expression and thus would need to be estimated using Monte Carlo (MC) sampling in practice (see Appendix C.1 for details). This is mainly due to the fact that $s_{\mathcal{D} \cup {({\mathbf{Z}},{\mathbf{y}})}}$ is a nonlinear function of $\mathbf{y}$ and thus non-Gaussian in general. Through some empirical testing shown in Appendix C, we observed relatively low sensitivity in performance to the precise scale factor, which motivates the following computationally cheaper acquisition:

with a pre-determined ${\hat{s}}_{t} > 0$ that is independent of $\mathbf{Z}$. This recovers GI when ${\hat{s}}_{t} = 0$ and focuses more on curvature as ${\hat{s}}_{t}$ increases. In Section 4.4, we show the NeST samples can drive the bound in (5. ‣ 4.1 An Acquisition for the Newton Step ‣ 4 NEWTON-STEP-TARGETED BAYESIAN OPTIMIZATION")) to zero as the batch size increases for any choice of scale factor.

### The NeST-BO Algorithm

Algorithm 1 summarizes the simple version of the loop. At iterate ${\mathbf{x}}_{t}$, choose a batch ${\mathbf{X}}_{t}$ by minimizing at ${\mathbf{x}}_{t}$; update the GP with the new observations; then move along the predicted Newton step with some step size. Note there are a number of practical implementation details, which we discuss more in the next section.

Since we are attempting to learn both the gradient and Hessian at ${\mathbf{x}}_{t}$, one can in fact easily adapt this algorithm to use a step direction from any form of, e.g., damped NM ) or NM with line search. We do not attempt to systematically compare different options in this work; instead we go with a standard "hybrid" implementation that uses Newton steps when they well-behaved and otherwise revert to gradient steps.

We provide an illustration and visual comparison of NeST-BO (top) to GIBO (bottom) in Figure 1, which demonstrates the advantages of simultaneously learning gradient and Hessian (curvature) information.

Inputs: initial iterate x0 ∈ ℝd; initial data 𝒟0; batch sizes {bt}; step sizes {γt}; scale factors {ŝt}; GP hyperparameters; and total number of iterations T.

6: Update GP posterior with 𝒟t + 1.
7: Compute $\hat{\mathbf{g}}\leftarrow{{\hat{\mathbf{g}}}_{\mathcal{D}_{t + 1}}{({\mathbf{x}}_{t})}}$ and $\hat{\mathbf{H}}\leftarrow{{\hat{\mathbf{H}}}_{\mathcal{D}_{t + 1}}{({\mathbf{x}}_{t})}}$.
8: Solve ${\hat{\mathbf{H}}{\mathbf{v}}} = \hat{\mathbf{g}}$ for ${{\hat{\mathbf{d}}}_{\mathcal{D}_{t + 1}}{({\mathbf{x}}_{t})}}\leftarrow{\mathbf{v}}$.
9: Update iterate: ${\mathbf{x}}_{t + 1} = {{\mathbf{x}}_{t} - {\gamma_{t}{\hat{\mathbf{d}}}_{\mathcal{D}_{t + 1}}{({\mathbf{x}}_{t})}}}$.

Figure 1: Top: NeST-BO’s acquisition ${\overset{\sim}{\alpha}}_{NeST}$; Bottom: GIBO’s acquisition ${\overset{\sim}{\alpha}}_{GI}$ on a 2D test function at iterate xt (blue circle). Darker background indicates larger acquisition value. Red square: location of the true Newton step. Blue triangle: GP-predicted Newton step. Orange star: acquisition minimizer. Black crosses: Past evaluation points. NeST-BO places samples away from xt along directions informative for curvature, rapidly shrinking the Newton-step error bound; GI tends to oversample near xt, slowing curvature identification.

### Implementation Details

Algorithm 1 describes an idealized NeST-BO loop used for exposition. In practice, just as vanilla NM can be brittle without safeguards, we found it helpful to use a slightly "hardened" variant for all experiments. The key point is that NeST-BO's value is in where it samples at each iteration (i.e., producing high-quality local gradient/Hessian information), so we can borrow standard Newton-style safeguards without changing the core idea. For completeness, the full pseudocode for our practical implementation is given in Appendix D. We summarize the main choices here.

### GP hyperparameters

In most applications, kernel hyperparameters are not known a priori. We thus need to fit the GP by maximizing the marginal log likelihood, which is standard in the BO literature. Our method does not rely on this specific estimator; any hyperparameter learning procedure can be used.

### Moving direction

NeST-BO is meant to behave like a local Newton-type method once it enters a well-behaved neighborhood. When ${\hat{\mathbf{H}}}_{\mathcal{D}}{({\mathbf{x}}_{t})}$ is positive definite (and not too ill-conditioned), this is a descent direction for the GP mean and typically behaves as expected. If ${\hat{\mathbf{H}}}_{\mathcal{D}}{({\mathbf{x}}_{t})}$ is indefinite or numerically unstable to invert, we interpret this as a signal that we are not yet in a regime where Newton steps are reliable, and we revert to a length-scale-normalized gradient step. This is a simple and robust fallback; many other Newton safeguards (e.g., damping/regularization or trust-region updates) could also be used, but we did not attempt to exhaustively test (or internally tune) these variants, which would be valuable future work.

### Batch versus sequential selection

Although supports joint batch optimization, we select points greedily. After choosing each point, we update the posterior covariance deterministically (note that the power functions do not depend on the realized outcomes), and then re-optimize to choose the next point. This replaces a single $b_{t}d$-dimensional search with $b_{t}$ separate $d$-dimensional searches and naturally discourages near-duplicate selections, since conditioning on a chosen location reduces posterior variance around it. In our preliminary tests, greedy selection closely matched joint optimization.

### Step size

We use a standard Armijo backtracking line search on the GP mean $\mu_{\mathcal{D}}$ along the chosen direction. This gives a lightweight safeguard against overly aggressive steps without requiring additional function evaluations, and we cap the number of backtracking iterations using standard defaults. There has been recent work on greedy NM, which suggests it can be advantageous to allow for step sizes larger than 1, but we do not consider that here.

### Scale factor

The scale ${\hat{s}}_{t}$ in controls how strongly (approximate) NeST emphasizes curvature (Hessian) uncertainty relative to gradient uncertainty. For the main experiments, we use a simple deterministic proxy ${\hat{s}}_{t} = 1$, which performed reliably across problems and dimensions. Appendix C.2 provides a broader comparison over ${\hat{s}}_{t}$ choices. We also tested a "plug-in" variant ${\hat{s}}_{t} = {s_{\mathcal{D}}{({\mathbf{x}}_{t})}}$ that neglects the lookahead dependence on $({\mathbf{Z}},{\mathbf{y}})$ (Appendix C.3); performance was very similar between these options, so we default to ${\hat{s}}_{t} = 1$ for simplicity.

### Theoretical Analysis

Let $\varepsilon_{t} = {\varepsilon_{\mathcal{D}_{t + 1}}{({\mathbf{x}}_{t})}}$ denote the Newton-step error after iteration $t$. By Theorem 1. ‣ 4.1 An Acquisition for the Newton Step ‣ 4 NEWTON-STEP-TARGETED BAYESIAN OPTIMIZATION"), $\varepsilon_{t}$ is controlled by posterior uncertainty in the *local derivatives* at ${\mathbf{x}}_{t}$; specifically, the power functions appearing in (5. ‣ 4.1 An Acquisition for the Newton Step ‣ 4 NEWTON-STEP-TARGETED BAYESIAN OPTIMIZATION")). This motivates a simple designability condition:

Vanishing power-function condition (VPC). The NeST design objective ${\pi_{\mathcal{D}_{t + 1}}^{\mathbf{g}}{({\mathbf{x}}_{t})}} + {{\hat{s}}_{t}\pi_{\mathcal{D}_{t + 1}}^{\mathbf{H}}{({\mathbf{x}}_{t})}}$ can be made arbitrarily small as $b_{t}$ increases.

VPC is not an abstract assumption on $\varepsilon_{t}$; it ties the step error to concrete, design-controllable posterior covariances. A key subtlety is that NeST-BO cannot directly minimize the right-hand side of (5. ‣ 4.1 An Acquisition for the Newton Step ‣ 4 NEWTON-STEP-TARGETED BAYESIAN OPTIMIZATION")) because the scale term $s_{\mathcal{D}_{t + 1}}{({\mathbf{x}}_{t})}$ is only revealed after the batch is observed. Nevertheless, the bound applies to the realized step error under any sampling rule, and VPC can be verified constructively for NeST. We state the main idea informally below; the complete statement and proof are in Appendix E.1.

### Theorem 2 (VPC under NeST sampling; informal)

Fix an iteration $t$ and the current iterate $\mathbf{x}_{t}$. For a batch $\mathbf{Z} = {(\mathbf{z}_{1},\ldots,\mathbf{z}_{b_{t}})} \in \mathcal{X}^{b_{t}}$, let ${\Phi_{t}{(\mathbf{Z})}} = {{\hat{\alpha}}_{NeST}{(\left. \mathbf{Z} \middle| {\mathbf{x}_{t},\mathcal{D},{\hat{s}}_{t}} \right.)}}$ be short for the approximate NeST acquisition function with ${\hat{s}}_{t} > 0$. Under mild domain and kernel regularity conditions, the following hold.

Let $b^{\star} = {d^{2} + d + 1}$. Then, in the noiseless setting, the optimal NeST design value can be driven to zero:

Equivalently, for every $\epsilon > 0$ and every $b_{t} \geq b^{\star}$, there exists a batch $\mathbf{Z}_{\epsilon}$ such that ${\Phi_{t}{(\mathbf{Z}_{\epsilon})}} \leq \epsilon$. Moreover, one explicit candidate design achieving this is a symmetric $b^{\star}$-point centered-difference stencil at radius $h$, for which ${\Phi_{t}{(\mathbf{Z}_{h})}} \lesssim h^{4}$ as $h\rightarrow 0$.

With i.i.d. Gaussian noise of variance $\sigma^{2}$, using $m$ replicates per location is equivalent to observing averaged responses with variance $\sigma^{2}/m$. Thus, for every $\epsilon > 0$ there exist $h$ and $m$ such that the corresponding replicated design satisfies ${\Phi_{t}{(\mathbf{Z}_{h}^{(m)})}} \leq \epsilon$.

An important consequence is that, once NeST-BO is operating in a neighborhood where NM is well-conditioned, VPC implies $\varepsilon_{t}\rightarrow 0$ as the batch size increases, and NeST-BO asymptotically inherits the local quadratic convergence rate of NM (full statement and proof in Appendix E.2). Finally, the VPC statement itself does not depend on the particular choice of scale factor beyond requiring ${\hat{s}}_{t} > 0$. Thus, the simplified acquisition in retains the same asymptotic guarantee, with the caveat that the argument is inherently for large enough batches.

### Scaling NeST-BO via Subspaces

The main computational bottleneck for NeST-BO in high ambient dimension $d$ is the Hessian term $\pi_{\mathcal{D} \cup {\mathbf{Z}}}^{\mathbf{H}}{({\mathbf{x}}_{t})}$, which scales quadratically in $d$. We propose to address this by instantiating NeST-BO inside embedded subspaces ${\mathbf{v}} \in {\mathbb{R}}^{m}$ of size $m \ll d$. We adopt the nested, sparse random-embedding scheme of BAxUS -- bins of input coordinates are hashed into $m$ target coordinates with random signs, and the target dimension is increased over time by splitting bins while retaining observations across embeddings. This approach preserves past data under splits and increases the probability that the subspace contains an optimizer as $m$ grows.

We run NeST-BO in the subspace $\mathbf{v}$, map the candidates back to the ambient dimension ${\mathbf{x}} = {{\mathbf{S}}^{\top}{\mathbf{v}}}$ (where ${\mathbf{S}}^{\top} \in {\mathbb{R}}^{d \times m}$ is the projection matrix) for evaluation, and update the GP in the embedded subspace coordinates. This reduces the per-candidate curvature cost from $O{(d^{2})}$ to $O{(m^{2})}$ while preserving the step-targeting principle. Compared to the original BAxUS algorithm, which couples its embedding with a variant of TuRBO, our version replaces TuRBO with NeST-BO; in problems where curvature matters, we find that this can can substantially accelerate optimization progress (see results in Section 5).

Lastly, note that our theoretical results related to VPC are proved only for NeST-BO in the original $d$-dimensional space, and they do not directly extend to the subspace variant. Intuitively, the VPC proof relies on constructing $d$-dimensional designs that can drive the full gradient and Hessian power functions at ${\mathbf{x}}_{t}$ to zero, whereas a fixed low-dimensional embedding only controls derivative information within the embedded coordinates and may not capture curvature directions relevant in ${\mathbb{R}}^{d}$. The BAxUS-style embedding should thus be viewed as a practical scalability heuristic that leverages the NeST sampling principle.

## RESULTS

We now benchmark NeST-BO and its subspace variant, labeled NeST-BO-sub, against strong local and global BO baselines: TuRBO, GIBO, MPD, MinUCB, BAxUS, and a "vanilla" GP-BO configured with dimensionally calibrated priors and LogEI (we label this *D-scaled LogEI*). We also include Sobol sampling as a non-model baseline.

Unless a global minimizer is known, we report the minimum observed value; otherwise we show simple regret (in log scale). Curves display the median across $10$ independent replicates with $\pm$ one standard error as the shaded band. Implementation details (e.g., models, hyperparameter updates, acquisition optimization, and the precise evaluation budgets for each task) are provided in Appendix F. In short, we used a common SE kernel across methods and standard GP training and acquisition optimizers from BoTorch; hyperparameters and method-specific settings follow prior work and are held consistent across tasks to keep comparisons fair. Due to space limitations, additional ablations and diagnostics appear in Appendix G. The code is available on GitHub:

### Synthetic Test Functions

We consider two regimes relevant to our method. Moderate dimension ($d = 20$): Sphere, Griewank, and Ackley. High dimension with sparse structure ($d = 1000$ with $d_{\text{eff}} = 30$ relevant variables): Griewank, Ackley, and Rosenbrock; the remaining coordinates are dummies and the algorithms are not told which ones are active. These are commonly chosen test problems in the BO literature; formal definitions are given in Appendix F.3. Figure 2 (first six panels in the top two rows) summarizes the results.

Figure 2: Summary of performance versus evaluations for all synthetic and real-world problems and all methods. Each panel shows either simple regret (log scale; when the global minimizer is known) or the minimum observed value (otherwise). Curves are medians across 10 runs; shading is ± one standard error. Top two rows: synthetic problems (20d and 1000d with 30 active variables). Bottom two rows: real-world tasks (control, planning, and high-dimensional model selection). See Appendix F for the full protocol and Appendix G for extended studies.

On the $d = 20$ problems, NeST-BO consistently matches or outperforms all non-subspace baselines. A common pattern is an initial period with slower progress when far from a minimizer (before curvature is accurately estimated) followed by a steep drop once the iterate enters a well-behaved neighborhood. As several steps accumulate, the estimated Newton step better aligns with the true local geometry, further accelerating progress -- consistent with our Newton-step error bound, which tightens as the gradient and Hessian power functions shrink. Subspace methods start from stronger initial values by design (they restrict the initial design and acquisitions), but NeST-BO-sub ultimately achieves the lowest regret and, notably, improves over BAxUS across all three problems. These results indicate that how one moves inside a subspace matters, i.e., curvature-aware Newton updates can be more effective than trust-region moves, even when both operate in the same embedding space.

On the $d = 1000$ sparse suite, subspaces are essential. Methods that attempt to learn gradients and/or Hessians in the ambient space require $O{(d)}$ queries per iteration and cannot meaningfully progress under our fixed budgets (e.g., 200 evaluations), so we do not include them here. NeST-BO-sub clearly dominates BAxUS, D-scaled LogEI, and TuRBO, achieving substantially lower regret on both Ackley and Griewank. TuRBO's trust-region strategy is disadvantaged in very high dimensions, where large local diameters push pairwise distances into regimes that degrade GP fit and acquisition gradients; in contrast, NeST-BO-sub converts a handful of targeted samples near the iterate into accurate Newton steps inside the selected subspace (that can expand as iterations proceed), which drives fast local improvement.

### Mid- to High-Dim. Real-World Tasks

We evaluate six real-world benchmarks spanning reinforcement learning (RL) control, robotic planning, and large-scale hyperparameter tuning. Control: Lunar Lander ($d = 12$) and Swimmer ($d = 16$) from OpenAI Gymnasium; the objective is the negative episodic return (reward sign flipped). Planning: Robot Pushing ($d = 14$) and Rover Trajectory ($d = 60$) from Wang et al.; Eriksson et al., both optimized as negative reward. Very high-dimension: Ant ($d = 888$) -- a MuJoCo quadruped with 8-dimensional action space and 111-dimensional observations, yielding a linear state-feedback policy with 888 parameters -- and Leukemia ($d = 7129$), a weighted Lasso problem with 7129 hyperparameters from LassoBench. Task definitions, bounds, and initialization protocols are summarized in Appendix F.4. Figure 2 (last six panels in bottom two rows) reports median performance with $\pm$ one standard error bands.

In the mid-dimensional group ($d \leq 60$), NeST-BO is consistently state of the art or competitive, achieving the lowest average value in the fewest iterations for Lunar Lander, Robot Pushing, and Swimmer. On Rover Trajectory, NeST-BO-sub edges out NeST-BO, aligning with the intuition that embeddings can capture useful structure as dimensionality and coupling grow. On Lunar Lander and Swimmer, however, subspaces can slightly hurt performance, suggesting most coordinates contribute and the ambient space is preferable.

In the very high-dimensional group, NeST-BO-sub is again the best-performing method. On Ant ($d = 888$), D-scaled LogEI and TuRBO show little-to-no improvement over their starting values, while BAxUS improves but plateaus well above NeST-BO-sub. The Ant landscape is both non-stationary and ill-conditioned; length-scale calibration alone (as in D-scaled LogEI) can over-smooth such objectives, and trust-region steps struggle to adapt their geometry. On Leukemia ($d = 7129$), NeST-BO-sub continues to improve throughout the budget and achieves the best final objective, whereas other methods stagnate early.

### Other Methods in Same Subspace

A natural question raised by our subspace results in Figure 2 is whether NeST-BO's gains are primarily due to the embedding, or whether targeting the local Newton step continues to matter once we restrict the search to lower-dimensional subspaces. To isolate these effects, we compare NeST-BO-sub to two strong baselines that use the same subspace machinery: (i) GIBO-sub, i.e., GIBO run in the subspace using its length-scale-normalized gradient step and (ii) D-scaled LogEI-sub, i.e., standard LogEI run in the subspace using the GP prior . For context, we also include BAxUS. Figure 3 shows the embedding is not the whole story. NeST-BO-sub drives regret down by several orders of magnitude relative to GIBO-sub and D-scaled LogEI-sub (the latter two plateau near $\sim 10^{0}$ on the log scale), while NeST-BO-sub continues improving throughout the budget. On Ackley, the same pattern holds: NeST-BO-sub reaches substantially lower regret and converges faster, while the other subspace methods level off earlier.

Figure 3: Optimization of 1000-dimensional Griewank and Ackley with 30 active variables. All -sub variants operate using the same BAxUS-style embedding approach. Median simple regret (log scale) with ± one standard error shading across 10 runs.

## CONCLUSIONS

This work presents NeST-BO, a curvature-aware local Bayesian optimization (BO) method that selects samples to shrink a one-step lookahead bound on Newton-step error and then moves with a damped Newton update. Theoretical analysis establishes a vanishing power-function condition that holds under NeST-BO sampling, implying the algorithm inherits (inexact) Newton guarantees while our experiments show consistent gains over state-of-the-art local and high-dimensional BO baselines on synthetic and real-world problems, including tasks with several thousands of variables (when combined with a subspace variant to enhance scalability). Looking ahead, two promising directions for future research include investigating improved subspace embedding strategies and improving numerical efficiency of the acquisition optimization by better exploiting kernel structure and sparsity for derivative-aware GPs.
