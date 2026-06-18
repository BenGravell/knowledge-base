<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Concentration Inequalities for Statistical Inference

Topics include Regression, Statistical inference, Poisson regression.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper gives a review of concentration inequalities which are widely employed in non-asymptotical analyses of mathematical statistics in a wide range of settings, from distribution-free to distribution-dependent, from sub-Gaussian to sub-exponential, sub-Gamma, and sub-Weibull random variables, and from the mean to the maximum concentration. This review provides results in these settings with some fresh new results. Given the increasing popularity of high-dimensional data and inference, results in the context of high-dimensional linear and Poisson regressions are also provided. We aim to illustrate the concentration inequalities with known constants and to improve existing bounds with sharper constants.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In probability theory and statistical inference, researchers often need to bound the probability of a difference between a random quantity from its target, usually the error bound of estimation. Concentration inequalities (CIs) are tools for attaining such bounds, and play important roles in deriving theoretical results for various inferential situations in statistics and probability. The recent developments in high-dimensional (HD) statistical inference, and statistical and machine learning have generated renewed interests in the CIs, as reflected in Koltchinskii, Vershynin, Wainwright and Fan et al.. As the CIs are diverse in their forms and the underlying distributional requirements, and are scattered around in references, there is an increasing need for a review which collects existing results together with some new results (sharper and constants-specified CIs) from the authors for researchers and graduate students working in statistics and probability. This motivates the writing of this review.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

CIs enable us to obtain non-asymptotic results for estimating, constructing confidence intervals, and doing hypothesis testing with a high-probability guarantee. For example, the first-order optimized condition for HD linear regressions should be held with a high probability to guarantee the well-behavior of the estimator. The concentration inequality for error distributions is to ensure the concentration from first-order optimized conditions to the estimator.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $Z_{n}:={f{(X_{1},\cdots,X_{n})}}$ and $X_{1},\cdots,X_{n}$ are random variables. We present two types of CIs: distribution-free and distribution-dependent. Distribution free CIs are free of distribution assumptions, while the distribution-dependent CIs are based on exponential moment conditions reflecting the tail property for the particular class of distributions. Concentration phenomenons for a sum of sub-Weibull random variables will lead to a mixture of two tails: sub-Gaussian for small deviations and sub-Weibull for large deviations from the mean, and it is closely related to Strong Law of Large Numbers, Central Limit Theorem, and Law of the Iterative Logarithm. We provide applications of the CIs to empirical processes and high-dimensional data settings. The latter includes the linear and Poisson regression with a diverging number of covariates. We organize the materials in the forms of Lemmas, Corollaries, Propositions, and Theorems. Lemmas and Corollaries are on existing results usually without proof except for a few fundamental ones.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Propositions are also for existing results but with sharper or more precise constants and sometimes come with proofs. Theorems are for new results. This review contains 27 Lemmas, 21 Corollaries, 15 Propositions, and 4 Theorems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The review is organized as follows. Section 2 outlines distribution-free CIs. CIs for Sub-Gaussian, Sub-exponential, sub-Gamma, and sub-Weibull random variables are given in Section 3, 4, 5, and 6 respectively. Section 7 reports concentration for the maximal of random variables and suprema of empirical processes. Applications for high dimensional linear and Poisson regression are outlined in Section 8. Section 9 discusses extensions to other settings.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Distribution-free Concentration Bounds", "weight": 1.0} -->

The purpose here is to introduce distribution-free CIs. We first review Markov's, Chebysheff's and Chernoff's tail probability bounds that constitute fundamental inequalities for deriving most of the concentration bounds; see Chap. 1 of Durrett or Appendix B in Giraud for the proofs.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Example 2.8 (Empirical distribution function, EDF)", "weight": 1.0} -->

McDiarmid's inequality (also called bounded difference inequality, see McDiarmid ) is a concentration inequality for a multivariate function of random sequence ${\{ X_{i}\}}_{i = 1}^{n}$, says $f{(X_{1},\ldots,X_{n})}$. As a generalization of Hoeffding's inequality, it does not require any distribution assumptions about r.vs and the $f{(X_{1},\ldots,X_{n})}$ may be dependent sum of r.vs. The only requirement is the bounded difference condition by replacing $X_{j}$ by $X_{j}^{^{\prime}}$ meanwhile maintaining the others fixed in $f{(X_{1},\ldots,X_{n})}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Example 2.13 (The supremum of bounded EP)", "weight": 1.0} -->

Given $f \in \mathcal{F}$, WLOG, assume that

<!-- chunk {"id": "body-0011", "role": "body", "section": "Motivations", "weight": 1.0} -->

In probability, there is a well-known inequality for bounding the Gaussian tail. If $X \sim {N{}}$, Gordon obtained for $x > 0$

<!-- chunk {"id": "body-0012", "role": "body", "section": "Motivations", "weight": 1.0} -->

