An Optimal Algorithm for Bandit and Zero-Order Convex Optimization with Two-Point Feedback

Topics include Convex optimization, Bandits, Optimization.

We consider the closely related problems of bandit convex optimization with two-point feedback, and zero-order stochastic convex optimization with two function evaluations per round. We provide a simple algorithm and analysis which is optimal for convex Lipschitz functions. This improves on \cite{dujww13}, which only provides an optimal result for smooth functions; Moreover, the algorithm and analysis are simpler, and readily extend to non-Euclidean problems. The algorithm is based on a small but surprisingly powerful modification of the gradient estimator.

## Introduction

We consider the problem of bandit convex optimization with two-point feedback. This problem can be defined as a repeated game between a learner and an adversary as follows: At each round $t$, the adversary picks a convex function $f_{t}$ on ${\mathbb{R}}^{d}$, which is not revealed to the learner. The learner then chooses a point $\mathbf{w}_{t}$ from some known and closed convex set $\mathcal{W} \subseteq {\mathbb{R}}^{d}$, and suffers a loss $f_{t}{(\mathbf{w}_{t})}$....

In this note, we focus on obtaining bounds on the expected average regret (with respect to the learner's randomness).

Combining these inequalities and plugging back into Eq., we get

Dividing both sides by $T$, the result follows.

This bound matches (this time up to a logarithmic factor) the lower bound in for this setting.

The analysis of the algorithm is presented in the following theorem:

over $\mathcal{W}$, where $\mathbf{u}_{t}$ is a vector picked uniformly at random from the Euclidean unit sphere. Then the function is convex, Lipschitz with constant $G_{2}$, satisfies

A closely-related and easier setting is zero-order stochastic convex optimization. In this setting, our goal is to approximately solve ${F{(\mathbf{w})}} = {{\min_{\mathbf{w} \in \mathcal{W}}{\mathbb{E}}_{\xi}}{\lbrack{f{(\mathbf{w};\xi)}}\rbrack}}$, given limited access to ${\{{f{( \cdot;\xi_{t})}}\}}_{t = 1}^{T}$ where $\xi_{t}$ are i.i.d. instantiations. Specifically, we assume that each $f{( \cdot,\xi_{t})}$ is not directly observed, but rather can be queried at two points. This models situations where computing gradients directly is complicated or infeasible....

Thus, an algorithm for bandit optimization can be converted to an algorithm for zero-order stochastic optimization with similar guarantees.

The bandit optimization setting with two-point feedback was proposed and studied in. Independently, and considered two-point methods for stochastic optimization. Both papers are based on randomized gradient estimates which are then fed into standard first-order algorithms (e.g. gradient descent, or more generally mirror descent). However, the regret/error guarantees in both papers were suboptimal in terms of the dependence on the dimension....

In this note, we present and analyze a simple algorithm with the following properties:
