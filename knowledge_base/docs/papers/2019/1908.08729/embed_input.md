<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Wasserstein Distributionally Robust Optimization: Theory and Applications in Machine Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Many decision problems in science, engineering and economics are affected by uncertain parameters whose distribution is only indirectly observable through samples. The goal of data-driven decision-making is to learn a decision from finitely many training samples that will perform well on unseen test samples. This learning task is difficult even if all training and test samples are drawn from the same distribution - especially if the dimension of the uncertainty is large relative to the training sample size. Wasserstein distributionally robust optimization seeks data-driven decisions that perform well under the most adverse distribution within a certain Wasserstein distance from a nominal distribution constructed from the training samples. In this tutorial we will argue that this approach has many conceptual and computational benefits. Most prominently, the optimal decisions can often be computed by solving tractable convex optimization problems, and they enjoy rigorous out-of-sample and asymptotic consistency guarantees. We will also show that Wasserstein distributionally robust optimization has interesting ramifications for statistical learning and motivates new approaches for fundamental learning tasks such as classification, regression, maximum likelihood estimation or minimum mean square error estimation, among others.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider a decision problem under uncertainty, where each admissible decision results in an uncertain loss that is modeled by a measurable extended real-valued loss function $\ell{(\xi)}$. We assume that the random vector $\xi \in {\mathbb{R}}^{m}$ captures all decision-relevant risk factors and is governed by a probability distribution $\mathbb{P}$. The feasible set of all available loss functions is denoted by $\mathcal{L}$. The risk of a decision $\ell \in \mathcal{L}$ is defined as the expected loss under $\mathbb{P}$, that is,

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

and the optimal risk is defined as the risk of the least risky admissible loss function, that is,

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To ensure that the expectations in and are defined for all measurable loss functions, we set ${{\mathbb{E}}^{\mathbb{P}}{\lbrack{\ell{(\xi)}}\rbrack}} = \infty$ whenever the expectations of the positive and negative parts of $\ell{(\xi)}$ are both infinite. This convention means that infeasibility trumps unboundedness.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In most real decision-making situations, the distribution $\mathbb{P}$ is fundamentally unknown. However, $\mathbb{P}$ may be indirectly observable through training samples ${\hat{\xi}}_{i}$, $i \in {\{ 1,\ldots,N\}}$, drawn independently from $\mathbb{P}$. In addition, some structural properties of $\mathbb{P}$ may be known. For example, if $\xi$ represents a vector of uncertain prices, then $\mathbb{P}$ must be supported on the nonnegative orthant ${\mathbb{R}}_{+}^{m}$. Alternatively, $\mathbb{P}$ may be known to display certain symmetry or unimodality properties, or it may even be known to belong to some parametric distribution family.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

If the distribution $\mathbb{P}$ is unknown, we lack an important input parameter for the risk evaluation problem and the decision problem. In this case, the unknown true distribution $\mathbb{P}$ could be replaced with a nominal distribution ${\hat{\mathbb{P}}}_{N}$ estimated from the $N$ training samples. Note that unlike $\mathbb{P}$, the nominal distribution ${\hat{\mathbb{P}}}_{N}$ is accessible as it is constructed from observable quantities. Therefore, the nominal risk evaluation and decision problems (that is, problems and with ${\hat{\mathbb{P}}}_{N}$ instead of $\mathbb{P}$) are at least in principle solvable. The following example showcases common methods for constructing the nominal distribution ${\hat{\mathbb{P}}}_{N}$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Example 1.1 (Nominal distribution)", "weight": 1.0} -->

In the remainder we will primarily work with the following non-parametric and parametric models for the nominal distribution.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Example 1.1 (Nominal distribution)", "weight": 1.0} -->

In the absence of any structural information, it is convenient to set ${\hat{\mathbb{P}}}_{N}$ to the discrete empirical distribution, that is, the uniform distribution on the $N$ training samples,

<!-- chunk {"id": "body-0010", "role": "body", "section": "Example 1.1 (Nominal distribution)", "weight": 1.0} -->

In the presence of structural information, it is often convenient to set ${\hat{\mathbb{P}}}_{N}$ to an elliptical distribution with a structure-dependent density generator $g$, that is,

<!-- chunk {"id": "body-0011", "role": "body", "section": "Example 1.1 (Nominal distribution)", "weight": 1.0} -->

where only the mean vector $\hat{\mu}$ and the covariance matrix $\hat{\Sigma}$ depend on the training samples and are constructed via maximum likelihood estimation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Example 1.1 (Nominal distribution)", "weight": 1.0} -->

As a function of the training data, the nominal distribution ${\hat{\mathbb{P}}}_{N}$ constitutes itself a random object, which is governed by the distribution ${\mathbb{P}}^{N}$ of the $N$ independent training samples. $\square$

<!-- chunk {"id": "body-0013", "role": "body", "section": "Example 1.1 (Nominal distribution)", "weight": 1.0} -->

Even if the most sophisticated statistical tools are deployed, the nominal distribution ${\hat{\mathbb{P}}}_{N}$ will invariably differ from the unknown true distribution $\mathbb{P}$ that generated the training samples. Moreover, if ${\hat{\mathbb{P}}}_{N}$ is used instead of $\mathbb{P}$, the solutions of the risk evaluation problem and the decision problem are likely to inherit any estimation errors in ${\hat{\mathbb{P}}}_{N}$. In the context of financial portfolio theory it has even been observed that estimation errors in the input parameters of an optimization problem are often amplified by the optimization. To make things worse, one can generally show that even if the distributional input parameters of a decision problem are unbiased, the optimization results tend to be optimistically biased. Thus, implementing the optimal decisions leads to disappointment in out-of-sample tests. In decision analysis this phenomenon is sometimes termed the optimizer's curse, and in stochastic optimization it is referred to as the optimization bias.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Example 1.2 (Optimizer's curse)", "weight": 1.0} -->

where the second equality holds because the inner expectation is linear in ${\hat{\mathbb{P}}}_{N}$. This implies that $\mathcal{R}{({\hat{\mathbb{P}}}_{N},\ell)}$ constitutes an unbiased estimator for the true risk $\mathcal{R}{({\mathbb{P}},\ell)}$. Moreover, we have

<!-- chunk {"id": "body-0015", "role": "body", "section": "Example 1.2 (Optimizer's curse)", "weight": 1.0} -->

