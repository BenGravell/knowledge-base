## Introduction

DL optimization commonly relies on adaptive gradient methods, namely the Adam optimizer. It differs from stochastic gradient descent in that the learning rate is a structured diagonal matrix built from previous gradients rather than a scalar. In full matrix AdaGrad, the inverse matrix square root of the sum of outer products of previous gradients is the learning rate.

Full matrix preconditioning is impractical for modern deep learning architectures: for instance, the ResNet-50 architecture has over 23 million parameters, requiring more than 2 petabytes to represent its gradient covariance. Thus, diagonal preconditioning methods remain popular. However, previous work has demonstrated state-of-the-art results in some settings, such as large-batch data parallel training, for nondiagonal forms of preconditioning. In particular, Shampoo introduces a factorization of full matrix preconditioning method with adoption in large-scale industrial applications such as training Google's ads click-through-rate model. Furthermore, as hardware evolves, memory efficiency becomes an increasing concern, as "logic improves much faster than wires and SRAM, so logic is relatively free": from TPUv2 to TPUv3, per-chip bfloat16 operations per second improved $2.67 \times$ but memory bandwidth only improved $1.29 \times$. GPUs exhibit a similar pattern for compute and memory increase, at $5 \times$ and $2.2 \times$, for V100 to A100.

Investigation into the Kronecker-factored gradient covariance matrix reveals a concentrated, but changing, spectrum (Fig. 3), suggesting the majority of the spectral mass can be represented by a low-rank matrix, albeit rotating over time. The Frequent Directions (FD) sketch provides a mechanism to track the top eigenvectors without materializing the full covariance matrix, as proposed in. Is a large portion of the spectral mass sufficient to retain the performance of adaptive regularization in theory and practice? In this work, we investigate this hypothesis.

In the setting of online convex optimization, by applying a dynamic diagonal regularization to the FD sketch, we can recover full-matrix AdaGrad regret up to additive spectral terms under a memory constraint, providing a novel guarantee without curvature assumptions (Sec. 4.1). Rigorously composing our approach with Shampoo (Sec. 4.2) unlocks a second-order algorithm which requires sub-linear memory for its accumulators.

By modifying FD for exponential moving averages (Sec. 4.3), we demonstrate a practical algorithm competitive with at-least-linear memory Shampoo and Adam in three modern DL settings (Sec. 5.1). While previous work shows rank-1 preconditioners are effective for trading off quality for memory, these results demonstrate a Pareto improvement by using higher-rank approximations.

We explain the competitive performance of Sketchy with observations of fast spectral decay in the moving average of Kronecker-factored gradient covariance in DL settings (Sec. 5.2).

## Setting and Definitions

### Regret and Optimization

The optimization problem of training a deep neural network has a non-convex objective loss function $f$. Since finding the global optimum is computationally intractable in general, theoretical guarantees focus on convergence to an $\varepsilon$-approximate first-order optimum: a point $x$ such that ${\|{{\nabla f}{(x)}}\|} \leq \varepsilon$. A smooth non-convex problem can be reduced to solving a series of offline convex problems. The convex sub-problems have form ${f_{t}{(x)}} = {{f{(x)}} + {c{\|{x - x_{t}}\|}^{2}}}$, where $c$ is a constant and $x_{t}$ is an iterate in the optimization process. Using online-to-batch conversion, we can translate the regret bound of an online convex optimization (OCO) algorithm to convergence guarantees for offline optimization. For more details of this reduction, see Appendix B.1. Therefore, non-convex optimization guarantees can be obtained from regret bounds, and we focus on the latter in this paper.

In this setting, an OCO algorithm chooses a point $x_{t} \in \mathcal{K}$ iteratively, where $\mathcal{K} \subseteq {\mathbb{R}}^{d}$ is a convex decision set (take $\mathcal{K} = {\mathbb{R}}^{d}$ if unconstrained). After the decision is made, the adversary reveals a convex loss function $f_{t}$, to which the algorithm suffers cost $f_{t}{(x_{t})}$. Upon receiving the cost, the algorithm updates its decision for the next iteration. The regret for an online algorithm is given by

### Sketching and the Frequent Directions Method

