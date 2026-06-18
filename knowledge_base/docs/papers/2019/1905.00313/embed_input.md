Revisiting the Polyak Step Size

Topics include Convex optimization, Gradient descent, Optimization.

This paper revisits the Polyak step size schedule for convex optimization problems, proving that a simple variant of it simultaneously attains near optimal convergence rates for the gradient descent algorithm, for all ranges of strong convexity, smoothness, and Lipschitz parameters, without a-priory knowledge of these parameters.

## Introduction

Scaleable optimization for machine learning is based entirely on first order gradient methods. Besides the age-old method of stochastic approximation, three accelerated methods have proved their practical and theoretical significance: Nesterov acceleration, variance reduction and adaptive learning-rate/regularization.

Adaptive choices of step sizes allow optimization algorithms to accelerate quickly according to the local curvature and smoothness of the optimization landscape. However, in theory, there are few parameter free algorithms, and, in practice, there are many search heuristics utilized.

Let

Although this class of algorithms is not optimal in all settings (i.e. the aforementioned accelerations can be applied), it is fundamental, and we may ask what are optimal known rates along with the optimal step size choices are for this particular algorithm. Here, Table 1 shows the best known rates for gradient descent in the standard regimes: general convex (non-smooth with bounded sub-gradients); $\beta$-smooth; $\alpha$-strongly-convex; and $\beta$-smooth&$\alpha$-strongly convex (see for more details).

This work: We show that a single (and simple) choice of a step size schedule gives, simultaneously, the optimal convergence (among the class of gradient descent algorithms) in all these regimes, without knowing these parameters in advance. Perhaps surprisingly, this choice is that prescribed , who argued that this choice was optimal for the non-smooth, convex case (marked as "convex" in Table 1, see also ).