The above observations can be interpreted as follows. Someone solving the nominal decision problem thinks that the risk of $\ell^{\star}$ amounts to ${\mathcal{R}{({\hat{\mathbb{P}}}_{N},\ell^{\star})}} = {\mathcal{R}{({\hat{\mathbb{P}}}_{N},\mathcal{L})}}$ (the in-sample risk), which is typically smaller than the optimal risk $\mathcal{R}{({\mathbb{P}},\mathcal{L})}$ attainable under full knowledge of $\mathbb{P}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Example 1.2 (Optimizer's curse)", "weight": 1.0} -->

However, the actual risk $\mathcal{R}{({\mathbb{P}},\ell^{\star})}$ of the optimizer $\ell^{\star}$ under the true distribution (the out-of-sample risk) is always larger than $\mathcal{R}{({\mathbb{P}},\mathcal{L})}$. The difference between the out-of-sample risk and the in-sample risk is termed the post-decision disappointment. The optimizer's curse refers to the observation that the post-decision disappointment is positive on average. $\square$

<!-- chunk {"id": "body-0017", "role": "body", "section": "Example 1.2 (Optimizer's curse)", "weight": 1.0} -->

In order to quantify the sensitivity of $\mathcal{R}{({\mathbb{P}},\ell)}$ and $\mathcal{R}{({\mathbb{P}},\mathcal{L})}$ with respect to the unknown true distribution $\mathbb{P}$, we must introduce a distance measure between probability distributions. As we will argue below, the Wasserstein distance is a particularly convenient choice.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

Depending on the available structural information on $\mathbb{P}$, the nominal distributions portrayed in Example 1.1 ‣ 1 Introduction"), which will be used throughout this tutorial, are essentially optimal within certain estimator families.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

Thus, the type-1 Wasserstein distance between $\mathbb{P}$ and its closest $N$-point distribution cannot decay faster than $N^{- {1/m}}$. Maybe surprisingly, the empirical distribution ${\hat{\mathbb{P}}}_{N} = {\frac{1}{N}{\sum_{i = 1}^{N}\delta_{{\hat{\xi}}_{i}}}}$ attains this optimal decay rate in a probabilistic sense even though it is constructed from $N$ random samples but without knowledge of $\mathbb{P}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

Indeed, \[, Theorem 2\] implies that for every $\eta \in {}$ there exist $\overline{N} \in {\mathbb{N}}$ and $\overline{c} > 0$ such that ${W_{1}{({\hat{\mathbb{P}}}_{N},{\mathbb{P}})}} \leq {\overline{c}N^{- {1/m}}}$ with confidence $1 - \eta$ for every $N \geq \overline{N}$. Thus, if we aim to approximate $\mathbb{P}$ with a sequence of discrete distributions, the empirical distribution ${\hat{\mathbb{P}}}_{N}$ is essentially optimal in the sense that it attains the best possible convergence rate at any desired confidence level.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

Elliptical distributions: Assume that $\mathbb{P}$ is known to be an elliptical distribution with a known density generator $g$ but unknown mean vector $\mu$ and covariance matrix $\Sigma$. In this case, the problem of finding an estimator ${\hat{\mathbb{P}}}_{N}$ for the distribution $\mathbb{P}$ reduces to finding an estimator ${\hat{\theta}}_{N}$ for the vector $\theta = {(\mu,\Sigma)}$ of unknown distribution parameters. Under mild regularity conditions, the Cramér-Rao inequality guarantees that the covariance matrix of $\sqrt{N} \cdot {\hat{\theta}}_{N}$ exceeds the inverse Fisher information matrix in a positive semidefinite sense for any unbiased estimator ${\hat{\theta}}_{N}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

As the maximum likelihood estimator ${\hat{\theta}}_{N}^{ML}$ is asymptotically unbiased and efficient, i.e., the mean of ${\hat{\theta}}_{N}^{ML}$ converges to $\theta$ and the variance of $\sqrt{N} \cdot {\hat{\theta}}_{N}^{ML}$ converges to the inverse Fisher information matrix as $N$ grows, it is asymptotically optimal among all conceivable unbiased estimators.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

We emphasize that, by mobilising more powerful results from statistics, the above optimality guarantees could be extended to even larger families of estimators. $\square$

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

Example 1.6 ‣ 1 Introduction") suggests that the accuracy of the nominal distribution cannot be increased beyond some fundamental limit by tuning the estimator. The only remaining option to reduce the estimation error is to increase the sample size $N$, which may be expensive or impossible. Indeed, additional training samples may only become available in the future. Thus, the optimizer's curse illustrated in Example 1.2 ‣ 1 Introduction") is fundamental and cannot be eliminated. However, once the potential to improve the estimator ${\hat{\mathbb{P}}}_{N}$ is exhausted, it may still be possible to mitigate the optimizer's curse by altering the risk evaluation and decision problems and directly. Specifically, we propose here to robustify these problems against the uncertainty about the true distribution $\mathbb{P}$. Distributional uncertainty is often referred to as ambiguity or Knightian uncertainty and is conveniently captured by an ambiguity set, that is, an uncertainty set in the space of probability distributions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

To formalize this idea, we let $\Xi \subseteq {\mathbb{R}}^{m}$ be a closed set that is known to contain the support of $\mathbb{P}$. In the absence of any structural information, we may simply set $\Xi = {\mathbb{R}}^{m}$. Moreover, we denote by $\mathcal{P}{(\Xi)}$ the family of all probability distributions supported on $\Xi$, and we define the ambiguity set

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

as the ball of radius $\varepsilon \geq 0$ in $\mathcal{P}{(\Xi)}$ centered at the nominal distribution ${\hat{\mathbb{P}}}_{N}$ with respect to the type-$p$ Wasserstein distance. By construction, this ambiguity set contains all distributions supported on $\Xi$ that can be obtained by reshaping the nominal distribution ${\hat{\mathbb{P}}}_{N}$ at a transportation cost of at most $\varepsilon$. We can think of ${\mathbb{B}}_{\varepsilon,p}{({\hat{\mathbb{P}}}_{N})}$ as the set of all distributions for which the estimation error---as measured by the type-$p$ Wasserstein distance---is at most $\varepsilon$, and we can interpret $\varepsilon$ as the maximum estimation error against which we seek protection.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

Using the proposed ambiguity set, we define the worst-case risk as

