<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sketchy: Memory-Efficient Adaptive Regularization with Frequent Directions

Topics include Regularization, Sketching, Second-order optimization, Adaptive step size, Neural networks, Optimization, Machine learning efficiency.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Uses frequent-directions sketches to build a memory-efficient adaptive regularization method for training large models. Sketchy is positioned as a practical compromise between richer curvature information and the memory limits of standard adaptive optimizers.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Adaptive regularization methods that exploit more than the diagonal entries exhibit state of the art performance for many tasks, but can be prohibitive in terms of memory and running time. We find the spectra of the Kronecker-factored gradient covariance matrix in deep learning (DL) training tasks are concentrated on a small leading eigenspace that changes throughout training, motivating a low-rank sketching approach. We describe a generic method for reducing memory and compute requirements of maintaining a matrix preconditioner using the Frequent Directions (FD) sketch. While previous approaches have explored applying FD for second-order optimization, we present a novel analysis which allows efficient interpolation between resource requirements and the degradation in regret guarantees with rank k: in the online convex optimization (OCO) setting over dimension d, we match full-matrix d^ memory regret using only dk memory up to additive error in the bottom d-k eigenvalues of the gradient covariance. Further, we show extensions of our work to Shampoo, resulting in a method competitive in quality with Shampoo and Adam, yet requiring only sub-linear memory for tracking second moments.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

DL optimization commonly relies on adaptive gradient methods, namely the Adam optimizer. It differs from stochastic gradient descent in that the learning rate is a structured diagonal matrix built from previous gradients rather than a scalar. In full matrix AdaGrad, the inverse matrix square root of the sum of outer products of previous gradients is the learning rate.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Full matrix preconditioning is impractical for modern deep learning architectures: for instance, the ResNet-50 architecture has over 23 million parameters, requiring more than 2 petabytes to represent its gradient covariance. Thus, diagonal preconditioning methods remain popular. However, previous work has demonstrated state-of-the-art results in some settings, such as large-batch data parallel training, for nondiagonal forms of preconditioning. In particular, Shampoo introduces a factorization of full matrix preconditioning method with adoption in large-scale industrial applications such as training Google's ads click-through-rate model. Furthermore, as hardware evolves, memory efficiency becomes an increasing concern, as "logic improves much faster than wires and SRAM, so logic is relatively free": from TPUv2 to TPUv3, per-chip bfloat16 operations per second improved $2.67 \times$ but memory bandwidth only improved $1.29 \times$. GPUs exhibit a similar pattern for compute and memory increase, at $5 \times$ and $2.2 \times$, for V100 to A100.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Investigation into the Kronecker-factored gradient covariance matrix reveals a concentrated, but changing, spectrum (Fig. 3), suggesting the majority of the spectral mass can be represented by a low-rank matrix, albeit rotating over time. The Frequent Directions (FD) sketch provides a mechanism to track the top eigenvectors without materializing the full covariance matrix, as proposed. Is a large portion of the spectral mass sufficient to retain the performance of adaptive regularization in theory and practice? In this work, we investigate this hypothesis.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the setting of online convex optimization, by applying a dynamic diagonal regularization to the FD sketch, we can recover full-matrix AdaGrad regret up to additive spectral terms under a memory constraint, providing a novel guarantee without curvature assumptions (Sec. 4.1). Rigorously composing our approach with Shampoo (Sec. 4.2) unlocks a second-order algorithm which requires sub-linear memory for its accumulators.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

By modifying FD for exponential moving averages (Sec. 4.3), we demonstrate a practical algorithm competitive with at-least-linear memory Shampoo and Adam in three modern DL settings (Sec. 5.1). While previous work shows rank-1 preconditioners are effective for trading off quality for memory, these results demonstrate a Pareto improvement by using higher-rank approximations.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We explain the competitive performance of Sketchy with observations of fast spectral decay in the moving average of Kronecker-factored gradient covariance in DL settings (Sec. 5.2).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Regret and Optimization", "weight": 1.0} -->

