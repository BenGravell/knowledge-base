<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Why Random Reshuffling Beats Stochastic Gradient Descent

Topics include Gradient descent, Stochastic gradients, RR, Stochastic gradient descent.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We analyze the convergence rate of the random reshuffling (RR) method, which is a randomized first-order incremental algorithm for minimizing a finite sum of convex component functions. RR proceeds in cycles, picking a uniformly random order (permutation) and processing the component functions one at a time according to this order, i.e., at each cycle, each component function is sampled without replacement from the collection. Though RR has been numerically observed to outperform its with-replacement counterpart stochastic gradient descent (SGD), characterization of its convergence rate has been a long standing open question. In this paper, we answer this question by showing that when the component functions are quadratics or smooth and the sum function is strongly convex, RR with iterate averaging and a diminishing stepsize alpha_k = Theta(1/k^(s)) for s in (1/2, 1) converges at rate Theta(1/k^s) with probability one in the suboptimality of the objective value, thus improving upon the Omega(1/k) rate of SGD.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our analysis draws on the theory of Polyak-Ruppert averaging and relies on decoupling the dependent cycle gradient error into an independent term over cycles and another term dominated by alpha_k^. This allows us to apply law of large numbers to an appropriately weighted version of the cycle gradient errors, where the weights depend on the stepsize. We also provide high probability convergence rate estimates that shows decay rate of different terms and allows us to propose a modification of RR with convergence rate O(1/k^).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction: First-order incremental methods", "weight": 1.5} -->

with $f_{i}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$. This problem arises in many contexts and applications including regression or more generally parameter estimation problems (where $f_{i}{(x)}$ is the loss function representing the error between the output and the prediction of a parametric model), minimization of an expected value of a function (where the expectation is taken over a finite probability distribution or approximated by an $m$-sample average), machine learning, or distributed optimization over networks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction: First-order incremental methods", "weight": 1.5} -->

One widely studied approach for solving problem is the deterministic incremental gradient (IG) method. IG method is similar to the standard gradient method with the key difference that at each iteration, the decision vector is updated incrementally by taking sequential steps along the gradient of the component functions $f_{i}$ in a cyclic order. Hence, we can view each outer iteration $k$ as a cycle of $m$ inner iterations: starting from initial point $x_{0}^{0} \in {\mathbb{R}}^{n}$, for each $k \geq 0$, we update the iterate $x_{i}^{k}$ as

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction: First-order incremental methods", "weight": 1.5} -->

Intuitively, it is clear that slow progress can be obtained if the functions that are processed consecutively have gradients close to zero. Indeed, the performance of IG is known to be pretty sensitive to the order functions are processed \[6, Example 2.1.3\].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction: First-order incremental methods", "weight": 1.5} -->

However, in general a favorable order is not known in advance, and a common approach is choosing the indices of functions to process as independent and uniformly distributed samples from the set $\{ 1,2,\ldots,m\}$. This way no particular order is favored, making the method less vulnerable to particularly bad orders. This approach amounts to at each iteration sampling the function indices with replacement from the set $\{ 1,2,\ldots,m\}$ and is called the Stochastic Gradient Descent (SGD) method, a.k.a. Robbins-Monro algorithm. SGD is strongly related to the classical field of stochastic approximation. Recently it has received a lot of attention due to its applicability to large-scale problems and became popular especially in machine learning applications (see e.g. ).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction: First-order incremental methods", "weight": 1.5} -->

An alternative popular approach that works well in practice is following a mixed approach between SGD and IG, sampling the functions randomly but not allowing repetitions, that is sampling the component functions at each iteration without-replacement, or equivalently picking a random order at each cycle. Specifically, at each cycle $k$, we draw a permutation $\sigma_{k}$ of $\{ 1,2,\ldots,m\}$ independently and uniformly at random over the set of all permutations

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction: First-order incremental methods", "weight": 1.5} -->

where $\alpha_{k} > 0$ is a stepsize. We set $x_{0}^{k + 1} = x_{m}^{k}$ as before and refer to $\{ x_{0}^{k}\}$ as the outer iterates. This method is called the Random Reshuffling (RR) method \[6, Section 2.1\] and will be the focus of this paper.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Motivation and summary of contributions", "weight": 1.0} -->

