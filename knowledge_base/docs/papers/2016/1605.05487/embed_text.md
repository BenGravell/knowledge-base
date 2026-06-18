## Introduction

The classical one-sided Chebyshev inequality for a random variable $\overset{\sim}{\xi}$ with mean $\mu$ and variance $\sigma^{2}$ can be represented as

This inequality is sharp. Indeed, for $\gamma \neq \mu$ it is binding under the two-point distribution

In the degenerate case $\gamma = \mu$, the inequality is still sharp because the distributions

have mean $\mu$ and variance $\sigma^{2}$ for every $\kappa > 0$, while ${\lim_{\kappa \uparrow \infty}{{\mathbb{P}}_{\kappa}\left( {\overset{\sim}{\xi} \geq \gamma} \right)}} = 1$. Note, however, that no single distribution with mean $\mu = \gamma$ and variance $\sigma^{2} > 0$ can satisfy ${{\mathbb{P}}\left( {\overset{\sim}{\xi} \geq \gamma} \right)} = 1$.

If we have the extra information that the random variable $\overset{\sim}{\xi}$ is non-negative (and without much loss of generality that $\mu > 0$), then one can strengthen the Chebyshev inequality to

see, e.g.,. The extremal distributions are supported on the non-negative real line if either $\gamma \geq {\mu + \left. \sigma^{2}/\mu \right.} > \mu$ or if $\gamma < \mu$. Thus, they certify the sharpness of in the respective parameter domains. For $\mu \leq \gamma < {\mu + \left. \sigma^{2}/\mu \right.}$ the Chebyshev inequality for non-negative random variables reduces in fact to the classical Markov inequality ${{\mathbb{P}}\left( {\overset{\sim}{\xi} \geq \gamma} \right)} \leq \left. \mu/\gamma \right.$. In this Markov regime, the Chebyshev inequality remains sharp because the distributions

have mean $\mu$ and variance $\sigma^{2}$ for every $\kappa > {\mu + \left. \sigma^{2}/\mu \right.}$, while ${\lim_{\kappa \uparrow \infty}{{\mathbb{P}}_{\kappa}\left( {\overset{\sim}{\xi} \geq \gamma} \right)}} = \left. \mu/\gamma \right.$. From the textbook proof of Markov's inequality it follows that ${\mathbb{P}}^{\star} = {{\left\lbrack {1 - \left. \mu/\gamma \right.} \right\rbrack\delta_{0}} + {\left\lbrack \mu/\gamma \right\rbrack\delta_{\gamma}}}$ is the only distribution on the non-negative reals that has mean $\mu$ and satisfies ${{\mathbb{P}}^{\star}\left( {\overset{\sim}{\xi} \geq \gamma} \right)} = \left. \mu/\gamma \right.$. However, the additional requirement that the variance of $\overset{\sim}{\xi}$ under ${\mathbb{P}}^{\star}$ must equal $\sigma^{2}$ implies $\gamma = {\mu + \left. \sigma^{2}/\mu \right.}$. Thus, for $\mu \leq \gamma < {\mu + \left. \sigma^{2}/\mu \right.}$ there cannot exist any single distribution with ${{\mathbb{P}}\left( {\overset{\sim}{\xi} \geq \gamma} \right)} = \left. \mu/\gamma \right.$.

In the rest of the paper we consider a sequence of $T$ random variables ${\overset{\sim}{\xi}}_{1},{\overset{\sim}{\xi}}_{2},\ldots,{\overset{\sim}{\xi}}_{T}$ and assume that the first two moments of these random variables are known and permutation symmetric. Specifically, assume that all random variables share the same mean $\mu$ and variance $\sigma^{2}$, respectively, while all pairs of mutually distinct random variables share the same correlation coefficient $\rho$. Thus, the mean vector and the covariance matrix of $\overset{\sim}{\mathbf{ξ}} = \left( {\overset{\sim}{\xi}}_{1},\ldots,{\overset{\sim}{\xi}}_{T} \right)^{\intercal}$ are given by

respectively. Throughout the paper we assume that $\sigma > 0$ and ${- \frac{1}{T - 1}} < \rho < 1$. These conditions are necessary and sufficient for the covariance matrix $\mathbf{\Sigma}$ to be strictly positive definite. Note that $\overset{\sim}{\mathbf{ξ}}$ constitutes a weak-sense stationary stochastic process in the sense of.

An elementary calculation reveals that the sum $\sum_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}$ has mean value $T\mu$ and variance $T\sigma^{2}\left( {1 + {\left( {T - 1} \right)\rho}} \right)$. The classical Chebyshev inequality applied to $\sum_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}$ thus implies

This inequality is still sharp due to a projection property of distribution families with compatible first and second moments. Indeed, for any distribution ${\mathbb{P}}_{\zeta}$ of a random variable $\overset{\sim}{\zeta}$ with mean value $T\mu$ and variance $T\sigma^{2}\left( {1 + {\left( {T - 1} \right)\rho}} \right)$ there exists a distribution $\mathbb{P}$ of the random vector $\overset{\sim}{\mathbf{ξ}}$ with mean vector $\mathbf{μ}$ and covariance matrix $\mathbf{\Sigma}$ such that ${\mathbb{P}}_{\zeta}$ coincides with the marginal distribution of $\sum_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}$ under $\mathbb{P}$, that is, ${{\mathbb{P}}_{\zeta}\left( {\overset{\sim}{\zeta} \in B} \right)} = {{\mathbb{P}}\left( {{\sum_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \in B} \right)}$ for every Borel set $B \subseteq {\mathbb{R}}$. The extremal distributions certifying the sharpness of can therefore be used to construct multivariate extremal distributions of $\overset{\sim}{\mathbf{ξ}}$ certifying the sharpness of. This result may be unexpected. Indeed, if ${\overset{\sim}{\xi}}_{1},\ldots,{\overset{\sim}{\xi}}_{T}$ are independent and identically distributed, then, by the central limit theorem, their sum is approximately normally distributed with mean $T\mu$ and variance $T\sigma^{2}$. In contrast, if ${\overset{\sim}{\xi}}_{1},\ldots,{\overset{\sim}{\xi}}_{T}$ are only known to be uncorrelated with a common mean and variance (but not necessarily independent and identically distributed), then, by the projection theorem, their sum may follow any distribution with mean $T\mu$ and variance $T\sigma^{2}$.

Assume now that ${\overset{\sim}{\xi}}_{t}$ is non-negative for every $t = {1,\ldots,T}$ (and without much loss of generality that $\mu > 0$). As we will prove in Proposition 2.1 ‣ 2 Optimization Perspective on Chebyshev Inequalities ‣ Chebyshev Inequalities for Products of Random Variables") below, a distribution $\mathbb{P}$ supported on ${\mathbb{R}}_{+}^{T}$ with mean vector $\mathbf{μ}$ and covariance matrix $\mathbf{\Sigma}$ as given in exists iff ${\mu^{2} + {\rho\sigma^{2}}} \geq 0$. We will assume that this condition holds throughout the rest of the paper. In this setting, the generalized Chebyshev inequality applied to the non-negative random variable $\sum_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}$ implies

Even though the multivariate extension of the univariate Chebyshev inequality can still be shown to be sharp, we are not aware of an elementary proof; see Theorem 6.3 ‣ 6 Extensions ‣ Chebyshev Inequalities for Products of Random Variables") below.

In this paper we aim to derive Chebyshev inequalities for products of non-negative random variables. Specifically, we will derive sharp upper bounds on the left and right tail probabilities ${\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \leq \gamma} \right)$ and ${\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \geq \gamma} \right)$, respectively. Products of random variables frequently arise in physics, statistics, finance, number theory and many other branches of science. Indeed, they are at the heart of stochastic models of many complex phenomena. When rocks are crushed, for example, the size of a fragment is multiplied by a random factor (that is smaller than 1) in every single breakup event. Similar multiplicative phenomena explain the distribution of body weights, stock prices, the sizes of biological populations, income, rainfall etc..

Note that the stochastic process $\overset{\sim}{\mathbf{π}} = \left\{ {\overset{\sim}{\pi}}_{T} \right\}_{T \in {\mathbb{N}}}$ defined through ${\overset{\sim}{\pi}}_{T} = {\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}}$ can be interpreted as a geometric random walk driven by the weak-sense stationary process $\overset{\sim}{\mathbf{ξ}} = \left\{ {\overset{\sim}{\xi}}_{t} \right\}_{t \in {\mathbb{N}}}$. Chebyshev inequalities for the products of the ${\overset{\sim}{\xi}}_{t}$ thus provide tight bounds on the quantiles of a geometric random walk when there is limited distributional information. Consequently, they are potentially relevant for the many applications in economics and operations research, where geometric Brownian motions are traditionally used to model the prices of assets. An improved understanding of weak-sense geometric random walks may also stimulate new research directions in distributionally robust optimziation and optimal uncertainty quantification.

### Remark 1.1 (Chebyshev in Log-Space)

It seems natural to reduce Chebyshev inequalities for products of non-negative random variables to Chebyshev inequalities for their logarithms. Assume thus that the first two moments of the logarithmic random variables ${\overset{\sim}{\eta}}_{t} = {\log{({\overset{\sim}{\xi}}_{t})}}$, $1,\ldots,T$, are known and permutation symmetric. Specifically, denote by $\mu_{\eta}$, $\sigma_{\eta}^{2}$ and $\rho_{\eta}$ the mean, variance and correlation coefficient in log-space. Then, the Chebyshev inequality for sums implies

Note that (7 ‣ 1 Introduction ‣ Chebyshev Inequalities for Products of Random Variables")) is sharp because is sharp. However, there is no one-to-one correspondence between the moments of the original and the logarithmic random variables. Even worse, it is possible that $\mu$ is finite while $\mu_{\eta} = {- \infty}$ (e.g., if $\xi_{t} = 0$ with positive probability), or that $\mu_{\eta}$ is finite while $\mu = {+ \infty}$ (e.g., if ${\overset{\sim}{\xi}}_{t}$ follows a Pareto distribution with unit shape parameter). In this work we focus on the case where the ${\overset{\sim}{\xi}}_{t}$ have known finite first and second moments, and we explicitly allow the event ${\overset{\sim}{\xi}}_{t} = 0$ to have positive probability. This assumption can be crucial for truthfully capturing the bankruptcy risks in financial applications, for instance.

The starting point of this paper is the intriguing observation that modern optimization theory provides powerful tools for constructing and analyzing probability inequalities. Assume for instance that we aim to find a sharp probability inequality for a target event characterized through finitely many polynomial inequalities on a random vector $\overset{\sim}{\mathbf{ξ}}$. Assume further that the desired inequality should hold for all distributions of $\overset{\sim}{\mathbf{ξ}}$ satisfying finitely many polynomial support and moment constraints. In the special case of the Chebyshev inequality, the target event corresponds to the set $\left\{ {\xi \in {\mathbb{R}}}:{\xi \geq \gamma} \right\}$, while the relevant distribution family corresponds to the class of all distributions on $\mathbb{R}$ with mean $\mu$ and variance $\sigma^{2}$. Constructing the desired probability inequality is thus tantamount to maximizing the probability of the target event over the given distribution family. This leads to a generalized moment problem over probability measures. Under a mild regularity condition, this moment problem admits a strong dual linear program subject to polynomially parameterized semi-infinite constraints. A key insight of is that this dual problem can be approximated systematically by tractable semidefinite programs. The resulting approximations are safe (i.e., they are guaranteed to provide upper bounds on the probability of the semialgebraic event). Moreover, these approximations are always tight in the univariate case but generically loose in the multivariate setting.

Stronger statements are available for probability inequalities that rely exclusively on first- and second-order moments. Specifically, if the support of the random vector $\overset{\sim}{\mathbf{ξ}}$ is unrestricted, the best upper bound on the probability of a convex target event is given by $\left. 1/\left( {1 + d^{2}} \right) \right.$, where $d$ represents the distance of the target event from the mean vector of $\overset{\sim}{\mathbf{ξ}}$ under the Mahalanobis norm induced by the covariance matrix of $\overset{\sim}{\mathbf{ξ}}$. More generally, if the target event constitutes a union of finitely many convex sets, over each of which convex quadratic optimization problems can be solved in polynomial time, then the best Chebyshev bound can be computed by an efficient algorithm reminiscent of the ellipsoid method of convex optimization. Recently it has been observed that if the target event is defined by quadratic inequalities, the best Chebyshev bound coincides exactly with the optimal value of a single tractable semidefinite program. In spite of these encouraging results, the computation of Chebyshev bounds becomes hard in the presence of support constraints. Specifically, if $\overset{\sim}{\mathbf{ξ}}$ is supported on the non-negative orthant, it is already NP-hard to find sharp Chebyshev bounds for convex polyhedral target events.

For a random vector $\overset{\sim}{\mathbf{ξ}}$ with zero mean and unrestricted support, the above methods have been used to derive a sharp Chebyshev bound on ${\mathbb{P}}\left( {{{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \geq 1},{{\overset{\sim}{\xi}}_{t} > {0{\forall t}}}} \right)$, which is expressed in terms of the solution of a tractable convex program. As the ${\overset{\sim}{\xi}}_{t}$ are allowed to adopt negative values, however, we believe that the practical relevance of this bound is limited. In this paper we aim to derive sharp Chebyshev bounds on ${\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \geq \gamma} \right)$ and ${\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \leq \gamma} \right)$ under the explicit assumption that $\overset{\sim}{\mathbf{ξ}}$ is supported on the non-negative orthant. Note that the second target event $\left\{ {{\mathbf{ξ}} \in {\mathbb{R}}_{+}^{T}}:{{\prod_{t = 1}^{T}\xi_{t}} \leq \gamma} \right\}$ is neither convex nor representable as a finite union of convex sets, nor representable through finitely many quadratic constraints in $\mathbf{ξ}$. Thus, none of the existing techniques could be used to bound its probability even if there were no support constraints. As support constraints generically lead to intractability, we focus here on the special case where the first- and second-order moments are permutation-symmetric.

The main results of this paper can be summarized as follows.

If the distribution $\mathbb{P}$ of the non-negative random variables has mean $\mathbf{μ}$ and covariance matrix $\mathbf{\Sigma}$ as given in, then the sharp upper Chebyshev bounds on ${\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \geq \gamma} \right)$ and ${\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \leq \gamma} \right)$ can both be expressed as the optimal values of explicit semidefinite programs, which are amenable to efficient numerical solution via interior point algorithms.

If the distribution $\mathbb{P}$ of the non-negative random variables has mean $\mathbf{μ}$ and a covariance matrix bounded above by $\mathbf{\Sigma}$ in a positive semidefinite sense, then we obtain an explicit analytical formula for the sharp upper Chebyshev bound on ${\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \geq \gamma} \right)$.

The Chebyshev bound in (ii) coincides with the corresponding bound in (i) for all values of $\gamma$ that are either sufficiently small or sufficiently large. For intermediate values of $\gamma$ the numerical bound in (i) may be strictly smaller than the analytical bound in (ii).

If the distribution $\mathbb{P}$ of the non-negative random variables has mean $\mathbf{μ}$ and a covariance matrix bounded above by $\mathbf{\Sigma}$ in a positive semidefinite sense, then the sharp upper Chebyshev bound on ${\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \leq \gamma} \right)$ coincides with the corresponding numerical bound in (i). Thus, there is a distribution that makes this bound sharp and has covariance matrix $\mathbf{\Sigma}$.

The Chebyshev bound in (iv) reduces to the trivial bound $1$ for every $\gamma > 0$ if $T$ exceeds an explicit threshold $T_{0}$. Thus, in the worst case, the weak-sense geometric random walk $\overset{\sim}{\mathbf{π}} = \left\{ {\overset{\sim}{\pi}}_{T} \right\}_{T \in {\mathbb{N}}}$ defined through ${\overset{\sim}{\pi}}_{T} = {\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}}$ is absorbed at $0$ with certainty if $T \geq T_{0}$.

The techniques devised for constructing Chebyshev bounds for products of random variables can also be used to derive Chebyshev bounds on sums, maxima and minima (and possibly other permutation-symmetric functionals) of non-negative random variables.

The rest of the paper is structured as follows. In Section 2 we formalize the connection between probability inequalities and convex optimization. Left- and right-sided Chebyshev inequalities for products of random variables are then derived in Sections 3 and 4, respectively, while generalized Chebyshev inequalities that account for imprecise knowledge of the covariances are discussed in Section 5. Chebyshev inequalities for other permutation-symmetric functionals of the random variables are presented in Section 6, and examples are given in Section 7.

### Notation

