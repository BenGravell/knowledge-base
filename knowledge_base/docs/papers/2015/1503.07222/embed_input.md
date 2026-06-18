Exponential Convergence Bounds Using Integral Quadratic Constraints

Topics include Stability analysis, Online algorithms, Exponential stability.

The theory of integral quadratic constraints (IQCs) allows verification of stability and gain-bound properties of systems containing nonlinear or uncertain elements. Gain bounds often imply exponential stability, but it can be challenging to compute useful numerical bounds on the exponential decay rate. In this work, we present a modification of the classical IQC results of Megretski and Rantzer that leads to a tractable computational procedure for finding exponential rate certificates.

## Introduction

In robust control problems, we seek absolute performance guarantees about a system in the presence of bounded uncertainty. Examples of such results include the small gain theorem & passivity theory, dissipativity theory, and integral quadratic constraints (IQCs).

In this paper, we present a modification of IQC theory, the most general of the aforementioned tools, that allows one to certify *exponential stability* rather than just bounded-input bounded-output (BIBO) stability. Moreover, we can compute numerical bounds on the exponential decay rate of the state.

## Conclusion

We presented a modification of IQC theory that allows the certification of exponential rates. Although we only gave the $\rho$-IQC specialization for pointwise and Zames-Falb IQCs, the concept can in principle be extended to other IQCs such as, for example, uncertain time delays or slowly varying systems. As the dictionary of $\rho$-IQCs is further populated, the applicability of the technique outlined herein would be correspondingly expanded.

Thus, these three conditions ensure BIBO stability of the system in Fig. 3. We then apply Proposition 5 to arrive at exponential stability of Fig. 1.

### Proposition 5

Finding the best upper bound amounts to minimizing $\rho^{2}$ subject to being feasible. This type of problem occurs frequently in robust control and is known as a *generalized eigenvalue optimization problem* (GEVP). The GEVP is not an LMI because is not jointly linear in $\rho^{2}$ and $P$. One simple approach to solving the GEVP is to perform a bisection search on $\rho^{2}$, but there are more sophisticated methods available; see for example.

Even when BIBO stable systems are exponentially stable, the estimates of the exponential decay rates provided by standard IQC theory are typically very conservative. We will show that this conservatism can be greatly reduced if we directly certify exponential stability and use the method presented herein to compute the associated decay rate.

Our modified IQC analysis was successfully applied in to analyze convergence properties of commonly-used optimization algorithms such as the gradient descent method. These algorithms converge at an exponential rate when applied to strongly convex functions, and the modified IQC analysis automatically produces very tight bounds on the convergence rates.