Without-replacement sampling schemes are often easier to implement efficiently compared to with-replacement sampling schemes, guarantee that every point in the data set is touched at least once, and often have better practical performance than their with-replacement counterparts. For instance, Bottou empirically compares SGD and RR methods and finds that RR converges with a rate close to $\sim {1/k^{2}}$ whereas SGD is much slower achieving its min-max lower bound of $\Omega{({1/k})}$ for strongly convex objective functions. Many other papers listed above report a similar empirical behavior. This discrepancy in rate between RR and SGD is not only observed for large $m$ but also for small $m$ (as we illustrate in Example 3.2), and understanding it theoretically has been a long-standing open problem.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Motivation and summary of contributions", "weight": 1.0} -->

To our knowledge, the only existing theoretical analysis for RR is given by a recent paper of Recht and Ré which focuses on least mean squared optimization and formulates a conjecture that would prove that the expected convergence rate of RR is faster than that of SGD. Given $N$ arbitrary positive-definite matrices of dimension $n \times n$, the conjecture says that products of any $K$ matrices chosen from this set of $N$ matrices satisfy a non-commutative arithmetic-geometric mean inequality for every positive integer $N$ and every $K \leq N$. This conjecture has been proven only in some special cases (for $N = 2$, for $N = 3$ and when $N$ is a multiple of 3 and $K = 3$ ).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Motivation and summary of contributions", "weight": 1.0} -->

Recht and Ré also analyze a special case of (that arises when ${f_{i}{(x)}} = {({{a_{i}^{T}x} - y_{i}})}^{2}$ is a quadratic function where $a_{i}$ is a column vector that is randomly generated according to a random model and $y_{i}$ is a scalar) and show that after a fixed amount of iterations, the upper bounds on the expected mean square error using without-replacement sampling is smaller than that of with-replacement sampling with high probability on most models of $a_{i}$ (probabilities are taken with respect to the random data generation model). Despite these advances, there has been a lack of convergence theory for RR that characterizes its convergence rate and explains its fast performance. Analyzing algorithms based on without-replacement sampling such as RR is more difficult than with-replacement based approaches such as SGD.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Motivation and summary of contributions", "weight": 1.0} -->

The reason is that the underlying independence assumption for the with-replacement sampling allows a tractable analysis with classical martingale convergence theory, whereas without-replacement sampling introduces correlations and dependencies among the sampled gradients and iterates that are harder to analyze. The aim of our paper is to fill this theoretical gap for the case when the objective function $f$ in is strongly convex and develop a novel algorithm that can accelerate the convergence further. We next summarize our contributions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Motivation and summary of contributions", "weight": 1.0} -->