<!-- chunk {"id": "body-0028", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

and the worst-case optimal risk as

<!-- chunk {"id": "body-0029", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

Problem constitutes a distributionally robust optimization problem. It seeks decisions that have minimum risk under the most adverse distributions in the ambiguity set. Intuitively, problem can thus be viewed as a zero-sum game, where the decision-maker first selects an admissible loss function with the goal to minimize the risk, in response to which some fictitious adversary or 'nature' selects a distribution from within the ambiguity set with the goal to maximize the risk. The hope is that by minimizing the worst-case risk, we actually push down the risk under all distributions in the ambiguity set---in particular under the unknown true distribution $\mathbb{P}$, which is contained in the ambiguity set if $\varepsilon$ is large enough. Thus, there is reason to hope that the solutions of distributionally robust optimization problems with carefully calibrated ambiguity sets display low out-of-sample risk.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

The distributionally robust risk evaluation and decision problems and are attractive for a multitude of diverse reasons.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

Fidelity: Distributionally robust models are more 'honest' than their nominal counterparts as they acknowledge the presence of distributional uncertainty. They also benefit from information about the type and magnitude of the estimation errors, which is conveniently encoded in the geometry and size of the ambiguity set.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

Managing expectations: Due to the optimizer's curse, the solutions of nominal decision problems equipped with noisy estimators display an optimistic in-sample risk, which cannot be realized out of sample; see Example 1.2 ‣ 1 Introduction"). In contrast, the solutions of distributionally robust decision problems are guaranteed to display an out-of-sample risk that falls below the worst-case optimal risk whenever the ambiguity set contains the unknown true distribution. Thus, nominal decision problems over-promise and under-deliver, while distributionally robust decision problems under-promise and over-deliver.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

Computational tractability: The distributionally robust problems and can often be reformulated as (or tightly approximated by) finite convex programs that are solvable in polynomial time. Section will showcase some key tractability results.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

Performance guarantees: For judiciously calibrated ambiguity sets, one can prove that the worst-case optimal risk for any fixed sample size $N$ provides an upper confidence bound on the out-of-sample risk attained by the optimizers of (finite sample guarantee) and that the optimizers of converge almost surely to an optimizer of as $N$ tends to infinity (asymptotic guarantee); see Section.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

Regularization by robustification: The optimizer's curse is reminiscent of overfitting phenomena that plague most statistical learning models. One can show that distributionally robust learning models equipped with a Wasserstein ambiguity set are often equivalent to regularized learning models that minimize the sum of a nominal objective and a norm term that penalizes hypothesis complexity. Similarly, one can show that some distributionally robust maximum likelihood estimation models produce shrinkage estimators. Thus, Wasserstein distributional robustness offers new probabilistic interpretations for popular regularization techniques. The empirical success of regularization methods in statistics fuels hope that Wasserstein distributionally robust models can effectively combat the optimizer's curse across many application areas. Connections between robustification and regularization will be explored in Section.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

Anticipating black swans: If uncertainty is modeled by the empirical distribution, then the nominal decision problem evaluates the admissible loss functions only at the training samples. However, possible future uncertainty realizations that differ from all training samples but could have devastating consequences ('black swans') are ignored. If the empirical distribution may be perturbed within a Wasserstein ball with a positive radius, on the other hand, then (possibly small amounts of) probability mass can be moved anywhere in the support set $\Xi$. Thus, the Wasserstein distributionally robust decision problem faithfully anticipates the possibility of black swans. We emphasize that all distributions in a Kullback-Leibler divergence ball must be absolutely continuous with respect to the nominal distribution, which implies that the corresponding distributionally robust decision problems ignore the possibility of black swans.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

Axiomatic justification: If the random vector $\xi$ may follow any distribution in some ambiguity set $\mathcal{Q}$ (e.g., a Wasserstein ball), then the scalar random variable $\ell{(\xi)}$ corresponding to a fixed loss function $\ell \in \mathcal{L}$ may follow any distribution in the induced ambiguity set ${\ell_{\ast}{(\mathcal{Q})}} = {\{{\ell_{\ast}{({\mathbb{Q}})}}:{{\mathbb{Q}} \in \mathcal{Q}}\}}$, where $\ell_{\ast}{({\mathbb{Q}})}$ is the pushforward measure of $\mathbb{Q}$ under $\ell$. We call a loss function $\ell \in \mathcal{L}$ unambiguous if $\ell_{\ast}{(\mathcal{Q})}$ is a singleton.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

Under a mild technical condition, the loss functions must then be ranked by the worst-case risk $\sup_{{\mathbb{Q}} \in \mathcal{Q}}{\mathcal{R}{({\mathbb{Q}},\ell)}}$ \[, Theorem 12\]. This result provides an axiomatic justification for adopting a distributionally robust approach.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

Optimality principle: Data-driven optimization aims to use the training data directly to construct an estimator for the objective of problem (a predictor) and a decision that minimizes this predictor (a prescriptor) without the detour of constructing an estimator for $\mathbb{P}$. It has been shown that optimal predictors and the corresponding prescriptors can be constructed by solving a meta-optimization model that minimizes the in-sample risk of the predictor-prescriptor pairs subject to constraints guaranteeing that the in-sample risk is actually attainable out of sample. It has been shown that this meta-optimization problem admits a unique solution: the best predictor-prescriptor pair is obtained by solving a distributionally robust optimization problem over all distributions in some neighborhood of the empirical distribution \[, Theorem 7\]. Thus, if one aims to transform training data to decisions, it is in some precise sense optimal to do this by solving a data-driven distributionally robust optimization problem.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example 1.6 (Limitations of estimator performance)", "weight": 1.0} -->

Distributionally robust optimization models with Wasserstein ambiguity sets were introduced. Reformulations of these models as nonconvex optimization problems as well as initial attempts to solve these problems via algorithms from global optimization are reported and \[, § 7.1\]. In the next section we will review convex reformulations and approximations that were discovered in and significantly generalized.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Computation", "weight": 1.0} -->

The aim of this section is to show that the worst-case risk evaluation problem and the distributionally robust decision problem are computationally tractable in many situations of practical interest. Note first that checking whether a fixed distribution $\mathbb{Q}$ is feasible in requires computing the Wasserstein distance $W_{p}{({\mathbb{Q}},{\hat{\mathbb{P}}}_{N})}$. It is therefore instructive to study the complexity of evaluating Wasserstein distances between arbitrary distributions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Computation", "weight": 1.0} -->

Computing the Wasserstein distance between two discrete distributions amounts to solving a tractable linear program that is susceptible to the network simplex algorithm as well as dual ascent methods or specialized auction algorithms, etc. The set of feasible transportation plans is termed the transportation polytope and displays many useful theoretical properties, which are surveyed. The need to evaluate Wasserstein distances between increasingly fine-grained histograms has recently motivated efficient approximation schemes. When augmented with an entropic regularization term, for instance, the finite-dimensional transportation problem can be solved quickly by using Sinkhorn's algorithm. Variants of this approach use Tikhonov regularizers, Bregman divergences or Tsallis entropies instead of the entropic regularization term. A survey of algorithms for the finite-dimensional transportation problem is provided.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Computation", "weight": 1.0} -->

As soon as at least one of the two involved distributions ceases to be discrete, the Wasserstein distance can no longer be evaluated in polynomial time. Even in the simplest imaginable scenario where one distribution is uniform on a hypercube and the other distribution is discrete with two atoms, computing the Wasserstein distance becomes intractable.

<!-- chunk {"id": "body-0044", "role": "body", "section": "General Analysis of the Worst-Case Risk", "weight": 1.0} -->

Before attempting to derive exact tractable reformulations for the worst-case risk, we focus on the simpler task of establishing efficiently computable upper and lower bounds. To derive a pessimistic upper bound, we note that the transportation cost ${\|{\xi - \xi^{\prime}}\|}^{p}$ is a convex function of the random variable $\|{\xi - \xi^{\prime}}\|$ for any $p \geq 1$. Jensen's inequality thus implies

<!-- chunk {"id": "body-0045", "role": "body", "section": "General Analysis of the Worst-Case Risk", "weight": 1.0} -->

Hence, the worst-case risk of a loss function $\ell \in \mathcal{L}$ over the type-$p$ Wasserstein ball satisfies

<!-- chunk {"id": "body-0046", "role": "body", "section": "General Analysis of the Worst-Case Risk", "weight": 1.0} -->

where the equality follows from the definition of the worst-case risk, while the second inequality is a direct consequence of the Kantorovich-Rubinstein theorem (see Theorem 1.5 ‣ 1 Introduction")). We summarize the above reasoning in the following theorem.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Assume now that the Wasserstein ambiguity set is centered at the empirical distribution defined in ). In this case, under a mild convexity assumption, the worst-case risk can be exactly expressed as the optimal value of a finite convex optimization problem.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 2.7 (Limiting cases I)", "weight": 1.0} -->

For $p = 1$, the constraints of the finite convex program (2.6 ‣ 2.2 Tractability Results for Empirical Nominal Distributions ‣ 2 Computation")) are thus equivalent to

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 2.7 (Limiting cases I)", "weight": 1.0} -->

In the opposite limit when $p$ tends to $\infty$ and $q$ to 1, the function $\varphi{(q)}$ converges to 1. One can then show that $\gamma = 0$ at optimality and that the constraints of problem (2.6 ‣ 2.2 Tractability Results for Empirical Nominal Distributions ‣ 2 Computation")) simplify to^11^1Updated.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 2.7 (Limiting cases I)", "weight": 1.0} -->

We refer to \[, Appendix A.6\] for a formal proof. $\square$

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 2.7 (Limiting cases I)", "weight": 1.0} -->

As it expresses the worst-case risk $\mathcal{R}_{\varepsilon,p}{({\hat{\mathbb{P}}}_{N},\ell)}$ as the optimal value of a minimization problem, Theorem 2.6 ‣ 2.2 Tractability Results for Empirical Nominal Distributions ‣ 2 Computation") primarily serves as a vehicle to solve the distributionally robust decision problem. In order to construct an extremal distribution that solves problem, one may dualize the finite convex program (2.6 ‣ 2.2 Tractability Results for Empirical Nominal Distributions ‣ 2 Computation")) to convert it back to a maximization problem.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 2.9 (Limiting cases II)", "weight": 1.0} -->

For $p = 1$, the last constraint of ) simplifies to

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 2.9 (Limiting cases II)", "weight": 1.0} -->

