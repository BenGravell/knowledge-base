<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Learning from temporally-correlated data is a core facet of modern machine learning. Yet our understanding of sequential learning remains incomplete, particularly in the multi-trajectory setting where data consists of many independent realizations of a time-indexed stochastic process. This important regime both reflects modern training pipelines such as for large foundation models, and offers the potential for learning without the typical mixing assumptions made in the single-trajectory case. However, instance-optimal bounds are known only for least-squares regression with dependent covariates; for more general models or loss functions, the only broadly applicable guarantees result from a reduction to either i.i.d. learning, with effective sample size scaling only in the number of trajectories, or an existing single-trajectory result when each individual trajectory mixes, with effective sample size scaling as the full data budget deflated by the mixing-time. In this work, we significantly broaden the scope of instance-optimal rates in multi-trajectory settings via the Hellinger localization framework, a general approach for maximum likelihood estimation. Our method proceeds by first controlling the squared Hellinger distance at the path-measure level via a reduction to i.i.d.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

learning, followed by localization as a quadratic form in parameter space weighted by the trajectory Fisher information. This yields instance-optimal bounds that scale with the full data budget under a broad set of conditions. We instantiate our framework across four diverse case studies: a simple mixture of Markov chains, dependent linear regression under non-Gaussian noise, generalized linear models with non-monotonic activations, and linear-attention sequence models. In all cases, our bounds nearly match the instance-optimal rates from asymptotic normality, substantially improving over standard reductions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning from sequential data is central to modern machine learning (ML) and statistical modeling, underpinning applications such as language modeling, speech recognition, time-series forecasting, generalist robotics, neurological sequence analysis, and many other examples. Yet, despite its importance and prevalence, our fundamental understanding of when learning from sequential streams is possible---and what the sharp, problem-specific sample complexities are---remains far less developed compared with the classical i.i.d. setting.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are two predominant approaches to analyzing non-i.i.d. sequential learning setups. The first approach is to consider consuming data from a single stochastic process indexed by time $t$, and study what happens to the estimator as time progresses forward. In this paper, we will refer to a realization from a time-index stochastic process as a trajectory, and hence we denote this approach as the *single-trajectory* setting. This setting is challenging, as simple examples illustrate the necessity of imposing non-trivial assumptions about the long-running behavior of the underlying process. The strongest results hold under assumptions about the rate of convergence (typically quantified via its mixing-time ) of the stochastic process to its time-marginal distributions, and provide bounds on e.g., the excess risk of the empirical risk minimizer (ERM) as time $t$ moves forward (see e.g., ). However, these type of results suffer from some key drawbacks: (i) Many processes---e.g., human dialogue, periodic locomotion gaits, wearable sensor data---are interesting precisely because they do *not* mix.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Even for processes that do mix, analytical bounds on the mixing-time can be quite conservative in high-dimension, and challenging to estimate numerically without assuming extra structure. (ii) Typical bounds suffer from *sample deflation*, where the non-i.i.d. sequential rate is a factor of the mixing-time larger than its corresponding i.i.d. rate (i.e., its effective sample size is deflated by the mixing-time); furthermore, the non-i.i.d. rates are only valid after time $t$ exceeds some factor of the mixing-time, typically referred to as a burn-in time.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The second approach to studying sequential learning sits in-between the classic i.i.d. setting, where every data point is independent, and the single-trajectory setting, where every data point is correlated. Instead, one assumes that many independent realizations of a stochastic process are observed, a setup we will refer to as the *multi-trajectory* setting (see e.g., ). In the multi-trajectory setting, data within a trajectory is temporally correlated as usual, but importantly, data across different trajectories is independent. The latter fact is crucial, as it enables reductions to i.i.d. learning only using minimal assumptions about the underlying process. A further benefit of the multi-trajectory data model is that it is a much more accurate description of the underlying training data for modern ML models which ingest sequential data---such as vision-language models (VLMs), large language models (LLMs), and generalist behavior policies for robotics ---compared with the single-trajectory model.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nevertheless, despite these advantages, many open questions still remain regarding the multi-trajectory model. A naïve reduction to i.i.d. learning, where each trajectory is treated as a single data point, only yields rates where the effective sample size is the $m$, the number of trajectories. Here, the length $T$ of each trajectory^11^1We assume for ease of exposition that each trajectory has the same length. is absent from this sample size, which is in general not the correct scaling. On the other hand, embedding a multi-trajectory process into a single trajectory and appealing to a single-trajectory result yields either (i) similar bounds as the i.i.d. reduction if no assumption on the mixing-time of the individual trajectories is made, or (ii) bounds where the effective sample size scales as the $mT/\kappa$---i.e., *total* number of data points available to the learner divided by the mixing-time $\kappa$ of the individual trajectories. While (ii) improves upon the i.i.d. reduction, the deflation factor is in general not optimal for multi-trajectory settings.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Indeed, a recent line of work shows that for square-loss regression from dependent covariates, one can obtain---under a set of conditions which do not generally require e.g., bounded mixing-times---finite-sample rates where the effective sample size not only improves to $mT$, but also the bounds nearly match those prescribed by asymptotic normality of maximum likelihood estimation (MLE). However, as their proof techniques are tailored specifically for square-loss, it is unclear how to generalize these results more broadly to e.g., MLE settings.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we significantly broaden our understanding of learning in the multi-trajectory setting by providing a general framework---which we call the *Hellinger localization framework*---for deriving sharp instance-optimal parameter recovery rates for general maximum-likelihood estimation. At a high-level, our framework proceeds in two main phases: In the first phase, we utilize a reduction to i.i.d. learning which controls the squared Hellinger distance between the *path measures* of the MLE estimate and the underlying distribution, at a rate where the sample size is $m$, the number of trajectories. In the second phase, we utilize the fact that squared Hellinger distance is locally quadratic in the parameter space, weighted by the Fisher information matrix of the underlying path measure. This has two key consequences: First, it allows us to extract out an additional scaling factor of $T$, the length of each trajectory, whenever the process contains sufficient excitation. Second, the Fisher information matrix allows us to derive instance-specific rates that match, up to logarithmic factors, those prescribed by asymptotic normality of MLE.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our framework thus yields instance-optimal bounds where the effective sample size contains all the observed data (i.e., scales as $mT$), and applies broadly to maximum likelihood estimation problems. Furthermore, as our framework relies only on bounded growth conditions of both the score function and the observed information matrix for localization, it applies beyond the usual mixing processes and stable dynamics typically assumed in sequential learning.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

To demonstrate the generality of our approach, we instantiate the Hellinger localization framework in four case studies: (i) a simple mixture of Markov chains example, (ii) a dependent linear regression setting under general (i.e., non-Gaussian) product-noise distributions, (iii) a non-monotonic generalized linear model (GLM) example, and (iv) a linear-attention sequence modeling problem. For each of these case studies, our framework obtains near-optimal parameter recovery error rates, yielding significant improvements over the rates obtained by standard reductions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Paper organization", "weight": 1.0} -->

This manuscript is organized as follows. In Section 2, we review related work. Section 3 describes the multi-trajectory MLE problem setup, reviews the standard i.i.d. and single-trajectory reductions in more detail, and presents the Hellinger localization framework, including a step-by-step guide describing how to instantiate the framework for a general problem. Section 4 contains the results of our four specific case studies; for each case study, we also conduct a more thorough literature review on the specific problem beyond what is described in Section 2. Section 5 concludes the paper, with the appendices containing the deferred proofs.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Setup and General Framework", "weight": 1.0} -->

In this section, we review background, outline our general problem formulation and describe our new Hellinger localization framework. We first describe the notation used in our work.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Maximum Likelihood Estimation in Multi-Trajectory Settings", "weight": 1.0} -->

We fix an index $T\in\mathbb{N}_{+}$ and consider a stochastic process $z_{1:T}:=(z_{t})_{t=1}^{T}$ taking values in $\mathsf{Z}$. Let $p(z_{1:T})$ denote the joint distribution over $z_{1:T}$. We emphasize that the process $z_{1:T}$ is not necessarily stationary nor ergodic, nor does it necessarily have bounded mixing-times. Our learner observes $m\in\mathbb{N}_{+}$ independent trajectories $\mathcal{D}_{m,T}:=((z^{(i)}_{t})_{t=1}^{T})_{i=1}^{m}$ with each $z^{(i)}_{1:T}\sim p(\cdot)$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Maximum Likelihood Estimation in Multi-Trajectory Settings", "weight": 1.0} -->

Fix a parametric class $\mathcal{P}:=\{p_{\theta}(z_{1:T})\mid\theta\in\Theta\}$ of distributions and consider the maximum-likelihood (MLE) estimator $\hat{p}_{m,T}\in\mathcal{P}$ given the dataset $\mathcal{D}_{m,T}$ as: In this work, we are interested in the finite-sample behavior of the MLE estimator $\hat{p}_{m,T}$ in the *realizable* setting, i.e., where $p\in\mathcal{P}$. We impose some regularity conditions to make the analysis well-posed.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Maximum Likelihood Estimation in Multi-Trajectory Settings", "weight": 1.0} -->

First, we endow $\mathsf{Z}$ with a base measure $\mu$ (e.g., counting measure for discrete $\mathsf{Z}$ or Lebesgue measure when $\mathsf{Z}$ is a subset of Euclidean space), and we overload $p_{\theta}$ to also denote the Radon-Nikodym density w.r.t. the corresponding base measure $\mu$ on $\mathsf{Z}$. We also assume that (a) for $\mu^{\otimes T}$-a.e.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Maximum Likelihood Estimation in Multi-Trajectory Settings", "weight": 1.0} -->

$z_{1:T}\in\mathsf{Z}^{T}$, the map $\theta\mapsto p_{\theta}(z_{1:T})$ is $C^{2}(\Theta_{0})$ where $\Theta_{0}\supseteq\Theta$ is an open set, (b) that there exists a unique $\theta\in\Theta$ such that $p_{\theta}(\cdot)=p(\cdot)$ (almost surely), and that (c) the parameter set $\Theta$ is star-convex around $\theta$.^22^2That is for any $\theta\in\Theta$, $s\theta+(1-s)\theta\in\Theta$ for all $s\in$. As our analysis relies on local quadratic expansions, this technical assumption ensures that such expansions are indeed valid. To set the stage for our results, let us first review what is known about the MLE estimator $\hat{p}_{m,T}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Asymptotic normality", "weight": 1.0} -->

First, we can use the lens of asymptotic normality to understand limiting behavior as $m\to\infty$ (but $T$ is fixed). To do this, we recall that the Fisher information (FI) matrix for the *trajectory* $z_{1:T}$ is defined as: Under the assumption that $\theta\in\mathrm{int}(\Theta)$ and that the estimator $\hat{\theta}_{m,T}$ is consistent (i.e., $\hat{\theta}_{m,T}\to\theta$ a.s. as $m\to\infty$), standard asymptotic normality \see e.g., for $M$-estimators yields: where $\stackrel{{\scriptstyle\mathrm{d}}}{{\rightsquigarrow}}$ denotes convergence in distribution. The condition (3.3) depends implicitly on the trajectory length $T$ through the FI matrix $\mathcal{I}(\theta)$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Asymptotic normality", "weight": 1.0} -->

However, as the FI matrix $\mathcal{I}(\theta)$ factorizes nicely across time: we generically expect that $\mathcal{I}(\theta)$ grows at least linearly with $T$, i.e., $\lambda_{\min}(\mathcal{I}(\theta))\geqslant\Omega(T)$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Asymptotic normality", "weight": 1.0} -->

Hence, if we define the *normalized* Fisher information matrix $\bar{\mathcal{I}}(\theta):=T^{-1}\cdot\mathcal{I}(\theta)$, the result (3.3) implies that the limiting behavior as $m\to\infty$ scales with high probability as: Therefore, as long as the normalized FI matrix provides sufficient excitation so that $\lambda_{\min}(\bar{\mathcal{I}}(\theta))$ does *not* vanish to zero as the trajectory length $T$ increases, then (3.4) implies that the squared parameter error decreases at a $1/(mT)$ rate, a rate which not involves *all* the data points available in the training set, but as importantly is also *instance-optimal*, containing instance-specific scaling through the FI matrix $\bar{\mathcal{I}}(\theta)$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Asymptotic normality", "weight": 1.0} -->

Hence, showing that (3.4) holds in a non-asymptotic, finite number of trajectories regime under general conditions serves as one of the main goals of this work.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Asymptotic normality", "weight": 1.0} -->

As we will discuss in detail in the remainder of this sub-section, finite-sample rates of the form (3.4) are known to hold for the setting of least-squares regression over dependent covariates under various assumptions; unfortunately, these analysis techniques heavily utilize the structure of the square-loss, and do not readily extend to more general losses such as the log-loss for MLE. Beyond the square-loss, the most general rates comes from reductions to either (i) standard i.i.d. learning results or (ii) existing single-trajectory results; the former yields rates exhibiting sub-optimal $1/m$ scaling, whereas the latter inherits the single-trajectory stability assumptions that are often unnecessary in the multi-trajectory case, and suffers from sample-deflation issues in the rates. This motivates the need for developing a new approach for establishing finite-sample instance-optimal rates for the multi-trajectory setting, which we turn to in Section 3.2.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Linear least-squares regression and linear system identification", "weight": 1.0} -->

One case where a non-asymptotic rate of the form (3.4) is shown to hold in the literature is in the setting of linear least-squares regression over dependent covariates.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Linear least-squares regression and linear system identification", "weight": 1.0} -->

Specifically, consider the following linear dynamical system (LDS) parameterized by $A\in\mathbb{R}^{d\times d}$: For any $\theta=\mathrm{vec}(A)\in\mathbb{R}^{d^{2}}$, the FI matrix $\mathcal{I}(\theta)$ takes on the form: Hence letting $\hat{A}_{m,T}\in\operatorname*{arg\,min}_{A\in\mathbb{R}^{d\times d}}\tsum\slimits@_{i=1}^{m}\tsum\slimits@_{t=1}^{T-1}\lVert z_{t+1}^{(i)}-Az_{t}^{(i)}\rVert^{2}$ denote the MLE (3.1) and $A$ denote the true dynamics matrix generating the data via (3.5), plugging the FI matrix into (3.4) yields where

<!-- chunk {"id": "body-0026", "role": "body", "section": "Linear least-squares regression and linear system identification", "weight": 1.0} -->

In, it is shown that this rate (3.6) holds in expectation whenever $m\gtrsim d$, and that this cut-off is sharp. Similar results hold for the more general linear regression from LDS covariates. We emphasize here that the rate from (3.6) is truly a multi-trajectory phenomenon, and is *not* possible for arbitrary $A$ from a single trajectory; as shown, the MLE is not generally consistent in the single-trajectory setting when $A$ is unstable.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Reductions to existing i.i.d./single-trajectory results", "weight": 1.0} -->

Beyond the linear least-squares regression setting, a simple generic approach for deriving rates in the multi-trajectory setting is to invoke an existing i.i.d. and/or single-trajectory result. As an example of an i.i.d. reduction, using the standard Rademacher complexity machinery for deriving risk bounds in independent settings,^33^3For analyzing MLE, there are much sharper non-asymptotic analysis in the i.i.d. setting (e.g.,), which do not require almost sure bounds on log-likelihoods, contain the correct variance-optimal scaling, and also capture fast-rates in realizable settings. We present the simplest result here to make our point clear.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Reductions to existing i.i.d./single-trajectory results", "weight": 1.0} -->

