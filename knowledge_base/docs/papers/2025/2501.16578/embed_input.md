<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Comparison Theorems for the Minimum Eigenvalue of a Random Positive-semidefinite Matrix

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper establishes a new comparison principle for the minimum eigenvalue of a sum of independent random positive-semidefinite matrices. The principle states that the minimum eigenvalue of the matrix sum is controlled by the minimum eigenvalue of a Gaussian random matrix that inherits its statistics from the summands. This methodology is powerful because of the vast arsenal of tools for treating Gaussian random matrices. As applications, the paper presents short, conceptual proofs of some old and new results in high-dimensional statistics. It also settles a long-standing open question in computational linear algebra about the injectivity properties of very sparse random matrices.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

This paper establishes a new comparison principle for the minimum eigenvalue of a sum of independent random positive-semidefinite matrices. The principle states that the minimum eigenvalue of the matrix sum is controlled by the minimum eigenvalue of a Gaussian random matrix that inherits its statistics from the summands. This methodology is powerful because of the vast arsenal of tools for treating Gaussian random matrices. As applications, the paper presents short, conceptual proofs of some old and new results in high-dimensional statistics. It also settles a long-standing open question in computational linear algebra about the injectivity properties of very sparse random matrices.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Key words and phrases", "weight": 1.0} -->

Comparison theorem, high-dimensional probability, high-dimensional statistics, random matrix

<!-- chunk {"id": "body-0005", "role": "body", "section": "Motivation", "weight": 1.0} -->

Random positive-semidefinite (psd) matrices appear throughout high-dimensional statistics and high-dimensional probability. In particular, random psd matrices model the sample covariance of a random vector, and they capture properties of random linear embeddings. For a psd matrix, the minimum eigenvalue provides a quantitative measure of invertibility, so it is often the crucial statistic of these random matrix models. This paper introduces a new technique for studying the minimum eigenvalue of a random psd matrix by establishing a comparison with the minimum eigenvalue of a Gaussian random matrix. It also showcases several applications of this methodology.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Intuition: Positive random walks", "weight": 1.0} -->

Consider a random walk on the real line that can only move in the positive direction. What is the probability that the random walk remains close to its origin? This event occurs only when all of the increments are small, which is very unlikely. We can capture this insight with a standard probability inequality that is the starting point for our investigation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Intuition: Positive random walks", "weight": 1.0} -->

To model the positive random walk, we introduce a sum of nonnegative real random variables that are independent and identically distributed (iid): When the increment $W$ has two moments, we can compare the moment generating function (mgf) for the lower tail of the positive sum $Y$ with the mgf of a Gaussian real random variable. For all $\theta\geq 0$, See Section˜7 for a proof of (1.1). The mgf bound leads to a classic inequality for the lower tail: In other words, the lower tail of the positive sum $Y$ is related to the lower tail of a matching Gaussian random variable $Z$ that inherits its statistics from the summand $W$. See Figure˜1.1 for an illustration.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Random psd matrices", "weight": 1.0} -->

This paper demonstrates that the same phenomena persist in the matrix setting. Consider a sum of iid random psd matrices, either real or complex: The minimum eigenvalue $\lambda_{\min}(\bm{Y})$ can be expressed as the minimum of a family of iid positive sums: For each direction $\bm{u}$, the sum in (1.4) is very unlikely to be zero because of (1.2). On the other hand, the random summands $\bm{W}_{i}$ must cover every direction $\bm{u}$ before the minimum eigenvalue $\lambda_{\min}(\bm{Y})$ is strictly positive. It is not clear which of these two opposing principles prevails.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Random psd matrices", "weight": 1.0} -->

To resolve this dilemma, we adapt the strategy behind the scalar inequality (1.2) to the matrix setting. Construct a self-adjoint Gaussian random matrix $\bm{Z}$ that inherits its statistics from the summands: | | $\displaystyle\operatorname{\mathbb{E}}[\bm{Z}]$ | $\displaystyle=n\cdot\operatorname{\mathbb{E}}[\bm{W}];$ | | (1.5) | | | $\displaystyle\operatorname{Var}[\operatorname{Tr}[\bm{MZ}]]$ | $\displaystyle=n\cdot\operatorname{\mathbb{E}}[|{\operatorname{Tr}[\bm{MW}]}|^{2}]\quad\text{for all self-adjoint $\bm{M}$.}$ | | | Inspired by (1.1), we will establish a comparison between the trace mgfs of the two random matrices: Figure˜1.2 illustrates the comparison.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Random psd matrices", "weight": 1.0} -->

While the scalar case (1.1) is easy, the matrix inequality (1.6) relies on a deep fact from matrix analysis called Stahl's theorem, formerly the BMV conjecture \[:Proof-BMV\].

<!-- chunk {"id": "body-0011", "role": "body", "section": "Random psd matrices", "weight": 1.0} -->

Using standard methods from high-dimensional probability \[:Introduction-Matrix, vH16:Probability-High\], the trace inequality (1.6) leads to a probabilistic comparison for the minimum eigenvalues: where $d$ is the matrix dimension. The weak variance $\sigma_{*}^{2}(\bm{Z})\coloneqq\max_{\|{\bm{u}}\|=1}\operatorname{Var}[\bm{u}^{*}\bm{Z}\bm{u}]$ controls the variance of $\lambda_{\min}(\bm{Z})$. The result (1.7) is powerful enough to yield sharp, dimension-free bounds for the minimum eigenvalue of some models. See Theorem˜2.3. ‣ 2.3. Gaussian comparison: Sum of iid psd random matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") for the full statement of the comparison.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Random psd matrices", "weight": 1.0} -->

To analyze the minimum eigenvalue $\lambda_{\min}(\bm{Z})$ of the Gaussian matrix in (1.7), we have a bristling armamentarium of techniques at our disposal. This methodology leads to short, conceptual proofs of several important results from high-dimensional statistics (Section˜5). It also addresses a vexing open question from computational linear algebra about very sparse random matrices (Section˜6).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Roadmap", "weight": 1.0} -->

Section˜2 states two comparison theorems and discusses related work. Section˜3 provides background on Gaussian random matrices that aids in the analysis of the comparison model. Sections˜4, 5 and 6 apply the main results to several examples. Section˜7 details a proof of (1.2) that generalizes to matrices. Last, Sections˜8 and 9 establish the main results, including (1.6) and (1.7).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Main results and related work", "weight": 1.0} -->

This section states our two main comparison theorems. The first concerns the sum of psd matrices with random weights. The second theorem concerns a sum of iid random psd matrices described in Section˜1.2. Afterward, we present a simple first example, and we discuss some related work.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Gaussian comparison: Randomly weighted sum of psd matrices", "weight": 1.0} -->

The first result treats a random matrix model where we randomly weight the terms in a sum of fixed psd matrices.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Second moments and Gaussians", "weight": 1.0} -->

To state our next result compactly, we introduce notation that describes the second moments of a random matrix model.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Gaussian comparison: Sum of iid psd random matrices", "weight": 1.0} -->

Our second result provides a Gaussian comparison for a sum of iid random psd matrices, the model described in the introduction.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Conjecture 2.4 (Non-iid sums)", "weight": 1.0} -->

It is natural to conjecture a comparison between the random matrices In this setting, we were only able to establish weak variants of (2.4. ‣ 2.3. Gaussian comparison: Sum of iid psd random matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")) and (2.5. ‣ 2.3. Gaussian comparison: Sum of iid psd random matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")), but we believe that similar statements should remain valid.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Example: Wishart matrix", "weight": 1.0} -->

As a first example, we treat the minimum eigenvalue of a standard real Wishart matrix \[:Aspects-Multivariate, Sec. 3.2\]. Introduce the random, rank-one psd matrix Draw independent copies $\bm{W}_{1},\dots,\bm{W}_{n}$ of the random matrix $\bm{W}$, and form the sum: After a calculation of the first and second moments of $\bm{W}$, Theorem˜2.3.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example: Wishart matrix", "weight": 1.0} -->

‣ 2.3. Gaussian comparison: Sum of iid psd random matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") furnishes a comparison between the Wishart matrix $\bm{Y}$ and the Gaussian matrix where $\gamma\sim\textsc{normal}_{\mathbb{R}}$ and $\bm{G}_{\mathrm{goe}}$ is drawn independently from the (unnormalized) Gaussian orthogonal ensemble (GOE); see Section˜3.7.3 for details. Exploiting standard facts about the GOE matrix \[:Alice-Bob, Exer. 6.48\], we find that the minimum eigenvalue and the weak variance satisfy Therefore, Theorem˜2.3.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Example: Wishart matrix", "weight": 1.0} -->

‣ 2.3. Gaussian comparison: Sum of iid psd random matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") yields the explicit, nonasymptotic bound The bound is nontrivial when $n\geq\big{(}2\sqrt{d}+\sqrt{6\log(2d)}\big{)}^{2}$. In particular, it suffices that $n\gtrsim d$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example: Wishart matrix", "weight": 1.0} -->

