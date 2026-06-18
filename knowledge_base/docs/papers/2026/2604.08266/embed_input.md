<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Orion-Lite: Distilling LLM Reasoning into Efficient Vision-Only Driving Models

Topics include Autonomous driving, Large language models, Language models, Vision-language models, Benchmarks, Planning, Orion-Lite, Vision-language-action model.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Leveraging the general world knowledge of Large Language Models (LLMs) holds significant promise for improving the ability of autonomous driving systems to handle rare and complex scenarios. While integrating LLMs into Vision-Language-Action (VLA) models has yielded state-of-the-art performance, their massive parameter counts pose severe challenges for latency-sensitive and energy-efficient deployment. Distilling LLM knowledge into a compact driving model offers a compelling solution to retain these reasoning capabilities while maintaining a manageable computational footprint. Although previous works have demonstrated the efficacy of distillation, these efforts have primarily focused on relatively simple scenarios and open-loop evaluations. Therefore, in this work, we investigate LLM distillation in more complex, interactive scenarios under closed-loop evaluation. We demonstrate that through a combination of latent feature distillation and ground-truth trajectory supervision, an efficient vision-only student model \textbf{Orion-Lite} can even surpass the performance of its massive VLA teacher, ORION.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Setting a new state-of-the-art on the rigorous Bench2Drive benchmark, with a Driving Score of 80.6. Ultimately, this reveals that vision-only architectures still possess significant, untapped potential for high-performance reactive planning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, Vision-Language Models (VLMs) and Vision-Language-Action (VLA) architectures have emerged as a dominant paradigm in autonomous driving research. By integrating Large Language Models (LLMs) with vision encoders and aligning them with through visual question-answering (VQA), these methods can leverage the rich world knowledge embedded in LLMs. This integration of LLM modules introduces explicit causal reasoning into VLA driving models, allowing them to better optimize driving trajectories in complex, interactive scenarios.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consequently, VLA models currently achieve state-of-the-art performance across multiple autonomous driving benchmarks. However, their reliance on massive LLMs introduces severe computational bottlenecks, including prohibitive GPU memory consumption and high inference latency. While many of these architectures possess Chain-of-Thought (CoT) capabilities for multi-turn visual reasoning, their practical closed-loop deployment typically relies on "direct" modes to mitigate latency. In this direct mode, intermediate reasoning steps are bypassed entirely, and the LLM is prompted with a static, pre-defined instruction template to generate latent waypoints. This essentially renders the LLM as a feature extractor.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While recent works have explored knowledge distillation to mitigate these bottlenecks, the efficacy of distilling LLMs for more challenging closed-loop driving scenarios remains an open question. For instance, DiMA demonstrates improved inference speed by distilling LLM knowledge into a vision-only model, but its evaluation is strictly limited to open-loop metrics. Similarly, VERDI performs distillation from Qwen-2.5-VL for closed-loop evaluation on HugSim. However, it primarily compares its student model against older baselines like UniAD rather than against its own teacher model. Consequently, how much performance a student model can maintain relative to its teacher in more realistic, interactive environments remains underexplored. This brings us to our core research question: how can the "reasoning" capabilities of an LLM inside a VLA be efficiently distilled without suffering a performance gap in challenging, closed-loop scenarios?

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To answer this question, we select Bench2Drive as our rigorous closed-loop evaluation environment. Bench2Drive is the first benchmark comprehensively designed to assess an end-to-end autonomous driving (E2E-AD) system's multi-ability performance in a closed-loop manner, introducing 44 interactive scenarios (e.g., cut-ins, overtaking, detours), 23 weather conditions, and 12 distinct towns. Historically, evaluating E2E-AD methods relied on open-loop datasets (e.g., nuScenes ) using L2 displacement errors and collision rates, which often fail to reflect actual driving performance. In fact, the average open-loop box collision rate on Bench2Drive is $4.5 \times$ higher than on nuScenes (using UniAD, VAD, and ORION as baselines ), highlighting the dataset's inherent complexity. Conversely, existing closed-loop protocols (e.g., Town05Long and Longest6) typically rely on a small set of fixed routes, where the standard driving score exhibits high variance due to unsmoothed metric functions and route randomness.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Bench2Drive bridges this gap by having more environments and scenarios, offering a stable, highly interactive evaluation standard.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Focusing on this challenging benchmark, we take the currently publicly available state-of-the-art VLA model, ORION, and investigate the effect of different distillation strategies on our proposed student model, Orion-Lite, which replaces the heavy LLM with a lightweight transformer decoder. We find that, when employing a synergistic combination of latent distillation and ground-truth trajectory supervision, Orion-Lite surprisingly surpasses its 7B-parameter ORION teacher. Not relying on an LLM, Orion-Lite accelerates the reasoning module's inference by $150 \times$, tripling the overall system speed. Moreover, it reduces total GPU memory usage from 31 GB to 8 GB, making it more suitable for actual deployment. Furthermore, qualitative analysis reveals that our distilled model exhibits superior robustness in complex edge cases where the original ORION model hesitates or fails. This lightweight, vision-only architecture achieves new state-of-the-art performance on the standard Bench2Drive benchmark, outperforming its teacher VLA-based ORION, the online Reinforcement Learning based MindDrive, and the World Model based UniDrive-WM.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

