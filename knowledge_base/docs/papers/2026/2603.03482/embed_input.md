<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Beyond Pixel Histories: World Models with Persistent 3D State

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Interactive world models continually generate video by responding to a user's actions, enabling open-ended generation capabilities. However, existing models typically lack a 3D representation of the environment, meaning 3D consistency must be implicitly learned from data, and spatial memory is restricted to limited temporal context windows. This results in an unrealistic user experience and presents significant obstacles to downstream tasks such as training agents. To address this, we present PERSIST, a new paradigm of world model which simulates the evolution of a latent 3D scene: environment, camera, and renderer. This allows us to synthesise new frames with persistent spatial memory and consistent geometry. Both quantitative metrics and a qualitative user study show substantial improvements in spatial memory, 3D consistency, and long-horizon stability over existing methods, enabling coherent, evolving 3D worlds. We further demonstrate novel capabilities, including synthesising diverse 3D environments from a single image, as well as enabling fine-grained, geometry-aware control over generated experiences by supporting environment editing and specification directly in 3D space.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Interactive world models aim to generate experiences that unfold over time in response to user actions, enabling a new class of photo-realistic, personalised, and immersive interactive experiences for human users (kanervisto2025world; genie3; huang2025voyager). At the same time, such models hold significant potential for safely training embodied agents within simulators learned directly from data (hafner2025training; micheli2023transformers; alonso2024diffusion; garcin2024dred). Unlike passive video generation, interactive generation requires models to respond meaningfully to external interventions. In this setting, realism is not determined solely by per-frame visual quality, but by the degree to which the generated experience maintains persistent environments and stable dynamics throughout extended rollouts.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most existing approaches to interactive video generation rely on autoregressive (AR) models that condition on the history of past observations and actions to generate the most recent frame, often using diffusion-based transformers with causal attention (peebles2023scalable). This formulation is attractive: it naturally supports real-time action conditioning, allows generation to proceed indefinitely, and integrates cleanly with recent advances in large-scale video modelling. As a result, AR video diffusion models form the backbone of many recent neural game engines and interactive world models (chegamegen; he2025matrix; valevskidiffusion; zhang2025matrix; yu2025gamefactory).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, conditioning on high-dimensional visual observations is computationally expensive, and the number of prior frames that AR models can ingest is tightly constrained by hardware. In practice, this limits AR generation to condition on what amounts to only a few seconds of past footage, even when observations are compressed to lower spatial and/or temporal resolutions using learned autoencoders. As a result, a growing body of work has explored how best to populate this limited contextual window, most commonly through heuristic strategies that retrieve individual key frames from a memory bank of past observations (xiao2025worldmem; huang2025memory).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Yet, an inherent flaw of key-frame retrieval methods is that each pixel observation provides only partial, redundant, and viewpoint-dependent information about the world at a fixed point in time. As the memory bank grows, identifying the relevant past evidence becomes increasingly difficult. As a result, generating extended and coherent experiences within complex 3D environments remains an open challenge.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose to depart from pixel-based histories and substitute key frame retrieval with active key frame generation. We are inspired by traditional 3D simulators and game engines, which maintain coherence by directly rendering pixel frames from a persistent and dynamically evolving 3D state of the world. We introduce PERSIST, a framework that brings persistence to learned AR world models by tracking a dynamic 3D representation of the environment. We describe our framework in Figure 1. PERSIST decomposes world simulation into three coupled components: a world-frame model that predicts how a learned representation of a 3D scene evolves over time, a camera model that tracks the agent's viewpoint within this scene, and a world-to-pixel generation module that produces observations via differentiable projection and a learned rendering function.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Rather than treating pixels as the primary carrier of memory, PERSIST models the structure and dynamics of the environment in a latent 3D space. This persistent world representation captures how the scene evolves over time, while the camera acts as a query mechanism that extracts the subset of 3D information relevant to guide the generation of the current frame. This formulation enables long-horizon rollouts with fixed-cost memory, enforces geometric consistency by construction, and remains fully learned and compatible with modern diffusion and flow-based training objectives.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate PERSIST in a complex 3D environment and find that explicitly modelling persistent 3D dynamics leads to substantially improved long-horizon generation quality compared to rolling-window and memory-retrieval baselines. Our approach exhibits stronger temporal stability, improved spatial memory when revisiting previously observed regions, and markedly better 3D consistency overall. Beyond quantitative gains, persistent world representation enables new capabilities, including explicit 3D scene initialisation, mid-episode scene edits, and the emergence of off-screen dynamic processes that continue to evolve even when not directly observed.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Persistent Environment Representation", "weight": 1.0} -->