How tight is the inequality (2.10)? Rescale by the number $n$ of samples, and introduce the aspect ratio $\varrho\coloneq d/n\in(0,1]$. When $d,n\to\infty$ with the ratio $\varrho$ fixed, we determine that In this regime, the sharp asymptotic \[:Limit-Smallest\] is When the aspect ratio $\varrho$ is small (that is, $n\gg d$), the bound (2.10) is correct to first order, including the numerical constant. On the other hand, the bound is only active inside the regime where $n\geq 4d$, so it does not speak to the more challenging case where $n\approx d$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Nonexample: Wishart matrix", "weight": 1.0} -->

Suppose that we apply Theorem˜2.3. ‣ 2.3. Gaussian comparison: Sum of iid psd random matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") directly to the random matrix $\bm{Y}\sim\textsc{wishart}_{\mathbb{R}}(\mathbf{I}_{d},n)$ without a decomposition into rank-one terms. (That is, we set $\bm{W}\sim\textsc{wishart}_{\mathbb{R}}(\mathbf{I}_{d},n)$ and add only a single copy.) After a calculation, we obtain the comparison model: The minimum eigenvalue satisfies the same bound as before, but the weak variance is much larger: Theorem˜2.3.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Nonexample: Wishart matrix", "weight": 1.0} -->

‣ 2.3. Gaussian comparison: Sum of iid psd random matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") results in the comparison This inequality is always vacuous.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Nonexample: Wishart matrix", "weight": 1.0} -->

From this exercise, we discover that Theorem˜2.3. ‣ 2.3. Gaussian comparison: Sum of iid psd random matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") furnishes different conclusions, depending on how we decompose a random matrix as a sum of iid psd terms. Heuristically, we want to break the random matrix into the smallest pieces we can to extract the most leverage from the theorem.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Equivariance", "weight": 1.0} -->

An attractive feature of Theorems˜2.1. ‣ 2.1. Gaussian comparison: Randomly weighted sum of psd matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") and 2.3. ‣ 2.3. Gaussian comparison: Sum of iid psd random matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") is that the results are equivariant under linear transformations (Proposition˜3.1. ‣ 3.2. First and second moments of random matrices ‣ 3. Gaussian random matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Equivariance", "weight": 1.0} -->

In particular, if $\bm{Z}$ is a Gaussian comparison model for the random psd sum $\bm{Y}$, then $\bm{K}^{*}\bm{Z}\bm{K}$ is a Gaussian comparison model for $\bm{K}^{*}\bm{Y}\bm{K}$. In this statement, $\bm{K}$ is any conformable matrix, not necessarily square.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Equivariance", "weight": 1.0} -->

This observation facilitates the computation of comparison models. For instance, it is often convenient to transform the random matrix $\bm{Y}$ so that its expectation $\operatorname{\mathbb{E}}\bm{Y}=\mathbf{I}$. The equivariance property also plays a central role in the analysis of randomized subspace injections (Section˜6).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Gaussian comparison versus matrix concentration", "weight": 1.0} -->

When is the Gaussian comparison method effective? Consider a self-adjoint Gaussian matrix $\bm{Z}\in\mathbb{H}_{d}$. Its minimum eigenvalue satisfies A sufficient condition for the comparison (2.4. ‣ 2.3. Gaussian comparison: Sum of iid psd random matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")) between $\lambda_{\min}(\bm{Y})$ and $\lambda_{\min}(\bm{Z})$ to be informative is that the right-hand side of (2.11) is positive. To check the latter condition, we need to understand the scale for the expected norm.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Gaussian comparison versus matrix concentration", "weight": 1.0} -->

To that end, define the matrix variance statistic \[:Introduction-Matrix, Eqn. (2.2.4)\]: The matrix variance controls the expected norm of a self-adjoint, centered Gaussian matrix: This statement (2.12) is a variant of the matrix Khinchin inequality (˜3.3. ‣ 3.5. Matrix variance ‣ 3. Gaussian random matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")). Both bounds in (2.12) are saturated. We must undertake a more sensitive analysis to determine whether or not the expected norm includes the dimensional factor, $\log(2d)$. The matrix variance compares with the weak variance: Both bounds in (2.13) are attainable. In contrast to $\lambda_{\min}(\bm{Z})$, the statistics $\sigma^{2}(\bm{Z})$ and $\sigma_{*}^{2}(\bm{Z})$ are easy to compute, as they only depend on the second moments of the random matrix.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Gaussian comparison versus matrix concentration", "weight": 1.0} -->

We can obtain a coarse version of Theorem˜9.1. ‣ 9. Gaussian comparison: Sum of iid random psd matrices ‣ 8.4. Extension: Polynomial moments ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") by incorporating the estimates (2.11), (2.12), and (2.13). For instance, the expectation bound (2.4.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Gaussian comparison versus matrix concentration", "weight": 1.0} -->

‣ 2.3. Gaussian comparison: Sum of iid psd random matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")) implies that In fact, an improvement of the estimate (2.14) follows from simpler arguments based on the scalar mgf inequality (1.1) and matrix concentration tools \[:Introduction-Matrix\]; see Appendix˜A. ‣ 9.9. Technical Step 8: Convergence of the Gaussian model ‣ Item 2. ‣ Lemma 9.5 (Empirical approximation: Weak convergence).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Gaussian comparison versus matrix concentration", "weight": 1.0} -->

‣ 9.8. Technical Step 7: Convergence of the empirical model ‣ 9. Gaussian comparison: Sum of iid random psd matrices ‣ 8.4. Extension: Polynomial moments ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4 ‣ 2nd item ‣ 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") for details.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Gaussian comparison versus matrix concentration", "weight": 1.0} -->

The benefits of the Gaussian comparison method now come into sharper focus. Theorems˜2.1. ‣ 2.1. Gaussian comparison: Randomly weighted sum of psd matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") and 2.3. ‣ 2.3. Gaussian comparison: Sum of iid psd random matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") are most effective in case But we need a finer scalpel than the matrix Khinchin inequality (2.12) to assess whether the expected norm includes the dimensional factor.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 2.5 (Wishart: Matrix concentration)", "weight": 1.0} -->

Suppose we apply the matrix concentration bound (2.14) to the comparison model (2.9) for the Wishart matrix $\bm{Y}\sim\textsc{wishart}_{\mathbb{R}}(\mathbf{I}_{d},n)$. The matrix variance statistic $\sigma^{2}(\bm{Z})=n(d+2)$, and we arrive at the bound This bound, while nontrivial, does not capture the correct dimensional dependence that is visible in (2.10). We have squandered the valuable distributional information provided by Theorem˜2.3. ‣ 2.3. Gaussian comparison: Sum of iid psd random matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix").

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 2.6 (Intrinsic freeness)", "weight": 1.0} -->

Recent research \[:Second-Order-Matrix,:Matrix-Concentration\] has demonstrated that we can sometimes compare the eigenvalue distribution of a Gaussian matrix with a free probability model, using simple summary statistics. These intrinsic freeness results can be valuable for handling the Gaussian comparison model, but they are unhelpful for the applications in this paper.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Universality laws for random matrices", "weight": 1.0} -->

Compared with our work, the results that are closest in spirit appear in a recent paper of Brailovskaya & van Handel \[:Universality-Sharp\]. Their paper contains quantitative universality theorems for sums of random matrices, in the spirit of the Berry--Esseen theorem. As we will explain, their results are incomparable with the ones in this paper.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Universality laws for random matrices", "weight": 1.0} -->

Brailovskaya & van Handel consider an independent sum of self-adjoint random matrices $\bm{W}_{i}$, not necessarily psd or identically distributed. They compare the sum with a Gaussian model that shares the same first- and second-order statistics, as in the multivariate central limit theorem: In contrast, our approach requires the summands $\bm{W}_{i}$ to be iid random psd matrices, and it compares the sum with a slightly different Gaussian model.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Universality laws for random matrices", "weight": 1.0} -->

Under appropriate conditions on the summands, Brailovskaya & van Handel argue that the eigenvalue distribution of $\bm{Y}$ and the eigenvalue distribution of the Gaussian model $\bm{Z}^{\prime}$ are similar. Their results address both the spectral density and the spectral support. As one may imagine, it appears to require stricter assumptions on the statistics of the random matrices to ensure this strong affinity.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Universality laws for random matrices", "weight": 1.0} -->

For instance, to control the minimum eigenvalue of the random sum, Brailovskaya & van Handel assume that the uniform bound statistic This condition ensures that each one of the summands makes a limited contribution to the sum. The restriction is particularly important when the random matrices have few moments or the summands have inhomogeneous distributions. Under this surmise, they prove \[:Universality-Sharp, Thm. 2.8\] that the expected distance between the minimum eigenvalues satisfies As in the present paper, the second term arises from Gaussian concentration. To understand the first term, recall from (2.12) that the scale for the minimum eigenvalue of $\operatorname{\mathbb{E}}\lambda_{\min}(\bm{Z}^{\prime}-\operatorname{\mathbb{E}}\bm{Z}^{\prime})$ is the statistic $\sigma(\bm{Z}^{\prime})$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Universality laws for random matrices", "weight": 1.0} -->

