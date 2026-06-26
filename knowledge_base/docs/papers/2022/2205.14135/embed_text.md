## Introduction

Transformer models have emerged as the most widely used architecture in applications such as natural language processing and image classification. Transformers have grown larger and deeper, but equipping them with longer context remains difficult, since the self-attention module at their heart has time and memory complexity quadratic in sequence length. An important question is whether making attention faster and more memory-efficient can help Transformer models address their runtime and memory challenges for long sequences.

Many approximate attention methods have aimed to reduce the compute and memory requirements of attention. These methods range from sparse-approximation to low-rank approximation, and their combinations. Although these methods reduce the compute requirements to linear or near-linear in sequence length, many of them do not display wall-clock speedup against standard attention and have not gained wide adoption. One main reason is that they focus on FLOP reduction (which may not correlate with wall-clock speed) and tend to ignore overheads from memory access (IO).

Figure 1: Left: FlashAttention uses tiling to prevent materialization of the large N × N attention matrix (dotted box) on (relatively) slow GPU HBM. In the outer loop (red arrows), FlashAttention loops through blocks of the K and V matrices and loads them to fast on-chip SRAM. In each block, FlashAttention loops over blocks of Q matrix (blue arrows), loading them to SRAM, and writing the output of the attention computation back to HBM. Right: Speedup over the PyTorch implementation of attention on GPT-2. FlashAttention does not read and write the large N × N attention matrix to HBM, resulting in an 7.6× speedup on the attention computation.

In this paper, we argue that a missing principle is making attention algorithms IO-aware ---that is, carefully accounting for reads and writes to different levels of fast and slow memory (e.g., between fast GPU on-chip SRAM and relatively slow GPU high bandwidth memory, or HBM, Figure 1 left). On modern GPUs, compute speed has out-paced memory speed, and most operations in Transformers are bottlenecked by memory accesses. IO-aware algorithms have been critical for similar memory-bound operations, when reading and writing data can account for a large portion of the runtime---such as database joins, image processing, numerical linear algebra, and more. However, common Python interfaces to deep learning such as PyTorch and Tensorflow do not allow fine-grained control of memory access.

We propose FlashAttention, a new attention algorithm that computes exact attention with far fewer memory accesses. Our main goal is to avoid reading and writing the attention matrix to and from HBM. This requires (i) computing the softmax reduction without access to the whole input (ii) not storing the large intermediate attention matrix for the backward pass. We apply two well-established techniques to address these challenges. (i) We restructure the attention computation to split the input into blocks and make several passes over input blocks, thus incrementally performing the softmax reduction (also known as tiling). (ii) We store the softmax normalization factor from the forward pass to quickly recompute attention on-chip in the backward pass, which is faster than the standard approach of reading the intermediate attention matrix from HBM. We implement FlashAttention in CUDA to achieve fine-grained control over memory access and fuse all the attention operations into one GPU kernel. Even with the increased FLOPs due to recomputation, our algorithm both runs faster (up to 7.6x on GPT-2, Figure 1 right) and uses less memory---linear in sequence length---than standard attention, thanks to the massively reduced amount of HBM access.

We analyze the IO complexity of FlashAttention, proving that it requires $O{({N^{2}d^{2}M^{- 1}})}$ HBM accesses where $d$ is the head dimension and $M$ is the size of SRAM, as compared to $\Omega{({{Nd} + N^{2}})}$ of standard attention. For typical values of $d$ and $M$, FlashAttention requires many times fewer HBM accesses compared to standard attention (up to 9$\times$ fewer, as shown in Fig. 2). Moreover, we provide a lower bound, showing that no exact attention algorithm can asymptotically improve on the number of HBM accesses over all SRAM sizes.

