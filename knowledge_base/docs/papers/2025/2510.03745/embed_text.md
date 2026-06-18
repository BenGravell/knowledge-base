## Introduction

Approximating integrals using a finite set of sample points is a central task in scientific computation, with applications ranging from numerical integration to uncertainty quantification and Bayesian inference to computer vision and machine learning tasks; (pmlr-v80-chen18f; paulin2022; Keller2013a mishra21; longo21). Problems that arise in these areas often involve computing expectations of the form ${\mathbb{E}}_{\rho}{(f)}$ of a function $f{({\mathbf{x}})}$ in ${\mathbb{R}}^{d}$ with respect to some probability distribution $F$ with density function $\rho{({\mathbf{x}})}$.

The simple Monte Carlo (MC) method estimates expectations of this kind by drawing samples ${\{\mathbf{X}_{i}\}}_{i = 1}^{N}$ randomly IID from $F$ and computing the sample mean, i.e.,

In this work, we will assume that there exists a transformation to map our integration problem to the $d$-dimensional unit hypercube and thus will assume hereafter that $F$ is the uniform distribution on ${\lbrack 0,1\rbrack}^{d}$. Under the assumption that some notion of variance of the integrand $f{({\mathbf{x}})}$ is finite (e.g., in the sense of Hardy-Krause; (owen2005_hardykrause)), the standard MC convergence rate of $\mathcal{O}{(N^{- {1/2}})}$ applies, which may necessitate very large $N$ when a high degree of accuracy is required. A popular variation on the MC method is to replace the random samples with a deterministic node set that more evenly covers the domain. Such *low-discrepancy* (LD) points form the foundation of quasi-Monte Carlo (QMC) methods; (; HICKKIRKSOR2025), which achieve error rates close to $\mathcal{O}{(N^{- 1})}$ in favorable cases.

Assuming the integrand belongs to a reproducing kernel Hilbert space (RKHS) $\mathcal{H}$ of functions ${\mathbb{R}}^{d}\rightarrow{\mathbb{R}}$ equipped with an inner product ${\langle \cdot, \cdot \rangle}_{\mathcal{H}}$ and corresponding norm $\parallel \cdot \parallel_{\mathcal{H}}$, one can use the Cauchy-Schwarz inequality within $\mathcal{H}$ to derive an error bound on the approximation as

In the above, $D_{2}^{k}{({\{\mathbf{X}_{i}\}}_{i = 1}^{N})}$ is referred to as the kernel discrepancy, or simply, the discrepancy for brevity, and the term ${\| f\|}_{\mathcal{H}}$ is a measure of variation of the integrand; see for further details. The discrepancy term measures how closely the empirical distribution of the discrete sample point set approximates the uniform distribution on ${\lbrack 0,1\rbrack}^{d}$. Denote by $k:{{{\mathbb{R}}^{d} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}}$ the reproducing kernel associated with the RKHS $\mathcal{H}$. The (squared) discrepancy can be computed explicitly as

Thus, employing sampling locations ${\{\mathbf{X}_{i}\}}_{i = 1}^{N}$ with small discrepancy, in principle, leads to a more accurate and tighter approximation of the expectation of interest. It then follows that constructing sampling nodes with minimal discrepancy is of broad importance, with applications across many areas of computational science.

### Sets versus Sequences

In the study of QMC methods, it is important to distinguish between LD sets and sequences. Theoretical results on sequences in dimension $d$ often correspond to those on sets in dimension $d + 1$; (; kirk2020). Thus, despite being closely linked, sets and sequences are designed to address different problems.

LD sets are finite collections of nodes that achieve good uniformity over the $d -$dimensional unit hypercube. For such sets, one can typically establish a discrepancy bound of ${C{({\log N})}^{d - 1}}/N$ for some absolute constant $C$ depending on the specific construction. These are particularly well suited to applications where the number of samples is known in advance, and this fixed-$N$ setting is exactly the problem addressed by the recently successful Message-Passing Monte Carlo (MPMC) framework; (ruschkirk24). Classical examples of LD sets include Hammersley point sets; (Hammersley1960), rank-1 lattices and digital nets;. In contrast, LD sequences are infinite constructions that are extensible in the number of points, with the property that every initial segment, referred to in this text as a *prefix*, of length $N$ achieves discrepancy of order $\mathcal{O}{({{({\log N})}^{d}/N})}$. Classical examples are the van der Corput sequence in one-dimension, Sobol' and Halton sequences for any dimension; (; Sobol1967) and their numerous variants, as well as more modern greedy-optimized extensible constructions; (Kritzinger2022). As an important remark, the standard LD sequence constructions typically yield much smaller discrepancy values at special values of $N$, such as a powers of $2$, which introduces an inherent limitation in practice as performance can fluctuate depending on the chosen sample size. For example, in the first $2^{14}$ van der Corput points, there is never a better discrepancy for $N$ points than for $2^{m}$ points when $2^{m} < N < 2^{m + 1}$; (practicalqmc, Figure 15.4).

