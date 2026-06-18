On the Convergence of the Iterative Linear Exponential Quadratic Gaussian Algorithm to Stationary Points

A classical method for risk-sensitive nonlinear control is the iterative linear exponential quadratic Gaussian algorithm. We present its convergence analysis from a first-order optimization viewpoint. We identify the objective that the algorithm actually minimizes and we show how the addition of a proximal term guarantees convergence to a stationary point.

## Introduction

We present a convergence analysis of the classical iterative linear quadratic exponential Gaussian controller (ILEQG) for finite-horizon risk-sensitive or safe nonlinear control. The ILEQG algorithm is particularly popular in robotics applications and can be seen as a risk-sensitive counterpart of the iterative linear quadratic Gaussian (ILQG) algorithm. We adopt here the viewpoint of the modern complexity analysis of first-order optimization algorithms as done by Roulet et al. for ILQG.

We address the following questions: (i) what is the convergence rate of ILEQG to a stationary point? (ii) how can we set the step-size to guarantee a decreasing objective along the iterations? The analysis we present here sheds light on these questions by highlighting the objective minimized by ILEQG which is a Gaussian approximation of a risk-sensitive cost around the linearized trajectory. We underscore the importance of the addition of a proximal regularization component for ILEQG to guarantee a worst-case convergence to a stationary point of the objective.

The main result of the paper is Theorem 2.5, where a sufficient decrease condition to choose the strength of the proximal regularization is given. The result also yields a complexity bound in terms of calls to a dynamic programming procedure implementable in a "differentiable programming" framework, that is, a computational framework equipped with an automatic differentiation software library. We illustrate the variant of the iterative regularized linear quadratic exponential Gaussian controller we recommend on simple risk-sensitive nonlinear control examples.

## Conclusion

We dissected the ILEQG algorithm to understand its correct implementation, this revealed: (i) the objective it minimizes, that is not the risk-sensitive cost but an approximation of it, (ii) the necessary introduction from an optimization viewpoint of a regularization inside the step, (iii) a sufficient decrease condition that ensures proven stationary convergence to a near-stationary point.
