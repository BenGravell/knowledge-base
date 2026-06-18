PLUTO: Pushing the Limit of Imitation Learning-based Planning for Autonomous Driving

We present PLUTO, a powerful framework that pushes the limit of imitation learning-based planning for autonomous driving. Our improvements stem from three pivotal aspects: a longitudinal-lateral aware model architecture that enables flexible and diverse driving behaviors; An innovative auxiliary loss computation method that is broadly applicable and efficient for batch-wise calculation; A novel training framework that leverages contrastive learning, augmented by a suite of new data augmentations to regulate driving behaviors and facilitate the understanding of underlying interactions. We assessed our framework using the large-scale real-world nuPlan dataset and its associated standardized planning benchmark. Impressively, PLUTO achieves state-of-the-art closed-loop performance, beating other competing learning-based methods and surpassing the current top-performed rule-based planner for the first time. Results and code are available at

## Introduction

Learning-based planning has emerged as a potentially scalable approach for autonomous driving, attracting significant research interest. Imitation-based planning, in particular, has demonstrated noteworthy success in simulations and real-world applications. Yet, the efficacy of learning-based planning remains unsatisfactory. As indicated, conventional rule-based planning outperforms all learning-based alternatives, winning the 2023 nuPlan planning challenge.

The first challenge lies in acquiring multi-modal driving behaviors. It is observed that while learning-based planners are good at learning longitudinal tasks such as lane following, they struggle with lateral tasks, for instance, executing lane changes or navigating around obstacles, even when space permits. We attribute this deficiency to the absence of explicit lateral behavior modeling within the architectural design of the model.

We introduce a query-based model architecture that simultaneously addresses lateral and longitudinal planning maneuvers, enabling flexible and diverse driving behaviors.

We propose a novel method for calculating auxiliary loss based on differential interpolation. This method is applicable to a broad spectrum of auxiliary tasks and allows for efficient batch-wise computation in vector-based models.

## Conclusion

In this study, we introduce Pluto, a pioneering data-driven planning framework that extends the capabilities of imitation learning within the autonomous driving domain. We propose innovative solutions concerning model architecture, data augmentation, and the learning framework, effectively addressing enduring challenges in imitation learning. The query-based model architecture furnishes the planner with the capacity for adaptable driving behaviors across both longitudinal and lateral dimensions.

## Limitations and Future Work

. In our approach, we predict a single trajectory for each dynamic agent. This methodology yields satisfactory outcomes in practical applications; nevertheless, the generation of meaningful joint multimodal predictions and their efficient incorporation into planning strategies represent significant areas for future research. The addition of a post-processing module has been demonstrated to improve overall performance effectively. However, it cannot handle scenarios where all generated trajectories are unusable.