The optimization problem of training a deep neural network has a non-convex objective loss function $f$. Since finding the global optimum is computationally intractable in general, theoretical guarantees focus on convergence to an $\varepsilon$-approximate first-order optimum: a point $x$ such that ${\|{{\nabla f}{(x)}}\|} \leq \varepsilon$. A smooth non-convex problem can be reduced to solving a series of offline convex problems. The convex sub-problems have form ${f_{t}{(x)}} = {{f{(x)}} + {c{\|{x - x_{t}}\|}^{2}}}$, where $c$ is a constant and $x_{t}$ is an iterate in the optimization process. Using online-to-batch conversion, we can translate the regret bound of an online convex optimization (OCO) algorithm to convergence guarantees for offline optimization. For more details of this reduction, see Appendix B.1.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Regret and Optimization", "weight": 1.0} -->

Therefore, non-convex optimization guarantees can be obtained from regret bounds, and we focus on the latter in this paper.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Regret and Optimization", "weight": 1.0} -->

In this setting, an OCO algorithm chooses a point $x_{t} \in \mathcal{K}$ iteratively, where $\mathcal{K} \subseteq {\mathbb{R}}^{d}$ is a convex decision set (take $\mathcal{K} = {\mathbb{R}}^{d}$ if unconstrained). After the decision is made, the adversary reveals a convex loss function $f_{t}$, to which the algorithm suffers cost $f_{t}{(x_{t})}$. Upon receiving the cost, the algorithm updates its decision for the next iteration. The regret for an online algorithm is given by

<!-- chunk {"id": "body-0013", "role": "body", "section": "Sketching and the Frequent Directions Method", "weight": 1.0} -->

Given a stream of vectors $g_{t} \in {\mathbb{R}}^{d}$, $t \in {\lbrack T\rbrack}$, we utilize the FD sketch given in Alg. 1 which maintains a low-rank approximation of the true running covariance $G_{t} = {\sum_{s \leq t}{g_{s}g_{s}^{\top}}}$. At each time $t$, it maintains a matrix $B_{t}$ of size $d \times \ell$ whose last column is $0$ and whose square is the sketch ${B_{t}B_{t}^{\top}} = {\overline{G}}_{t}$. After seeing $g_{t}$ from the stream, we update the previous matrix using Alg. 1, which updates $B_{t + 1}$ of size $d \times \ell$ whose last column remains $0$; take $B_{0} = 0$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Sketching and the Frequent Directions Method", "weight": 1.0} -->

$B_{t + 1}$ is obtained by decomposing the sum of ${\overline{G}}_{t}$ and the newly observed matrix, keeping only the top eigendirections, and reducing the eigenvalues uniformly by $\ell$-th eigenvalue. At every iteration $t$, denote $\rho_{t}:=\lambda_{\ell}^{(t)}$ be the removed eigenvalue from the covariance update in Alg. 1.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Sketching and the Frequent Directions Method", "weight": 1.0} -->

For convenience, let $\rho_{1:t}\overset{\text{def}}{=}{\sum_{s = 1}^{t}\rho_{s}}$ be the cumulative escaped mass. For a matrix $X$, we denote its $i$-th leading eigenvalue by $\lambda_{i}{(X)}$. Let $\parallel \cdot \parallel_{F}$ denote the Frobenius norm of a matrix.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Sketching and the Frequent Directions Method", "weight": 1.0} -->

0: Invariant that last column of Bt − 1 is 0. 0: The last column of Bt is 0. 1: Input: Previous state ${\overline{G}}_{t - 1} = {B_{t - 1}B_{t - 1}^{\top}} \in {\mathbb{R}}^{d \times d}$
2: Input: New symmetric PSD matrix Mt ∈ ℝd × d. 3: Eigendecompose ${{\overline{U}}_{t}{{diag}{\lambda^{(t)}{\overline{U}}_{t}^{\top}}}} = {{\overline{G}}_{t - 1} + M_{t}}$ where λ(t) contains descending eigenvalues. 4: Define Ut as the matrix whose columns are the first ℓ columns of ${\overline{U}}_{t}$, and λ[1: ℓ](t) be its eigenvalues.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Sketching and the Frequent Directions Method", "weight": 1.0} -->

5: Update Bt = Utdiag(λ[1: ℓ](t)−λℓ(t))1/2. λℓ(t), BtBt⊤. Algorithm 1 Frequent Directions Update (FD-update)

<!-- chunk {"id": "body-0018", "role": "body", "section": "Sketching and the Frequent Directions Method", "weight": 1.0} -->

The fundamental property of FD is that applying Alg.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Spectral Analysis of DL Training", "weight": 1.0} -->

