<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Geometric Action Model for Robot Policy Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Generalist robot policies must follow user instructions while reasoning about how objects, cameras, and robot actions interact in the 3D physical world. Recent vision-language-action models (VLAs) and video world-action models (WAMs) inherit strong semantic or temporal priors from large-scale foundation models, but they still operate primarily on 2D image frames or 2D-derived latent spaces, leaving implicit the 3D geometry required for contact-rich manipulation. We propose the Geometric Action Model (GAM), a language-conditioned manipulation policy that directly repurposes a pretrained geometric foundation model (GFM) as a shared substrate for perception, temporal prediction, and action decoding. GAM splits the GFM at an intermediate layer: the shallow layers serve as an observation encoder, and a causal future predictor inserted at the split layer forecasts future latent tokens conditioned on language, proprioception, and action history. The predicted future tokens are then routed through the remaining GFM blocks for feature propagation and decoding, allowing a single backbone to produce both future geometry and actions. This design equips the GFM with language-conditioned temporal world modeling through minimal architectural modification while preserving its rich geometric priors.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Across a broad suite of simulation and real-robot manipulation benchmarks, GAM is more accurate, more robust, faster, and lighter than current foundation-model-scale baselines.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A long-standing goal in robotics is to build generalist manipulation policies that can follow natural-language instructions and manipulate arbitrary objects across diverse scenes. To achieve this, a general manipulation model must not only recognize objects and parse instructions, but also reason about how the physical world will evolve under its own actions. This requires a unified understanding of language, visual appearance, scene geometry, robot state, and physical dynamics.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent progress has therefore increasingly relied on large-scale foundation models as pretrained substrates for robot policies. Vision-language-action models (VLAs) build on vision-language models whose representations are aligned with natural language, and learn to map visual and linguistic tokens to robot actions. Video world-action models (WAMs) instead leverage pretrained video generation models, using their world prediction priors to jointly model future frames and actions. While these approaches have shown impressive language-conditioned manipulation ability, they are fundamentally in 2D: 3D cues such as depth, scale, and occlusion are left implicit in monocular cues that the action decoder must disentangle on its own, leading to limited generalization across environment changes, especially in robot initial state and camera viewpoint.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To overcome this limitation, recent work incorporates 3D geometric information into robot policies. One line learns policies directly on explicit 3D observations such as raw point clouds, demonstrating the value of geometry for generalization but typically requiring task-specific encoders trained from scratch. With the emergence of Geometric Foundation Models (GFMs), some works transfer pretrained geometric priors into VLA policies, either distilling selected GFM features into the VLA backbone through representation alignment or attaching a lightweight action head on top of a GFM's final features. These improve spatial awareness, but use the GFM only as a static feature extractor: its multi-layer geometric structure is never repurposed as the policy's own temporal and action-generating substrate.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose Geometric Action Model (GAM), which directly repurposes a GFM as a manipulation policy by using it as a shared medium for perception, future-state prediction, and action decoding. We show that by jointly predicting future action and geometry, geometric world dynamics can be inherently incorporated into robot policies.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, we split the pretrained GFM at an intermediate layer: the shallow layers serve as an observation encoder, while the remaining layers serve as a decoder block. Given the current visual observation, the observation encoder extracts spatially meaningful scene representations. To model how the world evolves over time, we insert a causal transformer at the intermediate layer that predicts future feature representations. This predictor is conditioned on task language, proprioception, and action history by introducing them as additional tokens at each timestep. The predicted future-state tokens are then processed by the remaining GFM decoder together with an action token, allowing the backbone to produce both future geometry and robot actions. An intuitive comparison between existing paradigms and our proposed framework is illustrated in Figure 2.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Across diverse simulation and real-world benchmarks, GAM matches or exceeds the success rate of current foundation-model-scale baselines such as VLAs and WAMs while using substantially fewer trainable parameters and substantially faster inference (55$\times$ faster), and shows improved generalization to unseen scenarios. GAM especially achieves outstanding performance in camera perturbation settings ($\uparrow$`<!-- -->`{=html}9.7%p), which requires geometric understanding priors.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contributions are as follows: We introduce Geometric Action Model (GAM), a manipulation policy that combines temporal world modeling, latent feature-space prediction, and a geometric foundation-model substrate in a single shared-backbone architecture.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that action and geometry can be predicted in a shared token space: a single autoregressive sequence and a single backbone forward pass produce both action tokens and future-scene tokens, decoded by a lightweight action regression head and a depth head.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate that across diverse simulation and real-world manipulation benchmarks, GAM is simultaneously more accurate, more robust, faster, and lighter than current foundation-model-scale alternatives.