we have that the excess risk (in KL-divergence) of the MLE $\hat{\theta}_{m,T}$ satisfies with probability at least $1-\delta$, where $B$ bounds the log-likelihood $T^{-1}\cdot\log p_{\theta}(z_{1:T})$ a.s., $\mathcal{R}_{m}(\mathcal{G}_{t})$ is the Rademacher complexity of the function class $\mathcal{G}_{t}:=\{z_{1:T}\mapsto\log p_{\theta}(z_{t}\mid z_{1:t-1})\mid\theta\in\Theta\}$, and $c_{0}$ is a universal constant.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Reductions to existing i.i.d./single-trajectory results", "weight": 1.0} -->

Assuming that each conditional $|\log p_{\theta}(z_{t}\mid z_{1:t-1})|\leqslant O$, then we have $B\leqslant O$ as well. We also generically expect that $\mathcal{R}_{m}(\mathcal{G}_{t})\leqslant O(\sqrt{p/m})$, which is the usual rate for parametric function classes.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Reductions to existing i.i.d./single-trajectory results", "weight": 1.0} -->

Furthermore, $\frac{1}{T}\mathrm{KL}(p(z_{1:T})\;\|\;p_{\hat{\theta}_{m,T}}(z_{1:T}))\approx\frac{1}{2}\lVert\theta-\hat{\theta}_{m,T}\rVert^{2}_{\bar{\mathcal{I}}(\theta)}$ asymptotically as $\hat{\theta}_{m,T}\to\theta$, and hence the scaling w.r.t. $T$ in the excess risk (3.7) is the correct one for comparison to (3.4). Therefore, the general scaling for the RHS of (3.8) is of order $\sqrt{p/m}$, i.e., the effective sample size is the number of trajectories $m$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Reductions to existing i.i.d./single-trajectory results", "weight": 1.0} -->

Note that in the realizable setting when $\inf_{\theta^{\prime}\in\Theta}\mathrm{KL}(p(z_{1:T})\;\|\;p_{\theta^{\prime}}(z_{1:T}))=0$, the bound for (3.8) can be improved to a fast-rate $p/m$ scaling with local Rademacher complexities.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Reductions to existing i.i.d./single-trajectory results", "weight": 1.0} -->

Single-trajectory results can also be used for reductions, by embedding the trajectories $\{z_{1:T}^{(i)}\}$ into one single trajectory $\bar{z}_{1:mT}:=(z_{1:T}^{},\dots,z_{1:T}^{(m)})$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Reductions to existing i.i.d./single-trajectory results", "weight": 1.0} -->

For this discussion, we focus on results relying on $\beta$-mixing^44^4The $\beta$-mixing coefficients (cf.) for $\{z_{t}\}_{t=1}$ are defined as $\beta(k):=\sup_{j\in\mathbb{N}_{+}}\mathbb{E}_{z_{1:j}}[\lVert\mathbb{P}_{z_{j+k:\infty}}(\cdot\mid z_{1:j})-\mathbb{P}_{z_{j+k:\infty}}\rVert_{\mathrm{TV}}]$. The process is called $\beta$-mixing if $\beta(k)\to 0$ as $k\to\infty$. for concreteness, noting that our discussion also applies to results that rely on other definitions of mixing (e.g., $\phi$-mixing) in the literature.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Reductions to existing i.i.d./single-trajectory results", "weight": 1.0} -->

We also assume the process $\{z_{t}\}$ is Markovian, as this makes the reduction simpler to state. Because $z_{1:T}^{(i)}\perp z_{1:T}^{(j)}$ whenever $i\neq j$, then we have that the $\beta$-mixing coefficients $\bar{\beta}(k)$ of $\{\bar{z}_{t}\}$ satisfy $\bar{\beta}(k)=\beta(k)\cdot\mathds{1}\{k<T\}$, where $\beta(k)$ are the $\beta$-mixing coefficients of $\{z_{t}\}$. Hence, the embedded trajectory $\{\bar{z}_{t}\}$ is trivially $\beta$-mixing with mixing-time equal to $T$ without any assumption on $\beta(k)$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Reductions to existing i.i.d./single-trajectory results", "weight": 1.0} -->

Using this mixing-time and invoking a single-trajectory $\beta$-mixing result, such as, without any further assumption on $\beta(k)$ yields a similar result to (3.8).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Reductions to existing i.i.d./single-trajectory results", "weight": 1.0} -->

However, if we further assume that $\beta(k)\leqslant C\exp(-\rho k)$ for some $\rho>0$, and that $T/(2\kappa)\in\mathbb{N}_{+}$ for $\kappa:=\lceil\rho^{-1}\log(CmT/\delta)\rceil$, then we have the improved result: with probability at least $1-\delta$, where $\bar{\mathcal{R}}_{mT/\kappa}^{j}$ denotes the *de-coupled* Rademacher complexity: with the pair $(\tilde{z}^{(i)}_{(\ell-1)2\kappa+j-1},\tilde{z}^{(i)}_{(\ell-1)2\kappa+j})$ drawn from the same distribution as

<!-- chunk {"id": "body-0037", "role": "body", "section": "Reductions to existing i.i.d./single-trajectory results", "weight": 1.0} -->

$(z_{(\ell-1)2\kappa+j-1},z_{(\ell-1)2\kappa+j})$, but *independently* across $i\in[m]$ and $\ell\in[\kappa]$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Reductions to existing i.i.d./single-trajectory results", "weight": 1.0} -->

Similar to before, we generically expect that $\bar{\mathcal{R}}^{j}_{mT/\kappa}$ scales as order $\sqrt{\kappa p/(mT)}$. Hence, the general scaling of the RHS of (3.9) is of order $\sqrt{\kappa p/(mT)}$. Furthermore, as with the i.i.d. reduction, in the realizable setting local Rademacher arguments can also be used to improve the scaling of (3.9) to the fast-rate $\kappa p/(mT)$. This is an improvement over (3.8), as the effective sample size increases from $m$ to $mT/\kappa$; however, this sample size still remains deflated by $\kappa$, as a consequence of the standard blocking technique used for de-coupling.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Regression with square-loss", "weight": 1.0} -->

A recent line of work has shown that the sample size deflation described previously can be removed in the special case of non-linear regression with the square-loss, in both parametric and non-parametric regimes. To make their results concrete, we consider the following parametric family of distribution $\mathcal{P}$ over trajectories in $\mathbb{R}^{d}$: coupled with the non-linear least-squares estimator $\hat{\theta}_{m,T}\in\operatorname*{arg\,min}_{\theta\in\Theta}\tsum\slimits@_{i=1}^{m}\tsum\slimits@_{t=1}^{T-1}\lVert z_{t+1}^{(i)}-f_{\theta}(z_{t}^{(i)})\rVert^{2}$ with $\Theta\subseteq\mathbb{R}^{p}$, which is precisely the MLE estimator for (3.10).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Regression with square-loss", "weight": 1.0} -->

We now specialize the main result of \[2, Theorem 3.1\] to the problem (3.10). Suppose that the following assumptions hold:^55^5We state a clear set of assumptions, but not the most minimal, as \[2, Theorem 3.1\] is stated in broad generality.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Regression with square-loss", "weight": 1.0} -->

*(Realizable):* The process $\{z_{t}\}$ is generated by (3.10) for some $\theta\in\Theta$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Regression with square-loss", "weight": 1.0} -->

*(Stationary process):* The process $\{z_{t}\}$ has a stationary measure $\nu$, and $z_{1}\sim\nu$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Regression with square-loss", "weight": 1.0} -->

*(Function class regularity):* For every $x\in\mathbb{R}^{d}$, the map $\theta\mapsto f_{\theta}(x)$ is $L(x)$-Lipschitz, with $\lVert L(x)\rVert_{\mathcal{L}^{2}(\nu)}<\infty$. Furthermore, the set $\Theta\subseteq\mathbb{R}^{p}$ is a bounded set.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Regression with square-loss", "weight": 1.0} -->

*(Burn-in):* Either (i) $mT\gtrsim\mathrm{poly}_{\eta}(T,p)$ or (ii) $\{z_{t}\}$ is $\beta$-mixing with $\beta(k)\leqslant C\exp(-\rho k)$ and $T\gtrsim\kappa:=\lceil\rho^{-1}\log(CmT/\delta)\rceil$, $mT\gtrsim\mathrm{poly}_{\eta}(\kappa,p)$, where $\mathrm{poly}_{\eta}(\cdot)$ denotes that the polynomial dependence is a function of $\eta$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Regression with square-loss", "weight": 1.0} -->

Then, the MLE estimator $\hat{\theta}_{m,T}$ satisfies with probability at least $1-\delta$, where $\sigma^{2}_{\mathrm{prox}}\geqslant\sigma^{2}$ is a variance proxy which is determined from the specific choice of $(p,\eta)$ in Assumption (c). In the case where $p=\infty$, we have $\sigma^{2}_{\mathrm{prox}}=\sigma^{2}$. Furthermore, when $p<\infty$ and $\eta=1$, we have that $\sigma^{2}_{\mathrm{prox}}=C_{p}\sigma^{2}+o_{mT}$ by the martingale Rosenthal inequality (cf. A.6.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Regression with square-loss", "weight": 1.0} -->

‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), where $C_{p}$ is a constant only depending on $p$. On the other hand, when $p<\infty$ and $\eta<1$, the precise relationship between $\sigma^{2}_{\mathrm{prox}}$ and $\sigma^{2}$ is more complex. We observe that the rate (3.11) is order-wise optimal from asymptotic normality (up to the variance proxy $\sigma^{2}_{\mathrm{prox}})$; importantly, the rate (3.11) has the correct dependence on the entire dataset size $mT$, compared with the deflated rate $mT/\kappa$ from the previous single-trajectory reduction.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Regression with square-loss", "weight": 1.0} -->

However, Assumptions (a)-(e) can be restrictive and/or challenging to verify. We first note that the stationary process Assumption (b) can be removed by using \[19, Theorem 4.1\] instead of \[2, Theorem 3.1\], although the downside of this is that the weakly sub-Gaussian Assumption (c) is then replaced with a trajectory-level hyper-contractivity condition (cf. \[19, Def. 4.1\]) which is more challenging to verify. On the other hand, while the weakly sub-Gaussian Assumption (c) holds broadly if $f_{\theta}$ is bounded and smooth in its input (cf. \[2, Prop. 4.1\]), the constants $(L,\eta)$ provided depend poorly on the process dimension $d$, which yields burn-in times for $m,T$ that can depend exponentially in $d$; sharp control on the $(L,\eta)$ constants is only currently available for simple function classes, e.g., linear function classes.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Summary", "weight": 1.0} -->

The finite-sample behavior of the MLE in multi-trajectory settings is currently most broadly available through reduction to either an existing i.i.d. or single-trajectory result. In either case, there is a gap between the resulting bound (cf. (3.8) for the i.i.d. reduction and (3.9) for the single-trajectory reduction) compared with the optimal bound (3.4) in terms of effective sample sizes. In the case of least-squares regression (both for linear and more general parametric models), however, the finite-sample rate (3.6) for linear regression and (3.11) for more general parametric regression matches the CLT-optimal bound up to constant factors in the former, and up to a variance-proxy factor in the latter. This naturally raises the question whether optimal finite-sample rates can be derived beyond the square-loss setting.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Summary", "weight": 1.0} -->

The proof techniques used for analyzing the square-loss (e.g., self-normalized martingales, small-ball inequalities) take advantage of either the closed-form nature of the linear regression solution, or specific properties of the square-loss such as the offset basic inequality \see e.g. and hence do not readily generalize. This motivates the need for a different approach for establishing error bounds of the form (3.4) in more general settings.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Analyzing MLE via Localization in Hellinger Distance", "weight": 1.0} -->

We next develop a set of tools and a general five-step framework for analyzing the MLE over a diverse set of problems. The roadmap for the remainder of this section is as follows. We first develop tools in Section 3.2.1 to control the Hellinger distance of the MLE solution to the true solution in terms of their length-$T$ trajectory (path) measures. Next, we study in Section 3.2.2 how we can localize the Hellinger distance so that it approximately behaves like a weighted Euclidean norm over the parameters, where the weight is determined by the Fisher information matrix at optimality. Importantly, given sufficient trajectory-level excitation, the FI matrix scales with the trajectory length $T$, providing the correct scaling with length of each trajectory. Building on these mathematical tools, in Section 3.3 we work through a simple illustrative example combining these tools to derive a sharp rate for parameter recovery in a two-state Markov chain. Finally, we present our general Hellinger localization framework in Section 3.4.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Divergence measures", "weight": 1.0} -->

For two measures $p,q$ over the same probability space, we define the Total-Variation (TV) distance, Hellinger distance, and Kullback-Leibler (KL) divergence as: Note that the last definition of KL divergence require the absolute continuity condition $p\ll q$. For what follows, we will often overload notation and write e.g., $\mathrm{d}_{H}(\theta_{1},\theta_{2})=\mathrm{d}_{H}(p_{\theta_{1}},p_{\theta_{2}})$ for $\theta_{1},\theta_{2}\in\Theta$ (and similarly for TV distance and KL divergences).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Control of Trajectory Measures in Hellinger Distance", "weight": 1.0} -->

Our main approach is based on techniques used for studying density estimation with maximum-likelihood. To set the stage for what follows, we first state a prototypical non-asymptotic result from the study of maximum-likelihood estimators. The following instantiation is from and applied directly to our problem setting (3.1), although it traces its roots back to the work of. Similar instantiations of the following result can also be found in more recent works.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 3.7", "weight": 1.0} -->

One key difference between 3.1. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") and 3.6 is that the former applies directly to the MLE estimator $\hat{\theta}_{m,T}$ (3.1) over $\mathcal{P}$, whereas the latter applies to the discretized MLE estimator $\hat{\theta}^{\varepsilon}_{m,T}$ (3.14) over $\mathcal{P}_{\varepsilon}$. In practice there is no difference between these two estimators at a sufficiently small $\varepsilon$ below floating point resolution. However, from a theoretical perspective, the discrete estimator seems to exhibit more favorable properties than the exact MLE estimator. One of these properties is allowing one to relax the covering requirement on $\mathcal{P}$ to either Hellinger (3.15.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 3.7", "weight": 1.0} -->

‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) or max FI-divergence (3.16. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), both which are less stringent than the max divergence covering in 3.1. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), which requires an almost sure bound on the log-density ratio.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 3.7", "weight": 1.0} -->

This is an important relaxation, as it allows us to handle trajectory distributions where the paths $z_{1:T}$ are not bounded almost surely; in such situations the Hellinger/max-FI divergences can still be finite as we will see in the sequel. We leave open the question of whether rates of the form (3.15. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) and (3.16. ‣ Theorem 3.6.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Remark 3.7", "weight": 1.0} -->

‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) are possible for $\hat{p}_{m,T}$ without relying on max divergence coverings, noting that some extra tail conditions on $\mathcal{P}$ would be needed to control the behavior of the empirical log likelihood $\frac{1}{m}\tsum\slimits@_{i=1}^{m}\log p(z^{(i)}_{1:T})$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 3.8", "weight": 1.0} -->