Denote the loss function of the $i$-th example for weights $x$ as $f_{i}{(x)}$. The spectrum of the Hessian matrix $\sum_{i}{\nabla^{2}f_{i}}$ has been the subject of intensive investigation in DL and its properties have been used to devise training methods.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Spectral Analysis of DL Training", "weight": 1.0} -->

Recent papers inspect the covariance matrix, $\sum_{i}{{({\nabla f_{i}})}{({\nabla f_{i}})}^{\top}}$. In small models, where its computation is feasible, these works identify fast spectral decay.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Spectral Analysis of DL Training", "weight": 1.0} -->

Agarwal et al. take advantage of this observation by using a low-rank approximation of the whole covariance matrix, based on a limited history of the gradients, $\sum_{i = {t - r}}^{r}{{({\nabla f_{i}})}{({\nabla f_{i}})}^{\top}}$. This approach still requires $r$ copies of the model gradients in memory, where typically $r$ should scale with $\beta_{2}^{- 1}$, with $\beta_{2}$ the exponential moving average for second order statistics (the authors set $r = 200$). Fundamentally, approximating the whole covariance matrix constrains Agarwal et al. application to small models.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Spectral Analysis of DL Training", "weight": 1.0} -->

In our work, we validate the decay hypothesis holds across the per-layer factored covariance matrices in several modern neural networks. For a layer's gradient matrix $G_{i}$ at the $i$-th example and a second moment decay term $\beta_{2}$, our work inspects spectral decay for $L_{t} = {\sum_{i}{\beta_{2}^{t - i}G_{i}G_{i}^{\top}}}$ and $R_{t} = {\sum_{i}{\beta_{2}^{t - i}G_{i}^{\top}G_{i}}}$; the spectral structure for these outer products is not well-documented. Furthermore, as described in Sec. 3.4, approximating the factored covariance $L_{t} \otimes R_{t}$ requires less memory than the full covariance and explains why our method can scale to large modern architectures whereas Agarwal et al. cannot.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Sublinear Memory Methods", "weight": 1.0} -->

Extreme Tensoring, AdaFactor, and SM3 are methods that require sublinear memory relative to the number of parameters, at the other end of the memory-quality tradeoff beyond methods that rely on the diagonal of the gradient covariance such as Adam. Owing to different structural assumptions on the set of feasible preconditioners, comparison with these methods is out of scope. However, these methods may compose with our approach. One may apply Extreme Tensoring first, then sketch the resulting reshaped tensor covariances with our method to further reduce memory consumption. Similarly, an SM3-like approach which reduces the indices for each dimension to be preconditioned can be applied before Sketchy is applied to remaining indices.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Sublinear Memory Methods", "weight": 1.0} -->

Crucially, Adam, which uses linear memory for second moment representations, compares favorably in terms of quality to all of these sublinear-memory methods. By increasing rank in factored covariance representation, Sketchy is competitive with Adam, despite sublinear memory for second moment representation. Thus, for simplicity, we compare to only Adam, which dominates the alternative sublinear approaches in terms of quality.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Sketching-based Approaches", "weight": 1.0} -->

Ω(T3/4)111The regret of Ada-FD is expressed in terms of dynamic run-time quantities which do not admit a universal bound in terms of GT; we display its regret for the specific case of Observation 2 instead (a detailed look at its regret is given in Appendix B.3).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Sketching-based Approaches", "weight": 1.0} -->

Several works have explored sketching-like approximations to the gradient covariance matrix, but none provide an adaptive bound exploiting fast spectral decay in gradient covariance without additional assumptions (Tbl. 1). In this section, we consider the OCO setting over dimension $d$ (Sec. 2).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Sketching-based Approaches", "weight": 1.0} -->

