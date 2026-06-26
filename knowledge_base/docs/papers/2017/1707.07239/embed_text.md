## Introduction

Time-Optimal Path Parameterization (TOPP) is the problem of finding the fastest way to traverse a path in the configuration space of a robot system while respecting the system constraints. This classical problem has a wide range of applications in robotics. In many industrial processes (cutting, welding, machining, 3D printing, etc.) or mobile robotics applications (driverless cars, warehouse UGVs, aircraft taxiing, etc.), the robot paths may be predefined, and optimal productivity implies tracking those paths at the highest possible speed while respecting the process and robot constraints. From a conceptual viewpoint, TOPP has been used extensively as subroutine to kinodynamic motion planning algorithms. Because of its practical and theoretical importance, TOPP has received considerable attention since its inception in the 1980's, see for a recent review.

### Existing approaches to TOPP

There are two main families of methods to TOPP, based respectively on Numerical Integration (NI) and Convex Optimization (CO). Each approach has its strengths and weaknesses.

The NI-based approach was initiated , and further improved and extended by many researchers, see for a review. NI-based algorithms are based on Pontryagin's Maximum Principle, which states that the time-optimal path parameterization consists of alternatively maximally accelerating and decelerating segments. The key advantage of this approach is that the optimal controls can be explicitly computed (and not searched for as in the CO approach) at each path position, resulting in extremely fast implementations. However, this requires finding the switch points between accelerating and decelerating segments, which constitutes a major implementation difficulty as well as the main cause of failure. Another notable implementation difficulty is handling of velocity bounds ^11^1In a NI-based algorithm, to account for velocity bounds, one has to compute the direct Maximum Velocity Curve ${MVC}_{direct}$, then find and resolve "trap points". Implementing this procedure is tricky in practice because of accumulating numerical errors. This observation comes from our own experience with the TOPP library.. The formulation of the present paper naturally removes those two difficulties.

The CO-based approach was initiated by and further extended . This approach formulates TOPP as a single large convex optimization program, whose optimization variables are the accelerations and squared velocities at discretized positions along the path. The main advantages of this approach are: (i) it is simple to implement and robust, as one can use off-the-shelf convex optimization packages; (ii) other convex objectives than traversal time can be considered. On the downside, the optimization program to solve is huge -- the number of variables and constraint inequalities scale with the discretization step size -- resulting in implementations that are one order of magnitude slower than NI-based methods. This makes CO-based methods inappropriate for online motion planning or as subroutine to kinodynamic motion planners.

Figure 1: Time-Optimal Path Parameterization by Reachability Analysis (TOPP-RA) computes the optimal parameterization in two passes. In the first pass (backward), starting from the last grid point N, the algorithm computes controllable sets (red intervals) recursively. In the second pass (forward), starting now from grid point 0, the algorithm greedily selects the highest controls such that resulting velocities remain inside the respective controllable sets.

### Proposed new approach based on Reachability Analysis

In this paper, we propose a new approach to TOPP based on Reachability Analysis (RA), a standard notion from control theory. The key insight is: given an interval of squared velocities ${\mathbb{I}}_{s}$ at some position $s$ on the path, the *reachable* set ${\mathbb{I}}_{s + \Delta}$ (the set of all squared velocities at the next path position that can be reached from ${\mathbb{I}}_{s}$ following admissible controls) and the *controllable* set ${\mathbb{I}}_{s - \Delta}$ (the set of all squared velocities at the previous path position such that there exists an admissible control leading to a velocity in ${\mathbb{I}}_{s}$) can be computed quickly and robustly by solving a few *small* Linear Programs (LPs). By recursively computing controllable sets at discretized positions on the path, one can then extract the time-optimal parameterization in time $O{({mN})}$, where $m$ is the number of constraint inequalities and $N$ the discretization grid size, see Fig. 1 for an illustration.

As compared to NI-based methods, the proposed approach has therefore a better time complexity (actual computation time is similar for problem instances with few constraints, and becomes significantly faster for instances with $> 22$ constraints). More importantly, the proposed method is much easier to implement and has a success rate of $100\%$, while state-of-the-art NI-based implementations (e.g. ) comprise thousands of lines of code and still report failures on hard problem instances. As compared to CO-based methods, the proposed approach enjoys the same level of robustness and of ease-of-implementation while being significantly faster.

Besides the gains in implementation robustness and performance, viewing the classical TOPP problem from the proposed new perspective yields the following additional benefits: constraints for redundantly-actuated systems are handled natively: there is no need to project the constraints to the plane (path acceleration $\times$ control) at each path position, as done; Admissible Velocity Propagation, a recent concept for kinodynamic motion planning (see Section VI-A for a brief summary), can be derived "for free"; robustness to parametric uncertainty, e.g. uncertain coefficients of friction or uncertain inertia matrices, can be obtained in a natural way.

More details regarding the benefits as well as definitions of relevant concepts will be given in Section VI.

### Organization of the paper

The rest of the paper is organized as follows. Section II formulates the TOPP problem in a general setting. Section III applies Reachability Analysis to the path-projected dynamics. Section IV presents the core algorithm to compute the time-optimal path parameterization. Section V reports extensive experimental results to demonstrate the gains in robustness and performance permitted by the new approach. Section VI discusses the additional benefits mentioned previously: Admissible Velocity Propagation and robustness to parametric uncertainty. Finally, Section VII offers some concluding remarks and directions for future research.

## Problem formulation

### II-A Generalized constraints

