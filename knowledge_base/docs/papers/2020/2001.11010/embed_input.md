<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Automatic Repair of Convex Optimization Problems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Given an infeasible, unbounded, or pathological convex optimization problem, a natural question to ask is: what is the smallest change we can make to the problem's parameters such that the problem becomes solvable? In this paper, we address this question by posing it as an optimization problem involving the minimization of a convex regularization function of the parameters, subject to the constraint that the parameters result in a solvable problem. We propose a heuristic for approximately solving this problem that is based on the penalty method and leverages recently developed methods that can efficiently evaluate the derivative of the solution of a convex cone program with respect to its parameters. We illustrate our method by applying it to examples in optimal control and economics.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Parametrized convex optimization", "weight": 1.0} -->

We consider parametrized convex optimization problems, which have the form

<!-- chunk {"id": "body-0004", "role": "body", "section": "Solvable problems", "weight": 1.0} -->

We allow $p^{\star}$ to take on the extended values $\pm \infty$. Roughly speaking, we say that is *solvable* if $p^{\star}$ is finite and attainable. (We will define solvable formally below, when we canonicalize into a cone program.) When the problem is unsolvable, it falls into one of three cases: it is *infeasible* if $p^{\star} = {+ \infty}$, *unbounded below* if $p^{\star} = {- \infty}$, and *pathological* if $p^{\star}$ is finite, but not attainable by any $x$, or strong duality does not hold. Unsolvable problems are often undesirable since, in many cases, there does not exist a solution.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Performance metric", "weight": 1.0} -->

The goal in this paper is to repair an unsolvable problem by adjusting the parameter $\theta$ so that it becomes solvable. We will judge the desirability of a new parameter $\theta$ by a (convex) performance metric function $r:{\text{R}^{k}\rightarrow{\text{R} \cup {\{{+ \infty}\}}}}$, which we would like to be small. (Infinite values of $r$ denote constraints on the parameter.) A simple example of $r$ is the Euclidean distance to an initial parameter vector $\theta_{0}$, or ${r{(\theta)}} = {\|{\theta - \theta_{0}}\|}_{2}$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Repairing a convex optimization problem", "weight": 1.0} -->

In this paper, we consider the problem of repairing a convex optimization problem, as measured by the performance metric, by solving the problem

<!-- chunk {"id": "body-0007", "role": "body", "section": "Pathologies", "weight": 1.0} -->

There are various pathologies that can occur in this formulation. For example, the set of $\theta$ that lead to solvable problems could be open, meaning there might not exist a solution to, or the complement could have (Lebesgue) measure zero, meaning that the problem can be made solvable by essentially any perturbation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Pathologies", "weight": 1.0} -->

and regularization function ${r{(\theta)}} = \theta^{2}$. The set of solvable $\theta$ is $\{\theta\mid{\theta \neq 0}\}$, which is both open and has complement with measure zero. The optimal value of problem is 0, but is not attainable by any solvable $\theta$. The best we can hope to do in these situations is to produce a minimizing sequence.

<!-- chunk {"id": "body-0009", "role": "body", "section": "NP-hardness", "weight": 1.0} -->

Repairing a convex optimization problem is NP-hard. To show this, we reduce the 0-1 integer programming problem

<!-- chunk {"id": "body-0010", "role": "body", "section": "NP-hardness", "weight": 1.0} -->

Let ${r{(\theta)}} = 0$. The convex optimization problem that we would like to be solvable be

<!-- chunk {"id": "body-0011", "role": "body", "section": "NP-hardness", "weight": 1.0} -->

with variable $x$. Problem has the same constraints as, since is feasible if and only if ${\theta_{i}{({\theta_{i} - 1})}} = 0$, $i = {1,\ldots,n}$, and ${A\theta} = b$. Therefore, the problem of finding any feasible parameters for (i.e., with ${r{(\theta)}} = 0$), is at least as hard as the 0-1 integer programming problem, which is known to be NP-hard.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Cone program formulation", "weight": 1.0} -->

