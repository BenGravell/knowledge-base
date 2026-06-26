## Abstract

In this paper we introduce *disciplined convex-concave programming* (DCCP), which combines the ideas of disciplined convex programming (DCP) with convex-concave programming (CCP). Convex-concave programming is an organized heuristic for solving nonconvex problems that involve objective and constraint functions that are a sum of a convex and a concave term. DCP is a structured way to define convex optimization problems, based on a family of basic convex and concave functions and a few rules for combining them. Problems expressed using DCP can be automatically converted to standard form and solved by a generic solver; widely used implementations include YALMIP, CVX, CVXPY, and Convex.jl. In this paper we propose a framework that combines the two ideas, and includes two improvements over previously published work on convex-concave programming, specifically the handling of domains of the functions, and the issue of nondifferentiability on the boundary of the domains. We describe a Python implementation called DCCP, which extends CVXPY, and give examples.

## Disciplined convex-concave programming

### Difference of convex programming

Difference of convex (DC) programming problems have the form where $x \in \text{R}^{n}$ is the optimization variable, and the functions $f_{i}:{\text{R}^{n}\rightarrow\text{R}}$ and $g_{i}:{\text{R}^{n}\rightarrow\text{R}}$ for $i = {0,\ldots,m}$ are convex. The DC problem can also include equality constraints of the form ${p_{i}{(x)}} = {q_{i}{(x)}}$, where $p_{i}$ and $q_{i}$ are convex; we simply express these as the pair of inequality constraints which have the difference of convex form. When the functions $g_{i}$ are all affine, the problem is a convex optimization problem, and easily solved.

The broad class of DC functions includes all $C^{2}$ functions, so the DC problem is very general. A special case is Boolean linear programs, which can represent many problems, such as the traveling salesman problem, that are widely believed to be hard to solve. DC programs arise in many applications in fields such as signal processing, machine learning, computer vision, and statistics \[THA^+^14\].

DC problems can be solved globally by methods such as branch and bound \[, \], which can be slow in practice. Good overviews of solving DC programs globally can be found in \[, \] and the references therein. A locally optimal (approximate) solution can be found instead through the many techniques of general nonlinear optimization.

The convex-concave procedure (CCP) is another heuristic algorithm for finding a local optimum of, which leverages our ability to efficiently solve convex optimization problems. In its basic form, it replaces concave terms with a convex upper bound, and then solves the resulting convex problem, which is a restriction of the original DC problem. Basic CCP can thus be viewed as an instance of majorization minimization (MM) algorithms, in which a minimization problem is approximated by an easier to solve upper bound created around the current point (a step called majorization) and then minimized. Many MM extensions have been developed over the years and more can be found in \[ \]. CCP can also be viewed as a version of DCA which instead of explicitly stating the linearization, finds it by solving a dual problem. More information on DCA can be found and the references therein.

A recent overview of CCP, with some extensions, can be found, where the issue of infeasibility is handled (heuristically) by an increasing penalty on constraint violations. The method we present in this paper is an extension of the penalty CCP method introduced, given as algorithm 1.1 below.

Algorithm 1.1 *Penalty CCP.* See for discussion of a few variations on the penalty CCP algorithm, such as not using slack variables for constraints that are convex, i.e., the case when $g_{i}$ is affine. Here it is assumed that $g_{i}$ are differentiable, and have full domain (i.e., $\text{R}^{n}$). The first condition is not critical; we can replace ${\nabla g_{i}}{(x_{k})}$ with a subgradient of $g_{i}$ at $x_{k}$, if it is not differentiable. The linearization with a subgradient instead of the gradient is still a lower bound on $g_{i}$.

In some practical applications, the second assumption, that $g_{i}$ have full domain, does not hold, in which case the penalty CCP algorithm can fail, by arriving at a point $x_{k}$ not in the domain of $g_{i}$, so the convexification step fails. This is one of the issues we will address in this paper.

### Disciplined convex programming

Disciplined convex programming (DCP) is a methodology introduced by Grant et al. that imposes a set of conventions that must be followed when constructing (or specifying or defining) convex programs. Conforming problems are called *disciplined convex programs*.

