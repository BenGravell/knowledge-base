<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Bayesian Optimization in a Billion Dimensions via Random Embeddings

Topics include REMBO, Bayesian optimization, Random embeddings, High-dimensional optimization, Black-box optimization, Gaussian processes, Algorithm configuration.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces REMBO, a Bayesian optimization method that searches a random low-dimensional embedding of a very high-dimensional input space. The key contribution is showing that Gaussian-process Bayesian optimization can remain effective in billion-dimensional spaces when the objective has low intrinsic dimensionality, with both theory and solver-configuration experiments supporting the claim.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Bayesian optimization techniques have been successfully applied to robotics, planning, sensor placement, recommendation, advertising, intelligent user interfaces and automatic algorithm configuration. Despite these successes, the approach is restricted to problems of moderate dimension, and several workshops on Bayesian optimization have identified its scaling to high-dimensions as one of the holy grails of the field. In this paper, we introduce a novel random embedding idea to attack this problem. The resulting Random EMbedding Bayesian Optimization (REMBO) algorithm is very simple, has important invariance properties, and applies to domains with both categorical and continuous variables. We present a thorough theoretical analysis of REMBO. Empirical results confirm that REMBO can effectively solve problems with billions of dimensions, provided the intrinsic dimensionality is low. They also show that REMBO achieves state-of-the-art performance in optimizing the 47 discrete parameters of a popular mixed integer linear programming solver.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Let $f:{\mathcal{X}\rightarrow{\mathbb{R}}}$ be a function on a compact subset $\mathcal{X} \subseteq {\mathbb{R}}^{D}$. We address the following global optimization problem

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We are particularly interested in objective functions $f$ that may satisfy one or more of the following criteria: they do not have a closed-form expression, are expensive to evaluate, do not have easily available derivatives, or are non-convex. We treat $f$ as a *blackbox* function that only allows us to query its function value at arbitrary $x \in \mathcal{X}$. To address objectives of this challenging nature, we adopt the Bayesian optimization framework.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In a nutshell, in order to optimize a blackbox function $f$, Bayesian optimization uses a prior distribution that captures our beliefs about the behavior of $f$, and updates this prior with sequentially acquired data. Specifically, it iterates the following phases: use the prior to decide at which input $x \in \mathcal{X}$ to query $f$ next; evaluate $f{(x)}$; and update the prior based on the new data $\langle x,{f{(x)}}\rangle$. Step 1 uses a so-called *acquisition function* that quantifies the expected value of learning the value of $f{(x)}$ for each $x \in \mathcal{X}$. This procedure is illustrated in Figure 1.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The role of the acquisition function is to trade off exploration and exploitation; popular choices include Thompson sampling (?, ?), probability of improvement (?), expected improvement (?), upper-confidence-bounds (?), and online portfolios of these (?). These are typically optimized by choosing points where the predictive mean is high (exploitation) and where the variance is large (exploration). Since they typically have an analytical expression that is easy to evaluate, they are much easier to optimize than the original objective function, using off-the-shelf numerical optimization algorithms.^11^1This optimization step can in fact be circumvented when using treed multi-scale optimistic optimization as recently demonstrated by ? (?). There also exist several more involved Bayesian non-linear experimental design approaches for constructing the acquisition function, where the utility to be optimized involves an entropy of an aspect of the posterior. This includes the work of ? (?) for finding maxima of functions, the works of ? (?) and ? (?) for learning functions, and the work of ? (?) for estimating Markov decision processes.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

These works rely on expensive approximate inference methods for computing intractable integrals.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The term *Bayesian optimization* was coined several decades ago by Jonas Močkus (?). A popular version of the method is known as *efficient global optimization* in the experimental design literature since the 1990s (?). Often, the approximation of the objective function is obtained using Gaussian process (GP) priors. For this reason, the technique is also referred to as *GP bandits* (?). However, many other approximations of the objective have been proposed, including Parzen estimators (?), Bayesian parametric models (?), treed GPs (?) and random forests (?, ?, ?). These may be more suitable than GPs when the number of iterations grows without bound, or when the objective function is believed to have discontinuities. We also note that often assumptions on the smoothness of the objective function are encoded without use of the Bayesian paradigm, while leading to similar algorithms and theoretical guarantees (see, for example, ?, and the references therein).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

