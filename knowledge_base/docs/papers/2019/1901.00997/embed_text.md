## Introduction

In applications such as portfolio optimization in finance, the quality of a portfolio is not satisfactorily captured by the expected value of return. Indeed, in such applications, a more risk-sensitive metric is desirable, so as to capture typical losses in the case of adverse events. Value-at-Risk (VaR) and Conditional-Value-at-Risk (CVaR) are two risk-aware metrics, which are widely used in applications such as portfolio optimization and insurance. VaR at level $\alpha \in $ conveys the maximum loss incurred by the portfolio with a confidence of $\alpha.$ In other words, the portfolio incurs a loss greater than VaR at level $\alpha$ with probability ${1 - \alpha}.$ In turn, CVaR at level $\alpha \in $ captures the expected loss incurred by the portfolio, *given* that the losses exceed VaR at level $\alpha.$ CVaR has an advantage over VaR, in that the former is a *coherent^11^1A risk measure is said to be coherent, if it is monotonic, translation invariant, sub-additive, and positive homogeneous.* risk measure.

In this paper, we derive concentration bounds for CVaR estimators, for both light-tailed and heavy-tailed random variables. For light-tailed distributions, our concentration bound uses a classical CVaR estimator based on the empirical distribution. For the heavy-tailed case, we employ a truncation-based CVaR estimator, and derive a concentration result under a mild assumption: the $p$th moment of the distribution is assumed to exist, for some ${p > 1}.$ Notably, our concentration bounds enjoy an exponential decay in the sample size, for heavy-tailed as well as light-tailed distributions. Our results also subsume or strengthen existing CVaR concentration results, as we discuss in the next subsection. We believe our bounds are order optimal, and the dependence the number of samples as well as the accuracy cannot be improved.

In order to highlight an important application for our CVaR concentration results, we consider a stochastic bandit set-up with a risk-sensitive metric for measuring the quality of an arm. In particular, we consider a $K$-armed stochastic bandit setting, and study the problem of finding the arm with the *lowest CVaR value* (at a fixed level $\alpha \in $) in a fixed budget setting. We propose an algorithm for the best CVaR arm identification that is inspired by successive-rejects. Using our CVaR concentration bound, we establish an upper bound on the probability of incorrect arm identification by our algorithm at the end of the given budget.

### Related Work

For the case of bounded distributions, a popular CVaR estimate has been shown to exponentially concentrate around the true CVaR -- see. In comparison to CVaR, obtaining a concentration result for VaR is easier, and does not require assumptions on the tail of the distribution -- see, a paper which also derives a one-sided CVaR concentration bound. More recent work considers CVaR concentration for distributions with bounded support on one side. In another recent paper, the authors derive an exponentially decaying concentration bound for the case of sub-Gaussian distributions, using a concentration result for the Wasserstein distance between the empirical and the true distributions. However, the above approach leads to poor concentration bounds (with power law decay in the sample size) for other relevant disribution classes, such as light-tailed and bounded-moment distributions.

While bandit learning has a long history, dating back to, risk-based criteria have been considered only recently. consider mean-variance optimization in a regret minimization framework. In the best arm identification setting, VaR-based criteria has been studied by and. CVaR-based criteria has been explored in a bandit context by, albeit with an assumption of bounded arms' distributions.

The rest of this paper is organized as follows: Section 2 presents the preliminaries. Sections 3 and 4 present the key concentration bounds for light and heavy-tailed distributions, respectively. Section 3.3 provides bandit algorithms and their analyses for the problem of the best CVaR arm identification with fixed budget under $K$-armed stochastic bandits. The proofs are contained in Section 5, and Section 6 concludes the paper.

## Preliminaries

Given a r.v. $X$ with cumulative distribution function (CDF) $F( \cdot )$, the VaR $v_{\alpha}(X)$ and CVaR $c_{\alpha}(X)$ at level $\alpha \in $ are defined as follows ^22^2For notational brevity, we omit $X$ from the notations $v_{\alpha}{(X)}$ and $c_{\alpha}{(X)}$ whenever the underlying the r.v. can be understood from the context.:

