An Elementary Approach to Convergence Guarantees of Optimization Algorithms for Deep Networks

We present an approach to obtain convergence guarantees of optimization algorithms for deep networks based on elementary arguments and computations. The convergence analysis revolves around the analytical and computational structures of optimization oracles central to the implementation of deep networks in machine learning software. We provide a systematic way to compute estimates of the smoothness constants that govern the convergence behavior of first-order optimization algorithms used to train deep networks. A diverse set of example components and architectures arising in modern deep networks intersperse the exposition to illustrate the approach.

## Introduction

Deep networks have achieved remarkable performance in several application domains such as computer vision, natural language processing and genomics. The input-output mapping implemented by a deep neural network is a chain of compositions of modules, where each module is typically a composition of a non-linear mapping, called an activation function, and an affine mapping. The last module in the chain is usually task-specific in that it relates to a performance accuracy for a specific task.

The optimization problem arising when training a deep network is often framed as a non-convex optimization problem, dismissing the structure of the objective yet central to the software implementation. Indeed optimization algorithms used to train deep networks proceed by making calls to first-order (or second-order) oracles relying on dynamic programming such as gradient back-propagation. Gradient back-propagation is now part of modern machine learning software.

In Sec. 2, we define the parameterized input-output map implemented by a deep network as a chain-composition of modules and write the corresponding optimization objective consisting in learning the parameters of this map. In Sec. 3, we detail the implementation of first-order and second-order oracles by dynamic programming; the classical gradient back-propagation algorithm is recovered as a canonical example. Gauss-Newton steps can also be simply stated in terms of calls to an automatic-differentiation oracle implemented in modern machine learning software libraries.

## Deep network architecture

A feed-forward deep network of depth $\tau$ can be described as a transformation of an input $x$ into an output $x_{\tau}$ through the composition of $\tau$ blocks, called layers, illustrated in Fig. 1. Each layer is defined by a set of parameters. In general, (see Sec. 2.3 for a detailed decomposition), these parameters act on the input of the layer through an affine operation followed by a non-linear operation. Formally, the $t$^th^ layer can be described as a function of its parameters $u_{t}$ and a given input $x_{t - 1}$ that outputs $x_{t}$ as
