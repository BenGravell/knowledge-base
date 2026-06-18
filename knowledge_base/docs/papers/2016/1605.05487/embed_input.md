<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Chebyshev Inequalities for Products of Random Variables

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We derive sharp probability bounds on the tails of a product of symmetric non-negative random variables using only information about their first two moments. If the covariance matrix of the random variables is known exactly, these bounds can be computed numerically using semidefinite programming. If only an upper bound on the covariance matrix is available, the probability bounds on the right tails can be evaluated analytically. The bounds under precise and imprecise covariance information coincide for all left tails as well as for all right tails corresponding to quantiles that are either sufficiently small or sufficiently large. We also prove that all left probability bounds reduce to the trivial bound 1 if the number of random variables in the product exceeds an explicit threshold. Thus, in the worst case, the weak-sense geometric random walk defined through the running product of the random variables is absorbed at 0 with certainty as soon as time exceeds the given threshold. The techniques devised for constructing Chebyshev bounds for products can also be used to derive Chebyshev bounds for sums, maxima and minima of non-negative random variables.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The classical one-sided Chebyshev inequality for a random variable $\overset{\sim}{\xi}$ with mean $\mu$ and variance $\sigma^{2}$ can be represented as

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This inequality is sharp. Indeed, for $\gamma \neq \mu$ it is binding under the two-point distribution

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the degenerate case $\gamma = \mu$, the inequality is still sharp because the distributions

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

If we have the extra information that the random variable $\overset{\sim}{\xi}$ is non-negative (and without much loss of generality that $\mu > 0$), then one can strengthen the Chebyshev inequality to

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

see, e.g.,. The extremal distributions are supported on the non-negative real line if either $\gamma \geq {\mu + \left. \sigma^{2}/\mu \right.} > \mu$ or if $\gamma < \mu$. Thus, they certify the sharpness of in the respective parameter domains. For $\mu \leq \gamma < {\mu + \left. \sigma^{2}/\mu \right.}$ the Chebyshev inequality for non-negative random variables reduces in fact to the classical Markov inequality ${{\mathbb{P}}\left( {\overset{\sim}{\xi} \geq \gamma} \right)} \leq \left. \mu/\gamma \right.$. In this Markov regime, the Chebyshev inequality remains sharp because the distributions

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the rest of the paper we consider a sequence of $T$ random variables ${\overset{\sim}{\xi}}_{1},{\overset{\sim}{\xi}}_{2},\ldots,{\overset{\sim}{\xi}}_{T}$ and assume that the first two moments of these random variables are known and permutation symmetric. Specifically, assume that all random variables share the same mean $\mu$ and variance $\sigma^{2}$, respectively, while all pairs of mutually distinct random variables share the same correlation coefficient $\rho$. Thus, the mean vector and the covariance matrix of $\overset{\sim}{\mathbf{ξ}} = \left( {\overset{\sim}{\xi}}_{1},\ldots,{\overset{\sim}{\xi}}_{T} \right)^{\intercal}$ are given by

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

respectively. Throughout the paper we assume that $\sigma > 0$ and ${- \frac{1}{T - 1}} < \rho < 1$. These conditions are necessary and sufficient for the covariance matrix $\mathbf{\Sigma}$ to be strictly positive definite. Note that $\overset{\sim}{\mathbf{ξ}}$ constitutes a weak-sense stationary stochastic process in the sense of.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

This inequality is still sharp due to a projection property of distribution families with compatible first and second moments.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The extremal distributions certifying the sharpness of can therefore be used to construct multivariate extremal distributions of $\overset{\sim}{\mathbf{ξ}}$ certifying the sharpness of. This result may be unexpected. Indeed, if ${\overset{\sim}{\xi}}_{1},\ldots,{\overset{\sim}{\xi}}_{T}$ are independent and identically distributed, then, by the central limit theorem, their sum is approximately normally distributed with mean $T\mu$ and variance $T\sigma^{2}$. In contrast, if ${\overset{\sim}{\xi}}_{1},\ldots,{\overset{\sim}{\xi}}_{T}$ are only known to be uncorrelated with a common mean and variance (but not necessarily independent and identically distributed), then, by the projection theorem, their sum may follow any distribution with mean $T\mu$ and variance $T\sigma^{2}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Assume now that ${\overset{\sim}{\xi}}_{t}$ is non-negative for every $t = {1,\ldots,T}$ (and without much loss of generality that $\mu > 0$). As we will prove in Proposition 2.1 ‣ 2 Optimization Perspective on Chebyshev Inequalities ‣ Chebyshev Inequalities for Products of Random Variables") below, a distribution $\mathbb{P}$ supported on ${\mathbb{R}}_{+}^{T}$ with mean vector $\mathbf{μ}$ and covariance matrix $\mathbf{\Sigma}$ as given in exists iff ${\mu^{2} + {\rho\sigma^{2}}} \geq 0$. We will assume that this condition holds throughout the rest of the paper. In this setting, the generalized Chebyshev inequality applied to the non-negative random variable $\sum_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}$ implies

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Even though the multivariate extension of the univariate Chebyshev inequality can still be shown to be sharp, we are not aware of an elementary proof; see Theorem 6.3 ‣ 6 Extensions ‣ Chebyshev Inequalities for Products of Random Variables") below.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we aim to derive Chebyshev inequalities for products of non-negative random variables. Specifically, we will derive sharp upper bounds on the left and right tail probabilities ${\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \leq \gamma} \right)$ and ${\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \geq \gamma} \right)$, respectively. Products of random variables frequently arise in physics, statistics, finance, number theory and many other branches of science. Indeed, they are at the heart of stochastic models of many complex phenomena. When rocks are crushed, for example, the size of a fragment is multiplied by a random factor (that is smaller than 1) in every single breakup event. Similar multiplicative phenomena explain the distribution of body weights, stock prices, the sizes of biological populations, income, rainfall etc..

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consequently, they are potentially relevant for the many applications in economics and operations research, where geometric Brownian motions are traditionally used to model the prices of assets. An improved understanding of weak-sense geometric random walks may also stimulate new research directions in distributionally robust optimziation and optimal uncertainty quantification.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 1.1 (Chebyshev in Log-Space)", "weight": 1.0} -->