In some examples, the factor $R^{1/6}\log d$ submerges the first term below this level.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Universality laws for random matrices", "weight": 1.0} -->

The results of Brailovskaya & van Handel are powerful and wide ranging. For some of the applications we consider in this paper, however, their approach produces several parasitic logarithmic factors that make it impossible to reach the optimal bounds. These factors are particularly significant in applications to computational mathematics (Section˜6), where constants and logarithms matter.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Universality laws for random matrices", "weight": 1.0} -->

As with our Gaussian comparison theorems, the proof strategy in the paper of Brailovskaya & van Handel is based on techniques from Stein's method. While there are small points of similarity (e.g., the use of interpolation), our technical apparatus follows an independent design.

<!-- chunk {"id": "body-0044", "role": "body", "section": "An independent sum of random psd matrices", "weight": 1.0} -->

There is also a body of work that provides specialized bounds for the minimum eigenvalue of an independent sum of random psd matrices. Several of these papers are inspired by the same observation (1.2) that an independent sum of nonnegative real random variables has a Gaussian lower tail, and they pursue this insight in creative and multifarious ways. We focus on the earliest and most distinctive contributions.

<!-- chunk {"id": "body-0045", "role": "body", "section": "An independent sum of random psd matrices", "weight": 1.0} -->

This literature treats several different random matrix models. To facilitate comparisons, we summarize the implications for a special case involving sample covariance matrices. Consider a random vector $\bm{w}\in\mathbb{R}^{d}$ that has four finite moments. For normalization, assume that the vector is isotropic: $\operatorname{\mathbb{E}}[\bm{ww}^{\transp}]=\mathbf{I}_{d}$. Form the sample covariance matrix based on $n$ samples: For a parameter $\varepsilon\in$, how many samples $n=n(\varepsilon)$ are sufficient to ensure that $\lambda_{\min}(\bm{Y})\geq 1-\varepsilon$ with high probability? The weak assumptions on moments make this question very challenging.

<!-- chunk {"id": "body-0046", "role": "body", "section": "An independent sum of random psd matrices", "weight": 1.0} -->

Srivastava & Vershynin \[:Covariance-Estimation\] formulated this problem and made the first contribution. They considered a random vector $\bm{w}\in\mathbb{R}^{d}$ that satisfies the uniform fourth moment condition They establish a sample complexity bound: Their paper is important because the sample complexity $n$ has the correct (linear) dependence on the dimension $d$, although it exhibits a suboptimal dependence on $\varepsilon$. Their proof employs a Stieltjes transform argument inspired by work in spectral graph theory \[:Twice-Ramanujan\].

<!-- chunk {"id": "body-0047", "role": "body", "section": "An independent sum of random psd matrices", "weight": 1.0} -->

Koltchinskii & Mendelson \[:Bounding-Smallest\] developed a family of related results under a weak form of the moment condition (2.15). For some $\eta>2$, assume that Their work yields the correct dependence on the parameter $\varepsilon$. Indeed, The constant $C=C(\eta,L)$. Their proof involves truncation, small ball probabilities, and a Vapnik--Chervonenkis dimension argument.

<!-- chunk {"id": "body-0048", "role": "body", "section": "An independent sum of random psd matrices", "weight": 1.0} -->

Oliveira \[:Lower-Tail\] proposed a third approach. Under the assumption (2.15), he established that The bound (2.16) has the correct dependence on all of the parameters. Oliveira's argument relies on the PAC-Bayesian method \[:PAC-Bayes,:Simplified-PAC-Bayesian,:Robust-Linear\], a technique that smooths the distribution and employs the variational properties of the entropy to obtain bounds. In Section˜5, we will exploit the Gaussian comparison method to give a short proof of Oliveira's bound (2.16).

<!-- chunk {"id": "body-0049", "role": "body", "section": "An independent sum of random psd matrices", "weight": 1.0} -->

