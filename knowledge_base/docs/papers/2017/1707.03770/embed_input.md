Fastest Convergence for Q-learning

The Zap Q-learning algorithm introduced in this paper is an improvement of Watkins' original algorithm and recent competitors in several respects. It is a matrix-gain algorithm designed so that its asymptotic variance is optimal. Moreover, an ODE analysis suggests that the transient behavior is a close match to a deterministic Newton-Raphson implementation. This is made possible by a two time-scale update equation for the matrix gain sequence. The analysis suggests that the approach will lead to stable and efficient computation even for non-ideal parameterized settings. Numerical experiments confirm the quick convergence, even in such non-ideal cases. A secondary goal of this paper is tutorial. The first half of the paper contains a survey on reinforcement learning algorithms, with a focus on minimum variance algorithms.

## Introduction

It is recognized that algorithms for reinforcement learning such as TD- and Q-learning can be slow to converge. The poor performance of Watkins' Q-learning algorithm was first quantified , and since then many papers have appeared with proposed improvements, such as.

An emphasis in much of the literature is computation of finite-time PAC (probably almost correct) bounds as a metric for performance. Explicit bounds were obtained in for Watkins' algorithm, and in for the "speedy" Q-learning algorithm that was introduced by these authors. A general theory is presented in for stochastic approximation algorithms.

In each of the models considered in prior work, the update equation for the parameter estimates can be expressed

The CLT will be a guide to algorithm design in the present paper. For a typical stochastic approximation algorithm, this takes the following form: denoting $\{{{{\overset{\sim}{\theta}}_{n}:=\theta_{n}} - \theta^{\ast}}:{n \geq 0}\}$ to be the error sequence, under general conditions the scaled sequence $\{{\sqrt{n}{\overset{\sim}{\theta}}_{n}}:{n \geq 1}\}$ converges in distribution to a Gaussian distribution, $\mathcal{N}{(0,\Sigma_{\theta})}$.

As shown in examples in this paper, the asymptotic covariance is often a good predictor of finite-time performance, since the CLT approximation is accurate for reasonable values of $n$.

In addition to accelerating the convergence rate of standard algorithms for reinforcement learning, it is hoped that this paper will lead to entirely new algorithms. In particular, there is little theory to support Q-learning in non-ideal settings in which the optimal "$Q$-function" does not lie in the parameterized function class. Convergence results have been obtained for a class of optimal stopping problems, and for deterministic models. There is now intense practical interest, despite an incomplete theory. A stronger supporting theory will surely lead to more efficient algorithms.
