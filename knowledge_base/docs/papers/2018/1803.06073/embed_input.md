Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees

Topics include Semidefinite programming, Lyapunov methods, Optimization, Automated convergence proofs, Lyapunov functions.

We present a novel way of generating Lyapunov functions for proving linear convergence rates of first-order optimization methods. Our approach provably obtains the fastest linear convergence rate that can be verified by a quadratic Lyapunov function (with given states), and only relies on solving a small-sized semidefinite program. Our approach combines the advantages of performance estimation problems (PEP, due to Drori & Teboulle ) and integral quadratic constraints (IQC, due to Lessard et al. ), and relies on convex interpolation (due to Taylor et al. ).

## Introduction

In this work, we study first-order methods for solving the (unconstrained) minimization problem

where $f:^{d}\rightarrow$. In the sequel, we focus on the case where $f$ is $L$-smooth and $\mu$-strongly convex, though our methodology can be adapted to a broader class of problems.

To solve ($\mathcal{P}$), we consider methods that iteratively update their estimate of the optimizer using only gradient evaluations. One possibility for proving convergence of such methods is by finding *Lyapunov functions*.

In this paper, we present an automated way of generating quadratic Lyapunov functions for certifying linear convergence of first-order iterative methods to solve ($\mathcal{P}$). The procedure relies on solving a small-sized semidefinite program (SDP) so it is computationally efficient. Moreover, the procedure is *tight*, meaning that if the SDP is infeasible, then no such quadratic Lyapunov function exists.

## Conclusion

In this work, we studied first-order iterative fixed-step methods applied to smooth strongly convex functions. We presented a semidefinite formulation whose feasibility is both necessary and sufficient for the existence of a quadratic Lyapunov function. For smooth strongly convex minimization, restriction to quadratic Lyapunov functions is natural, as nonlinearities are exactly characterized by quadratic interpolation constraints. Using other tools such as sum-of-squares Lyapunov functions (see e.g., Parrilo ) could be beneficial for more general algorithm and problem classes.

This methodology unifies two previous approaches to worst-case analyses: performance estimation due to Drori & Teboulle and integral quadratic constraints due to Lessard et al.. Moreover, this approach admits a large number of potential extensions, both in terms of classes of optimization problems and types of algorithms that can be analyzed (see e.g., extensions for performance estimation ). In particular, Lyapunov functions can be used to study sublinear convergence rates (see e.g., Hu & Lessard ), switched systems (e.g., for adaptive methods), noisy methods (see e.g., Cyrus et al. ), or continuous-time settings such as .
