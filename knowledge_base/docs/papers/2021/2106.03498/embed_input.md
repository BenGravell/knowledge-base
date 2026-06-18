Identifiability in Inverse Reinforcement Learning

Topics include Inverse reinforcement learning, Identifiability, Entropy regularization, Markov decision process, Reward learning, Machine learning theory, Optimization.

Characterizes when reward functions can and cannot be identified from demonstrations in inverse reinforcement learning. The key result is that entropy regularization, multiple discount factors, or sufficiently different environments can break the usual reward ambiguity up to well-defined equivalence classes.

Inverse reinforcement learning attempts to reconstruct the reward function in a Markov decision problem, using observations of agent actions. As already observed in Russell the problem is ill-posed, and the reward function is not identifiable, even under the presence of perfect information about optimal behavior. We provide a resolution to this non-identifiability for problems with entropy regularization. For a given environment, we fully characterize the reward functions leading to a given policy and demonstrate that, given demonstrations of actions for the same reward under two distinct discount factors, or under sufficiently different environments, the unobserved reward can be recovered up to a constant. We also give general necessary and sufficient conditions for reconstruction of time-homogeneous rewards on finite horizons, and for action-independent rewards, generalizing recent results of Kim et al. and Fu et al..

## Introduction

Inverse reinforcement learning aims to use observations of agents' actions to determine their reward function. The problem has roots in the very early stages of optimal control theory; Kalman raised the question of whether, by observation of optimal policies, one can recover coefficients of a quadratic cost function (see also Boyd et al. ). This question naturally generalizes to the generic framework of Markov decision process and stochastic control.

In the 1970s, these questions were taken up within economics, as a way of determining utility functions from observations. For instance, Keeney and Raiffa set out to determine a proper ordering of all possible states which are deterministic functions of actions. In this setup, the problem is static and the outcome of an action is immediate. Later in Sargent, a dynamic version of a utility assessment problem was studied, under the context of finding the proper wage through observing dynamic labor demand.

In other words, we do not simply wish to learn a reward which allows us to imitate agents in the current environment, but which allows us to predict their actions in other settings.

In this paper, we give a precise characterization of the range of rewards which yield a particular policy for an entropy regularized Markov decision problem. This separates the main task of estimation (of the optimal policy from observed actions) from the inverse problem (of inferring rewards from a given policy). We find that even with perfect knowledge of the optimal policy, the corresponding rewards are not fully identifiable; nevertheless, the space of consistent rewards is parameterized by the value function of the control problem.
