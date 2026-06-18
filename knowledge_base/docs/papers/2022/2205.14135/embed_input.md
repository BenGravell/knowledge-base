<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

Topics include Transformers, Attention mechanisms, Classification, Accuracy, FlashAttention, Graphics processing unit, High bandwidth memory, HBM.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length. Approximate attention methods have attempted to address this problem by trading off model quality to reduce the compute complexity, but often do not achieve wall-clock speedup. We argue that a missing principle is making attention algorithms IO-aware - accounting for reads and writes between levels of GPU memory. We propose FlashAttention, an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM. We analyze the IO complexity of FlashAttention, showing that it requires fewer HBM accesses than standard attention, and is optimal for a range of SRAM sizes. We also extend FlashAttention to block-sparse attention, yielding an approximate attention algorithm that is faster than any existing approximate attention method. FlashAttention trains Transformers faster than existing baselines: 15% end-to-end wall-clock speedup on BERT-large (seq.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

length 512) compared to the MLPerf 1.1 training speed record, 3x speedup on GPT-2 (seq. length 1K), and 2.4x speedup on long-range arena (seq. length 1K-4K). FlashAttention and block-sparse FlashAttention enable longer context in Transformers, yielding higher quality models (0.7 better perplexity on GPT-2 and 6.4 points of lift on long-document classification) and entirely new capabilities: the first Transformers to achieve better-than-chance performance on the Path-X challenge (seq. length 16K, 61.4% accuracy) and Path-256 (seq. length 64K, 63.1% accuracy).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Transformer models have emerged as the most widely used architecture in applications such as natural language processing and image classification. Transformers have grown larger and deeper, but equipping them with longer context remains difficult, since the self-attention module at their heart has time and memory complexity quadratic in sequence length. An important question is whether making attention faster and more memory-efficient can help Transformer models address their runtime and memory challenges for long sequences.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many approximate attention methods have aimed to reduce the compute and memory requirements of attention. These methods range from sparse-approximation to low-rank approximation, and their combinations. Although these methods reduce the compute requirements to linear or near-linear in sequence length, many of them do not display wall-clock speedup against standard attention and have not gained wide adoption. One main reason is that they focus on FLOP reduction (which may not correlate with wall-clock speed) and tend to ignore overheads from memory access (IO).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we argue that a missing principle is making attention algorithms IO-aware ---that is, carefully accounting for reads and writes to different levels of fast and slow memory (e.g., between fast GPU on-chip SRAM and relatively slow GPU high bandwidth memory, or HBM, Figure 1 left). On modern GPUs, compute speed has out-paced memory speed, and most operations in Transformers are bottlenecked by memory accesses. IO-aware algorithms have been critical for similar memory-bound operations, when reading and writing data can account for a large portion of the runtime---such as database joins, image processing, numerical linear algebra, and more. However, common Python interfaces to deep learning such as PyTorch and Tensorflow do not allow fine-grained control of memory access.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose FlashAttention, a new attention algorithm that computes exact attention with far fewer memory accesses. Our main goal is to avoid reading and writing the attention matrix to and from HBM. This requires (i) computing the softmax reduction without access to the whole input (ii) not storing the large intermediate attention matrix for the backward pass. We apply two well-established techniques to address these challenges. (i) We restructure the attention computation to split the input into blocks and make several passes over input blocks, thus incrementally performing the softmax reduction (also known as tiling). (ii) We store the softmax normalization factor from the forward pass to quickly recompute attention on-chip in the backward pass, which is faster than the standard approach of reading the intermediate attention matrix from HBM. We implement FlashAttention in CUDA to achieve fine-grained control over memory access and fuse all the attention operations into one GPU kernel.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Even with the increased FLOPs due to recomputation, our algorithm both runs faster (up to 7.6x on GPT-2, Figure 1 right) and uses less memory---linear in sequence length---than standard attention, thanks to the massively reduced amount of HBM access.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We analyze the IO complexity of FlashAttention, proving that it requires $O{({N^{2}d^{2}M^{- 1}})}$ HBM accesses where $d$ is the head dimension and $M$ is the size of SRAM, as compared to $\Omega{({{Nd} + N^{2}})}$ of standard attention. For typical values of $d$ and $M$, FlashAttention requires many times fewer HBM accesses compared to standard attention (up to 9$\times$ fewer, as shown in Fig. 2). Moreover, we provide a lower bound, showing that no exact attention algorithm can asymptotically improve on the number of HBM accesses over all SRAM sizes.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We also show that FlashAttention can serve as a useful primitive for realizing the potential of approximate attention algorithms by overcoming their issues with memory access overhead. As a proof of concept, we implement block-sparse FlashAttention, a sparse attention algorithm that is 2-4$\times$ faster than even FlashAttention, scaling up to sequence length of 64k. We prove that block-sparse FlashAttention has better IO complexity than FlashAttention by a factor proportional to the sparsity ratio. We discuss further extensions to other operations (attention on multi-GPU, kernel regression, block-sparse matrix multiply) in Section 5. We open-source FlashAttention to make it easier to build on this primitive.^11^1FlashAttention code is available at

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We empirically validate that FlashAttention speeds up model training and improves model quality by modeling longer context. We also benchmark the runtime and memory footprint of FlashAttention and block-sparse FlashAttention compared to prior attention implementations.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Faster Model Training. FlashAttention trains Transformer models faster in wall-clock time. We train BERT-large (seq. length 512) 15% faster than the training speed record in MLPerf 1.1, GPT2 (seq. length 1K) 3$\times$ faster than baseline implementations from HuggingFace and Megatron-LM, and long-range arena (seq. length 1K-4K) 2.4$\times$ faster than baselines.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Higher Quality Models. FlashAttention scales Transformers to longer sequences, which improves their quality and enables new capabilities. We observe a 0.7 improvement in perplexity on GPT-2 and 6.4 points of lift from modeling longer sequences on long-document classification. FlashAttention enables the first Transformer that can achieve better-than-chance performance on the Path-X challenge, solely from using a longer sequence length (16K). Block-sparse FlashAttention enables a Transformer to scale to even longer sequences (64K), resulting in the first model that can achieve better-than-chance performance on Path-256.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Benchmarking Attention. FlashAttention is up to 3$\times$ faster than the standard attention implementation across common sequence lengths from 128 to 2K and scales up to 64K. Up to sequence length of 512, FlashAttention is both faster and more memory-efficient than any existing attention method, whereas for sequence length beyond 1K, some approximate attention methods (e.g., Linformer) start to become faster. On the other hand, block-sparse FlashAttention is faster than all existing approximate attention methods that we know of.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Hardware Performance", "weight": 1.0} -->

