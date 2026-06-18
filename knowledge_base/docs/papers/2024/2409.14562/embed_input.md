DROP: Dexterous Reorientation via Online Planning

Topics include Reinforcement learning, Predictive control, Robotics, Robustness, Real-time systems, Online algorithms, Offline algorithms, Sampling-based methods, Planning, Control, Learning, Sampling, DROP.

Achieving human-like dexterity is a longstanding challenge in robotics, in part due to the complexity of planning and control for contact-rich systems. In reinforcement learning (RL), one popular approach has been to use massively-parallelized, domain-randomized simulations to learn a policy offline over a vast array of contact conditions, allowing robust sim-to-real transfer. Inspired by recent advances in real-time parallel simulation, this work considers instead the viability of online planning methods for contact-rich manipulation by studying the well-known in-hand cube reorientation task. We propose a simple architecture that employs a sampling-based predictive controller and vision-based pose estimator to search for contact-rich control actions online. We conduct thorough experiments to assess the real-world performance of our method, architectural design choices, and key factors for robustness, demonstrating that our simple sampling-based approach achieves performance comparable to prior RL-based works. Supplemental material:

## Introduction

Achieving dexterity comparable to human hands has been a longstanding challenge in robotics. While even simple robots can produce dynamic, contact-rich behavior, general methods for doing so are still scarce. For contact-rich tasks, reinforcement learning (RL) has been the dominant paradigm due to its ability to generate real-world robust plans. One well-studied task is in-hand cube reorientation, where a hand must rotate a cube to match consecutive goal orientations....

Figure 1: The DROP architecture. DROP consists of (i) a vision-based cube pose estimator (composed of the Keypoint Predictor, Smoother, and Corrector), and (ii) a sampling-based planner that selects control actions by conducting model-based rollouts and iteratively improving the sampling distribution online based on the costs J(i).

Enhanced, data-driven search. As noted in our ablations, finding good plans via search demands many threads; indeed, our work relies on a server-grade CPU, since dynamics simulation is about an order of magnitude slower on GPUs. Thus, improving efficiency is key for better performance. Promising directions include sampling from imitation-learned policies \[\], learning value functions for rollout evaluation \[\], and exploring alternate spline parameterizations \[\] or action spaces \[\]. Searching for high-level commands for a lower-level RL policy could perhaps yield systems with both the flexibility of search and robustness of RL.

DROP opens many paths for contact-rich manipulation. It is our hope that algorithms like DROP can generalize to more real-world tasks than cube reorientation, unlocking tool use, enhanced human-robot collaboration, and more.

Figure 3: Examples of rotations. CEM can discover many contact-rich plans for cube reorientation. The red arrows show where forces are primarily applied to achieve rotations. (A) The middle finger pushes down on a cube edge while the base of the thumb lifts the opposite corner, rotating the Q face up. (B) The ring finger and base of the index finger push on opposite corners to rotate the T face up. (C) The thumb pulls down on the W face while the base of the ring finger pushes on the opposite corner to rotate the Y face up....

Mathematically, the DROP cube reorientation problem is expressed as the optimal control problem

### IV-B Main Hardware Results
