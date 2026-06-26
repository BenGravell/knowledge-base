<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sampling-based Model Predictive Control Using Trust Regions

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sampling-based model predictive control (MPC) algorithms, such as model predictive path integral (MPPI), enable approximate, gradient-free solutions to optimal control problems by drawing samples from a proposal distribution, evaluating their trajectory costs, and updating the proposal parameters accordingly. However, these approaches typically rely on heuristics for adjusting hyperparameters, such as temperature or momentum, or manual tuning. We propose a trust region formulation for sampling-based MPC that constrains updates of the proposal distribution via a principled Kullback-Leibler (KL) divergence bound and, optionally, an entropy lower bound. This replaces heuristic hyperparameter adaptation with values that are optimal w.r.t. the underlying Lagrangian. We further improve sample efficiency and convergence by combining the trust region update with deterministic localized cumulative distribution (LCD)-based sampling. Experiments on two benchmark environments demonstrate that the proposed trust region update achieves faster convergence and better sample efficiency in low-sample and low-iteration regimes, especially when paired with deterministic LCD-based sampling.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sampling-based model predictive control methods, such as cross-entropy method--model predictive control and model predictive path integral, have gained popularity for solving complex optimal control problems due to their ability to efficiently parallelize computations and handle arbitrary cost functions and system dynamics.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

These methods iteratively refine a parameterized proposal probability density function over control sequences by drawing samples, evaluating their trajectory costs, and updating the proposal parameters accordingly. Importance-weighting-based variants such as standard model predictive path integral, and iterative extensions thereof assign weights to the sampled control sequences based on their associated trajectory costs, thereby using a temperature parameter to control the sharpness of the weighting. This parameter is typically held constant or adjusted heuristically during optimization. Similarly, cross-entropy method-based methods rely on momentum-style smoothing to prevent premature collapse of the proposal distribution. These heuristics are often difficult to tune and may compromise convergence or performance across different problem settings.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by the success of trust region methods in reinforcement learning, where principled Kullback--Leibler-constrained updates have largely replaced heuristic parameter tuning, we propose to transfer these ideas to sampling-based model predictive control. Specifically, for each proposal update, we constrain the new proposal to remain within a bounded divergence from the previous one. The resulting constrained optimization problem is solved via Lagrange multipliers, with optimal hyperparameters obtained from the dual formulation. The updated proposal is then projected back onto the original distribution family (e.g., Gaussian), yielding a feasible distribution from which control sequences are sampled in the subsequent iteration.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Orthogonal to the choice of update rule, the sampling method directly affects the quality and smoothness of the control. In our previous work, we demonstrated that exchanging random samples with precomputed, optimally-placed deterministic samples based on localized cumulative distributions yield improved sample efficiency and smoother control sequences. localized cumulative distribution-based sampling shows superior coverage and inherently positions the samples homogeneously, i.e., it induces a smooth distribution of the sizes of the sample-free gaps between them. It is therefore well-suited for integration and optimization tasks. In particular, it integrates well with trust region updates, which restrict the proposal to remain close to the original and thus to regions with high sample coverage.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contribution", "weight": 1.0} -->

We propose a trust region formulation for sampling-based model predictive control that replaces heuristic proposal adaptations with principled Kullback--Leibler-constrained updates derived from dual optimization. Building on our previous work, we further combine the trust region update with deterministic localized cumulative distribution-based sampling to improve sample efficiency. Both contributions are evaluated on two benchmark control tasks and compared against heuristic baselines across multiple sampling strategies, including random and low-discrepancy sampling (Sobol and Halton ).

<!-- chunk {"id": "body-0008", "role": "body", "section": "III-A Sampling-based MPC", "weight": 1.0} -->

A prominent approach to sampling-based model predictive control is the cross-entropy method, which iteratively updates a proposal probability density function by selecting low-cost elite samples and maximizing their likelihood. For Gaussian proposals, the updated moments for the next iteration are computed as the empirical mean and covariance of the selected control sequences. To improve numerical robustness and reduce premature concentration of the proposal, many implementations introduce a momentum (or smoothing) term across iterations. For the mean update, this is typically written as where $\hat{{\underline{\xi}}}_{j}^{\prime}$ denotes the (unsmoothed) mean of the elite set.

<!-- chunk {"id": "body-0009", "role": "body", "section": "III-A Sampling-based MPC", "weight": 1.0} -->

