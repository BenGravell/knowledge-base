Global Convergence of Adaptive Gradient Methods for an Over-parameterized Neural Network

Adaptive gradient methods like AdaGrad are widely used in optimizing neural networks. Yet, existing convergence guarantees for adaptive gradient methods require either convexity or smoothness, and, in the smooth setting, only guarantee convergence to a stationary point. We propose an adaptive gradient method and show that for two-layer over-parameterized neural networks - if the width is sufficiently large (polynomially) - then the proposed method converges to the global minimum in polynomial time, and convergence is robust, without the need to fine-tune hyper-parameters such as the step-size schedule and with the level of over-parametrization independent of the training error. Our analysis indicates in particular that over-parametrization is crucial for the harnessing the full potential of adaptive gradient methods in the setting of neural networks.

## Introduction

Gradient-based methods are widely used in optimizing neural networks. One crucial component in gradient methods is the learning rate (a.k.a. step size) hyper-parameter, which determines the convergence speed of the optimization procedure. A large learning rate can speed up the convergence but if it is larger than a threshold, the optimization algorithm cannot converge. This is by now well-understood for convex problems; excellent works on this topic include Nash and Nocedal, Bertsekas, Nesterov, Haykin et al., Bubeck et al., and the recent review for large-scale stochastic optimization to Bottou et al.....

Recently, a series of breakthrough papers showed that (stochastic) gradient descent can provably converge to the global minima for over-parameterized neural networks. However, these papers all require the step size to be sufficiently small to guarantee the global convergence. In practice, these optimization algorithms can use a much larger learning rate while still converging to the global minimum. This leads to the following question:

### Proposition 5.2

On the other hand, the update rule in can resolve the problem because the growth of $b_{k}$ is larger than such that the upper bound of ${\|{{\mathbf{w}_{r}{(k)}} - {\mathbf{w}_{r}{}}}\|}_{2}$ $k = {0,{1\ldots},{T_{0} - 1}}$, is better than that in Proposition 5.2 and even Lemma 4.2 if $c{<{b_{0}{<{\etaC}\parallel}\mathbf{H}^{\infty}}\parallel}$ for some small $c$....

## An Adaptive Method for Over-parameterized Neural Networks

We use $\mathbf{W}{(k)}$ to denote the parameters at the $k$-th iteration.

### Condition 4.1

*What is the optimal learning rate in optimizing neural networks?*

While finding the optimal step size is important theoretically for identifying the optimal convergence rate, the optimal learning rate often depends on certain unknown parameters of the problem. For example, for a convex and $L$-smooth objective function, the optimal learning rate is $O{({1/L})}$ where $L$ is often unknown to practitioners. To solve this problem, adaptive methods are proposed so that they can change the learning rate on-the-fly according to gradient information received along the way....

On the other hand, the theoretical investigation in adaptive methods in optimizing neural networks is limited....
