Learning Dexterous Manipulation from Suboptimal Experts

Learning dexterous manipulation in high-dimensional state-action spaces is an important open challenge with exploration presenting a major bottleneck. Although in many cases the learning process could be guided by demonstrations or other suboptimal experts, current RL algorithms for continuous action spaces often fail to effectively utilize combinations of highly off-policy expert data and on-policy exploration data. As a solution, we introduce Relative Entropy Q-Learning (REQ), a simple policy iteration algorithm that combines ideas from successful offline and conventional RL algorithms. It represents the optimal policy via importance sampling from a learned prior and is well-suited to take advantage of mixed data distributions. We demonstrate experimentally that REQ outperforms several strong baselines on robotic manipulation tasks for which suboptimal experts are available.

## Introduction

In recent years, deep reinforcement learning (RL) algorithms have demonstrated increasing capabilities in solving complex robotic control problems both in simulation and on real robots. However, exploration remains a significant challenge for high-dimensional robotics tasks with sparse rewards -- the prevalent setting in the domain of robotic manipulation. Crafting a shaped reward function for manipulation tasks is often highly non-trivial due to the characteristics of the desired behavior, which might require complex interactions with tools to accomplish the task.

In this work, we aim to develop an algorithm that excels in the setting of reinforcement learning from suboptimal experts (RLfSE) where we have direct access to an imperfect or partial task solution, as well as the ability to collect new data.

## Relative Entropy Q-Learning

We introduce Relative Entropy Q-Learning (REQ). REQ is a policy iteration algorithm targeting the KL-constrained RL objective $\mathcal{J}_{c}$ from Equation 1 in each iteration. We start by realizing that the solution to the KL-constrained objective at iteration i, $\pi_{i} = {{\arg{\max_{\pi}\mathcal{J}_{c}}}{(\pi,\pi_{i}^{\text{prior}},\epsilon)}}$, can be obtained in closed form by formulating the Lagrangian of the constrained optimization problem and solving for $\pi$. The solution consists of a softmax over Q-values (a well known result, see e.g. ) ${\pi_{i}{(\left. a \middle| s \right.)}} \propto {\pi_{i}^{\text{prior}}{(\left.

## Policy Evaluation

The first key observation is that we can learn the state-action value function of $\pi_{i}$ without the need to explicitly represent $\pi_{i}$ via a parametric policy.

## Conclusion and Future Work

We have presented an approach for learning from suboptimal experts for complex dexterous robotic manipulation. We demonstrated that our algorithm, Relative Entropy Q-Learning (REQ), is effective in many different learning scenarios -- including off-policy and offline RL as well as RL from demonstration (RLfD). In addition, our proposed approach for Reinforcement Learning from Suboptimal Experts (RLfSE), significantly outperforms competitive baselines. In particular, REQfSE leverages intertwining exploration to solve highly complex tasks that are otherwise intractable.
