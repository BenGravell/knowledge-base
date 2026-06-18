## Introduction

Recent robotic foundation models, termed Vision-Language Action models (VLAs), extend pretrained Vision-Language Models (VLMs) to predict motor actions. While VLAs successfully inherit linguistic priors to generalize across diverse language instructions, especially manipulating diverse objects, their generalization to novel environments and, more critically, to new motions or skills remains limited. For example, VLAs can successfully execute "move coke can to Taylor Swift" by leveraging the web knowledge acquired during VLM pretraining to identify the target location, and connecting it to the learned move skill from the robot data. However, they fail at a task like "untie the shoelace" if that specific skill was not present in the robot training data. Although VLM priors encode what to do at a semantic level, they lack representations of how actions should be executed with precise spatial awareness, aligned with geometry, dynamics, and motor control. As a result, VLAs often struggle to adapt to new environments or generalize to novel tasks beyond the distribution of expert demonstrations, without explicitly collecting large-scale task- and environment-specific action data.

In this paper, we present DreamZero, a 14B robot foundation model built upon a pretrained image-to-video diffusion backbone. We term this architecture a World Action Model (WAM)---a foundation model designed to predict both actions and visual future states in an aligned manner. Initialized from video diffusion models trained on web-scale video data, WAMs leverage rich spatiotemporal priors to jointly generate future frames and actions conditioned on language instructions and observations. This shifts action learning from dense state--action imitation to inverse dynamics---aligning motor commands with predicted visual futures. Consequently, we observe that this enables effective learning from robot data that are heterogeneous trajectories collected during the execution of useful behaviors in real-world settings, rather than relying solely on carefully repeated demonstrations zero-shot generalization to new tasks in new environments, and efficient cross-embodiment transfer.

Figure 2: Joint Video and Action Prediction. DreamZero jointly generates video and action. We observe that the predicted actions closely align with the generated video. The examples are from totally unseen tasks.

This approach yields three core advancements that distinguish DreamZero from prior work, including other WAMs. First, DreamZero unlocks new generalization capabilities beyond traditional VLAs and previous WAMs---across environments, across tasks, and across embodiments (Figure 2 and Figure 3). Compared to the state-of-the-art pretrained VLAs, we observe more than a 2$\times$ improvement in average task progress on environment and task generalization benchmarks. Second, DreamZero demonstrates that generalist policies can be learned effectively from diverse, heterogeneous data, breaking away from the conventional wisdom that generalist robot policies require multiple repeated demonstrations per task. Although other WAMs show that priors learned from videos prediction improves sample efficiency for action learning compared to VLAs, most works still focus on repeated demonstrations. Moreover, the environment generalization of DreamZero is retained even after task-specific post-training, outperforming state-of-the-art VLAs by 10% on average task progress. Lastly, we demonstrate two forms of cross-embodiment transfer. First, video-only demonstrations from another robot (YAM) or humans yield a relative improvement of over 42% on unseen task performance for the target robot (AgiBot G1) with just 10--20 minutes of data. Second, and more surprisingly, we show that DreamZero enables few-shot embodiment adaptation: a model pretrained on AgiBot G1 adapts to an entirely new robot (YAM) with only 30 minutes of play data, retaining zero-shot generalization. To the best of our knowledge, this sets a new benchmark for data-efficient embodiment adaptation.

DreamZerois a 14B autoregressive diffusion transformer trained with a teacher-forcing chunk-wise video denoising objective. Our architectural analysis reveals that larger pretrained video diffusion models produce higher-quality video predictions, which directly translates to superior downstream action execution---indicating that policy performance is fundamentally tied to video generation quality. We further find that diverse distribution of the training data is essential for generalization, outperforming multi-task repetitive data with the same amount of hours. Furthermore, we observe that autoregressive architectures lead to smoother robot motions and higher modality alignment between predicted videos and executed actions.

To address the computational overhead inherent to video diffusion models, we introduce a suite of optimizations spanning three categories: algorithmic improvements, including decoupled video and action denoising schedules (DreamZero-Flash); system-level parallelism and caching strategies; and low-level optimizations such as quantization, and CUDA kernel tuning. Collectively, these techniques achieve a 38× inference speedup without degrading performance, enabling DreamZero to generate action chunks at approximately 7Hz for smooth, real-time robotic control.

Our main contributions are:

We introduce DreamZero, a 14B WAM that jointly predicts video and actions, enabling effective learning from diverse, non-repetitive robot data.

We demonstrate over 2$\times$ improvement in zero-shot generalization to unseen verbs and motions compared to state-of-the-art VLAs, while retaining generalization across objects and environments.

We present model and system optimizations achieving 38$\times$ inference speedup, enabling real-time closed-loop control at 7Hz.

We demonstrate cross-embodiment transfer: video-only data from humans (12 minutes) or other robots (20 minutes) yields a relative improvement of over 42% on unseen tasks, and introduce few-shot embodiment adaptation---DreamZero pretrained on AgiBot G1 adapts to an entirely new robot (YAM) with only 30 minutes of play data, enabling zero-shot generalization.

We open-source our model weights, inference code, and code to run publicly available real-world (RoboArena) and simulation benchmarks (PolaRiS and Genie Sim 3.0)^11^1Despite only being trained on $\sim$`<!-- -->`{=html}500 hours of real-world data, DreamZero shows non-trivial performance on Genie Sim 3.0, which is a simulation benchmark comprised of 100 different tasks without being explicitly trained on the 10k hours of simulation training data. at

Figure 3: Free-form Evaluation. DreamZero performs a diverse range of tasks when conditioned on natural language instructions, including object manipulation, tool use, and human-robot interaction.

