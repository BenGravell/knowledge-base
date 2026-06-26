<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Factoring Nonnegative Matrices with Linear Programs

Topics include Nonnegative matrix factorization, Linear programming, Separable NMF, Topic modeling, Feature selection, Robust recovery, Large-scale optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces a linear-programming approach to separable nonnegative matrix factorization that identifies representative rows or features and expresses the remaining data through them. Beyond the clean convex formulation, the paper is notable for robustness analysis under more general noise than earlier separable-NMF methods and for showing that the resulting implementation can scale to multi-gigabyte data.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper describes a new approach, based on linear programming, for computing nonnegative matrix factorizations (NMFs). The key idea is a data-driven model for the factorization where the most salient features in the data are used to express the remaining features. More precisely, given a data matrix X, the algorithm identifies a matrix C such that X approximately equals CX and some linear constraints. The constraints are chosen to ensure that the matrix C selects features; these features can then be used to find a low-rank NMF of X. A theoretical analysis demonstrates that this approach has guarantees similar to those of the recent NMF algorithm of Arora et al.. In contrast with this earlier work, the proposed method extends to more general noise models and leads to efficient, scalable algorithms. Experiments with synthetic and real datasets provide evidence that the new approach is also superior in practice. An optimized C++ implementation can factor a multigigabyte matrix in a matter of minutes.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nonnegative matrix factorization (NMF) is a popular approach for selecting features in data. Many machine-learning and data-mining software packages (including Matlab, R, and Oracle Data Mining ) now include heuristic computational methods for NMF. Nevertheless, we still have limited theoretical understanding of when these heuristics are correct.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The difficulty in developing rigorous methods for NMF stems from the fact that the problem is computationally challenging. Indeed, Vavasis has shown that NMF is NP-Hard; see for further worst-case hardness results. As a consequence, we must instate additional assumptions on the data if we hope to compute nonnegative matrix factorizations in practice.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this spirit, Arora, Ge, Kannan, and Moitra (AGKM) have exhibited a polynomial-time algorithm for NMF that is provably correct---provided that the data is drawn from an appropriate model, based on ideas. The AGKM result describes one circumstance where we can be sure that NMF algorithms are capable of producing meaningful answers. This work has the potential to make an impact in machine learning because proper feature selection is an important preprocessing step for many other techniques. Even so, the actual impact is damped by the fact that the AGKM algorithm is too computationally expensive for large-scale problems and is not tolerant to departures from the modeling assumptions. Thus, for NMF, there remains a gap between the theoretical exercise and the actual practice of machine learning.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The present work presents a scalable, robust algorithm that can successfully solve the NMF problem under appropriate hypotheses. Our first contribution is a new formulation of the nonnegative feature selection problem that only requires the solution of a single linear program. Second, we provide a theoretical analysis of this algorithm. This argument shows that our method succeeds under the same modeling assumptions as the AGKM algorithm with an additional *margin constraint* that is common in machine learning. We prove that if there exists a unique, well-defined model, then we can recover this model accurately; our error bound improves substantially on the error bound for the AGKM algorithm in the high SNR regime. One may argue that NMF only "makes sense" (i.e., is well posed) when a unique solution exists, and so we believe our result has independent interest. Furthermore, our algorithm can be adapted for a wide class of noise models.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In addition to these theoretical contributions, our work also includes a major algorithmic and experimental component. Our formulation of NMF allows us to exploit methods from operations research and database systems to design solvers that scale to extremely large datasets. We develop an efficient stochastic gradient descent (SGD) algorithm that is (at least) two orders of magnitude faster than the approach of AGKM when both are implemented in Matlab. We describe a parallel implementation of our SGD algorithm that can robustly factor matrices with $10^{5}$ features and $10^{6}$ examples in a few minutes on a multicore workstation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our formulation of NMF uses a data-driven modeling approach to simplify the factorization problem. More precisely, we search for a small collection of rows from the data matrix that can be used to express the other rows. This type of approach appears in a number of other factorization problems, including rank-revealing QR, interpolative decomposition, subspace clustering, dictionary learning, and others. Our computational techniques can be adapted to address large-scale instances of these problems as well.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Separable Nonnegative Matrix Factorizations and Hott Topics", "weight": 1.0} -->

