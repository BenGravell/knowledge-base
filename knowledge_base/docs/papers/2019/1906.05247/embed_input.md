Bootstrapping Upper Confidence Bound

Upper Confidence Bound (UCB) method is arguably the most celebrated one used in online decision making with partial information feedback. Existing techniques for constructing confidence bounds are typically built upon various concentration inequalities, which thus lead to over-exploration. In this paper, we propose a non-parametric and data-dependent UCB algorithm based on the multiplier bootstrap. To improve its finite sample performance, we further incorporate second-order correction into the above construction. In theory, we derive both problem-dependent and problem-independent regret bounds for multi-armed bandits under a much weaker tail assumption than the standard sub-Gaussianity. Numerical results demonstrate significant regret reductions by our method, in comparison with several baselines in a range of multi-armed and linear bandit problems.

## Introduction

In artificial intelligence, learning to make decisions online plays a critical role in many fields, such as personalized news recommendation, robotics and the game of Go. To learn to make optimal decisions as soon as possible, the decision-makers must carefully design an algorithm to balance the trade-off between the exploration and exploitation. Over-exploration could be expensive and unethical in practice, e.g., medical decision making. On the other hand, insufficient exploration tends to make an algorithm stuck at a sub-optimal solution. The delicate design of exploration methods stands in the heart of online learning and decision making.

Upper Confidence Bound (UCB) is a class of highly effective algorithms in dealing with the exploration-exploitation trade-off in bandits and reinforcement learning. The tightness of confidence bound, as is known, is the key ingredient to achieve the optimal degree of explorations. To the best of our knowledge, nearly all the existing works construct confidence bounds based on various concentration inequalities, e.g. Hoeffding-type, empirical Bernstein type or self-normalized type....

## Conclusion

In this paper, we propose a novel class of non-parametric and data-driven UCB algorithms based on multiplier bootstrap. It is easy to implement and has the potential to be generalized to other complex structured problems. As future works, we will evaluate our idea on other structured contextual bandits and reinforcement learning problems.

### Main Algorithm: Bootstrapped UCB

### Second-order Correction

The proof relies on a precise characterization of $p$-th moment of a Weibull random variable and standard symmetrization arguments. Details are deferred to Section B.2 in the supplement. This theorem generalizes the Hoeffding-type concentration inequalities for sub-Gaussian random variables (see, e.g. Proposition 5.10 in Vershynin ), and Bernstein-type concentration inequalities for sub-exponential random variables (see, e.g. Proposition 5.16 in Vershynin ) up to some constants.

In this paper, we propose a non-parametric and data-dependent UCB algorithm based on the multiplier bootstrap, called bootstrapped UCB. The principle is to use the multiplier bootstrapped quantile as the confidence bound to enforce the exploration....
