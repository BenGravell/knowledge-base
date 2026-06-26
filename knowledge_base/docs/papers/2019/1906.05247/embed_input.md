<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Bootstrapping Upper Confidence Bound

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Upper Confidence Bound (UCB) method is arguably the most celebrated one used in online decision making with partial information feedback. Existing techniques for constructing confidence bounds are typically built upon various concentration inequalities, which thus lead to over-exploration. In this paper, we propose a non-parametric and data-dependent UCB algorithm based on the multiplier bootstrap. To improve its finite sample performance, we further incorporate second-order correction into the above construction. In theory, we derive both problem-dependent and problem-independent regret bounds for multi-armed bandits under a much weaker tail assumption than the standard sub-Gaussianity. Numerical results demonstrate significant regret reductions by our method, in comparison with several baselines in a range of multi-armed and linear bandit problems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In artificial intelligence, learning to make decisions online plays a critical role in many fields, such as personalized news recommendation, robotics and the game of Go. To learn to make optimal decisions as soon as possible, the decision-makers must carefully design an algorithm to balance the trade-off between the exploration and exploitation. Over-exploration could be expensive and unethical in practice, e.g., medical decision making. On the other hand, insufficient exploration tends to make an algorithm stuck at a sub-optimal solution. The delicate design of exploration methods stands in the heart of online learning and decision making.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Upper Confidence Bound (UCB) is a class of highly effective algorithms in dealing with the exploration-exploitation trade-off in bandits and reinforcement learning. The tightness of confidence bound, as is known, is the key ingredient to achieve the optimal degree of explorations. To the best of our knowledge, nearly all the existing works construct confidence bounds based on various concentration inequalities, e.g. Hoeffding-type, empirical Bernstein type or self-normalized type. Those concentration-based confidence bounds, however, are typically conservative since they are *data-independent.* Concentration inequalities only exploit tail information, e.g., bounded or sub-Gaussian, rather than the whole distribution knowledge. In general, the loose constant factor may result in confidence bounds that are too wide to be informative.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a non-parametric and data-dependent UCB algorithm based on the multiplier bootstrap, called bootstrapped UCB. The principle is to use the multiplier bootstrapped quantile as the confidence bound to enforce the exploration. Inspired by recent advances on non-asymptotic guarantee and non-asymptotic inference such as, we develop an explicit second-order correction for the multiplier bootstrapped quantile that ensures the non-asymptotic validity. Our algorithm is easy to implement and has the potential to be generalized to more complicated models such as structured contextual bandits.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In theory, we develop both problem-dependent and problem-independent regret bounds for multi-armed bandits with symmetric rewards under a much weaker tail assumption, i.e., sub-Weibull distribution, than the classical sub-Gaussianity. In this case, it is proven that the mean estimator can still achieve the same problem-independent regret bound as the one under the sub-Gaussian assumption. Note that our result does not rely on other sophisticated approaches such as median-of-means or Catoni's M-estimator. A key technical tool we propose is a new concentration inequality for the sum of sub-Weibull random variables. Empirically, we evaluate our method in several multi-armed and linear bandit models. When the exact posterior is unavailable or the noise variance is mis-specified, the bootstrapped UCB demonstrates superior performance over variants of Thompson sampling and concentration-based UCB due to its non-parametric and data-dependent nature.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, an increasing number of works study bootstrap methods for multi-armed and contextual bandits as an alternative to Thompson sampling. Most treat the bootstrap just as a way to randomize historical data (without any theoretical guarantee). One exception is who derive a regret bound for Bernoulli bandit by adding pseudo observations. However, their method cannot be easily extended to unbounded cases, and their analyses heavily limit to the Bernoulli assumption. In contrast, our method applies to a broader class of bandit models with rigorous regret analysis.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. Section 2 introduces the basic setup and our bootstrapped UCB algorithm. Section 3 provides the regret analysis and Section 4 conducts several experiments.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Notations", "weight": 1.0} -->

Throughout the paper, we denote ${{\mathbb{P}}_{\mathbf{w}}{( \cdot )}},{{\mathbb{E}}_{\mathbf{w}}{( \cdot )}}$ as the probability and expectation operator with respect to the distribution of the vector $\mathbf{w}$ only, conditioning on other random variables. We use similar notations for ${\mathbb{P}}_{\mathbf{y}}{( \cdot )}$, ${\mathbb{E}}_{\mathbf{y}}{( \cdot )}$ with respect to $\mathbf{y}$ only. $\lbrack n\rbrack$ means the set $\{ 1,2,\ldots,n\}$. We denote boldface lower letters (e.g. $\mathbf{x}$, $\mathbf{y}$) as a vector.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Notations", "weight": 1.0} -->