which is called *Mills's inequality*, relating to Mills's ratio (Mills, ). The upper bound in is mostly used to derive law of the iterated logarithm (Durrett, ). However, if $x$ tends to zero the upper bound goes to $+ \infty$ which makes it meaningless. So the Mill's inequality is useful only for larger $x$. We need a better inequality. In fact, the upper bound in can be strengthened as in Lemma B.3 in Giraud: ${{P{({{|X|} \geq x})}} \leq e^{- {x^{2}/2}}}.$ We refer it as the *sharper Mill's inequality*.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Example 3.1 ($O{(a^{- 2})}$-decay tail inequality is not enough)", "weight": 1.0} -->

In statistics, people want to study a general class of error distributions (beyond Gaussian) whose moment generating function (MGF): $Ee^{sX}$ have similar Gaussian properties with $s$ in specific subset of $\mathbb{R}$. To derive sharper Mill's inequality, it is natural to define the class of sub-Gaussian r.v. as follows.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Example 3.4 (Bounded r.vs)", "weight": 1.0} -->

There are at least seven equivalent forms for sub-Gaussian as shown in the following.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark 3.6", "weight": 1.0} -->

The ${EX} = 0$ is for convenience as the zero mean is used in the proof of Corollary 3.5. ‣ 3.1 Motivations ‣ 3 Sub-Gaussian Distributions ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference"), see Vershynin for the details and the proof of the equivalences -. The equivalences is given in Theorem 2.6 of Wainwright The moment condition for integers $k$ in can be relaxed to *even integers* $k$ by the symmetrization technique. By symmetry of $X$, let us consider a negative independent copy $- X^{\prime}$ which is independent of $X$ and has the same distribution as $X$. If is true and ${E{({- X^{\prime}})}} = 0$, from Jensen's inequality ${Ee^{\theta{({- X^{\prime}})}}} \geq e^{\theta E{({- X^{\prime}})}} = 1$ since $- X^{\prime}$ has zero mean.

<!-- chunk {"id": "body-0016", "role": "body", "section": "The variance proxy and sub-Gaussian norm", "weight": 1.0} -->

We show that the $\sigma^{2}$ in Definition 3.2. ‣ 3.1

<!-- chunk {"id": "body-0017", "role": "body", "section": "The variance proxy and sub-Gaussian norm", "weight": 1.0} -->

The $\sigma^{2}$ not only characterizes the speed of decay in the sub-Gaussian tail probability, but also bounds the variance of $n^{- {1/2}}{\sum_{i = 1}^{n}X_{i}}$. This is because, by the sub-Gaussian MGF

<!-- chunk {"id": "body-0018", "role": "body", "section": "The variance proxy and sub-Gaussian norm", "weight": 1.0} -->

Dividing $s^{2}$ on both sides of and taking $s\rightarrow 0$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The variance proxy and sub-Gaussian norm", "weight": 1.0} -->

In the theory of empirical process, sub-Gaussian definitions are characterized by Orlicz norms (see Definition 6.7. ‣ 6.1 Sub-Weibull r.vs and 𝜓_𝜃-norm ‣ 6 Sub-Weibull distributions ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference") below and van der Vaart and Wellner ) to derive exponential tail inequality for empirical process.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example 3.9 (The sub-Gaussian norm of Gaussian r.vs.)", "weight": 1.0} -->

However, the neat notation for defining sub-Gaussian norm sometime leads to unknown constants in the CIs as shown next.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Randomly weighted sum of independent sub-Gaussian variables", "weight": 1.0} -->

In this part, we outline the sub-Gaussian type CIs for the randomly weighted sum of exponential family r.vs: $S_{n}^{W} =:\sum_{i = 1}^{n}W_{i}Y_{i}$ where ${\{ W_{i}\}}_{i = 1}^{n}$ are called the multipliers (or random weights) which are independent from ${\{ Y_{i}\}}_{i = 1}^{n}$. The normalized sum $\frac{1}{\sqrt{n}}{({S_{n}^{W} - {ES_{n}^{W}}})}$ is also call *multiplier empirical processes*, and it serves for the multiplier Bootstrap inference where the multipliers $\{ W_{i}\}$ are r.vs independent from ${\{ Y_{i}\}}_{i = 1}^{n}$, see Chapter 2.9 of van der Vaart and Wellner.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Randomly weighted sum of independent sub-Gaussian variables", "weight": 1.0} -->

To get sub-Gaussian concentration, some regularity conditions for the parameter space are required.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Concentration for Lipschitz functions of random vectors", "weight": 1.0} -->

In the analyses of high-dimensional statistics by empirical processes, researches often resort to the CIs of Lipschitz functions for either bounded or strongly log-concave random vectors (Wainwright, ).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example 3.22 (Order Statistics)", "weight": 1.0} -->

From Lemma 3.20. ‣ 3.4 Concentration for Lipschitz functions of random vectors ‣ 3 Sub-Gaussian Distributions ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference") and Lemma 3.21. ‣ 3.4 Concentration for Lipschitz functions of random vectors ‣ 3 Sub-Gaussian Distributions ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference"), suppose that $\left\{ X_{i} \right\}_{i = 1}^{n}$ are independent r.vs which are $\gamma -$strongly log-concave distributed satisfying ${P{\lbrack{{{f{(X)}} - {Ef{(X)}}} \geq t}\rbrack}} \leq e^{- \frac{\gamma t^{2}}{4L^{2}}}$ for any function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ that is $L$-Lipschitz w.r.t. the Euclidean norm.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example 3.22 (Order Statistics)", "weight": 1.0} -->

