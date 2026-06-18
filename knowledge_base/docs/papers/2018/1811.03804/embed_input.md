Gradient Descent Finds Global Minima of Deep Neural Networks

Gradient descent finds a global minimum in training deep neural networks despite the objective function being non-convex. The current paper proves gradient descent achieves zero training loss in polynomial time for a deep over-parameterized neural network with residual connections (ResNet). Our analysis relies on the particular structure of the Gram matrix induced by the neural network architecture. This structure allows us to show the Gram matrix is stable throughout the training process and this stability implies the global optimality of the gradient descent algorithm. We further extend our analysis to deep residual convolutional neural networks and obtain a similar convergence result.

## Introduction

One of the mysteries in deep learning is randomly initialized first-order methods like gradient descent achieve zero training loss, even if the labels are arbitrary. Over-parameterization is widely believed to be the main reason for this phenomenon as only if the neural network has a sufficiently large capacity, it is possible for this neural network to fit all the training data. For example, Lu et al. proved that except for a measure zero set, all functions cannot be approximated by ReLU networks with a width less than the input dimension. In practice, many neural network architectures are highly over-parameterized.

The second mysterious phenomenon in training deep neural networks is "deeper networks are harder to train." To solve this problem, He et al. proposed the deep residual network (ResNet) architecture which enables randomly initialized first order method to train neural networks with an order of magnitude more layers. Theoretically, Hardt & Ma showed that residual links in linear networks prevent gradient vanishing in a large neighborhood of zero, but for neural networks with non-linear activations, the advantages of using residual connections are not well understood.

In this paper, we demystify these two mysterious phenomena. We consider the setting where there are $n$ data points, and the neural network has $H$ layers with width $m$. We focus on the least-squares loss and assume the activation function is Lipschitz and smooth. This assumption holds for many activation functions including the soft-plus and sigmoid. Our contributions are summarized below.

As a warm-up, we first consider a fully-connected feedforward network. We show if $m = {\Omega\left( {{poly}{(n)}2^{O{(H)}}} \right)}$^11^1The precise polynomials and data-dependent parameters are stated in Section 5, 6, 7., then randomly initialized gradient descent converges to zero training loss at a linear rate.

## Conclusion

In this paper, we show that gradient descent on deep overparametrized networks can obtain zero training loss. Our proof builds on a careful analysis of the random initialization scheme and a perturbation analysis which shows that the Gram matrix is increasingly stable under overparametrization. These techniques allow us to show that every step of gradient descent decreases the loss at a geometric rate.

We
