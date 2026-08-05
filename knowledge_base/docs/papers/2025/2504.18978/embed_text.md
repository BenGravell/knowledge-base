<!-- arxiv-full-text:v1 {"arxiv_id": "2504.18978", "source": "arxiv-html"} -->

## Introduction

Selecting the most effective motion-planning algorithm for a robotic system often requires balancing three competing objectives: reliability, computational efficiency, and trajectory quality. Consider Sparrow, the robot arm in Fig. 1 that sorts individual products into bins before they get packaged in the Amazon warehouses. The algorithms that move Sparrow must be extremely reliable, as these robots handle millions of diverse products every day, and each failure requires expensive interventions. They must be efficient, since every millisecond spent planning is taken away from other crucial computations, and limits the robot reactivity to sensor observations. Finally, they should generate trajectories that push the robot to its physical limits, so that the work-cell throughput is maximized and the hardware is fully utilized. Unfortunately, general-purpose methods for motion planning do not excel in all of these areas at once.

Sampling-based methods like PRM, RRT, and their asymptotically optimal versions can be fast enough for real-time applications. They are highly parallelizable and can run on a GPU. They are also reliable in low-dimensional spaces, where dense sampling is computationally feasible. However, they become significantly less effective as the space dimension grows. Additionally, although their kinodynamic variants support differential constraints, sampling-based methods remain considerably less practical for designing smooth continuous trajectories than producing polygonal paths.

Trajectory-optimization methods based on nonconvex programming scale well to high-dimensional spaces and explicitly factor in the robot kinematics and dynamics. Over the years, these techniques have become significantly faster and, with the advent of specialized GPU implementations, they are now even viable for real-time motion planning. Despite these advances, the main limitation of trajectory optimization remains its reliance on local solvers, which require extensive parameter tuning, handcrafted warm starts, may suffer from inconsistent runtimes, and can even fail to find a solution. While various strategies have been proposed to address these issues, trajectory optimization remains often too brittle for industrial deployment.

Figure 1: Sparrow robot sorting products into bins in the Amazon warehouses.

Recently, a new family of motion planners that combine sampling-based and trajectory-optimization methods has stemmed . First, the collision-free space is decomposed into safe convex sets. This decomposition can be computed using region-inflation algorithms and tailored sampling strategies. For UAVs, also safe flight corridors are widely used. Then, the continuous trajectory is optimized in conjunction with the discrete sequence of sets to be traversed. The work in has shown that, for a limited class of costs and constraints, this discrete-continuous problem is solvable through a single convex program, using the framework called Graphs of Convex Sets (GCS). The extensions of GCS in have enabled the solution of larger problems in a fraction of the time. The motion planner in tackles a similar problem, but first selects a discrete sequence of safe sets using a heuristic, and later optimizes a continuous trajectory within these fixed sets. This split sacrifices optimality but preserves completeness, and enables support for a broader range of costs and constraints.

This paper focuses on a problem similar to the one in the second phase of: we seek a trajectory that traverses a sequence of convex sets in minimum time, and satisfies convex velocity and acceleration constraints. This is a purely continuous problem, but is nonconvex due to the joint optimization of the trajectory shape and timing. Our contribution is a biconvex method, which we call Sequence of Convex Sets (SCS), that solves this problem effectively. SCS starts by quickly producing a feasible trajectory. Then, it alternates between two convex subproblems. The first is obtained from the original nonconvex problem by fixing the points where the trajectory transitions from one safe set to the next. The second is derived similarly, by fixing the transition velocities.

As most multi-convex methods, SCS is heuristic: it typically finds high-quality trajectories quickly, but might not converge to the problem optimum, or within a given distance of it. On the other hand, SCS is complete (i.e., guaranteed to find a feasible solution). Its main algorithmic advantage is that the two convex subproblems are conservative approximations of the original nonconvex problem. This allows us to take whole steps in the direction their optima without using a line search or a trust region, as done in and other trajectory-optimization methods. This makes the convergence of SCS fast and monotone, and eliminates any parameter tuning. Furthermore, it makes our algorithm anytime (it returns a feasible trajectory even if stopped early).

We show that SCS consistently finds high-quality trajectories in a fraction of the time of the state-of-the-art solvers SNOPT and IPOPT. We also demonstrate SCS on the task of transferring packages between bins using two Sparrow robots. In this task, SCS designs lower-cost trajectories than the trust-region method , and achieves runtimes comparable to waypoint-based methods that are commonly used in industry.

### I-A Outline

This paper is organized as follows. In §II, we state our motion-planning problem and, in §III, we give a high-level overview of SCS. The details on the two convex subproblems and the initialization step are illustrated in §IV, §V, and §VI. Up to this point, we work only with infinite-dimensional trajectories. In §VII, we show how our method can be efficiently implemented on a computer by using piecewise Bézier curves as a finite-dimensional trajectory parameterization. The strengths and limitations of SCS are discussed in §VIII and §IX. In §X, we demonstrate the effectiveness of SCS through a variety of numerical experiments.

### I-B Notation and convexity background

In this paper, the variable $i$ is always understood to be a positive integer. Thus, when saying for all $i \leq I$ we mean for all $i \in {\{ 1,\ldots,I\}}$. Conversely, the variable $k$ is always nonnegative, and $k \leq K$ is shorthand for $k \in {\{ 0,\ldots,K\}}$.

