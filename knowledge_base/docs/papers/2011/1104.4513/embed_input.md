<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Tail Bounds for All Eigenvalues of a Sum of Random Matrices

Topics include Matrix concentration, Random matrices, Eigenvalue tail bounds, Laplace transform method, Chernoff bounds, Bernstein bounds, Covariance estimation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends matrix concentration beyond the largest eigenvalue by introducing a minimax Laplace-transform argument for individual eigenvalue tails. The result gives Chernoff-, Bennett-, and Bernstein-style bounds for all eigenvalues of a sum and illustrates why this matters for sparsification and relative-accuracy covariance estimation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This work introduces the minimax Laplace transform method, a modification of the cumulant-based matrix Laplace transform method developed in "User-friendly tail bounds for sums of random matrices" (arXiv:1004.4389v6) that yields both upper and lower bounds on each eigenvalue of a sum of random self-adjoint matrices. This machinery is used to derive eigenvalue analogues of the classical Chernoff, Bennett, and Bernstein bounds. Two examples demonstrate the efficacy of the minimax Laplace transform. The first concerns the effects of column sparsification on the spectrum of a matrix with orthonormal rows. Here, the behavior of the singular values can be described in terms of coherence-like quantities. The second example addresses the question of relative accuracy in the estimation of eigenvalues of the covariance matrix of a random process. Standard results on the convergence of sample covariance matrices provide bounds on the number of samples needed to obtain relative accuracy in the spectral norm, but these results only guarantee relative accuracy in the estimate of the maximum eigenvalue.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The minimax Laplace transform argument establishes that if the lowest eigenvalues decay sufficiently fast, on the order of (K^2*r*log(p))/eps^2 samples, where K is the condition number of an optimal rank-r approximation to C, are sufficient to ensure that the dominant r eigenvalues of the covariance matrix of a N(0, C) random vector are estimated to within a factor of 1+-eps with high probability.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The field of nonasymptotic random matrix theory has traditionally focused on the problem of bounding the extreme eigenvalues of a random matrix. In some circumstances, however, we may also be interested in studying the behavior of the interior eigenvalues. In this case, classical tools do not readily apply. Indeed, the interior eigenvalues are determined by the min-max of a random process, which is very challenging to control.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper demonstrates that it is possible to combine the matrix Laplace transform method detailed with the Courant--Fischer characterization of eigenvalues to obtain nontrivial bounds on the interior eigenvalues of a sum of random self-adjoint matrices. This approach expands the scope of the matrix probability inequalities so that they provide interesting information about the bulk spectrum.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

As one application of our approach, we investigate estimates for the covariance matrix of a centered stationary random process. We show that the eigenvalues of the sample covariance matrix provide relative-error approximations to the eigenvalues of the covariance matrix. We focus on Gaussian processes, but our arguments can be extended to other distributions. The following theorem distills the results in section 7.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Outline", "weight": 1.0} -->

In section 2, we introduce the notation used in this paper and state a convenient version of the Courant--Fischer theorem. In section 3, we use the Courant--Fischer theorem to extend the Laplace transform technique to apply to all the eigenvalues of self-adjoint matrices, thereby obtaining the minimax Laplace transform. We apply this technique in sections 4 and 5 to develop eigenvalue analogs of the classical Chernoff and Bernstein bounds. The final two sections illustrate, using two familiar problems, that the minimax Laplace technique gives us significantly more information on the spectra of random matrices than current approaches. In section 6, we use the Chernoff bounds to quantify the effects of column sparsification on all the singular values of matrices with orthogonal rows. In section 7, we consider the question of how fast, in relative error, the eigenvalues of empirical covariance matrices converge.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Tail Bounds For Interior Eigenvalues", "weight": 1.0} -->

In this section we develop a generic bound on the tail probabilities of eigenvalues of sums of independent, random, self-adjoint matrices. We establish this bound by supplementing the matrix Laplace transform methodology of with Proposition 2.1. ‣ 2. Background and Notation ‣ Tail Bounds for All Eigenvalues of A Sum of Random Matrices") and a new result, due to Lieb and Seiringer, on the concavity of a certain trace function on the cone of positive-definite matrices.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Tail Bounds For Interior Eigenvalues", "weight": 1.0} -->

First we observe that the Courant--Fischer theorem allows us relate the behavior of the $k$th eigenvalue of a matrix to the behavior of the largest eigenvalue of an appropriate compression of the matrix.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Chernoff bounds", "weight": 1.0} -->

Classical Chernoff bounds establish that the tails of a sum of independent nonnegative random variables decay subexponentially. develops Chernoff bounds for the maximum and minimum eigenvalues of a sum of independent positive-semidefinite matrices. We extend this analysis to study the interior eigenvalues.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Chernoff bounds", "weight": 1.0} -->

Intuitively, the eigenvalue tail bounds should depend on how concentrated the summands are; e.g., the maximum eigenvalue of a sum of operators whose ranges are aligned is likely to vary more than that of a sum of operators whose ranges are orthogonal. To measure how much a finite sequence of random summands $\{{\mathbf{X}}_{j}\}$ concentrates in a given subspace, we define a function $\Psi:{{\bigcup_{1 \leq k \leq n}{\mathbb{V}}_{k}^{n}}\rightarrow{\mathbb{R}}}$ that satisfies The sequence $\{{\mathbf{X}}_{j}\}$ associated with $\Psi$ will always be clear from context. We have the following result.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