We also show that FlashAttention can serve as a useful primitive for realizing the potential of approximate attention algorithms by overcoming their issues with memory access overhead. As a proof of concept, we implement block-sparse FlashAttention, a sparse attention algorithm that is 2-4$\times$ faster than even FlashAttention, scaling up to sequence length of 64k. We prove that block-sparse FlashAttention has better IO complexity than FlashAttention by a factor proportional to the sparsity ratio. We discuss further extensions to other operations (attention on multi-GPU, kernel regression, block-sparse matrix multiply) in Section 5. We open-source FlashAttention to make it easier to build on this primitive.^11^1FlashAttention code is available at We empirically validate that FlashAttention speeds up model training and improves model quality by modeling longer context. We also benchmark the runtime and memory footprint of FlashAttention and block-sparse FlashAttention compared to prior attention implementations.

Faster Model Training. FlashAttention trains Transformer models faster in wall-clock time. We train BERT-large (seq. length 512) 15% faster than the training speed record in MLPerf 1.1, GPT2 (seq. length 1K) 3$\times$ faster than baseline implementations from HuggingFace and Megatron-LM, and long-range arena (seq. length 1K-4K) 2.4$\times$ faster than baselines.

Higher Quality Models. FlashAttention scales Transformers to longer sequences, which improves their quality and enables new capabilities. We observe a 0.7 improvement in perplexity on GPT-2 and 6.4 points of lift from modeling longer sequences on long-document classification. FlashAttention enables the first Transformer that can achieve better-than-chance performance on the Path-X challenge, solely from using a longer sequence length (16K). Block-sparse FlashAttention enables a Transformer to scale to even longer sequences (64K), resulting in the first model that can achieve better-than-chance performance on Path-256.

Benchmarking Attention. FlashAttention is up to 3$\times$ faster than the standard attention implementation across common sequence lengths from 128 to 2K and scales up to 64K. Up to sequence length of 512, FlashAttention is both faster and more memory-efficient than any existing attention method, whereas for sequence length beyond 1K, some approximate attention methods (e.g., Linformer) start to become faster. On the other hand, block-sparse FlashAttention is faster than all existing approximate attention methods that we know of.

## Background

We provide some background on the performance characteristics of common deep learning operations on modern hardware (GPUs). We also describe the standard implementation of attention.

### Hardware Performance

We focus here on GPUs. Performance on other hardware accelerators are similar.

GPU Memory Hierarchy. The GPU memory hierarchy (Fig. 1 left) comprises multiple forms of memory of different sizes and speeds, with smaller memory being faster. As an example, the A100 GPU has 40-80GB of high bandwidth memory (HBM) with bandwidth 1.5-2.0TB/s and 192KB of on-chip SRAM per each of 108 streaming multiprocessors with bandwidth estimated around 19TB/s. The on-chip SRAM is an order of magnitude faster than HBM but many orders of magnitude smaller in size. As compute has gotten faster relative to memory speed, operations are increasingly bottlenecked by memory (HBM) accesses. Thus exploiting fast SRAM becomes more important.

Execution Model. GPUs have a massive number of threads to execute an operation (called a kernel). Each kernel loads inputs from HBM to registers and SRAM, computes, then writes outputs to HBM.

Performance characteristics. Depending on the balance of computation and memory accesses, operations can be classified as either compute-bound or memory-bound. This is commonly measured by the *arithmetic intensity*, which is the number of arithmetic operations per byte of memory access.

Compute-bound: the time taken by the operation is determined by how many arithmetic operations there are, while time accessing HBM is much smaller. Typical examples are matrix multiply with large inner dimension, and convolution with large number of channels.

Memory-bound: the time taken by the operation is determined by the number of memory accesses, while time spent in computation is much smaller. Examples include most other operations: elementwise (e.g., activation, dropout), and reduction (e.g., sum, softmax, batch norm, layer norm).

Kernel fusion. The most common approach to accelerate memory-bound operations is kernel fusion: if there are multiple operations applied to the same input, the input can be loaded once from HBM, instead of multiple times for each operation. Compilers can automatically fuse many elementwise operations. However, in the context of model training, the intermediate values still need to be written to HBM to save for the backward pass, reducing the effectiveness of naive kernel fusion.

### Standard Attention Implementation

Given input sequences ${\mathbf{Q},\mathbf{K},\mathbf{V}} \in {\mathbb{R}}^{N \times d}$ where $N$ is the sequence length and $d$ is the head dimension, we want to compute the attention output $\mathbf{O} \in {\mathbb{R}}^{N \times d}$: where $softmax$ is applied row-wise.

