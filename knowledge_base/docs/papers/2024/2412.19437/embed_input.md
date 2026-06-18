<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DeepSeek-V3 Technical Report

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present DeepSeek-V3, a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. To achieve efficient inference and cost-effective training, DeepSeek-V3 adopts Multi-head Latent Attention (MLA) and DeepSeekMoE architectures, which were thoroughly validated in DeepSeek-V2. Furthermore, DeepSeek-V3 pioneers an auxiliary-loss-free strategy for load balancing and sets a multi-token prediction training objective for stronger performance. We pre-train DeepSeek-V3 on 14.8 trillion diverse and high-quality tokens, followed by Supervised Fine-Tuning and Reinforcement Learning stages to fully harness its capabilities. Comprehensive evaluations reveal that DeepSeek-V3 outperforms other open-source models and achieves performance comparable to leading closed-source models. Despite its excellent performance, DeepSeek-V3 requires only 2.788M H800 GPU hours for its full training. In addition, its training process is remarkably stable. Throughout the entire training process, we did not experience any irrecoverable loss spikes or perform any rollbacks.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The model checkpoints are available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, Large Language Models (LLMs) have been undergoing rapid iteration and evolution, progressively diminishing the gap towards Artificial General Intelligence (AGI). Beyond closed-source models, open-source models, including DeepSeek series, LLaMA series, Qwen series, and Mistral series (Jiang et al. Mistral, ), are also making significant strides, endeavoring to close the gap with their closed-source counterparts. To further push the boundaries of open-source model capabilities, we scale up our models and introduce DeepSeek-V3, a large Mixture-of-Experts (MoE) model with 671B parameters, of which 37B are activated for each token.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

With a forward-looking perspective, we consistently strive for strong model performance and economical costs. Therefore, in terms of architecture, DeepSeek-V3 still adopts Multi-head Latent Attention (MLA) for efficient inference and DeepSeekMoE for cost-effective training. These two architectures have been validated in DeepSeek-V2, demonstrating their capability to maintain robust model performance while achieving efficient training and inference. Beyond the basic architecture, we implement two additional strategies to further enhance the model capabilities. Firstly, DeepSeek-V3 pioneers an auxiliary-loss-free strategy for load balancing, with the aim of minimizing the adverse impact on model performance that arises from the effort to encourage load balancing. Secondly, DeepSeek-V3 employs a multi-token prediction training objective, which we have observed to enhance the overall performance on evaluation benchmarks.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to achieve efficient training, we support the FP8 mixed precision training and implement comprehensive optimizations for the training framework. Low-precision training has emerged as a promising solution for efficient training, its evolution being closely tied to advancements in hardware capabilities. In this work, we introduce an FP8 mixed precision training framework and, for the first time, validate its effectiveness on an extremely large-scale model. Through the support for FP8 computation and storage, we achieve both accelerated training and reduced GPU memory usage. As for the training framework, we design the DualPipe algorithm for efficient pipeline parallelism, which has fewer pipeline bubbles and hides most of the communication during training through computation-communication overlap. This overlap ensures that, as the model further scales up, as long as we maintain a constant computation-to-communication ratio, we can still employ fine-grained experts across nodes while achieving a near-zero all-to-all communication overhead. In addition, we also develop efficient cross-node all-to-all communication kernels to fully utilize InfiniBand (IB) and NVLink bandwidths.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, we meticulously optimize the memory footprint, making it possible to train DeepSeek-V3 without using costly tensor parallelism. Combining these efforts, we achieve high training efficiency.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

During pre-training, we train DeepSeek-V3 on 14.8T high-quality and diverse tokens. The pre-training process is remarkably stable. Throughout the entire training process, we did not encounter any irrecoverable loss spikes or have to roll back. Next, we conduct a two-stage context length extension for DeepSeek-V3. In the first stage, the maximum context length is extended to 32K, and in the second stage, it is further extended to 128K. Following this, we conduct post-training, including Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) on the base model of DeepSeek-V3, to align it with human preferences and further unlock its potential. During the post-training stage, we distill the reasoning capability from the DeepSeek-R1 series of models, and meanwhile carefully maintain the balance between model accuracy and generation length.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate DeepSeek-V3 on a comprehensive array of benchmarks. Despite its economical training costs, comprehensive evaluations reveal that DeepSeek-V3-Base has emerged as the strongest open-source base model currently available, especially in code and math. Its chat version also outperforms other open-source models and achieves performance comparable to leading closed-source models, including GPT-4o and Claude-3.5-Sonnet, on a series of standard and open-ended benchmarks.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Lastly, we emphasize again the economical training costs of DeepSeek-V3, summarized in Table, achieved through our optimized co-design of algorithms, frameworks, and hardware. During the pre-training stage, training DeepSeek-V3 on each trillion tokens requires only 180K H800 GPU hours, i.e., 3.7 days on our cluster with 2048 H800 GPUs. Consequently, our pre-training stage is completed in less than two months and costs 2664K GPU hours. Combined with 119K GPU hours for the context length extension and 5K GPU hours for post-training, DeepSeek-V3 costs only 2.788M GPU hours for its full training. Assuming the rental price of the H800 GPU is \$2 per GPU hour, our total training costs amount to only \$5.576M. Note that the aforementioned costs include only the official training of DeepSeek-V3, excluding the costs associated with prior research and ablation experiments on architectures, algorithms, or data.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Architecture: Innovative Load Balancing Strategy and Training Objective

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

On top of the efficient architecture of DeepSeek-V2, we pioneer an auxiliary-loss-free strategy for load balancing, which minimizes the performance degradation that arises from encouraging load balancing.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We investigate a Multi-Token Prediction (MTP) objective and prove it beneficial to model performance. It can also be used for speculative decoding for inference acceleration.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Pre-Training: Towards Ultimate Training Efficiency

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We design an FP8 mixed precision training framework and, for the first time, validate the feasibility and effectiveness of FP8 training on an extremely large-scale model.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Through the co-design of algorithms, frameworks, and hardware, we overcome the communication bottleneck in cross-node MoE training, achieving near-full computation-communication overlap. This significantly enhances our training efficiency and reduces the training costs, enabling us to further scale up the model size without additional overhead.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

At an economical cost of only 2.664M H800 GPU hours, we complete the pre-training of DeepSeek-V3 on 14.8T tokens, producing the currently strongest open-source base model. The subsequent training stages after pre-training require only 0.1M GPU hours.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

Post-Training: Knowledge Distillation from DeepSeek-R1

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce an innovative methodology to distill reasoning capabilities from the long-Chain-of-Thought (CoT) model, specifically from one of the DeepSeek R1 series models, into standard LLMs, particularly DeepSeek-V3. Our pipeline elegantly incorporates the verification and reflection patterns of R1 into DeepSeek-V3 and notably improves its reasoning performance. Meanwhile, we also maintain control over the output style and length of DeepSeek-V3.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

Knowledge: On educational benchmarks such as MMLU, MMLU-Pro, and GPQA, DeepSeek-V3 outperforms all other open-source models, achieving 88.5 on MMLU, 75.9 on MMLU-Pro, and 59.1 on GPQA. Its performance is comparable to leading closed-source models like GPT-4o and Claude-Sonnet-3.5, narrowing the gap between open-source and closed-source models in this domain. For factuality benchmarks, DeepSeek-V3 demonstrates superior performance among open-source models on both SimpleQA and Chinese SimpleQA. While it trails behind GPT-4o and Claude-Sonnet-3.5 in English factual knowledge (SimpleQA), it surpasses these models in Chinese factual knowledge (Chinese SimpleQA), highlighting its strength in Chinese factual knowledge.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

Code, Math, and Reasoning: DeepSeek-V3 achieves state-of-the-art performance on math-related benchmarks among all non-long-CoT open-source and closed-source models. Notably, it even outperforms o1-preview on specific benchmarks, such as MATH-500, demonstrating its robust mathematical reasoning capabilities. On coding-related tasks, DeepSeek-V3 emerges as the top-performing model for coding competition benchmarks, such as LiveCodeBench, solidifying its position as the leading model in this domain. For engineering-related tasks, while DeepSeek-V3 performs slightly below Claude-Sonnet-3.5, it still outpaces all other models by a significant margin, demonstrating its competitiveness across diverse technical benchmarks.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the remainder of this paper, we first present a detailed exposition of our DeepSeek-V3 model architecture. Subsequently, we introduce our infrastructures, encompassing our compute clusters, the training framework, the support for FP8 training, the inference deployment strategy, and our suggestions on future hardware design. Next, we describe our pre-training process, including the construction of training data, hyper-parameter settings, long-context extension techniques, the associated evaluations, as well as some discussions. Thereafter, we discuss our efforts on post-training, which include Supervised Fine-Tuning (SFT), Reinforcement Learning (RL), the corresponding evaluations, and discussions. Lastly, we conclude this work, discuss existing limitations of DeepSeek-V3, and propose potential directions for future research.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Architecture", "weight": 1.0} -->

We first introduce the basic architecture of DeepSeek-V3, featured by Multi-head Latent Attention (MLA) for efficient inference and DeepSeekMoE for economical training. Then, we present a Multi-Token Prediction (MTP) training objective, which we have observed to enhance the overall performance on evaluation benchmarks. For other minor details not explicitly mentioned, DeepSeek-V3 adheres to the settings of DeepSeek-V2.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Basic Architecture", "weight": 1.0} -->

The basic architecture of DeepSeek-V3 is still within the Transformer framework. For efficient inference and economical training, DeepSeek-V3 also adopts MLA and DeepSeekMoE, which have been thoroughly validated by DeepSeek-V2. Compared with DeepSeek-V2, an exception is that we additionally introduce an auxiliary-loss-free load balancing strategy for DeepSeekMoE to mitigate the performance degradation induced by the effort to ensure load balance. Figure illustrates the basic architecture of DeepSeek-V3, and we will briefly review the details of MLA and DeepSeekMoE in this section.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Multi-Head Latent Attention", "weight": 1.0} -->