There is a rich literature on Bayesian optimization, and for further details we refer readers to more tutorial treatments (?, ?, ?, ?, ?, ?) and recent theoretical results (?, ?, ?).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Bayesian optimization has been demonstrated to outperform other state-of-the-art blackbox optimization techniques when function evaluations are expensive and the number of allowed function evaluations is therefore low (?). In recent years, it has found increasing use in the machine learning community (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?). Despite many success stories, the approach is restricted to problems of moderate dimension, typically up to about 10. Of course, for a great many problems this is all that is needed. However, to advance the state of the art, we need to scale the methodology to high-dimensional parameter spaces. This is the goal of this paper.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is difficult to scale Bayesian optimization to high dimensions. To ensure that a global optimum is found, we require good coverage of $\mathcal{X}$, but as the dimensionality increases, the number of evaluations needed to cover $\mathcal{X}$ increases exponentially. As a result, there has been little progress on this challenging problem, with a few exceptions. ? (?) introduced a non-standard Bayesian optimization method based on a tree of one-dimensional density estimators and applied it successfully to optimize the 238 parameters of a complex vision architecture (?). ? (?) used random forests models in Bayesian optimization to achieve state-of-the-art performance in optimizing up to 76 mixed discrete/continuous parameters of algorithms for solving hard combinatorial problems, and to successfully carry out combined model selection and hyperparameter optimization for the 768 parameters of the Auto-WEKA framework (?). ? (?) showed that these two methods indeed yielded the best performance for high-dimensional hyperparameter optimization (e.g., in deep belief networks).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, both are based on weak uncertainty estimates that can fail even for the optimization of very simple functions and lack theoretical guarantees.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the *linear* bandits case, ? (?) recently proposed a compressed sensing strategy to attack problems with a high degree of sparsity. Also recently, ? (?) made significant progress by introducing a two stage strategy for optimization and variable selection of high-dimensional GPs. In the first stage, sequential likelihood ratio tests, with a couple of tuning parameters, are used to select the relevant dimensions. This, however, requires the relevant dimensions to be axis-aligned with an ARD kernel. Chen and colleagues provide empirical results only for synthetic examples (of up to 400 dimensions), but they provide key theoretical guarantees.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many researchers have noted that for certain classes of problems most dimensions do not change the objective function significantly; examples include hyper-parameter optimization for neural networks and deep belief networks (?), as well as other machine learning algorithms and various state-of-the-art algorithms for solving $\mathcal{N}\mathcal{P}$-hard problems (?). That is to say these problems have *"low effective dimensionality"*. To take advantage of this property, ? (?) proposed to simply use random search for optimization -- the rationale being that points sampled uniformly at random in each dimension can densely cover each low-dimensional subspace. As such, random search can exploit low effective dimensionality *without knowing which dimensions are important*. In this paper, we exploit the same property in a new Bayesian optimization variant based on random embeddings.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

As we first demonstrated in a recent IJCAI conference paper (?), random embeddings enable us to scale Bayesian optimization to arbitrary $D$ provided the objective function has low intrinsic dimensionality. Importantly, the algorithm associated with this idea, which we called REMBO, is not restricted to cases with axis-aligned intrinsic dimensions but applies to any $d$-dimensional linear subspace. ? (?) recently proposed an adaptive, but more expensive, variant of REMBO with theoretical guarantees.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this journal version of our work, we expand the presentation to provide more details throughout. In particular, we expand our description of the strategy for selecting the boundaries of the low-dimensional space and for setting the kernel length scale parameter; we show by means of an additional application (automatic configuration of random forest body-part classifiers) that the performance of our technique does not collapse when the problem does not have an obvious low effective dimensionality. Our experiments (Section 4) also show that REMBO can solve problems of previously untenable high extrinsic dimensions, and that REMBO can achieve state-of-the-art performance for optimizing the 47 discrete parameters of a popular mixed integer linear programming solver.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Bayesian Optimization", "weight": 1.0} -->

