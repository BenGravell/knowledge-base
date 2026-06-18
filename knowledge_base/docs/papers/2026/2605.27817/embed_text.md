## Introduction

The core challenge of robot intelligence is one of generalization: we seek a system that can control a wide variety of embodiments to solve unseen tasks in new environments.

In natural language processing, the generality of large language models (LLMs) and vision-language models (VLMs) emerged through jointly scaling models and datasets. Vision-language-action (VLA) models extend pretrained vision-language backbones with action outputs in an attempt to transfer their generality to robotics tasks. However, different from the success of fine-tuning LLMs to VLMs, where web-scale, paired text and image data was available, no web-scale robot action data exists. In practice, it has proven challenging to achieve strong levels of generalization to new tasks, embodiments, and environments with VLAs: robot actions appear to be too distinct to inherit the generality of text and image models through fine-tuning on comparatively small action datasets.

Video generative models have been proposed as an alternative robotics backbone. They can generate "visual plans", imagining what it would look like for a robot to solve a specified task. Video models are not intrinsically tied to the action space of any one robot, and video data is abundant. However, we must now solve the problem of translating the video plan into robot actions. One route is to integrate actions into the video backbone itself, either through joint video-and-action prediction, known as *world-action models* (WAMs), or through action-conditioned world models paired with inference-time search. This route has produced impressive results, but, as with VLAs, requires a particularly rare kind of data for training: paired video, action, and text data.

In this work, we test the limits of an alternative approach to leveraging video models for robotics: a separate inverse dynamics model (IDM) that takes video as input and outputs corresponding robot actions. This separation has several key advantages. First, an IDM can be trained with *task-agnostic* video-action data, which can be more readily generated e.g. via self-play. Second, the same generative model can be shared across multiple embodiments by swapping the IDM. Lastly, stronger video backbones can be swapped in without retraining the IDM. However, the performance of the end-to-end pipeline is now critically dependent on the performance of the IDM: An inaccurate IDM leads to failures even if the video plan was perfect. Prior IDMs regress actions directly from a pair of generated frames with an unconstrained network. We find that, with limited action data, IDMs often generalize poorly out of distribution. Moreover, their accuracy degrades substantially as the complexity of the action space grows with more complex embodiments (Sec. 4).

To overcome these challenges, we introduce the Jacobian-IDM (J-IDM), which predicts actions through the inversion of a learned tangent map between action perturbations and pixel motion. We show that such a structure is both data-efficient and scales gracefully with embodiment complexity. We then pair J-IDM with a 14B video model adapted from the Large Video Planner: the video model predicts a visual lookahead, J-IDM translates this lookahead into an executable action chunk, the system executes and observes, and finally replans based on the rollout. We call our closed-loop video-to-action policy Video-to-Embodied Robot Action Model (VERA).

VERA is successful in simulated and real settings. On a real Panda arm, VERA performs zero-shot language-conditioned manipulation in a new physical setup with varied camera placements, scene configurations, and prompts requiring visual and linguistic reasoning. On a real Allegro hand, VERA performs RGB-only 16-DoF in-hand cube reorientation. In simulation, J-IDM outperforms prior IDM baselines. Furthermore, we validate that a video planner trained across our real-world embodiments can be used with different embodiment-specific J-IDMs. Lastly, we situate VERA against recent VLA and WAM baselines on real-world manipulation tasks. Our results show that video planning decoupled from a faithful inverse dynamics model is a promising and modular alternative for zero-shot, multi-embodiment, and generalizable robot control.

## Related Work and Preliminaries

### Behavior Cloning and Vision-Language-Action Models

Behavior cloning (BC) remains the dominant recipe for robot manipulation, learning actions directly from observations and task context, from offline visuomotor BC and language-conditioned imitation to more expressive sequence models based on action chunking, diffusion, and 3D action-centric representations. Modern VLA and generalist robot policies largely scale this same action-supervised interface: RT-1 and RT-2 attach robot actions to large visual/language backbones, while PaLM-E, RoboCat, Open X-Embodiment / RT-X, Octo, OpenVLA, and the $\pi$-family extend this paradigm to broader data mixtures, embodiments, and action spaces. Despite their scale and generality across task semantics, these methods still couple perception and control within a single embodiment-specific model. VERA instead keeps the foundation model in video space and learns separate embodiment-specific video-to-action bridges for each embodiment.

