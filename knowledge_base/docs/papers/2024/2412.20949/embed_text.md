<!-- arxiv-full-text:v1 {"arxiv_id": "2412.20949", "source": "arxiv-html"} -->

## Abstract

We prove a Bernstein inequality for vector-valued self-normalized martingales. We first give an alternative perspective of the corresponding sub-Gaussian bound due to Abbasi-Yadkori et al. via a PAC-Bayesian argument with Gaussian priors. By instantiating this argument to priors drawn uniformly over well-chosen ellipsoids, we obtain a Bernstein bound.

## Tail Bounds for Self-Normalized Martingales

Deviation inequalities for self-normalized martingales play a key role in obtaining guarantees for linear regression in interactive and sequential decision-making tasks, such as learning an autoregression or regret minimization in linear bandits. The most prevalent version of such an inequality currently in use is due to Abbasi-Yadkori et al. and rests on the method of pseudo-maximization popularized by Peña et al., dating back to Robbins and Siegmund. Comparing their result to the central limit theorem, their bound is nearly optimal but depends on the sub-Gaussian variance proxy instead of the actual variance. In this note, we overcome this issue by casting the pseudo-maximization technique through the lens of the PAC-Bayesian inequality. The present approach simplifies classical pseudo-maximization by relegating the complexity of evaluating exponential integrals against the smoothing distribution to the computation of a generic Kullback-Liebler divergence term. This allows us to generalize the argument of Abbasi-Yadkori et al. but without access to globally defined moment generating function bounds.

Let us now proceed by describing the setting of our result and that of Abbasi-Yadkori et al.. Fix a filtration $\mathcal{F}_{0:\infty}$ and two square-integrable processes: $X_{1:\infty}$, taking values in ${\mathbb{R}}^{d}$, and $W_{1:\infty}$, taking values in $\mathbb{R}$. For each $T \in {\mathbb{N}}$, let $X_{1:T}$ be adapted to $\mathcal{F}_{0:{T - 1}}$ and $W_{1:T}$ to $\mathcal{F}_{1:T}$ with ${\mathbf{E}{\lbrack\left. W_{k} \middle| \mathcal{F}_{k - 1} \right.\rbrack}} = 0$ for every $k \in {\mathbb{N}}$. For $t \in {\mathbb{N}}$, we define: and are interested in bounds on the random walk $S_{T}$ in the random Mahalanobis norm ${\| S_{T}\|}_{{({V_{T} + \Gamma})}^{- 1}}^{2} = {S_{T}^{\mathsf{T}}{({V_{T} + \Gamma})}^{- 1}S_{T}}$ for some fixed positive semidefinite matrix $\Gamma \succeq 0$. This is called a *self-normalized martingale*. Under the assumption that $W_{k}$ is $\mathcal{F}_{k - 1}$-conditionally $\sigma_{subG}^{2}$-sub-Gaussian for each $k \in {\mathbb{N}}$,^11^1${{{\mathbf{E}\left\lbrack {\exp\left({\lambda W_{k}} \right)} \middle| \mathcal{F}_{k - 1} \right\rbrack} \leq {\exp\left(\frac{\lambda^{2}\sigma_{subG}^{2}}{2} \right)}},{{\forall k} \in {\mathbb{N}}}}.$ Abbasi-Yadkori et al. show that for every stopping time $\tau$ ($\in \mathcal{F}_{0:\infty}$) and with probability $1 - \delta$: Their approach rests on an elegant application of the pseudo-maximization technique developed by Peña et al., dating back to Robbins and Siegmund. While elegant, the result of Abbasi-Yadkori et al. has one shortcoming as compared to classical asymptotics: the linear dependence on the conditional variance proxy $\sigma_{subG}^{2}$ as opposed to the conditional variance, $\sigma_{var}^{2} \triangleq {\sup{\{{\left. {\mathbf{E}{\lbrack\left. W_{k}^{2} \middle| \mathcal{F}_{k - 1} \right.\rbrack}} \middle| {\text{~a.s.,~}k} \right. \in T}\}}}$. The traditional fix to this in the literature on concentration inequalities is to invoke a Bernstein-type bound on the moment generating function (MGF) of the $W_{k}$ instead of a Hoeffding type of bound. Unfortunately, directly combining a Bernstein MGF bound with the pseudo-maximization technique does not lead to analytically tractable upper bounds as it requires the evaluation of an exponential integral over a bounded domain (an ellipsoid). Moreover, previous attempts at establishing Bernstein bounds (via methods orthogonal to pseudo-maximization) for vector-valued self-normalized martingales suffer from extraneous logarithmic dependencies and have significantly looser constants.

