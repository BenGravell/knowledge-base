Acceleration by Stepsize Hedging I: Multi-Step Descent and the Silver Stepsize Schedule

Topics include Gradient descent, Acceleration, Stepsize hedging.

Can we accelerate convergence of gradient descent without changing the algorithm - just by carefully choosing stepsizes? Surprisingly, we show that the answer is yes. Our proposed Silver Stepsize Schedule optimizes strongly convex functions in k^log_rho 2 approx k^.7864 iterations, where rho = 1+sqrt is the silver ratio and k is the condition number. This is intermediate between the textbook unaccelerated rate k and the accelerated rate sqrt(k) due to Nesterov in 1983. The non-strongly convex setting is conceptually identical, and standard black-box reductions imply an analogous accelerated rate epsilon^-log_rho 2 approx epsilon^(-0).7864. We conjecture and provide partial evidence that these rates are optimal among all possible stepsize schedules. The Silver Stepsize Schedule is constructed recursively in a fully explicit way. It is non-monotonic, fractal-like, and approximately periodic of period k^log_rho 2. This leads to a phase transition in the convergence rate: initially super-exponential (acceleration regime), then exponential (saturation regime).

## Introduction

Gradient descent (GD) is a simple iterative algorithm to minimize an objective function $f$ by producing better and better estimates via the update

GD dates back nearly two hundred years to the work of Cauchy, yet it (and its variants) remain a primary workhorse in modern optimization, engineering, and machine learning due to the practical efficacy, simplicity, and scalability. It is of both theoretical and practical importance to analyze the convergence of GD and moreover to optimize parameters so that this convergence is as fast as possible.

A central fact in convex optimization is that with a prudent choice of the stepsize schedule $\{\alpha_{t}\}$---the only^11^1In convex optimization, we typically view the initialization $x_{0}$ as part of the problem instance rather than a parameter choice, since $x_{0} = 0$ without loss of generality after a possible translation of the objective function $f$. parameters of the algorithm---running GD from any initialization $x_{0}$ produces iterates which optimize $f$ to arbitrary accuracy. Quantifying this statement leads to two intertwined questions: How fast does $x_{n}$ converge to a minimizer $x^{\ast}$ of $f$?

This series of papers revisits these classical questions in the fundamental setting of smooth^22^2In the non-smooth setting, it is classically known that acceleration is impossible, and moreover GD achieves the minimax-optimal convergence rate with simple monotonically decaying stepsize schedules like $\alpha_{t} \asymp {1/\sqrt{t}}$. convex optimization. Our overarching goal is to understand how much mileage can be obtained by simply optimizing the stepsize choice for GD.

## Future work

This work removes a key stumbling block in previous analyses of optimization algorithms: we show that directly analyzing *multi-step descent* can lead to improved convergence analyses. This general principle opens up a number of directions in both the design and analysis of optimization algorithms. We list a few here.