We focus here on GPUs. Performance on other hardware accelerators are similar.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Hardware Performance", "weight": 1.0} -->

GPU Memory Hierarchy. The GPU memory hierarchy (Fig. 1 left) comprises multiple forms of memory of different sizes and speeds, with smaller memory being faster. As an example, the A100 GPU has 40-80GB of high bandwidth memory (HBM) with bandwidth 1.5-2.0TB/s and 192KB of on-chip SRAM per each of 108 streaming multiprocessors with bandwidth estimated around 19TB/s. The on-chip SRAM is an order of magnitude faster than HBM but many orders of magnitude smaller in size. As compute has gotten faster relative to memory speed, operations are increasingly bottlenecked by memory (HBM) accesses. Thus exploiting fast SRAM becomes more important.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Hardware Performance", "weight": 1.0} -->

Execution Model. GPUs have a massive number of threads to execute an operation (called a kernel). Each kernel loads inputs from HBM to registers and SRAM, computes, then writes outputs to HBM.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Hardware Performance", "weight": 1.0} -->

Performance characteristics. Depending on the balance of computation and memory accesses, operations can be classified as either compute-bound or memory-bound. This is commonly measured by the *arithmetic intensity*, which is the number of arithmetic operations per byte of memory access.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Hardware Performance", "weight": 1.0} -->