While we do not introduce a fundamentally novel distillation algorithm, the core contribution of our work lies in the empirical demonstration that a standard distillation loss, combined with ground-truth trajectory supervision, allows a highly compressed student model to surpass its teacher's performance ceiling for challenging scenarios and under closed-loop evaluation. This suggests that the causal reasoning capability required for autonomous driving does not strictly need to manifest through a massive LLM during inference, positioning efficient visual reasoning as a highly promising direction for future research. In this work, we report these empirical findings and perform ablation studies to explore this phenomenon. A more exhaustive analysis of the underlying mechanisms is deferred to future work.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Architectural Simplification: we demonstrate that a compact and lightweight transformer decoder can replace a 7B-parameter LLM in a VLA driving model without compromising performance on current challenging closed-loop benchmarks. This heavily suggests that for standard, reactive E2E trajectory planning, massive LLMs may not be strictly necessary for inference.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

State-of-the-Art Vision-Only Model: we show that when our shallow student model is trained jointly with feature distillation and ground-truth supervision, it effectively outperforms the teacher's driving capabilities. Our method achieves new state-of-the-art results on the Bench2Drive closed-loop evaluation, outperforming competing VLA, RL, and WM methods using only a fraction of the computational resources.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Open Source: To facilitate reproducibility and support future research in efficient autonomous driving, all code, model weights, and evaluation scripts will be made publicly available upon acceptance.

<!-- chunk {"id": "body-0014", "role": "body", "section": "End-to-End Autonomous Driving", "weight": 1.0} -->

End-to-end (E2E) autonomous driving frameworks effectively map raw sensor inputs directly to planning trajectories or control signals. UniAD pioneered this direction by unifying perception, prediction, and planning into a single framework. To enhance safety, VAD incorporated vectorized planning constraints, while VADv2 transitioned to a probabilistic paradigm. Recently, approaches like DiffusionDrive have been employed to capture multimodal trajectory distributions, and methods such as LAW and WoTE integrate next-frame prediction as an implicit world model to enhance the vision encoder's spatial-temporal representations. Despite these advancements, many E2E methods still suffer from error accumulation in closed-loop scenarios. To address this, DriveTransformer proposed a unified transformer framework processing perception and planning in parallel, achieving strong results on Bench2Drive. Our work builds upon this vision-only E2E paradigm but diverges significantly: we demonstrate that a high-performance vision-only model can be derived by distilling the latent cognitive capabilities of a complex VLA teacher into a drastically lighter decoder, indicating that current vision-only architectures still possess significant, untapped potential.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Vision-Language Models", "weight": 1.0} -->

