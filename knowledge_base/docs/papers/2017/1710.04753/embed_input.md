A Robust Accelerated Optimization Algorithm for Strongly Convex Functions

Topics include Robustness, Optimization, Control, Robust momentum method, Convex function, Gradient method.

This work proposes an accelerated first-order algorithm we call the Robust Momentum Method for optimizing smooth strongly convex functions. The algorithm has a single scalar parameter that can be tuned to trade off robustness to gradient noise versus worst-case convergence rate. At one extreme, the algorithm is faster than Nesterov's Fast Gradient Method by a constant factor but more fragile to noise. At the other extreme, the algorithm reduces to the Gradient Method and is very robust to noise. The algorithm design technique is inspired by methods from classical control theory and the resulting algorithm has a simple analytical form. Algorithm performance is verified on a series of numerical simulations in both noise-free and relative gradient noise cases.

## Introduction

Consider the unconstrained optimization problem

where $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is $L$-smooth and $m$-strongly convex. The strong convexity of $f$ guarantees that there exists a unique minimizer $x_{\star}$ satisfying ${{\nabla f}{(x_{\star})}} = 0$. First-order methods are widely used for solving when the Hessian is prohibitively expensive to compute, e.g., when the problem dimension is large. A simple first-order algorithm for solving is the Gradient Method (GM),

For smooth and strongly convex $f$, the GM with a well-chosen stepsize converges linearly to the optimizer. That is, for some $c \geq 0$ and $\rho \in {\lbrack 0,1)}$, we have

For example, the standard choice $\alpha = {1/L}$ leads to a linear rate $\rho = {1 - \frac{m}{L}}$, while the choice $\alpha = \frac{2}{L + m}$ results in the improved linear rate $\rho = \frac{L - m}{L + m}$.

The FGM tuned with $\alpha = \frac{1}{L}$ and $\beta = \frac{\sqrt{L} - \sqrt{m}}{\sqrt{L} + \sqrt{m}}$ converges with rate $\rho^{2} < {1 - \sqrt{m/L}}$, which is faster than the GM rate^22^2A numerical study in revealed that the standard rate bound for FGM derived in is conservative. Nevertheless, the bound has a simple algebraic form and is asymptotically tight.. The rate can be improved to $\rho = {1 - \sqrt{m/L}}$ using an accelerated algorithm called the Triple Momentum Method. This is the fastest known worst-case convergence rate for this class of problems.

As observed in \[3, §5.2\], optimization algorithm design involves a tradeoff between performance and robustness. For example, consider stepsize tuning for the GM. Using $\alpha = \frac{2}{L + m}$ optimizes the convergence rate, but makes the algorithm fragile to gradient noise. The more conservative choice $\alpha = \frac{1}{L}$ results in slower convergence, but more robustness to noise. This is consistent with the intuition that a smaller stepsize can improve the algorithm's robustness at the price of degrading its performance.
