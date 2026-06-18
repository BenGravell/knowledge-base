Being Optimistic to Be Conservative: Quickly Learning a CVaR Policy

Topics include Reinforcement learning, Bellman equations, Uncertainty, Learning, Conservative, Conditional value at risk, Markov decision process.

While maximizing expected return is the goal in most reinforcement learning approaches, risk-sensitive objectives such as conditional value at risk (CVaR) are more suitable for many high-stakes applications. However, relatively little is known about how to explore to quickly learn policies with good CVaR. In this paper, we present the first algorithm for sample-efficient learning of CVaR-optimal policies in Markov decision processes based on the optimism in the face of uncertainty principle. This method relies on a novel optimistic version of the distributional Bellman operator that moves probability mass from the lower to the upper tail of the return distribution. We prove asymptotic convergence and optimism of this operator for the tabular policy evaluation case. We further demonstrate that our algorithm finds CVaR-optimal policies substantially faster than existing baselines in several simulated environments with discrete and continuous state spaces.

## Introduction

A key goal in reinforcement learning (RL) is to quickly learn to make good decisions by interacting with an environment. In most cases the quality of the decision policy is evaluated with respect to its expected (discounted) sum of rewards. However, in many interesting cases, it is important to consider the full distributions over the potential sum of rewards, and the desired objective may be a risk-sensitive measure of this distribution....

A popular risk-sensitive measure of a distribution of outcomes is the Conditional Value at Risk (CVaR) (?). Intuitively, CVaR is the expected reward in the worst $\alpha$-fraction of outcomes, and has seen extensive use in financial portfolio optimization (?), often under the name "expected shortfall". While there has been recent interest in the RL community in learning to converge or identify good CVaR decision policies in Markov decision processes (?; ?; ?; ?), interestingly we are unaware of prior work focused on how to quickly learn such CVaR MDP policies, even though sample efficient RL for maximizing expected outcomes is a deep and...

## Conclusion

We present a new algorithm for quickly learning CVaR-optimal policies in Markov decision processes. This algorithm is the first to leverage optimism in combination with distributional reinforcement learning to learn risk-averse policies in a sample-efficient manner. Unlike existing work on expected return criteria which rely on reward bonuses for optimism, We introduce optimism by directly modifying the target return distribution and provide a theoretical justification that in the evaluation case for finite MDPs, this indeed yields optimistic estimates....

Our setting differs from (?) in the sense that we have to compute the count before taking the action $a$. A naive way would be to try all actions and train the model to compute the counts but this method is slow and requires the environment to support an undo action. Instead, we can estimate $PG$ for all actions as follows. Consider the density model parametrized by $\theta$, $\rho{(s,a;\theta)}$. After observing $(s,a)$, the training step to maximize the log likelihood will update the parameters by $\theta^{\prime} = {\theta + {\alpha{{\nabla_{\theta}\log}\rho}{(s,a;\theta)}}}$, where $\alpha$ is the learning rate....

### Theorem 2