Consider a $n$-dof robot system, whose configuration is denoted by a $n$ dimensional vector $\mathbf{q} \in {\mathbb{R}}^{n}$. A *geometric path* $\mathcal{P}$ in the configuration space is represented as a function $\mathbf{q}{(s)}_{s \in {\lbrack 0,s_{end}\rbrack}}$. We assume that $\mathbf{q}{(s)}$ is piece-wise $\mathcal{C}^{2}$-continuous. A *time parameterization* is a piece-wise $\mathcal{C}^{2}$, increasing scalar function $s:{{\lbrack 0,T\rbrack}\rightarrow{\lbrack 0,s_{end}\rbrack}}$, from which a *trajectory* is recovered as $\mathbf{q}{({s{(t)}})}_{t \in {\lbrack 0,T\rbrack}}$.

In this paper, we consider *generalized second-order constraints* of the following form $\mathbf{A},\mathbf{B},\mathbf{f}$ are continuous mappings from ${\mathbb{R}}^{n}$ to ${\mathbb{R}}^{m \times n},{\mathbb{R}}^{n \times m \times n}$ and ${\mathbb{R}}^{m}$ respectively; $\mathcal{C}{(\mathbf{q})}$ is a convex polytope in ${\mathbb{R}}^{m}$.

### Implementation remark 1

The above form is the most general in the TOPP literature to date, and can account for many types of kinodynamic constraints, including velocity and acceleration bounds, joint torque bounds for fully- or redundantly-actuated robots, contact stability under Coulomb friction model, etc.

Consider for instance the torque bounds on a fully-actuated manipulator This can be rewritten in the form of with $\mathbf{A}:=\mathbf{M}$, $\mathbf{B}:=\mathbf{C}$, $\mathbf{f}:=\mathbf{g}$ and which is clearly convex.

For redundantly-actuated manipulators, it was shown that the TOPP problem can also be formulated in the form of with where $\mathbf{S}$ is a linear transformation, which implies that the so-defined $\mathcal{C}{(\mathbf{q})}$ is a convex polytope.

In legged robots, the TOPP problem under contact-stability constraints where the friction cones are linearized was shown to be reducible to the form of with $\mathcal{C}{(\mathbf{q})}$ being also a *convex polytope*.

If the friction cones are not linearized, then $\mathcal{C}{(\mathbf{q})}$ is still convex, but not polytopic. The developments in the present paper that concern reachable and controllable sets (Section III) are still valid in the convex, non-polytopic case. The developments on time-optimality (Section IV) is however only applicable to the polytopic case. ∎ Finally, we also consider first-order constraints of the form where the coefficients are matrices of appropriate sizes and $\mathcal{C}^{v}{(\mathbf{q})}$ is a convex set. Direct velocity bounds and momentum bounds are examples of first-order constraints.

### II-B Projecting the constraints on the path

Differentiating successively $\mathbf{q}{(s)}$, one has where $\square'$ denotes differentiation with respect to the path parameter $s$. From now, we shall refer to $s,\overset{˙}{s},\overset{¨}{s}$ as the position, velocity and acceleration respectively.

Substituting Eq. to Eq., one transforms second-order constraints on the system dynamics into constraints on $s,\overset{˙}{s},\overset{¨}{s}$ as follows Similarly, first-order constraints are transformed into

### II-C Path discretization

As in the CO-based approach, we divide the interval $\lbrack 0,s_{end}\rbrack$ into $N$ segments and $N + 1$ grid points Denote by $u_{i}$ the constant path acceleration over the interval $\lbrack s_{i},s_{i + 1}\rbrack$ and by $x_{i}$ the squared velocity ${\overset{˙}{s}}_{i}^{2}$ at $s_{i}$. By simple algebraic manipulations, one can show that the following relation holds where $\Delta_{i}:={s_{i + 1} - s_{i}}$. In the sequel we refer to $s_{i}$ as the $i$-stage, $u_{i}$ and $x_{i}$ as respectively the control and state at the $i$-stage. Any sequence $x_{0},u_{0},\ldots,x_{N - 1},u_{N - 1},x_{N}$ that satisfies the linear relation is referred to as a path parameterization.

A parameterization is *admissible* if it satisfies the constraints at every points in $\lbrack 0,s_{end}\rbrack$. One possible way to bring this requirement into the discrete setting is through a *collocation* discretization scheme: for each position $s_{i}$, one evaluates the continuous constraints and requires the control and state $u_{i},x_{i}$ to verify where ${\mathbf{a}_{i}:={\mathbf{a}{(s_{i})}}},{{\mathbf{b}_{i}:={\mathbf{b}{(s_{i})}}},{{\mathbf{c}_{i}:={\mathbf{c}{(s_{i})}}},{\mathcal{C}_{i}:={\mathcal{C}{(s_{i})}}}}}$.

Since the constraints are enforced only at a finite number of points, the actual continuous constraints might not be respected everywhere along $\lbrack 0,s_{end}\rbrack$ ^22^2This limitation is however not specific to the proposed approach as both the NI and CO approaches require discretization at some stages of the algorithm.. Therefore, it is important to bound the constraint satisfaction error. We show in Appendix -D that the collocation scheme has an error of order $O{(\Delta_{i})}$. Appendix -D also presents a first-order interpolation discretization scheme, which has an error of order $O{(\Delta_{i}^{2})}$ but which involves more variables and inequality constraints than the collocation scheme.

## Reachability Analysis of the path-projected dynamics

The key to our analysis is that the "path-projected dynamics", is a *discrete-time linear system* with *linear control-state inequality constraints*. This observation immediately allows us to take advantage of the set-membership control problems studied in the Model Predictive Control (MPC) literature.

### III-A Admissible states and controls