Let $X_{(k)}$ be the $k$-th order statistic of $X_{1},\ldots,X_{n}$, it can be shown that

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example 3.22 (Order Statistics)", "weight": 1.0} -->

More results of the tail bounds for the order statistics of IID r.vs are reported in Boucheron.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Example 4.1 (MGF of exponential distributions)", "weight": 1.0} -->

Consider the exponential r.v. $X \sim {{Exp}{(\mu)}}$ with ${EX} = \mu > 0$. The MGF of $X - \mu$ satisfies

<!-- chunk {"id": "body-0028", "role": "body", "section": "Example 4.1 (MGF of exponential distributions)", "weight": 1.0} -->

In ), the MGF of the exponential r.v. is divergent on $s = {1/\mu}$ and it cannot be bounded by a Gaussian MGF of $s$ in $\mathbb{R}$, and the exponential MGF is bounded by Gaussian MGF for ${|s|} \leq \frac{1}{2\mu}$ via inequality ). Motivated by Example 4.1. ‣ 4.1 Characterizations ‣ 4 Sub-exponential Distributions ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference"), the first definition of sub-exponential distribution ) below is exactly the locally sub-Gaussian property.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Example 4.5 (Geometric distributions)", "weight": 1.0} -->

and Corollary 4.3. ‣ 4.1 Characterizations ‣ 4 Sub-exponential Distributions ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference") implies the centralized ${Geo}{(q)}$ is sub-exponential with $K_{3} = {- {4/{\log{({1 - q})}}}}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Example 4.6 (Discrete Laplace r.vs)", "weight": 1.0} -->

A r.v. $X \sim {{DL}{(q)}}$ obeys the discrete Laplace distribution if ${{f_{q}{(k)}} = {{\mathbb{P}}{({X = k})}} = {\frac{1 - q}{1 + q}q^{|k|}}},{k \in {\mathbb{Z}} = {\{ 0,{\pm 1},{\pm 2},\ldots\}}}$ with parameter ${q \in {}}.$ The discrete Laplace r.v. is the difference of two IID ${Geo}{(q)}$. The geometric distribution is sub-exponential, thus Corollary 4.7. ‣ 4.1 Characterizations ‣ 4 Sub-exponential Distributions ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference")(a) mentioned later implies that the discrete Laplace is also sub-exponential distributed. In differential privacy of network models, the noises are assumed following the discrete Laplace distribution, see Fan et al. and references therein.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Example 4.6 (Discrete Laplace r.vs)", "weight": 1.0} -->

The next result shows that a sum of independent sub-exponential r.vs has two tails with difference convergence rate, which is slightly different from Hoeffding's inequality. Deviating from the mean, it tells us that the tail of the sum of sub-exponential r.vs behaves like a combination of a Gaussian tail and a exponential tail.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 4.8", "weight": 1.0} -->

The $({\frac{nt^{2}}{{\overline{\lambda}}^{2}} \land \frac{nt}{\alpha}})$ in ) reveals that the smaller $\alpha$ (locally sub-Gaussian factor) leads to sharper sub-exponential concentration. The sub-exponential concentration tends to the sub-Gaussian concentration with variance proxy ${\overline{\lambda}}^{2}$ when $\alpha\rightarrow 0$, which coincides the locally sub-Gaussian definition for sub-exponential distribution in Definition 4.2. ‣ 4.1 Characterizations ‣ 4 Sub-exponential Distributions ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference").

<!-- chunk {"id": "body-0033", "role": "body", "section": "Sub-exponential norm", "weight": 1.0} -->

Recall the Corollary 4.3. ‣ 4.1 Characterizations ‣ 4 Sub-exponential Distributions ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference")): The absolute value of sub-exponential r.v. $|X|$ has a bound MGF at point $K_{5}^{- 1}$: ${\phi_{|X|}{(K_{5}^{- 1})}}:={Ee^{{|X|}/K_{5}}} \leq 2$. Similar to the definition of sub-Gaussian norm, we define the sub-exponential norm.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Example 4.18 (The sub-exponential norm of Poisson r.v.)", "weight": 1.0} -->

Corollary 4.13. ‣ 4.2 Sub-exponential norm ‣ 4 Sub-exponential Distributions ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference") is useful in the next subsection for the concentration for quadratic forms.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Concentration for quadratic forms and norm of random vectors", "weight": 1.0} -->

All concentration results in the above sections are about the mean. The inference for the variance and covariance in high-dimensional models is an important problem, see Section 6 of Wainwright. It is connected with squares of r.vs. The sample variance is a quadratic form (with shift term) of the data. The data are often postulated as sub-Gaussian. For the square of a sub-Gaussian r.v., it is natural to ask what is the behavior of the tail (or the exponential moment). The answer is sub-exponential by using ) in Corollary 3.5. ‣ 3.1 Motivations ‣ 3 Sub-Gaussian Distributions ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference").

<!-- chunk {"id": "body-0036", "role": "body", "section": "Concentration for quadratic forms and norm of random vectors", "weight": 1.0} -->

