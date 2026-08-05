<!-- arxiv-full-text:v1 {"arxiv_id": "2409.11321", "source": "arxiv-html"} -->

## Introduction

With ever-increasing costs of LLM training, optimization efficiency has become a central question in the field of deep learning. Several recent works have tackled this challenge by addressing both the memory and compute footprint of optimizers. In Algoperf, a recent optimization efficiency benchmark, Shampoo, a second-order algorithm, outperformed all other submissions, including Adam, reducing wall-clock time by 28%. Higher-order preconditioning has also been applied in large-scale training runs, such as Gemini-1.5 Flash.

The success of Shampoo has drawn increasing attention from the deep learning community. Several works have explored ways to scale Shampoo by improving its memory and compute efficiency. Other research has examined the theoretical foundations of Shampoo and proposed minor adjustments (such as using power $1/2$ rather than $1/4$) that align with prior empirical findings. Moreover, Morwani et al. also showed that Shampoo with the aforementioned modifications is close to the optimal Kronecker approximation of the Adagrad optimizer.

Our first contribution is demonstrating that the variant of Shampoo proposed by Morwani et al. is equivalent^11^1Given this connection, the results of Morwani et al. can be interpreted as showing that the eigenbasis provided by Shampoo's preconditioner is close to the "optimal" basis for running Adafactor. to running Adafactor in the eigenbasis provided by Shampoo's preconditioner. This interpretation of Shampoo connects it to a broader family of methods (e.g. ) that design second-order algorithms by running a first-order method in the eigenbasis provided by a second-order method. Building on this insight, we can explore a broader design space for combining first and second order methods. Many of our design choices are a synthesis of conceptual ideas from prior works of George et al.; Anil et al.; Morwani et al. as well as implementation ideas from works of Wang et al.; Zhao et al..

