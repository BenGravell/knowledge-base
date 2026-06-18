Simple Policy Optimization

Topics include Reinforcement learning, Policy optimization, Proximal policy optimization, Simple policy optimization, SPO.

Proposes a modified policy gradient loss that achieves better performance than PPO while maintaining simplicity.

Model-free reinforcement learning algorithms have seen remarkable progress, but key challenges remain. Trust Region Policy Optimization (TRPO) is known for ensuring monotonic policy improvement through conservative updates within a trust region, backed by strong theoretical guarantees. However, its reliance on complex second-order optimization limits its practical efficiency. Proximal Policy Optimization (PPO) addresses this by simplifying TRPO's approach using ratio clipping, improving efficiency but sacrificing some theoretical robustness. This raises a natural question: Can we combine the strengths of both methods? In this paper, we introduce Simple Policy Optimization (SPO), a novel unconstrained first-order algorithm. By slightly modifying the policy loss used in PPO, SPO can achieve the best of both worlds. Our new objective improves upon ratio clipping, offering stronger theoretical properties and better constraining the probability ratio within the trust region. Empirical results demonstrate that SPO outperforms PPO with a simple implementation, particularly for training large, complex network architectures end-to-end.

## Introduction

Deep Reinforcement Learning (DRL) has achieved great success in recent years, notably in games (Mnih et al. Silver et al. Vinyals et al., ), foundation model fine-tuning (Ouyang et al. Black et al., ), and robotic control (Makoviychuk et al. Rudin et al., ). Policy gradient (PG) methods (Sutton & Barto Lehmann, ), as a major paradigm in RL, have been widely adopted by the academic community. One main practical challenge of PG methods is to reduce the variance of the gradients while keeping the bias low. In this context, a widely used technique is to add a baseline when sampling an estimate of the action-value function....

Figure 2: (Left) The only difference between SPO and PPO is the policy loss, where rt (θ) = πθ (at|st)/πθold (at|st) and ϵ is the probability ratio hyperparameter, making it simple and straightforward to implement SPO based on high-quality PPO implementations. (Right) The optimization behavior of PPO and SPO is visualized, where each scatter point represents the probability ratio of a single data point for a specific training epoch, with its color corresponding to its advantage, and the red line representing the probability ratio bound.

## Conclusion

In this paper, we introduce Simple Policy Optimization (SPO), a novel unconstrained first-order algorithm that effectively combines the strengths of Trust Region Policy Optimization (TRPO) and Proximal Policy Optimization (PPO). SPO maintains optimization within the trust region, benefiting from TRPO's theoretical guarantees while preserving the efficiency of PPO. Our experimental results demonstrate that SPO achieves competitive performance across various benchmarks with a simple implementation. Moreover, SPO simplifies the training of deep policy networks, addressing a key challenge faced by existing algorithms....

Given the old policy $\pi$, and $\Omega_{TV},\Omega_{KL}$ presented in Proposition 4.2, let

In other words, PPO-Clip aims to remove the high incentive for pushing the current policy away from the old one. PPO-Clip has gained wide adoption in the academic community due to its simplicity and performance.

It can be obtained that $f_{ppo}$ is not $\epsilon$-aligned, as $f_{ppo}$ zeros the gradients under some special cases according to. For $f_{spo}$, we have the following theorem:
