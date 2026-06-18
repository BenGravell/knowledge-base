<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Modified Gauss-Newton Algorithms under Noise

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Gauss-Newton methods and their stochastic version have been widely used in machine learning and signal processing. Their nonsmooth counterparts, modified Gauss-Newton or prox-linear algorithms, can lead to contrasting outcomes when compared to gradient descent in large-scale statistical settings. We explore the contrasting performance of these two classes of algorithms in theory on a stylized statistical example, and experimentally on learning problems including structured prediction. In theory, we delineate the regime where the quadratic convergence of the modified Gauss-Newton method is active under statistical noise. In the experiments, we underline the versatility of stochastic (sub)-gradient descent to minimize nonsmooth composite objectives.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Arising from the literature on non-linear least squares, the Gauss-Newton method was proposed to tackle generic compositional problems of the form ${\min_{w \in {\mathbb{R}}^{d}}f}{({\phi{(w)}})}$ by linearizing the inner function $\phi$ around the current iterate and solving the resulting subproblem.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Gauss-Newton method and its variants such as the Levenberg-Marquardt method have been applied successfully in phase retrieval, nonlinear control, and non-negative matrix factorization. Modern machine learning problems such as deep learning possess a similar compositional structure, which makes Gauss-Newton-like algorithms potential good candidates. However, in such problems, we are often interested in the generalization performance on unseen data. It is unclear whether the additional cost of solving the subproblems can be amortized by the superior efficiency of Gauss-Newton-like algorithms.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we investigate whether modified Gauss-Newton methods or prox-linear algorithms with incremental gradient inner loops are superior to direct stochastic subgradient algorithms for nonsmooth problems with a compositional objective and a finite-sum structure in terms of generalization error. We present a statistical example and quantify when the quadratic convergence of the exact prox-linear method is not active before hitting the noise level of the problem. We present synthetic experiments that delineate the regimes where the stochastic subgradient methods outperform the prox-linear method. We also compare these algorithms on a structured prediction problem with a convolutional neural network (end-to-end path planning). Experimental results suggest that modified Gauss-Newton methods or prox-linear algorithms offer marginal gains in some settings, and confirm the versatility of direct stochastic subgradient algorithms to tackle complex learning problems. All proofs are given in the appendix.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Problem Setting and Optimization Algorithms", "weight": 1.0} -->

For *multi-output regression* of input $x_{i} \in {\mathbb{R}}^{p}$ to output $y_{i} \in {\mathbb{R}}^{k}$, we take ${\phi_{i}{(w)}} = {{\varphi{(x_{i};w)}} - y_{i}}$ as the residual of a predictor $\varphi{( \cdot;w)}$. We take a nonsmooth loss function such as ${f{(u)}} = {\| u\|}_{2}$ ($\ell_{2}$ loss without the square), which is applicable in robust regression problems. A more sophisticated example is *structured prediction*, the prediction of a combinatorial object such as a sequence. Here, $\phi_{i}{(w)}$ is a score for each structured output, and $f$ is the structural hinge loss, computed efficiently using dynamic programming. For applications, see, e.g.,.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem Setting and Optimization Algorithms", "weight": 1.0} -->

We compare two families of optimization algorithms, which are stochastic and nonsmooth versions of gradient descent and the Gauss-Newton algorithm. The stochastic subgradient method (abbreviated SGD) is the nonsmooth and stochastic analogue of gradient descent.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Setting and Optimization Algorithms", "weight": 1.0} -->

In deep learning, the subgradient $v \in {\partial{({{f \circ \phi_{i}}{(w)}})}}$ requires the computation of the vector-Jacobian product, readily given by reverse-mode automatic differentiation implemented in software such as PyTorch.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Setting and Optimization Algorithms", "weight": 1.0} -->

The modified Gauss-Newton method, also known as the prox-linear method, applied to, proceeds by finding approximate solutions of a partially linearized approximation of the objective with an additional regularization term. Given a regularization parameter $\kappa \geq 0$, it iterates

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Setting and Optimization Algorithms", "weight": 1.0} -->