A simple example that the quadratic form of Gaussian is $\chi^{2}$ distributed, and the $\chi^{2}$-distribution of 2 degrees of freedom is exponentially distributed with mean 2.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Example 4.19 (Chi-squared r.vs)", "weight": 1.0} -->

Similar sub-exponential results also hold for independent sum of square of sub-Gaussian r.vs. The following two lemmas in of Vershynin confirm this simple example to the general situation.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Sub-Gamma distributions", "weight": 1.0} -->

Comparing to the classical Chebyshev's inequality, Bernstein-type inequalities have more precise concentration, it originally is an extension of the Hoeffding's inequality with bounded assumption \[see Bernstein, Bennett \]. As mentioned by Pollard, the proof of Hoeffding's inequality with endpoints of the interval $\lbrack a,b\rbrack$ in Lemma 2.7.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Sub-Gamma distributions", "weight": 1.0} -->

without any other variance information.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Sub-Gamma distributions", "weight": 1.0} -->

If $X$ takes values near the endpoints of the interval $\lbrack a,b\rbrack$ with a small probability, it is guessed that the sharper concentration could be improved by adding variance condition. The following tail bound for the sum $S_{n}:={\sum_{i = 1}^{n}X_{i}}$ needs extra variance information.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example 5.2 (Non-asymptotic confidence intervals)", "weight": 1.0} -->

To prove Corollary 5.1. ‣ 5.1 Sub-Gamma distributions ‣ 5 Sub-Gamma Distributions and Bernstein’s Inequality ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference"), we need get the sharp bounds of the MGF of the single variable and then do aggregation for the summation. By the Taylor expansion, we have

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 5.2 (Non-asymptotic confidence intervals)", "weight": 1.0} -->

Applying the inequality ${{k!}/2} \geq 3^{k - 2}$ for any $k \geq 2$, it implies

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example 5.2 (Non-asymptotic confidence intervals)", "weight": 1.0} -->

The upper bounds of MGF essentially have the same form in comparison with Gamma distribution below whose MGF is bounded by ) in following example.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 5.3 (Gamma r.vs)", "weight": 1.0} -->

Motivated by the MGF bounds in ), Boucheron et al. defines the sub-Gamma r.v. based on the right tail and left tail with variance factor $v$ and scale factor $b$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example 5.5 (Sub-exponential r.vs)", "weight": 1.0} -->

The sub-Gamma condition ) leads to the useful tail bounds and moment bounds.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Bernstein's growth of moments condition", "weight": 1.0} -->

In some settings, one can not assume the r.vs being bounded. Bernstein's inequality for the sum of independent r.vs allows us to estimate the tail probability by a weaker version of an exponential condition on the growth of the $k$-moment without the boundedness.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Concentration of exponential family without compact space", "weight": 1.0} -->

Theory and statistical applications of natural exponential family have attracted renewed attention in the past years (Lehmann and Romano, ). in Lasso penalized *generalized linear models* (GLMs), the results of oracle inequalities lie on CIs of a quantity that can be represent as Karush-Kuhn-Tucker conditions (see (8.11. ‣ 8.4 High-dimensional Poisson regressions with random design ‣ 8 Concentration for High-dimensional Statistics ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference"))) related to the centralized exponential family empirical process: $\sum_{i = 1}^{n}{w_{i}{({Y_{i} - {EY_{i}}})}}$ for no-random weights ${\{ w_{i}\}}_{i = 1}^{n}$ depending on the fixed design. Kakade et al. has studied the sub-exponential growth of the cumulants of an exponential family distribution and studied oracle inequalities of Lasso regularized GLMs, but the constant in their result is not specific.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Concentration of exponential family without compact space", "weight": 1.0} -->

In this part, we obtain cental moments bounds with a specific constant, which gives the Bernstein's inequality for the general exponential family, and the proof is based on the Cauchy formula of higher-order derivatives for complex functions \[Corollary 4.3 in Stein and Shakarchi \].

<!-- chunk {"id": "body-0049", "role": "body", "section": "Example 5.21 (Log-concave continuous distributions, Bagnoli and Bergstrom )", "weight": 1.0} -->

Many continuous distributions, such as *normal distribution*, *exponential distribution*, *uniform distribution over any convex set*, *logistic distribution*, *extreme value distribution*, *chi-square distribution*, *chi distribution*, *hyperbolic secant distribution*, *Laplace distribution*, *Weibull distribution* (the shape parameter $\theta \geq 1$), *Gamma distribution* (the shape parameter $a \geq 1$) and *Beta distribution* (both shape parameters are $\geq 1$) have log-concave continuous densities.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Example 5.21 (Log-concave continuous distributions, Bagnoli and Bergstrom )", "weight": 1.0} -->

Analogous to the log-concave continuous function, we can define log-concave sequence for the p.m.f. of discrete r.v., which also has Bernstein-type concentrations.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Example 5.23 (Log-concave discrete distributions)", "weight": 1.0} -->

*Bernoulli and binomial distributions*, *Poisson distribution*, *geometric distribution*, and *negative binomial distribution* (with number of success $> 1$) and *hypergeometric distribution* have log-concave integer-valued p.m.f., see Johnson et al..

<!-- chunk {"id": "body-0052", "role": "body", "section": "Sub-Weibull r.vs and $\\psi_{\\theta}$-norm", "weight": 1.0} -->

A r.v. is heavy-tailed if its distribution function $F{( \cdot )}$ fails to be bounded by a decreasing exponential function (Foss et al., ),

<!-- chunk {"id": "body-0053", "role": "body", "section": "Sub-Weibull r.vs and $\\psi_{\\theta}$-norm", "weight": 1.0} -->

We first give a simple example of the heavy-tailed distributions arisen by multiplying sub-Gaussian r.vs. The proof is motivated by Lemmas 2.7.7 of Vershynin.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Example 6.3 (Weibull r.vs)", "weight": 1.0} -->

The Weibull r.v. $X \in {\mathbb{R}}^{+}$ is defined by its survival function

<!-- chunk {"id": "body-0055", "role": "body", "section": "Example 6.3 (Weibull r.vs)", "weight": 1.0} -->

Sub-Weibull distribution is characterized by the right tail of the Weibull distribution and is a generalization of both sub-Gaussian and sub-exponential distributions.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Concentrations for sub-Weibull summation", "weight": 1.0} -->

The Chernoff inequality tricks in the derivation of Corollary 4.7. ‣ 4.1 Characterizations ‣ 4 Sub-exponential Distributions ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference") for sub-exponential concentration is not valid for sub-Weibull distributions, since the exponential moment equivalent conditions of sub-Weibull are on the absolute value $|X|$. However, Bernstein's moment condition is the exponential moment of the absolute value. An alternative method is given by Kuchibhotla and Chakrabortty, who defines the so-called Generalized Bernstein-Orlicz (GBO) norm.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Concentrations for sub-Weibull summation", "weight": 1.0} -->