For attention, DeepSeek-V3 adopts the MLA architecture. Let $d$ denote the embedding dimension, $n_{h}$ denote the number of attention heads, $d_{h}$ denote the dimension per head, and $\mathbf{h}_{t} \in {\mathbb{R}}^{d}$ denote the attention input for the $t$-th token at a given attention layer.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Multi-Head Latent Attention", "weight": 1.0} -->

that applies RoPE matrices; and $\lbrack \cdot; \cdot \rbrack$ denotes concatenation.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Multi-Head Latent Attention", "weight": 1.0} -->

Note that for MLA, only the blue-boxed vectors (i.e., $\mathbf{c}_{t}^{KV}$ and $\mathbf{k}_{t}^{R}$) need to be cached during generation, which results in significantly reduced KV cache while maintaining performance comparable to standard Multi-Head Attention (MHA).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Basic Architecture of DeepSeekMoE", "weight": 1.0} -->

For Feed-Forward Networks (FFNs), DeepSeek-V3 employs the DeepSeekMoE architecture. Compared with traditional MoE architectures like GShard, DeepSeekMoE uses finer-grained experts and isolates some experts as shared ones.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Basic Architecture of DeepSeekMoE", "weight": 1.0} -->

where $N_{s}$ and $N_{r}$ denote the numbers of shared experts and routed experts, respectively; ${FFN}_{i}^{(s)}{( \cdot )}$ and ${FFN}_{i}^{(r)}{( \cdot )}$ denote the $i$-th shared expert and the $i$-th routed expert, respectively; $K_{r}$ denotes the number of activated routed experts; $g_{i,t}$ is the gating value for the $i$-th expert; $s_{i,t}$ is the token-to-expert affinity; $\mathbf{e}_{i}$ is the centroid vector of the $i$-th routed expert; and ${Topk}{( \cdot,K)}$ denotes the set comprising $K$ highest scores among the affinity scores calculated for the $t$-th token and all routed experts.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Basic Architecture of DeepSeekMoE", "weight": 1.0} -->

Slightly different from DeepSeek-V2, DeepSeek-V3 uses the sigmoid function to compute the affinity scores, and applies a normalization among all selected affinity scores to produce the gating values.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Auxiliary-Loss-Free Load Balancing", "weight": 1.0} -->

For MoE models, an unbalanced expert load will lead to routing collapse and diminish computational efficiency in scenarios with expert parallelism. Conventional solutions usually rely on the auxiliary loss (Fedus et al. Lepikhin et al., ) to avoid unbalanced load. However, too large an auxiliary loss will impair the model performance. To achieve a better trade-off between load balance and model performance, we pioneer an auxiliary-loss-free load balancing strategy to ensure load balance.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Auxiliary-Loss-Free Load Balancing", "weight": 1.0} -->

Note that the bias term is only used for routing. The gating value, which will be multiplied with the FFN output, is still derived from the original affinity score $s_{i,t}$. During training, we keep monitoring the expert load on the whole batch of each training step. At the end of each step, we will decrease the bias term by $\gamma$ if its corresponding expert is overloaded, and increase it by $\gamma$ if its corresponding expert is underloaded, where $\gamma$ is a hyper-parameter called bias update speed. Through the dynamic adjustment, DeepSeek-V3 keeps balanced expert load during training, and achieves better performance than models that encourage load balance through pure auxiliary losses.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Complementary Sequence-Wise Auxiliary Loss", "weight": 1.0} -->

where the balance factor $\alpha$ is a hyper-parameter, which will be assigned an extremely small value for DeepSeek-V3; $\mathbb{1}{( \cdot )}$ denotes the indicator function; and $T$ denotes the number of tokens in a sequence. The sequence-wise balance loss encourages the expert load on each sequence to be balanced.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Node-Limited Routing", "weight": 1.0} -->

Like the device-limited routing used by DeepSeek-V2, DeepSeek-V3 also uses a restricted routing mechanism to limit communication costs during training. In short, we ensure that each token will be sent to at most $M$ nodes, which are selected according to the sum of the highest $\frac{K_{r}}{M}$ affinity scores of the experts distributed on each node. Under this constraint, our MoE training framework can nearly achieve full computation-communication overlap.

<!-- chunk {"id": "body-0035", "role": "body", "section": "No Token-Dropping", "weight": 1.0} -->

Due to the effective load balancing strategy, DeepSeek-V3 keeps a good load balance during its full training. Therefore, DeepSeek-V3 does not drop any tokens during training. In addition, we also implement specific deployment strategies to ensure inference load balance, so DeepSeek-V3 also does not drop tokens during inference.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Multi-Token Prediction", "weight": 1.0} -->

Inspired by Gloeckle et al., we investigate and set a Multi-Token Prediction (MTP) objective for DeepSeek-V3, which extends the prediction scope to multiple future tokens at each position. On the one hand, an MTP objective densifies the training signals and may improve data efficiency. On the other hand, MTP may enable the model to pre-plan its representations for better prediction of future tokens. Figure illustrates our implementation of MTP. Different from Gloeckle et al., which parallelly predicts $D$ additional tokens using independent output heads, we sequentially predict additional tokens and keep the complete causal chain at each prediction depth. We introduce the details of our MTP implementation in this section.

<!-- chunk {"id": "body-0037", "role": "body", "section": "MTP Modules", "weight": 1.0} -->

To be specific, our MTP implementation uses $D$ sequential modules to predict $D$ additional tokens. The $k$-th MTP module consists of a shared embedding layer ${Emb}{( \cdot )}$, a shared output head ${OutHead}{( \cdot )}$, a Transformer block ${TRM}_{k}{( \cdot )}$, and a projection matrix $M_{k} \in {\mathbb{R}}^{{d \times 2}d}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "MTP Modules", "weight": 1.0} -->

where $\lbrack \cdot; \cdot \rbrack$ denotes concatenation. Especially, when $k = 1$, $\mathbf{h}_{i}^{k - 1}$ refers to the representation given by the main model. Note that for each MTP module, its embedding layer is shared with the main model.

<!-- chunk {"id": "body-0039", "role": "body", "section": "MTP Modules", "weight": 1.0} -->

where $T$ represents the input sequence length and ~i:j~ denotes the slicing operation (inclusive of both the left and right boundaries).

<!-- chunk {"id": "body-0040", "role": "body", "section": "MTP Modules", "weight": 1.0} -->

The output head ${OutHead}{( \cdot )}$ linearly maps the representation to logits and subsequently applies the ${Softmax}{( \cdot )}$ function to compute the prediction probabilities of the $k$-th additional token. Also, for each MTP module, its output head is shared with the main model. Our principle of maintaining the causal chain of predictions is similar to that of EAGLE, but its primary objective is speculative decoding (Xia et al. Leviathan et al., ), whereas we utilize MTP to improve training.

<!-- chunk {"id": "body-0041", "role": "body", "section": "MTP Training Objective", "weight": 1.0} -->

where $T$ denotes the input sequence length, $t_{i}$ denotes the ground-truth token at the $i$-th position, and $P_{i}^{k}{\lbrack t_{i}\rbrack}$ denotes the corresponding prediction probability of $t_{i}$, given by the $k$-th MTP module.

<!-- chunk {"id": "body-0042", "role": "body", "section": "MTP in Inference", "weight": 1.0} -->

Our MTP strategy mainly aims to improve the performance of the main model, so during inference, we can directly discard the MTP modules and the main model can function independently and normally. Additionally, we can also repurpose these MTP modules for speculative decoding to further improve the generation latency.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Compute Clusters", "weight": 1.0} -->

DeepSeek-V3 is trained on a cluster equipped with 2048 NVIDIA H800 GPUs. Each node in the H800 cluster contains 8 GPUs connected by NVLink and NVSwitch within nodes. Across different nodes, InfiniBand (IB) interconnects are utilized to facilitate communications.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Training Framework", "weight": 1.0} -->

The training of DeepSeek-V3 is supported by the HAI-LLM framework, an efficient and lightweight training framework crafted by our engineers from the ground up. On the whole, DeepSeek-V3 applies 16-way Pipeline Parallelism (PP), 64-way Expert Parallelism (EP) spanning 8 nodes, and ZeRO-1 Data Parallelism (DP).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Training Framework", "weight": 1.0} -->

In order to facilitate efficient training of DeepSeek-V3, we implement meticulous engineering optimizations. Firstly, we design the DualPipe algorithm for efficient pipeline parallelism. Compared with existing PP methods, DualPipe has fewer pipeline bubbles. More importantly, it overlaps the computation and communication phases across forward and backward processes, thereby addressing the challenge of heavy communication overhead introduced by cross-node expert parallelism. Secondly, we develop efficient cross-node all-to-all communication kernels to fully utilize IB and NVLink bandwidths and conserve Streaming Multiprocessors (SMs) dedicated to communication. Finally, we meticulously optimize the memory footprint during training, thereby enabling us to train DeepSeek-V3 without using costly Tensor Parallelism (TP).

<!-- chunk {"id": "body-0046", "role": "body", "section": "DualPipe and Computation-Communication Overlap", "weight": 1.0} -->

For DeepSeek-V3, the communication overhead introduced by cross-node expert parallelism results in an inefficient computation-to-communication ratio of approximately 1:1. To tackle this challenge, we design an innovative pipeline parallelism algorithm called DualPipe, which not only accelerates model training by effectively overlapping forward and backward computation-communication phases, but also reduces the pipeline bubbles.