An intimate connection between distributionally robust optimization with type-$\infty$ Wasserstein balls and classical robust optimization has first been discovered. $\square$

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 2.9 (Limiting cases II)", "weight": 1.0} -->

Even though problem ) is guaranteed to have an optimal solution, the worst-case risk may not be attained by any distribution if $p = 1$. An instance of problem that fails to be solvable is constructed in Example 2.10 ‣ 2.2 Tractability Results for Empirical Nominal Distributions ‣ 2 Computation") below, which replicates \[, Example 2\].

<!-- chunk {"id": "body-0055", "role": "body", "section": "Example 2.10 (Non-existence of extremal distributions)", "weight": 1.0} -->

If $\nu_{\infty} = \varnothing$, one can show that

<!-- chunk {"id": "body-0056", "role": "body", "section": "Example 2.10 (Non-existence of extremal distributions)", "weight": 1.0} -->

is an extremal distribution that solves. For $p > 1$, the last constraint in ) ensures that $\theta_{ij} = 0$ whenever $\alpha_{ij} = 0$ because otherwise $\alpha_{ij}{\|{\theta_{ij}/\alpha_{ij}}\|}^{p}$ evaluates to $\infty$. This implies that the set $\nu_{\infty}$ is empty. Thus, for $p > 1$, the worst-case risk of a piecewise concave loss function is always attained by the discrete distribution ${\mathbb{Q}}^{\star}$ constructed above.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Example 2.10 (Non-existence of extremal distributions)", "weight": 1.0} -->

If $\nu_{\infty} \neq \varnothing$, which is only possible in the special case $p = 1$, the distributions

<!-- chunk {"id": "body-0058", "role": "body", "section": "Example 2.10 (Non-existence of extremal distributions)", "weight": 1.0} -->

are feasible and asymptotically optimal in as $n \geq {|\nu_{\infty}|}$ tends to infinity. Intuitively, these distributions send some atoms with decaying probabilities to infinity along specific recession directions $\theta_{ij}^{\star}$, ${(i,j)} \in \nu_{\infty}$, of the support set. Note that moving an atom to infinity is possible even when only a finite (type-1) transportation budget is available provided that the probability mass transported is inversely proportional to the transportation distance.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Example 2.10 (Non-existence of extremal distributions)", "weight": 1.0} -->

For $p > 1$, atoms can also migrate to infinity at a finite transportation cost provided that their probabilities are inversely proportional to the $p^{th}$ power of the transportation distance. As piecewise concave loss functions grow at most linearly, however, the decay in probability always outweighs the increase in loss. This reasoning provides an intuitive explanation for our insight that $\nu_{\infty} = \varnothing$ and that the supremum in is always attained for $p > 1$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Example 2.10 (Non-existence of extremal distributions)", "weight": 1.0} -->

Given the promising results for piecewise concave loss functions, it is natural to ask whether the convex reformulations of Theorems 2.6 ‣ 2.2 Tractability Results for Empirical Nominal Distributions ‣ 2 Computation") and 2.8 ‣ 2.2 Tractability Results for Empirical Nominal Distributions ‣ 2 Computation") can be generalized. Indeed, it has been discovered that similar results are available for convex (but not piecewise convex) loss functions under the additional condition that there are no support constraints ($\Xi = {\mathbb{R}}^{m}$).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Remark 2.12 (Computing the Lipschitz modulus)", "weight": 1.0} -->

By Theorem 2.11 ‣ 2.2 Tractability Results for Empirical Nominal Distributions ‣ 2 Computation"), computing the worst-case risk of a convex loss function $\ell{(\xi)}$ requires computing the Lipschitz modulus of $\ell{(\xi)}$ with respect to the prescribed norm $\parallel \cdot \parallel$ on ${\mathbb{R}}^{m}$. One can show that

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 2.12 (Computing the Lipschitz modulus)", "weight": 1.0} -->

that is, the Lipschitz modulus of $\ell{(\xi)}$ coincides with the radius of the smallest dual norm ball around 0 that encloses the domain of the conjugate loss function $\ell^{\ast}{(z)}$ \[, § 6.2\]. Unfortunately, problem ) maximizes a convex function over a convex set and is therefore hard. More formally, assume that ${\ell{(\xi)}} = {{\mu^{\top}\xi} + {\|{\Sigma^{\frac{1}{2}}\xi}\|}_{2}}$ for an arbitrary $\mu \in {\mathbb{R}}^{m}$ and $\Sigma \in {\mathbb{S}}_{+}^{m}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Remark 2.12 (Computing the Lipschitz modulus)", "weight": 1.0} -->

An elementary calculation shows that ${\ell^{\ast}{(z)}} = 0$ if $z \in \mathcal{E}$ and ${\ell^{\ast}{(z)}} = \infty$ if $z \notin \mathcal{E}$, where $\mathcal{E} = {\{{\mu + {\Sigma^{\frac{1}{2}}u}}:{{\| u\|}_{2} \leq 1}\}}$ stands for the ellipsoid with center $\mu$ and shape matrix $\Sigma$. Hence, $\mathcal{E}$ is the domain of $\ell^{\ast}{(z)}$. In order to compute the Lipschitz modulus of $\ell{(\xi)}$ with respect to the $\infty$-norm, for example, we thus need to solve an instance of problem ) that maximizes the 1-norm over $\mathcal{E}$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 2.12 (Computing the Lipschitz modulus)", "weight": 1.0} -->

As maximizing the 1-norm over an arbitrary ellipsoid is NP-hard \[, Lemma 4.1\], we conclude that the worst-case risk evaluation problem is intractable even for polyhedral norms and for simple classes of (convex) conic quadratic loss functions. $\square$

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 2.12 (Computing the Lipschitz modulus)", "weight": 1.0} -->

One can show that the supremum of the worst-case risk evaluation problem is never attained under the conditions of Theorem 2.11 ‣ 2.2 Tractability Results for Empirical Nominal Distributions ‣ 2 Computation"), that is, any asymptotically optimal sequence of distributions must push some (decreasing amount of) probability mass to infinity. As in the case of a piecewise concave loss function, such a sequence can be constructed explicitly. To do so, choose a maximizer $z^{\star}$ of problem ), which is generally intractable as pointed out in Remark 2.12 ‣ 2.2 Tractability Results for Empirical Nominal Distributions ‣ 2 Computation"). Moreover, select $i_{0} \in {\lbrack N\rbrack}$ and $\xi^{\star} \in {\arg{\max_{{\|\xi\|} \leq 1}{\xi^{\top}z^{\star}}}}$. Then, the distributions

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 2.12 (Computing the Lipschitz modulus)", "weight": 1.0} -->