Compute-bound: the time taken by the operation is determined by how many arithmetic operations there are, while time accessing HBM is much smaller. Typical examples are matrix multiply with large inner dimension, and convolution with large number of channels.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Hardware Performance", "weight": 1.0} -->

Memory-bound: the time taken by the operation is determined by the number of memory accesses, while time spent in computation is much smaller. Examples include most other operations: elementwise (e.g., activation, dropout), and reduction (e.g., sum, softmax, batch norm, layer norm).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Hardware Performance", "weight": 1.0} -->

Kernel fusion. The most common approach to accelerate memory-bound operations is kernel fusion: if there are multiple operations applied to the same input, the input can be loaded once from HBM, instead of multiple times for each operation. Compilers can automatically fuse many elementwise operations. However, in the context of model training, the intermediate values still need to be written to HBM to save for the backward pass, reducing the effectiveness of naive kernel fusion.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Standard Attention Implementation", "weight": 1.0} -->

Standard attention implementations materialize the matrices $\mathbf{S}$ and $\mathbf{P}$ to HBM, which takes $O{(N^{2})}$ memory. Often $N \gg d$ (e.g., for GPT2, $N = 1024$ and $d = 64$). We describe the standard attention implementation in Algorithm. As some or most of the operations are memory-bound (e.g., softmax), the large number of memory accesses translates to slow wall-clock time.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Standard Attention Implementation", "weight": 1.0} -->

This problem is exacerbated by other elementwise operations applied to the attention matrix, such as masking applied to $\mathbf{S}$ or dropout applied to $\mathbf{P}$. As a result, there have been many attempts to fuse several elementwise operations, such as fusing masking with softmax.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Standard Attention Implementation", "weight": 1.0} -->

In Section 3.2, we will show that the standard attention implementation performs HBM accesses quadratic in the sequence length $N$. We also compare the number of FLOPs and number of HBM accesses of standard attention and of our method (FlashAttention).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Standard Attention Implementation", "weight": 1.0} -->

1: Load Q, K by blocks from HBM, compute S = QK⊤, write S to HBM.
2: Read S from HBM, compute P = softmax (S), write P to HBM.
3: Load P and V by blocks from HBM, compute O = PV, write O to HBM.
Algorithm 0 Standard Attention Implementation

<!-- chunk {"id": "body-0026", "role": "body", "section": "FlashAttention: Algorithm, Analysis, and Extensions", "weight": 1.0} -->

We show how to compute exact attention with fewer HBM reads/writes and without storing large intermediate matrices for the backward pass. This yields an attention algorithm that is both memory efficient and faster in wall-clock time. We analyze its IO complexity, showing that our method requires much fewer HBM accesses compared to standard attention. We further show that FlashAttention can serve as a useful primitive by extending it to handle block-sparse attention.

<!-- chunk {"id": "body-0027", "role": "body", "section": "FlashAttention: Algorithm, Analysis, and Extensions", "weight": 1.0} -->

We focus here on the forward pass for ease of exposition; Appendix B contains details for the backward.

<!-- chunk {"id": "body-0028", "role": "body", "section": "An Efficient Attention Algorithm With Tiling and Recomputation", "weight": 1.0} -->

Given the inputs ${\mathbf{Q},\mathbf{K},\mathbf{V}} \in {\mathbb{R}}^{N \times d}$ in HBM, we aim to compute the attention output $\mathbf{O} \in {\mathbb{R}}^{N \times d}$ and write it to HBM. Our goal is to reduce the amount of HBM accesses (to sub-quadratic in $N$).

<!-- chunk {"id": "body-0029", "role": "body", "section": "An Efficient Attention Algorithm With Tiling and Recomputation", "weight": 1.0} -->

