<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

HOGWILD!: A Lock-Free Approach to Parallelizing Stochastic Gradient Descent

Topics include Stochastic gradient descent, Parallel optimization, Lock-free algorithms, Sparse updates, Shared memory, Machine learning systems, Asynchronous optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Shows that SGD can be parallelized without locks when gradient updates are sparse enough that write conflicts are limited. The paper combines convergence analysis with a simple shared-memory implementation, making HOGWILD! an influential baseline for asynchronous optimization on multicore hardware.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Stochastic Gradient Descent (SGD) is a popular algorithm that can achieve state-of-the-art performance on a variety of machine learning tasks. Several researchers have recently proposed schemes to parallelize SGD, but all require performance-destroying memory locking and synchronization. This work aims to show using novel theoretical analysis, algorithms, and implementation that SGD can be implemented without any locking. We present an update scheme called HOGWILD! which allows processors access to shared memory with the possibility of overwriting each other's work. We show that when the associated optimization problem is sparse, meaning most gradient updates only modify small parts of the decision variable, then HOGWILD! achieves a nearly optimal rate of convergence. We demonstrate experimentally that HOGWILD! outperforms alternative schemes that use locking by an order of magnitude.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

With its small memory footprint, robustness against noise, and rapid learning rates, Stochastic Gradient Descent (SGD) has proved to be well suited to data-intensive machine learning tasks. However, SGD's scalability is limited by its inherently sequential nature; it is difficult to parallelize. Nevertheless, the recent emergence of inexpensive multicore processors and mammoth, web-scale data sets has motivated researchers to develop several clever parallelization schemes for SGD. As many large data sets are currently pre-processed in a MapReduce-like parallel-processing framework, much of the recent work on parallel SGD has focused naturally on MapReduce implementations. MapReduce is a powerful tool developed at Google for extracting information from huge logs (e.g., "find all the urls from a 100TB of Web data") that was designed to ensure fault tolerance and to simplify the maintenance and programming of large clusters of machines. But MapReduce is not ideally suited for online, numerically intensive data analysis. Iterative computation is difficult to express in MapReduce, and the overhead to ensure fault tolerance can result in dismal throughput.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Indeed, even Google researchers themselves suggest that other systems, for example Dremel, are more appropriate than MapReduce for data analysis tasks.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

For some data sets, the sheer size of the data dictates that one use a cluster of machines. However, there are a host of problems in which, after appropriate preprocessing, the data necessary for statistical analysis may consist of a few terabytes or less. For such problems, one can use a single inexpensive work station as opposed to a hundred thousand dollar cluster. Multicore systems have significant performance advantages, including low latency and high throughput shared main memory (a processor in such a system can write and read the shared physical memory at over 12GB/s with latency in the tens of nanoseconds); and high bandwidth off multiple disks (a thousand-dollar RAID can pump data into main memory at over 1GB/s). In contrast, a typical MapReduce setup will read incoming data at rates less than tens of MB/s due to frequent checkpointing for fault tolerance. The high rates achievable by multicore systems move the bottlenecks in parallel computation to synchronization (or locking) amongst the processors. Thus, to enable scalable data analysis on a multicore machine, any performant solution must minimize the overhead of locking.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose a simple strategy for eliminating the overhead associated with locking: *run SGD in parallel without locks*, a strategy that we call Hogwild!. In Hogwild!, processors are allowed equal access to shared memory and are able to update individual components of memory at will. Such a lock-free scheme might appear doomed to fail as processors could overwrite each other's progress. However, when the data access is *sparse*, meaning that individual SGD steps only modify a small part of the decision variable, we show that memory overwrites are rare and that they introduce barely any error into the computation when they do occur. We demonstrate both theoretically and experimentally a near linear speedup with the number of processors on commonly occurring sparse learning problems.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 2, we formalize a notion of sparsity that is sufficient to guarantee such a speedup and provide canonical examples of sparse machine learning problems in classification, collaborative filtering, and graph cuts. Our notion of sparsity allows us to provide theoretical guarantees of linear speedups in Section 4. As a by-product of our analysis, we also derive rates of convergence for algorithms with constant stepsizes. We demonstrate that robust $1/k$ convergence rates are possible with constant stepsize schemes that implement an exponential back-off in the constant over time. This result is interesting in of itself and shows that one need not settle for $1/\sqrt{k}$ rates to ensure robustness in SGD algorithms.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In practice, we find that computational performance of a lock-free procedure exceeds even our theoretical guarantees. We experimentally compare lock-free SGD to several recently proposed methods. We show that all methods that propose memory locking are significantly slower than their respective lock-free counterparts on a variety of machine learning applications.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Sparse Separable Cost Functions", "weight": 1.0} -->

