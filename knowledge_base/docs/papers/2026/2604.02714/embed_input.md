<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

ExploreVLA: Dense World Modeling and Exploration for End-to-End Autonomous Driving

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

End-to-end autonomous driving models based on Vision-Language-Action (VLA) architectures have shown promising results by learning driving policies through behavior cloning on expert demonstrations. However, imitation learning inherently limits the model to replicating observed behaviors without exploring diverse driving strategies, leaving it brittle in novel or out-of-distribution scenarios. Reinforcement learning (RL) offers a natural remedy by enabling policy exploration beyond the expert distribution. Yet VLA models, typically trained on offline datasets, lack directly observable state transitions, necessitating a learned world model to anticipate action consequences. In this work, we propose a unified understanding-and-generation framework that leverages world modeling to simultaneously enable meaningful exploration and provide dense supervision. Specifically, we augment trajectory prediction with future RGB and depth image generation as dense world modeling objectives, requiring the model to learn fine-grained visual and geometric representations that substantially enrich the planning backbone. Beyond serving as a supervisory signal, the world model further acts as a source of intrinsic reward for policy exploration: its image prediction uncertainty naturally measures a trajectory's novelty relative to the training distribution, where high uncertainty indicates out-of-distribution scenarios that, if safe, represent valuable learning opportunities.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We incorporate this exploration signal into a safety-gated reward and optimize the policy via Group Relative Policy Optimization (GRPO). Experiments on the NAVSIM and nuScenes benchmarks demonstrate the effectiveness of our approach, achieving a state-of-the-art PDMS score of 93.7 and an EPDMS of 88.8 on NAVSIM. The code is available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

End-to-end autonomous driving has advanced rapidly with the emergence of Vision-Language-Action (VLA) architectures \[hwang2024emma, jiang2025diffvla, zhou2025opendrivevla, wang2025alpamayo\], which unify perception, reasoning, and planning within a single model. By leveraging the representational power of large vision-language models, these models have demonstrated promising capabilities in translating raw sensor observations into driving actions. Yet, the dominant training paradigm for such models (behavior cloning on expert demonstrations or supervised fine-tuning) introduces a fundamental bottleneck: the learned policy can only replicate the behaviors it has observed, without the ability to discover alternative strategies that may be equally or more effective. This limitation manifests as distributional brittleness: when confronted with scenarios that deviate from the expert distribution, the policy lacks the exploratory experience needed to generalize \[ross2011reduction, codevilla2019exploring\].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning (RL) offers a principled mechanism to overcome this limitation by allowing the agent to explore beyond the boundaries of expert data and optimize its policy through trial-and-error interaction \[guo2025improving\]. Recent advances in RL post-training, exemplified by Group Relative Policy Optimization (GRPO) \[shao2024deepseekmath\], have demonstrated that sampling diverse candidate outputs and performing relative ranking can effectively improve policy quality atop strong pretrained models. However, applying RL to autonomous driving poses challenges distinct from other domains. In language tasks, state transitions are fully determined by the model's output, and outcomes are immediately observable. In robotics, high-fidelity simulators enable safe trial-and-error. Autonomous driving enjoys neither advantage: the consequences of a planned trajectory depend on complex scene dynamics that no existing simulator faithfully captures. These challenges motivate the need for a world model that can internalize environment dynamics and anticipate action consequences from data alone.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Yet a further challenge remains: standard task-level rewards such as Predictive Driver Model Score (PDMS) \[dauner2024navsim\] evaluate trajectory quality but do not distinguish between policies that merely replicate expert behavior and those that have genuinely discovered novel strategies. An exploration signal orthogonal to task performance is therefore essential to unlock the full potential of RL post-training.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A second limitation of existing VLA driving models is the sparsity of their supervisory signals. Most approaches rely on textual descriptions and trajectory waypoints as training targets \[zhou2025autovla, zhou2025opendrivevla\], which, while informative for high-level decision-making, fail to capture the rich spatial geometry and fine-grained appearance of driving scenes. This supervisory deficit constrains the model's ability to build comprehensive representations, particularly for aspects of the environment (such as road topology, object extent, and depth ordering) that are critical for safe planning but are not explicitly encoded in sparse action labels \[li2025drivevla\].

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose a unified understanding-and-generation framework that addresses both limitations through a single mechanism: dense world modeling and exploration (Fig.˜1). Specifically, we augment trajectory prediction with future RGB and depth image generation as auxiliary objectives. On the supervision side, these generation tasks require the model to predict fine-grained visual appearance and metric geometry of future scenes, providing dense gradient signals that substantially enrich the planning backbone's visual and geometric representations. On the exploration side, we leverage a key insight: *the world model's image prediction uncertainty naturally measures a trajectory's novelty relative to the training distribution*. Since the world model is trained exclusively on expert demonstrations, it produces low-uncertainty predictions for trajectories within the expert distribution but exhibits high uncertainty on out-of-distribution (OOD) trajectories. Crucially, this uncertainty reflects distance to the *entire* training distribution, rather than deviation from a single ground-truth trajectory, which provides a more reliable novelty signal than trajectory distance alone.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We incorporate this signal into a safety-gated exploration reward: trajectories that achieve high PDMS scores while exhibiting high prediction uncertainty are identified as valuable discoveries of new successful strategies and receive an exploration bonus. This composite reward is optimized via GRPO, enabling the policy to expand its behavioral repertoire while maintaining driving safety.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contributions can be summarized as follows: We introduce a novel exploration mechanism for RL post-training that uses the world model's image prediction uncertainty as an intrinsic novelty measure, coupled with a safety-gated reward to encourage beneficial out-of-distribution exploration.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a unified VLA framework that jointly predicts future trajectories, RGB images, and depth images, leveraging dense world modeling to provide rich visual and geometric supervision for the planning backbone.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate state-of-the-art performance on the NAVSIM benchmark with a PDMS of 93.7 and an EPDMS of 88.8, and validate the generalizability of our approach on the nuScenes dataset.

