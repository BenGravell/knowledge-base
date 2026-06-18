Gradient Descent Provably Optimizes Over-parameterized Neural Networks

Topics include Gradient descent, Neural networks.

One of the mysteries in the success of neural networks is randomly initialized first order methods like gradient descent can achieve zero training loss even though the objective function is non-convex and non-smooth. This paper demystifies this surprising phenomenon for two-layer fully connected ReLU activated neural networks. For an m hidden node shallow neural network with ReLU activation and n training data, we show as long as m is large enough and no two inputs are parallel, randomly initialized gradient descent converges to a globally optimal solution at a linear convergence rate for the quadratic loss function. Our analysis relies on the following observation: over-parameterization and random initialization jointly restrict every weight vector to be close to its initialization for all iterations, which allows us to exploit a strong convexity-like property to show that gradient descent converges at a global linear rate to the global optimum. We believe these insights are also useful in analyzing deep models and other first order methods.

## Introduction

Neural networks trained by first order methods have achieved a remarkable impact on many applications, but their theoretical properties are still mysteries. One of the empirical observation is even though the optimization objective function is non-convex and non-smooth, randomly initialized first order methods like stochastic gradient descent can still find a global minimum. Surprisingly, this property is not correlated with labels. In Zhang et al., authors replaced the true labels with randomly generated labels, but still found randomly initialized first order methods can always achieve zero training loss.

A widely believed explanation on why a neural network can fit all training labels is that the neural network is over-parameterized. For example, Wide ResNet (Zagoruyko and Komodakis, ) uses 100x parameters than the number of training data. Thus there must exist one such neural network of this architecture that can fit all training data. However, the existence does not imply why the network found by a randomly initialized first order method can fit all the data. The objective function is neither smooth nor convex, which makes traditional analysis technique from convex optimization not useful in this setting.

In this paper we demystify this surprising phenomenon on two-layer neural networks with rectified linear unit (ReLU) activation. Formally, we consider a neural network of the following form.

Our main focus of this paper is to analyze the following procedure. We fix the second layer and apply gradient descent (GD) to optimize the first layer^11^1In Section 3.2, we also extend our technique to analyze the setting where we train both layers jointly.

## Conclusion and Discussion

In this paper we show with over-parameterization, gradient descent provable converges to the global minimum of the empirical loss at a linear convergence rate. The key proof idea is to show the over-parameterization makes Gram matrix remain positive definite for all iterations, which in turn guarantees the linear convergence. Here we list some future directions.

First, we believe our approach can be generalized to deep neural networks. We elaborate the main idea here for gradient flow. Consider a deep neural network of the form