Our goal throughout is to minimize a function $f:{X \subseteq {\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ of the form

<!-- chunk {"id": "body-0011", "role": "body", "section": "Sparse Separable Cost Functions", "weight": 1.0} -->

Here $e$ denotes a small subset of $\{ 1,\ldots,n\}$ and $x_{e}$ denotes the values of the vector $x$ on the coordinates indexed by $e$. The key observation that underlies our lock-free approach is that the natural cost functions associated with many machine learning problems of interest are *sparse* in the sense that $|E|$ and $n$ are both very large but each individual $f_{e}$ acts only on a very small number of components of $x$. That is, each subvector $x_{e}$ contains just a few components of $x$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Sparse Separable Cost Functions", "weight": 1.0} -->

The cost function (2.1) induces a *hypergraph* $G = {(V,E)}$ whose nodes are the individual components of $x$. Each subvector $x_{e}$ induces an edge in the graph $e \in E$ consisting of some subset of nodes. A few examples illustrate this concept.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Sparse SVM", "weight": 1.0} -->

and we know *a priori* that the examples $z_{\alpha}$ are very sparse (see for example ). To write this cost function in the form of (2.1), let $e_{\alpha}$ denote the components which are non-zero in $z_{\alpha}$ and let $d_{u}$ denote the number of training examples which are non-zero in component $u$ ($u = {1,2,\ldots,n}$). Then we can rewrite (2.2) as

<!-- chunk {"id": "body-0014", "role": "body", "section": "Sparse SVM", "weight": 1.0} -->

Each term in the sum (2.3) depends only on the components of $x$ indexed by the set $e_{\alpha}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Matrix Completion", "weight": 1.0} -->

In the matrix completion problem, we are provided entries of a low-rank, $n_{r} \times n_{c}$ matrix $\mathbf{Z}$ from the index set $E$. Such problems arise in collaborative filtering, Euclidean distance estimation, and clustering. Our goal is to reconstruct $\mathbf{Z}$ from this sparse sampling of data.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Graph Cuts", "weight": 1.0} -->

Problems involving minimum cuts in graphs frequently arise in machine learning (see for a comprehensive survey). In such problems, we are given a sparse, nonnegative matrix $W$ which indexes similarity between entities. Our goal is to find a partition of the index set $\{ 1,\ldots,n\}$ that best conforms to this similarity matrix. Here the graph structure is explicitly determined by the similarity matrix $W$; arcs correspond to nonzero entries in $W$. We want to match each string to some list of $D$ entities. Each node is associated with a vector $x_{i}$ in the $D$-dimensional simplex $S_{D} = {\{{\zeta \in {\mathbb{R}}^{D}}:{\zeta_{v} \geq {0{\sum_{v = 1}^{D}\zeta_{v}}} = 1}\}}$. Here, two-way cuts use $D = 2$, but multiway-cuts with tens of thousands of classes also arise in entity resolution problems.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Graph Cuts", "weight": 1.0} -->

For example, we may have a list of $n$ strings, and $W_{uv}$ might index the similarity of each string. Several authors (e.g., ) propose to minimize the cost function

<!-- chunk {"id": "body-0018", "role": "body", "section": "Graph Cuts", "weight": 1.0} -->

In all three of the preceding examples, the number of components involved in a particular term $f_{e}$ is a small fraction of the total number of entries.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Graph Cuts", "weight": 1.0} -->

The quantity $\Omega$ simply quantifies the size of the hyper edges. $\rho$ determines the maximum fraction of edges that intersect any given edge. $\Delta$ determines the maximum fraction of edges that intersect any variable. $\rho$ is a measure of the sparsity of the hypergraph, while $\Delta$ measures the node-regularity. For our examples, we can make the following observations about $\rho$ and $\Delta$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Graph Cuts", "weight": 1.0} -->

Sparse SVM. $\Delta$ is simply the maximum frequency that any feature appears in an example, while $\rho$ measures how clustered the hypergraph is. If some features are very common across the data set, then $\rho$ will be close to one.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Graph Cuts", "weight": 1.0} -->

Matrix Completion. If we assume that the provided examples are sampled uniformly at random and we see more than $n_{c}{\log{(n_{c})}}$ of them, then $\Delta \approx \frac{\log{(n_{r})}}{n_{r}}$ and $\rho \approx \frac{2{\log{(n_{r})}}}{n_{r}}$. This follows from a *coupon collector* argument.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Graph Cuts", "weight": 1.0} -->

Graph Cuts. $\Delta$ is the maximum degree divided by $|E|$, and $\rho$ is at most $2\Delta$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Graph Cuts", "weight": 1.0} -->

We now describe a simple protocol that achieves a linear speedup in the number of processors when $\Omega$, $\Delta$, and $\rho$ are relatively small.

<!-- chunk {"id": "body-0024", "role": "body", "section": "The Hogwild! Algorithm", "weight": 1.0} -->

Here we discuss the parallel processing setup. We assume a shared memory model with $p$ processors. The decision variable $x$ is accessible to all processors. Each processor can read $x$, and can contribute an update vector to $x$. The vector $x$ is stored in shared memory, and we assume that the componentwise addition operation is atomic, that is

<!-- chunk {"id": "body-0025", "role": "body", "section": "The Hogwild! Algorithm", "weight": 1.0} -->

can be performed atomically by any processor for a scalar $a$ and $v \in {\{ 1,\ldots,n\}}$. This operation does not require a separate locking structure on most modern hardware: such an operation is a single atomic instruction on GPUs and DSPs, and it can be implemented via a compare-and-exchange operation on a general purpose multicore processor like the Intel Nehalem. In contrast, the operation of updating many components at once requires an auxiliary locking structure.

<!-- chunk {"id": "body-0026", "role": "body", "section": "The Hogwild! Algorithm", "weight": 1.0} -->

Each processor then follows the procedure in Algorithm 1. To fully describe the algorithm, let $b_{v}$ denote one of the standard basis elements in ${\mathbb{R}}^{n}$, with $v$ ranging from $1,\ldots,n$. That is, $b_{v}$ is equal to $1$ on the $v$th component and $0$ otherwise. Let $\mathcal{P}_{v}$ denote the Euclidean projection matrix onto the $v$th coordinate, i.e., $\mathcal{P}_{v} = {b_{v}b_{v}^{T}}$. $\mathcal{P}_{v}$ is a diagonal matrix equal to $1$ on the $v$th diagonal and zeros elsewhere. Let ${G_{e}{(x)}} \in {\mathbb{R}}^{n}$ denote a gradient or subgradient of the function $f_{e}$ multiplied by $|E|$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "The Hogwild! Algorithm", "weight": 1.0} -->

That is, we extend $f_{e}$ from a function on the coordinates of $e$ to all of ${\mathbb{R}}^{n}$ simply by ignoring the components in $\neg e$ (i.e., not in $e$). Then

<!-- chunk {"id": "body-0028", "role": "body", "section": "The Hogwild! Algorithm", "weight": 1.0} -->

Here, $G_{e}$ is equal to zero on the components in $\neg e$. Using a sparse representation, we can calculate $G_{e}{(x)}$, only knowing the values of $x$ in the components indexed by $e$. Note that as a consequence of the uniform random sampling of $e$ from $E$, we have

<!-- chunk {"id": "body-0029", "role": "body", "section": "The Hogwild! Algorithm", "weight": 1.0} -->

In Algorithm 1, each processor samples an term $e \in E$ uniformly at random, computes the gradient of $f_{e}$ at $x_{e}$, and then writes

<!-- chunk {"id": "body-0030", "role": "body", "section": "The Hogwild! Algorithm", "weight": 1.0} -->

Importantly, note that the processor modifies only the variables indexed by $e$, leaving all of the components in $\neg e$ (i.e., not in $e$) alone. We assume that the stepsize $\gamma$ is a fixed constant. Even though the processors have no knowledge as to whether any of the other processors have modified $x$, we define $x_{j}$ to be the state of the decision variable $x$ after $j$ updates have been performed^11^1Our notation overloads subscripts of $x$. For clarity throughout, subscripts $i,j$, and $k$ refer to iteration counts, and $v$ and $e$ refer to components or subsets of components.. Since two processors can write to $x$ at the same time, we need to be a bit careful with this definition, but we simply break ties at random. Note that $x_{j}$ is generally updated with a stale gradient, which is based on a value of $x$ read many clock cycles earlier.

<!-- chunk {"id": "body-0031", "role": "body", "section": "The Hogwild! Algorithm", "weight": 1.0} -->

We use $x_{k{(j)}}$ to denote the value of the decision variable used to compute the gradient or subgradient that yields the state $x_{j}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "The Hogwild! Algorithm", "weight": 1.0} -->

