Randomized Numerical Linear Algebra: Foundations & Algorithms

This survey describes probabilistic algorithms for linear algebra computations, such as factorizing matrices and solving linear systems. It focuses on techniques that have a proven track record for real-world problem instances. The paper treats both the theoretical foundations of the subject and the practical computational issues. Topics covered include norm estimation; matrix approximation by sampling; structured and unstructured random embeddings; linear regression problems; low-rank approximation; subspace iteration and Krylov methods; error estimation and adaptivity; interpolatory and CUR factorizations; Nyström approximation of positive-semidefinite matrices; single view ("streaming") algorithms; full rank-revealing factorizations; solvers for linear systems; and approximation of kernel matrices that arise in machine learning and in scientific computing.

## Introduction

Numerical linear algebra (NLA) is one of the great achievements of scientific computing. On most computational platforms, we can now routinely and automatically solve small- and medium-scale linear algebra problems to high precision. The purpose of this survey is to describe a set of probabilistic techniques that have joined the mainstream of NLA over the last decade. These new techniques have accelerated everyday computations for small- and medium-size problems, and they have enabled large-scale computations that were beyond the reach of classical methods.

## Classical numerical linear algebra

NLA definitively treats several major classes of problems, including

solution of dense and sparse linear systems;

orthogonalization, least-squares, and Tikhonov regularization;
