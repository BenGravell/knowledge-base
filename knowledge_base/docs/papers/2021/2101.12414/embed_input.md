<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Low Rank Forecasting

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the problem of forecasting multiple values of the future of a vector time series, using some past values. This problem, and related ones such as one-step-ahead prediction, have a very long history, and there are a number of well-known methods for it, including vector auto-regressive models, state-space methods, multi-task regression, and others. Our focus is on low rank forecasters, which break forecasting up into two steps: estimating a vector that can be interpreted as a latent state, given the past, and then estimating the future values of the time series, given the latent state estimate. We introduce the concept of forecast consistency, which means that the estimates of the same value made at different times are consistent. We formulate the forecasting problem in general form, and focus on linear forecasters, for which we propose a formulation that can be solved via convex optimization. We describe a number of extensions and variations, including nonlinear forecasters, data weighting, the inclusion of auxiliary data, and additional objective terms. We illustrate our methods with several examples.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Forecasting", "weight": 1.0} -->

We consider the problem of forecasting future values of a vector time series $x_{t} \in \text{R}^{n}$, $t = {1,2,\ldots}$, given previously observed values. At each time $t$ we form an estimate of the future values $x_{t + 1},\ldots,x_{t + H}$, where $H$ is our prediction horizon. We denote these as ${\hat{x}}_{t + {1|t}},{\hat{x}}_{t + {2|t}},\ldots,{\hat{x}}_{t + {H|t}}$, where ${\hat{x}}_{\tau|t}$ is our prediction of $x_{\tau}$ made at time $t$.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Forecasting", "weight": 1.0} -->

These estimates are based on the $M$ current and past values, $x_{t},x_{t - 1},\ldots,x_{{t - M} + 1}$, where $M$ is the memory of our forecaster. When $H = 1$, forecasting reduces to the common problem of predicting the next value in the time series, given the previous $M$ values.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Forecasting", "weight": 1.0} -->

We introduce some notation to denote these windows of past and future values. We define the *past* at time $t$ as We define the *future* at time $t$ as We make the observation that $p_{t}$ and $p_{t + 1}$ are related by a block shift, since where $a_{i:j}$ denotes the subvector of $a$ with entries $i,\ldots,j$. A similar shift structure holds for $f_{t}$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Forecasting", "weight": 1.0} -->

(We will come back to this soon with the concept of forecasting consistency.)

<!-- chunk {"id": "body-0007", "role": "body", "section": "Low rank forecasting and latent state", "weight": 1.0} -->

We can interpret the time series $z_{t}$, $t = {M,{M + 1},\ldots}$ as a *latent state*. The term state is justified since $z_{t}$ is a summary of the past sufficient to carry out our forecast. Under Kalman's definition, the state of a dynamic system is "the least amount of data one has to know about the past behavior of the system in order to predict its future behavior". (We note one small difference: In the traditional abstract definition of state, the past and future are infinite, whereas here we have limited them to $M$ and $H$ time periods, respectively.) The term rank for the dimension of the intermediate value $z_{t}$ is not standard; but we will see later that it coincides with the rank of a certain matrix when we restrict our attention to linear forecasters.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Low rank forecasting and latent state", "weight": 1.0} -->

The latent state can be very useful in applications, since it summarizes what we need to know to about the past at time $t$ in one vector $z_{t} \in \text{R}^{r}$, in order to carry out our forecast. In some applications, identifying the latent state can be just as important as carry out the actual forecasts.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Judging forecaster performance", "weight": 1.0} -->

Suppose we have a $T$-long observation of the time series, $x_{1},\ldots,x_{T}$, with $T \geq {M + H}$. From this data set we extract the $N$ pairs of past and future, with $N = {{T - H - M} + 1}$. We judge the performance of a forecaster on this data set by its average loss, where $\ell:{\text{R}^{Hn}\rightarrow\text{R}}$ is a convex loss function. (The lower the loss function, the better the forecast.) Common choices include the $\ell_{2}$ (squared) loss ${\ell{(u)}} = {\| u\|}_{2}^{2}$, $\ell_{1}$ loss ${\ell{(u)}} = {\| u\|}_{1}$, or an appropriate Huber penalty function \[2, §6.1.2\].

<!-- chunk {"id": "body-0010", "role": "body", "section": "Judging forecaster performance", "weight": 1.0} -->

When the data set is also the one used to fit or choose the forecaster, $\mathcal{L}$ is the training loss. When the data set is a different set of data, not used to fit or choose the forecaster, $\mathcal{L}$ is the test loss. We are interested in finding a forecaster that has low test loss, i.e., makes good forecasts on data that was not used to fit it. Another approach is walk-forward cross-validation, where one produces a number of successive training and test data sets from a single data set, where all test data points occur after all training data points. (This is to avoid look-ahead bias, and is in contrast to standard cross-validation, where one creates random training and test splits.)

<!-- chunk {"id": "body-0011", "role": "body", "section": "Forecaster consistency", "weight": 1.0} -->

Consider the value $x_{\tau}$, with $\tau \geq {M + 1}$. We make predictions of $x_{\tau}$, denoted as ${\hat{x}}_{\tau|t}$, at times forecasts of the same value, made at different times and with different available information, need not be the same. We say the forecast is *consistent* if these forecasts are not too different. We note that inconsistency is not necessarily bad; it simply means that over the different periods in which we form a prediction of $x_{\tau}$, we are changing our prediction.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Forecaster consistency", "weight": 1.0} -->