2: Sample e uniformly at random from E
3: Read current state xe and evaluate Ge (x)
Algorithm 1 Hogwild! update for individual processors

<!-- chunk {"id": "body-0033", "role": "body", "section": "The Hogwild! Algorithm", "weight": 1.0} -->

In what follows, we provide conditions under which this asynchronous, incremental gradient algorithm converges. Moreover, we show that if the hypergraph induced by $f$ is isotropic and sparse, then this algorithm converges in nearly the same number of gradient steps as its serial counterpart. Since we are running in parallel and without locks, this means that we get a nearly linear speedup in terms of the number of processors.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Fast Rates for Lock-Free Parallelism", "weight": 1.0} -->

We now turn to our theoretical analysis of Hogwild! protocols. To make the analysis tractable, we assume that we update with the following "with replacement" procedure: each processor samples an edge $e$ uniformly at random and computes a subgradient of $f_{e}$ at the current value of the decision variable. Then it chooses an $v \in e$ uniformly at random and updates

<!-- chunk {"id": "body-0035", "role": "body", "section": "Fast Rates for Lock-Free Parallelism", "weight": 1.0} -->

Note that the stepsize is a factor $|e|$ larger than the step in (3.1). Also note that this update is completely equivalent to

<!-- chunk {"id": "body-0036", "role": "body", "section": "Fast Rates for Lock-Free Parallelism", "weight": 1.0} -->

