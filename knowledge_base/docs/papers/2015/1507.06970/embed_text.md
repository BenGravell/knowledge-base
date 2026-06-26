## Introduction

Asynchronous parallel stochastic optimization algorithms have recently gained significant traction in algorithmic machine learning. A large body of recent work has demonstrated that near-linear speedups are achievable, in theory and practice, on many common machine learning tasks. Moreover, when these lock-free algorithms are applied to non-convex optimization, significant speedups are still achieved with no loss of statistical accuracy. This behavior has been demonstrated in practice in state-of-the-art deep learning systems such as Google's Downpour SGD and Microsoft's Project Adam.

Although asynchronous stochastic algorithms are simple to implement and enjoy excellent performance in practice, they are challenging to analyze theoretically. The current analyses require lengthy derivations and several assumptions that may not reflect realistic system behavior. Moreover, due to the difficult nature of the proofs, the algorithms analyzed are often simplified versions of those actually run in practice.

In this paper, we propose a general framework for deriving convergence rates for parallel, lock-free, asynchronous first-order stochastic algorithms. We interpret the algorithmic effects of asynchrony as perturbing the stochastic iterates with bounded noise. This interpretation allows us to show how a variety of asynchronous first-order algorithms can be analyzed as their serial counterparts operating on noisy inputs. The advantage of our framework is that it yields elementary convergence proofs, can remove or relax simplifying assumptions adopted in prior art, and can yield improved bounds when compared to earlier work.

We demonstrate the general applicability of our framework by providing new convergence analyses for Hogwild!, *i.e.*, the asynchronous stochastic gradient method (SGM), for asynchronous stochastic coordinate descent (ASCD), and KroMagnon: a novel asynchronous sparse version of the stochastic variance-reduced gradient (SVRG) method. In particular, we provide a modified version of SVRG that allows for sparse updates, we show that this method can be parallelized in the asynchronous model, and we provide convergence guarantees using our framework. Experimentally, the asynchronous, parallel sparse SVRG achieves nearly-linear speedups on a machine with 16 cores and is sometimes four orders of magnitude faster than the standard (dense) SVRG method.

### Related work

The algorithmic tapestry of parallel stochastic optimization is rich and diverse extending back at least to the late 60s. Much of the contemporary work in this space is built upon the foundational work of Bertsekas, Tsitsiklis et al.; the shared memory access model that we are using in this work, is very similar to the partially asynchronous model introduced in the aforementioned manuscripts. Recent advances in parallel and distributed computing technologies have generated renewed interest in the theoretical understanding and practical implementation of parallel stochastic algorithms.

The power of lock-free, asynchronous stochastic optimization on shared-memory multicore systems was first demonstrated in the work of. The authors introduce Hogwild!, a completely lock-free and asynchronous parallel stochastic gradient method (SGM) that exhibits nearly linear speedups for a variety of machine learning tasks. Inspired by Hogwild!, several authors developed lock-free and asynchronous algorithms that move beyond SGM, such as the work of Liu et al. on parallel stochastic coordinate descent. Additional work in first order optimization and beyond, extending to parallel iterative linear solvers, has further shown that linear speedups are possible in the asynchronous shared memory model.

## Perturbed Stochastic Gradients

### Preliminaries and Notation

We study parallel asynchronous iterative algorithms that minimize convex functions $f{(\mathbf{x})}$ with $\mathbf{x} \in {\mathbb{R}}^{d}$. The computational model is the same as that of Niu et al.: a number of cores have access to the same shared memory, and each of them can read and update components of $\mathbf{x}$ in the shared memory. The algorithms that we consider are asynchronous and lock-free: cores do not coordinate their reads or writes, and while a core is reading/writing other cores can update the shared variables in $\mathbf{x}$.

We focus our analysis on functions $f$ that are $L$-smooth and $m$-strongly convex. A function $f$ is $L$-smooth if it is differentiable and has Lipschitz gradients where $\parallel \cdot \parallel$ denotes the Euclidean norm. Strong convexity with parameter $m > 0$ imposes a curvature condition on $f$: Strong convexity implies that $f$ has a unique minimum $\mathbf{x}^{\ast}$ and satisfies In the following, we use $i$, $j$, and $k$ to denote iteration counters, while reserving $v$ and $u$ to denote coordinate indices. We use $\mathcal{O}{}$ to denote absolute constants.

### Perturbed Iterates

A popular way to minimize convex functions is via first-order stochastic algorithms. These algorithms can be described using the following general iterative expression: where $\xi_{j}$ is a random variable independent of $\mathbf{x}_{j}$ and $\mathbf{g}$ is an unbiased estimator of the true gradient of $f$ at $\mathbf{x}_{j}$: ${{\mathbb{E}}_{\xi_{j}}\mathbf{g}{(\mathbf{x}_{j},\xi_{j})}} = {{\nabla f}{(\mathbf{x}_{j})}}$. The success of first-order stochastic techniques partly lies in their computational efficiency: the small computational cost of using noisy gradient estimates trumps the gains of using true gradients.

A major advantage of the iterative formula in (2.1) is that---in combination with strong convexity, and smoothness inequalities---one can easily track algorithmic progress and establish convergence rates to the optimal solution. Unfortunately, the progress of asynchronous parallel algorithms cannot be precisely described or analyzed using the above iterative framework. Processors do not read from memory actual iterates $\mathbf{x}_{j}$, as there is no global clock that synchronizes reads or writes while different cores write/read "stale" variables.

In the subsequent sections, we show that the following simple perturbed variant of Eq. (2.1) can capture the algorithmic progress of asynchronous stochastic algorithms. Consider the following iteration where $\mathbf{n}_{j}$ is a stochastic error term. For simplicity let ${\hat{\mathbf{x}}}_{j} = {\mathbf{x}_{j} + \mathbf{n}_{j}}$. Then, where in the last equation we added and subtracted the term $2\gamma{\langle{\hat{\mathbf{x}}}_{j},{\mathbf{g}{({\hat{\mathbf{x}}}_{j},\xi_{j})}}\rangle}$.

We assume that ${\hat{\mathbf{x}}}_{j}$ and $\xi_{j}$ are independent. However, in contrast to recursion (2.1), we no longer require $\mathbf{x}_{j}$ to be independent of $\xi_{j}$. The importance of the above independence assumption will become clear in the next section.

We now take the expectation of both sides in (2.3). Since ${\hat{\mathbf{x}}}_{j}$ and $\mathbf{x}^{\ast}$ are independent of $\xi_{j}$, we use iterated expectations to obtain ${{{\mathbb{E}}{\langle{{\hat{\mathbf{x}}}_{j} - \mathbf{x}^{\ast}},{\mathbf{g}{({\hat{\mathbf{x}}}_{j},\xi_{j})}}\rangle}} = {{\mathbb{E}}{\langle{{\hat{\mathbf{x}}}_{j} - \mathbf{x}^{\ast}},{{\nabla f}{({\hat{\mathbf{x}}}_{j})}}\rangle}}}.$ Moreover, since $f$ is $m$-strongly convex, we know that where the second inequality is a simple consequence of the triangle inequality. Now, let $a_{j} = {{\mathbb{E}}{\|{\mathbf{x}_{j} - \mathbf{x}^{\ast}}\|}^{2}}$ and substitute (2.4) back into Eq. (2.3) to get The recursive equation (2.5) is key to our analysis. We show that for given $R_{0}^{j}$, $R_{1}^{j}$, and $R_{2}^{j}$, we can obtain convergence rates through elementary algebraic manipulations. Observe that there are three "error" terms in (2.5): $R_{0}^{j}$ captures the stochastic gradient decay with each iteration, $R_{1}^{j}$ captures the mismatch between the true iterate and its noisy estimate, and $R_{2}^{j}$ measures the size of the projection of that mismatch on the gradient at each step. The key contribution of our work is to show that 1) this iteration can capture the algorithmic progress of asynchronous algorithms, and 2) the error terms can be bounded to obtain a $\mathcal{O}{({{\log{({1/\epsilon})}}/\epsilon})}$ rate for Hogwild!, and linear rates of convergence for asynchronous SCD and asynchronous sparse SVRG.

## Analyzing Hogwild!