We first need some definitions. Denote the $i$-stage set of *admissible* control-state pairs by One can see $\Omega_{i}$ as the projection of $\mathcal{C}_{i}$ on the $(\overset{¨}{s},{\overset{˙}{s}}^{2})$ plane. Since $\mathcal{C}_{i}$ is a polytope, $\Omega_{i}$ is a *polygon*. Algorithmically, the projection can be obtained by e.g. the recursive expansion algorithm.

Next, the $i$-stage set of *admissible states* is the projection of $\Omega_{i}$ on the second axis The $i$-stage set of *admissible controls* given a state $x$ is Note that, since $\Omega_{i}$ is convex, both $\mathcal{X}_{i}$ and $\mathcal{U}_{i}{(x)}$ are *intervals*.

Classic terminologies in the TOPP literature (e.g. Maximum Velocity Curve, $\alpha$ and $\beta$ acceleration fields, etc.) can be conveniently expressed using these definitions. See the first part of Appendix -A for more details.

### Implementation remark 2

For redundantly-actuated manipulators and contact-stability of legged robots, both NI-based and CO-based methods must compute $\Omega_{i}$ at each discretized position $i$ along the path, which is costly. Our proposed approach avoids performing this 2D projection: instead, it will only require a few 1D projections per discretization step. Furthermore, each of these 1D projections amounts to a pair of LPs and can therefore be performed extremely quickly. ∎

### III-B Reachable sets

The key notion in Reachability Analysis is that of $i$-stage reachable set.

### Definition 1 ($i$-stage reachable set)

Consider a set of starting states ${\mathbb{I}}_{0}$. The *$i$-stage reachable set* $\mathcal{L}_{i}{({\mathbb{I}}_{0})}$ is the set of states $x \in \mathcal{X}_{i}$ such that there exist a state $x_{0} \in {\mathbb{I}}_{0}$ and a sequence of admissible controls $u_{0},\ldots,u_{i - 1}$ that steers the system from $x_{0}$ to $x$. ∎ To compute the $i$-stage reachable set, one needs the following intermediate representation.

### Definition 2 (Reach set)

Consider a set of states $\mathbb{I}$. The *reach set* $\mathcal{R}_{i}{({\mathbb{I}})}$ is the set of states $x \in \mathcal{X}_{i + 1}$ such that there exist a state $\overset{\sim}{x} \in {\mathbb{I}}$ and an admissible control $u \in {\mathcal{U}_{i}{(\overset{\sim}{x})}}$ that steers the system from $\overset{\sim}{x}$ to $x$, i.e.

### Implementation remark 3

Let us note ${\Omega_{i}{({\mathbb{I}})}}:={\{{{(u,\overset{\sim}{x})} \in \Omega_{i}}\mid{\overset{\sim}{x} \in {\mathbb{I}}}\}}$. If $\mathbb{I}$ is convex, then $\Omega_{i}{({\mathbb{I}})}$ is convex as the intersection of two convex sets. Next, $\mathcal{R}_{i}{({\mathbb{I}})}$ can be seen as the intersection of the projection of $\Omega_{i}{({\mathbb{I}})}$ onto a line and the interval $\mathcal{X}_{i + 1}$. Thus, $\mathcal{R}_{i}{({\mathbb{I}})}$ is an interval, hence defined by its lower and upper bounds $(x^{-},x^{+})$, which can be computed as follows Since $\Omega_{i}{({\mathbb{I}})}$ is a polygon, the above equations constitute two LPs. Note finally that there is no need to compute explicitly $\Omega_{i}{({\mathbb{I}})}$, since one can write directly and similarly for $x^{-}$. ∎ The $i$-stage reachable set can be recursively computed by

### Implementation remark 4

If ${\mathbb{I}}_{0}$ is an interval, then by recursion and by application of Implementation remark 3, all the $\mathcal{L}_{i}$ are intervals. Each step of the recursion requires solving two LPs for computing $\mathcal{R}_{i - 1}{({\mathcal{L}_{i - 1}{({\mathbb{I}}_{0})}})}$. Therefore, $\mathcal{L}_{i}$ can be computed by solving ${2i} + 2$ LPs. ∎ The $i$-stage reachable set may be empty, which implies that the system can not evolve without violating constraints: the path is not time-parameterizable. One can also note that

### III-C Controllable sets

Controllability is the dual notion of reachability, as made clear by the following definitions.

### Definition 3 ($i$-stage controllable set)

Consider a set of desired ending states ${\mathbb{I}}_{N}$. The *$i$-stage controllable set* $\mathcal{K}_{i}{({\mathbb{I}}_{N})}$ is the set of states $x \in \mathcal{X}_{i}$ such that there exist a state $x_{N} \in {\mathbb{I}}_{N}$ and a sequence of admissible controls $u_{i},\ldots,u_{N - 1}$ that steers the system from $x$ to $x_{N}$. ∎ The dual notion of "reach set" is that of "one-step" set.

### Definition 4 (One-step set)

Consider a set of states $\mathbb{I}$. The *one-step set* $\mathcal{Q}_{i}{({\mathbb{I}})}$ is the set of states $x \in \mathcal{X}_{i}$ such that there exist a state $\overset{\sim}{x} \in {\mathbb{I}}$ and an admissible control $u \in {\mathcal{U}_{i}{(x)}}$ that steers the system from $x$ to $\overset{\sim}{x}$, i.e.

The $i$-stage controllable set can now be computed recursively by | | $\mathcal{K}_{N}{({\mathbb{I}}_{N})}$ | ${= {{\mathbb{I}}_{N} \cap \mathcal{X}_{N}}},$ | | \(10\) | | | $\mathcal{K}_{i}{({\mathbb{I}}_{N})}$ | ${= {\mathcal{Q}_{i}{({\mathcal{K}_{i + 1}{({\mathbb{I}}_{N})}})}}}.$ | | |