We first consider the case when the component functions are quadratics. Building on the recent convergence rate results for the cyclic IG, we first present a key result (Theorem 20) that provides an upper bound for the distance from the optimal solution of the iterates generated by an incremental method that processes component functions with an arbitrary fixed order and uses a stepsize $\Theta{({1/k^{s}})}$ for $s \in {(0,1\rbrack}$. This upper bound decays at rate $\mathcal{O}{({1/k^{s}})}$ and depends on the strong convexity constant of the sum function and an order dependent parameter given by a weighted average of Hessian matrices where the weights are given by the sum of the component gradients processed up to that point according to the given order.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Motivation and summary of contributions", "weight": 1.0} -->

We use this result to show that the distance to the optimal solution of the iterates generated by RR algorithm with stepsize $\Theta{({1/k^{s}})}$, for all $s \in {(0,1\rbrack}$, converges to 0 at rate $\mathcal{O}{({1/k^{s}})}$ in expectation (where the expectation is over the random sequence of iterates). However, we show that achieving the rate $\mathcal{O}{({1/k})}$ involves adapting the stepsize to the strong convexity constant of the sum function.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Motivation and summary of contributions", "weight": 1.0} -->

We then consider the $q$-suffix averages of the iterates generated by RR for some $q \in {(0,1\rbrack}$ (which is obtained by averaging the last $qk$ iterates at iteration $k$) and show that with a stepsize $\alpha_{k} = {R/{({k + 1})}^{s}}$ for $s \in {({1/2},1)}$ and $R > 0$, they converge almost surely at rate $\mathcal{O}{({1/k^{s}})}$ to the optimal solution. We provide an explicit characterization of the asymptotic rate constant in terms of the averaging parameter $q$, the stepsize parameters $R$ and $s$ and the Hessian matrices and the gradients of the component functions at the optimal solution (parts $(i)$ and $({ii})$ of Theorem 3).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Motivation and summary of contributions", "weight": 1.0} -->

Using strong convexity, this implies an almost sure convergence rate $\Theta{({1/k^{2s}})}$ in the suboptimality of the objective value. Our analysis views RR as a gradient descent method with random gradient errors. The analysis of RR is complicated by the fact that the cumulative gradient error over cycles are dependent. A key step in our proof is to decouple the cycle gradient error into a $\mathcal{O}{(\alpha_{k})}$ term independent over cycles and another term that scales as $\mathcal{O}{(\alpha_{k}^{2})}$. This allows us to use strong law of large numbers for a properly weighted average of the cycle error gradient sequence (where the weights depend on the stepsize) and show almost sure convergence of the $q$-suffix averaged iterates. Another key component of our analysis is to adapt the Polyak-Ruppert averaging techniques developed for SGD to RR.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Motivation and summary of contributions", "weight": 1.0} -->

We also provide a high probability convergence rate estimate for the distance of $q$-suffix averages to the optimal solution that consists of two terms, with the first term corresponding to a $1/k^{s}$ decay of a "bias" term (where bias is defined as the expected value of the cycle gradient errors of RR which may be non-zero) and the second term representing a $1/k$ decay for $0 < q < 1$ (and $\log{k/k}$ decay for $q = 1$); see part $({iii})$ of Theorem 3. These results are obtained by martingale concentration techniques. We use the characterization of the bias to estimate it with a term that can be computed during the RR iterations. We show that subtracting the estimated bias from the averaged RR iterates accelerates the convergence rate further, leaving only the second error term of $1/k$ decay in the iterates (part $({iv})$ of Theorem 3).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Motivation and summary of contributions", "weight": 1.0} -->

Based on this result, we propose a new algorithm which we call the De-biased Random Reshuffling (DRR) method that can accelerate the asymptotic convergence rate of RR in the suboptimality of the function values from $\mathcal{O}{({1/k^{2s}})}$ to $\mathcal{O}{({1/k^{2}})}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Motivation and summary of contributions", "weight": 1.0} -->

Finally, in Theorem 4 we show that our results in Theorem 3 extend to the more general case when component functions are smooth (twice continuously differentiable) under a Lipschitz assumption on the Hessian, which allows us to control the second order term in a Taylor expansion of the gradient.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Motivation and summary of contributions", "weight": 1.0} -->

Outline: The outline of the paper is as follows. In Section 3, we introduce our approach for analyzing RR, present Polyak-Ruppert averaging and give a motivating example. Section 4 focuses on the case when component functions are quadratics. We first present a convergence rate estimate for IG with a fixed arbitrary order. We then focus on RR and study convergence of averaged iterates to the optimal solution. Section 5 extends our results to smooth functions. Section 6 proposes the DRR algorithm that can accelerate RR further. Finally, we conclude with a summary of our work in Section 7. Some of the technical lemmas required in the details of the proofs are deferred to Sections A, B and C of the Appendix.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Motivation and summary of contributions", "weight": 1.0} -->

Notation: We study the point-wise dominance of stochastic sequences by deterministic sequences and use the following notation. Let $x_{k} = {x_{k}{(\omega)}}$ be a stochastic real-valued sequence (where $\omega$ can be thought as the source of randomness) and $y_{k}$ be a real-valued deterministic sequence.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Motivation and summary of contributions", "weight": 1.0} -->

When $x_{k}$ is deterministic, these definitions reduce to the standard definitions of $\mathcal{O}{( \cdot )}$ and $o{( \cdot )}$ for deterministic sequences. For random $x_{k}$, the only difference is that we require the constants to be independent of the choice of $\omega$. For example, if $x_{k}$ is uniformly distributed over $\lbrack 0,10\rbrack$, we write $x_{k} = {\mathcal{O}{}}$. Throughout the paper, $\parallel \cdot \parallel$ denotes the vector or matrix 2-norm (maximum singular value).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

The sum function ${f{(x)}} = {\sum_{i = 1}^{m}{f_{i}{(x)}}}$ is strongly convex, i.e., there exists a constant $c > 0$ such that the function ${f{(x)}} - {\frac{c}{2}{\| x\|}^{2}}$ is convex on ${\mathbb{R}}^{n}$.^11^1Such functions arise naturally in support vector machines and other regularized learning algorithms or regression problems (see e.g. ).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

Note that this assumption is on the sum function $f$, it does not require the convexity of the individual component functions $f_{i}$. A consequence of this assumption is that there exists a unique optimal solution to which we denote by $x^{\ast}$. Another consequence is that the Hessian at the optimal solution is invertible since

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

where $I_{n}$ is the $n \times n$ identity matrix.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

To analyze RR, we view it as a gradient method with random gradient errors and rewrite the outer iterations as

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

is the cumulative gradient errors associated with the cycle $k$. This approach is similar to the analysis of SGD, where one writes each (inner) iteration as a gradient method with error. The key difference that simplifies the analysis of SGD is the fact that the iteration gradient errors at the current iterate are independent (because of independent identically distributed sampling of component function indices) allowing use of martingale central limit theorems to obtain convergence and rate results (see e.g. ). In contrast, for RR, not only are the iteration gradient errors dependent (because of sampling a random order at cycle $k$ coupling indices $\sigma_{k}{(i)}$ and $\sigma_{k}{(j)}$ for $i \neq j$), but also the cycle gradient errors $E_{k_{1}}$ and $E_{k_{2}}$ for cycles $k_{1} \neq k_{2}$ are dependent as they both depend on the history of the iterates.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

This necessitates a different line of attack for the convergence analysis of RR.^22^2There is some literature that analyzes SGD under correlated noise \[21, Ch. 6\], but the noise needs to have a special structure (such as a mixing property) which does not seem to be applicable to the analysis of RR.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

A key idea in our analysis is to use a recent upper bound for the convergence rate of cyclic incremental gradient method (see ), which can be generalized to hold for any fixed deterministic order. This bound implies an almost sure upper bound (in fact one that holds for all sample paths) on the distance of the outer iterates $x_{0}^{k}$ generated by RR from the optimal solution $x^{\ast}$ denoted by $\text{dist}_{k} = {\|{x_{0}^{k} - x^{\ast}}\|}$ (see Section 4.1). Crucially, this result implies an upper bound in expected distance which is asymptotically $m$ times smaller than the almost sure guarantees on the distance of the iterates.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

In analyzing RR, we will also consider the average of the outer iterate sequence given by^33^3It is well known that computing this (moving) average can be done efficiently in a dynamic manner by storing a vector of length $n$. ${{\overline{x}}_{k}:=\frac{\sum_{j = 0}^{k - 1}x_{0}^{j}}{k}}.$ We also consider averaging only the most recent iterates, i.e.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

The generated sequence is referred to as the $q$-suffix average of the sequence $x_{0}^{k}$. For SGD, it was shown that $q$-suffix averaging with $0 < q < 1$ leads to better performance then averaging (which corresponds to the $q = 1$ case by definition), improving the convergence rate in the suboptimality of the function value from $\log{k/k}$ to $1/k$. This is in line with our results in Section 4 which show faster rate for the $0 < q < 1$ case. The parameter $q$ can be thought as a measure of how much memory one uses during the averaging process.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

We will obtain our strongest convergence results (in the almost sure sense and with a similar $m$ dependence as the expected guarantees) for averaged iterate sequences with "large step sizes", a technique known as Polyak-Ruppert averaging, which has been used in achieving optimal rates for SGD in a robust manner as explained next.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Polyak-Ruppert averaging", "weight": 1.0} -->

SGD has a long history going back to the seminal paper of Robbins and Monro. It has been analyzed under different assumptions extensively in the stochastic approximation literature (see e.g. ). For stochastic convex optimization, it has been shown that SGD has a min-max lower bound of $\Omega{({1/k})}$. One way of achieving this optimal $1/k$ rate is to use a stepsize $\alpha_{k} = {R/k}$ where $R$ is a positive scalar adjusted properly to the strong convexity constant of the objective function but this requires the knowledge or the estimate of an accurate lower bound on the strong convexity constant. If a lower bound is not known or cannot be estimated accurately, the convergence can be potentially slow \[25, Section 2.1\]. Polyak-Ruppert averaging is a technique that allows to get the optimal $\sim {1/k}$ rate in an asymptotically efficient manner without the need to adjust to the strong convexity constant.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Polyak-Ruppert averaging", "weight": 1.0} -->

It relies on using a larger stepsize $\alpha_{k} = {R/k^{s}}$ (with $R$ an arbitrary positive constant and $s \in {({1/2},1)}$) that decays slower than $\Theta{({1/k})}$ but then taking the time average of the iterates to filter out the undesired oscillations arising due to the larger steps.^44^4IG shows similar properties to SGD in terms of the robustness of the stepsize rules $\alpha_{k} = {R/k^{s}}$. The convergence rate (in $k$) is only robust to the strong convexity constant of the objective for $s < 1$ but not for $s = 1$. We will later show that the same technique allows us to get almost sure guarantees for the averaged iterates without the need to tune the stepsize to the strong convexity constant (see Theorems 3 and 4).

<!-- chunk {"id": "body-0036", "role": "body", "section": "A motivating example", "weight": 1.0} -->

Before presenting our convergence analysis, we consider a simple example that highlights the difference in convergence mechanisms of SGD and RR and gives intuition on why RR is faster than SGD asymptotically.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

where the cycle gradient errors are given by

<!-- chunk {"id": "body-0038", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

In contrast, SGD starting from an initial point $y^{0}$ leads to the iterations

<!-- chunk {"id": "body-0039", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

where $i_{j}$ is an independent and identically distributed (i.i.d.) random variable with a uniform distribution over the index set $\{ 1,2\}$ and the gradient error $e^{j}$ is given by

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

We consider a stepsize of $\alpha_{k} = \frac{R}{k^{s}}$ with $s = 0.75$ for both algorithms.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

{2\alpha_{k}^{2}}})}\text{dist}_{k}} + {2\alpha_{k}^{2}}}}.$ Then, by invoking classical results for the asymptotic behavior of non-negative sequences (see e.g. \[6, Appendix A.4.3\], we get $\text{dist}_{k + 1}\rightarrow 0$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

Theorem 20 also shows global convergence of RR on this example. By a similar argument, it can be shown that SGD is also convergent to the optimal solution $x^{\ast} = 0$ in mean-square, i.e. ${{\mathbb{E}}{\| y^{j}\|}^{2}}\rightarrow 0$ (see also e.g. ).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

Then, it follows from and that the cumulative gradient error of SGD for any cycle $k$ (defined as the cumulative sum $\sum_{j = {{({k - 1})}m}}^{{km} - 1}e_{j})$) has zero expectation and $\Theta{}$ variance whereas the gradient errors in RR are $E_{k} = {\mathcal{O}{(\alpha_{k})}}$ with a typically non-zero expectation satisfying ${{\mathbb{E}}{(E_{k})}} = {\alpha_{k}{({1 - {2x_{0}^{k}}})}}$ and an asymptotically smaller variance $\mathcal{O}{(\alpha_{k}^{2})}$ compared to SGD. In other words, the cycle gradient errors go to zero with probability one for RR whereas the gradient errors in SGD are typically bounded away from zero with a positive probability.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

