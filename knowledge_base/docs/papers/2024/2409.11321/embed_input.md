<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SOAP: Improving and Stabilizing Shampoo Using Adam

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

There is growing evidence of the effectiveness of Shampoo, a higher-order preconditioning method, over Adam in deep learning optimization tasks. However, Shampoo's drawbacks include additional hyperparameters and computational overhead when compared to Adam, which only updates running averages of first- and second-moment quantities. This work establishes a formal connection between Shampoo (implemented with the 1/2 power) and Adafactor - a memory-efficient approximation of Adam - showing that Shampoo is equivalent to running Adafactor in the eigenbasis of Shampoo's preconditioner. This insight leads to the design of a simpler and computationally efficient algorithm: ShampoO with Adam in the Preconditioner's eigenbasis (SOAP). With regards to improving Shampoo's computational efficiency, the most straightforward approach would be to simply compute Shampoo's eigendecomposition less frequently. Unfortunately, as our empirical results show, this leads to performance degradation that worsens with this frequency. SOAP mitigates this degradation by continually updating the running average of the second moment, just as Adam does, but in the current (slowly changing) coordinate basis.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Furthermore, since SOAP is equivalent to running Adam in a rotated space, it introduces only one additional hyperparameter (the preconditioning frequency) compared to Adam. We empirically evaluate SOAP on language model pre-training with 360 m and 660 m sized models. In the large batch regime, SOAP reduces the number of iterations by over 40% and wall clock time by over 35% compared to AdamW, with approximately 20% improvements in both metrics compared to Shampoo. An implementation of SOAP is available at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

