<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Distributionally Robust Optimization with Bias and Variance Reduction

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the distributionally robust optimization (DRO) problem with spectral risk-based uncertainty set and f-divergence penalty. This formulation includes common risk-sensitive learning objectives such as regularized condition value-at-risk (CVaR) and average top-k loss. We present Prospect, a stochastic gradient-based algorithm that only requires tuning a single learning rate hyperparameter, and prove that it enjoys linear convergence for smooth regularized losses. This contrasts with previous algorithms that either require tuning multiple hyperparameters or potentially fail to converge due to biased gradient estimates or inadequate regularization. Empirically, we show that Prospect can converge 2-3x faster than baselines such as stochastic gradient and stochastic saddle-point methods on distribution shift and fairness benchmarks spanning tabular, vision, and language domains.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The ingredients of empirical risk minimization (ERM) are generally considered to be: a model with parameters $w \in \mathbb{R}^d$ (e.g. a neural network), a loss $\ell: \mathbb{R}^d \rightarrow \mathbb{R}^n$ where $\ell_i(w)$ is the error of $w$ on training example $i$, and an optimizer that returns a sequence $(w\pow{t})_{t \geq 1}$ converging to the solution of \min_{w \in \mathbb{R}^d} \frac{1}{n} \sum_{i=1}^n \ell_i(w).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The fourth ingredientoften taken for grantedis the choice of risk functional, which aggregates individual training losses $\ell(w) \in \mathbb{R}^n$ into a univariate summary to be optimized. While[eq:erm] uses the simple average (meant to estimate the expected loss under the training distribution), a deployed model often observes data from different distributions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by this phenomenon, we consider an objective that explicitly captures sensitivity to such distribution shifts: \min_{w \in \mathbb{R}^d} \msc{R}_\mathcal P(\ell(w)) \quad \text{ where } \quad \msc{R}_\mathcal P(l):= \max_{q \in \mathcal P}\br{\sum_{i=1}^n q_i l_i - \nu D(q \Vert \mathbf{1}_n/n)}, in which $\mathcal P \subseteq \Delta^n = \br{\text{probability distributions on $n$ atoms}}$ is an uncertainty set of distributions, $\nu \geq 0$ is a hyperparameter, and $D(q \Vert \mathbf{1}_n/n)$ is a penalty that represents the divergence of $q$ from the original uniform weights $\mathbf{1}_n / n = (1/n, \ldots, 1/n)$ (e.g.the

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The risk value $\msc{R}_\mathcal P(\ell(w))$emulates a game in which nature pays a price of $\nu$ per unit $D(q \Vert \mathbf{1}_n/n)$ to replace the expected loss under the given training distribution $\mathbf{1}_n / n$ with the expected loss under $q$. The distribution $q$ is a reweighting of the training data that is chosen to be maximally unfavorable for the current model performance $\ell(w)$. Accordingly, we refer to $\nu$ as the shift cost.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Objectives of the form [eq:risk-sensitive], known as distributionally robust (DR) optimization problems, have seen a wave of recent interest in machine learning theory and practice. Examples range throughout diverse contexts such as reinforcement [Liu2022Distributionally, kallus2022doubly, Liu2022DistributionallyRobustQ, Xu2023Group, Wang2023AFinite, Lotidis2023Wasserstein, kallus2022doubly, ren2022distributionally, clement2021first], continual [Wang2022Improving], interactive [Yang2023Distributionally, mu2022factored, inatsu2021active, sinha2020formula], Bayesian [Tay2022Efficient, Inatsu2022Bayesian], and federated [deng2020distributionally] learning, along with dimension reduction [vu2022distributionally], computer vision [samuel2021distributional, sapkota2021distributionally], and structured prediction [Li2022Moment, fathony2018distributionally].

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Historically used in quantitative finance, a popular such objective is the conditional value-at-risk (a.k.a.superquantile/expected shortfall/average top-$k$ loss), or CVaR. In terms of methods, the CVaR has been used as a canonical DR objective [Fan2017Learningwith, kawaguchi2020ordered, Rahimian2022Frameworks], as well as in unsupervised [Maurer2021Robust], reinforcement [singh2020improving], and federated learning [pillutla2023federated]. In applications, it has also been employed for robust language modeling [liu2021just] and robotics [Sharma2020Risk]. The CVaR falls into the broader category of spectral risk measures (SRMs), a class of DR objectives that includes the extremile and exponential spectral risk measure (ESRM) [acerbi2002coherence, cotter2006extreme, daouia2019extremiles].

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by 1) the success of the CVaR in numerous applications and 2) the importance of stochastic optimization in ML, the principal goal of this paper is to develop stochasticWe use stochastic interchangeably with incremental, meaning algorithms that make $O$ calls per iteration to a fixed set of oracles $\br{(\ell_i, \nabla \ell_i)}_{i=1}^n$, and not streaming algorithms that sample fresh data at each iteration. optimization algorithms for spectral risk measures.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we propose Prospect\xspace, a stochastic algorithm for optimizing spectral risk measures with only one tunable hyperparameter: a constant learning rate. Theoretically, Prospect\xspaceconverges linearly for any positive shift cost on regularized convex losses. This contrasts with previous stochastic methods that may fail to converge due to bias [Levy2020Large-Scale, kawaguchi2020ordered], may not converge for small shift costs [Mehta2022Stochastic], or require the tuning of multiple hyperparameters [palaniappan2016stochastic]. Experimentally, Prospect\xspacedemonstrates equal or faster convergence than competitors on the training objective on nearly all problems and datasets considered, and exhibits higher stability with respect to external metrics on fairness and distribution shift benchmarks.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Besides spectral risk measures (SRMs), other DR objectives can be recovered by changing the uncertainty set $\mathcal P$. Examples include those based on $f$-divergences [dommel2021Convex, Levy2020Large-Scale, Ben-Tal2013Robust], the Wasserstein metric [blanchet2019Robust, esfahani2018Data, Kuhn2019Wasserstein, bui2022a, abadeh2018wasserstein, nguyen2020distributionally, chen2019selecting, zhu2022distributionally, phan2023global], maximum mean discrepancy [kirschner2020distributionally, staib2019distributionally, nemmour2021approximate], or more generally integral probability metrics [husain2020distributional]. This work focuses on optimizing SRM objectives.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We compare against stochastic algorithms that either are single-hyperparameter out-of-the-box methods such as stochastic gradient descent and stochastic regularized dual averaging [Xiao2009Dual], or multi-hyperparameter methods that converge linearly on strongly convex SRM-based objectives, such as LSVRG [Mehta2022Stochastic] and saddle-point SAGA [palaniappan2016stochastic]. Note that LSVRG may not converge for small shift costs. Other methods may only achieve sublinear convergence rates, even in the strongly convex regime [yu2022fast, ghosh2021efficient, carmon2022distributionally, li2019afirst, shen2022TowardsScalable, Hamedani2023AStochastic].

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Non-convex settings have also been studied [jin2021nonconvex, jiao2022distributed, Sagawa2020Distributionally, luo2020stochastic, ho2023adversarial], as well as statistical aspects [liu2022distributionallyrobust, blanchet2019multivariate, zeng2022generalization, Maurer2021Robust, Lee2020LearningBounds, Khim2020uniformConvergence, zhou2023sample, zhou2021finite, cranko2021generalized, LA2022AWasserstein, Pandey2019EstimationOS]. Our goal is to achieve unconditional linear convergence for smooth, strongly convex (regularized) losses with a single hyperparameter.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Objectives of the form [eq:risk-sensitive] yield connections to other areas in modern machine learning. They are a special case of subpopulation shift, wherein the data-generating distribution and the distribution shift stems from changes in the mixture. In our case, the subpopulations are point masses at the observed data points. In the context of algorithmic fairness, the may represent data conditioned on some protected attribute (e.g.race, gender, age range), and common notations of fairness such as demographic/statistical parity [Agarwal2018AReductions, Agarwal2019FairRegression] impose (informally) that model performance with respect to each should be roughly equal. As such, robustness to reweighting and algorithmic fairness are often aligned notions [williamson2019fairness], with recent research arguing that distributionally robust models are more fair [hashimoto2018fairness, vu2022distributionally] and that fair models are more distributionally robust [mukherjee2022domain].

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