As mentioned in the introduction, Bayesian optimization has two ingredients that need to be specified: The prior and the acquisition function. In this work, we adopt GP priors. We review GPs very briefly and refer the interested reader to the book by ? (?). A GP is a distribution over functions specified by its mean function $m{( \cdot )}$ and covariance $k{( \cdot, \cdot )}$. More specifically, given a set of points $\mathbf{x}_{1:t}$, with $\mathbf{x}_{i} \in {\mathbb{R}}^{D}$, we have

<!-- chunk {"id": "body-0019", "role": "body", "section": "Bayesian Optimization", "weight": 1.0} -->

where ${\mathbf{K}{(\mathbf{x}_{1:t},\mathbf{x}_{1:t})}_{i,j}} = {k{(\mathbf{x}_{i},\mathbf{x}_{j})}}$ serves as the covariance matrix. A common choice of $k$ is the squared exponential function (see Definition 7 on page 7), but many other choices are possible depending on our degree of belief about the smoothness of the objective function.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Bayesian Optimization", "weight": 1.0} -->

An advantage of using GPs lies in their analytical tractability.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Bayesian Optimization", "weight": 1.0} -->

That is, we can compute the posterior predictive mean $\mu{( \cdot )}$ and variance $\sigma{( \cdot )}$ exactly for any point $\mathbf{x}^{\ast}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Bayesian Optimization", "weight": 1.0} -->

At each iteration of Bayesian optimization, one has to re-compute the predictive mean and variance. These two quantities are used to construct the second ingredient of Bayesian optimization: The acquisition function. In this work, we report results for the expected improvement acquisition function (?, ?, ?):

<!-- chunk {"id": "body-0023", "role": "body", "section": "Bayesian Optimization", "weight": 1.0} -->

Note that this utility favors the selection of points with high variance (points in regions not well explored) and points with high mean value (points worth exploiting). We also experimented with the UCB acquisition function (?, ?) and found it to yield similar results. The optimization of the closed-form acquisition function can be carried out by off-the-shelf numerical optimization procedures, such as DIRECT (?) and CMA-ES (?); it is only based on the GP model of the blackbox function $f$ and does not require additional evaluations of $f$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Bayesian Optimization", "weight": 1.0} -->

The Bayesian optimization procedure is shown in Algorithm 1.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Bayesian Optimization", "weight": 1.0} -->

3: Find xt + 1 ∈ ℝD by optimizing the acquisition function u: xt + 1 = arg max x ∈ 𝒳u (x|𝒟t).
4: Augment the data 𝒟t + 1 = 𝒟t ∪ {(xt + 1,f (xt + 1))}.
5: Update the kernel hyper-parameters.
Algorithm 1 Bayesian Optimization

<!-- chunk {"id": "body-0026", "role": "body", "section": "Random Embedding for Bayesian Optimization", "weight": 1.0} -->

Before introducing our new algorithm and its theoretical properties, we need to define what we mean by effective dimensionality formally.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Increasing the Success Rate of REMBO", "weight": 1.0} -->

Theorem 3 only guarantees that $\mathcal{Y}$ contains the optimum with probability at least $1 - \epsilon$; with probability $\delta \leq \epsilon$ the optimizer lies outside of $\mathcal{Y}$. There are several ways to guard against this problem. One is to simply run REMBO multiple times with different independently drawn random embeddings. Since the probability of failure with each embedding is $\delta$, the probability of the optimizer not being included in the considered space of $k$ independently drawn embeddings is $\delta^{k}$. Thus, the failure probability vanishes exponentially quickly in the number of REMBO runs, $k$. Note also that these independent runs can be trivially parallelized to harness the power of modern multi-core machines and large compute clusters.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Increasing the Success Rate of REMBO", "weight": 1.0} -->