Related model predictive path integral-like methods also perform (iterative) proposal refinement, but they rely on importance weighting of sampled control sequences instead of hard elite selection. The weights are given by and are used to compute the updated Gaussian moments as the control sequences' weighted sample mean and covariance. The inverse temperature $\lambda$ controls the exploration-exploitation trade-off and remains constant or is adapted heuristically during optimization. Furthermore, iterative model predictive path integral variants additionally employ momentum-style smoothing ˜4 of the proposal update, analogous to cross-entropy method, to mitigate premature convergence.

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-A Sampling-based MPC", "weight": 1.0} -->

Orthogonal to the above methods, improvements in sampling efficiency and smoothness of the optimized control inputs have been achieved by using low-discrepancy sequences, such as the Halton sequence, time-correlated noise, or, as in our previous work, by using optimal deterministic samples based on the localized cumulative distribution.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-B Trust Regions in reinforcement learning", "weight": 1.0} -->

In reinforcement learning, trust region methods provide principled policy updates that balance exploration and exploitation while ensuring stable learning. The core idea is to limit the update step by constraining the Kullback--Leibler divergence between the new policy and the old policy, preventing drastic changes that can lead to performance degradation. Adding an entropy constraint further encourages exploration and prevents premature convergence to suboptimal policies. These concepts have been established for policy search, step-based reinforcement learning, episodic reinforcement learning, and gradient-based stochastic optimal control with quadratic reward functions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Trust Region model predictive control", "weight": 1.0} -->

Inspired by the success of trust region methods in reinforcement learning, we propose a trust region formulation for sampling-based model predictive control to improve the optimization process and remove the need for heuristic parameter adaptation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Trust Region model predictive control", "weight": 1.0} -->

At iteration $j$, let $f_{j}$ denote the current proposal probability density function over control sequences ${\underline{\xi}}$, and $f_{j+1}$ the next proposal probability density function to be optimized. The trust region optimization problem is then given by where $D_{\mathrm{KL}}(\cdot\|\cdot)$ is the Kullback--Leibler divergence, $H(\cdot)$ is the entropy, $\epsilon$ is the maximum allowed Kullback--Leibler divergence between consecutive proposals, $H_{\min}$ is the minimum required entropy of the proposal, and the last constraint ensures that $f_{j+1}$ is normalized. The Kullback--Leibler constraint prevents overly aggressive updates, while the minimum entropy constraint encourages exploration and mitigates premature collapse of the proposal. Note that the entropy constraint is optional and can be omitted if task-specific knowledge suggests that proposal collapse is not a concern, e.g., when a small number of iterations is used.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Trust Region model predictive control", "weight": 1.0} -->

To solve the constrained problem, we form the Lagrangian where $\eta$, $\alpha$, and $\nu$ are the Lagrange multipliers associated with the Kullback--Leibler divergence, entropy, and normalization constraints, respectively. To find the optimal proposal for the next iteration, we take the functional derivative of $\mathcal{L}$ w.r.t. $f_{j+1}$ and set it to zero (see Sec.˜-A for details). The optimal proposal is then given by where $Z_{\eta,\alpha}$ is the normalization constant, written as expectation over $f_{j}$. Since the multiplier $\nu$ is implicitly handled in the normalization, it can be omitted from subsequent derivation steps. Note that in the case of a Gaussian proposal $f_{j}({\underline{\xi}})$, for $\alpha>0$, $f_{j+1}^{\ast}$ is generally non-Gaussian.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Trust Region model predictive control", "weight": 1.0} -->

However, for $\alpha=0$, the Gaussianity is preserved.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Trust Region model predictive control", "weight": 1.0} -->

By substituting $f_{j+1}^{\ast}$ back into the simplified Lagrangian $\mathcal{L}(f_{j+1}^{\ast},\eta,\alpha)$ (see Sec.˜-B), we obtain the dual function which we use to find the optimal Lagrange multipliers $\eta^{\ast}$ and $\alpha^{\ast}$ by numerically solving the dual problem Since the optimization over $\eta$ and $\alpha$ is always two-dimensional (in particular, it is independent of the control input dimension and horizon length), standard gradient-based solvers are efficient in practice. The gradient of the dual function $\nabla g(\eta,\alpha)$ is given by where the partial derivatives of $\log Z_{\eta,\alpha}$ are Note that the gradient is entirely written in terms of expectations of $f_{j}$. Consequently, the gradient can be estimated from samples drawn from $f_{j}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Trust Region model predictive control", "weight": 1.0} -->

