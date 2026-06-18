Stochastic Algebraic Riccati Equations Are Almost as Easy as Deterministic Ones Theoretically

Topics include Optimal control, Control, Algebraic Riccati equation, Riccati equation.

Stochastic algebraic Riccati equations, also known as rational algebraic Riccati equations, arising in linear-quadratic optimal control for stochastic linear time-invariant systems, were considered to be not easy to solve. The-state-of-art numerical methods most rely on differentiability or continuity, such as Newton-type method, LMI method, or homotopy method. In this paper, we will build a novel theoretical framework and reveal the intrinsic algebraic structure appearing in this kind of algebraic Riccati equations. This structure guarantees that to solve them is almost as easy as to solve deterministic/classical ones, which will shed light on the theoretical analysis and numerical algorithm design for this topic.

## Introduction

Algebraic Riccati equations (AREs) arise in various models related to control theory, especially in linear-quadratic optimal control design. The deterministic/classical ones are considered for the deterministic linear time-invariant systems, including discrete-time algebraic Riccati equations (DAREs)

and continuous-time algebraic Riccati equations (CAREs)

During many years, people have developed rich theoretical results and numerical methods for the DAREs and CAREs. Readers are referred to to obtain an overview for both theories and algorithms. In comparison, the stochastic/rational ones are considered for the stochastic linear time-invariant systems, including stochastic discrete-time algebraic Riccati equations (SDAREs)

and stochastic continuous-time algebraic Riccati equations (SCAREs)

The key to the problem is the algebraic structures behind the equations. In this paper, we will build up a simple and clear algebraic interpretation of SDAREs and SCAREs with the help of the so-called left semi-tensor product. In the analysis we find out the Toeplitz structure and the symplectic structure appearing in the equations, and illustrate the fact that the fixed point iteration and the doubling iteration are also valid for them. The algebraic structures found here will shed light on the theoretical analysis and numerical algorithms design, and strongly imply that stochastic AREs are almost as easy as deterministic ones.