It seems natural to reduce Chebyshev inequalities for products of non-negative random variables to Chebyshev inequalities for their logarithms. Assume thus that the first two moments of the logarithmic random variables ${\overset{\sim}{\eta}}_{t} = {\log{({\overset{\sim}{\xi}}_{t})}}$, $1,\ldots,T$, are known and permutation symmetric. Specifically, denote by $\mu_{\eta}$, $\sigma_{\eta}^{2}$ and $\rho_{\eta}$ the mean, variance and correlation coefficient in log-space. Then, the Chebyshev inequality for sums implies

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 1.1 (Chebyshev in Log-Space)", "weight": 1.0} -->

Note that (7 ‣ 1 Introduction ‣ Chebyshev Inequalities for Products of Random Variables")) is sharp because is sharp. However, there is no one-to-one correspondence between the moments of the original and the logarithmic random variables. Even worse, it is possible that $\mu$ is finite while $\mu_{\eta} = {- \infty}$ (e.g., if $\xi_{t} = 0$ with positive probability), or that $\mu_{\eta}$ is finite while $\mu = {+ \infty}$ (e.g., if ${\overset{\sim}{\xi}}_{t}$ follows a Pareto distribution with unit shape parameter). In this work we focus on the case where the ${\overset{\sim}{\xi}}_{t}$ have known finite first and second moments, and we explicitly allow the event ${\overset{\sim}{\xi}}_{t} = 0$ to have positive probability.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 1.1 (Chebyshev in Log-Space)", "weight": 1.0} -->

This assumption can be crucial for truthfully capturing the bankruptcy risks in financial applications, for instance.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 1.1 (Chebyshev in Log-Space)", "weight": 1.0} -->

The starting point of this paper is the intriguing observation that modern optimization theory provides powerful tools for constructing and analyzing probability inequalities. Assume for instance that we aim to find a sharp probability inequality for a target event characterized through finitely many polynomial inequalities on a random vector $\overset{\sim}{\mathbf{ξ}}$. Assume further that the desired inequality should hold for all distributions of $\overset{\sim}{\mathbf{ξ}}$ satisfying finitely many polynomial support and moment constraints. In the special case of the Chebyshev inequality, the target event corresponds to the set $\left\{ {\xi \in {\mathbb{R}}}:{\xi \geq \gamma} \right\}$, while the relevant distribution family corresponds to the class of all distributions on $\mathbb{R}$ with mean $\mu$ and variance $\sigma^{2}$. Constructing the desired probability inequality is thus tantamount to maximizing the probability of the target event over the given distribution family. This leads to a generalized moment problem over probability measures.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 1.1 (Chebyshev in Log-Space)", "weight": 1.0} -->

Under a mild regularity condition, this moment problem admits a strong dual linear program subject to polynomially parameterized semi-infinite constraints. A key insight of is that this dual problem can be approximated systematically by tractable semidefinite programs. The resulting approximations are safe (i.e., they are guaranteed to provide upper bounds on the probability of the semialgebraic event). Moreover, these approximations are always tight in the univariate case but generically loose in the multivariate setting.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 1.1 (Chebyshev in Log-Space)", "weight": 1.0} -->

Stronger statements are available for probability inequalities that rely exclusively on first- and second-order moments. Specifically, if the support of the random vector $\overset{\sim}{\mathbf{ξ}}$ is unrestricted, the best upper bound on the probability of a convex target event is given by $\left. 1/\left( {1 + d^{2}} \right) \right.$, where $d$ represents the distance of the target event from the mean vector of $\overset{\sim}{\mathbf{ξ}}$ under the Mahalanobis norm induced by the covariance matrix of $\overset{\sim}{\mathbf{ξ}}$. More generally, if the target event constitutes a union of finitely many convex sets, over each of which convex quadratic optimization problems can be solved in polynomial time, then the best Chebyshev bound can be computed by an efficient algorithm reminiscent of the ellipsoid method of convex optimization.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 1.1 (Chebyshev in Log-Space)", "weight": 1.0} -->

Recently it has been observed that if the target event is defined by quadratic inequalities, the best Chebyshev bound coincides exactly with the optimal value of a single tractable semidefinite program. In spite of these encouraging results, the computation of Chebyshev bounds becomes hard in the presence of support constraints. Specifically, if $\overset{\sim}{\mathbf{ξ}}$ is supported on the non-negative orthant, it is already NP-hard to find sharp Chebyshev bounds for convex polyhedral target events.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 1.1 (Chebyshev in Log-Space)", "weight": 1.0} -->