The conventions of DCP restrict the set of functions that can appear in a problem and the way functions can be composed. Every function in a disciplined convex program must come from a set of atomic functions with known curvature and graph implementation, or representation as partial optimization over a cone program \[, \]. Every composition of functions $f{({g_{1}{(x)}},\ldots,{g_{k}{(x)}})}$, where $f:{\text{R}^{p}\rightarrow\text{R}\rightarrow\text{R}}$ is convex and ${g_{1},\ldots,g_{p}}:{\text{R}^{n}\rightarrow\text{R}}$, must satisfy the following composition rule, which ensures the composition is convex. Let $\overset{\sim}{f}:{\text{R}^{p}\rightarrow\text{R}\rightarrow{\text{R} \cup {\{\infty\}}}}$ be the extended-value extension of $f$ \[, Chap. 3\]. One of the following conditions must hold for each $i = {1,\ldots,p}$: $g_{i}$ is convex and $\overset{\sim}{f}$ is nondecreasing in argument $i$ on the range of $({g_{1}{(x)}},\ldots,{g_{p}{(x)}})$. $g_{i}$ is concave and $\overset{\sim}{f}$ is nonincreasing in argument $i$ on the range of $({g_{1}{(x)}},\ldots,{g_{p}{(x)}})$.

The composition rule for concave functions is analogous. These rules allow us to certify the curvature (i.e., convexity or concavity) of functions described as compositions using the basic atomic functions.

A DCP problem has the specific form where $o$ (the objective), $l_{i}$ (lefthand sides), and $r_{i}$ (righthand sides) are expressions (functions of the variable $x$) with curvature known from the DCP rules, and $\sim$ denotes one of the relational operators $=$, $\leq$, or $\geq$. In DCP this problem must be convex, which imposes conditions on the curvature of the expressions, listed below.

For a minimization problem, $o$ must be convex; for a maximization problem, $o$ must be concave.

When the relational operator is $=$, $l_{i}$ and $r_{i}$ must both be affine.

When the relational operator is $\leq$, $l_{i}$ must be convex, and $r_{i}$ must be concave.

When the relational operator is $\geq$, $l_{i}$ must be concave, and $r_{i}$ must be convex.

Functions that are affine (i.e., are both convex and concave) can match either curvature requirement; for example, we can minimize or maximize an affine expression.

A disciplined convex program can be transformed into an equivalent cone program by replacing each function with its graph implementation. The convex optimization modeling systems YALMIP, CVX, CVXPY, and Convex.jl \[UMZ^+^14\] use DCP to verify problem convexity and automatically convert convex programs into cone programs, which can then be solved using generic solvers.

### Disciplined convex-concave programming

We refer to a problem as a *disciplined convex-concave program* if it has the form, with $o$, $l_{i}$, and $r_{i}$ all having known DCP-verified curvature, *but the DCP curvature conditions for the objective and constraints need not hold*. Such problems include DCP as a special case, but it includes many other nonconvex problems as well. In a DCCP problem we can, for example, maximize a convex function, subject to nonaffine equality constraints, and nonconvex inequality constraints between convex and concave expressions.

The general DC program and the DCCP standard form are equivalent. To express as, we express it as where $x$ is the original optimization variable, and $t$ is a new optimization variable. The objective here is convex, we have one (nonconvex) equality constraint, and the constraints are all nonconvex (except for some special cases when $f_{i}$ or $g_{i}$ is affine) It is straighforward to express the DCCP problem in the form, by identifying the functions $o_{i}$, $l_{i}$, and $r_{i}$ as $\pm f_{i}$ or $\pm g_{i}$ depending on their curvatures.

DCCP problems are an ideal standard form for DC programming because the linearized problem in algorithm 1.1 is a DCP program whenever the original problem is DCCP. The linearized problem can thus be automatically converted into a cone program and solved using generic solvers.

## Domain and subdifferentiability

In this section we delve deeper into an issue that is 'assumed away' in the standard treatments and discussions of DC programming, specifically, how to handle the case when the functions $g_{i}$ do not have full domain. (The functions $f_{i}$ can have non-full domains, but this is handled automatically by the conversion into a cone program.)

### An example