Another way of increasing REMBO's success rate is to increase the dimensionality $d$ it uses internally. When $d > d_{e}$, with probability $1$ we have $\binom{d}{d_{e}}$ different embeddings of dimensionality $d_{e}$. That is, we only need to select $d_{e}$ columns of $\mathbf{A} \in {\mathbb{R}}^{D \times d}$ to represent the $d_{e}$ relevant dimensions of $\mathbf{x}$. The algorithm can achieve this by setting the remaining $d - d_{e}$ sub-components of the $d$-dimensional vector $\mathbf{y}$ to zero. Informally, since we have more embeddings, it is more likely that one of these will include the optimizer. In our experiments, we will assess the merits and shortcomings of these two strategies.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Choice of Kernel", "weight": 1.0} -->

Since REMBO uses GP-based Bayesian optimization to search in the region $\mathcal{Y} \subset {\mathbb{R}}^{d}$, we need to define a kernel between two points ${\mathbf{y}^{},\mathbf{y}^{}} \in \mathcal{Y}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Hyper-parameter Optimization", "weight": 1.0} -->

0: Upper and lower bounds U &gt; L &gt; 0 for hyper-parameter.
0: Initial length scale hyper-parameter ℓ ∈ [L, U].
3: Find xt + 1 by optimizing the acquisition function u: xt + 1 = arg max x ∈ 𝒳u (x|𝒟t).
4: if $\sqrt{\sigma^{2}{(\mathbf{x}_{t + 1})}} &lt; t_{\sigma}$ then
9: Augment the data 𝒟t + 1 = {𝒟t, (xt + 1,f (xt + 1))}
15: Learn the hyper-parameter by optimizing the log marginal likelihood by using DIRECT and CMA-ES: ℓ = arg max l ∈ [L, U]log p (f1: t + 1|x1: t + 1,l)
Algorithm 3 Bayesian Optimization with Hyper-parameter Optimization.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Hyper-parameter Optimization", "weight": 1.0} -->

For Bayesian optimization (and therefore REMBO), it is difficult to manually estimate the true length scale hyper-parameter of a problem at hand. To avoid any manual steps and to achieve robust performance across diverse sets of objective functions, in this paper we adopted an adaptive hyper-parameter optimization scheme. The length scale of GPs is often set by maximizing marginal likelihood (?, ?). However, as demonstrated by ? (?), this approach, when implemented naively, may not guarantee convergence. This is not only true of approaches that maximize the marginal likelihood, but also of approaches that rely on Monte Carlo sampling from the posterior distribution (?, ?) when the number of data is very small, unless the prior is very informative.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Hyper-parameter Optimization", "weight": 1.0} -->

Here, we propose to optimize the length scale parameter $\ell$ by maximizing the marginal likelihood subject to an upper bound $U$ which is decreased when the algorithm starts exploiting too much. Full details are given in Algorithm 3. We say that the algorithm is exploiting when the standard deviation at the maximizer of the acquisition function $\sqrt{\sigma{(\mathbf{x}_{t + 1})}}$ is less than some threshold $t_{\sigma}$ for $5$ consecutive iterations. Intuitively, this means that the algorithm did not emphasize exploration (searching in new parts of the space, where the predictive uncertainty is high) for $5$ consecutive iterations. When this criterion is met, the algorithm decreases its upper bound $U$ multiplicatively and re-optimizes the hyper-parameter subject to the new bound. Even when the criterion is not met the hyper-parameter is re-optimized every $20$ iterations. For each optimization of the acquisition function, the algorithm runs both DIRECT (?) and CMA-ES (?) and uses the result of the best of the two options.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Hyper-parameter Optimization", "weight": 1.0} -->

The astute reader may wonder about the difficulty of optimizing the acquisition functions. For REMBO, however, we have not found the optimization of the acquisition function to be a problem since we only need to optimize it in the low-dimensional space and our acquisition function evaluations are cheap, allowing us tens of thousands of evaluations in seconds that (empirically) suffice to cover the low-dimensional space well.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Hyper-parameter Optimization", "weight": 1.0} -->

