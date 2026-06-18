Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

Topics include Diffusion policy, Diffusion models, Action diffusion, Machine learning, Imitation learning, Robot learning, Visuomotor policy, Transformers.

Models robot visuomotor policy as a denoising diffusion process over action sequences, enabling multimodal and high-dimensional action distributions that outperform regression-based imitation learning methods on dexterous manipulation benchmarks.

This paper introduces Diffusion Policy, a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process. We benchmark Diffusion Policy across 15 different tasks from 4 different robot manipulation benchmarks and find that it consistently outperforms existing state-of-the-art robot learning methods with an average improvement of 46.9%. Diffusion Policy learns the gradient of the action-distribution score function and iteratively optimizes with respect to this gradient field during inference via a series of stochastic Langevin dynamics steps. We find that the diffusion formulation yields powerful advantages when used for robot policies, including gracefully handling multimodal action distributions, being suitable for high-dimensional action spaces, and exhibiting impressive training stability. To fully unlock the potential of diffusion models for visuomotor policy learning on physical robots, this paper presents a set of key technical contributions including the incorporation of receding horizon control, visual conditioning, and the time-series diffusion transformer....

## Introduction

Policy learning from demonstration, in its simplest form, can be formulated as the supervised regression task of learning to map observations to actions. In practice however, the unique nature of predicting robot actions --- such as the existence of multimodal distributions, sequential correlation, and the requirement of high precision --- makes this task distinct and challenging compared to other supervised learning problems.

Prior work attempts to address this challenge by exploring different action representations -- using mixtures of Gaussians Mandlekar et al., categorical representations of quantized actions Shafiullah et al., or by switching the the policy representation -- from explicit to implicit to better capture multi-modal distributions Florence et al.; Wu et al..

## Conclusion

In this work, we assess the feasibility of diffusion-based policies for robot behaviors. Through a comprehensive evaluation of 15 tasks in simulation and the real world, we demonstrate that diffusion-based visuomotor policies consistently and definitively outperform existing methods while also being stable and easy to train. Our results also highlight critical design factors, including receding-horizon action prediction, end-effector position control, and efficient visual conditioning, that is crucial for unlocking the full potential of diffusion-based policies....

In particular, when the prediction horizon is one time step, $T_{p} = 1$, it can be seen that the optimal denoiser which minimizes

## Intriguing Properties of Diffusion Policy

We found training ViT from scratch to be challenging (with only 22% success rate), likely due to the limited amount data. We also found training with frozen pretrained vision encoder to yield poor performance, which indicates that diffusion policy prefers different vision representation than what is offered in popular pretraining methods. However, we found finetuning the pretrained vision encoder with a small learning rate (10x smaller vs diffusion policy network) gives the best performance overall. This is especially true for the CLIP-trained ViT-B/16, which reaches 98% success rate with only 50 epochs of training....

In this work, we seek to address this challenge by introducing a new form of robot visuomotor policy that generates behavior via a "conditional denoising diffusion process Ho et al....