Fixed $\alpha > 0$ and $L \geq 0$, define a function $\Psi_{\theta,L}{( \cdot )}$ with its inverse function ${{\Psi_{\theta,L}^{- 1}{(t)}}:={\sqrt{\log{({t + 1})}} + {L{\lbrack{\log{({t + 1})}}\rbrack}^{1/\theta}{\forall t}}} \geq 0}.$ A promising development is that the following GBO norm helps us derive tail behaviors for sub-Weibull r.vs.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Concentration for Extremes", "weight": 1.0} -->

The CIs presented so far only concern with linear combinations of independent r.vs or Lipschitz function of random vectors. In many statistics applications, we have to control the maximum of the $n$ r.vs when deriving the error bounds, while these r.vs may be arbitrarily dependent. This section is developed on advanced proof skills. So we present the proofs even for existing results, which are applications of CIs in a probability aspect.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Maximal inequalities", "weight": 1.0} -->

This section presents the maximal inequalities for r.vs. ${\{ X_{i}\}}_{i = 1}^{n}$ which may not be independent. In the theory of empirical process, it is of interest to bound $E{\max_{1 \leq i \leq n}{|X_{i}|}}$ \[Section 2.2, van der Vaart and Wellner \]. If ${\{ X_{i}\}}_{i = 1}^{n}$ are arbitrary sequence of real-valued r.vs and have finite $r$-th moments ($r \geq 1$), Aven gives a crude upper bounds for $E{\max_{1 \leq i \leq n}X_{i}}$ by Jensen's inequality

<!-- chunk {"id": "body-0060", "role": "body", "section": "Maximal inequalities", "weight": 1.0} -->

Page314 of van der Vaart mentions a sharper version of without the proof. In below, we introduce the proof by the truncation technique.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Example 7.3 (Pareto distribution)", "weight": 1.0} -->

Corollary 7.1. ‣ 7.1 Maximal inequalities ‣ 7 Concentration for Extremes ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference") reveals that $\max_{1 \leq i \leq n}{|X_{i}|}$ diverges at rate slower than $n^{1/r}$ under the $r$-th moment condition. As $r$ increases, it will slow down the divergence rate of the maxima. If we have arbitrary finite $r$-th moment conditions (such as Gaussian distribution), it means that the divergence rate of maxima is slower than any polynomial rate $n^{1/r}$. This suggests that the rate may be logarithmic. With the sub-Gaussian assumptions, the logarithmic divergence rate is possible and the proof is based on controlling the expectation of the supremum of variables, from the argument in Pisier.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Concentration for suprema of empirical processes", "weight": 1.0} -->

The study of the empirical processes begins with the uniform limit law of EDF in Example 2.8. ‣ 2 Distribution-free Concentration Bounds ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference"). The Glivenko-Cantelli theorem extends the LLN for EDF and gives uniform convergence: ${\left\| {{\mathbb{F}}_{n} - F} \right\|_{\infty} = {\sup_{t \in {\mathbb{R}}}\left| {{{\mathbb{F}}_{n}{(t)}} - {F{(t)}}} \right|}\overset{\text{~as~}}{\rightarrow}0}.$ Moreover, a stronger result than Example 2.8. ‣ 2 Distribution-free Concentration Bounds ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference") is the Dvoretzky-Kiefer-Wolfowitz (DKW) inequality (Dvoretzky et al., )

