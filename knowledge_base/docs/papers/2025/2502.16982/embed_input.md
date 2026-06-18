<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Muon Is Scalable for LLM Training

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recently, the Muon optimizer based on matrix orthogonalization has demonstrated strong results in training small-scale language models, but the scalability to larger models has not been proven. We identify two crucial techniques for scaling up Muon: adding weight decay and carefully adjusting the per-parameter update scale. These techniques allow Muon to work out-of-the-box on large-scale training without the need of hyper-parameter tuning. Scaling law experiments indicate that Muon achieves ~ 2x computational efficiency compared to AdamW with compute optimal training. Based on these improvements, we introduce Moonlight, a 3B/16B-parameter Mixture-of-Expert (MoE) model trained with 5.7T tokens using Muon. Our model improves the current Pareto frontier, achieving better performance with much fewer training FLOPs compared to prior models. We open-source our distributed Muon implementation that is memory optimal and communication efficient. We also release the pretrained, instruction-tuned, and intermediate checkpoints to support future research.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rapid advancement of large language models (LLMs) \[undefab, undefh, undefj, undefaj\] has significantly pushed forward the progress in artificial general intelligence. However, training capable LLMs remains a computationally intensive and resource-demanding process due to scaling laws \[undefq, undefm\]. Optimizers play a crucial role in efficiently and effectively training of LLMs, with Adam \[undefr\] and its variant AdamW \[undefz\] being the standard choice for most large-scale training.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent developments in optimization algorithms have shown potential to improve training efficiency beyond AdamW \[undefy, undefo, undefar, undefam, undefu, undefv, undefad, undefx, undefw, undefac\]. Among these, \[undefo\] proposed Muon, which updates matrix parameters with orthogonalized gradient momentum using Newton-Schulz iteration. Initial experiments with Muon have demonstrated promising results in small-scale language model training. However, as discussed in this blog \[undefo\], several critical challenges remain unaddressed: how to effectively scale optimizers based on matrix orthogonalization to larger models with billions of parameters trained with trillions of tokens, how to compute approximate orthogonalization in a distributed setting, and whether such optimizers can generalize across different training stages including pre-training and supervised finetuning (SFT).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this technical report, we present a comprehensive study addressing these challenges. Our work builds upon Muon while systematically identifying and resolving its limitations in large-scale training scenarios.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Analysis for Effective Scaling of Muon: Through extensive analysis, we identify that weight decay plays a crucial role in Muon's scalability. Besides, we propose scale adjustments to Muon's parameter-wise update rule. Such adjustments allow Muon to work out-of-the-box without hyper-parameter tuning, and also significantly improve training stability.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Efficient Distributed Implementation: We develop a distributed version of Muon with ZeRO-1 \[undefae\] style optimization, achieving optimal memory efficiency and reduced communication overhead while preserving the mathematical properties of the algorithm.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Scaling Law Validation: We performed scaling law research that compares Muon with strong AdamW baselines, and showed the superior performance of Muon (1(a)). Based on the scaling law results, Muon achieves comparable performance to AdamW trained counterparts while requiring only approximately 52% of the training FLOPs.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our comprehensive experiments demonstrate that Muon can effectively replace AdamW as the de facto optimizer for large-scale LLM training, offering significant improvements in both training efficiency and model performance. As a result of this work, we release Moonlight, a 16B-parameter MoE model trained using Muon, along with our implementation and intermediate training checkpoints to facilitate further research in scalable optimization techniques for LLMs.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The Muon Optimizer", "weight": 1.0} -->

Muon \[undefo\] has recently been proposed to optimize neural network weights representable as matrices.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The Muon Optimizer", "weight": 1.0} -->

Here, $\mathbf{M}_{t}$ is the momentum of gradient at iteration $t$, set as a zero matrix when $t = 0$. In Equation 1, a Newton-Schulz iteration process \[undefb\] is adopted to approximately solve ${({\mathbf{M}_{t}\mathbf{M}_{t}^{T}})}^{- {1/2}}\mathbf{M}_{t}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Newton-Schulz Iterations for Matrix Orthogonalization", "weight": 1.0} -->