The key difference between (3.15. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) and (3.16. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) is that the former only controls $\mathrm{d}_{H}(\hat{\theta}^{\varepsilon}_{m,T},\theta)$, whereas the latter controls $\mathrm{d}_{H}(\theta,\theta)$ along the entire ray $\theta\in\mathrm{conv}\{\hat{\theta}^{\varepsilon}_{m,T},\theta\}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 3.8", "weight": 1.0} -->

Note that since in general neither Hellinger nor squared Hellinger distance is convex in the *parameter space*, the former in general does *not* imply the latter. Thus, (3.16. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) is a strictly stronger conclusion than (3.15. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), and therefore requires a stronger set of assumptions (e.g., log-concavity of $\mathcal{P}$). As we will see in the sequel, the conclusion (3.16. ‣ Theorem 3.6.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 3.8", "weight": 1.0} -->

‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) will play an important role in allowing $m\gtrsim\mathrm{polylog}(T)$ instead of $m\gtrsim T\cdot\mathrm{polylog}(T)$ minimum number of trajectories for our CLT rates to hold.

<!-- chunk {"id": "body-0060", "role": "body", "section": "(a)", "weight": 1.0} -->

Let $\mathcal{P}_{\varepsilon}\subseteq\mathcal{P}$ denote a minimal $\varepsilon$-covering of $\mathcal{P}$ in the Hellinger distance (cf. 3.2. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")).

<!-- chunk {"id": "body-0061", "role": "body", "section": "(a)", "weight": 1.0} -->

Let us abbreviate $\hat{p}^{\varepsilon}:=\hat{p}^{\varepsilon}_{m,T}$, and for $p\in\mathcal{P}$ let $\varphi_{\varepsilon}[p]\in\mathcal{P}_{\varepsilon}$ denote the closest element in the Hellinger cover, i.e., $\mathrm{d}_{H}(\varphi_{\varepsilon}[p],p)\leqslant\varepsilon$. We first consider a hypothetical scenario where each $z^{(i)}:=z^{(i)}_{1:T}$ in $\mathcal{D}_{m,T}$ is drawn i.i.d. from $p^{\varepsilon}:=\varphi_{\varepsilon}[p]$ instead of $p$. By combining (3.17) and A.5.

<!-- chunk {"id": "body-0062", "role": "body", "section": "(a)", "weight": 1.0} -->

‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") with a union bound over $\mathcal{P}_{\varepsilon}$, we have with probability at least $1-\delta/2$ over $(p^{\varepsilon})^{\otimes m}$, where the last inequality is since $\hat{p}^{\varepsilon}$ is the MLE over $\mathcal{P}_{\varepsilon}$ and $p^{\varepsilon}\in\mathcal{P}_{\varepsilon}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "(a)", "weight": 1.0} -->

On the other hand, by triangle inequality for Hellinger distance followed by the inequality $(a+b)^{2}\leqslant 2(a^{2}+b^{2})$ for $a,b\in\mathbb{R}$, Hence, we have shown that: where $\hat{p}^{\varepsilon}[\mathcal{D}_{m,T}]$ is notation to emphasize that $\hat{p}^{\varepsilon}$ is a function of the data $\mathcal{D}_{m,T}$. Recall that $\lVert p-q\rVert_{\mathrm{TV}}\leqslant\mathrm{d}_{H}(p,q)$ for two measures $p,q$ \cf. [39, Section 7.3\].

<!-- chunk {"id": "body-0064", "role": "body", "section": "(a)", "weight": 1.0} -->

Hence we can change measure between $\mathcal{D}_{m,T}\sim(p^{\varepsilon})^{\otimes m}$ and $\mathcal{D}_{m,T}\sim p^{\otimes m}$ as follows: where the last inequality follows from A.2 since we have $\mathrm{d}_{H}(p,p^{\varepsilon})\leqslant\varepsilon\leqslant\delta/(2\sqrt{2m})$. This establishes (3.15. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) for the Hellinger divergence discretized $\hat{\theta}^{\varepsilon}_{m,T}$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "(a)", "weight": 1.0} -->

The proof for the max FI divergence discretized estimator is nearly identical, and hence omitted.

<!-- chunk {"id": "body-0066", "role": "body", "section": "(b)", "weight": 1.0} -->

we first consider a hypothetical scenario where each $z^{(i)}:=z^{(i)}_{1:T}$ in $\mathcal{D}_{m,T}$ is drawn i.i.d.

<!-- chunk {"id": "body-0067", "role": "body", "section": "(b)", "weight": 1.0} -->

from $p^{\varepsilon}:=p_{\theta^{\varepsilon}}$. By combining (3.17) and A.5. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") with a union bound over both $\mathcal{P}_{\varepsilon}$ and $\{s_{k}\}_{k=1}^{N}$, we have with probability at least $1-\delta/2$ over $(p^{\varepsilon})^{\otimes m}$, abbreviating $\hat{\theta}^{\varepsilon}(s_{\eta}):=\hat{\theta}^{\varepsilon}(s_{\eta};\theta^{\varepsilon})$, where the last inequality holds from the following arguments.

<!-- chunk {"id": "body-0068", "role": "body", "section": "(b)", "weight": 1.0} -->

First note that log-concavity of $\mathcal{P}$ means that for $\mu^{\otimes T}$ a.e. $z\in\mathsf{Z}^{T}$, $-\log p_{\hat{\theta}^{\varepsilon}(s_{\eta})}(z)\leqslant-(1-s_{\eta})\log p_{\theta^{\varepsilon}}(z)-s_{\eta}\log p_{\hat{\theta}^{\varepsilon}}(z)$. Hence, and therefore we have that the empirical log-likelihood ratio satisfies: where the last inequality holds since $\hat{\theta}^{\varepsilon}$ is a MLE over $\mathcal{P}_{\varepsilon}$ and $p^{\varepsilon}\in\mathcal{P}_{\varepsilon}$. Let us denote the event that (3.19.

<!-- chunk {"id": "body-0069", "role": "body", "section": "(b)", "weight": 1.0} -->

‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds as $\mathcal{E}_{1}$. On this event, we have by (3.18.

<!-- chunk {"id": "body-0070", "role": "body", "section": "(b)", "weight": 1.0} -->

‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) and $(a+b+c)^{2}\leqslant 3(a^{2}+b^{2}+c^{2})$ for $a,b,c\in\mathbb{R}$, on $\mathcal{E}_{1}$, for every $s\in$, Hence, we have shown that: Above, as in part (a), we use the notation $\hat{\theta}^{\varepsilon}[\mathcal{D}_{m,T}]$ to emphasize the dependence of the estimator on the data $\mathcal{D}_{m,T}$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "(b)", "weight": 1.0} -->

We now take similar steps as in part (a) to change measure between $\mathcal{D}_{m,T}\sim(p^{\varepsilon})^{\otimes m}$ and $\mathcal{D}_{m,T}\sim p^{\otimes m}$: where the last inequality follows from A.2 since we have $\mathrm{d}_{H}(p,p^{\varepsilon})\leqslant\varepsilon\leqslant\delta/(2\sqrt{2m})$. This establishes the result. ∎

<!-- chunk {"id": "body-0072", "role": "body", "section": "Equivalence of Hellinger Distance and Fisher-weighted Metric", "weight": 1.0} -->

3.6 is, at its core, a result about i.i.d. learning. It however contains a rich amount of information about trajectories *within* the divergence term $\mathrm{d}_{H}^{2}(\theta^{\varepsilon}_{m,T},\theta)$. In this section, we study how to extract this information out of the Hellinger divergence. As previously discussed, this is challenging as neither the Hellinger nor squared Hellinger distance tensorizes across $z_{1:T}$ in non-i.i.d. settings. However, when $\hat{\theta}^{\varepsilon}_{m,T}$ is close to $\theta$, such a tensorization is indeed possible, as observed via the asymptotic expansion (3.12). Our next result quantifies the radius of validity for this expansion, through a second-order Taylor expansion analysis.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Remark 3.10", "weight": 1.0} -->

