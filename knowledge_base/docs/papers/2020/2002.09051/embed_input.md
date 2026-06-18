An Elementary Approach to Convergence Guarantees of Optimization Algorithms for Deep Networks

We present an approach to obtain convergence guarantees of optimization algorithms for deep networks based on elementary arguments and computations. The convergence analysis revolves around the analytical and computational structures of optimization oracles central to the implementation of deep networks in machine learning software. We provide a systematic way to compute estimates of the smoothness constants that govern the convergence behavior of first-order optimization algorithms used to train deep networks. A diverse set of example components and architectures arising in modern deep networks intersperse the exposition to illustrate the approach.

## Introduction

Deep networks have achieved remarkable performance in several application domains such as computer vision, natural language processing and genomics. The input-output mapping implemented by a deep neural network is a chain of compositions of modules, where each module is typically a composition of a non-linear mapping, called an activation function, and an affine mapping. The last module in the chain is usually task-specific in that it relates to a performance accuracy for a specific task....

The optimization problem arising when training a deep network is often framed as a non-convex optimization problem, dismissing the structure of the objective yet central to the software implementation. Indeed optimization algorithms used to train deep networks proceed by making calls to first-order (or second-order) oracles relying on dynamic programming such as gradient back-propagation. Gradient back-propagation is now part of modern machine learning software....

We can also compare the smoothness properties of the smoothed network with the same network modified by adding the batch-normalization layer for $m$ inputs and $\epsilon$ normalization parameter at each convolutional layer. As shown in Appendix D, the batch-normalization satisfies

Intuitively, the batch-norm bounds the output of each layer, mitigating the increase of $m_{t}$ in the computations of the estimates of the smoothness in lines 8 and 9 of Algo. 4. Yet, for a small $\epsilon$, this effect is balanced by the non-smoothness of the batch-norm layer (which for $\epsilon\rightarrow 0$ tends to have an infinite slope around 0).

As explained in last subsection and shown in Appendix B, a gradient step can naturally be derived as a dynamic programming procedure applied to the subproblem. However, the implementation of the gradient step provides itself a different kind of oracle on the chain of computations as defined below.

We consider implicit functions that take the form

the Gauss-Newton oracle amounts to solving

In Sec. 2, we define the parameterized input-output map implemented by a deep network as a chain-composition of modules and write the corresponding optimization objective consisting in learning the parameters of this map. In Sec....
