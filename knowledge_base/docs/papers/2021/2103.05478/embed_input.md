<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Small Errors in Random Zeroth-order Optimization Are Imaginary

Topics include Optimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Most zeroth-order optimization algorithms mimic a first-order algorithm but replace the gradient of the objective function with some gradient estimator that can be computed from a small number of function evaluations. This estimator is constructed randomly, and its expectation matches the gradient of a smooth approximation of the objective function whose quality improves as the underlying smoothing parameter delta is reduced. Gradient estimators requiring a smaller number of function evaluations are preferable from a computational point of view. While estimators based on a single function evaluation can be obtained by use of the divergence theorem from vector calculus, their variance explodes as delta tends to 0. Estimators based on multiple function evaluations, on the other hand, suffer from numerical cancellation when delta tends to 0. To combat both effects simultaneously, we extend the objective function to the complex domain and construct a gradient estimator that evaluates the objective at a complex point whose coordinates have small imaginary parts of the order delta. As this estimator requires only one function evaluation, it is immune to cancellation. In addition, its variance remains bounded as delta tends to 0.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We prove that zeroth-order algorithms that use our estimator offer the same theoretical convergence guarantees as the state-of-the-art methods. Numerical experiments suggest, however, that they often converge faster in practice.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We study optimization problems of the form

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $f:{\mathcal{D}\rightarrow{\mathbb{R}}}$ is a real analytic and thus smooth objective function defined on an open set $\mathcal{D} \subseteq {\mathbb{R}}^{n}$, and $\mathcal{X} \subseteq \mathcal{D}$ is a non-empty closed feasible set. Throughout the paper we assume that problem (1.1) admits a global minimizer $x^{\star}$ and that the objective function $f$ can only be accessed through a deterministic zeroth-order oracle, which outputs function evaluations at prescribed test points. Under this premise, we aim to develop optimization algorithms that generate a (potentially randomized) sequence of iterates ${x_{1},x_{2},\ldots,x_{K}} \in \mathcal{X}$ approximating $x^{\star}$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

As they only have access to a zeroth-order oracle, these algorithms fall under the umbrella of zeroth-order optimization, derivative-free optimization or, more broadly, black-box optimization, see, e.g.,. As we will explain below and in contrast to all prior work on zeroth-order optimization, we will assume that our zeroth-order oracle also accepts complex inputs beyond $\mathcal{D}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Zeroth-order optimization algorithms are needed when problem (1.1) cannot be addressed with first- or higher-order methods. This is the case when there is no simple closed-form expression for $f$ and its partial derivatives or when evaluating the gradient of $f$ is expensive. In simulation-based optimization, for example, the function $f$ can be evaluated via offline or online simulation methods, but its gradient is commonly inaccessible. Zeroth-order optimization algorithms can also be used for addressing minimax, bandit or reinforcement learning problems, and they lend themselves for hyperparameter tuning in supervised learning. As they can only access function values, zeroth-order optimization methods are inevitably somewhat crude. This simplicity is both a curse and a blessing. On the one hand, it has a detrimental impact on the algorithms' ability to converge to local minima, on the other hand---and this requires further formalization, it may enable zeroth-order methods to escape from saddle points and thus makes them attractive for non-convex optimization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Zeroth-order optimization algorithms can be categorized into direct search methods, model-based methods and random search methods. Direct search methods evaluate the objective function at a set of trial points without the goal of approximating the gradient. A representative example of a direct search method is the popular Nelder--Mead algorithm. Model-based methods use zeroth-order information acquired in previous iterations to calibrate a $C^{r}$-smooth model for some $r \in {\mathbb{Z}}_{\geq 0}$ that approximates the black-box function $f$ locally around the current iterate and then construct the next iterate via $r^{th}$-order optimization methods. These approaches typically attain a higher accuracy than the direct and random search methods, and they have the additional advantage that function evaluations can be re-used. In general, however, they require at least $O{(n)}$ function evaluations in each iteration to construct a well-defined local model \[Ber+21\]. Examples of commonly used models include polynomial models, interpolation models and regression models.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast to model-based methods, random search methods estimate the gradients of $f$ at the iterates directly from finitely many function evaluations and use the resulting estimators as surrogates for the actual gradients in a first-order algorithm. More precisely, random search methods typically approximate $f$ by a smooth function $f_{\delta}$ that is close to $f$ for small $\delta$ and construct an unbiased estimator $g_{\delta}{(x)}$ for ${\nabla f_{\delta}}{(x)}$ by sampling $f$ at test points in the vicinity of $x$. For many popular approximations $f_{\delta}$ there exists $p \geq 1$ such that ${\|{{{\nabla f_{\delta}}{(x)}} - {{\nabla f}{(x)}}}\|} \leq {O{(\delta^{p})}}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In analogy to the model-based methods, $g_{\delta}{(x)}$ can thus be used as a surrogate for the actual gradient in a first-order algorithm. A striking advantage of these random search methods over model-based methods is that the computation of $g_{\delta}{(x)}$ requires only $O{}$ function evaluations, yet at the expense of weaker approximation guarantees \[Liu+20, Ber+21, \]. In principle, the approximation quality of the surrogate gradients (and therefore also the convergence rate of the first-order method at hand) can be improved by reducing the smoothing parameter $\delta$. As $g_{\delta}{(x)}$ is often reminiscent of a difference quotient with increment $\delta$, however, its evaluation is plagued by numerical cancellation. This means that if $\delta$ drops below a certain threshold, innocent round-off errors in the evaluations of $f$ have a dramatic impact on the evaluations of $g_{\delta}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hence, the actual numerical performance of a random search zeroth-order algorithm may fall significantly short of its theoretical performance \[Shi+22\], however, the awareness for this phenomenon seems to be lacking.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inspired by techniques for numerically differentiating analytic functions, we propose here a new smoothed approximation $f_{\delta}$ as well as a corresponding stochastic gradient estimator $g_{\delta}$ that can be evaluated rapidly and faithfully for arbitrarily small values of $\delta$ without suffering from cancellation effects. Integrating the new estimator into the gradient-descent-type algorithm

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

with adaptive stepsize $\mu_{k}$ and smoothing parameter $\delta_{k}$ gives rise to new randomized zeroth-order algorithms. The performance of such algorithms is measured by the decay rate of the regret $R_{K} = {\frac{1}{K}{\sum_{k = 1}^{K}{{\mathbb{E}}\left\lbrack {{f{(x_{k})}} - {f{(x^{\star})}}} \right\rbrack}}}$ as $K$ grows. Here, $x^{\star}$ is a global minimizer, and the expectation ${\mathbb{E}}{\lbrack \cdot \rbrack}$ is taken with respect to the randomness introduced by the algorithm.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Note that if $f$ is convex, then Jensen's inequality ensures that the expected suboptimality gap (or expected optimization error) of the averaged iterate ${\overline{x}}_{K} = {\frac{1}{K}{\sum_{k = 1}^{K}x_{k}}}$ satisfies ${{\mathbb{E}}\left\lbrack {{f{({\overline{x}}_{K})}} - {f{(x^{\star})}}} \right\rbrack} \leq R_{K}$. The main goal of this paper is to understand how $R_{K}$ scales with the total number $K$ of iterations and with critical problem parameters such as the dimension of $x$ or Lipschitz moduli of $f$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Whenever possible (e.g., when $f$ is strongly convex), we also analyze the expected suboptimality gap ${\mathbb{E}}{\lbrack{{f{(x_{K})}} - {f{(x^{\star})}}}\rbrack}$ of the last iterate $x_{K}$. The scaling behavior of $R_{K}$ with respect to $K$ reflects the algorithm's convergence rate. We will show that algorithms of the form (1.2) equipped with the new gradient estimator offer provable convergence rates, are numerically stable, and empirically outperform algorithms that exploit existing smoothed approximations both in terms of accuracy and runtime.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Contributions", "weight": 1.0} -->