The symbol $\mathbb{I}$ stands for the identity matrix, $\mathbf{1}$ for the vector of all ones, and $\mathbf{e}_{i}$ for the $i$-th standard basis vector. Their dimensions will always be clear from the context. The space of symmetric $T \times T$ matrices is denoted by ${\mathbb{S}}^{T}$, and its subset of all positive (negative) semidefinite matrices is denoted by ${\mathbb{S}}_{+}^{T}$. For ${{\mathbf{A}},{\mathbf{B}}} \in {\mathbb{S}}^{T}$, the statements ${\mathbf{A}} \succeq {\mathbf{B}}$ and ${\mathbf{B}} \preceq {\mathbf{A}}$ both mean that ${{\mathbf{A}} - {\mathbf{B}}} \in {\mathbb{S}}_{+}^{T}$. The indicator function $1_{\mathcal{E}}$ of a logical statement $\mathcal{E}$ is defined through $1_{\mathcal{E}} = 1$ if $\mathcal{E}$ holds true; $= 0$ otherwise. Random variables are denoted by tilde signs, while their realizations are denoted by the same symbols without tildes. The Dirac distribution concentrating unit mass at $\mathbf{ξ}$ is denoted by $\delta_{\mathbf{ξ}}$. For any closed set $\mathcal{S} \subseteq {\mathbb{R}}^{T}$, we let $\mathcal{M}_{+}(\mathcal{S})$ be the cone of all non-negative Borel measures supported on $\mathcal{S}$.

## Optimization Perspective on Chebyshev Inequalities

To analyze probability bounds using tools from optimization, we first introduce an ambiguity set $\mathcal{P}$, that is, a family of distributions for which the desired probability bound should hold. In this paper we mainly focus on the ambiguity set of all distributions supported on ${\mathbb{R}}_{+}^{T}$ that share the permutation-symmetric mean and covariance matrix defined in, that is, we set

We highlight that $\mathcal{P}$ is characterized by only four parameters: $T,\mu,\sigma,\rho$. Without much loss of generality, we assume henceforth that $\mu > 0$, $\sigma > 0$ and ${- \frac{1}{T - 1}} < \rho < 1$. The last two conditions are equivalent to $\mathbf{\Sigma} \succ \mathbf{0}$. To rule out trivial special cases, we further restrict attention to $T \geq 2$. However, all of these conditions do not yet guarantee that $\mathcal{P}$ is non-empty. Proposition 2.1 ‣ 2 Optimization Perspective on Chebyshev Inequalities ‣ Chebyshev Inequalities for Products of Random Variables") below provides a necessary and sufficient condition for the non-emptiness of $\mathcal{P}$.

### Proposition 2.1 (Non-emptiness of $\mathcal{P}$)

The ambiguity set $\mathcal{P}$ is non-empty iff ${\mu^{2} + {\rho\sigma^{2}}} \geq 0$.

If $\mathcal{P}$ is non-empty, then any ${\mathbb{P}} \in \mathcal{P}$ satisfies

where the equivalences follow from the definition of $\mathbf{\Sigma}$ and the assumption that $\rho < 1$.

Assume now that ${\mu^{2} + {\rho\sigma^{2}}} \geq 0$. We show that $\mathcal{P}$ contains a discrete distribution $\mathbb{P}$ satisfying

for $x \geq y \geq 0$, $z \geq 0$ and $p \in \lbrack 0,1\rbrack$. For this distribution to be contained in $\mathcal{P}$, it must also satisfy the following moment conditions:

${\mathbb{E}}_{\mathbb{P}}\left\lbrack \overset{\sim}{\mathbf{ξ}} \right\rbrack = {\mathbf{μ}}\mspace{92mu}\Longleftrightarrow\frac{p}{T}\left( x + (T - 1)y \right) + (1 - p)z = \mu$;

${\mathbb{E}}_{\mathbb{P}}\left\lbrack \overset{\sim}{\mathbf{ξ}}\overset{\sim}{\mathbf{ξ}}{}_{}^{} \right. = \mathbf{\Sigma} + {\mathbf{μ}}{\mathbf{μ}}^{\intercal}\Longleftrightarrow\frac{p}{T}\left( x^{2} + (T - 1)y^{2} \right) + (1 - p)z^{2} = \mu^{2} + \sigma^{2}$,\
a ${{\frac{p}{T}\left( {{2xy} + {\left( {T - 2} \right)y^{2}}} \right)} + {\left( {1 - p} \right)z^{2}}} = {\mu^{2} + {\rho\sigma^{2}}}$.

To construct $\mathbb{P}$, it is notationally convenient to perform the change of variables $m_{1}\leftarrow{\frac{1}{T}\left( {x + {\left( {T - 1} \right)y}} \right)}$ and $m_{2}\leftarrow{\frac{1}{T}\left( {x^{2} + {\left( {T - 1} \right)y^{2}}} \right)}$. For a given $\left( m_{1},m_{2} \right)$, we can then recover $(x,y)$ via

Note that the correspondence between $(x,y)$ and $\left( m_{1},m_{2} \right)$ is one-to-one and onto over $\left\{ {(x,y) \in {\mathbb{R}}_{+}^{2}}:{x \geq y} \right\}$ and $\left\{ {\left( m_{1},m_{2} \right) \in {\mathbb{R}}_{+}^{2}}:{m_{1}^{2} \leq m_{2} \leq {Tm_{1}^{2}}} \right\}$. Now, for $\mathbb{P}$ to be in $\mathcal{P}$, we require that

${\mathbb{E}}_{\mathbb{P}}\left\lbrack \overset{\sim}{\mathbf{ξ}} \right\rbrack = {\mathbf{μ}}\mspace{92mu}\Longleftrightarrow pm_{1} + (1 - p)z = \mu$;

${\mathbb{E}}_{\mathbb{P}}\left\lbrack \overset{\sim}{\mathbf{ξ}}\overset{\sim}{\mathbf{ξ}}{}_{}^{} \right. = \mathbf{\Sigma} + {\mathbf{μ}}{\mathbf{μ}}^{\intercal}\Longleftrightarrow pm_{2} + (1 - p)z^{2} = \mu^{2} + \sigma^{2}$,\

In the remainder of the proof, we thus need to show that there is ${m_{1},m_{2},z} \geq 0$, $m_{1}^{2} \leq m_{2} \leq {Tm_{1}^{2}}$, and $p \in \lbrack 0,1\rbrack$ satisfying (i') and (ii'). To this end, consider the choice

which satisfies $p \in \lbrack 0,1\rbrack$ by construction, as well as

Note that the terms inside the square roots are non-negative since $\rho > {- \left. 1/\left( {T - 1} \right) \right.}$.

### Step 1

We show that ${m_{1},m_{2},z} \geq 0$. The non-negativity of $m_{1}$ and $m_{2}$ holds by construction. To check that $z \geq 0$, we distinguish the cases $\rho > 0$, $\rho = 0$ and $\rho < 0$. For $\rho > 0$, we obtain $z = 0$ for $p = \frac{T\mu^{2}}{{T\mu^{2}} + {\left( {1 + {\left( {T - 1} \right)\rho}} \right)\sigma^{2}}}$. Since the square root term in the expression for $z$ is increasing in $p$, we thus conclude that $z \geq 0$. The case where $\rho = 0$ is analogous since $\frac{T\mu^{2}}{{T\mu^{2}} + \sigma^{2}} = \frac{T\mu^{2}}{{T\mu^{2}} + {\left( {1 + {\left( {T - 1} \right)\rho}} \right)\sigma^{2}}}$ for $\rho = 0$. For $\rho < 0$, on the other hand, we obtain $z = {\mu - {\sigma\sqrt{- \rho}}}$ for our choice of $p$. The resulting $z$ is thus non-negative due to the assumption that ${\mu^{2} + {\rho\sigma^{2}}} \geq 0$.

### Step 2

To check that $m_{1}^{2} \leq m_{2} \leq {Tm_{1}^{2}}$, we first use the definition of $m_{2}$ and the assumption that $\rho < 1$ to verify that $m_{1}^{2} \leq m_{2}$. The other inequality holds if and only if

where the first and second equivalence follow from the definitions of $m_{2}$ and $m_{1}$, respectively. We now show that the last inequality holds by distinguishing the cases $\rho > 0$, $\rho = 0$ and $\rho < 0$.

For $\rho > 0$, we observe that the expression $\sqrt{\left( {1 + {\left( {T - 1} \right)\rho}} \right)\left( {1 - p} \right)} - \sqrt{1 - \rho}$ in evaluates to 0 for $p = \frac{T\rho}{1 + {\left( {T - 1} \right)\rho}}$ and that it is decreasing in $p$. Since ${\mu\sqrt{pT}} \geq 0$ by construction, we thus conclude that the last inequality in holds, and hence $m_{2} \leq {Tm_{1}^{2}}$ when $\rho \geq 0$. In combination with and, the above inequality ensures that $m_{2} \leq {Tm_{1}^{2}}$.

For $\rho = 0$, equation simplifies to

where the two implications follow from algebraic manipulations and the fact that $\sqrt{p} \geq \frac{1 - \sqrt{1 - p}}{\sqrt{p}}$ for $p \in \lbrack 0,1\rbrack$, respectively. One readily verifies that the last inequality is satisfied by $p = \frac{T\mu^{2}}{{T\mu^{2}} + \sigma^{2}}$.

For $\rho < 0$, substituting $p$ in with its definition from yields

where the equalities follow from direct calculations and the inequality holds since ${\mu^{2} + {\rho\sigma^{2}}} \geq 0$. We thus conclude that $m_{2} \leq {Tm_{1}^{2}}$ whenever $\rho < 0$ as postulated.

### Step 3

We show that our choice of $m_{1},m_{2}$ and $z$ meets the requirements (i') and (ii'), regardless of the value of $p$. First, a direct calculation shows that requirement (i') follows from the definitions of $m_{1}$ and $z$. Next, the first requirement in (ii') follows from

