DROP: Dexterous Reorientation via Online Planning

Topics include Reinforcement learning, Predictive control, Robotics, Robustness, Real-time systems, Online algorithms, Offline algorithms, Sampling-based methods, Planning, Control, Learning, Sampling, DROP.

Achieving human-like dexterity is a longstanding challenge in robotics, in part due to the complexity of planning and control for contact-rich systems. In reinforcement learning (RL), one popular approach has been to use massively-parallelized, domain-randomized simulations to learn a policy offline over a vast array of contact conditions, allowing robust sim-to-real transfer. Inspired by recent advances in real-time parallel simulation, this work considers instead the viability of online planning methods for contact-rich manipulation by studying the well-known in-hand cube reorientation task. We propose a simple architecture that employs a sampling-based predictive controller and vision-based pose estimator to search for contact-rich control actions online. We conduct thorough experiments to assess the real-world performance of our method, architectural design choices, and key factors for robustness, demonstrating that our simple sampling-based approach achieves performance comparable to prior RL-based works.

## Introduction

Achieving dexterity comparable to human hands has been a longstanding challenge in robotics. While even simple robots can produce dynamic, contact-rich behavior, general methods for doing so are still scarce. For contact-rich tasks, reinforcement learning (RL) has been the dominant paradigm due to its ability to generate real-world robust plans. One well-studied task is in-hand cube reorientation, where a hand must rotate a cube to match consecutive goal orientations.

Leveraging recent advances in real-time parallel simulation (e.g., MJPC), we instead study the online approach of sampling-based predictive control (SPC) methods for in-hand manipulation, which continuously replan by simulating parallel rollouts and applying optimal control actions over short time horizons. In contrast with RL, such online planning methods can adjust the task or model without re-training, but may demand expensive online computation. While tools like MJPC have made SPC feasible for many simulated contact-rich tasks, their real-world utility remains largely unproven.

Our main contribution is DROP (Dexterous Reorientation via Online Planning), a system architecture that consists of (i) a simple sampling-based planner and (ii) a vision-based state estimator comprising a keypoint detection model, a pose smoother, and a collision-aware state corrector. Our aim is not to design the best cube reorientation policy, but to test the viability of sampling-based strategies by thoroughly assessing DROP's real-world performance, architectural design, and key factors for robustness.

## Conclusion and Future Directions

This work presents DROP, a minimalist online planning method for in-hand manipulation via sampling-based predictive control that achieves robust cube rotations in hardware. While promising, there are many avenues for future research.

Better planners. While we found that vanilla CEM already achieved impressive results, many more sophisticated algorithms exist, such as CMA-ES, MPPI, etc.