We use calligraphic letters to represent sets, and bold letters for vectors, vector-valued functions, and matrices. We use the notation ${\lambda\mathcal{S}} = {\{{\lambda{\mathbf{x}}}:{{\mathbf{x}} \in \mathcal{S}}\}}$ to denote the product of a scalar $\lambda \in {\mathbb{R}}$ and a set $\mathcal{S} \subseteq {\mathbb{R}}^{n}$. We will use multiple times the fact that if a set $\mathcal{S}$ is convex then also the set $\{{({\mathbf{x}},\lambda)}:{\lambda \geq {0{\mathbf{x}}} \in {\lambda\mathcal{S}}}\}$ is convex \[3, §2.3.3\]. The latter set is easily computed in practice: for instance, if $\mathcal{S}$ is a polytope of the form $\{{\mathbf{x}}:{{{\mathbf{A}}{\mathbf{x}}} \leq {\mathbf{b}}}\}$, then the condition ${\mathbf{x}} \in {\lambda\mathcal{S}}$ is equivalent to ${{\mathbf{A}}{\mathbf{x}}} \leq {\lambda{\mathbf{b}}}$. A similar formula can be used for any set $\mathcal{S}$ described in standard conic form \[29, Ex. 4.3\].

## Problem Statement

We seek a trajectory that traverses a sequence of convex sets in minimum time, subject to boundary conditions and convex velocity and acceleration constraints. Fig. 2 shows a simple instance of this problem, and illustrates our notation.

Figure 2: Example of the motion-planning problem. The safe convex sets to be traversed are 𝒬1, …, 𝒬4. The trajectory q: [0, T] → ℝ2 is shown in blue. The initial and terminal points are qinit and qterm. The times t0, …, t4 determine the trajectory piece assigned to each safe set.

The sequence of safe convex sets is denoted as where $I$ is the number of sets and $n$ is the space dimension. Each set is assumed to be closed and intersect with the next: The trajectory is represented by the function ${\mathbf{q}}:{{\lbrack 0,T\rbrack}\rightarrow{\mathbb{R}}^{n}}$, with time duration $T > 0$. The initial ${\mathbf{q}}{}$ and terminal point ${\mathbf{q}}{(T)}$ are fixed to ${\mathbf{q}}_{init} \in \mathcal{Q}_{1}$ and ${\mathbf{q}}_{term} \in \mathcal{Q}_{I}$, respectively.

The safe sets must be traversed in the given order, and no set can be skipped. We denote with $t_{1} \leq \ldots \leq t_{I - 1}$ the *transition times* at which the trajectory moves from one set to the next. For simplicity of notation, we also let $t_{0} = 0$ and $t_{I} = T$. We then require that the trajectory ${\mathbf{q}}{(t)}$ lie in the set $\mathcal{Q}_{i}$ for all $t \in {\lbrack t_{i - 1},t_{i}\rbrack}$ and $i \leq I$.

The trajectory velocity and the acceleration are denoted as $\overset{˙}{\mathbf{q}}{(t)}$ and $\overset{¨}{\mathbf{q}}{(t)}$, respectively. The first is assumed to be continuous, while the second is allowed to have discontinuities (i.e., $\mathbf{q}$ is continuously differentiable). The initial $\overset{˙}{\mathbf{q}}{}$ and terminal $\overset{˙}{\mathbf{q}}{(T)}$ velocities are fixed to zero. The trajectory derivatives must satisfy the constraints at all times $t \in {\lbrack 0,T\rbrack}$. The sets $\mathcal{V}$ and $\mathcal{A}$ are closed and convex, and contain the origin in their interior: Among the trajectories that verify the constraints above, we seek one of minimum time duration $T$. This leads us to the following optimization problem: The variables are the trajectory $\mathbf{q}$, the duration $T$, and the times $t_{0},\ldots,t_{I}$. The first makes the problem infinite dimensional. The *problem data* are the endpoints ${\mathbf{q}}_{init}$ and ${\mathbf{q}}_{term}$, the safe sets $\mathcal{Q}_{1},\ldots,\mathcal{Q}_{I}$, and the constraint sets $\mathcal{V}$ and $\mathcal{A}$. The differentiability constraint on the function $\mathbf{q}$ is implicit here.

### II-A Feasibility

With the next proposition, we establish the feasibility of problem. As in \[28, §II-C\], we do so by constructing a polygonal (i.e., piecewise linear) trajectory that satisfies all the problem constraints. A similar construction will be used to initialize our method.

### Proposition 1

If the problem data satisfy the assumptions listed above, then problem is feasible.

### Proof

We construct a trajectory $\mathbf{q}$ that starts at ${{\mathbf{q}}{(t_{0})}} = {\mathbf{q}}_{init}$, terminates at ${{\mathbf{q}}{(t_{I})}} = {\mathbf{q}}_{term}$, and interpolates any *transition points* ${{\mathbf{q}}{(t_{i})}} \in {\mathcal{Q}_{i} \cap \mathcal{Q}_{i + 1}}$ for $i \leq {I - 1}$. For $i \leq I$, the trajectory piece within the set $\mathcal{Q}_{i}$ connects ${\mathbf{q}}{(t_{i - 1})}$ and ${\mathbf{q}}{(t_{i})}$ through a straight line. Thus, the overall trajectory stays within the union of the safe sets and traverses them in the desired order. We let the times $t_{0},\ldots,t_{I}$ be well spaced, so that the velocity $\overset{˙}{\mathbf{q}}$ and the acceleration $\overset{¨}{\mathbf{q}}$ can be small enough to lie in the constraint sets $\mathcal{V}$ and $\mathcal{A}$ at all times (recall that these sets contain the origin in their interior). Finally, we require that the velocity be zero at each time $t_{0},\ldots,t_{I}$. This makes the velocity continuous, even though the trajectory is polygonal. The resulting trajectory is feasible for problem. ∎

### II-B Positive traversal times

