<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Comparison Theorems for the Minimum Eigenvalue of a Random Positive-semidefinite Matrix

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper establishes a new comparison principle for the minimum eigenvalue of a sum of independent random positive-semidefinite matrices. The principle states that the minimum eigenvalue of the matrix sum is controlled by the minimum eigenvalue of a Gaussian random matrix that inherits its statistics from the summands. This methodology is powerful because of the vast arsenal of tools for treating Gaussian random matrices. As applications, the paper presents short, conceptual proofs of some old and new results in high-dimensional statistics. It also settles a long-standing open question in computational linear algebra about the injectivity properties of very sparse random matrices.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

This paper establishes a new comparison principle for the minimum eigenvalue of a sum of independent random positive-semidefinite matrices. The principle states that the minimum eigenvalue of the matrix sum is controlled by the minimum eigenvalue of a Gaussian random matrix that inherits its statistics from the summands. This methodology is powerful because of the vast arsenal of tools for treating Gaussian random matrices. As applications, the paper presents short, conceptual proofs of some old and new results in high-dimensional statistics. It also settles a long-standing open question in computational linear algebra about the injectivity properties of very sparse random matrices.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Motivation", "weight": 1.0} -->

psd) matrices appear throughout high-dimensional statistics and high-dimensional probability. In particular, random psd matrices model the sample covariance of a random vector, and they capture properties of random linear embeddings. For a psd matrix, the minimum eigenvalue provides a quantitative measure of invertibility, so it is often the crucial statistic of these random matrix models. This paper introduces a new technique for studying the minimum eigenvalue of a random psd matrix by establishing a comparison with the minimum eigenvalue of a Gaussian random matrix. It also showcases several applications of this

<!-- chunk {"id": "body-0005", "role": "body", "section": "Intuition: Positive random walks", "weight": 1.0} -->

Consider a random walk on the real line that can only move in the positive direction. What is the probability that the random walk remains close to its origin? This event occurs only when allof the increments are small, which is very unlikely. We can capture this insight with a standard probability inequality that is the starting point for our investigation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Intuition: Positive random walks", "weight": 1.0} -->

To model the positive random walk, we introduce nonnegative real random variables that are independent and identically distributed (iid): \quad\text{where the $W_i$ are iid copies of $W \geq 0$.}$$ When the increment $W$ has two moments, we can compare the moment generating function (mgf) for the lower tail of the positive sum $Y$ with the mgf of a Gaussian real random variable. For all $\theta \geq 0$, $$\Expect[\econst^{-\theta Y}] \leq \Expect[\econst^{- \theta Z}] \quad\text{where}\quad Z \sim \normal_{\R}\left(n \cdot \Expect[W],\ n \cdot \Expect[W^2] \right).$$ See sec:scalar-pf for a proof of[eqn:intro-scalar-mgf].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Intuition: Positive random walks", "weight": 1.0} -->

The mgf bound leads to a classic inequality for the lower tail: $$\Prob{ Y \leq \Expect[Z] - t } \leq \quad\text{for $t \in $.} In other words, the lower tail of the positive sum $Y$ is related to the lower tail of a matching Gaussian random variable $Z$ that inherits its statistics from the summand $W$. See fig:comparison-1dfor an illustration.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Intuition: Positive random walks", "weight": 1.0} -->

(Positive sum: Comparison). These plots illustrate the distribution $Y$ of an iid sum of nonnegative real random variables (black line), along with the matching Gaussian distribution $Z$ (dashed blue), described byeqn:intro-scalar-mgf, and the tail bound (dotted red), described byeqn:intro-scalar-tail. The left-hand panel shows the densities; the right-hand panel shows the cumulative distributions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Random psd matrices", "weight": 1.0} -->

This paper demonstrates that the same phenomena persist in the matrix setting.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Random psd matrices", "weight": 1.0} -->

Consider a sum of iid random psd matrices, either real or complex: $$\mtx{Y} = \sum_{i=1}^n \mtx{W}_i \quad\text{where the $\mtx{W}_i$ are iid copies of a random psd matrix $\mtx{W}$.}$$ The minimum eigenvalue $\lambda_{\min}(\mtx{Y})$ can be expressed as the minimum of a family of iid positive sums: $$\lambda_{\min}(\mtx{Y}) = \min\nolimits_{\norm{\vct{u}} = 1} \sum_{i=1}^n \vct{u}^* \mtx{W}_i \vct{u}.$$ For each direction $\vct{u}$, the sum in[eqn:iid-psd-sum-rayleigh] is very unlikely to be zero because of[eqn:intro-scalar-tail].

<!-- chunk {"id": "body-0011", "role": "body", "section": "Random psd matrices", "weight": 1.0} -->

On the other hand, the random summands $\mtx{W}_i$ must cover every direction $\vct{u}$ before the minimum eigenvalue $\lambda_{\min}(\mtx{Y})$is strictly positive. It is not clear which of these two opposing principles prevails.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Random psd matrices", "weight": 1.0} -->

To resolve this dilemma, we adapt the strategy behind the scalar inequality [eqn:intro-scalar-tail] to the matrix setting.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Random psd matrices", "weight": 1.0} -->

Construct a self-adjoint Gaussian random matrix $\mtx{Z}$ that inherits its statistics from the summands: \Expect[\mtx{Z}] &= n \cdot \Expect[\mtx{W}]; \\\Var[\trace[\mtx{MZ}]] &= n \cdot \Expect[\abssq{\trace[\mtx{MW}]}] \quad\text{for all self-adjoint $\mtx{M}$.} Inspired by[eqn:intro-scalar-mgf], we will establish a comparison between the trace mgfs of the two random matrices: $$\Expect[\trace \econst^{-\theta \mtx{Y}}] \leq 2 \Expect[\trace \econst^{-\theta \mtx{Z}}] \quad\text{for all $\theta \geq 0$.}$$ fig:comparison-2d illustrates the comparison.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Random psd matrices", "weight": 1.0} -->

While the scalar case[eqn:intro-scalar-mgf] is easy, the matrix inequality[eqn:intro-matrix-mgf] relies on a deep fact from matrix analysis called Stahl's theorem, formerly the BMV conjecture[:Proof-BMV].

<!-- chunk {"id": "body-0015", "role": "body", "section": "Random psd matrices", "weight": 1.0} -->

Using standard methods from the trace inequality[eqn:intro-matrix-mgf] leads to a probabilistic comparison for the minimum eigenvalues: $$\Prob{ \lambda_{\min}(\mtx{Y}) \geq \Expect[\lambda_{\min}(\mtx{Z})] - t } \leq 2d \cdot \econst^{-t^2 / (2 \sigma_*^2(\mtx{Z}))},$$ where $d$ is the matrix dimension. The weak variance $\sigma_*^2(\mtx{Z}) \coloneqq \max_{\norm{\vct{u}}=1} \Var[\vct{u}^* \mtx{Z} \vct{u}]$ controls the variance of $\lambda_{\min}(\mtx{Z})$. The result[eqn:intro-matrix-tail] is powerful enough to yield sharp, dimension-free bounds for the minimum eigenvalue of some models.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Random psd matrices", "weight": 1.0} -->

Seethm:iid-intro for the full statement of the comparison.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Random psd matrices", "weight": 1.0} -->

To analyze the minimum eigenvalue $\lambda_{\min}(\mtx{Z})$ of the Gaussian matrix in[eqn:intro-matrix-tail], we have a bristling armamentarium of techniques at our disposal. This methodology leads to short, conceptual proofs of several important results from high-dimensional statistics (sec:scov). It also addresses a vexing open question from computational linear algebra about very sparse random matrices (sec:subspace-inj).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Random psd matrices", "weight": 1.0} -->

(Bivariate positive sum: Comparison). This figure illustrates the Gaussian comparisoneqn:intro-matrix-comp for a $2 \times 2$ diagonal random matrix $\mtx{W}$ with independent entries. The bivariate distribution of a pair of independent positive sums. The distribution of the matching Gaussian model. Bivariate cumulative distribution functions. Brighter colors correspond to higher probabilities. The Gaussian comparison is valid southwest of the expectation (white lines). More precisely, the comparison concerns the minimum of the two coordinates, whose distribution looks similar to the univariate case (fig:comparison-1d).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Roadmap", "weight": 1.0} -->

sec:main-results states two comparison theorems and discusses related work. sec:gaussians provides background on Gaussian random matrices that aids in the analysis of the comparison model. sec:designs,sec:scov,sec:subspace-inj apply the main results to several examples. sec:scalar-pf details a proof of[eqn:intro-scalar-tail] that generalizes to matrices. Last, sec:psd-weights,sec:iid establish the main results, including[eqn:intro-matrix-mgf] and[eqn:intro-matrix-tail].

<!-- chunk {"id": "body-0020", "role": "body", "section": "Main results and related work", "weight": 1.0} -->

This section states our two main comparison theorems. The first concerns the sum of psd matrices with random weights.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Main results and related work", "weight": 1.0} -->

The second theorem concerns a sum of iid random psd matrices described in sec:intro-random-psd. Afterward, we present a simple first example, and we discuss some related work.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Gaussian comparison: Randomly weighted sum of psd matrices", "weight": 1.0} -->

The first result treats a random matrix model where we randomly weight the terms in a sum of fixed psd matrices.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Gaussian comparison: Randomly weighted sum of psd matrices", "weight": 1.0} -->

Fix a system of psd matrices $(\mtx{A}_1, \dots, \mtx{A}_n)$, real or complex, with common dimension $d$. Consider an independent family $(W_1, \dots, W_n)$ of nonnegative real random variables with two finite moments: $W_i \geq 0$ and $\Expect[W_i^2] < +\infty$. Define the random matrices \mtx{Y} &= \sum_{i=1}^n W_i \mtx{A}_i; \\&&\text{where $X_i \sim \normal_{\R}(\Expect[W_i], \ \Expect[W_i^2])$ are \hilite{independent}.} Then there is a stochastic comparison between the minimum eigenvalues of $\mtx{Y}$ and $\mtx{Z}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Gaussian comparison: Randomly weighted sum of psd matrices", "weight": 1.0} -->

The short argument employs tools from Stein's method[:Fundamentals-Steins,:Normal-Approximation]; it also relies on Stahl's theorem[:Proof-BMV]. The weak variance $\sigma_*^2(\mtx{Z})$ arises from Gaussian concentration[:Concentration-Inequalities] for the minimum eigenvalue; seefact:gauss-lip.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Gaussian comparison: Randomly weighted sum of psd matrices", "weight": 1.0} -->

A valuable feature of thm:sampling-intro is that the psd coefficient matrices $\mtx{A}_i$ are arbitrary, and the random weights $W_i$ can have different distributions. Of particular interest is the case where $W_i \sim \bernoulli(p_i)$, which models a random sample from a family of fixed psd matrices. Compare the construction of the Gaussian comparison model[eqn:sampling-comp] with the scalar case outlined in[eqn:intro-scalar-mgf]. sec:designs applies thm:sampling-intro to the geometric problem of sampling from a complex projective design. This result complements Rudelson's theorem[:Random-Vectors]on sampling from

<!-- chunk {"id": "body-0026", "role": "body", "section": "Second moments and Gaussians", "weight": 1.0} -->

To state our next result compactly, we introduce notation that describes the second moments of a random matrix model.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Second moments and Gaussians", "weight": 1.0} -->

Let $\mtx{X} \in\Sym_d$ be a random self-adjoint matrix. Define the second moment function and the variance function of the random matrix: \Mo[\mtx{X}](\mtx{M}) &\coloneqq \Expect{} \abssq{\ip{\mtx{M}}{\mtx{X}}} = \Expect[(\trace[\mtx{MX}])^2], \\\Varo[\mtx{X}](\mtx{M}) &\coloneqq \Var[\ip{\mtx{M}}{\mtx{X}}] = \Var[\trace[\mtx{MX}]] \qquad\text{for \hilite{self-adjoint} $\mtx{M} \in \Sym_d$.}$$ These functions pack up the second-order statistics of the linear marginals of the random matrix.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Second moments and Gaussians", "weight": 1.0} -->

Recall that a (real or complex) random matrix is and only if the real and imaginary parts of the entries compose a jointly Gaussian family of real random variables; A self-adjoint Gaussian matrix $\mtx{Z} \in \Sym_d$ is uniquely determined by its expectation $\Expect[\mtx{Z}]$ and variance function $\Varo[\mtx{Z}]$. Given a self-adjoint matrix $\mtx{\Delta} \in \Sym_d$ and a positive quadratic form $\mathsf{V}: \Sym_d \to \R_+$, we write $\normal(\mtx{\Delta}, \mathsf{V})$ for the unique Gaussian distribution on self-adjoint matrices with expectation $\mtx{\Delta}$ and variance function $\mathsf{V}$. For more background on Gaussian random matrices, see sec:gaussians.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Gaussian comparison: Sum of iid psd random matrices", "weight": 1.0} -->

Our second result provides a Gaussian comparison for a sum of iid random psd matrices, the model described in the introduction.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Gaussian comparison: Sum of iid psd random matrices", "weight": 1.0} -->

Let $\mtx{W}$ be a random psd matrix, real or complex, with dimension $d$ and with two finite moments: $\Expect \norm{\mtx{W}}^2 < + \infty$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Gaussian comparison: Sum of iid psd random matrices", "weight": 1.0} -->

Consider any self-adjoint Gaussian matrix $\mtx{X}$ with dimension $d$ whose first- and second-order statistics satisfy $$\Expect[\mtx{X}] = \Expect[\mtx{W}] \quad\text{and}\quad \Varo[\mtx{X}] \geq \Mo[\mtx{W}].$$ For a natural number $n \in \N$, define the random matrices &&\text{where $\mtx{W}_i \sim \mtx{W}$ iid;} \\&&\text{where $\mtx{Z}_i \sim \mtx{X}$ iid.}% Then there is a stochastic comparison between the minimum eigenvalues of $\mtx{Y}$ and $\mtx{Z}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Gaussian comparison: Sum of iid psd random matrices", "weight": 1.0} -->

is a (nontrivial) corollary of thm:sampling-intro. For the proof, the strategy is to draw a sample from the distribution of the summand $\mtx{W}$ and to approximate the iid sum $\mtx{Y}$ by extracting a subsample. Seesec:iidfor the grisly details.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Gaussian comparison: Sum of iid psd random matrices", "weight": 1.0} -->

Let us expand on the difference between the two comparison theorems. thm:sampling-intro forces the summands to take the simple form $W_i \mtx{A}_i$, each summand has its own distribution. In contrast, thm:iid-intro comprehends a general distribution $\mtx{W}$, but it requires the summands to be identical copies of $\mtx{W}$. We permit inequality in the comparison[eqn:iid-intro-match] to facilitate the application of the result.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Gaussian comparison: Sum of iid psd random matrices", "weight": 1.0} -->

The Gaussian comparison model[eqn:iid-comp] for the sum $\mtx{Y}$ can also be written in the form $$\mtx{Z} = n \cdot (\Expect \mtx{X}) + \sqrt{n} \cdot (\mtx{X} - \Expect \mtx{X}) \sim \normal(n \cdot \Expect[\mtx{X}],\ n \cdot \Varo[\mtx{X}]).$$ The statement[eqn:iid-comp-simple] follows from the stability properties of the Gaussian. Compare with[eqn:intro-scalar-mgf]. thm:iid-intro supports many applications. As a first example, sec:wishart provides a bound for the minimum eigenvalue of a Wishart matrix. sec:scov develops some old and new results on the minimum eigenvalue of a sample covariance matrix.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Gaussian comparison: Sum of iid psd random matrices", "weight": 1.0} -->

sec:subspace-injstudies random linear embeddings, and it resolves a recalcitrant problem on the injectivity properties of very sparse random matrices.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Gaussian comparison: Sum of iid psd random matrices", "weight": 1.0} -->

It is natural to conjecture a comparison between the random matrices \mtx{Y} &= \sum_{i=1}^n \mtx{W}_i && \text{where $\mtx{W}_i$ are psd and independent;} \\\mtx{Z} &= \sum_{i=1}^n \mtx{X}_i && \text{where $\mtx{X}_i \sim \normal(\Expect[\mtx{W}_i],\ \Mo[\mtx{W}_i])$ are independent.} In this setting, we were only able to establish weak variants of[eqn:intro-thm-iid-expect] and[eqn:intro-thm-iid-tail], but we believe that similar statements should remain valid.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Example: Wishart matrix", "weight": 1.0} -->

As a first example, we treat the minimum eigenvalue of a standard real Wishart matrix[:Aspects-Multivariate]. Introduce the random, rank-one psd matrix $$\mtx{W} = \vct{gg}^\transp \in \Sym_d(\R) \quad\text{where $\vct{g} \sim \normal_{\R}(\vct{0}, \Id_d)$.}$$ Draw independent copies $\mtx{W}_1, \dots, \mtx{W}_n$ of the random matrix $\mtx{W}$, and form the sum: \mtx{Y} = \sum_{i=1}^n \mtx{W}_i \sim \textsc{wishart}_{\R}(\Id_d, n).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Example: Wishart matrix", "weight": 1.0} -->

%$$ After a calculation of the first and second moments of $\mtx{W}$, thm:iid-intro furnishes a comparison between the Wishart matrix $\mtx{Y}$ and the Gaussian matrix $$\mtx{Z} = n \cdot \Id_d + \gamma \sqrt{n} \cdot \Id_d + \sqrt{n} \cdot \mtx{G}_{\goe} \in \Sym_d(\R),$$ where $\gamma \sim \normal_{\R}$ and $\mtx{G}_{\goe}$ is drawn independently from the (unnormalized) Gaussian orthogonal ensemble (GOE); seesec:goe for details.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Example: Wishart matrix", "weight": 1.0} -->