While other measures of inconsistency could be used, we will judge inconsistency of the forecasts of $x_{\tau}$ using a sum of squares measure. Define the average of the predictions of $x_{\tau}$ made at different times. Thus ${\hat{x}}_{\tau|t} - {\overline{x}}_{\tau}$ is the deviation of the prediction of $x_{\tau}$ made at time $t$ and the average of all predictions we make of $x_{\tau}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Forecaster consistency", "weight": 1.0} -->

Now consider a $T$-long observation of the time series, from which we obtain the data set $(p_{t},f_{t})$, $t = {M,\ldots,{T - H}}$. We define the (sum of squares) inconsistency as While forecaster consistency need not lead to better performance (and indeed, often does not), it can be considered as a desirable property for a forecaster, independent of forecast loss or performance. As a concrete example, suppose we are predicting the future cash flows of a business, and adjusting business operations based on these forecasts. In this case, inconsistent forecasts could lead to more changes in business operations than we would like. We may prefer forecasts that are more consistent, at the cost of some loss in forecast performance.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Statistical forecasting", "weight": 1.0} -->

We mention here a general method for forecasting that includes many existing methods (described in more detail below). Suppose we assume that $\{ x_{t}\}$ is a stationary stochastic process, with a distribution of ${(p_{t},f_{t})} \in \text{R}^{M + H}$ that, by stationarity, does not depend on $t$. A natural forecast in this case is the conditional mean of the future given the past, i.e., (The forecaster function $\phi$ does not depend on $t$.) This forecaster minimizes the mean square error $\mathbf{E}{\|{{\hat{f}}_{t} - f_{t}}\|}_{2}^{2}$ over all possible forecasters.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Outline", "weight": 1.0} -->

In §2 we describe the special case of linear forecasting. In §3 we describe a number of methods for producing linear forecasters. In §4 we describe our method for low rank forecasting. In §5 we describe a number of extensions and variations, a number of which have been incorporated in the software. In §6 we show three examples: simulated, stock volatility, and traffic. We defer an extended discussion of the very large body of prior and related work to §7.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Low rank linear forecasting", "weight": 1.0} -->

So for a linear forecaster, a low rank coefficient matrix corresponds to a low rank forecaster, in the general sense.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Low rank linear forecasting", "weight": 1.0} -->

Evidently the latent state associated with a low rank linear forecaster is only defined up to an invertible linear transformation, since $\overset{\sim}{U} = {US}$ and $\overset{\sim}{V} = {S^{- 1}V}$ define the same forecaster, when $S \in \text{R}^{r \times r}$ is invertible. The latent state associated with $\overset{\sim}{U}$ and $\overset{\sim}{V}$ is $S^{T}z_{t}$, where $z_{t}$ is the latent state associated with $U$ and $V$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Hankel data matrices", "weight": 1.0} -->

Suppose we have data $x_{1},\ldots,x_{T}$, from which we extract $N = {{T - H - M} + 1}$ past/future pairs, ${(p_{M},f_{M})},\ldots,{(p_{T - H},f_{T - H})}$. From these data we form the data matrices These matrices are block Hankel, due to the shift structure mentioned in §1.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Forecasts matrix", "weight": 1.0} -->

We stack the forecasts into the matrix This matrix is in general *not* block Hankel, unless the forecaster is completely consistent, i.e., never changes its prediction of any value $x_{\tau}$. (This only happens when $\mathcal{I} = 0$.)

<!-- chunk {"id": "body-0020", "role": "body", "section": "Loss", "weight": 1.0} -->

The average loss can be expressed as where we extend $\ell$ to apply row-wise to its matrix argument, and $\mathbf{1}$ is the vector with all entries one. For the $\ell_{2}$ (squared) loss, this can be written as $\mathcal{L} = {{({1/N})}{\|{{P\theta} - F}\|}_{F}^{2}}$, where $\parallel \cdot \parallel_{F}$ denotes the Frobenius norm of a matrix.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Inconsistency", "weight": 1.0} -->

The inconsistency measure $\mathcal{I}$ can be expressed as where $\operatorname{\mathbf{d}\mathbf{i}\mathbf{s}\mathbf{t}}{(\hat{F})}$ is the Frobenius norm distance to the set of block Hankel matrices. It is readily shown that the projection $\pi{(Z)}$ of an ${N \times H}n$ matrix $Z$ onto the set of block Hankel matrices is obtained by replacing each block by the average over the corresponding anti-diagonal blocks. We observe for future use that $\mathcal{I}$ is a convex quadratic function of $\theta$. The inconsistency measure can be evaluated in $O{({NHn})}$ flops, and its gradient can be evaluated in the same order; see appendix §A for the details.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Linear forecasting methods", "weight": 1.0} -->

In this section we describe several general and well known methods for constructing a linear forecaster. Our purpose here is to describe these forecasting methods using our notation; we will not use the material of this section in the sequel. Some of the methods described here produce low rank forecasters. In other cases, if a low rank forecaster is desired, we can use the truncated SVD (singular value decomposition) of the coefficient matrix to obtain a low rank approximation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Forecasting via autocovariance", "weight": 1.0} -->

The methods described below start by modeling $(p_{t},f_{t})$ as a Gaussian zero mean random variable (that does not depend on $t$), Since ${(p_{t},f_{t})} = {(x_{{t - M} + 1},\ldots,x_{t + H})}$, $\Sigma$ is block Toeplitz, where $\Sigma_{i} = {\mathbf{E}{x_{t}x_{t + i}^{T}}}$ is the $i$th autocovariance of the process $\{ x_{t}\}$. (So $\Sigma_{- i} = \Sigma_{i}^{T}$.) There are many methods available to estimate the autocovariance matrices $\Sigma_{0},\ldots,\Sigma_{{M + H} - 1}$ from some training data; see, e.g.,.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Iterated AR($M$) forecasting", "weight": 1.0} -->