<!-- chunk {"id": "body-0047", "role": "body", "section": "DualPipe and Computation-Communication Overlap", "weight": 1.0} -->

The key idea of DualPipe is to overlap the computation and communication within a pair of individual forward and backward chunks. To be specific, we divide each chunk into four components: attention, all-to-all dispatch, MLP, and all-to-all combine. Specially, for a backward chunk, both attention and MLP are further split into two parts, backward for input and backward for weights, like in ZeroBubble. In addition, we have a PP communication component. As illustrated in Figure, for a pair of forward and backward chunks, we rearrange these components and manually adjust the ratio of GPU SMs dedicated to communication versus computation. In this overlapping strategy, we can ensure that both all-to-all and PP communication can be fully hidden during execution. Given the efficient overlapping strategy, the full DualPipe scheduling is illustrated in Figure. It employs a bidirectional pipeline scheduling, which feeds micro-batches from both ends of the pipeline simultaneously and a significant portion of communications can be fully overlapped.

<!-- chunk {"id": "body-0048", "role": "body", "section": "DualPipe and Computation-Communication Overlap", "weight": 1.0} -->

This overlap also ensures that, as the model further scales up, as long as we maintain a constant computation-to-communication ratio, we can still employ fine-grained experts across nodes while achieving a near-zero all-to-all communication overhead.

<!-- chunk {"id": "body-0049", "role": "body", "section": "DualPipe and Computation-Communication Overlap", "weight": 1.0} -->

In addition, even in more general scenarios without a heavy communication burden, DualPipe still exhibits efficiency advantages. In Table, we summarize the pipeline bubbles and memory usage across different PP methods. As shown in the table, compared with ZB1P and 1F1B, DualPipe significantly reduces the pipeline bubbles while only increasing the peak activation memory by $\frac{1}{PP}$ times. Although DualPipe requires keeping two copies of the model parameters, this does not significantly increase the memory consumption since we use a large EP size during training. Compared with Chimera, DualPipe only requires that the pipeline stages and micro-batches be divisible by 2, without requiring micro-batches to be divisible by pipeline stages. In addition, for DualPipe, neither the bubbles nor activation memory will increase as the number of micro-batches grows.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Efficient Implementation of Cross-Node All-to-All Communication", "weight": 1.0} -->

In order to ensure sufficient computational performance for DualPipe, we customize efficient cross-node all-to-all communication kernels (including dispatching and combining) to conserve the number of SMs dedicated to communication. The implementation of the kernels is co-designed with the MoE gating algorithm and the network topology of our cluster. To be specific, in our cluster, cross-node GPUs are fully interconnected with IB, and intra-node communications are handled via NVLink. NVLink offers a bandwidth of 160 GB/s, roughly 3.2 times that of IB (50 GB/s). To effectively leverage the different bandwidths of IB and NVLink, we limit each token to be dispatched to at most 4 nodes, thereby reducing IB traffic. For each token, when its routing decision is made, it will first be transmitted via IB to the GPUs with the same in-node index on its target nodes. Once it reaches the target nodes, we will endeavor to ensure that it is instantaneously forwarded via NVLink to specific GPUs that host their target experts, without being blocked by subsequently arriving tokens.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Efficient Implementation of Cross-Node All-to-All Communication", "weight": 1.0} -->

In this way, communications via IB and NVLink are fully overlapped, and each token can efficiently select an average of 3.2 experts per node without incurring additional overhead from NVLink. This implies that, although DeepSeek-V3 selects only 8 routed experts in practice, it can scale up this number to a maximum of 13 experts (4 nodes $\times$ 3.2 experts/node) while preserving the same communication cost. Overall, under such a communication strategy, only 20 SMs are sufficient to fully utilize the bandwidths of IB and NVLink.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Efficient Implementation of Cross-Node All-to-All Communication", "weight": 1.0} -->

In detail, we employ the warp specialization technique and partition 20 SMs into 10 communication channels. During the dispatching process, IB sending, IB-to-NVLink forwarding, and NVLink receiving are handled by respective warps. The number of warps allocated to each communication task is dynamically adjusted according to the actual workload across all SMs. Similarly, during the combining process, NVLink sending, NVLink-to-IB forwarding and accumulation, and IB receiving and accumulation are also handled by dynamically adjusted warps. In addition, both dispatching and combining kernels overlap with the computation stream, so we also consider their impact on other SM computation kernels. Specifically, we employ customized PTX (Parallel Thread Execution) instructions and auto-tune the communication chunk size, which significantly reduces the use of the L2 cache and the interference to other SMs.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Extremely Memory Saving with Minimal Overhead", "weight": 1.0} -->

In order to reduce the memory footprint during training, we employ the following techniques.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Recomputation of RMSNorm and MLA Up-Projection", "weight": 1.0} -->

We recompute all RMSNorm operations and MLA up-projections during back-propagation, thereby eliminating the need to persistently store their output activations. With a minor overhead, this strategy significantly reduces memory requirements for storing activations.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Exponential Moving Average in CPU", "weight": 1.0} -->

During training, we preserve the Exponential Moving Average (EMA) of the model parameters for early estimation of the model performance after learning rate decay. The EMA parameters are stored in CPU memory and are updated asynchronously after each training step. This method allows us to maintain EMA parameters without incurring additional memory or time overhead.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Shared Embedding and Output Head for Multi-Token Prediction", "weight": 1.0} -->

With the DualPipe strategy, we deploy the shallowest layers (including the embedding layer) and deepest layers (including the output head) of the model on the same PP rank. This arrangement enables the physical sharing of parameters and gradients, of the shared embedding and output head, between the MTP module and the main model. This physical sharing mechanism further enhances our memory efficiency.

<!-- chunk {"id": "body-0057", "role": "body", "section": "FP8 Training", "weight": 1.0} -->

Inspired by recent advances in low-precision training, we propose a fine-grained mixed precision framework utilizing the FP8 data format for training DeepSeek-V3. While low-precision training holds great promise, it is often limited by the presence of outliers in activations, weights, and gradients (Sun et al. He et al. Fishman et al., ). Although significant progress has been made in inference quantization (Xiao et al. Frantar et al., ), there are relatively few studies demonstrating successful application of low-precision techniques in large-scale language model pre-training. To address this challenge and effectively extend the dynamic range of the FP8 format, we introduce a fine-grained quantization strategy: tile-wise grouping with $1 \times N_{c}$ elements or block-wise grouping with $N_{c} \times N_{c}$ elements. The associated dequantization overhead is largely mitigated under our increased-precision accumulation process, a critical aspect for achieving accurate FP8 General Matrix Multiplication (GEMM).

<!-- chunk {"id": "body-0058", "role": "body", "section": "FP8 Training", "weight": 1.0} -->

Moreover, to further reduce memory and communication overhead in MoE training, we cache and dispatch activations in FP8, while storing low-precision optimizer states. We validate the proposed FP8 mixed precision framework on two model scales similar to DeepSeek-V2-Lite and DeepSeek-V2, training for approximately 1 trillion tokens (see more details in Appendix B.1). Notably, compared with the baseline, the relative loss error of our FP8-training model remains consistently below 0.25%, a level well within the acceptable range of training randomness.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Mixed Precision Framework", "weight": 1.0} -->

Building upon widely adopted techniques in low-precision training (Kalamkar et al. Narang et al., ), we propose a mixed precision framework for FP8 training. In this framework, most compute-density operations are conducted in FP8, while a few key operations are strategically maintained in their original data formats to balance training efficiency and numerical stability. The overall framework is illustrated in Figure.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Mixed Precision Framework", "weight": 1.0} -->

Firstly, in order to accelerate model training, the majority of core computation kernels, i.e., GEMM operations, are implemented in FP8 precision. These GEMM operations accept FP8 tensors as inputs and produce outputs in or. As depicted in Figure, all three GEMMs associated with the Linear operator, namely Fprop (forward pass), Dgrad (activation backward pass), and Wgrad (weight backward pass), are executed in FP8. This design theoretically doubles the computational speed compared with the original method. Additionally, the FP8 Wgrad GEMM allows activations to be stored in FP8 for use in the backward pass. This significantly reduces memory consumption.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Mixed Precision Framework", "weight": 1.0} -->

Despite the efficiency advantage of the FP8 format, certain operators still require a higher precision due to their sensitivity to low-precision computations. Besides, some low-cost operators can also utilize a higher precision with a negligible overhead to the overall training cost. For this reason, after careful investigations, we maintain the original precision (e.g., or ) for the following components: the embedding module, the output head, MoE gating modules, normalization operators, and attention operators. These targeted retentions of high precision ensure stable training dynamics for DeepSeek-V3. To further guarantee numerical stability, we store the master weights, weight gradients, and optimizer states in higher precision. While these high-precision components incur some memory overheads, their impact can be minimized through efficient sharding across multiple DP ranks in our distributed training system.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Improved Precision from Quantization and Multiplication", "weight": 1.0} -->

Based on our mixed precision FP8 framework, we introduce several strategies to enhance low-precision training accuracy, focusing on both the quantization method and the multiplication process.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Fine-Grained Quantization", "weight": 1.0} -->

In low-precision training frameworks, overflows and underflows are common challenges due to the limited dynamic range of the FP8 format, which is constrained by its reduced exponent bits. As a standard practice, the input distribution is aligned to the representable range of the FP8 format by scaling the maximum absolute value of the input tensor to the maximum representable value of FP8. This method makes low-precision training highly sensitive to activation outliers, which can heavily degrade quantization accuracy. To solve this, we propose a fine-grained quantization method that applies scaling at a more granular level. As illustrated in Figure (a), for activations, we group and scale elements on a 1x128 tile basis (i.e., per token per 128 channels); and for weights, we group and scale elements on a 128x128 block basis (i.e., per 128 input channels per 128 output channels). This approach ensures that the quantization process can better accommodate outliers by adapting the scale according to smaller groups of elements.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Fine-Grained Quantization", "weight": 1.0} -->