Most existing zeroth-order schemes approximate the gradient of $f$ in a way that makes them susceptible to numerical instability. For example, if $f \in {C^{1}{({\mathbb{R}})}}$ is Lipschitz continuous with Lipschitz constant $L$, then, in theory, the finite-difference approximation ${({{f{({x + \delta})}} - {f{(x)}}})}/\delta$ converges to $\partial_{x}{f{(x)}}$ as $\delta > 0$ tends to zero. In practice, however, $f$ can only be evaluated to within machine precision, which means that $f{({x + \delta})}$ and $f{(x)}$ become indistinguishable for sufficiently small $\delta$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Contributions", "weight": 1.0} -->

More precisely, as $f$ is Lipschitz continuous, we have ${|{{f{({x + \delta})}} - {f{(x)}}}|} \leq {L \cdot {|\delta|}}$, and thus cancellation errors are prone to occur when $L \cdot {|\delta|}$ approaches machine precision \[, § 11\]. Other gradient estimators that are based on multiple function evaluations or that involve interpolation schemes suffer from similar cancellation errors. Nevertheless, the convergence guarantees of the corresponding zeroth-order methods require that the smoothing parameter $\delta$ must be driven to zero. For example, \[, Thm. 3.1\] establishes regret bounds under the assumption that the smoothing parameter of a multi-point estimator scales as $\delta_{k} = {O{({1/\sqrt{k}})}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Contributions", "weight": 1.0} -->

The randomized gradient estimator (1.3) avoids cancellation errors because it requires only one single function evaluation---an attractive feature that has, to the best of our knowledge, gone largely unnoticed to date. However, as pointed out earlier, the variance of this estimator diverges as $\delta$ decays, which leads to suboptimal convergence rates. In this paper we propose a numerically stable gradient estimator that enables competitive convergence rates and is immune to cancellation errors. More precisely, we will use complex arithmetic to construct a one-point estimator akin to (1.3) that offers similar approximation and convergence guarantees as state-of-the-art two-point estimators. Maybe surprisingly, we will see that computing this new estimator is not significantly more expensive than evaluating (1.3). Our results critically rely on the assumption that the objective function $f$ is real analytic on its domain $\mathcal{D}$. Recall that $f$ is real analytic if it locally coincides with its multivariate Taylor series.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Contributions", "weight": 1.0} -->

We emphasize that real analyticity does not imply $\beta^{th}$-order smoothness for some $\beta \in {\mathbb{Z}}_{> 0}$ in the sense of \[, § 1.1\], which means that $f$ is almost surely $\beta - 1$ times differentiable and that the ${({\beta - 1})}^{th}$-order term of its Taylor series is globally Lipschitz continuous. We will recall that $f$ can be extended to a complex analytic function $f:{\Omega\rightarrow{\mathbb{C}}}$ defined on some open set $\Omega \subseteq {\mathbb{C}}^{n}$ that covers $\mathcal{D} \subseteq {\mathbb{R}}^{n}$. By slight abuse of notation, this extension is also denoted by $f$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Contributions", "weight": 1.0} -->

Given an oracle that evaluates $f$ at any query point in $\Omega$, we will devise new zeroth-order methods that combine the superior convergence rates and low variances of multi-point schemes reported in \[Duc+15, \] with the numerical robustness of single-point approaches.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Contributions", "weight": 1.0} -->

We now use $R = {\|{x_{1} - x^{\star}}\|}_{2}$ to denote the distance from the initial iterate $x_{1}$ to a minimizer $x^{\star}$ and $F = {{f{(x_{1})}} - {f{(x^{\star})}}}$ to denote the suboptimality of $x_{1}$. Assuming that the objective function $f$ is real analytic and has an $L$-Lipschitz continuous gradient, we will devise zeroth-order methods that offer the following convergence guarantees. If (1.1) represents a (constrained or unconstrained) convex optimization problem with $x^{\star} \in {{int}{(\mathcal{X})}}$, then our algorithm's regret decays as $O{({{nLR^{2}}/K})}$ with the iteration counter $K$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Contributions", "weight": 1.0} -->

If, in addition, $f$ is $\tau$-strongly convex for some $\tau > 0$, then the expected suboptimality decays at the linear rate $O{({{({1 - {\tau/{({4nL})}}})}^{K}LR^{2}})}$. If (1.1) represents a non-convex optimization problem, finally, we establish local convergence to a stationary point and prove that ${{\min_{k \in {\lbrack K\rbrack}}{\mathbb{E}}}{\lbrack{\|{{\nabla f}{(x_{k})}}\|}_{2}^{2}\rbrack}} \leq {O{({{nLF}/K})}}$. All of these convergence rates are qualitatively equivalent to the respective rates reported in \[, Thm. 8\], and they are sharper than the rates provided in \[, § 3\] in the noise-free limit.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Contributions", "weight": 1.0} -->

The latter rely on higher-order smoothness properties of $f$ but do not require $f$ to be analytic. The key difference to all existing methods is that we can drive the smoothing parameter to $0$, e.g., as $\delta_{k} = {\delta/k}$, without risking numerical instability.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Contributions", "weight": 1.0} -->

As highlighted in the recent survey article, an important open question in zeroth-order optimization is whether single-point estimators enable equally fast convergence rates as multi-point estimators. The desire to reap the benefits of multi-point estimators at the computational cost of using single-point estimators has inspired multi-point estimators with memory, which only require a single new function evaluation per call \[Zha+22\]. However, this endeavor has not yet led to algorithms that improve upon the theoretical and empirical performance of the state-of-the-art methods. Filtering techniques inspired by ideas from extremum seeking control can be leveraged to improve the convergence rates obtained in \[Zha+22\] to $O{({n/K^{2/3}})}$. However, this rate is still inferior to the ones reported. To our best knowledge, we propose here the first single-point zeroth-order algorithm that enjoys the same convergence rates as the multi-point methods but often outperforms these methods in experiments. The price we pay for these benefits is the assumption that there exists a zeroth-order oracle accepting complex queries.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Contributions", "weight": 1.0} -->

This assumption is restrictive as it rules out oracles that depend on performing a physical experiment or timing a computational run etc. Nevertheless, as we will see in Section, the approach can excel in the context of simulation-based optimization.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Contributions", "weight": 1.0} -->

Numerical experiments built around standard test problems as well as a model predictive control (MPC) problem corroborate our theoretical results and demonstrate the practical efficiency of the proposed algorithms. Although cancellation effects are caused by rounding to machine precision, which is nowadays of the order $10^{- 16}$, our single-point gradient estimator improves both the accuracy as well as the speed of zeroth-order algorithms already when $\varepsilon$-optimal solutions with $\varepsilon \gg 10^{- 16}$ are sought.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Structure", "weight": 1.0} -->

Section reviews basic tools from multivariate complex analysis and introduces the complex-step method from numerical differentiation. Section then combines smoothing techniques with complex arithmetic to construct a new single-point gradient estimator, and Sections - analyze the favorable convergence rates of zeroth-order optimization methods equipped with the new gradient estimator in the context of convex, strongly convex and non-convex optimization, respectively. Section reports on numerical experiments, and Section concludes.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Example 2.6 (Complex analytic extensions)", "weight": 1.0} -->

Finally, the unique solution $f{(x)}$ to the Lyapunov equation ${f{(x)}} = {{x^{2}f{(x)}} + 1}$ parametrized by $x \in {\mathbb{R}}$ is real analytic on ${\mathbb{R}} \smallsetminus {\{ 1\}}$. It admits the extension

<!-- chunk {"id": "body-0029", "role": "body", "section": "Example 2.6 (Complex analytic extensions)", "weight": 1.0} -->

The next example shows that the domain $\Omega$ of the complex analytic extension is not always representable as ${\mathbb{R}}^{n} + {i \cdot {({- \overline{\delta}},\overline{\delta})}^{n}}$ for some $\overline{\delta} > 0$ even if $\mathcal{D} = {\mathbb{R}}^{n}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Example 2.7 (Non-trivial extension)", "weight": 1.0} -->

To avoid technical discussions of limited practical impact, we will from now on restrict attention to functions $f \in {C^{\omega}{(\mathcal{D})}}$ that admit a complex analytic extension to $\Omega = {{\mathcal{D} \times i} \cdot {({- \overline{\delta}},\overline{\delta})}^{n}}$ for some $\overline{\delta} > 0$. One can show that such an extension always exists if $f \in {C^{\omega}{({\mathbb{R}}^{n})}}$ and $\mathcal{D}$ is bounded or if $f$ is entire, that is, if $f$ has a globally convergent power series representation. The latter condition is restrictive, however, because it rules out simple functions such as ${f{(x)}} = {1/{({1 + x^{2}})}}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Example 2.7 (Non-trivial extension)", "weight": 1.0} -->

Provided there is no risk of confusion, we will sometimes call a real analytic function $f \in C^{\omega}$ and its complex analytic extension simply an analytic function.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Complex-step approximation", "weight": 1.0} -->

The finite-difference method \[Vui+23, Ch. 3\] is arguably the most straightforward approach to numerical differentiation. It simply approximates the derivative of any sufficiently smooth function $f \in {C^{2}{({\mathbb{R}})}}$ by a difference quotient. For example, the forward-difference method uses the approximation

<!-- chunk {"id": "body-0033", "role": "body", "section": "Complex-step approximation", "weight": 1.0} -->

The continuity of the second derivative of $f$ allows for a precise formula for the $O{(\delta)}$ remainder term. However, as explained earlier, the finite difference method suffers from cancellation errors when $\delta$ becomes small. The complex-step approximation proposed in and further refined in \[ Abr+18\] leverages ideas from complex analysis to approximate the derivative of any real analytic function $f \in {C^{\omega}{({\mathbb{R}})}}$ on the basis of one single function evaluation only, thereby offering an elegant remedy for numerical cancellation. Denoting by $u$ and $v$ as usual the real and imaginary parts of the unique complex analytic extension of $f$, which exists thanks to Lemma 2.5. ‣ 2.1 Multivariate complex analysis ‣ 2 Preliminaries ‣ Small errors in random zeroth-order optimization are imaginary"), we observe that $\partial_{x}{f{(x)}}$ equals

<!-- chunk {"id": "body-0034", "role": "body", "section": "Complex-step approximation", "weight": 1.0} -->

where the first and the fourth equalities hold because $f{(x)}$ must be a real number, which implies that ${v{(x,0)}} = 0$, while the second equality follows from the Cauchy-Riemann equations. The derivative $\partial_{x}{f{(x)}}$ can thus be approximated by the fraction ${\Im{({f{({x + {i\delta}})}})}}/\delta$, which requires merely a single function evaluation. To estimate the approximation error, we consider the Taylor expansion

<!-- chunk {"id": "body-0035", "role": "body", "section": "Complex-step approximation", "weight": 1.0} -->

of the unique complex analytic extension of $f$, which exists thanks to Lemma 2.5. ‣ 2.1 Multivariate complex analysis ‣ 2 Preliminaries ‣ Small errors in random zeroth-order optimization are imaginary"). Separating the real and imaginary parts of (2.5) then yields

<!-- chunk {"id": "body-0036", "role": "body", "section": "Complex-step approximation", "weight": 1.0} -->

This reasoning shows that a single complex function evaluation $f{({x + {i\delta}})}$ is sufficient to approximate both $f{(x)}$ as well as $\partial_{x}{f{(x)}}$ without the risk of running into numerical instability caused by cancellation effects. In addition, the respective approximation errors scale quadratically with $\delta$ and are thus one order of magnitude smaller than the error incurred by (2.4). Note also that the complex-step approximation recovers the derivatives of quadratic functions exactly irrespective of the choice of $\delta$. For example, if ${f{(x)}} = x^{2}$, then ${{\Im{({f{({x + {i\delta}})}})}}/\delta} = {2x} = {\partial_{x}{f{(x)}}}$. This insight suggests that the approximation is numerically robust for locally quadratic functions.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Complex-step approximation", "weight": 1.0} -->

The error of the complex-step approximation can be further reduced to $O{(\delta^{4})}$ by enriching it with a finite-difference method. However, the resulting scheme requires multiple function evaluations and is thus again prone to cancellation errors. Unless time is expensive, the standard complex-step approximation therefore remains preferable. The complex-step approximation can also be generalized to handle matrix functions or to approximate higher-order derivatives. Its ramifications for automatic differentiation (AD) are discussed. We return to AD below.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Complex-step approximation", "weight": 1.0} -->

Being immune to cancellation effects, the complex-step approach offers approximations of almost arbitrary precision. For example, software by the UK's National Physical Laboratory is reported to use smoothing parameters as small as $\delta = 10^{- 100}$ \[, p. 44\]. The complex-step approach also emerges in various other domains. For example, it is successfully used in airfoil design. However, its potential for applications in optimization has not yet been fully exploited. Coordinate-wise complex-step approximations with noisy function evaluations show promising performance in line search experiments but come without a rigorous convergence analysis. In addition, the complex-step approach is used to approximate the gradients and Hessians in deterministic Newton algorithms for blackbox optimization models. The potential of leveraging complex arithmetic in mathematical optimization is also mentioned. In this paper we use the complex-step method to construct an estimator akin to (1.3) and provide a full regret analysis. Our approach is most closely related to the recent works, which integrate the complex-step and simultaneous perturbation stochastic approximations into a gradient-descent algorithm and offer a rigorous asymptotic convergence theory.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Complex-step approximation", "weight": 1.0} -->

In contrast, we will derive convergence rates for a variety of zeroth-order optimization problems.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Complex-step approximation", "weight": 1.0} -->

In optimization, the ability to certify that the gradient of an objective function is sufficiently small (i.e., smaller than a prescribed tolerance) is crucial to detect local optima. The following example shows that, with the exception of the complex-step approach, standard numerical schemes to approximate gradients fail to offer such certificates---at least when a high precision is required.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example 2.8 (Numerical stability of gradient estimators)", "weight": 1.0} -->

To showcase the power of the complex-step method and to expose the numerical difficulties encountered by finite-difference methods, we approximate the derivative of ${f{(x)}} = x^{3}$ at $x \in {\{{- 1},0,10\}}$ via a forward-difference ($\mathsf{f}\mathsf{d}$), central-difference ($\mathsf{c}\mathsf{d}$) and complex-step ($\mathsf{c}\mathsf{s}$) method, that is, for small values of $\delta$ we compare ${f_{\mathsf{f}\mathsf{d}}{(x,\delta)}} = {\frac{1}{\delta}{({{f{({x + \delta})}} - {f{(x)}}})}}$, ${f_{\mathsf{c}\mathsf{d}}{(x,\delta)}} =

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 2.8 (Numerical stability of gradient estimators)", "weight": 1.0} -->

Figure 2.1 visualizes the absolute approximation errors as a function of $\delta$. We observe that $f_{\mathsf{c}\mathsf{d}}$ and $f_{\mathsf{c}\mathsf{s}}$ offer the same approximation quality and incur an error of $O{(\delta^{2})}$ for all sufficiently large values of $\delta$. However, only the complex-step approximation reaches machine precision ($\approx 10^{- 16}$), whereas both finite-difference methods deteriorate below $\delta \approx 10^{- 6}$ due to subtractive cancellation errors. Note that for $x = 0$ all errors are equal to $\delta^{2}$ because ${f{}} = 0$. As most existing zeroth-order optimization methods use finite-difference-based gradient estimators, we conclude that there is room for numerical improvements by leveraging complex arithmetic.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Automatic differentiation", "weight": 1.0} -->

The complex-step approach is closely related to automatic differentiation (AD). AD decomposes the evaluation of $f$ into a partially ordered set of elementary operations and evaluates its derivative recursively using the rules of differentiation such as the chain and product rules etc. Moreover, while the complex step approach evaluates $f$ at complex numbers of the form $a + {ib}$ with ${a,b} \in {\mathbb{R}}$ and an abstract imaginary unit $i$ satisfying $i^{2} = {- 1}$, a version of forward-mode AD evaluates $f$ at dual numbers of the form $a + {b\varepsilon}$ with ${a,b} \in {\mathbb{R}}$ and $\varepsilon \neq 0$ an abstract number satisfying $\varepsilon^{2} = 0$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Automatic differentiation", "weight": 1.0} -->

The arithmetics of dual numbers imply that ${f{({x + \varepsilon})}} = {{f{(x)}} + {\varepsilon{\partial_{x}{f{(x)}}}}}$ whenever $f$ is real analytic, and hence one can compute both $f{(x)}$ as well as $\partial_{x}{f{(x)}}$ in one forward pass. Intuitively, $\varepsilon$ should thus be interpreted as a nilpotent infinitesimal unit.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Automatic differentiation", "weight": 1.0} -->

While the set of complex numbers forms a field, the set of dual numbers only forms a ring (in fact, it forms the quotient ring ${{\mathbb{R}}{\lbrack\varepsilon\rbrack}}/\varepsilon^{2}$, which fails to be a field because multiplicative inverses and hence terms such as $\varepsilon^{2}/\varepsilon$ and $\sqrt{\varepsilon^{2}}$ are not defined). The assumptions that $\varepsilon \neq 0$ and $\varepsilon^{2} = 0$ require us to give up the law of the excluded middle and thus also the axiom of choice.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Automatic differentiation", "weight": 1.0} -->

The complex-step approach is computationally cheap, can approximate the derivative of an analytic function $f$ at extremely high accuracy levels (see Figure 2.1) and even remains applicable when function evaluations are noisy. AD is computationally more expensive than the complex-step approach, in settings where the latter applies, yet, AD usually finds the exact derivative of $f$. Whether or not AD will succeed, however, depends on the representation of $f$; see, e.g., \[Hüc+23\] for a discussion of possible pitfalls. That is, AD must be able to evaluate $f$ at all dual numbers of the form $x + \varepsilon$. The following example inspired illustrates why this is restrictive.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Automatic differentiation", "weight": 1.0} -->

For instance, the deep learning toolbox in MATLAB as well as the state-of-the-art AD tools in Julia \[Bez+17\] (e.g., ForwardDiff.jl, Zygote.jl and Enzyme.jl ) or in Python (e.g., JAX \[Bra+18\]) evaluate $\partial_{x}{f{}}$ to NaN, whereas the complex-step method provides a close approximation of the correct value ${\partial_{x}{f{}}} = 0$. We remark that the derivative of ${f{(x)}} = {{sinc}{(x)}}$ is hard-coded in Julia.^11^1 Hence, for AD to succeed the representation of $f$ is critical, that is, $f$ must be defined as ${f{(x)}} = {{sinc}{(x)}}$ instead of ${f{(x)}} = {{\sin{(x)}}/x}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Automatic differentiation", "weight": 1.0} -->

A simpler, yet contrived, example is ${f{(x)}} = {x/x}$, for which the version of AD under consideration evaluates $\partial_{x}{f{}}$ to NaN, too. Note also that AD fails to compute the derivative of ${f{(x)}} = {\exp{({(\sqrt{x^{2}})}^{2})}}$ at $0$ even though there is no division by $0$. All of these problems emerge because the dual numbers form only a ring instead of a field. As pointed out, these theoretical deficiencies of AD could be remedied by working with the Levi-Civita field, whose members generalize the dual numbers and are representable as $\sum_{q \in {\mathbb{Q}}}{a_{q}\varepsilon^{q}}$ with $a_{q} \in {\mathbb{R}}$ for all $q \in {\mathbb{Q}}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Automatic differentiation", "weight": 1.0} -->

Unfortunately, the members of the Levi-Civita field do not admit a finite representation in general and are therefore difficult to handle computationally.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Lipschitz inequalities", "weight": 1.0} -->

In order to be able to design reasonable zeroth-order optimization algorithms, we need to impose some regularity on the objective function $f$. This is usually done by requiring $f$ to display certain Lipschitz continuity properties. Following, for any integers ${p,k} \geq 0$ with $p \leq k$, we thus use $C_{L}^{k,p}{(\mathcal{D})}$ to denote the family of all $k$ times continuously differentiable functions on $\mathcal{D}$ whose $p^{th}$ derivative is Lipschitz continuous with Lipschitz constant $L \geq 0$. Similarly, we use $C_{L}^{\omega,p}{(\mathcal{D})}$ to denote the family of all analytic functions in $C_{L}^{p,p}{(\mathcal{D})}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Lipschitz inequalities", "weight": 1.0} -->

For example, if $f \in {C_{L_{1}}^{1,1}{(\mathcal{D})}}$, then $f$ has a Lipschitz continuous gradient, that is,

<!-- chunk {"id": "body-0052", "role": "body", "section": "Lipschitz inequalities", "weight": 1.0} -->

By \[, Eq. \], this condition is equivalent to the inequality

<!-- chunk {"id": "body-0053", "role": "body", "section": "Lipschitz inequalities", "weight": 1.0} -->

If $f \in {C_{L_{1}}^{1,1}{(\mathcal{D})}}$ is also convex then, the Lipschitz condition (2.6) is also equivalent to

<!-- chunk {"id": "body-0054", "role": "body", "section": "Lipschitz inequalities", "weight": 1.0} -->

By \[, Lem. 1.2.4\], this condition is equivalent to the inequality

<!-- chunk {"id": "body-0055", "role": "body", "section": "Lipschitz inequalities", "weight": 1.0} -->

More generally, any $f \in {C_{L_{p}}^{p,p}{(\mathcal{D})}}$ has a Lipschitz continuous $p^{th}$ derivative. Recalling the definitions of higher-order partial derivatives and multi-indices, this requirement can be expressed as

<!-- chunk {"id": "body-0056", "role": "body", "section": "A smoothed complex-step approximation", "weight": 1.0} -->

We now use ideas from to construct a new gradient estimator, which can be viewed as a complex-step generalization of the estimators proposed. Our construction is based on the following assumption, which we assume to hold throughout the rest of the paper.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Assumption 3.1 (Analytic extension)", "weight": 1.0} -->

Recall from Lemma 2.5. ‣ 2.1 Multivariate complex analysis ‣ 2 Preliminaries ‣ Small errors in random zeroth-order optimization are imaginary") that $f$ admits an analytic extension to some open set $\Omega \subseteq {\mathbb{C}}^{n}$ covering $\mathcal{D}$ whenever $f \in {C^{\omega}{(\mathcal{D})}}$. However, unless $f$ is entire or $\mathcal{D}$ is bounded, $\Omega$ may not contain a strip of the form envisaged in Assumption 3.1. ‣ 3 A smoothed complex-step approximation ‣ Small errors in random zeroth-order optimization are imaginary"). Hence, this assumption is not automatically satisfied for any real analytic function $f \in {C^{\omega}{(\mathcal{D})}}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Assumption 3.1 (Analytic extension)", "weight": 1.0} -->

