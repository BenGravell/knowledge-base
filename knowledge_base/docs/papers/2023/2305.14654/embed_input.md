Barkour: Benchmarking Animal-level Agility with Quadruped Robots

Animals have evolved various agile locomotion strategies, such as sprinting, leaping, and jumping. There is a growing interest in developing legged robots that move like their biological counterparts and show various agile skills to navigate complex environments quickly. Despite the interest, the field lacks systematic benchmarks to measure the performance of control policies and hardware in agility. We introduce the Barkour benchmark, an obstacle course to quantify agility for legged robots. Inspired by dog agility competitions, it consists of diverse obstacles and a time based scoring mechanism. This encourages researchers to develop controllers that not only move fast, but do so in a controllable and versatile way. To set strong baselines, we present two methods for tackling the benchmark. In the first approach, we train specialist locomotion skills using on-policy reinforcement learning methods and combine them with a high-level navigation controller....

## Introduction

Figure 1: Barkour benchmark overview and example behavior.

There has been a proliferation of legged robot development inspired by animal mobility. Recent notable examples include the ETH ANYmal, the MIT Mini Cheetah, the KAIST RaiBo, Unitree A1/Go1, and the Boston Dynamics Spot robots. An important research question in this field is how to develop a controller that enables legged robots to exhibit animal-level agility while also being able to generalize across various obstacles and terrains. Through the exploration of both learning and traditional control-based methods, there has been significant progress in enabling robots to walk across a wide range of terrains....

One limitation of the current proposed baseline methods is that we use privileged information such as the CAD model of the environment and the position of the robot (via a Motion-Capture system) in the world frame. An important future work direction is to explore Barkour using only on-board sensors for both low-level locomotion skills and high-level navigation controller.

An equally exciting direction for future research on Barkour is to evaluate the impact of modifications to robot hardware, different form-factors, and sensors on performance or training speed. Finally, we are also looking into evaluating Barkour in an interactive setting, closer to real-world dog agility competitions, with a human leading a robot through the course.

Exploring the influence of the Barkour benchmark on enhancing the agility of quadruped robots necessitates considerable controller development and thorough real hardware experimentation. This poses significant challenges on the reliability and repeatability of the robot hardware, especially given the highly agile movements we strive for. Moreover, quadruped animals exhibit diverse body configurations compared to typical quadruped robots, which can significantly affect their capacity for agile motion....

OWP takes all three categories of observations as input and is trained with randomly sampled velocity commands. The training environment for OWP follows the general uneven terrain curriculum designed by Rudin et al, which consists of mild slopes, stairs, and random steps. Please refer to Appendix -E for details of the observation space, the velocity sampling, and the reward structure.
