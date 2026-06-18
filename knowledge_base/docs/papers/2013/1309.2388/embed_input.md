<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Minimizing Finite Sums with the Stochastic Average Gradient

Topics include Stochastic average gradient, Finite-sum optimization, Variance reduction, Linear convergence, Convex optimization, Non-uniform sampling, Empirical risk minimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Gives the extended analysis of SAG for smooth finite-sum convex objectives, proving faster rates than black-box stochastic gradient methods and linear convergence under strong convexity. Compared with the shorter NeurIPS paper, this version clarifies the Lyapunov-style proof, step-size behavior, storage tradeoffs, and non-uniform sampling ideas that made SAG a canonical variance-reduction method.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose the stochastic average gradient (SAG) method for optimizing the sum of a finite number of smooth convex functions. Like stochastic gradient (SG) methods, the SAG method's iteration cost is independent of the number of terms in the sum. However, by incorporating a memory of previous gradient values the SAG method achieves a faster convergence rate than black-box SG methods. The convergence rate is improved from O(1/k^{1/2}) to O(1/k) in general, and when the sum is strongly-convex the convergence rate is improved from the sub-linear O(1/k) to a linear convergence rate of the form O(p^k) for p \textless{} 1. Further, in many cases the convergence rate of the new method is also faster than black-box deterministic gradient methods, in terms of the number of gradient evaluations. Numerical experiments indicate that the new algorithm often dramatically outperforms existing SG and deterministic gradient methods, and that the performance may be further improved through the use of non-uniform sampling strategies.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A plethora of the optimization problems arising in practice involve computing a minimizer of a finite sum of functions measuring misfit over a large number of data points. A classical example is least-squares regression,

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

where the $a_{i} \in {\mathbb{R}}^{p}$ and $b_{i} \in {\mathbb{R}}$ are the data samples associated with a regression problem. Another important example is logistic regression,

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

where the $a_{i} \in {\mathbb{R}}^{p}$ and $b_{i} \in {\{{- 1},1\}}$ are the data samples associated with a binary classification problem. A key challenge arising in modern applications is that the number of data points $n$ (also known as *training examples*) can be extremely large, while there is often a large amount of redundancy between examples. The most wildly successful class of algorithms for taking advantage of the *sum* structure for problems where $n$ is very large are *stochastic gradient* (SG) methods \Robbins and Monro, [1951, Bottou and LeCun, 2003\]. Although the theory behind SG methods allows them to be applied more generally, SG methods are often used to solve the problem of optimizing a finite sample average,

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we focus on such *finite data* problems where each $f_{i}$ is *smooth* and *convex*.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In addition to this basic setting, we will also be interested in cases where the sum $g$ has the additional property that it is *strongly-convex*. This often arises due to the use of a strongly-convex regularizer such as the squared $\ell_{2}$-norm, resulting in problems of the form

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

where each $l_{i}$ is a data-misfit function (as in least-squares and logistic regression) and the positive scalar $\lambda$ controls the strength of the regularization. These problems can be put in the framework of by using the choice

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The resulting function $g$ will be strongly-convex provided that the individual loss functions $l_{i}$ are convex. An extensive list of convex loss functions used in a statistical data-fitting context is given by Teo et al., and non-smooth loss functions (or regularizers) can also be put in this framework by using smooth approximations (for example, see Nesterov ).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

For optimizing problem, the standard *deterministic* or *full gradient* (FG) method, which dates back to Cauchy, uses iterations of the form

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $\alpha_{k}$ is the step size on iteration $k$. Assuming that a minimizer $x^{\ast}$ exists, then under standard assumptions the sub-optimality achieved on iteration $k$ of the FG method with a constant step size is given by

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

when $g$ is convex \see Nesterov, [2004, Corollary 2.1.2\]. This results in a *sublinear* convergence rate. When $g$ is strongly-convex, the error also satisfies

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

for some $\rho < 1$ which depends on the condition number of $g$ \see Nesterov, [2004, Theorem 2.1.5\]. This results in a *linear* convergence rate, which is also known as a *geometric* or *exponential* rate because the error is cut by a fixed fraction on each iteration. Unfortunately, the FG method can be unappealing when $n$ is large because its iteration cost scales linearly in $n$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main appeal of SG methods is that they have an iteration cost which is *independent* of $n$, making them suited for modern problems where $n$ may be very large. The basic SG method for optimizing uses iterations of the form

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

where at each iteration an index $i_{k}$ is sampled uniformly from the set $\{ 1,\ldots,n\}$. The randomly chosen gradient $f_{i_{k}}^{\prime}{(x^{k})}$ yields an unbiased estimate of the true gradient $g^{\prime}{(x^{k})}$ and one can show under standard assumptions (see \Nemirovski et al., ) that, for a suitably chosen decreasing step-size sequence $\{\alpha_{k}\}$, the SG iterations have an expected sub-optimality for convex objectives of

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

and an expected sub-optimality for strongly-convex objectives of

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

In these rates, the expectations are taken with respect to the selection of the $i_{k}$ variables. These sublinear rates are slower than the corresponding rates for the FG method, and under certain assumptions these convergence rates are *optimal* in a model of computation where the algorithm only accesses the function through unbiased measurements of its objective and gradient (see Nemirovski and Yudin, Nemirovski et al., Agarwal et al. ). Thus, we should not expect to be able to obtain the convergence rates of the FG method if the algorithm only relies on unbiased gradient measurements. Nevertheless, by using the stronger assumption that the functions are sampled from a finite dataset, in this paper we show that we can achieve the convergence rates of FG methods while preserving the iteration complexity of SG methods.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

The primary contribution of this work is the analysis of a new algorithm that we call the *stochastic average gradient* (SAG) method, a randomized variant of the incremental aggregated gradient (IAG) method of Blatt et al.. The SAG method has the low iteration cost of SG methods, but achieves the convergence rates stated above for the FG method. The SAG iterations take the form

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

where at each iteration a random index $i_{k}$ is selected and we set

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

That is, like the FG method, the step incorporates a gradient with respect to each function. But, like the SG method, each iteration only computes the gradient with respect to a single example and the cost of the iterations is independent of $n$. Despite the low cost of the SAG iterations, we show in this paper that with a constant step-size *the SAG iterations have an $O{({1/k})}$ convergence rate for convex objectives and a linear convergence rate for strongly-convex objectives*, like the FG method. That is, by having access to $i_{k}$ and by keeping a *memory* of the most recent gradient value computed for each index $i$, this iteration achieves a faster convergence rate than is possible for standard SG methods. Further, in terms of effective passes through the data, we will also see that for many problems the convergence rate of the SAG method is also faster than is possible for standard FG methods.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the main contexts where minimizing the sum of smooth convex functions arises is machine learning. In this context, $g$ is often an *empirical* risk (or a regularized empirical risk), which is a sample average approximation to the *true* risk that we are interested. It is known that with $n$ training examples the empirical risk minimizer (ERM) has an error for the true risk of $O{({1/\sqrt{n}})}$ in the convex case and $O{({1/n})}$ in the strongly-convex case. Since these rates are achieved by doing one pass through the data with an SG method, in the worst case the SAG algorithm applied to the empirical risk cannot improve the convergence rate in terms of the true risk over this simple method. Nevertheless, Srebro and Sridharan note that "overwhelming empirical evidence shows that for almost all actual data, the ERM *is* better. However, we have no understanding of why this happens".