Suppose the domain of $g_{i}$ is $\mathcal{D}_{i}$, for $i = {0,\ldots,m}$. If $\mathcal{D}_{i} \neq \text{R}^{n}$, simply defining the linearization ${\hat{g}}_{i}{(x;z)}$ as the first order Taylor expansion of $g_{i}$ at the point $z$ can lead to failure. The following simple problem gives an example: where $x \in \text{R}$ is the optimization variable. The objective has domain $\text{R}_{+}$, and the solution is evidently $x^{\star} = 0$. The linearized problem in the first iteration of CCP is which has solution $x_{1} = {- 1}$. The DCCP algorithm will fail in the first step of the next iteration, since the original objective function is not defined at $x_{1} = {- 1}$.

If we add the domain constraint directly into the linearized problem, we obtain $x_{1} = 0$, but the first step of the next iteration also fails here, in a different way. While $x_{1}$ is in the domain of the objective function, the objective is not differentiable (or superdifferentiable) at $x_{1}$, so the linearization does not exist. This phenomenon of non-subdifferentiability or non-superdifferentiability can only occur at a point on the boundary of the domain.

### Linearization with domain

Suppose that the intersection of domains of all $g_{i}$ in problem is $\mathcal{D} = {\cap_{i = 0}^{m}\mathcal{D}_{i}}$. The correct way to handle the domain is to define the linearization of $g_{i}$ at point $z$ to be where the indicator function is so any feasible point for the linearized problem is in the domain $\mathcal{D}$.

Since $g_{i}$ is convex, $\mathcal{D}_{i}$ is a convex set and $\mathcal{I}_{i}$ is a convex function. Therefore the 'linearization' is a concave function; it follows that if we replace the standard linearization in algorithm 1.1 with the domain-restricted linearization, the linearized problem is still convex.

### Domain in DCCP

Recall that we defined DCCP problems to ensure that the linearized problem in algorithm 1.1 is a DCP problem. It is not obvious that if we replace the standard linearization with equation the linearized problem is still a DCP problem. In this section we prove that the linearized DCCP problem still satisfies the rules of DCP, or equivalently that each $\mathcal{I}_{i}{(x)}$ has a known graph implementation or satisfies the DCP composition rule.

If $g_{i}$ is an atomic function, then we assume that for some cone constraints $\mathcal{K}_{1},\ldots,\mathcal{K}_{p}$. The assumption is reasonable since $g_{i}$ itself can be represented as partial optimization over a cone program. The graph implementation of $\mathcal{I}_{i}{(x)}$ is simply The other possibility is that $g_{i}$ is a composition of atomic functions. Since the original problem is DCCP, we may assume that ${g_{i}{(x)}} = {f{({h_{1}{(x)}},\ldots,{h_{p}{(x)}})}}$ for some convex atomic function $f:{\text{R}^{p}\rightarrow\text{R}}$ and DCP compliant ${h_{1},\ldots,h_{p}}:{\text{R}^{n}\rightarrow\text{R}}$ such that $f{({h_{1}{(x)}},\ldots,{h_{p}{(x)}})}$ satisfies the DCP composition rule. Then we have where $\mathcal{I}_{f}$ is the indicator function for the domain of $f$ and $\mathcal{I}_{h_{1}},\ldots,\mathcal{I}_{h_{p}}$ are defined similarly.

Since $f$ is convex, $\mathcal{I}_{f}$ is convex. Moreover, $\mathcal{I}_{f}{({h_{1}{(x)}},\ldots,{h_{p}{(x)}})}$ satisfies the DCP composition rule. To see why, observe that for $i = {1,\ldots,p}$, if $h_{i}$ is convex then by assumption the extended-value extension $\overset{\sim}{f}$ is nondecreasing in argument $i$ on the range of $({h_{1}{(x)}},\ldots,{h_{p}{(x)}})$. It follows that $\mathcal{I}_{f}$ is nondecreasing in argument $i$ on the range of $({h_{1}{(x)}},\ldots,{h_{p}{(x)}})$. Similarly, if $h_{i}$ is concave then $\mathcal{I}_{f}$ is nonincreasing in argument $i$ on the range of $({h_{1}{(x)}},\ldots,{h_{p}{(x)}})$.

An inductive argument shows that $\mathcal{I}_{h_{1}},\ldots,\mathcal{I}_{h_{p}}$ are convex and satisfy the DCP rules. We conclude that $\mathcal{I}_{i}$ satisfies the DCP composition rule.

### Sub-differentiability on boundary

