Should We Learn Contact-Rich Manipulation Policies from Sampling-Based Planners?

Topics include Motion planning, Robotics, Diffusion models, Sampling-based methods, Optimization, Planning, Learning, Sampling, Behavior cloning, Rapidly-exploring random tree.

The tremendous success of behavior cloning (BC) in robotic manipulation has been largely confined to tasks where demonstrations can be effectively collected through human teleoperation. However, demonstrations for contact-rich manipulation tasks that require complex coordination of multiple contacts are difficult to collect due to the limitations of current teleoperation interfaces. We investigate how to leverage model-based planning and optimization to generate training data for contact-rich dexterous manipulation tasks. Our analysis reveals that popular sampling-based planners like rapidly exploring random tree (RRT), while efficient for motion planning, produce demonstrations with unfavorably high entropy. This motivates modifications to our data generation pipeline that prioritizes demonstration consistency while maintaining solution diversity. Combined with a diffusion-based goal-conditioned BC approach, our method enables effective policy learning and zero-shot transfer to hardware for two challenging contact-rich manipulation tasks.

## Introduction

Many everyday manipulation tasks require coordinating multiple contacts with objects using different parts of the body, such as opening a bottle or carrying a large box. To endow robots with true autonomy, acquiring proficiency in these contact-rich dexterous manipulation skills is crucial. However, executing such skills demands intricate coordination between the hands, the arms, and even the whole body, which leads to a high-dimensional action space.

These limitations have motivated recent work in leveraging synthetic data generated through physics-based simulators. Such data can be produced through various approaches: reinforcement learning (RL), model-based trajectory optimization, or a combination of both. This teacher-student training paradigm, where a BC agent learns from an algorithmic expert, has shown success across domains including autonomous driving, legged locomotion, and dexterous manipulation. Given these successes, recent attention has turned to a critical question: how can we produce and curate high-quality data to improve student policy performance?

We show that using inconsistent, high-entropy demonstrations degrades policy performance when learning contact-rich manipulation skills through BC.

## Conclusion

In this work, we demonstrate that model-based motion planning offers a compelling alternative to human teleoperation for generating training data for contact-rich manipulation tasks. This approach eliminates the bottleneck of manual data collection while enabling the generation of demonstrations for complex tasks that are challenging to demonstrate through current teleoperation interfaces, such as those involving full-arm contacts and multi-finger coordination.

However, our analysis reveals an important nuance: the effectiveness of learning from planned demonstrations heavily depends on how we design the planning algorithm. While popular sampling-based planners like RRT excel at global planning, they can generate demonstrations with high action entropy that are difficult to learn , especially in low-data regimes. This insight motivates us to modify our data generation pipeline to prioritize demonstration consistency while maintaining adequate state space coverage and solution diversity.