<!-- chunk {"id": "body-0023", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although our analysis does not give insight into the better performance of ERM, our analysis shows that the SAG algorithm will be preferable to SG methods for finding the ERM and hence for many machine learning applications.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Introduction", "weight": 1.5} -->

The next section reviews several closely-related algorithms from the literature, including previous attempts to combine the appealing aspects of FG and SG methods. However, despite $60$ years of extensive research on SG methods, with a significant portion of the applications focusing on finite datasets, we believe that this is the first general method that achieves the convergence rates of FG methods while preserving the iteration cost of standard SG methods. Section 3 states the (standard) assumptions underlying our analysis and gives our convergence rate results. Section 4 discusses practical implementation issues including how we adaptively set the step size and how we can reduce the storage cost needed by the algorithm. For example, we can reduce the memory requirements from $O{({np})}$ to $O{(n)}$ in the common scenario where each $f_{i}$ only depends on a linear function of $x$, as in least-squares and logistic regression. Section 5 presents a numerical comparison of an implementation based on SAG to competitive SG and FG methods, indicating that the method may be very useful for problems where we can only afford to do a few passes through a data set.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Introduction", "weight": 1.5} -->

A preliminary conference version of this work appears in Le Roux et al., and we extend this work in various ways. Most notably, the analysis in the prior work focuses only on showing linear convergence rates in the strongly-convex case while the present work also gives an $O{({1/k})}$ convergence rate for the general convex case. In the prior work we show (Proposition 1) that a small step-size gives a slow linear convergence rate (comparable to the rate of FG methods in terms of effective passes through the data), while we also show (Proposition 2) that a much larger step-size yields a much faster convergence rate, but this requires that $n$ is sufficiently large compared to the condition number of the problem. In the present work (Section 3) our analysis yields a very fast convergence rate using a large step-size (Theorem 1), even when this condition required by the prior work is not satisfied. Surprisingly, for ill-conditioned problems our new analysis shows that using SAG iterations can be nearly $n$ times as fast as the standard gradient method.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Introduction", "weight": 1.5} -->

To prove this stronger result, Theorem 1 employs a Lyapunov function that generalizes the Lyapunov functions used in Propositions 1 and 2 of the previous work. This new Lyapunov function leads to a unified proof for both the convex and the strongly-convex cases, and for both well-conditioned and ill-conditioned problems. However, this more general Lyapunov function leads to a more complicated analysis. To significantly simplify the formal proof, we use a computed-aided strategy to verify the non-negativity of certain polynomials that arise in the proof. Beyond this significantly strengthened result, in this work we also argue that yet-faster convergence rates may be achieved by *non-uniform* sampling (Section 4.8) and present numerical results showing that this can lead to drastically improved performance (Section 5.5).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

In our analysis we assume that each function $f_{i}$ in is convex and differentiable, and that each gradient $f_{i}^{\prime}$ is Lipschitz-continuous with constant $L$, meaning that for all $x$ and $y$ in ${\mathbb{R}}^{p}$ and each $i$ we have

<!-- chunk {"id": "body-0028", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

This is a fairly weak assumption on the $f_{i}$ functions, and in cases where the $f_{i}$ are twice-differentiable it is equivalent to saying that the eigenvalues of the Hessians of each $f_{i}$ are bounded above by $L$. We will also assume the existence of at least one minimizer $x^{\ast}$ that achieves the optimal function value. We denote the average iterate by ${\overline{x}}^{k} = {\frac{1}{k}{\sum_{i = 0}^{k - 1}x^{i}}}$, and the variance of the gradient norms at the optimum $x^{\ast}$ by $\sigma^{2} = {\frac{1}{n}{\sum_{i}{\|{f_{i}^{\prime}{(x^{\ast})}}\|}^{2}}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

Our convergence results consider two different initializations for the $y_{i}^{0}$ variables: setting $y_{i}^{0} = 0$ for all $i$, or setting them to the centered gradient at the initial point $x^{0}$ given by $y_{i}^{0} = {{f_{i}^{\prime}{(x^{0})}} - {g^{\prime}{(x^{0})}}}$. We note that all our convergence results are expressed in terms of expectations with respect to the internal randomization of the algorithm (the selection of the random variables $i_{k}$), and not with respect to the data which is assumed to be deterministic and fixed.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

In addition to this basic convex case discussed above, we will also consider the case where the average function $g = {\frac{1}{n}{\sum_{i = 1}^{n}f_{i}}}$ is strongly-convex with constant $\mu > 0$, meaning that the function $x\mapsto{{g{(x)}} - {\frac{\mu}{2}{\| x\|}^{2}}}$ is convex. For twice-differentiable $g$, this is equivalent to requiring that the eigenvalues of the Hessian of $g$ are bounded below by $\mu$. This is a stronger assumption that is often not satisfied in practical applications. Nevertheless, in many applications we are free to choose a regularizer of the parameters, and thus we can add an $\ell_{2}$-regularization term as in to transform any convex problem into a strongly-convex problem (in this case we have $\mu \geq \lambda$).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

Note that strong-convexity implies the existence of a unique $x^{\ast}$ that achieves the optimal function value.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

Under these standard assumptions, we now state our convergence result.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

In Algorithm 1 we give pseudo-code for an implementation of the basic method, where we use a variable $d$ to track the quantity $({\sum_{i = 1}^{n}y_{i}})$. This section focuses on further implementation details that are useful in practice. In particular, we discuss modifications that lead to better practical performance than the basic Algorithm 1, including ways to reduce the storage cost, how to handle regularization, how to set the step size, using mini-batches, and using non-uniform sampling. Note that an implementation of the algorithm that incorporates many of these aspects is available from the first author's webpage.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Structured gradients and just-in-time parameter updates", "weight": 1.0} -->

For many problems the storage cost of $O{({np})}$ for the $y_{i}^{k}$ vectors is prohibitive, but we can often use the structure of the gradients $f_{i}^{\prime}$ to reduce this cost. For example, a commonly-used specialization of is *linearly-parameterized* models which take form

<!-- chunk {"id": "body-0035", "role": "body", "section": "Structured gradients and just-in-time parameter updates", "weight": 1.0} -->

For problems where the vectors $a_{i}$ are sparse, an individual gradient $f_{i}^{\prime}$ will inherit the sparsity pattern of the corresponding $a_{i}$. However, the update of $x$ in Algorithm 1 appears unappealing since in general $d$ will be dense, resulting in an iteration cost of $O{(p)}$. Nevertheless, we can take advantage of the simple form of the SAG updates to implement a 'just-in-time' variant of the SAG algorithm where the iteration cost is proportional to the number of non-zeroes in $a_{i_{k}}$. In particular, we do this by not explicitly storing the full vector $x^{k}$ after each iteration.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Structured gradients and just-in-time parameter updates", "weight": 1.0} -->

Instead, on each iteration we only compute the elements $x_{j}^{k}$ corresponding to non-zero elements of $a_{i_{k}}$, by applying the *sequence of updates* to each variable $x_{j}^{k}$ since the last iteration where it was non-zero in $a_{i_{k}}$. This sequence of updates can be applied efficiently since it simply involves changing the step size. For example, if variable $j$ has been zero in $a_{i_{k}}$ for $5$ iterations, then we can compute the needed value $x_{j}^{k}$ using

<!-- chunk {"id": "body-0037", "role": "body", "section": "Structured gradients and just-in-time parameter updates", "weight": 1.0} -->

This update allows SAG to be efficiently applied to sparse data sets where $n$ and $p$ are both in the millions or higher but the number of non-zeros is much less than $np$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Re-weighting on early iterations", "weight": 1.0} -->

In the update of $x$ in Algorithm 1, we normalize the direction $d$ by the total number of data points $n$. When initializing with $y_{i}^{0} = 0$ we believe this leads to steps that are too small on early iterations of the algorithm where we have only seen a fraction of the data points, because many $y_{i}$ variables contributing to $d$ are set to the uninformative zero-vector. Following Blatt et al., the more logical normalization is to divide $d$ by $m$, the number of data points that we have seen at least once (which converges to $n$ once we have seen the entire data set), leading to the update $x = {x - {\frac{\alpha}{m}d}}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Re-weighting on early iterations", "weight": 1.0} -->

Although this modified SAG method appears more difficult to analyze, in our experiments we found that running the basic SAG algorithm from the very beginning with this modification outperformed the basic SAG algorithm as well as the SG/SAG hybrid algorithm mentioned in the Section 3. In addition to using the gradient information collected during the first $k$ iterations, this modified SAG algorithm is also advantageous over hybrid SG/SAG algorithms because it only requires estimating a single constant step size.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Exact and efficient regularization", "weight": 1.0} -->

In the case of regularized objectives like, the cost of computing the gradient of the regularizer is independent of $n$. Thus, we can use the exact gradient of the regularizer in the update of $x$, and only use $d$ to approximate the sum of the $l_{i}^{\prime}$ functions. By incorporating the gradient of the regularizer explicitly, the update for $y_{i}$ in Algorithm 1 becomes $y_{i} = {l_{i}^{\prime}{(x)}}$, and in the case of $\ell_{2}$-regularization the update for $x$ becomes

<!-- chunk {"id": "body-0041", "role": "body", "section": "Exact and efficient regularization", "weight": 1.0} -->

If the loss function gradients $l_{i}^{\prime}$ are sparse as in Section 4.1, then these modifications lead to a reduced storage requirement even though the gradient of the regularizer is dense. Further, although the update of $x$ again appears to require dense vector operations, we can implement the algorithm efficiently if the $a_{i}$ are sparse. In particular, to allow efficient multiplication of $x$ by the scalar $({1 - {\alpha\lambda}})$, it is useful to represent $x$ in the form $x = {\kappaz}$, where $\kappa$ is a scalar and $z$ is a vector (as done by Shalev-Shwartz et al. ). Under this representation, we can multiply $x$ by a scalar in $O{}$ by simply updating $\kappa$ (though to prevent $\kappa$ becoming too large or too small we may need to occasionally re-normalize by setting $z = {\kappaz}$ and $\kappa = 1$).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Exact and efficient regularization", "weight": 1.0} -->

To efficiently implement the vector subtraction operation, we can use a variant of the just-in-time updates from Section 4.1. In Algorithm 2, we give pseudo-code for a variant of SAG that includes all of these modifications, and thus uses no full-vector operations. This code uses a vector $y$ to keep track of the scalars $l_{i}^{\prime}{(u_{i}^{k})}$, a vector $C$ to determine whether a data point has previously been visited, a vector $V$ to track the last time a variable was updated, and a vector $S$ to keep track of the cumulative sums needed to implement the just-in-time updates.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Exact and efficient regularization", "weight": 1.0} -->

{Initialization, note that x = κ z.}
{This is the first time we have sampled this data point.}
{Just-in-time calculation of needed values of z.}
{Update the memory y and the direction d.}
Let J be the support of ai
{Update κ and the sum needed for z updates.}
{Final x is κ times the just-in-time update of all z.}
Algorithm 2 SAG variant for minimizing ${\frac{\lambda}{2}{\| x\|}^{2}} + {\frac{1}{n}{\sum_{i = 1}^{n}{l_{i}{({a_{i}^{\top}x})}}}}$, with step size α and ai sparse.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Warm starting", "weight": 1.0} -->

In many scenarios we may need to solve a set of closely-related optimization problems. For example, we may want to apply Algorithm 2 to a regularized objective of the form for several values of the regularization parameter $\lambda$. Rather than solving these problems independently, we might expect to obtain better performance by warm-starting the algorithm. Although initializing $x$ with the solution of a related problem can improve performance, we can expect an even larger performance improvement if we also use the gradient information collected from a run of SAG for a close value of $\lambda$. For example, in Algorithm 2 we could initialize $x$, $y_{i}$, $d$, $m$, and $C_{i}$ based on a previous run of the SAG algorithm. In this scenario, Theorem 1 suggests that it may be beneficial in this setting to center the $y_{i}$ variables around $d$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Larger step sizes", "weight": 1.0} -->

In our experiments we have observed that utilizing a step size of $1/L$, as in standard FG methods, always converged and often performed better than the step size of ${1/16}L$ suggested by our analysis. Thus, in our experiments we used $\alpha_{k} = {1/L}$ even though we do not have a formal analysis of the method under this step size. We also found that a step size of $2/{({L + {n\mu}})}$, which in the strongly-convex case corresponds to the best fixed step size for the FG method in the special case of $n = 1$ \see Nesterov, [2004, Theorem 2.1.15\], sometimes yields even better performance (though in other cases it performs poorly).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Line-search when $L$ is not known", "weight": 1.0} -->

In general the Lipschitz constant $L$ will not be known, but we may obtain a reasonable approximation of a valid $L$ by evaluating $f_{i}$ values while running the algorithm. In our experiments, we used a basic line-search where we start with an initial estimate $L^{0}$, and double this estimate whenever we do not satisfy the inequality

<!-- chunk {"id": "body-0047", "role": "body", "section": "Line-search when $L$ is not known", "weight": 1.0} -->

which must be true if $L^{k}$ is valid. An important property of this test is that it depends on $f_{i_{k}}$ but not on $g$, and thus the cost of performing this test is independent of $n$. To avoid instability caused by comparing very small numbers, we only do this test when ${\|{f_{i_{k}}^{\prime}{(x^{k})}}\|}^{2} > 10^{- 8}$. Since $L$ is a global quantity but the algorithm will eventually remain within a neighbourhood of the optimal solution, it is possible that a smaller estimate of $L$ (and thus a larger step size) can be used as we approach $x^{\ast}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Line-search when $L$ is not known", "weight": 1.0} -->

To potentially take advantage of this, we initialize with the slightly smaller $L^{k} = {({L^{k - 1}2^{- {1/n}}})}$ at each iteration, so that the estimate of $L$ is halved if we do $n$ iterations (an effective pass through the data) and never violate the inequality. Note that in the case of $\ell_{2}$-regularized objectives, we can perform the line-search to find an estimate of the Lipschitz constant of $l_{i}^{\prime}$ rather than $f_{i}^{\prime}$, and then simply add $\lambda$ to this value to take into account the effect of the regularizer.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Line-search when $L$ is not known", "weight": 1.0} -->

Note that the cost of this line-search is *independent* of $n$, making it suitable for large problems. Further, for linearly-parameterized models of the form $f_{i}{({a_{i}^{T}x})}$, it is also possible to implement the line-search so that its cost is also independent of the number of variables $p$. To see why, if we use $\delta^{k} = {a_{i_{k}}^{T}x^{k}}$ and the structure in the gradient then the left side is given by

<!-- chunk {"id": "body-0050", "role": "body", "section": "Line-search when $L$ is not known", "weight": 1.0} -->

Thus, if we pre-compute the squared norms ${\| a_{i}\|}^{2}$ and note that $\delta^{k}$ and $f_{i_{k}}^{\prime}{(\delta^{k})}$ are already needed by the SAG update, then each iteration only involves operations on scalar values and the single-variable function $f_{i_{k}}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Mini-batches for vectorized computation and reduced storage", "weight": 1.0} -->

Because of the use of vectorization and parallelism in modern architectures, practical SG implementations often group functions into 'mini-batches' and perform SG iterations on the mini-batches. We can also use mini-batches within the SAG iterations to take advantage of the same vectorization and parallelism. Additionally, for problems with dense gradients mini-batches can dramatically decrease the storage requirements of the algorithm, since we only need to store a vector $y_{i}$ for each mini-batch rather than for each example. Thus, for example, using a mini-batch of size $100$ leads to a $100$-fold reduction in the storage cost.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Mini-batches for vectorized computation and reduced storage", "weight": 1.0} -->

A subtle issue that arises when using mini-batches is that the value of $L$ in the Lipschitz condition is based on the mini-batches instead of the original functions $f_{i}$. For example, consider the case where we have a batch $\mathcal{B}$ and the minimum value of $L$ in for each $i$ is given by $L_{i}$. In this case, a valid value of $L$ for the function $x\mapsto{\frac{1}{|\mathcal{B}|}{\sum_{i \in \mathcal{B}}{f_{i}{(x)}}}}$ would be $\max_{i \in \mathcal{B}}{\{ L_{i}\}}$. We refer to this as $L_{\text{max}}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Mini-batches for vectorized computation and reduced storage", "weight": 1.0} -->

Note that $L_{\text{Hessian}} \leq L_{\text{mean}} \leq L_{\text{max}}$, although $L_{\text{Hessian}}$ will typically be more difficult to compute than $L_{\text{mean}}$ or $L_{\text{max}}$ (although a line-search as discussed in the previous section can reduce this cost). Due to the potential of using a smaller $L$, *we may obtain a faster convergence rate by using larger mini-batches*. However, in terms of passes through the data this faster convergence may be offset by the higher iteration cost associated with using mini-batches.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Non-uniform example selection", "weight": 1.0} -->

In standard SG methods, it is crucial to sample the functions $f_{i}$ uniformly, at least asymptotically, in order to yield an unbiased gradient estimate and subsequently achieve convergence to the optimal value (alternately, the bias induced by non-uniform sampling would need to be asymptotically corrected). In SAG iterations, however, the weight of each gradient is constant and equal to $1/n$, regardless of the frequency at which the corresponding function is sampled. We might thus consider sampling the functions $f_{i}$ non-uniformly, without needing to correct for this bias. Though we do not yet have any theoretical proof as to why a non-uniform sampling might be beneficial, intuitively we would expect that we do not need to sample functions $f_{i}$ whose gradient changes slowly as often as functions $f_{i}$ whose gradient changes more quickly.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Non-uniform example selection", "weight": 1.0} -->

Indeed, we provide here an argument to justify a non-uniform sampling strategy based on the Lipschitz constants of the individual gradients $f_{i}^{\prime}$ and we note that in subsequent works this intuition has proved correct for related algorithms \Xiao and Zhang, [2014, Schmidt et al., 2015\].

<!-- chunk {"id": "body-0056", "role": "body", "section": "Non-uniform example selection", "weight": 1.0} -->

Let $L_{i}$ again be the Lipschitz constant of $f_{i}^{\prime}$, and assume that the functions are placed in increasing order of Lipschitz constants, so that $L_{1} \leqslant L_{2} \leqslant \ldots \leqslant L_{n}$. In the ill-conditioned setting where the convergence rate depends on $\frac{\mu}{L}$, a simple way to improve the rate by decreasing $L$ is to replace $f_{n}$ by two functions $f_{n1}$ and $f_{n2}$ such that

<!-- chunk {"id": "body-0057", "role": "body", "section": "Non-uniform example selection", "weight": 1.0} -->

Hence, if $L_{n - 1} < \frac{nL_{n}}{n + 1}$, this problem has the same $\mu$ but a smaller $L$ than the original one, improving the bound on the convergence rate. By duplicating $f_{n}$, we increase its probability of being sampled from $\frac{1}{n}$ to $\frac{2}{n + 1}$, but we also replace $y_{n}^{k}$ by a noisier version, i.e. $y_{n1}^{k} + y_{n2}^{k}$. Using a noisier version of the gradient appears detrimental, so we assume that the improvement comes from increasing the frequency at which $f_{n}$ is sampled, and that logically we might obtain a better rate by simply sampling $f_{n}$ more often in the original problem and not explicitly duplicating the data.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Non-uniform example selection", "weight": 1.0} -->

We now consider the extreme case of duplicating each function $f_{i}$ a number of times equal to the Lipschitz constant of their gradient, assuming that these constants are integers. The new problem becomes

<!-- chunk {"id": "body-0059", "role": "body", "section": "Non-uniform example selection", "weight": 1.0} -->

The function $g$ is now written as the sum of $\sum_{k}L_{k}$ functions, each with a gradient with Lipschitz constant $\frac{\sum_{k}L_{k}}{n}$. The new problem has the same $\mu$ as before, but now has an $L$ equal to the average of the Lipschitz constants across the $f_{i}^{\prime}$, rather than their maximum, thus improving the bound on the convergence rate. Sampling these functions uniformly is now equivalent to sampling the original $f_{i}$'s according to their Lipschitz constant. Thus, we might expect to obtain better performance, instead of creating a larger problem by duplicating the functions in proportion to their Lipschitz constant, simply sampling the functions from the original problem in proportion to their Lipschitz constants.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Non-uniform example selection", "weight": 1.0} -->

Sampling in proportion to the Lipschitz constants of the gradients was explored by Nesterov in the context of coordinate descent methods, and is also somewhat related to the sampling scheme used by Strohmer and Vershynin in the context of their randomized Kaczmarz algorithm. Since the first version of this work was released, Needell et al. have analyzed sampling according to the Lipschitz constant in the context of SG iterations. Such a sampling scheme makes the iteration cost depend on $n$, due to the need to generate samples from a general discrete distribution over $n$ variables. However, after an initial preprocessing cost of $O{(n)}$ we can sample from such distributions in $O{({\log n})}$ using a simple binary search \see Robert and Casella, [2004, Example 2.10\].

<!-- chunk {"id": "body-0061", "role": "body", "section": "Non-uniform example selection", "weight": 1.0} -->

Unfortunately, sampling the functions according to the Lipschitz constants and using a step size of $\alpha_{k} = \frac{n}{\sum_{i}L_{i}}$ does not seem to converge in general. However, by changing the number of times we duplicate each $f_{i}$, we can interpolate between the Lipschitz sampling and the uniform sampling. In particular, if each function $f_{i}$ is duplicated $L_{i} + c$ times, where $L_{i}$ is the Lipschitz constant of $f_{i}^{\prime}$ and $c$ a positive number, then the new problem becomes

<!-- chunk {"id": "body-0062", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In this section we perform empirical evaluations of the SAG iterations. We first compare the convergence of an implementation of the SAG iterations to a variety of competing methods available. We then seek to evaluate the effect of different algorithmic choices such as the step size, mini-batches, and non-uniform sampling.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

If we can only afford one pass through the data, then an SG method should be used.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

If we can afford to do many passes through the data (say, several hundred), then an FG method should be used.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

We expect that the SAG iterations will be most useful between these two extremes, where we can afford to do more than one pass through the data but cannot afford to do enough passes to warrant using FG algorithms like the AFG or L-BFGS methods. To test whether this is indeed the case in practice, we perform a variety of experiments evaluating the performance of the SAG algorithm in this scenario.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

Although the SAG algorithm can be applied more generally, in our experiments we focus on the important and widely-used $\ell_{2}$-regularized logistic regression problem

<!-- chunk {"id": "body-0067", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

as a canonical problem satisfying our assumptions. In our experiments we set the regularization parameter $\lambda$ to $1/n$, which is in the range of the smallest values that would typically be used in practice, and thus which results in the most ill-conditioned problems of this form that would be encountered.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

Our experiments focus on the freely-available benchmark binary classification data sets listed in Table 2. The *quantum* and *protein* data set was obtained from the KDD Cup 2004 website;^11^1 the *covertype* (based on the datset of Blackard, Jock, and Dean), *rcv1*, *news*, and *rcv1Full* data sets were obtained from the LIBSVM Data website; ^22^2 the *sido* data set was obtained from the Causality Workbench website,^33^3 the *spam* data set was prepared by \see Carbonetto, [2009, §2.6.5\] using the TREC 2005 corpus^44^4 and the *alpha* data set was obtained from the Pascal Large Scale Learning Challenge website^55^5 We added a (regularized) bias term to all data sets, and for dense features we standardized so that they would have a mean of zero and a variance of one.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

To obtain results that are independent of the practical implementation of the algorithm, we measure the objective as a function of the number of effective passes through the data, measured as the number of times we evaluate $l_{i}^{\prime}$ divided by the number of examples $n$. If they are implemented to take advantage of the sparsity present in the data sets, the runtimes of all algorithms examined in this section differ by at most a constant times this measure.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

AFG: A variant of the accelerated full gradient method of Nesterov, where iterations of with a step size of $1/L^{k}$ are interleaved with an extrapolation step. We used an adaptive line-search to estimate a local $L$ based on the variant proposed for $\ell_{2}$-regularized logistic regression by Liu et al..

<!-- chunk {"id": "body-0071", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

L-BFGS: A publicly-available limited-memory quasi-Newton method that has been tuned for log-linear models such as logistic regression \Schmidt,. This method is the most complicated method we considered.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

SG: The stochastic gradient method described by iteration. Since setting the step-size in this method is a tenuous issue, we chose the constant step size that gave the best performance (in hindsight) among all powers of $10$ (we found that this constant step-size strategies gave better performance than the variety of decreasing step-size strategies that we experimented with).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

ASG: The average of the iterations generated by the SG method above, where again we choose the best step size among all powers of $10$.^66^6Note that we also compared to a variety of other SG methods including the popular Pegasos SG method of Shalev-Shwartz et al., SG with momentum, SG with gradient averaging, the regularized dual averaging method of Xiao (a stochastic variant of the primal-dual subgradient method of Nesterov for regularized objectives), the accelerated SG method of Delyon and Juditsky, SG methods that only average the later iterations as in the 'optimal' SG method for non-smooth optimization of Rakhlin et al., the epoch SG method of Hazan and Kale, the 'nearly-optimal' SG method of Ghadimi and Lan, a diagonally-scaled SG method using the inverse of the coordinate-wise Lipshitz constants as the diagonal terms, and the adaptive diagonally-scaled AdaGrad method of Duchi et al..

<!-- chunk {"id": "body-0074", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

However, we omit results obtained using these algorithms since they never performed substantially better than the minimum between the *SG* and *ASG* methods when their step-size was chosen in hindsight.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

IAG: The incremental aggregated gradient method of Blatt et al. described by iteration with a cyclic choice of $i_{k}$. We used the re-weighting described in Section 4.2, we used the exact regularization as described in Section 4.3, and we chose the step-size that gave the best performance among all powers of $10$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

SAG-LS: The proposed stochastic average gradient method described by iteration. We used the re-weighting described in Section 4.2, the exact regularization as described in Section 4.3, and we used a step size of $\alpha_{k} = {1/L^{k}}$ where $L^{k}$ is an approximation of the Lipschitz constant for the negative log-likelihoods ${l_{i}{(x)}} = {\log{({1 + {\exp{({- {b_{i}a_{i}^{\top}x}})}}})}}$. Although this Lipschitz constant is given by $0.25{\max_{i}{\{{\| a_{i}\|}^{2}\}}}$, we used the line-search described in Section 4.6 to estimate it, to test the ability to use SAG as a black-box algorithm (in addition to avoiding this calculation and potentially obtaining a faster convergence rate by obtaining an estimate that could be smaller than the global value).

<!-- chunk {"id": "body-0077", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

We plot the results of the different methods for the first $50$ effective passes through the data in Figure 1. For the stochastic methods, we plot the mean performance as well as the minimum and maximum function values across $10$ choices for the initial random seed.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

FG vs. SG: Although the performance of SG methods is known to be catastrophic if the step size is not chosen carefully, after giving the SG methods (*SG* and *ASG*) an unfair advantage (by allowing them to choose the best step-size in hindsight), the SG methods always do substantially better than the FG methods (*AFG* and *L-BFGS*) on the first few passes through the data. However, the SG methods typically make little progress after the first few passes. In contrast, the FG methods make steady progress and eventually the faster FG method (*L-BFGS*) typically passes the SG methods.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

(FG and SG) vs. SAG: The SAG iterations seem to achieve the best of both worlds. They start out substantially better than FG methods, often obtaining similar performance to an SG method with the best step-size chosen in hindsight. But the SAG iterations continue to make steady progress even after the first few passes through the data. This leads to better performance than SG methods on later iterations, and on most data sets the sophisticated FG methods do not catch up to the SAG method even after $50$ passes through the data.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Comparison to FG and SG Methods", "weight": 1.0} -->

IAG vs. SAG: Even though these two algorithms differ in only the seemingly-minor detail of selecting data points at random (SAG) compared to cycling through the data (IAG), the performance improvement of SAG over its deterministic counterpart IAG is striking (even though the IAG method was allowed to choose the best step-size in hindsight). We believe this is due to the larger step sizes allowed by the SAG iterations, which would cause the IAG iterations to diverge.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Comparison to Coordinate Optimization Methods", "weight": 1.0} -->

For the $\ell_{2}$-regularized logistic regression problem, an alternative means to take advantage of the structure of the problem and achieve a linear convergence rate with a cheaper iteration cost than FG methods is to use randomized coordinate optimization methods. In particular, we can achieve a linear convergence rate by applying coordinate descent to the primal \Nesterov, or coordinate-ascent to the dual \Shalev-Schwartz and Zhang, [2013b\].

<!-- chunk {"id": "body-0082", "role": "body", "section": "Comparison to Coordinate Optimization Methods", "weight": 1.0} -->

PCD: The randomized primal coordinate-descent method of Nesterov, using a step-size of $1/L_{j}$, where $L_{j}$ is the Lipschitz-constant with respect to coordinate $j$ of $g^{\prime}$. Here, we sampled the coordinates uniformly.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Comparison to Coordinate Optimization Methods", "weight": 1.0} -->

PCD-L: The same as above, but sampling coordinates according to their Lipschitz constant, which can lead to an improved convergence rate \Nesterov,.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Comparison to Coordinate Optimization Methods", "weight": 1.0} -->

DCA: Applying randomized coordinate ascent to the dual, with uniform example selection and an exact line-search \Shalev-Schwartz and Zhang, [2013b\].

<!-- chunk {"id": "body-0085", "role": "body", "section": "Comparison to Coordinate Optimization Methods", "weight": 1.0} -->

As with comparing FG and SG methods, it is difficult to compare coordinate-wise methods to FG and SG methods in an implementation-independent way. To do this in a way that we believe is fair (when discussing convergence rates), we measure the number of effective passes of the *DCA* method as the number of iterations of the method divided by $n$ (since each iteration accesses a single example as in SG and SAG iterations). We measure the number of effective passes for the *PCD* and *PCD-L* methods as the number of iterations multiplied by $n/p$ so that $1$ effective pass for this method has a cost of $O{({np})}$ as in FG and SG methods. We ignore the additional cost associated with the Lipschitz sampling for the *PCD-L* method (as well as the expense incurred because the *PCD-L* method tended to favour updating the bias variable for sparse data sets) and we also ignore the cost of numerically computing the optimal step-size for the *DCA* method.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Comparison to Coordinate Optimization Methods", "weight": 1.0} -->

We compare the performance of the randomized coordinate optimization methods to several of the best methods from the previous experiment in Figure 2.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Comparison to Coordinate Optimization Methods", "weight": 1.0} -->

PCD vs. PCD-L: For the problems with $n > p$ (top and bottom rows of Figure 2), there is little difference between uniform and Lipschitz sampling of the coordinates. For the problems with $p > n$ (middle row of Figure 2), sampling according to the Lipschitz constant leads to a large performance improvement over uniform sampling.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Comparison to Coordinate Optimization Methods", "weight": 1.0} -->

PCD vs. DCA: For the problems with $p > n$, *DCA* and *PCD-L* have similar performance. For the problems with $n > p$, the performance of the methods typically differed but neither strategy tended to dominate the other.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Comparison to Coordinate Optimization Methods", "weight": 1.0} -->

(PCD and DCA) vs. (SAG): For some problems, the *PCD* and *DCA* methods have performance that is similar to *SAG-LS* and the *DCA* method even gives better performance than *SAG-LS* on one data set. However, for many data sets either the *PCD-L* or the *DCA* method (or both) perform poorly while the *SAG-LS* iterations are among the best or substantially better than all other methods on every data set. This suggests that, while coordinate optimization methods are clearly extremely effective for some problems, the SAG method tends to be a more robust choice across problems.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Comparison of Step-Size Strategies", "weight": 1.0} -->

In our prior work we analyzed the step-sizes $\alpha_{k} = {{1/2}nL}$ and $\alpha_{k} = {{1/2}n\mu}$ \Le Roux et al. while Section 3 considers the choice $\alpha_{k} = {{1/16}L}$ and Section 4.5 discusses the choices $\alpha_{k} = {1/L}$ and $\alpha_{k} = {2/{({L + {n\mu}})}}$ as in FG methods. In Figure 3 we compare the performance of these various strategies to the performance of the SAG algorithm with our proposed line-search as well as the IAG and SAG algorithms when the best step-size is chosen in hindsight.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Comparison of Step-Size Strategies", "weight": 1.0} -->

Proposition 1 of Le Roux et al.: Using a step-size of $\alpha_{k} = {{1/2}nL}$ performs poorly, and makes little progress compared to the other methods. This makes sense because Proposition 1 in Le Roux et al. implies that the convergence rate (in terms of effective passes through the data) under this step size will be similar to the basic gradient method, which is known to perform poorly unless the problem is very well-conditioned.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Comparison of Step-Size Strategies", "weight": 1.0} -->

Proposition 2 of Le Roux et al.: Using a step-size of $\alpha_{k} = {{1/2}n\mu}$ performs extremely well on the data sets with $p > n$ (middle row). In contrast, for the data sets with $n > p$ it often performs very poorly, and in some cases appears to diverge. This is consistent with Proposition 2 in Le Roux et al., which shows a fast convergence rate under this step size only if certain conditions on $\{ n,\mu,L\}$ hold.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Comparison of Step-Size Strategies", "weight": 1.0} -->

Theorem 1: Using a step-size of $\alpha_{k} = {{1/16}L}$ performs consistently better than the smaller step size $\alpha_{k} = {{1/2}nL}$, but in some cases it performs worse than $\alpha_{k} = {{1/2}n\mu}$. However, in contrast to $\alpha_{k} = {{1/2}n\mu}$, the step size $\alpha_{k} = {{1/16}L}$ always has reasonable performance.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Comparison of Step-Size Strategies", "weight": 1.0} -->

Section 4.5: The step size of $\alpha_{k} = {1/L}$ performs performs extremely well on the data sets with $p > n$, and performs better than the step sizes discussed above on all but one of the remaining data sets. The step size of $\alpha_{k} = {2/{({L + {n\mu}})}}$ seems to perform the same or slightly better than using $\alpha_{k} = {1/L}$ except on one data set where it performs poorly.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Comparison of Step-Size Strategies", "weight": 1.0} -->

Line-Search: Using the line-search from Section 4.6 tends to perform as well or better than the various constant step size strategies, and tends to have similar performance to choosing the best step size in hindsight.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Comparison of Step-Size Strategies", "weight": 1.0} -->

IAG vs. SAG: When choosing the best step size in hindsight, the SAG iterations tend to choose a much larger step size than the IAG iterations. The step sizes chosen for SAG were $100$ to $10000$ times larger than the step sizes chosen by IAG, and always lead to better performance by several orders of magnitude.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Effect of mini-batches", "weight": 1.0} -->

As we discuss in Section 4.7, when using mini-batches within the SAG iterations there is a trade-off between the higher iteration cost of using mini-batches and the faster convergence rate obtained using mini-batches due to the possibility of using a smaller value of $L$. In Figure 4, we compare (on the dense data sets) the excess sub-optimality as a function of the number of examples seen for various mini-batch sizes and the three step-size strategies $1/L_{\text{max}}$, $1/L_{\text{mean}}$, and $1/L_{\text{Hessian}}$ discussed in Section 4.7.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Effect of mini-batches", "weight": 1.0} -->

Even though Theorem 1 hints at a maximum mini-batch size of $\frac{n\mu}{2L}$ without loss of convergence speed, this is a very conservative estimate. In our experiments, the original value of $\frac{n\mu}{L}$ was on the order of $10^{- 5}$ and mini-batch sizes of up to 500 could be used without a loss in performance. Not only does this yield large memory storage gains, it would increase the computational efficiency of the algorithm when taking into account vectorization.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Effect of non-uniform sampling", "weight": 1.0} -->

In our final experiment, we explored the effect of using the non-uniform sampling strategy discussed in Section 4.8.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Effect of non-uniform sampling", "weight": 1.0} -->

SAG (Lipschitz): In this method we sample the functions in proporition to $L_{i} + c$, where $L_{i}$ is the global Lipschitz constant of the corresponding $f_{i}^{\prime}$ and we set $c$ to the average of these constants, $c = L_{\text{mean}} = {{({1/n})}{\sum_{i}L_{i}}}$. Plugging in these values into the formula at the end of Section 4.8 and using $L_{\text{max}}$ to denote the maximum $L_{i}$ value, we set the step-size to $\alpha_{k} = {{{1/2}L_{\text{max}}} + {{1/2}L_{\text{mean}}}}$.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Effect of non-uniform sampling", "weight": 1.0} -->

SAG-LS (Lipschitz): In this method we formed estimates of the quantities $L_{i}$, $L_{\text{max}}$, and $L_{\text{mean}}$. The estimator $L_{\text{max}}^{k}$ is computed in the same way as the SAG-LS method. To estimate each $L_{i}$, we keep track of an estimate $L_{i}^{k}$ for each $i$ and we set $L_{\text{mean}}^{k}$ to the average of the $L_{i}^{k}$ values among the $f_{i}$ that we have sampled at least once.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Effect of non-uniform sampling", "weight": 1.0} -->

We set $L_{i}^{k} = L_{i}^{k - 1}$ if example $i$ was not selected and otherwise we initialize to $L_{i}^{k} = {L_{i}^{k - 1}/2}$ and perform the line-search until we have a valid $L_{i}^{k}$ (this means that $L_{\text{mean}}^{k}$ will be approximately halved if we perform a full pass through the data set and never violate the inequality). To ensure that we do not ignore important unseen data points for too long, in this method we sample a previously unseen function with probability ${({n - m})}/n$, and otherwise we sample from the previously seen $f_{i}$ in proportion to $L_{i}^{k} + L_{\text{mean}}^{k}$.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Effect of non-uniform sampling", "weight": 1.0} -->

To prevent relying too much on our initially-poor estimate of $L_{\text{mean}}$, we use a step size of $\alpha_{k} = {{\frac{n - m}{n}\alpha_{\text{max}}} + {\frac{m}{n}\alpha_{\text{mean}}}}$, where $\alpha_{\text{max}} = {1/L_{\text{max}}^{k}}$ is the step-size we normally use with uniform sampling and $\alpha_{\text{mean}} = {{{1/2}L_{\text{max}}^{k}} + {{1/2}L_{\text{mean}}^{k}}}$ is the step-size we use with the non-uniform sampling method, so that the method interpolates between these extremes until the entire data set has been sampled.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Effect of non-uniform sampling", "weight": 1.0} -->

SAG (1/L) vs. SAG (Lipschitz): With access to global quantities and a constant step size, the difference between uniform and non-uniform sampling was typically quite small. However, in some cases the non-uniform sampling method behaved much better (top row of Figure 5).

<!-- chunk {"id": "body-0105", "role": "body", "section": "Effect of non-uniform sampling", "weight": 1.0} -->

SAG-LS vs. SAG-LS (Lipschitz): When estimating the Lipschitz constants of the individual functions, the non-uniform sampling strategy often gave better performance. Indeed, the adaptive non-uniform sampling strategy gave solutions that are orders of magnitude more accurate than any method we examined for several of the data sets (e.g., the *protein*, *covertype*, and *sido* data sets) In the context of logistic regression, it makes sense that an adaptive sampling scheme could lead to better performance, as many correctly-classified data samples might have a very slowly-changing gradient near the solution, and thus they do not need to be sampled often.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Discussion", "weight": 1.5} -->

Since the first version of this work was published \Le Roux et al. there has been an explosion of interest in stochastic methods with improved convergence rates. In this section we first review other algorithms that have been discovered to have this property, and then we discuss the many possible variants on these basic algorithms that have been explored. As this is a very quickly-evolving area there are likely to be many new developments in the near future, but we note that this literature review is up to date as of January, 2015.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Alternative Algorithms", "weight": 1.0} -->

SDCA: The first algorithm that was shown to have a similar convergence rate and iteration cost to SAG was in fact a much older algorithm: coordinate optimization applied to a dual problem with randomized coordinate selection, referred to as stochastic dual coordinate ascent (SDCA). Shalev-Schwartz and Zhang \[2013b\] consider the problem of minimizing an $\ell_{2}$-regularized finite sum,

<!-- chunk {"id": "body-0108", "role": "body", "section": "Alternative Algorithms", "weight": 1.0} -->

where each $f_{i}$ is convex and each $f_{i}^{\prime}$ is Lipschitz-continuous, by optimizing its Fenchel dual,

<!-- chunk {"id": "body-0109", "role": "body", "section": "Alternative Algorithms", "weight": 1.0} -->

They consider applying exact coordinate optimization to a randomly selected coordinate. Using the primal-dual relationship $x = {\frac{1}{n\lambda}{\sum_{i = 1}^{N}{x_{i}a_{i}}}}$, they show a linear convergence rate in terms of the duality gap. Since there is one dual variable associated with each example $i$, the iteration cost is independent of $n$ and thus the strategy has similar convergence properties to SAG (the memory requirements are identical in this context, see Section 4.1).

<!-- chunk {"id": "body-0110", "role": "body", "section": "Alternative Algorithms", "weight": 1.0} -->

This result is related to the earlier result of \Nesterov who shows a similar convergence rate for randomized coordinate descent.^77^7Local linear convergence rates of deterministic coordinate descent methods had been established much earlier \Luo and Tseng,. However, the result of Nesterov cannot be directly applied to the dual problem in general since the dual does not necessarily have a Lipschitz-continuous gradient. A similar result was also reported even earlier by Collins et al. without requiring that the gradient of the dual is Lipschitz-continuous, but this result again only applied to the dual objective. More recently, Shalev-Schwartz and Zhang \[2013a\] show linear convergence of SDCA in the more general setting

<!-- chunk {"id": "body-0111", "role": "body", "section": "Alternative Algorithms", "weight": 1.0} -->

where $A_{i}$ are matrices and $r$ is $1 -$strongly convex. They also relax the requirement of exact coordinate optimization, providing a variety of more practical alternatives. Further, in subsequent work they obtain a convergence rate in the convex case by adding an explicit strongly-convex regularizer to the problem \Shalev-Schwartz and Zhang,.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Alternative Algorithms", "weight": 1.0} -->

A disadvantage of SDCA compared to the SAG algorithm is that the SDCA convergence rates depend on $\lambda$ rather than the strong-convexity constant $\mu$. In the worst case we have $\mu = \lambda$, but if $\mu$ is much larger then the convergence rate of SAG is much faster. Further, even in cases where $\mu = \lambda$, the convergence rate of SAG might be much faster if the iterates stay in local region with a higher strong-convexity constant. As an extreme example, due to local strong-convexity SAG might have a linear convergence rate in scenarios where SDCA has a sub-linear convergence. This subtle but practically important issue was a key focus in the recent work of \Agarwal and Bottou and indeed the performance of SDCA was very poor on three of the test problems in our experiments. See Figure 2 (top left, top right, bottom right).

<!-- chunk {"id": "body-0113", "role": "body", "section": "Alternative Algorithms", "weight": 1.0} -->

MISO: Mairal analyzes a very general surrogate optimization framework, that includes a wide vareity of existing algorithms. He also considers incremental algorithms in this framework, and specialized to the smooth and unconstraeind setting (with a 'Lipschitz surrogate') obtains an algorithm (MISO) that is very similar to the SAG algorithm,

<!-- chunk {"id": "body-0114", "role": "body", "section": "Alternative Algorithms", "weight": 1.0} -->

where $y_{i}^{k}$ is defined as in the SAG algorithm 6, and $x_{i}^{k}$ is the parameter vector used to compute the corresponding $y_{i}^{k}$. Thus, instead of applying the SAG step to $x^{k}$, MISO applies the step to the average of the previous $x_{i}^{k}$ values used to form the current $y_{i}^{k}$ variables. Mairal shows that this algorithm also achieves an $O{({1/k})}$ rate for convex objectives and a linear convergence rate for strongly-convex objectives.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Alternative Algorithms", "weight": 1.0} -->

However, MISO has the disadvantage that it not only requires storing the $n$ gradient values but also storing $n$ previous iterations (which are less likely to have a nice structure). Further, the linear convergence rate shown for MISO is substantially slower than the convergence rate shown in Theorem 1. In particular, the rate is more similar to the substantially slower Proposition 1 in our prior work \Le Roux et al.,. Subsequent work on the MISO algorithm has shown an analogous result to Proposition 2 in our prior work; if the $n$ is sufficiently larger than $L\mu$, then using a step-size proportional to $1/\mu$ yields a faster convergence rate \Mairal, [2014, Defazio et al., 2014b\]. However, using this step-size causes divergence if $\mu$ is not sufficiently large.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Alternative Algorithms", "weight": 1.0} -->

SVRG: Another interesting framework that has been considered is known as 'mixed optimization', 'stochastic variance-reduced gradient' (SVRG), or 'semi-stochastic gradient descent' (S2GD) \Mahdavi and Jin, [2013, Johnson and Zhang, 2013, Zhang et al., 2013, Konečnỳ and Richtárik, 2013\].^88^8Wang et al. consider a related algorithm that maintains an easily-computable approximation to the current gradient $g^{\prime}{(x^{k})}$. Although this can improve the constants in the sublinear SG convergence rates, it does not improve the rates. Unlike FG methods that utilize the full gradient $g^{\prime}$ and SG methods that consider individual gradients $f_{i}^{\prime}$, these mixed optimization methods combine the two. In particular, they use a (possibly regularized) iteration of the form

<!-- chunk {"id": "body-0117", "role": "body", "section": "Alternative Algorithms", "weight": 1.0} -->

where ${\overset{\sim}{x}}^{k}$ is the last iterate where the full gradient $g^{\prime}$ was evaluated. The algorithm alternates between computing the full gradient at ${\overset{\sim}{x}}^{k}$, and performing some number $m$ of stochastic gradient iterations. Note this is very similar to the SAG algorithm written in the form

<!-- chunk {"id": "body-0118", "role": "body", "section": "Alternative Algorithms", "weight": 1.0} -->

where $x_{i}^{k}$ is defined as in the MISO algorithm. These methods are thus similar to SAG in the use of potentially-outdated gradient information, but differ in that the outdated gradients are all computed at the same previous iteration ${\overset{\sim}{x}}^{k}$ and the weighting of terms is changed. If the step-size and parameter $m$ are set appropriately, this algorithm has a linear convergence rate in the strongly-convex case. It can also achieve an $O{({1/k})}$ convergence rate in the general convex case, by applying it to a purturbed problem where a strongly-convex regularizer has been added.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Alternative Algorithms", "weight": 1.0} -->

A key advantage of this strategy is it only requires storing ${\overset{\sim}{x}}^{k}$, rather than the $n$ gradient values. However, to obtain this improved memory requirement we must evaluate $f_{i}^{\prime}$ twice on each iteration. Further, the algorithm innefficiently requires full passes through the data to evaluate $f_{j}^{\prime}{({\overset{\sim}{x}}^{k})}$ for all $j$.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Alternative Algorithms", "weight": 1.0} -->

A disadvantage of the SVRG method is that it requires setting two parameters (rather than one) and the convergence rate depends in a non-trivial way on their interaction both with each other and with both the Lipschitz constant and the strong-convexity. As with SDCA, the dependence on the strong-convexity constant is notable. In particular, the algorithm can't be applied without modification to general convex problems, and (although the effect is not as severe as it is with SDCA) the convergence rate may be substantially slower than SAG if there exists hidden strong convexity.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Alternative Algorithms", "weight": 1.0} -->

Self-Concordant Objectives: A surprising recent development is that Bach and Moulines have shown that the finite sum assumption is not required to obtain the $O{({1/k})}$ convergence rate in the special case of least squares. They show that an averaged SG method achieves this rate, and give a 2-phase Newton-like SG method that achieves this rate under an assumption similar to self-concordance. However, this assumption does not hold in general for the class of problems considered here.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Alternative Algorithms", "weight": 1.0} -->

SAGA: One of the most recent developments in this area is the SAGA algorithm Defazio et al. \[2014a\]. This algorithm intelligently combines the updates used in the SAG and SVRG algorithms. This method maintains the appealing properties of SAG, but yields a simpler proof. However, the proof technique used in that work does not yield a simpler analysis of the original SAG algorithm.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Alternative Algorithms", "weight": 1.0} -->

Lower Bounds: There has been recent work on determining a lower bound on the convergence rate that can be expected for minimizing finite sums. Defazio et al. \[2014b\] show that the rate must be at least $({1 - {1/n}})$ in the strongly-convex case, while Agarwal and Bottou establish a bound that also depends on the condition number $L/\mu$.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Generalizations and Other Issues", "weight": 1.0} -->

Accelerated gradient: AFG methods are variants of the basic FG method that can obtain an $O{({1/k^{2}})}$ convergence rate for the general convex case, and faster linear convergence rates that depend on the square root of the condition number $(\sqrt{L/\mu})$ rather than the condition number $({L/\mu})$ in the strongly-convex case \see Nesterov, [2004, §2.2.1\]. For strongly-convex objectives, it has been shown that a mini-batch strategy can obtain a better dependence on the condition number in certain regimes for SDCA \Shalev-Shwartz and Zhang, and more recently for SVRG \Nitanda,. It is possible that similar arguments could hold for SAG algorithms, which could be advantageous over these methods for reasons discussed in the previous section.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Generalizations and Other Issues", "weight": 1.0} -->

Shalev-Schwartz and Zhang have also given an accelerated version of the SDCA method for ill-conditioned problems, that uses SDCA to solve a sequence of regularized problems up to a prescribed optimality. Since this procedure ultimately relies on the sequence of primal solutions, we can also accelerate SAG using a procedure like this. However, a difficulty with this procedure (whether SAG or SDCA are used) is the cost of measuring the optimality of the sub-problems.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Generalizations and Other Issues", "weight": 1.0} -->

Rather than using this inner-outer procedure, Lin et al. show that using a deterministic primal iteration (based on the full data set) allows one to construct a primal solution that has the accelerated rate from the result of an accelerated dual coordinate ascent method. Zhang and Xiao give a coordinate-wise variant of the accelerated primal-dual method of Chambolle and Pock that also achieves this rate. Based on these results, it is possible that accelerated versions of SAG could be developed that do not rely on an inner-outer procedure.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Generalizations and Other Issues", "weight": 1.0} -->

The convergence rates of these accelerated methods have the same form as the lower bound established by Agarwal and Bottou. However, Agarwal and Bottou point out that these accelerated convergence rates depend on $\lambda$ rather than $\mu$. Thus, they conclude that the basic SAG algorithm may still be much faster on some problems than accelerated SDCA methods, and indeed show how to construct a problem where SAG is arbitrarily faster than accelerated SDCA. The possibility of developing an accelerated SAG algorithm that is adaptive to $\mu$ remains open.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Generalizations and Other Issues", "weight": 1.0} -->

Proximal gradient and ADMM: It is becoming increasingly common to address problems of the form

<!-- chunk {"id": "body-0129", "role": "body", "section": "Generalizations and Other Issues", "weight": 1.0} -->

where $f_{i}$ and $g$ satisfy our assumptions and $r$ is a general convex function that could be non-smooth or enforce that constraints are satisfied. Proximal-gradient methods for problems with this structure use iterations of the form

<!-- chunk {"id": "body-0130", "role": "body", "section": "Generalizations and Other Issues", "weight": 1.0} -->

where the prox${}_{\alpha k}^{}{\lbrack y\rbrack}$ operator is the solution to the proximity problem

<!-- chunk {"id": "body-0131", "role": "body", "section": "Generalizations and Other Issues", "weight": 1.0} -->

Proximal-gradient and accelerated proximal-gradient methods are appealing for solving non-smooth optimization problems because they achieve the same convergence rates as FG methods for smooth optimization problems \Nesterov, [2007, Schmidt et al., 2011\]. We have explored a variant of the proximal-gradient method where the average over the $f_{i}^{\prime}{(x^{k})}$ values is replaced by the SAG approximation. Although our analysis does not directly apply to this scenario, we believe that this proximal-SAG algorithm for composite non-smooth optimization achieves the same convergence rates as the SAG algorithm for smooth optimization; this is supported by the experiments of Xiao and Zhang. Indeed, there now exist proximal-gradient variants of SDCA \Shalev-Schwartz and Zhang, [2013a\], MISO \Mairal SVRG \Xiao and Zhang and SAGA \Defazio et al., [2014a\].

<!-- chunk {"id": "body-0132", "role": "body", "section": "Generalizations and Other Issues", "weight": 1.0} -->

In cases where $r$ is composed with a linear function, we can consider approaches based on the alternating direction method of multipliers (ADMM). This has been explored for SDCA \Suzuki, and MISO \Zhong and Kwok and a variant based on SAG is also likely to be possible.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Generalizations and Other Issues", "weight": 1.0} -->

Coordinate-wise: The key advantage of SG and SAG methods is that the iteration cost is independent of the number of functions $n$. However, in many applications we may also be concerned with the dependence of the iteration cost on the number of variables $p$. Randomized coordinate-wise methods offer linear convergence rates with an iteration cost that is linear in $n$ but independent of $p$ \Nesterov,. We can consider a variant of SAG whose iteration cost is independent of both $n$ and $p$ by using the update

<!-- chunk {"id": "body-0134", "role": "body", "section": "Generalizations and Other Issues", "weight": 1.0} -->

to each coordinate $j$ of each vector $y_{i}$ in the SAG algorithm, and where $j_{k}$ is a sample from the set $\{ 1,2,\ldots,p\}$. Konečnỳ et al. recently proposed an SVRG algorithm of this flavour.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Generalizations and Other Issues", "weight": 1.0} -->

Newton-like: In cases where $g$ is twice-differentiable, we can also consider Newton-like variants of the SAG algorithm,

<!-- chunk {"id": "body-0136", "role": "body", "section": "Generalizations and Other Issues", "weight": 1.0} -->

where $B^{k}$ is a positive-definite approximation to the inverse Hessian $g^{\operatorname{\prime\prime}}{(x^{k})}$. We would expect to obtain a faster convergence rate by using an appropriate choice of the sequence $\{ B^{k}\}$. However, in order to not increase the iteration cost these matrices should be designed to allow fast multiplication. For example, we could choose $B^{k}$ to be diagonal, which would also preserve any sparsity present in the updates. Sohl-Dickstein et al. propose a quasi-Newton method in this class that shows impressive empirical results, although the iteration cost is much higher.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Generalizations and Other Issues", "weight": 1.0} -->

Relaxing Convexity Assumptions: It is likely that the convexity assumptions made in this work could be relaxed. For example, Gong and Ye show SVRG can obtain a linear convergence under weaker assumptions. Since SAG is adaptive to hidden strong-convexity, the assumptions needed for its linear convergence are likely even weaker. Further, the SAG algorithm may also be useful even if $g$ is non-convex (which is different than SDCA). In this case we expect that, similar to the IAG method \Blatt et al. the algorithm converges to a stationary point under very general conditions.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Generalizations and Other Issues", "weight": 1.0} -->

Non-Uniform Sampling: We have given an argument that non-uniform sampling should benefit the SAG algorithm, and shown empirically that it can lead to a substantial improvement. However, we have not yet given a full analysis of this scheme. Subsequent works have shown that the type of dependency we conjecture here (e.g., dependence on the average Lispschitz constant) can be achieved with non-uniform sampling in the context of SDCA \Qu et al., [2014, Zhao and Zhang, 2014\], SVRG \Xiao and Zhang and SAGA \Schmidt et al.,

<!-- chunk {"id": "body-0139", "role": "body", "section": "Generalizations and Other Issues", "weight": 1.0} -->

Step-size selection and termination criteria: The three major disadvantages of SG methods are: (i) the slow convergence rate, (ii) deciding when to terminate the algorithms, and (iii) choosing the step size while running the algorithm. This work shows that the SAG iterations achieve a much faster convergence rate, but the SAG iterations may also be advantageous in terms of termination criteria and choosing step sizes. In particular, the SAG iterations suggest a natural termination criterion; since the quantity $d$ in Algorithm 1 converges to $f^{\prime}{(x^{k})}$ as $\|{x^{k} - x^{k - 1}}\|$ converges to zero, we can use $\| d\|$ as an approximation of the optimality of $x^{k}$ as the iterates converge. Regarding choosing the step-size, a disadvantage of a constant step-size strategy is that a step-size that is too large may cause divergence. But, we expect that it is possible to design line-search or trust-region strategies that avoid this issue.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Generalizations and Other Issues", "weight": 1.0} -->

Such strategies might even lead to faster convergence for functions that are locally well-behaved around their optimum, as indicated in our experiments. Further, while SG methods require specifying a sequence of step sizes and mis-specifying this sequence can have a disastrous effect on the convergence rate \see Nemirovski et al., [2009, §2.1\], our theory shows that the SAG iterations achieve a fast convergence rate for any sufficiently small constant step size, and our experiments indicate that a simple line-search gives strong performance.