where we have used the notation ${\lbrack X\rbrack^{+} = {\max(0,X)}}.$ Typical values of $\alpha$ chosen in practice are $0.95$ and $0.99$. We make the following assumption for the purpose of CVaR estimation as well as for the concentration bounds derived later.\
(C1) The r.v. $X$ is continuous with strictly increasing CDF.

Under (C1), $v_{\alpha}(X)$ is a solution to ${{\mathbb{P}}\left\lbrack {X \leq \xi} \right\rbrack} = \alpha$, i.e., ${v_{\alpha}(X)} = {F^{- 1}(\alpha)}$. Further, if $X$ has a positive density at $v_{\alpha}(X)$, then ${c_{\alpha}(X)} = {{\mathbb{E}}\left\lbrack {\left. X \middle| X \right. \geq {v_{\alpha}(X)}} \right\rbrack}$ (cf. ).

## CVaR estimation: Light-tailed case

In this section, we define empirical CVaR, provide a concentration result for CVaR estimation assuming that the underlying distribution is light-tailed, and subsequently present a multi-armed bandit application.

### VaR and CVaR estimation

Let $\left\{ X_{i} \right\}_{i = 1}^{n}$ be $n$ i.i.d. samples drawn from the distribution of $X$. Let $\left\{ X_{\lbrack i\rbrack} \right\}_{i = 1}^{n}$ be the order statistics of $\left\{ X_{i} \right\}_{i = 1}^{n}$, i.e., ${X_{\lbrack 1\rbrack} \geq {X_{\lbrack 2\rbrack}\cdots} \geq X_{\lbrack n\rbrack}}.$ Let ${\hat{F}}_{n}( \cdot )$ be the empirical distribution function calculated using $\left\{ X_{i} \right\}_{i = 1}^{n}$, defined as ${{{{\hat{F}}_{n}(x)} = {\frac{1}{n}{\sum_{i = 1}^{n}{{\mathbb{I}}\left\{ {X_{i} \leq x} \right\}}}}},{{\forall x} \in {\mathbb{R}}}}.$ Notice that CVaR is a conditional expectation, where the conditioning event requires VaR. Thus, CVaR estimation requires VaR to be estimated as well. Let ${\hat{v}}_{n,\alpha}$ and ${\hat{c}}_{n,\alpha}$ denote the estimates of VaR and CVaR at level $\alpha$ using the $n$ samples above. These quantities are defined as follows:

### Concentration bounds

In the case of distributions with bounded support, a concentration result for CVaR exists in the literature. For the case of unbounded distributions, deriving a CVaR concentration result becomes considerably easier when the form of distributions are known, *i.e.,* when the closed-form expressions of VaR and CVaR can be derived. To illustrate, consider the case of a Gaussian r.v. $X$ with mean $\mu$ and variance $\sigma^{2}$. Let ${Q(\xi)} = {\frac{1}{\sqrt{2\pi}}{\int_{\xi}^{\infty}{{\exp\left( {- \left. x^{2}/2 \right.} \right)}{dx}}}}$. Notice that ${Q\left( {- x} \right)} = {1 - {Q(x)}}$ and also that ${F_{X}(\xi)} = {Q\left( \frac{\mu - \xi}{\sigma} \right)}$. Hence, $v_{\alpha}(X)$ is the solution to ${Q\left( \frac{\mu - \xi}{\sigma} \right)} = \alpha$, which implies that

The CVaR $c_{\alpha}(X)$ for Gaussian $X$ can be shown, using Acerbi's formula \[6, pp. 329\], to be equal to ${\mu\left( \frac{\alpha}{1 - \alpha} \right)} + {\sigmac_{\alpha}(Z)}$, where $Z$ is the standard Gaussian random variable *i.e.,* ${Z \sim {\mathcal{N}}}.$

