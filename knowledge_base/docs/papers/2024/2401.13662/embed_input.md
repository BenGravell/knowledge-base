The Definitive Guide to Policy Gradients in Deep Reinforcement Learning: Theory, Algorithms and Implementations

Topics include Reinforcement learning, Control, Learning, Policy gradients.

In recent years, various powerful policy gradient algorithms have been proposed in deep reinforcement learning. While all these algorithms build on the Policy Gradient Theorem, the specific design choices differ significantly across algorithms. We provide a holistic overview of on-policy policy gradient algorithms to facilitate the understanding of both their theoretical foundations and their practical implementations. In this overview, we include a detailed proof of the continuous version of the Policy Gradient Theorem, convergence results and a comprehensive discussion of practical algorithms. We compare the most prominent algorithms on continuous control environments and provide insights on the benefits of regularization. All code is available at

## Introduction

Reinforcement Learning (RL) is a powerful set of methods for an agent to learn how to act optimally in a given environment to maximize some reward signal. In contrast to other methods such as dynamic programming, RL achieves this task of learning an optimal policy, which dictates the optimal behavior, via a trial-and-error process of interacting with the environment. Most early successful applications of RL use value-based methods (e.g., ), which estimate the expected future rewards to inform the agent's decisions.

The remainder of this paper is organized as follows. Section 2 introduces fundamental definitions in RL as well as an overview of deep learning. Section 3 derives the theoretical foundations of policy gradient algorithms with a special focus on proving the Policy Gradient Theorem, based on which we will construct several existing practical algorithms in Section 4. In Section 5, we discuss convergence results from literature. Section 6, presents the results of our numerical experiments comparing the discussed algorithms. Section 7 concludes.

## Conclusion

In this work, we presented a holistic overview of on-policy policy gradient methods in reinforcement learning. We derived the theoretical foundations of policy gradient algorithms, primarily in the form of the Policy Gradient Theorem. We have shown how the most prominent policy gradient algorithms can be derived based on this theorem. We discussed common techniques used by these algorithms to stabilize training including learning an advantage function to limit the variance of estimated policy gradients, constraining the divergence between policies and regularizing the policy through entropy bonuses.

We acknowledge several limitations of our work. First, we deliberately limited our scope to on-policy algorithms, which excludes closely related off-policy policy gradient algorithms and the novelties introduced by them. Second, we presented an incomplete overview of on-policy policy gradient algorithms as other, albeit less established, algorithms exist (e.g., ) and the development of further algorithms remains an active research field. Here, we focused on the, in our view, most prominent algorithms as determined by their impact, usage and introduced novelties.