where the first equality holds since the requirement (i') is met, and the fourth equality follows from the definitions of $m_{1}$, $m_{2}$ and $z$.

Finally, to prove the second requirement in (ii'), we first observe that

where the second equality follows from the definition of $m_{2}$. Note that the term on the left (right) side of this equality constitutes the difference between the left (right) sides of the requirements in (ii'). The second requirement in (ii') and the claim thus follow.

In order to establish Chebyshev bounds for products of random variables, we will formulate generalized moment problems that optimize over the probability measures in the ambiguity set $\mathcal{P}$. We can then leverage powerful duality results from convex optimization to reformulate these moment problems as explicit semidefinite programs that are amenable to efficient solution via interior point methods. The *weak duality* principle, which holds true for every optimization problem, states that the optimal value of a (primal) minimization problem is bounded from below by the optimal value of its associated dual (maximization) problem. To establish tight probability bounds, we need to invoke the *strong duality* principle, which states that under certain conditions the optimal values of the primal and dual optimization problems coincide. In our setting, strong duality holds whenever ${\mu^{2} + {\rho\sigma^{2}}} > 0$.

### Theorem 2.1 (Slater Condition)

If ${\mu^{2} + {\rho\sigma^{2}}} > 0$, then the moment vector $(1,{\mathbf{μ}},{\mathbf{\Sigma} + {{\mathbf{μ}}{\mathbf{μ}}^{\intercal}}})$ is contained in the interior of the moment cone $\mathcal{K}$ defined through

We first show that $\mathcal{P}$ contains a distribution of the form where the inequalities $x \geq y \geq 0$, $z \geq 0$ and $p \in \lbrack 0,1\rbrack$ hold *strictly*, as well as ${x + {\left( {T - 1} \right)y}} > {Tz}$ (Step 1). This distribution allows us to show that $\left( 1,{\mathbf{μ}},{\mathbf{\Sigma} + {{\mathbf{μ}}{\mathbf{μ}}^{\intercal}}} \right)$ is in the relative interior of $\mathcal{K}_{1} = {\mathcal{K} \cap \left( {\left\{ 1 \right\} \times {\mathbb{R}}_{+}^{T} \times {\mathbb{S}}_{+}^{T}} \right)}$ (Step 2), from which the result follows directly by re-scaling the measures in $\mathcal{K}_{1}$ (Step 3).

### Step 1

We distinguish the cases $\rho < 0$ and $\rho \geq 0$. For $\rho < 0$, one readily verifies that the choice of $p$, $x$, $y$ and $z$ in the proof of Proposition 2.1 ‣ 2 Optimization Perspective on Chebyshev Inequalities ‣ Chebyshev Inequalities for Products of Random Variables") satisfies $x > y > 0$, $z > 0$, $p \in $ and ${x + {\left( {T - 1} \right)y}} > {Tz}$ by construction. Moreover, these inequalities are also satisfied strictly for $\rho \geq 0$ if we replace $p$ in with any value from the open interval $(0,p)$.

### Step 2

To prove that $\left( 1,{\mathbf{μ}},{\mathbf{\Sigma} + {{\mathbf{μ}}{\mathbf{μ}}^{\intercal}}} \right) \in {\text{rel}\text{int}\mathcal{K}_{1}}$, we show that all perturbed ambiguity sets

with ${\mathbf{μ}}^{\epsilon} \in {\mathcal{B}_{\epsilon}({\mathbf{μ}})}$ and $\mathbf{\Omega}^{\epsilon} \in {\mathcal{B}_{\epsilon}\left( {\mathbf{\Sigma} + {{\mathbf{μ}}{\mathbf{μ}}^{\intercal}}} \right)}$ are non-empty for sufficiently small $\epsilon$, where $\mathcal{B}_{\epsilon}({\mathbf{x}})$ denotes the $\epsilon$-ball around $\mathbf{x}$ in the respective space. Note that the covariance matrix of any distribution in $\mathcal{P}\left( {\mathbf{μ}}^{\epsilon},\mathbf{\Omega}^{\epsilon} \right)$ is positive definite for small $\epsilon$ since $\mathbf{\Sigma} \succ \mathbf{0}$ and the eigenvalues are continuous functions of the second-order moment matrix. In the following, we construct a discrete distribution ${\mathbb{P}}^{\epsilon} \in {\mathcal{P}\left( {\mathbf{μ}}^{\epsilon},\mathbf{\Omega}^{\epsilon} \right)}$ with

where $p$ is the constant chosen in Step 1. The moment conditions for ${\mathbb{P}}^{\epsilon}$ then simplify to:

${\mathbb{E}}_{{\mathbb{P}}^{\epsilon}}\left\lbrack \overset{\sim}{\mathbf{ξ}} \right\rbrack = {\mathbf{μ}}^{\epsilon}\mspace{37mu}\Longleftrightarrow\frac{p}{T}\sum\limits_{i = 1}^{T}\xi_{t}^{\epsilon,i} + (1 - p)\xi_{t}^{\epsilon,{T + 1}} = \mu_{t}^{\epsilon}\mspace{90mu}\forall t = 1,\ldots,T$;

${\mathbb{E}}_{{\mathbb{P}}^{\epsilon}}\left\lbrack \overset{\sim}{\mathbf{ξ}}\overset{\sim}{\mathbf{ξ}}{}_{}^{} \right. = \mathbf{\Omega}^{\epsilon}\Longleftrightarrow\frac{p}{T}\sum\limits_{i = 1}^{T}\left( \xi_{t}^{\epsilon,i} \right)^{2} + (1 - p)\left( \xi_{t}^{\epsilon,{T + 1}} \right)^{2} = \Omega_{tt}^{\epsilon}\mspace{28mu}\forall t = 1,\ldots,T$,\
a ${{{\frac{p}{T}{\sum\limits_{i = 1}^{T}{\xi_{s}^{\epsilon,i}\xi_{t}^{\epsilon,i}}}} + {\left( {1 - p} \right)\xi_{s}^{\epsilon,{T + 1}}\xi_{t}^{\epsilon,{T + 1}}}} = \Omega_{st}^{\epsilon}}\mspace{33mu}{{\forall 1} \leq s < t \leq T}$.

These moment conditions represent a system of nonlinear equations ${{\mathbf{F}}\left( {\mathbf{μ}}^{\epsilon},\mathbf{\Omega}^{\epsilon};\left\{ {\mathbf{ξ}}^{\epsilon,i} \right\}_{i = 1}^{T + 1} \right)} = \mathbf{0}$ in the moments ${\mathbf{μ}}^{\epsilon}$ and $\mathbf{\Omega}^{\epsilon}$ as well as the atoms ${\mathbf{ξ}}^{\epsilon,i}$, $i = {1,\ldots,{T + 1}}$, of the distribution ${\mathbb{P}}^{\epsilon}$. From Step 1 we know that ${{\mathbf{F}}\left( {\mathbf{μ}},{\mathbf{\Sigma} + {{\mathbf{μ}}{\mathbf{μ}}^{\intercal}}};\left\{ {\mathbf{ξ}}^{i} \right\}_{i = 1}^{T + 1} \right)} = \mathbf{0}$ for ${\mathbf{ξ}}^{i} = {{y\mathbf{1}} + {\left( {x - y} \right)\mathbf{e}_{i}}}$, $i = {1,\ldots,T}$, ${\mathbf{ξ}}^{T + 1} = {z\mathbf{1}}$ and for some ${x,y,z} \in {\mathbb{R}}_{+}$ satisfying $x > y > 0$, $z > 0$ and ${x + {\left( {T - 1} \right)y}} > {Tz}$. Moreover, the implicit function theorem proves the existence of continuously differentiable functions ${\mathbf{g}}^{i}:{{{\mathbb{R}}_{+}^{T} \times {\mathbb{S}}_{+}^{T}}\rightarrow{\mathbb{R}}^{T}}$, $i = {1,\ldots,{T + 1}}$, such that ${{\mathbf{F}}\left( {\mathbf{μ}}^{\epsilon},\mathbf{\Omega}^{\epsilon};\left\{ {{\mathbf{g}}^{i}\left( {\mathbf{μ}}^{\epsilon},\mathbf{\Omega}^{\epsilon} \right)} \right\}_{i = 1}^{T + 1} \right)} = \mathbf{0}$ for all ${\mathbf{μ}}^{\epsilon} \in {\mathcal{B}_{\epsilon}({\mathbf{μ}})}$ and $\mathbf{\Omega}^{\epsilon} \in {\mathcal{B}_{\epsilon}\left( {\mathbf{\Sigma} + {{\mathbf{μ}}{\mathbf{μ}}^{\intercal}}} \right)}$, provided that $\epsilon$ is sufficiently small, $\mathbf{F}$ is continuously differentiable, and the Jacobian of $\mathbf{F}$ with respect to ${\mathbf{ξ}}^{\epsilon,i}$ has full row rank at $\left( {\mathbf{μ}}^{\epsilon},\mathbf{\Omega}^{\epsilon},\left\{ {\mathbf{ξ}}^{\epsilon,i} \right\}_{i = 1}^{T + 1} \right) = \left( {\mathbf{μ}},{\mathbf{\Sigma} + {{\mathbf{μ}}{\mathbf{μ}}^{\intercal}}},\left\{ {\mathbf{ξ}}^{i} \right\}_{i = 1}^{T + 1} \right)$. Thus, the functions ${\mathbf{g}}^{i}$ allow us to construct distributions of the form that satisfy the moment conditions of the perturbed ambiguity sets $\mathcal{P}\left( {\mathbf{μ}}^{\epsilon},\mathbf{\Omega}^{\epsilon} \right)$ for all ${\mathbf{μ}}^{\epsilon} \in {\mathcal{B}_{\epsilon}({\mathbf{μ}})}$ and $\mathbf{\Omega}^{\epsilon} \in {\mathcal{B}_{\epsilon}\left( {\mathbf{\Sigma} + {{\mathbf{μ}}{\mathbf{μ}}^{\intercal}}} \right)}$. Since each ${\mathbf{g}}^{i}$ is continuous, we have ${{\mathbf{g}}^{i}\left( {\mathbf{μ}}^{\epsilon},\mathbf{\Omega}^{\epsilon} \right)} > \mathbf{0}$ for all ${\mathbf{μ}}^{\epsilon} \in {\mathcal{B}_{\epsilon}({\mathbf{μ}})}$ and $\mathbf{\Omega}^{\epsilon} \in {\mathcal{B}_{\epsilon}\left( {\mathbf{\Sigma} + {{\mathbf{μ}}{\mathbf{μ}}^{\intercal}}} \right)}$ when $\epsilon$ is sufficiently small, that is, the support of ${\mathbb{P}}^{\epsilon}$ is contained in ${\mathbb{R}}_{+}^{T}$, and thus ${\mathbb{P}}^{\epsilon}$ is indeed contained in $\mathcal{P}\left( {\mathbf{μ}}^{\epsilon},\mathbf{\Omega}^{\epsilon} \right)$.

The moment function $\mathbf{F}$ is continuously differentiable by construction. To apply the implicit function theorem, we therefore only need to show that the Jacobian $\mathbf{J}$ of $\mathbf{F}$ with respect to ${\mathbf{ξ}}^{\epsilon,1}$,..., ${\mathbf{ξ}}^{\epsilon,{T + 1}}$ has full row rank at $\left( {\mathbf{μ}}^{\epsilon},\mathbf{\Omega}^{\epsilon},\left\{ {\mathbf{ξ}}^{\epsilon,i} \right\}_{i = 1}^{T + 1} \right) = \left( {\mathbf{μ}},{\mathbf{\Sigma} + {{\mathbf{μ}}{\mathbf{μ}}^{\intercal}}},\left\{ {\mathbf{ξ}}^{i} \right\}_{i = 1}^{T + 1} \right)$. For ease of exposition, we divide the first $T^{2}$ and the last $T$ columns of $\mathbf{J}$ by $\frac{p}{T}$ and $1 - p$, respectively, and we divide the rows corresponding to the first requirement in (ii) by 2. We then obtain

where for $i = {1,\ldots,T}$, the matrix $\mathbf{C}^{i} \in {\mathbb{R}}^{{(\binom{T}{2})} \times T}$ satisfies

Here, the indices $s$ and $t$, $1 \leq s < t \leq T$, encode the row and the index $j$ refers to the column of $\mathbf{C}^{i}$, respectively. The matrix $\mathbf{C}^{T + 1}$ is defined analogously with $x$ and $y$ replaced by $z$.

Consider the linear combination $\left( {\mathbf{m}}^{\intercal},{\mathbf{v}}^{\intercal},{\mathbf{c}}^{\intercal} \right)\mathbf{J}$ of all rows of $\mathbf{J}$ with the coefficients $m_{t}$ $\left( {t = {1,\ldots,T}} \right)$ for the first block of $T$ rows, $v_{t}$ $\left( {t = {1,\ldots,T}} \right)$ for the second block of $T$ rows, and $c_{st}$ for the third block of $\binom{T}{2}$ rows. For notational convenience, we define $c_{st} = c_{ts}$ for $s > t$. To prove that $\mathbf{J}$ has full row rank, we need to show that $\left( {\mathbf{m}}^{\intercal},{\mathbf{v}}^{\intercal},{\mathbf{c}}^{\intercal} \right)\mathbf{J}$ evaluates to $\mathbf{0}^{\intercal}$ only if $\mathbf{m}$, $\mathbf{v}$ and $\mathbf{c}$ vanish. To this end, consider the first and the $\left( {T + 1} \right)$th element (i.e., the first elements of the first two column blocks) of the equation ${\left( {\mathbf{m}}^{\intercal},{\mathbf{v}}^{\intercal},{\mathbf{c}}^{\intercal} \right)\mathbf{J}} = \mathbf{0}^{\intercal}$, which are equivalent to

Subtracting the two equations implies that ${\left( {x - y} \right)\left( {v_{1} - c_{12}} \right)} = 0$, which in turn yields $v_{1} = c_{12}$ since $x \neq y$. Generalizing this observation to the $t$th columns in each pair of column blocks $s$ and $t$, we find that all $v_{t}$ and $c_{st}$ must be equal to a single variable $v$. Next, consider the $\left( {T^{2} + 1} \right)$th and $\left( {T^{2} + 2} \right)$th columns (i.e., the first two elements of the last column block) of the equation ${\left( {\mathbf{m}}^{\intercal},{\mathbf{v}}^{\intercal},{\mathbf{c}}^{\intercal} \right)\mathbf{J}} = \mathbf{0}^{\intercal}$, which are equivalent to

However, since $v_{t} = c_{st} = v$ for all $s$ and $t$, we conclude that $m_{1} = m_{2}$. Again, generalizing this observation to each pair of columns in the last column block, we can identify all $m_{t}$ by a single number $m$. Replacing $v_{t}$ and $c_{st}$ by $v$ and $m_{t}$ by $m$, the previous two equations simplify to

and we conclude that $m = v = 0$ since we established earlier that ${x + {\left( {T - 1} \right)y}} \neq {Tz}$. Hence, the Jacobian $\mathbf{J}$ indeed has full row rank, which concludes Step 2.

### Step 3

We have shown in Step 2 that ${\mathcal{P}\left( {\mathbf{μ}}^{\epsilon},\mathbf{\Omega}^{\epsilon} \right)} \neq \varnothing$ for all ${\mathbf{μ}}^{\epsilon} \in {\mathcal{B}_{\epsilon}({\mathbf{μ}})}$ and $\mathbf{\Omega}^{\epsilon} \in {\mathcal{B}_{\epsilon}\left( {\mathbf{\Sigma} + {{\mathbf{μ}}{\mathbf{μ}}^{\intercal}}} \right)}$, which implies that $\left( 1,{\mathbf{μ}},{\mathbf{\Sigma} + {{\mathbf{μ}}{\mathbf{μ}}^{\intercal}}} \right) \in {\text{rel}\text{int}\mathcal{K}_{1}}$. Since $\left\{ {\lambda\mathcal{K}_{1}}:{\lambda \in {\mathbb{R}}_{+}} \right\} \subseteq \mathcal{K}$, we have ${\lambda\mathcal{P}\left( {\mathbf{μ}}^{\epsilon},\mathbf{\Omega}^{\epsilon} \right)} \subseteq \mathcal{K}$ for all $\lambda \geq 0$. As the moments are linear in the measure, we thus conclude that $\left( 1,{\mathbf{μ}},{\mathbf{\Sigma} + {{\mathbf{μ}}{\mathbf{μ}}^{\intercal}}} \right) \in {\text{int}\mathcal{K}}$ as desired.

Theorem 2.1 ‣ Step 3: ‣ 2 Optimization Perspective on Chebyshev Inequalities ‣ Chebyshev Inequalities for Products of Random Variables") will allow us to use the strong duality theorem of \[27, Proposition 3.4\], which states that a linear optimization problem over the distributions in $\mathcal{P}$ has the same optimal value as its associated dual problem. In the remainder of the paper, we will make extensive use of this insight, and we therefore assume from now on that ${\mu^{2} + {\rho\sigma^{2}}} > 0$.

## Left-Sided Chebyshev Bounds

In this section we study *left-sided Chebyshev bounds* of the form

where the ambiguity set $\mathcal{P}$ is defined in. We begin with the main result of this section.

### Theorem 3.1 (Left-Sided Chebyshev Bound)

Let $\gamma > 0$. For all $T \geq 3$, the left-sided Chebyshev bound $\text{L}{(\gamma)}$ coincides with the optimal objective value of the semidefinite program

where we use the convention that the entries of $\mathbf{p}$, $\mathbf{P}$, $\mathbf{q}$ and $\mathbf{Q}$ are numbered starting from $0$. For $T = 2$, $\text{L}{(\gamma)}$ is given by a variant of (13 ‣ 3 Left-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables")) where the constraints ${p_{2} + q_{1}} = {\alpha - 1}$ and ${p_{T} + q_{T - 1}} = {2{({T - 1})}\gamma_{2}\gamma^{\frac{1}{T - 1}}}$ are combined to ${p_{2} + q_{1}} = {{\alpha - 1} + {2{({T - 1})}\gamma_{2}\gamma^{\frac{1}{T - 1}}}}$.

We first reformulate the maximum probability of the left tail of the product $\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}$ falling below $\gamma$ as the generalized moment problem

This moment problem admits a strong conic dual in the Lagrange multipliers $\alpha \in {\mathbb{R}}$, ${\mathbf{β}} \in {\mathbb{R}}^{T}$ and $\mathbf{\Gamma} \in {\mathbb{S}}^{T}$ corresponding to the normalization, mean and covariance constraints in, respectively, see Theorem 2.1 ‣ Step 3: ‣ 2 Optimization Perspective on Chebyshev Inequalities ‣ Chebyshev Inequalities for Products of Random Variables") and \[27, Proposition 3.4\]. Recalling that ${\mathbf{μ}} = {\mu\mathbf{1}}$ and $\mathbf{\Sigma} = {{\left( {1 - \rho} \right)\sigma^{2}{\mathbb{I}}} + {\rho\sigma^{2}\mathbf{1}\mathbf{1}^{\intercal}}}$, the dual problem can be expressed as

By Lemma 3.1 below, the symmetry of problem implies that we may restrict attention to permutation-symmetric solutions of the form $(\alpha,{\mathbf{β}},\mathbf{\Gamma})$ with ${\mathbf{β}} = {\beta\mathbf{1}}$ and $\mathbf{\Gamma} = {{\gamma_{1}{\mathbb{I}}} + {\gamma_{2}\mathbf{1}\mathbf{1}^{\intercal}}}$ for some ${\beta,\gamma_{1},\gamma_{2}} \in {\mathbb{R}}$. Thus, problem simplifies to

Lemma 3.2 then implies that can be reduced to

By assigning a Lagrange multiplier $\lambda_{1} \geq 0$ to the constraint $s \geq 0$ and using the $\mathcal{S}$-lemma, the first constraint in can be reformulated as the linear matrix inequality

where the first equivalence follows from the observation that a $2 \times 2$-matrix is positive semidefinite iff it has non-negative diagonal elements as well as a non-negative determinant, while the second equivalence uses a well-known reformulation of hyperbolic constraints as second-order cone constraints \[6, p. 197\]. Similarly, the second constraint in holds iff there exists $\lambda_{2} \geq 0$ with

Lemma 3.3 below further allows us to decompose the third constraint in into two simpler semi-infinite constraints.

${{\inf\limits_{s \in {\lbrack 0,{T\gamma^{1/T}}\rbrack}}\alpha} + {\betas} + {\gamma_{2}s^{2}} + {\gamma_{1}\frac{s^{2}}{T}}} \geq 1$ (18a)
$\inf\limits_{s \geq {T\gamma^{1/T}}}\left\{ \alpha + \beta s + \gamma_{2}s^{2} + \gamma_{1}\min\limits_{{\underset{¯}{\xi},\overline{\xi}} \geq 0}\left\{ \underset{¯}{\xi}{}_{}^{}(T - 1)\overline{\xi}{}_{}^{}\underset{¯}{\xi} + (T - 1)\overline{\xi} = s,\underset{¯}{\xi}\overline{\xi}{}_{}^{T - 1}\gamma \right\} \right\} \geq 1$ (18b)

As $s \in \left\lbrack 0,{T\gamma^{1/T}} \right\rbrack$ iff ${s\left( {{T\gamma^{1/T}} - s} \right)} \geq 0$, we can once again use the $\mathcal{S}$-lemma to show that (18a) holds iff there exists $\lambda_{3} \geq 0$ with

Finally, it remains to be shown that (18b) also admits a conic reformulation. To do so, we first argue that one can replace (18b) with

without changing the optimal value of problem. If $\gamma_{1} \geq 0$, then is indeed equivalent to (18b). On the other hand, if $\gamma_{1} < 0$, we find

which means that (18b) is implied by the second semi-infinite constraint in problem. By eliminating $s = {\underset{¯}{\xi} + {\left( {T - 1} \right)\overline{\xi}}}$, the maximization problem on the left hand side of reduces to

Note that the constraint $s \geq {T\gamma^{1/T}}$ has been dropped in the above formulation. This constraint is redundant due to the inequality of arithmetic and geometric means, which implies that

By setting $\kappa = {\underset{¯}{\xi}}^{1/{({T - 1})}}$, we can further replace $\underset{¯}{\xi}$ and $\overline{\xi}$ with $\kappa^{T - 1}$ and $\left. \gamma^{1/{({T - 1})}}/\kappa \right.$, respectively. Using elementary manipulations, one can then show that reduces to

Note that the objective of the maximization problem on the left hand side of constitutes a polynomial of degree $2T$ in $\kappa$ and is therefore representable as ${l(\kappa)} = {\sum_{i = 0}^{2T}{a_{i}\kappa^{i}}}$, where

Here we assumed that $T > 2$. For $T = 2$, the quadratic monomial in $l(\kappa)$ would have the coefficient ${\alpha - 1} + {2\left( {T - 1} \right)\gamma_{2}\gamma^{\frac{1}{T - 1}}}$ instead of $\alpha - 1$. Thus, the case $T = 2$ could be handled via a case distinction, which we omit for the sake of brevity.

Constraint thus requires the polynomial $l(\kappa)$ to be non-negative for all $\kappa \geq 0$. By the Markov-Lukacs Theorem, this is equivalent to postulating that $l(\kappa)$ admits a sum-of-squares representation of the form ${l(\kappa)} = {{p(\kappa)} + {\kappaq(\kappa)}}$, where ${p(\kappa)} = {\sum_{i = 0}^{2T}{p_{i}\kappa^{i}}}$ and ${q(\kappa)} = {\sum_{i = 0}^{{2T} - 2}{q_{i}\kappa^{i}}}$ are sum-of-squares polynomials of degrees $2T$ and ${2T} - 2$, respectively. By matching the coefficients of all monomials, one verifies that the identity ${l(\kappa)} = {{p(\kappa)} + {\kappaq(\kappa)}}$ holds iff

Moreover, by \[23, Theorem 3\], $p(\kappa)$ and $q(\kappa)$ are sum-of-squares polynomials iff there exist positive semidefinite matrices ${\mathbf{P}} \in {\mathbb{S}}_{+}^{T + 1}$ and ${\mathbf{Q}} \in {\mathbb{S}}_{+}^{T}$ such that

Thus, holds iff the conic constraints and are satisfied. The claim now follows by replacing the three semi-infinite constraints in with their explicit conic reformulations.

The proof of Theorem 3.1 ‣ 3 Left-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables") relies on 4 auxiliary lemmas, which we prove next.

### Lemma 3.1

Problem has a permutation symmetric minimizer $\left( \alpha^{\star},{\mathbf{β}}^{\star},\mathbf{\Gamma}^{\star} \right)$ that satisfies ${\mathbf{β}}^{\star} = {\beta^{\star}\mathbf{1}}$ and $\mathbf{\Gamma}^{\star} = {{\gamma_{1}^{\star}{\mathbb{I}}} + {\gamma_{2}^{\star}\mathbf{1}\mathbf{1}^{\intercal}}}$ for some ${\beta^{\star},\gamma_{1}^{\star},\gamma_{2}^{\star}} \in {\mathbb{R}}$.

Let $\mathfrak{P}$ be the set of all permutations of the index set $\left\{ 1,\ldots,T \right\}$. For any $\pi \in {\mathfrak{P}}$ we denote by $\mathbf{P}_{\pi} \in {\mathbb{R}}^{T \times T}$ the permutation matrix defined through $\left( \mathbf{P}_{\pi} \right)_{ij} = 1$ if ${\pi(i)} = j$; $= 0$ otherwise. Let $(\alpha,{\mathbf{β}},\mathbf{\Gamma})$ by any optimal solution to, which exists by \[27, Proposition 3.4\]. We first show that the permuted solution $\left( \alpha_{\pi},{\mathbf{β}}_{\pi},\mathbf{\Gamma}_{\pi} \right) = \left( \alpha,{\mathbf{P}_{\pi}{\mathbf{β}}},{\mathbf{P}_{\pi}\mathbf{\Gamma}\mathbf{P}_{\pi}^{\intercal}} \right)$ is also optimal in. To this end, we observe that

where the first equality follows from the definition of $\alpha_{\pi}$, ${\mathbf{β}}_{\pi}$ and $\mathbf{\Gamma}_{\pi}$, the second equality exploits the cyclicity property of the trace scalar product, and the third equality holds due to the permutation symmetry of $\mathbf{1}$ and the fact that $\mathbf{P}_{\pi}^{\intercal} = \mathbf{P}_{\pi^{- 1}} = \mathbf{P}_{\pi}^{- 1}$. Thus, $\left( \alpha_{\pi},{\mathbf{β}}_{\pi},\mathbf{\Gamma}_{\pi} \right)$ has the same objective value as $(\alpha,{\mathbf{β}},\mathbf{\Gamma})$. To show that $\left( \alpha_{\pi},{\mathbf{β}}_{\pi},\mathbf{\Gamma}_{\pi} \right)$ is feasible in, we note that

where the first equivalence follows from the definition of $\alpha_{\pi}$, ${\mathbf{β}}_{\pi}$ and $\mathbf{\Gamma}_{\pi}$ and because $\mathbf{P}_{\pi}^{\intercal} = \mathbf{P}_{\pi}^{- 1}$, the second equivalence holds because permutations are bijective, and the third equivalence relies on the permutation symmetry of the non-negative orthant. Thus, $\left( \alpha_{\pi},{\mathbf{β}}_{\pi},\mathbf{\Gamma}_{\pi} \right)$ satisfies the semi-infinite constraints in whenever $(\alpha,{\mathbf{β}},\mathbf{\Gamma})$ does. We conclude that $\left( \alpha_{\pi},{\mathbf{β}}_{\pi},\mathbf{\Gamma}_{\pi} \right)$ is feasible and thus optimal in for every $\pi \in {\mathfrak{P}}$.

Due to the convexity of the (semi-infinite) linear program, the equally weighted average $\left( \alpha^{\star},{\mathbf{β}}^{\star},\mathbf{\Gamma}^{\star} \right) = {\frac{1}{T!}\left. \sum{}_{\pi \in {\mathfrak{P}}}\left( \alpha_{\pi},{\mathbf{β}}_{\pi},\mathbf{\Gamma}_{\pi} \right) \right.}$ constitutes another optimal solution. It is now clear that ${\mathbf{P}_{\pi}{\mathbf{β}}^{\star}} = {\mathbf{β}}^{\star}$ and ${\mathbf{P}_{\pi}\mathbf{\Gamma}^{\star}\mathbf{P}_{\pi}^{\intercal}} = \mathbf{\Gamma}^{\star}$ for any $\pi \in {\mathfrak{P}}$ since ${\pi({\mathfrak{P}})} = {\mathfrak{P}}$. Thus, the claim follows.

### Lemma 3.2

For ${\alpha,\beta,\gamma_{1},\gamma_{2},\Delta} \in {\mathbb{R}}$ and ${\underset{¯}{\gamma},\overline{\gamma}} \in {{\mathbb{R}}_{+} \cup {\{\infty\}}}$, $\underset{¯}{\gamma} \leq \overline{\gamma}$, we have

$f_{T}\left( \underset{¯}{\gamma},\overline{\gamma} \right)$ $= \inf\limits_{{\mathbf{ξ}} \geq \mathbf{0}}\left\{ \parallel {\mathbf{ξ}} \parallel_{2}^{2}: \parallel {\mathbf{ξ}} \parallel_{1} = 1,\prod_{t = 1}^{T}\xi_{t} \in \left\lbrack \underset{¯}{\gamma},\overline{\gamma} \right\rbrack \right\}$ (25a)
$\text{and}g_{T}\left( \underset{¯}{\gamma},\overline{\gamma} \right)$ $= \sup\limits_{{\mathbf{ξ}} \geq \mathbf{0}}\left\{ \parallel {\mathbf{ξ}} \parallel_{2}^{2}: \parallel {\mathbf{ξ}} \parallel_{1} = 1,\prod_{t = 1}^{T}\xi_{t} \in \left\lbrack \underset{¯}{\gamma},\overline{\gamma} \right\rbrack \right\}.$ (25b)

Moreover, we have ${f_{T}{(\underset{¯}{\gamma},\infty)}} = {1/T}$ for $\underset{¯}{\gamma} \leq T^{- T}$ and ${g_{T}{(0,\overline{\gamma})}} = 1$ for $\overline{\gamma} \in {{\mathbb{R}}_{+} \cup {\{\infty\}}}$.

Figure 1: The subproblems (25a) (left) and (25b) (right) determine the smallest and the largest spheres centered at the origin that intersect with the hyperplane ∥ξ∥1 = 1 (shaded areas) and the hyperbola ${\prod_{t = 1}^{T}\xi_{t}} = {\overline{\gamma},\underset{¯}{\gamma}}$ (solid lines). The dashed circles represent level sets of the objective function ∥ξ∥22. Both graphs illustrate the case where T = 3.

Figure 1 visualizes the two parametric subproblems (25a) and (25b). Note that both problems are non-convex whenever $\overline{\gamma} < \infty$ as their last constraints are equivalent to $\left( {\prod_{t = 1}^{T}\xi_{t}} \right)^{1/T} \in \left\lbrack {\underset{¯}{\gamma}}^{1/T},{\overline{\gamma}}^{1/T} \right\rbrack$ and because geometric means are concave \[6, § 3.1\]. Moreover, the subproblem (25b) remains non-convex for $\overline{\gamma} = \infty$ since it maximizes a convex objective function.

The first constraint in can be reduced to

by decomposing the maximization over all ${\mathbf{ξ}} \geq \mathbf{0}$ into two nested maximization problems over all $s \geq {T{\underset{¯}{\gamma}}^{1/T}}$ and over all ${\mathbf{ξ}} \geq \mathbf{0}$ with $\left\| {\mathbf{ξ}} \right\|_{1} = s$, respectively. Here, the lower bound on $s$ is owed to the fact that there is ${\mathbf{ξ}} \geq \mathbf{0}$ satisfying $\left\| {\mathbf{ξ}} \right\|_{1} = s$ and ${\prod_{t = 1}^{T}\xi_{t}} \in \left\lbrack \underset{¯}{\gamma},\overline{\gamma} \right\rbrack$ if and only if $s \geq {T{\underset{¯}{\gamma}}^{1/T}}$. A case distinction on the sign of $\gamma_{1}$ shows that constraint holds if and only if

is satisfied. The change of variables ${\mathbf{ξ}}\leftarrow{s{\mathbf{ξ}}}$ shows that this constraint system is equivalent to the second constraint system in. Finally, we have ${f_{T}\left( \underset{¯}{\gamma},\infty \right)} = \left. 1/T \right.$ for $\underset{¯}{\gamma} \leq T^{- T}$ and ${g_{T}\left( 0,\overline{\gamma} \right)} = 1$ for $\overline{\gamma} \in {{\mathbb{R}}_{+} \cup \left\{ \infty \right\}}$ since the inequalities ${\frac{1}{T}\left\| {\mathbf{ξ}} \right\|_{1}^{2}} \leq \left\| {\mathbf{ξ}} \right\|_{2}^{2} \leq \left\| {\mathbf{ξ}} \right\|_{1}^{2}$ are tight for ${\mathbf{ξ}} = \mathbf{1}$ and ${\mathbf{ξ}} = \mathbf{e}_{i}$, respectively.

### Lemma 3.3

For $T \geq 2$, $\underset{¯}{\gamma} = 0$ and $\overline{\gamma} \geq 0$, the optimal value $f_{T}{(0,\overline{\gamma})}$ of (25a) equals

We first observe that the non-convex optimization problem (25a) is bounded below by its relaxation $\min_{{\|{\mathbf{ξ}}\|}_{1} = 1}\left\| {\mathbf{ξ}} \right\|_{2}^{2}$. Note, however, that the optimal solution ${\mathbf{ξ}} = {\frac{1}{T}\mathbf{1}}$ of this relaxation is feasible and thus optimal in (25a) whenever $\overline{\gamma} \geq T^{- T}$. Thus, we have ${f_{T}\left( 0,\overline{\gamma} \right)} = \frac{1}{T}$ for $\overline{\gamma} \geq T^{- T}$. For $0 \leq \overline{\gamma} < T^{- T}$, on the other hand, the product constraint ${\prod_{t = 1}^{T}\xi_{t}} \leq \overline{\gamma}$ must be binding, for otherwise convex combinations of the optimal solution $\mathbf{ξ}$ with $\frac{1}{T}\mathbf{1}$ would improve the objective function of $f_{T}\left( 0,\overline{\gamma} \right)$, which is a contradiction. In summary, we thus find

When $\overline{\gamma} = 0$, the product constraint in the first line of can only be satisfied if $\xi_{t} = 0$ for at least one $t$. By permutation symmetry, we may assume without loss of generality that $\xi_{T} = 0$. Then, the product constraint is automatically satisfied and may be disregarded, implying that the minimization problem in the first line of is solved by $\xi_{1} = \xi_{2} = \cdots = \xi_{T - 1} = \frac{1}{T - 1}$ and $\xi_{T} = 0$. We thus conclude that ${f_{T}} = \frac{1}{T - 1}$ and therefore

We now study the non-convex parametric optimization problem

on the domain $0 < \overline{\gamma} < T^{- T}$. Observe that has a non-empty compact feasible set for any admissible $\overline{\gamma}$ and is therefore solvable. Assigning Lagrange multipliers $a$ and $b$ to the norm and product constraints, respectively, we find that any optimal solution to must satisfy the stationarity conditions

where the equivalence follows from primal feasibility. Note that each $\xi_{t}$ needs to satisfy an identical quadratic equation, which must have two distinct positive real roots^11^1The existence of at least one real root is guaranteed because is solvable and because any optimal solution must satisfy the stationarity conditions. In fact, the stationarity conditions must admit two distinct positive real roots because otherwise ${\mathbf{ξ}} = {\frac{1}{T}\mathbf{1}}$ would be the only conceivable optimal solution, which is impossible for $\overline{\gamma} < T^{- T}$. $\underset{¯}{\xi}$ and $\overline{\xi}$. The roots depend on $a$, $b$ and $\overline{\gamma}$, but this dependence is notationally suppressed to avoid clutter. At optimality, the decision variables $\xi_{1},{\xi_{2}\ldots},\xi_{T}$ can thus be partitioned into two groups, where all variables in the first group are equal to $\underset{¯}{\xi}$, and all variables in the second group are equal to $\overline{\xi}$. This structural insight allows us to simplify problem. Indeed, by permutation symmetry, it is sufficient to consider only solutions that satisfy $\xi_{1} = \cdots = \xi_{k} = \underset{¯}{\xi}$ and $\xi_{k + 1} = \cdots = \xi_{T} = \overline{\xi}$ for some ${\underset{¯}{\xi},\overline{\xi}} > 0$ and for some $k \in \left\{ 1,\ldots,\left\lfloor \frac{T}{2} \right\rfloor \right\}$. Thus, the optimal value of coincides with

where the functions $f_{T,k}:{\left( 0,T^{- T} \right)\rightarrow{\mathbb{R}}}$ for $k = {1,2,\ldots,\left\lfloor \frac{T}{2} \right\rfloor}$ are defined through

By Lemma 3.4 below, the optimal value of is given by $f_{T,1}\left( \overline{\gamma} \right)$. Hence, if we replace the minimization problem in with $f_{T,1}\left( \overline{\gamma} \right)$, we obtain

The statement of the lemma now follows since the minimization problem in the equation above evaluates to $\left. 1/T \right.$ at $\overline{\gamma} = T^{- T}$. Indeed, the minimization problem is bounded below by $\min_{{\|{\mathbf{ξ}}\|}_{1} = 1}\left\| {\mathbf{ξ}} \right\|_{2}^{2}$, and the optimal value $\left. 1/T \right.$ of this bound is achieved by the feasible solution $\underset{¯}{\xi} = \overline{\xi} = \left. 1/T \right.$ of the minimization problem at $\overline{\gamma} = T^{- T}$.

### Lemma 3.4

For $T \geq 2$ and $0 < \overline{\gamma} < T^{- T}$, the optimal value of is given by $f_{T,1}{(\overline{\gamma})}$.

The statement holds trivially true when $\left\lfloor \frac{T}{2} \right\rfloor = 1$, that is, for $T \in \left\{ 2,3 \right\}$. Next, we show that ${f_{4,1}\left( \overline{\gamma} \right)} < {f_{4,2}\left( \overline{\gamma} \right)}$ for any $\overline{\gamma} \in \left( 0,4^{- 4} \right)$. This inequality not only implies that the statement holds true for $T = 4$ but will also be instrumental for proving the statement for $T > 4$.

Fix $\overline{\gamma} \in \left( 0,4^{- 4} \right)$ and note that

where the second equality follows from the substitution $\underset{¯}{\xi}\leftarrow{2\underset{¯}{\xi}}$ and $\overline{\xi}\leftarrow{2\overline{\xi}}$, and the last equality holds because ${f_{2,1}\left( \overline{\gamma} \right)} = {1 - {2\overline{\gamma}}}$ for any $\overline{\gamma} \in \left( 0,2^{- 2} \right)$, which can be verified by direct calculation. Thus, we need to show that ${f_{4,1}\left( \overline{\gamma} \right)} < {\frac{1}{2} - {4\sqrt{\overline{\gamma}}}}$, where

It is therefore sufficient to find $\overline{\xi}^{\star}$ feasible in with

where $\zeta^{\pm} = \left. \left( {3 \pm \sqrt{3 - {48\sqrt{\overline{\gamma}}}}} \right)/12 \right.$ are the roots of $12\left( \overline{\xi}{}_{}^{} \right.^{2} - 6\overline{\xi}{}_{}^{}\left( 1/2 + 4\sqrt{\overline{\gamma}} \right)$. Equivalently, we should demonstrate the existence of some $\overline{\xi}{}_{}^{}\left( \zeta^{-},\zeta^{+} \right)$ with $\left( 1 - 3\overline{\xi}{}_{}^{} \right.\left( \overline{\xi}{}_{}^{} \right.^{3} - \overline{\gamma} = 0$. By the intermediate value theorem, this holds if

But these inequalities are automatically satisfied under the assumption that $\overline{\gamma} \in \left( 0,4^{- 4} \right)$. Indeed, recalling the definition of $\zeta^{-}$ and defining $z^{-} = {{12\zeta^{-}} - 3} = {- \sqrt{3 - {48\sqrt{\overline{\gamma}}}}}$, we have

where the inequality holds because $z^{-} \in \left( {- \sqrt{3}},0 \right)$ for $\overline{\gamma} \in \left( 0,4^{- 4} \right)$. Similarly, defining $z^{+} = {{12\zeta^{+}} - 3} = \sqrt{3 - {48\sqrt{\overline{\gamma}}}}$, we can prove that ${{\left( {1 - {3\zeta^{+}}} \right)\left( \zeta^{+} \right)^{3}} - \overline{\gamma}} < 0$. Thus, we have shown that ${f_{4,1}\left( \overline{\gamma} \right)} < {f_{4,2}\left( \overline{\gamma} \right)}$ for any $\overline{\gamma} \in \left( 0,4^{- 4} \right)$, which establishes the assertion for $T = 4$.

Fix now some $T \geq 5$ and assume for the sake of argument that there exist $k \in \left\{ 2,\ldots,\left\lfloor \frac{T}{2} \right\rfloor \right\}$ and $\overline{\gamma} \in \left( 0,T^{- T} \right)$ with ${f_{T}\left( 0,\overline{\gamma} \right)} = {f_{T,k}\left( \overline{\gamma} \right)} < {f_{T,1}\left( \overline{\gamma} \right)}$. Hence, there are some $\underset{¯}{\xi} > 0$ and $\overline{\xi} > 0$ with $\underset{¯}{\xi} \neq \overline{\xi}$ such that the minimum of $f_{T}\left( 0,\overline{\gamma} \right)$ in is attained by the solution $\xi_{1} = \cdots = \xi_{k} = \underset{¯}{\xi}$ and $\xi_{k + 1} = \cdots = \xi_{T} = \overline{\xi}$. Fixing $\xi_{1},\ldots,\xi_{k - 2}$ and $\xi_{k + 3},\ldots,\xi_{T}$ at their optimal values and optimizing only over the remaining four decision variables in $f_{T}\left( 0,\overline{\gamma} \right)$ yields

Defining the strictly positive constant $c = {1 - {\left( {k - 2} \right)\underset{¯}{\xi}} - {\left( {T - k - 2} \right)\overline{\xi}}} = {{2\underset{¯}{\xi}} + {2\overline{\xi}}}$ and using the substitution $y_{t}\leftarrow\left. \xi_{{k - 2} + t}/c \right.$ for $t = {1,\ldots,4}$ further yields

where the second equality follows from the definition of $f_{4}\left( 0,\overline{\gamma} \right)$ in. By construction, the minimization problem in must be solved by $y_{1} = y_{2} = \underset{¯}{\xi}$ and $y_{3} = y_{4} = \overline{\xi}$. However, this contradicts our previous results. In fact, we know that the solution of $f_{4}\left( 0,\overline{\gamma} \right)$ must have the following properties for $T = 4$. If $\left. \overline{\gamma}/\left\lbrack c^{4}{\underset{¯}{\xi}}^{k - 2}\overline{\xi}{}_{}^{T - k - 2} \right. < 4^{- 4} \right.$, then three out of the four $\xi_{t}$ variables must be equal at optimality. Conversely, if $\left. \overline{\gamma}/\left\lbrack c^{4}{\underset{¯}{\xi}}^{k - 2}\overline{\xi}{}_{}^{T - k - 2} \right. \geq 4^{- 4} \right.$, then all four $\xi_{t}$ variables must be equal. This contradicts our assumption that there exist $k \in \left\{ 2,\ldots,\left\lfloor \frac{T}{2} \right\rfloor \right\}$ and $\overline{\gamma} \in \left( 0,T^{- T} \right)$ with ${f_{T}\left( 0,\overline{\gamma} \right)} = {f_{T,k}\left( \overline{\gamma} \right)} < {f_{T,1}\left( \overline{\gamma} \right)}$. Thus, the assertion holds for all $T > 4$.

We now show that in the worst case, the weak-sense geometric random walk $\overset{\sim}{\mathbf{π}} = \left\{ {\overset{\sim}{\pi}}_{T} \right\}_{T \in {\mathbb{N}}}$ defined through ${\overset{\sim}{\pi}}_{T} = {\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}}$ is absorbed at $0$ with certainty if $T$ exceeds a threshold $T_{0}$.

### Theorem 3.2 (Certainty of Absorption)

For $T > {\frac{\mu^{2} + \sigma^{2}}{{({1 - \rho})}\sigma^{2}} + 1}$ we have ${\text{L}{(\gamma)}} = 1$ for every $\gamma > 0$.

From the proof of Proposition 2.1 ‣ 2 Optimization Perspective on Chebyshev Inequalities ‣ Chebyshev Inequalities for Products of Random Variables") we know that there exists a discrete distribution ${\mathbb{P}}_{0} = \left. \sum{}_{k \in \mathcal{K}}{p_{k}\delta_{{\mathbf{ξ}}^{k}}} \right. \in \mathcal{P}$ with scenarios ${\mathbf{ξ}}^{k}$ and associated probabilities $p_{k} > 0$, where $k$ ranges over a finite index set $\mathcal{K}$ of cardinality $T + 1$. By the permutation symmetry, any discrete distribution of the form ${\mathbb{P}}_{0} \in \mathcal{P}$ can be used to construct a corresponding symmetric distribution

which is also an element of $\mathcal{P}$. Here, $\mathfrak{P}$ denotes the group of all permutations of $\left\{ 1,\ldots,T \right\}$, while $\mathbf{P}_{\pi} \in {\mathbb{R}}^{T \times T}$ denotes the permutation matrix induced by $\pi \in {\mathfrak{P}}$; see also Lemma 3.1. Next, we define $m_{1}^{k} = {\frac{1}{T}{\sum_{t = 1}^{T}\xi_{t}^{k}}}$ and $m_{2}^{k} = {\frac{1}{T}{\sum_{t = 1}^{T}\left( \xi_{t}^{k} \right)^{2}}}$ as the arithmetic and quadratic means of scenario ${\mathbf{ξ}}^{k}$, respectively. It turns out that the first two moments of $\overset{\sim}{\mathbf{ξ}}$ can be expressed in terms of $m_{1}^{k}$ and $m_{2}^{k}$. Note, for instance, that for any $t \neq s$ we have

where the first equality follows from the definition of $\mathbb{P}$ and because the $t$-th component of $\mathbf{P}_{\pi}{\mathbf{ξ}}^{(k)}$ is given by $\xi_{\pi{(t)}}^{k}$, while the third equality holds because there are $\left( {T - 2} \right)!$ permutations that map $s$ to $r$ and $t$ to any fixed index different from $r$. Similarly, one can show that

The moment conditions in the definition of $\mathcal{P}$ thus reduce to

$\sum\limits_{k \in \mathcal{K}}p_{k}$ $= 1$ (37a)
$\sum\limits_{k \in \mathcal{K}}{p_{k}m_{1}^{k}}$ $= \mu$ (37b)
$\sum\limits_{k \in \mathcal{K}}{p_{k}m_{2}^{k}}$ $= {\mu^{2} + \sigma^{2}}$ (37c)
$\sum\limits_{k \in \mathcal{K}}{\frac{p_{k}}{T - 1}\left( {{T\left( m_{1}^{k} \right)^{2}} - m_{2}^{k}} \right)}$ ${= {\mu^{2} + {\rho\sigma^{2}}}}.$ (37d)

In the following we will update the scenarios ${\mathbf{ξ}}^{k}$ of the distribution $\mathbb{P}$ iteratively in finitely many steps, always ensuring that $\mathbb{P}$ remains within $\mathcal{P}$ after each update. The terminal distribution will have the property that ${\prod_{t = 1}^{T}\xi_{t}^{k}} = 0$ for every $k \in \mathcal{K}$, which means that we will have constructed a distribution ${\mathbb{P}} \in \mathcal{P}$ with ${{\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} = 0} \right)} = 1$. This will establish the claim.

### Step 1

Keeping the scenario probabilities as well as the scenario-wise arithmetic and quadratic means constant, we first replace each ${\mathbf{ξ}}^{k}$ with a minimizer of the problem

which depends parametrically on $m_{1}^{k}$ and $m_{2}^{k}$. By Lemma 3.5 (i) below, problem is indeed solvable for every $k \in \mathcal{K}$. The new distribution with updated scenarios still belongs to $\mathcal{P}$ because we did not change $p_{k}$, $m_{1}^{k}$ and $m_{2}^{k}$, implying that the moment conditions remain valid. To gain a better understanding of the updated distribution, we define the disjoint index sets

and note that $\mathcal{K} = {\mathcal{K}^{+} \cup \mathcal{K}^{-}}$ by Lemma 3.5 (i) below. Lemma 3.5 (ii) further implies that

We will henceforth say that $\mathcal{K}^{+}$ ($\mathcal{K}^{-}$) is the index set of the absorbing (non-absorbing) scenarios. If all scenarios are absorbing (that is, if $\mathcal{K}^{+} = \mathcal{K}$), then ${{\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} = 0} \right)} = 1$, and we are done.