In Appendix B.2, we further discuss the training instability when we group and scale activations on a block basis in the same way as weights quantization.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Fine-Grained Quantization", "weight": 1.0} -->

One key modification in our method is the introduction of per-group scaling factors along the inner dimension of GEMM operations. This functionality is not directly supported in the standard FP8 GEMM. However, combined with our precise accumulation strategy, it can be efficiently implemented.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Fine-Grained Quantization", "weight": 1.0} -->

Notably, our fine-grained quantization strategy is highly consistent with the idea of microscaling formats, while the Tensor Cores of NVIDIA next-generation GPUs (Blackwell series) have announced the support for microscaling formats with smaller quantization granularity. We hope our design can serve as a reference for future work to keep pace with the latest GPU architectures.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Increasing Accumulation Precision", "weight": 1.0} -->

Low-precision GEMM operations often suffer from underflow issues, and their accuracy largely depends on high-precision accumulation, which is commonly performed in an precision (Kalamkar et al. Narang et al., ). However, we observe that the accumulation precision of FP8 GEMM on NVIDIA H800 GPUs is limited to retaining around 14 bits, which is significantly lower than accumulation precision. This problem will become more pronounced when the inner dimension K is large, a typical scenario in large-scale model training where the batch size and model width are increased. Taking GEMM operations of two random matrices with K = 4096 for example, in our preliminary test, the limited accumulation precision in Tensor Cores results in a maximum relative error of nearly 2%. Despite these problems, the limited accumulation precision is still the default option in a few FP8 frameworks, severely constraining the training accuracy.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Increasing Accumulation Precision", "weight": 1.0} -->

In order to address this issue, we adopt the strategy of promotion to CUDA Cores for higher precision. The process is illustrated in Figure (b). To be specific, during MMA (Matrix Multiply-Accumulate) execution on Tensor Cores, intermediate results are accumulated using the limited bit width. Once an interval of $N_{C}$ is reached, these partial results will be copied to registers on CUDA Cores, where full-precision accumulation is performed. As mentioned before, our fine-grained quantization applies per-group scaling factors along the inner dimension K. These scaling factors can be efficiently multiplied on the CUDA Cores as the dequantization process with minimal additional computational cost.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Increasing Accumulation Precision", "weight": 1.0} -->

It is worth noting that this modification reduces the WGMMA (Warpgroup-level Matrix Multiply-Accumulate) instruction issue rate for a single warpgroup. However, on the H800 architecture, it is typical for two WGMMA to persist concurrently: while one warpgroup performs the promotion operation, the other is able to execute the MMA operation. This design enables overlapping of the two operations, maintaining high utilization of Tensor Cores. Based on our experiments, setting $N_{C} = 128$ elements, equivalent to 4 WGMMAs, represents the minimal accumulation interval that can significantly improve precision without introducing substantial overhead.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Mantissa over Exponents", "weight": 1.0} -->

In contrast to the hybrid FP8 format adopted by prior work, which uses E4M3 (4-bit exponent and 3-bit mantissa) in Fprop and E5M2 (5-bit exponent and 2-bit mantissa) in Dgrad and Wgrad, we adopt the E4M3 format on all tensors for higher precision. We attribute the feasibility of this approach to our fine-grained quantization strategy, i.e., tile and block-wise scaling. By operating on smaller element groups, our methodology effectively shares exponent bits among these grouped elements, mitigating the impact of the limited dynamic range.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Online Quantization", "weight": 1.0} -->

Delayed quantization is employed in tensor-wise quantization frameworks, which maintains a history of the maximum absolute values across prior iterations to infer the current value. In order to ensure accurate scales and simplify the framework, we calculate the maximum absolute value online for each 1x128 activation tile or 128x128 weight block. Based on it, we derive the scaling factor and then quantize the activation or weight online into the FP8 format.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Low-Precision Storage and Communication", "weight": 1.0} -->

In conjunction with our FP8 training framework, we further reduce the memory consumption and communication overhead by compressing cached activations and optimizer states into lower-precision formats.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Low-Precision Optimizer States", "weight": 1.0} -->

We adopt the data format instead of to track the first and second moments in the AdamW optimizer, without incurring observable performance degradation. However, the master weights (stored by the optimizer) and gradients (used for batch size accumulation) are still retained in to ensure numerical stability throughout training.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Low-Precision Activation", "weight": 1.0} -->

As illustrated in Figure, the Wgrad operation is performed in FP8. To reduce the memory consumption, it is a natural choice to cache activations in FP8 format for the backward pass of the Linear operator.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Low-Precision Activation", "weight": 1.0} -->

> \(1\) Inputs of the Linear after the attention operator. These activations are also used in the backward pass of the attention operator, which makes it sensitive to precision. We adopt a customized E5M6 data format exclusively for these activations. Additionally, these activations will be converted from an 1x128 quantization tile to an 128x1 tile in the backward pass. To avoid introducing extra quantization error, all the scaling factors are round scaled, i.e., integral power of 2.
> \(2\) Inputs of the SwiGLU operator in MoE. To further reduce the memory cost, we cache the inputs of the SwiGLU operator and recompute its output in the backward pass. These activations are also stored in FP8 with our fine-grained quantization method, striking a balance between memory efficiency and computational accuracy.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Low-Precision Communication", "weight": 1.0} -->

Communication bandwidth is a critical bottleneck in the training of MoE models. To alleviate this challenge, we quantize the activation before MoE up-projections into FP8 and then apply dispatch components, which is compatible with FP8 Fprop in MoE up-projections. Like the inputs of the Linear after the attention operator, scaling factors for this activation are integral power of 2. A similar strategy is applied to the activation gradient before MoE down-projections. For both the forward and backward combine components, we retain them in to preserve training precision in critical parts of the training pipeline.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Inference and Deployment", "weight": 1.0} -->

We deploy DeepSeek-V3 on the H800 cluster, where GPUs within each node are interconnected using NVLink, and all GPUs across the cluster are fully interconnected via IB. To simultaneously ensure both the Service-Level Objective (SLO) for online services and high throughput, we employ the following deployment strategy that separates the prefilling and decoding stages.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Prefilling", "weight": 1.0} -->

The minimum deployment unit of the prefilling stage consists of 4 nodes with 32 GPUs. The attention part employs 4-way Tensor Parallelism (TP4) with Sequence Parallelism (SP), combined with 8-way Data Parallelism (DP8). Its small TP size of 4 limits the overhead of TP communication. For the MoE part, we use 32-way Expert Parallelism, which ensures that each expert processes a sufficiently large batch size, thereby enhancing computational efficiency. For the MoE all-to-all communication, we use the same method as in training: first transferring tokens across nodes via IB, and then forwarding among the intra-node GPUs via NVLink. In particular, we use 1-way Tensor Parallelism for the dense MLPs in shallow layers to save TP communication.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Prefilling", "weight": 1.0} -->

To achieve load balancing among different experts in the MoE part, we need to ensure that each GPU processes approximately the same number of tokens. To this end, we introduce a deployment strategy of redundant experts, which duplicates high-load experts and deploys them redundantly. The high-load experts are detected based on statistics collected during the online deployment and are adjusted periodically (e.g., every 10 minutes). After determining the set of redundant experts, we carefully rearrange experts among GPUs within a node based on the observed loads, striving to balance the load across GPUs as much as possible without increasing the cross-node all-to-all communication overhead. For the deployment of DeepSeek-V3, we set 32 redundant experts for the prefilling stage. For each GPU, besides the original 8 experts it hosts, it will also host one additional redundant expert.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Prefilling", "weight": 1.0} -->

Furthermore, in the prefilling stage, to improve the throughput and hide the overhead of all-to-all and TP communication, we simultaneously process two micro-batches with similar computational workloads, overlapping the attention and MoE of one micro-batch with the dispatch and combine of another.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Prefilling", "weight": 1.0} -->

Finally, we are exploring a dynamic redundancy strategy for experts, where each GPU hosts more experts (e.g., 16 experts), but only 9 will be activated during each inference step. Before the all-to-all operation at each layer begins, we compute the globally optimal routing scheme on the fly. Given the substantial computation involved in the prefilling stage, the overhead of computing this routing scheme is almost negligible.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Decoding", "weight": 1.0} -->

During decoding, we treat the shared expert as a routed one. From this perspective, each token will select 9 experts during routing, where the shared expert is regarded as a heavy-load one that will always be selected. The minimum deployment unit of the decoding stage consists of 40 nodes with 320 GPUs. The attention part employs TP4 with SP, combined, while the MoE part uses EP320. For the MoE part, each GPU hosts only one expert, and 64 GPUs are responsible for hosting redundant experts and shared experts. All-to-all communication of the dispatch and combine parts is performed via direct point-to-point transfers over IB to achieve low latency. Additionally, we leverage the IBGDA technology to further minimize latency and enhance communication efficiency.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Decoding", "weight": 1.0} -->

Similar to prefilling, we periodically determine the set of redundant experts in a certain interval, based on the statistical expert load from our online service. However, we do not need to rearrange experts since each GPU only hosts one expert. We are also exploring the dynamic redundancy strategy for decoding. However, this requires more careful optimization of the algorithm that computes the globally optimal routing scheme and the fusion with the dispatch kernel to reduce overhead.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Decoding", "weight": 1.0} -->