This notation will be more convenient for the subsequent analysis.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Fast Rates for Lock-Free Parallelism", "weight": 1.0} -->

This with replacement scheme assumes that a gradient is computed and then only one of its components is used to update the decision variable. Such a scheme is computationally wasteful as the rest of the components of the gradient carry information for decreasing the cost. Consequently, in practice and in our experiments, we perform a modification of this procedure. We partition out the edges *without replacement* to all of the processors at the beginning of each epoch. The processors then perform *full updates* of all of the components of each edge in their respective queues. However, we emphasize again that we do not implement any locking mechanisms on any of the variables. We do not analyze this "without replacement" procedure because no one has achieved tractable analyses for SGD in any without replacement sampling models. Indeed, to our knowledge, all analysis of without-replacement sampling yields rates that are comparable to a standard subgradient descent algorithm which takes steps along the full gradient of (2.1) (see, for example ). That is, these analyses suggest that without-replacement sampling should require a factor of $|E|$ more steps than with-replacement sampling. In practice, this worst case behavior is never observed.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Fast Rates for Lock-Free Parallelism", "weight": 1.0} -->

In fact, it is conventional wisdom in machine learning that without-replacement sampling in stochastic gradient descent actually outperforms the with-replacement variants on which all of the analysis is based.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Fast Rates for Lock-Free Parallelism", "weight": 1.0} -->

To state our theoretical results, we must describe several quantities that important in the analysis of our parallel stochastic gradient descent scheme. We follow the notation and assumptions of Nemirovski *et al*. To simplify the analysis, we will assume that each $f_{e}$ in (2.1) is a convex function.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Fast Rates for Lock-Free Parallelism", "weight": 1.0} -->

We also assume $f$ is strongly convex with modulus $c$. By this we mean that

<!-- chunk {"id": "body-0041", "role": "body", "section": "Fast Rates for Lock-Free Parallelism", "weight": 1.0} -->

