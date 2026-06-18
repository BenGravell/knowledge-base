## Introduction

Nonnegative matrix factorization (NMF) is a popular approach for selecting features in data. Many machine-learning and data-mining software packages (including Matlab, R, and Oracle Data Mining ) now include heuristic computational methods for NMF. Nevertheless, we still have limited theoretical understanding of when these heuristics are correct.

The difficulty in developing rigorous methods for NMF stems from the fact that the problem is computationally challenging. Indeed, Vavasis has shown that NMF is NP-Hard; see for further worst-case hardness results. As a consequence, we must instate additional assumptions on the data if we hope to compute nonnegative matrix factorizations in practice.

In this spirit, Arora, Ge, Kannan, and Moitra (AGKM) have exhibited a polynomial-time algorithm for NMF that is provably correct---provided that the data is drawn from an appropriate model, based on ideas from. The AGKM result describes one circumstance where we can be sure that NMF algorithms are capable of producing meaningful answers. This work has the potential to make an impact in machine learning because proper feature selection is an important preprocessing step for many other techniques. Even so, the actual impact is damped by the fact that the AGKM algorithm is too computationally expensive for large-scale problems and is not tolerant to departures from the modeling assumptions. Thus, for NMF, there remains a gap between the theoretical exercise and the actual practice of machine learning.

The present work presents a scalable, robust algorithm that can successfully solve the NMF problem under appropriate hypotheses. Our first contribution is a new formulation of the nonnegative feature selection problem that only requires the solution of a single linear program. Second, we provide a theoretical analysis of this algorithm. This argument shows that our method succeeds under the same modeling assumptions as the AGKM algorithm with an additional *margin constraint* that is common in machine learning. We prove that if there exists a unique, well-defined model, then we can recover this model accurately; our error bound improves substantially on the error bound for the AGKM algorithm in the high SNR regime. One may argue that NMF only "makes sense" (i.e., is well posed) when a unique solution exists, and so we believe our result has independent interest. Furthermore, our algorithm can be adapted for a wide class of noise models.

In addition to these theoretical contributions, our work also includes a major algorithmic and experimental component. Our formulation of NMF allows us to exploit methods from operations research and database systems to design solvers that scale to extremely large datasets. We develop an efficient stochastic gradient descent (SGD) algorithm that is (at least) two orders of magnitude faster than the approach of AGKM when both are implemented in Matlab. We describe a parallel implementation of our SGD algorithm that can robustly factor matrices with $10^{5}$ features and $10^{6}$ examples in a few minutes on a multicore workstation.

Our formulation of NMF uses a data-driven modeling approach to simplify the factorization problem. More precisely, we search for a small collection of rows from the data matrix that can be used to express the other rows. This type of approach appears in a number of other factorization problems, including rank-revealing QR, interpolative decomposition, subspace clustering, dictionary learning, and others. Our computational techniques can be adapted to address large-scale instances of these problems as well.

## Separable Nonnegative Matrix Factorizations and Hott Topics

Notation. For a matrix $\mathbf{M}$ and indices $i$ and $j$, we write ${\mathbf{M}}_{i \cdot}$ for the $i$th row of $\mathbf{M}$ and ${\mathbf{M}}_{\cdot j}$ for the $j$th column of $\mathbf{M}$. We write $M_{ij}$ for the $(i,j)$ entry.

Let $\mathbf{Y}$ be a nonnegative $f \times n$ data matrix with columns indexing examples and rows indexing features. Exact NMF seeks a factorization ${\mathbf{Y}} = {{\mathbf{F}}{\mathbf{W}}}$ where the feature matrix $\mathbf{F}$ is $f \times r$, where the weight matrix $\mathbf{W}$ is $r \times n$, and both factors are nonnegative. Typically, $r \ll {\min{\{ f,n\}}}$.