The requirement $\overline{\delta} \in {}$ is unrestrictive and has the convenient consequence that $\delta^{p} \leq \delta^{p - 1}$ for any $\delta \in {(0,\overline{\delta})}$ and $p \in {\mathbb{Z}}_{\geq 0}$. All subsequent results are based on a smoothed complex-step approximation $f_{\delta}$ of $f$, which is defined through

<!-- chunk {"id": "body-0059", "role": "body", "section": "Assumption 3.1 (Analytic extension)", "weight": 1.0} -->

Here, the radius $\delta \in {(0,\overline{\delta})}$ of the ball used for averaging represents a tuneable smoothing parameter. Given prior structural knowledge about $f$, one could replace ${\mathbb{B}}^{n}$ with a different compact set. We emphasize that the integral in (3.1) is well-defined whenever $\delta \in {(0,\overline{\delta})}$, which ensures that $f$ has no singularities in the integration domain. Next, we address the approximation quality of $f_{\delta}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Example 3.6 (Loss of convexity)", "weight": 1.0} -->

If $f \in {C^{\omega}{({\mathbb{R}})}}$ is entire, then it has a globally convergent power series representation with real coefficients. Consequently, $f$ satisfies

<!-- chunk {"id": "body-0061", "role": "body", "section": "Example 3.6 (Loss of convexity)", "weight": 1.0} -->

