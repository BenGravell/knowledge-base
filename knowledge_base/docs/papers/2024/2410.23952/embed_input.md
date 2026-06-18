Scalable Kernel Inverse Optimization

Inverse Optimization (IO) is a framework for learning the unknown objective function of an expert decision-maker from a past dataset. In this paper, we extend the hypothesis class of IO objective functions to a reproducing kernel Hilbert space (RKHS), thereby enhancing feature representation to an infinite-dimensional space. We demonstrate that a variant of the representer theorem holds for a specific training loss, allowing the reformulation of the problem as a finite-dimensional convex optimization program. To address scalability issues commonly associated with kernel methods, we propose the Sequential Selection Optimization (SSO) algorithm to efficiently train the proposed Kernel Inverse Optimization (KIO) model. Finally, we validate the generalization capabilities of the proposed KIO model and the effectiveness of the SSO algorithm through learning-from-demonstration tasks on the MuJoCo benchmark.

## Introduction

Inverse Optimization (IO) is distinct from traditional optimization problems, where we typically seek the optimal decision variables by optimizing an objective function over a set of constraints. In contrast, inverse optimization works "in reverse" by inferring the optimization objective given the optimal solution. The inherent assumption in IO is that an agent generates its decision by solving an optimization problem. The assumed optimization problem is called the Forward Optimization Problem (FOP), which is parametric in the exogenous signal $\hat{s}$ with the corresponding optimal solution $\hat{u}$.

Contributions.

Kernelized IO Formulation: We propose a novel Kernel Inverse Optimization (KIO) model based on suboptimality loss. The proposed approach leverages kernel methods to enable IO models to operate on infinite-dimensional feature spaces, which allows KIO to outperform existing imitation learning (IL) algorithms on complex continuous control tasks in low-data regimes.

Sequential Selection Optimization Algorithm: To address the quadratic computational complexity of the proposed KIO model, we introduce the Sequential Selection Optimization (SSO) algorithm inspired by coordinate descent style updates. This algorithm selectively optimizes components of the decision variable, greatly enhancing efficiency and scalability while provably converging to the same solution of our proposed KIO model.

## Conclusion and Limitations

We introduced Kernel Inverse Optimization (KIO), an inverse optimization model leveraging kernel methods, along with its simplified variant and the theoretical derivations. Subsequently, we proposed the Sequential Selection Optimization (SSO) algorithm for training the KIO model, which addresses memory issues by decomposing the original problem into a series of subproblems. Our empirical results demonstrate that KIO exhibits strong learning capabilities in complex control tasks, while the SSO algorithm achieves rapid convergence to the optimal solution within a limited number of iterations.