We apply two established techniques (tiling, recomputation) to overcome the technical challenge of computing exact attention in sub-quadratic HBM accesses. We describe this in Algorithm 1. The main idea is that we split the inputs $\mathbf{Q},\mathbf{K},\mathbf{V}$ into blocks, load them from slow HBM to fast SRAM, then compute the attention output with respect to those blocks. By scaling the output of each block by the right normalization factor before adding them up, we get the correct result at the end.

<!-- chunk {"id": "body-0030", "role": "body", "section": "An Efficient Attention Algorithm With Tiling and Recomputation", "weight": 1.0} -->

Tiling. We compute attention by blocks. Softmax couples columns of $\mathbf{K}$, so we decompose the large softmax with scaling.

<!-- chunk {"id": "body-0031", "role": "body", "section": "An Efficient Attention Algorithm With Tiling and Recomputation", "weight": 1.0} -->

Therefore if we keep track of some extra statistics (${m{(x)}},{\ell{(x)}}$), we can compute softmax one block at a time.^22^2This style of aggregation is called *algebraic aggregation*. We thus split the inputs $\mathbf{Q},\mathbf{K},\mathbf{V}$ into blocks (Algorithm 1 line 3), compute the softmax values along with extra statistics (Algorithm 1 line 10), and combine the results (Algorithm 1 line 12).

<!-- chunk {"id": "body-0032", "role": "body", "section": "An Efficient Attention Algorithm With Tiling and Recomputation", "weight": 1.0} -->

Recomputation. One of our goals is to not store $O{(N^{2})}$ intermediate values for the backward pass. The backward pass typically requires the matrices ${\mathbf{S},\mathbf{P}} \in {\mathbb{R}}^{N \times N}$ to compute the gradients with respect to $\mathbf{Q},\mathbf{K},\mathbf{V}$. However, by storing the output $\mathbf{O}$ and the softmax normalization statistics $(m,\ell)$, we can recompute the attention matrix $\mathbf{S}$ and $\mathbf{P}$ easily in the backward pass from blocks of $\mathbf{Q},\mathbf{K},\mathbf{V}$ in SRAM. This can be seen as a form of selective gradient checkpointing. While gradient checkpointing has been suggested to reduce the maximum amount of memory required, all implementations (that we know off) have to trade speed for memory.

<!-- chunk {"id": "body-0033", "role": "body", "section": "An Efficient Attention Algorithm With Tiling and Recomputation", "weight": 1.0} -->

In contrast, even with more FLOPs, our recomputation speeds up the backward pass due to reduced HBM accesses (Fig. 2). The full backward pass description is in Appendix B.

<!-- chunk {"id": "body-0034", "role": "body", "section": "An Efficient Attention Algorithm With Tiling and Recomputation", "weight": 1.0} -->

Implementation details: Kernel fusion. Tiling enables us to implement our algorithm in one CUDA kernel, loading input from HBM, performing all the computation steps (matrix multiply, softmax, optionally masking and dropout, matrix multiply), then write the result back to HBM (masking and dropout in Appendix B). This avoids repeatedly reading and writing of inputs and outputs from and to HBM.

<!-- chunk {"id": "body-0035", "role": "body", "section": "An Efficient Attention Algorithm With Tiling and Recomputation", "weight": 1.0} -->

We show FlashAttention's correctness, runtime, and memory requirement (proof in Appendix C).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Analysis: IO Complexity of FlashAttention", "weight": 1.0} -->

We analyze the IO complexity of FlashAttention, showing significant reduction in HBM accesses compared to standard attention. We also provide a lower bound, proving that no exact attention algorithm can asymptotically improve on HBM accesses over all SRAM sizes. Proofs are in Appendix C.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Extension: Block-Sparse FlashAttention", "weight": 1.0} -->

We extend FlashAttention to approximate attention: we propose block-sparse FlashAttention, whose IO complexity is smaller than FlashAttention by a factor proportional to the sparsity.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Extension: Block-Sparse FlashAttention", "weight": 1.0} -->

