<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Stochastic Gradient Method with an Exponential Convergence Rate for Finite Training Sets

Topics include Stochastic average gradient, Variance reduction, Finite-sum optimization, Linear convergence, Convex optimization, Empirical risk minimization, Incremental gradient methods.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the stochastic average gradient method, which stores the most recent gradient for each finite-sum component and averages those stored gradients to obtain a low-cost update with linear convergence on strongly convex objectives. It is one of the first modern variance-reduction methods showing that finite training sets permit faster rates than black-box stochastic gradient assumptions allow.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a new stochastic gradient method for optimizing the sum of a finite set of smooth functions, where the sum is strongly convex. While standard stochastic gradient methods converge at sublinear rates for this problem, the proposed method incorporates a memory of previous gradient values in order to achieve a linear convergence rate. In a machine learning context, numerical experiments indicate that the new algorithm can dramatically outperform standard algorithms, both in terms of optimizing the training error and reducing the test error quickly.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A plethora of the problems arising in machine learning involve computing an approximate minimizer of the sum of a loss function over a large number of training examples, where there is a large amount of redundancy between examples. The most wildly successful class of algorithms for taking advantage of this type of problem structure are *stochastic gradient* (SG) methods Robbins and Monro; Bottou and LeCun. Although the theory behind SG methods allows them to be applied more generally, in the context of machine learning SG methods are typically used to solve the problem of optimizing a sample average over a finite training set, i.e., In this work, we focus on such *finite training data* problems where each $f_{i}$ is *smooth* and the average function $g$ is *strongly-convex*.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

