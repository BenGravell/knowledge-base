<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Primal-Dual iLQR

Topics include iLQR, Trajectory optimization, Primal-dual methods, Nonlinear optimal control, JAX.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces Primal-Dual iLQR, incorporating both primal and dual (Lagrange multiplier) variable updates within the iLQR backward/forward pass, enabling trajectory optimization with favorable convergence properties. The technique is restricted to problems without arbitrary state and control constraints; only kinodynamic constraints are handled.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce a new algorithm for solving unconstrained discrete-time optimal control problems. Our method follows a direct multiple shooting approach, and consists of applying the SQP method together with an augmented Lagrangian primal-dual merit function. We use the LQR algorithm to efficiently solve the primal-dual Newton-KKT system. As our algorithm is a specialization of NPSQP, it inherits its generic properties, including global convergence, fast local convergence, and the lack of need for second order corrections or dimension expansions, improving on existing direct multiple shooting approaches such as acados, ALTRO, GNMS, FATROP, and FDDP. The solutions of the LQR-shaped subproblems posed by our algorithm can be be parallelized to run in time logarithmic in the number of stages, states, and controls. Moreover, as our method avoids sequential rollouts of the nonlinear dynamics, it can run in parallel time per line search iteration. Therefore, this paper provides a practical, theoretically sound, and highly parallelizable (for example, with a GPU) method for solving nonlinear discrete-time optimal control problems.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

An open-source JAX implementation of this algorithm can be found on GitHub.

<!-- chunk {"id": "body-0005", "role": "body", "section": "II-A Unconstrained Discrete-Time Optimal Control Problems", "weight": 1.0} -->

Unconstrained discrete-time optimal control problems are optimization problems of the form $\begin{array}{ccr} Such optimization problems are ubiquitous in the fields of motion planning and controls.

<!-- chunk {"id": "body-0006", "role": "body", "section": "II-B Related Work", "weight": 1.0} -->

Naïf applications of generic optimization methods to unconstrained discrete-time optimal control problems would require $O{({N^{3}{({n + m})}^{3}})}$ operations for solving the linear systems posed at each iteration, where $N,n,m$ are respectively the number of stages, states, and controls of the problem. The first algorithm to improve on this was DDP, achieving complexity $O{({N{({n + m})}^{3}})}$. Its convergence properties were studied. iLQR can be seen as a version of DDP with coarser second derivative information (in particular, disregarding the Hessians of the dynamics), trading off local quadratic convergence for some added ease of implementation. Stagewise Newton exploits the fact that the computation of a Newton step on the "eliminated problem" (obtained by eliminating the variables $x_{i}$ in decreasing order of $i$ by plugging in the dynamics into the costs) can be reduced to solving an LQR problem, thereby achieving the same computational complexity as DDP.

<!-- chunk {"id": "body-0007", "role": "body", "section": "II-B Related Work", "weight": 1.0} -->

DDP, iLQR, and Stagewise Newton are all single shooting methods. This makes them hard to warm start, as the state trajectory cannot be chosen independently of the control trajectory. This can result in more iterations being required for these methods to converge, as well as higher likelihoods of convergence to undesired local optima. Moreover, they require that the dynamics be evaluated sequentially, making them harder to parallelize. introduces a multiple shooting equivalent of iLQR, called GNMS, as well as an algorithm that combines single and multiple shooting, called iLQR-GNMS, with similar computational complexity to the methods discussed above. There are no available convergence results for iLQR-GNMS; at a minimum, a line search procedure or a filter method would have to be added for these algorithms to achieve global convergence. introduces an alternative multiple shooting equivalent of iLQR, called FDDP, which adds a curvilinear line search that smoothly transitions between using the nonlinear dynamics in the forward pass for larger step sizes and using the affine dynamics for smaller step sizes. There are also no available convergence results for FDDP.

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-B Related Work", "weight": 1.0} -->

In both cases, as second order derivatives of the dynamics are not considered, there cannot be local quadratic convergence.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-B Related Work", "weight": 1.0} -->

