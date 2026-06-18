Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees

Topics include Semidefinite programming, Lyapunov methods, Optimization, Automated convergence proofs, Lyapunov functions.

We present a novel way of generating Lyapunov functions for proving linear convergence rates of first-order optimization methods. Our approach provably obtains the fastest linear convergence rate that can be verified by a quadratic Lyapunov function (with given states), and only relies on solving a small-sized semidefinite program. Our approach combines the advantages of performance estimation problems (PEP, due to Drori & Teboulle ) and integral quadratic constraints (IQC, due to Lessard et al. ), and relies on convex interpolation (due to Taylor et al. ).

## Introduction

In this work, we study first-order methods for solving the (unconstrained) minimization problem

where $f:^{d}\rightarrow$. In the sequel, we focus on the case where $f$ is $L$-smooth and $\mu$-strongly convex, though our methodology can be adapted to a broader class of problems.

### Code

The code used to implement ($\rho$-SDP) and generate the figures in this paper is available at

### Performance Estimation Problem (PEP)

Lemma 2. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") shows that if we can find a quadratic Lyapunov function, then we can use this to prove linear convergence of method ($\mathcal{M}$) when $f \in \mathcal{F}_{\mu,L}$. In the following section, we construct an SDP whose feasibility is necessary and sufficient for the existence of such a Lyapunov function.

### Positive Definite Quadratics From Sampling

To solve ($\mathcal{P}$), we consider methods that iteratively update their estimate of the optimizer using only gradient evaluations. One possibility for proving convergence of such methods is by finding *Lyapunov functions*.

A Lyapunov function can be interpreted as defining an "energy" that decreases geometrically with each iteration of the method, with an energy of zero corresponding to reaching the optimal solution of ($\mathcal{P}$). The existence of such an energy function thus provides a straightforward certificate of linear convergence for the iterative method.

In this paper, we present an automated way of generating quadratic Lyapunov functions for certifying linear convergence of first-order iterative methods to solve ($\mathcal{P}$). The procedure relies on solving a small-sized semidefinite program (SDP) so it is computationally efficient. Moreover, the procedure is *tight*, meaning that if the SDP is infeasible, then no such quadratic Lyapunov function exists.

Our results unify recent SDP-based works for certifying convergence of first-order methods, namely: performance estimation problems and integral quadratic constraints from robust control, using smooth strongly convex interpolation. These connections are further discussed in Section 4.3.

### Organization

The paper is organized as follows. We describe the class of methods under consideration and basic properties of Lyapunov functions in Sections 2...