## Related Work

### Vision Language Action Models

Utilizing Foundation Models for Robotics. Developing foundation models for physical artificial intelligence has emerged as a significant research frontier. One line of work involves using existing, pre-trained foundation models as "black-box" reasoners to handle high-level task planning. These works usually involve modular systems, where the foundation models generate sequences of instructions, visual traces, or affordances that are subsequently executed by specialized, low-level robotic policies or controllers. While this modularity simplifies complex planning and enables stronger generalization and efficiency, it is contingent upon having a pre-existing library of low-level skills and a robust interface to bridge the gap between abstract reasoning and physical execution. Additionally, these decoupled systems face the risk of compounding errors across modules.

VLAs. On the other hand, end-to-end models such as Vision-Language-Action models (VLAs), have gained popularity by moving away from a rigid hierarchy of planning and control, combining language-conditioned semantics and low-level robot actions within the same model. VLAs are often initialized from large vision-language (VLM) models pre-trained on web-scale datasets. While pushing the frontier on visual-semantic knowledge transfer, these models are pre-trained on static image-text datasets, which limits their ability to inherit spatiotemporal priors required to transfer knowledge to new physical skills.

Generalization in VLAs. Generalization in VLAs has been mostly demonstrated on object and semantic level while generalization to completely new skills and environments has remained limited. In particular, existing work utilizing VLAs achieves environment generalization by collecting human teleoperation data across hundreds of diverse environments for specific tasks. Furthermore, while current VLAs attempt to achieve task generalization by covering a large library of language-conditioned motion primitives, this approach is fundamentally constrained by the impracticality of capturing the vast amount of possible physical interactions and motions with a fixed set of episode-level language-conditioned tasks. In contrast, video-based world models learn from every consecutive frame pair in the data, while also leveraging large-scale video pretraining to understand physical dynamics.

### Video Model-based Robot Policies

Video Generation in Robotics. Prior works show that video generation models can be used to synthesize robot trajectories and extract executable actions at test-time through various approaches: inverse-dynamics models, optical flow as dense correspondence, or trajectory prediction as high-level planning. Other works generate human videos---either with 3D tracking or for novel scenes and motions ---and train policies using point tracking objectives. Most recently, demonstrated that video generation models can produce synthetic robot data for unseen behaviors in novel environments, leveraging the strong generalization capabilities of these models.

Joint Video and Action Generation. Another line of work couples video and action generation for end-to-end learning. These methods demonstrate that incorporating a world modeling objective alongside action prediction improves multi-task performance, sample efficiency, and generalization to novel scenes and objects. Previous work learns to do joint world modeling and action prediction from scratch or from VLAs, while more recent work leverages pretrained video diffusion models to inherit rich visual dynamics priors. We refer to these models collectively as World Action Models (WAMs) since they leverage world modeling capability (predicting the future state) for action prediction. We use the term World Action Models (WAMs) rather than Video Action Models (VAMs) to reflect that video is just one possible world modeling objective---future WAMs may align actions with other predictive modalities such as tactile sensing, force feedback, or learned latent representations. In contrast to prior WAMs, DreamZero systematically explores data diversity and scale to expose the full generalization potential of WAMs, adopts an autoregressive architecture better suited for long-horizon world--action modeling, achieves state-of-the-art generalization across both novel tasks and environments, and achieves state-of-the-art cross-embodiment tranfer, both learning from different embodiments (video only) and few-shot adaptation to a new embodiment.

Why WAMs. WAMs built upon video diffusion backbones inherit rich spatiotemporal priors from web-scale data, capturing the best of both paradigms: the seamless gradient flow of end-to-end VLAs and dense world modeling supervision for planning. Unlike latent world models, which learn dynamics from scratch in compact latent spaces, WAMs leverage pretrained video representations that already encode physical dynamics from internet-scale data. Central to this approach is learning the joint distribution of video and action---DreamZero simultaneously learns both modalities, with video prediction serving as an implicit visual planner that guides action generation. This formulation not only means that improving robotic capabilities reduces to improving video generation, but also enables three capabilities that elude current VLAs: zero-shot generalization to novel tasks, effective learning from heterogeneous robot data, and extremely efficient cross-embodiment transfer from videos. We provide further discussion about the differences between WAMs and alternative world model architectures (e.g., latent-space, 3D point cloud) in Appendix A.

Figure 4: Model Architecture of DreamZero. The model takes three inputs: visual context (encoded via a VAE), language instructions (via a text encoder), and proprioceptive state (via a state encoder). These are processed by an autoregressive DiT backbone using flow matching, which jointly predicts future video frames and actions through separate decoders. During training (left), for each chunk, the model denoises noisy video and action latents conditioned on clean video context. During inference (right), predictions are executed asynchronously in the real world, and ground-truth observations are fed back into the KV cache to prevent error accumulation.

## DreamZero

Pretrained video diffusion models offer rich spatiotemporal priors from web-scale data, making them attractive backbones for robot policies. However, converting these models into effective World Action Models (WAMs) presents three key challenges: Video-action alignment: jointly predicting video and actions requires tight coupling between visual futures and motor commands, yet naively combining separate video and action heads can lead to misalignment; Architectural design: it remains unclear whether bidirectional or autoregressive architectures are better suited for WAMs, with implications in modality alignment, error accumulation, and inference efficiency; and Real-time inference: video diffusion models require iterative denoising across high-dimensional latent spaces, making them prohibitively slow for closed-loop control.