Learning an autoregressive model ${\mathcal{Q}}_{\theta}$ is often challenging when $\mathcal{E}$ is a complex 3D environment featuring high dimensional pixel observations. First, memory constraints limit ${\mathcal{Q}}_{\theta}$ to condition on a finite context window of past $K$ frames, which degrades temporal consistency once the generated episode exceeds this horizon. Second, pixel observations typically provide partial information about the environment's hidden state, making learning accurate transition dynamics challenging. One might therefore attempt to have ${\mathcal{Q}}_{\theta}$ condition on some approximation of the hidden state $s$; however $s$ can be arbitrarily complex or entirely unmeasurable. Even if $s$ were accessible, learning the observation function $\Omega\mathrel{\mathop{\ordinarycolon}}{\mathbb{S}}\rightarrow{\mathbb{O}}$ to recover observations can be a comparably challenging problem.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Persistent Environment Representation", "weight": 1.0} -->

For example, in the case of a video game, $s$ would be the program's dynamic memory contents, which may not be particularly helpful for easily recovering pixel observations.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Persistent Environment Representation", "weight": 1.0} -->

Instead, we define a proxy $\tilde{s}=\langle{\bm{w}},{\bm{c}}\rangle$, where ${\bm{w}}$ is a world-frame representing a fixed region of space centred on the agent, and ${\bm{c}}$ is a camera state encoding the agent's view within ${\bm{w}}$. Although not a perfect replacement for the true hidden state, $\tilde{s}$ is an effective modelling choice when $\mathcal{E}$ is a 3D environment, as it lets us: Simplify information retrieval. Figure 2 demonstrates how the world-frame ${\bm{w}}_{t}$ can function as a dynamic spatial memory module throughout the episode, while the camera state ${\bm{c}}_{t}$ acts as a spatial lookup key to retrieve the spatial information in ${\bm{w}}_{t}$ that is necessary to reconstruct ${\bm{o}}_{t}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Persistent Environment Representation", "weight": 1.0} -->

${\bm{c}}_{t}$ encodes the information to project this information to screen-space, without requiring explicit knowledge of the true observation function.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Persistent Environment Representation", "weight": 1.0} -->

Improve dynamics predictions. Tracking ${\bm{w}}$ and ${\bm{c}}$ over time facilitates modelling dynamics that are difficult to infer from pixel observations alone, such as interactions or collisions with out-of-view objects, or tracking how occluded regions of the environment change over time.

<!-- chunk {"id": "body-0015", "role": "body", "section": "PERSIST", "weight": 1.0} -->

We present PERSIST (Persistent Environment Representations for Simulating Interactive Space-Time), a world simulation framework for complex 3D environments. PERSIST decomposes the world simulation objective into the tasks of world frame prediction, camera prediction and world-to-pixel generation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "PERSIST", "weight": 1.0} -->

Dataset construction and pre-processing. The different components of PERSIST are trained from a dataset of trajectories collected from $\mathcal{E}$. A trajectory consists of a sequence of pixel observations $O$, actions $A$, world-frames $W$ and camera views $C$. In this work, we assume that $W$ and $C$ are directly obtainable from $\mathcal{E}$, the former as a 3D voxel grid within a cuboid centred on the agent, and the latter as a vector encoding the camera intrinsics and extrinsics. Actions are embedded as a 23-dimensional multi-hot encoding of key presses and discretised mouse movements. We train a 2D-VAE and a 3D-VAE to encode pixel- and world-frames into latent patches $\bar{{\bm{o}}}$ and $\bar{{\bm{w}}}$ of 10$\times$`<!-- -->`{=html}10 pixels and $4^{3}$ voxels respectively.