Exploiting standard facts about the GOE matrix[:Alice-Bob], we find that the minimum eigenvalue and the weak variance satisfy $$\Expect \lambda_{\min}(\mtx{Z}) \geq n - 2 \sqrt{dn} \qquad\text{and}\qquad \sigma_{*}^2(\mtx{Z}) \leq 3n.$$ Therefore, thm:iid-intro yields the explicit, nonasymptotic bound $$\Expect \lambda_{\min}(\mtx{Y}) \geq n - 2\sqrt{dn} - \sqrt{6 n \log(2d)}.$$ The bound is nontrivial when $n \geq \big(2 \sqrt{d} + \sqrt{6 \log(2d)} \big)^2$. In particular, it suffices that $n \gtrsim d$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example: Wishart matrix", "weight": 1.0} -->

How tight is the inequality [eqn:wishart-nonasymp]? Rescale by the number $n$ of samples, and introduce the aspect ratio $\varrho \coloneq d/n \in (0,1]$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example: Wishart matrix", "weight": 1.0} -->

When $d, n \to \infty$ with the ratio $\varrho$ fixed, we determine that $$\Expect \lambda_{\min}(n^{-1} \mtx{Y}) \geq 1 - 2 \sqrt{ \varrho } - \sqrt{6 \log (2d) / n} In this regime, the sharp asymptotic[:Limit-Smallest] is $$\lambda_{\min}(n^{-1} \mtx{Y}) \to 1 - 2 \sqrt{\varrho} + \varrho \quad\text{almost surely}.$$ When the aspect ratio $\varrho$ is small (that is, $n \gg d$), the bound[eqn:wishart-nonasymp] is correct to first order, including the numerical constant. On the other hand, the bound is only active inside the regime where $n \geq 4d$, so it does not speak to the more challenging case

<!-- chunk {"id": "body-0042", "role": "body", "section": "Nonexample: Wishart matrix", "weight": 1.0} -->

Suppose that we apply thm:iid-intro directly to the random matrix $\mtx{Y} \sim \textsc{wishart}_{\R}(\Id_d, n)$ without a decomposition into rank-one terms.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Nonexample: Wishart matrix", "weight": 1.0} -->

(That is, we set $\mtx{W} \sim \textsc{wishart}_{\R}(\Id_d, n)$ and add only a single copy.) After a calculation, we obtain the comparison model: $$\mtx{Z} = n \cdot \Id_d + \gamma n \cdot \Id_d + \sqrt{n} \cdot \mtx{G}_{\goe}.$$ The minimum eigenvalue satisfies the same bound as before, but the weak variance is much larger: $$\Expect \lambda_{\min}(\mtx{Z}) \geq 1 - 2 \sqrt{dn} \quad\text{and}\quad \sigma_{*}^2(\mtx{Z}) \leq n^2 + 2n.$$ thm:iid-intro results in the comparison $$\Expect \lambda_{\min}(\mtx{Y}) \geq n - 2 \sqrt{dn} - n \sqrt{2 (1 +

<!-- chunk {"id": "body-0044", "role": "body", "section": "Nonexample: Wishart matrix", "weight": 1.0} -->

2/n) \log (2d)}.$$ This inequality is always vacuous.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Nonexample: Wishart matrix", "weight": 1.0} -->

From this exercise, we discover that thm:iid-introfurnishes different conclusions, depending on how we decompose a random matrix as a sum of iid psd terms. Heuristically, we want to break the random matrix into the smallest pieces we can to extract the most leverage from the theorem.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Equivariance", "weight": 1.0} -->

thm:sampling-intro,thm:iid-intro is that the results are equivariant under linear transformations (prop:mom-equi). In particular, if $\mtx{Z}$ is a Gaussian comparison model for the random psd sum $\mtx{Y}$, then $\mtx{K}^* \mtx{Z} \mtx{K}$ is a Gaussian comparison model for $\mtx{K}^* \mtx{Y} \mtx{K}$. In this statement, $\mtx{K}$is any conformable matrix, not necessarily square.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Equivariance", "weight": 1.0} -->

This observation facilitates the computation of comparison models. For instance, it is often convenient to transform the random matrix $\mtx{Y}$ so that its expectation $\Expect \mtx{Y} = \Id$. The equivariance property also plays a central role in the analysis of randomized subspace injections (sec:subspace-inj).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Gaussian comparison versus matrix concentration", "weight": 1.0} -->

When is the Gaussian comparison method effective?

<!-- chunk {"id": "body-0049", "role": "body", "section": "Gaussian comparison versus matrix concentration", "weight": 1.0} -->

Consider a self-adjoint Gaussian matrix $\mtx{Z} \in \Sym_d$. Its minimum eigenvalue satisfies $$\Expect \lambda_{\min}(\mtx{Z}) \geq \lambda_{\min}(\Expect \mtx{Z}) - \Expect \norm{ \mtx{Z} - \Expect \mtx{Z} }.$$ A sufficient condition for the comparison[eqn:intro-thm-iid-expect] between $\lambda_{\min}(\mtx{Y})$ and $\lambda_{\min}(\mtx{Z})$ to be informative is that the right-hand side of[eqn:lmin-lb]is positive. To check the latter condition, we need to understand the scale for the expected norm.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Gaussian comparison versus matrix concentration", "weight": 1.0} -->

To that end, define the matrix variance statistic[:Introduction-Matrix]: $$\sigma^2(\mtx{Z}) \coloneqq \norm{ \Expect{} (\mtx{Z} - \Expect \mtx{Z})^2 }.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Gaussian comparison versus matrix concentration", "weight": 1.0} -->

The matrix variance controls the expected norm of a self-adjoint, centered $$\sqrt{(2/\pi) \, \sigma^2(\mtx{Z})} \leq \Expect \norm{ \mtx{Z} - \Expect \mtx{Z} } \leq \sqrt{2 \sigma^2(\mtx{Z}) \log(2d)}.$$ This statement[eqn:nck-intro] is a variant of the matrix Khinchin inequality (fact:nck). Both bounds in[eqn:nck-intro] are saturated. We must undertake a more sensitive analysis to determine whether or not the expected norm includes the dimensional factor, $\log(2d)$. The matrix variance compares with the weak variance: $$\sigma_*^2(\mtx{Z}) \leq \sigma^2(\mtx{Z}) \leq d \cdot \sigma_*^2(\mtx{Z}).$$ Both bounds in[eqn:intro-var-wvar] are attainable.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Gaussian comparison versus matrix concentration", "weight": 1.0} -->

In contrast to $\lambda_{\min}(\mtx{Z})$, the statistics $\sigma^2(\mtx{Z})$ and $\sigma_*^2(\mtx{Z})$are easy to compute, as they only depend on the second moments of the random matrix.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Gaussian comparison versus matrix concentration", "weight": 1.0} -->

We can obtain a coarse version of thm:iid-sum by incorporating the estimates[eqn:lmin-lb], [eqn:nck-intro], and[eqn:intro-var-wvar]. For instance, the expectation bound[eqn:intro-thm-iid-expect] $$\Expect \lambda_{\min}(\mtx{Y}) \geq \lambda_{\min}(\Expect \mtx{Z}) - 2\sqrt{2 \sigma^2(\mtx{Z}) \log(2d)}. %$$ In fact, an improvement of the estimate[eqn:mtx-bern-lb] follows from simpler arguments based on the scalar mgf inequality[eqn:intro-scalar-mgf] and matrix concentration tools[:Introduction-Matrix]; see app:epz for details.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Gaussian comparison versus matrix concentration", "weight": 1.0} -->

The benefits of the Gaussian comparison method now come into sharper focus. thm:sampling-intro,thm:iid-intro are most effective in case $$\lambda_{\min}(\Expect \mtx{Z}) \gg \Expect \norm{ \mtx{Z} - \Expect \mtx{Z}} \approx \sigma(\mtx{Z}) But we need a finer scalpel than the matrix Khinchin inequality[eqn:nck-intro]to assess whether the expected norm includes the dimensional factor. [Wishart: Matrix concentration] Suppose we apply the matrix concentration bound[eqn:mtx-bern-lb] to the comparison model[eqn:wishart-comp] for the Wishart matrix $\mtx{Y} \sim \textsc{wishart}_{\R}(\Id_d, n)$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Gaussian comparison versus matrix concentration", "weight": 1.0} -->

The matrix variance statistic $\sigma^2(\mtx{Z}) = n(d+2)$, and we arrive at the bound $$\Expect \lambda_{\min}(\mtx{Y}) \geq n - 2 \sqrt{2n (d+2) \log(2d)}.$$ This bound, while nontrivial, does not capture the correct dimensional dependence that is visible in[eqn:wishart-nonasymp]. We have squandered the valuable distributional information provided by thm:iid-intro.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Gaussian comparison versus matrix concentration", "weight": 1.0} -->

Recent research[:Second-Order-Matrix,:Matrix-Concentration] has demonstrated that we can sometimes compare the eigenvalue distribution of a Gaussian matrix with a free probability model, using simple summary statistics. These intrinsic freeness results can be valuable for handling the Gaussian comparison model, but they are unhelpful for the applications in this paper.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Universality laws for random matrices", "weight": 1.0} -->

Compared with our work, the results that are closest in spirit appear in a recent paper of Brailovskaya & van Handel[:Universality-Sharp]. Their paper contains quantitative universality theorems for sums of random matrices, in the spirit of the BerryEsseen theorem. As we will explain, their results are incomparable with the ones in this paper.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Universality laws for random matrices", "weight": 1.0} -->

& van Handel consider an independent sum of self-adjoint random matrices $\mtx{W}_i$, not necessarily psd or identically distributed. They compare the sum with a Gaussian model that shares the same first- and second-order statistics, as in the multivariate central limit theorem: $$\mtx{Y} = \sum_{i=1}^n \mtx{W}_i \quad\text{and}\quad \mtx{Z}' \sim \normal(\Expect[\mtx{Y}],\ \Varo[\mtx{Y}]).$$ In contrast, our approach requires the summands $\mtx{W}_i$to be iid random psd matrices, and it compares the sum with a slightly different Gaussian model.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Universality laws for random matrices", "weight": 1.0} -->

Under appropriate conditions on the summands, Brailovskaya & van Handel argue that the eigenvalue distribution of $\mtx{Y}$ and the eigenvalue distribution of the Gaussian model $\mtx{Z}'$ are similar. Their results address both the spectral density and the spectral support. As one may imagine, it appears to require stricter assumptions on the statistics of the random matrices to ensure this strong affinity.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Universality laws for random matrices", "weight": 1.0} -->

For instance, to control the minimum eigenvalue of the random sum, & van Handel assume that the uniform bound statistic $$R \coloneqq \Expect \max\nolimits_i \norm{\mtx{W}_i}^2 \ll \sigma(\mtx{Y}) (\log d)^{-3}.$$ This condition ensures that each one of the summands makes a limited contribution to the sum. The restriction is particularly important when the random matrices have few moments or the summands have inhomogeneous distributions.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Universality laws for random matrices", "weight": 1.0} -->