Another approach is to posit an AR($M$) model of $x_{t}$, i.e., where $\epsilon_{t} \sim {\mathcal{N}{(0,W)}}$ are independent and $A_{i} \in \text{R}^{n \times n}$, $i = {1,\ldots,m}$. We implicitly assume that the coefficients are such that the model is stable, so it defines a stationary stochastic process. A simple way to fit an AR($M$) model is by linear regression; $W$ is an estimate of the one-step ahead prediction error covariance.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Iterated AR($M$) forecasting", "weight": 1.0} -->

With this model we can work out the autocovariance matrices and then use the general formula, but we can more directly find the conditional mean of the future, given the past. Evidently we have and, continuing recursively, for $\tau = {{t + 2},\ldots}$, we have where ${\overset{\sim}{x}}_{s \mid t} = x_{t}$ if $s \leq t$ and ${\overset{\sim}{x}}_{s \mid t} = {\mathbf{E}{({x_{s} \mid p_{t}})}}$ for $s > t$. This is the same as iterating the dynamics of the AR($M$) model forward, with $\epsilon_{s} = 0$. This forecaster is evidently linear, but not, in general, low rank. (Of course it agrees with the general formula above.)

<!-- chunk {"id": "body-0026", "role": "body", "section": "Forecasting using a latent state space model", "weight": 1.0} -->

Another approach is to model $\{ x_{t}\}$ as a stationary Gaussian stochastic process generated by a state space model, where $z_{t} \in \text{R}^{r}$ is the latent state, $A \in \text{R}^{r \times r}$, and $C \in \text{R}^{n \times r}$, $\epsilon_{t} \sim {\mathcal{N}{(0,Q)}}$ is a process noise, and $\eta_{t} \sim {\mathcal{N}{(0,R)}}$ is a measurement noise. (We assume that $\epsilon_{t}$ and $\eta_{t}$ are independent of one another and across time.) We assume that the matrix $A$ is stable (i.e., its eigenvalues have magnitude less than one), so this defines a stationary stochastic process.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Forecasting using a latent state space model", "weight": 1.0} -->

There are many ways to fit a state space model to time series training data, e.g., via N4SID, EM, and least squares auto-tuning. Here too we can work out the autocovariance coefficients and use the general formula above to find a forecaster. This forecaster, not surprisingly, has low rank, indeed, rank $r$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Forecasting using a latent state space model", "weight": 1.0} -->

Here we describe the construction of the associated forecaster in a more natural way, that explains the factorization of $\theta$ into two natural parts: a state estimator, followed by a forward simulator. The first step is to determine $\mathbf{E}{({z_{t} \mid p_{t}})}$, our estimate of the current latent state, given the past. This can be done by solving the Kalman smoothing problem with memory $M$ The value of $z_{t}$ is $\mathbf{E}{({z_{t} \mid p_{t}})}$. This is a linearly constrained least squares problem, so the solution is a linear function of the past $p_{t}$, i.e., $z_{t} = {Kp_{t}}$, where $K \in \text{R}^{{r \times M}n}$. The matrix $K$ is readily found by forming the KKT optimality conditions, and standard linear algebra computations.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Forecasting using a latent state space model", "weight": 1.0} -->

We note one slight difference between this state estimator and the traditional Kalman filter: this one uses only the $M$ previous values of $x_{s}$ (i.e., $p_{t}$), whereas the Kalman filter uses all previous values.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Forecasting using a latent state space model", "weight": 1.0} -->

It is readily seen that for $\tau = {{t + 1},\ldots,{t + H}}$, we have This shows that $\theta$ has rank (at most) $r$, the dimension of the latent time series. This is hardly surprising, since under this model the past and future are independent, given the current state $z_{t}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Forecasting via regression", "weight": 1.0} -->

Regression yields another set of methods for choosing $\theta$ directly from a given training data set. (Regression methods and statistical methods are closely linked, as we discuss below.) Let $\mathcal{L}{(\theta)}$ denote the loss on the training data set. In (regularized) regression, the parameter matrix $\theta$ is chosen as a minimizer of where $\mathcal{R}:{\text{R}^{{{Mn} \times H}n}\rightarrow\text{R}}$ is a convex regularizer function, and $\lambda$ is a positive hyper-parameter. This is a convex function, so computing an optimal $\theta$ is in principle straightforward.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Forecasting via regression", "weight": 1.0} -->

The most common regression problem, ridge regression, uses $\ell_{2}$ loss and regularization, so the objective is with variable $\theta$. This has the minimizer The objective is separable across the columns of $\theta$, which means each column of $\theta$ can be found separately. This forecaster simply uses a separate ridge regression to predict $x_{\tau}$ based on $p_{t}$, for $\tau = {{t + 1},\ldots,{t + H}}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Forecasting via regression", "weight": 1.0} -->

When $\lambda = 0$, ridge regression is ordinary least squares, and coincides with the statistical method above when we use the empirical estimates of the autocovariance matrices, since $\theta = {{\hat{\Sigma}}_{\text{pp}}^{- 1}{\hat{\Sigma}}_{\text{fp}}}$, where ${\hat{\Sigma}}_{\text{pp}}$ is the empirical covariance of $p_{t}$ and ${\hat{\Sigma}}_{\text{fp}}$ is the empirical covariance of $f_{t}$ and $p_{t}$, which are given by

