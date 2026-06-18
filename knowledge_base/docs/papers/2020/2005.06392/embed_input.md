On the Global Convergence Rates of Softmax Policy Gradient Methods

We make three contributions toward better understanding policy gradient methods in the tabular setting. First, we show that with the true gradient, policy gradient with a softmax parametrization converges at a O(1/t) rate, with constants depending on the problem and initialization. This result significantly expands the recent asymptotic convergence results. The analysis relies on two findings: that the softmax policy gradient satisfies a Łojasiewicz inequality, and the minimum probability of an optimal action during optimization can be bounded in terms of its initial value. Second, we analyze entropy regularized policy gradient and show that it enjoys a significantly faster linear convergence rate O(e^-c * t) toward softmax optimal policy (c > 0). This result resolves an open question in the recent literature. Finally, combining the above two results and additional new Omega(1/t) lower bound results, we explain how entropy regularization improves policy optimization, even with the true gradient, from the perspective of convergence rate. The separation of rates is further explained using the notion of non-uniform Łojasiewicz degree....

## Introduction

The *policy gradient* is one of the most foundational concepts in Reinforcement Learning (RL), lying at the core of policy-search and actor-critic methods. This paper is concerned with the analysis of the convergence rate of *policy gradient methods*. As an approach to RL, the appeal of policy gradient methods is that they are conceptually straightforward and under some regularity conditions they guarantee monotonic improvement of the value. A secondary appeal is that policy gradient methods were shown to achieve effective empirical performance.

Despite the prevalence and importance of policy optimization in RL, the theoretical understanding of policy gradient method has, until recently, been severely limited. A key barrier to understanding is the inherent non-convexity of the value landscape with respect to standard policy parametrizations. As a result, little has been known about the global convergence behavior of policy gradient method. Recently, important new progress in understanding the convergence behavior of policy gradient has been achieved....

## Conclusions and Future Work

We set out to study the convergence speed of softmax policy gradient methods with and without entropy regularization in the tabular setting. Here, the error is measured in terms of the sub-optimality of the policy obtained after some number of updates. Our main findings is that without entropy regularization, the rate is $\Theta{({1/t})}$, which is faster than rates previously obtained. Our analysis also uncovered an unpleasant dependence on the initial parameter values. With entropy regularization, the rate becomes linear, where now the constant in the exponent is influenced by the initial choice of parameters....

### Theorem 4

Proposition 2 suggests that one should set $\theta_{1}$ so that $\pi_{\theta_{1}}$ is uniform. Using this initialization, we can show that ${\inf_{t \geq 1}{\pi_{\theta_{t}}{(a^{\ast})}}} \geq {1/K}$, strengthening Theorem 2. ‣ 3.2.1 The Instructive Case of Bandits ‣ 3.2 Convergence Rates ‣ 3 Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods"):

Using Update 2. ‣ 4.2.1 Bandit Case ‣ 4.2 Convergence Rates ‣ 4 Entropy Regularized Policy Gradient ‣ On the Global Convergence Rates of Softmax Policy Gradient Methods") with ${\tau\eta} \leq 1$, ${\forall t} > 0$,