where $\mathbf{X}_{N}$ is the result of such process after $N$ iteration steps. Here $a$, $b$, $c$ are coefficients. In order to ensure the correct convergence of Equation 2, we need to tune the coefficients so that the polynomial ${f{(x)}} = {{ax} + {bx^{3}} + {cx^{5}}}$ has a fixed point near 1. In the original design of \[undefo\], the coefficients are set to $a = 3.4445$, $b = {- 4.7750}$, $c = 2.0315$ in order to make the iterative process converge faster for small initial singular values. In this work, we follow the same setting of coefficients.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Steepest Descent Under Norm Constraints", "weight": 1.0} -->

\[undefb\] proposed to view the optimization process in deep learning as steepest descent under norm constraints. From this perspective, we can view the difference between Muon and Adam \[undefr, undefz\] as the difference in norm constraints. Whereas Adam is a steepest descent under the a norm constraint dynamically adjusted from a Max-of-Max norm, Muon offers a norm constraint that lies in a static range of Schatten-$p$ norm for some large $p$ \[undefi\]. When equation 1 is accurately computed, the norm constraint offered by Muon will be the spectral norm. Weights of neural networks are used as operators on the input space or the hidden space, which are usually (locally) Euclidean \[undefd\], so the norm constraint on weights should be an induced operator norm (or spectral norm for weight matrices). In this sense, the norm constraint offered by Muon is more reasonable than that offered by Adam.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Weight Decay", "weight": 1.0} -->

While Muon performs significantly better than AdamW on a small scale as shown by \[undefo\], we found the performance gains diminish when we scale up to train a larger model with more tokens. We observed that both the weight and the layer output's RMS keep growing to a large scale, exceeding the high-precision range of bf16, which might hurt the model's performance. To resolve this issue, we introduced the standard AdamW (\[undefz\]) weight decay mechanism into Muon^11^1The original implementation of Muon omits weight decay. A recent concurrent work in Muon incorporates weight decay and demonstrates improved performance. See this commit and this discussion..

<!-- chunk {"id": "body-0015", "role": "body", "section": "Weight Decay", "weight": 1.0} -->

We experimented on Muon both with and without weight decay to understand its impact on the training dynamics of LLMs. Based on our scaling law research in Sec 3.2, we trained an 800M parameters model with 100B tokens ($\sim 5 \times$ optimal training tokens). Figure 2 shows validation loss curves of the model trained with AdamW, vanilla Muon (without weight decay), and Muon with weight decay. While vanilla Muon initially converges faster, we observed that some model weights grew too large over time, potentially limiting the model's long-term performances. Adding weight decay addressed this issue - the results demonstrate that Muon with weight decay outperforms both vanilla Muon and AdamW, achieving lower validation loss in the over-train regime. Therefore, we adjusted our update rule to equation 3, where $\lambda$ is the weight decay ratio.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Consistent update RMS", "weight": 1.0} -->

An important property of Adam and AdamW (\[undefr\], \[undefz\]) is that they maintain a theoretical update RMS around 1^22^2Due to Adam's $\beta_{1} < \beta_{2}$ and $\epsilon > 0$, the actual update RMS is usually less than 1..

<!-- chunk {"id": "body-0017", "role": "body", "section": "Matching update RMS of AdamW", "weight": 1.0} -->

Muon is designed to update matrix-based parameters. In practice, AdamW is used in couple with Muon to handle non-matrix based parameters, like RMSNorm, LM head, and embedding parameters. We would like the optimizer hyper-parameters (learning rate $\eta$, weight decay $\lambda$) to be shared among matrix and non-matrix parameters.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Matching update RMS of AdamW", "weight": 1.0} -->

We propose to match Muon's update RMS to be similar to that of AdamW. From empirical observations, AdamW's update RMS is usually around 0.2 to 0.4.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Matching update RMS of AdamW", "weight": 1.0} -->

