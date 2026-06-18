<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Perturbed Iterate Analysis for Asynchronous Stochastic Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce and analyze stochastic optimization methods where the input to each gradient update is perturbed by bounded noise. We show that this framework forms the basis of a unified approach to analyze asynchronous implementations of stochastic optimization algorithms.In this framework, asynchronous stochastic optimization algorithms can be thought of as serial methods operating on noisy inputs. Using our perturbed iterate framework, we provide new analyses of the Hogwild! algorithm and asynchronous stochastic coordinate descent, that are simpler than earlier analyses, remove many assumptions of previous models, and in some cases yield improved upper bounds on the convergence rates. We proceed to apply our framework to develop and analyze KroMagnon: a novel, parallel, sparse stochastic variance-reduced gradient (SVRG) algorithm. We demonstrate experimentally on a 16-core machine that the sparse and parallel version of SVRG is in some cases more than four orders of magnitude faster than the standard SVRG algorithm.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Asynchronous parallel stochastic optimization algorithms have recently gained significant traction in algorithmic machine learning. A large body of recent work has demonstrated that near-linear speedups are achievable, in theory and practice, on many common machine learning tasks. Moreover, when these lock-free algorithms are applied to non-convex optimization, significant speedups are still achieved with no loss of statistical accuracy. This behavior has been demonstrated in practice in state-of-the-art deep learning systems such as Google's Downpour SGD and Microsoft's Project Adam.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although asynchronous stochastic algorithms are simple to implement and enjoy excellent performance in practice, they are challenging to analyze theoretically. The current analyses require lengthy derivations and several assumptions that may not reflect realistic system behavior. Moreover, due to the difficult nature of the proofs, the algorithms analyzed are often simplified versions of those actually run in practice.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a general framework for deriving convergence rates for parallel, lock-free, asynchronous first-order stochastic algorithms. We interpret the algorithmic effects of asynchrony as perturbing the stochastic iterates with bounded noise. This interpretation allows us to show how a variety of asynchronous first-order algorithms can be analyzed as their serial counterparts operating on noisy inputs. The advantage of our framework is that it yields elementary convergence proofs, can remove or relax simplifying assumptions adopted in prior art, and can yield improved bounds when compared to earlier work.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate the general applicability of our framework by providing new convergence analyses for Hogwild!, *i.e.*, the asynchronous stochastic gradient method (SGM), for asynchronous stochastic coordinate descent (ASCD), and KroMagnon: a novel asynchronous sparse version of the stochastic variance-reduced gradient (SVRG) method. In particular, we provide a modified version of SVRG that allows for sparse updates, we show that this method can be parallelized in the asynchronous model, and we provide convergence guarantees using our framework. Experimentally, the asynchronous, parallel sparse SVRG achieves nearly-linear speedups on a machine with 16 cores and is sometimes four orders of magnitude faster than the standard (dense) SVRG method.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Perturbed Iterates", "weight": 1.0} -->

A popular way to minimize convex functions is via first-order stochastic algorithms.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Perturbed Iterates", "weight": 1.0} -->

where $\xi_{j}$ is a random variable independent of $\mathbf{x}_{j}$ and $\mathbf{g}$ is an unbiased estimator of the true gradient of $f$ at $\mathbf{x}_{j}$: ${{\mathbb{E}}_{\xi_{j}}\mathbf{g}{(\mathbf{x}_{j},\xi_{j})}} = {{\nabla f}{(\mathbf{x}_{j})}}$. The success of first-order stochastic techniques partly lies in their computational efficiency: the small computational cost of using noisy gradient estimates trumps the gains of using true gradients.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Perturbed Iterates", "weight": 1.0} -->

A major advantage of the iterative formula in (2.1) is that---in combination with strong convexity, and smoothness inequalities---one can easily track algorithmic progress and establish convergence rates to the optimal solution. Unfortunately, the progress of asynchronous parallel algorithms cannot be precisely described or analyzed using the above iterative framework. Processors do not read from memory actual iterates $\mathbf{x}_{j}$, as there is no global clock that synchronizes reads or writes while different cores write/read "stale" variables.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Perturbed Iterates", "weight": 1.0} -->

In the subsequent sections, we show that the following simple perturbed variant of Eq. (2.1) can capture the algorithmic progress of asynchronous stochastic algorithms. Consider the following iteration

<!-- chunk {"id": "body-0011", "role": "body", "section": "Perturbed Iterates", "weight": 1.0} -->

