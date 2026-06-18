PLUTO: Pushing the Limit of Imitation Learning-based Planning for Autonomous Driving

We present PLUTO, a powerful framework that pushes the limit of imitation learning-based planning for autonomous driving. Our improvements stem from three pivotal aspects: a longitudinal-lateral aware model architecture that enables flexible and diverse driving behaviors; An innovative auxiliary loss computation method that is broadly applicable and efficient for batch-wise calculation; A novel training framework that leverages contrastive learning, augmented by a suite of new data augmentations to regulate driving behaviors and facilitate the understanding of underlying interactions. We assessed our framework using the large-scale real-world nuPlan dataset and its associated standardized planning benchmark. Impressively, PLUTO achieves state-of-the-art closed-loop performance, beating other competing learning-based methods and surpassing the current top-performed rule-based planner for the first time. Results and code are available at

## Introduction

Learning-based planning has emerged as a potentially scalable approach for autonomous driving, attracting significant research interest \[\]. Imitation-based planning, in particular, has demonstrated noteworthy success in simulations and real-world applications. Yet, the efficacy of learning-based planning remains unsatisfactory. As indicated in \[\], conventional rule-based planning outperforms all learning-based alternatives, winning the 2023 nuPlan planning challenge....

The first challenge lies in acquiring multi-modal driving behaviors. It is observed that while learning-based planners are good at learning longitudinal tasks such as lane following, they struggle with lateral tasks \[\], for instance, executing lane changes or navigating around obstacles, even when space permits. We attribute this deficiency to the absence of explicit lateral behavior modeling within the architectural design of the model....

### Limitations and Future Work

. In our approach, we predict a single trajectory for each dynamic agent. This methodology yields satisfactory outcomes in practical applications; nevertheless, the generation of meaningful joint multimodal predictions and their efficient incorporation into planning strategies represent significant areas for future research. The addition of a post-processing module has been demonstrated to improve overall performance effectively. However, it cannot handle scenarios where all generated trajectories are unusable....

Interactive Agent Dropout $\in \mathcal{T}^{-}$: excludes agents that have direct or indirect interactions with the AV. Identification of interactive agents follows the methodology outlined in Non-interactive Agents Dropout. This function aims to train the model on less intuitive interactions within complex scenarios, such as unprotected left turns and lane changes.

Firstly, this provides dense supervision which benefits the training. Secondly, the generated predictions play a crucial role in eliminating unsuitable planning proposals during the post-processing stage, as detailed in Section III-F. Denote agent's ground truth trajectory as ${\mathbf{P}}_{1:N_{A}}^{gt}$, the prediction loss is

In this study, we conduct a comparative analysis between Pluto and both existing and state-of-the-art (SOTA) methodologies utilizing the nuPlan benchmark to demonstrate the efficacy of our...