The papers discussed in this section depend heavily on moment assumptions, such as (2.15), which cannot capture the detailed distribution of a random vector. To highlight the benefits of the Gaussian comparison method, we will obtain new bounds for the sample covariance of a very sparse random vector (Theorem˜5.4. ‣ 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Gaussian random matrices", "weight": 1.0} -->

To take advantage of the Gaussian comparison method, we must be able to construct the comparison model and determine its spectral properties. This section outlines some facts about Gaussian random matrices that will play a role in the applications and the proofs of the main theorems. For generality, we work in the complex setting, which includes the real setting as a special case.

<!-- chunk {"id": "body-0051", "role": "body", "section": "The Cartesian decomposition", "weight": 1.0} -->

To simplify some formulas, let us introduce the Cartesian decomposition of a square matrix. The real part and imaginary part of a square matrix $\bm{M}\in\mathbb{M}_{d}(\mathbb{C})$ with complex entries are the self-adjoint matrices The Cartesian decomposition states that $\bm{M}=(\operatorname{Re}\bm{M})+\mathrm{i}(\operatorname{Im}\bm{M})$, and the two terms are orthogonal with respect to the trace inner product.

<!-- chunk {"id": "body-0052", "role": "body", "section": "First and second moments of random matrices", "weight": 1.0} -->

Let $\bm{X}\in\mathbb{H}_{d}(\mathbb{C})$ be a random self-adjoint matrix with complex entries. The second moment function (Definition˜2.2. ‣ 2.2. Second moments and Gaussians ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")) contains information about the second moment of each entry of the random matrix: As usual, $\mathbf{E}_{ij}\in\mathbb{M}_{d}(\mathbb{C})$ is the $(i,j)$ element of the standard basis for matrices. We can extract mixed second moments via polarization. For example, In the last two displays, the range of the indices $i,j,k,\ell=1,\dots,d$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "First and second moments of random matrices", "weight": 1.0} -->

The variance function (Definition˜2.2. ‣ 2.2. Second moments and Gaussians ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")) collects the second moments of the centered random matrix: For random self-adjoint matrices $\bm{X},\bm{Y}\in\mathbb{H}_{d}(\mathbb{C})$, the variance function is additive in the sense that For contrast, the second moment function $\mathsf{Mom}$ does not satisfy the additivity rule (3.1).

<!-- chunk {"id": "body-0054", "role": "body", "section": "First and second moments of random matrices", "weight": 1.0} -->

The first and second moments of a random matrix are equivariant under linear transformations. This fact allows us to transfer the comparison theorems between models. We remark that there are many types of linear transformations that preserve the cone of psd matrices \[:Positive-Definite, Sec. 2.1\].

<!-- chunk {"id": "body-0055", "role": "body", "section": "Matrix Gaussian series", "weight": 1.0} -->

Section˜2.2 provides an abstract definition of a Gaussian random matrix. This section introduces a concrete model that is often useful for calculations. A (self-adjoint) matrix Gaussian series is a random matrix model of the form The coefficients $(\bm{\Delta},\bm{H}_{1},\dots,\bm{H}_{n})$ are deterministic matrices in $\mathbb{H}_{d}(\mathbb{C})$. Let us emphasize that the Gaussian random variables $\gamma_{i}$ are real-valued. Every self-adjoint Gaussian random matrix can be written in the form (3.2) in many different ways.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Matrix Gaussian series", "weight": 1.0} -->

We can easily compute the mean and variance function of the random matrix (3.2): The expression for the variance function follows from the additivity rule (3.1).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Gaussian monotonicity", "weight": 1.0} -->

Gaussian random matrices enjoy a strong monotonicity property. As the variance function increases, expectations of convex functions of the random matrix also increase.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Matrix variance", "weight": 1.0} -->

We can capture information about spectral features of a Gaussian matrix using scalar summary statistics. The matrix variance of a self-adjoint Gaussian matrix $\bm{Z}\in\mathbb{H}_{d}(\mathbb{C})$ is The second identity in (3.6) is valid for an arbitrary representation (3.2) of $\bm{Z}$ as a Gaussian series. When $\bm{Z},\bm{Z}^{\prime}$ are independent, we have the subadditivity rule $\sigma^{2}(\bm{Z}+\bm{Z}^{\prime})\leq\sigma^{2}(\bm{Z})+\sigma^{2}(\bm{Z}^{\prime})$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Matrix variance", "weight": 1.0} -->

The matrix Khinchin inequality \[:Introduction-Matrix, Thm. 4.6.1\]

<!-- chunk {"id": "body-0060", "role": "body", "section": "Fact 3.3 (Matrix Khinchin)", "weight": 1.0} -->

Consider a self-adjoint Gaussian matrix $\bm{Z}$ with dimension $d$. Then In general, the logarithmic factor in (3.7. ‣ 3.5. Matrix variance ‣ 3. Gaussian random matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")) is required. The lower bound stated in (2.12) follows from a sharp moment comparison \[:Gaussian-Measures, Cor. 3\] and Jensen's inequality.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Weak variance", "weight": 1.0} -->

For a self-adjoint Gaussian matrix $\bm{Z}\in\mathbb{H}_{d}(\mathbb{C})$, the weak variance statistic is defined as The second identity holds for an arbitrary representation (3.2) of $\bm{Z}$ as a Gaussian series. As stated in (2.13), the weak variance is controlled by the matrix variance, and both bounds are attainable.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Weak variance", "weight": 1.0} -->

The weak variance can easily be expressed in terms of the variance function: We have written $\|{\cdot}\|_{1}$ for the Schatten $1$-norm. As a consequence, for self-adjoint Gaussian matrices $\bm{Z},\bm{Z}^{\prime}\in\mathbb{H}_{d}(\mathbb{C})$, the weak variance is monotone with respect to the variance function: When $\bm{Z},\bm{Z}^{\prime}$ are independent, we also have the subadditivity rule $\sigma_{*}^{2}(\bm{Z}+\bm{Z}^{\prime})\leq\sigma_{*}^{2}(\bm{Z})+\sigma_{*}^{2}(\bm{Z}^{\prime})$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Weak variance", "weight": 1.0} -->

The weak variance arises when studying concentration properties of Gaussian random matrices.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Fact 3.4 (Gaussian concentration)", "weight": 1.0} -->

Let $h:\mathbb{H}_{d}(\mathbb{C})\to\mathbb{R}$ be a function that is $1$-Lipschitz with respect to the $\ell_{2}$ operator norm: For a self-adjoint Gaussian matrix $\bm{Z}\in\mathbb{H}_{d}(\mathbb{C})$, the mgf of $h(\bm{Z})$ satisfies We can instantiate (3.10. ‣ 3.6. Weak variance ‣ 3. Gaussian random matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")) with $h=\lambda_{\max}$ or $h=\lambda_{\min}$ because of Weyl's inequality \[:Matrix-Analysis, Cor. III.2.6\].

<!-- chunk {"id": "body-0065", "role": "body", "section": "Basic examples", "weight": 1.0} -->

Let us collect some simple Gaussian matrices that we may combine to build comparison models. Indeed, we can represent a Gaussian matrix as a sum of independent Gaussian matrices by breaking the variance function into pieces and identifying a Gaussian model for each piece. This strategy is justified by the additivity (3.1) of the variance. In this section, the random variables $\gamma,\gamma_{i},\gamma_{jk},\smash{\gamma_{jk}^{\prime}}$ are iid $\textsc{normal}_{\mathbb{R}}$. For $v\geq 0$, the distribution $\textsc{normal}_{\mathbb{C}}(0,v)$ generates a complex Gaussian random variable whose real and imaginary parts are iid $\textsc{normal}_{\mathbb{R}}(0,v/2)$ random variables.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Scalar Gaussian matrix", "weight": 1.0} -->

As a warmup, consider the scalar matrix $\bm{S}\coloneqq\gamma\mathbf{I}\in\mathbb{H}_{d}(\mathbb{C})$. It is easy to see that $\operatorname{\mathbb{E}}\lambda_{\min}(\bm{S})=\operatorname{\mathbb{E}}\lambda_{\max}(\bm{S})=0$. The variance function of the scalar matrix acts as Last, note that the matrix variance and weak variance coincide: $\sigma^{2}(\bm{S})=\sigma^{2}_{*}(\bm{S})=1$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Diagonal Gaussian matrix", "weight": 1.0} -->

Next, consider the diagonal matrix: The extreme eigenvalues satisfy This expectation bound is asymptotically sharp. The variance function of the diagonal matrix is The matrix variance and weak variance again coincide: $\sigma^{2}(\bm{D})=\sigma_{*}^{2}(\bm{D})=1$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Gaussian orthogonal ensemble", "weight": 1.0} -->

Now, we turn to a more sophisticated example. A random matrix from the (unnormalized) Gaussian orthogonal ensemble (GOE) takes the form Note that this matrix is real and symmetric. The diagonal entries are iid $\textsc{normal}_{\mathbb{R}}$ random variables, while the entries in the upper triangle are iid $\textsc{normal}_{\mathbb{R}}$ random variables. The key property of the GOE distribution is orthogonal invariance: The extreme eigenvalues of the GOE matrix satisfy an elegant bound \[:Alice-Bob, Exer. 6.48\]: To recognize the GOE matrix, observe that its variance function is The matrix variance and weak variance differ almost as much as possible. Indeed, $\sigma^{2}(\bm{G}_{\mathrm{goe}})=d+1$ and $\sigma_{*}^{2}(\bm{G}_{\mathrm{goe}})=2$. GOE matrices arise in several of our comparisons.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Gaussian unitary ensemble", "weight": 1.0} -->

The Gaussian unitary ensemble (GUE) is the complex cousin of the GOE. A random matrix from this family takes the form The diagonal entries are iid real $\textsc{normal}_{\mathbb{R}}$ random variables, while the entries in the upper triangle are iid complex $\textsc{normal}_{\mathbb{C}}$ random variables. The GUE distribution is unitarily invariant: The extreme eigenvalues of the GUE matrix satisfy the following bound \[:Alice-Bob, Exer. 6.38\].

<!-- chunk {"id": "body-0070", "role": "body", "section": "Gaussian unitary ensemble", "weight": 1.0} -->

The variance function of the GUE matrix acts as The matrix variance and weak variance differ as much as possible: $\sigma^{2}(\bm{G}_{\mathrm{gue}})=d$ and $\sigma_{*}^{2}(\bm{G}_{\mathrm{gue}})=1$. Among all random matrices, the GUE matrix is perhaps the most fundamental.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Application: Sampling from a design", "weight": 1.0} -->

We begin with a geometric example. If we randomly subsample a set of vectors that spans a (complex) linear space, does the reduced set still span the space? In considering this question, we must enforce some regularity properties to avoid situations where most of the vectors fall in a proper subspace. For illustration, we impose a rather strong condition, which ensures that the vectors are distributed evenly across the unit sphere.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Projective designs", "weight": 1.0} -->

Consider a finite system $\mathcal{U}\coloneqq(\bm{u}_{1},\dots,\bm{u}_{n})$ of unit-norm vectors in $\mathbb{C}^{d}$. The system is called a complex projective $t$-design when it yields a quadrature rule for homogeneous degree-$2t$ polynomials on the complex unit sphere $\mathbb{S}^{d-1}(\mathbb{C})$. More precisely, for each vector $\bm{a}\in\mathbb{C}^{d}$, In particular, a projective 1-design is the same as an isotropic system (aka a unit-norm tight frame), so it spans the whole space: We are interested in a projective 2-design, which is characterized by the condition A projective $2$-design is always a projective $1$-design. Examples of projective 2-designs include systems of equiangular vectors, mutually unbiased bases, and other highly symmetric configurations. See \[:Introduction-Finite, Chap.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Projective designs", "weight": 1.0} -->

8\] or \[:Fast-State-Tomography, App. B.1\] for more examples and discussion.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Sampling from a projective design", "weight": 1.0} -->

A classic question in nonasymptotic random matrix theory asks when a random subset of an isotropic system remains a spanning set. The fundamental result for this problem is due to Rudelson \[:Random-Vectors\]; see Section˜4.2.1 for a proof sketch.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Fact 4.1 (Sampling: Projective 1-design)", "weight": 1.0} -->

Consider a complex projective 1-design $\mathcal{U}\coloneqq(\bm{u}_{1},\dots,\bm{u}_{n})$ consisting of $n$ unit-norm vectors in $\smash{\mathbb{C}^{d}}$. For a parameter $1\leq s\leq n$, construct a random subsystem $\mathcal{U}^{\prime}$ with an average of $s$ vectors by uniform sampling: When $s\geq d\log(d/\delta)$, the random system $\mathcal{U}^{\prime}$ spans $\mathbb{C}^{d}$ with probability at least $1-\delta$. The logarithmic factor in the sampling complexity is necessary.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Fact 4.1 (Sampling: Projective 1-design)", "weight": 1.0} -->

As a complement to ˜4.1. ‣ 4.2. Sampling from a projective design ‣ 4. Application: Sampling from a design ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix"), we study the problem of sampling from a complex projective 2-design. We will establish that a random subset remains a spanning set when the average number of vectors exceeds the ambient dimension by a constant factor. The proof appears in Section˜4.2.2.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Application: Sample covariance matrices", "weight": 1.0} -->

Our next application arises from high-dimensional statistics. Suppose that we want to detect which linear marginals of a random vector have strictly positive variance \[:Covariance-Estimation\]. One procedure is to draw iid copies of the random vector and to form the sample covariance matrix. The sample covariance matrix provides estimates for the variance of each marginal. How many samples are sufficient to ensure that none of these estimates is too small?

<!-- chunk {"id": "body-0078", "role": "body", "section": "Application: Sample covariance matrices", "weight": 1.0} -->

Using the Gaussian comparison theorem (Theorem˜2.3. ‣ 2.3. Gaussian comparison: Sum of iid psd random matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")), we can reproduce and extend several major results on sample covariance matrices from the recent literature. When the second moments and fourth moments of the random vector are comparable, then the sampling complexity is proportional to the dimension of the random vector \[:Lower-Tail\]. We can also obtain useful information about the sample covariance matrix of a very sparse random vector \[:Extreme-Singular\].

<!-- chunk {"id": "body-0079", "role": "body", "section": "The sample covariance matrix", "weight": 1.0} -->

Consider a real random vector $\bm{w}\in\mathbb{R}^{d}$ with dimension $d$ that has four finite moments: $\operatorname{\mathbb{E}}\|{\bm{w}}\|^{4}<+\infty$. Assume that the random vector is centered, and introduce the (population) covariance matrix: For simplicity, we also assume that the covariance matrix $\bm{K}$ has full rank $d$. We can compute the variance of a linear marginal of the random vector in terms of the covariance matrix: Our goal is to obtain lower bounds for the variance in every direction, which we call the variance detection problem.

<!-- chunk {"id": "body-0080", "role": "body", "section": "The sample covariance matrix", "weight": 1.0} -->

Suppose that we sample $n$ iid copies of the random vector $\bm{w}$. The sample covariance matrix of this data is the random psd matrix The sample covariance is an unbiased estimator for the true covariance: $\operatorname{\mathbb{E}}[\widehat{\bm{K}}_{n}]=\bm{K}$ for each $n\in\mathbb{N}$. Moreover, the sample covariance matrix provides estimates for the variance of each linear marginal (5.1) of the distribution. For a parameter $\varepsilon\in$, with high probability, we aspire that How many samples $n=n(\bm{w},\varepsilon)$ are sufficient to ensure that the property (5.3) is likely to prevail?

<!-- chunk {"id": "body-0081", "role": "body", "section": "The sample covariance matrix", "weight": 1.0} -->

The answer to this question depends on the distribution of the random vector $\bm{w}$. Since $\bm{K}$ has rank $d$, it is necessary that $n\geq d$ because the rank of the sample covariance matrix $\smash{\widehat{\bm{K}}_{n}}$ does not exceed the number $n$ of samples. For a worst-case vector that satisfies $\|{\bm{w}}\|\lesssim\smash{\sqrt{d}}$, it is necessary to draw $n\asymp d\log d$ samples \[:Random-Vectors\].

<!-- chunk {"id": "body-0082", "role": "body", "section": "The sample covariance matrix", "weight": 1.0} -->

A major technical challenge is to find large classes of random vectors where the sample complexity of (5.3) is proportional to the dimension: $n\asymp d$. This problem has already inspired a vast literature that draws on a diverse set of technical ideas. The Gaussian comparison inequality (Theorem˜2.3. ‣ 2.3. Gaussian comparison: Sum of iid psd random matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")) offers a new methodology for addressing this problem.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Remark 5.1 (Sample covariance: Complex setting)", "weight": 1.0} -->

Our approach adapts to the complex setting with minimal changes. We work in the real setting, as it is more typical in the statistics literature.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Sample covariance: Four moment theorem", "weight": 1.0} -->

Our first result reconstructs a prominent theorem from high-dimensional statistics, in a form due to Oliveira \[:Lower-Tail\]. When the second and fourth moments of a random vector are comparable, then the sample complexity of the variance detection problem is proportional to the dimension. The proof appears below in Section˜5.2.2.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Prior work", "weight": 1.0} -->

Srivastava & Vershynin \[:Covariance-Estimation, Thm. 1.5\] established the first result in the spirit of Theorem˜5.2. ‣ 5.2. Sample covariance: Four moment theorem ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix"), with suboptimal dependence on the parameter $\varepsilon$. Koltchinskii & Mendelson \[:Bounding-Smallest, Thm. 1.3\] obtained improvements to the dependence on $\varepsilon$ with slightly stricter moment assumptions. Oliveira \[:Lower-Tail, Thm. 1.1\] obtained a version of the result stated here, which gives the correct dependence on all the parameters. See Section˜2.8.2 for more discussion.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Prior work", "weight": 1.0} -->

Several papers \[:Covariance-Estimation,:Bounding-Smallest,:Sample-Covariance\] present nonasymptotic bounds on the minimum eigenvalue of the sample covariance assuming control of the $2+\eta$ moments, where $\eta>0$. These conditions are weaker than (5.4. ‣ 5.2. Sample covariance: Four moment theorem ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")). Nevertheless, we will see that the Gaussian comparison method can tease out structure from the random vector that is invisible to a uniform bound on moments (Section˜5.3).

<!-- chunk {"id": "body-0087", "role": "body", "section": "Example: Sparse covariance matrices", "weight": 1.0} -->

For a more challenging example that goes beyond the scope of Theorem˜5.2. ‣ 5.2. Sample covariance: Four moment theorem ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix"), we consider variance detection for a sparse random vector. For simplicity, we treat the case of iid entries, but we only require four finite moments.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Example: Sparse covariance matrices", "weight": 1.0} -->

Fix the dimension $d$, and let $\zeta\in(0,d]$ be a sparsity parameter. Introduce a real random variable $\psi$ that is standardized and has bounded fourth moment: Construct a sparse random vector $\bm{w}\in\mathbb{R}^{d}$ with iid entries: It is straightforward to check that $\bm{w}$ is centered and isotropic, and $\bm{w}$ has $\zeta$ nonzero entries on average. How does the sample complexity of the variance detection problem depend on the sparsity?

<!-- chunk {"id": "body-0089", "role": "body", "section": "Application: Randomized subspace injections", "weight": 1.0} -->

In numerical linear algebra, we can devise randomized algorithms for large-scale matrix computations; for example, see \[:Randomized-Numerical\]. The design and analysis of these algorithms often relies on methods from random matrix theory. In fact, the tools in the present paper were developed to treat challenging mathematical problems from this field.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Application: Randomized subspace injections", "weight": 1.0} -->

A randomized subspace injection is a random linear map whose action preserves the dimension of a fixed subspace \[:Improved-Approximation,:Universality-Laws\]. These injections serve as an important building block for randomized linear algebra algorithms \[:Sketching-Tool,:Randomized-Numerical, MDM+23:Randomized-Numerical\]. In this section, we employ the Gaussian comparison theorem (Theorem 2.3. ‣ 2.3. Gaussian comparison: Sum of iid psd random matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")) to develop a new analysis of subspace injections based on very sparse random matrices \[:Low-Rank-Approximation,:OSNAP-Faster\]. The result largely settles an open question of Nelson & Nguyen \[:OSNAP-Faster,:Lower-Bounds\] that has generated a substantial literature; Section 6.3.1 summarizes the prior work.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Subspace injections", "weight": 1.0} -->

For a given subspace, a subspace injection is a linear map that does not annihilate any vector in that subspace \[:Universality-Laws, Sec. 7.1\].

<!-- chunk {"id": "body-0092", "role": "body", "section": "Remark 6.2 (Subspace embedding \\[:Improved-Approximation\\])", "weight": 1.0} -->

For an orthonormal matrix $\bm{Q}\in\mathbb{R}^{n\times d}$, suppose that $\bm{\Phi}\in\mathbb{R}^{k\times n}$ satisfies the two-sided bound Then we say that $\bm{\Phi}$ is an $(\alpha,\beta)$-subspace embedding for the range of $\bm{Q}$. While it is critical that the contraction factor $\alpha>0$, weak control on the ratio $\beta/\alpha$ suffices for most applications.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Randomized subspace injections", "weight": 1.0} -->

In many applications to computational linear algebra, we must construct a subspace injection without detailed knowledge of the fixed subspace $\bm{Q}$. We can achieve this goal by drawing the matrix $\bm{\Phi}$ at random.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Randomized subspace injections", "weight": 1.0} -->

Consider an isotropic random vector $\bm{\varphi}\in\mathbb{R}^{n}$; that is, $\operatorname{\mathbb{E}}[\bm{\varphi}\bm{\varphi}^{\transp}]=\mathbf{I}_{n}$. The distribution of the random vector $\bm{\varphi}$ is an algorithmic design choice. For an embedding dimension $k$, construct the random matrix Since the rows are isotropic, the random matrix is an isometry on average: The normalization (6.5) is chosen so that $\bm{\Phi}$ typically has a contraction factor $\alpha\leq 1$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Randomized subspace injections", "weight": 1.0} -->

For a fixed subspace $\bm{Q}\in\mathbb{R}^{d\times n}$ and embedding dimension $k$, we want to demonstrate that the random matrix $\bm{\Phi}$ is a subspace injection for the range of $\bm{Q}$ with high probability. Quantitatively, we need to understand how the contraction factor $\alpha$ depends on the embedding dimension $k$. In view of (6.2), it suffices to establish a lower bound on the minimum eigenvalue of the random psd matrix By the construction (6.4), the matrix $\bm{Y}$ is a sum of iid random psd matrices, so we can activate our Gaussian comparison tools (Theorem 2.3. ‣ 2.3. Gaussian comparison: Sum of iid psd random matrices ‣ 2. Main results and related work ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")).

<!-- chunk {"id": "body-0096", "role": "body", "section": "Sparse dimension reduction maps", "weight": 1.0} -->

In computational applications, it is desirable to employ very sparse random matrices as subspace injections. While these maps are widely used \[:Randomized-Numerical, MDM+23:Randomized-Numerical\], no existing analysis justifies the typical parameter choices. We outline prior work in Section 6.3.1.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Sparse dimension reduction maps", "weight": 1.0} -->

Choose an embedding dimension $k\geq d$, and fix the sparsity parameter $\zeta\in(0,k]$. Construct the random vector It is easy to verify that $\bm{\varphi}$ is centered and isotropic. Form the random matrix $\bm{\Phi}$, as in (6.4). Observe that $\bm{\Phi}$ has an average of $\zeta$ nonzero entries per column, for a total of $\zeta n$ nonzero entries on average. We inquire when this sparse random matrix $\bm{\Phi}$ serves as a subspace injection for a fixed subspace. To achieve an embedding dimension $k\asymp d$, what is the minimal sparsity $\zeta$?

<!-- chunk {"id": "body-0098", "role": "body", "section": "Sparse dimension reduction maps", "weight": 1.0} -->

The result depends on a geometric property of the subspace. Define the coherence $\mu(\bm{Q})$ of an orthonormal matrix $\bm{Q}\in\mathbb{R}^{n\times d}$ via The coherence describes the alignment of the range of $\bm{Q}$ with the standard coordinate basis $(\mathbf{e}_{1},\dots,\mathbf{e}_{n})$. It satisfies the inequalities $d/n\leq\mu(\bm{Q})\leq 1$.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Remark 6.4 (Subspace embedding: Sparse random matrix)", "weight": 1.0} -->

To verify the subspace embedding property (Remark 6.2. ‣ 6.1. Subspace injections ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")) of the iid sparse random matrix $\bm{\Phi}$ in Theorem 6.3. ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix"), we can easily obtain adequate upper bounds for the dilation factor $\beta$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Remark 6.4 (Subspace embedding: Sparse random matrix)", "weight": 1.0} -->

For example, with $k\asymp d$ and $\zeta\asymp\mu(\bm{Q})\log d$, This statement follows quickly when we apply the matrix Bernstein inequality \[:Introduction-Matrix, Thm. 6.1.1\] to the decomposition For these parameter choices, the remaining question is whether we can reach the bound $\operatorname{\mathbb{E}}\beta\leq\mathrm{Const}$.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Prior work and discussion", "weight": 1.0} -->

Sarlós \[:Improved-Approximation\] introduced the definition of a subspace embedding (Remark 6.2. ‣ 6.1. Subspace injections ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")). Clarkson & Woodruff \[:Low-Rank-Approximation\] proposed the first construction of a sparse subspace embedding. Soon after, Nelson & Nguyen \[:OSNAP-Faster\] identified more effective constructions, including the iid entry model in Theorem 6.3.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Prior work and discussion", "weight": 1.0} -->

‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") and a related model, called a fixed-sparsity subspace embedding, that has exactly $\zeta$ nonzero entries per column. There are several variants of these sparse subspace embeddings, which offer slightly different advantages and disadvantages. For brevity, we summarize results without listing the details of the embedding constructions.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Prior work and discussion", "weight": 1.0} -->

What are the opportunities for and limitations on sparse subspace embeddings? For any fixed-sparsity subspace embedding with conditioning ratio $\beta/\alpha\eqqcolon 1+\varepsilon$, Nelson & Nguyen \[:Lower-Bounds, Thm. 13\] established lower bounds for the parameters: Bourgain et al. \[:Toward-Unified, Thm. 5\] obtained upper bounds for the parameters of sparse subspace embeddings that identified the role of the coherence statistic $\mu(\bm{Q})$. Using matrix concentration tools, Cohen \[:Nearly-Tight-Oblivious, Thm. 4.2\] obtained upper bounds for fixed-sparsity subspace embeddings: For a long time, Cohen's analysis was the best available, and it has remained a vexing problem to obtain an upper bound that matches the minimal dependence (6.10).

<!-- chunk {"id": "body-0104", "role": "body", "section": "Prior work and discussion", "weight": 1.0} -->

In applications, constants and logarithms are important. Based on computer experiments, Tropp et al. \[:Streaming-Low-Rank\] recommended the following parameter settings for fixed-sparsity subspace embeddings: These parameters work well, but they lack theoretical justification. Regardless, fixed-sparsity subspace embeddings are widely used in computational linear algebra \[:Randomized-Numerical, MDM+23:Randomized-Numerical\].

<!-- chunk {"id": "body-0105", "role": "body", "section": "Prior work and discussion", "weight": 1.0} -->

The last few years have witnessed a burst of new theoretical activity. Cartis et al. \[:Hashing-Embeddings\] established upper bounds that improve over the Bourgain et al. result for subspaces with sufficiently small coherence. Chennakod et al. \[:Optimal-Embedding, Thm. 1.2\] removed the $\log d$ factor from the embedding dimension $k$ at the cost of higher sparsity $\zeta$ by invoking results of Brailovskaya & van Handel \[:Universality-Sharp\]. In the last few months, Chennakod et al. \[:Optimal-Oblivious, Thm. 3.4\] made further improvements to their arguments, reaching the following guarantee for fixed-sparsity subspace embeddings: The latter result is the state of the art. While the embedding dimension $k$ has the optimal form, the excess logarithmic factors in the sparsity $\zeta$ remain a serious limitation.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Prior work and discussion", "weight": 1.0} -->

As outlined, the prior work has focused on sparse subspace embeddings (Remark 6.2. ‣ 6.1. Subspace injections ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")), rather than sparse subspace injections (Definition 6.1. ‣ 6.1. Subspace injections ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")). Nevertheless, the injection property is by far the more important feature, both in theory and in practice; see \[:Universality-Laws, Sec. 7.1\] or \[:Randomized-Numerical, Sec. 8\]. Our result (Theorem 6.3.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Prior work and discussion", "weight": 1.0} -->

‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")) is the first to prove that sparse random matrices serve as subspace injections with (essentially) the minimal dependence (6.10) on the subspace dimension $d$ in both the embedding dimension $k$ and the sparsity $\zeta$. The plain role of the subspace coherence $\mu(\bm{Q})$ is an added bonus.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Remark 6.5 (Fixed-sparsity subspace injection)", "weight": 1.0} -->

We have treated the simplest model for a sparse subspace injection, where the random matrix $\bm{\Phi}$ has iid entries. The Gaussian comparison theorem also allows us to study the injection properties of a certain class of fixed-sparsity random matrices \[:Optimal-Oblivious, Def. 3.2\]. To obtain a $(1-\varepsilon)$-subspace injection, it is sufficient that As compared with Theorem 6.3. ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix"), the subspace coherence $\mu(\bm{Q})$ does not appear in this result.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Remark 6.5 (Fixed-sparsity subspace injection)", "weight": 1.0} -->

As compared with Chennakod et al. \[:Optimal-Oblivious\], we have reduced the dependence on $\log d$ significantly, at the cost of a worse dependence on $\varepsilon$.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Gaussian comparison: Positive scalar sums", "weight": 1.0} -->

The technical development commences in this section. As a warmup, we develop a proof of the lower tail bound for an independent sum of positive scalar random variables.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Completely monotone functions", "weight": 1.0} -->

Our approach takes advantage of a special feature of the decaying exponential that is encapsulated in the next definition.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Tools from Stein's method", "weight": 1.0} -->

The main steps in the analysis are adapted from the literature on Charles Stein's method, a collection of tools for establishing distributional approximations and concentration inequalities. This section outlines some ideas from Stein's method. See the survey of Ross \[:Fundamentals-Steins\] or the book of Chen et al. \[:Normal-Approximation\] for more information.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Tools from Stein's method", "weight": 1.0} -->

To describe the variability in a distribution, we can employ exchangeable pairs of random variables. A pair $(W,Y)$ of real random variables is exchangeable when $(W,Y)\sim(Y,W)$. Equivalently, for every bivariate function $F:\mathbb{R}\times\mathbb{R}\to\mathbb{R}$ where the expectation exists. A pair of iid random variables is the most basic example of an exchangeable pair.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Tools from Stein's method", "weight": 1.0} -->

The next ingredient is an elegant covariance identity. Let $g,h:\mathsf{I}\to\mathbb{R}$ be functions on the interval $\mathsf{I}\subseteq\mathbb{R}$. For an iid pair $(W,Y)$ of random variables taking values in $\mathsf{I}$, This formula can be verified by direct calculation. It is valid whenever the expectations are finite.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Tools from Stein's method", "weight": 1.0} -->

To bound differences of function values, as in (7.5), we employ a formula of Hermite. For a continuously differentiable function $h:\mathsf{I}\to\mathbb{R}$, Identity (7.6) follows from the fundamental theorem of calculus. Moreover, if $h^{\prime}$ is convex on $\mathsf{I}$, then When $w=y$ in (7.6) or (7.7), we interpret the left-hand side as $h^{\prime}(w)$.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Tools from Stein's method", "weight": 1.0} -->

The most important element in our proof of Theorem 7.1. ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") is an association inequality for functions with opposite sense \[:Concentration-Inequalities, Thm. 2.14\]. Assume that $g:\mathsf{I}\to\mathbb{R}$ is increasing, while $h:\mathsf{I}\to\mathbb{R}$ is decreasing. For any random variable $W$ taking values in $\mathsf{I}$, Equivalently, the covariance of $g(W)$ and $h(W)$ is negative.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Tools from Stein's method", "weight": 1.0} -->