If $f_{\delta}$ inherited convexity from $f$, one could simply incorporate the estimator (3.4) into the algorithms studied in \[, § 5\], and the corresponding convergence analysis would carry over with minor modifications. As the smoothed complex-step approximation may destroy convexity, however, a different machinery is needed here.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Convex optimization", "weight": 1.0} -->

We now study the convergence properties of zeroth-order algorithms for solving problem (1.1) under the assumption that $f$ is a convex function on $\mathcal{D}$ and $\mathcal{X}$ is a non-empty closed convex subset of $\mathcal{D}$. Our methods mimic existing algorithms developed but use the single-point estimator $g_{\delta}$ defined in (3.4) instead of a multi-point estimator that may suffer from cancellation effects. Our method is described in Algorithm 4.1, where $\Pi_{\mathcal{X}}:{\mathcal{D}\rightarrow\mathcal{X}}$ denotes the Euclidean projection onto $\mathcal{X}$. Note that $\Pi_{\mathcal{X}}$ reduces to the identity operator if $\mathcal{X} = \mathcal{D}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Non-convex optimization", "weight": 1.0} -->

We now extend the convergence guarantees for Algorithm 4.1 to unconstrained non-convex optimization problems. Our proof strategy differs from the one as the smoothed objective function $f_{\delta}$ does not necessarily admit a Lipschitz continuous gradient. In this setting, convergence can still be guaranteed if the initial iterate $x_{1}$ is sufficiently close to some global minimizer $x^{\star}$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