For a random vector $\overset{\sim}{\mathbf{ξ}}$ with zero mean and unrestricted support, the above methods have been used to derive a sharp Chebyshev bound on ${\mathbb{P}}\left( {{{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \geq 1},{{\overset{\sim}{\xi}}_{t} > {0{\forall t}}}} \right)$, which is expressed in terms of the solution of a tractable convex program. As the ${\overset{\sim}{\xi}}_{t}$ are allowed to adopt negative values, however, we believe that the practical relevance of this bound is limited.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 1.1 (Chebyshev in Log-Space)", "weight": 1.0} -->

Note that the second target event $\left\{ {{\mathbf{ξ}} \in {\mathbb{R}}_{+}^{T}}:{{\prod_{t = 1}^{T}\xi_{t}} \leq \gamma} \right\}$ is neither convex nor representable as a finite union of convex sets, nor representable through finitely many quadratic constraints in $\mathbf{ξ}$. Thus, none of the existing techniques could be used to bound its probability even if there were no support constraints. As support constraints generically lead to intractability, we focus here on the special case where the first- and second-order moments are permutation-symmetric.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 1.1 (Chebyshev in Log-Space)", "weight": 1.0} -->

The main results of this paper can be summarized as follows.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 1.1 (Chebyshev in Log-Space)", "weight": 1.0} -->

If the distribution $\mathbb{P}$ of the non-negative random variables has mean $\mathbf{μ}$ and covariance matrix $\mathbf{\Sigma}$ as given, then the sharp upper Chebyshev bounds on ${\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \geq \gamma} \right)$ and ${\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \leq \gamma} \right)$ can both be expressed as the optimal values of explicit semidefinite programs, which are amenable to efficient numerical solution via interior point algorithms.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 1.1 (Chebyshev in Log-Space)", "weight": 1.0} -->

If the distribution $\mathbb{P}$ of the non-negative random variables has mean $\mathbf{μ}$ and a covariance matrix bounded above by $\mathbf{\Sigma}$ in a positive semidefinite sense, then we obtain an explicit analytical formula for the sharp upper Chebyshev bound on ${\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \geq \gamma} \right)$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 1.1 (Chebyshev in Log-Space)", "weight": 1.0} -->

The Chebyshev bound in (ii) coincides with the corresponding bound in (i) for all values of $\gamma$ that are either sufficiently small or sufficiently large. For intermediate values of $\gamma$ the numerical bound in (i) may be strictly smaller than the analytical bound in (ii).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 1.1 (Chebyshev in Log-Space)", "weight": 1.0} -->

If the distribution $\mathbb{P}$ of the non-negative random variables has mean $\mathbf{μ}$ and a covariance matrix bounded above by $\mathbf{\Sigma}$ in a positive semidefinite sense, then the sharp upper Chebyshev bound on ${\mathbb{P}}\left( {{\prod_{t = 1}^{T}{\overset{\sim}{\xi}}_{t}} \leq \gamma} \right)$ coincides with the corresponding numerical bound in (i). Thus, there is a distribution that makes this bound sharp and has covariance matrix $\mathbf{\Sigma}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 1.1 (Chebyshev in Log-Space)", "weight": 1.0} -->

The techniques devised for constructing Chebyshev bounds for products of random variables can also be used to derive Chebyshev bounds on sums, maxima and minima (and possibly other permutation-symmetric functionals) of non-negative random variables.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1.1 (Chebyshev in Log-Space)", "weight": 1.0} -->

The rest of the paper is structured as follows. In Section 2 we formalize the connection between probability inequalities and convex optimization. Left- and right-sided Chebyshev inequalities for products of random variables are then derived in Sections 3 and 4, respectively, while generalized Chebyshev inequalities that account for imprecise knowledge of the covariances are discussed in Section 5. Chebyshev inequalities for other permutation-symmetric functionals of the random variables are presented in Section 6, and examples are given in Section 7.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Optimization Perspective on Chebyshev Inequalities", "weight": 1.0} -->

To analyze probability bounds using tools from optimization, we first introduce an ambiguity set $\mathcal{P}$, that is, a family of distributions for which the desired probability bound should hold. In this paper we mainly focus on the ambiguity set of all distributions supported on ${\mathbb{R}}_{+}^{T}$ that share the permutation-symmetric mean and covariance matrix defined, that is, we set

<!-- chunk {"id": "body-0033", "role": "body", "section": "Optimization Perspective on Chebyshev Inequalities", "weight": 1.0} -->

We highlight that $\mathcal{P}$ is characterized by only four parameters: $T,\mu,\sigma,\rho$. Without much loss of generality, we assume henceforth that $\mu > 0$, $\sigma > 0$ and ${- \frac{1}{T - 1}} < \rho < 1$. The last two conditions are equivalent to $\mathbf{\Sigma} \succ \mathbf{0}$. To rule out trivial special cases, we further restrict attention to $T \geq 2$. However, all of these conditions do not yet guarantee that $\mathcal{P}$ is non-empty. Proposition 2.1 ‣ 2 Optimization Perspective on Chebyshev Inequalities ‣ Chebyshev Inequalities for Products of Random Variables") below provides a necessary and sufficient condition for the non-emptiness of $\mathcal{P}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Step 2", "weight": 1.0} -->

To check that $m_{1}^{2} \leq m_{2} \leq {Tm_{1}^{2}}$, we first use the definition of $m_{2}$ and the assumption that $\rho < 1$ to verify that $m_{1}^{2} \leq m_{2}$. The other inequality holds if and only if

<!-- chunk {"id": "body-0035", "role": "body", "section": "Step 2", "weight": 1.0} -->