To establish the result (7.8), note that Combine this formula with the covariance identity (7.5).

<!-- chunk {"id": "body-0118", "role": "body", "section": "Covariance bounds for completely monotone functions", "weight": 1.0} -->

This section shows how the tools from Stein's method lead to clean bounds for covariances involving a completely monotone function. In particular, this argument applies to the mgf of the lower tail.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Positive sum: mgf bound", "weight": 1.0} -->

With Lemma 7.3. ‣ 7.3. Covariance bounds for completely monotone functions ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") at hand, we quickly obtain a bound for the mgf of a sum of independent, nonnegative random variables.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Gaussian comparison: Randomly weighted sums of psd matrices", "weight": 1.0} -->

In this section, we turn to the proof of Section 2.1, which provides a bound for the minimum eigenvalue of a randomly weighted sum of fixed psd matrices. For technical reasons, we develop the result using slightly different notation and assumptions.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Gaussian comparison: Randomly weighted sums of psd matrices", "weight": 1.0} -->

Fix a system $(\bm{A}_{1},\dots,\bm{A}_{n})$ of psd matrices, with common dimension $d$. These matrices need not be distinct from each other. Consider an independent family $(W_{1},\dots,W_{n})$ of square-integrable, nonnegative real random variables: $W_{i}\geq 0$ and $\operatorname{\mathbb{E}}W_{i}^{2}<+\infty$. Form the random psd matrix We will compare the random psd matrix $\bm{X}$ with an appropriate Gaussian model. Define the deterministic self-adjoint matrices Construct the centered Gaussian matrix Equivalently, $\bm{Z}\sim\textsc{normal}(\bm{0},\mathsf{V})$ with variance function With these definitions, we can state a comparison inequality.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Stahl's theorem: Complete monotonicity of the trace exponential", "weight": 1.0} -->