Given a predefined block sparsity mask $\mathbf{M} \in {\{ 0,1\}}^{{{N/B_{r}} \times N}/B_{c}}$ we can easily adapt Algorithm 1 to only compute the nonzero blocks of the attention matrix. The algorithm is identical to Algorithm 1, except we skip zero blocks. We reproduce the algorithm description in Algorithm 5 in Appendix B.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Extension: Block-Sparse FlashAttention", "weight": 1.0} -->

We also analyze the IO complexity of block-sparse FlashAttention.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate the impact of using FlashAttention to train Transformer models. We validate two claims about training time and model accuracy, and report attention runtime and memory benchmarks.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments", "weight": 1.0} -->

Training Speed. FlashAttention outperforms the MLPerf 1.1 speed record for BERT by 15%, and speeds up GPT-2 up to 3$\times$ over HuggingFace and $1.8 \times$ over Megatron over standard Transformers. FlashAttention speeds up the long-range arena (LRA) benchmark 2.4$\times$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

Quality. FlashAttention scales Transformers to longer sequences, yielding higher quality. FlashAttention trains GPT-2 with context length 4K faster than Megatron trains GPT-2 with context length 1K, while achieving 0.7 better perplexity. Modeling longer sequences yields 6.4 points of lift on two long-document classification tasks. Finally, FlashAttention yields the first Transformer that can achieve better-than-random performance on the challenging Path-X task (sequence length 16K), and block-sparse FlashAttention yields the first sequence model that we know of that can achieve better-than-random performance on Path-256 (sequence length 64K).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

Benchmarking Attention. We measure the runtime and memory performance of FlashAttention and block-sparse FlashAttention based on sequence length. We confirm that the memory footprint of FlashAttention scales linearly with seq. length and is up to 3$\times$ faster than standard attention for common seq. lengths (up to 2K). We confirm that runtime of block-sparse FlashAttention scales linearly in seq. length and is faster than all existing approximate attention baselines.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experiments", "weight": 1.0} -->

Additional experiment details are in Appendix E.

<!-- chunk {"id": "body-0045", "role": "body", "section": "BERT", "weight": 1.0} -->

FlashAttention yields the fastest single-node BERT training speed that we know of. We train a BERT-large model with FlashAttention on Wikipedia. Table 1 compares our training time to the implementation from Nvidia that set the training speed record for MLPerf 1.1. Our implementation is 15% faster.

<!-- chunk {"id": "body-0046", "role": "body", "section": "GPT-2", "weight": 1.0} -->

FlashAttention yields faster training times for GPT-2 on the large OpenWebtext dataset than the widely used HuggingFace and Megatron-LM implementations. Table 2 shows up to 3$\times$ end-to-end speedup compared to Huggingface and 1.7$\times$ speedup compared to Megatron-LM. FlashAttention achieves the same perplexity as the other two implementations, as we do not change the model definition. Appendix E includes plots of the validation perplexity throughout training, confirming that FlashAttention is as numerically stable as the baselines and produces the same training / validation curves.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Long-range Arena", "weight": 1.0} -->

We compare vanilla Transformer (with either standard implementation or FlashAttention) on the long-range arena (LRA ) benchmark. We measure accuracy, throughput, and training time of all models. Each task has a different sequence length varying between 1024 and 4096. We follow the implementation and experimental setting in Tay et al. and Xiong et al..^33^3LRA accuracy results are known to be highly dependent on the tuning procedure. Our reproduced baselines perform better than as reported in the original comparison. Table 3 shows that FlashAttention achieves up 2.4$\times$ speed-up compared to standard attention. Block-sparse FlashAttention is faster than all of the approximate attention methods that we have tested.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Language Modeling with Long Context", "weight": 1.0} -->

The runtime and memory-efficiency of FlashAttention allow us to increase the context length of GPT-2 by 4$\times$ while still running faster than the optimized implementation from Megatron-LM. Table 4 shows that that GPT-2 with FlashAttention and context length 4K is still 30% faster than GPT-2 from Megatron with context length 1K, while achieving 0.7 better perplexity.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Long Document Classification", "weight": 1.0} -->

