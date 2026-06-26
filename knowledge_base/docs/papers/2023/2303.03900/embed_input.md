<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study optimal transport-based distributionally robust optimization problems where a fictitious adversary, often envisioned as nature, can choose the distribution of the uncertain problem parameters by reshaping a prescribed reference distribution at a finite transportation cost. In this framework, we show that robustification is intimately related to various forms of variation and Lipschitz regularization even if the transportation cost function fails to be (some power of) a metric. We also derive conditions for the existence and the computability of a Nash equilibrium between the decision-maker and nature, and we demonstrate numerically that nature's Nash strategy can be viewed as a distribution that is supported on remarkably deceptive adversarial samples. Finally, we identify practically relevant classes of optimal transport-based distributionally robust optimization problems that can be addressed with efficient gradient descent algorithms even if the loss function or the transportation cost function are nonconvex (but not both at the same time).

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Because of their relevance for empirical risk minimization in machine learning, stochastic optimization methods are becoming increasingly popular beyond their traditional application domains in operations research and economics. In the wake of the ongoing data revolution and the rapid emergence of ever more complex decision problems, there is also a growing need for stochastic optimization models outputting reliable decisions that are insensitive to input misspecification and easy to compute.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A (static) stochastic optimization problem aims to minimize the expected value ${\mathbb{E}}_{Z\sim{\mathbb{P}}}[\ell(\theta,Z)]$ of an uncertainty-affected loss function $\ell:{\mathbb{R}}^{m}\times{\mathbb{R}}^{d}\to(-\infty,\infty]$ across all feasible decisions $\theta\in\Theta\subseteq{\mathbb{R}}^{m}$, where $Z$ is the random vector of all uncertain problem parameters that is governed by some probability distribution ${\mathbb{P}}$ supported on ${\mathcal{Z}}\subseteq{\mathbb{R}}^{d}$. To exclude trivialities, we assume throughout the paper that the feasible set $\Theta$ and the support set ${\mathcal{Z}}$ are non-empty and closed. Despite their simplicity, static stochastic optimization problems are ubiquitous in statistics and machine learning, among many other application domains.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, their practical deployment is plagued by a fundamental challenge, namely that the distribution ${\mathbb{P}}$ governing $Z$ is rarely accessible to the decision-maker. In a data-driven decision situation, for instance, ${\mathbb{P}}$ is only indirectly observable through a set of independent training samples. In this case one may use standard methods from statistics to construct a parametric or non-parametric reference distribution $\hat{{\mathbb{P}}}$ from the data. However, $\hat{\mathbb{P}}$ invariably differs from ${\mathbb{P}}$ due to inevitable statistical errors, and optimizing in view of $\hat{{\mathbb{P}}}$ instead of ${\mathbb{P}}$ may lead to decisions that display a poor performance on test data. For example, in machine learning it is well known that deep neural networks trained in view of the empirical distribution of the training data can easily be fooled by adversarial examples, that is, test samples subject to seemingly negligible noise that cause the neural network to make a wrong prediction.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Even worse, the decision problem at hand could suffer from a distribution shift, that is, the training data may originate from a distribution other than ${\mathbb{P}}$, under which decisions are evaluated.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A promising strategy to mitigate the detrimental effects of estimation errors in the reference distribution $\hat{{\mathbb{P}}}$ would be to minimize the worst-case expected loss with respect to all distributions in some neighborhood of $\hat{{\mathbb{P}}}$. There is ample evidence that, for many natural choices of the neighborhood of $\hat{{\mathbb{P}}}$, this distributionally robust approach leads to tractable optimization models and provides a simple means to derive powerful generalization bounds. Specialized distributionally robust approaches may even enable generalization in the face of domain shifts or may make the training of deep neural networks more resilient against adversarial attacks.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

More formally, distributionally robust optimization (DRO) captures the uncertainty about the unknown distribution ${\mathbb{P}}$ through an ambiguity set ${\mathbb{B}}_{\varepsilon}(\hat{{\mathbb{P}}})$, that is, an $\varepsilon$-neighborhood of the reference distribution $\hat{{\mathbb{P}}}$ with respect to a distance function on the space ${\mathcal{P}}({\mathcal{Z}})$ of all distributions supported on ${\mathcal{Z}}$. Using this ambiguity set, the DRO problem of interest is formulated as the minimax problem Problem can be viewed as a zero-sum game between the decision-maker, who chooses the decision $\theta$, and a fictitious adversary, often envisioned as 'nature', who chooses the distribution ${\mathbb{Q}}$ of $Z$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

function satisfying the identity of indiscernibles ($c(z,\hat{z})=0$ if and only if $z=\hat{z}$), and $\Pi({\mathbb{P}},\hat{{\mathbb{P}}})$ represents the set of all joint probability distributions of $Z$ and $\hat{Z}$ with marginals ${\mathbb{P}}$ and $\hat{{\mathbb{P}}}$, respectively.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Note that the ambiguity set ${\mathbb{B}}_{\varepsilon}(\hat{{\mathbb{P}}})$ constructed in this way may be interpreted as the family of all probability distributions ${\mathbb{Q}}$ that can be obtained by reshaping the reference distribution $\hat{{\mathbb{P}}}$ at a finite cost of at most $\varepsilon\geq 0$, where the cost of moving unit probability from $\hat{z}$ to $z$ is given by $c(z,\hat{z})$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The following regularity conditions will be assumed to hold throughout the paper.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 1 (Continuity assumptions)", "weight": 1.0} -->

The transportation cost function $c(z,\hat{z})$ is lower semicontinuous in $(z,\hat{z})$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 1 (Continuity assumptions)", "weight": 1.0} -->

For any $\theta\in\Theta$, the loss function $\ell(\theta,\hat{z})$ is upper semicontinuous and $\hat{{\mathbb{P}}}$-integrable in $\hat{z}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 1 (Continuity assumptions)", "weight": 1.0} -->

Assumption 1. ‣ 1 Introduction ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (i) ‣ Assumption 1 (Continuity assumptions). ‣ 1 Introduction ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") ensures that the optimal transport problem in the definition of $d_{c}({\mathbb{P}},\hat{{\mathbb{P}}})$ is solvable \[95, Theorem 4.1\] and admits a strong dual linear program over a space of integrable functions \[95, Theorem 5.10\]. Together, Assumptions 1. ‣ 1 Introduction ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (i) ‣ Assumption 1 (Continuity assumptions). ‣ 1 Introduction ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") and 1. ‣ 1 Introduction ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (ii) ‣ Assumption 1 (Continuity assumptions).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1 (Continuity assumptions)", "weight": 1.0} -->