According to constraint (1h), the *traversal time* $T_{i} = {t_{i} - t_{i - 1}}$ of a safe set $\mathcal{Q}_{i}$ can be zero. This can be optimal if, e.g., a safe set is lower dimensional or our trajectory touches it only at an extreme point. However, our biconvex method will assume that the traversal times $T_{i}$ are strictly positive, for all $i \leq I$. The following is a simple sufficient condition on the problem data that ensures this. It forces our trajectory to cover a nonzero distance within each safe set.

### Assumption 1

The boundary points and the safe sets are such that ${\mathbf{q}}_{init} \notin \mathcal{Q}_{2}$, ${\mathbf{q}}_{term} \notin \mathcal{Q}_{I - 1}$, and We will let this assumption hold throughout the paper, so that zero traversal times will always be infeasible in our optimization problems. Alternatively, our algorithm can be easily modified to incorporate a small lower bound on the traversal times. For most practical problems, this modification has a negligible effect on the optimal trajectories.

## Biconvex Method

We give a high-level overview of our biconvex method here, deferring the details to later sections.

The observation at the core of SCS is that problem reduces to a convex program if we fix either the *transition points* or the *transition velocities*: (More precisely, this is true modulo a small conservative approximation of the acceleration constraint (1g), which relies on an estimate of the traversal times.) In these convex programs, the transition points or velocities are fixed, but the rest of the trajectory is optimized.

This observation motivates the method illustrated in Fig. 3 for solving problem: *Initialization (1st panel).* We compute a polygonal trajectory that connects the initial ${\mathbf{q}}_{init}$ and terminal point ${\mathbf{q}}_{term}$, and has short time duration. This is designed through a small number of convex programs.

*Fixed transition points (2nd panel).* We fix the transition points ${{\mathbf{q}}{(t_{1})}},\ldots,{{\mathbf{q}}{(t_{I - 1})}}$ of the polygonal trajectory, and use its traversal times $T_{1},\ldots,T_{I}$ to approximate the acceleration constraints. This leads to a convex subproblem that improves the polygonal trajectory.

*Fixed transition velocities (3rd panel).* We fix the transition velocities ${\overset{˙}{\mathbf{q}}{(t_{1})}},\ldots,{\overset{˙}{\mathbf{q}}{(t_{I - 1})}}$ of the improved trajectory, and use its traversal times $T_{1},\ldots,T_{I}$ to approximate the acceleration constraints. This leads to another convex subproblem that further improves our solution.

*Iterations (4th panel).* We keep refining our trajectory by solving the two convex subproblems in alternation.