Standard attention implementations materialize the matrices $\mathbf{S}$ and $\mathbf{P}$ to HBM, which takes $O{(N^{2})}$ memory. Often $N \gg d$ (e.g., for GPT2, $N = 1024$ and $d = 64$). We describe the standard attention implementation in Algorithm. As some or most of the operations are memory-bound (e.g., softmax), the large number of memory accesses translates to slow wall-clock time.

This problem is exacerbated by other elementwise operations applied to the attention matrix, such as masking applied to $\mathbf{S}$ or dropout applied to $\mathbf{P}$. As a result, there have been many attempts to fuse several elementwise operations, such as fusing masking with softmax.

In Section 3.2, we will show that the standard attention implementation performs HBM accesses quadratic in the sequence length $N$. We also compare the number of FLOPs and number of HBM accesses of standard attention and of our method (FlashAttention).

1: Load Q, K by blocks from HBM, compute S = QK⊤, write S to HBM. 2: Read S from HBM, compute P = softmax (S), write P to HBM. 3: Load P and V by blocks from HBM, compute O = PV, write O to HBM. Algorithm 0 Standard Attention Implementation

## FlashAttention: Algorithm, Analysis, and Extensions

We show how to compute exact attention with fewer HBM reads/writes and without storing large intermediate matrices for the backward pass. This yields an attention algorithm that is both memory efficient and faster in wall-clock time. We analyze its IO complexity, showing that our method requires much fewer HBM accesses compared to standard attention. We further show that FlashAttention can serve as a useful primitive by extending it to handle block-sparse attention.

We focus here on the forward pass for ease of exposition; Appendix B contains details for the backward.

### An Efficient Attention Algorithm With Tiling and Recomputation

Given the inputs ${\mathbf{Q},\mathbf{K},\mathbf{V}} \in {\mathbb{R}}^{N \times d}$ in HBM, we aim to compute the attention output $\mathbf{O} \in {\mathbb{R}}^{N \times d}$ and write it to HBM. Our goal is to reduce the amount of HBM accesses (to sub-quadratic in $N$).

We apply two established techniques (tiling, recomputation) to overcome the technical challenge of computing exact attention in sub-quadratic HBM accesses. We describe this in Algorithm 1. The main idea is that we split the inputs $\mathbf{Q},\mathbf{K},\mathbf{V}$ into blocks, load them from slow HBM to fast SRAM, then compute the attention output with respect to those blocks. By scaling the output of each block by the right normalization factor before adding them up, we get the correct result at the end.

Tiling. We compute attention by blocks. Softmax couples columns of $\mathbf{K}$, so we decompose the large softmax with scaling. For numerical stability, the softmax of vector $x \in {\mathbb{R}}^{B}$ is computed as: For vectors ${x^{},x^{}} \in {\mathbb{R}}^{B}$, we can decompose the softmax of the concatenated $x = \begin{bmatrix} \end{bmatrix} \in {\mathbb{R}}^{2B}$ as: Therefore if we keep track of some extra statistics (${m{(x)}},{\ell{(x)}}$), we can compute softmax one block at a time.^22^2This style of aggregation is called *algebraic aggregation*. We thus split the inputs $\mathbf{Q},\mathbf{K},\mathbf{V}$ into blocks (Algorithm 1 line 3), compute the softmax values along with extra statistics (Algorithm 1 line 10), and combine the results (Algorithm 1 line 12).

Recomputation. One of our goals is to not store $O{(N^{2})}$ intermediate values for the backward pass. The backward pass typically requires the matrices ${\mathbf{S},\mathbf{P}} \in {\mathbb{R}}^{N \times N}$ to compute the gradients with respect to $\mathbf{Q},\mathbf{K},\mathbf{V}$. However, by storing the output $\mathbf{O}$ and the softmax normalization statistics $(m,\ell)$, we can recompute the attention matrix $\mathbf{S}$ and $\mathbf{P}$ easily in the backward pass from blocks of $\mathbf{Q},\mathbf{K},\mathbf{V}$ in SRAM. This can be seen as a form of selective gradient checkpointing. While gradient checkpointing has been suggested to reduce the maximum amount of memory required, all implementations (that we know off) have to trade speed for memory. In contrast, even with more FLOPs, our recomputation speeds up the backward pass due to reduced HBM accesses (Fig. 2). The full backward pass description is in Appendix B.

