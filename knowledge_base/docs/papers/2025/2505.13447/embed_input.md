Mean Flows for One-step Generative Modeling

Topics include Neural networks, Diffusion models, Learning.

We propose a principled and effective framework for one-step generative modeling. We introduce the notion of average velocity to characterize flow fields, in contrast to instantaneous velocity modeled by Flow Matching methods. A well-defined identity between average and instantaneous velocities is derived and used to guide neural network training. Our method, termed the MeanFlow model, is self-contained and requires no pre-training, distillation, or curriculum learning. MeanFlow demonstrates strong empirical performance: it achieves an FID of 3.43 with a single function evaluation (1-NFE) on ImageNet 256x256 trained from scratch, significantly outperforming previous state-of-the-art one-step diffusion/flow models. Our study substantially narrows the gap between one-step diffusion/flow models and their multi-step predecessors, and we hope it will motivate future research to revisit the foundations of these powerful models.

## Introduction

The goal of generative modeling is to transform a prior distribution into the data distribution. Flow Matching provides an intuitive and conceptually simple framework for constructing flow paths that transport one distribution to another. Closely related to diffusion models, Flow Matching focuses on the velocity fields that guide model training. Since its introduction, Flow Matching has seen widespread adoption in modern generative modeling.

In this work, we propose a principled and effective framework, termed MeanFlow, for one-step generation. The core idea is to introduce a new ground-truth field representing the average velocity, in contrast to the instantaneous velocity typically modeled in Flow Matching. Average velocity is defined as the ratio of displacement to a time interval, with displacement given by the time integral of the instantaneous velocity. Solely originated from this definition, we derive a well-defined, intrinsic relation between the average and instantaneous velocities, which naturally serves as a principled basis for guiding network training.

Building on this fundamental concept, we train a neural network to directly model the average velocity field. We introduce a loss function that encourages the network to satisfy the intrinsic relation between average and instantaneous velocities. No extra consistency heuristic is needed. The existence of the ground-truth target field ensures that the optimal solution is, in principle, independent of the specific network, which in practice can lead to more robust and stable training.

## Conclusion

We have presented MeanFlow, a principled and effective framework for one-step generation. Broadly speaking, the scenario considered in this work is related to multi-scale simulation problems in physics that may involve a range of scales, lengths, and resolution, in space or time. Carrying out numerical simulation is inherently limited by the ability of computers to resolve the range of scales. Our formulation involves describing the underlying quantity at coarsened levels of granularity, a common theme that underlies many important applications in physics.
