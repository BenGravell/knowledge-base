PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization

Topics include Convex optimization, Nonconvex optimization, Stochastic gradients, Deep learning, Probabilistic models, Datasets, Accuracy, Online algorithms, Optimization, Learning, PAGE, PL.

In this paper, we propose a novel stochastic gradient estimator - ProbAbilistic Gradient Estimator (PAGE) - for nonconvex optimization. PAGE is easy to implement as it is designed via a small adjustment to vanilla SGD: in each iteration, PAGE uses the vanilla minibatch SGD update with probability p_t or reuses the previous gradient with a small adjustment, at a much lower computational cost, with probability 1-p_t. We give a simple formula for the optimal choice of p_t. Moreover, we prove the first tight lower bound Omega(n+sqrt(n)/epsilon^) for nonconvex finite-sum problems, which also leads to a tight lower bound Omega(b+sqrt(b)/epsilon^) for nonconvex online problems, where b: = minsigma^/epsilon^, n. Then, we show that PAGE obtains the optimal convergence results O(n+sqrt(n)/epsilon^) (finite-sum) and O(b+sqrt(b)/epsilon^) (online) matching our lower bounds for both nonconvex finite-sum and online problems. Besides, we also show that for nonconvex functions satisfying the Polyak-Łojasiewicz (PL) condition, PAGE can automatically switch to a faster linear convergence rate O(*log frac1epsilon)....

## Introduction

Nonconvex optimization is ubiquitous across many domains of machine learning, including robust regression, low rank matrix recovery, sparse recovery and supervised learning. Driven by the applied success of deep neural networks, and the critical place nonconvex optimization plays in training them, research in nonconvex optimization has been undergoing a renaissance.

### The problem

## Conclusion

In this paper, we propose a simple and optimal PAGE algorithm for both nonconvex finite-sum and online optimization. We prove tight lower bounds and show that PAGE achieves the optimal convergence results matching our lower bounds for both nonconvex finite-sum problems and online problems. We also show that for nonconvex functions satisfying the PL condition, PAGE can automatically switch to a faster linear convergence rate. Besides, PAGE is easy to implement and we conduct several deep learning experiments (e.g., LeNet, VGG, ResNet) in PyTorch which confirm the practical superiority of PAGE....

### Corollary 2 (Optimal result for problem )

### Assumption 2 (Average $L$-smoothness)

Suppose that Assumptions 1 ‣ 3 Notation and Assumptions ‣ PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization") and 2 ‣ 3 Notation and Assumptions ‣ PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization") hold. Choose the stepsize $\eta \leq \frac{1}{L{({1 + {\sqrt{b}/b^{\prime}}})}}$, minibatch size $b = {\min{\{{\lceil\frac{2\sigma^{2}}{\epsilon^{2}}\rceil},n\}}}$, secondary minibatch size $b^{\prime} \leq \sqrt{b}$ and probability $p_{t} \equiv \frac{b^{\prime}}{b + b^{\prime}}$....

Motivated by this development, we consider the general optimization problem

where $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ is a differentiable and possibly nonconvex function. We are interested in functions having the *finite-sum* form

where the functions $f_{i}$ are also differentiable and possibly nonconvex. Form captures the standard empirical risk minimization problems in machine learning. Moreover, if the number of data samples $n$ is very large or even infinite, e.g., in the online/streaming case, then $f{(x)}$ usually is modeled via the *online* form

which we also consider in this work. For notational convenience, we adopt the notation of the finite-sum form in the descriptions and algorithms in...
