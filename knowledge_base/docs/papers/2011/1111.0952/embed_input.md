Computing a Nonnegative Matrix Factorization - Provably

Topics include Nonnegative matrix factorization, Separable NMF, Provable algorithms, Matrix factorization, Polynomial time algorithm, Topic model, Computational complexity.

Identifies separability conditions under which nonnegative matrix factorization becomes tractable and gives polynomial-time algorithms for exact and approximate NMF in those regimes. The paper is important because it turns a widely used heuristic matrix factorization problem into a provable algorithmic setting connected to topics and mixture models.

In the Nonnegative Matrix Factorization (NMF) problem we are given an n x m nonnegative matrix M and an integer r > 0. Our goal is to express M as A W where A and W are nonnegative matrices of size n x r and r x m respectively. In some applications, it makes sense to ask instead for the product AW to approximate M - i.e. (approximately) minimize normM - AW_F where norm{}_F denotes the Frobenius norm; we refer to this as Approximate NMF. This problem has a rich history spanning quantum mechanics, probability theory, data analysis, polyhedral combinatorics, communication complexity, demography, chemometrics, etc. In the past decade NMF has become enormously popular in machine learning, where A and W are computed using a variety of local search heuristics. Vavasis proved that this problem is NP-complete. We initiate a study of when this problem is solvable in polynomial time: 1. We give a polynomial-time algorithm for exact and approximate NMF for every constant r. Indeed NMF is most interesting in applications precisely when r is small. 2. We complement this with a hardness result, that if exact NMF can be solved in time (nm)^(o)(r), 3-SAT has a sub-exponential time algorithm.

## Introduction

In the Nonnegative Matrix Factorization (NMF) problem we are given an $n \times m$ matrix $M$ with nonnegative real entries (such a matrix will be henceforth called "nonnegative") and an integer $r > 0$. Our goal is to express $M$ as $AW$ where $A$ and $W$ are nonnegative matrices of size $n \times r$ and $r \times m$ respectively. We refer to $r$ as the inner-dimension of the factorization and the smallest value of $r$ for which there is such a factorization as the nonnegative rank of $M$.

NMF is a fundamental problem that has been independently introduced in a number of different contexts and applications. Many interesting heuristics and local search algorithms (including the familiar Expectation Maximization or EM) have been proposed to find such factorizations. One compelling family of applications is data analysis, where a nonnegative factorization is computed in order to extract certain latent relationships in the data and has been applied to image segmentation, information retrieval and document clustering.

## Question 1.1

Can a nonnegative matrix factorization be computed efficiently when the inner-dimension, $r$, is small?

Vavasis recently proved that the NMF problem is $NP$-hard when $r$ is large, but this only rules out an algorithm whose running time is polynomial in $n$, $m$ and $r$. Arguably, in most significant applications, $r$ is small. Usually the algorithm designer posits a two-level generative model for the data and uses NMF to compute "hidden" variables that explain the data. This explanation is only interesting when the number of hidden variables ($r$) is much smaller than the number of examples ($m$) or the number of observations per example ($n$).