In supervised learning, the data distribution is modeled as $P = P_{X, Y}$ for a feature-label pair $(X, Y)$ and related settings of covariate shift (changes in $P_{X}$ and not $P_{Y|X}$) [sugiyama2007direct] as well as label shift (changes in $P_Y$ and not $P_{X|Y}$) [lipton2018detecting] may also modeled with distributional robustness [zhang2021coping] as illustrated in fig:subpopulations.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Minimizing Spectral Risk with Bias and Variance Reduction", "weight": 1.0} -->

This section describes the key technical challenges in constructing a stochastic optimizer for spectral risk measures and how Prospect\xspacetackles them. In order to build a convergent stochastic algorithm, we will construct an estimate $v_i$ for the gradient of[eq:risk-sensitive] based on a single data index $i$, such that $v_i \rightarrow \nabla \msc{R}_\mathcal P(\ell(w))$ as the iteration counter approaches infinity.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Minimizing Spectral Risk with Bias and Variance Reduction", "weight": 1.0} -->

Precisely, we require that for $i \sim \Unif[n]$, \mathbb{E}\|\nabla \msc{R}_\mathcal P(\ell(w)) - v_i\|_2^2 = \underbrace{\|\nabla \msc{R}_\mathcal P(\ell(w)) - \mathbb{E}[v_i]\|_2^2}_{\text{bias}} + \underbrace{\mathbb{E}\|\mathbb{E}[v_i] - v_i\|_2^2}_{\text{variance}} decreases to zero asymptotically. In the remainder of this section, we first identify concretely our target estimand (i.e.$\nabla \msc{R}_\mathcal P(\ell(w))$ for the spectral risk uncertainty set), construct an estimate, and then describe individual procedures to ensure that the bias and variance terms in[eq:decomposition]vanish.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Minimizing Spectral Risk with Bias and Variance Reduction", "weight": 1.0} -->