‣ 1 Introduction ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") ensure that the inner maximization problem in admits a strong dual minimization problem \[16, Theorem 1\]; see also Proposition 1. ‣ 1 Introduction ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") below. Optimal transport-based DRO problems of the form are nowadays routinely studied in diverse areas such as statistical learning, estimation and filtering, control, dynamical systems theory, hypothesis testing, inverse optimization, and chance constrained programming etc.; see for a recent survey. The existing literature focuses almost exclusively on Wasserstein ambiguity sets, which are obtained by setting the transportation cost function to $c(z,\hat{z})=\|z-\hat{z}\|^{p}$ for some norm $\|\cdot\|$ on ${\mathbb{R}}^{d}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1 (Continuity assumptions)", "weight": 1.0} -->

Allowing for more general transportation cost functions enables the decision-maker to inject prior information about the likelihood of certain subsets of ${\mathcal{Z}}$ into the definition of the ambiguity set. For example, setting $c(z,\hat{z})=\infty\cdot\mathds{1}_{z\not\in{\mathbb{A}}(\hat{z})}$ for some closed set ${\mathbb{A}}(\hat{z})\subseteq{\mathcal{Z}}$ with $\hat{z}\in{\mathbb{A}}(\hat{z})$ ensures that the probability mass located at $\hat{z}$ cannot be moved outside of ${\mathbb{A}}(\hat{z})$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1 (Continuity assumptions)", "weight": 1.0} -->

More generally, assigning $c(z,\hat{z})$ a large value for every $\hat{z}$ in the support of the reference distribution $\hat{{\mathbb{P}}}$ makes it expensive for nature to transport probability mass to $z$. Thus, $z$ has a low probability under every distribution in the ambiguity set. The following proposition describes a strong dual of nature's inner maximization problem in and reveals how $c$ impacts the solution of the underlying DRO problem. This strong duality result was first established in for finite-dimensional problems with discrete reference distributions and then generalized.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Nash Equilibria in DRO", "weight": 1.0} -->

By construction, the DRO problem constitutes a zero-sum game between an agent, who chooses the decision $\theta\in\Theta$, and some fictitious adversary or 'nature', who chooses the distribution ${\mathbb{Q}}\in{\mathbb{B}}_{\varepsilon}(\hat{{\mathbb{P}}})$. In this section we will show that, under some mild technical conditions, any optimal solution $\theta^{\star}$ that solves the primal DRO problem and any optimal distribution ${\mathbb{Q}}^{\star}$ that solves the dual DRO problem form a Nash equilibrium. Thus, $\theta^{\star}$ and ${\mathbb{Q}}^{\star}$ satisfy the saddle point condition The existence of a Nash equilibrium implies that and are strong duals (that is, they share the same optimal values) and that they are both solvable. However, strong duality does not imply the existence of a Nash equilibrium (that is, the optimal values are not necessarily attained).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Nash Equilibria in DRO", "weight": 1.0} -->

While it is well known that the primal DRO problem has a wide range of applications, the practical relevance of the dual DRO problem is less obvious. Indeed, the dual problem models a situation in which the decision maker observes the distribution that governs random quantities. As we will explain below, however, the dual DRO problem has deep connections to robust statistics, machine learning and related fields. In robust statistics, an optimal solution $\theta^{\star}$ of an estimation problem of the form is referred to as a minimax estimator or a robust estimator.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Nash Equilibria in DRO", "weight": 1.0} -->

When $\theta^{\star}$ and ${\mathbb{Q}}^{\star}$ satisfy the saddle point condition, then the robust estimator $\theta^{\star}$ solves the stochastic program $\min_{\theta\in\Theta}~{\mathbb{E}}_{Z\sim{\mathbb{Q}}^{\star}}\left[\ell(\theta,Z)\right]$, which minimizes the expected loss under the crisp distribution ${\mathbb{Q}}^{\star}$; see also \[58, Chapter 5\]. For this reason, ${\mathbb{Q}}^{\star}$ is often referred to as a least favorable distribution. The existence of ${\mathbb{Q}}^{\star}$ makes the robust estimator $\theta^{\star}$ particularly attractive.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Nash Equilibria in DRO", "weight": 1.0} -->

Indeed, if ${\mathbb{Q}}^{\star}$ exists, then $\theta^{\star}$ solves a classical stochastic program akin to the ideal learning problem one would want to solve if the true distribution was known.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Nash Equilibria in DRO", "weight": 1.0} -->

Nash equilibria are also relevant for adversarial machine learning, which aims to immunize neural networks against perturbations of the input data. An important aspect of adversarial training is the generation of adversarial examples, which are perturbations of training samples designed to mislead the neural network into making false predictions. Given a fixed neural network encoded by $\hat{\theta}\in\Theta$, one can construct adversarial examples by solving the worst-case expectation problem Specifically, adversarial examples can be obtained by sampling from an extremal distribution ${\mathbb{Q}}^{\star}$ that solves problem. A desirable property of adversarial examples is their transferability across models. An adversarial example that fools one model often succeeds in fooling other models, too, thus enabling attacks on machine learning systems without direct access to the target model. Hence, incorporating transferable adversarial examples into training is likely to enhance the robustness and security of the resulting model. The dual DRO problem offers a systematic approach to generate transferable adversarial examples.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Nash Equilibria in DRO", "weight": 1.0} -->

Specifically, the solutions of constitute model-agnostic worst-case distributions that depend only on the decision space $\Theta$. In contrast, the worst-case distributions that solve problem are tailored to a specific model $\hat{\theta}\in\Theta$. The solutions of are designed to challenge all decisions within $\Theta$, thus making them inherently transferable across all possible prediction models.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Nash Equilibria in DRO", "weight": 1.0} -->

To date, dual DRO problems have only been investigated in specific applications. For example, it is known that the least favorable distributions in distributionally robust minimum mean square error estimation and Kalman filtering problems over type-$2$ Wasserstein ambiguity sets centered at Gaussian reference distributions are Gaussian, and that they can be computed efficiently via semidefinite programming. When the ambiguity set is defined in terms of the Kullback-Leibler divergence instead of the Wasserstein distance, the least favorable distribution remains Gaussian and can be found in quasi-closed form. Similar results are available for generalized $\tau$-divergence ambiguity sets. In addition, Nash equilibria for distributionally robust pricing and auction design problems with rectangular ambiguity sets can sometimes also be derived in closed form.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Nash Equilibria in DRO", "weight": 1.0} -->

We emphasize that, in contrast to the worst-case expectation problem, whose objective function is linear in the distribution ${\mathbb{Q}}$, the dual DRO problem maximizes a concave objective function representable as the pointwise infimum of infinitely many linear functions of ${\mathbb{Q}}$. This makes the dual DRO problem considerably more challenging to solve.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Nash Equilibria in DRO", "weight": 1.0} -->

In the remainder of this section, we will first identify mild regularity conditions under which the primal and dual DRO problems and are strong duals and/or admit a Nash equilibrium (Section 2.1). Next, we will show that if the reference distribution is discrete and the loss function is convex-piecewise concave, then the dual DRO problem can be reformulated as a finite convex program (Section 2.2). This reformulation will finally enable us to construct a least favorable distribution.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Existence of Nash Equilibria", "weight": 1.0} -->