With ever-increasing costs of LLM training, optimization efficiency has become a central question in the field of deep learning. Several recent works have tackled this challenge by addressing both the memory and compute footprint of optimizers. In Algoperf, a recent optimization efficiency benchmark, Shampoo, a second-order algorithm, outperformed all other submissions, including Adam, reducing wall-clock time by 28%. Higher-order preconditioning has also been applied in large-scale training runs, such as Gemini-1.5 Flash.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The success of Shampoo has drawn increasing attention from the deep learning community. Several works have explored ways to scale Shampoo by improving its memory and compute efficiency. Other research has examined the theoretical foundations of Shampoo and proposed minor adjustments (such as using power $1/2$ rather than $1/4$) that align with prior empirical findings. Moreover, Morwani et al. also showed that Shampoo with the aforementioned modifications is close to the optimal Kronecker approximation of the Adagrad optimizer.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our first contribution is demonstrating that the variant of Shampoo proposed by Morwani et al. is equivalent^11^1Given this connection, the results of Morwani et al. can be interpreted as showing that the eigenbasis provided by Shampoo's preconditioner is close to the "optimal" basis for running Adafactor. to running Adafactor in the eigenbasis provided by Shampoo's preconditioner. This interpretation of Shampoo connects it to a broader family of methods (e.g. ) that design second-order algorithms by running a first-order method in the eigenbasis provided by a second-order method. Building on this insight, we can explore a broader design space for combining first and second order methods. Many of our design choices are a synthesis of conceptual ideas from prior works of George et al.; Anil et al.; Morwani et al. as well as implementation ideas from works of Wang et al.; Zhao et al..

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Explicitly, we study SOAP (ShampoO with Adam in the Preconditioner's eigenbasis) an algorithm that runs AdamW in the eigenbasis provided by Shampoo. Our main contributions are as follows: We make a formal connection between the Shampoo and the Adafactor algorithm. This insight leads us to consider the SOAP algorithm, which runs AdamW in the preconditioned space provided by Shampoo.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

SOAP outperforms both Shampoo and Adam in language model pre-training tasks with model sizes 360m and 660m, even after extensive hyperparameter tuning of Shampoo.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

SOAP reduces the number of hyperparameters compared to Shampoo, resulting in only one additional hyperparameter compared to AdamW: preconditioning frequency.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

SOAP demonstrates greater robustness to large preconditioning frequency compared to Shampoo on language model pre-training tasks.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We should also note that while similar algorithmic variants have been discussed in the literature (e.g. see the appendix of Anil et al. ), we are the first to systematically evaluate it.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Organization: In Section 3, we discuss related works. In Section 4, we start by showing an equivalence between Shampoo (with exponent 1/2) and running Adafactor in the eigenspace given by Shampoo, then with this equivalence as the starting point we describe SOAP. In Section 5, we provide our experimental methodology and in Section 6, we compare the performance of AdamW, Shampoo and SOAP on language modeling tasks. In Sections 7.2 and 7.3 we discuss the the space and time complexity of SOAP and how it can be improved. In Section 6.4 we show that efficiency benefits of SOAP over AdamW are maintained for longer duration runs where #tokens = 100 $\times$ model size.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Theory", "weight": 1.0} -->

We begin by describing an equivalence between Shampoo and running Adafactor in the eigenbasis of the Shampoo preconditioner. For simplicity we omit momentum but the equivalence also holds with momentum. For this equivalence we use Shampoo with the following modifications from the original Shampoo optimizer: We use power $1/2$ instead of power $1/4$. This was already recommended in practical implementations and a theoretical connection between optimal Kronecker approximation of Adagrad preconditioner and Shampoo with power $1/2$ was established in Morwani et al..

<!-- chunk {"id": "body-0014", "role": "body", "section": "Theory", "weight": 1.0} -->

We also use the scalar correction to per layer learning rates described in Ren & Goldfarb; Morwani et al..

<!-- chunk {"id": "body-0015", "role": "body", "section": "Theory", "weight": 1.0} -->

Instead of the running average of $L$ and $R$ across time steps, we use dataset averages.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Theory", "weight": 1.0} -->

With these changes in place (first occurrence of these changes is highlighted in red in the algorithm below) we formally define the two algorithms whose equivalence we show in Algorithms 1 and 2.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Theory", "weight": 1.0} -->

3: L ← 𝔼B[GBGBT] {Where the expectation is over a random batch B.} Algorithm 1 Single step of idealized Shampoo with power 1/2.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Theory", "weight": 1.0} -->

8: {Idealized version of code for Adafactor taking Gt′ to be the gradient} 12: ${\hat{V}}_{t} = \frac{AC^{T}}{\mathbf{1}_{n}^{\top}A}$ {Elementwise division} 13: $G_{t}^{\operatorname{\prime\prime}}\leftarrow\frac{G_{t}'}{\sqrt{{\hat{V}}_{t}} + \epsilon}$ {Elementwise division and square root} 14: Gt''' ← QLGt''QRT {Projecting back to original space} Algorithm 2 Single step of idealized Adafactor in Shampoo’s eigenspace.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Experimental Methodology", "weight": 1.0} -->

Hyperparameter tuning: We begin with hyperparameter values suggested by prior research for both AdamW and Distributed Shampoo (e.g., $\beta_{2} = 0.95$). Initially, we conduct a learning rate sweep to determine the optimal learning rate for each optimizer. Once the optimal learning rate is identified, we perform two-dimensional sweeps for each of the remaining hyperparameters, where we vary the selected hyperparameter alongside the learning rate. The purpose of these sweeps is to demonstrate that our default hyperparameter settings are near-optimal, disregarding potential interactions between two non-learning-rate hyperparameters. A detailed discussion of the hyperparameter sweeps is provided in Appendix A.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Experimental Methodology", "weight": 1.0} -->

Throughput Measurement: We evaluate the throughput of each optimizer by measuring the number of tokens processed per second. At present, we perform these measurements on a single H100 GPU and utilize gradient accumulation to accommodate large batch sizes. While this approach may seem to disadvantage AdamW--- as the overhead of Shampoo/SOAP is compared against multiple gradient accumulation steps--- it is important to note that the overhead of Shampoo/SOAP can be amortized across layers by distributing the updates across multiple GPUs. This technique is employed in the distributed implementation of Shampoo. A comprehensive comparison of distributed implementations of these algorithms is left to future work.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experimental Methodology", "weight": 1.0} -->

Efficiency Benefits: Simply running SOAP for the same duration as Shampoo and AdamW cannot be directly used to calculate the efficiency benefit (in terms of training steps or wall-clock time) of using SOAP since we use a cosine schedule. Therefore, we run SOAP on $.5,.625,.75$ and $.875$ fraction of the training data and fit a scaling law of the form $a + {bN^{- \beta}}$ through the final losses obtained, where $N$ represents the number of training points and $a,b,\beta$ are the parameters of the fit. We show these points and the corresponding scaling laws obtained in Figure 2. This scaling law is then used to calculate the efficiency benefit in terms of training steps and wallclock time as shown in Figure 2. Here, the horizontal lines represent the final losses of AdamW and Shampoo.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Language Modeling Experiments", "weight": 1.0} -->

In this section we focus on empirically comparing AdamW, DistributedShampoo, and SOAP on language modeling tasks.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Measuring Efficiency Benefits", "weight": 1.0} -->

In Figure 1 (left and middle) and Figure 3 we show train loss curves for AdamW, Shampoo, and SOAP on 360m and 660m models with 2m token batch size and "chinchilla-optimal" i.e. 20x model size number of tokens. In these plots we observe that SOAP outperforms the other two optimizers. To directly calculate the efficiency benefit of SOAP, we also run SOAP with cosine decay for a shorter lr schedule, as shown in Figures 1 and 3. This allows us to approximate the following efficiency benefits (when batch size is set to 2m and preconditioning frequency to 10): $\geq {40\%}$ reduction in the number of iterations and $\geq {35\%}$ reduction in wall clock time compared to AdamW; $\approx {20\%}$ reduction in iterations and wall clock time as compared to Shampoo. Precise efficiency benefit calculations are presented in Figure 2(left and middle). In Section 6.4 we show that efficiency benefits of SOAP over AdamW are maintained for longer duration runs where #tokens = 100 $\times$ model size.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Effect of Frequency of Finding Eigenvectors/Inverse", "weight": 1.0} -->

In Figure 1 (right), we compare SOAP and Shampoo with respect to preconditioning frequency. We observe the following: For all frequencies we tried from 1 to 100, both optimizers outperform AdamW.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Effect of Frequency of Finding Eigenvectors/Inverse", "weight": 1.0} -->

At frequency 1, SOAP and Shampoo are quite close in performance.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Effect of Frequency of Finding Eigenvectors/Inverse", "weight": 1.0} -->

At higher frequencies, the performance of both SOAP and Shampoo degrades but SOAP's performance degrades significantly slower than Shampoo's.

<!-- chunk {"id": "body-0027", "role": "body", "section": "SOAP Improves the Critical Batch Size", "weight": 1.0} -->

When scaling up batch sizes, the ideal outcome is that doubling the batch size results in halving the number of training steps needed to achieve the same performance. The batch size at which this ideal scaling starts to break down is referred to by McCandlish et al. as the critical batch size. As models and datasets grow larger, it becomes increasingly important to develop optimizers that support larger critical batch sizes, thereby reducing the serial runtime of a training run. In this subsection, we compare the critical batch sizes of AdamW and SOAP. Relative to our baseline setup of a 2 million batch size, when we decrease the batch size by a factor of $k$, we increase the preconditioning frequency by the same factor. This ensures that the FLOPS and wall clock multiplicative overhead for the eigenvector decomposition steps remains consistent with the 2 million batch size setting.

<!-- chunk {"id": "body-0028", "role": "body", "section": "SOAP Improves the Critical Batch Size", "weight": 1.0} -->

We start by training a 360 million parameter model with a batch size of 256k for a "Chinchilla-optimal" number of tokens (20 times the model size) using AdamW, achieving a loss of 2.842. This value is set as the target loss for our comparisons. In Figure 4 (left), we show the number of steps AdamW and SOAP require to reach this target loss as we vary the batch size. SOAP consistently requires fewer steps across all batch sizes, with the multiplicative benefits becoming more pronounced at larger batch sizes. Additionally, we compare these results to the ideal scenario (dashed line) of linear scaling, where doubling the batch size halves the number of steps. SOAP more closely follows the linear scaling trend compared to AdamW, indicating that it has a higher critical batch size in this setup.

<!-- chunk {"id": "body-0029", "role": "body", "section": "SOAP Improves the Critical Batch Size", "weight": 1.0} -->

In Figure 4 (right), we present the optimal runs for each optimizer (including Shampoo) at the smallest batch size we consider: 256k. SOAP outperforms both Shampoo and AdamW, reducing the number of iterations by 25% compared to AdamW, and by approximately 10% compared to Shampoo. Furthermore, in Figure 2 (right, bottom), we demonstrate that SOAP also achieves a wall-clock time improvement of $\geq {15\%}$ over AdamW and around 10% over Shampoo. We note that these results are a preliminary analysis for smaller batch size runs. Our approach of keeping the product of batch size and preconditioning frequency constant may not be optimal, and a better trade-off could likely be found. Furthermore, SOAP's overhead could potentially be reduced by performing $L$ and $R$ updates in lower precision (instead of fp32). Finally, the diminished efficiency gains of second-order methods at smaller batch sizes are consistent with prior findings.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Scaling to Larger Token Counts", "weight": 1.0} -->

Thus far, our focus has been on Chinchilla-optimal token counts for a given model size. However, in many practical scenarios, models are trained on significantly larger token budgets to optimize inference costs and downstream performance. In Figure 5, we demonstrate that SOAP maintains its advantage Adam even in extended training runs.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Further Efficiency Improvements", "weight": 1.0} -->

In this section, we discuss space and time complexity of SOAP and provide an overview of potential avenues for further space and compute efficiency improvements in SOAP.

<!-- chunk {"id": "body-0032", "role": "body", "section": "One Sided Eigenbasis", "weight": 1.0} -->

As described in Section 3, Zhao et al. have an algorithm similar to ours. One of the differences is that they only project the smaller side of the layer using the eigenbasis while using identity as the rotation matrix for the larger side i.e. if $m < n$ we set $Q_{R} = I_{n}$ in Algorithm 3 and if $m > n$ we set $Q_{L} = I_{m}$. Doing this leads to a reduction in space usage as well as reduction of optimizer time overhead, which is discussed in Sections 7.2.1 and 7.3.1.

<!-- chunk {"id": "body-0033", "role": "body", "section": "One Sided Eigenbasis", "weight": 1.0} -->

In Figure 6, it is evident that the one-sided projection results in slightly reduced performance compared to the original SOAP optimizer. However, it still performs on par, or marginally better than, Shampoo, while maintaining greater computational efficiency. Further investigation into the potential for these variants to surpass the computational efficiency of original SOAP optimizer is left for future work.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Space usage of SOAP", "weight": 1.0} -->

For a $m \times n$ matrix where $m > n$ we require space usage^44^4One $mn$ is for storing the gradients, this can be avoided (as long as there is no gradient accumulation) by applying gradients along with backprop but this is not implemented by default in standard deep learning frameworks such as PyTorch. Hence we will include this term in all of our calculations. (beyond weights and activations), specifically for $L,Q_{L},R,Q_{R},{\text{momentum~}{(M)}}$, AdamW's second order estimate ($V$), and the gradient. This is the same space usage as DistributedShampoo while AdamW uses $3mn$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Improving space usage of SOAP", "weight": 1.0} -->

The most direct way to reduce memory is using low precision to store the $L,R,Q_{L},Q_{R},V$ matrices, which is done by Dettmers et al.; Wang et al.. Orthogonal to the low precision approaches, there are two algorithmic approaches to improving the space usage of SOAP: Using Adafactor instead of Adam as the diagonal preconditioner after rotating by $Q_{L}$ and $Q_{R}$. This reduces the space usage by $mn$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Improving space usage of SOAP", "weight": 1.0} -->

Using one sided version of SOAP (Section 7.1). This reduces space usage from ${2m^{2}} + {2n^{2}} + {3mn}$ to $2\min{(m,n)}^{2} + 3mn$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Improving space usage of SOAP", "weight": 1.0} -->

Combining these approaches yields space usage of $2\min{(m,n)}^{2} + 2mn$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Improving space usage of SOAP", "weight": 1.0} -->

For standard transformer architectures the last variant which combines the two approaches would yield less space usage overall compared to AdamW (which uses $3mn$).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Improving space usage of SOAP", "weight": 1.0} -->

We try these approaches in Figure 6. We observe that using Adafactor instead of AdamW yields very small reductions in performance while using one-sided preconditioner results in larger reductions. Nonetheless even after combining these two approaches the resulting optimizer outperforms AdamW while having a smaller space requirement than AdamW. Regarding space usage we also note that Adafactor (with momentum added back) itself utilizes only $2mn$ space usage and has been shown to perform comparable to AdamW for ViT training and for language model training. Further space reduction beyond Adafactor has been studied in the Adalomo, GaLore, and AdaMeM papers.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Time Overhead of SOAP", "weight": 1.0} -->

There are two types of overhead of Shampoo and SOAP over AdamW: the overhead per step and the overhead when changing the preconditioner (or for SOAP, the preconditioner's eigenbasis). Let us first analyze the first one. For SOAP per step for a layer of size $m \times n$ we have an overhead of We note that this is more than the overhead of Shampoo which is $m^{3} + n^{3} + {m^{2}n} + {n^{2}m}$. This can be observed in Figure 2 (bottom, right) but not in the other figures since there the second type of overhead is the dominant term.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Time Overhead of SOAP", "weight": 1.0} -->

The second type of overhead is due to changing the preconditioner for Shampoo (or for SOAP, preconditioner's eigenbasis i.e. $Q_{L}$ and $Q_{R}$). The DistributedShampoo implementation of Shampoo uses a direct call to torch.linalg.eigh for this. Following Wang et al. we use Algorithm 4 which uses power iteration based approach which calls torch.linalg.qr. We note that torch.linalg.qr is faster than torch.linalg.eigh. In Figure 7 (right) we see that using power iteration based approach (torch.linalg.qr) performs as well as fresh eigenvector decomposition (torch.linalg.eigh).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Time Overhead of SOAP", "weight": 1.0} -->

Effect of frequency on overhead: In Figure 7 (left), we observe that the overhead decreases as the preconditioning frequency increases, i.e., the frequency of invoking Algorithm 4. If the only additional computation occurred in Algorithm 4, we would expect the overhead to scale as $1.0/{(\text{preconditioning frequency})}$, approaching zero. However, empirical results (Figure 7 left) show that the overhead approaches an asymptote greater than zero. This is attributable to the additional matrix multiplications required to update $L$, update $R$, project the gradient, and reproject the gradient (for each layer) in the optimizer. Currently, these operations are performed in float32; reducing the precision of these operations, as proposed in Wang et al., could lower this asymptote.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Improving time overhead of SOAP", "weight": 1.0} -->

The per step overhead of SOAP can be reduced by using low precision to store the $L,R,Q_{L},Q_{R},V$ matrices, which in turn will speed up computation done using these matrices. This approach cannot be used for reducing the overhead for the preconditioner update in popular deep learning frameworks such as Pytorch since torch.linalg.qr does not support precision lower than float32. Orthogonal to the low precision approach we can improve the per step time overhead of SOAP by the following algorithmic approaches: Using Adafactor instead of Adam (Section 7.2) as the diagonal preconditioner after rotating by $Q_{L}$ and $Q_{R}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Improving time overhead of SOAP", "weight": 1.0} -->

In this version of SOAP the overhead can be improved by from $m^{3} + n^{3} + {2m^{2}n} + {2n^{2}m}$ to $m^{3} + n^{3} + m^{2}n + n^{2}m + \max{(m,n)}^{2}\min{(m,n)} + \min{(m,n)}^{3}$ by merging the project and project back steps for the smaller dimension.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Improving time overhead of SOAP", "weight": 1.0} -->

Combining these approaches yields an overhead of $\min{(m,n)}^{2}\max{(m,n)} + 2\min{(m,n)}^{3}$ Using one-sided version also reduces the second type of overhead from a calls to torch.linalg.qr on a $m \times m$ and a $n \times n$ matrix to only a single call to ${\min{(m,n)}} \times {\min{(m,n)}}$ matrix.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Discussion and Future Work", "weight": 1.5} -->

We study an optimizer called SOAP: ShampoO with Adam in the Preconditioner's eigenbasis. We show that SOAP outperforms both AdamW and Shampoo in language modeling tasks and show that it is more robust to changes in preconditioning frequency than Shampoo. For future work, we would like to explore further improvements to the design of SOAP, in particular, related to using lower precision for the preconditioners as well as a better distributed implementation. We would also like to explore the performance of SOAP on other domains such as vision.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Discussion and Limitations", "weight": 1.5} -->

We study an optimizer called SOAP: ShampoO with Adam in the Preconditioner's eigenbasis. We show that SOAP outperforms both AdamW and Shampoo in language modeling tasks and show that it is more robust to changes in preconditioning frequency than Shampoo. While we have explored many factors such as batch size (Section 6.3) and training duration (Section 6.4) we acknowledge that our study focuses on a relatively small scale compared to recent LLMs Touvron et al. which are two orders of magnitude bigger. We hypothesize that our findings on the performance of SOAP would generalize to larger scales due to its theoretical foundation. SOAP's robustness is also supported by the fact that SOAP is equivalent to running Adam in a rotated space, and Adam has proven to be effective across scale and tasks. However, this hypothesis remains to be validated.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Discussion and Limitations", "weight": 1.5} -->

For future work, we aim to improve the design of SOAP further, particularly by exploring the use of lower precision for preconditioners and optimizing its distributed implementation. Additionally, we are interested in testing SOAP's performance in other domains, such as vision, to evaluate its performance across different types of tasks.