To prove Theorem 8.1. ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix"), we extend the considerations behind the scalar comparison (Theorem 7.1.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Stahl's theorem: Complete monotonicity of the trace exponential", "weight": 1.0} -->

‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")) to the matrix setting. This strategy depends on a profound fact from matrix analysis, called Stahl's theorem \[:Proof-BMV\].

<!-- chunk {"id": "body-0124", "role": "body", "section": "Fact 8.2 (Stahl's theorem; formerly the BMV conjecture)", "weight": 1.0} -->

Fix self-adjoint matrices $\bm{A},\bm{B}\in\mathbb{H}_{d}$, and assume that $\bm{A}$ is psd. Then the trace exponential function In particular, Lemma 7.3. ‣ 7.3. Covariance bounds for completely monotone functions ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") applies to the function $f$.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Fact 8.2 (Stahl's theorem; formerly the BMV conjecture)", "weight": 1.0} -->

While Stahl's theorem is recent, it has a remarkable history. In 1975, Bessis--Moussa--Villani \[:Monotonic-Converging\] conjectured 8.2. ‣ 8.1. Stahl’s theorem: Complete monotonicity of the trace exponential ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") as part of their method for bounding partition functions of quantum mechanical systems.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Fact 8.2 (Stahl's theorem; formerly the BMV conjecture)", "weight": 1.0} -->

