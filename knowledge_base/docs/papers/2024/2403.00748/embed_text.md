<!-- arxiv-full-text:v1 {"arxiv_id": "2403.00748", "source": "arxiv-html"} -->

## Introduction

### II-A Unconstrained Discrete-Time Optimal Control Problems

Unconstrained discrete-time optimal control problems are optimization problems of the form $\begin{array}{ccr} Such optimization problems are ubiquitous in the fields of motion planning and controls.

### II-B Related Work

Naïf applications of generic optimization methods to unconstrained discrete-time optimal control problems would require $O{({N^{3}{({n + m})}^{3}})}$ operations for solving the linear systems posed at each iteration, where $N,n,m$ are respectively the number of stages, states, and controls of the problem. The first algorithm to improve on this was DDP, achieving complexity $O{({N{({n + m})}^{3}})}$. Its convergence properties were studied . iLQR can be seen as a version of DDP with coarser second derivative information (in particular, disregarding the Hessians of the dynamics), trading off local quadratic convergence for some added ease of implementation. Stagewise Newton exploits the fact that the computation of a Newton step on the "eliminated problem" (obtained by eliminating the variables $x_{i}$ in decreasing order of $i$ by plugging in the dynamics into the costs) can be reduced to solving an LQR problem, thereby achieving the same computational complexity as DDP.

DDP, iLQR, and Stagewise Newton are all single shooting methods. This makes them hard to warm start, as the state trajectory cannot be chosen independently of the control trajectory. This can result in more iterations being required for these methods to converge, as well as higher likelihoods of convergence to undesired local optima. Moreover, they require that the dynamics be evaluated sequentially, making them harder to parallelize. introduces a multiple shooting equivalent of iLQR, called GNMS, as well as an algorithm that combines single and multiple shooting, called iLQR-GNMS, with similar computational complexity to the methods discussed above. There are no available convergence results for iLQR-GNMS; at a minimum, a line search procedure or a filter method would have to be added for these algorithms to achieve global convergence. introduces an alternative multiple shooting equivalent of iLQR, called FDDP, which adds a curvilinear line search that smoothly transitions between using the nonlinear dynamics in the forward pass for larger step sizes and using the affine dynamics for smaller step sizes. There are also no available convergence results for FDDP. In both cases, as second order derivatives of the dynamics are not considered, there cannot be local quadratic convergence.

Much work has also been done in handling discrete-time optimal control problems with stagewise constraints. ALTRO, FATROP, and acados are likely the most competitive open source software packages for this application at the time of writing. ALTRO handles constraints via the augmented Lagrangian method, while FATROP uses an interior point method and acados uses an SQP approach. ForcesNLP is likely the most competitive competing commercial software package at the time of writing, and also relies on an interior point method.

At a high level and modulo technicalities, FATROP can be seen as a specialization of IPOPT with a linear system solver that handles LQR problems with extra stagewise affine constraints in time $O{({N{({n + m})}^{3}})}$. Inequality constraints are handled by eliminating some of the block-rows of the modified KKT system, as originally done . The modified KKT system will only have the extra stagewise affine constraints when the problem being solved has other stagewise equality constraints besides the dynamics. A similar algorithm that does not handle other general equality constraints had previously been presented . As compared to the specialization of FATROP to problems without stagewise equality constraints, our method has the advantage of not requiring second order corrections for fast local convergence. ForcesNLP also follows an interior point approach, but relies on a Cholesky factorizations instead of LQR decompositions for solving its linear systems.

On the other hand, the augmented Lagrangian technique employed by ALTRO yields linear systems that can be solved via the LQR algorithm, even in the presence of stagewise equality constraints. However, ALTRO has a slightly unorthodox way of doing multiple shooting: it modifies the dynamics $x_{n + 1} = {f_{n}{(x_{n},u_{n})}}$ into $x_{n + 1} = {{f_{n}{(x_{n},u_{n})}} + e_{n}}$ and adds the constraints $e_{n} = 0$. This makes it possible to independently warm start the state trajectory (while breaking the non-dynamic $e_{n} = 0$ constraint) while still using a single shooting algorithm. This approach has the disadvantage of substantially expanding the control dimension.

Finally, the SQP approach followed by acados poses inequality-constrained quadratic subproblems, which are then solved by HPIPM, an efficient interior point QP solver that exploits the discrete-time optimal control problem structure. While it does not currently support stagewise equality constraints other than the dynamics, it could be extended to do so using a similar approach to. Moreover, due to not employing a globalization strategy, global convergence is not guaranteed. When the functions defining the problem are expensive to evaluate, SQP methods become time-competitive, as the higher number of linear system solves will be compensated by the lower number of evaluations of the nonlinear problem.

### II-C Contributions

This paper introduces the Primal-Dual iLQR algorithm, which consists of a specialization of the generic NPSQP algorithm to the case of unconstrained discrete-time optimal control problems.

Our algorithm explores the sparsity structure of the Newton-KKT systems of unconstrained discrete-time optimal control problems, resulting in only $O{({N{({n + m})}^{3}})}$ operations for solving the linear systems posed at each iteration, where $N,n,m$ are respectively the number of stages, states, and controls of the problem.

Moreover, we show that the primal-dual Newton-KKT systems we pose can be solved in $O{({{{\log{(N)}}{\log{(n)}}} + {\log{(m)}}})}$ parallel time complexity, using a minor variation of, and that the remaining parts of our method have constant parallel time complexity.

Our algorithm improves on earlier direct multiple shooting methods, specifically by guaranteeing global convergence and not impeding local superlinear convergence (even without second order corrections), under the assumptions described .

## General Optimization Background

### III-A First-order Optimality Conditions and KKT Systems

Given a constrained optimization problem of the form for any local optimum $x$ meeting the standard linear independence constraint qualification (LICQ) constraints (i.e., for which the rows of $J{(c)}{(x)}$ are linearly independent), there exists a vector $\lambda$ (called the Lagrange/KKT multiplier) for which In other words, $(x,\lambda)$ is a critical point (but not necessarily a minimizer) of the Lagrangian function $\mathcal{L}{(x,\lambda)}$ defined as ${g{(x)}} + {\lambda^{T}c{(x)}}$.

### III-B Sequential Quadratic Programming

The sequential quadratic programming (SQP) method for equality-constrained non-linear optimization problems consists of applying Newton's method for finding zeros of $\nabla\mathcal{L}$, typically in combination with a line search mechanism, in order to ensure global convergence.

Below, let $A = {J{(c)}{(x)}}$, $l = {{\nabla_{x}\mathcal{L}}{(x,\lambda)}}$, and $d = {c{(x)}}$. Moreover, let $Q$ be a positive definite approximation of ${\nabla_{xx}^{2}\mathcal{L}}{(x,\lambda)}$. Such an approximation can be constructed, for example, via regularization. Alternatively, the terms involving ${\nabla_{xx}^{2}c}{(x)}$ can be dropped entirely, and $Q$ would consist purely of a positive definite approximation of ${\nabla_{xx}g}{(x)}$. The latter approach, of course, would result in local quadratic convergence being lost. For simplicity of notation, we henceforth drop the dependencies of these terms in $x$.

