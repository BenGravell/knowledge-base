Primal-Dual iLQR

Topics include iLQR, Trajectory optimization, Primal-dual methods, Nonlinear optimal control, JAX.

Introduces Primal-Dual iLQR, incorporating both primal and dual (Lagrange multiplier) variable updates within the iLQR backward/forward pass, enabling trajectory optimization with favorable convergence properties. The technique is restricted to problems without arbitrary state and control constraints; only kinodynamic constraints are handled.

We introduce a new algorithm for solving unconstrained discrete-time optimal control problems. Our method follows a direct multiple shooting approach, and consists of applying the SQP method together with an augmented Lagrangian primal-dual merit function. We use the LQR algorithm to efficiently solve the primal-dual Newton-KKT system. As our algorithm is a specialization of NPSQP, it inherits its generic properties, including global convergence, fast local convergence, and the lack of need for second order corrections or dimension expansions, improving on existing direct multiple shooting approaches such as acados, ALTRO, GNMS, FATROP, and FDDP. The solutions of the LQR-shaped subproblems posed by our algorithm can be be parallelized to run in time logarithmic in the number of stages, states, and controls. Moreover, as our method avoids sequential rollouts of the nonlinear dynamics, it can run in parallel time per line search iteration. Therefore, this paper provides a practical, theoretically sound, and highly parallelizable (for example, with a GPU) method for solving nonlinear discrete-time optimal control problems....

## Introduction

### II-A Unconstrained Discrete-Time Optimal Control Problems

Unconstrained discrete-time optimal control problems are optimization problems of the form

The proposed algorithm is globally convergent and does not impede superlinear local convergence, without requiring second order corrections to be applied.

Finally, solving the subproblems posed by our method can be parallelized to run in time logarithmic in the number of stages, states, and controls. Moreover, as our method never performs nonlinear dynamics rollouts, it allows that the evaluation of the dynamics and derivatives be computed in parallel, resulting in $O{}$ parallel time per line search iteration.

Note that NPSQP \[\] uses a slightly different line search method. Specifically, it enforces both Wolfe conditions, not only the Armijo condition.

Similarly, it can also be shown that $\Delta\lambda$ is the corresponding Lagrange multiplier. As long as $Q$ is positive definite, this cost function is bounded from below. Depending on the sparsity pattern of this system, weaker requirements on $Q$ might also guarantee this.

A parallel algorithm for solving these problems was presented in \[\], although we require some minor changes due to a difference in problem formulations. In order to describe this method, we need to introduce an important definition. An interval value function $V_{i\rightarrow j}{(x_{i},x_{j})}$ maps states $x_{i},x_{j}$ at stages $i,j$ to the minimum possible cost incurred in stages $i,\ldots,{j - 1}$ among all trajectories that start at state $x_{i}$ in stage $i$ and end at state $x_{j}$ in stage $j$ ($\infty$ if no such trajectory exists). The key insight of \[\] is that the optimal interval value functions can be represented as

Such optimization problems are ubiquitous in the fields of motion planning and controls.

### II-B Related Work

Naïf applications of generic optimization methods to unconstrained discrete-time optimal control problems would require $O{({N^{3}{({n + m})}^{3}})}$ operations for solving the linear systems posed at each iteration, where $N,n,m$ are respectively the number of stages, states, and controls of the problem. The first algorithm to improve on this was DDP \[\], achieving complexity $O{({N{({n + m})}^{3}})}$. Its convergence properties were studied in \[\]....