The motivation of this algorithm is to rather err on the side of having too small a length scale: given a squared exponential kernel $k_{\ell}$, with a smaller length scale than another kernel $k$, one can show that any function $f$ in the RKHS characterized by $k$ is also an element of the RKHS characterized by $k_{\ell}$. Thus, when running expected improvement, one can safely use $k_{\ell}$ instead of $k$ as the kernel of the GP and still preserve convergence (?). We argue that (with a small enough lower bound $L$) the algorithm would eventually reduce the upper bound enough to allow convergence. Also, the algorithm would not explore indefinitely as $L$ is required to be positive. In our experiments, we set the initial constraint $\lbrack L,U\rbrack$ to be $\lbrack 0.01,50\rbrack$ and set $t_{\sigma} = 0.002$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Hyper-parameter Optimization", "weight": 1.0} -->

We want to stress the fact that the above argument is only known to hold for a class of kernels over continuous domains (e.g. squared exponential and Matérn class kernels). Although we believe that a similar argument could be made for integer and categorical kernels, rigorous arguments concerning convergence under these kernels remain a challenge in Bayesian optimization.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

We now study REMBO empirically. We first use synthetic functions of small intrinsic dimensionality $d_{e} = 2$ but extrinsic dimension $D$ up to $1$ billion to demonstrate REMBO's independence of $D$. Then, we apply REMBO to automatically optimize the 47 parameters of a widely-used mixed integer linear programming solver and demonstrate that it achieves state-of-the-art performance. However, we also warn against the blind application of REMBO. To illustrate this, we study REMBO's performance for tuning the 14 parameters of a random forest body part classifier used by Kinect. In this application, all the $D = 14$ parameters appear to be important, and while REMBO (based on $d = 3$) finds reasonable solutions (better than random search and comparable to what domain experts achieve), standard Bayesian optimization can outperform REMBO (and the domain experts) in such moderate-dimensional spaces. More optimistically, this random forest tuning application shows that REMBO does not fail catastrophically when it is not clear that the optimization problem has low effective dimensionality.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

For all our experiments, we used a single robust version of REMBO that automatically sets its GP's length scale parameter as described in Section 3.3. The code for REMBO, as well as all data used in our experiments is publicly available at

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Some of our experiments required substantial computational resources, with the computational expense of each experiment depending mostly on the cost of evaluating the respective black-box function. While the synthetic experiments in Section 4.2 only required minutes for each run of each method, optimizing the mixed integer programming solver in Section 4.4 required 4-5 hours per run, and optimizing the random forest classifier in Section 4.5 required 4-5 days per run. In total, we used over half a year of CPU time for the experiments in this paper. In the first two experiments, we study the effect of our two methods for increasing REMBO's success rate (see Section 3.1) by running different numbers of independent REMBO runs with different settings of its internal dimensionality $d$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Bayesian Optimization in a Billion Dimensions", "weight": 1.0} -->

The experiments in this section employ a standard $d_{e} = 2$-dimensional benchmark function for Bayesian optimization, embedded in a $D$-dimensional space. That is, we add $D - 2$ additional dimensions which do not affect the function at all. More precisely, the function whose optimum we seek is ${f{(\mathbf{x}_{1:D})}} = {g{(x_{i},x_{j})}}$, where $g$ is the Branin function

<!-- chunk {"id": "body-0040", "role": "body", "section": "Bayesian Optimization in a Billion Dimensions", "weight": 1.0} -->

and where $i$ and $j$ are selected once using a random permutation. To measure the performance of each optimization method, we used the *optimality gap*: the difference of the best function value it found and the optimal function value.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Bayesian Optimization in a Billion Dimensions", "weight": 1.0} -->

