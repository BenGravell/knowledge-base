<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce a distributionally robust maximum likelihood estimation model with a Wasserstein ambiguity set to infer the inverse covariance matrix of a p-dimensional Gaussian random vector from n independent samples. The proposed model minimizes the worst case (maximum) of Stein's loss across all normal reference distributions within a prescribed Wasserstein distance from the normal distribution characterized by the sample mean and the sample covariance matrix. We prove that this estimation problem is equivalent to a semidefinite program that is tractable in theory but beyond the reach of general purpose solvers for practically relevant problem dimensions p. In the absence of any prior structural information, the estimation problem has an analytical solution that is naturally interpreted as a nonlinear shrinkage estimator. Besides being invertible and well-conditioned even for p > n, the new shrinkage estimator is rotation-equivariant and preserves the order of the eigenvalues of the sample covariance matrix. These desirable properties are not imposed ad hoc but emerge naturally from the underlying distributionally robust optimization model. Finally, we develop a sequential quadratic approximation algorithm for efficiently solving the general estimation problem subject to conditional independence constraints typically encountered in Gaussian graphical models.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The covariance matrix $\Sigma ≔ {{\mathbb{E}}^{\mathbb{P}}{\lbrack{{({\xi - {{\mathbb{E}}^{\mathbb{P}}{\lbrack\xi\rbrack}}})}{({\xi - {{\mathbb{E}}^{\mathbb{P}}{\lbrack\xi\rbrack}}})}^{\top}}\rbrack}}$ of a random vector $\xi \in {\mathbb{R}}^{p}$ governed by a distribution $\mathbb{P}$ collects basic information about the spreads of all individual components and the linear dependencies among all pairs of components of $\xi$. The inverse $\Sigma^{- 1}$ of the covariance matrix is called the precision matrix. This terminology captures the intuition that a large spread reflects a low precision and vice versa.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

While the covariance matrix appears in the formulations of many problems in engineering, science and economics, it is often the precision matrix that emerges in their solutions. For example, the optimal classification rule in linear discriminant analysis, the optimal investment portfolio in Markowitz' celebrated mean-variance model or the optimal array vector of the beamforming problem in signal processing all depend on the precision matrix. Moreover, the optimal fingerprint method used to detect a multivariate climate change signal blurred by weather noise requires knowledge of the climate vector's precision matrix.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

If the distribution $\mathbb{P}$ of $\xi$ is known, then the covariance matrix $\Sigma$ and the precision matrix $\Sigma^{- 1}$ can at least principally be calculated in closed form. In practice, however, $\mathbb{P}$ is never known and only indirectly observable through $n$ independent training samples ${\hat{\xi}}_{1},\ldots,{\hat{\xi}}_{n}$ from $\mathbb{P}$. In this setting, $\Sigma$ and $\Sigma^{- 1}$ need to be estimated from the training data.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

For later convenience, $\hat{\Sigma}$ is defined here without Bessel's correction and thus constitutes a biased estimator.^11^1An elementary calculation shows that ${{\mathbb{E}}^{{\mathbb{P}}^{n}}{\lbrack\hat{\Sigma}\rbrack}} = {\frac{n - 1}{n}\Sigma}$. Moreover, as a sum of $n$ rank-$1$ matrices, $\hat{\Sigma}$ is rank deficient in the big data regime ($p > n$). In this case, $\hat{\Sigma}$ cannot be inverted to obtain a precision matrix estimator, which is often the actual quantity of interest.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

If $\xi$ follows a normal distribution with unknown mean $\mu$ and precision matrix $X \succ 0$, which we will assume throughout the rest of the paper, then the log-likelihood function of the training data can be expressed as Note that $\hat{\mathcal{L}}{(\mu,X)}$ is strictly concave in $\mu$ and $X$ \[7, Chapter 7\] and depends on the training samples only through the sample mean and the sample covariance matrix. It is clear from the last expression that $\hat{\mathcal{L}}{(\mu,X)}$ is maximized by $\mu^{\star} = \hat{\mu}$ for any fixed $X$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The maximum likelihood estimator $X^{\star}$ for the precision matrix is thus obtained by maximizing $\hat{\mathcal{L}}{(\hat{\mu},X)}$ over all $X \succ 0$, which is tantamount to solving the convex program If $\hat{\Sigma}$ is rank deficient, which necessarily happens for $p > n$, then problem is unbounded.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

If $\hat{\Sigma}$ is invertible, on the other hand, then the first-order optimality conditions can be solved analytically, showing that the minimum of problem is attained at $X^{\star} = {\hat{\Sigma}}^{- 1}$. This implies that maximum likelihood estimation under normality simply recovers the sample covariance matrix but fails to yield a precision matrix estimator for $p > n$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Adding an $\ell_{1}$-regularization term to its objective function guarantees that problem has a unique minimizer $X^{\star} \succ 0$, which constitutes a proper (invertible) precision matrix estimator. Moreover, as the $\ell_{1}$-norm represents the convex envelope of the cardinality function on the unit hypercube, the $\ell_{1}$-norm regularized maximum likelihood estimation problem promotes sparse precision matrices that encode interpretable Gaussian graphical models. Indeed, under the given normality assumption one can show that $X_{ij} = 0$ if and only if the random variables $\xi_{i}$ and $\xi_{j}$ are conditionally independent given ${\{\xi_{k}\}}_{k \notin {\{ i,j\}}}$. The sparsity pattern of the precision matrix $X$ thus captures the conditional independence structure of $\xi$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In theory, the $\ell_{1}$-norm regularized maximum likelihood estimation problem can be solved in polynomial time via modern interior point algorithms. In practice, however, scalability to high dimensions remains challenging due to the problem's semidefinite nature, and larger problem instances must be addressed with special-purpose methods such as the Newton-type QUIC algorithm.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Instead of penalizing the $\ell_{1}$-norm of the precision matrix, one may alternatively penalize its inverse $X^{- 1}$ with the goal of promoting sparsity in the covariance matrix and thus controlling the marginal independence structure of $\xi$. Despite its attractive statistical properties, this alternative model leads to a hard non-convex and non-smooth optimization problem, which can only be solved approximately.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

