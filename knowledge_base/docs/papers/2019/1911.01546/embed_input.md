Being Optimistic to Be Conservative: Quickly Learning a CVaR Policy

Topics include Reinforcement learning, Bellman equations, Uncertainty, Learning, Conservative, Conditional value at risk, Markov decision process.

While maximizing expected return is the goal in most reinforcement learning approaches, risk-sensitive objectives such as conditional value at risk (CVaR) are more suitable for many high-stakes applications. However, relatively little is known about how to explore to quickly learn policies with good CVaR. In this paper, we present the first algorithm for sample-efficient learning of CVaR-optimal policies in Markov decision processes based on the optimism in the face of uncertainty principle. This method relies on a novel optimistic version of the distributional Bellman operator that moves probability mass from the lower to the upper tail of the return distribution. We prove asymptotic convergence and optimism of this operator for the tabular policy evaluation case. We further demonstrate that our algorithm finds CVaR-optimal policies substantially faster than existing baselines in several simulated environments with discrete and continuous state spaces.

## Introduction

A key goal in reinforcement learning (RL) is to quickly learn to make good decisions by interacting with an environment. In most cases the quality of the decision policy is evaluated with respect to its expected (discounted) sum of rewards. However, in many interesting cases, it is important to consider the full distributions over the potential sum of rewards, and the desired objective may be a risk-sensitive measure of this distribution.

In this paper we work towards sample efficient reinforcement learning algorithms that can quickly identify a policy with an optimal CVaR. Our focus is in minimizing the amount of experience needed to find such a policy, similar in spirit to probably approximately correct RL methods for expected reward. Note that this is different than another important topic in risk-sensitive RL, which focuses on safe exploration: algorithms that focus on avoiding any potentially very poor outcomes during learning.

Our approach is inspired by the popular and effective principle of optimism in the face of uncertainty (OFU) in sample efficient RL for maximizing expected outcomes (?; ?). Such work typically works by considering uncertainty over the MDP model parameters or state-action value function, and constructing an optimistic value function given that uncertainty that is then used to guide decision making. To take a similar idea for rapidly learning the optimal CVaR policy, we seek to consider the uncertainty in the distribution of outcomes possible and the resulting CVaR value.

## Conclusion

We present a new algorithm for quickly learning CVaR-optimal policies in Markov decision processes. This algorithm is the first to leverage optimism in combination with distributional reinforcement learning to learn risk-averse policies in a sample-efficient manner. Unlike existing work on expected return criteria which rely on reward bonuses for optimism, We introduce optimism by directly modifying the target return distribution and provide a theoretical justification that in the evaluation case for finite MDPs, this indeed yields optimistic estimates.
