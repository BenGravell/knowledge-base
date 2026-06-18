A Vector Bernstein Inequality for Self-Normalized Martingales

We prove a Bernstein inequality for vector-valued self-normalized martingales. We first give an alternative perspective of the corresponding sub-Gaussian bound due to Abbasi-Yadkori et al. via a PAC-Bayesian argument with Gaussian priors. By instantiating this argument to priors drawn uniformly over well-chosen ellipsoids, we obtain a Bernstein bound.

## Abstract

We prove a Bernstein inequality for vector-valued self-normalized martingales. We first give an alternative perspective of the corresponding sub-Gaussian bound due to Abbasi-Yadkori et al. via a PAC-Bayesian argument with Gaussian priors. By instantiating this argument to priors drawn uniformly over well-chosen ellipsoids, we obtain a Bernstein bound.

## Tail Bounds for Self-Normalized Martingales

Deviation inequalities for self-normalized martingales play a key role in obtaining guarantees for linear regression in interactive and sequential decision-making tasks, such as learning an autoregression or regret minimization in linear bandits. The most prevalent version of such an inequality currently in use is due to Abbasi-Yadkori et al. and rests on the method of pseudo-maximization popularized by Peña et al., dating back to Robbins and Siegmund. Comparing their result to the central limit theorem, their bound is nearly optimal but depends on the sub-Gaussian variance proxy instead of the actual variance.

Their approach rests on an elegant application of the pseudo-maximization technique developed by Peña et al., dating back to Robbins and Siegmund. While elegant, the result of Abbasi-Yadkori et al. has one shortcoming as compared to classical asymptotics: the linear dependence on the conditional variance proxy $\sigma_{subG}^{2}$ as opposed to the conditional variance, $\sigma_{var}^{2} \triangleq {\sup{\{{\left. {\mathbf{E}{\lbrack\left. W_{k}^{2} \middle| \mathcal{F}_{k - 1} \right.\rbrack}} \middle| {\text{~a.s.,~}k} \right. \in T}\}}}$.

In this note, we provide an alternative perspective on the proof of (1.2), where, instead of computing the exponential integral directly, we invoke the variational characterization of Kullback-Liebler divergence via the PAC-Bayesian lemma to relegate this difficulty to the calculation of said divergence. Beyond Gaussian priors, this turns out to be significantly simpler than the evaluation of an exponential integral.