### Video Generative Models

Large-scale video pretraining has produced increasingly capable generative models with emergent visual priors and rudimentary physical reasoning. We build on the WAN family of open-weight video diffusion transformers and train with Diffusion Forcing, which enables variable-context conditioning.

### Joint Video-and-Action Models

A complementary line of work trains a single backbone to predict both future visual observations and robot actions, using video prediction as dense dynamics supervision while retaining an action head for execution. GR-2 jointly models video, language, and actions for manipulation; Video Prediction Policy learns predictive visual representations for policy learning; and LingBot-VA and DreamZero / World Action Models co-predict world states and actions with a video model backbone. Related action-conditioned world models and simulators use generated futures for planning or search. These approaches couple visual forecasting and action generation, whereas VERA separates them: the video model proposes an action-free visual plan, and an embodiment-specific IDM translates visual motion into controls.

### Video Models with Inverse Dynamics Models

Most closely related to VERA are methods that decouple robot control into a pixel-space planner and a translator. A similar factorization has also begun to appear in industrial systems: concurrent with this work, Rhoda AI's Direct Video-Action system achieves closed-loop, long-horizon bimanual manipulation in real-world settings. This result provides encouraging evidence that decoupled architectures can scale to real deployments.

## The Video-to-Embodied Robot Action Model

In this section, we first articulate the central technical challenge of using a video generative model as a robot policy --- translating predicted video into executable actions --- and identify the desired traits of a good translator (Sec. 3.1). We then introduce our proposed solution, the Jacobian IDM (Sec. 3.2) and describe how we put it all together in a closed-loop with a video model in Sec. 3.3.

### The Video-to-Action Problem

A video world model $\pi_{vid}$ produces a visual plan in pixel space: given an observation history $\mathbf{o}_{\leq t}$ and a goal $g$, it samples

Robots, however, do not act in pixels; they execute embodiment-specific commands such as position, velocity, or torque commands. The central question for the Video Model-IDM direction is therefore: how do we recover actions ${\hat{\mathbf{a}}}_{t:{{t + M} - 1}}$ from video frames?

### Desidarata: Faithfulness, data-efficiency, and scaling with DoFs

A good IDM should, first and foremost, be faithful: its inferred actions should reliably reproduce the predicted visual transition when executed. Beyond this, because action-labeled data is typically limited, it should be data-efficient, best if it only requires self-play data to train. Finally, it should scale with action complexity, allowing it to work for a variety of complex embodiments.

### IDMs require careful designs

Current IDMs come in two flavors. The first is hand-crafted methods based on retargeting or 3D representations. The second is direct parameterization via a neural network that learns to regress ${\hat{\mathbf{a}}}_{t}$ from the image pair $({\hat{\mathbf{o}}}_{t},{\hat{\mathbf{o}}}_{t + 1})$ end-to-end. Such an approach, which we call a Direct IDM (D-IDM), has value in its simplicity. However, under limited data and complex embodiments, a more structured IDM may be needed to satisfy the previous criteria. In Section 4 we show empirically that unstructured D-IDMs may sacrifice *faithfulness* under (i) data constraints and (ii) increasing action dimension.

### The Jacobian Inverse Dynamics Model

### The embodiment Jacobian

The problem of relating infinitesimal actions to motion is solved in classical robotics by the embodiment Jacobian. Let $\mathbf{a} \in {\mathbb{R}}^{n}$ denote the robot's action vector and $\mathbf{x}_{i} \in {\mathbb{R}}^{3}$ the 3D location of body point $i$. At a given state---observed as $\mathbf{o}$---the embodiment Jacobian

(Eq. 2) is the local linear map from action perturbations to 3D point motion: ${\delta\mathbf{x}_{i}} \approx {\mathbf{J}_{i}{(\mathbf{o})}\delta\mathbf{a}}$. However, 3D points are never observed directly, making such a Jacobian difficult to learn directly.

### Image-space Jacobian field

This motivates predicting the Jacobian directly in image space, with $\mathbf{o}$ itself as the conditioning variable. Given a single image $\mathbf{o} \in {\mathbb{R}}^{H \times W \times 3}$, an image-conditioned transformer $\mathbf{J}_{\theta}$ outputs a dense field

