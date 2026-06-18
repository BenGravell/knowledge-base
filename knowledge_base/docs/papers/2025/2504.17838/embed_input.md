CaRL: Learning Scalable Planning Policies with Simple Rewards

Topics include Autonomous driving, Reinforcement learning, Policy learning, Policy optimization, Sample efficiency.

Shows that privileged RL for autonomous-driving planning can scale better with a simple route-completion reward than with heavily shaped reward sums. CaRL is notable for treating reward simplicity as the enabling ingredient for large-batch PPO and strong closed-loop driving performance.

We investigate reinforcement learning (RL) for privileged planning in autonomous driving. State-of-the-art approaches for this task are rule-based, but these methods do not scale to the long tail. RL, on the other hand, is scalable and does not suffer from compounding errors like imitation learning. Contemporary RL approaches for driving use complex shaped rewards that sum multiple individual rewards, \eg~progress, position, or orientation rewards. We show that PPO fails to optimize a popular version of these rewards when the mini-batch size is increased, which limits the scalability of these approaches. Instead, we propose a new reward design based primarily on optimizing a single intuitive reward term: route completion. Infractions are penalized by terminating the episode or multiplicatively reducing route completion. We find that PPO scales well with higher mini-batch sizes when trained with our simple reward, even improving performance. Training with large mini-batch sizes enables efficient scaling via distributed data parallelism. We scale PPO to 300M samples in CARLA and 500M samples in nuPlan with a single 8-GPU node.

## Introduction

We consider the task of privileged planning, in which an autonomous vehicle drives using ground truth perception inputs. Such planners are traditionally rule-based. While rule-based approaches work well for regular driving, they require special scenario-specific rules to solve more complex scenarios, which is unlikely to scale to the long tail of driving scenarios.

We propose an alternative reward design that does not rely on rule-based planners. The design learns policies with route completion (RC) as the only source of reward. To learn to avoid infractions, we end the episode upon any major infraction, e.g. collision, and reduce the obtained route completion multiplicatively while the agent is violating soft constraints, e.g., exceeding the speed limit.

Our final model, named CaRL, outperforms Roach and the recent world model RL-planner Think2Drive on the longest6 v2 benchmark, by 42 and 57 Driving Score (DS) respectively. We also implement our method on the nuPlan simulator, which measures performance in realistic everyday scenarios via log replay. We show that with minimal changes, our method can achieve 91 closed-loop score on the benchmark in both non-reactive and reactive traffic. The resulting model is both 1.7 (non-reactive) and 7.9 (reactive) points better than the prior best learning based approach, Diffusion Planner, while being 10x faster at inference time.

## Conclusion

Contemporary RL methods for driving often use complex rewards that induce tradeoffs between multiple reward terms. We observe that these tradeoffs prevent scalability. Training with large mini-batch sizes with PPO leads to degenerate policies, likely since the optimization gets stuck in a local minimum of the reward. We propose an alternative reward design based on optimizing a single reward: route completion. Infractions either terminate the episode or multiplicatively reduce route completion.

We investigate urban driving at moderate speeds of up to 80 km/h. Problems specific to high-speed driving on highways are not considered.

CaRL has two main failure modes in CARLA: missing exits in highway off-ramps and other cars crashing into its rear in scenarios where another car runs a red light (rear-end collisions are counted as the agent's fault in CARLA). We show examples in the Appendix Section C.