For a set $\mathcal{E}$, we define its complement as $\mathcal{E}^{c}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem setup", "weight": 1.0} -->

As a fruit fly, we illustrate our idea on the stochastic multi-armed bandit problem. In detail, the decision-makers interact with an environment for $T$ rounds. In round $t \in {\lbrack T\rbrack}$, the decision-makers pull an arm $I_{t} \in {\lbrack K\rbrack}$ and observes its reward $y_{I_{t}}$ which is drawn from a distribution associated with the arm $I_{t}$, denoted by $P_{I_{t}}$ with an unknown mean $\mu_{I_{t}}$. Without loss of generality, we assume arm $1$ is the optimal arm, that is, $\mu_{1} = {\max_{k \in {\lbrack K\rbrack}}\mu_{k}}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem setup", "weight": 1.0} -->

In multi-armed bandit problems, the objective is to minimize the expected cumulative regret, defined as, where $\Delta_{k} = {\mu_{1} - \mu_{k}}$ is the sub-optimality gap for arm $k$, and $\mathbf{I}{\{ \cdot \}}$ is an indicator function. Here, the second equality is from the regret decomposition Lemma (Lemma 4.5 in). We call an upper bound of $R{(T)}$ problem-independent if the bound only depends on the distributional assumption and not on the specific bandit problem, say the gap $\Delta_{k}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Upper Confidence Bound", "weight": 1.0} -->

The upper confidence bound (UCB) algorithm is based on the principle of optimism in the face of uncertainty. The key idea is to act as if the environment (parameterized by $\mu_{k}$ in multi-armed bandits) is as nice as plausibly possible. Concretely, a plausible environment refers to an upper confidence bound $\mathcal{G}{({\mathbf{y}}_{n},{1 - \alpha})}$ for the true mean $\mu$, of the form where ${\mathbf{y}}_{n} = {(y_{1},\ldots,y_{n})}^{\top}$ is the sample vector, ${\overline{y}}_{n}$ is the empirical mean, $\alpha \in {}$ is the confidence level, and $h_{\alpha}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{+}}$ is a threshold that could be either data-dependent or data-independent.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Multiplier Bootstrap", "weight": 1.0} -->

Multiplier bootstrap is a fast and easy-to-implement alternative to the standard bootstrap, and has been successfully applied in various statistical contexts. Its goal is to approximate the distribution of the target statistic by reweighing its summands with random multipliers independent of the data. For instance, in a mean estimation problem, we define a multiplier bootstrapped estimator as ${{n^{- 1}{\sum_{i = 1}^{n}{w_{i}{({y_{i} - {\overline{y}}_{n}})}}}} = {n^{- 1}{\sum_{i = 1}^{n}{{({w_{i} - {\overline{w}}_{n}})}y_{i}}}}},$ where ${\{ w_{i}\}}_{i = 1}^{n}$ are some random variables independent of ${\mathbf{y}}_{n}$, called bootstrap weights.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Multiplier Bootstrap", "weight": 1.0} -->

Some classical weights are as follows: *Efron's bootstrap weights.* $(w_{1},\ldots,w_{n})$ is a multinomial random vector with parameters $(n;n^{- 1},\ldots,n^{- 1})$. This is the standard nonparameteric bootstrap.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Multiplier Bootstrap", "weight": 1.0} -->

*Gaussian weights.* $w_{i}$'s are i.i.d standard Gaussian random variables. This is closely related to Gaussian approximation in statistics.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Multiplier Bootstrap", "weight": 1.0} -->

*Rademacher weights.* $w_{i}$'s are i.i.d Rademacher variables. This is closely related to symmetrization in learning theory.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Multiplier Bootstrap", "weight": 1.0} -->