Random projection (Ada-LR) is most spiritually similar to our work. Although it does not reduce memory usage, it relies on random projections to lower dimension $\ell \leq d$ to reduce inverse matrix computation costs. An alternative without formal guarantees, RadaGrad, reduces memory consumption to $O{({d\ell})}$; however, as with all Johnson-Lindenstraus projection methods, it suffers a probabilistic failure rate scaling as $O{(\ell^{- 1})}$ (in comparison, our method inherits FD's determinism).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Sketching-based Approaches", "weight": 1.0} -->

Frequent Directions (FD), provides an alternative matrix sketching approach from the data streaming literature. As an adaptive sketch, it dominates random projection in terms of matrix recovery, and lower bounds show its memory usage is optimal in the sense that any equally-accurate approximation to an adversarially-chosen true covariance $G_{T}$ in operator norm constructed from the corresponding gradients must use $O{({d\ell})}$ bits.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Sketching-based Approaches", "weight": 1.0} -->

In the context of exp-concave cost functions, Luo et al. provide an FD sketched version of Online Newton Step (ONS), FD-SON. In this setting, their approach nearly recovers classical ONS regret, up to logarithmic error in $\sum_{i = 1}^{\ell - 1}{\lambda_{i}{(G_{T})}}$ and additive error in $\sum_{i = \ell}^{d}{\lambda_{i}{(G_{T})}}$. However, without the exp-concave assumption, FD-SON falls back to a gradient-descent-like default regret of $O\left( {\lambda_{\ell:d}\sqrt{T}} \right)$, which can be $\Omega{(T)}$ without spectral decay. In the context of linear bandits, Chen et al. uses FD for memory reduction. The resulting algorithm, SCFD, is similar to Alg.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Sketching-based Approaches", "weight": 1.0} -->

2, but SCFD lacks a projection step and does not handle general domains $\mathcal{K}$. We emphasize that our contribution is in the novelty of our regret analysis for general OCO settings, in contrast to linear bandits.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Sketching-based Approaches", "weight": 1.0} -->

The main prior work exploring FD for general online convex settings, Wan and Zhang, extends the FD-SON approach by adding a fixed diagonal perturbation $\delta I$ to an FD-based preconditioner, in Ada-FD. However, this approach does not achieve $\sqrt{T}$ regret even in a non-adversarial setting with stochastic linear cost functions (Observation 2), where learning rate and $\delta$ are tuned. Dynamically changing diagonal regularization is essential for worst-case $O\left( \sqrt{T} \right)$ performance.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Observation 2", "weight": 1.0} -->

Suppose we receive linear cost functions ${f_{t}{(x)}} = \left\langle x,g_{t} \right\rangle$, where $g_{t} \in {\mathbb{R}}^{d}$ is a random vector drawn iid from any distribution over $r \leq d$ orthonormal vectors $W$. For any sketch size $\ell \leq r$, the bound on the expected regret of Ada-FD is $\Omega{(T^{3/4})}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Shampoo", "weight": 1.0} -->

Perhaps our most compelling application is reducing the memory of Shampoo. Shampoo is an adaptive preconditioning method that takes into account the structure of the parameter space, and thus is more efficient than full matrix AdaGrad. For example, if the parameter is a weight matrix $W$ of size $m \times n$, AdaGrad treats the matrix-shaped parameters as a vector of size $mn$, and the preconditioner has size $m^{2}n^{2}$; Shampoo instead has left and right preconditioners $L,R$ of size $n \times n$ and $m \times m$, respectively, with the preconditioned update $L^{- {1/4}}WR^{- {1/4}}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Shampoo", "weight": 1.0} -->

Write $\overline{\text{vec}}(W)$ as the vectorized weights, then it is equivalent to ${{({L \otimes R})}\overline{\text{vec}}(W)} = {\overline{\text{vec}}\left( {LWR} \right)}$, where $\otimes$ denotes the Kronecker product. Figure 1 illustrates the updates of AdaGrad and Shampoo, where AdaGrad update uses the entire matrix instead of the diagonal, which is shown in the figure. In other words, Shampoo uses a Kronecker-factored preconditioner, and the factorization preserves the matrix structure of the parameters. Since in DL optimization parameters often have matrix structure, Shampoo has strong empirical performance, and has improved upon state-of-the-art results in large-scale tasks such as language modeling with BERT-Large and image classification on ImageNet.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Shampoo", "weight": 1.0} -->

However, Shampoo memory costs may still be prohibitive for rectangular weight matrices. In BERT-Large, most parameters are in the feed-forward network layers, which consist of $4096 \times 1024$ dense kernels; other transformers follow similar narrow-to-wide patterns. For large models, occupying even $4 \times$ memory for the left preconditioner can frequently result in OOM in memory-constrained settings; this was in fact one of the practical motivations for our proposed approach.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Shampoo", "weight": 1.0} -->

Anil et al. introduces two workarounds for the problem of rectangular matrices based on limiting covariance modelling. Furthermore, both approximations can be applied to our method, so we do not compare against them. First, the authors propose Blocked Shampoo, which views each weight matrix $W$ of shape $m \times n$ as ${mn}/b^{2}$ blocks of size $b \times b$ for some block size $b < {\min{(m,n)}}$ (in the limit $b = 1$, this recovers diagonal AdaGrad). This approach is dependent on the ordering of neurons in hidden layers. Another approximation relies on only one-sided covariance upper bounds, $L_{t} \otimes I$ or $I \otimes R_{t}$. Note, however, that the one-sided approximation doesn't help with vector parameters, such as those that appear for the bias terms in dense layers or layer norms. For 3D weights, such as those which appear in homogeneous Mixtures of Experts, blocking increases memory consumption.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Shampoo", "weight": 1.0} -->

These approaches do not take into account the fast decay of the preconditioner's spectrum, which is the focus of our work.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Algorithms and Main Theorems", "weight": 1.0} -->

In this section, we introduce the adaptation of Frequent Directions (FD) to AdaGrad (Sec. 4.1) and Shampoo (Sec. 4.2), the corresponding algorithms and regret guarantees. Additionally, in Sec. 4.3, we modify FD to support exponential moving averages.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Algorithms and Main Theorems", "weight": 1.0} -->

The main technical novelty in incorporating Alg. 1 to AdaGrad (Alg. 2) and Shampoo (Alg. 3) is the construction of preconditioning matrices with FD-sketched matrices compensated by the cumulative escaped masses. The insight of such construction lies in the observation that while the FD sketch lower bounds the full preconditioning matrix, the FD sketch compensated with the cumulative escaped masses upper bounds the full preconditioning matrix, as demonstrated in Lemma 10 for AdaGrad and Lemma 14 for Shampoo. The regret guarantee for AdaGrad and Shampoo directly depends on the trace of the preconditioning matrices, therefore obtaining upper and lower bounds on the preconditioning matrices allows explicit additive dependence on the cumulative escaped mass. We expect this approach to be reusable for alternative approximation schemes.

<!-- chunk {"id": "body-0040", "role": "body", "section": "FD for AdaGrad", "weight": 1.0} -->

Our main algorithm in this section is Alg. 2 run with FD (Alg. 1) as the sketching method. ${\overset{\sim}{G}}_{t}^{- {1/2}}$ in Alg. 2 denotes the Moore-Penrose pseudoinverse of the matrix ${\overset{\sim}{G}}_{t}^{1/2}$. Our main algorithm, Sketchy AdaGrad, in this section exploits the FD approach outlined in Alg. 1 as the sketching method in AdaGrad. In particular, at every time step, we pass the newly received subgradient $g_{t}$ into Alg. 1, which updates and maintains a low-rank sketch ${\overline{G}}_{t}$ of the AdaGrad preconditioning matrix $G_{t}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "FD for AdaGrad", "weight": 1.0} -->

