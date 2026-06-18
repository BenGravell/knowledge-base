Policy Optimization Provably Converges to Nash Equilibria in Zero-Sum Linear Quadratic Games

Topics include Nonconvex optimization, Reinforcement learning, Optimization, Control, Learning, Neuroevolution, Zero-sum linear quadratic, Linear quadratic, Saddle point.

We study the global convergence of policy optimization for finding the Nash equilibria (NE) in zero-sum linear quadratic (LQ) games. To this end, we first investigate the landscape of LQ games, viewing it as a nonconvex-nonconcave saddle-point problem in the policy space. Specifically, we show that despite its nonconvexity and nonconcavity, zero-sum LQ games have the property that the stationary point of the objective function with respect to the linear feedback control policies constitutes the NE of the game. Building upon this, we develop three projected nested-gradient methods that are guaranteed to converge to the NE of the game. Moreover, we show that all of these algorithms enjoy both globally sublinear and locally linear convergence rates. Simulation results are also provided to illustrate the satisfactory convergence properties of the algorithms. To the best of our knowledge, this work appears to be the first one to investigate the optimization landscape of LQ games, and provably show the convergence of policy optimization methods to the Nash equilibria....

## Introduction

Reinforcement learning (RL) has achieved sensational progress recently in several prominent decision-making problems, e.g., playing the game of Go and playing real-time strategy games. Interestingly, all of these problems can be formulated as zero-sum Markov games involving two opposing players or teams. Moreover, their algorithmic frameworks are all based upon *policy optimization* (PO) methods such as actor-critic and proximal policy optimization (PPO), where the policies are parametrized and iteratively updated....

In contrast to the tremendous empirical success, theoretical understanding of policy optimization methods for the multi-agent RL settings, especially the zero-sum Markov game setting, lags behind. Although the convergence of policy optimization algorithms to *locally optimal* policies has been established in the classical RL setting with a *single-agent/player*, extending those theoretical guarantees to *Nash equilibrium* (NE) policies, a common solution concept in game theory also known as the saddle-point equilibrium (SPE) in the zero-sum setting, suffers from the following two caveats.

## Concluding Remarks

This paper has developed policy optimization methods, specifically, projected nested-gradient methods, to solve for the Nash equilibria of zero-sum LQ games. In spite of the nonconvexity-nonconcavity of the problem, the gradient-based algorithms have been shown to converge to the NE with globally sublinear and locally linear rates. This work appears to be the first one showing that policy optimization methods can converge to the NE of a class of zero-sum Markov games, with finite-iteration analyses....

### Lemma 6.4

Suppose ${E_{x_{0} \sim \mathcal{D}}x_{0}x_{0}^{\top}} > 0$ and Assumption 2.1 holds. For any $L \in \underset{¯}{}$, where $\underset{¯}{}$ is defined in (3.3). ‣ 3 Policy Gradient and Landscape ‣ Policy Optimization Provably Converges to Nash Equilibria in Zero-Sum Linear Quadratic Games")), it follows that: i) the inner-loop LQR problem always admits a solution, with a positive definite $P_{{K{(L)}},L}$ and a stabilizing control pair $({K{(L)}},L)$; ii) there exists a constant stepsize $\alpha > 0$ for each of the updates (4.3)- such that the generated control pair sequences ${\{{(K_{\tau},L)}\}}_{\tau \geq 0}$ are always stabilizing;...
