An Optimal Algorithm for Bandit and Zero-Order Convex Optimization with Two-Point Feedback

Topics include Convex optimization, Bandits, Optimization.

We consider the closely related problems of bandit convex optimization with two-point feedback, and zero-order stochastic convex optimization with two function evaluations per round. We provide a simple algorithm and analysis which is optimal for convex Lipschitz functions. This improves on \cite{dujww13}, which only provides an optimal result for smooth functions; Moreover, the algorithm and analysis are simpler, and readily extend to non-Euclidean problems. The algorithm is based on a small but surprisingly powerful modification of the gradient estimator.

## Introduction

We consider the problem of bandit convex optimization with two-point feedback. This problem can be defined as a repeated game between a learner and an adversary as follows: At each round $t$, the adversary picks a convex function $f_{t}$ on ${\mathbb{R}}^{d}$, which is not revealed to the learner. The learner then chooses a point $\mathbf{w}_{t}$ from some known and closed convex set $\mathcal{W} \subseteq {\mathbb{R}}^{d}$, and suffers a loss $f_{t}{(\mathbf{w}_{t})}$.

In this note, we focus on obtaining bounds on the expected average regret (with respect to the learner's randomness).

A closely-related and easier setting is zero-order stochastic convex optimization. In this setting, our goal is to approximately solve ${F{(\mathbf{w})}} = {{\min_{\mathbf{w} \in \mathcal{W}}{\mathbb{E}}_{\xi}}{\lbrack{f{(\mathbf{w};\xi)}}\rbrack}}$, given limited access to ${\{{f{( \cdot;\xi_{t})}}\}}_{t = 1}^{T}$ where $\xi_{t}$ are i.i.d. instantiations. Specifically, we assume that each $f{( \cdot,\xi_{t})}$ is not directly observed, but rather can be queried at two points. This models situations where computing gradients directly is complicated or infeasible.

Like previous algorithms, our algorithm is based on a random gradient estimator, which given a function $f$ and point $\mathbf{w}$, queries $f$ at two random locations close to $\mathbf{w}$, and computes a random vector whose expectation is a gradient of a smoothed version of $f$. The papers essentially use the estimator which queries at $\mathbf{w}$ and $\mathbf{w} + {\delta\mathbf{u}}$ (where $\mathbf{u}$ is a random unit vector and $\delta > 0$ is a small parameter), and returns

In contrast, our algorithm uses a slightly different estimator (also used in ), which queries at ${\mathbf{w} - {\delta\mathbf{u}}},{\mathbf{w} + {\delta\mathbf{u}}}$, and returns

Since the performance of the algorithm crucially depends on the second moment of the gradient estimate, this leads to a highly sub-optimal guarantee. In, this was handled by adding an additional random perturbation and using a more involved analysis. Surprisingly, it turns out that the slightly different estimator in Eq. does not suffer from this problem, and its second moment is essentially linear in the dimension $d$.