We evaluate REMBO using a fixed budget of $500$ function evaluations that is spread across multiple interleaved runs --- for example, when using $k = 4$ interleaved REMBO runs, each of them was only allowed $125$ function evaluations. We study the choices of $k$ and $d$ by considering several combinations of these values. The results in Table 1 demonstrate that interleaved runs helped improve REMBO's performance. We note that in 13/50 REMBO runs, the global optimum was indeed not contained in the box $\mathcal{Y}$ REMBO searched with $d = 2$; this is the reason for the poor mean performance of REMBO with $d = 2$ and $k = 1$. However, the remaining $37$ runs performed very well, and REMBO thus performed well when using multiple interleaved runs: with a failure rate of 13/50=0.26 per independent run, the failure rate using $k = 4$ interleaved runs is only $0.26^{4} \approx 0.005$. One could easily achieve an arbitrarily small failure rate by using many independent parallel runs.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Bayesian Optimization in a Billion Dimensions", "weight": 1.0} -->

Using a larger $d$ is also effective in increasing the probability of the optimizer falling into REMBO's box $\mathcal{Y}$ but at the same time slows down REMBO's convergence (such that interleaving several short runs loses its effectiveness).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Bayesian Optimization in a Billion Dimensions", "weight": 1.0} -->

Next, we compared REMBO to standard Bayesian optimization (BO) and to random search, for an extrinsic dimensionality of $D = 25$. Standard BO is well known to perform well in low dimensions, but to degrade above a tipping point of about 15-20 dimensions. Our results for $D = 25$ (see Figure 4, left) confirm that BO performed rather poorly just above this critical dimensionality (merely tying with random search). REMBO, on the other hand, still performed very well in 25 dimensions.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Bayesian Optimization in a Billion Dimensions", "weight": 1.0} -->

One important advantage of REMBO is that --- in contrast to the approach of ? (?) --- it does not require the effective dimension to be coordinate aligned. To demonstrate this fact empirically, we rotated the embedded Branin function by an orthogonal rotation matrix $\mathbf{R} \in {\mathbb{R}}^{D \times D}$. That is, we replaced $f{(\mathbf{x})}$ by $f{({\mathbf{R}\mathbf{x}})}$. Figure 4 (middle) shows that REMBO's performance is not affected by this rotation.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Bayesian Optimization in a Billion Dimensions", "weight": 1.0} -->

Finally, since REMBO is independent of the extrinsic dimensionality $D$ as long as the intrinsic dimensionality $d_{e}$ is small, it performed just as well in $D = 1\, 000\, 000\, 000$ dimensions (see Figure 4, right). To the best of our knowledge, the only other existing method that can be run in such high dimensionality is random search.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Bayesian Optimization in a Billion Dimensions", "weight": 1.0} -->

For reference, we also evaluated the method of ? (?) for these functions, confirming that it does not handle rotation gracefully: while it performed best in the non-rotated case for $D = 25$, it performed worst in the rotated case. It could not be used efficiently for more than $D = {1,000}$. Based on a Mann-Whitney U test with Bonferroni multiple-test correction, all performance differences were statistically significant, except Random vs. standard BO. Finally, comparing REMBO to the method of ? (?), we also note that REMBO is much simpler to implement and that its results are very reliable (with interleaved runs).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Synthetic Discrete Experiment", "weight": 1.0} -->

In this section, we test the high-dimensional kernel with a synthetic experiment. Specifically, we again optimize the Branin function, but restrict its domain to $225$ discrete points on a regular grid. As above, we added $23$ additional irrelevant dimensions to make the problem 25-dimensional in total.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Synthetic Discrete Experiment", "weight": 1.0} -->

We used a small fixed budget of $100$ function evaluations for all algorithms involved as the problem would require no more than $225$ evaluations to be solved completely. We used $k = 4$ interleaved runs for REMBO. We again compare REMBO to random search and standard BO. For REMBO, we use the high-dimensional kernel to handle the discrete nature of the problem. The result of the comparison is summarized in Figure 5. Standard BO again suffered from the high extrinsic dimensionality and performed slightly worse than random search. REMBO, on the other hand, performed well in this setting.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Automatic Configuration of a Mixed Integer Linear Programming Solver", "weight": 1.0} -->