where the first and second equivalence follow from the definitions of $m_{2}$ and $m_{1}$, respectively. We now show that the last inequality holds by distinguishing the cases $\rho > 0$, $\rho = 0$ and $\rho < 0$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Step 2", "weight": 1.0} -->

For $\rho > 0$, we observe that the expression $\sqrt{\left( {1 + {\left( {T - 1} \right)\rho}} \right)\left( {1 - p} \right)} - \sqrt{1 - \rho}$ in evaluates to 0 for $p = \frac{T\rho}{1 + {\left( {T - 1} \right)\rho}}$ and that it is decreasing in $p$. Since ${\mu\sqrt{pT}} \geq 0$ by construction, we thus conclude that the last inequality in holds, and hence $m_{2} \leq {Tm_{1}^{2}}$ when $\rho \geq 0$. In combination with and, the above inequality ensures that $m_{2} \leq {Tm_{1}^{2}}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Step 2", "weight": 1.0} -->

where the two implications follow from algebraic manipulations and the fact that $\sqrt{p} \geq \frac{1 - \sqrt{1 - p}}{\sqrt{p}}$ for $p \in \lbrack 0,1\rbrack$, respectively. One readily verifies that the last inequality is satisfied by $p = \frac{T\mu^{2}}{{T\mu^{2}} + \sigma^{2}}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Step 2", "weight": 1.0} -->

For $\rho < 0$, substituting $p$ in with its definition from yields

<!-- chunk {"id": "body-0039", "role": "body", "section": "Step 2", "weight": 1.0} -->

where the equalities follow from direct calculations and the inequality holds since ${\mu^{2} + {\rho\sigma^{2}}} \geq 0$. We thus conclude that $m_{2} \leq {Tm_{1}^{2}}$ whenever $\rho < 0$ as postulated.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Step 3", "weight": 1.0} -->

We show that our choice of $m_{1},m_{2}$ and $z$ meets the requirements (i') and (ii'), regardless of the value of $p$. First, a direct calculation shows that requirement (i') follows from the definitions of $m_{1}$ and $z$. Next, the first requirement in (ii') follows from

<!-- chunk {"id": "body-0041", "role": "body", "section": "Step 3", "weight": 1.0} -->

where the first equality holds since the requirement (i') is met, and the fourth equality follows from the definitions of $m_{1}$, $m_{2}$ and $z$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Step 3", "weight": 1.0} -->

Finally, to prove the second requirement in (ii'), we first observe that

<!-- chunk {"id": "body-0043", "role": "body", "section": "Step 3", "weight": 1.0} -->

where the second equality follows from the definition of $m_{2}$. Note that the term on the left (right) side of this equality constitutes the difference between the left (right) sides of the requirements in (ii'). The second requirement in (ii') and the claim thus follow.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Step 3", "weight": 1.0} -->

In order to establish Chebyshev bounds for products of random variables, we will formulate generalized moment problems that optimize over the probability measures in the ambiguity set $\mathcal{P}$. We can then leverage powerful duality results from convex optimization to reformulate these moment problems as explicit semidefinite programs that are amenable to efficient solution via interior point methods. The *weak duality* principle, which holds true for every optimization problem, states that the optimal value of a (primal) minimization problem is bounded from below by the optimal value of its associated dual (maximization) problem. To establish tight probability bounds, we need to invoke the *strong duality* principle, which states that under certain conditions the optimal values of the primal and dual optimization problems coincide. In our setting, strong duality holds whenever ${\mu^{2} + {\rho\sigma^{2}}} > 0$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Step 1", "weight": 1.0} -->

We distinguish the cases $\rho < 0$ and $\rho \geq 0$. For $\rho < 0$, one readily verifies that the choice of $p$, $x$, $y$ and $z$ in the proof of Proposition 2.1 ‣ 2 Optimization Perspective on Chebyshev Inequalities ‣ Chebyshev Inequalities for Products of Random Variables") satisfies $x > y > 0$, $z > 0$, $p \in $ and ${x + {\left( {T - 1} \right)y}} > {Tz}$ by construction. Moreover, these inequalities are also satisfied strictly for $\rho \geq 0$ if we replace $p$ in with any value from the open interval $(0,p)$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Step 2", "weight": 1.0} -->

Note that the covariance matrix of any distribution in $\mathcal{P}\left( {\mathbf{μ}}^{\epsilon},\mathbf{\Omega}^{\epsilon} \right)$ is positive definite for small $\epsilon$ since $\mathbf{\Sigma} \succ \mathbf{0}$ and the eigenvalues are continuous functions of the second-order moment matrix. In the following, we construct a discrete distribution ${\mathbb{P}}^{\epsilon} \in {\mathcal{P}\left( {\mathbf{μ}}^{\epsilon},\mathbf{\Omega}^{\epsilon} \right)}$ with

<!-- chunk {"id": "body-0047", "role": "body", "section": "Step 2", "weight": 1.0} -->

where $p$ is the constant chosen in Step 1.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Step 2", "weight": 1.0} -->

The moment function $\mathbf{F}$ is continuously differentiable by construction.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Step 2", "weight": 1.0} -->

For ease of exposition, we divide the first $T^{2}$ and the last $T$ columns of $\mathbf{J}$ by $\frac{p}{T}$ and $1 - p$, respectively, and we divide the rows corresponding to the first requirement in (ii) by 2. We then obtain

<!-- chunk {"id": "body-0050", "role": "body", "section": "Step 2", "weight": 1.0} -->

Here, the indices $s$ and $t$, $1 \leq s < t \leq T$, encode the row and the index $j$ refers to the column of $\mathbf{C}^{i}$, respectively. The matrix $\mathbf{C}^{T + 1}$ is defined analogously with $x$ and $y$ replaced by $z$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Step 2", "weight": 1.0} -->

Subtracting the two equations implies that ${\left( {x - y} \right)\left( {v_{1} - c_{12}} \right)} = 0$, which in turn yields $v_{1} = c_{12}$ since $x \neq y$. Generalizing this observation to the $t$th columns in each pair of column blocks $s$ and $t$, we find that all $v_{t}$ and $c_{st}$ must be equal to a single variable $v$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Step 2", "weight": 1.0} -->

Next, consider the $\left( {T^{2} + 1} \right)$th and $\left( {T^{2} + 2} \right)$th columns (i.e., the first two elements of the last column block) of the equation ${\left( {\mathbf{m}}^{\intercal},{\mathbf{v}}^{\intercal},{\mathbf{c}}^{\intercal} \right)\mathbf{J}} = \mathbf{0}^{\intercal}$, which are equivalent to

<!-- chunk {"id": "body-0053", "role": "body", "section": "Step 2", "weight": 1.0} -->

However, since $v_{t} = c_{st} = v$ for all $s$ and $t$, we conclude that $m_{1} = m_{2}$. Again, generalizing this observation to each pair of columns in the last column block, we can identify all $m_{t}$ by a single number $m$. Replacing $v_{t}$ and $c_{st}$ by $v$ and $m_{t}$ by $m$, the previous two equations simplify to

<!-- chunk {"id": "body-0054", "role": "body", "section": "Step 2", "weight": 1.0} -->

and we conclude that $m = v = 0$ since we established earlier that ${x + {\left( {T - 1} \right)y}} \neq {Tz}$. Hence, the Jacobian $\mathbf{J}$ indeed has full row rank, which concludes Step 2.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Step 3", "weight": 1.0} -->

Theorem 2.1 ‣ Step 3: ‣ 2 Optimization Perspective on Chebyshev Inequalities ‣ Chebyshev Inequalities for Products of Random Variables") will allow us to use the strong duality theorem of \[27, Proposition 3.4\], which states that a linear optimization problem over the distributions in $\mathcal{P}$ has the same optimal value as its associated dual problem. In the remainder of the paper, we will make extensive use of this insight, and we therefore assume from now on that ${\mu^{2} + {\rho\sigma^{2}}} > 0$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Left-Sided Chebyshev Bounds", "weight": 1.0} -->