<!-- chunk {"id": "body-0063", "role": "body", "section": "Concentration for suprema of empirical processes", "weight": 1.0} -->

In some statistical applications, given an estimator $\hat{\theta},$ and $f_{\hat{\theta}}{(X_{i})}$ is a function of $X_{i}$ and $\hat{\theta}$. We want to study its asymptotic properties for sums of $f_{\hat{\theta}}{(X_{i})}$ that changes with both $n$ and $\hat{\theta}$,

<!-- chunk {"id": "body-0064", "role": "body", "section": "Concentration for suprema of empirical processes", "weight": 1.0} -->

Two conditions to get the convergence of $\sup_{f \in \mathcal{F}}{|{{({{\mathbb{P}}_{n} - P})}f_{\theta}}|}$ are the finite *bracketing number* condition with $L_{1}{(P)}$-norm in Theorem 19.4 of van der Vaart (or finite uniform covering numbers in Theorem 19.13 of van der Vaart ).

<!-- chunk {"id": "body-0065", "role": "body", "section": "Example 7.17 (Empirical process with indicator functions, Example 19.4 of van der Vaart )", "weight": 1.0} -->

Their total number $k$ can be chosen smaller than ${\lceil{1/\varepsilon}\rceil} \leq {2/\varepsilon}$, where ${\lceil r\rceil} = {\min{\{{m \in {\mathbb{Z}}};{m \leq {r + 1}}\}}}$ is the upper integer part of $r \in {\mathbb{R}}$ (i.e. is the smallest integer that is greater than or equal to $x.$). So

<!-- chunk {"id": "body-0066", "role": "body", "section": "Example 7.17 (Empirical process with indicator functions, Example 19.4 of van der Vaart )", "weight": 1.0} -->

We conclude that the class $\mathcal{F}$ is P-Glivenko-Cantelli, and it shows the Glivenko-Cantelli theorem.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Example 7.18 (Weighted empirical process with dependent weights)", "weight": 1.0} -->

Suppose we observe a sequence of IID observations ${\{\left( X_{i},Y_{i} \right)\}}_{i = 1}^{n}$ drawn from a random pair $(X,Y)$. Given some weighted functions $W{( \cdot )}$ and a bounded estimator $\hat{t} \in {(0,\tau\rbrack}$, we want to study the stochastic convergence of dependent weighted empirical processes

<!-- chunk {"id": "body-0068", "role": "body", "section": "Example 7.18 (Weighted empirical process with dependent weights)", "weight": 1.0} -->

Consider the class of functions indexed by $t$,

<!-- chunk {"id": "body-0069", "role": "body", "section": "Example 7.18 (Weighted empirical process with dependent weights)", "weight": 1.0} -->

If the upper bounds of $N_{\lbrack\rbrack}\left( \varepsilon,\mathcal{F},{L_{2}{(P)}} \right)$ and $\sup{{}_{}^{}\left( \varepsilon,\mathcal{F},{L_{2}{(Q)}} \right)}$ have polynomial rates w.r.t. $O{({1/\varepsilon})}$, the following tail bound estimate gives the convergence rate of suprema of empirical processes in Lemma 7.15. ‣ 7.2 Concentration for suprema of empirical processes ‣ 7 Concentration for Extremes ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference") obtained by Talagrand. It extends DKW inequality to general empirical processes with the bounded function classes.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Example 7.22 (Expected bound for supremum of bounded EP)", "weight": 1.0} -->

Remark: In general, $E{\lbrack{\sup\limits_{f \in \mathcal{F}}{\frac{1}{\sqrt{n}}{\sum\limits_{i = 1}^{n}{f{(X_{i})}}}}}\rbrack}$ is bounded by the *uniform entropy integral* evaluated by VC dimension of the general $\mathcal{F}$, see Theorem 3.5.4 in Giné and Nickl.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Example 7.22 (Expected bound for supremum of bounded EP)", "weight": 1.0} -->

To further bound $E{\{{\sup_{f \in \mathcal{F}}{\sqrt{n}{|{{({{\mathbb{P}}_{n} - {\mathbb{P}}})}f}|}}}\}}$ in Lemma 7.20. ‣ 7.2 Concentration for suprema of empirical processes ‣ 7 Concentration for Extremes ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference") with ${\Phi{(t)}} = {|t|}$, Theorem 3.5.4 in Giné and Nickl gave a constants-specified upper bound for the expectation of suprema of unbounded empirical processes.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Example 7.25 (A proof of DKW inequality, Oliveira )", "weight": 1.0} -->

The proof is divided into 3 steps.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Remark 7.27", "weight": 1.0} -->

It is worth noting that the inequalities of Hoeffding, sub-exponential, Bernstein and Sub-weibull also hold for the maximum of the partial-sums $\max_{1 \leq k \leq n}S_{k}$ by virtue of Doob's sub-martingale inequality (Section 7.2.c, 7.3, 7.5 in Lin and Bai ).

<!-- chunk {"id": "body-0074", "role": "body", "section": "Remark 7.27", "weight": 1.0} -->

where the last inequality will be proved in Step3.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Remark 7.27", "weight": 1.0} -->