Implementation details: Kernel fusion. Tiling enables us to implement our algorithm in one CUDA kernel, loading input from HBM, performing all the computation steps (matrix multiply, softmax, optionally masking and dropout, matrix multiply), then write the result back to HBM (masking and dropout in Appendix B). This avoids repeatedly reading and writing of inputs and outputs from and to HBM.

0: Matrices Q, K, V ∈ ℝN × d in HBM, on-chip SRAM of size M. 1: Set block sizes ${B_{c} = \left\lceil \frac{M}{4d} \right\rceil},{B_{r} = {\min\left(\left\lceil \frac{M}{4d} \right\rceil,d \right)}}$. 3: Divide Q into $T_{r} = \left\lceil \frac{N}{B_{r}} \right\rceil$ blocks Q1, …, QTr of size Br × d each, and divide K, V in to $T_{c} = \left\lceil \frac{N}{B_{c}} \right\rceil$ blocks K1, …, KTc and V1, …, VTc, of size Bc × d each. 4: Divide O into Tr blocks Oi, …, OTr of size Br × d each, divide ℓ into Tr blocks ℓi, …, ℓTr of size Br each, divide m into Tr blocks m1, …, mTr of size Br each. 6: Load Kj, Vj from HBM to on-chip SRAM. 8: Load Qi, Oi, ℓi, mi from HBM to on-chip SRAM. 9: On chip, compute Si j = Qi KjT ∈ ℝBr × Bc. 10: On chip, compute ${\overset{\sim}{m}}_{ij} = {{rowmax}{(\mathbf{S}_{ij})}} \in {\mathbb{R}}^{B_{r}}$, ${\overset{\sim}{\mathbf{P}}}_{ij} = {\exp{({\mathbf{S}_{ij} - {\overset{\sim}{m}}_{ij}})}} \in {\mathbb{R}}^{B_{r} \times B_{c}}$ (pointwise), ${\overset{\sim}{\ell}}_{ij} = {{rowsum}{({\overset{\sim}{\mathbf{P}}}_{ij})}} \in {\mathbb{R}}^{B_{r}}$. 11: On chip, compute $m_{i}^{new} = {\max{(m_{i},{\overset{\sim}{m}}_{ij})}} \in {\mathbb{R}}^{B_{r}}$, $\ell_{i}^{new} = {{e^{m_{i} - m_{i}^{new}}\ell_{i}} + {e^{{\overset{\sim}{m}}_{ij} - m_{i}^{new}}{\overset{\sim}{\ell}}_{ij}}} \in {\mathbb{R}}^{B_{r}}$. 12: Write $\mathbf{O}_{i}\leftarrow{{diag}{(\ell_{i}^{new})}^{- 1}{({{{diag}{(\ell_{i})}e^{m_{i} - m_{i}^{new}}\mathbf{O}_{i}} + {e^{{\overset{\sim}{m}}_{ij} - m_{i}^{new}}{\overset{\sim}{\mathbf{P}}}_{ij}\mathbf{V}_{j}}})}}$ to HBM. 13: Write ℓi ← ℓinew, mi ← minew to HBM.

We show FlashAttention's correctness, runtime, and memory requirement (proof in Appendix C).

### Theorem 1

Algorithm 1 returns $\mathbf{O} = {{softmax}{({\mathbf{Q}\mathbf{K}}^{\top})}\mathbf{V}}$ with $O{({N^{2}d})}$ FLOPs and requires $O{(N)}$ additional memory beyond inputs and output.

### Analysis: IO Complexity of FlashAttention