<!-- chunk {"id": "body-0017", "role": "body", "section": "World-Frame and Camera Prediction", "weight": 1.0} -->

World frame prediction. At each timestep, a new world-frame is generated by sampling where $K$ is the model's temporal context window and latents $\bar{W}^{t-1}_{t-K}$ and $\bar{O}^{t-1}_{t-K-1}$ are encoded using the VAEs. ${\mathcal{W}}_{\theta}$ is parametrised as a rectified flow model with a causal Diffusion Transformer (DiT) backbone (peebles2023scalable) employing interleaved spatial, temporal and cross-attention modules (decart2024oasis). We modify the spatial module to handle three spatial dimensions, and replace RoPE spatial embeddings (su2024roformer) with absolute position embeddings of the XYZ coordinates of the centroid of each voxel token. We keep the temporal module as-is. Actions and cameras are jointly embedded using a multi-layer perceptron (MLP).

<!-- chunk {"id": "body-0018", "role": "body", "section": "World-Frame and Camera Prediction", "weight": 1.0} -->

The resulting embeddings are added to the denoising timestep embedding and injected into each module via Adaptive Layer Normalisation (AdaLN) (peebles2023scalable). We concatenate pixel patches channel-wise with Plücker embeddings (xiao2025worldmem; sitzmann2021light) computed from $C^{t-1}_{t-K-1}$ to convey 3D projection information. The resulting patches are then injected into the model via the cross-attention module. Finally, we employ the 3D-VAE to decode $\bar{{\bm{w}}}_{t}$ to its native resolution.

<!-- chunk {"id": "body-0019", "role": "body", "section": "World-Frame and Camera Prediction", "weight": 1.0} -->

Crucially, ${\mathcal{W}}_{\theta}$ supports conditioning on $\bar{W}=\varnothing$, making it capable of generating the initial world frame ${\bm{w}}_{0}$ from initial condition $\langle{\bm{o}}_{0},{\bm{c}}_{0}\rangle$ at inference time. Thus, while we rely on $W$ to train ${\mathcal{W}}_{\theta}$, we do not have to rely on ground truth 3D conditioning during inference. We provide examples for each inference configuration in Figure 3.

<!-- chunk {"id": "body-0020", "role": "body", "section": "World-Frame and Camera Prediction", "weight": 1.0} -->

Camera model. At any given timestep, the cameras is represented as the 10-dimensional vector ${\bm{c}}=\langle\textbf{pos},\textbf{rot},\text{fov}\rangle$, where $\textbf{pos}\in{\mathbb{R}}^{3}$ encodes the camera's position in the world-frame, $\textbf{rot}\in{\mathbb{R}}^{6}$ its orientation as a 6D continuous rotation (zhou2019continuity), and $\text{fov}\in{\mathbb{R}}$ its field-of-view. The camera model predicts ${\bm{c}}_{t}={\mathcal{C}}_{\theta}(C^{t-1}_{t-1-K},W^{t}_{t-K},A^{t}_{t-K})$ using a 1D causal transformer backbone with RoPE temporal embeddings.

<!-- chunk {"id": "body-0021", "role": "body", "section": "World-Frame and Camera Prediction", "weight": 1.0} -->

Individual tokens are obtained by passing pos and rot through separate positional embedders, concatenating fov and applying a linear projection. $W$ is cropped to its inner-most $4^{3}$ voxels and embedded alongside $A$ via a joint MLP prior to AdaLN injection.

<!-- chunk {"id": "body-0022", "role": "body", "section": "World-Frame and Camera Prediction", "weight": 1.0} -->

inference time. The camera model is trained via MSE losses applied to each component of $\bar{{\bm{c}}}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "World-to-Pixel Generation", "weight": 1.0} -->

In order to condition the pixel-space generation on 3D information we need to form world-to-pixel correspondence.

