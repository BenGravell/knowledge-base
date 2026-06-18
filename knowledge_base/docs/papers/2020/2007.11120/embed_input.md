On Linear Convergence of Policy Gradient Methods for Finite MDPs

Topics include Policy iteration, Optimization, Policy gradients.

We revisit the finite time analysis of policy gradient methods in the one of the simplest settings: finite state and action MDPs with a policy class consisting of all stochastic policies and with exact gradient evaluations. There has been some recent work viewing this setting as an instance of smooth non-linear optimization problems and showing sub-linear convergence rates with small step-sizes. Here, we take a different perspective based on connections with policy iteration and show that many variants of policy gradient methods succeed with large step-sizes and attain a linear rate of convergence.

## Introduction

Policy gradient methods, dating back to the works of, along with their modern variants, have emerged as one of the most effective classes of algorithms for solving challenging reinforcement learning problems with impressive empirical success. Despite this, little was known about their global convergence properties, as these methods search over a parameterized class of policies by performing (stochastic) gradient descent on a scalar loss function that is typically non-convex.

This has changed recently with several recent papers analysing the global convergence properties of policy gradient methods. Our earlier work identifies properties for general MDPs which guarantee that (despite non-convexity) the optimization landscape does not suffer from spurious local optima, thereby implying convergence of policy gradient methods to globally optimal solutions. Though that work does not consider specific algorithms, some convergence rates for follow easily from the framework (e.g. a sub-linear convergence rate for tabular MDPs using projected gradient descent with natural parameterization)....

## Conclusion and Future Work

In this work, we use illuminating connections with policy iteration as shown in Bhandari and Russo to show how many variants of policy gradient algorithms with large step-sizes and exact gradient evaluations converge geometrically fast for tabular MDPs. An interesting question for future work is whether these results can be extended to function approximation settings where the policy class might be restricted, for example in Agarwal et al.. Another interesting question is whether our results hold in settings where unbiased estimates of the value functions are obtained via sampling....

### Remark 1 (Policy parameterization and infima vs minima)

Note that for tabular MDPs, a policy iteration step is simple as it reduces to solving a linear optimization problem over the probability simplex, and the optimal solution is to select the best action for each state.

where $\rho_{\min} = {{\min_{s \in \mathcal{S}}\rho}{(s)}}$. A natural question to ask is whether the presence of the factor of $\rho_{\min}$ in the geometric rate is merely an artifact of our analysis technique and if in practice, line search always ends up picking the policy iteration update corresponding to $\alpha = 1$....