We assume that ${\hat{\mathbf{x}}}_{j}$ and $\xi_{j}$ are independent. However, in contrast to recursion (2.1), we no longer require $\mathbf{x}_{j}$ to be independent of $\xi_{j}$. The importance of the above independence assumption will become clear in the next section.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Perturbed Iterates", "weight": 1.0} -->

where the second inequality is a simple consequence of the triangle inequality. Now, let $a_{j} = {{\mathbb{E}}{\|{\mathbf{x}_{j} - \mathbf{x}^{\ast}}\|}^{2}}$ and substitute (2.4) back into Eq. (2.3) to get

<!-- chunk {"id": "body-0013", "role": "body", "section": "Perturbed Iterates", "weight": 1.0} -->

The recursive equation (2.5) is key to our analysis. We show that for given $R_{0}^{j}$, $R_{1}^{j}$, and $R_{2}^{j}$, we can obtain convergence rates through elementary algebraic manipulations. Observe that there are three "error" terms in (2.5): $R_{0}^{j}$ captures the stochastic gradient decay with each iteration, $R_{1}^{j}$ captures the mismatch between the true iterate and its noisy estimate, and $R_{2}^{j}$ measures the size of the projection of that mismatch on the gradient at each step.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Perturbed Iterates", "weight": 1.0} -->

The key contribution of our work is to show that 1) this iteration can capture the algorithmic progress of asynchronous algorithms, and 2) the error terms can be bounded to obtain a $\mathcal{O}{({{\log{({1/\epsilon})}}/\epsilon})}$ rate for Hogwild!, and linear rates of convergence for asynchronous SCD and asynchronous sparse SVRG.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Analyzing Hogwild!", "weight": 1.0} -->

In this section, we provide a simple analysis of Hogwild!, the asynchronous implementation of SGM.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Analyzing Hogwild!", "weight": 1.0} -->

where $\mathbf{x} \in {\mathbb{R}}^{d}$, and each $f_{e_{i}}{(\mathbf{x})}$ depends only on the coordinates indexed by the subset $e_{i}$ of $\{ 1,2,\ldots,d\}$. For simplicity we assume that the terms of $f$ are differentiable; our results can be readily extended to non-differentiable $f_{e_{i}}$s.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Analyzing Hogwild!", "weight": 1.0} -->

We refer to the sets $e_{i}$ as *hyperedges* and denote the set of hyperedges by $\mathcal{E}$. We sometimes refer to $f_{e_{i}}$s as the *terms* of $f$. As shown in Fig. 1, the hyperedges induce a bipartite graph between the $n$ terms and the $d$ variables in $\mathbf{x}$, and a conflict graph between the $n$ terms. Let ${\overline{\Delta}}_{\text{C}}$ be the average degree in the conflict graph; that is, the average number of terms that are in conflict with a single term. We assume that ${\overline{\Delta}}_{\text{C}} \geq 1$, otherwise we could decompose the problem into smaller independent sub-problems. As we will see, under our perturbed iterate analysis framework the convergence rate of asynchronous algorithms depends on ${\overline{\Delta}}_{\text{C}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Analyzing Hogwild!", "weight": 1.0} -->

Hogwild! (Alg. 1) is a method to parallelize SGM in the asynchronous setting. It is deployed on multiple cores that have access to shared memory, where the optimization variable $\mathbf{x}$ and the data points that define the $f$ terms are stored. During its execution each core samples uniformly at random a hyperedge $s$ from $\mathcal{E}$. It reads the coordinates $v \in s$ of the shared vector $\mathbf{x}$, evaluates $\nabla f_{s}$ at the point read, and finally adds $- {\gamma{\nabla f_{s}}}$ to the shared variable.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Analyzing Hogwild!", "weight": 1.0} -->

1:while number of sampled hyperedges ≤ T do in parallel
2: sample a random hyperedge s
3: ${\lbrack\hat{\mathbf{x}}\rbrack}_{s}$ = an inconsistent read of the shared variable [x]s
4: ${\lbrack\mathbf{u}\rbrack}_{s} = {- {{\gamma \cdot \mathbf{g}}{({\lbrack\hat{\mathbf{x}}\rbrack}_{s},s)}}}$

<!-- chunk {"id": "body-0020", "role": "body", "section": "Analyzing Hogwild!", "weight": 1.0} -->

During the execution of Hogwild! cores do not synchronize or follow an order between reads or writes. Moreover, they access (i.e., read or write) a set of coordinates in $\mathbf{x}$ without the use of any locking mechanisms that would ensure a conflict-free execution. This implies that the reads/writes of distinct cores can intertwine in arbitrary ways, *e.g.*, while a core updates a subset of variables, before completing its task, other cores can read/write the same subset of variables.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Analyzing Hogwild!", "weight": 1.0} -->

In, the authors analyzed a variant of Hogwild! in which several simplifying assumptions were made. Specifically, in 1) only a single coordinate per sampled hyperedge is updated (*i.e.*, the for loop in Hogwild! is replaced with a single coordinate update); 2) the authors assumed *consistent reads*, i.e., it was assumed that while a core is reading the shared variable, no writes from other cores occur; 3) the authors make an implicit assumption on the uniformity of the processing times of cores (explained in the following), that does not generically hold in practice. These simplifications alleviate some of the challenges in analyzing Hogwild! and allowed the authors to provide a convergence result. As we show in the current paper, however, these simplifications are not necessary to obtain a convergence analysis. Our perturbed iterates framework can be used in an elementary way to analyze the original version of Hogwild!, yielding improved bounds compared to earlier analyses.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Ordering the samples", "weight": 1.0} -->