As explained in Fig. 1 (left), the prox-linear method creates a convex model of $F$ around $w_{t}$ by linearizing the inner function as ${\phi_{i}{(w)}} \approx {{\phi_{i}{(w_{t})}} + {{\nabla\phi_{i}}{(w_{t})}^{\top}{({w - w_{t}})}}}$. The next iterate is the minimizer of the model plus a proximal term. Compare this with the subgradient method, where the model is ${F{(w_{t})}} + {v^{\top}{({w - w_{t}})}}$, for $v \in {\partial{F{(w_{t})}}}$; see also Fig. 1 (right). It is usually not possible to solve the subproblem exactly (barring some special cases). We consider using accelerated incremental algorithms such as Casimir-SVRG.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Setting and Optimization Algorithms", "weight": 1.0} -->

Computationally, each iteration of the inner loop requires having access to Jacobian-vector product $v\mapsto{{\nabla\phi_{i}}{(w)}v}$ which is most efficiently computed via forward-mode automatic differentiation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Tradeoffs of the Prox-linear Method in Statistical Settings", "weight": 1.0} -->

Gauss-Newton methods and their variants are known to enjoy quadratic local convergence, provided *the subproblems are solved exactly*. In statistical learning problems, it is not meaningful to optimize beyond the noise level of the problem. If the noise level of the problem is large, the quadratic convergence may not be useful. We formalize this in a stylized example.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Tradeoffs of the Prox-linear Method in Statistical Settings", "weight": 1.0} -->

We start with a typical quadratic local convergence result of the prox-linear method in the overparameterized regime $d > {nk}$. In particular, we assume that the minimal singular value $\sigma_{\min}{({{\nabla\phi}{(w)}^{\top}})}$ of the transposed Jacobian of $\phi = {(\phi_{1};\cdots;\phi_{n})}$ is strictly positive, which implies that the Jacobian $\nabla\phi$ is surjective.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Experiments", "weight": 1.0} -->

We consider 3 setups: multi-output regression, structured prediction, and solving non-linear equations. All hyper-parameters are tuned by grid search.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Experiments", "weight": 1.0} -->

Synthetic Multi-output Regression. We consider a regression task of predicting output $y \in {\mathbb{R}}^{k}$ from input $x \in {\mathbb{R}}^{p}$, given a synthetic dataset ${\{{(x_{i},y_{i})}\}}_{i = 1}^{n}$ of input-output pairs of varying size $n$ where $p = 128$ and $k = 10$. We sample each input as $x_{i} \sim {\mathcal{N}{(0,\Sigma)}}$, where the covariance $\Sigma$ exhibits a $1/j^{2}$ spectral decay.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Experiments", "weight": 1.0} -->

The output is generated as $y_{i} = {{\varphi^{\star}{(x_{i};w^{\star})}} + {\sigma\xi_{i}}}$, where $\varphi^{\star}{( \cdot;w^{\star})}$ is a multilayer perceptron (MLP) with one hidden layer of width $256$, and standard normal weights $w^{\star}$, while $\xi_{i}$ is sampled from a standard Laplace distribution in ${\mathbb{R}}^{k}$ and $\sigma$ is the noise scale, which we vary. We define the signal-to-noise ratio (SNR) of a problem instance as $\text{SNR} = {{\| w^{\star}\|}^{2}/\sigma^{2}}$. Finally, the loss and evaluation measure we use is the nonsmooth $\ell_{2}$ loss.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Experiments", "weight": 1.0} -->

We vary the number of samples $n$ and the SNR (equivalently, $\sigma$) and compare the two methods introduced in Sec. 2: the stochastic subgradient method (SGD) and prox-linear with incremental gradient inner loop (PLI). We tune hyperparameters to achieve the smallest loss on a held-out validation dataset in $100$ epochs and report the test loss. We run the experiment in two regimes: (a) under-parameterized, where the model is an MLP with $64$ hidden units, and, (b) over-parameterized, where the MLP has $512$ hidden units, compared to the $256$ hidden units of $\varphi^{\star}{( \cdot;w^{\star})}$. We see in Fig. 2 that SGD tends to outperform PLI overall, especially in the high SNR regime. In the low SNR regime, PLI and SGD are mostly tied in their performance, exhibiting very similar test errors.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Experiments", "weight": 1.0} -->

