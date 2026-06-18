<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Concentration Bounds for CVaR Estimation: The Cases of Light-tailed and Heavy-tailed Distributions

Topics include Bandits, Optimization, Concentration bounds, Conditional value at risk, Random variable.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Conditional Value-at-Risk (CVaR) is a widely used risk metric in applications such as finance. We derive concentration bounds for CVaR estimates, considering separately the cases of light-tailed and heavy-tailed distributions. In the light-tailed case, we use a classical CVaR estimator based on the empirical distribution constructed from the samples. For heavy-tailed random variables, we assume a mild `bounded moment' condition, and derive a concentration bound for a truncation-based estimator. Notably, our concentration bounds enjoy an exponential decay in the sample size, for heavy-tailed as well as light-tailed distributions. To demonstrate the applicability of our concentration results, we consider a CVaR optimization problem in a multi-armed bandit setting. Specifically, we address the best CVaR-arm identification problem under a fixed budget. We modify the well-known successive rejects algorithm to incorporate a CVaR-based criterion. Using the CVaR concentration result, we derive an upper-bound on the probability of incorrect identification by the proposed algorithm.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In applications such as portfolio optimization in finance, the quality of a portfolio is not satisfactorily captured by the expected value of return. Indeed, in such applications, a more risk-sensitive metric is desirable, so as to capture typical losses in the case of adverse events. Value-at-Risk (VaR) and Conditional-Value-at-Risk (CVaR) are two risk-aware metrics, which are widely used in applications such as portfolio optimization and insurance. VaR at level $\alpha \in $ conveys the maximum loss incurred by the portfolio with a confidence of $\alpha.$ In other words, the portfolio incurs a loss greater than VaR at level $\alpha$ with probability ${1 - \alpha}.$ In turn, CVaR at level $\alpha \in $ captures the expected loss incurred by the portfolio, *given* that the losses exceed VaR at level $\alpha.$ CVaR has an advantage over VaR, in that the former is a *coherent^11^1A risk measure is said to be coherent, if it is monotonic, translation invariant, sub-additive, and positive homogeneous.* risk measure.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we derive concentration bounds for CVaR estimators, for both light-tailed and heavy-tailed random variables. For light-tailed distributions, our concentration bound uses a classical CVaR estimator based on the empirical distribution. For the heavy-tailed case, we employ a truncation-based CVaR estimator, and derive a concentration result under a mild assumption: the $p$th moment of the distribution is assumed to exist, for some ${p > 1}.$ Notably, our concentration bounds enjoy an exponential decay in the sample size, for heavy-tailed as well as light-tailed distributions. Our results also subsume or strengthen existing CVaR concentration results, as we discuss in the next subsection. We believe our bounds are order optimal, and the dependence the number of samples as well as the accuracy cannot be improved.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to highlight an important application for our CVaR concentration results, we consider a stochastic bandit set-up with a risk-sensitive metric for measuring the quality of an arm. In particular, we consider a $K$-armed stochastic bandit setting, and study the problem of finding the arm with the *lowest CVaR value* (at a fixed level $\alpha \in $) in a fixed budget setting. We propose an algorithm for the best CVaR arm identification that is inspired by successive-rejects. Using our CVaR concentration bound, we establish an upper bound on the probability of incorrect arm identification by our algorithm at the end of the given budget.

<!-- chunk {"id": "body-0006", "role": "body", "section": "CVaR estimation: Light-tailed case", "weight": 1.0} -->

In this section, we define empirical CVaR, provide a concentration result for CVaR estimation assuming that the underlying distribution is light-tailed, and subsequently present a multi-armed bandit application.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Concentration bounds", "weight": 1.0} -->

In the case of distributions with bounded support, a concentration result for CVaR exists in the literature. For the case of unbounded distributions, deriving a CVaR concentration result becomes considerably easier when the form of distributions are known, *i.e.,* when the closed-form expressions of VaR and CVaR can be derived. To illustrate, consider the case of a Gaussian r.v. $X$ with mean $\mu$ and variance $\sigma^{2}$. Let ${Q(\xi)} = {\frac{1}{\sqrt{2\pi}}{\int_{\xi}^{\infty}{{\exp\left( {- \left. x^{2}/2 \right.} \right)}{dx}}}}$. Notice that ${Q\left( {- x} \right)} = {1 - {Q(x)}}$ and also that ${F_{X}(\xi)} = {Q\left( \frac{\mu - \xi}{\sigma} \right)}$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Concentration bounds", "weight": 1.0} -->

Hence, $v_{\alpha}(X)$ is the solution to ${Q\left( \frac{\mu - \xi}{\sigma} \right)} = \alpha$, which implies that

<!-- chunk {"id": "body-0009", "role": "body", "section": "Concentration bounds", "weight": 1.0} -->

The CVaR $c_{\alpha}(X)$ for Gaussian $X$ can be shown, using Acerbi's formula \[6, pp. 329\], to be equal to ${\mu\left( \frac{\alpha}{1 - \alpha} \right)} + {\sigmac_{\alpha}(Z)}$, where $Z$ is the standard Gaussian random variable *i.e.,* ${Z \sim {\mathcal{N}}}.$

<!-- chunk {"id": "body-0010", "role": "body", "section": "Concentration bounds", "weight": 1.0} -->

It is clear from the above argument that estimates of $\mu$ and $\sigma$ are sufficient to estimate $c_{\alpha}(X)$ for the Gaussian case. Sample mean ${\hat{\mu}}_{n}$ and sample variance ${\hat{\sigma}}_{n}^{2}$ (computed using $n$ samples from the distribution of $X$) would serve this purpose and we obtain ${\hat{c}}_{n} = {{\hat{\mu}\left( \frac{\alpha}{1 - \alpha} \right)} + {\hat{\sigma}c_{\alpha}(Z)}}$ as a proxy for $c_{\alpha}(X)$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Concentration bounds", "weight": 1.0} -->

Given standard concentration bounds for these quantities through Hoeffding and Bernstein's inequalities, it is straightforward to establish that ${\hat{c}}_{n,\alpha}$ concentrates exponentially around ${c_{\alpha}(X)}.$ Similarly, for the case of exponential random variables, we can exploit the memoryless property to derive an explicit expression for CVaR, in terms of the mean $\mu$ and the level $\alpha.$

<!-- chunk {"id": "body-0012", "role": "body", "section": "Concentration bounds", "weight": 1.0} -->

We therefore focus on distributions that do not have closed-form expressions for VaR and CVaR. In such a setting, the CVaR has to be estimated directly from the available samples. However, for establishing concentration bounds for the CVaR, which involves conditioning on a tail event, it is common to make some assumptions on the tail distribution. In, an exponentially decaying CVaR concentration result is derived for the class of sub-Gaussian random variables, using a Wasserstein distance approach. However, the same approach provides unsatisfactory results (with power-law decay) for light-tailed as well as heavy-tailed distributions with bounded higher moments.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Concentration bounds", "weight": 1.0} -->

We now define the class of light-tailed distributions, while heavy-tailed distributions are handled in the next section.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

The bound in the theorem above is significantly better than the two-sided bound obtained in for the light-tailed case. In particular, the bound in the theorem above has an exponential tail decay irrespective of whether $\epsilon$ is large or small, while the bound in has an exponential decay for small $\epsilon$, and a power law for large $\epsilon$. For a light-tailed r.v., one expects a tail behavior similar to that of Gaussian with constant variance for small $\epsilon$, and an exponential decay for large $\epsilon$, and our bound is consistent with this expected behavior.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark 3.5", "weight": 1.0} -->

In comparison to the one-sided bound for light-tailed r.v.s, obtained, our bound exhibits much better dependence w.r.t. the number of samples $n$ as well as the accuracy $\epsilon$. More importantly, since our bound is two-sided, it opens avenues for a bandit application, while a one-sided bound is insufficient for this purpose.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 3.5", "weight": 1.0} -->

In the following section, we provide a multi-armed bandit algorithm that incorporates a CVaR objective, and analyze the finite-time performance of this algorithm using the bound derived in Theorem 3.3. ‣ 3.2 Concentration bounds ‣ 3 CVaR estimation: Light-tailed case ‣ Concentration bounds for CVaR estimation: The cases of light-tailed and heavy-tailed distributions").

<!-- chunk {"id": "body-0017", "role": "body", "section": "Application: Multi-armed bandits", "weight": 1.0} -->

We consider a $K$-armed stochastic bandit problem, with arms' distributions $\mathcal{P}_{1},\ldots,\mathcal{P}_{K}$. We study the problem of finding the arm with the *lowest CVaR value* (at a fixed level $\alpha \in $) in a fixed budget setting. In this setting, a bandit algorithm interacts with the environment over a given budget of $n$ rounds. In each round $t = {1,\ldots,n}$, the algorithm pulls an arm $I_{t} \in \left\{ 1,\ldots,K \right\}$ and observes a sample cost from the distribution $\mathcal{P}_{I_{t}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Application: Multi-armed bandits", "weight": 1.0} -->

At the end of the budget $n$ rounds, the bandit algorithm recommends an arm $J_{n}$ and is judged based on the probability of incorrect identification, i.e., ${\mathbb{P}}\left\lbrack {J_{n} \neq i^{\ast}} \right\rbrack$, where $i^{\ast}$ denotes the best arm. Earlier works use the expected value to define the best arm, while we use CVaR.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Application: Multi-armed bandits", "weight": 1.0} -->

Set $A_{k + 1} = {A_{k} \smallsetminus {\underset{i\in A_{k}}{\arg ⁡\max}{\hat{c}}_{\alpha,n_{k}}^{i}}}$, i.e., remove the arm with the highest empirical CVaR, with ties broken arbitrarily. Output: Return the solitary element in AK. Algorithm 1 CVaR-SR algorithm

<!-- chunk {"id": "body-0020", "role": "body", "section": "Application: Multi-armed bandits", "weight": 1.0} -->

Algorithm 1 presents the pseudo code of our CVaR-SR algorithm, designed to find the CVaR-optimal arm under a fixed budget. The algorithm is a variation of the regular successive rejects (SR) algorithm, with the following key difference: regular SR uses sample mean to estimate the expected value of each arm, while CVaR-SR used empirical CVaR, as defined, to estimate CVaR for each arm. The elimination logic, i.e., having $K - 1$ phases, and removing the worst arm (according to sample estimates of CVaR) at the end of each phase, is borrowed from regular SR.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Application: Multi-armed bandits", "weight": 1.0} -->

In the following result, we analyze the performance of CVaR-SR algorithm for light-tailed distributions.

<!-- chunk {"id": "body-0022", "role": "body", "section": "CVaR estimation: Heavy-tailed case", "weight": 1.0} -->

As mentioned before, an alternative proof approach using Wasserstein distance provides weak concentration rates for distributions with bounded higher moments - a gap that we address in this work. In particular, we employ a truncation-based estimator for CVaR to handle the case when the underlying distribution satisfies the following assumption:\
(C2) ${\exists p} \in {(1,2\rbrack,u}$ such that ${{\mathbb{E}}\left\lbrack |X|^{p} \right\rbrack} < u < \infty$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "CVaR estimation", "weight": 1.0} -->

Recall that $\left\{ X_{\lbrack i\rbrack} \right\}_{i = 1}^{n}$ denote the order statistics of $n$ i.i.d. samples drawn from the distribution of $X$. Using the VaR estimate ${\hat{v}}_{n,\alpha}$, as defined earlier in Section 3.1,

<!-- chunk {"id": "body-0024", "role": "body", "section": "CVaR estimation", "weight": 1.0} -->

In, $B_{i}$ represents a truncation level of $X_{i}$, and the choice for $B_{i}$ given above is under the assumption that ${{\mathbb{E}}\left\lbrack |X|^{p} \right\rbrack} < u < \infty$ for some $p \in (1,2\rbrack$. Such a truncation based estimator has been employed in the context of expected regret minimization with heavy-tailed random variables. Intuitively, the truncation level serves to discard very large samples values early, as $B_{i}$ is set to grow slowly with $i.$

<!-- chunk {"id": "body-0025", "role": "body", "section": "Concentration bounds", "weight": 1.0} -->

In particular, the following result is more general, as it can handle heavy-tailed distributions that satisfy (C2).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

A bandit application for the case of heavy-tailed distributions can be worked out using arguments similar to that in Section 3.3. The main difference is that the SR algorithm in the heavy-tailed case would involve a truncated estimator, and a slightly different hardness measure that is derived using Theorem 4.1. ‣ 4.2 Concentration bounds ‣ 4 CVaR estimation: Heavy-tailed case ‣ Concentration bounds for CVaR estimation: The cases of light-tailed and heavy-tailed distributions"). We omit the details due to space constraints.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

We derived concentration bounds for CVaR estimation, separately considering light-tailed and heavy-tailed distributions. For light-tailed distributions, our concentration bound uses a classical CVaR estimator based on the empirical distribution. For the heavy-tailed case, we employ a truncation based CVaR estimator, and derive a concentration result under a mild bounded-moment assumption. Our concentration bound enjoys exponential decay in the sample size even for heavy-tailed random variables. We highlighted the applicability of the CVaR concentration result by considering a risk-aware best bandit arm selection problem. We proposed an adaptation of the successive rejects algorithm to the setting where the goal is to find an arm with the lowest CVaR. Using the CVaR concentration bound, we established error bounds for the proposed algorithm.
