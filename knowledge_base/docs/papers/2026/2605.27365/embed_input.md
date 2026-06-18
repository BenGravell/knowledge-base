<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

LocateAnything: Fast and High-Quality Vision-Language Grounding with Parallel Box Decoding

Topics include Vision-language, Vision-language models, Object detection, Localization, Computer vision, Parallel algorithms, Object recognition.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces a vision-language grounding model that predicts object boxes in parallel for faster localization. The main contribution is an architecture and decoding strategy aimed at preserving grounding quality while reducing the sequential cost of box generation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Vision-language models (VLMs) commonly formulate visual grounding and detection as a coordinate-token generation problem, serializing each 2D box into multiple 1D tokens that are learned and decoded largely independently. This token-by-token decoding mismatches the coupled structure of box geometry and creates a practical inference bottleneck due to strictly sequential generation. We introduce LocateAnything, a unified generative grounding and detection framework based on Parallel Box Decoding (PBD). By decoding geometric elements such as bounding boxes and points as atomic units in a single step, LocateAnything preserves intra-box geometric coherence and unlocks substantial parallelism. We show that PBD improves both decoding throughput and localization accuracy. We further develop a scalable data engine and curate LocateAnything-Data, a large-scale dataset with more than 138 million training samples, substantially increasing data diversity for high-precision localization. Extensive evaluations show that LocateAnything advances the speed-accuracy frontier, achieving significantly higher decoding throughput while improving high-IoU localization quality across diverse benchmarks.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The results highlight the complementary benefits of Parallel Box Decoding and large-scale training data in enabling efficient and precise unified visual grounding and detection.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Vision-language models (VLMs) (bai2025qwen2.5vl; chen2025eagle; wang2025internvl3; huang2026step3; yang2025kwai; deshmukh2025nvidia) are increasingly adopted as a general-purpose backbone for interactive and embodied systems due to their broader knowledge and stronger instruction-following capabilities than conventional specialized models (zhang2022dino; liu2023grounding; carion2020end; ren2016faster).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To act in the world, VLMs (bai2025qwen2.5vl; fu2025llmdet; zhan2024griffon; wang2025internvl3; azzolini2025cosmos) must be tightly grounded in *perception* --- in particular, they *localize* task-relevant entities (\\eg, objects (zhang2024llava; jiang2025rexomni; yu2025perception; wang2023exploring), UI elements (liu2025scalecua; lin2024showui; feizi2025grounding; nayak2025ui), regions (ren2024pixellm; yuan2025pixelrefer; lai2024lisa; cheng2024spatialrgpt; ranzinger2024radio; heinrich2025radiov2)) from natural-language intents with high quality and low latency, which requires high vision-language grounding capabilities.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Object detection and grounding in VLMs (zhan2024griffon; li2025lmmdet; yu2025perception; peng2023kosmos; zhang2024ferretv2; jiang2025rexomni; man2025locateanything3d) are often formulated as a *generative* problem. Under the next-token prediction (NTP) paradigm (chen2021pix2seq; jiang2025rexomni; peng2023kosmos), a VLM can answer open-ended queries by emitting spatial coordinates as a token sequence.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

As illustrated in the bottom panel of Fig. 1, existing methods (you2023ferret; peng2023kosmos; zhang2024ferretv2; jiang2025rexomni; qi2025cot4det) commonly represent coordinates as either Textual Digits (\\eg, "1024" as "1", "0", "2", "4") or Quantized Tokens (\\eg, $x_{1}\rightarrow y_{1}\rightarrow x_{2}\rightarrow y_{2}$). Despite their differences, these representations serialize a 2D geometric object into a 1D stream, forcing token-by-token generation at inference time. This token-level sequential decoding becomes a practical bottleneck (higher latency and lower throughput) and under-utilizes the strong structured correlation among coordinates $(x_{1},y_{1},x_{2},y_{2})$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multi-Token Prediction (MTP) (li2025diffusionvl; liu2025sequential; nie2025large; ye2025dream) offers a natural approach to reducing decoding steps by predicting multiple tokens in parallel. In language modeling, MTP is usually implemented by randomly (i) choosing positions in the sequence and training the model to predict a following span in parallel (\\ie, next-block prediction) (liu2025sequential; cai2024medusa; li2025eagle; liu2024deepseek), or (ii) masking some tokens of the sequence and training the model to reconstruct the original text, such as masked diffusion modeling (li2022diffusion; arriola2025block; nie2025large; liu2025tidar). However, these formulations are largely *structure-agnostic*: they treat inputs as generic token streams and mainly capture correlations driven by co-occurrence. Inferring the missing tokens from random subsets requires the model to represent complex and irregular conditional distributions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

