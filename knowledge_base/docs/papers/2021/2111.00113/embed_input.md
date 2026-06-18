Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems

This paper develops a new class of algorithms for general linear systems and eigenvalue problems. These algorithms apply fast randomized sketching to accelerate subspace projection methods, such as GMRES and Rayleigh-Ritz. This approach offers great flexibility in designing the basis for the approximation subspace, which can improve scalability in many computational environments. The resulting algorithms outperform the classic methods with minimal loss of accuracy. For model problems, numerical experiments show large advantages over MATLAB's optimized routines, including a 100 x speedup over gmres and a 10 x speedup over eigs.

## Introduction

Arguably, the most exciting recent development in numerical linear algebra (NLA) is the advent of new randomized algorithms that are fast, scalable, robust, and reliable. For example, many practitioners have adopted the "randomized SVD" and its relatives to compute truncated singular value decompositions of large matrices. Randomized preconditioning allows us to solve highly overdetermined least-squares problems faster than any previous algorithm.

In spite of these successes, our community has made less progress on other core challenges from NLA, especially problems involving nonsymmetric square matrices. This paper exposes a new class of algorithms for solving general linear systems and eigenvalue problems. Our framework combines subspace projection methods, such as GMRES and the Rayleigh--Ritz process, with the modern technique of randomized sketching. This approach allows us to accelerate the existing methods by incorporating approximation subspaces that are easier to construct. The resulting algorithms are faster than their classic counterparts, without much loss of accuracy.

## Sketching a least-squares problem

The sketch-and-solve paradigm is a basic tool for randomized matrix computations. The idea is to decrease the dimension of a large problem by projecting it onto a random subspace and to solve the smaller problem instead. The solution of this "sketched problem" sometimes serves in place of the solution to the original computational problem.

## Discussion

Our idea to combine subspace projection methods with sketching offers compelling advantages over the classic algorithms, especially in modern computing environments. Nevertheless, it must be acknowledged that this approach suffers from some of the same weaknesses as GMRES and RR. For example, when the basis $\mathbf{B}$ is a Krylov subspace, these methods are limited by the approximation power of Krylov subspaces. Furthermore, we are not aware of a universal method for quickly computing a full-rank basis for the Krylov subspace, short of expensive strategies based on full orthogonalization. Both of these points merit further attention.

With hindsight, our framework appears as an obvious application of the sketch-and-solve paradigm for overdetermined least-squares problems. A critical reader may even wonder whether this idea is actually novel. Let us respond to this concern.
