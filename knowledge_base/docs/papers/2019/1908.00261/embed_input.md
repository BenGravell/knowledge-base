On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift

Topics include Reinforcement learning, Supervised learning, Learning, Policy gradients, Markov decision process, State space, Approximation error.

Policy gradient methods are among the most effective methods in challenging reinforcement learning problems with large state and/or action spaces. However, little is known about even their most basic theoretical convergence properties, including: if and how fast they converge to a globally optimal solution or how they cope with approximation error due to using a restricted class of parametric policies. This work provides provable characterizations of the computational, approximation, and sample size properties of policy gradient methods in the context of discounted Markov Decision Processes (MDPs). We focus on both: "tabular" policy parameterizations, where the optimal policy is contained in the class and where we show global convergence to the optimal policy; and parametric policy classes (considering both log-linear and neural policy classes), which may not contain the optimal policy and where we provide agnostic learning results....

## Introduction

Policy gradient methods have a long history in the reinforcement learning (RL) literature and are an attractive class of algorithms as they are applicable to any differentiable policy parameterization; admit easy extensions to function approximation; easily incorporate structured state and action spaces; are easy to implement in a simulation based, model-free manner. Owing to their flexibility and generality, there has also been a flurry of improvements and refinements to make these ideas work robustly with deep neural network based approaches (see e.g. Schulman et al. ).

Despite the large body of empirical work around these methods, their convergence properties are only established at a relatively coarse level; in particular, the folklore guarantee is that these methods converge to a stationary point of the objective, assuming adequate smoothness properties hold and assuming either exact or unbiased estimates of a gradient can be obtained (with appropriate regularity conditions on the variance)....

With regards to sample size issues, we showed that simply using stochastic (projected) gradient ascent suffices for accurate policy optimization. However, in terms of improving sample efficiency and polynomial dependencies, there are number of important questions for future research, including variance reduction techniques along with data re-use.

There are number of compelling directions for further study. The first is in understanding how to remove the density ratio guarantees among prior algorithms; our results are suggestive that the incremental policy optimization approaches, including CPI, PSDP, and MD-MPI Geist et al., may permit such an improved analysis. The question of understanding what representations are robust to distribution shift is well-motivated by the nature of our distribution-shifted, approximation error (the transfer error)....

## Function Approximation and Distribution Shift

The proof is provided in Appendix B.2. The lemma illustrates that lack of good exploration can indeed be detrimental in policy gradient algorithms, since the gradient can be small either due to $\pi$ being near-optimal, or, simply because $\pi$ does not visit advantageous states often enough. In this sense, it also demonstrates the necessity of the distribution mismatch coefficient in Lemma 4.1....