We keep track of the cumulative escaped mass $\rho_{1:t}$, which we add back to the low-rank sketch to create the Sketchy preconditioner ${\overset{\sim}{G}}_{t}$, with which we perform the regular AdaGrad descent and projection.

<!-- chunk {"id": "body-0042", "role": "body", "section": "FD for Shampoo", "weight": 1.0} -->

In this section, we adapt FD-update to Shampoo. For simplicity, we optimize over ${\mathbb{R}}^{m \times n}$ in Alg. 3; projection may be handled as in Alg. 2. Similar to Sketchy AdaGrad, Sketchy Shampoo uses the FD approach outlined in Alg. 1 to sketch the left and right preconditioning matrices for Shampoo. In particular, we maintain two parallel sketching streams using Alg. 1 to produce sketches ${\overline{L}}_{t},{\overline{R}}_{t}$ for the left and right preconditioning matrices.

<!-- chunk {"id": "body-0043", "role": "body", "section": "FD for Shampoo", "weight": 1.0} -->

We keep track of the cumulative escaped masses $\rho_{1:t}^{L}$ and $\rho_{1:t}^{R}$ from sketching the left and right preconditioning matrices, respectively, and compensate the cumulative escaped mass to create the left and right Sketchy preconditioning matrices ${\overset{\sim}{L}}_{t},{\overset{\sim}{R}}_{t}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Exponentially Weighted FD", "weight": 1.0} -->