We validated this choice with empirical results (see Appendix A for details). Moreover, we highlighted that with this adjustment, Muon can directly reuse the learning rate and weight decay tuned for AdamW.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Other Hyper-parameters", "weight": 1.0} -->

Muon contains two other tunnable hyper-parameters: Newton-Schulz iteration steps and momentum $\mu$. We empirically observe that when setting $N$ to $10$, the iterative process will yield a more accurate orthogonalization result than $N = 5$, but it won't lead to better performances. Hence we set $N = 5$ in this work for the sake of efficiency. We do not see a consistent performance gain in tuning momentum, so we chose 0.95, same as \[undefo\].

<!-- chunk {"id": "body-0021", "role": "body", "section": "ZeRO-1 and Megatron-LM", "weight": 1.0} -->

\[undefae\] introduced the ZeRO-1 technique that partitions the expensive optimizer states (e.g. master weights, momentum) all over the cluster. Megatron-LM \[undefah\] integrated ZeRO-1 into its native parallel designs. Based on Megatron-LM's sophisticated parallel strategies, e.g. Tensor-Parallel (TP), Pipeline Parallel (PP), Expert Parallel (EP) and Data Parallel (DP), the communication workload of ZeRO-1 can be reduced from gathering all over the distributed world to only gathering over the data parallel group.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Method", "weight": 1.0} -->

ZeRO-1 is efficient for AdamW because it calculates updates in an element-wise fashion. However, Muon requires the full gradient matrix to calculate the updates. Therefore, vanilla ZeRO-1 is not directly applicable to Muon. We propose a new distributed solution based on ZeRO-1 for Muon, referred to as Distributed Muon.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Method", "weight": 1.0} -->

DP Gather. For a local DP partitioned master weight (${1/D}P$ the size of the model weight), this operation is to gather the corresponding partitioned gradients into a full gradient matrix.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Method", "weight": 1.0} -->

Calculate Full Update. After the above gathering, perform Newton-Schulz iteration steps on the full gradient matrix as described in Sec 2.1. Note that we will then discard part of the full update matrix, as we only need the partition corresponding to the local parameters to perform update.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Method", "weight": 1.0} -->

The implementation of Distributed Muon is described in Algorithm 1. The additional operations introduced by Distributed Muon are colored in blue.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Method", "weight": 1.0} -->

0: Full Gradients G, DP partitioned Momentum m, DP partitioned parameters p, momentum μ.
1: // Reduce-scatter G on DP for correct gradients
2: g = reduce_scatter(G, dp_group)
3: // Apply momentum to g using local partitioned momentum m
4: g′ = update_with_momentum (g,m,μ)
5: // DP Gather: gathering g′ across DP into a full matrix G
7: // Calculate Muon update
9: // Discard the rest of U and only keep the local partition u, then apply the update rule
11: // All-gather updated p′ into P
12: P = all_gather(p′, dp_group)
13: // Return the update RMS for logging
14: return $\sqrt{\mathbf{u}^{2}.{\text{mean}{}}}$

<!-- chunk {"id": "body-0027", "role": "body", "section": "Analysis", "weight": 1.0} -->

Memory Usage. Muon uses only one momentum buffer, while AdamW uses two momentum buffers. Therefore, the additional memory used by the Muon optimizer is half of Distributed AdamW.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Analysis", "weight": 1.0} -->

