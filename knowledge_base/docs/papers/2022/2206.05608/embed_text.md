## Introduction

Gradient boosting is a classic machine learning algorithm successfully used for web search, recommendation systems, weather forecasting, and other problems. In a nutshell, gradient boosting methods iteratively combine simple models (usually decision trees), minimizing a given loss function. Despite the recent success of neural approaches in various areas, gradient-boosted decision trees (GBDT) are still state-of-the-art algorithms for *tabular* datasets containing heterogeneous features.

This paper aims at a better theoretical understanding of GBDT methods for regression problems assuming the widely used RMSE loss function. First, we show that the gradient boosting with regularization can be reformulated as an optimization problem in some Reproducing Kernel Hilbert Space (RKHS) with implicitly defined kernel structure. After obtaining that connection between GBDT and kernel methods, we introduce a technique for sampling from prior Gaussian process distribution with the same kernel that defines RKHS so that the final output would converge to a sample from the Gaussian process posterior. Without this technique, we can view the output of GBDT as the mean function of the Gaussian process.

Importantly, our theoretical analysis assumes the regularized gradient boosting procedure (Algorithm 2) without any simplifications --- we only need decision trees to be symmetric (oblivious) and properly randomized (Algorithm 1). These assumptions are non-restrictive and are satisfied in some popular gradient boosting implementations, e.g., CatBoost.

Our experiments confirm that the proposed sampler from the Gaussian process posterior outperforms the previous approaches and gives better knowledge uncertainty estimates and improved out-of-domain detection.

## Background

Assume that we are given a distribution $\varrho$ over $X \times Y$, where $X \subset {\mathbb{R}}^{d}$ is called a feature space and $Y \subset {\mathbb{R}}$ --- a target space. Further assume that we are given a dataset $\mathbf{z} = {\{{(x_{i},y_{i})}\}}_{i = 1}^{N} \subset {X \times Y}$ of size $N \geq 1$ sampled i.i.d. from $\varrho$. Let us denote by ${\rho{({dx})}} = {\int_{Y}{{d\varrho}{({dx},{dy})}}}$. W.l.o.g., we also assume that $X = {{supp}\rho} = \overline{\left\{ {x\in{\mathbb{R}}^{d}}:{{{\forall\epsilon}>0},{{\rho{({\{{x^{\prime}\in{\mathbb{R}}^{d}}:{{\|{x-x^{\prime}}\|}_{{\mathbb{R}}^{d}}<\epsilon}\}})}}>0}} \right\}}$ which is a closed subset of ${\mathbb{R}}^{d}$. Moreover, for technical reasons, we assume that ${\frac{1}{2N}{\sum_{i = 1}^{N}y_{i}^{2}}} \leq R^{2}$ for some constant $R > 0$ almost surely, which can always be enforced by clipping. Throughout the paper, we also denote by $\mathbf{x}_{N}$ and $\mathbf{y}_{N}$ the matrix of all feature vectors and the vector of targets.

### Gradient boosted decision trees

Given a loss function $L:{{\mathbb{R}}^{2}\rightarrow{\mathbb{R}}}$, a classic gradient boosting algorithm iteratively combines weak learners (usually decision trees) to reduce the average loss over the train set $\mathbf{z}$: ${\mathcal{L}{(f)}} = {{\mathbb{E}}_{\mathbf{z}}{\lbrack{L{({f{(x)}},y)}}\rbrack}}$. At each iteration $\tau$, the model is updated as: ${f_{\tau}{(x)}} = {{f_{\tau - 1}{(x)}} + {\epsilonw_{\tau}{(x)}}}$, where ${w_{\tau}{(\cdot)}} \in \mathcal{W}$ is a weak learner chosen from some family of functions $\mathcal{W}$, and $\epsilon$ is a learning rate. The weak learner $w_{\tau}$ is usually chosen to approximate the negative gradient of the loss function ${- {g_{\tau}{(x,y)}}}:={- \left. \frac{\partial{L{(s,y)}}}{\partial s} \right|_{s = {f_{\tau - 1}{(x)}}}}$: The family $\mathcal{W}$ usually consists of decision trees. In this case, the algorithm is called GBDT (Gradient Boosted Decision Trees). A decision tree is a model that recursively partitions the feature space into disjoint regions called leaves. Each leaf $R_{j}$ of the tree is assigned to a value, which is the estimated response $y$ in the corresponding region. Thus, we can write ${w{(x)}} = {\sum_{j = 1}^{d}{\theta_{j}\mathbf{1}_{\{{x \in R_{j}}\}}}}$, so the decision tree is a linear function of the leaf values $\theta_{j}$.

