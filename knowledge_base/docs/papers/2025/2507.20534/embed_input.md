<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Kimi K2: Open Agentic Intelligence

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce Kimi K2, a Mixture-of-Experts (MoE) large language model with 32 billion activated parameters and 1 trillion total parameters. We propose the MuonClip optimizer, which improves upon Muon with a novel QK-clip technique to address training instability while enjoying the advanced token efficiency of Muon. Based on MuonClip, K2 was pre-trained on 15.5 trillion tokens with zero loss spike. During post-training, K2 undergoes a multi-stage post-training process, highlighted by a large-scale agentic data synthesis pipeline and a joint reinforcement learning (RL) stage, where the model improves its capabilities through interactions with real and synthetic environments. Kimi K2 achieves state-of-the-art performance among open-source non-thinking models, with strengths in agentic capabilities. Notably, K2 obtains 66.1 on Tau2-Bench, 76.5 on ACEBench (En), 65.8 on SWE-Bench Verified, and 47.3 on SWE-Bench Multilingual - surpassing most open and closed-sourced baselines in non-thinking settings.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

It also exhibits strong capabilities in coding, mathematics, and reasoning tasks, with a score of 53.7 on LiveCodeBench v6, 49.5 on AIME 2025, 75.1 on GPQA-Diamond, and 27.1 on OJBench, all without extended thinking. These results position Kimi K2 as one of the most capable open-source large language models to date, particularly in software engineering and agentic tasks. We release our base and post-trained model checkpoints to facilitate future research and applications of agentic intelligence.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The development of Large Language Models (LLMs) is undergoing a profound paradigm shift towards Agentic Intelligence -- the capabilities for models to autonomously perceive, plan, reason, and act within complex and dynamic environments. This transition marks a departure from static imitation learning towards models that actively learn through interactions, acquire new skills beyond their training distribution, and adapt behavior through experiences. It is believed that this approach allows an AI agent to go beyond the limitation of static human-generated data, and acquire superhuman capabilities through its own exploration and exploitation. Agentic intelligence is thus rapidly emerging as a defining capability for the next generation of foundation models, with wide-ranging implications across tool use, software development, and real-world autonomy.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Achieving agentic intelligence introduces challenges in both pre-training and post-training. Pre-training must endow models with broad general-purpose priors under constraints of limited high-quality data, elevating token efficiency---learning signal per token---as a critical scaling coefficient. Post-training must transform those priors into actionable behaviors, yet agentic capabilities such as multi-step reasoning, long-term planning, and tool use are rare in natural data and costly to scale. Scalable synthesis of structured, high-quality agentic trajectories, combined with general reinforcement learning (RL) techniques that incorporate preferences and self-critique, are essential to bridge this gap.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we introduce Kimi K2, a 1.04 trillion-parameter Mixture-of-Experts (MoE) LLM with 32 billion activated parameters, purposefully designed to address the core challenges and push the boundaries of agentic capability. Our contributions span both the pre-training and post-training frontiers: We present MuonClip, a novel optimizer that integrates the token-efficient Muon algorithm with a stability-enhancing mechanism called QK-Clip. Using MuonClip, we successfully pre-trained Kimi K2 on 15.5 trillion tokens without a single loss spike.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce a large-scale agentic data synthesis pipeline that systematically generates tool-use demonstrations via simulated and real-world environments. This system constructs diverse tools, agents, tasks, and trajectories to create high-fidelity, verifiably correct agentic interactions at scale.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We design a general reinforcement learning framework that combines verifiable rewards (RLVR) with a self-critique rubric reward mechanism. The model learns not only from externally defined tasks but also from evaluating its own outputs, extending alignment from static into open-ended domains.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Kimi K2 demonstrates strong performance across a broad spectrum of agentic and frontier benchmarks. It achieves scores of 66.1 on Tau2-bench, 76.5 on ACEBench (en), 65.8 on SWE-bench Verified, and 47.3 on SWE-bench Multilingual, outperforming most open- and closed-weight baselines under non-thinking evaluation settings, closing the gap with Claude 4 Opus and Sonnet. In coding, mathematics, and broader STEM domains, Kimi K2 achieves 53.7 on LiveCodeBench v6, 27.1 on OJBench, 49.5 on AIME 2025, and 75.1 on GPQA-Diamond, further highlighting its capabilities in general tasks. On the LMSYS Arena leaderboard ^44^4 Kimi K2 ranks as the top 1 open-source model and 5th overall based on over 3,000 user votes.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To spur further progress in Agentic Intelligence, we are open-sourcing our base and post-trained checkpoints, enabling the community to explore, refine, and deploy agentic intelligence at scale.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Pre-training", "weight": 1.0} -->

The base model of Kimi K2 is a trillion-parameter mixture-of-experts (MoE) transformer model, pre-trained on 15.5 trillion high-quality tokens. Given the increasingly limited availability of high-quality human data, we posit that token efficiency is emerging as a critical coefficient in the scaling of large language models. To address this, we introduce a suite of pre-training techniques explicitly designed for maximizing token efficiency. Specifically, we employ the token-efficient Muon optimizer and mitigate its training instabilities through the introduction of QK-Clip. Additionally, we incorporate synthetic data generation to further squeeze the intelligence out of available high-quality tokens. The model architecture follows an ultra-sparse MoE with multi-head latent attention (MLA) similar to DeepSeek-V3, derived from empirical scaling law analysis. The underlying infrastructure is built to optimize both training efficiency and research efficiency.

<!-- chunk {"id": "body-0012", "role": "body", "section": "MuonClip: Stable Training with Weight Clipping", "weight": 1.0} -->

We train Kimi K2 using the token-efficient Muon optimizer, incorporating weight decay and consistent update RMS scaling. Experiments in our previous work Moonlight show that, under the same compute budget and model size --- and therefore the same amount of training data --- Muon substantially outperforms AdamW, making it an effective choice for improving token efficiency in large language model training.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Training instability when scaling Muon", "weight": 1.0} -->

Despite its efficiency, scaling up Muon training reveals a challenge: training instability due to exploding attention logits, an issue that occurs more frequently with Muon but less with AdamW in our experiments. Existing mitigation strategies are insufficient. For instance, logit soft-cap directly clips the attention logits, but the dot products between queries and keys can still grow excessively before capping is applied. On the other hand, Query-Key Normalization (QK-Norm) is not applicable to multi-head latent attention (MLA), because its Key matrices are not fully materialized during inference.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Taming Muon with QK-Clip", "weight": 1.0} -->

To address this issue, we propose a novel weight-clipping mechanism QK-Clip to explicitly constrain attention logits. QK-Clip works by rescaling the query and key projection weights post-update to bound the growth of attention logits.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Taming Muon with QK-Clip", "weight": 1.0} -->

Let the input representation of a transformer layer be $\mathbf{X}$. For each attention head $h$, its query, key, and value projections are computed as where $\mathbf{W}_{q},\mathbf{W}_{k},\mathbf{W}_{v}$ are model parameters. The attention output is: We define the max logit, a per-head scalar, as the maximum input to softmax in this batch $B$: where $i,j$ are indices of different tokens in a training sample $\mathbf{X}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Taming Muon with QK-Clip", "weight": 1.0} -->