### Implementation remark 5

Similar to Implementation remark 4, every one-step set $\mathcal{Q}_{i}{({\mathbb{I}})}$ is an interval, whose lower and upper bounds $(x^{-},x^{+})$ are given by the following two LPs and similarly for $x^{-}$. Thus, computing the $i$-stage controllable set will require solving ${2{({N - i})}} + 2$ LPs. ∎ The $i$-stage controllable set may be empty, in that case, the path is not time-parameterizable. One also has

## TOPP by Reachability Analysis

### IV-A Algorithm

Armed with the notions of reachable and controllable sets, we can now proceed to solving the TOPP problem. The Reachability-Analysis-based TOPP algorithm (TOPP-RA) is given in Algorithm 1 below and illustrated in Fig. 1.

Input: Path 𝒫, starting and ending velocities ${\overset{˙}{s}}_{0},{\overset{˙}{s}}_{N}$ /* Backward pass: compute the controllable sets */5if 𝒦0 = ⌀ or ${\overset{˙}{s}}_{0}^{2} \notin \mathcal{K}_{0}$ then /* Forward pass: select controls greedily */10 ui*:= max u, subject to: xi* + 2 Δi u ∈ 𝒦i + 1 and (u, xi*) ∈ Ωi The algorithm proceeds in two passes. The first pass goes backward: it recursively computes the controllable sets $\mathcal{K}_{i}{({\{{\overset{˙}{s}}_{N}^{2}\}})}$ given the desired ending velocity ${\overset{˙}{s}}_{N}$, as described in Section III-C. If any of the controllable sets is empty or if the starting state ${\overset{˙}{s}}_{0}^{2}$ is not contained in the 0-stage controllable set, then the algorithm reports failure.

Otherwise, the algorithm proceeds to a second, forward, pass. Here, the optimal states and controls are constructed *greedily*: at each stage $i$, the highest admissible control $u$ such that the resulting next state belongs to the $({i + 1})$-stage controllable set is selected.

Note that one can construct a "dual version" of TOPP-RA as follows: (i) in a forward pass, recursively compute the $i$-stage reachable sets, $i \in {\lbrack 0,\ldots,N\rbrack}$; (ii) in a backward pass, greedily select, at stage $i$, the lowest control such that the previous state belongs to the $({i - 1})$-stage reachable set.

In the following sections, we show the correctness and optimality of the algorithm and give a more detailed complexity analysis.

### IV-B Correctness of TOPP-RA

We show that TOPP-RA is correct in the sense of the following theorem.

### Theorem 1

Consider a discretized TOPP instance. TOPP-RA returns an admissible parameterization solving that instance whenever one exists, and reports Infeasible otherwise.

### Proof

\(1\) We first show that, if TOPP-RA reports Infeasible, then the instance is indeed not parameterizable. By contradiction, assume that there exists an admissible parameterization ${{\overset{˙}{s}}_{0}^{2} = {x_{0},u_{0},\ldots,u_{N - 1}}},{x_{N} = {\overset{˙}{s}}_{N}^{2}}$. We now show by backward induction on $i$ that $\mathcal{K}_{i}$ contains at least $x_{i}$.

Initialization: $\mathcal{K}_{N}$ contains $x_{N}$ by construction.

Induction: Assume that $\mathcal{K}_{i}$ contains $x_{i}$. Since the parameterization is admissible, one has $x_{i} = {x_{i - 1} + {2\Delta_{i}u_{i - 1}}}$ and ${(u_{i - 1},x_{i - 1})} \in \Omega_{i - 1}$. By definition of the controllable sets, $x_{i - 1} \in \mathcal{K}_{i - 1}$.

We have thus shown that none of the $\mathcal{K}_{i}$ is empty and that $\mathcal{K}_{0}$ contains at least $x_{0} = {\overset{˙}{s}}_{0}^{2}$, which implies that TOPP-RA cannot report Infeasible.

\(2\) Assume now that TOPP-RA returns a sequence $(x_{0}^{\ast},u_{0}^{\ast},\ldots,u_{N - 1}^{\ast},x_{N}^{\ast})$. One can easily show by forward induction on $i$ that the sequence indeed constitutes an admissible parameterization that solves the instance. ∎

### IV-C Asymptotic optimality of TOPP-RA

We show the following result: as the discretization step size goes to zero, the cost, i.e. traversal time, of the parameterization returned by TOPP-RA converges to the optimal value.

Unsurprisingly, the main difficulty with proving asymptotic optimality comes from the existence of zero-inertia points. Note however this difficulty does not affect the robustness or the correctness of the algorithm.

To avoid too many technicalities, we make the following assumption.

### Assumption 1 (and definition)

There exist piece-wise $\mathcal{C}^{1}$-continuous functions ${\overset{\sim}{\mathbf{a}}{(s)}_{s \in {\lbrack 0,1\rbrack}}},{\overset{\sim}{\mathbf{b}}{(s)}_{s \in {\lbrack 0,1\rbrack}}},{\overset{\sim}{\mathbf{c}}{(s)}_{s \in {\lbrack 0,1\rbrack}}}$ such that for all $i \in {\{ 0,\ldots,N\}}$, the set of admissible control-state pairs is given by Augment $\overset{\sim}{\mathbf{a}},\overset{\sim}{\mathbf{b}},\overset{\sim}{\mathbf{c}}$ into $\overline{\mathbf{a}},\overline{\mathbf{b}},\overline{\mathbf{c}}$ by adding two inequalities that express the condition ${x + {2\Delta_{i}u}} \in \mathcal{K}_{i + 1}$. The set of admissible *and controllable* control-state pairs is given by The above assumption is easily verified in the canonical case of a fully-actuated manipulator subject to torque bounds tracking a smooth path. It allows us to next easily define zero-inertia points.

