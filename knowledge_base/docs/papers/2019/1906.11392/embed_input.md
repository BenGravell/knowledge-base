From Self-tuning Regulators to Reinforcement Learning and Back Again

Topics include Reinforcement learning, Robotics, Vehicles, Safety, Robustness, System identification, Distributed systems, Control, Learning.

Machine and reinforcement learning (RL) are increasingly being applied to plan and control the behavior of autonomous systems interacting with the physical world. Examples include self-driving vehicles, distributed sensor networks, and agile robots. However, when machine learning is to be applied in these new settings, the algorithms had better come with the same type of reliability, robustness, and safety bounds that are hallmarks of control theory, or failures could be catastrophic. Thus, as learning algorithms are increasingly and more aggressively deployed in safety critical settings, it is imperative that control theorists join the conversation. The goal of this tutorial paper is to provide a starting point for control theorists wishing to work on learning related problems, by covering recent advances bridging learning and control theory, and by placing these results within an appropriate historical context of system identification and adaptive control.

## Introduction & Motivation

With their recent successes in image classification, video game playing, sophisticated robotic simulations, and complex strategy games such as Go, machine and reinforcement learning (RL) are now being applied to plan and control the behavior of autonomous systems that interact with physical environments. Such systems, which include self-driving vehicles and agile robots, must interact with complex environments that are ever changing and difficult to model, strongly motivating the use of data-driven techniques....

To that end, it is important to recognize that while the applications areas and technical tools are new, the challenges faced -- uncertain and time varying systems and environments, unreliable sensing modalities, the need for robust stability and performance, etc. -- are not, and that many classical results from the system identification and adaptive control literature can be brought to bear on these problems....

## Conclusions

This tutorial paper and our companion paper presented a broad overview of recent progress towards the finite-time analysis for reinforcement learning and self-tuning control methods. We have attempted to provide a summary of representative results in this space that establish connections between the self-tuning control literature and methods recently proposed in reinforcement learning. The former are typically model-based, and are well-studied from a theoretical perspective, although more effort is still needed to better understand their finite-time behavior....

### IV-A3 Structured MDPs

The study of regret bounds for LQR was initiated in. Here we summarize a recent treatment of the problem, as provided in. There, the authors study the performance of CE control for LQR, and study a regret measure of the form

Let the controller $\mathbf{K}$ stabilize $(\hat{A},\hat{B})$ and $(\mathbf{\Phi}_{x},\mathbf{\Phi}_{u})$ be its corresponding system response (27 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")) on system $(\hat{A},\hat{B})$. Then if $\mathbf{K}$ stabilizes $(A,B)$, it achieves the following LQR cost $J{(A,B,\mathbf{K})}$ defined as

Indeed, at a cursory glance, classical self-tuning regulators have the same objective as contemporary RL: an initial control policy and/or model is posited, data is collected, and a refined...
