<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving

Topics include Autonomous driving, Vision-language-action, Diffusion models, Vision-language models, End-to-end planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces Fast-dDrive, a block-diffusion vision-language-action model for autonomous driving that preserves causal section ordering while refining structured outputs in parallel. The paper targets the practical speed-accuracy tradeoff for real-time VLA-based driving policies.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

End-to-end autonomous driving via Vision-Language-Action (VLA) models demands a precarious balance between high-fidelity trajectory planning and efficient inference. Existing paradigms typically fall short: autoregressive (AR) VLAs are memory-bandwidth-bound on edge hardware and prone to exposure-bias drift, while full-sequence diffusion models preclude KV-cache reuse and suffer from "logical leakage" that violates the fundamental perceive-then-plan causality. We present Fast-dDrive, a block-diffusion VLA that performs bidirectional refinement within semantic units while enforcing strict causal ordering across them. Leveraging the observation that driving VLAs often emit structured JSON-like outputs, Fast-dDrive freezes structural tokens into a section scaffold and employs a section-aware training recipe that prioritizes safety-critical planning. We further introduce Scaffold Speculative Decoding to achieve AR-equivalent quality at significantly higher throughput.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, we propose a low-overhead test-time scaling scheme: by forking N stochastic trajectory rollouts from a single shared-prefix KV cache and averaging them, we effectively suppress prediction variance at a fractional computational cost. Empirical results demonstrate that Fast-dDrive redefines the speed-accuracy frontier for driving agents. On the WOD-E2E test set, Fast-dDrive achieves SOTA ADE@3s and ADE@5s, alongside the highest RFS among diffusion-based VLAs; on nuScenes, it reduces average L2 error to 0.32 m (a 22% improvement). When integrated with SGLang, our framework delivers 12x throughput speedup over the AR baseline, narrowing the gap between high-capacity VLAs and the efficiency demands of real-time on-vehicle deployment.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

End-to-end (E2E) autonomous driving has progressed rapidly by unifying perception, reasoning, and planning within a single trainable system. A growing line of work extends this paradigm with Vision-Language Models (VLMs) and Vision-Language-Action (VLA) models, which leverage broad world knowledge and natural-language reasoning to handle the long-tail scenarios that dominate real-world driving and to expose interpretable explanations of the agent's decisions. For any such system to be practically useful, two requirements must be met *simultaneously*: the predicted trajectory must be accurate and globally consistent with the model's reasoning, and inference must be efficient enough on edge hardware at batch size one to remain competitive with classical planners. Existing VLAs typically satisfy at most one of these criteria.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Driving VLAs are predominantly built on autoregressive (AR) decoders inherited from general-purpose VLMs, which emit the structured reasoning trace and the trajectory tokens one at a time. Sequential decoding causes a well-known *exposure-bias* effect: each waypoint conditions on previously emitted (and possibly noisy) coordinates, so small errors at the start of a 5 s plan can compound into physically implausible maneuvers. In addition, single-token decoding at batch size one is strictly memory-bandwidth-bound on modern GPUs: each new token reloads the full set of model weights while leaving the available parallel compute largely idle, making efficient on-vehicle deployment fundamentally hard.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent diffusion-based language models, typically formulated as masked-diffusion modeling (MDM) where masked tokens are iteratively unmasked via bidirectional attention, replace AR with iterative denoising that provides global context at every refinement step. Applied to driving, dVLM-AD reformulates the structured driving response as a single bidirectional denoising target and improves reasoning--action consistency over AR baselines, but at two structural costs: (i) full-sequence bidirectional attention precludes KV-cache reuse, keeping end-to-end latency far above AR baselines; and (ii) treating the response as one bidirectional unit ignores its inherent causal structure (perception, explanation, meta-behavior decision, and trajectory in that order), admitting *logical leakage* where the planned trajectory can retroactively influence the model's stated perception. We instead propose Fast-dDrive (Figure 1), a block-diffusion VLA that decodes the structured driving output section by section under strict causal ordering, with bidirectional refinement confined within each section, directly resolving both costs while preserving the global-context benefit of diffusion.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