<!-- chunk {"id": "body-0024", "role": "body", "section": "World-to-Pixel Generation", "weight": 1.0} -->

World projection. We project ${\bm{w}}$ to screen-space via the projection operator where $\tilde{{\bm{w}}}_{2D}\in\mathbb{R}^{h\times w\times l\times m}$ is a per-pixel depth-ordered list of $l$ voxel features with $m$ channels, indexed according to their position in screen space $\langle h_{i},w_{j}\rangle$. ${\bm{d}}\in\mathbb{R}^{h\times w\times l}$ is the linear depth of each voxel feature measured in camera space. We provide a visualisation of how $\mathcal{R}$ constructs $\tilde{{\bm{w}}}_{2D}$ and ${\bm{d}}$ in Figure 4. $\mathcal{R}$ employs the same $h,w$ screen dimensions as the pixel latents, ensuring pixel-level alignment with $\bar{{\bm{o}}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "World-to-Pixel Generation", "weight": 1.0} -->

Pixel frame prediction. Pixel frames are generated by sampling where ${W_{2D}}_{t-K}^{t}$ is obtained from the projection ${\mathcal{R}}(C_{t-K}^{t},W_{t-K}^{t})$. Here, ${\mathcal{P}}_{\theta}$ acts as a learned deferred shader (thies2019deferred) which additionally predicts information not provided by 3D latents (e.g. texture, lighting, particle effects, screen-space overlays,...). This choice allows ${\mathcal{P}}_{\theta}$ to learn arbitrary rendering functions, whilst encouraging spatial consistency through its dependency on ${\bm{w}}_{2D}$. ${\mathcal{P}}_{\theta}$ is parametrised as a rectified flow model with a causal DiT backbone employing interleaved spatial and temporal modules (decart2024oasis). Actions are embedded using a MLP and injected via AdaLN.

<!-- chunk {"id": "body-0026", "role": "body", "section": "World-to-Pixel Generation", "weight": 1.0} -->

${\bm{w}}_{2D}$ is projected to latent space via a channel-wise 1D-convolution and is incorporated to $\bar{{\bm{o}}}$ via channel-wise concatenation. Crucially, we assign more latent channels to ${\bm{w}}_{2D}$ than to $\bar{{\bm{o}}}$, in order to bias the model to use the 3D latent frame as its primary source of information.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Mitigating Exposure Bias", "weight": 1.0} -->

During training, the denoisers condition on latents encoded from the training data. However, they condition on autoregressive predictions at inference time, leading to exposure bias (ning2023elucidating). We train each denoiser with diffusion forcing (chen2024diffusion) to make them robust to the exposure bias induced by their own predictions. In addition, at inference ${\mathcal{W}}_{\theta}$ depends on latents predicted by ${\mathcal{P}}_{\theta}$, and vice-versa. To alleviate the resulting distributional shift, we apply a flat 10% random noise augmentation to $\bar{O}$ when training ${\mathcal{W}}_{\theta}$, and to $\bar{W}$ when training ${\mathcal{P}}_{\theta}$. This lets us train each component of PERSIST separately and combine them at inference time without any fine-tuning.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments", "weight": 1.0} -->

We conduct our experiments within Luanti (luanti2024), an open-source voxel-based game engine inspired by Minecraft.^33^3We prefer Luanti over Minecraft due to its open-source design and expressive Lua API, which facilitates data collection and experimentation. Voxel environments discretise 3D space into individual voxels, each voxel taking on any of thousands of possible configurations (e.g. water, stone, air, etc. ). These environments constitute a valuable research platform (malagon2025craftium; fan2022minedojo; guss2019minerl; baker2022video), as they instantiate interpretable, complex, diverse, and persistent 3D worlds with rich player--environment interactions. Unlike prior work that learns world models from data collected within a single game map (alonso2024diffusion; kanervisto2025world), we learn a broad distribution of procedurally generated worlds. Training world models within procedural environments substantially increases the difficulty of achieving spatial and temporal consistency, as the model cannot overfit to a fixed environment layout.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

