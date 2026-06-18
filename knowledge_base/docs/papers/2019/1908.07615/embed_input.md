Iterative Linearized Control: Stable Algorithms and Complexity Guarantees

We examine popular gradient-based algorithms for nonlinear control in the light of the modern complexity analysis of first-order optimization algorithms. The examination reveals that the complexity bounds can be clearly stated in terms of calls to a computational oracle related to dynamic programming and implementable by gradient back-propagation using machine learning software libraries such as PyTorch or TensorFlow. Finally, we propose a regularized Gauss-Newton algorithm enjoying worst-case complexity bounds and improved convergence behavior in practice. The software library based on PyTorch is publicly available.

## Introduction

Finite horizon discrete time nonlinear control has been studied for decades, with applications ranging from spacecraft dynamics to robot learning. Popular nonlinear control algorithms, such as differential dynamic programming or iterative linear quadratic Gaussian algorithms, are commonly derived using a linearization argument relating the nonlinear control problem to a linear control problem.

We examine nonlinear control algorithms based on iterative linearization techniques through the lens of the modern complexity analysis of first-order optimization algorithms. We first reformulate the problem as the minimization of an objective that is written as a composition of functions. Owing to this reformulation, we can frame several popular nonlinear control algorithms as first-order optimization algorithms applied to this objective.

The plots show stable convergence of the regularized ILQR on these problems. The proposed accelerated regularized Gauss-Newton algorithm displays stable and fast convergence. Applications of accelerated regularized Gauss-Newton algorithms to reinforcement learning problems would be interesting to explore.

Figure 2: Convergence of ILQR, regularized ILQR and accelerated regularized ILQR on the inverted pendulum (top) and two-link arm (bottom) control problems for an horizon τ = 100.

As presented in Section 2, the gradient back-propagation is divided in two main phases: (i) the forward pass that computes and store the gradients of the dynamics along the trajectory given by a command, (ii) the backward and roll-out passes that compute the gradient of the objective given the gradients of the costs and penalties along the trajectory....

### Proposition 2.3

### ILQR, ILQG

We highlight the equivalence of dynamic programming and gradient back-propagation in this framework and underline the central role of the corresponding automatic differentiation oracle in the complexity analysis in terms of convergence to a stationary point of the objective. We show that the number of calls to this automatic differentiation oracle is the relevant complexity measure given the outreach of machine learning software libraries such as PyTorch or TensorFlow.

Along the way we propose several improvements to the iterative linear quadratic regulator (ILQR) algorithm, resulting in an accelerated regularized Gauss-Newton algorithm...