The constants in (3.23. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) and (3.25. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) can be made arbitrarily close to $1/4$ (cf. (3.12)) at the expense of decreasing the constants in the local radius conditions (3.22. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) and (3.24.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Remark 3.10", "weight": 1.0} -->

‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")).

<!-- chunk {"id": "body-0075", "role": "body", "section": "(a)", "weight": 1.0} -->

Fix a vector $q\in\mathbb{R}^{p}$ and $s\in$. We first bound: where (a) is Cauchy-Schwarz, (b) follows by the following bounds with $q_{s}:=\mathcal{I}_{s}^{-1/2}q$ and using the inequality $(a+b)^{2}\leqslant 2(a^{2}+b^{2})$ for $a,b\in\mathbb{R}$: \(c\) follows from the basic inequalities: and (d) follows by our stated assumption (3.26). Hence, setting $q=\mathcal{I}_{s}^{1/2}\Delta$, we have: Now, utilizing the second order expansion from (3.26), The upper bound is established in a nearly identical way, which yields (3.23. ‣ Proposition 3.9.

<!-- chunk {"id": "body-0076", "role": "body", "section": "(a)", "weight": 1.0} -->

‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")).

<!-- chunk {"id": "body-0077", "role": "body", "section": "(b)", "weight": 1.0} -->

Using (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), we conclude that for all $s\in$, From this, we conclude that: from which (3.25. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) follows from plugging the above semidefinite inequalities into (3.23. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")).

<!-- chunk {"id": "body-0078", "role": "body", "section": "(b)", "weight": 1.0} -->

∎ 3.9 shows that the region for which the asymptotic expansion (3.12) holds is governed by two key conditions: (i) the value of $\sup_{\theta\in\mathrm{conv}\{\theta_{0},\theta_{1}\}}\mathrm{d}_{H}(\theta_{0},\theta)$ being small enough relative to the inverse of the moment bounds $B_{1}^{2}(\theta_{0},\theta_{1})$ and $B_{2}(\theta_{0},\theta_{1})$ (cf. (3.22. ‣ Proposition 3.9.

<!-- chunk {"id": "body-0079", "role": "body", "section": "(b)", "weight": 1.0} -->

‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"))), and (ii) the parameters $\theta_{0},\theta_{1}$ being close enough as measured through the corresponding FI matrices (cf. (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"))). In Section 3.4, we describe the Hellinger localization framework, which gives a general recipe for verifying these conditions so that 3.6 can be used in conjunction with 3.9 to establish non-asymptotic rates for the MLE which exhibit the CLT scaling (3.4).

<!-- chunk {"id": "body-0080", "role": "body", "section": "(b)", "weight": 1.0} -->

Before describing our general framework, we first work through a specific example next in Section 3.3, which will set the stage for the general recipe.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Two-State Markov Chain Example", "weight": 1.0} -->

We now demonstrate how the combination of 3.6 and 3.9 gives us a nearly optimal parameter recovery bound via a simple example. We consider a two-state discrete-time Markov chain, where $\mathsf{Z}=\{0,1\}$, $\Theta=[\mu,1-\mu]$ for some $\mu\in(0,1/2)$, and $\mathcal{P}$ is the set of all two-state Markov chains with $z_{1}\sim\rho_{1}$ (independent of $\theta$) and one-step transition probability: For what follows, we will assume that $T\geqslant 2$ (otherwise no information about the Markov chain transition probabilities is revealed). We assume $p\in\mathcal{P}$ with parameter $\theta\in\Theta$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Two-State Markov Chain Example", "weight": 1.0} -->

While this specific problem is simple enough that its MLE estimator can be studied via only elementary concentration inequalities (which we discuss at the end), we utilize our framework to analyze this problem in order to illustrate both the mechanics and relative sharpness of our arguments.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Roadmap", "weight": 1.0} -->

We first compute the FI matrix $\mathcal{I}(\theta)$ in addition to its uniform bound $\mathcal{I}_{\max}$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Roadmap", "weight": 1.0} -->

From these quantities, we bound the covering number $\mathcal{N}_{\mathcal{I}_{\max}}(\mathcal{P},\varepsilon)$ and invoke 3.6 (b) for log-concave $\mathcal{P}$; this yields control of the Hellinger distance between $\theta$ and every element in $\mathrm{conv}\{\theta,\hat{\theta}^{\varepsilon}_{m,T}\}$, where $\hat{\theta}^{\varepsilon}_{m,T}$ denotes the discretized MLE estimator.^99^9Specially, $\hat{\theta}^{\varepsilon}_{m,T}$ denotes the max FI divergence discretized MLE estimator at resolution $\varepsilon=1/(2\sqrt{2m})$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Roadmap", "weight": 1.0} -->

With this bound in hand, we then estimate the quantities $B_{1},B_{2}$ (cf. (3.20), (3.21)); a key intermediate step is to show that control of the Hellinger distance from 3.6 implies a direct $O(1/m)$ bound on the squared parameter error, which we then use to localize the $B_{1},B_{2}$ computation in a small neighborhood around $\theta$. At this point, we are now able to invoke 3.9 (a) to boost our bound on the squared parameter error to $O(1/(mT))$; the only missing piece is that this bound is not variance-optimal. However, by using this bound to establish that the condition (3.24. ‣ Proposition 3.9.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Roadmap", "weight": 1.0} -->

‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds, we finally conclude by invoking 3.9 (b), which yields the instance-optimal rate.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Roadmap", "weight": 1.0} -->

Towards carrying out this plan, we first introduce some notation. Let us denote $\sigma^{2}:=\theta(1-\theta)$, which is the variance of a $\mathrm{Bern}(\theta)$ distribution, and governs the curvature of the FI matrix $\mathcal{I}(\theta)$. We also define the set $\Theta_{\sigma}:=\{\theta\in\Theta\mid|\theta-\theta|\leqslant\sigma^{2}/2\}$ for localization purposes: observe that for $\theta\in\Theta_{\sigma}$, we have $\frac{1}{\theta(1-\theta)}\leqslant\frac{2}{\sigma^{2}}$, a key inequality we will use in our computations.

<!-- chunk {"id": "body-0088", "role": "body", "section": "FI matrix, covering number, and Hellinger bound", "weight": 1.0} -->

We first gather the results of some straightforward computations in Appendix B: From this, we bound covering number of $\mathcal{P}$ in the max FI-divergence (cf. 3.4. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) as: Now we are in a position to apply 3.6. Setting $\varepsilon=\delta/(2\sqrt{2m})$ and $\eta=1/\mathrm{diam}(\Theta)$, we obtain with probability at least $1-\delta$, the max FI divergence MLE estimator satisfies: Let us denote the event in (3.28) by $\mathcal{E}_{1}$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Estimate $B_{1}$ and $B_{2}$", "weight": 1.0} -->

We will estimate $B_{1}(\theta_{0},\theta_{1})$ and $B_{2}(\theta_{0},\theta_{1})$ over $\theta_{0},\theta_{1}\in\Theta_{\sigma}$. Before we proceed, we first utilize (3.28) to construct a condition on $m$ such that $\hat{\theta}_{m,T}^{\varepsilon}\in\Theta_{\sigma}$ on $\mathcal{E}_{1}$. Specifically: where (a) uses the data processing inequality for $f$-divergences, (b) uses the inequality $\lVert p-q\rVert_{\mathrm{TV}}\leqslant\mathrm{d}_{H}(p,q)$ for two measures $p,q$, and (c) uses the fact that $z_{1}\sim\rho_{1}$ irregardless of $\theta$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Estimate $B_{1}$ and $B_{2}$", "weight": 1.0} -->

Hence, if $m\gtrsim\sigma^{-4}\log(mT/(\mu\delta))$, then we have that $\hat{\theta}^{\varepsilon}_{m,T}\in\Theta_{\sigma}$ on $\mathcal{E}_{1}$. By convexity of $\Theta_{\sigma}$, this implies that $\mathrm{conv}\{\hat{\theta}^{\varepsilon}_{m,T},\theta\}\subset\Theta_{\sigma}$. By A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), it suffices to take $m\gtrsim\sigma^{-4}\log(T/(\mu\delta))$. In summary: Next, we show in Appendix B that: Hence, for any $\theta\in\Theta_{\sigma}$, we have: Therefore, we have established

<!-- chunk {"id": "body-0091", "role": "body", "section": "Parameter error bound", "weight": 1.0} -->

We first verify the condition in (3.22. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) for $\theta_{0}=\theta$ and $\theta_{1}=\hat{\theta}^{\varepsilon}_{m,T}$. By combining (3.28), (3.31), and A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), it suffices to choose an $m$ satisfying: Thus combining all requirements on $m,T$ from (3.28), (3.29), and (3.32): Therefore by (3.23. ‣ Proposition 3.9.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Parameter error bound", "weight": 1.0} -->

‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) from 3.9, we have on $\mathcal{E}_{1}$: To lower bound the LHS, observe that for any $\theta\in\Theta$, $\mathcal{I}(\theta)\geqslant 4(T-1)$. Hence for any $\theta_{0},\theta_{1}\in\Theta$, $\mathcal{I}(\theta_{0},\theta_{1})\gtrsim T$, which implies that on $\mathcal{E}_{1}$,

<!-- chunk {"id": "body-0093", "role": "body", "section": "Verify FI radius", "weight": 1.0} -->

We first observe for any $\theta_{0},\theta_{1}\in\Theta_{\sigma}$, From (3.33) and (3.34), we have on $\mathcal{E}_{1}$: By another application of A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), we can ensure the FI radius condition (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds on $\mathcal{E}_{1}$ by setting $mT\gtrsim\sigma^{-4}\log(1/(\mu\delta))$, which is already implied by $m\gtrsim\sigma^{-4}\log(T/(\mu\delta))$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Verify FI radius", "weight": 1.0} -->

3.9 now yields via (3.25. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) that on $\mathcal{E}_{1}$,

<!-- chunk {"id": "body-0095", "role": "body", "section": "Final result", "weight": 1.0} -->

Combining the previous arguments, the final result is that as long as $m$ satisfies: then with probability at least $1-\delta$ (over $\mathcal{D}_{m,T}$),

<!-- chunk {"id": "body-0096", "role": "body", "section": "Sharpness of the result", "weight": 1.0} -->

We now evaluate the sharpness of this result by providing an elementary solution based on sub-Exponential tail inequalities for Binomial distributions. We show in Appendix B that there exists an event $\mathcal{E}_{2}$ with probability at least $1-\delta$ that satisfies Comparing both the requirement on $mT$ in (3.37) to (3.35), in addition to the final error rate to (3.36), we see that the result utilizing our framework is sharp up to log factors in the final error rate, but misses a few factors in the requirement on $m$. In particular, (3.37) shows that $mT\gtrsim\tilde{O}(\sigma^{-2})$ suffices to enter the CLT rate regime, but (3.35) requires the more conservative bound $m\gtrsim\tilde{O}(\sigma^{-4})$.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Sharpness of the result", "weight": 1.0} -->

We note that the source of this conservatism is due to (a) the use of the data processing inequality to lower bound $\mathrm{d}_{H}(\hat{p}^{\varepsilon}_{m,T},p)\geqslant\mathrm{d}_{H}(\hat{p}^{\varepsilon}_{m,T}(z_{1},z_{2}),p(z_{1},z_{2}))$ and (b) further lower bounding

<!-- chunk {"id": "body-0098", "role": "body", "section": "Sharpness of the result", "weight": 1.0} -->

The DPI inequality (a) is lossy in this case, since it is possible to prove (at least when $\rho_{1}=\mathrm{Unif}(\{1,2\})$) that the tensorization property $\mathrm{d}_{H}^{2}(\theta_{0},\theta_{1})=1-(1-\mathrm{d}_{H}^{2}(\mathrm{Bern}(\theta_{0}),\mathrm{Bern}(\theta_{1})))^{T-1}$ actually holds \see e.g. [57, Lemma 5\]. Going from Hellinger to TV distance in (b) is lossy as well since the TV distance between two Bernoulli distributions loses all local curvature information. Nevertheless, we see that our general framework is able to capture the qualitative aspects of this problem which arise from a problem-specific analysis.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Hellinger Localization Framework", "weight": 1.0} -->

Previously in Section 3.3, we saw a specific example of how 3.9 was combined with 3.6 to establish non-asymptotic rates for MLE which exhibit nearly optimal CLT scaling from (3.3). In this section, we will utilize these two results to provide a general recipe, which we call the *Hellinger localization framework*, for establishing rates. Importantly, our framework in addition to being general purpose, does not inherently rely on any mixing, ergodicity, or stationarity properties of the process $z_{1:T}$, but instead relies on the presence of multiple independent trajectories to allow us to learn from possibly non-stationary and/or non-mixing processes. Before we present the main framework, we introduce a key identifiability condition which plays an important role.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Remark 3.12 (Single-step Hellinger Identifiability)", "weight": 1.0} -->

One simple method we utilize to obtain sub-optimal---but *problem specific*---Hellinger identifiability (cf. 3.11. ‣ 3.4 Hellinger Localization Framework ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) constants is through the use of the *data processing inequality* (DPI) for $f$-divergences. Suppose that $z_{1}\sim\rho_{1}$ for all $\theta\in\Theta$. Then we have: where the equality holds from \[39, Prop. 7.2\] and the inequality is the DPI for $f$-divergences \cf. [39, Thm. 7.4\]. While the inequality above is often lossy, it is in practice often much easier to prove identifiability using the single-step distributions, i.e., We will show several examples of this in the sequel.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Remark 3.12 (Single-step Hellinger Identifiability)", "weight": 1.0} -->

The remainder of this paper is dedicated to realizing the Hellinger localization framework on a diverse set of estimation problems, which we turn to in Section 4.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Case Studies", "weight": 1.0} -->

This section contains the four multi-trajectory parameter recovery with ERM case studies that we consider in this work: (i) a mixture of two-state Markov chains (Section 4.1), (ii) a linear regression from dependent covariates setup with general (i.e., non-Gaussian) product-noises (Section 4.2), (iii) a GLM setup with a non-expansive, non-monotonic activation function (Section 4.3), and (iv) a simple linear-attention sequence model (Section 4.4). The problem setup and analysis for each case study is fairly self-contained, and can be read in any order.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Mixture of Two-State Markov Chains", "weight": 1.0} -->

We build on the example from Section 3.3 by considering the following mixture formulation. Suppose we have two Markov chains $M^{}$, $M^{}$, and a Bernoulli distribution $P$ on $\{0,1\}$. The generative process we consider proceeds by first sampling $B\sim P$ and $z_{1}\sim\rho_{1}$ independently, and then generating $z_{t+1}\mid z_{t},B$ from $M^{(B)}_{z_{t},z_{t+1}}$. The goal is to recover the parameters for the two Markov chains $M^{}$, $M^{}$ given $m$ trajectories of length $T$ from this process ($\mathcal{D}_{m,T}$), where $B^{(i)}$ is unobserved for each trajectory $i$. Such a problem is a special case of learning from mixtures of Markov chains.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Mixture of Two-State Markov Chains", "weight": 1.0} -->

Our motivation for studying this problem is two-fold: (a) the parameters of both Markov chains clearly cannot be learned in a single-trajectory setting, necessitating a multi-trajectory approach, and (b) the trajectory process $\{z_{t}\}$ is *not* $\alpha$-mixing, but we can still apply the Hellinger localization framework to derive sharp rates directly for the MLE.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Mixtures are not $\\alpha$-mixing", "weight": 1.0} -->

We give a short argument illustrating the lack of $\alpha$-mixing for the process $\{z_{t}\}$. We fix a $p_{\theta}\in\mathcal{P}$ with $\theta_{0}\neq\theta_{1}$. First, we recall the definition of $\alpha$-mixing and introduce some notation. For $a\leqslant b$, we let $z_{a:b}=(z_{a},\dots,z_{b})$, and we let $\sigma(z_{a:b})$ denote the $\sigma$-algebra generated by the subsequence $z_{a:b}$. The $\alpha$-mixing coefficients are defined as (cf. \[8, Eq. 2.2\], \[9, Def. 2.2\]): The process $\{z_{t}\}$ is denoted $\alpha$-mixing if $\alpha(k)\to 0$ as $k\to\infty$.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Mixtures are not $\\alpha$-mixing", "weight": 1.0} -->

We consider $\alpha$-mixing in this section, as it is the *weakest* notion of dependency used in the literature; in particular it is known that $\psi$-mixing $\phi$-mixing $\beta$-mixing $\alpha$-mixing, and furthermore $\rho$-mixing $\alpha$-mixing as well.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

Although $\{z_{t}\}_{t=1}$ is not $\alpha$-mixing, it is ergodic as $M^{}$ and $M^{}$ admit the same stationary distribution, which implies any time average of single trajectory will converge to the same marginal expectation. In general, the mixture of Markov chain process will be non-ergodic and non-mixing as long as the candidate transition matrices have different stationary distributions.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

We remark that mixing coefficients are not fully standardized in the literature, and depending on what specific definition is adopted, the trajectory $\{z_{t}\}$ could be considered mixing. As a specific example, in a weaker definition of $\beta$-mixing is considered, defined as $\beta(k)=\sup_{t\geqslant 1}\mathbb{E}_{z_{1:t}}[\lVert\mathbb{P}_{z_{t+k}}(\cdot\mid z_{1:t})-\mathbb{P}_{z_{t+k}}(\cdot)\rVert_{\mathrm{TV}}]$. Under this definition $\{z_{t}\}$ is actually $\beta$-mixing, since the $M^{(i)}$'s admit the same stationary distribution. However, there are many ways to modify the mixture model (4.1) so that it is not $\beta$-mixing under this more relaxed definition.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

A simple modification is where $\theta_{i}^{\prime}=\theta_{i}+\tau$ (modulating by one if necessary), where $\tau$ is a fixed offset. Another option is to consider general two-state Markov chains (so that $\theta$ contains four total parameters). For both modifications, the structure of the proof to be presented remains the same, although the detailed calculations may be different, especially for the general two-state parameterization.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

Towards stating our main result, we define the following quantities for $\theta\in^{2}$: The following is our main parameter recovery bound for the mixture of Markov chains problem.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Comparison to existing results", "weight": 1.0} -->

Learning mixture of Markov chains has been recently studied by a few authors. From this set of works, most related to ours is, where the authors develop efficient algorithms for clustering and estimating the family of transition matrices.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Comparison to existing results", "weight": 1.0} -->

Adapted to our specific setting, \[59, Theorem 4\] reads that when: then their algorithm recovers an estimate $\hat{\theta}_{m,T}$ that satisfies with probability at least $1-\delta$: We note that although the result from has less stringent requirements on both the minimum number of trajectories $m$ and trajectory length $T$ compared with 4.3, the final rate (4.4) has both (i) a $1/(mT^{2/3})$ scaling in comparison to a $1/(mT)$ scaling in (4.3), and (ii) also scales proportion to $\tau_{\mathrm{mix}}^{2/3}$ as opposed to $\bar{\sigma}^{2}(\theta)$ in (4.3); note that in general $\tau_{\mathrm{mix}}$ can grow arbitrarily large as $\theta$ approaches the boundary of the positive orthant, whereas $\bar{\sigma}^{2}(\theta)\leqslant

<!-- chunk {"id": "body-0113", "role": "body", "section": "Comparison to existing results", "weight": 1.0} -->

On the other hand, as mentioned previously, the work provides an efficient algorithm which can also learn the distribution of the latent variable $B$, whereas our result 4.3 uses the MLE estimate which, in this case, requires maximizing a non-concave objective and does not handle the case where the distribution of $B$ must be jointly learned. Extensions of our analysis to more general mixture setups, in addition to practical algorithms such as expectation maximization, is left as interesting future work. In Section 4.1.3, we comment in more detail on how our proof techniques may be generalized to other mixture recovery problems.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Preliminary Results for 4.3", "weight": 1.0} -->

Our analysis resembles that of the two-state Markov chain case (cf. Section 3.3), given that each trajectory can be associated with a particular chain if the trajectory length $T$ is sufficiently long. In the following, we state a few auxiliary results that will be crucial towards enabling our analysis.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Remark 4.5", "weight": 1.0} -->

We note that one could get a similar result by applying \[63, Theorem 3.9\]. However, our requirement on $T$ from the above lemma does not depend linearly on the inverse spectral gap $\asymp[\min\{\theta_{i},1-\theta_{i}\}]^{-1}$ of the chain defined by individual $\theta_{i}$'s.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Remark 4.10 (On identifiability up to permutation)", "weight": 1.0} -->

We note that picking a uniform distribution for $B$ illustrates one key issue in mixture models, where we can only identify parameters up to a permutation. Therefore we have to assume some additional distinguishability between parameters (e.g., the restricted subset $\Theta_{+}$) to guarantee unique identifiability. We discuss this issue in more detail in Section 4.1.3.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Covering Number Bound", "weight": 1.0} -->

We first compute an upper bound $\mathcal{I}_{\max}$ such that $\mathcal{I}(\theta)\preccurlyeq\mathcal{I}_{\max}$ for all $\theta\in\Theta$.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Covering Number Bound", "weight": 1.0} -->

Applying C.2 and recall the related computation in 4.8, specifically (4.11), we have: Hence, we have for all $\theta\in\Theta$: Consequently, for any $\theta,\theta^{\prime}\in\Theta$, Therefore we can upper bound the metric entropy We now first apply 3.6 (a) with resolution $\varepsilon=\delta/(2\sqrt{2m})$, which yields an event $\mathcal{E}_{1}$ with probability at least $1-\delta$, where on $\mathcal{E}_{1}$: where the last inequality follows from by assumption, $m\geqslant 4$, and the observation For the remainder of the proof, we will assume we are on the event $\mathcal{E}_{1}$. Invoking the Hellinger identifiability (4.9) and A.1.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Covering Number Bound", "weight": 1.0} -->

‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"): We can now additionally impose (cf. A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) where $c$ is some constant radius.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Parameter error bound", "weight": 1.0} -->

Our first step is to define a more refined $\mathcal{I}_{\max}^{\prime}$ for $\theta\in\Theta^{\prime}$. From 4.8, for any $\theta\in\Theta^{\prime}$: Hence, following (3.40) using $\mathcal{I}_{\max}^{\prime}$ instead of $\mathcal{I}_{\max}$, we obtain that: where recall that the last inequality is from (4.23). Therefore, combining the above inequality with (4.30) and A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), condition (3.22. ‣ Proposition 3.9.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Parameter error bound", "weight": 1.0} -->

‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds if in addition to (4.26) and (4.27) we also have: Applying 3.9 (a), we obtain from (3.23. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")): Furthermore, from (4.28),

<!-- chunk {"id": "body-0122", "role": "body", "section": "Verify FI radius", "weight": 1.0} -->

For the variance-weighted CLT rate, we want to show the FI radius condition (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")). By combining C.4 and (4.28), we have for any $\theta\in\Theta^{\prime}$, Hence condition (3.24. ‣ Proposition 3.9.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Verify FI radius", "weight": 1.0} -->

‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) is implied: Now recall from the error decomposition in (4.9), we have By triangle inequality, a further sufficient condition is: From Section 3.3, specifically, (3.34), we have that (4.34) can be satisfied by requiring and in view of (4.32) and A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), this holds if: This condition is however already implied by (4.31) (up to adjusting constant factors). We now address condition (4.35).