<!-- chunk {"id": "body-0013", "role": "body", "section": "World Models for Autonomous Driving", "weight": 1.0} -->

In the context of autonomous driving, world models offer the ability to predict future states of the driving scene, enabling planning, data augmentation, and closed-loop evaluation without costly real-world interactions \[guan2024world, feng2025survey, ding2025understanding, yan2025ad\]. A significant line of work focuses on video prediction-based world models \[gao2024vista, hassan2025gem, yang2025resim\]. For example, GAIA-1 \[hu2023gaia\] leverages a generative model conditioned on video, text, and action inputs to produce realistic driving videos. DriveDreamer \[wang2024drivedreamer\] generates future driving frames conditioned on HDMaps and 3D bounding boxes. GenAD \[yang2024generalized\] proposes an action-conditioned video generation framework that supports long-horizon future prediction for planning. Another prominent direction explores world models within structured geometric spaces.

<!-- chunk {"id": "body-0014", "role": "body", "section": "World Models for Autonomous Driving", "weight": 1.0} -->

UniWorld \[min2023uniworld\] proposes a unified framework for 4D occupancy forecasting, and OccWorld \[zheng2024occworld\] extends this idea by predicting 3D occupancy and ego-motion jointly, providing a compact world representation for downstream planning. UniScene \[li2025uniscene\] further scales this paradigm by jointly generating consistent future semantic occupancy, LiDAR and multi-view images. Beyond generation and prediction, several works integrate world models into the planning pipeline. For instance, WoTE \[li2025end\] incorporates a BEV world model to predict future states for online trajectory evaluation and selection. OmniNWM \[li2025omninwm\] employs a learned navigation world model to generate imagined futures and derive planning rewards from predicted scene dynamics. World4Drive \[zheng2025world4drive\] further introduces a latent world model that predicts future latent states under multiple driving intentions and selects trajectories via a learned selector.

