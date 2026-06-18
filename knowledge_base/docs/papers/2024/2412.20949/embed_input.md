<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Vector Bernstein Inequality for Self-Normalized Martingales

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We prove a Bernstein inequality for vector-valued self-normalized martingales. We first give an alternative perspective of the corresponding sub-Gaussian bound due to Abbasi-Yadkori et al. via a PAC-Bayesian argument with Gaussian priors. By instantiating this argument to priors drawn uniformly over well-chosen ellipsoids, we obtain a Bernstein bound.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

We prove a Bernstein inequality for vector-valued self-normalized martingales. We first give an alternative perspective of the corresponding sub-Gaussian bound due to Abbasi-Yadkori et al. via a PAC-Bayesian argument with Gaussian priors. By instantiating this argument to priors drawn uniformly over well-chosen ellipsoids, we obtain a Bernstein bound.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Tail Bounds for Self-Normalized Martingales", "weight": 1.0} -->

Deviation inequalities for self-normalized martingales play a key role in obtaining guarantees for linear regression in interactive and sequential decision-making tasks, such as learning an autoregression or regret minimization in linear bandits. The most prevalent version of such an inequality currently in use is due to Abbasi-Yadkori et al. and rests on the method of pseudo-maximization popularized by Peña et al., dating back to Robbins and Siegmund. Comparing their result to the central limit theorem, their bound is nearly optimal but depends on the sub-Gaussian variance proxy instead of the actual variance. In this note, we overcome this issue by casting the pseudo-maximization technique through the lens of the PAC-Bayesian inequality. The present approach simplifies classical pseudo-maximization by relegating the complexity of evaluating exponential integrals against the smoothing distribution to the computation of a generic Kullback-Liebler divergence term. This allows us to generalize the argument of Abbasi-Yadkori et al. but without access to globally defined moment generating function bounds.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Tail Bounds for Self-Normalized Martingales", "weight": 1.0} -->

Their approach rests on an elegant application of the pseudo-maximization technique developed by Peña et al., dating back to Robbins and Siegmund. While elegant, the result of Abbasi-Yadkori et al. has one shortcoming as compared to classical asymptotics: the linear dependence on the conditional variance proxy $\sigma_{subG}^{2}$ as opposed to the conditional variance, $\sigma_{var}^{2} \triangleq {\sup{\{{\left. {\mathbf{E}{\lbrack\left. W_{k}^{2} \middle| \mathcal{F}_{k - 1} \right.\rbrack}} \middle| {\text{~a.s.,~}k} \right. \in T}\}}}$. The traditional fix to this in the literature on concentration inequalities is to invoke a Bernstein-type bound on the moment generating function (MGF) of the $W_{k}$ instead of a Hoeffding type of bound.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Tail Bounds for Self-Normalized Martingales", "weight": 1.0} -->

Unfortunately, directly combining a Bernstein MGF bound with the pseudo-maximization technique does not lead to analytically tractable upper bounds as it requires the evaluation of an exponential integral over a bounded domain (an ellipsoid). Moreover, previous attempts at establishing Bernstein bounds (via methods orthogonal to pseudo-maximization) for vector-valued self-normalized martingales suffer from extraneous logarithmic dependencies and have significantly looser constants.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Tail Bounds for Self-Normalized Martingales", "weight": 1.0} -->

In this note, we provide an alternative perspective on the proof of (1.2), where, instead of computing the exponential integral directly, we invoke the variational characterization of Kullback-Liebler divergence via the PAC-Bayesian lemma to relegate this difficulty to the calculation of said divergence. Beyond Gaussian priors, this turns out to be significantly simpler than the evaluation of an exponential integral. It allows us to modularize the proof strategy of Abbasi-Yadkori et al. and replace their Gaussian prior with uniform ellipsoidal priors that are suitable in combination with exponential inequalities that only hold for a restricted domain (contrast this with Hoeffding MGF bounds being valid for all $\lambda$).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Tail Bounds for Self-Normalized Martingales", "weight": 1.0} -->

The rest of this note is organized as follows. We state our main result immediately below and then proceed to discuss its consequences. Its proof is given in Section 2.2. Preliminaries relating to our application of the PAC-Bayesian lemma are given in Section 2 where we also provide a proof of (1.2) as a warm-up. Auxiliary lemmata are proven in Section 3.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The Result", "weight": 1.0} -->

To apply a Bernstein MGF bound, we will require some additional boundedness assumptions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The Result", "weight": 1.0} -->

for a positive scalar $B_{W}$ and a positive definite matrix $B_{X}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Remarks on Theorem 1", "weight": 1.0} -->

When $\Gamma = 0$, requiring $\alpha = 0$ in Theorem 1 can be thought of as a burn-in requirement, restricting the Bernstein inequality to cases in which the corresponding least squares error is sufficiently small. Typically, $\alpha = 0$ once the sample size is large enough as ${\| S_{\tau}\|}_{V_{\tau}^{- 2}}^{2}$ is the norm-squared error of the least squares estimator in the model $Y_{k} = {{\langle\theta_{\star},X_{k}\rangle} + W_{k}}$ up to time $\tau$. When $S_{\tau}$ is not too large, the variance proxy $\sigma_{subG}^{2}$ in (1.2) can thus be replaced by the variance term $\sigma_{var}^{2}$ with just a little overhead in $\varepsilon$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Remarks on Theorem 1", "weight": 1.0} -->

For $\Gamma \succeq {\varepsilon^{- 1}e^{- 1}{({d + 2})}B_{W}^{2}B_{X}^{2}}$ (corresponding instead to ridge regression) one may choose $V = \Gamma$ and use (1.2) to control $\alpha$ at the cost of an inflated failure probability ($\delta$ to $2\delta$).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Remarks on Theorem 1", "weight": 1.0} -->

Together, $\varepsilon$ and $\nu$ control the sharpness of the multiplicative constants of the bound. In the large sample regime, these can often both be allowed to tend to $0$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Remarks on Theorem 1", "weight": 1.0} -->

Using Theorem 1 instead of the result in Abbasi-Yadkori et al. sharpens existing bounds for least squares estimators with martingale difference noise, allowing one to achieve optimal dependence in $\sigma_{var}^{2}$. See e.g. the proof structure laid out in Ziemann et al..

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remarks on Theorem 1", "weight": 1.0} -->

These improvements also potentially extend to refining linear bandit analyses, previously motivating the results in Abbasi-Yadkori et al. and Zhao et al..

<!-- chunk {"id": "body-0016", "role": "body", "section": "PAC-Bayesian Bounds", "weight": 1.0} -->

Let $\rho$ and $\pi$ be two probability measures supported on a set $\Lambda \subset {\mathbb{R}}^{d}$. Recall that ${d_{KL}{(\rho,\pi)}} \triangleq {\int_{\Lambda}{{\log\left( \frac{d\rho}{d\pi} \right)}{d\rho}}} \in {\lbrack 0,{+ \infty}\rbrack}$ is the Kullback-Leibler divergence between $\rho$ and $\pi$. Our analysis in the sequel rests on the well-known PAC-Bayesian lemma, stated below.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Warm-up: Sub-Gaussian Deviation Bounds", "weight": 1.0} -->

Before we prove our main result, let us explain how a version of the result of Abbasi-Yadkori et al. can be established via Lemma 1. ‣ 2 PAC-Bayesian Bounds ‣ A Vector Bernstein Inequality for Self-Normalized Martingales"). This will inform the proof strategy of our result by essentially replacing Gaussians with a certain covariance ellipsoid with uniform distributions over the same ellipsoid. We prove the result for $\sigma_{subG}^{2} = 1$ and note that the general case follows by rescaling.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Warm-up: Sub-Gaussian Deviation Bounds", "weight": 1.0} -->

By making use of the identity (2.2), it is easy to see that the right hand side of (2.3) satisfies the exponential inequality required for Lemma 1. ‣ 2 PAC-Bayesian Bounds ‣ A Vector Bernstein Inequality for Self-Normalized Martingales"). Namely, the tower rule and the conditional sub-Gaussianity of $\{{{W_{k},k} \geq 1}\}$ implies that ${\mathbf{E}{\exp\left( {{\langle\lambda,S_{T}\rangle} - {\frac{1}{2}{\|\lambda\|}_{V_{T}}^{2}}} \right)}} \leq 1$ for all $\lambda \in {\mathbb{R}}^{d}$ and $T \in {\mathbb{N}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Warm-up: Sub-Gaussian Deviation Bounds", "weight": 1.0} -->