In this section we study *left-sided Chebyshev bounds* of the form

<!-- chunk {"id": "body-0057", "role": "body", "section": "Left-Sided Chebyshev Bounds", "weight": 1.0} -->

where the ambiguity set $\mathcal{P}$ is defined. We begin with the main result of this section.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Step 1", "weight": 1.0} -->

Keeping the scenario probabilities as well as the scenario-wise arithmetic and quadratic means constant, we first replace each ${\mathbf{ξ}}^{k}$ with a minimizer of the problem

<!-- chunk {"id": "body-0059", "role": "body", "section": "Step 1", "weight": 1.0} -->

which depends parametrically on $m_{1}^{k}$ and $m_{2}^{k}$. By Lemma 3.5 (i) below, problem is indeed solvable for every $k \in \mathcal{K}$. The new distribution with updated scenarios still belongs to $\mathcal{P}$ because we did not change $p_{k}$, $m_{1}^{k}$ and $m_{2}^{k}$, implying that the moment conditions remain valid. To gain a better understanding of the updated distribution, we define the disjoint index sets

<!-- chunk {"id": "body-0060", "role": "body", "section": "Step 1", "weight": 1.0} -->

and note that $\mathcal{K} = {\mathcal{K}^{+} \cup \mathcal{K}^{-}}$ by Lemma 3.5 (i) below. Lemma 3.5 (ii) further implies that

<!-- chunk {"id": "body-0061", "role": "body", "section": "Step 2", "weight": 1.0} -->

If there exists a non-absorbing scenario $i \in \mathcal{K}^{-}$, we will alter both the scenarios and their quadratic means to make scenario $i$ absorbing, while ensuring that all scenarios $k \in \mathcal{K}^{+}$ remain absorbing. To achieve this, we consider the following family of quadratic means parameterized in $\lambda \in \lbrack 0,1\rbrack$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Step 2", "weight": 1.0} -->

By construction, $p_{k}$, $m_{1}^{k}$ and $m_{2}^{k} = {m_{2}^{k}(\lambda)}$ satisfy the moment conditions for every $\lambda \in \lbrack 0,1\rbrack$. As in Step 1, the scenario ${\mathbf{ξ}}^{k}(\lambda)$ is then chosen to be a minimizer of problem with inputs $m_{1}^{k}$ and $m_{2}^{k} = {m_{2}^{k}(\lambda)}$. However, could fail to be solvable for $\lambda \lesssim 1$, in which case the proposed construction would fail. Indeed, Lemma 3.5 (i) shows that is only solvable when $1 \leq \left. {m_{2}^{k}(\lambda)}/\left( m_{1}^{k} \right)^{2} \right. \leq T$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Step 2", "weight": 1.0} -->

In the remainder we will demonstrate that there is $\lambda^{\star} \in $ such that ${\mathbf{ξ}}^{k}\left( \lambda^{\star} \right)$ exists for every $k \in \mathcal{K}$ and such that all scenarios $k \in {\mathcal{K}^{+} \cup \left\{ i \right\}}$ are absorbing.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Step 2", "weight": 1.0} -->