An inherent trade-off arises: the discrepancy can often be minimized more effectively for a LD set since the sampling nodes are optimized globally for a particular, pre-specified $N$; (ruschkirk24). However, extending such optimized sets to larger sizes is challenging, as adding new nodes typically disrupts the carefully balanced uniformity. Sequences, on the other hand, provide greater flexibility in practice, since they allow sample sizes to be increased adaptively without restarting the construction, albeit often at the cost of a slightly higher discrepancy for any given $N$. This trade-off is illustrated in Fig. 1, which compares the discrepancy in $d = 4$ of MPMC (trained to minimize the discrepancy at $N = 1024$) with that of classical low-discrepancy sequences as the number of points increases. We observe that MPMC achieves the lowest discrepancy at $N = 1024$, clearly outperforming all other methods at this target length. However, for most $N^{\prime} < N$, it does not surpass standard low-discrepancy sequences. This is expected, since MPMC was optimized only for the full point set of $1024$ points. This highlights the need for a sequential generation mechanism for low-discrepancy sampling points.

Figure 1: D2star discrepancy for increasing number of sampling points in d = 4 for MPMC, Sobol’, Halton, NeuroLDS, and Scrambled Sobol’ (mean over 32 scrambled sequences).

### Related Work

There exists a growing literature on the optimization of sampling node locations. Some works aim to minimize the discrepancy directly; (cle25; support_points2018; pmlr-v80-chen18f; kernel_thinning2024), while others use alterative methods and figures-of-merit; (miller2025expecteddiverseutilityedu; mak2025_robust_designs; BdryGP_mak_2025).

The Message-Passing Monte Carlo (MPMC) method; (ruschkirk24) is one such general QMC construction method, and unlike classical construction methods such as digital nets or rank-1 lattices, which are derived through number-theoretic means, MPMC is the first work to formulate the problem as one of learning a uniform design through state-of-the-art geometric deep learning tools. The core of the method is a graph neural network based on a message-passing algorithm where each node of the graph corresponds to a sample point and the edges (formed via nearest neighbor) encode the geometric relations between the points. The optimization is initialized by IID random points contained in ${\lbrack 0,1\rbrack}^{d}$ and proceeds by updating the message-passing neural network parameters according to an $L_{2}$-based discrepancy function--the classical $L_{2}$-star discrepancy is used in the original formulation--which serves as a differentiable objective function. A resulting transformation is learned which maps the original IID random points into a uniform output set which has very small discrepancy. MPMC has its main strengths in the very effective minimization of discrepancy values for an $N$-element point set--some of the smallest discrepancy values ever obtained--and its flexibility of design via the exchangeability of differentiable loss function including extensions to minimize Stein discrepancies;.

Importantly, the limitations of MPMC are also clear: the optimization process must be repeated for each fixed choice of $N$ since the construction is not extensible to larger point sets. Furthermore, the computational cost grows quickly with the number of sampling points and thus training more than a few thousand points becomes very computationally expensive. These limitations highlight the need for a model which allows for sequential and extensible generation of LD sequences of points.

### Our Contribution

In this paper, following in the footsteps of several recent works employing machine learning architectures in LD optimization pipelines, we develop NeuroLDS, a flexible finite LDS generator. We further demonstrate that NeuroLDS outperforms classical LD sequences in terms of discrepancy minimization, QMC integration, robot motion planning, and scientific machine learning applications.

## Methods

Figure 2: Schematic of the proposed NeuroLDS model. First, each index i ∈ {1, …, N} is mapped to a sinusoidal feature vector ψi ∈ ℝ1 + 2 K. Second, the encoded features are passed through an L-layer multilayer perceptron (MLP), which outputs Xi ∈ d. Finally, the collection {X1, …, XN} forms a (learned) low-discrepancy sequence within the unit hypercube.

