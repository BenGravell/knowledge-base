## Introduction

The development of Large Language Models (LLMs) is undergoing a profound paradigm shift towards Agentic Intelligence -- the capabilities for models to autonomously perceive, plan, reason, and act within complex and dynamic environments. This transition marks a departure from static imitation learning towards models that actively learn through interactions, acquire new skills beyond their training distribution, and adapt behavior through experiences \[(https://arxiv.org/html/2507.20534v2#bib.bib164 "Welcome to the era of experience")\]. It is believed that this approach allows an AI agent to go beyond the limitation of static human-generated data, and acquire superhuman capabilities through its own exploration and exploitation. Agentic intelligence is thus rapidly emerging as a defining capability for the next generation of foundation models, with wide-ranging implications across tool use, software development, and real-world autonomy.

Achieving agentic intelligence introduces challenges in both pre-training and post-training. Pre-training must endow models with broad general-purpose priors under constraints of limited high-quality data, elevating token efficiency---learning signal per token---as a critical scaling coefficient. Post-training must transform those priors into actionable behaviors, yet agentic capabilities such as multi-step reasoning, long-term planning, and tool use are rare in natural data and costly to scale. Scalable synthesis of structured, high-quality agentic trajectories, combined with general reinforcement learning (RL) techniques that incorporate preferences and self-critique, are essential to bridge this gap.

In this work, we introduce Kimi K2, a 1.04 trillion-parameter Mixture-of-Experts (MoE) LLM with 32 billion activated parameters, purposefully designed to address the core challenges and push the boundaries of agentic capability. Our contributions span both the pre-training and post-training frontiers:

We present MuonClip, a novel optimizer that integrates the token-efficient Muon algorithm with a stability-enhancing mechanism called QK-Clip. Using MuonClip, we successfully pre-trained Kimi K2 on 15.5 trillion tokens without a single loss spike.

We introduce a large-scale agentic data synthesis pipeline that systematically generates tool-use demonstrations via simulated and real-world environments. This system constructs diverse tools, agents, tasks, and trajectories to create high-fidelity, verifiably correct agentic interactions at scale.

We design a general reinforcement learning framework that combines verifiable rewards (RLVR) with a self-critique rubric reward mechanism. The model learns not only from externally defined tasks but also from evaluating its own outputs, extending alignment from static into open-ended domains.

Kimi K2 demonstrates strong performance across a broad spectrum of agentic and frontier benchmarks. It achieves scores of 66.1 on Tau2-bench, 76.5 on ACEBench (en), 65.8 on SWE-bench Verified, and 47.3 on SWE-bench Multilingual, outperforming most open- and closed-weight baselines under non-thinking evaluation settings, closing the gap with Claude 4 Opus and Sonnet. In coding, mathematics, and broader STEM domains, Kimi K2 achieves 53.7 on LiveCodeBench v6, 27.1 on OJBench, 49.5 on AIME 2025, and 75.1 on GPQA-Diamond, further highlighting its capabilities in general tasks. On the LMSYS Arena leaderboard ^44^4[https://lmarena.ai/leaderboard/text](https://lmarena.ai/leaderboard/text), Kimi K2 ranks as the top 1 open-source model and 5th overall based on over 3,000 user votes.

To spur further progress in Agentic Intelligence, we are open-sourcing our base and post-trained checkpoints, enabling the community to explore, refine, and deploy agentic intelligence at scale.

## Pre-training

The base model of Kimi K2 is a trillion-parameter mixture-of-experts (MoE) transformer \[(https://arxiv.org/html/2507.20534v2#bib.bib43 "Attention is all you need")\] model, pre-trained on 15.5 trillion high-quality tokens. Given the increasingly limited availability of high-quality human data, we posit that token efficiency is emerging as a critical coefficient in the scaling of large language models. To address this, we introduce a suite of pre-training techniques explicitly designed for maximizing token efficiency. Specifically, we employ the token-efficient Muon optimizer \[(https://arxiv.org/html/2507.20534v2#bib.bib159 "Muon: an optimizer for hidden layers in neural networks"), (https://arxiv.org/html/2507.20534v2#bib.bib158 "Muon is scalable for llm training")\] and mitigate its training instabilities through the introduction of QK-Clip. Additionally, we incorporate synthetic data generation to further squeeze the intelligence out of available high-quality tokens. The model architecture follows an ultra-sparse MoE with multi-head latent attention (MLA) similar to DeepSeek-V3 \[(https://arxiv.org/html/2507.20534v2#bib.bib84 "DeepSeek-v3 technical report")\], derived from empirical scaling law analysis. The underlying infrastructure is built to optimize both training efficiency and research efficiency.

### MuonClip: Stable Training with Weight Clipping

We train Kimi K2 using the token-efficient Muon optimizer \[(https://arxiv.org/html/2507.20534v2#bib.bib159 "Muon: an optimizer for hidden layers in neural networks")\], incorporating weight decay and consistent update RMS scaling \[(https://arxiv.org/html/2507.20534v2#bib.bib158 "Muon is scalable for llm training")\]. Experiments in our previous work Moonlight \[(https://arxiv.org/html/2507.20534v2#bib.bib158 "Muon is scalable for llm training")\] show that, under the same compute budget and model size --- and therefore the same amount of training data --- Muon substantially outperforms AdamW \[(https://arxiv.org/html/2507.20534v2#bib.bib161 "Adam: A method for stochastic optimization"), (https://arxiv.org/html/2507.20534v2#bib.bib160 "Decoupled weight decay regularization")\], making it an effective choice for improving token efficiency in large language model training.

### Training instability when scaling Muon

Despite its efficiency, scaling up Muon training reveals a challenge: training instability due to exploding attention logits, an issue that occurs more frequently with Muon but less with AdamW in our experiments. Existing mitigation strategies are insufficient. For instance, logit soft-cap \[(https://arxiv.org/html/2507.20534v2#bib.bib162 "Gemma 2: improving open language models at a practical size")\] directly clips the attention logits, but the dot products between queries and keys can still grow excessively before capping is applied. On the other hand, Query-Key Normalization (QK-Norm) \[(https://arxiv.org/html/2507.20534v2#bib.bib4 "Scaling vision transformers to 22 billion parameters"), \] is not applicable to multi-head latent attention (MLA), because its Key matrices are not fully materialized during inference.

### Taming Muon with QK-Clip

To address this issue, we propose a novel weight-clipping mechanism QK-Clip to explicitly constrain attention logits. QK-Clip works by rescaling the query and key projection weights post-update to bound the growth of attention logits.

Let the input representation of a transformer layer be $\mathbf{X}$. For each attention head $h$, its query, key, and value projections are computed as

where $\mathbf{W}_{q},\mathbf{W}_{k},\mathbf{W}_{v}$ are model parameters. The attention output is:

We define the max logit, a per-head scalar, as the maximum input to softmax in this batch $B$:

where $i,j$ are indices of different tokens in a training sample $\mathbf{X}$.

The core idea of QK-Clip is to rescale $\mathbf{W}_{k},\mathbf{W}_{q}$ whenever $S_{\max}^{h}$ exceeds a target threshold $\tau$. Importantly, this operation does not alter the forward/backward computation in the current step --- we merely use the max logit as a guiding signal to determine the strength to control the weight growth.

A naïve implementation clips all heads at the same time:

where $\gamma = {\min{(1,{\tau/S_{\max}})}}$ with $S_{\max} = {\max_{h}S_{\max}^{h}}$, and $\alpha$ is a balancing parameter typically set to $0.5$, applying equal scaling to queries and keys.

However, we observe that in practice, only a small subset of heads exhibit exploding logits. In order to minimize our intervention on model training, we determine a per-head scaling factor $\gamma_{h} = {\min{(1,{\tau/S_{\max}^{h}})}}$, and opt to apply per-head QK-Clip. Such clipping is straightforward for regular multi-head attention (MHA). For MLA, we apply clipping only on unshared attention head components:

$\text{q}^{C}$ and $\text{k}^{C}$ (head-specific components): each scaled by $\sqrt{\gamma_{h}}$

$\text{q}^{R}$ (head-specific rotary): scaled by $\gamma_{h}$,

$\text{k}^{R}$ (shared rotary): left untouched to avoid effect across heads.

1:for each training step t do
2: // 1. Muon optimizer step
3: for each weight W ∈ ℝn × m do
4: Mt = μ Mt − 1 + Gt ⊳ M0 = 0, Gt is the grad of Wt, μ is momentum
5: $\mathbf{O}_{t} = {{{{Newton} - {Schulz}}{(\mathbf{M}_{t})}} \cdot \sqrt{\max{(n,m)}} \cdot 0.2}$ ⊳ Match Adam RMS
6: Wt = Wt − 1 − η (Ot+λ Wt − 1) ⊳ learning rate η, weight decay λ
9: for each attention head h in every attention layer of the model do
10: Obtain Smaxh already computed during forward
13: $\mathbf{W}_{qc}^{h}\leftarrow{\mathbf{W}_{qc}^{h} \cdot \sqrt{\gamma}}$
14: $\mathbf{W}_{kc}^{h}\leftarrow{\mathbf{W}_{kc}^{h} \cdot \sqrt{\gamma}}$
Algorithm 1 MuonClip Optimizer

Figure 2: Left: During a mid-scale training run, attention logits rapidly exceed 1000, which could lead to potential numerical instabilities and even training divergence. Right: Maximum logits for Kimi K2 with MuonClip and τ = 100 over the entire training run. The max logits rapidly increase to the capped value of 100, and only decay to a stable range after approximately 30% of the training steps, demonstrating the effective regulation effect of QK-Clip.

### MuonClip: The New Optimizer

We integrate Muon with weight decay, consistent RMS matching, and QK-Clip into a single optimizer, which we refer to as MuonClip (see Algorithm (https://arxiv.org/html/2507.20534v2#alg1 "Algorithm 1 ‣ Taming Muon with QK-Clip ‣ 2.1 MuonClip: Stable Training with Weight Clipping ‣ 2 Pre-training ‣ Kimi K2: Open Agentic Intelligence")).

We demonstrate the effectiveness of MuonClip from several scaling experiments. First, we train a mid-scale 9B activated and 53B total parameters Mixture-of-Experts (MoE) model using the vanilla Muon. As shown in Figure (https://arxiv.org/html/2507.20534v2#S2.F2 "Figure 2 ‣ Taming Muon with QK-Clip ‣ 2.1 MuonClip: Stable Training with Weight Clipping ‣ 2 Pre-training ‣ Kimi K2: Open Agentic Intelligence") (Left), we observe that the maximum attention logits quickly exceed a magnitude of 1000, showing that attention logits explosion is already evident in Muon training to this scale. Max logits at this level usually result in instability during training, including significant loss spikes and occasional divergence.

Next, we demonstrate that QK-Clip does not degrade model performance and confirm that the MuonClip optimizer preserves the optimization characteristics of Muon without adversely affecting the loss trajectory. A detailed discussion of the experiment designs and findings is provided in the Appendix [D](https://arxiv.org/html/2507.20534v2#A4 "Appendix D QK-Clip Does Not Impair Model Quality ‣ Kimi K2: Open Agentic Intelligence").

Finally, we train Kimi K2, a large-scale MoE model, using MuonClip with $\tau = 100$ and monitor the maximum attention logits throughout the training run (Figure (https://arxiv.org/html/2507.20534v2#S2.F2 "Figure 2 ‣ Taming Muon with QK-Clip ‣ 2.1 MuonClip: Stable Training with Weight Clipping ‣ 2 Pre-training ‣ Kimi K2: Open Agentic Intelligence") (Right)). Initially, the logits are capped at 100 due to QK-Clip. Over the course of training, the maximum logits gradually decay to a typical operating range without requiring any adjustment to $\tau$. Importantly, the training loss remains smooth and stable, with no observable spikes, as shown in Figure (https://arxiv.org/html/2507.20534v2#S2.F3 "Figure 3 ‣ MuonClip: The New Optimizer ‣ 2.1 MuonClip: Stable Training with Weight Clipping ‣ 2 Pre-training ‣ Kimi K2: Open Agentic Intelligence"), validating that MuonClip provides robust and scalable control over attention dynamics in large-scale language model training.

Figure 3: Per-step training loss curve of Kimi K2, without smoothing or sub-sampling. It shows no spikes throughout the entire training process. Note that we omit the very beginning of training for clarity.

### Pre-training Data: Improving Token Utility with Rephrasing

Token efficiency in pre-training refers to how much performance improvement is achieved for each token consumed during training. Increasing token utility---the effective learning signal each token contributes---enhances the per-token impact on model updates, thereby directly improving token efficiency. This is particularly important when the supply of high-quality tokens is limited and must be maximally leveraged. A naive approach to increasing token utility is through repeated exposure to the same tokens, which can lead to overfitting and reduced generalization.

A key advancement in the pre-training data of Kimi K2 over Kimi K1.5 is the introduction of a synthetic data generation strategy to increase token utility. Specifically, a carefully designed rephrasing pipeline is employed to amplify the volume of high-quality tokens without inducing significant overfitting. In this report, we describe two domain-specialized rephrasing techniques---targeted respectively at the Knowledge and Mathematics domains---that enable this controlled data augmentation.

### Knowledge Data Rephrasing

Pre-training on natural, knowledge-intensive text presents a trade-off: a single epoch is insufficient for comprehensive knowledge absorption, while multi-epoch repetition yields diminishing returns and increases the risk of overfitting. To improve the token utility of high-quality knowledge tokens, we propose a synthetic rephrasing framework composed of the following key components:

Style- and perspective-diverse prompting: Inspired by WRAP \[(https://arxiv.org/html/2507.20534v2#bib.bib129 "Rephrasing the web: a recipe for compute and data-efficient language modeling")\], we apply a range of carefully engineered prompts to enhance linguistic diversity while maintaining factual integrity. These prompts guide a large language model to generate faithful rephrasings of the original texts in varied styles and from different perspectives.

Chunk-wise autoregressive generation: To preserve global coherence and avoid information loss in long documents, we adopt a chunk-based autoregressive rewriting strategy. Texts are divided into segments, rephrased individually, and then stitched back together to form complete passages. This method mitigates implicit output length limitations that typically exist with LLMs. An overview of this pipeline is presented in Figure (https://arxiv.org/html/2507.20534v2#S2.F4.1 "Figure 4 ‣ Knowledge Data Rephrasing ‣ 2.2 Pre-training Data: Improving Token Utility with Rephrasing ‣ 2 Pre-training ‣ Kimi K2: Open Agentic Intelligence").

Fidelity verification: To ensure consistency between original and rewritten content, we perform fidelity checks that compare the semantic alignment of each rephrased passage with its source. This serves as an initial quality control step prior to training.

We compare data rephrasing with multi-epoch repetition by testing their corresponding accuracy on SimpleQA. We experiment with an early checkpoint of K2 and evaluate three training strategies: repeating the original dataset for 10 epochs, rephrasing the data once and repeating it for 10 epochs, and rephrasing the data 10 times with a single training pass. As shown in Table (https://arxiv.org/html/2507.20534v2#S2.T1 "Table 1 ‣ Knowledge Data Rephrasing ‣ 2.2 Pre-training Data: Improving Token Utility with Rephrasing ‣ 2 Pre-training ‣ Kimi K2: Open Agentic Intelligence"), the accuracy consistently improves across these strategies, demonstrating the efficacy of our rephrasing-based augmentation. We extended this method to other large-scale knowledge corpora and observed similarly encouraging results, and each corpora is rephrased at most twice.

## Rephrasings
## Epochs

Table 1: SimpleQA Accuracy under three rephrasing-epoch configurations

Figure 4: Auto-regressive chunk-wise rephrasing pipeline for long input excerpts. The input is split into smaller chunks with preserved context, rewritten sequentially, and then concatenated into a full rewritten passage.

### Mathematics Data Rephrasing

To enhance mathematical reasoning capabilities, we rewrite high-quality mathematical documents into a "learning-note" style, following the methodology introduced in SwallowMath \[(https://arxiv.org/html/2507.20534v2#bib.bib130 "Rewriting pre-training data boosts llm performance in math and code")\]. In addition, we increased data diversity by translating high-quality mathematical materials from other languages into English.

Although initial experiments with rephrased subsets of our datasets show promising results, the use of synthetic data as a strategy for continued scaling remains an active area of investigation. Key challenges include generalizing the approach to diverse source domains without compromising factual accuracy, minimizing hallucinations and unintended toxicity, and ensuring scalability to large-scale datasets.

### Pre-training Data Overall

The Kimi K2 pre-training corpus comprises 15.5 trillion tokens of curated, high-quality data spanning four primary domains: Web Text, Code, Mathematics, and Knowledge. Most data processing pipelines follow the methodologies outlined in Kimi K1.5 \[(https://arxiv.org/html/2507.20534v2#bib.bib85 "Kimi k1. 5: scaling reinforcement learning with llms")\]. For each domain, we performed rigorous correctness and quality validation and designed targeted data experiments to ensure the curated dataset achieved both high diversity and effectiveness.

### Model Architecture

Kimi K2 is a 1.04 trillion-parameter Mixture-of-Experts (MoE) transformer model with 32 billion activated parameters. The architecture follows a similar design to DeepSeek-V3 \[(https://arxiv.org/html/2507.20534v2#bib.bib84 "DeepSeek-v3 technical report")\], employing Multi-head Latent Attention (MLA) \[(https://arxiv.org/html/2507.20534v2#bib.bib9 "Deepseek-v2: a strong, economical, and efficient mixture-of-experts language model")\] as the attention mechanism, with a model hidden dimension of 7168 and an MoE expert hidden dimension of 2048. Our scaling law analysis reveals that continued increases in sparsity yield substantial performance improvements, which motivated us to increase the number of experts to 384, compared to 256 in DeepSeek-V3. To reduce computational overhead during inference, we cut the number of attention heads to 64, as opposed to 128 in DeepSeek-V3. Table (https://arxiv.org/html/2507.20534v2#S2.T2 "Table 2 ‣ 2.3 Model Architecture ‣ 2 Pre-training ‣ Kimi K2: Open Agentic Intelligence") presents a detailed comparison of architectural parameters between Kimi K2 and DeepSeek-V3.

#Layers

Experts Active per Token

Number of Dense Layers

Table 2: Architectural comparison between Kimi K2 and DeepSeek-V3

### Sparsity Scaling Law

We develop a sparsity scaling law tailored for the Mixture-of-Experts (MoE) model family using Muon. Sparsity is defined as the ratio of the total number of experts to the number of activated experts. Through carefully controlled small-scale experiments, we observe that --- under a fixed number of activated parameters (i.e., constant FLOPs) --- increasing the total number of experts (i.e., increasing sparsity) consistently lowers both the training and validation loss, thereby enhancing overall model performance (Figure (https://arxiv.org/html/2507.20534v2#S2.F6 "Figure 6 ‣ Sparsity Scaling Law ‣ 2.3 Model Architecture ‣ 2 Pre-training ‣ Kimi K2: Open Agentic Intelligence")). Concretely, under the compute-optimal sparsity scaling law, achieving the same validation loss of 1.5, sparsity 48 reduces FLOPs by 1.69×, 1.39×, and 1.15× compared to sparsity levels 8, 16, and 32, respectively. Though increasing sparsity leads to better performance, this gain comes with increased infrastructure complexity. To balance model performance with cost, we adopt a sparsity of 48 for Kimi K2, activating 8 out of 384 experts per forward pass.

Figure 5: Sparsity Scaling Law. Increasing sparsity leads to improved model performance. We fixed the number of activated experts to 8 and the number of shared experts to 1, and varied the total number of experts, resulting in models with different sparsity levels.

Figure 6: Scaling curves for models with number of attention heads equals to number of layers and their counterparts with doubled attention heads. Doubling the number of attention heads leads to a reduction in validation loss of approximately 0.5% to 1.2%.

### Number of Attention Heads

DeepSeek-V3 \[(https://arxiv.org/html/2507.20534v2#bib.bib84 "DeepSeek-v3 technical report")\] sets the number of attention heads to roughly twice the number of model layers to better utilize memory bandwidth and enhance computational efficiency. However, as the context length increases, doubling the number of attention heads leads to significant inference overhead, reducing efficiency at longer sequence lengths. This becomes a major limitation in agentic applications, where efficient long context processing is essential. For example, with a sequence length of 128k, increasing the number of attention heads from 64 to 128, while keeping the total expert count fixed at 384, leads to an 83% increase in inference FLOPs. To evaluate the impact of this design, we conduct controlled experiments comparing configurations where the number of attention heads equals the number of layers against those with double number of heads, under varying training FLOPs. Under iso-token training conditions, we observe that doubling the attention heads yields only modest improvements in validation loss (ranging from 0.5% to 1.2%) across different compute budgets (Figure (https://arxiv.org/html/2507.20534v2#S2.F6 "Figure 6 ‣ Sparsity Scaling Law ‣ 2.3 Model Architecture ‣ 2 Pre-training ‣ Kimi K2: Open Agentic Intelligence")). Given that sparsity 48 already offers strong performance, the marginal gains from doubling attention heads do not justify the inference cost. Therefore we choose to 64 attention heads.

### Training Infrastructure

### Compute Cluster

Kimi K2 was trained on a cluster equipped with NVIDIA H800 GPUs. Each node in the H800 cluster contains 2 TB RAM and 8 GPUs connected by NVLink and NVSwitch within nodes. Across different nodes, ${\text{8} \times \text{400}}\text{Gbps}$ RoCE interconnects are utilized to facilitate communications.

### Parallelism for Model Scaling

Training of large language models often progresses under dynamic resource availability. Instead of optimizing one parallelism strategy that's only applicable under specific amount of resources, we pursue a flexible strategy that allows Kimi K2 to be trained on any number of nodes that is a multiple of 32. Our strategy leverages a combination of 16-way Pipeline Parallelism (PP) with virtual stages \[(https://arxiv.org/html/2507.20534v2#bib.bib134 "Gpipe: efficient training of giant neural networks using pipeline parallelism"), (https://arxiv.org/html/2507.20534v2#bib.bib135 "Efficient large-scale language model training on gpu clusters using megatron-lm"), (https://arxiv.org/html/2507.20534v2#bib.bib145 "Breadth-first pipeline parallelism"), (https://arxiv.org/html/2507.20534v2#bib.bib146 "Zero bubble pipeline parallelism"), (https://arxiv.org/html/2507.20534v2#bib.bib147 "Hanayo: harnessing wave-like pipeline parallelism for enhanced large model training efficiency"), (https://arxiv.org/html/2507.20534v2#bib.bib152 "Pipedream: fast and efficient pipeline parallel dnn training")\], 16-way Expert Parallelism (EP) \[(https://arxiv.org/html/2507.20534v2#bib.bib133 "Gshard: scaling giant models with conditional computation and automatic sharding")\], and ZeRO-1 Data Parallelism \[(https://arxiv.org/html/2507.20534v2#bib.bib148 "Zero: memory optimizations toward training trillion parameter models")\].

Under this setting, storing the model parameters in and their gradient accumulation buffer in requires approximately 6 TB of GPU memory, distributed over a model-parallel group of 256 GPUs. Placement of optimizer states depends on the training configurations. When the total number of training nodes is large, the optimizer states are distributed, reducing its per-device memory footprint to a negligible level. When the total number of training nodes is small (e.g., 32), we can offload some optimizer states to CPU.

This approach allows us to reuse an identical parallelism configuration for both small- and large-scale experiments, while letting each GPU hold approximately 30 GB of GPU memory for all states. The rest of the GPU memory are used for activations, as described in Sec. [2.4.3](https://arxiv.org/html/2507.20534v2#S2.SS4.SSS3 "2.4.3 Activation Reduction ‣ 2.4 Training Infrastructure ‣ 2 Pre-training ‣ Kimi K2: Open Agentic Intelligence"). Such a consistent design is important for research efficiency, as it simplifies the system and substantially accelerates experimental iteration.

### EP communication overlap with interleaved 1F1B

By increasing the number of warm-up micro-batches, we can overlap EP all-to-all communication with computation under the standard interleaved 1F1B schedule \[(https://arxiv.org/html/2507.20534v2#bib.bib152 "Pipedream: fast and efficient pipeline parallel dnn training"), (https://arxiv.org/html/2507.20534v2#bib.bib135 "Efficient large-scale language model training on gpu clusters using megatron-lm")\]. In comparison, DualPipe \[(https://arxiv.org/html/2507.20534v2#bib.bib84 "DeepSeek-v3 technical report")\] doubles the memory required for parameters and gradients, necessitating an increase in parallelism to compensate. Increasing PP introduces more bubbles, while increasing EP, as discussed below, incurs higher overhead. The additional costs are prohibitively high for training a large model with over 1 trillion parameters and thus we opted not to use DualPipe.

However, interleaved 1F1B splits the model into more stages, introducing non-trivial PP communication overhead. To mitigate this cost, we decouple the weight-gradient computation from each micro-batch's backward pass and execute it in parallel with the corresponding PP communication. Consequently, all PP communications can be effectively overlapped except for the warm-up phase.

### Smaller EP size

To ensure full computation-communication overlap during the 1F1B stage, the reduced attention computation time in K2 (which has 64 attention heads compared to 128 heads in DeepSeek-V3) necessitates minimizing the time of EP operations. This is achieved by adopting the smallest feasible EP parallelization strategy, specifically EP = 16. Utilizing a smaller EP group also relaxes expert-balance constraints, allowing for near-optimal speed to be achieved without further tuning.

### Activation Reduction

After reserving space for parameters, gradient buffers, and optimizer states, the remaining GPU memory on each device is insufficient to hold the full MoE activations. To ensure the activation memory fits within the constraints, especially for the initial pipeline stages that accumulate the largest activations during the 1F1B warm-up phase, the following techniques are employed.

### Selective recomputation

Recomputation is applied to inexpensive, high-footprint stages, including LayerNorm, SwiGLU, and MLA up-projections \[(https://arxiv.org/html/2507.20534v2#bib.bib84 "DeepSeek-v3 technical report")\]. Additionally, MoE down-projections are recomputed during training to further reduce activation memory. While optional, this recomputation maintains adequate GPU memory, preventing crashes caused by expert imbalance in early training stages.

### FP8 storage for insensitive activations

Inputs of MoE up-projections and SwiGLU are compressed to FP8-E4M3 in 1$\times$ 128 tiles with scales. Small-scale experiments show no measurable loss increase. Due to potential risks of performance degradation that we observed during preliminary study, we do not apply FP8 in computation.

Figure 7: Computation, communication and offloading overlapped in different PP phases.

### Activation CPU offload

All remaining activations are offloaded to CPU RAM. A copy engine is responsible for streaming the offload and onload, overlapping with both computation and communication kernels. During the 1F1B phase, we offload the forward activations of the previous micro-batch while prefetching the backward activations of the next. The warm-up and cool-down phases are handled similarly and the overall pattern is shown in Figure (https://arxiv.org/html/2507.20534v2#S2.F7 "Figure 7 ‣ FP8 storage for insensitive activations ‣ 2.4.3 Activation Reduction ‣ 2.4 Training Infrastructure ‣ 2 Pre-training ‣ Kimi K2: Open Agentic Intelligence"). Although offloading may slightly affect EP traffic due to PCIe traffic congestion, our tests show that EP communication remains fully overlapped.

### Training recipe

We pre-trained the model with a 4,096-token context window using the MuonClip optimizer (Algorithm (https://arxiv.org/html/2507.20534v2#alg1 "Algorithm 1 ‣ Taming Muon with QK-Clip ‣ 2.1 MuonClip: Stable Training with Weight Clipping ‣ 2 Pre-training ‣ Kimi K2: Open Agentic Intelligence")) and the WSD learning rate schedule \[(https://arxiv.org/html/2507.20534v2#bib.bib175 "Minicpm: unveiling the potential of small language models with scalable training strategies")\], processing a total of 15.5T tokens. The first 10T tokens were trained with a constant learning rate of 2e-4 after a 500-step warm-up, followed by 5.5T tokens with a cosine decay from 2e-4 to 2e-5. Weight decay was set to 0.1 throughout, and the global batch size was held at 67M tokens. The overall training curve is shown in Figure (https://arxiv.org/html/2507.20534v2#S2.F3 "Figure 3 ‣ MuonClip: The New Optimizer ‣ 2.1 MuonClip: Stable Training with Weight Clipping ‣ 2 Pre-training ‣ Kimi K2: Open Agentic Intelligence").

Towards the end of pre-training, we conducted an annealing phase followed by a long-context activation stage. The batch size was kept constant at 67M tokens, while the learning rate was decayed from 2e-5 to 7e-6. In this phase, the model was trained on 400 billion tokens with a 4k sequence length, followed by an additional 60 billion tokens with a 32k sequence length. To extend the context window to 128k, we employed the YaRN method \[(https://arxiv.org/html/2507.20534v2#bib.bib21 "Yarn: efficient context window extension of large language models")\].

## Post-Training

### Supervised Fine-Tuning

We employ the Muon optimizer \[(https://arxiv.org/html/2507.20534v2#bib.bib159 "Muon: an optimizer for hidden layers in neural networks")\] in our post-training and recommend its use for fine-tuning with K2. This follows from the conclusion of our previous work \[(https://arxiv.org/html/2507.20534v2#bib.bib158 "Muon is scalable for llm training")\] that a Muon-pre-trained checkpoint produces the best performance with Muon fine-tuning.

We construct a large-scale instruction-tuning dataset spanning diverse domains, guided by two core principles: maximizing prompt diversity and ensuring high response quality. To this end, we develop a suite of data generation pipelines tailored to different task domains, each utilizing a combination of human annotation, prompt engineering, and verification processes. We adopt K1.5 \[(https://arxiv.org/html/2507.20534v2#bib.bib85 "Kimi k1. 5: scaling reinforcement learning with llms")\] and other in-house domain-specialized expert models to generate candidate responses for various tasks, followed by LLMs or human-based judges to perform automated quality evaluation and filtering. For agentic data, we create a data synthesis pipeline to teach models tool-use capabilities through multi-step, interactive reasoning.

### Large-Scale Agentic Data Synthesis for Tool Use Learning

A critical capability of modern LLM agents is their ability to autonomously use unfamiliar tools, interact with external environments, and iteratively refine their actions through reasoning, execution, and error correction. Agentic tool use capability is essential for solving complex, multi-step tasks that require dynamic interaction with real-world systems. Recent benchmarks such as ACEBench \[(https://arxiv.org/html/2507.20534v2#bib.bib114 "ACEBench: who wins the match point in tool learning?")\] and $\tau$-bench \[(https://arxiv.org/html/2507.20534v2#bib.bib116 "Tau-bench: a benchmark for tool-agent-user interaction in real-world domains")\] have highlighted the importance of comprehensive tool-use evaluation, while frameworks like ToolLLM \[(https://arxiv.org/html/2507.20534v2#bib.bib121 "Toolllm: facilitating large language models to master 16000+ real-world apis")\] and ACEBench \[(https://arxiv.org/html/2507.20534v2#bib.bib114 "ACEBench: who wins the match point in tool learning?")\] have demonstrated the potential of teaching models to use thousands of tools effectively.

However, training such capabilities at scale presents a significant challenge: while real-world environments provide rich and authentic interaction signals, they are often difficult to construct at scale due to cost, complexity, privacy and accessibility constraints. Recent work on synthetic data generation (AgentInstruct \[(https://arxiv.org/html/2507.20534v2#bib.bib117 "Agentinstruct: toward generative teaching with agentic flows")\]; Self-Instruct \[(https://arxiv.org/html/2507.20534v2#bib.bib118 "Self-instruct: aligning language models with self-generated instructions")\]; StableToolBench \[(https://arxiv.org/html/2507.20534v2#bib.bib119 "StableToolBench: towards stable large-scale benchmarking on tool learning of large language models")\]; ZeroSearch \[(https://arxiv.org/html/2507.20534v2#bib.bib6 "ZeroSearch: incentivize the search capability of llms without searching")\]) has shown promising results in creating large-scale data without relying on real-world interactions. Building on these advances and inspired by ACEBench \[(https://arxiv.org/html/2507.20534v2#bib.bib114 "ACEBench: who wins the match point in tool learning?")\]'s comprehensive data synthesis framework, we developed a pipeline that simulates real-world tool-use scenarios at scale, enabling the generation of tens of thousands of diverse and high-quality training examples.

(a) Synthesizing tool specs, agents and tasks

(b) Generating agent trajectories

Figure 8: Data synthesis pipeline for tool use. (a) Tool specs are from both real-world tools and LLMs; agents and tasks are the generated from the tool repo. (b) Multi-agent pipeline to generate and filter trajectories with tool calling.

(a) t-SNE visualization of real MCP tools, colored by their original source categories

(b) t-SNE visualization of synthetic tools, colored by pre-defined domain categories

Figure 9: t-SNE visualizations of tool embeddings. (a) Real-world MCP tools exhibit natural clustering based on their original source categories. (b) Synthetic tools are organized into pre-defined domain categories, providing systematic coverage of the tool space. Together, they ensure comprehensive representation across different tool functionalities.

There are three stages in our data synthesis pipeline, depicted in Fig. (https://arxiv.org/html/2507.20534v2#S3.F8 "Figure 8 ‣ 3.1.1 Large-Scale Agentic Data Synthesis for Tool Use Learning ‣ 3.1 Supervised Fine-Tuning ‣ 3 Post-Training ‣ Kimi K2: Open Agentic Intelligence").

Tool spec generation: we first construct a large repository of tool specs from both real-world tools and LLM-synthetic tools;

Agent and task generation: for each tool-set sampled from the tool repository, we generate an agent to use the toolset and some corresponding tasks;

Trajectory generation: for each agent and task, we generate trajectories where the agent finishes the task by invoking tools.

### Domain Evolution and Tool Generation

We construct a comprehensive tool repository through two complementary approaches. First, we directly fetch 3000+ real MCP (Model Context Protocol) tools from GitHub repositories, leveraging existing high-quality tool specs. Second, we systematically evolve \[(https://arxiv.org/html/2507.20534v2#bib.bib7 "WizardLM: empowering large pre-trained language models to follow complex instructions")\] synthetic tools through a hierarchical domain generation process: we begin with key categories (e.g., financial trading, software applications, robot control), then evolve multiple specific application domains within each category. Specialized tools are then synthesized for each domain, with clear interfaces, descriptions, and operational semantics. This evolution process produces over 20,000 synthetic tools. Figure (https://arxiv.org/html/2507.20534v2#S3.F9 "Figure 9 ‣ 3.1.1 Large-Scale Agentic Data Synthesis for Tool Use Learning ‣ 3.1 Supervised Fine-Tuning ‣ 3 Post-Training ‣ Kimi K2: Open Agentic Intelligence") visualizes the diversity of our tool collection through t-SNE embeddings, demonstrating that both MCP and synthetic tools cover complementary regions of the tool space.

### Agent Diversification

We generate thousands of distinct agents by synthesizing various system prompts and equipping them with different combinations of tools from our repository. This creates a diverse population of agents with varied capabilities, areas of expertise, and behavioral patterns, ensuring a broad coverage of potential use cases.

### Rubric-Based Task Generation

For each agent configuration, we generate tasks that range from simple to complex operations. Each task is paired with an explicit rubric that specifies success criteria, expected tool-use patterns, and evaluation checkpoints. This rubric-based approach ensures a consistent and objective evaluation of agent performance.

### Multi-turn Trajectory Generation

We simulate realistic tool-use scenarios through several components:

User Simulation: LLM-generated user personas with distinct communication styles and preferences engage in multi-turn dialogues with agents, creating naturalistic interaction patterns.

Tool Execution Environment: A sophisticated tool simulator (functionally equivalent to a world model) executes tool calls and provides realistic feedback. The simulator maintains and updates state after each tool execution, enabling complex multi-step interactions with persistent effects. It introduces controlled stochasticity to produce varied outcomes including successes, partial failures, and edge cases.

### Quality Evaluation and Filtering

An LLM-based judge evaluates each trajectory against the task rubrics. Only trajectories that meet the success criteria are retained for training, ensuring high-quality data while allowing natural variation in task-completion strategies.

### Hybrid Approach with Real Execution Environments

While simulation provides scalability, we acknowledge the inherent limitation of simulation fidelity. To address this, we complement our simulated environments with real execution sandboxes for scenarios where authenticity is crucial, particularly in coding and software engineering tasks. These real sandboxes execute actual code, interact with genuine development environments, and provide ground-truth feedback through objective metrics such as test suite pass rates. This combination ensures that our models learn from both the diversity of simulated scenarios and the authenticity of real executions, significantly strengthening practical agent capabilities.

By leveraging this hybrid pipeline that combines scalable simulation with targeted real-world execution, we generate diverse, high-quality tool-use demonstrations that balance coverage and authenticity. The scale and automation of our synthetic data generation, coupled with the grounding provided by real execution environments, effectively implements large-scale rejection sampling \[(https://arxiv.org/html/2507.20534v2#bib.bib176 "Large language models can self-improve"), (https://arxiv.org/html/2507.20534v2#bib.bib177 "Star: bootstrapping reasoning with reasoning")\] through our quality filtering process. This high-quality synthetic data, when used for supervised fine-tuning, has demonstrated significant improvements in the model's tool-use capabilities across a wide range of real-world applications.

### Reinforcement Learning

Reinforcement learning (RL) is believed to have better token efficiency and generalization than SFT. Based on the work of K1.5 \[(https://arxiv.org/html/2507.20534v2#bib.bib85 "Kimi k1. 5: scaling reinforcement learning with llms")\], we continue to scale RL in both task diversity and training FLOPs in K2. To support this, we develop a Gym-like extensible framework that facilitates RL across a wide range of scenarios. We extend the framework with a large number of tasks with verifiable rewards. For tasks that rely on subjective preferences, such as creative writing and open-ended question answering, we introduce a self-critic reward in which the model performs pairwise comparisons to judge its own outputs. This approach allows tasks from various domains to all benefit from the RL paradigm.

### Verifiable Rewards Gym

### Math, STEM and Logical Tasks

For math, stem and logical reasoning domains, our RL data preparation follows two key principles, *diverse coverage* and *moderate difficulty*.

*Diverse Coverage.* For math and stem tasks, we collect high-quality QA pairs using a combination of expert annotations, internal QA extraction pipelines, and open datasets \[(https://arxiv.org/html/2507.20534v2#bib.bib178 "Numinamath: the largest public dataset in ai4maths with 860k pairs of competition math problems and solutions"), (https://arxiv.org/html/2507.20534v2#bib.bib179 "Aimo-2 winning solution: building state-of-the-art mathematical reasoning models with openmathreasoning dataset")\]. During the collection process, we leverage a tagging system to deliberately increase coverage of under-covered domains. For logical tasks, our dataset comprises a variety of formats, including structured data tasks (e.g., multi-hop tabular reasoning, cross-table aggregation) and logic puzzles (e.g., the 24-game, Sudoku, riddles, cryptarithms, and Morse-code decoding).

*Moderate Difficulty.* The RL prompt-set should be neither too easy nor too hard, both of which may produce little signal and reduce learning efficiency. We assess the difficulty of each problem using the SFT model's pass@k accuracy and select only problems with moderate difficulty.

### Complex Instruction Following

Effective instruction following requires not only understanding explicit constraints but also navigating implicit requirements, handling edge cases, and maintaining consistency over extended dialogues. We address these challenges through a hybrid verification framework that combines automated verification with adversarial detection, coupled with a scalable curriculum generation pipeline. Our approach employs a dual-path system to ensure both precision and robustness:

Hybrid Rule Verification. We implement two verification mechanisms: deterministic evaluation via code interpreters for instructions with verifiable outputs (e.g., length, style constraints), and LLM-as-judge evaluation for instructions requiring nuanced understanding of constraints. To address potential adversarial behaviors where models might claim instruction fulfillment without actual compliance, we incorporate an additional hack-check layer that specifically detects such deceptive claims.

Multi-Source Instruction Generation. To construct our training data, we employ three distinct generation strategies to ensure comprehensive coverage: expert-crafted complex conditional prompts and rubrics developed by our data team agentic instruction augmentation inspired by AutoIF \[(https://arxiv.org/html/2507.20534v2#bib.bib13 "Self-play with execution feedback: improving instruction-following capabilities of large language models")\], and a fine-tuned model specialized for generating additional instructions that probe specific failure modes or edge cases. This multipronged approach ensures both breadth and depth in instruction coverage.

### Faithfulness

Faithfulness is essential for an agentic model operating in scenarios such as multi-turn tool use, self-generated reasoning chains, and open-environment interactions. Inspired by the evaluation framework from FACTS Grounding \[(https://arxiv.org/html/2507.20534v2#bib.bib124 "The facts grounding leaderboard: benchmarking llms’ ability to ground responses to long-form input")\], we train a sentence-level faithfulness judge model to perform automated verification. The judge is effective in detecting sentences that make a factual claim without supporting evidence in context. It serves as a reward model to enhance overall faithfulness performance.

### Coding & Software Engineering

To enhance our capability in tackling competition-level programming problems, we gather problems and their judges from both open-source datasets \[(https://arxiv.org/html/2507.20534v2#bib.bib170 "OpenCoder: the open cookbook for top-tier code large language models"), (https://arxiv.org/html/2507.20534v2#bib.bib169 "KodCode: a diverse, challenging, and verifiable synthetic dataset for coding")\] and synthetic sources. To ensure the diversity of the synthetic data and the correctness of reward signals, we incorporate high-quality human-written unit tests retrieved from pre-training data.

For software engineering tasks, we collect a vast amount of pull requests and issues from GitHub to build software development environment that consists of user prompts/issues and executable unit tests. This environment was built on a robust sandbox infrastructure, powered by Kubernetes for scalability and security. It supports over 10,000 concurrent sandbox instances with stable performance, making it ideal for both competitive coding and software engineering tasks.

### Safety

Our work to enhance the safety begins with a human-curated set of seed prompts, manually crafted to encompass prevalent risk categories such as violence, fraud, and discrimination.

To simulate sophisticated jailbreak attempts (e.g., role-playing, literary narratives, and academic discourse), we employ an automated prompt evolution pipeline with three key components:

Attack Model: Iteratively generates adversarial prompts designed to elicit unsafe responses from the target LLM.

Target Model: Produces responses to these prompts, simulating potential vulnerabilities.

Judge Model: Evaluates the interaction to determine if the adversarial prompt successfully bypasses safety mechanisms.

Each interaction is assessed using a task-specific rubric, enabling the judge model to provide a binary success/failure label.

### Beyond Verification: Self-Critique Rubric Reward

To extend model alignment beyond tasks with verifiable reward, we introduce a framework for general reinforcement learning from self-critic feedbacks. This approach is designed to align LLMs with nuanced human preferences, including helpfulness, creativity, depth of reasoning, factuality, and safety, by extending the capabilities learned from verifiable scenarios to a broader range of subjective tasks. The framework operates using a Self-Critique Rubric Reward mechanism, where the model evaluates its own outputs to generate preference signals. To bootstrap K2 as a competent judge, we curated a mixture of open-source and in-house preference datasets and initialize its critic capability in the SFT stage.

### Self-Critiqued Policy Optimization

In the first core process of the learning loop, the K2 actor generates responses for general prompts that cover a wide range of use cases. The K2 critic then ranks all results by performing pairwise evaluations against a combination of rubrics, which incorporates both core rubrics (Appendix. [F.1](https://arxiv.org/html/2507.20534v2#A6.SS1 "F.1 Core Rubrics ‣ Appendix F K2 Critic Rubrics for General RL ‣ Kimi K2: Open Agentic Intelligence")), which represent the fundamental values of our AI assistant that Kimi cherish, prescriptive rubrics (Appendix. [F.2](https://arxiv.org/html/2507.20534v2#A6.SS2 "F.2 Prescriptive Rubrics ‣ Appendix F K2 Critic Rubrics for General RL ‣ Kimi K2: Open Agentic Intelligence")) that aim to eliminate reward hacking, and human-annotated rubrics crafted by our data team for specific instructional contexts. Although certain rubrics can be designated as mandatory, K2 retains the flexibility to weigh them against its internal priors. This capacity enables a dynamic and continuous alignment with its evolving on-policy behavior, ensuring that the model's responses remain coherent with its core identity while adapting to specific instructions.

### Closed-Loop Critic Refinement and Alignment

During RL training, the critic model is refined using verifiable signals. On-policy rollouts generated from verifiable-reward prompts are used to continuously update the critic, a crucial step that distills objective performance signals from RLVR directly into its evaluation model. This transfer learning process grounds its more subjective judgments in verifiable data, allowing the performance gains from verifiable tasks to enhance the critic's judgment on complex tasks that lack explicit reward signals. This closed-loop process ensures that the critic continuously recalibrates its evaluation standards in lockstep with the policy's evolution. By grounding subjective evaluation in verifiable data, the framework enables robust and scalable alignment with complex, non-verifiable human objectives.

Consequently, this holistic alignment yields comprehensive performance improvements across a wide spectrum of domains, including user intent understanding, creative writing, complex reasoning, and nuanced language comprehension.

### RL Algorithm

We adopt the policy optimization algorithm introduced in K1.5 \[(https://arxiv.org/html/2507.20534v2#bib.bib85 "Kimi k1. 5: scaling reinforcement learning with llms")\] as the foundation for K2. For each problem $x$, we sample $K$ responses $\{ y_{1},\ldots,y_{k}\}$ from the previous policy $\pi_{old}$, and optimize the model $\pi_{\theta}$ with respect to the following objective:

where ${\overline{r}{(x)}} = {\frac{1}{k}{\sum_{i = 1}^{k}{r{(x,y_{i})}}}}$ is the mean rewards of the sampled responses, $\tau > 0$ is a regularization parameter that promotes stable learning. As in SFT, we employ the Muon optimizer \[(https://arxiv.org/html/2507.20534v2#bib.bib159 "Muon: an optimizer for hidden layers in neural networks")\] to minimize this objective. As we scale RL training to encompass a broader range of tasks in K2, a primary challenge is achieving consistent performance improvements across all domains. To address this, we introduce several additions to the RL algorithm.

### Budget Control

It has been widely observed that RL often results in a substantial increase in the length of model-generated responses \[(https://arxiv.org/html/2507.20534v2#bib.bib85 "Kimi k1. 5: scaling reinforcement learning with llms"), (https://arxiv.org/html/2507.20534v2#bib.bib131 "Deepseek-r1: incentivizing reasoning capability in llms via reinforcement learning")\]. While longer responses can enable the model to utilize additional test-time compute for improved performance on complex reasoning tasks, the benefits often do not justify its inference cost in non-reasoning domains. To encourage the model to properly distribute inference budget, we enforce a per-sample *maximum token budget* throughout RL training, where the budget is determined based on the type of task. Responses that exceed this token budget are truncated and assigned a penalty, which incentivizes the model to generate solutions within the specified limit. Empirically, this approach significantly enhances the model's token efficiency, encouraging concise yet effective solutions across all domains.

### PTX Loss

To prevent the potential forgetting of valuable, high-quality data during joint RL training, we curate a dataset comprising hand-selected, high-quality samples and integrate it into the RL objective through an auxiliary PTX loss \[(https://arxiv.org/html/2507.20534v2#bib.bib68 "Training language models to follow instructions with human feedback")\]. This strategy not only leverages the advantages of high-quality data, but also mitigates the risk of overfitting to the limited set of tasks explicitly present in the training regime. This augmentation substantially improves the model's generalization across a broader range of domains.

### Temperature Decay

For tasks such as creative writing and complex reasoning, we find that promoting exploration via a high sampling temperature during the initial stages of training is crucial. A high temperature allow the model to generate diverse and innovative responses, thereby facilitating the discovery of effective strategies and reducing the risk of premature convergence to suboptimal solutions. However, retaining a high temperature in the later stages of training or during evaluation can be detrimental, as it introduces excessive randomness and compromises the reliability and consistency of the model's outputs. To address this, we employ a temperature decay schedule, to shift from exploration to exploitation throughout the training. This strategy ensures that the model leverages exploration when it is most beneficial, while ultimately converge on stable and high-quality outputs.

### RL Infrastructure

### Colocated Architecture

Similar to K1.5 \[(https://arxiv.org/html/2507.20534v2#bib.bib85 "Kimi k1. 5: scaling reinforcement learning with llms")\], we adopt a hybrid colocated architecture for our synchronized RL training, where the training and inference engines live on the same workers. When one engine is actively working, the other engine releases or offloads its GPU resources to accommodate. In each iteration of RL training, a centralized controller first calls the inference engine to generate new data for training. It then notifies the training engine to train on the new data, and send updated parameters to the inference engine for the next iteration.

Each engine is heavily optimized for throughput. In addition, as the model scales to the size of K2, the latency of engine switching and failure recovery becomes significant. We present our system design considerations in these aspects.

### Efficient Engine Switching

During rollout, the parameters of the training engine are offloaded to DRAM. Bringing up the training engine is therefore a simple step of H2D transmission. However, bringing up the inference engine is a bigger challenge, as it must obtain updated parameters from the training engine with a different sharding paradigm.

Figure 10: Parameter update utilizing a checkpoint engine

Given the scale of K2 and the vast number of devices involved, using a network file system for resharding and broadcasting parameters is impractical. The aggregate bandwidth required to keep overhead low reaches several petabytes per second. To address this challenge, we developed a distributed checkpoint engine co-located on training nodes to manage parameter states. To perform a parameter update, each checkpoint engine worker obtains a local copy of parameters from the training engine, then broadcasts the full parameter set across all checkpoint engine workers. Subsequently, the inference engine retrieves only the parameter shard it requires from the checkpoint engine. This process is illustrated in Figure (https://arxiv.org/html/2507.20534v2#S3.F10 "Figure 10 ‣ 3.3.2 Efficient Engine Switching ‣ 3.3 RL Infrastructure ‣ 3 Post-Training ‣ Kimi K2: Open Agentic Intelligence"). To enable this for a 1T model, updates are performed parameter-by-parameter in a pipelined manner, minimizing memory footprint (see Appendix [G](https://arxiv.org/html/2507.20534v2#A7 "Appendix G Engine Switching Pipeline for RL Training ‣ Kimi K2: Open Agentic Intelligence")).

We opt to broadcast the full parameter set across the entire cluster, regardless of the specific sharding schemes on each inference worker. While this transfers several times more data than a theoretically optimal approach, it offers a simpler system design that is less intrusive to the training and inference engines. We chose to trade off this minor overhead to fully decouple the training engine and the inference engine, significantly simplifying maintenance and testing.

Notably, this approach outperforms the transfer-what-you-need method due to reduced synchronization overhead and higher network bandwidth utilization. Our system can complete a full parameter update for Kimi K2 with less than 30 seconds, a negligible duration for a typical RL training iteration. The source code for the checkpoint engine is available on Github^55^5[https://github.com/MoonshotAI/checkpoint-engine](https://github.com/MoonshotAI/checkpoint-engine).

### Efficient System Startup

As large-scale training is prone to system failure, optimizing the startup time is crucial for models as large as Kimi K2.

To start the training engine, we let each training worker selectively read part or none of the parameters from disk, and broadcast necessary parameters to its peers. The design goal is to ensure all workers collectively read the checkpoint only once, minimizing expensive disk IO.

As the inference engines are independent replicas, we would like to avoid introducing extra synchronization barriers between them. Therefore, we opt to reuse checkpoint engine for startup: we let checkpoint engine collectively read the checkpoint from disk, similar to how the training engine starts. Then it updates the state of the uninitialized inference engine, using the approach introduced in the previous section. By leveraging the dedicated checkpoint engine, the system also becomes robust to single-point failures, because an inference replica can restart without communicating with other replicas.

### Agentic Rollout

Our RL infrastructure supports the training of long-horizon, multi-turn agentic tasks. During rollout, these tasks present distinct challenges, such as complex environmental interactions and prolonged rollout durations. Here we introduce a few optimizations to alleviate these issues.

Due to the diversity of environments, certain interactions may be blocked on waiting for environment feedback (e.g., a virtual machine or a code interpreter), leaving the GPUs idle. We employ two strategies to maximize GPU utilization: (i) we deploy heavy environments as dedicated services that can scale up more easily; (ii) we employ a large number of concurrent rollouts to amortize the latency induced by certain expensive interactions.

Another challenge in agentic rollout is that individual rollout trajectories can be extremely long. To prevent long-tail trajectories from blocking the entire rollout process, we employ the partial rollout \[(https://arxiv.org/html/2507.20534v2#bib.bib85 "Kimi k1. 5: scaling reinforcement learning with llms")\] technique. This strategy allows long-tail unfinished tasks to be paused, and resumed in the next RL iteration.

To improve research efficiency, we also design a unified interface inspired by the OpenAI Gym framework \[(https://arxiv.org/html/2507.20534v2#bib.bib174 "OpenAI gym")\] to streamline the integration of new environments. We hope to scale our RL infrastructure to more diverse interactive environments in the future.

## Evaluations

This section begins with the post-training evaluation of Kimi-K2-Instruct, followed by a brief overview of the capabilities of Kimi-K2-Base. We conclude with a comprehensive safety evaluation.

### Post-training Evaluations

### Evaluation Settings

### Benchmarks

We assess Kimi-K2-Instruct across different areas. For coding, we adopt LiveCodeBench v6 \[(https://arxiv.org/html/2507.20534v2#bib.bib98 "Livecodebench: holistic and contamination free evaluation of large language models for code")\], OJBench \[(https://arxiv.org/html/2507.20534v2#bib.bib153 "OJBench: a competition level code benchmark for large language models")\], MultiPL-E \[(https://arxiv.org/html/2507.20534v2#bib.bib22 "MultiPL-e: a scalable and polyglot approach to benchmarking neural code generation")\], SWE-bench Verified \[(https://arxiv.org/html/2507.20534v2#bib.bib154 "SWE-bench: can language models resolve real-world github issues?"), (https://arxiv.org/html/2507.20534v2#bib.bib155 "SWE-smith: scaling data for software engineering agents")\], TerminalBench \[(https://arxiv.org/html/2507.20534v2#bib.bib156 "Terminal-bench: a benchmark for ai agents in terminal environments")\], Multi-SWE-bench \[(https://arxiv.org/html/2507.20534v2#bib.bib173 "Multi-swe-bench: a multilingual benchmark for issue resolving")\], SWE-Lancer \[(https://arxiv.org/html/2507.20534v2#bib.bib106 "SWE-lancer: can frontier llms earn $1 million from real-world freelance software engineering?")\], PaperBench \[(https://arxiv.org/html/2507.20534v2#bib.bib172 "PaperBench: evaluating ai’s ability to replicate ai research")\], and Aider-Polyglot \[(https://arxiv.org/html/2507.20534v2#bib.bib151 "Aider llm leaderboards")\]. For tool use tasks, we evaluate performance on $\tau^{2}$-Bench \[(https://arxiv.org/html/2507.20534v2#bib.bib157 "τ2-Bench: evaluating conversational agents in a dual-control environment")\] and AceBench \[(https://arxiv.org/html/2507.20534v2#bib.bib114 "ACEBench: who wins the match point in tool learning?")\], which emphasize multi-turn tool-calling capabilities. In reasoning, we include a wide range of mathematical, science and logical tasks: AIME 2024/2025, MATH-500, HMMT 2025, CNMO 2024, PolyMath-en, ZebraLogic \[(https://arxiv.org/html/2507.20534v2#bib.bib163 "ZebraLogic: on the scaling limits of llms for logical reasoning")\], AutoLogi \[(https://arxiv.org/html/2507.20534v2#bib.bib165 "AutoLogi: automated generation of logic puzzles for evaluating reasoning abilities of large language models")\], GPQA-Diamond \[(https://arxiv.org/html/2507.20534v2#bib.bib108 "Gpqa: a graduate-level google-proof q&a benchmark")\], SuperGPQA \[(https://arxiv.org/html/2507.20534v2#bib.bib103 "Supergpqa: scaling llm evaluation across 285 graduate disciplines")\], and Humanity's Last Exam (Text-Only) \[(https://arxiv.org/html/2507.20534v2#bib.bib166 "Humanity’s last exam")\]. We benchmark the long-context capabilities on: MRCR^66^6[https://huggingface.co/datasets/openai/mrcr](https://huggingface.co/datasets/openai/mrcr) for long-context retrieval, and DROP \[(https://arxiv.org/html/2507.20534v2#bib.bib3 "DROP: A reading comprehension benchmark requiring discrete reasoning over paragraphs")\], FRAMES \[(https://arxiv.org/html/2507.20534v2#bib.bib12 "Fact, fetch, and reason: a unified evaluation of retrieval-augmented generation")\] and LongBench v2 \[(https://arxiv.org/html/2507.20534v2#bib.bib11 "LongBench v2: towards deeper understanding and reasoning on realistic long-context multitasks")\] for long-context reasoning. For factuality, we evaluate FACTS Grounding \[(https://arxiv.org/html/2507.20534v2#bib.bib124 "The facts grounding leaderboard: benchmarking llms’ ability to ground responses to long-form input")\], the Vectara Hallucination Leaderboard \[(https://arxiv.org/html/2507.20534v2#bib.bib125 "Hallucination evaluation model (revision 7437011)")\], and FaithJudge \[(https://arxiv.org/html/2507.20534v2#bib.bib127 "Benchmarking llm faithfulness in rag with evolving leaderboards")\]. Finally, general capabilities are assessed using MMLU \[(https://arxiv.org/html/2507.20534v2#bib.bib86 "Measuring massive multitask language understanding")\], MMLU-Redux \[(https://arxiv.org/html/2507.20534v2#bib.bib102 "Are we done with mmlu?")\], MMLU-Pro \[(https://arxiv.org/html/2507.20534v2#bib.bib87 "MMLU-pro: a more robust and challenging multi-task language understanding benchmark")\], IFEval \[(https://arxiv.org/html/2507.20534v2#bib.bib45 "Instruction-following evaluation for large language models")\], Multi-Challenge \[(https://arxiv.org/html/2507.20534v2#bib.bib167 "MultiChallenge: a realistic multi-turn conversation evaluation benchmark challenging to frontier llms")\], SimpleQA \[(https://arxiv.org/html/2507.20534v2#bib.bib104 "Measuring short-form factuality in large language models")\], and LiveBench \[(https://arxiv.org/html/2507.20534v2#bib.bib168 "LiveBench: a challenging, contamination-free LLM benchmark")\].

### Baselines

We benchmark against both open-source and proprietary frontier models, ensuring every candidate is evaluated under its non-thinking configuration to eliminate additional gains from test-time compute. Open-source baselines: DeepSeek-V3-0324 and Qwen3-235B-A22B, with the latter run in the vendor-recommended no-thinking regime. Proprietary baselines: Claude Sonnet 4, Claude Opus 4, GPT-4.1, and Gemini 2.5 Flash Preview. Each invoked in its respective non-thinking mode via official APIs under unified temperature and top-p settings.

Evaluation Configurations All runs query models in their non-thinking mode. Output token length is capped at 8192 tokens everywhere except SWE-bench Verified (Agentless), which is raised to 16384. For benchmarks with high per-question variance, we adopt repeated sampling $k$ times and average the results to obtain stable scores, denoted as Avg@k. For long-context tasks, we set the context window size to 128K tokens during evaluation, truncating any input that exceeds this limit to fit within the window. SWE-bench Verified is evaluated in two modes: Agentless Coding via Single Patch without Test (Acc) and Agentic Coding via bash/editor tools under both Single Attempt (Acc) and Multiple Attempts (Acc) using best-of-N selection with an internal verifier; SWE-bench Multilingual is tested only in the single-attempt agentic setting. Some data points have been omitted due to prohibitively expensive evaluation costs.

SWE-bench Verified Agentless-Single-Patch (Pass@1)

SWE-bench Verified Agentic-Single-Attempt (Pass@1)

SWE-bench Verified Agentic-Multi-Attempt (Pass@1)

SWE-bench Multilingual (Pass@1)

Paper Bench Code-Dev (Acc.)

Terminal Bench In-House (Acc.)

Terminal Bench Terminus (Acc.)

Tool Use Tasks

Tau2 retail (Avg@4)

Tau2 airline (Avg@4)

Tau2 telecom (Avg@4)

Math &amp; STEM Tasks

Humanity’s Last Exam (Acc.)

IFEval (Prompt Strict)

Arena Hard v2.0 Hard Prompt (Win rate)

Arena Hard v2.0 Creative Writing (Win rate)

FACTS Grounding (Adjusted)

Table 3: Performance comparison of Kimi-K2-Instruct against leading open-source and proprietary models across diverse tasks. Bold denotes the global SOTA; underlined bold indicates the best open-source result. Data points marked with * are taken directly from the model’s technical report or blog.

### Evaluation Results

A comprehensive evaluation results of Kimi-K2-Instruct is shown in Table (https://arxiv.org/html/2507.20534v2#S4.T3 "Table 3 ‣ Baselines ‣ 4.1.1 Evaluation Settings ‣ 4.1 Post-training Evaluations ‣ 4 Evaluations ‣ Kimi K2: Open Agentic Intelligence"), with detailed explanation provided in the Appendix [C](https://arxiv.org/html/2507.20534v2#A3 "Appendix C Evaluation Details ‣ Kimi K2: Open Agentic Intelligence"). Below, we highlight key results across four core domains:

### Agentic and Competitive Coding

Kimi-K2-Instruct demonstrates state-of-the-art open-source performance on real-world SWE tasks. It outperforms most baselines on SWE-bench Verified (65.8%, 71.6% with multiple attemps), SWE-bench Multilingual (47.3%), and SWE-lancer (39.1%), significantly closing the gap with Claude 4 Opus and Sonnet. On competitive coding benchmarks (e.g., LiveCodeBench v6 53.7%, OJBench 27.1%), it also leads among all models, highlighting its practical coding proficiency across difficulty levels.

### Agentic Tool Use

On multi-turn tool-use benchmarks, Kimi-K2-Instruct sets a new standard. It achieves 66.1 Pass@1 on $\tau^{2}$-Bench and 76.5 on ACEBench, substantially outperforming all baselines. These results affirm its strength in grounded, controlled, and agent-driven tool orchestration across domains.

### General Capabilities

Kimi-K2-Instruct exhibits strong, balanced performance across general knowledge, math, instruction following, and long-context tasks. It surpasses open-source peers on SimpleQA (31.0%), MMLU (89.5%) and MMLU-Redux (92.7%), and leads all models on instruction benchmarks (IFEval: 89.8%, Multi-Challenge: 54.1%). In math and STEM, it achieves top-tier scores, and remains competitive on long-context factuality and retrieval (DROP: 93.5%, MRCR: 55.0%). These results position Kimi-K2-Instruct as a well-rounded and capable generalist across both short- and long-context settings.

### Open-Ended Evaluation

On the LMSYS Arena leaderboard, Kimi-K2-Instruct ranks as the top-1 open-source model and 5th overall based on over 3,000 user votes. This real-world preference signal---across diverse, blind prompts---underscores Kimi-K2's strengths in generating high-quality responses on open-ended tasks.

### Pre-training Evaluations

### Evaluation Settings

### Benchmarks

We evaluate Kimi-K2-Base across diverse capability areas. For general capabilities, we assess on MMLU \[(https://arxiv.org/html/2507.20534v2#bib.bib86 "Measuring massive multitask language understanding")\], MMLU-Pro \[(https://arxiv.org/html/2507.20534v2#bib.bib87 "MMLU-pro: a more robust and challenging multi-task language understanding benchmark")\], MMLU-Redux \[(https://arxiv.org/html/2507.20534v2#bib.bib102 "Are we done with mmlu?")\], BBH \[(https://arxiv.org/html/2507.20534v2#bib.bib88 "Challenging big-bench tasks and whether chain-of-thought can solve them")\], TriviaQA \[(https://arxiv.org/html/2507.20534v2#bib.bib89 "TriviaQA: a large scale distantly supervised challenge dataset for reading comprehension")\], SuperGPQA \[(https://arxiv.org/html/2507.20534v2#bib.bib103 "Supergpqa: scaling llm evaluation across 285 graduate disciplines")\], SimpleQA \[(https://arxiv.org/html/2507.20534v2#bib.bib104 "Measuring short-form factuality in large language models")\], HellaSwag \[(https://arxiv.org/html/2507.20534v2#bib.bib105 "Hellaswag: can a machine really finish your sentence?")\], AGIEval \[(https://arxiv.org/html/2507.20534v2#bib.bib107 "Agieval: a human-centric benchmark for evaluating foundation models")\], GPQA-Diamond \[(https://arxiv.org/html/2507.20534v2#bib.bib108 "Gpqa: a graduate-level google-proof q&a benchmark")\], ARC-Challenge \[(https://arxiv.org/html/2507.20534v2#bib.bib109 "Think you have solved question answering? try arc, the ai2 reasoning challenge")\], and WinoGrande \[(https://arxiv.org/html/2507.20534v2#bib.bib110 "Winogrande: an adversarial winograd schema challenge at scale")\]. For coding capabilities, we employ EvalPlus \[(https://arxiv.org/html/2507.20534v2#bib.bib97 "Is your code generated by chatgpt really correct? rigorous evaluation of large language models for code generation")\] (averaging HumanEval \[(https://arxiv.org/html/2507.20534v2#bib.bib90 "Evaluating large language models trained on code")\], MBPP \[(https://arxiv.org/html/2507.20534v2#bib.bib91 "Program synthesis with large language models")\], HumanEval+, and MBPP+), LiveCodeBench v6 \[(https://arxiv.org/html/2507.20534v2#bib.bib98 "Livecodebench: holistic and contamination free evaluation of large language models for code")\], and CRUXEval \[(https://arxiv.org/html/2507.20534v2#bib.bib99 "Cruxeval: a benchmark for code reasoning, understanding and execution")\]. For mathematical reasoning, we utilize GSM8K \[(https://arxiv.org/html/2507.20534v2#bib.bib95 "Training verifiers to solve math word problems")\], GSM8K-Platinum \[(https://arxiv.org/html/2507.20534v2#bib.bib100 "Do large language model benchmarks test reliability?")\], MATH \[(https://arxiv.org/html/2507.20534v2#bib.bib94 "Measuring mathematical problem solving with the math dataset")\], and CMATH \[(https://arxiv.org/html/2507.20534v2#bib.bib96 "CMATH: can your language model pass chinese elementary school math test?")\]. For Chinese language capabilities, we evaluate on C-Eval \[(https://arxiv.org/html/2507.20534v2#bib.bib93 "C-eval: a multi-level multi-discipline chinese evaluation suite for foundation models")\], CMMLU \[(https://arxiv.org/html/2507.20534v2#bib.bib92 "CMMLU: measuring massive multitask language understanding in chinese")\], and CSimpleQA \[\].

### Baselines

We benchmark against leading open-source foundation models: DeepSeek-V3-Base \[(https://arxiv.org/html/2507.20534v2#bib.bib84 "DeepSeek-v3 technical report")\], Qwen2.5-72B-Base \[(https://arxiv.org/html/2507.20534v2#bib.bib111 "Qwen2.5 technical report")\] (Note that Qwen3-235B-A22B-Base is not open-sourced, and the largest open-sourced base model in the Qwen series is Qwen2.5-72B-Base), and Llama 4-Maverick \[(https://arxiv.org/html/2507.20534v2#bib.bib113 "The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation — ai.meta.com")\] (Llama 4-Behemoth is also not open-sourced). All models are evaluated under identical configurations to ensure fair comparison.

### Evaluation Configurations

We employ perplexity-based evaluation for MMLU, MMLU-Redux, GPQA-Diamond, HellaSwag, ARC-Challenge, C-Eval, and CMMLU. Generation-based evaluation is used for MMLU-Pro, SuperGPQA, TriviaQA, BBH, CSimpleQA, MATH, CMATH, GSM8K, GSM8K-Platinum, CRUXEval, LiveCodeBench, and EvalPlus. To mitigate the high variance inherent to GPQA-Diamond, we report the mean score across eight independent runs. All evaluations are conducted using our internal framework derived from LM-Harness-Evaluation \[(https://arxiv.org/html/2507.20534v2#bib.bib112 "Lessons from the trenches on reproducible evaluation of language models")\], ensuring consistent settings across all models.

### Evaluation Results

Table (https://arxiv.org/html/2507.20534v2#S4.T4 "Table 4 ‣ Chinese Language Understanding ‣ 4.2.2 Evaluation Results ‣ 4.2 Pre-training Evaluations ‣ 4 Evaluations ‣ Kimi K2: Open Agentic Intelligence") presents a comprehensive comparison of Kimi-K2-Base against leading open-source foundation models across diverse evaluation benchmarks. The results demonstrate that Kimi-K2-Base achieves state-of-the-art performance across the majority of evaluated tasks, establishing it as a leading foundation model in the open-source landscape.

### General Language Understanding

Kimi-K2-Base achieves state-of-the-art performance on 10 out of 12 English language benchmarks. Notable results include MMLU (87.79%), MMLU-Pro (69.17%), MMLU-Redux (90.17%), SuperGPQA (44.67%), and SimpleQA (35.25%), significantly outperforming all baselines.

### Coding Capabilities

On coding benchmarks, Kimi-K2-Base sets new standards with leading performance across all metrics. It achieves 74.00% on CRUXEval-I-cot, 83.50% on CRUXEval-O-cot, 26.29% on LiveCodeBench v6, and 80.33% on EvalPlus, demonstrating superior code generation and comprehension abilities, particularly in scenarios requiring step-by-step reasoning.

### Mathematical Reasoning

Kimi-K2-Base exhibits exceptional mathematical capabilities, leading on three out of four benchmarks: MATH (70.22%), GSM8K (92.12%), and GSM8K-Platinum (94.21%). It maintains competitive performance on CMATH (90.26%), narrowly behind DeepSeek-V3-Base (90.53%). These results highlight the model's robust mathematical problem-solving abilities across varying difficulty levels.

### Chinese Language Understanding

The model demonstrates superior multilingual capabilities, achieving state-of-the-art results across all Chinese language benchmarks: C-Eval (92.50%), CMMLU (90.90%), and CSimpleQA (77.57%). These results establish Kimi-K2-Base as a leading model for Chinese language understanding while maintaining strong performance across other languages.

#Shots

## Activated Params

## Total Params

Table 4: Performance comparison of Kimi-K2-Base against leading open-source models across diverse tasks.

### Safety Evaluation

### Experiment Settings

We conducted red-teaming evaluations on Kimi K2 compare with other open-source LLMs. The evaluation covered a range of attack scenarios---including harmful content, privacy content, and security content, as well as different attack strategies such as prompt injection and iterative jailbreak.

We choose *Promptfoo*^77^7[https://github.com/promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) to generate adversarial prompts and analyze the responses. By this way, we can evaluate model in a scalable ways.

Model Selection We compare Kimi K2 with three other open-source LLMs: DeepSeek-V3, DeepSeek-R1, and Qwen3.

Promptfoo Settings Table (https://arxiv.org/html/2507.20534v2#S4.T5 "Table 5 ‣ 4.3.1 Experiment Settings ‣ 4.3 Safety Evaluation ‣ 4 Evaluations ‣ Kimi K2: Open Agentic Intelligence") lists plugins and strategies evaluated, with each plugin paired with all strategies to assess their performance.

Graphic Content, Harassment and Bullying, Hate Speech, Insults, Profanity, Radicalization, Self Harm, Sexual Content, ToxicChat

Chemical&amp;Biological Weapons, Child Exploitation, Copyright Violations, Cybercrime, Illegal Activities, Illegal Drugs, Indiscriminate Weapons, Intellectual Property Violation, Non-Violent Crime, Violent Crime, Sex Crimes

Competitor Endorsement, Unsupervised Contracts, Excessive Agency, Hallucination, Misinformation and Disinformation, Specialized Advice, Unsafe Practices, Imitation, Overreliance, Political Opinions, Religious Sensitivity

Privacy Violation, PII in API/Database, Direct PII Exposure, PII in Session Data, PII via Social Engineering

ASCII Smuggling, CyberSecEval, Harmbench, Debug Access, Divergent Repetition, DoNotAnswer, Malicious Code, Pliny, Prompt Extraction, Reasoning DoS, Tool Discovery

Basic, Prompt Injection, Iterative Jailbreak, Crescendo

Table 5: Enabled Plugins and Strategies

Test Case Count Given the inherent non-determinism of large language model inference, single-pass outputs may exhibit variability. To account for this, we generated 3 attack prompts per plugin for each strategy.

Prompt Language Settings We pre-tested the language compatibility for each plugin-strategy combination. Some plugins support both English and Chinese, while others only support English. For combinations that support both, we generated 3 prompts in each language, resulting in 6 prompts per combination.

Manual Review We incorporated human review into the evaluation process. To minimize subjectivity problem, we conducted multiple rounds of review and assigned the same reviewer to evaluate all cases within a given test set to ensure consistency and reduce variability in judgment.

### Safety Evaluation Results

Table (https://arxiv.org/html/2507.20534v2#S4.T6 "Table 6 ‣ 4.3.2 Safety Evaluation Results ‣ 4.3 Safety Evaluation ‣ 4 Evaluations ‣ Kimi K2: Open Agentic Intelligence") presents the passing rates of different models under various plugin--strategy combinations.

Table 6: Safety Evaluation Results

Without targeted optimization for specific evaluation scenarios, the passing rate of some complex cases (e.g., Harmful--Iterative Jailbreak) was relatively higher compared to other models.

Across different attack strategies, the models exhibited varying trends. Under the strategy, passing rates generally approached or reached 100%, suggesting that encoding transformations had minimal impact on the models' basic robustness. In contrast, the Crescendo strategy led to a general drop in passing rates, indicating stronger adversarial effectiveness.

In addition, complex attack strategies do not always outperform basic prompts. Some originally adversarial prompts may lose their intended meaning after multiple rounds of transformation, rendering the resulting model outputs less meaningful.

Automated Red-teaming Limitations Due to the involvement of human review, the evaluation results inevitably contain a degree of subjectivity. Additionally, certain plugin types involve API misuse or external tool invocation, which are more suitable for evaluating agent models with tool-calling capabilities. In the context of base LLMs, such tests may have limited relevance.

## Limitations

In our internal tests, we have identified some limitations in current Kimi K2 models. When dealing with hard reasoning tasks or unclear tool definition, the model may generate excessive tokens, sometimes leading to truncated outputs or incomplete tool calls. Additionally, performance may decline on certain tasks if tool use is unnecessarily enabled. When building complete software projects, the success rate of one-shot prompting is not as good as using K2 under an agentic coding framework. We are working to address these issues in future releases and looking forward to more feedbacks.

## Conclusions

We introduced Kimi K2, a 1T-parameter open-weight MoE model built for agentic intelligence. Leveraging the token-efficient MuonClip optimizer and a 15.5T-token high-quality dataset, Kimi K2 achieves stable, scalable pre-training. Post-training combines large-scale synthetic tool-use data with a unified RL framework using both verifiable rewards and self-critic feedbacks. Kimi K2 sets new state-of-the-art on agentic and reasoning benchmarks, establishing itself as the most capable open-weight LLM to date.