<!-- chunk {"id": "body-0034", "role": "body", "section": "A regularized regression method", "weight": 1.0} -->

The method we propose is a regression method with two particular regularization functions, one that encourages $\theta$ to be low rank, and another that encourages forecaster consistency. We choose $\theta$ to minimize where $\parallel \cdot \parallel_{\ast}$ is the dual norm of a matrix (also known as the nuclear norm, trace norm, Ky Fan norm, or Schatten norm), i.e., the sum of its singular values, and $\lambda$ and $\kappa$ are positive hyper-parameters that control the strength of the two types of regularization. The objective is a convex function of $\theta$, and so in principle straightforward to minimize. The nuclear norm is widely used as a convex surrogate for the (nonconvex) rank function; roughly speaking it promotes low rank of its matrix argument. Generally (but not always), the larger $\lambda$ is, the lower the rank of $\theta$. The forecaster consistency term, as discussed above, encourages $\theta$ to produce consistent forecasts.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Critical value of $\\lambda$", "weight": 1.0} -->

There is a critical value $\lambda^{\max}$, with the property that $\theta = 0$ if and only if $\lambda \geq \lambda^{\max}$. When $\mathcal{L}$ is differentiable, $\lambda^{\max}$ is given by where ${{\nabla_{\theta}\mathcal{L}}{}} \in \text{R}^{{{Mn} \times H}n}$ is the gradient of $\mathcal{L}{(\theta)}$ at $\theta = 0$, and $\parallel \cdot \parallel_{2}$ is the $\ell_{2}$ norm (maximum singular value). This can be verified by examining the condition under which $\theta = 0$ is optimal, i.e., that the subdifferential of includes $0$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Critical value of $\\lambda$", "weight": 1.0} -->

When the $\ell_{2}$ loss is used, this condition reduces to (This can be computed efficiently, without forming the matrix $P^{T}F$, using power iteration.) It is convenient to express the nuclear norm regularization as $\lambda = {\alpha\lambda^{\max}}$, with $\alpha \in {\lbrack 0,1\rbrack}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Choosing $\\alpha$ and $\\kappa$", "weight": 1.0} -->

The traditional method for choosing the hyper-parameters $\alpha$ and $\kappa$ is to compute $\theta$ for a number of combinations of them, and for each forecaster, evaluate the performance on another (test) data set, not used to form $\theta$, i.e., train the forecaster. Among these forecasters we choose one that yields least or nearly least test loss, skewing toward larger values of $\alpha$ and $\kappa$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Choosing $\\alpha$ and $\\kappa$", "weight": 1.0} -->

When consistency is regarded as a second objective, and not a regularizer meant to give better test performance, we fix $\kappa$ and do not consider it a hyper-parameter. In this case the term $\kappa\mathcal{I}{(\theta)}$ should also be included when evaluating the test performance.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Solution method", "weight": 1.0} -->

The objective is convex, and can be minimized using many methods. Smaller instances of the problem can be solved with just a few lines of generic CVXPY code. There also exist a number of specialized methods for problems with nuclear norm regularization. Generic methods, however, will not scale well, since the number of scalar variables, $HMn^{2}$, can be very large when one or more of $H$, $M$, or $n$ is large. We describe here a simple customized method that does scale well. The method is closely related to well known methods, so we simply outline it here.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Factored problem", "weight": 1.0} -->

Suppose we know that the solution to has at most rank $k$. Then is equivalent to the *factored* problem with variables $U \in \text{R}^{{Mn} \times k}$ and $V \in \text{R}^{{k \times H}n}$. That is, $U,V$ is a solution to if and only if $\theta = {UV}$ is a solution to and ${\| U\|}_{F}^{2} = {\| V\|}_{F}^{2} = {\frac{1}{2}{\|\theta\|}_{\ast}}$. (See, e.g., for a proof.) Solving this problem directly gives us the two factors of $\theta$. In fact we obtain a balanced factorization, i.e., the (positive) singular values of $U$ and $V$ are the same.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Alternating method", "weight": 1.0} -->

The problem is not convex, but it is convex in $U$ for fixed $V$ and convex in $V$ for fixed $U$. Each of these minimizations can be carried out efficiently using, e.g., the limited-memory Broyden Fletcher Goldfarb and Shanno (L-BFGS) method. This method requires storing a modest number of matrices with the same same sizes as $U$ and $V$, and in each iteration, the computation of the gradient of the objective with respect to $U$ or $V$. (The gradients of the objective in are given in appendix §A; in our implementation they are mostly computed automatically using automatic differentiation techniques.)

<!-- chunk {"id": "body-0042", "role": "body", "section": "Computing the rank of $UV$", "weight": 1.0} -->

After solving problem, it can be the case that the rank of $UV$ is less than $k$. We can both find the rank of $UV$, compute reduced versions of $U$ and $V$, and compute the reduced-rank SVD of $\theta$ efficiently (i.e., without actually computing the full SVD of $\theta = {UV}$ or even forming $\theta$) as follows. Denote the rank of $U$ by $r_{U}$ and the rank of $V$ by $r_{V}$. First, we compute the SVD of $U$ and $V$, where $U_{U},\Sigma_{U},V_{U}$ and $U_{V},\Sigma_{V},V_{V}$ are the appropriate sizes.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Choosing $k$", "weight": 1.0} -->