<!-- chunk {"id": "body-0013", "role": "body", "section": "GAM: Geometric Action Model", "weight": 1.0} -->

Problem Formulation. We consider language-conditioned robot manipulation. At each timestep $t$, the robot receives a multi-view RGB observation $o_{t}=\{I_{v,t}\}_{v=1}^{V}$ from $V$ fixed cameras, a proprioceptive state $s_{t}\in\mathbb{R}^{d_{s}}$ describing the robot's joint configuration and end-effector pose, and a natural-language task instruction $\ell$ that is held constant throughout an episode. The policy $\pi_{\theta}$ must produce an action chunk $\hat{a}_{t}\in\mathbb{R}^{C\times d_{a}}$ of length $C$, encoding the next $C$ delta-pose or joint commands to be executed open-loop before the next observation is acquired.

<!-- chunk {"id": "body-0014", "role": "body", "section": "GAM: Geometric Action Model", "weight": 1.0} -->

We learn a policy: from a dataset of $N$ expert demonstrations $\mathcal{D}=\{(\tau_{i},\ell_{i})\}_{i=1}^{N}$, where each trajectory $\tau_{i}=(o_{t},s_{t},a_{t})_{t=1}^{T_{i}}$ pairs a sequence of observations, states, and executed action chunks with a fixed instruction $\ell_{i}$. The policy conditions on a context window of $H$ recent timesteps.

<!-- chunk {"id": "body-0015", "role": "body", "section": "GAM: Geometric Action Model", "weight": 1.0} -->

Overview. In the following sections, we explain how we transform a pretrained GFM into a language-conditioned world-action model. Our key idea is to split the GFM into two parts and insert a causal temporal predictor between them. This design lets GAM formulate future prediction directly inside the GFM latent space, enabling all predictive computation to be performed in the GFM's geometric representation space.

<!-- chunk {"id": "body-0016", "role": "body", "section": "GAM: Geometric Action Model", "weight": 1.0} -->

Concretely, our framework operates in three sequential stages inside the GFM. First, the observation encoder (§4.1) repurposes the shallow layers of the GFM to extract latent geometric features from multi-view observations. Next, the causal future predictor (§4.2) operates at the split layer, where it combines these geometric features with language, proprioception, and action history to predict future latent tokens. Finally, during feature propagation and decoding (§4.3), the predicted future tokens are routed through the remaining deep GFM blocks to simultaneously decode future geometry and the final action chunk $\hat{a}_{t}$. Figure 3 (a) shows the overall architecture of our model.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Observation Encoder", "weight": 1.0} -->

We first reuse the shallow layers of the pretrained GFM as the observation encoder. Let $L_{s}$ denote the split layer where the causal future predictor is inserted. The original GFM transformer stack is then decomposed into an encoder and a decoder: Here, the choice of $L_{s}$ is important because $L_{s}$ must be deep enough to extract sufficiently rich visual features from the raw observations, yet shallower than the earliest layer used in the DPT head $L_{s}<m_{1}$, so that predicted future states can be decoded into future geometries by the DPT heads.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Observation Encoder", "weight": 1.0} -->

After defining this split layer $L_{s}$, for each timestep $t^{\prime}$ in the context window, we tokenize the multi-view RGB observation $o_{t^{\prime}}=\{I_{v,t^{\prime}}\}_{v=1}^{V}$ using the original GFM patch embedding. This produces the initial multi-view token sequence: where each view contributes one camera token and $P$ patch tokens. The observation encoder maps these tokens to the split-layer representation $\mathbf{Z}_{t^{\prime}}^{(L_{s})}$. By applying this encoding independently to each timestep in the context window, the output of this stage is a sequence of per-timestep geometric latent states $\{\mathbf{Z}_{t-H+1}^{(L_{s})},\ldots,\mathbf{Z}_{t}^{(L_{s})}\}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Causal Future Predictor", "weight": 1.0} -->

After the observation encoder, GAM performs temporal prediction directly at the split layer $L_{s}$, forecasting the next latent geometric state from current and past observations while conditioning on the task instruction, proprioception, and action history. To this end, we insert a causal future predictor $g_{\phi}$ between the shallow encoder $E_{\leq L_{s}}$ and the deep decoder $D_{>L_{s}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Causal Future Predictor", "weight": 1.0} -->

For each timestep $t^{\prime}$ in the context window, the encoder provides latent tokens $\mathbf{Z}_{t^{\prime}}^{(L_{s})}$, and we embed the proprioceptive state $s_{t^{\prime}}$ and previous action $a_{t^{\prime}-1}$ as tokens: with $\psi_{s},\psi_{a}$ lightweight projection layers, and the instruction $\ell$ into language tokens $\mathbf{L}_{\ell}$ with a pretrained text encoder.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Causal Future Predictor", "weight": 1.0} -->

The combined sequence $\mathbf{X}$ is then processed through block-causal self-attention, ensuring the model incorporates past and present contexts without future leakage, as illustrated in Figure 3 (b). At the final layer of the predictor $g_{\phi}$, we read off the predictions from their respective sequence slots. Specifically, the hidden states corresponding to the geometry slots forecast the latent geometric tokens of the future frame, denoted as $\tilde{\mathbf{Z}}_{t^{\prime}+1}^{(L_{s})}$. Concurrently, the hidden state of the designated previous-action slot is projected to produce a predicted next action token $\tilde{\mathbf{a}}_{t^{\prime}}\in\mathbb{R}^{d}$, in direct analogy to next-token prediction in a causal language model. By jointly forecasting action and geometric latents in this layer, we ensure that action tightly interacts with spatial representations.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Causal Future Predictor", "weight": 1.0} -->

This design of introducing a causal transformer predictor $g_{\phi}$ allows the pretrained GFM to acquire language-conditioned temporal world modeling with minimal architectural modification. Only the inserted $g_{\phi}$ needs to learn how to fuse language, proprioception, and action history with GFM latent features. The resulting predictions, $\widetilde{\mathbf{Z}}_{t^{\prime}+1}^{(L_{s})}$ and $\tilde{\mathbf{a}}_{t^{\prime}}$, are then passed to the remaining GFM blocks for joint geometry and action decoding.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Feature Propagation and Action Decoding", "weight": 1.0} -->

We perform this *feature propagation* by appending each view's corresponding action token $\tilde{\mathbf{a}}_{v,t^{\prime}}$ directly to its geometry token sequence for each timestep: To prevent future leakage, we extend the predictor's causal mask strategy to the GFM's remaining global attention layers ($f_{\text{global}}^{(m)}$).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Feature Propagation and Action Decoding", "weight": 1.0} -->

Finally, the propagated features are decoded by two heads. The lightweight action head $h_{\text{act}}$ aggregates action tokens over the context window to regress the executable action chunk $\hat{a}_{t^{\prime}}$, while the original GFM depth head $h_{\text{depth}}$ decodes geometry tokens into action-aligned future depth maps. The GFM's deep blocks, originally pretrained to decode shallow features into 3D geometry, are thus repurposed here as the decoder of the world model's predicted future.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Training and Inference", "weight": 1.0} -->

The policy is trained end-to-end by minimizing a multi-task objective over action execution, world modeling, and geometric decoding: where the $\lambda$ factors balance each term and $\mathcal{H}=\{t-H+1,\ldots,t\}$ is the context window. The *action* loss $\mathcal{L}_{\text{act}}$ is an $\ell_{1}$ regression between the decoded action chunk $\hat{a}_{t^{\prime}}$ and the expert action $a_{t^{\prime}}$ over all $t^{\prime}\in\mathcal{H}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Training and Inference", "weight": 1.0} -->

The *future-feature* loss $\mathcal{L}_{\text{feat}}$ anchors the predictor $g_{\phi}$ to temporal geometric transitions by aligning predicted future tokens $\tilde{\mathbf{Z}}_{t^{\prime}+1}^{(L_{s})}$ with the actual next frame $\mathbf{Z}_{t^{\prime}+1}^{(L_{s})}$ extracted from frozen GFM: The *future-depth* loss $\mathcal{L}_{\text{depth}}$ grounds the predicted future in valid 3D structure by supervising the decoded depth $\tilde{D}_{t^{\prime}+1}=h_{\text{depth}}(\tilde{\mathbf{Z}}_{t^{\prime}+1}^{(m^{*})})$ using depth head $h_{\text{depth}}$ against ground-truth future depth

<!-- chunk {"id": "body-0027", "role": "body", "section": "Training and Inference", "weight": 1.0} -->

$D_{t^{\prime}+1}$, adopting the scale-invariant and gradient-matching penalties of the GFM.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Training and Inference", "weight": 1.0} -->

At inference, we maintain the historical context online with key-value caching, so each step processes only the new observation $o_{t}$ and previous action $a_{t-1}$ in a single feed-forward pass.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

We use DA3-Giant fine-tuned on Track4World as the backbone. We insert a 12-layer causal predictor with width $d_{g}=1024$ at layer $L_{s}=12$, where alternating attention begins. For the task instruction, we extract language tokens using a frozen T5 encoder. The policy uses a context horizon of $H=4$ for pre-training and $H=1$ for post-training and predicts $C=8$ step action chunks in a $d_{a}=7$ end-effector action space from $d_{s}=7$ proprioceptive states. We pretrain GAM on 784K single-arm robot trajectories from RoboCasa365, MimicGen, and OpenX-Embodiment, then post-train it on each benchmark. We optimize with AdamW using a constant learning rate, freeze layers before $L_{s}$ and the depth head, and supervise depth with simulator ground truth.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Simulation Benchmarks. We evaluate generalization across distinct axes using two simulation benchmarks. Specifically, we train our policy on LIBERO, a lifelong single-arm manipulation benchmark spanning diverse spatial layouts, object identities, and task goals. To rigorously assess out-of-distribution robustness, we then evaluate the trained models in a zero-shot manner on LIBERO-Plus, which introduces controlled environmental perturbations across dimensions such as camera viewpoint, lighting, and backgrounds. We report additional results in the appendix.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Real-Robot Setup. We train on four manipulation tasks ($\sim$`<!-- -->`{=html}200 demonstrations each) using wrist-mounted and third-person cameras, adhering to the simulation protocol. Since ground-truth geometry is unavailable in the real world, target future depth maps are obtained as pseudo-labels directly from the pretrained backbone GFM. We evaluate robustness via 20 trials per task, divided equally between nominal setups and perturbed environments, specifically varying external camera positions. See the appendix for robot environment with full task and evaluation details.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Baselines. We compare GAM against representative baselines from three families discussed in §2: VLAs, WAMs, and geometry-aware VLAs. For the real-robot setup, we compare against $\pi_{0.5}$ and Spatial Forcing. For fairness, comparisons utilize a matched evaluation protocol, with performance numbers either re-evaluated using available checkpoints or taken directly from their respective published benchmarks.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Main Results", "weight": 1.0} -->

Simulation Results. As shown in Table 1, GAM achieves highly competitive success rates on the standard LIBERO benchmark, where performance is heavily saturated. Crucially, on the more challenging LIBERO-Plus benchmark, our model consistently outperforms competing baselines, demonstrating a remarkable improvement in the camera-perturbation setting ($\uparrow$`<!-- -->`{=html}9.7%p). This gain highlights the advantage of our end-to-end integration of the GFM. While existing geometry-aware VLAs only partially exploit GFM representations, GAM embeds the GFM throughout its entire predictive pathway to yield a deeply geometry-aware policy.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Main Results", "weight": 1.0} -->

Real-world Results. To examine whether the gains observed in simulation transfer to physical execution, we additionally evaluate GAM in a real-world setting. Figure 4 shows that GAM substantially outperforms all baselines. In particular, our model remains robust under out-of-domain conditions (the camera-perturbation setting) where other baselines struggle. These results demonstrate that GAM generalizes to the real-world domain and is robust under perturbations, owing to its thorough exploitation of the GFM when training the policy.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Post-training Component Analysis", "weight": 1.0} -->

Table 2 summarizes ablation study of key post-training components on Object suite of LIBERO and LIBERO-Plus. Pretraining is crucial for robustness: omitting it mildly affects nominal LIBERO but severely degrades LIBERO-Plus. With a pretrained backbone, removing $L_{\text{depth}}$ or $L_{\text{feat}}$ has minimal impact, suggesting geometric dynamics are already encoded. Notably, even without pretraining, these future-prediction losses provide strong geometric supervision and substantially improve robustness on LIBERO-Plus. Finally, the horizon ablation shows that $H=1$ is sufficient and more robust than longer histories, consistent with prior observations that extended context can introduce spurious correlations.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Post-training Component Analysis", "weight": 1.0} -->

Split Layer $L_{s}$ Selection. Table 3 evaluates the depth of future predictor by shifting the split layer $L_{s}$ and re-initializing the predictor. We exclude future-depth loss in this experiment because it is not equally applicable to all split layers and could isolate the effect of $\mathcal{L}_{\text{feat}}$ itself. Our default choice of $L_{s}=12$ achieves peak performance, validating it as the optimal seam between frame-wise and cross-view attention. While layer 19 remains competitive, inserting the predictor too early ($L_{s}=0$) or late ($L_{s}\in\{27,33,39\}$) causes total performance collapse. This confirms that forecasted tokens require sufficient interaction through deep layers to properly integrate into the pretrained 3D geometric prior.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Analysis", "weight": 1.0} -->

Inference Speed and Model Size. As shown in Table 4, GAM achieves the lowest latency among all baselines, requiring only 6.9 ms ($\approx$`<!-- -->`{=html}145 Hz) for a single feed-forward pass and running up to 55$\times$ faster than the diffusion-based Cosmos Policy.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Analysis", "weight": 1.0} -->

All methods are benchmarked under the same setup, with further details provided in the appendix. By utilizing single-pass prediction, GAM avoids the multi-step denoising of diffusion policies, achieving low latency while matching prior accuracy and robustness with only 1.4B parameters.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Analysis", "weight": 1.0} -->

Robustness to Viewpoint and Scene Variation. Figure 5 further breaks down the camera-perturbation results by difficulty level of LIBERO-Plus. GAM achieves consistently higher success rates than all baselines at every level, and the advantage remains clear even under the strongest perturbations.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conclusion and Limitation", "weight": 1.5} -->

We introduced Geometric Action Model, which unifies geometry and action prediction with temporal world modeling inside a single shared GFM. By inserting a causal transformer between the GFM's shallow and deep layers, GAM autoregressively decodes actions and future geometries, resolving the spatial ambiguities of traditional foundation-model substrates. Across extensive simulation and real-world benchmarks, GAM achieves superior accuracy, faster inference, and strong out-of-distribution robustness to environmental perturbations. The framework also has limitations. Its language reasoning and commonsense capabilities are bounded by the frozen text encoder; integrating a large language model or an external reasoning module is a natural next step.