For tightly coupled units such as bounding boxes, this supervision does not match well the training objective because it can learn to generate token combinations across bounding-box boundaries and even object categories, as demonstrated in Fig. 2. Consequently, the model must fit many unreliable patterns, inducing spurious correlations, sacrificing structured decoding, and amplifying error propagation, which together reduce accuracy, reliability, and decoding speed.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

To reconcile high-throughput decoding with reliable localization, we propose LocateAnything, a unified framework for VLM-based visual detection and grounding built upon Parallel Box Decoding (PBD). Our key idea is to align MTP blocks with structured units: during training, LocateAnything treats each bounding box (or point) as an *atomic unit* and learns to predict the full coordinate set $(x_{1},y_{1},x_{2},y_{2})$ in one parallel step. This *box-aligned* training target avoids arbitrary chunking of coordinate tokens. As a result, our strategy improves the localization performance of the model, while simultaneously unlocking the speed benefits of parallel decoding.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

With the proposed PBD, we study various strategies for structured bounding-box decoding to balance throughput and accuracy. Our observations motivate a flexible inference design to meet different latency--robustness requirements by providing three on-demand modes. (i) Fast Mode (MTP) predicts full boxes in parallel for maximum throughput, which is suitable for latency- and compute-constrained settings, such as on-device robotics and embodied agents. (ii) Slow Mode (NTP) decodes coordinate tokens autoregressively for maximum stability, which is appropriate for high-precision labeling, final-pass dataset curation, and accuracy-oriented offline evaluation. (iii) Hybrid Mode uses Fast Mode by default and falls back to Slow Mode when the parallel output is unreliable, \\eg, due to format or consistency violations; this mode is intended for production pipelines that require both speed and accuracy. Overall, Hybrid Mode preserves most of the speed gains of parallel decoding while maintaining robust outputs.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce LocateAnything, an early exploration of applying multi-token prediction to VLM-based detection/grounding via Parallel Box Decoding, performing box-aligned decoding to improve throughput and accuracy.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present a Hybrid decoding policy that detects unreliable parallel blocks and performs localized NTP re-decoding only for the problematic block, reducing worst-case failures while retaining most speed gains.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Extensive evaluations, including layout grounding, long-tail detection, and GUI grounding, show that LocateAnything advances the speed--accuracy frontier, outperforming the SOTA by a large margin. It achieves up to 2.5$\times$ higher decoding throughput while improving localization quality.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Method", "weight": 1.0} -->

This section presents LocateAnything, a fast and effective framework that integrates Parallel Box Decoding (PBD) into VLMs for visual detection and grounding. Section 3.1 introduces the model architecture and the block-based output formulation. Section 3.2 details the joint training strategy, which aligns NTP with block-level MTP. Section 3.3 describes the on-demand inference mechanism, featuring a hybrid mode that dynamically balances decoding throughput and robustness. Finally, Section 3.4 outlines the construction of our large-scale training dataset, LocateAnything-Data.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Model Architecture and Formulation", "weight": 1.0} -->

Overview. As illustrated in Fig. 3, LocateAnything builds upon a native-resolution VLM pre-trained on large-scale image-text corpora. The architecture comprises a Moon-ViT (team2025kimi) vision encoder and a Qwen2.5 (qwen2.5) language decoder, bridged by a MLP projector. Given an input image $\mathcal{I}$, the vision encoder extracts visual tokens $Z = {\text{Encoder}{(\mathcal{I})}}$ at the native resolution, preserving the fine-grained spatial details crucial for high-precision localization. These tokens are subsequently fed into the language model, which directly converts them into a sequence of box-aligned block-level predictions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Model Architecture and Formulation", "weight": 1.0} -->

