<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Efficient Learning of Generalized Linear and Single Index Models with Isotonic Regression

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Generalized Linear Models (GLMs) and Single Index Models (SIMs) provide powerful generalizations of linear regression, where the target variable is assumed to be a (possibly unknown) 1-dimensional function of a linear predictor. In general, these problems entail non-convex estimation procedures, and, in practice, iterative local search heuristics are often used. Kalai and Sastry recently provided the first provably efficient method for learning SIMs and GLMs, under the assumptions that the data are in fact generated under a GLM and under certain monotonicity and Lipschitz constraints. However, to obtain provable performance, the method requires a fresh sample every iteration. In this paper, we provide algorithms for learning GLMs and SIMs, which are both computationally and statistically efficient. We also provide an empirical study, demonstrating their feasibility in practice.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The oft used linear regression paradigm models a target variable $Y$ as a linear function of a vector-valued input $X$. Namely, for some vector $w$, we assume that ${{\mathbb{E}}{\lbrack\left. Y \middle| X \right.\rbrack}} = {w \cdot X}$. Generalized linear models (GLMs) provide a flexible extension of linear regression, by assuming the existence of a "link" function $g$ such that ${{\mathbb{E}}{\lbrack\left. Y \middle| X \right.\rbrack}} = {g^{- 1}{({w \cdot X})}}$. $g$ "links" the conditional expectation of $Y$ to $X$ in a linear manner, i.e. ${g{({{\mathbb{E}}{\lbrack\left. Y \middle| X \right.\rbrack}})}} = {w \cdot X}$ (see for a review).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This simple assumption immediately leads to many practical models, including logistic regression, the workhorse for binary probabilistic modeling.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Typically, the link function is assumed to be known (often chosen based on problem-specific constraints), and the parameter $w$ is estimated using some iterative procedure. Even in the setting where $g$ is known, we are not aware of a classical estimation procedure which is computationally efficient, yet achieves a good statistical rate with provable guarantees. The standard procedure is iteratively reweighted least squares, based on Newton-Ralphson (see ).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Single Index Models (SIMs), *both* $g$ and $w$ are unknown. Here, we face the more challenging (and practically relevant) question of jointly estimating $g$ and $w$, where $g$ may come from a large non-parametric family such as all monotonic functions. There are two issues here: 1) What statistical rate is achievable for simultaneous estimation of $g$ and $w$? 2) Is there a *computationally* efficient algorithm for this joint estimation? With regards to the former, under mild Lipschitz-continuity restrictions on $g^{- 1}$, it is possible to characterize the effectiveness of an (appropriately constrained) joint empirical risk minimization procedure. This suggests that, from a purely statistical viewpoint, it may be worthwhile to attempt to jointly optimize $g$ and $w$ on the empirical data.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, the issue of *computationally efficiently* estimating both $g$ and $w$ (and still achieving a good statistical rate) is more delicate, and is the focus of this work. We note that this is not a trivial problem: in general, the joint estimation problem is highly non-convex, and despite a significant body of literature on the problem, existing methods are usually based on heuristics, which are not guaranteed to converge to a global optimum (see for instance ). We note that recently, presented a kernel-based method which does allow (improper) learning of certain types of GLM's and SIM's, even in an agnostic setting where no assumptions are made on the underlying distribution. On the flip side, the formal computational complexity guarantee degrades super-polynomially with the norm of $w$, which show is provably unavoidable in their setting.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The recently proposed Isotron algorithm provides the first provably efficient method for learning GLMs and SIMs, under the common assumption that $g^{- 1}$ is monotonic and Lipschitz, and assuming the data corresponds to the model. The algorithm attained both polynomial sample and computational complexity, with a sample size dependence that does not depend explicitly on the dimension. The algorithm is a variant of the "gradient-like" perceptron algorithm, with the added twist that on each update, an isotonic regression procedure is performed on the linear predictions. Recall that isotonic regression is a procedure which finds the best monotonic one dimensional regression function. Here, the well-known Pool Adjacent Violator ($\mathsf{P}\mathsf{A}\mathsf{V}$) algorithm provides a computationally efficient method for this task.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately, a cursory inspection of the Isotron algorithm suggests that, while it is computationally efficient, it is very wasteful statistically, as each iteration of the algorithm throws away all previous training data and requests new examples. Our intuition is that the underlying technical reasons for this are due to the fact that the $\mathsf{P}\mathsf{A}\mathsf{V}$ algorithm need not return a function with a bounded Lipschitz constant. Furthermore, empirically, it not clear how deleterious this issue may be.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work seeks to address these issues both theoretically and practically. We present two algorithms, the GLM-tron algorithm for learning GLMs with a known monotonic and Lipschitz $g^{- 1}$, and the L-Isotron algorithm for the more general problem of learning SIMs, with an unknown monotonic and Lipschitz $g^{- 1}$. Both algorithms are practical, parameter-free and are provably efficient, both statistically and computationally. Moreover, they are both easily kernelizable. In addition, we investigate both algorithms empirically, and show they are both feasible approaches. Furthermore, our results show that the original Isotron algorithm (ran on the same data each time) is perhaps also effective in several cases, even though the $\mathsf{P}\mathsf{A}\mathsf{V}$ algorithm does not have a Lipschitz constraint.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