We will now assess the empirical performance of different variants of Algorithm 4.1 equipped with different gradient estimators on standard test problems. Specifically, we will compare the proposed complex-step estimator $g_{\mathsf{c}\mathsf{s}}$ defined in (3.4) against the forward-difference estimator

<!-- chunk {"id": "body-0065", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

both of which rely on Gaussian smoothing \[, Eq. \]; see also Example 2.8. ‣ 2.2 Complex-step approximation ‣ 2 Preliminaries ‣ Small errors in random zeroth-order optimization are imaginary"). As pointed out in the introduction, the single-point estimator (1.3) displays a higher variance and thus leads to slow convergence, in general. Therefore, we exclude it from the numerical experiments. When using $g_{\mathsf{f}\mathsf{d}}$ or $g_{\mathsf{c}\mathsf{d}}$, we set the stepsize of Algorithm 4.1 to $\mu_{k} = {1/{({4{({n + 4})}L_{1}})}}$ as recommended in \[, Eq. \]. When using $g_{\mathsf{c}\mathsf{s}}$, on the other hand, we select the stepsize in view of the structural properties of the given objective function $f$ in accordance with Theorems 4.2.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

‣ 4 Convex optimization ‣ Small errors in random zeroth-order optimization are imaginary"), 5.1. ‣ 5 Strongly convex optimization ‣ Small errors in random zeroth-order optimization are imaginary") and 6.1. ‣ 6 Non-convex optimization ‣ Small errors in random zeroth-order optimization are imaginary"). We recall that when $\delta_{k}$ is fixed, $\delta_{k} \approx 10^{- 8}$ is optimal for $g_{\mathsf{f}\mathsf{d}}$ whereas $\delta_{k} \approx 10^{- 5}$ is optimal for $g_{\mathsf{c}\mathsf{d}}$, cf. Figure 0(a) ‣ Figure 2.1 ‣ 2.2 Complex-step approximation ‣ 2 Preliminaries ‣ Small errors in random zeroth-order optimization are imaginary"). Also, the initial iterate $x_{1}$ is always set to $0$ unless stated otherwise.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