We propose the following simple method for choosing the value of $k$. We start with a modest value of $k$ (say 10 or 20), solve, and then if $r = {\operatorname{\mathbf{r}\mathbf{a}\mathbf{n}\mathbf{k}}{({UV})}} = k$ (computed using the method above), we double $k$ and solve again. If, on the other hand, $r < k$, then we know that our choice of $k$ was large enough, and terminate.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Convergence", "weight": 1.0} -->

Since this is an alternating method, the objective is decreasing and so converges. Whether the alternating method converges to the solution of the original (convex) problem is another question. We can check for global optimality of $\theta = {UV}$ in the original convex problem as follows. Suppose $\ell$ is differentiable and let i.e., the gradient of the differentiable part of the objective. Then $\theta$ is globally optimal if and only if the following conditions hold where $\theta = {U_{\theta}\Sigma_{\theta}V_{\theta}}$ is the SVD of $\theta$ (computed as described in above). The residuals of these three conditions could be used as a stopping criterion for the alternating method.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Convergence", "weight": 1.0} -->

We have observed that in all numerical examples when $r < k$, the final $\theta$ is close to satisfying the optimality conditions above. Unfortunately, verifying optimality requires us to form a matrix the same size as $\theta$, as well as compute its norm. While the norm could be evaluated using a power method, never explicitly forming the matrix, we would suggest that this final global optimality check is not needed in practice.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Practical considerations", "weight": 1.0} -->

When we are solving the problem for many values of $\alpha$ and $\kappa$, or performing walk-forward cross-validation, we can warm-start this iterative algorithm at the previously computed solution. It is worth noting that we do not need to actually form $P$ or $F$. This can be necessary when the size of the original time series fits in memory but $P$ and $F$ do not, which could be the case when $M$ or $H$ is very large. All we need is to compute the gradient of the objective with respect to $U$ or $V$, which can be done without forming $P$ or $F$. For example, $PU$ can be implemented as a one-dimensional convolution of the time series $x_{1},\ldots,x_{T}$ with a number of kernels extracted from $U$. Since the alternating method only requires computing the gradient, and basic dense linear algebra, it can be performed on either a CPU or GPU.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Extensions and variations", "weight": 1.0} -->

In this section we describe a number of extensions and variations. Several of these extensions are quite useful and have been incorporated into the software.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Nonlinear forecasting", "weight": 1.0} -->

In this section we describe low rank nonlinear forecasting. Our forecaster has the familiar form $\phi = {\mathcal{V} \circ \mathcal{U}}$, but instead of the encoder and encoder being linear, they are nonlinear functions, for example neural networks. The encoder $\mathcal{U}$ encodes the past into the latent state $z_{t}$, as $z_{t} = {\mathcal{U}{(p_{t};\theta_{U})}}$ and has parameters $\theta_{U} \in \text{R}^{p_{U}}$. The decoder $\mathcal{V}$ decodes the state into the forecast ${\hat{f}}_{t}$, as ${\hat{f}}_{t} = {\mathcal{V}{(z_{t};\theta_{V})}}$ and has parameters $\theta_{V} \in \text{R}^{p_{V}}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Nonlinear forecasting", "weight": 1.0} -->

The fitting problem in the nonlinear forecasting case becomes The second term in the objective is no longer the nuclear norm of the forecaster matrix, since the predictor is nonlinear. However, it can still be useful; it will help control the complexity of the neural network parameters. We can also use the same forecaster consistency term.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Nonlinear forecasting", "weight": 1.0} -->

We can approximately solve problem using the stochastic gradient method (SGD). We refer the reader to and the references therein for possible architectures and training methods. We note that problem is equivalent to the methods described in §4 with single layer (i.e., linear) neural networks for $\mathcal{U}$ and $\mathcal{V}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Data weighting", "weight": 1.0} -->

We can weight the components of the loss function, based on how much we care about particular parts of the forecast. That is, we adjust the loss term to where $W \in \text{R}_{+}^{{N \times H}n}$ is the *weight matrix*, and $\circ$ denotes the Hadamard or elementwise product. We denote the (block) elements of $W$ as $w_{\tau \mid t}$, i.e., The larger ${(w_{\tau \mid t})}_{i}$ is, the more we care about forecasting the $i$th element of $x_{\tau}$ at time $t$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Data weighting", "weight": 1.0} -->

There are many ways to construct a weight matrix. One way is via exponentially decaying weighting on $t$, $\tau$, and a separate constant weight for each element of the time series. That is, we specify a halflife for $t$, denoted $h^{t} > 0$ and a halflife for $\tau$, denoted $h^{\tau} > 0$. Then let the weights for time and forecast time be We also specify a weight for each element of the time series, denoted $w^{col} \in \text{R}_{+}^{n}$. For example, if ${(w^{col})}_{i} = 0$, then we do not care about forecasting ${(x_{t})}_{i}$. (But note that we do use ${(x_{t})}_{i}$ to forecast the other elements of $x_{t}$.) The weights are then given by the product of these three weights,

<!-- chunk {"id": "body-0053", "role": "body", "section": "Auxiliary data", "weight": 1.0} -->

Often we have auxiliary information or data separate from the time series that can be useful for forecasting future values of the time series. Common examples are time-based features, such as hour, day of week, or month. These features could be useful for forecasting, but are clearly not worth forecasting themselves. Another example is an additional time series that is related to or correlated with our time series.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Auxiliary data", "weight": 1.0} -->