The core idea of QK-Clip is to rescale $\mathbf{W}_{k},\mathbf{W}_{q}$ whenever $S_{\max}^{h}$ exceeds a target threshold $\tau$. Importantly, this operation does not alter the forward/backward computation in the current step --- we merely use the max logit as a guiding signal to determine the strength to control the weight growth.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Taming Muon with QK-Clip", "weight": 1.0} -->

A naïve implementation clips all heads at the same time: where $\gamma=\min(1,\tau/S_{\max})$ with $S_{\max}=\max_{h}S_{\max}^{h}$, and $\alpha$ is a balancing parameter typically set to $0.5$, applying equal scaling to queries and keys.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Taming Muon with QK-Clip", "weight": 1.0} -->

However, we observe that in practice, only a small subset of heads exhibit exploding logits. In order to minimize our intervention on model training, we determine a per-head scaling factor $\gamma_{h}=\min(1,\tau/S_{\max}^{h})$, and opt to apply per-head QK-Clip. Such clipping is straightforward for regular multi-head attention (MHA). For MLA, we apply clipping only on unshared attention head components: $\textbf{q}^{C}$ and $\textbf{k}^{C}$ (head-specific components): each scaled by $\sqrt{\gamma_{h}}$ $\textbf{q}^{R}$ (head-specific rotary): scaled by $\gamma_{h}$, $\textbf{k}^{R}$ (shared rotary): left untouched to avoid effect across heads.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Taming Muon with QK-Clip", "weight": 1.0} -->

1:for each training step t do 2: // 1. Muon optimizer step 3: for each weight W ∈ ℝn × m do 4: Mt = μMt − 1 + Gt ⊳ M0 = 0, Gt is the grad of Wt, μ is momentum 5: $\mathbf{O}_{t}=\operatorname{Newton-Schulz}(\mathbf{M}_{t})\cdot\sqrt{\max(n,m)}\cdot 0.2$

<!-- chunk {"id": "body-0020", "role": "body", "section": "Taming Muon with QK-Clip", "weight": 1.0} -->

$\mathbf{W}_{kc}^{h}\leftarrow\mathbf{W}_{kc}^{h}\cdot\sqrt{\gamma}$ Algorithm 1 MuonClip Optimizer Figure 2: Left: During a mid-scale training run, attention logits rapidly exceed 1000, which could lead to potential numerical instabilities and even training divergence.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Taming Muon with QK-Clip", "weight": 1.0} -->

Right: Maximum logits for Kimi K2 with MuonClip and τ = 100 over the entire training run. The max logits rapidly increase to the capped value of 100, and only decay to a stable range after approximately 30% of the training steps, demonstrating the effective regulation effect of QK-Clip.

<!-- chunk {"id": "body-0022", "role": "body", "section": "MuonClip: The New Optimizer", "weight": 1.0} -->

We integrate Muon with weight decay, consistent RMS matching, and QK-Clip into a single optimizer, which we refer to as MuonClip (see Algorithm 1).

<!-- chunk {"id": "body-0023", "role": "body", "section": "MuonClip: The New Optimizer", "weight": 1.0} -->

We demonstrate the effectiveness of MuonClip from several scaling experiments. First, we train a mid-scale 9B activated and 53B total parameters Mixture-of-Experts (MoE) model using the vanilla Muon. As shown in Figure 2 (Left), we observe that the maximum attention logits quickly exceed a magnitude of 1000, showing that attention logits explosion is already evident in Muon training to this scale. Max logits at this level usually result in instability during training, including significant loss spikes and occasional divergence.

<!-- chunk {"id": "body-0024", "role": "body", "section": "MuonClip: The New Optimizer", "weight": 1.0} -->

Next, we demonstrate that QK-Clip does not degrade model performance and confirm that the MuonClip optimizer preserves the optimization characteristics of Muon without adversely affecting the loss trajectory. A detailed discussion of the experiment designs and findings is provided in the Appendix D.

<!-- chunk {"id": "body-0025", "role": "body", "section": "MuonClip: The New Optimizer", "weight": 1.0} -->

Finally, we train Kimi K2, a large-scale MoE model, using MuonClip with $\tau=100$ and monitor the maximum attention logits throughout the training run (Figure 2 (Right)). Initially, the logits are capped at 100 due to QK-Clip. Over the course of training, the maximum logits gradually decay to a typical operating range without requiring any adjustment to $\tau$. Importantly, the training loss remains smooth and stable, with no observable spikes, as shown in Figure 3, validating that MuonClip provides robust and scalable control over attention dynamics in large-scale language model training.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Pre-training Data: Improving Token Utility with Rephrasing", "weight": 1.0} -->

Token efficiency in pre-training refers to how much performance improvement is achieved for each token consumed during training. Increasing token utility---the effective learning signal each token contributes---enhances the per-token impact on model updates, thereby directly improving token efficiency. This is particularly important when the supply of high-quality tokens is limited and must be maximally leveraged. A naive approach to increasing token utility is through repeated exposure to the same tokens, which can lead to overfitting and reduced generalization.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Pre-training Data: Improving Token Utility with Rephrasing", "weight": 1.0} -->

A key advancement in the pre-training data of Kimi K2 over Kimi K1.5 is the introduction of a synthetic data generation strategy to increase token utility. Specifically, a carefully designed rephrasing pipeline is employed to amplify the volume of high-quality tokens without inducing significant overfitting. In this report, we describe two domain-specialized rephrasing techniques---targeted respectively at the Knowledge and Mathematics domains---that enable this controlled data augmentation.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Knowledge Data Rephrasing", "weight": 1.0} -->

Pre-training on natural, knowledge-intensive text presents a trade-off: a single epoch is insufficient for comprehensive knowledge absorption, while multi-epoch repetition yields diminishing returns and increases the risk of overfitting. To improve the token utility of high-quality knowledge tokens, we propose a synthetic rephrasing framework composed of the following key components: Style- and perspective-diverse prompting: Inspired by WRAP, we apply a range of carefully engineered prompts to enhance linguistic diversity while maintaining factual integrity. These prompts guide a large language model to generate faithful rephrasings of the original texts in varied styles and from different perspectives.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Knowledge Data Rephrasing", "weight": 1.0} -->

Chunk-wise autoregressive generation: To preserve global coherence and avoid information loss in long documents, we adopt a chunk-based autoregressive rewriting strategy. Texts are divided into segments, rephrased individually, and then stitched back together to form complete passages. This method mitigates implicit output length limitations that typically exist with LLMs. An overview of this pipeline is presented in Figure 4.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Knowledge Data Rephrasing", "weight": 1.0} -->

Fidelity verification: To ensure consistency between original and rewritten content, we perform fidelity checks that compare the semantic alignment of each rephrased passage with its source. This serves as an initial quality control step prior to training.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Knowledge Data Rephrasing", "weight": 1.0} -->

We compare data rephrasing with multi-epoch repetition by testing their corresponding accuracy on SimpleQA. We experiment with an early checkpoint of K2 and evaluate three training strategies: repeating the original dataset for 10 epochs, rephrasing the data once and repeating it for 10 epochs, and rephrasing the data 10 times with a single training pass. As shown in Table 1, the accuracy consistently improves across these strategies, demonstrating the efficacy of our rephrasing-based augmentation. We extended this method to other large-scale knowledge corpora and observed similarly encouraging results, and each corpora is rephrased at most twice.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Mathematics Data Rephrasing", "weight": 1.0} -->

To enhance mathematical reasoning capabilities, we rewrite high-quality mathematical documents into a "learning-note" style, following the methodology introduced in SwallowMath. In addition, we increased data diversity by translating high-quality mathematical materials from other languages into English.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Mathematics Data Rephrasing", "weight": 1.0} -->