A subtle but important point in the analysis of Hogwild! is the need to define an order for the sampled hyperedges. A key point of difference of our work is that *we order the samples based on the order in which they were sampled*, not the order in which cores complete the processing of the samples.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Defining read iterates and clarifying independence assumptions", "weight": 1.0} -->

Since the shared memory variable can change inconsistently during reads and writes, we also have to be careful about the notion of iterates in Hogwild!.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The above independence assumption is important when establishing the convergence rate of the algorithm, and has been held explicitly or implicitly in prior work. Specifically, when proving convergence rates for these algorithms we need to show via iterated expectations that ${{\mathbb{E}}\left\langle {{\hat{\mathbf{x}}}_{i} - \mathbf{x}^{\ast}},{g{({\hat{\mathbf{x}}}_{i},s_{i})}} \right\rangle} = \left\langle {{\hat{\mathbf{x}}}_{i} - \mathbf{x}^{\ast}},{\nabla{({\hat{\mathbf{x}}}_{i})}} \right\rangle$, which follows from the independence of ${\hat{\mathbf{x}}}_{i}$ and $s_{i}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

However, observe that although ${\overline{\mathbf{x}}}_{i}$ is independent of $s_{i}$ by construction, this is not the case for the vector ${\hat{\mathbf{x}}}_{i}$ read by the core that sampled $s_{i}$. For example, consider the scenario of two consecutively sampled hyperedges in Alg. 1 that overlap on a subset of coordinates. Then, say one core is reading the coordinates of the shared variables indexed by its hyperedge, while the second core is updating a subset of these coordinates. In this case, the values read by the first core depend on the support of the sampled hyperedge.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

One way to rigorously enforce the independence of ${\hat{\mathbf{x}}}_{i}$ and $s_{i}$ is to require the processors to read the entire shared variable $\mathbf{x}$ before sampling a new hyperedge. However, this might not be reasonable in practice, as the dimension of $\mathbf{x}$ tends to be considerably larger than the sparsity of the hyperedges. As we mentioned earlier, in Appendix A, we show how to overcome the issue of dependence and thereby remove Assumption 1; however, this results in a slightly more cumbersome analysis. To ease readability, in our main text we do adopt Assumption 1.

<!-- chunk {"id": "body-0027", "role": "body", "section": "The perturbed iterates view of asynchrony", "weight": 1.0} -->

In this work, we assume that all writes are atomic, in the sense that they will be successfully recorded in the shared memory at some point. Atomicity is a reasonable assumption in practice, as it can be strictly enforced through compare-and-swap operations.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Every write in line 6 of Alg. 1 will complete successfully.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

This assumption implies that all writes will appear in the shared memory by the end of the execution, in the form of coordinate-wise updates. Due to commutativity the order in which these updates are recorded in the shared memory is irrelevant.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

