<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SARAH: A Novel Method for Machine Learning Problems Using Stochastic Recursive Gradient

Topics include Stochastic gradients, Learning, SARAH, Stochastic recursive gradients.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we propose a StochAstic Recursive grAdient algoritHm (SARAH), as well as its practical variant SARAH+, as a novel approach to the finite-sum minimization problems. Different from the vanilla SGD and other modern stochastic methods such as SVRG, S2GD, SAG and SAGA, SARAH admits a simple recursive framework for updating stochastic gradient estimates; when comparing to SAG/SAGA, SARAH does not require a storage of past gradients. The linear convergence rate of SARAH is proven under strong convexity assumption. We also prove a linear convergence rate (in the strongly convex case) for an inner loop of SARAH, the property that SVRG does not possess. Numerical experiments demonstrate the efficiency of our algorithm.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We are interested in solving a problem of the form where each $f_{i}$, $i \in {\lbrack n\rbrack}\overset{\text{def}}{=}{\{ 1,\ldots,n\}}$, is convex with a Lipschitz continuous gradient. Throughout the paper, we assume that there exists an optimal solution $w^{\ast}$ of.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, many advanced optimization methods have been developed for problem. While the objective function is smooth and convex, the traditional optimization methods, such as gradient descent (GD) or Newton method are often impractical for this problem, when $n$ -- the number of training samples and hence the number of $f_{i}$'s -- is very large. In particular, GD updates iterates as follows Under strong convexity assumption on $P$ and with appropriate choice of $\eta_{t}$, GD converges at a linear rate in terms of objective function values $P{(w_{t})}$. However, when $n$ is large, computing ${\nabla P}{(w_{t})}$ at each iteration can be prohibitive.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

As an alternative, stochastic gradient descent (SGD)^11^1We mark here that even though stochastic gradient is referred to as SG in literature, the term stochastic gradient descent (SGD) has been widely used in many important works of large-scale learning, including SAG/SAGA, SDCA, SVRG and MISO., originating from the seminal work of Robbins and Monro in 1951, has become the method of choice for solving. At each step, SGD picks an index $i \in {\lbrack n\rbrack}$ uniformly at random, and updates the iterate as $w_{t + 1} = {w_{t} - {\eta_{t}{\nabla f_{i}}{(w_{t})}}}$, which is up-to $n$ times cheaper than an iteration of a full gradient method. The convergence rate of SGD is slower than that of GD, in particular, it is sublinear in the strongly convex case. The tradeoff, however, is advantageous due to the tremendous per-iteration savings and the fact that low accuracy solutions are sufficient.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This trade-off has been thoroughly analyzed. Unfortunately, in practice SGD method is often too slow and its performance is too sensitive to the variance in the sample gradients ${\nabla f_{i}}{(w_{t})}$. Use of mini-batches (averaging multiple sample gradients ${\nabla f_{i}}{(w_{t})}$) was used in to reduce the variance and improve convergence rate by constant factors. Using diminishing sequence $\{\eta_{t}\}$ is used to control the variance, but the practical convergence of SGD is known to be very sensitive to the choice of this sequence, which needs to be hand-picked.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, a class of more sophisticated algorithms have emerged, which use the specific finite-sum form of and combine some deterministic and stochastic aspects to reduce variance of the steps. The examples of these methods are SAG/SAGA, SDCA, SVRG, DIAG, MISO and S2GD, all of which enjoy faster convergence rate than that of SGD and use a fixed learning rate parameter $\eta$. In this paper we introduce a new method in this category, SARAH, which further improves several aspects of the existing methods. In Table 2 we summarize complexity and some other properties of the existing methods and SARAH when applied to strongly convex problems. Although SVRG and SARAH have the same convergence rate, we introduce a practical variant of SARAH that outperforms SVRG in our experiments.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fixed Learning Rate Low Storage Cost $\mathcal{O}\left({n + \left(\sqrt{n}/\epsilon \right)} \right)$ SARAH (one outer loop) Table 1: Comparisons between different algorithms for strongly convex functions. κ = L/μ is the condition number. Table 2: Comparisons between different algorithms for convex functions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In addition, theoretical results for complexity of the methods or their variants when applied to general convex functions have been derived. In Table 2 we summarize the key complexity results, noting that convergence rate is now sublinear.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

