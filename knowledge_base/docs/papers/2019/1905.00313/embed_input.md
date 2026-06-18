Revisiting the Polyak Step Size

Topics include Convex optimization, Gradient descent, Optimization.

This paper revisits the Polyak step size schedule for convex optimization problems, proving that a simple variant of it simultaneously attains near optimal convergence rates for the gradient descent algorithm, for all ranges of strong convexity, smoothness, and Lipschitz parameters, without a-priory knowledge of these parameters.

## Introduction

Scaleable optimization for machine learning is based entirely on first order gradient methods. Besides the age-old method of stochastic approximation, three accelerated methods have proved their practical and theoretical significance: Nesterov acceleration, variance reduction and adaptive learning-rate/regularization.

Adaptive choices of step sizes allow optimization algorithms to accelerate quickly according to the local curvature and smoothness of the optimization landscape. However, in theory, there are few parameter free algorithms, and, in practice, there are many search heuristics utilized.

Now the proof Theorem 2 follows.

### Proof

### Theorem 2

### Proof

Summing up over $T$ iterations, and using Cauchy-Schwartz, we have

Let us examine this question of parameter free, adaptive learning rates for one of the most standard algorithms, namely the gradient descent method:

Although this class of algorithms is not optimal in all settings (i.e. the aforementioned accelerations can be applied), it is fundamental, and we may ask what are optimal known rates along with the optimal step size choices are for this particular algorithm. Here, Table 1 shows the best known rates for gradient descent in the standard regimes: general convex (non-smooth with bounded sub-gradients); $\beta$-smooth; $\alpha$-strongly-convex; and $\beta$-smooth&$\alpha$-strongly convex (see for more details).

From a practical perspective these step size settings are unfortunately disparate in various regimes: ranging from rapidly decaying at $\eta_{t} = {O{(\frac{1}{\alphat})}}$ to moderately decaying at $\eta_{t} = {O{(\frac{1}{\sqrt{t}})}}$ to a constant $\eta_{t} = \frac{1}{\beta}$ (see for more details).

This work: We show that a single (and simple) choice of a step size schedule gives, simultaneously, the optimal convergence (among the class of gradient descent algorithms) in all these regimes, without knowing these parameters in advance. Perhaps surprisingly, this choice is that prescribed by, who argued that this choice was optimal for the non-smooth, convex case (marked as "convex" in Table 1, see also ).

Table 1: Standard convergence rates of gradient descent in convex optimization problems. Error denotes f (xt) − f (x⋆) of a first order methods as a function of the number of iterations....