In this section, we provide a simple analysis of Hogwild!, the asynchronous implementation of SGM. We focus on functions $f$ that are decomposable into $n$ terms: where $\mathbf{x} \in {\mathbb{R}}^{d}$, and each $f_{e_{i}}{(\mathbf{x})}$ depends only on the coordinates indexed by the subset $e_{i}$ of $\{ 1,2,\ldots,d\}$. For simplicity we assume that the terms of $f$ are differentiable; our results can be readily extended to non-differentiable $f_{e_{i}}$s.

We refer to the sets $e_{i}$ as *hyperedges* and denote the set of hyperedges by $\mathcal{E}$. We sometimes refer to $f_{e_{i}}$s as the *terms* of $f$. As shown in Fig. 1, the hyperedges induce a bipartite graph between the $n$ terms and the $d$ variables in $\mathbf{x}$, and a conflict graph between the $n$ terms. Let ${\overline{\Delta}}_{\text{C}}$ be the average degree in the conflict graph; that is, the average number of terms that are in conflict with a single term. We assume that ${\overline{\Delta}}_{\text{C}} \geq 1$, otherwise we could decompose the problem into smaller independent sub-problems. As we will see, under our perturbed iterate analysis framework the convergence rate of asynchronous algorithms depends on ${\overline{\Delta}}_{\text{C}}$.

Figure 1: The bipartite graph on the left has as its leftmost vertices the n function terms and as its rightmost vertices the coordinates of x. A term fei is connected to a coordinate xj if hyperedge ei contains j (i.e., if the i-th term is a function of that coordinate). The graph on the right depicts a conflict graph between the function terms. The vertices denote the function terms, and two terms are joined by an edge if they conflict on at least one coordinate in the bipartite graph.

Hogwild! (Alg. 1) is a method to parallelize SGM in the asynchronous setting. It is deployed on multiple cores that have access to shared memory, where the optimization variable $\mathbf{x}$ and the data points that define the $f$ terms are stored. During its execution each core samples uniformly at random a hyperedge $s$ from $\mathcal{E}$. It reads the coordinates $v \in s$ of the shared vector $\mathbf{x}$, evaluates $\nabla f_{s}$ at the point read, and finally adds $- {\gamma{\nabla f_{s}}}$ to the shared variable.

1:while number of sampled hyperedges ≤ T do in parallel 2: sample a random hyperedge s 3: ${\lbrack\hat{\mathbf{x}}\rbrack}_{s}$ = an inconsistent read of the shared variable [x]s 4: ${\lbrack\mathbf{u}\rbrack}_{s} = {- {{\gamma \cdot \mathbf{g}}{({\lbrack\hat{\mathbf{x}}\rbrack}_{s},s)}}}$ During the execution of Hogwild! cores do not synchronize or follow an order between reads or writes. Moreover, they access (i.e., read or write) a set of coordinates in $\mathbf{x}$ without the use of any locking mechanisms that would ensure a conflict-free execution. This implies that the reads/writes of distinct cores can intertwine in arbitrary ways, *e.g.*, while a core updates a subset of variables, before completing its task, other cores can read/write the same subset of variables.

In, the authors analyzed a variant of Hogwild! in which several simplifying assumptions were made. Specifically, in 1) only a single coordinate per sampled hyperedge is updated (*i.e.*, the for loop in Hogwild! is replaced with a single coordinate update); 2) the authors assumed *consistent reads*, i.e., it was assumed that while a core is reading the shared variable, no writes from other cores occur; 3) the authors make an implicit assumption on the uniformity of the processing times of cores (explained in the following), that does not generically hold in practice. These simplifications alleviate some of the challenges in analyzing Hogwild! and allowed the authors to provide a convergence result. As we show in the current paper, however, these simplifications are not necessary to obtain a convergence analysis. Our perturbed iterates framework can be used in an elementary way to analyze the original version of Hogwild!, yielding improved bounds compared to earlier analyses.

### Ordering the samples

A subtle but important point in the analysis of Hogwild! is the need to define an order for the sampled hyperedges. A key point of difference of our work is that *we order the samples based on the order in which they were sampled*, not the order in which cores complete the processing of the samples.

### Definition 1

We denote by $s_{i}$ the $i$-th sampled hyperedge in a run of Alg. 1.

That is, $s_{i}$ denotes the sample obtained when line $2$ in Alg. 1 is executed for the $i$-th time. This is different from the original work of, in which the samples were ordered according to the completion time of each thread. The issue with such an ordering is that the distribution of the samples, conditioned on the ordering, is not always uniform; for example, hyperedges of small cardinality are more likely to be "early" samples. A uniform distribution is needed for the theoretical analysis of stochastic gradient methods, a point that is disregarded . Our ordering according to sampling time resolves this issue by guaranteeing uniformity among samples in a trivial way.

### Defining read iterates and clarifying independence assumptions

Since the shared memory variable can change inconsistently during reads and writes, we also have to be careful about the notion of iterates in Hogwild!.

### Definition 2

We denote by ${\overline{\mathbf{x}}}_{i}$ the contents of the shared memory before the $i$-th execution of line $2$. Moreover, we denote by ${\hat{\mathbf{x}}}_{i} \in {\mathbb{R}}^{d}$ the vector, that in coordinates $v \in s_{i}$ contains exactly what the core that sampled $s_{i}$ read. We then define ${\lbrack{\hat{\mathbf{x}}}_{i}\rbrack}_{v} = {\lbrack{\overline{\mathbf{x}}}_{i}\rbrack}_{v}$ for all $v \notin s_{i}$. Note that we do not assume consistent reads, *i.e.*, the contents of the shared memory can potentially change while a core is reading.

At this point we would like to briefly discuss an independence assumption held by all prior work. In the following paragraph, we explain why this assumption is not always true in practice. In Appendix A, we show how to lift such independence assumption, but for ease of exposition we do adopt it in our main text.

### Assumption 1

The vector ${\hat{\mathbf{x}}}_{i}$ is independent of the sampled hyperedge $s_{i}$.

The above independence assumption is important when establishing the convergence rate of the algorithm, and has been held explicitly or implicitly in prior work. Specifically, when proving convergence rates for these algorithms we need to show via iterated expectations that ${{\mathbb{E}}\left\langle {{\hat{\mathbf{x}}}_{i} - \mathbf{x}^{\ast}},{g{({\hat{\mathbf{x}}}_{i},s_{i})}} \right\rangle} = \left\langle {{\hat{\mathbf{x}}}_{i} - \mathbf{x}^{\ast}},{\nabla{({\hat{\mathbf{x}}}_{i})}} \right\rangle$, which follows from the independence of ${\hat{\mathbf{x}}}_{i}$ and $s_{i}$. However, observe that although ${\overline{\mathbf{x}}}_{i}$ is independent of $s_{i}$ by construction, this is not the case for the vector ${\hat{\mathbf{x}}}_{i}$ read by the core that sampled $s_{i}$. For example, consider the scenario of two consecutively sampled hyperedges in Alg. 1 that overlap on a subset of coordinates. Then, say one core is reading the coordinates of the shared variables indexed by its hyperedge, while the second core is updating a subset of these coordinates. In this case, the values read by the first core depend on the support of the sampled hyperedge.

One way to rigorously enforce the independence of ${\hat{\mathbf{x}}}_{i}$ and $s_{i}$ is to require the processors to read the entire shared variable $\mathbf{x}$ before sampling a new hyperedge. However, this might not be reasonable in practice, as the dimension of $\mathbf{x}$ tends to be considerably larger than the sparsity of the hyperedges. As we mentioned earlier, in Appendix A, we show how to overcome the issue of dependence and thereby remove Assumption 1; however, this results in a slightly more cumbersome analysis. To ease readability, in our main text we do adopt Assumption 1.

### The perturbed iterates view of asynchrony

In this work, we assume that all writes are atomic, in the sense that they will be successfully recorded in the shared memory at some point. Atomicity is a reasonable assumption in practice, as it can be strictly enforced through compare-and-swap operations.

### Assumption 2

Every write in line 6 of Alg. 1 will complete successfully.