Additionally, to enhance throughput and hide the overhead of all-to-all communication, we are also exploring processing two micro-batches with similar computational workloads simultaneously in the decoding stage. Unlike prefilling, attention consumes a larger portion of time in the decoding stage. Therefore, we overlap the attention of one micro-batch with the dispatch+MoE+combine of another. In the decoding stage, the batch size per expert is relatively small (usually within 256 tokens), and the bottleneck is memory access rather than computation. Since the MoE part only needs to load the parameters of one expert, the memory access overhead is minimal, so using fewer SMs will not significantly affect the overall performance. Therefore, to avoid impacting the computation speed of the attention part, we can allocate only a small portion of SMs to dispatch+MoE+combine.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Suggestions on Hardware Design", "weight": 1.0} -->

Based on our implementation of the all-to-all communication and FP8 training scheme, we propose the following suggestions on chip design to AI hardware vendors.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Communication Hardware", "weight": 1.0} -->

In DeepSeek-V3, we implement the overlap between computation and communication to hide the communication latency during computation. This significantly reduces the dependency on communication bandwidth compared to serial computation and communication. However, the current communication implementation relies on expensive SMs (e.g., we allocate 20 out of the 132 SMs available in the H800 GPU for this purpose), which will limit the computational throughput. Moreover, using SMs for communication results in significant inefficiencies, as tensor cores remain entirely under-utilized.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Communication Hardware", "weight": 1.0} -->

Forwarding data between the IB (InfiniBand) and NVLink domain while aggregating IB traffic destined for multiple GPUs within the same node from a single GPU.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Communication Hardware", "weight": 1.0} -->

Transporting data between RDMA buffers (registered GPU memory regions) and input/output buffers.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Communication Hardware", "weight": 1.0} -->

Executing reduce operations for all-to-all combine.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Communication Hardware", "weight": 1.0} -->

Managing fine-grained memory layout during chunked data transferring to multiple experts across the IB and NVLink domain.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Communication Hardware", "weight": 1.0} -->

We aspire to see future vendors developing hardware that offloads these communication tasks from the valuable computation unit SM, serving as a GPU co-processor or a network co-processor like NVIDIA SHARP Graham et al.. Furthermore, to reduce application programming complexity, we aim for this hardware to unify the IB (scale-out) and NVLink (scale-up) networks from the perspective of the computation units. With this unified interface, computation units can easily accomplish operations such as read, write, multicast, and reduce across the entire IB-NVLink-unified domain via submitting communication requests based on simple primitives.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Higher FP8 GEMM Accumulation Precision in Tensor Cores", "weight": 1.0} -->

In the current Tensor Core implementation of the NVIDIA Hopper architecture, FP8 GEMM suffers from limited accumulation precision. After aligning 32 mantissa products by right-shifting based on the maximum exponent, the Tensor Core only uses the highest 14 bits of each mantissa product for addition, and truncates bits exceeding this range. The accumulation of addition results into registers also employs 14-bit precision. Our implementation partially mitigates the limitation by accumulating the addition results of 128 FP8$\times$FP8 multiplications into registers with precision in the CUDA core. Although helpful in achieving successful FP8 training, it is merely a compromise due to the Hopper architecture's hardware deficiency in FP8 GEMM accumulation precision. Future chips need to adopt higher precision.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Support for Tile- and Block-Wise Quantization", "weight": 1.0} -->

Current GPUs only support per-tensor quantization, lacking the native support for fine-grained quantization like our tile- and block-wise quantization. In the current implementation, when the $N_{C}$ interval is reached, the partial results will be copied from Tensor Cores to CUDA cores, multiplied by the scaling factors, and added to registers on CUDA cores. Although the dequantization overhead is significantly mitigated combined with our precise accumulation strategy, the frequent data movements between Tensor Cores and CUDA cores still limit the computational efficiency. Therefore, we recommend future chips to support fine-grained quantization by enabling Tensor Cores to receive scaling factors and implement MMA with group scaling. In this way, the whole partial sum accumulation and dequantization can be completed directly inside Tensor Cores until the final result is produced, avoiding frequent data movements.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Support for Online Quantization", "weight": 1.0} -->

The current implementations struggle to effectively support online quantization, despite its effectiveness demonstrated in our research. In the existing process, we need to read 128 activation values (the output of the previous computation) from HBM (High Bandwidth Memory) for quantization, and the quantized FP8 values are then written back to HBM, only to be read again for MMA. To address this inefficiency, we recommend that future chips integrate FP8 cast and TMA (Tensor Memory Accelerator) access into a single fused operation, so quantization can be completed during the transfer of activations from global memory to shared memory, avoiding frequent memory reads and writes. We also recommend supporting a warp-level cast instruction for speedup, which further facilitates the better fusion of layer normalization and FP8 cast. Alternatively, a near-memory computing approach can be adopted, where compute logic is placed near the HBM. In this case, elements can be cast to FP8 directly as they are read from HBM into the GPU, reducing off-chip memory access by roughly 50%.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Support for Transposed GEMM Operations", "weight": 1.0} -->

The current architecture makes it cumbersome to fuse matrix transposition with GEMM operations. In our workflow, activations during the forward pass are quantized into 1x128 FP8 tiles and stored. During the backward pass, the matrix needs to be read out, dequantized, transposed, re-quantized into 128x1 tiles, and stored in HBM. To reduce memory operations, we recommend future chips to enable direct transposed reads of matrices from shared memory before MMA operation, for those precisions required in both training and inference. Combined with the fusion of FP8 format conversion and TMA access, this enhancement will significantly streamline the quantization workflow.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Data Construction", "weight": 1.0} -->

Compared with DeepSeek-V2, we optimize the pre-training corpus by enhancing the ratio of mathematical and programming samples, while expanding multilingual coverage beyond English and Chinese. Also, our data processing pipeline is refined to minimize redundancy while maintaining corpus diversity. Inspired by Ding et al., we implement the document packing method for data integrity but do not incorporate cross-sample attention masking during training. Finally, the training corpus for DeepSeek-V3 consists of 14.8T high-quality and diverse tokens in our tokenizer.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Data Construction", "weight": 1.0} -->

In the training process of DeepSeekCoder-V2, we observe that the Fill-in-Middle (FIM) strategy does not compromise the next-token prediction capability while enabling the model to accurately predict middle text based on contextual cues. In alignment with DeepSeekCoder-V2, we also incorporate the FIM strategy in the pre-training of DeepSeek-V3.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Data Construction", "weight": 1.0} -->

This structure is applied at the document level as a part of the pre-packing process. The FIM strategy is applied at a rate of 0.1, consistent with the PSM framework.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Data Construction", "weight": 1.0} -->

The tokenizer for DeepSeek-V3 employs Byte-level BPE with an extended vocabulary of 128K tokens. The pretokenizer and training data for our tokenizer are modified to optimize multilingual compression efficiency. In addition, compared with DeepSeek-V2, the new pretokenizer introduces tokens that combine punctuations and line breaks. However, this trick may introduce the token boundary bias when the model processes multi-line prompts without terminal line breaks, particularly for few-shot evaluation prompts. To address this issue, we randomly split a certain proportion of such combined tokens during training, which exposes the model to a wider array of special cases and mitigates this bias.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Model Hyper-Parameters", "weight": 1.0} -->

We set the number of Transformer layers to 61 and the hidden dimension to 7168. All learnable parameters are randomly initialized with a standard deviation of 0.006. In MLA, we set the number of attention heads $n_{h}$ to 128 and the per-head dimension $d_{h}$ to 128. The KV compression dimension $d_{c}$ is set to 512, and the query compression dimension $d_{c}^{\prime}$ is set to 1536. For the decoupled queries and key, we set the per-head dimension $d_{h}^{R}$ to 64. We substitute all FFNs except for the first three layers with MoE layers. Each MoE layer consists of 1 shared expert and 256 routed experts, where the intermediate hidden dimension of each expert is 2048. Among the routed experts, 8 experts will be activated for each token, and each token will be ensured to be sent to at most 4 nodes. The multi-token prediction depth $D$ is set to 1, i.e., besides the exact next token, each token will predict one additional token.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Model Hyper-Parameters", "weight": 1.0} -->

As DeepSeek-V2, DeepSeek-V3 also employs additional RMSNorm layers after the compressed latent vectors, and multiplies additional scaling factors at the width bottlenecks. Under this configuration, DeepSeek-V3 comprises 671B total parameters, of which 37B are activated for each token.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Training Hyper-Parameters", "weight": 1.0} -->

We employ the AdamW optimizer with hyper-parameters set to $\beta_{1} = 0.9$, $\beta_{2} = 0.95$, and ${{weight}\_{decay}} = 0.1$. We set the maximum sequence length to 4K during pre-training, and pre-train DeepSeek-V3 on 14.8T tokens. As for the learning rate scheduling, we first linearly increase it from 0 to $2.2 \times 10^{- 4}$ during the first 2K steps. Then, we keep a constant learning rate of $2.2 \times 10^{- 4}$ until the model consumes 10T training tokens. Subsequently, we gradually decay the learning rate to $2.2 \times 10^{- 5}$ in 4.3T tokens, following a cosine decay curve.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Training Hyper-Parameters", "weight": 1.0} -->

During the training of the final 500B tokens, we keep a constant learning rate of $2.2 \times 10^{- 5}$ in the first 333B tokens, and switch to another constant learning rate of $7.3 \times 10^{- 6}$ in the remaining 167B tokens. The gradient clipping norm is set to 1.0. We employ a batch size scheduling strategy, where the batch size is gradually increased from 3072 to 15360 in the training of the first 469B tokens, and then keeps 15360 in the remaining training. We leverage pipeline parallelism to deploy different layers of a model on different GPUs, and for each layer, the routed experts will be uniformly deployed on 64 GPUs belonging to 8 nodes. As for the node-limited routing, each token will be sent to at most 4 nodes (i.e., $M = 4$). For auxiliary-loss-free load balancing, we set the bias update speed $\gamma$ to 0.001 for the first 14.3T tokens, and to 0.0 for the remaining 500B tokens.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Training Hyper-Parameters", "weight": 1.0} -->