can be shown to be feasible and asymptotically optimal in as $n \geq 1$ tends to infinity.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 2.12 (Computing the Lipschitz modulus)", "weight": 1.0} -->

Assume next that $p = 2$, the loss function $\ell{(\xi)}$ is quadratic and the transportation cost in the definition of the Wasserstein distance is induced by the Euclidean norm. Then, the worst-case risk coincides with the optimal value of a tractable semidefinite program (SDP).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Example 2.15 (Non-existence of extremal distributions with $N$ atoms)", "weight": 1.0} -->

If the worst-case risk over a Wasserstein ball centered at the empirical distribution is attained, then there always exists an extremal distribution with $N + 1$ atoms that can be characterized in quasi-closed form \[, Corollary 2\]. In practice, however, it is often convenient to ignore this minimal representability and to search over candidate distributions with more than $N + 1$ atoms, e.g., by solving a finite convex optimization problem such as (2.8 ‣ 2.2 Tractability Results for Empirical Nominal Distributions ‣ 2 Computation")). For generic nominal distributions, necessary and sufficient conditions for the existence of an extremal distribution are detailed in \[, Corollary 1\].

<!-- chunk {"id": "body-0069", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

We will now demonstrate that the worst-case risk evaluation problem and the distributionally robust decision problem sometimes admit exact tractable reformulations or conservative tractable approximations even if the nominal distribution $\hat{\mathbb{P}}$ is continuous. To show this, we assume throughout this section that ${\hat{\mathbb{P}}}_{N}$ has mean vector $\hat{\mu} \in {\mathbb{R}}^{m}$ and covariance matrix $\hat{\Sigma} \in {\mathbb{S}}_{+}^{m}$. Thus, we implicitly assume that ${\hat{\mathbb{P}}}_{N}$ has finite second-order moments.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

We first define an uncertainty set in the space of mean vectors and covariance matrices.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

This uncertainty set is of interest because it covers the projection of the type-2 Wasserstein ball ${\mathbb{B}}_{\varepsilon,2}{({\hat{\mathbb{P}}}_{N})}$ onto the space of mean vectors and covariance matrices. Moreover, if the nominal distribution is elliptical, $\mathcal{U}_{\varepsilon}{(\hat{\mu},\hat{\Sigma})}$ is actually equal to the projection of ${\mathbb{B}}_{\varepsilon,2}{({\hat{\mathbb{P}}}_{N})}$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Remark 2.22 (Second layer of robustness)", "weight": 1.0} -->

Distributionally robust optimization problems akin to ([26a]) and ([26b]) that accommodate a second layer of robustness to account for moment ambiguity have been investigated, among others. As the optimal value of the inner maximization problem is always concave in $(\mu,M)$ but typically nonconcave in $(\mu,\Sigma)$, moment ambiguity has mostly been modeled through convex uncertainty sets for $(\mu,M)$, thereby ensuring convexity of the outer maximization problem. For example, uncertainty sets that force $\mu$ to lie in an ellipsoid and $M$ in the intersection of two positive semi-definite cones were studied, while box-type uncertainty sets for $(\mu,M)$ were proposed and refined. Convex uncertainty sets for $(\mu,\Sigma)$ were shown to render the outer maximization problems convex only in special cases, e.g., when evaluating a worst-case value-at-risk of a linear or quadratic loss function.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Remark 2.22 (Second layer of robustness)", "weight": 1.0} -->

The convex uncertainty set $\mathcal{U}_{\varepsilon}{(\hat{\mu},\hat{\Sigma})}$ for $(\mu,\Sigma)$ is remarkable because it leads to a second-layer maximization problem in ([26a]) that admits a convex reformulation for all loss functions $\ell{(\xi)}$. $\square$

<!-- chunk {"id": "body-0074", "role": "body", "section": "Remark 2.22 (Second layer of robustness)", "weight": 1.0} -->

The decomposition ([26b]) of the Gelbrich risk evaluation problem into two consecutive maximization problems offers a systematic approach to derive convex reformulations. A tractable SDP reformulation is available, for example, when the loss function $\ell{(\xi)}$ is a pointwise maximum of finitely many (possibly indefinite) quadratic functions.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

We now argue that for judiciously calibrated Wasserstein ambiguity sets, the worst-case risk associated with a finite sample size $N$ provides an upper confidence bound on the true risk for all admissible loss functions (finite sample guarantee) and that the worst-case optimal risk converges almost surely to the true optimal risk as $N$ tends to infinity (asymptotic guarantee). Intuitively, the finite sample guarantee ensures that the out-of-sample risk will fall short of the worst-case risk with high confidence when we implement an optimizer of the distributionally robust decision probelm, while the asymptotic guarantee formalizes the simple intuition that more data enables us to make better decisions.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

Concentration inequalities for the nominal distribution ${\hat{\mathbb{P}}}_{N}$ and its moments can be used to derive finite sample and asymptotic guarantees. If ${\hat{\mathbb{P}}}_{N}$ is the empirical distribution, for instance, one can prove that ${\hat{\mathbb{P}}}_{N}$ converges exponentially fast to the data-generating distribution $\mathbb{P}$, in probability with respect to the Wasserstein distance, as $N$ tends to infinity.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Remark 3.3 (Improved finite sample guarantees)", "weight": 1.0} -->

Requiring the Wasserstein ball to cover $\mathbb{P}$ with high confidence is only a sufficient but not a necessary condition for the finite sample guarantees (32a ‣ 3 Performance Guarantees")) and (32b ‣ 3 Performance Guarantees")). Indeed, these guarantees can be sustained even if the Wasserstein radius is reduced below $\varepsilon_{N}{(\eta)}$, which is essentially the smallest radius for which the Wasserstein ball represents a $({1 - \eta})$-confidence set for $\mathbb{P}$. The minimal Wasserstein radius that preserves the finite sample guarantees (32a ‣ 3 Performance Guarantees")) and (32b ‣ 3 Performance Guarantees")) often decays significantly faster than $\mathcal{O}{(N^{- \frac{1}{m}})}$ without suffering from a curse of dimensionality.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Remark 3.3 (Improved finite sample guarantees)", "weight": 1.0} -->

If $p = 1$, the data-generating distribution is absolutely continuous with respect to the Lebesgue measure and the set $\mathcal{L}$ of admissible loss functions admits a smooth parameterization, for example, one can show that a Wasserstein radius of the order $\mathcal{O}{(\sqrt{\log{m/N}})}$ maintains finite sample guarantees akin to (32a ‣ 3 Performance Guarantees")) and (32b ‣ 3 Performance Guarantees")), which is consistent with recent findings in the compressed sensing and high-dimensional statistics literature \[, Theorem 1\]. $\square$

<!-- chunk {"id": "body-0079", "role": "body", "section": "Remark 3.3 (Improved finite sample guarantees)", "weight": 1.0} -->

As the number $N$ of training samples grows, one can simultaneously reduce the Wasserstein radius $\varepsilon$ and the significance level $\eta$ without sacrificing the finite sample guarantees (32a ‣ 3 Performance Guarantees")) and (32b ‣ 3 Performance Guarantees")), which allows us to prove asymptotic consistency \[, Theorem 3.6\].

