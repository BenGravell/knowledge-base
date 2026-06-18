Streaming Flow Policy: Simplifying Diffusion/Flow-Matching Policies by Treating Action Trajectories as Flow Trajectories

Topics include Flow matching, Diffusion models, Robot learning, Imitation learning, Visuomotor policy, Streaming flow policy.

Simplifies flow-matching robot policies by treating the entire action trajectory as a flow trajectory rather than denoising per-timestep, reducing inference overhead while maintaining expressive multimodal action distributions.

Recent advances in diffusion/flow-matching policies have enabled imitation learning of complex, multi-modal action trajectories. However, they are computationally expensive because they sample a *trajectory of trajectories*—a diffusion/flow trajectory of action trajectories. They discard intermediate action trajectories, and must wait for the sampling process to complete before any actions can be executed on the robot. We simplify diffusion/flow policies by *treating action trajectories as flow trajectories*. Instead of starting from pure noise, our algorithm samples from a narrow Gaussian around the last action. Then, it incrementally integrates a velocity field learned via flow matching to produce a sequence of actions that constitute a *single* trajectory. This enables actions to be streamed to the robot on-the-fly *during* the flow sampling process, and is well-suited for receding horizon policy execution. Despite streaming, our method retains the ability to model multi-modal behavior. We train flows that *stabilize* around demonstration trajectories to reduce distribution shift and improve imitation learning performance....

## Introduction

Recent advances in robotic imitation learning, such as diffusion policy and flow-matching policy have enabled robots to learn complex, multi-modal action distributions for challenging real-world tasks such as cooking, laundry folding, robot assembly and navigation \[\]. They take a history of observations as input, and output a sequence of actions (also called an "action chunk")....

In this work, we propose a novel imitation learning framework that harnesses the temporal structure of action trajectories. We simplify diffusion$/$flow policies by treating action trajectories as flow trajectories. Our aim is to learn a flow transport in the action space $\mathcal{A}$, as opposed to trajectory space $\mathcal{A}^{T}$. Unlike diffusion$/$flow policies that start the sampling process from pure Gaussian noise (in $\mathcal{A}^{T}$), our initial sample comes from a narrow Gaussian centered around the most recently generated action (in $\mathcal{A}$)....

Intuitively, the target velocity field $v^{\ast}$ at $(a,t)$ is a weighted average of conditional flow velocities $v_{\xi}{(a,t)}$ over demonstrations $\xi$. The weight for $\xi$ is the Bayesian posterior probability of $\xi$, where the prior probability $p_{\mathcal{D}}{(\left. \xi \middle| h \right.)}$ is the probability of $\xi$ given $h$ in the training distribution, and the likelihood $p_{\xi}{(\left. a \middle| t \right.)}$ is the probability that the conditional flow around $\xi$ generates $a$ at time $t$.

Under sufficiently small values of $k$, we have from Eq. 2 that ${v_{\xi}{(a,t)}} \approx {\overset{˙}{\xi}{(t)}}$. Note that $v^{\ast}$ is then a convex combination of demonstration velocities $\overset{˙}{\xi}{(t)}$. Consider convex constraints over velocities ${\overset{˙}{\xi}{(t)}} \in C$ i.e. $\overset{˙}{\xi}{(t)}$ is constrained to lie in a convex set $C$ for all $\xi$ with non-zero support ${p_{\mathcal{D}}{(\xi)}} > 0$ and for all $t \in {\lbrack 0,1\rbrack}$. This is the case, for example, when robot joint velocities lie in a closed interval $\lbrack v_{\min},v_{\max}\rbrack$. Then, Eq. 6 implies that $v^{\ast}$ also lies in $C$.

## Experiments

This is simply an expected $L_{2}$ loss between a candidate velocity field $v{(a,\left. t \middle| h \right.)}$ and the the analytically constructed conditional velocity field $v_{\xi}{(a,t)}$ as target....