This assumption implies that all writes will appear in the shared memory by the end of the execution, in the form of coordinate-wise updates. Due to commutativity the order in which these updates are recorded in the shared memory is irrelevant. Hence, after processing a total of $T$ hyperedges the shared memory contains: where $\mathbf{x}_{0}$ is the initial guess and $\mathbf{x}_{i}$ is defined as the vector that contains all gradient updates up to sample $s_{i - 1}$.

### Remark 1

Throughout this section we denote ${\mathbf{g}{(\mathbf{x},s_{j})}} = {{\nabla f_{s_{j}}}{(\mathbf{x})}}$, which we assume to be bounded: ${\|{\mathbf{g}{(\mathbf{x},s)}}\|} \leq M$. Such a uniform bound on the norm of the stochastic gradient is true when operating on a bounded $\ell_{\infty}$ ball; this can in turn be enforced by a simple, coordinate-wise thresholding operator. We can refine our analysis by avoiding the uniform bound on $\|{\mathbf{g}{(\mathbf{x},s)}}\|$, through a simple application of the co-coercivity lemma as it was used ; in this case, our derivations would only require a uniform bound on $\|{\mathbf{g}{(\mathbf{x}^{\ast},s)}}\|$. Our subsequent derivations can be adapted to the above, however to keep our derivations elementary we will use the uniform bound on $\|{\mathbf{g}{(\mathbf{x},s)}}\|$.

### Remark 2

Observe that although a core is only reading the subset of variables that are indexed by its sampled hyperedge, in (3.2) we use the entire vector $\hat{\mathbf{x}}$ as the input to the sampled gradient. We can do this since $\mathbf{g}{({\hat{\mathbf{x}}}_{k},s_{k})}$ is independent of the coordinates of ${\hat{\mathbf{x}}}_{k}$ outside the support of hyperedge $s_{k}$.

Using the above definitions, we define the perturbed iterates of Hogwild! as for $i = {0,1,\ldots,{T - 1}}$, where $s_{i}$ is the $i$-th uniformly sampled hyperedge. Observe that all but the first and last of these iterates are "fake": there might not be an actual time when they exist in the shared memory during the execution. However, $\mathbf{x}_{0}$ is what is stored in memory before the execution starts, and $\mathbf{x}_{T}$ is exactly what is stored in shared memory at the end of the execution.

We observe that the iterates in (3.3) place Hogwild! in the perturbed gradient framework introduced in §2: We are only left to bound the three error terms $R_{0}^{j}$, $R_{1}^{j}$, and $R_{2}^{j}$. Before we proceed, we note that for the technical soundness of our theorems, we have to also define a random variable that captures the system randomness. In particular, let $\xi$ denote a random variable that encodes the randomness of the system (i.e., random delays between reads and writes, gradient computation time, etc). Although we do not explicitly use $\xi$, its distribution is required implicitly to compute the expectations for the convergence analysis. This is because the random samples $s_{0},s_{1},\ldots,s_{T - 1}$ do not fully determine the output of Alg. 1. However, $s_{0},\ldots,s_{T - 1}$ along with $\xi$ completely determine the time of all reads and writes. We continue with our final assumption needed by our analysis, that is also needed by prior art.

### Assumption 3 (Bounded overlaps)

Two hyperedges $s_{i}$ and $s_{j}$ overlap in time if they are processed concurrently at some point during the execution of Hogwild!. The time during which a hyperedge $s_{i}$ is being processed begins when the sampling function is called and ends after the last coordinate of $\mathbf{g}{({\hat{\mathbf{x}}}_{i},s_{i})}$ is written to the shared memory. We assume that there exists a number $\tau \geq 0$, such that the maximum number of sampled hyperedges that can overlap in time with a particular sampled hyperedge cannot be more than $\tau$.