Explicitly, we study SOAP (ShampoO with Adam in the Preconditioner's eigenbasis) an algorithm that runs AdamW in the eigenbasis provided by Shampoo. Our main contributions are as follows: We make a formal connection between the Shampoo and the Adafactor algorithm. This insight leads us to consider the SOAP algorithm, which runs AdamW in the preconditioned space provided by Shampoo.

SOAP outperforms both Shampoo and Adam in language model pre-training tasks with model sizes 360m and 660m, even after extensive hyperparameter tuning of Shampoo.

SOAP reduces the number of hyperparameters compared to Shampoo, resulting in only one additional hyperparameter compared to AdamW: preconditioning frequency.

SOAP demonstrates greater robustness to large preconditioning frequency compared to Shampoo on language model pre-training tasks.

We should also note that while similar algorithmic variants have been discussed in the literature (e.g. see the appendix of Anil et al. ), we are the first to systematically evaluate it.

Organization: In Section 3, we discuss related works. In Section 4, we start by showing an equivalence between Shampoo (with exponent 1/2) and running Adafactor in the eigenspace given by Shampoo, then with this equivalence as the starting point we describe SOAP. In Section 5, we provide our experimental methodology and in Section 6, we compare the performance of AdamW, Shampoo and SOAP on language modeling tasks. In Sections 7.2 and 7.3 we discuss the the space and time complexity of SOAP and how it can be improved. In Section 6.4 we show that efficiency benefits of SOAP over AdamW are maintained for longer duration runs where #tokens = 100 $\times$ model size.

Figure 1: Comparing performance of tuned runs for AdamW, Shampoo (using DistributedShampoo implementation) and SOAP. In left and middle figures, Shampoo and SOAP use a preconditioning frequency of 10. The ”shorter LR schedule” plot is where we tuned the cosine decay so as to achieve the same terminal performance as AdamW. There we observe a ≥ 40% reduction in the number of iterations and a ≥ 35% reduction in wall clock time compared to AdamW, and approximately a 20% reduction in both metrics compared to Shampoo. In the right figure we ablate preconditioning frequency and observe a slower degradation of performance of SOAP as compared to Shampoo. See Section 6 for a discussion of experimental results and ablation of batch size and Section 5 for experimental methodology.

## Notation and Background

We denote the weight matrix of a neural network layer by $W \in {\mathbb{R}}^{m \times n}$, and the corresponding gradient by $G \in {\mathbb{R}}^{m \times n}$. At a given time step $t$, these are denoted as $W_{t}$ and $G_{t}$, respectively. For a batch of inputs at time $t$, denoted by $B_{t}$, the loss and its gradient evaluated at $W_{t}$ are represented as $\phi_{B_{t}}{(W_{t})}$ and ${\nabla_{W}\phi_{B_{t}}}{(W_{t})}$, respectively.

Adagrad is an online learning second-order algorithm that maintains a preconditioner $H \in {\mathbb{R}}^{{{mn} \times m}n}$. If the vectorized gradient at time $t$ is denoted by $g_{t}$ (i.e., $g_{t} = {\text{vec}{(G_{t})}} \in {\mathbb{R}}^{mn}$), then the update of the preconditioner and the vectorized weights $w_{t} \in {\mathbb{R}}^{mn}$ with learning rate $\eta$ is given by Adam, a widely used first-order optimization algorithm in deep learning is a diagonal approximation of Adagrad. It maintains an exponential moving average of the gradients $G_{t}$ (denoted as $M_{t}$) and of element-wise squared gradients $G_{t}^{2}$ (denoted as $V_{t}$) for a given weight matrix $W$. Its update rule with learning rate $\eta$ is given by where the division is performed element-wise.

Adafactor, a variant of Adam, replaces $V_{t}$ with its best rank-1 approximation $V_{t}'$ to reduce memory usage. While the original Adafactor paper proposed additional modifications, such as changes to the learning rate schedule, we focus on the version of Adafactor proposed in recent works, whose update with learning rate $\eta$ is given by Shampoo is a second-order optimization algorithm that approximates Adagrad and maintains two preconditioners, $L_{t} \in {\mathbb{R}}^{m \times m}$ and $R_{t} \in {\mathbb{R}}^{n \times n}$, for a given weight matrix $W \in {\mathbb{R}}^{m \times n}$. The updates for the preconditioners and the weights with learning rate $\eta$ are as follows: In practice, Shampoo is implemented with several other modifications such as layerwise learning rate grafting and exponents other than $- {1/4}$. We will use the DistributedShampoo implementation which has these variations available as hyperparameters.

## Related Work

We begin by discussing works that are closely related, including George et al.; Anil et al. and Zhao et al.. Subsequently, we cover extended related works.

KFAC is a well-known second-order optimization algorithm designed for neural networks. E-KFAC builds upon KFAC in a manner analogous to our extension of Shampoo, introducing a diagonal preconditioner that is updated between KFAC inversion steps. However, E-KFAC's algorithm is not identical to running Adam in KFAC's eigenbasis, as the diagonal preconditioner is not Adam.

Anil et al. introduced several algorithmic and numerical improvements to develop a practical and scalable version of Shampoo. Notably, they empirically found that using an exponent of $1/2$ outperforms the original exponent of $1/4$ in Shampoo. Of particular interest to our work is Appendix B of Anil et al., where, inspired by E-KFAC, they describe an algorithm that is essentially equivalent to SOAP for 2D layers. However, no experiments were provided, and the authors claimed that unpublished experiments showed no empirical improvement over Shampoo. This discrepancy between our findings may be due to some of the implementation details of SOAP.

GaLore was recently proposed as a method to reduce Adam's memory footprint by maintaining momentum in a low-rank subspace derived from the singular value decomposition (SVD) of the gradients. Their algorithm's full-rank version bears similarity to ours, with some notable distinctions. Firstly, their projection subspace is determined by the SVD of the current gradient, while we maintain an exponential moving average of $GG^{T}$ and $G^{T}G$. Secondly, we retain momentum in the original space and project it onto the preconditioned space, whereas they maintain it in the preconditioned space and do not rotate it each time the preconditioned space is updated. In Appendix B, we study GaLore's performance and find that our modifications are necessary for improving upon Shampoo. Moreover, their method only projects one side of a layer using the eigenbasis while using the identity basis on the other side. We examine the impact of one-sided projection for SOAP in Section 7.1.

Diagonal Preconditioning based Optimizers: Other than AdamW, there are other optimizers which involve diagonal preconditoning such as Lion, Sophia, and Adafactor. Recent works of Kaddour et al.; Zhao et al. showed that these optimizers perform comparably to AdamW for LLM pretraining but do not surpass it. This suggests the need to explore non-diagonal preconditioners. We discuss prior works on non-diagonal preconditioners below.

Second-Order Optimization: Research on second-order optimization in deep learning is generally divided into two categories: Hessian-free methods and methods that estimate the Hessian.

Hessian-Free Methods: Hessian-free approaches optimize without explicitly computing the Hessian matrix, instead employing iterative techniques to approximate the Newton step. Other recent works have focused on designing iterative preconditioners to improve the convergence specifically for stochastic optimization algorithms.

Hessian Estimation Methods: These methods maintain an efficient approximation of the Hessian for neural networks. KFAC and Shampoo are two widely recognized methods in this area.

KFAC was one of the first approaches to go beyond diagonal preconditioners in neural networks, demonstrating that a layer-wise Kronecker-factored preconditioner approximates the layer-wise Hessian in multi-layer perceptrons (MLPs). Subsequent works extended KFAC to other architectures. Recent research has further improved trace and diagonal estimates for KFAC. Efforts to scale up KFAC have focused on making the inversion step more efficient or enhancing distributed implementations.

Shampoo, another second-order optimization algorithm, is motivated by the online learning algorithm Adagrad. Shampoo also employs a layer-wise Kronecker-factored preconditioner. A recent distributed implementation of Shampoo won an optimization efficiency benchmark, highlighting the practical utility of second-order methods in deep learning. Few recent works have provided theoretical advancements on top of Shampoo. Other works have proposed various strategies to improve Shampoo's scalability. We defer a comparison of SOAP with these methods to future work.

## Algorithm

### Theory

We begin by describing an equivalence between Shampoo and running Adafactor in the eigenbasis of the Shampoo preconditioner. For simplicity we omit momentum but the equivalence also holds with momentum. For this equivalence we use Shampoo with the following modifications from the original Shampoo optimizer: We use power $1/2$ instead of power $1/4$. This was already recommended in practical implementations and a theoretical connection between optimal Kronecker approximation of Adagrad preconditioner and Shampoo with power $1/2$ was established in Morwani et al..

We also use the scalar correction to per layer learning rates described in Ren & Goldfarb; Morwani et al..

Instead of the running average of $L$ and $R$ across time steps, we use dataset averages.

With these changes in place (first occurrence of these changes is highlighted in red in the algorithm below) we formally define the two algorithms whose equivalence we show in Algorithms 1 and 2.

3: L ← 𝔼B[GBGBT] {Where the expectation is over a random batch B.} Algorithm 1 Single step of idealized Shampoo with power 1/2.

8: {Idealized version of code for Adafactor taking Gt′ to be the gradient} 12: ${\hat{V}}_{t} = \frac{AC^{T}}{\mathbf{1}_{n}^{\top}A}$ {Elementwise division} 13: $G_{t}^{\operatorname{\prime\prime}}\leftarrow\frac{G_{t}'}{\sqrt{{\hat{V}}_{t}} + \epsilon}$ {Elementwise division and square root} 14: Gt''' ← QLGt''QRT {Projecting back to original space} Algorithm 2 Single step of idealized Adafactor in Shampoo’s eigenspace.

### Claim 1

Algorithms 1 and 2 are equivalent.

### Proof

Consider $G_{t}$ in the basis created after rotating by $Q_{L},Q_{R}$ i.e. $G_{t}' = {Q_{L}^{T}G_{t}Q_{R}}$. Let the eigenvalues of ${\mathbb{E}}_{B}{\lbrack{G_{B}G_{B}^{T}}\rbrack}$ and ${\mathbb{E}}_{B}{\lbrack{G_{B}^{T}G_{B}}\rbrack}$ be given by $\lambda_{1},\ldots,\lambda_{m}$ and $\mu_{1},\ldots,\mu_{n}$ respectively. Algorithm 1 scales the $i,j$ coordinate by ${({{\lambda_{i}\mu_{j}}/{({\sum_{i}\lambda_{i}})}})}^{- {1/2}}$, while Algorithm 2 scales them by ${({{A_{i}C_{j}}/{({\sum_{i}A_{i}})}})}^{- {1/2}}$. We now show that $A_{i} = \lambda_{i}$, an analogous argument shows $C_{j} = \mu_{j}$.

While these two algorithms are equivalent in their idealized forms, practical considerations reveal some differences. Firstly, the algorithms differ when using running averages instead of dataset averages. Secondly, and more significantly in practice, we do not invert or compute the eigenvector decomposition of $L$ and $R$ at every step. This means that the "adaptivity" of learning rates in Shampoo is limited^22^2We note that practical implementations of Shampoo use grafting which allows for learning rate adaptivity at every step, but this adaptivity is restricted to a single scalar per layer. to the updates of $L$ and $R$. In contrast, with Adafactor in Shampoo's eigenspace, the second moment estimates (i.e., $A$ and $C$ in Algorithm 2) can be updated at every step as they are computationally inexpensive. Additionally, instead of using Adafactor, we can opt^33^3Though using AdamW over Adafactor only gives very small improvements in performance, see Figure 6 and Section 7.2. We also note that one can use any other diagonal preconditioner based optimizer in place of Adam, such as Lion, Sophia or Schedule-Free AdamW. for Adam, which offers more generality. Combining these insights leads to Algorithm 3 which can be interpreted as running Adam in Shampoo's eigenspace.

6: {Now we “run” Adam on G′} 8: $N'\leftarrow\frac{M'}{\sqrt{{\hat{V}}_{t}} + \epsilon}$ {Elementwise division and square root} 9: {Now that we have preconditioned by Adam in the rotated space, we go back to the original space.} 12: {End of gradient step, we now update L and R and possibly also QL and QR. } Algorithm 3 Single step of SOAP for a m × n layer. Per layer, we maintain four matrices: L ∈ ℝm × m, R ∈ ℝn × n and V, M ∈ ℝm × n. For simplicity we ignore the initialization and other boundary effects such as bias correction. Hyperparameters: Learning rate η, betas = (β1, β2), epsilon ϵ, and preconditioning frequency f. An implementation of SOAP is available at Algorithm 4 Eigenvectors function, implemented using power iteration and QR decomposition. Inputs: PSD matrix P and estimate of eigenvectors Q. If the estimate was exact we would have P = QDQT where D is the diagonal matrix with eigenvalues.

We now describe some additional implementation details: Algorithm 3 describes the behavior of the algorithm for 2D layers. Following Zhao et al., for 1D layers we run standard AdamW. This reduces the overhead as compared to standard implementations of Shampoo which solve an eigenvector problem for 1D layers too.

Following Wang et al., we compute eigenvectors of $L$ (and $R$) using one step of power method (Algorithm 4). This requires doing one matrix multiplication followed by QR decomposition. QR decomposition is faster than standard eigenvector decomposition in PyTorch. For the first iteration, eigenvectors are initialized by doing a standard eigenvector decomposition.

For layers with huge dimensions such as the first and last layer in language modeling transformers, maintaining the eigenvectors would be space and time prohibitive. For such dimensions we fix the rotation matrix ($Q_{L}$ or $Q_{R}$) to be identity. Note that if we fix both $Q_{L}$ and $Q_{R}$ to be identity for a 2D layer, we would recover Adam.

Algorithm 3 omits bias correction and weight decay for simplicity, but these are used in the actual implementation, identical to their use in AdamW.

The main focus of the next sections will be to explore the empirical performance of this algorithm and its variations. n Sections 7.2 and 7.3 we discuss the the space and time complexity of SOAP and how it can be improved.

## Experimental Methodology

Hyperparameter tuning: We begin with hyperparameter values suggested by prior research for both AdamW and Distributed Shampoo (e.g., $\beta_{2} = 0.95$). Initially, we conduct a learning rate sweep to determine the optimal learning rate for each optimizer. Once the optimal learning rate is identified, we perform two-dimensional sweeps for each of the remaining hyperparameters, where we vary the selected hyperparameter alongside the learning rate. The purpose of these sweeps is to demonstrate that our default hyperparameter settings are near-optimal, disregarding potential interactions between two non-learning-rate hyperparameters. A detailed discussion of the hyperparameter sweeps is provided in Appendix A.

Figure 2: Precise efficiency benefits of SOAP over AdamW and Shampoo for 360m (at 256k and 2m batch size) and 660m (at 2m batch size) model. For the precise methodology, refer to Section 5.

Throughput Measurement: We evaluate the throughput of each optimizer by measuring the number of tokens processed per second. At present, we perform these measurements on a single H100 GPU and utilize gradient accumulation to accommodate large batch sizes. While this approach may seem to disadvantage AdamW--- as the overhead of Shampoo/SOAP is compared against multiple gradient accumulation steps--- it is important to note that the overhead of Shampoo/SOAP can be amortized across layers by distributing the updates across multiple GPUs. This technique is employed in the distributed implementation of Shampoo. A comprehensive comparison of distributed implementations of these algorithms is left to future work.

Efficiency Benefits: Simply running SOAP for the same duration as Shampoo and AdamW cannot be directly used to calculate the efficiency benefit (in terms of training steps or wall-clock time) of using SOAP since we use a cosine schedule. Therefore, we run SOAP on $.5,.625,.75$ and $.875$ fraction of the training data and fit a scaling law of the form $a + {bN^{- \beta}}$ through the final losses obtained, where $N$ represents the number of training points and $a,b,\beta$ are the parameters of the fit. We show these points and the corresponding scaling laws obtained in Figure 2. This scaling law is then used to calculate the efficiency benefit in terms of training steps and wallclock time as shown in Figure 2. Here, the horizontal lines represent the final losses of AdamW and Shampoo.

## Language Modeling Experiments

In this section we focus on empirically comparing AdamW, DistributedShampoo, and SOAP on language modeling tasks.

Figure 3: Comparing performance of tuned runs for AdamW, Shampoo (using DistributedShampoo implementation) and SOAP. Shampoo and SOAP use preconditioning frequency of 10. We observe a ≥ 40% reduction in the number of iterations and a ≥ 35% reduction in wall clock time compared to AdamW, and approximately a 20% reduction in both metrics compared to Shampoo. See Figure 1 for 660m results, Sections 6.2 and 6.3 for ablations of preconditioning frequency and batch size respectively, and Section 5 for detailed calculation of efficiency improvement and experimental methodology.

### Measuring Efficiency Benefits

In Figure 1 (left and middle) and Figure 3 we show train loss curves for AdamW, Shampoo, and SOAP on 360m and 660m models with 2m token batch size and "chinchilla-optimal" i.e. 20x model size number of tokens. In these plots we observe that SOAP outperforms the other two optimizers. To directly calculate the efficiency benefit of SOAP, we also run SOAP with cosine decay for a shorter lr schedule, as shown in Figures 1 and 3. This allows us to approximate the following efficiency benefits (when batch size is set to 2m and preconditioning frequency to 10): $\geq {40\%}$ reduction in the number of iterations and $\geq {35\%}$ reduction in wall clock time compared to AdamW; $\approx {20\%}$ reduction in iterations and wall clock time as compared to Shampoo. Precise efficiency benefit calculations are presented in Figure 2(left and middle). In Section 6.4 we show that efficiency benefits of SOAP over AdamW are maintained for longer duration runs where #tokens = 100 $\times$ model size.

### Effect of Frequency of Finding Eigenvectors/Inverse

In Figure 1 (right), we compare SOAP and Shampoo with respect to preconditioning frequency. We observe the following: For all frequencies we tried from 1 to 100, both optimizers outperform AdamW.

At frequency 1, SOAP and Shampoo are quite close in performance.

At higher frequencies, the performance of both SOAP and Shampoo degrades but SOAP's performance degrades significantly slower than Shampoo's.

Figure 4: (left) Comparing the critical batch size of AdamW vs SOAP. We can see that SOAP improves the critical batch size, by being much closer to the ideal linear scaling with batch size as compared to AdamW. (right) Comparing performance of tuned runs for AdamW, Shampoo (using DistributedShampoo implementation) and SOAP for token batch size of 256k. Shampoo and SOAP use preconditioning frequency of 80. We observe a ≥ 25% reduction in the number of iterations compared to AdamW, and approximately a 10% reduction compared to Shampoo. See Figure 2 (right) for wall-clock time improvement and Section 5 for detailed calculation of efficiency improvement.

### SOAP Improves the Critical Batch Size

When scaling up batch sizes, the ideal outcome is that doubling the batch size results in halving the number of training steps needed to achieve the same performance. The batch size at which this ideal scaling starts to break down is referred to by McCandlish et al. as the critical batch size. As models and datasets grow larger, it becomes increasingly important to develop optimizers that support larger critical batch sizes, thereby reducing the serial runtime of a training run. In this subsection, we compare the critical batch sizes of AdamW and SOAP. Relative to our baseline setup of a 2 million batch size, when we decrease the batch size by a factor of $k$, we increase the preconditioning frequency by the same factor. This ensures that the FLOPS and wall clock multiplicative overhead for the eigenvector decomposition steps remains consistent with the 2 million batch size setting.

We start by training a 360 million parameter model with a batch size of 256k for a "Chinchilla-optimal" number of tokens (20 times the model size) using AdamW, achieving a loss of 2.842. This value is set as the target loss for our comparisons. In Figure 4 (left), we show the number of steps AdamW and SOAP require to reach this target loss as we vary the batch size. SOAP consistently requires fewer steps across all batch sizes, with the multiplicative benefits becoming more pronounced at larger batch sizes. Additionally, we compare these results to the ideal scenario (dashed line) of linear scaling, where doubling the batch size halves the number of steps. SOAP more closely follows the linear scaling trend compared to AdamW, indicating that it has a higher critical batch size in this setup.

In Figure 4 (right), we present the optimal runs for each optimizer (including Shampoo) at the smallest batch size we consider: 256k. SOAP outperforms both Shampoo and AdamW, reducing the number of iterations by 25% compared to AdamW, and by approximately 10% compared to Shampoo. Furthermore, in Figure 2 (right, bottom), we demonstrate that SOAP also achieves a wall-clock time improvement of $\geq {15\%}$ over AdamW and around 10% over Shampoo. We note that these results are a preliminary analysis for smaller batch size runs. Our approach of keeping the product of batch size and preconditioning frequency constant may not be optimal, and a better trade-off could likely be found. Furthermore, SOAP's overhead could potentially be reduced by performing $L$ and $R$ updates in lower precision (instead of fp32). Finally, the diminished efficiency gains of second-order methods at smaller batch sizes are consistent with prior findings.

### Scaling to Larger Token Counts

Thus far, our focus has been on Chinchilla-optimal token counts for a given model size. However, in many practical scenarios, models are trained on significantly larger token budgets to optimize inference costs and downstream performance. In Figure 5, we demonstrate that SOAP maintains its advantage Adam even in extended training runs.

Figure 5: Performance comparison of SOAP and Adam for longer duration training runs.

## Further Efficiency Improvements

In this section, we discuss space and time complexity of SOAP and provide an overview of potential avenues for further space and compute efficiency improvements in SOAP.

### One Sided Eigenbasis

As described in Section 3, Zhao et al. have an algorithm similar to ours. One of the differences is that they only project the smaller side of the layer using the eigenbasis while using identity as the rotation matrix for the larger side i.e. if $m < n$ we set $Q_{R} = I_{n}$ in Algorithm 3 and if $m > n$ we set $Q_{L} = I_{m}$. Doing this leads to a reduction in space usage as well as reduction of optimizer time overhead, which is discussed in Sections 7.2.1 and 7.3.1.

In Figure 6, it is evident that the one-sided projection results in slightly reduced performance compared to the original SOAP optimizer. However, it still performs on par , or marginally better than, Shampoo, while maintaining greater computational efficiency. Further investigation into the potential for these variants to surpass the computational efficiency of original SOAP optimizer is left for future work.

Figure 6: Performance of variants of SOAP which improve space usage or time overhead. 1. SOAP (factorized): Uses Adafactor instead of Adam in Shampoo’s eigenbasis and 2. SOAP (one-sided): Uses Q = I (i.e. no rotation) on the large side of weight matrix and 3. SOAP (factorized, one-sided): Combines both of these changes. We observe that while using Adafactor instead of Adam causes a negligible increase in loss, using the one-sided variant causes a larger increase. However, the one-sided variant also has much larger reduction in time and space overhead. For computational benefits of these variants see Sections 7.2 and 7.3.

### Space usage of SOAP

For a $m \times n$ matrix where $m > n$ we require space usage^44^4One $mn$ is for storing the gradients, this can be avoided (as long as there is no gradient accumulation) by applying gradients along with backprop but this is not implemented by default in standard deep learning frameworks such as PyTorch. Hence we will include this term in all of our calculations. (beyond weights and activations), specifically for $L,Q_{L},R,Q_{R},{\text{momentum~}{(M)}}$, AdamW's second order estimate ($V$), and the gradient. This is the same space usage as DistributedShampoo while AdamW uses $3mn$.

### Improving space usage of SOAP

The most direct way to reduce memory is using low precision to store the $L,R,Q_{L},Q_{R},V$ matrices, which is done by Dettmers et al.; Wang et al.. Orthogonal to the low precision approaches, there are two algorithmic approaches to improving the space usage of SOAP: Using Adafactor instead of Adam as the diagonal preconditioner after rotating by $Q_{L}$ and $Q_{R}$. This reduces the space usage by $mn$.

Using one sided version of SOAP (Section 7.1). This reduces space usage from ${2m^{2}} + {2n^{2}} + {3mn}$ to $2\min{(m,n)}^{2} + 3mn$.

Combining these approaches yields space usage of $2\min{(m,n)}^{2} + 2mn$.

For standard transformer architectures the last variant which combines the two approaches would yield less space usage overall compared to AdamW (which uses $3mn$).

We try these approaches in Figure 6. We observe that using Adafactor instead of AdamW yields very small reductions in performance while using one-sided preconditioner results in larger reductions. Nonetheless even after combining these two approaches the resulting optimizer outperforms AdamW while having a smaller space requirement than AdamW. Regarding space usage we also note that Adafactor (with momentum added back) itself utilizes only $2mn$ space usage and has been shown to perform comparable to AdamW for ViT training and for language model training. Further space reduction beyond Adafactor has been studied in the Adalomo, GaLore, and AdaMeM papers.

### Time Overhead of SOAP

There are two types of overhead of Shampoo and SOAP over AdamW: the overhead per step and the overhead when changing the preconditioner (or for SOAP, the preconditioner's eigenbasis). Let us first analyze the first one. For SOAP per step for a layer of size $m \times n$ we have an overhead of We note that this is more than the overhead of Shampoo which is $m^{3} + n^{3} + {m^{2}n} + {n^{2}m}$. This can be observed in Figure 2 (bottom, right) but not in the other figures since there the second type of overhead is the dominant term.

The second type of overhead is due to changing the preconditioner for Shampoo (or for SOAP, preconditioner's eigenbasis i.e. $Q_{L}$ and $Q_{R}$). The DistributedShampoo implementation of Shampoo uses a direct call to torch.linalg.eigh for this. Following Wang et al. we use Algorithm 4 which uses power iteration based approach which calls torch.linalg.qr. We note that torch.linalg.qr is faster than torch.linalg.eigh. In Figure 7 (right) we see that using power iteration based approach (torch.linalg.qr) performs as well as fresh eigenvector decomposition (torch.linalg.eigh).

Figure 7: (Left) Depicting the overhead of SOAP over AdamW as a function of preconditioning frequency (Right) Comparing the performance of SOAP with torch.linalg.eigh for computing the eigenvectors with Algorithm 4, which uses torch.linalg.qr. Note that torch.linalg.qr is computationally more efficient than torch.linalg.eigh (as mentioned in Documentation ); however, both seem to have comparable performance throughout the preconditioning frequency spectrum.

Effect of frequency on overhead: In Figure 7 (left), we observe that the overhead decreases as the preconditioning frequency increases, i.e., the frequency of invoking Algorithm 4. If the only additional computation occurred in Algorithm 4, we would expect the overhead to scale as $1.0/{(\text{preconditioning frequency})}$, approaching zero. However, empirical results (Figure 7 left) show that the overhead approaches an asymptote greater than zero. This is attributable to the additional matrix multiplications required to update $L$, update $R$, project the gradient, and reproject the gradient (for each layer) in the optimizer. Currently, these operations are performed in float32; reducing the precision of these operations, as proposed in Wang et al., could lower this asymptote.

### Improving time overhead of SOAP

The per step overhead of SOAP can be reduced by using low precision to store the $L,R,Q_{L},Q_{R},V$ matrices, which in turn will speed up computation done using these matrices. This approach cannot be used for reducing the overhead for the preconditioner update in popular deep learning frameworks such as Pytorch since torch.linalg.qr does not support precision lower than float32. Orthogonal to the low precision approach we can improve the per step time overhead of SOAP by the following algorithmic approaches: Using Adafactor instead of Adam (Section 7.2) as the diagonal preconditioner after rotating by $Q_{L}$ and $Q_{R}$. In this version of SOAP the overhead can be improved by from $m^{3} + n^{3} + {2m^{2}n} + {2n^{2}m}$ to $m^{3} + n^{3} + m^{2}n + n^{2}m + \max{(m,n)}^{2}\min{(m,n)} + \min{(m,n)}^{3}$ by merging the project and project back steps for the smaller dimension.

Using one sided version of SOAP (Section 7.1). This reduces overhead from $m^{3} + n^{3} + {2m^{2}n} + {2n^{2}m}$ to $\min{(m,n)}^{3} + 2\min{(m,n)}^{2}\max{(m,n)}$.

Combining these approaches yields an overhead of $\min{(m,n)}^{2}\max{(m,n)} + 2\min{(m,n)}^{3}$ Using one-sided version also reduces the second type of overhead from a calls to torch.linalg.qr on a $m \times m$ and a $n \times n$ matrix to only a single call to ${\min{(m,n)}} \times {\min{(m,n)}}$ matrix.

## Discussion and Future Work

We study an optimizer called SOAP: ShampoO with Adam in the Preconditioner's eigenbasis. We show that SOAP outperforms both AdamW and Shampoo in language modeling tasks and show that it is more robust to changes in preconditioning frequency than Shampoo. For future work, we would like to explore further improvements to the design of SOAP, in particular, related to using lower precision for the preconditioners as well as a better distributed implementation. We would also like to explore the performance of SOAP on other domains such as vision.

## Discussion and Limitations

We study an optimizer called SOAP: ShampoO with Adam in the Preconditioner's eigenbasis. We show that SOAP outperforms both AdamW and Shampoo in language modeling tasks and show that it is more robust to changes in preconditioning frequency than Shampoo. While we have explored many factors such as batch size (Section 6.3) and training duration (Section 6.4) we acknowledge that our study focuses on a relatively small scale compared to recent LLMs Touvron et al. which are two orders of magnitude bigger. We hypothesize that our findings on the performance of SOAP would generalize to larger scales due to its theoretical foundation. SOAP's robustness is also supported by the fact that SOAP is equivalent to running Adam in a rotated space, and Adam has proven to be effective across scale and tasks. However, this hypothesis remains to be validated.

For future work, we aim to improve the design of SOAP further, particularly by exploring the use of lower precision for preconditioners and optimizing its distributed implementation. Additionally, we are interested in testing SOAP's performance in other domains, such as vision, to evaluate its performance across different types of tasks.