DreamZeroaddresses these challenges through three design choices. First, we train a single end-to-end model that jointly denoises video and action with a shared objective, ensuring deep integration between modalities. Second, we adopt an autoregressive architecture and exploit the closed-loop setting: after each action chunk is executed, we replace predicted frames with ground-truth observations in the KV cache, eliminating compounding errors while enabling efficient inference via KV caching and preserving native frame rates for precise modality alignment (See right side of Figure 4). Third, we introduce a suite of system-, implementation-, and model-level optimizations that achieve a 38$\times$ inference speedup, enabling real-time control at 7Hz. We detail the model architecture in Section 3.1 and real-time execution in Section 3.2.

### Model Architecture

Problem Formulation. DreamZero jointly predicts video $\mathbf{o}_{l:{l + H}}$ and actions $\mathbf{a}_{l:{l + H}}$ conditioned on language instruction $\mathbf{c}$, proprioceptive state $\mathbf{q}_{l}$ and visual observation including the current and the past history $\mathbf{o}_{0:l}$ where $H > 0$ is a fixed horizon and $l$ is a random index sampled from a trajectory. Note that joint prediction of video and action is a decomposition of autoregressive video prediction and action prediction from an inverse-dynamics model (IDM):

Instead of using two separate models (video prediction model and inverse dynamics model) to model the decomposed objective, we train a single model end-to-end with joint prediction objective. We believe that this end-to-end design enables better video-action alignment through a deep integration between the two modalities. Since pretrained video models are already optimized on the video prediction objective on diverse web-scale video data, DreamZero only needs to additionally learn to predict videos for the robot embodiment videos and extract corresponding actions from the generated videos. We further hypothesize that this encourages better generalization than the conventional practice of training VLA from VLM, as our approach explicitly learns temporal dynamics from video frames used both as conditioning inputs and prediction targets.

Model Architecture. The model architecture is shown in Figure 4. To retain the generalization capability of video models, we introduce minimal additional parameters: state encoders, action encoders, and decoders. For robot training data that contains multiple views, we concatenate all views into a single frame instead of making architectural changes to the backbone model.

In particular, DreamZero is trained to predict video frames and corresponding actions autoregressively. Autoregressive generation possesses the following advantages: it enables faster inference speed by utilizing KV-cache, the policy model can leverage the visual observation history as guidance for the next generation, and it avoids the modality alignment challenges (video, action, and language alignment) inherent to bidirectional models. Concretely, bidirectional diffusion typically requires processing fixed-length sequences, which often necessitates video subsampling that distorts native FPS, potentially harming video-action alignment. On the other hand, autoregressive generation leverages KV caching to support arbitrarily long contexts within a single forward pass. This preserves the native frame rate, ensuring precise alignment between video frames and robot actions. Some details illustration of this difference is provided in Appendix B.

We introduce autoregressive modeling only for the video modality to avoid error propagation coming from closed-loop action prediction. DreamZero is trained to predict video frames in a chunk manner; each chunk has a fixed number of latent frames $K$ to match the action horizon. Chunk-wise generation enables training on variable length of videos, similar to how LLMs are trained on variable length of language tokens. We provide more details on the QKV attention masking strategy for the different modalities in Appendix C.

Training Objective. Similar to recent video diffusion models and VLAs, we employ flow-matching as the training objective. Unlike recent WAMs, DreamZero shares the denoising timestep between video and action modality for faster convergence at the beginning of training. Also, we apply teacher forcing as a training objective; the model is trained to denoise the noisy current chunk conditioned on the clean previous chunks.

Formally, given a chunk index $k > 0$ and the denoising timestep $t_{k} \in {\lbrack 0,1\rbrack}$, we denote the corresponding noisy video latent vector for original video $\mathbf{o}^{k}$ as $\mathbf{z}_{t_{k}}^{k}$ and noisy normalized actions as $\mathbf{a}_{t_{k}}^{k}$. All frames within the same chunk share the same timestep $t_{k}$, while different chunks are assigned independent timesteps. Our model denoises $\mathbf{z}_{t_{k}}^{k}$ and $\mathbf{a}_{t_{k}}^{k}$, defined as linear interpolations between clean vectors and random Gaussian noises:

where ${\mathbf{z}_{0}^{k} \sim {\mathcal{N}{(\mathbf{0},\mathbf{I})}}},{\mathbf{a}_{0}^{k} \sim {\mathcal{N}{(\mathbf{0},\mathbf{I})}}}$, and $\mathbf{z}_{1}^{k}$ and $\mathbf{a}_{1}^{k}$ are a clean video latent vector and a normalized action, respectively. Thus, the clean context from the previous chunks can be denoted as $\mathcal{C}_{k} = {\{{(\mathbf{z}_{1}^{j},\mathbf{a}_{1}^{j})}\}}_{j = 1}^{k - 1}$.

We train the model $\mathbf{u}_{\theta}$ to predict the joint velocity for both modalities using the following flow-matching objective:

where ${w{(t_{k})}} > 0$ is a predefined weight function for $t_{k}$, $\mathbf{c}$ is the text condition, $\mathbf{q}_{k}$ is the proprioceptive states of $k$-th chunk, and the velocity $\mathbf{v}^{k} ≔ {{\lbrack\mathbf{z}_{1}^{k},\mathbf{a}_{1}^{k}\rbrack} - {\lbrack\mathbf{z}_{0}^{k},\mathbf{a}_{0}^{k}\rbrack}}$. To enable efficient training, we perform trajectory-level updates and apply attention masking (e.g., see Figure 14 for details) so that the current noisy chunk can attend to clean context of previous chunks. We provide the pseudo-code in Algorithm 1.

