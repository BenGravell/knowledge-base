EVORA: Deep Evidential Traversability Learning for Risk-Aware Off-Road Autonomy

Topics include Robotics, Uncertainty, Deep learning, Accuracy, Learning, EVORA, Uncertainty quantification.

Traversing terrain with good traction is crucial for achieving fast off-road navigation. Instead of manually designing costs based on terrain features, existing methods learn terrain properties directly from data via self-supervision to automatically penalize trajectories moving through undesirable terrain, but challenges remain to properly quantify and mitigate the risk due to uncertainty in learned models. To this end, this work proposes a unified framework to learn uncertainty-aware traction model and plan risk-aware trajectories. For uncertainty quantification, we efficiently model both aleatoric and epistemic uncertainty by learning discrete traction distributions and probability densities of the traction predictor's latent features. Leveraging evidential deep learning, we parameterize Dirichlet distributions with the network outputs and propose a novel uncertainty-aware squared Earth Mover's distance loss with a closed-form expression that improves learning accuracy and navigation performance....

## Introduction

Figure 1: This work proposes to learn terrain traction, the ratio between achieved and commanded velocities, while quantifying the uncertainty in the learned model to plan risk-aware trajectories. (a) Aleatoric uncertainty is the inherent and irreducible uncertainty due to partial observability. For example, visually similar terrain may have different traction values due to complex interactions between the robot and vegetation. (b) Epistemic uncertainty is the model uncertainty due to distribution shift between training and test environments, limiting the reliability of the learned model at test time.

Autonomous robots are increasingly being deployed in harsh off-road environments like mines, forests, and deserts, where both geometric and semantic understanding of the environments is required to identify non-geometric hazards (e.g., mud puddles, slippery surfaces) and geometric non-hazards (e.g., tall grass and foliage) \\editin order to achieve reliable navigation. To this end, recent approaches manually assign navigation costs based on semantic classification of the terrain, requiring significant human expertise to label and train a classifier sufficiently accurate and rich in order to achieve desired risk-aware behaviors....

## Conclusion

This work proposed EVORA, a unified framework for uncertainty-aware traversability learning based on evidential deep learning and risk-aware planning based on CVaR. EVORA models uncertain terrain traction via empirical distributions (aleatoric uncertainty) and identifies OOD terrain based on densities of traction predictor's latent features (epistemic uncertainty). By leveraging the proposed uncertainty-aware squared Earth Mover's Distance loss, we improved the network's prediction accuracy, OOD detection performance, and the downstream navigation performance....

### IV-B1 Worst-Case Expected Cost (CVaR-Cost )

where $n^{\text{prior}} = {\sum_{b = 1}^{B}\beta_{b}^{\text{prior}}}$ and $\mathbf{p}^{\text{prior}} = {{\mathbf{β}}^{\text{prior}}/n^{\text{prior}}}$. We use a flat prior by setting ${\mathbf{β}}^{\text{prior}} = \mathbf{1}_{B}$, where $\mathbf{1}_{B} \in {\mathbb{R}}^{B}$ is a vector of all ones, such that $\text{Dir}{({\mathbf{β}}^{prior})}$ is a uniform distribution over all PMFs....