It is clear from the above argument that estimates of $\mu$ and $\sigma$ are sufficient to estimate $c_{\alpha}(X)$ for the Gaussian case. Sample mean ${\hat{\mu}}_{n}$ and sample variance ${\hat{\sigma}}_{n}^{2}$ (computed using $n$ samples from the distribution of $X$) would serve this purpose and we obtain ${\hat{c}}_{n} = {{\hat{\mu}\left( \frac{\alpha}{1 - \alpha} \right)} + {\hat{\sigma}c_{\alpha}(Z)}}$ as a proxy for $c_{\alpha}(X)$. Given standard concentration bounds for these quantities through Hoeffding and Bernstein's inequalities, it is straightforward to establish that ${\hat{c}}_{n,\alpha}$ concentrates exponentially around ${c_{\alpha}(X)}.$ Similarly, for the case of exponential random variables, we can exploit the memoryless property to derive an explicit expression for CVaR, in terms of the mean $\mu$ and the level $\alpha.$

We therefore focus on distributions that do not have closed-form expressions for VaR and CVaR. In such a setting, the CVaR has to be estimated directly from the available samples. However, for establishing concentration bounds for the CVaR, which involves conditioning on a tail event, it is common to make some assumptions on the tail distribution. In, an exponentially decaying CVaR concentration result is derived for the class of sub-Gaussian random variables, using a Wasserstein distance approach. However, the same approach provides unsatisfactory results (with power-law decay) for light-tailed as well as heavy-tailed distributions with bounded higher moments.

We now define the class of light-tailed distributions, while heavy-tailed distributions are handled in the next section.

### Definition 3.1

A r.v. $X$ is said to be light-tailed if there exists a $c_{0} > 0$ such that ${{\mathbb{E}}{\lbrack{\exp{({\lambdaX})}}\rbrack}} < \infty$ for all ${{|\lambda|} < c_{0}}.$

The following lemma provides equivalent characterizations of light-tailed distributions -- see \[17, Theorem 2.2\].

### Lemma 3.2

The following statements are equivalent:

There exist constants ${\eta_{1},\eta_{2}} > 0$ such that ${{{{\mathbb{P}}\left\lbrack {|X| \geq t} \right\rbrack} \leq {\eta_{1}{\exp\left( {- {\eta_{2}t}} \right)}}},{{\forall t} > 0}}.$

There exist non-negative parameters $\sigma$ and $b$ such that

The following result presents a concentration bound for the case of light-tailed distributions:

### Theorem 3.3 (CVaR concentration: Light-tailed case)

Let ${\{ X_{i}\}}_{i = 1}^{n}$ be a sequence of i.i.d. r.v.s. Assume (C1). Let ${\hat{c}}_{n,\alpha}$ be the CVaR estimate given in formed using the above set of samples. Suppose that $X_{i}$, $i = {1,\ldots,n}$ are light-tailed with parameters $\sigma,b$, and VaR $v_{\alpha}$. Then, for any $\epsilon > 0$, we have

where $c$ is a distribution dependent constant.

A few remarks concerning the result above are in order.

### Remark 3.4

The bound in the theorem above is significantly better than the two-sided bound obtained in for the light-tailed case. In particular, the bound in the theorem above has an exponential tail decay irrespective of whether $\epsilon$ is large or small, while the bound in has an exponential decay for small $\epsilon$, and a power law for large $\epsilon$. For a light-tailed r.v., one expects a tail behavior similar to that of Gaussian with constant variance for small $\epsilon$, and an exponential decay for large $\epsilon$, and our bound is consistent with this expected behavior.

### Remark 3.5

In comparison to the one-sided bound for light-tailed r.v.s, obtained in, our bound exhibits much better dependence w.r.t. the number of samples $n$ as well as the accuracy $\epsilon$. More importantly, since our bound is two-sided, it opens avenues for a bandit application, while a one-sided bound is insufficient for this purpose.

In the following section, we provide a multi-armed bandit algorithm that incorporates a CVaR objective, and analyze the finite-time performance of this algorithm using the bound derived in Theorem 3.3. ‣ 3.2 Concentration bounds ‣ 3 CVaR estimation: Light-tailed case ‣ Concentration bounds for CVaR estimation: The cases of light-tailed and heavy-tailed distributions").

### Application: Multi-armed bandits