In this note, we provide an alternative perspective on the proof of (1.2), where, instead of computing the exponential integral directly, we invoke the variational characterization of Kullback-Liebler divergence via the PAC-Bayesian lemma to relegate this difficulty to the calculation of said divergence. Beyond Gaussian priors, this turns out to be significantly simpler than the evaluation of an exponential integral. It allows us to modularize the proof strategy of Abbasi-Yadkori et al. and replace their Gaussian prior with uniform ellipsoidal priors that are suitable in combination with exponential inequalities that only hold for a restricted domain (contrast this with Hoeffding MGF bounds being valid for all $\lambda$).

The rest of this note is organized as follows. We state our main result immediately below and then proceed to discuss its consequences. Its proof is given in Section 2.2. Preliminaries relating to our application of the PAC-Bayesian lemma are given in Section 2 where we also provide a proof of (1.2) as a warm-up. Auxiliary lemmata are proven in Section 3.

### The Result

To apply a Bernstein MGF bound, we will require some additional boundedness assumptions. Namely, we posit that: for a positive scalar $B_{W}$ and a positive definite matrix $B_{X}$.

### Theorem 1

Fix ${\delta,\varepsilon,\nu} \in {}$, a stopping time $\tau$ with respect to $\mathcal{F}_{0:\infty}$, a positive semidefinite matrix $\Gamma \succeq 0$, a positive definite matrix $V \succ 0$ and assume that (1.3) holds. Define Then as long as ${V_{\tau} + \Gamma} \succeq {e{({1 + \nu})}^{2}V} \succeq {{({1 + \nu})}^{2}\varepsilon^{- 1}{({d + 2})}B_{W}^{2}B_{X}^{2}}$ we that with probability at least $1 - \delta$:

### Remarks on Theorem 1

When $\Gamma = 0$, requiring $\alpha = 0$ in Theorem 1 can be thought of as a burn-in requirement, restricting the Bernstein inequality to cases in which the corresponding least squares error is sufficiently small. Typically, $\alpha = 0$ once the sample size is large enough as ${\| S_{\tau}\|}_{V_{\tau}^{- 2}}^{2}$ is the norm-squared error of the least squares estimator in the model $Y_{k} = {{\langle\theta_{\star},X_{k}\rangle} + W_{k}}$ up to time $\tau$. When $S_{\tau}$ is not too large, the variance proxy $\sigma_{subG}^{2}$ in (1.2) can thus be replaced by the variance term $\sigma_{var}^{2}$ with just a little overhead in $\varepsilon$.

For $\Gamma \succeq {\varepsilon^{- 1}e^{- 1}{({d + 2})}B_{W}^{2}B_{X}^{2}}$ (corresponding instead to ridge regression) one may choose $V = \Gamma$ and use (1.2) to control $\alpha$ at the cost of an inflated failure probability ($\delta$ to $2\delta$).

Together, $\varepsilon$ and $\nu$ control the sharpness of the multiplicative constants of the bound. In the large sample regime, these can often both be allowed to tend to $0$.

The bound can be put in a more convenient form by making use of either of the two numerical inequalities ${{({1 + {2\alpha}})}^{- 1}{({1 + \alpha})}^{2}} \leq {{({1 + \alpha^{2}})} \land {({1 + {\frac{1}{2}\alpha}})}}$.