In this paper, we propose a novel algorithm which combines some of the good properties of existing algorithms, such as SAGA and SVRG, while aiming to improve on both of these methods. In particular, our algorithm does not take steps along a stochastic gradient direction, but rather along an accumulated direction using past stochastic gradient information (as in SAGA) and occasional exact gradient information (as in SVRG). We summarize the key properties of the proposed algorithm below.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Similarly to SVRG, SARAH's iterations are divided into the outer loop where a full gradient is computed and the inner loop where only stochastic gradient is computed. Unlike the case of SVRG, the steps of the inner loop of SARAH are based on accumulated stochastic information.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Like SAG/SAGA and SVRG, SARAH has a sublinear rate of convergence for general convex functions, and a linear rate of convergence for strongly convex functions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

SARAH uses a constant learning rate, whose size is larger than that of SVRG. We analyze and discuss the optimal choice of the learning rate and the number of inner loop steps. However, unlike SAG/SAGA but similar to SVRG, SARAH does not require a storage of $n$ past stochastic gradients.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

We also prove a linear convergence rate (in the strongly convex case) for the inner loop of SARAH, the property that SVRG does not possess. We show that the variance of the steps inside the inner loop goes to zero, thus SARAH is theoretically more stable and reliable than SVRG.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

We provide a practical variant of SARAH based on the convergence properties of the inner loop, where the simple stable stopping criterion for the inner loop is used (see Section 4 for more details). This variant shows how SARAH can be made more stable than SVRG in practice.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Stochastic Recursive Gradient Algorithm", "weight": 1.0} -->

Now we are ready to present our SARAH (Algorithm 1).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Stochastic Recursive Gradient Algorithm", "weight": 1.0} -->

Parameters: the learning rate η > 0 and the inner loop size m. Initialize: ${\overset{\sim}{w}}_{0}$ $v_{0} = {\frac{1}{n}{\sum_{i = 1}^{n}{{\nabla f_{i}}{(w_{0})}}}}$ Sample it uniformly at random from [n] Set ${\overset{\sim}{w}}_{s} = w_{t}$ with t chosen uniformly at random from {0, 1, …, m} The key step of the algorithm is a recursive update of the stochastic gradient estimate (SARAH update) followed by the iterate update: For comparison, SVRG update can be written in a similar way as Observe that in SVRG, $v_{t}$ is an unbiased estimator of the gradient, while it is not true for SARAH.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Stochastic Recursive Gradient Algorithm", "weight": 1.0} -->

Hence, SARAH is different from SGD and SVRG type of methods, however, the following total expectation holds, ${{\mathbb{E}}{\lbrack v_{t}\rbrack}} = {{\mathbb{E}}{\lbrack{{\nabla P}{(w_{t})}}\rbrack}}$, differentiating SARAH from SAG/SAGA.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Stochastic Recursive Gradient Algorithm", "weight": 1.0} -->

SARAH is similar to SVRG since they both contain outer loops which require one full gradient evaluation per outer iteration followed by one full gradient descent step with a given learning rate. The difference lies in the inner loop, where SARAH updates the stochastic step direction $v_{t}$ recursively by adding and subtracting component gradients to and from the previous $v_{t - 1}{({t \geq 1})}$. Each inner iteration evaluates $2$ stochastic gradients and hence the total work per outer iteration is $\mathcal{O}{({n + m})}$ in terms of the number of gradient evaluations. Note that due to its nature, without running the inner loop, i.e., $m = 1$, SARAH reduces to the GD algorithm.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

To proceed with the analysis of the proposed algorithm, we will make the following common assumptions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 1 ($L$-smooth)", "weight": 1.0} -->

Each $f_{i}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, $i \in {\lbrack n\rbrack}$, is $L$-smooth, i.e., there exists a constant $L > 0$ such that Note that this assumption implies that ${P{(w)}} = {\frac{1}{n}{\sum_{i = 1}^{n}{f_{i}{(w)}}}}$ is also *L-smooth*. The following strong convexity assumption will be made for the appropriate parts of the analysis, otherwise, it would be dropped.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2a ($\\mu$-strongly convex)", "weight": 1.0} -->

