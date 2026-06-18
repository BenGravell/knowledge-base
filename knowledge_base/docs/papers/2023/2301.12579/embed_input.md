Sample Efficient Deep Reinforcement Learning via Local Planning

The focus of this work is sample-efficient deep reinforcement learning (RL) with a simulator. One useful property of simulators is that it is typically easy to reset the environment to a previously observed state. We propose an algorithmic framework, named uncertainty-first local planning (UFLP), that takes advantage of this property. Concretely, in each data collection iteration, with some probability, our meta-algorithm resets the environment to an observed state which has high uncertainty, instead of sampling according to the initial-state distribution. The agent-environment interaction then proceeds as in the standard online RL setting. We demonstrate that this simple procedure can dramatically improve the sample cost of several baseline RL algorithms on difficult exploration tasks. Notably, with our framework, we can achieve super-human performance on the notoriously hard Atari game, Montezuma's Revenge, with a simple (distributional) double DQN. Our work can be seen as an efficient approximate implementation of an existing algorithm with theoretical guarantees, which offers an interpretation of the positive empirical results.

## Introduction

Simulators are ubiquitous in modern reinforcement learning (RL). They correspond to either to the environment itself (as in chess, go, and video games ) or to a simplified model of the true environment (such as robotic arm manipulation, car driving, or plasma shape control in fusion ). Simulators have been widely used in RL research. Many standard benchmarks in RL involve simulators, for example, Atari games, Mujoco simulation engine, OpenAI Gym, DeepMind control suite, and DeepMind Lab....

Local access has received less attention from the RL community compared online access. On the theory side, several recent works show that local access makes sample-efficient learning possible in settings where it has not been shown in the online access setting. On the empirical side, the *vine* method in TRPO uses local access to obtain better estimates of the value function, and the Go-Explore algorithm of Ecoffet et al. relies on local access to achieve state-of-the-art performance on several hard-exploration Atari games....

## Conclusions and Future Directions

We propose a new algorithmic framework for learning with a simulator under the local access protocol. We demonstrate that our proposed uncertainty-first approach to revisiting states in history can dramatically improve the sample cost of several baseline algorithms on sparse-reward environments. An important direction for future work is improving the quality of uncertainty estimation in MDPs, since the this directly affects the effectiveness of the framework. Another interesting direction for future work is to extend this approach to partially observed environments.

### Policy Iteration

One intuition behind the criterion that chooses an uncertain state as a starting point is that it expands the subset of the state space that we can use to start the data collection process, which in turn helps control extrapolation errors in value function estimation. Revisiting uncertain states can also improve sample efficiency in environments where states that are important for decision-making are difficult to reach.

In this section, we evaluate the benefits of local vs. online access by training agents on difficult exploration tasks. We use two (bsuite) environments: Deep Sea and Cartpole Swingup, and four Atari games: Montezuma's Revenge, PrivateEye, Venture, and Pitfall....