The integration of LLMs into autonomous driving has led to the emergence of VLA models. EMMA utilizes Gemini to generate future trajectories natively as text tokens. OpenEMMA extends this to open-source VLMs but relies on auxiliary 3D modules. DriveVLM adopts a dual-system approach for trajectory refinement. Recently, Alpamayo-R1 demonstrated that reinforcement learning post-training can further improve reasoning quality and reasoning-action consistency. ORION and OmniDrive explore using LLMs to condition generative planners. More recent works incorporate online Reinforcement Learning (MindDrive ) and World Models (UniDrive-WM ). Crucially, in architectures like ORION and MindDrive, the final driving trajectory is decoded directly from the LLM's latent hidden states rather than its textual output. This architectural trait effectively renders the LLM as an overparameterized feature extractor. Our work capitalizes on this insight, challenging the necessity of the massive LLM during inference for standard E2E reactive planning tasks.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Knowledge Distillation", "weight": 1.0} -->

Knowledge distillation (KD) transfers capabilities from heavy teacher models to lightweight student models. DriveAdapter, Hydra-MDP, and Hydra-MDP++ distill knowledge from a heavy vision-centric teacher to a more efficient vision-only student model. Distinct from these methods, our work focuses specifically on distilling the reasoning capabilities of the LLM within a VLA model into a vision-only student.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Knowledge Distillation", "weight": 1.0} -->

More directly relevant to our paradigm are VERDI and DiMA, which distill VLM knowledge into vision models. VERDI aligns the VLM's text output with the vision model's predictions using complex progressive feature projectors. DiMA explores distilling VLM features via KL-divergence but limits its evaluation to open-loop metrics. We advance this research by directly distilling the continuous latent LLM features using simple $\mathcal{L}_{1}$ regression, avoiding auxiliary text encoders, offline rule-based experts, and suboptimal distributional metrics. Furthermore, we validate our framework in highly complex, realistic closed-loop evaluations.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Method", "weight": 1.0} -->

In this section, we detail our proposed knowledge distillation framework, designed to effectively compress the massive LLM inside a VLA driving model without sacrificing performance in complex, closed-loop scenarios. The overall pipeline is illustrated in Figure 1. Our framework utilizes the state-of-the-art ORION as the teacher model. To create our highly efficient, vision-only end-to-end model, we introduce a lightweight distillation module (Section 3.3) that transfers the latent reasoning representations from the teacher LLM to a shallow transformer decoder. To avoid computational redundancy during distillation, we utilize the teacher's intermediate state embeddings (Section 3.2) to represent the dense visual and contextual information.

<!-- chunk {"id": "body-0019", "role": "body", "section": "State Embedding Extraction", "weight": 1.0} -->

Following the ORION architecture, we first extract multi-view image features $F_{m}$ from the frozen vision encoder. The QT-Former, a query-based temporal module, employs learnable scene queries $Q_{s} \in {\mathbb{R}}^{N_{s} \times C_{q}}$ and perception queries $Q_{p} \in {\mathbb{R}}^{N_{p} \times C_{q}}$, where $N_{s}$ and $N_{p}$ denote the number of queries and $C_{q}$ represents the channel dimension.

<!-- chunk {"id": "body-0020", "role": "body", "section": "State Embedding Extraction", "weight": 1.0} -->

These queries exchange information via self-attention and subsequently interact with the image features $F_{m}$ through cross-attention. The perception queries are then routed to task-specific heads for object detection, traffic state recognition, and dynamic agent motion prediction. To efficiently aggregate historical context, ORION utilizes history queries $Q_{h} \in {\mathbb{R}}^{N_{h} \times C_{q}}$ alongside a long-term memory bank $M \in {\mathbb{R}}^{{({N_{h} \times n})} \times C_{q}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "State Embedding Extraction", "weight": 1.0} -->

The final concatenated features comprising the map vision embedding, ego-vehicle status, and the driving command serve as the input tokens $T_{c} \in {\mathbb{R}}^{N_{c} \times C_{c}}$ for our student model, where $N_{c}$ is the sequence length and $C_{c}$ is the channel dimension. In the teacher model, the LLM processes $T_{c}$ alongside tokenized text prompts to output the latent planning tokens $T_{p} \in {\mathbb{R}}^{1 \times C_{p}}$. For our student framework, we discard the text prompts entirely to achieve a vision-only architecture, utilizing the teacher's $T_{p}$ as the pseudo-ground truth distillation target.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Lightweight Distillation Module", "weight": 1.0} -->