<!-- chunk {"id": "body-0124", "role": "body", "section": "Verify FI radius", "weight": 1.0} -->

Recalling $\mathcal{I}_{\operatorname*{\mathsf{diag}}}(\theta)\succcurlyeq(T-1)\cdot I_{2}$, we have: where (a) uses C.4, (b) uses (4.20) from the proof of 4.8, and (c) uses (4.21), and (d) uses the requirement on $T$ from (4.27) (possibly adjusting constant factors as necessary), and follows the arguments bounding $\zeta$ in (4.20) from 4.8.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Final result", "weight": 1.0} -->

We now have the necessary requirements to invoke 3.9 (b) to conclude: In particular, combined with 4.8, this also implies We conclude by summarizing the requirements on $m,T$. In total, we require conditions (4.26), (4.27), and (4.31) to hold. These are readily simplified into assumptions (b) and (c) in the theorem statement, from which the result follows.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Extensions of Proof Techniques to More General Mixture Problems", "weight": 1.0} -->

We now discuss the extent to which the proof strategy for Section 4.1 extends to general mixture distributions.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Extensions of Proof Techniques to More General Mixture Problems", "weight": 1.0} -->

We require the weights $f_{k}$ to be in the strict interior for regularity (e.g., differentiability and exchanging derivatives with integrals) reasons. The data-generating process we consider proceeds similarly to what we considered in Section 4.1. Specifically, a latent variable $B\in[k]$ is first drawn according to $\{f_{i}\}_{i=1}^{k}$, which is then used condition the data $z_{1:T}\sim p_{\theta_{B}}$.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Mixture with known weights", "weight": 1.0} -->

For Step 2 onward, we inspect $w_{\theta}^{(i)}(z_{1:T})$: Ideally, each component of the mixture should be identifiable from the others given long enough trajectories.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Mixture with known weights", "weight": 1.0} -->

Hence, a natural assumption is that when $B=i$ (i.e., $z_{1:T}\sim p_{\theta_{i}}$), for any $j\neq i$ the following ergodic condition holds: there exists some constant $\Delta_{ij}>0$ such that The immediate implication of (4.39) is that when $B=i$: On a flip side, when $B=k\neq i$, we have: Since $w_{\theta}^{(i)}(z_{1:T})\geqslant 0$, we have $w_{\theta}^{(i)}(z_{1:T})\overset{T\to\infty}{\leftrightline\mathrel{\mkern-3.1mu}\rightarrow}0$ a.s. when $B=k\neq i$.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Mixture with known weights", "weight": 1.0} -->

To see why this implies (4.39), observe that $\pi_{\theta_{i}}\otimes p_{\theta_{i}}$ is the density of the ergodic measure of the augmented process $\{(z_{t},z_{t+1})\}_{t=1}$ under $p_{\theta_{i}}$. Hence the right hand side of (4.41) reads: Following (4.40), we can again argue that for large $T$, the Hessian (and therefore the Fisher information) can be controlled by a block-diagonal matrix of the mixture components' Fisher information matrices under the Loewner order.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Mixture with known weights", "weight": 1.0} -->

Some remarks are in order. First, for an exact analogue of 4.8, we need to prove the Loewner order equivalence holds uniformly within a ball around $\theta$. Our previous proof strategy requires characterizing non-asymptotic mixing behavior instead of the asymptotic convergence as in (4.39). In particular, if we are working with a Markov process and consider the augmented process $\left\{(z_{t},z_{t+1})\right\}_{t=1}$ with an ergodic measure denoted by $\pi$, we expect the following Bernstein-type inequality to hold:^1010^10Here we only stated a schematic form. More precisely, under various mixing conditions, the right hand side might include additional $\operatorname*{polylog}(T)$ factors. where $C(\mathcal{H})$ typically quantifies boundedness of the function class $\mathcal{H}$. Such results are available for various classes of mixing processes (see e.g.,).

<!-- chunk {"id": "body-0132", "role": "body", "section": "Mixture with known weights", "weight": 1.0} -->

In particular, stable LDS are geometrically $\beta$-mixing, and therefore \[66, Theorem 1 and 2\] are readily applicable. Specialized bounds for Markov chains are also available \see e.g., [71, Theorem 2.4\]. This would allow us to obtain instance-optimal rates for the more general mixture dynamics, including but not limited to those considered in prior art (e.g.,).

<!-- chunk {"id": "body-0133", "role": "body", "section": "Mixture with known weights", "weight": 1.0} -->

Second, we face the technical challenge that Hellinger identifiability (analogue of 4.9) does not in general hold when a subset of weights are equal. In the scalar case, as in 4.9, we worked around this issue by assuming a monotone order on the corresponding parameters to guarantee unique identifiability of parameters. In the general case, we need to redefine the notion of Hellinger identifiability to be symmetry aware.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Mixture with known weights", "weight": 1.0} -->

Next, let $\mathsf{Sym}_{\mathcal{J}}(\theta)$ denote the set of cardinality $\tprod\slimits@_{i=1}^{\ell}(|\mathcal{J}_{i}|!)$ which given a parameter vector $\theta\in\Theta^{k}$ enumerates all possible permutations within each equivalence class for $\theta$. We then consider the following modified definition of Hellinger identifiability (cf. 3.11. ‣ 3.4 Hellinger Localization Framework ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), which states that there exists $(\gamma_{1},\gamma_{2})$ such that: We note the above symmetrized condition needs to be shown on a problem-specific basis.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Mixture with known weights", "weight": 1.0} -->

We conclude by remarking that under the particular outline above, it seems necessary to require ergodicity of mixture *components* to obtain non-trivial results, as otherwise the behavior of Fisher information is difficult to analyze. However, we do know that, for example, LDS with non-mixing behavior can still be identified with parametric rate from a single trajectory and so we postulate that e.g., identifying mixtures of LDS may also be possible without mixing assumptions. This reflects a limitation for our current instantiation of Hellinger localization for mixture recovery, which we leave addressing to future work.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Dependent Regression under General Product-Noise Distributions", "weight": 1.0} -->

We next consider the following family of trajectory distributions $p_{\theta}(z_{1:T})$ over $\mathsf{Z}=\mathbb{R}^{d}$ parameterized by $\theta\in\Theta$ of the following form: Here, the matrix-valued map $M:\mathbb{R}^{d}\mapsto\mathbb{R}^{d\times p}$ is allowed to be non-linear, and assumed to be known. This setup generalizes the linear system identification problem detailed in Section 3.1 and has received considerable attention recently as a tractable form of non-linear system identification, especially when a control input is added to the matrix $M$, i.e., $z_{t+1}=M(z_{t},u_{t})\theta+w_{t}$ (see e.g.,); a more detailed literature review is given in Section 4.2.1. The noise variable $w_{t}$ is drawn independently across time $t$ from a distribution which has the following product density w.r.t.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Dependent Regression under General Product-Noise Distributions", "weight": 1.0} -->

the Lebesgue measure on $\mathbb{R}^{d}$: where $\phi:\mathbb{R}\mapsto\mathbb{R}$ is a known scalar function parameterizing the noise distribution. Hence, our setup differs from more standard settings in the following way: we do not need to assume the noise is either Gaussian or sub-Gaussian, but the functional form of the density is needed to solve the MLE. In what follows, given a vector $w\in\mathbb{R}^{d}$, we let $\bm{\phi}$ denote the function mapping $\mathbb{R}^{d}\mapsto\mathbb{R}^{d}$ defined as $\bm{\phi}(w):=(\phi(w_{1}),\dots,\phi(w_{d}))$. With this notation, we can write the MLE (3.1) for (4.46) as: We assume the following regularity conditions on $\phi$.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Example 4.12 (Multivariate normal distribution)", "weight": 1.0} -->

satisfies the conditions in 4.11. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") with $\sigma^{2}_{\phi_{\nu}}=\nu^{2}$ and $(\beta_{1},\beta_{2})=$.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Example 4.13 (Smoothed \"Bang-Bang\" noise)", "weight": 1.0} -->

This corresponds to $p_{\phi_{\nu}}=\frac{1}{2}\mathsf{N}(1,\nu^{2})+\frac{1}{2}\mathsf{N}(-1,\nu^{2})$, a Gaussian mixture model with two $\nu^{2}$ variance mixtures centered as $\pm 1$. If $\nu\in$, then $\phi_{\nu}$ satisfies the conditions in 4.11. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") for $(\beta_{1},\beta_{2})=(c^{\prime}/\nu^{6},c^{\prime\prime}/\nu^{24})$, where $c^{\prime},c^{\prime\prime}$ are universal positive constants.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Example 4.14 (Smoothed Laplace distribution)", "weight": 1.0} -->

Let us define $\phi$ as: As $c\to\infty$, we have that $\phi_{c,\nu}(x)\to|x/\nu|$ pointwise, so $p_{\phi_{c,\nu}}$ is a smoothed Laplace distribution with second-order curvature. Define $Z(c):=\int\cosh(cx)^{-1/c}\mathrm{d}x$. We have that $\phi_{c,\nu}$ satisfies the conditions of 4.11. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") for $(\beta_{1},\beta_{2})=\left(\frac{2c}{\tanh^{2}(cZ(c)/4)},\frac{16}{\tanh^{8}(cZ(c)/4)}\right)$.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Example 4.14 (Smoothed Laplace distribution)", "weight": 1.0} -->

With the data generating process $p_{\theta}(z_{1:T})$ in place, we now turn to the analysis of the MLE estimator in this model. We remark that the MLE estimator (4.48) in general for this problem is *not* the solution to a least-squares regression problem (unless $p_{\phi}$ is Gaussian), nor is it generally the solution to convex optimization problem (unless $\phi$ is convex). Furthermore, as seen in 4.14. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), the noise does not necessarily have sub-Gaussian tails as well, as is the standard assumption in many dependent learning works (e.g., ), although we note that some works have also considered heavier-tailed noise in various settings. The following is our main result regarding parameter recovery for the model (4.46).

<!-- chunk {"id": "body-0142", "role": "body", "section": "Linear Dynamical System Identification", "weight": 1.0} -->

The LDS system identification problem reviewed in (3.5) is a special case of the model (4.46), with $p=d^{2}$, $\theta=\mathrm{vec}(A)$, and $M(z)=(z^{\mathsf{T}}\otimes I_{d})$. Hence 4.15 can be thought of as a generalization of the results from for multi-trajectory learning in LDS. However, there are some caveats/limitations to the extent that 4.15 truly generalizes the result.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Linear Dynamical System Identification", "weight": 1.0} -->

Focusing on Assumption (c), we have that $\lVert M(z)\rVert_{\mathrm{op}}=\lVert(z^{\mathsf{T}}\otimes I_{d})\rVert_{\mathrm{op}}=\lVert z\rVert$, and hence Assumption (c) posits a uniform bound on the quantity $\chi(\theta):=\frac{1}{T^{\prime}}\tsum\slimits@_{t=1}^{T^{\prime}}\mathbb{E}_{p_{\theta}}[\lVert z_{t}\rVert^{8}]$ as $\theta$ varies over $\Theta$. However, the quantity $\chi(\theta)$ exhibits two phase-transitions depending on the operator norm of $\mathrm{mat}(\theta)$.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Linear Dynamical System Identification", "weight": 1.0} -->

When $\lVert\mathrm{mat}(\theta)\rVert_{\mathrm{op}}<1$, then $\chi(\theta)=O$ (ignoring all constants other than $T$) by the ergodic theorem. On the other hand, when $\lVert\mathrm{mat}(\theta)\rVert_{\mathrm{op}}=1$, then $\chi(\theta)=\mathrm{poly}(T)$. Finally, when $\lVert\mathrm{mat}(\theta)\rVert_{\mathrm{op}}=\rho>1$, we have $\chi(\theta)=\rho^{O(T)}$. In the last regime, the bound (4.49. ‣ Theorem 4.15.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Linear Dynamical System Identification", "weight": 1.0} -->

‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) becomes sub-optimal compared with (3.6), and ends up scaling as $1/m$ instead of the optimal $1/(mT)$. Furthermore, in the $\lVert\mathrm{mat}(\theta)\rVert_{\mathrm{op}}=1$ regime, the requirement on $m$ becomes $m\gtrsim\mathrm{poly}(T)$, which is also not sharp. Thus, for LDS system identification, (4.46) is only sharp in the case when $R<1$.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Linear Dynamical System Identification", "weight": 1.0} -->

It is important to clarify that the main issue is not that the Hellinger framework requires stability/mixing of the process $z_{1:T}$, but instead the issue is that for LTI systems, the states $z_{t}$ can easily grow exponential in $T$ depending on the parameter $A$, which makes both covering and localization arguments extremely sensitive to minor perturbations in the parameters. The situation for LDS can be somewhat reconciled by utilizing a closed-form lower bound for the trajectory-level Hellinger distance \[56, Section 4\], which would address the sub-optimal $m\gtrsim\mathrm{poly}(T)$ requirement when $R=1$. However, when $R>1$, this strategy would still not yield the correct rates, as we would still need to perform a covering argument under the hood.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Linear Dynamical System Identification", "weight": 1.0} -->

In the least-squares analysis, the issue of uniform convergence when $A$ is not stable is handled elegantly via the special structure of the square loss. In particular, the square loss lends itself to an *offset basic inequality* which allows the uniform convergence to be *self-normalized*, preventing unstable $A$'s from adversely affecting the resulting covering numbers. We leave to future work a generalized form of self-normalization that can also be applied to log losses and the Hellinger framework. One possible starting point for this extension is the work of, which provides techniques to define and analyze offset empirical processes for logarithmic, and more generally exp-concave losses.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Non-linear System Identification", "weight": 1.0} -->

In its general form, problem (4.46) is typically studied in its controlled variant, i.e., $z_{t+1}=M(z_{t},u_{t})\theta+w_{t}$, where $z_{t}$ is interpreted as the state of a discrete-time dynamical system, and $u_{t}$ the control input at time $t$. We note that 4.15 for identifying the model (4.46) can be readily translated into this control setting with some minor modifications to incorporate the expectation over the control sequence $u_{t}$ in the Fisher information matrix, and also to include the full map $M(z_{t},u_{t})$ in the definitions for $M_{1},M_{2}$ in Assumptions (b), (c); we omit the exact result in the interest of space.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Non-linear System Identification", "weight": 1.0} -->

Learning in the controlled formulation of (4.46) is studied mostly as an active learning problem, with a focus on designing optimal algorithms for selecting inputs; the necessity of active learning in the single-trajectory setting, absent smoothness conditions on $M(z,u)$, was demonstrated. The line of work from considers task-guided exploration, proposing an algorithm that quantifies which system parameters are most relevant to solving the task, and actively explores to minimize uncertainty in these parameters, achieving a near instance-optimal rate for the downstream task; this was later extended by to general parameteric dynamics models. Extending our Hellinger localization framework for active exploration, especially for downstream control tasks, is exciting future work.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Non-linear System Identification", "weight": 1.0} -->

