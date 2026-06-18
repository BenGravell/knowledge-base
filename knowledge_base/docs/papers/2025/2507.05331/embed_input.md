A Careful Examination of Large Behavior Models for Multitask Dexterous Manipulation

Topics include Imitation learning, Robotics, Robustness, Diffusion models, Foundation models, Control, Learning.

Robot manipulation has seen tremendous progress in recent years, with imitation learning policies enabling successful performance of dexterous and hard-to-model tasks. Concurrently, scaling data and model size has led to the development of capable language and vision foundation models, motivating large-scale efforts to create general-purpose robot foundation models. While these models have garnered significant enthusiasm and investment, meaningful evaluation of real-world performance remains a challenge, limiting both the pace of development and inhibiting a nuanced understanding of current capabilities. In this paper, we rigorously evaluate multitask robot manipulation policies, referred to as Large Behavior Models (LBMs), by extending the Diffusion Policy paradigm across a corpus of simulated and real-world robot data. We propose and validate an evaluation pipeline to rigorously analyze the capabilities of these models with statistical confidence. We compare against single-task baselines through blind, randomized trials in a controlled setting, using both simulation and real-world experiments....

## Introduction

Achieving flexible, generalist robots is a central ambition of robotics research. While modern robots are physically capable of performing a wide array of tasks in myriad settings, reliable autonomy has traditionally been limited to simple tasks or highly structured environments. Recently, visuomotor learning-based methods---trained to condition on robot sensor observations and produce low-level actions---have emerged as promising solutions to bridge this gap between hardware capabilities and autonomous performance....

Despite these strengths, single-task behavior-cloned policies remain brittle, exhibiting limited generalization to task variations or environments outside their training distributions. To overcome this brittleness, the field is increasingly adopting Large Behavior Models (LBMs) --visuomotor foundation models trained on large-scale multitask datasets containing action-level demonstrations. Inspired by the success of large-scale generalist models in Computer Vision and Natural Language Processing, these models seek to improve reliability through broad training data support and more robust learned visual and sensory representations....

We made a decision to run 50 real-world rollouts per task per policy per condition, and to further reduce the measurement uncertainty with hardware displays for reproducible initial conditions. The reproducible initial conditions did mean that each rollout took more time; we intend to continue to optimize the evaluation protocol to improve throughput. Additionally, despite these experimental protocols designed to minimize environment variability and human error, we expect that both initial condition and scoring mistakes are non-zero, likely adding to the noise of our measurements....

We also study LBMs with modestly-sized language encoders pretrained via CLIP. While we expect many of our findings will generalize to larger VLAs, we expect that some aspects like language steerability will differ in that setting.

### Binary Success/Failure Criteria

### Pretraining scaling laws

Table 2: Image Augmentation and Model Architecture Hyperparameters

To rigorously study the impact of multitask pretraining, we train multiple LBMs on approximately 1,700 hours of robot demonstrations comprised of over 500 internally collected high-diversity tasks as well as publicly available robot data....