The following assumption is instrumental to prove the existence of a Nash equilibrium. In the remainder of the paper we equip ${\mathcal{P}}({\mathcal{Z}})$ with the topology of weak convergence of probability distributions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 2 (Transportation cost)", "weight": 1.0} -->

There exists a metric $d(z,\hat{z})$ on ${\mathcal{Z}}$ with compact sublevel sets such that $c(z,\hat{z})\geq d^{p}(z,\hat{z})$ for some exponent $p\in{\mathbb{N}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 2 (Transportation cost)", "weight": 1.0} -->

Assumption 2. ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") will enable us to prove that the ambiguity set ${\mathbb{B}}_{\varepsilon}(\hat{{\mathbb{P}}})$ is weakly compact. We emphasize that Assumption 2. ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (ii) ‣ Assumption 2 (Transportation cost). ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") is unrestrictive and allows for transportation costs that fail to display common properties such as symmetry, convexity, homogeneity, or the triangle inequality.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Example 1 (Local Mahalanobis transportation cost)", "weight": 1.0} -->

The local Mahalanobis transportation cost is defined as $c(z,\hat{z})=\langle z-\hat{z},A(\hat{z})(z-\hat{z})\rangle$, where $A(\hat{z})$ represents a positive definite matrix for each $\hat{z}\in{\mathcal{Z}}$. This transportation cost trivially satisfies Assumption 1. ‣ 1 Introduction ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (i) ‣ Assumption 1 (Continuity assumptions). ‣ 1 Introduction ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") if $A(\hat{z})$ is continuous in $\hat{z}$. In addition, it satisfies Assumption 2. ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (i) ‣ Assumption 2 (Transportation cost).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Example 1 (Local Mahalanobis transportation cost)", "weight": 1.0} -->

‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") if the reference distribution $\hat{{\mathbb{P}}}$ has finite second moments, and it satisfies Assumption 2. ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (ii) ‣ Assumption 2 (Transportation cost).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Example 1 (Local Mahalanobis transportation cost)", "weight": 1.0} -->

‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") for $d(z,\hat{z})=\alpha\|z-\hat{z}\|_{2}$ and $p=2$ if $\alpha=\inf_{\hat{z}\in{\mathcal{Z}}}\lambda_{\min}(A(\hat{z}))>0$. However, the local Mahalanobis transportation cost fails to be symmetric.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Example 2 (Discrete metric)", "weight": 1.0} -->

If the transportation cost is identified with the (nonconvex) discrete metric $c(z,\hat{z})=\mathds{1}_{\{z\neq\hat{z}\}}$, then the optimal transport distance reduces to the total variation distance \[95, § 6\]. In this case, Assumptions 1. ‣ 1 Introduction ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (i) ‣ Assumption 1 (Continuity assumptions). ‣ 1 Introduction ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") and 2. ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (i) ‣ Assumption 2 (Transportation cost). ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") are trivially satisfied, and Assumption 2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Example 2 (Discrete metric)", "weight": 1.0} -->

‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (ii) ‣ Assumption 2 (Transportation cost). ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") holds for $d(z,\hat{z})=c(z,\hat{z})$ and for any $p\geq 1$ provided that the support set ${\mathcal{Z}}$ is compact.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 2 (Discrete metric)", "weight": 1.0} -->

The next lemma identifies minimal conditions under which ${\mathbb{B}}_{\varepsilon}(\hat{{\mathbb{P}}})$ is weakly compact. Thus, it generalizes \[100, Theorem 1\] to ambiguity sets defined in terms of general optimal transport discrepancies.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 3 (Loss function)", "weight": 1.0} -->

For any $z\in{\mathcal{Z}}$, the function $\ell(\theta,z)$ is lower semicontinuous in $\theta$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumption 3 (Loss function)", "weight": 1.0} -->

For any $\theta\in\Theta$, there are $g>0$, $\hat{z}_{0}\in{\mathcal{Z}}$ and $r\in(0,p)$ with $\ell(\theta,z)\leq g\left[1+d^{r}(z,\hat{z}_{0})\right]$ for all $z\in{\mathcal{Z}}$, where $d$ and $p$ are the metric and the exponent from Assumption 2. ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (ii) ‣ Assumption 2 (Transportation cost). ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization"), respectively.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption 3 (Loss function)", "weight": 1.0} -->

As we will see below, Assumptions 3. ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (i) ‣ Assumption 3 (Loss function). ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") and 3. ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (ii) ‣ Assumption 3 (Loss function).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Assumption 3 (Loss function)", "weight": 1.0} -->

‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") imply that ${\mathbb{E}}_{Z\sim{\mathbb{Q}}}\left[\ell(\theta,Z)\right]$ is lower semicontinuous in $\theta$, while Assumptions 1. ‣ 1 Introduction ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (ii) ‣ Assumption 1 (Continuity assumptions). ‣ 1 Introduction ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") and 3. ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (iv) ‣ Assumption 3 (Loss function).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Assumption 3 (Loss function)", "weight": 1.0} -->

‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") imply that ${\mathbb{E}}_{Z\sim{\mathbb{Q}}}\left[\ell(\theta,Z)\right]$ is weakly upper semicontinuous in ${\mathbb{Q}}$. Note that Assumption 3. ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (ii) ‣ Assumption 3 (Loss function). ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") trivially holds for non-negative loss functions. However, it also holds under the following two conditions, which are typically easy to check.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Assumption 3 (Loss function)", "weight": 1.0} -->

First, ${\mathbb{B}}_{\varepsilon}(\hat{{\mathbb{P}}})$ is contained in a $p$-th Wasserstein ball around a nominal distribution $\hat{\mathbb{P}}$ with finite $p$-th moments. This implies via \[100, Lemma 1\] that all distributions ${\mathbb{Q}}\in{\mathbb{B}}_{\varepsilon}(\hat{{\mathbb{P}}})$ have finite $p$-th moments.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Assumption 3 (Loss function)", "weight": 1.0} -->

Second, for any $\bar{\theta}\in\Theta$, there exist $g>0$, a reference point $\hat{z}_{0}\in{\mathcal{Z}}$ and a neighborhood ${\mathcal{U}}$ of $\bar{\theta}$ such that $\ell(\theta,z)\geq-g\left[1+d^{p}(z,\hat{z}_{0})\right]$ for all $\theta\in{\mathcal{U}}$ and $z\in{\mathcal{Z}}$. As for the inf-compactness condition in Assumption 3. ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (iii) ‣ Assumption 3 (Loss function).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Assumption 3 (Loss function)", "weight": 1.0} -->

‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization"), suppose that ${\mathbb{E}}_{Z\sim{\mathbb{Q}}}\left[\ell(\theta,Z)\right]$ is lower semicontinuous in $\theta$. In this case, Assumption 3. ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (iii) ‣ Assumption 3 (Loss function). ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") is trivially satisfied if $\Theta$ is compact.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Assumption 4 (Properness conditions)", "weight": 1.0} -->