Perhaps the most directly related work is that of, which shows that the feature map $M$ being real-analytic is sufficient to allow *non-active* i.i.d. random control signals to suffice for parameter recovery. Their arguments proceed by showing that since the zeros of the real-analytic function have measure zero, this implies that the standard martingale small-ball conditions (cf. ) used to show a lower bound on the empirical covariance matrix hold generically. This idea is also applicable to our framework, and can be used to certify non-degeneracy of the Fisher information matrix as required by Assumption (e) in 4.15 for real-analytic feature maps.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Covering number bound", "weight": 1.0} -->

Using this notation, we compute the gradient and Hessian of the log probability as: Consequently, we see that where the last equality utilizes the IBP identity $\mathbb{E}_{w\sim p_{\phi}}[\phi^{\prime\prime}(w)]=\mathbb{E}_{w\sim p_{\phi}}[(\phi^{\prime}(w))^{2}]$ from 4.16. Furthermore, we can construct a uniform bound $\mathcal{I}_{\max}$ using the definition of $\bar{\mu}$: Therefore we have an upper bound for the metric entropy under the max-FI divergence: From 3.6, with probability at least $1-\delta$, Hence by the arguments outlined in (3.42) combined with A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), as long as then whenever (4.50) holds, we have Call this event $\mathcal{E}_{1}$.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Covering number bound", "weight": 1.0} -->

Furthermore, since the log-likelihood of $z_{1:T}$ for $\theta\in\Theta$ can be written as: where $\mathrm{const}$ does not depend on $\theta$, when $\phi$ is convex, then $\mathcal{P}$ is log-concave (cf. 3.5). It is not hard to see that $\mathrm{diam}(\Theta)=2RT\bar{\mu}$. Hence from 3.6, with probability at least $1-\delta$, Call this event $\mathcal{E}_{1,\mathrm{cvx}}$.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Estimate $B_{1}$ and $B_{2}$", "weight": 1.0} -->

Next, we compute: Now since $\mathbb{E}_{w\sim p_{\bm{\phi}}}[\phi^{\prime}(w_{j})\phi^{\prime}(w_{k})]=(\mathbb{E}_{w\sim p_{\phi}}[\phi^{\prime}(w)])^{2}=0$ for $j,k\in[d]$ with $j\neq k$ by coordinate-wise independence of $p_{\bm{\phi}}$ and 4.16, we have that Now let us focus on $\mathbb{E}[d_{t}^{4}]$: where the penultimate inequality follows from Hölder's inequality, and the last inequality follows from 4.11. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization").

<!-- chunk {"id": "body-0154", "role": "body", "section": "Estimate $B_{1}$ and $B_{2}$", "weight": 1.0} -->

Hence, Now we will set $v=\mathcal{I}(\theta)^{-1/2}\bar{v}$ where $\bar{v}\in\mathbb{S}^{p-1}$ is a unit test vector; hence $\lVert v\rVert\leqslant\sqrt{\sigma^{2}_{\phi}/(\underline{\mu}T)}$. By Rosenthal's inequality for MDS (A.6. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), we have: where the last inequality holds from Assumption (f). Hence we have We next focus on $B_{2}$. We first fix a vector $q\in\mathbb{R}^{d}$, and observe that where the last inequality holds from 4.11.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Estimate $B_{1}$ and $B_{2}$", "weight": 1.0} -->

‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") and the IBP identity (cf. 4.16) $\mathbb{E}_{w\sim p_{\theta}}[\phi^{\prime\prime}(w)]=\mathbb{E}_{w\sim p_{\theta}}[(\phi^{\prime}(w))^{2}]=\sigma_{\phi}^{-2}$. Hence fixing a test vector $v\in\mathbb{R}^{p}$, we have Now again we choose $v=\mathcal{I}(\theta)^{-1/2}\bar{v}$ for a unit norm $\bar{v}\in\mathbb{R}^{p}$. We then have Altogether, we can bound

<!-- chunk {"id": "body-0156", "role": "body", "section": "Parameter error bound", "weight": 1.0} -->

We first cover the case where $\phi$ is not convex. Combining (4.52), (4.54), and A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), as long as $m$ satisfies (4.51) and also then condition (3.22. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds on $\mathcal{E}_{1}$. Hence from 3.9, combining (3.23. ‣ Proposition 3.9.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Parameter error bound", "weight": 1.0} -->

‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) with (4.52), we have on $\mathcal{E}_{1}$: We now turn to the case where $\phi$ is convex. Combining (4.53), (4.54), and A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), we see that if $m$ satisfies: Hence from 3.9, combining (3.23. ‣ Proposition 3.9.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Parameter error bound", "weight": 1.0} -->

‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) with (4.53), we have on $\mathcal{E}_{1,\mathrm{cvx}}$,

<!-- chunk {"id": "body-0159", "role": "body", "section": "Verify FI radius", "weight": 1.0} -->

In order to verify the FI radius condition (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), we will make use of A.3. Fix $\theta_{1},\theta_{2}\in\Theta$ and a unit norm $v\in\mathbb{S}^{p-1}$. We have the following: where (a) follows from A.3 and (b) follows from Jensen's inequality. Hence by the variational characterization of operator norm, for any $\theta\in\Theta$: Hence from (4.52) and A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), as long as $m$ satisfies (4.51), (4.55), and then the FI radius condition (3.24.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Verify FI radius", "weight": 1.0} -->

‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds on $\mathcal{E}_{1}$. On the other hand when $\phi$ is convex, from (4.53) and A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), as long as $m$ satisfies (4.56) and: then the FI radius condition (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds on $\mathcal{E}_{1,\mathrm{cvx}}$.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Verify FI radius", "weight": 1.0} -->

The result for both cases now follows from 3.9, specifically (3.25. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")).

<!-- chunk {"id": "body-0162", "role": "body", "section": "Non-Monotonic Sinusoidal GLM Dynamics", "weight": 1.0} -->

For our next setup, we consider the following generalized linear model (GLM) of dynamics, given parameters $A\in\mathbb{R}^{d\times d}$, where $\sin(\cdot)$ is overloaded to apply component-wise given a vector input, and $w_{t}$ is drawn independently across time. While more general GLM dynamics $z_{t+1}=\phi(Az_{t})+w_{t}$ have been studied in the literature in the context of system identification, the specific sinusoidal GLM we consider is more challenging as it is an instance of a *non-monotonic*, *non-expansive*^1111^11An activation function $\phi(x)$ is *expansive* if there exists a $\zeta>0$ such that $|\phi(x)-\phi(y)|\geqslant\zeta|x-y|$ for all $x,y\in\mathbb{R}$. activation function.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Non-Monotonic Sinusoidal GLM Dynamics", "weight": 1.0} -->

Furthermore, we do not impose any stability assumptions on the $A$ matrix in (4.58), as is done in prior works. The following theorem is our main result for parameter recovery in this model. In the following result, we let $\hat{\theta}^{\varepsilon}_{m,T}=\mathrm{vec}(\hat{A}^{\varepsilon}_{m,T})$ and $\theta=\mathrm{vec}(A)$.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Comparison to existing results", "weight": 1.0} -->

To the best of our knowledge, this is the first rate for parameter recovery in any GLM dynamics model in the multi-trajectory setting, which obtains a nearly instance-optimal rate of $\tilde{O}(d^{2}/(mT))$.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Comparison to existing results", "weight": 1.0} -->

The previous sharpest rate for this problem utilizes the fact that the MLE $\hat{\theta}_{m,T}$ for this problem involves solving a realizable, parametric least-squares ERM problem, and hence the reduction described in Section 3.1 to the result of would provide a similar bound on the *excess risk*, but not the weighted parameter error directly; as described in Section 3.1, however, without verification of the weakly sub-Gaussian condition specifically for the function class $\{\sin(A_{1}x)-\sin(A_{2}x)\mid A_{1},A_{2}\in\Theta\}$ (which to the best of our knowledge has not been shown in the literature), the best burn-in requirement on $m,T$ that this reduction can provide depends exponentially on the process dimension $d$.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Comparison to existing results", "weight": 1.0} -->

On the other hand, 4.17 requires that both $m\gtrsim\mathrm{poly}(d)\cdot T$ and $T\gtrsim\mathrm{poly}(d)$ requirement; while it is likely that our exact polynomial dependence is not optimal, we are able to break the exponential in $d$ barrier of existing results.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Comparison to existing results", "weight": 1.0} -->

In the single-trajectory setting, several recent works have explicitly studied parameter recovery for GLM dynamics. However, the specific setting (4.58) we consider does not satisfy the requisite assumptions for any of these works, and hence these works cannot be used as a basis for reduction. To start, the works all assume a model class with a 1-Lipschitz monotonic activation function $\phi$, with fast rates further requiring $\phi$ to be expansive. The $\sin$ function only satisfies the $1$-Lipschitz requirement; the bounded and oscillatory nature of $\sin$ violates the other assumptions. The work requires a one-point convexity assumption on the population loss, which is challenging to verify; they are only able to verify their condition assuming uniformly monotonic activations (i.e., $\phi^{\prime}\geqslant\zeta>0$).

<!-- chunk {"id": "body-0168", "role": "body", "section": "Comparison to existing results", "weight": 1.0} -->

Regarding stability of $A$, additionally assume Lyapunov stability conditions, specifically that there exists a diagonal positive definite $K$ and scalar $\rho<1$ such that $AKA\preccurlyeq\rho\cdot K$; however, it is immediately obvious that this does not hold in our setting as we permit $A=c\cdot I_{d}$ for $c>1$, which would require $\rho\geqslant c^{2}>1$. This also violates the explicit assumption made in some works that $\lVert A\rVert_{\mathrm{op}}<1$.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Comparison to existing results", "weight": 1.0} -->

Other works such as made explicit exponential regularity assumptions on the trajectories that given a noise sequence $\{w_{t}\}_{t=1}^{T-1}$, the difference in states from two initial states will expand at most by a factor of $\rho=1+O(1/T)$ every timestep; however, this is also violated in our setting.^1212^12Concretely, our setup does not satisfy \[27, Assumption 4\] for any $\rho\leqslant 1+O(1/T)$, as we now show. Let $\Phi_{t}(z)$ denote the value of $z_{t}$ following the dynamics $z_{t+1}=\sin(2z_{t})$ starting at $z_{1}=z$.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Hellinger identifiability for sinusoidal GLMs", "weight": 1.0} -->

Before we turn to applying the Hellinger localization framework to this problem, we discuss the main technical challenge: absent the strict monotonically increasing activation function assumption $\phi^{\prime}(x)\geqslant\gamma>0$, establishing both that (a) $\mathcal{I}(\theta)\succcurlyeq\Omega(T)\cdot I_{d^{2}}$ and that (b) $\mathrm{d}_{H}^{2}(\hat{p}^{\varepsilon}_{m,T},p)\leqslant\gamma^{2}$ implies $\lVert\hat{\theta}^{\varepsilon}_{m,T}-\theta\rVert^{2}\lesssim\gamma^{2}$ (i.e., Hellinger identifiability (3.11.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Hellinger identifiability for sinusoidal GLMs", "weight": 1.0} -->

‣ 3.4 Hellinger Localization Framework ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"))) becomes substantially more challenging. A key step towards establishing identifiability is to show the bound $\gamma^{2}:=\mathbb{E}_{z\sim\mathsf{N}(0,\sigma^{2}I_{d})}[(\sin(\langle u_{1},z\rangle)-\sin(\langle u_{2},z\rangle))^{2}]\gtrsim\sigma^{2}\lVert u_{1}-u_{2}\rVert^{2}$ when $\gamma^{2}$ is sufficiently small. We believe this result, which is detailed in Appendix D, to be of independent interest, and may be helpful in e.g., analyzing neural networks with sinusoidal activation functions.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Hellinger identifiability for sinusoidal GLMs", "weight": 1.0} -->

We remark that a similar bound is shown for ReLU activations in \[38, Lemma 11\], in particular for $z\sim\mathsf{N}(\mu,\sigma^{2}I_{d})$, $\mathbb{E}_{z}[(\mathrm{ReLU}(\langle u_{1},z\rangle)-\mathrm{ReLU}(\langle u_{2},z\rangle))^{2}]\geqslant\frac{\sigma^{2}}{4}e^{-\|\mu\|^{2}/\sigma^{2}}\|u_{1}-u_{2}\|^{2}$. A key difference is in how this style of result is used in our analysis versus. In our analysis, the Hellinger identifiability is only used for the first two timestep as noted in 3.12.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Hellinger identifiability for sinusoidal GLMs", "weight": 1.0} -->

‣ 3.4 Hellinger Localization Framework ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), and hence we only need to consider taking expectation over $z\sim\mathsf{N}(0,\sigma^{2}I_{d})$. On the other hand, proves identifiability at every timestep in order to relate parameter recovery error to average prediction error; hence their analysis is required to consider non-zero means $\mu$'s, leading to parameter error rates that have an $e^{d}$ dependence on the dimension in general (cf. \[38, Theorem 3\]).

<!-- chunk {"id": "body-0174", "role": "body", "section": "Step 1: Covering number bound", "weight": 1.0} -->

Define $h_{\theta}(z):=\sin(M(z)\theta)$ and its Jacobian w.r.t. $\theta$ $D_{\theta}h_{\theta}(z)=\operatorname*{\mathsf{diag}}(\cos(M(z)\theta))M(z)$ (similar to $\sin(\cdot)$, $\cos(\cdot)$ is also overloaded to apply component-wise given a vector input). We observe that Let us start with an upper bound. Since $\cos(x)^{2}\in$, we can see that $\operatorname*{\mathsf{diag}}(\cos^{2}(M(z_{t})\theta))\preccurlyeq I_{d}$.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Step 1: Covering number bound", "weight": 1.0} -->

Expanding $z_{t}=\mu_{t-1}+w_{t-1}$ for $\mu_{t-1}=h_{\theta}(z_{t-1})$ and observing that $\mathbb{E}[w_{t-1}]=0$, we can see: We fix a $v\in\mathbb{R}^{d}$ with unit norm, observe $\sin(x)^{2}\in$, and bound the outer product of $\mu_{t-1}$: Putting this all together gives the maximum eigenvalue of the Fisher information: We note that this is a parameter agnostic upper bound, and as such we can set $\mathcal{I}_{\max}=\frac{T}{\sigma^{2}}(d+\sigma^{2})\cdot I_{p}$.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Step 1: Covering number bound", "weight": 1.0} -->

By D.5 and the data processing inequality, for any $\theta\in\Theta$, This shows that $\mathcal{P}$ is $(\gamma_{1},\gamma_{2})$-identifiable (cf. 3.11. ‣ 3.4 Hellinger Localization Framework ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) for constants: Our next step is to apply 3.6 to ensure that the LHS condition in (4.59) holds. To do this, we shall estimate the covering number of $\mathcal{P}$ in the max FI divergence through the $\ell_{2}$ covering number.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Step 1: Covering number bound", "weight": 1.0} -->

If we fix some $\theta\in\Theta$ and let $\theta^{\prime}$ denote its closest element in an $\varepsilon$-covering of $\Theta$ in $\ell_{2}$, This allows the relation We now apply 3.6 with $\varepsilon=\delta/(2\sqrt{2m})$ to conclude that with probability at least $1-\delta$: where $c_{0}$ is a universal positive constant. Call this event $\mathcal{E}_{1}$. If we define $1/\Phi_{0}:=\min\{1,1/\sigma^{2}\}$, plugging this bound into (4.59) and applying A.1.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Step 1: Covering number bound", "weight": 1.0} -->

‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") yields that if $m$ satisfies where $c_{0}^{\prime}$ is a universal constant, then the following also holds on $\mathcal{E}_{1}$: For what follows, we define the set A key property of $\Theta^{\prime}$ that we will utilize is that $\theta\in\Theta^{\prime}$ implies $\lVert\mathrm{mat}(\theta)[j]\rVert\geqslant\lVert\mathrm{mat}(\theta)[j]\rVert/2$ for all $j\in[d]$ by the triangle inequality.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Ensuring that $\\hat{\\theta}^{\\varepsilon}_{m,T}\\in\\Theta^{\\prime}$ on $\\mathcal{E}_{1}$", "weight": 1.0} -->

Using D.5 and (4.60), we have that if $m$ satisfies, then we have that $\hat{\theta}^{\varepsilon}_{m,T}\in\Theta^{\prime}$ on $\mathcal{E}_{1}$. Using A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), this holds whenever $m$ satisfies: where $c_{1}$ is another univeral constant. We can note that since $\Phi_{1}\geqslant\Phi_{0}$, this constraint automatically satisfies (4.61) (possibly after adjusting the value of $c_{1}$).

