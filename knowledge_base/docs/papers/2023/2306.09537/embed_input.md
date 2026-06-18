QuadSwarm: A Modular Multi-Quadrotor Simulator for Deep Reinforcement Learning with Direct Thrust Control

Topics include Reinforcement learning, Robotics, Aerial robotics, Robustness, Control, Learning, QuadSwarm, Simulation samples per second, SPS.

Reinforcement learning (RL) has shown promise in creating robust policies for robotics tasks. However, contemporary RL algorithms are data-hungry, often requiring billions of environment transitions to train successful policies. This necessitates the use of fast and highly-parallelizable simulators. In addition to speed, such simulators need to model the physics of the robots and their interaction with the environment to a level acceptable for transferring policies learned in simulation to reality. We present QuadSwarm, a fast, reliable simulator for research in single and multi-robot RL for quadrotors that addresses both issues. QuadSwarm, with fast forward-dynamics propagation decoupled from rendering, is designed to be highly parallelizable such that throughput scales linearly with additional compute. It provides multiple components tailored toward multi-robot RL, including diverse training scenarios, and provides domain randomization to facilitate the development and sim2real transfer of multi-quadrotor control policies....

## INTRODUCTION

Deep reinforcement learning (RL) has shown promise in developing agile control policies for quadrotors. However, RL algorithms require a large number of environment transitions to train successful policies in simulation. This motivates building fast and highly-parallelizable simulators. Additionally, it is important for the simulator to be good enough that policies trained on it transfer to the real world in spite of unmodeled environment dynamics and the simplified physics assumptions it will inevitably entail.

We describe a simulator, QuadSwarm, to facilitate research in single and multi-robot RL for quadrotors that addresses the aforementioned issues. Specifically, QuadSwarm supports five main ingredients required to enable the development of RL control policies for real quadrotors: $(i)$ A reasonably accurate physics model of a popular existing hardware platform, Crazyflie 2.x, and sufficient domain randomization to account for unmodeled effects; $({ii})$ Supports per-rotor thrust control; $({iii})$ Fast single-threaded throughput, highly parallelizable, and scales with additional compute; $({iv})$ A diverse collection of learning scenarios...

## Conclusions

We describe QuadSwarm, a simulator for Deep RL research on single and multi-quadrotor control policies and their sim2real transfer to real hardware. We demonstrate how QuadSwarm integrates five key ingredients: $(i)$ a reasonable physics model of Crazyflie 2.x, with domain randomization to account for unmodeled effects; $({ii})$ per-rotor thrust control; $({iii})$ fast, high parallelization, and scaling with additional compute; $({iv})$ a diverse collection of learning scenarios for single and multi-quadrotor teams; $(v)$ 100$\%$ written in Python....

We consider two situations of quadrotor interaction with the ground. When the quadrotor hits the ground we set the linear velocity, angular velocity, and acceleration to zero, regenerate the rotation matrix by setting the normal vector of the quadrotor upward, and reset all momenta. When the quadrotor is on the floor, and the thrust is not enough to allow the quadrotor to take off, we arrest motion on the floor with sufficiently high friction....

At timestep $t$, given actions $a^{(t)}$ from a policy sampled from an unconstrained Gaussian distribution, we constrain the actions to be in the range and use this to construct the...