We consider a $K$-armed stochastic bandit problem, with arms' distributions $\mathcal{P}_{1},\ldots,\mathcal{P}_{K}$. We study the problem of finding the arm with the *lowest CVaR value* (at a fixed level $\alpha \in $) in a fixed budget setting. In this setting, a bandit algorithm interacts with the environment over a given budget of $n$ rounds. In each round $t = {1,\ldots,n}$, the algorithm pulls an arm $I_{t} \in \left\{ 1,\ldots,K \right\}$ and observes a sample cost from the distribution $\mathcal{P}_{I_{t}}$. At the end of the budget $n$ rounds, the bandit algorithm recommends an arm $J_{n}$ and is judged based on the probability of incorrect identification, i.e., ${\mathbb{P}}\left\lbrack {J_{n} \neq i^{\ast}} \right\rbrack$, where $i^{\ast}$ denotes the best arm. Earlier works use the expected value to define the best arm, while we use CVaR.

Let $c_{\alpha}^{i}$ and $v_{\alpha}^{i}$ denote the CVaR and VaR of the arm $i$ at level $\alpha.$ Let ${c^{\ast} = {\min_{i = {1,\ldots,K}}c_{\alpha}^{i}}},$ and $i^{\ast}$ be the arm that achieves this minimum. The goal is to devise an algorithm for which ${\mathbb{P}}\left\lbrack {J_{n} \neq i^{\ast}} \right\rbrack$ is small after $n$ rounds of sampling. Let arm-$\lbrack i\rbrack$ denotes the $i^{th}$ lowest CVaR valued arm. Let $\Delta_{i} = {c_{\alpha}^{i} - c_{\alpha}^{i^{\ast}}}$ denote the gap between the CVaR values of arm-$i$ and the optimal arm.

Initialization: Set A1 = {1,…,K}, ${{\overline{\log}K} = {\frac{1}{2} + {\sum\limits_{i = 2}^{K}\frac{1}{i}}}},{n_{0} = 0}$, $n_{k} = \left\lceil {\frac{1}{\overline{\log}K}\frac{n - K}{{K + 1} - k}} \right\rceil$, k = 1, …, K − 1.
Play each arm in Ak for (nk−nk − 1) times.
Compute the CVaR estimate ĉα, nki for each arm i ∈ Ak using.
Set $A_{k + 1} = {A_{k} \smallsetminus {\underset{i\in A_{k}}{\arg ⁡\max}{\hat{c}}_{\alpha,n_{k}}^{i}}}$, i.e., remove the arm with the highest empirical CVaR, with ties broken arbitrarily.
Output: Return the solitary element in AK.
Algorithm 1 CVaR-SR algorithm

Algorithm 1 presents the pseudo code of our CVaR-SR algorithm, designed to find the CVaR-optimal arm under a fixed budget. The algorithm is a variation of the regular successive rejects (SR) algorithm, with the following key difference: regular SR uses sample mean to estimate the expected value of each arm, while CVaR-SR used empirical CVaR, as defined in, to estimate CVaR for each arm. The elimination logic, i.e., having $K - 1$ phases, and removing the worst arm (according to sample estimates of CVaR) at the end of each phase, is borrowed from regular SR.

In the following result, we analyze the performance of CVaR-SR algorithm for light-tailed distributions.

### Theorem 3.6 (Probability of incorrect identification)

Consider a $K$-armed stochastic bandit, where the arms' distributions satisfy (C1) and are light-tailed. For a given budget $n$, the arm, say $J_{n}$, returned by the CVaR-SR algorithm satisfies:

where $G_{\max}$ is a problem dependent constant that does not depend on the underlying CVaR gaps and $n$, and

## CVaR estimation: Heavy-tailed case