‣ Example 7.25 (A proof of DKW inequality, Oliveira ). ‣ 7.2 Concentration for suprema of empirical processes ‣ 7 Concentration for Extremes ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference")), we have ${{P{({{\max_{0 \leq k \leq n}S_{k}} \geq t})}} \leq {2P{({S_{n} \geq t})}}}.$ Then applying identity for differentiable function $f$

<!-- chunk {"id": "body-0076", "role": "body", "section": "Remark 7.27", "weight": 1.0} -->

where the last equality is by (7.25. ‣ 7.2 Concentration for suprema of empirical processes ‣ 7 Concentration for Extremes ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference")): ${\int_{0}^{\infty}{f^{\prime}{(t)}\mathbf{P}{\lbrack{X \geq t}\rbrack}{dt}}} = {{E{\lbrack{f{(X)}1_{\{{X \geq 0}\}}}\rbrack}} - {f{}E{\lbrack 1_{\{{X \geq 0}\}}\rbrack}}}$ and the second last inequality is by Lévy inequality (for ${\max\limits_{0 \leq i \leq n}S_{i}} \geq 0$ ^11^1Here we define $S_{0} = 0$ as the symmetric random walk starting at 0.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Remark 7.27", "weight": 1.0} -->

Therefore by ), we have sub-Gaussian MGF of suprema of empirical processes

<!-- chunk {"id": "body-0078", "role": "body", "section": "Remark 7.27", "weight": 1.0} -->

Finally, by Chernoff's inequality, we obtain the DKW inequality (7.25. ‣ 7.2 Concentration for suprema of empirical processes ‣ 7 Concentration for Extremes ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference")): ${P{({{\sup_{x \in {\mathbb{R}}}{|{{{\mathbb{F}}_{n}{(x)}} - {F{(x)}}}|}} > \varepsilon})}} \leq {\inf_{\theta > 0}{4e^{\frac{2\theta^{2}}{n} - {\theta\epsilon}}}} = {4e^{- {{n\varepsilon^{2}}/8}}}$ for every ${\varepsilon > 0}.$

<!-- chunk {"id": "body-0079", "role": "body", "section": "Concentration for High-dimensional Statistics", "weight": 1.0} -->

With the emergence of high-dimensional (HD) data such as the gene expression data, there are renewed interests on the CIs. One aspect of the HD data is such that the number of variables $p$ can be comparable to or even greater than the sample size $n$. This section provides results in three commonly encountered settings: increasing-dimensional ($p_{n} = {o{(n)}} < n$), large-dimensional ($p_{n} = {O{(n)}}$) and high-dimensional setting (${p_{n} \gg n},{p_{n} = e^{o{(n)}}}$).

<!-- chunk {"id": "body-0080", "role": "body", "section": "Linear models with diverging number of covariates", "weight": 1.0} -->

This subsection only considers the case that $p$ is increasing but $p < n$. The ordinary least square (OLS) estimator is

<!-- chunk {"id": "body-0081", "role": "body", "section": "Remark 8.3", "weight": 1.0} -->

As ${p,n}\rightarrow\infty$ with $p < n$, part (ii) implies that the OLS estimator may had poor performance if ${p/n}\rightarrow c > 0$. The average in-sample $\ell_{2}$-risk tends to zero if $p_{n} = {o{(n)}}$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Remark 8.3", "weight": 1.0} -->

which implies that, with probability greater than $1 - \delta_{n}$,

<!-- chunk {"id": "body-0083", "role": "body", "section": "Remark 8.3", "weight": 1.0} -->

which is a quadratic form of sub-Gaussian vector.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Non-asymptotic Bai-Yin theorem for random matrix", "weight": 1.0} -->

Let $\mathbf{A}$ be a $p \times p$ Hermitian matrix with real eigenvalues: $\lambda_{\max}:=\lambda_{1} \geq \cdots \geq \lambda_{p} =:\lambda_{\min}$. The *empirical spectral distribution* (ESD) of $\mathbf{A}$ is

<!-- chunk {"id": "body-0085", "role": "body", "section": "Non-asymptotic Bai-Yin theorem for random matrix", "weight": 1.0} -->

which resembles the EDF of IID samples. Let ${\{\mathbf{A}_{n}\}}_{n \geq 1}$ be a sequence of $p \times p$ Hermitian random matrices indexed by the sample size $n$, and $F_{\mathbf{A}_{n}}$ be the ESD of $\mathbf{A}_{n}$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Non-asymptotic Bai-Yin theorem for random matrix", "weight": 1.0} -->

In multivariate statistics, it is of interest to study the *sample covariance matrix* $\mathbf{S}_{n}:={\frac{1}{n}{\mathbf{X}\mathbf{X}}^{T}}$ where the double array $\mathbf{X} = \left\{ X_{ij},i = 1,\ldots,p;j = 1,\ldots,n \right\}$ contains zero-mean IID r.vs $\{ X_{ij}\}$ with variance $\sigma^{2}.$ Suppose that the dimensions $n$ and $p$ grow to infinity while $p/n$ converges to a constant in $\lbrack 0,1\rbrack$. Marčenko and Pastur gives the limit behavior of the ESD of $\mathbf{S}_{n}$. Bai and Yin obtained a strong version of the Marčenko-Pastur law.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Oracle inequalities for penalized linear models", "weight": 1.0} -->

