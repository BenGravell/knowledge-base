Isaac Gym: High Performance GPU-Based Physics Simulation for Robot Learning

Topics include Robotics, Neural networks, Learning, Isaac Gym.

Isaac Gym offers a high performance learning platform to train policies for wide variety of robotics tasks directly on GPU. Both physics simulation and the neural network policy training reside on GPU and communicate by directly passing data from physics buffers to PyTorch tensors without ever going through any CPU bottlenecks. This leads to blazing fast training times for complex robotics tasks on a single GPU with 2-3 orders of magnitude improvements compared to conventional RL training that uses a CPU based simulator and GPU for neural networks. We host the results and videos at and isaac gym can be downloaded at.

## Introduction

Figure 1: Isaac Gym allows high performance training on a variety of robotics environments. We benchmark on 8 different environments that offer a wide range of complexity and show the strengths of the simulator in blazing fast policy training on a single GPU. Top: Ant, Humanoid, Franka-cube-stack, Ingenuity. Bottom: Shadow Hand, ANYmal, Allegro, TriFinger.

In recent years, reinforcement learning (RL) has become one of the most promising research areas in machine learning and has demonstrated great potential for solving sophisticated decision-making problems. Deep reinforcement learning (Deep RL) has achieved superhuman performance in very challenging tasks, ranging from classic strategy games such as Go and Chess, to real-time computer games like StarCraft and DOTA. It has also shown impressive results in robotic settings, including legged locomotion and dexterous manipulation.

## Summary

We show that Isaac Gym is a high performance and high-fidelity framework that allows blistering fast training on many challenging simulated robotic environments on a single NVIDIA A100 GPU that previously would have required large heterogeneous clusters of CPUs and GPUs using a conventional RL setup with CPU-only simulators. Moreover, the simulation backend is also suited for learning contact-rich manipulations as confirmed by our sim-to-real transfer demonstrations with ANYmal locomotion and TriFinger cube reposing.

### Key Experimental Details

## Physics Simulation

Figure 9: Locomotion environments and the corresponding reward curves.

Simulators play a key role in training robots improving both the safety and iteration speed in the learning process. Training a humanoid robot that walks up and down stairs in the real world can lead to damage to its machinery and the environment, including humans that are working on the robot. An alternative is to train inside simulators that offer an efficient and scalable platform via trial-and-error with no safety issues as observed in the real world. To date, most researchers have relied on a combination of CPUs and GPUs to run reinforcement learning system....

However, switching back and forth between CPU cores optimized for sequential tasks and GPUs which offer large-scale parallelism is by nature inefficient, requiring data to be transferred between different parts of the system at multiple points during...
