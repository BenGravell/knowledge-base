## Introduction

In artificial intelligence, learning to make decisions online plays a critical role in many fields, such as personalized news recommendation, robotics and the game of Go. To learn to make optimal decisions as soon as possible, the decision-makers must carefully design an algorithm to balance the trade-off between the exploration and exploitation. Over-exploration could be expensive and unethical in practice, e.g., medical decision making. On the other hand, insufficient exploration tends to make an algorithm stuck at a sub-optimal solution. The delicate design of exploration methods stands in the heart of online learning and decision making.

Upper Confidence Bound (UCB) is a class of highly effective algorithms in dealing with the exploration-exploitation trade-off in bandits and reinforcement learning. The tightness of confidence bound, as is known, is the key ingredient to achieve the optimal degree of explorations. To the best of our knowledge, nearly all the existing works construct confidence bounds based on various concentration inequalities, e.g. Hoeffding-type, empirical Bernstein type or self-normalized type. Those concentration-based confidence bounds, however, are typically conservative since they are *data-independent.* Concentration inequalities only exploit tail information, e.g., bounded or sub-Gaussian, rather than the whole distribution knowledge. In general, the loose constant factor may result in confidence bounds that are too wide to be informative.

In this paper, we propose a non-parametric and data-dependent UCB algorithm based on the multiplier bootstrap, called bootstrapped UCB. The principle is to use the multiplier bootstrapped quantile as the confidence bound to enforce the exploration. Inspired by recent advances on non-asymptotic guarantee and non-asymptotic inference such as, we develop an explicit second-order correction for the multiplier bootstrapped quantile that ensures the non-asymptotic validity. Our algorithm is easy to implement and has the potential to be generalized to more complicated models such as structured contextual bandits.

In theory, we develop both problem-dependent and problem-independent regret bounds for multi-armed bandits with symmetric rewards under a much weaker tail assumption, i.e., sub-Weibull distribution, than the classical sub-Gaussianity. In this case, it is proven that the mean estimator can still achieve the same problem-independent regret bound as the one under the sub-Gaussian assumption. Note that our result does not rely on other sophisticated approaches such as median-of-means or Catoni's M-estimator . A key technical tool we propose is a new concentration inequality for the sum of sub-Weibull random variables. Empirically, we evaluate our method in several multi-armed and linear bandit models. When the exact posterior is unavailable or the noise variance is mis-specified, the bootstrapped UCB demonstrates superior performance over variants of Thompson sampling and concentration-based UCB due to its non-parametric and data-dependent nature.

Recently, an increasing number of works study bootstrap methods for multi-armed and contextual bandits as an alternative to Thompson sampling. Most treat the bootstrap just as a way to randomize historical data (without any theoretical guarantee). One exception is who derive a regret bound for Bernoulli bandit by adding pseudo observations. However, their method cannot be easily extended to unbounded cases, and their analyses heavily limit to the Bernoulli assumption. In contrast, our method applies to a broader class of bandit models with rigorous regret analysis.

The rest of the paper is organized as follows. Section 2 introduces the basic setup and our bootstrapped UCB algorithm. Section 3 provides the regret analysis and Section 4 conducts several experiments.

### Notations

Throughout the paper, we denote ${{\mathbb{P}}_{\mathbf{w}}{( \cdot )}},{{\mathbb{E}}_{\mathbf{w}}{( \cdot )}}$ as the probability and expectation operator with respect to the distribution of the vector $\mathbf{w}$ only, conditioning on other random variables. We use similar notations for ${\mathbb{P}}_{\mathbf{y}}{( \cdot )}$, ${\mathbb{E}}_{\mathbf{y}}{( \cdot )}$ with respect to $\mathbf{y}$ only. $\lbrack n\rbrack$ means the set $\{ 1,2,\ldots,n\}$. We denote boldface lower letters (e.g. $\mathbf{x}$, $\mathbf{y}$) as a vector. For a set $\mathcal{E}$, we define its complement as $\mathcal{E}^{c}$.

## Bootstrapped UCB

### Problem setup