All experiments are performed in MATLAB on a x86_64 machine with a 4 GHz CPU and 16 GB RAM, using double precision, that is, machine precision is $2^{- 52} \approx {2.2204 \cdot 10^{- 16}}$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

From Sections -- we know that Algorithm 4.1 with $g_{\mathsf{c}\mathsf{s}}$ is guaranteed to find stationary points of a wide range of convex and non-convex optimization problems provided that its stepsize is inversely proportional to the Lipschitz constant $L_{1}$ of the gradient of $f$. Implementing Algorithm 4.1 in practice thus requires knowledge of $L_{1}$. Unfortunately, the Lipschitz modulus of $f$ is typically unknown in the context of zeroth-order optimization, and the results of Sections -- indicate that increasing $L_{1}$ increases the number of iterations and decreases the smoothing parameter $\delta$ needed to attain a desired suboptimality gap $\epsilon$. These insights are consistent with classical results in zeroth-order optimization based on multi-point gradient estimators such as $g_{\mathsf{f}\mathsf{d}}$ or $g_{\mathsf{c}\mathsf{d}}$ (cf. ).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

As the complex-step method proposed in this paper remains numerically stable for almost arbitrarily small smoothing parameters $\delta$, it may thus be preferable to classical methods when $L_{1}$ is overestimated.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

The experiments will show that if $\delta$ is sufficiently large for multi-point methods to be applicable, then our complex-step method converges equally fast or faster than the multi-point methods, which obey the theoretical convergence rates reported. A theoretical explanation for the better empirical transient convergence behavior of the complex-step method is left for future work.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

(c) Cost $f{({\overline{x}}_{K})}$ for the log loss function (7.2).

<!-- chunk {"id": "body-0072", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

(d) Cost f(xK) for the log loss function (7.2).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Example 7.1 (Quadratic test function)", "weight": 1.0} -->

Assume that $\mathcal{X} = {\mathbb{R}}^{n}$ and $f$ is an ill-conditioned version of what Nesterov calls the 'worst function in the world' \[, § 2.1.2\], that is, assume that

<!-- chunk {"id": "body-0074", "role": "body", "section": "Example 7.1 (Quadratic test function)", "weight": 1.0} -->

where $n = 5$, $L = 10^{- 8}$, and $x^{(j)}$ denotes the $j^{th}$ component of $x$ for any $j \leq n$. One can show that $\nabla f$ has Lipschitz modulus $L_{1} = {4L}$ and that the unique global minimizer $x^{\star}$ of $f$ has coordinates ${(x^{\star})}^{(j)} = {1 - {j/{({n + 1})}}}$. In this case, the theoretical convergence guarantees of Algorithm 4.1 are independent of whether $g_{\mathsf{c}\mathsf{s}}$ or $g_{\mathsf{f}\mathsf{d}}$ is used.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Example 7.1 (Quadratic test function)", "weight": 1.0} -->

However, starting from $x_{1} = 0$ and gradually reducing the smoothing parameter $\delta_{k} = \delta$ towards machine precision exposes the advantages of the one-point estimator $g_{\mathsf{c}\mathsf{s}}$ over the multi-point estimator $g_{\mathsf{f}\mathsf{d}}$. Figures 0(a) ‣ Figure 7.1 ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary") and 0(b) ‣ Figure 7.1 ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary") visualize the suboptimality gap of ${\overline{x}}_{K}$ and $x_{K}$ as a function of $K$ along a single sample trajectory, respectively. Note that especially the performance of $x_{K}$ is significantly better when $g_{\mathsf{c}\mathsf{s}}$ is used.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Example 7.1 (Quadratic test function)", "weight": 1.0} -->

One might argue that, despite using the optimal $\delta \approx 10^{- 8}$, $g_{\mathsf{f}\mathsf{d}}$ leads to a higher suboptimality gap than $g_{\mathsf{c}\mathsf{s}}$ because of its inferior approximation quality; see, e.g., Figure 2.1. We shed more light on this conjecture in Example 7.3. ‣ 7.1 Unconstrained convex optimization ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary"), where we compare $g_{\mathsf{c}\mathsf{s}}$ against $g_{\mathsf{c}\mathsf{d}}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Example 7.2 (Logistic regression)", "weight": 1.0} -->

Assume that $\mathcal{X} = {\mathbb{R}}^{n}$ and $f$ is the log loss function used to quantify the prediction loss in logistic regression. Specifically, set

<!-- chunk {"id": "body-0078", "role": "body", "section": "Example 7.2 (Logistic regression)", "weight": 1.0} -->

for $m = 100$ and $n = 2$, and assume that the features $a_{i}$ and the labels $v_{i}$ are sampled independently from the standard normal distribution on ${\mathbb{R}}^{n}$ and the uniform distribution on $\{{- 1},1\}$, respectively. Denoting by $A \in {\mathbb{R}}^{m \times n}$ the matrix with rows $a_{i}^{\mathsf{T}}$ for all $i \leq m$, one readily verifies that $L_{1} = {\frac{1}{m}{\| A\|}_{2}}$. We compare again the empirical convergence properties of Algorithm 4.1 equipped with $g_{\mathsf{c}\mathsf{s}}$ or $g_{\mathsf{f}\mathsf{d}}$.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Example 7.2 (Logistic regression)", "weight": 1.0} -->

Figures 0(c) ‣ Figure 7.1 ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary") and 0(d) ‣ Figure 7.1 ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary") visualize the objective function values of ${\overline{x}}_{K}$ and $x_{K}$ as a function of $K$. We observe that the cancellation effects in the cost of ${\overline{x}}_{K}$ are mild even if $g_{\mathsf{f}\mathsf{d}}$ is used and $\delta_{k} = \delta$ is small, whereas those in the cost of $x_{K}$ are significantly more pronounced.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Constrained convex optimization", "weight": 1.0} -->

The next example revolves around a constrained optimization problem grounded in optimal control. We remark that the (unconstrained) infinite-horizon version of this problem could be addressed with the policy iteration scheme proposed in \[Faz+18, Mal+19\].

<!-- chunk {"id": "body-0081", "role": "body", "section": "Example 7.4 (Policy iteration)", "weight": 1.0} -->

We now address the MPC problem

<!-- chunk {"id": "body-0082", "role": "body", "section": "Example 7.4 (Policy iteration)", "weight": 1.0} -->