where $\mathbf{x}_{0}$ is the initial guess and $\mathbf{x}_{i}$ is defined as the vector that contains all gradient updates up to sample $s_{i - 1}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Throughout this section we denote ${\mathbf{g}{(\mathbf{x},s_{j})}} = {{\nabla f_{s_{j}}}{(\mathbf{x})}}$, which we assume to be bounded: ${\|{\mathbf{g}{(\mathbf{x},s)}}\|} \leq M$. Such a uniform bound on the norm of the stochastic gradient is true when operating on a bounded $\ell_{\infty}$ ball; this can in turn be enforced by a simple, coordinate-wise thresholding operator. We can refine our analysis by avoiding the uniform bound on $\|{\mathbf{g}{(\mathbf{x},s)}}\|$, through a simple application of the co-coercivity lemma as it was used; in this case, our derivations would only require a uniform bound on $\|{\mathbf{g}{(\mathbf{x}^{\ast},s)}}\|$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Our subsequent derivations can be adapted to the above, however to keep our derivations elementary we will use the uniform bound on $\|{\mathbf{g}{(\mathbf{x},s)}}\|$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Observe that although a core is only reading the subset of variables that are indexed by its sampled hyperedge, in (3.2) we use the entire vector $\hat{\mathbf{x}}$ as the input to the sampled gradient. We can do this since $\mathbf{g}{({\hat{\mathbf{x}}}_{k},s_{k})}$ is independent of the coordinates of ${\hat{\mathbf{x}}}_{k}$ outside the support of hyperedge $s_{k}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Using the above definitions, we define the perturbed iterates of Hogwild! as

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 2", "weight": 1.0} -->

for $i = {0,1,\ldots,{T - 1}}$, where $s_{i}$ is the $i$-th uniformly sampled hyperedge. Observe that all but the first and last of these iterates are "fake": there might not be an actual time when they exist in the shared memory during the execution. However, $\mathbf{x}_{0}$ is what is stored in memory before the execution starts, and $\mathbf{x}_{T}$ is exactly what is stored in shared memory at the end of the execution.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 2", "weight": 1.0} -->

We observe that the iterates in (3.3) place Hogwild!

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 2", "weight": 1.0} -->

We are only left to bound the three error terms $R_{0}^{j}$, $R_{1}^{j}$, and $R_{2}^{j}$. Before we proceed, we note that for the technical soundness of our theorems, we have to also define a random variable that captures the system randomness. In particular, let $\xi$ denote a random variable that encodes the randomness of the system (i.e., random delays between reads and writes, gradient computation time, etc). Although we do not explicitly use $\xi$, its distribution is required implicitly to compute the expectations for the convergence analysis. This is because the random samples $s_{0},s_{1},\ldots,s_{T - 1}$ do not fully determine the output of Alg. 1. However, $s_{0},\ldots,s_{T - 1}$ along with $\xi$ completely determine the time of all reads and writes. We continue with our final assumption needed by our analysis, that is also needed by prior art.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption 3 (Bounded overlaps)", "weight": 1.0} -->

Two hyperedges $s_{i}$ and $s_{j}$ overlap in time if they are processed concurrently at some point during the execution of Hogwild!. The time during which a hyperedge $s_{i}$ is being processed begins when the sampling function is called and ends after the last coordinate of $\mathbf{g}{({\hat{\mathbf{x}}}_{i},s_{i})}$ is written to the shared memory. We assume that there exists a number $\tau \geq 0$, such that the maximum number of sampled hyperedges that can overlap in time with a particular sampled hyperedge cannot be more than $\tau$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Assumption 3 (Bounded overlaps)", "weight": 1.0} -->

The usefulness of the above assumption is that it essentially abstracts away all system details relative to delays, processing overlaps, and number of cores into a single parameter. Intuitively, $\tau$ can be perceived as a proxy for the number of cores, i.e., we would expect that no more than roughly $O{({\#\text{cores}})}$ sampled hyperedges overlap in time with a single hyperedge, assuming that the processing times across the samples are approximately similar. Observe that if $\tau$ is small, then we expect the distance between $\mathbf{x}_{j}$ and the noisy iterate ${\hat{\mathbf{x}}}_{j}$ to be small. In our perturbed iterate framework, if we set $\tau = 0$, then we obtain the classical iterative formula of serial SGM.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Assumption 3 (Bounded overlaps)", "weight": 1.0} -->

To quantify the distance between ${\hat{\mathbf{x}}}_{j}$ (i.e., the iterate read by the core that sampled $s_{j}$) and $\mathbf{x}_{j}$ (i.e., the "fake" iterate used to establish convergence rates), we observe that any difference between them is caused solely by hyperedges that overlap with $s_{j}$ in time. To see this, let $s_{i}$ be an "earlier" sample, *i.e.*, $i < j$, that does not overlap with $s_{j}$ in time. This implies that the processing of $s_{i}$ finishes before $s_{j}$ starts being processed.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Assumption 3 (Bounded overlaps)", "weight": 1.0} -->

Hence, the full contribution of $\gamma\mathbf{g}{({\hat{\mathbf{x}}}_{i},s_{i})}$ will be recorded in both ${\hat{\mathbf{x}}}_{j}$ and $\mathbf{x}_{j}$ (for the latter this holds by definition). Similarly, if $i > j$ and $s_{i}$ does not overlap with $s_{j}$ in time, then neither ${\hat{\mathbf{x}}}_{j}$ nor $\mathbf{x}_{j}$ (for the latter, again by definition) contain any of the coordinate updates involved in the gradient update $\gamma\mathbf{g}{({\hat{\mathbf{x}}}_{i},s_{i})}$. Assumption 3. ‣ 3.3 The perturbed iterates view of asynchrony ‣ 3 Analyzing Hogwild!

<!-- chunk {"id": "body-0042", "role": "body", "section": "Assumption 3 (Bounded overlaps)", "weight": 1.0} -->

‣ Perturbed Iterate Analysis for Asynchronous Stochastic Optimization") ensures that if $i < {j - \tau}$ or $i > {j + \tau}$, the sample $s_{i}$ does not overlap in time with $s_{j}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Assumption 3 (Bounded overlaps)", "weight": 1.0} -->

By the above discussion, and due to Assumption 3. ‣ 3.3 The perturbed iterates view of asynchrony ‣ 3 Analyzing Hogwild! ‣ Perturbed Iterate Analysis for Asynchronous Stochastic Optimization"), there exist diagonal matrices $\mathbf{S}_{i}^{j}$ with diagonal entries in $\{{- 1},0,1\}$ such that

<!-- chunk {"id": "body-0044", "role": "body", "section": "Assumption 3 (Bounded overlaps)", "weight": 1.0} -->

These diagonal matrices account for any possible pattern of (potentially) partial updates that can occur while hyperedge $s_{j}$ is being processed. We would like to note that the above notation bears resemblance to the coordinate-update mismatch formulation of asynchronous coordinate-based algorithms, as.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Assumption 3 (Bounded overlaps)", "weight": 1.0} -->

We now turn to the convergence proof, emphasizing its elementary nature within the perturbed iterate analysis framework. We begin by bounding the error terms $R_{1}^{j}$ and $R_{2}^{j}$ ($R_{0}^{j}$ is already assumed to be at most $M^{2}$).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Comparison with the original Hogwild! analysis of", "weight": 1.0} -->

Let us summarize the key points of improvement compared to the original Hogwild!

<!-- chunk {"id": "body-0047", "role": "body", "section": "Comparison with the original Hogwild! analysis of", "weight": 1.0} -->

Our analysis is elementary and compact, and follows simply by bounding the $R_{0}^{j},R_{1}^{j}$, and $R_{2}^{j}$ terms, after introducing the perturbed gradient framework of § 2.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Comparison with the original Hogwild! analysis of", "weight": 1.0} -->

We do not assume consistent reads: while a core is reading from the shared memory other cores are allowed to read, or write.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Comparison with the original Hogwild! analysis of", "weight": 1.0} -->

In the authors analyze a simplified version of Hogwild! where for each sampled hyperedge only a randomly selected coordinate is updated. Here we analyze the "full-update" version of Hogwild!.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Comparison with the original Hogwild! analysis of", "weight": 1.0} -->

We order the samples by the order in which they were sampled, not by completion time. This allows to rigorously prove our convergence bounds, without assuming anything on the distribution of the processing time of each hyperedge. This is unlike, where there is an implicit assumption of uniformity with respect to processing times.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Comparison with the original Hogwild! analysis of", "weight": 1.0} -->

The previous work of establishes a nearly-linear speedup for Hogwild! if $\tau$ is bounded as $\tau = {\mathcal{O}\left( \sqrt{n/{\Delta_{\text{R}}\Delta_{\text{L}}^{2}}} \right)}$, where $\Delta_{\text{R}}$ is the maximum right degree of the term-variables bipartite graph, shown in Fig 1, and $\Delta_{\text{L}}$ is the maximum left degree of the same graph. Observe that ${\Delta_{\text{R}} \cdot \Delta_{\text{L}}^{2}} \geq {\Delta_{\text{L}} \cdot \Delta_{\text{C}}}$, where $\Delta_{\text{C}}$ is the maximum degree of the conflict graph.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Comparison with the original Hogwild! analysis of", "weight": 1.0} -->

Here, we obtain a linear speedup for up to $\tau = {\mathcal{O}\left( {\min\left\{ {n/{\overline{\Delta}}_{\text{C}}},{M^{2}/{\epsilonm^{2}}} \right\}} \right)}$, where ${\overline{\Delta}}_{\text{C}}$ is only the average degree of the conflict graph in Fig 1. Our bound on the delays can be orders of magnitude better than that of.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Asynchronous Stochastic Coordinate Descent", "weight": 1.0} -->

In this section, we use the perturbed gradient framework to analyze the convergence of asynchronous parallel stochastic coordinate descent (ASCD). This algorithm has been previously analyzed. We show that the algorithm admits an elementary treatment in our perturbed iterate framework, under the same assumptions made for Hogwild!.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Asynchronous Stochastic Coordinate Descent", "weight": 1.0} -->

1:while iterations ≤ T do in parallel
2: $\hat{\mathbf{x}} =$ an inconsistent read of the shared variable x

<!-- chunk {"id": "body-0055", "role": "body", "section": "Asynchronous Stochastic Coordinate Descent", "weight": 1.0} -->

ASCD, shown in Alg. 2, is a linearly convergent algorithm for minimizing strongly convex functions $f$. At each iteration a core samples one of the coordinates, computes a full gradient update for that coordinate, and proceeds with updating a single element of the shared memory variable $\mathbf{x}$. The challenge in analyzing ASCD, compared to Hogwild!, is that, in order to show linear convergence, we need to show that the error due to the asynchrony between cores decays fast when the iterates arrive close to the optimal solution. The perturbed iterate framework can handle this type of noise analysis in a straightforward manner, using simple recursive bounds.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Asynchronous Stochastic Coordinate Descent", "weight": 1.0} -->

We define ${\hat{\mathbf{x}}}_{i}$ as in the previous section, but now the samples $s_{i}$ are coordinates sampled uniformly at random from $\{ 1,2,\ldots,d\}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Asynchronous Stochastic Coordinate Descent", "weight": 1.0} -->

where $\mathbf{x}_{0}$ is the initial guess, $\mathbf{e}_{s_{j}}$ is the standard basis vector with a one at position $s_{j}$, ${\lbrack{{\nabla f}{(\mathbf{x})}}\rbrack}_{s_{j}}$ denotes the $s_{j}$-th coordinate of the gradient of $f$ computed at $\mathbf{x}$. Similar to Hogwild! in the previous section, ASCD satisfies the following iterative formula

<!-- chunk {"id": "body-0058", "role": "body", "section": "Asynchronous Stochastic Coordinate Descent", "weight": 1.0} -->

Furthermore, by a simple application of the $L$-Lipschitz assumption on $f$, we have a uniform bound on the norm of each computed gradient ${M^{2} ≔ {\max_{0 \leq k \leq T}{{\mathbb{E}}{\|{{\nabla f}{({\hat{\mathbf{x}}}_{k})}}\|}^{2}}} \leq {L^{2}{\hat{a}}_{0}}}.$ Here we assume that the optimization takes place in an $\ell_{\infty}$ ball, so that $M < \infty$. This simply means that the iterates will never have infinitely large coordinate values. This assumption is made in previous work explicitly or implicitly, and in practice it can be implemented easily since the projection on an $\ell_{\infty}$ ball can be done component-wise.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Asynchronous Stochastic Coordinate Descent", "weight": 1.0} -->

Finally, let us define the condition number of $f$ as ${\kappa ≔ {L/m}},$ where $L$ is the Lipschitz constant, and $m$ the strong convexity parameter.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Putting it all together", "weight": 1.0} -->

We can now plug in the upper bounds on $R_{0}^{j}$, $R_{1}^{j}$, and $R_{2}^{j}$ in our perturbed iterate recursive formula

<!-- chunk {"id": "body-0061", "role": "body", "section": "Putting it all together", "weight": 1.0} -->

To guarantee that ASCD follows the same recursion, i.e., it has the same convergence rate as the one implied by Eq. (4.4), we require that ${{{\gammam} - {r{(\gamma)}}} \geq {C{({{\gammam} - {\gamma^{2}dL^{2}}})}}},$ where $C < 1$ is a constant. Solving for $\gamma$ we get

<!-- chunk {"id": "body-0062", "role": "body", "section": "Putting it all together", "weight": 1.0} -->

where $C^{\prime} > 1$ is some absolute constant. For $\gamma = {\mathcal{O}{}\frac{\theta}{d\kappaL}}$, the $\delta{(\gamma)}$ term in the recursive bound becomes

<!-- chunk {"id": "body-0063", "role": "body", "section": "Sparse and Asynchronous SVRG", "weight": 1.0} -->

The SVRG algorithm, presented, is a variance-reduction approach to stochastic gradient descent with strong theoretical guarantees and empirical performance. In this section, we present a parallel, asynchronous and sparse variant of SVRG. We also present a convergence analysis, showing that the analysis proceeds in a nearly identical way to that of ASCD.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Serial Sparse SVRG", "weight": 1.0} -->

where $\mathbf{y}$ is the last iterate of the previous epoch, and as such is updated at the end of every epoch. Here $f$ is of the same form as in (3.1):

<!-- chunk {"id": "body-0065", "role": "body", "section": "Serial Sparse SVRG", "weight": 1.0} -->

and ${\mathbf{g}{(\mathbf{x},s_{j})}} = {{\nabla f_{s_{j}}}{(\mathbf{x})}}$, with hyperedges $s_{j} \in \mathcal{E}$ sampled uniformly at random. As is common in the SVRG literature, we further assume that the individual $f_{e_{i}}$ terms are $L$-smooth. The theoretical innovation in SVRG is having an SGM flavored algorithm, with small amortized cost per iteration, where the variance of the gradient estimate is smaller than that of standard SGM. For a certain selection of learning rate, epoch size, and number of iterations, establishes that SVRG attains a linear rate.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Serial Sparse SVRG", "weight": 1.0} -->

Observe that when optimizing a decomposable $f$ with sparse terms, in contrast to SGM, the SVRG iterates will be dense due to the term ${\nabla f}{(\mathbf{y})}$. From a practical perspective, when the SGM iterates are sparse---the case in several applications ---the cost of writing a sparse update in shared memory is significantly smaller than applying the dense gradient update term ${\nabla f}{(\mathbf{y})}$. Furthermore, these dense updates will cause significantly more memory conflicts in an asynchronous execution, amplifying the error terms in (2.5), and introducing time delays due to memory contention.

<!-- chunk {"id": "body-0067", "role": "body", "section": "KroMagnon: Asynchronous Parallel Sparse SVRG", "weight": 1.0} -->

We now present an asynchronous implementation of sparse SVRG. This implementation, which we refer to as KroMagnon, is given in Algorithm 3.

<!-- chunk {"id": "body-0068", "role": "body", "section": "KroMagnon: Asynchronous Parallel Sparse SVRG", "weight": 1.0} -->

4: while number of sampled hyperedges ≤ S do in parallel
5: sample a random hyperedge s
6: ${\lbrack\hat{\mathbf{x}}\rbrack}_{s}$ = an inconsistent read of the shared variable [x]s

<!-- chunk {"id": "body-0069", "role": "body", "section": "KroMagnon: Asynchronous Parallel Sparse SVRG", "weight": 1.0} -->

To prove the convergence of KroMagnon we follow the line of reasoning presented in the previous section. Most of the arguments used here come from a straightforward generalization of the analysis of ASCD. The main result of this section is given below.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Putting it all together", "weight": 1.0} -->

If we set $\gamma = {\mathcal{O}{}\frac{\theta}{L\kappa}}$, i.e., the same step size as serial sparse SVRG (Theorem 13), then the above becomes

<!-- chunk {"id": "body-0071", "role": "body", "section": "Putting it all together", "weight": 1.0} -->

Therefore, KroMagnon satisfies the recursion

<!-- chunk {"id": "body-0072", "role": "body", "section": "Putting it all together", "weight": 1.0} -->

## data
## features

<!-- chunk {"id": "body-0073", "role": "body", "section": "Empirical Evaluation of KroMagnon", "weight": 1.0} -->

In this section we evaluate KroMagnon empirically. Our two goals are to demonstrate that KroMagnon is faster than dense SVRG, and KroMagnon has speedups comparable to those of Hogwild!. We implemented Hogwild!, asynchronous dense SVRG, and KroMagnon in Scala, and tested them on the problems and datasets listed in Table 1. Each algorithm was run for 50 epochs, using up to 16 threads. For the SVRG algorithms, we recompute $\mathbf{y}$ and the full gradient ${\nabla f}{(\mathbf{y})}$ every two epochs. We normalize the objective values such that the objective at the initial starting point has a value of one, and the minimum attained across all algorithms and epochs has a value of zero. Experiments were conducted on a Linux machine with 2 Intel Xeon Processor E5-2670 (2.60GHz, eight cores each) with 250Gb memory.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Comparison with dense SVRG", "weight": 1.0} -->

We were unable to run dense SVRG on the url and eswiki-2013 datasets due to the large number of features. Figures 3(a), 3(b), and 5(a) show that KroMagnon is one-two orders of magnitude faster than dense SVRG. In fact, running dense SVRG on 16 threads is slower than KroMagnon on a single thread. Moreover, as seen in Fig. 4(a), KroMagnon on 16 threads can be up to four orders of magnitude faster than serial dense SVRG. Both dense SVRG and KroMagnon attain similar optima.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Speedups", "weight": 1.0} -->

We measured the time each algorithm takes to achieve 99.9% and 99.99% of the minimum achieved by that algorithm. Speedups are computed relative to the runtime of the algorithm on a single thread. Although the speedup of KroMagnon varies across datasets, we find that KroMagnon has comparable speedups with Hogwild! on all datasets, as shown in Figure 3(c), 3(d), 4(c), 4(d), 5(c), 5(d). We further observe that dense SVRG has better speedup scaling. This happens because the per iteration complexity of Hogwild! and KroMagnon is significantly cheaper to the extent that the additional overhead associated with having extra threads leads to some speedup loss; this is not the case for dense SVRG as the per iteration cost is higher.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Conclusions and Open Problems", "weight": 1.0} -->

We have introduced a novel framework for analyzing parallel asynchronous stochastic gradient optimization algorithms. The main advantage of our framework is that it is straightforward to apply to a range of first-order stochastic algorithms, while it involves elementary derivations. Moreover, in our analysis we lift, or relax, many of the assumptions made in prior art, *e.g.*, we do not assume consistent reads, and we analyze full stochastic gradient updates. We use our framework to analyze Hogwild! and ASCD, and further introduce and analyze KroMagnon, a new asynchronous sparse SVRG algorithm.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Conclusions and Open Problems", "weight": 1.0} -->

It would be interesting to obtain tighter bounds for the convergence of function values of the algorithms presented. How do the "errors" due to asynchrony influence the convergence rate of function values? In this case the number of iterations required to reach a target accuracy should scale with the condition number of the objective, not its square. Moreover, the literature on stochastic coordinate descent establishes convergence results in terms of coordinate-wise Lipschitz constants---a more refined smoothness quantity than the full-function smoothness. It would be worthwhile to know if our framework can be adapted to take these parameters into account.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Conclusions and Open Problems", "weight": 1.0} -->

Our perturbed iterates framework relies fundamentally on the strong convexity assumption. However, asynchronous algorithms are known to perform well on non-strongly convex (and even nonconvex) objectives. Can we generalize our framework to simply convex, or smooth functions? Under what assumptions, or simple families of functions, can we show convergence for nonconvex problems?

<!-- chunk {"id": "body-0079", "role": "body", "section": "Conclusions and Open Problems", "weight": 1.0} -->

As previously explained, we believe that the upper bounds on $\tau$---the proxy for the number of cores---in our ASCD and KroMagnon analyses are amenable to improvements. It is an open problem to explore the extent of such improvements.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Conclusions and Open Problems", "weight": 1.0} -->

Our analysis offers sensible upper bounds only in the presence of sparsity. It seems, however, that to obtain speedup results for Hogwild!, it is only necessary to have small correlation between randomly sampled gradients. In what practical setups do randomly selected gradients have sufficiently small correlation? Does that immediately imply linear speedups in the same way that update sparsity does?

<!-- chunk {"id": "body-0081", "role": "body", "section": "Conclusions and Open Problems", "weight": 1.0} -->

In this work we analyzed three similar stochastic first-order methods. It is an open problem to apply our framework and provide an elementary analysis for a greater variety of stochastic gradient type optimization algorithms, such as AdaGrad-type schemes (similar to ), or stochastic dual coordinate methods (similar to ).

<!-- chunk {"id": "body-0082", "role": "body", "section": "Conclusions and Open Problems", "weight": 1.0} -->

Capturing the effects of asynchrony as noise on the algorithmic input seems to be applicable to settings beyond stochastic optimization. As shown recently for a combinatorial graph problem, a similar viewpoint enables the analysis of an asynchronous graph clustering algorithm. It is an interesting endeavor to explore the extent to which a perturbed iterate viewpoint is suitable for analyzing general asynchronous iterative algorithms.