The bootstrap principle suggests that the $({1 - \alpha})$-quantile of the distribution of $n^{- 1}{\sum_{i = 1}^{n}{w_{i}{({y_{i} - {\overline{y}}_{n}})}}}$ conditionally on ${\mathbf{y}}_{n}$ could be used to approximate the $({1 - \alpha})$-quantile of the distribution of ${\overline{y}}_{n} - \mu$. As the first building block, the multiplier bootstrapped quantile is defined as, The question is whether $q_{\alpha}{({{\mathbf{y}}_{n} - {\overline{y}}_{n}})}$ is a valid threshold for any sample size $n \geq 1$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Second-order Correction", "weight": 1.0} -->

Most statistical theories guarantee the asymptotic validity of $q_{\alpha}{({{\mathbf{y}}_{n} - {\overline{y}}_{n}})}$ by the multiplier central limit theorem. However, we show that such a claim is valid *non-asymptotically* at the cost of adding a second-order correction. Next theorem rigorously characterizes this phenomenon under a symmetric assumption on the reward. Moreover, in Section A in the supplement, we show that without the second-order correction, a naive bootstrapped UCB will result in linear regret.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 2.3 (Choice of $\\varphi{({\\mathbf{y}}_{n})}$)", "weight": 1.0} -->

If ${\{ y_{i}\}}_{i = 1}^{n}$ are independent 1-sub-Gaussian random variables, a natural choice of $\varphi{({\mathbf{y}}_{n})}$ is ${({{2{\log{({1/\alpha})}}}/n})}^{1/2}$ by Hoeffding's inequality (Lemma 2. ‣ Appendix F Supporting Lemmas ‣ Bootstrapping Upper Confidence Bound")). Plugging it into (2.5. ‣ 2.2 Second-order Correction ‣ 2 Bootstrapped UCB ‣ Bootstrapping Upper Confidence Bound")) and letting $\delta = {1/2}$, the bootstrapped threshold in (2.5.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 2.3 (Choice of $\\varphi{({\\mathbf{y}}_{n})}$)", "weight": 1.0} -->

‣ 2.2 Second-order Correction ‣ 2 Bootstrapped UCB ‣ Bootstrapping Upper Confidence Bound")) becomes Lemma B.3 in the supplement shows that the main term is of order at least $\mathcal{O}{(n^{- {1/2}})}$ as $n$ grows, which implies the second order correction is just a remainder term. We emphasize that the reminder term is obviously not sharp and will be sharpened as a future work.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 2.4", "weight": 1.0} -->

Existing works on UCB-type algorithms typically utilized various concentration inequalities, e.g. Hoeffding's inequality or empirical Bernstein's inequality, to find a valid threshold $h_{\alpha}{({\mathbf{y}}_{n})}$. However, they are not data-dependent and only use the tail information, rather than fully exploit the whole distribution knowledge. This is typically conservative, and leads to over-exploration.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 2.5", "weight": 1.0} -->

Empirical KL-UCB used empirical likelihood to build confidence intervals for general distributions that have support in $\lbrack 0,1\rbrack$. Although empirical KL-UCB is also data-dependent, our proposed method is from a very different non-parametric perspective and uses different tools by bootstrap. In practice, resampling tends to be more efficient computationally, without solving a convex optimization each round like empirical KL-UCB. Moreover, our method can work with unbounded rewards and we believe it is easier to generalize to structured bandits, e.g. linear bandit.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 2.5", "weight": 1.0} -->

In Figure 1, we compare different approaches to calculate 95% confidence bound for the population mean based on samples from a truncated-normal distribution. When the sample size is extremely small $({\leq 10})$, the naive bootstrap (without any correction) cannot output a valid threshold since the bootstrapped quantile is smaller than the true 95% quantile. This confirms the necessity of the second-order correction. When the sample size increases, our bootstrapped threshold converges to the truth rapidly. This confirms the correction term is just a small remainder term. Additionally, the bootstrapped threshold is shown to be sharper than Hoeffding's bound and empirical Bernstein bound when sample size is large (see the right panel of Figure 1).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Main Algorithm: Bootstrapped UCB", "weight": 1.0} -->

Based on the above theoretical findings, we conclude that bootstrapped UCB will select the arm according to its UCB index defined as below: where $n_{k,t}$ is the number of pulls for arm $k$ until time $t$. Practically, we may use Monte Carlo quantile approximation to get an approximated bootstrapped quantile ${\overset{\sim}{q}}_{\alpha{({1 - \delta})}}{({{\mathbf{y}}_{n_{k,t}} - {\overline{y}}_{n_{k,t}}},{\mathbf{w}}^{B})}$ and corresponding theorem for the control of the approximation of the bootstrapped quantile is also derived (see Section D in the supplement for details).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Main Algorithm: Bootstrapped UCB", "weight": 1.0} -->