Path Planning as Structured Prediction. Among all monotonic paths from the top left corner to the bottom right corner of a grid, our task is to find the path that maximizes the rewards collected on each tile it passes through. Specifically, we consider images generated in the game Warcraft II; see Fig. 3. Each tile corresponds to some terrain such as water, desert, grass, or rock with a fixed reward (grass $>$ desert $>$ water $>$ rock). As long as the rewards can directly be observed, this task can be solved by dynamic programming. In this experiment, the rewards are not directly observed; they are computed as the transformation of the raw pixels of each tile by a convolutional neural network. Our goal is to learn the reward function from a dataset of random maps with their associated optimal path. Given a map $x$ with associated best path $y$, denote by $\psi{(x,y,y^{\prime};w)}$ the score of a path $y^{\prime}$ parameterized by $w$. Our objective is

<!-- chunk {"id": "body-0019", "role": "body", "section": "Experiments", "weight": 1.0} -->

The methods we consider are (i) stochastic subgradient methods, denoted SGD, with various learning rates strategies $\gamma_{t} = \gamma_{0}$, $\gamma_{t} = {\gamma_{0}/\sqrt{t}}$ and $\gamma_{t} = {\gamma_{0}/t}$, (ii) a variance-reduced stochastic sub-gradient method, denoted SVRG, (iii) an accelerated algorithm on the Moreau-envelope of the objective as described, denoted Casimir-SVRG, (iv) a prox-linear algorithm with incremental inner loop as described, denoted PLI. For SGD, subgradients of can be computed by estimating the highest reward path $y^{\prime}$ associated with a given sample $(x_{i},y_{i})$ for a feature map parameterized by the current parameters $w$. Both Casimir-SVRG and PL are implemented by smoothing the objective.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Experiments", "weight": 1.0} -->

We take inf-convolution of the max by a squared $\ell_{2}$ norm, which can be approximated by returning the top-$K$ shortest paths for the given score function.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experiments", "weight": 1.0} -->

In Fig. 4, we observe that SGD with constant step-size carefully tuned can perform as well as more sophisticated methods such as the modified Gauss-Newton method. Most importantly, for a small regularization parameter ($\mu = {10^{- 4}/n}$), SGD yields the best test Hamming loss, which in this task is the target metric.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experiments", "weight": 1.0} -->

Solving Non-linear Equations. Gauss-Newton-type methods can be applied to stochastic non-linear equations of the form

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experiments", "weight": 1.0} -->

where $f$ is a convex, possibly nonsmooth, Lipschitz function such as $\parallel \cdot \parallel_{1}$ and the inner mappings are smooth and typically of the form ${\phi_{i}{(w)}} = {{\varphi{(x_{i},w)}} - y_{i}}$. Problem can be interpreted as ensuring that, on average, the non-linear mapping $\varphi{( \cdot,w)}$ maps the inputs $x_{i}$ to the targets $y_{i}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experiments", "weight": 1.0} -->

where $\hat{\nabla}\phi{(w)}$ and $\hat{\phi}{(w)}$ are approximations of ${\nabla\phi}{(w)}$ and $\phi{(w)}$ respectively that can be approximated from a mini-batch; we call this "SGD". Note that the minibatch subgradient estimates can be biased since the outer function $f$ can be non-linear. A modified Gauss-Newton or prox-linear method adapted to the inner finite sum performs the iterations

<!-- chunk {"id": "body-0025", "role": "body", "section": "Experiments", "weight": 1.0} -->

where each sub-problem can be solved by incremental algorithms such as the accelerated dual proximal gradient ascent.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

Experiment. We consider the experimental setting of. The objective is to solve where $f$ is the Huber loss, a smooth surrogate of the nonsmooth $\ell_{1}$ norm, and inner mappings $\phi$ are the concatenation of four different losses, i.e., ${\phi_{i}{(w)}} = {({\ell_{1}{({x_{i}^{\top}w},y_{i})}},\ldots,{\ell_{4}{({x_{i}^{\top}w},y_{i})}})}$, where the formulations of the losses can be found. The samples $(x_{i},y_{i})$ are drawn from the datasets ijcnn1 or covtype from the LIBSVM repository.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

We consider (i) a gradient descent denoted GD, (ii) a modified Gauss-Newton or prox-linear method denoted PL, (iii) a baseline of the form, denoted SGD, (iv) an incremental Gauss-Newton or prox-linear method as described, denoted PLI for consistency. In Fig. 5, we observe that PL outperforms GD as expected in the batch setting. However, this advantage is no longer present in the incremental setting. Here, we find that the SGD baseline performs on par with the Gauss-Newton variant PLI.
