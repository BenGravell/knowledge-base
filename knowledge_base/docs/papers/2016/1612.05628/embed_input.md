An Alternative Softmax Operator for Reinforcement Learning

Topics include Reinforcement learning, Planning, Learning.

Proposes the mellowmax operator

A softmax operator applied to a set of values acts somewhat like the maximization function and somewhat like an average. In sequential decision making, softmax is often used in settings where it is necessary to maximize utility but also to hedge against problems that arise from putting all of one's weight behind a single maximum utility decision. The Boltzmann softmax operator is the most commonly used softmax operator in this setting, but we show that this operator is prone to misbehavior. In this work, we study a differentiable softmax operator that, among other properties, is a non-expansion ensuring a convergent behavior in learning and planning. We introduce a variant of SARSA algorithm that, by utilizing the new operator, computes a Boltzmann policy with a state-dependent temperature parameter. We show that the algorithm is convergent and that it performs favorably in practice.

## Introduction

There is a fundamental tension in decision making between choosing the action that has highest expected utility and avoiding "starving" the other actions. The issue arises in the context of the exploration--exploitation dilemma, non-stationary decision problems, and when interpreting observed decisions.

In reinforcement learning, an approach to addressing the tension is the use of *softmax* operators for value-function optimization, and softmax policies for action selection. Examples include value-based methods such as SARSA or expected SARSA, and policy-search methods such as REINFORCE.

An

has parameter settings that allow it to approximate maximization arbitrarily accurately to perform reward-seeking behavior;

is differentiable to make it possible to improve via gradient-based optimization; and

In the following section, we provide a simple example illustrating why the non-expansion property is important, especially in the context of planning and on-policy learning. We then present a new softmax operator that is similar to the Boltzmann operator yet is a non-expansion. We prove several critical properties of this new operator, introduce a new softmax policy, and present empirical results.

## Conclusion and Future Work

We proposed the mellowmax operator as an alternative to the Boltzmann softmax operator. We showed that mellowmax has several desirable properties and that it works favorably in practice. Arguably, mellowmax could be used in place of Boltzmann throughout reinforcement-learning research.

A future direction is to analyze the fixed point of planning, reinforcement-learning, and game-playing algorithms when using the mellowmax operators. In particular, an interesting analysis could be one that bounds the sub-optimality of the fixed points found by GVI.