The algorithm is summarized in Algorithm 1. The computational complexity at step $t$ is ${\overset{\sim}{\mathcal{O}}{({Bt})}} \leq {\overset{\sim}{\mathcal{O}}{({BT})}}$. Comparing with vanilla UCB, the extra $Bt$ is due to resampling. In practice, the choice of $B$ is seldom treated as a tuning parameter, but usually determined by the available computational resource.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Regret Analysis", "weight": 1.0} -->

In Section 3.1, we derive regret bounds for bootstrapped UCB. Moreover, we show that naive bootstrapped UCB will result in linear regret in some cases in Section A in the supplement.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Regret Bound for Bootstrapped UCB", "weight": 1.0} -->

For multi-armed bandit problems, most literature consider sub-Gaussian rewards. In this work, we move beyond sub-Gaussianity and consider the reward under a much weaker tail assumption, so-called sub-Weibull distribution. As shown, it is characterized by the right tail of the Weibull distribution and generalizes sub-Gaussian and sub-exponential distributions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

The choice of $\alpha = {1/T^{2}}$ led to an easy analysis. Using similar techniques in Chapter 8.2 of, we can achieve a similar regret bound by setting $\alpha_{t} = {1/{({t{\log^{\tau}{(t)}}})}}$ for any $\tau > 0$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

consider bandit with heavy-tail (moment of order $({1 + \varepsilon})$) based on a median-of-means estimator. As mentioned in Chen and Zhou, there are two disadvantages for median-of-means approach: (a) it involves an additional tuning parameter; (b) it is numerically unstable for small sample size. In contrast, we identify a class of heavy-tailed bandits (sub-Weibull bandit) where mean estimators can still achieve regret bounds of the same order as those under sub-Gaussian reward distributions. The reason is that although sub-Weibull r.v. has heavier tail than sub-Gaussian r.v., its tail still has an exponential-like decay.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

In Section 4.1, we consider multi-armed bandits with both symmetric and asymmetric rewards. In Section 4.2, we extend our method to linear bandits. Implementation details and some additional experimental results are deferred to Section E in the supplement.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Multi-armed Bandit", "weight": 1.0} -->

In this section, we compare bootstrapped UCB (Algorithm 1) with three baselines: Upper Confidence Bound based on concentration inequalities (Vanilla UCB), Thompson sampling with normal Jeffery prior (Jeffery-TS) and Thompson sampling with Beta prior (Bernoulli-TS). For bounded rewards, we also compare with Giro ^11^1We have implemented Giro in the unbounded reward case, which could result in linear regret in most cases. See Figure 7 in the supplement. So, it's unclear what is the best way to add pseudo observations in this case., that is a sampling-based exploration method by adding artificial pseudo observations $\{ 0,1\}$ to escape from local optima, and empirical KL-UCB using package: PymaBandits. For the preliminary bound $\varphi{({\mathbf{y}}_{n})}$, we simply choose the one derived by the concentration inequality. Note that the second-order correction term in (2.5. ‣ 2.2 Second-order Correction ‣ 2 Bootstrapped UCB ‣ Bootstrapping Upper Confidence Bound")) is conservative.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Multi-armed Bandit", "weight": 1.0} -->

For practitioners, we suggest to set the correction term to be ${\varphi{({\mathbf{y}}_{n})}}/\sqrt{n}$. To be fair, we choose the confidence level $\alpha = {1/{({1 + t})}}$ for both UCB1 and bootstrapped UCB, and $\delta = 0.1$ in (2.5. ‣ 2.2 Second-order Correction ‣ 2 Bootstrapped UCB ‣ Bootstrapping Upper Confidence Bound")). All algorithms above require knowledge of an upper bound on the noise standard deviation. The number of bootstrap repetitions is $B = 200$, and the number of arms is $K = 5$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Multi-armed Bandit", "weight": 1.0} -->