Assumption 4. ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (i) ‣ Assumption 4 (Properness conditions). ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") ensures that the optimal value of the primal DRO problem is strictly smaller than $+\infty$, whereas Assumption 4. ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (ii) ‣ Assumption 4 (Properness conditions). ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") ensures that the optimal value of the dual DRO problem is strictly larger than $-\infty$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Assumption 4 (Properness conditions)", "weight": 1.0} -->

Note that any DRO problem that violates these conditions is pathological and of limited practical interest. We are now ready to state the main result of this section.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Computation of Nash Equilibria", "weight": 1.0} -->

At first sight, the dual DRO problem appears intractable as it constitutes a challenging maximin problem that maximizes the optimal value of a parametric minimization problem over an infinite-dimensional space of probability distributions. It is well known that the primal DRO problem can be reformulated as a finite convex program if the loss function $\ell(\theta,z)$, the support set ${\mathcal{Z}}$, the feasible set $\Theta$ and the transportation cost $c(z,\hat{z})$ display certain convexity properties and if the reference distribution $\hat{{\mathbb{P}}}$ is discrete; see, e.g., \[65, § 4.1\] or \[103, § 6\]. In the remainder of this section we will demonstrate that essentially the same regularity conditions also enable us to reformulate the dual DRO problem as a finite convex program. The solutions of the emerging convex programs can be used to construct a robust decision $\theta^{\star}$ and a least favorable distribution ${\mathbb{Q}}^{\star}$ that form a Nash equilibrium.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Computation of Nash Equilibria", "weight": 1.0} -->

We will now show that dual DRO problems of the form and can often be addressed with methods from convex optimization. To this end, we restrict attention to discrete reference distributions.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Assumption 5 (Discrete reference distribution)", "weight": 1.0} -->

We also need the following assumption, which constrains the shape of the transportation cost function, the loss function, the support set and the feasible set. Thus, it limits modeling flexibility.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Assumption 6 (Convexity conditions)", "weight": 1.0} -->

The transportation cost function $c(z,\hat{z})$ is lower semicontinuous in $(z,\hat{z})$ and convex in $z$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Assumption 6 (Convexity conditions)", "weight": 1.0} -->

The loss function is representable as a pointwise maximum of finitely many saddle functions, that is, we have $\ell(\theta,z)=\max_{i\in[I]}\ell_{i}(\theta,z)$ for some $I\in{\mathbb{N}}$, where $\ell_{i}(\theta,z)$ is proper, convex and lower semicontinuous in $\theta$, while $-\ell_{i}(\theta,z)$ is proper, convex and lower semicontinuous in $z$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Assumption 6 (Convexity conditions)", "weight": 1.0} -->

The support set is representable as ${\mathcal{Z}}=\{z\in{\mathbb{R}}^{d}:f_{k}(z)\leq 0~\forall k\in[K]\}$ for some $K\in{\mathbb{N}}$, where each function $f_{k}(z)$ is proper, convex and lower semicontinuous.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Assumption 6 (Convexity conditions)", "weight": 1.0} -->

The feasible set is representable as $\Theta=\{\theta\in{\mathbb{R}}^{m}:g_{l}(\theta)\leq 0~\forall l\in[L]\}$ for some $L\in{\mathbb{N}}$, where each function $g_{l}(\theta)$ is proper, convex and lower semicontinuous.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Assumption 6 (Convexity conditions)", "weight": 1.0} -->

Recall that the transportation cost function $c(z,\hat{z})$ is non-negative and satisfies the identity of indiscernibles. Together with Assumption 6. ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (i) ‣ Assumption 6 (Convexity conditions). ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization"), this immediately implies that $c(z,\hat{z})$ is proper, convex and lower semicontinuous in $z$ for every fixed $\hat{z}$ and that it is proper and lower semicontinuous in $\hat{z}$ for every fixed $z$. Assumption 6.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Assumption 6 (Convexity conditions)", "weight": 1.0} -->

‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (ii) ‣ Assumption 6 (Convexity conditions). ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") requires both $\ell_{i}(\theta,z)$ and $-\ell_{i}(\theta,z)$ to be proper, which implies that the saddle function $\ell_{i}(\theta,z)$ can adopt only finite values. However, the convex functions $f_{k}(z)$ and $g_{l}(\theta)$ introduced in Assumptions 6. ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (iii) ‣ Assumption 6 (Convexity conditions).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Assumption 6 (Convexity conditions)", "weight": 1.0} -->

‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") and 6. ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (iv) ‣ Assumption 6 (Convexity conditions). ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization"), respectively, may adopt the value $\infty$. Assumption 6. ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") has been introduced in to derive finite convex reformulations of primal DRO problems with optimal transport amiguigty sets, and it holds in many relevant applications of DRO.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Assumption 6 (Convexity conditions)", "weight": 1.0} -->

In the remainder, we adopt the following definition of a Slater point for a minimization problem.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Assumption 7 (Slater conditions)", "weight": 1.0} -->

The feasible set $\Theta$ admits a Slater point.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Assumption 7 (Slater conditions)", "weight": 1.0} -->

Assumption 7. ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") can always be enforced by slightly perturbing the problem data or by eliminating redundant constraints and decision variables; see, e.g., \[103, Example C.3\].

<!-- chunk {"id": "body-0059", "role": "body", "section": "Assumption 7 (Slater conditions)", "weight": 1.0} -->

Before addressing the dual DRO problem, we show that the primal DRO problem admits a finite convex reformulation when the above regularity conditions are satisfied. This reformulation was first derived under the simplifying assumption that $c(z,\hat{z})=\|z-\hat{z}\|$ is defined in terms of a norm on ${\mathcal{Z}}$ \[65, Theorem 4.2\] and later generalized to arbitrary convex transportation cost functions \[103, § 6\]. Proposition 2. ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") below re-derives this reformulation under the Assumptions 5. ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization"), 6.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Assumption 7 (Slater conditions)", "weight": 1.0} -->

‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") and 7. ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (i) ‣ Assumption 7 (Slater conditions). ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization"), which can be checked ex ante. In contrast, the regularity conditions used in can only be checked ex post by solving a convex program. To keep this paper self-contained, we provide a simple proof of Proposition 2. ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization"), which will also allow us to streamline the proof of Proposition 3.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Assumption 7 (Slater conditions)", "weight": 1.0} -->

‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") below.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Assumption 8", "weight": 1.0} -->

At least one of the following three conditions is satisfied: (i) ${\mathbb{E}}_{Z\sim{\mathbb{Q}}}[\ell(\theta,Z)]$ is inf-compact in $\theta\in\Theta$ for some ${\mathbb{Q}}\in{\mathbb{B}}_{\varepsilon}(\hat{\mathbb{P}})$, (ii) ${\mathcal{Z}}$ is compact or (iii) $c(z,\hat{z})$ grows superlinearly with $z$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Assumption 8", "weight": 1.0} -->