On top of this paradigm, Fast-dDrive further exploits a structural observation about modern driving VLMs: their structured outputs bundle perception, chain-of-thought, and trajectory into a schema-defined JSON whose keys and syntax are determined entirely by the schema rather than by the model. We treat those deterministic tokens as a frozen *scaffold* and denoise only the value tokens, concentrating model capacity on the few positions that actually require prediction.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Building on this scaffold and the Fast-dVLM architecture with a Qwen2.5-VL-3B backbone, our contributions span three axes: a section-weighted, noise-adaptive training scheme that prioritizes safety-critical reasoning; a scaffold-aware self-speculative decoder that auto-accepts structural tokens and verifies an MDM draft with the AR head, delivering AR-quality outputs at substantially lower latency; and a low-overhead test-time inference scaling scheme that, with the deterministic prefix decoded once, samples the AR verifier of Scaffold Speculative Decoding only on the trajectory section and averages a small number of trajectory rollouts forked from a shared KV cache, trading a fraction of additional inference compute for a meaningful accuracy gain. Concretely: Section-Aware Structured Diffusion (SASD). A scaffold-based training scheme that aligns block boundaries with semantic sections (ensuring $100\%$ structural validity by construction) and uses section-weighted cross-entropy together with a section-adaptive Beta noise schedule to concentrate capacity on safety-critical sections, at zero inference overhead.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Scaffold Speculative Decoding and shared-prefix test-time scaling. Scaffold Speculative Decoding (SS) auto-accepts scaffold tokens and lets the AR head verify a parallel MDM draft, producing outputs identical to pure AR at substantially lower latency. We further turn the deterministic SS verifier into a tunable inference-scaling axis: with the prefix decoded once and the verifier sampled at non-zero temperature only on the trajectory section, $N$ trajectory rollouts are forked from a shared KV cache and averaged, trading a fraction of extra inference compute for a meaningful accuracy gain.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

State-of-the-art accuracy at $\mathbf{12\times}$ throughput. On the WOD-E2E test set, Fast-dDrive achieves the lowest ADE@3s and ADE@5s among compared methods while maintaining the highest RFS among diffusion-based VLAs. It delivers this SOTA accuracy at over $200$ tokens per second on a single H100---representing a $6\times$ throughput increase over full-sequence diffusion and $4\times$ over AR baselines. When integrated with SGLang, this efficiency gain scales to a $12\times$ speedup over AR baselines, demonstrating that high-capacity VLAs can effectively bridge the gap toward real-time on-vehicle deployment without accuracy compromises.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

These results indicate block-diffusion VLAs, when paired with structure-aware training and inference, can match or exceed the accuracy of strong AR and full-sequence-diffusion baselines while running at substantially higher throughput, without sacrificing the interpretability of structured CoT outputs.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Methodology", "weight": 1.0} -->

We present Fast-dDrive, a block-diffusion VLA for end-to-end autonomous driving. We first review the block-diffusion formulation (§3.1), then describe our structure-aware scaffold diffusion training (§3.2), the two inference modes it admits (Section Diffusion and Scaffold Speculative Decoding, §3.3), and a low-overhead test-time inference scaling scheme that decodes the deterministic prefix once and averages multiple stochastic trajectory-section rollouts forked from a shared KV cache (§3.4).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Masked Diffusion Language Models", "weight": 1.0} -->

Let $\mathbf{x}_{0}=(x_{1},\ldots,x_{L})$ be the target token sequence and $\mathbf{c}=(\mathbf{v},\mathbf{p})$ the conditioning context (visual features and text prompt). A masked diffusion model defines a forward process that randomly replaces tokens with a special $[\mathrm{MASK}]$ token according to a noise schedule $\{\lambda_{t}\}_{t=1}^{T}$, yielding a corrupted sequence $\mathbf{x}_{t}$. The reverse process applies a denoising policy $p_{\theta}$ that predicts replacements for masked positions while keeping visible tokens fixed. Training minimizes the masked cross-entropy loss: where $\mathcal{M}_{t}=\{i:x_{t}^{i}=[\mathrm{MASK}]\}$ is the set of masked indices at step $t$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Masked Diffusion Language Models", "weight": 1.0} -->

