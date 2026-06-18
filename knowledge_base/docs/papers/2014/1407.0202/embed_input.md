<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SAGA: A Fast Incremental Gradient Method with Support for Non-Strongly Convex Composite Objectives

Topics include SAGA, Variance reduction, Incremental gradient methods, Finite-sum optimization, Composite optimization, Proximal methods, Non-strongly convex optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces SAGA, an unbiased table-based variance-reduced incremental-gradient method that bridges ideas from SAG, SDCA, and SVRG. Its main contribution is a tighter and more flexible theory covering composite objectives, direct non-strongly-convex use, and automatic adaptation to inherent strong convexity.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this work we introduce a new optimisation method called SAGA in the spirit of SAG, SDCA, MISO and SVRG, a set of recently proposed incremental gradient algorithms with fast linear convergence rates. SAGA improves on the theory behind SAG and SVRG, with better theoretical convergence rates, and has support for composite objectives where a proximal operator is used on the regulariser. Unlike SDCA, SAGA supports non-strongly convex problems directly, and is adaptive to any inherent strong convexity of the problem. We give experimental results showing the effectiveness of our method.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Remarkably, recent advances have shown that it is possible to minimise strongly convex finite sums provably faster in expectation than is possible without the finite sum structure. This is significant for machine learning problems as a finite sum structure is common in the empirical risk minimisation setting. The requirement of strong convexity is likewise satisfied in machine learning problems in the typical case where a quadratic regulariser is used.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, we are interested in minimising functions of the form

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $x \in {\mathbb{R}}^{d}$, each $f_{i}$ is convex and has Lipschitz continuous derivatives with constant $L$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $h:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$ is convex but potentially non-differentiable, and where the proximal operation of $h$ is easy to compute --- few incremental gradient methods are applicable in this setting.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contributions are as follows. In Section 2 we describe the SAGA algorithm, a novel incremental gradient method. In Section 5 we prove theoretical convergence rates for SAGA in the strongly convex case better than those for SAG and SVRG, and a factor of 2 from the SDCA convergence rates. These rates also hold in the composite setting. Additionally, we show that like SAG but unlike SDCA, our method is applicable to non-strongly convex problems without modification. We establish theoretical convergence rates for this case also. In Section 3 we discuss the relation between each of the fast incremental gradient methods, showing that each stems from a very small modification of another.

<!-- chunk {"id": "body-0009", "role": "body", "section": "SAGA Algorithm", "weight": 1.0} -->

We start with some known initial vector $x^{0} \in {\mathbb{R}}^{d}$ and known derivatives ${f_{i}^{\prime}{(\phi_{i}^{0})}} \in {\mathbb{R}}^{d}$ with $\phi_{i}^{0} = x^{0}$ for each $i$. These derivatives are stored in a table data-structure of length $n$, or alternatively a $n \times d$ matrix. For many problems of interest, such as binary classification and least-squares, only a single floating point value instead of a full gradient vector needs to be stored (see Section 4). SAGA is inspired both from SAG and SVRG (as we will discuss in Section 3).

<!-- chunk {"id": "body-0010", "role": "body", "section": "SAGA Algorithm", "weight": 1.0} -->

The proximal operator we use above is defined as

<!-- chunk {"id": "body-0011", "role": "body", "section": "SAGA Algorithm", "weight": 1.0} -->

We prove this result in Section 5. The requirement of strong convexity can be relaxed from needing to hold for each $f_{i}$ to just holding on average, but at the expense of a worse geometric rate ($1 - \frac{\mu}{6{({{\mun} + L})}})$, requiring a step size of $\gamma = {1/{({3{({{\mun} + L})}})}}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "SAGA Algorithm", "weight": 1.0} -->

In the non-strongly convex case, we have established the convergence rate in terms of the average iterate, excluding step 0: ${\overline{x}}^{k} = {\frac{1}{k}{\sum_{t = 1}^{k}x^{t}}}$. Using a step size of $\gamma = {1/{({3L})}}$ we have

<!-- chunk {"id": "body-0013", "role": "body", "section": "SAGA Algorithm", "weight": 1.0} -->

This result is proved in the supplementary material.

<!-- chunk {"id": "body-0014", "role": "body", "section": "SAGA Algorithm", "weight": 1.0} -->

Although any incremental gradient method can be applied to non-strongly convex problems via the addition of a small quadratic regularisation, the amount of regularisation is an additional tunable parameter which our method avoids.

<!-- chunk {"id": "body-0015", "role": "body", "section": "SAGA: midpoint between SAG and SVRG/S2GD", "weight": 1.0} -->