Unless stated otherwise, we assume that each row of the data matrix $\mathbf{Y}$ is normalized so it sums to one. Under this hypothesis, we may also assume that each row of $\mathbf{F}$ and of $\mathbf{W}$ also sums to one.

It is notoriously difficult to solve the NMF problem. Vavasis showed that it is NP-complete to decide whether a matrix admits a rank-$r$ nonnegative factorization. AGKM proved that an exact NMF algorithm can be used to solve 3-SAT in subexponential time.

The literature contains some mathematical analysis of NMF that can be used to motivate algorithmic development. Thomas developed a necessary and sufficient condition for the existence of a rank-$r$ NMF. More recently, Donoho and Stodden obtained a related sufficient condition for uniqueness. AGKM exhibited an algorithm that can produce a nonnegative matrix factorization under a weaker sufficient condition. To state their results, we need a definition.

### Definition 2.1

A set of vectors ${\{\mathbf{v}_{1},\ldots,\mathbf{v}_{r}\}} \subset {\mathbb{R}}^{d}$ is *simplicial* if no vector $\mathbf{v}_{i}$ lies in the convex hull of $\{\mathbf{v}_{j}:{j \neq i}\}$. The set of vectors is *$\alpha$-robust simplicial* if, for each $i$, the $\ell_{1}$ distance from $\mathbf{v}_{i}$ to the convex hull of $\{\mathbf{v}_{j}:{j \neq i}\}$ is at least $\alpha$. Figure 1 illustrates these concepts.

Algorithm 1 AGKM: Approximably Separable Nonnegative Matrix Factorization

2: Compute the f × f matrix D with Di j = ∥Xi⋅ − Xj⋅∥1.
4: Find the set 𝒩k of rows that are at least 5 ϵ/α + 2 ϵ away from Xk⋅.
5: Compute the distance δk of Xk⋅ from conv({Xj⋅:j ∈ 𝒩k}).
6: if δk &gt; 2 ϵ, add k to the set R.
8: Cluster the rows in R as follows: j and k are in the same cluster if Dj k ≤ 10 ϵ/α + 6 ϵ.
9: Choose one element from each cluster to yield W.

Figure 1: Numbered circles are hott topics. Their convex hull (orange) contains the other topics (small circles), so the data admits a separable NMF. The arrow d1 marks the ℓ1 distance from hott topic to the convex hull of the other two hott topics; definitions of d2 and d3 are similar. The hott topics are α-robustly simplicial when each di ≥ α.

These ideas support the uniqueness results of Donoho and Stodden and the AGKM algorithm. Indeed, we can find an NMF of $\mathbf{Y}$ efficiently if $\mathbf{Y}$ contains a set of $r$ rows that is simplicial and whose convex hull contains the remaining rows.

### Definition 2.2

An NMF $\mathbf{Y} = {\mathbf{F}\mathbf{W}}$ is called *separable* if the rows of $\mathbf{W}$ are simplicial and there is a permutation matrix $\mathbf{\Pi}$ such that

To compute a separable factorization of $\mathbf{Y}$, we must first identify a simplicial set of rows from $\mathbf{Y}$. Afterward, we compute weights that express the remaining rows as convex combinations of this distinguished set. We call the simplicial rows *hott* and the corresponding features *hott topics*.

This model allows us to express all the features for a particular instance if we know the values of the instance at the simplicial rows. This assumption can be justified in a variety of applications. For example, in text, knowledge of a few keywords may be sufficient to reconstruct counts of the other words in a document. In vision, localized features can be used to predict gestures. In audio data, a few bins of the spectrogram may allow us to reconstruct the remaining bins.

While a nonnegative matrix one encounters in practice might not admit a separable factorization, it may be *well-approximated* by a nonnnegative matrix with separable factorization. AGKM derived an algorithm for nonnegative matrix factorization of a matrix that is well-approximated by a separable factorization. To state their result, we introduce a norm on $f \times n$ matrices:

### Theorem 2.3 (AGKM \[4\])