We analyze the IO complexity of FlashAttention, showing significant reduction in HBM accesses compared to standard attention. We also provide a lower bound, proving that no exact attention algorithm can asymptotically improve on HBM accesses over all SRAM sizes. Proofs are in Appendix C.

### Theorem 2

Let $N$ be the sequence length, $d$ be the head dimension, and $M$ be size of SRAM with $d \leq M \leq {Nd}$. Standard attention (Algorithm ) requires $\Theta{({{Nd} + N^{2}})}$ HBM accesses, while FlashAttention (Algorithm 1) requires $\Theta{({N^{2}d^{2}M^{- 1}})}$ HBM accesses.

For typical values of $d$ (64-128) and $M$ (around 100KB), $d^{2}$ is many times smaller than $M$, and thus FlashAttention requires many times fewer HBM accesses than standard implementation. This leads to both faster execution and lower memory footprint, which we validate in Section 4.3.

The main idea of the proof is that given the SRAM size of $M$, we can load blocks of $\mathbf{K},\mathbf{V}$ of size $\Theta{(M)}$ each (Algorithm 1 line 6). For each block of $\mathbf{K}$ and $\mathbf{V}$, we iterate over all blocks of $\mathbf{Q}$ (Algorithm 1 line 8) to compute the intermediate values, resulting in $\Theta{({NdM^{- 1}})}$ passes over $\mathbf{Q}$. Each pass loads $\Theta{({Nd})}$ elements, which amounts to $\Theta{({N^{2}d^{2}M^{- 1}})}$ HBM accesses. We similarly prove that the backward pass of standard attention requires $\Theta{({{Nd} + N^{2}})}$ HBM accesses while the backward pass of FlashAttention requires $\Theta{({N^{2}d^{2}M^{- 1}})}$ HBM accesses (Appendix B).

We prove a lower-bound: one cannot asymptotically improve on the number of HBM accesses for all values of $M$ (the SRAM size) when computing exact attention.

### Proposition 3

Let $N$ be the sequence length, $d$ be the head dimension, and $M$ be size of SRAM with $d \leq M \leq {Nd}$. There does not exist an algorithm to compute exact attention with $o{({N^{2}d^{2}M^{- 1}})}$ HBM accesses for all $M$ in the range $\lbrack d,{Nd}\rbrack$.

The proof relies on the fact that for $M = {\Theta{({Nd})}}$ any algorithm must perform ${\Omega{({N^{2}d^{2}M^{- 1}})}} = {\Omega{({Nd})}}$ HBM accesses. This type of lower bound over a subrange of $M$ is common in the streaming algorithms literature. We leave proving parameterized complexity lower bounds in terms of $M$ as exciting future work.

We validate that the number of HBM accesses is the main determining factor of attention run-time. In Fig. 2 (left), we see that even though FlashAttention has higher FLOP count compared to standard attention (due to recomputation in the backward pass), it has much fewer HBM accesses, resulting in much faster runtime. In Fig. 2 (middle), we vary the block size $B_{c}$ of FlashAttention, which results in different amounts of HBM accesses, and measure the runtime of the forward pass. As block size increases, the number of HBM accesses decreases (as we make fewer passes over the input), and runtime decreases. For large enough block size (beyond 256), the runtime is then bottlenecked by other factors (e.g., arithmetic operations). Moreover, larger block size will not fit into the small SRAM size.

Figure 2: Left: Forward + backward runtime of standard attention and FlashAttention for GPT-2 medium (seq. length 1024, head dim. 64, 16 heads, batch size 64) on A100 GPU. HBM access is the primary factor affecting runtime. Middle: Forward runtime of FlashAttention (seq. length 1024, head dim. 64, 16 heads, batch size 64) on A100 GPU. Fewer HBM accesses result in faster runtime, up to a point. Right: The runtime (for seq. length 4K) of block-sparse FlashAttention is faster than FlashAttention by a factor proportional to the sparsity.

### Extension: Block-Sparse FlashAttention

We extend FlashAttention to approximate attention: we propose block-sparse FlashAttention, whose IO complexity is smaller than FlashAttention by a factor proportional to the sparsity.