Notions of Distribution Shift. Illustration of various forms of distribution shift that are characterized by maintaining the same training data but changing the weight of each example.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Minimizing Spectral Risk with Bias and Variance Reduction", "weight": 1.0} -->

The Gradient of a Spectral Risk Measure. Each SRM is parameterized by a vector $\sigma = (\sigma_1, \ldots, \sigma_n)$ of non-negative weights satisfying $\sigma_1 \leq \cdots \leq \sigma_n$ and $\sum_{i=1}^n \sigma_i = 1$, called the spectrum. The uncertainty set $\mathcal P = \mathcal P(\sigma)$ is the polytope \mathcal P(\sigma) = \operatorname{ConvexHull}\br{ \text{permutations of } (\sigma\_1, \ldots, \sigma\_n) }. See fig:permutahedron, sec:a:objective, for a visualization of $\mathcal P(\sigma)$ for the CVaR [Rockafellar2013Superquantiles,kawaguchi2020ordered, Laguel2022Superquantiles], extremile[daouia2019extremiles], and ESRM[cotter2006extreme].

<!-- chunk {"id": "body-0020", "role": "body", "section": "Minimizing Spectral Risk with Bias and Variance Reduction", "weight": 1.0} -->

The respective formulae for their spectra $\sigma$ and additional background on SRMs are also given in sec:a:objective. Define $\msc{R}_{\sigma}:= \msc{R}_{\mathcal P(\sigma)}$. When $\nu > 0$ and the map $q \mapsto D(q \Vert \mathbf{1}_n/n)$ is strongly convex over $\mathcal P(\sigma)$, we have that (lem:danskin, sec:a:objective) $\msc{R}_\sigma$ is differentiable with gradient given by \nabla \msc{R}_\sigma(l) = \operatorname*{arg\,max}_{q \in \mathcal P(\sigma)} \br{q^\top l - \nu D(q \Vert \mathbf{1}_n/n)} \in \mathbb{R}^n.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Minimizing Spectral Risk with Bias and Variance Reduction", "weight": 1.0} -->

This means the full-batch gradient $w \mapsto \nabla \msc{R}_{\sigma}(\ell(w)) \in \mathbb{R}^d$ can be computed by solving the inner maximization to retrieve $l \mapsto \nabla \msc{R}_\sigma(l) \in \mathbb{R}^n$, calling the oracles to retrieve $w \mapsto \nabla \ell(w) \in \mathbb{R}^{n\times d}$, and multiplying them by the chain rule. To solve for the maximizer, we prove by standard convex duality arguments (prop:isotonic, sec:a:objective) that when $D = D_f$ is an $f$-divergence, the maximum over $q$ can be expressed as a minimization problem that reduces to isotonic regression problem involving $f^*$, the convex conjugate of $f$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Minimizing Spectral Risk with Bias and Variance Reduction", "weight": 1.0} -->

Isotonic regression can be solved exactly by the Pool Adjacent Violators algorithm[best2000minimizing], which runs in $O(n)$ time when the losses are sorted; seesec:a:efficient.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Minimizing Spectral Risk with Bias and Variance Reduction", "weight": 1.0} -->

Bias Reduction via Loss Estimation. We now have a formula for the gradient and proceed to estimation. Denote by $q^l:= \nabla \msc{R}_\sigma(l)$ from[eq:gradient], and observe that by the chain rule, $\nabla \msc{R}_\sigma(\ell(w)) = \sum_{i=1}^n q^{\ell(w)}_i \nabla \ell(w)$. compute the most adversarial distribution $q^{\ell(w)} \in \mathcal P(\sigma)$ for a given set of losses $\ell(w)$, and then take a convex combination of the gradients $\nabla \ell_1(w), \ldots, \nabla \ell_n(w)$ weighted by the probability mass function $q^{\ell(w)}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Minimizing Spectral Risk with Bias and Variance Reduction", "weight": 1.0} -->