Dataset. We use the Craftium platform (malagon2025craftium) to collect game data to train and evaluate our models. We collect $\sim$`<!-- -->`{=html}40M environment interactions consisting of player actions, camera states, pixel and 3D observations. Actions are represented as multi-hot vectors encoding individual key presses and discretised mouse movements. 3D observations are represented as a $48^{3}$ voxel grid centred on the agent. In Luanti, individual voxels contain semantic information about a specific spatial location, encoded as integer labels. In total, we collect $\sim$`<!-- -->`{=html}100K trajectories, amounting to 460 hours of gameplay recorded at 24Hz. To interact with the game, we employ a similar strategy as (yu2025gamefactory) and design a simple policy that randomly samples from a set of pre-defined action sequences.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

Training and Inference. All models are trained using the AdamW (loshchilov2018decoupled) optimizer with a learning rate of $1e-4$. We first train the VAEs and pre-encode the 3D and pixel latents to accelerate the training of the dynamic models. The pixel and 3D VAEs take 4 and 12 days to train using 8 A100 GPUs. We train two versions of the 3D denoiser, "3D-S" and "3D-XL", which uses 8$\times$ more spatial tokens. 3D-S takes 3 days to train on 8 H100 GPUs, while 3D-XL and the pixel denoiser each take 10 days. The camera model trains on a single A100 in 16 hours with batch size 256. All other models use batch size 64. Each model is trained separately and assembled in the full pipeline with no further fine-tuning. At inference, we use 20 denoising steps per-frame and slightly noise past context frames to make the denoisers more resilient to imperfections in their own generations. We provide more implementation details in Appendix A.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Interactive Generation", "weight": 1.0} -->

In this section, we evaluate our method's ability to generate spatially and temporally consistent interactive experiences within game worlds held out from the training set.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Interactive Generation", "weight": 1.0} -->

Baselines. We compare our approach with Oasis (decart2024oasis) and WorldMem (xiao2025worldmemlongtermconsistentworld), two interactive video generation methods employing the same DiT backbone as ${\mathcal{P}}_{\theta}$. WorldMem tracks camera states during the rollout and guides generation by retrieving key-frames from $O^{t-1}_{0}$ that closely match the current camera state. Oasis directly conditions on a sliding window of the most recent $K$ observations.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Interactive Generation", "weight": 1.0} -->

Ablations. We conduct several ablations to evaluate the core components and design choices of our method. Unless otherwise specified, our base configuration and all ablations utilize the 3D-XL denoiser.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Interactive Generation", "weight": 1.0} -->

PERSIST-S employs the smaller 3D-S denoiser to measure how an $8\times$ reduction in spatial tokens impacts the modeling capabilities of ${\mathcal{W}}_{\theta}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Interactive Generation", "weight": 1.0} -->

No-3D-Upscale skips the 3D-VAE enhancement, projecting the world-frame latents directly into screen space without upscaling them to their native 3D resolution.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Interactive Generation", "weight": 1.0} -->

Camera-GT bypasses our learned camera model by conditioning directly on the ground-truth cameras.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Interactive Generation", "weight": 1.0} -->

Finally, we note that Oasis effectively serves as a baseline ablation of the entire 3D conditioning mechanism.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Interactive Generation", "weight": 1.0} -->

Evaluation Setup. To ensure a fair comparison, all baselines and ablations utilize the same VAEs and are trained under an identical rectified flow formulation on the training set. We measure the Fréchet Video Distance (FVD) (unterthiner2018towards) across 168 evaluation trajectories collected from held-out game worlds. These trajectories are generated using an action policy designed to balance world exploration with revisiting previously rendered locations from new viewpoints. Table 1 reports FVD scores computed over sets spanning the first 200, 400, and 600 trajectory timesteps. We use the first 400 ground truth frames and cameras to initialise WorldMem's memory bank. This contrasts with PERSIST, which only requires a single initial frame $\langle{\bm{o}}_{0},{\bm{c}}_{0}\rangle$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Interactive Generation", "weight": 1.0} -->