If it is difficult to estimate $\Psi{({\mathbf{V}}_{+})}$ or ${\Psi{({\mathbf{V}}_{-})}},$ one can resort to the weaker estimates Theorem 4.1. ‣ 4. Chernoff bounds ‣ Tail Bounds for All Eigenvalues of A Sum of Random Matrices") follows from Theorem 3.3. ‣ 3. Tail Bounds For Interior Eigenvalues ‣ Tail Bounds for All Eigenvalues of A Sum of Random Matrices") using an appropriate bound on the matrix moment generating functions. The following lemma is due to Ahlswede and Winter; see also \[, Lem. 5.8\].

<!-- chunk {"id": "body-0014", "role": "body", "section": "Bennett and Bernstein inequalities", "weight": 1.0} -->

The classical Bennett and Bernstein inequalities use the variance or knowledge of the moments of the summands to control the probability that a sum of independent random variables deviates from its mean. In, matrix Bennett and Bernstein inequalities are developed for the extreme eigenvalues of self-adjoint random matrix sums. We establish that the interior eigenvalues satisfy analogous inequalities.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Bennett and Bernstein inequalities", "weight": 1.0} -->

As in the derivation of the Chernoff inequalities of section 4, we need a measure of how concentrated the random summands are in a given subspace. Recall that the function $\Psi:{{\bigcup_{1 \leq k \leq n}{\mathbb{V}}_{k}^{n}}\rightarrow{\mathbb{R}}}$ satisfies The sequence $\{{\mathbf{X}}_{j}\}$ associated with $\Psi$ will always be clear from context.

<!-- chunk {"id": "body-0016", "role": "body", "section": "An application to column subsampling", "weight": 1.0} -->

As an application of our Chernoff bounds, we examine how sampling columns from a matrix with orthonormal rows affects the spectrum. This question has applications in numerical linear algebra and compressed sensing. The special cases of the maximum and minimum eigenvalues have been studied in the literature. The limiting spectral distributions of matrices formed by sampling columns from similarly structured matrices have also been studied: the results of apply to matrices formed by sampling columns from any fixed orthogonal matrix, and studies matrices formed by sampling columns and rows from the discrete Fourier transform matrix. We mention in particular, the main result of which provides a uniform bound on the tails of all singular values of the sampled matrix. The theorem proven in this section provides bounds which reflect the differences in the tails of the individual singular values, and thus can be viewed as an elaboration of the result.

<!-- chunk {"id": "body-0017", "role": "body", "section": "An application to column subsampling", "weight": 1.0} -->

Let $\mathbf{U}$ be an $n \times r$ matrix with orthonormal rows. We model the sampling operation using a random diagonal matrix $\mathbf{D}$ whose entries are independent $\text{Bern}{(p)}$ random variables. Then the random matrix can be interpreted as a random column submatrix of $\mathbf{U}$ with an average of $pr$ nonzero columns.

<!-- chunk {"id": "body-0018", "role": "body", "section": "An application to column subsampling", "weight": 1.0} -->

Our goal is to study the behavior of the spectrum of $\hat{\mathbf{U}}.$ Recall that the $j$th column of $\mathbf{U}$ is written ${\mathbf{u}}_{j}.$ Consider the following coherence-like quantity associated with ${\mathbf{U}}:$ There does not seem to be a simple expression for $\tau_{k}.$ However, by choosing ${\mathbf{V}}^{\ast}$ to be the restriction to an appropriate $k$-dimensional coordinate subspace, we see that $\tau_{k}$ always satisfies The following theorem shows that the behavior of ${s_{k}{(\hat{\mathbf{U}})}},$ the $k$th singular value of $\hat{\mathbf{U}},$ can be explained in terms of $\tau_{k}.$

<!-- chunk {"id": "body-0019", "role": "body", "section": "Covariance Estimation", "weight": 1.0} -->

We conclude with an extended example that illustrates how this circle of ideas allows one to answer interesting statistical questions. Specifically, we investigate the convergence of the individual eigenvalues of sample covariance matrices, with errors measured in *relative* precision.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Covariance Estimation", "weight": 1.0} -->

Covariance estimation is a basic and ubiquitious problem that arises in signal processing, graphical modeling, machine learning, and genomics, among other areas. Let ${\{{\mathbf{η}}_{j}\}}_{j = 1}^{n} \subset {\mathbb{R}}^{p}$ be i.i.d. samples drawn from some distribution with zero mean and covariance matrix ${\mathbf{C}}.$ Define the sample covariance matrix An important challenge is to determine how many samples are needed to ensure that the empirical covariance estimator has a fixed relative accuracy in the spectral norm. That is, given a fixed $\varepsilon,$ how large must $n$ be so that This estimation problem has been studied extensively. It is now known that for distributions with a finite second moment, $\Omega{({p{\log p}})}$ samples suffice, and for log-concave distributions, $\Omega{(p)}$ samples suffice.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Covariance Estimation", "weight": 1.0} -->

More broadly, Vershynin conjectures that, for distributions with finite fourth moment, $\Omega{(p)}$ samples suffice; he establishes this result to within iterated log factors. In, Srivastava and Vershynin establish that $\Omega{(p)}$ samples suffice for distributions which have finite $2 + \varepsilon$ moments, for some ${\varepsilon > 0},$ and satisfy an additional regularity condition.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Covariance Estimation", "weight": 1.0} -->

Inequality (7.1) ensures that the difference between the $k$th eigenvalues of ${\hat{\mathbf{C}}}_{n}$ and $\mathbf{C}$ is small, but it requires $O{(p)}$ measurements to obtain estimates of even a few of the eigenvalues. Specifically, letting ${\kappa_{\ell} = {{{\lambda_{1}{({\mathbf{C}})}}/\lambda_{\ell}}{({\mathbf{C}})}}},$ we see that $O{({\varepsilon^{- 2}\kappa_{\ell}^{2}p})}$ measurements are required to obtain relative-error estimates of the dominant $\ell$ eigenvalues of $\mathbf{C}$ using the results of.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Covariance Estimation", "weight": 1.0} -->

However, it is reasonable to expect that when the spectrum of $\mathbf{C}$ exhibits decay and ${\ell \ll p},$ much fewer than $O{(p)}$ measurements should suffice for relative-error recovery of the dominant $\ell$ eigenvalues.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Covariance Estimation", "weight": 1.0} -->

In this section, we derive a relative approximation bound for each eigenvalue of $\mathbf{C}$ that allows us to confirm this intuition. For simplicity we assume the samples are drawn from a $\mathcal{N}{(\mathbf{0},{\mathbf{C}})}$ distribution where $\mathbf{C}$ is full-rank, but the arguments can be extended to cover other distributions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 7.1", "weight": 1.0} -->

The results in Theorem 7.1 and Corollary 7.2 also apply when $\mathbf{C}$ is rank-deficient: simply replace each occurence of the dimension $p$ in the bounds with ${{rank}{({\mathbf{C}})}}.$

<!-- chunk {"id": "body-0026", "role": "body", "section": "Extensions of Theorem 7.1", "weight": 1.0} -->

Results analogous to Theorem 7.1 can be established for other distributions. If the distribution is bounded, the possibility that ${\hat{\lambda}}_{k}$ deviates above or below $\lambda_{k}$ can be controlled using the Bernstein inequality of Theorem 5.1. ‣ 5. Bennett and Bernstein inequalities ‣ Tail Bounds for All Eigenvalues of A Sum of Random Matrices"). If the distribution is unbounded but has matrix moments that satisfy a sufficiently nice growth condition, the probability that ${\hat{\lambda}}_{k}$ deviates below $\lambda_{k}$ as well as the probability that it deviates above $\lambda_{k}$ can be bounded using a Bernstein inequality analogous to that in Theorem 5.3. ‣ 5. Bennett and Bernstein inequalities ‣ Tail Bounds for All Eigenvalues of A Sum of Random Matrices").

<!-- chunk {"id": "body-0027", "role": "body", "section": "Extensions of Theorem 7.1", "weight": 1.0} -->

Theorem 7.1 controls the error in the $k$th sample eigenvalue in terms of all the eigenvalues of the covariance matrix, so it is most useful when the eigenvalues of the covariance matrix satisfy decay conditions such as those given in the statement of Theorem 1.1. If such conditions are not satisfied, the results of on the convergence of empirical covariance matrices of isotropic log-concave random vectors lead to tighter bounds on the probabilities that ${\hat{\lambda}}_{k}$ overestimates or underestimates $\lambda_{k}.$ To see the relevance of the results, first observe the following consequence of the subadditivity of the maximum eigenvalue mapping: In conjunction with (7.2), this gives us the following control on the probability that $\lambda_{k}{({\mathbf{X}})}$ overestimates ${\lambda_{k}{({\mathbf{A}})}}:$ In our application, $\mathbf{X}$ is the empirical covariance matrix and

<!-- chunk {"id": "body-0028", "role": "body", "section": "Extensions of Theorem 7.1", "weight": 1.0} -->

$\mathbf{A}$ is the actual covariance matrix.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Extensions of Theorem 7.1", "weight": 1.0} -->

${\hat{\lambda}}_{k}$ overestimating or underestimating $\lambda_{k}$ can be tightened beyond those suggested in Theorem 7.1 by using the results or. Note, however, that one cannot use knowledge of spectral decay to sharpen the results obtained and into estimates like those given in Theorem 1.1.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Extensions of Theorem 7.1", "weight": 1.0} -->

Finally, we note that the techniques developed in the proof of Theorem 7.1 can be used to investigate the spectrum of the error matrices ${{\hat{\mathbf{C}}}_{n} - {\mathbf{C}}}.$

<!-- chunk {"id": "body-0031", "role": "body", "section": "Proofs of the supporting lemmas", "weight": 1.0} -->

We now establish the lemmas used in the proof of Theorem 7.1.