When $\mathcal{D} \neq \text{R}^{n}$, a solution to the linearized problem ${\hat{x}}_{k}$ at iteration $k$ can be on the boundary of the closure of $\mathcal{D}$. It is possible (as our simple example above shows) that the convex function $g_{i}$ is not subdifferentiable at ${\hat{x}}_{k}$, which means the linearization does not exist and the algorithm fails. This pathology can and does occur in practical problems.

In order to handle this, at each iteration, when the subgradient ${\nabla g_{i}}{({\hat{x}}_{k})}$ for any function $g_{i}$ does not exist, we simply take a damped step, where $0 < \alpha < 1$. If $x_{0}$ is in the interior of the domain, then $x_{k}$ will be in the interior for all $k \geq 0$, and ${\nabla g_{i}}{(x_{k})}$ will be guaranteed to exist. The algorithm can (and does, for our simple example) converge to a point on the boundary of the the domain, but each iterate is in the interior of the domain, which is enough to guarantee that the linearization exists.

## Initialization

As a heuristic method, the result of algorithm 1.1 generally depends on the initialization, and the initial values of variables should be in the interior of the domain. In many applications there is a natural way to carry out this initialization; here we discuss a generic method (attempting) to do it. Note that in general the problem of finding $x_{0} \in \mathcal{D}$ can be very hard, so we do not expect to have a generic method that always works.

One simple and effective method is to generate random points $z_{j}$ for $j = {1,\ldots,k_{ini}}$, with entries drawn from from i.i.d. standard Gaussian distributions. We then project these points onto $\mathcal{D}$, i.e., solve the problems for $j = {1,\ldots,k_{ini}}$, denoting the solutions as $x_{ini}^{j}$. These points are on the boundary of $\mathcal{D}$ when $z_{j} \notin \mathcal{D}$. We then take Forming the average is a heuristic for finding $x_{0}$ in the interior of $\mathcal{D}$; but it is still possible that $x_{0}$ is on the boundary, in which case it is an unacceptable starting point. As a generic practical method, however, this approach seems to work very well.

## Implementation

The proposed methods described above have been implemented as the Python package DCCP, which extends the package CVXPY. New methods were added to CVXPY to return the domain of a DCP expression (as a list of constraints), and gradients (or subgradients or supergradients) were added to the atoms. The linearization, damping, and initialization are handled by the package DCCP. Users can form any DCCP problem of the form, with each expression composed of functions in the CVXPY library.

When the solve(method = 'dccp') method is called on a problem object, DCCP first verifies that the problem satisfies the DCCP rules. The package then splits each non-affine equality constraint $l_{i} = r_{i}$ into $l_{i} \leq r_{i}$ and $l_{i} \geq r_{i}$. The curvature of the objective and the left and righthand sides of each constraint is checked, and if needed, linearized. In the linearization the function value and gradient are CVXPYparameters, which are constants whose value can change without reconstructing the problem. For each constraint in which the left or righthand side is linearized, a slack variable is introduced, and added to the objective. For any expression that is linearized, the domain of the original expression is added into the constraints.

Algorithm 1.1 is next applied to the convexified problem. If a valid initial value of a variable is given by the user, it is used; otherwise the generic method described above is used. In each iteration the parameters in the linearizations (which are function and gradient values) are updated based on the current value of the variables. If a gradient (or super- or subgradient) w.r.t. any variable does not exist, damping is applied to all the variables. The convexified problem at each iteration is solved using CVXPY.

Some useful functions and attributes in the DCCP package are below.

Function `is_dccp(problem)` returns a boolean indicating if an optimization problem is DCCP.

Attribute `expression.gradient` returns a dictionary of the gradients of a DCP expression w.r.t. its variables at the points specified by `variable.value`. (This attribute is also in the core CVXPY package.)

Function `linearize(expression)` returns the linearization of a DCP expression.

Attribute `expression.domain` returns a list of constraints describing the domain of a DCP expression. (This attribute is also in the core CVXPY package.)

Function `convexify(constraint)` returns the transformed constraint (without slack variables) satisfying DCP of a DCCP constraint.

Method `problem.solve(method = ’dccp’)` carries out the proposed penalty CCP algorithm, and returns the value of the transformed cost function, the value of the weight $\mu_{k}$, and the maximum value of slack variables at each iteration $k$. An optional parameter is used to set the number of times to run CCP, using the randomized initialization.

## Examples