<!-- chunk {"id": "body-0015", "role": "body", "section": "World Models for Autonomous Driving", "weight": 1.0} -->

In our work, we leverage the world model not only for future state prediction but also as a source of intrinsic reward signals that encourage the policy to explore diverse and informative driving behaviors, thereby improving generalization beyond the coverage of the training data.

<!-- chunk {"id": "body-0016", "role": "body", "section": "VLA Models for Autonomous Driving", "weight": 1.0} -->

The integration of vision, language, and action within a unified framework has emerged as a promising paradigm for autonomous driving \[jiang2025survey, li2025recogdrive\]. Early efforts, such as DriveGPT-4 \[xu2024drivegpt4\], use frozen VLMs to narrate driving scenes but do not directly output control signals. Subsequent modular VLA approaches began embedding language into the planning loop. For example, OpenDriveVLA \[zhou2025opendrivevla\] fuses multimodal sensor inputs with textual route instructions to generate interpretable waypoints, while RAG-Driver \[yuan2024rag\] introduces retrieval-augmented planning for long-tail scenarios. The field then advances toward unified end-to-end architectures. EMMA \[hwang2024emma\] jointly performs detection and planning within a single VLM, and DiffVLA \[jiang2025diffvla\] combines diffusion-based trajectory sampling with language-conditioned embeddings. Most recently, reasoning-augmented VLA models have pushed the frontier further.

<!-- chunk {"id": "body-0017", "role": "body", "section": "VLA Models for Autonomous Driving", "weight": 1.0} -->

ORION \[fu2025orion\] incorporates a transformer memory module for long-horizon reasoning, and AutoVLA \[zhou2025autovla\] fuses CoT reasoning and trajectory planning in a single autoregressive transformer. Alpamayo-R1 \[wang2025alpamayo\] introduces causally grounded Chain-of-Causation reasoning tightly integrated with trajectory prediction, enhancing reasoning-action consistency and long-tail safety performance. Despite this rapid progress, most existing VLA models rely on textual descriptions and action trajectories as the primary supervisory signal, which are inherently sparse. This supervisory sparsity limits the model's ability to learn comprehensive scene representations. In contrast, our work leverages RGB and depth images as auxiliary dense supervisory signals to encourage the model to capture richer visual and geometric cues, thereby yielding more accurate and robust trajectory planning.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Unified Understanding and Generation Models", "weight": 1.0} -->

In foundation model research, the long-standing separation between understanding and generation has motivated a growing effort to unify both within a single architecture for greater scalability and cross-task synergy \[xie2024show, chen2025janus, wang2026multimodal\]. In autonomous driving, this paradigm has gained significant traction as researchers seek to bridge the gap between world modeling and end-to-end planning. For example, FutureSightDrive \[zeng2025futuresightdrive\] proposes a spatio-temporal visual Chain-of-Thought framework where a VLA model first generates future frames, including lane lines, 3D bounding boxes, and complete future images, as visual intermediate reasoning steps, then predicts trajectories conditioned on these imagined futures. Policy World Model (PWM) \[zhao2025pwm\] pre-trains on large-scale action-free video generation to learn world dynamics, then fine-tunes with a collaborative formulation where trajectory planning is explicitly conditioned on forecasted future states. DriveVLA-W0 \[li2025drivevla\] introduces world modeling objectives to unlock data scaling laws for end-to-end driving.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Unified Understanding and Generation Models", "weight": 1.0} -->

UniDrive-WM \[xiong2026unidrive\] unifies scene understanding, trajectory planning, and trajectory-conditioned future image generation within a single VLM. Epona \[zhang2025epona\] combines autoregressive causal modeling with diffusion-based generation through decoupled spatiotemporal factorization, enabling both high-fidelity video synthesis and trajectory planning. Together, these works demonstrate that jointly modeling future scene generation and action prediction yields more informed and anticipatory planning. Our work follows this unified paradigm by leveraging RGB and depth image generation as dense supervisory signals alongside trajectory prediction, while further employing the world model to provide intrinsic reward signals that encourage exploratory driving behaviors and improve generalization beyond the training distribution.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Overview", "weight": 1.0} -->