NeuroLDS is a deterministic sequence generator $f_{\theta}:{{\{ 1,\ldots,N\}}\rightarrow{\lbrack 0,1\rbrack}^{d}}$ that preserves the index-driven construction central to QMC. Classical LD sequences (e.g., Halton and Sobol') are constructed via number-theoretic digit transforms of the index; see Section 2.1 for details. Instead, NeuroLDS feeds the index $i$ through a $K$-band sinusoidal positional encoding and an $L$-layer multi-linear perceptron (MLP) with ReLU and final sigmoid activation functions to obtain $\mathbf{X}_{i} \in {\lbrack 0,1\rbrack}^{d}$. We first carry out a pre-training procedure by approximating a traditional LD sequence (i.e., Sobol') using the mean squared error (MSE), then fine-tune by minimizing closed-form $L_{2}$-based discrepancy losses over all sequence prefixes; see and Appendix A for exact expressions of the discrepancy loss functions.

### Index-Based Sequence Construction

Classical QMC sequences such as Halton and Sobol' rely on the *index* $i \in {\mathbb{N}}_{0}$ as the fundamental input. For Halton, the $j$-th coordinate is obtained from the *radical--inverse* function in base $b_{j}$ with $b_{1},\ldots,b_{d}$ typically chosen as the first $d$ primes;. Writing $i = {\sum_{k = 0}^{\infty}{a_{k}b_{j}^{k}}}$ with digits $a_{k} \in {\{ 0,\ldots,{b_{j} - 1}\}}$, the $j$-th coordinate of the $i$-th point of the Halton sequence is

i.e., take the digits of $i$ in base $b_{j}$ and place them after the decimal point. The Halton sequence is therefore $\{{({\phi_{b_{1}}{(i)}},\ldots,{\phi_{b_{d}}{(i)}})}:{i \geq 0}\}$. This yields good equidistribution in low $d$, but number-theoretic correlations emerge as $d$ grows.

Sobol' sequences, in contrast, are digital $(t,d)$-sequences in base $2$ constructed from primitive polynomials over the *finite field* ${\mathbb{F}}_{2}:={\{ 0,1\}}$ (arithmetic mod $2$; addition is bitwise XOR); (Sobol1967; ). Each dimension $j$ uses a polynomial ${p_{j}{(z)}} = {z^{m_{j}} + {a_{1}z^{m_{j} - 1}} + \cdots + a_{m_{j}}}$ with coefficients $a_{i} \in {\{ 0,1\}}$ to generate binary *direction numbers* $v_{j,k} \in {}$ (interpreted as binary fractions). For $k > m_{j}$, they satisfy

where $\oplus$ denotes bitwise XOR and $\gg m_{j}$ denotes a bitwise right shift by $m_{j}$ places. Let ${g{(i)}} = {i \oplus {({i \gg 1})}}$ be the Gray code of $i$, and let $g_{k}{(i)}$ be its $k$-th bit. Then

interpreted as a binary fraction in $\lbrack 0,1)$ by reading the resulting bitstring after the binary point. This digital construction yields very small discrepancy even in moderate $d$.

Inspired by these number-theoretic constructions, we also root our approach in the index, but instead of fixed digit expansions or direction numbers, we expose multiple frequency scales of $i$ via sinusoidal features. These features play an analogous role to the radical--inverse digits of Halton or the Gray-coded direction numbers of Sobol', while allowing the downstream MLP to *learn* flexible digital rules according to a discrepancy objective function generating points in ${\lbrack 0,1\rbrack}^{d}$ that achieve very high uniformity. Each index $i$ is mapped to a sinusoidal encoding,

analogous to Fourier features in positional encoding. This embedding exposes multiple frequency scales of the index to the network, mirroring the role of base-$b$ digit expansions in Halton or Sobol'.

The encoded index is passed through an $L$-layer feedforward network with ReLU activations and a final sigmoid, yielding ${\mathbf{X}_{i} = {f_{\theta}{(\psi_{i})}} \in {\lbrack 0,1\rbrack}^{d}}.$ The collection ${\{\mathbf{X}_{i}\}}_{i = 1}^{N}$ defines a deterministic, learned sequence.