They established the result in two special cases: when $\bm{A},\bm{B}$ commute; or when $\bm{A},\bm{B}$ are $2\times 2$ matrices. Over the next decades, the BMV conjecture received significant attention in mathematical physics, but it was not resolved.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Fact 8.2 (Stahl's theorem; formerly the BMV conjecture)", "weight": 1.0} -->

In 2004, Lieb & Seiringer \[:Equivalent-Forms\] proved that 8.2.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Fact 8.2 (Stahl's theorem; formerly the BMV conjecture)", "weight": 1.0} -->

‣ 8.1. Stahl’s theorem: Complete monotonicity of the trace exponential ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") admits an equivalent formulation: For all psd $\bm{A},\bm{B}\in\mathbb{H}_{d}$, the coefficients of the polynomial $w\mapsto\operatorname{Tr}{}(w\bm{A}+\bm{B})^{p}$ are nonnegative for all $p\in\mathbb{N}$.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Fact 8.2 (Stahl's theorem; formerly the BMV conjecture)", "weight": 1.0} -->

This link with real algebraic geometry ignited a new stage of research, based on sum-of-squares hierarchies and semidefinite programming, that generated new evidence supporting the BMV conjecture.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Fact 8.2 (Stahl's theorem; formerly the BMV conjecture)", "weight": 1.0} -->

Finally, in 2012, Herbert Stahl \[:Proof-BMV\] established 8.2. ‣ 8.1. Stahl’s theorem: Complete monotonicity of the trace exponential ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") using classic methods from complex analysis. Bernstein's theorem (7.3) states that a completely monotone function is the Laplace transform of a finite, positive Borel measure. Roughly speaking, Stahl inverted the Laplace transform to obtain the representing measure. To prove that the representing measure is positive, he exploited the theory of Riemann surfaces.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Fact 8.2 (Stahl's theorem; formerly the BMV conjecture)", "weight": 1.0} -->

See \[:Herbert-Stahls\] for another account of Stahl's proof.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Fact 8.2 (Stahl's theorem; formerly the BMV conjecture)", "weight": 1.0} -->

Very recently, Otte Heinävaara constructed a rather different argument \[:Tracial-Joint, Thm. 2\] that leads to a remarkable generalization of 8.2. ‣ 8.1. Stahl’s theorem: Complete monotonicity of the trace exponential ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Fact 8.3 (Heinävaara's theorem)", "weight": 1.0} -->

Fix self-adjoint matrices $\bm{A},\bm{B}\in\mathbb{H}_{d}$, and assume that $\bm{A}$ is psd. Consider a function $h:\mathbb{R}\to\mathbb{R}$ that is completely monotone to order $K$. Then the trace function Stahl's theorem (8.2.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Fact 8.3 (Heinävaara's theorem)", "weight": 1.0} -->

‣ 8.1. Stahl’s theorem: Complete monotonicity of the trace exponential ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")) follows from the choice $h(w)=\mathrm{e}^{-w}$.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Fact 8.3 (Heinävaara's theorem)", "weight": 1.0} -->

Heinävaara's proof of 8.3. ‣ 8.1. Stahl’s theorem: Complete monotonicity of the trace exponential ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") appeals to a novel object, called a tracial joint spectral measure, that captures the behavior of trace functions of the form $(w,y)\mapsto\operatorname{Tr}h(w\bm{A}+y\bm{B})$ for self-adjoint $\bm{A},\bm{B}$. His techniques yield many deep new statements about trace functions.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Additional tools", "weight": 1.0} -->

The argument involves some standard tools from probability and matrix analysis. First, we record the Gaussian integration by parts (IBP) rule \[:Normal-Approximations, Lem. 1.1.1\].

<!-- chunk {"id": "body-0137", "role": "body", "section": "Fact 8.4 (Gaussian IBP)", "weight": 1.0} -->

Consider iid real standard normal variables $(\gamma_{1},\dots,\gamma_{n})$. For each differentiable function $h:\mathbb{R}^{n}\to\mathbb{R}$, In this formula, $\partial_{i}h$ denotes the partial derivative of $h$ with respect to its $i$th argument. The identity is valid whenever the right-hand side is finite.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Fact 8.4 (Gaussian IBP)", "weight": 1.0} -->

Second, we recall a classic formula from matrix calculus \[:Matrix-Analysis, Example X.4.2(v)\]. For self-adjoint matrices $\bm{A},\bm{H}\in\mathbb{H}_{d}$, the derivative of the exponential at $\bm{A}$ in the direction $\bm{H}$ satisfies As a consequence, the derivative of the trace exponential simplifies to The statement (8.9) follows from (8.8) when we take the trace and cycle to combine the exponentials.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Comparison for the trace mgf", "weight": 1.0} -->

With Stahl's theorem (8.2. ‣ 8.1. Stahl’s theorem: Complete monotonicity of the trace exponential ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")) at hand, we can establish a bound for the trace mgf associated with the minimum eigenvalue of a random psd matrix.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Extension: Polynomial moments", "weight": 1.0} -->

The proof of Proposition 8.5. ‣ 8.3. Comparison for the trace mgf ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") can be adapted to obtain a comparison theorem for one-sided polynomial moments.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Gaussian comparison: Sum of iid random psd matrices", "weight": 1.0} -->

This section develops a comparison theorem for the minimum eigenvalue of a sum of iid random psd matrices. This formulation includes covariance matrices and related models. Surprisingly, this result is a consequence of the comparison (Theorem 8.1. ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")) for sums of randomly weighted psd matrices.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Gaussian comparison: Sum of iid random psd matrices", "weight": 1.0} -->

Let $\bm{W}$ be a random psd matrix with dimension $d$. Assume that $\bm{W}$ is square-integrable: $\operatorname{\mathbb{E}}\|{\bm{W}}\|^{2}<+\infty$. For a fixed natural number $k\in\mathbb{N}$, consider the random psd matrix $\bm{Y}$ obtained by adding $k$ independent copies of $\bm{W}$. That is, We compare the random psd matrix $\bm{Y}$ with an appropriate Gaussian model. Consider a centered Gaussian matrix that follows the distribution With these definitions, we can state another comparison theorem.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Step 1: Empirical approximation", "weight": 1.0} -->