For the balance loss, we set $\alpha$ to 0.0001, just to avoid extreme imbalance within any single sequence. The MTP loss weight $\lambda$ is set to 0.3 for the first 10T tokens, and to 0.1 for the remaining 4.8T tokens.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Long Context Extension", "weight": 1.0} -->

We adopt a similar approach to DeepSeek-V2 to enable long context capabilities in DeepSeek-V3. After the pre-training stage, we apply YaRN for context extension and perform two additional training phases, each comprising 1000 steps, to progressively expand the context window from 4K to 32K and then to 128K. The YaRN configuration is consistent with that used in DeepSeek-V2, being applied exclusively to the decoupled shared key $\mathbf{k}_{t}^{R}$. The hyper-parameters remain identical across both phases, with the scale $s = 40$, $\alpha = 1$, $\beta = 32$, and the scaling factor $\sqrt{t} = {{0.1{\ln s}} + 1}$. In the first phase, the sequence length is set to 32K, and the batch size is 1920. During the second phase, the sequence length is increased to 128K, and the batch size is reduced to 480. The learning rate for both phases is set to $7.3 \times 10^{- 6}$, matching the final learning rate from the pre-training stage.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Long Context Extension", "weight": 1.0} -->

Through this two-phase extension training, DeepSeek-V3 is capable of handling inputs up to 128K in length while maintaining strong performance. Figure illustrates that DeepSeek-V3, following supervised fine-tuning, achieves notable performance on the \"Needle In A Haystack\" (NIAH) test, demonstrating consistent robustness across context window lengths up to 128K.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Evaluation Benchmarks", "weight": 1.0} -->

The base model of DeepSeek-V3 is pretrained on a multilingual corpus with English and Chinese constituting the majority, so we evaluate its performance on a series of benchmarks primarily in English and Chinese, as well as on a multilingual benchmark. Our evaluation is based on our internal evaluation framework integrated in our HAI-LLM framework.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Evaluation Benchmarks", "weight": 1.0} -->

Multi-subject multiple-choice datasets include MMLU, MMLU-Redux, MMLU-Pro, MMMLU, C-Eval, and CMMLU.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Evaluation Benchmarks", "weight": 1.0} -->

Language understanding and reasoning datasets include HellaSwag, PIQA, ARC, and BigBench Hard (BBH).

<!-- chunk {"id": "body-0110", "role": "body", "section": "Evaluation Benchmarks", "weight": 1.0} -->

Closed-book question answering datasets include TriviaQA and NaturalQuestions.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Evaluation Benchmarks", "weight": 1.0} -->

Reading comprehension datasets include RACE Lai et al., DROP, C3, and CMRC.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Evaluation Benchmarks", "weight": 1.0} -->

Reference disambiguation datasets include CLUEWSC and WinoGrande Sakaguchi et al..

<!-- chunk {"id": "body-0113", "role": "body", "section": "Evaluation Benchmarks", "weight": 1.0} -->

Language modeling datasets include Pile.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Evaluation Benchmarks", "weight": 1.0} -->

Chinese understanding and culture datasets include CCPM.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Evaluation Benchmarks", "weight": 1.0} -->

Math datasets include GSM8K, MATH, MGSM, and CMath.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Evaluation Benchmarks", "weight": 1.0} -->

Code datasets include HumanEval, LiveCodeBench-Base (0801-1101), MBPP, and CRUXEval.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Evaluation Benchmarks", "weight": 1.0} -->

Standardized exams include AGIEval. Note that AGIEval includes both English and Chinese subsets.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Evaluation Benchmarks", "weight": 1.0} -->

Following our previous work, we adopt perplexity-based evaluation for datasets including HellaSwag, PIQA, WinoGrande, RACE-Middle, RACE-High, MMLU, MMLU-Redux, MMLU-Pro, MMMLU, ARC-Easy, ARC-Challenge, C-Eval, CMMLU, C3, and CCPM, and adopt generation-based evaluation for TriviaQA, NaturalQuestions, DROP, MATH, GSM8K, MGSM, HumanEval, MBPP, LiveCodeBench-Base, CRUXEval, BBH, AGIEval, CLUEWSC, CMRC, and CMath. In addition, we perform language-modeling-based evaluation for Pile-test and use Bits-Per-Byte (BPB) as the metric to guarantee fair comparison among models using different tokenizers.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Evaluation Results", "weight": 1.0} -->

In Table, we compare the base model of DeepSeek-V3 with the state-of-the-art open-source base models, including DeepSeek-V2-Base (our previous release), Qwen2.5 72B Base, and LLaMA-3.1 405B Base. We evaluate all these models with our internal evaluation framework, and ensure that they share the same evaluation setting. Note that due to the changes in our evaluation framework over the past months, the performance of DeepSeek-V2-Base exhibits a slight difference from our previously reported results. Overall, DeepSeek-V3-Base comprehensively outperforms DeepSeek-V2-Base and Qwen2.5 72B Base, and surpasses LLaMA-3.1 405B Base in the majority of benchmarks, essentially becoming the strongest open-source model.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Evaluation Results", "weight": 1.0} -->

From a more detailed perspective, we compare DeepSeek-V3-Base with the other open-source base models individually. Compared with DeepSeek-V2-Base, due to the improvements in our model architecture, the scale-up of the model size and training tokens, and the enhancement of data quality, DeepSeek-V3-Base achieves significantly better performance as expected. Compared with Qwen2.5 72B Base, the state-of-the-art Chinese open-source model, with only half of the activated parameters, DeepSeek-V3-Base also demonstrates remarkable advantages, especially on English, multilingual, code, and math benchmarks. As for Chinese benchmarks, except for CMMLU, a Chinese multi-subject multiple-choice task, DeepSeek-V3-Base also shows better performance than Qwen2.5 72B. Compared with LLaMA-3.1 405B Base, the largest open-source model with 11 times the activated parameters, DeepSeek-V3-Base also exhibits much better performance on multilingual, code, and math benchmarks.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Evaluation Results", "weight": 1.0} -->

As for English and Chinese language benchmarks, DeepSeek-V3-Base shows competitive or better performance, and is especially good on BBH, MMLU-series, DROP, C-Eval, CMMLU, and CCPM.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Evaluation Results", "weight": 1.0} -->

Due to our efficient architectures and comprehensive engineering optimizations, DeepSeek-V3 achieves extremely high training efficiency. Under our training framework and infrastructures, training DeepSeek-V3 on each trillion tokens requires only 180K H800 GPU hours, which is much cheaper than training 72B or 405B dense models.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Ablation Studies for Multi-Token Prediction", "weight": 1.0} -->

In Table, we show the ablation results for the MTP strategy. To be specific, we validate the MTP strategy on top of two baseline models across different scales. At the small scale, we train a baseline MoE model comprising 15.7B total parameters on 1.33T tokens. At the large scale, we train a baseline MoE model comprising 228.7B total parameters on 540B tokens. On top of them, keeping the training data and the other architectures the same, we append a 1-depth MTP module onto them and train two models with the MTP strategy for comparison. Note that during inference, we directly discard the MTP module, so the inference costs of the compared models are exactly the same. From the table, we can observe that the MTP strategy consistently enhances the model performance on most of the evaluation benchmarks.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Ablation Studies for the Auxiliary-Loss-Free Balancing Strategy", "weight": 1.0} -->

In Table, we show the ablation results for the auxiliary-loss-free balancing strategy. We validate this strategy on top of two baseline models across different scales. At the small scale, we train a baseline MoE model comprising 15.7B total parameters on 1.33T tokens. At the large scale, we train a baseline MoE model comprising 228.7B total parameters on 578B tokens. Both of the baseline models purely use auxiliary losses to encourage load balance, and use the sigmoid gating function with top-K affinity normalization. Their hyper-parameters to control the strength of auxiliary losses are the same as DeepSeek-V2-Lite and DeepSeek-V2, respectively. On top of these two baseline models, keeping the training data and the other architectures the same, we remove all auxiliary losses and introduce the auxiliary-loss-free balancing strategy for comparison. From the table, we can observe that the auxiliary-loss-free strategy consistently achieves better model performance on most of the evaluation benchmarks.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Batch-Wise Load Balance VS. Sequence-Wise Load Balance", "weight": 1.0} -->

The key distinction between auxiliary-loss-free balancing and sequence-wise auxiliary loss lies in their balancing scope: batch-wise versus sequence-wise. Compared with the sequence-wise auxiliary loss, batch-wise balancing imposes a more flexible constraint, as it does not enforce in-domain balance on each sequence. This flexibility allows experts to better specialize in different domains. To validate this, we record and analyze the expert load of a 16B auxiliary-loss-based baseline and a 16B auxiliary-loss-free model on different domains in the Pile test set. As illustrated in Figure, we observe that the auxiliary-loss-free model demonstrates greater expert specialization patterns as expected.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Batch-Wise Load Balance VS. Sequence-Wise Load Balance", "weight": 1.0} -->

To further investigate the correlation between this flexibility and the advantage in model performance, we additionally design and validate a batch-wise auxiliary loss that encourages load balance on each training batch instead of on each sequence. The experimental results show that, when achieving a similar level of batch-wise load balance, the batch-wise auxiliary loss can also achieve similar model performance to the auxiliary-loss-free method. To be specific, in our experiments with 1B MoE models, the validation losses are: 2.258 (using a sequence-wise auxiliary loss), 2.253 (using the auxiliary-loss-free method), and 2.253 (using a batch-wise auxiliary loss). We also observe similar results on 3B MoE models: the model using a sequence-wise auxiliary loss achieves a validation loss of 2.085, and the models using the auxiliary-loss-free method or a batch-wise auxiliary loss achieve the same validation loss of 2.080.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Batch-Wise Load Balance VS. Sequence-Wise Load Balance", "weight": 1.0} -->