Assumption 8 is unrestrictive in practice, and we will later see that it can be further relaxed.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Assumption 9", "weight": 1.0} -->

The next theorem formalizes the above insights, thus identifying conditions under which one can compute Nash equilibra for the DRO problem by solving the finite convex programs (10. ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")) and (21. ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")).

<!-- chunk {"id": "body-0065", "role": "body", "section": "Regularization by Robustification", "weight": 1.0} -->

It is well known that many regularization schemes in statistics and machine learning admit a robustness interpretation. Apart from carrying an aesthetic appeal, such interpretations often lead to generalization bounds for the optimizers of regularized learning models. This prompts us to seek a comprehensive theory of regularization and optimal transport-based robustification that unifies various specialized results scattered across the existing literature and that rationalizes, for the first time, a broad range of higher-order variation regularization schemes. In Section 3.1 we first study the primal regularizing effects of robustification by relating the worst-case expected loss to the expected loss under the reference distribution adjusted by Lipschitz and higher-order variation regularization terms. In Section 3.2 we then study the dual regularizing effects of robustification by relating the worst-case expected loss to the expected value of a regularized (e.g., smoothed) loss function under the reference distribution.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Primal Regularizating Effects of Robustification", "weight": 1.0} -->

In this section we will show that, under natural regularity conditions, the worst-case expected loss across all distributions in a generic optimal transport-based ambiguity set is bounded above by the sum of the expected loss under the reference distribution and several regularization terms that penalize $L^{p}$-norms and Lipschitz moduli of the higher-order derivatives of the loss function. Our results generalize and unify several existing results, which have revealed intimate connections between robustification and gradient regularization, Hessian regularization and Lipschitz regularization; see also.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Primal Regularizating Effects of Robustification", "weight": 1.0} -->

The subsequent discussion focuses on the inner maximization problem, where $\theta$ is fixed. We thus temporarily suppress the dependence of the loss function on $\theta$ and use the shorthand notation $\ell(z)$ throughout this section. To exclude trivialities, we assume here that the support set ${\mathcal{Z}}$ is contained in the relative interior of the domain of $\ell(z)$. In addition, we will also adopt the following notational conventions. For any $k\in{\mathbb{Z}}_{+}$, we use $D^{k}\ell(z)$ to denote the totally symmetric tensor of all $k$-th order partial derivatives of $\ell(z)$. Accordingly, $D^{k}\ell(z)[\xi_{1},\ldots,\xi_{k}]$ stands for the directional derivative of $\ell(z)$ along the directions $\xi_{i}\in{\mathbb{R}}^{d}$ for $i\in[k]$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Primal Regularizating Effects of Robustification", "weight": 1.0} -->

If $\xi_{i}=\xi$ for all $i\in[k]$, then we use the shorthand $D^{k}\ell(z)[\xi]^{k}$. Any norm $\|\cdot\|$ on ${\mathbb{R}}^{d}$ induces a norm on the space of totally symmetric $k$-th order tensors through where the second equality follows from the symmetry of $D^{k}\ell(z)$ \[6, Satz 1\]. By slight abuse of notation, we use the same symbol $\|\cdot\|$ for the tensor norm induced by the vector norm $\|\cdot\|$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Primal Regularizating Effects of Robustification", "weight": 1.0} -->

The results of this section will depend on the following smoothness conditions.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Assumption 10 (Smoothness properties of the loss function)", "weight": 1.0} -->

The tensor $D^{k}\ell(z)$ of $k$-th order partial derivatives is Lipschitz continuous in $z$ for all $k\in[p-1]$ throughout $\operatorname{rint}(\operatorname{dom}(\ell))$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Assumption 10 (Smoothness properties of the loss function)", "weight": 1.0} -->

We are now ready to state the main result of this section.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Example 3 (Inexactness of (46a. ‣ 3.1 Primal Regularizating Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization\")))", "weight": 1.0} -->

As the nominal distribution concentrates all probability mass at the maximum of the loss function, it is clear that $\sup_{{\mathbb{Q}}\in{\mathbb{W}}_{\varepsilon}(\hat{{\mathbb{P}}})}{\mathbb{E}}_{Z\sim{\mathbb{Q}}}[\ell(Z)]=0$. To construct the upper bound in (46a.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Example 3 (Inexactness of (46a. ‣ 3.1 Primal Regularizating Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization\")))", "weight": 1.0} -->

‣ 3.1 Primal Regularizating Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")), note that $D^{1}\ell(z)=-z$ and $D^{2}\ell(z)=-1$ such that $\|D_{1}\ell(z)\|=|z|$, $\|D^{2}\ell(z)\|=1$ and $\operatorname{lip}(D^{2}\ell)=0$. As $\hat{\mathbb{P}}=\delta_{0}$, one thus readily verifies that the upper bound in (46a. ‣ 3.1 Primal Regularizating Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")) is given by $\varepsilon^{2}/2$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Example 3 (Inexactness of (46a. ‣ 3.1 Primal Regularizating Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization\")))", "weight": 1.0} -->

This upper bound is correct to first order in $\varepsilon$ but overestimates the second-order term in the Taylor expansion of the worst-case expected loss.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Example 3 (Inexactness of (46a. ‣ 3.1 Primal Regularizating Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization\")))", "weight": 1.0} -->

To conclude, we show that the results of this section generalize several bounds in the literature.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Remark 1 (Hessian regularization)", "weight": 1.0} -->

Corollary 2. ‣ 3.1 Primal Regularizating Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") generalizes \[7, Remark 10\], which establishes an upper bound on the worst-case expected loss across all distributions in a Wasserstein ball with $p>2$ and $d(z,\hat{z})=\|z-\hat{z}\|_{2}$. This bound penalizes the gradient and the Hessian of the loss function and holds only asymptotically for small $\varepsilon$. One readily verifies that this bound can be obtained from (46a.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Remark 1 (Hessian regularization)", "weight": 1.0} -->

‣ 3.1 Primal Regularizating Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")) by ignoring all terms of the order ${\mathcal{O}}(\varepsilon^{k})$ for $k>2$ and by noting that $\|D^{2}\ell(\hat{z})\|_{2}=\lambda_{\text{max}}\left(D^{2}\ell(\hat{z})\right)$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Remark 2 (Lipschitz regularization)", "weight": 1.0} -->

For $p=1$ the upper bound in (46b. ‣ 3.1 Primal Regularizating Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")) collapses to the sum of the expected loss under the reference distribution and the Lipschitz modulus of $\ell(z)$ weighted by the Wasserstein radius $\varepsilon$. This bound is exact for every $\varepsilon\geq 0$ provided that ${\mathcal{Z}}={\mathbb{R}}^{d}$ and the loss function is convex \[65, § 6.2\]. This result gives classical regularization schemes in statistics and machine learning a robustness interpretation. More generally, this bound is exact when the loss function $\ell(z)$ grows asymptotically at rate $\operatorname{lip}(\ell)$ along some recession direction of ${\mathcal{Z}}$ \[34, Corollary 2\]. Note, however, that the upper bound in (46b.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Remark 2 (Lipschitz regularization)", "weight": 1.0} -->

‣ 3.1 Primal Regularizating Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")) fails to be tight for $p>1$ even if $\ell(z)$ is convex.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Remark 2 (Lipschitz regularization)", "weight": 1.0} -->

