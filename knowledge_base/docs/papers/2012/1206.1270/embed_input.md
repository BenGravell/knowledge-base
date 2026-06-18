Factoring Nonnegative Matrices with Linear Programs

Topics include Nonnegative matrix factorization, Linear programming, Separable NMF, Topic modeling, Feature selection, Robust recovery, Large-scale optimization.

Introduces a linear-programming approach to separable nonnegative matrix factorization that identifies representative rows or features and expresses the remaining data through them. Beyond the clean convex formulation, the paper is notable for robustness analysis under more general noise than earlier separable-NMF methods and for showing that the resulting implementation can scale to multi-gigabyte data.

This paper describes a new approach, based on linear programming, for computing nonnegative matrix factorizations (NMFs). The key idea is a data-driven model for the factorization where the most salient features in the data are used to express the remaining features. More precisely, given a data matrix X, the algorithm identifies a matrix C such that X approximately equals CX and some linear constraints. The constraints are chosen to ensure that the matrix C selects features; these features can then be used to find a low-rank NMF of X. A theoretical analysis demonstrates that this approach has guarantees similar to those of the recent NMF algorithm of Arora et al.. In contrast with this earlier work, the proposed method extends to more general noise models and leads to efficient, scalable algorithms. Experiments with synthetic and real datasets provide evidence that the new approach is also superior in practice. An optimized C++ implementation can factor a multigigabyte matrix in a matter of minutes.

## Introduction

Nonnegative matrix factorization (NMF) is a popular approach for selecting features in data. Many machine-learning and data-mining software packages (including Matlab, R, and Oracle Data Mining ) now include heuristic computational methods for NMF. Nevertheless, we still have limited theoretical understanding of when these heuristics are correct.

The difficulty in developing rigorous methods for NMF stems from the fact that the problem is computationally challenging. Indeed, Vavasis has shown that NMF is NP-Hard; see for further worst-case hardness results. As a consequence, we must instate additional assumptions on the data if we hope to compute nonnegative matrix factorizations in practice.

## Discussion

This paper provides an algorithmic and theoretical framework for analyzing and deploying any factorization problem that can be posed as a linear (or convex) factorization localizing program. Future work should investigate the applicability of Hottopixx to other factorization localizing algorithms, such as subspace clustering, and should revisit earlier theoretical bounds on such prior art.

### Theorem 3.2

In particular, the AGKM algorithm computes the factorization exactly when $\epsilon = 0$. Although this method is guaranteed to run in polynomial time, it has many undesirable features. First, the algorithm requires a priori knowledge of the parameters $\alpha$ and $\epsilon$. It may be possible to calculate $\epsilon$, but we can only estimate $\alpha$ if we know which rows are hott. Second, the algorithm computes all $\ell_{1}$ distances between rows at a cost of $O{({f^{2}n})}$....

Dual subgradient ascent solves this problem by alternating between minimizing the Lagrangian over the constraint set $\Phi_{0}$, and then taking a subgradient step with respect to the dual variables

In this spirit, Arora, Ge, Kannan, and Moitra (AGKM) have exhibited a polynomial-time algorithm for NMF that is provably correct---provided that the data is drawn from an appropriate model, based on ideas from. The AGKM result describes one circumstance where we can be sure that NMF algorithms are capable of producing meaningful answers. This work has the potential to make an impact in machine learning because proper feature selection is an important preprocessing step for many other techniques....