We denote the auxiliary information known at time $t$ by the vector $a_{t} \in \text{R}^{p}$. There are two ways to incorporate auxiliary information into our forecasting problem. The first is to remove the effect of $a_{t}$ on $x_{t}$, and then forecast the residual time series. We might do this by solving the problem with variable $S \in \text{R}^{n \times p}$. (We can of course add regularization here if needed.) When the auxiliary information are simple functions of time such as linear or sinusoidal, this step is called de-trending or removing the trend or seasonality from a time series (see, e.g., \[5, §9\], \[15, §13.1.1\], or \[30, Appendix A\]). We then define a new series ${\overset{\sim}{x}}_{t} = {x_{t} - {Sa_{t}}}$, and forecast that series instead of the original series.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Auxiliary data", "weight": 1.0} -->

Our final forecast is then where ${\hat{\overset{\sim}{x}}}_{\tau \mid t}$ is the forecast for ${\overset{\sim}{x}}_{\tau}$ made at time $t$. The first term is the baseline; the second is the forecast of the residual time series, with the baseline removed.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Auxiliary data", "weight": 1.0} -->

The second way to incorporate auxiliary information is to make our forecaster a function of both the past and auxiliary data. That is, we let our forecaster be where $\Phi \in \text{R}^{{p \times H}n}$. We can decide whether or not to make $\Phi$ low rank. If we want it to be low rank, then the nuclear norm regularization term becomes

<!-- chunk {"id": "body-0057", "role": "body", "section": "Other regularization", "weight": 1.0} -->

Other convex regularization on $\theta$ can be added to problem and the alternating method will work the same, because it will be biconvex in $U$ and $V$. Convex regularization on the factors $U$ and $V$ can be added, and the alternating method will work the same. For example, if we wanted the encoder $U$ to be sparse, i.e., each element of the state only depends on a few elements of the time series, then we could add a multiple of the term $\sum_{i,j}{|U_{ij}|}$ to the objective. (We note however that L-BFGS does not handle nonsmooth terms like absolute value well, so an alternate solution method might be needed.) When regularization is added to $U$ or $V$ individually, the fitting problem is nonconvex. While the algorithm will still work, there is no guarantee that it will converge to the global solution.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Latent state dynamics", "weight": 1.0} -->

If the sole objective is to forecast the original series $x_{t}$, the latent series $z_{t}$ is simply an intermediate quantity used in forming ${\hat{f}}_{t}$. In other cases, the latent series $z_{t}$ discovered by our forecasting method is actually of interest by itself. In those cases, it might be interesting to look at its dynamics, i.e., how $z_{t}$ evolves over time. One reasonable model of $z_{t}$ is an autoregressive model, where $A \in \text{R}^{r \times r}$ and $\epsilon_{t} \in {\mathcal{N}{(0,W)}}$ are independent. We can fit such a model by linear regression.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Examples", "weight": 1.0} -->

In this section we apply our method to three examples. All experiments were conducted using PyTorch on an unloaded Nvidia 1080 TI GPU.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Simulated state space dataset", "weight": 1.0} -->

We consider a dataset sampled from a state space model, where the state is $z_{t} \in \text{R}^{2}$ and the observations are $x_{t} \in \text{R}^{10}$. The entries of $A$ and $C$ are randomly sampled according to We scale $A$ so that its spectral radius is 0.98. We set the covariance matrices to $Q = I$ and $R = {{(0.1)}I}$. We consider as our training dataset a length 100 sample from the model, and as our test dataset a length 500 sample from the model. (In both of these datasets $z_{1}$ was sampled from the steady state distribution.) We take $H = M = 12$, so $\theta \in \text{R}^{120 \times 120}$ and we are using the 12 most recent values of $\{ x_{t}\}$ to predict the next 12 values of $\{ x_{t}\}$. The forecaster matrix $\theta$ contains $14400$ entries.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Simulated state space dataset", "weight": 1.0} -->

We begin by constructing the optimal (conditional mean) forecaster using the techniques described in §2, and the actual (true) values of $A$, $C$, $Q$, and $R$. This forecaster has a test loss of 10.54. Aside from the small difference between expectation and the empirical loss over the test set, no forecaster can do better, since this forecaster minimizes mean square loss over all forecasters, and uses the true values of the autocovariance matrices. We can therefore consider $10.54$ as an approximate lower bound on achievable performance.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Simulated state space dataset", "weight": 1.0} -->

Next we apply our method to the training dataset over 50 values of $\alpha \in {\lbrack 0.01,0.3\rbrack}$, with $\kappa = 0$, and in figure 1 plot the test loss and rank of $\theta$ versus $\alpha$. Fitting the forecaster took roughly five seconds. (Warm starting the optimization from the previous value of $\alpha$ reduced this considerably.) As $\alpha$ increases, the rank goes down. As $\alpha$ increases, the test loss initially goes down, and then after a certain value, the test loss begins to go up. This suggests that a good value of $\alpha$ is around 0.1, which corresponds to a forecaster of rank 2, which is the true dimension of the latent state. The test loss of this forecaster is 18.28, a bit above the lower bound found when the exact values of $A$, $C$, $Q$, and $R$ are used.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Simulated state space dataset", "weight": 1.0} -->

For comparison, the test loss for the zero forecaster is $50.7$, and the test loss for the empirical autocovariance forecaster is $27.23$. In figure 2 we show a forecast from our model (with $\alpha = 0.1$) on the test dataset.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Simulated state space dataset", "weight": 1.0} -->

We can also compare our extracted latent state to the true latent state. As mentioned above, the latent state is modulo a linear change of coordinates, so to compare the true latent state and the latent state of our forecaster, we use our latent state to predict the true latent state of the underlying state space model, by choosing $S$ to minimize over the coordinate transformation $S \in \text{R}^{2 \times 2}$. In figure 3 we plot the transformed states. We can see that our transformed latent states reasonably track the true latent states.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Simulated state space dataset", "weight": 1.0} -->

