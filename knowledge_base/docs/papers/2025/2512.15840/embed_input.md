<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Large Video Planner Enables Generalizable Robot Control

Topics include Robotics, Robustness, Large language models, Language models, Foundation models, Vision-language models, Datasets, Generalization, Planning, Control, Learning, Creating vision-language-action, Vision-language-action model.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

General-purpose robots require decision-making models that generalize across diverse tasks and environments. Recent works build robot foundation models by extending multimodal large language models (MLLMs) with action outputs, creating vision-language-action (VLA) systems. These efforts are motivated by the intuition that MLLMs' large-scale language and image pretraining can be effectively transferred to the action output modality. In this work, we explore an alternative paradigm of using large-scale video pretraining as a primary modality for building robot foundation models. Unlike static images and language, videos capture spatio-temporal sequences of states and actions in the physical world that are naturally aligned with robotic behavior. We curate an internet-scale video dataset of human activities and task demonstrations, and train, for the first time at a foundation-model scale, an open video model for generative robotics planning. The model produces zero-shot video plans for novel scenes and tasks, which we post-process to extract executable robot actions. We evaluate task-level generalization through third-party selected tasks in the wild and real-robot experiments, demonstrating successful physical execution.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Together, these results show robust instruction following, strong generalization, and real-world feasibility. We release both the model and dataset to support open, reproducible video-based robot learning. Our website is available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key component of many robotic systems is the planning algorithm \Garrett et al. which takes a high-level task or instruction alongside the robot's sensory observations to generates a sequence of states and actions that will achieve the goal. General-purpose robots --- systems designed to operate reliably across diverse tasks and novel environments --- would greatly benefit from planning algorithms that are themselves extremely general. Such planning algorithms should be able to comprehend unseen tasks, adapt fluidly to novel scenes, and output physically coherent behaviors. Developing these strong generalization capabilities remains a central, unresolved challenge of embodied intelligence today.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The recent success of foundation models in language and vision has reshaped how generalization is achieved in AI. Large language models (LLMs) \Achiam et al., [2023; Bai et al., 2023; Touvron et al., 2023; Comanici et al., 2025; Liu et al., 2024; Team et al., 2025b\] trained on internet-scale text corpora exhibit broad competence across unseen tasks, suggesting that scale and data diversity can induce powerful transfer. Extending this idea, multimodal large language models (MLLMs) \Liu et al., [2023; Team, 2024; Bai et al., 2025; Han et al., 2025\] align vision and language, grounding textual reasoning in perception. These advances have inspired robot foundation models---large, unified architectures that generalize across scenes and tasks by integrating perception, language, and control.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key instantiation is the Vision--Language--Action (VLA) model \Brohan et al., [2022; Kim et al., 2024; Black et al., 2024b\], which extends MLLMs with an action output modality.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, in comparison to web-scale text and image data that underpin MLLMs Schuhmann et al.; Penedo et al.; Chen et al. \[2024b\], robot action data is much scarcer \Collaboration et al., [2023; Bu et al., 2025\]. As a result, it is difficult to build VLA models with the same level of competency as that of MLLMs, with existing VLAs relying on an asymmetric form of transfer, where the pretrained knowledge in an MLLM is finetuned on a narrow amount of robot data. Such a construction leads to poor generalization when given new robot tasks in unseen situations \Wang et al., [2025b\].

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose an alternative paradigm for robot foundation models---using video as the primary modality. Unlike static image--text pairs, videos naturally encode state--action plans, visually depicting how the world evolves as agents interact with it. A video generative model conditioned on a textual instruction and an initial observation frame can predict plausible future frames---effectively generating visual action plans for diverse tasks. This formulation aligns closely with robotics: it captures spatial and temporal continuity, offering a far richer representation of continuous actions than text tokens. Moreover, video data is abundant online, spanning human activities, instructional tutorials, and task demonstrations. Each video implicitly contains action information, following the same pretraining principle that powers MLLMs---leveraging large, naturally occurring data to learn mappings grounded in real-world behavior. Compared to the asymmetric transfer of VLAs, this video-based paradigm offers a directly grounded source of transfer: the data itself captures the temporal dynamics of action, providing a stronger bridge to downstream embodied tasks.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To instantiate this paradigm, we develop a video foundation model purpose-built for embodied decision-making and action extraction. Unlike existing video generation models---typically optimized for content creation and prone to mode collapse---we prioritize the emphasizes on physical consistency to real image observations and adherence to task instructions. It takes textual instructions and initial observation frame(s) as input, generating predictive video plans from which executable actions are extracted \Du et al., [2023b\].

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We realize this vision through advances in both data and model design. First, we introduce and release a large-scale, open dataset curated for embodied decision making. Sourced from a diverse mix of internet and robot videos, this dataset is carefully processed to capture complex human and robot behaviors, maintain high temporal coherence, and ensure tight alignment with language instructions. Second, we propose a novel model that leverages History Guidance \Song et al., and Diffusion Forcing \Chen et al., [2024a\] to specifically enhance temporal coherence and causal consistency in the generated frames. These data and model contributions jointly enable large-scale, temporally grounded pretraining, leading to robust generalization across diverse tasks and scenes.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate our model's generalization through two complementary experiments. First, we perform an extensive independent evaluation to assess task-level generalization of the video model itself: independent testers freely selected scenes and tasks---encouraged to be creative and challenging---producing evaluations spanning diverse conditions, from outdoor scenes like crosswalks to dexterous tasks such as tearing tape. Second, we conduct real-robot experiments demonstrating end-to-end execution. Actions extracted from generated video plans are deployed on physical robots, from parallel grippers to dexterous hands, successfully executing tasks in uncontrolled environments. Compared to baseline models, our approach exhibits a stronger grasp of contact dynamics, goal reasoning, and end-to-end execution, demonstrating robust generalization across both simulated and real settings.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, our work makes three primary contributions. Large Video Planner (LVP), a large-scale video foundation model designed for robotic manipulation, and an associated framework for deploying it as a zero-shot policy on real robots. A curated, open internet-scale video dataset of human activities and robot task demonstrations, carefully processed for embodied decision making and instruction following. A rigorous evaluation of task-level generalization, using an independent testing protocol and real-robot experiments to systematically assess generalization across unseen environments, tasks, and embodiments.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Method", "weight": 1.0} -->