Model Inference. As shown in Figure 4, during inference, DreamZero jointly denoises video and action chunks, leveraging KV caching for efficiency. Unlike pure video generation, our closed-loop setting allows ground-truth observations to replace generated frames in the KV cache after each action execution (see Figure 14). This eliminates the compounding error problem inherent to autoregressive video generation---a key advantage unique to WAMs. Moreover, as a stateful policy, DreamZero can leverage visual history for tasks requiring memory.^22^2In this work, we do not explicitly evaluate or post-train DreamZero on tasks that can only succeed with memory. We leave this for future work.. We provide the pseudo-code of inference in Algorithm 2

### Real-time Execution of DreamZero

Diffusion-based WAMs inherit powerful generalization from video foundation models, but their iterative denoising process creates a fundamental tension with reactive robotic control. We address two questions: What prevents WAMs from being reactive policies? How do we resolve this for real-time control?

### The Reactivity Gap

Reactive policies must respond to environmental changes within tens of milliseconds. A naive implementation of DreamZero on a single GPU requires approximately 5.7 seconds per action chunk due to three bottlenecks: iterative denoising across 16 diffusion steps required for smooth actions, the computational cost of a 14B parameter DiT backbone, and sequential execution that blocks robot motion during inference. This latency makes closed-loop control infeasible.^33^3One might expect that generating only actions (not video) would accelerate inference, but at 14B scale we empirically found out that the speed gain is minimal---the number of diffusion steps and the number of DiT blocks dominate latency. Moreover, because video and action are jointly trained for strong cross-modal alignment, naively reducing action denoising steps degrades quality. This motivates DreamZero-Flash.

### Asynchronous Closed-Loop Execution

Our first step towards resolving this is through asynchronous execution that decouples inference from action execution. Rather than waiting for each inference to complete, the motion controller continuously executes the most recent action chunk while inference runs concurrently on the latest observation. This structure transforms the latency constraint from "inference must complete before the robot moves" to "inference must complete before the current action chunk expires." In our experiments, we deploy policies at an action horizon of 48 steps at 30Hz control frequency (1.6 seconds per chunk) for bimanual manipulation robots. Hence, we target inference latency below approximately 200ms to ensure sufficient overlap for smooth, reactive control.

### System-level Optimizations

Given the asynchronous execution structure, we optimize inference throughput through parallelism and caching.

CFG Parallelism. Classifier-free guidance requires two forward passes (conditional and unconditional). We distribute these across two GPUs, reducing per-step latency by 47%.

DiT Caching. We exploit the directional consistency of velocity predictions during flow matching. When cosine similarity between successive velocities exceeds a threshold, we reuse cached velocities, reducing effective DiT steps from 16 to 4 with minimal quality loss on action prediction.

### Implementation-level Optimizations

We further reduce latency through compiler and kernel enhancements.

Torch Compile and CUDA Graphs. We apply torch.compile with CUDA Graphs to eliminate CPU overhead and fuse operators. Static shapes cause recompilations only during the first trajectory.

Post-Training Quantization. On Blackwell architecture, we quantize weights and activations to NVFP4 while keeping sensitive operations (QKV, Softmax) in FP8 and non-linear operations .

Kernel and Scheduler Enhancements. We use the cuDNN backend for attention and migrate scheduler operations to GPU to eliminate CPU-GPU synchronization stalls.

Figure 5: Decoupled Noise Schedules. DreamZero (blue) uses coupled noise for video and action (both uniform). DreamZero-Flash (red) biases video toward high-noise states via a Beta distribution while keeping action noise uniform, training the model to predict clean actions from noisy visual context.

### Model-level Optimizations: DreamZero-Flash

Even with system optimizations, the number of diffusion steps remains the primary latency bottleneck. However, naively reducing steps degrades action quality because residual visual noise propagates into action predictions.

DreamZero-Flash addresses this by decoupling video and action noise schedules during training. The key insight is that, at inference time, actions should denoise to their final values while being conditioned on a still-noisy video representation within the current chunk, since with very few denoising steps (e.g., fewer than 4), the generated video tokens may remain inaccurate and thus provide a noisy conditioning signal. Standard DreamZero samples a shared timestep $t_{k} \sim {\mathcal{U}{}}$ for both modalities. This creates a train-test mismatch: during training, the model learns to predict actions when video and action are at the same noise level, but few-step or single-step inference requires predicting clean actions while video remains partially noisy.

DreamZero-Flash closes this gap by biasing video timesteps toward high-noise states via $t_{k}^{\text{video}} = {1 - \eta}$, where $\eta \sim {\text{Beta}{(\alpha,\beta)}}$ with $\alpha > \beta$. In practice, we use $\text{Beta}{}$ as an example configuration, yielding ${{\mathbb{E}}{\lbrack t_{k}^{\text{video}}\rbrack}} = 0.125$ (predominantly noisy), while action timesteps remain uniform (Figure 5). During training, this exposes the model to configurations where it must predict clean actions from noisy visual context, directly matching the few-step or single-step inference regime. As a result, we reduce the diffusion steps from four to one, cutting inference from $\sim 350$ms to $\sim 150$ms with minimal performance loss (Table 3). Moreover, the Flash formulation enables flexible training configurations---such as varying the noise sampling ratios of video and action---to better align training with different few-step or single-step inference regimes. In practice, we mainly apply Flash training as the final stage following the main DreamZero model training.

Action Chunk Smoothing. To suppress high-frequency noise in generated actions, we upsample chunks to $2 \times$ resolution, apply a Savitzky-Golay filter, and downsample to original resolution.