Communication Overhead. For each device, the additional DP gathering is only required by the local DP partitioned parameters $\mathbf{p}$. Therefore, the communication cost is less than the reduce-scatter of $\mathbf{G}$ or the all-gather of $\mathbf{P}$. Besides, Muon only requires the Newton-Schulz iteration steps in bf16, thus further reducing the communication overhead to 50% comparing to fp32. Overall, the communication workload of Distributed Muon is $(1,1.25\rbrack$ of that of Distributed AdamW.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Analysis", "weight": 1.0} -->

The upper-bound is calculated as that the communication of Distributed Muon is 4 (fp32 $\mathbf{G}$ reduce-scatter) + 2 (bf16 Muon gather) + 4 (fp32 $\mathbf{P}$ all-gather), while Distributed AdamW is 4 + 4. In practice, as we usually train with multiple DP, the empirical additional cost usually is closer to the lower-bound 1.^44^4If TP is enabled, Distributed Muon needs an extra bf16 TP gather on TP group..

<!-- chunk {"id": "body-0030", "role": "body", "section": "Analysis", "weight": 1.0} -->

Latency. Distributed Muon has larger end-to-end latencies than Distributed AdamW because it introduces additional communication and requires running Newton-Schulz iteration steps. However, this is not a significant issue because (a) only about 5 Newton-Schultz iteration steps are needed for a good result (discussed in Sec 2.2), and (b) the end-to-end latency caused by the optimizer is negligible compared to the model's forward-backward pass time (e.g. usually 1% to 3%). Moreover, several engineering techniques, such as overlapping gather and computation, and overlapping optimizer reduce-scatter with parameter gather, can further reduce latency.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Analysis", "weight": 1.0} -->

When training large-scale models in our distributed cluster, Distributed Muon has no noticeable latency overhead compared to its AdamW counterparts. We will soon release a pull request that implements Distributed Muon for the open-source Megatron-LM \[undefah\] project.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Consistent Update RMS", "weight": 1.0} -->

As discussed in Sec 2.2, we aim to match the update RMS across all matrix parameters and also match it with that of AdamW.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Consistent Update RMS", "weight": 1.0} -->

Baseline. We multiplied the update matrix by $0.2 \cdot \sqrt{H}$ ($H$ is the model hidden size) to maintain a consistent update RMS with AdamW. Note that $\max{(A,B)}$ equals to $H$ for most matrices.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Consistent Update RMS", "weight": 1.0} -->

Update Norm. We can directly normalize the updates calculated via Newton-Schulz iterations so its RMS strictly becomes 0.2;

<!-- chunk {"id": "body-0035", "role": "body", "section": "Consistent Update RMS", "weight": 1.0} -->

Adjusted LR. For each update matrix, we can scale its learning rate by a factor of $0.2 \cdot \sqrt{\max{(A,B)}}$ based on its shape.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Analysis", "weight": 1.0} -->

We designed experiments to illustrate the impact of Muon update RMS at an early training stage, because we observed that unexpected behaviors happened very quickly when training models at larger scale. We experimented with small scale 800M models as described in 3.2. The problem of inconsistent update RMS is more pronounced when the disparity between matrix dimensions increases. To highlight the problem for further study, we slightly modify the model architecture by replacing the Swiglu MLP with a standard 2-layer MLP, changing the shape of its matrix parameters from $\lbrack H,{2.6H}\rbrack$ to $\lbrack H,{4H}\rbrack$. We evaluated the model's loss and monitored a few of its parameters' RMS, specifically, attention query (shape $\lbrack H,H\rbrack$) and MLP (shape $\lbrack H,{4H}\rbrack$). We evaluated the model after training for 4B tokens out of a 20B-token schedule.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Analysis", "weight": 1.0} -->

query weight RMS
MLP weight RMS

<!-- chunk {"id": "body-0038", "role": "body", "section": "Analysis", "weight": 1.0} -->

Both Update Norm and Adjusted LR achieved better performances than Baseline;

<!-- chunk {"id": "body-0039", "role": "body", "section": "Analysis", "weight": 1.0} -->

For the MLP weight matrix of shape $\lbrack H,{4H}\rbrack$, both Update Norm and Adjusted LR obtain a weight RMS that is roughly doubled comparing to Baseline. This is reasonable as ${\sqrt{\text{max}{(H,{4H})}}/\sqrt{H}} = 2$, so the update RMS of Update Norm and Adjusted LR is roughly two times of Baseline;

<!-- chunk {"id": "body-0040", "role": "body", "section": "Analysis", "weight": 1.0} -->

For the attention query weight matrix of shape $\lbrack H,H\rbrack$, Update Norm still norms the update, while Adjusted LR does not because ${\sqrt{\text{max}{(H,H)}}/\sqrt{H}} = 1$. As a result, Adjusted LR results in a similar weight RMS as Baseline, but Update Norm has a larger weight rms similar to its MLP.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Analysis", "weight": 1.0} -->

Based on these findings, we choose the Adjusted LR method for future experiments because it has lower cost.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Scaling Law of Muon", "weight": 1.0} -->

For a fair comparison with AdamW, we performed scaling law experiments on a series of dense models in Llama \[undefj\] architecture. Building a strong baseline is of crucial importance in optimizer research. Hence, we perform a grid search for hyper-parameters of AdamW, following the compute-optimal training setup \[undefq\] (the grid search experiments can be found in Appendix B). Details of the model architecture and hyper-parameters can be found in Table 2. For Muon, as discussed in Sec 2.2, since we matched Muon's update RMS to AdamW, we directly reused the hyper-parameters that are optimal for the AdamW baseline.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Params. w/o Embedding", "weight": 1.0} -->

*In terms of number of examples in 8K context length.
Table 2: Scaling Law Models and Hyper-Parameters

<!-- chunk {"id": "body-0044", "role": "body", "section": "Params. w/o Embedding", "weight": 1.0} -->

The fitted scaling law curve can be found in figure 3, and the fitted equations are detailed in table 3. As shown in Figure 1(a), Muon only requires about 52% training FLOPs to match the performance of AdamW under compute-optimal setting.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

To evaluate Muon against contemporary model architectures, we pretrained from scratch using the deepseek-v3-small architecture \[undefh\] as it demonstrates strong performance and the original results serve as a reference for comparison. Our pretrained model has 2.24B activated and 15.29B total parameters (3B activated and 16B total when including embedding). Minor modifications to the architecture are detailed in Appendix C.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Pretraining Data", "weight": 1.0} -->

Our pretraining data details can be found in \[undefal\]. The maximum context length during pretraining is 8K.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Pretraining", "weight": 1.0} -->

The model is trained in several stages. We use a 1e-3 auxfree bias update rate in stage 1 and 2, and 0.0 auxfree bias update rate in stage 3. The weight decay is set to 0.1 for all stages. More details and discussions of model training can be found in the Appendix D.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Pretraining", "weight": 1.0} -->

0 to 33B tokens: In this stage, the learning rate linearly increases to 4.2e-4 in 2k steps. The batch size is kept at 2048 examples;

<!-- chunk {"id": "body-0049", "role": "body", "section": "Pretraining", "weight": 1.0} -->

33B to 5.2T tokens: In this stage, the learning rate decays from 4.2e-4 to 4.2e-5 in a cosine style. We keep the batch size at 2048 until 200B tokens, and then doubled to 4096 for the remaining;

<!-- chunk {"id": "body-0050", "role": "body", "section": "Pretraining", "weight": 1.0} -->

5.2T to 5.7T tokens: In this stage (also referred as the cooldown stage), the learning rate increases to 1e-4 in in 100 steps, and then linearly decays to 0 in 500B tokens, and we keep a constant 4096 batch size. In this stage, we use the highest quality data, focusing on math, code, and reasoning.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Evaluation Benchmarks", "weight": 1.0} -->

English Language Understanding and Reasoning: MMLU(5-shot)\[undefk\], MMLU-pro(5-shot) \[undefan\], BBH(3-shot) \[undefai\], TriviaQA(5-shot) \[undefp\]

<!-- chunk {"id": "body-0052", "role": "body", "section": "Evaluation Benchmarks", "weight": 1.0} -->

Code Generation: HumanEval(pass@1) \[undefe\], MBPP(pass@1)\[undefa\]

<!-- chunk {"id": "body-0053", "role": "body", "section": "Evaluation Benchmarks", "weight": 1.0} -->

Mathematical Reasoning: GSM8K(4-shot) \[undeff\] MATH \[undefl\], CMATH \[undefao\]

<!-- chunk {"id": "body-0054", "role": "body", "section": "Evaluation Benchmarks", "weight": 1.0} -->

Chinese Language Understanding and Reasoning: C-Eval(5-shot) \[undefn\], CMMLU(5-shot)\[undeft\]

<!-- chunk {"id": "body-0055", "role": "body", "section": "Performance", "weight": 1.0} -->

We named our model trained with Muon "Moonlight". We compared Moonlight with different public models on a similar scale. We first evaluated Moonlight at 1.2T

<!-- chunk {"id": "body-0056", "role": "body", "section": "Performance", "weight": 1.0} -->

Deepseek-v3-Small (\[undefh\]) is a 2.4B/16B-parameter MoE model trained with 1.33T tokens;

<!-- chunk {"id": "body-0057", "role": "body", "section": "Performance", "weight": 1.0} -->

Moonlight-A follows the same training settings as Moonlight, except that it uses the AdamW optimizer.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Performance", "weight": 1.0} -->

For Moonlight and Moonlight-A, we used the intermediate 1.2T token checkpoint of the total 5.7T pretraining, where the learning rate is not decayed to minimal and the model has not gone through the cooldown stage yet.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Performance", "weight": 1.0} -->

† The reported parameter counts exclude the embedding parameters.
Table 4: Comparison of different models at around 1.2T tokens.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Performance", "weight": 1.0} -->

As shown in Table 4, Moonlight-A, our AdamW-trained baseline model, demonstrates strong performance compared to similar public models. Moonlight performs significantly better than Moonlight-A, proving the scaling effectiveness of Muon. We observed that Muon especially excels on Math and Code related tasks, and we encourage the research community to further investigate this phenomena. After Moonlight is fully trained to 5.7T

<!-- chunk {"id": "body-0061", "role": "body", "section": "Performance", "weight": 1.0} -->

LLAMA3-3B from \[undefj\] is a 3B-parameter dense model trained with 9T tokens.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Performance", "weight": 1.0} -->

Qwen2.5-3B from \[undefap\] is a 3B-parameter dense model trained with 18T tokens.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Performance", "weight": 1.0} -->

Deepseek-v2-Lite from \[undefg\] is a 2.4B/16B-parameter MOE model trained with 5.7T tokens.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Performance", "weight": 1.0} -->

† The reported parameter counts exclude the embedding parameters.‡ We tested all listed models with the full set of TriviaQA.
Table 5: Comparison of different models on various benchmarks.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Performance", "weight": 1.0} -->

As shown in Table 5, Moonlight outperforms models with similar architectures trained with an equivalent number of tokens. Even when compared to dense models trained on substantially larger datasets, Moonlight maintains competitive performance. Detailed comparisons can be found in Appendix E. The performance of Moonlight is further compared with other well-known language models on MMLU and GSM8k, as illustrated in Figure 1(b) and Appendix E Figure 8.^55^5Performance metrics and computational requirements (FLOPs) for baseline models are sourced from \[undefaa\]. Notably, Moonlight lies on the Pareto frontier of model performance versus training budget, outperforming many other models across various sizes.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Dynamics of Singular Spectrum", "weight": 1.0} -->

In order to validate the intuition that Muon can optimize the weight matrices in more diverse directions, we conducted a spectral analysis of the weight matrices trained with Muon and AdamW.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Dynamics of Singular Spectrum", "weight": 1.0} -->

As shown in Figure 4, we visualized the average SVD entropy of the weight matrices across different training checkpoints during pretraining with 1.2T tokens. We can see that across all training checkpoints and all groups of weight matrices, the SVD entropy of Muon is higher than that of AdamW, which verifies the intuition that Muon can provide a more diverse spectrum of updates for the weight matrices. This discrepancy is more significant in the router weights for expert selection, which indicates that mixture-of-expert models can benefit more from Muon.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Dynamics of Singular Spectrum", "weight": 1.0} -->

Moreover, we visualized the singular value distributions of each weight matrix at the checkpoint trained with 1.2T tokens as demonstrated in Appendix F. We find that, for over 90% of the weight matrices, the SVD entropy when optimized by Muon is higher than that of AdamW, providing strong empirical evidence for Muon's superior capability in exploring diverse optimization directions.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Supervised Finetuning (SFT) with Muon", "weight": 1.0} -->

In this section, we present ablation studies on the Muon optimizer within the standard SFT stage of LLM training. Our findings demonstrate that the benefits introduced by Muon persist during the SFT stage. Specifically, a model that is both Muon-pretrained and Muon-finetuned outperforms others in the ablation studies. However, we also observe that when the SFT optimizer differs from the pretraining optimizer, SFT with Muon does not show a significant advantage over AdamW. This suggests that there is still considerable room for further exploration, which we leave for future work.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Ablation Studies on the Interchangeability of Pretrain and SFT Optimizers", "weight": 1.0} -->

To further investigate Muon's potential, we finetuned Moonlight@1.2T and Moonlight-A@1.2T using both the Muon and AdamW optimizers. These models were finetuned for two epochs on the open-source tulu-3-sft-mixture dataset (\[undefs\]), which contains 4k sequence length data. The learning rate followed a linear decay schedule, starting at $5 \times 10^{- 5}$ and gradually reducing to $0$. The results, shown in Table 6 with Muon ‣ 3 Experiments ‣ Muon is Scalable for LLM Training"), highlight the superior performance of Moonlight@1.2T compared to Moonlight-A@1.2T.

<!-- chunk {"id": "body-0071", "role": "body", "section": "SFT with Muon on public pretrained models", "weight": 1.0} -->

We further applied Muon to the supervised fine-tuning (SFT) of a public pretrained model, specifically the Qwen2.5-7B base model (\[undefap\]), using the open-source tulu-3-sft-mixture dataset (\[undefs\]). The dataset was packed with an 8k sequence length, and we employed a cosine decay learning rate schedule, starting at $2 \times 10^{- 5}$ and gradually decreasing to $2 \times 10^{- 6}$. The results are presented in Table 7 with Muon ‣ 3 Experiments ‣ Muon is Scalable for LLM Training"). For comparison, we show that the Muon-finetuned model achieves performance on par with the Adam-finetuned model. These results indicate that for optimal performance, it is more effective to apply Muon during the pretraining phase rather than during supervised fine-tuning.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Discussions", "weight": 1.0} -->

