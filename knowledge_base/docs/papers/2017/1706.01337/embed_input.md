Exponential Stability Analysis via Integral Quadratic Constraints

Topics include Stability analysis, Online algorithms, Generalization, Exponential stability.

The theory of integral quadratic constraints (IQCs) allows verification of stability and gain-bound properties of systems containing nonlinear or uncertain elements. Gain bounds often imply exponential stability, but it can be challenging to compute useful numerical bounds on the exponential decay rate. This work presents a generalization of the classical IQC results of Megretski and Rantzer that leads to a tractable computational procedure for finding exponential rate certificates that are far less conservative than ones computed from L_2 gain bounds alone. An expanded library of IQCs for certifying exponential stability is also provided and the effectiveness of the technique is demonstrated via numerical examples.

## Introduction

Analysis in the context of robust control is generally concerned with obtaining absolute performance guarantees about a system in the presence of bounded uncertainty. Examples of such results include the small gain theorem & passivity theory, dissipativity theory, the structured singular value $\mu$, and integral quadratic constraints (IQCs).

In this paper, we present a modification of IQC theory, the most general of the aforementioned tools, that allows one to certify *exponential stability* rather than just bounded-input bounded-output (BIBO) stability. Moreover, we can compute numerical bounds on the exponential decay rate of the state.

Even when BIBO stable systems are exponentially stable, estimates of the exponential decay rates provided by standard IQC theory are typically very conservative. We will show that this conservatism can be greatly reduced if we directly certify exponential stability and use the method presented herein to compute the associated decay rate.

Our modified IQC analysis was successfully applied in to analyze convergence properties of commonly-used optimization algorithms such as the gradient descent method. These algorithms converge at an exponential rate when applied to strongly convex functions, and the modified IQC analysis automatically produces very tight bounds on the convergence rates. Another potential application is in time-critical systems. In embedded model predictive control, for example, it is vital to have robust guarantees that desired error bounds will be met in the allotted time without overflow errors and in spite of fixed-point arithmetic.

## Conclusion

IQC theory is the most general tool available for certifying robust stability of systems in feedback with unknown, uncertain, or otherwise difficult nonlinearities. As stable systems are often exponentially stable, it is reasonable to want finer control over not only stability, but also exponential decay rate.

The generalization presented herein enables the certification of robust exponential stability with precise control over the decay rate. Moreover, the library of $\rho$-IQCs provided shows how this approach can be applied as broadly and efficiently as the classical IQC theory.