We can trade off forecaster consistency for performance. We fit the forecaster with $\alpha = 0.1$ for a number of values of $\kappa \in {\lbrack 10^{- 2},10^{1}\rbrack}$. In figure 4 we compare the train and test loss versus the train and test forecaster consistency for these values of $\kappa$. To improve forecaster consistency, we have to sacrifice performance (e.g., a 1000x reduction in forecaster consistency more than doubles our test loss). Finally, in figure 5 we demonstrate the effect of encouraging forecaster consistency.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Stock index absolute returns", "weight": 1.0} -->

In this example, we use previous absolute returns of a stock index to forecast future absolute returns of the index. It has been observed that stocks exhibit volatility clustering, first observed by Mandelbrot when he wrote "large changes tend to be followed by large changes, of either sign, and small changes tend to be followed by small changes". In this example we use the techniques of low rank forecasting to analyze volatility clustering. Along the way, we find that the latent state in a rank one forecaster very closely resembles the CBOE Volatility index (VIX), an index that tracks the 30-day expected volatility of the US stock market. We note that our model is very similar in spirit to a GARCH model, which has been observed to work well for modeling market volatility.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Stock index absolute returns", "weight": 1.0} -->

We gathered the daily absolute return of the SPY ETF (exchange traded fund), an ETF that closely tracks the S&P 500 index, from February 1993 to October 2020 ($T \approx 7000$). We annualize the daily absolute return by multiplying them by $\sqrt{250}$. We split the original dataset in half, into a training and test dataset. We also pre-process both datasets by subtracting the mean of $\{ x_{t}\}$ on the training dataset from both the training and test dataset.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Stock index absolute returns", "weight": 1.0} -->

Our goal will be to predict the next month of SPY's absolute returns ($H = 20$ trading days) from the past quarter of SPY's absolute returns ($M = 60$ trading days). The parameter $\theta$ is thus a 60 by 20 matrix, containing $1200$ entries.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Stock index absolute returns", "weight": 1.0} -->

We tried a number of values of $\alpha$, and found that $\alpha = 0.05$ worked well, and corresponds to a rank one forecaster. Fitting each forecaster took roughly four seconds, not using warm-start. (Warm starting the optimization from the previous value of $\alpha$ reduced this considerably.) The test loss of this forecaster is 0.022; for comparison, the test loss for the mean forecaster is 0.026, meaning our forecaster provides a 15% percent improvement in test loss. In figure 7 we show a forecast from our model on the test dataset. In figure 8 we show the forecaster test loss versus horizon (how many steps it is forecasting out). As expected, the test loss increases as we forecast further out.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Stock index absolute returns", "weight": 1.0} -->

In figure 6 we plot the latent state of the forecaster, along with the VIX, on the test set. At least visually, the forecaster's latent state looks like a (shifted and scaled) smooth version of the VIX. To investigate the correlation between the forecaster latent state and VIX, we took the deciles of both series, and calculated the number of times each series were in their respective deciles. In figure 9 we show a heatmap of the deciles. When the VIX index is in its highest decile, the forecaster latent state is also in its highest decile over 80% of the time. The heatmap looks very close to diagonal, so we can conclude that the two time series are very correlated.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Stock index absolute returns", "weight": 1.0} -->

Since the encoder $U$ and the decoder $V$ are both vectors (indeed one-dimensional filters), we can plot them. In figure 10 we show the parameters of the encoder and decoder. We can see that the decoder is most sensitive to the most recent values of the series, and also assigns high importance to the absolute returns 40 trading days ago (around $i = 20$). We also observe that the decoder $V$ is roughly decreasing in $i$; this means that the farther out we are forecasting, the closer the forecast gets to 0, or to simply predicting the mean value.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Traffic", "weight": 1.0} -->

We consider a dataset from the Caltrans performance measurement system (PeMS), which is composed of hourly road occupancy rates at $n = 100$ stations located on highways in Caltrans District 4 (the San Francisco Bay Area) from October 2019 to December 2019. Each data entry is the average occupancy rate over the hour, between 0 and 1, which is roughly the average fraction of the time each vehicle was present in that segment over 30 second windows (for more details see ).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Pre-processing", "weight": 1.0} -->

We carried out several pre-processing steps. We first clip or Winsorize the raw occupancy rates $o_{t}$ to be in $\lbrack 0.001,0.999\rbrack$, and then perform a logit transform, i.e., where division and $\log$ are elementwise. (This yields a more normal distribution.)

<!-- chunk {"id": "body-0074", "role": "body", "section": "Pre-processing", "weight": 1.0} -->

We split the dataset in half into a training and test dataset. We subtracted the mean occupancy rate on the training dataset for each station from the occupancy rates in both the training and test dataset. We take $M = 24$ and $H = 6$, so from the last day of traffic we predict the next quarter day of traffic. In total, there are around 1.4 million parameters in a linear forecaster. We use the $\ell_{2}$ (squared) loss. The loss of the constant (mean) forecaster was 1.108 on the training dataset and 0.962 on the test dataset.

<!-- chunk {"id": "body-0075", "role": "body", "section": "De-trending", "weight": 1.0} -->

