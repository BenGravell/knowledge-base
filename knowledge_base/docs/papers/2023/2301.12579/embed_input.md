Sample Efficient Deep Reinforcement Learning via Local Planning

The focus of this work is sample-efficient deep reinforcement learning (RL) with a simulator. One useful property of simulators is that it is typically easy to reset the environment to a previously observed state. We propose an algorithmic framework, named uncertainty-first local planning (UFLP), that takes advantage of this property. Concretely, in each data collection iteration, with some probability, our meta-algorithm resets the environment to an observed state which has high uncertainty, instead of sampling according to the initial-state distribution. The agent-environment interaction then proceeds as in the standard online RL setting. We demonstrate that this simple procedure can dramatically improve the sample cost of several baseline RL algorithms on difficult exploration tasks. Notably, with our framework, we can achieve super-human performance on the notoriously hard Atari game, Montezuma's Revenge, with a simple (distributional) double DQN. Our work can be seen as an efficient approximate implementation of an existing algorithm with theoretical guarantees, which offers an interpretation of the positive empirical results.

## Introduction

Simulators are ubiquitous in modern reinforcement learning (RL). They correspond to either to the environment itself (as in chess, go, and video games ) or to a simplified model of the true environment (such as robotic arm manipulation, car driving, or plasma shape control in fusion ). Simulators have been widely used in RL research. Many standard benchmarks in RL involve simulators, for example, Atari games, Mujoco simulation engine, OpenAI Gym, DeepMind control suite, and DeepMind Lab.

Local access has received less attention from the RL community compared online access. On the theory side, several recent works show that local access makes sample-efficient learning possible in settings where it has not been shown in the online access setting. On the empirical side, the *vine* method in TRPO uses local access to obtain better estimates of the value function, and the Go-Explore algorithm of Ecoffet et al. relies on local access to achieve state-of-the-art performance on several hard-exploration Atari games.

## Contributions

We propose a general algorithmic framework for RL with a simulator under the local access protocol. Our framework, named *uncertainty-first local planning* (UFLP), revisits states from the agent's history based on the uncertainty about their value.

We instantiate this framework with several base RL agents (deep Q-networks, policy iteration) and uncertainty estimates (ensemble, feature covariance, approximate counts, random network distillation).