### Two-Stage Optimization

Training proceeds in two complementary phases, and an overview of the overall architecture is shown in Figure 2.

### Pre-training (MSE alignment)

We initialize $f_{\theta}$ by regressing onto a chosen reference QMC sequence, with natural starting points being the Sobol' or Halton sequences. Given these targets ${\{ q_{i}\}}_{i = 1}^{N}$, we minimize

In practice, the reference sequence is generated with an appropriate burn-in period, as is sometimes recommended in the literature;. This pre-training phase stabilizes the learning process and proves essential for the success of our method (see Section 3.3).

### Fine-tuning (discrepancy minimization)

After pre-training, we further refine $f_{\theta}$ by minimizing differentiable $L_{2}$-based discrepancy losses, evaluated over all sequence prefixes. These losses are induced by symmetric positive-definite kernels $k$, and we adopt product-form kernels that yield classical discrepancy measures. For example, choosing ${k{({\mathbf{x}},{\mathbf{y}})}} = {\prod_{j = 1}^{d}\left( {1 - {\max{(x_{j},y_{j})}}} \right)}$ for ${{\mathbf{x}},{\mathbf{y}}} \in {\lbrack 0,1\rbrack}^{d}$ recovers the standard $L_{2}$ star discrepancy;. Other well-studied choices include symmetric, centered, and periodic variants, all of which admit exact and differentiable forms. Each discrepancy can be computed in $\mathcal{O}{({dN^{2}})}$ time across all prefixes of a sequence of length $N$. We refer to for a comprehensive overview of $L_{2}$ discrepancies, and to Appendix A for explicit kernel definitions, which serve as tunable hyperparameters in NeuroLDS.

In higher dimensions, the efficacy of QMC methods often relies on there being some underlying low-dimensional structure, or decaying importance of variables; (; wangsloan05). After the emergence of a rigorous framework from weighted function spaces, many works now exist in this setting; ( SLOAN2001697; GNEWUCH201429; chen2025highdimensionalquasimontecarlocombinatorial). Precisely, one assigns a product weight vector ${\mathbf{γ}} = {(\gamma_{1},\ldots,\gamma_{d})} \in {\mathbb{R}}_{+}^{d}$ often depending on some a-priori knowledge of the problem allowing one to quantify the relative importance of variables. This introduces a tailored training ability of NeuroLDS to be applied to anisotropic integrands, as demonstrated in our Borehole case study in Section 3.2.1.

Our overall fine-tuning loss averages prefix discrepancies:

where $w_{P}$ are a choice of weights and $\bullet \in {\{\text{star},\text{sym},\text{ctr},\text{per},\text{ext},\text{asd}\}}$ denotes the choice of kernel function.

In this work, all results are produced with uniform weights such that all prefix lengths $P \leq N$ contribute equally to the loss. Alternative weighting schemes and their potential effects are discussed in Section 3.3.

## Results

Code to replicate the experiments can be found at

### Discrepancy Minimization

We evaluate the discrepancy of NeuroLDS in dimension $d = 4$ for three different choices of $L_{2}$-discrepancy losses: the symmetric $D_{2}^{\text{sym}}$, the star $D_{2}^{\text{star}}$, and the centered $D_{2}^{\text{ctr}}$. For each loss, our NeuroLDS sequence is obtained by pretraining on Sobol' prefixes and then fine-tuning on the target discrepancy. To ensure comparable conditions, we apply a burn-in of $128$ points across the board: (i) during pretraining we regress to Sobol' with the first $128$ points discarded (i.e., indices are shifted by $128$), and (ii) Sobol' and Halton baselines are likewise evaluated after discarding their first $128$ points. Hyperparameters for NeuroLDS are selected *per loss* using Optuna the best configurations are summarized in the Appendix in Table 5.

Besides the classical Sobol' and Halton baselines, we also compare against randomized Sobol' via Owen's nested uniform scrambling; (Owen, 1995-nets and (t,s)-sequences"), 1997). This yields sequences that retain low-discrepancy guarantees in expectation, while breaking any uniformity flaws. In our experiments, we report the mean over $32$ independent scramblings.