Training Transformers with longer sequences with FlashAttention improves performance on the MIMIC-III and ECtHR datasets. MIMIC-III contains intensive care unit patient discharge summaries, each annotated with multiple labels. ECtHR contains legal cases from the European Court of Human Rights, each of which is mapped to articles of the Convention of Human Rights that were allegedly violaged. Both of these datasets contain very long text documents; the average number of tokens in MIMIC is 2,395 tokens, and the longest document contains 14,562 tokens, while the average and longest numbers in ECtHR are 2,197 and 49,392, respectively. We evaluate lift from increasing the sequence length of a pretrained RoBERTa model (we repeat the positional embeddings, as in Beltagy et al. ).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Long Document Classification", "weight": 1.0} -->

Table 6 shows that sequence length 16K outperforms length 512 by 4.3 points on MIMIC, and that length 8K outperforms length 512 by 8.5 points on ECtHR. The discrepancies may be due to subtle distribution shifts: MIMIC-III contains specialized medical text and thus may be more susceptible to a distribution shift in the document length, whereas ECtHR contains general language.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Path-X and Path-256", "weight": 1.0} -->

The Path-X and Path-256 benchmarks are challenging tasks from the long-range arena benchmark designed to test long context. The task is to classify whether two points in a black and white 128$\times$`<!-- -->`{=html}128 (or 256$\times$`<!-- -->`{=html}256) image have a path connecting them, and the images are fed to the transformer one pixel at a time. In prior work, all transformer models have either run out of memory, or only achieved random performance. There has been a search for alternative architectures that can model such long context. We present here the first result of Transformer models being able to solve Path-X and Path-256 (Table 6). We pretrain a transformer on Path-64, and then transfer to Path-X by spatially interpolating the positional embeddings.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Path-X and Path-256", "weight": 1.0} -->

FlashAttention achieves 61.4 accuracy on Path-X. Additionally, block-sparse FlashAttention enables the Transformers to scale to sequence length 64K, achieving 63.1 accuracy^44^4Path-256 requires longer sequences but has relatively shorter paths than Path-X, so it is easier to obtain a higher accuracy. on Path-256.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Benchmarking Attention", "weight": 1.0} -->

We vary sequence length and measure runtime and memory usage of FlashAttention and block-sparse FlashAttention against various attention baselines on one A100 GPU with 40 GB HBM, with dropout and a padding mask. We compare against reference implementations for exact attention, approximate attention, and sparse attention. We report a subset of baselines in the main body; Appendix E contains more baselines and full details.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Limitations and Future Directions", "weight": 1.5} -->

We discuss limitations of our approach and future directions. Related work is given in Appendix A.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Limitations and Future Directions", "weight": 1.5} -->

Compiling to CUDA. Our current approach to building IO-aware implementations of attention requires writing a new CUDA kernel for each new attention implementation. This requires writing the attention algorithm in a considerably lower-level language than PyTorch, and requires significant engineering effort. Implementations may also not be transferrable across GPU architectures. These limitations suggest the need for a method that supports writing attention algorithms in a high-level language (e.g., PyTorch), and compiling to IO-aware implementations in CUDA---similar to efforts such as Halide in image processing.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Limitations and Future Directions", "weight": 1.5} -->

IO-Aware Deep Learning. We believe that the IO-aware approach can extend beyond attention. Attention is the most memory-intensive computation in Transformers, but every layer in a deep network touches GPU HBM. We hope our work inspires IO-aware implementations of additional modules. We discuss these potential extensions in Appendix D.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Limitations and Future Directions", "weight": 1.5} -->

Multi-GPU IO-Aware Methods. Our IO-aware implementation of attention is optimal within constants for computing attention on a single GPU. However, the attention computation may be parallelizable across multiple GPUs. Using multiple GPUs adds an additional layer to IO analysis---accounting for data transfer between GPUs. We hope our work inspires future work in this direction.
