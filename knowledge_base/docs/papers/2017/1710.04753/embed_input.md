A Robust Accelerated Optimization Algorithm for Strongly Convex Functions

Topics include Robustness, Optimization, Control, Robust momentum method, Convex function, Gradient method.

This work proposes an accelerated first-order algorithm we call the Robust Momentum Method for optimizing smooth strongly convex functions. The algorithm has a single scalar parameter that can be tuned to trade off robustness to gradient noise versus worst-case convergence rate. At one extreme, the algorithm is faster than Nesterov's Fast Gradient Method by a constant factor but more fragile to noise. At the other extreme, the algorithm reduces to the Gradient Method and is very robust to noise. The algorithm design technique is inspired by methods from classical control theory and the resulting algorithm has a simple analytical form. Algorithm performance is verified on a series of numerical simulations in both noise-free and relative gradient noise cases.

## Introduction

Consider the unconstrained optimization problem

where $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is $L$-smooth and $m$-strongly convex. The strong convexity of $f$ guarantees that there exists a unique minimizer $x_{\star}$ satisfying ${{\nabla f}{(x_{\star})}} = 0$. First-order methods are widely used for solving when the Hessian is prohibitively expensive to compute, e.g., when the problem dimension is large. A simple first-order algorithm for solving is the Gradient Method (GM),

To illustrate the noise robustness properties of different tunings of the Robust Momentum Method, we compared it to the Fast Gradient Method when applied to a simple two-dimensional quadratic function. We used the gradient

where the gradient noise is $r_{k} = {- {\delta{\nabla f}{(y_{k})}}}$. See Figure 4. The RMM with $\nu = 0$ has the fastest convergence rate in the noiseless case ($\delta = 0$), but quickly diverges when noise is present. The FGM is more robust to noise, but also diverges when the noise magnitude $\delta$ is too large. The RMM with $\nu = 0.55$ remains stable for large amounts of noise, although in the absence of noise the convergence rate is slower than both other methods.

The algebraic identity has three main terms. We will see how each serves a role in explaining the convergence and robustness properties of our algorithm. We are now ready to prove Theorem 1.

### Proposition 2 (Co-coercivity)

Continuing with the frequency-domain interpretation, Lur'e systems can be analyzed using the formalism of Integral Quadratic Constraints (IQCs). To this end, the nonlinearity is characterized by a quadratic inequality that holds between its input and output

For smooth and strongly convex $f$, the GM with a well-chosen stepsize converges linearly to the optimizer. That is, for some $c \geq 0$ and $\rho \in {\lbrack 0,1)}$, we have

For example, the standard choice $\alpha = {1/L}$ leads to a linear rate $\rho = {1 - \frac{m}{L}}$, while the choice $\alpha = \frac{2}{L + m}$ results in the improved linear rate $\rho = \frac{L - m}{L + m}$.

The issue with the Gradient Method, however, is that the convergence rate is slow, especially for ill-conditioned problems where the ratio $\frac{L}{m}$ is large. A common method of accelerating convergence is to use *momentum*....