This section discusses the modification of Alg. 1 to support exponential moving averages. Early in algorithm development, we noticed that attempting to approximate the unweighted sum of factored gradient covariances $\sum_{t}{G_{t}G_{t}^{\top}}$ and $\sum_{t}{G_{t}^{\top}G_{t}}$ with FD tended to an estimate of covariance that was roughly $0$, creating numerical instabilities. Note that FD guarantee (Lem. 1. ‣ Sketching and the Frequent Directions Method. ‣ 2 Setting and Definitions ‣ Sketchy: Memory-efficient Adaptive Regularization with Frequent Directions")) still holds---but the error term $\rho_{1:T}$ becomes greater than $\left. \parallel G_{T}\parallel \right.$, resulting in a vacuous bound due to lack of spectral decay.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Experiments", "weight": 1.0} -->

We investigate how much of Shampoo's quality our low-memory approach can recover (Sec. 5.1) and whether the factored covariance exhibits spectral decay amenable to sketching (Sec. 5.2). We relegate convex examples to Appendix A due to space constraints, which check that Sketchy compares favorably to related work in a setting directly related to the theory.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Deep Neural Networks", "weight": 1.0} -->

We evaluate the effectiveness of S-Shampoo as a practical second-order algorithm for training networks, including

<!-- chunk {"id": "body-0047", "role": "body", "section": "Deep Neural Networks", "weight": 1.0} -->

ResNet-50 for ImageNet image classification task of ImageNet with random cropping and flipping augmentations.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Deep Neural Networks", "weight": 1.0} -->

A 16-layer Conformer model for the audio transcription task, Librispeech.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Deep Neural Networks", "weight": 1.0} -->

A GNN with 5 message-passing steps on ogbg-molpcba, which classifies structural properties of graphically encoded molecule inputs.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Deep Neural Networks", "weight": 1.0} -->

Our FD variant of Shampoo introduces only one new hyperparameter, the rank $\ell$, which we do not tune, but set to $\ell = 256$, which translates to $4 \times$ memory savings for Shampoo blocks of size $1024$ for the accumulators. Shampoo, Adam, and the underlying architectures introduce their own hyperparameters. S-Shampoo inherits those of Shampoo. We tune only common parameters between the three optimizers with the same budgets, selecting based on validation set accuracy. In the ImageNet case, we evaluate final test set performance using ImageNet v2, as the ImageNet test set is unavailable. Additinoal training information is available in Appendix C.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Deep Neural Networks", "weight": 1.0} -->