The function $P:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, is $\mu$-strongly convex, i.e., there exists a constant $\mu > 0$ such that ${{\forall w},w'} \in {\mathbb{R}}^{d}$, Another, stronger, assumption of $\mu$-strong convexity for will also be imposed when required in our analysis. Note that Assumption 2b implies Assumption 2a. ‣ 3 Theoretical Analysis ‣ SARAH: A Novel Method for Machine Learning Problems Using Stochastic Recursive Gradient") but not vice versa.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 2b", "weight": 1.0} -->

Under Assumption 2a. ‣ 3 Theoretical Analysis ‣ SARAH: A Novel Method for Machine Learning Problems Using Stochastic Recursive Gradient"), let us define the (unique) optimal solution of as $w^{\ast}$, Then strong convexity of $P$ implies that We note here, for future use, that for strongly convex functions of the form, arising in machine learning applications, the condition number is defined as $\kappa\overset{\text{def}}{=}{L/\mu}$. Furthermore, we should also notice that Assumptions 2a. ‣ 3 Theoretical Analysis ‣ SARAH: A Novel Method for Machine Learning Problems Using Stochastic Recursive Gradient") and 2b both cover a wide range of problems, e.g. $l_{2}$-regularized empirical risk minimization problems with convex losses.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 2b", "weight": 1.0} -->

Finally, as a special case of the strong convexity of all $f_{i}$'s with $\mu = 0$, we state the general convexity assumption, which we will use for convergence analysis.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Each function $f_{i}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, $i \in {\lbrack n\rbrack}$, is convex, i.e., Again, we note that Assumption 2b implies Assumption 3, but Assumption 2a. ‣ 3 Theoretical Analysis ‣ SARAH: A Novel Method for Machine Learning Problems Using Stochastic Recursive Gradient") does not. Hence in our analysis, depending on the result we aim, we will require Assumption 3 to hold by itself, or Assumption 2a. ‣ 3 Theoretical Analysis ‣ SARAH: A Novel Method for Machine Learning Problems Using Stochastic Recursive Gradient") and Assumption 3 to hold together, or Assumption 2b to hold by itself. We will always use Assumption 1. ‣ 3 Theoretical Analysis ‣ SARAH: A Novel Method for Machine Learning Problems Using Stochastic Recursive Gradient").

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Our iteration complexity analysis aims to bound the number of outer iterations $\mathcal{T}$ (or total number of stochastic gradient evaluations) which is needed to guarantee that ${\|{{\nabla P}{(w_{\mathcal{T}})}}\|}^{2} \leq \epsilon$. In this case we will say that $w_{\mathcal{T}}$ is an $\epsilon$-accurate solution. However, as is common practice for stochastic gradient algorithms, we aim to obtain the bound on the number of iterations, which is required to guarantee the bound on the expected squared norm of a gradient, i.e.,

<!-- chunk {"id": "body-0027", "role": "body", "section": "Linearly Diminishing Step-Size in a Single Inner Loop", "weight": 1.0} -->

The most important property of the SVRG algorithm is the variance reduction of the steps. This property holds as the number of outer iteration grows, but it does not hold, if only the number of inner iterations increases. In other words, if we simply run the inner loop for many iterations (without executing additional outer loops), the variance of the steps does not reduce in the case of SVRG, while it goes to zero in the case of SARAH. To illustrate this effect, let us take a look at Figures 2 and 2.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Linearly Diminishing Step-Size in a Single Inner Loop", "weight": 1.0} -->

In Figure 2, we applied one outer loop of SVRG and SARAH to a sum of $5$ quadratic functions in a two-dimensional space, where the optimal solution is at the origin, the black lines and black dots indicate the trajectory of each algorithm and the red point indicates the final iterate. Initially, both SVRG and SARAH take steps along stochastic gradient directions towards the optimal solution. However, later iterations of SVRG wander randomly around the origin with large deviation from it, while SARAH follows a much more stable convergent trajectory, with a final iterate falling in a small neighborhood of the optimal solution.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Linearly Diminishing Step-Size in a Single Inner Loop", "weight": 1.0} -->

In Figure 2, the x-axis denotes the *number of effective passes* which is equivalent to the number of passes through all of the data in the dataset, the cost of each pass being equal to the cost of one full gradient evaluation; and y-axis represents ${\| v_{t}\|}^{2}$. Figure 2 shows the evolution of ${\| v_{t}\|}^{2}$ for SARAH, SVRG, SGD+ (SGD with decreasing learning rate) and FISTA (an accelerated version of GD ) with $m = {4n}$, where the left plot shows the trend over multiple outer iterations and the right plot shows a single outer iteration^44^4In the plots of Figure 2, since the data for SVRG is noisy, we smooth it by using moving average filters with spans 100 for the left plot and 10 for the right one.. We can see that for SVRG, ${\| v_{t}\|}^{2}$ decreases over the outer iterations, while it has an increasing trend or oscillating trend for each inner loop.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Linearly Diminishing Step-Size in a Single Inner Loop", "weight": 1.0} -->