Hence, we may pick $\rho = {\mathsf{N}\left( {{({V_{T} + \Gamma})}^{- 1}S_{T}},\Sigma_{\rho} \right)}$ in Lemma 1. ‣ 2 PAC-Bayesian Bounds ‣ A Vector Bernstein Inequality for Self-Normalized Martingales").

<!-- chunk {"id": "body-0020", "role": "body", "section": "Warm-up: Sub-Gaussian Deviation Bounds", "weight": 1.0} -->

We point out that there is an asymmetry between $\Sigma_{\rho}$ and $\Sigma_{\pi}$ at this point. The first is allowed to depend on the processes $S_{T},V_{T}$ but the latter is not. Applying Lemma 1. ‣ 2 PAC-Bayesian Bounds ‣ A Vector Bernstein Inequality for Self-Normalized Martingales") to the process (2.2)

<!-- chunk {"id": "body-0021", "role": "body", "section": "Warm-up: Sub-Gaussian Deviation Bounds", "weight": 1.0} -->

which is identical to the result of Abbasi-Yadkori et al. (modulo the stopping time, which can easily be addressed---see below).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark 2.1", "weight": 1.0} -->

By directly applying this proof strategy to (2.2)

<!-- chunk {"id": "body-0023", "role": "body", "section": "Variance Sensitive Deviation Bounds: Proof of Theorem 1", "weight": 1.0} -->

The use of Gaussian distributions in the self-normalized martingale bound is very convenient as it admits closed form KL expressions. However, their use hinges on the fact that an exponential inequality holds throughout ${\mathbb{R}}^{d}$. We now show how to obtain a similar bound using distributions with compact support. In the sequel, we assume that $\sigma_{{var},\varepsilon}^{2} = 1$ and note that the general result can be recovered by rescaling $S_{\tau}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Variance Sensitive Deviation Bounds: Proof of Theorem 1", "weight": 1.0} -->

Let us now consider two ellipsoidal distributions. We construct them as follows. Fix two positive definite matrices $\Sigma_{\pi}$ and $\Sigma_{\rho}$ to be determined momentarily and a measurable weight factor $\alpha \in {\lbrack 0,\infty)}$. First, let $\pi$ be uniform over the ellipsoid centered at zero and with shape $\Sigma_{\pi}$, i.e., uniform over $\{{x \in {\mathbb{R}}^{d}}:{{x^{\mathsf{T}}\Sigma_{\pi}^{- 1}x} \leq 1}\}$. Second, let $\rho$ be uniform over the ellipsoid with center $\frac{1}{1 + \alpha}{({V_{\tau} + \Gamma})}^{- 1}S_{\tau}$ and shape $\Sigma_{\rho}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Variance Sensitive Deviation Bounds: Proof of Theorem 1", "weight": 1.0} -->

Moreover, using Lemma 3, on the same event we have that

<!-- chunk {"id": "body-0026", "role": "body", "section": "Variance Sensitive Deviation Bounds: Proof of Theorem 1", "weight": 1.0} -->

We note that (2.12)-(2.13) only hold when the event $\{{{\rho - \text{Ellipsoid}} \subset {\pi - \text{Ellipsoid}}}\}$ occurs, which in itself is contingent on our choice of $\alpha$. First, note that with our choice of priors, the use of Lemma 2 requires the additional constraint $V \succeq {\varepsilon^{- 1}e^{- 1}{({d + 2})}B_{W}^{2}B_{X}^{2}}$. To conclude the proof it remains to verify that a good choice of $\alpha$ can be made. The required event occurs precisely when

<!-- chunk {"id": "body-0027", "role": "body", "section": "Variance Sensitive Deviation Bounds: Proof of Theorem 1", "weight": 1.0} -->

by applying Young's inequality and optimizing the weight $\mu$ as above. Moreover, one can verify that the above inequality holds with $\alpha = {\left( {\frac{\sqrt{e}{({1 + \nu})}{\| S_{\tau}\|}_{{({V_{\tau} + \Gamma})}^{- 1}V{({V_{\tau} + \Gamma})}^{- 1}}}{\nu\sqrt{d + 2}} - 1} \right) \vee 0}$, so that our priors are indeed well defined for this choice. Hence, under the imposed constraints on $V,\varepsilon$ and $\nu$ we have thus obtained that

<!-- chunk {"id": "body-0028", "role": "body", "section": "Variance Sensitive Deviation Bounds: Proof of Theorem 1", "weight": 1.0} -->

This finishes the proof. $\blacksquare$