In this section we describe some simple examples, show how they can be expressed using DCCP, and give the results. In each case we run the default solve method, with no tuning or adjustment of algorithm parameters.

### Circle packing

The aim is to arrange $n$ circles in $\text{R}^{2}$ with given radii $r_{i}$ for $i = {1,\ldots,n}$, so that they do not overlap and are contained in the smallest possible square. The optimization problem can be formulated as where the variables are the centers of the circles $c_{i} \in \text{R}^{2}$, $i = {1,\ldots,n}$, and $r_{i}$, $i = {1,\ldots,n}$, are given data. If $l$ is the value of the objective function, the circles are contained in the square ${\lbrack{- l},l\rbrack} \times {\lbrack{- l},l\rbrack}$.

This problem can be specified in DCCP (and solved, in the last line) as follows.

> prob = Problem(Minimize(max_entries(row_norm(c,’inf’)+r)), constr) > prob.solve(method = ’dccp’) Figure 1: Circle packing.

The result obtained for an instance of the problem, with $n = 14$ circles, is shown in figure 1. The fraction of the square covered by circles is $0.73$.

### Boolean least squares

A binary signal $s \in {\{{- 1},1\}}^{n}$ is transmitted through a communication channel, and received as $y = {{As} + v}$, where $v \sim {\mathcal{N}{(0,{\sigma^{2}I})}}$ is a noise, and $A \in \text{R}^{m \times n}$ is the channel matrix. The maximum likelihood estimate of $s$ given $y$ is a solution of where $x$ is the optimization variable. It is a boolean least squares problem if the objective function is squared.

The corresponding code for this problem is given below.

> prob = Problem(Minimize(norm(y-A*x,2)), [square(x) == 1]) > result = prob.solve(method = ’dccp’) Note that the square function in the constraint is elementwise.

Figure 2: Boolean least squares.

We consider some numerical examples with $m = n = 100$, with $A_{ij} \sim {\mathcal{N}{}}$ i.i.d., and $s_{i}$ i.i.d. with probability $1/2$ $1$ or $- 1$. The signal to noise ratio level is $n/\sigma^{2}$. In each of the $10$ independent instances, $A$ and $s$ are generated, and $n/\sigma^{2}$ takes $8$ values from $1$ to $17$. For each value of $n/\sigma^{2}$, $v$ is generated. The bit error rates averaged from $10$ instances are shown in figure 2. Also shown are the same results obtained when the boolean least squares problem is solved globally (at considerably more effort) using MOSEK. We can see that the results, judged in terms of bit error rate, are very similar.

### Path planning

The goal is to find the shortest path connecting points $a$ and $b$ in $\text{R}^{d}$ that avoids $m$ circles, centered at $p_{j}$ with radius $r_{j}$, $j = {1,\ldots,m}$. After discretizing the arc length parametrized path into points $x_{0},\ldots,x_{n}$, the problem is posed as where $L$ and $x_{i}$ are variables, and $a$, $b$, $p_{j}$, and $r_{j}$ are given.

The code is given below.

> constr += [norm(x[:,i]-center[:,j],2) >= r[j]] > prob = Problem(Minimize(cost), constr) > result = prob.solve(method = ’dccp’) Figure 3: Path planning.

An example with $d = 2$ and $n = 50$ is shown in figure 3.

### Control with collision avoidance

We have $n$ linear dynamic systems, given by where $t = {0,1,\ldots}$ denotes (discrete) time, $x_{t}^{i}$ are the states, and $y_{t}^{i}$ are the outputs. At each time $t$ for $t = {0,\ldots,T}$ the $n$ outputs $y_{t}^{i}$ are required to keep a distance of at least $d_{\min}$ from each other. The initial states $x_{0}^{i}$ and ending states $x_{n}^{i}$ are given by $x_{init}^{i}$ and $x_{end}^{i}$, and the inputs are limited by ${\| u_{t}^{i}\|}_{\infty} \leq f_{\max}$. We will minimize a sum of the $\ell_{1}$ norms of the inputs, an approximation of fuel use. (Of course we can have any convex state and input constraints, and any convex objective.) This gives the problem where $x_{t}^{i}$, $y_{t}^{i}$, and $u_{t}^{i}$ are variables.

The code can be written as follows.

