CaRL: Learning Scalable Planning Policies with Simple Rewards

Topics include Autonomous driving, Reinforcement learning, Policy learning, Policy optimization, Sample efficiency.

Shows that privileged RL for autonomous-driving planning can scale better with a simple route-completion reward than with heavily shaped reward sums. CaRL is notable for treating reward simplicity as the enabling ingredient for large-batch PPO and strong closed-loop driving performance.

We investigate reinforcement learning (RL) for privileged planning in autonomous driving. State-of-the-art approaches for this task are rule-based, but these methods do not scale to the long tail. RL, on the other hand, is scalable and does not suffer from compounding errors like imitation learning. Contemporary RL approaches for driving use complex shaped rewards that sum multiple individual rewards, \eg~progress, position, or orientation rewards. We show that PPO fails to optimize a popular version of these rewards when the mini-batch size is increased, which limits the scalability of these approaches. Instead, we propose a new reward design based primarily on optimizing a single intuitive reward term: route completion. Infractions are penalized by terminating the episode or multiplicatively reducing route completion. We find that PPO scales well with higher mini-batch sizes when trained with our simple reward, even improving performance. Training with large mini-batch sizes enables efficient scaling via distributed data parallelism. We scale PPO to 300M samples in CARLA and 500M samples in nuPlan with a single 8-GPU node....

## Introduction

We consider the task of privileged planning, in which an autonomous vehicle drives using ground truth perception inputs. Such planners are traditionally rule-based. While rule-based approaches work well for regular driving \[\], they require special scenario-specific rules to solve more complex scenarios \[\], which is unlikely to scale to the long tail of driving scenarios.

Training neural planners with imitation learning (IL) is a popular alternative to rule-based approaches, because these methods can scale with data. Yet surprisingly, these methods underperform compared to rule-based or hybrid approaches \[\]. A common explanation for this behavior is that IL suffers from a distribution shift between the open-loop training objective and the closed-loop inference task.

Our reward gives fewer local hints than other rewards. We have deliberately chosen an RL algorithm (PPO) that uses Monte-Carlo returns for optimization, which sum up rewards. This might alleviate the absence of locality. RL algorithms based on Q-learning, that rely on local TD-prediction, such as Soft-Actor Critic \[\], may have a harder time optimizing our reward, although we have not investigated other algorithms.

We think these limitations can be addressed and are promising directions for future work.

The soft penalties $p_{t}$ are $1$ if their condition is not violated and otherwise have a value $\in {\lbrack 0,1)}$ depending on the type of infraction. Soft penalties are constraints that the agent should typically adhere to, such as staying within the speed limit, but may violate in order to avoid a hard penalty like a collision. It is important that soft penalty factors that the agent cannot avoid violating early on in training, such as comfort, need to be $> 0$. Otherwise, the agent would receive no reward. It is possible to apply a soft penalty for multiple frames e.g....

Table 1: Default Hyperparameters of PPO for CARLA and Atari.

### CARLA

Figure 1: Simple rewards scale with mini-batch size. Typical rewards in driving consist of complex rewards that trade off many individual components. This limits scalability as PPO gets stuck in local minima with larger mini-batch sizes. We propose a simple alternative based on maximizing route completion that scales well with mini-batch size.