There are several possible directions for future research that could further explore and expand upon the current findings.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Incorporating All Parameters into the Muon Framework", "weight": 1.0} -->

Currently, the Muon optimizer is utilized in conjunction with the Adam optimizer, where certain parameters remain under the purview of Adam optimization. This hybrid approach, while functional, presents an opportunity for improvement. The integration of the optimization of all parameters exclusively within the Muon framework is a topic of significant research interest.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Extending Muon to Schatten Norms", "weight": 1.0} -->

The Muon optimizer can be interpreted as the steepest descent method under the spectral norm. Given the broad applicability and versatility of Schatten norms, extending Muon to encompass the general Schatten norm is a promising direction. This extension may unlock additional optimization capabilities and potentially yield superior results compared to the current spectral norm-based implementation.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Understanding and Solving the Pretraining-Finetuning Mismatch", "weight": 1.0} -->

A notable phenomenon observed in practice is the suboptimal performance of models pretrained with AdamW when fine-tuned with Muon, and vice versa. This optimizer mismatch presents a significant barrier to effectively leveraging the extensive repository of AdamW-pretrained checkpoints, thereby necessitating a rigorous theoretical investigation. A precise understanding of the underlying mechanisms is essential for devising robust and effective solutions.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this technical report, we presented a comprehensive study on the scalability of Muon in LLM training. Through systematic analysis and improvements, we successfully applied Muon to a 3B/16B-parameter MoE model trained on 5.7 trillion tokens. Our results demonstrate that Muon can effectively replace AdamW as the standard optimizer for large-scale LLM training, offering significant advantages in both training efficiency and model performance. By open-sourcing our implementation, the Moonlight model, and intermediate training checkpoints, we aim to facilitate further research in scalable optimization techniques and accelerate the development of training methods for LLMs.