A recent paper Ustimenko & Prokhorenkova proposes a modification of classic stochastic gradient boosting (SGB) called *Stochastic Gradient Langevin Boosting* (SGLB). SGLB combines gradient boosting with stochastic gradient Langevin dynamics to achieve global convergence even for non-convex loss functions. As a result, the obtained algorithm provably converges to some stationary distribution (invariant measure) concentrated near the global optimum of the loss function. We mention this method because it samples from similar distribution as our method but with a different kernel.

### Estimating uncertainty

In addition to the predictive quality, it is often important to detect when the system is uncertain and can be mistaken. For this, different measures of *uncertainty* can be used. There are two main sources of uncertainty: *data uncertainty* (a.k.a. aleatoric uncertainty) and *knowledge uncertainty* (a.k.a. epistemic uncertainty). Data uncertainty arises due to the inherent complexity of the data, such as additive noise or overlapping classes. For instance, if the target is distributed as $\left. y \middle| x \right. \sim {\mathcal{N}{({f{(x)}},{\sigma^{2}{(x)}})}}$, then $\sigma{(x)}$ reflects the level of data uncertainty. This uncertainty can be assessed if the model is probabilistic.

Knowledge uncertainty arises when the model gets input from a region either sparsely covered by or far from the training data. Since the model does not have enough data in this region, it will likely make a mistake. A standard approach to estimating knowledge uncertainty is based on *ensembles*. Assume that we have trained an ensemble of several independent models. If all the models understand an input (low knowledge uncertainty), they will give similar predictions. However, for out-of-domain examples (high knowledge uncertainty), the models are likely to provide diverse predictions. For regression tasks, one can obtain knowledge uncertainty by measuring the variance of the predictions provided by multiple models.

Such ensemble-based approaches are standard for neural networks. Recently, ensembles were also tested for GBDT models. The authors consider two ways of generating ensembles: ensembles of independent SGB models and ensembles of independent SGLB models. While empirically methods are very similar, SGLB has better theoretical properties: the convergence of parameters to the stationary distribution allows one to sample models from a particular posterior distribution. One drawback of SGLB is that its convergence rate is unknown, as the proof is asymptotic. However, the convergence rate can be upper bounded by that of Stochastic Gradient Langevin Dynamics for log-concave functions, e.g., Zou et al., which is not dimension-free. In contrast, our rate is dimension-free and scales linearly with inverse precision.

### Gaussian process inference