Our student module replaces the massive 7B-parameter LLM with a highly efficient transformer-based architecture. This module consists of an input projection layer, a learnable planning query, a shallow standard transformer decoder, and an output projection layer.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Lightweight Distillation Module", "weight": 1.0} -->

The input projection, implemented as a linear layer followed by layer normalization, compresses the input token channels from $C_{c}$ to a hidden dimension $C_{h}$, yielding the compressed tokens $T_{cc} \in {\mathbb{R}}^{N_{c} \times C_{h}}$. To emulate the generative planning mechanism of the LLM, we initialize a learnable planning query $Q_{plan} \in {\mathbb{R}}^{1 \times C_{h}}$. Through the cross-attention mechanism within the 6-layer transformer decoder, $Q_{plan}$ (Query) attends to the dense compressed tokens $T_{cc}$ (Key/Value), extracting the critical spatio-temporal features necessary for trajectory generation. Finally, the output projection layer maps the decoder's output back to the original planning token dimension $C_{p}$, perfectly aligning the student's output space with the teacher's generative planner.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Lightweight Distillation Module", "weight": 1.0} -->

This bottleneck design effectively retains essential planning information to manage complex scenarios while drastically reducing computational overhead.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Training Objectives", "weight": 1.0} -->

Feature Mimic Loss. Let $T_{student} \in {\mathbb{R}}^{1 \times C_{p}}$ denote the final projected output of the student decoder. Using the teacher's generated planning tokens $T_{p}$ as the target, we apply an $\mathcal{L}_{1}$ regression loss, $\mathcal{L}_{mimic}$, to minimize the representational divergence.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Training Objectives", "weight": 1.0} -->

Joint Distillation and E2E Supervision. Rather than relying on the LLM's latent features only, our training phase jointly optimizes the newly initialized transformer decoder alongside the pre-trained VAE generative planner. Throughout this process, the pre-trained vision encoder and QT-Former are kept strictly frozen with weights initialized from ORION. Because the vision encoder already captures robust spatial-temporal representations, we focus the gradient updates entirely on the lightweight student decoder and the ensuing planner.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Training Objectives", "weight": 1.0} -->

Following standard E2E formulations, we incorporate environmental feedback via collision loss $\mathcal{L}_{col}$ and boundary loss $\mathcal{L}_{bd}$. Furthermore, we apply an $\mathcal{L}_{1}$ regression loss $\mathcal{L}_{reg}$ for deterministic trajectory prediction. To properly align the reasoning and action spaces within the generative planner, we retain the Kullback--Leibler divergence loss $\mathcal{L}_{vae}$ adopted by the ORION teacher. To clearly separate supervision signals, we decompose the overall objective into two components: (i) a ground-truth supervision term that aggregates all driving-related penalties, and (ii) a distillation term that regularizes the student with the teacher's latent distribution.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Training Objectives", "weight": 1.0} -->

This combination of ground truth and distillation losses ensures that the student model effectively distills knowledge from the ORION teacher, while retaining the foundational driving skills learned from the recorded trajectories.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Dataset", "weight": 1.0} -->

We train and evaluate our models utilizing the Bench2Drive dataset, which employs CARLA V2 as its closed-loop evaluation protocol for E2E autonomous driving. The official training set contains 1,000 annotated clips, each comprising multi-view camera data (6 cameras), 5 radars, and 1 LiDAR sweep. Radar and LiDAR sweeps are discarded, as our model leverages RGB cameras only. Each clip spans roughly 150 meters and captures a specific interactive driving scenario. For our distillation pipeline, we utilize 950 clips for training and 50 for open-loop validation. Comprehensive closed-loop evaluations are conducted on the official Bench2Drive CARLA simulator, encompassing 220 short routes across 44 complex, interactive scenarios.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