We present a unified understanding-and-generation framework for end-to-end autonomous driving that addresses two key limitations of existing VLA models: the lack of exploration beyond expert demonstrations and the reliance on sparse supervisory signals. Our framework consists of three components. First, we build upon a unified VLM backbone that jointly supports autoregressive text modeling and discrete image generation within a single architecture (Sec.˜3.3). Second, we introduce future RGB and depth image generation as dense world modeling objectives that provide token-level supervision alongside trajectory prediction, encouraging the model to learn richer scene representations (Sec.˜3.4). Third, we leverage the world model's prediction uncertainty as an intrinsic reward signal to guide policy exploration via Group Relative Policy Optimization (GRPO), enabling the model to discover diverse driving strategies beyond mere imitation (Sec.˜3.5). An overview of our framework is illustrated in Fig.˜2.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We formulate autonomous driving as a unified understanding-and-generation task, where a single model jointly predicts future trajectories and generates dense visual representations conditioned on the current driving context.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Input", "weight": 1.0} -->

At each timestep $t$, the model receives three inputs: the current and $T$ past front-view camera images $\{\mathbf{I}_{t-T},\cdots,\mathbf{I}_{t}\}$ with $\mathbf{I}\in\mathbb{R}^{H\times W\times 3}$, a natural language command $\mathbf{c}$, and the ego-vehicle status $\mathbf{s}_{t}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Tokenization", "weight": 1.0} -->

We maintain a unified vocabulary of discrete tokens spanning text, images, and special task indicators. For text tokenization, we adopt the same tokenizer from the pre-trained LLM backbone, such that the language command $\mathbf{c}$ is tokenized into $L$ text tokens $\mathbf{v}=\{v_{1},v_{2},\cdots,v_{L}\}$. For image tokenization, we employ a pre-trained MAGVIT-v2 \[yu2023language\] quantizer with a lookup-free codebook of size $K=8{,}192$. Each image is encoded into discrete tokens by partitioning it into non-overlapping patches of size $16\times 16$. Each of the $(T+1)$ input frames is independently tokenized into $M$ image tokens, yielding the input image token sequence $\mathbf{u}=\{u_{1},u_{2},\cdots,u_{(T+1)\times M}\}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Tokenization", "weight": 1.0} -->

For ego status encoding, the $\mathbf{s}_{t}$ is projected into the transformer's embedding space via a learnable MLP, producing ego status embeddings $\mathbf{e}_{s}$ that are concatenated with the other input tokens.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Causal and Full Attention Mechanism", "weight": 1.0} -->

We adopt the omni-attention mechanism from Show-o \[xie2024show\], which adaptively combines causal and full attention depending on the token type. Text tokens $\mathbf{v}$ and ego status embeddings $\mathbf{e}_{s}$ are processed via causal attention, where each token attends only to its preceding tokens. Image tokens $\mathbf{u}$ are processed via full attention, which allows comprehensive interaction among all spatial positions and ensures that the generation process is fully conditioned on the driving context.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Trajectory Prediction Head", "weight": 1.0} -->

In addition to the generation outputs, we extract the hidden states from the transformer at designated positions and feed them through a lightweight MLP head to predict future waypoints: where $\mathbf{h}$ denotes the hidden representation. This design decouples trajectory prediction from the discrete token vocabulary, allowing the model to produce continuous-valued waypoints while sharing the same contextualized representations learned through the joint understanding-and-generation objective.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Dense Supervisory Signals via World Modeling", "weight": 1.0} -->

A central limitation of existing VLA models for autonomous driving is their reliance on sparse supervisory signals. Textual descriptions provide only high-level semantic intent (*e.g*., "turn left"), while trajectory waypoints encode a thin, low-dimensional slice of the rich information embedded in driving scenes. As a result, the vast majority of scene structure, such as patial layout and depth ordering, remains unsupervised, which limits the model's ability to learn comprehensive representations of the driving environment.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Dense Supervisory Signals via World Modeling", "weight": 1.0} -->