In this section, we briefly describe the basics of Bayesian inference with Gaussian processes that is closely related to our analysis. A random variable $f$ with values in $L_{2}{(\rho)}$ is said to be a Gaussian process $f \sim {\mathcal{G}\mathcal{P}\left(f_{0},{{\sigma^{2}\mathcal{K}} + {\delta^{2}{Id}_{L_{2}}}} \right)}$ with covariance defined via a kernel ${\mathcal{K}{(x,x')}} = {{cov}\left({f{(x)}},{f{(x')}} \right)}$ and mean value $f_{0} \in {L_{2}{(\rho)}}$ iff ${\forall g} \in {L_{2}{(\rho)}}$ we have A typical Gaussian Process setup is to assume that the target $\left. y \middle| x \right.$ is distributed as $\mathcal{G}\mathcal{P}\left(\mathbb{0}_{L_{2}{(\rho)}},{{\sigma^{2}\mathcal{K}} + {\delta^{2}{Id}_{L_{2}}}} \right)$ for some kernel function^11^1$\mathcal{K}{(x,x')}$ is a kernel function if $\left\lbrack {\mathcal{K}{(x_{i},x_{j})}} \right\rbrack_{{i = 1},{j = 1}}^{N,N} \geq 0$ for any $N \geq 1$ and any $x_{i} \in X$ almost surely. $\mathcal{K}{(x,x')}$ with scales $\sigma > 0$ and $\delta > 0$: The posterior distribution $\left. {f{(x)}} \middle| {x,\mathbf{x}_{N},\mathbf{y}_{N}} \right.$ is again a Gaussian Process $\mathcal{G}\mathcal{P}{(f_{\ast},{{\sigma^{2}\overset{\sim}{\mathcal{K}}} + {\delta^{2}{Id}_{L_{2}}}})}$ with mean and covariance given by (see Rasmussen & Williams): with $\lambda = \frac{\delta^{2}}{\sigma^{2}}$. To estimate the posterior mean ${f_{\ast}^{\lambda}{(x)}} = {\int_{\mathbb{R}}{fp{(\left. f \middle| {x,\mathbf{x}_{N},\mathbf{y}_{N}} \right.)}{df}}}$, we can use the maximum a posteriori probability estimate (MAP) --- the only solution for the following Kernel Ridge Regression (KRR) problem: where $\mathcal{H} = \overline{{span}\left\{ {\mathcal{K}{(\cdot,x)}} \middle| {x\in X} \right\}} \subset {L_{2}{(\rho)}}$ is the reproducing kernel Hilbert space (RKHS) for the kernel $\mathcal{K}{(\cdot, \cdot)}$ and ${L{(f)}}\rightarrow\min_{f \in \mathcal{H}}$ means that we are seeking minimizers of this function $L{(f)}$. We refer to Appendix D for the details on KRR and RKHS.

To solve the KRR problem, one can apply the gradient descent (GD) method in the functional space: where $\epsilon > 0$ is a learning rate.

Since this objective is strongly convex due to the regularization, the gradient descent rapidly converges to the unique optimum: see Appendices C and E for the details.

Gradient descent guides $f_{\tau}$ to the posterior mean $f_{\ast}^{\lambda}$ of the Gaussian Process with kernel ${\sigma^{2}\mathcal{K}} + {\delta^{2}{Id}_{L_{2}}}$. To obtain the posterior variance estimate $\overset{\sim}{\mathcal{K}}{(x,x)}$ for any $x$, one can use sampling and introduce a source of randomness in the above iterative scheme as follows: This method is known as Sample-then-Optimize and is widely adopted for Bayesian inference. As $\tau\rightarrow\infty$, we get $f^{init} + f_{\infty}$ distributed as a Gaussian Process posterior with the desired mean and variance. Formally, the following result holds:

### Lemma 2.1

$f^{init} + f_{\infty}$ follows the Gaussian Process posterior $\mathcal{G}\mathcal{P}{(f_{\ast}^{\lambda},{{\sigma^{2}\overset{\sim}{\mathcal{K}}} + {\delta^{2}{Id}_{L_{2}}}})}$ :

## Evolution of GBDT in RKHS

### Preliminaries

In our analysis, we assume that we are given a finite set $\mathcal{V}$ of weak learners used for the gradient boosting.^22^2The finiteness of $\mathcal{V}$ is important for our analysis, and it usually holds in practice, see Section 3.2. Each $\nu$ corresponds to a decision tree that defines a partition of the feature space into disjoint regions (leaves). For each $\nu \in \mathcal{V}$, we denote the number of leaves in the tree by $L_{\nu} \geq 1$. Also, let $\phi_{\nu}:{X\rightarrow{\{ 0,1\}}^{L_{\nu}}}$ be a mapping that maps $x$ to the vector indicating its leaf index in the tree $\nu$. This mapping defines a decomposition of $X$ into the disjoint union: $X = {\cup_{j = 1}^{L_{\nu}}\left\{ {x \in X} \middle| {{\phi_{\nu}^{(j)}{(x)}} = 1} \right\}}$. Having $\phi_{\nu}$, we define a weak learner associated with it as $x\mapsto{\langle\theta,{\phi_{\nu}{(x)}}\rangle}_{{\mathbb{R}}^{L_{\nu}}}$ for any choice of $\theta \in {\mathbb{R}}^{L_{\nu}}$ which we refer to as 'leaf values'. In other words, $\theta$ corresponds to predictions assigned to each region of the space defined by $\nu$.

