Infinite-Horizon Policy-Gradient Estimation

Topics include Policy gradients, Reinforcement learning, Partial observability, Average reward, Gradient estimation, Simulation-based optimization, Bias-variance tradeoff.

Introduces GPOMDP, an online simulation-based estimator for policy gradients in average-reward POMDPs. The paper is notable for giving a memory-light eligibility-trace estimator with an explicit bias-variance parameter and connecting the choice of that parameter to the mixing behavior of the controlled process.

Gradient-based approaches to direct policy search in reinforcement learning have received much recent attention as a means to solve problems of partial observability and to avoid some of the problems associated with policy degradation in value-function methods. In this paper we introduce GPOMDP, a simulation-based algorithm for generating a biased estimate of the gradient of the average reward in Partially Observable Markov Decision Processes (POMDPs) controlled by parameterized stochastic policies. A similar algorithm was proposed by Kimura, Yamamura, and Kobayashi. The algorithm's chief advantages are that it requires storage of only twice the number of policy parameters, uses one free parameter beta in [0, 1) (which has a natural interpretation in terms of bias-variance trade-off), and requires no knowledge of the underlying state. We prove convergence of GPOMDP, and show how the correct choice of the parameter beta is related to the mixing time of the controlled POMDP.

## Introduction

Dynamic Programming is the method of choice for solving problems of decision making under uncertainty ( ?). However, the application of Dynamic Programming becomes problematic in large or infinite state-spaces, in situations where the system dynamics are unknown, or when the state is only partially observed. In such cases one looks for approximate techniques that rely on simulation, rather than an explicit model, and parametric representations of either the value-function or the policy, rather than exact representations.

Despite this success, most algorithms for training approximate value functions suffer from the same theoretical flaw: the performance of the greedy policy derived from the approximate value-function is not guaranteed to improve on each iteration, and in fact can be worse than the old policy by an amount equal to the maximum approximation error over all states. This can happen even when the parametric class contains a value function whose corresponding greedy policy is optimal. We illustrate this with a concrete and very simple example in Appendix A.

An alternative approach that circumvents this problem---the approach we pursue here---is to consider a class of stochastic policies parameterized by $\theta \in {\mathbb{R}}^{K}$, compute the gradient with respect to $\theta$ of the average reward, and then improve the policy by adjusting the parameters in the gradient direction. Note that the policy could be directly parameterized, or it could be generated indirectly from a value function.

## Conclusion

We have presented a general algorithm ($MCG$) for computing arbitrarily accurate approximations to the gradient of the average reward in a parameterized Markov chain. When the chain's transition matrix has distinct eigenvalues, the accuracy of the approximation was shown to be controlled by the size of the subdominant eigenvalue $|\lambda_{2}|$. We showed how the algorithm could be modified to apply to partially observable Markov decision processes controlled by parameterized stochastic policies, with both discrete and continuous control, observation and state spaces ($GPOMDP$).