By the Fisher-Neyman factorization theorem, $\hat{\Sigma}$ is a sufficient statistic for the true covariance matrix $\Sigma$ of a normally distributed random vector, that is, $\hat{\Sigma}$ contains the same information about $\Sigma$ as the entire training dataset. Without any loss of generality, we may thus focus on estimators that depend on the data only through $\hat{\Sigma}$. If neither the covariance matrix $\Sigma$ nor the precision matrix $\Sigma^{- 1}$ are known to be sparse and if there is no prior information about the orientation of their eigenvectors, it is reasonable to restrict attention to rotation equivariant estimators.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

A precision matrix estimator $\hat{X}{(\hat{\Sigma})}$ is called rotation equivariant if ${\hat{X}{({R\hat{\Sigma}R^{\top}})}} = {R\hat{X}{(\hat{\Sigma})}R^{\top}}$ for any rotation matrix $R$. This definition requires that the estimator for the rotated data coincides with the rotated estimator for the original data. One can show that rotation equivariant estimators have the same eigenvectors as the sample covariance matrix (see, e.g., \[40, Lemma 5.3\] for a simple proof) and are thus uniquely determined by their eigenvalues. Hence, imposing rotation equivariance reduces the degrees of freedom from ${p{({p + 1})}}/2$ to $p$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Using an entropy loss function introduced, Stein was the first to demonstrate that superior covariance estimators in the sense of statistical decision theory can be constructed by shrinking the eigenvalues of the sample covariance matrix. Unfortunately, his proposed shrinkage transformation may alter the order of the eigenvalues and even undermine the positive semidefiniteness of the resulting estimator when $p > n$, which necessitates an ad hoc correction step involving an isotonic regression. Various refinements of this approach are reported in and the references therein, but most of these works focus on the low-dimensional case when $n \geq p$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Jensen's inequality suggests that the largest (smallest) eigenvalue of the sample covariance matrix $\hat{\Sigma}$ is biased upwards (downwards), which implies that $\hat{\Sigma}$ tends to be ill-conditioned. This effect is most pronounced for $\Sigma \approx I$. A promising shrinkage estimator for the covariance matrix is thus obtained by forming a convex combination of the sample covariance matrix and the identity matrix scaled by the average of the sample eigenvalues. If its convex weights are chosen optimally in view of the Frobenius risk, the resulting shrinkage estimator can be shown to be both well-conditioned and more accurate than $\hat{\Sigma}$. Alternative shrinkage targets include the constant correlation model, which preserves the sample variances but equalizes all pairwise correlations, the single index model, which assumes that each random variable is explained by one systematic and one idiosyncratic risk factor, or the diagonal matrix of the sample eigenvalues etc.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

The linear shrinkage estimators described above are computationally attractive because evaluating convex combinations is cheap. Computing the corresponding precision matrix estimators requires a matrix inversion and is therefore more expensive. We emphasize that linear shrinkage estimators for the precision matrix itself, obtained by forming a cheap convex combination of the inverse sample covariance matrix and a shrinkage target, are not available in the big data regime when $p > n$ and $\hat{\Sigma}$ fails to be invertible.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

More recently, insights from random matrix theory have motivated a new rotation equivariant shrinkage estimator that applies an individualized shrinkage intensity to every sample eigenvalue. While this nonlinear shrinkage estimator offers significant improvements over linear shrinkage, its evaluation necessitates the solution of a hard nonconvex optimization problem, which becomes cumbersome for large values of $p$. Alternative nonlinear shrinkage estimators can be obtained by imposing an upper bound on the condition number of the covariance matrix in the underlying maximum likelihood estimation problem.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