where $\lambda_{n}\rightarrow 0$ is a tuning parameter and $s:={\|{\mathbf{β}}^{\ast}\|}_{0}$. In the following, we focus on the $\ell_{1}$ estimation and prediction consistencies for the penalized linear models. Let $\lambda > 0$ be a tuning parameter, the Lasso estimator (Tibshirani, ) for Model is

<!-- chunk {"id": "body-0088", "role": "body", "section": "Oracle inequalities for penalized linear models", "weight": 1.0} -->

By sub-derivative techniques in convex optimizations, the Karush-Kuhn-Tucker (KKT) condition of Lasso optimization function is

<!-- chunk {"id": "body-0089", "role": "body", "section": "Oracle inequalities for penalized linear models", "weight": 1.0} -->

see Candes and Tao. Lasso and DS are capable of producing sparse estimates with only a few (hence sparse) nonzero coefficients among the $p$ coefficients of the covariates. The idea of Lasso and DS was presented in a geophysics literature (Levy and Fullagar, ). By, we get ${\|{\hat{\beta}}_{DS}\|}_{1} \leq {\|{\hat{\beta}}_{L}\|}_{1}$, which signifies that the DS may be more sparse than the Lasso.

<!-- chunk {"id": "body-0090", "role": "body", "section": "High-dimensional Poisson regressions with random design", "weight": 1.0} -->

Lemma 4.2 in Bühlmann and van de Geer shows the first-order conditions for the optimization.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Extensions", "weight": 1.0} -->

The review has been focused on the sum of independent r.vs in the Euclidean space. However, independence structure may not be suitable for some applications, for instance, econometrics, survival analysis, and graphical models. At the same time, the Euclidean valued r.vs may not be appropriate for functional data and image data. In the following we point out results in settings not covered to broaden this review.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Extensions", "weight": 1.0} -->

By CIs for the martingales, oracle inequalities have been proposed for Lasso penalized Cox models, see Huang et al.. Some statistical models, such as the Ising model involving Markov's chains. Miasojedow and Rejchel applied Hoeffding's inequality for Markov's chains to deal with this difficulty, see Fan et al. for a review. In time series analysis, Xie and Xiao studies the square-root Lasso method for HD linear models with $\alpha$, $\rho$, $\phi$-mixing or $m$-dependent errors. The Hoeffding's and Bernstein's CIs for weakly dependent summations can be found in Bosq. Via sub-Weibull concentrations under $\beta$-mixing, non-asymptotic inequalities for estimation errors, and the prediction errors are obtained by Wong et al. for the Lasso-regularized sparse VAR model with sub-Weibull innovations. U-Statistic is another dependent sum, and Example 2.13.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Extensions", "weight": 1.0} -->

‣ 2 Distribution-free Concentration Bounds ‣ REVIEW ARTICLE Concentration Inequalities for Statistical Inference") provides a concentration result by McDiarmid's inequality. Borovskikh introduces the concentration for the Banach-valued U-statistics.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Extensions", "weight": 1.0} -->

In non-parametric regressions, the corresponding score functions may be r.vs in Banach (or Hilbert) space; see the monographs Ledoux and Talagrand, Yurinsky for introductions. Exponential tail bounds for Banach- or Hilbert-valued r.vs are indispensable for deriving sharp oracle inequalities of the error bounds, see Zhang, Zhang and Lei. Recently, Banach-valued CIs are applied to conceive non-asymptotic hypothesis testing for non-parametric regressions, see Yang et al.. To extend the empirical covariance matrices from finite to infinite dimension, the sample covariance operator is treated as a random element in Banach spaces. The concentrations of empirical covariance operator also have been raised attention in kernel principal components analysis, and functional data analysis, see Rosasco et al., Bunea and Xiao.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Extensions", "weight": 1.0} -->

Testing hypotheses on the regression coefficients are a necessity in measuring the effects of covariates on the certain response variables. Scientists are interested in testing the significance of a large number of covariates simultaneously. From this backgrounds, Zhong and Chen proposed simultaneous tests for coefficients in HD linear models under the "large $p$, small $n$" situations by U-statistics motivated by Chen and Qin. However, their HD tests are asymptotical without a non-asymptotic guarantee. Motivated by Arlot et al., Zhu and Bradic invents a new methodology for testing the linearity hypothesis in HD linear models, and the test they proposed does not impose any restriction of model sparsity. Based on the concentration of Lipschitz functions of Gaussian distributions or strongly log-concave distribution, Zhu developed a new concentration-based test in HD regressions. Recently, Wang et al. studied non-asymptotical two-sample testing using *Projected Wasserstein Distance*, via McDiarmid's inequality.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Extensions", "weight": 1.0} -->

In future, it would be essential and practical to study the estimator for the sub-exponential, sub-Gaussian, sub-Weibull and GBO norms as the unknown parameters when constructing non-asymptotical and data-driven confidence intervals; see Zhang et al.; Wang et al.; Zhou et al..