*Termination (5th panel).* We terminate when the relative objective decrease of an iteration is smaller than a fixed tolerance $\varepsilon \in {(0,1\rbrack}$. The objective decrease is measured between any two consecutive subproblems of the same kind (fixed transition points or velocities).

Figure 3: Steps of SCS during the solution of the problem in Fig. 2. In the initialization (1st panel), we quickly compute a feasible polygonal trajectory. Then, we alternate between a convex subproblem with fixed transition points and one with fixed transition velocities (2nd to 4th panels). We terminate when the cost decrease of an iteration is small enough (5th panel). The trajectory computed at each iteration (solid blue) is overlaid on the trajectory from the previous iteration (dashed red).

The following sections detail our algorithm. We first illustrate the subproblem with fixed transition velocities, then the one with fixed transition points, and lastly the initialization step. This order simplifies the exposition, although it is the opposite order of how these steps appear in our algorithm.

## Subproblem with Fixed Transition Velocities

This section illustrates the convex subproblem with fixed transition velocities ${\overset{˙}{\mathbf{q}}{(t_{1})}},\ldots,{\overset{˙}{\mathbf{q}}{(t_{I - 1})}}$. First, we formulate problem as a more tractable nonconvex program. Then, we convexify this program by fixing the transition velocities and approximating the acceleration constraint (1g).

### IV-A Change of variables

We parameterize the trajectory within each safe set $\mathcal{Q}_{i}$ using a function ${\mathbf{q}}_{i}:{{\lbrack 0,1\rbrack}\rightarrow{\mathbb{R}}^{n}}$ and a scalar $T_{i} > 0$. These decide the trajectory shape and traversal time, respectively. We also define the function ${h_{i}{(t)}} = {{({t - t_{i - 1}})}/T_{i}}$ that maps the interval of time $\lbrack t_{i - 1},t_{i}\rbrack$ assigned to the set $\mathcal{Q}_{i}$ to the unit interval $\lbrack 0,1\rbrack$. This allows us to reconstruct our trajectory as for all $t \in {\lbrack t_{i - 1},t_{i}\rbrack}$ and $i \leq I$. By differentiating the last equality, we obtain the following expressions for the trajectory velocity and acceleration: which hold for all $t \in {\lbrack t_{i - 1},t_{i}\rbrack}$ and $i \leq I$.

### IV-B Nonconvex formulation

We express problem in terms of the new variables. The objective function (1a) simply becomes The boundary conditions in (1b) to (1d) become where in the last constraint we canceled the traversal times $T_{1}$ and $T_{I}$ since the right-hand side is zero. The next conditions ensure that the trajectory and its derivative are continuous: The constraints in (1e), (1f), and (1g) become where we multiplied both sides of the velocity and the acceleration constraints by $T_{i}$ and $T_{i}^{2}$, respectively. Finally, constraint (1h) results in where zero traversal times are excluded because of Assumption 1.

Overall, problem is reformulated as | | subject to | ${\text{(}\text{) to (}\text{)}},$ | | | with variables ${\mathbf{q}}_{i}$ and $T_{i}$ for $i \leq I$. The objective and most of the constraints of this problem are linear. The position constraint (5a) is convex. As mentioned in §I-B, also the velocity constraint (5b) is convex. On the other hand, the velocity continuity (4b) and the acceleration constraint (5c) are nonconvex. Therefore, the overall problem is nonconvex.

### IV-C Convex restriction

The next step is to construct a *convex restriction* (informally, a convex inner approximation \[9, §2.1\]) of the nonconvex constraints of problem. To do so, we assume that the transition velocities have fixed value, and that we are given nominal values ${\overline{T}}_{i} > 0$ for the traversal times $T_{i}$, for all $i \leq I$.

With the transition velocities fixed, the velocity-continuity constraints (4b) become linear: To approximate the acceleration constraint (5c), we underestimate the convex function $T_{i}^{2}$ with its linearization around the nominal value ${\overline{T}}_{i}$: We then replace (5c) with These constraints are convex (see again the discussion in §I-B). Moreover, they imply (5c) because of the inequality and the assumption that the constraint set $\mathcal{A}$ contains the origin.

Collecting all the pieces, we have the following convex restriction of problem: | | subject to | ${\text{(}\text{) to (}\text{) except (}\text{) and (}\text{)}},$ | | | | | | ${\text{(}\text{) and (}\text{)}}.$ | | | Constraint is omitted here since it is implied by (10b). Given a feasible trajectory with transition velocities ${\mathbf{v}}_{1},\ldots,{\mathbf{v}}_{I - 1}$ and traversal times ${\overline{T}}_{1},\ldots,{\overline{T}}_{I}$, this problem yields another feasible trajectory with lower or equal cost.

## Subproblem with Fixed Transition Points

We now illustrate the convex subproblem with fixed transition points ${{\mathbf{q}}{(t_{1})}},\ldots,{{\mathbf{q}}{(t_{I - 1})}}$. In the previous section, we parameterized the trajectory at the "position level" using the functions ${\mathbf{q}}_{i}$ for $i \leq I$. The velocity and acceleration were ${\overset{˙}{\mathbf{q}}}_{i}/T_{i}$ and ${\overset{¨}{\mathbf{q}}}_{i}/T_{i}^{2}$, respectively. This choice made all the position constraints convex, and gave us some nonconvex velocity and acceleration constraints. Here, we parameterize the trajectory at the "velocity level" using the functions ${\overset{˙}{\mathbf{r}}}_{i} = {{\overset{˙}{\mathbf{q}}}_{i}/T_{i}}$. We recover the position as $T_{i}{\mathbf{r}}_{i}$ and the acceleration as ${\overset{¨}{\mathbf{r}}}_{i}/T_{i}$. Furthermore, we work with the reciprocals $S_{i} = {1/T_{i}}$ of the traversal times. This yields a problem equivalent to where all the velocity constraints are convex, and the nonconvexities are only at the position and acceleration levels: Observe that the objective of this problem is still convex, even though we work with the traversal-time reciprocals. The only nonconvex constraints are the position continuity (12e) and the acceleration constraint (12i), which have the same structure as the constraints (4b) and (5c), respectively.

We proceed as in the previous section to construct a convex restriction of problem. This time we assume that the transition points are fixed: This makes the position continuity (12e) linear: To approximate the acceleration constraint (12i), we assume again that we are given nominal values ${\overline{T}}_{i} > 0$ of the traversal times. We underestimate the convex function $1/S_{i}$ with its linearization around the nominal point: This gives us the following convex restriction of the acceleration constraint: Overall, the subproblem with fixed transition points is | | subject to | ${\text{(}\text{) to (}\text{) except (}\text{) and (}\text{)}},$ | | | | | | ${\text{(}\text{) and (}\text{)}}.$ | | | This convex subproblem allows us to improve a given feasible trajectory with transition points ${\mathbf{p}}_{1},\ldots,{\mathbf{p}}_{I - 1}$ and traversal times ${\overline{T}}_{1},\ldots,{\overline{T}}_{I}$.

## Initialization with Polygonal Trajectory

In the initialization of SCS we quickly identify a low-cost feasible trajectory for problem. As in the proof of Proposition 1, a natural candidate for this role is a polygonal trajectory that comes to a full stop at each "kink."

The shape of our polygonal trajectory is computed through the following convex program: Here the decision variables are the points ${\mathbf{p}}_{0},\ldots,{\mathbf{p}}_{I}$ that the trajectory interpolates through straight lines (black dots in the first panel of Fig. 3). The objective minimizes the total Euclidean length of the trajectory.

Next, we select the *vertices* of the polygonal trajectory, i.e., the points ${\mathbf{p}}_{i}$ that do not lie on the line connecting ${\mathbf{p}}_{i - 1}$ to ${\mathbf{p}}_{i + 1}$. (This condition can be efficiently checked using the triangle inequality.) For ease of notation, we also include ${\mathbf{p}}_{0}$ and ${\mathbf{p}}_{I}$ in the list of vertices. As an example, in the top panel of Fig. 3, the only point that is not a vertex is ${\mathbf{p}}_{1}$ (the second).

The initialization is completed by connecting each pair of consecutive vertices through a minimum-time trajectory segment, with zero velocity at the endpoints. While these vertex-to-vertex problems could be solved in closed form when working with infinite-dimensional trajectories, in practice, we use a finite-dimensional trajectory parameterization, and it is convenient to formulate them as convex programs. To this end, let us assume that we are connecting two vertices that are consecutive points ${\mathbf{p}}_{i - 1}$ and ${\mathbf{p}}_{i}$. (If not, we can proceed as follows and, afterwards, split the designed trajectory into pieces.) The vertex-to-vertex problem can be formulated as a convex program similar to the nonconvex problem: The variables are the traversal time $T_{i}$, its reciprocal $S_{i}$, and the function ${\mathbf{r}}_{i}:{{\lbrack 0,1\rbrack}\rightarrow{\mathbb{R}}^{n}}$ (which represents ${\mathbf{q}}_{i}/T_{i}$). The last constraint relaxes the nonconvex equality $T_{i} = {1/S_{i}}$ to a convex inequality. However, this relaxation is lossless: in fact, given any feasible solution ${\overline{T}}_{i}$, ${\overline{S}}_{i}$, and ${\overline{\mathbf{r}}}_{i}$, the solution $T_{i} = {\overline{T}}_{i}$, $S_{i} = {1/{\overline{T}}_{i}}$, and ${\mathbf{r}}_{i} = {{\overline{\mathbf{r}}}_{i}/{({{\overline{T}}_{i}{\overline{S}}_{i}})}}$ is also feasible, has equal cost, and satisfies $T_{i} = {1/S_{i}}$. In practice, we solve problem as a one-dimensional problem, leveraging the fact that its optimal trajectories are straight lines. This accelerates our algorithm when working in high-dimensional spaces.

## Numerical Implementation

The numerical implementation of our method requires a finite-dimensional trajectory parameterization. In some special cases, it is possible to use a parameterization that captures the infinite-dimensional optimum of problem. However, in general, optimal trajectories can be quite complex, and some approximation error is unavoidable.

Bézier curves have been widely used in motion planning, and enjoy several properties that make them particularly well suited for our problems. In this section, we first collect some basic definitions and properties of Bézier curves, following \[28, §V-A\]. Then we show how the infinite-dimensional problems in the previous sections can be translated into efficient finite-dimensional programs.

### VII-A Bézier curves

Bézier curves are constructed using Bernstein polynomials. The *Bernstein polynomials* of degree $K$ are defined over the interval ${\lbrack 0,1\rbrack} \subset {\mathbb{R}}$ as follows: (Recall that in this paper $k$ is nonnegative and $k \leq K$ is shorthand for $k \in {\{ 0,\ldots,K\}}$.) The Bernstein polynomials are nonnegative and, by the binomial theorem, sum up to one. Therefore, the scalars ${\beta_{0}{(s)}},\ldots,{\beta_{K}{(s)}}$ represent the coefficients of a convex combination for all $s \in {\lbrack 0,1\rbrack}$. We use these coefficients to combine a given set of *control points* ${{\mathbf{γ}}_{0},\ldots,{\mathbf{γ}}_{K}} \in {\mathbb{R}}^{n}$, and obtain a *Bézier curve*: The function ${\mathbf{γ}}:{{\lbrack 0,1\rbrack}\rightarrow{\mathbb{R}}^{n}}$ is a (vector-valued) polynomial of degree $K$. Fig. 4 shows a Bézier curve of degree $K = 4$ in $n = 2$ dimensions.

Figure 4: A two-dimensional Bézier curve with control points γ0, …, γ4. The area shaded in yellow is the convex hull of the control points.

The following are a few selected properties of Bézier curves. We refer to for a more comprehensive list.

### Property 1 (Derivative)

The derivative $\overset{˙}{\gamma}$ of the Bézier curve $\mathbf{γ}$ is a Bézier curve of degree $K - 1$. Its control points are computed via the linear difference equation

### Property 2 (Endpoint)

The Bézier curve $\mathbf{γ}$ starts at its first control point and ends at its last control point:

### Property 3 (Convex hull)

The Bézier curve $\mathbf{γ}$ is contained in the convex hull of its control points at all times: This convex hull is shaded in yellow in Fig. 4.

### VII-B Finite-dimensional trajectory parameterization

When solving the programs, and numerically, we restrict our trajectory segments (${\mathbf{q}}_{i}$ or ${\mathbf{r}}_{i}$) to Bézier curves of degree $K$, and enforce all the necessary constraints leveraging the properties above. Property 1. ‣ VII-A Bézier curves ‣ VII Numerical Implementation ‣ A Biconvex Method for Minimum-Time Motion Planning Through Sequences of Convex Sets") tells us that the trajectory velocity and acceleration are also piecewise Bézier curves, of degree $K - 1$ and $K - 2$, respectively. Using Property 2. ‣ VII-A Bézier curves ‣ VII Numerical Implementation ‣ A Biconvex Method for Minimum-Time Motion Planning Through Sequences of Convex Sets"), we can then easily enforce any boundary or continuity condition by constraining the first and last control points of our Bézier curves. The containment of a trajectory segment (or its derivatives) in a convex set can be enforced using Property 3. ‣ VII-A Bézier curves ‣ VII Numerical Implementation ‣ A Biconvex Method for Minimum-Time Motion Planning Through Sequences of Convex Sets"): if all the control points of a Bézier curve lie in a convex set, then so does the whole curve. In the initialization step, we might also have to split a trajectory segment, obtained by solving problem, into multiple pieces. This is easily done by using De Casteljau's algorithm \[10, §2.4\].