Once the optimal Lagrange multipliers $\eta^{\ast}$ and $\alpha^{\ast}$ have been obtained, the optimal proposal probability density function $f_{j+1}^{\ast}$ follows directly from ˜10. We can derive a Dirac-mixture approximation of $f_{j+1}^{\ast}$ based on samples drawn from $f_{j}$ and weights Finally, we project our Dirac-mixture approximation of $f_{j+1}^{\ast}$ onto the same parametric form as the original proposal probability density function, e.g., via moment matching for Gaussians, or expectation--maximization for Gaussian mixtures. In this work, we use Gaussian proposals, which yield a closed-form update for the new mean $\hat{{\underline{\xi}}}_{j+1}$ and covariance ${{\mathbf{C}}}_{j+1}$, expressed in terms of the weighted empirical sample mean and covariance.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Trust Region model predictive control", "weight": 1.0} -->

Notably, when $\alpha^{\ast}=0$, this projection does not introduce additional error, as the true $f_{j+1}^{\ast}$ is Gaussian. In the general case, however, the projection incurs an additional approximation error.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Trust Region model predictive control", "weight": 1.0} -->

Although different in derivation, the resulting weights ˜19 exhibit a form similar to those in ˜5 used by model predictive path integral-like methods. In particular, when the entropy constraint is inactive, i.e., $\alpha^{\ast}=0$, the two formulations coincide exactly. Importantly, however, our approach yields optimal weights in a principled manner from the trust region formulation, thereby eliminating the need for heuristic hyperparameter adaptation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Algorithmic Improvements", "weight": 1.0} -->

Beyond the trust region formulation, we introduce several algorithmic improvements. An overview is provided in Alg.˜1, where the additional steps are highlighted in blue. Among these, the sampling method is a central design choice: we use random sampling as a baseline and introduce low-discrepancy and deterministic localized cumulative distribution-based sampling as an extension.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Algorithmic Improvements", "weight": 1.0} -->

Input: State ${\underline{x}}_{k}$, initial parameters ${\underline{\theta}}_{0}=(\hat{{\underline{\xi}}}_{0},{{\mathbf{C}}}_{0})$, buffered samples from previous step 1 Warm start last proposal mean and buffered samples 3 Sample ${\underline{u}}^{}_{k:k+N_{\mathrm{H}}-1},\ldots,{\underline{u}}^{(N)}_{k:k+N_{\mathrm{H}}-1}\sim f(\cdot;{\underline{\theta}}_{j})$ 4 Add saved samples from buffer 5 Clip samples to input bounds Trajectory shooting using ˜3 Evaluate costs

<!-- chunk {"id": "body-0022", "role": "body", "section": "Algorithmic Improvements", "weight": 1.0} -->

$\{J_{k}({\underline{u}}^{(i)}_{k:k+N_{\mathrm{H}}-1})\}_{i=1}^{N}$ using ˜2 6 Solve dual problem ˜13 7 Update proposal parameters ${\underline{\theta}}_{j+1}$ (weighted sample mean and covariance) using ˜19 8 Add NBuffer best samples to buffer return first control ${\underline{u}}_{k}^{*}$ from best sampled sequence Algorithm 1 Trust Region MPC Step

<!-- chunk {"id": "body-0023", "role": "body", "section": "V-A Sampling Methods", "weight": 1.0} -->

We propose to use deterministic samples based on localized cumulative distributions to represent the isotropic standard normal distribution $\mathcal{N}({\underline{\xi}};{\underline{0}},{{\mathbf{I}}})$ optimally with a fixed number of samples. The optimization is done *offline*, and these samples are stored for use in optimization iterations. For this, we use our Python package^11^1 At each iteration $j$ the stored samples are mapped to match the proposal parameters ${\underline{\theta}}_{j}=(\hat{{\underline{\xi}}}_{j},{{\mathbf{C}}}_{j})$ via where ${{\mathbf{L}}}_{j}$ satisfies ${{\mathbf{C}}}_{j}={{\mathbf{L}}}_{j}{{\mathbf{L}}}_{j}^{\top}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "V-A Sampling Methods", "weight": 1.0} -->

A random rotation matrix ${{\mathbf{R}}}_{j}$ is drawn each iteration from the special orthogonal group $SO(d_{{\xi}})$ (orthogonal matrices with determinant $+1$). Applying the rotation before scaling preserves the optimality because the standard normal distribution is rotationally invariant, while the random rotation introduces stochasticity that improves exploration. Fig.˜1 illustrates the precomputed sample set and the transformation.