To conclude, we re-introduce the decision variable $\theta$ and highlight the usefulness of the bounds developed in this section for solving the DRO problem. If the loss function $\ell(\theta,z)$ is nonconvex in $\theta$ and/or $z$, then it is generically hard to evaluate and to minimize the worst-case expectation exactly even if the nominal distribution is discrete. If the Lipschitz modulus of $D^{p-1}\ell$ can be evaluated in closed form, however, then the upper bound of Theorem 1. ‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") can be computed efficiently because it consists of several sample averages. In addition, this upper bound can be minimized approximately by using stochastic gradient descent-type algorithms. By Theorem 1.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Remark 2 (Lipschitz regularization)", "weight": 1.0} -->

‣ 2.1 Existence of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization"), the resulting approximate minimizers enjoy the same robustness guarantees as the exact minimizers of the nonconvex DRO problem.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Dual Regularizing Effects of Robustification", "weight": 1.0} -->

A distributionally robust learning model over linear hypotheses is a DRO problem of the form where $L:{\mathbb{R}}\to(-\infty,+\infty]$ is a univariate loss function. Thus, is a special case of with $\ell(\theta,z)=L(\langle\theta,z\rangle)$. Throughout this section we will focus on problem instead of the more general problem. Several important problems in operations research and machine learning can be framed as instances of. Examples include portfolio optimization and newsvendor problems, plain vanilla or kernelized regression and classification problems, (linear) inverse problems, and phase retrieval problems. For problem to be well-defined, we assume throughout this section that Assumption 1. ‣ 1 Introduction ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") holds. Proposition 1.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Dual Regularizing Effects of Robustification", "weight": 1.0} -->

‣ 1 Introduction ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") thus implies that the DRO problem is equivalent to the stochastic program whose objective function involves the expectation of the $c$-transform $\ell_{c}(\theta,\lambda,\hat{Z})$ under the reference distribution $\hat{{\mathbb{P}}}$. Throughout this section we also assume that ${\mathcal{Z}}={\mathbb{R}}^{d}$, and thus the $c$-transform satisfies While the conservative bound (44. ‣ 3.1 Primal Regularizating Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")) derived in Section 3.1 exposes the primal regularizing effects, the reformulation exposes the dual regularizing effects of robustification.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Dual Regularizing Effects of Robustification", "weight": 1.0} -->

Indeed, from a primal perspective, robustification essentially amounts to adding various regularization terms to the expected loss, and from a dual perspective, robustification essentially amounts to replacing the loss with its $c$-transform, which is best viewed as a regularized version of the loss function, and tuning the corresponding regularization parameter $\lambda$. The main goal of this section is to shed more light on this dual perspective on robustification. Specifically, we will show that the $c$-transform $\ell_{c}$ can often be expressed in terms of a suitable envelope of $L$ such as the Pasch-Hausdorff envelope or the Moreau envelope. In addition, we will show how the formulas and can be exploited algorithmically. Indeed, in Section 2.2 we showed that problem is equivalent to a finite convex program if all convexity conditions of Assumption 6. ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") are satisfied.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Dual Regularizing Effects of Robustification", "weight": 1.0} -->

In this section we will show that, as its objective function depends only on a one-dimensional projection of $z$, problem can sometimes be solved efficiently even if $L$ fails to be (piecewise) concave or even if $c$ fails to be convex.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Dual Regularizing Effects of Robustification", "weight": 1.0} -->

We now leverage techniques from nonconvex optimization to recast the (possibly nonconvex) problem for evaluating the $c$-transform as a univariate optimization problem.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Pasch-Hausdorff Envelope", "weight": 1.0} -->

Throughout this section we assume that all conditions of Proposition 4). ‣ 3.2 Dual Regularizing Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") hold and that $p=1$. In this case, $L_{1}(\cdot,\lambda)$ is usually called the Pasch-Hausdorff envelope of $L$. One can show that $L_{1}(\cdot,\lambda)$ coincides with the smallest $\lambda$-Lipschitz continuous majorant of $L$ or evaluates to $+\infty$ if no such majorant exists \[8, Proposition 12.17\]. Under the conditions of this section, the univariate minimizaton problem on the right hand side of. ‣ 3.2 Dual Regularizing Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")) can sometimes be solved analytically.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Pasch-Hausdorff Envelope", "weight": 1.0} -->

This allows us to recover---in a unified and simplified manner---several reformulation results from the recent literature on Wasserstein DRO.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Example 4 (Aymptotically steep Lipschitz continuous loss)", "weight": 1.0} -->

If the asymptotic linear growth rate of the loss function $L$, which is defined as $\limsup_{|s|\to\infty}L(s)/|s|$, coincides with the Lipschitz modulus of $L$, then the Pasch-Hausdorff envelope of $L$ satisfies $L_{1}(s,\lambda)=L(s)$ if $\lambda\geq\operatorname{lip}(L)$ and $L_{1}(s,\lambda)=+\infty$ otherwise. To see this, assume first that $\lambda\geq\operatorname{lip}(L)$. In that case, we have where the second inequality holds because the loss function $L$ is Lipschitz continuous with Lipschitz modulus $\operatorname{lip}(L)$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Example 4 (Aymptotically steep Lipschitz continuous loss)", "weight": 1.0} -->

If $\lambda<\operatorname{lip}(L)$, on the other hand, then we have where the second inequality holds because the asymptotic linear growth rate of $L$ coincides with $\operatorname{lip}(L)$. Hence, the objective function in the minimization problem on the right hand side of. ‣ 3.2 Dual Regularizing Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")) evaluates to $+\infty$ whenever $\lambda<\operatorname{lip}(L)$. As $\varepsilon\|\theta\|_{*}\geq 0$, we thus have $\lambda=\operatorname{lip}(L)$ at optimality, and.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Example 4 (Aymptotically steep Lipschitz continuous loss)", "weight": 1.0} -->

‣ 3.2 Dual Regularizing Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")) simplifies to Hence, the worst-case expected loss over a 1-Wasserstein ball of radius $\varepsilon$ coincides exactly with the expected loss under the reference distribution adjusted by the regularization term $\varepsilon\operatorname{lip}(L)\|\theta\|_{*}$. This result strengthens the inequality derived in Corollary 2. ‣ 3.1 Primal Regularizating Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") for $p=1$ to an equality.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Example 4 (Aymptotically steep Lipschitz continuous loss)", "weight": 1.0} -->

