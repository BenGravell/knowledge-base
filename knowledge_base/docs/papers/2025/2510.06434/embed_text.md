## Introduction

Learning from sequential data is central to modern machine learning (ML) and statistical modeling, underpinning applications such as language modeling, speech recognition, time-series forecasting, generalist robotics, neurological sequence analysis, and many other examples. Yet, despite its importance and prevalence, our fundamental understanding of when learning from sequential streams is possible---and what the sharp, problem-specific sample complexities are---remains far less developed compared with the classical i.i.d. setting.

There are two predominant approaches to analyzing non-i.i.d. sequential learning setups. The first approach is to consider consuming data from a single stochastic process indexed by time $t$, and study what happens to the estimator as time progresses forward. In this paper, we will refer to a realization from a time-index stochastic process as a trajectory, and hence we denote this approach as the *single-trajectory* setting. This setting is challenging, as simple examples illustrate the necessity of imposing non-trivial assumptions about the long-running behavior of the underlying process. The strongest results hold under assumptions about the rate of convergence (typically quantified via its mixing-time ) of the stochastic process to its time-marginal distributions, and provide bounds on e.g., the excess risk of the empirical risk minimizer (ERM) as time $t$ moves forward (see e.g., ). However, these type of results suffer from some key drawbacks: (i) Many processes---e.g., human dialogue, periodic locomotion gaits, wearable sensor data---are interesting precisely because they do *not* mix. Even for processes that do mix, analytical bounds on the mixing-time can be quite conservative in high-dimension, and challenging to estimate numerically without assuming extra structure. (ii) Typical bounds suffer from *sample deflation*, where the non-i.i.d. sequential rate is a factor of the mixing-time larger than its corresponding i.i.d. rate (i.e., its effective sample size is deflated by the mixing-time); furthermore, the non-i.i.d. rates are only valid after time $t$ exceeds some factor of the mixing-time, typically referred to as a burn-in time.

The second approach to studying sequential learning sits in-between the classic i.i.d. setting, where every data point is independent, and the single-trajectory setting, where every data point is correlated. Instead, one assumes that many independent realizations of a stochastic process are observed, a setup we will refer to as the *multi-trajectory* setting (see e.g., ). In the multi-trajectory setting, data within a trajectory is temporally correlated as usual, but importantly, data across different trajectories is independent. The latter fact is crucial, as it enables reductions to i.i.d. learning only using minimal assumptions about the underlying process. A further benefit of the multi-trajectory data model is that it is a much more accurate description of the underlying training data for modern ML models which ingest sequential data---such as vision-language models (VLMs), large language models (LLMs), and generalist behavior policies for robotics ---compared with the single-trajectory model.

Nevertheless, despite these advantages, many open questions still remain regarding the multi-trajectory model. A naïve reduction to i.i.d. learning, where each trajectory is treated as a single data point, only yields rates where the effective sample size is the $m$, the number of trajectories. Here, the length $T$ of each trajectory^11^1We assume for ease of exposition that each trajectory has the same length. is absent from this sample size, which is in general not the correct scaling. On the other hand, embedding a multi-trajectory process into a single trajectory and appealing to a single-trajectory result yields either (i) similar bounds as the i.i.d. reduction if no assumption on the mixing-time of the individual trajectories is made, or (ii) bounds where the effective sample size scales as the ${mT} \Uparrow \kappa$---i.e., *total* number of data points available to the learner divided by the mixing-time $\kappa$ of the individual trajectories. While (ii) improves upon the i.i.d. reduction, the deflation factor is in general not optimal for multi-trajectory settings. Indeed, a recent line of work shows that for square-loss regression from dependent covariates, one can obtain---under a set of conditions which do not generally require e.g., bounded mixing-times---finite-sample rates where the effective sample size not only improves to $mT$, but also the bounds nearly match those prescribed by asymptotic normality of maximum likelihood estimation (MLE). However, as their proof techniques are tailored specifically for square-loss, it is unclear how to generalize these results more broadly to e.g., MLE settings.

In this work, we significantly broaden our understanding of learning in the multi-trajectory setting by providing a general framework---which we call the *Hellinger localization framework*---for deriving sharp instance-optimal parameter recovery rates for general maximum-likelihood estimation. At a high-level, our framework proceeds in two main phases: In the first phase, we utilize a reduction to i.i.d. learning which controls the squared Hellinger distance between the *path measures* of the MLE estimate and the underlying distribution, at a rate where the sample size is $m$, the number of trajectories. In the second phase, we utilize the fact that squared Hellinger distance is locally quadratic in the parameter space, weighted by the Fisher information matrix of the underlying path measure. This has two key consequences: First, it allows us to extract out an additional scaling factor of $T$, the length of each trajectory, whenever the process contains sufficient excitation. Second, the Fisher information matrix allows us to derive instance-specific rates that match, up to logarithmic factors, those prescribed by asymptotic normality of MLE. Our framework thus yields instance-optimal bounds where the effective sample size contains all the observed data (i.e., scales as $mT$), and applies broadly to maximum likelihood estimation problems. Furthermore, as our framework relies only on bounded growth conditions of both the score function and the observed information matrix for localization, it applies beyond the usual mixing processes and stable dynamics typically assumed in sequential learning.

To demonstrate the generality of our approach, we instantiate the Hellinger localization framework in four case studies: (i) a simple mixture of Markov chains example, (ii) a dependent linear regression setting under general (i.e., non-Gaussian) product-noise distributions, (iii) a non-monotonic generalized linear model (GLM) example, and (iv) a linear-attention sequence modeling problem. For each of these case studies, our framework obtains near-optimal parameter recovery error rates, yielding significant improvements over the rates obtained by standard reductions.

### Paper organization

This manuscript is organized as follows. In Section 2, we review related work. Section 3 describes the multi-trajectory MLE problem setup, reviews the standard i.i.d. and single-trajectory reductions in more detail, and presents the Hellinger localization framework, including a step-by-step guide describing how to instantiate the framework for a general problem. Section 4 contains the results of our four specific case studies; for each case study, we also conduct a more thorough literature review on the specific problem beyond what is described in Section 2. Section 5 concludes the paper, with the appendices containing the deferred proofs.

## Related Work

We first review the relevant literature for learning from non-i.i.d. sequential data in the single-trajectory (single realization of a time-indexed stochastic process) setting; as already discussed briefly and will be reviewed in more detail in Section 3.1, single-trajectory results can generally be used to analyze multi-trajectory settings. The most common approach to analyzing single-trajectory learning is to impose mixing-time assumptions on the underlying process (see e.g., ); as a result, excess-risk or parameter recovery rates are typically a factor of mixing-time worse than their corresponding i.i.d. rates, as the standard blocking technique can only utilize one data point in every mixing-time size chunk. Recently, there have been a few improvements for various problem settings. A line of work studying parameter recovery in linear dynamical systems allows for the transition matrix $A$ to be marginally stable (i.e., $\rho1$) or even unstable (i.e., $\rho > 1$); both situations correspond to unbounded mixing-times, with the former marginally stable setting also extended for a class of GLMs. For realizable non-linear regression problems with square loss, shows that assuming a certain trajectory-level hyper-contractivity condition holds, the sample size deflation in the excess risk bound can actually be removed, leaving the mixing-time dependence to only the burn-in time. The work further improves upon this result by obtaining variance-optimal rates under a (weakly) sub-Gaussian class (cf. ) assumption; as this result is important context for our work, we review it in detail in Section 3.1. Despite improvements, these works either (a) only apply to a limited class of models, or (b) require the underlying process to mix, to satisfy additional technical assumptions (e.g., trajectory hyper-contractivity or sub-Gaussian class) that can be difficulty to verify, and only apply for the square-loss.

Next, we address literature directly studying the multi-trajectory setting (see e.g., ). Most relevant to our work is, which studies parameter recovery for linear least-squares regression from dependent covariates, and derives instance-optimal rates that scale with the full dataset size $mT$ while requiring no stability/mixing assumptions; we review these results in more detail in Section 3.1. While this work also provides important context and motivation for our study, their proof techniques---self-normalized martingales and extensions of small-ball inequalities ---are tailored for the specific closed-form structure of the linear least-squares regression solution, and do not admit obvious extensions to more general setups. On the other hand, our approach is based more on information-theoretic concepts, building on a combination of techniques for analyzing density estimation, in conjunction with locally quadratic expansions of $f$-divergences (specifically, the squared Hellinger distance in our setting).

We next briefly remark on other recent progress in learning from non-i.i.d. data sources. One line of work studies learning either regression functions or filters from the perspective of online learning and regret minimization, constructing a online predictor of future observations that is competitive over a family of fixed predictors given perfect hindsight knowledge. We view our results as complementary to this line of work---an interesting question for future research is to study these regret minimization formulations in settings where multi-trajectory data is revealed online to the player. Another line of work considers non-temporal data correlations, specifically learning Ising models from either a single sample (e.g., ), or multiple independent samples (e.g., ). While these problem setups are not directly comparable, we believe it is interesting future work to study whether our techniques can also be applied in such a setting.

Finally, the case studies we consider in Section 4 are special cases and/or natural extensions of problem setups previously considered in the literature; we provide detailed overview of problem-specific related work for each case study in its corresponding sub-section.

## Problem Setup and General Framework

In this section, we review background, outline our general problem formulation and describe our new Hellinger localization framework. We first describe the notation used in our work.

### Notation