More generally, it is interesting to note how the statistical assumption that the data are in fact generated by some GLM leads to an efficient estimation procedure, despite it being a non-convex problem. Without making any assumptions, i.e. in the agnostic setting, this problem is at least hard as learning parities with noise.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Setting", "weight": 1.0} -->

We assume the data $(x,y)$ are sampled i.i.d. from a distribution supported on ${\mathbb{B}}_{d} \times {\lbrack 0,1\rbrack}$, where ${\mathbb{B}}_{d} = {\{{x \in {\mathbb{R}}^{d}}:{\left\| x \right\| \leq 1}\}}$ is the unit ball in $d$-dimensional Euclidean space. Our algorithms and analysis also apply to the case where ${\mathbb{B}}_{d}$ is the unit ball in some high (or infinite)-dimensional kernel feature space.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Setting", "weight": 1.0} -->

We assume there is a fixed vector $w$, such that $\left\| w \right\| \leq W$, and a non-decreasing $1$-Lipschitz function $u:{{\mathbb{R}}\rightarrow{\lbrack 0,1\rbrack}}$, such that ${{\mathbb{E}}{\lbrack\left. y \middle| x \right.\rbrack}} = {u{({w \cdot x})}}$ for all $x$. Note that $u$ plays the same role here as $g^{- 1}$ in generalized linear models, and we use this notation for convenience. Also, the restriction that $u$ is 1-Lipschitz is without loss of generality, since the norm of $w$ is arbitrary (an equivalent restriction is that $\left\| w \right\| = 1$ and that $u$ is $W$-Lipschitz for an arbitrary $W$).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Setting", "weight": 1.0} -->

Our focus is on approximating the regression function well, as measured by the squared loss. For a real valued function $h:{{\mathbb{B}}_{d}\rightarrow{\lbrack 0,1\rbrack}}$, define ${err}{(h)}$ measures the error of $h$, and $\varepsilon{(h)}$ measures the excess error of $h$ compared to the Bayes-optimal predictor $x\mapsto{u{({w \cdot x})}}$. Our goal is to find $h$ such that $\varepsilon{(h)}$ (equivalently, ${err}{(h)}$) is as small as possible.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Setting", "weight": 1.0} -->

