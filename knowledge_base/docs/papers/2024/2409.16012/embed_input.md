PRESTO: Fast Motion Planning Using Diffusion Models Based on Key-Configuration Environment Representation

Topics include PRESTO, Motion planning, Diffusion, Diffusion models, Trajectory optimization, Collision-free.

We introduce a learning-guided motion planning framework that generates seed trajectories using a diffusion model for trajectory optimization. Given a workspace, our method approximates the configuration space (C-space) obstacles through an environment representation consisting of a sparse set of task-related key configurations, which is then used as a conditioning input to the diffusion model. The diffusion model integrates regularization terms that encourage smooth, collision-free trajectories during training, and trajectory optimization refines the generated seed trajectories to correct any colliding segments. Our experimental results demonstrate that high-quality trajectory priors, learned through our C-space-grounded diffusion model, enable the efficient generation of collision-free trajectories in narrow-passage environments, outperforming previous learning- and planning-based baselines. Videos and additional materials can be found on the project page:

## Introduction

Motion planning involves finding a smooth and collision-free path in a high-dimensional configuration space (C-space). Classical motion planning algorithms typically use either sampling-based methods \[lavalle1998rapidly, lavalle2001rapidly, kavraki1996probabilistic\] or optimization-based methods \[ratliff2009chomp, schulman2014motion\] to address motion planning across various domains. However, in high-dimensional C-spaces with narrow passages, sampling-based methods incur high computational costs due to large search spaces and small volume of solutions....

Recent works leverage generative models to directly learn trajectory distributions instead \[janner2022planning, huang2023diffusion, carvalho2023motion\]. By casting motion planning as sampling from a learned distribution, these models can efficiently generate trajectories within a consistent computational budget. However, they often struggle to generalize to new, complex C-spaces, resulting in high collision rates in the generated trajectories, because most of these approaches use the workspace as input to neural networks instead of the C-space....

## Conclusion

We present \\ourmethod, a learning-guided motion planning framework that integrates diffusion-based trajectory sampling with post-processing trajectory optimization. Incorporating C-space environment representations based on key configurations and a motion-planning training objective, our framework efficiently generates collision-free trajectories in unseen environments. Simulated experiments demonstrate the efficacy of our framework compared to both diffusion-based planning approaches and conventional motion planning methods. In this work, we assumed known environment geometry for ground-truth collision states at key configurations....

## Experiments

To process the inputs, the trajectory $\tau_{i}$ is first patchified and tokenized by an MLP, as in DiT \[Peebles2022DiT\]. The diffusion step $i$ and the start and goal configurations $q_{s}$ and $q_{g}$ are mapped to high-dimensional frequency embeddings \[Peebles2022DiT\] to capture small changes. The embedded trajectory patches are given as input tokens to the transformer, while $i$, $\phi$, $q_{s}$, and $q_{g}$ are incorporated as conditioning inputs to align sampled trajectories with the current scene and endpoint constraints.