Under this surmise, they prove[:Universality-Sharp] that the expected distance between the minimum eigenvalues satisfies $$\Expect \abs{ \lambda_{\min}(\mtx{Y}) - \lambda_{\min}(\mtx{Z}') } \lesssim \sigma(\mtx{Z}')^{5/6} R^{1/6} \log d % + \smash{\sigma_*(\mtx{Z}')} (\log d)^{1/2}.$$ As in the present paper, the second term arises from Gaussian concentration. To understand the first term, recall from[eqn:nck-intro] that the scale for the minimum eigenvalue of $\Expect \lambda_{\min}(\mtx{Z}' - \Expect \mtx{Z}')$ is the statistic $\sigma(\mtx{Z}')$. In some examples, the factor $R^{1/6} \log d$submerges the first term below this level.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Universality laws for random matrices", "weight": 1.0} -->

The results of Brailovskaya & van Handel are powerful and wide ranging. For some of the applications we consider in this paper, however, their approach produces several parasitic logarithmic factors that make it impossible to reach the optimal bounds. These factors are particularly significant in applications to computational mathematics (sec:subspace-inj), where constants and logarithms matter.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Universality laws for random matrices", "weight": 1.0} -->

As with our Gaussian comparison theorems, the proof strategy in the paper of &van Handel is based on techniques from Stein's method. While there are small points of similarity (e.g., the use of interpolation), our technical apparatus follows an independent design.

<!-- chunk {"id": "body-0064", "role": "body", "section": "An independent sum of random psd matrices", "weight": 1.0} -->

There is also a body of work that provides specialized bounds for the minimum eigenvalue of an independent sum of random psd matrices. Several of these papers are inspired by the same observation that an independent sum of nonnegative real random variables has a Gaussian lower tail, and they pursue this insight in creative and multifarious ways. We focus on the earliest and most distinctive contributions.

<!-- chunk {"id": "body-0065", "role": "body", "section": "An independent sum of random psd matrices", "weight": 1.0} -->

This literature treats several different random matrix models. To facilitate comparisons, we summarize the implications for a special case involving sample covariance matrices. Consider a random vector $\vct{w} \in \R^d$ that has four finite moments. For normalization, assume that the vector is isotropic: $\Expect[\vct{ww}^\transp] = \Id_d$. Form the sample covariance matrix based on $n$ samples: $$\mtx{Y} = \frac{1}{n} \sum_{i=1}^n \vct{w}_i \vct{w}_i^\transp \quad\text{where $\vct{w}_i \sim \vct{w}$ iid.}$$ For a parameter $\eps \in $, how many samples $n = n(\eps)$ are sufficient to ensure that $\lambda_{\min}(\mtx{Y}) \geq 1 - \eps$with high probability? The weak assumptions on moments make this question very challenging.

<!-- chunk {"id": "body-0066", "role": "body", "section": "An independent sum of random psd matrices", "weight": 1.0} -->

formulated this problem and made the first contribution. They considered a random vector $\vct{w} \in \R^d$ that satisfies the uniform fourth moment condition $$\max\nolimits_{\norm{\vct{u}} = 1} \Expect{} \abs{ \ip{ \vct{u} }{ \vct{w} } }^{4} \leq L.

<!-- chunk {"id": "body-0067", "role": "body", "section": "An independent sum of random psd matrices", "weight": 1.0} -->

They establish a sample complexity bound: \quad\text{implies}\quad \Expect \lambda_{\min}(\mtx{Y}) \geq 1 - \eps.$$ Their paper is important because the sample complexity $n$ has the correct (linear) dependence on the dimension $d$, although it exhibits a suboptimal dependence on $\eps$. Their proof employs a Stieltjes transform argument inspired by work in spectral graph theory[:Twice-Ramanujan].

<!-- chunk {"id": "body-0068", "role": "body", "section": "An independent sum of random psd matrices", "weight": 1.0} -->

& Mendelson[:Bounding-Smallest] developed a family of related results under a weak form of the moment condition[eqn:sv-moments]. For some $\eta > 2$, assume that $$\Prob{ \abs{\ip{ \vct{u} }{ \vct{w} }} > t } \leq L t^{-(2 + \eta)} \quad\text{when $\norm{ \vct{u} } = 1$ and $t \geq 1$.}$$ Their work yields the correct dependence on the parameter $\eps$. Indeed, \quad\text{implies}\quad \Prob{ \lambda_{\min}(\mtx{Y}) < 1 - \eps } \leq C \log(\econst n / d) \cdot \econst^{- d / C }.$$ The constant $C = C(\eta, L)$. Their proof involves truncation, small ball probabilities, and a VapnikChervonenkis dimension argument. [:Lower-Tail] proposed a third approach.

<!-- chunk {"id": "body-0069", "role": "body", "section": "An independent sum of random psd matrices", "weight": 1.0} -->

Under the assumption[eqn:sv-moments], he established that $$n \geq 81 L \eps^{-2}{} (d + 2 \log(2/\delta)) \quad\text{implies that}\quad \Prob{ \lambda_{\min}(\mtx{Y}) < 1 - \eps } The bound[eqn:scov-oliveira] has the correct dependence on all of the parameters. Oliveira's argument relies on the PAC-Bayesian method[:PAC-Bayes,:Simplified-PAC-Bayesian,:Robust-Linear], a technique that smooths the distribution and employs the variational properties of the entropy to obtain bounds. In sec:scov, we will exploit the Gaussian comparison method to give a short proof of Oliveira's bound[eqn:scov-oliveira].

<!-- chunk {"id": "body-0070", "role": "body", "section": "An independent sum of random psd matrices", "weight": 1.0} -->

The papers discussed in this section depend heavily on moment assumptions, such as which cannot capture the detailed distribution of a random vector. To highlight the benefits of the Gaussian comparison method, we will obtain new bounds for the sample covariance of a very sparse random vector (thm:sparse-cov).

<!-- chunk {"id": "body-0071", "role": "body", "section": "Gaussian random matrices", "weight": 1.0} -->

To take advantage of the Gaussian comparison method, we must be able to construct the comparison model and determine its spectral properties. This section outlines some facts about Gaussian random matrices that will play a role in the applications and the proofs of the main theorems. For generality, we work in the complex setting, which includes the real setting as a special case.

<!-- chunk {"id": "body-0072", "role": "body", "section": "The Cartesian decomposition", "weight": 1.0} -->

To simplify some formulas, let us introduce the Cartesian decomposition of a square matrix.

<!-- chunk {"id": "body-0073", "role": "body", "section": "The Cartesian decomposition", "weight": 1.0} -->

The real part and imaginary part of a square matrix $\mtx{M} \in \M_d(\C)$ with complex entries are the self-adjoint matrices \Re \mtx{M} \coloneqq \frac{1}{2} (\mtx{M} + \mtx{M}^*) \in \Sym_d(\C) \quad\text{and}\quad \Im \mtx{M} \coloneqq \frac{1}{2\iunit} (\mtx{M} - \mtx{M}^*) \in \Sym_d(\C).

<!-- chunk {"id": "body-0074", "role": "body", "section": "The Cartesian decomposition", "weight": 1.0} -->

The Cartesian decomposition states that $\mtx{M} = (\Re \mtx{M}) + \iunit (\Im \mtx{M})$, and the two terms are orthogonal with respect to the trace inner product.

<!-- chunk {"id": "body-0075", "role": "body", "section": "First and second moments of random matrices", "weight": 1.0} -->

$\mtx{X} \in \Sym_d(\C)$ be a random self-adjoint matrix with complex entries. The second moment function (def:second-moments) contains information about the second moment of each entry of the random matrix: \quad\text{and}\quad As usual, $\mathbf{E}_{ij} \in \M_d(\C)$ is the $(i, j)$ element of the standard basis for matrices. We can extract mixed second moments via polarization.

<!-- chunk {"id": "body-0076", "role": "body", "section": "First and second moments of random matrices", "weight": 1.0} -->

The variance function (def:second-moments) collects the second moments of the centered random matrix: \Varo[\mtx{X}] = \Mo[\mtx{X} - \Expect \mtx{X}] = \Mo[\mtx{X}] - \Mo[\Expect \mtx{X}].$$ For random self-adjoint matrices $\mtx{X}, \mtx{Y} \in \Sym_d(\C)$, the variance function is additive in the sense that $$\Varo[\mtx{X} + \mtx{Y}] = \Varo[\mtx{X}] + \Varo[\mtx{Y}] \quad\text{when $\mtx{X}, \mtx{Y}$ are \hilite{independent}.}$$ For contrast, the second moment function $\Mo$ does not satisfy the additivity rule[eqn:cov-add].

<!-- chunk {"id": "body-0077", "role": "body", "section": "First and second moments of random matrices", "weight": 1.0} -->

As usual, $\coll{L}^*$ is the adjoint of the linear map with respect to the trace inner product.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Matrix Gaussian series", "weight": 1.0} -->

sec:intro-mom provides an abstract definition of a Gaussian random matrix. This section introduces a concrete model that is often useful for calculations. A (self-adjoint) matrix Gaussian series is a random matrix model of the form $$\mtx{Z} = \mtx{\Delta} + \sum_{i=1}^n \gamma_i \mtx{H}_i \quad\text{where $\gamma_i \sim \normal_{\R}$ iid.}$$ The coefficients $(\mtx{\Delta}, \mtx{H}_1, \dots, \mtx{H}_n)$ are deterministic matrices in $\Sym_d(\C)$. Let us emphasize that the Gaussian random variables $\gamma_i$ are real-valued. Every self-adjoint Gaussian random matrix can be written in the form[eqn:mtx-gauss]in many different ways.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Matrix Gaussian series", "weight": 1.0} -->

We can easily compute the mean and variance function of the $$\Expect \mtx{Z} = \mtx{\Delta} \quad\text{and}\quad \Varo[\mtx{Z}](\mtx{M}) = \sum_{i=1}^n \abssq{ \ip{ \mtx{M} }{\mtx{H}_i} } \quad\text{for $\mtx{M} \in \Sym_d(\C)$.}$$ The expression for the variance function follows from the additivity rule[eqn:cov-add].

<!-- chunk {"id": "body-0080", "role": "body", "section": "Gaussian monotonicity", "weight": 1.0} -->

Gaussian random matrices enjoy a strong monotonicity property. As the variance function increases, expectations of convex functions of the random matrix also increase.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Gaussian monotonicity", "weight": 1.0} -->

Consider two self-adjoint Gaussian matrices whose distributions $\mtx{Z} \sim \normal(\mtx{\Delta}, \mathsf{V})$ and $\mtx{Z}' \sim \normal(\mtx{\Delta}, \mathsf{V}')$ take values in $\Sym_d(\C)$ and share the same mean.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Gaussian monotonicity", "weight": 1.0} -->

Suppose the variance functions $\mathsf{V}$ and $\mathsf{V}'$ satisfy the pointwise inequality $$\mathsf{V}(\mtx{M}) \leq \mathsf{V}'(\mtx{M}) \quad\text{for all $\mtx{M} \in \Sym_d(\C)$.}$$ For each convex function $f: \Sym_d(\C) \to \R$, $$\Expect f(\mtx{Z}) \leq \Expect f(\mtx{Z}').$$ Since $\mathsf{V}' - \mathsf{V}$ is a positive quadratic form on $\Sym_d(\C)$, we can construct a Gaussian matrix $\mtx{X} \sim \normal(\mtx{0}, \mathsf{V}' - \mathsf{V})$ that is independent from $\mtx{Z}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Gaussian monotonicity", "weight": 1.0} -->

By linearity of expectation, $\Expect[\mtx{Z} + \mtx{X}] = \mtx{\Delta}$. By additivity of the variance function[eqn:cov-add], $$\Varo[\mtx{Z} + \mtx{X}] = \Varo[\mtx{Z}] + \Varo[\mtx{X}] = \mathsf{V} + (\mathsf{V}' - \mathsf{V}) = \mathsf{V}'.$$ Therefore, the sum $\mtx{Z} + \mtx{X} \sim \normal(\mtx{\Delta}, \mathsf{V}')$ follows the same distribution as $\mtx{Z}'$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Gaussian monotonicity", "weight": 1.0} -->

To obtain the convexity inequality[eqn:gauss-convex], note that $$\Expect f(\mtx{Z}') = \Expect f(\mtx{Z} + \mtx{X}) \geq \Expect f(\mtx{Z}).$$ We have invoked Jensen's inequality, conditional on $\mtx{Z}$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Matrix variance", "weight": 1.0} -->

We can capture information about spectral features of a Gaussian matrix using scalar summary statistics.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Matrix variance", "weight": 1.0} -->

The matrix variance of a self-adjoint Gaussian matrix $\mtx{Z} \in \Sym_d(\C)$ $$\sigma^2(\mtx{Z}) \coloneqq \lnorm{ \Expect{} (\mtx{Z} - \Expect \mtx{Z})^2 } = \lnorm{ \sum_{i=1}^n \mtx{H}_i^2 }.$$ The second identity in[eqn:matrix-var] is valid for an arbitrary representation[eqn:mtx-gauss] of $\mtx{Z}$ as a Gaussian series. When $\mtx{Z}, \mtx{Z}'$ are independent, we have the subadditivity rule $\sigma^2(\mtx{Z} + \mtx{Z}') \leq \sigma^2(\mtx{Z}) + \sigma^2(\mtx{Z}')$.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Matrix variance", "weight": 1.0} -->

The matrix Khinchin inequality states that the matrix variance controls the expectation of the extreme eigenvalues of the Consider a self-adjoint Gaussian matrix $\mtx{Z}$ with dimension $d$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Matrix variance", "weight": 1.0} -->

$$- \Expect \lambda_{\min}(\mtx{Z} - \Expect \mtx{Z}) = \Expect \lambda_{\max}(\mtx{Z} - \Expect \mtx{Z}) \leq \sqrt{2 \sigma^2(\mtx{Z}) \log d}.$$ In general, the logarithmic factor in[eqn:mki] is required. The lower bound stated in[eqn:nck-intro] follows from a sharp moment comparison[:Gaussian-Measures] and Jensen's inequality.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Weak variance", "weight": 1.0} -->

For a self-adjoint Gaussian matrix the weak variance statistic is defined as $$\sigma_*^2(\mtx{Z}) \coloneqq \max\nolimits_{\norm{\vct{u}} = 1} \Var[\vct{u}^* \mtx{Z} \vct{u}] = \max\nolimits_{\norm{\vct{u}} = 1} \sum_{i=1}^n (\vct{u}^* \mtx{H}_i \vct{u})^2.$$ The second identity holds for an arbitrary representation[eqn:mtx-gauss] of $\mtx{Z}$ as a Gaussian series. As stated in[eqn:intro-var-wvar], the weak variance is controlled by the matrix variance, and both bounds are attainable.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Weak variance", "weight": 1.0} -->

As a consequence, for self-adjoint Gaussian matrices $\mtx{Z}, \mtx{Z}' \in \Sym_d(\C)$, the weak variance is monotone with respect to the variance function: $$\Varo[\mtx{Z}] \leq \Varo[\mtx{Z}'] \quad\text{implies}\quad \sigma_*^2(\mtx{Z}) \leq \sigma_*^2(\mtx{Z}').$$ When $\mtx{Z}, \mtx{Z}'$ are independent, we also have the subadditivity rule $\sigma_*^2(\mtx{Z} + \mtx{Z}') \leq \sigma_*^2(\mtx{Z}) + \sigma_*^2(\mtx{Z}')$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Weak variance", "weight": 1.0} -->

The weak variance arises when studying concentration properties of Gaussian random matrices.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Weak variance", "weight": 1.0} -->

\R$.}$$ We can instantiate[eqn:gauss-lip-mgf] with $h = \lambda_{\max}$ or $h = \lambda_{\min}$ because of Weyl's inequality[:Matrix-Analysis].

<!-- chunk {"id": "body-0093", "role": "body", "section": "Weak variance", "weight": 1.0} -->

The last inequality is CauchySchwarz. In other words, the statistic $\sigma_*(\mtx{Z})$ is the Lipschitz constant of $h(\mtx{Z})$. Gaussian Lipschitz concentration[:Concentration-Inequalities] yields the mgf bound[eqn:gauss-lip-mgf].

<!-- chunk {"id": "body-0094", "role": "body", "section": "Basic examples", "weight": 1.0} -->

Let us collect some simple Gaussian matrices that we may combine to build comparison models. we can represent a Gaussian matrix as a sum of independent Gaussian matrices by breaking the variance function into pieces and identifying a Gaussian model for each piece. This strategy is justified by the additivity[eqn:cov-add] of the random variables $\gamma, \gamma_i, \gamma_{jk}, \smash{\gamma_{jk}'}$ are iid $\normal_{\R}$. For $v \geq 0$, the distribution $\normal_{\C}(0,v)$ generates a complex Gaussian random variable whose real and imaginary parts are iid $\normal_{\R}(0,v/2)$random variables.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Scalar Gaussian matrix", "weight": 1.0} -->

As a warmup, consider the scalar matrix $\mtx{S} \coloneqq \gamma \Id \in \Sym_d(\C)$. It is easy to see that $\Expect \lambda_{\min}(\mtx{S}) = \Expect \lambda_{\max}(\mtx{S}) = 0$. The variance function of the scalar matrix acts as $$\Varo[\mtx{S}](\mtx{M}) = (\trace \mtx{M})^2 \quad\text{for $\mtx{M} \in \Sym_d(\C)$.}$$ Last, note that the matrix variance and weak variance coincide: $\sigma^2(\mtx{S}) = \sigma^2_{*}(\mtx{S}) = 1$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Diagonal Gaussian matrix", "weight": 1.0} -->

Next, consider the diagonal matrix: $$\mtx{D} \coloneqq \sum_{i=1}^d \gamma_i \mathbf{E}_{ii} \in \Sym_d(\C). % The extreme eigenvalues satisfy $$- \Expect \lambda_{\min}(\mtx{D}) = \Expect \lambda_{\max}(\mtx{D}) = \Expect \max\{ \gamma_i: i =1, \dots, d\} \leq \sqrt{2 \log d}.$$ This expectation bound is asymptotically sharp.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Gaussian orthogonal ensemble", "weight": 1.0} -->

Now, we turn to a more sophisticated example. A random matrix from the (unnormalized) Gaussian orthogonal ensemble (GOE) takes the form $$\mtx{G}_{\goe} \coloneqq \sqrt{2} \sum_{j,k = 1}^d \gamma_{jk} (\Re \mathbf{E}_{jk}) Note that this matrix is real and symmetric. The diagonal entries are iid $\normal_{\R}$ random variables, while the entries in the upper triangle are iid $\normal_{\R}$ random variables.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Gaussian orthogonal ensemble", "weight": 1.0} -->

\quad\text{for $\mtx{M} \in \Sym_d(\R)$.}$$ The matrix variance and weak variance differ almost as much as possible.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Gaussian orthogonal ensemble", "weight": 1.0} -->

Indeed, $\sigma^2(\mtx{G}_{\goe}) = d + 1$ and $\sigma_*^2(\mtx{G}_{\goe}) = 2$. GOE matrices arise in several of our comparisons. (For example, see sec:wishart.)

<!-- chunk {"id": "body-0100", "role": "body", "section": "Gaussian unitary ensemble", "weight": 1.0} -->

Gaussian unitary ensemble (GUE) is the complex cousin of the GOE. A random matrix from this family takes the form $$\mtx{G}_{\gue} \coloneqq \sum_{j,k = 1}^d \big[\gamma_{jk} (\Re \mathbf{E}_{jk}) + \gamma_{jk}' (\Im \mathbf{E}_{jk}) \big] The diagonal entries are iid real $\normal_{\R}$ random variables, while the entries in the upper triangle are iid complex $\normal_{\C}$ random variables.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Gaussian unitary ensemble", "weight": 1.0} -->

The GUE distribution is unitarily invariant: $$\mtx{U}^* \mtx{G}_{\gue} \mtx{U} \sim \mtx{G}_{\gue} \quad\text{for each unitary $\mtx{U} \in \M_d(\C)$.}$$ The extreme eigenvalues of the GUE matrix satisfy the following bound[:Alice-Bob].

<!-- chunk {"id": "body-0102", "role": "body", "section": "Application: Sampling from a design", "weight": 1.0} -->

We begin with a geometric example. If we randomly subsample a set of vectors that spans a (complex) linear space, does the reduced set still span the space?

<!-- chunk {"id": "body-0103", "role": "body", "section": "Application: Sampling from a design", "weight": 1.0} -->

In considering this question, we must enforce some regularity properties to avoid situations where most of the vectors fall in a proper subspace. For illustration, we impose a rather strong condition, which ensures that the vectors are distributed evenly across the unit sphere.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Projective designs", "weight": 1.0} -->

Consider a finite system $\coll{U} \coloneqq (\vct{u}_1, \dots, \vct{u}_n)$ of unit-norm vectors in $\C^d$. The system is called a complex projective $t$-design when it yields a quadrature rule for homogeneous degree-$2t$ polynomials on the complex unit sphere $\mathbb{S}^{d-1}(\C)$.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Projective designs", "weight": 1.0} -->

Examples of projective 2-designs include systems of equiangular vectors, mutually unbiased bases, and other highly symmetric configurations. See[:Introduction-Finite] or[:Fast-State-Tomography]for more examples and discussion.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Sampling from a projective design", "weight": 1.0} -->

A classic question in nonasymptotic random matrix theory asks when a random subset of an isotropic system remains a spanning set. The fundamental result for this problem is due to Rudelson[:Random-Vectors]; see sec:rudelsonfor a proof sketch. [Sampling: Projective 1-design] Consider a complex projective 1-design $\coll{U} \coloneqq (\vct{u}_1, \dots, \vct{u}_n)$ consisting of $n$ unit-norm vectors in $\smash{\C^d}$. For a parameter $1 \leq s \leq n$, construct a random subsystem $\coll{U}'$ with an average of $s$ vectors by uniform sampling: \quad\text{where $\xi_i \sim \bernoulli(s/n)$ iid.}$$ When $s \geq d \log(d/\delta)$, the random system $\coll{U}'$ spans $\C^d$ with probability at least $1 - \delta$.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Sampling from a projective design", "weight": 1.0} -->

The logarithmic factor in the sampling complexity is necessary. fact:sampling-1-design, we study the problem of sampling from a complex projective 2-design. We will establish that a random subset remains a spanning set when the average number of vectors exceeds the ambient dimension by a constant factor. The proof appears insec:sampling-2-design.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Sampling from a projective design", "weight": 1.0} -->

With the notation of fact:sampling-1-design, assume that the system $\coll{U}$ is a complex projective 2-design. When the average number $s$ of sampled vectors satisfies $$s \geq 4 \big[\sqrt{d} + \sqrt{\log(d/\delta)} \big]^2, %$$ the random subset $\coll{U}'$ spans $\C^d$ with probability at least $1 - \delta$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Sampling from a projective design", "weight": 1.0} -->

To analyze the subsampled system $\coll{U}'$, defined in [eqn:subsample-vecs], we introduce the random psd matrix $$\mtx{Y} \coloneqq \sum_{\vct{u} \in \coll{U}'} \vct{uu}^* = \sum_{i=1}^n \xi_i \vct{u}_i \vct{u}_i^* \quad\text{where $\xi_i \sim \bernoulli(s/n)$ iid.}$$ Observe that the system $\coll{U}'$ spans $\C^d$ if and only if $\lambda_{\min}(\mtx{Y}) > 0$. We can obtain the minimum eigenvalue bound from a quick application of the Gaussian comparison method (thm:sampling-intro).

<!-- chunk {"id": "body-0110", "role": "body", "section": "Sampling from a projective design", "weight": 1.0} -->

the existing techniques for minimum eigenvalues[:Covariance-Estimation,:Bounding-Smallest,:Lower-Tail] all fail to provide the correct bound for $\lambda_{\min}(\mtx{Y})$ because the summands in[eqn:Y-subsample] are both spiky and non-identically distributed. Spectral universality tools, such as[:Universality-Sharp], also produce the wrong answer when applied to the random matrix $\mtx{Y}$.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Application: Sample covariance matrices", "weight": 1.0} -->

Our next application arises from high-dimensional statistics. Suppose that we want to detect which linear marginals of a random vector have strictly positive variance One procedure is to draw iid copies of the random vector and to form the sample covariance matrix. The sample covariance matrix provides estimates for the variance of each marginal. How many samples are sufficient to ensure that none of these estimates is too small?

<!-- chunk {"id": "body-0112", "role": "body", "section": "Application: Sample covariance matrices", "weight": 1.0} -->

Using the Gaussian comparison theorem (we can reproduce and extend several major results on sample covariance matrices from the recent literature. When the second moments and fourth moments of the random vector are comparable, then the sampling complexity is proportional to the dimension of the random vector[:Lower-Tail]. We can also obtain useful information about the sample covariance matrix of a very sparse random vector[:Extreme-Singular].

<!-- chunk {"id": "body-0113", "role": "body", "section": "The sample covariance matrix", "weight": 1.0} -->

real random vector $\vct{w} \in \R^d$ with dimension $d$ that has four finite moments: $\Expect \norm{\vct{w}}^4 < + \infty$. Assume that the random vector is centered, and introduce the (population) covariance matrix: $$\Expect[\vct{w}] = \vct{0} \quad\text{and} \quad \mtx{K} \coloneqq \Expect[\vct{ww}^\transp].$$ For simplicity, we also assume that the covariance matrix $\mtx{K}$ has full rank $d$.

<!-- chunk {"id": "body-0114", "role": "body", "section": "The sample covariance matrix", "weight": 1.0} -->

We can compute the variance of a linear marginal of the random vector in terms of the covariance matrix: $$\Var[\ip{ \vct{a} }{ \vct{w} }] = \vct{a}^\transp \mtx{K} \vct{a} \quad\text{for each $\vct{a} \in \R^d$.}$$ Our goal is to obtain lower bounds for the variance in every direction, which we call the variance detectionproblem.

<!-- chunk {"id": "body-0115", "role": "body", "section": "The sample covariance matrix", "weight": 1.0} -->

Suppose that we sample $n$ iid copies of the random vector $\vct{w}$. The sample covariance matrix of this data is the random psd matrix $$\widehat{\mtx{K}}_n \coloneqq \frac{1}{n} \sum_{i=1}^n \vct{w}_i \vct{w}_i^\transp \quad\text{where $\vct{w}_i \sim \vct{w}$ iid.}$$ The sample covariance is an unbiased estimator for the true covariance: $\Expect[\widehat{\mtx{K}}_n] = \mtx{K}$ for each $n \in \N$. Moreover, the sample covariance matrix provides estimates for the variance of each linear marginal[eqn:marg-var] of the distribution.

<!-- chunk {"id": "body-0116", "role": "body", "section": "The sample covariance matrix", "weight": 1.0} -->

For a parameter $\eps \in $, with high probability, $$\vct{a}^\transp \widehat{\mtx{K}}_n \vct{a} \geq (1 - \eps) \cdot \vct{a}^\transp \mtx{K} \vct{a} \quad\text{for \hilite{all} $\vct{a} \in \R^d$.}$$ How many samples $n = n(\vct{w}, \eps)$ are sufficient to ensure that the property[eqn:scov-marginal-lb]is likely to prevail?

<!-- chunk {"id": "body-0117", "role": "body", "section": "The sample covariance matrix", "weight": 1.0} -->

The answer to this question depends on the distribution of the random vector Since $\mtx{K}$ has rank $d$, it is necessary that $n \geq d$ because the rank of the sample covariance matrix $\smash{\widehat{\mtx{K}}_n}$ does not exceed the number $n$ of samples. For a worst-case vector that satisfies $\norm{\vct{w}} \lesssim \smash{\sqrt{d}}$, it is necessary to draw $n \asymp d \log d$ samples[:Random-Vectors].

<!-- chunk {"id": "body-0118", "role": "body", "section": "The sample covariance matrix", "weight": 1.0} -->

A major technical challenge is to find large classes of random vectors where the sample complexity of is proportional to the dimension: $n \asymp d$. This problem has already inspired a vast literature that draws on a diverse set of technical ideas. The Gaussian comparison inequality (thm:iid-intro) offers a new methodology for addressing this problem.

<!-- chunk {"id": "body-0119", "role": "body", "section": "The sample covariance matrix", "weight": 1.0} -->

Our approach adapts to the complex setting with minimal changes. We work in the real setting, as it is more typical in the statistics literature.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Sample covariance: Four moment theorem", "weight": 1.0} -->

Our first result reconstructs a prominent theorem from high-dimensional statistics, in a form When the second and fourth moments of a random vector are comparable, then the sample complexity of the variance detection problem is proportional The proof appears below insec:scov-mom-result-pf.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Sample covariance: Four moment theorem", "weight": 1.0} -->

Suppose that $\vct{w} \in \R^d$ is a centered random vector with covariance matrix $\mtx{K}$ and with four finite moments.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Sample covariance: Four moment theorem", "weight": 1.0} -->

\widehat{\mtx{K}}_n \vct{a} > (1 - \eps) \cdot \vct{a}^\transp \mtx{K} \vct{a} \quad\text{for all $\vct{a} \in \R^d$.}$$ The sample complexity [eqn:scov-mom-samples] contains a startup cost of $n \gtrsim \beta^2 \log(d/\delta)$ samples to ensure that the failure probability is controlled.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Sample covariance: Four moment theorem", "weight": 1.0} -->

Usually, the sample complexity is governed by the other term: $n \gtrsim \beta^2 d$. The statistic $\beta$relates the second and fourth moments of marginals of the random vector.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Sample covariance: Four moment theorem", "weight": 1.0} -->

The sample complexity $n \asymp d$ whenever the comparison factor $\beta$ is independent of the dimension $d$. Many types of random vectors meet this criterion, including random vectors with independent bounded entries, log-concave random vectors, and tensor products of independent random vectors. We refer to the literature[:Covariance-Estimation,:Bounding-Smallest,:Lower-Tail,:Dimension-Free-Bounds]for more examples and discussion.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Prior work", "weight": 1.0} -->

& Vershynin[:Covariance-Estimation] established the first result in the spirit ofthm:scov-mom-result, with suboptimal dependence on the parameter $\eps$. Koltchinskii & Mendelson[:Bounding-Smallest] obtained improvements to the dependence on $\eps$ with slightly stricter Oliveira[:Lower-Tail] obtained a version of the result stated here, which gives the correct dependence on all the parameters. See sec:related-psd-sumfor more discussion. [:Covariance-Estimation,:Bounding-Smallest,:Sample-Covariance] present nonasymptotic bounds on the minimum eigenvalue of the sample covariance assuming control of the $2 + \eta$ moments, where $\eta > 0$. These conditions are weaker than[eqn:scov-mom-cond]. Nevertheless, we will see that the Gaussian comparison method can tease out structure from the random vector that is invisible to a uniform bound on moments (sec:sparse-cov).

<!-- chunk {"id": "body-0126", "role": "body", "section": "Example: Sparse covariance matrices", "weight": 1.0} -->

For a more challenging example that goes beyond the scope of we consider variance detection for a sparserandom vector. For simplicity, we treat the case of iid entries, but we only require four finite moments.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Example: Sparse covariance matrices", "weight": 1.0} -->

Fix the dimension $d$, and let $\zeta \in (0, d]$ be a sparsity parameter. Introduce a real random variable $\psi$ that is standardized and has bounded \quad\text{and}\quad \quad\text{and}\quad \Expect \abs{\psi}^4 = C.$$ Construct a sparse random vector $\vct{w} \in \R^d$ with iid entries: $$\vct{w} = \sqrt{\frac{d}{\smash{\zeta}}} \begin{bmatrix} \xi_1 \psi_1 \\ \vdots \\ \xi_d \psi_d \end{bmatrix} \quad\text{where}\quad & \text{$\xi_i \sim \bernoulli(\zeta / d)$ iid}; \\& \text{$\psi_i \sim \psi$ iid}.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Example: Sparse covariance matrices", "weight": 1.0} -->

\\It is straightforward to check that $\vct{w}$ is centered and isotropic, and $\vct{w}$ has $\zeta$ nonzero entries on average. How does the sample complexity of the variance detection problem depend Instate the prevailing notation, and fix parameters $\eps, \delta \in $. Suppose that the number $n$ of samples satisfies $$n \geq \frac{25 d \cdot (1 \vee (2C \zeta^{-1} \log(2d/\delta)))}{\eps^2}.$$ With probability at least $1 - \delta$, the sample covariance matrix of the sparse random vector $\vct{w}$ has minimum eigenvalue $\lambda_{\min}(\smash{\widehat{\mtx{K}}_n}) > 1 - \eps$. thm:sparse-cov handles two different behavioral regimes.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Example: Sparse covariance matrices", "weight": 1.0} -->

- When $\zeta \geq 2C \log d$, the sample complexity $n \asymp d$. - When $\zeta \leq 2C \log d$, the sample complexity $n \asymp C \zeta^{-1} d \log d$.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Example: Sparse covariance matrices", "weight": 1.0} -->

The linear sample complexity in the first regime is quite difficult to achieve, especially when the distribution $\psi$ has few moments. In the ultra-sparse case ($\zeta \leq 1$), similar results follow from classic matrix concentration inequalities, such asfact:matrix-epz.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Example: Sparse covariance matrices", "weight": 1.0} -->

We were unable to locate any prior work that matches although there are several closely related results. In particular, assume that the distribution $\psi$ is bounded. In this case, the paper[:Nonasymptotic-Concentration] achieves the same complexity estimate[eqn:sparse-cov-samples] for the expectation of the minimum eigenvalue of the sample covariance matrix. In the regime where the sparsity $\zeta \gtrsim \log d$ and $d/n$ is constant, Dumitriu & Zhu[:Extreme-Singular] achieve stronger estimates for the expectation of the minimum eigenvalue that are sufficient to attain the BaiYin limit, which is out of reach for our method. For a thorough literature review, refer to the paper[:Extreme-Singular].

<!-- chunk {"id": "body-0132", "role": "body", "section": "Application: Randomized subspace injections", "weight": 1.0} -->

In numerical linear algebra, for large-scale matrix computations; for example, see[:Randomized-Numerical]. The design and analysis of these algorithms often relies on methods from random matrix theory. In fact, the tools in the present paper were developed to treat challenging mathematical problems from this field. randomized subspace injection is a random linear map whose action preserves the dimension of a fixed subspace[:Improved-Approximation,:Universality-Laws]. These injections serve as an important building block for randomized linear algebra algorithms[:Sketching-Tool,:Randomized-Numerical,MDM+23:Randomized-Numerical]. In this section, we employ the Gaussian comparison theorem (thm:iid-intro) to develop a new analysis of subspace injections based on very sparse random matrices[:Low-Rank-Approximation,:OSNAP-Faster]. The result largely settles an open question of Nelson & Nguyen[:OSNAP-Faster,:Lower-Bounds] that has generated a substantial literature; sec:subspace-priorsummarizes the prior work.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Subspace injections", "weight": 1.0} -->

For a given subspace, a subspace injection is a linear map that does not annihilate any vector in that subspace Fix a matrix $\mtx{Q} \in \R^{n \times d}$ with $d$ orthonormal columns. For a fixed contraction factor $\alpha > 0$, suppose that $\mtx{\Phi} \in \R^{k \times n}$ is a matrix that satisfies $$\norm{ \mtx{\Phi} \mtx{Q} \vct{u} }^2 \geq \alpha \cdot \norm{ \vct{u} }^2 \quad\text{for all $\vct{u} \in \R^d$.} %$$ When[eqn:subspace-inj] holds, we say that $\mtx{\Phi}$ is an $\alpha$-subspace injection for the $d$-dimensional range of $\mtx{Q}$ with embedding dimension $k$.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Subspace injections", "weight": 1.0} -->

If[eqn:subspace-inj] holds only when $\alpha = 0$, then $\mtx{\Phi}$ is not a subspace injection for $\mtx{Q}$.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Subspace injections", "weight": 1.0} -->

The subspace injection property [eqn:subspace-inj] has an equivalent \lambda_{\min}((\mtx{\Phi} \mtx{Q})^\transp (\mtx{\Phi} \mtx{Q})) \geq \alpha > 0.$$ Of course, a necessary condition for the subspace injection property[eqn:subspace-inj] or[eqn:subspace-inj-lmin] is that the embedding dimension exceeds the subspace dimension: $k \geq d$.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Subspace injections", "weight": 1.0} -->

We want to design subspace injections where the embedding dimension For an orthonormal matrix $\mtx{Q} \in \R^{n \times d}$, suppose that $\mtx{\Phi} \in \R^{k \times n}$ satisfies the two-sided bound $$\alpha \cdot \norm{ \vct{u} }^2 \leq \norm{ \mtx{\Phi Q} \vct{u} }^2 \leq \beta \cdot \norm{ \vct{u} }^2 \quad\text{for all $\vct{u} \in \R^d$.}$$ Then we say that $\mtx{\Phi}$ is an $(\alpha, \beta)$-subspace embedding for the range of $\mtx{Q}$. While it is critical that the contraction factor $\alpha > 0$, weak control on the ratio $\beta / \alpha$ suffices for most applications.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Randomized subspace injections", "weight": 1.0} -->

In many applications to computational linear algebra, we must construct a subspace injection without detailed knowledge of the fixed subspace We can achieve this goal by drawing the matrix $\mtx{\Phi}$ at random. isotropic random vector $\vct{\phi} \in \R^n$; that is, $\Expect[\vct{\phi} \vct{\phi}^\transp] = \Id_n$. The distribution of the random vector $\vct{\phi}$ is an algorithmic design choice.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Randomized subspace injections", "weight": 1.0} -->

For an embedding dimension $k$, construct the random matrix $$\mtx{\Phi} = \frac{1}{\sqrt{k}} \begin{bmatrix} \text{} & \vct{\phi}_1^\transp & \text{} \\\text{} & \vct{\phi}_k^\transp & \text{} \end{bmatrix} \quad\text{where $\vct{\phi}_i \sim \vct{\phi}$ iid.}$$ Since the rows are isotropic, the random matrix is an isometry on average: $$\Expect \norm{ \mtx{\Phi} \vct{u} }^2 = \norm{ \vct{u} }^2 \quad\text{for each $\vct{u} \in \R^n$.}$$ The normalization[eqn:subspace-isom] is chosen so that $\mtx{\Phi}$ typically has a contraction factor For a fixed subspace

<!-- chunk {"id": "body-0139", "role": "body", "section": "Randomized subspace injections", "weight": 1.0} -->

$\mtx{Q} \in \R^{d \times n}$ and embedding dimension $k$, we want to demonstrate that the random matrix $\mtx{\Phi}$ is a subspace injection for the range of $\mtx{Q}$ with high probability.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Randomized subspace injections", "weight": 1.0} -->

Quantitatively, we need to understand how the contraction factor $\alpha$ depends on the embedding dimension $k$. In view of[eqn:subspace-inj-lmin], it suffices to establish a lower bound on the minimum eigenvalue of the random psd matrix $$\mtx{Y} \coloneqq (\mtx{\Phi} \mtx{Q})^\transp (\mtx{\Phi} \mtx{Q}) = \frac{1}{k} \sum_{i=1}^k \mtx{Q}^\transp (\vct{\phi}_i \vct{\phi}_i^\transp) \mtx{Q}.$$ By the construction[eqn:iid-subspace-inj], the matrix $\mtx{Y}$ is a sum of iid random psd matrices, so we can activate our Gaussian comparison tools (thm:iid-intro).

<!-- chunk {"id": "body-0141", "role": "body", "section": "Sparse dimension reduction maps", "weight": 1.0} -->

In computational applications, it is desirable to employ very sparse random matrices While these maps are widely used[:Randomized-Numerical,MDM+23:Randomized-Numerical], no existing analysis justifies the typical parameter choices. We outline prior work in sec:subspace-prior.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Sparse dimension reduction maps", "weight": 1.0} -->

Choose an embedding dimension $k \geq d$, and fix the sparsity parameter $\zeta \in (0, k]$. Construct the random vector $$\vct{\phi}^\transp = \sqrt{\frac{k}{\smash{\zeta}}} \cdot \begin{bmatrix} \xi_1 \psi_1 & \hdots & \xi_n \psi_n \end{bmatrix} \in \R^n \quad\text{where}\quad &\text{$\xi_i \sim \bernoulli(\zeta / k)$ iid;} \\&\text{$\psi_i \sim \uniform\{\pm 1\}$ iid.} It is easy to verify that $\vct{\phi}$ is centered and Form the random matrix $\mtx{\Phi}$, as in[eqn:iid-subspace-inj].

<!-- chunk {"id": "body-0143", "role": "body", "section": "Sparse dimension reduction maps", "weight": 1.0} -->

Observe that $\mtx{\Phi}$ has an average of $\zeta$ nonzero entries per column, for a total of $\zeta n$ nonzero entries on average. We inquire when this sparse random matrix $\mtx{\Phi}$ serves as a subspace injection for a fixed subspace. To achieve an embedding dimension $k \asymp d$, what is the minimal sparsity $\zeta$?

<!-- chunk {"id": "body-0144", "role": "body", "section": "Sparse dimension reduction maps", "weight": 1.0} -->

The result depends on a geometric property of the subspace. of an orthonormal matrix $\mtx{Q} \in \R^{n \times d}$ via $$\mu(\mtx{Q}) \coloneqq \max\{ \normsq{ \mathbf{e}_i^\transp \mtx{Q} }: i = 1, \dots, n \}.$$ The coherence describes the alignment of the range of $\mtx{Q}$ with the standard coordinate basis $(\mathbf{e}_1, \dots, \mathbf{e}_n)$. It satisfies the inequalities $d/n \leq \mu(\mtx{Q}) \leq 1$.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Sparse dimension reduction maps", "weight": 1.0} -->

Fix an orthonormal matrix $\mtx{Q} \in \R^{n \times d}$ with coherence $\mu(\mtx{Q})$, defined in[eqn:coherence]. For parameters $\eps, \delta \in $, choose $$k \geq \frac{16 (d \vee 6 \log(2d/\delta))}{\eps^2} \qquad\text{and}\qquad \zeta \geq \frac{32 \mu(\mtx{Q}) \log(2d / \delta)}{\eps^2}.$$ Construct the sparse random matrix $\mtx{\Phi} \in \R^{k \times n}$ using[eqn:iid-subspace-inj] and[eqn:sparse-inj-vec]. Then $\mtx{\Phi}$ is a $(1-\eps)$-subspace injection for $\mtx{Q}$ with probability at least $1 - \delta$.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Sparse dimension reduction maps", "weight": 1.0} -->

The proof of thm:sparse-injection appears below in sec:sparse-inj-pf. It follows from a quick application of Gaussian comparison, in the same manner as the result for sparse sample covariance matrices (thm:sparse-cov). thm:sparse-injection has several attractive features. First, we have achieved the optimal embedding dimension $k \asymp d$. Second, the sparsity level $\zeta \lesssim \log d$ for every subspace, nearly matching known lower bounds for sparse subspace embeddings; see[eqn:nelson-nguyen] below. Third, the result shows that we can even reduce the sparsity for subspaces with small coherence. The ultimate limit, for a minimally coherent subspace, is $\zeta \gtrsim (d \log d) / n$, which allows for a random subspace injection with just $\mathcal{O}(d \log d)$ nonzero entries.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Sparse dimension reduction maps", "weight": 1.0} -->

Further improvements to the sparsity are only possible for special subspaces (e.g., when the rows of $\mtx{Q}$compose a complex projective 2-design).

<!-- chunk {"id": "body-0148", "role": "body", "section": "Sparse dimension reduction maps", "weight": 1.0} -->

For a sparse random matrix with iid entries, the $\eps^{-2}$ dependence in the embedding dimension $k$ and the sparsity $\zeta$ seems to be For most applications, the parameter $\eps$ is a constant (say, $\eps = 1/2$), so the poor scaling in $\eps$ is not a significant concern. In contrast, the subspace dimension $d$ can be quite large, so it is essential to obtain the minimal dependence on $d$.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Sparse dimension reduction maps", "weight": 1.0} -->

To verify the subspace embedding property (rem:subspace-embedding) of the iid sparse random matrix $\mtx{\Phi}$ in thm:sparse-injection, we can easily obtain adequate upper bounds for the dilation factor $\beta$.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Prior work and discussion", "weight": 1.0} -->

os[:Improved-Approximation] introduced the definition of a subspace embedding (rem:subspace-embedding). Clarkson & Woodruff[:Low-Rank-Approximation] proposed the first construction of a sparse subspace embedding. Soon after, Nelson & Nguyen[:OSNAP-Faster] identified more effective constructions, including the iid entry model in thm:sparse-injection and a related model, called a fixed-sparsity subspace embedding, that has exactly $\zeta$ nonzero entries per column. There are several variants of these sparse subspace embeddings, which offer slightly different advantages and disadvantages. For brevity, we summarize results without listing the details of the embedding constructions.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Prior work and discussion", "weight": 1.0} -->

What are the opportunities for and limitations on sparse subspace embeddings? For any fixed-sparsity subspace embedding with conditioning ratio $\beta / \alpha \eqqcolon 1 + \eps$, Nelson & Nguyen[:Lower-Bounds] established lower bounds for the parameters: \quad\text{and}\quad \zeta \gtrsim (\log d) / (\eps \log \log d).$$ Bourgain et al.[:Toward-Unified] obtained upper bounds for the parameters of sparse subspace embeddings that identified the role of the coherence statistic $\mu(\mtx{Q})$.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Prior work and discussion", "weight": 1.0} -->

Using matrix concentration tools, Cohen[:Nearly-Tight-Oblivious] obtained upper bounds for fixed-sparsity subspace embeddings: $$k \lesssim (d \log d) / \eps^2 \quad\text{and}\quad \zeta \lesssim (\log d) / \eps.$$ For a long time, Cohen's analysis was the best available, and it has remained a vexing problem to obtain an upper bound that matches the minimal dependence[eqn:nelson-nguyen].

<!-- chunk {"id": "body-0153", "role": "body", "section": "Prior work and discussion", "weight": 1.0} -->

In applications, constants and logarithms are important. Based on computer experiments, Tropp et al. recommended the following parameter settings for fixed-sparsity subspace embeddings: \quad\text{and}\quad These parameters work well, but they lack theoretical justification. Regardless, fixed-sparsity subspace embeddings are widely used in computational linear algebra[:Randomized-Numerical,MDM+23:Randomized-Numerical].

<!-- chunk {"id": "body-0154", "role": "body", "section": "Prior work and discussion", "weight": 1.0} -->

The last few years have witnessed a burst of new theoretical activity. [:Hashing-Embeddings] established upper bounds that improve over the Bourgain et al.result for subspaces with sufficiently Chennakod et al.[:Optimal-Embedding] removed the $\log d$ factor from the embedding dimension $k$ at the cost of higher sparsity $\zeta$ by invoking results of Brailovskaya & van Handel[:Universality-Sharp]. In the last few months, Chennakod et al.[:Optimal-Oblivious] made further improvements to their arguments, reaching the following guarantee for fixed-sparsity \quad\text{and}\quad \zeta \lesssim \log^2(d/\eps) / \eps + \log^3(d / \eps).$$ The latter result is the state of the art. While the embedding dimension $k$ has the optimal form, the excess logarithmic factors in the sparsity $\zeta$ remain a serious limitation.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Prior work and discussion", "weight": 1.0} -->

As outlined, the prior work has focused on sparse subspace (rem:subspace-embedding), rather than sparse subspace injections Nevertheless, the injection property is by far the more important feature, both in theory and in practice; see[:Universality-Laws] or[:Randomized-Numerical]. Our result (thm:sparse-injection) is the first to prove that sparse random matrices serve as subspace injections with (essentially) the minimal dependence[eqn:nelson-nguyen] on the subspace dimension $d$ in both the embedding dimension $k$ and the sparsity $\zeta$. The plain role of the subspace coherence $\mu(\mtx{Q})$is an added bonus.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Prior work and discussion", "weight": 1.0} -->

We have treated the simplest model for a sparse subspace injection, where the random matrix $\mtx{\Phi}$ has iid entries. The Gaussian comparison theorem also allows us to study the injection properties of a certain class of fixed-sparsity random matrices[:Optimal-Oblivious]. To obtain a $(1-\eps)$-subspace injection, it is sufficient that \qquad\text{and}\quad \zeta \lesssim (\log d) / \eps^2.$$ As compared with thm:sparse-injection, the subspace coherence $\mu(\mtx{Q})$ does not appear in this result. As compared with Chennakod et al.[:Optimal-Oblivious], we have reduced the dependence on $\log d$ significantly, at the cost of a worse dependence on $\eps$.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Gaussian comparison: Positive scalar sums", "weight": 1.0} -->

The technical development commences in this section. As a warmup, we develop a proof of the lower tail bound for an independent sum of positive scalar random variables.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Gaussian comparison: Positive scalar sums", "weight": 1.0} -->

Consider an independent family $(W_1, \dots, W_n)$ of nonnegative, square-integrable, real random variables: $W_i \geq 0$ and $\Expect W_i^2 < + \infty$.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Gaussian comparison: Positive scalar sums", "weight": 1.0} -->

Introduce the sum of the random variables, along with the sum of second moments: \quad\text{and}\quad L_2 \coloneqq \sum_{i=1}^n \Expect W_i^2.$$ Then the lower tail of the sum $X$ satisfies $$\Prob{ X \leq \Expect X - t } \leq \econst^{-t^2 / (2L_2)} \quad\text{for all $t \geq 0$.}$$ Introduce the mgf of the lower tail of the centered sum: $$\mgf_X(\theta) \coloneqq \Expect \econst^{ - \theta (X - \Expect X)} \quad\text{for $\theta \geq 0$.}$$ prop:scalar-mgf, below, states that $\log \mgf_X(\theta) \leq \theta^2 L_2/2$ for all $\theta \geq 0$.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Gaussian comparison: Positive scalar sums", "weight": 1.0} -->

The Laplace transform method[:Concentration-Inequalities] yields the tail bound $$\Prob{ X - \Expect X \leq -t } \leq \inf\nolimits_{\theta > 0} \econst^{-\theta t + \log \mgf_X(\theta)} \leq \inf\nolimits_{\theta > 0} \econst^{-\theta t + \theta^2 L_2 / 2} The infimum is attained when $\theta = t / L_2$. thm:positive-sum depends on a bound for $\mgf_X$, defined in[eqn:scalar-mgf]. Although this bound is classic and rather elementary[:Concentration-Inequalities], we will develop an alternative treatment that has more potential for generalization. The results in this section will reappear in the proof of the matrix

<!-- chunk {"id": "body-0161", "role": "body", "section": "Completely monotone functions", "weight": 1.0} -->

Our approach takes advantage of a special feature of the decaying exponential that is encapsulated in the next definition.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Completely monotone functions", "weight": 1.0} -->

A function $f: \set{I} \to \R$ on the interval $\set{I} \subseteq \R$ is completely monotone to order $K$ when its first $K$ derivatives exist and alternate sign: \quad\text{for all $w \in \set{I}$ and each $k = 0, 1, 2, \dots, K$.}$$ If the interval $\set{I}$ includes an endpoint, the derivatives at the endpoint are interpreted as one-sided derivatives. The function $f$ is completely monotone when[eqn:cm] holds for each $K \in \N$.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Completely monotone functions", "weight": 1.0} -->

The fundamental example of a completely monotone function is a For fixed $\theta \geq 0$ and variable $w \in \R$, the function $$w \mapsto \econst^{-\theta w} \quad\text{is completely monotone for $w \in \R$.}$$ In fact, a function $f: \R_{+} \to \R$ on the nonnegative real line is completely monotone if and only if it is the Laplace transform of a finite, positive Borel measure $\mu$: $$f(w) = \int_{[0,\infty)} \econst^{-\theta w} \, \mu(\diff{\theta}).

<!-- chunk {"id": "body-0164", "role": "body", "section": "Completely monotone functions", "weight": 1.0} -->

The representation[eqn:bernstein] is called Bernstein's theorem[:Laplace-Transform].

<!-- chunk {"id": "body-0165", "role": "body", "section": "Completely monotone functions", "weight": 1.0} -->

Completely monotone functions support a beautiful theory, elaborated in the classic book of Widder The monograph of Schilling et al.[:Bernstein-Functions-2ed]is a more recent reference. This background is not required for our

<!-- chunk {"id": "body-0166", "role": "body", "section": "Tools from Stein's method", "weight": 1.0} -->

The main steps in the analysis are adapted from the literature on Charles Stein's method, a collection of tools for establishing distributional approximations and concentration inequalities.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Tools from Stein's method", "weight": 1.0} -->

This section outlines some ideas from Stein's method. See the survey of Ross[:Fundamentals-Steins] or the book of Chen et al.[:Normal-Approximation]for more information.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Tools from Stein's method", "weight": 1.0} -->

To describe the variability in a distribution, we can employ exchangeable pairs of random variables. $(W, Y)$ of real random variables is exchangeable when for every bivariate function $F: \R \times \R \to \R$where the expectation exists. A pair of iid random variables is the most basic example of an exchangeable pair.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Tools from Stein's method", "weight": 1.0} -->

The next ingredient is an elegant covariance identity. $g, h: \set{I} \to \R$ be functions on the interval $\set{I} \subseteq \R$. For an iid pair $(W,Y)$ of random variables taking values in $\set{I}$, = \frac{1}{2} \Expect\big[(g(W) - g(Y))(h(W) - h(Y)) \big].$$ This formula can be verified by direct calculation. It is valid whenever the expectations are finite.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Tools from Stein's method", "weight": 1.0} -->

To bound differences of function values, as in we employ a formula of Hermite. For a continuously differentiable function $h: \set{I} \to \R$, $$\frac{h(w) - h(y)}{w-y} = \int_0^1 h'(\tau w + (1 - \tau) y) \idiff{\tau} \quad\text{for all $w, y \in \set{I}$.}$$ Identity[eqn:hermite] follows from the fundamental theorem of calculus. Moreover, if $h'$ is convex on $\set{I}$, then \quad\text{for all $w, y \in \set{I}$.}$$ When $w = y$ in[eqn:hermite] or[eqn:hermite-cvx], we interpret the left-hand side as $h'(w)$.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Tools from Stein's method", "weight": 1.0} -->

The most important element in our proof of for functions with opposite sense[:Concentration-Inequalities]. Assume that $g: \set{I} \to \R$ is increasing, while $h: \set{I} \to \R$ is decreasing. For any random variable $W$ taking values in $\set{I}$, $$\Expect[g(W) h(W)] \leq \Expect[g(W)] \cdot \Expect[h(W)].$$ Equivalently, the covariance of $g(W)$ and $h(W)$ is negative. To establish the result[eqn:neg-assoc], note that \quad\text{for all $s, t \in \set{I}$.}$$ Combine this formula with the covariance identity[eqn:cov-exch].

<!-- chunk {"id": "body-0172", "role": "body", "section": "Covariance bounds for completely monotone functions", "weight": 1.0} -->

This section shows how the tools from Stein's method lead to clean bounds for covariances involving a completely monotone function. In particular, this argument applies to the mgf of the lower tail.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Covariance bounds for completely monotone functions", "weight": 1.0} -->

Let $f: \R_+ \to \R$ be a function on the nonnegative real line that is completely monotone to order four. For each nonnegative real random variable $W$, $$\Cov(W, f'(W)) = \Expect\big[(W - \Expect W) f'(W) \big] \leq \Expect[W^2] \cdot \Expect[f''(W)].$$ The bound is valid when the expectations are finite.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Covariance bounds for completely monotone functions", "weight": 1.0} -->

According to def:cm, the derivatives of a completely monotone function $f$ alternate sign. We only rely on the conditions that $f''$is positive, decreasing, and convex, so complete monotonicity to order four is sufficient. $Y$ be an independent copy of $W$. By the exchangeable pairs formula[eqn:cov-exch], \Cov(W, f'(W)) &= \frac{1}{2} \Expect\big[(W - Y)(f'(W) - f'(Y)) \big] \\&\leq \frac{1}{4} \Expect \big[(W - Y)^2 (f''(W) + f''(Y)) \big] = \frac{1}{2} \Expect \big[(W - Y)^2 f''(W) \big].

<!-- chunk {"id": "body-0175", "role": "body", "section": "Covariance bounds for completely monotone functions", "weight": 1.0} -->

The inequality is the bound[eqn:hermite-cvx] for the divided difference of the function $f'$, whose derivative $f''$ is convex. In the last step, we have used the exchangeability[eqn:exch] of $(W, Y)$to simplify the expression.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Covariance bounds for completely monotone functions", "weight": 1.0} -->

To continue, let us separate the two factors in the expectation. $(w - y)^2 \leq w^2 + y^2$ for $w, y \geq 0$.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Covariance bounds for completely monotone functions", "weight": 1.0} -->

$$\Cov(W, f'(W)) \leq \frac{1}{2} \Expect\big[(W^2 + Y^2) f''(W) \big] \leq \frac{1}{2} \Expect[W^2 f''(W)] + \frac{1}{2} \Expect[W^2] \cdot \Expect[f''(W)].$$ The second step relies on the independence and identical distribution of $(W,Y)$. On the nonnegative real line $\R_+$, the function $w \mapsto w^2$ is increasing, while $f''$ is decreasing. Thus, the association inequality[eqn:neg-assoc] furnishes a bound for the first expectation on the right-hand side: $$\Expect[W^2 f''(W)] \leq \Expect[W^2] \cdot \Expect[f''(W)].$$ Combine the last two displays to arrive at the advertised result.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Covariance bounds for completely monotone functions", "weight": 1.0} -->

[lem:cov-cm] depends crucially on the assumption that $f'''$ is negative, which allows us to invoke the association inequality[eqn:neg-assoc] to decouple $W^2$ from $f''(W)$. The entropy method employs association inequalities in a similar fashion; for instance, see[:Concentration-Inequalities]. The overall structure of the proof is similar with classic arguments from Stein's method, exemplified in[:Steins-Method].

<!-- chunk {"id": "body-0179", "role": "body", "section": "Positive sum: mgf bound", "weight": 1.0} -->

lem:cov-cmat hand, we quickly obtain a bound for the mgf of a sum of independent, nonnegative random variables.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Positive sum: mgf bound", "weight": 1.0} -->

Instate the hypotheses of thm:positive-sum. The mgf[eqn:scalar-mgf] satisfies the bound $$\log \mgf_X(\theta) \leq % \quad\text{for all $\theta \geq 0$.}$$ We can rewrite the outcome of prop:scalar-mgf in a more suggestive fashion: $$\Expect \econst^{-\theta X} \leq \Expect \econst^{-\theta Z} \quad\text{where $Z \sim \normal(\Expect X, L_2)$.}$$ In other words, we have compared the lower tail of the sum $X$ with the lower tail of an appropriate normal random variable $Z$ whose statistics derive from the summands in $X$. In sec:psd-weights, we will see that the inequality[eqn:scalar-mgf-normal]generalizes to matrices.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Positive sum: mgf bound", "weight": 1.0} -->

Recall the definition[eqn:scalar-mgf] of $\mgf_X(\theta)$. Since $\log \mgf_{X} = 0$, the result holds for $\theta = 0$, and we may assume that $\theta > 0$. The derivative of the mgf takes the form \mgf'_X(\theta) &= - \Expect\big[(X - \Expect X) \econst^{-\theta(X - \Expect X)} \big] \\&= - \sum_{i=1}^n \Expect\big[(W_i - \Expect W_i) \econst^{-\theta(X - \Expect X)} \big] \eqqcolon - \sum_{i=1}^n \Expect \big[(W_i - \Expect W_i) \econst^{\theta B_i - \theta W_i} \big].

<!-- chunk {"id": "body-0182", "role": "body", "section": "Positive sum: mgf bound", "weight": 1.0} -->

The second relation expands the sum $X - \Expect X = \sum_{i=1}^n (W_i - \Expect W_i)$. Note that the random variable $B_i \coloneqq W_i - (X - \Expect X)$ is statistically independent $B_i$, applylem:cov-cm to the completely monotone function $f_i(w) \coloneqq \econst^{\theta B_i - \theta w}$. This step results in the bound \mgf'_X(\theta) &\leq \theta \sum_{i=1}^n \Expect[W_i^2] \cdot \Expect[\econst^{\theta B_i - \theta W_i}] \\&= \theta \sum_{i=1}^n \Expect[W_i^2] \cdot \Expect[\econst^{-\theta(X - \Expect X)}] = \theta L_2 \cdot \mgf_X(\theta).

<!-- chunk {"id": "body-0183", "role": "body", "section": "Positive sum: mgf bound", "weight": 1.0} -->

Solve the differential inequality to complete the proof.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Gaussian comparison: Randomly weighted sums of psd matrices", "weight": 1.0} -->

In this section, we turn to the proof of which provides a bound for the minimum eigenvalue of a randomly weighted sum of fixed psd matrices. For technical reasons, we develop the result using slightly different notation and assumptions. $(\mtx{A}_1, \dots, \mtx{A}_n)$ of psd matrices, with common dimension $d$. These matrices need not be distinct from each other. Consider an independent family $(W_1, \dots, W_n)$ of square-integrable, nonnegative real random variables: $W_i \geq 0$ and $\Expect W_i^2 < + \infty$. Form the random psd matrix $$\mtx{X} \coloneqq \sum_{i=1}^n W_i \mtx{A}_i.$$ We will compare the random psd matrix $\mtx{X}$ with an appropriate Gaussian model.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Gaussian comparison: Randomly weighted sums of psd matrices", "weight": 1.0} -->

Fix an arbitrary self-adjoint matrix $\mtx{\Delta} \in \Sym_d$. Introduce the random $d$-dimensional matrices $\mtx{X}$ and $\mtx{Z}$ from[eqn:psd-weight] and [eqn:psd-weight-gauss].

<!-- chunk {"id": "body-0186", "role": "body", "section": "Gaussian comparison: Randomly weighted sums of psd matrices", "weight": 1.0} -->

thm:psd-weights generalizes thm:sampling-intro from the introduction by allowing a shift $\mtx{\Delta}$of the expectation. This improvement comes for free and allows for a more transparent and natural argument.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Gaussian comparison: Randomly weighted sums of psd matrices", "weight": 1.0} -->

prop:psd-weight-mgf, below, provides a comparison for the trace mgfs: $$\mgf_{\mtx{X}}(\theta) \coloneqq \Expect \trace \econst^{-\theta (\mtx{X} - \Expect \mtx{X} + \mtx{\Delta})} \leq \Expect \trace \econst^{- \theta (\mtx{Z} + \mtx{\Delta})} \quad\text{for $\theta \geq 0$.}$$ Bound the trace exponential on the right-hand side in terms of the minimum eigenvalue: $$\mgf_{\mtx{X}}(\theta) \leq d \cdot \Expect \lambda_{\max}\big(\econst^{- \theta (\mtx{Z} + \mtx{\Delta})} \big) = d \cdot \Expect \econst^{-\theta \lambda_{\min}(\mtx{Z} +

<!-- chunk {"id": "body-0188", "role": "body", "section": "Gaussian comparison: Randomly weighted sums of psd matrices", "weight": 1.0} -->

\mtx{\Delta})}.$$ Indeed, the trace of a psd matrix does not exceed the dimension times the maximum eigenvalue. The second relation is the spectral mapping theorem, combined with the fact that the decreasing exponential function reverses the order of the eigenvalues.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Gaussian comparison: Randomly weighted sums of psd matrices", "weight": 1.0} -->

The Gaussian concentration inequality[eqn:gauss-lip-mgf] controls the fluctuations of the minimum eigenvalue $\lambda_{\min}(\mtx{Z} + \mtx{\Delta})$ around its mean: $$\mgf_{\mtx{X}}(\theta) \leq d \cdot \econst^{-\theta \Expect \lambda_{\min}(\mtx{Z} + \mtx{\Delta})} \cdot \econst^{\theta^2 \sigma_*^2(\mtx{Z}) / 2}.$$ The inequality[eqn:psd-weight-mgf-pf]quickly leads to both the stated results.

<!-- chunk {"id": "body-0190", "role": "body", "section": "Gaussian comparison: Randomly weighted sums of psd matrices", "weight": 1.0} -->

To obtain the probability bound we employ the matrix Laplace transform method[:Introduction-Matrix]. For fixed $t \geq 0$ and arbitrary $\theta > 0$, \Prob{ \lambda_{\min}(\mtx{X} - \Expect \mtx{X} + \mtx{\Delta}) \leq \Expect \lambda_{\min}(\mtx{Z} + \mtx{\Delta}) - t } &\leq \econst^{\theta (\Expect \lambda_{\min}(\mtx{Z} + \mtx{\Delta}) - t)} \cdot \mgf_{\mtx{X}}(\theta) \\&\leq d \cdot \econst^{-\theta t} \cdot \econst^{\theta^2 \sigma_*^2(\mtx{Z}) / 2}.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Gaussian comparison: Randomly weighted sums of psd matrices", "weight": 1.0} -->

The second inequality is[eqn:psd-weight-mgf-pf]. Select $\theta = t / \sigma_*^2(\mtx{Z})$to reach the probability inequality. [eqn:psd-weight-expect] for the expectation follows from a similar argument. For arbitrary $\theta > 0$, the matrix Laplace transform \Expect \lambda_{\min}(\mtx{X} - \Expect \mtx{X} - \mtx{\Delta}) &\geq -\frac{1}{\theta} \log \mgf_{\mtx{X}}(\theta) \\&\geq - \frac{1}{\theta} \left[\log d - \theta \Expect \lambda_{\min}(\mtx{Z} + \mtx{\Delta}) + \theta^2 \sigma_*^2(\mtx{Z}) / 2 \right].

<!-- chunk {"id": "body-0192", "role": "body", "section": "Gaussian comparison: Randomly weighted sums of psd matrices", "weight": 1.0} -->

The second inequality is[eqn:psd-weight-mgf-pf]. Choose $\theta = \sqrt{ (2 \log d) / \sigma_*^2(\mtx{Z}) }$ to reach the expectation bound.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Gaussian comparison: Randomly weighted sums of psd matrices", "weight": 1.0} -->

Choose the shift $\mtx{\Delta} = \Expect \mtx{X}$, and define the Gaussian matrix $\mtx{Z}' \coloneqq \mtx{Z} + \Expect \mtx{X} \sim \normal(\Expect \mtx{X}, \mathsf{V})$, where $\mathsf{V}$ is defined in[eqn:psd-weight-covar]. Change variables to state thm:sampling-intro directly in terms of the distribution of $\mtx{Z}'$.

<!-- chunk {"id": "body-0194", "role": "body", "section": "Stahl's theorem: Complete monotonicity of the trace exponential", "weight": 1.0} -->

thm:psd-weights, we extend the considerations behind the scalar comparison (thm:positive-sum) to the matrix setting. This strategy depends on a profound fact from matrix analysis, called Stahl's theorem[:Proof-BMV]. [Stahl's theorem; formerly the BMV conjecture] Fix self-adjoint matrices $\mtx{A}, \mtx{B} \in \Sym_d$, and assume that $\mtx{A}$ is psd. Then the trace exponential function $$f(w) \coloneqq \trace \exp(\mtx{B} - w \mtx{A}) \quad\text{is completely monotone for $w \geq 0$.}$$ In particular, lem:cov-cm applies to the function $f$.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Stahl's theorem: Complete monotonicity of the trace exponential", "weight": 1.0} -->

While Stahl's theorem is recent, it has a remarkable history. conjectured fact:bmv as part of their method for bounding partition functions of quantum mechanical systems. They established the result in two special cases: when $\mtx{A}, \mtx{B}$ commute; or when $\mtx{A}, \mtx{B}$ are $2 \times 2$matrices. Over the next decades, the BMV conjecture received significant attention in mathematical physics, but it was not resolved. proved that fact:bmv admits an equivalent formulation: For all psd $\mtx{A}, \mtx{B} \in \Sym_d$, the coefficients of the polynomial $w \mapsto \trace{} (w \mtx{A} + \mtx{B})^p$ are nonnegative for all $p \in \N$. This link with real algebraic geometry ignited a new stage of research, based on sum-of-squares hierarchies and semidefinite programming, that generated new evidence supporting the BMV conjecture.

<!-- chunk {"id": "body-0196", "role": "body", "section": "Stahl's theorem: Complete monotonicity of the trace exponential", "weight": 1.0} -->

Finally, in 2012, Herbert Stahl established fact:bmv using classic methods from complex analysis. Bernstein's theorem[eqn:bernstein] states that a completely monotone function is the Laplace transform of a finite, positive Borel measure. Roughly speaking, Stahl inverted the Laplace transform to obtain the representing measure. To prove that the representing measure is positive, he exploited the theory of Riemann surfaces. See[:Herbert-Stahls]for another account of Very recently, Otte Hein avaara constructed a rather different argument[:Tracial-Joint] that leads to a remarkable generalization of fact:bmv: Fix self-adjoint matrices $\mtx{A}, \mtx{B} \in \Sym_d$, and assume that $\mtx{A}$ is psd. Consider a function $h: \R \to \R$ that is completely monotone to order $K$.

<!-- chunk {"id": "body-0197", "role": "body", "section": "Stahl's theorem: Complete monotonicity of the trace exponential", "weight": 1.0} -->

Then the trace function $$f(w) \coloneqq \trace h(w \mtx{A} - \mtx{B}) \quad\text{is completely monotone to order $K$ for $w \in \R$.}$$ Stahl's theorem (fact:bmv) follows from the choice $h(w) = \econst^{-w}$.

<!-- chunk {"id": "body-0198", "role": "body", "section": "Stahl's theorem: Complete monotonicity of the trace exponential", "weight": 1.0} -->

Heinavaara's proof of fact:heina appeals to a novel object, called a tracial joint spectral measure, that captures the behavior of trace functions of the form $(w,y) \mapsto \trace h(w \mtx{A} + y \mtx{B})$ for self-adjoint $\mtx{A}, \mtx{B}$. His techniques yield many deep new statements about trace functions.

<!-- chunk {"id": "body-0199", "role": "body", "section": "Additional tools", "weight": 1.0} -->

The argument involves some standard tools from probability and matrix analysis. First, we record the Gaussian integration by parts (IBP) rule Consider iid real standard normal variables $(\gamma_1, \dots, \gamma_n)$. For each differentiable function $h: \R^n \to \R$, $$\Expect\big[\gamma_i \cdot h(\gamma_1, \dots, \gamma_n) \big] = \Expect\big[(\partial_i h)(\gamma_1, \dots, \gamma_n) \big].$$ In this formula, $\partial_i h$ denotes the partial derivative of $h$ with respect to its $i$th argument. The identity is valid whenever the right-hand side is finite. we recall a classic formula from matrix calculus[:Matrix-Analysis].

<!-- chunk {"id": "body-0200", "role": "body", "section": "Additional tools", "weight": 1.0} -->

\trace\big[\mtx{H} \econst^{\mtx{A}} \big].$$ The statement[eqn:d-trexp] follows from[eqn:d-exp]when we take the trace and cycle to combine the exponentials.

<!-- chunk {"id": "body-0201", "role": "body", "section": "Comparison for the trace mgf", "weight": 1.0} -->

With Stahl's theorem (fact:bmv) at hand, we can establish a bound for the trace mgf associated with the minimum eigenvalue of a random psd matrix.

<!-- chunk {"id": "body-0202", "role": "body", "section": "Comparison for the trace mgf", "weight": 1.0} -->

Instate the hypotheses of thm:psd-weights. For $\theta \geq 0$, $$\mgf_{\mtx{X}}(\theta) \coloneqq \Expect \trace \econst^{-\theta(\mtx{X} - \Expect \mtx{X} + \mtx{\Delta})} \leq \Expect \trace \econst^{-\theta(\mtx{Z} + \mtx{\Delta})} \eqqcolon \mgf_{\mtx{Z}}(\theta).$$ In the scalar setting (the mgf of a Gaussian random variable emerges from a direct argument. In the matrix setting, it is more expedient to compare the trace mgf of the psd model with the trace mgf of the Gaussian model. This argument relies on interpolation, much like classic Gaussian comparison inequalities[:Inegalite-Type] or more recent work on universality for random matrices[:Universality-Sharp].

<!-- chunk {"id": "body-0203", "role": "body", "section": "Comparison for the trace mgf", "weight": 1.0} -->

To implement the comparison, we interpolate between the two random matrix models. Define a path in the space of random matrices: $$\mtx{Y}_s \coloneqq \sqrt{s}\, (\mtx{X} - \Expect \mtx{X}) + \sqrt{1-s} \, \mtx{Z} + \mtx{\Delta} \quad\text{for $s \in $.}$$ Introduce the trace mgf of the interpolants: $$u(s) \coloneqq \Expect \trace \econst^{-\theta \mtx{Y}_s} \quad\text{for $s \in $.}$$ Note that $u = \mgf_{\mtx{Z}}(\theta)$ and $u = \mgf_{\mtx{X}}(\theta)$. We claim that the derivative $u'(s) \leq 0$ for $s \in $. Once this point is settled, prop:scalar-mgffollows inexorably.

<!-- chunk {"id": "body-0204", "role": "body", "section": "Comparison for the trace mgf", "weight": 1.0} -->

By a scaling argument, we can assume that $\theta = 1$. Now, for fixed $s \in $, the derivative $u'(s)$ along the interpolation path takes the form $$u'(s) = \frac{-1}{2\sqrt{s}} \Expect \trace \big[(\mtx{X} - \Expect \mtx{X}) \econst^{-\mtx{Y}_s} \big] - \frac{-1}{2\sqrt{1 - s}} \Expect \trace \big[\mtx{Z} \econst^{-\mtx{Y}_s} \big] \eqqcolon \onecirc - \twocirc.$$ We start with the second term $\twocirc$, involving the Gaussian random matrix, as it offers a template for how to bound the first term $\onecirc$.

<!-- chunk {"id": "body-0205", "role": "body", "section": "Comparison for the trace mgf", "weight": 1.0} -->

The second line is the Gaussian IBP rule (fact:gauss-ibp). This calculation relies on the formula[eqn:d-exp] for the derivative of the matrix exponential. The partial derivative $\partial_{\gamma_i} \mtx{Y}_s = \sqrt{1 - s} \, \mtx{H}_i$, owing to the expressions[eqn:mtx-path] for $\mtx{Y}_s$ and[eqn:psd-weight-gauss] for $\mtx{Z}$. For the last step, recall the definition[eqn:psd-weight-system] of the matrix coefficients $\mtx{H}_i$.

<!-- chunk {"id": "body-0206", "role": "body", "section": "Comparison for the trace mgf", "weight": 1.0} -->

For each index $i$, we have defined the random matrix $\mtx{B}_i \coloneqq \sqrt{s} W_i \mtx{A}_i - \mtx{Y}_s$. Observe that $\mtx{B}_i$ is statistically independent from the random variable $W_i$. $\mtx{B}_i$, introduce the (deterministic) function $$f_i(w) \coloneqq \trace \econst^{\mtx{B}_i - \sqrt{s} w \mtx{A}_i} \quad\text{for $w \geq 0$ and $i = 1, \dots, n$.}$$ Stahl's theorem (fact:bmv) asserts that each $f_i$ is completely monotone for fixed self-adjoint $\mtx{A}_i, \mtx{B}_i$ with $\mtx{A}_i$ psd.

<!-- chunk {"id": "body-0207", "role": "body", "section": "Comparison for the trace mgf", "weight": 1.0} -->

The last line depends on the relations $\mtx{B}_i - \sqrt{s} W_i \mtx{A}_i = - \mtx{Y}_s$. As promised, $u'(s) = \onecirc - \twocirc \leq 0$.

<!-- chunk {"id": "body-0208", "role": "body", "section": "Extension: Polynomial moments", "weight": 1.0} -->

prop:psd-weight-mgfcan be adapted to obtain a comparison theorem for one-sided polynomial moments.

<!-- chunk {"id": "body-0209", "role": "body", "section": "Extension: Polynomial moments", "weight": 1.0} -->

Instate the hypotheses of thm:psd-weights. For each $p \geq 4$, $$\Expect \trace{} (\mtx{X} - \Expect \mtx{X} + \mtx{\Delta})_-^p \leq \Expect \trace{} (\mtx{Z} + \mtx{\Delta})_-^p.$$ As usual, the negative part $(a)_{-} \coloneqq \max\{-a, 0\}$ for $a \in \R$ binds before the power.

<!-- chunk {"id": "body-0210", "role": "body", "section": "Extension: Polynomial moments", "weight": 1.0} -->

The structure of the argument is identical with the proof ofprop:psd-weight-mgf. For justification, when $p \geq 4$, note that $h: w \mapsto (w)_-^p$ is completely monotone to order four on the real line. Heinevaara's theorem (fact:heina) ensures that the associated trace function $f(w) \coloneqq \trace{} (w\mtx{A} - \mtx{B})_{-}^p$ is also completely monotone to order four. Therefore, we can activate lem:cov-cm.

<!-- chunk {"id": "body-0211", "role": "body", "section": "Extension: Polynomial moments", "weight": 1.0} -->

While it is not really necessary to compute the derivatives of the trace function one may employ the Dalecki\iKre\in formula[:Matrix-Analysis] to obtain the detailed expressions.

<!-- chunk {"id": "body-0212", "role": "body", "section": "Gaussian comparison: Sum of iid random psd matrices", "weight": 1.0} -->

This section develops a comparison theorem for the minimum iid random psd matrices. This formulation includes covariance matrices and related models. Surprisingly, this result is a consequence of the comparison (thm:psd-weights) for sums of randomly weighted psd matrices. $\mtx{W}$ be a random psd matrix with dimension $d$. Assume that $\mtx{W}$ is square-integrable: $\Expect \norm{\mtx{W}}^2 < + \infty$. For a fixed natural number $k \in \N$, consider the random psd matrix $\mtx{Y}$ obtained by adding $k$ independent copies of $\mtx{W}$. That is, $$\mtx{Y} \coloneqq \sum_{j=1}^k \mtx{W}_j \quad\text{where $\mtx{W}_j \sim \mtx{W}$ iid.}$$ We compare the random psd matrix $\mtx{Y}$ with an appropriate Gaussian model.

<!-- chunk {"id": "body-0213", "role": "body", "section": "Gaussian comparison: Sum of iid random psd matrices", "weight": 1.0} -->

Consider a centered Gaussian matrix that follows the distribution $$\mtx{Z} \sim \normal(\mtx{0}, \mathsf{V}) \quad\text{where}\quad \mathsf{V} \coloneqq k \cdot \Mo[\mtx{W}].$$ With these definitions, we can state another comparison theorem.

<!-- chunk {"id": "body-0214", "role": "body", "section": "Gaussian comparison: Sum of iid random psd matrices", "weight": 1.0} -->

Fix an arbitrary self-adjoint matrix $\mtx{\Delta} \in \Sym_d$. Introduce the random $d$-dimensional matrices $\mtx{Y}$ and $\mtx{Z}$ from[eqn:iid-sum] and[eqn:iid-gauss].

<!-- chunk {"id": "body-0215", "role": "body", "section": "Gaussian comparison: Sum of iid random psd matrices", "weight": 1.0} -->

The content of the argument is a comparison inequality for the trace mgfs: $$\mgf_{\mtx{Y}}(\theta) \coloneqq \Expect \trace \econst^{- \theta (\mtx{Y} - \Expect \mtx{Y} + \mtx{\Delta})} \leq 2 \Expect \trace \econst^{-\theta (\mtx{Z} + \mtx{\Delta})} \quad\text{for $\theta \geq 0$.}$$ See[eqn:iid-mgf-pf] below. The rest of the argument follows the same route as the proof ofthm:psd-weights.

<!-- chunk {"id": "body-0216", "role": "body", "section": "Gaussian comparison: Sum of iid random psd matrices", "weight": 1.0} -->

To derive the result in the introduction, we choose the shift $\mtx{\Delta} = \Expect \mtx{Y}$, and we employ monotonicity properties of the Gaussian distribution to relax the assumption on the variance function.

<!-- chunk {"id": "body-0217", "role": "body", "section": "Gaussian comparison: Sum of iid random psd matrices", "weight": 1.0} -->

Here are the details. Construct the Gaussian distribution $\mtx{Z}' \sim \normal(\mtx{\Delta}, \mathsf{V}')$ where $\mtx{\Delta} = \Expect \mtx{Y} $ and the variance function $\mathsf{V}' \geq \mathsf{V} = k \cdot \Mo[\mtx{W}]$.

<!-- chunk {"id": "body-0218", "role": "body", "section": "Gaussian comparison: Sum of iid random psd matrices", "weight": 1.0} -->

Invoke thm:iid-sum with the centered Gaussian matrix $\mtx{Z} \sim \normal(\mtx{0}, \mathsf{V})$ to obtain the $$\Expect \lambda_{\min}(\mtx{Y}) \geq \Expect \lambda_{\min}(\mtx{Z} + \mtx{\Delta}) - \sqrt{2\smash{\sigma_*^2(\mtx{Z})} \log(2d)}.$$ Gaussian monotonicity (prop:gauss-monotone) for the concave function $\mtx{A} \mapsto \lambda_{\min}(\mtx{A} + \mtx{\Delta})$ and monotonicity of the weak variance[eqn:wvar-monotone] $$\Expect \lambda_{\min}(\mtx{Z} + \mtx{\Delta}) \geq \Expect \lambda_{\min}(\mtx{Z}')

<!-- chunk {"id": "body-0219", "role": "body", "section": "Gaussian comparison: Sum of iid random psd matrices", "weight": 1.0} -->

\quad\text{and}\quad \sigma_*^2(\mtx{Z}) \leq \sigma_*^2(\mtx{Z}').$$ Combine the last two displays and adjust the notation to reach the expectation bound[eqn:intro-thm-iid-expect] in thm:iid-intro. The proof of the tail bound[eqn:intro-thm-iid-tail] is similar.

<!-- chunk {"id": "body-0220", "role": "body", "section": "Step 1: Empirical approximation", "weight": 1.0} -->

To lighten notation, assume that the shift $\mtx{\Delta} \in \Sym_d$equals the zero matrix. The proof for a general shift is no different.

<!-- chunk {"id": "body-0221", "role": "body", "section": "Step 1: Empirical approximation", "weight": 1.0} -->

For a large parameter $\coll{A}_n \coloneqq (\mtx{A}_1, \dots, \mtx{A}_n)$ where the matrices $\mtx{A}_i$ are iid copies of $\mtx{W}$. The sampled matrices may not be distinct. Until the last steps of the proof, we regard the sample $\coll{A}_n$ as fixed.

<!-- chunk {"id": "body-0222", "role": "body", "section": "Step 1: Empirical approximation", "weight": 1.0} -->

$$\widehat{\mtx{Y}}_n \coloneqq \sum_{j=1}^k \widehat{\mtx{W}}_j \quad\text{where $\widehat{\mtx{W}}_j \sim \widehat{\mtx{W}}$.}$$ As a heuristic, when the number $n$ of sample points is large, the distribution of the proxy $\smash{\widehat{\mtx{Y}}_n}$ is close to the distribution of the original sum $\mtx{Y}$. lem:empirical-weakjustifies this claim.

<!-- chunk {"id": "body-0223", "role": "body", "section": "Step 2: Multinomial model", "weight": 1.0} -->

To analyze the proxy $\smash{\widehat{\mtx{Y}}_n}$, we work with an alternative representation. The $k$ independent summands in the proxy take the form $$\widehat{\mtx{W}}_j = \mtx{A}_{I_j} \quad\text{where $I_j \sim \uniform\{1, \dots, n\}$ iid for $j = 1, \dots, k$.}$$ For each index $i = 1, \dots, n$, define a scalar random variable $\delta_i$ that counts the number of the $I_j$ that select the index $i$.

<!-- chunk {"id": "body-0224", "role": "body", "section": "Step 2: Multinomial model", "weight": 1.0} -->

$$\delta_i \coloneqq \#\big\{ j \in \{1, \dots, k\}: I_j = i \big\}.$$ As a consequence, $\vct{\delta} \coloneqq (\delta_1, \dots, \delta_n) \sim \multinomial(k, n)$ follows the multinomial distribution of $k$ balls placed independently and uniformly at random in $n$ bins. Recall that $$\delta_i \sim \binomial(1/n, k) \quad\text{and}\quad Because of the coupling between the distributions, $$\widehat{\mtx{Y}}_n = \sum_{j=1}^k \widehat{\mtx{W}}_j = \sum_{i=1}^n \delta_i \mtx{A}_i.$$ Let us emphasize that the coefficient vector $\vct{\delta}$ is independent from the sample $\coll{A}_n$.

<!-- chunk {"id": "body-0225", "role": "body", "section": "Step 3: Poissonization", "weight": 1.0} -->

$\delta_i$ in the representation[eqn:proxy-multi] are not independent, but we can pass to a model that has independent coefficients: $$\mtx{X}_n \coloneqq \sum_{i=1}^n Q_i \mtx{A}_i \quad\text{where $Q_i \sim \poisson(k/n)$ iid.}$$ The Poisson variables $Q_i$ are independent from each other and from the multinomial variables $\delta_i$. Since $\Expect Q_i = \Expect \delta_i$, the conditional expectations of the random matrices $\mtx{X}_n$ and $\smash{\widehat{\mtx{Y}}_n}$ coincide.

<!-- chunk {"id": "body-0226", "role": "body", "section": "Step 3: Poissonization", "weight": 1.0} -->

Consider the random matrices $\smash{\widehat{\mtx{Y}}_n}$ and $\mtx{X}_n$ defined in[eqn:proxy-multi] and[eqn:proxy-poisson].

<!-- chunk {"id": "body-0227", "role": "body", "section": "Step 3: Poissonization", "weight": 1.0} -->

\widehat{\mtx{W}} \condbar \coll{A}_n \big] \right) \right) \quad\text{for $(s_1, \dots, s_n) \in \R_+^n$.}$$ According to[eqn:proxy-expect], the conditional expectation in the definition of $f$ coincides with the conditional expectation of both $\smash{\widehat{\mtx{Y}}_n}$ and of $\mtx{X}_n$.

<!-- chunk {"id": "body-0228", "role": "body", "section": "Step 3: Poissonization", "weight": 1.0} -->

Thus, we obtain the trace exponential with $\smash{\widehat{\mtx{Y}}_n}$ by evaluating $f(\delta_1, \dots, \delta_n)$, and we obtain the trace exponential with $\mtx{X}_n$ by evaluating $f(Q_1, \dots, Q_n)$.

<!-- chunk {"id": "body-0229", "role": "body", "section": "Step 3: Poissonization", "weight": 1.0} -->

The key insight is that the function with respect to each argument $s_i$ because each matrix $\mtx{A}_i$ is psd. This is a well-established and easy fact[:Trace-Inequalities], and it is also contained in Stahl's theorem (fact:bmv).

<!-- chunk {"id": "body-0230", "role": "body", "section": "Step 3: Poissonization", "weight": 1.0} -->

For completeness, we include the familiar argument that leads to the conclusion of the lemma. Recall that $(\delta_1, \dots, \delta_n) \sim \multinomial(k, n)$ and that $Q_i \sim \poisson(k/n)$ iid for $i = 1, \dots, n$. Define the sum $Q \coloneqq \sum_{i=1}^n Q_i$ of the Poisson variables, and note that $Q \sim \poisson(k)$.

<!-- chunk {"id": "body-0231", "role": "body", "section": "Step 3: Poissonization", "weight": 1.0} -->

The first inequality follows from the law of total expectation and the positivity of $f$. The second inequality depends on the monotonicity of $f$. The third inequality holds because $k$ is the median of the $\poisson(k)$ distribution[:Medians-Gamma]. Last, conditioning the Poisson variables on the event $\{Q = k\}$ produces the multinomial distribution[:Probability-Computing-2ed].

<!-- chunk {"id": "body-0232", "role": "body", "section": "Step 3: Poissonization", "weight": 1.0} -->

The analog of lem:poisson holds if we replace the trace exponential with any other trace function that is both positive and monotone. In particular, it applies to the one-sided power function $\mtx{M} \mapsto \trace{} (\mtx{M})_{-}^p$ for $p > 0$.

<!-- chunk {"id": "body-0233", "role": "body", "section": "Step 4: Comparison with the Gaussian model", "weight": 1.0} -->

We may now invoke the existing trace mgf bound (to compare the independent model $\mtx{X}_n$with a suitable Gaussian matrix.

<!-- chunk {"id": "body-0234", "role": "body", "section": "Step 4: Comparison with the Gaussian model", "weight": 1.0} -->

Construct the centered (conditionally) Gaussian random matrix $$\mtx{Z}_n \sim \normal(\mtx{0}, \mathsf{V}_n).$$ By the law of large numbers, when the number $n$ of samples is large, $\mathsf{V}_n \approx \mathsf{V}$, where $\mathsf{V}$ is defined in[eqn:iid-gauss]. As a consequence, the distribution of $\mtx{Z}_n$ is close to the distribution of the original Gaussian model $\mtx{Z}$ with covariance $\mathsf{V}$. lem:gauss-weak, below, fully justifies this claim.

<!-- chunk {"id": "body-0235", "role": "body", "section": "Step 4: Comparison with the Gaussian model", "weight": 1.0} -->

To compare the trace mgfs of the proxy $\smash{\widehat{\mtx{Y}}_n}$ and the Gaussian matrix $\mtx{Z}_n$, first apply the Poissonization result (lem:poisson). Then invoke the trace mgf bound (prop:psd-weight-mgf), conditional on $\coll{A}_n$.

<!-- chunk {"id": "body-0236", "role": "body", "section": "Step 5: Limits", "weight": 1.0} -->

At this stage, we can unfreeze the random sample and take limits. This process will produce the bound $$\Expect \trace \econst^{- \theta(\mtx{Y} - \Expect \mtx{Y})} \leq 2 \Expect \trace \econst^{-\theta \mtx{Z}}.$$ The random matrices $\mtx{Y}$ and $\mtx{Z}$ are defined in[eqn:iid-sum] and[eqn:iid-gauss]. The remaining steps leading to this result are technical. lem:truncation shows that it is enough to prove[eqn:iid-mgf-pf] under the additional assumption that the random summand $\mtx{W}$ is bounded.

<!-- chunk {"id": "body-0237", "role": "body", "section": "Step 5: Limits", "weight": 1.0} -->

The first limit follows from lem:empirical-weak. The second relation is the mgf bound[eqn:iid-prelimit]. The second limit follows from lem:gauss-weak. The details of these computations occupy the upcoming subsections.

<!-- chunk {"id": "body-0238", "role": "body", "section": "Technical Step 6: Truncation", "weight": 1.0} -->

To continue, we restrict our attention to the setting where the $\mtx{W}$is bounded in norm.

<!-- chunk {"id": "body-0239", "role": "body", "section": "Technical Step 6: Truncation", "weight": 1.0} -->

Suppose that[eqn:iid-mgf-pf] holds when the norm $\norm{\mtx{W}}$ is uniformly bounded. Then[eqn:iid-mgf-pf] remains valid when $\Expect \norm{\mtx{W}}^2 < + \infty$.

<!-- chunk {"id": "body-0240", "role": "body", "section": "Technical Step 6: Truncation", "weight": 1.0} -->

Suppose that $\Expect \norm{\mtx{W}}^2 < + \infty$. Let $R > 0$ be a truncation parameter. We will consider the random matrix models arising from the truncated summand: $\mtx{W} \indicator\{ \norm{\mtx{W}} \leq R \}$.

<!-- chunk {"id": "body-0241", "role": "body", "section": "Technical Step 6: Truncation", "weight": 1.0} -->

For iid summands $\mtx{W}_j \sim \mtx{W}$, define the coupled random matrix models $$\mtx{Y} \coloneqq \sum_{j=1}^k \mtx{W}_j \quad\text{and}\quad \mtx{Y}_{\wedge R} \coloneqq \sum_{j=1}^k \mtx{W}_j \indicator\{ \norm{\mtx{W}_j} \leq R \}.$$ Since the trace exponential is monotone with respect to the psd order[:Trace-Inequalities], $$\trace \econst^{-\theta (\mtx{Y}_{\wedge R} - \Expect \mtx{Y}_{\wedge R})} \leq \trace \econst^{\theta \Expect \mtx{Y} } < + \infty \quad\text{pointwise and for all $R > 0$.}$$ We have used the semidefinite relations

<!-- chunk {"id": "body-0242", "role": "body", "section": "Technical Step 6: Truncation", "weight": 1.0} -->

Bounded convergence yields $$\lim\nolimits_{R \to \infty} \Expect \trace\econst^{-\theta (\mtx{Y}_{\wedge R} - \Expect \mtx{Y}_{\wedge R})} = \Expect \trace \econst^{-\theta (\mtx{Y} - \Expect \mtx{Y})}.$$ Indeed, $\smash{\mtx{Y}_{\wedge R}} \to \mtx{Y}$ pointwise, and so $\Expect \smash{\mtx{Y}_{\wedge R}} \to \Expect \mtx{Y}$. The limit of the expectation is confirmed by applying monotone convergence to the quadratic forms induced by the random psd matrices.

<!-- chunk {"id": "body-0243", "role": "body", "section": "Technical Step 6: Truncation", "weight": 1.0} -->

Therefore, the Gaussian random matrices $\smash{\mtx{Z}_{\wedge R}} \sim \normal(\mtx{0}, \smash{\mathsf{V}_{\wedge R}})$ and $\mtx{Z} \sim \normal(\mtx{0}, \mathsf{V})$ satisfy $$\Expect \trace \econst^{-\theta \mtx{Z}_{\wedge R}} \leq \Expect \trace \econst^{-\theta \mtx{Z}} \quad\text{for all $R > 0$.}$$ This statement follows from monotonicity (prop:gauss-monotone) for the expectation of a convex function of a Gaussian. Convexity of the trace exponential is an easy classical fact[:Trace-Inequalities], which is also contained in Stahl's theorem (fact:bmv).

<!-- chunk {"id": "body-0244", "role": "body", "section": "Technical Step 6: Truncation", "weight": 1.0} -->

The inequality in the last display depends on the hypothesis of the lemma, namely that the relation[eqn:iid-mgf-pf] holds when $\norm{\mtx{W}}$

<!-- chunk {"id": "body-0245", "role": "body", "section": "Technical Step 7: Convergence of the empirical model", "weight": 1.0} -->

Next, we must verify that the empirical approximations $\smash{\widehat{\mtx{Y}}_n}$ converge weakly to the original random matrix model $\mtx{Y}$.

<!-- chunk {"id": "body-0246", "role": "body", "section": "Technical Step 7: Convergence of the empirical model", "weight": 1.0} -->

Assume that the random summand has two finite moments: $\Expect \norm{\mtx{W}}^2 < + \infty$. Define random matrices $\mtx{Y}$ and $\smash{\widehat{\mtx{Y}}_n}$ as in[eqn:iid-sum] and[eqn:proxy-multi].

<!-- chunk {"id": "body-0247", "role": "body", "section": "Technical Step 7: Convergence of the empirical model", "weight": 1.0} -->

- For each bounded, Lipschitz function $h: \Sym_d \to \R$, $$\Expect h\big(\widehat{\mtx{Y}}_n - \Expect\big[\widehat{\mtx{Y}}_n \condbar \coll{A}_n \big] \big) \to \Expect h(\mtx{Y} - \Expect \mtx{Y}) \quad\text{as $n \to \infty$.}$$ - If $\norm{\mtx{W}}$ is uniformly bounded, the limit[eqn:empirical-weak] also holds for $h(\mtx{M}) \coloneqq \trace \econst^{-\theta \mtx{M}}$ with $\theta \in \R$.

<!-- chunk {"id": "body-0248", "role": "body", "section": "Technical Step 7: Convergence of the empirical model", "weight": 1.0} -->

Lipschitz functions are defined with respect to the Frobenius norm on self-adjoint matrices. The expectations average over everything, including the random sample $\coll{A}_n$.

<!-- chunk {"id": "body-0249", "role": "body", "section": "Technical Step 7: Convergence of the empirical model", "weight": 1.0} -->

To begin, let us explore some properties of the empirical approximation $\smash{\widehat{\mtx{Y}}_n}$. The representation[eqn:proxy-multi] shows that $$\widehat{\mtx{Y}}_n = \sum_{i=1}^n \delta_i^{(n)} \mtx{A}_i \quad\text{where $\vct{\delta}^{(n)} \sim \multinomial(k, n)$.}$$ The multinomial coefficients $\smash{\vct{\delta}^{(n)}} \coloneqq \big(\delta^{(n)}_1, \dots, \delta^{(n)}_n \big)$ are independent from the sample $\coll{A}_n$.

<!-- chunk {"id": "body-0250", "role": "body", "section": "Technical Step 7: Convergence of the empirical model", "weight": 1.0} -->

Define the event $\set{D}_n$ where the multinomial selects $k$ distinct summands: $$\set{D}_n \coloneqq \big\{ \# \supp\big(\vct{\delta}^{(n)}\big) = k \big\}.$$ For large sample size $n$, it is likely that $\set{D}_n$ occurs. By the birthday paradox argument[:Probability-Computing-2ed], $$\Probe(\set{D}_n) = \prod_{j=1}^k \left(1 - \frac{j-1}{n}\right) \geq 1 - \sum_{j=1}^k \frac{j-1}{n} Conditional on the event $\set{D}_n$ occurring, the distribution of the empirical approximation $\smash{\widehat{\mtx{Y}}_n}$ is the same as the distribution $\mtx{Y}$.

<!-- chunk {"id": "body-0251", "role": "body", "section": "Technical Step 7: Convergence of the empirical model", "weight": 1.0} -->

More precisely, for each Borel set $\set{B} \subseteq \Sym_d$, $$\Prob{ \widehat{\mtx{Y}}_n \in \set{B} \lcondbar \set{D}_n } = \Prob{ \sum_{i \in \supp(\vct{\delta}^{(n)})} \mtx{A}_i \in \set{B} \lcondbar \set{D}_n } = \Prob{ \sum_{j=1}^k \mtx{W}_j \in \set{B} } = \Prob{ \mtx{Y} \in \set{B} }.$$ Indeed, each sample $\mtx{A}_i$ is an independent draw from the distribution $\mtx{W}$, as are the random matrices $\mtx{W}_1, \dots, \mtx{W}_k$. This argument formalizes the intuition that the empirical approximation is a good proxy for the original random matrix.

<!-- chunk {"id": "body-0252", "role": "body", "section": "Technical Step 7: Convergence of the empirical model", "weight": 1.0} -->

Next, we turn to the conditional expectation of the empirical approximation. Since each coefficient $\delta_i \sim \binomial(1/n, k)$, $$\Expect\big[\widehat{\mtx{Y}}_n \condbar \coll{A}_n \big] = \frac{k}{n} \sum_{i=1}^n \mtx{A}_i.$$ Each sample $\mtx{A}_i$ is an independent copy of $\mtx{W}$, so its expectation satisfies $\Expect \mtx{A}_i = \Expect \mtx{W} = k^{-1} \Expect \mtx{Y}$.

<!-- chunk {"id": "body-0253", "role": "body", "section": "Technical Step 7: Convergence of the empirical model", "weight": 1.0} -->

Now, suppose that $h$ has bounded Lipschitz norm $L$. In other words, both the uniform norm of $h$ and the Lipschitz constant of $h$ are at most $L$.

<!-- chunk {"id": "body-0254", "role": "body", "section": "Technical Step 7: Convergence of the empirical model", "weight": 1.0} -->

Define the sequence of moments $$E_n \coloneqq \Expect h\big(\widehat{\mtx{Y}}_n - \Expect \big[\widehat{\mtx{Y}}_n \condbar \coll{A}_n \big] \big).$$ Add and subtract the matrix $\Expect \mtx{Y}$, and invoke the Lipschitz property: $$E_n = \Expect h\big(\widehat{\mtx{Y}}_n - \Expect \mtx{Y} \big) \pm L \cdot \Expect \lnorm{ \Expect\big[\widehat{\mtx{Y}}_n \condbar \coll{A}_n \big] - \Expect \mtx{Y} }_{\mathrm{F}}.$$ The notation $x = a \pm b$ is shorthand for the pair of inequalities $a - b \leq x \leq a + b$.

<!-- chunk {"id": "body-0255", "role": "body", "section": "Technical Step 7: Convergence of the empirical model", "weight": 1.0} -->

From[eqn:proxy-mean], we see that the second term on the right-hand side of the last display tends to zero.

<!-- chunk {"id": "body-0256", "role": "body", "section": "Technical Step 7: Convergence of the empirical model", "weight": 1.0} -->

Indeed, the conditional distribution $\smash{\widehat{\mtx{Y}}_n} \condbar \set{D}_n \sim \mtx{Y}$. The inequalities depend on two applications of the probability estimate[eqn:birthday] and the fact that the magnitude of $h$ is uniformly bounded by $L$. Altogether, $$E_n = \Expect h \big(\widehat{\mtx{Y}}_n - \Expect\big[\widehat{\mtx{Y}}_n \condbar \coll{A}_n \big] \big) \to \Expect h(\mtx{Y} - \Expect \mtx{Y}) \quad\text{as $n \to \infty$.}$$ We have established the weak convergence claim.

<!-- chunk {"id": "body-0257", "role": "body", "section": "Technical Step 7: Convergence of the empirical model", "weight": 1.0} -->

Last, assume that the random summand satisfies $\norm{\mtx{W}} \leq R$ In this case, the random matrices $\smash{\widehat{\mtx{Y}}_n}$ and $\mtx{Y}$ are all bounded in norm by $kR$. The trace exponential function $h(\mtx{M}) = \trace \econst^{-\theta \mtx{M}}$ is bounded and Lipschitz on the common support of these random matrices. Therefore, the weak convergence result[eqn:empirical-weak] $$\Expect \trace \econst^{-\theta (\widehat{\mtx{Y}}_n - \Expect [\widehat{\mtx{Y}}_n \condbar \coll{A}_n])} \to \Expect \trace \econst^{-\theta (\mtx{Y} - \Expect \mtx{Y})} \quad\text{as $n \to \infty$.}$$ This is the second conclusion.

<!-- chunk {"id": "body-0258", "role": "body", "section": "Technical Step 8: Convergence of the Gaussian model", "weight": 1.0} -->

Finally, we must argue that the sequence $\mtx{Z}_n$ of Gaussian models converges weakly to the target Gaussian distribution $\mtx{Z}$. The proof relies on characteristic functions.

<!-- chunk {"id": "body-0259", "role": "body", "section": "Technical Step 8: Convergence of the Gaussian model", "weight": 1.0} -->

Assume that the random summand has two finite moments: $\Expect \norm{\mtx{W}}^2 < + \infty$. Define Gaussian matrices $\mtx{Z}$ and $\mtx{Z}_n$ as in[eqn:iid-gauss] and[eqn:proxy-gauss].

<!-- chunk {"id": "body-0260", "role": "body", "section": "Technical Step 8: Convergence of the Gaussian model", "weight": 1.0} -->

- For each bounded Lipschitz function $h: \Sym_d \to \R$, $$\Expect h(\mtx{Z}_n) \to \Expect h(\mtx{Z}) \quad\text{as $n \to \infty$.}$$ - If $\norm{\mtx{W}}$ is uniformly bounded, the limit[eqn:gauss-weak] also holds for $h(\mtx{M}) \coloneqq \trace \econst^{-\theta \mtx{M}}$ with $\theta \in \R$.

<!-- chunk {"id": "body-0261", "role": "body", "section": "Technical Step 8: Convergence of the Gaussian model", "weight": 1.0} -->

The expectation averages over everything, including the random sample $\coll{A}_n$.

<!-- chunk {"id": "body-0262", "role": "body", "section": "Technical Step 8: Convergence of the Gaussian model", "weight": 1.0} -->

This just reinterprets the usual formula for the Gaussian characteristic function[:Real-Analysis].

<!-- chunk {"id": "body-0263", "role": "body", "section": "Technical Step 8: Convergence of the Gaussian model", "weight": 1.0} -->

Recall that a sequence of random matrices converges weakly if and only if the characteristic functions converge pointwise to a limit that is continuous Therefore, to prove the weak convergence statement[eqn:gauss-weak], it suffices to verify that $$\chi_{\mtx{Z}_n}(\mtx{M}) \to \chi_{\mtx{Z}}(\mtx{M}) \quad\text{for each $\mtx{M} \in \Sym_d$.}$$ Equivalently, we can obtain weak convergence from the limit $$\Expect \econst^{ - \mathsf{V}_n(\mtx{M}) / 2} \to \econst^{ - \mathsf{V}(\mtx{M}) / 2} \quad\text{for each $\mtx{M} \in \Sym_d$.}$$ But this statement follows instantly from bounded convergence and the almost sure limit[eqn:cov-lln].

<!-- chunk {"id": "body-0264", "role": "body", "section": "Technical Step 8: Convergence of the Gaussian model", "weight": 1.0} -->

Indeed, variance functions are positive, so the exponentials are uniformly bounded by one.

<!-- chunk {"id": "body-0265", "role": "body", "section": "Technical Step 8: Convergence of the Gaussian model", "weight": 1.0} -->

Last, assume that the random summand satisfies $\norm{\mtx{W}} \leq R$ for some $R > 0$. We must upgrade the weak convergence[eqn:gauss-weak] to convergence for the trace mgf function $h(\mtx{M}) \coloneqq \trace \econst^{-\theta \mtx{M}}$ This step requires asymptotic uniform integrability[vdV98:Asymptotic-Statistics].

<!-- chunk {"id": "body-0266", "role": "body", "section": "Technical Step 8: Convergence of the Gaussian model", "weight": 1.0} -->

$$\lim\nolimits_{B \to \infty} \limsup\nolimits_{n \to \infty} \Expect\big[\trace \econst^{-\theta \mtx{Z}_n} \indicator\{ \norm{\mtx{Z}_n} \geq B \} \big] Granted[eqn:gauss-aui], we obtain the limit $\Expect h(\mtx{Z}_n) \to \Expect h(\mtx{Z})$, and the proof is complete.

<!-- chunk {"id": "body-0267", "role": "body", "section": "Technical Step 8: Convergence of the Gaussian model", "weight": 1.0} -->

By monotonicity (prop:gauss-monotone), applied conditionally on $\coll{A}_n$, the comparison $\Expect f(\mtx{Z}_n) \leq \Expect f(\mtx{G})$ holds for each convex function $f: \Sym_d \to \R$.

<!-- chunk {"id": "body-0268", "role": "body", "section": "Technical Step 8: Convergence of the Gaussian model", "weight": 1.0} -->

The last inequality follows from the comparison of $\mtx{Z}_n$ with $\mtx{G}$. Since $\mtx{G}$ is a fixed Gaussian matrix, the two expectations with respect to $\mtx{G}$ are finite, and the asymptotic uniform integrability condition[eqn:gauss-aui] is valid.

<!-- chunk {"id": "body-0269", "role": "body", "section": "Extension: Polynomial moments", "weight": 1.0} -->

The proof of the trace mgf comparison [eqn:iid-mgf-pf]can be adapted to obtain a comparison theorem for polynomial moments.

<!-- chunk {"id": "body-0270", "role": "body", "section": "Extension: Polynomial moments", "weight": 1.0} -->

Instate the hypotheses of thm:iid-sum. For each $p \geq 4$, $$\Expect \trace{} (\mtx{Y} - \Expect \mtx{Y} + \mtx{\Delta})_-^p \leq 2 \Expect \trace{} (\mtx{Z} + \mtx{\Delta})_-^p.$$ Note that the trace function $f(w) \coloneqq \trace{} (w\mtx{A} - \mtx{B})_{-}^p$ is completely monotone of order four when $p \geq 4$. Therefore, we can activate the Poissonization result (rem:poisson) and the polynomial moment bound for weighted sums (prop:psd-weights-poly). These are the main changes, as compared with the proof of[eqn:iid-mgf-pf]. There are also some minor technical differences in the proofs of lem:truncation,lem:empirical-weak,lem:gauss-weak.

<!-- chunk {"id": "body-0271", "role": "body", "section": "Matrix concentration for psd sums", "weight": 1.0} -->

For completeness, we include a short proof of the matrix concentration results for the lower tail of a psd sum. This result was communicated to the author by Andreas Maurer in 2011, but there does not seem to be [Matrix concentration: Exponential PaleyZygmund] Consider an independent family $(\mtx{W}_1, \dots, \mtx{W}_n)$ of random psd matrices with common dimension $d$ and with two finite moments.

<!-- chunk {"id": "body-0272", "role": "body", "section": "Matrix concentration for psd sums", "weight": 1.0} -->

\cdot \lambda_{\min}(\Expect \mtx{Y})$ in the tail bound[eqn:epz-tail]. We obtain a ratio of the squared norm of the first moment to the norm of the sum of second moments. The proof depends on a trace mgf bound.

<!-- chunk {"id": "body-0273", "role": "body", "section": "Matrix concentration for psd sums", "weight": 1.0} -->

Let $\mtx{W}$ be a random psd matrix with two finite moments. For $\theta \geq 0$, we have the semidefinite relation $$\log \Expect \econst^{-\theta \mtx{W}} \psdle \theta (\Expect \mtx{W}) + \tfrac{1}{2} \theta^2 (\Expect \mtx{W}^2).$$ Recall the numerical inequality $\econst^{-a} \leq 1 - a + a^2 / 2$, valid for $a \geq 0$.

<!-- chunk {"id": "body-0274", "role": "body", "section": "Matrix concentration for psd sums", "weight": 1.0} -->

By the transfer rule[:Introduction-Matrix], the inequality extends to matrices: $$\Expect \econst^{-\theta \mtx{W}} \psdle \Expect[\Id - \theta \mtx{W} + \tfrac{1}{2} \theta^2 \mtx{W}^2] = \Id - \theta (\Expect \mtx{W}) + \tfrac{1}{2} \theta^2 (\Expect \mtx{W}^2) \quad\text{for $\theta \geq 0$.}$$ Since the logarithm is matrix monotone[:Introduction-Matrix], we can extract the logarithm. Apply the numerical inequality $\log(1 + a) \leq a$ for $a > - 1$ using the transfer rule.

<!-- chunk {"id": "body-0275", "role": "body", "section": "Matrix concentration for psd sums", "weight": 1.0} -->

The result follows quickly from standard matrix concentration arguments. For example, to derive the probability inequality, we apply the matrix Laplace transform method[:Introduction-Matrix].

<!-- chunk {"id": "body-0276", "role": "body", "section": "Matrix concentration for psd sums", "weight": 1.0} -->

The second inequality requires the subadditivity of matrix log-mgfs[:Introduction-Matrix] and the monotonicity of the trace exponential. The third inequality is lem:epz-cgf. The last inequality depends on the spectral mapping theorem and the definition of $L_2$. Select $\theta = t/ (2L_2)$ to complete the bound. The stated result follows from an application of Weyl's inequality[:Matrix-Analysis].