To lighten notation, assume that the shift $\bm{\Delta}\in\mathbb{H}_{d}$ equals the zero matrix. The proof for a general shift is no different.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Step 1: Empirical approximation", "weight": 1.0} -->

For a large parameter $n\in\mathbb{N}$, draw a sample $\mathcal{A}_{n}\coloneqq(\bm{A}_{1},\dots,\bm{A}_{n})$ where the matrices $\bm{A}_{i}$ are iid copies of $\bm{W}$. The sampled matrices may not be distinct. Until the last steps of the proof, we regard the sample $\mathcal{A}_{n}$ as fixed.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Step 1: Empirical approximation", "weight": 1.0} -->

Consider a random matrix $\smash{\widehat{\bm{W}}}$ that takes a uniformly random value from the fixed sample $\mathcal{A}_{n}$: We construct a proxy $\smash{\widehat{\bm{Y}}_{n}}$ for the iid sum $\bm{Y}$ by forming an iid sum of copies of $\smash{\widehat{\bm{W}}}$.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Step 1: Empirical approximation", "weight": 1.0} -->

As a heuristic, when the number $n$ of sample points is large, the distribution of the proxy $\smash{\widehat{\bm{Y}}_{n}}$ is close to the distribution of the original sum $\bm{Y}$. Lemma 9.5. ‣ 9.8. Technical Step 7: Convergence of the empirical model ‣ 9. Gaussian comparison: Sum of iid random psd matrices ‣ 8.4. Extension: Polynomial moments ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") justifies this claim.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Step 2: Multinomial model", "weight": 1.0} -->

To analyze the proxy $\smash{\widehat{\bm{Y}}_{n}}$, we work with an alternative representation. The $k$ independent summands in the proxy take the form For each index $i=1,\dots,n$, define a scalar random variable $\delta_{i}$ that counts the number of the $I_{j}$ that select the index $i$. That is, As a consequence, $\bm{\delta}\coloneqq(\delta_{1},\dots,\delta_{n})\sim\textsc{multinomial}(k,n)$ follows the multinomial distribution of $k$ balls placed independently and uniformly at random in $n$ bins. Recall that Because of the coupling between the distributions, Let us emphasize that the coefficient vector $\bm{\delta}$ is independent from the sample $\mathcal{A}_{n}$.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Step 3: Poissonization", "weight": 1.0} -->

The coefficients $\delta_{i}$ in the representation (9.4) are not independent, but we can pass to a model that has independent coefficients: The Poisson variables $Q_{i}$ are independent from each other and from the multinomial variables $\delta_{i}$. Since $\operatorname{\mathbb{E}}Q_{i}=\operatorname{\mathbb{E}}\delta_{i}$, the conditional expectations of the random matrices $\bm{X}_{n}$ and $\smash{\widehat{\bm{Y}}_{n}}$ coincide.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Step 3: Poissonization", "weight": 1.0} -->

Standard arguments quickly lead to a comparison between the two random models $\smash{\widehat{\bm{Y}}_{n}}$ and $\bm{X}_{n}$.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Remark 9.3 (Poissonization)", "weight": 1.0} -->

The analog of Lemma 9.2. ‣ 9.4. Step 3: Poissonization ‣ 9. Gaussian comparison: Sum of iid random psd matrices ‣ 8.4. Extension: Polynomial moments ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") holds if we replace the trace exponential with any other trace function that is both positive and monotone. In particular, it applies to the one-sided power function $\bm{M}\mapsto\operatorname{Tr}{}(\bm{M})_{-}^{p}$ for $p>0$.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Step 4: Comparison with the Gaussian model", "weight": 1.0} -->

We may now invoke the existing trace mgf bound (Proposition 8.5. ‣ 8.3. Comparison for the trace mgf ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")) to compare the independent model $\bm{X}_{n}$ with a suitable Gaussian matrix.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Step 4: Comparison with the Gaussian model", "weight": 1.0} -->

Conditional on the sample $\mathcal{A}_{n}$, define the variance function Indeed, since $Q_{i}\sim\textsc{poisson}(k/n)$, its second moment is $(1+k/n)(k/n)$. Construct the centered (conditionally) Gaussian random matrix By the law of large numbers, when the number $n$ of samples is large, $\mathsf{V}_{n}\approx\mathsf{V}$, where $\mathsf{V}$ is defined in (9.2). As a consequence, the distribution of $\bm{Z}_{n}$ is close to the distribution of the original Gaussian model $\bm{Z}$ with covariance $\mathsf{V}$. Lemma 9.6. ‣ 9.9. Technical Step 8: Convergence of the Gaussian modelIn Lemma 9.5 (Empirical approximation: Weak convergence).

<!-- chunk {"id": "body-0153", "role": "body", "section": "Step 4: Comparison with the Gaussian model", "weight": 1.0} -->

‣ 9.8. Technical Step 7: Convergence of the empirical model ‣ 9. Gaussian comparison: Sum of iid random psd matrices ‣ 8.4. Extension: Polynomial moments ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4 ‣ 2nd item ‣ 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix"), below, fully justifies this claim.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Step 4: Comparison with the Gaussian model", "weight": 1.0} -->

To compare the trace mgfs of the proxy $\smash{\widehat{\bm{Y}}_{n}}$ and the Gaussian matrix $\bm{Z}_{n}$, first apply the Poissonization result (Lemma 9.2. ‣ 9.4. Step 3: Poissonization ‣ 9. Gaussian comparison: Sum of iid random psd matrices ‣ 8.4. Extension: Polynomial moments ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")). Then invoke the trace mgf bound (Proposition 8.5.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Step 4: Comparison with the Gaussian model", "weight": 1.0} -->

‣ 8.3. Comparison for the trace mgf ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix")), conditional on $\mathcal{A}_{n}$. We arrive at the comparison It remains to relate the random matrices $\smash{\widehat{\bm{Y}}_{n}}$ and $\bm{Z}_{n}$ to the target models $\bm{Y}$ and $\bm{Z}$.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Step 5: Limits", "weight": 1.0} -->

At this stage, we can unfreeze the random sample $\mathcal{A}_{n}$ and take limits. This process will produce the bound The random matrices $\bm{Y}$ and $\bm{Z}$ are defined in (9.1) and (9.2). The remaining steps leading to this result are technical.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Step 5: Limits", "weight": 1.0} -->

First, Lemma 9.4. ‣ 9.7. Technical Step 6: Truncation ‣ 9. Gaussian comparison: Sum of iid random psd matrices ‣ 8.4. Extension: Polynomial moments ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix") shows that it is enough to prove (9.9) under the additional assumption that the random summand $\bm{W}$ is bounded. In this case, we may calculate that The first limit follows from Lemma 9.5.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Step 5: Limits", "weight": 1.0} -->

‣ 9.8. Technical Step 7: Convergence of the empirical model ‣ 9. Gaussian comparison: Sum of iid random psd matrices ‣ 8.4. Extension: Polynomial moments ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4In 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix"). The second relation is the mgf bound (9.5). The second limit follows from Lemma 9.6. ‣ 9.9. Technical Step 8: Convergence of the Gaussian modelIn Lemma 9.5 (Empirical approximation: Weak convergence).

<!-- chunk {"id": "body-0159", "role": "body", "section": "Step 5: Limits", "weight": 1.0} -->

‣ 9.8. Technical Step 7: Convergence of the empirical model ‣ 9. Gaussian comparison: Sum of iid random psd matrices ‣ 8.4. Extension: Polynomial moments ‣ 8. Gaussian comparison: Randomly weighted sums of psd matrices ‣ 7.4. Positive sum: mgf bound ‣ 7. Gaussian comparison: Positive scalar sums ‣ 6.3.2. Proof of Theorem 6.3 ‣ 6.3. Sparse dimension reduction maps ‣ 6. Application: Randomized subspace injections ‣ 5.3.1. Proof of Theorem 5.4 ‣ 2nd item ‣ 5.3. Example: Sparse covariance matrices ‣ 5. Application: Sample covariance matrices ‣ Comparison theorems for the minimum eigenvalue of a random positive-semidefinite matrix"). The details of these computations occupy the upcoming subsections.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Technical Step 6: Truncation", "weight": 1.0} -->

To continue, we restrict our attention to the setting where the random summand $\bm{W}$ is bounded in norm.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Technical Step 7: Convergence of the empirical model", "weight": 1.0} -->

Next, we must verify that the empirical approximations $\smash{\widehat{\bm{Y}}_{n}}$ converge weakly to the original random matrix model $\bm{Y}$.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Technical Step 8: Convergence of the Gaussian model", "weight": 1.0} -->

Finally, we must argue that the sequence $\bm{Z}_{n}$ of Gaussian models converges weakly to the target Gaussian distribution $\bm{Z}$. The proof relies on characteristic functions.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Extension: Polynomial moments", "weight": 1.0} -->

The proof of the trace mgf comparison (9.9) can be adapted to obtain a comparison theorem for polynomial moments.