A robot foundation model maps observations and goals to a sequence of actions. We realize this through a two-stage design: a large video planner followed by action extraction. Consider a robot facing a door it has never encountered before. Its camera perceives the door handle as its owner instructs, "Open this door." The robot first employs a video foundation model to imagine how a rational human would perform the task---generating a video where a hand reaches for the handle, twists it, and pushes the door open. It then applies action extraction algorithms to translate this visual plan into executable control signals, whether for a dexterous five-fingered hand or a parallel gripper.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Method", "weight": 1.0} -->

In Section 3.1, we present our video foundation model for generative planning in video space. Section 3.2 introduces an internet-scale video dataset of human activities and robot demonstrations that we curated for this study. Finally, Section 4 describes our retargeting mechanism that grounds the generated video plans into robot-specific actions across diverse morphologies.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Latent Diffusion", "weight": 1.0} -->

We begin building our video foundation model following the latent diffusion framework \Brooks et al., [2024; Wan et al., 2025\]. We use a temporally causal 3D variational autoencoder (VAE) to compress a video clip in pixel space into a compact, lower-dimensional latent representation $x$. The VAE encodes each $8\times 8\times 4$ spatiotemporal patch into a 16-channel embedding, converting an input of shape $[1+T,3,H,W]$ into a latent of shape $1+\lceil T/4\rceil,16,\lceil H/4\rceil,\lceil W/4\rceil$, where $T+1$ is the number of frames and $H,W$ are spatial dimensions. The first frame of a video is repeated $4$ times before such compression to allow co-training with single-frame image data, which corresponds to the $1$ in $T+1$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Latent Diffusion", "weight": 1.0} -->