We address this by formulating future scene generation as an auxiliary world modeling objective that provides dense supervision alongside trajectory prediction. Our model is trained to generate $F$ future frames of both RGB images and depth maps, effectively requiring it to "imagine" the future visual and geometric state of the world. This dense generation objective forces the model to internalize fine-grained knowledge about scene dynamics.

<!-- chunk {"id": "body-0029", "role": "body", "section": "RGB Generation as Visual Supervision", "weight": 1.0} -->

The future RGB generation objective requires the model to predict the visual appearance of upcoming driving scenes, providing dense supervision over texture, color, object identity, and scene semantics. Each future RGB frame is tokenized via the shared MAGVIT-v2 quantizer, and the model learns to reconstruct randomly masked tokens through the mask token prediction objective. Formally, the RGB generation loss over all $F$ future frames is: where $u^{\text{rgb}}_{f,j}$ is the $j$-th masked token of the $f$-th future RGB frame, and $\mathbf{u}^{\text{rgb}}_{f,*}$ denotes the corresponding masked sequence. By reconstructing future visual tokens, the model learns to capture how scene appearance evolves under the current driving context.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Depth Generation as Geometric Supervision", "weight": 1.0} -->

Complementary to RGB, the depth generation objective supervises the model on the 3D geometric structure of future scenes. Depth maps encode object distances, spatial layout, and surface orientation, which is critical for safe planning but entirely absent from text or trajectory supervision. The depth generation loss is defined analogously: where $u^{\text{dep}}_{f,j}$ is the $j$-th masked token of the $f$-th future depth map.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Intrinsic Reward from World Model for Exploration", "weight": 1.0} -->

Models trained purely via behavior cloning tend to narrowly replicate the expert's actions and struggle to generalize when the test-time distribution deviates from the training data. In the second stage of training, we leverage the world model learned in the first stage as a source of intrinsic reward signals that encourage the policy to explore novel yet safe driving behaviors beyond mere imitation. The core idea is that the world model's image prediction uncertainty provides a natural measure of trajectory novelty relative to the entire training distribution: high uncertainty indicates that the model has rarely encountered the visual consequences of a given action, signaling an out-of-distribution trajectory that, if safe, represents a valuable learning opportunity.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Uncertainty-Based Exploration Bonus", "weight": 1.0} -->

Given a candidate trajectory $\boldsymbol{\tau}_{i}$ sampled from the current VLA policy, we condition the world model on $\boldsymbol{\tau}_{i}$ and perform future image generation. For each predicted discrete image token, the model outputs a probability distribution over the MAGVIT-v2 codebook. We quantify the prediction uncertainty using the entropy of these token-level distributions, averaged across all generated future RGB and depth tokens: where $\mathcal{M}$ denotes the set of generated image token positions across all future RGB and depth frames, and $p_{j}$ is the predicted probability of image token $j$. A high entropy indicates that the world model is uncertain about the visual consequences of trajectory $\boldsymbol{\tau}_{i}$, meaning the trajectory leads to scenarios underrepresented in the training distribution. Conversely, low entropy indicates an in-distribution trajectory whose consequences the model has already learned to predict.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Uncertainty-Based Exploration Bonus", "weight": 1.0} -->

We define the exploration bonus as the normalized entropy: where $f(\mathcal{H})=(\mathcal{H}-\mathcal{H}_{\min})/(\mathcal{H}_{\max}-\mathcal{H}_{\min})$ maps the raw entropy to a normalized bonus $b_{i}\in$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Safety-Gated Reward", "weight": 1.0} -->

