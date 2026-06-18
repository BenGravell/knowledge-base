Efficient Numerical Algorithm for Large-Scale Damped Natural Gradient Descent

Topics include Gradient descent, Natural gradients, Benchmarks, Cholesky decomposition.

We propose a new algorithm for efficiently solving the damped Fisher matrix in large-scale scenarios where the number of parameters significantly exceeds the number of available samples. This problem is fundamental for natural gradient descent and stochastic reconfiguration. Our algorithm is based on Cholesky decomposition and is generally applicable. Benchmark results show that the algorithm is significantly faster than existing methods.

## Introduction

Natural gradient descent is a fundamental optimization technique widely employed in the field of machine learning. Its quantum counterpart, known as stochastic reconfiguration, holds paramount importance in variational quantum Monte Carlo methods. However, when applied to large-scale problems, such as training neural networks, a significant bottleneck emerges due to the computational burden of inverting the Fisher information matrix. Although approximations like KFAC have been introduced to mitigate this burden, they often fall short of replicating the performance of the exact method.

In large-scale scenarios, where the number of samples is typically much smaller than the number of model parameters, a damping term becomes essential. In this paper, we propose a fast algorithm for inverting the damped Fisher information matrix, based on Cholesky decomposition. This algorithm is designed for GPU implementation and can be easily parallelized, promising to significantly improve the scalability and performance of natural gradient descent and stochastic reconfiguration.

## Results

Our

In this equation $S$ is a $n \times m$ matrix, while $x$ and $v$ are both $m$-dimensional vectors. The parameter $\lambda$ determines the damping strength and $I$ represents the $m \times m$ identity matrix. In the context of natural gradient descent, $S$ is the (scaled) score matrix, defined as $S_{ij} = {\frac{1}{\sqrt{n}}\frac{\partial{{\log P_{\theta}}\left( x_{i} \right)}}{\partial\theta_{j}}}$, where $P_{\theta}\left( x_{i} \right)$ is the model's predicted probability of sample $x_{i}$ and $\theta_{j}$ is the $j$-th parameter of the model. $S^{\mathsf{T}}S$ yields the estimated Fisher information matrix.