As an example, in the case of $\ell_{2}$-regularized logistic regression we have $f_{i}{(x)}: = \frac{\lambda}{2} \parallel x \parallel^{2} + \log{(1 + \exp{(- b_{i}a_{i}^{T}x)})}$, where $a_{i} \in {\mathbb{R}}^{p}$ and $b_{i} \in {\{{- 1},1\}}$ are the training examples associated with a binary classification problem and $\lambda$ is a regularization parameter. More generally, any $\ell_{2}$-regularized empirical risk minimization problem of the form falls in the framework of provided that the loss functions $l_{i}$ are convex and smooth. An extensive list of convex loss functions used in machine learning is given by Teo et al., and we can even include non-smooth loss functions (or regularizers) by using smooth approximations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The standard *full gradient* (FG) method, which dates back to Cauchy, uses iterations of the form Using $x^{\ast}$ to denote the unique minimizer of $g$, the FG method with a constant step size achieves a *linear* convergence rate: for some $\rho < 1$ which depends on the condition number of $g$. Linear convergence is also known as *geometric* or *exponential* convergence, because the cost is cut by a fixed fraction on each iteration. Despite the fast convergence rate of the FG method, it can be unappealing when $n$ is large because its iteration cost scales linearly in $n$. SG methods, on the other hand, have an iteration cost which is *independent* of $n$, making them suited for that setting. The basic SG method for optimizing uses iterations of the form where $\alpha_{k}$ is a step-size and a training example $i_{k}$ is selected uniformly among the set $\{ 1,\ldots,n\}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The randomly chosen gradient $f_{i_{k}}'{(x^{k})}$ yields an unbiased estimate of the true gradient $g'{(x^{k})}$, and one can show under standard assumptions that, for a suitably chosen decreasing step-size sequence $\{\alpha_{k}\}$, the SG iterations achieve the sublinear convergence rate where the expectation is taken with respect to the selection of the $i_{k}$ variables. Under certain assumptions this convergence rate is *optimal* for strongly-convex optimization in a model of computation where the algorithm only accesses the function through unbiased measurements of its objective and gradient (see Nemirovski and Yudin; Nemirovski et al.; Agarwal et al.). Thus, we cannot hope to obtain a better convergence rate if the algorithm only relies on unbiased gradient measurements. Nevertheless, by using the stronger assumption that the functions are sampled from a finite dataset, in this paper we show that we can achieve an exponential converengence rate while preserving the iteration cost of SG methods.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The primay contribution of this work is the analysis of a new algorithm that we call the *stochastic average gradient* (SAG) method, a randomized variant of the incremental aggregated gradient (IAG) method Blatt et al., which combines the low iteration cost of SG methods with a linear convergence rate as in FG methods. The SAG method uses iterations of the form where at each iteration a random training example $i_{k}$ is selected and we set That is, like the FG method, the step incorporates a gradient with respect to each training example. But, like the SG method, each iteration only computes the gradient with respect to a single training example and the cost of the iterations is independent of $n$. Despite the low cost of the SAG iterations, in this paper we show that *the SAG iterations have a linear convergence rate*, like the FG method. That is, by having access to $i_{k}$ and by keeping a *memory* of the most recent gradient value computed for each training example $i$, this iteration achieves a faster convergence rate than is possible for standard SG methods.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Further, in terms of effective passes through the data, we also show that for certain problems the convergence rate of SAG is faster than is possible for standard FG methods.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In a machine learning context where $g{(x)}$ is a *training cost* associated with a predictor parameterized by $x$, we are often ultimately interested in the *testing cost*, the expected loss on unseen data points. Note that a linear convergence rate for the training cost does not translate into a similar rate for the testing cost, and an appealing propertly of SG methods is that they achieve the optimal $O{({1/k})}$ rate for the *testing cost* as long as every datapoint is seen *only once*. However, as is common in machine learning, we assume that we are only given a finite training data set and thus that datapoints are revisited multiple times. In this context, the analysis of SG methods only applies to the training cost and, although our analysis also focuses on the training cost, in our experiments the SAG method typically reached the optimal testing cost faster than both FG and SG methods.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The next section reviews closely-related algorithms from the literature, including previous attempts to combine the appealing aspects of FG and SG methods. However, despite $60$ years of extensive research on SG methods, most of the applications focusing on finite datasets, we are not aware of any other SG method that achieves a linear convergence rate while preserving the iteration cost of standard SG methods. Section 3 states the (standard) assumptions underlying our analysis and gives the main technical results; we first give a slow linear convergence rate that applies for any problem, and then give a very fast linear convergence rate that applies when $n$ is sufficiently large. Section 4 discusses practical implementation issues, including how to reduce the storage cost from $O{({np})}$ to $O{(n)}$ when each $f_{i}$ only depends on a linear combination of $x$. Section 5 presents a numerical comparison of an implementation based on SAG to SG and FG methods, indicating that the method may be very useful for problems where we can only afford to do a few passes through a data set.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

In our analysis we assume that each function $f_{i}$ in is differentiable and that each gradient $f_{i}'$ is Lipschitz-continuous with constant $L$, meaning that for all $x$ and $y$ in ${\mathbb{R}}^{p}$ we have This is a fairly weak assumption on the $f_{i}$ functions, and in cases where the $f_{i}$ are twice-differentiable it is equivalent to saying that the eigenvalues of the Hessians of each $f_{i}$ are bounded above by $L$. In addition, we also assume that the average function $g = {\frac{1}{n}{\sum_{i = 1}^{n}f_{i}}}$ is strongly-convex with constant $\mu > 0$, meaning that the function $x\mapsto{{g{(x)}} - {\frac{\mu}{2}{\| x\|}^{2}}}$ is convex.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