### Summary

Table 1 summarizes cumulative speedups. System and implementation optimizations yield $\sim 9 \times$ speedup on H100 and $\sim 16 \times$ on GB200; adding DreamZero-Flash achieves 38$\times$ on GB200, reducing latency from 5.7s to 150ms. With the exception of DiT caching and quantization, all system and implementation-level optimizations are mathematically equivalent to baseline and show no measurable performance degradation.

+ Torch Compile + CUDA Graphs

+ Kernel &amp; Scheduler Opts.

Table 1: Cumulative inference speedups. Each row includes all optimizations above it. Entries marked “—” indicate features not applicable to that hardware.

## Experimental Setup

We validate our main hypotheses about learning from diverse data on two robot embodiments: the AgiBot G1 mobile bimanual manipulator and the Franka single-arm robot. We pretrain separately for each embodiment, leaving multi-embodiment training for future work. For cross-embodiment experiments, we utilize both the YAM robot and human egocentric data. The experimental setup for AgiBot G1 is illustrated in Figure 7.

We compare against two state-of-the-art Vision-Language-Action models (VLAs): GR00T N1.6 and $\pi_{0.5}$. For each baseline, we evaluate two initialization strategies: from-scratch, using pretrained VLM weights without prior robot data training for a fair apple-to-apple comparison with DreamZero, and from-pretrained, using official checkpoints pretrained on thousands of hours of cross-embodiment robot data. Both variants are then trained on identical data as DreamZero: $\sim 500$ hours of teleoperation data we collected for AgiBot G1, and DROID for Franka. We keep the compute budget comparable across all methods by matching total batch size and gradient steps.^44^4For from-pretrained baselines, this constitutes continual training on top of the official weights.

(a) Episode Duration Distribution

(b) Subtask Count Distribution per Episode

Figure 6: Distribution statistics for the AgiBot pretraining corpus: episode durations, subtask density, and skill coverage across 7.2K episodes (∼500 hours).

### Pretraining

Data. Our data collection philosophy differs from that of existing VLAs. While recent works have shown that VLAs can learn effective policies from moderate-sized datasets, these approaches typically rely on structured, task-focused demonstrations to ensure consistent behavior. We hypothesize that learning to only predict actions without encoding the knowledge about future world states makes it challenging to leverage highly heterogeneous, non-repetitive data effectively, as the model must implicitly infer dynamics from noisy state-action pairs. In contrast, we hypothesize DreamZero's world modeling objective enables effective learning from diverse demonstrations, allowing us to prioritize breadth and utility over repetition during data collection.

Using AgiBot G1, we collect approximately 500 hours of teleoperation data across 22 unique environments (see Figure 15), including homes, restaurants, supermarkets, coffee shops, and offices---prioritizing task diversity and real-world utility over task-specific repetition. As shown in Figure 6, each episode averages around 4.4 minutes and encompasses approximately 42 subtasks---significantly longer-horizon than typical robotic manipulation datasets. The skill distribution reflects real-world deployment requirements: navigation enables movement between workspaces, while torso adjustments allow interaction with objects at varying heights (shelves, cabinets). Additional details on the data collection pipeline are provided in Appendix E.^55^5We plan to open-source this dataset in upcoming releases. Some samples can be found at

We also validate DreamZero on the Franka single-arm robot using DROID, one of the most heterogeneous publicly available robotic datasets to demonstrate the effectiveness of WAMs on diverse, open-source data and enables reproducibility prior to the release of our in-house AgiBot dataset. We open-source the checkpoint and inference code to run some DROID-sim evals in PolaRiS.^66^6Available at

Training. We use Wan2.1-I2V-14B-480P, a 14B image-to-video diffusion model, as the backbone for DreamZero. We train for 100K steps with a global batch size of 128 for AgiBot and 100K steps with a global batch size of 128 for DROID datasets. We update all DiT blocks, the state encoder, action encoder, and action decoder, while freezing the text encoder, image encoder, and VAE.^77^7We experimented with LoRA but found it led to suboptimal results. For both datasets, we filter out idle actions and use relative joint positions as the default action representation. We also conduct some ablations (Section 5.2) where we initialize from Wan2.1-I2V-5B-480P to see the effect of model size (5B vs. 14B).

Figure 7: AgiBot Evaluation Set-up. We are first-citizens of generalization evals, where the default setting is unseen environment and unseen objects.

Evaluation Protocol. We evaluate models out of the box after pretraining. Our default evaluation setting is unseen environments, unseen objects---because our pretraining and post-training data were collected in a different geographic location from our evaluation sites, every benchmark inherently tests out-of-distribution generalization rather than interpolation within the training distribution. We evaluate on two categories: seen and unseen tasks. We define the granularity of a task as a combination of the motion required for the task and the object type. For example, if the training data contains folding a red-colored shirt and evaluate the model to fold a black-colored shirt with a different size, it is considered as a seen task. On the other hand, if we evaluate the model to fold socks, it is considered as an unseen task because the motion required to fold socks is different from folding a shirt (See samples in Figure 7).

AgiBot Evaluation Protocol. For seen tasks, we select 10 tasks from the pretraining distribution, including pick-and-place variants, stacking, wiping, and folding; we run 8 rollouts per task across 4 robots, each in different environments and different objects (80 rollouts total per checkpoint). We divide 10 seen tasks into three categories: PnP-Easy (Pick and place fruit, Wipe the mess, Take out fruit from bag), PnP-Hard (Pick and place fork/spoon, put the pen in pen holder, put the cup on the coaster, stack bowls/cups in a row), and Contact-Rich Manipulation (fold shirts, fold shorts, stack clothes). For unseen tasks, we evaluate 10 tasks absent from training---such as ironing, painting, pulling carts, cube stacking, removing a hat from a mannequin, and untying shoe laces---with 8 rollouts per task across 4 robots (80 rollouts total per checkpoint). The full list of each evaluation rollout initial frame and prompt is provided in Appendix F, and some evaluation rollouts can be found here.^88^8 for main evaluation rollouts and for accumulation of unique evaluation rollouts.