Block-Based Output Formulation. To facilitate PBD, we abandon standard NTP coordinate generation. Instead, continuous coordinates are normalized to $\lbrack 0,1000\rbrack$, discretized into tokens (jiang2025rexomni; chen2021pix2seq), and reorganized into a sequence of blocks $\mathbf{B} = {(b_{1},b_{2},\ldots,b_{N})}$. Conditioned on the visual features $Z$ and a text query $\mathcal{E}$, the joint probability is formulated as ${P{({\mathbf{B} \mid {\mathcal{Z},\mathcal{E}}})}} = {\prod_{i = 1}^{N}{P{({b_{i} \mid {b_{< i},Z,\mathcal{E}}})}}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Model Architecture and Formulation", "weight": 1.0} -->

Each block $b_{i}$ acts as an atomic unit of constant length $L = 6$, accommodating a bounding box and two structural tokens (\\eg, \<box\> and \</box\>). To guarantee uniform tensor shapes for parallel decoding, any unoccupied positions are padded with a \<null\> token. As depicted in Fig. 3, we define four functional block types. Semantic Block: Encodes the linguistic identity. If an expression exceeds the capacity of a single block, it is partitioned across multiple consecutive blocks. Box Block: Uses four quantized coordinates representing the bounding boxes. Negative Block: Explicitly indicates the absence of a queried object. End Block: Signals the termination of the generation process.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Training Design", "weight": 1.0} -->

Our method treats bounding box coordinates as an indivisible atomic unit, enforcing structured supervision and unlocking the capability for parallel generation. However, parallelizing the output directly in the training phase risks disrupting the model's inherent causal reasoning process. To resolve this issue, we introduce a dual-formulation training strategy that jointly optimizes two aligned representations: the NTP sequence to preserve the causal reasoning ability, and the block-wise MTP formulation for box-aligned predictions. To implement this, a single concatenated input sequence is constructed: $x_{\text{all}} = {x_{\text{vis}} \oplus x_{\text{q}} \oplus x_{\text{ntp}} \oplus x_{\text{blk}}}$, where $\oplus$ denotes sequence concatenation.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Training Design", "weight": 1.0} -->

The terms $x_{\text{vis}}$ and $x_{\text{q}}$ serve as the shared context (visual and text query inputs), $x_{\text{ntp}}$ represents the standard NTP input sequence, and $x_{\text{blk}}$ is the block-wise MTP input sequence. Essentially, they represent the identical ground truth in two distinct formats: a token-level representation and a block-level representation.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Training Design", "weight": 1.0} -->

Specifically, inspired by (liu2025sequential; liu2025wedlm), $x_{\text{blk}}$ is constructed by traversing $x_{\text{ntp}}$ from left to right, splitting and padding the sequence according to our previously defined block rules. Within each block, we retain the first token to serve as the prediction context, while replacing all subsequent tokens with \[mask\] tokens. This structure prompts the model to simultaneously predict all masked tokens within the block in a single cohesive step. Notably, if the block size is set to 1, this MTP formulation naturally becomes equivalent to standard NTP.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Training Design", "weight": 1.0} -->

Attention Mask Design. The core challenge of this dual-sequence formulation is how to isolate the NTP and MTP streams while allowing both to leverage the shared context. This is achieved through a specialized attention mask (as shown in Fig.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Training Design", "weight": 1.0} -->

Causal Attention for NTP. To preserve the original language capabilities of the VLM, the shared context ($x_{\text{vis}}$ and $x_{\text{q}}$) and the NTP sequence ($x_{\text{ntp}}$) collectively employ a causal attention mask. Tokens within these segments can only attend to preceding tokens. Crucially, they are restricted from attending to $x_{\text{blk}}$ to prevent data leakage. This strict causal formulation perfectly aligns with the standard KV Cache usage during inference.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Training Design", "weight": 1.0} -->

Causal Flow Across Blocks. To align with the semi-autoregressive generation process, attention across different blocks in $x_{\text{blk}}$ is strictly causal. Tokens in the active block can attend to the shared context and all previously committed blocks, but cannot see future blocks. This historical visibility enables the model to learn dependencies between different box predictions, effectively mitigating duplicate or missing bounding boxes.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Training Design", "weight": 1.0} -->

Bidirectional Intra-Block Attention. Following the block-causal design widely adopted in recent generative modeling (arriola2025block; nie2025large; wang2025diffusion; wu2025fast; fu2025efficient; wu2025fastv1), tokens within the same block share bidirectional attention. This fully-connected intra-block interaction allows the model to capture complex internal relationships (\\eg, geometric dependencies among a set of coordinates) and resolve all internal tokens simultaneously within a single functional unit.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Training Design", "weight": 1.0} -->

Objective. Guided by this mask, we jointly minimize the cross-entropy losses for both sequences, \\ie, $\mathcal{L} = {\mathcal{L}_{ntp} + \mathcal{L}_{mtp}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "On-Demand Inference Modes", "weight": 1.0} -->

While our proposed PBD significantly accelerates inference, parallel decoding faces an inherent exploration-exploitation dilemma in highly complex scenes, as shown in Fig. 5. The first is Format Irregularity, which occurs in complex scenes containing multiple instances across categories. During parallel decoding, the model may struggle at category boundaries, hesitating between continuing to predict for the current class or transitioning to a new class. This uncertainty manifests as malformed syntax within a single predicted block, erroneously mixing structural and coordinate tokens (\\eg, \<box\>\<211\>\</ref\>\<911\>\<887\>\</box\>). The second is Spatial Ambiguity, which arises when objects are densely arranged in regular grids, such as rows or columns. The MTP approach can blur spatial boundaries and output an intermediate coordinate situated between two objects, consequently producing low IoU predictions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "On-Demand Inference Modes", "weight": 1.0} -->

Both failure patterns can be effectively resolved using an NTP fallback mechanism. The NTP prediction can achieve higher precision when handling complex category transitions and dense spatial layouts. Therefore, during MTP inference, we continuously validate the syntactic integrity and monitor spatial confidence. Specifically, an ambiguity trigger is activated if two conditions are met simultaneously: the top-1 coordinate token's probability is below 0.7, and the max-min difference among the top-5 coordinate tokens exceeds 80 within the normalized space. Upon detection of a format violation or high spatial ambiguity, the compromised block is discarded, and the generation reverts to the last verified prefix. NTP is then employed to autoregressively generate the tokens for the specific problematic block. Once the block is completed, the model seamlessly switches back to MTP for subsequent predictions.

<!-- chunk {"id": "body-0030", "role": "body", "section": "On-Demand Inference Modes", "weight": 1.0} -->

Based on the above discussion, we propose three on-demand inference modes to balance throughput and spatial robustness. Slow Mode, which generates the output token-by-token using standard NTP. Fast Mode, which leverages MTP to predict box-aligned blocks. For each block, \<null\> padding tokens are discarded, and the remaining tokens are appended to the output; the committed tokens are stored in the key-value cache and serve as causal context for subsequent prediction steps. Hybrid Mode, which employs MTP by default but seamlessly switches to NTP when parallel outputs become unreliable.

<!-- chunk {"id": "body-0031", "role": "body", "section": "On-Demand Inference Modes", "weight": 1.0} -->

Inference-Time Attention Mask. During inference, the attention mask for each MTP decoding step mirrors the training-time block-causal pattern illustrated in Fig. 4. All previously committed tokens in the KV cache follow standard causal attention, while the $n_{\text{future}}$ tokens in the current MTP block attend to each other bidirectionally, enabling parallel token prediction. Meanwhile, the current block can attend to all preceding blocks but is prevented from accessing subsequent ones. After each MTP step, the KV cache is truncated to retain only committed tokens, evicting mask tokens and the duplicated anchor to ensure the cache stays consistent with the causal prefix seen during training.

<!-- chunk {"id": "body-0032", "role": "body", "section": "LocateAnything-Data", "weight": 1.0} -->

To train a highly capable model for general-purpose visual detection and grounding, we curate LocateAnything-Data, a large-scale, multi-domain dataset. The dataset construction details can be found in the supplementary.

<!-- chunk {"id": "body-0033", "role": "body", "section": "LocateAnything-Data", "weight": 1.0} -->

As illustrated in Fig. 6, the dataset contains 12M unique images and 138M natural language queries. Furthermore, the dataset includes 785M annotated bounding boxes, providing massive and dense supervisory signals to guide the spatial learning of the LocateAnything model. The training corpus is categorized into six distinct tasks. General object detection constitutes the foundation, representing 66.9% of the queries and providing the essential bounding box supervision (83.1%) to help the model achieve precise and dense coordinate alignments. Grounding user interface elements (16.5% of queries) enable the model to support embodied agents and graphical user interface navigation tasks. Natural language referring comprehension (7.3% of queries) enables the model to link complex linguistic intents to specific spatial regions. Text localization (3.6% of queries) ensures that the model can perceive and tightly ground textual information within images. Document and scene layout grounding (3.5% of queries) enriches the structural reasoning capabilities of the model. Point-based localization tasks (2.2% of queries) further refine the spatial precision of the model for fine-grained predictions.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Training Details and Evaluation Setup", "weight": 1.0} -->

Training Details. We first conduct an initial training on the base VLM with focus entirely on world-knowledge alignment, during which all detection and grounding data are excluded. We then apply a two-stage supervised fine-tuning to the base VLM to train our LocateAnything model. In Stage-1, we incorporate a massive mixture of 138M queries into the overall training data to equip the model with comprehensive grounding and detection capabilities. In Stage-2, we reduce the proportion of general training data to 20% while significantly increasing the proportion of data containing many objects per image (\\eg, MOT20Det (dendorfer2020motchallengebenchmarksinglecameramultiple), SKU110K (goldman2019precise)) to enhance the model's ability in dense detection. For model ablations, we train all models exclusively on the COCO dataset (lin2014microsoft) to strictly isolate PBD's architectural benefits from our massive 138M data. Detailed configurations for both the base VLM and the subsequent LocateAnything model training are provided in the supplementary materials.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Training Details and Evaluation Setup", "weight": 1.0} -->

Qwen3-VL-4B (bai2025qwen3vltechnicalreport)

<!-- chunk {"id": "body-0036", "role": "body", "section": "Training Details and Evaluation Setup", "weight": 1.0} -->

Qwen3-VL-8B (bai2025qwen3vltechnicalreport)

<!-- chunk {"id": "body-0037", "role": "body", "section": "Training Details and Evaluation Setup", "weight": 1.0} -->

Compared Methods. We compare LocateAnything against three categories of methods. Specialized detectors, including representative general detection models such as DETR (carion2020end) and Deformable-DETR (zhu2021deformabledetrdeformabletransformers), \\etc, open-set detectors such as Grounding DINO (liu2023grounding), leading document layout analysis model DocLayout-YOLO (zhao2024doclayout), and text detection model PaddleOCRv5 (cui2025paddleocr). General-purpose VLMs with grounding capabilities, including Qwen3-VL (bai2025qwen3vltechnicalreport), DeepSeek-VL2 (wu2024deepseekvl2mixtureofexpertsvisionlanguagemodels), OVIS2.5 (lu2025ovis25technicalreport), MiMo-VL (coreteam2025mimovltechnicalreport), and SEED1.5-VL (guo2025seed15vltechnicalreport), \\etc.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Training Details and Evaluation Setup", "weight": 1.0} -->

These models adopt textual coordinate representations with standard next-token prediction, providing a direct comparison to our parallel box decoding paradigm. VLM-based detection and grounding specialists, including Rex-Omni (jiang2025rexomni), which is the most related work to ours targeting unified detection and grounding in a VLM framework. For GUI grounding, we also include several domain-specific expert models (liu_infigui-r1_2025; xie_scaling_2025; liu2025scalecua; yang_gta1_2025; ye_mobile-agent-v3_2025; zhou_mai-ui_2025; team_ui-venus-15_2026).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Training Details and Evaluation Setup", "weight": 1.0} -->

Evaluation Setup. Following the evaluation framework established in Rex-Omni (jiang2025rexomni), we conduct a comprehensive assessment across multiple visual perception tasks. Object Detection is evaluated on COCO for common objects, LVIS (gupta2019lvis) for long-tailed distributions, and VisDrone (du2019visdrone) and Dense200 (jiang2025rexomni) for dense and tiny object scenarios. Language-aware Grounding tasks include Referring Expression Comprehension (REC) on RefCOCOg and HumanRef (jiang2025referring). Interactive tasks are evaluated through GUI Grounding on ScreenSpot-Pro (li2025screenspot). Additionally, Layout Grounding on DocLayNet (pfitzmann2022doclaynet) and M6Doc (cheng2023m6doc), along with OCR (text detection and recognition) on TotalText (ch2017total), are reported together under scene text and document understanding tasks.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Training Details and Evaluation Setup", "weight": 1.0} -->

The metric for each task is summarized as follows. Box-based outputs: For detection, layout, and OCR tasks, a prediction is considered correct (\\ie, a true positive) if its Intersection over Union (IoU) with the ground truth exceeds a certain threshold. The F1-score is reported at ${IoU} = 0.5$, ${IoU} = 0.95$, and as a mean over thresholds ($mIoU$). Point-based outputs: For pointing tasks, a prediction is considered correct if the predicted point falls within the ground-truth segmentation mask or bounding box. We similarly report the F1-score for these point-based outputs based on this correctness criterion.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Training Details and Evaluation Setup", "weight": 1.0} -->

Qwen3-VL-4B (bai2025qwen3vltechnicalreport)

<!-- chunk {"id": "body-0042", "role": "body", "section": "Training Details and Evaluation Setup", "weight": 1.0} -->

Qwen3-VL-8B (bai2025qwen3vltechnicalreport)

<!-- chunk {"id": "body-0043", "role": "body", "section": "Main Results", "weight": 1.0} -->

In this section, we report the accuracy metrics and the throughput (measured in boxes per second, BPS on a single NVIDIA H100 GPU with a batch size of 1) of LocateAnything under the default Hybrid Mode. The results of Fast and Slow Mode are provided in the supplementary materials.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Main Results", "weight": 1.0} -->

Qwen3-VL-30B-A3B* (bai2025qwen3vltechnicalreport)

<!-- chunk {"id": "body-0045", "role": "body", "section": "Main Results", "weight": 1.0} -->

High-Quality Multi-Object Detection. Our model exhibits robust generalization in both common and complex dense object detection scenarios. On general detection benchmarks reported in Tab. 1, LocateAnything improves the mean F1 by +3.8% on LVIS and +1.8% on COCO compared to Rex-Omni, despite sharing an identical model size. Crucially, the model effectively learns the generalized spatial distribution, transferring its detection capabilities to unseen, heavily packed object types. This is evidenced by its performance on the dense detection benchmarks in Tab. 2, where it achieves 39.9 mean F1 on VisDrone, substantially outperforming Rex-Omni which scores 35.8. Similarly, it reaches a competitive 58.7 mean F1 on Dense200, demonstrating superior boundary delineation and instance separation in heavily overlapping environments.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Main Results", "weight": 1.0} -->

Qwen3-VL-4B (bai2025qwen3vltechnicalreport)

<!-- chunk {"id": "body-0047", "role": "body", "section": "Main Results", "weight": 1.0} -->

Qwen3-VL-8B (bai2025qwen3vltechnicalreport)

<!-- chunk {"id": "body-0048", "role": "body", "section": "Main Results", "weight": 1.0} -->

Precise Open-World Localization Ability. LocateAnything demonstrates exceptional fine-grained localization capabilities across diverse open-world benchmarks, including user interface grounding, document layout parsing, and referring expression comprehension. As shown in Tab. 3, on the ScreenSpot-Pro (li2025screenspot), it achieves a SOTA mean F1 of 60.3, surpassing generalist VLMs like Qwen3-VL-30B-A3B and specialized models tailored for UI tasks such as GUI-Owl-32B. Furthermore, in document understanding tasks detailed in Tab. 4, LocateAnything establishes a new standard by reaching 76.8 and 70.1 mean F1 on DocLayNet and M6Doc, respectively, outperforming Rex-Omni by substantial margins. This precise spatial reasoning extends to complex referring tasks, as shown in Tab. 5, where the model seamlessly aligns nuanced human intents with visual regions, achieving 78.7 mean F1 on the HumanRef benchmark and remaining highly competitive on RefCOCOg against top-tier models.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Main Results", "weight": 1.0} -->

Superior Decoding Speed. A key advantage of our model is its drastically reduced decoding steps. As shown in Tab. 1, our model achieves 12.7 BPS under the default hybrid mode, over 10$\times$ faster than textual-based Qwen3-VL (1.1 BPS) and 2.5$\times$ faster than quantized-based Rex-Omni (5.0 BPS).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Main Results", "weight": 1.0} -->

Qwen3-VL-4B (bai2025qwen3vltechnicalreport)

<!-- chunk {"id": "body-0051", "role": "body", "section": "Main Results", "weight": 1.0} -->

Qwen3-VL-8B (bai2025qwen3vltechnicalreport)

<!-- chunk {"id": "body-0052", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

We conduct ablation studies on the COCO dataset to validate our core designs. The results are shown in Tab. 6 and Fig. 7.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Coordinate Representation. As Tab. 6(a) shows, under the NTP paradigm, Textual and Quantized representations yield sub-optimal performance (49.1 and 50.1 mean F1, respectively) due to forced token-by-token generation. Our PBD (Slow Mode) achieves the highest F1-score of 52.1, proving that a box-aligned formulation provides stronger supervision for spatial reasoning than 1D serialization, without sacrificing throughput.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

MTP Formulation. Tab. 6(b) compares our box-aligned MTP against existing structure-agnostic MTP formulations. Methods like SDLM and Block Diffusion force the model to learn spurious, unaligned cross-boundary patterns, suffering from lower accuracy and limited acceleration (\\eg, SDLM-B6 achieves 46.1 F1-score at 5.5 BPS). Furthermore, structure-agnostic methods (\\eg, SDLM-B4, B6, B8) exhibit a strict speed-accuracy trade-off, where increasing the block size yields only marginal throughput gains while consistently degrading the F1-score. In contrast, our PBD strictly aligns MTP blocks with structured bounding box units, dramatically outpacing existing methods in throughput (16.9 BPS) while improving the mean F1 to 49.6.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Decoding Mode. Tab. 6(c) ablates the impact of our dual-formulation training ($\mathcal{L}_{ntp}$ and $\mathcal{L}_{blk}$). Training with isolated losses limits the model's potential; joint training successfully pushes the Slow Mode upper bound from 50.1 to 52.1 F1-score. During inference, Fast Mode (MTP) maximizes throughput (16.9 BPS) but induces accuracy drops in complex scenes. Hybrid Mode seamlessly resolves this trade-off, preserving most speed gains (13.2 BPS) while achieving robust, high-precision localization (51.6 F1-score).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Box Output Order. We investigate four spatial sorting strategies in Fig. 7 (left): X-Y Corner Order (sorting by the x-coordinate of the left-top corner, then by the y-coordinate), Center Distance (the distance of the bounding box center point to the origin), Area (sorted from largest to smallest), and Random (shuffled randomly). Results show X-Y Corner Order yields the highest F1-score. We take this setting as default in dataset construction.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Throughput. We compare generation time and throughput with NTP methods in Fig. 7 (right). As target boxes increase from 20 to 300, NTP methods suffer from a severe latency bottleneck. In contrast, the Parallel method exhibits little increase in generation time, increasing throughput from 12 BPS to $\sim$`<!-- -->`{=html}25 BPS in dense scenes. These findings confirm that PBD effectively breaks the decoding bottleneck, achieving a $2 \times$ to $6 \times$ speedup.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Qualitative Results", "weight": 1.0} -->

Fig. 8 visualizes representative grounding results of our model. Visual comparisons with other methods are provided in the supplementary materials. We observe three consistent behaviors. (i) Compositional grounding: our model handles attribute/part/spatial/reasoning-style queries well with consistent spatial alignment, supported by the diversity and coverage of our training data. (ii) Robustness to large instance counts: as targets grow from sparse to crowded settings, the predicted boxes remain structured and accurate, reflecting the precision of our box-level decoding. This robustness is further strengthened by our Stage-2 training that emphasizes many-object images, improving dense localization in practice. Moreover, our Hybrid Mode maintains most of the parallel decoding speed while improving output stability in multi-instance generation. (iii) Reliable localization in clutter: boxes stay compact and well-separated under occlusion, repetitive textures, and grid-like dense layouts. Our hybrid inference mode further stabilizes these hard cases by detecting unreliable parallel blocks and falling back to NTP re-decoding when needed.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented LocateAnything, a unified framework that reformulates visual grounding and detection in VLMs via *Parallel Box Decoding*. By elevating geometric elements to atomic units rather than 1D streams, LocateAnything aligned the training supervision with the inherently coupled nature of spatial coordinates. With massive 138M text-image training queries and a flexible on-demand inference mechanism, LocateAnything not only delivered SOTA accuracy across diverse tasks, but also achieved up to a $2.5 \times$ speedup over competitive methods. Our method provided a practical and scalable route for real-time visual perception, opening the door to deploying general-purpose VLMs in latency-sensitive embodied robotics and interactive agents.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Limitation. Currently, our model is primarily trained with supervised fine-tuning. Reinforcement learning is an important next step to further optimize the block-level decoding policy, reduce fallback frequency, and encourage effective exploration in hard dense/long-tail cases, which could improve both robustness and worst-case decoding speed. We leave it for future work.
