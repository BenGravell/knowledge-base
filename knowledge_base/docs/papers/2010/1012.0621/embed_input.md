The Convex Geometry of Linear Inverse Problems

Topics include Linear inverse problems, Atomic norms, Convex geometry, Low-dimensional models, Sparse recovery, Low-rank recovery.

Develops a convex-geometric framework for linear inverse problems in which model simplicity is encoded by atomic norms and tangent cones. The paper unifies sparse, low-rank, and other structured recovery results under one geometric recovery theory.

In applications throughout science and engineering one is often faced with the challenge of solving an ill-posed inverse problem, where the number of available measurements is smaller than the dimension of the model to be estimated. However in many practical situations of interest, models are constrained structurally so that they only have a few degrees of freedom relative to their ambient dimension. This paper provides a general framework to convert notions of simplicity into convex penalty functions, resulting in convex optimization solutions to linear, underdetermined inverse problems. The class of simple models considered are those formed as the sum of a few atoms from some (possibly infinite) elementary atomic set; examples include well-studied cases such as sparse vectors and low-rank matrices, as well as several others including sums of a few permutations matrices, low-rank tensors, orthogonal matrices, and atomic measures. The convex programming formulation is based on minimizing the norm induced by the convex hull of the atomic set; this norm is referred to as the atomic norm.

## Introduction

Deducing the state or structure of a system from partial, noisy measurements is a fundamental task throughout the sciences and engineering. A commonly encountered difficulty that arises in such inverse problems is the limited availability of data relative to the ambient dimension of the signal to be estimated. However many interesting signals or models in practice contain few degrees of freedom relative to their ambient dimension.

We describe a model as simple if it can be written as a nonnegative combination of a few elements from an atomic set.

where $\mathcal{A}$ is a set of atoms that constitute simple building blocks of general signals. Here we assume that $\mathbf{x}$ is *simple* so that $k$ is relatively small. For example $\mathcal{A}$ could be the finite set of unit-norm one-sparse vectors in which case $\mathbf{x}$ is a sparse vector, or $\mathcal{A}$ could be the infinite set of unit-norm rank-one matrices in which case $\mathbf{x}$ is a low-rank matrix.

In each of these examples as well as several others, a fundamental problem of interest is to recover $\mathbf{x}$ given limited *linear* measurements. For instance the question of recovering a sparse function over the group of permutations (i.e., the sum of a few permutation matrices) given linear measurements in the form of partial Fourier information was investigated in the context of ranked election problems. Similar linear inverse problems arise with atomic measures in system identification, with orthogonal matrices in machine learning, and with simple models formed from several other atomic sets (see Section 2.2 for more examples).

Motivated by the success of these methods we propose a general convex optimization framework in Section 2 in order to recover objects with structure of the form from limited linear measurements. The guiding question behind our framework is: how do we take a concept of simplicity such as sparsity and derive the $\ell_{1}$ norm as a convex heuristic? In other words what is the natural procedure to go from the set of one-sparse vectors $\mathcal{A}$ to the $\ell_{1}$ norm? We observe that the convex hull of (unit-Euclidean-norm) one-sparse vectors is the unit ball of the $\ell_{1}$ norm, or the cross-polytope.