DROID Evaluation Protocol. We evaluate on 20 seen tasks and 20 unseen tasks (verbs absent from DROID), performing 2 rollouts per task, for a total of 80 evaluation rollouts across 40 tasks for each checkpoint. We compare DreamZero against the publicly released $\pi_{0.5}$-DROID and an internally trained GR00T N1.6-DROID checkpoint. Object positions are fixed across checkpoints to ensure fairness. Each rollout is scored from 0 to 1.0 based on partial task completion; full details are provided in Appendix G.

### Post-training

Beyond pre-training, we evaluate whether WAMs improve fine-tuning performance on task-specific data using the AgiBot robot.

Data. We collect post-training data on three downstream tasks:

Shirt folding (33 hrs): Fold a flattened t-shirt through 5 sequential stages. We randomize initial shirt position across 2 shirt types.

Fruit packing (12 hrs): Pack 10 fruits from a table into a bag. We randomize fruit combinations and positions of fruits and bag.

Table bussing (40 hrs): Clear 5 pieces of trash into a trash bin and 5 pieces of dishware (dish, bowl, fork, and spoon) into a dish bin. We randomize object types, combinations, and positions.

Training. We post-train for 50K steps per task. As in pretraining, we update all parameters except the text encoder, image encoder, and VAE.

Evaluation Protocol. We measure average task progress across 10 rollouts per task. Task progress is defined as: folding stages completed out of 5 for shirt folding, fruits successfully packed out of 10 for fruit packing and items cleared for table bussing. Following Barreiros et al., we apply an image overlay to the initial scene to reduce variance.

## Experimental Results

### Main Results

Figure 8: Seen Task Evaluation. DreamZero effectively learns from diverse data and generalizes to new environments, outperforming VLAs across all task categories. VLAs trained from scratch achieve near-zero success, while pretrained VLAs show modest performance—likely benefiting from embodiment-specific knowledge acquired through repetitive demonstrations during pretraining.

We evaluate the zero-shot generalization performance of DreamZero compared to baseline models and investigate the following research questions:

### Q1. Do WAMs learn better from diverse, non-repetitive data?

We evaluate pretrained models out-of-the-box on tasks present in the pretraining data, but in zero-shot environments with unseen objects. Results are shown in Figure 8.

On AgiBot G1, from-scratch VLAs achieve near-zero task progress score across all categories. Even on simple pick-and-place tasks (PnP Easy), VLAs occasionally reach toward the correct object but fail to interact accurately with unseen objects in novel environments. In contrast, DreamZero successfully learns from heterogeneous data, achieving 62.2% average task progress---over 2$\times$ higher than the best pretrained VLA baseline (27.4%), despite those baselines being pretrained on thousands of hours of cross-embodiment robot data before continued training on our data mix. On DROID-Franka, we show a similar result as well; DreamZero which is only trained on the DROID dataset outperforms pre-trained baseline models trained on multiple robot embodiment data.

We attribute this gap to the joint video-action formulation: while VLAs require massive robot data to learn direct observation-to-a ction mappings, WAMs leverage video generation as a strong prior for action prediction, enabling effective learning of diverse data and generalization to unseen environments. Notably, we observe tight alignment between generated videos and real-world execution, even for suboptimal behaviors (Figure 16). Most DreamZero failures stem from video generation errors rather than action prediction---the policy faithfully executes whatever trajectory the video predicts. This suggests that improvements to the video backbone would directly translate to better WAM performance.

Figure 9: Zero-shot Generalization to Unseen Tasks. DreamZero achieves non-trivial task progress on 10 tasks absent from training, while VLAs struggle across both embodiments.

### Q2. Do WAMs generalize to unseen tasks?

Figure 9 evaluates generalization to 10 tasks entirely absent from the pretraining distribution, including untying shoelaces, ironing, painting with a brush, and shaking hands.

On AgiBot G1, from-scratch VLAs achieve near-zero task progress ($< {1\%}$), while DreamZero reaches 39.5% on average---with strong performance on tasks like "Remove Hat from Mannequin" (85.7%) and "Shake Hands" (59.2%). DreamZero also significantly outperforms pretrained VLA baselines (39.5% vs. 16.3%), even though those baselines may have encountered some of these tasks during cross-embodiment pretraining. Also on the DROID-Franka setup, DreamZero significantly outperforms (49% task progress, 22.5% success rate) other pretrained baselines (31% task progress, 12.5% success rate for GR00T N1.6 and 33% task progress, 7.5% success rate for $\pi_{0.5}$).

Qualitatively, we observe that pretrained VLAs often reach toward objects and attempt grasping regardless of the instruction, suggesting they overfit to dominant training behaviors (e.g., pick-and-place) rather than understanding novel task semantics, accounting for their partial task progress despite failing to complete the intended tasks. In contrast, DreamZero performs visual planning for unseen tasks and executes them successfully, with strong alignment between generated videos and real-world actions.

Beyond structured evaluation, we conduct free-form testing on over 100+ additional tasks, including "Pop the ballon" and "Press elevator button", by doing free-form prompting with verbal instructions.^99^9Rollouts of these tasks are provided in

