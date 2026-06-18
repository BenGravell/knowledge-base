Factoring Nonnegative Matrices with Linear Programs

Topics include Nonnegative matrix factorization, Linear programming, Separable NMF, Topic modeling, Feature selection, Robust recovery, Large-scale optimization.

Introduces a linear-programming approach to separable nonnegative matrix factorization that identifies representative rows or features and expresses the remaining data through them. Beyond the clean convex formulation, the paper is notable for robustness analysis under more general noise than earlier separable-NMF methods and for showing that the resulting implementation can scale to multi-gigabyte data.

This paper describes a new approach, based on linear programming, for computing nonnegative matrix factorizations (NMFs). The key idea is a data-driven model for the factorization where the most salient features in the data are used to express the remaining features. More precisely, given a data matrix X, the algorithm identifies a matrix C such that X approximately equals CX and some linear constraints. The constraints are chosen to ensure that the matrix C selects features; these features can then be used to find a low-rank NMF of X. A theoretical analysis demonstrates that this approach has guarantees similar to those of the recent NMF algorithm of Arora et al.. In contrast with this earlier work, the proposed method extends to more general noise models and leads to efficient, scalable algorithms. Experiments with synthetic and real datasets provide evidence that the new approach is also superior in practice. An optimized C++ implementation can factor a multigigabyte matrix in a matter of minutes.

## Introduction

Nonnegative matrix factorization (NMF) is a popular approach for selecting features in data. Many machine-learning and data-mining software packages (including Matlab, R, and Oracle Data Mining ) now include heuristic computational methods for NMF. Nevertheless, we still have limited theoretical understanding of when these heuristics are correct.

The difficulty in developing rigorous methods for NMF stems from the fact that the problem is computationally challenging. Indeed, Vavasis has shown that NMF is NP-Hard; see for further worst-case hardness results. As a consequence, we must instate additional assumptions on the data if we hope to compute nonnegative matrix factorizations in practice.

The present work presents a scalable, robust algorithm that can successfully solve the NMF problem under appropriate hypotheses. Our first contribution is a new formulation of the nonnegative feature selection problem that only requires the solution of a single linear program. Second, we provide a theoretical analysis of this algorithm. This argument shows that our method succeeds under the same modeling assumptions as the AGKM algorithm with an additional *margin constraint* that is common in machine learning.

In addition to these theoretical contributions, our work also includes a major algorithmic and experimental component. Our formulation of NMF allows us to exploit methods from operations research and database systems to design solvers that scale to extremely large datasets. We develop an efficient stochastic gradient descent (SGD) algorithm that is (at least) two orders of magnitude faster than the approach of AGKM when both are implemented in Matlab. We describe a parallel implementation of our SGD algorithm that can robustly factor matrices with $10^{5}$ features and $10^{6}$ examples in a few minutes on a multicore workstation.

## Discussion

This paper provides an algorithmic and theoretical framework for analyzing and deploying any factorization problem that can be posed as a linear (or convex) factorization localizing program. Future work should investigate the applicability of Hottopixx to other factorization localizing algorithms, such as subspace clustering, and should revisit earlier theoretical bounds on such prior art.