For completeness, in §A, we report the finite-dimensional versions of the convex programs and. We also report the finite-dimensional version of the nonconvex program, which will serve as a baseline in the experiments below.

## Strengths

This section illustrates the main strengths of SCS.

### VIII-A Convergence and completeness

Under our assumptions on the problem data, SCS is guaranteed to converge monotonically. In fact, the initialization step must succeed, since problems and are feasible and admit an optimal solution. Then, the convex subproblems and are guaranteed to produce trajectories that are not worse than the ones they are initialized . This makes our algorithm *complete* (guaranteed to find a solution) and *anytime* (returns a feasible solution even if stopped early).

These results extend to the finite-dimensional implementation of SCS from §VII, provided that our Bézier curves have degree $K \geq 3$. This minimum degree is sufficient for our trajectory segments to represent straight lines with zero endpoint velocity, and ensures the success of the initialization step. After that, the biconvex alternation can only improve our finite-dimensional trajectory. Notably, our piecewise Bézier trajectories satisfy the constraints of problem at all continuous times, rather than at a finite set of times, as is common for sampling-based and trajectory-optimization methods.

### VIII-B Optimality

SCS is *heuristic*: it is not guaranteed to find an optimal solution (global or local), or to converge within a fixed distance from one. However, it typically finds high-quality trajectories in a fraction of the time of state-of-the-art solvers (see the experiments in §X-B). The trajectory parameterization using Bézier curves can also affect the optimality of our trajectories. In this direction, we remark that a Bézier curve is as expressive as any polynomial of equal degree \[10, §1.3\]. Another source of suboptimality are the conservative convex constraints obtained using Property 3. ‣ VII-A Bézier curves ‣ VII Numerical Implementation ‣ A Biconvex Method for Minimum-Time Motion Planning Through Sequences of Convex Sets"). However, these constraints get arbitrarily accurate as the degree $K$ increases. Potentially, we could also use exact containment conditions like sums of squares, but this would make our programs much more expensive to solve.