Let $\epsilon$ and $\alpha$ be nonnegative constants satisfying $\epsilon \leq \frac{\alpha^{2}}{20 + {13\alpha}}$. Let $\mathbf{X}$ be a nonnegative data matrix. Assume $\mathbf{X} = {\mathbf{Y} + \mathbf{\Delta}}$ where $\mathbf{Y}$ is a nonnegative matrix whose rows have unit $\ell_{1}$ norm, where $\mathbf{Y} = {\mathbf{F}\mathbf{W}}$ is a rank-$r$ separable factorization in which the rows of $\mathbf{W}$ are $\alpha$-robust simplicial, and where ${\parallel\mathbf{\Delta}\parallel}_{\infty,1} \leq \epsilon$. Then Algorithm 1 finds a rank-$r$ nonnegative factorization $\hat{\mathbf{F}}\hat{\mathbf{W}}$ that satisfies the error bound ${\parallel{\mathbf{X} - {\hat{\mathbf{F}}\hat{\mathbf{W}}}}\parallel}_{\infty,1} \leq {{{10\epsilon}/\alpha} + {7\epsilon}}$.

In particular, the AGKM algorithm computes the factorization exactly when $\epsilon = 0$. Although this method is guaranteed to run in polynomial time, it has many undesirable features. First, the algorithm requires a priori knowledge of the parameters $\alpha$ and $\epsilon$. It may be possible to calculate $\epsilon$, but we can only estimate $\alpha$ if we know which rows are hott. Second, the algorithm computes all $\ell_{1}$ distances between rows at a cost of $O{({f^{2}n})}$. Third, for every row in the matrix, we must determine its distance to the convex hull of the rows that lie at a sufficient distance; this step requires us to solve a linear program for each row of the matrix at a cost of $\Omega{({fn})}$. Finally, this method is intimately linked to the choice of the error norm ${\parallel \cdot \parallel}_{\infty,1}$. It is not obvious how to adapt the algorithm for other noise models. We present a new approach, based on linear programming, that overcomes these drawbacks.

## Main Theoretical Results: NMF by Linear Programming

This paper shows that we can factor an approximately separable nonnegative matrix by solving a linear program. A major advantage of this formulation is that it scales to very large data sets.

Here is the key observation: Suppose that $\mathbf{Y}$ is any $f \times n$ nonnegative matrix that admits a rank-$r$ separable factorization ${\mathbf{Y}} = {{\mathbf{F}}{\mathbf{W}}}$. If we pad $\mathbf{F}$ with zeros to form an $f \times f$ matrix, we have

We call the matrix $\mathbf{C}$ *factorization localizing*. Note that any factorization localizing matrix $\mathbf{C}$ is an element of the polyhedral set

Thus, to find an exact NMF of $\mathbf{Y}$, it suffices to find a feasible element of ${\mathbf{C}} \in {\Phi{({\mathbf{Y}})}}$ whose diagonal is integral. This task can be accomplished by linear programming. Once we have such a $\mathbf{C}$, we construct $\mathbf{W}$ by extracting the rows of $\mathbf{X}$ that correspond to the indices $i$ where $C_{ii} = 1$. We construct the feature matrix $\mathbf{F}$ by extracting the nonzero columns of $\mathbf{C}$. This approach is summarized in Algorithm 2. In turn, we can prove the following result.

### Theorem 3.1

Suppose $\mathbf{Y}$ is a nonnegative matrix with a rank-$r$ separable factorization $\mathbf{Y} = {\mathbf{F}\mathbf{W}}$. Then Algorithm 2 constructs a rank-$r$ nonnegative matrix factorization of $\mathbf{Y}$.

As the theorem suggests, we can isolate the rows of $\mathbf{Y}$ that yield a simplicial factorization by solving a single linear program. The factor $\mathbf{F}$ can be found by extracting columns of $\mathbf{C}$.

