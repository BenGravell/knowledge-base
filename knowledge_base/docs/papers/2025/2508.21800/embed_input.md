Tree-Guided Diffusion Planner

Topics include Robotics, Diffusion models, Generalization, Planning, Control, Sampling, TDP.

Planning with pretrained diffusion models has emerged as a promising approach for solving test-time guided control problems. Standard gradient guidance typically performs optimally under convex, differentiable reward landscapes. However, it shows substantially reduced effectiveness in real-world scenarios with non-convex objectives, non-differentiable constraints, and multi-reward structures. Furthermore, recent supervised planning approaches require task-specific training or value estimators, which limits test-time flexibility and zero-shot generalization. We propose a Tree-guided Diffusion Planner (TDP), a zero-shot test-time planning framework that balances exploration and exploitation through structured trajectory generation. We frame test-time planning as a tree search problem using a bi-level sampling process: diverse parent trajectories are produced via training-free particle guidance to encourage broad exploration, and sub-trajectories are refined through fast conditional denoising guided by task objectives.

## Introduction

Diffusion models offer a data-driven framework for planning, enabling the generation of coherent and expressive trajectories learning from offline demonstrations \[janner2022planningdiffusionflexiblebehavior, liang2023adaptdiffuserdiffusionmodelsadaptive, pmlrv202li23ad, chen2024simplehierarchicalplanningdiffusion\]. Compared to single-step model-free reinforcement learning (RL) methods \[kumar2020conservativeqlearningofflinereinforcement, kostrikov2021offlinereinforcementlearningimplicit\], diffusion planners are more effective for long-horizon planning by generating temporally extended trajectories through multi-step prediction.

We propose Tree-guided Diffusion Planner (TDP), which formulates test-time planning as a tree search problem that balances exploration via diverse trajectory samples and exploitation via guided sub-trajectories. While pretrained diffusion planners model underlying system dynamics, TDP samples high-reward (i.e., high guidance score for the test task) solution trajectories conditioned on the learned dynamics in a zero-shot manner. TDP equips the pretrained diffusion planner model with the ability to reason over higher-level objectives.

## Conclusion

In summary, we propose TDP, a flexible test-time planning framework that leverages a pretrained diffusion planner via a bi-level trajectory-sampling process without training. By balancing trajectory diversity and gradient-guided refinement via a branching structure of sampled trajectories, our method addresses key limitations of conventional test-time-guided planning. Empirical results across both structured and compositional manipulation tasks demonstrate consistent performance gains over existing baselines, particularly in scenarios that demand out-of-distribution generalization.

## Limitation and Future Work

While TDP outperforms existing planning approaches across a suite of challenging test-time control tasks, our bi-level trajectory generation process incurs additional computational cost due to the expanded search in trajectory space and the pairwise trajectory distance calculations. We analyze the additional computational time required for the two PnP tasks and the PnWP task in Appendix˜G. Future work may explore more efficient search strategies or learned priors to reduce overhead while ensuring sufficient exploration and preserving planning performance.