We de-trend the time series as described in §5.3 by using auxiliary time-based features. As auxiliary features we use sine and cosine of hour (with periods of 24, 12, 8, 6, and 24/5 hours), hour in week (at harmonic periods of 168, 168/2, 168/3, 168/4, and 168/5 hours), and a binary weekday/weekend feature. We also use all pairwise products of these auxiliary features, which for products of sines and cosines are sinusoids at the sum and difference frequencies. In total there are 462 auxiliary features. This (deterministic) baseline model yields a training loss of 0.099 and a test loss of 0.203.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Forecasting", "weight": 1.0} -->

Next, we construct a low rank forecaster for the residual series. Figure 11 shows the rank and test loss versus the regularization parameter $\alpha$. The choice $\alpha = 0.07$ yields a rank 14 forecaster with a test loss of 0.184, and improvement of around 10% over the baseline model. Fitting the forecaster takes around 11 seconds. An example forecast is shown in figure 12.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Classical time series models", "weight": 1.0} -->

Classical models of time series model them as stationary stochastic processes. Given the random process, the optimal (in terms of mean squared loss) forecaster is the conditional mean forecaster, i.e., the forecast of future values is the mean of the future values given the observed past \[5, §5\]. Some common linear models that fall under this category are the Wiener filter, exponential smoothing, moving average \[5, §3.3\], autoregressive \[5, §3.2\], ARMA \[5, §3.4\], and ARIMA \[5, §4\]. Most of these models are Markov processes, meaning the future is independent of the past, given a particular state or summarization of the past. Most of these models are also special cases of linear state space models, and exact forecasting can be done by first Kalman filtering, and then iterating the state space model without disturbances \[5, §5.5\]. There exist many methods to fit state space models to data \[5, §7\], including N4SID, EM, and least squares auto-tuning.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Classical time series models", "weight": 1.0} -->

State space models are very closely related to dynamic factor models, which have found applications in economics. Our paper is focused on the problem of forecasting, and does not explicitly construct a stochastic model of the time series.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Minimum order system identification", "weight": 1.0} -->

A closely related problem in system identification is finding the minimal order representation of a linear system. One approach is to construct a Hankel matrix of impulse responses, which was first proposed by Ho and Kalman, and later expanded upon by Tether, Risannen, Woodside, Silverman, Akaike, Chow, and Aoki. These early papers spawned the field of subspace identification, which has resulted in techniques like N4SID, which take the SVD of a particular block Hankel matrix, and related techniques like MOESP and CVA (see, e.g., \[82, §10.6\] for a summary). We also point the reader to the paper by Jansson, which poses subspace identification methods as a regression, where the forecasting matrix is low rank.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Low rank matrix approximation", "weight": 1.0} -->

The techniques in this paper are closely related to the formation of low rank approximations to matrices, which dates all the way back to Eckart's seminal work on principal component analysis (PCA). The basis of PCA is that the truncated SVD of a matrix is the best low rank approximation of the matrix (in terms of Frobenius norm), and has been expanded heavily and generalized to different data types, objective functions, and regularization functions. A standard convex, continuous approximation of the rank function is the nuclear norm function, and convex optimization problems involving nuclear norms can be expressed as semidefinite programs, and efficient solution methods exist (see, e.g., ). The nuclear norm also exhibits a number of nice theoretical properties, e.g., it can be used to recover the true minimum rank solution for certain problems, and near-optimal solutions in others. It has also proved to be a useful heuristic for system identification problems. For more discussion on the nuclear norm, and its applications, see, e.g., and the references therein.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Reduced rank prediction", "weight": 1.0} -->

A closely related problem is reduced rank prediction. Reduced rank regression can be traced back to the work, where a likelihood-ratio test is obtained for the hypothesis that the rank of the regression coefficient matrix is a given number. Later, the work provided an explicit form of the estimate of the regression coefficient matrix with a given rank, and discussed the asymptotics of the estimated regression coefficient matrix. The reduced rank regression problem was approximately solved as a nuclear norm penalized least squares problem, and then further generalized into an adaptive nuclear norm penalized reduced rank regression problem. For more details on reduced rank regression, please refer to. The optimization problem in the form of a loss function plus a nuclear norm regularization term has applications in in multi-task learning; see, e.g.,.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Reduced rank time series", "weight": 1.0} -->

Similar to reduced rank regression, reduced rank time series modeling is also closely connected with the low rank forecasting problem. Early work such as fit reduced rank coefficient models to vector time series to provide a concise representation of vector time series models. Many of these models work by extracting a lower dimensional vector time series from the past first, and then perform one-step ahead forecast (which corresponds to $H = 1$) based on the extracted low dimensional vector time series. This is very similar to the (low rank) two step forecasting technique discussed in this paper. The reduced rank modeling problem has been generalized into the structured VAR modeling problem. In these papers, regularization terms are added to encourage certain structures. For example, a nuclear norm term is often used to encourage the transition matrix to be low rank, and $\ell_{1}$ norm is used to encourage the transition matrix to be sparse.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Extracting a low-dimensional predictable time series", "weight": 1.0} -->

Another related problem is extract a low-dimensional (self-)predictable time series from a high-dimensional vector time series. The paper is an early one with the explicit goal of predictability. After this, many other methods have been developed in different research areas on extracting predictable time series, including economics, machine learning, process system engineering, signal processing, and atmospheric research. Another closely related line of work is on predictive state representations.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Nonlinear forecasters", "weight": 1.0} -->

There also exist many nonlinear forecasting methods. These methods are often based on neural networks, e.g., recurrent neural networks, convolutional neural networks, and autoencoders. Other nonlinear forecasting methods include regime switching models and NARMAX models. Recently, there have also been methods proposed that perform vector time series forecasting through matrix completion, where the vector time series are assumed share some common structures.
