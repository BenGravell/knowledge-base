MuJoCo Playground

Topics include Robotics, Learning, MuJoCo playground.

We introduce MuJoCo Playground, a fully open-source framework for robot learning built with MJX, with the express goal of streamlining simulation, training, and sim-to-real transfer onto robots. With a simple "pip install playground", researchers can train policies in minutes on a single GPU. Playground supports diverse robotic platforms, including quadrupeds, humanoids, dexterous hands, and robotic arms, enabling zero-shot sim-to-real transfer from both state and pixel inputs. This is achieved through an integrated stack comprising a physics engine, batch renderer, and training environments. Along with video results, the entire framework is freely available at playground.mujoco.org

## Introduction

Reinforcement learning (RL) with subsequent transfer to hardware (sim-to-real), is emerging as a leading paradigm in modern robotics. The benefits of simulation are obvious -- safety and cheap data.

Create a simulated environment that matches the real world.

Encode desired robot behavior with a reward function.

The key enabler of this approach is a simulator that is realistic, convenient, and fast.

With this work, we aim to further advance and make sim-to-real robot learning even more accessible. We introduce MuJoCo Playground, a fully open-source framework for robot learning designed for rapid iteration and deployment of sim-to-real reinforcement learning policies. We build upon MuJoCo XLA (MJX), a JAX-based branch of the MuJoCo physics engine that runs on GPU, enabling training directly on device.

We develop a comprehensive suite of robotic environments using MJX, demonstrating sim-to-real transfer across diverse platforms including quadrupeds, humanoids, dexterous hands, and robot arms.

## Limitations

MuJoCo Playground inherits the limitations of MJX due to constraints imposed by JAX. First, just-in-time (JIT) compilation can be slow (1-3 minutes on Playground's tasks). Second, computation time related to contacts does not scale like the number of *active* contacts in the scene, but like the number of *possible* contacts in the scene. This is due to JAX's requirement of static shapes at compile time. This limitation can be overcome by using more flexible frameworks like Warp and Taichi. This upgrade is an active area of development. Finally we should note that the vision-based training using Madrona is still at an early stage.

## Conclusion

MuJoCo Playground is a library built upon the open-source MuJoCo simulator and Madrona batch renderer with implementations across several reinforcement learning and robotics environments. We demonstrate policy training on various GPU topologies using JAX and pytorch-based reinforcement learning libraries. We also demonstrate sim-to-real deployment on several robotic tasks and embodiments, from locomotion to both dexterous and non-prehensile manipulation from proprioceptive state and from pixels. We look forward to seeing the community put this resource to use in advancing robotics research and its applications.