Table 6 in the Appendix reports the exact discrepancy values for several values of $N$. NeuroLDS achieves the lowest discrepancy at every sequence length for all three losses. Scrambling reduces some oscillations in Sobol', but even its randomized variants remain above NeuroLDS for all reported $N$. The full sequence discrepancy profiles are shown in Fig. 3. For completeness, the Appendix also reports the corresponding $D_{2}^{\text{sym}}$ discrepancy curves in dimensions $1$--$3$ (see Fig. 10), which serve as a lower-dimensional reference and show that improvements are modest in 1D but become progressively clearer as dimension increases.

For visual aid, Fig. 6 in the Appendix shows the first $N \in {\{ 64,128,256\}}$ points of Sobol' and NeuroLDS in two dimensions. For this illustrative experiment, NeuroLDS was trained with the $D_{2}^{\text{sym}}$, and all hyperparameters were tuned via Optuna. Although Sobol' achieves good global coverage, it often exhibits structured alignments and mild clustering artifacts, particularly at small $N$. By contrast, NeuroLDS points appear more irregular, or random, while still covering the domain evenly.

Figure 3: Comparison plots of different discrepancy metrics for 4d point sequences up to a length of 10000 as a function of sequence length: D2sym (left), D2star (middle), and D2ctr (right). Each panel compares Sobol’, Halton, NeuroLDS, and Scrambled Sobol’ (mean over 32 scrambled sequences).

### Applications

### Quasi-Monte Carlo Integration

LDS are most often employed in QMC integration to approximate a $d$-dimensional integral over ${\lbrack 0,1\rbrack}^{d}$, with the goal of achieving faster convergence than standard Monte Carlo. To illustrate the effectiveness of NeuroLDS in this setting, we consider the 8-dimensional Borehole function, a benchmark in uncertainty quantification, sensitivity analysis, and approximation algorithms (; MORRISBOREHOLE1993; KERSAUDY2015). The function models the flow rate of water through a borehole connecting two aquifers separated by an impermeable rock layer. Our objective is to approximate the expected flow rate, i.e., the integral of the Borehole function over the 8-dimensional parameter space; see Appendix B for details.

Since no analytical solution is available, we pre-compute a high-fidelity reference value using plain Monte Carlo with $N = 2^{21}$ samples. Against this benchmark, we compare several low-discrepancy constructions: classical Sobol' and Halton sequences, our proposed NeuroLDS, and a greedy baseline obtained via Nelder--Mead optimization (NM_optimization1965); see pmlr-v80-chen18f for implementation details. Both NeuroLDS and the NM-Greedy construction are optimized against the weighted symmetric $L_{2}$ discrepancy (see Appendix A), using a computed weight vector $\mathbf{γ}$ that down-weights irrelevant coordinates identified by sensitivity analysis and penalizes irregularity more evenly across dimensions; details are again given in Appendix B. A visualization of the weighted star--discrepancy behavior for all methods is provided in Appendix 11.

The experimental protocol is deterministic: for each sequence type we generate a single fixed instance of the first $N$ points, without randomization or scrambling, and compute the absolute error of the sample mean estimator of the Borehole integral. Table 1 reports these errors across a range of $N$, with the smallest error in each row highlighted in bold.

We find that NeuroLDS, trained with coordinate-weighted discrepancy losses to emphasize the most influential variables, consistently delivers superior accuracy compared with the other sequences across nearly all values of $N$. By contrast, Halton performs the worst overall, as expected given its well-documented uniformity pathologies in moderate to high dimensions (kirklem24). Although the NM-Greedy construction also incorporates sensitivity-informed weights, its performance lags behind NeuroLDS. Notably, NeuroLDS achieves either the smallest or second-smallest error for all but two tested values of $N$.

Table 1: Absolute errors for the Borehole integral approximation with increasing sequence length (N) for NeuroLDS, Sobol’, Halton and a greedy construction. Bold marks the best error per row, underlined the second best.

### Robot Motion Planning

Optimal exploration of the configuration space is a crucial component of sampling based motion planning. Indeed, if the sampled points leave large gaps or cluster unevenly, the planner may fail to discover important paths between regions, particularly when narrow passages are present. For a specific family of planners-Probabilistic Roadmaps (PRM)-there exist theoretical guarantees that directly connect the quality of sampling to path optimality. More recently, the guarantee has been expressed in terms of discrepancy, and significant empirical performance gains obtained with MPMC *point sets* on a suite of PRM benchmarks.