Using Theorem 1 instead of the result in Abbasi-Yadkori et al. sharpens existing bounds for least squares estimators with martingale difference noise, allowing one to achieve optimal dependence in $\sigma_{var}^{2}$. See e.g. the proof structure laid out in Ziemann et al..

These improvements also potentially extend to refining linear bandit analyses, previously motivating the results in Abbasi-Yadkori et al. and Zhao et al..

## PAC-Bayesian Bounds

Let $\rho$ and $\pi$ be two probability measures supported on a set $\Lambda \subset {\mathbb{R}}^{d}$. Recall that ${d_{KL}{(\rho,\pi)}} \triangleq {\int_{\Lambda}{{\log\left( \frac{d\rho}{d\pi} \right)}{d\rho}}} \in {\lbrack 0,{+ \infty}\rbrack}$ is the Kullback-Leibler divergence between $\rho$ and $\pi$. Our analysis in the sequel rests on the well-known PAC-Bayesian lemma, stated below.

### Lemma 1 (PAC-Bayesian deviation bound)

Let $\Lambda$ be a subset of ${\mathbb{R}}^{d}$, and $Z{(\lambda)}$, $\lambda \in \Lambda$, be a family of real-valued random variables. Assume that ${\mathbf{E}{\lbrack{{\exp Z}{(\lambda)}}\rbrack}} \leq 1$ for every $\lambda \in \Lambda$. Let $\pi$ be a probability distribution on $\Lambda$. Then for all ${u \in {\lbrack 0,\infty)}}:$ where $\rho$ spans all probability measures on $\Lambda$.

We will instantiate the PAC-Bayesian lemma with $Z{(\lambda)}$ as the quadratic form (and with $t = \tau)$ To account for the fact that the Mahalanobis norm appearing in (1.2) includes an additive factor $\Gamma$, let us also take note of the identity In particular, we seek to bound the RHS of (2.2) (or (2.3)) but will use the LHS to establish an exponential inequality. In the two sections that follow we first show how to recover the results of Abbasi-Yadkori et al. featuring the variance proxy $\sigma_{subG}^{2}$ and then proceed to generalize these to variance sensitive Bernstein bounds depending on $\sigma_{var}^{2}$ in the leading order.

### Warm-up: Sub-Gaussian Deviation Bounds

Before we prove our main result, let us explain how a version of the result of Abbasi-Yadkori et al. can be established via Lemma 1. ‣ 2 PAC-Bayesian Bounds ‣ A Vector Bernstein Inequality for Self-Normalized Martingales"). This will inform the proof strategy of our result by essentially replacing Gaussians with a certain covariance ellipsoid with uniform distributions over the same ellipsoid. We prove the result for $\sigma_{subG}^{2} = 1$ and note that the general case follows by rescaling.

By making use of the identity (2.2), it is easy to see that the right hand side of (2.3) satisfies the exponential inequality required for Lemma 1. ‣ 2 PAC-Bayesian Bounds ‣ A Vector Bernstein Inequality for Self-Normalized Martingales"). Namely, the tower rule and the conditional sub-Gaussianity of $\{{{W_{k},k} \geq 1}\}$ implies that ${\mathbf{E}{\exp\left({{\langle\lambda,S_{T}\rangle} - {\frac{1}{2}{\|\lambda\|}_{V_{T}}^{2}}} \right)}} \leq 1$ for all $\lambda \in {\mathbb{R}}^{d}$ and $T \in {\mathbb{N}}$. Hence, we may pick $\rho = {\mathsf{N}\left({{({V_{T} + \Gamma})}^{- 1}S_{T}},\Sigma_{\rho} \right)}$ in Lemma 1. ‣ 2 PAC-Bayesian Bounds ‣ A Vector Bernstein Inequality for Self-Normalized Martingales"). We have: Moreover, if we now set $\pi = {\mathsf{N}{(0,\Sigma_{\pi})}}$ we have that: We point out that there is an asymmetry between $\Sigma_{\rho}$ and $\Sigma_{\pi}$ at this point. The first is allowed to depend on the processes $S_{T},V_{T}$ but the latter is not. Applying Lemma 1. ‣ 2 PAC-Bayesian Bounds ‣ A Vector Bernstein Inequality for Self-Normalized Martingales") to the process (2.2) yields that with probability at least $1 - e^{- u}$: Hence it makes sense to choose $\Sigma_{\rho} = {({V_{T} + \Gamma})}^{- 1}$ and $\Sigma_{\pi} = \Gamma^{- 1}$ giving: which is identical to the result of Abbasi-Yadkori et al. (modulo the stopping time, which can easily be addressed---see below).

