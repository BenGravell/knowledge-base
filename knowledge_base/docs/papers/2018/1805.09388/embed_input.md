Regret Bounds for Robust Adaptive Control of the Linear Quadratic Regulator

Topics include Regret bounds, Robustness, Control, Linear quadratic regulator, Adaptive control, Robust control, Linear systems.

We consider adaptive control of the Linear Quadratic Regulator (LQR), where an unknown linear system is controlled subject to quadratic costs. Leveraging recent developments in the estimation of linear systems and in robust controller synthesis, we present the first provably polynomial time algorithm that provides high probability guarantees of sub-linear regret on this problem. We further study the interplay between regret minimization and parameter estimation by proving a lower bound on the expected regret in terms of the exploration schedule used by any algorithm. Finally, we conduct a numerical study comparing our robust adaptive algorithm to other methods from the adaptive LQR literature, and demonstrate the flexibility of our proposed method by extending it to a demand forecasting problem subject to state constraints.

## Introduction

The problem of adaptively controlling an unknown dynamical system has a rich history, with classical asymptotic results of convergence and stability dating back decades. Of late, there has been a renewed interest in the study of a particular instance of such problems, namely the adaptive Linear Quadratic Regulator (LQR), with an emphasis on *non-asymptotic* guarantees of stability and performance....

### Related Work

We presented a polynomial-time algorithm for the adaptive LQR problem that provides high probability guarantees of sub-linear regret. In contrast to other approaches to this problem, our robust adaptive method guarantees stability, robust performance, and parameter estimation. We also explored the interplay between regret minimization and parameter estimation, identifying fundamental limits connecting the two.

Several questions remain to be answered. It is an open question whether a polynomial-time algorithm can achieve a regret of $\overset{\sim}{\mathcal{O}}{(\sqrt{T})}$. In our implementation of OFU, we observed that PGD performed quite effectively. Interesting future work is to see if the techniques of Fazel et al. for policy gradient optimization on LQR can be applied to prove convergence of PGD on the OFU subroutine, which would provide an optimal polynomial-time algorithm....

### Assumption 3.1

Although other approaches to optimal controller design exists, we argue now that the SLS parameterization has some appealing properties when applied to the control of uncertain systems. In particular, suppose that rather than having access to the true system transition matrices $(A_{\star},B_{\star})$, we instead only have access to estimates $(\hat{A},\hat{B})$. The SLS framework allows us to characterize the system responses achieved by a controller, computed using only the estimates $(\hat{A},\hat{B})$, on the true system $(A_{\star},B_{\star})$....

We saw that Algorithm 1 achieves $\overset{\sim}{\mathcal{O}}{(T^{2/3})}$ regret with high probability. Now we provide a matching algorithmic lower bound on the expected regret, showing that the analysis presented in Section 3.1 is sharp as a function of $T$. Moreover, our lower bound characterizes how much regret must be accrued in order to achieve a specified estimation rate for the system parameters $(A_{\star},B_{\star})$.
