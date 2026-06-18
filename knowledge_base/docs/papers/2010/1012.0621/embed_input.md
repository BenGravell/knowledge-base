The Convex Geometry of Linear Inverse Problems

Topics include Linear inverse problems, Atomic norms, Convex geometry, Low-dimensional models, Sparse recovery, Low-rank recovery.

Develops a convex-geometric framework for linear inverse problems in which model simplicity is encoded by atomic norms and tangent cones. The paper unifies sparse, low-rank, and other structured recovery results under one geometric recovery theory.

In applications throughout science and engineering one is often faced with the challenge of solving an ill-posed inverse problem, where the number of available measurements is smaller than the dimension of the model to be estimated. However in many practical situations of interest, models are constrained structurally so that they only have a few degrees of freedom relative to their ambient dimension. This paper provides a general framework to convert notions of simplicity into convex penalty functions, resulting in convex optimization solutions to linear, underdetermined inverse problems. The class of simple models considered are those formed as the sum of a few atoms from some (possibly infinite) elementary atomic set; examples include well-studied cases such as sparse vectors and low-rank matrices, as well as several others including sums of a few permutations matrices, low-rank tensors, orthogonal matrices, and atomic measures. The convex programming formulation is based on minimizing the norm induced by the convex hull of the atomic set; this norm is referred to as the atomic norm....

## Introduction

Deducing the state or structure of a system from partial, noisy measurements is a fundamental task throughout the sciences and engineering. A commonly encountered difficulty that arises in such inverse problems is the limited availability of data relative to the ambient dimension of the signal to be estimated. However many interesting signals or models in practice contain few degrees of freedom relative to their ambient dimension....

We describe a model as simple if it can be written as a nonnegative combination of a few elements from an atomic set. Concretely let $\mathbf{x} \in {\mathbb{R}}^{p}$ be formed as follows:

### Large-scale algorithms

Finally, we think that the most fruitful extensions of this work lie in a thorough exploration of the empirical performance and efficacy of atomic norms on large-scale inverse problems. The proposed algorithms in Section 5 require only the knowledge of the proximity operator of an atomic norm, or a Euclidean projection operator onto the dual norm ball. Using these design principles and the geometry of particular atomic norms should enable the scaling of atomic norm techniques to massive data sets.

### Proposition 3.10

Gordon's theorem thus provides a simple characterization of the number of measurements required for reconstruction with the atomic norm. Indeed the Gaussian width of $\Omega = {{T_{\mathcal{A}}{(\mathbf{x}^{\star})}} \cap {\mathbb{S}}^{p - 1}}$ is the only quantity that we need to compute in order to obtain bounds for both exact and robust recovery. Unfortunately it is in general not easy to compute Gaussian widths....

Consequently outer approximations of the atomic set give rise to approximate norms that provide lower bounds on the optimal value of the problem.

where $\mathcal{A}$ is a set of atoms that constitute simple building blocks of general signals. Here we assume that $\mathbf{x}$ is *simple* so that $k$ is relatively small. For example $\mathcal{A}$ could be the finite set of unit-norm one-sparse vectors in which case $\mathbf{x}$ is a sparse vector, or $\mathcal{A}$ could be the infinite set of unit-norm rank-one matrices in which case $\mathbf{x}$ is a low-rank matrix....

In each of these examples as well as several others, a fundamental problem of interest is to recover $\mathbf{x}$ given limited *linear* measurements....
