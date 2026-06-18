On the Performance of Thompson Sampling on Logistic Bandits

We study the logistic bandit, in which rewards are binary with success probability exp(betaa^(top) theta) / (1 + exp(betaa^(top) theta)) and actions a and coefficients theta are within the d-dimensional unit ball. While prior regret bounds for algorithms that address the logistic bandit exhibit exponential dependence on the slope parameter beta, we establish a regret bound for Thompson sampling that is independent of beta. Specifically, we establish that, when the set of feasible actions is identical to the set of possible coefficient vectors, the Bayesian regret of Thompson sampling is tildeO(dsqrt(T)). We also establish a tildeO(sqrt(detaT)/lambda) bound that applies more broadly, where lambda is the worst-case optimal log-odds and eta is the "fragility dimension," a new statistic we define to capture the degree to which an optimal action for one model fails to satisfice for others. We demonstrate that the fragility dimension plays an essential role by showing that, for any epsilon > 0, no algorithm can achieve poly(d, 1/lambda)* T^-epsilon regret.

## Introduction

In the logistic bandit an agent observes a binary reward after each action, with outcome probabilities governed by a logistic function:

Each action $a$ and parameter vector $\theta$ is a vector within the $d$-dimensional unit ball. The agent initially knows the scale parameter $\beta$ but is uncertain about the coefficient vector $\theta$. The problem of learning to improve action selection over repeated interactions is sometimes referred to as the logistic bandit problem or online logistic regression.

We can also show that (as in Appendix D), for any fixed $\lambda \in {}$, there exists $\gamma > 1$, such that for any $d \geq 2$ we can find a pair of action and parameter sets $(\mathcal{A}_{d},\Theta_{d})$ with ${\mathcal{A}_{d},\Theta_{d}} \in {\mathbb{R}}^{d}$, ${|\mathcal{A}_{d}|} = {|\Theta_{d}|} \geq \gamma^{d}$ that satisfies, and Assumption 1 with constant $\lambda$. For any real function $f{( \cdot )}$, polynomial $p{( \cdot )}$ and constant $\epsilon \in {}$, choose $d$ large enough such that $\gamma^{\epsilond} > {16f{(\lambda)}p{(d)}}$ and $\beta_{d}$ large enough such that

Toyota Research Institute (TRI) provided funds to assist the authors (Tengyu Ma) with their research but this article solely reflects the opinions and conclusions of its authors and not TRI or any other Toyota entity. Shi Dong is supported by the Herb and Jane Dwight Stanford Graduate Fellowship.

### Remark 3.5

For our general result, we assume that the following assumption holds.

### Theorem 3.9

The logistic bandit serves as a model for a wide range of applications. One example is the problem of personalized recommendation, in which a service provider successively recommends content, receiving only binary responses from users, indicating "like" or "dislike." A growing literature treats the design and analysis of action selection algorithms for the logistic bandit....

To shed light on this issue, we build on an information-theoretic line of analysis, which was first proposed in \[Russo and Van Roy\] and further developed in \[Bubeck and Eldan\] and \[Dong and Van Roy\]. A critical device here is the information ratio, which quantifies the one-stage trade-off between exploration and exploitation....