### Step 2

If there exists a non-absorbing scenario $i \in \mathcal{K}^{-}$, we will alter both the scenarios and their quadratic means to make scenario $i$ absorbing, while ensuring that all scenarios $k \in \mathcal{K}^{+}$ remain absorbing. To achieve this, we consider the following family of quadratic means parameterized in $\lambda \in \lbrack 0,1\rbrack$.

By construction, $p_{k}$, $m_{1}^{k}$ and $m_{2}^{k} = {m_{2}^{k}(\lambda)}$ satisfy the moment conditions for every $\lambda \in \lbrack 0,1\rbrack$. As in Step 1, the scenario ${\mathbf{ξ}}^{k}(\lambda)$ is then chosen to be a minimizer of problem with inputs $m_{1}^{k}$ and $m_{2}^{k} = {m_{2}^{k}(\lambda)}$. However, could fail to be solvable for $\lambda \lesssim 1$, in which case the proposed construction would fail. Indeed, Lemma 3.5 (i) shows that is only solvable when $1 \leq \left. {m_{2}^{k}(\lambda)}/\left( m_{1}^{k} \right)^{2} \right. \leq T$. In the remainder we will demonstrate that there is $\lambda^{\star} \in $ such that ${\mathbf{ξ}}^{k}\left( \lambda^{\star} \right)$ exists for every $k \in \mathcal{K}$ and such that all scenarios $k \in {\mathcal{K}^{+} \cup \left\{ i \right\}}$ are absorbing.

