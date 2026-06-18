Simple Policy Optimization

Topics include Reinforcement learning, Policy optimization, Proximal policy optimization, Simple policy optimization, SPO.

Proposes a modified policy gradient loss that achieves better performance than PPO while maintaining simplicity.

Model-free reinforcement learning algorithms have seen remarkable progress, but key challenges remain. Trust Region Policy Optimization (TRPO) is known for ensuring monotonic policy improvement through conservative updates within a trust region, backed by strong theoretical guarantees. However, its reliance on complex second-order optimization limits its practical efficiency. Proximal Policy Optimization (PPO) addresses this by simplifying TRPO's approach using ratio clipping, improving efficiency but sacrificing some theoretical robustness. This raises a natural question: Can we combine the strengths of both methods? In this paper, we introduce Simple Policy Optimization (SPO), a novel unconstrained first-order algorithm. By slightly modifying the policy loss used in PPO, SPO can achieve the best of both worlds. Our new objective improves upon ratio clipping, offering stronger theoretical properties and better constraining the probability ratio within the trust region. Empirical results demonstrate that SPO outperforms PPO with a simple implementation, particularly for training large, complex network architectures end-to-end.

## Introduction

Deep Reinforcement Learning (DRL) has achieved great success in recent years, notably in games (Mnih et al. Silver et al. Vinyals et al., ), foundation model fine-tuning (Ouyang et al. Black et al., ), and robotic control (Makoviychuk et al. Rudin et al., ). Policy gradient (PG) methods (Sutton & Barto Lehmann, ), as a major paradigm in RL, have been widely adopted by the academic community. One main practical challenge of PG methods is to reduce the variance of the gradients while keeping the bias low. In this context, a widely used technique is to add a baseline when sampling an estimate of the action-value function.

To address these challenges, Schulman et al. proved that optimizing a certain surrogate objective guarantees policy improvement with non-trivial step sizes. Subsequently, the TRPO algorithm was derived through a series of approximations, which impose a trust region constraint during the policy iterations, leading to monotonic policy improvement in theory. However, given the complexity of second-order optimization, TRPO is highly inefficient and can be hard to extend to large-scale RL environments.

In this paper, we propose a new model-free RL algorithm named Simple Policy Optimization (SPO) designed to more effectively bound probability ratios through a novel objective function. The key differences in optimization behavior between PPO and SPO are illustrated in Figure.

To overcome PPO's limitation in constraining probability ratios, we propose a new objective function, leading to the development of the proposed SPO algorithm.

## Conclusion

In this paper, we introduce Simple Policy Optimization (SPO), a novel unconstrained first-order algorithm that effectively combines the strengths of Trust Region Policy Optimization (TRPO) and Proximal Policy Optimization (PPO). SPO maintains optimization within the trust region, benefiting from TRPO's theoretical guarantees while preserving the efficiency of PPO. Our experimental results demonstrate that SPO achieves competitive performance across various benchmarks with a simple implementation. Moreover, SPO simplifies the training of deep policy networks, addressing a key challenge faced by existing algorithms.
