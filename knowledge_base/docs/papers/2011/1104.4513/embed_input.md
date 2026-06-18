Tail Bounds for All Eigenvalues of a Sum of Random Matrices

Topics include Matrix concentration, Random matrices, Eigenvalue tail bounds, Laplace transform method, Chernoff bounds, Bernstein bounds, Covariance estimation.

Extends matrix concentration beyond the largest eigenvalue by introducing a minimax Laplace-transform argument for individual eigenvalue tails. The result gives Chernoff-, Bennett-, and Bernstein-style bounds for all eigenvalues of a sum and illustrates why this matters for sparsification and relative-accuracy covariance estimation.

This work introduces the minimax Laplace transform method, a modification of the cumulant-based matrix Laplace transform method developed in "User-friendly tail bounds for sums of random matrices" (arXiv:1004.4389v6) that yields both upper and lower bounds on each eigenvalue of a sum of random self-adjoint matrices. This machinery is used to derive eigenvalue analogues of the classical Chernoff, Bennett, and Bernstein bounds. Two examples demonstrate the efficacy of the minimax Laplace transform. The first concerns the effects of column sparsification on the spectrum of a matrix with orthonormal rows. Here, the behavior of the singular values can be described in terms of coherence-like quantities. The second example addresses the question of relative accuracy in the estimation of eigenvalues of the covariance matrix of a random process. Standard results on the convergence of sample covariance matrices provide bounds on the number of samples needed to obtain relative accuracy in the spectral norm, but these results only guarantee relative accuracy in the estimate of the maximum eigenvalue....

## Introduction

The field of nonasymptotic random matrix theory has traditionally focused on the problem of bounding the extreme eigenvalues of a random matrix. In some circumstances, however, we may also be interested in studying the behavior of the interior eigenvalues. In this case, classical tools do not readily apply. Indeed, the interior eigenvalues are determined by the min-max of a random process, which is very challenging to control.

This paper demonstrates that it is possible to combine the matrix Laplace transform method detailed in \[\] with the Courant--Fischer characterization of eigenvalues to obtain nontrivial bounds on the interior eigenvalues of a sum of random self-adjoint matrices. This approach expands the scope of the matrix probability inequalities from \[\] so that they provide interesting information about the bulk spectrum.

Combine this result with (7.8) to see that

Complete the proof by using this estimate in (7.6).

### Lemma 5.2

Intuitively, the eigenvalue tail bounds should depend on how concentrated the summands are; e.g., the maximum eigenvalue of a sum of operators whose ranges are aligned is likely to vary more than that of a sum of operators whose ranges are orthogonal. To measure how much a finite sequence of random summands $\{{\mathbf{X}}_{j}\}$ concentrates in a given subspace, we define a function $\Psi:{{\bigcup_{1 \leq k \leq n}{\mathbb{V}}_{k}^{n}}\rightarrow{\mathbb{R}}}$ that satisfies

### Theorem 6.1 (Column Subsampling of Matrices with Orthonormal Rows)

As one application of our approach, we investigate estimates for the covariance matrix of a centered stationary random process. We show that the eigenvalues of the sample covariance matrix provide relative-error approximations to the eigenvalues of the covariance matrix. We focus on Gaussian processes, but our arguments can be extended to other distributions. The following theorem distills the results in section 7.

### Theorem 1.1

Let $\kappa_{\ell}$ be the condition number associated with a dominant $\ell$-dimensional invariant subspace of $\mathbf{C},$

Thus, assuming sufficiently fast decay of the residual eigenvalues, $n = {\Omega{({\varepsilon^{- 2}\kappa_{\ell}^{2}\ell{\log p}})}}$ samples ensure that the top $\ell$ eigenvalues of $\mathbf{C}$ are captured to relative precision....