Figure 10: Posttraining Results. WAMs enable stronger post-training results across three tasks, indicating that environment generalization of DreamZero is retained after post-training.

### Q3. Do WAMs improve post-training performance?

We investigate whether WAMs retain their generalization even after fine-tuning on task-specific data. Figure 10 shows results on three tasks with varying distribution diversity.

DreamZeromatches or outperforms VLA baselines across all tasks: comparable performance on shirt folding and table bussing while significantly outperforming on fruit packing. Similar to the findings from Figure 8 and Figure 9, from-scratch baselines fail to learn accurate motions to grasp the target objects; this means that from-scratch VLAs tend to overfit to the training data and fail to generalize to scenarios where we vary the table height, table distance, objects, and object placements, mostly due to the evaluation site being in a different geographic location (see Figure 7 for samples). Although pretraining on multiple robot embodiments with repetitive data largely boosts the post-training genearlization performance for pretrained baselines, DreamZero still matches or outperforms pretrained VLA baselines without cross embodiment pretraining. Since we still evaluate on unseen environments for post-training, this implies that the environment generalization of DreamZero is retained after post-training.

### Q4. Do WAMs enable strong cross-embodiment transfer to unseen tasks?

Having shown that WAMs generalize to unseen tasks (Figure 9), we now investigate whether this generalization can be further improved by leveraging video data from different embodiments performing the same tasks. Crucially, we use only the video prediction objective for the cross-embodiment data (no actions), while maintaining the joint video-action objective for the AgiBot pretraining data; the cross-embodiment data thus serves as additional visual experience to strengthen the world model's understanding of task dynamics and expected behavior.

Figure 11: Cross-Embodiment Transfer. We explore robot-to-robot (YAM → AgiBot) and human-to-robot embodiment transfer to unseen tasks.

We explore two settings (Figure 11): Robot-to-robot transfer using the bimanual YAM robot, and Human-to-robot transfer using egocentric human demonstrations. For each setting, we collect 72 multi-view trajectories of the 9 unseen tasks (8 demonstrations per task, 20 minutes for YAM, 12 minutes for human).^1010^10We exclude Pulling Cart task since data collection through teleoperation was infeasible with our bimanual YAM robot setup. We then co-train from the DreamZero-AgiBot checkpoint on a 1:1 mix with pretraining data for 10K steps.

Results on the 9 unseen tasks (Table 2) show that both transfer settings improve performance over the baseline DreamZero. Robot-to-robot transfer yields the largest gain (38.3% $\rightarrow$ 55.4%), likely due to the narrower embodiment gap; both YAM and AgiBot are bimanual parallel grippers. Human-to-robot transfer also improves performance (38.3% $\rightarrow$ 54.3%), despite the larger morphological gap and dynamic egocentric viewpoints.

DreamZero + Human2Robot Transfer

DreamZero + Robot2Robot Transfer

Table 2: Cross-Embodiment Transfer Results. Average task progress on unseen tasks (± standard error). Both transfer settings improve over baseline (result from Table 9) using only 10–20 minutes of video-only demonstration data.

These results point to a promising property of WAMs: unlike recent VLA approaches to embodiment transfer, our method relies solely on visual information without action labels. While current success rates remain moderate, the consistent improvement from just 10--20 minutes of video-only data provides an early signal that cross-embodiment visual experience transfers meaningfully. This opens a potential scaling pathway: abundant human video data---orders of magnitude larger than robot datasets---could enable WAMs to acquire diverse skills without action annotation, pending further research into strengthening the transfer mechanism.

### Q5. Do WAMs enable few-shot new embodiment adaptation?

Figure 12: Few-shot Embodiment Adaptation. We explore few-shot embodiment adaptation by post-training on 30 minutes of new embodiment play data and evaluating on pick-and-place variants requiring strong language following.

We post-trained the DreamZero-AgiBot checkpoint on a new bimanual manipulator (YAM robot) using only 55 trajectories across 11 unique tasks ($\sim$`<!-- -->`{=html}30 minutes of data).^1111^11We visualize the entire 30 minutes of play data As illustrated in Figure 12, despite limited data and diversity, the post-trained policy retains strong language following ability, even generalizing to novel objects unseen during training, including pumpkins, teddy bears, pens, cup noodles, and paper bags. Even with minimal data, we observe tight video-action alignment, demonstrating very efficient cross-embodiment transfer.

We hypothesize that two factors enable this efficiency: the visual similarity of AgiBot G1 and YAM embodiment (both equipped with bi-manual parallel grippers), and more fundamentally, learning an implicit IDM from predicted videos may be inherently more sample-efficient than direct policy learning---the model only needs to learn the mapping from visual futures to actions, while leveraging the pretrained video model's existing understanding of physical dynamics. Consistent with our AgiBot findings, failures primarily stem from video prediction errors rather than action extraction, suggesting that increasing task diversity during post-training could further improve performance.^1212^12In this specific post-training experiment, we only utilized 11 short, global language annotations unique for each task. We hypothesize diversifying the language can also enable stronger tranfer, but leave further investigation to future work.

### Q6. Does DreamZero-Flash maintain performance with fewer denoising steps?

We evaluate whether DreamZero-Flash can maintain task performance under aggressive single-step denoising. As shown in Table 3, reducing DreamZero from 4 denoising steps to 1 step drops task progress substantially (83% $\rightarrow$ 52%) on the table bussing task. In contrast, DreamZero-Flash achieves a higher average success rate (74%) at single-step inference, sitting only 9% below the 4-step baseline while being $\sim 2 \times$ faster. This suggests that decoupled noise scheduling offers a more effective speed--accuracy trade-off for real-time deployment.