When $f$ is strongly convex, there exists a unique minimizer $x_{\star}$ and we denote $f_{\star} = {f{(x_{\star})}}$. We additionally assume that there exists a constant $M$ such that

<!-- chunk {"id": "body-0042", "role": "body", "section": "Fast Rates for Lock-Free Parallelism", "weight": 1.0} -->

We assume throughout that ${\gammac} < 1$. (Indeed, when ${\gammac} > 1$, even the ordinary gradient descent algorithms will diverge.)

<!-- chunk {"id": "body-0043", "role": "body", "section": "Fast Rates for Lock-Free Parallelism", "weight": 1.0} -->

Our main results are summarized by the following

<!-- chunk {"id": "body-0044", "role": "body", "section": "Robust $1/k$ rates", "weight": 1.0} -->

Suppose we run Algorithm 1 for a fixed number of gradient updates $K$ with stepsize $\gamma < {1/c}$. Then, we wait for the threads to coalesce, reduce $\gamma$ by a constant factor $\beta \in {}$, and run for $\beta^{- 1}K$ iterations. In some sense, this piecewise constant stepsize protocol approximates a $1/k$ diminishing stepsize. The main difference with the following analysis from previous work is that our stepsizes are always less than $1/c$ in contrast to beginning with very large stepsizes. Always working with small stepsizes allows us to avoid the possible exponential slow-downs that occur with standard diminishing stepsize schemes.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Robust $1/k$ rates", "weight": 1.0} -->

To be precise, suppose $a_{k}$ is any sequence of real numbers satisfying

<!-- chunk {"id": "body-0046", "role": "body", "section": "Robust $1/k$ rates", "weight": 1.0} -->

where $a_{\infty}$ is some non-negative function of $\gamma$ satisfying

<!-- chunk {"id": "body-0047", "role": "body", "section": "Robust $1/k$ rates", "weight": 1.0} -->

and $c_{r}$ and $B$ are constants. This recursion underlies many convergence proofs for SGD where $a_{k}$ denotes the distance to the optimal solution after $k$ iterations. We will derive appropriate constants for Hogwild! in the Appendix. We will also discuss below what these constants are for standard stochastic gradient descent algorithms.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Robust $1/k$ rates", "weight": 1.0} -->

Factoring out the dependence on $\gamma$ will be useful in what follows. Unwrapping (5.1) we have

<!-- chunk {"id": "body-0049", "role": "body", "section": "Robust $1/k$ rates", "weight": 1.0} -->

Suppose we want this quantity to be less than $\epsilon$. It is sufficient that both terms are less than $\epsilon/2$. For the second term, this means that it is sufficient to set

<!-- chunk {"id": "body-0050", "role": "body", "section": "Robust $1/k$ rates", "weight": 1.0} -->

For the first term, we then need

<!-- chunk {"id": "body-0051", "role": "body", "section": "Robust $1/k$ rates", "weight": 1.0} -->