As Fig. 2 demonstrates, the second-order information leveraged by Shampoo results in improvements over Adam, a first-order method. Our method performs at least as well as Adam in all cases, despite using asympotically less memory to represent covariance (as Fig. 1 shows, Adam uses $O{({mn})}$ for a rectangular weight matrix's diagonal accumulators, whereas S-Shampoo uses $O{({{mk} + {nk}})}$). In the GNN case (OBGB-MolPCBA), Shampoo does not perform as well; its training curves indicate overfitting, but we note that S-Shampoo was less susceptible to overfit like Adam.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Spectral Analysis", "weight": 1.0} -->

To explain Sketchy's strong performance in Sec. 5.1, we inspect the exponential moving average of Kronecker-factored gradient covariance for fast spectral decay. We find that this is indeed the case in practice, so Sketchy's low-rank plus diagonal covariance is representative of true training statistics.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Spectral Analysis", "weight": 1.0} -->

For all our architectures, we tune Shampoo and extract the intermediate gradient covariances over the course of training. To make our curves comparable across architectures, we fix the parameter for the second moment, $\beta_{2} = 0.999$ for these runs. Furthermore, ResNet-50 has a few parameters with dimension 2048, but the largest dimension for any parameter from the other two architectures is 1024, so we use the Blocked Shampoo variant discussed in Sec. 3.4 with block size 1024. In other words, weights containing a dimension 2048 are split into two. We tune other Shampoo parameters for each architecture, and plot statistics of Kronecker factors $L_{t} = {\sum_{i}{\beta_{2}^{t - i}G_{t}G_{t}^{\top}}}$ and $R_{t} = {\sum_{i}{\beta_{2}^{t - i}G_{t}^{\top}G_{t}}}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Spectral Analysis", "weight": 1.0} -->

In Fig. 3, we plot the intrinsic dimension of Kronecker covariance factors over training for our three settings. The intrinsic dimension determines the rate at which empirical covariance estimates concentrate to their expectation, rather than a random vector's actual dimension, up to logarithmic factors (Vershynin, Remark 5.6.3). Despite actual dimensionality being over 1024, intrinsic dimension across all architectures stays below 105. A conspicuous phase shift 10% of the way through training may be the result of a change from linear learning rate warmup to a learning rate decay, starting at roughly 5% of the way into training.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Spectral Analysis", "weight": 1.0} -->

Given $\beta_{2} = 0.999$, we emphasize that the behavior in Fig. 3 is an emergent property of DL training. Though surely a lower $\beta_{2}$ would naturally result in lower intrinsic dimension (which can still be taken advantage of by Alg. 2 and 3), we would still expect higher intrinsic dimension if covariances were near-isometries. If we observe some large number $n = 10000$ draws $x_{i}$ of $1024 \times d$ matrices with iid $N{}$ entries, then numerical experiments show that the average intrinsic dimension of $\sum_{i = 0}^{n - 1}{\beta_{2}^{i}x_{i}x_{i}^{\top}}$ is $324.63$ ($0.52$) and $862.13$ ($0.25$) for $d = {1,64}$, respectively, with parenthesized numbers denoting standard error across 20 trials.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Spectral Analysis", "weight": 1.0} -->

Values generated this way are larger than the average intrinsic dimension of roughly 10, 30, 50 observed in Fig. 3.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Discussion", "weight": 1.5} -->

Up to spectral error, Alg. 2 achieves full-matrix AdaGrad regret despite approximating the *smallest* part of the spectrum of $G_{t}^{- {1/2}}$ at each step. Remarkably, these eigenvectors correspond to the *most* easily discernible signals of the covariance for the stream $g_{t}$. This apparent (and fortuitous) coincidence is resolved by considering the covariance of ${\overset{\sim}{G}}_{t}^{- {1/2}}g_{t}$: whitening the gradient to facilitate optimization best reflects on regret; as a result, approximating top eigenvectors of $G_{T}$ helps more than the bottom ones.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our initial implementation focused on correctness rather than physical speed or memory reduction. Engineering optimizers competitive with existing industrial-strength implementations of Adam and Shampoo was out of scope. In implementing FD, we performed updates via the factored SVD of $\lbrack{\beta_{2}^{1/2}B_{t}};G_{t}\rbrack$ rather than the eigendecomposition depicted in Alg. 1; this avoids squaring, which is unavoidable in Shampoo. For speed, Shampoo subsamples gradients for its covariance estimation and updates its inverse matrix roots intermittently, every fixed number of steps. A tuning script provided by Anil et al. included gradients from every step, but updated roots every 10 steps. Since FD does not separate sampling from its computation of estimated covariance eigendecomposition, we took the more difficult setting for S-Shampoo, only allowing it to simultaneously observe every 10^th^ gradient and update its covariance inverse roots (see Appendix G for a theoretical justification).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Discussion", "weight": 1.5} -->

Though step-skipping makes Shampoo and S-Shampoo tractable, future work may explore further speedups: since FD only requires the top $\ell$ eigenvalues, iterative Lanczos-like routines which are accelerator-friendly, such as LOBPCG, may allow incremental updates to ${\overset{\sim}{G}}_{t}^{- {1/2}}$ in factored form with only a few matrix multiplies, S-Shampoo may be able to update more frequently than its non-sketched counterpart, further improving quality.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we address a gap in the OCO literature for low-memory optimization with the novel Alg. 2 and demonstrate its relevance to practical non-convex problems such as neural net training (Sec. 5.1) by leveraging a new observation about gradient covariance (Sec. 5.2).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The growing disparity between compute capability and memory bandwidth underscores the need for further research in this direction. Further, large-batch settings reduce the performance gap between first and Shampoo-based second order methods, since the batch-size independent runtime of the optimizer is amortized per example used for the gradient calculation. Even in performing experiments for this work, we would frequently find that faster accelerators were unavailable, but many previous-generation ones were, encouraging us to leverage data-parallel training. For datasets such as Imagenet, we notice the advantage of second order methods in dealing with large batches even at relatively modest sizes, such as 1024; many works on explore several larger multiples of this.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Potential for future work includes numerical methods outlined in the previous section as well optimizing the rank $\ell$ across the many tensors in a network, as the spread in Fig. 3 highlights the large variance in covariance intrinsic dimension. Furthermore, the inductive biases conferred by the minima which different-rank representations of curvature reach may have problem-dependent generalization implications, a question which we leave for future work. For a comparison of full rank preconditioning's effect versus first-order minima, see Amari et al..