Let us define a linear space $\mathcal{F} \subset {L_{2}{(\rho)}}$ of all possible ensembles of trees from $\mathcal{V}$: We note that the space $\mathcal{F}$ can be data-dependent since $\mathcal{V}$ may depend on $\mathbf{z}$, but we omit this dependence in the notation for simplicity. Note that we do not take the closure w.r.t. the topology of $L_{2}{(\rho)}$ since we assume that $\mathcal{V}$ is finite and therefore $\mathcal{F}$ is finite-dimensional and thus topologically closed.

### GBDT algorithm under consideration

Our theoretical analysis holds for classic GBDT algorithms discussed in Section 2.1 equipped with regularization from Ustimenko & Prokhorenkova. The only requirement we need is that the procedure of choosing each new tree has to be properly randomized. Let us discuss a tree selection algorithm that we assume in our analysis.

Each new tree approximates the gradients of the loss function with respect to the current predictions of the model. Since we consider the RMSE loss function, the gradients are proportional to the residuals $r_{j} = {y_{j} - {f{(x_{j})}}}$, where $f$ is the currently built model. The tree structure is defined by the features and the corresponding thresholds used to split the space. The analysis in this paper assumes the *SampleTree* procedure (see Algorithm 1), which is a classic approach equipped with proper randomization. *SampleTree* builds an *oblivious* decision tree, i.e., all nodes at a given level share the same splitting criterion (feature and threshold).^33^3In fact, the procedure can be extended to arbitrary trees, but this would over-complicate formulation of the algorithm and would not change the space of tree ensembles as any non-symmetric tree can be represented as a sum of symmetric ones. To limit the number of candidate splits, each feature is quantized into $n + 1$ bins. In other words, for each feature, we have $n$ thresholds that can be chosen arbitrarily.^44^4A standard approach is to quantize the feature such that all $n + 1$ buckets have approximately the same number of training samples. The maximum tree depth is limited by $m$. Recall that we denote the set of all possible tree structures by $\mathcal{V}$.

We build the tree in a top-down greedy manner. At each step, we choose one split among all the remaining candidates based on the following *score* defined for $\nu \in \mathcal{V}$ and residuals $r$: output: oblivious tree structure ν ∈ 𝒱 hyper-parameters: number of feature splits n, max. tree depth m, random strength β ∈ [0, ∞) 𝒮 = {(j, k)|j ∈ {1, …, d}, k ∈ {1, …, n}} — indices of all possible splits choose next split as ${\{ s_{i + 1}\}} = {\underset{s\in\mathcal{S}^{(i)}}{\arg\max}\left({{D\left({(\nu_{i},s)},r \right)} - {\beta{\log{({- {{\log u_{i}}{(s)}}})}}}} \right)}$ update candidate splits: 𝒮(i + 1) = 𝒮(i) ∖ {si + 1} hyper-parameters: learning rate ϵ > 0, regularization λ > 0, iterations of boosting T, parameters of SampleTree m, n, β ντ = SampleTree (rτ; m, n, β) — construct a tree $\theta_{\tau} = \left(\frac{\sum_{i = 1}^{N}{\phi_{\nu_{\tau}}^{(j)}{(x_{i})}r_{\tau}^{(i)}}}{\sum_{i = 1}^{N}{\phi_{\nu_{\tau}}^{(j)}{(x_{i})}}} \right)_{j = 1}^{L_{\nu_{\tau}}}$ — set values in leaves ${f_{\tau + 1}{(\cdot)}} = {{{({1 - \frac{\lambda\epsilon}{N}})}f_{\tau}{(\cdot)}} + {\epsilon\left\langle {\phi_{\nu_{\tau}}{(\cdot)}},\theta_{\tau} \right\rangle_{{\mathbb{R}}^{L_{\nu_{\tau}}}}}}$ — update model In classic gradient boosting, one builds a tree recursively by choosing such split $s$ that maximizes the score $D{({(\nu_{i},s)},r)}$.^55^5Maximizing is equivalent to minimizing the squared error between the residuals and the mean values in the leaves. Random noise is often added to the scores to improve generalization. In *SampleTree*, we choose a split that maximizes Here $\beta$ is random strength: $\beta = 0$ gives the standard greedy approach, while $\beta\rightarrow\infty$ gives the uniform distribution among all possible split candidates.

