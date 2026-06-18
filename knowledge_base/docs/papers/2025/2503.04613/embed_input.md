Whole-Body Model-Predictive Control of Legged Robots with MuJoCo

Topics include Predictive control, Robotics, Real-time systems, Online algorithms, Control, Model predictive control, Humanoid robot.

We demonstrate the surprising real-world effectiveness of a very simple approach to whole-body model-predictive control (MPC) of quadruped and humanoid robots: the iterative LQR (iLQR) algorithm with MuJoCo dynamics and finite-difference approximated derivatives. Building upon the previous success of model-based behavior synthesis and control of locomotion and manipulation tasks with MuJoCo in simulation, we show that these policies can easily generalize to the real world with few sim-to-real considerations. Our baseline method achieves real-time whole-body MPC on a variety of hardware experiments, including dynamic quadruped locomotion, quadruped walking on two legs, and full-sized humanoid bipedal locomotion. We hope this easy-to-reproduce hardware baseline lowers the barrier to entry for real-world whole-body MPC research and contributes to accelerating research velocity in the community.

## Introduction

Enabling legged robots to achieve human and animal-level agility has been a decades-long challenge for robotics researchers. In addition to the challenges faced by other non-legged mobile robots (e.g., drones, autonomous vehicles, etc.), legged systems are generally high-dimensional and must effectively reason about making and breaking contact with the world. Advancements in model-based control and reinforcement learning (RL) methods have unlocked tremendous in-the-wild legged robot capabilities over the last $10$-$15$ years.

This paper aims to reduce this gap by providing an open-sourced baseline MPC algorithm and real-world legged robot implementation built on the MuJoCo physics engine, a standard, easy-to-use open-source robotics simulator. We show that a standard gradient-based MPC algorithm, in particular the iterative LQR (iLQR) algorithm, based on MuJoCo is surprisingly capable of solving a variety of challenging *real-world* tasks such as bipedal locomotion on a quadruped and full-sized humanoid robot in *real time*.

Our

A simple-yet-surprisingly-effective baseline whole-body predictive control algorithm for real-world legged robot locomotion.

The remainder of this paper is organized as follows: We begin by reviewing relevant literature on iLQR, whole-body MPC, and open-source efforts for model-based control in Sec. II. Next, we briefly introduce the MuJoCo contact model and iLQR in Sec. III, followed by key considerations and implementation details for transferring iLQR policies to hardware in IV. Then, we cover the hardware setup and experimental results in Sec. V. Finally, we conclude in Sec. VI by discussing current limitations of our system and directions for future work.