### VIII-C Computational efficiency

The runtime of an iteration of SCS is polynomial in all the relevant problem data, and linear in the number $I$ of safe sets and the degree $K$ of the Bézier curves. In fact, the subproblems and have banded structure, and are solvable in a time that is linear in $I$ and $K$ (see, e.g., ). Problems and are also banded, and solvable in a time that is linear in $I$ and $K$, respectively. In addition, the latter problem is solved at most $I$ times.

The overall time complexity of SCS is harder to quantify. However, in practice, we observed that the number of iterations necessary for convergence is often insensitive to $I$ and $K$ (see the experiments in §X-B). This leads to overall runtimes that are often linear in $I$ and $K$.

### VIII-D Limited parameter tuning

SCS does not require the tuning of any step-size or trust-region parameter. The only numerical values set by the user are the degree $K$ of the Bézier curves and the convergence tolerance $\varepsilon$. The first should be at least three to ensure convergence, and can be increased to improve the solution quality. For the second, we have found that $\varepsilon = 0.01$ is sufficiently small for most problems.

### VIII-E Advantages over existing methods

As discussed in §I, SCS addresses a problem similar to the one in \[28, §V\]. Compared to that approach, SCS applies to a narrower set of motion-planning problems, but converges much faster (see experiments in §X-C). This is because its subproblems are convex restrictions of the original nonconvex program, and at every iteration we can take a full step towards their optima.

The GCS motion planner from requires a convex trajectory parameterization within each safe set. However, as also seen in this paper, this is very challenging when we optimize both the trajectory shape and timing, and imposes strict limitations on the types of costs and constraints that GCS can handle. For instance, the method in can only enforce coarse approximations of the acceleration constraints (1g). The recent work proposes a semidefinite relaxation for these time-scaling problems, broadening the list of costs and constraints that GCS can accommodate but sacrificing the algorithm completeness. Overall, GCS and SCS can be viewed as complementary methods, and can be combined in hybrid approaches where GCS provides an approximate solution to the high-level discrete-continuous problem and SCS refines the trajectory within a fixed sequence of safe sets.

Optimization problems similar to the one considered in this paper are also faced by UAV motion planners based on safe flight corridors. However, these planners typically bypass the problem nonconvexity by fixing the corridor traversal times using heuristics, while here we optimize these times explicitly.

The main advantage of SCS over general-purpose methods for trajectory optimization is its reliability and completeness. Furthermore, SCS can generate high-quality trajectories for complex planning problems within a few milliseconds (see §X-C). In contrast, trajectory-optimization methods require a GPU to achieve comparable runtimes. Finally, most common trajectory-optimization methods do not take full advantage of the structure of minimum-time problems.

The minimum-distance problem, solved to initialize SCS, is similar to the problem addressed by common sampling-based methods. This step is straightforward for us since we assume that the free space is represented as a sequence of convex sets. Contrarily, sampling-based methods rely solely on a collision checker, which makes finding a minimum-distance curve significantly more challenging. The work explores a combined approach, where a sampling-based method is used to find a polygonal curve that is later inflated into a sequence of safe sets for SCS to plan through.

Finally, various convex relaxations and reformulations of time-optimal control and trajectory-tracking problems have been proposed over the years (see, e.g., ). However, none of these methods applies directly to the problem of designing trajectories through sequences of convex sets.

## Limitations

Our method has a few worth-noting limitations. First of all, SCS is restricted to minimum-time problems. However, a similar approach can be applied to problems with fixed final time and cost function that penalizes the magnitude of the trajectory velocity and acceleration.

SCS requires that the robot free space is described as a sequence of convex sets. This description can be challenging to compute for high-dimensional problems and cluttered environments. However, as mentioned in §I, many practical methods for decomposing complex spaces into convex sets are now available, and also GPU-based algorithms have been recently developed.

The trajectories generated by SCS may have acceleration jumps, which can make them difficult to track on real hardware. A simple workaround is to add a smoothing step. Alternatively, we can ensure that the trajectory acceleration (as well as any higher-order derivative) is continuous by setting it to zero at the transition times. This is easily seen to be a linear constraint. A similar limitation is that SCS can only handle constraints on the velocity and acceleration but not, for example, on the trajectory jerk.