### Remark 2.1

By directly applying this proof strategy to (2.2) one may also obtain the following deviation bound with probability at least $1 - e^{- u}$:

### Variance Sensitive Deviation Bounds: Proof of Theorem 1

The use of Gaussian distributions in the self-normalized martingale bound is very convenient as it admits closed form KL expressions. However, their use hinges on the fact that an exponential inequality holds throughout ${\mathbb{R}}^{d}$. We now show how to obtain a similar bound using distributions with compact support. In the sequel, we assume that $\sigma_{{var},\varepsilon}^{2} = 1$ and note that the general result can be recovered by rescaling $S_{\tau}$.

Let us now consider two ellipsoidal distributions. We construct them as follows. Fix two positive definite matrices $\Sigma_{\pi}$ and $\Sigma_{\rho}$ to be determined momentarily and a measurable weight factor $\alpha \in {\lbrack 0,\infty)}$. First, let $\pi$ be uniform over the ellipsoid centered at zero and with shape $\Sigma_{\pi}$, i.e., uniform over $\{{x \in {\mathbb{R}}^{d}}:{{x^{\mathsf{T}}\Sigma_{\pi}^{- 1}x} \leq 1}\}$. Second, let $\rho$ be uniform over the ellipsoid with center $\frac{1}{1 + \alpha}{({V_{\tau} + \Gamma})}^{- 1}S_{\tau}$ and shape $\Sigma_{\rho}$. Note that we must choose $\alpha$ such that ${{\frac{1}{1 + \alpha}{({V_{\tau} + \Gamma})}^{- 1}S_{\tau}} + {\{{x \in {\mathbb{R}}^{d}}:{{x^{\mathsf{T}}\Sigma_{\rho}^{- 1}x} \leq 1}\}}} \subset {\{{x \in {\mathbb{R}}^{d}}:{{x^{\mathsf{T}}\Sigma_{\pi}^{- 1}x} \leq 1}\}}$. Momentarily leaving this point aside, it is easy to see that on the event that the second ellipsoid is contained in the first, the KL divergence between these two distributions is the logarithmic volume ratio (Lemma 4): Moreover, using Lemma 3, on the same event we have that In other words, combined with ${\| S_{\tau}\|}_{{({V_{\tau} + \Gamma})}^{- 1}\Gamma{({V_{\tau} + \Gamma})}^{- 1}} \geq 0$, the PAC-Bayesian bound in Lemma 1. ‣ 2 PAC-Bayesian Bounds ‣ A Vector Bernstein Inequality for Self-Normalized Martingales"), justified by the exponential inequality in Lemma 2, yields that with probability $1 - e^{- u}$: In particular, we may choose $\Sigma_{\rho} = {{({d + 2})}{({V_{\tau} + \Gamma})}^{- 1}}$ and $\Sigma_{\pi} = {e^{- 1}{({d + 2})}V^{- 1}}$ to obtain: We note that (2.12)-(2.13) only hold when the event $\{{{\rho - \text{Ellipsoid}} \subset {\pi - \text{Ellipsoid}}}\}$ occurs, which in itself is contingent on our choice of $\alpha$. First, note that with our choice of priors, the use of Lemma 2 requires the additional constraint $V \succeq {\varepsilon^{- 1}e^{- 1}{({d + 2})}B_{W}^{2}B_{X}^{2}}$. To conclude the proof it remains to verify that a good choice of $\alpha$ can be made. The required event occurs precisely when If ${V_{\tau} + \Gamma} \succeq {{({1 + \nu})}^{2}eV}$ it suffices To see this, let $y = {\frac{1}{1 + \alpha}{({V_{\tau} + \Gamma})}^{- 1}S_{\tau}}$ and note that we must show that ${{({y + x})}^{\mathsf{T}}V{({y + x})}} \leq {e^{- 1}{({d + 2})}}$ for every $x \in {\mathbb{R}}^{d}$ satisfying ${x^{\mathsf{T}}{({V_{\tau} + \Gamma})}x} \leq {d + 2}$. Now we have that for every $\mu > 0$: | | | $= \left({\frac{\sqrt{d + 2}}{\sqrt{e}{({1 + \nu})}} + \sqrt{y^{\mathsf{T}}Vy}} \right)^{2}$ | | $\left({\mu = \sqrt{\frac{e{({1 + \nu})}^{2}y^{\mathsf{T}}Vy}{d + 2}}} \right)$ | | | by applying Young's inequality and optimizing the weight $\mu$ as above. Moreover, one can verify that the above inequality holds with $\alpha = {\left({\frac{\sqrt{e}{({1 + \nu})}{\| S_{\tau}\|}_{{({V_{\tau} + \Gamma})}^{- 1}V{({V_{\tau} + \Gamma})}^{- 1}}}{\nu\sqrt{d + 2}} - 1} \right) \vee 0}$, so that our priors are indeed well defined for this choice. Hence, under the imposed constraints on $V,\varepsilon$ and $\nu$ we have thus obtained that This finishes the proof. $\blacksquare$

