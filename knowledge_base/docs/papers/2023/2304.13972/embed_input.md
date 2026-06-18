Convergence of Adam under Relaxed Assumptions

In this paper, we provide a rigorous proof of convergence of the Adaptive Moment Estimate (Adam) algorithm for a wide class of optimization objectives. Despite the popularity and efficiency of the Adam algorithm in training deep neural networks, its theoretical properties are not yet fully understood, and existing convergence proofs require unrealistically strong assumptions, such as globally bounded gradients, to show the convergence to stationary points. In this paper, we show that Adam provably converges to epsilon-stationary points with O(epsilon^(-4)) gradient complexity under far more realistic conditions. The key to our analysis is a new proof of boundedness of gradients along the optimization trajectory of Adam, under a generalized smoothness assumption according to which the local smoothness (i.e., Hessian norm when it exists) is bounded by a sub-quadratic function of the gradient norm. Moreover, we propose a variance-reduced version of Adam with an accelerated gradient complexity of O(epsilon^(-3)).

## Introduction

In this paper, we study the non-convex unconstrained stochastic optimization problem

The Adaptive Moment Estimation (Adam) algorithm has become one of the most popular optimizers for solving when $f$ is the loss for training deep neural networks. Owing to its efficiency and robustness to hyper-parameters, it is widely applied or even sometimes the default choice in many machine learning application domains such as natural language processing, generative adversarial networks, computer vision, and reinforcement learning. It is also well known that Adam significantly outperforms stochastic gradient descent (SGD) for certain models like transformer.

### Understanding why Adam is better than SGD

We want to note that our results can not explain why Adam is better than SGD for training transformers, because shows that non-adaptive SGD converges with the same $\mathcal{O}{(\epsilon^{- 4})}$ gradient complexity under even weaker conditions. It would be interesting and impactful if one can find a reasonable setting (function class, gradient oracle, etc) under which Adam or other adaptive methods provably outperform SGD.

### Theorem 4.2

The standard smooth function class is very restrictive as it only contains functions that are upper and lower bounded by quadratic functions. The $(L_{0},L_{1})$ smooth function class is more general since it also contains, e.g., univariate polynomials and exponential functions. Assumption 2 is even more general and contains univariate rational functions, double exponential functions, etc. See Appendix B.1 smoothness ‣ Convergence of Adam Under Relaxed Assumptions") for the formal propositions and proofs....

For any $t < \tau$, choosing $G \geq \lambda$ and a small enough $\eta$,

Despite its success in practice, theoretical analyses of Adam are still limited. The original proof of convergence in was later shown by Reddi et al. to contain gaps. The authors in also showed that for a range of momentum parameters chosen *independently with the problem instance*, Adam does not necessarily converge even for convex objectives. However, in deep learning practice, the hyper-parameters are in fact *problem-dependent* as they are usually tuned after given the problem and weight initialization....

To address the above-mentioned gap between theory and practice, we provide a new convergence analysis of Adam *without...
