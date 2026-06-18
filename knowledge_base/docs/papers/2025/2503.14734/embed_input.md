GR00T N1: An Open Foundation Model for Generalist Humanoid Robots

Topics include Imitation learning, Robotics, Robustness, Transformers, Diffusion models, Foundation models, Vision-language models, Datasets, Benchmarks, Learning, GR00T N1, Vision-language-action model, Humanoid robot.

General-purpose robots need a versatile body and an intelligent mind. Recent advancements in humanoid robots have shown great promise as a hardware platform for building generalist autonomy in the human world. A robot foundation model, trained on massive and diverse data sources, is essential for enabling the robots to reason about novel situations, robustly handle real-world variability, and rapidly learn new tasks. To this end, we introduce GR00T N1, an open foundation model for humanoid robots. GR00T N1 is a Vision-Language-Action (VLA) model with a dual-system architecture. The vision-language module (System 2) interprets the environment through vision and language instructions. The subsequent diffusion transformer module (System 1) generates fluid motor actions in real time. Both modules are tightly coupled and jointly trained end-to-end. We train GR00T N1 with a heterogeneous mixture of real-robot trajectories, human videos, and synthetically generated datasets. We show that our generalist robot model GR00T N1 outperforms the state-of-the-art imitation learning baselines on standard simulation benchmarks across multiple robot embodiments....

## Introduction

Creating autonomous robots to perform everyday tasks in the human world has long been a fascinating goal and, at the same time, a significant technical undertaking. Recent progress in robotic hardware, artificial intelligence, and accelerated computing has collectively paved the ground for developing general-purpose robot autonomy. To march toward human-level physical intelligence, we advocate for a full-stack solution that integrates the three key ingredients: hardware, models, and data. First and foremost, robots are embodied physical agents, and their hardware determines their capability envelope....

In recent years, foundation models have brought forth dramatic breakthroughs in understanding and generating visual and text data. They demonstrate the effectiveness of training generalist models on web-scale data to enable strong generalization and fast adaptation to downstream tasks. The successes of foundation models in neighboring fields of AI have depicted a promising roadmap for building the "backbone" of intelligence for generalist robots, endowing them with a set of core competencies and enabling them to rapidly learn and adapt in the real world....

## Conclusions

We have presented GR00T N1, an open foundation model for generalist humanoid robots. GR00T N1 features a dual-system model design, leverages heterogeneous training data, and supports multiple robot embodiments. We systematically evaluate it as a generalist policy across simulation benchmarks and on the real GR-1 humanoid robot. Our experiments demonstrate its strong generalization capabilities, enabling robots to learn diverse manipulation skills with high data efficiency....

### Neural Trajectories

### Post-training

Figure 8: Real-World Tasks. All images are captured from policy rollouts of GR00T-N1-2B and models post-trained from GR00T-N1-2B. (Top) Pre-training evaluations. We design two manipulation tasks to assess our pretrained models. The left image shows a left-to-right handover, while the right image illustrates the placement of novel objects into an unseen target container. (Bottom) Post-training evaluations. We introduce four distinct task categories. From top to bottom, we present examples of object-to-container pick-and-place, articulated object manipulation, industrial object manipulation, and multi-agent coordination.