To sum up, *SampleTree* is a classic oblivious tree construction but with added random noise. We do this to make the distribution of trees regular in a certain sense: roughly speaking, the distributions should stabilize with iterations by converging to some fixed distribution.

Given the algorithm *SampleTree*, we describe the gradient boosting procedure assumed in our analysis in Algorithm 2. It is a classic GBDT algorithm but with the update rule ${f_{\tau + 1}{( \cdot )}} = {{\left( {1 - {{\lambda\epsilon}/N}} \right)f_{\tau}{( \cdot )}} + {\epsilonw_{\tau}{(x)}}}$. In other words, we shrink the model at each iteration, which serves as regularization. Such shrinkage is available, e.g., in the CatBoost library.

### Distribution of trees

The *SampleTree* algorithm induces a local family of distributions $p{( \cdot |f,\beta)}$ for each $f \in \mathcal{F}$:

### Remark 3.1

Lemma D.5 ensure that such distribution coincides with the one where we use $f_{\ast}{(\mathbf{x}_{N})}$ instead of $\mathbf{y}_{N}$. This is due to the fact that ${{D\left( \nu,{\mathbf{y}_{N} - {f{(\mathbf{x}_{N})}}} \right)} = {D\left( \nu,{f_{\ast} - {f{(\mathbf{x}_{N})}}} \right){\forall\nu}} \in \mathcal{V}},{f \in \mathcal{F}}$.

The following lemma describes the distribution $p{(\left. {d\nu} \middle| {f,\beta} \right.)}$, see Appendix F for the proof.

### Lemma 3.2

(Probability of a tree)^66^6Note that for oblivious decision trees, changing the order of splits does not affect the obtained partition. Hence, we assume that each tree is defined by an unordered set of splits. where the sum is over all permutations $\varsigma \in \mathcal{P}_{m}$, $\nu_{\varsigma,i} = {(s_{\varsigma{}},\ldots,s_{\varsigma{(i)}})}$, and $\nu = {(s_{1},\ldots,s_{m})}$.

Let us define the stationary distribution of trees as $\pi{( \cdot )} = \lim_{\beta\rightarrow\infty}p{( \cdot |f,\beta)}$. It follows from Remark 3.1 that we also have $\pi{( \cdot )} = p{( \cdot |f_{\ast},\beta)}$.

### Corollary 3.3

(Stationary distribution is the uniform distribution over tree structures)\We have ${\pi{({d\nu})}} = \left. \left| {d\nu} \right|/\binom{nd}{m} \right.$, where $\binom{nd}{m} = \frac{{({nd})}!}{{{({{nd} - m})}!}{m!}}$.

### RKHS structure

In this section, we describe the evolution of GBDT in a certain Reproducing Kernel Hilbert Space (RKHS). Even though the problem is finite dimensional, treating it as functional regression is more beneficial as dimension of the ensembles space grows rapidly and therefore we want to obtain dimension-free constants which is impossible if we treat it as finite dimensional optimization problem. Let us start with defining necessary kernels. For convenience, we also provide a diagram illustrating the introduced kernels and relations between them in Appendix A.

### Definition 3.4

A weak learner's kernel $k_{\nu}{(\cdot, \cdot)}$ is a kernel function associated with a tree structure $\nu \in \mathcal{V}$ which can be defined as: This weak learner's kernel is a building block for any other possible kernel in boosting and is used to define the iterations of the boosting algorithm analytically.

### Definition 3.5

We also define a *greedy* kernel of the gradient boosting algorithm as follows: This greedy kernel is a kernel that guides the GBDT iterations, i.e., we can think of each iteration as SGD with a kernel from 3.5, and 3.4 is used as a stochastic gradient estimator of the Fréchet derivative in RKHS defined by the kernel from 3.5.

### Definition 3.6

