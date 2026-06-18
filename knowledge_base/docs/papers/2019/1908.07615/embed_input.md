Iterative Linearized Control: Stable Algorithms and Complexity Guarantees

We examine popular gradient-based algorithms for nonlinear control in the light of the modern complexity analysis of first-order optimization algorithms. The examination reveals that the complexity bounds can be clearly stated in terms of calls to a computational oracle related to dynamic programming and implementable by gradient back-propagation using machine learning software libraries such as PyTorch or TensorFlow. Finally, we propose a regularized Gauss-Newton algorithm enjoying worst-case complexity bounds and improved convergence behavior in practice. The software library based on PyTorch is publicly available.

## Introduction

Finite horizon discrete time nonlinear control has been studied for decades, with applications ranging from spacecraft dynamics to robot learning. Popular nonlinear control algorithms, such as differential dynamic programming or iterative linear quadratic Gaussian algorithms, are commonly derived using a linearization argument relating the nonlinear control problem to a linear control problem.

We examine nonlinear control algorithms based on iterative linearization techniques through the lens of the modern complexity analysis of first-order optimization algorithms. We first reformulate the problem as the minimization of an objective that is written as a composition of functions. Owing to this reformulation, we can frame several popular nonlinear control algorithms as first-order optimization algorithms applied to this objective.

We highlight the equivalence of dynamic programming and gradient back-propagation in this framework and underline the central role of the corresponding automatic differentiation oracle in the complexity analysis in terms of convergence to a stationary point of the objective. We show that the number of calls to this automatic differentiation oracle is the relevant complexity measure given the outreach of machine learning software libraries such as PyTorch or TensorFlow.

Along the way we propose several improvements to the iterative linear quadratic regulator (ILQR) algorithm, resulting in an accelerated regularized Gauss-Newton algorithm enjoying a complexity bound in terms of convergence to a stationary point and displaying stable convergence behavior in practice. Regularized Gauss-Newton algorithms give a template for the design of algorithms based on partial linearization with guaranteed convergence.
