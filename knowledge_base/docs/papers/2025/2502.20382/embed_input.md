Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization

Topics include Trajectory optimization, Robotics, Diffusion models, Datasets, Optimization, Planning.

We present a low-cost data generation pipeline that integrates physics-based simulation, human demonstrations, and model-based planning to efficiently generate large-scale, high-quality datasets for contact-rich robotic manipulation tasks. Starting with a small number of embodiment-flexible human demonstrations collected in a virtual reality simulation environment, the pipeline refines these demonstrations using optimization-based kinematic retargeting and trajectory optimization to adapt them across various robot embodiments and physical parameters. This process yields a diverse, physically consistent dataset that enables cross-embodiment data transfer, and offers the potential to reuse legacy datasets collected under different hardware configurations or physical parameters. We validate the pipeline's effectiveness by training diffusion policies from the generated datasets for challenging contact-rich manipulation tasks across multiple robot embodiments, including a floating Allegro hand and bimanual robot arms. The trained policies are deployed zero-shot on hardware for bimanual iiwa arms, achieving high success rates with minimal human input.

## Introduction

The emergence of foundation models has transformed fields such as natural language processing and computer vision, where models trained on massive, internet-scale datasets demonstrate remarkable generalization across diverse reasoning tasks. Motivated by this success, the robotics community is currently pursuing foundation models for generalist robot policies capable of flexible and robust decision-making across a wide range of tasks, leading to significant industrial investments in large-scale robot learning.

In this work, we propose a data generation framework that leverages the strengths of both approaches: human demonstrations can provide global guidance, while trajectory optimization can locally refine these demonstrations to ensure dynamic feasibility. Starting with a small number of human demonstrations collected in a virtual reality (VR) environment, our method uses model-based trajectory optimization to generate large datasets of dynamically feasible, contact-rich trajectories in simulation.

We present an intuitive, embodiment-flexible demonstration interface based on virtual reality and physics simulation, enabling fast data collection for dexterous contact-rich manipulation.

## Limitations and Future Work

While our method efficiently generates abundant contact-rich trajectories, several limitations remain. First, although our human-hand demonstration framework is fast and intuitive, it may not fully exploit the kinematic capabilities of the target robot, such as continuous joint rotation or specialized dexterous maneuvers. Future work could explore the application of our automated data generation framework to embodiment-aware legacy datasets, better capturing the unique motion capabilities of different robotic systems.

Second, although our method demonstrates strong performance in the vicinity of the demonstration due to trajectory optimization, the learned policies struggle to recover from states far outside the demonstrated regions, such as those resulting from catastrophic failure. Future work could explore more advanced planning techniques to iteratively improve the learned policies' robustness in unvisited regions of the state space.
