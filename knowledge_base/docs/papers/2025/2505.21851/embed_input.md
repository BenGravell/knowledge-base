Streaming Flow Policy: Simplifying Diffusion/Flow-Matching Policies by Treating Action Trajectories as Flow Trajectories

Topics include Flow matching, Diffusion models, Robot learning, Imitation learning, Visuomotor policy, Streaming flow policy.

Simplifies flow-matching robot policies by treating the entire action trajectory as a flow trajectory rather than denoising per-timestep, reducing inference overhead while maintaining expressive multimodal action distributions.

Recent advances in diffusion/flow-matching policies have enabled imitation learning of complex, multi-modal action trajectories. However, they are computationally expensive because they sample a *trajectory of trajectories*—a diffusion/flow trajectory of action trajectories. They discard intermediate action trajectories, and must wait for the sampling process to complete before any actions can be executed on the robot. We simplify diffusion/flow policies by *treating action trajectories as flow trajectories*. Instead of starting from pure noise, our algorithm samples from a narrow Gaussian around the last action. Then, it incrementally integrates a velocity field learned via flow matching to produce a sequence of actions that constitute a *single* trajectory. This enables actions to be streamed to the robot on-the-fly *during* the flow sampling process, and is well-suited for receding horizon policy execution. Despite streaming, our method retains the ability to model multi-modal behavior. We train flows that *stabilize* around demonstration trajectories to reduce distribution shift and improve imitation learning performance.

## Introduction

Recent advances in robotic imitation learning, such as diffusion policy and flow-matching policy have enabled robots to learn complex, multi-modal action distributions for challenging real-world tasks such as cooking, laundry folding, robot assembly and navigation. They take a history of observations as input, and output a sequence of actions (also called an "action chunk"). Conventional diffusion$/$flow policies represent a direct application of diffusion models and flow-matching to robot action sequences --- they formulate the generative process as probabilistic transport in the space of action sequences, starting from pure Gaussian noise.

In this work, we propose a novel imitation learning framework that harnesses the temporal structure of action trajectories. We simplify diffusion$/$flow policies by treating action trajectories as flow trajectories. Our aim is to learn a flow transport in the action space $\mathcal{A}$, as opposed to trajectory space $\mathcal{A}^{T}$. Unlike diffusion$/$flow policies that start the sampling process from pure Gaussian noise (in $\mathcal{A}^{T}$), our initial sample comes from a narrow Gaussian centered around the most recently generated action (in $\mathcal{A}$).

We show how a streaming flow policy with the above desiderata can be learned using flow matching. Given an action trajectory from the training set, we construct a velocity field conditioned on this example that samples paths in a narrow Gaussian "tube" around the demonstration.

## Conclusion

In this work, we have presented a novel approach to imitation learning that addresses the computational limitations of existing diffusion and flow-matching policies. Our key contribution is a simplified approach that treats action trajectories as flow trajectories. This enables incremental integration of a learned velocity field that allows actions to be streamed to the robot during the flow sampling process. The streaming capability makes our method particularly well-suited for receding horizon policy execution.

## Limitations

In this section, we discuss some limitations of our approach.