> constr += [norm(u[i],’inf’) <= f_max] > constr += [norm(y[i][t] - y[j][t],2) >= d_min] > prob = Problem(Minimize(cost), constr) > prob.solve(method = ’dccp’) We consider an instance with $n = 2$, with outputs (positions) $y_{t}^{i} \in \text{R}^{2}$, $d_{\min} = 0.6$, $f_{\max} = 0.5$, $T = 100$. The linear dynamic system matrices are The results are in figure 4, where the black arrows in the first two figures show initial and final states (position and velocity), and the black dashed line in the third figure shows $d_{\min}$.

Figure 4: Optimal control with collision avoidance. Left: Output trajectory without collision avoidance. Middle: Output trajectory with collision avoidance. Right: Distance between outputs versus time.

### Sparse recovery using $\ell_{1/2}$ 'norm'

The aim is to recover a sparse nonnegative signal $x_{0} \in \text{R}^{n}$ from a measurement vector $y = {Ax_{0}}$, where $A \in \text{R}^{m \times n}$ (with $m < n$) is a known sensing matrix. A common heuristic based on convex optimization is to minimize the $\ell_{1}$ norm of $x$ (which reduces here to the sum of entries of $x$) subject to $y = {Ax_{0}}$ (and here, $x \geq 0$). It has been proposed to minimize the sum of the *squareroots* of the entries of $x$, which since $x \geq 0$ is the same as minimizing the squareroot of the $\ell_{1/2}$ 'norm' (which is not convex, and therefore not a norm), to obtain better recovery. The optimization problem is where $x$ is the variable. (The constraint $x \geq 0$ is implicit, since this is the objective domain.) This is a nonconvex problem, directly in DCCP form.

The corresponding code is as follows.

> prob = Problem(Minimize(sum_entries(sqrt(x))), [A*x == y]) > result = prob.solve(method = ’dccp’) Figure 5: Sparse recovery. Left: l1 norm. Right: Sqrt of ℓ1/2 ‘norm’.

In a numerical simulation, we take $n = 100$, $A_{ij} \sim {\mathcal{N}{}}$, the positions of the nonzero entries in $x_{0}$ are from uniform distribution, and the nonzero values are the absolute values of $\mathcal{N}{}$ random variables. To count the probability of recovery, $100$ independent instances are tested, and a recovery is successful if the relative error ${\|{\hat{x} - x_{0}}\|}_{2}/{\| x_{0}\|}_{2}$ is less than $0.01$. In each instance, the cardinality takes $6$ values from $30$ to $50$, according to which $x_{0}$ is generated, and $A$ is generated for each $m$ taking one of the $6$ values from $50$ to $80$. The results in figure 5 verify that nonconvex recovery is more effective than convex recovery.

### Phase retrieval

Phase retrieval is the problem of recovering a signal $x_{0} \in \mathbf{C}^{n}$ from the magnitudes of the complex inner products $x_{0}^{\ast}a_{k}$, for $k = {1,\ldots,m}$, where $a_{k} \in \mathbf{C}^{n}$ are the given measurement vectors. The recovery problem can be expressed as where $x \in \mathbf{C}^{n}$ is the optimization variable, and $a_{k}$ and $y_{k} \in \text{R}_{+}$ are given. The lefthand side of the constraints are convex quadratic functions of the real and imaginary parts of the arguments, which are in turn linear functions of the variable $x$.

The following code segment specifies the problem. CVXPY (and therefore DCCP) does not yet support complex variables and constants, so we expand complex numbers into real and imaginary parts.

> z.value = np.random.rand > prob = Problem(Minimize, constr) > result = prob.solve(method = ’dccp’) Figure 6: Phase retrieval.

We consider an instance with $n = 128$ and $m = {3n}$. The real part and the imaginary part of each entry of $x_{0}$ and $a_{k}$ are i.i.d. $\mathcal{N}{}$. The result in figure 6 shows that the phase is recovered (up to a global constant).

### Magnitude filter design

A filter is characterized by its impulse response ${\{ h_{k}\}}_{k = 1}^{n}$. Its frequency response $H:{{\lbrack 0,\pi\rbrack}\rightarrow\mathbf{C}}$ is defined as where $i = \sqrt{- 1}$. In *magnitude filter design*, the goal is to find impulse response coefficients that meet certain specifications on the magnitude of the frequency response. We will consider a typical lowpass filter design problem, which can be expressed as where $h \in \text{R}^{n}$ and $U_{stop} \in \text{R}$ are the optimization variables. The passband magnitude limits $L_{pass}$ and $U_{pass}$ are given.