which assigns to every pixel $\mathbf{p}$ a $2 \times n$ matrix that linearizes how an action increment ${\delta\mathbf{a}} \in {\mathbb{R}}^{n}$ moves that pixel:

where $\delta\mathbf{p}$ is the per-pixel measurement of the observation change $\delta\mathbf{o}$, obtained in practice from an off-the-shelf optical-flow estimator (Eq. 5). Prior work parameterized this Jacobian as a *3D* field, lifting per-pixel motion to 3D via volume rendering of a NeRF-style scene representation; we drop the 3D scene representation, which lets us scale $\mathbf{J}_{\theta}$ as a single, large image-conditioned transformer. At test time, we recover the action by inverting Eq. 4.

### Joint forward-inverse training objective

We train $\mathbf{J}_{\theta}$ on a dataset of $(\mathbf{o}_{t},{\delta\mathbf{a}_{t}},\mathbf{o}_{t + 1})$ tuples. For each tuple, we extract a dense optical flow field $\mathbf{v}_{t} \in {\mathbb{R}}^{H \times W \times 2}$ between $\mathbf{o}_{t}$ and $\mathbf{o}_{t + 1}$ using off-the-shelf motion estimators. We supervise $\mathbf{J}_{\theta}$ with a joint forward-inverse loss combining the per-pixel Charbonnier objective ${\rho{(x)}} = \sqrt{x^{2} + \varepsilon^{2}}$ on the predicted pixel motion with an action-reconstruction term using a $\lambda$-regularized pseudoinverse $\mathbf{J}_{\theta}^{\dagger,\lambda}$:

with $w_{\text{a}} = 0.3$; see App. B for training details.

### From forward model to IDM

At inference, we are given two consecutive predicted frames $({\hat{\mathbf{o}}}_{t},{\hat{\mathbf{o}}}_{t + 1})$ from the video planner. We extract their optical flow $\mathbf{v}_{t}$ with the same off-the-shelf motion estimator used in training and recover the action via the $\lambda$-regularized pseudoinverse:

### Video World Model as a Closed-Loop Robot Planner

VERA uses a video world model as a planner in observation space, as illustrated in Fig. 2. Given some observations and conditioning signal (typically text), it predicts how the scene should visually evolve. Two design choices distinguish our planner from a vanilla video model.

Figure 2: Translating video to actions. a, Given context frames, our video world model rolls out a short visual plan. b, The Jacobian IDM inverts each step of this path into a chunk of low-level actions. c, The chunk is executed and observations return to the video model for closed-loop execution.

### Action-free robot post-training

We instantiate the planner from a pretrained video model and lightly adapt it to robot video-only data; the post-training objective is generative video prediction with *no action head*. Two modifications make it usable as a policy: video-to-video finetuning ($N$ context frames , $M$ future frames out) for autoregressive rollouts, and a multi-view variant that tiles cameras into a single canvas. Architectural details are in App. A.1--A.2.

### Executing on a visual chunk

Although the planner generates $M$ future frames, the controller commits to executing only the first $K$ predicted frames. The Jacobian IDM converts this committed prefix into a chunk of robot actions by applying Eq. 6 independently to every pair of adjacent frames, using the current observation $\mathbf{o}_{t}$ as the anchor:

yielding a chunk length of $K$ actions. This allows the planner to reason over a longer visual look-ahead while the controller stays grounded through frequent feedback. Consistent with prior findings on action chunking, we observe that this chunking improves performance; we ablate the choice of $K$ in Fig. 8.

### Closed-loop replanning

After executing the chunk, the robot appends the newly observed frames to its history and queries the planner again. The execution horizon $K$ governs the feedback--smoothness trade-off: larger values produce longer locally-coherent chunks and amortize video generation time; smaller values reduce drift during execution. The full procedure is given in Alg. 1.

## Experiments

