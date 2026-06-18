Dynamic Programming through the Lens of Semismooth Newton-Type Methods (Extended Version)

Topics include Policy iteration, Value iteration, Control, Markov decision process, Fixed-point iteration, Dynamic programming, Bellman equations, Fixed point.

Policy iteration and value iteration are at the core of many (approximate) dynamic programming methods. For Markov Decision Processes with finite state and action spaces, we show that they are instances of semismooth Newton-type methods to solve the Bellman equation. In particular, we prove that policy iteration is equivalent to the exact semismooth Newton method and enjoys local quadratic convergence rate. This finding is corroborated by extensive numerical evidence in the fields of control and operations research, which confirms that policy iteration generally requires few iterations to achieve convergence even when the number of policies is vast. We then show that value iteration is an instance of the fixed-point iteration method. In this spirit, we develop a novel locally accelerated version of value iteration with global convergence guarantees and negligible extra computational costs.

## INTRODUCTION

Approximate dynamic programming (ADP) is a powerful algorithmic strategy to handle stochastic sequential decision making problems arising in a wide range of applications, from control to games and resource allocation, to name a few. At the core of some of the biggest success stories of ADP is an approximate version of policy iteration. In particular, after an extensive offline training phase where an approximation of the optimal cost is produced, one iteration of an approximate version of policy iteration is performed (online learning). Empirical evidence suggests that this final step greatly enhances performance....

The connection between policy iteration and Newton's method dates back to the late 60's. Puterman and Brumelle were among the first who exploited this connection to study the convergence properties of policy iteration for MDPs with continuous action spaces. More recently, Santos and Ruts exploited this connection to analyze the asymptotic convergence of policy iteration for the discretization of a specific class of MDPs with continuous spaces. Bertsekas in provides a graphical analysis of the connection between policy iteration and Newton's method....

We developed a unified convergence analysis for semismooth Newton-type methods based on the kappa condition. We then proved that PI and VI are semismooth Newton-type methods. In particular, Propositions III.5") and III.6") reveal that PI and VI sit at the two opposite sides in the spectrum of semismooth Newton-type methods: PI enjoys local quadratic contraction but its costs per iteration are demanding; instead, VI is based on a coarse approximation of the elements in Clarke's generalized Jacobian which allows to drastically reduce the costs per iteration at the price of downgrading the local quadratic convergence to a linear one....

Finally, another promising future direction consists in formalizing and exploiting the connection between inexact semismooth Newton methods and optimistic policy iteration-type algorithms.

We call $r$ the Bellman residual function.

The function in Example II.3") is strongly semismooth and BD-regular everywhere, but not CD-regular at $\theta = 5$, since $0 \in {\partial{f{}}}$.

Under Assumption III.4"), PI is an instance of the semismooth Newton method to solve the Bellman residual function (15")). Hence, the local contraction is quadratic.