The usefulness of the above assumption is that it essentially abstracts away all system details relative to delays, processing overlaps, and number of cores into a single parameter. Intuitively, $\tau$ can be perceived as a proxy for the number of cores, i.e., we would expect that no more than roughly $O{({\#\text{cores}})}$ sampled hyperedges overlap in time with a single hyperedge, assuming that the processing times across the samples are approximately similar. Observe that if $\tau$ is small, then we expect the distance between $\mathbf{x}_{j}$ and the noisy iterate ${\hat{\mathbf{x}}}_{j}$ to be small. In our perturbed iterate framework, if we set $\tau = 0$, then we obtain the classical iterative formula of serial SGM.

To quantify the distance between ${\hat{\mathbf{x}}}_{j}$ (i.e., the iterate read by the core that sampled $s_{j}$) and $\mathbf{x}_{j}$ (i.e., the "fake" iterate used to establish convergence rates), we observe that any difference between them is caused solely by hyperedges that overlap with $s_{j}$ in time. To see this, let $s_{i}$ be an "earlier" sample, *i.e.*, $i < j$, that does not overlap with $s_{j}$ in time. This implies that the processing of $s_{i}$ finishes before $s_{j}$ starts being processed. Hence, the full contribution of $\gamma\mathbf{g}{({\hat{\mathbf{x}}}_{i},s_{i})}$ will be recorded in both ${\hat{\mathbf{x}}}_{j}$ and $\mathbf{x}_{j}$ (for the latter this holds by definition). Similarly, if $i > j$ and $s_{i}$ does not overlap with $s_{j}$ in time, then neither ${\hat{\mathbf{x}}}_{j}$ nor $\mathbf{x}_{j}$ (for the latter, again by definition) contain any of the coordinate updates involved in the gradient update $\gamma\mathbf{g}{({\hat{\mathbf{x}}}_{i},s_{i})}$. Assumption 3. ‣ 3.3 The perturbed iterates view of asynchrony ‣ 3 Analyzing Hogwild! ‣ Perturbed Iterate Analysis for Asynchronous Stochastic Optimization") ensures that if $i < {j - \tau}$ or $i > {j + \tau}$, the sample $s_{i}$ does not overlap in time with $s_{j}$.

By the above discussion, and due to Assumption 3. ‣ 3.3 The perturbed iterates view of asynchrony ‣ 3 Analyzing Hogwild! ‣ Perturbed Iterate Analysis for Asynchronous Stochastic Optimization"), there exist diagonal matrices $\mathbf{S}_{i}^{j}$ with diagonal entries in $\{{- 1},0,1\}$ such that These diagonal matrices account for any possible pattern of (potentially) partial updates that can occur while hyperedge $s_{j}$ is being processed. We would like to note that the above notation bears resemblance to the coordinate-update mismatch formulation of asynchronous coordinate-based algorithms, as.

We now turn to the convergence proof, emphasizing its elementary nature within the perturbed iterate analysis framework. We begin by bounding the error terms $R_{1}^{j}$ and $R_{2}^{j}$ ($R_{0}^{j}$ is already assumed to be at most $M^{2}$).

### Lemma 3

Hogwild! satisfies the recursion in (2.5) with where ${\overline{\Delta}}_{\text{C}}$ is the average degree of the conflict graph between the hyperedges.

### Proof

The norm of the mismatch can be bounded in the following way: since $\mathbf{S}_{i}^{j}$ are diagonal sign matrices and since the steps $\mathbf{g}{({\hat{\mathbf{x}}}_{i},s_{i})}$ are supported on the samples $s_{i}$. We use the upper bound ${\|{\mathbf{g}{({\hat{\mathbf{x}}}_{i},s_{i})}}\|} \leq M$ to obtain The last step follows because two sampled hyperedges (sampled with replacement) intersect with probability at most $2\frac{{\overline{\Delta}}_{\text{C}}}{n}$. We can bound $R_{2}^{j}$ in a similar way: Plugging the bounds of Lemma 3 in our recursive formula, we see that Hogwild! satisfies the recursion On the other hand, serial SGM satisfies the recursion ${a_{j + 1} \leq {{\left({1 - {\gammam}} \right)a_{j}} + {\gamma^{2}M^{2}}}}.$ If the step size is set to $\gamma = \frac{\epsilonm}{2M^{2}}$, it attains target accuracy $\epsilon$ in $T \geq {{{2M^{2}}/{({\epsilonm^{2}})}}{\log\left(\frac{2a_{0}}{\epsilon} \right)}}$ iterations. Hence, when the term $\delta$ of (3.5) is order-wise constant, Hogwild! satisfies the same recursion (up to constants) as serial SGM. This directly implies the main result of this section.

### Theorem 4

If the number of samples that overlap in time with a single sample during the execution of Hogwild! is bounded as Hogwild!, with step size $\gamma = \frac{\epsilonm}{2M^{2}}$, reaches an accuracy of ${{\mathbb{E}}{\|{\mathbf{x}_{k} - \mathbf{x}^{\ast}}\|}^{2}} \leq \epsilon$ after Since the iteration bound in the theorem is (up to a constant) the same as that of serial SGM, our result implies a linear speedup. We would like to note that an improved rate of $O{({1/\epsilon})}$ can be obtained by appropriately diminishing stepsizes per epoch (see, *e.g.*,). Furthermore, observe that although the $\frac{M^{2}}{\epsilonm^{2}}$ bound on $\tau$ might seem restrictive, it is---up to a logarithmic factor---proportional to the total number of iterations required by Hogwild! (or even serial SGM) to reach $\epsilon$ accuracy. Assuming that the average degree of the conflict graph is constant, and that we perform a constant number of passes over the data, *i.e.*, $T = {c \cdot n}$, then $\tau$ can be as large as $\overset{\sim}{\mathcal{O}}{(n)}$, *i.e.*, nearly linear in the number of function terms.^11^1$\overset{\sim}{\mathcal{O}}$ hides logarithmic terms.

### Comparison with the original Hogwild! analysis of

Let us summarize the key points of improvement compared to the original Hogwild! analysis: Our analysis is elementary and compact, and follows simply by bounding the $R_{0}^{j},R_{1}^{j}$, and $R_{2}^{j}$ terms, after introducing the perturbed gradient framework of § 2.

We do not assume consistent reads: while a core is reading from the shared memory other cores are allowed to read, or write.

In the authors analyze a simplified version of Hogwild! where for each sampled hyperedge only a randomly selected coordinate is updated. Here we analyze the "full-update" version of Hogwild!.

We order the samples by the order in which they were sampled, not by completion time. This allows to rigorously prove our convergence bounds, without assuming anything on the distribution of the processing time of each hyperedge. This is unlike, where there is an implicit assumption of uniformity with respect to processing times.

The previous work of establishes a nearly-linear speedup for Hogwild! if $\tau$ is bounded as $\tau = {\mathcal{O}\left( \sqrt{n/{\Delta_{\text{R}}\Delta_{\text{L}}^{2}}} \right)}$, where $\Delta_{\text{R}}$ is the maximum right degree of the term-variables bipartite graph, shown in Fig 1, and $\Delta_{\text{L}}$ is the maximum left degree of the same graph. Observe that ${\Delta_{\text{R}} \cdot \Delta_{\text{L}}^{2}} \geq {\Delta_{\text{L}} \cdot \Delta_{\text{C}}}$, where $\Delta_{\text{C}}$ is the maximum degree of the conflict graph. Here, we obtain a linear speedup for up to $\tau = {\mathcal{O}\left( {\min\left\{ {n/{\overline{\Delta}}_{\text{C}}},{M^{2}/{\epsilonm^{2}}} \right\}} \right)}$, where ${\overline{\Delta}}_{\text{C}}$ is only the average degree of the conflict graph in Fig 1. Our bound on the delays can be orders of magnitude better than that of.

## Asynchronous Stochastic Coordinate Descent

In this section, we use the perturbed gradient framework to analyze the convergence of asynchronous parallel stochastic coordinate descent (ASCD). This algorithm has been previously analyzed . We show that the algorithm admits an elementary treatment in our perturbed iterate framework, under the same assumptions made for Hogwild!.

1:while iterations ≤ T do in parallel 2: $\hat{\mathbf{x}} =$ an inconsistent read of the shared variable x ASCD, shown in Alg. 2, is a linearly convergent algorithm for minimizing strongly convex functions $f$. At each iteration a core samples one of the coordinates, computes a full gradient update for that coordinate, and proceeds with updating a single element of the shared memory variable $\mathbf{x}$. The challenge in analyzing ASCD, compared to Hogwild!, is that, in order to show linear convergence, we need to show that the error due to the asynchrony between cores decays fast when the iterates arrive close to the optimal solution. The perturbed iterate framework can handle this type of noise analysis in a straightforward manner, using simple recursive bounds.

We define ${\hat{\mathbf{x}}}_{i}$ as in the previous section, but now the samples $s_{i}$ are coordinates sampled uniformly at random from $\{ 1,2,\ldots,d\}$. After $T$ samples have been processed completely, the following vector is contained in shared memory: where $\mathbf{x}_{0}$ is the initial guess, $\mathbf{e}_{s_{j}}$ is the standard basis vector with a one at position $s_{j}$, ${\lbrack{{\nabla f}{(\mathbf{x})}}\rbrack}_{s_{j}}$ denotes the $s_{j}$-th coordinate of the gradient of $f$ computed at $\mathbf{x}$. Similar to Hogwild! in the previous section, ASCD satisfies the following iterative formula Notice that ${{\mathbb{E}}_{s_{j}}\mathbf{g}{({\hat{\mathbf{x}}}_{j},s_{j})}} = {{\nabla f}{({\hat{\mathbf{x}}}_{j})}}$, and thus, similarly to Hogwild!, ASCD's iterates $a_{j} = {{\mathbb{E}}{\|{\mathbf{x}_{j} - \mathbf{x}^{\ast}}\|}^{2}}$ satisfy the recursion of Eq. (2.5): Before stating the main result of this section, let us introduce some further notation. Let us define the largest distance between the optimal vector, and the vector read by the cores during the execution of the algorithm:${{\hat{a}}_{0} ≔ {\max_{0 \leq k \leq T}{{\mathbb{E}}{\|{{\hat{\mathbf{x}}}_{k} - \mathbf{x}^{\ast}}\|}^{2}}}},$ a value which should be thought of as proportional to $a_{0} = {{\mathbb{E}}{\|{\mathbf{x}_{0} - \mathbf{x}^{\ast}}\|}^{2}}$. Furthermore, by a simple application of the $L$-Lipschitz assumption on $f$, we have a uniform bound on the norm of each computed gradient ${M^{2} ≔ {\max_{0 \leq k \leq T}{{\mathbb{E}}{\|{{\nabla f}{({\hat{\mathbf{x}}}_{k})}}\|}^{2}}} \leq {L^{2}{\hat{a}}_{0}}}.$ Here we assume that the optimization takes place in an $\ell_{\infty}$ ball, so that $M < \infty$. This simply means that the iterates will never have infinitely large coordinate values. This assumption is made in previous work explicitly or implicitly, and in practice it can be implemented easily since the projection on an $\ell_{\infty}$ ball can be done component-wise. Finally, let us define the condition number of $f$ as ${\kappa ≔ {L/m}},$ where $L$ is the Lipschitz constant, and $m$ the strong convexity parameter.

### Theorem 5

Let the maximum number of coordinates that can be concurrently processed while a core is processing a single coordinate be at most Then, ASCD with step-size $\gamma = \frac{\mathcal{O}{}}{dL\kappa}$ achieves an error ${{\mathbb{E}}{\|{\mathbf{x}_{k} - \mathbf{x}^{\ast}}\|}^{2}} \leq \epsilon$ after Using the recursive inequality (2.5), serial SCD with the same step-size as in the above theorem, can be shown to achieve the same accuracy as ASCD in the same number of steps. Hence, as long as the proxy for the number of cores is bounded as $\tau = \mathcal{O}{(\min{\{\kappa\sqrt{d}\log{({{\hat{a}}_{0}/\epsilon})}^{- 1},\sqrt{d}\}})}$, our theorem implies a linear speedup with respect to this simple convergence bound. We would like to note, however, that the coordinate descent literature sometimes uses more refined properties of the function to be optimized that can lead to potentially better convergence bounds, especially in terms of function value accuracy, i.e., ${f{(\mathbf{x}_{k})}} - {f{(\mathbf{x}^{\ast})}}$ (see e.g.,).

We would further like to remark that between the two bounds on $\tau$, the second one, i.e., $\mathcal{O}{(\sqrt{d})}$, is the more restrictive, as the first one is proportional---up to log factors---to the square root of the number of iterations, which is usually $\Omega{(d)}$. We explain in our subsequent derivation how this loose bound can be improved, but leave the tightness of the bound as an open question for future work.

### Proof of Theorem 5

The analysis here is slightly more involved compared to Hogwild!.The main technical bottleneck is to relate the decay of $R_{0}^{j}$ with that of $R_{1}^{j}$, and then to exploit the sparsity of the updates for bounding $R_{2}^{j}$.

We start with a simple upper bound on the norm of the gradient updates. From the $L$-Lipschitz assumption on ${\nabla f}{(\mathbf{x})}$, we have where the last inequality is due to Jensen's inequality. This yields the following result.

### Lemma 6

For any $k$ and $j$ we have ${{{\mathbb{E}}\left\| {\mathbf{g}{({\hat{\mathbf{x}}}_{k},s_{k})}} \right\|^{2}} \leq {2dL^{2}\left({a_{j} + {{\mathbb{E}}{\|{\mathbf{x}_{j} - {\hat{\mathbf{x}}}_{k}}\|}^{2}}} \right)}}.$ Let $T$ be the total number of ASCD iterations, and let us define the set which has cardinality at most ${2r\tau} + 1$ and contains all indices around $j$ within $r\tau$ steps, as sketched in Fig. 2.

Figure 2: The set 𝒮rj = {max {j − r τ, 0}, …, j − 1, j, j + 1, …, min {j + r τ, T}} comprises the indices around j (including j) within r τ steps. The cardinality of such a set is 2 r τ + 1. Here, 𝒮0j = {j}.

Due to Assumption 3. ‣ 3.3 The perturbed iterates view of asynchrony ‣ 3 Analyzing Hogwild! ‣ Perturbed Iterate Analysis for Asynchronous Stochastic Optimization"), and similar to, there exist variables $\sigma_{i,k}^{j} \in {\{{- 1},0,1\}}$ such that, for any index $k$ in the set $\mathcal{S}_{r}^{j}$, we have The above equation implies that the difference between a "fake" iterate at time $j$ and the value that was read at time $k$ can be expressed as a linear combination of any coordinate updates that occurred during the time interval defined by $\mathcal{S}_{r + 1}^{j}$.

From Eq. (4.1) we see that $\|{{\hat{\mathbf{x}}}_{k} - \mathbf{x}_{j}}\|$, for any $k \in \mathcal{S}_{r}^{j}$, can be upper bounded in terms of the magnitude of the coordinate updates that occur in $\mathcal{S}_{r + 1}^{j}$. Since these updates are coordinates of the true gradient, we can use their norm to bound the size of ${\hat{\mathbf{x}}}_{k} - \mathbf{x}_{j}$. This will be useful towards bounding $R_{1}^{j}$. Moreover, Lemma 6 shows that the magnitude of the gradient steps can be upper bounded in terms of the size of the mismatches. This will in turn be useful in bounding $R_{0}^{j}$. The above observations are fundamental to our approach. The following lemma makes the above ideas explicit.

### Lemma 7

For any $j \in {\{ 0,\ldots,T\}}$, we have

### Proof

The first inequality is a consequence of Lemma 6. For the second, as mentioned previously, we have ${{\hat{\mathbf{x}}}_{k} - \mathbf{x}_{j}} = {\sum_{i \in \mathcal{S}_{r + 1}^{j}}{\sigma_{i,k}\gamma\mathbf{g}{({\hat{\mathbf{x}}}_{i},s_{i})}}}$ when $k \in \mathcal{S}_{r}^{j}$. Hence, where the first inequality follows due to Jensen's inequality, and the last inequality uses the bound ${|S_{r + 1}^{j}|} \leq {{2{({r + 1})}\tau} + 1} \leq {3\tau{({r + 1})}}$. ∎

### Remark 3

The $\tau^{2}$ factor in the upper bound on $\max{{\mathbb{E}}{\|{{\hat{\mathbf{x}}}_{k} - \mathbf{x}_{j}}\|}^{2}}$ in Lemma 7 might be loose. We believe that it should instead be $\tau$, when $\tau$ is smaller than some measure of the sparsity. If the sparsity of the steps $\mathbf{g}{({\hat{\mathbf{x}}}_{i},s_{i})}$ can be exploited, we suspect that the condition $\tau = {\mathcal{O}{(\sqrt{d})}}$ in Theorem 5 could be improved to $\tau = {\mathcal{O}{(\sqrt{d})}}$.

Let us now define for simplicity ${G_{r} = {\max_{k \in \mathcal{S}_{r}^{j}}{{\mathbb{E}}{\|{\mathbf{g}{({\hat{\mathbf{x}}}_{k},s_{k})}}\|}^{2}\text{~and~}\Delta_{r}}} = {\max_{k \in \mathcal{S}_{r}^{j}}{{\mathbb{E}}{\|{{\hat{\mathbf{x}}}_{k} - \mathbf{x}_{j}}\|}^{2}}}}.$ Observe that that all gradient norms can be bounded as a property that we will use in our bounds. Observe that $R_{0}^{j} = {{\mathbb{E}}{\|{\mathbf{g}{({\hat{\mathbf{x}}}_{j},s_{j})}}\|}^{2}} = G_{0}$ and $R_{1}^{j} = {{\mathbb{E}}{\|{{\hat{\mathbf{x}}}_{j} - \mathbf{x}_{j}}\|}^{2}} = \Delta_{0}$. To obtain bounds for our first two error terms, $R_{0}^{j}$ and $R_{1}^{j}$, we will expand the recursive relations that are implied by Lemma 7. As shown in § B.1 of the Appendix, we obtain the following bounds.

### Lemma 8

Let $\tau \leq \frac{\kappa\sqrt{d}}{\ell}$ and set $\gamma = \frac{\theta}{6dL\kappa}$, for any $\theta \leq 1$ and $\ell \geq 1$. Then, The Cauchy-Schwartz inequality implies the bound $R_{2}^{j} \leq \sqrt{R_{0}^{j}R_{1}^{j}}$. Unfortunately this approach yields a result that can only guarantee convergence up to a factor of $\sqrt{d}$ slower than serial SCD. This happens because upper bounding the inner product $\langle{{\hat{\mathbf{x}}}_{j} - \mathbf{x}_{j}},{\mathbf{g}{({\hat{\mathbf{x}}}_{j},s_{j})}}\rangle$ by ${\|{{\hat{\mathbf{x}}}_{j} - \mathbf{x}_{j}}\|}{\|{\mathbf{g}{({\hat{\mathbf{x}}}_{j},s_{j})}}\|}$ disregards the extreme sparsity of $\mathbf{g}{({\hat{\mathbf{x}}}_{j},s_{j})}$. The next lemma uses a slightly more involved argument to bound $R_{2}^{j}$ exploiting the sparsity of the gradient update. The proof can be found in Appendix B.1.

### Lemma 9

Let $\tau \leq \frac{\kappa\sqrt{d}}{\ell}$ and $\tau = {\mathcal{O}{(\sqrt{d})}}$. Then, ${R_{2}^{j} \leq {\mathcal{O}{}\left( {{\thetama_{j}} + {\theta^{2\ell}\frac{M^{2}}{L\kappa}}} \right)}}.$

### Putting it all together

We can now plug in the upper bounds on $R_{0}^{j}$, $R_{1}^{j}$, and $R_{2}^{j}$ in our perturbed iterate recursive formula to find that ASCD satisfies Observe that in the serial case of SCD the errors $R_{1}^{j}$ and $R_{2}^{j}$ are zero, and $R_{0}^{j} = {{\mathbb{E}}{\|{g{(\mathbf{x}_{j},s_{j})}}\|}^{2}}$. By applying the Lipschitz assumption on $f$, we get ${{\mathbb{E}}{\|{g{(\mathbf{x}_{j},s_{j})}}\|}^{2}} \leq {dL^{2}a_{j}}$, and obtain the simple recursive formula To guarantee that ASCD follows the same recursion, i.e., it has the same convergence rate as the one implied by Eq. (4.4), we require that ${{{\gammam} - {r{(\gamma)}}} \geq {C{({{\gammam} - {\gamma^{2}dL^{2}}})}}},$ where $C < 1$ is a constant. Solving for $\gamma$ we get where $C' > 1$ is some absolute constant. For $\gamma = {\mathcal{O}{}\frac{\theta}{d\kappaL}}$, the $\delta{(\gamma)}$ term in the recursive bound becomes where we used the inequality $M^{2} \leq {L^{2}{\hat{a}}_{0}}$. Hence, ASCD satisfies Let us set $\theta$ to be a sufficiently small constant so that ${\mathcal{O}{}\frac{\theta}{d\kappa^{2}}} = \frac{1}{d\kappa^{2}}$ and solve for $\ell$ such that ${\mathcal{O}{}\theta^{2\ell}{\hat{a}}_{0}} = {\epsilon/2}$. This gives ${\ell = {\mathcal{O}{}{\log\left({{\hat{a}}_{0}/\epsilon} \right)}}}.$ Our main theorem for ASCD now follows from solving ${\left({1 - {{\mathcal{O}}/{d\kappa^{2}}}} \right)^{j + 1}a_{0}} = {\epsilon/2}$ for $j$.

## Sparse and Asynchronous SVRG

The SVRG algorithm, presented , is a variance-reduction approach to stochastic gradient descent with strong theoretical guarantees and empirical performance. In this section, we present a parallel, asynchronous and sparse variant of SVRG. We also present a convergence analysis, showing that the analysis proceeds in a nearly identical way to that of ASCD.

### Serial Sparse SVRG

The original SVRG algorithm of runs for a number of epochs; the per epoch iteration is given as follows: where $\mathbf{y}$ is the last iterate of the previous epoch, and as such is updated at the end of every epoch. Here $f$ is of the same form as in (3.1): and ${\mathbf{g}{(\mathbf{x},s_{j})}} = {{\nabla f_{s_{j}}}{(\mathbf{x})}}$, with hyperedges $s_{j} \in \mathcal{E}$ sampled uniformly at random. As is common in the SVRG literature, we further assume that the individual $f_{e_{i}}$ terms are $L$-smooth. The theoretical innovation in SVRG is having an SGM flavored algorithm, with small amortized cost per iteration, where the variance of the gradient estimate is smaller than that of standard SGM. For a certain selection of learning rate, epoch size, and number of iterations, establishes that SVRG attains a linear rate.

Observe that when optimizing a decomposable $f$ with sparse terms, in contrast to SGM, the SVRG iterates will be dense due to the term ${\nabla f}{(\mathbf{y})}$. From a practical perspective, when the SGM iterates are sparse---the case in several applications ---the cost of writing a sparse update in shared memory is significantly smaller than applying the dense gradient update term ${\nabla f}{(\mathbf{y})}$. Furthermore, these dense updates will cause significantly more memory conflicts in an asynchronous execution, amplifying the error terms in (2.5), and introducing time delays due to memory contention.

A sparse version of SVRG can be obtained by letting the support of the update be determined by that of $\mathbf{g}{(\mathbf{y},s_{j})}$: where $\mathbf{D}_{s_{j}} = {\mathbf{P}_{s_{j}}\mathbf{D}}$, and $\mathbf{P}_{s_{j}}$ is the projection on the support of $s_{j}$ and $\mathbf{D} = {{diag}\left(p_{1}^{- 1},\ldots,p_{d}^{- 1} \right)}$ is a $d \times d$ diagonal matrix. The weight $p_{v}$ is equal to the probability that index $v$ belongs to a hyperedge sampled uniformly at random from $\mathcal{E}$. These probabilities can be computed from the right degrees of the bipartite graph shown in Fig. 1. The normalization ensures that ${{\mathbb{E}}_{s_{j}}\mathbf{D}_{s_{j}}{\nabla f}{(\mathbf{y})}} = {{\nabla f}{(\mathbf{y})}}$ and thus that ${{\mathbb{E}}\mathbf{v}_{j}} = {{\nabla f}{(\mathbf{x}_{j})}}$. We will establish the same upper bound on ${\mathbb{E}}{\|\mathbf{v}_{j}\|}^{2}$ for sparse SVRG as the one used in to establish a linear rate of convergence for dense SVRG. As before we assume that there exists a uniform bound $M > 0$ such that ${\|\mathbf{v}_{j}\|} \leq M$.

### Lemma 10

The variance of the serial sparse SVRG procedure in (5.2) satisfies

### Proof

By definition $\mathbf{v}_{j} = {{{\mathbf{g}{(\mathbf{x}_{j},s_{j})}} - {\mathbf{g}{(\mathbf{y},s_{j})}}} + {\mathbf{D}_{s_{j}}{\nabla f}{(\mathbf{y})}}}$. Therefore We expand the second term to find that Since $\mathbf{g}{(\mathbf{x},s_{j})}$ is supported on $s_{j}$ for all $\mathbf{x}$, we have where the second equality follows by the property of iterated expectations. The conclusion follows because ${{\mathbb{E}}{\|{\mathbf{D}_{s_{j}}{\nabla f}{(\mathbf{y})}}\|}^{2}} = {{\nabla f}{(\mathbf{y})}^{\top}\mathbf{D}{\nabla f}{(\mathbf{y})}}$. ∎ Observe that the last term in the variance bound is a non-negative quadratic form, hence we can drop it and obtain the same variance bound as the one obtained in for dense SVRG. This directly leads to the following corollary.

### Corollary 11

Sparse SVRG admits the same convergence rate upper bound as that of the SVRG of.

We note that usually the convergence rates for SVRG are obtained for function value differences. However, since our perturbed iterate framework of § 2 is based on iterate differences, we re-derive a convergence bound for iterates.

### Lemma 12

Let the step size be $\gamma = \frac{1}{4L\kappa}$ and the length of an epoch be $8\kappa^{2}$. Then, ${{{\mathbb{E}}{\|{\mathbf{y}_{k} - \mathbf{x}^{\ast}}\|}^{2}} \leq {{0.75^{k} \cdot {\mathbb{E}}}{\|{\mathbf{y}_{0} - \mathbf{x}^{\ast}}\|}^{2}}},$ where $\mathbf{y}_{k}$ is the iterate at the end of the $k$-th epoch.

### Proof

We bound the distance to the optimum after one epoch of length $8\kappa^{2}$: The first inequality follows from Lemma 10 and an application of iterated expectations to obtain ${{\mathbb{E}}{\langle{\mathbf{x}_{j} - \mathbf{x}^{\ast}},\mathbf{v}_{j}\rangle}} = {{\mathbb{E}}{\langle{\mathbf{x}_{j} - \mathbf{x}^{\ast}},{{\nabla f}{(\mathbf{x}_{j})}}\rangle}}$. The second inequality follows from the smoothness of $\mathbf{g}{(\mathbf{x},s_{j})}$, and the third inequality follows since $f$ is $m$-strongly convex.

We can rewrite the inequality as $a_{j + 1} \leq {{{({{1 - {2\gammam}} + {2\gamma^{2}L^{2}}})}a_{j}} + {2\gamma^{2}L^{2}a_{0}}}$, because by construction $\mathbf{y} = \mathbf{x}_{0}$. Let $\gamma = \frac{1}{4L\kappa}$. Then, ${{1 - {2\gammam}} + {2\gamma^{2}L^{2}}} \leq {1 - \frac{1}{4\kappa^{2}}}$ and since $\frac{1}{4\kappa^{2}} \leq \frac{1}{4}$. Therefore Setting the length of an epoch to be $j = {2 \cdot {({4\kappa^{2}})}}$ gives us $a_{j + 1} \leq {{({{1/2} + {1/4}})} \cdot a_{0}} = {0.75 \cdot a_{0}}$, and the conclusion follows. ∎ We thus obtain the following convergence rate result:

### Theorem 13

Sparse SVRG, with step size $\gamma = {\mathcal{O}{}\frac{1}{L\kappa}}$ and epoch size $S = {\mathcal{O}{}\kappa^{2}}$, reaches accuracy ${{\mathbb{E}}{\|{\mathbf{y}_{E} - \mathbf{x}^{\ast}}\|}^{2}} \leq \epsilon$ after $E = {\mathcal{O}{}{\log\left( {a_{0}/\epsilon} \right)}}$ epochs, where $\mathbf{y}_{E}$ is the last iterate of the final epoch, and $a_{0} = {\|{\mathbf{x}_{0} - \mathbf{x}^{\ast}}\|}^{2}$ is the initial distance squared to the optimum.

### KroMagnon: Asynchronous Parallel Sparse SVRG

We now present an asynchronous implementation of sparse SVRG. This implementation, which we refer to as KroMagnon, is given in Algorithm 3.

4: while number of sampled hyperedges ≤ S do in parallel 5: sample a random hyperedge s 6: ${\lbrack\hat{\mathbf{x}}\rbrack}_{s}$ = an inconsistent read of the shared variable [x]s Let ${\mathbf{v}{({\hat{\mathbf{x}}}_{j},s_{j})}} = {{{\mathbf{g}{({\hat{\mathbf{x}}}_{j},s_{j})}} - {\mathbf{g}{(\mathbf{y},s_{j})}}} + {\mathbf{D}_{s_{j}}{\nabla f}{(\mathbf{y})}}}$ be the noisy gradient update vector. Then, after processing a total of $T$ hyperedges, the shared memory contains: We now define the perturbed iterates as $\mathbf{x}_{i + 1} = {\mathbf{x}_{i} - {\gamma\mathbf{v}{({\hat{\mathbf{x}}}_{i},s_{i})}}}$ for $i = {0,1,\ldots,{T - 1}}$, where $s_{i}$ is the $i$-th uniformly sampled hyperedge. Since ${{\mathbb{E}}\mathbf{v}{({\hat{\mathbf{x}}}_{j},s_{j})}} = {{\nabla f}{(\mathbf{x}_{j})}}$, KroMagnon also satisfies recursion (2.5): To prove the convergence of KroMagnon we follow the line of reasoning presented in the previous section. Most of the arguments used here come from a straightforward generalization of the analysis of ASCD. The main result of this section is given below.

### Theorem 14

Let the maximum number of samples that can overlap in time with a single sample be bounded as Then, KroMagnon, with step size $\gamma = {\mathcal{O}{}\frac{1}{L\kappa}}$ and epoch size $S = {\mathcal{O}{}\kappa^{2}}$, attains ${{\mathbb{E}}{\|{\mathbf{y}_{E} - \mathbf{x}^{\ast}}\|}^{2}} \leq \epsilon$ after $E = {\mathcal{O}{}{\log\left({a_{0}/\epsilon} \right)}}$ epochs, where $\mathbf{y}_{E}$ is the last iterate of the final epoch, and $a_{0} = {\|{\mathbf{x}_{0} - \mathbf{x}^{\ast}}\|}^{2}$ is the initial distance squared to the optimum.

We would like to note that the total number of iterations in the above bound is---up to a universal constant---the same as that of serial sparse SVRG as presented in Theorem 13. Again, as with Hogwild! and ASCD, this implies a linear speedup.

Similar to our ASCD analysis, we remark that between the two bounds on $\tau$, the second one is the more restrictive. The first one is, up to logarithmic factors, equal to the square root of the total number of iterations per epoch; we expect that the size of the epoch is proportional to $n$, the number of function terms (or data points). This suggests that the first bound is proportional to $\overset{\sim}{\mathcal{O}}{(\sqrt{n})}$ for most reasonable applications. Moreover, the second bound is certainly loose; we argue that it can be tightened using a more refined analysis.

### Proof of Theorem 14

It is easy to see that due to Lemma 10 we get the following bound on the norm of the gradient estimate.

### Lemma 15

For any $k$ and $j$ we have

### Proof

Due to Lemma 10 we have ${{\mathbb{E}}{\|{\mathbf{v}{({\hat{\mathbf{x}}}_{j},s_{j})}}\|}^{2}} \leq {{2L^{2}{\mathbb{E}}{\|{{\hat{\mathbf{x}}}_{j} - \mathbf{x}^{\ast}}\|}^{2}} + {2L^{2}{\mathbb{E}}{\|{\mathbf{y} - \mathbf{x}^{\ast}}\|}^{2}}}$. Then, using the fact that $\mathbf{y} = \mathbf{x}_{0}$ and applying the triangle inequality, we obtain the result. ∎ The set $\mathcal{S}_{r}^{j}$ is defined as in the previous section: $\mathcal{S}_{r}^{j} = {\{{\max{\{{j - {r\tau}},0\}}},\ldots,{j - 1},j,{j + 1},\ldots,{\min{\{{j + {r\tau}},T\}}}\}}$, and has cardinality at most ${2r\tau} + 1$. By Assumption 3. ‣ 3.3 The perturbed iterates view of asynchrony ‣ 3 Analyzing Hogwild! ‣ Perturbed Iterate Analysis for Asynchronous Stochastic Optimization"), there exist diagonal sign matrices $\mathbf{S}_{i}^{j}$ with diagonal entries in $\{{- 1},0,1\}$ such that This leads to the following lemma.

### Lemma 16

If $G_{r} = {\max_{k \in \mathcal{S}_{r}^{j}}{{\mathbb{E}}\left\| {\mathbf{v}{({\hat{\mathbf{x}}}_{k},s_{k})}} \right\|^{2}}}$ and $\Delta_{r} = {\max_{k \in \mathcal{S}_{r}^{j}}{{\mathbb{E}}{\|{{\hat{\mathbf{x}}}_{k} - \mathbf{x}_{j}}\|}^{2}}}$,

### Proof

The proof for the bound on $\Delta_{r}$ is identical to the proof of Lemma 7. We then use Lemma 15 to bound ${\mathbb{E}}\left\| {\mathbf{v}{({\hat{\mathbf{x}}}_{k},s_{k})}} \right\|^{2}$. ∎ As explained in the remark after Lemma 7, it should be possible to improve $\tau^{2}$ to $\tau$ in the upper bound on $\Delta_{r}$. Doing so would improve the condition $\tau = {\mathcal{O}{(\sqrt{n/{\overline{\Delta}}_{\text{C}}})}}$ of Theorem 14 to $\tau = {\mathcal{O}{(\sqrt{n/{\overline{\Delta}}_{\text{C}}})}}$. One possible approach to this problem can be found in § B.2.2 of the Appendix.

We can now obtain bounds on the errors due to asynchrony. The proofs for the following two lemmas can be found in Appendix B.2.

### Lemma 17

Suppose $\tau \leq \frac{\kappa}{\ell}$ and $\gamma = \frac{\theta}{12L\kappa}$. Then the error terms $R_{0}^{j}$ and $R_{1}^{j}$ of KroMagnon satisfy the following inequalities: Similarly to the ASCD derivations, we obtain the following bound for $R_{2}^{j}$.

### Lemma 18

Suppose $\tau \leq \frac{\kappa}{\ell}$ and $\tau = {\mathcal{O}\left( \sqrt{\frac{n}{{\overline{\Delta}}_{\text{C}}}} \right)}$, and let $\gamma = \frac{\theta}{12L\kappa}$. Then,

### Putting it all together

After plugging in the upper bounds on $R_{0}^{j}$, $R_{1}^{j}$, and $R_{2}^{j}$ in the main recursion satisfied by KroMagnon, we find that: If we set $\gamma = {\mathcal{O}{}\frac{\theta}{L\kappa}}$, i.e., the same step size as serial sparse SVRG (Theorem 13), then the above becomes We choose $\theta = {\mathcal{O}{}} \leq {1/2}$ to be a sufficiently small constant, so that the term $\mathcal{O}{}\theta$ in the brackets above is at most $0.5$. Then we can choose $j = {\mathcal{O}{}\kappa^{2}}$ so that the entire coefficient in the brackets is at most $0.75$. Finally, we set $\ell = {\mathcal{O}{}{\log\left({M^{2}/{L^{2}\epsilon}} \right)}}$, so that the last term is smaller than $\epsilon/8$. Let $\mathbf{y}_{k}$ be the iterate after the $k$-th epoch and $A_{k} = {{\mathbb{E}}{\|{\mathbf{y}_{k} - \mathbf{x}^{\ast}}\|}^{2}}$. Therefore, KroMagnon satisfies the recursion This implies that $\mathcal{O}{}{\log{({a_{0}/\epsilon})}}$ epochs are sufficient to reach $\epsilon$ accuracy, where $a_{0}$ is ${\|{\mathbf{x}_{0} - \mathbf{x}^{\ast}}\|}^{2}$ the initial distance squared to the optimum.

## data

## features

Vertex cover222 Following, we optimize a quadratic penalty relaxation for vertex cover ${\min_{x \in {\lbrack 0,1\rbrack}^{{|V|} + {|E|}}}\left. \sum{}_{v \in V}x_{v} \right.} + {\frac{\beta}{2}\left. \sum{}_{{(u,v)} \in E}\left( {{x_{u} + x_{v}} - x_{u,v} - 1} \right)^{2} \right.} + {\frac{1}{2\beta}\left. \sum{}_{v \in V}x_{v}^{2} \right.} + \left. \sum{}_{e \in E}x_{e}^{2} \right.$.

Table 1: The problems and data sets used in our experimental evaluation. We test KroMagnon, dense SVRG, and Hogwild! on three different tasks: linear regression, logistic regression, and vertex cover. We test the algorithms on sparse data sets, of various sizes and feature dimensions.

## Empirical Evaluation of KroMagnon

In this section we evaluate KroMagnon empirically. Our two goals are to demonstrate that KroMagnon is faster than dense SVRG, and KroMagnon has speedups comparable to those of Hogwild!. We implemented Hogwild!, asynchronous dense SVRG, and KroMagnon in Scala, and tested them on the problems and datasets listed in Table 1. Each algorithm was run for 50 epochs, using up to 16 threads. For the SVRG algorithms, we recompute $\mathbf{y}$ and the full gradient ${\nabla f}{(\mathbf{y})}$ every two epochs. We normalize the objective values such that the objective at the initial starting point has a value of one, and the minimum attained across all algorithms and epochs has a value of zero. Experiments were conducted on a Linux machine with 2 Intel Xeon Processor E5-2670 (2.60GHz, eight cores each) with 250Gb memory.

(a) Linear regression, synthetic (b) Logistic regression, synthetic (c) Linear regression, synthetic (d) Logistic regression, synthetic Figure 3: Linear and logistic regression on synthetic data. In subfigures (a) and (b) we plot the convergence with respect to normalized objective value as a function of wall-clock time, and in (c) and (d) the speedup with respect to the number of threads. The above experiments are all for linear and logistic regression problems on synthetic data, in which we have 3 million data points, each with 10K features, and each data point with 20 nonzero entries. We observe that KroMagnon is significantly faster than parallel and dense SVRG, while they both can attain better objective values compared to constant step-size Hogwild!. Moreover, we observe that the speedup gains of Hogwild! and KroMagnon are scaling reasonably well for up to 16 threads.

(a) Vertex cover, wordassociation (b) Vertex cover, eswiki-2013 (c) Vertex cover, wordassociation (d) Vertex cover, eswiki-2013 Figure 4: Vertex cover on the wordassociation-2011 and eswiki-2013 datasets. Subfigure (a) shows the convergence of the algorithms on wordassociation-2011, a small graph with less than 11,000 vertices. KroMagnon on a single thread is 3-4 orders of magnitude faster than desnse SVRG on this dataset. Convergence of KroMagnon and Hogwild! on the eswiki-2013 dataset is shown in subfigure (b); we were unable to run dense SVRG on this larger graph. Subfigures (c) and (d) show the speedups of the algorithms on the two datasets. In subfigure (c), both Hogwild! and KroMagnon exhibit poorer speedups than dense SVRG because of the rapid conve on the smaller wordassociation-2011 dataset. In subfigure (d) we observe that Hogwild! achieves a speedup of up to 8x and KroMagnon up to 5x.

### Comparison with dense SVRG

We were unable to run dense SVRG on the url and eswiki-2013 datasets due to the large number of features. Figures 3(a), 3(b), and 5(a) show that KroMagnon is one-two orders of magnitude faster than dense SVRG. In fact, running dense SVRG on 16 threads is slower than KroMagnon on a single thread. Moreover, as seen in Fig. 4(a), KroMagnon on 16 threads can be up to four orders of magnitude faster than serial dense SVRG. Both dense SVRG and KroMagnon attain similar optima.

### Speedups

We measured the time each algorithm takes to achieve 99.9% and 99.99% of the minimum achieved by that algorithm. Speedups are computed relative to the runtime of the algorithm on a single thread. Although the speedup of KroMagnon varies across datasets, we find that KroMagnon has comparable speedups with Hogwild! on all datasets, as shown in Figure 3(c), 3(d), 4(c), 4(d), 5(c), 5(d). We further observe that dense SVRG has better speedup scaling. This happens because the per iteration complexity of Hogwild! and KroMagnon is significantly cheaper to the extent that the additional overhead associated with having extra threads leads to some speedup loss; this is not the case for dense SVRG as the per iteration cost is higher.

(a) Logistic regression, rcv1 (b) Logistic regression, url (c) Logistic regression, rcv1 (d) Logistic regression, url Figure 5: Logistic regression on the rcv1 and url datasets. Subfigure (a) shows the convergence of the algorithms on the rcv1 dataset. For a given objective value, KroMagnon is 1-2 orders of magnitude faster than dense SVRG. On the larger url dataset (subfigure (b)), we were unable to run dense SVRG. Note that some of the effect of asynchrony can be observed in these experiments: the objective values obtained by KroMagnon, Hogwild!, and dense SVRG are slightly different on 1 thread compared to 16 threads. Speedups of the algorithms are shown in subfigures (c) and (d)–KroMagnon has a slightly better speedup than Hogwild! on rcv1, and the same speedup on url.

## Conclusions and Open Problems

We have introduced a novel framework for analyzing parallel asynchronous stochastic gradient optimization algorithms. The main advantage of our framework is that it is straightforward to apply to a range of first-order stochastic algorithms, while it involves elementary derivations. Moreover, in our analysis we lift, or relax, many of the assumptions made in prior art, *e.g.*, we do not assume consistent reads, and we analyze full stochastic gradient updates. We use our framework to analyze Hogwild! and ASCD, and further introduce and analyze KroMagnon, a new asynchronous sparse SVRG algorithm.

We conclude with some open problems: It would be interesting to obtain tighter bounds for the convergence of function values of the algorithms presented. How do the "errors" due to asynchrony influence the convergence rate of function values? In this case the number of iterations required to reach a target accuracy should scale with the condition number of the objective, not its square. Moreover, the literature on stochastic coordinate descent establishes convergence results in terms of coordinate-wise Lipschitz constants---a more refined smoothness quantity than the full-function smoothness. It would be worthwhile to know if our framework can be adapted to take these parameters into account.

Our perturbed iterates framework relies fundamentally on the strong convexity assumption. However, asynchronous algorithms are known to perform well on non-strongly convex (and even nonconvex) objectives. Can we generalize our framework to simply convex, or smooth functions? Under what assumptions, or simple families of functions, can we show convergence for nonconvex problems?

As previously explained, we believe that the upper bounds on $\tau$---the proxy for the number of cores---in our ASCD and KroMagnon analyses are amenable to improvements. It is an open problem to explore the extent of such improvements.

Our analysis offers sensible upper bounds only in the presence of sparsity. It seems, however, that to obtain speedup results for Hogwild!, it is only necessary to have small correlation between randomly sampled gradients. In what practical setups do randomly selected gradients have sufficiently small correlation? Does that immediately imply linear speedups in the same way that update sparsity does?

In this work we analyzed three similar stochastic first-order methods. It is an open problem to apply our framework and provide an elementary analysis for a greater variety of stochastic gradient type optimization algorithms, such as AdaGrad-type schemes (similar to ), or stochastic dual coordinate methods (similar to ).

Capturing the effects of asynchrony as noise on the algorithmic input seems to be applicable to settings beyond stochastic optimization. As shown recently for a combinatorial graph problem, a similar viewpoint enables the analysis of an asynchronous graph clustering algorithm. It is an interesting endeavor to explore the extent to which a perturbed iterate viewpoint is suitable for analyzing general asynchronous iterative algorithms.