Informally, this leads to a more accurate direction of descent for RR and is the main reason behind the faster convergence we demonstrate for RR compared to SGD in our analysis.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

We also observe that the cycle gradient error $E_{k}$ given by consists of the sum of two terms: The first term is $\mathcal{O}{(\alpha_{k})}$ and is independent over the cycles as the permutations $\sigma_{k}$ are independent and identically distributed whereas the second term is of smaller (second) order as $x_{0}^{j}\rightarrow 0$. We will show later in Lemma B.4 that such a decomposition can be obtained more generally when component functions are quadratics or they are smooth functions and will be a key step in the proof of Theorem 3.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Quadratic component functions", "weight": 1.0} -->

We first consider quadratic component functions which allows an elegant analysis without the need to approximate higher order terms. We will show in Section 5 that the same line of analysis extends to smooth component function under a Lipschitz assumption on the Hessian matrices. Let $f_{i}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ be a quadratic function of the form

<!-- chunk {"id": "body-0047", "role": "body", "section": "Quadratic component functions", "weight": 1.0} -->

where $P_{i}$ is a symmetric $n \times n$ matrix, $q_{i} \in {\mathbb{R}}^{n}$ is a column vector and $r_{i}$ is a scalar. Note that $f_{i}$ has Lipschitz gradients, i.e.,

<!-- chunk {"id": "body-0048", "role": "body", "section": "Quadratic component functions", "weight": 1.0} -->

where $L_{i} = {\| P_{i}\|}$. It follows from the triangle inequality that $f$ has Lipschitz gradients with Lipschitz constant at most

<!-- chunk {"id": "body-0049", "role": "body", "section": "Convergence Rate", "weight": 1.0} -->

Our convergence analysis of RR builds on a recent upper bound for convergence rate of (deterministic) cyclic IG method (see ), which can be generalized to hold for any fixed permutation $\sigma$ of $\{ 1,2,\ldots,m\}$. This result implies an upper bound (for all sample paths) on the distance to the optimal solution of the iterates generated by RR, which is presented next.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

A consequence of Lemma B.3 proved in the Appendix is that

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

We obtain from that ${{\mathbb{E}}\left( \text{dist}_{k} \right)} = {{O{(\frac{1}{mk})}} + {o{({1/k})}}}$. Note that, the performance guarantee for IG from Corollary 4.1 is $\text{dist}_{k} = {{\mathcal{O}{({1/k})}} + {o{({1/k})}}}$ which is also worse than RR by a factor of $O{(m)}$. For a fair comparison with the SGD method, we consider running the SGD iterations for $j = {km}$ iterations so that both RR and SGD methods have access to the same number of component gradients.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

In this case, expected distance to suboptimality for SGD with the recommended $O{({1/j})}$ stepsize is $\mathcal{O}{(\frac{1}{\sqrt{j}})}$ where the hidden constants are independent of $m$ (see e.g. ) which is worse than the $\mathcal{O}{({1/j})}$ guarantees for RR when $j$ is sufficiently large. These bounds show that when $m$ is small and $k$ is large, IG could outperform SGD in theory, however SGD (and RR) are more suitable for applications when $m$ is large and will admit better bounds compared to IG if $m$ is large enough for a given $k$ fixed^77^7We note however that SGD upper bounds are in expectation whereas IG results are deterministic which is a stronger notion of convergence.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

It is also natural to ask what would happen to the rate constants and to the rate if one would take stepsize $\alpha_{k} = {\Theta{({1/k^{s}})}}$ and apply (Polyak-Ruppert) averaging to the RR iterates, especially given the fact that $\mathcal{O}{({1/k^{s}})}$ stepsize used in averaging does not require adjustment of the parameter $R$ to the strong convexity level. More generally, one could consider $q$-suffix averaging. In the next section, we show that for the averaged RR iterates, similar upper bounds in hold not only in expectation but also in probability. Another benefit of averaging is that it leads to not only upper bounds but also lower bounds which can then be leveraged to accelerate RR further as we will show in Section 6.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Convergence rate with averaging", "weight": 1.0} -->

The following theorem characterizes the rate of convergence of the averages of iterates generated by RR. Part $(i)$ and $({ii})$ of this theorem show that $q$-suffix averages of the RR iterates converge at rate $1/k^{s}$ to the optimal solution almost surely with a stepsize $\Theta{({1/k^{s}})}$ for $s \in {({1/2},1)}$. By gradient Lipschitzness, this translates into a rate of $\Theta{({1/k^{2s}})}$ for the suboptimality of the objective value. The result is based on decoupling the cycle gradient errors $E_{k}$ into a $\Theta{(\alpha_{k})}$ term independent over the cycles and another $\mathcal{O}{(\alpha_{k}^{2})}$ term that becomes negligible in the limit.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Convergence rate with averaging", "weight": 1.0} -->

Part $({iii})$ is a high-probability convergence rate estimate for the approximation error ${\overline{x}}_{q,k} - x^{\ast}$. The approximation error consists of two terms, the first term $b_{q,k}$ which we call the "bias" term is deterministic and decays like $\sim {1/k^{s}}$. It comes from the expected value of the independent part of the gradient cycle errors which may be different than zero. The second part is on the order of $1/k$ for $0 < q < 1$ (and $\log{k/k}$ when $q = 1$) and it is based on the Azuma-Hoeffding inequality for martingale concentration. Finally, part $({iv})$ is on estimating the bias term $b_{q,k}$ with another quantity ${\hat{b}}_{q,k}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Convergence rate with averaging", "weight": 1.0} -->

It shows that by subtracting the estimated bias from the averaged iterates, we can approximate the optimal solution $x^{\ast}$ up to an $\mathcal{O}{({1/k})}$ error in distances or equivalently up to an $\mathcal{O}{({1/k^{2}})}$ error in the suboptimality of the objective value. In Section 6, this result will be fundamental for Algorithm 1 that accelerates the convergence of RR from $\Theta{({1/k^{2s}})}$ to $\mathcal{O}{({1/k^{2}})}$ with high probability in the suboptimality of the objective value.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Extension to smooth component functions", "weight": 1.0} -->

Extending our results to more general smooth functions requires obtaining similar bounds for the cycle gradient errors which depend on the gradients and Hessian matrices of the component functions along the inner iterates. In order to be able to control the change of gradients and Hessian matrices along the iterates, we introduce the following assumption which has also been used to analyze SGD.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Assumption 5.1", "weight": 1.0} -->

The functions $f_{i}$ are convex on ${\mathbb{R}}^{n}$ and have Lipschitz continuous second derivatives, i.e. there exists a constant $U_{i}$ such that

<!-- chunk {"id": "body-0059", "role": "body", "section": "Assumption 5.1", "weight": 1.0} -->

Under this assumption, by the triangle inequality, ${\nabla^{2}f}{( \cdot )}$ is also Lipschitz with constant ${U:={\sum_{i = 1}^{m}U_{i}}}.$ When the component functions are quadratics, we have the special case with $U = U_{i} = 0$. We will now see how this assumption makes it possible to control the change of gradients of the component functions. Smooth functions $f$ with Lipschitz Hessians are quadratic-like in the sense that the first-order Taylor approximation to the gradient of $f$ is almost affine (with a quadratic term controlled by the parameter $U$) satisfying

<!-- chunk {"id": "body-0060", "role": "body", "section": "Assumption 5.1", "weight": 1.0} -->

(see e.g. \[18, Section 1.3\]) The analysis of Theorem 3 (and Lemma B.4 it builds upon) considers the $U = 0$ case (see e.g. (36 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")) and (48 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent"))) applying a first-order Taylor approximation to the gradient of the component functions at $x = x_{0}^{k}$ where ${\|{x - x^{\ast}}\|} = {\|{x_{0}^{k} - x^{\ast}}\|} = {\mathcal{O}{(\alpha_{k})}}$ by Lemma B.1.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Assumption 5.1", "weight": 1.0} -->

Therefore, when $U \neq 0$, an extra correction term $\eta = {\mathcal{O}{(\alpha_{k}^{2})}}$ needs to be added to the analysis. However, we show in the next theorem that this correction term does not cause a slow down in the convergence rate (in terms of dependency in $k$) compared to the quadratic case because the $q$-suffix averages of this $\mathcal{O}{(\alpha_{k}^{2})}$ correction term decays like $\mathcal{O}{({1/k})}$.^88^8This is due to the fact that the sequence $\alpha_{k}^{2}$ is summable when $s > {1/2}$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Assumption 5.1", "weight": 1.0} -->

We will also need one more technical assumption that appeared in a number of papers in the literature for analyzing incremental methods to rule out the case that the iterates diverge to infinity. In particular, this assumption is made in for generalizing Theorem 20 on the rate of deterministic IG from quadratic functions to general smooth functions which we will be referring to.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Assumption 5.2", "weight": 1.0} -->

Iterates ${\{ x_{j}^{k}\}}_{j,k}$ generated are uniformly bounded, i.e. there exists a non-empty compact Euclidean ball $\mathcal{X} \subset {\mathbb{R}}^{n}$ that contains all the iterates a.s.^99^9Note that if this assumption holds and if $f_{i}$ is three-times continuously differentiable on the compact set $\mathcal{X}$, then the third-order derivatives are bounded and Assumption 5.1 holds.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Assumption 5.2", "weight": 1.0} -->

Equipped with these two assumptions, all the results of Theorem 3 extend naturally with minor modifications. In particular, $P_{i}$ (which is a constant Hessian matrix in the setting of Theorem 3) needs to be replaced by ${\nabla^{2}f_{i}}{(x^{\ast})}$ or ${\nabla^{2}f_{i}}{(x_{i - 1}^{k})}$ depending on the context.

<!-- chunk {"id": "body-0065", "role": "body", "section": "An RR algorithm with bias removal", "weight": 1.0} -->

Part $({iii})$ of Theorem 4 (see also part $({iii})$ of Theorem 3) shows that if the estimate of the bias term ${\hat{r}}_{q,k}$ given by (51 ‣ Theorem 4. ‣ 5 Extension to smooth component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")) is subtracted from the $q$-suffix averaged RS iterates, then the distance to the optimal solution of the $q$-suffix averaged iterates becomes on the order of $\mathcal{O}{({1/k})}$ for $0 < q < 1$ and on the order of $\mathcal{O}{({\log{k/k}})}$ for $q = 1$ with high probability.

<!-- chunk {"id": "body-0066", "role": "body", "section": "An RR algorithm with bias removal", "weight": 1.0} -->

By strong convexity, this translates into a rate of $\overset{\sim}{\mathcal{O}}{({1/k^{2}})}$ in the suboptimality of the objective values (where $\overset{\sim}{\mathcal{O}}$ ignores the logarithmic terms in $k$ appearing when $q = 1$.). We call this "subtraction operation", bias removal. Algorithm DRR describes how this can be implemented. In a practical implementation, the number of cycles can be fixed in advance to a certain number $K$, and the estimation of the bias can be done only once at the last ($K$-th) cycle (see Step $({ii})$ of Algorithm 1) and then can be subtracted from the averaged iterates.

<!-- chunk {"id": "body-0067", "role": "body", "section": "An RR algorithm with bias removal", "weight": 1.0} -->

Input: Initial point x00 ∈ ℝn, number of cycles K ∈ ℕ, suffix averaging parameter q ∈ (0, 1], stepsize parameters R &gt; 0 and s ∈ (1/2,1).
Initialization: ${\overline{x}}_{1,0} = 0 \in {\mathbb{R}}^{n}$, v̂0 = 0 ∈ ℝn, ${\overline{\alpha}}_{1,0} = 0 \in {\mathbb{R}}$, Ĥ0 = 0 ∈ ℝn × n.

<!-- chunk {"id": "body-0068", "role": "body", "section": "An RR algorithm with bias removal", "weight": 1.0} -->

Output: ${\overline{x}}_{q,K} - {\hat{b}}_{q,K}$.
Algorithm 1 De-biased Random Reshuffling (DRR)

<!-- chunk {"id": "body-0069", "role": "body", "section": "An RR algorithm with bias removal", "weight": 1.0} -->

The bias removal of the DRR algorithm requires an $n \times n$ matrix inversion which requires $\approx n^{3}$ arithmetic operations (if there is more structure on the Hessian of $f_{i}$ such as low-rankness or sparsity this could be improved to $\approx n^{2}$), but accelerates the convergence with high-probability. For small or moderate $n$, this could be done efficiently and incrementally processing the functions one at a time; however for large $n$ this may be impractical or infeasible limiting the applicability of this method. Nevertheless, the expensive matrix inversion step does not need to be done at every cycle, it suffices to do it only once at the end of the last cycle. Figure 3 compares the performance of SGD, RR and DRR methods in terms of the histogram of the distance to the optimal solution (left panel) and suboptimality of the objective function (right panel) on a randomly generated quadratic example with a dense Hessian matrix with parameters $m = 50$, $n = 20$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "An RR algorithm with bias removal", "weight": 1.0} -->

For a fair comparison, we run all the algorithms with the same amount of CPU time. In particular, in Figure 3 we run DRR for 0.5 seconds including the bias correction step, and run RR and SGD for the same amount of time. We observe that SGD is consistently performing the worst, whereas DRR leads often to a better solution than RR both in terms of distances to the optimal solution and suboptimality. Figure 3 repeats the experiment with 5 seconds, we see a clearer separation between the histograms of the RR method and the De-biased RR method. We see similar results when we run the algorithms for different amount of times. These results show that the asymptotic performance would get better if one removes the bias term and typically we need more cycles for the bias correction term to be effective. The results also illustrate the results of Theorem 3 and 4 on the biasedness of the RR iterations in the sense that asymptotically an improvement can be obtained by subtracting the bias.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We analyzed the random reshuffling (RR) method for minimizing a finite sum of convex component functions. When the objective function is strongly convex and the component functions are smooth, averaged RR iterates converge at rate $\sim {1/k^{s}}$ to the optimal solution almost surely (which translates into a rate of $1/k^{2s}$ in the suboptimality of the objective value) for a diminishing stepsize $\alpha_{k} = {\Theta{({1/k^{s}})}}$ with $s \in {({1/2},1)}$. This is faster than SGD's $\Omega{(\frac{1}{k})}$ rate. Viewing RR as a gradient descent method with random gradient errors, this result builds on first showing that gradient errors $E_{k}$ satisfying $E_{k} = {\mathcal{O}{(\alpha_{k})}}$ and then relating the gradient error sequence to an i.i.d sequence to which martingale theory is applicable.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Note that the gradient errors in SGD are larger with a $\mathcal{O}{}$ variance, which leads to a less accurate gradient descent direction. Beyond RR and SGD comparison, these results also give insight into the fast convergence properties of without-replacement sampling strategies compared to with-replacement sampling strategies.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Conclusion", "weight": 1.5} -->

After characterizing the convergence rate of RR, we look into second-order terms in the asymptotic expansion of the averaged RR iterates and obtain high probability bounds. We use these bounds to develop a new method that can accelerate the convergence rate of RR to $\mathcal{O}{(\frac{1}{k^{2}})}$ with high probability. Finally, we show that the $\mathcal{O}{(\frac{1}{k^{2}})}$ rate can also be achieved in expectation (which is a weaker notion of convergence with respect to convergence with high probability) for the $s = 1$ case by adjusting the stepsize to the strong convexity constant of the objective properly.