### Definition 5 (Zero-inertia points)

A point $s^{\bullet}$ constitutes a zero-inertia point if there is a constraint $k$ such that ${\overline{\mathbf{a}}{(s^{\bullet})}{\lbrack k\rbrack}} = 0$. ∎ We have the following theorem, whose proof is given in Appendix -B ‣ VII Conclusion ‣ A New Approach to Time-Optimal Path Parameterization based on Reachability Analysis") (to simplify the notations, we consider uniform step sizes $\Delta_{0} = \cdots = \Delta_{N - 1} = \Delta$).

### Theorem 2

Consider a TOPP instance *without zero-inertia points*. There exists a $\Delta_{thr}$ such that if $\Delta < \Delta_{thr}$, then the parameterization returned by TOPP-RA is optimal.

The key hypothesis of this theorem is that there is no zero-inertia points. In practice, however, zero-inertia points are unavoidable and in fact constitute the most common type of switch points. The next theorem, whose proof is given in Appendix -C ‣ VII Conclusion ‣ A New Approach to Time-Optimal Path Parameterization based on Reachability Analysis"), establishes that the sub-optimality gap converges to zero with step size.

### Theorem 3

Consider a TOPP instance with a zero-inertia point at $s^{\bullet}$. Denote by $J^{\ast}$ the cost of the parameterization returned by TOPP-RA at step size $\Delta$: $\sum_{i = 0}^{N + 1}\frac{\Delta}{\sqrt{x_{i}^{\ast}}}$ and by $J^{\dagger}$ the minimum cost at the same step size. Then one has This theorem implies that, by reducing the step size, the cost of the parameterization returned by TOPP-RA can be made arbitrarily close to the minimum cost. This remains true when there are a finite number of zero-inertia points. The case of zero-inertia *arcs* might be more problematic, but it is always possible to avoid such arcs during the planning stage.

### IV-D Complexity analysis

We now perform a complexity analysis of TOPP-RA and compare it with the Numerical Integration and the Convex Optimization approaches. For simplicity, we shall restrict the discussion to the non-redundantly actuated case (the redundantly-actuated case actually brings an additional advantage to TOPP-RA, see Implementation remark 3).

Assume that there are $m$ constraint inequalities and that the path discretization grid size is $N$. As a large part of the computation time is devoted to solving LPs, we need a good estimate of the practical complexity of this operation. Consider a LP with $\nu$ optimization variables and $m$ inequality constraints. Different LP methods (ellipsoidal, simplex, active sets, etc.) have different complexities. For the purpose of this section, we consider the best *practical* complexity, which is realized by the simplex method, in $O{({\nu^{2}m})}$.

*TOPP-RA:* The LPs considered here have 2 variables and $m + 2$ inequalities. Since one needs to solve $3N$ such LPs, the complexity of TOPP-RA is $O{({mN})}$.

*Numerical integration approach:* The dominant component of this approach, in terms of time complexity, is the computation of the Maximum Velocity Curve (MVC). In most TOPP-NI implementations to date, the MVC is computed, at each discretized path position, by solving $O{(m^{2})}$ second-order polynomials, which results in an overall complexity of $O{({m^{2}N})}$.

*Convex optimization approach:* This approach formulates the TOPP problem as a single large convex optimization program with $O{(N)}$ variables and $O{({mN})}$ inequality constraints. In the fastest implementation we know of, the author solves the convex optimization problem by solving a sequence of linear programs (SLP) with the same number of variables and inequalities. Thus, the time complexity of this approach is $O{({KmN^{3}})}$, where $K$ is the number of SLP iterations.

This analysis shows that TOPP-RA has the best theoretical complexity. The next section experimentally assesses this observation.

## Experiments

We implements TOPP-RA in Python on a machine running Ubuntu with a Intel i7-4770 3.9GHz CPU and 8Gb RAM. To solve the LPs we use the Python interface of the solver qpOASES. The implementation and test cases are available at

### V-A Experiment 1: Pure joint velocity and acceleration bounds

In this experiment, we compare TOPP-RA against TOPP-NI -- the fastest known implementation of TOPP, which is based on the Numerical Integration approach. For simplicity, we consider pure joint velocity and acceleration bounds, which involve the same difficulty as any other types of kinodynamic constraints, as far as TOPP is concerned.

### V-A1 Effect of the number of constraint inequalities

We considered random geometric paths with varying degrees of freedom $n \in {\lbrack 2,60\rbrack}$. Each path was generated as follows: we sampled $5$ random waypoints and interpolated smooth geometric paths using cubic splines. For each path, velocity and acceleration bounds were also randomly chosen such that the bounds contain zero. This ensures that all generated instances are feasible. Each problem instance thus has $m = {{2n} + 2}$ constraint inequalities: $2n$ inequalities corresponding to acceleration bounds (no pruning was applied, contrary to ) and $2$ inequalities corresponding to velocity bounds (the joint velocity bounds could be immediately pruned into one lower and one upper bound on $\overset{˙}{s}$). According to the complexity analysis of Section IV-D, we consider the number of inequalities, rather than the degree of freedom, as independent variable. Finally, the discretization grid size was chosen as $N = 500$.

Fig. 2 shows the time-parameterizations and the resulting trajectories produced by TOPP-RA and TOPP-NI on an instance with $({{n = 6},{m = 14}})$. One can observe that the two algorithms produced virtually identical results, hinting at the correctness of TOPP-RA.