As a fruit fly, we illustrate our idea on the stochastic multi-armed bandit problem. In detail, the decision-makers interact with an environment for $T$ rounds. In round $t \in {\lbrack T\rbrack}$, the decision-makers pull an arm $I_{t} \in {\lbrack K\rbrack}$ and observes its reward $y_{I_{t}}$ which is drawn from a distribution associated with the arm $I_{t}$, denoted by $P_{I_{t}}$ with an unknown mean $\mu_{I_{t}}$. Without loss of generality, we assume arm $1$ is the optimal arm, that is, $\mu_{1} = {\max_{k \in {\lbrack K\rbrack}}\mu_{k}}$. In multi-armed bandit problems, the objective is to minimize the expected cumulative regret, defined as, where $\Delta_{k} = {\mu_{1} - \mu_{k}}$ is the sub-optimality gap for arm $k$, and $\mathbf{I}{\{ \cdot \}}$ is an indicator function. Here, the second equality is from the regret decomposition Lemma (Lemma 4.5 in). We call an upper bound of $R{(T)}$ problem-independent if the bound only depends on the distributional assumption and not on the specific bandit problem, say the gap $\Delta_{k}$.

### Upper Confidence Bound

The upper confidence bound (UCB) algorithm is based on the principle of optimism in the face of uncertainty. The key idea is to act as if the environment (parameterized by $\mu_{k}$ in multi-armed bandits) is as nice as plausibly possible. Concretely, a plausible environment refers to an upper confidence bound $\mathcal{G}{({\mathbf{y}}_{n},{1 - \alpha})}$ for the true mean $\mu$, of the form where ${\mathbf{y}}_{n} = {(y_{1},\ldots,y_{n})}^{\top}$ is the sample vector, ${\overline{y}}_{n}$ is the empirical mean, $\alpha \in {}$ is the confidence level, and $h_{\alpha}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{+}}$ is a threshold that could be either data-dependent or data-independent.

### Definition 2.1

We define $\mathcal{G}{({\mathbf{y}}_{n},{1 - \alpha})}$ as a non-asymptotic upper confidence bound if for *any sample size $n \geq 1$*, the following inequality holds In bandit problems, a non-asymptotic control on the confidence level is more commonly used. This is rather different from the asymptotic validity of confidence bound in statistics literature.

A generic UCB algorithm will select the action based on its UCB index ${\overline{y}}_{n} + {h_{\alpha}{({\mathbf{y}}_{n})}}$ for different arms. As is well known, the sharper the threshold is, the better exploration and exploitation trade-off one can achieve. By the definition of quantile, the sharpest threshold in (2.2) is the $({1 - \alpha})$-quantile of the distribution of ${\overline{y}}_{n} - \mu$. However, this quantile relies on the knowledge of the exact reward distribution and is therefore itself unknown. To evaluate this value, we construct a data-dependent confidence bound based on the multiplier bootstrap.

### Confidence Bound Based on Multiplier Bootstrap

### Multiplier Bootstrap

Multiplier bootstrap is a fast and easy-to-implement alternative to the standard bootstrap, and has been successfully applied in various statistical contexts. Its goal is to approximate the distribution of the target statistic by reweighing its summands with random multipliers independent of the data. For instance, in a mean estimation problem, we define a multiplier bootstrapped estimator as ${{n^{- 1}{\sum_{i = 1}^{n}{w_{i}{({y_{i} - {\overline{y}}_{n}})}}}} = {n^{- 1}{\sum_{i = 1}^{n}{{({w_{i} - {\overline{w}}_{n}})}y_{i}}}}},$ where ${\{ w_{i}\}}_{i = 1}^{n}$ are some random variables independent of ${\mathbf{y}}_{n}$, called bootstrap weights. Some classical weights are as follows: *Efron's bootstrap weights.* $(w_{1},\ldots,w_{n})$ is a multinomial random vector with parameters $(n;n^{- 1},\ldots,n^{- 1})$. This is the standard nonparameteric bootstrap.

*Gaussian weights.* $w_{i}$'s are i.i.d standard Gaussian random variables. This is closely related to Gaussian approximation in statistics.

*Rademacher weights.* $w_{i}$'s are i.i.d Rademacher variables. This is closely related to symmetrization in learning theory.