Quantitative Results. As shown in Table 1, baselines relying solely on pixel history (Oasis and WorldMem) yield significantly worse FVD scores, with generation quality degrading sharply over time. In contrast, PERSIST and its variants maintain stable FVD scores across extended horizons, highlighting the critical role of conditioning on the 3D state. Among the ablations, No-3D-Upscale suffers the highest FVD penalty. This confirms the benefit of rendering from a high-resolution 3D latent, which produces a ${\bm{w}}_{2D}$ with superior depth resolution and 3D-to-pixel alignment. Conversely, PERSIST-S performs only marginally worse than the base configuration. While upscaling is crucial for rendering, the underlying 3D representation is highly robust to spatial compression (up to $512\times$ when combining the 3D-VAE and 3D-S denoiser). Finally, while Camera-GT achieves an FVD nearly identical to the base model, we observe that bypassing the learned camera model introduces physical inconsistencies that are not captured by the FVD (e.g. agent phasing through terrain or floating). We provide a qualitative example in Figure 11.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Interactive Generation", "weight": 1.0} -->

Generation stability. Qualitative analysis of sample rollouts (Figure 5) confirms that pixel-history baselines consistently produce irrecoverable artifacts by the 200^th^ timestep. In contrast, PERSIST produces remarkably stable rollouts. We corroborate this observation by measuring FID (heusel2017gans) at each generation timestep (Figure 6), finding that PERSIST suffers virtually no degradation over a 600-step episode. PERSIST does begin the episode with a slightly higher FID because it regenerates the initial pixel observation to ensure proper pixel/world-frame alignment. To demonstrate that this initial penalty is strictly an alignment artifact, Figure 6 includes PERSIST$+{\bm{w}}_{0}$, a variant introduced in Section 6.2 that receives perfectly aligned initial world and pixel frames. Regardless of initialization, PERSIST maintains its visual quality over time, whereas pixel-history baselines rapidly degrade.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Interactive Generation", "weight": 1.0} -->

In practice, we observe that the world-frames produced by ${\mathcal{W}}_{\theta}$ remain coherent for several thousand steps. Because ${\bm{w}}_{2D}$ is obtained directly from these highly stable world-frames, it provides reliable structural guidance over long horizons and lets ${\mathcal{P}}_{\theta}$ recover from visual artifacts. We showcase multiple examples of this self-correction over the course of a 2,000-step episode in Figure 13.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Interactive Generation", "weight": 1.0} -->

Human study. While FVD and FID scores capture distribution-level discrepancies, they are known to favor per-frame visual quality over the spatial and temporal coherence of individual generations (ge2024content). To complement our automated metrics, we conduct a human study comprising over 800 rollout evaluations from 28 participants. Users rated each video on "Visual Fidelity", "3D Consistency" and "Temporal Consistency", before assigning an overall score. Results are summarized in Table 2, with full methodological details in Appendix B and extended results in Appendix C. Across all metrics, PERSIST configurations consistently outperform the baselines, corroborating our quantitative and qualitative findings. Interestingly, PERSIST-S performs similarly to the base configuration in both average user ratings and head-to-head comparisons. This highlights that the FVD penalty observed for PERSIST-S does not translate to a human-perceptible degradation in generation quality.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Interactive Generation", "weight": 1.0} -->

Inference efficiency. Finally, we conduct a preliminary investigation into the speed-quality tradeoff of our method. We find that generation stability is preserved even when reducing the number of denoising steps from 20 down to 2 and 4 for ${\mathcal{W}}_{\theta}$ and ${\mathcal{P}}_{\theta}$, respectively. This yields a $3\times$ inference speed-up with only a moderate impact on generation quality (see Appendix D for a detailed analysis).

<!-- chunk {"id": "body-0044", "role": "body", "section": "New Applications and Emerging Capabilities", "weight": 1.0} -->

In addition to its improvement to the quality and coherence of generated experiences, we find that PERSIST's 3D representation confers a number of new capabilities.

<!-- chunk {"id": "body-0045", "role": "body", "section": "New Applications and Emerging Capabilities", "weight": 1.0} -->