Subtracting (37d) from (37c) and dividing the difference by (37c) yields

where the inequality follows from the assumption that $T > {\frac{\mu^{2} + \sigma^{2}}{\left( {1 - \rho} \right)\sigma^{2}} + 1}$. Multiplying both sides of the inequality by $\frac{T - 1}{T}$ and partitioning $\mathcal{K}$ into $\mathcal{K}^{+}$ and $\mathcal{K}^{-}$ further reveals that

The expression on the left hand side of the above inequality represents a weighted average of the fractions $\left. \left( {m_{2}^{k} - \left( m_{1}^{k} \right)^{2}} \right)/m_{2}^{k} \right.$ across all $k \in \mathcal{K}$. Recall from (39a) and (39b) that the fractions indexed by $k \in \mathcal{K}^{+}$ are larger or equal to $\left. 1/T \right.$, while those indexed by $k \in \mathcal{K}^{-}$ are strictly smaller than $\left. 1/T \right.$. The inequality asserts that the fractions corresponding to $k \in \mathcal{K}^{+}$ dominate those corresponding to $k \in \mathcal{K}^{-}$. Thus, remains valid if we replace $\mathcal{K}^{-}$ with $\left\{ i \right\}$, that is,

Using the notation introduced in, the inequality can be reformulated as

which constitutes a weighted average of the fractions $\left. \left( {{m_{2}^{k}} - \left( m_{1}^{k} \right)^{2}} \right)/m_{2}^{k} \right.$ across all $k \in {\mathcal{K}^{+} \cup \left\{ i \right\}}$. By construction, we have ${\left. \left( {{m_{2}^{k}} - \left( m_{1}^{k} \right)^{2}} \right)/m_{2}^{k} \right.} = \frac{1}{T}$ for every $k \in \mathcal{K}^{+}$, and thus the average on the left hand side of the above inequality can exceed $\frac{1}{T}$ only if

As $i \in \mathcal{K}^{-}$, the relation (39b) further implies that

The intermediate value theorem then guarantees the existence of $\lambda^{\star} \in $ with

By construction, we thus have $1 \leq \left. {m_{2}^{k}\left( \lambda^{\star} \right)}/\left( m_{1}^{k} \right)^{2} \right. \leq T$ for every $k \in \mathcal{K}$, which implies via Lemma 3.5 (i) that the corresponding scenarios ${\mathbf{ξ}}^{k}\left( \lambda^{\star} \right)$ are well-defined. Our construction also guarantees that $\frac{T}{T - 1} \leq \left. {m_{2}^{k}\left( \lambda^{\star} \right)}/\left( m_{1}^{k} \right)^{2} \right. \leq T$ for every $k \in {\mathcal{K}^{+} \cup \left\{ i \right\}}$, which implies via Lemma 3.5 (ii) that the corresponding scenarios ${\mathbf{ξ}}^{k}\left( \lambda^{\star} \right)$ are absorbing. Thus, by replacing ${\mathbf{ξ}}^{k}$ with ${\mathbf{ξ}}^{k}\left( \lambda^{\star} \right)$ in we obtain a new distribution ${\mathbb{P}} \in \mathcal{P}$ with more absorbing scenarios. As the total number of scenarios is finite, we can repeat Step 2 finitely many times to construct a distribution ${\mathbb{P}} \in \mathcal{P}$ that has only absorbing scenarios. Thus, the claim follows.

The proof of Theorem 3.2 ‣ 3 Left-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables") relies on the following auxiliary result.

### Lemma 3.5

Assume that ${m_{1},m_{2}} > 0$ and consider the parametric program

Then, the following statements hold:

Problem is feasible and solvable iff $T \geq \frac{m_{2}}{m_{1}^{2}} \geq 1$.

The optimal value of is zero iff $T \geq \frac{m_{2}}{m_{1}^{2}} \geq \frac{T}{T - 1}$.

Figure 2: Feasible region of problem for T = 2 and different values of m1 and m2. The diagonal line corresponds to the constraint ${\frac{1}{T}{\sum_{t = 1}^{T}\xi_{t}}} = m_{1}$, and each dotted curve corresponds to the constraint ${\frac{1}{T}{\sum_{t = 1}^{T}\xi_{t}^{2}}} = m_{2}$ for some combination of m1 and m2. The innermost and the outermost curves correspond to the cases where m2/m12 = 1 and m2/m12 = T, respectively. The feasible region for the (m1,m2)-combination represented by the bold curve is given by the two dots.

Figure 2 visualizes how the feasible set of problem depends on $m_{1}$ and $m_{2}$.

As for assertion (i), assume that there is $\mathbf{ξ}$ feasible in. We then have ${\frac{1}{T}{\sum_{t = 1}^{T}\xi_{t}}} = m_{1}$, which implies that ${Tm_{1}^{2}} \geq m_{2} \geq m_{1}^{2}$ since $\left. \left. \left. \parallel{\mathbf{ξ}}\parallel \right._{1} \geq \parallel{\mathbf{ξ}}\parallel \right._{2} \geq \frac{1}{\sqrt{T}}\parallel{\mathbf{ξ}}\parallel_{1} \right.$. Conversely, if $T \geq \frac{m_{2}}{m_{1}^{2}} \geq 1$, we may define ${\mathbf{ξ}} = \left( z,\frac{{m_{1}T} - z}{T - 1},\ldots,\frac{{m_{1}T} - z}{T - 1} \right)$ for some $z \in \left\lbrack m_{1},{Tm_{1}} \right\rbrack$ to be chosen later. By construction, we have ${\frac{1}{T}{\sum_{t = 1}^{T}\xi_{t}}} = m_{1}$ irrespective of $z$, while

changes continuously from $m_{1}^{2}$ to $Tm_{1}^{2}$ when $z$ is swept from $m_{1}$ to $Tm_{1}$. Thus, by the intermediate value theorem, we may assume that ${\frac{1}{T}{\sum_{t = 1}^{T}\xi_{t}^{2}}} = m_{2} \in \left\lbrack m_{1}^{2},{Tm_{1}^{2}} \right\rbrack$ for some suitably chosen $z \in \left\lbrack m_{1},{Tm_{1}} \right\rbrack$. We conclude that is feasible whenever $T \geq \frac{m_{2}}{m_{1}^{2}} \geq 1$. In that case, however, is also solvable as the objective function is continuous and the feasible set is compact.

To prove assertion (ii), we observe that the optimal value of vanishes iff the problem admits a minimizer $\mathbf{ξ}$ with ${\prod_{t = 1}^{T}\xi_{t}} = 0$. More precisely, by permutation symmetry, the minimum of vanishes iff there exists $\mathbf{ξ}$ with $\xi_{T} = 0$, ${\frac{1}{T}{\sum_{t = 1}^{T - 1}\xi_{t}}} = m_{1}$ and ${\frac{1}{T}{\sum_{t = 1}^{T - 1}\xi_{t}^{2}}} = m_{2}$. By assertion (i), however, the last two inequalities are satisfiable iff