<!-- chunk {"id": "body-0180", "role": "body", "section": "Lower bound FI matrix", "weight": 1.0} -->

Our first task is to estimate a lower bound on the FI matrix for $\theta\in\Theta^{\prime}$. Recall the Fisher information from earlier: We can expand $z_{t}=\mu_{t-1}+w_{t-1}$ for $\mu_{t-1}=h_{\theta}(x_{t-1})$ to expand the dependency of the expectation on the previous timestep.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Lower bound FI matrix", "weight": 1.0} -->

We choose a $\nu_{0}$ to be specified later, and observe that by D.1 and a union bound, with $A=\mathrm{mat}(\theta)$ and $A[j]\in\mathbb{R}^{d}$ denoting the $j$-th row of $A$, Call this event, which depends on $\mu_{t-1}$, $\mathcal{E}_{\mu_{t-1}}$. Letting $A_{\min}:=\min_{j\in[d]}\lVert A[j]\rVert$, we now write: where the last equality follows from the bi-linearity of the Kronecker product. We now fix a $v\in\mathbb{R}^{d}$ with unit-norm, and observe, dropping subscripts on $t$ for clarity, where the last inequality holds by hyper-contractivity of Gaussian polynomials \see e.g., [86, Ch. 5\].

<!-- chunk {"id": "body-0182", "role": "body", "section": "Lower bound FI matrix", "weight": 1.0} -->

Hence we set $\nu_{0}=1/324$, from which we conclude Consequently, we have that Therefore, we conclude that: Up until this point, we have not used the assumption that $\theta\in\Theta^{\prime}$. Observe that $A_{\min}\geqslant A_{\star,\min}/2$ whenever $\theta\in\Theta^{\prime}$, we finally conclude that for $\theta\in\Theta^{\prime}$,

<!-- chunk {"id": "body-0183", "role": "body", "section": "Step 2: Estimating $B_{1}$ and $B_{2}$", "weight": 1.0} -->

We will estimate $B_{1}$ and $B_{2}$ over $\Theta^{\prime}$. We start with $B_{1}$. First, given a trajectory $z_{1:T}\sim p_{\theta}$, we have that Now fix a test vector $v\in\mathbb{R}^{d^{2}}$, and consider: A useful inequality is the following.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Step 2: Estimating $B_{1}$ and $B_{2}$", "weight": 1.0} -->

We next bound $\mathbb{E}[\lVert z_{t}\rVert^{4}]$ as: Using this bound, Since $\lVert w_{t}\rVert$ is a $\sigma$-sub-Gaussian random variable, we know that $\mathbb{E}[\lVert w_{t}\rVert^{8}]\lesssim\sigma^{8}d^{4}$. On the other hand, where the last inequality holds since we assume $T\gtrsim d^{2}$. Now we set $v=\mathcal{I}(\theta)^{-1/2}\bar{v}$ for a unit norm $\bar{v}$, we have that We now move to $B_{2}$. First we define the vector-valued function for a fixed $q\in\mathbb{R}^{d}$: The Jacobian of $g(\theta;z,q)$ is given: where denotes the Hadamard (entry-wise) product.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Step 2: Estimating $B_{1}$ and $B_{2}$", "weight": 1.0} -->

Now we have Hence, given a test vector $v\in\mathbb{R}^{d^{2}}$, given $z_{1:T}\sim p_{\theta}$, for all $t\in[T-1]$ we have: Now we set $v=\mathcal{I}(\theta)^{-1/2}\bar{v}$ for a unit norm $\bar{v}$, we have that Finally, we conclude that

<!-- chunk {"id": "body-0186", "role": "body", "section": "Step 3: Parameter error bound", "weight": 1.0} -->

Utilizing (4.62) and (4.65), we have that to verify the condition (3.22. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) for $\theta_{0}=\theta$ and $\theta_{1}=\hat{\theta}^{\varepsilon}_{m,T}$ on $\mathcal{E}_{1}$, we need $m$ to satisfy: by A.1.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Step 3: Parameter error bound", "weight": 1.0} -->

‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") it suffices for $m$ to satisfy: From (4.64), we have that on $\Theta^{\prime}$, the following lower bound $\inf_{\theta\in\Theta^{\prime}}\lambda_{\min}(\mathcal{I}(\theta))\gtrsim\frac{T}{d^{2}}\cdot\min\{1,\sigma^{2}A_{\star,\min}^{2}\}$ holds. Since (a) (3.22. ‣ Proposition 3.9.

<!-- chunk {"id": "body-0188", "role": "body", "section": "Step 3: Parameter error bound", "weight": 1.0} -->

‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds for $\theta_{0}=\theta$ and $\theta_{1}=\hat{\theta}^{\varepsilon}_{m,T}$ implies (3.22. ‣ Proposition 3.9.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Step 3: Parameter error bound", "weight": 1.0} -->

‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) also holds for $\theta_{0}=\theta$ and any $\theta_{1}\in\mathrm{conv}\{\hat{\theta}^{\varepsilon}_{m,T},\theta\}$ and (b) $\hat{\theta}^{\varepsilon}_{m,T}\in\Theta^{\prime}$ implies $\mathrm{conv}\{\hat{\theta}^{\varepsilon}_{m,T},\theta\}\subset\Theta^{\prime}$, by (3.23. ‣ Proposition 3.9.

<!-- chunk {"id": "body-0190", "role": "body", "section": "Step 3: Parameter error bound", "weight": 1.0} -->

‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) from 3.9, we have on $\mathcal{E}_{1}$, for every $\theta\in\mathrm{conv}\{\hat{\theta}^{\varepsilon}_{m,T},\theta\}$, where the last inequality holds since we assume that $T\gtrsim d^{2}$.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Step 4: Verify FI radius", "weight": 1.0} -->

We will utilize A.4 to verify the FI radius condition (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")). Since ${}_{\theta}\log p_{\theta}(z_{t+1}\mid z_{t})=-\frac{1}{\sigma^{2}}(D_{\theta}h_{\theta}(z_{t}))^{\mathsf{T}}(h_{\theta}(z_{t})-z_{t+1})$ for $t\geqslant 1$, we have for any $\theta\in\Theta$, We also have the base case $\mathcal{I}_{1}(\theta)=0$.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Step 4: Verify FI radius", "weight": 1.0} -->