Given a stream of vectors $g_{t} \in {\mathbb{R}}^{d}$, $t \in {\lbrack T\rbrack}$, we utilize the FD sketch given in Alg. 1 which maintains a low-rank approximation of the true running covariance $G_{t} = {\sum_{s \leq t}{g_{s}g_{s}^{\top}}}$. At each time $t$, it maintains a matrix $B_{t}$ of size $d \times \ell$ whose last column is $0$ and whose square is the sketch ${B_{t}B_{t}^{\top}} = {\overline{G}}_{t}$. After seeing $g_{t}$ from the stream, we update the previous matrix using Alg. 1, which updates $B_{t + 1}$ of size $d \times \ell$ whose last column remains $0$; take $B_{0} = 0$. $B_{t + 1}$ is obtained by decomposing the sum of ${\overline{G}}_{t}$ and the newly observed matrix, keeping only the top eigendirections, and reducing the eigenvalues uniformly by $\ell$-th eigenvalue. At every iteration $t$, denote $\rho_{t}:=\lambda_{\ell}^{(t)}$ be the removed eigenvalue from the covariance update in Alg. 1.

For convenience, let $\rho_{1:t}\overset{\text{def}}{=}{\sum_{s = 1}^{t}\rho_{s}}$ be the cumulative escaped mass. For a matrix $X$, we denote its $i$-th leading eigenvalue by $\lambda_{i}{(X)}$. Let $\parallel \cdot \parallel_{F}$ denote the Frobenius norm of a matrix.

0: Invariant that last column of Bt − 1 is 0.
0: The last column of Bt is 0.
1: Input: Previous state ${\overline{G}}_{t - 1} = {B_{t - 1}B_{t - 1}^{\top}} \in {\mathbb{R}}^{d \times d}$
2: Input: New symmetric PSD matrix Mt ∈ ℝd × d.
3: Eigendecompose ${{\overline{U}}_{t}{{diag}{\lambda^{(t)}{\overline{U}}_{t}^{\top}}}} = {{\overline{G}}_{t - 1} + M_{t}}$ where λ(t) contains descending eigenvalues.
4: Define Ut as the matrix whose columns are the first ℓ columns of ${\overline{U}}_{t}$, and λ[1: ℓ](t) be its eigenvalues.
5: Update Bt = Utdiag(λ[1: ℓ](t)−λℓ(t))1/2. λℓ(t), BtBt⊤.
Algorithm 1 Frequent Directions Update (FD-update)

The fundamental property of FD is that applying Alg. 1 over a stream of vectors $g_{t}$, with $B_{0} = 0$, the sum of escaped mass $\rho_{t} = \lambda_{\ell}^{(t)}$ can be bounded by the bottom eigenvalues of $G_{T}$, formally given by the following lemma:

### Lemma 1 (Liberty \[16\])

The cumulative escaped mass $\rho_{1:T}$ can be upper bounded as

### Proof

## Related Work

### Spectral Analysis of DL Training

Denote the loss function of the $i$-th example for weights $x$ as $f_{i}{(x)}$. The spectrum of the Hessian matrix $\sum_{i}{\nabla^{2}f_{i}}$ has been the subject of intensive investigation in DL and its properties have been used to devise training methods.

Recent papers inspect the covariance matrix, $\sum_{i}{{({\nabla f_{i}})}{({\nabla f_{i}})}^{\top}}$. In small models, where its computation is feasible, these works identify fast spectral decay.

Agarwal et al. take advantage of this observation by using a low-rank approximation of the whole covariance matrix, based on a limited history of the gradients, $\sum_{i = {t - r}}^{r}{{({\nabla f_{i}})}{({\nabla f_{i}})}^{\top}}$. This approach still requires $r$ copies of the model gradients in memory, where typically $r$ should scale with $\beta_{2}^{- 1}$, with $\beta_{2}$ the exponential moving average for second order statistics (the authors set $r = 200$). Fundamentally, approximating the whole covariance matrix constrains Agarwal et al. application to small models.

In our work, we validate the decay hypothesis holds across the per-layer factored covariance matrices in several modern neural networks. For a layer's gradient matrix $G_{i}$ at the $i$-th example and a second moment decay term $\beta_{2}$, our work inspects spectral decay for $L_{t} = {\sum_{i}{\beta_{2}^{t - i}G_{i}G_{i}^{\top}}}$ and $R_{t} = {\sum_{i}{\beta_{2}^{t - i}G_{i}^{\top}G_{i}}}$; the spectral structure for these outer products is not well-documented. Furthermore, as described in Sec. 3.4, approximating the factored covariance $L_{t} \otimes R_{t}$ requires less memory than the full covariance and explains why our method can scale to large modern architectures whereas Agarwal et al. cannot.

### Sublinear Memory Methods