Although initial experiments with rephrased subsets of our datasets show promising results, the use of synthetic data as a strategy for continued scaling remains an active area of investigation. Key challenges include generalizing the approach to diverse source domains without compromising factual accuracy, minimizing hallucinations and unintended toxicity, and ensuring scalability to large-scale datasets.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Pre-training Data Overall", "weight": 1.0} -->

The Kimi K2 pre-training corpus comprises 15.5 trillion tokens of curated, high-quality data spanning four primary domains: Web Text, Code, Mathematics, and Knowledge. Most data processing pipelines follow the methodologies outlined in Kimi K1.5. For each domain, we performed rigorous correctness and quality validation and designed targeted data experiments to ensure the curated dataset achieved both high diversity and effectiveness.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

Kimi K2 is a 1.04 trillion-parameter Mixture-of-Experts (MoE) transformer model with 32 billion activated parameters. The architecture follows a similar design to DeepSeek-V3, employing Multi-head Latent Attention (MLA) as the attention mechanism, with a model hidden dimension of 7168 and an MoE expert hidden dimension of 2048. Our scaling law analysis reveals that continued increases in sparsity yield substantial performance improvements, which motivated us to increase the number of experts to 384, compared to 256 in DeepSeek-V3. To reduce computational overhead during inference, we cut the number of attention heads to 64, as opposed to 128 in DeepSeek-V3. Table 2 presents a detailed comparison of architectural parameters between Kimi K2 and DeepSeek-V3.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

#Layers

