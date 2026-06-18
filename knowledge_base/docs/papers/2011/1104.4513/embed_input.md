Tail Bounds for All Eigenvalues of a Sum of Random Matrices

Topics include Matrix concentration, Random matrices, Eigenvalue tail bounds, Laplace transform method, Chernoff bounds, Bernstein bounds, Covariance estimation.

Extends matrix concentration beyond the largest eigenvalue by introducing a minimax Laplace-transform argument for individual eigenvalue tails. The result gives Chernoff-, Bennett-, and Bernstein-style bounds for all eigenvalues of a sum and illustrates why this matters for sparsification and relative-accuracy covariance estimation.

This work introduces the minimax Laplace transform method, a modification of the cumulant-based matrix Laplace transform method developed in "User-friendly tail bounds for sums of random matrices" (arXiv:1004.4389v6) that yields both upper and lower bounds on each eigenvalue of a sum of random self-adjoint matrices. This machinery is used to derive eigenvalue analogues of the classical Chernoff, Bennett, and Bernstein bounds. Two examples demonstrate the efficacy of the minimax Laplace transform. The first concerns the effects of column sparsification on the spectrum of a matrix with orthonormal rows. Here, the behavior of the singular values can be described in terms of coherence-like quantities. The second example addresses the question of relative accuracy in the estimation of eigenvalues of the covariance matrix of a random process. Standard results on the convergence of sample covariance matrices provide bounds on the number of samples needed to obtain relative accuracy in the spectral norm, but these results only guarantee relative accuracy in the estimate of the maximum eigenvalue.

## Introduction

The field of nonasymptotic random matrix theory has traditionally focused on the problem of bounding the extreme eigenvalues of a random matrix. In some circumstances, however, we may also be interested in studying the behavior of the interior eigenvalues. In this case, classical tools do not readily apply. Indeed, the interior eigenvalues are determined by the min-max of a random process, which is very challenging to control.

This paper demonstrates that it is possible to combine the matrix Laplace transform method detailed with the Courant--Fischer characterization of eigenvalues to obtain nontrivial bounds on the interior eigenvalues of a sum of random self-adjoint matrices. This approach expands the scope of the matrix probability inequalities so that they provide interesting information about the bulk spectrum.

As one application of our approach, we investigate estimates for the covariance matrix of a centered stationary random process. We show that the eigenvalues of the sample covariance matrix provide relative-error approximations to the eigenvalues of the covariance matrix. We focus on Gaussian processes, but our arguments can be extended to other distributions. The following theorem distills the results in section 7.

## Outline

In section 2, we introduce the notation used in this paper and state a convenient version of the Courant--Fischer theorem. In section 3, we use the Courant--Fischer theorem to extend the Laplace transform technique to apply to all the eigenvalues of self-adjoint matrices, thereby obtaining the minimax Laplace transform. We apply this technique in sections 4 and 5 to develop eigenvalue analogs of the classical Chernoff and Bernstein bounds. The final two sections illustrate, using two familiar problems, that the minimax Laplace technique gives us significantly more information on the spectra of random matrices than current approaches.