The bootstrap principle suggests that the $({1 - \alpha})$-quantile of the distribution of $n^{- 1}{\sum_{i = 1}^{n}{w_{i}{({y_{i} - {\overline{y}}_{n}})}}}$ conditionally on ${\mathbf{y}}_{n}$ could be used to approximate the $({1 - \alpha})$-quantile of the distribution of ${\overline{y}}_{n} - \mu$. As the first building block, the multiplier bootstrapped quantile is defined as, The question is whether $q_{\alpha}{({{\mathbf{y}}_{n} - {\overline{y}}_{n}})}$ is a valid threshold for any sample size $n \geq 1$.

### Second-order Correction

Most statistical theories guarantee the asymptotic validity of $q_{\alpha}{({{\mathbf{y}}_{n} - {\overline{y}}_{n}})}$ by the multiplier central limit theorem. However, we show that such a claim is valid *non-asymptotically* at the cost of adding a second-order correction. Next theorem rigorously characterizes this phenomenon under a symmetric assumption on the reward. Moreover, in Section A in the supplement, we show that without the second-order correction, a naive bootstrapped UCB will result in linear regret.

### Theorem 2.2 (Non-asymptotic Second-order Correction)

Suppose ${\{ y_{i}\}}_{i = 1}^{n}$ are i.i.d symmetric random variables with respect to its mean $\mu$, and the bootstrap weights ${\{ w_{i}\}}_{i = 1}^{n}$ are i.i.d Rademacher random variables. For two arbitrary parameters ${\alpha,\delta} \in {}$, the following inequality holds for any sample size $n \geq 1$, where $\varphi{({\mathbf{y}}_{n})}$ is a non-negative function satisfying ${{{\mathbb{P}}_{\mathbf{y}}{({{|{{\overline{y}}_{n} - \mu}|} \geq {\varphi{({\mathbf{y}}_{n})}}})}} \leq \alpha}.$ The detailed proof is deferred to Section B.1 in the supplement. In (2.5. ‣ 2.2 Second-order Correction ‣ 2 Bootstrapped UCB ‣ Bootstrapping Upper Confidence Bound")), the bootstrapped threshold may be interpreted as a main term, i.e., $q_{\alpha{({1 - \delta})}}{({{\mathbf{y}}_{n} - {\overline{y}}_{n}})}$ (at a shrunk confidence level), plus a second-order correction term, i.e., ${({{\log{({{2/\alpha}\delta})}}/n})}^{1/2}\varphi{({\mathbf{y}}_{n})}$. The latter is added to guarantee the non-asymptotic validity of the bootstrapped threshold. In the above, $\varphi{({\mathbf{y}}_{n})}$ could be any preliminary upper bound on ${\overline{y}}_{n} - \mu$. Hence, Theorem 2.2. ‣ 2.2 Second-order Correction ‣ 2 Bootstrapped UCB ‣ Bootstrapping Upper Confidence Bound") transforms a possibly coarse prior bound $\varphi{({\mathbf{y}}_{n})}$ on quantiles into a more accurate version that is based on a main term estimated by multiplier bootstrap plus a second-order correction term based on $\varphi{({\mathbf{y}}_{n})}$ multiplied by a $\mathcal{O}{(n^{- {1/2}})}$ factor.

### Remark 2.3 (Choice of $\varphi{({\mathbf{y}}_{n})}$)

If ${\{ y_{i}\}}_{i = 1}^{n}$ are independent 1-sub-Gaussian random variables, a natural choice of $\varphi{({\mathbf{y}}_{n})}$ is ${({{2{\log{({1/\alpha})}}}/n})}^{1/2}$ by Hoeffding's inequality (Lemma 2. ‣ Appendix F Supporting Lemmas ‣ Bootstrapping Upper Confidence Bound")). Plugging it into (2.5. ‣ 2.2 Second-order Correction ‣ 2 Bootstrapped UCB ‣ Bootstrapping Upper Confidence Bound")) and letting $\delta = {1/2}$, the bootstrapped threshold in (2.5. ‣ 2.2 Second-order Correction ‣ 2 Bootstrapped UCB ‣ Bootstrapping Upper Confidence Bound")) becomes Lemma B.3 in the supplement shows that the main term is of order at least $\mathcal{O}{(n^{- {1/2}})}$ as $n$ grows, which implies the second order correction is just a remainder term. We emphasize that the reminder term is obviously not sharp and will be sharpened as a future work.