In, the authors make the observation that the variance of the standard stochastic gradient (SGD) update direction can only go to zero if decreasing step sizes are used, thus preventing a linear convergence rate unlike for batch gradient descent. They thus propose to use a variance reduction approach (see and references therein for example) on the SGD update in order to be able to use constant step sizes and get a linear convergence rate. We present the updates of their method called SVRG (Stochastic Variance Reduced Gradient) in below, comparing it with the non-composite form of SAGA rewritten. They also mention that SAG (Stochastic Average Gradient) can be interpreted as reducing the variance, though they do not provide the specifics. Here, we make this connection clearer and relate it to SAGA.

<!-- chunk {"id": "body-0016", "role": "body", "section": "SAGA: midpoint between SAG and SVRG/S2GD", "weight": 1.0} -->

We first review a slightly more generalized version of the variance reduction approach (we allow the updates to be biased). Suppose that we want to use Monte Carlo samples to estimate ${\mathbb{E}}X$ and that we can compute efficiently ${\mathbb{E}}Y$ for another random variable $Y$ that is highly correlated with $X$. One variance reduction approach is to use the following estimator $\theta_{\alpha}$ as an approximation to ${\mathbb{E}}X$: $\theta_{\alpha}:={{\alpha{({X - Y})}} + {{\mathbb{E}}Y}}$, for a step size $\alpha \in {\lbrack 0,1\rbrack}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "SAGA: midpoint between SAG and SVRG/S2GD", "weight": 1.0} -->

The variance of $\theta_{\alpha}$ is: ${{Var}{(\theta_{\alpha})}} = {\alpha^{2}{\lbrack{{{{Var}{(X)}} + {{Var}{(Y)}}} - {2{{Cov}{(X,Y)}}}}\rbrack}}$, and so if ${Cov}{(X,Y)}$ is big enough, the variance of $\theta_{\alpha}$ is reduced compared to $X$, giving the method its name. By varying $\alpha$ from 0 to 1, we increase the variance of $\theta_{\alpha}$ towards its maximum value (which usually is still smaller than the one for $X$) while decreasing its bias towards zero.

<!-- chunk {"id": "body-0018", "role": "body", "section": "SAGA: midpoint between SAG and SVRG/S2GD", "weight": 1.0} -->

Both SAGA and SAG can be derived from such a variance reduction viewpoint: here $X$ is the SGD direction sample $f_{j}^{\prime}{(x^{k})}$, whereas $Y$ is a past stored gradient $f_{j}^{\prime}{(\phi_{j}^{k})}$. SAG is obtained by using $\alpha = {1/n}$ (update rewritten in our notation in ), whereas SAGA is the unbiased version with $\alpha = 1$ (see below). For the same $\phi$'s, the variance of the SAG update is $1/n^{2}$ times the one of SAGA, but at the expense of having a non-zero bias. This non-zero bias might explain the complexity of the convergence proof of SAG and why the theory has not yet been extended to proximal operators. By using an unbiased update in SAGA, we are able to obtain a simple and tight theory, with better constants than SAG, as well as theoretical rates for the use of proximal operators.

<!-- chunk {"id": "body-0019", "role": "body", "section": "SAGA: midpoint between SAG and SVRG/S2GD", "weight": 1.0} -->

The SVRG update is obtained by using $Y = {f_{j}^{\prime}{(\overset{\sim}{x})}}$ with $\alpha = 1$ (and is thus unbiased -- we note that SAG is the only method that we present in the related work that has a biased update direction). The vector $\overset{\sim}{x}$ is not updated every step, but rather the loop over $k$ appears inside an outer loop, where $\overset{\sim}{x}$ is updated at the start of each outer iteration. Essentially SAGA is at the midpoint between SVRG and SAG; it updates the $\phi_{j}$ value each time index $j$ is picked, whereas SVRG updates all of $\phi$'s as a batch. The S2GD method has the same update as SVRG, just differing in how the number of inner loop iterations is chosen. We use SVRG henceforth to refer to both methods.

<!-- chunk {"id": "body-0020", "role": "body", "section": "SAGA: midpoint between SAG and SVRG/S2GD", "weight": 1.0} -->

SVRG makes a trade-off between time and space. For the equivalent practical convergence rate it makes 2x-3x more gradient evaluations, but in doing so it does not need to store a table of gradients, but a single average gradient. The usage of SAG vs. SVRG is problem dependent. For example for linear predictors where gradients can be stored as a reduced vector of dimension $p - 1$ for $p$ classes, SAGA is preferred over SVRG both theoretically and in practice. For neural networks, where no theory is available for either method, the storage of gradients is generally more expensive than the additional backpropagations, but this is computer architecture dependent.

<!-- chunk {"id": "body-0021", "role": "body", "section": "SAGA: midpoint between SAG and SVRG/S2GD", "weight": 1.0} -->

