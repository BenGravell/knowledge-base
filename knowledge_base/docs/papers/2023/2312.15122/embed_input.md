Scaling Is All You Need: Autonomous Driving with JAX-Accelerated Reinforcement Learning

Topics include Reinforcement learning, Autonomous driving, Vehicles, Safety, Scalability, Learning, Need, Machine learning.

Reinforcement learning has been demonstrated to outperform even the best humans in complex domains like video games. However, running reinforcement learning experiments on the required scale for autonomous driving is extremely difficult. Building a large scale reinforcement learning system and distributing it across many GPUs is challenging. Gathering experience during training on real world vehicles is prohibitive from a safety and scalability perspective. Therefore, an efficient and realistic driving simulator is required that uses a large amount of data from real-world driving. We bring these capabilities together and conduct large-scale reinforcement learning experiments for autonomous driving. We demonstrate that our policy performance improves with increasing scale. Our best performing policy reduces the failure rate by 64% while improving the rate of driving progress by 25% compared to the policies produced by state-of-the-art machine learning for autonomous driving.

## Introduction

In this paper, we set up a scalable reinforcement learning framework and combine it with an efficient simulator for autonomous driving based on real-world data. We then conduct experiments on billions of agent steps with different model sizes in order to determine if we can overcome the constrained state space of the simulator by using increasingly more real-world data.

The main contributions of our work are:

In this paper we combined an efficient and realistic autonomous driving simulator with a scalable reinforcement learning framework. This allowed us to run large scale reinforcement learning experiments training on billions of agents steps with increasing model size on different dataset sizes of real-world driving.

Our data shows that we can obtain similar scaling behavior as in other reinforcement learning settings \[\] when using increasingly large datasets of real-world driving. In particular, we were able to obtain better policies with larger models when using sufficiently large datasets. Our best policy reduces the failure rate compared to the current SOTA \[\] by 64% while improving progress by 25%. These results are very encouraging, and motivate further experiments with increasing size....

The observation space retrieves a subset of the information of the environment state and transforms the fields of the observation vector into an agent-centric coordinate frame.

Data segments of different sizes are not suitable for parallel execution on hardware accelerators. To overcome this issue, a common maximum size for each type of data is defined. All data elements in the dynamic data are then padded to the defined maximum size for each time step.

## Evaluation

We demonstrate how to use prerecorded real-world driving data in a hardware-accelerated simulator as part of distributed reinforcement learning to achieve improving policy performance with increasing experiment size.

We demonstrate that our largest scale experiments, using a 25M parameter model on 6000 h of human-expert driving from San Francisco training on 2.5 billion agent steps, reduced the failure rate compared to the current state of the art \[\] by 64%.

## Related work

In this paper we present a hardware-accelerated autonomous driving simulator for real-world driving scenarios, which is similar to Waymax \[\]....