### Remark 2.4

Existing works on UCB-type algorithms typically utilized various concentration inequalities, e.g. Hoeffding's inequality or empirical Bernstein's inequality, to find a valid threshold $h_{\alpha}{({\mathbf{y}}_{n})}$. However, they are not data-dependent and only use the tail information, rather than fully exploit the whole distribution knowledge. This is typically conservative, and leads to over-exploration.

### Remark 2.5

Empirical KL-UCB used empirical likelihood to build confidence intervals for general distributions that have support in $\lbrack 0,1\rbrack$. Although empirical KL-UCB is also data-dependent, our proposed method is from a very different non-parametric perspective and uses different tools by bootstrap. In practice, resampling tends to be more efficient computationally, without solving a convex optimization each round like empirical KL-UCB. Moreover, our method can work with unbounded rewards and we believe it is easier to generalize to structured bandits, e.g. linear bandit.

In Figure 1, we compare different approaches to calculate 95% confidence bound for the population mean based on samples from a truncated-normal distribution. When the sample size is extremely small $({\leq 10})$, the naive bootstrap (without any correction) cannot output a valid threshold since the bootstrapped quantile is smaller than the true 95% quantile. This confirms the necessity of the second-order correction. When the sample size increases, our bootstrapped threshold converges to the truth rapidly. This confirms the correction term is just a small remainder term. Additionally, the bootstrapped threshold is shown to be sharper than Hoeffding's bound and empirical Bernstein bound when sample size is large (see the right panel of Figure 1).

Figure 1: 95% confidence bound of the sample mean.

### Main Algorithm: Bootstrapped UCB

Based on the above theoretical findings, we conclude that bootstrapped UCB will select the arm according to its UCB index defined as below: where $n_{k,t}$ is the number of pulls for arm $k$ until time $t$. Practically, we may use Monte Carlo quantile approximation to get an approximated bootstrapped quantile ${\overset{\sim}{q}}_{\alpha{({1 - \delta})}}{({{\mathbf{y}}_{n_{k,t}} - {\overline{y}}_{n_{k,t}}},{\mathbf{w}}^{B})}$ and corresponding theorem for the control of the approximation of the bootstrapped quantile is also derived (see Section D in the supplement for details). The algorithm is summarized in Algorithm 1. The computational complexity at step $t$ is ${\overset{\sim}{\mathcal{O}}{({Bt})}} \leq {\overset{\sim}{\mathcal{O}}{({BT})}}$. Comparing with vanilla UCB, the extra $Bt$ is due to resampling. In practice, the choice of $B$ is seldom treated as a tuning parameter, but usually determined by the available computational resource.

Input: the number of bootstrap repetitions B, hyper-parameter δ. Pull each arm once to initialize the algorithm. Set confidence level α = 1/(t + 1). Calculate the boostrapped quantile ${\overset{\sim}{q}}_{\alpha{({1 - \delta})}}{({{\mathbf{y}}_{n_{k,t}} - {\overline{y}}_{n_{k,t}}},{\mathbf{w}}^{B})}$. Pull the arm $${I_{t} = {\operatorname{argmax}\limits_{k \in {\lbrack K\rbrack}}{({{\overline{y}}_{n_{k,t}} + {{\overset{\sim}{q}}_{\alpha{({1 - \delta})}}{({{\mathbf{y}}_{n_{k,t}} - {\overline{y}}_{n_{k,t}}},{\mathbf{w}}^{B})}} + {{({{\log{({{2/\alpha}\delta})}}/n_{k,t}})}^{1/2}\varphi{({\mathbf{y}}_{n_{k,t}})}}})}}}.$$ Receive reward yIt. Algorithm 1 Bootstrapped UCB

## Regret Analysis