SVRG also has an additional parameter besides step size that needs to be set, namely the number of iterations per inner loop ($m$). This parameter can be set via the theory, or conservatively as $m = n$, however doing so does not give anywhere near the best practical performance. Having to tune one parameter instead of two is a practical advantage for SAGA.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Finito/MISO$\\mu$", "weight": 1.0} -->

Eliminating $u^{k}$ recovers the update for $x^{k}$. We now describe how the Finito and MISO$\mu$ methods are closely related to SAGA.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Finito/MISO$\\mu$", "weight": 1.0} -->

The step size used is of the order of ${1/\mu}n$. To simplify the discussion of this algorithm we will introduce the notation $\overline{\phi} = {\frac{1}{n}{\sum_{i}\phi_{i}^{k}}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Finito/MISO$\\mu$", "weight": 1.0} -->

SAGA can be interpreted as Finito, but with the quantity $\overline{\phi}$ replaced with $u$, which is updated in the same way as $\overline{\phi}$, but *in expectation*.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Finito/MISO$\\mu$", "weight": 1.0} -->

The update is identical in expectation to the update for $u$, $u^{k + 1} = {u^{k} + {\frac{1}{n}{({x^{k} - u^{k}})}}}$. There are three advantages of SAGA over Finito/MISO$\mu$. SAGA does not require strong convexity to work, it has support for proximal operators, and it does not require storing the $\phi_{i}$ values. MISO has proven support for proximal operators only in the case where impractically small step sizes are used. The big advantage of Finito/MISO$\mu$ is that when using a per-pass re-permuted access ordering, empirical speed-ups of up-to a factor of 2x has been observed. This access order can also be used with the other methods discussed, but with smaller empirical speed-ups. Finito/MISO$\mu$ is particularly useful when $f_{i}$ is computationally expensive to compute compared to the extra storage costs required over the other methods.

<!-- chunk {"id": "body-0026", "role": "body", "section": "SDCA", "weight": 1.0} -->

The Stochastic Dual Coordinate Descent (SDCA) method on the surface appears quite different from the other methods considered. It works with the convex conjugates of the $f_{i}$ functions. However, in this section we show a novel transformation of SDCA into an equivalent method that only works with primal quantities, and is closely related to the MISO$\mu$ method.

<!-- chunk {"id": "body-0027", "role": "body", "section": "SDCA", "weight": 1.0} -->

We claim that this algorithm is equivalent to the version of SDCA where exact block-coordinate maximisation is used on the dual.^11^1More precisely, to Option I of Prox-SDCA as described in \[11, Figure 1\]. We will simply refer to this method as "SDCA" in this paper for brevity. Firstly, note that while SDCA was originally described for one-dimensional outputs (binary classification or regression), it has been expanded to cover the multi-class predictor case (called Prox-SDCA there). In this case, the primal objective has a separate strongly convex regulariser, and the functions $f_{i}$ are restricted to the form ${f_{i}{(x)}}:={\psi_{i}{({X_{i}^{T}x})}}$, where $X_{i}$ is a $d \times p$ feature matrix, and $\psi_{i}$ is the loss function that takes a $p$ dimensional input, for $p$ classes.

<!-- chunk {"id": "body-0028", "role": "body", "section": "SDCA", "weight": 1.0} -->

To stay in the same general setting as the other incremental gradient methods, we work directly with the $f_{i}{(x)}$ functions rather than the more structured $\psi_{i}{({X_{i}^{T}x})}$. The dual objective to maximise then becomes

<!-- chunk {"id": "body-0029", "role": "body", "section": "SDCA", "weight": 1.0} -->

where $\alpha_{i}$'s are $d$-dimensional dual variables.

<!-- chunk {"id": "body-0030", "role": "body", "section": "SDCA", "weight": 1.0} -->

As noted by Shalev-Shwartz & Zhang, the update is actually an instance of the proximal operator of the convex conjugate of $f_{j}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "SDCA", "weight": 1.0} -->

This decomposition allows us to compute the proximal operator of the conjugate via the primal proximal operator. As this is the only use in the basic SDCA method of the conjugate function, applying this decomposition allows us to completely eliminate the "dual" aspect of the algorithm, yielding the above primal form of SDCA. The dual variables are related to the primal representatives $\phi_{i}$'s through $\alpha_{i} = {- {f_{i}^{\prime}{(\phi_{i})}}}$. The KKT conditions ensure that if the $\alpha_{i}$ values are dual optimal then $x^{k} = {\gamma{\sum_{i}\alpha_{i}}}$ as defined above is primal optimal. The same trick is commonly used to interpret Dijkstra's set intersection as a primal algorithm instead of a dual block coordinate descent algorithm.