Let $\mathbf{Y}$ be a nonnegative $f \times n$ data matrix with columns indexing examples and rows indexing features. Exact NMF seeks a factorization ${\mathbf{Y}} = {{\mathbf{F}}{\mathbf{W}}}$ where the feature matrix $\mathbf{F}$ is $f \times r$, where the weight matrix $\mathbf{W}$ is $r \times n$, and both factors are nonnegative. Typically, $r \ll {\min{\{ f,n\}}}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Separable Nonnegative Matrix Factorizations and Hott Topics", "weight": 1.0} -->

Unless stated otherwise, we assume that each row of the data matrix $\mathbf{Y}$ is normalized so it sums to one. Under this hypothesis, we may also assume that each row of $\mathbf{F}$ and of $\mathbf{W}$ also sums to one.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Separable Nonnegative Matrix Factorizations and Hott Topics", "weight": 1.0} -->

It is notoriously difficult to solve the NMF problem. Vavasis showed that it is NP-complete to decide whether a matrix admits a rank-$r$ nonnegative factorization. AGKM proved that an exact NMF algorithm can be used to solve 3-SAT in subexponential time.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Separable Nonnegative Matrix Factorizations and Hott Topics", "weight": 1.0} -->

The literature contains some mathematical analysis of NMF that can be used to motivate algorithmic development. Thomas developed a necessary and sufficient condition for the existence of a rank-$r$ NMF. More recently, Donoho and Stodden obtained a related sufficient condition for uniqueness. AGKM exhibited an algorithm that can produce a nonnegative matrix factorization under a weaker sufficient condition. To state their results, we need a definition.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Main Theoretical Results: NMF by Linear Programming", "weight": 1.0} -->

This paper shows that we can factor an approximately separable nonnegative matrix by solving a linear program. A major advantage of this formulation is that it scales to very large data sets.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Main Theoretical Results: NMF by Linear Programming", "weight": 1.0} -->

Here is the key observation: Suppose that $\mathbf{Y}$ is any $f \times n$ nonnegative matrix that admits a rank-$r$ separable factorization ${\mathbf{Y}} = {{\mathbf{F}}{\mathbf{W}}}$. If we pad $\mathbf{F}$ with zeros to form an $f \times f$ matrix, we have We call the matrix $\mathbf{C}$ *factorization localizing*. Note that any factorization localizing matrix $\mathbf{C}$ is an element of the polyhedral set Thus, to find an exact NMF of $\mathbf{Y}$, it suffices to find a feasible element of ${\mathbf{C}} \in {\Phi{({\mathbf{Y}})}}$ whose diagonal is integral. This task can be accomplished by linear programming.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Main Theoretical Results: NMF by Linear Programming", "weight": 1.0} -->

Once we have such a $\mathbf{C}$, we construct $\mathbf{W}$ by extracting the rows of $\mathbf{X}$ that correspond to the indices $i$ where $C_{ii} = 1$. We construct the feature matrix $\mathbf{F}$ by extracting the nonzero columns of $\mathbf{C}$. This approach is summarized in Algorithm 2. In turn, we can prove the following result.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Robustness to Noise", "weight": 1.0} -->

Suppose we observe a nonnegative matrix $\mathbf{X}$ whose rows sum to one. Assume that ${\mathbf{X}} = {{\mathbf{Y}} + \mathbf{\Delta}}$ where $\mathbf{Y}$ is a nonnegative matrix whose rows sum to one, which has a rank-$r$ separable factorization ${\mathbf{Y}} = {{\mathbf{F}}{\mathbf{W}}}$ such that the rows of $\mathbf{W}$ are $\alpha$-robust simplicial, and where ${\parallel\mathbf{\Delta}\parallel}_{\infty,1} \leq \epsilon$. Define the polyhedral set The set $\Phi{({\mathbf{X}})}$ consists of matrices $\mathbf{C}$ that *approximately* locate a factorization of $\mathbf{X}$. We can prove the following result.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Incremental Gradient Algorithms for NMF", "weight": 1.0} -->

The rudiments of our fast implementation rely on two standard optimization techniques: dual decomposition and incremental gradient descent. Both techniques are described in depth in Chapters 3.4 and 7.8 of Bertsekas and Tstisklis.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Incremental Gradient Algorithms for NMF", "weight": 1.0} -->

Dual subgradient ascent solves this problem by alternating between minimizing the Lagrangian over the constraint set $\Phi_{0}$, and then taking a subgradient step with respect to the dual variables where ${\mathbf{C}}^{\star}$ is the minimizer of the Lagrangian over $\Phi_{0}$. The update of $w_{i}$ makes very little difference in the solution quality, so we typically only update $\beta$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Incremental Gradient Algorithms for NMF", "weight": 1.0} -->