Alternatively, multi-factor models familiar from the arbitrage pricing theory can be used to approximate the covariance matrix by a sum of a low-rank and a diagonal component, both of which have only few free parameters and are thus easier to estimate. Such a dimensionality reduction leads to stable estimators.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper endeavors to develop a principled approach to precision matrix estimation, which is inspired by recent advances in distributionally robust optimization. For the sake of argument, assume that the true distribution of $\xi$ is given by ${\mathbb{P}} = {\mathcal{N}{(\mu_{0},\Sigma_{0})}}$, where $\Sigma_{0} \succ 0$. If $\mu_{0}$ and $\Sigma_{0}$ were known, the quality of some estimators $\mu$ and $X$ for $\mu_{0}$ and $\Sigma_{0}^{- 1}$, respectively, could conveniently be measured by Stein's loss which is reminiscent of the log-likelihood function.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is easy to verify that Stein's loss is nonnegative for all $\mu \in {\mathbb{R}}^{p}$ and $X \in {\mathbb{S}}_{+}^{p}$ and vanishes only at the true mean $\mu = \mu_{0}$ and the true precision matrix $X = \Sigma_{0}^{- 1}$. Of course, we cannot minimize Stein's loss directly because $\mathbb{P}$ is unknown. As a naïve remedy, one could instead minimize an approximation of Stein's loss obtained by removing the (unknown but irrelevant) normalization constant ${- {\log{\det\Sigma_{0}}}} - p$ and replacing $\mathbb{P}$ in with the empirical distribution ${\hat{\mathbb{P}}}_{n} = {\mathcal{N}{(\hat{\mu},\hat{\Sigma})}}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, in doing so we simply recover the standard maximum likelihood estimation problem, which is unbounded for $p > n$ and outputs the sample mean and the inverse sample covariance matrix for $p \leq n$. This motivates us to robustify the empirical loss minimization problem by exploiting that ${\hat{\mathbb{P}}}_{n}$ is close to $\mathbb{P}$ in Wasserstein distance.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Tractable Reformulation", "weight": 1.0} -->

Throughout this paper we assume that the random vector $\xi \in {\mathbb{R}}^{p}$ is normally distributed. This is in line with the common practice in statistics and in the natural and social sciences, whereby normal distributions are routinely used to model random vectors whose distributions are unknown. The normality assumption is often justified by the central limit theorem, which suggests that random vectors influenced by many small and unrelated disturbances are approximately normally distributed. Moreover, the normal distribution maximizes entropy across all distributions with given first- and second-order moments, and as such it constitutes the least prejudiced distribution compatible with a given mean vector and covariance matrix.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Tractable Reformulation", "weight": 1.0} -->

In order to facilitate rigorous statements, we first provide a formal definition of normal distributions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 2.5 (Kullback-Leibler divergence between normal distributions)", "weight": 1.0} -->

In the big data regime ($p > n$) the sample covariance matrix $\hat{\Sigma}$ is singular even if the samples are drawn from a non-degernerate normal distribution ${\mathbb{P}} = {\mathcal{N}{(\mu,\Sigma)}}$ with $\Sigma \in {\mathbb{S}}_{+ +}^{p}$. In this case, the Kullback-Leibler distance between the empirical distribution $\hat{\mathbb{P}} = {\mathcal{N}{(\hat{\mu},\hat{\Sigma})}}$ and $\mathbb{P}$ is infinite, and thus $\hat{\mathbb{P}}$ and $\mathbb{P}$ are perceived as maximally dissimilar despite their intimate relation. In contrast, their Wasserstein distance is finite.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 2.5 (Kullback-Leibler divergence between normal distributions)", "weight": 1.0} -->

In the remainder of this section we develop a tractable reformulation for the distributionally robust estimation problem. Before investigating the general problem, we first address a simpler problem variant where the true mean $\mu_{0}$ of $\xi$ is known to vanish. Thus, we temporarily assume that $\xi$ follows $\mathcal{N}{(0,\Sigma_{0})}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 2.5 (Kullback-Leibler divergence between normal distributions)", "weight": 1.0} -->

In this setting, it makes sense to focus on the modified ambiguity set $\mathcal{P}_{\rho}^{0} ≔ {\{{{\mathbb{Q}} \in \mathcal{N}_{0}^{p}}:{{{\mathbb{W}}{({\mathbb{Q}},\hat{\mathbb{P}})}} \leq \rho}\}}$, which contains all normal distributions with zero mean that have a Wasserstein distance of at most $\rho \geq 0$ from the empirical distribution $\hat{\mathbb{P}} = {\mathcal{N}{(0,\hat{\Sigma})}}$. Under these assumptions, the estimation problem thus simplifies to We are now ready to state the first main result of this section.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Analytical Solution without Sparsity Information", "weight": 1.0} -->

If we have no prior information about the precision matrix, it is natural to set $\mathcal{X} = {\mathbb{S}}_{+ +}^{p}$. In this case, the distributionally robust estimation problem can be solved in quasi-closed form.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 3.2 (Properties of $X^{\\star}$)", "weight": 1.0} -->

The optimal distributionally robust estimator $X^{\star}$ identified in Theorem 3.1. ‣ 3. Analytical Solution without Sparsity Information ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator") commutes with the sample covariance matrix $\hat{\Sigma}$ because both matrices share the same eigenbasis. Moreover, the eigenvalues of $X^{\star}$ are obtained from those of $\hat{\Sigma}$ via a nonlinear transformation that depends on the size $\rho$ of the ambiguity set. We emphasize that all eigenvalues of $X^{\star}$ are positive for every $\rho > 0$, which implies that $X^{\star}$ is invertible.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 3.2 (Properties of $X^{\\star}$)", "weight": 1.0} -->

These insights suggest that $X^{\star}$ constitutes a nonlinear shrinkage estimator, which enjoys the rotation equivariance property (when all data points are rotated by $R \in {\mathbb{R}}^{p \times p}$, then $X^{\star}$ changes to $RX^{\star}R^{\top}$).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 3.2 (Properties of $X^{\\star}$)", "weight": 1.0} -->