State-of-the-art algorithms for solving hard computational problems tend to parameterize several design choices in order to allow a customization of the algorithm to new problem domains. Automated methods for algorithm configuration have recently demonstrated that substantial performance gains of state-of-the-art algorithms can be achieved in a fully automated fashion (?, ?, ?, ?, ?, ?). These successes have led to a paradigm shift in algorithm development towards the active design of highly parameterized frameworks that can be automatically customized to particular problem domains using optimization (?, ?, ?). The resulting algorithm configuration problems have been shown to have low dimensionality (?), and here, we demonstrate that REMBO can exploit this low dimensionality even in the discrete spaces typically encountered in algorithm configuration. We use a configuration problem obtained from ? (?), aiming to configure the 40 binary and 7 categorical parameters of lpsolve (?), a popular mixed integer programming (MIP) solver that has been downloaded over 40 000 times in the last year.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Automatic Configuration of a Mixed Integer Linear Programming Solver", "weight": 1.0} -->

The objective is to minimize the optimality gap lpsolve can obtain in a time limit of five seconds for a MIP encoding of a wildlife corridor problem from computational sustainability (?). Algorithm configuration usually aims to improve performance for a representative set of problem instances, and effective methods need to solve two orthogonal problems: searching the parameter space effectively and deciding how many instances to use in each evaluation (to trade off computational overhead and over-fitting). Our contribution is for the first of these problems; to focus on how effectively the different methods search the parameter space, we only consider configuration on a single problem instance.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Automatic Configuration of a Mixed Integer Linear Programming Solver", "weight": 1.0} -->

Due to the discrete nature of this optimization problem, we could only apply REMBO using the high-dimensional kernel for categorical variables $k_{\lambda}^{D}{(\mathbf{y}^{},\mathbf{y}^{})}$ described in Section 3.2. While we have not proven any theoretical guarantees for discrete optimization problems, REMBO appears to effectively exploit the low effective dimensionality of at least this particular optimization problem.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Automatic Configuration of a Mixed Integer Linear Programming Solver", "weight": 1.0} -->

As in the synthetic experiment, REMBO's performance could be further improved by using multiple interleaved runs. However, as shown by ? (?), multiple independent runs can also improve the performance of SMAC and especially ParamILS. Thus, to be fair, we re-evaluated all approaches using interleaved runs. Figure 6 (right) shows that ParamILS and REMBO benefitted most from interleaving $k = 4$ runs. However, the statistical test results did not change, still showing that SMAC and REMBO outperformed Random and BO, with no other significant performance differences.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Automatic Configuration of Random Forest Kinect Body Part Classifier", "weight": 1.0} -->

We now evaluate REMBO's performance for optimizing the 14 parameters of a random forest body part classifier. This classifier closely follows the proprietary system used in the Microsoft Kinect (?) and is available at

<!-- chunk {"id": "body-0054", "role": "body", "section": "Automatic Configuration of Random Forest Kinect Body Part Classifier", "weight": 1.0} -->

We begin by describing some details of the dataset and classifier in order to build intuition for the objective function and the parameters being optimized. The data we used consists of pairs of depth images and ground truth body part labels. Specifically, we used 1 500 pairs of 320x240 resolution depth and body part images, each of which was synthesized from a random pose of the CMU mocap dataset. Depth, ground truth body parts and predicted body parts (as predicted by the classifier described below) are visualized for one pose in Figure 7 (left). There are 19 body parts plus one background class. For each of these 20 possible labels, the training data contained 25 000 pixels, randomly selected from 500 training images. Both validation and test data contained *all* pixels in the 500 validation and test images, respectively.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Automatic Configuration of Random Forest Kinect Body Part Classifier", "weight": 1.0} -->

The random forest classifier is applied to one pixel $P$ at a time. At each node of each of its decision trees, it computes the depth difference between two pixels described by offsets from $P$ and compares this to a threshold. At training time, many possible pairs of offsets are generated at random, and the pair yielding highest information gain for the training data points is selected. Figure 7 (right) visualizes a potential feature for the pixel in the green box: it computes the depth difference between the pixels in the red box and the white box, specified by respective offsets u and v. At training time, u and v are drawn from two independent 2-dimensional Gaussian distributions, each of which is parameterized by its two mean parameters $\mu_{1}$ and $\mu_{2}$ and three covariance terms $\Sigma_{11}$, $\Sigma_{12}$, and $\Sigma_{22}$ ($\Sigma_{21} = \Sigma_{12}$ because of symmetry).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Automatic Configuration of Random Forest Kinect Body Part Classifier", "weight": 1.0} -->