High uncertainty alone does not guarantee that exploration is beneficial, since a trajectory leading to a collision is novel but not useful. We therefore gate the exploration bonus using the PDMS \[dauner2024navsim\], which evaluates trajectory quality on a $$ scale based on collision avoidance, comfort, and progress. The intrinsic reward for trajectory $\boldsymbol{\tau}_{i}$ is: where $\delta$ is a safety threshold and $\lambda$ controls the exploration strength. The gating mechanism ensures that only safe trajectories ($\text{PDMS}_{i}>\delta$) receive the exploration bonus. Unsafe or failed explorations are scored purely by their PDMS without additional encouragement. This design prioritizes trajectories that are simultaneously novel (high world model uncertainty) and good (high PDMS). Such trajectories represent out-of-distribution behaviors that are critical for improving generalization beyond expert demonstrations.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Policy Optimization via GRPO", "weight": 1.0} -->

We optimize the policy using GRPO \[shao2024deepseekmath\]. At each iteration, we sample a group of $G$ candidate trajectories $\{\boldsymbol{\tau}_{1},\cdots,\boldsymbol{\tau}_{G}\}$ from the current policy. Each trajectory and corresponding predicted image tokens are scored using the reward in Eq.˜7, and rewards are normalized within the group to compute relative advantages: The policy is updated to increase the likelihood of trajectories with positive advantages and suppress those with negative advantages. This group-relative formulation naturally steers the policy toward trajectories that are both good and novel within each sampled group.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Training Strategy", "weight": 1.0} -->

As shown in Fig.˜2, our training proceeds in two stages. The first stage consists of two phases: pre-training and supervised fine-tuning. During pre-training, ground-truth future actions are provided as input, and the model is trained solely with the image generation objective. This allows the model to adapt its visual generation capabilities to driving scenes. In the supervised fine-tuning phase, the model is trained to jointly predict both actions and future images. In the second stage, we further refine the policy using an intrinsic reward derived from the world model to encourage exploration.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Datasets", "weight": 1.0} -->

We evaluate our method on two widely used autonomous driving benchmarks: NAVSIM and nuScenes.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Datasets", "weight": 1.0} -->

NAVSIM \[dauner2024navsim, cao2025pseudo\] is a recently proposed non-reactive simulation benchmark built upon the OpenScene dataset. NAVSIM v1 evaluates planning quality using PDMS \[dauner2024navsim\], and NAVSIM v2 adopts the Extended PDMS (EPDMS) \[cao2025pseudo\]. Both metrics aggregate factors such as progress, time-to-collision, and comfort, achieving stronger correlation with closed-loop evaluations. We train on the navtrain split and report results on the navtest split. In NAVSIM, the model predicts future waypoints in the form of $(x,y,\theta)$ over a 4-second planning horizon. nuScenes \[caesar2020nuscenes\] consists of 1,000 driving scenes and has become a standard benchmark for open-loop planning evaluation.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Datasets", "weight": 1.0} -->

Following prior works \[hu2022st, hu2023planning, jiang2023vad\], we adopt the standard train/val split and evaluate using the L2 displacement error and collision rate between predicted and ground-truth trajectories. On nuScenes, the model predicts future waypoints in the form of $(x,y)$. The evaluation results on nuScenes are presented in the supplementary material.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Our model is built upon Show-o \[xie2024show\] as the backbone architecture. In the first training stage, we first pre-train the model for 10 epochs by conditioning on ground-truth future actions and supervising only the image generation. We then perform supervised fine-tuning for 15 epochs, where the model jointly predicts future trajectories and generates future RGB and depth images. In the second stage, we apply GRPO-based post-training with LoRA \[hu2022lora\] for 5 epochs to further refine the policy using the exploration-aware reward described in Sec.˜3.5. All experiments are conducted on 4$\times$H200 GPUs. We obtain depth maps from a pre-trained monocular depth estimation model \[yin2023metric3d\]. Detailed hyperparameters are provided in the supplementary material.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Ego Status MLP TransFuser [chitta2022transfuser] DRAMA [yuan2024drama] Centaur [sima2025centaur] DriveSuprim [yao2025drivesuprim] DrivingGPT [chen2025drivinggpt] FSDrive [zeng2025futuresightdrive] PWM [zhao2025pwm] AutoVLA [zhou2025autovla] AutoVLA† [zhou2025autovla] Table 1: Comparison on NAVSIM v1 with closed-loop metrics. The best performance is marked in bold, and the second best is underlined. Abbreviations: no at-fault collision (NC), drivable area compliance (DAC), ego progress (EP), time to collision (TTC), comfort (Comf.). SC: single-view camera; MC: multi-view camera; L: LiDAR; †: best-of-N (N=6) strategy [zhou2025autovla].