Extreme Tensoring, AdaFactor, and SM3 are methods that require sublinear memory relative to the number of parameters, at the other end of the memory-quality tradeoff beyond methods that rely on the diagonal of the gradient covariance such as Adam. Owing to different structural assumptions on the set of feasible preconditioners, comparison with these methods is out of scope. However, these methods may compose with our approach. One may apply Extreme Tensoring first, then sketch the resulting reshaped tensor covariances with our method to further reduce memory consumption. Similarly, an SM3-like approach which reduces the indices for each dimension to be preconditioned can be applied before Sketchy is applied to remaining indices.

Crucially, Adam, which uses linear memory for second moment representations, compares favorably in terms of quality to all of these sublinear-memory methods. By increasing rank in factored covariance representation, Sketchy is competitive with Adam, despite sublinear memory for second moment representation. Thus, for simplicity, we compare to only Adam, which dominates the alternative sublinear approaches in terms of quality.

### Sketching-based Approaches

Regret (general convex)

Full Matrix AdaGrad

Ω(T3/4)111The regret of Ada-FD is expressed in terms of dynamic run-time quantities which do not admit a universal bound in terms of GT; we display its regret for the specific case of Observation 2 instead (a detailed look at its regret is given in Appendix B.3).

$\sqrt{\ell\lambda_{\ell:d}T}$

${{tr}{(G_{T}^{1/2})}} + \sqrt{d{({d - \ell})}\lambda_{\ell:d}}$

Table 1: Memory-efficient adaptive gradient methods, in the OCO setting with dimension d (Sec. 2). We describe the worst-case regret bounds without exp-concavity assumptions, asymptotically, hiding logarithmic factors, treating the decision set diameter as a constant, and assume optimally-tuned hyperparameters. ℓ refers to the controllable preconditioner rank. Note ${{tr}G_{T}^{1/2}} = \sqrt{\min_{H \in \mathcal{H}}{\sum_{t}\left. \parallel\nabla_{t}\parallel \right._{H}^{2}}}$ is the optimal preconditioner’s regret among the class of positive semi-definite, unit-trace matrices, ℋ, and GT is the sum of gradient outer products. We let eigenvalues λi = λi(GT) with $\lambda_{i:j} = {\sum_{m = i}^{j}\lambda_{m}}$.

Several works have explored sketching-like approximations to the gradient covariance matrix, but none provide an adaptive bound exploiting fast spectral decay in gradient covariance without additional assumptions (Tbl. 1). In this section, we consider the OCO setting over dimension $d$ (Sec. 2).

