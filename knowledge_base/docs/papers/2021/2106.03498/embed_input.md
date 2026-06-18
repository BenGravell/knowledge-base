Identifiability in Inverse Reinforcement Learning

Topics include Inverse reinforcement learning, Identifiability, Entropy regularization, Markov decision process, Reward learning, Machine learning theory, Optimization.

Characterizes when reward functions can and cannot be identified from demonstrations in inverse reinforcement learning. The key result is that entropy regularization, multiple discount factors, or sufficiently different environments can break the usual reward ambiguity up to well-defined equivalence classes.

Inverse reinforcement learning attempts to reconstruct the reward function in a Markov decision problem, using observations of agent actions. As already observed in Russell the problem is ill-posed, and the reward function is not identifiable, even under the presence of perfect information about optimal behavior. We provide a resolution to this non-identifiability for problems with entropy regularization. For a given environment, we fully characterize the reward functions leading to a given policy and demonstrate that, given demonstrations of actions for the same reward under two distinct discount factors, or under sufficiently different environments, the unobserved reward can be recovered up to a constant. We also give general necessary and sufficient conditions for reconstruction of time-homogeneous rewards on finite horizons, and for action-independent rewards, generalizing recent results of Kim et al. and Fu et al..

## Introduction

Inverse reinforcement learning aims to use observations of agents' actions to determine their reward function. The problem has roots in the very early stages of optimal control theory; Kalman raised the question of whether, by observation of optimal policies, one can recover coefficients of a quadratic cost function (see also Boyd et al. ). This question naturally generalizes to the generic framework of Markov decision process and stochastic control.

In the 1970s, these questions were taken up within economics, as a way of determining utility functions from observations. For instance, Keeney and Raiffa set out to determine a proper ordering of all possible states which are deterministic functions of actions. In this setup, the problem is static and the outcome of an action is immediate. Later in Sargent, a dynamic version of a utility assessment problem was studied, under the context of finding the proper wage through observing dynamic labor demand.

Figure 9: Learning from optimal policies under γ1 and γ2: difference ${\overset{\sim}{\Pi}}_{1} - \Pi_{1}$ between learnt and true policies under γ1. Note scale of 10−3.

Figure 10: Learning from optimal policies under γ1 and γ2: differences ${\overset{\sim}{\Pi}}_{2} - \Pi_{2}$ between learnt and true policies under γ2. Note scale of 10−3.

Then there exists a horizon $T$ such that the time-homogeneous IRL problem is well posed (as in Theorem 4). In particular, in case (ii) ‣ Corollary 1. ‣ 4.1 Time-homogeneous finite-horizon identifiability. ‣ 4 Finite horizon results ‣ Identifiability in inverse reinforcement learning"), it is sufficient to take any finite $T \geq {d + 1}$; in case (iii) ‣ Corollary 1. ‣ 4.1 Time-homogeneous finite-horizon identifiability. ‣ 4 Finite horizon results ‣ Identifiability in inverse reinforcement learning") it is sufficient to take any finite $T \geq {d + {RR^{\prime}}}$.

Let $\mathcal{R} \subset {\mathbb{N}}$ be a set of natural numbers, with the property that $\mathcal{R}$ is closed under addition (if ${a,b} \in \mathcal{R}$ then ${a + b} \in \mathcal{R}$). Suppose $\mathcal{R}$ has greatest common divisor $1$ (i.e. ${\gcd{(\mathcal{R})}} = 1$). Then there exist elements ${a,b} \in \mathcal{R}$ which are coprime (i.e. ${\gcd{(a,b)}} = 1$)....