On the other hand, for a unit-norm $v\in\mathbb{R}^{d^{2}}$ and $\theta_{1},\theta_{2}\in\Theta$, Hence, we have that $B_{\mathcal{I}}\lesssim\max\{1/\sigma^{2},d\}$. By A.4 and (4.67) we have on $\mathcal{E}_{1}$ for any $\theta\in\mathrm{conv}\{\hat{\theta}^{\varepsilon}_{m,T},\theta\}$, Combining (4.62), (4.64), and (4.68), we have that on $\mathcal{E}_{1}$, Hence by A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), we have that (3.24. ‣ Proposition 3.9.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Step 4: Verify FI radius", "weight": 1.0} -->

‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2

<!-- chunk {"id": "body-0194", "role": "body", "section": "Step 5: Final result", "weight": 1.0} -->

If $m$ satisfies conditions (4.63), (4.66), and (4.69), then on $\mathcal{E}_{1}$ we have from 3.9 and (4.60):

<!-- chunk {"id": "body-0195", "role": "body", "section": "Sequence Modeling with Linear Attention", "weight": 1.0} -->

Since their introduction, transformer models and architectures have found popularity in modern sequence modeling tasks, finding use in fields such as language modeling, computer vision, and reinforcement learning. Despite their widespread application however, full theoretical analysis of multi-layer transformer models is currently out of reach. As a result, stylized and simplified attention modules that isolate core mechanisms are commonly used in the literature as analytically tractable proxies for analyzing the full models. Single-layer linear self-attention models have been used to explore the dynamics of in-context learning and emergent inductive biases in transformers. Recent works show that attention can operate as a max-margin token selection mechanism, even establishing an equivalence with hard-margin SVM. Furthermore, established the global convergence of gradient descent for this framework, and a finite sample bounds were established by with parameter estimation upper bounds; we take particular inspiration from this line of work, especially, and analyze a simple linear transformer with a single-layer cross-attention and linear activation.

<!-- chunk {"id": "body-0196", "role": "body", "section": "Sequence Modeling with Linear Attention", "weight": 1.0} -->

Let us consider a vocabulary of $K$ tokens denoting the states $z\in\mathsf{Z}$, each assigned a $d$-dimensional embedding by an embedding matrix $E=[e_{1}\ \@cdots\ e_{K}]^{\mathsf{T}}\in\mathbb{R}^{K\times d}$, such that $\mathsf{Z}=\{e_{i}\mid i\in[K]\}$. We further emphasize that these embeddings $\{e_{k}\}_{k=1}^{K}$ are *not* the standard basis vectors, which we denote instead $\mathbf{1}(k)\in\mathbb{R}^{K}$ in this section.

<!-- chunk {"id": "body-0197", "role": "body", "section": "Sequence Modeling with Linear Attention", "weight": 1.0} -->

We assume that the first *two* tokens $z_{0},z_{1}$ are drawn from a given initial distribution $\rho_{1}$ over $\mathsf{Z}\times\mathsf{Z}$ to create an initial state for cross-attention.

<!-- chunk {"id": "body-0198", "role": "body", "section": "Sequence Modeling with Linear Attention", "weight": 1.0} -->

To sample a new token $z_{t+1}\in\mathsf{Z}$ in a sequence $z_{0:t}$ where $z_{0:t}\in\mathbb{R}^{(t+1)\times d}$, we sample *auto-regressively* by taking the last token $z_{t}$ to be the query token in a cross-attention layer given as: where $\mathcal{K},Q,V\in\mathbb{R}^{d\times d}$ denote the key, query, and value matrices, $C\in\mathbb{R}^{(K-1)\times d}$ denotes the classifier head, $\mathbb{A}$ denotes an activation function, $\mathbb{S}$ denotes the softmax function, and $\Phi:\mathbb{R}^{K-1}\mapsto\mathbb{R}^{K}$ denotes the function that embeds $\Phi(x):=(x,0)$.^1313^13The function

<!-- chunk {"id": "body-0199", "role": "body", "section": "Sequence Modeling with Linear Attention", "weight": 1.0} -->

$\Phi$ is introduced to allow for parameter recovery; otherwise parameterizing a distribution over $[K]$ using $K$ logits is not identifiable, as softmax is invariant under affine transforms (i.e., $\mathbb{S}(x+c\mathds{1})=\mathbb{S}(x)$ for any $c\in\mathbb{R}$).

<!-- chunk {"id": "body-0200", "role": "body", "section": "Sequence Modeling with Linear Attention", "weight": 1.0} -->

We shall denote $\theta:=\mathrm{vec}(\mathcal{K}Q^{\mathsf{T}})$ to be the parametrization such that $\Theta=\{\theta\in\mathbb{R}^{d^{2}}\mid\lVert\theta\rVert\leqslant R\}$, and we constrain $V=I_{d}$ and $C$ to be fixed matrices. Finally, we use a linear activation, where we normalize by $1/t$ for key trajectory length $t$.^1414^14This normalization ensures that the sum of key-query attention scores does not scale with trajectory length, which would increase the magnitude inside the outer softmax over time and cause exponential decay in the minimum probability of a token. This scaling is implicit in softmax activation settings, which would divide by the sum of the exponentiated weights. We note that this scaling is also used in practice.

<!-- chunk {"id": "body-0201", "role": "body", "section": "Sequence Modeling with Linear Attention", "weight": 1.0} -->

This all simplifies to the following: where we recall that $\mathrm{mat}$ is the matricization function such that $\mathrm{mat}(\theta)\in\mathbb{R}^{d\times d}$.

<!-- chunk {"id": "body-0202", "role": "body", "section": "Comparison with \\[97, Corollary 4.3\\]", "weight": 1.0} -->

As mentioned previously, the most comparable result to 4.18 is \[97, Corollary 4.3\]. Here, the authors also study a multi-trajectory data model, but one key difference is that, the trajectory $z_{0:T}$ is not auto-regressively generated. Instead, there is a distribution $\mathcal{D}_{X}$ over *prompts* $z_{0:T-1}$, followed by a last token $z_{T}$ generated from a self-attention model conditioned on the prompt $z_{0:T-1}$, resembling a standard supervised learning setup. Consequently, their final parameter recovery rate only decays with the number of trajectory $m$, in comparison to our rate (4.72) which decreases with the total data budget $mT$. Another difference between our two settings is a structural one.

<!-- chunk {"id": "body-0203", "role": "body", "section": "Comparison with \\[97, Corollary 4.3\\]", "weight": 1.0} -->

We choose to analyze a setting with linear activation instead of softmax activation $\mathbb{A}$, and we constrain the outputs of the classifier head $C$ to $\Delta^{K-1}$ (the probability simplex in $\mathbb{R}^{K}$) by means of an outer softmax activation (i.e., we treat the outputs of the classifier head as logits, as is typically done in practice), as detailed in (4.70). On the other hand in they consider a softmax activation $\mathbb{A}$, but omit the softmax activation after the classifier head. Hence, they require additional assumptions on the classifier head and the embeddings matrix to ensure that the output of the classifier head is a valid probability distribution. This may seem like a minor difference, but their setup requires that vocabulary embeddings $E$ are linearly independent \[97, Assumption 2.3\], which requires that $d\geqslant K$ (i.e., the embedding dimension exceeds the vocabulary size).

<!-- chunk {"id": "body-0204", "role": "body", "section": "Comparison with \\[97, Corollary 4.3\\]", "weight": 1.0} -->

As we discussed previously, in practice we typically have the opposite trend (i.e., embedding dimension is much smaller than vocabulary size), which our model allows.

<!-- chunk {"id": "body-0205", "role": "body", "section": "Comparison with \\[97, Corollary 4.3\\]", "weight": 1.0} -->

With these remarks in place, we can now directly compare our bounds to, keeping in mind the differences in problem setup and assumptions described previously. To keep the comparison simple, we will suppress dependency on $C,R,E$, and only focus on $m,T,K$ in the bounds. The main parameter recovery result in states that with high probability: where $\alpha>0$ is the strong convexity constant of the population loss over a ball around $\theta$. This quantity $\alpha$ is left unspecified in their argument; they only argue that $\alpha>0$, but do not provide an explicit lower bound for it.

<!-- chunk {"id": "body-0206", "role": "body", "section": "Comparison with \\[97, Corollary 4.3\\]", "weight": 1.0} -->

Since for negative log likelihood, both Fisher information and Hessian of the population loss coincide, in the notation of our work, $\alpha=\inf_{\theta\in B(\theta,r_{0})}\lambda_{\min}(\mathbb{E}_{z_{0:T-1}\sim\mathcal{D}_{X}}[\mathcal{I}_{T}(\theta\mid z_{0:T-1})])$ (note that the conditional Fisher Information notation is defined in (A.1)) where $r_{0}$ is a localization parameter which we consider as a constant. With this in mind, 4.18 implies that with high probability: where $\bar{\alpha}:=\lambda_{\min}(\bar{\mathcal{I}}(\theta))$. As mentioned previously, we show a lower bound on $\bar{\alpha}\gtrsim K^{-4}$, which again is most likely not optimal.

<!-- chunk {"id": "body-0207", "role": "body", "section": "Comparison with \\[97, Corollary 4.3\\]", "weight": 1.0} -->

Comparing (4.73) with (4.74), we see that the dependence on the parameter dimension ($K$ for the former as they consider a subspace of $d\times d$ matrices with dimension $\leqslant K^{2}$, $d$ for our case) is equivalent up to log factors. On the other hand, our bound yields an improvement on the dependence of the $\bar{\alpha}$ (vs. $\alpha$) parameter in the final rate. Finally and most importantly, as our setting studies auto-regressive generation, our rate is able to capture the dependence on all the data points $mT$, rather than just the number of trajectories $m$.

<!-- chunk {"id": "body-0208", "role": "body", "section": "Step 1: Covering number bound", "weight": 1.0} -->

As earlier, we first estimate the covering number of $\mathcal{P}$ in the FI norm through the $\ell_{2}$ covering number. Let $J:=\begin{bmatrix}I_{K-1}\\0\end{bmatrix}\in\mathbb{R}^{K\times(K-1)}$.

<!-- chunk {"id": "body-0209", "role": "body", "section": "Step 1: Covering number bound", "weight": 1.0} -->

Next, since we have this motivates finding an expression for the Fisher information matrix and its maximum eigenvalue.

<!-- chunk {"id": "body-0210", "role": "body", "section": "Step 1: Covering number bound", "weight": 1.0} -->

If we let $(z_{t})\in[K]$ denote the index of the token associated with entry $z_{t}$ and $[M_{0:t}]_{i}$ denote the $i$-th row of $M_{0:t}$, we calculate the Hessian of the log likelihood: If we denote the conditional expectation $\mathbb{E}_{t}^{\theta}[\cdot]\triangleq\mathbb{E}_{p_{\theta}}[\cdot\mid z_{0:t}]$, Hence, the FI matrix can be represented as: We may see that for all $t\in[T-1]$, $\lVert M_{0:t}\rVert_{\mathrm{op}}\leqslant\sup_{k\in[K]}\lVert e_{k}\rVert^{3}\lVert C\rVert_{\mathrm{op}}=\lVert

<!-- chunk {"id": "body-0211", "role": "body", "section": "Step 1: Covering number bound", "weight": 1.0} -->

C\rVert_{\mathrm{op}}$. Expanding out the multiplication and upper bounding gives our result.

<!-- chunk {"id": "body-0212", "role": "body", "section": "Step 1: Covering number bound", "weight": 1.0} -->

This implies the relation for $\varepsilon\in$: Applying 3.6 with $\varepsilon=\frac{\delta}{2\sqrt{2m}}$ and $\eta=\frac{1}{2R\lVert C\rVert_{\mathrm{op}}\sqrt{mT}}$, and upper bounding $R\lVert C\rVert_{\mathrm{op}}\sqrt{mT}/\delta\leqslant(R\lVert C\rVert_{\mathrm{op}}\sqrt{mT}/\delta)^{d^{2}}$ in the logarithm, for some universal constant $c_{0}>0$ we obtain with probability at least $1-\delta$, For satisfactory $c_{0}$, the final $\frac{1+\delta^{2}}{m}$ term can additionally be collapsed into the first term given that $d>1$.

<!-- chunk {"id": "body-0213", "role": "body", "section": "Step 1: Covering number bound", "weight": 1.0} -->

Let us denote $\mathbf{1}(z)\in\{0,1\}^{K}$ to be the one-hot standard basis vector such that for $i\in[K]$, $[\mathbf{1}(z)]_{i}=1$ if $z=e_{i}$ and $[\mathbf{1}(z)]_{i}=0$ otherwise. When invoking 3.6, we can use the log-concave conclusion (3.16. ‣ Theorem 3.6.

<!-- chunk {"id": "body-0214", "role": "body", "section": "Step 1: Covering number bound", "weight": 1.0} -->

‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), since $\log p_{\theta}(z_{0:T})$ is given: which is the sum of affine terms in $\theta$ minus the sum of terms which are given by taking the log-sum-exp (LSE) of a linear function of $\theta$, which is convex \cf. [100, Section 3.1.5\]. Hence, $\log p_{\theta}(z_{0:T})$ is a concave function by basic composition rules.

<!-- chunk {"id": "body-0215", "role": "body", "section": "Step 2: Estimating $B_{1}$ and $B_{2}$", "weight": 1.0} -->

Crucial in bounding $B_{1}$ and $B_{2}$ is bounding the smallest eigenvalue of $\mathcal{I}(\theta)$, so let us note the expansion of the Fisher information from eq. 4.76: We note that if one simply looks at $\operatorname*{\mathsf{diag}}(\mathbb{S}(M_{0:t}\theta))-\mathbb{S}(M_{0:t}\theta)\mathbb{S}(M_{0:t}\theta)^{\mathsf{T}}$, the minimum eigenvalue would be zero since there is a constrained direction due to $\mathbb{S}(M_{0:t}\theta)$ lying on the $K-1$ dimensional simplex. Hence, we look at the reduced matrix by ignoring the last redundant coordinate, which restores a non-zero minimum eigenvalue.

<!-- chunk {"id": "body-0216", "role": "body", "section": "Step 2: Estimating $B_{1}$ and $B_{2}$", "weight": 1.0} -->

Let us now find such a $\mu$ by lower bounding $\log p_{\theta}(e_{k}\mid z_{0:t})$ and exponentiating it to find a bound for $p_{\theta}(e_{k}\mid z_{0:t})$ for arbitrary $k\in[K]$: We now exponentiate to recover a bound for the conditional likelihood: Through Cauchy-Schwartz we may bound the quantity inside the exponent, giving our final bound.

<!-- chunk {"id": "body-0217", "role": "body", "section": "Step 2: Estimating $B_{1}$ and $B_{2}$", "weight": 1.0} -->

Once we have this, we can extract the inner matrix from $\mathcal{I}(\theta)$ by lower bounding the Rayleigh quotient, giving: The smallest eigenvalue of this quantity can be lower bounded by the minimum eigenvalue of both sides of the Kronecker product. The first quantity can be handled by lower bounding the probability of seeing a particular token, For the second quantity, we note that the minimum eigenvalue function is concave so we may lower bound the expression by moving it into the expectation: Finally, we may put this all together for an expression for the minimum eigenvalues of the conditional and unconditional Fisher information matrices: We can now begin working on finding bounds for the constants $B_{1}$ and $B_{2}$.

<!-- chunk {"id": "body-0218", "role": "body", "section": "Step 2: Estimating $B_{1}$ and $B_{2}$", "weight": 1.0} -->

We may observe that $\mathbf{1}(z_{t+1})-\mathbb{S}(M_{0:t}\theta)$ is a bounded random variable vector: From this we can observe the following: This all gives that $\psi_{t+1}$ is a zero-mean bounded random variable given by $\sigma^{2}=2\lVert v\rVert^{2}\lVert C\rVert_{\mathrm{op}}^{2}$, and we can see that $\langle v,{}_{\theta}\log p_{\theta}(z_{0:T})\rangle=\tsum\slimits@_{t=2}^{T}\psi_{t}$ is a martingale sum. This allows us to apply Azuma-Hoeffding (A.7.

<!-- chunk {"id": "body-0219", "role": "body", "section": "Step 2: Estimating $B_{1}$ and $B_{2}$", "weight": 1.0} -->

‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), giving us that and as such $\mathbb{E}[\langle v,{}_{\theta}\log p_{\theta}(z_{0:t})\rangle^{4}]^{1/4}\leqslant 4\sqrt{2T}\lVert v\rVert\lVert C\rVert_{\mathrm{op}}$. We note that applying Rosenthal's inequality for MDS (cf. A.6. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) retrieves a similar result, but requires a longer proof in order to express a bound for both terms.

<!-- chunk {"id": "body-0220", "role": "body", "section": "Step 3: Parameter error bound", "weight": 1.0} -->

From here, we can unlock the first set of bounds by verifying (3.22. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")): In order to satisfy this condition, we can take $m\geqslant\left(d^{2}\log\left(\frac{TR^{2}\lVert C\rVert_{\mathrm{op}}^{2}m}{\delta^{2}}\right)+1+\delta^{2}\right)\cdot\frac{T^{2}\lVert C\rVert_{\mathrm{op}}^{4}}{\lambda_{\min}(\mathcal{I}(\theta))^{2}}$. If we apply A.1.

<!-- chunk {"id": "body-0221", "role": "body", "section": "Step 4: Verify FI radius", "weight": 1.0} -->

We now need to show (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) in order to unlock the second bound. To this end, we show a Lipschitz condition on the conditional Fisher information from eq. 4.75: This gives us that $\mathrm{Lip}\leqslant 3\lVert C\rVert_{\mathrm{op}}^{3}$. Let us now find an expression for the second moment bound: With both a globally bounded Lipschitz constant and a finite $B_{\mathcal{I}}$, we can apply A.4 to bound the difference in Fisher informations: Note that the lower bound on $\lambda_{\min}(\mathcal{I}(\theta))$ in (4.78) is agnostic to the value of $\theta\in\Theta$.

<!-- chunk {"id": "body-0222", "role": "body", "section": "Step 4: Verify FI radius", "weight": 1.0} -->

Therefore, If we apply this to (3.23. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2

<!-- chunk {"id": "body-0223", "role": "body", "section": "Step 5: Final result", "weight": 1.0} -->

Finally, we can plug in our expression for the minimum eigenvalue in eq. 4.78 to take the following bound and applying A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") extracts $m$ to satisfy the Fisher radius: Notably, this additionally satisfies (4.79).

<!-- chunk {"id": "body-0224", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced the Hellinger localization framework for deriving nearly instance-optimal parameter recovery rates for multi-trajectory learning setups. We applied our framework to a diverse set of case studies, including a mixture of Markov chains example, a dependent linear regression problem with general noise distributions, a non-monotonic sinusoidal GLM example, and a linear attention sequence modeling setup. In each case, we showed that our Hellinger localization framework was able to provide nearly instance-optimal rates that significantly improve upon the prior art.

<!-- chunk {"id": "body-0225", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our work further opens up several avenues for future investigation. We list out a few ideas, starting with technical improvements, and ending with more broader, high-level directions.

<!-- chunk {"id": "body-0226", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Extensions of self-normalization: As discussed in Section 4.2.1, one particular drawback of our current framework is that it places un-necessary requirements on the regularity of the trajectory process $z_{1:T}$. Concretely, in the context of dependent linear regression, the process $z_{1:T}$ can not grow more than $\mathrm{poly}(T)$, which rules out e.g., recovering linear dynamical systems with spectral radius $>1$. We believe this restriction is purely a technical limitation of our argument, which currently does not have a method to self-normalize as is done in analysis specialized for least-squares linear regression. The work of which generalizes offset complexity to exp-concave losses is a natural starting point for such an inquiry.

<!-- chunk {"id": "body-0227", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Improved minimum trajectory requirements for non-log-concave families: As we discussed in Section 3.4, another limitation of our current analysis is that whenever the family of distribution $\mathcal{P}$ is not log-concave, our requirements on the number of trajectory $m$ grows from $m\gtrsim\mathrm{polylog}(T)$ in the log-concave setting, to $m\gtrsim T\cdot\mathrm{polylog}(T)$. We believe this scaling should generally be improvable. One possible pathway is to utilize the local geodesic convexity of the squared Hellinger distance in the Fisher-Rao metric, and conduct our second-order Taylor analysis (cf. 3.9) over geodesics.

<!-- chunk {"id": "body-0228", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Non-realizable settings: Our work is carried out in the realizable setting, i.e., where the data generating distribution $p\in\mathcal{P}$. A natural and useful extension would be to allow for $p\mathrel{\mathchoice{\vtop{\halign}}{\vtop{\halign}}{\vtop{\halign}}{\vtop{\halign}}}\mathcal{P}$, and study convergence to the best distribution in $\mathcal{P}$, i.e., $\theta^{\mathcal{P}}:=\operatorname*{arg\,min}_{p\in\mathcal{P}}\mathrm{KL}(p\;\|\;p)$.

<!-- chunk {"id": "body-0229", "role": "body", "section": "Conclusion", "weight": 1.5} -->

One key technical challenge for the non-realizable setting is extending 3.6 to measure squared Hellinger distance $\mathrm{d}_{H}^{2}(\hat{p}^{\varepsilon}_{m,T},p^{\mathcal{P}})$ without relying on e.g., max divergence coverings (cf. 3.1. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), but instead allowing for some less stringent tail behavior for the log-likelihoods which is still practical to verify. This could also be useful in allowing 3.6 to apply directly to the MLE estimator and not its discretized counterpart (cf. 3.7).

<!-- chunk {"id": "body-0230", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Applications to non-sequentially dependent data: While our work focuses on sequentially-ordered stochastic processes, our main tools in Section 3 (i.e., 3.6 and 3.9) are actually agnostic to this sequential structure. It is only when we analyze the score function and observed information matrix moments (i.e., (3.20) and (3.21) from 3.9) that we impose a temporal dependence in the data. Hence, an interesting future direction is to apply our main tools to other problem settings with different correlation structures, such as for Ising models (cf. related work from Section 2) and other graph/network structures.

<!-- chunk {"id": "body-0231", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Applications for filtering and control problems: Finally, through the case studies in Section 4, we have looked at parameter recovery in various types of dynamical systems. A natural next step is to consider the downstream control task where the recovered model parameters would be applied, by extending our results to enable task-specific optimal exploration for a broader family of parametric models and loss functions (cf. discussion in Section 4.2.1). Another direction is to apply our framework for filtering problems in state estimation, which can be cast as a latent maximum likelihood estimation problems. Here, an important sub-direction would be to study the application of our techniques to analyzing not just the exact MLE estimate, but also practical algorithms such as expectation-maximization and variational inference, which are necessary in situations where directly computing the MLE is computationally intractable.