In Section 3.1, we derive regret bounds for bootstrapped UCB. Moreover, we show that naive bootstrapped UCB will result in linear regret in some cases in Section A in the supplement.

### Regret Bound for Bootstrapped UCB

For multi-armed bandit problems, most literature consider sub-Gaussian rewards. In this work, we move beyond sub-Gaussianity and consider the reward under a much weaker tail assumption, so-called sub-Weibull distribution. As shown , it is characterized by the right tail of the Weibull distribution and generalizes sub-Gaussian and sub-exponential distributions.

### Definition 1 (Sub-Weibull Distribution)

We define $y$ as a sub-Weibull random variable if it has a bounded $\psi_{\beta}$-norm. The $\psi_{\beta}$-norm of $y$ for any $\beta > 0$ is defined as Particularly, when $\beta$ = 1 or 2, sub-Weibull random variables reduce to sub-exponential or sub-Gaussian random variables, respectively. It is obvious that the smaller $\beta$ is, the heavier tail the random variable has. Next theorem provides a corresponding concentration inequality for the sum of independent sub-Weibull random variables.

### Theorem 3.1 (Concentration Inequality for Sub-Weibull Distribution)

Suppose ${\{ y_{i}\}}_{i = 1}^{n}$ are independent sub-Weibull random variables with ${\| y_{i}\|}_{\psi_{\beta}} \leq \sigma$. Then there exists an absolute constant $C_{\beta}$ only depending on $\beta$ such that for any ${\mathbf{a}} = {(a_{1},\ldots,a_{n})} \in {\mathbb{R}}^{n}$ and $0 < \alpha < {1/e^{2}}$, with probability at least $1 - \alpha$.

The proof relies on a precise characterization of $p$-th moment of a Weibull random variable and standard symmetrization arguments. Details are deferred to Section B.2 in the supplement. This theorem generalizes the Hoeffding-type concentration inequalities for sub-Gaussian random variables (see, e.g. Proposition 5.10 in Vershynin ), and Bernstein-type concentration inequalities for sub-exponential random variables (see, e.g. Proposition 5.16 in Vershynin ) up to some constants.

In Theorem 3.2, we provide both problem-dependent and problem-independent regret bounds.

### Theorem 3.2

Consider a stochastic $K$-armed sub-Weibull bandit, where the noise follows a symmetric sub-Weibull distribution with its $\psi_{\beta}$-norm upper bounded by $\sigma$. Denote $n_{k,t}$ as the number of pulls for arm $k$ until time $t$. We choose $\varphi$ according to Theorem 3.1. ‣ 3.1 Regret Bound for Bootstrapped UCB ‣ 3 Regret Analysis ‣ Bootstrapping Upper Confidence Bound") as follows and let the confidence level $\alpha = {1/T^{2}}$. For any round $T$, the problem-dependent regret of bootstrapped UCB is upper bounded by where $C_{\beta}$ is some absolute constant from Theorem 3.1. ‣ 3.1 Regret Bound for Bootstrapped UCB ‣ 3 Regret Analysis ‣ Bootstrapping Upper Confidence Bound"), and $\Delta_{k}$ is the sub-optimality gap. Moreover, if the round $T \geq {2^{{2/\beta} - 3}K{({\log T})}^{{2/\beta} - 1}}$, the problem-independent regret of bootstrapped UCB is upper bounded by The main proof structure follows the standard analysis of UCB and relies on a sharp upper bound for the (data-dependent) bootstrapped quantile term by Theorem 3.1. ‣ 3.1 Regret Bound for Bootstrapped UCB ‣ 3 Regret Analysis ‣ Bootstrapping Upper Confidence Bound"). Details are deferred to Section B.3 in the supplement. When $\beta \geq 1$, (3.2) provides a logarithm regret that matches the state-of-art result. When $\beta < 1$, we have a non-negligible term ${({\log T})}^{1/\beta}$ that is the price paid for heavy-tailedness. However, this term does not depend on the gap $\Delta_{k}$. Therefore, we have an optimal problem-independent regret bound.

### Remark 3.3

The choice of $\alpha = {1/T^{2}}$ led to an easy analysis. Using similar techniques in Chapter 8.2 of, we can achieve a similar regret bound by setting $\alpha_{t} = {1/{({t{\log^{\tau}{(t)}}})}}$ for any $\tau > 0$.

