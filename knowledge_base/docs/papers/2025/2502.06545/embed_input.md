Universal Sequence Preconditioning

Topics include Regret bounds, Neural networks, Recurrent neural networks, Universal sequence preconditioning.

We study the problem of preconditioning in sequential prediction. From the theoretical lens of linear dynamical systems, we show that convolving the target sequence corresponds to applying a polynomial to the hidden transition matrix. Building on this insight, we propose a universal preconditioning method that convolves the target with coefficients from orthogonal polynomials such as Chebyshev or Legendre. We prove that this approach reduces regret for two distinct prediction algorithms and yields the first ever sublinear and hidden-dimension-independent regret bounds (up to logarithmic factors) that hold for systems with marginally table and asymmetric transition matrices. Finally, extensive synthetic and real-world experiments show that this simple preconditioning strategy improves the performance of a diverse range of algorithms, including recurrent neural networks, and generalizes to signals beyond linear dynamical systems.

## Introduction

In sequence prediction the goal of the learner is to predict the next token accurately according to a specified loss function, such as the mean square error or cross-entropy. This fundamental problem in machine learning has gained increased importance with the rise of large language models, which perform sequence prediction on tokens using cross entropy. The focus of this paper is preconditioning, i.e. modifying the target sequence to make it easier to learn.

It is widely acknowledged that learning this sequence can be "easier\" than learning the original sequence for a large number of modalities. In this work we seek a more general framework for sequence preconditioning that captures the same intuition behind differencing and extends it to a broader class of transformations. The question we ask is

What is the general form of sequence preconditioning that enables provably accurate learning?

From an information-theoretic perspective, approaches of this kind seem futile---predicting $\mathbf{y}_{t}$ or $\sum_{i}{c_{i}\mathbf{y}_{t - i}}$ seems equally hard in an adversarial setting. Yet we show that when the data arises from a linear dynamical system (LDS), there exists a *universal* form of preconditioning that provably improves learnability, independent of the specific system. In the LDS setting, we show that preconditioning significantly strengthens existing prediction methods, leading to new regret bounds.

## Discussion

There are many settings in machine learning where universal, rather than learned, rules have proven very efficient. For example, physical laws of motion can be learned directly from observation data. However, Newton's laws of motion succinctly crystallize very general phenomenon, and have proven very useful for large scale physics simulation engines. Similarly, in the theory of mathematical optimization, adaptive gradient methods have revolutionized deep learning.

By analogy, our thesis in this paper is that universal preconditioning based on the solid theory of dynamical systems can be applicable to many domains or, at the very least, an initialization for other learning methods.