Given inputs ${\mathbf{Q},\mathbf{K},\mathbf{V}} \in {\mathbb{R}}^{N \times d}$ and a mask matrix $\overset{\sim}{\mathbf{M}} \in {\{ 0,1\}}^{N \times N}$, we want to compute: where ${({{\mathbf{S} \odot}1_{\overset{\sim}{\mathbf{M}}}})}_{kl} = \mathbf{S}_{kl}$ if ${\overset{\sim}{\mathbf{M}}}_{kl} = 1$ and $- \infty$ if $\mathbf{M}_{kl} = 0$. We require $\overset{\sim}{\mathbf{M}}$ to have block form: for some block sizes $B_{r},B_{c}$, for all $k,l$, ${\overset{\sim}{\mathbf{M}}}_{k,l} = \mathbf{M}_{ij}$ with ${i = {\lfloor{k/B_{r}}\rfloor}},{j = {\lfloor{l/B_{c}}\rfloor}}$ for some $\mathbf{M} \in {\{ 0,1\}}^{{{N/B_{r}} \times N}/B_{c}}$.

Given a predefined block sparsity mask $\mathbf{M} \in {\{ 0,1\}}^{{{N/B_{r}} \times N}/B_{c}}$ we can easily adapt Algorithm 1 to only compute the nonzero blocks of the attention matrix. The algorithm is identical to Algorithm 1, except we skip zero blocks. We reproduce the algorithm description in Algorithm 5 in Appendix B.

We also analyze the IO complexity of block-sparse FlashAttention.

### Proposition 4

Let $N$ be the sequence length, $d$ be the head dimension, and $M$ be size of SRAM with $d \leq M \leq {Nd}$. Block-sparse FlashAttention (Algorithm 5) requires $\Theta{({{Nd} + {N^{2}d^{2}M^{- 1}s}})}$ HBM accesses where $s$ is the fraction of nonzero blocks in the block-sparsity mask.

We see that applying block-sparsity yields a direct improvement by the sparsity to the larger term in the IO complexity. For large sequence lengths $N$, $s$ is often set to $N^{- {1/2}}$ or $N^{- 1}{\log N}$, resulting in $\Theta{({N\sqrt{N}})}$ or $\Theta{({N{\log N}})}$ IO complexity. For downstream experiments, we use the fixed butterfly sparsity pattern, which has been shown to be able to approximate arbitrary sparsity.

In Fig. 2 (right), we validate that as the sparsity increases, the runtime of block-sparse FlashAttention improves proportionally. On the LRA benchmark, block-sparse FlashAttention achieves 2.8$\times$ speedup, while performing on par with standard attention (Section 4).

## Experiments

We evaluate the impact of using FlashAttention to train Transformer models. We validate two claims about training time and model accuracy, and report attention runtime and memory benchmarks.

Training Speed. FlashAttention outperforms the MLPerf 1.1 speed record for BERT by 15%, and speeds up GPT-2 up to 3$\times$ over HuggingFace and $1.8 \times$ over Megatron over standard Transformers. FlashAttention speeds up the long-range arena (LRA) benchmark 2.4$\times$.

Quality. FlashAttention scales Transformers to longer sequences, yielding higher quality. FlashAttention trains GPT-2 with context length 4K faster than Megatron trains GPT-2 with context length 1K, while achieving 0.7 better perplexity. Modeling longer sequences yields 6.4 points of lift on two long-document classification tasks. Finally, FlashAttention yields the first Transformer that can achieve better-than-random performance on the challenging Path-X task (sequence length 16K), and block-sparse FlashAttention yields the first sequence model that we know of that can achieve better-than-random performance on Path-256 (sequence length 64K).

Benchmarking Attention. We measure the runtime and memory performance of FlashAttention and block-sparse FlashAttention based on sequence length. We confirm that the memory footprint of FlashAttention scales linearly with seq. length and is up to 3$\times$ faster than standard attention for common seq. lengths (up to 2K). We confirm that runtime of block-sparse FlashAttention scales linearly in seq. length and is faster than all existing approximate attention baselines.

Additional experiment details are in Appendix E.

### Faster Models with FlashAttention

