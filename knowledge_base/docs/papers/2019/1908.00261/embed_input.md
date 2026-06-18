On the Theory of Policy Gradient Methods: Optimality, Approximation, and Distribution Shift

Topics include Reinforcement learning, Supervised learning, Learning, Policy gradients, Markov decision process, State space, Approximation error.

Policy gradient methods are among the most effective methods in challenging reinforcement learning problems with large state and/or action spaces. However, little is known about even their most basic theoretical convergence properties, including: if and how fast they converge to a globally optimal solution or how they cope with approximation error due to using a restricted class of parametric policies. This work provides provable characterizations of the computational, approximation, and sample size properties of policy gradient methods in the context of discounted Markov Decision Processes (MDPs). We focus on both: "tabular" policy parameterizations, where the optimal policy is contained in the class and where we show global convergence to the optimal policy; and parametric policy classes (considering both log-linear and neural policy classes), which may not contain the optimal policy and where we provide agnostic learning results.

## Introduction

Policy gradient methods have a long history in the reinforcement learning (RL) literature and are an attractive class of algorithms as they are applicable to any differentiable policy parameterization; admit easy extensions to function approximation; easily incorporate structured state and action spaces; are easy to implement in a simulation based, model-free manner. Owing to their flexibility and generality, there has also been a flurry of improvements and refinements to make these ideas work robustly with deep neural network based approaches (see e.g. Schulman et al. ).

Despite the large body of empirical work around these methods, their convergence properties are only established at a relatively coarse level; in particular, the folklore guarantee is that these methods converge to a stationary point of the objective, assuming adequate smoothness properties hold and assuming either exact or unbiased estimates of a gradient can be obtained (with appropriate regularity conditions on the variance).

Overall, the results of this work place policy gradient methods under a solid theoretical footing, analogous to the global convergence guarantees of iterative value function based algorithms.

## Discussion

This work provides a systematic study of the convergence properties of policy optimization techniques, both in the tabular and the function approximation settings. At the core, our results imply that the non-convexity of the policy optimization problem is not the fundamental challenge for typical variants of the policy gradient approach. This is evidenced by the global convergence results which we establish and that demonstrate the relative niceness of the underlying optimization problem.

In the tabular case, our results show that the nature and severity of the exploration/distribution mismatch term differs in different policy optimization approaches. For instance, we find that doing policy gradient in its standard form for both the direct and softmax parameterizations can be slow to converge, particularly in the face of distribution mismatch, even when policy gradients are computed exactly. Natural policy gradient, on the other hand, enjoys a fast dimension-free convergence when we are in tabular settings with exact gradients.