0: An f × n nonnegative matrix Y with a rank-r separable NMF.
0: An f × r matrix F and r × n matrix W with F ≥ 0, W ≥ 0, and Y = F W.
1: Find the unique C ∈ Φ (Y) to minimize pT diag(C) where p is any vector with distinct values.
2: Let I = {i: Ci i = 1} and set W = YI⋅ and F = C⋅I.
Algorithm 2 Separable Nonnegative Matrix Factorization by Linear Programming

### Robustness to Noise

Suppose we observe a nonnegative matrix $\mathbf{X}$ whose rows sum to one. Assume that ${\mathbf{X}} = {{\mathbf{Y}} + \mathbf{\Delta}}$ where $\mathbf{Y}$ is a nonnegative matrix whose rows sum to one, which has a rank-$r$ separable factorization ${\mathbf{Y}} = {{\mathbf{F}}{\mathbf{W}}}$ such that the rows of $\mathbf{W}$ are $\alpha$-robust simplicial, and where ${\parallel\mathbf{\Delta}\parallel}_{\infty,1} \leq \epsilon$. Define the polyhedral set

The set $\Phi{({\mathbf{X}})}$ consists of matrices $\mathbf{C}$ that *approximately* locate a factorization of $\mathbf{X}$. We can prove the following result.

### Theorem 3.2

Suppose that $\mathbf{X}$ satisfies the assumptions stated in the previous paragraph. Furthermore, assume that for every row $\mathbf{Y}_{j, \cdot}$ that is not hott, we have the margin constraint ${\|{\mathbf{Y}_{j, \cdot} - \mathbf{Y}_{i, \cdot}}\|} \geq d_{0}$ for all hott rows $i$. Then we can find a nonnegative factorization satisfying ${\parallel{\mathbf{X} - {\hat{\mathbf{F}}\hat{\mathbf{W}}}}\parallel}_{\infty,1} \leq {2\epsilon}$ provided that $\epsilon < \frac{\min{\{{\alphad_{0}},\alpha^{2}\}}}{9{({r + 1})}}$. Furthermore, this factorization correctly identifies the hott topics appearing in the separable factorization of $\mathbf{Y}$.

Algorithm 3 requires the solution of two linear programs. The first minimizes a cost vector over $\Phi_{2\epsilon}{({\mathbf{X}})}$. This lets us find $\hat{\mathbf{W}}$. Afterward, the matrix $\hat{\mathbf{F}}$ can be found by setting

0: An f × n nonnegative matrix X that satisfies the hypotheses of Theorem 3.2.
0: An f × r matrix F and r × n matrix W with F ≥ 0, W ≥ 0, and ∥ X − F W∥∞, 1 ≤ 2 ϵ.
1: Find C ∈ Φ2 ϵ (X) that minimizes pT diagC where p is any vector with distinct values.
2: Let I = {i: Ci i = 1} and set W = XI⋅.
3: Set F = arg minZ ∈ ℝf × r ∥ X − ZW∥∞, 1
Algorithm 3 Approximably Separable Nonnegative Matrix Factorization by Linear Programming

Our robustness result requires a *margin-type* constraint assuming that the original configuration consists either of duplicate hott topics, or topics that are reasonably far away from the hott topics. On the other hand, under such a margin constraint, we can construct a considerably better approximation than that guaranteed by the AGKM algorithm. Moreover, unlike AGKM, our algorithm does not need to know the parameter $\alpha$.

The proofs of Theorems 3.1 and 3.2 can be found in the appendix. The main idea is to show that we can only represent a hott topic efficiently using the hott topic itself. Some earlier versions of this paper contained incomplete arguments, which we have remedied. For a signifcantly stronger robustness analysis of Algorithm 3, see the recent paper.

Having established these theoretical guarantees, it now remains to develop an algorithm to solve the LP. Off-the-shelf LP solvers may suffice for moderate-size problems, but for large-scale matrix factorization problems, their running time is prohibitive, as we show in Section 5. In Section 4, we turn to describe how to solve Algorithm 3 efficiently for large data sets.