3D generation. At initialisation, it is essential for ${\bm{w}}_{0}$ to capture the structure and semantics of the provided conditioning RGB observation. In Figure 12, we show that ${\mathcal{W}}_{\theta}$ successfully generates plausible starting world frames, while also outpainting unseen regions differently from one episode to the next. This ability lets PERSIST generate environments that are both diverse and coherent, supporting a wide variety of interactive experiences.

<!-- chunk {"id": "body-0046", "role": "body", "section": "New Applications and Emerging Capabilities", "weight": 1.0} -->

Explicit 3D initialisation. By default, PERSIST initialises generation from starting condition $\langle{\bm{o}}_{0},{\bm{c}}_{0}\rangle$, with the initial world-frame ${\bm{w}}_{0}$ being inferred by the world dynamics model ${\mathcal{W}}_{\theta}$. However, PERSIST also supports ${\bm{w}}_{0}$ being provided as a starting condition^44^4See Algorithms 1 and 2 for the respective inference algorithms of PERSIST and PERSIST+${\bm{w}}_{0}$.. This explicit 3D conditioning allows a greater degree of control over the generated experience than providing an image, as the full surroundings of the agent can be specified.

<!-- chunk {"id": "body-0047", "role": "body", "section": "New Applications and Emerging Capabilities", "weight": 1.0} -->

To assess how effectively PERSIST can leverage explicit 3D conditioning, we evaluate a variant denoted PERSIST+${\bm{w}}_{0}$, where a ground-truth world-frame ${\bm{w}}_{0}$ is provided at initialisation. PERSIST+${\bm{w}}_{0}$ achieves lower FID and FVD scores and higher human ratings (Tables 1 and 2, Figure 6), demonstrating that the model successfully incorporates the additional information contained within ${\bm{w}}_{0}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "New Applications and Emerging Capabilities", "weight": 1.0} -->

World edits mid-generation. valevski2024diffusionmodelsrealtimegame and kanervisto2025world proposed to perform manual edits to generated pixel frames before re-injecting them as context, as an alternative way of controlling the generated experience. As we can extract ${\bm{w}}_{t}$ at any point during generation, we obtain the capability of making precise 3D-edits to the world mid-episode. We pause generation at timestep $t$ and manually edit ${\bm{w}}_{t}$ to obtain $\tilde{{\bm{w}}}_{t}$. We then restart generation using $\{\tilde{{\bm{w}}}_{t},{\bm{c}}_{t},{\bm{o}}_{t},{\bm{a}}_{t}\}$ as the starting condition. We show several edit examples in Figure 7.

<!-- chunk {"id": "body-0049", "role": "body", "section": "New Applications and Emerging Capabilities", "weight": 1.0} -->

Persistent world dynamics. PERSIST learns to model environmental processes that evolve on their own. In Figure 8, we provide examples of environment dynamics and interactions occurring outside of the agent's view. We observe that dynamics occurring off-screen will sometimes act as causal drivers for emergent on-screen effects.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we introduced PERSIST, a world modelling framework that tracks the evolution of a persistent latent 3D state. Our results demonstrate that actively generating guidance frames from this 3D state substantially improves spatial memory, temporal coherence, and overall generation quality and stability compared to conditioning on pixel-based histories. We show that tracking this 3D world state allows the model to capture environment dynamics occurring beyond the agent's view. Additionally, it lets users pre-specify, visualise, and modify the structure of generated environments, creating new ways of controlling generated experiences.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Despite these advances, PERSIST currently relies on ground-truth 3D supervision during training and maintains a finite region of 3D space in memory. Furthermore, our implementation was not optimised for inference speed and does not yet achieve real-time inference. We believe these limitations outline a clear roadmap for future research involving persistent 3D world states: in-the-wild training via synthetic 3D annotations obtained from 2D-to-3D foundation models (wang2025vggt; sam3dteam2025sam3d3dfyimages), end-to-end post-training on generated rollouts to mitigate autoregressive drift (huang2025self), and access to unconstrained spatial memory via a 3D memory bank. We provide a detailed discussion of these directions in Appendix E.