Theorem 3.1. ‣ 3. Analytical Solution without Sparsity Information ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator") characterizes the optimal solution of problem in quasi-closed form up to the spectral decomposition of $\hat{\Sigma}$ and the numerical solution of equation (16b. ‣ 3. Analytical Solution without Sparsity Information ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator")). By \[39, Theorem 1.1\], the eigenvalues of $\hat{\Sigma}$ can be computed to within an absolute error $\varepsilon$ in $\mathcal{O}{(p^{3})}$ arithmetic operations. Moreover, as its left-hand side is increasing in $\gamma^{\star}$, equation (16b. ‣ 3. Analytical Solution without Sparsity Information ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator")) can be solved reliably via bisection or by the Newton-Raphson method.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 3.2 (Properties of $X^{\\star}$)", "weight": 1.0} -->

The following lemma provides a priori bounds on $\gamma^{\star}$ that can be used to initialize the bisection interval.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 3.4 (Numerical stability)", "weight": 1.0} -->

If both $\gamma^{\star}$ and $\lambda_{i}$ are large numbers, then formula (16a. ‣ 3. Analytical Solution without Sparsity Information ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator")) for $x_{i}^{\star}$ becomes numerically instable. A mathematically equivalent but numerically more robust reformulation of (16a. ‣ 3. Analytical Solution without Sparsity Information ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator")) is In the following we investigate the impact of the Wasserstein radius $\rho$ on the optimal Lagrange multiplier $\gamma^{\star}$ and the corresponding optimal estimator $X^{\star}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Numerical Solution with Sparsity Information", "weight": 1.0} -->

We now investigate a more general setting where $\mathcal{X}$ may be a strict subset of ${\mathbb{S}}_{+ +}^{p}$, which captures a prescribed conditional independence structure of $\xi$. Specifically, we assume that there exists $\mathcal{E} \subseteq {\{ 1,\ldots,p\}}^{2}$ such that the random variables $\xi_{i}$ and $\xi_{j}$ are conditionally independent given $\xi_{- {\{ i,j\}}}$ for any pair ${(i,j)} \in \mathcal{E}$, where $\xi_{- {\{ i,j\}}}$ represents the truncation of the random vector $\xi$ without the components $\xi_{i}$ and $\xi_{j}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Numerical Solution with Sparsity Information", "weight": 1.0} -->

It is well known that if $\xi$ follows a normal distribution with covariance matrix $S \succ 0$ and precision matrix $X = S^{- 1}$, then $\xi_{i}$ and $\xi_{j}$ are conditionally independent given $\xi_{- {(i,j)}}$ if and only if $X_{ij} = 0$. This reasoning forms the basis of the celebrated Gaussian graphical models, see, e.g.,. Any prescribed conditional independence structure of $\xi$ can thus conveniently be captured by the feasible set We may assume without loss of generality that $\mathcal{E}$ inherits symmetry from $X$, that is, ${(i,j)} \in \mathcal{E}\Longrightarrow{(j,i)} \in \mathcal{E}$. In Section 3 we have seen that the robust maximum likelihood estimation problem admits an analytical solution when $\mathcal{E} = \varnothing$. In the general case, analytical tractability is lost.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Numerical Solution with Sparsity Information", "weight": 1.0} -->

Indeed, if $\mathcal{E} \neq \varnothing$, then even the nominal estimation problem obtained by setting $\rho = 0$ requires numerical solution. In this section we develop a Newton-type algorithm to solve in the presence of prior conditional independence information. For the sake of consistency, we will refer to the optimal solution of problem as the Wasserstein shrinkage estimator even in the presence of sparsity constraints.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 4.1 (Conditional independence information in $\\mathcal{P}_{\\rho}$)", "weight": 1.0} -->

We emphasize that our proposed estimation model accounts for the prescribed conditional independence structure only in the feasible set $\mathcal{X}$ but not in the ambiguity set $\mathcal{P}_{\rho}$. Otherwise, the ambiguity set would have to be redefined as While conceptually attractive, this new ambiguity set is empty even for some $\rho > 0$ because the inverse sample covariance matrix ${\hat{\Sigma}}^{- 1}$ violates the prescribed conditional independence relationships with probability 1.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 4.1 (Conditional independence information in $\\mathcal{P}_{\\rho}$)", "weight": 1.0} -->

Recall from Theorem 2.6. ‣ 2. Tractable Reformulation ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator") that the estimation problem is equivalent to the convex program (6. ‣ 2. Tractable Reformulation ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator")) and that the optimal value of (6. ‣ 2. Tractable Reformulation ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator")) depends continuously on $\hat{\Sigma} \in {\mathbb{S}}_{+}^{p}$. In the remainder of this section we may thus assume without much loss of generality that $\hat{\Sigma} \succ 0$. Otherwise, we can replace $\hat{\Sigma}$ with $\hat{\Sigma} + {\varepsilonI}$ for some small $\varepsilon > 0$ without significantly changing the estimation problem's solution. Inspired, we now develop a sequential quadratic approximation algorithm for solving problem (6.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 4.1 (Conditional independence information in $\\mathcal{P}_{\\rho}$)", "weight": 1.0} -->

‣ 2. Tractable Reformulation ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator")) with sparsity information. Note that the set $\mathcal{X}$ of feasible precision matrices typically fixes many entries to zero, thus reducing the effective problem dimension and making a second-order algorithm attractive even for large instances of (6. ‣ 2. Tractable Reformulation ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator")).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 4.1 (Conditional independence information in $\\mathcal{P}_{\\rho}$)", "weight": 1.0} -->