In contrast, SARAH enjoys decreasing trends both in the outer and the inner loop iterations.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Linearly Diminishing Step-Size in a Single Inner Loop", "weight": 1.0} -->

We will now show that the stochastic steps computed by SARAH converge linearly in the inner loop. We present two linear convergence results based on our two different assumptions of $\mu$-*strong convexity*. These results substantiate our conclusion that SARAH uses more stable stochastic gradient estimates than SVRG. The following theorem is our first result to demonstrate the linear convergence of our stochastic recursive step $v_{t}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

In this section, we derive the general convergence rate results for Algorithm 1. First, we present two important Lemmas as the foundation of our theory. Then, we proceed to prove sublinear convergence rate of a single outer iteration when applied to general convex functions. In the end, we prove that the algorithm with multiple outer iterations has linear convergence rate in the strongly convex case.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Strongly Convex Case", "weight": 1.0} -->

We now turn to the discussion of the linear convergence rate of SARAH under the strong convexity assumption on $P$. From Theorem 2, for any $s \geq 1$, using property of the $\mu$-*strongly convex* $P$, we have Let us define $\sigma_{m}\overset{\text{def}}{=}{\frac{1}{\mu\eta{({m + 1})}} + \frac{\etaL}{2 - {\etaL}}}$. Then by choosing $\eta$ and $m$ such that $\sigma_{m} < 1$, and applying recursively, we are able to reach the following convergence result.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Theorem 4 implies that any $\eta < {1/L}$ will work for SARAH. Let us compare our convergence rate to that of SVRG. The linear rate of SVRG, as presented, is given by We observe that it implies that the learning rate has to satisfy $\eta < {1/{({4L})}}$, which is a tighter restriction than $\eta < {1/L}$ required by SARAH. In addition, with the same values of $m$ and $\eta$, the rate or convergence of (the outer iterations) of SARAH is always smaller than that of SVRG.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 2", "weight": 1.0} -->

To further demonstrate the better convergence properties of SARAH, let us consider following optimization problem which can be interpreted as the best convergence rates for different values of $m$, for both SARAH and SVRG. After simple calculations, we plot both learning rates and the corresponding theoretical rates of convergence, as shown in Figure 3, where the right plot is a zoom-in on a part of the middle plot. The left plot shows that the optimal learning rate for SARAH is significantly larger than that of SVRG, while the other two plots show significant improvement upon outer iteration convergence rates for SARAH over SVRG.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Based on Theorem 4, we are able to derive the following total complexity for SARAH in the strongly convex case.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Practical Variant", "weight": 1.0} -->

While SVRG is an efficient variance-reducing stochastic gradient method, one of its main drawbacks is the sensitivity of the practical performance with respect to the choice of $m$. It is know that $m$ should be around $\mathcal{O}{(\kappa)}$,^55^5 In practice, when $n$ is large, $P{(w)}$ is often considered as a regularized Empirical Loss Minimization problem with regularization parameter $\lambda = \frac{1}{n}$, then ${\kappa \sim {\mathcal{O}{(n)}}}.$ while it still remains unknown that what the exact best choice is. In this section, we propose a practical variant of SARAH as SARAH+ (Algorithm 2), which provides an automatic and adaptive choice of the inner loop size $m$. Guided by the linear convergence of the steps in the inner loop, demonstrated in Figure 2, we introduce a stopping criterion based on the values of ${\| v_{t}\|}^{2}$ while upper-bounding the total number of steps by a large enough $m$ for robustness.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Practical Variant", "weight": 1.0} -->

The other modification compared to SARAH (Algorithm 1) is the more practical choice ${\overset{\sim}{w}}_{s} = w_{t}$, where $t$ is the last index of the particular inner loop, instead of randomly selected intermediate index.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Practical Variant", "weight": 1.0} -->

Parameters: the learning rate η > 0, 0 < γ ≤ 1 and the maximum inner loop size m. Initialize: ${\overset{\sim}{w}}_{0}$ $v_{0} = {\frac{1}{n}{\sum_{i = 1}^{n}{{\nabla f_{i}}{(w_{0})}}}}$ Sample it uniformly at random from [n] Set ${\overset{\sim}{w}}_{s} = w_{t}$ Different from SARAH, SARAH+ provides a possibility of earlier termination and unnecessary careful choices of $m$, and it also covers the classical gradient descent when we set $\gamma = 1$ (since the while loop does not proceed). In Figure 4 we present the numerical performance of SARAH+ with different $\gamma$s on *rcv1* and *news20* datasets. The size of the inner loop provides a trade-off between the fast sub-linear convergence in the inner loop and linear convergence in the outer loop.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Practical Variant", "weight": 1.0} -->

