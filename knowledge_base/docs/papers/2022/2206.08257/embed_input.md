Gradient Descent for Low-Rank Functions

Several recent empirical studies demonstrate that important machine learning tasks, e.g., training deep neural networks, exhibit low-rank structure, where the loss function varies significantly in only a few directions of the input space. In this paper, we leverage such low-rank structure to reduce the high computational cost of canonical gradient-based methods such as gradient descent (GD). Our proposed Low-Rank Gradient Descent (LRGD) algorithm finds an epsilon-approximate stationary point of a p-dimensional function by first identifying r <= p significant directions, and then estimating the true p-dimensional gradient at every iteration by computing directional derivatives only along those r directions. We establish that the "directional oracle complexities" of LRGD for strongly convex and non-convex objective functions are O(r log(1/epsilon) + rp) and O(r/epsilon^ + rp), respectively. When r ll p, these complexities are smaller than the known complexities of O(p log(1/epsilon)) and O(p/epsilon^) of {\gd} in the strongly convex and non-convex settings, respectively....

## Introduction

First order optimization methods such as Gradient Descent (GD) and its variants have become the cornerstone of training modern machine learning models. Hence, reducing the running times of first order methods has been an important problem in the optimization literature, cf.. The running times of GD methods is known to grow linearly with the dimension of the model parameters, which can be very large, e.g., in deep neural networks. However, it has recently been observed that many empirical risk minimization problems have objective functions (i.e., real-valued losses) with *low-rank structure* in their gradients....

Roughly speaking, a low-rank function is a differentiable real-valued function whose gradients live *close* to a low-dimensional subspace. Such low-rank structure has been exploited to theoretically improve the running times of federated optimization algorithms in. Yet, canonical GD methods do not exploit this additional structure. Hence, the goal of this work is to address the following question:

Conclusion. This work proposes an optimization approach that leverages low-rank structure to reduce the number of directional derivative queries. We believe that other optimization methods could benefit from incorporating such an approach.

## Appendices

which together with 2) in Proposition 2.1. ‣ 2.2 Exactly low-rank functions ‣ 2 Formal setup and low-rank structure ‣ Gradient Descent for Low-Rank Functions") yields that $H$ is of full dimension $r = p$. On the other hand, we expand on some properties of low-rank functions in Appendix C.1. Furthermore, we illustrate via an example in Appendix C.2 that optimization of a high-rank function can sometimes be equivalently represented as optimization of a low-rank function using an appropriately chosen non-linear transformation.

where $\epsilon > 0$ is the predefined accuracy. Note that it suffices to find an $\epsilon^{\prime}$-stationary point of $f$ with $\epsilon^{\prime} = \sqrt{2\mu\epsilon}$ to get an $\epsilon$-minimizer of $f$, which explains the relation between both settings.

The proposed algorithm, LRGD, is an iterative gradient-based method. It starts by identifying a subspace $H$ of rank $r \leq p$ that is a good candidate to match our definition of approximately low-rank function for the objective $f$, i.e., Definition 2.3....