<!-- chunk {"id": "body-0042", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

TransFuser [chitta2022transfuser] DriveSuprem [yao2025drivesuprim] ARTEMIS [feng2025artemis] DiffusionDrive [liao2025diffusiondrive] DiffusionDriveV2 [zou2025diffusiondrivev2] Table 2: Comparison on NAVSIM v2 with extended closed-loop metrics. The best performance is marked in bold, and the second best is underlined.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Results on NAVSIM v1", "weight": 1.0} -->

Tab.˜1 presents the comparison on the NAVSIM v1 benchmark. Our ExploreVLA achieves the highest PDMS of 93.7 with the best-of-N strategy, outperforming all prior approaches. Notably, ExploreVLA uses only a single-view camera, yet surpasses multi-sensor methods such as DriveSuprim and Centaur. Even without the best-of-N strategy, ExploreVLA attains a PDMS of 90.4, which is competitive with multi-view methods like AutoVLA. Among the sub-metrics, ExploreVLA$\dagger$ achieves the best TTC and the second-best scores on NC, DAC, and EP, demonstrating that our world-model-based exploration reward helps the model internalize diverse and robust driving behaviors beyond what pure imitation learning can provide.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Results on NAVSIM v2", "weight": 1.0} -->

Tab.˜2 further validates our approach on NAVSIM v2, which introduces extended closed-loop metrics including driving direction compliance (DDC), traffic light compliance (TLC), lane keeping (LK), history comfort (HC), and extended comfort (EC). ExploreVLA achieves the highest EPDMS of 88.8, surpassing the previous best result of 86.1 by DriveVLA-W0 by 2.7 points. Our method obtains the best scores on six out of nine individual metrics, while remaining highly competitive on the rest.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Analysis of Intrinsic Reward Modeling", "weight": 1.0} -->

Fig.˜3 provides an analysis of our intrinsic reward modeling mechanism. The left shows a generally positive correlation between the exploration bonus and L2 error with respect to the ground-truth trajectory: as the sampled trajectory deviates further from the expert action, the world model's prediction uncertainty tends to increase, resulting in higher exploration bonuses. However, L2 distance is not always an unreliable measure of novelty, and our uncertainty-based bonus reflects it more faithfully. The right of Fig.˜3 shows a representative failure case: a trajectory that closely follows the expert's direction may incur a large L2 error due to positional shift, while a trajectory that takes a fundamentally different route may have a smaller L2 error. Additionally, we randomly select 1,000 straight-driving scenes and apply two types of perturbation to the expert trajectory: speed variation, which changes vehicle speed while following nearly identical paths, and direction variation, which changes the driving direction and therefore represents genuinely different driving behaviors. As shown in Tab.˜3, the speed perturbation produces a substantially larger L2 error despite exhibiting little behavioral novelty, whereas the direction perturbation yields a smaller L2 error while receiving a significantly higher exploration bonus.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Analysis of Intrinsic Reward Modeling", "weight": 1.0} -->

These results indicate that the proposed uncertainty-based reward better captures behavioral novelty than trajectory distance.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Analysis of Intrinsic Reward Modeling", "weight": 1.0} -->

Type 1 (speed Δ, similar path) Type 2 (direction Δ, different path) Table 3: L2 error vs. exploration bonus on 1,000 randomly selected straight-driving scenes under two perturbation types. L2 error misjudges novelty in both cases, whereas our exploration bonus correctly assigns low novelty to speed changes (similar path) and high novelty to direction changes (different path).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

RGB Img. Gen. Depth Img. Gen.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Effect of Dense Visual Supervision", "weight": 1.0} -->

Tab.˜4 examines the contribution of RGB and depth image generation as auxiliary supervision during Stage 1 training. The trajectory-only baseline without any image generation achieves the lowest PDMS. Adding either RGB or depth generation alone yields comparable improvements, which confirms that both modalities provide meaningful dense supervisory signals for learning better scene representations. Combining both RGB and depth generation further improves PDMS to 88.5. This indicates that RGB and depth capture complementary information (visual appearance and geometric structure) and their joint supervision leads to a more comprehensive understanding of driving scenes.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Effect of Reward Design", "weight": 1.0} -->

Tab.˜5 isolates the contribution of each reward component during Stage 2 RL. Starting from the Stage 1 model (PDMS 88.50), applying only the PDMS reward brings a substantial improvement to 90.19, demonstrating the effectiveness of GRPO-based post-training. Using the image-based exploration reward alone yields only a marginal gain (88.53), which is expected since the image reward serves as an exploration bonus rather than a direct driving quality signal. Without the safety gate provided by PDMS thresholding, the exploration signal alone cannot effectively guide policy improvement. When combining both rewards, the model achieves the best PDMS of 90.36. This confirms that the image-based exploration reward provides a complementary learning signal that encourages the policy to discover diverse driving strategies beyond what the PDMS reward alone can incentivize.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Effect of the Safety Threshold", "weight": 1.0} -->

The safety threshold $\delta$ in Eq.˜7 controls which trajectories are eligible for the exploration bonus. We ablate $\delta\in\{0,0.3,0.6,0.9\}$ in Tab.˜6. The proposed exploration reward consistently improves over the PDMS-only baseline (second row in Tab.˜5) across all threshold choices. This result indicates that the effectiveness of our method is not sensitive to the exact value of $\delta$. Among all settings, $\delta=0.9$ achieves the best performance. The similar performance observed for $\delta\in\{0,0.3,0.6\}$ can be explained by the Stage 1 policy distribution. Approximately $99\%$ of the sampled trajectories already achieve PDMS scores above $0.6$, and thus making these thresholds insufficient for distinguishing safe trajectories from risky ones. When $\delta$ is increased to $0.9$, the safety gate begins to effectively separate safe-and-novel trajectories from unsafe exploratory behaviors, leading to the highest PDMS.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Qualitative Analysis", "weight": 1.0} -->

Fig.˜4 visualizes planned trajectories after Stage 1 and Stage 2 in three representative scenarios. In each case, the Stage 1 model exhibits a safety-critical failure (*i.e*., colliding with a vehicle, passing dangerously close to pedestrians, or running a stop sign). After Stage 2 reinforcement learning, the model successfully corrects these behaviors. These results demonstrate that our world-model-based RL not only improves aggregate metrics but also rectifies safety-critical failures that pure imitation learning struggles to resolve from expert demonstrations alone.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented ExploreVLA, a unified framework that addresses the lack of exploration and sparse supervision in VLA-based autonomous driving. By jointly predicting future trajectories, RGB images, and depth maps, our approach provides dense world modeling supervision that enriches scene representations. We further leverage the world model's prediction uncertainty as an intrinsic novelty measure, combined with a safety-gated reward and GRPO, to guide the policy toward diverse yet safe driving strategies beyond expert imitation. Extensive experiments on the NAVSIM and nuScenes benchmarks validate the effectiveness of our approach, achieving state-of-the-art performance on NAVSIM.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Limitations and Future Work. Our framework currently uses a single front-view camera; extending to multi-view inputs could further broaden spatial coverage and planning robustness. Moreover, our reinforcement learning stage relies on offline/open-loop post-training, which may bias the policy toward the training distribution and provide limited opportunities to learn recovery behaviors from self-induced states. Future work will investigate integrating our uncertainty-guided exploration framework with large-scale closed-loop reinforcement learning and evaluation.