The proposed algorithm starts at $X_{0} = I$ and at some $\gamma_{0} > 1$, which are trivially feasible in (6. ‣ 2. Tractable Reformulation ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator")). In each iteration the algorithm moves from the current iterate $(X_{t},\gamma_{t})$ along a feasible descent direction, which is constructed from a quadratic approximation of the objective function of problem (6. ‣ 2. Tractable Reformulation ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator")). A judiciously chosen step size guarantees that the next iterate $(X_{t + 1},\gamma_{t + 1})$ remains feasible and has a better (lower) objective value; see Algorithm 1. The construction of the descent direction relies on the following lemma.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 4.4 (Steepest descent algorithm)", "weight": 1.0} -->

The computation of the descent direction in Proposition 4.3. ‣ 4. Numerical Solution with Sparsity Information ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator") requires second-order information. It is easy to verify that Proposition 4.3. ‣ 4. Numerical Solution with Sparsity Information ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator") remains valid if the Hessian $H$ is replaced with the identity matrix, in which case the sequential quadratic approximation algorithm reduces to the classical steepest descent algorithm \[37, Chapter 3\].

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 4.4 (Steepest descent algorithm)", "weight": 1.0} -->

The next proposition establishes that Algorithm 1 converges to the unique minimizer of problem (6. ‣ 2. Tractable Reformulation ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator")).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 4.6 (Refinements of Algorithm 1)", "weight": 1.0} -->

For large values of $p$, computing and storing the exact Hessian matrix $H$ from Proposition 4.3. ‣ 4. Numerical Solution with Sparsity Information ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator") is prohibitive. In this case, $H$ can be approximated by a low-rank matrix as in the limited-memory Broyden-Fletcher-Goldfarb-Shanno (BFGS) method without sacrificing global convergence. Alternatively, one can resort to a coordinate descent method akin to the QUIC algorithm, in which case both the global and local convergence guarantees of Proposition 4.5. ‣ 4. Numerical Solution with Sparsity Information ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator") remain valid.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Extremal Distributions", "weight": 1.0} -->

It is instructive to characterize the extremal distributions that attain the supremum in for a given sample covariance matrix $\hat{\Sigma}$ and a fixed candidate estimator $X$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