As mentioned before, an alternative proof approach using Wasserstein distance provides weak concentration rates for distributions with bounded higher moments - a gap that we address in this work. In particular, we employ a truncation-based estimator for CVaR to handle the case when the underlying distribution satisfies the following assumption:\
(C2) ${\exists p} \in {(1,2\rbrack,u}$ such that ${{\mathbb{E}}\left\lbrack |X|^{p} \right\rbrack} < u < \infty$.

### CVaR estimation

Recall that $\left\{ X_{\lbrack i\rbrack} \right\}_{i = 1}^{n}$ denote the order statistics of $n$ i.i.d. samples drawn from the distribution of $X$. Using the VaR estimate ${\hat{v}}_{n,\alpha}$, as defined earlier in Section 3.1, we propose a truncation-based estimator ${\hat{c}}_{n,\alpha}$ for CVaR at level $\alpha$, defined as follows:

In, $B_{i}$ represents a truncation level of $X_{i}$, and the choice for $B_{i}$ given above is under the assumption that ${{\mathbb{E}}\left\lbrack |X|^{p} \right\rbrack} < u < \infty$ for some $p \in (1,2\rbrack$. Such a truncation based estimator has been employed in the context of expected regret minimization with heavy-tailed random variables in. Intuitively, the truncation level serves to discard very large samples values early on, as $B_{i}$ is set to grow slowly with $i.$

### Concentration bounds

In particular, the following result is more general, as it can handle heavy-tailed distributions that satisfy (C2).

### Theorem 4.1 (CVaR concentration: Bounded moment case)

Let ${\{ X_{i}\}}_{i = 1}^{n}$ be a sequence of i.i.d. r.v.s satisfying (C1) and (C2). Let ${\hat{c}}_{n,\alpha}$ be the CVaR estimate given in formed using the above set of samples. Fix $\epsilon > 0$.

For the case when ${p \in },$,

where $c$ is a distribution-dependent constant.

For the case when the distribution of $X$ has a bounded second moment, i.e., $p = 2$,

where $c^{\prime}$ is a distribution-dependent constant.

### Remark 4.2

A bandit application for the case of heavy-tailed distributions can be worked out using arguments similar to that in Section 3.3. The main difference is that the SR algorithm in the heavy-tailed case would involve a truncated estimator, and a slightly different hardness measure that is derived using Theorem 4.1. ‣ 4.2 Concentration bounds ‣ 4 CVaR estimation: Heavy-tailed case ‣ Concentration bounds for CVaR estimation: The cases of light-tailed and heavy-tailed distributions"). We omit the details due to space constraints.

## Proofs

### Proof of Theorem 3.3. ‣ 3.2 Concentration bounds ‣ 3 CVaR estimation: Light-tailed case ‣ Concentration bounds for CVaR estimation: The cases of light-tailed and heavy-tailed distributions")

Before providing the main proof, we note that empirical CVaR, as defined in, involves empirical VaR, and it is natural to expect that empirical CVaR concentration would require empirical VaR to concentrate as well. VaR concentration bounds have been derived recently in, and we recall their result below. This result will be used to establish the bound in Theorem 3.3. ‣ 3.2 Concentration bounds ‣ 3 CVaR estimation: Light-tailed case ‣ Concentration bounds for CVaR estimation: The cases of light-tailed and heavy-tailed distributions").

### Lemma 5.1 (VaR concentration)

Suppose that (C1) holds. For any ${\epsilon > 0},$ we have

where $c$ is a constant that depends on the value of the density $f$ of the r.v. $X$ in a neighbourhood of ${v_{\alpha}{(X)}}.$

### Proof of Theorem 3.3. ‣ 3.2 Concentration bounds ‣ 3 CVaR estimation: Light-tailed case ‣ Concentration bounds for CVaR estimation: The cases of light-tailed and heavy-tailed distributions")

The reader is referred to the initial passage in the proof of Proposition 5 in for a justification of the equality in.

Using $\left| {{{\hat{F}}_{n}\left( {\hat{v}}_{n,\alpha} \right)} - {F\left( v_{\alpha} \right)}} \right| \leq \left. 1/n \right.$, we obtain

where the final inequality uses the concentration result in Lemma 5.1. ‣ 5.1 Proof of Theorem 3.3 ‣ 5 Proofs ‣ Concentration bounds for CVaR estimation: The cases of light-tailed and heavy-tailed distributions") to obtain the first term, while the second term can be arrived at as follows: Letting $\epsilon^{\prime} = \frac{\left( {1 - \alpha} \right)\epsilon}{2}$,

where the first inequality follows by using the fact that $\left| {{{\hat{F}}_{n}\left( v_{\alpha} \right)} - {F\left( v_{\alpha} \right)}} \right| \leq 2$, since the empirical/true distributions are bounded above by $1$. The final inequality above uses the VaR concentration result from Lemma 5.1. ‣ 5.1 Proof of Theorem 3.3 ‣ 5 Proofs ‣ Concentration bounds for CVaR estimation: The cases of light-tailed and heavy-tailed distributions"). Thus,

for a distribution dependent constant $c_{3}.$

Next, using, the estimation error ${\hat{c}}_{n,\alpha} - c_{\alpha}$ can be written as

For bounding the $I_{1}$ term on the RHS above, we use the fact that $\left( {X - v_{\alpha}} \right)^{+}$ is a light-tailed r.v. This can be argued as follows: Letting $\mu_{\alpha}^{+} = {{\mathbb{E}}\left\lbrack \left( {X - v_{\alpha}} \right)^{+} \right\rbrack}$,

where ${c_{1},c_{2}},$ and $c_{4}$ are distribution-dependent constants. Next, using the fact that $X$ is light-tailed, we have

In the above, we have used the fact that ${{\mathbb{E}}\left\lbrack {\left( {X - v_{\alpha}} \right)^{2}{\mathbb{I}}\left\{ {X \geq v_{\alpha}} \right\}} \right\rbrack} \leq {{{\mathbb{E}}X^{2}} + v_{\alpha}^{2}}$. Comparing with the following identity:

it is easy to see that $\left( {X - v_{\alpha}} \right)^{+}$ is a light-tailed r.v. with parameters $\left( {\sigma^{2} + v_{\alpha}^{2}},b \right)$, whenever $X$ is light-tailed with parameters $\left( \sigma^{2},b \right)$ (see ).

Using a standard light-tailed concentration result (cf. Theorem 2.2. in ), we obtain

The main claim follows by using

and substituting the bounds obtained in and in the RHS above. ∎

### Proof of Theorem 3.6. ‣ 3.3 Application: Multi-armed bandits ‣ 3 CVaR estimation: Light-tailed case ‣ Concentration bounds for CVaR estimation: The cases of light-tailed and heavy-tailed distributions")

### Proof

We begin the proof by rewriting the CVaR concentration bound present in Theorem 3.3. ‣ 3.2 Concentration bounds ‣ 3 CVaR estimation: Light-tailed case ‣ Concentration bounds for CVaR estimation: The cases of light-tailed and heavy-tailed distributions") in a simplified manner as follows:

where ${G = {\min\left\{ \frac{c\left( {1 - \alpha} \right)}{2\left( {\sigma^{2} + v_{\alpha}^{2}} \right)},\frac{1}{4b},{c\left( {1 - \alpha} \right)} \right\}}}.$\
Note that, if the CVaR-SR algorithm has eliminated the optimal arm in phase $i$ then it implies that at least one of the last $i$ worst arms *i.e.,* one of the arms in $\left\{ \lbrack K\rbrack,\left\lbrack {K - 1} \right\rbrack,\cdots,\left\lbrack {{K - i} + 1} \right\rbrack \right\}$ must not have been eliminated in phase $i.$ Hence, we obtain

We now bound the above terms individually as follows.

where $(a)$ is due to Theorem 3.3. ‣ 3.2 Concentration bounds ‣ 3 CVaR estimation: Light-tailed case ‣ Concentration bounds for CVaR estimation: The cases of light-tailed and heavy-tailed distributions") and, and $G_{\max} = {\max_{i}G_{i}}$. Further, note that

where $H$ is as defined in the theorem statement. By substituting the above in, we obtain

Similarly, we can show that

The main claim follows by substituting and in. ∎

### Proof of Theorem 4.1. ‣ 4.2 Concentration bounds ‣ 4 CVaR estimation: Heavy-tailed case ‣ Concentration bounds for CVaR estimation: The cases of light-tailed and heavy-tailed distributions")

### Proof

Using $\left| {{{\hat{F}}_{n}\left( {\hat{v}}_{n,\alpha} \right)} - {F\left( v_{\alpha} \right)}} \right| \leq \left. 1/n \right.$, we obtain

where the final inequality uses the concentration result in Lemma 5.1. ‣ 5.1 Proof of Theorem 3.3 ‣ 5 Proofs ‣ Concentration bounds for CVaR estimation: The cases of light-tailed and heavy-tailed distributions") to obtain the first term, while the second term can be arrived at as in the proof of Theorem 3.3. ‣ 3.2 Concentration bounds ‣ 3 CVaR estimation: Light-tailed case ‣ Concentration bounds for CVaR estimation: The cases of light-tailed and heavy-tailed distributions"). In particular, letting $\epsilon^{\prime} = \frac{\left( {1 - \alpha} \right)\epsilon}{2}$, and using, we have

where the final inequality follows by using DKW inequality for the first term, and VaR concentration result from Lemma 5.1. ‣ 5.1 Proof of Theorem 3.3 ‣ 5 Proofs ‣ Concentration bounds for CVaR estimation: The cases of light-tailed and heavy-tailed distributions") for the second term, together with the fact that ${{\hat{F}}_{n}\left( v_{\alpha} \right)} \leq 1$. Thus,

where $I_{1} = {{\frac{1}{1 - \alpha}{\mathbb{E}}\left\lbrack {X{\mathbb{I}}\left\{ {v_{\alpha} \leq X} \right\}} \right\rbrack} - {\frac{1}{n\left( {1 - \alpha} \right)}{\sum_{i = 1}^{n}{X_{i}{\mathbb{I}}\left\{ {v_{\alpha} \leq X_{i} \leq B_{i}} \right\}}}}}$, and\
$I_{2} = {{\frac{1}{1 - \alpha}{\mathbb{E}}\left\lbrack {v_{\alpha}{\mathbb{I}}\left\{ {v_{\alpha} \leq X} \right\}} \right\rbrack} - {\frac{1}{n\left( {1 - \alpha} \right)}{\sum_{i = 1}^{n}{v_{\alpha}{\mathbb{I}}\left\{ {v_{\alpha} \leq X_{i} \leq B_{i}} \right\}}}}}$. We bound the $I_{1}$ term, using a technique from, as follows:

where we have used the fact that ${{\mathbb{E}}\left( X^{p} \right)} \geq {B^{p - 1}{\mathbb{E}}\left\lbrack {X{\mathbb{I}}\left\{ {X > B} \right\}} \right\rbrack}$ to handle the first term in, and Bernstein's inequality to bound the second term there.

Along similar lines, the term $I_{2}$ is bounded as follows:

where we have used Hoeffding's inequality, and $B_{i}^{p} \geq B_{i}^{p - 1}$for bounding the second term^33^3Note that for a fixed $\delta,$ we can assume $B_{i} > 1$ for all $i$ by taking a $u$ large enough. in, while the first term is bounded using an argument similar to that used in bounding $I_{1}$ term above.

Using $B_{i} = \left( \frac{ui}{\log\left( 1/\delta \right)} \right)^{1/p}$, we have, w.p. $\left( {1 - \delta} \right)$,

Combining the bound above, with that in, we obtain

If the second moment is bounded, i.e., $p = 2$, we have

where $c$ is a distribution-dependent constant. Along similar lines, a concentration bound for the other tail can be obtained. Thus, we have

Similarly, from, for the case when $p \in $, we obtain

where $c^{\prime}$ is a distribution-dependent constant.

## Concluding Remarks

We derived concentration bounds for CVaR estimation, separately considering light-tailed and heavy-tailed distributions. For light-tailed distributions, our concentration bound uses a classical CVaR estimator based on the empirical distribution. For the heavy-tailed case, we employ a truncation based CVaR estimator, and derive a concentration result under a mild bounded-moment assumption. Our concentration bound enjoys exponential decay in the sample size even for heavy-tailed random variables. We highlighted the applicability of the CVaR concentration result by considering a risk-aware best bandit arm selection problem. We proposed an adaptation of the successive rejects algorithm to the setting where the goal is to find an arm with the lowest CVaR. Using the CVaR concentration bound, we established error bounds for the proposed algorithm.