future_meta_behavior "nearby_vehicle":"yes", "pedestrian":"no", "cyclist":"no", "traffic_element":"yes", "road_hazard":"no", "weather_condition":"no", "construction":"no", "emergency_vehicle":"no", "animal":"no", "special_vehicle":"no", "door_opening_vehicle":"no" "explanation": "This is an example.", "future_meta_behavior": { "lateral": "keep lane" Table 1: Top: per-section value/scaffold token counts in our schema. The scaffold accounts for ∼ 30% of decoded tokens. Bottom: an example structured output of Fast-dDrive. Only value tokens need to be decoded.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Block-Causal Diffusion", "weight": 1.0} -->

Full-sequence bidirectional diffusion precludes KV-cache reuse and requires full recomputation at every denoising step. Block Diffusion addresses this by partitioning the output into $B$ blocks of size $d$: $\mathbf{x}_{0}=[\mathbf{b}_{1},\ldots,\mathbf{b}_{B}]$, where blocks are generated left-to-right with *bidirectional* attention within each block and *causal* attention across blocks. Formally, block $\mathbf{b}_{j}$ attends to the full prompt $\mathbf{c}$ and all preceding blocks $\mathbf{b}_{1:j-1}$ (whose KV cache can be reused), but not to future blocks $\mathbf{b}_{j+1:B}$. This recovers KV-cache compatibility while retaining parallel generation within each block.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Block-Causal Diffusion", "weight": 1.0} -->

Fast-dVLM extends block diffusion to vision-language models via direct conversion from autoregressive VLMs, and introduces *self-speculative decoding*: for each block, the MDM head drafts all tokens in parallel via bidirectional attention, then an AR head with causal attention verifies the draft sequentially, accepting tokens until the first mismatch plus one bonus token. This achieves significant speedup with quality equivalent to pure AR decoding.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Scaffold Construction and Section-Aligned Blocks", "weight": 1.0} -->

Following prior work, the model outputs a structured JSON with four semantic sections: critical_objects (12 binary detections), explanation (free-form reasoning), future_meta_behavior (categorical actions), and trajectory (5 waypoint coordinates over 5 s). These sections differ dramatically in token count, difficulty, and safety impact.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Scaffold Construction and Section-Aligned Blocks", "weight": 1.0} -->

We exploit the fixed JSON schema by pre-filling all structural tokens (keys, brackets, punctuation) as a frozen scaffold $\hat{\mathbf{x}}_{T}$, leaving only *value tokens* masked. Let $\mathcal{A}$ denote scaffold (anchor) positions and $\mathcal{E}=\{1{:}L\}\setminus\mathcal{A}$ the editable value positions; the diffusion process operates exclusively on $\mathcal{E}$: This guarantees $100\%$ structural correctness and reduces the denoising workload by ${\sim}30\%$ (Table 1). We further align block boundaries with section boundaries, partitioning each section $s$ into $n_{s}=\lceil|\mathcal{E}_{s}|/d\rceil$ blocks. Sections are denoised in the causal order CO $\to$ Expl $\to$ FMB $\to$ Traj, each block providing complete intra-section bidirectional context.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Scaffold Construction and Section-Aligned Blocks", "weight": 1.0} -->

Variable-length sections use a NULL token for padding, stripped at inference time.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Safety-Prioritized Training", "weight": 1.0} -->

The four sections differ vastly in safety impact: a wrong trajectory coordinate may cause a collision, while a slightly imperfect explanation has no such consequence. We introduce two complementary training-time mechanisms to bias learning capacity toward safety-critical sections. *Section-weighted loss* assigns each section $s$ a positive scalar weight $w_{s}$ that scales its per-token cross-entropy: where larger weights are assigned to safety-critical sections so that gradients on hard, high-impact tokens dominate the update. *Section-adaptive noise* replaces the uniform diffusion schedule with per-section Beta distributions $t_{s}\sim\mathrm{Beta}(\alpha_{s},\beta_{s})$, allowing the noise schedule to be tailored to each section's difficulty profile. Concrete values for $\{w_{s}\}$ and $\{(\alpha_{s},\beta_{s})\}$ are reported in §4.1. Both mechanisms incur zero inference overhead.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Joint AR and Diffusion Training", "weight": 1.0} -->

Following Fast-dVLM, we train under a dual-stream objective that combines our section-weighted MDM loss (Eq. 3) with a token-level causal LM loss $\mathcal{L}_{\mathrm{AR}}$ over the same response labels on the clean stream: The diffusion branch learns parallel value denoising under intra-block bidirectional attention, while the causal branch preserves the pretrained AR decoding capability. As shown in §3.3, this joint objective is what enables a single trained Fast-dDrive to expose both a diffusion-only and a self-speculative decoding mode without further fine-tuning.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Inference: Section Diffusion and Scaffold Spec", "weight": 1.0} -->

Because the joint AR + diffusion objective in Eq. preserves both decoding heads on the same weights, Fast-dDrive supports two complementary inference modes over the same scaffold and section-aligned blocks, mirroring the dual-mode setup of Fast-dVLM.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Section Diffusion (SD)", "weight": 1.0} -->

SD reuses the training-time procedure at inference: starting from the pre-filled scaffold $\hat{\mathbf{x}}_{T}$, the MDM head iteratively unmasks value positions section by section over the section-aligned dynamic blocks of §3.2, attending to preceding blocks via cached causal context (i.e., *causal context decoding* in the sense of Fast-dVLM ). KV caches from the scaffold and from earlier sections are reused without recomputation, yielding a diffusion-only baseline that does not invoke the AR head.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Scaffold Speculative Decoding (SS)", "weight": 1.0} -->

The second mode invokes self-speculative decoding, in which the MDM head drafts a block in parallel and the AR head verifies it sequentially. Vanilla self-spec operates on fixed-size blocks without awareness of scaffolds or section structure; we extend it to Scaffold Speculative Decoding (SS), which exploits the scaffold from §3.2 to further reduce computational overhead while preserving generation quality.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Given the pre-filled scaffold $\hat{\mathbf{x}}_{T}$, Scaffold Spec processes each block $\mathbf{b}_{j}$ in the section-ordered sequence as follows: Auto-accept scaffold: All scaffold positions within $\mathbf{b}_{j}$ are directly accepted without drafting or verification. Only value positions $\mathcal{E}_{j}=\mathcal{E}\cap\mathbf{b}_{j}$ enter the draft-verify cycle.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Draft (MDM head): A single forward pass with block-bidirectional attention fills all $|\mathcal{E}_{j}|$ masked value positions simultaneously, producing draft tokens $\{\tilde{x}_{i}\}_{i\in\mathcal{E}_{j}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Verify (AR head): A causal forward pass over the entire block computes AR logits. For each value position $i\in\mathcal{E}_{j}$ in left-to-right order, if $\arg\max p_{\theta}^{\mathrm{AR}}(\cdot\mid\mathbf{x}_{<i})=\tilde{x}_{i}$, the token is accepted; otherwise, the AR token replaces the draft and all subsequent draft tokens are discarded. One bonus token is always accepted at the rejection point.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Efficiency Analysis", "weight": 1.0} -->

Each block requires exactly 2 forward passes (draft + verify), regardless of block size. The key speedup over vanilla self-speculative decoding comes from two sources: scaffold tokens are auto-accepted with *zero* forward passes; section-aligned blocks ensure that the MDM draft has complete semantic context, improving draft acceptance rate compared to arbitrary fixed-size blocks. Combined, this yields a remarkable speedup over standard self-speculative decoding.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Test-Time Inference Scaling via Shared-Prefix Multi-Trajectory Rollouts", "weight": 1.0} -->

Scaffold Spec (§3.3) decodes the structured output deterministically: a single SS pass already returns the model's most-confident trajectory. To convert additional inference compute into additional accuracy, we introduce stochasticity *inside* the AR verifier and average $N$ trajectory rollouts. Two design choices keep this scheme both cheap and quality-preserving.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Test-Time Inference Scaling via Shared-Prefix Multi-Trajectory Rollouts", "weight": 1.0} -->

Trajectory-only stochasticity. The first three sections (critical_objects, explanation, future_meta_behavior) are heavily structured by the schema and have sharply peaked posteriors; sampling them adds no useful diversity and only degrades downstream sections. We therefore keep the AR verifier greedy on the first three sections and only enable softmax sampling once decoding enters the trajectory section.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Test-Time Inference Scaling via Shared-Prefix Multi-Trajectory Rollouts", "weight": 1.0} -->

Shared prefix. Because the first three sections are deterministic, their KV cache is identical across rollouts. We decode them *once*, fork the KV cache $N$ times, and continue Scaffold Spec on the trajectory section $N$ times, each with independent random draws. Since the trajectory section is short relative to the full output, this adds only a fractional cost per extra rollout rather than a full SS pass.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Trajectory averaging", "weight": 1.0} -->

Let $\{\boldsymbol{\tau}^{(i)}\}_{i=1}^{N}$ be the $N$ rollout trajectories, each interpolated to 20 waypoints via Jerk-Minimizing Trajectory (JMT) fitting. The output is the equal-weight average $\boldsymbol{\tau}_{\mathrm{out}}\;=\;\frac{1}{N}\sum_{i=1}^{N}\boldsymbol{\tau}^{(i)}.$ By the variance-of-the-mean argument, averaging $N$ rollouts reduces residual variance by a factor of $1/N$ while leaving any deterministic bias unchanged. Each rollout is still produced by Scaffold Spec (only the trajectory-section verifier step is sampled), so per-rollout quality stays close to the deterministic SS baseline, a regime that sampling the verifier on the full output cannot reach.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Datasets", "weight": 1.0} -->

We evaluate in open-loop settings on two established benchmarks. nuScenes contains 1,000 urban driving scenes split 700/150/150 for train/val/test, with annotated keyframes sampled at 2 Hz. Waymo Open Dataset End-to-End (WOD-E2E) comprises 4,021 long-tail driving segments of 20 s each, split 2,037/479/1,505; for test evaluation, only the first 12 s of each segment are provided and predictions must be generated from information available up to that point. We adopt the chain-of-thought annotations from dVLM-AD for the four-section structured output. Sensor specifications and capture rates are deferred to Appendix A.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Input Modalities", "weight": 1.0} -->

The model consumes RGB camera frames, ego state, and a high-level navigation command; we use no LiDAR, radar, or HD map. Following prior open-loop VLA work, we use 3 past front-camera frames spanning the last 1 s on nuScenes and the 3 front-facing cameras at the current frame on WOD-E2E; each image is resized so that the longer side is at most $512$ px before being patchified by Qwen2.5-VL's vision encoder. Frame timestamps, per-view sizing, and the joint-view WOD-E2E variant we explored are detailed in Appendix A.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Evaluation Metrics", "weight": 1.0} -->

*Planning accuracy.* For nuScenes, following dVLM-AD, we report the L2 distance error at 1/2/3 s horizons. For WOD-E2E, we report Average Displacement Error (ADE) at 3 s and 5 s horizons, and Rater Feedback Score (RFS), a human-aligned trust-region score where higher values indicate better matches to multiple human-rated reference trajectories. *Inference efficiency.* On a single NVIDIA H100 with batch size 1 we report *Latency* (ms per sample), *TPS* (tokens per second), and *Tok/Step* (tokens committed per model forward pass; AR decoding gives $\text{Tok/Step}{=}1$).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Fast-dDrive is built on Qwen2.5-VL-3B converted to the Fast-dVLM block-diffusion architecture and outputs a structured JSON of the four sections defined in §3.2. We train the model on $8{\times}$H100 GPUs with block-causal attention, fine-tuning for 3 epochs on the WOD-E2E training set. For WOD-E2E we mix the $30$k CoT-annotated samples with an additional $60$k trajectory-only samples (no CoT) to improve trajectory coverage; the nuScenes training set ($23$k samples) is used separately. SASD instantiates Eq. with section loss weights $\{w_{s}\}=\{3.0,2.0,1.5,1.0\}$ and Beta noise parameters $\{(\alpha_{s},\beta_{s})\}=\{,(1,1.5) \}$ for trajectory, future_meta_behavior, critical_objects, and explanation respectively. Efficiency benchmarks are measured on a single H100.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Main Results", "weight": 1.0} -->

Fast-dDrive (Scaffold Spec) Table 2: Comparison on WOD-E2E test set. ∗: zero-shot (no fine-tuning). †: measured by us with the original backbone under the same conditions as our model. TPS and Tok/Step are measured on a single H100.

<!-- chunk {"id": "body-0039", "role": "body", "section": "WOD-E2E Results", "weight": 1.0} -->

VLMs / VLAs with Reasoning Table 3: L2 Error on nuScenes val set. ∗: zero-shot.

<!-- chunk {"id": "body-0040", "role": "body", "section": "WOD-E2E Results", "weight": 1.0} -->

Table 2 reports planning accuracy and decoding throughput on the WOD-E2E test set against representative AR baselines and the diffusion baseline dVLM-AD. With a single inference run, Fast-dDrive (Scaffold Spec) attains the lowest ADE@3s and ADE@5s among the compared methods, and an RFS that surpasses the diffusion baseline dVLM-AD by a clear margin and is competitive with the strongest AR baseline despite our model using neither GRPO post-training nor a larger trajectory pool. Adding the shared-prefix multi-trajectory rollout of §3.4 further reduces both ADE values at sub-$2{\times}$ wall-clock cost relative to a single Scaffold-Spec pass, since only the trajectory section is rolled out $N$ times from a forked KV cache. On efficiency, Fast-dDrive runs at $4{\times}$--$6{\times}$ the decoding throughput of dVLM-AD and the AR baselines while committing ${\sim}5$ tokens per model forward pass, giving a clear advantage on the accuracy--efficiency Pareto frontier.

<!-- chunk {"id": "body-0041", "role": "body", "section": "nuScenes Results", "weight": 1.0} -->

Table 3 reports L2 errors on the nuScenes validation set following the dVLM-AD protocol. Fast-dDrive achieves the lowest average L2 among the listed VLM/VLA systems with reasoning, with consistent gains over the diffusion and AR-with-CoT baselines across all three horizons; it also matches or improves upon classical training-based driving policies that lack interpretable reasoning. Combined with the WOD-E2E results, this indicates that our structure-aware design transfers between predominantly nominal urban driving and long-tail scenarios without per-dataset tuning.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Efficiency & Performance Analysis", "weight": 1.0} -->

Table 4 compares Fast-dDrive inference variants against the AR baseline (Qwen2.5-VL-3B trained with the same data and recipe but standard autoregressive decoding) and dVLM-AD on the WOD-E2E validation set (single H100, batch size 1).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Efficiency & Performance Analysis", "weight": 1.0} -->

Among the Fast-dDrive variants, Scaffold Spec achieves the lowest latency and highest throughput, nearly doubling the TPS of vanilla self-speculative decoding while matching its accuracy. The speedup stems from scaffold auto-acceptance, which removes ${\sim}30\%$ of tokens from the draft-verify loop. Compared to dVLM-AD, which requires full-sequence recomputation at every denoising step, Scaffold Spec achieves roughly $6{\times}$ the throughput by combining block-level KV-cache reuse with scaffold-aware speculative acceptance. The AR baseline, despite sharing the same backbone and training data, is both slower (limited to one token per forward pass) and less accurate than the block-diffusion variants, suggesting that bidirectional context within blocks produces more globally consistent trajectories than purely sequential decoding.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Efficiency & Performance Analysis", "weight": 1.0} -->

Section Diffusion yields competitive throughput but slightly higher ADE than the speculative variants, indicating that causal AR verification contributes meaningfully to trajectory quality; this accuracy gap motivates the shared-prefix rollout scheme of §3.4. All Fast-dDrive variants substantially outperform dVLM-AD on both ADE and RFS, confirming that section-aware block diffusion with SASD training is more effective than full-sequence diffusion for structured driving outputs. Finally, integrating Scaffold Spec into SGLang yields an additional ${\sim}3{\times}$ speedup via optimized kernels and CUDA graph, demonstrating that the algorithmic gains compose well with system-level optimizations.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Efficiency & Performance Analysis", "weight": 1.0} -->

AR Baseline (Qwen2.5-VL-3B) dVLM-AD (Full-seq MDM) Fast-dDrive (Section Diffusion) Table 4: Inference efficiency and accuracy comparison on WOD-E2E val set. Latency: average wall-clock time per sample. TPS: tokens per second (including scaffold tokens). Tok/Step: effective tokens committed per model forward pass.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

We ablate the two components of SASD training (Section-Importance-Weighted Loss, IWL; Section-Adaptive Noise Schedule, SNS) by re-training under each of the four on/off combinations while holding all other factors fixed; results are in Table 5. IWL is the primary contributor: by up-weighting trajectory and meta-behavior tokens, it directly amplifies the gradient on the positions most critical for planning quality, yielding a clear RFS improvement over the uniform-weight baseline. SNS alone provides a smaller but complementary gain by biasing the noise schedule toward harder denoising configurations for safety-critical sections. When combined, IWL and SNS achieve the best RFS among all configurations, indicating that loss weighting and noise shaping address complementary aspects of the training objective.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

Table 4 further confirms that Scaffold Spec is the most efficient inference method at no accuracy cost relative to Self-Spec, while Section Diffusion offers a useful alternative when diversity is needed (see §3.4). For test-time scaling, Figure 4(b) shows that ADE@5s decreases monotonically with the number of trajectory rollouts $N$; we adopt $N{=}4$ as the default, which provides a favorable accuracy--latency trade-off.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented Fast-dDrive, a block-diffusion VLA that exploits the inherent structure of driving outputs to simultaneously advance planning accuracy and inference efficiency. By treating deterministic schema tokens as a frozen scaffold, aligning diffusion blocks with semantic sections, and prioritizing safety-critical tokens during training, Fast-dDrive achieves state-of-the-art trajectory accuracy at $6{\times}$ the throughput of full-sequence diffusion baselines, demonstrating that structured generation and efficient decoding are complementary rather than conflicting objectives. The shared-prefix multi-trajectory rollout scheme further shows that block diffusion naturally admits a low-cost test-time scaling axis unavailable to AR models. We believe these results point toward a broader principle: when model outputs have known structure, encoding that structure into the diffusion process yields compounding gains in both quality and speed.