These constitute 10 of the parameters that need to be optimized, with range for the mean components and for the covariance terms. Low covariance terms yield local features, while high terms yield global features. Next to these ten parameters, the random forest classifier has four other standard parameters, outlined in Table 2. It is well known in computer vision that many of the parameters described here are important. Much research has been devoted to identifying their best values, but results are dataset specific, without definitive general answers.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Automatic Configuration of Random Forest Kinect Body Part Classifier", "weight": 1.0} -->

Min. No. samples for non leaf nodes

<!-- chunk {"id": "body-0058", "role": "body", "section": "Automatic Configuration of Random Forest Kinect Body Part Classifier", "weight": 1.0} -->

Bootstrap for per tree sampling

<!-- chunk {"id": "body-0059", "role": "body", "section": "Automatic Configuration of Random Forest Kinect Body Part Classifier", "weight": 1.0} -->

The objective in optimizing these RF classifier parameters is to find a parameter setting that learns the best classifier in a given time budget of five minutes. To enable competitive performance in this short amount of time, at each node of the tree only a random subset of data points is considered. Also note that the above parameters do not include the number of trees $T$ in the random forest; since performance improves monotonically in $T$, we created as many trees as possible in the time budget. Trees are constructed depth first and returned in their current state when the time budget is exceeded. Using a fixed budget results in a subtle optimization problem because of the complex interactions between the various parameters (maximum depth, number of potential offsets, number of trees and accuracy).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Automatic Configuration of Random Forest Kinect Body Part Classifier", "weight": 1.0} -->

It is unclear a priori whether a low-dimensional subspace of these 14 interacting parameters exists that captures the classification accuracy of the resulting random forests. We performed large-scale computational experiments with REMBO, random search, and standard Bayesian optimization (BO) to study this question. In this experiment, we used the high-dimensional kernel for REMBO to avoid the potential over-exploration problems of the low-dimensional kernel described in Section 3.2. We believed that $D = 14$ dimensions would be small enough to avoid inefficiencies in fitting the GP in $D$ dimensions. This belief was confirmed by the observation that standard BO (which operates in $D = 14$ dimensions) performed well for this problem.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Automatic Configuration of Random Forest Kinect Body Part Classifier", "weight": 1.0} -->

We conclude that the parameter space of this RF classifier does not appear to have a clear low effective dimensionality; since the extrinsic dimensionality is only moderate, this leads REMBO to perform somewhat worse than standard Bayesian optimization, but it is still possible to achieve reasonable performance based on as little as $d = 3$ dimensions.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have demonstrated that it is possible to use random embeddings in Bayesian optimization to optimize functions of extremely high extrinsic dimensionality $D$ provided that they have low intrinsic dimensionality $d_{e}$. Moreover, our resulting REMBO algorithm is coordinate independent and it only requires a simple modification of the original Bayesian optimization algorithm; namely multiplication by a random matrix. We proved REMBO's independence of $D$ theoretically and empirically validated it by optimizing low-dimensional functions embedded in previously untenable extrinsic dimensionalities of up to $1$ billion. We also theoretically and empirically showed REMBO's rotational invariance. Finally, we demonstrated that REMBO achieves state-of-the-art performance for optimizing the 47 discrete parameters of a popular mixed integer programming solver, thereby providing further evidence for the observation (already put forward by Bergstra, Hutter and colleagues) that, for many problems of great practical interest, the number of important dimensions indeed appears to be much lower than their extrinsic dimensionality.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We note that the central idea of our work -- using an otherwise unmodified optimization procedure in a randomly embedded space -- in principle could be applied to arbitrary optimization procedures. Evaluating the effciency of this technique for other procedures is an interesting topic for future work.