Subtracting (37d) from (37c) and dividing the difference by (37c) yields

<!-- chunk {"id": "body-0065", "role": "body", "section": "Step 2", "weight": 1.0} -->

where the inequality follows from the assumption that $T > {\frac{\mu^{2} + \sigma^{2}}{\left( {1 - \rho} \right)\sigma^{2}} + 1}$. Multiplying both sides of the inequality by $\frac{T - 1}{T}$ and partitioning $\mathcal{K}$ into $\mathcal{K}^{+}$ and $\mathcal{K}^{-}$ further reveals that

<!-- chunk {"id": "body-0066", "role": "body", "section": "Step 2", "weight": 1.0} -->

The expression on the left hand side of the above inequality represents a weighted average of the fractions $\left. \left( {m_{2}^{k} - \left( m_{1}^{k} \right)^{2}} \right)/m_{2}^{k} \right.$ across all $k \in \mathcal{K}$. Recall from (39a) and (39b) that the fractions indexed by $k \in \mathcal{K}^{+}$ are larger or equal to $\left. 1/T \right.$, while those indexed by $k \in \mathcal{K}^{-}$ are strictly smaller than $\left. 1/T \right.$. The inequality asserts that the fractions corresponding to $k \in \mathcal{K}^{+}$ dominate those corresponding to $k \in \mathcal{K}^{-}$. Thus, remains valid if we replace $\mathcal{K}^{-}$ with $\left\{ i \right\}$, that is,

<!-- chunk {"id": "body-0067", "role": "body", "section": "Step 2", "weight": 1.0} -->

Using the notation introduced, the inequality can be reformulated as

<!-- chunk {"id": "body-0068", "role": "body", "section": "Step 2", "weight": 1.0} -->

As $i \in \mathcal{K}^{-}$, the relation (39b) further implies that

<!-- chunk {"id": "body-0069", "role": "body", "section": "Step 2", "weight": 1.0} -->

The intermediate value theorem then guarantees the existence of $\lambda^{\star} \in $ with

<!-- chunk {"id": "body-0070", "role": "body", "section": "Step 2", "weight": 1.0} -->

\leq T$ for every $k \in {\mathcal{K}^{+} \cup \left\{ i \right\}}$, which implies via Lemma 3.5 (ii) that the corresponding scenarios ${\mathbf{ξ}}^{k}\left( \lambda^{\star} \right)$ are absorbing. Thus, by replacing ${\mathbf{ξ}}^{k}$ with ${\mathbf{ξ}}^{k}\left( \lambda^{\star} \right)$ in we obtain a new distribution ${\mathbb{P}} \in \mathcal{P}$ with more absorbing scenarios. As the total number of scenarios is finite, we can repeat Step 2 finitely many times to construct a distribution ${\mathbb{P}} \in \mathcal{P}$ that has only absorbing scenarios. Thus, the claim follows.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Step 2", "weight": 1.0} -->

The proof of Theorem 3.2 ‣ 3 Left-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables") relies on the following auxiliary result.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Right-Sided Chebyshev Bounds", "weight": 1.0} -->

We now study *right-sided Chebyshev bounds* of the form

<!-- chunk {"id": "body-0073", "role": "body", "section": "Right-Sided Chebyshev Bounds", "weight": 1.0} -->

where the ambiguity set $\mathcal{P}$ is defined. We first present the main result of this section.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Covariance Bounds", "weight": 1.0} -->

The ambiguity set $\mathcal{P}$ reflects the assumption that the covariance matrix $\mathbf{\Sigma}$ is known *precisely* and that the (co-)variances of the components of $\overset{\sim}{\mathbf{ξ}}$ are permutation symmetric. Either assumption may prove overly restrictive in practice. In this section, we therefore assume that only an upper bound on the covariance matrix is available. More precisely, we consider the ambiguity set

<!-- chunk {"id": "body-0075", "role": "body", "section": "Covariance Bounds", "weight": 1.0} -->

where $\mathbf{μ}$ and $\mathbf{\Sigma}$ are defined as in Section 1. For $\gamma > 0$, we are then interested in quantifying *relaxed left-sided and right-sided Chebyshev bounds* of the form

<!-- chunk {"id": "body-0076", "role": "body", "section": "Covariance Bounds", "weight": 1.0} -->

In the following, we analyze each of these relaxed bounds in turn.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Step 1", "weight": 1.0} -->

We show that ${\overline{\gamma}}^{1/T}$ is the maximum root of the convex quadratic function

<!-- chunk {"id": "body-0078", "role": "body", "section": "Step 1", "weight": 1.0} -->

where $a$ and $b$ are defined in the statement of the theorem, and that this root satisfies ${\overline{\gamma}}^{1/T} > {\mu + \frac{\sigma^{2}\theta}{T\mu}}$. From the quadratic formula we know that the maximum root $x^{\star}$ of $q(x)$ satisfies

<!-- chunk {"id": "body-0079", "role": "body", "section": "Step 1", "weight": 1.0} -->

as well as ${q(x)}\rightarrow\infty$ for $x\rightarrow\infty$ since $\mu > {\sqrt{\frac{1 - \rho}{T}}\sigma}$. Since $q(x)$ is quadratic, both observations imply that the maximum root $x^{\star} = {\overline{\gamma}}^{1/T}$ of $q(x)$ indeed belongs to the interval $\left( {\mu + \frac{\sigma^{2}\theta}{T\mu}},\infty \right)$.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Step 2", "weight": 1.0} -->