Figure 2: Time-optimal parameterization of a 6-dof path under velocity and acceleration bounds (m = 14 constraint inequalities and N = 500 grid points). TOPP-RA and TOPP-NI produce virtually identical results. (A): joint velocities. (B): joint accelerations. (C): velocity profiles in the $(s,\overset{˙}{s})$ plane. Note the small chattering in the joint accelerations produced by TOPP-NI, which is an artifact of the integration process. This chattering is absent from the TOPP-RA profiles.

Fig. 3 shows the computation time for TOPP-RA and TOPP-NI, excluding the "setup" and "extract trajectory" steps (which takes much longer in TOPP-NI than in TOPP-RA). The experimental results confirm our theoretical analysis in that the complexity of TOPP-RA is in linear in $m$ while that of TOPP-NI is quadratic in $m$. In terms of actual computation time, TOPP-RA becomes faster than TOPP-NI as soon as $m \geq 22$. Table I reports the different components of the computation time.

Figure 3: Computation time of TOPP-RA (solid blue) and TOPP-NI (solid orange), excluding the “setup” and “extract trajectory” steps, as a function of the number of constraint inequalities. Confirming our theoretical complexity analysis, the complexity of TOPP-RA is linear in the number of constraint inequalities m (linear fit in dashed green), while that of TOPP-NI is quadratic in m (quadratic fit in dashed red). In terms of actual computation time, TOPP-RA becomes faster than TOPP-NI as soon as m ≥ 22.

TABLE I: Breakdown of TOPP-RA and TOPP-NI total computation time to parameterize a path discretized with N = 500 grid points, subject to m = 30 inequalities.

Perhaps even more importantly than mere computation time, TOPP-RA was extremely robust: it maintained $100\%$ success rate over all instances, while TOPP-NI struggled with instances with many inequality constraints ($m \geq 40$), see Fig. 4. Since all TOPP instances were feasible, an algorithm failed when it did not return a correct parameterization.

Figure 4: Success rate for TOPP-RA and TOPP-NI. TOPP-RA enjoys consistently 100% success rate while TOPP-NI reports failure for more complex problem instances (m ≥ 40).

### V-A2 Effect of discretization grid size

Grid size (or its inverse, discretization time step) is an important parameter for both TOPP-RA and TOPP-NI as it affects running time, success rate and solution quality, as measured by constraint satisfaction error and sub-optimality. Here, we assess the effect of grid size on *success rate* and *solution quality*. Remark that, based on our complexity analysis in Section IV-D, running time depends linearly on grid size in both algorithms.

In addition to TOPP-RA and TOPP-NI, we considered TOPP-RA-intp. This variant of TOPP-RA employs the first-order interpolation scheme (see Appendix -D) to discretize the constraints, instead of the collocation scheme introduced in Section II-C.

We considered different grid sizes $N \in {\lbrack 100,1000\rbrack}$. For each grid size, we generated and solved $100$ random parameterization instances; each instance consists of a random path with $n = 14$ subject to random kinematic constraints, as in the previous experiment. Fig. 5-A shows success rates versus grid sizes. One can observe that TOPP-RA and TOPP-RA-intp maintained $100\%$ success rate across all grid sizes, while TOPP-NI reported two failures at $N = 100$ and $N = 1000$.

Figure 5: (A): effect of grid size on success rate. (B): effect of grid size on relative constraint satisfaction error, defined as the ratio between the error and the respective bound. TOPP-RA-intp returned solutions that are orders of magnitude better than TOPP-RA and TOPP-NI. (C): effect of grid size on difference between the average solution’s cost and the optimal cost, which is approximated by solving TOPP-RA-intp with N = 10000. Solutions produced by TOPP-RA-intp had higher costs than those produced by TOPP-RA as those instances were more highly constrainted.

Next, to measure the effect of grid size on solution quality, we looked at the *relative greatest constraint satisfaction errors*, defined as the ratio between the errors, whose definition is given in Appendix -D2, and the respective bounds. For each instance, we sampled the resulting trajectories at $1\ {ms}$ and computed the greatest constraint satisfaction errors by comparing the sampled joint accelerations and velocities to their respective bounds. Then, we averaged instances with the same grid size to obtain the average error for each $N$.

Fig. 5-B shows the average relative greatest constraint satisfaction errors of the three algorithms with respect to grid size. One can observe that TOPP-RA and TOPP-NI have constraint satisfaction errors of the same order of magnitude for $N < 500$, while TOPP-RA demonstrates better quality for $N \geq 500$. TOPP-RA-intp produces solutions with much higher quality. This result confirms our error analysis of different discretization schemes in Appendix -D and demonstrates that the interpolation discretization scheme is better than the collocation scheme whenever solution quality is concerned.

Fig. 5-C shows the average difference between the costs of solutions returned by TOPP-RA and TOPP-RA-intp with the *true* optimal cost, which was approximated by running TOPP-RA-intp with grid size $N = 10000$. One can observe that both algorithms are asymptotically optimal. Even more importantly, the differences are relatively small: even at the coarse grid size of $N = 100$, the difference is only $10^{- 2}{\ \sec}$.

### V-B Experiment 2: Legged robot in multi-contact

Here we consider the time-parameterization problem for a 50-dof legged robot in multi-contact under joint torque bounds and linearized friction cone constraints.

### V-B1 Formulation

