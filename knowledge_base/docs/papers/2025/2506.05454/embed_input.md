Zeroth-Order Optimization Finds Flat Minima

Topics include Reinforcement learning, Language models, Classification, Optimization, Learning, TRACE.

Zeroth-order methods are extensively used in machine learning applications where gradients are infeasible or expensive to compute, such as black-box attacks, reinforcement learning, and language model fine-tuning. Existing optimization theory focuses on convergence to an arbitrary stationary point, but less is known on the implicit regularization that provides a fine-grained characterization on which particular solutions are finally reached. We show that zeroth-order optimization with the standard two-point estimator favors solutions with small trace of Hessian, which is widely used in previous work to distinguish between sharp and flat minima. We further provide convergence rates of zeroth-order optimization to approximate flat minima for convex and sufficiently smooth functions, where flat minima are defined as the minimizers that achieve the smallest trace of Hessian among all optimal solutions. Experiments on binary classification tasks with convex losses and language model fine-tuning support our theoretical findings.

## Introduction

There are many emerging machine learning problems where gradients are not accessible or expensive to compute, hindering the application of gradient-based optimization algorithms. For example, fine-tuning large language models (LLMs), particularly at the scale of billions of parameters, faces significant memory bottlenecks, primarily because of the memory-intensive nature of backpropagation. Zeroth-order optimization offers a compelling alternative as it permits gradient estimation via finite differences of loss values. Malladi et al....

To be more specific, for the optimization problem ${\min_{x \in {\mathbb{R}}^{d}}f}{(x)}$ with parameters $x \in {\mathbb{R}}^{d}$ and a loss function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, zeroth-order optimization with the standard two-point gradient estimator \[\] iteratively updates $x$ by substituting the computationally intractable gradient with

Motivated by the observation that zeroth-order optimization with the two-point estimator inherently minimizes $\text{Tr}{({{\nabla^{2}f}{(x)}})}$, we initiate a formal study of this implicit regularization. Specifically, we analyze its convergence to flat minima, defined as the ones with the lowest trace of Hessian among all minimizers. For convex and sufficiently smooth (Assumptions 3.3. ‣ 3 Complexity for Finding Flat Minima ‣ Zeroth-Order Optimization Finds Flat Minima")) functions, we prove that Algorithm guarantees $({\mathcal{O}{({\epsilon/d^{2}})}},\epsilon)$-approximate flat minima (Definition 3.2....

Theoretical and empirical performance of zeroth-order methods is often limited by the high variance in gradient estimation. A promising direction is to combine zeroth-order and first-order methods to leverage the strengths of both. We only examine zeroth-order optimization using the standard two-point estimator. Exploring whether the convergence complexity can be further improved with possible modifications and additional algorithmic designs remains an interesting line of work. The current theoretical results require convexity and higher-order smoothness assumptions of the function....

### Convergence Analysis

Figure plots the values of the loss function and the trace of Hessian when applying gradient descent and zeroth-order optimization on Example 2.1....