### Related Work

Localizing factorizations via column or row subset selection is a popular alternative to direct factorization methods such as the SVD. Interpolative decomposition such as Rank-Revealing QR and CUR have favorable efficiency properties as compared to factorizations (such as SVD) that are not based on exemplars. Factorization localization has been used in subspace clustering and has been shown to be robust to outliers.

In recent work on dictionary learning, Esser et al. and Elhamifar et al. have proposed a factorization localization solution to nonnegative matrix factorization using group sparsity techniques. Esser et al. prove asymptotic exact recovery in a restricted noise model, but this result requires preprocessing to remove duplicate or near-duplicate rows. Elhamifar shows exact representative recovery in the noiseless setting assuming no hott topics are duplicated. Our work here improves upon this work in several aspects, enabling finite sample error bounds, the elimination of any need to preprocess the data, and algorithmic implementations that scale to very large data sets.

## Incremental Gradient Algorithms for NMF

The rudiments of our fast implementation rely on two standard optimization techniques: dual decomposition and incremental gradient descent. Both techniques are described in depth in Chapters 3.4 and 7.8 of Bertsekas and Tstisklis.

We aim to minimize ${\mathbf{p}}^{T}{{diag}{({\mathbf{C}})}}$ subject to ${\mathbf{C}} \in {\Phi_{\tau}{({\mathbf{X}})}}$. To proceed, form the Lagrangian

with multipliers $\beta$ and ${\mathbf{w}} \geq \mathbf{0}$. Note that we do not dualize out all of the constraints. The remaining ones appear in the constraint set $\Phi_{0} = {\{{\mathbf{C}}:{{{\mathbf{C}} \geq \mathbf{0}},{{{{diag}{({\mathbf{C}})}} \leq 1},{{\text{~and~}C_{ij}} \leq {{C_{jj}\text{for all}i},j}}}}\}}$.

Dual subgradient ascent solves this problem by alternating between minimizing the Lagrangian over the constraint set $\Phi_{0}$, and then taking a subgradient step with respect to the dual variables

where ${\mathbf{C}}^{\star}$ is the minimizer of the Lagrangian over $\Phi_{0}$. The update of $w_{i}$ makes very little difference in the solution quality, so we typically only update $\beta$.

We minimize the Lagrangian using projected incremental gradient descent. Note that we can rewrite the Lagrangian as

Here, ${supp}{({\mathbf{x}})}$ is the set indexing the entries where $\mathbf{x}$ is nonzero, and $\mu_{j}$ is the number of nonzeros in row $j$ divided by $n$. The incremental gradient method chooses one of the $n$ summands at random and follows its subgradient. We then project the iterate onto the constraint set $\Phi_{0}$. The projection onto $\Phi_{0}$ can be performed in the time required to sort the individual columns of $\mathbf{C}$ plus a linear-time operation. The full procedure is described in Appendix B. In the case where we expect a unique solution, we can drop the constraint $C_{ij} \leq C_{jj}$, resulting in a simple clipping procedure: set all negative items to zero and set any diagonal entry exceeding one to one. In practice, we perform a tradeoff. Since the constraint $C_{ij} \leq C_{jj}$ is used solely for symmetry breaking, we have found empirically that we only need to project onto $\Phi_{0}$ every $n$ iterations or so.

This incremental iteration is repeated $n$ times in a phase called an *epoch*. After each epoch, we update the dual variables and quit after we believe we have identified the large elements of the diagonal of $\mathbf{C}$. Just as before, once we have identified the hott rows, we can form $\mathbf{W}$ by selecting these rows of $\mathbf{X}$. We can find $\mathbf{F}$ just as before, by solving. Note that this minimization can also be computed by incremental subgradient descent. The full procedure, called Hottopixx, is described in Algorithm 4.

