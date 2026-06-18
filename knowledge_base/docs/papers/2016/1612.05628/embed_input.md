An Alternative Softmax Operator for Reinforcement Learning

Topics include Reinforcement learning, Planning, Learning.

Proposes the mellowmax operator

A softmax operator applied to a set of values acts somewhat like the maximization function and somewhat like an average. In sequential decision making, softmax is often used in settings where it is necessary to maximize utility but also to hedge against problems that arise from putting all of one's weight behind a single maximum utility decision. The Boltzmann softmax operator is the most commonly used softmax operator in this setting, but we show that this operator is prone to misbehavior. In this work, we study a differentiable softmax operator that, among other properties, is a non-expansion ensuring a convergent behavior in learning and planning. We introduce a variant of SARSA algorithm that, by utilizing the new operator, computes a Boltzmann policy with a state-dependent temperature parameter. We show that the algorithm is convergent and that it performs favorably in practice.

## Introduction

There is a fundamental tension in decision making between choosing the action that has highest expected utility and avoiding "starving" the other actions. The issue arises in the context of the exploration--exploitation dilemma, non-stationary decision problems, and when interpreting observed decisions.

In reinforcement learning, an approach to addressing the tension is the use of *softmax* operators for value-function optimization, and softmax policies for action selection. Examples include value-based methods such as SARSA or expected SARSA, and policy-search methods such as REINFORCE.

An important future work is to expand the scope of our theoretical understanding to the more general function approximation setting, in which the state space or the action space is large and abstraction techniques are used. Note that the importance of non-expansion in the function approximation case is well-established.

Finally, due to the convexity of mellowmax, it is compelling to use it in a gradient-based algorithm in the context of sequential decision making. IRL is a natural candidate given the popularity of softmax in this setting.

### Averaging

Although it has been known for a long time that the Boltzmann operator is not a non-expansion, we are not aware of a published example of an MDP for which two distinct fixed points exist. The MDP presented in Figure 1 is the first example where, as shown in Figure 4, GVI under $\text{boltz}_{\beta}$ has two distinct fixed points. We also show, in Figure 5, a vector field visualizing GVI updates under $\text{boltz}_{\beta = 16.55}$. The updates can move the current estimates farther from the fixed points. The behavior of SARSA (Figure 2) results from the algorithm stochastically bouncing back and forth between the two fixed points....

## Experiments on MDPs

An ideal softmax operator is a parameterized set of operators that:

has parameter settings that allow it to approximate maximization arbitrarily accurately to perform reward-seeking behavior;

is a non-expansion for all parameter settings ensuring convergence to a unique fixed point;

is differentiable to make it possible to improve via gradient-based optimization; and

avoids the starvation of non-maximizing actions.

Let $\text{X} = {x_{1},\ldots,x_{n}}$ be a vector of values. We define the following operators:
