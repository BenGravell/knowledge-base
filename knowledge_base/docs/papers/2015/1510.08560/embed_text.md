## Introduction: First-order incremental methods

We consider the following unconstrained optimization problem where the objective function is the sum of a large number of component functions:

with $f_{i}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$. This problem arises in many contexts and applications including regression or more generally parameter estimation problems (where $f_{i}{(x)}$ is the loss function representing the error between the output and the prediction of a parametric model), minimization of an expected value of a function (where the expectation is taken over a finite probability distribution or approximated by an $m$-sample average), machine learning, or distributed optimization over networks.

One widely studied approach for solving problem is the deterministic incremental gradient (IG) method. IG method is similar to the standard gradient method with the key difference that at each iteration, the decision vector is updated incrementally by taking sequential steps along the gradient of the component functions $f_{i}$ in a cyclic order. Hence, we can view each outer iteration $k$ as a cycle of $m$ inner iterations: starting from initial point $x_{0}^{0} \in {\mathbb{R}}^{n}$, for each $k \geq 0$, we update the iterate $x_{i}^{k}$ as

where $\alpha_{k} > 0$ is a stepsize with the convention that $x_{0}^{k + 1} = x_{m}^{k}$.

Intuitively, it is clear that slow progress can be obtained if the functions that are processed consecutively have gradients close to zero. Indeed, the performance of IG is known to be pretty sensitive to the order functions are processed \[6, Example 2.1.3\]. If there is a favorable order $\sigma$ (defined as a permutation of $\{ 1,2,\ldots,m\}$) that can be obtained by exploiting problem-specific knowledge, the method can be updated to process the functions with this order instead with the iterations:

However, in general a favorable order is not known in advance, and a common approach is choosing the indices of functions to process as independent and uniformly distributed samples from the set $\{ 1,2,\ldots,m\}$. This way no particular order is favored, making the method less vulnerable to particularly bad orders. This approach amounts to at each iteration sampling the function indices with replacement from the set $\{ 1,2,\ldots,m\}$ and is called the Stochastic Gradient Descent (SGD) method, a.k.a. Robbins-Monro algorithm. SGD is strongly related to the classical field of stochastic approximation. Recently it has received a lot of attention due to its applicability to large-scale problems and became popular especially in machine learning applications (see e.g. ).

An alternative popular approach that works well in practice is following a mixed approach between SGD and IG, sampling the functions randomly but not allowing repetitions, that is sampling the component functions at each iteration without-replacement, or equivalently picking a random order at each cycle. Specifically, at each cycle $k$, we draw a permutation $\sigma_{k}$ of $\{ 1,2,\ldots,m\}$ independently and uniformly at random over the set of all permutations

and process the functions with this order:

where $\alpha_{k} > 0$ is a stepsize. We set $x_{0}^{k + 1} = x_{m}^{k}$ as before and refer to $\{ x_{0}^{k}\}$ as the outer iterates. This method is called the Random Reshuffling (RR) method \[6, Section 2.1\] and will be the focus of this paper.

## Motivation and summary of contributions

Without-replacement sampling schemes are often easier to implement efficiently compared to with-replacement sampling schemes, guarantee that every point in the data set is touched at least once, and often have better practical performance than their with-replacement counterparts. For instance, Bottou empirically compares SGD and RR methods and finds that RR converges with a rate close to $\sim {1/k^{2}}$ whereas SGD is much slower achieving its min-max lower bound of $\Omega{({1/k})}$ for strongly convex objective functions. Many other papers listed above report a similar empirical behavior. This discrepancy in rate between RR and SGD is not only observed for large $m$ but also for small $m$ (as we illustrate in Example 3.2), and understanding it theoretically has been a long-standing open problem.

To our knowledge, the only existing theoretical analysis for RR is given by a recent paper of Recht and Ré which focuses on least mean squared optimization and formulates a conjecture that would prove that the expected convergence rate of RR is faster than that of SGD. Given $N$ arbitrary positive-definite matrices of dimension $n \times n$, the conjecture says that products of any $K$ matrices chosen from this set of $N$ matrices satisfy a non-commutative arithmetic-geometric mean inequality for every positive integer $N$ and every $K \leq N$. This conjecture has been proven only in some special cases (for $N = 2$, for $N = 3$ and when $N$ is a multiple of 3 and $K = 3$ ). Recht and Ré also analyze a special case of (that arises when ${f_{i}{(x)}} = {({{a_{i}^{T}x} - y_{i}})}^{2}$ is a quadratic function where $a_{i}$ is a column vector that is randomly generated according to a random model and $y_{i}$ is a scalar) and show that after a fixed amount of iterations, the upper bounds on the expected mean square error using without-replacement sampling is smaller than that of with-replacement sampling with high probability on most models of $a_{i}$ (probabilities are taken with respect to the random data generation model). Despite these advances, there has been a lack of convergence theory for RR that characterizes its convergence rate and explains its fast performance. Analyzing algorithms based on without-replacement sampling such as RR is more difficult than with-replacement based approaches such as SGD. The reason is that the underlying independence assumption for the with-replacement sampling allows a tractable analysis with classical martingale convergence theory, whereas without-replacement sampling introduces correlations and dependencies among the sampled gradients and iterates that are harder to analyze. The aim of our paper is to fill this theoretical gap for the case when the objective function $f$ in is strongly convex and develop a novel algorithm that can accelerate the convergence further. We next summarize our contributions.

We first consider the case when the component functions are quadratics. Building on the recent convergence rate results for the cyclic IG in, we first present a key result (Theorem 20) that provides an upper bound for the distance from the optimal solution of the iterates generated by an incremental method that processes component functions with an arbitrary fixed order and uses a stepsize $\Theta{({1/k^{s}})}$ for $s \in {(0,1\rbrack}$. This upper bound decays at rate $\mathcal{O}{({1/k^{s}})}$ and depends on the strong convexity constant of the sum function and an order dependent parameter given by a weighted average of Hessian matrices where the weights are given by the sum of the component gradients processed up to that point according to the given order. We use this result to show that the distance to the optimal solution of the iterates generated by RR algorithm with stepsize $\Theta{({1/k^{s}})}$, for all $s \in {(0,1\rbrack}$, converges to 0 at rate $\mathcal{O}{({1/k^{s}})}$ in expectation (where the expectation is over the random sequence of iterates). However, we show that achieving the rate $\mathcal{O}{({1/k})}$ involves adapting the stepsize to the strong convexity constant of the sum function.

We then consider the $q$-suffix averages of the iterates generated by RR for some $q \in {(0,1\rbrack}$ (which is obtained by averaging the last $qk$ iterates at iteration $k$) and show that with a stepsize $\alpha_{k} = {R/{({k + 1})}^{s}}$ for $s \in {({1/2},1)}$ and $R > 0$, they converge almost surely at rate $\mathcal{O}{({1/k^{s}})}$ to the optimal solution. We provide an explicit characterization of the asymptotic rate constant in terms of the averaging parameter $q$, the stepsize parameters $R$ and $s$ and the Hessian matrices and the gradients of the component functions at the optimal solution (parts $(i)$ and $({ii})$ of Theorem 3). Using strong convexity, this implies an almost sure convergence rate $\Theta{({1/k^{2s}})}$ in the suboptimality of the objective value. Our analysis views RR as a gradient descent method with random gradient errors. The analysis of RR is complicated by the fact that the cumulative gradient error over cycles are dependent. A key step in our proof is to decouple the cycle gradient error into a $\mathcal{O}{(\alpha_{k})}$ term independent over cycles and another term that scales as $\mathcal{O}{(\alpha_{k}^{2})}$. This allows us to use strong law of large numbers for a properly weighted average of the cycle error gradient sequence (where the weights depend on the stepsize) and show almost sure convergence of the $q$-suffix averaged iterates. Another key component of our analysis is to adapt the Polyak-Ruppert averaging techniques developed for SGD to RR.

We also provide a high probability convergence rate estimate for the distance of $q$-suffix averages to the optimal solution that consists of two terms, with the first term corresponding to a $1/k^{s}$ decay of a "bias" term (where bias is defined as the expected value of the cycle gradient errors of RR which may be non-zero) and the second term representing a $1/k$ decay for $0 < q < 1$ (and $\log{k/k}$ decay for $q = 1$); see part $({iii})$ of Theorem 3. These results are obtained by martingale concentration techniques. We use the characterization of the bias to estimate it with a term that can be computed during the RR iterations. We show that subtracting the estimated bias from the averaged RR iterates accelerates the convergence rate further, leaving only the second error term of $1/k$ decay in the iterates (part $({iv})$ of Theorem 3). Based on this result, we propose a new algorithm which we call the De-biased Random Reshuffling (DRR) method that can accelerate the asymptotic convergence rate of RR in the suboptimality of the function values from $\mathcal{O}{({1/k^{2s}})}$ to $\mathcal{O}{({1/k^{2}})}$.

Finally, in Theorem 4 we show that our results in Theorem 3 extend to the more general case when component functions are smooth (twice continuously differentiable) under a Lipschitz assumption on the Hessian, which allows us to control the second order term in a Taylor expansion of the gradient.

Outline: The outline of the paper is as follows. In Section 3, we introduce our approach for analyzing RR, present Polyak-Ruppert averaging and give a motivating example. Section 4 focuses on the case when component functions are quadratics. We first present a convergence rate estimate for IG with a fixed arbitrary order. We then focus on RR and study convergence of averaged iterates to the optimal solution. Section 5 extends our results to smooth functions. Section 6 proposes the DRR algorithm that can accelerate RR further. Finally, we conclude with a summary of our work in Section 7. Some of the technical lemmas required in the details of the proofs are deferred to Sections A, B and C of the Appendix.

Notation: We study the point-wise dominance of stochastic sequences by deterministic sequences and use the following notation. Let $x_{k} = {x_{k}{(\omega)}}$ be a stochastic real-valued sequence (where $\omega$ can be thought as the source of randomness) and $y_{k}$ be a real-valued deterministic sequence. We write ${{x_{k} = {\mathcal{O}{(y_{k})}}}\Leftrightarrow{{{\exists h} > {0,{\exists k_{0}}\quad\text{such that}}}\quad{{{|x_{k}|} \leq {h{|y_{k}|}}}\mspace{21mu}{{\forall k} \geq {k_{0},{\forall\omega}}}}}},$ where $h$ and $k_{0}$ are independent of $\omega$ (Note that the requirement is that this inequality holds for all $\omega$, not just for almost all $\omega$). When $x_{k}$ is non-negative for every $\omega$, given another deterministic positive sequence $z_{k}$, we also introduce the inequality version of this definition: ${x_{k} \leq {y_{k} + {o{(z_{k})}}}}\Leftrightarrow{{{\forall\varepsilon} > {0,{\exists{k_{0}{(\varepsilon)}}}\quad\text{such that}}}\qquad{{{z_{k}^{- 1}{|{{x_{k}{(\omega)}} - y_{k}}|}} \leq \varepsilon},{{\forall k} \geq {{k_{0}{(\varepsilon)}},{\forall\omega}}}}}$ where $k_{0}$ depends on $\varepsilon$ but is independent of $\omega$. When $x_{k}$ is deterministic, these definitions reduce to the standard definitions of $\mathcal{O}{( \cdot )}$ and $o{( \cdot )}$ for deterministic sequences. For random $x_{k}$, the only difference is that we require the constants to be independent of the choice of $\omega$. For example, if $x_{k}$ is uniformly distributed over $\lbrack 0,10\rbrack$, we write $x_{k} = {\mathcal{O}{}}$. Throughout the paper, $\parallel \cdot \parallel$ denotes the vector or matrix 2-norm (maximum singular value).

## Preliminaries

We consider solving problem with RR method with iterations given in. Throughout we assume the following:

### Assumption 3.1

The sum function ${f{(x)}} = {\sum_{i = 1}^{m}{f_{i}{(x)}}}$ is strongly convex, i.e., there exists a constant $c > 0$ such that the function ${f{(x)}} - {\frac{c}{2}{\| x\|}^{2}}$ is convex on ${\mathbb{R}}^{n}$.^11^1Such functions arise naturally in support vector machines and other regularized learning algorithms or regression problems (see e.g. ).

Note that this assumption is on the sum function $f$, it does not require the convexity of the individual component functions $f_{i}$. A consequence of this assumption is that there exists a unique optimal solution to which we denote by $x^{\ast}$. Another consequence is that the Hessian at the optimal solution is invertible since

where $I_{n}$ is the $n \times n$ identity matrix.

To analyze RR, we view it as a gradient method with random gradient errors and rewrite the outer iterations as

is the cumulative gradient errors associated with the cycle $k$. This approach is similar to the analysis of SGD, where one writes each (inner) iteration as a gradient method with error. The key difference that simplifies the analysis of SGD is the fact that the iteration gradient errors at the current iterate are independent (because of independent identically distributed sampling of component function indices) allowing use of martingale central limit theorems to obtain convergence and rate results (see e.g. ). In contrast, for RR, not only are the iteration gradient errors dependent (because of sampling a random order at cycle $k$ coupling indices $\sigma_{k}{(i)}$ and $\sigma_{k}{(j)}$ for $i \neq j$), but also the cycle gradient errors $E_{k_{1}}$ and $E_{k_{2}}$ for cycles $k_{1} \neq k_{2}$ are dependent as they both depend on the history of the iterates. This necessitates a different line of attack for the convergence analysis of RR.^22^2There is some literature that analyzes SGD under correlated noise \[21, Ch. 6\], but the noise needs to have a special structure (such as a mixing property) which does not seem to be applicable to the analysis of RR.

A key idea in our analysis is to use a recent upper bound for the convergence rate of cyclic incremental gradient method (see ), which can be generalized to hold for any fixed deterministic order. This bound implies an almost sure upper bound (in fact one that holds for all sample paths) on the distance of the outer iterates $x_{0}^{k}$ generated by RR from the optimal solution $x^{\ast}$ denoted by $\text{dist}_{k} = {\|{x_{0}^{k} - x^{\ast}}\|}$ (see Section 4.1). Crucially, this result implies an upper bound in expected distance which is asymptotically $m$ times smaller than the almost sure guarantees on the distance of the iterates.

In analyzing RR, we will also consider the average of the outer iterate sequence given by^33^3It is well known that computing this (moving) average can be done efficiently in a dynamic manner by storing a vector of length $n$. ${{\overline{x}}_{k}:=\frac{\sum_{j = 0}^{k - 1}x_{0}^{j}}{k}}.$ We also consider averaging only the most recent iterates, i.e. at iteration $k$, averaging the last $qk$ iterates for some constant $q \in {(0,1\rbrack}$:

The generated sequence is referred to as the $q$-suffix average of the sequence $x_{0}^{k}$. For SGD, it was shown that $q$-suffix averaging with $0 < q < 1$ leads to better performance then averaging (which corresponds to the $q = 1$ case by definition), improving the convergence rate in the suboptimality of the function value from $\log{k/k}$ to $1/k$. This is in line with our results in Section 4 which show faster rate for the $0 < q < 1$ case. The parameter $q$ can be thought as a measure of how much memory one uses during the averaging process. We define the $q$-suffix average of the stepsize in a similar way:

We will obtain our strongest convergence results (in the almost sure sense and with a similar $m$ dependence as the expected guarantees) for averaged iterate sequences with "large step sizes", a technique known as Polyak-Ruppert averaging, which has been used in achieving optimal rates for SGD in a robust manner as explained next.

### Polyak-Ruppert averaging

SGD has a long history going back to the seminal paper of Robbins and Monro. It has been analyzed under different assumptions extensively in the stochastic approximation literature (see e.g. ). For stochastic convex optimization, it has been shown that SGD has a min-max lower bound of $\Omega{({1/k})}$. One way of achieving this optimal $1/k$ rate is to use a stepsize $\alpha_{k} = {R/k}$ where $R$ is a positive scalar adjusted properly to the strong convexity constant of the objective function but this requires the knowledge or the estimate of an accurate lower bound on the strong convexity constant. If a lower bound is not known or cannot be estimated accurately, the convergence can be potentially slow \[25, Section 2.1\]. Polyak-Ruppert averaging is a technique that allows to get the optimal $\sim {1/k}$ rate in an asymptotically efficient manner without the need to adjust to the strong convexity constant. It relies on using a larger stepsize $\alpha_{k} = {R/k^{s}}$ (with $R$ an arbitrary positive constant and $s \in {({1/2},1)}$) that decays slower than $\Theta{({1/k})}$ but then taking the time average of the iterates to filter out the undesired oscillations arising due to the larger steps.^44^4IG shows similar properties to SGD in terms of the robustness of the stepsize rules $\alpha_{k} = {R/k^{s}}$. The convergence rate (in $k$) is only robust to the strong convexity constant of the objective for $s < 1$ but not for $s = 1$. We will later show that the same technique allows us to get almost sure guarantees for the averaged iterates without the need to tune the stepsize to the strong convexity constant (see Theorems 3 and 4).

### A motivating example

Before presenting our convergence analysis, we consider a simple example that highlights the difference in convergence mechanisms of SGD and RR and gives intuition on why RR is faster than SGD asymptotically.

### Example 3.2

Consider the component functions

where the cycle gradient errors are given by

Plugging in the identities ${{\nabla f_{1}}{(x)}} = {x - 1}$, ${{\nabla f_{2}}{(x)}} = {{2x} + 1}$ obtained from and the inner update formula, we obtain

where ${\mu{(\sigma_{k})}} = {- {{\nabla^{2}f_{\sigma_{k}{}}}{(x^{\ast})}{\nabla f_{\sigma_{k}{}}}{(x^{\ast})}}}$ satisfying

In contrast, SGD starting from an initial point $y^{0}$ leads to the iterations

where $i_{j}$ is an independent and identically distributed (i.i.d.) random variable with a uniform distribution over the index set $\{ 1,2\}$ and the gradient error $e^{j}$ is given by

We consider a stepsize of $\alpha_{k} = \frac{R}{k^{s}}$ with $s = 0.75$ for both algorithms. Note that for this example, RR is globally convergent to the optimal solution $x^{\ast} = 0$ with probability one, therefore $x_{0}^{j}\rightarrow 0$.^55^5To see this, note that the RR iterations for this example are given by $x_{0}^{k + 1} = {{{({{1 - {\frac{3}{2}\alpha_{k}}} + {2\alpha_{k}^{2}}})}x_{0}^{k}} - {\alpha_{k}^{2}\mu{(\sigma_{k})}}}$ which implies, after taking norms of both sides and using the fact that ${\|{\mu{(\sigma_{k})}}\|} \leq 2$, ${\text{dist}_{k + 1} \leq {{{({{1 - {\frac{3}{2}\alpha_{k}}} + {2\alpha_{k}^{2}}})}\text{dist}_{k}} + {2\alpha_{k}^{2}}}}.$ Then, by invoking classical results for the asymptotic behavior of non-negative sequences (see e.g. \[6, Appendix A.4.3\], we get $\text{dist}_{k + 1}\rightarrow 0$. Theorem 20 also shows global convergence of RR on this example. By a similar argument, it can be shown that SGD is also convergent to the optimal solution $x^{\ast} = 0$ in mean-square, i.e. ${{\mathbb{E}}{\| y^{j}\|}^{2}}\rightarrow 0$ (see also e.g. ). Then, it follows from and that the cumulative gradient error of SGD for any cycle $k$ (defined as the cumulative sum $\sum_{j = {{({k - 1})}m}}^{{km} - 1}e_{j})$) has zero expectation and $\Theta{}$ variance whereas the gradient errors in RR are $E_{k} = {\mathcal{O}{(\alpha_{k})}}$ with a typically non-zero expectation satisfying ${{\mathbb{E}}{(E_{k})}} = {\alpha_{k}{({1 - {2x_{0}^{k}}})}}$ and an asymptotically smaller variance $\mathcal{O}{(\alpha_{k}^{2})}$ compared to SGD. In other words, the cycle gradient errors go to zero with probability one for RR whereas the gradient errors in SGD are typically bounded away from zero with a positive probability. Informally, this leads to a more accurate direction of descent for RR and is the main reason behind the faster convergence we demonstrate for RR compared to SGD in our analysis.

Figure 1: Left panel: Comparison of the histogram of the approximation error ${\overline{x}}_{k} - x^{\ast}$ of the averaged iterates for RR and SGD after k = 500 cycles over 10000 sample paths created for the Example 3.2 with s = 0.75. Each sample path contains 1000 gradient computations for both RR and SGD. Right, top panel: Histogram of the scaled approximation error $k^{s}{({{\overline{x}}_{k} - x^{\ast}})}$ for RR iterates which is concentrated around the vertical line in red. Right, bottom panel: Histogram of the scaled approximation error $k^{1/2}{({{\overline{x}}_{k} - x^{\ast}})}$ for SGD which has the shape of a standard normal distribution. The vertical blue line passing through the origin is the axis of symmetry for this distribution indicating that this distribution is centered.

We also observe that the cycle gradient error $E_{k}$ given by consists of the sum of two terms: The first term is $\mathcal{O}{(\alpha_{k})}$ and is independent over the cycles as the permutations $\sigma_{k}$ are independent and identically distributed whereas the second term is of smaller (second) order as $x_{0}^{j}\rightarrow 0$. We will show later in Lemma B.4 that such a decomposition can be obtained more generally when component functions are quadratics or they are smooth functions and will be a key step in the proof of Theorem 3.

Figure 1 compares the RR and SGD algorithms with averaging in terms of the histogram of the error (distance of the averaged iterates to the optimal solution $x^{\ast}$). In other words, we compare the approximation errors ${\overline{x}}_{k} - x^{\ast}$ and ${\overline{y}}_{k} - x^{\ast}$ where where ${\overline{y}}_{k}:=\frac{\sum_{j = 0}^{{mk} - 1}y^{j}}{mk}$ is the averaged SGD iterates after $k$ cycles (or equivalently $mk$ inner iterations). For a fair comparison, both algorithms are run with the same parameters using $k = 500$ cycles over $10000$ sample paths created for the Example (3.2) where $s = 0.75$. The left panel in Figure 1 compares the histograms of ${\overline{x}}_{k} - x^{\ast}$ and ${\overline{y}}_{k} - x^{\ast}$ and shows that the approximation error ${\overline{x}}_{k} - x^{\ast}$ for RR is typically much smaller compared to that of SGD suggesting RR has a faster convergence rate. The top panel on the right illustrates that the scaled approximation error $k^{s}{({{\overline{x}}_{k} - x^{\ast}})}$ is concentrated around its mean (marked by the red line) suggesting $\mathcal{O}{({1/k^{s}})}$ convergence rate almost surely for the averaged RR iterates. On the other hand, the bottom panel on the right shows that the distribution of $k^{1/2}{({{\overline{y}}_{k} - x^{\ast}})}$ is approximately a standard normal distribution as predicted by the theory, illustrating the $\mathcal{O}{({1/k^{1/2}})}$ convergence rate of the averaged SGD iterates to the optimal solution $x^{\ast}$ in distribution. In Section 4, we will develop the first convergence theory for RR, establishing the $\mathcal{O}{({1/k^{s}})}$ convergence rate we observe in the numerical experiments and show that $k^{s}{({{\overline{x}}_{k} - x^{\ast}})}$ converges almost surely to a point for which we provide an explicit formula.

## Quadratic component functions

We first consider quadratic component functions which allows an elegant analysis without the need to approximate higher order terms. We will show in Section 5 that the same line of analysis extends to smooth component function under a Lipschitz assumption on the Hessian matrices. Let $f_{i}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ be a quadratic function of the form

where $P_{i}$ is a symmetric $n \times n$ matrix, $q_{i} \in {\mathbb{R}}^{n}$ is a column vector and $r_{i}$ is a scalar. Note that $f_{i}$ has Lipschitz gradients, i.e.,

where $L_{i} = {\| P_{i}\|}$. It follows from the triangle inequality that $f$ has Lipschitz gradients with Lipschitz constant at most

Moreover, Assumption 3.1 implies that the Hessian matrix of the sum satisfies ${{{\nabla^{2}f}{(x)}} = {\sum_{i = 1}^{m}{{\nabla^{2}f_{i}}{(x)}}} = {\sum_{i = 1}^{m}P_{i}} \geq {cI_{n}} > 0}.$

### Convergence Rate

Our convergence analysis of RR builds on a recent upper bound for convergence rate of (deterministic) cyclic IG method (see ), which can be generalized to hold for any fixed permutation $\sigma$ of $\{ 1,2,\ldots,m\}$. This result implies an upper bound (for all sample paths) on the distance to the optimal solution of the iterates generated by RR, which is presented next.

### Theorem 1

Let Assumption 3.1 hold. Let $f_{i}{(x)}$ be a quadratic function of the form ${f_{i}{(x)}} = {{{\frac{1}{2}x_{i}^{T}P_{i}x} - {q_{i}^{T}x}} + r_{i}}$ where $P_{i}$ is a symmetric $n \times n$ matrix, $q_{i} \in {\mathbb{R}}^{n}$ is a column vector and $r_{i}$ is a scalar for $i = {1,2,\ldots,m}$. Suppose Assumption 3.1 holds. Consider the iterates $\{ x_{0}^{k}\}$ generated by the iterations with a fixed order $\sigma$ and stepsize $\alpha_{k} = {R/{({k + 1})}^{s}}$ where $R > 0$ and $s \in {({1/2},1)}$. Then^66^6The original result in was stated for $\sigma = {\{ 1,2,\ldots,m\}}$ but here we translate this result into an arbitrary permutation $\sigma$ of $\{ 1,2,\ldots,m\}$ by noting that processing the set of functions $\{ f_{1},f_{2},\ldots,f_{m}\}$ with order $\sigma$ is equivalent to processing the permuted functions $\{ f_{\sigma_{1}},f_{\sigma_{2}},\ldots,f_{\sigma_{m}}\}$ with order $\{ 1,2,\ldots,m\}$.,

where $c$ is the strong convexity constant of the sum function $f{(x)}$ and

This theorem provides an upper bound on the rate with a rate constant $\mu{(\sigma)}$ that depends on the order $\sigma$. Note that the best rate that IG with a fixed order $\sigma$ can attain in terms of upper bounds is $\mathcal{O}{({1/k})}$ and requires a stepsize $R/{({k + 1})}$ with $R > {1/c}$ (see also for the lower bound of $\Omega{({1/k})}$ for IG under some conditions). We next provide some upper bounds on $\mu{(\sigma)}$. We define

Using $L_{i} = {\| P_{i}\|}$ for each $i$, it follows from the triangle inequality that

where $L$ is the Lipschitz constant of the gradient of $f$ defined by. By replacing $\mu{(\sigma)}$ by $M_{\Gamma}$ in Theorem 20 one can get an upper bound on the worst-case convergence rate that applies to any choice of fixed order $\sigma$. Using a similar argument along the lines of the proof of Theorem 20 on the convergence rate of IG, it is straightforward to show that RR never performs any slower than this worst-case convergence rate which is the subject of the next result. The idea is to bound the stochastic $\text{dist}_{k}$ sequence from above point-wise. The proof is a simple exercise and is omitted due to space considerations.

### Corollary 4.1

Under the setting of Theorem 20, if $\sigma$ is sampled uniformly at each cycle instead of being kept fixed, then

with probability one where $M_{\Gamma}$ is deterministic and is defined by.

Corollary 4.1 provides a simple worst-case upper bound on the rate, however the rate constant $M_{\Gamma} = {\sup_{\sigma}{\|{\mu{(\sigma)}}\|}}$ is pessimistic and can be thought as a worst-case performance measure that holds for every sample path. One way to get better constants is to consider convergence in expectation, a weaker notion of convergence compared to almost sure convergence. In the next theorem, we show that $M_{\Gamma}$ can be improved to a typically much smaller constant $\|\overline{\mu}\|$ where

can be thought as a measure of average performance over the choice of random permutations.

### Theorem 2

Let $f_{i}{(x)}$ be a quadratic function of the form ${{f_{i}{(x)}} = {{{\frac{1}{2}x_{i}^{T}P_{i}x} - {q_{i}^{T}x}} + r_{i}}},$ where $P_{i}$ is a symmetric $n \times n$ matrix, $q_{i} \in {\mathbb{R}}^{n}$ is a column vector and $r_{i}$ is a scalar for $i = {1,2,\ldots,m}$. Suppose Assumption 3.1 holds. Consider the iterates $\{ x_{0}^{k}\}$ generated by the RR iterations and stepsize $\alpha_{k} = {R/{({k + 1})}^{s}}$ where $R > 0$ and $s \in {(0,1\rbrack}$. Then,

where the expectation is taken over the sequence of iterates, $\overline{\mu}$ is defined by.

### Remark 4.2

A consequence of Lemma B.3 proved in the Appendix is that

where $\overline{\mu}$ is defined by. By the triangle inequality, ${\|\overline{\mu}\|} \leq {\sum_{i = 1}^{m}{L_{i}G_{\ast}}} = {LG_{\ast}}$ where $G_{\ast}$ is defined by. This upper bound is $m$ times smaller than the previous upper bound on $M_{\Gamma}$ in. As an example, consider $s = 1$ with ${Rc} = 2$. In this case, $L = {\mathcal{O}{(m)}}$, $c = {\mathcal{O}{(m)}}$, $R = {\mathcal{O}{({1/m})}}$ and ${\|\overline{\mu}\|} = {\mathcal{O}{(m)}}$. We obtain from that ${{\mathbb{E}}\left( \text{dist}_{k} \right)} = {{O{(\frac{1}{mk})}} + {o{({1/k})}}}$. Note that, the performance guarantee for IG from Corollary 4.1 is $\text{dist}_{k} = {{\mathcal{O}{({1/k})}} + {o{({1/k})}}}$ which is also worse than RR by a factor of $O{(m)}$. For a fair comparison with the SGD method, we consider running the SGD iterations for $j = {km}$ iterations so that both RR and SGD methods have access to the same number of component gradients. In this case, expected distance to suboptimality for SGD with the recommended $O{({1/j})}$ stepsize is $\mathcal{O}{(\frac{1}{\sqrt{j}})}$ where the hidden constants are independent of $m$ (see e.g. ) which is worse than the $\mathcal{O}{({1/j})}$ guarantees for RR when $j$ is sufficiently large. These bounds show that when $m$ is small and $k$ is large, IG could outperform SGD in theory, however SGD (and RR) are more suitable for applications when $m$ is large and will admit better bounds compared to IG if $m$ is large enough for a given $k$ fixed^77^7We note however that SGD upper bounds are in expectation whereas IG results are deterministic which is a stronger notion of convergence.

It is also natural to ask what would happen to the rate constants and to the rate if one would take stepsize $\alpha_{k} = {\Theta{({1/k^{s}})}}$ and apply (Polyak-Ruppert) averaging to the RR iterates, especially given the fact that $\mathcal{O}{({1/k^{s}})}$ stepsize used in averaging does not require adjustment of the parameter $R$ to the strong convexity level. More generally, one could consider $q$-suffix averaging. In the next section, we show that for the averaged RR iterates, similar upper bounds in hold not only in expectation but also in probability. Another benefit of averaging is that it leads to not only upper bounds but also lower bounds which can then be leveraged to accelerate RR further as we will show in Section 6.

### Convergence rate with averaging

The following theorem characterizes the rate of convergence of the averages of iterates generated by RR. Part $(i)$ and $({ii})$ of this theorem show that $q$-suffix averages of the RR iterates converge at rate $1/k^{s}$ to the optimal solution almost surely with a stepsize $\Theta{({1/k^{s}})}$ for $s \in {({1/2},1)}$. By gradient Lipschitzness, this translates into a rate of $\Theta{({1/k^{2s}})}$ for the suboptimality of the objective value. The result is based on decoupling the cycle gradient errors $E_{k}$ into a $\Theta{(\alpha_{k})}$ term independent over the cycles and another $\mathcal{O}{(\alpha_{k}^{2})}$ term that becomes negligible in the limit. Part $({iii})$ is a high-probability convergence rate estimate for the approximation error ${\overline{x}}_{q,k} - x^{\ast}$. The approximation error consists of two terms, the first term $b_{q,k}$ which we call the "bias" term is deterministic and decays like $\sim {1/k^{s}}$. It comes from the expected value of the independent part of the gradient cycle errors which may be different than zero. The second part is on the order of $1/k$ for $0 < q < 1$ (and $\log{k/k}$ when $q = 1$) and it is based on the Azuma-Hoeffding inequality for martingale concentration. Finally, part $({iv})$ is on estimating the bias term $b_{q,k}$ with another quantity ${\hat{b}}_{q,k}$. It shows that by subtracting the estimated bias from the averaged iterates, we can approximate the optimal solution $x^{\ast}$ up to an $\mathcal{O}{({1/k})}$ error in distances or equivalently up to an $\mathcal{O}{({1/k^{2}})}$ error in the suboptimality of the objective value. In Section 6, this result will be fundamental for Algorithm 1 that accelerates the convergence of RR from $\Theta{({1/k^{2s}})}$ to $\mathcal{O}{({1/k^{2}})}$ with high probability in the suboptimality of the objective value.

### Theorem 3

Let $f_{i}{(x)}$ be a quadratic function of the form

where $P_{i}$ is a symmetric $n \times n$ matrix, $q_{i} \in {\mathbb{R}}^{n}$ is a column vector and $r_{i}$ is a scalar for $i = {1,2,\ldots,m}$. Consider the $q$-suffix averages ${\overline{x}}_{q,k}$ of the RR iterates generated by the iterations with stepsize $\alpha_{k} = \frac{R}{{({k + 1})}^{s}}$ where $R > 0$ and $s \in {(\frac{1}{2},1)}$. Suppose that Assumption 3.1 holds. Then the following statements are true:

For any $0 < q \leq 1$, the $q$-suffix averaged stepsize ${\overline{\alpha}}_{q,k}$ defined in satisfies

For any $0 < q \leq 1$, we have

where $\overline{\mu}$ is given by, i.e., the normalized error ${({{\overline{x}}_{q,k} - x^{\ast}})}/{\overline{\alpha}}_{q,k}$ converges to the constant vector $- {H_{\ast}^{- 1}\overline{\mu}}$ almost surely where $H_{\ast} = {\sum_{i = 1}^{m}P_{i}}$ is the Hessian matrix at the optimal solution and $\overline{\mu}$ is given by. Then, from part $(i)$,

Hence, the $q$-suffix averaged iterates ${\overline{x}}_{q,k}$ converge to the optimal solution $x^{\ast}$ with rate $1/k^{s}$ almost surely.

With probability at least $1 - \delta$, we have

is deterministic, $\overline{\mu}$ is given by $()$ and ${\overline{\alpha}}_{q,k}$ is the averaged stepsize defined in. The constants hidden by $\mathcal{O}{( \cdot )}$ depend only on $G_{\ast},L,m,R,c,q$ and $s$.

where ${\overline{\alpha}}_{q,k}$ is the averaged stepsize defined in. Then, ${{\hat{b}}_{q,k} = {b_{q,k} + {\mathcal{O}{(\alpha_{k}^{2})}}}}.$ It follows from part $({ii})$ that with probability at least $1 - \delta$,

### Proof

As the stepsize sequence is monotonically decreasing, we have the bounds

Dividing each term by $qk$, after a straightforward integration we obtain

which completes the proof.

Taking the $q$-suffix averages of both sides of, we obtain

As $f$ is a quadratic, the first order Taylor series for the gradient of $f$ is exact:

Therefore, (35 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")) becomes $I_{q,k} = \frac{{\sum_{j = {{({1 - q})}k}}^{k - 1}{H_{\ast}{({x_{0}^{j} - x^{\ast}})}}} + E_{j}}{qk}$ which is equivalent to

and can be interpreted as the ($q$-suffix) averaged gradient error sequence $E_{j}$ normalized by the ($q$-suffix) averaged stepsize sequence $\alpha_{j}$. Since $H_{\ast}$ is invertible by the strong convexity of $f$ (see ), we can rewrite (37 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")) as

where we used the inequality ${\| H_{\ast}^{- 1}\|} \leq {1/c}$ implied by and Lemma B.2 from the appendix to provide an upper bound for the second term in the first equality. Note that, as a consequence of Lemma B.2, $\mathcal{O}{( \cdot )}$ notation above hides a constant that depends only on the parameters $G_{\ast},L,c,m,R,s,q$ and also $\text{dist}_{0}$ when $q = 1$. Then, dividing both sides of (39 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")) by ${\overline{\alpha}}_{q,k}$, taking limits as $k$ goes to infinity, using part $(i)$ on the asymptotic behavior of ${\overline{\alpha}}_{q,k}$ and the fact that $Y_{q,k}\rightarrow\overline{\mu}$ a.s. from Lemma B.4, we obtain the claimed result.

By parts $(i)$ and $({iii})$ of Lemma B.4 from the appendix that relates the gradient error sequence $E_{j}$ to a sequence of i.i.d. variables $\mu{(\sigma_{j})}$, for $0 < q \leq 1$,

We first give a proof for $q = 1$, the proof for the remaining $q \in {}$ case will be similar. Assume $q = 1$. Plugging $q = 1$ and (40 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")) into (39 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")), we obtain

where $b_{1,k}$ is defined by (33 ‣ Theorem 3. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")) and we used in the last step the fact that for $s > {1/2}$

where $\zeta{( \cdot )}$ is the Riemann-Zeta function. We now study the asymptotic behavior of the last summation term in (41 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")) by introducing the process $S_{1,k} = {\sum_{j = 0}^{k - 1}Z_{j}}$, where $Z_{j}:={\alpha_{j}{({{\mu{(\sigma_{j})}} - \overline{\mu}})}}$ and $k \geq 0$ with the convention that $S_{1,0} = 0$. Equipped with this definition, (41 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")) becomes

The random variables $Z_{j}$ are independent, centered and have an identical distribution up to the scaling factor $\alpha_{j}$. Therefore, $S_{1,k}$ is a sum of centered random variables satisfying:

where we used (70 ‣ Lemma B.4. ‣ Appendix B Technical lemmas for the proof of Theorem 3 ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")) in the last inequality (see also Lemma B.3). Then, by the Azuma-Hoeffding inequality, for every $t > 0$,

where $\beta = {2{\sum_{j = 0}^{\infty}\gamma_{j}^{2}}} < \infty$ as $\alpha_{j}$ is square-summable (see (42 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent"))). Note that $\beta$ depends only on $G_{\ast},L,m$ and the stepsize parameters $R$ and $s$. It is easy to see that selecting $t \geq t_{\delta} = \sqrt{\beta{\log{({2/\delta})}}}$ makes the right-hand side $\leq \delta$. Therefore for any $\delta > 0$, with probability at least $1 - \delta$,

which if inserted into the expression (43 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")) completes the proof for the $q = 1$ case. For $0 < q < 1$ case, the same line of reasoning applies except that we replace $b_{1,k}$ with $b_{q,k}$ and we can improve the $\mathcal{O}{({\log{k/k}})}$ term in the expression (43 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")) to $\mathcal{O}{({1/k})}$, this is justified by (39 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")). Then, this leads to

where $S_{q,k}:={\sum_{j = {{({1 - q})}k}}^{k - 1}Z_{j}} = {S_{1,k} - S_{1,{{({1 - q})}k}}}$ is the $q$-suffix cumulative sum (cumulative sum of the last $qk$ terms) of the sequence $Z_{k}$. Then using (45 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")), with probability at least $1 - \delta$,

Plugging this high probability bound into (46 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")), we conclude.

By Lemma B.1, we have ${\max\limits_{1\leq i<m}{\|{x_{i - 1}^{k} - x^{\ast}}\|}} = {\mathcal{O}{(\alpha_{k})}}$. Therefore,

for any $i = {1,2,\ldots,m}$. As a consequence,

where in the second equality we use the fact that ${\overline{\alpha}}_{q,k} = {\mathcal{O}{({1/k^{s}})}} = {\mathcal{O}{(\alpha_{k})}}$ implied by part $(i)$.

## Extension to smooth component functions

Extending our results to more general smooth functions requires obtaining similar bounds for the cycle gradient errors which depend on the gradients and Hessian matrices of the component functions along the inner iterates. In order to be able to control the change of gradients and Hessian matrices along the iterates, we introduce the following assumption which has also been used to analyze SGD.

### Assumption 5.1

The functions $f_{i}$ are convex on ${\mathbb{R}}^{n}$ and have Lipschitz continuous second derivatives, i.e. there exists a constant $U_{i}$ such that

Under this assumption, by the triangle inequality, ${\nabla^{2}f}{( \cdot )}$ is also Lipschitz with constant ${U:={\sum_{i = 1}^{m}U_{i}}}.$ When the component functions are quadratics, we have the special case with $U = U_{i} = 0$. We will now see how this assumption makes it possible to control the change of gradients of the component functions. Smooth functions $f$ with Lipschitz Hessians are quadratic-like in the sense that the first-order Taylor approximation to the gradient of $f$ is almost affine (with a quadratic term controlled by the parameter $U$) satisfying

(see e.g. \[18, Section 1.3\]) The analysis of Theorem 3 (and Lemma B.4 it builds upon) considers the $U = 0$ case (see e.g. (36 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")) and (48 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent"))) applying a first-order Taylor approximation to the gradient of the component functions at $x = x_{0}^{k}$ where ${\|{x - x^{\ast}}\|} = {\|{x_{0}^{k} - x^{\ast}}\|} = {\mathcal{O}{(\alpha_{k})}}$ by Lemma B.1. Therefore, when $U \neq 0$, an extra correction term $\eta = {\mathcal{O}{(\alpha_{k}^{2})}}$ needs to be added to the analysis. However, we show in the next theorem that this correction term does not cause a slow down in the convergence rate (in terms of dependency in $k$) compared to the quadratic case because the $q$-suffix averages of this $\mathcal{O}{(\alpha_{k}^{2})}$ correction term decays like $\mathcal{O}{({1/k})}$.^88^8This is due to the fact that the sequence $\alpha_{k}^{2}$ is summable when $s > {1/2}$.

We will also need one more technical assumption that appeared in a number of papers in the literature for analyzing incremental methods to rule out the case that the iterates diverge to infinity. In particular, this assumption is made in for generalizing Theorem 20 on the rate of deterministic IG from quadratic functions to general smooth functions which we will be referring to.

### Assumption 5.2

Iterates ${\{ x_{j}^{k}\}}_{j,k}$ generated are uniformly bounded, i.e. there exists a non-empty compact Euclidean ball $\mathcal{X} \subset {\mathbb{R}}^{n}$ that contains all the iterates a.s.^99^9Note that if this assumption holds and if $f_{i}$ is three-times continuously differentiable on the compact set $\mathcal{X}$, then the third-order derivatives are bounded and Assumption 5.1 holds.

Equipped with these two assumptions, all the results of Theorem 3 extend naturally with minor modifications. In particular, $P_{i}$ (which is a constant Hessian matrix in the setting of Theorem 3) needs to be replaced by ${\nabla^{2}f_{i}}{(x^{\ast})}$ or ${\nabla^{2}f_{i}}{(x_{i - 1}^{k})}$ depending on the context.

### Theorem 4

Consider the RR iterations given by with stepsize $\alpha_{k} = \frac{R}{{({k + 1})}^{s}}$ where $R > 0$ and $s \in {(\frac{1}{2},1)}$. Suppose that Assumptions 3.1, 5.1 and 5.2 hold. Then the following statements are true:

For any $0 < q \leq 1$, ${{{\lim_{k\rightarrow\infty}{k^{s}{({{\overline{x}}_{q,k} - x^{\ast}})}}} = {{- {a_{q}{(s)}H_{\ast}^{- 1}\overline{v}}}\quad a}}.s}.$ where $H_{\ast} = {{\nabla^{2}f}{(x^{\ast})}}$ is the Hessian matrix at the optimal solution, $a_{q}{(s)}$ is defined by (30 ‣ Theorem 3. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")) and

With probability at least $1 - \delta$, we have

is deterministic. The constants hidden by $\mathcal{O}{( \cdot )}$ depend only on $G_{\ast},L,m,R,c,q,s$ and $U$.

Then, ${{\hat{r}}_{q,k} = {r_{q,k} + {\mathcal{O}{(\alpha_{k}^{2})}}}}.$ It follows from part $({ii})$ that with probability at least $1 - \delta$,

### Proof

The proof techniques of Theorem 3 applies directly except that the Taylor approximation for the gradients of the component functions will have an extra term compared to the proof of Theorem 3 (see also ). Also, instead of Lemmas B.2 and B.4 that apply to only quadratic functions, their extensions Lemmas C.3 and C.4 given in the appendix are used in the proof. For the sake of completeness, besides these changes, we also give an overview of the main modifications required for each part of the proof:

The expression (36 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")) for the gradient should be modified to include an extra error term $\eta_{j}$ of the form

By Lemma C.2, $\sum_{j}\eta_{j} \leq \frac{U}{2} \parallel \parallel x_{0}^{j} - x^{\ast} \parallel^{2} = \mathcal{O}{(\alpha_{j}^{2})}$ therefore the sequence $\eta_{j}$ is summable and if averaged decays like $\mathcal{O}{({1/k})}$ without degrading the convergence rate except possibly the constants hidden by $\mathcal{O}{( \cdot )}$.

The same proof applies by invoking Lemma C.4 in lieu of Lemma B.4.

Instead of Lemma B.1, we use Lemma C.2. The expression (48 ‣ Proof. ‣ 4.2 Convergence rate with averaging ‣ 4 Quadratic component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")) on the difference of gradients needs to be adjusted as

The right-hand side is still $\mathcal{O}{(\alpha_{k}^{2})}$ by an application of Lemma C.2 therefore the rest of the proof applies.

## An RR algorithm with bias removal

Part $({iii})$ of Theorem 4 (see also part $({iii})$ of Theorem 3) shows that if the estimate of the bias term ${\hat{r}}_{q,k}$ given by (51 ‣ Theorem 4. ‣ 5 Extension to smooth component functions ‣ Why Random Reshuffling Beats Stochastic Gradient Descent")) is subtracted from the $q$-suffix averaged RS iterates, then the distance to the optimal solution of the $q$-suffix averaged iterates becomes on the order of $\mathcal{O}{({1/k})}$ for $0 < q < 1$ and on the order of $\mathcal{O}{({\log{k/k}})}$ for $q = 1$ with high probability. By strong convexity, this translates into a rate of $\overset{\sim}{\mathcal{O}}{({1/k^{2}})}$ in the suboptimality of the objective values (where $\overset{\sim}{\mathcal{O}}$ ignores the logarithmic terms in $k$ appearing when $q = 1$.). We call this "subtraction operation", bias removal. Algorithm DRR describes how this can be implemented. In a practical implementation, the number of cycles can be fixed in advance to a certain number $K$, and the estimation of the bias can be done only once at the last ($K$-th) cycle (see Step $({ii})$ of Algorithm 1) and then can be subtracted from the averaged iterates.

Input: Initial point x00 ∈ ℝn, number of cycles K ∈ ℕ, suffix averaging parameter q ∈ (0, 1], stepsize parameters R &gt; 0 and s ∈ (1/2,1).
Initialization: ${\overline{x}}_{1,0} = 0 \in {\mathbb{R}}^{n}$, v̂0 = 0 ∈ ℝn, ${\overline{\alpha}}_{1,0} = 0 \in {\mathbb{R}}$, Ĥ0 = 0 ∈ ℝn × n.

For each cycle k = 0, 1, 2, …, K − 1:

Pick a permutation σk of {1,…,m} uniformly at random.
Compute xik by: ${{x_{i}^{k} = {x_{i - 1}^{k} - {\alpha_{k}{\nabla f_{\sigma_{k}{(i)}}}\left( x_{i - 1}^{k} \right)}}},{\alpha_{k} = \frac{R}{\left( {k + 1} \right)^{s}}}}.$
// Precompute for the bias estimation only for the last cycle

Set outer iterate: x0k + 1 = xmk.

Update the simple average of the iterates and the stepsize:

${{\overline{x}}_{1,{k + 1}} = {{\frac{k}{k + 1}{\overline{x}}_{1,k}} + {\frac{1}{k + 1}x_{0}^{k}}}},{{\overline{\alpha}}_{1,{k + 1}} = {{\frac{k}{k + 1}{\overline{\alpha}}_{1,k}} + {\frac{1}{k + 1}\alpha_{k}}}}$

If q ∈, compute q-suffix averages from the simple averages:

$${{{\overline{x}}_{q,K} = \frac{{\overline{x}}_{1,K} - {q{\overline{x}}_{1,{{({1 - q})}K}}}}{1 - q}},{{\overline{\alpha}}_{q,K} = \frac{{\overline{\alpha}}_{1,K} - {q{\overline{\alpha}}_{1,{{({1 - q})}K}}}}{1 - q}}}.$$

Estimate the bias by the formula: ${\hat{b}}_{q,K} = {- {{\overline{\alpha}}_{q,K}{\hat{H}}_{m}^{- 1}{\hat{v}}_{m}}}$ in the last cycle.

Output: ${\overline{x}}_{q,K} - {\hat{b}}_{q,K}$.
Algorithm 1 De-biased Random Reshuffling (DRR)

The bias removal of the DRR algorithm requires an $n \times n$ matrix inversion which requires $\approx n^{3}$ arithmetic operations (if there is more structure on the Hessian of $f_{i}$ such as low-rankness or sparsity this could be improved to $\approx n^{2}$), but accelerates the convergence with high-probability. For small or moderate $n$, this could be done efficiently and incrementally processing the functions one at a time; however for large $n$ this may be impractical or infeasible limiting the applicability of this method. Nevertheless, the expensive matrix inversion step does not need to be done at every cycle, it suffices to do it only once at the end of the last cycle. Figure 3 compares the performance of SGD, RR and DRR methods in terms of the histogram of the distance to the optimal solution (left panel) and suboptimality of the objective function (right panel) on a randomly generated quadratic example with a dense Hessian matrix with parameters $m = 50$, $n = 20$. For a fair comparison, we run all the algorithms with the same amount of CPU time. In particular, in Figure 3 we run DRR for 0.5 seconds including the bias correction step, and run RR and SGD for the same amount of time. We observe that SGD is consistently performing the worst, whereas DRR leads often to a better solution than RR both in terms of distances to the optimal solution and suboptimality. Figure 3 repeats the experiment with 5 seconds, we see a clearer separation between the histograms of the RR method and the De-biased RR method. We see similar results when we run the algorithms for different amount of times. These results show that the asymptotic performance would get better if one removes the bias term and typically we need more cycles for the bias correction term to be effective. The results also illustrate the results of Theorem 3 and 4 on the biasedness of the RR iterations in the sense that asymptotically an improvement can be obtained by subtracting the bias.

## Conclusion

We analyzed the random reshuffling (RR) method for minimizing a finite sum of convex component functions. When the objective function is strongly convex and the component functions are smooth, averaged RR iterates converge at rate $\sim {1/k^{s}}$ to the optimal solution almost surely (which translates into a rate of $1/k^{2s}$ in the suboptimality of the objective value) for a diminishing stepsize $\alpha_{k} = {\Theta{({1/k^{s}})}}$ with $s \in {({1/2},1)}$. This is faster than SGD's $\Omega{(\frac{1}{k})}$ rate. Viewing RR as a gradient descent method with random gradient errors, this result builds on first showing that gradient errors $E_{k}$ satisfying $E_{k} = {\mathcal{O}{(\alpha_{k})}}$ and then relating the gradient error sequence to an i.i.d sequence to which martingale theory is applicable. Note that the gradient errors in SGD are larger with a $\mathcal{O}{}$ variance, which leads to a less accurate gradient descent direction. Beyond RR and SGD comparison, these results also give insight into the fast convergence properties of without-replacement sampling strategies compared to with-replacement sampling strategies.

After characterizing the convergence rate of RR, we look into second-order terms in the asymptotic expansion of the averaged RR iterates and obtain high probability bounds. We use these bounds to develop a new method that can accelerate the convergence rate of RR to $\mathcal{O}{(\frac{1}{k^{2}})}$ with high probability. Finally, we show that the $\mathcal{O}{(\frac{1}{k^{2}})}$ rate can also be achieved in expectation (which is a weaker notion of convergence with respect to convergence with high probability) for the $s = 1$ case by adjusting the stepsize to the strong convexity constant of the objective properly.

Figure 2: Comparison of RR, Debiased-RR (DRR) and SGD when component functions are random quadratics with m = 50, n = 20 and with simulation time 0.5 seconds over 500 sample paths. Top, left: Histograms of distk for RR, DRR and SGD. Bottom, left: Histograms of distk for RR and DRR only (without SGD). Top, right: Histograms of the suboptimality in objective value for RR, DRR and SGD. Bottom, right: Histograms of the suboptimality in objective value for RR and DRR only (without SGD).
Figure 3: Comparison of RR, De-biased-RR (DRR) and SGD. The simulation framework and parameters are the same as those in Fig. 3 except that the simulation time is 5 seconds instead for each path.
