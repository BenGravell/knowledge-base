Causal Composition Diffusion Model for Closed-loop Traffic Generation

Topics include Autonomous driving, Safety, Diffusion models, Causal inference, Datasets, Benchmarks, Optimization, Control, Learning, Closed-loop.

Simulation is critical for safety evaluation in autonomous driving, particularly in capturing complex interactive behaviors. However, generating realistic and controllable traffic scenarios in long-tail situations remains a significant challenge. Existing generative models suffer from the conflicting objective between user-defined controllability and realism constraints, which is amplified in safety-critical contexts. In this work, we introduce the Causal Compositional Diffusion Model (CCDiff), a structure-guided diffusion framework to address these challenges. We first formulate the learning of controllable and realistic closed-loop simulation as a constrained optimization problem. Then, CCDiff maximizes controllability while adhering to realism by automatically identifying and injecting causal structures directly into the diffusion process, providing structured guidance to enhance both realism and controllability. Through rigorous evaluations on benchmark datasets and in a closed-loop simulator, CCDiff demonstrates substantial gains over state-of-the-art approaches in generating realistic and user-preferred trajectories....

## Introduction

Reliable closed-loop traffic simulation is essential for assessing autonomous vehicle (AV) safety in diverse and complex scenarios. Simulations must be both realistic, capturing the intricacies of real-world driving, and controllable, allowing customization aligned with user preferences. However, balancing realism with controllability remains a significant challenge. Previous works often prioritize one aspect, optimizing either realism or user-specified objectives. How to jointly achieve both objectives under safety-critical conditions remains fruitful yet unresolved.

Figure 1: Comparison of safety-critical scenario generation methods, featuring CCDiff alongside existing methods (STRIVE, CTG, and TrafficSim). The illustrated scenario involves Car 13 executing an unprotected left turn, prompting Car 7 to change lanes and interfere with Car 5. Unlike other methods, CCDiff successfully achieves both realism and controllability in generating this safety-critical scenario. In the right column, CCDiff’s spatial reasoning method is compared to a distance-based baseline approach....

### Diffusion model for sequential decision making

Diffusion models have shown strong controllability in density estimation and generation tasks. Scenario Diffusion \[\] adopts latent diffusion, utilizing multi-source conditioning to generate realistic scenarios. In closed-loop traffic simulation, several prior works incorporate compositional classifier-based guidance to steer the diffusion model's sampling process, including signal temporal logic (STL) guidance, language-based guidance \[\], adversarial guidance, and game-theoretic guidance \[\].

We propose CCDiff, a principled algorithm to solve the constrained optimization problem by identifying the causal structure and injecting it as a structured guidance to the diffusion model.

Recent advances in deep generative models have enabled scalable traffic behavior simulation, facilitating realistic scenario generation from massive offline datasets. Notably, prior works compose explicit rules into scenario generation, such as causal graphs (CG), signal temporal logic (STL), or large language models (LLM), which act as structured constraints to improve the controllability. However, interactive driving scenarios cannot be fully encapsulated by explicit rules alone....