with planning horizon $T \in {\mathbb{Z}}_{\geq 0}$ and initial state $s_{0} \in {\mathbb{R}}^{n_{s}}$. Note that the dynamic constraints in (7.3. ‣ 7.2 Constrained convex optimization ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary")) can be used to express the state trajectory $s = {\{ s_{t}\}}_{t = 0}^{T}$ as an affine function of the $n$-dimensional input trajectory $x = {\{ x_{t}\}}_{t = 0}^{T - 1}$ with $n = {Tn_{x}}$. We can thus eliminate $s$ and express the objective function of (7.3. ‣ 7.2 Constrained convex optimization ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary")) as a quadratic function $f{(x)}$ of the inputs $x$ alone.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Example 7.4 (Policy iteration)", "weight": 1.0} -->

Similarly, we can identify the feasible set of (7.3. ‣ 7.2 Constrained convex optimization ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary")) with the compact hypercube $\mathcal{X} = {\{{x \in {\mathbb{R}}^{n}}:{{\| x\|}_{\infty} \leq 1}\}}$. Hence, the MPC problem (7.3. ‣ 7.2 Constrained convex optimization ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary")) constitutes an instance of (1.1). We further assume that the cost matrices $Q \succeq 0$ and $R \succ 0$ are known, that the system matrices $A$ and $B$ are unknown, and that the costs of a given input trajectory $x$ can be evaluated by simulation. This implies that $f$ is unknown but admits a zeroth-order oracle.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Example 7.4 (Policy iteration)", "weight": 1.0} -->

Throughout this experiment we set $(A,B,Q,R)$ to the standard two-dimensional MPC instance^22^2 in Yalmip \[Löf04\], and we set $T = 15$ and $s_{0} = {}$. We emphasize that the optimal solution of (1.1) may reside on the boundary of $\mathcal{X}$, and thus the theoretical guarantees of Sections and do not apply. Nevertheless, we will show that Algorithm 4.1 performs better when the complex-step estimator $g_{\mathsf{c}\mathsf{s}}$ is used instead of the central-difference estimator $g_{\mathsf{c}\mathsf{d}}$. We initialize the algorithm at the origin and upper bound the Lipschitz modulus of $\nabla f$ by $L_{1} = {4 \cdot 10^{4}}$. This crude bound is merely based on the operator norms of $A$ and $B$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Example 7.4 (Policy iteration)", "weight": 1.0} -->

Figure 2(a) ‣ Figure 7.3 ‣ 7.2 Constrained convex optimization ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary") visualizes the suboptimality gap of $x_{K}$ as a function of $K$. The oscillations in the suboptimality gap corresponding to $g_{\mathsf{c}\mathsf{s}}$ emerge because the optimizer $x^{\star}$ of (7.3. ‣ 7.2 Constrained convex optimization ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary")) resides on the boundary of $\mathcal{X}$. Note that Theorems 4.2. ‣ 4 Convex optimization ‣ Small errors in random zeroth-order optimization are imaginary") and 5.1. ‣ 5 Strongly convex optimization ‣ Small errors in random zeroth-order optimization are imaginary") do not apply even though $f$ is strongly convex. The reason is again that ${{\nabla f}{(x^{\star})}} \neq 0$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Example 7.4 (Policy iteration)", "weight": 1.0} -->

Convergence results for optimization problems with boundary solutions have recently been obtained by allowing the stepsize $\mu_{k}$ to decay with $k$. These results even hold if we have only access to noisy function evaluations. We thus solve problem (7.3. ‣ 7.2 Constrained convex optimization ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary")) once again with Algorithm 4.1 and the complex-step estimator $g_{\mathsf{c}\mathsf{s}}$ but set $\mu_{k} = {1/k}$ instead of $\mu_{k} = {1/{({2nL_{1}})}}$, both for $\delta_{k} = {\delta/k}$ with $\delta = 10^{- 5}$. In this case, guarantees the suboptimality gap to decay as $O{({1/K})}$.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Example 7.4 (Policy iteration)", "weight": 1.0} -->

Figure 2(a) ‣ Figure 7.3 ‣ 7.2 Constrained convex optimization ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary") empirically validates this theoretical result. Note also that initial convergence is slower under a harmonically decaying stepsize. Figure 2(b) ‣ Figure 7.3 ‣ 7.2 Constrained convex optimization ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary") shows the state trajectories corresponding to differently computed inputs $x_{K}$ for $K = {5 \cdot 10^{4}}$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Example 7.4 (Policy iteration)", "weight": 1.0} -->

(b) State trajectories generated by the control policies.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Example 7.4 (Policy iteration)", "weight": 1.0} -->

(d) Paths of iterates starting at four different initial points.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Non-convex optimization", "weight": 1.0} -->

We finally apply our method to a classical non-convex test problem.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Example 7.5 (Rosenbrock function)", "weight": 1.0} -->

We compare the complex-step estimator $g_{\mathsf{c}\mathsf{s}}$ against $g_{\mathsf{c}\mathsf{d}}$ but remark that the convergence behavior of Algorithm 4.1 does not change noticeably when $g_{\mathsf{f}\mathsf{d}}$ is replaced with $g_{\mathsf{c}\mathsf{d}}$. We also set $x_{1}$ to one of four different points in $\mathcal{X}$ as visualized in Figure 2(d) ‣ Figure 7.3 ‣ 7.2 Constrained convex optimization ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary").

<!-- chunk {"id": "body-0092", "role": "body", "section": "Example 7.5 (Rosenbrock function)", "weight": 1.0} -->

Figures 2(c) ‣ Figure 7.3 ‣ 7.2 Constrained convex optimization ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary") and 2(d) ‣ Figure 7.3 ‣ 7.2 Constrained convex optimization ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary") show the convergence of the suboptimality gap of $x_{K}$ and the paths of iterates generated by Algorithm 4.1, respectively. Again, the complex-step estimator $g_{\mathsf{c}\mathsf{s}}$ leads to significantly faster convergence. An additional acceleration can be achieved by decreasing $\delta$ below $10^{- 5}$. In this case, however, the Gaussian smoothing method eventually breaks down. We point out that, compared to other derivative-free approaches such as the Nelder-Mead algorithm, the convergence is slow, and future work should aim at improving our understanding of the relative merits of these methods, e.g., fast empirical convergence (Nelder-Mead algorithm) versus slower but guaranteed convergence (Algorithm 4.1).

<!-- chunk {"id": "body-0093", "role": "body", "section": "Outlook", "weight": 1.0} -->

To close the paper, we discuss potential applications of our methods in the context of simulation-based optimization, where evaluating the objective function $f$ requires the solution of an ordinary differential equation (ODE) or a partial differential equation (PDE). This section is illustrative only, and additional work is required to derive rigorous convergence guarantees. We start with an optimization problem involving an ODE, which---due to its chaotic nature---often serves as a benchmark problem in the dynamical systems literature; see, e.g.,.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Example 7.6 (Lorenz system)", "weight": 1.0} -->