While the gradient is computable, however, accessing $\ell(w)$ and $\nabla \ell(w)$ requires $n$ calls to the function/gradient oracles $\{\ell_i, \nabla \ell_i\}_{i=1}^n$, which can be prohibitive. While using a plugin estimate with a mini-batch of size $m < n$ is a natural choice in ERM (making the first term in[eq:decomposition] zero), this will be biased for our objective due to the maximization over $q$. For example, for $m = 1$, we have that $\msc{R}_\sigma(\ell_i(w)) = \ell_i(w) \text{ and } \nabla_w\msc{R}_\sigma(\ell_i(w)) = \nabla_w \ell_i(w)$, which are unbiased estimates of the ERM objective and gradient, respectively (not the SRM objective).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Minimizing Spectral Risk with Bias and Variance Reduction", "weight": 1.0} -->

Prediction Error Reduction. Optimization trajectories on the DR objective. Darker shade indicates lower objective value. Left: Average trajectory of Prospect\xspaceover 20 seeds compared to full-batch gradient descent. Right: Single trajectory of Prospect\xspacewith/without adding a control variate.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Minimizing Spectral Risk with Bias and Variance Reduction", "weight": 1.0} -->

However, note that if the optimal weights $q^{\ell(w)}$ were known, then for $i$ sampled from the uniform distribution on $[n]$, that $nq_i^{\ell(w)} \nabla \ell_i(w)$ is an unbiased estimate for $\sum_{i=1}^n q^{\ell(w)}_i \nabla \ell(w) = \nabla \msc{R}_\sigma(\ell(w))$. While computing $q^{\ell(w)}$ again requires computing $\ell(w)$, the key ingredient of bias reduction in Prospect\xspaceis maintaining a table $l \in \mathbb{R}^n$ of losses such that $l \approx \ell(w)$ for the current iterate $w \in \mathbb{R}^d$, and using $q^l$ as a running estimate of $q^\ell(w)$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Minimizing Spectral Risk with Bias and Variance Reduction", "weight": 1.0} -->

This is justified as when $q \mapsto D(q\Vert \mathbf{1}_n)$ is strongly convex, we have by prop:primobjgradient the map $l \mapsto q^l$ is Lipschitz continuous in $l$ with respect to $\norm{\cdot}_2$. l \approx \ell(w) \implies q^l \approx q^{\ell(w)} \implies \E{i \sim \Unif[n]}{nq^l_i \nabla \ell_i(w)} \approx \nabla \msc{R}_\sigma(\ell(w)).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Minimizing Spectral Risk with Bias and Variance Reduction", "weight": 1.0} -->

We prove in sec:lsaga\_algo that $l - \ell(w) \rightarrow 0$ as the iterate counter goes to infinity for our particular choice of $l$, yielding an asymptotically unbiased gradient estimate as illustrated in fig:gametheory(left).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Minimizing Spectral Risk with Bias and Variance Reduction", "weight": 1.0} -->

Variance Reduction via Control Variates. The final ingredient of our stochastic gradient estimate is a variance reduction scheme. Given any estimator $\hat{\theta}$ of $\theta \in \mathbb{R}^d$, a control variate is another estimator $\hat{\psi}$ over the same probability space with a known expectation $\mathbb{E}[\hat{\psi}] = \psi \in \mathbb{R}^d$, such that $\mathbb{E}[(\hat{\theta} - \theta)^\top(\hat{\psi} - \psi)] > 0$. We can exploit this positive correlation to construct an estimator with strictly smaller variance that $\hat{\theta}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Minimizing Spectral Risk with Bias and Variance Reduction", "weight": 1.0} -->

In the unrealistic case in which $\hat{\psi} = \hat{\theta}$, the optimal multiplier is $\alpha = 1$, trivially achieving zero variance. Similar to $l$, we prove in sec:lsaga\_algo that $g - \nabla \ell(w) \rightarrow 0$ and $\rho - q^{\ell(w)} \rightarrow 0$, so we have in the notation of[eq:control] that $\hat{\psi} - \hat{\theta} \rightarrow 0$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Minimizing Spectral Risk with Bias and Variance Reduction", "weight": 1.0} -->

Thus, by using $\alpha = 1$, our final stochastic gradient estimate is $$\begin{align}\textstyle \hat{\theta} - \alpha(\hat{\psi} - \psi) = nq^l_i \nabla \ell_i(w) - n\rho_i g_i + \textstyle\sum_{j=1}^n \rho_j g_j, which has asymptotically vanishing variance without decreasing the learning rate, as illustrated in fig:gametheory (right). This variance reduction scheme generalizes (and is inspired by) the one employed in the SAGA optimizer [defazio2014saga] for ERM, in which $\rho$ is set to $\mathbf{1}_n/n$. Finally, while ignored in this section for ease of presentation, each $g_i$ will actually approximate the gradients of the regularized losses $\ell_i + \mu \norm{\cdot}_2^2$ for $\mu > 0$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

