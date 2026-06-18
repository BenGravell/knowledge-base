Randomized Numerical Linear Algebra: Foundations & Algorithms

This survey describes probabilistic algorithms for linear algebra computations, such as factorizing matrices and solving linear systems. It focuses on techniques that have a proven track record for real-world problem instances. The paper treats both the theoretical foundations of the subject and the practical computational issues. Topics covered include norm estimation; matrix approximation by sampling; structured and unstructured random embeddings; linear regression problems; low-rank approximation; subspace iteration and Krylov methods; error estimation and adaptivity; interpolatory and CUR factorizations; Nyström approximation of positive-semidefinite matrices; single view ("streaming") algorithms; full rank-revealing factorizations; solvers for linear systems; and approximation of kernel matrices that arise in machine learning and in scientific computing.

## Introduction

Numerical linear algebra (NLA) is one of the great achievements of scientific computing. On most computational platforms, we can now routinely and automatically solve small- and medium-scale linear algebra problems to high precision. The purpose of this survey is to describe a set of probabilistic techniques that have joined the mainstream of NLA over the last decade. These new techniques have accelerated everyday computations for small- and medium-size problems, and they have enabled large-scale computations that were beyond the reach of classical methods.

### Classical numerical linear algebra

? focuses on computational aspects of randomized NLA. A distinctive feature is the discussion of efficient algorithms for factorizing matrices of full, or nearly full, rank.

? gives a mathematical treatment of how matrix concentration supports a few randomized NLA algorithms, and includes a complete proof of correctness for the SparseCholesky algorithm described in Section 18.

Another idea is to apply randomized sampling to control sparsity levels. This technique arises in Section 18, which contains a randomized algorithm that accelerates incomplete Cholesky preconditioning for sparse graph Laplacians.

Over the course of this survey we will explore a number of different ways that randomization can be used to design effective NLA algorithms. For the moment, let us just summarize the most important benefits.

Section 16 develops randomized algorithms for computing a factorization of a full-rank matrix, such as a pivoted QR decomposition or a URV decomposition.

NLA definitively treats several major classes of problems, including

solution of dense and sparse linear systems;

orthogonalization, least-squares, and Tikhonov regularization;

determination of eigenvalues, eigenvectors, and invariant subspaces;

singular value decomposition (SVD) and total least-squares.

In spite of this catalog of successes, important challenges remain. The sheer scale of certain datasets (terabytes and beyond) makes them impervious to classical NLA algorithms. Modern computing architectures (GPUs, multi-core CPUs, massively distributed systems) are powerful, but this power can only be unleashed by algorithms that minimize data movement and that are designed ab initio with parallel computation in mind....