We then freeze the 3D VAE and train a special video diffusion model \[Sohl-Dickstein et al., [2015; Ho et al., 2020; Lipman et al., 2022; Peebles and Xie, 2023\] in this compressed latent space using a modified Diffusion Forcing Transformer \Chen et al., [2024a; Song et al., 2025\], a DiT \Peebles and Xie, variant we introduce below, and illustrated in Figure 2. Following the diffusion training recipe, we add Gaussian noise to a clean video latent and train our diffusion model to remove such noise. At sampling time, starting from a latent pre-filled with noise, the model iteratively denoises the latent until obtaining a clean sample. The VAE decoder then decodes this latent into a video sample.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Latent Diffusion", "weight": 1.0} -->

Specifically, we train this video diffusion model with the flow matching objective \Lipman et al.,. Under a shifted schedule \Esser et al., that emphasizes higher noise levels, we add noise to an encoded video latent $z_{0}$ by $z_{k}=(1-k)z_{0}+k\epsilon$, where $k$ denotes the chosen noise level, $\epsilon\sim\mathcal{N}$ and $z_{k}$ is the noisy latent. The model $f_{\theta}$ is trained to predict the flow $\epsilon-z_{0}$ conditioned on the noisy latent $z_{t}$, conditioning $c$ (comprising the input image and text instruction), and noise level $t$, minimizing the matching loss \Lipman et al., $\mathcal{L}=||f_{\theta}(z_{k},c,k)-k(\epsilon-z_{0})||_{2}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Diffusion Forcing Transformer", "weight": 1.0} -->

A challenge in the video diffusion model is temporal coherence. In our formulation, the generated video must be coherent with not only the language instruction (text-to-video or t2v) but also the first frame (image-to-video or i2v) specified by the robot observation. In addition, one may want to condition the video generation on multiple previous frames (video-to-video or v2v) to generate multi-stage video plans. Traditionally, one achieves such conditioning by finetuning a t2v model to cross-attend to separate patches of the context frame(s) \Wan et al.,. We, however, propose to better satisfy this need with the recently proposed Diffusion Forcing framework.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Diffusion Forcing Transformer", "weight": 1.0} -->

Instead of adding a uniform level of noise to all tokens like in legacy video diffusion models, Diffusion Forcing \Chen et al., [2024a\] found that training video diffusion models with different noise levels at different frames has the additional benefit of flexibility and rollout stability. Since all the noise levels are random during training, at test time one can flexibly control the conditioning by selecting the desired noise level.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Diffusion Forcing Transformer", "weight": 1.0} -->

To learn i2v and v2v with a unified objective, we adopt diffusion forcing and apply different noise levels to context frames versus generated frames. As shown in Figure 2(b), given a diffusion transformer on a fixed number of latent frames, we first randomly sample a history length from $\{0,1,2,\ldots,6\}$ latent frames, splitting the video into a history segment and a future segment. We then apply independent noise levels to each segment and feed the resulting noisy video to our model, leaving all other settings unchanged. For example, if one adds zero noise to the first frame or first few frames at training time, the model will find it as a perfectly visible context frame and learn to condition on it; if the history frames have an intermediate noise level, the model treats it as partial information and learns to be robust to out-of-distribution context frames. In this way, we can flexibly condition on a clean first frame or multiple history frames at sampling time, by setting the their noise levels to 0.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Diffusion Forcing Transformer", "weight": 1.0} -->

Not only does this method eliminate an extra cross-attention to variable-length context tokens, but it's also compatible with existing DiT model weights without architectural changes. Following Song et al., we simply feed different noise level embeddings to different tokens in the DiT architecture, instead of uniform ones. This allows us to train a Diffusion Forcing model on top of the weights of a pre-trained video foundation model, WAN 2.1 14B \Wan et al.,. Following the practice of WAN 2.1 14B, we cross-attend to the CLIP features of the first frame as well as the text embeddings extracted by the UMT5 \Chung et al., encoder. Because Diffusion Forcing achieves context frame conditioning in a cleaner way, we remove WAN's mask and guidance channels used for image conditioning.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Enhanced Temporal Coherence with History Guidance", "weight": 1.0} -->

In addition to flexible conditioning and compatibility with legacy weights, our design can significantly enhance context coherence by enabling special sampling techniques from Diffusion Forcing \Chen et al., [2024a; Song et al., 2025\].

<!-- chunk {"id": "body-0023", "role": "body", "section": "Enhanced Temporal Coherence with History Guidance", "weight": 1.0} -->

Classifier-Free Guidance (CFG) \Ho and Salimans, is known to improve visual quality and conditioning adherence in visual generative models. WAN 2.1 utilizes a text-CFG that combines the output of a text-conditional diffusion model and that of an unconditional one. However, this still yields unsatisfactory motion fidelity and weak image conditioning as shown in Figure 5.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Enhanced Temporal Coherence with History Guidance", "weight": 1.0} -->

LVP adopts history guidance \Song et al. a CFG variant that performs guidance on any amount of context frames. Let $x_{k}$ denote the future segment to be diffused at noise level $k$ and $c_{\text{text}}$ the task instruction. As our model is trained with Diffusion Forcing, we can flexibly condition on a provided history segment $x_{\text{hist}}$ at sampling time by setting its noise level to zero, be it a single frame or a context video: Similarly, we can set the noise level of context frames to the maximum to fully mask out the context frames and obtain the unconditional score: To perform history guidance, we sample with the combined score Just as text-based CFG enhances adherence to text instruction, history guidance enhances adherence to context images.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Enhanced Temporal Coherence with History Guidance", "weight": 1.0} -->

compared to traditional text-based guidance, yielding physically viable plans with strong instruction following.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Autoregressive Extension for Multi-Stage Planning", "weight": 1.0} -->

Due to the flexible history conditioning, our model can extend a previously generated or captured video. The model supports up to 24 frames (6 latent frames in VAE space) as context. We can repeat video extension iteratively to generate multi-stage video plans. See Figure 7 and the videos on our website for multi-stage results.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Training Details", "weight": 1.0} -->

We train the model in two stages to progressively improve its visual planning capability and visual quality: Continue pretraining. Starting from Wan I2V 14B weights, we discard the weights that handle the extra masking and image guidance channels. We train on the full dataset for 60k steps with a batch size of 128, for a total of 200B tokens. At this stage, the model captures rich dynamics and strong instruction-following behavior, but the generated videos often exhibit excessive camera motion, which hinders smooth deployments on robots.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Training Details", "weight": 1.0} -->

Low camera motion finetuning. To reduce unwanted camera motion, we curate a smaller subset from Ego4D, Epic-Kitchens, and Panda datasets by selecting clips with a much lower average optical flow magnitude, and finetune for an additional 10k steps. This stage effectively suppresses camera drift and improves overall temporal smoothness and visual stability.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Training Details", "weight": 1.0} -->

The total training takes around 14 days with 128 H100 SXM5 GPUs.

<!-- chunk {"id": "body-0030", "role": "body", "section": "LVP-1M: A video dataset of human and robot actions", "weight": 1.0} -->

Training a video foundation model for embodied planning demands abundant data emphasizing diverse object interactions with action-centric text annotations. This contrasts with standard video datasets used for content-creation-oriented video generation \Kong et al., [2024; Wan et al., 2025\], which often prioritize aesthetic quality, cinematic shots, or dense captions of visual appearance and elements rather than motions. To this end, we curate LVP-1M, a diverse and high-quality dataset of 1.4M short clips showing humans or robots interacting with objects, each paired with multiple action-centric captions.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Video Sources", "weight": 1.0} -->

Given the vast availability of video data, we source raw videos from existing datasets before providing our own high-quality annotations. To ensure broad diversity across scenes, tasks, and embodiments, we combine robot teleoperation and human activity videos.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Video Sources", "weight": 1.0} -->

We start with web crawls widely used by video foundation models. We choose Pandas 70M \Chen et al., [2024b\] as a source of videos for heavy filtering. These internet-scale datasets contain diverse videos filtered for visual quality and captioned with visual content. They provide crucial scale and diversity that span countless tasks, scenes, and objects. However, only a small proportion of these videos capture detailed hand interactions with objects at sufficient resolution, not to mention near-zero robot coverage.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Video Sources", "weight": 1.0} -->

A second source of video comes from egocentric human activity datasets. These medium-scale datasets contain many annotated human--object interactions with moderate diversity but often suffer from large background motion due to camera movement. In addition, we found that atomic action annotations in these datasets still have lengths varying from seconds to minutes. We opt to draw videos from Ego4D \Grauman et al. Epic Kitchens \Damen et al. and Something-something \Goyal et al., dataset before heavy filtering, frame alignment and recaptioning.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Video Sources", "weight": 1.0} -->

A third source of videos come from robotics datasets featuring teleoperated robots performing tasks. While they provide knowledge about robot morphology, spanning parallel-jaw grippers to dexterous multi-fingered hands, they often have poor visual quality, poorly aligned frame rates, and limited diversity. Further, we found that short captions describing the task are often lacking, with many videos annotated with captions as vague as "pick", or not featuring a caption at all. We opt to select Bridge \Walke et al. Droid \Khazatsky et al. Language Table \Lynch et al. and AgiBot-World \Bu et al., for heavy captioning and frame alignment.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Video Sources", "weight": 1.0} -->

We provide a summary of video sources and their key properties in Table 1, examples from each dataset in Figure 3(a), and additional details in App. A. Together, we hope our model will achieve synergy by learning better instruction following from the diversity of web crawls, better object-hand interactions from egocentric human activities, as well as robotic morphologies from robot data.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Temporal Alignment", "weight": 1.0} -->

We train our model to generate 3-second action videos at 16 frames per second, as this provides a good trade-off between computational cost and action granularity. However, we observe that different datasets often feature varying-length clips for atomic actions, spanning 1 second to 1 minute. A closer examination reveals that robotics datasets contain motions much slower than those of humans performing the same tasks and are often recorded at drastically different frame rates, sometimes as low as 5 fps.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Temporal Alignment", "weight": 1.0} -->

Rather than naively aligning frame rates or trimming a video clip to a target length, we deem it important to align all clips to human speed to avoid temporal inconsistency - if a human normally finishes the task in 3 seconds, we resample the robot video (via upsampling or speeding up) so that it performs the same task in 3 seconds, regardless of its original frame rate or teleoperation speed. We achieve this by visually inspecting all datasets to determine the appropriate subsampling ratio following this principle. We also break down long-horizon tasks into atomic actions if any annotation contains multi-stage tasks. Some egocentric human activity datasets already provide action clip annotations, but we further refine them by trimming each clip precisely at the action's start and end points. As we found later in experiments, such alignment is critical to enhancing the transfer between different morphologies.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Quality Filtering", "weight": 1.0} -->

After temporal alignment, we first discard clips that are low-resolution, too short, too long, or poorly lit. We then apply some additional filters to focus the model on embodied motion planning: Filtering rapid camera motions. Many egocentric videos exhibit rapid camera rotations, leading to large background shifts and high training loss. These distract the model from learning meaningful foreground object motions. To mitigate this, we filter videos using optical flow statistics.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Quality Filtering", "weight": 1.0} -->

Ensuring visible embodiment. To avoid ambiguity, we require the embodiment (hand or robot gripper) to be clearly visible in the first frame. We use object detectors to automatically filter out clips where the embodiment is absent.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Quality Filtering", "weight": 1.0} -->

Expert motion. Many robot datasets contain suboptimal trajectories where the robot does not successfully accomplish the task. Traditionally, robot foundation models do not filter such data even when a "success" annotation is provided. However, we consider it important to remove these failure trajectories.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Quality Filtering", "weight": 1.0} -->

Filtering Pandas-70M subset. We perform three stages of progressive filtering to extract a subset focused on human interactions from the large Panda-70M dataset. First, we perform keyword-based filtering on captions using a whitelist (e.g., "grasping", "pull") and a blacklist (e.g., \"cartoon,\" \"video game\"). We then use human detectors to retain only clips containing one to four humans visible in the first, middle, and last frames. Finally, we perform another round of filtering with Gemini. For each video clip, we prompt Gemini with four questions to verify whether the clip contains rich human hand motions. We list more details of this in the Appendix A.1.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Action-Centric Re-Caption", "weight": 1.0} -->

To enhance the instruction following of our model, we generate multiple high-quality captions for each video. Traditionally, video foundation models favor extremely detailed captions describing all the visual elements. We observe that some robot datasets or ego-centric datasets only feature extremely short task descriptions as simple as one word, such as "pick". For these videos (e.g., DROID, Ego4D), we prompt Gemini Flash with the instruction and initial frame to create more detailed and varied captions. For videos that lack task annotations, we prompt Gemini with the entire video clip and ask it to describe the primary action and involved objects.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Action-Centric Re-Caption", "weight": 1.0} -->

In total, including repeated captions, we obtain 4.1 million captioned clips. We find that providing Gemini with a short description (e.g., "pick up a cup") substantially improves caption accuracy, as the video perception of Gemini tends to describe static scene contents well but struggles with fine-grained action dynamics. We make sure each video clip is paired with two to five distinct captions, some short, some extremely descriptive, to enhance linguistic diversity and improve training robustness.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Robot Actions from Video Plans", "weight": 1.0} -->

Given a camera observation and a task description, our large video planner can generate a video plan of a human hand or robot gripper executing the task. This section describes how we extract executable actions from a video plan and deploy them on robots.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Robot Actions from Video Plans", "weight": 1.0} -->

Our action extraction pipeline supports retargeting generated human hand video to a dexterous hand or even a simple robot gripper (see Appendix D.6). In this section, however, we primarily focus on one type of transfer: human hand video to dexterous robot hand execution, as the majority of our robot experiments are done with a humanoid robot with a dexterous hand.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Human Hand Motion Estimation", "weight": 1.0} -->

We reconstruct an accurate and temporally aligned hand pose as first step for motion retargeting. To do so, we first predict hand pose in each video frame independently using image-based hand reconstruction model:*HaMeR* \Pavlakos et al. then align and refine the predicted human hand with a dynamic scene reconstruction model, *MegaSAM* \Li et al.,.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Human Hand Motion Estimation", "weight": 1.0} -->

Per-frame Hand Pose Estimation. For each input frame $I_{t}$, *HaMeR* predicts MANO \Romero et al., hand vertices $\mathbf{V}_{t}$ and a global wrist orientation $\mathbf{R}_{t}\in\mathrm{SO}$ in the camera coordinate frame. While HaMeR provides accurate hand shape and articulation, its per-frame translation estimates tend to drift over time due to the lack of temporal consistency enforcement.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Human Hand Motion Estimation", "weight": 1.0} -->

4D Consistent Alignment. We then align the translations of the per-frame reconstructed human hand. Specifically, we leverage a 4D reconstruction model, *MegaSAM* \Li et al. which outputs per-frame depth maps $D_{t}(u,v)$, camera intrinsics $\mathbf{K}$, and extrinsics $\{\mathbf{E}_{t}\}_{t=0}^{T-1}$. After getting per-frame depth and camera pose, we backproject pixels of the hand into 3D, where pixels of the hand $(u_{t},v_{t})$ are obtained by projecting the MANO wrist joint regressed from $\mathbf{V}_{t}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Human Hand Motion Estimation", "weight": 1.0} -->

We retain HaMeR's orientation $\mathbf{R_{t}}$ while using the backprojected wrist pointclouds to estimate $\mathbf{T_{t}}$. This enforces temporal smoothness, resolves monocular scale ambiguity, and significantly improves wrist localization robustness.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Human Hand Motion Estimation", "weight": 1.0} -->

Temporal Completion and Smoothing. Frames with invalid depth/pixels are marked missing and linearly interpolated in position. Quaternions use SLERP with sign flips to maintain continuity. We then apply a causal Savitzky-Golay filter (window $w$, order $d$) to positions and quaternion components, followed by re-normalization, noted as $\hat{\mathbf{T}}_{\mathcal{R}\leftarrow\mathcal{W},t}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Robot Finger Motion Retargeting", "weight": 1.0} -->

Given the human hand pose estimated by the previous module, we design retargeting modules that support both multi-finger dexterous hands and parallel-jaw grippers. We introduce multi-finger dexterous hands below and parallel-jaw grippers in Appendix D.6.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Robot Finger Motion Retargeting", "weight": 1.0} -->

To retarget robot finger joints from human hands, we use *Dex-Retargeting* \Qin et al. which first extracts human hand keypoints using an RGB-based detector and then maps them to robot joint configurations by solving a DexPilot-style optimization objective. This produces robot finger joint angles $\mathbf{q}^{R}_{t}\in\mathbb{R}^{n_{\mathrm{dof}}}$, enabling fine-grained imitation of articulated human manipulation.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Robot Finger Motion Retargeting", "weight": 1.0} -->

We export per-frame wrist SE $\big(\hat{\mathbf{p}}^{\mathcal{R}}_{\mathcal{W},t},\hat{\mathbf{q}}^{\mathcal{R}}_{\mathcal{W},t},\hat{\mathbf{T}}_{\mathcal{R}\leftarrow\mathcal{W},t}\big)$ and robot joints $\{\mathbf{q}^{R}_{t}\}$, together with metadata (joint names, DOF). Qualitative checks are performed by rendering the robot hand motions in simulation, see videos in the project website.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Real-Robot Execution", "weight": 1.0} -->

Given the human wrist trajectories $\{\mathbf{P}_{t}\}_{t=0}^{T-1}$ and the robot finger joint trajectories $\{\mathbf{q}_{t}\}_{t=0}^{T-1}$ estimated by the preceding modules (both expressed in the camera coordinates of the first video frame), our goal is to execute the motion on a physical robot. We first rotate the wrist poses into the robot control frame, then use the resulting wrist translations and orientations to solve the inverse kinematics (IK) for the arm (using cuRoboSundaralingam et al. ), while the finger trajectories directly drive the robot hand joints.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Real-Robot Execution", "weight": 1.0} -->

Camera-to-Robot Alignment. Let $\mathcal{C}_{0}$ denote the coordinate frame of the first camera, $\mathcal{M}$ the MANO hand frame, and $\mathcal{R}$ the robot control frame. We align the recovered wrist poses from $\mathcal{C}_{0}$ to $\mathcal{R}$ via an extrinsic calibration. In practice, this reduces to applying a fixed rotation $\mathbf{M}\!\in\!\mathrm{SO}$ that unifies the axes of $\mathcal{C}_{0}$ and $\mathcal{R}$: where $\mathbf{p}^{\mathcal{C}_{0}}_{\mathcal{W},t}$ and $\mathbf{R}^{\mathcal{C}_{0}}_{\mathcal{W},t}$ are the wrist translation and rotation at time $t$ in $\mathcal{C}_{0}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Real-Robot Execution", "weight": 1.0} -->

We then assemble the wrist pose $\mathbf{T}_{\mathcal{R}\leftarrow\mathcal{W},t}\!\in\!\mathrm{SE}$ and its quaternion parameterization $\mathbf{q}^{\mathcal{R}}_{\mathcal{W},t}$ for downstream control.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Real-Robot Execution", "weight": 1.0} -->

Robot Wrist and Finger Execution. With the wrist trajectory expressed in $\mathcal{R}$, we use cuRoboSundaralingam et al. to solve IK and obtain arm joint trajectories that follow $\{\mathbf{p}^{\mathcal{R}}_{\mathcal{W},t},\,\mathbf{R}^{\mathcal{R}}_{\mathcal{W},t}\}_{t=0}^{T-1}$. In parallel, the finger joint sequence $\{\mathbf{q}_{t}\}_{t=0}^{T-1}$ is sent directly to the robot hand controller. Finally, the robot control API executes these synchronized arm and hand trajectories to complete the task.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Evaluating task-level generalization", "weight": 1.0} -->

Traditionally, robot foundation models are evaluated on tasks similar to those in their training sets - picking up slightly different objects at randomized locations after seeing a lot of pick-and-place trajectories, or folding t-shirts after learning from large amout of t-shirt folding data Brohan et al.; Kim et al.; Wang et al. \[2025b\]. We refer to these as object-level and configuration-level generalizations. They are exciting steps towards a zero-shot model but the "verbs" in the task description are constrained to this small set, like "pick" or "fold".

<!-- chunk {"id": "body-0059", "role": "body", "section": "Evaluating task-level generalization", "weight": 1.0} -->

We are interested in a stronger type of generalization - zero-shot task-level generalization: evaluating whether a model can perform drastically different tasks it has never encountered.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Third-party selection of novel tasks", "weight": 1.0} -->

We believe that true task-level generalization should allow any human to propose a task in any environment---without requiring prior knowledge of the capability of the model. To this end, we crowdsource test data from third-party participants by asking them to propose manipulation tasks from their everyday surroundings. Each participant was instructed to: propose a short manipulation task that takes 3--5 seconds for a human; take a photo of the scene showing both the hand and the target object; write a brief text description of the intended task; and stay diverse and challenging, be creative about tasks and scenes.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Third-party selection of novel tasks", "weight": 1.0} -->

After this step, we gathered around 200 tasks with very out-of-distribution scene like "at a gasoline pump", out-of-distribution yet hard tasks such as "flush the toilet" or "tear the tape". However, we noticed that some volunteers still submitted low quality data such as blurry photos or boring tasks. To ensure quality, a separate group of third-party annotators filtered out samples that did not follow instructions or resembled basic tabletop pick-and-push tasks already covered in existing robot datasets. After filtering, 100 high-quality tasks remained, each consisting of one observation image and an instruction text. The instruction texts were further refined using Gemini to produce more detailed task descriptions.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Evaluating video motion planning", "weight": 1.0} -->

We first evaluate the stand-alone performance of our video planner. We feed oberservation images and rephrased instruction texts to our model. Figure 6 shows qualitative examples of generated video plans on this in-the-wild test set. Figure 7 shows multi-stage video plans by extending generated videos repeatedly using our video-to-video generation.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Evaluating video motion planning", "weight": 1.0} -->

We compare against three strong video generation baselines: Wan 2.1 I2V 14B \Wan et al. Cosmos-Predict 2 14B \Agarwal et al. and Hunyuan I2V 13B \Kong et al.,. For each prompt, every method generates four videos.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Evaluating video motion planning", "weight": 1.0} -->

We design a four-level evaluation metric that measures instruction following, motion planning feasibility, and physical realism.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Evaluating video motion planning", "weight": 1.0} -->

Correct contact: The hand makes contact with the specified object at a correct location. Failures include touching the wrong object or making no contact.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Evaluating video motion planning", "weight": 1.0} -->

Correct end state: The final frame achieves the instructed goal (motion quality ignored).

<!-- chunk {"id": "body-0067", "role": "body", "section": "Evaluating video motion planning", "weight": 1.0} -->

Task complete: Both correct contact and correct end state with plausible, continuous motion (minor physics artifacts allowed).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Evaluating video motion planning", "weight": 1.0} -->

Perfect task complete: The task is completed with visually flawless physics and no noticeable artifacts. This highest level incorporates all prior criteria and additionally evaluates physical consistency and visual fidelity.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Evaluating video motion planning", "weight": 1.0} -->

Levels 1--2 test comprehension and prompt following---whether the model correctly interprets and interacts with the right objects. Level 3 evaluates whether the model can generate complete video planning with feasible and coherent motions. Level 4 additionally measures physical realism and overall visual fidelity.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Evaluating video motion planning", "weight": 1.0} -->

We ask third-party annotators to score all the generated videos and report both the average success rate and Best@4 (best result among four generations) for each level in Table 2, with quantitative comparisons illustrated in Figure 5.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Evaluating video motion planning", "weight": 1.0} -->

For all models, performance decreases monotonically from Level 1 to Level 4, reflecting the increasing difficulty of each criterion. While pretrained Wan 2.1 achieves relatively high scores on Level 1 (correct contact), its performance drops sharply on Levels 2--4, indicating that it can initiate the correct interaction but fails to produce coherent, task-complete motion trajectories. In contrast, our model achieves significantly higher scores across all levels, with the largest gains at Levels 3 and 4, indicating better generalization in producing coherent, physically consistent motion planning under in-the-wild conditions. Notably, our model attains a 59.3% success rate at Level 3 (Task Complete) on the third-party test set, highlighting its ability to perform coherent and semantically grounded motion planning for unseen tasks in unseen environments. In addition, in Figure 7, we illustrate how our model is able to rollout long video plans.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Evaluating video motion planning", "weight": 1.0} -->

Level 1: Correct contact Level 2: End state Level 3: Task complete Table 2: Video Plan Evaluation. Evaluation on 100 in-the-wild manipulation prompts collected from third-party participants. We report the average success rate (Average) and Best@4 for each level. Our method achieves substantially higher success at Levels 3–4 than the baselines, indicating stronger generation of coherent, task-complete plans in in-the-wild settings.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Evaluating Real-World Robot Manipulation", "weight": 1.0} -->

The previous experiment demonstrates that our large video planner exhibits strong zero-shot generalization for unseen tasks and novel scenes. We now evaluate the complete pipeline, from video generation to action retargeting and execution, on real-world robotic platforms.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Tasks", "weight": 1.0} -->

We conduct experiments on two distinct robot morphologies: a Franka Emika Arm with a parallel-jaw gripper and a G1 Arm equipped with an Inspire dexterous hand. Each platform is tested on task sets that highlight different manipulation capabilities. For the dexterous hand, we further evaluate challenging novel tasks such as opening a door, opening a box, and scooping coffee beans, as shown in the right columns of Figure 8.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Tasks", "weight": 1.0} -->

Task Set and Tasks Task Group A: w/ Parallel Gripper Task Group B: w/ Dexterous Hands Press Elevator Button Sweep Tennis Ball into Bucket Scoop Coffee Beans (b) Tear off Clear Tape (b) Task Group C: Out-of-distribution Set Pick Objects (OOD Object1) Pick A into B (OOD Object1) Pick Objects (OOD Scene2) Pick A into B (OOD Scene2) Figure 8: Robot Execution Evaluation. Left: Comparison of Task Success Across Methods on Franka Arm with Parallel-Jew Gripper and G1 with Inspire Hands. 1 denotes tests on OOD objects; 2 denotes scenes that differ substantially from the training videos. Right: Visualization of the robot tasks and experiments.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Tasks", "weight": 1.0} -->

Franka Arm with Parallel-Jaw Gripper As reported in Task Groups A and C of Table 8, this set focuses on manipulation tasks that can be achieved with simple two-finger grasps, such as object pick-and-place, block stacking, and bottle relocation. These tasks emphasize grasp detection and robust trajectory execution under limited actuation. Group A serves as the standard benchmark, while Group C primarily focuses on out-of-distribution task sets that contain unseen scenarios in the training video dataset. We include more details about gripper cases in Appendix D.6.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Tasks", "weight": 1.0} -->

Humanoid with Dexterous Hand As reported in Task Group B of Table 8, this set targets fine-grained dexterous manipulation requiring multiple degrees of freedom. Tasks include in-hand rotation, tool use (e.g., pen writing or screwdriver insertion), and precise placement of irregular objects. These tasks stress the ability of our method to transfer complex human hand articulations to the robot hand.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Baselines", "weight": 1.0} -->

We compare our method against several state-of-the-art vision-language-action baselines: $\pi_{0}$ \Black et al., [2024b\]: We evaluate $\pi_{0}$ model by loading the released checkpoint and directly testing its generalization to our benchmark tasks, following the standard usage protocol.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Baselines", "weight": 1.0} -->

OpenVLA \Kim et al.,: We include OpenVLA with its released checkpoint as a baseline, evaluating its performance on our task sets without additional fine-tuning.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Baselines", "weight": 1.0} -->

Note that $\pi_{0}$ and OpenVLA are not compatible with multi-finger dexterous hand settings and are therefore only tested on parallel-gripper tasks.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Results", "weight": 1.0} -->

Quantitative comparisons are presented in Table 8, and qualitative examples of successful executions are shown in Figure 9. Our approach exhibits strong zero-shot generalization on the most challenging settings---e.g., scooping coffee beans and tearing tape---underscoring the significance of the proposed method. Across both task suites, it consistently outperforms existing baselines, with especially outstanding performance on dexterous manipulation. In contrast, baselines show strong performance at tasks similar to training distributions, e.g. picking up objects, but struggle with task-level generalization. We speculate that such regression arises because imitation learning based robot foundation models have seen a lot of trajectories of pick-and-place, but have never seen enough diverse tasks to robustly generalize to new ones.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Limitations", "weight": 1.5} -->

Our approach has several limitations. On the video generation side, producing a single video plan takes several minutes on a single A100 GPU, making direct real-time deployment on robots intractable. Potential solutions include step-distillation methods Salimans and Ho; Yin et al., which reduce the number of inference steps, or causal video models Chen et al. \[2024a\]; Yin et al.; Huang et al., which lower the latency of the generation process. In addition, on the robotics side, our robot action extraction has several limitations. Our current robotics action extraction pipeline uses open-source models to estimate 4D reconstructions and hand pose estimations. Both of these models can make mistakes, sometimes leading to task failures. Even if all models succeed, the retarget might not be sufficient for certain dexterous hands. In addition, retargeting actions to the parallel-jaw gripper can be challenging due to its much lower degree-of-freedom count compared to a human hand. Finally, our overall robot execution framework is run in an open-loop manner, which is not sufficient for accomplishing dexterous tasks.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We investigate a different approach to robot foundation models with video as the backbone. We present Large Video Planner (LVP), a 14-billion parameter video foundation model for embodiment planning. LVP generates videos as motion plans conditioned on one or a few scene frames and a text description of the task. We demonstrate that these generated motion plans can be successfully retargeted to dexterous robotic hands using open-source reconstruction and retargeting tools. Evaluations on third-party proposed tasks show evidence of task-level generalization, a capability limited in existing VLA models. We open-source our model, data, and training code to support the research community and hope this work will inspire further exploration of video foundation model for robotics.
