GPUDrive: Data-driven, Multi-agent Driving Simulation at 1 Million FPS

Topics include Reinforcement learning, Multi-agent systems, Datasets, Optimization, Planning, Learning, GPUDrive.

Multi-agent learning algorithms have been successful at generating superhuman planning in various games but have had limited impact on the design of deployed multi-agent planners. A key bottleneck in applying these techniques to multi-agent planning is that they require billions of steps of experience. To enable the study of multi-agent planning at scale, we present GPUDrive. GPUDrive is a GPU-accelerated, multi-agent simulator built on top of the Madrona Game Engine capable of generating over a million simulation steps per second. Observation, reward, and dynamics functions are written directly in C++, allowing users to define complex, heterogeneous agent behaviors that are lowered to high-performance CUDA. Despite these low-level optimizations, GPUDrive is fully accessible through Python, offering a seamless and efficient workflow for multi-agent, closed-loop simulation. Using GPUDrive, we train reinforcement learning agents on the Waymo Open Motion Dataset, achieving efficient goal-reaching in minutes and scaling to thousands of scenarios in hours. We open-source the code and pre-trained agents at

## Introduction

Multi-agent learning has been impactful across a wide range of fully cooperative and zero-sum games (Cui et al. Wurman et al. Pérolat et al. Silver et al. Jaderberg et al. Bakhtin et al., ). However, its impact on multi-agent planning for settings that mix humans and robots has been muted. In contrast to the ubiquity of multi-agent learning-based agents in zero-sum games, multi-agent planners for most practical robotic systems are not derived from the output of game-theoretically sound learning algorithms....

Figure 1: Extremely fast multi-agent simulation with GPUDrive. Top: Bird’s-eye view of Waymo Open Motion Dataset scenarios in GPUDrive, with boxes marking controlled agents and circles denoting their goals. Bottom: Corresponding agent views, centered on one agent. Observations can be easily configured based on the user’s objectives. Here, agents are provided with a scene view through a relative coordinate frame. Shown are nearby road points within a configurable radius (set to 50 meters) and the relative positions of other agents in the scene.

## Ethics Statement

This paper presents GPUDrive, a GPU-accelerated simulator for multi-agent learning in autonomous driving. We use publicly available datasets, such as the Waymo Open Motion Dataset, which are anonymized to protect privacy. GPUDrive is intended for research purposes and not for real-world deployment without further validation. We recognize the risks of autonomous systems and emphasize the importance of safety and fairness in their application. Although this work does not involve human participants directly, it leverages real-world data that may reflect human behavior, and we strive to avoid harm or discrimination....

As GPUDrive is implemented in C++, we provide a Pythonic interface through nanobind. We create environments for both torch and jax that conform to the Gymnasium API so users can use the simulator entirely through Python if they prefer.

Figure 2: Example scenarios from the Waymo Open Motion Dataset rendered in GPUDrive. The blue boxes and circles indicate agents and their respective destinations.

where $A_{k}$ is the set of agents in the $k^{th}$ world, $S$ is the number of steps taken, and $\Delta T$ is the number of seconds elapsed....