It was first discovered in the context of distributionally robust linear regression, where the random vector $Z=(X,Y)\in{\mathbb{R}}^{d}$ consists of a multi-dimensional input $X\in{\mathbb{R}}^{d-1}$ and a scalar output $Y\in{\mathbb{R}}$, the decision $\theta=(\theta_{x},\theta_{y})\in{\mathbb{R}}^{d}$ consists of the weight vector $\theta_{x}\in{\mathbb{R}}^{d-1}$ of a linear predictor and the constant $\theta_{y}=-1$, while the prediction loss $L(\langle\theta,Z\rangle)=L(\langle\theta_{x},X\rangle-Y)$ is determined by a Lipschitz continuous convex function $L$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Example 4 (Aymptotically steep Lipschitz continuous loss)", "weight": 1.0} -->

Note that convexity is a simple sufficient condition for the asymptotic linear growth rate of $L$ to coincide with $\operatorname{lip}(L)$. In the context of distributionally robust linear classification, where the output $Y$ is restricted to $+1$ or $-1$ and the prediction loss is given by $L(Y\langle\theta,X\rangle)$, it has further been shown that whenever the transportation cost function satisfies $c((x,y),(\hat{x},\hat{y}))=\|x-\hat{x}\|$ if $y=\hat{y}$; $=+\infty$ if $y\neq\hat{y}$, where $\|\cdot\|$ is an arbitrary norm on the input space.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Example 4 (Aymptotically steep Lipschitz continuous loss)", "weight": 1.0} -->

In this case, the output $Y$ has the same marginal under every distribution ${\mathbb{Q}}\in{\mathbb{B}}_{\varepsilon}(\hat{{\mathbb{P}}})$ as under the reference distribution $\hat{{\mathbb{P}}}$. The above identity can be derived by repeating the arguments that led to (52. ‣ 3.2.1 Pasch-Hausdorff Envelope ‣ 3.2 Dual Regularizing Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")) with obvious minor modifications. Details are omitted for brevity. The general identity (52.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Example 4 (Aymptotically steep Lipschitz continuous loss)", "weight": 1.0} -->

‣ 3.2.1 Pasch-Hausdorff Envelope ‣ 3.2 Dual Regularizing Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")) for nonconvex loss functions whose asymptotic linear growth rate coincides with their Lipschitz modulus was first established in \[34, Corollary 2\].

<!-- chunk {"id": "body-0096", "role": "body", "section": "Example 5 (Zero-one loss)", "weight": 1.0} -->

One readily verifies that the Pasch-Hausdorff envelope of the zero-one loss $L(s)=\mathds{1}_{\{s\leq 0\}}$ satisfies $L_{1}(s,\lambda)=\max\{0,1-\max\{0,\lambda s\}\}$. By Proposition 4). ‣ 3.2 Dual Regularizing Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization"), we thus have If $\Theta$ is a cone, then the scaling factor $\lambda$ can be eliminated by using the variable substitution $\theta^{\prime}\leftarrow\lambda\theta$. In this case, the DRO problem reduces a stochastic program under the reference distribution, that is, The above identity was first derived in the context of distributionally robust linear classification using recent results on ambiguous chance constraints and their relation to conditional value-at-risk constraints. Our derivation based on the Pasch-Hausdorff envelope is new and shorter.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Moreau Envelope", "weight": 1.0} -->

Throughout this section we assume that all conditions of Proposition 4). ‣ 3.2 Dual Regularizing Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") hold and that $p=2$. In this case, $L_{2}(s,\lambda)$ is termed the Moreau envelope of $L$. Under the conditions of this section, the univariate minimizaton problem on the right hand side of. ‣ 3.2 Dual Regularizing Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")) can be solved analytically in interesting special cases, which leads again to simplified derivations of existing reformulation results.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Example 6 (Quadratic loss)", "weight": 1.0} -->

The Moreau envelope of the quadratic loss function $L(s)=s^{2}$ satisfies $L_{2}(s,\lambda)=\lambda s^{2}/(\lambda-1)$ if $\lambda>1$, $L_{2}(s,\lambda)=+\infty\cdot\mathds{1}_{\{s\neq 0\}}$ if $\lambda=1$, and $L_{2}(s,\lambda)=+\infty$ if $0\leq\lambda\leq 1$. If we assume that $\hat{{\mathbb{P}}}(\langle\theta,\hat{Z}\rangle\neq 0)>0$ to rule out trivialities, then Proposition 4).

<!-- chunk {"id": "body-0099", "role": "body", "section": "Example 6 (Quadratic loss)", "weight": 1.0} -->

‣ 3.2 Dual Regularizing Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") implies that The second equality in the above expression holds because the minimization problem over $\lambda$ is solved analytically by $\lambda^{\star}=1+\sqrt{\varepsilon}\|\theta\|_{*}({\mathbb{E}}_{\hat{Z}\sim\hat{{\mathbb{P}}}}[(\langle\theta,\hat{Z}\rangle)^{2}])^{-1/2}$. This identity was first discovered in the context of distributionally robust least squares regression; see \[15, Proposition 2\].

<!-- chunk {"id": "body-0100", "role": "body", "section": "Example 7 (Zero-one loss)", "weight": 1.0} -->

The Moreau envelope of the zero-one loss $L(s)=\mathds{1}_{\{s\leq 0\}}$ is given by $L_{2}(s,\lambda)=\max\{0,1-\sqrt{\lambda}s\max\{0,\sqrt{\lambda}s\}\}$. If $\Theta$ is a cone, then, in analogy to Example 5. ‣ 3.2.1 Pasch-Hausdorff Envelope ‣ 3.2 Dual Regularizing Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization"), we can use Proposition 4). ‣ 3.2 Dual Regularizing Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") and the variable substitution $\theta^{\prime}\leftarrow\sqrt{\lambda}\theta$ to conclude that

<!-- chunk {"id": "body-0101", "role": "body", "section": "Remark 3", "weight": 1.0} -->

If the loss function in is representable as $L(\theta^{\top}z)$ for some matrix $\theta\in{\mathbb{R}}^{d\times k}$ and some proper, convex and lower semicontinuous function $L:{\mathbb{R}}^{k}\to(-\infty,+\infty]$, while $c$ is proper and lower semicontinuous, then one can proceed as in the proof of Theorem 3.11 (i) to show that In this case, $\gamma$ is no longer a scalar but ranges over ${\mathbb{R}}^{k}$. Even though nonconvex, the resulting maximization problem may still be much easier to solve than when $k\ll d$. That is, we have reformulated a high-dimensional nonconvex problem as a low-dimensional nonconvex problem. Loss functions of the type considered here arise in multi-output regression and classification.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

All linear and second-order cone programs in our experiments are implemented in Python and solved with Gurobi 10.0.0 on a $2.4$ GHz quad-core machine with $8$ GB RAM. To ensure reproducibility, all source codes are made available at

<!-- chunk {"id": "body-0103", "role": "body", "section": "Nash Equilibria", "weight": 1.0} -->