Each Newton step for finding a zero of $h{(z)}$ is obtained by solving ${h'{(z)}\Delta z} = {- {h{(z)}}}$. If $h = {\nabla\mathcal{L}}$, this corresponds to solving It can be shown (by a simple application of the first-order optimality conditions mentioned above) that $\Delta x$ is the solution of Similarly, it can also be shown that $\Delta\lambda$ is the corresponding Lagrange multiplier. As long as $Q$ is positive definite, this cost function is bounded from below. Depending on the sparsity pattern of this system, weaker requirements on $Q$ might also guarantee this.

Convergence is established when $\Delta x$ and $\Delta\lambda$ are sufficiently close to $0$. The solution is feasible as long as $d = 0$, but convergence to locally infeasible solutions is possible.

### III-C Merit Functions

Merit functions offer a measure of progress towards the final solution and are typically used in combination with a line search procedure. Note that it would be inadequate to simply apply line search on the original objective, as SQP may (and often does) provide a search direction that locally increases that objective (usually trading that off for a reduction in the constraint violations). Filter methods, used , provide an alternative mechanism for measuring progress and determining whether the candidate step should be accepted, but this paper will not be using that approach.

Given a penalty parameter $\rho > 0$, we define the $\ell_{2}$ merit function Below, $\Delta x$ and $\Delta\lambda$ correspond to SQP step defined above; moreover, $D{(\cdot; \cdot)}$ is used to represent the directional derivative operator. Noting that ${{\nabla_{\lambda}\mathcal{L}}{(x,\lambda)}} = {c{(x)}} = d$, it holds that | | | $D{(m_{\rho};\begin{pmatrix} | | \(8\) | | | | $= {\Delta x^{T}{\nabla_{x}m_{\rho}}{(x,\lambda)}}$ | | | | | | $= {{\Delta x^{T}{\nabla_{x}\mathcal{L}}{(x,\lambda)}} + {\rho\Delta x^{T}J{(c)}{(x)}^{T}c{(x)}}}$ | | | | | | $= {{{- {\Delta x^{T}Q\Delta x}} - {\Delta x^{T}A^{T}\Delta\lambda}} + {\rho\Delta x^{T}A^{T}d}}$ | | | | | | $= {{{- {\Delta x^{T}Q\Delta x}} + {{\nabla_{\lambda}\mathcal{L}}{(x,\lambda)}^{T}\Delta\lambda}} - {\rho{\nabla_{\lambda}\mathcal{L}}{(x,\lambda)}^{T}d}}$ | | | | | | $= {{{- {\Delta x^{T}Q\Delta x}} + {d^{T}\Delta\lambda}} - {\rho{\parallel d\parallel}^{2}}}$ | | | | | | $D{(m_{\rho};\begin{pmatrix} | | \(10\) | | | | {\Delta x^{T}} & {\Delta\lambda^{T}} | | | | | $=$ | ${{{- {\Delta x^{T}Q\Delta x}} + {2d^{T}\Delta\lambda}} - {\rho{\parallel d\parallel}^{2}}}.$ | | | Note that, as $Q$ is positive definite, ${- {\Delta x^{T}Q\Delta x}} < 0$ unless ${\Delta x} = 0$. When $d$ is not acceptably close to $0$, we suggest taking which ensures that ${D{(m_{\rho};\begin{pmatrix} {\Delta x^{T}} & {\Delta\lambda^{T}} \end{pmatrix})}} < 0$ (due to the Cauchy-Schwarz inequality). Otherwise, we suggest taking $\rho = 0.01$.

Note that suggests instead never decreasing $\rho$, and whenever an increase is required, increasing it to twice the minimal value required for making

### III-D Line Search

Having computed $\Delta x$, $\Delta\lambda$, and $\rho$, we wish to compute a step size $\alpha$ that results in an acceptable decrease in our merit function $m_{\rho}$. Typically, this is achieved by performing a backtracking line search. $\alpha$ starts as $1$ and decreases by a constant multiplicative factor (often $0.5$) every iteration, until | | | ${m_{\rho}{({x + {\alpha\Delta x}},{\lambda + {\alpha\Delta\lambda}})}} <$ | | \(13\) | | | | ${m_{\rho}{(x,\lambda)}} + {k\alpha D{(m_{\rho};\begin{pmatrix} | | | | | | {\Delta x^{T}} & {\Delta\lambda^{T}} | | | is satisfied (where $k \in {}$ is called the Armijo factor; typically, $10^{- 4}$ is used). This is called the Armijo condition. This process is guaranteed to terminate as long as $g{(x)}$ and $c{(x)}$ are differentiable at $x$ and ${D{(m_{\rho};\begin{pmatrix} {\Delta x^{T}} & {\Delta\lambda^{T}} When ${\Delta x} = 0$ and $d = 0$ but ${\Delta\lambda} \neq 0$, we take a full step without conducting a line search.

Note that NPSQP uses a slightly different line search method. Specifically, it enforces both Wolfe conditions, not only the Armijo condition.

## Algorithm Derivation

In this section, we specialize the methods described above to the case of unconstrained discrete-time optimal control problems as needed.

The corresponding Lagrange/KKT multipliers are $\lambda_{0},\ldots,\lambda_{N}$ respectively. Letting $x = {(x_{0},u_{0},\ldots,x_{N - 1},u_{N - 1},x_{N})}$, $A_{i} = {J_{x}{(f_{i})}{(x_{i},u_{i})}}$ and $B_{i} = {J_{u}{(f_{i})}{(x_{i},u_{i})}}$, | | | 0 & 0 & 0 & 0 & \ddots & \ddots & \ddots & 0 & 0 \\ | | | Note that the LICQ conditions are always met for matrices of this form, due to the presence of the $- I$ blocks, independently of the $A_{i}$ and $B_{i}$.

The SQP constraint ${{Ap} + d} = 0$ becomes Note that if $x_{0}$ is warm started as $s_{0}$ then $\Delta x_{0}$ will always be $0$.

Similarly, noting that The SQP cost ${\frac{1}{2}p^{T}Qp} + {l^{T}p}$ is simply ${\sum\limits_{i = 0}^{N}{\frac{1}{2}p_{i}^{T}Q_{i}p_{i}}} + {l_{i}^{T}p_{i}}$, where $p_{i} = {({\Delta x_{i}},{\Delta u_{i}})}$ for $i \in {\{ 0,\ldots,{N - 1}\}}$ and $p_{N} = {\Delta x_{N}}$.

If exact Hessians are used, the matrices $Q_{i}$ need not be positive semi-definite. However, we require that positive definite approximations be used instead. It would also be acceptable to only require positive semi-definiteness, as long as the $\nabla_{u_{i}u_{i}}^{2}$ components of the $Q_{i}$ be positive definite. However, this would require checking that ${\Delta x^{T}Q\Delta x} > 0$ at the end of the LQR solve. If this condition is not met, positive definite approximations would have to be used. Requiring positive definiteness in the first place avoids this complication.

In this case, the the SQP problem is a primal-dual LQR problem, which can be efficiently solved.

In order to ensure that the matrices $Q_{i}$ are positive semi-definite, it may be helpful to maintain regularization parameters $\mu_{i}$ and always use $Q_{i} + {\mu_{i}I}$ instead of $Q_{i}$. If, during the LQR process, we detect that $Q_{i} + {\mu_{i}I}$ is not positive definite, $\mu_{i}$ can be updated by multiplying it by an updated factor $r > 1$. When increasing $\mu_{i}$ is not required, we can instead update $\mu_{i}$ by dividing it by $r$. Minimum and maximum regularization parameters may also be established, to allow, when possible, $\mu_{i}$ to eventually be set to $0$ if $Q_{i}$ is consistently positive definite, as well as to prevent exploring unreasonably high regularization parameters. Another option would be to regularize the $Q_{i}$ by performing an explicit eigenvalue decomposition and removing negative (or non-positive, when positive definiteness is required) eigenvalues.

## Sequential Primal LQR Overview

In this section, we will go over the conventional sequential algorithm for solving primal LQR problems. In the interest of not deviating from standard notation, variable names may henceforth not match earlier parts of this paper. A linear-quadratic regulator (LQR) problem is an unconstrained discrete-time optimal control problem where the costs are quadratic functions and the dynamics are affine functions. Specifically, they are optimization problems of the form Note that the $R_{i}$ are required to be positive definite, and that the $Q_{i} - {M_{i}R_{i}^{- 1}M_{i}^{T}}$ are required to be positive semi-definite, otherwise a minimum may not exist.

The conventional method for solving LQR problems sequentially relies on the fact that the optimal cost-to-go functions are quadratic on the state at the corresponding stage. Therefore, such functions ${V_{i}{(x_{i})}} = {{0.5x_{i}^{T}P_{i}x_{i}} + {p_{i}^{T}x_{i}} + z_{i}}$ can be computed in decreasing order of stage (i.e. $i$). Moreover, the optimal controls to be applied at each stage can be shown to be affine functions of the state at the corresponding stage, i.e. $u_{i} = {{K_{i}x_{i}} + k_{i}}$. The $K_{i}$ and $k_{i}$ can be computed as part of the same backward pass as the $P_{i}$ and $p_{i}$. Note that the constants $z_{i}$ do not need to be computed. Initializing $P_{N} = Q_{N}$ and $p_{N} = q_{N}$, and introducing $G_{i},H_{i},h_{i}$ as convenient auxiliary variables, the following recursion rules can be used: Once the $K_{i},k_{i}$ have been computed, the $u_{i}$ can be computed in increasing order of $i$, by alternating evaluations of $u_{i} = {{K_{i}x_{i}} + k_{i}}$ and $x_{i + 1} = {{A_{i}x_{i}} + {B_{i}u_{i}} + c_{i}}$. This is usually called the LQR forward pass.

## Associative Scans Overview

Associative scans are a common parallelization mechanism used in functional programming, first introduced . They were used in to derive a simple method for solving (primal) LQR problems in $O{({{\log{(m)}} + {{\log{(N)}}{\log{(n)}}}})}$ parallel time, where $N,n,m$ are respectively the number of stages, states, and controls.

Given a set $\mathcal{X}$, a function $f:{{\mathcal{X} \times \mathcal{X}}\rightarrow\mathcal{X}}$ is said to be associative if ${{{\forall a},b,c} \in \mathcal{X}},{{f{({f{(a,b)}},c)}} = {f{(a,{f{(b,c)}})}}}$. The forward associative scan operation $S_{f}{(x_{1},\ldots,x_{n};f)}$ can be recursively defined by ${S_{f}{(x_{1};f)}} = x_{1}$ and ${S_{f}{(x_{1},\ldots,x_{i + 1};f)}} = {(y_{1},\ldots,y_{i},{f{(y_{i},x_{i + 1})}})}$, where ${y_{1},\ldots,y_{i}} = {S_{f}{(x_{1},\ldots,x_{i};f)}}$. Similarly, the reverse associative scan operation $S_{r}{(x_{1},\ldots,x_{n};f)}$ can be recursively defined by ${S_{r}{(x_{1};f)}} = x_{1}$ and ${S_{r}{(x_{1},\ldots,x_{i + 1};f)}} = {({f{(x_{1},y_{2})}},y_{2},\ldots,y_{i + 1})}$, where ${y_{2},\ldots,y_{i + 1}} = {S_{r}{(x_{2},\ldots,x_{i + 1};f)}}$. provides a method for performing associative scans of $N$ elements in parallel time $O{({\log{(N)}})}$.

## Parallel Primal LQR Overview

A parallel algorithm for solving these problems was presented, although we require some minor changes due to a difference in problem formulations. In order to describe this method, we need to introduce an important definition. An interval value function $V_{i\rightarrow j}{(x_{i},x_{j})}$ maps states $x_{i},x_{j}$ at stages $i,j$ to the minimum possible cost incurred in stages $i,\ldots,{j - 1}$ among all trajectories that start at state $x_{i}$ in stage $i$ and end at state $x_{j}$ in stage $j$ ($\infty$ if no such trajectory exists). The key insight of is that the optimal interval value functions can be represented as | | $V_{i\rightarrow j}{(x_{i},x_{j})} = \max\limits_{\lambda}\left(\frac{1}{2}x_{i}^{T}P_{i\rightarrow j}x_{i} + p_{i\rightarrow j}^{T}x_{i} \right.$ | | \(24\) | | | $\left. - \frac{1}{2}\lambda^{T}C_{i\rightarrow j}\lambda - \lambda^{T}\left(x_{j} - A_{i\rightarrow j}x_{i} - c_{i\rightarrow j} \right) \right).$ | | | Initializing, for $i \in {\{ 0,\ldots,{N - 1}\}}$, $V_{i\rightarrow{i + 1}}$ with and initializing $V_{N\rightarrow{N + 1}}$ with the following combination rules can be applied to compute $V_{i\rightarrow k}$ from $V_{i\rightarrow j}$ and $V_{j\rightarrow k}$: | | $P_{i\rightarrow k}$ | ${= {{A_{i\rightarrow j}^{T}\left({I + {P_{j\rightarrow k}C_{i\rightarrow j}}} \right)^{- 1}P_{j\rightarrow k}A_{i\rightarrow j}} + P_{i\rightarrow j}}},$ | | \(27\) | | | $p_{i\rightarrow k}$ | $= {A_{i\rightarrow j}^{T}\left({I + {P_{j\rightarrow k}C_{i\rightarrow j}}} \right)^{- 1}\left({p_{j\rightarrow k} + {J_{j\rightarrow k}c_{i\rightarrow j}}} \right)}$ | | | | | $A_{i\rightarrow k}$ | ${= {A_{j\rightarrow k}\left({I + {C_{i\rightarrow j}P_{j\rightarrow k}}} \right)^{- 1}A_{i\rightarrow j}}},$ | | | | | $C_{i\rightarrow k}$ | ${= {{A_{j\rightarrow k}\left({I + {C_{i\rightarrow j}P_{j\rightarrow k}}} \right)^{- 1}C_{i\rightarrow j}A_{j\rightarrow k}^{T}} + C_{j\rightarrow k}}},$ | | | | | $c_{i\rightarrow k}$ | $= {A_{j\rightarrow k}\left({I + {C_{i\rightarrow j}P_{j\rightarrow k}}} \right)^{- 1}\left({c_{i\rightarrow j} - {C_{i\rightarrow j}p_{j\rightarrow k}}} \right)}$ | | | A reverse associative scan can be used to compute the $P_{i\rightarrow{N + 1}},p_{i\rightarrow{N + 1}}$ (i.e. the $P_{i},p_{i}$ from section V), which in turn can be used to compute the $K_{i},k_{i}$ in $O{}$ parallel time.

Finally, we wish to compute the $x_{i},u_{i}$ from the $K_{i},k_{i}$. Note that the sequential LQR forward pass has $O{(T)}$ parallel time complexity. However, as done , we can reduce the computation of the $x_{i}$ to a sequential composition of affine functions, which can also be parallelized with an associative scan. This will be described in the next section.

Once these affine functions have been composed, they can be independently applied to $x_{0}$ to recover all the $x_{i}$. The $u_{i}$ can then be computed in $O{}$ parallel time by independently evaluating $u_{i} = {{K_{i}x_{i}} + k_{i}}$.

## Composing Affine Functions with Associative Scans

In this section, we describe an $O{({\log{(N)}})}$ parallel time algorithm for composing $N$ affine functions ${F_{i}{(x)}} = {{M_{i}x_{i}} + m_{i}}$, as done .

Letting $\mathcal{X} = {{\mathbb{R}}^{n} \times {\mathbb{R}}^{n \times n}}$ and letting $f:{\mathcal{X}\rightarrow\mathcal{X}}$ be defined by ${f{({(a,B)},{(c,D)})}} = {({{Da} + c},{DB})}$, we claim that $f$ is associative. This is simple to verify: Moreover, note that $f$ is the affine function composition operator, as ${{D{({{Bx} + a})}} + c} = {{{({DB})}x} + {({{Da} + c})}}$.

## Dual LQR Backward Pass

Next, we show how to compute the multipliers $\lambda$, i.e. how to solve the dual part of the LQR problem. Note that primal-dual LQR problems can be solved in a single Newton step, independently of the starting values of $x,\lambda$. Therefore, starting with ${x,\lambda} = 0$, the ${\Delta x},{\Delta\lambda}$ from the Newton-KKT system correspond to the optimal $x,\lambda$. Having determined $x$ using one of the primal LQR algorithms, determining $\lambda$ can be done by specializing ${{{\nabla_{xx}\mathcal{L}}{}x} + {J{(c)}{}^{T}\lambda}} = {- {{\nabla_{x}\mathcal{L}}{}}}$ (i.e. the first block-row of the Newton-KKT system). Note that we discard the rows where $J{(c)}{(x)}^{T}$ contains any of the $B_{i}$ (as they are not useful for computing the $\lambda_{i}$), and keep the rows where it contains any of the $A_{i}$.

Specifically, for $i \in {\{ 0,\ldots,{N - 1}\}}$, it holds that Note that these equations can be used to recursively compute the $\lambda_{i}$, in decreasing order of $i$.

Moreover, note that these $\lambda_{i}$ also satisfy the block-rows of ${{{\nabla_{xx}\mathcal{L}}{}x} + {J{(c)}{}^{T}\lambda}} = {- {{\nabla_{x}\mathcal{L}}{}}}$ that we discarded, as a solution to the full Newton-KKT system must exist due to the LICQ conditions being satisfied, and as these $\lambda_{i}$ are the *only* solution that satisfies the block-rows we did not discard.

## Parallel Dual LQR

While the dual LQR backward pass described in section IX can be parallelized with a reverse associative scan (in a similar fashion to section VIII), we can actually compute the multipliers $\lambda$ in $O{}$ parallel time.

The multiplier $\lambda_{0}$ is also the Lagrange/KKT multiplier of By the first order optimality conditions, the gradient of the corresponding Lagrangian Similarly, each multiplier $\lambda_{i}$ is also the Lagrange/KKT multiplier of The corresponding Lagrangian is Similarly, the first order optimality conditions imply Finally, note that all the $\lambda_{i}$ can be evaluated independently, so a backward pass is not required using these formulas. This method of computing the multipliers also has the advantage of involving fewer computations and being more numerically stable.

## Benchmarks

Figure 1: The solution of the quad-pendulum problem.

Below, we include an example run of our algorithm on on a quad-pendulum problem, which we got from GitHub (${{google}/t}rajax$) and modified to treat constraints as high-penalty costs (using a gain of $100$). We also increased the final state cost gains on the positions to $1000$. This seems to be the problem used . Note that we solve a single primal-dual LQR problem for each iteration, and have to evaluate the user model once per line search step. A JAX implementation of our algorithm takes 46ms to finish solving this problem (on the CPU of an M2 MacBook Air). Below, you can find a visual description of the problem and solution, as well as solver logs.

## Conclusion

This paper introduces a new algorithm for solving unconstrained discrete-time optimal control problems, called Primal-Dual iLQR.

This framework can easily be extended to handle constrained problems. Ideally, an interior point method would be used to handle general inequality constraints. It would also be possible to handle both general equality and inequality constraints with an augmented Lagrangian method, although local superlinear convergence would be lost. In both cases, the LQR shape of the posed subproblems can be preserved. Preserving superlinar local convergence in the presence of general equality constraints would require employing a linear equality-constrained LQR subproblem solver. Using SQP to handle general nonlinear constraints would yield Newton-KKT systems that are fundamentally different from the ones we consider, and would therefore require substantial changes to our method (including adding substantially slower iterative subproblem solves).

Our method is substantially easier to warm start as compared to single-shooting methods such as DDP, iLQR, or Stagewise Newton, as it treats both state and control trajectories as free variables in the optimization problem (without incurring extra computational costs); this allows them to be independently seeded, even in dynamically infeasible ways.

The proposed algorithm is globally convergent and does not impede superlinear local convergence, without requiring second order corrections to be applied.

Finally, solving the subproblems posed by our method can be parallelized to run in time logarithmic in the number of stages, states, and controls. Moreover, as our method never performs nonlinear dynamics rollouts, it allows that the evaluation of the dynamics and derivatives be computed in parallel, resulting in $O{}$ parallel time per line search iteration.
