Physics-Driven Data Generation for Contact-Rich Manipulation via Trajectory Optimization

Topics include Trajectory optimization, Robotics, Diffusion models, Datasets, Optimization, Planning.

We present a low-cost data generation pipeline that integrates physics-based simulation, human demonstrations, and model-based planning to efficiently generate large-scale, high-quality datasets for contact-rich robotic manipulation tasks. Starting with a small number of embodiment-flexible human demonstrations collected in a virtual reality simulation environment, the pipeline refines these demonstrations using optimization-based kinematic retargeting and trajectory optimization to adapt them across various robot embodiments and physical parameters. This process yields a diverse, physically consistent dataset that enables cross-embodiment data transfer, and offers the potential to reuse legacy datasets collected under different hardware configurations or physical parameters. We validate the pipeline's effectiveness by training diffusion policies from the generated datasets for challenging contact-rich manipulation tasks across multiple robot embodiments, including a floating Allegro hand and bimanual robot arms. The trained policies are deployed zero-shot on hardware for bimanual iiwa arms, achieving high success rates with minimal human input. Project website:

## Introduction

The emergence of foundation models has transformed fields such as natural language processing and computer vision, where models trained on massive, internet-scale datasets demonstrate remarkable generalization across diverse reasoning tasks. Motivated by this success, the robotics community is currently pursuing foundation models for generalist robot policies capable of flexible and robust decision-making across a wide range of tasks, leading to significant industrial investments in large-scale robot learning \[\]....

To address data scarcity, robot learning researchers often rely on a spectrum of data sources varying in cost, quality, and transferability. The most informative data typically consists of high-quality demonstrations specific to the task, environment, and embodiment, but such data is costly and time-consuming to collect, as it requires human teleoperation with specialized hardware. At the opposite end of the spectrum, there is a wealth of lower-quality data in the form of internet videos showing humans and robots performing manipulation tasks....

## Conclusion

In this work, we present a novel, cost-effective pipeline that combines physics-based simulations, human demonstrations, and model-based planning to address data scarcity in contact-rich robotic manipulation tasks. A key insight of our approach is that human demonstrations---even when collected on a different morphology---offer valuable global task information that model-based planners often struggle to discover independently due to the high-dimensional search space and complex contact dynamics....

The kinematically consistent robot trajectories ${}_{0:T}^{}$ are generally not dynamically feasible due to the embodiment gap and differences in physical parameters. However, they can provide good guidance on generating dynamically feasible trajectories with complex multi-contact interactions. In particular, human demonstrations provide global information about when and where to make contact with the object, which model-based planning can then locally refine....

Figure 1: VR-based human-hand demonstration framework.

Figure 4: Distribution and snapshots of trajectories generated from a single demonstration. (a) The original demonstration (orange) is locally perturbed and augmented to about 100 dynamically feasible contact-rich trajectories (blue) for each system....