We first illustrate the computation of Nash equilibria between a statistician and nature in the context of a distributionally robust support vector machine problem. We thus assume that $Z=(X,Y)\in{\mathbb{R}}^{d}$ consists of a feature vector $X\in{\mathcal{X}}\subseteq{\mathbb{R}}^{d-1}$ and a label $Y\in{\mathcal{Y}}=\{-1,+1\}$. In addition, $\theta\in\Theta={\mathbb{R}}^{d-1}$ is the weight vector of a linear classifier, and $\ell(\theta,Z)=\max\{0,1-Y\langle\theta,X\rangle\}$ is the hinge loss function, which represents the pointwise maximum of $I=2$ saddle functions.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Nash Equilibria", "weight": 1.0} -->

In this setting, the Nash equilibrium between the statistician and nature can be computed by using the techniques that were developed in Section 2.2 and further generalized in Appendix A. Indeed, one readily verifies that Assumptions 5. ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization"), 11. ‣ Appendix A Computation of Nash Equilibria Revisited ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") and 12. ‣ Appendix A Computation of Nash Equilibria Revisited ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") hold. In addition, as we will see below, one can also show that Assumption 9 is satisfied. This implies that Nash strategies for the statistician and nature can be computed by solving the finite convex programs (70. ‣ Appendix A Computation of Nash Equilibria Revisited ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")) and (77.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Nash Equilibria", "weight": 1.0} -->

‣ Appendix A Computation of Nash Equilibria Revisited ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")), which generalize problems (10. ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")) and (21. ‣ 2.2 Computation of Nash Equilibria ‣ 2 Nash Equilibria in DRO ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")), respectively; see Theorem 5. ‣ Appendix A Computation of Nash Equilibria Revisited ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization"). Specifically, under the given assumptions about the loss and transportation cost functions as well as the reference distribution, one can show that if ${\mathcal{X}}={\mathbb{R}}^{d-1}$, then (70.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Nash Equilibria", "weight": 1.0} -->

‣ Appendix A Computation of Nash Equilibria Revisited ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")) simplifies to while problem (77. ‣ Appendix A Computation of Nash Equilibria Revisited ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization")) reduces to The following proposition shows that distributionally robust support vector machine problem under consideration admits a continuum of least favorable distributions, which represent different Nash strategies of nature. This implies that there is in fact a continuum of many different Nash equilibria.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Distributionally Robust Log-Optimal Portfolio Selection", "weight": 1.0} -->

Assume now that the components of the random vector $Z\in{\mathcal{Z}}={\mathbb{R}}^{d}$ represent the total returns of $d$ assets over the next month, say.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Distributionally Robust Log-Optimal Portfolio Selection", "weight": 1.0} -->

If the asset returns over consecutive months are serially independent and governed by the same distribution ${\mathbb{P}}\in{\mathcal{P}}({\mathcal{Z}})$ satisfying some plausible mild regularity conditions (such as ${\mathbb{P}}[Z\in{\mathbb{R}}^{d}_{++}]=1$), and if $\Theta$ represents the probability simplex in ${\mathbb{R}}^{d}$, then one can show that the constantly rebalanced portfolio $\theta\in\Theta$ that maximizes the expected log-utility ${\mathbb{E}}_{Z\sim{\mathbb{P}}}[\log(\langle\theta,Z\rangle)]$ generates more wealth than any other causal portfolio strategy with probability 1 in the long run \[27, Theorem 15.3.1\]. Unfortunately, however, the asset return distribution ${\mathbb{P}}$ is unknown in practice. It is therefore natural to study a distributionally robust problem formulation.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Distributionally Robust Log-Optimal Portfolio Selection", "weight": 1.0} -->

In contrast to, where ${\mathbb{P}}$ is assumed to be unknown except for its first- and second-order moments, we model distributional ambiguity here via an optimal transport-based ambiguity set centered at the empirical distribution $\hat{{\mathbb{P}}}=(1/J)\sum_{j\in[J]}\delta_{\,\hat{z}_{j}}$ on $J$ training samples $\hat{z}_{j}\in{\mathbb{R}}^{d}_{++}$, $j\in[J]$. Thus, we aim to solve which is an instance of with $L(s)=-\log(s)$ if $s>0$ and $L(s)=+\infty$ if $s\leq 0$.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Distributionally Robust Log-Optimal Portfolio Selection", "weight": 1.0} -->

If the transportation cost function is set to $c(z,\hat{z})=\|z-\hat{z}\|^{p}$ for some norm $\|\cdot\|$ on ${\mathbb{R}}^{d}$ and exponent $p\geq 1$, then ${\mathbb{B}}_{\varepsilon}(\hat{{\mathbb{P}}})$ reduces to the $p$-th Wasserstein ball of radius $\varepsilon^{p}$ around $\hat{{\mathbb{P}}}$. One readily verifies that any such Wasserstein ball contains distributions that assign a strictly positive mass to 0. Thus, the worst-case expected log-utility of any portfolio $\theta\in\Theta$ is unbounded from above, which implies that problem is infeasible. To ensure that problem is well-defined, the cost of moving any fixed probability mass towards 0 must tend to infinity.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Distributionally Robust Log-Optimal Portfolio Selection", "weight": 1.0} -->

This can be ensured, for example, by setting $c(z,\hat{z})=\sum_{i\in[d]}|\log(z_{i}/\hat{z}_{i}))|$ with $\operatorname{dom}(c(\cdot,\hat{z}))={\mathbb{R}}^{d}_{++}$ for every $\hat{z}\in{\mathbb{R}}^{d}_{++}$. Even though it is nonconvex in both of its arguments, this transportation cost function defines a metric on ${\mathcal{Z}}$ that gives rise to a valid optimal transport discrepancy.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Distributionally Robust Log-Optimal Portfolio Selection", "weight": 1.0} -->

Elementary calculations show that $L^{*}(s)=-1-\log(-s)$ and that $c^{*1}(s,\hat{z})=\sum_{i\in[d]}h(s_{i}\hat{z}_{i})$, where the auxiliary function $h:{\mathbb{R}}\rightarrow(-\infty,+\infty]$ is defined through $h(s)=-1-\log(-s)$ if $s<-1$, $h(s)=s$ if $-1\leq s\leq 0$ and $h(s)=+\infty$ if $s>0$. Note that the proper convex function $h$ is differentiable on its domain. By Theorem 4. ‣ 3.2 Dual Regularizing Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") (i) ‣ Theorem 4 (Nonconvex duality).

<!-- chunk {"id": "body-0113", "role": "body", "section": "Distributionally Robust Log-Optimal Portfolio Selection", "weight": 1.0} -->

‣ 3.2 Dual Regularizing Effects of Robustification ‣ 3 Regularization by Robustification ‣ Nash Equilibria, Regularization and Computation in Optimal Transport-Based Distributionally Robust Optimization") and as $\operatorname{dom}(L^{*})=(-\infty,0)$, the $c$-transform can thus be reformulated as The next proposition shows that the maximization problem in can be solved efficiently by sorting.
