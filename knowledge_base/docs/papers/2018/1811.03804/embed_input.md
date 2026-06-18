Gradient Descent Finds Global Minima of Deep Neural Networks

Gradient descent finds a global minimum in training deep neural networks despite the objective function being non-convex. The current paper proves gradient descent achieves zero training loss in polynomial time for a deep over-parameterized neural network with residual connections (ResNet). Our analysis relies on the particular structure of the Gram matrix induced by the neural network architecture. This structure allows us to show the Gram matrix is stable throughout the training process and this stability implies the global optimality of the gradient descent algorithm. We further extend our analysis to deep residual convolutional neural networks and obtain a similar convergence result.

## Introduction

One of the mysteries in deep learning is randomly initialized first-order methods like gradient descent achieve zero training loss, even if the labels are arbitrary. Over-parameterization is widely believed to be the main reason for this phenomenon as only if the neural network has a sufficiently large capacity, it is possible for this neural network to fit all the training data. For example, Lu et al. proved that except for a measure zero set, all functions cannot be approximated by ReLU networks with a width less than the input dimension. In practice, many neural network architectures are highly over-parameterized....

The second mysterious phenomenon in training deep neural networks is "deeper networks are harder to train." To solve this problem, He et al. proposed the deep residual network (ResNet) architecture which enables randomly initialized first order method to train neural networks with an order of magnitude more layers. Theoretically, Hardt & Ma showed that residual links in linear networks prevent gradient vanishing in a large neighborhood of zero, but for neural networks with non-linear activations, the advantages of using residual connections are not well understood.

The current analysis is for gradient descent, instead of stochastic gradient descent. We believe the analysis can be extended to stochastic gradient, while maintaining the linear convergence rate.

The convergence rate can be potentially improved if the minimum eigenvalue takes into account the contribution of all Gram matrices, but this would considerably complicate the initialization and perturbation analysis.

We leverage this insight to our deep neural network setting. Again we consider the sequence ${\{{\mathbf{y} - {\mathbf{u}{(k)}}}\}}_{k = 0}^{\infty}$, which admits the dynamics

This assumption is used to guarantee the positive-definiteness of certain Gram matrices which we will define later. Softplus function satisfies this assumption by definition.

The Gram matrix $\mathbf{K}^{(H)}$ is recursively defined as follows, for ${(i,j)} \in {{\lbrack n\rbrack} \times {\lbrack n\rbrack}}$, and $h = {1,\ldots,{H - 1}}$

In this paper, we demystify these two mysterious phenomena. We consider the setting where there are $n$ data points, and the neural network has $H$ layers with width $m$....
