GPUDrive: Data-driven, Multi-agent Driving Simulation at 1 Million FPS

Topics include Reinforcement learning, Multi-agent systems, Datasets, Optimization, Planning, Learning, GPUDrive.

Multi-agent learning algorithms have been successful at generating superhuman planning in various games but have had limited impact on the design of deployed multi-agent planners. A key bottleneck in applying these techniques to multi-agent planning is that they require billions of steps of experience. To enable the study of multi-agent planning at scale, we present GPUDrive. GPUDrive is a GPU-accelerated, multi-agent simulator built on top of the Madrona Game Engine capable of generating over a million simulation steps per second. Observation, reward, and dynamics functions are written directly in C++, allowing users to define complex, heterogeneous agent behaviors that are lowered to high-performance CUDA. Despite these low-level optimizations, GPUDrive is fully accessible through Python, offering a seamless and efficient workflow for multi-agent, closed-loop simulation. Using GPUDrive, we train reinforcement learning agents on the Waymo Open Motion Dataset, achieving efficient goal-reaching in minutes and scaling to thousands of scenarios in hours. We open-source the code and pre-trained agents at

## Introduction

Multi-agent learning has been impactful across a wide range of fully cooperative and zero-sum games (Cui et al. Wurman et al. Pérolat et al. Silver et al. Jaderberg et al. Bakhtin et al., ). However, its impact on multi-agent planning for settings that mix humans and robots has been muted. In contrast to the ubiquity of multi-agent learning-based agents in zero-sum games, multi-agent planners for most practical robotic systems are not derived from the output of game-theoretically sound learning algorithms.

The divergence in preferred technique between these two domains is partially the outcome of two distinct, challenging components of real-world multi-agent planning. First, unlike zero-sum games, it is necessary to play a human-compatible strategy that is difficult to identify without data. Second, generating the billions of samples needed for multi-agent learning algorithms is difficult with existing simulators. The former challenge is difficult for multi-agent learning since there is not a clear equilibrium concept that algorithms should be pursuing.

To address these challenges and unlock multi-agent learning as a tool for generating capable self-driving planners, we introduce GPUDrive. GPUDrive is a simulator intended to mix real-world driving data with simulation speeds that enable the application of sample-inefficient but effective RL algorithms to the design of autonomous planners. GPUDrive runs at over a million steps per second on both consumer-grade and datacenter-class GPUs and has a sufficiently light memory footprint to support hundreds to thousands of simultaneous worlds (environments) with hundreds of agents per world.

## Conclusion

In this work, we present GPUDrive, a GPU-accelerated, multi-agent, and data-driven simulator. GPUDrive is intended to help generate the billions of samples that are likely needed to achieve effective reinforcement learning for multi-agent driving planners. By building atop the Madrona Engine, we can scale GPUDrive to hundreds of worlds with potentially thousands of agents leading to throughput of millions of steps per second. This throughput occurs while synthesizing complex observations such as LiDAR.

## Future work and simulator extensions

This paper represents an initial step toward scaling reinforcement learning for multi-agent planning in safety-critical, mixed human-autonomous settings.