## Auxiliary Results

### Lemma 2

Impose (1.3), fix a stopping time $\tau$ with respect to $\mathcal{F}_{0:\infty}$ and $\varepsilon \in {}$. We have that for every $\lambda \in {\mathbb{R}}^{d}$ satisfying ${\|\lambda\|}_{B_{X}^{2}B_{W}^{2}}^{2} \leq \varepsilon^{2}$ and where $\sigma_{{var},\varepsilon}^{2} \triangleq {{({1 - \varepsilon})}^{- 1}\sigma_{var}^{2}}$.

### Proof

Applying Bernstein's moment inequality conditionally on $\mathcal{F}_{k - 1}$ yields that as long as ${\lambda^{\mathsf{T}}X_{k}X_{k}^{\mathsf{T}}\lambda} = {|{\langle\lambda,X_{k}\rangle}|}^{2} < B_{W}^{- 2}$. Since ${X_{k}X_{k}^{\mathsf{T}}} \preceq B_{X}^{2}$, this holds deterministically as long as ${\|\lambda\|}_{B_{W}^{2}B_{X}^{2}}^{2} < 1$. In particular, if we fix $\varepsilon \in {}$ and impose ${\|\lambda\|}_{B_{X}^{2}B_{W}^{2}}^{2} \leq \varepsilon^{2}$ we find that Applying the tower property repeatedly, it thus follows that with $\sigma_{{var},\varepsilon}^{2} = {{({1 - \varepsilon})}^{- 1}\sigma_{var}^{2}}$ we have that for every $t$ and for every $\lambda$ satisfying ${\|\lambda\|}_{B_{X}^{2}B_{W}^{2}}^{2} \leq \varepsilon^{2}$.

