Acceleration by Stepsize Hedging I: Multi-Step Descent and the Silver Stepsize Schedule

Topics include Gradient descent, Acceleration, Stepsize hedging.

Can we accelerate convergence of gradient descent without changing the algorithm - just by carefully choosing stepsizes? Surprisingly, we show that the answer is yes. Our proposed Silver Stepsize Schedule optimizes strongly convex functions in k^log_rho 2 approx k^.7864 iterations, where rho = 1+sqrt is the silver ratio and k is the condition number. This is intermediate between the textbook unaccelerated rate k and the accelerated rate sqrt(k) due to Nesterov in 1983. The non-strongly convex setting is conceptually identical, and standard black-box reductions imply an analogous accelerated rate epsilon^-log_rho 2 approx epsilon^(-0).7864. We conjecture and provide partial evidence that these rates are optimal among all possible stepsize schedules. The Silver Stepsize Schedule is constructed recursively in a fully explicit way. It is non-monotonic, fractal-like, and approximately periodic of period k^log_rho 2. This leads to a phase transition in the convergence rate: initially super-exponential (acceleration regime), then exponential (saturation regime).

## Introduction

Gradient descent (GD) is a simple iterative algorithm to minimize an objective function $f$ by producing better and better estimates via the update

GD dates back nearly two hundred years to the work of Cauchy, yet it (and its variants) remain a primary workhorse in modern optimization, engineering, and machine learning due to the practical efficacy, simplicity, and scalability. It is of both theoretical and practical importance to analyze the convergence of GD and moreover to optimize parameters so that this convergence is as fast as possible.

### Robustness

The Silver Stepsize Schedule periodically uses extremely large step sizes, which are overly aggressive in isolation, but effective when combined with other short steps. It is natural to wonder if this dependence between iterations makes such strategies more sensitive to model misspecification, noisy gradients, inexact arithmetic, or other considerations in practical implementations. We expect this may occur, since it does for other accelerated algorithms, see e.g.,.

Our starting point is a known result on convex interpolability, recalled next. There is a set of consistency conditions that any $f \in \mathcal{F}$ must satisfy at any set of points ${\{ x_{i}\}}_{i \in \mathcal{I}}$: the co-coercivity

Although many time-varying stepsize schedules have been considered for GD, no convergences analyses improved over the textbook unaccelerated rate beyond the quadratic case. In 2018, Altschuler's MS thesis considered time-varying stepsize schedules in several settings, all through the unifying lens of hedging and multi-step descent. In Chapter 8 of the thesis, the PESTO framework was used to show for the first time the advantage of using time-varying stepsize schedules for GD beyond the quadratic setting. Explicit solutions were given for $n = {2,3}$ in the strongly convex setting....

For all $i \in {\mathbb{N}}$ and all sufficiently large horizons $n \geqslant 2^{i}$, the stepsize $a_{2^{i}}$ is used in $2^{- i}$ fraction of the $n$-step Silver Stepsize Schedule. For example, for all horizons $n \geqslant 2$, the smallest stepsize $a_{2} = {\kappa/{({\kappa - 1})}}$ is used in every other iteration. For the infinite limit of the Silver Stepsize Schedule (see §1.1.3), the occupation measure simplifies to