<!-- chunk {"id": "body-0025", "role": "body", "section": "V-A Sampling Methods", "weight": 1.0} -->

As alternatives, we also consider scrambled (randomized) low-discrepancy sampling using Sobol and Halton sequences, as well as standard random sampling. Note that the root mean square error of random sampling for approximating expectations (integration) decreases proportionally to $N^{-\frac{1}{2}}$, while low-discrepancy sampling scales proportionally to $(\log N)^{d_{{\xi}}}N^{-1}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "V-A Sampling Methods", "weight": 1.0} -->

In comparison to low-discrepancy sampling, localized cumulative distribution-based sampling has the advantage of allowing deterministic samples to be optimized directly for Gaussians. In contrast, low-discrepancy sampling, such as Halton and Sobol, requires a transformation from a uniform distribution to a Gaussian distribution, which can introduce additional error and complexity.

<!-- chunk {"id": "body-0027", "role": "body", "section": "V-A Sampling Methods", "weight": 1.0} -->

(a) Standard normal samples Figure 1: Example showing 25 two-dimensional deterministic samples, where the probability density function is indicated by the background color. Adapted version.

<!-- chunk {"id": "body-0028", "role": "body", "section": "V-B Standard Improvements", "weight": 1.0} -->

Besides sampling methods, we apply several standard enhancements commonly used in sampling-based model predictive control. We use warm starting by initializing the proposal mean at iteration $j=0$ with the shifted mean from the previous time step, in which the last control input is duplicated to fill the horizon. To enforce control input bounds, sampled controls are clipped to the admissible range. This can be viewed as modified system dynamics incorporating an additional saturation nonlinearity.

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-B Standard Improvements", "weight": 1.0} -->

We further use a buffer of size $N_{\mathrm{Buffer}}$ that retains the $N_{\mathrm{Buffer}}$ best trajectories (cost-based ranking) from the previous iteration, as, to improve sample efficiency. As with the mean of the proposal, the buffered samples are also warm-started in iteration $j=0$ in the same way as described above.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-B Standard Improvements", "weight": 1.0} -->

Finally, to encourage smooth control trajectories, we use a time-correlated proposal covariance. The time correlation structure is derived from colored noise with power spectral density $\mathrm{PSD}(\omega)\propto\nicefrac{{1}}{{\omega^{\beta}}}$, where $\beta$ controls the noise color and $\omega$ denotes frequency. Within a time step, the controls are assumed to be uncorrelated. During optimization, only marginal variances are updated, while the correlation structure is kept fixed, since estimating full covariance matrices from a few samples is error-prone. Further details are provided.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate the proposed method on two benchmark environments: (i) cart-pole swing-up and (ii) truck backer-upper, using the same system and controller settings as.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

As baseline, we use an model predictive path integral-like method, which also updates proposal mean and covariance from weighted samples but does not enforce a trust region. Instead, it relies on a temperature heuristic and momentum-style smoothing ˜4 to stabilize optimization.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

To isolate the effect of the trust region formulation, both methods use the same algorithmic enhancements from Sec.˜V and the same hyperparameters as. We compare performance in terms of sample efficiency, smoothness of the control inputs, and convergence over iterations. Smoothness is measured using $\sum_{k=1}^{T-1}\|{\underline{u}}_{k}-{\underline{u}}_{k-1}\|^{2}$, where $T$ is the number of time steps in a simulation (see ), and a lower value indicates a smoother control trajectory. Both sample efficiency and convergence are evaluated in terms of cumulative cost, which is the sum of stage costs over $T$ steps.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

We consider four sampling methods: random sampling, low-discrepancy sampling (Sobol and Halton ), and the deterministic localized cumulative distribution-based sampling. To transform the uniform Sobol and Halton samples to an arbitrary Gaussian, we use the inverse transform and eigenvalue decomposition, as described, with no further moment correction. In the plots, heuristic baseline variants are shown with solid lines, and trust region variants are shown with dashed lines labeled with suffix *TR*. Labels indicate the sampling method, where the prefix *ds* denotes deterministic localized cumulative distribution sampling. Furthermore, we compare to the cross-entropy method using localized cumulative distribution-based samples denoted by *dsCEM*.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

Each method and setting is evaluated over $100$ runs, and statistics are reported as median and interquartile range. Results are shown in Figs.˜3, 4 and 2.

