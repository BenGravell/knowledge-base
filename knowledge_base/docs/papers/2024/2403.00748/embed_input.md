Primal-Dual iLQR

Topics include iLQR, Trajectory optimization, Primal-dual methods, Nonlinear optimal control, JAX.

Introduces Primal-Dual iLQR, incorporating both primal and dual (Lagrange multiplier) variable updates within the iLQR backward/forward pass, enabling trajectory optimization with favorable convergence properties. The technique is restricted to problems without arbitrary state and control constraints; only kinodynamic constraints are handled.

We introduce a new algorithm for solving unconstrained discrete-time optimal control problems. Our method follows a direct multiple shooting approach, and consists of applying the SQP method together with an augmented Lagrangian primal-dual merit function. We use the LQR algorithm to efficiently solve the primal-dual Newton-KKT system. As our algorithm is a specialization of NPSQP, it inherits its generic properties, including global convergence, fast local convergence, and the lack of need for second order corrections or dimension expansions, improving on existing direct multiple shooting approaches such as acados, ALTRO, GNMS, FATROP, and FDDP. The solutions of the LQR-shaped subproblems posed by our algorithm can be be parallelized to run in time logarithmic in the number of stages, states, and controls. Moreover, as our method avoids sequential rollouts of the nonlinear dynamics, it can run in parallel time per line search iteration. Therefore, this paper provides a practical, theoretically sound, and highly parallelizable (for example, with a GPU) method for solving nonlinear discrete-time optimal control problems.

## II-A Unconstrained Discrete-Time Optimal Control Problems

Unconstrained discrete-time optimal control problems are optimization problems of the form

Such optimization problems are ubiquitous in the fields of motion planning and controls.

## II-B Related Work

Naïf applications of generic optimization methods to unconstrained discrete-time optimal control problems would require $O{({N^{3}{({n + m})}^{3}})}$ operations for solving the linear systems posed at each iteration, where $N,n,m$ are respectively the number of stages, states, and controls of the problem. The first algorithm to improve on this was DDP, achieving complexity $O{({N{({n + m})}^{3}})}$. Its convergence properties were studied.

## Conclusion

This paper introduces a new algorithm for solving unconstrained discrete-time optimal control problems, called Primal-Dual iLQR.

This framework can easily be extended to handle constrained problems. Ideally, an interior point method would be used to handle general inequality constraints. It would also be possible to handle both general equality and inequality constraints with an augmented Lagrangian method, although local superlinear convergence would be lost. In both cases, the LQR shape of the posed subproblems can be preserved. Preserving superlinar local convergence in the presence of general equality constraints would require employing a linear equality-constrained LQR subproblem solver.

Our method is substantially easier to warm start as compared to single-shooting methods such as DDP, iLQR, or Stagewise Newton, as it treats both state and control trajectories as free variables in the optimization problem (without incurring extra computational costs); this allows them to be independently seeded, even in dynamically infeasible ways.

Finally, solving the subproblems posed by our method can be parallelized to run in time logarithmic in the number of stages, states, and controls. Moreover, as our method never performs nonlinear dynamics rollouts, it allows that the evaluation of the dynamics and derivatives be computed in parallel, resulting in $O{}$ parallel time per line search iteration.