We minimize the Lagrangian using projected incremental gradient descent. Note that we can rewrite the Lagrangian as Here, ${supp}{({\mathbf{x}})}$ is the set indexing the entries where $\mathbf{x}$ is nonzero, and $\mu_{j}$ is the number of nonzeros in row $j$ divided by $n$. The incremental gradient method chooses one of the $n$ summands at random and follows its subgradient. We then project the iterate onto the constraint set $\Phi_{0}$. The projection onto $\Phi_{0}$ can be performed in the time required to sort the individual columns of $\mathbf{C}$ plus a linear-time operation. The full procedure is described in Appendix B. In the case where we expect a unique solution, we can drop the constraint $C_{ij} \leq C_{jj}$, resulting in a simple clipping procedure: set all negative items to zero and set any diagonal entry exceeding one to one. In practice, we perform a tradeoff.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Incremental Gradient Algorithms for NMF", "weight": 1.0} -->

Since the constraint $C_{ij} \leq C_{jj}$ is used solely for symmetry breaking, we have found empirically that we only need to project onto $\Phi_{0}$ every $n$ iterations or so.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Incremental Gradient Algorithms for NMF", "weight": 1.0} -->

This incremental iteration is repeated $n$ times in a phase called an *epoch*. After each epoch, we update the dual variables and quit after we believe we have identified the large elements of the diagonal of $\mathbf{C}$. Just as before, once we have identified the hott rows, we can form $\mathbf{W}$ by selecting these rows of $\mathbf{X}$. We can find $\mathbf{F}$ just as before, by solving. Note that this minimization can also be computed by incremental subgradient descent. The full procedure, called Hottopixx, is described in Algorithm 4.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Incremental Gradient Algorithms for NMF", "weight": 1.0} -->

0: An f × n nonnegative matrix X. Primal and dual stepsizes sp and sd. 0: An f × r matrix F and r × n matrix W with F ≥ 0, W ≥ 0, and ∥ X − F W∥∞, 1 ≤ 2 ϵ. 1: Pick a cost p with distinct entries. 5: Choose k uniformly at random from [n]. 11: Let I = {i: Ci i = 1} and set W = XI⋅. 12: Set F = arg minZ ∈ ℝf × r ∥ X − ZW∥∞, 1 Algorithm 4 Hottopixx: Approximate Separable NMF by Incremental Gradient Descent

<!-- chunk {"id": "body-0024", "role": "body", "section": "Sparsity and Computational Enhancements for Large Scale", "weight": 1.0} -->

For small-scale problems, Hottopixx can be implemented in a few lines of Matlab code. But for the very large data sets studied in Section 5, we take advantage of natural parallelism and a host of low-level optimizations that are also enabled by our formulation. As in any numerical program, memory layout and cache behavior can be critical factors for performance. We use standard techniques: in-memory clustering to increase prefetching opportunities, padded data structures for better cache alignment, and compiler directives to allow the Intel compiler to apply vectorization.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Sparsity and Computational Enhancements for Large Scale", "weight": 1.0} -->

Note that the incremental gradient step (step 6 in Algorithm 4) only modifies the entries of $\mathbf{C}$ where ${\mathbf{X}}_{\cdot k}$ is nonzero. Thus, we can parallelize the algorithm with respect to updating either the rows or the columns of $\mathbf{C}$. We store $\mathbf{X}$ in large contiguous blocks of memory to encourage hardware prefetching. In contrast, we choose a dense representation of our localizing matrix $\mathbf{C}$; this choice trades space for runtime performance.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Sparsity and Computational Enhancements for Large Scale", "weight": 1.0} -->

Each worker thread is assigned a number of rows of $\mathbf{C}$ so that all rows fit in the shared L3 cache. Then, each worker thread repeatedly scans $\mathbf{X}$ while marking updates to multiple rows of $\mathbf{C}$. We repeat this process until all rows of $\mathbf{C}$ are scanned, similar to the classical block-nested loop join in relational databases.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

Except for the speedup curves, all of the experiments were run on an identical configuration: a dual Xeon X650 (6 cores each) machine with 128GB of RAM. The kernel is Linux 2.6.32-131.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments", "weight": 1.0} -->

In small-scale, synthetic experiments, we compared Hottopixx to the AGKM algorithm and the linear programming formulation of Algorithm 3 implemented in Matlab. Both AGKM and Algorithm 3 were run using CVX coupled to the SDPT3 solver. We ran Hottopixx for $50$ epochs with primal stepsize 1e-1 and dual stepsize 1e-2. Once the hott topics were identified, we fit $\mathbf{F}$ using two cleaning epochs of incremental gradient descent for all three algorithms.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