In practice, most convex optimization problems are solved by reformulating them as equivalent conic programs and passing the numerical data in the reformulated problem to general conic solvers such as SCS, Mosek, or Gurobi. This process of canonicalization is often done automatically by packages like CVXPY, which generate a conic program from a high-level description of the problem.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Canonicalization", "weight": 1.0} -->

For the remainder of the paper, we will consider the canonicalized form of problem. The primal (P) and dual (D) form of the canonicalized convex cone program is (see, e.g., )

<!-- chunk {"id": "body-0014", "role": "body", "section": "Solution", "weight": 1.0} -->

The vector $(x^{\star},y^{\star},s^{\star})$ is a solution to problem if

<!-- chunk {"id": "body-0015", "role": "body", "section": "Solution", "weight": 1.0} -->

These conditions merely state that $(x^{\star},s^{\star})$ is primal feasible, $y^{\star}$ is dual feasible, and that there is zero duality gap, which implies that $(x^{\star},y^{\star},s^{\star})$ is optimal by weak duality \[5, §5.2.2\]. Problems and are solvable if and only if there exists a point that satisfies.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Primal-dual embedding", "weight": 1.0} -->

The primal-dual embedding of problem is the cone program

<!-- chunk {"id": "body-0017", "role": "body", "section": "Primal-dual embedding", "weight": 1.0} -->

with variables $t$, $x$, $y$, and $s$. This problem is guaranteed to be feasible since, for any $\theta \in \text{R}^{k}$, setting $x = 0$, $y = 0$, $s = 0$, and $t = {\|{({b{(\theta)}},{c{(\theta)}})}\|}_{2}$ yields a feasible point. The problem is also guaranteed to be bounded from below, since the objective is nonnegative. Taken together, this implies that problem always has a solution, assuming it is not pathological.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Optimal value of", "weight": 1.0} -->

Let $t^{\star}:{\text{R}^{k}\rightarrow\text{R}}$ denote the optimal value of problem as a function of $\theta$. Notably, we have that ${t^{\star}{(\theta)}} = 0$ if and only if problem is solvable, since if ${t^{\star}{(\theta)}} = 0$, the solution to problem satisfies and therefore problem is solvable. On the other hand, if problem is solvable, then there exists a point that satisfies and is feasible, so ${t^{\star}{(\theta)}} = 0$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Differentiability of $t^{\\star}$", "weight": 1.0} -->

In practice, $t^{\star}$ is often a differentiable function of $\theta$. This is the case when $A$, $b$, and $c$ are differentiable, which we will assume, and the optimal value of problem is differentiable in $A$, $b$, and $c$. Under some technical conditions that are often satisfied in practice, the optimal value of a cone program is a differentiable function of its problem data. We will assume that $t^{\star}$ is differentiable, and that we can efficiently compute its gradient ${\nabla t^{\star}}{(\theta)}$ using the methods described in and the chain rule.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Reformulation", "weight": 1.0} -->

In light of these observations, we can reformulate problem as

<!-- chunk {"id": "body-0021", "role": "body", "section": "Reformulation", "weight": 1.0} -->

with variable $\theta$. Here we have replaced the intractable constraint in problem with an equivalent smooth equality constraint. Since this problem is NP-hard, we must resort to heuristics to find approximate solutions; we give one in §3.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Penalty method", "weight": 1.0} -->

One simple heuristic is to use the penalty method to (approximately) solve. Starting from $\theta^{0} \in \text{R}^{k}$ and $\lambda^{0} > 0$, at iteration $\ell$, the penalty method performs the update

<!-- chunk {"id": "body-0023", "role": "body", "section": "Penalty method", "weight": 1.0} -->

To perform the update, we must solve the unconstrained optimization problem

<!-- chunk {"id": "body-0024", "role": "body", "section": "Penalty method", "weight": 1.0} -->