Figure 3: Zero-Shot Evaluation on Panda Arm. a, After training on DROID, we deploy zero-shot on a Panda in an unseen scene with ad-hoc camera placements; in Press-Hidden-Button, the blue target is visible from only one of three views, with an orange distractor probing instruction grounding. b, Visualization of the predicted Jacobian: each column of Jθ is assigned a fixed RGB color and rendered, per pixel, weighted by the norm of the corresponding Jacobian column. Columns: action channels; rows: viewpoints. c, Generated frames and executions shown side-by-side with the text prompt; actions remain closely aligned with the generated frames.

We evaluate the VERA system in closed-loop manipulation, isolate the Jacobian IDM against alternative IDM variants, and compare to state-of-the-art VLA and world-action baselines.

### Experiment Setup

Unless otherwise noted, VERA uses a Wan-family pretrained video model as the planner and an embodiment-specific J-IDM initialized from VGGT as the translator. We evaluate in simulation (PushT, MimicGen Panda, Allegro-Sim cube reorientation ) and on hardware (Panda-Real post-trained on DROID, Allegro-Real dexterous reorientation), reporting closed-loop success and task progress; full setup and video-model ablations are in Appendix A--A.2.

### Main Results

### Jacobian IDMs enable faithful video-to-action translation

We found that our Jacobian IDM can faithfully translate video chunks predicted by a world model into action chunks executed on the robot. Qualitatively, across environments, we have executions that are consistent with our generations, as shown in Fig. 3,4. Faithful translation naturally provides the robotic system with the capabilities of video models: visuospatial reasoning, prompt-following, embodiment generalization, and task generalization. These will be discussed throughout the rest of this section.

Figure 4: In-Hand Object Reorientation. a, Cube-reorientation demonstrations with three language instructions (clockwise, counter-clockwise, random); we evaluate prompt-conditioned in-hand reorientation. b, Predicted Jacobian visualized as in Fig. 3b (columns: selected action channels out of 16 total; rows: viewpoints). c, Generated frames and executions side-by-side with prompt; the model orchestrates dexterous finger motions.

### VERA performs zero-shot, prompt-following manipulation tasks on a Panda arm

Just as any video model can generate videos zero-shot in new environments, when armed with a translator, VERA performs zero-shot manipulation. Throughout our evaluations, we varied lighting conditions, camera configurations, and object orientations and found it robust to such changes. Our robot can perform manipulations that follow complex prompts, as demonstrated in Fig. 1, and perform complex vision-language reasoning tasks, as will be expanded upon in Sec. 4.3.

### VERA admits multi-embodiment

Our video model which is finetuned across DROID and sim and real allegro hands --- two vastly different embodiments --- is able to generate successful video plans on both. Then, armed with two embodiment-specific J-IDMs, is able to control both a panda arm and the contact-rich re-orientation of a block via its fingers. As seen in Fig. 4, the latter is a multi-stage and challenging task for a purely visual system. However, armed with a strong video model, a sufficient translator, and closed loop control, VERA is able to complete the task.

### Designing a Faithful IDM for Video-to-action Translation

Figure 5: J-IDM scales with action dimensionality. a, Rollouts of recovered actions for direct-IDM baselines and J-IDM as DoFs grow. b, At a fixed data budget, the J-IDM gap over direct-IDMs widens with DoF. c, At high DoF, J-IDM has a better data-accuracy trade-off across training sizes.

The closed-loop results above rely on *faithful* video-to-action translation. We now isolate this property and ask what makes it possible. By comparing a Jacobian-parameterized IDM against unstructured D-IDM baselines under controlled data and DoF budgets, we find the gain comes specifically from the Jacobian-based constraint. The J-IDM is one concrete instantiation of that constraint; the rest of this subsection compares it against unstructured D-IDM baselines.

### Experiment Setup

We compare our J-IDM against blackbox D-IDM approaches. In particular, we test against two models: one which takes in a pair of images (i.e. $\mathbf{o}_{t}$ and $\mathbf{o}_{t + 1}$) and another which takes in an image and the optical flow between the two images. All models are kept at the same parameter count, trained on the same data, and share the same architecture with the exception of the decoding head. The flow-conditioned model serves as an ablation of our approach, since it has the same input-output behavior, but lacks our structured representation. The image-pair model is our best-effort replication of UniPi. Because we use a different architecture to ensure a fair comparison, we refer to this baseline as UniPi\*. More details can be found in Appendix B.3.