### BERT

FlashAttention yields the fastest single-node BERT training speed that we know of. We train a BERT-large model with FlashAttention on Wikipedia. Table 1 compares our training time to the implementation from Nvidia that set the training speed record for MLPerf 1.1. Our implementation is 15% faster.

Training time (minutes) Table 1: Training time of BERT-large, starting from the same initialization provided by the MLPerf benchmark, to reach the target accuracy of 72.0% on masked language modeling. Averaged over 10 runs on 8×A100 GPUs.

### GPT-2

FlashAttention yields faster training times for GPT-2 on the large OpenWebtext dataset than the widely used HuggingFace and Megatron-LM implementations. Table 2 shows up to 3$\times$ end-to-end speedup compared to Huggingface and 1.7$\times$ speedup compared to Megatron-LM. FlashAttention achieves the same perplexity as the other two implementations, as we do not change the model definition. Appendix E includes plots of the validation perplexity throughout training, confirming that FlashAttention is as numerically stable as the baselines and produces the same training / validation curves.

Training time (speedup) GPT-2 small - Huggingface GPT-2 small - Megatron-LM GPT-2 small - FlashAttention GPT-2 medium - Huggingface GPT-2 medium - Megatron-LM GPT-2 medium - FlashAttention Table 2: GPT-2 small and medium using FlashAttention achieve up to 3× speed up compared to Huggingface implementation and up to 1.7× compared to Megatron-LM. Training time reported on 8×A100s GPUs.

### Long-range Arena

We compare vanilla Transformer (with either standard implementation or FlashAttention) on the long-range arena (LRA ) benchmark. We measure accuracy, throughput, and training time of all models. Each task has a different sequence length varying between 1024 and 4096. We follow the implementation and experimental setting in Tay et al. and Xiong et al..^33^3LRA accuracy results are known to be highly dependent on the tuning procedure. Our reproduced baselines perform better than as reported in the original comparison. Table 3 shows that FlashAttention achieves up 2.4$\times$ speed-up compared to standard attention. Block-sparse FlashAttention is faster than all of the approximate attention methods that we have tested.

Table 3: The performance of standard attention, FlashAttention, block-sparse FlashAttention, and approximate attention baselines on the Long-Range-Arena benchmarks.

### Better Models with Longer Sequences

### Language Modeling with Long Context

The runtime and memory-efficiency of FlashAttention allow us to increase the context length of GPT-2 by 4$\times$ while still running faster than the optimized implementation from Megatron-LM. Table 4 shows that that GPT-2 with FlashAttention and context length 4K is still 30% faster than GPT-2 from Megatron with context length 1K, while achieving 0.7 better perplexity.

Training time (speedup) GPT-2 small - Megatron-LM GPT-2 small - FlashAttention GPT-2 small - FlashAttention GPT-2 small - FlashAttention Table 4: GPT-2 small with FlashAttention, with 4× larger context length compared to Megatron-LM, is still 30% faster while achieving 0.7 better perplexity. Training time on 8×A100 GPUs is reported.

### Long Document Classification

Training Transformers with longer sequences with FlashAttention improves performance on the MIMIC-III and ECtHR datasets. MIMIC-III contains intensive care unit patient discharge summaries, each annotated with multiple labels. ECtHR contains legal cases from the European Court of Human Rights, each of which is mapped to articles of the Convention of Human Rights that were allegedly violaged. Both of these datasets contain very long text documents; the average number of tokens in MIMIC is 2,395 tokens, and the longest document contains 14,562 tokens, while the average and longest numbers in ECtHR are 2,197 and 49,392, respectively. We evaluate lift from increasing the sequence length of a pretrained RoBERTa model (we repeat the positional embeddings, as in Beltagy et al. ).

Table 6 shows that sequence length 16K outperforms length 512 by 4.3 points on MIMIC, and that length 8K outperforms length 512 by 8.5 points on ECtHR. The discrepancies may be due to subtle distribution shifts: MIMIC-III contains specialized medical text and thus may be more susceptible to a distribution shift in the document length, whereas ECtHR contains general language.