0: An f × n nonnegative matrix X. Primal and dual stepsizes sp and sd.
0: An f × r matrix F and r × n matrix W with F ≥ 0, W ≥ 0, and ∥ X − F W∥∞, 1 ≤ 2 ϵ.
1: Pick a cost p with distinct entries.
5: Choose k uniformly at random from [n].
11: Let I = {i: Ci i = 1} and set W = XI⋅.
12: Set F = arg minZ ∈ ℝf × r ∥ X − ZW∥∞, 1
Algorithm 4 Hottopixx: Approximate Separable NMF by Incremental Gradient Descent

### Sparsity and Computational Enhancements for Large Scale

For small-scale problems, Hottopixx can be implemented in a few lines of Matlab code. But for the very large data sets studied in Section 5, we take advantage of natural parallelism and a host of low-level optimizations that are also enabled by our formulation. As in any numerical program, memory layout and cache behavior can be critical factors for performance. We use standard techniques: in-memory clustering to increase prefetching opportunities, padded data structures for better cache alignment, and compiler directives to allow the Intel compiler to apply vectorization.

Note that the incremental gradient step (step 6 in Algorithm 4) only modifies the entries of $\mathbf{C}$ where ${\mathbf{X}}_{\cdot k}$ is nonzero. Thus, we can parallelize the algorithm with respect to updating either the rows or the columns of $\mathbf{C}$. We store $\mathbf{X}$ in large contiguous blocks of memory to encourage hardware prefetching. In contrast, we choose a dense representation of our localizing matrix $\mathbf{C}$; this choice trades space for runtime performance.

Each worker thread is assigned a number of rows of $\mathbf{C}$ so that all rows fit in the shared L3 cache. Then, each worker thread repeatedly scans $\mathbf{X}$ while marking updates to multiple rows of $\mathbf{C}$. We repeat this process until all rows of $\mathbf{C}$ are scanned, similar to the classical block-nested loop join in relational databases.

## Experiments

Except for the speedup curves, all of the experiments were run on an identical configuration: a dual Xeon X650 (6 cores each) machine with 128GB of RAM. The kernel is Linux 2.6.32-131.

In small-scale, synthetic experiments, we compared Hottopixx to the AGKM algorithm and the linear programming formulation of Algorithm 3 implemented in Matlab. Both AGKM and Algorithm 3 were run using CVX coupled to the SDPT3 solver. We ran Hottopixx for $50$ epochs with primal stepsize 1e-1 and dual stepsize 1e-2. Once the hott topics were identified, we fit $\mathbf{F}$ using two cleaning epochs of incremental gradient descent for all three algorithms.

To generate our instances, we sampled $r$ hott topics uniformly from the unit simplex in ${\mathbb{R}}^{n}$. These topics were duplicated $d$ times. We generated the remaining $f - {r{({d + 1})}}$ rows to be random convex combinations of the hott topics, with the combinations selected uniformly at random. We then added noise with $(\infty,1)$-norm error bounded by $\eta \cdot \frac{\alpha^{2}}{20 + {13\alpha}}$. Recall that AGKM algorithm is only guaranteed to work for $\eta < 1$. We ran with $f \in {\{ 40,80,160\}}$, $n \in {\{ 400,800,1600\}}$, $r \in {\{ 3,5,10\}}$, $d \in {\{ 0,1,2\}}$, and $\eta \in {\{ 0.25,0.95,4,10,100\}}$. Each experiment was repeated $5$ times.

Because we ran over $2000$ experiments with $405$ different parameter settings, it is convenient to use the *performance profiles* to compare the performance of the different algorithms. Let $\mathcal{P}$ be the set of experiments and $\mathcal{A}$ denote the set of different algorithms we are comparing. Let $Q_{a}{(p)}$ be the value of some performance metric of the experiment $p \in \mathcal{P}$ for algorithm $a \in \mathcal{A}$. Then the performance profile at $\tau$ for a particular algorithm is the fraction of the experiments where the value of $Q_{a}{(p)}$ lies within a factor of $\tau$ of the minimal value of ${\min_{b \in \mathcal{A}}Q_{b}}{(p)}$. That is,