### J-IDMs are performant under data and complexity constraints

A controlled 2D "toy finger" study (Fig. 5) sweeps degrees of freedom and self-play data quantity. The structured parameterization brings two benefits over an unstructured regressor: at fixed data, J-IDM is the only model preserving faithful reconstruction as DoFs grow (Fig. 5a,b); and at fixed DoFs ($=$`<!-- -->`{=html}5), it is approximately $2 \times$ more data-efficient (Fig. 5c).

### Faithful translation results in higher success rates

This fidelity carries downstream. In Tab. 2, J-IDM achieves the lowest action-reconstruction MSE on all but one of the tested environments. Improved reconstruction translates to task success by preserving the video model's "dreams": with the planner held fixed, J-IDM outperforms UniPi\* on every closed-loop task (Tab. 1).

Table 1: Closed-loop results in simulated environments. Each cell reports success rate / task progress (%, ↑). J-IDM yields higher closed-loop success than a UniPi*-style direct inverse-dynamics baseline across planar pushing, 7-DoF arm manipulation, and 16-DoF dexterous manipulation.

Action reconstruction MSE ↓

Table 2: Action reconstruction for video-to-action translation. Reconstruction MSE on held-out visual transitions. Jacobian IDM achieves the lowest MSE on Allegro-Sim, PushT-Sim, and 5-joint fingers, and remains competitive on Panda-Sim. Best / second-best.

### VERA and other Robotic Foundation Models

We compare VERA against state-of-the-art VLA and WAM baselines ($\pi_{0.5}$, DreamZero) on an in-house Panda manipulation suite, using DROID-trained checkpoints across all systems (Fig. 6).

### Instruction following on basic tasks

On basic "push A"/"pick up B" tasks, DreamZero attains 90%, VERA 60%, and $\pi_{0.5}$ 30%. VERA's failures generally arise from the video-to-action step: VERA's dreamed futures on failing rollouts consistently complete the task, but the translation to action lacks fidelity. $\pi_{0.5}$, on the other hand, frequently disregards the instruction and acts on the wrong object.

Figure 6: Real-world comparison with robot foundation model baselines. VERA remains competitive on basic tasks and substantially better on challenging tasks.

### Instruction following on challenging tasks

We further design two sets of harder, reasoning-heavy prompts: location-based prompts (e.g., "push the button on top of the paper") that do not directly reveal the target, and semantic-based prompts (e.g., "push the button matching the wrench's color") that require visual grounding. While video-to-action translation is the bottleneck for VERA on basic tasks, the strength of the underlying video model allows VERA to remain performant: DreamZero and $\pi_{0.5}$ frequently act on incorrect objects entirely, whereas VERA succeeds, suggesting that decoupling the planner from the IDM preserves more of the video model's reasoning.

### Reasoning through occlusions

To further test multi-view reasoning, we design the "find the button" challenge: a button is hidden behind a wall, visible from only one of three cameras, amid distractor props on a cluttered table (Figs. 3, 7). DreamZero and $\pi_{0.5}$ struggle to locate and navigate around the wall. VERA, on the other hand, produces coherent plans that the J-IDM is able to execute. Moreover, for DreamZero, the dreamed future itself fails to produce a plan that finds and presses the button, indicating that the failure originates in the video branch. This is consistent with the hypothesis that preserving the video branch on its own allows the model to retain video-model reasoning capabilities that an end-to-end head would otherwise dilute.

## Discussion and Conclusion

### Conclusion

We have shown that strong video models, paired with a faithful IDM, can control diverse embodiments and solve diverse tasks. Our Jacobian IDM is one such instantiation: data-efficient, scaling with action dimensionality, and preserving the visual reasoning of the planner that an end-to-end action head would otherwise dilute.

### Limitations

VERA still requires robot-specific video for planner post-training, depends on off-the-shelf optical-flow trackers for J-IDM supervision, and cannot reason about force-based control from RGB alone. Faithful action recovery also degrades when the predicted transition has little observable pixel motion.

### Future Work

Promising directions include sim-to-real J-IDM transfer to remove the need for real-robot action data, planner co-training across humans and robots, and an embodiment-conditioned Jacobian that serves multiple morphologies---motivating careful IDM design as video world models improve.