Following the Bench2Drive benchmark, we report five different metrics for closed-loop evaluation: Driving Score (DS), Success Rate (SR), Efficiency, Comfortness, and Multi-Ability. Driving Score, standard in CARLA, is the primary metric, multiplying the route completion percentage by a penalty discount factor for any infractions (e.g., collisions, running red lights). Success Rate measures the percentage of successfully completed routes within a designated time limit. Efficiency and Comfortness quantify the agent's navigational speed and kinematic smoothness, respectively. Multi-Ability independently evaluates the model across five advanced urban driving skills (Merging, Overtaking, Emergency Braking, Giving Way, and Traffic Signs). For the sake of completeness, we also report open-loop validation. In this case, analogously to ST-P3, we report the L2 trajectory displacement error (Avg. L2) and the bounding box collision rate.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Model Settings. Unlike VLA-based frameworks, our proposed Orion-Lite is a vision-only architecture that receives raw camera frames as input and directly yields trajectory predictions.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Training Process. We initialize the vision encoder, QT-Former, and VAE planner with pre-trained ORION weights. The 7B LLM is replaced by our randomly initialized 6-layer decoder (reducing reasoning parameters from 7B to 0.1B). During distillation, the vision encoder and QT-Former remain frozen; only the student decoder and VAE planner are updated. All ablations adopt this setting unless otherwise specified. Models are trained for 20 epochs at $640 \times 640$ resolution using AdamW with learning rate $5 \times 10^{- 5}$ and weight decay $1 \times 10^{- 4}$. Training requires $\sim$`<!-- -->`{=html}20 hours on a single RTX A6000 (48GB) GPU. Closed-loop evaluations utilize the same device. Further details are provided in our open-source repository.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Main Results", "weight": 1.0} -->

As detailed in Figure 2 and Table 1, our distilled model yields exceptional efficiency gains while achieving superior performance with respect to the teacher model. During the inference phase, the reasoning module of our student model is 150$\times$ faster than the VLA teacher's LLM and it reduces the inference GPU memory usage from 31 GB to 8 GB. This results in a 3$\times$ decrease of the overall end-to-end system latency. On top of these massive benefits in latency and memory consumption, our distilled model surpasses the ORION teacher by +2.9 DS, +0.9 SR, and +5.8 in Mean Multi-Ability (see Table 2).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Main Results", "weight": 1.0} -->

Evaluated under the Bench2Drive closed-loop evaluation, our lightweight vision-only framework establishes a new state-of-the-art across closed-loop metrics, also outperforming the recent online RL and WM-based E2E-AD models. This explicitly answers our core research question: through our distillation framework, the reasoning capabilities of a massive LLM can be effectively compressed into a lightweight transformer decoder without compromising and, in fact, improving performance in challenging closed-loop scenarios.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Main Results", "weight": 1.0} -->

In the subsequent ablation study, we conduct further experiments to verify whether both the mimic loss and trajectory supervision are strictly necessary for this performance leap, while also analyzing the role of the mimic loss during training and the efficacy of various mimic loss formulations.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

