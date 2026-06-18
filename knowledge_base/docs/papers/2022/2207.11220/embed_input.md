Stochastic Algebraic Riccati Equations Are Almost as Easy as Deterministic Ones Theoretically

Topics include Optimal control, Control, Algebraic Riccati equation, Riccati equation.

Stochastic algebraic Riccati equations, also known as rational algebraic Riccati equations, arising in linear-quadratic optimal control for stochastic linear time-invariant systems, were considered to be not easy to solve. The-state-of-art numerical methods most rely on differentiability or continuity, such as Newton-type method, LMI method, or homotopy method. In this paper, we will build a novel theoretical framework and reveal the intrinsic algebraic structure appearing in this kind of algebraic Riccati equations. This structure guarantees that to solve them is almost as easy as to solve deterministic/classical ones, which will shed light on the theoretical analysis and numerical algorithm design for this topic.

## Introduction

Algebraic Riccati equations (AREs) arise in various models related to control theory, especially in linear-quadratic optimal control design. The deterministic/classical ones are considered for the deterministic linear time-invariant systems, including discrete-time algebraic Riccati equations (DAREs)

and continuous-time algebraic Riccati equations (CAREs)

However, the two iterations could not be straightforwardly used as mature numerical methods to solve the equations, because the left semi-tensor products make the size of involving matrices grow twice-exponentially ($r^{2^{k}}n$ in fact), which makes the storage an impossible task. Take the doubling iteration 2.15 or 3.17 as an example: if ${n = 1},{r = 2}$, then the numbers of rows of first several terms $A_{k}$ or $E_{k}$ (also the number of rows/columns of $G_{k}$) are $2,4,16,256,65536$. Hence more work needs to be done on developing practical algorithms, though the algebraic structure is revealed as clearly as the deterministic AREs.

Anyway, as we can see, many parallel theoretical results and numerical methods for DAREs and CAREs can probably be generalized to SDAREs and SCAREs. Plenty of results are ready to be examined, and of course a lot of gaps are still needed to be filled. We believe that there must be efficient algorithms proposed under the philosophy of this paper, and we leave it for future work.

Clearly, in the case $r = 1$ the $\ltimes$-symplecticity and the $\ltimes$-doubling transformation degenerate to the classical symplecticity and the doubling transformation respectively.

Similarly, substituting $\Delta_{t - 2}$ with its expression of $\Delta_{t - 3}$, we also have

## SCARE

During many years, people have developed rich theoretical results and numerical methods for the DAREs and CAREs. Readers are referred to to obtain an overview for both theories and algorithms. In comparison, the stochastic/rational ones are considered for the stochastic linear time-invariant systems, including stochastic discrete-time algebraic Riccati equations (SDAREs)

and stochastic continuous-time algebraic Riccati equations (SCAREs)

Here $r - 1$ is the number of stochastic processes involved in the stochastic systems dealt with, and it is easy to check that for the case $r = 1$ SDAREs and SCAREs degenerate to DAREs and CAREs respectively....