However, most sampling-based planners construct their search structures *sequentially*. For example, the Rapidly-exploring Random Tree (RRT) grows strictly one node at a time, with each new sample extending the current frontier of exploration (Algorithm provided in Appendix C). In this setting, order matters significantly: an early bias toward one region may starve others, leading to poor coverage of narrow passages. The sequential sampling structure must align with the incremental expansion of RRT, with both spatial distribution and temporal ordering central to performance.

We compare the sampling quality of NeuroLDS against uniform sampling, as well as Halton and Sobol' sequences, on a challenging motion planning experiment: Kinematic Chain in a Semi-Circular Tunnel. The task is to control a chain of 4 revolute joints in the plane from an initial configuration inside a semi-circular tunnel to an exterior target pose. The challenge lies in threading the articulated links through the curved tunnel, requiring coordinated rotations across all joints. We randomize the placement of the tunnel between runs, with 160 repetitions per sequence. The success rates for the experiment under different difficulty levels are summarized in Table 2. Across all passage widths, NeuroLDS consistently delivers the highest success, demonstrating its ability to guide the planner through narrow passages. Moreover, when we fix the average success rate (aggregated over all passage widths) achieved by NeuroLDS, we find that Sobol' requires $2.50$ times as many sampling points, Halton requires $1.55$ times as many, and Uniform sampling requires $2.27$ times as many to reach the same average performance. The structured, adaptive sampling of NeuroLDS produces well-distributed points that efficiently cover the configuration space, ensuring robust path discoveries. Overall, these results highlight the advantage of neural-adapted sampling in motion planning tasks, where sequential exploration and effective coverage are critical.

Table 2: RRT success rates (in %) for NeuroLDS, Sobol, Halton, and Uniform sampling. Each distribution uses 10 precomputed sequences of length N = 105, reused across random initializations and difficulty levels. Bold marks the best per row, underline the second best.

### Scientific Machine Learning

LDS have been shown to improve the generalization of deep neural networks trained to approximate parameter-to-observable mappings arising from parametric partial differential equations (PDEs) (mishra21; longo21). In this section, we empirically test whether NeuroLDS improves the performance of deep neural networks over random points and competing LDS constructions in this context. To this end, we consider a multidimensional Black-Scholes PDE that models the pricing of a European multi-asset basket call option, where the assets in the basket are assumed to change in time according to a multivariate geometric brownian motion. The details of the PDE is given in Appendix D. In our experimental setup, we train neural networks to predict the 'fair price', i.e., solution of the Black-Scholes PDE at time $t = 0$, for different initial values of the underlying asset prices drawn from ${\lbrack 0,1\rbrack}^{2}$. We compare the performance of NeuroLDS against uniform random points as well as Sobol' sequences and NMGreedy. We fix the length of the sequence to $1000$. To ensure meaningful results, we present the average of $20$ training runs of the same network using different random weight initializations. Moreover, we conduct a light random search to optimize the learning rate, width, and number of layers of the trained MLP for each of the three sampling methods. The results can be seen in Table 3. While Sobol' sequences outperform uniform random points and NM Greedy falls short, our NeuroLDS achieve superior performance over the baselines. Moreover, NeuroLDS achieves lower error than the baselines for any choice of the $L_{2}$-discrepancy. We conclude that NeuroLDS can successfully be leveraged in the context of scientific machine learning.

Table 3: Average mean-squared error (MSE) of fair price predictions for the 2d Black–Scholes PDE over 20 runs (lower is better). Values are reported as [ × 10−4]. Best result in bold.

### Model Ablations and Sensitivity Studies

We now examine the role of individual design choices in NeuroLDS.

### Pre-training vs. direct discrepancy minimization

To assess whether pre-training is necessary, we compared two pipelines *in 2d, 3d, and 4d*: 1) Pre-train+FT: regress to Sobol' sequence and then fine-tune on the target discrepancy; 2) Direct: initialize randomly and optimize the discrepancy loss from scratch. We kept the architecture, optimizer, and budget fixed, and tuned hyperparameters for each pipeline via Optuna. Across all dimensions, the Direct variant consistently collapsed to a degenerate solution in which points concentrate near a corner of ${\lbrack 0,1\rbrack}^{d}$ (a pathology observed also in related work ), while Pre-train+FT remained stable. This indicates that Sobol'-based pre-training provides an essential inductive bias before discrepancy refinement.