with variable $\theta$. The objective is the sum of a differentiable function and a potentially nonsmooth convex function, for which there exist many efficient methods. The simplest (and often most effective) of these methods is the proximal gradient method (which stems from the proximal point method; for a modern reference see ). The proximal gradient method consists of the iterations

<!-- chunk {"id": "body-0025", "role": "body", "section": "Penalty method", "weight": 1.0} -->

where the proximal operator is defined as

<!-- chunk {"id": "body-0026", "role": "body", "section": "Penalty method", "weight": 1.0} -->

Since $r$ is convex, evaluating the proximal operator of $\alpha\lambdar$ requires solving a convex optimization problem. Indeed, for many practical choices of $r$, its proximal operator has a closed-form expression \[16, §6\].

<!-- chunk {"id": "body-0027", "role": "body", "section": "Penalty method", "weight": 1.0} -->

We run the proximal gradient method until the stopping criterion

<!-- chunk {"id": "body-0028", "role": "body", "section": "Penalty method", "weight": 1.0} -->

is reached, where $g^{l} = {{\nabla t^{\star}}{(\theta^{l})}}$, for some given tolerance $\epsilon_{in} > 0$. We employ the adaptive step size scheme described. The full procedure is described in algorithm 3 below.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Penalty method", "weight": 1.0} -->

Algorithm 3.1 *Finding the closest solvable convex optimization problem.*

<!-- chunk {"id": "body-0030", "role": "body", "section": "Implementation", "weight": 1.0} -->

We have implemented algorithm 3 in Python, which is available online at

<!-- chunk {"id": "body-0031", "role": "body", "section": "Implementation", "weight": 1.0} -->

The interface is the repair method, which, given a parametrized CVXPY problem and a convex regularization function, uses algorithm 3 to find the parameters that approximately minimize that regularization function and result in a solvable CVXPY problem. We use SCS to solve cone programs and diffcp to compute the gradient of cone programs. We require the CVXPY problem to be a disciplined parametrized program (DPP), so that the mapping from parameters to $(A,b,c)$ is affine, and hence differentiable.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Implementation", "weight": 1.0} -->

Until this point, we have assumed that the optimal value of problem is differentiable in $A$, $b$, and $c$. However, in our implementation, we do not require this to be the case. So long as it is differentiable almost everywhere, it is reasonable to apply the proximal gradient method to. At non-differentiable points, we instead compute a heuristic quantity. For example, a source of non-differentiability is the singularity of a particular matrix; in this case, diffcp computes a least-squares approximation of the gradient \[2, §3\].

<!-- chunk {"id": "body-0033", "role": "body", "section": "Spacecraft landing", "weight": 1.0} -->

We consider the problem of landing a spacecraft with a gimbaled thruster. The dynamics are

<!-- chunk {"id": "body-0034", "role": "body", "section": "Spacecraft landing", "weight": 1.0} -->

where $m > 0$ is the spacecraft mass, ${x{(t)}} \in \text{R}^{3}$ is the spacecraft position, ${f{(t)}} \in \text{R}^{3}$ is the force applied by the thruster, $g > 0$ is the gravitational acceleration, and $e_{3} = {}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Spacecraft landing", "weight": 1.0} -->

Our goal, given some initial position $x^{init} \in \text{R}^{3}$ and velocity $v^{init} \in \text{R}^{3}$, is to land the spacecraft at zero position and velocity at some touchdown time $T > 0$, i.e., ${x{(T)}} = 0$ and ${\overset{˙}{x}{(T)}} = 0$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Spacecraft landing", "weight": 1.0} -->

We have a total available fuel $M^{fuel}$ and a thrust limit $F^{\max}$. This results in the constraints

<!-- chunk {"id": "body-0037", "role": "body", "section": "Spacecraft landing", "weight": 1.0} -->

where $\gamma$ is the fuel consumption coefficient. We also have a gimbal constraint