Finally, there is a *stationary* kernel $\mathcal{K}{(x,x')}$ that is independent from $f$: which we call a *prior* kernel of the gradient boosting.

This kernel defines the limiting solution since the gradient projection on RKHS converges to zero, and thus 3.5 converges to 3.6.

Note that $\mathcal{F} = {{span}\left\{ {\mathcal{K}{(\cdot,x)}}\mid{x \in \mathcal{X}} \right\}}$. Having the space of functions $\mathcal{F}$, we define RKHS structure $\mathcal{H} = \left(\mathcal{F},{\langle \cdot, \cdot \rangle}_{\mathcal{H}} \right)$ on it using a scalar product defined as Now, let us define the empirical error of a model $f$: Then, we define ${V{(f,\lambda)}} = {{L{(f,\lambda)}} - {\inf_{f' \in \mathcal{F}}{L{(f',\lambda)}}}}$. Let us also define the following functions: $f_{\ast}^{\lambda} \in {{{\arg\min}_{f \in \mathcal{F}}V}{(f,\lambda)}}$ and It is known that such $f_{\ast}$ exists and is unique since the set of all solutions is convex, and therefore there is a unique minimizer of the norm $\parallel \cdot \parallel_{\mathcal{H}}$. Finally, the following lemma gives the formula of the GBDT iteration in terms of kernels in Lemma 3.7 which will be useful in proving our results. See Appendix D for the proofs.

### Lemma 3.7

Iterations $f_{\tau}$ of Gradient Boosting (Algorithm 2) can be written in the form:

### Kernel Gradient Boosting convergence to KRR

Consider the sequence ${\{ f_{\tau}\}}_{\tau \in {\mathbb{N}}}$ generated by the gradient boosting algorithm. Its evolution is described by Lemma 3.7. The following theorem estimates the expected (w.r.t. the randomness of tree selection) empirical error of $f_{T}$ relative to the best possible ensemble. The full statement of the theorem and its proof can be found in Appendix G.

### Theorem 3.8

Assume that $\beta,T_{1}$ are sufficiently large and $\epsilon$ is sufficiently small (see Appendix G). Then, ${\forall T} \geq T_{1}$,

### Corollary 3.9

(Convergence to the solution of the KRR problem) Under the assumptions of the previous theorem, we have the following dimension-free bound: This bound is dimension-free thanks to functional treatment and exponentially decaying to small value with iterations and therefore justifies the observed rapid convergence of gradient boosting algorithms in practice even though dimension of space $\mathcal{H}$ is enormous.

## Gaussian inference

So far, the main result of the paper proved in Section 3.5 shows that Algorithm 2 solves the Kernel Ridge Regression problem, which can be interpreted as learning Gaussian Process posterior mean $f_{\ast}^{\lambda}$ under the assumption that $f \sim {\mathcal{G}\mathcal{P}{(0,{{\sigma^{2}\mathcal{K}} + {\delta^{2}{Id}_{L_{2}}}})}}$ where $\lambda = \frac{\sigma^{2}}{\delta^{2}}$. I.e., Algorithm 2 does not give us the posterior variance. Still, as mentioned earlier, we can estimate the posterior variance through Monte-Carlo sampling in a sample-then-optimize way. For that, we need to somehow sample from the prior distribution $\mathcal{G}\mathcal{P}{(0,{{\sigma^{2}\mathcal{K}} + {\delta^{2}{Id}_{L_{2}}}})}$.

### Prior sampling

We introduce Algorithm 3 for sampling from the prior distribution. *SamplePrior* generates an ensemble of random trees (with random splits and random values in leaves). Note that while being random, the tree structure depends on the dataset features $\mathbf{x}_{N}$ since candidate splits are based on $\mathbf{x}_{N}$.

We first note that the process $h_{T}{(\cdot)}$ is centered with covariance operator $\mathcal{K}$: | | ${\mathbb{E}}h_{T}{(x)}h_{T}{(y)}$ | ${{= {\mathcal{K}{(x,y)}{\forall x}}},{y \in X}}.$ | | | Then, we show that $h_{T}{(\cdot)}$ converges to the Gaussian Process in the limit.

### Lemma 4.1

