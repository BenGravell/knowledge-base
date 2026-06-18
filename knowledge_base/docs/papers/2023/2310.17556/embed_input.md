Efficient Numerical Algorithm for Large-Scale Damped Natural Gradient Descent

Topics include Gradient descent, Natural gradients, Benchmarks, Cholesky decomposition.

We propose a new algorithm for efficiently solving the damped Fisher matrix in large-scale scenarios where the number of parameters significantly exceeds the number of available samples. This problem is fundamental for natural gradient descent and stochastic reconfiguration. Our algorithm is based on Cholesky decomposition and is generally applicable. Benchmark results show that the algorithm is significantly faster than existing methods.

## Introduction

Natural gradient descent is a fundamental optimization technique widely employed in the field of machine learning. Its quantum counterpart, known as stochastic reconfiguration, holds paramount importance in variational quantum Monte Carlo methods. However, when applied to large-scale problems, such as training neural networks, a significant bottleneck emerges due to the computational burden of inverting the Fisher information matrix. Although approximations like KFAC \[\] have been introduced to mitigate this burden, they often fall short of replicating the performance of the exact method.

In large-scale scenarios, where the number of samples is typically much smaller than the number of model parameters, a damping term becomes essential. In this paper, we propose a fast algorithm for inverting the damped Fisher information matrix, based on Cholesky decomposition. This algorithm is designed for GPU implementation and can be easily parallelized, promising to significantly improve the scalability and performance of natural gradient descent and stochastic reconfiguration.

It's worth noting that there are existing papers addressing large-scale SR, particularly for neural network wavefunctions, such as \[\] and \[RVB^+^23\]. These methods rely on the least-square structure of the SR procedure, meaning that the gradient $v$ is a linear combination of the rows of $S$, i.e., $v = {S^{\mathsf{T}}f}$. This requirement limits the choice of the loss function and prevents the use of regularization. In contrast, our algorithm does not have this limitation and can be applied to any loss function, including those used in Wasserstein quantum Monte Carlo \[NNT^+^23\]....

Iterative methods, such as conjugate gradient descent, can efficiently solve Equation 1. These methods typically scale linearly with both $n$ and $m$, but the number of iterations increase significantly when the matrix is ill-conditioned. This leads to slow convergence and higher computational costs. Our algorithm, on the other hand, is non-iterative and generally avoids such issues.

We implemented the algorithm in JAX and conducted tests on a single NVIDIA A100 GPU with 80 GB of memory. We evaluated the algorithm's performance on problems with $m \sim 10^{6}$ parameters and $n \sim 10^{3}$ samples, which is beyond the capability of the naive inversion method....