First, we consider symmetric rewards with a mean parameter $\mu_{k}$ generated from $\text{Uniform}{({- 1},1)}$. The noise follows either truncated-normal distribution within $\lbrack{- 1},1\rbrack$, or standard Gaussian distribution. From Figure 2, bootstrapped UCB outperforms Jeffery-TS and Vanilla-UCB for truncated-normal bandit and has comparable or sometimes better performance over empirical KL-UCB. It's obvious that if the reward distribution is exactly Gaussian and the plug-in estimate for the noise standard deviation is the truth, Jeffery-TS should be the best. However, when the posterior (plots (a),(b)) or noise standard derivation (plot (c)) are mis-specified, the performance of TS deteriorates fast. Since (concentration-based) Vanilla UCB only uses the tail information (bounded or sub-Gaussian), it is very conservative and results in bad regret as expected.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Multi-armed Bandit", "weight": 1.0} -->

Second, we consider asymmetric rewards with a mean parameter $\mu_{k}$ generated from $\text{Uniform}{(0.25,0.75)}$. For Bernoulli bandit, the reward follows ${Ber}{(\mu_{k})}$; for Beta bandit, the reward follows ^22^2We adopt the technique in Agrawal and Goyal to run Thompson Sampling with $\lbrack 0,1\rbrack$ rewards. In particular, for any reward $y_{t} \in {\lbrack 0,1\rbrack}$, we draw pseudo reward ${\hat{y}}_{t} \sim {{Ber}{(y_{t})}}$, and then use ${\hat{y}}_{t}$ instead of $y_{t}$ in the algorithm. ${Beta}{({v\mu_{k}},{v{({1 - \mu_{k}})}})}$ for $v = 8$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Multi-armed Bandit", "weight": 1.0} -->

From Figure 3, bootstrapped UCB outperforms Vanilla UCB and Giro in both cases, and outperforms Bernoulli-TS for Beta bandit. In fact, we are supposed not to beat Bernoulli-TS for Bernoulli bandit since TS fully makes use of the distribution knowledge in this case. One possible explanation is that our method is non-parametric.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Multi-armed Bandit", "weight": 1.0} -->

Third, we demonstrate that the robustness of bootstrapped UCB over mis-specifications of the noise standard deviation. In the left panel of Figure 4, we consider the cumulative regret at round $T = 2000$ of standard Gaussian bandit. As one can see, when we increase the plug-in upper bound of the standard deviation of the noise, bootstrapped UCB is more robust than Bernoulli-TS and Vanilla UCB.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Multi-armed Bandit", "weight": 1.0} -->

Last, we present a frequentist instance-dependent regret curve for truncated-normal bandit and the experiment set up follows Lattimore. We plot cumulative regrets at $T = 2000$ of various algorithms with respect to the instance gap $\Delta$ and the mean vector $\mu = {(\Delta,0,0,0,0)}$. The results are summarized in the right panel of Figure 4.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Linear Bandit", "weight": 1.0} -->

We extend our method to linear bandit case. The basic set up follows the one in Russo and Van Roy. In detail, ${\mathbf{θ}}^{\ast} \in {\mathbb{R}}^{d}$ is drawn from a multivariate Gaussian distribution with mean vector $\mu = 0$ and covariance matrix $\Sigma = {10I_{d}}$. The noise follows a standard Gaussian distribution. There are $100$ actions with feature vector components drawn uniformly at random from $\lbrack{- {1/\sqrt{10}}},{1/\sqrt{10}}\rbrack$. We consider two state-of-art methods: Thompson sampling for linear bandit (TSL) and optimism in the face of uncertainty for linear bandits (OFUL). Following the principle of constructing second-order correction in mean problems (Theorem 2.2.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Linear Bandit", "weight": 1.0} -->

The formal definition of ${\hat{\mathbf{θ}}}_{t},{\hat{\mathbf{θ}}}_{t}^{(b)},\beta_{t,{1 - \delta},\sigma}^{\text{OFUL}}$ and some basic setups are given in Section E.2 in the supplement. To be fair, the confidence level for all methods is set to be $\delta = {1/{({1 + t})}}$ and we plug in the true standard deviation of the noise for each method. From Figure 5, we can see that bootstrapped UCB greatly improves the cumulative regret over TSL and OFUL.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we propose a novel class of non-parametric and data-driven UCB algorithms based on multiplier bootstrap. It is easy to implement and has the potential to be generalized to other complex structured problems. As future works, we will evaluate our idea on other structured contextual bandits and reinforcement learning problems.