Much work has also been done in handling discrete-time optimal control problems with stagewise constraints. ALTRO, FATROP, and acados are likely the most competitive open source software packages for this application at the time of writing. ALTRO handles constraints via the augmented Lagrangian method, while FATROP uses an interior point method and acados uses an SQP approach. ForcesNLP is likely the most competitive competing commercial software package at the time of writing, and also relies on an interior point method.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-B Related Work", "weight": 1.0} -->

At a high level and modulo technicalities, FATROP can be seen as a specialization of IPOPT with a linear system solver that handles LQR problems with extra stagewise affine constraints in time $O{({N{({n + m})}^{3}})}$. Inequality constraints are handled by eliminating some of the block-rows of the modified KKT system, as originally done. The modified KKT system will only have the extra stagewise affine constraints when the problem being solved has other stagewise equality constraints besides the dynamics. A similar algorithm that does not handle other general equality constraints had previously been presented. As compared to the specialization of FATROP to problems without stagewise equality constraints, our method has the advantage of not requiring second order corrections for fast local convergence. ForcesNLP also follows an interior point approach, but relies on a Cholesky factorizations instead of LQR decompositions for solving its linear systems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-B Related Work", "weight": 1.0} -->

On the other hand, the augmented Lagrangian technique employed by ALTRO yields linear systems that can be solved via the LQR algorithm, even in the presence of stagewise equality constraints. However, ALTRO has a slightly unorthodox way of doing multiple shooting: it modifies the dynamics $x_{n + 1} = {f_{n}{(x_{n},u_{n})}}$ into $x_{n + 1} = {{f_{n}{(x_{n},u_{n})}} + e_{n}}$ and adds the constraints $e_{n} = 0$. This makes it possible to independently warm start the state trajectory (while breaking the non-dynamic $e_{n} = 0$ constraint) while still using a single shooting algorithm. This approach has the disadvantage of substantially expanding the control dimension.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Related Work", "weight": 1.0} -->

Finally, the SQP approach followed by acados poses inequality-constrained quadratic subproblems, which are then solved by HPIPM, an efficient interior point QP solver that exploits the discrete-time optimal control problem structure. While it does not currently support stagewise equality constraints other than the dynamics, it could be extended to do so using a similar approach to. Moreover, due to not employing a globalization strategy, global convergence is not guaranteed. When the functions defining the problem are expensive to evaluate, SQP methods become time-competitive, as the higher number of linear system solves will be compensated by the lower number of evaluations of the nonlinear problem.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-C Contributions", "weight": 1.0} -->

This paper introduces the Primal-Dual iLQR algorithm, which consists of a specialization of the generic NPSQP algorithm to the case of unconstrained discrete-time optimal control problems.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-C Contributions", "weight": 1.0} -->

Our algorithm explores the sparsity structure of the Newton-KKT systems of unconstrained discrete-time optimal control problems, resulting in only $O{({N{({n + m})}^{3}})}$ operations for solving the linear systems posed at each iteration, where $N,n,m$ are respectively the number of stages, states, and controls of the problem.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-C Contributions", "weight": 1.0} -->

Moreover, we show that the primal-dual Newton-KKT systems we pose can be solved in $O{({{{\log{(N)}}{\log{(n)}}} + {\log{(m)}}})}$ parallel time complexity, using a minor variation of, and that the remaining parts of our method have constant parallel time complexity.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-C Contributions", "weight": 1.0} -->

Our algorithm improves on earlier direct multiple shooting methods, specifically by guaranteeing global convergence and not impeding local superlinear convergence (even without second order corrections), under the assumptions described.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A First-order Optimality Conditions and KKT Systems", "weight": 1.0} -->