To prove the result for $\tau$ a stopping time, define the (by the calculations above) nonnegative supermartingale $M_{t} \triangleq {\exp\left( {{\langle\lambda,S_{t}\rangle} - \frac{\sigma_{{var},\varepsilon}^{2}{\|\lambda\|}_{V_{t}}^{2}}{2}} \right)}$. It follows by standard optional stopping arguments and Fatou's Lemma that $M_{\tau} = {\operatorname{lim\ inf}_{T\rightarrow\infty}M_{\tau \land T}}$ also is a nonnegative supermartingale. In particular ${\mathbf{E}M_{\tau}} \leq 1$ as per requirement. ∎

### Lemma 3

Fix ${\Sigma \in {\mathbb{R}}^{d \times d}},{\Sigma \succ 0}$ and let $U$ be uniformly distributed over $\left. \{{x \in {\mathbb{R}}^{d}} \middle| {{x^{\mathsf{T}}\Sigma^{- 1}x} \leq 1}\} \right.$. Then ${\mathbf{E}UU^{\mathsf{T}}} = {\frac{1}{d + 2}\Sigma}$.

### Proof

Since $U = {\sqrt{\Sigma}Y}$ where $Y$ is uniform over ${x^{\mathsf{T}}x} \leq 1$ it suffices to prove the result for $Y$. By symmetry we must have ${\mathbf{E}YY^{\mathsf{T}}} = {\alpha I_{d}}$ for some $\alpha > 0$. Moreover, it is easy to see that ${{tr}{\mathbf{E}YY^{\mathsf{T}}}} = \frac{d}{d + 2}$. Hence $\alpha = {({d + 2})}^{- 1}$ and the result is established. ∎

### Lemma 4

Fix ${\Sigma_{\pi},\Sigma_{\rho}} \in {\mathbb{R}}^{d \times d}$ with ${\Sigma_{\pi},\Sigma_{\rho}} \succ 0$. Let $\pi$ and $\rho$ be uniform distributions over $E_{\pi} \triangleq \left. \{{x \in {\mathbb{R}}^{d}} \middle| {{x^{\mathsf{T}}\Sigma_{\pi}^{- 1}x} \leq 1}\} \right.$ and $E_{\rho} \triangleq \left. \{{x \in {\mathbb{R}}^{d}} \middle| {{x^{\mathsf{T}}\Sigma_{\rho}^{- 1}x} \leq 1}\} \right.$ respectively. If $E_{\rho} \subseteq E_{\pi}$ we have that ${d_{KL}{(\rho,\pi)}} = {\frac{1}{2}{\log\frac{\det\Sigma_{\pi}}{\det\Sigma_{\rho}}}}$.

### Proof

| | | $= {\int_{E_{\rho}}{{\log{\frac{\det\sqrt{\Sigma_{\pi}}}{\det\sqrt{\Sigma_{\rho}}}d\rho}}{(x)}}}$ | | $(\text{volume ratio})$ | | | | | | $= {{\log\frac{\det\sqrt{\Sigma_{\pi}}}{\det\sqrt{\Sigma_{\rho}}}}{\int_{E_{\rho}}{{d\rho}{(x)}}}} = {\log\frac{\det\sqrt{\Sigma_{\pi}}}{\det\sqrt{\Sigma_{\rho}}}}$ | | $\left({{\int_{E_{\rho}}{{d\rho}{(x)}}} = 1} \right)$ | | |

### Proof of Lemma 1. ‣ 2 PAC-Bayesian Bounds ‣ A Vector Bernstein Inequality for Self-Normalized Martingales")

By integrating the inequality ${\mathbf{E}{\lbrack{{\exp Z}{(\lambda)}}\rbrack}} \leq 1$ with respect to $\pi$ and Fubini: We now change measure using the variational characterization of the relative relative entropy functional, which reads: where the supremum spans over all probability measures $\rho$ over $\Lambda$. Hence The result follows by a Chernoff bound applied to $\left\{ {{\sup_{\rho}\left\{ {{\int_{\Lambda}{Z{(\lambda)}{d\rho}{(\lambda)}}} - {d_{KL}{(\rho,\pi)}}} \right\}} > u} \right\}$. ∎