Table 5: Long Document performance (micro F1) at different sequence lengths using FlashAttention.

Table 6: We report the first Transformer model that can achieve non-random performance on Path-X and Path-256.

### Path-X and Path-256

The Path-X and Path-256 benchmarks are challenging tasks from the long-range arena benchmark designed to test long context. The task is to classify whether two points in a black and white 128$\times$`<!-- -->`{=html}128 (or 256$\times$`<!-- -->`{=html}256) image have a path connecting them, and the images are fed to the transformer one pixel at a time. In prior work, all transformer models have either run out of memory, or only achieved random performance. There has been a search for alternative architectures that can model such long context. We present here the first result of Transformer models being able to solve Path-X and Path-256 (Table 6). We pretrain a transformer on Path-64, and then transfer to Path-X by spatially interpolating the positional embeddings. FlashAttention achieves 61.4 accuracy on Path-X. Additionally, block-sparse FlashAttention enables the Transformers to scale to sequence length 64K, achieving 63.1 accuracy^44^4Path-256 requires longer sequences but has relatively shorter paths than Path-X, so it is easier to obtain a higher accuracy. on Path-256.

### Benchmarking Attention

Figure 3: Left: runtime of forward pass + backward pass. Right: attention memory usage.

We vary sequence length and measure runtime and memory usage of FlashAttention and block-sparse FlashAttention against various attention baselines on one A100 GPU with 40 GB HBM, with dropout and a padding mask. We compare against reference implementations for exact attention, approximate attention, and sparse attention. We report a subset of baselines in the main body; Appendix E contains more baselines and full details.

### Runtime

Figure 3 (left) reports the runtime in milliseconds of the forward + backward pass of FlashAttention and block-sparse FlashAttention compared to the baselines in exact, approximate, and sparse attention (exact numbers in Appendix E). Runtime grows quadratically with sequence length, but FlashAttention runs significantly faster than exact attention baselines, up to 3$\times$ faster than the PyTorch implementation. The runtimes of many approximate/sparse attention mechanisms grow linearly with sequence length, but FlashAttention still runs faster than approximate and sparse attention for short sequences due to fewer memory accesses. The approximate attention runtimes begin to cross over with FlashAttention at sequences between 512 and 1024. On the other hand, block-sparse FlashAttention is faster than all implementations of exact, sparse, and approximate attention that we know of, across all sequence lengths.

### Memory Footprint

Figure 3 (right) shows the memory footprint of FlashAttention and block-sparse FlashAttention compared to various exact, approximate, and sparse attention baselines. FlashAttention and block-sparse FlashAttention have the same memory footprint, which grows linearly with sequence length. FlashAttention is up to 20$\times$ more memory efficient than exact attention baselines, and is more memory-efficient than the approximate attention baselines. All other algorithms except for Linformer run out of memory on an A100 GPU before 64K, and FlashAttention is still 2$\times$ more efficient than Linformer.

## Limitations and Future Directions

We discuss limitations of our approach and future directions. Related work is given in Appendix A.

Compiling to CUDA. Our current approach to building IO-aware implementations of attention requires writing a new CUDA kernel for each new attention implementation. This requires writing the attention algorithm in a considerably lower-level language than PyTorch, and requires significant engineering effort. Implementations may also not be transferrable across GPU architectures. These limitations suggest the need for a method that supports writing attention algorithms in a high-level language (e.g., PyTorch), and compiling to IO-aware implementations in CUDA---similar to efforts such as Halide in image processing.

IO-Aware Deep Learning. We believe that the IO-aware approach can extend beyond attention. Attention is the most memory-intensive computation in Transformers, but every layer in a deep network touches GPU HBM. We hope our work inspires IO-aware implementations of additional modules. We discuss these potential extensions in Appendix D.

Multi-GPU IO-Aware Methods. Our IO-aware implementation of attention is optimal within constants for computing attention on a single GPU. However, the attention computation may be parallelizable across multiple GPUs. Using multiple GPUs adds an additional layer to IO analysis---accounting for data transfer between GPUs. We hope our work inspires future work in this direction.