The code can be written as follows.

> for l in range(len(omega)): > constr += [norm(expo[l]*h,2) >= L_pass] > constr += [norm(expo[l]*h,2) <= U_pass] > constr += [norm(expo[l]*h,2) <= U_stop] > prob = Problem(Minimize(U_stop), constr) > result = prob.solve(method = ’dccp’) Figure 7: Low pass filter design. The frequency response magnitude upper and lower limits are shown.

An instance of low pass filter design, with $n = 10$ and $N = 100$, is shown in figure 7.

### Sparse singular vectors

The left singular vectors associated with the smallest and largest singular values of a matrix $A$ (globally) minimize and maximize ${\|{Ax}\|}_{2}$ subject to ${\| x\|}_{2} = 1$. Here we seek sparse vectors, with ${\| x\|}_{2} = 1$, which make ${\|{Ax}\|}_{2}$ large or small. To induce sparsity in $x$, we limit the $\ell_{1}$-norm of $x$. (We could also limit a nonconvex sparsifier, as above in sparse recovery.) This leads to the problems where $x \in \text{R}^{n}$ is the variable and $\mu \geq 0$ controls the sparsification, to find $x$ that is sparse, satisfies ${\| x\|}_{2} = 1$, and makes ${\|{Ax}\|}_{2}$ small or large. We call such a vector, with some abuse of notation, a *sparse singular vector*. Since ${\| x\|}_{2} = 1$, we know $1 \leq {\| x\|}_{1} \leq \sqrt{n}$, so the range of $\mu$ can be set as $\lbrack 1,\sqrt{n}\rbrack$.

The code (for minimization) is the following.

> Ψprob = Problem(Minimize(norm(A*x)), [norm(x) == 1, norm(x,1) <= mu]) > Ψprob.solve(method = ’dccp’) Figure 8: Sparse singular vectors.

We consider an instance for minimization with a random matrix $A \in \text{R}^{100 \times 100}$ with i.i.d. entries $A_{ij} \sim {\mathcal{N}{}}$, with (positive) smallest singular value $\sigma_{\min}$. The parameter $\mu$ is swept from $1$ to $10$ with increment $0.2$, and for each value of $\mu$ the result of solving the problem above is shown as a red dot in figure 8. The most left point in the figure corresponds to ${\| x\|}_{1} \leq 1$, which gives cardinality $1$. (In this instance it achieves the globally optimal value, which is the smallest of the norm of the columns of $A$.)

### Gaussian covariance matrix estimation

Suppose $y_{i} \in \text{R}^{n}$ for $i = {1,\ldots,N}$ are points drawn i.i.d from $\mathcal{N}{(0,\Sigma)}$. Our goal is to estimate the parameter $\Sigma$ given these samples. The maximum likelihood problem of estimating $\Sigma$ is convex in the inverse of $\Sigma$, but not $\Sigma$. If there are no other constraints on $\Sigma$, the maximum likelihood estimate is $\hat{\Sigma} = {\frac{1}{N}{\sum_{i = 1}^{N}{y_{i}y_{i}^{T}}}}$, the empirical covariance matrix. We consider here the case where the sign of the off-diagonal entries in $\Sigma$ is known; that is, we know which entries of $\Sigma$ are negative, which are zero, and which are positive. (So we know which components of $y$ are uncorrelated, and which are negatively and positively correlated.)

The maximum likelihood problem is then where $\Sigma$ is the variable, and the index sets $\Omega_{+}$, $\Omega_{-}$, and $\Omega_{0}$ are given. The objective is a difference of convex functions, so we transform the problem into the following DCCP problem with additional variable $t$, The code is as follows.

> cost = -log_det(Sigma) - t > trace_val = trace(sum([matrix_frac(y[:,i], Sigma)/N for i in range(N)])) > prob = Problem(Maximize(cost), > prob.solve(method = ’dccp’) Figure 9: Gaussian covariance matrix estimation.

An example with $n = 20$ and $N = 30$ is in figure 9. Not surprisingly, knowledge of the signs of the entries of $\Sigma$ allows us to obtain a much better estimate of the true covariance matrix.