and thus the claim follows.

## Right-Sided Chebyshev Bounds

We now study *right-sided Chebyshev bounds* of the form

where the ambiguity set $\mathcal{P}$ is defined in. We first present the main result of this section.

### Theorem 4.1 (Right-Sided Chebyshev Bound)

Let $\gamma > 0$. For all $T \geq 3$ the right-sided Chebyshev bound $\text{R}{(\gamma)}$ coincides with the optimal objective value of the semidefinite program

where we use the convention that the entries of $\mathbf{p}$, $\mathbf{P}$, $\mathbf{q}$ and $\mathbf{Q}$ are numbered starting from $0$. For $T = 2$, $\text{R}{(\gamma)}$ is given by a variant of (47 ‣ 4 Right-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables")) where the constraints ${p_{2} + q_{1}} = {\alpha - 1}$ and ${p_{T} + q_{T - 1}} = {2{({T - 1})}\gamma_{2}\gamma^{\frac{1}{T - 1}}}$ are combined to ${p_{2} + q_{1}} = {{\alpha - 1} + {2{({T - 1})}\gamma_{2}\gamma^{\frac{1}{T - 1}}}}$.

Using similar arguments as in the proof of Theorem 3.1 ‣ 3 Left-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables"), one first shows that the worst-case probability problem $\sup_{{\mathbb{P}} \in \mathcal{P}}{{\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \geq \gamma} \right)}$ admits a strong dual which constitutes a semi-infinite optimization problem. Exploiting this problem's permutation symmetry, one can further show that its optimal value amounts to

Details are omitted for brevity of exposition. Lemma 3.2 then implies that reduces to

By leveraging the $\mathcal{S}$-lemma and a well-known reformulation of hyperbolic constraints as second-order cone constraints, one can use similar arguments as in the proof of Theorem 3.1 ‣ 3 Left-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables") to show that the first three constraints in hold iff there exist ${\lambda_{1},\lambda_{2},\lambda_{3}} \geq 0$ satisfying

By Lemma 4.1 below, the last semi-infinite constraint in can be re-expressed as

which is identical to. The claim then follows by replacing this constraint with its explicit semidefinite reformulation familiar from Theorem 3.1 ‣ 3 Left-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables").

The proof of Theorem 4.1 ‣ 4 Right-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables") relies on 2 auxiliary lemmas, which we prove next.

### Lemma 4.1

For $T \geq 2$, $\overline{\gamma} = \infty$ and $\underset{¯}{\gamma} \geq 0$, the optimal value $g_{T}{(\underset{¯}{\gamma},\infty)}$ of (25b) equals

If $\underset{¯}{\gamma} > T^{- T}$, then the maximization problem (25b) is infeasible due to the inequality of arithmetic and geometric means, and thus we have ${g_{T}\left( \underset{¯}{\gamma},\infty \right)} = {- \infty}$. For $\underset{¯}{\gamma} = T^{- T}$, the unique feasible solution of (25b) is ${\mathbf{ξ}} = {\frac{1}{T}\mathbf{1}}$, which implies that ${g_{T}\left( \underset{¯}{\gamma},\infty \right)} = \frac{1}{T}$. Moreover, for $\underset{¯}{\gamma} = 0$, the last constraint in (25b) becomes redundant. In this case $g_{T}\left( \underset{¯}{\gamma},\infty \right)$ is optimized by ${\mathbf{ξ}} = \mathbf{e}_{i}$, and thus we find ${g_{T}\left( \underset{¯}{\gamma},\infty \right)} = 1$. Lastly, for $0 < \underset{¯}{\gamma} < T^{- T}$, the maximization problem (25b) is feasible, and every feasible solution has strictly positive components. In addition, the product constraint ${\prod_{t = 1}^{T}\xi_{t}} \geq \underset{¯}{\gamma}$ is binding at optimality for otherwise convex combinations of the optimal solution $\mathbf{ξ}$ with $\mathbf{e}_{i}$, where $i \in {\arg{\max\left\{ {{\mathbf{ξ}}_{j}:{j = {1,\ldots,T}}} \right\}}}$, would improve the objective function of (25b), which is a contradiction. We thus conclude that

As in the proof of Lemma 3.3, for $0 < \underset{¯}{\gamma} < T^{- T}$ one can use the optimality conditions of (25b) to show that

where the functions $g_{T,k}:{\left( 0,T^{- T} \right)\rightarrow{\mathbb{R}}}$, $k = {1,2,\ldots,\left\lfloor \frac{T}{2} \right\rfloor}$, are defined through

Lemma 4.2 below asserts that the maximum in is attained at $k = 1$. We thus obtain

The statement of the lemma now follows since the maximization problem in the equation above evaluates to $1$ at $\underset{¯}{\gamma} = 0$ and to $\left. 1/T \right.$ at $\underset{¯}{\gamma} = T^{- T}$. Indeed, the maximization problem is bounded above by $\max_{{\|{\mathbf{ξ}}\|}_{1} = 1}\left\| {\mathbf{ξ}} \right\|_{2}^{2}$, and the optimal value $1$ of this bound is achieved by the feasible solution $\left( \underset{¯}{\xi},\overline{\xi} \right) = $ of the maximization problem at $\underset{¯}{\gamma} = 0$. Likewise, $g_{T}\left( T^{- T},\infty \right)$ is bounded above by $\max_{{\mathbf{ξ}} \geq \mathbf{0}}\left\{ {\left\| {\mathbf{ξ}} \right\|_{2}^{2}:{{\left\| {\mathbf{ξ}} \right\|_{1} = 1},{\left. \prod{}_{t}\xi_{t} \right. = T^{- T}}}} \right\}$, and the optimal value $\left. 1/T \right.$ of this bound is achieved by the feasible solution $\left( \underset{¯}{\xi},\overline{\xi} \right) = \left( \frac{1}{T},\frac{1}{T} \right)$ of the maximization problem.

### Lemma 4.2

For $T \geq 2$ and $0 < \underset{¯}{\gamma} < T^{- T}$, the optimal value of is given by $g_{T,1}{(\underset{¯}{\gamma})}$.

The proof widely parallels that of Lemma 3.4 and is therefore omitted.

We now show that in the extreme case, the weak-sense geometric random walk $\overset{\sim}{\mathbf{π}} = \left\{ {\overset{\sim}{\pi}}_{T} \right\}_{T \in {\mathbb{N}}}$ defined through ${\overset{\sim}{\pi}}_{T} = {\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}}$ weakly exceeds the deterministic growth process $\left\{ \mu^{T} \right\}_{T \in {\mathbb{N}}}$ with certainty for any time horizon $T$, assuming that $\rho \geq 0$. The result can be viewed as the right-sided analogue of Theorem 3.2 ‣ 3 Left-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables").

### Proposition 4.1

If $\rho \geq 0$, then ${\text{R}{(\gamma)}} = 1$ for all $\gamma \leq \mu^{T}$.

The objective function of problem can be reformulated as

For $\gamma \leq \mu^{T}$, the first term equals the left hand side of the third semi-infinite constraint in if we set $s = {T\mu}$, and it must therefore be greater than or equal to 1. In the second term, the factor $\left( {\gamma_{1} + {\left( {1 + {\left( {T - 1} \right)\rho}} \right)\gamma_{2}}} \right)$ can be expressed as the linear combination ${\rho \cdot \left( {\gamma_{1} + {T\gamma_{2}}} \right)} + {\left( {1 - \rho} \right) \cdot \left( {\gamma_{1} + \gamma_{2}} \right)}$. For $\rho \geq 0$, this linear combination becomes a convex combination, and the claim follows since ${\gamma_{1} + {T\gamma_{2}}} \geq 0$ and ${\gamma_{1} + \gamma_{2}} \geq 0$ are explicit constraints in the equivalent reformulation (47 ‣ 4 Right-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables")).

We highlight that Proposition 4.1 breaks down for $\rho < 0$.

## Covariance Bounds

The ambiguity set $\mathcal{P}$ reflects the assumption that the covariance matrix $\mathbf{\Sigma}$ is known *precisely* and that the (co-)variances of the components of $\overset{\sim}{\mathbf{ξ}}$ are permutation symmetric. Either assumption may prove overly restrictive in practice. In this section, we therefore assume that only an upper bound on the covariance matrix is available. More precisely, we consider the ambiguity set

where $\mathbf{μ}$ and $\mathbf{\Sigma}$ are defined as in Section 1. For $\gamma > 0$, we are then interested in quantifying *relaxed left-sided and right-sided Chebyshev bounds* of the form

In the following, we analyze each of these relaxed bounds in turn.

### Theorem 5.1 (Relaxed Left-Sided Chebyshev Bound)

The relaxed left-sided Chebyshev bound satisfies ${\text{L}^{\prime}{(\gamma)}} = {\text{L}{(\gamma)}}$ for all $\gamma > 0$.

By repeating the first few steps of the proof of Theorem 3.1 ‣ 3 Left-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables"), one can show that $\text{L}^{\prime}(\gamma)$ coincides with the optimal value of with the extra constraint $\mathbf{\Gamma} \succeq \mathbf{0}$. In this case Lemma 3.1 remains valid and implies that we can restrict attention to permutation-symmetric solutions of the form $\mathbf{\Gamma} = {{\gamma_{1}{\mathbb{I}}} + {\gamma_{2}\mathbf{1}\mathbf{1}^{\intercal}}}$ for some ${\gamma_{1},\gamma_{2}} \in {\mathbb{R}}$. As $\mathbf{\Gamma} = {{\gamma_{1}{\mathbb{I}}} + {\gamma_{2}\mathbf{1}\mathbf{1}^{\intercal}}} \succeq \mathbf{0}$ iff ${\gamma_{1} + {T\gamma_{2}}} \geq 0$ and $\gamma_{1} \geq 0$ by virtue of \[26, Proposition 4\], we may then conclude that $\text{L}^{\prime}(\gamma)$ coincides with the optimal value of with the extra constraints ${\gamma_{1} + {T\gamma_{2}}} \geq 0$ and $\gamma_{1} \geq 0$. Note that is equivalent to (13 ‣ 3 Left-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables")) and. As ${\gamma_{1} + {T\gamma_{2}}} \geq 0$ is an explicit constraint of problem (13 ‣ 3 Left-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables")), it is necessarily an implicit constraint of the problems and. Thus, $\text{L}^{\prime}(\gamma)$ coincides with the optimal value of with the extra constraint $\gamma_{1} \geq 0$. To prove the identity ${\text{L}(\gamma)} = {\text{L}^{\prime}(\gamma)}$, it is therefore sufficient to show that appending the extra constraint $\gamma_{1} \geq 0$ has no impact on the optimal value of.

To this end, fix any feasible solution of problem with $\gamma_{1} < 0$. As this solution must satisfy the constraint ${\alpha + {s\beta} + {s^{2}\gamma_{2}} + {s^{2}\gamma_{1}}} \geq 1$ for every $s \geq 0$ and as $s = {T\mu} > 0$, we have

Moreover, the objective function of can be reformulated as

which constitutes a sum of three terms. The first term in the sum is greater than or equal to 1 because of, and the second term is strictly positive because $T \geq 2$, $\gamma_{1} < 0$ and ${\mu^{2} + {\rho\sigma^{2}}} > 0$. The third term is non-negative because $\rho > {- \left. 1/\left( {T - 1} \right) \right.}$ and ${\gamma_{1} + \gamma_{2}} \geq 0$ is an explicit constraint of (13 ‣ 3 Left-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables")) and thus an implicit constraint of. In summary, we have shown that the objective value of any feasible solution of with $\gamma_{1} < 0$ is strictly greater than 1. As the optimal value $\text{L}(\gamma)$ of represents a probability, however, we conclude that no feasible solution with $\gamma_{1} < 0$ can optimize. Thus, the extra constraint $\gamma_{1} \geq 0$ does not change the optimal value of, and the claim follows.

### Theorem 5.2 (Relaxed Right-Sided Chebyshev Bound)

The relaxed right-sided Chebyshev bound admits the analytical solution

where $\theta = {1 + {{({T - 1})}\rho}} > 0$.

Using similar arguments as in the proof of the previous theorem, one can show that $\text{R}^{\prime}(\gamma)$ coincides with the optimal value of the following semi-infinite optimization problem:

Without loss of generality, we use different symbols $\overline{\mathbf{ξ}}$ and $\underset{¯}{\mathbf{ξ}}$ to denote the uncertain parameters in the two semi-infinite constraints, respectively. Note that can be viewed as the robust counterpart of an uncertain convex program with constraint-wise uncertainty sets. As the left hand sides of the robust constraints are convex in the respective uncertainties, the 'primal worst equals dual best' duality scheme portrayed in \[2, Theorem 4.1\] implies that is equivalent to

where $p$ and $q$ represent dual variables assigned to the two robust constraints in. Thus, the primal uncertain convex program is solved under the worst possible realizations of $\overline{\mathbf{ξ}}$ and $\underset{¯}{\mathbf{ξ}}$, while the dual uncertain convex program is solved under the best possible realizations, in which case $\overline{\mathbf{ξ}}$ and $\underset{¯}{\mathbf{ξ}}$ become decision variables. Problem has intuitive appeal as it can be interpreted as a restriction of the original worst-case probability problem that minimizes over all two-point distributions in the ambiguity set $\mathcal{P}^{\prime}$ with scenarios $\overline{\mathbf{ξ}}$ and $\underset{¯}{\mathbf{ξ}}$ and corresponding probabilities $p$ and $q$, respectively. Note that constitutes a non-convex program because it involves multilinear terms in the decisions. Using the variable transformations ${\mathbf{u}}\leftarrow{p\overline{\mathbf{ξ}}}$ and ${\mathbf{v}}\leftarrow{q\underset{¯}{\mathbf{ξ}}}$ we can reformulate as

Note that if $p = 0$ ($q = 0$), then ${\mathbf{u}} = \mathbf{0}$ (${\mathbf{v}} = \mathbf{0}$) for otherwise the matrix inequality is not satisfiable. In and below we adhere to the convention that $\left. 0/0 \right. = 0$, which reflects the idea that a scenario with zero probability mass should have zero weight in the covariance matrix. Observe that problem is a convex program. In particular, the first constraint is convex because of the concavity of geometric means, and the last constraint is convex due to a standard Schur complement argument. Exploiting the problem's permutation symmetry and convexity, one can proceed as in Lemma 3.1 to show that has a permutation symmetric minimizer of the form ${\mathbf{u}} = {u\mathbf{1}}$ and ${\mathbf{v}} = {v\mathbf{1}}$ for some scalar decision variables ${u,v} \in {\mathbb{R}}_{+}$. Restricting the search to permutation symmetric solutions, problem can therefore be reformulated as

It can be shown that the eigenvalues of the matrix ${\left( {1 - \rho} \right)\sigma^{2}{\mathbb{I}}} + {\left( {{\mu^{2} + {\rho\sigma^{2}}} - \frac{u^{2}}{p} - \frac{v^{2}}{q}} \right)\mathbf{1}\mathbf{1}^{\intercal}}$ are given by $\left( {1 - \rho} \right)\sigma^{2}$ and ${\left( {1 - \rho} \right)\sigma^{2}} + {T\left( {{\mu^{2} + {\rho\sigma^{2}}} - \frac{u^{2}}{p} - \frac{v^{2}}{q}} \right)}$; see e.g. \[26, Proposition 4\]. Since ${\left( {1 - \rho} \right)\sigma^{2}} > 0$ by assumption, the matrix inequality in is equivalent to the scalar constraint

Any feasible solution of satisfies ${q\gamma^{1/T}} \leq v \leq \mu$, implying that the optimal value of is bounded above by $\min\left\{ 1,{\mu\gamma^{- {1/T}}} \right\}$. For $0 < \gamma^{1/T} \leq \mu$, an optimal solution of is then given by $(p,q,u,v) = (0,1,0,\mu)$, and the optimal value is equal to 1. For $\mu < \gamma^{1/T} < {\mu + \frac{\left( {1 + {\left( {T - 1} \right)\rho}} \right)\sigma^{2}}{T\mu}}$, on the other hand, an optimal solution is given by $(p,q,u,v) = \left( {1 - {\mu\gamma^{- {1/T}}}},{\mu\gamma^{- {1/T}}},0,\mu \right)$ with corresponding optimal value $\mu\gamma^{- {1/T}}$. Indeed, any larger value of $q$ would require a larger value of $v$, which in turn would violate the non-negativity of $u$ as ${u + v} = \mu$. One can show that the constraint is always inactive at this solution. For $\gamma^{1/T} \geq {\mu + \frac{\left( {1 + {\left( {T - 1} \right)\rho}} \right)\sigma^{2}}{T\mu}}$, finally, the constraint implies that $q$ must not exceed $\mu\gamma^{- {1/T}}$, which in turn implies that the constraint must be binding. Furthermore, $q$ has to be strictly positive for otherwise would be solved by $(p,q,u,v) = (1,0,\mu,0)$, which contradicts our earlier finding that the constraint is binding. Substituting $p = {1 - q}$ and $u = {\mu - v}$, the left hand side of becomes a quadratic function of $v$ parametric in $q$. We denote the two roots of this function by $v^{+}$ and $v^{-}$ and define $u^{+} = {\mu - v^{+}}$ and $u^{-} = {\mu - v^{-}}$. A direct calculation yields

By construction, both $\left( u^{+},v^{+} \right)$ and $\left( u^{-},v^{-} \right)$ satisfy as an equality. However, there is no $q \in (0,1\rbrack$ for which $\left( u^{+},v^{+} \right)$ is feasible in. Indeed, a direct calculation reveals that the constraint $v^{+} \geq {q\gamma^{1/T}}$ from can hold only if

However, is not satisfiable as its left hand side is strictly negative by assumption, whereas its right hand side is non-negative. Therefore, $\left( u^{+},v^{+} \right)$ is infeasible in.

In contrast, the second solution $\left( u^{-},v^{-} \right)$ is feasible in if we select $q \in (0,1\rbrack$ with

Problem aims to maximize $q$, which is tantamount to setting

where the second equality follows from $\gamma^{1/T} \geq {\mu + \frac{\left( {1 + {\left( {T - 1} \right)\rho}} \right)\sigma^{2}}{T\mu}}$. Thus, the claim follows.

In addition to admitting an analytical solution, the relaxed right-sided Chebyshev bounds also allow us to determine a distribution ${\mathbb{P}}^{\star} \in \mathcal{P}^{\prime}$ that attains the probability bound.

### Corollary 5.1 (Extremal Distribution)

A distribution ${\mathbb{P}}^{\star} \in \mathcal{P}^{\prime}$ attaining the relaxed right-sided Chebyshev bound $\text{R}^{\prime}{(\gamma)}$ is given by ${\mathbb{P}}^{\star} = {{p^{\star}\delta_{{\lbrack{u^{\star}/p^{\star}}\rbrack}\mathbf{1}}} + {q^{\star}\delta_{{\lbrack{v^{\star}/q^{\star}}\rbrack}\mathbf{1}}}}$, where

and $p^{\star} = {1 - q^{\star}}$, as well as

and $u^{\star} = {\mu - v^{\star}}$, where $\theta = {1 + {{({T - 1})}\rho}} > 0$.

The proof follows directly from that of Theorem 5.2 ‣ 5 Covariance Bounds ‣ Chebyshev Inequalities for Products of Random Variables") and is thus omitted.

The relaxed left-sided and right-sided Chebyshev bounds differ in the sense that the left-sided bound coincides with $\text{L}(\gamma)$, whereas $\text{R}^{\prime}(\gamma)$ does not equal $\text{R}(\gamma)$ in general. The relaxed right-sided Chebyshev bound does coincide with $\text{R}(\gamma)$, however, when $T$ is sufficiently large.

### Proposition 5.1

If $\mu > {\sqrt{\frac{1 - \rho}{T}}\sigma}$, then ${\text{R}^{\prime}{(\gamma)}} = {\text{R}{(\gamma)}}$ for all $\gamma \geq \overline{\gamma}$, where

with $a = {\mu - {\sqrt{\frac{1 - \rho}{T}}\sigma}}$, $b = \frac{T}{\sigma^{2}\theta}$ and $\theta = {1 + {{({T - 1})}\rho}}$.

Note that ${ab}\rightarrow\infty$ and thus ${\overline{\gamma}}^{1/T}\rightarrow\mu$ whenever $T\rightarrow\infty$. The rate of convergence depends on $\mu$, $\sigma$ and $\rho$, and the fastest convergence is observed for large $\mu$ and small $\sigma$ and $\rho$.

We first show that ${\overline{\gamma}}^{1/T} > {\mu + \frac{\sigma^{2}\theta}{T\mu}}$ (Step 1), which allows us to invoke Theorem 5.2 ‣ 5 Covariance Bounds ‣ Chebyshev Inequalities for Products of Random Variables") to conclude that ${\text{R}^{\prime}(\gamma)} = \frac{\sigma^{2}\theta}{{\sigma^{2}\theta} + {T\left( {\mu - \gamma^{1/T}} \right)^{2}}}$. We then employ Corollary 5.1 ‣ 5 Covariance Bounds ‣ Chebyshev Inequalities for Products of Random Variables") to construct a distribution ${\mathbb{P}}^{\star} \in \mathcal{P}^{\prime}$ that satisfies ${{\mathbb{P}}^{\star}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \geq \gamma} \right)} = {\text{R}^{\prime}(\gamma)}$ (Step 2), and we show that a suitable perturbation of ${\mathbb{P}}^{\star}$ results in a distribution ${\mathbb{P}} \in \mathcal{P}$ that satisfies ${{\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \geq \gamma} \right)} = {{\mathbb{P}}^{\star}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \geq \gamma} \right)}$ (Step 3). The statement then follows from the fact that $\text{R}(\gamma)$ is bounded above by $\text{R}^{\prime}(\gamma)$.