We now give a brief description of our formulation, for more details, refer to. Let $\mathbf{w}_{i}$ denote the net contact wrench (force-torque pair) exerted on the robot by the $i$-th contact at point $\mathbf{p}_{i}$. Using the linearized friction cone, one obtains the set of feasible wrenches as a polyhedral cone for some matrix $\mathbf{F}_{i}$. This matrix can be found using the Cone Double Description method. Combining with the equation governing rigid-body dynamics, we obtain the full dynamic feasibility constraint as follow where $\mathbf{J}_{i}{(\mathbf{q})}$ is the wrench Jacobian. The convex set $\mathcal{C}{(\mathbf{q})}$ in Eq. can now be identified as a multi-dimensional polyhedron.

We considered a simple swaying motion: the robot stands with both feet lie flat on two uneven steps and shift its body back and forth, see Fig. 6. The coefficient of friction was set to $\mu = 0.5$. Start and end path velocities were set to zero. Discretization grid size was $N = 100$. The number of constraint inequalities was $m = 242$.

Figure 6: Time-parameterization of a legged robot trajectory under joint torque bounds and multi-contact friction constraints. (A): Snapshots of the retimed motion. (B): Optimal velocity profile computed by TOPP-RA (blue) and upper and lower limits of the controllable sets (dashed red). (C): The optimal joint torques and contact forces are obtained “for free” as slack variables of the optimization programs solved in the forward pass. Net contact forces for the left foot are shown in colors and those for the right foot are shown in transparent lines.

### V-B2 Results

Excluding computation of dynamic quantities, TOPP-RA took $267\ {ms}$ to solve for the time-optimal path parameterization on our computer. The final parameterization is shown in Fig. 6 and computation time is presented in Table II.

Compared to TOPP-NI and TOPP-CO, TOPP-RA had significantly better computation time, chiefly because both existing methods require an expensive polytopic projection step. Indeed, reported projection time of $2.4\ s$ for a similar sized problem, which is significantly more expensive than TOPP-RA computation time. Notice that , computing the parameterization takes an addition $2.46\ s$ which leads to a total computation time of $4.86\ s$.

To make a more accurate comparison, we implement the following pipeline on our computer to solve the same problem project the constraint polyhedron $\mathcal{C}_{i}$ onto the path using Bretl's polygon recursive expansion algorithm; parameterize the resulting problem using TOPP-NI.

This pipeline turned out to be much slower than TOPP-RA. We found that the number of LPs the projection step solved is nearly 8 times more than the number of LPs solved by TOPP-RA (which is fixed at ${3N} = 300$). For a more detailed comparison of computation time and parameters of the LPs, refer to Table II.

### V-B3 Obtaining joint torques and contact forces "for free"

Another interesting feature of TOPP-RA is that the algorithm can optimize and obtain joint torques and contact forces "for free" without additional processing. Concretely, since joint torques and contact forces are slack variables, one can simply store the optimal slack variable at each step and obtain a trajectory of feasible forces. To optimize the forces, we can solve the following quadratic program (QP) at the $i$-th step of the forward pass where $\epsilon$ is a positive scalar. Figure 6's lower plot shows computed contact wrench for the left leg. We note that both existing approaches, TOPP-NI and TOPP-CO are not able to produce joint torques and contact forces readily as they "flatten" the constraint polygon in the projection step.

In fact, the above formulation suggests that time-optimality is simply a specific objective cost function (linear) of the more general family of quadratic objectives. Therefore, one can in principle depart from time-optimality in favor of more realistic objective such as minimizing torque while maintaining a certain nominal velocity $x_{norm}$ as follow Finally, we observed that the choice of path discretization scheme has noticeable effects on both computational cost and quality of the result. In general, TOPP-RA-intp produced smoother trajectories and better (lower) constraint satisfaction error at the cost of longer computation time. On the other hand, TOPP-RA was faster but produced trajectories with jitters ^33^3Our experiments show that singularities do not cause parameterization failures for TOPP-RA and the jitters can usually be removed easily. One possible method is to use cubic splines to smooth the velocity profile locally around the jitters. near dynamic singularities and had worse (higher) constraint satisfaction error. comp. dynamic quantities contact forces avail.

Constraints sat. error TABLE II: Computation time (ms) and internal parameters comparison between TOPP-RA, TOPP-NI and TOPP-RA-intp (first-order interpolation) in Experiment 2.

## Additional benefits of TOPP by Reachability Analysis

We now elaborate on the additional benefits provided by the reachability analysis approach to TOPP.

### VI-A Admissible Velocity Propagation

Admissible Velocity Propagation (AVP) is a recent concept for kinodynamic motion planning. Specifically, given a path and an initial interval of velocities, AVP returns exactly the interval of all the velocities the system can reach after traversing the path while respecting the system kinodynamic constraints. Combined with existing *geometric* path planners, such as RRT, this can be advantageously used for *kinodynamic* motion planning: at each tree extension in the configuration space, AVP can be used to guarantee the eventual existence of admissible path parameterizations.

Suppose that the initial velocity interval is ${\mathbb{I}}_{0}$. It can be immediately seen that, what is computed by AVP is exactly the reachable set $\mathcal{L}_{N}{({\mathbb{I}}_{0})}$ (cf. Section III-B). Furthermore, what is computed by AVP-Backward given a desired final velocity interval ${\mathbb{I}}_{N}$ is exactly the controllable set $\mathcal{K}_{0}{({\mathbb{I}}_{N})}$ (cf. Section III-C). In terms of complexity, $\mathcal{R}_{N}{({\mathbb{I}}_{0})}$ and $\mathcal{K}_{0}{({\mathbb{I}}_{N})}$ can be found by solving respectively $2N$ and $2N$ LPs. We have thus re-derived the concepts of AVP at no cost.

### VI-B Robustness to parametric uncertainty