Note that the last condition holds because is binding when $\gamma^{1/T} \geq {\mu + \frac{\sigma^{2}\theta}{T\mu}}$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Step 3", "weight": 1.0} -->

Consider the distribution $\mathbb{P}$ defined through

<!-- chunk {"id": "body-0082", "role": "body", "section": "Step 3", "weight": 1.0} -->

which implies ${\text{R}(\gamma)} = {\text{R}^{\prime}(\gamma)}$. We thus need to show that ${\mathbb{P}} \in \mathcal{P}$. To this end, we first observe that the first two moments of $\overset{\sim}{\mathbf{ξ}}$ under $\mathbb{P}$ satisfy

<!-- chunk {"id": "body-0083", "role": "body", "section": "Step 3", "weight": 1.0} -->

where the last row is due to and our definition of $\lambda$. It remains to be shown that $\overset{\sim}{\mathbf{ξ}}$ is non-negative $\mathbb{P}$-a.s. By construction of $\mathbb{P}$, this is the case iff $u^{\star} \geq {p^{\star}\lambda}$. We now observe that

<!-- chunk {"id": "body-0084", "role": "body", "section": "Step 3", "weight": 1.0} -->

where the first identity follows, the second one is due to the definition of $q^{\star}$ in Corollary 5.1 ‣ 5 Covariance Bounds ‣ Chebyshev Inequalities for Products of Random Variables"), and the inequality holds since there is $C > 0$ such that

<!-- chunk {"id": "body-0085", "role": "body", "section": "Step 3", "weight": 1.0} -->

and this expression is non-negative whenever $\gamma \geq \overline{\gamma}$. We thus conclude that

<!-- chunk {"id": "body-0086", "role": "body", "section": "Extensions", "weight": 1.0} -->

The techniques developed in this paper can also be used to construct Chebyshev bounds for sums, minima and maxima of non-negative random variables. All these Cheybshev bounds can be reduced to computing $\sup_{{\mathbb{P}} \in \mathcal{P}}{{\mathbb{P}}\left( {{h\left( \overset{\sim}{\mathbf{ξ}} \right)} \leq 0} \right)}$ for some permutation-symmetric functional $h({\mathbf{ξ}})$.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We first compare our Chebyshev bounds $\text{R}(\gamma)$ and $\text{L}(\gamma)$ with alternative bounds proposed in the literature, as well as the relaxed Chebyshev bound $\text{R}^{\prime}(\gamma)$ from Section 5. We then present a case study that employs our left-sided Chebyshev bound $\text{L}(\gamma)$ to select financial portfolios under imprecise knowledge of the asset return distributions. All optimization problems are solved with the SDPT3 optimization software using the YALMIP interface.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Comparison of Chebyshev Bounds", "weight": 1.0} -->

Instead of employing the bounds $\text{R}(\gamma)$ and $\text{L}(\gamma)$ from Sections 3 and 4, which are exact but may result in computationally challenging optimization problems, one can employ existing results to derive approximate bounds on the tail probabilities of a product of non-negative, permutation-symmetric random variables. In the following, we compare our bounds with two such approximations based on earlier results of Marshall and Olkin and Vandenberghe et al.. Both approximations rely on the larger ambiguity set

<!-- chunk {"id": "body-0089", "role": "body", "section": "Comparison of Chebyshev Bounds", "weight": 1.0} -->

Marshall and Olkin derive a convex optimization problem that provides a tight upper bound on the probability that the random vector $\overset{\sim}{\mathbf{ξ}}$ is contained in a closed convex set $\mathcal{C}$, assuming that $\overset{\sim}{\mathbf{ξ}}$ can be governed by any distribution from the ambiguity set $\mathcal{P}^{0}$. The choice $\mathcal{C} = \left\{ {{\mathbf{ξ}} \in {\mathbb{R}}^{T}}:{{\prod_{t = 1}^{T}\xi_{t}} \geq \gamma} \right\}$ allows us to approximate the right-sided Chebyshev bound $\text{R}(\gamma)$. For this special case, the bound of Marshall and Olkin has the analytical solution

<!-- chunk {"id": "body-0090", "role": "body", "section": "Comparison of Chebyshev Bounds", "weight": 1.0} -->

which follows from \[4, Theorem 6.1\]. By construction, ${\text{R}^{\text{MO}}(\gamma)} \geq {\text{R}(\gamma)}$ since $\mathcal{P} \subset \mathcal{P}^{0}$. Note that $\text{R}^{\text{MO}}(\gamma)$ coincides with our relaxed Chebyshev bound $\text{R}^{\prime}(\gamma)$ for $\gamma \geq \left( {\mu + \frac{\sigma^{2}\theta}{T\mu}} \right)^{T}$, see Theorem 5.2 ‣ 5 Covariance Bounds ‣ Chebyshev Inequalities for Products of Random Variables"). Thus, $\text{R}^{\text{MO}}(\gamma)$ also coincides with our right-sided Chebyshev bound $\text{R}(\gamma)$ for large values of $\gamma$, see Proposition 5.1.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Comparison of Chebyshev Bounds", "weight": 1.0} -->

Note that the bound of Marshall and Olkin cannot be used to approximate our left-sided Chebyshev bound $\text{L}(\gamma)$ since the complement of $\mathcal{C}$ fails to be convex.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Comparison of Chebyshev Bounds", "weight": 1.0} -->