<!-- chunk {"id": "body-0032", "role": "body", "section": "SDCA", "weight": 1.0} -->

The primal form of SDCA differs from the other incremental gradient methods described in this section in that it assumes strong convexity is induced by a separate strongly convex regulariser, rather than each $f_{i}$ being strongly convex. In fact, SDCA can be modified to work without a separate regulariser, giving a method that is at the midpoint between Finito and SDCA. We detail such a method in the supplementary material.

<!-- chunk {"id": "body-0033", "role": "body", "section": "SDCA variants", "weight": 1.0} -->

Note that $\phi_{j}^{k + 1}$ does not actually have to be explicitly known, just the gradient $f_{j}^{\prime}{(\phi_{j}^{k + 1})}$, which is the result of the above interpolation. Variant 5 by Shalev-Shwartz & Zhang does not require operations on the conjugate function, it simply uses $\beta = \frac{\mun}{L + {\mun}}$. The most practical variant performs a line search involving the convex conjugate to determine $\beta$. As far as we are aware, there is no simple primal equivalent of this line search. So in cases where we can not compute the proximal operator from the standard SDCA variant, we can either introduce a tuneable parameter into the algorithm ($\beta$), or use a dual line search, which requires an efficient way to evaluate the convex conjugates of each $f_{i}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Implementation", "weight": 1.0} -->

For many problems each derivative $f_{i}^{\prime}$ is just a simple weighting of the $i$th data vector. Logistic regression and least squares have this property. In such cases, instead of storing the full derivative $f_{i}^{\prime}$ for each $i$, we need only to store the weighting constants. This reduces the storage requirements to be the same as the SDCA method in practice. A similar trick can be applied to multi-class classifiers with $p$ classes by storing $p - 1$ values for each $i$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Implementation", "weight": 1.0} -->

Our algorithm assumes that initial gradients are known for each $f_{i}$ at the starting point $x^{0}$. Instead, a heuristic may be used where during the first pass, data-points are introduced one-by-one, in a non-randomized order, with averages computed in terms of those data-points processed so far. This procedure has been successfully used with SAG.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Implementation", "weight": 1.0} -->

The SAGA update as stated is slower than necessary when derivatives are sparse. A just-in-time updating of $u$ or $x$ may be performed just as is suggested for SAG, which ensures that only sparse updates are done at each iteration.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Implementation", "weight": 1.0} -->

We give the form of SAGA for the case where each $f_{i}$ is strongly convex. However in practice we usually have only convex $f_{i}$, with strong convexity in $f$ induced by the addition of a quadratic regulariser. This quadratic regulariser may be split amongst the $f_{i}$ functions evenly, to satisfy our assumptions.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Implementation", "weight": 1.0} -->

For sparse implementations instead of scaling $x^{k}$ at each step, a separate scaling constant $\beta^{k}$ may be scaled instead, with $\beta^{k}x^{k}$ being used in place of $x^{k}$. This is a standard trick used with stochastic gradient methods.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Implementation", "weight": 1.0} -->

For sparse problems with a quadratic regulariser the just-in-time updating can be a little intricate. In the supplementary material we provide example python code showing a correct implementation that uses each of the above tricks.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Theory", "weight": 1.0} -->

In this section, all expectations are taken with respect to the choice of $j$ at iteration $k + 1$ and conditioned on $x^{k}$ and each $f_{i}^{\prime}{(\phi_{i}^{k})}$ unless stated otherwise.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Theory", "weight": 1.0} -->

We start with two basic lemmas that just state properties of convex functions, followed by Lemma 1, which is specific to our algorithm. The proofs of each of these lemmas is in the supplementary material.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

We performed a series of experiments to validate the effectiveness of SAGA. We tested a binary classifier on MNIST, COVTYPE, IJCNN1 and a least squares predictor on MILLIONSONG. Details of these datasets can be found. We used the same code base for each method, just changing the main update rule. SVRG was tested with the recalibration pass used every $n$ iterations, as suggested. Each method had its step size parameter chosen so as to give the fastest convergence.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

We tested with a L2 regulariser, which all methods support, and with a L1 regulariser on a subset of the methods. The results are shown in Figure 2. We can see that Finito (perm) performs the best on a per epoch equivalent basis, but it can be the most expensive method per step. SVRG is similarly fast on a per epoch basis, but when considering the number of gradient evaluations per epoch is double that of the other methods for this problem, it is middle of the pack. SAGA can be seen to perform similar to the non-permuted Finito case, and to SDCA. Note that SAG is slower than the other methods at the beginning. To get the optimal results for SAG, an adaptive step size rule needs to be used rather than the constant step size we used. In general, these tests confirm that the choice of methods should be done based on their properties as discussed in Section 3, rather than their convergence rate.