### Remark 3.4

consider bandit with heavy-tail (moment of order $({1 + \varepsilon})$) based on a median-of-means estimator. As mentioned in Chen and Zhou, there are two disadvantages for median-of-means approach: (a) it involves an additional tuning parameter; (b) it is numerically unstable for small sample size. In contrast, we identify a class of heavy-tailed bandits (sub-Weibull bandit) where mean estimators can still achieve regret bounds of the same order as those under sub-Gaussian reward distributions. The reason is that although sub-Weibull r.v. has heavier tail than sub-Gaussian r.v., its tail still has an exponential-like decay.

## Experiments

In Section 4.1, we consider multi-armed bandits with both symmetric and asymmetric rewards. In Section 4.2, we extend our method to linear bandits. Implementation details and some additional experimental results are deferred to Section E in the supplement.

### Multi-armed Bandit

In this section, we compare bootstrapped UCB (Algorithm 1) with three baselines: Upper Confidence Bound based on concentration inequalities (Vanilla UCB), Thompson sampling with normal Jeffery prior (Jeffery-TS) and Thompson sampling with Beta prior (Bernoulli-TS). For bounded rewards, we also compare with Giro ^11^1We have implemented Giro in the unbounded reward case, which could result in linear regret in most cases. See Figure 7 in the supplement. So, it's unclear what is the best way to add pseudo observations in this case., that is a sampling-based exploration method by adding artificial pseudo observations $\{ 0,1\}$ to escape from local optima, and empirical KL-UCB using package: PymaBandits. For the preliminary bound $\varphi{({\mathbf{y}}_{n})}$, we simply choose the one derived by the concentration inequality. Note that the second-order correction term in (2.5. ‣ 2.2 Second-order Correction ‣ 2 Bootstrapped UCB ‣ Bootstrapping Upper Confidence Bound")) is conservative. For practitioners, we suggest to set the correction term to be ${\varphi{({\mathbf{y}}_{n})}}/\sqrt{n}$. To be fair, we choose the confidence level $\alpha = {1/{({1 + t})}}$ for both UCB1 and bootstrapped UCB, and $\delta = 0.1$ in (2.5. ‣ 2.2 Second-order Correction ‣ 2 Bootstrapped UCB ‣ Bootstrapping Upper Confidence Bound")). All algorithms above require knowledge of an upper bound on the noise standard deviation. The number of bootstrap repetitions is $B = 200$, and the number of arms is $K = 5$.

First, we consider symmetric rewards with a mean parameter $\mu_{k}$ generated from $\text{Uniform}{({- 1},1)}$. The noise follows either truncated-normal distribution within $\lbrack{- 1},1\rbrack$, or standard Gaussian distribution. From Figure 2, bootstrapped UCB outperforms Jeffery-TS and Vanilla-UCB for truncated-normal bandit and has comparable or sometimes better performance over empirical KL-UCB. It's obvious that if the reward distribution is exactly Gaussian and the plug-in estimate for the noise standard deviation is the truth, Jeffery-TS should be the best. However, when the posterior (plots (a),(b)) or noise standard derivation (plot (c)) are mis-specified, the performance of TS deteriorates fast. Since (concentration-based) Vanilla UCB only uses the tail information (bounded or sub-Gaussian), it is very conservative and results in bad regret as expected.

Figure 2: Cumulative regrets for truncated-normal bandit and Gaussian bandit. Sigma is the upper bound on the standard deviation of the noise. The results are averaged over 200 realizations.