<!-- chunk {"id": "body-0038", "role": "body", "section": "Spacecraft landing", "weight": 1.0} -->

where $\alpha$ is equal to the tangent of the maximum gimbal angle.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Spacecraft landing", "weight": 1.0} -->

We discretize the thrust profile, position, and velocity at intervals of length $h$, or

<!-- chunk {"id": "body-0040", "role": "body", "section": "Spacecraft landing", "weight": 1.0} -->

To find if there exists a thrust profile to land the spacecraft, we solve the problem

<!-- chunk {"id": "body-0041", "role": "body", "section": "Spacecraft landing", "weight": 1.0} -->

with variables $x$, $v$, and $f$. This problem is a parametrized convex optimization problem, with parameter

<!-- chunk {"id": "body-0042", "role": "body", "section": "Spacecraft landing", "weight": 1.0} -->

Suppose that we are given a parameter vector $\theta_{0}$ for which it is impossible to find a feasible thrust profile, i.e., problem is infeasible. Suppose, in addition, that we are allowed to change the spacecraft's parameters in a limited way. We seek to find the smallest changes to the mass and constraints on the fuel and thrust limit that guarantees the feasibility of problem. We can (approximately) do this with algorithm 3.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We consider a numerical example with data

<!-- chunk {"id": "body-0044", "role": "body", "section": "Numerical example", "weight": 1.0} -->

The initial parameters are infeasible, i.e., there is no possible thrust profile which allows the spacecraft to land in time, so we use algorithm 3 to modify the design parameters in order to have a feasible landing thrust profile. We use the performance metric

<!-- chunk {"id": "body-0045", "role": "body", "section": "Numerical example", "weight": 1.0} -->

which constrains the mass to be greater than or equal to 9, and penalizes the percentage change in each of the parameters. The resulting feasible design has the parameters

<!-- chunk {"id": "body-0046", "role": "body", "section": "Arbitrage", "weight": 1.0} -->

Consider an event (e.g., horse race, sports game, or a financial market over a short time period) with $m$ possible outcomes and $n$ possible wagers on the outcome. The return matrix is $R \in \text{R}^{m \times n}$, where $R_{ij}$ is the return in dollars for the outcome $i$ and wager $j$ per dollar bet. A betting strategy is a vector $w \in \text{R}_{+}^{n}$, where $w_{i}$ is the amount that we bet on the $i$th wager. If we use a betting strategy $w$ and outcome $i$ occurs, then the return is ${({Rw})}_{i}$ dollars.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Arbitrage", "weight": 1.0} -->

We say that there is an *arbitrage opportunity* in this event if there exists a betting strategy $w \in \text{R}_{+}^{n}$ that is guaranteed to have nonnegative return for each outcome, and positive return in at least one outcome. We can check whether there exists an arbitrage opportunity by solving the convex optimization problem

<!-- chunk {"id": "body-0048", "role": "body", "section": "Arbitrage", "weight": 1.0} -->

with variable $w$. If this problem is unbounded above, then there is an arbitrage opportunity.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Arbitrage", "weight": 1.0} -->

Suppose that we are the event organizer (e.g., sports book director, bookie, or financial exchange) and we wish to design the return matrix $R$ such that there is are arbitrage opportunities and that some performance metric $r$ is small. We can tackle this problem by finding the nearest solvable convex optimization problem to problem using algorithm 3.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We consider a horse race with $n = 3$ horses and $m = 5$ outcomes. The initial return matrix is

<!-- chunk {"id": "body-0051", "role": "body", "section": "Numerical example", "weight": 1.0} -->

for which there is an arbitrage opportunity in the direction

<!-- chunk {"id": "body-0052", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We consider the regularization function ${r{(R)}} = {\|{{({R - R_{0}})}/R_{0}}\|}_{1}$, where $/$ is meant elementwise. After running algorithm 3, the arbitrage-free return matrix is