The following convergence holds almost surely in $x \in X$: hyper-parameters: number of iterations T, parameters of SampleTree m, n ντ = SampleTree (𝟘ℝN; m, n, 1) — sample random tree $\theta_{\tau} \sim \mathcal{N}\left(\mathbb{0}_{{\mathbb{R}}^{L_{\nu_{\tau}}}},{diag}\left(\frac{N}{\max{\{ N_{\nu_{\tau}}^{(j)},1\}}}:j \in {\{ 1,\ldots,L_{\nu_{\tau}}\}} \right) \right)$ — generate random values in leaves ${h_{\tau + 1}{(\cdot)}} = {{h_{\tau}{(\cdot)}} + {\frac{1}{\sqrt{T}}\left\langle {\phi_{\nu_{\tau}}{(\cdot)}},\theta_{\tau} \right\rangle_{{\mathbb{R}}^{L_{\nu_{\tau}}}}}}$ — update model

### Posterior sampling

Now we are ready to introduce Algorithm 4 for sampling from the posterior. The procedure is simple: we first perform $T_{0}$ iterations of SamplePrior to obtain a function $h_{T_{0}}{( \cdot )}$ and then we train a standard GBDT model $f_{T_{1}}{( \cdot )}$ approximating ${\mathbf{y}_{N} - {\sigmah_{T_{0}}{(\mathbf{x}_{N})}}} + {\mathcal{N}{(\mathbb{0}_{N},{\delta^{2}I_{N}})}}$. Our final model is ${\sigmah_{T_{0}}{( \cdot )}} + {f_{T_{1}}{( \cdot )}}$.

We further refer to this procedure as *SamplePosterior* or *KGB* (Kernel Gradient Boosting) for brevity. Denote | | {{{h_{\infty} = {\lim\limits_{T_{0}\rightarrow\infty}h_{T_{0}}}},{f_{\infty} = {\lim f_{T_{1}}}}},} | | where the first limit is with respect to the point-wise convergence of stochastic processes and the second one with respect to $L_{2}{(\rho)}$ convergence.

The following theorem shows that KGB indeed samples from the desired posterior. The proof directly follows from Lemmas 4.1 and 2.1. hyper-parameters: learning rate ϵ > 0, boosting iteration T1, SamplePrior iterations T0, parameters of SampleTree m, n, β, kernel scale σ > 0 (default σ = 1), noise scale δ > 0 (default: δ = 0.01) ${f_{T_{1}}{(\cdot)}} = {{TrainGBDT}\left({(\mathbf{x}_{N},\mathbf{y}_{N}^{new})};\epsilon,T_{1},m,n,\beta,\frac{\delta^{2}}{\sigma^{2}} \right)}$

### Theorem 4.2

In the limit, the output of Algorithm 4 follows the Gaussian process posterior: with mean ${\overset{\sim}{f}{(x)}} = {\mathcal{K}{(x,\mathbf{x}_{N})}\left({{\mathcal{K}{(\mathbf{x}_{N},\mathbf{x}_{N})}} + {\lambdaI_{N}}} \right)^{- 1}\mathbf{y}_{N}}$ and covariance ${{\overset{\sim}{\mathcal{K}}{(x,x)}} = {\delta^{2} + {\sigma^{2}\left({{\mathcal{K}{(x,x)}} - {\mathcal{K}{(x,\mathbf{x}_{N})}\left({{\mathcal{K}{(\mathbf{x}_{N},\mathbf{x}_{N})}} + {\lambdaI_{N}}} \right)^{- 1}\mathcal{K}{(\mathbf{x}_{N},x)}}} \right)}}}.$

## Experiments

This section empirically evaluates the proposed KGB algorithm and shows that it indeed allows for better knowledge uncertainty estimates.

### Synthetic experiment

To illustrate the KGB algorithm in a controllable setting, we first conduct a synthetic experiment. For this, we defined the feature distribution as uniform over $D = {\{{{(x,y)} \in {\lbrack 0,1\rbrack}^{2}}:{\frac{1}{10} \leq {{({x - \frac{1}{2}})}^{2} - {({y - \frac{1}{2}})}^{2}} \leq {\frac{1}{4} \land {({x \leq {\frac{2}{5} \vee x} \geq \frac{3}{5}})} \land {({y \leq {\frac{2}{5} \vee y} \geq \frac{3}{5}})}}}\}}$. We sample 10K points from $U{({\lbrack 0,1\rbrack}^{2})}$ and take into the train set only those that fall into $D$. The target is defined as ${f{(x,y)}} = {x + y}$. Figure 1(a) illustrates the training dataset colored with the target values. For evaluation, we take the same 10K points without restricting them to $D$.