In addition, we define the empirical counterpart ${\hat{err}{(h)}},{\hat{\varepsilon}{(h)}}$, based on a sample ${(x_{1},y_{1})},\ldots,{(x_{m},y_{m})}$, to be Note that $\hat{\varepsilon}$ is the standard *fixed design error* (as this error conditions on the observed $x$'s).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Setting", "weight": 1.0} -->

Our algorithms work by iteratively constructing hypotheses $h^{t}$ of the form ${h^{t}{(x)}} = {u^{t}{({w^{t} \cdot x})}}$, where $u^{t}$ is a non-decreasing, $1$-Lipschitz function, and $w^{t}$ is a linear predictor. The algorithmic analysis provides conditions under which $\hat{\varepsilon}{(h^{t})}$ is small, and using statistical arguments, one can guarantee that $\varepsilon{(h^{t})}$ would be small as well.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Setting", "weight": 1.0} -->

To simplify the presentation of our results, we use the standard $O{( \cdot )}$ notation, which always hides only universal constants.

<!-- chunk {"id": "body-0018", "role": "body", "section": "The GLM-tron Algorithm", "weight": 1.0} -->

We begin with the simpler case, where the transfer function $u$ is assumed to be known (e.g. a sigmoid), and the problem is estimating $w$ properly. We present a simple, parameter-free, perceptron-like algorithm, GLM-tron, which efficiently finds a close-to-optimal predictor. We note that the algorithm works for arbitrary non-decreasing, Lipschitz functions $u$, and thus covers most generalized linear models. The pseudo-code appears as Algorithm 1.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The GLM-tron Algorithm", "weight": 1.0} -->

To analyze the performance of the algorithm, we show that if we run the algorithm for sufficiently many iterations, one of the predictors $h^{t}$ obtained must be nearly-optimal, compared to the Bayes-optimal predictor.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The L-Isotron Algorithm", "weight": 1.0} -->

We now present L-Isotron, in Algorithm 2, which is applicable to the harder setting where the transfer function $u$ is unknown, except for it being non-decreasing and $1$-Lipschitz. This corresponds to the semi-parametric setting of single index models.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The L-Isotron Algorithm", "weight": 1.0} -->

The algorithm that we present is again simple and parameter-free. The main difference compared to GLM-tron algorithm is that now the transfer function must also be learned, and the algorithm keeps track of a transfer function $u^{t}$ which changes from iteration to iteration. The algorithm is also rather similar to the Isotron algorithm, with the main difference being that instead of applying the $\mathsf{P}\mathsf{A}\mathsf{V}$ procedure to fit an arbitrary monotonic function at each iteration, we use a different procedure, $\mathsf{L}\mathsf{P}\mathsf{A}\mathsf{V}$, which fits a *Lipschitz* monotonic function. This difference is the key which allows us to make the algorithm practical while maintaining non-trivial guarantees (getting similar guarantees for the Isotron required a fresh training sample at each iteration).

<!-- chunk {"id": "body-0022", "role": "body", "section": "The L-Isotron Algorithm", "weight": 1.0} -->

The $\mathsf{L}\mathsf{P}\mathsf{A}\mathsf{V}$ procedure takes as input a set of points ${(z_{1},y_{1})},\ldots,{(z_{m},y_{m})}$ in ${\mathbb{R}}^{2}$, and fits a non-decreasing, $1$-Lipschitz function $u$, which minimizes $\sum_{i = 1}^{m}{({{u{(z_{i})}} - y_{i}})}^{2}$. This problem has been studied in the literature, and we followed the method of in our empirical studies. The running time of the method proposed is $O{(m^{2})}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "The L-Isotron Algorithm", "weight": 1.0} -->

While this can be slow for large-scale datasets, we remind the reader that this is a one-dimensional fitting problem, and thus a highly accurate fit can be achieved by randomly subsampling the data (the details of this argument, while straightforward, are beyond the scope of the paper).

<!-- chunk {"id": "body-0024", "role": "body", "section": "The L-Isotron Algorithm", "weight": 1.0} -->

We now turn to the formal analysis of the algorithm. The formal guarantees parallel those of the previous subsection. However, the rates achieved are somewhat worse, due to the additional difficulty of simultaneously estimating both $u$ and $w$. It is plausible that these rates are sharp for information-theoretic reasons, based on the 1-dimensional lower bounds (although the assumptions are slightly different, and thus they do not directly apply to our setting).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we present an empirical study of the GLM-tron and the L-Isotron algorithms. The first experiment we performed is a synthetic one, and is meant to highlight the difference between L-Isotron and the Isotron algorithm of. In particular, we show that attempting to fit the transfer function without any Lipschitz constraints may cause Isotron to overfit, complementing our theoretical findings. The second set of experiments is a comparison between GLM-tron, L-Isotron and several competing approaches. The goal of these experiments is to show that our algorithms perform well on real-world data, even when the distributional assumption required for their theoretical guarantees does not precisely hold.

<!-- chunk {"id": "body-0026", "role": "body", "section": "L-Isotron vs Isotron", "weight": 1.0} -->

As discussed earlier, our L-Isotron algorithm (Algorithm 2) is similar to the Isotron algorithm of, with two main differences: First, we apply $\mathsf{L}\mathsf{P}\mathsf{A}\mathsf{V}$ at each iteration to find the best *Lipschitz* monotonic function to the data, while they apply the $\mathsf{P}\mathsf{A}\mathsf{V}$ (Pool Adjacent Violator) procedure to fit a monotonic (generally non-Lipschitz) function. The second difference is the theoretical guarantees, which in the case of Isotron required working with a fresh training sample at each iteration.

<!-- chunk {"id": "body-0027", "role": "body", "section": "L-Isotron vs Isotron", "weight": 1.0} -->

While the first difference is inherent, the second difference is just an outcome of the analysis. In particular, one might still try and apply the Isotron algorithm, using the same training sample at each iteration. While we do not have theoretical guarantees for this algorithm, it is computationally efficient, and one might wonder how well it performs in practice. As we see later, it actually performs quite well on the datasets we examined. However, in this subsection we provide a simple example, which shows that sometimes, the repeated fitting of a *non*-Lipschitz function, as done in the Isotron algorithm, can cause overfit and thus hurt performance, compared to fitting a Lipschitz function as done in the L-Isotron algorithm.