<!-- chunk {"id": "body-0080", "role": "body", "section": "Distributionally Robust Optimization in Machine Learning", "weight": 1.0} -->

We now demonstrate that the theory of data-driven distributionally robust optimization with Wasserstein ambiguity sets has interesting ramifications for statistical learning and motivates new approaches for addressing fundamental learning tasks such as classification (Section [4.1]), regression (Section [4.2]), maximum likelihood estimation (Section [4.3]) or minimum mean square error estimation (Section [4.4]). We conclude with an overview of other applications of distributionally robust optimization in machine learning (Section [4.5]).

<!-- chunk {"id": "body-0081", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

In binary classification problems the central object of study is a random vector $\xi = {(x,y)}$, where $x \in {\mathbb{R}}^{n}$ is termed the input, and $y \in {\{{- 1},{+ 1}\}}$ is referred to as the output. The distribution $\mathbb{P}$ of $\xi$ is unknown but indirectly observable through finitely many training samples ${\hat{\xi}}_{i} = {({\hat{x}}_{i},{\hat{y}}_{i})}$, $i \in {\lbrack N\rbrack}$. The goal of binary classification is to predict the output $y$ corresponding to a given input $x$. The classifier with the lowest possible misclassification probability is the one that predicts $y = 1$ if ${{\mathbb{P}}{\lbrack{y = \left.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

1 \middle| x \right.}\rbrack}} \geq 0.5$ and $y = {- 1}$ otherwise. Unfortunately, this classifier is not implementable when $\mathbb{P}$ is unknown.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

Statistical learning aims to construct classifiers solely on the basis of the training data. One of the most popular approaches in practice is to construct a linear scoring function $w^{\top}x$, encoded by a weight vector $w \in {\mathbb{R}}^{n}$, and to predict $y$ as the sign of $w^{\top}x$. In hindsight, the prediction was correct if the actual output $y$ coincides with the predicted output $\operatorname{sign}{({w^{\top}x})}$ or, equivalently, if the product ${y \cdot w^{\top}}x$ is positive. The realized prediction error can thus be quantified by $L{({{y \cdot w^{\top}}x})}$, where $L{(z)}$ is some nonnegative and non-increasing univariate loss function that is large for negative and small for positive values of $z$. Examples of popular loss functions are listed in Table [4.1].

<!-- chunk {"id": "body-0084", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

The best scoring function for a given choice of $L{(z)}$ is the one whose weight vector $w$ minimizes the expected prediction error ${\mathbb{E}}^{\mathbb{P}}{\lbrack{L{({{y \cdot w^{\top}}x})}}\rbrack}$. Unfortunately, the expectation is evaluated under the unknown distribution $\mathbb{P}$, and thus the optimal scoring function cannot be computed. Promising near-optimal scoring functions can be found, however, by solving a distributionally robust classification model that minimizes the worst-case expected prediction error with respect to a type-1 Wasserstein ball, that is,

<!-- chunk {"id": "body-0085", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

where ${\hat{\mathbb{P}}}_{N}$ is the empirical distribution on the training samples. We assume here that all distributions in the Wasserstein ball are supported on $\Xi = {{\mathbb{X}} \times {\mathbb{Y}}}$, where ${\mathbb{X}} \subseteq {\mathbb{R}}^{n}$ is convex and closed, while ${\mathbb{Y}} = {\{{- 1},{+ 1}\}}$. We also assume that the norm on the input-output space used in the definition of the Wasserstein distance is additively separable, that is, ${\|\xi\|} = {{\| x\|} + {\frac{\kappa}{2}{|y|}}}$, where---by slight abuse of notation---$\| x\|$ stands for an arbitrary norm on the input space, while $\kappa > 0$ quantifies the relative importance of outputs versus inputs.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

Commonly used loss functions for binary classification. \upname L(z) learning model \down \uphinge loss max {0, 1 − z} support vector machine smooth hinge loss $\left\{ \begin{array}{ll}
{\frac{1}{2} - z} &amp; {{\text{if~}z} \leq 0} \\
{\frac{1}{2}\left( {1 - z} \right)^{2}} &amp; {{\text{if~}0} &lt; z &lt; 1} \\
0 &amp; {{\text{if~}z} \geq 1}
\end{array} \right.$ smooth support vector machine logloss log (1+exp (−z)) logistic regression \down

<!-- chunk {"id": "body-0087", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

The classification model is easily recognized as an instance of the distributionally robust decision problem that optimizes over all (multivariate) loss functions of the form ${\ell{(\xi)}} = {L{({{y \cdot w^{\top}}x})}}$ parameterized by $w \in {\mathbb{R}}^{n}$. By leveraging Theorem 2.6 ‣ 2.2 Tractability Results for Empirical Nominal Distributions ‣ 2 Computation"), problem can be recast as a finite convex program if $L{(z)}$ is convex and piecewise linear, while $\mathbb{X}$ is convex and closed. An alternative convex reformulation can be obtained from Theorem 2.11 ‣ 2.2 Tractability Results for Empirical Nominal Distributions ‣ 2 Computation") if $L{(z)}$ is convex (but not necessarily piecewise linear), while ${\mathbb{X}} = {\mathbb{R}}^{n}$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

For all univariate loss functions listed in Table [4.1], the convex reformulations of problem are equivalent to tractable conic programs. Explicit formulations of these conic programs are reported in \[, § 3.2\].

<!-- chunk {"id": "body-0089", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

The distributionally robust classification problem encapsulates two interesting special cases. First, if the Wasserstein radius is set to $\varepsilon = 0$, then collapses to the standard empirical risk minimization problem that minimizes the average prediction error across the training samples. Moreover, if the parameter $\kappa$ appearing in the definition of the norm tends to infinity, then reduces to a classical regularized empirical risk minimization problem.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Distributionally Robust Regression", "weight": 1.0} -->

The goal of regression is a to predict a real (as opposed to a categorical) output $y \in {\mathbb{R}}$ corresponding to a given input $x \in {\mathbb{R}}^{n}$. The regressor that attains the lowest possible mean squared error is the one that predicts the output as ${\mathbb{E}}^{\mathbb{P}}{\lbrack\left. y \middle| x \right.\rbrack}$. Unfortunately, this regressor is not implementable when the distribution $\mathbb{P}$ of the random vector $\xi = {(x,y)}$ is unknown.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Distributionally Robust Regression", "weight": 1.0} -->

In practice it is often convenient to construct a linear regressor that predicts the output by a linear function $w^{\top}x$ encoded by a weight vector $w \in {\mathbb{R}}^{n}$. The realized prediction error can thus be quantified by $L{({{w^{\top}x} - y})}$, where $L{(z)}$ is some nonnegative univariate loss function that is large when $z$ deviates from 0. Examples of popular loss functions for regression are listed in Table [4.2]. The best linear regressor that minimizes the expected prediction error ${\mathbb{E}}^{\mathbb{P}}{\lbrack{L{({{w^{\top}x} - y})}}\rbrack}$ cannot be computed when $\mathbb{P}$ is unknown, but promising near-optimal linear regressors can be found by solving the distributionally robust regression model

<!-- chunk {"id": "body-0092", "role": "body", "section": "Distributionally Robust Regression", "weight": 1.0} -->

which minimizes the worst-case expected prediction error in view of all distributions on a convex closed set $\Xi = {{\mathbb{X}} \times {\mathbb{Y}}} \subseteq {{\mathbb{R}}^{n} \times {\mathbb{R}}}$ within a type-$p$ Wasserstein ball around the empirical distribution on $N$ training samples. By Theorem 2.6 ‣ 2.2 Tractability Results for Empirical Nominal Distributions ‣ 2 Computation"), problem can be reformulated as a finite convex program if $p = 1$, $L{(z)}$ is convex and piecewise linear, and $\mathbb{X}$ and $\mathbb{Y}$ are convex and closed.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Distributionally Robust Regression", "weight": 1.0} -->

A convex reformulation can also be obtained from Theorem 2.6 ‣ 2.2 Tractability Results for Empirical Nominal Distributions ‣ 2 Computation") if $p = 1$, $L{(z)}$ is convex (but not necessarily piecewise linear), while ${\mathbb{X}} = {\mathbb{R}}^{n}$ and ${\mathbb{Y}} = {\mathbb{R}}$. Moreover, problem can be reformulated as a finite convex program by using Theorem 2.13 ‣ 2.2 Tractability Results for Empirical Nominal Distributions ‣ 2 Computation") if $p = 2$, $L{(z)}$ is convex quadratic, ${\mathbb{X}} = {\mathbb{R}}^{n}$ and ${\mathbb{Y}} = {\mathbb{R}}$. For details see \[, § 3.1\] and \[, § 3\].

<!-- chunk {"id": "body-0094", "role": "body", "section": "Distributionally Robust Regression", "weight": 1.0} -->

Commonly used loss functions for regression \upname L(z) parameter learning model \down \upsquared error z2 n/a ordinary least squares Huber loss $\left\{ \begin{array}{ll}
{\frac{1}{2}\xi^{2}} &amp; {{\text{if~}{|z|}} \leq \delta} \\
{\delta{({{|z|} - {\frac{1}{2}\delta}})}} &amp; \text{otherwise}
\end{array} \right.$ δ ∈ ℝ+ Huber regression δ-insensitive loss max {0, |z| − δ} δ ∈ ℝ+ support vector regression pinball loss max {−δz, (1−δ)z} δ ∈ quantile regression \down

<!-- chunk {"id": "body-0095", "role": "body", "section": "Distributionally Robust Regression", "weight": 1.0} -->

Assume now that the norm on the input-output space satisfies ${\|\xi\|} = {{\| x\|} + {\frac{\kappa}{2}{|y|}}}$, where $\| x\|$ is an arbitrary norm on the input space, while $\kappa > 0$ quantifies the relative importance of outputs versus inputs. In the absence of output uncertainty (that is, for $\kappa = \infty$), there is again an intimate relation between robustification and regularization.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

Consider now the problem of estimating the mean vector $\mu \in {\mathbb{R}}^{m}$ and the covariance matrix $\Sigma \in {\mathbb{S}}_{+}^{m}$ of a random vector $\xi \in {\mathbb{R}}^{m}$ from independent training samples ${\hat{\xi}}_{i}$, $i \in {\lbrack N\rbrack}$. The simplest estimators for $\mu$ and $\Sigma$ are the sample mean $\hat{\mu}$ and the sample covariance matrix $\hat{\Sigma}$, which we define as the actual mean and covariance matrix of the empirical distribution, i.e.,

<!-- chunk {"id": "body-0097", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

While $\Sigma$ serves as an input for many problems in engineering, science or economics, it is often the precision matrix $\Sigma^{- 1}$ that appears in their solutions. For example, in mean-variance portfolio analysis the portfolio variance to be minimized depends on the covariance matrix of the asset returns, while the optimal portfolio weights depend on the precision matrix. Similarly, linear discriminant analysis uses the covariance matrix of the features as an input and outputs a maximum likelihood classifier that depends on the precision matrix. Moreover, the optimal fingerprint method for climate change detection requires the covariance matrix of the internal climate variability as an input and outputs a climate change signal depending on the precision matrix. Thus, it is often more important to know the precision matrix than the covariance matrix. To ensure that the precision matrix is well defined, we will henceforth assume that $\Sigma \succ 0$. Unfortunately, the sample covariance matrix is rank-deficient in the big-data regime when the dimension of $\xi$ exceeds the sample size ($m > N$) even if $\Sigma$ has full rank.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

In this case, one cannot invert $\hat{\Sigma}$ to obtain a meaningful precision matrix estimator.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

From now on we will assume that the unknown true distribution $\mathbb{P}$ of $\xi$ is normal. Thus, the problem of maximizing the log-likelihood of the training samples reduces to the following convex program over all candidate mean vectors $\mu$ and precision matrices $X$ \[, § 7.1\]. \\be inf_μ∈R\^m, X ∈S\_+\^m { -logdetX + 1N ∑\_i=1\^N (\^ξ_i - μ)\^⊤X (\^ξ_i - μ) } \\eeUnfortunately, this maximum likelihood estimation (MLE) problem is unbounded for $N \leq m$ and (almost surely) solved by $\mu^{\star} = \hat{\mu}$ and $X^{\star} = {\hat{\Sigma}}^{- 1}$ for $N > m$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

Thus, we fail again to find an estimator in the big-data regime and simply recover the sample mean and the sample covariance matrix in the small-data regime. To overcome this deficiency, we robustify the MLE problem against all distributions within a type-2 Wasserstein ball centered at the normal nominal distribution ${\hat{\mathbb{P}}}_{N} = {\mathcal{N}{(\hat{\mu},\hat{\Sigma})}}$, that is, we solve the robust MLE problem \\be inf_μ∈R\^m, X∈S\_+\^m {-logdetX + sup_Q ∈B_ε, 2(\^P_N) E\^Q \[(ξ-μ)\^⊤X (ξ-μ) \]}.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

\\eeIf $\varepsilon = 0$, then the robust MLE problem ([4.3]) reduces to the nominal MLE problem ([4.3]) because---by the definition of the sample mean and the sample covariance matrix---the (normal) nominal distribution has the same first- and second-order moments as the (discrete) empirical distribution and because the loss function in the expectation is quadratic in $\xi$. One can show via Theorem 2.25 ‣ 2.3 Tractability Results for Elliptical Nominal Distributions ‣ 2 Computation") that ([4.3]) is equivalent to a convex SDP with a determinant term in the objective function. Provided that the Wasserstein radius $\varepsilon$ is strictly positive, this SDP is solvable even in the big-data regime when $m > N$. Thus, it yields a valid precision matrix estimator even if the sample covariance matrix is rank-deficient. Moreover, as SDPs are tractable, the optimal estimator can be computed in polynomial time.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

In fact, the SDP at hand is highly symmetric and can therefore even be solved in closed form \[, Theorem 3.1\].

<!-- chunk {"id": "body-0103", "role": "body", "section": "Distributionally Robust Minimum Mean Square Error Estimation", "weight": 1.0} -->

This elementary problem is fundamental for numerous applications in engineering (e.g., linear systems theory ), econometrics (e.g., linear regression, time series analysis ), machine learning and signal processing (e.g., Kalman filtering ) or information theory (e.g., multiple-input multiple-output systems ), etc. To formalize the estimation problem, we define an estimator as a measurable function $\psi{(y)}$ that maps the observation $y$ to a prediction of the signal $x$, and we denote by $\Psi$ the family of all possible estimators. Moreover, we define the distributionally robust minimum mean square error (MMSE) estimator as an optimizer of

<!-- chunk {"id": "body-0104", "role": "body", "section": "Distributionally Robust Minimum Mean Square Error Estimation", "weight": 1.0} -->

Note that constitutes an infinite-dimensional functional optimization problem and thus appears to be hard. However, by establishing a minimax theorem for and exploiting the properties of elliptical distributions, one can show that the outer infimum in is attained by an affine estimator. Combining this structural insight with Theorem 2.25 ‣ 2.3 Tractability Results for Elliptical Nominal Distributions ‣ 2 Computation") allows us to prove that the estimation problem is in fact equivalent to a convex program.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Other Applications in Machine Learning", "weight": 1.0} -->

Ideas from distributionally robust optimization also permeate several other areas of statistics and machine learning. For example, a distributionally robust optimization model involving two Wasserstein balls centered at two distinct empirical distributions can be used to develop a computationally tractable convex approximation for the minimax robust hypothesis testing problem that aims to minimize the maximum of the worst-case type-I and type-II errors of a prescribed hypothesis test. Another example is data-driven inverse optimization, where one observes random signals as well as optimal solutions of an optimization problem parameterized by these signals. The aim is to predict the solution corresponding to a new unseen signal from $N$ independent historical observations without any knowledge of the optimization problem's objective function. This problem can be framed as a structural regression problem that minimizes the worst-case expected prediction loss with respect to a Wasserstein ambiguity set over a space of candidate objective functions. Data-driven inverse optimization lends itself, for example, to learning the purchasing behavior of consumers, the production costs of electricity generators, the route choice preferences of passengers in a multimodal transportation system or the hidden optimality principles governing a biological system.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Other Applications in Machine Learning", "weight": 1.0} -->

As a third example, distributionally robust optimization models with Wasserstein ambiguity sets can be used to efficiently compute the worst-case misclassification probability of a given classifier, which amounts to evaluating the worst-case expectation of the (nonconvex) zero-one loss. Using similar techniques, one can also efficiently compute the worst-case probability of an undesirable event described by the conjunction or disjunction of several linear inequalities for the random vector $\xi$. If the undesirable event can be influenced so as drive its worst-case probability below a prescribed tolerance, we face a distributionally robust chance constraint. Even though distributionally robust chance constrained programs with Wasserstein ambiguity sets around the empirical distribution are intractable in general, they are sometimes equivalent to mixed-integer linear programs that can be solved with off-the-shelf software. In contrast, distributionally robust chance constrained programs with moment ambiguity sets can often be reformulated as (or tightly approximated by) tractable conic programs.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Other Applications in Machine Learning", "weight": 1.0} -->

To conclude, we highlight two opportunities for tailoring a distributionally robust decision problem with a Wasserstein ambiguity set around the empirical distribution to a given training dataset. Recall first that finite sample guarantees hold whenever $\varepsilon$ is large enough for the Wasserstein ball to contain the unknown data-generating distribution with high confidence $1 - \beta$. Recall also that the distributionally robust decision problem can often be reformulated as a tractable convex program whose size scales with the sample size $N$.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Other Applications in Machine Learning", "weight": 1.0} -->

If the computational burden is unmanageable for the given sample size, we can select $K \ll N$, approximate ${\hat{\mathbb{P}}}_{N}$ with the closest $K$-point distribution ${\mathbb{Q}}_{K}^{\star}$ in Wasserstein distance and replace the original Wasserstein ball of radius $\varepsilon$ around ${\hat{\mathbb{P}}}_{N}$ with a new inflated Wasserstein ball of radius $\varepsilon + {W_{p}{({\hat{\mathbb{P}}}_{N},{\mathbb{Q}}_{K}^{\star})}}$ around ${\mathbb{Q}}_{K}^{\star}$. By construction, the inflated Wasserstein ball contains the data-generating distribution with the same confidence $1 - \beta$. But the size of the corresponding decision problem is only proportional to $K$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Other Applications in Machine Learning", "weight": 1.0} -->

This approach provides a systematic method for reducing the computational burden without sacrificing robustness guarantees (but at the expense of increasing the model's level of conservatism). The approximation of a rich $N$-point distribution with a sparse $K$-point distribution is referred to as scenario reduction in the stochastic programming literature. While the exact computation of ${\mathbb{Q}}_{K}^{\star}$ is hard, there exist efficient approximation algorithms for scenario reduction.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Other Applications in Machine Learning", "weight": 1.0} -->

An important input for any distributionally robust optimization model with a Wasserstein ambiguity set is the norm that determines the transportation cost in the definition of the Wasserstein distance. The flexibility to choose this norm could be exploited to improve the out-of-sample performance of the model's optimizers. A method for learning the best Mahalanobis norm from the training data is described. It is shown that this metric learning framework encompasses adaptive regularization as a special case.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Other Applications in Machine Learning", "weight": 1.0} -->

*Acknowledgments.* This research was funded by the SNSF grant BSCGI0_157733. We are grateful to Erick Delage, Bart Van Parys and Shuhao Yan for pointing out errors in the published version of this paper.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Conjugates, Support Functions and Dual Norms", "weight": 1.0} -->

Examples of support functions. \upΞ σΞ(z) dom(σΞ)\down \up{ξ: ∥ξ∥ ≤ b} b∥z∥* ℝm {ξ: Cξ ≤ d} inf {λ⊤d: λ ∈ ℝ+l, C⊤λ = z} {C⊤λ: λ ∈ ℝ+l} {ξ: f(ξ) ≤ 0} inf {λf*(z/λ): λ ∈ ℝ+l} − recc (f)* {ξ: ξ ∈ Ξk∀k ∈ [K]} $\inf{\{{\sum_{k = 1}^{K}{\sigma_{\Xi_{k}}{(z_{k})}}}:{{\sum_{k = 1}^{K}z_{k}} = z}\}}$ − ⋂k ∈ [K]recc (Ξk)* \down Assume that b ∈ ℝ+, C ∈ ℝl × m and d ∈ ℝl. Let f(ξ) be a closed, proper and convex function, and let Ξk, k ∈ [K], be convex closed sets with nonempty intersection.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Conjugates, Support Functions and Dual Norms", "weight": 1.0} -->

Denote by recc (f)* and recc (Ξk)* the cones dual to the recession cones of the function f(ξ) and the set Ξk, respectively.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Conjugates, Support Functions and Dual Norms", "weight": 1.0} -->

Examples of dual norms. \up∥ξ∥ ∥z∥* comment\down ∥ξ∥p ∥z∥q standard p-norms ∥ξ∥1 ∥z∥∞ limiting case when p ↓ 1 and q ↑ ∞ α∥ξ∥p $\frac{1}{\alpha}{\| z\|}_{q}$ scaled p-norms ∥Aξ∥p ∥A−1z∥q scaled p-norms ∑k ∈ [K]∥ξk∥pk maxk ∈ [K]∥zk∥qk additively separable norms Assume that p, q ≥ 1 with ${\frac{1}{p} + \frac{1}{q}} = 1$, α &gt; 0, A ∈ 𝕊++m, and pk, qk ≥ 1 with ${\frac{1}{p_{k}} + \frac{1}{q_{k}}} = 1$ for all k ∈ [K]. Moreover, ξ = (ξ1,…,ξK) and z = (z1,…,zK), where ξk, zk ∈ ℝmk and ${\sum_{k = 1}^{K}m_{k}} = m$.