is commonly known as the Lorenz system \[, Ch. 9\]. It was developed as a stylized model of atmospheric convection, with $\ell_{1}$, $\ell_{2}$ and $\ell_{3}$ representing the rate of convection, the horizontal temperature variation and the vertical temperature variation, respectively. However, the Lorenz system also arises in the study of chemical reactions, population dynamics or electric circuits etc. In the following we denote by $\varphi^{t}{(x)}$ the time-$t$ state of a Lorenz system with initial state ${\ell{}} = x$. Given a potentially noisy measurement $p$ of the state at time $t \geq 0$, a problem of practical interest is to estimate the initial state $x$ that led to $p$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Example 7.6 (Lorenz system)", "weight": 1.0} -->

If $x$ is known to belong to a closed set $\mathcal{X} \subseteq {\mathbb{R}}^{3}$, then it can conveniently be estimated by solving an instance of problem (1.1) with objective function ${f{(x)}} = {\|{p - {\varphi^{t}{(x)}}}\|}_{2}^{2}$ and feasible set $\mathcal{X}$. We expect this problem to be challenging because the Lorenz system is known to be chaotic. Thus, slight changes in the initial state have a dramatic impact on the future trajectory. Moreover, the objective function is not available in closed form but must be evaluated with a numerical ODE solver. As all commonly used ODE solvers map the initial state $x$ to an approximation of $\varphi^{t}{(x)}$ by recursively applying analytic (in fact, polynomial) transformations, the resulting instance of problem (1.1) can be addressed with Algorithm 4.1.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Example 7.6 (Lorenz system)", "weight": 1.0} -->

We remark that most out-of-the-box ODE solvers accept complex-valued initial conditions. Here we use MATLAB's ode45 routine.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Example 7.6 (Lorenz system)", "weight": 1.0} -->

Finally, we sample the initial iterate $x_{1}$ from the uniform distribution on the boundary of $\mathcal{X}$, use $L_{1} = {1,000}$ as a conservative estimate for the Lipschitz modulus of $\nabla f$ and set the smoothing parameter to $\delta = 10^{- 10}$. By Theorem 6.1. ‣ 6 Non-convex optimization ‣ Small errors in random zeroth-order optimization are imaginary"), Algorithm 4.1 converges to a stationary point $x^{\star}$ of the objective function with ${{\nabla f}{(x^{\star})}} = 0$ provided that ${\|{{\nabla f}{(x_{1})}}\|}_{2}$ is sufficiently small. See the discussion below Example 7.4. ‣ 7.2 Constrained convex optimization ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary") for the case ${{\nabla f}{(x^{\star})}} \neq 0$.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Example 7.6 (Lorenz system)", "weight": 1.0} -->

Figure 3(a) ‣ Figure 7.4 ‣ Example 7.6 (Lorenz system). ‣ 7.4 Outlook ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary") shows the decay of $f{(x_{K})}$ with the total number $K$ of iterations for 10 independent simulation runs. Figure 3(b) ‣ Figure 7.4 ‣ Example 7.6 (Lorenz system). ‣ 7.4 Outlook ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary") visualizes the corresponding state trajectories^33^3A video of the state evolution is available from ${\{{\varphi^{t}{(x_{K})}}\}}_{t \in {\lbrack 0,2\rbrack}}$ for $K = 10^{5}$. Only 6 of the 10 trajectories are shown for better visibility.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Example 7.6 (Lorenz system)", "weight": 1.0} -->

(a) Decay of f(xK) with the total number K of iterations for 10 independent simulation runs.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Example 7.6 (Lorenz system)", "weight": 1.0} -->

(b) Trajectories of (7.4) starting from ℓ (unknown), x0 (initial) and xK for K = 105 (optimized).

<!-- chunk {"id": "body-0101", "role": "body", "section": "Example 7.6 (Lorenz system)", "weight": 1.0} -->

To close this section, we highlight that the complex-step method offers distinct benefits in the context of simulation-based optimization, where the objective function $f$ can only be evaluated within prescribed error tolerances. In Example 7.6. ‣ 7.4 Outlook ‣ 7 Numerical experiments ‣ Small errors in random zeroth-order optimization are imaginary"), for instance, the evaluation of $f$ is corrupted by ODE integration errors. Unfortunately, such errors can have a detrimental impact on classical finite-difference-based optimization schemes. Indeed, the central-difference estimator $\frac{1}{2\delta_{k}}{({{f{({x_{k} + {\delta_{k}y_{k}}})}} - {f{({x_{k} - {\delta_{k}y_{k}}})}}})}y_{k}$ for ${\nabla f}{(x_{k})}$ is useless for optimization unless the numerical errors in the evaluation of $f$ are significantly smaller than $\delta_{k}$.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Example 7.6 (Lorenz system)", "weight": 1.0} -->

As $\delta_{k}$ must decay to $0$ as $k$ grows, so must the numerical tolerances. Otherwise, the ODE integration errors would dominate, which could be seen as another manifestation of catastrophic cancellation. Inexact evaluations of $f$ can conveniently be modeled as outputs of a noisy zeroth-order oracle. While this paper was under review, it has been shown that convergence guarantees for Algorithm 4.1 can be obtained even if the complex zeroth-order oracle is affected by independently and identically distributed noise and even if the sequence of smoothing parameters ${\{\delta_{k}\}}_{k \in {\mathbb{Z}}_{> 0}}$ is chosen independently of the noise statistics. This provides strong evidence that the complex-step approach may be able to overcome the practical obstructions outlined above that plague classical finite-difference schemes in simulation-based optimization. As integration errors are arguably not purely random and serially independent, however, further research is needed.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Example 7.6 (Lorenz system)", "weight": 1.0} -->

We highlight that complex-step derivatives are routinely used in PDE-constrained optimization. For example, they are used in a recent airfoil optimization package^44^4 developed in 2021. The underlying algorithm relies on sequential quadratic programming \[, Ch. 18\] and assumes that the complex-step derivative equals the gradient. In contrast, our analysis provides a rigorous treatment of approximation errors.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Example 7.6 (Lorenz system)", "weight": 1.0} -->

Additional applications of the complex-step derivative are discussed in \[, § 3.2\].

<!-- chunk {"id": "body-0105", "role": "body", "section": "Conclusions and future work", "weight": 1.0} -->

The cancellation effects that plague all multi-point gradient estimators tend to have a detrimental effect on the numerical stability and the convergence behavior of zeroth-order algorithms. These numerical problems can sometimes be mitigated by replacing the terminal iterate $x_{K}$ with the averaged iterate ${\overline{x}}_{K} = {\frac{1}{K}{\sum_{k = 1}^{K}x_{k}}}$, at the cost of slower convergence. The single-point complex-step gradient estimator thus provides an attractive alternative to the classical gradient estimators because it leads to provably fast and numerically stable algorithms. As pointed out, smoothness is not a necessary condition for the applicability of the complex-step approximation, which suggests that the analyticity assumption used in this paper can perhaps be relaxed. Other promising research directions would be to extend our convergence guarantees to the class of weakly convex functions and to investigate multi-batch as well as online settings.