This is a stronger assumption and is not satisfied by all machine learning models. However, note that in machine learning we are typically free to choose the regularizer, and we can always add an $\ell_{2}$-regularization term as in Eq. to transform any convex problem into a strongly-convex problem (in this case we have $\mu \geq \lambda$). Note that strong-convexity implies that the problem is solvable, meaning that there exists some unique $x^{\ast}$ that achieves the optimal function value. Our convergence results assume that we initialize $y_{i}^{0}$ to a zero vector for all $i$, and our results depend on the variance of the gradient norms at the optimum $x^{\ast}$, denoted by $\sigma^{2} = {\frac{1}{n}{\sum_{i}{\|{f_{i}'{(x^{\ast})}}\|}^{2}}}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

Finally, all our convergence results consider expectations with respect to the internal randomization of the algorithm, and not with respect to the data (which are assumed to be deterministic and fixed).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

We first consider the convergence rate of the method when using a constant step size of $\alpha_{k} = \frac{1}{2nL}$, which is similar to the step size needed for convergence of the IAG method in practice.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

In this section we describe modifications that substantially reduce the SAG iteration's memory requirements, as well as modifications that lead to better practical performance.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Further, because of the simple form of the SAG updates, if $a_{i}$ is sparse we can use 'lazy updates' in order to reduce the iteration cost from $O{(p)}$ down to the sparsity level of $a_{i}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Mini-batches: To employ vectorization and parallelism, practical SG implementations often group training examples into 'mini-batches' and perform SG iterations on the mini-batches. We can also use mini-batches within the SAG iterations, and for problems with dense gradients this decreases the storage requirements of the algorithm since we only need a $y_{i}^{k}$ for each mini-batch. Thus, for example, using mini-batches of size $100$ leads to a 100-fold reduction in the storage cost.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Step-size re-weighting: On early iterations of the SAG algorithm, when most $y_{i}^{k}$ are set to the uninformative zero vector, rather than dividing $\alpha_{k}$ in by $n$ we found it was more effective to divide by $m$, the number of unique $i_{k}$ values that we have sampled so far (which converges to $n$). This modification appears more difficult to analyze, but with this modification we found that the SAG algorithm outperformed the SG/SAG hybrid algorithm analyzed in Proposition 2.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Exact regularization: For regularized objectives like we can use the exact gradient of the regularizer, rather than approximating it. For example, our experiments on $\ell_{2}$-regularized optimization problems used the recursion This can be implemented efficiently for sparse data sets by using the representation $x = {\kappaz}$, where $\kappa$ is a scalar and $z$ is a vector, since the update based on the regularizer simply updates $\kappa$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Large step sizes: Proposition 1 requires $\alpha_{k} \leqslant {{1/2}Ln}$ while under an additional assumption Proposition 2 allows $\alpha_{k} \leqslant {{1/16}L}$. In practice we observed better performance using step sizes of $\alpha_{k} = {1/L}$ and $\alpha_{k} = {2/{({L + {n\mu}})}}$. These step sizes seem to work even when the additional assumption of Proposition 2 is not satisfied, and we conjecture that the convergence rates under these step sizes are much faster than the rate obtained in Proposition 1 for the general case.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Line search: Since $L$ is generally not known, we experimented with a basic line-search, where we start with an initial estimate $L_{0}$, and we double this estimate whenever we do not satisfy the instantiated Lipschitz inequality To avoid instability caused by comparing very small numbers, we only do this test when ${\|{f_{i_{k}}'{(x^{k})}}\|}^{2} > 10^{- 8}$. To allow the algorithm to potentially achieve a faster rate due to a higher degree of local smoothness, we multiply $L_{k}$ by $2^{({- {1/n}})}$ after each iteration.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Our experiments compared an extensive variety of competitive FG and SG methods. Our first experiments focus on the following methods, which we chose because they have no dataset-dependent tuning parameters: Steepest: The full gradient method described by iteration, with a line-search that uses cubic Hermite polynomial interpolation to find a step size satisfying the strong Wolfe conditions, and where the parameters of the line-search were tuned for the problems at hand.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

AFG: Nesterov's accelerated full gradient method Nesterov, where iterations of with a fixed step size are interleaved with an extrapolation step, and we use an adaptive line-search based on Liu et al..

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

L-BFGS: A publicly-available limited-memory quasi-Newton method that has been tuned for log-linear models.^33^3 This method is by far the most complicated method we considered.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

Pegasos: The state-of-the-art SG method described by iteration with a step size of $\alpha_{k} = {{1/\mu}k}$ and a projection step onto a norm-ball known to contain the optimal solution Shalev-Shwartz et al..

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

RDA: The regularized dual averaging method Xiao, another recent state-of-the-art SG method.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

ESG: The epoch SG method Hazan and Kale, which runs SG with a constant step size and averaging in a series of epochs, and is optimal for non-smooth stochastic strongly-convex optimization.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

NOSG: The nearly-optimal SG method Ghadimi and Lan, which combines ideas from SG and AFG methods to obtain a nearly-optimal dependency on a variety of problem-dependent constants.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

SAG: The proposed stochastic average gradient method described by iteration using the modifications discussed in the previous section. We used a step-size of $\alpha_{k} = {2/{({L_{k} + {n\lambda}})}}$ where $L_{k}$ is either set constant to the global Lipschitz constant (SAG-C) or set by adaptively estimating the constant with respect to the logistic loss function using the line-search described in the previous section (SAG-LS). The SAG-LS method was initialized with $L_{0} = 1$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

The theoretical convergence rates suggest the following strategies for deciding on whether to use an FG or an SG method: If we can only afford one pass through the data, then an SG method should be used.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

If we can afford to do many passes through the data (say, several hundred), then an FG method should be used.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We expect that the SAG iterations will be most useful between these two extremes, where we can afford to do more than one pass through the data but cannot afford to do enough passes to warrant using FG algorithms like L-BFGS. To test whether this is indeed the case on real data sets, we performed experiments on a set of freely available benchmark binary classification data sets.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

The *quantum* ($p = 50000$, $p = 78$) and *protein* ($n = 145751$, $p = 74$) data set was obtained from the KDD Cup 2004 website,^44^4 the *sido* data set was obtained from the Causality Workbench website,^55^5 while the *rcv1* ($n = 20242$, $p = 47236$) and *covertype* ($n = 581012$, $p = 54$) data sets were obtained from the LIBSVM data website.^66^6 Although our method can be applied to any differentiable function, on these data sets we focus on the $\ell_{2}$-regularized logistic regression problem, with $\lambda = {1/n}$. We split each dataset in two, training on one half and testing on the other half. We added a (regularized) bias term to all data sets, and for dense features we standardized so that they would have a mean of zero and a variance of one.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We measure the training and testing costs as a function of the number of effective passes through the data, measured as the number of $f_{i}'$ evaluations divided by $n$. These results are thus independent of the practical implementation of the algorithms. We plot the training and testing costs of the different methods for 30 effective passes through the data in Figure 1.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In our second series of experiments, we sought to test whether SG methods (or the IAG method) with a very carefully chosen step size would be competitive with the SAG iterations. In particular, we compared the following variety of basic FG and SG methods.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

FG: The full gradient method described by iteration.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

AFG: The accelerated full gradient method Nesterov, where iterations of are interleaved with an extrapolation step. peg: The pegasos algorithm of Shalev-Shwartz et al., but where we multiply the step size by a constant.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

SG: The stochastic gradient method described by iteration, where we use a constant step-size.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

ASG: The stochastic gradient method described by iteration, where we use a constant step size and average the iterates.^77^7We have also compared to a variety of other SG methods, such as SG with momentum, SG with gradient averaging, accelerated SG, and using SG but delaying averaging until after the first effective pass. However, none of these SG methods performed better than the ASG method above so we omit them to keep the plots simple.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

IAG: The incremental aggregated gradient method of Blatt et al. described by iteration but with a cyclic choice of $i_{k}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

SAG: The proposed stochastic average gradient method described by iteration.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

For all of the above methods, we chose the step size that gave the best performance among powers of $10$. On the full data sets, we compare these methods to each other and to the L-BFGS and the SAG-LS algorithms from the previous experiment in Figure 2, which also shows the selected step sizes.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We can observe several trends across these experiments: FG vs. SG: Although the performance of SG methods can be catastrophic if the step size is not chosen carefully (e.g., the *quantum* and *covertype* data), with a carefully-chosen step-size the SG methods always do substantially better than FG methods on the first few passes through the data. In contrast, the adaptive FG methods in the first experiment are not sensitive to the step size and because of its steady progress the best FG method (L-BFGS) always eventually passes the SG methods.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

(FG and SG) vs. SAG: The SAG iterations seem to achieve the best of both worlds. They start out substantially better than FG methods, but continue to make steady (linear) progress which leads to better performance than SG methods. The significant speed-up observed for SAG in reaching low training costs often also seems to translate into reaching the optimal testing cost more quickly than the other methods. We also note that the proposed line-search seems to perform as well or better than choosing the optimal fixed step-size in hind sight.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

IAG vs. SAG: The second experiment shows that the IAG method performs similarly to the regular FG method, and they also show the surprising result that the randomized SAG method outperforms the closely-related deterministic IAG method by a very large margin. This is due to the larger step sizes used by the SAG iterations, which would cause the IAG iterations to diverge.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Discussion", "weight": 1.5} -->

Optimal regularization strength: One might wonder if the additional hypothesis in Proposition 2 is satisfied in practice. In a learning context, where each function $f_{i}$ is the loss associated to a single data point, $L$ is equal to the largest value of the loss second derivative $\xi$ (1 for the square loss, 1/4 for the logistic loss) times $R^{2}$, where $R$ is a the uniform bound on the norm of each data point. Thus, the constraint $\frac{\mu}{L} \geqslant \frac{8}{n}$ is satisfied when $\lambda \geqslant \frac{8\xiR^{2}}{n}$. In low-dimensional settings, the optimal regularization parameter is of the form $C/n$ Liang et al. where $C$ is a scalar constant, and may thus violate the constraint.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Discussion", "weight": 1.5} -->

However, the improvement with respect to regularization parameters of the form $\lambda = {C/\sqrt{n}}$ is known to be asymptotically negligible, and in any case in such low-dimensional settings, regular stochastic or batch gradient descent may be efficient enough in practice. In the more interesting high-dimensional settings where the dimension $p$ of our covariates is not small compared to the sample size $n$, then all theoretical analyses we are aware of advocate settings of $\lambda$ which satisfy this constraint. For example, Sridharan et al. considers parameters of the form $\lambda = \frac{C}{\sqrt{n}}$ in the parametric setting, while Eberts and Steinwart considers $\lambda = \frac{C}{n^{\beta}}$ with $\beta < 1$ in a non-parametric setting.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Discussion", "weight": 1.5} -->

Training cost vs. testing cost: The theoretical contribution of this work is limited to the convergence rate of the training cost. Though there are several settings where this is the metric of interest (e.g., variational inference in graphical models), in many cases one will be interested in the convergence speed of the testing cost. Since the $O{({1/k})}$ convergence rate of the testing cost, achieved by SG methods with decreasing step sizes (and a single pass through the data), is provably optimal when the algorithm only accesses the function through unbiased measurements of the objective and its gradient, it is unlikely that one can obtain a linear convergence rate for the testing cost with the SAG iterations. However, as shown in our experiments, the testing cost of the SAG iterates often reaches its minimum quicker than existing SG methods, and we could expect to improve the constant in the $O{({1/k})}$ convergence rate, as is the case with online second-order methods Bottou and Bousquet.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Discussion", "weight": 1.5} -->

Step-size selection and termination criteria: The three major disadvantages of SG methods are: (i) the slow convergence rate, (ii) deciding when to terminate the algorithm, and (iii) choosing the step size while running the algorithm. This paper showed that the SAG iterations achieve a much faster convergence rate, but the SAG iterations may also be advantageous in terms of tuning step sizes and designing termination criteria. In particular, the SAG iterations suggest a natural termination criterion; since the average of the $y_{i}^{k}$ variables converges to $g'{(x^{k})}$ as $\|{x^{k} - x^{k - 1}}\|$ converges to zero, we can use ${({1/n})}{\|{\sum_{i}y_{i}^{k}}\|}$ as an approximation of the optimality of $x^{k}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Discussion", "weight": 1.5} -->

Further, while SG methods require specifying a sequence of step sizes and mispecifying this sequence can have a disastrous effect on the convergence rate, our theory shows that the SAG iterations iterations achieve a linear convergence rate for any sufficiently small constant step size and our experiments indicate that a simple line-search gives strong performance.
