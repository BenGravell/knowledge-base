From Self-tuning Regulators to Reinforcement Learning and Back Again

Topics include Reinforcement learning, Robotics, Vehicles, Safety, Robustness, System identification, Distributed systems, Control, Learning.

Machine and reinforcement learning (RL) are increasingly being applied to plan and control the behavior of autonomous systems interacting with the physical world. Examples include self-driving vehicles, distributed sensor networks, and agile robots. However, when machine learning is to be applied in these new settings, the algorithms had better come with the same type of reliability, robustness, and safety bounds that are hallmarks of control theory, or failures could be catastrophic. Thus, as learning algorithms are increasingly and more aggressively deployed in safety critical settings, it is imperative that control theorists join the conversation. The goal of this tutorial paper is to provide a starting point for control theorists wishing to work on learning related problems, by covering recent advances bridging learning and control theory, and by placing these results within an appropriate historical context of system identification and adaptive control.

## Introduction & Motivation

With their recent successes in image classification, video game playing, sophisticated robotic simulations, and complex strategy games such as Go, machine and reinforcement learning (RL) are now being applied to plan and control the behavior of autonomous systems that interact with physical environments. Such systems, which include self-driving vehicles and agile robots, must interact with complex environments that are ever changing and difficult to model, strongly motivating the use of data-driven techniques.

To that end, it is important to recognize that while the applications areas and technical tools are new, the challenges faced -- uncertain and time varying systems and environments, unreliable sensing modalities, the need for robust stability and performance, etc. -- are not, and that many classical results from the system identification and adaptive control literature can be brought to bear on these problems.

In this tutorial paper and our companion paper, we highlight recent advances that provide non-asymptotic analysis of adaptive algorithms. Our aim is for these papers is for them to serve as a jumping off point for control theorists wanting to work in RL problems. In, we present an overview of tools and results on finite-data guarantees for system identification.

## Limitations of PAC-Bounds

As an algorithm that is $(\epsilon,\delta)$-PAC is only penalized for suboptimal behavior exceeding the $\epsilon$ threshold, there is no guarantee of convergence to an optimal policy. In fact, as pointed out in and illustrated in the LQR example above, many PAC algorithms cease learning once they are able to produce an $\epsilon$-suboptimal strategy.

## Limitations of Regret Bounds

As regret only tracks the integral of suboptimal behavior, it does not distinguish between a few severe mistakes and many small ones. In fact, shows that for Tabular MDP problems, an algorithm achieving optimal regret may still make infinitely many mistakes that are maximally suboptimal. Thus regret bounds cannot provide guarantees about transient worst-case deviations from the baseline cost $b_{T}$, which may have implications on guaranteeing the robustness or safety of an algorithm. We comment further on regret for discrete MDPs in the next section.