### Step 1

We show that ${\overline{\gamma}}^{1/T}$ is the maximum root of the convex quadratic function

where $a$ and $b$ are defined in the statement of the theorem, and that this root satisfies ${\overline{\gamma}}^{1/T} > {\mu + \frac{\sigma^{2}\theta}{T\mu}}$. From the quadratic formula we know that the maximum root $x^{\star}$ of $q(x)$ satisfies

and replacing $a$ and $b$ with their definitions reveals that $x^{\star} = {\overline{\gamma}}^{1/T}$. To show that ${\overline{\gamma}}^{1/T} > {\mu + \frac{\sigma^{2}\theta}{T\mu}}$, we observe that

as well as ${q(x)}\rightarrow\infty$ for $x\rightarrow\infty$ since $\mu > {\sqrt{\frac{1 - \rho}{T}}\sigma}$. Since $q(x)$ is quadratic, both observations imply that the maximum root $x^{\star} = {\overline{\gamma}}^{1/T}$ of $q(x)$ indeed belongs to the interval $\left( {\mu + \frac{\sigma^{2}\theta}{T\mu}},\infty \right)$.

### Step 2

The distribution ${\mathbb{P}}^{\star}$ in Corollary 5.1 ‣ 5 Covariance Bounds ‣ Chebyshev Inequalities for Products of Random Variables") satisfies ${{\mathbb{P}}^{\star}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \geq \gamma} \right)} = {\text{R}^{\prime}(\gamma)}$. For later reference, we remark that ${\mathbb{P}}^{\star} = {{p^{\star}\delta_{{\lbrack{u^{\star}/p^{\star}}\rbrack}\mathbf{1}}} + {q^{\star}\delta_{{\lbrack{v^{\star}/q^{\star}}\rbrack}\mathbf{1}}}}$ satisfies the properties

Note that the last condition holds because is binding when $\gamma^{1/T} \geq {\mu + \frac{\sigma^{2}\theta}{T\mu}}$.

### Step 3

Consider the distribution $\mathbb{P}$ defined through

with $\lambda = {\sqrt{\frac{1 - \rho}{p^{\star}T}}\sigma}$. If ${\mathbb{P}} \in \mathcal{P}$, then we find that

which implies ${\text{R}(\gamma)} = {\text{R}^{\prime}(\gamma)}$. We thus need to show that ${\mathbb{P}} \in \mathcal{P}$. To this end, we first observe that the first two moments of $\overset{\sim}{\mathbf{ξ}}$ under $\mathbb{P}$ satisfy

where the last row is due to and our definition of $\lambda$. It remains to be shown that $\overset{\sim}{\mathbf{ξ}}$ is non-negative $\mathbb{P}$-a.s. By construction of $\mathbb{P}$, this is the case iff $u^{\star} \geq {p^{\star}\lambda}$. We now observe that

where the first identity follows from, the second one is due to the definition of $q^{\star}$ in Corollary 5.1 ‣ 5 Covariance Bounds ‣ Chebyshev Inequalities for Products of Random Variables"), and the inequality holds since there is $C > 0$ such that

and this expression is non-negative whenever $\gamma \geq \overline{\gamma}$. We thus conclude that

which in turn implies that $u^{\star} \geq {\sqrt{\frac{\left( {1 - \rho} \right)p^{\star}}{T}}\sigma} = {p^{\star}\lambda}$ as desired. The claim now follows.

## Extensions

The techniques developed in this paper can also be used to construct Chebyshev bounds for sums, minima and maxima of non-negative random variables. All these Cheybshev bounds can be reduced to computing $\sup_{{\mathbb{P}} \in \mathcal{P}}{{\mathbb{P}}\left( {{h\left( \overset{\sim}{\mathbf{ξ}} \right)} \leq 0} \right)}$ for some permutation-symmetric functional $h({\mathbf{ξ}})$.

### Theorem 6.1

For any permutation-symmetric continuous functional $h:{{\mathbb{R}}_{+}^{T}\rightarrow{\mathbb{R}}}$, we have

where the optimal value functions $\underset{¯}{\phi}{(s)}$ and $\overline{\phi}{(s)}$ are defined as

for all $s \geq 0$, while $\mathcal{S} = \left\{ {s \in {\mathbb{R}}_{+}}:{{\underset{¯}{\phi}{(s)}} < {+ \infty}} \right\}$ denotes the effective domain of $\underset{¯}{\phi}{(s)}$ and $\overline{\phi}{(s)}$.

The proof is largely based on arguments familiar from Theorems 3.1 ‣ 3 Left-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables") and 4.1 ‣ 4 Right-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables"). Details are omitted for brevity of exposition.

The significance of Theorem 6.1 is that it enables us to compute $\sup_{{\mathbb{P}} \in \mathcal{P}}{{\mathbb{P}}\left( {{h\left( \overset{\sim}{\mathbf{ξ}} \right)} \leq 0} \right)}$ by solving a semidefinite program whenever $\underset{¯}{\phi}(s)$ and $\overline{\phi}(s)$ are piecewise polynomials. In this case the last two constraints in reduce to the requirement that a univariate piecewise polynomial, whose coefficients depend affinely on the decision variables, must be non-negative uniformly on $\mathcal{S}$. Such conditions can systematically be reformulated as linear matrix inequalities.

