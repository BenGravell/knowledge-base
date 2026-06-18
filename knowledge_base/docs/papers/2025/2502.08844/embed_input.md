MuJoCo Playground

Topics include Robotics, Learning, MuJoCo playground.

We introduce MuJoCo Playground, a fully open-source framework for robot learning built with MJX, with the express goal of streamlining simulation, training, and sim-to-real transfer onto robots. With a simple "pip install playground", researchers can train policies in minutes on a single GPU. Playground supports diverse robotic platforms, including quadrupeds, humanoids, dexterous hands, and robotic arms, enabling zero-shot sim-to-real transfer from both state and pixel inputs. This is achieved through an integrated stack comprising a physics engine, batch renderer, and training environments. Along with video results, the entire framework is freely available at playground.mujoco.org

## Introduction

Reinforcement learning (RL) \[\] with subsequent transfer to hardware (sim-to-real) \[\], is emerging as a leading paradigm in modern robotics. The benefits of simulation are obvious -- safety and cheap data. The recipe involves four steps:

Create a simulated environment that matches the real world.

## Conclusion

MuJoCo Playground is a library built upon the open-source MuJoCo simulator and Madrona batch renderer with implementations across several reinforcement learning and robotics environments. We demonstrate policy training on various GPU topologies using JAX and pytorch-based reinforcement learning libraries. We also demonstrate sim-to-real deployment on several robotic tasks and embodiments, from locomotion to both dexterous and non-prehensile manipulation from proprioceptive state and from pixels. We look forward to seeing the community put this resource to use in advancing robotics research and its applications.

### Results

### IV-B1 Quadruped Locomotion

The policy receives estimates of the block's position and orientation from an open-source camera tracker \[\]. We use direct high-frequency torque control at 200 Hz, where the RL policy outputs motor torques for the arm's seven joints (with the gripper closed). By learning to control torques rather than joint positions, the agent develops smooth, compliant behavior that transfers effectively to hardware, delivering superior performance even when direct torque control at high frequencies poses learning challenges \[\]. This recipe, therefore, holds broad value for practitioners.

Encode desired robot behavior with a reward function.

The key enabler of this approach is a simulator that is realistic, convenient, and fast.

The realism requirement is self-evident, the "digital twin" of step 1 demands a minimal level of fidelity \[\]. Convenience and usability are equally critical, streamlining the creation, modification, composition, and characterization (system identification) of simulated robots.

The importance of speed is less obvious -- why does it matter if training takes ten minutes or ten hours? The answer lies in reward design (step 2), which cannot be easily automated: what the robot *ought* to do is an expression of human preference....