<!-- chunk {"id": "body-0036", "role": "body", "section": "VI-A Trust Region Parameter Sweep", "weight": 1.0} -->

The $\epsilon$-sweep result for the proposed trust region method with random, low-discrepancy, and deterministic localized cumulative distribution sampling is shown in Fig.˜2 for $100$ samples, and $5$ optimizer iterations examined for cart-pole swing-up. The lowest cumulative cost is achieved at $\epsilon=2$ for all sampling methods. If $\epsilon$ is larger, the trust region constraint is looser, and allows for more aggressive updates that can lead to worse performance. When $\epsilon$ is smaller, the trust region constraint is tighter, which can lead to more conservative updates requiring more iterations to achieve good performance. However, if large iteration counts are feasible, a smaller $\epsilon$ can achieve better performance.

<!-- chunk {"id": "body-0037", "role": "body", "section": "VI-A Trust Region Parameter Sweep", "weight": 1.0} -->

In our experiments, the entropy lower bound $H_{\min}$ did not have a significant effect on performance, as we only considered maximum iteration counts up to ten, which is not enough for the proposal distribution to collapse. However, in scenarios where more iterations are feasible, $H_{\min}$ can help prevent premature collapse of the proposal distribution and improve performance.

<!-- chunk {"id": "body-0038", "role": "body", "section": "VI-A Trust Region Parameter Sweep", "weight": 1.0} -->

In the following comparisons, the trust region parameters are fixed to $\epsilon=2$ and $H_{\min}=-50$. Since Sobol and Halton samples show very similar trends, we present Sobol only in the following plots for readability.

<!-- chunk {"id": "body-0039", "role": "body", "section": "VI-A Trust Region Parameter Sweep", "weight": 1.0} -->

(a) Cumulative costs over sample size (b) Control input smoothness (c) Cumulative costs over optimizer iterations Figure 3: Results for the cart-pole swing-up environment. All plots share the same legend.

<!-- chunk {"id": "body-0040", "role": "body", "section": "VI-A Trust Region Parameter Sweep", "weight": 1.0} -->

(a) Cumulative costs over sample size (b) Control input smoothness (c) Cumulative costs over optimizer iterations Figure 4: Results for the truck backer-upper environment. All plots share the same legend as in Fig.˜3.

<!-- chunk {"id": "body-0041", "role": "body", "section": "VI-B Sample Efficiency", "weight": 1.0} -->

In the sample-efficiency analysis, the number of optimizer iterations is fixed to three, and sample sizes from $20$ to $300$ are evaluated (see Figs.˜3(a) and 4(a) ‣ Fig. 4 ‣ VI-A Trust Region Parameter Sweep ‣ VI Experiments ‣ Sampling-based Model Predictive Control Using Trust Regions")). In both environments, trust region variants mostly achieve lower cumulative costs than heuristic variants when the sample budget is small (e.g., $N<100$), which indicates improved sample efficiency. Across settings, the trust region method with deterministic localized cumulative distribution sampling consistently outperforms its heuristic counterpart and dsCEM. This advantage is particularly pronounced for the cart-pole swing-up, where the proposed dsTR clearly achieves the best performance in the low-sample regime.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VI-C Control Input Smoothness", "weight": 1.0} -->

The smoothness comparison, shown in Figs.˜3(b) and 4(b) ‣ Fig. 4 ‣ VI-A Trust Region Parameter Sweep ‣ VI Experiments ‣ Sampling-based Model Predictive Control Using Trust Regions"), uses the same sample and iteration settings as in Sec.˜VI-B. In truck backer-upper, trust region variants improve action smoothness over heuristic variants for low sample sizes across all sampling strategies. In cart-pole swing-up, heuristic variants with random and Sobol sampling are smoother than their trust region counterparts for most sample sizes. However, in most settings, dsTR achieves a smoothness slightly lower than dsMPPI and dsCEM and, among all methods, has the best smoothness and lowest cost.

<!-- chunk {"id": "body-0043", "role": "body", "section": "VI-D Convergence", "weight": 1.0} -->

In the convergence analysis, displayed in Figs.˜3(c) and 4(c) ‣ Fig. 4 ‣ VI-A Trust Region Parameter Sweep ‣ VI Experiments ‣ Sampling-based Model Predictive Control Using Trust Regions"), the sample size is fixed to $N=40$, and the maximum number of iterations ($j_{\mathrm{max}}$) is varied over $\{1,3,5,10\}$. Trust region variants show faster convergence than heuristic variants and dsCEM, with lower median cumulative costs and tighter interquartile ranges across iterations. This effect is particularly pronounced for the truck backer-upper: even after ten iterations, heuristic variants do not reach the cost achieved by trust region variants using only three iterations for any sampling strategy. Across both environments, dsTR provides the best convergence behavior, achieving lower costs with fewer iterations than all alternatives.

