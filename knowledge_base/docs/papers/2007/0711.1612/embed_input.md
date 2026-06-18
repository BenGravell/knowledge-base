Enhancing Sparsity by Reweighted L1 Minimization

Topics include Compressed sensing, Sparse recovery, Reweighted L1, Convex optimization, Iterative reweighting, Signal reconstruction.

Proposes solving a sequence of weighted L1 problems to better approximate sparsity than a single unweighted relaxation. The simple iterative reweighting rule often recovers sparse signals from fewer measurements and became a standard heuristic in compressed sensing and sparse modeling.

It is now well understood that it is possible to reconstruct sparse signals exactly from what appear to be highly incomplete sets of linear measurements and that this can be done by constrained L1 minimization. In this paper, we study a novel method for sparse signal recovery that in many situations outperforms L1 minimization in the sense that substantially fewer measurements are needed for exact recovery. The algorithm consists of solving a sequence of weighted L1-minimization problems where the weights used for the next iteration are computed from the value of the current solution. We present a series of experiments demonstrating the remarkable performance and broad applicability of this algorithm in the areas of sparse signal recovery, statistical estimation, error correction and image processing. Interestingly, superior gains are also achieved when our method is applied to recover signals with assumed near-sparsity in overcomplete representations - not by reweighting the L1 norm of the coefficient sequence as is common, but by reweighting the L1 norm of the transformed object.

## Introduction

What makes some scientific or engineering problems at once interesting and challenging is that often, one has fewer equations than unknowns. When the equations are linear, one would like to determine an object $x_{0} \in {\mathbb{R}}^{n}$ from data $y = {\Phix_{0}}$, where $\Phi$ is an $m \times n$ matrix with fewer rows than columns; i.e., $m < n$. The problem is of course that a system with fewer equations than unknowns usually has infinitely many solutions and thus, it is apparently impossible to identify which of these candidate solutions is indeed the "correct" one without some additional information.

The use of $\ell_{1}$ regularization has become so widespread that it could arguably be considered the "modern least squares". This raises the question of whether we can improve upon $\ell_{1}$ minimization? It is natural to ask, for example, whether a different (but perhaps again convex) alternative to $\ell_{0}$ minimization might also find the correct solution, but with a lower measurement requirement than $\ell_{1}$ minimization.

In this paper, we consider one such alternative, which aims to help rectify a key difference between the $\ell_{1}$ and $\ell_{0}$ norms, namely, the dependence on magnitude: larger coefficients are penalized more heavily in the $\ell_{1}$ norm than smaller coefficients, unlike the more democratic penalization of the $\ell_{0}$ norm. To address this imbalance, we propose a weighted formulation of $\ell_{1}$ minimization designed to more democratically penalize nonzero coefficients.

## Discussion

In summary, reweighted $\ell_{1}$ minimization outperforms plain $\ell_{1}$ minimization in a variety of setups. Therefore, this technique might be of interest to researchers in the field of compressed sensing and/or statistical estimation as it might help to improve the quality of reconstructions and/or estimations. Further, this technique is easy to deploy as it can be built on top of existing $\ell_{1}$ solvers and the number of iterations is typically very low so that the additional computational cost is not prohibitive. We conclude this paper by discussing related work and possible future directions.
