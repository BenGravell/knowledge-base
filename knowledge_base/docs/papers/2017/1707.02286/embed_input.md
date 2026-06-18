Emergence of Locomotion Behaviours in Rich Environments

Topics include Policy gradients, Reinforcement learning, Robustness, Learning.

The reinforcement learning paradigm allows, in principle, for complex behaviours to be learned directly from simple reward signals. In practice, however, it is common to carefully hand-design the reward function to encourage a particular solution, or to derive it from demonstration data. In this paper explore how a rich environment can help to promote the learning of complex behavior. Specifically, we train agents in diverse environmental contexts, and find that this encourages the emergence of robust behaviours that perform well across a suite of tasks. We demonstrate this principle for locomotion - behaviours that are known for their sensitivity to the choice of reward. We train several simulated bodies on a diverse set of challenging terrains and obstacles, using a simple reward function based on forward progress. Using a novel scalable variant of policy gradient reinforcement learning, our agents learn to run, jump, crouch and turn as required by the environment without explicit reward-based guidance. A visual depiction of highlights of the learned behavior can be viewed following.

## Introduction

Reinforcement learning has demonstrated remarkable progress, achieving high levels of performance in Atari games, 3D navigation tasks, and board games. What is common among these tasks is that there is a well-defined reward function, such as the game score, which can be optimised to produce the desired behaviour. However, there are many other tasks where the "right" reward function is less clear, and optimisation of a naïvely selected one can lead to surprising results that do not match the expectations of the designer....

Reward engineering has led to a number of successful demonstrations of locomotion behaviour, however, these examples are known to be brittle: they can lead to unexpected results if the reward function is modified even slightly, and for more advanced behaviours the appropriate reward function is often non-obvious in the first place. Also, arguably, the requirement of careful reward design sidesteps a primary challenge of reinforcement learning: how an agent can learn for itself, directly from a limited reward signal, to achieve rich and effective behaviours. In this paper we return to this challenge.

## Discussion

We have investigated the question whether and to what extent training agents in a rich environment can lead to the emergence of behaviors that are not directly incentivized via the reward function. This departs from the common setup in control where a reward function is carefully tuned to achieve particular solutions. Instead, we use deliberately simple and generic reward functions but train the agent over a wide range of environmental conditions....

### Terrain and obstacles

We consider three continuous control tasks for benchmarking the algorithms. All environments rely on the Mujoco physics engine. Two tasks are locomotion tasks in obstacle-free environments and the third task is a planar target-reaching task that requires memory. *Planar walker*: a simple bipedal walker with 9 degrees-of-freedom (DoF) and 6 torque actuated joints. It receives a primary reward proportional to its forward velocity, additional terms penalize control and the violation of box constraints on torso height and angle. Episodes are terminated early when the walker falls. *Humanoid*: The humanoid has 28 DoF and 21 acutated joints....

### Planar Walker