<!-- chunk {"id": "body-0044", "role": "body", "section": "VI-E Runtime", "weight": 1.0} -->

amean ± standard deviation in ms evaluated over 100 runs TABLE I: Computation times per control step (jmax = 3).

<!-- chunk {"id": "body-0045", "role": "body", "section": "VI-E Runtime", "weight": 1.0} -->

Computation times per control step are reported in Tab.˜I. All runtimes were measured on a single Intel Xeon Platinum 8368 core. As expected, heuristic variants are generally faster than trust region variants because trust region updates require an additional optimization step. Across sampling methods, deterministic variants (dsTR and dsMPPI) are faster than low-discrepancy variants (Halton and Sobol) due to precomputed samples, while random sampling remains the fastest. Further runtime reductions are possible through parallelization.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Discussion", "weight": 1.5} -->

The experiments show that trust region updates improve both sample efficiency and convergence compared to heuristic updates across all considered settings and sampling methods. Although heuristic methods remain competitive in certain settings, the proposed trust region model predictive control is consistently outperforming them, in particular, when computational budgets are limited, i.e., when only a small number of samples and iterations are feasible. Note that reducing the required sample size directly reduces computation time. On parallel hardware, even a difference of a single sample can significantly affect the runtime. E.g., if the hardware can process up to 32 trajectories (samples) in parallel, requiring 33 samples would effectively double the computation time.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Discussion", "weight": 1.5} -->

Regarding sampling methods, low-discrepancy sampling (Halton and Sobol) generally improves upon random sampling, and deterministic localized cumulative distribution sampling yields further improvements, particularly when combined with trust region updates.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Discussion", "weight": 1.5} -->

Notably, trust regions in combination with localized cumulative distribution-based sampling improve both sample and iteration efficiency without sacrificing control smoothness, making it particularly attractive for online model predictive control on resource-constrained hardware.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We proposed a trust region formulation for sampling-based model predictive control that uses principled updates of proposal distribution parameters, eliminating the need for heuristic adaptation, commonly found in state-of-the-art methods such as model predictive path integral. Across the considered experiments, the proposed methods demonstrated improved convergence behavior and sample efficiency compared to heuristic baselines. Additionally, combining trust region updates with deterministic localized cumulative distribution-based sampling yielded the strongest results in the low-sample and low-iteration regimes, further improving performance. These results suggest that the proposed approach is well-suited for real-world applications where reliable convergence and sample efficiency are essential.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Derivation of the Optimal Next Proposal", "weight": 1.0} -->

Using the Kullback--Leibler divergence and entropy, given by the expanded Lagrangian ˜9 reads Taking the functional derivative point-wise w.r.t. $f_{j+1}({\underline{\xi}})$ yields Setting this derivative to zero and solving for $\log f_{j+1}$ gives where $C$ absorbs all additive constants. Exponentiating yields the optimal proposal $f_{j+1}^{\ast}$ ˜10, where the multiplier $\nu$ is implicitly accounted for by $Z_{\eta,\alpha}$ required to satisfy the normalization constraint.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Derivation of the Dual Function", "weight": 1.0} -->

To derive the dual function $g(\eta,\alpha)$, we substitute the optimal proposal $f_{j+1}^{\ast}$ back into the Lagrangian. First, we take the logarithm of the optimal proposal ˜10 multiplied by $(\eta+\alpha)$ to match the coefficient of the entropy term in the Lagrangian Taking the expectation of this term w.r.t. $f_{j+1}^{\ast}$ yields Since $f_{j+1}^{\ast}$ is a valid probability density function, it integrates to $1$. Then, substituting ˜35 back into the simplified Lagrangian reads where the normalization multiplier $\nu$ has been absorbed in $Z_{\eta,\alpha}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Derivation of the Dual Function", "weight": 1.0} -->

Notice that the terms involving the expected cost and the cross-entropy $\eta\int_{\mathds{R}^{d_{{\xi}}}}f_{j+1}^{\ast}({\underline{\xi}})\log f_{j}({\underline{\xi}})\operatorname{d}\!{\underline{\xi}}$ cancel out. The remaining terms yield the dual function ˜12.