By combining the bias reduction and variance reduction schemes from the previous section, we build an algorithm that achieves overall prediction error reduction. Thus, we now present the Prediction Error-Reduced Optimizer for Spectral Risk Measures (Prospect\xspace) algorithm to solve \min_{w \in \mathbb{R}^d} \sbr{F_\sigma(w):= \msc{R}_\sigma(\ell(w)) + \frac{\mu}{2}\norm{w}_2^2}, where $\mu > 0$ is a regularization constant. The full algorithm is given in algo:lsaga. We offer in this section an intuitive explanation of the algorithm, discussion of computational complexity, theoretical convergence guarantees, and extensions to non-smooth settings.

<!-- chunk {"id": "body-0033", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

Instantiating Bias and Variance Reduction. Consider a current iterate $w \in \mathbb{R}^d$. As mentioned in sec:problem, bias and variance reduction relies on the three approximations: the losses $l$ for $\ell(w) \in \mathbb{R}^n$, each gradient $g_i$ for $\nabla \ell_i(w) + \mu w \in \mathbb{R}^{d}$, and the weights $\rho$ for $q^{\ell(w)} \in \mathcal P$. Given initial point $w_0 \in \mathbb{R}^d$, we initialize $l = \ell(w_0)$, $g = \nabla \ell(w_0)$, and $\rho = q^{\ell(w_0)}$ (including $\bar{g}:= g^\top \rho$).

<!-- chunk {"id": "body-0034", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

At each iterate, we sample indices $i, j \sim \Unif[n]$ independently. The index $i$ is used to compute the stochastic gradient estimate[eqg:grad\_estimate], yielding the update direction $v$ in alg:lsaga:update at the cost of a call to a $(\ell_i, \nabla \ell_i)$ oracle. Then, $l$ is updated by replacing $l_j$ with $\ell_j(w)$ costing another call to $(\ell_j, \nabla \ell_j)$, and we reset $q$ (the variable that stores $q^l$). Next, we use $i$ again to make the replacements of $g_i$ with $\nabla \ell_i(w) + \mu w$ and $\rho_i$ with $q_i = q_i^l$. In summary, each approximation is updated every iteration by changing one component based on the current iterate $w$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

The indices $i, j$ are decoupled for theoretical convenience, but in practice using only $i$ works similarly, which we use in sec:experiments.

<!-- chunk {"id": "body-0036", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

The weight update in alg:lsaga:dual is solved exactly by (i) sorting the vector of losses in $O(n \log n)$, (ii) plugging the sorted loss table $l$ into the Pool Adjacent Violators (PAV) algorithm running in $O(n)$ time, as mentioned in sec:problem. Because only one element of $l$ changes every iterate, we may simply bubble sort $l$ starting from the index that was changed. While in the worst case, this cost is $O(n)$, it is exactly $O(s)$ where $s$ is the number of swaps needed to resort $l$. We find in experiments that the sorted order of $l$ stabilizes quickly. The storage of the gradient table $g$ requires $O(nd)$ space in general, but it can be reduced to $O(n)$ for generalized linear models and nonlinear additive models.

<!-- chunk {"id": "body-0037", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

For losses of the form $\ell_i(w) = h(x_i^\top w, y_i)$, for a differentiable loss $h$ and scalar output $y_i$, we have $\nabla \ell_i(w) = x_i \, h'(x_i^{\top} w, y_i)$. We only need to store the scalar $h'(x_i^{\top} w, y_i)$, so Prospect\xspacerequires $O(n + d)$ memory. In terms of computational complexity, Lines[alg:lsaga:param] and[alg:lsaga:cv] require $O(d)$ operations and Line[alg:lsaga:dual] requires at most $O(n)$ operations, so that in total the iteration complexity is $O(n+d)$. In comparison, a full batch gradient descent requires $O(nd)$ operations so Prospect\xspacedecouples efficiently the cost of computing the losses, gradients, and weights.

<!-- chunk {"id": "body-0038", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

We assume throughout that each $\ell_i$ is convex, $G$-Lipschitz, and $L$-smooth. We also assume that the $D = D_f$ is an $f$-divergence with the generator $f$ being $\alpha_n$-strongly convex on the interval $[0, n]$ (e.g.$\alpha_n = 2n$ for the $\chi^2$-divergence and $\alpha_n = 1$for the KL-divergence).

<!-- chunk {"id": "body-0039", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

The convergence guarantees depend on the condition numbers $\kappa = 1 + L / \mu$ of the individual regularized losses, as well as a measure $\kappa_\sigma = n\sigma_n$ of the skewness of the spectrum. Note that both $\kappa$ and $\kappa_\sigma$ are necessarily larger than or equal to one. Define $w^\star:= \operatorname*{arg\,min}_{w} F_\sigma(w)$, which exists and is unique due to the strong convexity of $F_\sigma$. The proof is given in sec:a:main\_result.

<!-- chunk {"id": "body-0040", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

Prospect\xspacewith a small enough step size is guaranteed to converge linearly for all $\nu > 0$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

If, in addition, the shift cost is $\nu \ge \Omega(G^2 / \mu \alpha_n)$, then the sequence of iterates $(w\pow{t})_{t\geq 1}$ generated by Prospect\xspaceand learning rate $\eta = (12 \mu (1+\kappa) \kappa_\sigma)^{-1} $ converges linearly at a rate $\tau = 2\max\left\{n, 24 \kappa_\sigma(\kappa + 1)\right\}$, i.e., $$\mathbb{E}\|w\pow{t} - w^\star\|_2^2 \le (1 + \sigma_n^{-1} + \sigma_n^{-2}) \exp(-t/\tau) \|w\pow{0} - w^\star\|_2^2 \,.$$ The number of iterations $t$ required by Prospect\xspaceto achieve $\mathbb{E}\|w\pow{t} -

<!-- chunk {"id": "body-0042", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

w^\star\|_2^2 \le \varepsilon$ (provided that $\nu$ is large enough) is $t = O((n + \kappa \kappa_\sigma) \ln(1/\epsilon))$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

This exactly matches the rate of the LSVRG\xspace[Mehta2022Stochastic], the only primal stochastic optimizer that converges linearly for spectral risk measures. However, unlike LSVRG\xspace, Prospect\xspaceis guaranteed to converge linearly for any shift cost and has a single hyperparameter, the stepsize $\eta$. Similarly, compared to primal-dual stochastic saddle-point methods, our algorithm requires only one learning rate, streamlining its implementation.

<!-- chunk {"id": "body-0044", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

Prospectfor Non-Smooth Objectives. We may wonder about the convergence behavior of Prospect\xspacewhen either the shift cost $\nu = 0$, or the underlying losses $\ell_i$ are non-smooth. While the smoothness of the objective is then lost, Prospect\xspacestill converges to the minimizer $w_0^\star$ as we prove below. The first setting is relevant as historically, SRMs such as the conditional value-at-risk have been employed as coherent risk measures for loss distributions [acerbi2002coherence] in the form of an $L$-estimator $\sum_{i=1}^n \sigma_i l_{(i)}$ (as seen in sec:problem). If these losses are separated at the optimum, however, we may achieve linear convergence with Prospect\xspaceeven with $\nu = 0$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

This behavior can be explained as hidden smoothness in the objective [eq:lsaga\_obj]; the objective is indeed differentiable at points satisfying $\ell_{}(w) < \cdots < \ell_{(n)}(w)$, where $\ell_{(i)}(w)$ denotes the $i$-th smallest loss at $w$. Assume convex losses $\ell_1, \ldots, \ell_n$ and $\mu > 0$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

Let $w^\star_\nu$ be the unique minimizer of [eq:lsaga\_obj] with shift cost $\nu \geq 0$. Assume that the values $\ell_1(w^\star_0), \ldots, \ell_n(w^\star_0)$ are all distinct. Then, there exists a constant $\nu_0 > 0$ such that $w^\star_0 = w^\star_\nu$ exactly for all $\nu \leq \nu_0$. Thus, running Prospect\xspacewith $\nu \in (0, \nu_0]$ converges to the minimizer $w_0^\star$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

In particular, $\nu_0$ is chosen so that $\nu_0 \p{\sigma_{i+1} - \sigma_i} < \ell_{(i+1)}(w^\star_0) - \ell_{(i)}(w^\star_0)$ for each $i$, or as the multiplicative factor that relates gaps in the spectrum to the gaps in the loss at optimality (see sec:a:objective).

<!-- chunk {"id": "body-0048", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

For the setting in which any $\ell_i$ may be non-smooth, we generalize Prospect\xspaceby applying it to the Moreau envelope of each loss $\ell_i$ and their gradients[bauschke2011convex, rockafellar1976monotone], allowing for accelerated performance and non-smooth losses (such as those containing an $\ell_1$ penalty). Specifically, we consider oracles $\nabla \operatorname{env}(\ell_i)(w)$ where $\operatorname{env}(\ell_i) = \inf_{v \in \mathbb{R}^d} \ell_i(v) + \|w-v\|_2^2$; the updates can be expressed in terms of the proximal operators of the losses[bauschke2011convex]. Such an approach has been considered for ERM by [defazio2016simple] to accelerate the SAGA algorithm.

<!-- chunk {"id": "body-0049", "role": "body", "section": "The Prospect\\xspaceAlgorithm", "weight": 1.0} -->

The oracles can be accessed either in closed form or by efficient subroutines in common machine learning settings[defazio2016simple,frerix2018proximal,roulet2022differentiable], we can adapt algo:lsaga to leverage such oracles. The resulting algorithm enjoys a linear convergence guarantee similar to thm:lsaga:main with a more liberal condition on the shift cost $\nu$ while providing competitive performance in practice. We refer to sec:a:prox\_sagafor details.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Experiments", "weight": 1.0} -->

We compare Prospect\xspaceagainst competitors in a variety of learning tasks. While we focus attention on its performance as an optimizer with respect to its training objective, we also highlight metrics of interest on the test set in fairness and distribution shift benchmarks. The code containing the algorithm implementation and data preparation is made publicly available online: Setting, Baselines, Evaluation. We consider supervised learning tasks where data points $z_i = (x_i, y_i)$ are input-label pairs. Losses are of the form $\ell_i(w):= h(y_i, w^\top \phi(x_i))$, with $\phi$ a fixed feature embedding, and $h$ measuring prediction error. The spectrums considered are: We compare against four baselines: minibatch stochastic gradient descent (SGD), stochastic regularized dual averaging (SRDA) [Xiao2009Dual], Saddle-SAGA [palaniappan2016stochastic], and LSVRG [Mehta2022Stochastic].

<!-- chunk {"id": "body-0051", "role": "body", "section": "Experiments", "weight": 1.0} -->

For SGD/SRDA, we use a batch size of 64 and for LSVRG we use an epoch length of $n$. For Saddle-SAGA, we show that allowing different primal and dual learning rates provides theoretically and experimentally improvement (sec:a:saddle\_saga) and use this improved heuristic (setting the dual stepsize $10n$ times smaller than the primal one).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Experiments", "weight": 1.0} -->

\operatorname{Suboptimality}(w) = (F_\sigma(w) - F_\sigma(w^\star)) \, /\, (F_\sigma(w\pow{0}) - F_\sigma(w^\star)) \where $w^\star$ is approximated by running LBFGS[nocedal1999numerical] on the objective until convergence. The $x$-axis displays the number of calls to any first-order oracle $w \mapsto (\ell_i(w), \nabla \ell_i(w))$ divided by $n$, i.e. the number of passes through the training set. We fix the shift cost $\nu = 1$ and regularization parameter $\mu = 1/n$. Further details of the setup such as hyperparameter tuning, and additional results are given in sec:a:experiments,sec:a:additionalrespectively.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Tabular Least-Squares Regression", "weight": 1.0} -->

Regression benchmarks. The $y$-axis measures the suboptimality as given by eqn:subopt, while the $x$-axis measures the number of calls to the function value/gradient oracle divided by $n$. Rows indicate different spectral risk objectives and columns indicate datasets.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Tabular Least-Squares Regression", "weight": 1.0} -->

We consider five regression benchmarks under square loss. The datasets are The training curves are shown in fig:uci.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Tabular Least-Squares Regression", "weight": 1.0} -->

Across datasets and objectives, we find that Prospect\xspaceexhibits linear convergence at a rate no worse than SaddleSAGA\xspaceand LSVRG\xspacebut often much better. For example, Prospect\xspaceconverges to precision $10^{-8}$ for the CVaR on concrete and the extremile on power within half the number of passes that LSVRG takes for the same suboptimality. Similarly, for the ESRM on yacht, SaddleSAGA\xspacerequires 64 epochs to reach the same precision as Prospect\xspaceat 40 epochs. The direct stochastic methods, SGD/SRDA, are biased and fail to converge for any learning rate.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Fair Classification and Regression", "weight": 1.0} -->

we explore the relationship between robust learning and group fairness on 2 common tabular benchmarks. Diabetes 130-Hospitals (diabetes) is a binary classification task of predicting readmission for diabetes patients based on 10 years worth of clinical data from 130 US hospitals [Rizvi2014Impact]. Adult Census (acsincome) is a regression task of predicting income of US adults given features compiled from the American Community Survey [Ding2021Retiring].

<!-- chunk {"id": "body-0057", "role": "body", "section": "Fair Classification and Regression", "weight": 1.0} -->

We evaluate fairness with the statistical parity score, which compares predictive distributions of a model given different values of a particular protected attribute [Agarwal2018AReductions, Agarwal2019FairRegression]. Letting $Z = (X, Y, A)$ denote a random (input, label, metadata attribute) triplet, a model $g$ is said to satisfy statistical parity (SP) if the conditional distribution of $g(X)$ over predictions given $A = a$ is equal for any value $a$. Intuitively, statistical parity scores measure the maximum deviation between these distributions for any over $a$, so values close to zero indicate SP-fairness. In diabetes, we use gender as the protected attribute $A$, whereas in acsincome we use race as the protected attribute. Note that the protected attributes are not supplied to the models. The results are given in fig:fairness.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Fair Classification and Regression", "weight": 1.0} -->

Firstly, we note that Prospect\xspaceconverges rapidly on both datasets while LSVRG fails to converge on diabetes and SaddleSAGA\xspacefails to converge on acsincome. Secondly, LSVRG does not stabilize with respect to classification SP, showing a mean/std SP score of $1.38 \pm 0.25\%$ within the final ten passes on the diabetes CVaR, whereas Prospect\xspacegives $0.82 \pm 0.00\%$, i.e., a $40\%$ relative improvement with greater stability. While SaddleSAGA\xspacedoes stabilize in SP on diabetes, it fails to qualitatively decrease at all on the acsincome. Interestingly, while suboptimality and SP-fairness are correlated for Prospect\xspace, SGD (reaching only $10^{-1}$ suboptimality with respect to the CVaR objectives on acsincome) achieves a lower fairness score. Again, across both suboptimality and fairness, Prospect\xspaceis either the best or close to the best.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Fair Classification and Regression", "weight": 1.0} -->

Fairness benchmarks. Top: Training curves on the CVaR and extremile for diabetes (left) and CVaR and extremile for acsincome (right). Bottom: Statistical parity scores for the two classification objectives on diabetes and regression objectives on acsincome. Values closer to zero indicate better SP-fairness.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Image and Text Classification under Distribution Shift", "weight": 1.0} -->

We consider two tasks from the WILDS distribution shift benchmark The Amazon Reviews (amazon) task [ni2019justifying] consists of classifying text reviews of products to a rating of 1-5, with disjoint train and test reviewers. The iWildCam (iwildcam) image classification challenge [beery2020iwildcam] contains labeled images of animals, flora, and backgrounds from cameras placed in wilderness sites. Shifts are due to changes in camera angles, locations, lighting... $n=10000$ and $n=20000$ examples respectively. For both datasets, we train a linear probe classifier, i.e., a linear model over a frozen deep For amazon, we use a pretrained BERT model[Devlin2019BERTPO] fine-tuned on a held-out subset of the Amazon Reviews training set for 2 epochs. For iwildcam, we use a pretrained on ImageNet (without fine-tuning).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Image and Text Classification under Distribution Shift", "weight": 1.0} -->

Apart from the training suboptimality, we evaluate the spectral risk objectives on their robustness to subpopulation shifts. We define each subpopulation group based on the true label. For amazon, we use the worst group misclassification error on the test set For iwildcam, we use the median group errorowing to its larger number of classes.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Image and Text Classification under Distribution Shift", "weight": 1.0} -->

For both amazon and iwildcam, Prospect\xspaceand SaddleSAGA\xspace(with our heuristic) outperform LSVRG\xspacein training suboptimality. We hypothesize that this phenomenon is due to checkpoints of LSVRG\xspacegetting stale over the $n$-length epochs for these datasets with large $n$ (leading to a slow reduction of bias). In contrast, Prospect\xspaceand SaddleSAGA\xspaceavoid this issue by dynamically updating the running estimates of the importance weights. For the worst group error for amazon, Prospect\xspaceand SaddleSAGA\xspaceoutperform LSVRG\xspace. Prospect\xspacehas a mean/std worst group error of $77.38 {\pm} 0.00 \%$ over the last ten passes on the extremile, whereas SaddleSAGA\xspacehas a slightly worse $77.53 {\pm} 1.57 \%$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Image and Text Classification under Distribution Shift", "weight": 1.0} -->

Interestingly, on iwildcam, LSVRG\xspaceand Prospect\xspacegive stronger generalization performance, nearly $1$pp better, than SaddleSAGA\xspacein terms of median group misclassification rate. In summary, across tasks and objectives, Prospect\xspacedemonstrates best or close to best performance.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Image and Text Classification under Distribution Shift", "weight": 1.0} -->

Distribution shift results. Top row: Training curves and worst group misclassification error on amazon test. Bottom row: Training curves and median group misclassification error on the iwildcam test set. Smaller values indicate better performance for all metrics.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this paper, we introduced Prospect\xspace, a distributionally robust optimization algorithm for minimizing spectral risk measures with a linear convergence guarantee. Prospect demonstrates rapid linear convergence on benchmark examples and has the practical benefits of converging for any shift cost while only having a single hyperparameter. Promising avenues for future work include extensions to the non-convex setting by considering the regular subdifferential, variations using other uncertainty sets, and further exploring connections to algorithmic fairness.