A similar approximation $\text{L}^{\text{VBC}}(\gamma)$ can be derived for our left-sided Chebyshev bound $\text{L}(\gamma)$ by considering the strict complement of $\mathcal{C}$. Note that $\text{R}^{\text{VBC}}(\gamma)$ and $\text{L}^{\text{VBC}}(\gamma)$ can over- or underestimate our bounds $\text{R}(\gamma)$ and $\text{L}(\gamma)$ due to the use of the Taylor approximation.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Comparison of Chebyshev Bounds", "weight": 1.0} -->

The MO bound has an analytical solution and can therefore be computed in negligible time. In contrast, the VBC bounds and our bounds require the solution of semidefinite programs with two LMIs of size $\mathcal{O}\left( T^{2} \right)$. Table 2 compares the computation times of both bounds for products of different size $T$ on a computer with a 3.40GHz i7 CPU and 16GB RAM. While both bounds can be computed within seconds, the VBC bounds require significantly less runtime than our bounds. We attribute this to the LMI reformulations of the polynomial constraints in Theorems 3.1 ‣ 3 Left-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables") and 4.1 ‣ 4 Right-Sided Chebyshev Bounds ‣ Chebyshev Inequalities for Products of Random Variables"), which seem to lack structure that can be exploited by SDPT3.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Case Study: Financial Risk Management", "weight": 1.0} -->

Consider an investor who allocates a limited budget to a fixed pool of $n$ assets over a time horizon of $T$ periods. We denote by ${\overset{\sim}{r}}_{t,i} \geq {- 1}$, $t = {1,\ldots,T}$ and $i = {1,\ldots,n}$, the relative price change of asset $i$ between periods $t$ and $t + 1$. We assume that the investor pursues a fixed-mix (or constant proportions) strategy which rebalances the portfolio composition to a pre-selected set of weights ${\mathbf{w}} \in \mathcal{W} = \left\{ {{\mathbf{z}} \in {\mathbb{R}}_{+}^{n}}:{{\mathbf{e}^{\intercal}{\mathbf{z}}} = 1} \right\}$ at the beginning of each period.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Case Study: Financial Risk Management", "weight": 1.0} -->

Note that despite being memoryless, fixed-mix strategies are dynamic since they recapitalize those assets whose returns were below average ('buy low') and divest assets whose returns were above average ('sell high'). Fixed-mix strategies generalize the well-known $\left. 1/N \right.$-portfolio, and they have received significant attention among both academics and practitioners.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Case Study: Financial Risk Management", "weight": 1.0} -->

We assume that the investor assesses the fixed-mix strategy $\mathbf{w}$ in view of the value-at-risk of the portfolio's terminal wealth, which is defined as

<!-- chunk {"id": "body-0097", "role": "body", "section": "Case Study: Financial Risk Management", "weight": 1.0} -->

Here, the asset returns ${\overset{\sim}{\mathbf{r}}}_{t} = \left( {\overset{\sim}{r}}_{t,i} \right)_{i = 1}^{n}$ are governed by the probability distribution $\mathbb{P}$, and $\epsilon$ is a pre-specified parameter that reflects the investor's risk tolerance.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Case Study: Financial Risk Management", "weight": 1.0} -->

Calculating the value-at-risk of a portfolio's terminal wealth requires perfect knowledge of the joint asset return distribution $\mathbb{P}$, which is unavailable in practice. Following, we will assume that it is only known that the asset returns $\left( {\overset{\sim}{\mathbf{r}}}_{t} \right)_{t = 1}^{T}$ follow a weak-sense white noise process with mean $\mathbf{μ}$ and variance $\mathbf{\Sigma}$, that is, the asset returns are serially uncorrelated and have period-wise identical first and second-order moments.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Case Study: Financial Risk Management", "weight": 1.0} -->

We denote the set of all these distributions by $\mathcal{P}_{\mathbf{w}}$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Case Study: Financial Risk Management", "weight": 1.0} -->

In, the worst-case value-at-risk of the portfolio's terminal wealth is replaced with a quadratic approximation. The Chebyshev bounds proposed in this paper allow us to calculate the worst-case value-at-risk exactly without resorting to any approximation. Indeed, one verifies that

<!-- chunk {"id": "body-0101", "role": "body", "section": "Case Study: Financial Risk Management", "weight": 1.0} -->

where we have made explicit the dependence of the left-sided Chebyshev bound $L$ on the mean ${\mathbf{w}}^{\intercal}{\mathbf{μ}}$ and the variance ${\mathbf{w}}^{\intercal}\mathbf{\Sigma}{\mathbf{w}}$ of the wealth evolution $\left( {\overset{\sim}{\xi}}_{t} \right)_{t = 1}^{T}$. Since $L$ is monotonically non-decreasing in $\gamma$, the last expression can be evaluated efficiently through bisection on $\gamma$.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Case Study: Financial Risk Management", "weight": 1.0} -->

In addition to *evaluating* the worst-case value-at-risk of a pre-selected portfolio $\mathbf{w}$, an investor often seeks to determine a portfolio ${\mathbf{w}}^{\star}$ that *optimizes* the worst-case value-at-risk. The search for optimal portfolios is greatly simplified by the observation that there is always a portfolio ${\mathbf{w}}^{\star}$ on the mean-variance efficient frontier that maximizes $\text{WVaR}_{\epsilon}({\mathbf{w}})$ over (subsets of) $\mathcal{W}$.