Second, we consider asymmetric rewards with a mean parameter $\mu_{k}$ generated from $\text{Uniform}{(0.25,0.75)}$. For Bernoulli bandit, the reward follows ${Ber}{(\mu_{k})}$; for Beta bandit, the reward follows ^22^2We adopt the technique in Agrawal and Goyal to run Thompson Sampling with $\lbrack 0,1\rbrack$ rewards. In particular, for any reward $y_{t} \in {\lbrack 0,1\rbrack}$, we draw pseudo reward ${\hat{y}}_{t} \sim {{Ber}{(y_{t})}}$, and then use ${\hat{y}}_{t}$ instead of $y_{t}$ in the algorithm. ${Beta}{({v\mu_{k}},{v{({1 - \mu_{k}})}})}$ for $v = 8$. From Figure 3, bootstrapped UCB outperforms Vanilla UCB and Giro in both cases, and outperforms Bernoulli-TS for Beta bandit. In fact, we are supposed not to beat Bernoulli-TS for Bernoulli bandit since TS fully makes use of the distribution knowledge in this case. One possible explanation is that our method is non-parametric.

Figure 3: Cumulative regrets for Bernoulli bandit and Beta bandit. The results are averaged over 200 realizations.

Third, we demonstrate that the robustness of bootstrapped UCB over mis-specifications of the noise standard deviation. In the left panel of Figure 4, we consider the cumulative regret at round $T = 2000$ of standard Gaussian bandit. As one can see, when we increase the plug-in upper bound of the standard deviation of the noise, bootstrapped UCB is more robust than Bernoulli-TS and Vanilla UCB.

Figure 4: The left panel is the cumulative regret over noise levels while the right panel is the instance-dependent regret of various algorithms as a function of gaps. The results are averaged over 200 realizations.

Last, we present a frequentist instance-dependent regret curve for truncated-normal bandit and the experiment set up follows Lattimore. We plot cumulative regrets at $T = 2000$ of various algorithms with respect to the instance gap $\Delta$ and the mean vector $\mu = {(\Delta,0,0,0,0)}$. The results are summarized in the right panel of Figure 4.

### Linear Bandit

We extend our method to linear bandit case. The basic set up follows the one in Russo and Van Roy. In detail, ${\mathbf{θ}}^{\ast} \in {\mathbb{R}}^{d}$ is drawn from a multivariate Gaussian distribution with mean vector $\mu = 0$ and covariance matrix $\Sigma = {10I_{d}}$. The noise follows a standard Gaussian distribution. There are $100$ actions with feature vector components drawn uniformly at random from $\lbrack{- {1/\sqrt{10}}},{1/\sqrt{10}}\rbrack$. We consider two state-of-art methods: Thompson sampling for linear bandit (TSL) and optimism in the face of uncertainty for linear bandits (OFUL). Following the principle of constructing second-order correction in mean problems (Theorem 2.2. ‣ 2.2 Second-order Correction ‣ 2 Bootstrapped UCB ‣ Bootstrapping Upper Confidence Bound")), we construct the bootstrapped UCB for linear bandit (BUCBL) as follows: At each round $t$, the action is selected as $\operatorname{argmax}_{\mathbf{x}}{({{{\mathbf{x}}^{\top}{\hat{\mathbf{θ}}}_{t}} + {\beta_{t,{1 - \delta}}^{\text{BUCBL}}{\|{\mathbf{x}}\|}_{V_{t}^{- 1}}}})}$, where $\beta_{t,{1 - \delta}}^{\text{BUCBL}} = {{q_{\alpha}{({{\hat{\mathbf{θ}}}_{t}^{(b)} - {\hat{\mathbf{θ}}}_{t}})}} + {\beta_{t,{1 - \delta},\sigma}^{\text{OFUL}}/\sqrt{n}}}$. The formal definition of ${\hat{\mathbf{θ}}}_{t},{\hat{\mathbf{θ}}}_{t}^{(b)},\beta_{t,{1 - \delta},\sigma}^{\text{OFUL}}$ and some basic setups are given in Section E.2 in the supplement. To be fair, the confidence level for all methods is set to be $\delta = {1/{({1 + t})}}$ and we plug in the true standard deviation of the noise for each method. From Figure 5, we can see that bootstrapped UCB greatly improves the cumulative regret over TSL and OFUL.

Figure 5: Cumulative regret for linear bandit.

## Conclusion

In this paper, we propose a novel class of non-parametric and data-driven UCB algorithms based on multiplier bootstrap. It is easy to implement and has the potential to be generalized to other complex structured problems. As future works, we will evaluate our idea on other structured contextual bandits and reinforcement learning problems.