To assess the statistical and computational properties of the proposed Wasserstein shrinkage estimator, we compare it against two state-of-the-art precision matrix estimators from the literature.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 6.3 (Bessel's correction)", "weight": 1.0} -->

So far we used $\mathcal{N}{(\hat{\mu},\hat{\Sigma})}$ as the nominal distribution, where the sample covariance matrix $\hat{\Sigma}$ was identified with the (biased) maximum likelihood estimator. In practice, it is sometimes useful to use $\hat{\Sigma}/\kappa$ as the nominal covariance matrix, where $\kappa \in {}$ is a Bessel correction that removes the bias; see, e.g., Sections 6.2.1 and 6.2.2 below. Under the premise that $\mathcal{X}$ is a cone, it is easy to see that if $(X^{\star},\gamma^{\star})$ is optimal in (15.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 6.3 (Bessel's correction)", "weight": 1.0} -->

‣ 2. Tractable Reformulation ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator")) for a prescribed Wasserstein radius $\rho$ and a scaled sample covariance matrix $\hat{\Sigma}/\kappa$, then $({\kappaX^{\star}},{\kappa\gamma^{\star}})$ is optimal in (15. ‣ 2. Tractable Reformulation ‣ Distributionally Robust Inverse Covariance Estimation: The Wasserstein Shrinkage Estimator")) for a scaled Wasserstein radius $\sqrt{\kappa}\rho$ and the original sample covariance matrix $\hat{\Sigma}$. Thus, up to scaling, using a Bessel correction is tantamount to shrinking $\rho$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experiments with Synthetic Data", "weight": 1.0} -->

Consider a $({p = 20})$-variate Gaussian random vector $\xi$ with zero mean. The (unknown) true covariance matrix $\Sigma_{0}$ of $\xi$ is constructed as follows. We first choose a density parameter $d \in {\{{12.5\%},{50\%},{100\%}\}}$. Using the legacy MATLAB 5.0 uniform generator initialized with seed 0, we then generate a matrix $C \in {\mathbb{R}}^{p \times p}$ with $\lfloor{d \times p^{2}}\rfloor$ randomly selected nonzero elements, all of which represent independent Bernoulli random variables taking the values $+ 1$ or $- 1$ with equal probabilities. Finally, we set $\Sigma_{0} = {({{C^{\top}C} + {10^{- 3}I}})}^{- 1} \succ 0$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Experiments with Synthetic Data", "weight": 1.0} -->

As usual, the quality of an estimator $X^{\star}$ for the precision matrix $\Sigma_{0}^{- 1}$ is evaluated using Stein's loss function which vanishes if $X^{\star} = \Sigma_{0}^{- 1}$ and is strictly positive otherwise.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Experiments with Synthetic Data", "weight": 1.0} -->

All simulation experiments involve $100$ independent trials. In each trial, we first draw $n \in {\{ 10,20,40,60\}}$ independent samples from $\mathcal{N}{(0,\Sigma_{0})}$, which are used to compute the sample covariance matrix $\hat{\Sigma}$ and the corresponding precision matrix estimators. Figure 2 shows Stein's loss of the Wasserstein shrinkage estimator without structure information for $\rho \in {\lbrack 10^{- 2},10^{1}\rbrack}$, the linear shrinkage estimator for $\alpha \in {\lbrack 10^{- 5},10^{0}\rbrack}$ and the $\ell_{1}$-regularized maximum likelihood estimator for $\beta \in {\lbrack{5 \times 10^{- 5}},10^{0}\rbrack}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Experiments with Synthetic Data", "weight": 1.0} -->

Lines represent averages, while shaded areas capture the tubes between the empirical 20% and 80% quantiles across all $100$ trials. Note that all three estimators approach ${\hat{\Sigma}}^{- 1}$ when their respective tuning parameters tend to zero. As $\hat{\Sigma}$ is rank deficient for $n < p = 20$, Stein's loss thus diverges for small tuning parameters when $n = 10$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Experiments with Synthetic Data", "weight": 1.0} -->

The best Wasserstein shrinkage estimator in a given trial is defined as the one that minimizes Stein's loss over all $\rho \geq 0$. The best linear shrinkage and $\ell_{1}$-regularized maximum likelihood estimators are defined analogously. Figure 2 reveals that the best Wasserstein shrinkage estimators dominate the best linear shrinkage and---to a lesser extent---the best $\ell_{1}$-regularized maximum likelihood estimators in terms of Stein's loss for all considered parameter settings. The dominance is more pronounced for small sample sizes. We emphasize that Stein's loss depends explicitly on the unknown true covariance matrix $\Sigma_{0}$. Thus, Figure 2 is not available in practice, and the optimal tuning parameters $\rho^{\star}$, $\alpha^{\star}$ and $\beta^{\star}$ cannot be computed exactly. The performance of different precision matrix estimators with estimated tuning parameters will be studied in Section 6.2.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Experiments with Synthetic Data", "weight": 1.0} -->

For $d = {12.5\%}$ and $d = {50\%}$, the true precision matrix $\Sigma_{0}^{- 1}$ has many zeros, and prior knowledge of their positions could be used to improve estimator accuracy. To investigate this effect, we henceforth assume that the feasible set $\mathcal{X}$ correctly reflects a randomly selected portion of 50%, 75% or 100% of all zeros of $\Sigma_{0}^{- 1}$, while $\mathcal{X}$ contains no (neither correct nor incorrect) information about the remaining zeros. In this setting, we construct the Wasserstein shrinkage estimator by solving problem numerically.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Experiments with Synthetic Data", "weight": 1.0} -->

In the last experiment, we investigate the Wasserstein radius $\rho^{\star}$ of the best Wasserstein shrinkage estimator without sparsity information. Figure 4 visualizes the average of $\rho^{\star}$ across 100 independent trials as a function of the sample size $n$. A standard regression analysis based on the data of Figure 4 reveals that $\rho^{\star}$ converges to zero approximately as $n^{- \kappa}$ with $\kappa \approx {61\%}$ for $d = {12.5\%}$, $\kappa \approx {66\%}$ for $d = {50\%}$ and $\kappa \approx {68\%}$ for $d = {100\%}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Experiments with Real Data", "weight": 1.0} -->

We now study the properties of the Wasserstein shrinkage estimator in the context of linear discriminant analysis, portfolio selection and the inference of solar irradiation patterns.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Linear Discriminant Analysis", "weight": 1.0} -->

Linear discriminant analysis aims to predict the class $y \in \mathcal{Y}$, ${|\mathcal{Y}|} < \infty$, of a feature vector $z \in {\mathbb{R}}^{p}$ under the assumption that the conditional distribution of $z$ given $y$ is normal with a class-dependent mean $\mu_{y} \in {\mathbb{R}}^{p}$ and class-independent covariance matrix $\Sigma_{0} \in {\mathbb{S}}_{+ +}^{p}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Linear Discriminant Analysis", "weight": 1.0} -->

If all $\mu_{y}$ and $\Sigma_{0}$ are known, the maximum likelihood classifier $\mathcal{C}:{{\mathbb{R}}^{p}\rightarrow\mathcal{Y}}$ assigns $z$ to a class that maximizes the likelihood of observing $y$, that is, In practice, however, the conditional moments are typically unknown and must be inferred from finitely many training samples $({\hat{z}}_{i},{\hat{y}}_{i})$, $i \leq n$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Linear Discriminant Analysis", "weight": 1.0} -->

Accounting for Bessel's correction, the conditional distribution of ${\hat{\xi}}_{i}$ given ${\hat{y}}_{i}$ is normal with mean 0 and covariance matrix ${({{|\mathcal{I}_{{\hat{y}}_{i}}|} - 1})}{|\mathcal{I}_{{\hat{y}}_{i}}|}^{- 1}\Sigma_{0}$. The marginal distribution of ${\hat{\xi}}_{i}$ thus constitutes a mixture of $|\mathcal{Y}|$ normal distributions with mean 0, all of which share the same covariance matrix up to a scaling factor close to unity. As such, the residuals fail to be normally distributed. Moreover, due to their dependence on the sample means, the residuals are correlated. However, if each class accommodates many training samples, then the residuals can approximately be regarded as independent samples from $\mathcal{N}{(0,\Sigma_{0})}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Linear Discriminant Analysis", "weight": 1.0} -->

Irrespective of these complications, the sample covariance matrix provides an unbiased estimator for $\Sigma_{0}$. Indeed, by the law of total expectation we have where $\mathbb{P}$ stands for the unknown true joint distribution of the residuals and class labels. In a data-driven setting, the ideal maximum likelihood classifier is replaced with which depends on the raw data through the sample averages ${\hat{\mu}}_{y}$, $y \in \mathcal{Y}$, and some precision matrix estimator $X^{\star}$. The possible choices for $X^{\star}$ include the Wasserstein shrinkage estimator without prior information, the linear shrinkage estimator and the $\ell_{1}$-regularized maximum likelihood estimator, all of which depend on the data merely through $\hat{\Sigma}$. Note that the naïve precision matrix estimator ${\hat{\Sigma}}^{- 1}$ exists only for $n > p$ and is therefore disregarded.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Linear Discriminant Analysis", "weight": 1.0} -->

All estimators depend on a scalar parameter (the Wasserstein radius $\rho$, the mixing parameter $\alpha$ or the penalty parameter $\beta$) that can be used to tune the performance of the classifier.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Linear Discriminant Analysis", "weight": 1.0} -->

We test the classifier equipped with different estimators $X^{\star}$ on two preprocessed datasets: The "colon cancer" dataset contains 62 gene expression profiles, each of which involves 2,000 features and is classified either as normal tissue (NT) or tumor-affected tissue (TT). The data is split into a training dataset of 29 observations (9 in class NT and 20 in class TT) and a test dataset of 33 observations (13 in class NT and 20 in class TT).

<!-- chunk {"id": "body-0062", "role": "body", "section": "Linear Discriminant Analysis", "weight": 1.0} -->

The "leukemia" dataset contains 72 gene expression profiles, each of which involves 3,571 features and is classified either as acute lymphocytic leukemia (ALL) or acute myeloid leukemia (AML). The data is split into a training dataset of 38 observations (27 in class ALL and 11 in class AML) and a test dataset of 34 observations (20 in class ALL and 14 in class AML).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Linear Discriminant Analysis", "weight": 1.0} -->

Classification is based solely on the first $p \in {\{ 20,40,80,100\}}$ features of each gene expression profile. We use leave-one-out cross validation on the training data to tune the precision matrix estimator $X^{\star}$ with the goal to maximize the correct classification rate of the classifier. To keep the computational overhead manageable, we optimize the tuning parameters over the finite search grids We highlight that, in case of the $\ell_{1}$-regularized maximum likelihood estimator, cross validation becomes computationally prohibitive for $p > 80$ even if the state-of-the-art QUIC routine is used to solve the underlying semidefinite programs. In contrast, the Wasserstein and linear shrinkage estimators can be computed and tuned quickly even for $p \gg 100$. Once the optimal tuning parameters are found, we fix them and recalculate $X^{\star}$ on the basis of the entire training dataset. Finally, we substitute the resulting precision matrix estimator into the classifier and evaluate its correct classification rate on the test dataset.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Linear Discriminant Analysis", "weight": 1.0} -->

The test results are reported in Table 1. We observe that the Wasserstein shrinkage estimator frequently outperforms the linear shrinkage and $\ell_{1}$-regularized maximum likelihood estimators, especially for higher values of $p$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Linear Discriminant Analysis", "weight": 1.0} -->

Colon cancer dataset Leukemia dataset \bigstrut Table 1. Correct classification rate of the classifier instantiated with different precision matrix estimators. The best result in each experiment is highlighted in bold.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Minimum Variance Portfolio Selection", "weight": 1.0} -->

Consider the minimum variance portfolio selection problem without short sale constraints where the portfolio vector $w \in {\mathbb{R}}^{p}$ captures the percentage weights of initial capital allocated to $p$ different assets with random returns, $\mathbb{1} \in {\mathbb{R}}^{p}$ stands for the vector of ones, and $\Sigma_{0} \in {\mathbb{S}}_{+ +}^{p}$ denotes the covariance matrix of the asset returns. The objective represents the variance of the portfolio return, which is strictly convex in $w$ thanks to the positive definiteness of $\Sigma_{0}$. The unique optimal solution of this portfolio selection problem is given by $w^{\star} = {{{\Sigma_{0}^{- 1}\mathbb{1}}/\mathbb{1}^{\top}}\Sigma_{0}^{- 1}\mathbb{1}}$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Minimum Variance Portfolio Selection", "weight": 1.0} -->

A vast body of literature in finance focuses on finding accurate precision matrix estimators for portfolio construction, see, e.g.,. In the following we compare the minimum variance portfolios based on the Wasserstein shrinkage estimator without structural information, the linear shrinkage estimator and $\ell_{1}$-regularized maximum likelihood estimator on two preprocessed datasets from the Fama-French online data library:^22^2See the "48 industry portfolios" dataset and the "100 portfolios formed on size and book-to-market" dataset (FF100). Recall that the estimators depend on the data only through the sample covariance matrix $\hat{\Sigma}$, which is computed from the residual returns relative to the sample means and thus needs to account for Bessel's correction. The datasets both consist of monthly returns for the period from January 1996 to December 2016. The first 120 observations from January 1996 to December 2005 serve as the training dataset.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Minimum Variance Portfolio Selection", "weight": 1.0} -->

The optimal tuning parameters that minimize the portfolio variance are estimated via leave-one-out cross validation on the training dataset using the finite search grids The out-of-sample performance of the minimum variance portfolio corresponding to a particular precision matrix estimator is then evaluated using the rolling horizon method over the period from January 2006 to December 2016, where the sample covariance matrix needed as an input for the precision matrix is re-estimated every three months based on the most recent 120 observations (10 years), while the tuning parameter is kept fixed. The resulting out-of-sample mean, standard deviation and Sharpe ratio of the portfolio return are reported in Table 2. While the $\ell_{1}$-regularized maximum likelihood estimator yields the portfolio with the lowest standard deviation for both datasets, the Wasserstein shrinkage estimator always generates the highest mean and, maybe surprisingly, the highest Sharpe ratio.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Minimum Variance Portfolio Selection", "weight": 1.0} -->

Table 2. Standard deviation, mean and Sharpe ratio of the minimum variance portfolio based on different estimators. The best result in each experiment is highlighted in bold.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Inference of Solar Irradiation Patterns", "weight": 1.0} -->

In the last experiment we aim to estimate the spatial distribution of solar irradiation in Switzerland using the "surface incoming shortwave radiation" (SIS) data provided by MeteoSwiss.^33^3See The SIS data captures the horizontal solar irradiation intensities in $\text{W/m}^{2}$ for pixels of size 1.6km by 2.3km based on the effective cloud albedo, which is derived from satellite imagery. The dataset spans 13 years from 2004 to 2016, with a total number of 4,749 daily observations. We deseasonalize the time series of each pixel as follows. First, we divide the original time series by a shifted sinusoid with a yearly period, whose baseline level, phase and amplitude are estimated via ordinary least squares regression. Next, we subtract unity. The resulting deseasonalized time series is viewed as the sample path of a zero mean Gaussian noise process. This approach relies on the assumption that the mean and the standard deviation of the original time series share the same seasonality pattern.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Inference of Solar Irradiation Patterns", "weight": 1.0} -->

It remains to estimate the joint distribution of the pixel-wise Gaussian white noise processes, which is fully determined by the precision matrix of the deseasonalized data. We estimate the precision matrix using the Wasserstein shrinkage, linear shrinkage and $\ell_{1}$-regularized maximum likelihood estimators. As each pixel represents a geographical location and as the solar irradiation intensities at two distant pixels are likely to be conditionally independent given the intensities at all other pixels, it is reasonable to assume that the precision matrix is sparse; see also. Specifically, we assume here that the solar irradiation intensities at two pixels indexed by $(i,j)$ and $(i',j')$ are conditionally independent and that the corresponding entry of the precision matrix vanishes whenever ${{|{i - i'}|} + {|{j - j'}|}} > 3$. This sparsity information can be used to enhance the basic Wasserstein shrinkage estimator.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Inference of Solar Irradiation Patterns", "weight": 1.0} -->

Consider now the Diablerets region of Switzerland, which is described by a spatial matrix of 20$\times$`<!-- -->`{=html}20 pixels. Thus, the corresponding precision matrix has dimension 400$\times$`<!-- -->`{=html}400. The average daily solar irradiation intensities within the region of interest are visualized in Figure 5. We note that the sunshine exposure is highly variable due to the heterogeneous geographical terrain characterized by a high mountain range in the south intertwined with deep valleys in the north. In order to assess the quality of a specific precision matrix estimator, we use $K$-fold cross validation with $K = 13$. The $k$-th fold comprises all observations of year $k$ and is used to construct the estimator $X_{k}^{\star}$. The data of the remaining 12 years, without year $k$, are used to compute the empirical covariance matrix ${\hat{\Sigma}}_{- k}$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Inference of Solar Irradiation Patterns", "weight": 1.0} -->

The estimation error of $X_{k}^{\star}$ is then measured via Stein's loss We emphasize that here, in contrast to the experiment with synthetic data, ${\hat{\Sigma}}_{- k}$ is used as a proxy for the unknown true covariance matrix $\Sigma$. Figure 6 shows Stein's loss of the Wasserstein shrinkage estimator with and without structure information for $\rho \in {\lbrack 10^{- 2},10^{0}\rbrack}$, the linear shrinkage estimator for $\alpha \in {\lbrack 10^{- 3},{2 \times 10^{- 2}}\rbrack}$ and the $\ell_{1}$-regularized maximum likelihood estimator for $\beta \in {\lbrack 10^{- 5},10^{- 3}\rbrack}$. Lines represent averages, while shaded areas capture the tubes between the best- and worst-case loss realizations across all $K$ folds.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Inference of Solar Irradiation Patterns", "weight": 1.0} -->

The Wasserstein shrinkage estimator with structure information reduces the minimum average loss by 13.5% relative to the state-of-the-art $\ell_{1}$-regularized maximum likelihood estimator. Moreover, the average runtimes for computing the different estimators amount to 51.84s for the Wasserstein shrinkage estimator with structural information (Algorithm 1), 0.08s for the Wasserstein shrinkage estimator without structural information (analytical formula and bisection algorithm), 0.01s for the linear shrinkage estimator (analytical formula) and 1493.61s for the $\ell_{1}$-regularized maximum likelihood estimator (QUIC algorithm ).