Given a constrained optimization problem of the form for any local optimum $x$ meeting the standard linear independence constraint qualification (LICQ) constraints (i.e., for which the rows of $J{(c)}{(x)}$ are linearly independent), there exists a vector $\lambda$ (called the Lagrange/KKT multiplier) for which In other words, $(x,\lambda)$ is a critical point (but not necessarily a minimizer) of the Lagrangian function $\mathcal{L}{(x,\lambda)}$ defined as ${g{(x)}} + {\lambda^{T}c{(x)}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Sequential Quadratic Programming", "weight": 1.0} -->

The sequential quadratic programming (SQP) method for equality-constrained non-linear optimization problems consists of applying Newton's method for finding zeros of $\nabla\mathcal{L}$, typically in combination with a line search mechanism, in order to ensure global convergence.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Sequential Quadratic Programming", "weight": 1.0} -->

Below, let $A = {J{(c)}{(x)}}$, $l = {{\nabla_{x}\mathcal{L}}{(x,\lambda)}}$, and $d = {c{(x)}}$. Moreover, let $Q$ be a positive definite approximation of ${\nabla_{xx}^{2}\mathcal{L}}{(x,\lambda)}$. Such an approximation can be constructed, for example, via regularization. Alternatively, the terms involving ${\nabla_{xx}^{2}c}{(x)}$ can be dropped entirely, and $Q$ would consist purely of a positive definite approximation of ${\nabla_{xx}g}{(x)}$. The latter approach, of course, would result in local quadratic convergence being lost. For simplicity of notation, we henceforth drop the dependencies of these terms in $x$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Sequential Quadratic Programming", "weight": 1.0} -->

Each Newton step for finding a zero of $h{(z)}$ is obtained by solving ${h'{(z)}\Delta z} = {- {h{(z)}}}$. If $h = {\nabla\mathcal{L}}$, this corresponds to solving It can be shown (by a simple application of the first-order optimality conditions mentioned above) that $\Delta x$ is the solution of Similarly, it can also be shown that $\Delta\lambda$ is the corresponding Lagrange multiplier. As long as $Q$ is positive definite, this cost function is bounded from below. Depending on the sparsity pattern of this system, weaker requirements on $Q$ might also guarantee this.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Sequential Quadratic Programming", "weight": 1.0} -->

Convergence is established when $\Delta x$ and $\Delta\lambda$ are sufficiently close to $0$. The solution is feasible as long as $d = 0$, but convergence to locally infeasible solutions is possible.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-C Merit Functions", "weight": 1.0} -->

Merit functions offer a measure of progress towards the final solution and are typically used in combination with a line search procedure. Note that it would be inadequate to simply apply line search on the original objective, as SQP may (and often does) provide a search direction that locally increases that objective (usually trading that off for a reduction in the constraint violations). Filter methods, used, provide an alternative mechanism for measuring progress and determining whether the candidate step should be accepted, but this paper will not be using that approach.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Merit Functions", "weight": 1.0} -->

Note that suggests instead never decreasing $\rho$, and whenever an increase is required, increasing it to twice the minimal value required for making

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-D Line Search", "weight": 1.0} -->

Having computed $\Delta x$, $\Delta\lambda$, and $\rho$, we wish to compute a step size $\alpha$ that results in an acceptable decrease in our merit function $m_{\rho}$. Typically, this is achieved by performing a backtracking line search.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-D Line Search", "weight": 1.0} -->

This process is guaranteed to terminate as long as $g{(x)}$ and $c{(x)}$ are differentiable at $x$ and ${D{(m_{\rho};\begin{pmatrix} {\Delta x^{T}} & {\Delta\lambda^{T}} When ${\Delta x} = 0$ and $d = 0$ but ${\Delta\lambda} \neq 0$, we take a full step without conducting a line search.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-D Line Search", "weight": 1.0} -->

Note that NPSQP uses a slightly different line search method. Specifically, it enforces both Wolfe conditions, not only the Armijo condition.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Algorithm Derivation", "weight": 1.0} -->

In this section, we specialize the methods described above to the case of unconstrained discrete-time optimal control problems as needed.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Algorithm Derivation", "weight": 1.0} -->

The SQP constraint ${{Ap} + d} = 0$ becomes Note that if $x_{0}$ is warm started as $s_{0}$ then $\Delta x_{0}$ will always be $0$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Algorithm Derivation", "weight": 1.0} -->

If exact Hessians are used, the matrices $Q_{i}$ need not be positive semi-definite. However, we require that positive definite approximations be used instead. It would also be acceptable to only require positive semi-definiteness, as long as the $\nabla_{u_{i}u_{i}}^{2}$ components of the $Q_{i}$ be positive definite. However, this would require checking that ${\Delta x^{T}Q\Delta x} > 0$ at the end of the LQR solve. If this condition is not met, positive definite approximations would have to be used. Requiring positive definiteness in the first place avoids this complication.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Algorithm Derivation", "weight": 1.0} -->

In this case, the the SQP problem is a primal-dual LQR problem, which can be efficiently solved.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Algorithm Derivation", "weight": 1.0} -->

In order to ensure that the matrices $Q_{i}$ are positive semi-definite, it may be helpful to maintain regularization parameters $\mu_{i}$ and always use $Q_{i} + {\mu_{i}I}$ instead of $Q_{i}$. If, during the LQR process, we detect that $Q_{i} + {\mu_{i}I}$ is not positive definite, $\mu_{i}$ can be updated by multiplying it by an updated factor $r > 1$. When increasing $\mu_{i}$ is not required, we can instead update $\mu_{i}$ by dividing it by $r$. Minimum and maximum regularization parameters may also be established, to allow, when possible, $\mu_{i}$ to eventually be set to $0$ if $Q_{i}$ is consistently positive definite, as well as to prevent exploring unreasonably high regularization parameters.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Algorithm Derivation", "weight": 1.0} -->

Another option would be to regularize the $Q_{i}$ by performing an explicit eigenvalue decomposition and removing negative (or non-positive, when positive definiteness is required) eigenvalues.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Sequential Primal LQR Overview", "weight": 1.0} -->

In this section, we will go over the conventional sequential algorithm for solving primal LQR problems. In the interest of not deviating from standard notation, variable names may henceforth not match earlier parts of this paper. A linear-quadratic regulator (LQR) problem is an unconstrained discrete-time optimal control problem where the costs are quadratic functions and the dynamics are affine functions. Specifically, they are optimization problems of the form Note that the $R_{i}$ are required to be positive definite, and that the $Q_{i} - {M_{i}R_{i}^{- 1}M_{i}^{T}}$ are required to be positive semi-definite, otherwise a minimum may not exist.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Sequential Primal LQR Overview", "weight": 1.0} -->

The conventional method for solving LQR problems sequentially relies on the fact that the optimal cost-to-go functions are quadratic on the state at the corresponding stage. Therefore, such functions ${V_{i}{(x_{i})}} = {{0.5x_{i}^{T}P_{i}x_{i}} + {p_{i}^{T}x_{i}} + z_{i}}$ can be computed in decreasing order of stage (i.e. $i$). Moreover, the optimal controls to be applied at each stage can be shown to be affine functions of the state at the corresponding stage, i.e. $u_{i} = {{K_{i}x_{i}} + k_{i}}$. The $K_{i}$ and $k_{i}$ can be computed as part of the same backward pass as the $P_{i}$ and $p_{i}$. Note that the constants $z_{i}$ do not need to be computed.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Associative Scans Overview", "weight": 1.0} -->

Associative scans are a common parallelization mechanism used in functional programming, first introduced. They were used in to derive a simple method for solving (primal) LQR problems in $O{({{\log{(m)}} + {{\log{(N)}}{\log{(n)}}}})}$ parallel time, where $N,n,m$ are respectively the number of stages, states, and controls.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Parallel Primal LQR Overview", "weight": 1.0} -->

Finally, we wish to compute the $x_{i},u_{i}$ from the $K_{i},k_{i}$. Note that the sequential LQR forward pass has $O{(T)}$ parallel time complexity. However, as done, we can reduce the computation of the $x_{i}$ to a sequential composition of affine functions, which can also be parallelized with an associative scan. This will be described in the next section.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Parallel Primal LQR Overview", "weight": 1.0} -->

Once these affine functions have been composed, they can be independently applied to $x_{0}$ to recover all the $x_{i}$. The $u_{i}$ can then be computed in $O{}$ parallel time by independently evaluating $u_{i} = {{K_{i}x_{i}} + k_{i}}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Dual LQR Backward Pass", "weight": 1.0} -->

Next, we show how to compute the multipliers $\lambda$, i.e. how to solve the dual part of the LQR problem. Note that primal-dual LQR problems can be solved in a single Newton step, independently of the starting values of $x,\lambda$. Therefore, starting with ${x,\lambda} = 0$, the ${\Delta x},{\Delta\lambda}$ from the Newton-KKT system correspond to the optimal $x,\lambda$. Having determined $x$ using one of the primal LQR algorithms, determining $\lambda$ can be done by specializing ${{{\nabla_{xx}\mathcal{L}}{}x} + {J{(c)}{}^{T}\lambda}} = {- {{\nabla_{x}\mathcal{L}}{}}}$ (i.e. the first block-row of the Newton-KKT system).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Dual LQR Backward Pass", "weight": 1.0} -->

Note that we discard the rows where $J{(c)}{(x)}^{T}$ contains any of the $B_{i}$ (as they are not useful for computing the $\lambda_{i}$), and keep the rows where it contains any of the $A_{i}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Dual LQR Backward Pass", "weight": 1.0} -->

Specifically, for $i \in {\{ 0,\ldots,{N - 1}\}}$, it holds that Note that these equations can be used to recursively compute the $\lambda_{i}$, in decreasing order of $i$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Dual LQR Backward Pass", "weight": 1.0} -->

Moreover, note that these $\lambda_{i}$ also satisfy the block-rows of ${{{\nabla_{xx}\mathcal{L}}{}x} + {J{(c)}{}^{T}\lambda}} = {- {{\nabla_{x}\mathcal{L}}{}}}$ that we discarded, as a solution to the full Newton-KKT system must exist due to the LICQ conditions being satisfied, and as these $\lambda_{i}$ are the *only* solution that satisfies the block-rows we did not discard.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Parallel Dual LQR", "weight": 1.0} -->

While the dual LQR backward pass described in section IX can be parallelized with a reverse associative scan (in a similar fashion to section VIII), we can actually compute the multipliers $\lambda$ in $O{}$ parallel time.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Parallel Dual LQR", "weight": 1.0} -->

The multiplier $\lambda_{0}$ is also the Lagrange/KKT multiplier of By the first order optimality conditions, the gradient of the corresponding Lagrangian Similarly, each multiplier $\lambda_{i}$ is also the Lagrange/KKT multiplier of The corresponding Lagrangian is Similarly, the first order optimality conditions imply Finally, note that all the $\lambda_{i}$ can be evaluated independently, so a backward pass is not required using these formulas. This method of computing the multipliers also has the advantage of involving fewer computations and being more numerically stable.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

Below, we include an example run of our algorithm on on a quad-pendulum problem, which we got from GitHub (${{google}/t}rajax$) and modified to treat constraints as high-penalty costs (using a gain of $100$). We also increased the final state cost gains on the positions to $1000$. This seems to be the problem used. Note that we solve a single primal-dual LQR problem for each iteration, and have to evaluate the user model once per line search step. A JAX implementation of our algorithm takes 46ms to finish solving this problem (on the CPU of an M2 MacBook Air). Below, you can find a visual description of the problem and solution, as well as solver logs.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper introduces a new algorithm for solving unconstrained discrete-time optimal control problems, called Primal-Dual iLQR.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This framework can easily be extended to handle constrained problems. Ideally, an interior point method would be used to handle general inequality constraints. It would also be possible to handle both general equality and inequality constraints with an augmented Lagrangian method, although local superlinear convergence would be lost. In both cases, the LQR shape of the posed subproblems can be preserved. Preserving superlinar local convergence in the presence of general equality constraints would require employing a linear equality-constrained LQR subproblem solver. Using SQP to handle general nonlinear constraints would yield Newton-KKT systems that are fundamentally different from the ones we consider, and would therefore require substantial changes to our method (including adding substantially slower iterative subproblem solves).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our method is substantially easier to warm start as compared to single-shooting methods such as DDP, iLQR, or Stagewise Newton, as it treats both state and control trajectories as free variables in the optimization problem (without incurring extra computational costs); this allows them to be independently seeded, even in dynamically infeasible ways.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The proposed algorithm is globally convergent and does not impede superlinear local convergence, without requiring second order corrections to be applied.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Finally, solving the subproblems posed by our method can be parallelized to run in time logarithmic in the number of stages, states, and controls. Moreover, as our method never performs nonlinear dynamics rollouts, it allows that the evaluation of the dynamics and derivatives be computed in parallel, resulting in $O{}$ parallel time per line search iteration.