We have seen that SCS cannot handle problems where an optimal traversal time $T_{i}$ is zero (in which case the corresponding variable $S_{i}$ in the subproblem with fixed transition points is infinity). Although Assumption 1 is sufficient to rule out this scenario, some practically relevant problems do not meet this assumption. In these cases, we can enforce an artificial lower bound on the time spent in each safe set.

## Numerical Experiments

We demonstrate SCS on three numerical experiments. First, we conclude the simple running example in Fig. 2 and 3 by reporting its solution statistics. Second, we analyze the performance of SCS as a function of multiple problem data, and we compare it with state-of-the-art solvers for nonconvex optimization. Finally, we demonstrate SCS on a minimum-time package-transfer problem with two Sparrow robots, and we benchmark it against other motion-planning methods.

The Python implementation of SCS used in the experiments below is available at It is based on Drake, and uses the open-source solver Clarabel for the convex programs. All the experiments are run on a laptop with Apple M2 Pro processor and 16 GB of RAM. The solvers SNOPT and IPOPT are also called through Drake's Python interface (and are warm started with the same polygonal trajectory as SCS).

### X-A Running example

We provide here the details of the running example illustrated in Fig. 2. The initial and terminal points are ${\mathbf{q}}_{init} = {}$ and ${\mathbf{q}}_{term} = {(10,1.5)}$, respectively. The geometry of the safe sets can be deduced from the figure. The constraint sets $\mathcal{V}$ and $\mathcal{A}$ are circles centered at the origin of radius $10$ and $1$, respectively. The trajectory in Fig. 2 has time duration $T = 7.45$, and is designed by SCS with degree $K = 5$ and termination tolerance $\varepsilon = 0.01$.

The curves in Fig. 3 represent the actual iterations of SCS. The initial polygonal trajectory has time duration $T = 12.49$ (1st panel). This value decreases to $8.82$ in the first subproblem with fixed transition points (2nd panel), then to $8.06$ and $7.51$ in the subsequent subproblems (3rd and 4th panels). SCS converges after solving only five subproblems.

As a baseline for SCS, we solve the finite-dimensional version of the nonconvex program with SNOPT and IPOPT. This problem is stated in §A, see, and uses the same trajectory parameterization as SCS. Both solvers yield the trajectory duration $T = 7.40$, which is only $0.7\%$ shorter than ours. Our simple Python implementation of SCS takes $10$ ms to converge, while SNOPT takes $21$ ms and IPOPT needs $261$ ms. Note, however, that these solvers use smaller termination tolerances than SCS. Increasing the optimality tolerances of the nonconvex solvers does not reduce their runtimes significantly. Conversely, if we decrease the SCS tolerance to, e.g., $\varepsilon = 10^{- 4}$, the objective gap between SCS and the nonconvex solvers decreases to $0.1\%$, but the runtime of SCS increases to $50$ ms. This is typical for multi-convex methods: they find high-quality solutions quickly, but can be slow if we seek very accurate solutions.

### X-B Runtime analysis and comparison with nonconvex solvers

We analyze the runtimes of SCS, SNOPT, and IPOPT as functions of several problem parameters: the number $I$ of safe sets, the number $m$ of facets of each safe set, the space dimension $n$, and the trajectory degree $K$. We show that, across a wide range of problem instances, SCS finds low-cost trajectories more quickly and reliably than the two state-of-the-art solvers.

We construct an instance of problem where each safe set $\mathcal{Q}_{i}$ represents one link of an $n$-dimensional staircase. The safe sets are polytopes that approximate ellipsoids with increasing accuracy as their number $m$ of facets grows. Fig. 5 shows an instance of this problem with the corresponding optimal trajectory. In this instance, we have $I = 5$ safe sets in $n = 2$ dimensions, and each set has $m = 4$ facets (rectangular safe sets). More details on the construction of these problems are reported in §B.

Figure 5: Benchmark problem with I = 5 safe sets in n = 2 dimensions, with m = 4 facets each. The optimal trajectory is shown in blue.

We consider a first batch of instances where we let the number $I$ of safe sets grow from $3$ to $3000$, while we fix the space dimension to $n = 3$, the number of facets to $m = 6$, and the trajectory degree to $K = 3$. The top panel of Fig. 6 shows the runtimes of SCS, SNOPT, and IPOPT. The two nonconvex solvers return trajectories with equal cost, when SNOPT does not fail or reach our time limit of $1$ h (missing markers in the figure). SCS designs trajectories that have slightly higher cost ($1.2\%$ in the worst case). SCS is faster in almost all instances: SNOPT and IPOPT have comparable runtimes only on the smallest and largest problems, respectively. The runtimes of SCS increase a little more than linearly: as the number of safe sets grows by a factor of $1000$, its runtimes increase by $3060$. The number of subproblems necessary for SCS to converge with tolerance $\varepsilon = 0.01$ ranges between $5$ and $8$.

Figure 6: Comparison of SCS with the solvers SNOPT and IPOPT. The runtimes of the three methods are analyzed as functions of multiple problem data. Missing markers correspond to solver failures. The runtimes of SCS grow almost linearly in each experiment (note that the horizontal axis has logarithmic scale in the first two panels and linear scale in the last two).

The second panel in Fig. 6 shows the effects of increasing the number $m$ of facets of the safe sets from $3$ to $3000$, while keeping $I = 20$, $n = 2$, and $K = 5$. In this case, SCS and the nonconvex solvers find identical trajectories (despite the larger termination tolerance of SCS). SCS solves each problem much faster than SNOPT and IPOPT, and its runtimes increase sublinearly with $m$ (as the number of facets grows by $1000$, the runtime grows by $210$). The number of subproblems necessary for SCS to converge is equal to $5$ for every value of $m$.

In the third panel of Fig. 6, we let the space dimension $n$ grow from $2$ to $20$, while we set $I = 20$, $m = {2n}$, and $K = 3$. The nonconvex solvers find again identical trajectories, and SCS has a maximum cost gap of $3.2\%$. SCS is again the fastest, and its runtimes increase a little more than linearly with $n$ (the space dimension grows by $10$ and the runtimes by $17.6$). The number of SCS subproblems ranges between $5$ and $16$.

In the fourth panel of Fig. 6, we let $I = 20$, $m = 6$, $n = 3$, and increase the degree $K$ from $3$ to $30$. All the methods return similar trajectories: the maximum cost difference between SCS and the nonconvex solvers is $0.4\%$. SCS is the fastest and its runtimes grow linearly with $K$ (the degree increases by $10$ and the runtimes by $9.9$). IPOPT performs better than SNOPT, which also fails in one instance. SCS always converges after $5$ subproblems.

### X-C Minimum-time package transfer with two Sparrow robots

We use SCS to plan the motion of two Sparrow robots that transfer packages between bins in simulation. We also benchmark SCS against the trust-region method proposed in \[28, §V\], as well as a simple waypoint-based motion planner representative of those commonly used in industry.

The package-transfer task is illustrated in Fig. 7. The two robots face each other, and between them is a table with two bins. One bin contains ten packages and the other is empty. The goal is to move all the packages in the first bin to the second as quickly as possible. The final package positions in the second bin must mirror the initial positions in the first bin. Packages are represented as axis-aligned boxes (these can be the packages themselves, or bounding boxes of products with more complex shape). The bins have side $0.6$ and height $0.3$, and the distance between their centers is $1$. The package sides are drawn uniformly at random between $0.1$ and $0.25$. Also the initial package positions are drawn uniformly at random within the corresponding bin, and sampled packages are rejected when they collide with existing packages.

Figure 7: Sparrow robots that move packages between bins in minimum time.

Figure 8: Two-dimensional illustration of the three-dimensional safe sets 𝒬i used for the package-transfer task. The top panel shows the sets for picking the rightmost package. The bottom panel shows the sets for its placement. The latter are shrunk to avoid the collision of the transported package.

We solve the task using a state machine. At each iteration, if a robot has completed its previous pick or place motion, we plan its next motion neglecting the presence of the other robot. If this results in a collision, we let the robot idle until the next iteration. If the state machine stalls (neither arm can execute its motion without colliding with the other), we retract one arm and allow the other to move. Each time a robot plans a picking motion, it targets the package closest to its side of the table. Trajectories are planned directly in the three-dimensional task space, and the full robot configuration is retrieved through inverse kinematics. We let the sets $\mathcal{V}$ and $\mathcal{A}$, that constrain the gripper velocity and acceleration, be spheres of radius $10$ centered at the origin. (In practice, these sets can be shaped to prevent package delamination, and ensure that the robots can track the designed task-space trajectories.) We use Bézier curves of degree $K = 5$ and set the termination tolerance to $\varepsilon = 0.01$.

For each pick and place motion, the three-dimensional task space is decomposed into five box-shaped safe sets $\mathcal{Q}_{i}$, illustrated in two dimensions in Fig. 8. The first and fifth sets allow the gripper to reach the trajectory endpoints, without colliding with the packages in the bins. The second and fourth sets cover the space above the packages in the two bins. The third is a transfer region that connects the spaces above the bins. As shown in the bottom panel of Fig. 8, these sets are shrunk during a place motion to avoid collisions of the transported package (packages are always picked above their centers).

We consider $50$ randomly generated package-transfer problems. As the low-level motion planner for the state machine just described, we compare SCS against the following alternatives: The trust-region method from \[28, §V\], modified as described in §C to deal with minimum-time problems.

A simple waypoint-based motion planner, which lifts a package vertically, moves it horizontally above the desired destination, and places it down. Where each trajectory segment is executed in minimum time.

The three methods use the same constraints and trajectory parameterization. The first two share also the same initialization strategy and termination tolerance. Tab. I shows the statistics for the task-completion time and the runtime of each motion planner. SCS generates the best trajectories: in fact, the average completion time for the overall package-transfer task is about $10$ s for SCS, $13$ s for the trust-region method, and $15$ s for the waypoint-based planner. In other words, SCS allows us to transfer $28\%$ and $50\%$ more packages per unit of time than the trust-region and the waypoint-based planners, respectively. The runtimes of SCS are approximately five times longer than those of the waypoint-based planner, but they remain very low for practical use. The trust region method is roughly three times slower than SCS. The videos of five of these package-transfer tasks are provided as Supplementary Material.

TABLE I: Package-Transfer Benchmark We conclude by emphasizing that the trust-region and the waypoint-based planners are natural baselines for the task considered in this section. The first provides the same completeness guarantees as SCS, designs smooth trajectories, and has relatively low runtimes. The second is widespread in warehouse automation thanks to its good performance and high reliability. In our experience, off-the-shelf nonconvex trajectory optimization faces significant challenges with this package-transfer task: it struggles with the many collision geometries in Fig. 7, relies on handcrafted warm starts, can take seconds to converge (unless we use accelerated hardware), and can also fail to converge. Sampling-based planners can be more reliable, but generate polygonal curves that require additional smoothing. They excel in tasks where finding a collision-free trajectory is the main challenge, and trajectory cost is secondary. However, our package-transfer task presents the opposite challenge.
