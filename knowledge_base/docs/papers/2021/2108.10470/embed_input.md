Isaac Gym: High Performance GPU-Based Physics Simulation for Robot Learning

Topics include Robotics, Neural networks, Learning, Isaac Gym.

Isaac Gym offers a high performance learning platform to train policies for wide variety of robotics tasks directly on GPU. Both physics simulation and the neural network policy training reside on GPU and communicate by directly passing data from physics buffers to PyTorch tensors without ever going through any CPU bottlenecks. This leads to blazing fast training times for complex robotics tasks on a single GPU with 2-3 orders of magnitude improvements compared to conventional RL training that uses a CPU based simulator and GPU for neural networks. We host the results and videos at and isaac gym can be downloaded .

## Introduction

In recent years, reinforcement learning (RL) has become one of the most promising research areas in machine learning and has demonstrated great potential for solving sophisticated decision-making problems. Deep reinforcement learning (Deep RL) has achieved superhuman performance in very challenging tasks, ranging from classic strategy games such as Go and Chess, to real-time computer games like StarCraft and DOTA. It has also shown impressive results in robotic settings, including legged locomotion and dexterous manipulation.

Simulators play a key role in training robots improving both the safety and iteration speed in the learning process. Training a humanoid robot that walks up and down stairs in the real world can lead to damage to its machinery and the environment, including humans that are working on the robot. An alternative is to train inside simulators that offer an efficient and scalable platform via trial-and-error with no safety issues as observed in the real world. To date, most researchers have relied on a combination of CPUs and GPUs to run reinforcement learning system.

Popular physics engines like MuJoCo, PyBullet, DART, Drake, V-Rep etc. need large CPU clusters to solve challenging RL tasks naturally face these bottlenecks. For instance, , almost 30,000 CPU cores (920 worker machines with 32 cores each) were used to train a robot to solve the Rubik's Cube task using RL. In a similar task, used a cluster of 384 systems with 6144 CPU cores, plus 8 NVIDIA V100 GPUs, and required 30 hours of training for RL to converge.

To address these bottlenecks, we present Isaac Gym - an end-to-end high performance robotics simulation platform. It runs an end-to-end GPU accelerated training pipeline, which allows researchers to overcome the aforementioned limitations and achieves 2-3 orders of magnitude of training speed-up in continuous control tasks. Isaac Gym leverages NVIDIA PhysX to provide a GPU-accelerated simulation back-end, allowing it to gather experience data required for robotics RL at rates only achievable using a high degree of parallelism. It provides a PyTorch tensor-based API to access the results of physics simulation natively on the GPU.
