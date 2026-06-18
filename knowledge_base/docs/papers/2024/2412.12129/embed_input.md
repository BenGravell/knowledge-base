SceneDiffuser: Efficient and Controllable Driving Simulation Initialization and Rollout

Topics include Driving simulation, Diffusion models, Traffic simulation, Scene generation, Closed-loop simulation, Autonomous driving, Controllable generation, World models.

Presents SceneDiffuser, a diffusion-based scene-level prior for both traffic-scene initialization and closed-loop rollout. Its amortized denoising scheme lowers inference cost while generalized hard constraints and language-guided constraints make generated driving scenarios more controllable.

Realistic and interactive scene simulation is a key prerequisite for autonomous vehicle (AV) development. In this work, we present SceneDiffuser, a scene-level diffusion prior designed for traffic simulation. It offers a unified framework that addresses two key stages of simulation: scene initialization, which involves generating initial traffic layouts, and scene rollout, which encompasses the closed-loop simulation of agent behaviors. While diffusion models have been proven effective in learning realistic and multimodal agent distributions, several challenges remain, including controllability, maintaining realism in closed-loop simulations, and ensuring inference efficiency. To address these issues, we introduce amortized diffusion for simulation. This novel diffusion denoising paradigm amortizes the computational cost of denoising over future simulation steps, significantly reducing the cost per rollout step (16x less inference steps) while also mitigating closed-loop errors.

## Introduction

Simulation environments allow efficient and safe evaluation of autonomous driving systems. Simulation involves initialization (determining starting conditions for agents) and rollout (simulating agent behavior over time), typically treated as separate problems. Inspired by diffusion models' success in generative media, such as video generation and video editing (inpainting, extension, uncropping etc.), we propose SceneDiffuser, a unified spatiotemporal diffusion model that addresses both initialization and rollout for autonomous driving, trained end-to-end on logged driving scenes.

One challenge in simulation is evaluating long-tail safety-critical scenarios. While data mining can help, such scenarios are often rare. We address this by learning a generative scene realism prior that allows editing logged scenes or generating diverse scenarios. Our model supports scene perturbation (modifying a scene while retaining similarity) and agent injection (adding agents to create challenging scenarios). We also enable synthetic scene generation on roadgraphs with realistic layouts.

## Conclusion

We have introduced SceneDiffuser, a scene-level diffusion prior designed for traffic simulation. SceneDiffuser combines scene initialization with scene rollout to provide a diffusion-based approach to closed-loop agent simulation that is efficient (through amortized autoregression) and controllable (through generalized hard constraints). We performed scaling and ablation studies and demonstrated model improvements with computational resources. On WOSAC, we demonstrate competitive results with the leaderboard and state-of-the-art performance among diffusion methods.

Limitations While our amortized diffusion approach is, to our knowledge, the only and best performing closed-loop diffusion-based agent model with competitive performance, we do not exceed current SOTA performance for other autoregressive models. We do not explicitly model validity masks and resort to logged validity in this work. Future work looks to also model the validity mask.