For KGB, we fix $\epsilon = 0.3$, $T_{0} = 100$, $T_{1} = 900$, $\sigma = 10^{- 2}$, $\delta = 10^{- 4}$ $\beta = 0.1$, $m = 4$, $n = 64$, and sampled $100$ KGB models. Figure 1(b) shows the estimated by Monte-Carlo posterior mean $\overset{\sim}{\mu}$. On Figure 1(c), we show $\log\overset{\sim}{\sigma}$, where ${\overset{\sim}{\sigma}}^{2}$ is the posterior variance estimated by Monte-Carlo. One can see that the posterior variance is small in-domain and grows when we move outside the dataset $D$, as desired.

(c) $\log\overset{\sim}{\sigma}$ Figure 1: KGB on a synthetic dataset.

### Experiment on real datasets

Uncertainty estimates for GBDTs have been previously analyzed by Malinin et al.. Our experiments on real datasets closely follow their setup, and we compare the proposed KGB with SGB, SGLB, and their ensembles. For the experiments, we use several standard regression datasets. The implementation details can be found in Appendix H. The code of our experiments can be found on GitHub.^77^7 Table 1: Predictive performance, RMSE Table 2: Error and OOD detection We note that in our setup, we cannot compute likelihoods as kernel $\mathcal{K}$ is defined implicitly, and its evaluation requires summing up among all possible trees structures number of which grows as ${({nd})}^{m}$ which is unfeasible, not to mention the requirement to inverse the kernel which requires $\mathcal{O}{(N^{2 + \omega})}$ operations which additionally rules out the applicability of classical Gaussian Processes methods with our kernel. Therefore, a typical Bayesian setup is not applicable, and we resort to the uncertainty estimation setup described in Malinin et al.. Also, the intractability of the kernel does not allow us to treat $\sigma,\delta$ in a fully Bayesian way, as it will require estimating the likelihood. Therefore, we fix them as constants, but we note that this will not affect the evaluation metrics for our setup as they are scale and translation invariant.

First, we compare KGB with SGLB since they both sample from similar posterior distributions. Thus, this comparison allows us to find out which of the algorithms does a better sampling from the posterior and thus provides us with more reliable estimates of knowledge uncertainty. Moreover, we consider the SGB approach as the most "straightforward" way to generate an ensemble of models.

In Table 5, we compare the predictive performance of the methods. Interestingly, we obtain improvements on almost all the datasets. Here we perform cross-validation to estimate statistical significance with paired $t$-test and highlight the approaches that are insignificantly different from the best one ($\text{p-value} > 0.05$). Then, we check whether uncertainty measured as the variance of the model's predictions can be used to detect errors and out-of-domain inputs. Detecting errors can be evaluated via the Prediction-Rejection Ratio (PRR). PRR measures how well uncertainty estimates correlate with errors and rank-order them. Out-of-domain (OOD) detection is usually assessed via the area under the ROC curve (AUC-ROC) for the binary task of detecting whether a sample is OOD. For this, one needs an OOD test set. We use the same OOD test sets (sampled from other datasets) as Malinin et al.. The results of this experiment are given in Table 5. We can see that the proposed method significantly outperforms the baselines for out-of-domain detection. These improvements can be explained by the theoretical soundness of KGB: convergence properties are theoretically grounded and non-asymptotic. In contrast, for SGB, there are no general results applicable in our setting, while for SGLB the guarantees are asymptotic. In summary, these results show that our approach is superior to SGB and SGLB, achieving smaller values of RMSE and having better knowledge uncertainty estimates.

## Conclusion

This paper theoretically analyses the classic gradient boosting algorithm. In particular, we show that GBDT converges to the solution of a certain Kernel Ridge Regression problem. We also introduce a simple modification of the classic algorithm allowing one to sample from the Gaussian posterior. The proposed method gives much better knowledge uncertainty estimates than the existing approaches.

We highlight the following important directions for future research. First, to explore how one can control the kernel and use it for better knowledge uncertainty estimates. Also, we do not analyze generalization in the current work, which is another important research topic. Finally, we need to establish universal approximation property which further justifies need for functional formalism.