<!-- chunk {"id": "body-0037", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

Experts Active per Token Number of Dense Layers Table 2: Architectural comparison between Kimi K2 and DeepSeek-V3

<!-- chunk {"id": "body-0038", "role": "body", "section": "Sparsity Scaling Law", "weight": 1.0} -->

We develop a sparsity scaling law tailored for the Mixture-of-Experts (MoE) model family using Muon. Sparsity is defined as the ratio of the total number of experts to the number of activated experts. Through carefully controlled small-scale experiments, we observe that --- under a fixed number of activated parameters (i.e., constant FLOPs) --- increasing the total number of experts (i.e., increasing sparsity) consistently lowers both the training and validation loss, thereby enhancing overall model performance (Figure 6). Concretely, under the compute-optimal sparsity scaling law, achieving the same validation loss of 1.5, sparsity 48 reduces FLOPs by 1.69×, 1.39×, and 1.15× compared to sparsity levels 8, 16, and 32, respectively. Though increasing sparsity leads to better performance, this gain comes with increased infrastructure complexity. To balance model performance with cost, we adopt a sparsity of 48 for Kimi K2, activating 8 out of 384 experts per forward pass.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Number of Attention Heads", "weight": 1.0} -->

DeepSeek-V3 sets the number of attention heads to roughly twice the number of model layers to better utilize memory bandwidth and enhance computational efficiency. However, as the context length increases, doubling the number of attention heads leads to significant inference overhead, reducing efficiency at longer sequence lengths. This becomes a major limitation in agentic applications, where efficient long context processing is essential. For example, with a sequence length of 128k, increasing the number of attention heads from 64 to 128, while keeping the total expert count fixed at 384, leads to an 83% increase in inference FLOPs. To evaluate the impact of this design, we conduct controlled experiments comparing configurations where the number of attention heads equals the number of layers against those with double number of heads, under varying training FLOPs. Under iso-token training conditions, we observe that doubling the attention heads yields only modest improvements in validation loss (ranging from 0.5% to 1.2%) across different compute budgets (Figure 6). Given that sparsity 48 already offers strong performance, the marginal gains from doubling attention heads do not justify the inference cost. Therefore we choose to 64 attention heads.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Compute Cluster", "weight": 1.0} -->

Kimi K2 was trained on a cluster equipped with NVIDIA H800 GPUs. Each node in the H800 cluster contains 2 TB RAM and 8 GPUs connected by NVLink and NVSwitch within nodes. Across different nodes, $\text{8}\!\times\!\text{400}~\text{Gbps}$ RoCE interconnects are utilized to facilitate communications.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Parallelism for Model Scaling", "weight": 1.0} -->

Training of large language models often progresses under dynamic resource availability. Instead of optimizing one parallelism strategy that's only applicable under specific amount of resources, we pursue a flexible strategy that allows Kimi K2 to be trained on any number of nodes that is a multiple of 32. Our strategy leverages a combination of 16-way Pipeline Parallelism (PP) with virtual stages, 16-way Expert Parallelism (EP), and ZeRO-1 Data Parallelism.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Parallelism for Model Scaling", "weight": 1.0} -->

Under this setting, storing the model parameters in and their gradient accumulation buffer in requires approximately 6 TB of GPU memory, distributed over a model-parallel group of 256 GPUs. Placement of optimizer states depends on the training configurations. When the total number of training nodes is large, the optimizer states are distributed, reducing its per-device memory footprint to a negligible level. When the total number of training nodes is small (e.g., 32), we can offload some optimizer states to CPU.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Parallelism for Model Scaling", "weight": 1.0} -->

This approach allows us to reuse an identical parallelism configuration for both small- and large-scale experiments, while letting each GPU hold approximately 30 GB of GPU memory for all states. The rest of the GPU memory are used for activations, as described in Sec. 2.4.3. Such a consistent design is important for research efficiency, as it simplifies the system and substantially accelerates experimental iteration.

<!-- chunk {"id": "body-0044", "role": "body", "section": "EP communication overlap with interleaved 1F1B", "weight": 1.0} -->

By increasing the number of warm-up micro-batches, we can overlap EP all-to-all communication with computation under the standard interleaved 1F1B schedule. In comparison, DualPipe doubles the memory required for parameters and gradients, necessitating an increase in parallelism to compensate. Increasing PP introduces more bubbles, while increasing EP, as discussed below, incurs higher overhead. The additional costs are prohibitively high for training a large model with over 1 trillion parameters and thus we opted not to use DualPipe.

<!-- chunk {"id": "body-0045", "role": "body", "section": "EP communication overlap with interleaved 1F1B", "weight": 1.0} -->

However, interleaved 1F1B splits the model into more stages, introducing non-trivial PP communication overhead. To mitigate this cost, we decouple the weight-gradient computation from each micro-batch's backward pass and execute it in parallel with the corresponding PP communication. Consequently, all PP communications can be effectively overlapped except for the warm-up phase.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Smaller EP size", "weight": 1.0} -->

To ensure full computation-communication overlap during the 1F1B stage, the reduced attention computation time in K2 (which has 64 attention heads compared to 128 heads in DeepSeek-V3) necessitates minimizing the time of EP operations. This is achieved by adopting the smallest feasible EP parallelization strategy, specifically EP = 16. Utilizing a smaller EP group also relaxes expert-balance constraints, allowing for near-optimal speed to be achieved without further tuning.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Activation Reduction", "weight": 1.0} -->

After reserving space for parameters, gradient buffers, and optimizer states, the remaining GPU memory on each device is insufficient to hold the full MoE activations. To ensure the activation memory fits within the constraints, especially for the initial pipeline stages that accumulate the largest activations during the 1F1B warm-up phase, the following techniques are employed.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Selective recomputation", "weight": 1.0} -->

Recomputation is applied to inexpensive, high-footprint stages, including LayerNorm, SwiGLU, and MLA up-projections. Additionally, MoE down-projections are recomputed during training to further reduce activation memory. While optional, this recomputation maintains adequate GPU memory, preventing crashes caused by expert imbalance in early training stages.

<!-- chunk {"id": "body-0049", "role": "body", "section": "FP8 storage for insensitive activations", "weight": 1.0} -->

Inputs of MoE up-projections and SwiGLU are compressed to FP8-E4M3 in 1$\times$ 128 tiles with scales. Small-scale experiments show no measurable loss increase. Due to potential risks of performance degradation that we observed during preliminary study, we do not apply FP8 in computation.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Activation CPU offload", "weight": 1.0} -->

All remaining activations are offloaded to CPU RAM. A copy engine is responsible for streaming the offload and onload, overlapping with both computation and communication kernels. During the 1F1B phase, we offload the forward activations of the previous micro-batch while prefetching the backward activations of the next. The warm-up and cool-down phases are handled similarly and the overall pattern is shown in Figure 7. Although offloading may slightly affect EP traffic due to PCIe traffic congestion, our tests show that EP communication remains fully overlapped.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Training recipe", "weight": 1.0} -->

We pre-trained the model with a 4,096-token context window using the MuonClip optimizer (Algorithm 1) and the WSD learning rate schedule, processing a total of 15.5T tokens. The first 10T tokens were trained with a constant learning rate of 2e-4 after a 500-step warm-up, followed by 5.5T tokens with a cosine decay from 2e-4 to 2e-5. Weight decay was set to 0.1 throughout, and the global batch size was held at 67M tokens. The overall training curve is shown in Figure 3.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Training recipe", "weight": 1.0} -->

Towards the end of pre-training, we conducted an annealing phase followed by a long-context activation stage. The batch size was kept constant at 67M tokens, while the learning rate was decayed from 2e-5 to 7e-6. In this phase, the model was trained on 400 billion tokens with a 4k sequence length, followed by an additional 60 billion tokens with a 32k sequence length. To extend the context window to 128k, we employed the YaRN method.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Supervised Fine-Tuning", "weight": 1.0} -->

We employ the Muon optimizer in our post-training and recommend its use for fine-tuning with K2. This follows from the conclusion of our previous work that a Muon-pre-trained checkpoint produces the best performance with Muon fine-tuning.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Supervised Fine-Tuning", "weight": 1.0} -->

We construct a large-scale instruction-tuning dataset spanning diverse domains, guided by two core principles: maximizing prompt diversity and ensuring high response quality. To this end, we develop a suite of data generation pipelines tailored to different task domains, each utilizing a combination of human annotation, prompt engineering, and verification processes. We adopt K1.5 and other in-house domain-specialized expert models to generate candidate responses for various tasks, followed by LLMs or human-based judges to perform automated quality evaluation and filtering. For agentic data, we create a data synthesis pipeline to teach models tool-use capabilities through multi-step, interactive reasoning.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Large-Scale Agentic Data Synthesis for Tool Use Learning", "weight": 1.0} -->

A critical capability of modern LLM agents is their ability to autonomously use unfamiliar tools, interact with external environments, and iteratively refine their actions through reasoning, execution, and error correction. Agentic tool use capability is essential for solving complex, multi-step tasks that require dynamic interaction with real-world systems. Recent benchmarks such as ACEBench and $\tau$-bench have highlighted the importance of comprehensive tool-use evaluation, while frameworks like ToolLLM and ACEBench have demonstrated the potential of teaching models to use thousands of tools effectively.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Large-Scale Agentic Data Synthesis for Tool Use Learning", "weight": 1.0} -->

However, training such capabilities at scale presents a significant challenge: while real-world environments provide rich and authentic interaction signals, they are often difficult to construct at scale due to cost, complexity, privacy and accessibility constraints. Recent work on synthetic data generation (AgentInstruct; Self-Instruct; StableToolBench; ZeroSearch ) has shown promising results in creating large-scale data without relying on real-world interactions. Building on these advances and inspired by ACEBench 's comprehensive data synthesis framework, we developed a pipeline that simulates real-world tool-use scenarios at scale, enabling the generation of tens of thousands of diverse and high-quality training examples.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Large-Scale Agentic Data Synthesis for Tool Use Learning", "weight": 1.0} -->

(a) Synthesizing tool specs, agents and tasks (b) Generating agent trajectories Figure 8: Data synthesis pipeline for tool use. (a) Tool specs are from both real-world tools and LLMs; agents and tasks are the generated from the tool repo. (b) Multi-agent pipeline to generate and filter trajectories with tool calling.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Large-Scale Agentic Data Synthesis for Tool Use Learning", "weight": 1.0} -->

(a) t-SNE visualization of real MCP tools, colored by their original source categories (b) t-SNE visualization of synthetic tools, colored by pre-defined domain categories Figure 9: t-SNE visualizations of tool embeddings. (a) Real-world MCP tools exhibit natural clustering based on their original source categories. (b) Synthetic tools are organized into pre-defined domain categories, providing systematic coverage of the tool space. Together, they ensure comprehensive representation across different tool functionalities.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Large-Scale Agentic Data Synthesis for Tool Use Learning", "weight": 1.0} -->

There are three stages in our data synthesis pipeline, depicted in Fig. 8.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Large-Scale Agentic Data Synthesis for Tool Use Learning", "weight": 1.0} -->

Tool spec generation: we first construct a large repository of tool specs from both real-world tools and LLM-synthetic tools; Agent and task generation: for each tool-set sampled from the tool repository, we generate an agent to use the toolset and some corresponding tasks; Trajectory generation: for each agent and task, we generate trajectories where the agent finishes the task by invoking tools.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Domain Evolution and Tool Generation", "weight": 1.0} -->

We construct a comprehensive tool repository through two complementary approaches. First, we directly fetch 3000+ real MCP (Model Context Protocol) tools from GitHub repositories, leveraging existing high-quality tool specs. Second, we systematically evolve synthetic tools through a hierarchical domain generation process: we begin with key categories (e.g., financial trading, software applications, robot control), then evolve multiple specific application domains within each category. Specialized tools are then synthesized for each domain, with clear interfaces, descriptions, and operational semantics. This evolution process produces over 20,000 synthetic tools. Figure 9 visualizes the diversity of our tool collection through t-SNE embeddings, demonstrating that both MCP and synthetic tools cover complementary regions of the tool space.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Agent Diversification", "weight": 1.0} -->

We generate thousands of distinct agents by synthesizing various system prompts and equipping them with different combinations of tools from our repository. This creates a diverse population of agents with varied capabilities, areas of expertise, and behavioral patterns, ensuring a broad coverage of potential use cases.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Rubric-Based Task Generation", "weight": 1.0} -->

For each agent configuration, we generate tasks that range from simple to complex operations. Each task is paired with an explicit rubric that specifies success criteria, expected tool-use patterns, and evaluation checkpoints. This rubric-based approach ensures a consistent and objective evaluation of agent performance.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Multi-turn Trajectory Generation", "weight": 1.0} -->

We simulate realistic tool-use scenarios through several components: User Simulation: LLM-generated user personas with distinct communication styles and preferences engage in multi-turn dialogues with agents, creating naturalistic interaction patterns.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Multi-turn Trajectory Generation", "weight": 1.0} -->

Tool Execution Environment: A sophisticated tool simulator (functionally equivalent to a world model) executes tool calls and provides realistic feedback. The simulator maintains and updates state after each tool execution, enabling complex multi-step interactions with persistent effects. It introduces controlled stochasticity to produce varied outcomes including successes, partial failures, and edge cases.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Quality Evaluation and Filtering", "weight": 1.0} -->

An LLM-based judge evaluates each trajectory against the task rubrics. Only trajectories that meet the success criteria are retained for training, ensuring high-quality data while allowing natural variation in task-completion strategies.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Hybrid Approach with Real Execution Environments", "weight": 1.0} -->

While simulation provides scalability, we acknowledge the inherent limitation of simulation fidelity. To address this, we complement our simulated environments with real execution sandboxes for scenarios where authenticity is crucial, particularly in coding and software engineering tasks. These real sandboxes execute actual code, interact with genuine development environments, and provide ground-truth feedback through objective metrics such as test suite pass rates. This combination ensures that our models learn from both the diversity of simulated scenarios and the authenticity of real executions, significantly strengthening practical agent capabilities.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Hybrid Approach with Real Execution Environments", "weight": 1.0} -->

By leveraging this hybrid pipeline that combines scalable simulation with targeted real-world execution, we generate diverse, high-quality tool-use demonstrations that balance coverage and authenticity. The scale and automation of our synthetic data generation, coupled with the grounding provided by real execution environments, effectively implements large-scale rejection sampling through our quality filtering process. This high-quality synthetic data, when used for supervised fine-tuning, has demonstrated significant improvements in the model's tool-use capabilities across a wide range of real-world applications.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

Reinforcement learning (RL) is believed to have better token efficiency and generalization than SFT. Based on the work of K1.5, we continue to scale RL in both task diversity and training FLOPs in K2. To support this, we develop a Gym-like extensible framework that facilitates RL across a wide range of scenarios. We extend the framework with a large number of tasks with verifiable rewards. For tasks that rely on subjective preferences, such as creative writing and open-ended question answering, we introduce a self-critic reward in which the model performs pairwise comparisons to judge its own outputs. This approach allows tasks from various domains to all benefit from the RL paradigm.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Math, STEM and Logical Tasks", "weight": 1.0} -->

For math, stem and logical reasoning domains, our RL data preparation follows two key principles, *diverse coverage* and *moderate difficulty*.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Math, STEM and Logical Tasks", "weight": 1.0} -->

*Diverse Coverage.* For math and stem tasks, we collect high-quality QA pairs using a combination of expert annotations, internal QA extraction pipelines, and open datasets. During the collection process, we leverage a tagging system to deliberately increase coverage of under-covered domains. For logical tasks, our dataset comprises a variety of formats, including structured data tasks (e.g., multi-hop tabular reasoning, cross-table aggregation) and logic puzzles (e.g., the 24-game, Sudoku, riddles, cryptarithms, and Morse-code decoding).

<!-- chunk {"id": "body-0072", "role": "body", "section": "Math, STEM and Logical Tasks", "weight": 1.0} -->

*Moderate Difficulty.* The RL prompt-set should be neither too easy nor too hard, both of which may produce little signal and reduce learning efficiency. We assess the difficulty of each problem using the SFT model's pass@k accuracy and select only problems with moderate difficulty.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Complex Instruction Following", "weight": 1.0} -->

Effective instruction following requires not only understanding explicit constraints but also navigating implicit requirements, handling edge cases, and maintaining consistency over extended dialogues. We address these challenges through a hybrid verification framework that combines automated verification with adversarial detection, coupled with a scalable curriculum generation pipeline. Our approach employs a dual-path system to ensure both precision and robustness: Hybrid Rule Verification. We implement two verification mechanisms: deterministic evaluation via code interpreters for instructions with verifiable outputs (e.g., length, style constraints), and LLM-as-judge evaluation for instructions requiring nuanced understanding of constraints. To address potential adversarial behaviors where models might claim instruction fulfillment without actual compliance, we incorporate an additional hack-check layer that specifically detects such deceptive claims.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Complex Instruction Following", "weight": 1.0} -->

Multi-Source Instruction Generation. To construct our training data, we employ three distinct generation strategies to ensure comprehensive coverage: expert-crafted complex conditional prompts and rubrics developed by our data team agentic instruction augmentation inspired by AutoIF, and a fine-tuned model specialized for generating additional instructions that probe specific failure modes or edge cases. This multipronged approach ensures both breadth and depth in instruction coverage.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Faithfulness", "weight": 1.0} -->

Faithfulness is essential for an agentic model operating in scenarios such as multi-turn tool use, self-generated reasoning chains, and open-environment interactions. Inspired by the evaluation framework from FACTS Grounding, we train a sentence-level faithfulness judge model to perform automated verification. The judge is effective in detecting sentences that make a factual claim without supporting evidence in context. It serves as a reward model to enhance overall faithfulness performance.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Coding & Software Engineering", "weight": 1.0} -->

To enhance our capability in tackling competition-level programming problems, we gather problems and their judges from both open-source datasets and synthetic sources. To ensure the diversity of the synthetic data and the correctness of reward signals, we incorporate high-quality human-written unit tests retrieved from pre-training data.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Coding & Software Engineering", "weight": 1.0} -->

For software engineering tasks, we collect a vast amount of pull requests and issues from GitHub to build software development environment that consists of user prompts/issues and executable unit tests. This environment was built on a robust sandbox infrastructure, powered by Kubernetes for scalability and security. It supports over 10,000 concurrent sandbox instances with stable performance, making it ideal for both competitive coding and software engineering tasks.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Safety", "weight": 1.0} -->

Our work to enhance the safety begins with a human-curated set of seed prompts, manually crafted to encompass prevalent risk categories such as violence, fraud, and discrimination.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Safety", "weight": 1.0} -->

To simulate sophisticated jailbreak attempts (e.g., role-playing, literary narratives, and academic discourse), we employ an automated prompt evolution pipeline with three key components: Attack Model: Iteratively generates adversarial prompts designed to elicit unsafe responses from the target LLM.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Safety", "weight": 1.0} -->

Target Model: Produces responses to these prompts, simulating potential vulnerabilities.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Safety", "weight": 1.0} -->

Judge Model: Evaluates the interaction to determine if the adversarial prompt successfully bypasses safety mechanisms.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Safety", "weight": 1.0} -->

Each interaction is assessed using a task-specific rubric, enabling the judge model to provide a binary success/failure label.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Beyond Verification: Self-Critique Rubric Reward", "weight": 1.0} -->

To extend model alignment beyond tasks with verifiable reward, we introduce a framework for general reinforcement learning from self-critic feedbacks. This approach is designed to align LLMs with nuanced human preferences, including helpfulness, creativity, depth of reasoning, factuality, and safety, by extending the capabilities learned from verifiable scenarios to a broader range of subjective tasks. The framework operates using a Self-Critique Rubric Reward mechanism, where the model evaluates its own outputs to generate preference signals. To bootstrap K2 as a competent judge, we curated a mixture of open-source and in-house preference datasets and initialize its critic capability in the SFT stage.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Self-Critiqued Policy Optimization", "weight": 1.0} -->

In the first core process of the learning loop, the K2 actor generates responses for general prompts that cover a wide range of use cases. The K2 critic then ranks all results by performing pairwise evaluations against a combination of rubrics, which incorporates both core rubrics (Appendix. F.1), which represent the fundamental values of our AI assistant that Kimi cherish, prescriptive rubrics (Appendix. F.2) that aim to eliminate reward hacking, and human-annotated rubrics crafted by our data team for specific instructional contexts. Although certain rubrics can be designated as mandatory, K2 retains the flexibility to weigh them against its internal priors. This capacity enables a dynamic and continuous alignment with its evolving on-policy behavior, ensuring that the model's responses remain coherent with its core identity while adapting to specific instructions.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Closed-Loop Critic Refinement and Alignment", "weight": 1.0} -->

During RL training, the critic model is refined using verifiable signals. On-policy rollouts generated from verifiable-reward prompts are used to continuously update the critic, a crucial step that distills objective performance signals from RLVR directly into its evaluation model. This transfer learning process grounds its more subjective judgments in verifiable data, allowing the performance gains from verifiable tasks to enhance the critic's judgment on complex tasks that lack explicit reward signals. This closed-loop process ensures that the critic continuously recalibrates its evaluation standards in lockstep with the policy's evolution. By grounding subjective evaluation in verifiable data, the framework enables robust and scalable alignment with complex, non-verifiable human objectives.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Closed-Loop Critic Refinement and Alignment", "weight": 1.0} -->

Consequently, this holistic alignment yields comprehensive performance improvements across a wide spectrum of domains, including user intent understanding, creative writing, complex reasoning, and nuanced language comprehension.

<!-- chunk {"id": "body-0087", "role": "body", "section": "RL Algorithm", "weight": 1.0} -->

We adopt the policy optimization algorithm introduced in K1.5 as the foundation for K2. For each problem $x$, we sample $K$ responses $\{y_{1},\dots,y_{k}\}$ from the previous policy $\pi_{\mathrm{old}}$, and optimize the model $\pi_{\theta}$ with respect to the following objective: where $\bar{r}(x)=\frac{1}{k}\sum_{i=1}^{k}r(x,y_{i})$ is the mean rewards of the sampled responses, $\tau>0$ is a regularization parameter that promotes stable learning. As in SFT, we employ the Muon optimizer to minimize this objective. As we scale RL training to encompass a broader range of tasks in K2, a primary challenge is achieving consistent performance improvements across all domains. To address this, we introduce several additions to the RL algorithm.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Budget Control", "weight": 1.0} -->

It has been widely observed that RL often results in a substantial increase in the length of model-generated responses. While longer responses can enable the model to utilize additional test-time compute for improved performance on complex reasoning tasks, the benefits often do not justify its inference cost in non-reasoning domains. To encourage the model to properly distribute inference budget, we enforce a per-sample *maximum token budget* throughout RL training, where the budget is determined based on the type of task. Responses that exceed this token budget are truncated and assigned a penalty, which incentivizes the model to generate solutions within the specified limit. Empirically, this approach significantly enhances the model's token efficiency, encouraging concise yet effective solutions across all domains.

<!-- chunk {"id": "body-0089", "role": "body", "section": "PTX Loss", "weight": 1.0} -->

To prevent the potential forgetting of valuable, high-quality data during joint RL training, we curate a dataset comprising hand-selected, high-quality samples and integrate it into the RL objective through an auxiliary PTX loss. This strategy not only leverages the advantages of high-quality data, but also mitigates the risk of overfitting to the limited set of tasks explicitly present in the training regime. This augmentation substantially improves the model's generalization across a broader range of domains.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Temperature Decay", "weight": 1.0} -->

For tasks such as creative writing and complex reasoning, we find that promoting exploration via a high sampling temperature during the initial stages of training is crucial. A high temperature allow the model to generate diverse and innovative responses, thereby facilitating the discovery of effective strategies and reducing the risk of premature convergence to suboptimal solutions. However, retaining a high temperature in the later stages of training or during evaluation can be detrimental, as it introduces excessive randomness and compromises the reliability and consistency of the model's outputs. To address this, we employ a temperature decay schedule, to shift from exploration to exploitation throughout the training. This strategy ensures that the model leverages exploration when it is most beneficial, while ultimately converge on stable and high-quality outputs.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Colocated Architecture", "weight": 1.0} -->

Similar to K1.5, we adopt a hybrid colocated architecture for our synchronized RL training, where the training and inference engines live on the same workers. When one engine is actively working, the other engine releases or offloads its GPU resources to accommodate. In each iteration of RL training, a centralized controller first calls the inference engine to generate new data for training. It then notifies the training engine to train on the new data, and send updated parameters to the inference engine for the next iteration.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Colocated Architecture", "weight": 1.0} -->

Each engine is heavily optimized for throughput. In addition, as the model scales to the size of K2, the latency of engine switching and failure recovery becomes significant. We present our system design considerations in these aspects.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Efficient Engine Switching", "weight": 1.0} -->

During rollout, the parameters of the training engine are offloaded to DRAM. Bringing up the training engine is therefore a simple step of H2D transmission. However, bringing up the inference engine is a bigger challenge, as it must obtain updated parameters from the training engine with a different sharding paradigm.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Efficient Engine Switching", "weight": 1.0} -->

We opt to broadcast the full parameter set across the entire cluster, regardless of the specific sharding schemes on each inference worker. While this transfers several times more data than a theoretically optimal approach, it offers a simpler system design that is less intrusive to the training and inference engines. We chose to trade off this minor overhead to fully decouple the training engine and the inference engine, significantly simplifying maintenance and testing.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Efficient Engine Switching", "weight": 1.0} -->

Notably, this approach outperforms the transfer-what-you-need method due to reduced synchronization overhead and higher network bandwidth utilization. Our system can complete a full parameter update for Kimi K2 with less than 30 seconds, a negligible duration for a typical RL training iteration. The source code for the checkpoint engine is available on Github^55^5

<!-- chunk {"id": "body-0096", "role": "body", "section": "Efficient System Startup", "weight": 1.0} -->

As large-scale training is prone to system failure, optimizing the startup time is crucial for models as large as Kimi K2.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Efficient System Startup", "weight": 1.0} -->

To start the training engine, we let each training worker selectively read part or none of the parameters from disk, and broadcast necessary parameters to its peers. The design goal is to ensure all workers collectively read the checkpoint only once, minimizing expensive disk IO.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Efficient System Startup", "weight": 1.0} -->

As the inference engines are independent replicas, we would like to avoid introducing extra synchronization barriers between them. Therefore, we opt to reuse checkpoint engine for startup: we let checkpoint engine collectively read the checkpoint from disk, similar to how the training engine starts. Then it updates the state of the uninitialized inference engine, using the approach introduced in the previous section. By leveraging the dedicated checkpoint engine, the system also becomes robust to single-point failures, because an inference replica can restart without communicating with other replicas.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Agentic Rollout", "weight": 1.0} -->

Our RL infrastructure supports the training of long-horizon, multi-turn agentic tasks. During rollout, these tasks present distinct challenges, such as complex environmental interactions and prolonged rollout durations. Here we introduce a few optimizations to alleviate these issues.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Agentic Rollout", "weight": 1.0} -->

Due to the diversity of environments, certain interactions may be blocked on waiting for environment feedback (e.g., a virtual machine or a code interpreter), leaving the GPUs idle. We employ two strategies to maximize GPU utilization: (i) we deploy heavy environments as dedicated services that can scale up more easily; (ii) we employ a large number of concurrent rollouts to amortize the latency induced by certain expensive interactions.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Agentic Rollout", "weight": 1.0} -->

Another challenge in agentic rollout is that individual rollout trajectories can be extremely long. To prevent long-tail trajectories from blocking the entire rollout process, we employ the partial rollout technique. This strategy allows long-tail unfinished tasks to be paused, and resumed in the next RL iteration.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Agentic Rollout", "weight": 1.0} -->

To improve research efficiency, we also design a unified interface inspired by the OpenAI Gym framework to streamline the integration of new environments. We hope to scale our RL infrastructure to more diverse interactive environments in the future.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Evaluations", "weight": 1.0} -->

This section begins with the post-training evaluation of Kimi-K2-Instruct, followed by a brief overview of the capabilities of Kimi-K2-Base. We conclude with a comprehensive safety evaluation.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

We assess Kimi-K2-Instruct across different areas. For coding, we adopt LiveCodeBench v6, OJBench, MultiPL-E, SWE-bench Verified, TerminalBench, Multi-SWE-bench, SWE-Lancer, PaperBench, and Aider-Polyglot. For tool use tasks, we evaluate performance on $\tau^{2}$-Bench and AceBench, which emphasize multi-turn tool-calling capabilities. In reasoning, we include a wide range of mathematical, science and logical tasks: AIME 2024/2025, MATH-500, HMMT 2025, CNMO 2024, PolyMath-en, ZebraLogic, AutoLogi, GPQA-Diamond, SuperGPQA, and Humanity's Last Exam (Text-Only). We benchmark the long-context capabilities: MRCR^66^6 for long-context retrieval, and DROP, FRAMES and LongBench v2 for long-context reasoning. For factuality, we evaluate FACTS Grounding, the Vectara Hallucination Leaderboard \[74")\], and FaithJudge.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

Finally, general capabilities are assessed using MMLU, MMLU-Redux, MMLU-Pro, IFEval, Multi-Challenge, SimpleQA, and LiveBench.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Baselines", "weight": 1.0} -->

We benchmark against both open-source and proprietary frontier models, ensuring every candidate is evaluated under its non-thinking configuration to eliminate additional gains from test-time compute. Open-source baselines: DeepSeek-V3-0324 and Qwen3-235B-A22B, with the latter run in the vendor-recommended no-thinking regime. Proprietary baselines: Claude Sonnet 4, Claude Opus 4, GPT-4.1, and Gemini 2.5 Flash Preview. Each invoked in its respective non-thinking mode via official APIs under unified temperature and top-p settings.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Baselines", "weight": 1.0} -->

Evaluation Configurations All runs query models in their non-thinking mode. Output token length is capped at 8192 tokens everywhere except SWE-bench Verified (Agentless), which is raised to 16384. For benchmarks with high per-question variance, we adopt repeated sampling $k$ times and average the results to obtain stable scores, denoted as Avg@k. For long-context tasks, we set the context window size to 128K tokens during evaluation, truncating any input that exceeds this limit to fit within the window. SWE-bench Verified is evaluated in two modes: Agentless Coding via Single Patch without Test (Acc) and Agentic Coding via bash/editor tools under both Single Attempt (Acc) and Multiple Attempts (Acc) using best-of-N selection with an internal verifier; SWE-bench Multilingual is tested only in the single-attempt agentic setting. Some data points have been omitted due to prohibitively expensive evaluation costs.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Baselines", "weight": 1.0} -->

SWE-bench Verified Agentless-Single-Patch (Pass@1) SWE-bench Verified Agentic-Single-Attempt (Pass@1) SWE-bench Verified Agentic-Multi-Attempt (Pass@1) SWE-bench Multilingual (Pass@1) Paper Bench Code-Dev (Acc.)

<!-- chunk {"id": "body-0109", "role": "body", "section": "Baselines", "weight": 1.0} -->

Tool Use Tasks Tau2 retail (Avg@4) Tau2 airline (Avg@4) Tau2 telecom (Avg@4) Math & STEM Tasks Humanity’s Last Exam (Acc.)

<!-- chunk {"id": "body-0110", "role": "body", "section": "Baselines", "weight": 1.0} -->

IFEval (Prompt Strict) Arena Hard v2.0 Hard Prompt (Win rate) Arena Hard v2.0 Creative Writing (Win rate) FACTS Grounding (Adjusted) Table 3: Performance comparison of Kimi-K2-Instruct against leading open-source and proprietary models across diverse tasks. Bold denotes the global SOTA; underlined bold indicates the best open-source result. Data points marked with * are taken directly from the model’s technical report or blog.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Evaluation Results", "weight": 1.0} -->

A comprehensive evaluation results of Kimi-K2-Instruct is shown in Table 3, with detailed explanation provided in the Appendix C.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Agentic and Competitive Coding", "weight": 1.0} -->

Kimi-K2-Instruct demonstrates state-of-the-art open-source performance on real-world SWE tasks. It outperforms most baselines on SWE-bench Verified (65.8%, 71.6% with multiple attemps), SWE-bench Multilingual (47.3%), and SWE-lancer (39.1%), significantly closing the gap with Claude 4 Opus and Sonnet. On competitive coding benchmarks (e.g., LiveCodeBench v6 53.7%, OJBench 27.1%), it also leads among all models, highlighting its practical coding proficiency across difficulty levels.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Agentic Tool Use", "weight": 1.0} -->

On multi-turn tool-use benchmarks, Kimi-K2-Instruct sets a new standard. It achieves 66.1 Pass@1 on $\tau^{2}$-Bench and 76.5 on ACEBench, substantially outperforming all baselines. These results affirm its strength in grounded, controlled, and agent-driven tool orchestration across domains.

<!-- chunk {"id": "body-0114", "role": "body", "section": "General Capabilities", "weight": 1.0} -->

Kimi-K2-Instruct exhibits strong, balanced performance across general knowledge, math, instruction following, and long-context tasks. It surpasses open-source peers on SimpleQA (31.0%), MMLU (89.5%) and MMLU-Redux (92.7%), and leads all models on instruction benchmarks (IFEval: 89.8%, Multi-Challenge: 54.1%). In math and STEM, it achieves top-tier scores, and remains competitive on long-context factuality and retrieval (DROP: 93.5%, MRCR: 55.0%). These results position Kimi-K2-Instruct as a well-rounded and capable generalist across both short- and long-context settings.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Open-Ended Evaluation", "weight": 1.0} -->

On the LMSYS Arena leaderboard, Kimi-K2-Instruct ranks as the top-1 open-source model and 5th overall based on over 3,000 user votes. This real-world preference signal---across diverse, blind prompts---underscores Kimi-K2's strengths in generating high-quality responses on open-ended tasks.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

We evaluate Kimi-K2-Base across diverse capability areas. For general capabilities, we assess on MMLU, MMLU-Pro, MMLU-Redux, BBH, TriviaQA, SuperGPQA, SimpleQA, HellaSwag, AGIEval, GPQA-Diamond, ARC-Challenge, and WinoGrande. For coding capabilities, we employ EvalPlus (averaging HumanEval, MBPP, HumanEval+, and MBPP+), LiveCodeBench v6, and CRUXEval. For mathematical reasoning, we utilize GSM8K, GSM8K-Platinum, MATH, and CMATH. For Chinese language capabilities, we evaluate on C-Eval, CMMLU, and CSimpleQA.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Baselines", "weight": 1.0} -->

We benchmark against leading open-source foundation models: DeepSeek-V3-Base, Qwen2.5-72B-Base (Note that Qwen3-235B-A22B-Base is not open-sourced, and the largest open-sourced base model in the Qwen series is Qwen2.5-72B-Base), and Llama 4-Maverick (Llama 4-Behemoth is also not open-sourced). All models are evaluated under identical configurations to ensure fair comparison.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Evaluation Configurations", "weight": 1.0} -->

We employ perplexity-based evaluation for MMLU, MMLU-Redux, GPQA-Diamond, HellaSwag, ARC-Challenge, C-Eval, and CMMLU. Generation-based evaluation is used for MMLU-Pro, SuperGPQA, TriviaQA, BBH, CSimpleQA, MATH, CMATH, GSM8K, GSM8K-Platinum, CRUXEval, LiveCodeBench, and EvalPlus. To mitigate the high variance inherent to GPQA-Diamond, we report the mean score across eight independent runs. All evaluations are conducted using our internal framework derived from LM-Harness-Evaluation, ensuring consistent settings across all models.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Evaluation Results", "weight": 1.0} -->

Table 4 presents a comprehensive comparison of Kimi-K2-Base against leading open-source foundation models across diverse evaluation benchmarks. The results demonstrate that Kimi-K2-Base achieves state-of-the-art performance across the majority of evaluated tasks, establishing it as a leading foundation model in the open-source landscape.

<!-- chunk {"id": "body-0120", "role": "body", "section": "General Language Understanding", "weight": 1.0} -->

Kimi-K2-Base achieves state-of-the-art performance on 10 out of 12 English language benchmarks. Notable results include MMLU (87.79%), MMLU-Pro (69.17%), MMLU-Redux (90.17%), SuperGPQA (44.67%), and SimpleQA (35.25%), significantly outperforming all baselines.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Coding Capabilities", "weight": 1.0} -->

On coding benchmarks, Kimi-K2-Base sets new standards with leading performance across all metrics. It achieves 74.00% on CRUXEval-I-cot, 83.50% on CRUXEval-O-cot, 26.29% on LiveCodeBench v6, and 80.33% on EvalPlus, demonstrating superior code generation and comprehension abilities, particularly in scenarios requiring step-by-step reasoning.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Mathematical Reasoning", "weight": 1.0} -->

Kimi-K2-Base exhibits exceptional mathematical capabilities, leading on three out of four benchmarks: MATH (70.22%), GSM8K (92.12%), and GSM8K-Platinum (94.21%). It maintains competitive performance on CMATH (90.26%), narrowly behind DeepSeek-V3-Base (90.53%). These results highlight the model's robust mathematical problem-solving abilities across varying difficulty levels.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Chinese Language Understanding", "weight": 1.0} -->

The model demonstrates superior multilingual capabilities, achieving state-of-the-art results across all Chinese language benchmarks: C-Eval (92.50%), CMMLU (90.90%), and CSimpleQA (77.57%). These results establish Kimi-K2-Base as a leading model for Chinese language understanding while maintaining strong performance across other languages.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Chinese Language Understanding", "weight": 1.0} -->

#Shots

<!-- chunk {"id": "body-0125", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

We conducted red-teaming evaluations on Kimi K2 compare with other open-source LLMs. The evaluation covered a range of attack scenarios---including harmful content, privacy content, and security content, as well as different attack strategies such as prompt injection and iterative jailbreak.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

We choose *Promptfoo*^77^7 to generate adversarial prompts and analyze the responses. By this way, we can evaluate model in a scalable ways.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

Model Selection We compare Kimi K2 with three other open-source LLMs: DeepSeek-V3, DeepSeek-R1, and Qwen3.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

Promptfoo Settings Table 5 lists plugins and strategies evaluated, with each plugin paired with all strategies to assess their performance.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

Graphic Content, Harassment and Bullying, Hate Speech, Insults, Profanity, Radicalization, Self Harm, Sexual Content, ToxicChat Chemical&Biological Weapons, Child Exploitation, Copyright Violations, Cybercrime, Illegal Activities, Illegal Drugs, Indiscriminate Weapons, Intellectual Property Violation, Non-Violent Crime, Violent Crime, Sex Crimes Competitor Endorsement, Unsupervised Contracts, Excessive Agency, Hallucination, Misinformation and Disinformation, Specialized Advice, Unsafe Practices, Imitation, Overreliance, Political Opinions, Religious Sensitivity Privacy Violation, PII in API/Database, Direct PII Exposure, PII in Session Data, PII via Social Engineering ASCII Smuggling, CyberSecEval, Harmbench, Debug Access, Divergent Repetition, DoNotAnswer, Malicious Code, Pliny, Prompt Extraction, Reasoning DoS, Tool Discovery Basic, Prompt Injection, Iterative Jailbreak, Crescendo Table 5: Enabled Plugins and Strategies Test Case Count Given the inherent non-determinism of large language model inference, single-pass outputs may exhibit variability. To account for this, we generated 3 attack prompts per plugin for each strategy.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

Prompt Language Settings We pre-tested the language compatibility for each plugin-strategy combination. Some plugins support both English and Chinese, while others only support English. For combinations that support both, we generated 3 prompts in each language, resulting in 6 prompts per combination.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Experiment Settings", "weight": 1.0} -->

Manual Review We incorporated human review into the evaluation process. To minimize subjectivity problem, we conducted multiple rounds of review and assigned the same reviewer to evaluate all cases within a given test set to ensure consistency and reduce variability in judgment.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Safety Evaluation Results", "weight": 1.0} -->

Table 6 presents the passing rates of different models under various plugin--strategy combinations.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Safety Evaluation Results", "weight": 1.0} -->

Across different attack strategies, the models exhibited varying trends. Under the strategy, passing rates generally approached or reached 100%, suggesting that encoding transformations had minimal impact on the models' basic robustness. In contrast, the Crescendo strategy led to a general drop in passing rates, indicating stronger adversarial effectiveness.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Safety Evaluation Results", "weight": 1.0} -->

In addition, complex attack strategies do not always outperform basic prompts. Some originally adversarial prompts may lose their intended meaning after multiple rounds of transformation, rendering the resulting model outputs less meaningful.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Safety Evaluation Results", "weight": 1.0} -->

Automated Red-teaming Limitations Due to the involvement of human review, the evaluation results inevitably contain a degree of subjectivity. Additionally, certain plugin types involve API misuse or external tool invocation, which are more suitable for evaluating agent models with tool-calling capabilities. In the context of base LLMs, such tests may have limited relevance.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Limitations", "weight": 1.5} -->

In our internal tests, we have identified some limitations in current Kimi K2 models. When dealing with hard reasoning tasks or unclear tool definition, the model may generate excessive tokens, sometimes leading to truncated outputs or incomplete tool calls. Additionally, performance may decline on certain tasks if tool use is unnecessarily enabled. When building complete software projects, the success rate of one-shot prompting is not as good as using K2 under an agentic coding framework. We are working to address these issues in future releases and looking forward to more feedbacks.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We introduced Kimi K2, a 1T-parameter open-weight MoE model built for agentic intelligence. Leveraging the token-efficient MuonClip optimizer and a 15.5T-token high-quality dataset, Kimi K2 achieves stable, scalable pre-training. Post-training combines large-scale synthetic tool-use data with a unified RL framework using both verifiable rewards and self-critic feedbacks. Kimi K2 sets new state-of-the-art on agentic and reasoning benchmarks, establishing itself as the most capable open-weight LLM to date.