By (5.2), we should pick $\gamma = \frac{\epsilon\vartheta}{2B}$ for $\vartheta \in {(0,1\rbrack}$. Combining this with (5.3) tells us that after

<!-- chunk {"id": "body-0052", "role": "body", "section": "Robust $1/k$ rates", "weight": 1.0} -->

iterations we will have $a_{k} \leq \epsilon$. This right off the bat almost gives us a $1/k$ rate, modulo the $\log{({1/\epsilon})}$ factor.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Robust $1/k$ rates", "weight": 1.0} -->

To eliminate the log factor, we can implement a backoff scheme where we reduce the stepsize by a constant factor after several iterations. This backoff scheme will have two phases: the first phase will consist of converging to the ball about $x_{\star}$ of squared radius less than $\frac{2B}{c_{r}}$ at an exponential rate. Then we will converge to $x_{\star}$ by shrinking the stepsize.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Robust $1/k$ rates", "weight": 1.0} -->

To calculate the number of iterates required to get inside a ball of squared radius $\frac{2B}{c_{r}}$, suppose the initial stepsize is chosen as $\gamma = \frac{\vartheta}{c_{r}}$ ($0 < \vartheta < 1$). This choice of stepsize guarantees that the $a_{k}$ converge to $a_{\infty}$. We use the parameter $\vartheta$ to demonstrate that we do not suffer much for underestimating the optimal stepsize (i.e., $\vartheta = 1$) in our algorithms. Using (5.3) we find that

<!-- chunk {"id": "body-0055", "role": "body", "section": "Robust $1/k$ rates", "weight": 1.0} -->

iterations are sufficient to converge to this ball. Note that this is a linear rate of convergence.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Robust $1/k$ rates", "weight": 1.0} -->

Now assume that $a_{0} < \frac{2\varthetaB}{c_{r}}$. Let's reduce the stepsize by a factor of $\beta$ each epoch. This reduces the achieved $\epsilon$ by a factor of $\beta$. Thus, after $\log_{\beta}{({a_{0}/\epsilon})}$ epochs, we will be at accuracy $\epsilon$. The total number of iterations required is then the sum of terms with the form (5.3), with $a_{0}$ set to be the radius achieved by the previous epoch and $\epsilon$ set to be $\beta$ times this $a_{0}$. Hence, for epoch number $\nu$, the initial distance is $\beta^{\nu - 1}a_{0}$ and the final radius is $\beta^{\nu}$. Summing over all of the epochs (except for the initial phase) gives

<!-- chunk {"id": "body-0057", "role": "body", "section": "Robust $1/k$ rates", "weight": 1.0} -->

This expression is minimized by selecting a backoff parameter $\approx 0.37$. Also, note that when we reduce the stepsize by $\beta$, we need to run for $\beta^{- 1}$ more iterations.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Robust $1/k$ rates", "weight": 1.0} -->

Combining (5.4) and (5.5), we estimate a total number of iterations equal to

<!-- chunk {"id": "body-0059", "role": "body", "section": "Robust $1/k$ rates", "weight": 1.0} -->

are sufficient to guarantee that $a_{k} \leq \epsilon$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Consequences for serial SGD", "weight": 1.0} -->

Let us compare the results of this constant step-size protocol to one where the stepsize at iteration $k$ is set to be $\gamma_{0}/k$ for some initial step size $\gamma$ for the standard (serial) incremental gradient algorithm applied to (2.1). Nemirovski *et al* show that the expected squared distance to the optimal solution, $a_{k}$, satisfies

<!-- chunk {"id": "body-0061", "role": "body", "section": "Consequences for serial SGD", "weight": 1.0} -->

The authors of demonstrate that a large step size: $\gamma_{k} = \frac{\Theta}{2ck}$ with $\Theta > 1$ yields a bound

<!-- chunk {"id": "body-0062", "role": "body", "section": "Consequences for serial SGD", "weight": 1.0} -->

On the other hand, a constant step size protocol achieves

<!-- chunk {"id": "body-0063", "role": "body", "section": "Consequences for serial SGD", "weight": 1.0} -->

This bound is obtained by plugging the algorithm parameters into (5.6) and letting $D_{0} = {2a_{0}}$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Consequences for serial SGD", "weight": 1.0} -->

Note that both bounds have asymptotically the same dependence on $M$, $c$, and $k$. The expression

<!-- chunk {"id": "body-0065", "role": "body", "section": "Consequences for serial SGD", "weight": 1.0} -->

is minimized when $\beta \approx 0.37$ and is equal to $1.34$. The expression

<!-- chunk {"id": "body-0066", "role": "body", "section": "Consequences for serial SGD", "weight": 1.0} -->

is minimized when $\Theta = 2$ and is equal to $1$ at this minimum. So the leading constant is slightly worse in the constant stepsize protocol when all of the parameters are set optimally. However, if $D_{0} \geq {M^{2}/c^{2}}$, the $1/k$ protocol has error proportional to $D_{0}$, but our constant stepsize protocol still has only a logarithmic dependence on the initial distance. Moreover, the constant stepsize scheme is much more robust to overestimates of the curvature parameter $c$. For the $1/k$ protocols, if one overestimates the curvature (corresponding to a small value of $\Theta$), one can get arbitrarily slow rates of convergence. An simple, one dimensional example in shows that $\Theta = 0.2$ can yield a convergence rate of $k^{- {1/5}}$. In our scheme, $\vartheta = 0.2$ simply increases the number of iterations by a factor of $5$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Consequences for serial SGD", "weight": 1.0} -->

The proposed fix in for the sensitivity to curvature estimates results in asymptotically slower convergence rates of $1/\sqrt{k}$. It is important to note that we need not settle for these slower rates and can still achieve robust convergence at $1/k$ rates.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Parallel Implementation of a Backoff Scheme", "weight": 1.0} -->

The scheme described about results in a $1/k$ rate of convergence for Hogwild! with the only synchronization overhead occurring at the end of each "round" or "epoch" of iteration. When implementing a backoff scheme for Hogwild!, the processors have to agree on when to reduce the stepsize. One simple scheme for this is to run all of the processors for a fixed number of iterations, wait for all of the threads to complete, and then globally reduce the stepsize in a master thread. We note that one can eliminate the need for the threads to coalesce by sending out-of-band messages to the processors to signal when to reduce $\gamma$. This complicates the theoretical analysis as there may be times when different processors are running with different stepsizes, but in practice could allow one to avoid synchronization costs. We do not implement this scheme, and so do not analyze this idea further.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Experiments", "weight": 1.0} -->

We ran numerical experiments on a variety of machine learning tasks, and compared against a round-robin approach proposed in and implemented in Vowpal Wabbit. We refer to this approach as RR. To be as fair as possible to prior art, we hand coded RR to be nearly identical to the Hogwild! approach, with the only difference being the schedule for how the gradients are updated. One notable change in RR from the Vowpal Wabbit software release is that we optimized RR's locking and signaling mechanisms to use spinlocks and busy waits (there is no need for generic signaling to implement round robin). We verified that this optimization results in nearly an order of magnitude increase in wall clock time for all problems that we discuss.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Experiments", "weight": 1.0} -->

We also compare against a model which we call AIG which can be seen as a middle ground between RR and Hogwild!. AIG runs a protocol identical to Hogwild! except that it locks all of the variables in $e$ in before and after the for loop on line 4 of Algorithm 1. Our experiments demonstrate that even this fine-grained locking induces undesirable slow-downs.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Experiments", "weight": 1.0} -->

All of the experiments were coded in C++ are run on an identical configuration: a dual Xeon X650 CPUs (6 cores each x 2 hyperthreading) machine with 24GB of RAM and a software RAID-0 over 7 2TB Seagate Constellation 7200RPM disks. The kernel is Linux 2.6.18-128. We never use more than 2GB of memory. All training data is stored on a seven-disk raid 0. We implemented a custom file scanner to demonstrate the speed of reading data sets of disk into small shared memory. This allows us to read data from the raid at a rate of nearly 1GB/s.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Experiments", "weight": 1.0} -->

All of the experiments use a constant stepsize $\gamma$ which is diminished by a factor $\beta$ at the end of each pass over the training set. We run all experiments for 20 such passes, even though less epochs are often sufficient for convergence. We show results for the largest value of the learning rate $\gamma$ which converges and we use $\beta = 0.9$ throughout. We note that the results look the same across a large range of $(\gamma,\beta)$ pairs and that all three parallelization schemes achieve train and test errors within a few percent of one another. We present experiments on the classes of problems described in Section 2.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Experiments", "weight": 1.0} -->

Sparse SVM. We tested our sparse SVM implementation on the Reuters RCV1 data set on the binary text classification task CCAT. There are 804,414 examples split into 23,149 training and 781,265 test examples, and there are 47,236 features. We swapped the training set and the test set for our experiments to demonstrate the scalability of the parallel multicore algorithms. In this example, $\rho = 0.44$ and $\Delta = 1.0$---large values that suggest a bad case for Hogwild!. Nevertheless, in Figure 3(a), we see that Hogwild! is able to achieve a factor of 3 speedup with while RR gets worse as more threads are added. Indeed, for fast gradients, RR is worse than a serial implementation.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Experiments", "weight": 1.0} -->

For this data set, we also implemented the approach in which runs multiple SGD runs in parallel and averages their output. In Figure 5(b), we display at the train error of the ensemble average across parallel threads at the end of each pass over the data. We note that the threads only communicate at the very end of the computation, but we want to demonstrate the effect of parallelization on train error. Each of the parallel threads touches every data example in each pass. Thus, the $10$ thread run does $10$x more gradient computations than the serial version. Here, the error is the same whether we run in serial or with ten instances. We conclude that on this problem, there is no advantage to running in parallel with this averaging scheme.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Experiments", "weight": 1.0} -->

Matrix Completion. We ran Hogwild! on three very large matrix completion problems. The Netflix Prize data set has 17,770 rows, 480,189 columns, and 100,198,805 revealed entries. The KDD Cup 2011 (task 2) data set has 624,961 rows, 1,000,990, columns and 252,800,275 revealed entries. We also synthesized a low-rank matrix with rank $10$, 1e7 rows and columns, and 2e9 revealed entries. We refer to this instance as "Jumbo." In this synthetic example, $\rho$ and $\Delta$ are both around 1e-7. These values contrast sharply with the real data sets where $\rho$ and $\Delta$ are both on the order of 1e-3.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Experiments", "weight": 1.0} -->

Graph Cuts. Our first cut problem was a standard image segmentation by graph cuts problem popular in computer vision. We computed a two-way cut of the abdomen data set. This data set consists of a volumetric scan of a human abdomen, and the goal is to segment the image into organs. The image has $512 \times 512 \times 551$ voxels, and the associated graph is 6-connected with maximum capacity 10. Both $\rho$ and $\Delta$ are equal to 9.2e-4 We see that Hogwild! speeds up the cut problem by more than a factor of 4 with 10 threads, while RR is twice as slow as the serial version.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Experiments", "weight": 1.0} -->

Our second graph cut problem sought a mulit-way cut to determine entity recognition in a large database of web data. We created a data set of clean entity lists from the DBLife website and of entity mentions from the DBLife Web Crawl. The data set consists of 18,167 entities and 180,110 mentions and similarities given by string similarity. In this problem each stochastic gradient step must compute a Euclidean projection onto a simplex of dimension 18,167. As a result, the individual stochastic gradient steps are quite slow. Nonetheless, the problem is still very sparse with $\rho$=8.6e-3 and $\Delta$=4.2e-3. Consequently, in Figure 3, we see the that Hogwild! achieves a ninefold speedup with 10 cores. Since the gradients are slow, RR is able to achieve a parallel speedup for this problem, however the speedup with ten processors is only by a factor of 5. That is, even in this case where the gradient computations are very slow, Hogwild! outperforms a round-robin scheme.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Experiments", "weight": 1.0} -->

What if the gradients are slow? As we saw with the DBLIFE data set, the RR method does get a nearly linear speedup when the gradient computation is slow. This raises the question whether RR ever outperforms Hogwild! for slow gradients. To answer this question, we ran the RCV1 experiment again and introduced an artificial delay at the end of each gradient computation to simulate a slow gradient. In Figure 5(c), we plot the wall clock time required to solve the SVM problem as we vary the delay for both the RR and Hogwild! approaches.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Experiments", "weight": 1.0} -->

Notice that Hogwild! achieves a greater decrease in computation time across the board. The speedups for both methods are the same when the delay is few milliseconds. That is, if a gradient takes longer than one millisecond to compute, RR is on par with Hogwild! (but not better). At this rate, one is only able to compute about a million stochastic gradients per hour, so the gradient computations must be very labor intensive in order for the RR method to be competitive.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Our proposed Hogwild! algorithm takes advantage of sparsity in machine learning problems to enable near linear speedups on a variety of applications. Empirically, our implementations outperform our theoretical analysis. For instance, $\rho$ is quite large in the RCV1 SVM problem, yet we still obtain significant speedups. Moreover, our algorithms allow parallel speedup even when the gradients are computationally intensive.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Our Hogwild! schemes can be generalized to problems where some of the variables occur quite frequently as well. We could choose to not update certain variables that would be in particularly high contention. For instance, we might want to add a bias term to our Support Vector Machine, and we could still run a Hogwild! scheme, updating the bias only every thousand iterations or so.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Conclusions", "weight": 1.0} -->

For future work, it would be of interest to enumerate structures that allow for parallel gradient computations with no collisions at all. That is, it may be possible to bias the SGD iterations to completely avoid memory contention between processors. For example, recent work proposed a biased ordering of the stochastic gradients in matrix completion problems that completely avoids memory contention between processors. An investigation into how to generalize this approach to other structures and problems would enable even faster computation of machine learning problems.
