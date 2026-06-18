QuadSwarm: A Modular Multi-Quadrotor Simulator for Deep Reinforcement Learning with Direct Thrust Control

Topics include Reinforcement learning, Robotics, Aerial robotics, Robustness, Control, Learning, QuadSwarm, Simulation samples per second, SPS.

Reinforcement learning (RL) has shown promise in creating robust policies for robotics tasks. However, contemporary RL algorithms are data-hungry, often requiring billions of environment transitions to train successful policies. This necessitates the use of fast and highly-parallelizable simulators. In addition to speed, such simulators need to model the physics of the robots and their interaction with the environment to a level acceptable for transferring policies learned in simulation to reality. We present QuadSwarm, a fast, reliable simulator for research in single and multi-robot RL for quadrotors that addresses both issues. QuadSwarm, with fast forward-dynamics propagation decoupled from rendering, is designed to be highly parallelizable such that throughput scales linearly with additional compute. It provides multiple components tailored toward multi-robot RL, including diverse training scenarios, and provides domain randomization to facilitate the development and sim2real transfer of multi-quadrotor control policies.

## INTRODUCTION

Deep reinforcement learning (RL) has shown promise in developing agile control policies for quadrotors. However, RL algorithms require a large number of environment transitions to train successful policies in simulation. This motivates building fast and highly-parallelizable simulators. Additionally, it is important for the simulator to be good enough that policies trained on it transfer to the real world in spite of unmodeled environment dynamics and the simplified physics assumptions it will inevitably entail.

We describe a simulator, QuadSwarm, to facilitate research in single and multi-robot RL for quadrotors that addresses the aforementioned issues.

We evaluate the speed of QuadSwarm on a machine with AMD Ryzen 7 2700X CPU (16 CPU cores). QuadSwarm achieves $>$`<!-- -->`{=html}48,500 simulation samples per second (SPS) in an environment with a single quadrotor and $>$`<!-- -->`{=html}62,000 SPS in an environment with eight quadrotors, enabling collision simulation. In the environment with eight quadrotors, QuadSwarm receives eight samples per simulation step, which speeds up simulation even though additional computation is required for collision.

## II-A1 AirSim and Air Learning

AirSim is a photo-realistic simulator for multiple vehicles, such as cars or quadrotors. However, there are three main limitations of using AirSim in RL research. First, AirSim's physics simulation is coupled with rendering, which limits its simulation speed and parallelization ability. Second, although AirSim supports multiple quadrotors, the physical simulation of collisions is overly simplified. This makes AirSim unsuitable for control tasks. Third, AirSim does not provide OpenAI Gym interface for multiple quadrotors.