In most works dedicated to TOPP, including the development of the present paper up to this point, the parameters appearing in the dynamics equations and in the constraints are supposed to be exactly known. In reality, those parameters, which include inertia matrices or payloads in robot manipulators, or feet positions or friction coefficients in legged robots, are only known up to some precision. An admissible parameterization for the nominal values of the parameters might not be admissible for the actual values, and the probability of constraints violation is even higher in the *optimal* parameterization, which saturates at least one constraint at any moment in time.

TOPP-RA provides a natural way to handle parametric uncertainty. Assume that the constraints appear in the following form | | | ${{{\mathbf{a}_{i}u} + {\mathbf{b}_{i}x} + \mathbf{c}_{i}} \in \mathcal{C}_{i}},$ | | \(11\) | | | | ${{\forall{(\mathbf{a}_{i},\mathbf{b}_{i},\mathbf{c}_{i},\mathcal{C}_{i})}} \in \mathcal{E}_{i}},$ | | | where $\mathcal{E}_{i}$ contains all the possible values that the parameters might take at path position $s_{i}$.

### Implementation remark 6

Consider for instance the manipulator with torque bounds of equation. Suppose that, at path position $i$, the inertia matrix is uncertain, i.e., that it might take any values $\mathbf{M}_{i} \in {B{(\mathbf{M}_{i}^{\text{nominal}},\epsilon)}}$, where $B{(\mathbf{M}_{i}^{\text{nominal}},\epsilon)}$ denotes the ball of radius $\epsilon$ centered around $\mathbf{M}_{i}^{\text{nominal}}$ for the max norm. Then, the first component of $\mathcal{E}_{i}$ is given by $\{{\mathbf{M}_{i}\mathbf{q}'{(s_{i})}}\mid{\mathbf{M}_{i} \in {B{(\mathbf{M}_{i}^{\text{nominal}},\epsilon)}}}\}$, which is a convex set.

In legged robots, uncertainties on feet positions or on friction coefficients can be encoded into a "set of sets", in which $\mathcal{C}_{i}$ can take values. ∎ TOPP-RA can handle this situation by suitably modifying its two passes. Before presenting the modifications, we first give some definitions. Denote the $i$-stage set of *robust admissible* control-state pairs by The sets of robust admissible states ${\hat{\mathcal{X}}}_{i}$ and robust admissible controls ${\hat{\mathcal{U}}}_{i}{(x)}$ can be defined as in Section III-A.

In the backward pass, TOPP-RA computes the *robust controllable sets*, whose definition is given below.

### Definition 6 ($i$-stage *robust* controllable set)

Consider a set of desired ending states ${\mathbb{I}}_{N}$. The *$i$-stage robust controllable set* ${\hat{\mathcal{K}}}_{i}{({\mathbb{I}}_{N})}$ is the set states $x \in \hat{\mathcal{X}_{i}}$ such that there exists a state $x_{N} \in {\mathbb{I}}_{N}$ and a sequence of *robust admissible controls* $u_{i},\ldots,u_{N - 1}$ that steers the system from $x$ to $x_{N}$. ∎ To compute the robust controllable sets, one needs the robust one-step set.

### Definition 7 (*Robust* one-step set)

Consider a set of states $\mathbb{I}$. The *robust one-step set* ${\hat{\mathcal{Q}}}_{i}{({\mathbb{I}})}$ is the set of states $x \in {\hat{\mathcal{X}}}_{i}$ such that there exists a state $\overset{\sim}{x} \in {\mathbb{I}}$ and a robust admissible control $u \in {{\hat{\mathcal{U}}}_{i}{(x)}}$ that steers the system from $x$ to $\overset{\sim}{x}$. ∎ Finally, in the forward pass, the algorithm selected the *greatest* robust admissible control at each stage.

### Implementation remark 7

Computing the robust one-step set and the greatest robust admissible control involves solving LPs with uncertain constraints of the form. In general, these constraints may contain hundreds of inequalities, making them difficult to handle by generic methods. In the mathematical optimization literature, they are known as "Robust Linear Programs", and specific methods have been developed to handle them efficiently, when the robust constraints are Conic Quadratic re-presentable (CQr) sets.

The first case can be treated as normal LPs with appropriate slack variables, while the last two cases are explicit Conic Quadratic Program (CQP). For more information on this conversion, refer to the first and second chapters of. ∎

## Conclusion

We have presented a new approach to solve the Time-Optimal Path Parameterization (TOPP) problem based on Reachability Analysis (TOPP-RA). The key insight is to compute, in a first pass, the sets of controllable states, for which admissible controls allowing to reach the goal are guaranteed to exist. Time-optimality can then be obtained, in a second pass, by a simple greedy strategy. We have shown, through theoretical analyses and extensive experiments, that the proposed algorithm is extremely robust (100% success rate), is competitive in terms of computation time as compared to the fastest known TOPP implementation and produces solutions with high quality. Finally, the new approach yields additional benefits: no need for polytopic projection in the redundantly-actuated case, Admissible Velocity Projection, and robustness to parameter uncertainty.

A recognized disadvantage of the classical TOPP formulation is that the time-optimal trajectory contains hard acceleration switches, corresponding to infinite jerks. Solving TOPP subject to jerk bounds, however, is not possible using the CO-based approach as the problem becomes non-convex. Some prior works proposed to either extend the NI-based approach or to represent the parameterization as a spline and optimize directly over the parameter space. Exploring how Reachability Analysis can be extended to handle jerk bounds is another direction of our future research.

Similar to the CO-based approach, Reachability Analysis can only be applied to instances with convex constraints. Yet in practice, it is often desirable to consider in addition non-convex constraints, such as joint torque bounds with viscous friction effect. Extending Reachability Analysis to handle non-convex constraints is another important research question.
