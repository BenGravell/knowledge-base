EVORA: Deep Evidential Traversability Learning for Risk-Aware Off-Road Autonomy

Topics include Robotics, Uncertainty, Deep learning, Accuracy, Learning, EVORA, Uncertainty quantification.

Traversing terrain with good traction is crucial for achieving fast off-road navigation. Instead of manually designing costs based on terrain features, existing methods learn terrain properties directly from data via self-supervision to automatically penalize trajectories moving through undesirable terrain, but challenges remain to properly quantify and mitigate the risk due to uncertainty in learned models. To this end, this work proposes a unified framework to learn uncertainty-aware traction model and plan risk-aware trajectories. For uncertainty quantification, we efficiently model both aleatoric and epistemic uncertainty by learning discrete traction distributions and probability densities of the traction predictor's latent features. Leveraging evidential deep learning, we parameterize Dirichlet distributions with the network outputs and propose a novel uncertainty-aware squared Earth Mover's distance loss with a closed-form expression that improves learning accuracy and navigation performance.

## Introduction

Autonomous robots are increasingly being deployed in harsh off-road environments like mines, forests, and deserts, where both geometric and semantic understanding of the environments is required to identify non-geometric hazards (e.g., mud puddles, slippery surfaces) and geometric non-hazards (e.g., tall grass and foliage) \\editin order to achieve reliable navigation. To this end, recent approaches manually assign navigation costs based on semantic classification of the terrain, requiring significant human expertise to label and train a classifier sufficiently accurate and rich in order to achieve desired risk-aware behaviors.

To achieve fast and reliable off-road navigation, this work considers both the upstream uncertainty-aware traversability learning problem and the downstream risk-aware navigation problem. Recognizing the inter-dependence of the two problems, our proposed pipeline, EVORA (EVidential Off-Road Autonomy), tightly integrates the proposed uncertainty-aware traversability model into the the proposed risk-aware planner.

## I-A1 \\editTraversability Analysis

Suitability of terrain for navigation can be assessed in various ways, e.g., based on proprioceptive measurements, geometric features and combinations of geometric and semantic features. Due to the difficulty of hand-crafting planning costs based on terrain features, self-supervised learning is increasingly being adopted to learn task-relevant traversability representations. For example, \\editLi et al. proposed to learn the support surfaces underneath dense vegetation for legged robot locomotion, and \\editGasparino et al. modeled terrain traction that captures how well the robot can follow the desired velocities.

## Conclusion

This work proposed EVORA, a unified framework for uncertainty-aware traversability learning based on evidential deep learning and risk-aware planning based on CVaR. EVORA models uncertain terrain traction via empirical distributions (aleatoric uncertainty) and identifies OOD terrain based on densities of traction predictor's latent features (epistemic uncertainty). By leveraging the proposed uncertainty-aware squared Earth Mover's Distance loss, we improved the network's prediction accuracy, OOD detection performance, and the downstream navigation performance.
