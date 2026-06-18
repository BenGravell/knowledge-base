Reinforcement Learning-Based Oscillation Dampening: Scaling up Single-Agent RL Algorithms to a 100 AV Highway Field Operational Test

Topics include Reinforcement learning, Autonomous vehicles, Traffic flow smoothing, Field operational test, Single-agent reinforcement learning, Control deployment, Highway traffic, Safety validation.

Documents the RL controller design and deployment path for a large automated-vehicle field test aimed at damping stop-and-go traffic oscillations. The paper is especially useful as an engineering account of moving from simulation and reward shaping to hardware constraints, safety considerations, and fleet-scale highway deployment.

In this article, we explore the technical details of the reinforcement learning (RL) algorithms that were deployed in the largest field test of automated vehicles designed to smooth traffic flow in history as of 2023, uncovering the challenges and breakthroughs that come with developing RL controllers for automated vehicles. We delve into the fundamental concepts behind RL algorithms and their application in the context of self-driving cars, discussing the developmental process from simulation to deployment in detail, from designing simulators to reward function shaping. We present the results in both simulation and deployment, discussing the flow-smoothing benefits of the RL controller. From understanding the basics of Markov decision processes to exploring advanced techniques such as deep RL, our article offers a comprehensive overview and deep dive of the theoretical foundations and practical implementations driving this rapidly evolving field. We also showcase real-world case studies and alternative research projects that highlight the impact of RL controllers in revolutionizing autonomous driving.

## Introduction

As the automotive industry continues to evolve, the quest for safer and more efficient self-driving cars has become a top priority. To achieve this, engineers and researchers are turning to state-of-the-art techniques like reinforcement learning to create intelligent control systems that can navigate complex environments with unprecedented precision and adaptability. Reinforcement learning (RL), a subfield of machine learning, offers a promising avenue for training automated vehicles to make optimal decisions and actions in real-time scenarios.

Together with the other articles presented in this special issue, this article constitutes an element of the technical work involved in bringing together objective of the CIRCLES project: the MegaVanderTest (MVT), the largest deployment of automated vehicles (AVs) designed to smooth traffic flow in history as of 2023. These AVs are partially automated and limited to longitudinal control. They do not communicate between each other, but communicate with a central server to get information about the downstream state of the highway.

Background material, including a short overview of reinforcement learning, human driver models, and policy gradient algorithms.

Problem formulation of the two classes of RL controllers designed for this experiment: Acceleration-based control and Adaptive Cruise Control (ACC)-based control.