Random projection (Ada-LR) is most spiritually similar to our work. Although it does not reduce memory usage, it relies on random projections to lower dimension $\ell \leq d$ to reduce inverse matrix computation costs. An alternative without formal guarantees, RadaGrad, reduces memory consumption to $O{({d\ell})}$; however, as with all Johnson-Lindenstraus projection methods, it suffers a probabilistic failure rate scaling as $O{(\ell^{- 1})}$ (in comparison, our method inherits FD's determinism).

Frequent Directions (FD), provides an alternative matrix sketching approach from the data streaming literature. As an adaptive sketch, it dominates random projection in terms of matrix recovery, and lower bounds show its memory usage is optimal in the sense that any equally-accurate approximation to an adversarially-chosen true covariance $G_{T}$ in operator norm constructed from the corresponding gradients must use $O{({d\ell})}$ bits.

In the context of exp-concave cost functions, Luo et al. provide an FD sketched version of Online Newton Step (ONS), FD-SON. In this setting, their approach nearly recovers classical ONS regret, up to logarithmic error in $\sum_{i = 1}^{\ell - 1}{\lambda_{i}{(G_{T})}}$ and additive error in $\sum_{i = \ell}^{d}{\lambda_{i}{(G_{T})}}$. However, without the exp-concave assumption, FD-SON falls back to a gradient-descent-like default regret of $O\left( {\lambda_{\ell:d}\sqrt{T}} \right)$, which can be $\Omega{(T)}$ without spectral decay. In the context of linear bandits, Chen et al. uses FD for memory reduction. The resulting algorithm, SCFD, is similar to Alg. 2, but SCFD lacks a projection step and does not handle general domains $\mathcal{K}$. We emphasize that our contribution is in the novelty of our regret analysis for general OCO settings, in contrast to linear bandits.

The main prior work exploring FD for general online convex settings, Wan and Zhang, extends the FD-SON approach by adding a fixed diagonal perturbation $\delta I$ to an FD-based preconditioner, in Ada-FD. However, this approach does not achieve $\sqrt{T}$ regret even in a non-adversarial setting with stochastic linear cost functions (Observation 2), where learning rate and $\delta$ are tuned. Dynamically changing diagonal regularization is essential for worst-case $O\left( \sqrt{T} \right)$ performance.

### Observation 2

Suppose we receive linear cost functions ${f_{t}{(x)}} = \left\langle x,g_{t} \right\rangle$, where $g_{t} \in {\mathbb{R}}^{d}$ is a random vector drawn iid from any distribution over $r \leq d$ orthonormal vectors $W$. For any sketch size $\ell \leq r$, the bound on the expected regret of Ada-FD is $\Omega{(T^{3/4})}$.

### Proof

Wan and Zhang remark Ada-FD has $\sqrt{T}$ regret when $G_{T}$ is low rank with rank below $k$, so $d - k$ of its eigenvalues are precisely zero. However, this setting does not require any sketching in the first place. By tracking the column space of observed gradients (e.g., with a reduced QR decomposition, rank-1-updated every step), the full matrix AdaGrad algorithm can be perfectly recovered without using more than $O{({dk})}$ memory.

In concrete convex examples, Sketchy compares favorably to these approaches (Appendix A).

### Shampoo

Figure 1: Asymptotic memory consumption for representing gradient covariance in adaptive regularization approaches for a single matrix parameter of size n × m. Here, r refers to the GGT history buffer size and k to the approximation rank of FD (both typically set to hundreds). Past sketching approaches like Ada-FD and Radagrad take memory similar to GGT, with r being sketch size; these are all asymptotically superlinear. This figure demonstrates optimizer memory usage in the theoretical OCO setting; in practice for deep learning workloads there are additive O(mn) factors for momentum, the parameters themselves, and grafting parameters for Shampoo and Sketchy.

Perhaps our most compelling application is reducing the memory of Shampoo. Shampoo is an adaptive preconditioning method that takes into account the structure of the parameter space, and thus is more efficient than full matrix AdaGrad. For example, if the parameter is a weight matrix $W$ of size $m \times n$, AdaGrad treats the matrix-shaped parameters as a vector of size $mn$, and the preconditioner has size $m^{2}n^{2}$; Shampoo instead has left and right preconditioners $L,R$ of size $n \times n$ and $m \times m$, respectively, with the preconditioned update $L^{- {1/4}}WR^{- {1/4}}$. Write $\overline{\text{vec}}(W)$ as the vectorized weights, then it is equivalent to ${{({L \otimes R})}\overline{\text{vec}}(W)} = {\overline{\text{vec}}\left( {LWR} \right)}$, where $\otimes$ denotes the Kronecker product. Figure 1 illustrates the updates of AdaGrad and Shampoo, where AdaGrad update uses the entire matrix instead of the diagonal, which is shown in the figure. In other words, Shampoo uses a Kronecker-factored preconditioner, and the factorization preserves the matrix structure of the parameters. Since in DL optimization parameters often have matrix structure, Shampoo has strong empirical performance, and has improved upon state-of-the-art results in large-scale tasks such as language modeling with BERT-Large and image classification on ImageNet in.

Figure 1 elaborates why the composition of FD and Shampoo is essential to avoid memory consumption asymptotically greater than parameter count for approximate full matrix regularization.

However, Shampoo memory costs may still be prohibitive for rectangular weight matrices. In BERT-Large, most parameters are in the feed-forward network layers, which consist of $4096 \times 1024$ dense kernels; other transformers follow similar narrow-to-wide patterns. For large models, occupying even $4 \times$ memory for the left preconditioner can frequently result in OOM in memory-constrained settings; this was in fact one of the practical motivations for our proposed approach.

Anil et al. introduces two workarounds for the problem of rectangular matrices based on limiting covariance modelling. Furthermore, both approximations can be applied to our method, so we do not compare against them. First, the authors propose Blocked Shampoo, which views each weight matrix $W$ of shape $m \times n$ as ${mn}/b^{2}$ blocks of size $b \times b$ for some block size $b < {\min{(m,n)}}$ (in the limit $b = 1$, this recovers diagonal AdaGrad). This approach is dependent on the ordering of neurons in hidden layers. Another approximation relies on only one-sided covariance upper bounds, $L_{t} \otimes I$ or $I \otimes R_{t}$. Note, however, that the one-sided approximation doesn't help with vector parameters, such as those that appear for the bias terms in dense layers or layer norms. For 3D weights, such as those which appear in homogeneous Mixtures of Experts, blocking increases memory consumption. These approaches do not take into account the fast decay of the preconditioner's spectrum, which is the focus of our work.

## Algorithms and Main Theorems

In this section, we introduce the adaptation of Frequent Directions (FD) to AdaGrad (Sec. 4.1) and Shampoo (Sec. 4.2), the corresponding algorithms and regret guarantees. Additionally, in Sec. 4.3, we modify FD to support exponential moving averages.

The main technical novelty in incorporating Alg. 1 to AdaGrad (Alg. 2) and Shampoo (Alg. 3) is the construction of preconditioning matrices with FD-sketched matrices compensated by the cumulative escaped masses. The insight of such construction lies in the observation that while the FD sketch lower bounds the full preconditioning matrix, the FD sketch compensated with the cumulative escaped masses upper bounds the full preconditioning matrix, as demonstrated in Lemma 10 for AdaGrad and Lemma 14 for Shampoo. The regret guarantee for AdaGrad () and Shampoo () directly depends on the trace of the preconditioning matrices, therefore obtaining upper and lower bounds on the preconditioning matrices allows explicit additive dependence on the cumulative escaped mass. We expect this approach to be reusable for alternative approximation schemes.

### FD for AdaGrad

Our main algorithm in this section is Alg. 2 run with FD (Alg. 1) as the sketching method. ${\overset{\sim}{G}}_{t}^{- {1/2}}$ in Alg. 2 denotes the Moore-Penrose pseudoinverse of the matrix ${\overset{\sim}{G}}_{t}^{1/2}$. Our main algorithm, Sketchy AdaGrad, in this section exploits the FD approach outlined in Alg. 1 as the sketching method in AdaGrad. In particular, at every time step, we pass the newly received subgradient $g_{t}$ into Alg. 1, which updates and maintains a low-rank sketch ${\overline{G}}_{t}$ of the AdaGrad preconditioning matrix $G_{t}$. We keep track of the cumulative escaped mass $\rho_{1:t}$, which we add back to the low-rank sketch to create the Sketchy preconditioner ${\overset{\sim}{G}}_{t}$, with which we perform the regular AdaGrad descent and projection.

1: Input: constraint set 𝒦, step size η, time horizon T.
2: Initialize x1 ∈ 𝒦, ${\overline{G}}_{0} = {\overset{\sim}{G}}_{0} = 0$.
4: Play xt, receive gt ∈ ∂ft(xt), suffer cost ft(xt).
5: Sketch ${(\rho_{t},{\overline{G}}_{t})} = {\texttt{FD-update}{({\overline{G}}_{t - 1},{g_{t}g_{t}^{\top}})}}$.
6: Update ${\overset{\sim}{G}}_{t} = {{\overline{G}}_{t} + {\rho_{1:t}I}}$, $y_{t + 1} = {x_{t} - {\eta{\overset{\sim}{G}}_{t}^{- {1/2}}g_{t}}}$, and $x_{t + 1} = {\underset{x\in\mathcal{K}}{argmin}{\|{y_{t + 1} - x}\|}_{{\overset{\sim}{G}}_{t}^{1/2}}^{2}}$.
Algorithm 2 Sketchy AdaGrad (S-AdaGrad)

### Theorem 3

Define $\Omega_{\ell} = \min_{k < \ell}{(\ell - k)}^{- 1}\sum_{i = {k + 1}}^{d}\lambda_{i}{(G_{T})}$, then with $\eta = \frac{D}{\sqrt{2}}$, Alg. 2 guarantees the following additive regret bound:

where $D$ is the diameter of the constraint set $\mathcal{K}$ if $\mathcal{K}$ is bounded and $\max_{t \in {\lbrack T\rbrack}}{\|{x_{t} - x^{*}}\|}_{2}$ otherwise.

### Proof

Notably in Thm. 3, $\text{Regret}_{T} = {O\left( \sqrt{T} \right)}$ and the lower eigenvalue dependence $\Omega_{\ell}$ is additive.

### Corollary 4

We can improve Theorem 3 slightly to

### Proof

The regret bound above holds under the optimal tuning of the learning rate, which depends on problem quantities that can be unknown a priori. It is possible to design a parameter-free variant of Alg. 2 by using the norm ${\| x\|}_{t} = {({x^{\top}{({{\overset{\sim}{G}}_{t} + I})}^{1/2}x})}^{1/2}$ in the projection step of Alg. 2, as seen in.

### FD for Shampoo

In this section, we adapt FD-update to Shampoo. For simplicity, we optimize over ${\mathbb{R}}^{m \times n}$ in Alg. 3; projection may be handled as in Alg. 2. Similar to Sketchy AdaGrad, Sketchy Shampoo uses the FD approach outlined in Alg. 1 to sketch the left and right preconditioning matrices for Shampoo. In particular, we maintain two parallel sketching streams using Alg. 1 to produce sketches ${\overline{L}}_{t},{\overline{R}}_{t}$ for the left and right preconditioning matrices. We keep track of the cumulative escaped masses $\rho_{1:t}^{L}$ and $\rho_{1:t}^{R}$ from sketching the left and right preconditioning matrices, respectively, and compensate the cumulative escaped mass to create the left and right Sketchy preconditioning matrices ${\overset{\sim}{L}}_{t},{\overset{\sim}{R}}_{t}$.

1: Input: step size η, time horizon T.
2: Initialize X0 = 0m × n, ${\overset{\sim}{L}}_{0} = {\varepsilon I_{m}}$, ${\overset{\sim}{R}}_{0} = {\varepsilon I_{n}}$, ${\overline{L}}_{0} = 0_{m}$, ${\overline{R}}_{0} = 0_{n}$.
4: Play Xt, suffer ft(Xt), receive Gt ∈ ∂ft(Xt).
5: Sketch ${(\rho_{t}^{L},{\overline{L}}_{t})} = {\texttt{FD-update}{({\overline{L}}_{t - 1},{G_{t}G_{t}^{\top}})}}$, ${(\rho_{t}^{R},{\overline{R}}_{t})} = {\texttt{FD-update}{({\overline{R}}_{t - 1},{G_{t}^{\top}G_{t}})}}$.
6: Update ${\overset{\sim}{L}}_{t} = {{\overline{L}}_{t} + {\rho_{1:t}^{L}I_{m}}}$, ${\overset{\sim}{R}}_{t} = {{\overline{R}}_{t} + {\rho_{1:t}^{R}I_{n}}}$ and $X_{t + 1} = {X_{t} - {\eta{\overset{\sim}{L}}_{t}^{- {1/4}}G_{t}{\overset{\sim}{R}}_{t}^{- {1/4}}}}$.
Algorithm 3 Sketchy Shampoo (S-Shampoo)

Denote $L_{T}\overset{\text{def}}{=}{{\sum_{t = 1}^{T}{G_{t}G_{t}^{\top}}} + {\varepsilon I}}$ and $R_{T}\overset{\text{def}}{=}{{\sum_{t = 1}^{T}{G_{t}^{\top}G_{t}}} + {\varepsilon I}}$.

### Theorem 5

Suppose $G_{1},{\ldots G_{T}}$ have rank at most $r$. Then Alg. 3 run with $\eta = {D/\sqrt{2r}}$ guarantees the following regret bound:

where $D = {\max_{t \in {\lbrack T\rbrack}}{\|{X_{t} - X^{*}}\|}_{F}}$ and $\Omega_{L,\ell},\Omega_{R,\ell}$ are analogous bounds for $\rho_{1:T}^{L},\rho_{1:T}^{R}$ from Lem. 1. ‣ Sketching and the Frequent Directions Method. ‣ 2 Setting and Definitions ‣ Sketchy: Memory-efficient Adaptive Regularization with Frequent Directions").

### Proof

Bounds may be improved analogous to Cor. 4 for Alg. 3, but we omit the similar statement due to space.

### Exponentially Weighted FD

This section discusses the modification of Alg. 1 to support exponential moving averages. Early in algorithm development, we noticed that attempting to approximate the unweighted sum of factored gradient covariances $\sum_{t}{G_{t}G_{t}^{\top}}$ and $\sum_{t}{G_{t}^{\top}G_{t}}$ with FD tended to an estimate of covariance that was roughly $0$, creating numerical instabilities. Note that FD guarantee (Lem. 1. ‣ Sketching and the Frequent Directions Method. ‣ 2 Setting and Definitions ‣ Sketchy: Memory-efficient Adaptive Regularization with Frequent Directions")) still holds---but the error term $\rho_{1:T}$ becomes greater than $\left. \parallel G_{T}\parallel \right.$, resulting in a vacuous bound due to lack of spectral decay.

Indeed, Fig. 3 motivating this work only confirmed that the exponential moving average ${L_{t}{(\beta_{2})}} = {\sum_{t}{\beta_{2}^{T - t}G_{t}G_{t}^{\top}}}$ exhibits fast spectral decay (and analogously for $R_{t}$). Luckily, thanks to the recursion ${L_{t + 1}{(\beta_{2})}} = {{\beta_{2}L_{t}} + {G_{t + 1}G_{t + 1}^{\top}}}$, the FD sketch may easily be adopted for this setting.

### Observation 6

Given a stream $g_{t}$ of vectors for $t \in {\lbrack T\rbrack}$, sketch size $\ell$, updates ${(\rho_{t}^{(\beta_{2})},{\overline{G}}_{t}^{(\beta_{2})})} = {\texttt{FD-update}{({\beta_{2}{\overline{G}}_{t - 1}^{(\beta_{2})}},{g_{t}g_{t}^{\top}})}}$, and $G_{T}^{(\beta_{2})} = {\sum_{t = 1}^{T}{\beta_{2}^{T - t}g_{t}g_{t}^{\top}}}$, we have

## Experiments

We investigate how much of Shampoo's quality our low-memory approach can recover (Sec. 5.1) and whether the factored covariance exhibits spectral decay amenable to sketching (Sec. 5.2). We relegate convex examples to Appendix A due to space constraints, which check that Sketchy compares favorably to related work in a setting directly related to the theory.

### Deep Neural Networks

We evaluate the effectiveness of S-Shampoo as a practical second-order algorithm for training networks, including

ResNet-50 for ImageNet image classification task of ImageNet with random cropping and flipping augmentations.

A 16-layer Conformer model for the audio transcription task, Librispeech.

A GNN with 5 message-passing steps on ogbg-molpcba, which classifies structural properties of graphically encoded molecule inputs.

Our FD variant of Shampoo introduces only one new hyperparameter, the rank $\ell$, which we do not tune, but set to $\ell = 256$, which translates to $4 \times$ memory savings for Shampoo blocks of size $1024$ for the accumulators. Shampoo, Adam, and the underlying architectures introduce their own hyperparameters. S-Shampoo inherits those of Shampoo. We tune only common parameters between the three optimizers with the same budgets, selecting based on validation set accuracy. In the ImageNet case, we evaluate final test set performance using ImageNet v2, as the ImageNet test set is unavailable. Additinoal training information is available in Appendix C.

Figure 2: Test metrics are classification error rate for top-1 accuracy for ImageNet v2, word error rate for Librispeech, and one minus average precision for OGBG-MolPCBA. We plot the mean of 5 random seeds, with 1.96 times the standard error as error bars. For readers familiar with ImageNet v1, final validation accuracy for Shampoo was 77.69% (0.03%), S-Shampoo having 77.18% (0.04%), and Adam having 76.76% (0.03%), but we emphasize that due to tuning, the test set performance pictured above should be of primary concern.

As Fig. 2 demonstrates, the second-order information leveraged by Shampoo results in improvements over Adam, a first-order method. Our method performs at least as well as Adam in all cases, despite using asympotically less memory to represent covariance (as Fig. 1 shows, Adam uses $O{({mn})}$ for a rectangular weight matrix's diagonal accumulators, whereas S-Shampoo uses $O{({{mk} + {nk}})}$). In the GNN case (OBGB-MolPCBA), Shampoo does not perform as well; its training curves indicate overfitting, but we note that S-Shampoo was less susceptible to overfit like Adam.

### Spectral Analysis

To explain Sketchy's strong performance in Sec. 5.1, we inspect the exponential moving average of Kronecker-factored gradient covariance for fast spectral decay. We find that this is indeed the case in practice, so Sketchy's low-rank plus diagonal covariance is representative of true training statistics.

For all our architectures, we tune Shampoo and extract the intermediate gradient covariances over the course of training. To make our curves comparable across architectures, we fix the parameter for the second moment, $\beta_{2} = 0.999$ for these runs. Furthermore, ResNet-50 has a few parameters with dimension 2048, but the largest dimension for any parameter from the other two architectures is 1024, so we use the Blocked Shampoo variant discussed in Sec. 3.4 with block size 1024. In other words, weights containing a dimension 2048 are split into two. We tune other Shampoo parameters for each architecture, and plot statistics of Kronecker factors $L_{t} = {\sum_{i}{\beta_{2}^{t - i}G_{t}G_{t}^{\top}}}$ and $R_{t} = {\sum_{i}{\beta_{2}^{t - i}G_{t}^{\top}G_{t}}}$.

Figure 3: Two measures of spectral decay. As described in Sec. 5.2, we demonstrate spectral decay of Lt and Rt covariance factors of shape 1024 × 1024. On the left, we take the factors C from the first layer of each network and plot the proportion of spectral mass captured by its top 256 eigenvalues throughout training, i.e., $\sum_{i = 1}^{256}{{\lambda_{i}{(C)}}/{\sum_{i = 1}^{1024}{\lambda_{i}{(C)}}}}$. On the right, we plot a continuous measure of eigenvalue concentration, the intrinsic dimension trC/λmax(C), typically 10× smaller than nominal dimension. We plot the average across all covariances for each network’s weight’s dimensions, with the shaded regions capturing the interquartile range.

In Fig. 3, we plot the intrinsic dimension of Kronecker covariance factors over training for our three settings. The intrinsic dimension determines the rate at which empirical covariance estimates concentrate to their expectation, rather than a random vector's actual dimension, up to logarithmic factors (Vershynin, Remark 5.6.3). Despite actual dimensionality being over 1024, intrinsic dimension across all architectures stays below 105. A conspicuous phase shift 10% of the way through training may be the result of a change from linear learning rate warmup to a learning rate decay, starting at roughly 5% of the way into training.

Given $\beta_{2} = 0.999$, we emphasize that the behavior in Fig. 3 is an emergent property of DL training. Though surely a lower $\beta_{2}$ would naturally result in lower intrinsic dimension (which can still be taken advantage of by Alg. 2 and 3), we would still expect higher intrinsic dimension if covariances were near-isometries. If we observe some large number $n = 10000$ draws $x_{i}$ of $1024 \times d$ matrices with iid $N{}$ entries, then numerical experiments show that the average intrinsic dimension of $\sum_{i = 0}^{n - 1}{\beta_{2}^{i}x_{i}x_{i}^{\top}}$ is $324.63$ ($0.52$) and $862.13$ ($0.25$) for $d = {1,64}$, respectively, with parenthesized numbers denoting standard error across 20 trials. Values generated this way are larger than the average intrinsic dimension of roughly 10, 30, 50 observed in Fig. 3.

## Discussion

Up to spectral error, Alg. 2 achieves full-matrix AdaGrad regret despite approximating the *smallest* part of the spectrum of $G_{t}^{- {1/2}}$ at each step. Remarkably, these eigenvectors correspond to the *most* easily discernible signals of the covariance for the stream $g_{t}$. This apparent (and fortuitous) coincidence is resolved by considering the covariance of ${\overset{\sim}{G}}_{t}^{- {1/2}}g_{t}$: whitening the gradient to facilitate optimization best reflects on regret; as a result, approximating top eigenvectors of $G_{T}$ helps more than the bottom ones.

Our initial implementation focused on correctness rather than physical speed or memory reduction. Engineering optimizers competitive with existing industrial-strength implementations of Adam and Shampoo was out of scope. In implementing FD, we performed updates via the factored SVD of $\lbrack{\beta_{2}^{1/2}B_{t}};G_{t}\rbrack$ rather than the eigendecomposition depicted in Alg. 1; this avoids squaring, which is unavoidable in Shampoo. For speed, Shampoo subsamples gradients for its covariance estimation and updates its inverse matrix roots intermittently, every fixed number of steps. A tuning script provided by Anil et al. included gradients from every step, but updated roots every 10 steps. Since FD does not separate sampling from its computation of estimated covariance eigendecomposition, we took the more difficult setting for S-Shampoo, only allowing it to simultaneously observe every 10^th^ gradient and update its covariance inverse roots (see Appendix G for a theoretical justification).

Though step-skipping makes Shampoo and S-Shampoo tractable, future work may explore further speedups: since FD only requires the top $\ell$ eigenvalues, iterative Lanczos-like routines which are accelerator-friendly, such as LOBPCG, may allow incremental updates to ${\overset{\sim}{G}}_{t}^{- {1/2}}$ in factored form with only a few matrix multiplies, S-Shampoo may be able to update more frequently than its non-sketched counterpart, further improving quality.

## Conclusion

In this work, we address a gap in the OCO literature for low-memory optimization with the novel Alg. 2 and demonstrate its relevance to practical non-convex problems such as neural net training (Sec. 5.1) by leveraging a new observation about gradient covariance (Sec. 5.2).

The growing disparity between compute capability and memory bandwidth underscores the need for further research in this direction. Further, large-batch settings reduce the performance gap between first and Shampoo-based second order methods, since the batch-size independent runtime of the optimizer is amortized per example used for the gradient calculation. Even in performing experiments for this work, we would frequently find that faster accelerators were unavailable, but many previous-generation ones were, encouraging us to leverage data-parallel training. For datasets such as Imagenet, we notice the advantage of second order methods in dealing with large batches even at relatively modest sizes, such as 1024; many works on explore several larger multiples of this.

Potential for future work includes numerical methods outlined in the previous section as well optimizing the rank $\ell$ across the many tensors in a network, as the spread in Fig. 3 highlights the large variance in covariance intrinsic dimension. Furthermore, the inductive biases conferred by the minima which different-rank representations of curvature reach may have problem-dependent generalization implications, a question which we leave for future work. For a comparison of full rank preconditioning's effect versus first-order minima, see Amari et al..