From the results, it appears that $\gamma = {1/8}$ is the optimal choice. With a larger $\gamma$, i.e. $\gamma > {1/8}$, the iterates in the inner loop do not provide sufficient reduction, before another full gradient computation is required, while with $\gamma < {1/8}$ an unnecessary number of inner steps is performed without gaining substantial progress. Clearly $\gamma$ is another parameter that requires tuning, however, in our experiments, the performance of SARAH+ has been very robust with respect to the choices of $\gamma$ and did not vary much from one data set to another.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Practical Variant", "weight": 1.0} -->

Similarly to SVRG, ${\| v_{t}\|}^{2}$ decreases in the outer iterations of SARAH+. However, unlike SVRG, SARAH+ also inherits from SARAH the consistent decrease of ${\| v_{t}\|}^{2}$ in expectation in the inner loops. It is not possible to apply the same idea of adaptively terminating the inner loop of SVRG based on the reduction in ${\| v_{t}\|}^{2}$, as ${\| v_{t}\|}^{2}$ may have side fluctuations as shown in Figure 2.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

To support the theoretical analyses and insights, we present our empirical experiments, comparing SARAH and SARAH+ with the state-of-the-art first-order methods for $\ell_{2}$-regularized logistic regression problems with on datasets *covtype, ijcnn1, news20* and *rcv1* ^66^6All datasets are available at For *ijcnn1* and *rcv1* we use the predefined testing and training sets, while *covtype* and *news20* do not have test data, hence we randomly split the datasets with $70\%$ for training and $30\%$ for testing. Some statistics of the datasets are summarized in Table 3.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The penalty parameter $\lambda$ is set to $1/n$ as is common practice. Note that like SVRG/S2GD and SAG/SAGA, SARAH also allows an efficient sparse implementation named "lazy updates". We conduct and compare numerical results of SARAH with SVRG, SAG, SGD+ and FISTA. SVRG and SAG are classic modern stochastic methods. SGD+ is SGD with decreasing learning rate $\eta = {\eta_{0}/{({k + 1})}}$ where $k$ is the number of effective passes and $\eta_{0}$ is some initial constant learning rate. FISTA is the Fast Iterative Shrinkage-Thresholding Algorithm, well-known as an efficient accelerated version of the gradient descent. Even though for each method, there is a theoretical safe learning rate, we compare the results for the best learning rates in hindsight.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In particular, to validate the efficiency of our practical variant SARAH+, we provide an insight into how important the choices of $m$ and $\eta$ are for SVRG and SARAH in Table 4 and Figure 6. Table 4 presents the optimal choices of $m$ and $\eta$ for each of the algorithm, while Figure 6 shows the behaviors of SVRG and SARAH with different choices of $m$ for *covtype* and *ijcnn1*, where $m^{\ast}$s denote the best choices. In Table 4, the optimal learning rates of SARAH vary less among different datasets compared to all the other methods and they approximate the theoretical upper bound for SARAH ($1/L$); on the contrary, for the other methods the empirical optimal rates can exceed their theoretical limits (SVRG with $1/{({4L})}$, SAG with $1/{({16L})}$, FISTA with $1/L$). This empirical studies suggest that it is much easier to tune and find the ideal learning rate for SARAH.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

As observed in Figure 6, the behaviors of both SARAH and SVRG are quite sensitive to the choices of $m$. With improper choices of $m$, the loss residuals can be increased considerably from $10^{- 15}$ to $10^{- 3}$ on both *covtype* in 40 effective passes and *ijcnn1* in 17 effective passes for SARAH/SVRG.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We propose a new variance reducing stochastic recursive gradient algorithm SARAH, which combines some of the properties of well known existing algorithms, such as SAGA and SVRG. For smooth convex functions, we show a sublinear convergence rate, while for strongly convex cases, we prove the linear convergence rate and the computational complexity as those of SVRG and SAG. However, compared to SVRG, SARAH's convergence rate constant is smaller and the algorithms is more stable both theoretically and numerically. Additionally, we prove the linear convergence for inner loops of SARAH which support the claim of stability. Based on this convergence we derive a practical version of SARAH, with a simple stopping criterion for the inner loops.
