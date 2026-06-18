Scaling Is All You Need: Autonomous Driving with JAX-Accelerated Reinforcement Learning

Topics include Reinforcement learning, Autonomous driving, Vehicles, Safety, Scalability, Learning, Need, Machine learning.

Reinforcement learning has been demonstrated to outperform even the best humans in complex domains like video games. However, running reinforcement learning experiments on the required scale for autonomous driving is extremely difficult. Building a large scale reinforcement learning system and distributing it across many GPUs is challenging. Gathering experience during training on real world vehicles is prohibitive from a safety and scalability perspective. Therefore, an efficient and realistic driving simulator is required that uses a large amount of data from real-world driving. We bring these capabilities together and conduct large-scale reinforcement learning experiments for autonomous driving. We demonstrate that our policy performance improves with increasing scale. Our best performing policy reduces the failure rate by 64% while improving the rate of driving progress by 25% compared to the policies produced by state-of-the-art machine learning for autonomous driving.

## Introduction

In this paper, we set up a scalable reinforcement learning framework and combine it with an efficient simulator for autonomous driving based on real-world data. We then conduct experiments on billions of agent steps with different model sizes in order to determine if we can overcome the constrained state space of the simulator by using increasingly more real-world data.

The

We demonstrate how to use prerecorded real-world driving data in a hardware-accelerated simulator as part of distributed reinforcement learning to achieve improving policy performance with increasing experiment size.

We demonstrate that our largest scale experiments, using a 25M parameter model on 6000 h of human-expert driving from San Francisco training on 2.5 billion agent steps, reduced the failure rate compared to the current state of the art by 64%.