For a vector $x{\mathbb{R}}^{d}$, we let ${}x{}_{p}$ denote its $\ell_{p}$ norm; for $p = 2$, we drop the subscript, i.e., ${x} = {x{}_{2}}$. The notation $x^{2} = {xx^{\mathsf{T}}}$ is shorthand for the outer product matrix. Also, the notation ${diag}{(x)}{\mathbb{R}}^{dd}$ is the diagonal matrix satisfying ${{diag}{(x)}_{ii}} = x_{i}$ for $i{(d\rfloor}$. Given a positive definite matrix $\Sigma{\mathbb{R}}^{dd}$, we let ${x{}_{\Sigma}} = \sqrt{x^{\mathsf{T}}\Sigmax}$ denote its weighed $\ell_{2}$ norm. For a matrix $M{\mathbb{R}}^{dk}$, we let ${}M{}_{op}$, ${}M{}_{F}$ denote its operator (maximum singular value) and Frobenius norm, respectively. If $d = k$ and $M$ is positive semi-definite, we let $M^{1 \Uparrow 2}$ denote its PSD square root. If $M = M^{\mathsf{T}}$ is symmetric, we let the eigenvalues of $M$ be denoted as $\lambda_{i}{(M)}$, $i{(d\rfloor}$, listed in non-increasing order. The notation ${vec}{(M)}{\mathbb{R}}^{dk}$ denotes vectorization of $M$; we follow the convention that vectorization is done in column-order, so that for size conforming matrices $A$, $M$, and $B$, the identity ${{vec}{({AMB})}} = {{({B^{\mathsf{T}}A})}{vec}{(M)}}$ holds, where denotes the Kronecker product. We use ${mat}{}$ to denote the inverse of ${vec}{}$, i.e., ${{mat}{({{vec}{(M)}})}} = M$; the output dimension $dk$ of ${mat}{}$ will be implicit from context. Given a real-valued random variable $X$, we let ${}X{}_{\mathcal{L}^{p}{(\rho)}} = {({\mathbb{E}}_{\rho}{(\bigcup X\bigcup^{p}\rfloor})}^{1 \Uparrow p}$ denote the $\mathcal{L}^{p}{(\rho)}$ norm. For a measure $\mu$, we let $\mu^{k}$ to denote its $k$-fold product measure. Finally, the unit sphere in ${\mathbb{R}}^{d}$ is denoted ${\mathbb{S}}^{d - 1}:={\{{{x{\mathbb{R}}^{d}x} = 1}\}}$.

### Maximum Likelihood Estimation in Multi-Trajectory Settings

We fix an index $T{\mathbb{N}}_{+}$ and consider a stochastic process $z_{1:T}:={(z_{t})}_{t = 1}^{T}$ taking values in $\mathsf{Z}$. Let $p{(z_{1:T})}$ denote the joint distribution over $z_{1:T}$. We emphasize that the process $z_{1:T}$ is not necessarily stationary nor ergodic, nor does it necessarily have bounded mixing-times. Our learner observes $m{\mathbb{N}}_{+}$ independent trajectories $\mathcal{D}_{m,T}:={({(z_{t}^{(i)})}_{t = 1}^{T})}_{i = 1}^{m}$ with each $z_{1:T}^{(i)}p{}$. Fix a parametric class $\mathcal{P}:={\{{p_{\theta}{(z_{1:T})}\theta\Theta}\}}$ of distributions and consider the maximum-likelihood (MLE) estimator ${\hat{p}}_{m,T}\mathcal{P}$ given the dataset $\mathcal{D}_{m,T}$ as:

In this work, we are interested in the finite-sample behavior of the MLE estimator ${\hat{p}}_{m,T}$ in the *realizable* setting, i.e., where $p\mathcal{P}$. We impose some regularity conditions to make the analysis well-posed. First, we endow $\mathsf{Z}$ with a base measure $\mu$ (e.g., counting measure for discrete $\mathsf{Z}$ or Lebesgue measure when $\mathsf{Z}$ is a subset of Euclidean space), and we overload $p_{\theta}$ to also denote the Radon-Nikodym density w.r.t. the corresponding base measure $\mu$ on $\mathsf{Z}$. We also assume that (a) for $\mu^{T}$-a.e. $z_{1:T}\mathsf{Z}^{T}$, the map $\thetap_{\theta}{(z_{1:T})}$ is $C^{2}{(\Theta_{0})}$ where $\Theta_{0}\Theta$ is an open set, (b) that there exists a unique $\theta\Theta$ such that ${p_{\theta}{}} = {p{}}$ (almost surely), and that (c) the parameter set $\Theta$ is star-convex around $\theta$.^22^2That is for any $\theta\Theta$, ${s\theta} + {{({1 - s})}\theta\Theta}$ for all $s{(0,1\rfloor}$. As our analysis relies on local quadratic expansions, this technical assumption ensures that such expansions are indeed valid. To set the stage for our results, let us first review what is known about the MLE estimator ${\hat{p}}_{m,T}$.

### Asymptotic normality

First, we can use the lens of asymptotic normality to understand limiting behavior as $m$ (but $T$ is fixed). To do this, we recall that the Fisher information (FI) matrix for the *trajectory* $z_{1:T}$ is defined as:

Under the assumption that $\theta{int}{(\Theta)}$ and that the estimator ${\hat{\theta}}_{m,T}$ is consistent (i.e., ${\hat{\theta}}_{m,T}\theta$ a.s. as $m$), standard asymptotic normality \see e.g., for $M$-estimators yields:

where $\overset{d}{}$ denotes convergence in distribution. The condition (3.3) depends implicitly on the trajectory length $T$ through the FI matrix $\mathcal{I}{(\theta)}$. However, as the FI matrix $\mathcal{I}{(\theta)}$ factorizes nicely across time:

we generically expect that $\mathcal{I}{(\theta)}$ grows at least linearly with $T$, i.e., $\lambda_{\min}{({\mathcal{I}{(\theta)}})}\Omega{(T)}$. Hence, if we define the *normalized* Fisher information matrix ${\overline{\mathcal{I}}{(\theta)}}:={T^{- 1}\mathcal{I}{(\theta)}}$, the result (3.3) implies that the limiting behavior as $m$ scales with high probability as:

Therefore, as long as the normalized FI matrix provides sufficient excitation so that $\lambda_{\min}{({\overline{\mathcal{I}}{(\theta)}})}$ does *not* vanish to zero as the trajectory length $T$ increases, then (3.4) implies that the squared parameter error decreases at a $1 \Uparrow {({mT})}$ rate, a rate which not involves *all* the data points available in the training set, but as importantly is also *instance-optimal*, containing instance-specific scaling through the FI matrix $\overline{\mathcal{I}}{(\theta)}$. Hence, showing that (3.4) holds in a non-asymptotic, finite number of trajectories regime under general conditions serves as one of the main goals of this work.

As we will discuss in detail in the remainder of this sub-section, finite-sample rates of the form (3.4) are known to hold for the setting of least-squares regression over dependent covariates under various assumptions; unfortunately, these analysis techniques heavily utilize the structure of the square-loss, and do not readily extend to more general losses such as the log-loss for MLE. Beyond the square-loss, the most general rates comes from reductions to either (i) standard i.i.d. learning results or (ii) existing single-trajectory results; the former yields rates exhibiting sub-optimal $1 \Uparrow m$ scaling, whereas the latter inherits the single-trajectory stability assumptions that are often unnecessary in the multi-trajectory case, and suffers from sample-deflation issues in the rates. This motivates the need for developing a new approach for establishing finite-sample instance-optimal rates for the multi-trajectory setting, which we turn to in Section 3.2.

### Linear least-squares regression and linear system identification

One case where a non-asymptotic rate of the form (3.4) is shown to hold in the literature is in the setting of linear least-squares regression over dependent covariates. Specifically, consider the following linear dynamical system (LDS) parameterized by $A{\mathbb{R}}^{dd}$:

For any $\theta = {{vec}{(A)}{\mathbb{R}}^{d^{2}}}$, the FI matrix $\mathcal{I}{(\theta)}$ takes on the form:

Hence letting ${{\hat{A}}_{m,T}{{\arg\min}_{A{\mathbb{R}}^{dd}}{{}_{i = 1}^{m}{}_{t = 1}^{T - 1}z_{t + 1}^{(i)}}}} - {Az_{t}^{(i)}{}^{2}}$ denote the MLE (3.1) and $A$ denote the true dynamics matrix generating the data via (3.5), plugging the FI matrix into (3.4) yields

where ${\Gamma_{t}{(A)}} = {\frac{1}{t - 1}{}_{s = 1}^{t - 1}\Sigma_{s}{(A)}}$. In, it is shown that this rate (3.6) holds in expectation whenever $md$, and that this cut-off is sharp. Similar results hold for the more general linear regression from LDS covariates. We emphasize here that the rate from (3.6) is truly a multi-trajectory phenomenon, and is *not* possible for arbitrary $A$ from a single trajectory; as shown , the MLE is not generally consistent in the single-trajectory setting when $A$ is unstable.

### Reductions to existing i.i.d./single-trajectory results

Beyond the linear least-squares regression setting, a simple generic approach for deriving rates in the multi-trajectory setting is to invoke an existing i.i.d. and/or single-trajectory result. As an example of an i.i.d. reduction, using the standard Rademacher complexity machinery for deriving risk bounds in independent settings,^33^3For analyzing MLE, there are much sharper non-asymptotic analysis in the i.i.d. setting (e.g., ), which do not require almost sure bounds on log-likelihoods, contain the correct variance-optimal scaling, and also capture fast-rates in realizable settings. We present the simplest result here to make our point clear. we have that the excess risk (in KL-divergence)

of the MLE ${\hat{\theta}}_{m,T}$ satisfies with probability at least $1 - \delta$,

where $B$ bounds the log-likelihood $T^{- 1}{\log p_{\theta}}{(z_{1:T})}$ a.s., $\mathcal{R}_{m}{(\mathcal{G}_{t})}$ is the Rademacher complexity of the function class $\mathcal{G}_{t}:={\{{z_{1:T}{\log p_{\theta}}{({z_{t}z_{1:{t - 1}}})}\theta\Theta}\}}$, and $c_{0}$ is a universal constant. Assuming that each conditional ${\bigcup{{\log p_{\theta}}{({z_{t}z_{1:{t - 1}}})}}\bigcup}O{}$, then we have $BO{}$ as well. We also generically expect that $\mathcal{R}_{m}{(\mathcal{G}_{t})}O{(\sqrt{p \Uparrow m})}$, which is the usual rate for parametric function classes. Furthermore, ${\frac{1}{T}{KL}{({p{(z_{1:T})}p_{{\hat{\theta}}_{m,T}}{(z_{1:T})}})}\frac{1}{2}\theta} - {{\hat{\theta}}_{m,T}{}_{\overline{\mathcal{I}}{(\theta)}}^{2}}$ asymptotically as ${\hat{\theta}}_{m,T}\theta$, and hence the scaling w.r.t. $T$ in the excess risk (3.7) is the correct one for comparison to (3.4). Therefore, the general scaling for the RHS of (3.8) is of order $\sqrt{p \Uparrow m}$, i.e., the effective sample size is the number of trajectories $m$. Note that in the realizable setting when ${\inf_{\theta^{}\Theta}{{KL}{({p{(z_{1:T})}p_{\theta^{}}{(z_{1:T})}})}}} = 0$, the bound for (3.8) can be improved to a fast-rate $p \Uparrow m$ scaling with local Rademacher complexities.

Single-trajectory results can also be used for reductions, by embedding the trajectories $\{ z_{1:T}^{(i)}\}$ into one single trajectory ${\overline{z}}_{1:{mT}}:={(z_{1:T}^{},\ldots,z_{1:T}^{(m)})}$. For this discussion, we focus on results relying on $\beta$-mixing^44^4The $\beta$-mixing coefficients (cf. ) for ${\{ z_{t}\}}_{t = 1}$ are defined as $\beta{(k)}:=\sup_{j{\mathbb{N}}_{+}}{\mathbb{E}}_{z_{1:j}}{({\mathbb{P}}_{z_{{j + k}:}}{(z_{1:j})} - {\mathbb{P}}_{z_{{j + k}:}}{}_{TV}\rfloor}$. The process is called $\beta$-mixing if $\beta{(k)}0$ as $k$. for concreteness, noting that our discussion also applies to results that rely on other definitions of mixing (e.g., $\phi$-mixing) in the literature. We also assume the process $\{ z_{t}\}$ is Markovian, as this makes the reduction simpler to state. Because $z_{1:T}^{(i)}z_{1:T}^{(j)}$ whenever $ij$, then we have that the $\beta$-mixing coefficients $\overline{\beta}{(k)}$ of $\{{\overline{z}}_{t}\}$ satisfy ${\overline{\beta}{(k)}} = {\beta{(k)}\mathbb{1}{\{{k < T}\}}}$, where $\beta{(k)}$ are the $\beta$-mixing coefficients of $\{ z_{t}\}$. Hence, the embedded trajectory $\{{\overline{z}}_{t}\}$ is trivially $\beta$-mixing with mixing-time equal to $T$ without any assumption on $\beta{(k)}$. Using this mixing-time and invoking a single-trajectory $\beta$-mixing result, such as , without any further assumption on $\beta{(k)}$ yields a similar result to (3.8). However, if we further assume that $\beta{(k)}C{\exp{({- {\rhok}})}}$ for some $\rho > 0$, and that ${T \Uparrow {({2\kappa})}}{\mathbb{N}}_{+}$ for $\kappa:={\rho^{- 1}{\log{({{CmT} \Uparrow \delta})}}}$, then we have the improved result: with probability at least $1 - \delta$,

where ${\overline{\mathcal{R}}}_{{mT} \Uparrow \kappa}^{j}$ denotes the *de-coupled* Rademacher complexity:

with the pair $({\overset{\sim}{z}}_{{{{({\ell - 1})}2\kappa} + j} - 1}^{(i)},{\overset{\sim}{z}}_{{{({\ell - 1})}2\kappa} + j}^{(i)})$ drawn from the same distribution as $(z_{{{{({\ell - 1})}2\kappa} + j} - 1},z_{{{({\ell - 1})}2\kappa} + j})$, but *independently* across $i{(m\rfloor}$ and $\ell{(\kappa\rfloor}$. Similar to before, we generically expect that ${\overline{\mathcal{R}}}_{{mT} \Uparrow \kappa}^{j}$ scales as order $\sqrt{{\kappap} \Uparrow {({mT})}}$. Hence, the general scaling of the RHS of (3.9) is of order $\sqrt{{\kappap} \Uparrow {({mT})}}$. Furthermore, as with the i.i.d. reduction, in the realizable setting local Rademacher arguments can also be used to improve the scaling of (3.9) to the fast-rate ${\kappap} \Uparrow {({mT})}$. This is an improvement over (3.8), as the effective sample size increases from $m$ to ${mT} \Uparrow \kappa$; however, this sample size still remains deflated by $\kappa$, as a consequence of the standard blocking technique used for de-coupling.

### Regression with square-loss

A recent line of work has shown that the sample size deflation described previously can be removed in the special case of non-linear regression with the square-loss, in both parametric and non-parametric regimes. To make their results concrete, we consider the following parametric family of distribution $\mathcal{P}$ over trajectories in ${\mathbb{R}}^{d}$:

coupled with the non-linear least-squares estimator ${{\hat{\theta}}_{m,T}{{\arg\min}_{\theta\Theta}{{}_{i = 1}^{m}{}_{t = 1}^{T - 1}z_{t + 1}^{(i)}}}} - {f_{\theta}{(z_{t}^{(i)})}{}^{2}}$ with $\Theta{\mathbb{R}}^{p}$, which is precisely the MLE estimator for (3.10). We now specialize the main result of \[2, Theorem 3.1\] to the problem (3.10). Suppose that the following assumptions hold:^55^5We state a clear set of assumptions, but not the most minimal, as \[2, Theorem 3.1\] is stated in broad generality.

*(Realizable):* The process $\{ z_{t}\}$ is generated by (3.10) for some $\theta\Theta$.

*(Stationary process):* The process $\{ z_{t}\}$ has a stationary measure $\nu$, and $z_{1}\nu$.

*(Weakly sub-Gaussian):* The function class $\mathcal{F}^{}:={\{{f_{\theta_{1}} - {f_{\theta_{2}}\theta_{1}}},{\theta_{2}\Theta}\}}$ satisfies a *weak-sub-Gaussian* condition \cf. [2, Def. 2.1\]: there exists $\eta{(0,1\rfloor}$ and $L1$ such that ${}f{}_{\Psi_{p}}L{}f{}_{\mathcal{L}^{2}{(\nu)}}^{\eta}$ for all $f\mathcal{F}^{}$, where ${f{}_{\Psi_{p}}}:={\sup_{k{\mathbb{N}}_{+}}{k^{- {1 \Uparrow p}}f{}_{\mathcal{L}^{p}{(\nu)}}}}$.

*(Function class regularity):* For every $x{\mathbb{R}}^{d}$, the map $\thetaf_{\theta}{(x)}$ is $L{(x)}$-Lipschitz, with ${L{(x)}{}_{\mathcal{L}^{2}{(\nu)}}} <$. Furthermore, the set $\Theta{\mathbb{R}}^{p}$ is a bounded set.

*(Burn-in):* Either (i) $mT{poly}_{\eta}{(T,p)}$ or (ii) $\{ z_{t}\}$ is $\beta$-mixing with $\beta{(k)}C{\exp{({- {\rhok}})}}$ and ${T\kappa}:={\rho^{- 1}{\log{({{CmT} \Uparrow \delta})}}}$, $mT{poly}_{\eta}{(\kappa,p)}$, where ${poly}_{\eta}{}$ denotes that the polynomial dependence is a function of $\eta$.

Then, the MLE estimator ${\hat{\theta}}_{m,T}$ satisfies with probability at least $1 - \delta$,

where $\sigma_{prox}^{2}\sigma^{2}$ is a variance proxy which is determined from the specific choice of $(p,\eta)$ in Assumption (c). In the case where $p =$, we have $\sigma_{prox}^{2} = \sigma^{2}$. Furthermore, when $p <$ and $\eta = 1$, we have that $\sigma_{prox}^{2} = {{C_{p}\sigma^{2}} + {o_{mT}{}}}$ by the martingale Rosenthal inequality (cf. A.6. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), where $C_{p}$ is a constant only depending on $p$. On the other hand, when $p <$ and $\eta < 1$, the precise relationship between $\sigma_{prox}^{2}$ and $\sigma^{2}$ is more complex. We observe that the rate (3.11) is order-wise optimal from asymptotic normality (up to the variance proxy $\sigma_{prox}^{2})$; importantly, the rate (3.11) has the correct dependence on the entire dataset size $mT$, compared with the deflated rate ${mT} \Uparrow \kappa$ from the previous single-trajectory reduction.

However, Assumptions (a)-(e) can be restrictive and/or challenging to verify. We first note that the stationary process Assumption (b) can be removed by using \[19, Theorem 4.1\] instead of \[2, Theorem 3.1\], although the downside of this is that the weakly sub-Gaussian Assumption (c) is then replaced with a trajectory-level hyper-contractivity condition (cf. \[19, Def. 4.1\]) which is more challenging to verify. On the other hand, while the weakly sub-Gaussian Assumption (c) holds broadly if $f_{\theta}$ is bounded and smooth in its input (cf. \[2, Prop. 4.1\]), the constants $(L,\eta)$ provided depend poorly on the process dimension $d$, which yields burn-in times for $m,T$ that can depend exponentially in $d$; sharp control on the $(L,\eta)$ constants is only currently available for simple function classes, e.g., linear function classes.

### Summary

The finite-sample behavior of the MLE in multi-trajectory settings is currently most broadly available through reduction to either an existing i.i.d. or single-trajectory result. In either case, there is a gap between the resulting bound (cf. (3.8) for the i.i.d. reduction and (3.9) for the single-trajectory reduction) compared with the optimal bound (3.4) in terms of effective sample sizes. In the case of least-squares regression (both for linear and more general parametric models), however, the finite-sample rate (3.6) for linear regression and (3.11) for more general parametric regression matches the CLT-optimal bound up to constant factors in the former, and up to a variance-proxy factor in the latter. This naturally raises the question whether optimal finite-sample rates can be derived beyond the square-loss setting. The proof techniques used for analyzing the square-loss (e.g., self-normalized martingales, small-ball inequalities) take advantage of either the closed-form nature of the linear regression solution, or specific properties of the square-loss such as the offset basic inequality \see e.g. and hence do not readily generalize. This motivates the need for a different approach for establishing error bounds of the form (3.4) in more general settings.

### Analyzing MLE via Localization in Hellinger Distance

We next develop a set of tools and a general five-step framework for analyzing the MLE over a diverse set of problems. The roadmap for the remainder of this section is as follows. We first develop tools in Section 3.2.1 to control the Hellinger distance of the MLE solution to the true solution in terms of their length-$T$ trajectory (path) measures. Next, we study in Section 3.2.2 how we can localize the Hellinger distance so that it approximately behaves like a weighted Euclidean norm over the parameters, where the weight is determined by the Fisher information matrix at optimality. Importantly, given sufficient trajectory-level excitation, the FI matrix scales with the trajectory length $T$, providing the correct scaling with length of each trajectory. Building on these mathematical tools, in Section 3.3 we work through a simple illustrative example combining these tools to derive a sharp rate for parameter recovery in a two-state Markov chain. Finally, we present our general Hellinger localization framework in Section 3.4.

### Divergence measures

For two measures $p,q$ over the same probability space, we define the Total-Variation (TV) distance, Hellinger distance, and Kullback-Leibler (KL) divergence as:

Note that the last definition of KL divergence require the absolute continuity condition $pq$. For what follows, we will often overload notation and write e.g., ${d_{H}{(\theta_{1},\theta_{2})}} = {d_{H}{(p_{\theta_{1}},p_{\theta_{2}})}}$ for $\theta_{1},{\theta_{2}\Theta}$ (and similarly for TV distance and KL divergences).

### Control of Trajectory Measures in Hellinger Distance

Our main approach is based on techniques used for studying density estimation with maximum-likelihood. To set the stage for what follows, we first state a prototypical non-asymptotic result from the study of maximum-likelihood estimators. The following instantiation is from and applied directly to our problem setting (3.1), although it traces its roots back to the work of. Similar instantiations of the following result can also be found in more recent works.

### Theorem 3.1 (cf. \[53, Proposition B.1\])

We have with probability at least $1 - \delta$,

where $\mathcal{N}{(\mathcal{P},\varepsilon)}$ is the $\varepsilon$-covering number of $\mathcal{P}$ in the max divergence.^66^6Specifically, a set $\mathcal{P}^{}\mathcal{P}$ is an $\varepsilon$-covering in max divergence if for every $p\mathcal{P}$ there exists a $p^{}\mathcal{P}^{}$ such that for a.e. $z_{1:T}\mathsf{Z}^{T}$, ${\log{({{{p{(z_{1:T})}} \Uparrow p^{}}{(z_{1:T})}})}}\varepsilon$. The quantity $\mathcal{N}{(\mathcal{P},\varepsilon)}$ denotes the cardinality of the smallest such $\varepsilon$-covering.

3.1. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") is a powerful result in that it controls the Hellinger divergence of the *trajectory (path)* distributions between the MLE estimator ${\hat{p}}_{m,T}{(z_{1:T})}$ and the true data-generating trajectory distribution $p{(z_{1:T})}$ at a $1 \Uparrow m$ rate, under fairly minimal assumptions on $\mathcal{P}$. In fact, the only assumption made on $\mathcal{P}$ is that its max divergence covering number is bounded. However, powerful as this result may be, extracting trajectory information out of the Hellinger divergence in order to obtain $1 \Uparrow {({mT})}$ rates is non-trivial, as the Hellinger distance does *not* in general tensorize nicely over non-product measures, unlike the KL-divergence.

Fortunately, some form of tensorization is indeed possible when ${\hat{p}}_{m,T}$ is close enough to $p$. In particular, by an asymptotic argument \see e.g. [39, Theorem 7.23\] for $\theta_{0},{\theta_{1}\Theta}$, the following local expansion holds:

Combining (3.12) with 3.1. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") yields a bound which resembles that of the CLT (3.4). Our key result is to quantify the region for which such a local expansion (3.12) holds, using a second-order Taylor expansion argument. The argument proceeds in two steps. Due to the nature of Taylor's theorem, we first need to uniformly control the performance of parameters within ${conv}{\{{\hat{\theta}}_{m,T},\theta\}}$,^77^7We define ${{conv}{\{\theta_{0},\theta_{1}\}}}:={\{{{{({1 - s})}\theta_{0}} + {s\theta_{1}s{(0,1\rfloor}}}\}}$. which we do via a star-shaped variation of 3.1. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"). We then Taylor expand the squared Hellinger distance and characterize the necessary radius conditions for (3.12) to hold.

To proceed, we first require the definition of an $\varepsilon$-cover in Hellinger distance.

### Definition 3.2 (Hellinger cover)

A set $\mathcal{P}^{}\mathcal{P}$ is an $\varepsilon$-covering of $\mathcal{P}$ in Hellinger distance if for every $p\mathcal{P}$, there exists a $p^{}\mathcal{P}^{}$ such that $d_{H}{(p,p^{})}\varepsilon$. The $\varepsilon$-covering number of $\mathcal{P}$ in Hellinger distance, denoted $\mathcal{N}_{H}{(\mathcal{P},\varepsilon)}$, is defined as the cardinality of the smallest such $\varepsilon$-covering.

One issue which arises with either Hellinger or squared Hellinger distance is that it is not convex in its parameterization, i.e., in general we have neither $\thetad_{H}{(\theta,\theta_{1})}$ nor $\thetad_{H}^{2}{(\theta,\theta_{1})}$ is convex for a fixed $\theta_{1}$; $f$-divergences are jointly convex in the space of *probability measures*, but not necessarily the specific parameterization. Thus, it will be necessary to consider another type of divergence.

For what follows, given $\theta_{0},{\theta_{1}\Theta}$, we define $\mathcal{I}{(\theta_{0},\theta_{1})}$ as the matrix:

Note that $\mathcal{I}{(\theta_{0},\theta_{1})}$ is symmetric, i.e., ${\mathcal{I}{(\theta_{0},\theta_{1})}} = {\mathcal{I}{(\theta_{1},\theta_{0})}}$. We also assume there exists a positive definite matrix $\mathcal{I}_{\max}$ such that $\mathcal{I}{(\theta)}\mathcal{I}_{\max}$ for all $\theta\Theta$. We use this to define both a symmetric averaged Fisher Information, and a max Fisher Information divergence measure:

The relationship $d_{FI}{(p_{\theta_{0}},p_{\theta_{1}})}d_{\mathcal{I}_{\max}}{(p_{\theta_{0}},p_{\theta_{1}})}$ is clear by definition. Furthermore, the max FI measure exhibits the necessary convexity of $\thetad_{\mathcal{I}_{\max}}{(\theta,\theta_{1})}$ for all fixed $\theta_{1}$, via the convexity of the weighted $\ell_{2}$ norm. We now show the following connection that these two FI distances dominate the Hellinger distance, with proof deferred to Appendix A.

### Proposition 3.3

For any $\theta_{0},{\theta_{1}\Theta}$ such that ${conv}{(\theta_{0},\theta_{1})}\Theta$, we have:

Parallel to 3.2. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), we also define a covering in terms of the max FI divergence as follows.

### Definition 3.4 (Max FI cover)

A set $\mathcal{P}^{}\mathcal{P}$ is an $\varepsilon$-covering of $\mathcal{P}$ in the max Fisher Information divergence if for every $p_{\theta}\mathcal{P}$, there exists a $p_{\theta^{}}\mathcal{P}^{}$ such that ${\theta} - {\theta^{}{}_{\mathcal{I}_{\max}}\varepsilon}$. The $\varepsilon$-covering number of $\mathcal{P}$ in the max Fisher Information divergence, denoted $\mathcal{N}_{\mathcal{I}_{\max}}{(\mathcal{P},\varepsilon)}$, is defined as the cardinality of the smallest such $\varepsilon$-covering.

Using this definition of $\varepsilon$-covering, we next introduce a *discretized* version of the MLE estimator (3.1). For $\varepsilon0$, we let $\mathcal{P}_{\varepsilon}\mathcal{P}$ denote a minimal $\varepsilon$-covering of $\mathcal{P}$ in either the Hellinger divergence (cf. 3.2. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) or max FI divergence (cf. 3.4. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"));^88^8If there is not a unique minimal $\varepsilon$-covering, then we break ties in an arbitrary way so that $\mathcal{P}_{\varepsilon}$ is not ambiguous. the specific divergence will be clear from context. We then define the MLE over this set as:

We also denote the parameters ${\hat{\theta}}_{m,T}^{\varepsilon}\Theta$ so that ${\hat{p}}_{m,T}^{\varepsilon} = p_{{\hat{\theta}}_{m,T}^{\varepsilon}}$. We further introduce the definition of the log-concavity of a parameterization of a density class.

### Definition 3.5

We say that $\mathcal{P}$ is *log-concave* if $\Theta$ is convex, and furthermore for every $\theta_{0},{\theta_{1}\Theta}$, $s{(0,1\rfloor}$, and $\mu^{T}$-a.e. $z\mathsf{Z}^{T}$,

That is, for $\mu^{T}$-a.e. $z\mathsf{Z}^{T}$, the function $\theta{\log p_{\theta}}{(z)}$ is concave over $\Theta$.

Finally, we define the max FI-diameter of $\Theta$ as:

We are now in a position to state the main result of the section.

### Theorem 3.6

Fix $\delta{}$ and resolution $\varepsilon{(0,{\delta \Uparrow {({2\sqrt{2m}})}}\rfloor}$. We have the following:

With probability at least $1 - \delta$ over the data $\mathcal{D}_{m,T}$, the Hellinger divergence discretized MLE estimator ${\hat{\theta}}_{m,T}^{\varepsilon}$ satisfies:

Furthermore, the same bound (3.15. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds for the max FI divergence discretized MLE estimator with $\mathcal{N}_{H}{(\mathcal{P},\varepsilon)}$ replaced with $\mathcal{N}_{\mathcal{I}_{\max}}{(\mathcal{P},\varepsilon)}$.

If we further assume that $\mathcal{P}$ is log-concave (cf. 3.5), then with probability at least $1 - \delta$ over the data $\mathcal{D}_{m,T}$, the max FI divergence discretized MLE estimator ${\hat{\theta}}_{m,T}^{\varepsilon}$ satisfies:

Before we turn to the proof of 3.6, several remarks are in order.

### Remark 3.7

One key difference between 3.1. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") and 3.6 is that the former applies directly to the MLE estimator ${\hat{\theta}}_{m,T}$ (3.1) over $\mathcal{P}$, whereas the latter applies to the discretized MLE estimator ${\hat{\theta}}_{m,T}^{\varepsilon}$ (3.14) over $\mathcal{P}_{\varepsilon}$. In practice there is no difference between these two estimators at a sufficiently small $\varepsilon$ below floating point resolution. However, from a theoretical perspective, the discrete estimator seems to exhibit more favorable properties than the exact MLE estimator. One of these properties is allowing one to relax the covering requirement on $\mathcal{P}$ to either Hellinger (3.15. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) or max FI-divergence (3.16. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), both which are less stringent than the max divergence covering in 3.1. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), which requires an almost sure bound on the log-density ratio. This is an important relaxation, as it allows us to handle trajectory distributions where the paths $z_{1:T}$ are not bounded almost surely; in such situations the Hellinger/max-FI divergences can still be finite as we will see in the sequel. We leave open the question of whether rates of the form (3.15. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) and (3.16. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) are possible for ${\hat{p}}_{m,T}$ without relying on max divergence coverings, noting that some extra tail conditions on $\mathcal{P}$ would be needed to control the behavior of the empirical log likelihood $\frac{1}{m}{}_{i = 1}^{m}{\log p}{(z_{1:T}^{(i)})}$.

### Remark 3.8

The key difference between (3.15. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) and (3.16. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) is that the former only controls $d_{H}{({\hat{\theta}}_{m,T}^{\varepsilon},\theta)}$, whereas the latter controls $d_{H}{(\theta,\theta)}$ along the entire ray $\theta{conv}{\{{\hat{\theta}}_{m,T}^{\varepsilon},\theta\}}$. Note that since in general neither Hellinger nor squared Hellinger distance is convex in the *parameter space*, the former in general does *not* imply the latter. Thus, (3.16. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) is a strictly stronger conclusion than (3.15. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), and therefore requires a stronger set of assumptions (e.g., log-concavity of $\mathcal{P}$). As we will see in the sequel, the conclusion (3.16. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) will play an important role in allowing $m{polylog}{(T)}$ instead of $mT{polylog}{(T)}$ minimum number of trajectories for our CLT rates to hold.

### Proof of 3.6

The proof follows the general structure of \[53, Proposition B.1\], but includes a few crucial modifications. Before we begin, we state the following upper bound on squared Hellinger distance which holds generally for two distributions $p,q$, which follows from the inequality ${\log{({1 + x})}}x$ for $x > {- 1}$:

### (a)

Let $\mathcal{P}_{\varepsilon}\mathcal{P}$ denote a minimal $\varepsilon$-covering of $\mathcal{P}$ in the Hellinger distance (cf. 3.2. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")). Let us abbreviate ${\hat{p}}^{\varepsilon}:={\hat{p}}_{m,T}^{\varepsilon}$, and for $p\mathcal{P}$ let $\varphi_{\varepsilon}{(p\rfloor}\mathcal{P}_{\varepsilon}$ denote the closest element in the Hellinger cover, i.e., $d_{H}{(\varphi_{\varepsilon}{(p\rfloor},p)}\varepsilon$. We first consider a hypothetical scenario where each $z^{(i)}:=z_{1:T}^{(i)}$ in $\mathcal{D}_{m,T}$ is drawn i.i.d. from $p^{\varepsilon}:=\varphi_{\varepsilon}{(p\rfloor}$ instead of $p$. By combining (3.17) and A.5. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") with a union bound over $\mathcal{P}_{\varepsilon}$, we have with probability at least $1 - {\delta \Uparrow 2}$ over ${(p^{\varepsilon})}^{m}$,

where the last inequality is since ${\hat{p}}^{\varepsilon}$ is the MLE over $\mathcal{P}_{\varepsilon}$ and $p^{\varepsilon}\mathcal{P}_{\varepsilon}$. On the other hand, by triangle inequality for Hellinger distance followed by the inequality ${({a + b})}^{2}2{({a^{2} + b^{2}})}$ for $a,{b{\mathbb{R}}}$,

Hence, we have shown that:

where ${\hat{p}}^{\varepsilon}{(\mathcal{D}_{m,T}\rfloor}$ is notation to emphasize that ${\hat{p}}^{\varepsilon}$ is a function of the data $\mathcal{D}_{m,T}$. Recall that ${p} - {q{}_{TV}d_{H}{(p,q)}}$ for two measures $p,q$ \cf. [39, Section 7.3\]. Hence we can change measure between $\mathcal{D}_{m,T}{(p^{\varepsilon})}^{m}$ and $\mathcal{D}_{m,T}p^{m}$ as follows:

where the last inequality follows from A.2 since we have ${d_{H}{(p,p^{\varepsilon})}\varepsilon\delta} \Uparrow {({2\sqrt{2m}})}$. This establishes (3.15. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) for the Hellinger divergence discretized ${\hat{\theta}}_{m,T}^{\varepsilon}$. The proof for the max FI divergence discretized estimator is nearly identical, and hence omitted.

### (b)

For $p\mathcal{P}$, let $\varphi_{\varepsilon}{(p\rfloor}\mathcal{P}_{\varepsilon}$ denote the closest element in the max FI-divergence $\varepsilon$-covering $\mathcal{P}_{\varepsilon}\mathcal{P}$, so that $d_{\mathcal{I}_{\max}}{(\varphi_{\varepsilon}{(p\rfloor},p)}\varepsilon$ for all $p\mathcal{P}$. We define the following parameterization of ${conv}{\{\theta,{\hat{\theta}}_{m,T}^{\varepsilon}\}}$:

We also abbreviate ${\hat{\theta}}^{\varepsilon} = {\hat{\theta}}_{m,T}^{\varepsilon}$ and $\theta^{\varepsilon} = \varphi_{\varepsilon}{(\theta\rfloor}$. Next, we let $s_{1},\ldots,{s_{N}{(0,1\rfloor}}$ be a minimal $\eta$-covering of $(0,1\rfloor$ in absolute value. For any $s{(0,1\rfloor}$, letting $s_{\eta}$ denote its nearest element in the cover, by the triangle inequality for Hellinger distance:

As in the proof of (a), we first consider a hypothetical scenario where each $z^{(i)}:=z_{1:T}^{(i)}$ in $\mathcal{D}_{m,T}$ is drawn i.i.d. from $p^{\varepsilon}:=p_{\theta^{\varepsilon}}$. By combining (3.17) and A.5. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") with a union bound over both $\mathcal{P}_{\varepsilon}$ and ${\{ s_{k}\}}_{k = 1}^{N}$, we have with probability at least $1 - {\delta \Uparrow 2}$ over ${(p^{\varepsilon})}^{m}$, abbreviating ${{\hat{\theta}}^{\varepsilon}{(s_{\eta})}}:={{\hat{\theta}}^{\varepsilon}{(s_{\eta};\theta^{\varepsilon})}}$,

where the last inequality holds from the following arguments. First note that log-concavity of $\mathcal{P}$ means that for $\mu^{T}$ a.e. $z\mathsf{Z}^{T}$, ${- {{\log p_{{\hat{\theta}}^{\varepsilon}{(s_{\eta})}}}{(z)}}} - {{({1 - s_{\eta}})}{\log p_{\theta^{\varepsilon}}}{(z)}} - {s_{\eta}{\log p_{{\hat{\theta}}^{\varepsilon}}}{(z)}}$. Hence,

and therefore we have that the empirical log-likelihood ratio satisfies:

where the last inequality holds since ${\hat{\theta}}^{\varepsilon}$ is a MLE over $\mathcal{P}_{\varepsilon}$ and $p^{\varepsilon}\mathcal{P}_{\varepsilon}$. Let us denote the event that (3.19. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds as $\mathcal{E}_{1}$. On this event, we have by (3.18. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) and ${({a + b + c})}^{2}3{({a^{2} + b^{2} + c^{2}})}$ for $a,b,{c{\mathbb{R}}}$, on $\mathcal{E}_{1}$, for every $s{(0,1\rfloor}$,

Hence, we have shown that:

Above, as in part (a), we use the notation ${\hat{\theta}}^{\varepsilon}{(\mathcal{D}_{m,T}\rfloor}$ to emphasize the dependence of the estimator on the data $\mathcal{D}_{m,T}$. We now take similar steps as in part (a) to change measure between $\mathcal{D}_{m,T}{(p^{\varepsilon})}^{m}$ and $\mathcal{D}_{m,T}p^{m}$:

where the last inequality follows from A.2 since we have ${d_{H}{(p,p^{\varepsilon})}\varepsilon\delta} \Uparrow {({2\sqrt{2m}})}$. This establishes the result. ∎

### Equivalence of Hellinger Distance and Fisher-weighted Metric

3.6 is, at its core, a result about i.i.d. learning. It however contains a rich amount of information about trajectories *within* the divergence term $d_{H}^{2}{(\theta_{m,T}^{\varepsilon},\theta)}$. In this section, we study how to extract this information out of the Hellinger divergence. As previously discussed, this is challenging as neither the Hellinger nor squared Hellinger distance tensorizes across $z_{1:T}$ in non-i.i.d. settings. However, when ${\hat{\theta}}_{m,T}^{\varepsilon}$ is close to $\theta$, such a tensorization is indeed possible, as observed via the asymptotic expansion (3.12). Our next result quantifies the radius of validity for this expansion, through a second-order Taylor expansion analysis.

### Proposition 3.9

Fix any $\theta_{0},{\theta_{1}\Theta}$ where for all $\theta{conv}{\{\theta_{0},\theta_{1}\}}$, we have (a) $\theta\Theta$ and (b) $\mathcal{I}{(\theta)}0$. Define the quantities:

Suppose that the following condition holds:

Then the following inequalities hold:

where ${\theta{(s)}}:={{{({1 - s})}\theta_{0}} + {s\theta_{1}}}$.

If in addition to (3.22. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holding, we furthermore have that:

then we also have the following inequalities:

### Remark 3.10

The constants in (3.23. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) and (3.25. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) can be made arbitrarily close to $1 \Uparrow 4$ (cf. (3.12)) at the expense of decreasing the constants in the local radius conditions (3.22. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) and (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")).

### Proof of 3.9

For $\theta\Theta$ and $z\mathsf{Z}^{T}$, define the function ${h{(\theta;z)}}:=\sqrt{p_{\theta}{(z)}}$. Abbreviating $\mu = \mu^{T}$, we take the first and second derivatives of both $\thetah{(\theta;z)}$ and $\thetad_{H}^{2}{(\theta_{0},\theta)}$:

We therefore have the identity for the Hessian $\mathcal{H}{(\theta;\theta_{0})}$:

Using the second-order integral version of Taylor's theorem and expanding $\thetad_{H}^{2}{(\theta_{0},\theta)}$ around $\theta = \theta_{0}$, with shorthand notation $\theta_{s}:={\theta{(s)}}$ and $\mathcal{I}_{s}:={\mathcal{I}{({\theta{(s)}})}}$ for $s{(0,1\rfloor}$, we have:

### (a)

Fix a vector $q{\mathbb{R}}^{p}$ and $s{(0,1\rfloor}$. We first bound:

where (a) is Cauchy-Schwarz, (b) follows by the following bounds with $q_{s}:={\mathcal{I}_{s}^{- {1 \Uparrow 2}}q}$ and using the inequality ${({a + b})}^{2}2{({a^{2} + b^{2}})}$ for $a,{b{\mathbb{R}}}$:

\(c\) follows from the basic inequalities:

and (d) follows by our stated assumption (3.26). Hence, setting $q = {\mathcal{I}_{s}^{1 \Uparrow 2}\Delta}$, we have:

Now, utilizing the second order expansion from (3.26),

The upper bound is established in a nearly identical way, which yields (3.23. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")).

### (b)

Using (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), we conclude that for all $s{(0,1\rfloor}$,

From this, we conclude that:

from which (3.25. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) follows from plugging the above semidefinite inequalities into (3.23. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")). ∎

3.9 shows that the region for which the asymptotic expansion (3.12) holds is governed by two key conditions: (i) the value of $\sup_{\theta{conv}{\{\theta_{0},\theta_{1}\}}}{d_{H}{(\theta_{0},\theta)}}$ being small enough relative to the inverse of the moment bounds $B_{1}^{2}{(\theta_{0},\theta_{1})}$ and $B_{2}{(\theta_{0},\theta_{1})}$ (cf. (3.22. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"))), and (ii) the parameters $\theta_{0},\theta_{1}$ being close enough as measured through the corresponding FI matrices (cf. (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"))). In Section 3.4, we describe the Hellinger localization framework, which gives a general recipe for verifying these conditions so that 3.6 can be used in conjunction with 3.9 to establish non-asymptotic rates for the MLE which exhibit the CLT scaling (3.4). Before describing our general framework, we first work through a specific example next in Section 3.3, which will set the stage for the general recipe.

### Two-State Markov Chain Example

We now demonstrate how the combination of 3.6 and 3.9 gives us a nearly optimal parameter recovery bound via a simple example. We consider a two-state discrete-time Markov chain, where $\mathsf{Z} = {\{ 0,1\}}$, $\Theta = {(\mu,{1 - \mu}\rfloor}$ for some $\mu{(0,{1 \Uparrow 2})}$, and $\mathcal{P}$ is the set of all two-state Markov chains with $z_{1}\rho_{1}$ (independent of $\theta$) and one-step transition probability:

For what follows, we will assume that $T2$ (otherwise no information about the Markov chain transition probabilities is revealed). We assume $p\mathcal{P}$ with parameter $\theta\Theta$. While this specific problem is simple enough that its MLE estimator can be studied via only elementary concentration inequalities (which we discuss at the end), we utilize our framework to analyze this problem in order to illustrate both the mechanics and relative sharpness of our arguments.

### Roadmap

We first compute the FI matrix $\mathcal{I}{(\theta)}$ in addition to its uniform bound $\mathcal{I}_{\max}$. From these quantities, we bound the covering number $\mathcal{N}_{\mathcal{I}_{\max}}{(\mathcal{P},\varepsilon)}$ and invoke 3.6 (b) for log-concave $\mathcal{P}$; this yields control of the Hellinger distance between $\theta$ and every element in ${conv}{\{\theta,{\hat{\theta}}_{m,T}^{\varepsilon}\}}$, where ${\hat{\theta}}_{m,T}^{\varepsilon}$ denotes the discretized MLE estimator.^99^9Specially, ${\hat{\theta}}_{m,T}^{\varepsilon}$ denotes the max FI divergence discretized MLE estimator at resolution $\varepsilon = {1 \Uparrow {({2\sqrt{2m}})}}$. With this bound in hand, we then estimate the quantities $B_{1},B_{2}$ (cf. (3.20), (3.21)); a key intermediate step is to show that control of the Hellinger distance from 3.6 implies a direct $O{({1 \Uparrow m})}$ bound on the squared parameter error, which we then use to localize the $B_{1},B_{2}$ computation in a small neighborhood around $\theta$. At this point, we are now able to invoke 3.9 (a) to boost our bound on the squared parameter error to $O{({1 \Uparrow {({mT})}})}$; the only missing piece is that this bound is not variance-optimal. However, by using this bound to establish that the condition (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds, we finally conclude by invoking 3.9 (b), which yields the instance-optimal rate.

Towards carrying out this plan, we first introduce some notation. Let us denote $\sigma^{2}:={\theta{({1 - \theta})}}$, which is the variance of a ${Bern}{(\theta)}$ distribution, and governs the curvature of the FI matrix $\mathcal{I}{(\theta)}$. We also define the set $\Theta_{\sigma}:={\{{\theta\Theta}\bigcup{\theta - {\theta\bigcup{\sigma^{2} \Uparrow 2}}}\}}$ for localization purposes: observe that for $\theta\Theta_{\sigma}$, we have $\frac{1}{\theta{({1 - \theta})}}\frac{2}{\sigma^{2}}$, a key inequality we will use in our computations.

### FI matrix, covering number, and Hellinger bound

We first gather the results of some straightforward computations in Appendix B:

From this, we bound covering number of $\mathcal{P}$ in the max FI-divergence (cf. 3.4. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) as:

Now we are in a position to apply 3.6. Setting $\varepsilon = {\delta \Uparrow {({2\sqrt{2m}})}}$ and $\eta = {{1 \Uparrow {diam}}{(\Theta)}}$, we obtain with probability at least $1 - \delta$, the max FI divergence MLE estimator satisfies:

Let us denote the event in (3.28) by $\mathcal{E}_{1}$.

### Estimate $B_{1}$ and $B_{2}$

We will estimate $B_{1}{(\theta_{0},\theta_{1})}$ and $B_{2}{(\theta_{0},\theta_{1})}$ over $\theta_{0},{\theta_{1}\Theta_{\sigma}}$. Before we proceed, we first utilize (3.28) to construct a condition on $m$ such that ${\hat{\theta}}_{m,T}^{\varepsilon}\Theta_{\sigma}$ on $\mathcal{E}_{1}$. Specifically:

where (a) uses the data processing inequality for $f$-divergences, (b) uses the inequality ${p} - {q{}_{TV}d_{H}{(p,q)}}$ for two measures $p,q$, and (c) uses the fact that $z_{1}\rho_{1}$ irregardless of $\theta$. Hence, if $m\sigma^{- 4}{\log{({{mT} \Uparrow {({\mu\delta})}})}}$, then we have that ${\hat{\theta}}_{m,T}^{\varepsilon}\Theta_{\sigma}$ on $\mathcal{E}_{1}$. By convexity of $\Theta_{\sigma}$, this implies that ${conv}{\{{\hat{\theta}}_{m,T}^{\varepsilon},\theta\}}\Theta_{\sigma}$. By A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), it suffices to take $m\sigma^{- 4}{\log{({T \Uparrow {({\mu\delta})}})}}$. In summary:

Next, we show in Appendix B that:

Hence, for any $\theta\Theta_{\sigma}$, we have:

Therefore, we have established

### Parameter error bound

We first verify the condition in (3.22. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) for $\theta_{0} = \theta$ and $\theta_{1} = {\hat{\theta}}_{m,T}^{\varepsilon}$. By combining (3.28), (3.31), and A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), it suffices to choose an $m$ satisfying:

Thus combining all requirements on $m,T$ from (3.28), (3.29), and (3.32):

Therefore by (3.23. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) from 3.9, we have on $\mathcal{E}_{1}$:

To lower bound the LHS, observe that for any $\theta\Theta$, $\mathcal{I}{(\theta)}4{({T - 1})}$. Hence for any $\theta_{0},{\theta_{1}\Theta}$, $\mathcal{I}{(\theta_{0},\theta_{1})}T$, which implies that on $\mathcal{E}_{1}$,

### Verify FI radius

We first observe for any $\theta_{0},{\theta_{1}\Theta_{\sigma}}$,

From (3.33) and (3.34), we have on $\mathcal{E}_{1}$:

By another application of A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), we can ensure the FI radius condition (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds on $\mathcal{E}_{1}$ by setting $mT\sigma^{- 4}{\log{({1 \Uparrow {({\mu\delta})}})}}$, which is already implied by $m\sigma^{- 4}{\log{({T \Uparrow {({\mu\delta})}})}}$. 3.9 now yields via (3.25. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) that on $\mathcal{E}_{1}$,

### Final result

Combining the previous arguments, the final result is that as long as $m$ satisfies:

then with probability at least $1 - \delta$ (over $\mathcal{D}_{m,T}$),

### Sharpness of the result

We now evaluate the sharpness of this result by providing an elementary solution based on sub-Exponential tail inequalities for Binomial distributions. We show in Appendix B that there exists an event $\mathcal{E}_{2}$ with probability at least $1 - \delta$ that satisfies

Comparing both the requirement on $mT$ in (3.37) to (3.35), in addition to the final error rate to (3.36), we see that the result utilizing our framework is sharp up to log factors in the final error rate, but misses a few factors in the requirement on $m$. In particular, (3.37) shows that $mT\overset{\sim}{O}{(\sigma^{- 2})}$ suffices to enter the CLT rate regime, but (3.35) requires the more conservative bound $m\overset{\sim}{O}{(\sigma^{- 4})}$. We note that the source of this conservatism is due to (a) the use of the data processing inequality to lower bound $d_{H}{({\hat{p}}_{m,T}^{\varepsilon},p)}d_{H}{({{\hat{p}}_{m,T}^{\varepsilon}{(z_{1},z_{2})}},{p{(z_{1},z_{2})}})}$ and (b) further lower bounding ${d_{H}{({{\hat{p}}_{m,T}^{\varepsilon}{(z_{1},z_{2})}},{p{(z_{1},z_{2})}})}{\hat{p}}_{m,T}^{\varepsilon}{(z_{1},z_{2})}} - {p{(z_{1},z_{2})}{}_{TV}}$. The DPI inequality (a) is lossy in this case, since it is possible to prove (at least when $\rho_{1} = {{Unif}{({\{ 1,2\}})}}$) that the tensorization property ${d_{H}^{2}{(\theta_{0},\theta_{1})}} = {1 - {({1 - {d_{H}^{2}{({{Bern}{(\theta_{0})}},{{Bern}{(\theta_{1})}})}}})}^{T - 1}}$ actually holds \see e.g. [57, Lemma 5\]. Going from Hellinger to TV distance in (b) is lossy as well since the TV distance between two Bernoulli distributions loses all local curvature information. Nevertheless, we see that our general framework is able to capture the qualitative aspects of this problem which arise from a problem-specific analysis.

### Hellinger Localization Framework

Previously in Section 3.3, we saw a specific example of how 3.9 was combined with 3.6 to establish non-asymptotic rates for MLE which exhibit nearly optimal CLT scaling from (3.3). In this section, we will utilize these two results to provide a general recipe, which we call the *Hellinger localization framework*, for establishing rates. Importantly, our framework in addition to being general purpose, does not inherently rely on any mixing, ergodicity, or stationarity properties of the process $z_{1:T}$, but instead relies on the presence of multiple independent trajectories to allow us to learn from possibly non-stationary and/or non-mixing processes. Before we present the main framework, we introduce a key identifiability condition which plays an important role.

### Definition 3.11 (Hellinger Identifiability)

We say that the parametric family $\mathcal{P}$ satisfies $(\gamma_{1},\gamma_{2})$-*Hellinger identifiability* (or $(\gamma_{1},\gamma_{2})$-*identifiability*) about the point $\theta\Theta$ if for every $p_{\theta}\mathcal{P}$:

3.11. ‣ 3.4 Hellinger Localization Framework ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") is in essence the minimal set of assumptions needed for parameter recovery; fortunately it is not hard to see that under our stated assumptions 3.11. ‣ 3.4 Hellinger Localization Framework ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") holds for some $(\gamma_{1},\gamma_{2})$ under fairly generic conditions (see A.8. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") for a precise statement). On the other, obtaining problem specific constants---especially *sharp* constants i.e., $\gamma_{2}^{- 1}\sqrt{\lambda_{\min}{({\mathcal{I}{(\theta)}})}}$ as we expect from asymptotic normality (cf. (3.3))---is non-trivial, and one of our main contributions. Indeed, our work can be contextualized as starting from a fairly sub-optimal pair $(\gamma_{1},\gamma_{2})$, and bootstrapping such a pair into a nearly optimal one; see 3.12. ‣ 3.4 Hellinger Localization Framework ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") for one particular method for obtaining a starting pair $(\gamma_{1},\gamma_{2})$. The specific steps of this recipe, which mirror the steps taken for the example in Section 3.3, are as follows:

Hellinger bound. If the density class is log-concave (cf. 3.5), or one can prove that $\thetad_{H}^{2}{(\theta,\theta)}$ is convex in the *parameter space*, we estimate the covering number $\mathcal{N}_{\mathcal{I}_{\max}}\mathcal{N}_{\mathcal{I}_{\max}}{(\mathcal{P},\varepsilon)}$ at resolution ${\varepsilon\delta} \Uparrow \sqrt{m}$ for $\mathcal{P}$, and apply 3.6, specifically (3.16. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), with $\eta{({{diam}{(\Theta)}\sqrt{m}})}^{- 1}$ to obtain the following event $\mathcal{E}_{1}$ that holds with probability at least $1 - \delta$ for a universal $c_{0}$:

Otherwise without log-concavity of $\mathcal{P}$, we rely on 3.3 to derive the bound:

Next, under the assumption of $(\gamma_{1},\gamma_{2})$-identifiability (cf. 3.11. ‣ 3.4 Hellinger Localization Framework ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), the previous inequality implies:

Applying 3.6, specifically (3.15. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), we obtain the event $\mathcal{E}_{1}$ with probability $1 - \delta$:

Estimate $B_{1}$ and $B_{2}$. We next compute upper bounds for $B_{1}B_{1}{({\hat{\theta}}_{m,T}^{\varepsilon},\theta)}$ and $B_{2}B_{2}{({\hat{\theta}}_{m,T}^{\varepsilon},\theta)}$ defined in (3.20) and (3.21). As these quantities are random variables due to the presence of ${\hat{\theta}}_{m,T}^{\varepsilon}$, we often approximate $B_{1},B_{2}$ by taking a supremum over a larger set $\Theta^{}\Theta$ for which we can ensure that ${conv}{\{{\hat{\theta}}_{m,T}^{\varepsilon},\theta\}}\Theta^{}$ on $\mathcal{E}_{1}$. For some problems, it suffices to take $\Theta^{} = \Theta$. However, for other problems, sharper estimates can be derived by more refined $\Theta^{}$. We will provide examples of both in the sequel.

Control of $B_{1}$ relies on the fact that ${{}_{}^{}p_{\theta}}{(z_{1:T})}$ forms a martingale in the realizable setting, and utilizes estimates from e.g., Burkholder's martingale Rosenthal inequality (see A.6. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") for a precise statement). Control of $B_{2}$ is often more straightforward, and a simple triangle inequality often suffices. Regarding scaling of $B_{1},B_{2}$, in the examples we work through in the sequel both scale at most poly-logarithmically in $T$.

Parameter error bound. Once $B_{1},B_{2}$ are controlled, then the upper bound on $\sup_{\theta{conv}{\{{\hat{\theta}}_{m,T}^{\varepsilon},\theta\}}}{d_{H}{(\theta,\theta)}}$ (which holds on $\mathcal{E}_{1}$) derived in Step 1 can be used to establish condition (3.22. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")). Concretely, this is done via a requirement on the minimum number of trajectories $m$. For the case when $\mathcal{P}$ is log-concave, this requirement scales as

whereas in the general case the trajectory requirement scales as

Given condition (3.22. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), 3.9 yields the following bound on the parameter error:

While this rate is still not quite the CLT rate (3.4) as the dependence on $\mathcal{I}_{2}{(\theta,{\hat{\theta}}_{m,T}^{\varepsilon})}$ is not necessarily variance optimal, for many practical applications this rate may be sufficient, especially if it is possible to show that $\mathcal{I}_{2}{(\theta,{\hat{\theta}}_{m,T}^{\varepsilon})}\Omega{(T)}I_{p}$ on $\mathcal{E}_{1}$.

Verify FI radius. In order to apply the second part 3.9 (i.e., obtain the bound (3.25. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"))), the FI radius condition (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) remains to be verified for $\theta_{0} = \theta$ and $\theta_{1} = {\hat{\theta}}_{m,T}^{\varepsilon}$. To do this, we often rely on the following upper bound:

We then proceed to show a bound on ${\mathcal{I}{(\theta_{0})}} - {\mathcal{I}{(\theta_{1})}{}_{op}}$ for $\theta_{0},{\theta_{1}\Theta}$ of the following form (see A.4 for a precise statement):

for suitable Lipschitz-like constants $L,B_{\mathcal{I}}$. This implies that

The RHS of this expression can be bounded by combining either (3.38) or (3.42) (depending on which one holds) with (3.45). Altogether, we have that condition (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds given a minimum amount of trajectories $m$ when $\mathcal{P}$ is log-concave:

where $\underset{¯}{\mu}:={{\lambda_{\min}{({\mathcal{I}_{2}{(\theta,{\hat{\theta}}_{m,T}^{\varepsilon})}})}} \Uparrow T}$. On the other hand, if $\mathcal{P}$ is not log-concave, we have that the sufficient condition for (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) to hold is

Final result. Combining all previous steps, we have that as long as:

For log-concave $\mathcal{P}$: the conditions (3.43) and (3.46) on $m$ hold,

For non-log-concave $\mathcal{P}$: the conditions (3.41), (3.44), and (3.47) on $m$ hold,

then we obtain the following rate with probability at least $1 - \delta$:

For the parametric function classes considered in this work, we will generally have ${\log{({\mathcal{N}_{\mathcal{I}_{\max}} \Uparrow \delta})}}p{\log{({{mT} \Uparrow \delta})}}$ due to the standard volumetric estimate, which yields the CLT rate (3.4) up to logarithmic factors. However, depending on the properties of the stochastic process generated by $p_{\theta}$, in particular the growth rate of the typical realization of $z_{1:T}$, the dependence on $T$ may be worse; an example of this will be given in Section 4.2.

We conclude by making a brief remark regarding the required scaling on $m$. For the log-concave $\mathcal{P}$ case, the required conditions generically yield the form $m{polylog}{(T)}$ (ignoring all other problem parameters) whereas for the non-log-concave $\mathcal{P}$ case, the scaling requirement increases to $mT{polylog}{(T)}$. For the latter case, we believe the linear scaling in $T$ to be an artifact of our analysis strategy, in particular the step taken in (3.39). We leave improving this step to future work.

### Remark 3.12 (Single-step Hellinger Identifiability)

One simple method we utilize to obtain sub-optimal---but *problem specific*---Hellinger identifiability (cf. 3.11. ‣ 3.4 Hellinger Localization Framework ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) constants is through the use of the *data processing inequality* (DPI) for $f$-divergences. Suppose that $z_{1}\rho_{1}$ for all $\theta\Theta$. Then we have:

where the equality holds from \[39, Prop. 7.2\] and the inequality is the DPI for $f$-divergences \cf. [39, Thm. 7.4\]. While the inequality above is often lossy, it is in practice often much easier to prove identifiability using the single-step distributions, i.e.,

We will show several examples of this in the sequel.

The remainder of this paper is dedicated to realizing the Hellinger localization framework on a diverse set of estimation problems, which we turn to in Section 4.

## Case Studies

This section contains the four multi-trajectory parameter recovery with ERM case studies that we consider in this work: (i) a mixture of two-state Markov chains (Section 4.1), (ii) a linear regression from dependent covariates setup with general (i.e., non-Gaussian) product-noises (Section 4.2), (iii) a GLM setup with a non-expansive, non-monotonic activation function (Section 4.3), and (iv) a simple linear-attention sequence model (Section 4.4). The problem setup and analysis for each case study is fairly self-contained, and can be read in any order.

### Mixture of Two-State Markov Chains

We build on the example from Section 3.3 by considering the following mixture formulation. Suppose we have two Markov chains $M^{}$, $M^{}$, and a Bernoulli distribution $P$ on $\{ 0,1\}$. The generative process we consider proceeds by first sampling $BP$ and $z_{1}\rho_{1}$ independently, and then generating ${z_{t + 1}z_{t}},B$ from $M_{z_{t},z_{t + 1}}^{(B)}$. The goal is to recover the parameters for the two Markov chains $M^{}$, $M^{}$ given $m$ trajectories of length $T$ from this process ($\mathcal{D}_{m,T}$), where $B^{(i)}$ is unobserved for each trajectory $i$. Such a problem is a special case of learning from mixtures of Markov chains. Our motivation for studying this problem is two-fold: (a) the parameters of both Markov chains clearly cannot be learned in a single-trajectory setting, necessitating a multi-trajectory approach, and (b) the trajectory process $\{ z_{t}\}$ is *not* $\alpha$-mixing, but we can still apply the Hellinger localization framework to derive sharp rates directly for the MLE.

Let us define $\mathcal{P}$ as instances of this Markov chain mixture with transition matrices:

where $\theta = {{(\theta_{0},\theta_{1})}\Theta}:={(\mu,{1 - \mu}\rfloor}^{2}$ with $0 < \mu < {1 \Uparrow 2}$, $P = {{Bern}{({1 \Uparrow 2})}}$, and $\rho_{1} = {{Unif}{({\{ 1,2\}})}}$. In the remainder of the section, we will use ${\mathbb{P}}_{\theta}$ to denote a trajectory measure on the space of $z_{1:}$ realized by a fixed parameter $\theta\Theta$, and for $i = {0,1}$, ${\mathbb{P}}_{\theta}^{(i)}{}:={\mathbb{P}}_{\theta}(\bigcup B = i)$. We further use ${\mathbb{E}}_{\theta}$ and ${\mathbb{E}}_{\theta}^{(i)}$ to denote expectation under ${\mathbb{P}}_{\theta}$ and ${\mathbb{P}}_{\theta}^{(i)}$ respectively, so that ${\mathbb{E}}_{\theta}{(X\rfloor} = \frac{1}{2}\left( {\mathbb{E}}_{\theta}^{}{(X\rfloor} + {\mathbb{E}}_{\theta}^{}{(X\rfloor} \right)$ for any random variable $X$.

### Mixtures are not $\alpha$-mixing

We give a short argument illustrating the lack of $\alpha$-mixing for the process $\{ z_{t}\}$. We fix a $p_{\theta}\mathcal{P}$ with $\theta_{0}\theta_{1}$. First, we recall the definition of $\alpha$-mixing and introduce some notation. For $ab$, we let $z_{a:b} = {(z_{a},\ldots,z_{b})}$, and we let $\sigma{(z_{a:b})}$ denote the $\sigma$-algebra generated by the subsequence $z_{a:b}$. The $\alpha$-mixing coefficients are defined as (cf. \[8, Eq. 2.2\], \[9, Def. 2.2\]):

The process $\{ z_{t}\}$ is denoted $\alpha$-mixing if $\alpha{(k)}0$ as $k$. We consider $\alpha$-mixing in this section, as it is the *weakest* notion of dependency used in the literature; in particular it is known that $\psi$-mixing $\phi$-mixing $\beta$-mixing $\alpha$-mixing, and furthermore $\rho$-mixing $\alpha$-mixing as well.

We now proceed as follows. A simple computation shows that for ${A_{j}\sigma{(z_{1:j})}},{B_{j,k}\sigma{(z_{{j + k}:})}}$:

Hence, by triangle inequality,

We now select $j = 2$, and let $k{\mathbb{N}}_{+}$. We define the events $A_{2}$ and $B_{2,k}$ to be:

We next observe that for $i{\{ 0,1\}}$,

and hence ${\bigcup{{{\mathbb{P}}_{\theta}^{}{(B_{j,k})}} - {{\mathbb{P}}_{\theta}^{}{(B_{j,k})}}}\bigcup} = {{\bigcup{\theta_{0} - \theta_{1}}\bigcup} \Uparrow 2}$. We also note that ${\lim_{k}{\bigcup{\Delta{(A_{2},B_{2,k})}}\bigcup}} = 0$, since we have ${\lim_{k}{\bigcup{{{\mathbb{P}}_{\theta}^{(i)}{({z_{j + k} = {1z_{j}} = 1})}} - {1 \Uparrow 2}}\bigcup}} = 0$ by the ergodicity of the individual Markov chains $M^{},M^{}$ \see e.g.,. On the other hand,

and hence ${\bigcup{{{\mathbb{P}}_{\theta}{({B = {0A_{2}}})}} - {1 \Uparrow 2}}\bigcup} > 0$ as $\theta_{0}\theta_{1}$. Therefore, we have

and hence we have that $\{ z_{t}\}$ is not $\alpha$-mixing.

### Remark 4.1

Although ${\{ z_{t}\}}_{t = 1}$ is not $\alpha$-mixing, it is ergodic as $M^{}$ and $M^{}$ admit the same stationary distribution, which implies any time average of single trajectory will converge to the same marginal expectation. In general, the mixture of Markov chain process will be non-ergodic and non-mixing as long as the candidate transition matrices have different stationary distributions.

### Remark 4.2

We remark that mixing coefficients are not fully standardized in the literature, and depending on what specific definition is adopted, the trajectory $\{ z_{t}\}$ could be considered mixing. As a specific example, in a weaker definition of $\beta$-mixing is considered, defined as $\beta{(k)} = \sup_{t1}{\mathbb{E}}_{z_{1:t}}{({\mathbb{P}}_{z_{t + k}}{(z_{1:t})} - {\mathbb{P}}_{z_{t + k}}{}{}_{TV}\rfloor}$. Under this definition $\{ z_{t}\}$ is actually $\beta$-mixing, since the $M^{(i)}$'s admit the same stationary distribution. However, there are many ways to modify the mixture model (4.1) so that it is not $\beta$-mixing under this more relaxed definition. A simple modification is

where $\theta_{i}^{} = {\theta_{i} + \tau}$ (modulating by one if necessary), where $\tau$ is a fixed offset. Another option is to consider general two-state Markov chains (so that $\theta$ contains four total parameters). For both modifications, the structure of the proof to be presented remains the same, although the detailed calculations may be different, especially for the general two-state parameterization.

Towards stating our main result, we define the following quantities for $\theta{}^{2}$:

The following is our main parameter recovery bound for the mixture of Markov chains problem.

### Theorem 4.3

Fix $\delta{}$, and define the constants $\rho:={{Gap}{(\theta)}}$ and $\sigma_{\min}^{2}:={\mu{({1 - \mu})}}$. Suppose that the following conditions hold:

$T{\max\left\{ \frac{{\overline{\sigma}}^{2}{(\theta)}}{\rho^{4}},\frac{1}{\rho^{2}} \right\}}{\log^{2}{({1 \Uparrow \mu})}}{\log\left( {\frac{{\overline{\sigma}}^{2}{(\theta)}}{{\underset{¯}{\sigma}}^{4}{(\theta)}}\frac{\log{({1 \Uparrow \mu})}}{\rho}} \right)}$,

$m{\max\left\{ \frac{1}{\rho^{4}},\frac{1}{\rho^{2}{\underset{¯}{\sigma}}^{4}{(\theta)}},\frac{T}{\rho^{2}{\underset{¯}{\sigma}}^{2}{(\theta)}} \right\}}{\log\left( {{\max\left\{ \frac{1}{\rho^{4}},\frac{1}{\rho^{2}{\underset{¯}{\sigma}}^{4}{(\theta)}},\frac{T}{\rho^{2}{\underset{¯}{\sigma}}^{2}{(\theta)}} \right\}}\frac{T}{\sigma_{\min}^{2}\delta}} \right)}$,

Let ${\hat{\theta}}_{m,T}^{\varepsilon}$ denote the max FI discretized MLE estimator (3.14) at resolution $\varepsilon = {\delta \Uparrow {({2\sqrt{2m}})}}$, and suppose the MLE estimator satisfies $\left( {\hat{\theta}}_{m,T}^{\varepsilon} \right)_{0}\left( {\hat{\theta}}_{m,T}^{\varepsilon} \right)_{1}$. With probability at least $1 - \delta$,

Some remarks are in order for 4.3. First, we note that Assumption (a) in 4.3 does not change the generality of the result, as the distribution $p_{\theta}{(z_{1:T})}$ is invariant under parameter permutation (since $B$ is sampled uniformly over the two choices), and hence we can assume wlog that $\theta_{,0} > \theta_{,1}$. Furthermore, given an MLE ${\hat{\theta}}_{m,T}^{\varepsilon}$, we can always assume wlog $\left( {\hat{\theta}}_{m,T}^{\varepsilon} \right)_{0} > \left( {\hat{\theta}}_{m,T}^{\varepsilon} \right)_{1}$, otherwise we just permute the estimator. Second, we remark that 4.3 is nearly fully *instance dependent*, i.e., both the requirements $m,T$ and the final parameter error bound on do not involve the global bound $\mu$ outside of poly-logarithmic factors, but instead depend on the problem-specific parameters $\rho,{\underset{¯}{\sigma}{(\theta)}},{\overline{\sigma}{(\theta)}}$ of the true, data-generating distribution. Third, the rate prescribed by (4.3) is in general not improvable, as it matches the two-state Markov chain argument in Section 3.3, specifically the optimal rate in (3.37).

We now discuss the requirements on $T$ via Assumption (b), and $m$ via Assumption (c). Starting with the requirement on $T$ in Assumption (b), the role of this condition is to ensure that there is sufficient information within a trajectory to distinguish which chain most likely generated the data *if the true parameters were known*; hence the scaling of ${poly}{({{1 \Uparrow {Gap}}{(\theta)}})}$ is quite intuitive. On the other hand, the requirement on $m$ in Assumption (c) parallels that of (3.35) in the two-state Markov chain case (cf. Section 3.3). The biggest difference is that in Assumption (c), we have the scaling of $m\overset{\sim}{\Omega}{(T)}$ instead of $m\overset{\sim}{\Omega}{}$ in (3.35). This comes the non-concavity of the MLE for the mixture problem, which required us to use (3.44), compared with the concave MLE for the two-state mixture; as noted in Section 3.4, the requirements on $m$ are worse for non-concave problems.

### Comparison to existing results

Learning mixture of Markov chains has been recently studied by a few authors. From this set of works, most related to ours is, where the authors develop efficient algorithms for clustering and estimating the family of transition matrices. Adapted to our specific setting, \[59, Theorem 4\] reads that when:

then their algorithm recovers an estimate ${\hat{\theta}}_{m,T}$ that satisfies with probability at least $1 - \delta$:

We note that although the result from has less stringent requirements on both the minimum number of trajectories $m$ and trajectory length $T$ compared with 4.3, the final rate (4.4) has both (i) a $1 \Uparrow {({mT^{2 \Uparrow 3}})}$ scaling in comparison to a $1 \Uparrow {({mT})}$ scaling in (4.3), and (ii) also scales proportion to $\tau_{mix}^{2 \Uparrow 3}$ as opposed to ${\overline{\sigma}}^{2}{(\theta)}$ in (4.3); note that in general $\tau_{mix}$ can grow arbitrarily large as $\theta$ approaches the boundary of the positive orthant, whereas ${{\overline{\sigma}}^{2}{(\theta)}1} \Uparrow 4$ always. On the other hand, as mentioned previously, the work provides an efficient algorithm which can also learn the distribution of the latent variable $B$, whereas our result 4.3 uses the MLE estimate which, in this case, requires maximizing a non-concave objective and does not handle the case where the distribution of $B$ must be jointly learned. Extensions of our analysis to more general mixture setups, in addition to practical algorithms such as expectation maximization, is left as interesting future work. In Section 4.1.3, we comment in more detail on how our proof techniques may be generalized to other mixture recovery problems.

### Preliminary Results for 4.3

Our analysis resembles that of the two-state Markov chain case (cf. Section 3.3), given that each trajectory can be associated with a particular chain if the trajectory length $T$ is sufficiently long. In the following, we state a few auxiliary results that will be crucial towards enabling our analysis. The following subset $\Theta^{}\Theta$ plays an important role in localizing the problem-specific parameters:

### Proposition 4.4

Fix $\theta = {{(\theta_{0},\theta_{1})}{}^{2}}$ and suppose that $\theta_{0}\theta_{1}$. Define for $i{\{ 0,1\}}$:

Fix $\varepsilon,{\delta{}}$, and suppose that $T$ satisfies:

Denote the posterior density of $B$ evaluated at $0$:

### Proof

To ease notation, we let $T^{}:={T - 1}$ for what follows. Given $z_{1:T}$, we have that

Next, since conditioned on $B = i$, the random variable $N_{stay}{(z_{1:T})}{Bin}{(T^{},\theta_{i})}$, and therefore the conditional MGF of $N_{stay}{(z_{1:T})}$ is:

By A.9, we have that with probability at least $1 - \delta$ over $z_{1:T}p_{\theta_{i}}$,

Let us temporarily call this event $\mathcal{E}$. On event $\mathcal{E}$ under $p_{\theta_{0}}$,

Therefore we have on event $\mathcal{E}$, there exists a universal $c > 0$ such that:

Now, we observe that for any $\varepsilon{}$,

To achieve the claimed result, it remains to derive sufficient conditions on $T$ so that the RHS of (4.6) is lower bounded by $\log{({{({1 - \varepsilon})} \Uparrow \varepsilon})}$. First, we require that

We also require that

Hence, we have that as long as:

The proof for ${\mathbb{P}}_{\theta}^{}$ proceeds exactly the same as above with the roles of $\theta_{0},\theta_{1}$ swapped. ∎

### Remark 4.5

We note that one could get a similar result by applying \[63, Theorem 3.9\]. However, our requirement on $T$ from the above lemma does not depend linearly on the inverse spectral gap ${(\min{\{\theta_{i},1 - \theta_{i}\}}\rfloor}^{- 1}$ of the chain defined by individual $\theta_{i}$'s.

### Corollary 4.6

Fix $\theta = {{(\theta_{,0},\theta_{,1})}\Theta}$ and $\varepsilon,{\delta{}}$. Suppose $T$ satisfies

Then for any $\theta\Theta^{}$, we have:

### Proof

First by Pinsker's inequality, we have:

Next, we have that for $\theta\Theta^{}$:

Consequently for $\theta\Theta^{}$ and $i{\{ 0,1\}}$, ${\Delta_{i}{(\theta)}{Gap}^{2}{(\theta)}} \Uparrow 2$. Next, for any $\theta\Theta$, we have:

since we assumed $\mu < {1 \Uparrow 2}$. Finally, for any $\theta\Theta^{}$ and $i{\{ 0,1\}}$,

The claim now follows from 4.4. ∎

### Corollary 4.7

Fix $\theta = {{(\theta_{,0},\theta_{,1})}\Theta}$ and $\varepsilon{}$, and suppose $T$ satisfies:

Then for any $\theta\Theta^{}$, we have:

Furthermore, fix any $k{\mathbb{N}}_{+}$ and $\eta{}$, and suppose that $T$ satisfies:

Then for any $\theta\Theta^{}$, we have:

### Proof

For the first part of the statement, we temporarily denote $\mathcal{E}:={\{{{\bigcup{{w_{\theta}{(z_{1:T})}} - 1}\bigcup} > {\varepsilon \Uparrow 2}}\}}$. Then we have, using $w_{\theta}{(z_{1:T})}{(0,1\rfloor}$:

where the last inequality holds from 4.6, given our requirement on $T$. The result for ${\mathbb{E}}_{\theta}^{}{(w_{\theta}{(z_{1:T})}\rfloor}\varepsilon$ follows using same proof.

For the second part of the statement, we invoke the first part with $\varepsilon = {\eta \Uparrow T^{k}}$, and use A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") to recover the dependence on $T$. Specifically, we require

It suffices to require that:

Applying A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") to the second inequality it suffices for $TkA{\log{({kA})}}$. Hence, simplifying further by bounding ${{\overline{\sigma}}^{2}{(\theta)}1} \Uparrow 4$ yields the claim. ∎

### Proposition 4.8

Fix $\theta = {{(\theta_{,0},\theta_{,1})}\Theta}$. Suppose $T$ satisfies:

We have for any $\theta\Theta^{}$:

where $\mathcal{I}{(\theta_{0})}$ and $\mathcal{I}{(\theta_{1})}$ are the Fisher information of the individual two-state Markov chains under $\theta_{0}$ and $\theta_{1}$ respectively (cf. Section 3.3), i.e., ${\mathcal{I}{(\theta_{i})}} = \frac{T - 1}{\theta_{i}{({1 - \theta_{i}})}}$ for $i{\{ 0,1\}}$.

### Proof

We start with calculating relevant derivatives for our mixture model $\mathcal{P}$. We recall that the parameter space is $\Theta = {(\mu,{1 - \mu}\rfloor}^{2}$. Given $\theta\Theta$, the log likelihood ratio is

Therefore the first order information is

We now compute the second order information:

we compute the Fisher information of $\theta$ as:

We now further define

We highlight the following expressions for $E_{0},E_{1}$:

With this error decomposition, we have that $\mathcal{I}{(\theta)}$ can be written as:

where in the penultimate inequality we applied Jensen's inequality, and in the last step we apply the simple inequality ${}A{}_{op}{}A{}_{F}\sqrt{nm}{\max_{i{(m\rfloor},j{(n\rfloor}}{\bigcup A_{ij}\bigcup}}$ for $A{\mathbb{R}}^{mn}$. We now recall from the two-state Markov chain example (Section 3.3) the following computation for $i = {0,1}$,

It is clear that we have

Hence, it is straightforward to show the following almost surely bounds:

From these bounds we can conclude that:

From (4.10), we have the following bound:

Since $E_{\overline{\mathcal{I}}{(\theta)}}$ is symmetric, this implies:

A nearly identical argument shows that $\overline{\mathcal{I}}{(\theta)}\left( {1 + \frac{4{({T - 1})}\zeta{\overline{\sigma}}^{2}{(\theta)}}{{\underset{¯}{\sigma}}^{4}{(\theta)}}} \right){\overline{\mathcal{I}}}_{s}{(\theta)}$. Hence, if we choose $\zeta\frac{{\underset{¯}{\sigma}}^{4}{(\theta)}}{8{\overline{\sigma}}^{2}{(\theta)}}\frac{1}{T - 1}$, we will have the desired inequality:

To conclude, we see that for any $\theta\Theta^{}$ and $i{\{ 0,1\}}$,

The RHS above implies that:

Consequently, we have for $\theta\Theta^{}$:

We now apply 4.7 with $\eta = \frac{{\underset{¯}{\sigma}}^{4}{(\theta)}}{48{\overline{\sigma}}^{2}{(\theta)}}$ and $k = 1$, from which the result follows.

### Proposition 4.9

Suppose that $T3$. The family of densities defined by (4.1) over $\Theta_{+}:={\{{\theta\Theta\theta_{0}\theta_{1}}\}}$ is $\left( {{{Gap}^{2}{(\theta)}} \Uparrow 44},{{13 \Uparrow {Gap}}{(\theta)}} \right)$-Hellinger identifiable (cf. 3.11. ‣ 3.4 Hellinger Localization Framework ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) around $\theta\Theta_{+}$.

### Proof

We first generate a table of transition probabilities for any $\theta\Theta$ over the first three elements $(z_{1},z_{2},z_{3})$, leading to eight possibilities:

$\frac{1}{4}\left( {\theta_{0}^{2} + \theta_{1}^{2}} \right)$

Table 1: A enumeration of the probabilities pθ (z1: 3) over the first three elements (z1,z2,z3) in z1: T.

We now use Table 1 to establish a lower bound for the TV distance ${p_{\theta}{(z_{1},z_{2},z_{3})}} - {p_{\theta}{(z_{1},z_{2},z_{3})}{}_{TV}}$ in terms of the parameters $\theta$ and $\theta$:

Hence by the data processing inequality, we have

Suppose we can control $d_{H}{(p_{\theta},p_{\theta})}\varepsilon$, this would imply that:

i.e., denoting $a:=\theta_{0}$, and $b:=\theta_{1}$, we have:

$S$ ${:={a^{2} + {b^{2}\left( {{\theta{}^{2}} - {4\varepsilon}},{{\theta{}^{2}} + {4\varepsilon}} \right\rfloor}}},$ (4.22a)
$Q$ ${:={a + {b\left( {{\theta{}_{1}} - {2\varepsilon}},{{\theta{}_{1}} + {2\varepsilon}} \right\rfloor}}}.$ (4.22b)

Our next step will be to solve for $(a,b)$ in terms of $(S,Q)$. To do this, we first will argue that the discriminant ${{2S} - Q^{2}} > 0$. We define the following quantities:

With this notation,

Now observe that since $\varepsilon\sqrt{2}$, we have ${{\bigcup\Delta\bigcup}8\varepsilon} + {8\varepsilon} + {4\varepsilon^{2}22\varepsilon}$, and hence:

This shows that ${{2S} - Q^{2}} > 0$, and therefore the following is the unique solution with $a > b$ to (4.22):

We next consider how $\sqrt{{2S} - Q^{2}}$ scales as a function of the perturbation $\Delta$. Let us define ${f{(\Delta)}}:=\sqrt{\rho^{2} + \Delta}$, which has derivative ${f^{}{(\Delta)}} = \frac{1}{2\sqrt{\rho^{2} + \Delta}}$. By concavity of square-root, we have:

On the other hand, by the mean value theorem for some $c$ with ${\bigcup c\bigcup}{\bigcup\Delta\bigcup}$:

We can make this interval symmetric:

Now we can conclude our analysis. We first observe that:

Next, we start with $a$. We have:

A similar argument shows that ${a\theta_{,0}} - {{{({1 + {5\sqrt{2}}})}\varepsilon} \Uparrow \rho}$, and hence we have:

Furthermore, a similar argument also shows that:

Hence, we have ${\theta} - {\theta\sqrt{2}\theta} - {{\theta13\varepsilon} \Uparrow \rho}$. Therefore, we have shown that for all $\theta\Theta^{}$:

### Remark 4.10 (On identifiability up to permutation)

We note that picking a uniform distribution for $B$ illustrates one key issue in mixture models, where we can only identify parameters up to a permutation. Therefore we have to assume some additional distinguishability between parameters (e.g., the restricted subset $\Theta_{+}$) to guarantee unique identifiability. We discuss this issue in more detail in Section 4.1.3.

### Proof of 4.3

For compactness of notation, in the proof we will use

### Covering Number Bound

We first compute an upper bound $\mathcal{I}_{\max}$ such that $\mathcal{I}{(\theta)}\mathcal{I}_{\max}$ for all $\theta\Theta$. Applying C.2 and recall the related computation in 4.8, specifically (4.11), we have:

Hence, we have for all $\theta\Theta$:

Consequently, for any $\theta,{\theta^{}\Theta}$,

Therefore we can upper bound the metric entropy

We now first apply 3.6 (a) with resolution $\varepsilon = {\delta \Uparrow {({2\sqrt{2m}})}}$, which yields an event $\mathcal{E}_{1}$ with probability at least $1 - \delta$, where on $\mathcal{E}_{1}$:

where the last inequality follows from by assumption, $m4$, and the observation

For the remainder of the proof, we will assume we are on the event $\mathcal{E}_{1}$. Invoking the Hellinger identifiability (4.9) and A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"):

We can now additionally impose (cf. A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"))

where $c$ is some constant radius. This results in the following key identity, which will be used in the sequel:

### Estimate $B_{1}$ and $B_{2}$

We now estimate $B_{1}{({\hat{\theta}}_{m,T}^{\varepsilon},\theta)}$ and $B_{2}{({\hat{\theta}}_{m,T}^{\varepsilon},\theta)}$. Our first step is to guarantee that ${\hat{\theta}}_{m,T}^{\varepsilon}\Theta^{}$ (cf. (4.5)), i.e.,

In view of (4.24), it suffices to require

We abbreviate the above to be written as:

In addition to (4.26), further requiring

implies by 4.8 that for any $\theta\text{conv}\left\{ {\hat{\theta}}_{m,T}^{\varepsilon},\theta \right\}$:

And therefore applying C.3, we have for any $\theta\text{conv}\left\{ {\hat{\theta}}_{m,T}^{\varepsilon},\theta \right\}$:

Notice each term *without* the density ratio $w_{\theta}^{(i)}{(z_{1:T})}$ resembles that what we have seen in Section 3.3. Hence we upper bound $(I)$ as:

where the third to last step follows from (3.30), and the last two steps we first set a large enough $T$ such that the last term is also $O{}$, for which our assumption (4.27) would suffice together with (4.21). A similar argument shows that

and therefore we can conclude

Now for $B_{2}$, we proceed as we did for $B_{1}$. For any $\theta\text{conv}\left\{ {\hat{\theta}}_{m,T}^{\varepsilon},\theta \right\}$:

Now using similar arguments for the upper bound of $(I)$ in (4.29), we can upper bound $({III})$:

By symmetry between $\theta_{0}$ and $\theta_{1}$, we have

Finally, we can upperbound $({VII})$:

where at the second step we again applied (4.21). Therefore $B_{2}^{2}{\max\left\{ \frac{1}{T{\underset{¯}{\sigma}}^{2}{(\theta)}},1 \right\}}$, and hence:

### Parameter error bound

Our first step is to define a more refined $\mathcal{I}_{\max}^{}$ for $\theta\Theta^{}$. From 4.8, for any $\theta\Theta^{}$:

Hence, following (3.40) using $\mathcal{I}_{\max}^{}$ instead of $\mathcal{I}_{\max}$, we obtain that:

where recall that the last inequality is from (4.23). Therefore, combining the above inequality with (4.30) and A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), condition (3.22. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds if in addition to (4.26) and (4.27) we also have:

Applying 3.9 (a), we obtain from (3.23. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")):

Furthermore, from (4.28), we have that $\mathcal{I}_{2}{(\theta,{\hat{\theta}}_{m,T}^{\varepsilon})}c_{0}TI_{2}$ for some $c_{0} > 0$, and hence the following parameter error bound holds as well:

### Verify FI radius

For the variance-weighted CLT rate, we want to show the FI radius condition (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")). By combining C.4 and (4.28), we have for any $\theta\Theta^{}$,

Hence condition (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) is implied :

Now recall from the error decomposition in (4.9), we have

By triangle inequality, a further sufficient condition is:

From Section 3.3, specifically, (3.34), we have that (4.34) can be satisfied by requiring

and in view of (4.32) and A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), this holds if:

This condition is however already implied by (4.31) (up to adjusting constant factors). We now address condition (4.35). Recalling $\mathcal{I}_{\operatorname{\mathsf{d}\mathsf{i}\mathsf{a}\mathsf{g}}}{(\theta)}{({T - 1})}I_{2}$, we have:

where (a) uses C.4, (b) uses (4.20) from the proof of 4.8, and (c) uses (4.21), and (d) uses the requirement on $T$ from (4.27) (possibly adjusting constant factors as necessary), and follows the arguments bounding $\zeta$ in (4.20) from 4.8.

### Final result

We now have the necessary requirements to invoke 3.9 (b) to conclude:

In particular, combined with 4.8, this also implies

We conclude by summarizing the requirements on $m,T$. In total, we require conditions (4.26), (4.27), and (4.31) to hold. These are readily simplified into assumptions (b) and (c) in the theorem statement, from which the result follows.

### Extensions of Proof Techniques to More General Mixture Problems

We now discuss the extent to which the proof strategy for Section 4.1 extends to general mixture distributions. We consider a density class $\mathcal{P}:=\left\{ {p_{\theta}\theta\Theta^{k}} \right\}$ over $k$ parameters ${\{\theta_{1},\ldots,\theta_{k}\}}\Theta$ where for all $ij$, $\theta_{i}\theta_{j}$, and a multinomial distribution on the index set $(k$\] parameterized by $f:={{(f_{1},\ldots,f_{k - 1})}\Delta_{\mu}^{k - 1}}$, where $f_{k}:={1 - {{}_{i = 1}^{k - 1}f_{i}}}$ and

denotes the $\mu$-strict interior of $k$-dimensional probability simplex, for $0 < {{\mu1} \Uparrow k}$. We require the weights $f_{k}$ to be in the strict interior for regularity (e.g., differentiability and exchanging derivatives with integrals) reasons. The data-generating process we consider proceeds similarly to what we considered in Section 4.1. Specifically, a latent variable $B{(k\rfloor}$ is first drawn according to ${\{ f_{i}\}}_{i = 1}^{k}$, which is then used condition the data $z_{1:T}p_{\theta_{B}}$.

### Mixture with known weights

We first suppose $f$ is known. Hence the densities $p_{\theta}\mathcal{P}$ are:

is the joint parameter to be learned. A simple computation of the first order information yields:

where $w_{\theta}^{(B)}{(z_{1:T})}$ is the posterior density of $B$ given $z_{1:T}$:

We now compute the second order information in blocks: for $1ijk$,

and the Hessian matrix ${{}_{}^{}p_{\theta}}{(z_{1:T})}$ is

We note the similarity between (4.36--4.38) and (4.7--4.8). We first consider the covering number bound. We assume for each mixture component $1ik$, we have the almost sure bounds:

where $c_{i},c_{i}^{}$ are some constants depending on system parameters such as state dimension, etc. As we will see in later sections, this is possible to show for many systems. We then have for ${1i},{jk}$,

Therefore we can apply C.1 to get

which implies $\mathcal{I}{(\theta)} = - {\mathbb{E}}_{\theta}\left( H_{\theta}{(z_{1:T})} \right\rfloor k\left( \max_{1ik}c_{i} \right)^{2}T^{2}I_{kd}$. That is, we have

which gives us a bound on the metric entropy under FI-norm:

This allows us to carry out the analysis done in Step 1.

For Step 2 onward, we inspect $w_{\theta}^{(i)}{(z_{1:T})}$:

Ideally, each component of the mixture should be identifiable from the others given long enough trajectories. Hence, a natural assumption is that when $B = i$ (i.e., $z_{1:T}p_{\theta_{i}}$), for any $ji$ the following ergodic condition holds: there exists some constant $\Delta_{ij} > 0$ such that

The immediate implication of (4.39) is that when $B = i$:

On a flip side, when $B = {ki}$, we have:

Since $w_{\theta}^{(i)}{(z_{1:T})}0$, we have $w_{\theta}^{(i)}{(z_{1:T})}\overset{T}{}0$ a.s. when $B = {ki}$. Therefore we conclude

For a concrete example of (4.39), suppose that the $p_{\theta_{i}}$'s are Markovian for each $1ik$, i.e., ${p_{\theta_{i}}{(z_{1:T})}} = {p{(z_{1})}{}_{t = 1}^{T - 1}p_{\theta_{i}}{({z_{t + 1}z_{t}})}}$. The natural ergodicity assumption in this case is the following:

where ${h_{ij}{(z_{t},z_{t + 1})}}:={\log\left( \frac{p_{\theta_{j}}{({z_{t + 1}z_{t}})}}{p_{\theta_{i}}{({z_{t + 1}z_{t}})}} \right)}$ and $\pi_{\theta_{i}}$ is the density of ergodic measure of the Markov process $\left\{ z_{t} \right\}_{t = 1}$ under $p_{\theta_{i}}$. Here, the notation denotes the following operation between a density $\pi$ and a transition density $p$: ${\pip{(z_{t},z_{t + 1})}}:={\pi{(z_{t})}p{({z_{t + 1}z_{t}})}}$. To see why this implies (4.39), observe that $\pi_{\theta_{i}}p_{\theta_{i}}$ is the density of the ergodic measure of the augmented process ${\{{(z_{t},z_{t + 1})}\}}_{t = 1}$ under $p_{\theta_{i}}$. Hence the right hand side of (4.41) reads:

Following (4.40), we can again argue that for large $T$, the Hessian (and therefore the Fisher information) can be controlled by a block-diagonal matrix of the mixture components' Fisher information matrices

under the Loewner order.

Some remarks are in order. First, for an exact analogue of 4.8, we need to prove the Loewner order equivalence holds uniformly within a ball around $\theta$. Our previous proof strategy requires characterizing non-asymptotic mixing behavior instead of the asymptotic convergence as in (4.39). In particular, if we are working with a Markov process and consider the augmented process $\left\{ {(z_{t},z_{t + 1})} \right\}_{t = 1}$ with an ergodic measure denoted by $\pi$, we expect the following Bernstein-type inequality to hold:^1010^10Here we only stated a schematic form. More precisely, under various mixing conditions, the right hand side might include additional $\operatorname{polylog}{(T)}$ factors.

where $C{(\mathcal{H})}$ typically quantifies boundedness of the function class $\mathcal{H}$. Such results are available for various classes of mixing processes (see e.g., ). In particular, stable LDS are geometrically $\beta$-mixing, and therefore \[66, Theorem 1 and 2\] are readily applicable. Specialized bounds for Markov chains are also available \see e.g., [71, Theorem 2.4\]. This would allow us to obtain instance-optimal rates for the more general mixture dynamics, including but not limited to those considered in prior art (e.g., ).

Second, we face the technical challenge that Hellinger identifiability (analogue of 4.9) does not in general hold when a subset of weights are equal. In the scalar case, as in 4.9, we worked around this issue by assuming a monotone order on the corresponding parameters to guarantee unique identifiability of parameters. In the general case, we need to redefine the notion of Hellinger identifiability to be symmetry aware. In particular, let $\mathcal{J} = {(\mathcal{J}_{1},\ldots,\mathcal{J}_{\ell})}$ partition the indices $(k\rfloor$ into $\ellk$ equivalence classes, where $f_{i_{1}} = f_{i_{2}}$ for all $i_{1},{i_{2}\mathcal{J}_{i}}$, and $f_{i_{1}}f_{j_{1}}$ for all $i_{1}\mathcal{J}_{i}$, $j_{1}\mathcal{J}_{j}$ with $ij$. Next, let ${\mathsf{S}\mathsf{y}\mathsf{m}}_{\mathcal{J}}{(\theta)}$ denote the set of cardinality ${}_{i = 1}^{\ell}{({{\bigcup\mathcal{J}_{i}\bigcup}!})}$ which given a parameter vector $\theta\Theta^{k}$ enumerates all possible permutations within each equivalence class for $\theta$. We then consider the following modified definition of Hellinger identifiability (cf. 3.11. ‣ 3.4 Hellinger Localization Framework ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), which states that there exists $(\gamma_{1},\gamma_{2})$ such that:

We note the above symmetrized condition needs to be shown on a problem-specific basis.

We conclude by remarking that under the particular outline above, it seems necessary to require ergodicity of mixture *components* to obtain non-trivial results, as otherwise the behavior of Fisher information is difficult to analyze. However, we do know that, for example, LDS with non-mixing behavior can still be identified with parametric rate from a single trajectory and so we postulate that e.g., identifying mixtures of LDS may also be possible without mixing assumptions. This reflects a limitation for our current instantiation of Hellinger localization for mixture recovery, which we leave addressing to future work.

### Mixture with unknown weights

We now extend the above calculation to the fully general setting where the joint parameter of interest is:

The density now takes the form

The cross-terms of the information matrix between the mixture weights $f$ and parameters $\theta$ are:

where the posterior weight

is defined similarly as before. Under the same ergodicity assumptions (4.39) from the previous section, both terms of (4.43) will converge to zero. We now calculate the Hessian with respect to the mixture weights:

Now under the ergodicity assumption (4.39), we can write the Hessian block ${H_{f}{(z_{1:T})}} = {{{}_{}^{}p_{\theta,f}}{(z_{1:T})}}$ and FI matrix block $\mathcal{I}{(f)} = - {\mathbb{E}}_{\theta,f}{(H_{f}{(z_{1:T})}\rfloor}$ for $T$ large as follows:

Now combining (4.42), (4.43) and (4.44) together, we obtain

This sheds light on how we can generalize the proof in Section 4.1.2 to the case where the mixture weights $f$ also need to be estimated, in addition to the mixture parameters $\theta$. Indeed, the proof strategy would be similar to that of Section 4.1.2; however, one additional challenge is that one would need to verify the Hellinger identifiability of the mixture weights.

### Dependent Regression under General Product-Noise Distributions

We next consider the following family of trajectory distributions $p_{\theta}{(z_{1:T})}$ over $\mathsf{Z} = {\mathbb{R}}^{d}$ parameterized by $\theta\Theta$ of the following form:

Here, the matrix-valued map $M:{{\mathbb{R}}^{d}{\mathbb{R}}^{dp}}$ is allowed to be non-linear, and assumed to be known. This setup generalizes the linear system identification problem detailed in Section 3.1 and has received considerable attention recently as a tractable form of non-linear system identification, especially when a control input is added to the matrix $M$, i.e., $z_{t + 1} = {{M{(z_{t},u_{t})}\theta} + w_{t}}$ (see e.g., ); a more detailed literature review is given in Section 4.2.1. The noise variable $w_{t}$ is drawn independently across time $t$ from a distribution which has the following product density w.r.t. the Lebesgue measure on ${\mathbb{R}}^{d}$:

where $\phi:{{\mathbb{R}}{\mathbb{R}}}$ is a known scalar function parameterizing the noise distribution. Hence, our setup differs from more standard settings in the following way: we do not need to assume the noise is either Gaussian or sub-Gaussian, but the functional form of the density is needed to solve the MLE. In what follows, given a vector $w{\mathbb{R}}^{d}$, we let $\mathbf{\phi}$ denote the function mapping ${\mathbb{R}}^{d}{\mathbb{R}}^{d}$ defined as ${\mathbf{\phi}{(w)}}:={({\phi{(w_{1})}},\ldots,{\phi{(w_{d})}})}$. With this notation, we can write the MLE (3.1) for (4.46) as:

We assume the following regularity conditions on $\phi$.

### Definition 4.11 (Regularity conditions on $\phi$)

We say that $\phi:{{\mathbb{R}}{\mathbb{R}}}$ is $(\beta_{1},\beta_{2})$-regular for constants ${{1\beta_{1}},\beta_{2}} <$, if the following conditions hold:

$\phiC^{2}{({\mathbb{R}})}$ and ${Z{(\phi)}} <$,

Both ${\lim_{\bigcup x\bigcup}{\phi{(x)}}} =$ and ${\lim_{\bigcup x\bigcup}{{\bigcup{\phi^{}{(x)}}\bigcup}{\exp{({- {\phi{(x)}}})}}}} = 0$,

${\mathbb{E}}_{wp_{\phi}}{({(\phi^{}{(w)})}^{2}\rfloor}\beta_{1} \Uparrow \sigma_{\phi}^{4}$, and

${\mathbb{E}}_{wp_{\phi}}{({(\phi^{}{(w)})}^{8}\rfloor}\beta_{2} \Uparrow \sigma_{\phi}^{8}$.

Before we look at a few examples of distributions satisfying 4.11. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), we briefly describe the role of each condition. Condition (a) simply ensures that $p_{\phi}$ is a well-defined $C^{2}{({\mathbb{R}})}$ density; having two derivatives is crucial in our framework, which relies on second order expansions. Condition (b) controls the growth of $p_{\phi}$ and states that $p_{\phi}$ must tend to zero in both directions which implies that ${\mathbb{E}}_{wp_{\phi}}{(\phi^{}{(w)}\rfloor} = 0$, and that the following integration by parts (IBP) identity ${\mathbb{E}}_{wp_{\phi}}{({(\phi^{}{(w)})}^{2}\rfloor} = {\mathbb{E}}_{wp_{\phi}}{(\phi^{}{(w)}\rfloor}$ holds (see 4.16); both identities play a key role in our analysis. Condition (c) ensures (via the IBP identity) that the amount of integrated curvature ${\mathbb{E}}_{wp_{\phi}}{(\phi^{}{(w)}\rfloor}$ is bounded away from zero, and is necessary for non-degenerate Fisher Information matrices $\mathcal{I}{(\theta)}$; note that in the case when $\phi$ is convex, then this condition is equivalent to $\phi^{}{(w)}$ cannot equal zero almost everywhere. Conditions (d) and (e) are *hyper-contractivity* conditions; indeed by the IBP identity (d) is equivalent to ${\mathbb{E}}_{wp_{\phi}}{({(\phi^{}{(w)})}^{2}\rfloor}\beta_{1}{({\mathbb{E}}_{wp_{\phi}}{(\phi^{}{(w)}\rfloor})}^{2}$, and similarly (e) states that ${\mathbb{E}}_{wp_{\phi}}{({(\phi^{}{(w)})}^{8}\rfloor}\beta_{2}{({\mathbb{E}}_{wp_{\phi}}{({(\phi^{}{(w)})}^{2}\rfloor})}^{4}$; by Jensen's inequality both $\beta_{1},\beta_{2}$ must be $1$.

We next build some intuition for the generality of 4.11. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), by giving a few examples below with explicit $(\beta_{1},\beta_{2})$ constants; proofs for the examples are given in Section 4.2.3.

### Example 4.12 (Multivariate normal distribution)

satisfies the conditions in 4.11. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") with $\sigma_{\phi_{\nu}}^{2} = \nu^{2}$ and ${(\beta_{1},\beta_{2})} = {}$.

### Example 4.13 (Smoothed "Bang-Bang" noise)

This corresponds to $p_{\phi_{\nu}} = {{\frac{1}{2}\mathsf{N}{(1,\nu^{2})}} + {\frac{1}{2}\mathsf{N}{({- 1},\nu^{2})}}}$, a Gaussian mixture model with two $\nu^{2}$ variance mixtures centered as $1$. If $\nu{}$, then $\phi_{\nu}$ satisfies the conditions in 4.11. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") for ${(\beta_{1},\beta_{2})} = {({c^{} \Uparrow \nu^{6}},{c^{} \Uparrow \nu^{24}})}$, where $c^{},c^{}$ are universal positive constants. Note that when $\nu0$, $p_{\phi_{\nu}}$ approaches "bang-bang" noise ${\frac{1}{2}\delta_{1}} + {\frac{1}{2}\delta_{- 1}}$.

### Example 4.14 (Smoothed Laplace distribution)

Let us define $\phi$ as:

As $c$, we have that $\phi_{c,\nu}{(x)}{\bigcup{x \Uparrow \nu}\bigcup}$ pointwise, so $p_{\phi_{c,\nu}}$ is a smoothed Laplace distribution with second-order curvature. Define $Z{(c)}:=\int\cosh{(cx)}^{- {1 \Uparrow c}}dx$. We have that $\phi_{c,\nu}$ satisfies the conditions of 4.11. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") for ${(\beta_{1},\beta_{2})} = \left( \frac{2c}{\tanh^{2}{({{cZ{(c)}} \Uparrow 4})}},\frac{16}{\tanh^{8}{({{cZ{(c)}} \Uparrow 4})}} \right)$.

With the data generating process $p_{\theta}{(z_{1:T})}$ in place, we now turn to the analysis of the MLE estimator in this model. We remark that the MLE estimator (4.48) in general for this problem is *not* the solution to a least-squares regression problem (unless $p_{\phi}$ is Gaussian), nor is it generally the solution to convex optimization problem (unless $\phi$ is convex). Furthermore, as seen in 4.14. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), the noise does not necessarily have sub-Gaussian tails as well, as is the standard assumption in many dependent learning works (e.g., ), although we note that some works have also considered heavier-tailed noise in various settings. The following is our main result regarding parameter recovery for the model (4.46).

### Theorem 4.15

Fix $\delta{}$, and suppose the following assumptions hold:

$\phi$ is $(\beta_{1},\beta_{2})$-regular per 4.11. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"),

$M_{1}:=\sup_{\theta\Theta}\left( {\mathbb{E}}_{p_{\theta}}\left( \frac{1}{T - 1}{}_{t = 1}^{T - 1}{}M{(z_{t})}{}_{op}^{4} \right\rfloor \right)^{1 \Uparrow 4} <$,

$M_{2}:=\sup_{\theta\Theta}\left( {\mathbb{E}}_{p_{\theta}}\left( \frac{1}{T - 1}{}_{t = 1}^{T - 1}{}M{(z_{t})}{}_{op}^{8} \right\rfloor \right)^{1 \Uparrow 8} <$,

$\overline{\mu}:={\sup_{\theta\Theta}{\lambda_{\max}\left( {\overline{\mathcal{I}}{(\theta)}} \right)}} <$,

$\underset{¯}{\mu}:={\inf_{\theta\Theta}{\lambda_{\min}\left( {\overline{\mathcal{I}}{(\theta)}} \right)}} > 0$, and

$T\beta_{2}^{1 \Uparrow 2}d^{2}{({M_{2} \Uparrow M_{1}})}^{4}$.

Let $\Theta = {\{{\theta{\mathbb{R}}^{p}\thetaR}\}}$, and let ${\hat{\theta}}_{m,T}^{\varepsilon}$ denote the max FI discretized MLE estimator (3.14) at resolution $\varepsilon = {\delta \Uparrow {({2\sqrt{2m}})}}$. Assume wlog that $R,M_{1},{\overline{\mu}1}$, and define $\kappa:={\overline{\mu} \Uparrow \underset{¯}{\mu}}$. Then:

If $\mathcal{P}$ is $(\gamma_{1},\gamma_{2})$-identifiable (cf. 3.11. ‣ 3.4 Hellinger Localization Framework ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) and the number of trajectories $m$ satisfies:

then with probability at least $1 - \delta$,

Here, $c_{1},c_{1}^{},c_{1}^{},c_{1}^{}$ are universal positive constants.

On the other hand if $\phi$ is convex, then as long as the number of trajectories $m$ satisfies

then with probability at least $1 - \delta$ the rate (4.49. ‣ Theorem 4.15. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) also holds, with $c_{1}$ replaced by $c_{2}$. Here, $c_{2},c_{2}^{},c_{2}^{}$ are universal positive constants.

Before turning to the proof of 4.15 (cf. Section 4.2.2), some remarks are in order. For the present discussion, we focus only on the characteristics of 4.15, deferring a detailed account and comparison to related work to Section 4.2.1. Focusing only on the parameters $m,T,p$, 4.15 states that (a) in general, if $m\overset{\sim}{\Omega}{({pT})}$, then the nearly (up to logarithmic factors) instance-optimal rate ${{\hat{\theta}}_{m,T}^{\varepsilon}} - {\theta{}_{\overline{\mathcal{I}}{(\theta)}}^{2}\overset{\sim}{O}{({p \Uparrow {({mT})}})}}$ from (4.49. ‣ Theorem 4.15. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds, and (b) if the scalar function $\phi$ parameterizing the noise distribution (4.47) is convex then the requirement on $m$ improves to $m\overset{\sim}{\Omega}{(p)}$, with the final rate (4.49. ‣ Theorem 4.15. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) remaining the same. In the $\phi$ convex case (b), the requirement on $m$ is in general not improvable, as is shown by the lower bounds in \[1, Section 6\] for linear regression. For case (a), the worse dependence comes from the non-concavity of the log-likelihood when $\phi$ is not convex, which requires us to use (3.44), compared with the concave log-likelihood when $\phi$ is convex; see the discussion in Section 3.4.

We next comment on the stated assumptions. The regularity Assumption (a) was previously discussed in the remarks following 4.11. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"). Assumptions (b) and (c) control the growth of the feature matrix $M{(z_{t})}$ over the trajectory $z_{1:T}$. By two applications of Jensen's inequality, with $T^{}:={T - 1}$,

and therefore $M_{1}M_{2}$, so assumption (c) actually implies (b). The growth of both $M_{1}$ and $M_{2}$ as a function of $T$ governs the dependence on $T$ for the minimum number of trajectories $m$; if $M$ is almost surely bounded, then $M_{1},M_{2}$ are trivially $O{}$. Assumption (d) is implied by Assumption (b), since by another application of Jensen's inequality we have $\overline{\mu}{({M_{1} \Uparrow \sigma_{\phi}})}^{2}$. Assumption (e) is states that the FI matrix $\mathcal{I}{(\theta)}$ is not degenerate over $\Theta$, and is necessary for parameter recovery. Assumption (f) is made to simplify the resulting expressions for the minimum number of trajectories $m$ required, and can be easily removed.

### Comparison to System Identification Literature

### Linear Dynamical System Identification

The LDS system identification problem reviewed in (3.5) is a special case of the model (4.46), with $p = d^{2}$, $\theta = {{vec}{(A)}}$, and ${M{(z)}} = {({z^{\mathsf{T}}I_{d}})}$. Hence 4.15 can be thought of as a generalization of the results from for multi-trajectory learning in LDS. However, there are some caveats/limitations to the extent that 4.15 truly generalizes the result. Focusing on Assumption (c), we have that ${M{(z)}{}_{op}} = {{({z^{\mathsf{T}}I_{d}})}{}_{op}} = {z}$, and hence Assumption (c) posits a uniform bound on the quantity $\chi{(\theta)}:=\frac{1}{T^{}}{}_{t = 1}^{T^{}}{\mathbb{E}}_{p_{\theta}}{(z_{t}{}^{8}\rfloor}$ as $\theta$ varies over $\Theta$. However, the quantity $\chi{(\theta)}$ exhibits two phase-transitions depending on the operator norm of ${mat}{(\theta)}$. When ${{mat}{(\theta)}{}_{op}} < 1$, then ${\chi{(\theta)}} = {O{}}$ (ignoring all constants other than $T$) by the ergodic theorem. On the other hand, when ${{mat}{(\theta)}{}_{op}} = 1$, then ${\chi{(\theta)}} = {{poly}{(T)}}$. Finally, when ${{mat}{(\theta)}{}_{op}} = \rho > 1$, we have ${\chi{(\theta)}} = \rho^{O{(T)}}$. In the last regime, the bound (4.49. ‣ Theorem 4.15. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) becomes sub-optimal compared with (3.6), and ends up scaling as $1 \Uparrow m$ instead of the optimal $1 \Uparrow {({mT})}$. Furthermore, in the ${{mat}{(\theta)}{}_{op}} = 1$ regime, the requirement on $m$ becomes $m{poly}{(T)}$, which is also not sharp. Thus, for LDS system identification, (4.46) is only sharp in the case when $R < 1$.

It is important to clarify that the main issue is not that the Hellinger framework requires stability/mixing of the process $z_{1:T}$, but instead the issue is that for LTI systems, the states $z_{t}$ can easily grow exponential in $T$ depending on the parameter $A$, which makes both covering and localization arguments extremely sensitive to minor perturbations in the parameters. The situation for LDS can be somewhat reconciled by utilizing a closed-form lower bound for the trajectory-level Hellinger distance \[56, Section 4\], which would address the sub-optimal $m{poly}{(T)}$ requirement when $R = 1$. However, when $R > 1$, this strategy would still not yield the correct rates, as we would still need to perform a covering argument under the hood.

In the least-squares analysis , the issue of uniform convergence when $A$ is not stable is handled elegantly via the special structure of the square loss. In particular, the square loss lends itself to an *offset basic inequality* which allows the uniform convergence to be *self-normalized*, preventing unstable $A$'s from adversely affecting the resulting covering numbers. We leave to future work a generalized form of self-normalization that can also be applied to log losses and the Hellinger framework. One possible starting point for this extension is the work of, which provides techniques to define and analyze offset empirical processes for logarithmic, and more generally exp-concave losses.

### Non-linear System Identification

In its general form, problem (4.46) is typically studied in its controlled variant, i.e., $z_{t + 1} = {{M{(z_{t},u_{t})}\theta} + w_{t}}$, where $z_{t}$ is interpreted as the state of a discrete-time dynamical system, and $u_{t}$ the control input at time $t$. We note that 4.15 for identifying the model (4.46) can be readily translated into this control setting with some minor modifications to incorporate the expectation over the control sequence $u_{t}$ in the Fisher information matrix, and also to include the full map $M{(z_{t},u_{t})}$ in the definitions for $M_{1},M_{2}$ in Assumptions (b), (c); we omit the exact result in the interest of space. Learning in the controlled formulation of (4.46) is studied mostly as an active learning problem, with a focus on designing optimal algorithms for selecting inputs; the necessity of active learning in the single-trajectory setting, absent smoothness conditions on $M{(z,u)}$, was demonstrated . The line of work from considers task-guided exploration, proposing an algorithm that quantifies which system parameters are most relevant to solving the task, and actively explores to minimize uncertainty in these parameters, achieving a near instance-optimal rate for the downstream task; this was later extended by to general parameteric dynamics models. Extending our Hellinger localization framework for active exploration, especially for downstream control tasks, is exciting future work.

Perhaps the most directly related work is that of, which shows that the feature map $M$ being real-analytic is sufficient to allow *non-active* i.i.d. random control signals to suffice for parameter recovery. Their arguments proceed by showing that since the zeros of the real-analytic function have measure zero, this implies that the standard martingale small-ball conditions (cf. ) used to show a lower bound on the empirical covariance matrix hold generically. This idea is also applicable to our framework, and can be used to certify non-degeneracy of the Fisher information matrix as required by Assumption (e) in 4.15 for real-analytic feature maps.

### Proof of 4.15

We first state a simple result regarding the noise distribution $p_{\phi}$ which will be useful in our analysis.

### Proposition 4.16

Given (a) and (b) of 4.11. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), the following identities are valid:

${\mathbb{E}}_{wp_{\phi}}{(\phi^{}{(w)}\rfloor} = 0$,

${\mathbb{E}}_{wp_{\phi}}{({(\phi^{}{(w)})}^{2}\rfloor} = {\mathbb{E}}_{wp_{\phi}}{(\phi^{}{(w)}\rfloor}$.

### Proof

We first note that:

For (a), we see that:

where the last equality holds from the assumption that $\phi{(w)}$ as $\bigcup w\bigcup$, and hence ${p_{\phi}{}} = 0$. For (b) using integration by parts,

where the last equality holds by the limiting behavior ${\lim_{\bigcup x\bigcup}{{\bigcup{\phi^{}{(x)}}\bigcup}{\exp{({- {\phi{(x)}}})}}}} = 0$. ∎

### Covering number bound

Let ${\mathbf{\phi}^{}{(x)}}:={({\phi^{}{(x_{1})}},{\ldots\phi^{}{(x_{d})}})}$ and ${\mathbf{\phi}^{}{(x)}}:={({\phi^{}{(x_{1})}},\ldots,{\phi^{}{(x_{d})}})}$. Using this notation, we compute the gradient and Hessian of the log probability as:

Consequently, we see that

where the last equality utilizes the IBP identity ${\mathbb{E}}_{wp_{\phi}}{(\phi^{}{(w)}\rfloor} = {\mathbb{E}}_{wp_{\phi}}{({(\phi^{}{(w)})}^{2}\rfloor}$ from 4.16. Furthermore, we can construct a uniform bound $\mathcal{I}_{\max}$ using the definition of $\overline{\mu}$:

Therefore we have an upper bound for the metric entropy under the max-FI divergence:

From 3.6, with probability at least $1 - \delta$,

Hence by the arguments outlined in (3.42) combined with A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), as long as

then whenever (4.50) holds, we have

Call this event $\mathcal{E}_{1}$. Furthermore, since the log-likelihood of $z_{1:T}$ for $\theta\Theta$ can be written as:

where $const$ does not depend on $\theta$, when $\phi$ is convex, then $\mathcal{P}$ is log-concave (cf. 3.5). It is not hard to see that ${{diam}{(\Theta)}} = {2RT\overline{\mu}}$. Hence from 3.6, with probability at least $1 - \delta$,

Call this event $\mathcal{E}_{1,{cvx}}$.

### Estimate $B_{1}$ and $B_{2}$

We first focus on $B_{1}$. Let us fix a test vector $v{\mathbb{R}}^{p}$, and define $d_{t}:={v^{\mathsf{T}}M^{\mathsf{T}}{(z_{t})}\mathbf{\phi}^{}{(w_{t})}}$, so that for $z_{1:T}p_{\theta}$,

Our first observation is that, with $\mathcal{F}_{t}:={\sigma{(z_{1:{t + 1}})}}$, we have ${\mathbb{E}}{(d_{t}\mathcal{F}_{t - 1}\rfloor} = {\mathbb{E}}{(v^{\mathsf{T}}M^{\mathsf{T}}{(z_{t})}\mathbf{\phi}^{}{(w_{t})}\mathcal{F}_{t - 1}\rfloor} = 0$ by 4.16, and hence ${(d_{t})}_{t1}$ is a MDS adapted to the filtration ${(\mathcal{F}_{t})}_{t1}$. Next, we compute:

Now since ${\mathbb{E}}_{wp_{\mathbf{\phi}}}{(\phi^{}{(w_{j})}\phi^{}{(w_{k})}\rfloor} = {({\mathbb{E}}_{wp_{\phi}}{(\phi^{}{(w)}\rfloor})}^{2} = 0$ for $j,k{(d\rfloor}$ with $jk$ by coordinate-wise independence of $p_{\mathbf{\phi}}$ and 4.16, we have that

Now let us focus on ${\mathbb{E}}{(d_{t}^{4}\rfloor}$:

where the penultimate inequality follows from Hölder's inequality, and the last inequality follows from 4.11. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"). Hence,

Now we will set $v = {\mathcal{I}{(\theta)}^{- {1 \Uparrow 2}}\overline{v}}$ where $\overline{v}{\mathbb{S}}^{p - 1}$ is a unit test vector; hence ${}v{}\sqrt{\sigma_{\phi}^{2} \Uparrow {({\underset{¯}{\mu}T})}}$. By Rosenthal's inequality for MDS (A.6. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), we have:

where the last inequality holds from Assumption (f). Hence we have

We next focus on $B_{2}$. We first fix a vector $q{\mathbb{R}}^{d}$, and observe that

where the last inequality holds from 4.11. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") and the IBP identity (cf. 4.16) ${\mathbb{E}}_{wp_{\theta}}{(\phi^{}{(w)}\rfloor} = {\mathbb{E}}_{wp_{\theta}}{({(\phi^{}{(w)})}^{2}\rfloor} = \sigma_{\phi}^{- 2}$. Hence fixing a test vector $v{\mathbb{R}}^{p}$, we have

Now again we choose $v = {\mathcal{I}{(\theta)}^{- {1 \Uparrow 2}}\overline{v}}$ for a unit norm $\overline{v}{\mathbb{R}}^{p}$. We then have

Altogether, we can bound

### Parameter error bound

We first cover the case where $\phi$ is not convex. Combining (4.52), (4.54), and A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), as long as $m$ satisfies (4.51) and also

then condition (3.22. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds on $\mathcal{E}_{1}$. Hence from 3.9, combining (3.23. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) with (4.52), we have on $\mathcal{E}_{1}$:

We now turn to the case where $\phi$ is convex. Combining (4.53), (4.54), and A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), we see that if $m$ satisfies:

Hence from 3.9, combining (3.23. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) with (4.53), we have on $\mathcal{E}_{1,{cvx}}$,

### Verify FI radius

In order to verify the FI radius condition (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), we will make use of A.3. Fix $\theta_{1},{\theta_{2}\Theta}$ and a unit norm $v{\mathbb{S}}^{p - 1}$. We have the following:

where (a) follows from A.3 and (b) follows from Jensen's inequality. Hence by the variational characterization of operator norm, for any $\theta\Theta$:

Hence from (4.52) and A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), as long as $m$ satisfies (4.51), (4.55), and

then the FI radius condition (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds on $\mathcal{E}_{1}$. On the other hand when $\phi$ is convex, from (4.53) and A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), as long as $m$ satisfies (4.56) and:

then the FI radius condition (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds on $\mathcal{E}_{1,{cvx}}$. The result for both cases now follows from 3.9, specifically (3.25. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")).

### Proof of Regularity Conditions for Example Distributions

### Proof for smoothed bang-bang noise (4.13. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"))

We abbreviate $p_{\nu} = p_{\phi_{\nu}}$. We have that ${\phi_{\nu}^{}{(x)}} = {\frac{x}{\nu^{2}} - {\frac{1}{\nu^{2}}{\tanh{({x \Uparrow \nu^{2}})}}}}$ and ${\mathbb{E}}_{xp_{\nu}}{(x^{2}\rfloor} = 1 + \nu^{2}$. For any $\varepsilon{}$, we have by Young's inequality

Basic calculus yields

Hence we have show that

Furthermore, imposing the restriction that $\nu{}$, a second order Taylor expansion around $\nu = 0$ yields that $\sqrt{1 + \nu^{2}} - {1\frac{\nu^{2}}{2^{3 \Uparrow 2}}}$ and hence ${\sigma^{- 2}\nu^{2}} \Uparrow 8$. Next, we compute ${\phi_{\nu}^{}{(x)}} = {\frac{1}{\nu^{2}} - {\frac{1}{\nu^{4}}{{sech}^{2}{({x \Uparrow \nu^{2}})}}}}$, and hence

Hence we can set $\beta_{1} = {8 \Uparrow \nu^{6}}$. Next, we have

For each mixture index $i{\{ 1,2\}}$, we have

Hence we can set ${\beta_{2}1} \Uparrow \nu^{24}$. ∎

### Proof for smoothed Laplace noise (4.14. ‣ 4.2 Dependent Regression under General Product-Noise Distributions ‣ 4 Case Studies ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"))

The first and second derivatives of $\phi_{c,\nu}$ are:

Define $Z{(c,\nu)}:=\int\cosh{(cx \Uparrow \nu)}^{- {1 \Uparrow c}}dx$. By a change of variables, ${Z{(c,\nu)}} = {\nuZ{(c)}}$. Also for $t{(0,{1 \Uparrow \nu})}$,

We control the RHS probability :

Choosing $t^{}$ such that $\frac{2{\tanh^{- 1}{({t^{}\nu})}}}{cZ{(c)}} = {1 \Uparrow 2}$, i.e., $t^{} = {\nu^{- 1}{\tanh{({{cZ{(c)}} \Uparrow 4})}}}$:

Now let us focus on controlling $\beta_{1}$. We have:

Hence we can take $\beta_{1} = \frac{2c}{\tanh^{2}{({{cZ{(c)}} \Uparrow 4})}}$. We next focus on controlling $\beta_{2}$. We have:

Hence we can take $\beta_{2} = \frac{16}{\tanh^{8}{({{cZ{(c)}} \Uparrow 4})}}$. ∎

### Non-Monotonic Sinusoidal GLM Dynamics

For our next setup, we consider the following generalized linear model (GLM) of dynamics, given parameters $A{\mathbb{R}}^{dd}$,

where $\sin{}$ is overloaded to apply component-wise given a vector input, and $w_{t}$ is drawn independently across time. While more general GLM dynamics $z_{t + 1} = {{\phi{({Az_{t}})}} + w_{t}}$ have been studied in the literature in the context of system identification, the specific sinusoidal GLM we consider is more challenging as it is an instance of a *non-monotonic*, *non-expansive*^1111^11An activation function $\phi{(x)}$ is *expansive* if there exists a $\zeta > 0$ such that ${\bigcup{{\phi{(x)}} - {\phi{(y)}}}\bigcup}\zeta{\bigcup{x - y}\bigcup}$ for all $x,{y{\mathbb{R}}}$. activation function. Furthermore, we do not impose any stability assumptions on the $A$ matrix in (4.58), as is done in prior works. The following theorem is our main result for parameter recovery in this model. In the following result, we let ${\hat{\theta}}_{m,T}^{\varepsilon} = {{vec}{({\hat{A}}_{m,T}^{\varepsilon})}}$ and $\theta = {{vec}{(A)}}$.

### Theorem 4.17

Fix $\delta{}$. Consider the max FI discretized MLE at resolution $\varepsilon = {\delta \Uparrow {({2\sqrt{2m}})}}$ over the set $\Theta = {\{{A{\mathbb{R}}^{dd}A{}_{F}R}\}}$ for $R1$. Put $A_{,\min}:=\min_{j{(d\rfloor}}{}A{(j\rfloor}{}$, where $A{(j\rfloor}{\mathbb{R}}^{d}$ denotes the $j$-th row of $A$, and suppose $A_{,\min} > 0$. Suppose also that $Td^{2}$. There exists constants $\Phi_{i}$, $i{\{ 1,2,3\}}$, which scale as ${poly}{(\sigma,{1 \Uparrow \sigma},{1 \Uparrow A_{,\min}},{1 \Uparrow d})}$, such that if $m$ satisfies for universal positive constants $c_{0},c_{1},c_{2}$:

then with probability at least $1 - \delta$ over $\mathcal{D}_{m,T}$,

The precise expressions for $\Phi_{i}$ are given in the proof.

where we emphasize that the expression on the RHS is over a *fresh* trajectory $z_{1:T}p_{\theta}$ that is independent of $\mathcal{D}_{m,T}$. Nevertheless, there is not a simple closed-form reduction and hence we leave it in its present form. If we treat $\sigma$, $R$, and $A_{,\min}$ as constants, then 4.17 states that whenever both $m\overset{\sim}{\Omega}{({d^{11}T})}$ and $Td^{2}$, then the nearly (up to logarithmic factors) instance-optimal rate ${{\hat{\theta}}_{m,T}^{\varepsilon}} - {\theta{}_{\overline{\mathcal{I}}{(\theta)}}^{2}\overset{\sim}{O}{({d^{2} \Uparrow {({mT})}})}}$ holds with high probability. We suspect that the $m\overset{\sim}{\Omega}{(d^{11})}$ requirement is sub-optimal and can be further improved with a more refined analysis. On the other hand, the requirement on $Td^{2}$ is made to simplify the expressions in the proof and can be removed. Furthermore, in our proof we show that ${\lambda_{\min}{({\overline{\mathcal{I}}{(\theta)}})}1} \Uparrow d^{2}$, which implies the parameter bound ${{\hat{\theta}}_{m,T}^{\varepsilon}} - {\theta{}^{2}\overset{\sim}{O}{({d^{4} \Uparrow {({mT})}})}}$. We leave to future work a sharp analysis of $\lambda_{\min}{({\overline{\mathcal{I}}{(\theta)}})}$ to determine the optimal *un-weighted* parameter error bound.

### Comparison to existing results

To the best of our knowledge, this is the first rate for parameter recovery in any GLM dynamics model in the multi-trajectory setting, which obtains a nearly instance-optimal rate of $\overset{\sim}{O}{({d^{2} \Uparrow {({mT})}})}$. The previous sharpest rate for this problem utilizes the fact that the MLE ${\hat{\theta}}_{m,T}$ for this problem involves solving a realizable, parametric least-squares ERM problem, and hence the reduction described in Section 3.1 to the result of would provide a similar bound on the *excess risk*, but not the weighted parameter error directly; as described in Section 3.1, however, without verification of the weakly sub-Gaussian condition specifically for the function class $\{{{\sin{({A_{1}x})}} - {{\sin{({A_{2}x})}}A_{1}}},{A_{2}\Theta}\}$ (which to the best of our knowledge has not been shown in the literature), the best burn-in requirement on $m,T$ that this reduction can provide depends exponentially on the process dimension $d$. On the other hand, 4.17 requires that both $m{poly}{(d)}T$ and $T{poly}{(d)}$ requirement; while it is likely that our exact polynomial dependence is not optimal, we are able to break the exponential in $d$ barrier of existing results.

In the single-trajectory setting, several recent works have explicitly studied parameter recovery for GLM dynamics. However, the specific setting (4.58) we consider does not satisfy the requisite assumptions for any of these works, and hence these works cannot be used as a basis for reduction. To start, the works all assume a model class with a 1-Lipschitz monotonic activation function $\phi$, with fast rates further requiring $\phi$ to be expansive. The $\sin$ function only satisfies the $1$-Lipschitz requirement; the bounded and oscillatory nature of $\sin$ violates the other assumptions. The work requires a one-point convexity assumption on the population loss, which is challenging to verify; they are only able to verify their condition assuming uniformly monotonic activations (i.e., ${\phi^{}\zeta} > 0$). Regarding stability of $A$, additionally assume Lyapunov stability conditions, specifically that there exists a diagonal positive definite $K$ and scalar $\rho < 1$ such that $AKA\rhoK$; however, it is immediately obvious that this does not hold in our setting as we permit $A = {cI_{d}}$ for $c > 1$, which would require ${\rhoc^{2}} > 1$. This also violates the explicit assumption made in some works that ${A{}_{op}} < 1$. Other works such as made explicit exponential regularity assumptions on the trajectories that given a noise sequence ${\{ w_{t}\}}_{t = 1}^{T - 1}$, the difference in states from two initial states will expand at most by a factor of $\rho = {1 + {O{({1 \Uparrow T})}}}$ every timestep; however, this is also violated in our setting.^1212^12Concretely, our setup does not satisfy \[27, Assumption 4\] for any ${\rho1} + {O{({1 \Uparrow T})}}$, as we now show. Let $\Phi_{t}{(z)}$ denote the value of $z_{t}$ following the dynamics $z_{t + 1} = {\sin{({2z_{t}})}}$ starting at $z_{1} = z$. Suppose there exists positive ${c_{1},\rho} = {1 + {c_{2} \Uparrow T}}$ such ${\bigcup{{\Phi_{t}{(z)}} - {\Phi_{t}{(z^{})}}}\bigcup}c_{1}\rho^{t}{\bigcup{z - z^{}}\bigcup}$ for all $z,{z^{}{\mathbb{R}}}$ and $t{\mathbb{N}}$. Clearly we have ${\Phi_{t}{}} = 0$ for all $t$. Furthermore, one can show that ${\lim_{t}{\Phi_{t}{(z)}}} = r$, where $r0.94775$ is the unique solution to $r = {\sin{({2r})}}$ in $(0,1\rfloor$, for all $z{(0,1\rfloor}$. Now, let $T_{0}$ be such that ${{\bigcup{{\Phi_{t}{(\overline{z})}} - r}\bigcup}r} \Uparrow 2$ for all $tT_{0}$, where $\overline{z}:={r \Uparrow {({4c_{1}e^{c_{2}}})}}$ (we can always take $c_{1},c_{2}$ large enough so that $\overline{z}{}$). Hence, for any $TT_{0}$, we have ${{r \Uparrow 2}{\bigcup{\Phi_{T}{(\overline{z})}}\bigcup}c_{1}\rho^{T}{\bigcup\overline{z}\bigcup}c_{1}e^{c_{2}}{\bigcup\overline{z}\bigcup}} = {r \Uparrow 4}$, a contradiction.

### Hellinger identifiability for sinusoidal GLMs

Before we turn to applying the Hellinger localization framework to this problem, we discuss the main technical challenge: absent the strict monotonically increasing activation function assumption ${\phi^{}{(x)}\gamma} > 0$, establishing both that (a) $\mathcal{I}{(\theta)}\Omega{(T)}I_{d^{2}}$ and that (b) $d_{H}^{2}{({\hat{p}}_{m,T}^{\varepsilon},p)}\gamma^{2}$ implies ${{\hat{\theta}}_{m,T}^{\varepsilon}} - {\theta{}^{2}\gamma^{2}}$ (i.e., Hellinger identifiability (3.11. ‣ 3.4 Hellinger Localization Framework ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"))) becomes substantially more challenging. A key step towards establishing identifiability is to show the bound $\gamma^{2}:={\mathbb{E}}_{z\mathsf{N}{(0,{\sigma^{2}I_{d}})}}{({(\sin{(u_{1},z)} - \sin{(u_{2},z)})}^{2}\rfloor}\sigma^{2}{}u_{1} - u_{2}{}^{2}$ when $\gamma^{2}$ is sufficiently small. We believe this result, which is detailed in Appendix D, to be of independent interest, and may be helpful in e.g., analyzing neural networks with sinusoidal activation functions. We remark that a similar bound is shown for ReLU activations in \[38, Lemma 11\], in particular for $z\mathsf{N}{(\mu,{\sigma^{2}I_{d}})}$, ${\mathbb{E}}_{z}{({({ReLU}{(u_{1},z)} - {ReLU}{(u_{2},z)})}^{2}\rfloor}\frac{\sigma^{2}}{4}e^{- {{\mu{}^{2}} \Uparrow \sigma^{2}}}{}u_{1} - u_{2}{}^{2}$. A key difference is in how this style of result is used in our analysis versus . In our analysis, the Hellinger identifiability is only used for the first two timestep as noted in 3.12. ‣ 3.4 Hellinger Localization Framework ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), and hence we only need to consider taking expectation over $z\mathsf{N}{(0,{\sigma^{2}I_{d}})}$. On the other hand, proves identifiability at every timestep in order to relate parameter recovery error to average prediction error; hence their analysis is required to consider non-zero means $\mu$'s, leading to parameter error rates that have an $e^{d}$ dependence on the dimension in general (cf. \[38, Theorem 3\]).

### Proof of 4.17

We will let $\theta = {{vec}{(A)}{\mathbb{R}}^{d^{2}}}$, $\Theta = {\{{\theta{\mathbb{R}}^{d^{2}}\thetaR}\}}$, and define the map ${M{(z)}}:={({z^{\mathsf{T}}I_{d}})}$ so that ${Az} = {M{(z)}{vec}{(A)}} = {M{(z)}\theta}$. For what follows, we will often use $A$ and $\theta$ interchangeably, and similarly for $A$ and $\theta$, choosing whichever notation is more convenient.

### Step 1: Covering number bound

Define ${h_{\theta}{(z)}}:={\sin{({M{(z)}\theta})}}$ and its Jacobian w.r.t. $\theta$ ${D_{\theta}h_{\theta}{(z)}} = {{{\operatorname{\mathsf{d}\mathsf{i}\mathsf{a}\mathsf{g}}{({\cos{({M{(z)}\theta})}})}}M}{(z)}}$ (similar to $\sin{}$, $\cos{}$ is also overloaded to apply component-wise given a vector input). We observe that

Let us start with an upper bound. Since $\cos{(x)}^{2}{(0,1\rfloor}$, we can see that ${\operatorname{\mathsf{d}\mathsf{i}\mathsf{a}\mathsf{g}}{({\cos^{2}{({M{(z_{t})}\theta})}})}}I_{d}$. This allows us to simplify the expression:

We now turn to analyzing ${\mathbb{E}}_{z_{t}p_{\theta}{({z_{t - 1}})}}{(z_{t}z_{t}^{\mathsf{T}}\rfloor}$. Expanding $z_{t} = {\mu_{t - 1} + w_{t - 1}}$ for $\mu_{t - 1} = {h_{\theta}{(z_{t - 1})}}$ and observing that ${\mathbb{E}}{(w_{t - 1}\rfloor} = 0$, we can see:

We fix a $v{\mathbb{R}}^{d}$ with unit norm, observe $\sin{(x)}^{2}{(0,1\rfloor}$, and bound the outer product of $\mu_{t - 1}$:

Putting this all together gives the maximum eigenvalue of the Fisher information:

We note that this is a parameter agnostic upper bound, and as such we can set $\mathcal{I}_{\max} = {\frac{T}{\sigma^{2}}{({d + \sigma^{2}})}I_{p}}$. By D.5 and the data processing inequality, for any $\theta\Theta$,

This shows that $\mathcal{P}$ is $(\gamma_{1},\gamma_{2})$-identifiable (cf. 3.11. ‣ 3.4 Hellinger Localization Framework ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) for constants:

Our next step is to apply 3.6 to ensure that the LHS condition in (4.59) holds. To do this, we shall estimate the covering number of $\mathcal{P}$ in the max FI divergence through the $\ell_{2}$ covering number. If we fix some $\theta\Theta$ and let $\theta^{}$ denote its closest element in an $\varepsilon$-covering of $\Theta$ in $\ell_{2}$,

This allows the relation

We now apply 3.6 with $\varepsilon = {\delta \Uparrow {({2\sqrt{2m}})}}$ to conclude that with probability at least $1 - \delta$:

where $c_{0}$ is a universal positive constant. Call this event $\mathcal{E}_{1}$. If we define ${1 \Uparrow \Phi_{0}}:={\min{\{ 1,{1 \Uparrow \sigma^{2}}\}}}$, plugging this bound into (4.59) and applying A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") yields that if $m$ satisfies

where $c_{0}^{}$ is a universal constant, then the following also holds on $\mathcal{E}_{1}$:

For what follows, we define the set

A key property of $\Theta^{}$ that we will utilize is that $\theta\Theta^{}$ implies ${}{mat}{(\theta)}{(j\rfloor}{}{}{mat}{(\theta)}{(j\rfloor}{} \Uparrow 2$ for all $j{(d\rfloor}$ by the triangle inequality.

### Ensuring that ${\hat{\theta}}_{m,T}^{\varepsilon}\Theta^{}$ on $\mathcal{E}_{1}$

Using D.5 and (4.60), we have that if $m$ satisfies,

then we have that ${\hat{\theta}}_{m,T}^{\varepsilon}\Theta^{}$ on $\mathcal{E}_{1}$. Using A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), this holds whenever $m$ satisfies:

where $c_{1}$ is another univeral constant. We can note that since $\Phi_{1}\Phi_{0}$, this constraint automatically satisfies (4.61) (possibly after adjusting the value of $c_{1}$).

### Lower bound FI matrix

Our first task is to estimate a lower bound on the FI matrix for $\theta\Theta^{}$. Recall the Fisher information from earlier:

We can expand $z_{t} = {\mu_{t - 1} + w_{t - 1}}$ for $\mu_{t - 1} = {h_{\theta}{(x_{t - 1})}}$ to expand the dependency of the expectation on the previous timestep.

We choose a $\nu_{0}$ to be specified later, and observe that by D.1 and a union bound, with $A = {{mat}{(\theta)}}$ and $A{(j\rfloor}{\mathbb{R}}^{d}$ denoting the $j$-th row of $A$,

Call this event, which depends on $\mu_{t - 1}$, $\mathcal{E}_{\mu_{t - 1}}$. Letting $A_{\min}:=\min_{j{(d\rfloor}}{}A{(j\rfloor}{}$, we now write:

where the last equality follows from the bi-linearity of the Kronecker product. We now fix a $v{\mathbb{R}}^{d}$ with unit-norm, and observe, dropping subscripts on $t$ for clarity,

where the last inequality holds by hyper-contractivity of Gaussian polynomials \see e.g., [86, Ch. 5\]. Hence we set $\nu_{0} = {1 \Uparrow 324}$, from which we conclude

Consequently, we have that

Therefore, we conclude that:

Up until this point, we have not used the assumption that $\theta\Theta^{}$. Observe that ${A_{\min}A_{,\min}} \Uparrow 2$ whenever $\theta\Theta^{}$, we finally conclude that for $\theta\Theta^{}$,

### Step 2: Estimating $B_{1}$ and $B_{2}$

We will estimate $B_{1}$ and $B_{2}$ over $\Theta^{}$. We start with $B_{1}$. First, given a trajectory $z_{1:T}p_{\theta}$, we have that

Now fix a test vector $v{\mathbb{R}}^{d^{2}}$, and consider:

A useful inequality is the following.

We next bound ${\mathbb{E}}{(z_{t}{}^{4}\rfloor}$ as:

Using this bound,

Since ${}w_{t}{}$ is a $\sigma$-sub-Gaussian random variable, we know that ${\mathbb{E}}{(w_{t}{}^{8}\rfloor}\sigma^{8}d^{4}$. On the other hand,

where the last inequality holds since we assume $Td^{2}$. Now we set $v = {\mathcal{I}{(\theta)}^{- {1 \Uparrow 2}}\overline{v}}$ for a unit norm $\overline{v}$, we have that

We now move to $B_{2}$. First we define the vector-valued function for a fixed $q{\mathbb{R}}^{d}$:

The Jacobian of $g{(\theta;z,q)}$ is given :

where denotes the Hadamard (entry-wise) product. Now we have

Hence, given a test vector $v{\mathbb{R}}^{d^{2}}$, given $z_{1:T}p_{\theta}$, for all $t{(T - 1\rfloor}$ we have:

Now we set $v = {\mathcal{I}{(\theta)}^{- {1 \Uparrow 2}}\overline{v}}$ for a unit norm $\overline{v}$, we have that

Finally, we conclude that

### Step 3: Parameter error bound

Utilizing (4.62) and (4.65), we have that to verify the condition (3.22. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) for $\theta_{0} = \theta$ and $\theta_{1} = {\hat{\theta}}_{m,T}^{\varepsilon}$ on $\mathcal{E}_{1}$, we need $m$ to satisfy:

by A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") it suffices for $m$ to satisfy:

From (4.64), we have that on $\Theta^{}$, the following lower bound $\inf_{\theta\Theta^{}}{\lambda_{\min}{({\mathcal{I}{(\theta)}})}\frac{T}{d^{2}}{\min{\{ 1,{\sigma^{2}A_{,\min}^{2}}\}}}}$ holds. Since (a) (3.22. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds for $\theta_{0} = \theta$ and $\theta_{1} = {\hat{\theta}}_{m,T}^{\varepsilon}$ implies (3.22. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) also holds for $\theta_{0} = \theta$ and any $\theta_{1}{conv}{\{{\hat{\theta}}_{m,T}^{\varepsilon},\theta\}}$ and (b) ${\hat{\theta}}_{m,T}^{\varepsilon}\Theta^{}$ implies ${conv}{\{{\hat{\theta}}_{m,T}^{\varepsilon},\theta\}}\Theta^{}$, by (3.23. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) from 3.9, we have on $\mathcal{E}_{1}$, for every $\theta{conv}{\{{\hat{\theta}}_{m,T}^{\varepsilon},\theta\}}$,

where the last inequality holds since we assume that $Td^{2}$.

### Step 4: Verify FI radius

We will utilize A.4 to verify the FI radius condition (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")). Since ${{{}_{}^{}p_{\theta}}{({z_{t + 1}z_{t}})}} = {- {\frac{1}{\sigma^{2}}{({D_{\theta}h_{\theta}{(z_{t})}})}^{\mathsf{T}}{({{h_{\theta}{(z_{t})}} - z_{t + 1}})}}}$ for $t1$, we have for any $\theta\Theta$,

We also have the base case ${\mathcal{I}_{1}{(\theta)}} = 0$. Hence for $t1$, $\theta_{1},{\theta_{2}\Theta}$, and any unit-norm $v{\mathbb{R}}^{d^{2}}$,

Therefore by the variational form of the operator norm, we have for all $t1$ and $\theta_{1},{\theta_{2}\Theta}$:

Note that for any $\theta\Theta$, ${\mathbb{E}}_{p_{\theta}}{({Lip}_{t + 1}{(z_{1:t})}\rfloor}\frac{1}{\sigma^{2}}{(1 + \sigma^{3}d^{3 \Uparrow 2})}\max{\{ 1 \Uparrow \sigma^{2},\sigma d^{3 \Uparrow 2}\}}$, and consequently ${Lip}{\max{\{{1 \Uparrow \sigma^{2}},{\sigmad^{3 \Uparrow 2}}\}}}$. On the other hand, for a unit-norm $v{\mathbb{R}}^{d^{2}}$ and $\theta_{1},{\theta_{2}\Theta}$,

Hence, we have that $B_{\mathcal{I}}{\max{\{{1 \Uparrow \sigma^{2}},d\}}}$. By A.4 and (4.67) we have on $\mathcal{E}_{1}$ for any $\theta{conv}{\{{\hat{\theta}}_{m,T}^{\varepsilon},\theta\}}$,

Combining (4.62), (4.64), and (4.68), we have that on $\mathcal{E}_{1}$,

Hence by A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization"), we have that (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) holds on $\mathcal{E}_{1}$ as long as $m$ satisfies:

### Step 5: Final result

If $m$ satisfies conditions (4.63), (4.66), and (4.69), then on $\mathcal{E}_{1}$ we have from 3.9 and (4.60):

### Sequence Modeling with Linear Attention

Since their introduction, transformer models and architectures have found popularity in modern sequence modeling tasks, finding use in fields such as language modeling, computer vision, and reinforcement learning. Despite their widespread application however, full theoretical analysis of multi-layer transformer models is currently out of reach. As a result, stylized and simplified attention modules that isolate core mechanisms are commonly used in the literature as analytically tractable proxies for analyzing the full models. Single-layer linear self-attention models have been used to explore the dynamics of in-context learning and emergent inductive biases in transformers. Recent works show that attention can operate as a max-margin token selection mechanism, even establishing an equivalence with hard-margin SVM. Furthermore, established the global convergence of gradient descent for this framework, and a finite sample bounds were established by with parameter estimation upper bounds; we take particular inspiration from this line of work, especially, and analyze a simple linear transformer with a single-layer cross-attention and linear activation.

Let us consider a vocabulary of $K$ tokens denoting the states $z\mathsf{Z}$, each assigned a $d$-dimensional embedding by an embedding matrix $E = {{(e_{1}\quad e_{K}\rfloor}^{\mathsf{T}}{\mathbb{R}}^{Kd}}$, such that $\mathsf{Z} = {\{ e_{i}i{(K\rfloor}\}}$. We further emphasize that these embeddings ${\{ e_{k}\}}_{k = 1}^{K}$ are *not* the standard basis vectors, which we denote instead $\mathbf{1}{(k)}{\mathbb{R}}^{K}$ in this section. We assume that the first *two* tokens $z_{0},z_{1}$ are drawn from a given initial distribution $\rho_{1}$ over $\mathsf{Z}\mathsf{Z}$ to create an initial state for cross-attention. To sample a new token $z_{t + 1}\mathsf{Z}$ in a sequence $z_{0:t}$ where $z_{0:t}{\mathbb{R}}^{{({t + 1})}d}$, we sample *auto-regressively* by taking the last token $z_{t}$ to be the query token in a cross-attention layer given as:

where $\mathcal{K},Q,{V{\mathbb{R}}^{dd}}$ denote the key, query, and value matrices, $C{\mathbb{R}}^{{({K - 1})}d}$ denotes the classifier head, $\mathbb{A}$ denotes an activation function, $\mathbb{S}$ denotes the softmax function, and $\Phi:{{\mathbb{R}}^{K - 1}{\mathbb{R}}^{K}}$ denotes the function that embeds ${\Phi{(x)}}:={(x,0)}$.^1313^13The function $\Phi$ is introduced to allow for parameter recovery; otherwise parameterizing a distribution over $(K\rfloor$ using $K$ logits is not identifiable, as softmax is invariant under affine transforms (i.e., ${{\mathbb{S}}{({x + {c\mathbb{1}}})}} = {{\mathbb{S}}{(x)}}$ for any $c{\mathbb{R}}$). We shall denote $\theta:={{vec}{({\mathcal{K}Q^{\mathsf{T}}})}}$ to be the parametrization such that $\Theta = {\{{\theta{\mathbb{R}}^{d^{2}}\thetaR}\}}$, and we constrain $V = I_{d}$ and $C$ to be fixed matrices. Finally, we use a linear activation, where we normalize by $1 \Uparrow t$ for key trajectory length $t$.^1414^14This normalization ensures that the sum of key-query attention scores does not scale with trajectory length, which would increase the magnitude inside the outer softmax over time and cause exponential decay in the minimum probability of a token. This scaling is implicit in softmax activation settings, which would divide by the sum of the exponentiated weights. We note that this scaling is also used in practice . This all simplifies to the following:

where we recall that $mat$ is the matricization function such that ${mat}{(\theta)}{\mathbb{R}}^{dd}$.

### Theorem 4.18

Fix $\delta{}$, and suppose that the embedding matrix $E$ and classifier head $C$ are both full column rank, with normalized embeddings such that ${\max_{k{(K\rfloor}}{e_{k}}} = 1$ and classifier head such that ${}C{}_{op}1$. Let $\Theta = {\{{\theta{\mathbb{R}}^{d^{2}}\thetaR}\}}$ for $R1$ and $d > 1$, and let ${\hat{\theta}}_{m,T}^{\varepsilon}$ denote the max FI discretized MLE estimator at resolution $\varepsilon = \frac{\delta}{2\sqrt{2m}}$. If the number of trajectories $m$ and the trajectory length $T$ satisfies

where $\kappa{(C)}$ denotes the condition number of $C$, then with probability at least $1 - \delta$ for $\delta{}$ and for a universal positive constant $c_{0}$, we have

To the best of our knowledge, 4.18 is the first result for learning the parameters of an auto-regression linear transformer model in the multiple trajectory setting which achieves a nearly instance-optimal rate (cf. (4.72)), which also includes a rate of convergence that decreases with all the data $mT$ instead of just the number of trajectories $m$. The most related result to 4.18 comes from \[97, Corollary 4.3\], which we will compare with in detail in a moment. Before discussion this related result, we make a few remarks on 4.18. First, we know that the assumption that both $E$ and $C$ are full column rank implies the constraint $d + {1K}$, which states that the embedding size $d$ is *less* than the vocabulary size $K$ minus one. This is a realistic assumption in practice, as typical vocabulary sizes for modern LLMs are often in the $100$k range, whereas typical embedding sizes are typically no more than $10$k.^1515^15For example, Meta's Llama3 8B model has a vocabulary size of $128$k with an embedding dimension of $4096$. We next focus on the trajectory requirement on $m$ in (4.71). We first note that the constraint on trajectory length $TT_{0}$ in (4.71) can be elided at the expense of a more complex expression for the required number of trajectories, but the final rate would remain the same. Next, the requirement on $m$, ignoring the contributions of $C,E$, is $m\overset{\sim}{\Omega}{({d^{2}K^{8}{\exp{(R)}}})}$. While the dependence on $d$ is correct, we anticipate that the dependence on $K,R$ is not sharp, and can be improved with further analysis. Similarly, in our analysis we show a bound of the form $\lambda_{\min}{({\overline{\mathcal{I}}{(\theta)}})}K^{- 4}{\exp{({- R})}}$ (also ignoring contributions of $C,E$), which implies from (4.72) a parameter recovery bound of ${{\hat{\theta}}_{m,T}^{\varepsilon}} - {\theta{}^{2}\overset{\sim}{O}{({{d^{2}K^{4}{\exp{(R)}}} \Uparrow {({mT})}})}}$; as with the requirement on $m$, we anticipate this parameter recovery bound is also not optimal in its dependence on $K,R$ (but is optimal in $d,m,T$).

### Comparison with \[97, Corollary 4.3\]

As mentioned previously, the most comparable result to 4.18 is \[97, Corollary 4.3\]. Here, the authors also study a multi-trajectory data model, but one key difference is that , the trajectory $z_{0:T}$ is not auto-regressively generated. Instead, there is a distribution $\mathcal{D}_{X}$ over *prompts* $z_{0:{T - 1}}$, followed by a last token $z_{T}$ generated from a self-attention model conditioned on the prompt $z_{0:{T - 1}}$, resembling a standard supervised learning setup. Consequently, their final parameter recovery rate only decays with the number of trajectory $m$, in comparison to our rate (4.72) which decreases with the total data budget $mT$. Another difference between our two settings is a structural one. We choose to analyze a setting with linear activation instead of softmax activation $\mathbb{A}$, and we constrain the outputs of the classifier head $C$ to $\Delta^{K - 1}$ (the probability simplex in ${\mathbb{R}}^{K}$) by means of an outer softmax activation (i.e., we treat the outputs of the classifier head as logits, as is typically done in practice), as detailed in (4.70). On the other hand in they consider a softmax activation $\mathbb{A}$, but omit the softmax activation after the classifier head. Hence, they require additional assumptions on the classifier head and the embeddings matrix to ensure that the output of the classifier head is a valid probability distribution. This may seem like a minor difference, but their setup requires that vocabulary embeddings $E$ are linearly independent \[97, Assumption 2.3\], which requires that $dK$ (i.e., the embedding dimension exceeds the vocabulary size). As we discussed previously, in practice we typically have the opposite trend (i.e., embedding dimension is much smaller than vocabulary size), which our model allows .

With these remarks in place, we can now directly compare our bounds to, keeping in mind the differences in problem setup and assumptions described previously. To keep the comparison simple, we will suppress dependency on $C,R,E$, and only focus on $m,T,K$ in the bounds. The main parameter recovery result in states that with high probability:

where $\alpha > 0$ is the strong convexity constant of the population loss over a ball around $\theta$. This quantity $\alpha$ is left unspecified in their argument; they only argue that $\alpha > 0$, but do not provide an explicit lower bound for it. Since for negative log likelihood, both Fisher information and Hessian of the population loss coincide, in the notation of our work, $\alpha = \inf_{\thetaB{(\theta,r_{0})}}\lambda_{\min}{({\mathbb{E}}_{z_{0:{T - 1}}\mathcal{D}_{X}}{(\mathcal{I}_{T}{(\theta z_{0:{T - 1}})}\rfloor})}$ (note that the conditional Fisher Information notation is defined in (A.1)) where $r_{0}$ is a localization parameter which we consider as a constant. With this in mind, 4.18 implies that with high probability:

where $\overline{\alpha}:={\lambda_{\min}{({\overline{\mathcal{I}}{(\theta)}})}}$. As mentioned previously, we show a lower bound on $\overline{\alpha}K^{- 4}$, which again is most likely not optimal. Comparing (4.73) with (4.74), we see that the dependence on the parameter dimension ($K$ for the former as they consider a subspace of $dd$ matrices with dimension $K^{2}$, $d$ for our case) is equivalent up to log factors. On the other hand, our bound yields an improvement on the dependence of the $\overline{\alpha}$ (vs. $\alpha$) parameter in the final rate. Finally and most importantly, as our setting studies auto-regressive generation, our rate is able to capture the dependence on all the data points $mT$, rather than just the number of trajectories $m$.

### Proof of 4.18

### Step 1: Covering number bound

As earlier, we first estimate the covering number of $\mathcal{P}$ in the FI norm through the $\ell_{2}$ covering number. Let $J:={\left( \begin{matrix}
\end{matrix} \right\rfloor{\mathbb{R}}^{K{({K - 1})}}}$. If we denote $M_{0:t}:={\frac{1}{t}z_{t}^{\mathsf{T}}{({JCz_{0:{t - 1}}^{\mathsf{T}}z_{0:{t - 1}}})}{\mathbb{R}}^{Kd^{2}}}$ and ${\overline{M}}_{0:t}:={\frac{1}{t}z_{t}^{\mathsf{T}}{({Cz_{0:{t - 1}}^{\mathsf{T}}z_{0:{t - 1}}})}{\mathbb{R}}^{{({K - 1})}d}}$, we can see that the following holds by vectorization:

As such we can say ${p_{\theta}{({z_{t + 1}z_{0:t}})}} = {{\mathbb{S}}{({M_{0:t}\theta})}_{k}}$ for $z_{t + 1} = e_{k}$. Next, since we have

this motivates finding an expression for the Fisher information matrix and its maximum eigenvalue. If we let ${(z_{t})}{(K\rfloor}$ denote the index of the token associated with entry $z_{t}$ and ${(M_{0:t}\rfloor}_{i}$ denote the $i$-th row of $M_{0:t}$, we calculate the Hessian of the log likelihood:

If we denote the conditional expectation ${\mathbb{E}}_{t}^{\theta}{(\rfloor}{\mathbb{E}}_{p_{\theta}}{(z_{0:t}\rfloor}$,

Hence, the FI matrix can be represented as:

We may see that for all $t{(T - 1\rfloor}$, ${M_{0:t}{}_{op}{\sup_{k{(K\rfloor}}{e_{k}{}^{3}C{}_{op}}}} = {C{}_{op}}$. Expanding out the multiplication and upper bounding gives our result.

This gives that for all $\theta\Theta$, $\lambda_{\max}{({\mathcal{I}{(\theta)}})}T{}C{}_{op}^{2}$: notably, this expression is agnostic of the exact parametrization. This allows us to set $\mathcal{I}_{\max} = {TC{}_{op}^{2}I_{d^{2}}}$, from which we have ${\lambda_{\max}{(\mathcal{I}_{\max})}} = {TC{}_{op}^{2}}$. If we fix some $\theta\Theta$ and let $\hat{\theta}$ denote its closest element in an $\varepsilon$-covering of $\Theta$ in $\ell_{2}$, substituting $\mathcal{I}_{\max}$ into the previous bound on $d_{\mathcal{I}_{\max}}{(p_{\theta},p_{\hat{\theta}})}$ gives $d_{\mathcal{I}_{\max}}{(p_{\theta},p_{\hat{\theta}})}\sqrt{T}{}C{}_{op}\varepsilon$. This implies the relation for $\varepsilon{}$:

Applying 3.6 with $\varepsilon = \frac{\delta}{2\sqrt{2m}}$ and $\eta = \frac{1}{2RC{}_{op}\sqrt{mT}}$, and upper bounding ${{RC{}_{op}\sqrt{mT}} \Uparrow \delta}{({{RC{}_{op}\sqrt{mT}} \Uparrow \delta})}^{d^{2}}$ in the logarithm, for some universal constant $c_{0} > 0$ we obtain with probability at least $1 - \delta$,

For satisfactory $c_{0}$, the final $\frac{1 + \delta^{2}}{m}$ term can additionally be collapsed into the first term given that $d > 1$. Let us denote $\mathbf{1}{(z)}{\{ 0,1\}}^{K}$ to be the one-hot standard basis vector such that for $i{(K\rfloor}$, ${(\mathbf{1}{(z)}\rfloor}_{i} = 1$ if $z = e_{i}$ and ${(\mathbf{1}{(z)}\rfloor}_{i} = 0$ otherwise. When invoking 3.6, we can use the log-concave conclusion (3.16. ‣ Theorem 3.6. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), since ${\log p_{\theta}}{(z_{0:T})}$ is given :

which is the sum of affine terms in $\theta$ minus the sum of terms which are given by taking the log-sum-exp (LSE) of a linear function of $\theta$, which is convex \cf. [100, Section 3.1.5\]. Hence, ${\log p_{\theta}}{(z_{0:T})}$ is a concave function by basic composition rules.

### Step 2: Estimating $B_{1}$ and $B_{2}$

Crucial in bounding $B_{1}$ and $B_{2}$ is bounding the smallest eigenvalue of $\mathcal{I}{(\theta)}$, so let us note the expansion of the Fisher information from eq. 4.76:

We note that if one simply looks at ${\operatorname{\mathsf{d}\mathsf{i}\mathsf{a}\mathsf{g}}{({{\mathbb{S}}{({M_{0:t}\theta})}})}} - {{\mathbb{S}}{({M_{0:t}\theta})}{\mathbb{S}}{({M_{0:t}\theta})}^{\mathsf{T}}}$, the minimum eigenvalue would be zero since there is a constrained direction due to ${\mathbb{S}}{({M_{0:t}\theta})}$ lying on the $K - 1$ dimensional simplex. Hence, we look at the reduced matrix by ignoring the last redundant coordinate, which restores a non-zero minimum eigenvalue. As such, we begin by examining the inner expression $J^{\mathsf{T}}{({{\operatorname{\mathsf{d}\mathsf{i}\mathsf{a}\mathsf{g}}{({{\mathbb{S}}{({M_{0:t}\theta})}})}} - {{\mathbb{S}}{({M_{0:t}\theta})}{\mathbb{S}}{({M_{0:t}\theta})}^{\mathsf{T}}}})}J$. E.1 states that if we can show there exists $\mu > 0$ such that $k{(K\rfloor}$, ${\mathbb{S}}{({M_{0:t}\theta})}_{k}\mu$, then $\lambda_{\min}\left( {J^{\mathsf{T}}{({{\operatorname{\mathsf{d}\mathsf{i}\mathsf{a}\mathsf{g}}{({{\mathbb{S}}{({M_{0:t}\theta})}})}} - {{\mathbb{S}}{({M_{0:t}\theta})}{\mathbb{S}}{({M_{0:t}\theta})}^{\mathsf{T}}}})}J} \right)\frac{\mu}{4{({K - 1})}}$. Let us now find such a $\mu$ by lower bounding ${\log p_{\theta}}{({e_{k}z_{0:t}})}$ and exponentiating it to find a bound for $p_{\theta}{({e_{k}z_{0:t}})}$ for arbitrary $k{(K\rfloor}$:

We now exponentiate to recover a bound for the conditional likelihood:

Through Cauchy-Schwartz we may bound the quantity inside the exponent, giving our final bound.

Therefore we can set $\mu = {\frac{1}{K}{\exp\left( {- {2RC{}_{op}}} \right)}}$ in order to satisfy the condition. This gives that $\lambda_{\min}\left( {J^{\mathsf{T}}{({{\operatorname{\mathsf{d}\mathsf{i}\mathsf{a}\mathsf{g}}{({{\mathbb{S}}{({M_{0:t}\theta})}})}} - {{\mathbb{S}}{({M_{0:t}\theta})}{\mathbb{S}}{({M_{0:t}\theta})}^{\mathsf{T}}}})}J} \right)\frac{\exp\left( {- {2C{}_{op}R}} \right)}{4K{({K - 1})}}$. Once we have this, we can extract the inner matrix from $\mathcal{I}{(\theta)}$ by lower bounding the Rayleigh quotient, giving:

The smallest eigenvalue of this quantity can be lower bounded by the minimum eigenvalue of both sides of the Kronecker product. The first quantity can be handled by lower bounding the probability of seeing a particular token,

For the second quantity, we note that the minimum eigenvalue function is concave so we may lower bound the expression by moving it into the expectation:

Finally, we may put this all together for an expression for the minimum eigenvalues of the conditional and unconditional Fisher information matrices:

We can now begin working on finding bounds for the constants $B_{1}$ and $B_{2}$. Let us take a test vector $v{\mathbb{R}}^{d}$ with magnitude ${v} = {\mathcal{I}{(\theta)}^{1 \Uparrow 2}{}_{op}}$ and analyze $\psi_{t + 1}$ defined as follows:

We can immediately see that ${\mathbb{E}}_{p_{\theta}}{(\psi_{t + 1}z_{0:t}\rfloor} = 0$. We may observe that ${\mathbf{1}{(z_{t + 1})}} - {{\mathbb{S}}{({M_{0:t}\theta})}}$ is a bounded random variable vector:

From this we can observe the following:

This all gives that $\psi_{t + 1}$ is a zero-mean bounded random variable given by $\sigma^{2} = {2v{}^{2}C{}_{op}^{2}}$, and we can see that ${{v},{{{}_{}^{}p_{\theta}}{(z_{0:T})}}} = {{}_{t = 2}^{T}\psi_{t}}$ is a martingale sum. This allows us to apply Azuma-Hoeffding (A.7. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), giving us that

and as such ${\mathbb{E}}{({v},{{{}_{}^{}p_{\theta}}{(z_{0:t})}{}^{4}}\rfloor}^{1 \Uparrow 4}4\sqrt{2T}{}v{}{}C{}_{op}$. We note that applying Rosenthal's inequality for MDS (cf. A.6. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) retrieves a similar result, but requires a longer proof in order to express a bound for both terms. Taking $v = {\mathcal{I}{(\theta)}^{1 \Uparrow 2}\overline{v}}$ for unit vector $\overline{v}$ results in $B_{1}4\sqrt{\frac{2T}{\lambda_{\min}{({\mathcal{I}{(\theta)}})}}}{}C{}_{op}$.

Since the Hessian of the conditional log-likelihood has no dependence on the new token, bounding $B_{2}$ reduces to $\sup_{\theta\Theta}{\mathcal{I}{(\theta)}^{- {1 \Uparrow 2}}M_{0:t}^{\mathsf{T}}{({{\operatorname{\mathsf{d}\mathsf{i}\mathsf{a}\mathsf{g}}{({{\mathbb{S}}{({M_{0:t}\theta})}})}} - {{\mathbb{S}}{({M_{0:t}\theta})}{\mathbb{S}}{({M_{0:t}\theta})}^{\mathsf{T}}}})}M_{0:t}\mathcal{I}{(\theta)}^{- {1 \Uparrow 2}}{}_{op}}$ which may be bounded by $\frac{2}{\lambda_{\min}{({\mathcal{I}{(\theta)}})}}{}C{}_{op}^{2}$.

### Step 3: Parameter error bound

From here, we can unlock the first set of bounds by verifying (3.22. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")):

In order to satisfy this condition, we can take $m\left( {{d^{2}{\log\left( \frac{TR^{2}C{}_{op}^{2}m}{\delta^{2}} \right)}} + 1 + \delta^{2}} \right)\frac{T^{2}C{}_{op}^{4}}{\lambda_{\min}{({\mathcal{I}{(\theta)}})}^{2}}$. If we apply A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") and expand out the minimum eigenvalue, for $T > 1$ this gives us:

### Step 4: Verify FI radius

We now need to show (3.24. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")) in order to unlock the second bound. To this end, we show a Lipschitz condition on the conditional Fisher information from eq. 4.75:

This gives us that ${Lip3}{}C{}_{op}^{3}$. Let us now find an expression for the second moment bound:

With both a globally bounded Lipschitz constant and a finite $B_{\mathcal{I}}$, we can apply A.4 to bound the difference in Fisher informations:

Note that the lower bound on $\lambda_{\min}{({\mathcal{I}{(\theta)}})}$ in (4.78) is agnostic to the value of $\theta\Theta$. Therefore,

If we apply this to (3.23. ‣ Proposition 3.9. ‣ 3.2.2 Equivalence of Hellinger Distance and Fisher-weighted Metric ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), we can upper bound the parameter distance:

If we put these together, we have the following:

If we take $T\frac{K^{4}C{}_{op}^{2}}{\sigma_{\min}{(C)}^{2}\sigma_{\min}{(E)}^{4}}{\exp{({6RC{}_{op}})}}$ such that ${}C{}_{op}\lambda_{\min}{({\mathcal{I}{(\theta)}})}^{- {1 \Uparrow 2}}1$, this is bounded above by $1 \Uparrow 2$ :

### Step 5: Final result

Finally, we can plug in our expression for the minimum eigenvalue in eq. 4.78 to take the following bound

and applying A.1. ‣ Appendix A Additional Results for Hellinger Localization ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization") extracts $m$ to satisfy the Fisher radius:

Notably, this additionally satisfies (4.79). In this case, we unlock the following bound for $\delta{}$:

## Conclusion

We introduced the Hellinger localization framework for deriving nearly instance-optimal parameter recovery rates for multi-trajectory learning setups. We applied our framework to a diverse set of case studies, including a mixture of Markov chains example, a dependent linear regression problem with general noise distributions, a non-monotonic sinusoidal GLM example, and a linear attention sequence modeling setup. In each case, we showed that our Hellinger localization framework was able to provide nearly instance-optimal rates that significantly improve upon the prior art.

Our work further opens up several avenues for future investigation. We list out a few ideas, starting with technical improvements, and ending with more broader, high-level directions.

Extensions of self-normalization: As discussed in Section 4.2.1, one particular drawback of our current framework is that it places un-necessary requirements on the regularity of the trajectory process $z_{1:T}$. Concretely, in the context of dependent linear regression, the process $z_{1:T}$ can not grow more than ${poly}{(T)}$, which rules out e.g., recovering linear dynamical systems with spectral radius $> 1$. We believe this restriction is purely a technical limitation of our argument, which currently does not have a method to self-normalize as is done in analysis specialized for least-squares linear regression. The work of which generalizes offset complexity to exp-concave losses is a natural starting point for such an inquiry.

Improved minimum trajectory requirements for non-log-concave families: As we discussed in Section 3.4, another limitation of our current analysis is that whenever the family of distribution $\mathcal{P}$ is not log-concave, our requirements on the number of trajectory $m$ grows from $m{polylog}{(T)}$ in the log-concave setting, to $mT{polylog}{(T)}$. We believe this scaling should generally be improvable. One possible pathway is to utilize the local geodesic convexity of the squared Hellinger distance in the Fisher-Rao metric, and conduct our second-order Taylor analysis (cf. 3.9) over geodesics.

Non-realizable settings: Our work is carried out in the realizable setting, i.e., where the data generating distribution $p\mathcal{P}$. A natural and useful extension would be to allow for $p\begin{array}{l}

\end{array}\mathcal{P}$, and study convergence to the best distribution in $\mathcal{P}$, i.e., $\theta^{\mathcal{P}}:={{{\arg\min}_{p\mathcal{P}}{KL}}{({pp})}}$. One key technical challenge for the non-realizable setting is extending 3.6 to measure squared Hellinger distance $d_{H}^{2}{({\hat{p}}_{m,T}^{\varepsilon},p^{\mathcal{P}})}$ without relying on e.g., max divergence coverings (cf. 3.1. ‣ 3.2.1 Control of Trajectory Measures in Hellinger Distance ‣ 3.2 Analyzing MLE via Localization in Hellinger Distance ‣ 3 Problem Setup and General Framework ‣ Nearly Instance-Optimal Parameter Recovery from Many Trajectories via Hellinger Localization")), but instead allowing for some less stringent tail behavior for the log-likelihoods which is still practical to verify. This could also be useful in allowing 3.6 to apply directly to the MLE estimator and not its discretized counterpart (cf. 3.7).

Applications to non-sequentially dependent data: While our work focuses on sequentially-ordered stochastic processes, our main tools in Section 3 (i.e., 3.6 and 3.9) are actually agnostic to this sequential structure. It is only when we analyze the score function and observed information matrix moments (i.e., (3.20) and (3.21) from 3.9) that we impose a temporal dependence in the data. Hence, an interesting future direction is to apply our main tools to other problem settings with different correlation structures, such as for Ising models (cf. related work from Section 2) and other graph/network structures.

Applications for filtering and control problems: Finally, through the case studies in Section 4, we have looked at parameter recovery in various types of dynamical systems. A natural next step is to consider the downstream control task where the recovered model parameters would be applied, by extending our results to enable task-specific optimal exploration for a broader family of parametric models and loss functions (cf. discussion in Section 4.2.1). Another direction is to apply our framework for filtering problems in state estimation, which can be cast as a latent maximum likelihood estimation problems. Here, an important sub-direction would be to study the application of our techniques to analyzing not just the exact MLE estimate, but also practical algorithms such as expectation-maximization and variational inference, which are necessary in situations where directly computing the MLE is computationally intractable.