### Alternative sequence generation with autoregressive GNNs

To test if explicit autoregression helps, we implemented an AR-GNN that emits one point conditioned on the previous prefix and compared it to our index-conditioned MLP *in 2d*. We matched parameter count and training budget and tuned both models with Optuna. While the AR-GNN performed reasonably for small sequence lengths, beyond a few hundred points the training signal became too weak to propagate through long contexts without truncation, and performance degraded relative to the index-based MLP. Because truncation undermines global low-discrepancy structure, we adopt the simpler index-based formulation, which proved more robust across dimensions.

### Effect of sinusoidal frequency parameter $K$

To isolate the contribution of the index encoding bandwidth, we trained models *in 2d, 3d, and 4d* that are *identical in every respect except $K$*, using $K \in {\{ 8,16,32\}}$ (Optuna re-tunes learning-rate and weight-decay per $K$). In 4d, the ablation is visualized in the dedicated panel figure (see Fig. 7): larger $K$ reduces fluctuations of $D_{2}^{\text{sym}}$ (i.e., more stable curves), whereas small $K$ (e.g., $8$) exhibits higher variance. Thus, increasing $K$ improves stability of the discrepancy profile at the cost of a modest increase in training time.

### Impact of non-linearities

We evaluated the necessity of depth by replacing the MLP with a purely linear map (followed by a sigmoid) and by a shallow one-hidden-layer ReLU MLP, all *in 2d and 3d* with Optuna-tuned hyperparameters. The linear model systematically failed to approximate Sobol'-like structure and yielded poor discrepancy throughout the prefix. A single hidden layer could reach competitive levels but required substantially longer training time. Our deeper MLP strikes a favorable accuracy--efficiency balance across dimensions.

### Impact of weights in fine-tuning discrepancy loss

We run on $d = 4$ with $10000$ points and optimal hyperparameters tuned via Optuna, and compare the effect of using uniform weighting $w_{P} = {1/{({N - 2})}}$ versus length-proportional weighting $w_{P^{\ast}} = {{2P}/{({{N^{2} + N} - 2})}}$. Clearly, from Figure 8 from the Appendix we see that performance is comparable: the uniform version performs slightly better for shorter prefixes, while $w_{P^{\ast}}$ yields lower discrepancy on longer prefixes. This matches intuition, since $w_{P^{\ast}}$ places more emphasis on later prefixes, thus optimizing them at the expense of early ones.

### Replacing the MLP with an LSTM

To assess whether recurrence offers any benefit for low-discrepancy sequence generation, we replace the index-conditioned MLP with a single-layer LSTM and evaluated both architectures for $d = 4$ under the $D_{2}^{\text{star}}$ objective with a target length of $500$ points. Hyperparameters for each model were tuned independently with Optuna, and Fig. 9 reports the best-performing trial from each sweep. In this controlled comparison, the LSTM's best configuration achieves a slightly lower discrepancy curve than the best MLP run, indicating that recurrent state can, at least in principle, capture marginally richer structure from the index embedding. However, this comes at a substantial computational cost: over five repeated sweeps, full MLP optimization requires roughly ten minutes on average, whereas the LSTM exceeds one hour. Because this gap grows even further for longer sequences, training an LSTM for 10,000 points becomes prohibitively expensive, especially given that the modest improvement it provides does not translate into any practical advantage. Consequently, the simpler MLP remains the more efficient architecture for NeuroLDS.

## Discussion

NeuroLDS shows that neural architectures can successfully generate LDS, providing a solution to the fixed $N$ limitation of the MPMC model (ruschkirk24), with strong empirical performance across numerical integration, path planning and scientific machine learning tasks. Our model formulation as presented here focuses on classical $L_{2}$-based discrepancy functions to target the uniform distribution on ${\lbrack 0,1\rbrack}^{d}$, the traditional setting for QMC methods. However, we note that the presented framework is flexible, and can be extended to more general notions of kernel discrepancies, such as Stein discrepancies (KSD_2016), enabling designs that compact non-uniform distributions into an extensible sequence of nodes.

Finally, we note that our reliance on Sobol' or Halton pre-alignment underlines the continued importance of classical number-theoretic and non-ML optimization-based QMC constructions, which provide the stability needed for successful training as highlighted in Section 3.3.