$\sup\limits_{{\mathbb{P}} \in \mathcal{P}}{{\mathbb{P}}\left( {{\min\limits_{t = {1,\ldots,T}}{\overset{\sim}{\xi}}_{t}} \leq \gamma} \right)}$
${\min\limits_{t = {1,\ldots,T}}\xi_{t}} - \gamma$
$\left\{ \begin{array}{l}
{\gamma^{2} + {\frac{1}{T - 1}\left( {s - \gamma} \right)^{2}}}
\end{array} \right.$
{{\text{if~}s} \geq {\gammaT}} \\
{{\text{if~}0} \leq s &lt; {\gammaT}}

$\sup\limits_{{\mathbb{P}} \in \mathcal{P}}{{\mathbb{P}}\left( {{\min\limits_{t = {1,\ldots,T}}{\overset{\sim}{\xi}}_{t}} \geq \gamma} \right)}$
$\gamma - {\min\limits_{t = {1,\ldots,T}}\xi_{t}}$
$\left\{ \begin{array}{l}
\end{array} \right.$
{{\text{if~}s} \geq {\gammaT}} \\
{{\text{if~}0} \leq s &lt; {\gammaT}}
$\left\{ \begin{array}{l}
{\left( {s - {\gammaT}} \right)^{2} + {2\gamma\left( {s - {\gammaT}} \right)} + {T\gamma^{2}}} \\
\end{array} \right.$
{{\text{if~}s} \geq {\gammaT}} \\
{{\text{if~}0} \leq s &lt; {\gammaT}}

$\sup\limits_{{\mathbb{P}} \in \mathcal{P}}{{\mathbb{P}}\left( {{\max\limits_{t = {1,\ldots,T}}{\overset{\sim}{\xi}}_{t}} \leq \gamma} \right)}$
${\max\limits_{t = {1,\ldots,T}}\xi_{t}} - \gamma$
$\left\{ \begin{array}{l}
\end{array} \right.$
{{\text{if~}0} \leq s \leq {\gammaT}} \\
$\left\{ \begin{array}{l}
{\gamma^{2} + \left( {s - \gamma} \right)^{2}} \\
{{\left( {T - 1} \right)\gamma^{2}} + \left( {s - {\left( {T - 1} \right)\gamma}} \right)^{2}} \\
\end{array} \right.$
{{\text{if~}0} \leq s \leq \gamma} \\
{{\text{if~}\gamma} &lt; s \leq {2\gamma}} \\
{{\text{if~}\left( {T - 1} \right)\gamma} &lt; s \leq {T\gamma}} \\

$\sup\limits_{{\mathbb{P}} \in \mathcal{P}}{{\mathbb{P}}\left( {{\max\limits_{t = {1,\ldots,T}}{\overset{\sim}{\xi}}_{t}} \geq \gamma} \right)}$
$\gamma - {\max\limits_{t = {1,\ldots,T}}\xi_{t}}$
$\left\{ \begin{array}{l}
{\gamma^{2} + {\frac{1}{T - 1}\left( {s - \gamma} \right)^{2}}} \\
\end{array} \right.$
{{\text{if~}s} \geq {\gammaT}} \\
{{\text{if~}\gamma} \leq s &lt; {\gammaT}} \\
{{\text{if~}0} \leq s &lt; \gamma}
$\left\{ \begin{array}{l}
\end{array} \right.$
{{\text{if~}s} \geq \gamma} \\
{{\text{if~}0} \leq s &lt; \gamma}

$\sup\limits_{{\mathbb{P}} \in \mathcal{P}}{{\mathbb{P}}\left( {{\sum\limits_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \leq \gamma} \right)}$
${\sum\limits_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} - \gamma$
$\left\{ \begin{array}{l}
\end{array} \right.$
{{\text{if~}0} \leq s \leq \gamma} \\
$\left\{ \begin{array}{l}
\end{array} \right.$
{{\text{if~}0} \leq s \leq \gamma} \\

$\sup\limits_{{\mathbb{P}} \in \mathcal{P}}{{\mathbb{P}}\left( {{\sum\limits_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \geq \gamma} \right)}$
$\gamma - {\sum\limits_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}}$
$\left\{ \begin{array}{l}
\end{array} \right.$
{{\text{if~}s} \geq \gamma} \\
{{\text{if~}0} \leq s &lt; \gamma}
$\left\{ \begin{array}{l}
\end{array} \right.$
{{\text{if~}s} \geq \gamma} \\
{{\text{if~}0} \leq s &lt; \gamma}

Table 1: Chebyshev bounds equivalent to $\sup_{{\mathbb{P}} \in \mathcal{P}}{{\mathbb{P}}{({{h{(\overset{\sim}{\mathbf{ξ}})}} \leq 0})}}$ for some permutation symmetric functional h (ξ). These bounds coincide with the optimal value of, instantiated with the respective piecewise polynomials $\underset{¯}{\phi}{(s)}$ and $\overline{\phi}{(s)}$.

Table 1 lists examples of permutation-symmetric functionals $h({\mathbf{ξ}})$ that lead to piecewise polynomial mappings $\underset{¯}{\phi}(s)$ and $\overline{\phi}(s)$ and thus to computable Chebyshev bounds. Theorems 6.2 ‣ 6 Extensions ‣ Chebyshev Inequalities for Products of Random Variables") and 6.3 ‣ 6 Extensions ‣ Chebyshev Inequalities for Products of Random Variables") below present two special cases in which these bounds can be evaluated analytically.

### Theorem 6.2 (Left-Sided Chebyshev Bound for Sums)

For any $\gamma > 0$ we have

where $\theta = {1 + {{({T - 1})}\rho}} > 0$.

By Theorem 6.1 the Chebyshev bound $\sup_{{\mathbb{P}} \in \mathcal{P}}{{\mathbb{P}}\left( {{\sum_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \geq \gamma} \right)}$ can be reformulated as the semi-infinite program, where the functions $\underset{¯}{\phi}(s)$ and $\overline{\phi}(s)$ are specified in Table 1. Distinguishing the cases $\gamma_{1} \geq 0$ and $\gamma_{1} < 0$, this semi-infinite program can be reduced to a robust optimization problem with a scalar uncertain parameter by using the 'primal worst equals dual best' duality scheme from robust optimization. One can further show that the optimal value of this problem coincides with the univariate Chebyshev bound $\sup_{{\mathbb{P}}_{1} \in \mathcal{P}}{{\mathbb{P}}\left( {\overset{\sim}{\xi} \geq \gamma} \right)}$, where $\mathcal{P}_{1}$ contains all distributions of $\overset{\sim}{\xi}$ supported on ${\mathbb{R}}_{+}$ with mean $T\mu$ and variance $\sigma^{2}T\left( {1 + {\left( {T - 1} \right)\rho}} \right)$. The latter Chebyshev bound has an analytical formula, which can be obtained from.

### Theorem 6.3 (Right-Sided Chebyshev Bound for Sums)

For any $\gamma > 0$ we have

where $\theta = {1 + {{({T - 1})}\rho}} > 0$.

The proof is widely parallel to that of Theorem 6.2 ‣ 6 Extensions ‣ Chebyshev Inequalities for Products of Random Variables") and is thus omitted for brevity.

## Numerical Experiments

We first compare our Chebyshev bounds $\text{R}(\gamma)$ and $\text{L}(\gamma)$ with alternative bounds proposed in the literature, as well as the relaxed Chebyshev bound $\text{R}^{\prime}(\gamma)$ from Section 5. We then present a case study that employs our left-sided Chebyshev bound $\text{L}(\gamma)$ to select financial portfolios under imprecise knowledge of the asset return distributions. All optimization problems are solved with the SDPT3 optimization software using the YALMIP interface.

### Comparison of Chebyshev Bounds

Instead of employing the bounds $\text{R}(\gamma)$ and $\text{L}(\gamma)$ from Sections 3 and 4, which are exact but may result in computationally challenging optimization problems, one can employ existing results to derive approximate bounds on the tail probabilities of a product of non-negative, permutation-symmetric random variables. In the following, we compare our bounds with two such approximations based on earlier results of Marshall and Olkin and Vandenberghe et al.. Both approximations rely on the larger ambiguity set

with support ${\mathbb{R}}^{T}$, where ${\mathbf{μ}} \in {\mathbb{R}}^{T}$ and $\mathbf{\Sigma} \in {\mathbb{S}}_{+}^{T}$, $\mathbf{\Sigma} \succ \mathbf{0}$, need not be permutation-symmetric.

Marshall and Olkin derive a convex optimization problem that provides a tight upper bound on the probability that the random vector $\overset{\sim}{\mathbf{ξ}}$ is contained in a closed convex set $\mathcal{C}$, assuming that $\overset{\sim}{\mathbf{ξ}}$ can be governed by any distribution from the ambiguity set $\mathcal{P}^{0}$. The choice $\mathcal{C} = \left\{ {{\mathbf{ξ}} \in {\mathbb{R}}^{T}}:{{\prod_{t = 1}^{T}\xi_{t}} \geq \gamma} \right\}$ allows us to approximate the right-sided Chebyshev bound $\text{R}(\gamma)$. For this special case, the bound of Marshall and Olkin has the analytical solution

which follows from \[4, Theorem 6.1\]. By construction, ${\text{R}^{\text{MO}}(\gamma)} \geq {\text{R}(\gamma)}$ since $\mathcal{P} \subset \mathcal{P}^{0}$. Note that $\text{R}^{\text{MO}}(\gamma)$ coincides with our relaxed Chebyshev bound $\text{R}^{\prime}(\gamma)$ for $\gamma \geq \left( {\mu + \frac{\sigma^{2}\theta}{T\mu}} \right)^{T}$, see Theorem 5.2 ‣ 5 Covariance Bounds ‣ Chebyshev Inequalities for Products of Random Variables"). Thus, $\text{R}^{\text{MO}}(\gamma)$ also coincides with our right-sided Chebyshev bound $\text{R}(\gamma)$ for large values of $\gamma$, see Proposition 5.1. Note that the bound of Marshall and Olkin cannot be used to approximate our left-sided Chebyshev bound $\text{L}(\gamma)$ since the complement of $\mathcal{C}$ fails to be convex.

Vandenberghe et al. derive a semidefinite program that provides a tight upper bound on the probability that $\overset{\sim}{\mathbf{ξ}} \in \mathcal{C}$ for a (not necessarily convex) set $\mathcal{C} = \left\{ {{\mathbf{ξ}} \in {\mathbb{R}}^{T}}:{{{{{\mathbf{ξ}}^{\intercal}{\mathbf{A}}_{i}{\mathbf{ξ}}} + {2{\mathbf{b}}_{i}^{\intercal}{\mathbf{ξ}}} + c_{i}} < {0{\forall i}} = 1},{\ldots,m}} \right\}$, assuming that the random vector $\overset{\sim}{\mathbf{ξ}}$ can be governed by any distribution from the ambiguity set $\mathcal{P}^{0}$. Employing a second-order Taylor approximation of $\prod_{t = 1}^{T}\xi_{t}$ around $\mu\mathbf{1}$,

we can derive an approximate right-sided Chebyshev bound ${\text{R}^{\text{VBC}}(\gamma)} = {\sup_{{\mathbb{P}} \in \mathcal{P}^{0}}{{\mathbb{P}}\left( {\overset{\sim}{\mathbf{ξ}} \in \mathcal{C}} \right)}}$ by replacing the product $\prod_{t = 1}^{T}\xi_{t}$ with its Taylor approximation in the definition of the set $\mathcal{C}$:

A similar approximation $\text{L}^{\text{VBC}}(\gamma)$ can be derived for our left-sided Chebyshev bound $\text{L}(\gamma)$ by considering the strict complement of $\mathcal{C}$. Note that $\text{R}^{\text{VBC}}(\gamma)$ and $\text{L}^{\text{VBC}}(\gamma)$ can over- or underestimate our bounds $\text{R}(\gamma)$ and $\text{L}(\gamma)$ due to the use of the Taylor approximation.

Figure 3: Comparison of the left-sided (left) and right-sided (right) Chebyshev bounds for the products of T = 5 (top) and T = 10 (bottom) random variables with μ = 1 and ρ = 0. The solid lines with squares, the dashed lines with triangles and the dotted lines with circles represent our bounds, the VBC bounds and the MO bounds, respectively. From bottom to top, the blue, red and green lines correspond to σ = 0.2, 0.3 and 0.4 (left) and σ = 0.4, 0.5 and 0.6 (right), respectively.

Figure 3 compares our Chebyshev bounds $\text{L}(\gamma)$ and $\text{R}(\gamma)$ with the approximate bounds $\text{L}^{\text{VBC}}(\gamma)$ and $\text{R}^{\text{VBC}}(\gamma)$ ('VBC bounds') as well as $\text{R}^{\text{MO}}(\gamma)$ ('MO bound'). As expected, the VBC bounds can over- and underestimate our bounds $\text{L}(\gamma)$ and $\text{R}(\gamma)$, whereas the MO bound consistently overestimates $\text{R}(\gamma)$. Moreover, the MO bound coincides with our right-sided Chebyshev bound for large values of $\gamma$. The quality of both approximations deteriorates with increasing $\sigma$ and decreasing $\gamma$. Interestingly, the VBC bound deterioates with increasing numbers of random variables, whereas the MO bound improves with increasing $T$. The figure shows that both approximate bounds can misestimate the bounds $\text{L}(\gamma)$ and $\text{R}(\gamma)$ substantially.

Number of random variables T

Table 2: Runtimes (secs) required to calculate the Chebyshev bounds. Each runtime is averaged over 10 instances with randomly selected μ, σ and γ, and it includes the calculation of both the left-sided and the right-sided bounds.

The MO bound has an analytical solution and can therefore be computed in negligible time. In contrast, the VBC bounds and our bounds require the solution of semidefinite programs with two LMIs of size $\mathcal{O}\left( T^{2} \right)$. Table 2 compares the computation times of both bounds for products of different size $T$ on a computer with a 3.40GHz i7 CPU and 16GB RAM. While both bounds can be computed within seconds, the VBC bounds require significantly less runtime than our bounds. We attribute this to the LMI reformulations of the polynomial constraints in Theorems 3.1 ‣ 3 Left-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables") and 4.1 ‣ 4 Right-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables"), which seem to lack structure that can be exploited by SDPT3.

Figure 4: Comparison of the right-sided Chebyshev bounds R (γ) (solid lines with squares), R′ (γ) (dashed lines with diamonds) and RMO (γ) (dotted lines with circles) with μ = 1 and ρ = 0. From bottom to top, the blue, red and green lines correspond to σ = 0.4, 0.5 and 0.6 in the left graph (with T = 5 fixed) and to T = 3, 5 and 7 in the right graph (with σ = 0.5 fixed), respectively.

Figure 4 compares the right-sided Chebyshev bound $\text{R}(\gamma)$ with the relaxed right-sided bound $\text{R}^{\prime}(\gamma)$ and the MO bound $\text{R}^{\text{MO}}(\gamma)$. The figure illustrates that $\text{R}^{\text{MO}}(\gamma)$ coincides with $\text{R}^{\prime}(\gamma)$ for $\gamma \geq \left( {\mu + \frac{\sigma^{2}\theta}{T\mu}} \right)^{T}$, and subsequently both bounds coincide with $\text{R}(\gamma)$ for large values of $\gamma$. The gaps between the bounds increase with larger variances $\sigma^{2}$, and they decrease with larger numbers of random variables $T$.

### Case Study: Financial Risk Management

Consider an investor who allocates a limited budget to a fixed pool of $n$ assets over a time horizon of $T$ periods. We denote by ${\overset{\sim}{r}}_{t,i} \geq {- 1}$, $t = {1,\ldots,T}$ and $i = {1,\ldots,n}$, the relative price change of asset $i$ between periods $t$ and $t + 1$. We assume that the investor pursues a fixed-mix (or constant proportions) strategy which rebalances the portfolio composition to a pre-selected set of weights ${\mathbf{w}} \in \mathcal{W} = \left\{ {{\mathbf{z}} \in {\mathbb{R}}_{+}^{n}}:{{\mathbf{e}^{\intercal}{\mathbf{z}}} = 1} \right\}$ at the beginning of each period. Note that despite being memoryless, fixed-mix strategies are dynamic since they recapitalize those assets whose returns were below average ('buy low') and divest assets whose returns were above average ('sell high'). Fixed-mix strategies generalize the well-known $\left. 1/N \right.$-portfolio, and they have received significant attention among both academics and practitioners.

We assume that the investor assesses the fixed-mix strategy $\mathbf{w}$ in view of the value-at-risk of the portfolio's terminal wealth, which is defined as

Here, the asset returns ${\overset{\sim}{\mathbf{r}}}_{t} = \left( {\overset{\sim}{r}}_{t,i} \right)_{i = 1}^{n}$ are governed by the probability distribution $\mathbb{P}$, and $\epsilon$ is a pre-specified parameter that reflects the investor's risk tolerance.

Calculating the value-at-risk of a portfolio's terminal wealth requires perfect knowledge of the joint asset return distribution $\mathbb{P}$, which is unavailable in practice. Following, we will assume that it is only known that the asset returns $\left( {\overset{\sim}{\mathbf{r}}}_{t} \right)_{t = 1}^{T}$ follow a weak-sense white noise process with mean $\mathbf{μ}$ and variance $\mathbf{\Sigma}$, that is, the asset returns are serially uncorrelated and have period-wise identical first and second-order moments. In that case, the wealth evolution $\left( {\overset{\sim}{\xi}}_{t} \right)_{t = 1}^{T} = \left( {1 + {{\mathbf{w}}^{\intercal}{\overset{\sim}{\mathbf{r}}}_{t}}} \right)_{t = 1}^{T}$ also follows a weak-sense stochastic process governed by a distribution ${\mathbb{P}}_{\mathbf{w}}$ supported on ${\mathbb{R}}_{+}^{T}$, under which the ${\overset{\sim}{\xi}}_{t}$ have mean ${\mathbf{w}}^{\intercal}{\mathbf{μ}}$ and variance ${\mathbf{w}}^{\intercal}\mathbf{\Sigma}{\mathbf{w}}$ and are serially uncorrelated. We denote the set of all these distributions by $\mathcal{P}_{\mathbf{w}}$. In this setting, an ambiguity-averse investor may assess the fixed-mix strategy $\mathbf{w}$ in view of the *worst-case* value-at-risk of the portfolio's terminal wealth over all distributions ${\mathbb{P}}_{\mathbf{w}} \in \mathcal{P}_{\mathbf{w}}$:

In, the worst-case value-at-risk of the portfolio's terminal wealth is replaced with a quadratic approximation. The Chebyshev bounds proposed in this paper allow us to calculate the worst-case value-at-risk exactly without resorting to any approximation. Indeed, one verifies that

where we have made explicit the dependence of the left-sided Chebyshev bound $L$ on the mean ${\mathbf{w}}^{\intercal}{\mathbf{μ}}$ and the variance ${\mathbf{w}}^{\intercal}\mathbf{\Sigma}{\mathbf{w}}$ of the wealth evolution $\left( {\overset{\sim}{\xi}}_{t} \right)_{t = 1}^{T}$. Since $L$ is monotonically non-decreasing in $\gamma$, the last expression can be evaluated efficiently through bisection on $\gamma$.

Figure 5: Wort-case value-at-risk of the growth rates of the minimum-variance (left) and maximum-expectation (right) portfolios for different investment horizons T and risk tolerances ϵ.

Figure 5 reports the worst-case value-at-risk of two portfolios over different time horizons $T$, where $\mathbf{μ}$ and $\mathbf{\Sigma}$ are calibrated to the 2003--2012 period of Fama and French's 10 Industry Portfolios data set.^22^2See http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data library.html. The minimum-variance portfolio (left graph) corresponds to the weight vector ${\mathbf{w}} \in \mathcal{W}$ that minimizes ${\mathbf{w}}^{\intercal}\mathbf{\Sigma}{\mathbf{w}}$, whereas the maximum-expectation portfolio (right graph) invests all wealth into the asset $i$ with the highest expected return $\mu_{i}$. To facilitate a fair comparison among different time horizons, the graphs report the growth rates of the portfolios, that is, the logarithms of the terminal wealth, divided by the number of investment periods $T$. As expected, the minimum-variance portfolio is less risky than the maximum-expectation portfolio, and the risk of both portfolios tends to decrease when the investment horizon $T$ grows. Interestingly, however, the risk of the maximum-expectation portfolio *increases* with large $T$ for low risk tolerances $\epsilon \lesssim 0.15$. This seemingly counter-intuitive effect is explained by Theorem 3.2 ‣ 3 Left-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables"), which states that the wealth evolution $\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}$ is absorbed at $0$ for large investment horizons $T$.

In addition to *evaluating* the worst-case value-at-risk of a pre-selected portfolio $\mathbf{w}$, an investor often seeks to determine a portfolio ${\mathbf{w}}^{\star}$ that *optimizes* the worst-case value-at-risk. The search for optimal portfolios is greatly simplified by the observation that there is always a portfolio ${\mathbf{w}}^{\star}$ on the mean-variance efficient frontier that maximizes $\text{WVaR}_{\epsilon}({\mathbf{w}})$ over (subsets of) $\mathcal{W}$. Indeed, Theorem 5.1 ‣ 5 Covariance Bounds ‣ Chebyshev Inequalities for Products of Random Variables") implies that ${\text{L}\left( \gamma;{{\mathbf{w}}^{\intercal}{\mathbf{μ}}},{{\mathbf{w}}^{\intercal}\mathbf{\Sigma}{\mathbf{w}}} \right)} = {\text{L}^{\prime}\left( \gamma;{{\mathbf{w}}^{\intercal}{\mathbf{μ}}},{{\mathbf{w}}^{\intercal}\mathbf{\Sigma}{\mathbf{w}}} \right)}$, and one readily verifies that $\text{L}^{\prime}\left( \gamma;{{\mathbf{w}}^{\intercal}{\mathbf{μ}}},{{\mathbf{w}}^{\intercal}\mathbf{\Sigma}{\mathbf{w}}} \right)$ is non-decreasing in both $\gamma$ and ${\mathbf{w}}^{\intercal}\mathbf{\Sigma}{\mathbf{w}}$. This implies that

for two portfolios $\mathbf{w}$ and ${\mathbf{w}}^{\prime}$ that satisfy ${{\mathbf{w}}^{\intercal}{\mathbf{μ}}} = {{\mathbf{w}}^{\prime}{}_{}^{}}$ and ${{\mathbf{w}}^{\intercal}\mathbf{\Sigma}{\mathbf{w}}} \geq {{\mathbf{w}}^{\prime}{}_{}^{}{\mathbf{w}}^{\prime}}$. We thus conclude that among all portfolios ${\mathbf{w}} \in \mathcal{W}$ that achieve the same mean return ${\mathbf{w}}^{\intercal}{\mathbf{μ}}$, the portfolio with smallest variance ${\mathbf{w}}^{\intercal}\mathbf{\Sigma}{\mathbf{w}}$ provides the best worst-case value-at-risk. We can therefore identify an optimal portfolio through a one-dimensional line search over the mean-variance efficient frontier.
