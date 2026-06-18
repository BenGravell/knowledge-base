An Improved Analysis of (Variance-Reduced) Policy Gradient and Natural Policy Gradient Methods

Topics include Policy gradients, Sample complexity, Natural policy gradient, NPG, Variance reduction.

In this paper, we revisit and improve the convergence of policy gradient (PG), natural PG (NPG) methods, and their variance-reduced variants, under general smooth policy parametrizations. More specifically, with the Fisher information matrix of the policy being positive definite: i) we show that a state-of-the-art variance-reduced PG method, which has only been shown to converge to stationary points, converges to the globally optimal value up to some inherent function approximation error due to policy parametrization; ii) we show that NPG enjoys a lower sample complexity; iii) we propose SRVR-NPG, which incorporates variance-reduction into the NPG update. Our improvements follow from an observation that the convergence of (variance-reduced) PG and NPG methods can improve each other: the stationary convergence analysis of PG can be applied to NPG as well, and the global convergence analysis of NPG can help to establish the global convergence of (variance-reduced) PG methods. Our analysis carefully integrates the advantages of these two lines of works.

## Introduction

Policy gradient (PG) methods, or more generally direct policy search methods, have long been recognized as one of the foundations of reinforcement learning (RL). Specifically, PG methods directly search for the optimal policy parameter that maximizes the long-term return in Markov decision processes (MDPs), following the policy gradient ascent direction. This search direction can be more efficient using a preconditioning matrix, e.g., using the natural PG direction. These methods have achieved tremendous empirical successes recently, especially boosted by the power of (deep) neural networks for policy parametrization.

In practice, the policy gradients are usually estimated via samples using Monte-Carlo rollouts and bootstrapping. Such stochastic PG methods notoriously suffer from very high variances, which not only destabilize but also slow down the convergence. Several conventional approaches have been advocated to reduce the variance of PG methods, e.g., by adding a baseline, or by using function approximation for estimating the value function, namely, developing actor-critic algorithms.

In contrast to the empirical successes of PG methods, their theoretical convergence guarantees, especially *non-asymptotic global* convergence guarantees, have not been addressed satisfactorily until very recently. By *non-asymptotic global* convergence, here we mean the convergence behavior of PG methods from any initialization, and the quality of the point they converge to (usually enjoys global optimality up to some compatible function approximation error due to policy parametrization), after a finite number of iterations/samples.

Motivated by these advances and the questions that remain to be answered, we aim in this paper to improve the convergence of PG and natural PG (NPG) methods, and their variance-reduced variants, under general smooth policy parametrizations. Our contributions are summarized as follows.

Contributions. With a focus on the conventional Monte-Carlo-based PG methods, we propose a general framework for analyzing their *global convergence*.
