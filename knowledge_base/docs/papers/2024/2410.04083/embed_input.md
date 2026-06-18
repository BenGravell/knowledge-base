OPTAMI: Global Superlinear Convergence of High-order Methods

Topics include Convex optimization, Optimization, OPTAMI.

Second-order methods for convex optimization outperform first-order methods in terms of theoretical iteration convergence, achieving rates up to O(k^(-5)) for highly-smooth functions. However, their practical performance and applications are limited due to their multi-level structure and implementation complexity. In this paper, we present new results on high-order optimization methods, supported by their practical performance. First, we show that the basic high-order methods, such as the Cubic Regularized Newton Method, exhibit global superlinear convergence for mu-strongly star-convex functions, a class that includes mu-strongly convex functions and some non-convex functions. Theoretical convergence results are both inspired and supported by the practical performance of these methods. Secondly, we propose a practical version of the Nesterov Accelerated Tensor method, called NATA. It significantly outperforms the classical variant and other high-order acceleration techniques in practice. The convergence of NATA is also supported by theoretical results. Finally, we introduce an open-source computational library for high-order methods, called OPTAMI.

## Introduction

In

where

## Basic Methods

High-order model.

where, for $p = 1$, we simplify notation to $\Phi_{x}{(y)}$. From, we can get the next upper-bound of the function $f{(x)}$

## Conclusion

Limitations. This paper primarily focuses on high-order methods which come with certain limitations. First of all, they have computational and memory limitations in high-dimensional spaces, due to the need for Hessian calculations. There are, however, approaches to overcome this, such as using first-order subsolvers, or inexact Hessian approximations like Quasi-Newton approximations (BFGS, L-SR1). In this paper, we focus on the exact Hessian to analyze methods' peak performance.\
Another limitation arises from the specific function classes and the theoretical results considered.

Conclusion and Future work. In the paper, we demonstrated that the basic high-order methods exhibit global superlinear convergence for $\mu$-strongly star-convex functions. This result is significant because it shows that high-order methods accelerate with each iteration, in stark contrast to first-order methods, which typically have a steady linear convergence rate. This raises intriguing questions: Can superlinear convergence rates be established for accelerated high-order methods as well?