In addition, although the batch-wise load balancing methods show consistent performance advantages, they also face two potential challenges in efficiency: load imbalance within certain sequences or small batches, and domain-shift-induced load imbalance during inference. The first challenge is naturally addressed by our training framework that uses large-scale expert parallelism and data parallelism, which guarantees a large size of each micro-batch. For the second challenge, we also design and implement an efficient inference framework with redundant expert deployment, as described in Section 3.4, to overcome it.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Supervised Fine-Tuning", "weight": 1.0} -->

We curate our instruction-tuning datasets to include 1.5M instances spanning multiple domains, with each domain employing distinct data creation methods tailored to its specific requirements.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Reasoning Data", "weight": 1.0} -->

For reasoning-related datasets, including those focused on mathematics, code competition problems, and logic puzzles, we generate the data by leveraging an internal DeepSeek-R1 model. Specifically, while the R1-generated data demonstrates strong accuracy, it suffers from issues such as overthinking, poor formatting, and excessive length. Our objective is to balance the high accuracy of R1-generated reasoning data and the clarity and conciseness of regularly formatted reasoning data.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Reasoning Data", "weight": 1.0} -->

To establish our methodology, we begin by developing an expert model tailored to a specific domain, such as code, mathematics, or general reasoning, using a combined Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) training pipeline. This expert model serves as a data generator for the final model. The training process involves generating two distinct types of SFT samples for each instance: the first couples the problem with its original response in the format of \<problem, original response\>, while the second incorporates a system prompt alongside the problem and the R1 response in the format of \.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Reasoning Data", "weight": 1.0} -->

The system prompt is meticulously designed to include instructions that guide the model toward producing responses enriched with mechanisms for reflection and verification. During the RL phase, the model leverages high-temperature sampling to generate responses that integrate patterns from both the R1-generated and original data, even in the absence of explicit system prompts. After hundreds of RL steps, the intermediate RL model learns to incorporate R1 patterns, thereby enhancing overall performance strategically.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Reasoning Data", "weight": 1.0} -->

Upon completing the RL training phase, we implement rejection sampling to curate high-quality SFT data for the final model, where the expert models are used as data generation sources. This method ensures that the final training data retains the strengths of DeepSeek-R1 while producing responses that are concise and effective.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Non-Reasoning Data", "weight": 1.0} -->

For non-reasoning data, such as creative writing, role-play, and simple question answering, we utilize DeepSeek-V2.5 to generate responses and enlist human annotators to verify the accuracy and correctness of the data.

<!-- chunk {"id": "body-0134", "role": "body", "section": "SFT Settings", "weight": 1.0} -->

We fine-tune DeepSeek-V3-Base for two epochs using the SFT dataset, using the cosine decay learning rate scheduling that starts at $5 \times 10^{- 6}$ and gradually decreases to $1 \times 10^{- 6}$. During training, each single sequence is packed from multiple samples. However, we adopt a sample masking strategy to ensure that these examples remain isolated and mutually invisible.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Reward Model", "weight": 1.0} -->

We employ a rule-based Reward Model (RM) and a model-based RM in our RL process.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Rule-Based RM", "weight": 1.0} -->

For questions that can be validated using specific rules, we adopt a rule-based reward system to determine the feedback. For instance, certain math problems have deterministic results, and we require the model to provide the final answer within a designated format (e.g., in a box), allowing us to apply rules to verify the correctness. Similarly, for LeetCode problems, we can utilize a compiler to generate feedback based on test cases. By leveraging rule-based validation wherever possible, we ensure a higher level of reliability, as this approach is resistant to manipulation or exploitation.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Model-Based RM", "weight": 1.0} -->

For questions with free-form ground-truth answers, we rely on the reward model to determine whether the response matches the expected ground-truth. Conversely, for questions without a definitive ground-truth, such as those involving creative writing, the reward model is tasked with providing feedback based on the question and the corresponding answer as inputs. The reward model is trained from the DeepSeek-V3 SFT checkpoints. To enhance its reliability, we construct preference data that not only provides the final reward but also includes the chain-of-thought leading to the reward. This approach helps mitigate the risk of reward hacking in specific tasks.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Group Relative Policy Optimization", "weight": 1.0} -->

Similar to DeepSeek-V2, we adopt Group Relative Policy Optimization (GRPO), which foregoes the critic model that is typically with the same size as the policy model, and estimates the baseline from group scores instead.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Group Relative Policy Optimization", "weight": 1.0} -->

We incorporate prompts from diverse domains, such as coding, math, writing, role-playing, and question answering, during the RL process. This approach not only aligns the model more closely with human preferences but also enhances performance on benchmarks, especially in scenarios where available SFT data are limited.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Evaluation Benchmarks", "weight": 1.0} -->

Apart from the benchmark we used for base model testing, we further evaluate instructed models on IFEval, FRAMES, LongBench v2, GPQA, SimpleQA, C-SimpleQA, SWE-Bench Verified, Aider ^11^1 LiveCodeBench, Codeforces ^22^2 Chinese National High School Mathematics Olympiad ^33^3 and American Invitational Mathematics Examination 2024.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Compared Baselines", "weight": 1.0} -->

We conduct comprehensive evaluations of our chat model against several strong baselines, including DeepSeek-V2-0506, DeepSeek-V2.5-0905, Qwen2.5 72B Instruct, LLaMA-3.1 405B Instruct, Claude-Sonnet-3.5-1022, and GPT-4o-0513. For the DeepSeek-V2 model series, we select the most representative variants for comparison. For closed-source models, evaluations are performed through their respective APIs.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Detailed Evaluation Configurations", "weight": 1.0} -->