In a performance profile, the higher a curve corresponding to an algorithm, the more often it outperforms the other algorithms. This gives a convenient way to contrast algorithms visually.

Figure 2: Performance profiles for synthetic data. (a) (∞,1)-norm error for 40 × 400 sized instances and (b) all instances. (c) is the performance profile for running time on all instances. RMSE performance profiles for the (d) small scale and (e) medium scale experiments. (f) (∞,1)-norm error for the η ≥ 1. In the noisy examples, even 4 epochs of Hottopixx is sufficient to obtain competitive reconstruction error.

Our performance profiles are shown in Figure 2. The first two figures correspond to experiments with $f = 40$ and $n = 400$. The third figure is for the synthetic experiments with all other values of $f$ and $n$. In terms of $(\infty,1)$-norm error, the linear programming solver typically achieves the lowest error. However, using SDPT3, it is prohibitively slow to factor larger matrices. On the other hand, Hottopixx achieves better noise performance than the AGKM algorithm in much less time. Moreover, the AGKM algorithm must be fed the values of $\epsilon$ and $\alpha$ in order to run. Hottopixx does not require this information and still achieves about the same error performance.

We also display a graph for running only four epochs (hott (fast)). This algorithm is by far the fastest algorithm, but does not achieve as optimal a noise performance. For very high levels of noise, however, it achieves a lower reconstruction error than the AGKM algorithm, whose performance degrades once $\eta$ approaches or exceeds $1$ (Figure 2(f)). We also provide performance profiles for the root-mean-square error of the nonnegative matrix factorizations (Figure 2 (d) and (e)). The performance is qualitatively similar to that for the $(\infty,1)$-norm.

We also coded Hottopixx in C++, using the design principles described in Section 4.1, and ran on three large data sets. We generated a large synthetic example (jumbo) as above with $r = 100$. We generated a co-occurrence matrix of people and places from the Dataset, normalized by TFIDF. We also used Hottopixx to select features from the RCV1 data set to recognize the class CCAT. The statistics for these data sets can be found in Table 1.

Table 1: Description of the large data sets. Time is to find 100 hott topics on the 12 core machines.

In Figure 3 (left), we plot the speed-up over a serial implementation. In contrast to other parallel methods that exhibit memory contention, we see superlinear speed-ups for up to 20 threads due to hardware prefetching and cache effects. All three of our large data sets can be trained in minutes, showing that we can scale Hottopixx on both synthetic and real data. Our algorithm is able to correctly identify the hott topics on the jumbo set. For clueweb, we plot the RMSE Figure 3 (middle). This curve rolls off quickly for the first few hundred topics, demonstrating that our algorithm may be useful for dimensionality reduction in Natural Language Processing applications. For RCV1, we trained an SVM on the set of features extracted by Hottopixx and plot the misclassification error versus the number of topics in Figure 3 (right). With $1500$ hott topics, we achieve $7\%$ misclassification error as compared to $5.5\%$ with the entire set of features.

Figure 3: (left) The speedup over a serial implementation for Hottopixx on the jumbo and clueweb data sets. Note the superlinear speedup for up to 20 threads. (middle) The RMSE for the clueweb data set. (right) The test error on RCV1 CCAT class versus the number of hott topics. The horizontal line indicates the test error achieved using all of the features.

## Discussion

This paper provides an algorithmic and theoretical framework for analyzing and deploying any factorization problem that can be posed as a linear (or convex) factorization localizing program. Future work should investigate the applicability of Hottopixx to other factorization localizing algorithms, such as subspace clustering, and should revisit earlier theoretical bounds on such prior art.