<!-- chunk {"id": "body-0028", "role": "body", "section": "L-Isotron vs Isotron", "weight": 1.0} -->

We constructed a synthetic dataset as follows: In a high dimensional space $({d = 400})$, we let $w = {(1,0,\ldots,0)}$ be the true direction. The transfer function is ${u{(t)}} = {{({1 + t})}/2}$. Each data point $x$ is constructed as follows: the first coordinate is chosen uniformly from the set $\{{- 1},0,1\}$, and out of the remaining coordinates, one is chosen uniformly at random and is set to $1$. All other coordinates are set to $0$. The $y$ values are chosen at random from $\{ 0,1\}$, so that ${{\mathbb{E}}{\lbrack\left. y \middle| x \right.\rbrack}} = {u{({w \cdot x})}}$. We used a sample of size $600$ to evaluate the performance of the algorithms.

<!-- chunk {"id": "body-0029", "role": "body", "section": "L-Isotron vs Isotron", "weight": 1.0} -->

In the synthetic example we construct, the first attribute is the only relevant attribute. However, because of the random noise in the $y$ values, Isotron tends to overfit using the irrelevant attributes. At data points where the true mean value $u{({w \cdot x})}$ equals $0.5$, Isotron (which uses $\mathsf{P}\mathsf{A}\mathsf{V}$) tries to fit the value $0$ or $1$, whichever is observed. On the other hand, L-Isotron (which uses $\mathsf{L}\mathsf{P}\mathsf{A}\mathsf{V}$) predicts this correctly as close to $0.5$, because of the Lipschitz constraint. Figure 1 shows the link functions predicted by L-Isotron and Isotron on this dataset.

<!-- chunk {"id": "body-0030", "role": "body", "section": "L-Isotron vs Isotron", "weight": 1.0} -->

Repeating the experiment $10$ times, the error of L-Isotron, normalized by the variance of the $y$ values, was $0.338 \pm 0.058$, while the normalized error for the Isotron algorithm was $0.526 \pm 0.175$. In addition, we observed that L-Isotron performed better rather consistently across the folds - the difference between the normalized error of Isotron and L-Isotron was $0.189 \pm 0.139$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "L-Isotron vs Isotron", "weight": 1.0} -->

{\text{(a)~}\text{concrete}\ } & {\text{(b)~}\text{communities}} Figure 2: The transfer function u as predicted by L-Isotron (blue) and Isotron (red) for the concrete and communities datasets. The domain of both functions was normalized to [−1, 1].

<!-- chunk {"id": "body-0032", "role": "body", "section": "Real World Datasets", "weight": 1.0} -->

We now turn to describe the results of experiments performed on several UCI datasets. We chose the following 5 datasets: communities, concrete, housing, parkinsons, and wine-quality.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Real World Datasets", "weight": 1.0} -->

On each dataset, we compared the performance of L-Isotron (L-Iso) and GLM-tron (GLM-t) with Isotron and several other algorithms. These include standard logistic regression (Log-R), linear regression (Lin-R) and a simple heuristic algorithm (SIM) for single index models, along the lines of standard iterative maximum-likelihood procedures for these types of problems (e.g., ). The algorithm works by iteratively fixing the direction $w$ and finding the best transfer function $u$, and then fixing $u$ and optimizing $w$ via gradient descent. For each of the algorithms we performed 10-fold cross validation, using $1$ fold each time as the test set, and we report averaged results across the folds.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Real World Datasets", "weight": 1.0} -->

Table 1 shows the mean squared error of all the algorithms across ten folds normalized by the variance in the $y$ values. Table 2 shows the difference between squared errors between the algorithms across the folds. The results indicate that the performance of L-Isotron and GLM-tron (and even Isotron) is comparable to other regression techniques and in many cases also slightly better. This suggests that these algorithms should work well in practice, while enjoying non-trivial theoretical guarantees.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Real World Datasets", "weight": 1.0} -->

It is also illustrative to see how the transfer functions found by the two algorithms, L-Isotron and Isotron, compare to each other. In Figure 2, we plot the transfer function for concrete and communities. The plots illustrate the fact that Isotron repeatedly fits a non-Lipschitz function resulting in a piecewise constant function, which is less intuitive than the smoother, Lipschitz transfer function found by the L-Isotron algorithm.
