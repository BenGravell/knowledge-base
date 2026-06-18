A Vector Bernstein Inequality for Self-Normalized Martingales

We prove a Bernstein inequality for vector-valued self-normalized martingales. We first give an alternative perspective of the corresponding sub-Gaussian bound due to Abbasi-Yadkori et al. via a PAC-Bayesian argument with Gaussian priors. By instantiating this argument to priors drawn uniformly over well-chosen ellipsoids, we obtain a Bernstein bound.

## Abstract

We prove a Bernstein inequality for vector-valued self-normalized martingales. We first give an alternative perspective of the corresponding sub-Gaussian bound due to Abbasi-Yadkori et al. via a PAC-Bayesian argument with Gaussian priors. By instantiating this argument to priors drawn uniformly over well-chosen ellipsoids, we obtain a Bernstein bound.

## Tail Bounds for Self-Normalized Martingales

We now change measure using the variational characterization of the relative relative entropy functional, which reads:

where the supremum spans over all probability measures $\rho$ over $\Lambda$. Hence

By making use of the identity (2.2), it is easy to see that the right hand side of (2.3) satisfies the exponential inequality required for Lemma 1. ‣ 2 PAC-Bayesian Bounds ‣ A Vector Bernstein Inequality for Self-Normalized Martingales"). Namely, the tower rule and the conditional sub-Gaussianity of $\{{{W_{k},k} \geq 1}\}$ implies that ${\mathbf{E}{\exp\left( {{\langle\lambda,S_{T}\rangle} - {\frac{1}{2}{\|\lambda\|}_{V_{T}}^{2}}} \right)}} \leq 1$ for all $\lambda \in {\mathbb{R}}^{d}$ and $T \in {\mathbb{N}}$. Hence, we may pick $\rho = {\mathsf{N}\left( {{({V_{T} + \Gamma})}^{- 1}S_{T}},\Sigma_{\rho} \right)}$ in Lemma 1....

## PAC-Bayesian Bounds

In other words, combined with ${\| S_{\tau}\|}_{{({V_{\tau} + \Gamma})}^{- 1}\Gamma{({V_{\tau} + \Gamma})}^{- 1}} \geq 0$, the PAC-Bayesian bound in Lemma 1. ‣ 2 PAC-Bayesian Bounds ‣ A Vector Bernstein Inequality for Self-Normalized Martingales"), justified by the exponential inequality in Lemma 2, yields that with probability $1 - e^{- u}$:

Deviation inequalities for self-normalized martingales play a key role in obtaining guarantees for linear regression in interactive and sequential decision-making tasks, such as learning an autoregression or regret minimization in linear bandits. The most prevalent version of such an inequality currently in use is due to Abbasi-Yadkori et al. and rests on the method of pseudo-maximization popularized by Peña et al., dating back to Robbins and Siegmund. Comparing their result to the central limit theorem, their bound is nearly optimal but depends on the sub-Gaussian variance proxy instead of the actual variance....

Their approach rests on an elegant application of the pseudo-maximization technique developed by Peña et al., dating back to Robbins and...