Table 3: DreamZero-Flash Evaluation. Task progress on table bussing with varying denoising steps (± standard error). DreamZero-Flash recovers most of the 4-step performance using only 1 denoising step.

### Model and Data Ablations

We conduct ablations to isolate the contributions of data diversity, model scale, and architecture. Due to computational constraints, all ablation models are trained with 50K steps and batch size 32, and evaluated on PnP Easy tasks for consistent comparison.

Table 4: Model and Data Ablations. Task progress on PnP Easy tasks (± standard error). AR = autoregressive, BD = bidirectional. All models trained with 50K steps and batch size 32.

### Q1. Does data diversity improve generalization?

We compare DreamZero trained on 500 hours of diverse data versus 500 hours of repetitive data, where the latter contains 70 tasks with many repeated demonstrations per task using similar object positions and configurations. As shown in Table 4, diverse data substantially improves generalization (33% → 50%), even on simple pick-and-place tasks. We hypothesize this reflects WAMs' learning dynamics: since video prediction is largely inherited from pretraining, the key challenge is learning inverse dynamics. A robust IDM requires diverse state-action correspondences across varied contexts, which repetitive data inherently lacks.

### Q2. Does WAM performance scale with model size?

For VLAs, scaling model size improves semantic reasoning but not necessarily action prediction. We find that WAMs exhibit clearer scaling behavior: the 14B model significantly outperforms the 5B model (50% vs. 21%), with the smaller model prone to visual hallucinations that propagate to erroneous actions.

To ensure fair comparison, we also scale VLA baselines to match DreamZero's size by initializing from 8B and 32B pretrained VLMs, truncating to the first half of the transformer blocks, and attaching DiT-based action modules following Bjorck et al.. As shown in Table 4, larger VLAs still fail to learn from diverse data (0% task progress), often hovering near objects without making contact. This suggests that scaling model capacity alone does not address VLAs' difficulty with diverse data distributions.

### Q3. Does autoregressive architecture outperform bidirectional?

We compare DreamZero's autoregressive (AR) architecture against a bidirectional (BD) variant. While task progress is similar (Table 4), the AR model produces substantially smoother motions---backpropagating through entire action sequences enables better temporal consistency. Additionally, AR inference is 3--4$\times$ faster due to KV caching.

## Discussion and Future Work

Scaling Laws of WAMs. We have identified that leveraging larger video backbone model and training on diverse data boosts downstream performance in Table 4. However, we still have lacking evidence for scaling laws for robot foundation models, specifically for WAMs. Similar to scaling laws for language models, scaling laws for WAMs depending on the model size, dataset size, and the training compute need to be explored to determine the optimal configuration to extract the maximal capability of WAMs. We expect that the tendency of scaling WAMs to be different from VLAs, showing a more direct scaling law for actions. We leave deep investigation on scaling laws for WAMs as future work.

Learning from In-the-wild Human Data. Although we have investigated leveraging egocentric human data to boost the performance on unseen tasks (Section 5), our experiments are still constrained to small scale in-lab data (only 12 minutes). Recently, a large amount of human video data has been released that has more diverse distribution compared to robot data. Since WAMs are pretrained on diverse internet video data, we hypothesize that leveraging large-scale egocentric human video data that are related to robot manipulation tasks would lead to stronger transfer to downstream robot tasks compared to current VLAs. We leave this direction as future work.

Faster Inference. Through model and system optimizations, we enable DreamZero to run at 7Hz using 2 GB200s. However, compared to current VLAs which runs up to over 20Hz on consumer GPUs, DreamZero is still computationally expensive due the large parameter size and the iterative denoising nature of video models. In the future, if smaller video backbone models also have strong generalization capability, WAMs could potentially be utilized as a real-time System 1 model on a lightweight edge device.

Long-horizon Reasoning. Current DreamZero architecture functions primarily as a System 1 model. Although DreamZero has a concept of visual memory, it is currently short-horizon (6 seconds). Robust long-horizon execution will require either a System 2 planner or WAMs with significantly extended context windows. For the former, both modular dual-system architectures and unified approaches offer promising directions. For the latter, techniques from video-based world models that maintain coherent generation over extended horizons could be adapted to expand WAM context length.

High-Precision Tasks. While DreamZero generalizes broadly across tasks and environments, it inherits limitations common to behavior cloning on tasks requiring sub-centimeter precision, such as key insertion or fine assembly. Our diverse pretraining strategy prioritizes breadth, which may underrepresent the dense demonstrations needed for these high-precision manipulation. That said, recent work showed promising results that WAMs may actually hold an advantage for high-precision manipulation tasks with millimeter tolerance, an encouraging signal that the trade-off between broad generalization and fine-grained dexterity may be reconcilable with further investigation.

Embodiment Design for WAMs. We hypothesize two key factors will shape the best robot embodiments for future WAM development: Degrees of freedom: Higher-DOF robots will require more play data to learn an accurate implicit IDM, as the mapping from visual futures to motor commands grows combinatorially with kinematic complexity. Quantifying the accuracy of implicit IDMs remains a challenge. Human similarity: Embodiments that more closely resemble humans---particularly humanoids with dexterous manipulation capabilities---may transfer more efficiently despite higher DOF, as they can leverage both the motion priors from video pretraining and the massive scale of human egocentric videos. These factors pull in opposite directions---yet human-like embodiments may win out by trading mechanical simplicity for access to web-scale human data---the fuel for next-generation robot foundation models.