The Role of Mimic Loss. Table 3 isolates the impact of the mimic loss. When training the shallow decoder from scratch relying solely on trajectory ground truth ($\mathcal{L}_{GT}$ without $\mathcal{L}_{mimic}$), performance drops to 73.9 DS. Notably, this still represents $\sim$`<!-- -->`{=html}95% of the teacher's performance, indicating that the frozen ORION vision encoder already provides a highly robust spatio-temporal foundation. Conversely, applying the mimic loss alone recovers 98% of the teacher's performance (76.0 DS). However, when applied jointly, the model achieves SOTA performance (80.6 DS). This shows that a synergistic combination of latent feature distillation and standard GT supervision can deliver better performance than the teacher itself, for a much lower inference footprint.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Impact of Training Duration. As shown in Table 4, directly training the ORION teacher for extended epochs (from 18 to 24 epochs) purely on ground truth results in performance degradation (77.7 DS $\rightarrow$ 77.1 DS), likely due to overfitting to the training dataset. In contrast, our joint distillation model can be stably trained for 20 epochs to achieve 80.6 DS. We attribute this to the powerful regularizing effect of knowledge distillation. The teacher LLM's latent embeddings act as soft labels, smoothing the target distribution and preventing the student from overfitting to hard, deterministic trajectory targets.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Decoder Depth. Figure 4 illustrates the effect of scaling the student decoder's depth. When utilizing mimic loss, a highly compressed 4-layer model achieves a remarkable peak in Driving Score (81.5 DS). However, the 6-layer configuration achieves a superior Mean Multi-Ability score (60.5%), demonstrating a more robust mastery across diverse, complex driving skills (e.g., merging) rather than merely optimizing the base navigation score. Consequently, we adopt the 6-layer architecture as our default Orion-Lite model. Scaling beyond 6 layers causes both DS and Mean Ability Score to steadily decline. This suggests that mapping to the LLM's latent driving intent requires relatively low representational capacity; an overly deep student network risks overfitting to the distillation task itself, thereby degrading generalization in unseen closed-loop scenarios.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Distance Metrics for Distillation. Table 5 evaluates various distance metrics for $\mathcal{L}_{mimic}$. Because the target planning tokens ($T_{p}$) are dense, continuous feature coordinates rather than discrete class logits, applying distributional metrics like KL-Divergence requires artificially normalizing the feature space (e.g. via softmax), which distorts the latent geometry. Consequently, standard Euclidean regression metrics ($\mathcal{L}_{1}$, $\mathcal{L}_{2}$) naturally outperform KL-Divergence for feature matching. Specifically, $\mathcal{L}_{1}$ yields the lowest collision rates. We attribute this to the fact that $\mathcal{L}_{1}$ regression is inherently more robust to the extreme outlier activations.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Vision Encoder Initialization. To assess whether the teacher training stage provides improved visual representations for driving, Table 6 compares different vision encoder initializations under trajectory-only supervision (i.e., without the mimic loss). We adopt Orion-Lite as the base architecture and keep all other settings unchanged unless stated otherwise. Initializing the encoder from the Orion teacher and keeping it frozen yields the best performance, achieving 77.4 DS and 51.8 SR. In contrast, replacing it with an EVA-02-L initialization while still freezing the encoder results in a substantial drop, to 54.3 DS and 21.8 SR. This large performance gap suggests that the teacher-trained encoder already captures driving-specific visual representations that are absent in a generic initialization. When the EVA-02-L encoder is unfrozen and fine-tuned, performance improves significantly to 72.4 DS and 47.3 SR, indicating that trajectory supervision can adapt a generic backbone to the driving domain. However, it still falls short of the frozen Orion initialization by 5.0 DS.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

These findings suggest that Orion's vision encoder acquires important semantic and spatial priors during joint training with the LLM, which are not easily recovered through trajectory supervision alone.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

While our student model achieves a $150 \times$ speedup in the reasoning module, the heavy pre-trained vision encoder (e.g., EVA-02-L) becomes the primary computational bottleneck during overall system inference. Furthermore, our distillation pipeline fundamentally relies on the prior existence of a fully trained, computationally expensive VLA teacher model. Additionally, our empirical validation is currently focused on the Bench2Drive benchmark. Although Bench2Drive is one of the most challenging benchmarks, future research should verify these findings across diverse driving datasets and explore the optimization the vision encoder itself together with the QT-Former. It is recommended to enhance the Bench2Drive test set with extra complex long-tail, edge-case scenarios to better research the need for VLA reasoning in autonomous driving. Additionally, developing novel frameworks capable of injecting broad world knowledge from an LLM directly into a visual reasoning module without the need to curate massive, domain-specific VQA datasets presents a highly promising direction to circumvent the need for massive teacher models entirely.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we address the severe computational bottlenecks of deploying Vision-Language-Action (VLA) models by introducing a streamlined, highly effective knowledge distillation framework. We show how to distill the latent reasoning capabilities of a massive 7B-parameter LLM into a shallow, efficient transformer decoder without suffering a performance gap in challenging, closed-loop scenarios. In fact, through joint distillation and ground truth trajectory supervision, our vision-only student model consistently surpasses its massive VLA teacher in these highly complicated driving scenarios.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our proposed Orion-Lite architecture drastically reduces inference latency and memory footprint while establishing a new state-of-the-art on the complex Bench2Drive benchmark. Ultimately, our findings suggest that rather than indefinitely scaling architectural parameters for inference, optimizing training paradigms and distilling latent reasoning capabilities can unlock significant, untapped potential in vision-only end-to-end autonomous driving.
