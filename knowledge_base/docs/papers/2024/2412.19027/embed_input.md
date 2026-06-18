CuClarabel: GPU Acceleration for a Conic Optimization Solver

Topics include Convex optimization, Semidefinite programming, Accuracy, Parallel computing, Optimization, CuClarabel.

We present the GPU implementation of the general-purpose interior-point solver Clarabel for convex optimization problems with conic constraints. We introduce a mixed parallel computing strategy that processes linear constraints first, then handles other conic constraints in parallel. The GPU solver currently supports linear equality and inequality constraints, second-order cones, exponential cones, power cones and positive semidefinite cones of the same dimensionality. We demonstrate that integrating a mixed parallel computing strategy with GPU-based direct linear system solvers enhances the performance of GPU-based conic solvers, surpassing their CPU-based counterparts across a wide range of conic optimization problems. We also show that employing mixed-precision linear system solvers can potentially achieve additional acceleration without compromising solution accuracy.

## Introduction

We

with respect to $x,s$ and with parameters $A \in \text{R}^{m \times n}$, $b \in \text{R}^{m}$, $q \in \text{R}^{n}$ and $P \in {SS}_{+}^{n}$ and variables ${x \in \text{R}^{n}},{s \in \text{R}^{m}}$. For the rest of the paper, ${SS}_{+}^{n}$ represents the cone of positive semi-definite matrices. The cone $\mathcal{K}$ is a closed convex cone. The formulation ($\mathcal{P}$) is very general and can model most conic convex optimization problems in practice.

with respect to $x,z$ and where $\mathcal{K}^{\ast}$ is the dual cone of $\mathcal{K}$. Solving $\mathcal{P}$ and $\mathcal{D}$ is equivalent to solving the Karush-Kuhn-Tucker (KKT) conditions when strong duality holds. On the other hand, the set of strongly primal infeasibility certificates for ($\mathcal{P}$) is

and the set of strongly dual infeasibility certificates is

## Conclusion

We have developed a GPU interior point solver for conic optimization.^33^3 In our implementation, we propose a mixed parallel computing strategy to process linear constraints with second-order cone, exponential cone, power cone and semidefinite cone constraints. Our GPU solver shows several times acceleration compared to state-of-the-art CPU conic solvers on many problems to high precision, such as QPs, SOCPs, exponential cone programs and SDPs.

Future research directions include extending support to general SDPs with PSD cones of varying dimensionalities. The proposed mixed parallel computing strategy for GPU implementation is also applicable to conic solvers based on first-order operator-splitting methods. This approach could improve GPU utilization, especially when sufficient computational resources are available to handle different cone classes in parallel. Additional performance gains may be achieved through kernel fusion, the use of CUDA graphs to reduce kernel launch overhead and overlapping more independent computation within interior-point methods.