For standard benchmarks including MMLU, DROP, GPQA, and SimpleQA, we adopt the evaluation prompts from the simple-evals framework^44^4 We utilize the Zero-Eval prompt format for MMLU-Redux in a zero-shot setting. For other datasets, we follow their original evaluation protocols with default prompts as provided by the dataset creators. For code and math benchmarks, the HumanEval-Mul dataset includes 8 mainstream programming languages (Python, Java, Cpp, C#, JavaScript, TypeScript, PHP, and Bash) in total. We use CoT and non-CoT methods to evaluate model performance on LiveCodeBench, where the data are collected from August 2024 to November 2024. The Codeforces dataset is measured using the percentage of competitors. SWE-Bench verified is evaluated using the agentless framework. We use the "diff" format to evaluate the Aider-related benchmarks. For mathematical assessments, AIME and CNMO 2024 are evaluated with a temperature of 0.7, and the results are averaged over 16 runs, while MATH-500 employs greedy decoding.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Detailed Evaluation Configurations", "weight": 1.0} -->

We allow all models to output a maximum of 8192 tokens for each benchmark.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Standard Evaluation", "weight": 1.0} -->

Table presents the evaluation results, showcasing that DeepSeek-V3 stands as the best-performing open-source model. Additionally, it is competitive against frontier closed-source models like GPT-4o and Claude-3.5-Sonnet.

<!-- chunk {"id": "body-0145", "role": "body", "section": "English Benchmarks", "weight": 1.0} -->

MMLU is a widely recognized benchmark designed to assess the performance of large language models, across diverse knowledge domains and tasks. DeepSeek-V3 demonstrates competitive performance, standing on par with top-tier models such as LLaMA-3.1-405B, GPT-4o, and Claude-Sonnet 3.5, while significantly outperforming Qwen2.5 72B. Moreover, DeepSeek-V3 excels in MMLU-Pro, a more challenging educational knowledge benchmark, where it closely trails Claude-Sonnet 3.5. On MMLU-Redux, a refined version of MMLU with corrected labels, DeepSeek-V3 surpasses its peers. In addition, on GPQA-Diamond, a PhD-level evaluation testbed, DeepSeek-V3 achieves remarkable results, ranking just behind Claude 3.5 Sonnet and outperforming all other competitors by a substantial margin.

<!-- chunk {"id": "body-0146", "role": "body", "section": "English Benchmarks", "weight": 1.0} -->

In long-context understanding benchmarks such as DROP, LongBench v2, and FRAMES, DeepSeek-V3 continues to demonstrate its position as a top-tier model. It achieves an impressive 91.6 F1 score in the 3-shot setting on DROP, outperforming all other models in this category. On FRAMES, a benchmark requiring question-answering over 100k token contexts, DeepSeek-V3 closely trails GPT-4o while outperforming all other models by a significant margin. This demonstrates the strong capability of DeepSeek-V3 in handling extremely long-context tasks. The long-context capability of DeepSeek-V3 is further validated by its best-in-class performance on LongBench v2, a dataset that was released just a few weeks before the launch of DeepSeek V3. On the factual knowledge benchmark, SimpleQA, DeepSeek-V3 falls behind GPT-4o and Claude-Sonnet, primarily due to its design focus and resource allocation. DeepSeek-V3 assigns more training tokens to learn Chinese knowledge, leading to exceptional performance on the C-SimpleQA.

<!-- chunk {"id": "body-0147", "role": "body", "section": "English Benchmarks", "weight": 1.0} -->

On the instruction-following benchmark, DeepSeek-V3 significantly outperforms its predecessor, DeepSeek-V2-series, highlighting its improved ability to understand and adhere to user-defined format constraints.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Code and Math Benchmarks", "weight": 1.0} -->

Coding is a challenging and practical task for LLMs, encompassing engineering-focused tasks like SWE-Bench-Verified and Aider, as well as algorithmic tasks such as HumanEval and LiveCodeBench. In engineering tasks, DeepSeek-V3 trails behind Claude-Sonnet-3.5-1022 but significantly outperforms open-source models. The open-source DeepSeek-V3 is expected to foster advancements in coding-related engineering tasks. By providing access to its robust capabilities, DeepSeek-V3 can drive innovation and improvement in areas such as software engineering and algorithm development, empowering developers and researchers to push the boundaries of what open-source models can achieve in coding tasks. In algorithmic tasks, DeepSeek-V3 demonstrates superior performance, outperforming all baselines on benchmarks like HumanEval-Mul and LiveCodeBench. This success can be attributed to its advanced knowledge distillation technique, which effectively enhances its code generation and problem-solving capabilities in algorithm-focused tasks.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Code and Math Benchmarks", "weight": 1.0} -->

On math benchmarks, DeepSeek-V3 demonstrates exceptional performance, significantly surpassing baselines and setting a new state-of-the-art for non-o1-like models. Specifically, on AIME, MATH-500, and CNMO 2024, DeepSeek-V3 outperforms the second-best model, Qwen2.5 72B, by approximately 10% in absolute scores, which is a substantial margin for such challenging benchmarks. This remarkable capability highlights the effectiveness of the distillation technique from DeepSeek-R1, which has been proven highly beneficial for non-o1-like models.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Chinese Benchmarks", "weight": 1.0} -->

Qwen and DeepSeek are two representative model series with robust support for both Chinese and English. On the factual benchmark Chinese SimpleQA, DeepSeek-V3 surpasses Qwen2.5-72B by 16.4 points, despite Qwen2.5 being trained on a larger corpus compromising 18T tokens, which are 20% more than the 14.8T tokens that DeepSeek-V3 is pre-trained.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Chinese Benchmarks", "weight": 1.0} -->

On C-Eval, a representative benchmark for Chinese educational knowledge evaluation, and CLUEWSC (Chinese Winograd Schema Challenge), DeepSeek-V3 and Qwen2.5-72B exhibit similar performance levels, indicating that both models are well-optimized for challenging Chinese-language reasoning and educational tasks.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Open-Ended Evaluation", "weight": 1.0} -->

In addition to standard benchmarks, we also evaluate our models on open-ended generation tasks using LLMs as judges, with the results shown in Table. Specifically, we adhere to the original configurations of AlpacaEval 2.0 and Arena-Hard, which leverage GPT-4-Turbo-1106 as judges for pairwise comparisons. On Arena-Hard, DeepSeek-V3 achieves an impressive win rate of over 86% against the baseline GPT-4-0314, performing on par with top-tier models like Claude-Sonnet-3.5-1022. This underscores the robust capabilities of DeepSeek-V3, especially in dealing with complex prompts, including coding and debugging tasks. Furthermore, DeepSeek-V3 achieves a groundbreaking milestone as the first open-source model to surpass 85% on the Arena-Hard benchmark. This achievement significantly bridges the performance gap between open-source and closed-source models, setting a new standard for what open-source models can accomplish in challenging domains.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Open-Ended Evaluation", "weight": 1.0} -->

Similarly, DeepSeek-V3 showcases exceptional performance on AlpacaEval 2.0, outperforming both closed-source and open-source models. This demonstrates its outstanding proficiency in writing tasks and handling straightforward question-answering scenarios. Notably, it surpasses DeepSeek-V2.5-0905 by a significant margin of 20%, highlighting substantial improvements in tackling simple tasks and showcasing the effectiveness of its advancements.

<!-- chunk {"id": "body-0154", "role": "body", "section": "DeepSeek-V3 as a Generative Reward Model", "weight": 1.0} -->

We compare the judgment ability of DeepSeek-V3 with state-of-the-art models, namely GPT-4o and Claude-3.5. Table presents the performance of these models in RewardBench. DeepSeek-V3 achieves performance on par with the best versions of GPT-4o-0806 and Claude-3.5-Sonnet-1022, while surpassing other versions. Additionally, the judgment ability of DeepSeek-V3 can also be enhanced by the voting technique. Therefore, we employ DeepSeek-V3 along with voting to offer self-feedback on open-ended questions, thereby improving the effectiveness and robustness of the alignment process.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Distillation from DeepSeek-R1", "weight": 1.0} -->

We ablate the contribution of distillation from DeepSeek-R1 based on DeepSeek-V2.5. The baseline is trained on short CoT data, whereas its competitor uses data generated by the expert checkpoints described above.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Distillation from DeepSeek-R1", "weight": 1.0} -->

Table demonstrates the effectiveness of the distillation data, showing significant improvements in both LiveCodeBench and MATH-500 benchmarks. Our experiments reveal an interesting trade-off: the distillation leads to better performance but also substantially increases the average response length. To maintain a balance between model accuracy and computational efficiency, we carefully selected optimal settings for DeepSeek-V3 in distillation.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Distillation from DeepSeek-R1", "weight": 1.0} -->

Our research suggests that knowledge distillation from reasoning models presents a promising direction for post-training optimization. While our current work focuses on distilling data from mathematics and coding domains, this approach shows potential for broader applications across various task domains. The effectiveness demonstrated in these specific areas indicates that long-CoT distillation could be valuable for enhancing model performance in other cognitive tasks requiring complex reasoning. Further exploration of this approach across different domains remains an important direction for future research.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Self-Rewarding", "weight": 1.0} -->

Rewards play a pivotal role in RL, steering the optimization process. In domains where verification through external tools is straightforward, such as some coding or mathematics scenarios, RL demonstrates exceptional efficacy. However, in more general scenarios, constructing a feedback mechanism through hard coding is impractical. During the development of DeepSeek-V3, for these broader contexts, we employ the constitutional AI approach, leveraging the voting evaluation results of DeepSeek-V3 itself as a feedback source. This method has produced notable alignment effects, significantly enhancing the performance of DeepSeek-V3 in subjective evaluations. By integrating additional constitutional inputs, DeepSeek-V3 can optimize towards the constitutional direction. We believe that this paradigm, which combines supplementary information with LLMs as a feedback source, is of paramount importance. The LLM serves as a versatile processor capable of transforming unstructured information from diverse scenarios into rewards, ultimately facilitating the self-improvement of LLMs. Beyond self-rewarding, we are also dedicated to uncovering other general and scalable rewarding methods to consistently advance the model capabilities in general scenarios.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Multi-Token Prediction Evaluation", "weight": 1.0} -->

Instead of predicting just the next single token, DeepSeek-V3 predicts the next 2 tokens through the MTP technique. Combined with the framework of speculative decoding (Leviathan et al. Xia et al., ), it can significantly accelerate the decoding speed of the model. A natural question arises concerning the acceptance rate of the additionally predicted token. Based on our evaluation, the acceptance rate of the second token prediction ranges between 85% and 90% across various generation topics, demonstrating consistent reliability. This high acceptance rate enables DeepSeek-V3 to achieve a significantly improved decoding speed, delivering 1.8 times TPS (Tokens Per Second).

<!-- chunk {"id": "body-0160", "role": "body", "section": "Conclusion, Limitations, and Future Directions", "weight": 1.5} -->

In this paper, we introduce DeepSeek-V3, a large MoE language model with 671B total parameters and 37B activated parameters, trained on 14.8T tokens. In addition to the MLA and DeepSeekMoE architectures, it also pioneers an auxiliary-loss-free strategy for load balancing and sets a multi-token prediction training objective for stronger performance. The training of DeepSeek-V3 is cost-effective due to the support of FP8 training and meticulous engineering optimizations. The post-training also makes a success in distilling the reasoning capability from the DeepSeek-R1 series of models. Comprehensive evaluations demonstrate that DeepSeek-V3 has emerged as the strongest open-source model currently available, and achieves performance comparable to leading closed-source models like GPT-4o and Claude-3.5-Sonnet. Despite its strong performance, it also maintains economical training costs. It requires only 2.788M H800 GPU hours for its full training, including pre-training, context length extension, and post-training.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Conclusion, Limitations, and Future Directions", "weight": 1.5} -->

While acknowledging its strong performance and cost-effectiveness, we also recognize that DeepSeek-V3 has some limitations, especially on the deployment. Firstly, to ensure efficient inference, the recommended deployment unit for DeepSeek-V3 is relatively large, which might pose a burden for small-sized teams. Secondly, although our deployment strategy for DeepSeek-V3 has achieved an end-to-end generation speed of more than two times that of DeepSeek-V2, there still remains potential for further enhancement. Fortunately, these limitations are expected to be naturally addressed with the development of more advanced hardware.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Conclusion, Limitations, and Future Directions", "weight": 1.5} -->

DeepSeek consistently adheres to the route of open-source models with longtermism, aiming to steadily approach the ultimate goal of AGI (Artificial General Intelligence). In the future, we plan to strategically invest in research across the following directions.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Conclusion, Limitations, and Future Directions", "weight": 1.5} -->

We will consistently study and refine our model architectures, aiming to further improve both the training and inference efficiency, striving to approach efficient support for infinite context length. Additionally, we will try to break through the architectural limitations of Transformer, thereby pushing the boundaries of its modeling capabilities.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Conclusion, Limitations, and Future Directions", "weight": 1.5} -->

We will continuously iterate on the quantity and quality of our training data, and explore the incorporation of additional training signal sources, aiming to drive data scaling across a more comprehensive range of dimensions.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Conclusion, Limitations, and Future Directions", "weight": 1.5} -->

We will consistently explore and iterate on the deep thinking capabilities of our models, aiming to enhance their intelligence and problem-solving abilities by expanding their reasoning length and depth.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Conclusion, Limitations, and Future Directions", "weight": 1.5} -->

We will explore more comprehensive and multi-dimensional model evaluation methods to prevent the tendency towards optimizing a fixed set of benchmarks during research, which may create a misleading impression of the model capabilities and affect our foundational assessment.