To generate our instances, we sampled $r$ hott topics uniformly from the unit simplex in ${\mathbb{R}}^{n}$. These topics were duplicated $d$ times. We generated the remaining $f - {r{({d + 1})}}$ rows to be random convex combinations of the hott topics, with the combinations selected uniformly at random. We then added noise with $(\infty,1)$-norm error bounded by $\eta \cdot \frac{\alpha^{2}}{20 + {13\alpha}}$. Recall that AGKM algorithm is only guaranteed to work for $\eta < 1$. We ran with $f \in {\{ 40,80,160\}}$, $n \in {\{ 400,800,1600\}}$, $r \in {\{ 3,5,10\}}$, $d \in {\{ 0,1,2\}}$, and $\eta \in {\{ 0.25,0.95,4,10,100\}}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

Each experiment was repeated $5$ times.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

Because we ran over $2000$ experiments with $405$ different parameter settings, it is convenient to use the *performance profiles* to compare the performance of the different algorithms. Let $\mathcal{P}$ be the set of experiments and $\mathcal{A}$ denote the set of different algorithms we are comparing. Let $Q_{a}{(p)}$ be the value of some performance metric of the experiment $p \in \mathcal{P}$ for algorithm $a \in \mathcal{A}$. Then the performance profile at $\tau$ for a particular algorithm is the fraction of the experiments where the value of $Q_{a}{(p)}$ lies within a factor of $\tau$ of the minimal value of ${\min_{b \in \mathcal{A}}Q_{b}}{(p)}$. That is, In a performance profile, the higher a curve corresponding to an algorithm, the more often it outperforms the other algorithms. This gives a convenient way to contrast algorithms visually.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our performance profiles are shown in Figure 2. The first two figures correspond to experiments with $f = 40$ and $n = 400$. The third figure is for the synthetic experiments with all other values of $f$ and $n$. In terms of $(\infty,1)$-norm error, the linear programming solver typically achieves the lowest error. However, using SDPT3, it is prohibitively slow to factor larger matrices. On the other hand, Hottopixx achieves better noise performance than the AGKM algorithm in much less time. Moreover, the AGKM algorithm must be fed the values of $\epsilon$ and $\alpha$ in order to run. Hottopixx does not require this information and still achieves about the same error performance.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

We also display a graph for running only four epochs (hott (fast)). This algorithm is by far the fastest algorithm, but does not achieve as optimal a noise performance. For very high levels of noise, however, it achieves a lower reconstruction error than the AGKM algorithm, whose performance degrades once $\eta$ approaches or exceeds $1$ (Figure 2(f)). We also provide performance profiles for the root-mean-square error of the nonnegative matrix factorizations (Figure 2 (d) and (e)). The performance is qualitatively similar to that for the $(\infty,1)$-norm.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

We also coded Hottopixx in C++, using the design principles described in Section 4.1, and ran on three large data sets. We generated a large synthetic example (jumbo) as above with $r = 100$. We generated a co-occurrence matrix of people and places from the Dataset, normalized by TFIDF. We also used Hottopixx to select features from the RCV1 data set to recognize the class CCAT. The statistics for these data sets can be found in Table 1.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

In Figure 3 (left), we plot the speed-up over a serial implementation. In contrast to other parallel methods that exhibit memory contention, we see superlinear speed-ups for up to 20 threads due to hardware prefetching and cache effects. All three of our large data sets can be trained in minutes, showing that we can scale Hottopixx on both synthetic and real data. Our algorithm is able to correctly identify the hott topics on the jumbo set. For clueweb, we plot the RMSE Figure 3 (middle). This curve rolls off quickly for the first few hundred topics, demonstrating that our algorithm may be useful for dimensionality reduction in Natural Language Processing applications. For RCV1, we trained an SVM on the set of features extracted by Hottopixx and plot the misclassification error versus the number of topics in Figure 3 (right). With $1500$ hott topics, we achieve $7\%$ misclassification error as compared to $5.5\%$ with the entire set of features.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Discussion", "weight": 1.5} -->

This paper provides an algorithmic and theoretical framework for analyzing and deploying any factorization problem that can be posed as a linear (or convex) factorization localizing program. Future work should investigate the applicability of Hottopixx to other factorization localizing algorithms, such as subspace clustering, and should revisit earlier theoretical bounds on such prior art.
