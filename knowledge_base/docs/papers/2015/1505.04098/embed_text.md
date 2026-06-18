## Introduction

Optimal motion planning is a highly active research topic in robotics, due to the pervasive need to compute paths that simultaneously avoid complex obstacles, satisfy dynamic constraints, and are high quality according to some cost function. Recent advances in sampling-based optimal motion planning build on decades of work in the topic of feasible motion planning, in which costs are ignored. However, the field is still some ways away from general-purpose optimal planning algorithms that accept arbitrary black-box constraints and costs as input. In particular, optimality under kinematic and differential constraints remains a major challenge for sampling-based planners.

This paper presents a new state-cost space formulation that transforms optimal motion planning problems into feasible kinodynamic (both kinematically- and differentially-constrained) motion planning problems. Using this formulation, we introduce a meta-algorithm, AO-$x$, to adapt any feasible kinodynamic planner $x$ into an asymptotically-optimal motion planner, provided that $x$ satisfies some relatively unrestrictive conditions, e.g., expected running time is finite. The meta-algorithm accepts arbitrary cost functions, including non-differentiable ones, and handles whatever kinematic and differential constraints are handled by the underlying feasible planner.

Figure 1: The state-cost space for a 2D, kinematically constrained problem with a path length cost function. State-cost space is 3D, with a conical reachable set with an apex at the start configuration (green circle). Two paths to the same state-space target (red filled circles) follow trajectories that arrive at different points in state-cost space (red open circles).

The formulation is rather straightforward: $n$-dimensional state is augmented with an auxiliary cost variable, which measures the cost-to-come (i.e., accumulated cost from the start state), yielding a $({n + 1})$-dimensional, dynamically-constrained feasible problem in (state, cost) space (Fig. 1). The meta-algorithm proceeds by generating a series of feasible trajectories in state-cost space with progressively lower costs. This is accomplished by first generating a feasible trajectory in state space, then progressively shrinking an upper bound on cost according to the cost of the best path found so far. This meta-algorithm is proven to converge toward an optimal path under relatively unrestrictive conditions.

The AO-$x$ meta-algorithm is demonstrated on practical examples using the RRT and EST algorithms as subroutines for feasible kinodynamic planning. Due to prior theoretical work on the running time of EST, we are able to prove that the expected running time of the meta-algorithm is $O{({\epsilon^{- 2}{\ln{\ln\epsilon^{- 1}}}})}$, where $\epsilon$ is the solution suboptimality. Critically, this is one of the few asymptotically-optimal planners that exclusively uses control-sampling to handle dynamic constraints, rather than resorting to a steering function or a numerical two-point boundary value problem solver. The new method outperforms prior planners in several toy scenarios including both dynamic constraints and complex cost functions.

## Background and Related Work

Optimal motion planning has been a topic of renewed activity in robotics largely due to the advent of sampling-based motion planners that are proven to be asymptotically optimal. But the community has had a long history of interest in optimal motions. Numerical trajectory optimization techniques have been long studied, but have several drawbacks. First, they are prone to falling into local minima, and second they typically require differentiable constraint and cost representations, which are often hard to produce for complex obstacles. Grid-based planners are often fast in low dimensional spaces but suffer from the "curse of dimensionality," with performance degrading rapidly in spaces of higher dimension. Sampling-based planners were originally developed to overcome many of these challenges, and have been shown to have excellent empirical performance in finding feasible paths in high-dimensional spaces, both without and with dynamic constraints. However, they tend to produce jerky paths that are far from optimal. Some hybrid approaches have combined sampling-based planning with local optimization to produce better paths.

More recently, sampling-based optimal planners like RRT\* produce asymptotically-optimal paths whose costs converge in expectation toward the optimal path. The insight is that optimal paths can be obtained by judiciously "rewiring" a tree of states to add connections that reduce the cost to a given node in the tree. However, this requires a steering function, a method to produce a curve between two states that is optimal when obstacles are ignored. In systems without dynamic constraints, this is as simple as generating a straight line. But steering functions for dynamically-constrained systems are much harder to come by.

Several authors have extended RRT\* to dynamically-constrained systems. It is relatively easy to apply RRT\* to dynamically-constrained systems if a steering function is available. Proving convergence is harder, requiring analysis of small-time controllability conditions. Other authors have extended RRT\* to systems whose dynamics and costs are (or can be approximated) by linear and quadratic functions, respectively, by definition of a suitable steering function based on the LQR principle. When more complex differential constraints are involved, it may not be possible to devise a suitable steering functions. One method generated complex maneuvers using RRT\* and performed each rewiring step by numerically solving a two-point boundary value problems. This adds greatly to computational expense. A similar method performed rewiring using a spline-based trajectory representation that is optimized via a nonlinear program solver.

The prior work with closest relation to ours in terms of generality of applicability is the Sparse-Stable-RRT planner. Like our work, it avoids the use of a steering function entirely and samples directly in control space. Approximate rewiring is performed by allowing connections to points that are "near enough" according to a state-space distance metric. This scheme was proven to satisfy asymptotic near-optimality, which is the property of converging toward a path with bounded suboptimality. In a more recent paper, the same authors have extended it to an asymptotically-optimal planner, SST\*, by progressively shrinking nearness threshold parameters. However, Sparse-Stable-RRT and SST\* and have many parameters to tune, and our experiments suggest that AO-$x$ planners in general outperform both planners.

We note the similarity of algorithm to Anytime-RRT, except that the planner uses state-cost space rather than simply state space (and has fewer parameters to tune). Hence, Anytime-RRT does not obey any theoretical asymptotic- or near-optimality guarantees. This is critical in practice, as our experiments suggest Anytime-RRT tends not to converge to an optimum.

## Theoretical Formulation

This section presents the state-cost space formulation, the meta-algorithms, and theoretical results regarding asymptotically-optimality.

### III-A Terminology

First we define key concepts of feasible, optimal, and boundedly-suboptimal planning problems, as well as complete, probabilistically complete, and asymptotically optimal planners. Let $X$ denote the state space.

### Definition 1

A feasible (kinodynamic) planning problem $P = {(X,U,x_{I},G,F,B,D)}$ asks to produce a trajectory ${y{(s)}}:{{\lbrack 0,S\rbrack}\rightarrow X}$ and control ${u{(s)}}:{{\lbrack 0,S\rbrack}\rightarrow U}$ such that:

This is a highly general formulation. Note that kinematic planning problems can simply set the control variable $u{(s)}$ to the derivative of the path, the control set to $B = {\{ u\quad|\mspace{21mu} \parallel u \parallel \leq 1\}}$, and the dynamic equation as ${D{(y,u)}} = u$. Second-order planning problems (i.e., those with inertia) can be defined with a configuration $\times$ velocity state $x = {(q,q)}$. Problems with time-variant constraints can be constructed in this same form by augmenting the state variable with the time variable $(x,t)$.

### Definition 2

An optimal planning problem $P = {(L,\Phi,X,U,x_{I},G,F,B,D)}$ asks to produce a trajectory ${y{(s)}}:{{\lbrack 0,S\rbrack}\rightarrow X}$ that minimizes the objective functional:

among all feasible trajectories (those that satisfy (1--5)). Here $L$ is the incremental cost and $\Phi$ is the terminal cost.

### Definition 3

A bounded-suboptimality planning problem $(P,\epsilon)$ asks to find a trajectory satisfying ${C{(y)}} = {C^{\ast} + \epsilon}$, where $C^{\ast}$ is the cost of the optimal path and $\epsilon > 0$ is a specified parameter.

### Definition 4

A complete planner $A$ finds a feasible solution to a problem $P$ when one exists, and terminates with "failure" if one does not. Moreover, it does so in finite time. A probabilistically-complete planner $A$ finds a feasible solution to a problem $P$, when one exists, with probability approaching 1 as more time is spent planning. A planner $A$ is asymptotically-optimal for the optimal planning problem $P$ if the cost $C{(t)}$ of the generated path approaches the optimum $C^{\ast}$ with probability 1 as more time $t$ is spent planning.

### III-B State-cost space equivalence

Our first contribution is to demonstrate an equivalence of any optimal planning problem with that of a canonical state-cost form in which the dependence on the incremental cost $L$ is eliminated. In particular, we augment each state $x$ with the cost $c$ taken to reach it from $x_{I}$ to derive an expanded state $z = {(x,c)}$.

### Theorem 1

The optimal planning problem $P = {(L,\Phi,X,U,x_{I},G,F,B,D)}$ is equivalent to a state-cost optimal planning problem without incremental costs

in such a way that solutions to $\hat{P}$ are in one-to-one correspondence with solutions to $P$. Here the terminal cost $\hat{\Phi}$ is given by

And the dynamics $\hat{D}$ are given by

The proof is straightforward, showing that the projection of solutions to $\hat{P}$ onto the first $dim{(X)}$ elements are solutions to $P$, and solutions to $P$ can be mapped to solutions to $\hat{P}$ via augmenting them with a cumulative cost dimension. Note that even if every state in the original space was reachable, not all points in the state-cost space are reachable. Moreover, the goal set is now a cylinder with infinite extent in the cost direction (Fig. 2.a).

Using this state-cost transformation, we derive a corollary that states that a boundedly-suboptimal problem with cost at most $\overline{c}$ can be solved by solving a feasible planning problem (Fig. 2.b).

### Corollary 1

A bounded-suboptimality planning problem $P$ with $\epsilon = {\overline{c} - C^{\ast}}$ is equivalent to a feasible planning problem $P_{\overline{c}} = {({X \times R^{+}},U,{(x_{I},0)},G_{\overline{c}},{F \times R^{+}},B,\hat{D})}$ where $G_{\overline{c}} = \left. \{{(x,c)} \middle| {{x \in G},{c \in {\lbrack 0,{\overline{c} - {\Phi{(x)}}}\rbrack}}}\} \right.$ is the set of terminal state-cost pairs satisfying the goal condition and the cost bound, and $\hat{D}$ is given by the state-cost transformation.

Specifically, if $y$ is a solution to $P_{\overline{c}}$, then it corresponds to a feasible solution of $P$ with cost no more than $\overline{c}$ (and no less than $C^{\ast}$). Also, $P_{\overline{c}}$ has no solution if and only if $\overline{c} < C^{\ast}$.

### III-C Bounded-suboptimality meta-planning with a complete feasible planner

The above corollary suggests that bounded-suboptimality planning is equivalent to feasible kinodynamic planning; however, $C^{\ast}$ is a priori unknown. Hence, we present a bounded-suboptimality meta-planner that repeatedly invokes a feasible planner while lowering an upper bound on cost. This idea builds some intuition for the asymptotically-optimal planner presented in the following section.

Figure 2: (a) The goal region in state-cost space extends the state-space goal region G infinitely along the cost axis. The optimal cost C* is the least-cost portion of the reachable set that touches the region. (b) Given the cost of an existing path $\overline{c}$, the optimal path is known to lie in the region of space with cost lower than $\overline{c}$. Finding a trajectory that improves upon $\overline{c}$ is a feasible planning problem. (c) The reachable portion of this goal set shrinks as $\overline{c}$ approaches the optimum.

The meta algorithm Bounded-Suboptimal($P$,$\epsilon$,$A$) accepts as input a problem $P$, a tolerance $\epsilon$, and a complete feasible planning algorithm $A$, and is listed as follows:

1:Run A (P∞) to obtain a first path y0. If no solution exists, then report ‘P has no solution’.
4: Run A (Pci − 1 − ϵ) to obtain a new solution yi. If no solution to Pci − 1 − ϵ exists, then stop.

Step 1 solves for a feasible solution to the original problem, with no limit on cost. In practice, it may be solved in the original state space simply by discarding the cost function. In the loop, Step 4 establishes a new cost upper bound by lowering the best cost found so far $c_{i - 1}$ by $\epsilon$. The following theorem proves correctness of this meta-algorithm.

### Theorem 2

If $A$ is a complete planner for the feasible kinodynamic planning problem, then Bounded-Suboptimal($A$,$\epsilon$) terminates in finite time and produces a path $y_{i}$ with cost no more than $C^{\ast} + \epsilon$.

### Proof

Let $i + 1$ be the index of the final iteration. In the prior iteration, a solution was found, so $c_{i} \geq C^{\ast}$. In the current iteration, no solution is found, and since $A$ is complete, the current planning problem, $P_{c_{i} - \epsilon}$ is infeasible. So, ${c_{i} - \epsilon} < C^{\ast}$, and therefore $c_{i} = {C{(y_{i})}}$ is within $\epsilon$ of optimal.

Running time is finite since each loop reduces the cost by at least $\epsilon$, and hence the inner loop is run no more than $\left\lceil \frac{c_{0} - C^{\ast}}{\epsilon} \right\rceil$ times. ∎

### III-D Asymptotically-optimal meta-planning with a randomized feasible planner

The need for a complete planner is too restrictive for practical use on high-dimensional problems, where only probabilistically complete planners are practical. Here, we relax this restriction while also eliminating the dependence on the parameter $\epsilon$, under the unrestrictive assumption that the cost is lowered by a nonnegligible fraction whenever $A$ finds a feasible path.

We will need to make some assumptions such that $A$ is "well-behaved" so that it has a significant chance of finding a path that shrinks the best cost found so far regardless of $\overline{c}$. Given some cost upper bound $\overline{c}$, define the cost of the next produced solution follow a cumulative density function $\varphi{({C{(y)}};\overline{c})}$. This function ranges from 0 to 1 on the support $\lbrack C^{\ast},\overline{c}\rbrack$, i.e., ${P\left( {{C{(y)}} \leq z} \right)} = {\varphi{(z;\overline{c})}}$. We do not prescribe any form for this distribution, however, we do require one condition for its moment.

Well-behavedness of $A$ requires two conditions:

If there exists a feasible solution and $\overline{c} > C^{\ast}$, then $A$ terminates in finite time.

Given a cost bound $\overline{c}$ expected suboptimality of the computed path is shrunk toward $C^{\star}$ by a non-negligible amount each iteration. (In practice, this means that there is a nonzero chance that the planner does not produce the worst-possible path).

Specifically, condition 2 requires that:

for some $w > 0$ (the $w$ is required for technical reasons; for most cases this condition enforces that ${E{\lbrack\left. {C{(y)}} \middle| \overline{c} \right.\rbrack}} < {({\overline{c} - C^{\ast}})}$). This condition is not overly restrictive for most randomized planners; the set of paths with ${C{(y)}} = \overline{c}$ is a set with measure zero in the space of paths, and is unlikely to be sampled at random.

We are now ready to present the main algorithm, AO-$x$.

1:Run A (P∞) to obtain a first path y0. If no solution exists, report ‘P has no solution’.
4: Run A (Pci − 1) to obtain a new solution yi.

### Theorem 3

If $A$ is a well-behaved randomized algorithm, then Asymptotically-optimal($A,n$) is asymptotically optimal. In other words, as $n$ approaches infinity, the probability that $y_{n}$ is not an optimal path approaches zero.

### Proof

Let $X_{0},\ldots,X_{n}$ be the nonnegative random variables denoting the suboptimality ${C\left( y_{i} \right)} - C^{\ast}$ during a run of the algorithm. We will show that they converge almost surely to the optimum as $n$ increases. That is we want to show that ${{P{({{{lim}_{n\rightarrow\infty}X_{n}} = 0})}} = 1}.$

Almost sure (a.s.) convergence is equivalent to ${\lim_{n\rightarrow\infty}{P\left( {{\sup_{m \geq n}X_{m}} > \epsilon} \right)}} = 0$. Since ${\sup_{m \geq n}X_{m}} = X_{n}$, a.s. convergence is implied by convergence in probability ${\lim_{n\rightarrow\infty}{P{({X_{n} > \epsilon})}}} = 0$. To prove convergence in probability, we will prove ${\lim_{n\rightarrow\infty}{E{\lbrack X_{n}\rbrack}}} = 0$ and then use the Markov inequality ${P{({X_{n} \geq \epsilon})}} \leq {{E{\lbrack X_{n}\rbrack}}/\epsilon}$.

and due to we have ${E{\lbrack\left. X_{n} \middle| x_{n - 1} \right.\rbrack}} \leq {{({1 - w})}x_{n - 1}}$. Hence,

Clearly this approaches 0 as $n$ increases. ∎

### III-E Convergence rate with respect to time

We now take a more detailed analysis of the case in which the feasible planner is probabilistically complete, and study the convergence of Asymptotically-Optimal in terms of running time $t$ rather than the number $n$ of planner calls. We show again, under relatively weak assumptions, that Asymptotically-Optimal is asymptotically optimal in terms of time, even though each call to the planner takes increasingly longer to complete as $n$ increases because the reachable portion of the goal set shrinks (Fig. 2.c).

A planner is probabilistically complete if the probability that it finds a feasible path, if one exists, approaches 1 as more time is spent planning. Note that a probabilistically complete planner will not necessarily terminate if no feasible path exists.

Note that probabilistic completeness is not a sufficient condition for a planner to be useful, since the convergence rate may be so slow that it is impractical. As an example, let $A$ be a probabilistically complete planner, and $f{(t)}$ denote $P{({\text{A fails given~}t\text{~seconds of planning}})}$. If ${f{(t)}} = {1/t}$, then expected running time is infinite.

We will assume that for the given $X$, $x_{I}$, $F$, and $\hat{D}$ the planner $A$ satisfies an exponential convergence bound, in which ${f{(t)}} \leq {\max\left( 1,{\alphae^{- {\betat}}} \right)}$ for some positive values $\alpha$ and $\beta$. In practice, an exponential convergence bound implies expected running time is finite.

A more refined analysis gives a tighter bound

Convergence rate varies, however, depending on the reachable portion of the goal region $G_{\overline{c}} \cap {R{(x_{I})}}$ where $R{(x)}$ is the reachability set of $x$ in state-cost-space (Fig. 2.c). In particular, a small goal region makes it rare to $A$ to sample a configuration in it at random, which slows convergence. Hence, the convergence rates are properly defined as a function of the volume of the goal region:

The following theorem gives an example of such a bound when the EST algorithm is used as the underlying feasible planner.

Theorem. Assuming the space is expansive, the Kinodynamic EST planner satisfies an exponential convergence bound with constants ${\alpha{(g)}} = {\gamma{\ln\frac{1}{g}}}$ and ${\beta{(g)}} = {\deltag}$ for positive constants $\gamma$ and $\delta$, where $g$ is the volume of the reachable goal region. Moreover, $E{\lbrack t\rbrack}$ is $O\left( {\frac{1}{g}{\ln{\ln\frac{1}{g}}}} \right)$ as $g$ approaches 0.

### Proof

From Hsu, Latombe, Kindel, and Rock 2002, Kinodynamic EST with a uniform sampling strategy fails to find a path with probability no more than $p$ if at least ${\frac{k}{\alpha}{\ln\frac{2k}{p}}} + {\frac{2}{g}{\ln\frac{2}{p}}}$ milestones are sampled, where $k = {\frac{1}{\beta}{\ln\frac{2}{g}}}$ and $\alpha$ and $\beta$ are expansiveness constants that are fixed for the given configuration space (not related to the $\alpha$ and $\beta$ defined above). Using a bit of algebra, this expression can be rewritten as a bounded probability of failure:

Here we have assumed that each sample takes constant time and the constant factor is ignored.

Now we will simplify this rather unwieldy expression. First, note that the exponents of the first two terms in the equation are upper bounded by 1 since they are ratios of two positive numbers to their sums, and hence

Next, we use the fact that ${\ln x} \leq x$. Hence, $k = {\frac{1}{\beta}{\ln\frac{2}{g}}} \leq \frac{2}{\betag}$. The factor $\frac{\alphag}{{kg} + {2\alpha}}$ in the exponent can now be lower bounded by $\frac{\alpha\beta}{2 + {2\alpha\beta}}g$ and hence we have the desired expression

With $\gamma = \frac{8}{\beta}$ and $\delta = \frac{\alpha\beta}{2 + {2\alpha\beta}}$ constant for a given configuration space. As a result, the running time is bounded by ${E\lbrack t\rbrack} \leq {{\frac{1}{\deltag}\left\lbrack {{\ln\gamma} + {\ln{\ln\frac{1}{g}}}} \right\rbrack} + \frac{1}{1 - e^{- {\deltag}}}}$. As $g$ shrinks, the latter term's order of convergence is $\frac{1}{g}$, so we can conclude that $E{\lbrack t\rbrack}$ is $O\left( {\frac{1}{g}{\ln{\ln\frac{1}{g}}}} \right)$ as desired. ∎

Figure 3: Running time for each invocation of the underlying planning subroutine increases asymptotically to infinity as the reachable goal volume decreases. The visibility characteristics of the underlying space also have major effects on running time. Plots illustrate the theoretical bounds on expected running time of EST for spaces of three different “difficulty” levels. Specifically, visibility constants α and β are set to 0.04, 0.02, and 0.01 for easy, medium, and hard spaces. It is assumed that 1,000 samples are generated per second.

Fig. 3 illustrates this bound. It is apparent that, since $G$ is fixed by the original problem, $G_{\overline{c}}$ varies only with the parameter $\overline{c}$. Hence we may also state these functions as $\alpha{(\overline{c})}$ and $\beta{(\overline{c})}$. In order for EST to be "well-behaved" as defined above, we must require that as $\overline{c}$ approaches $C^{\ast}$, the volume of $G_{\overline{c}} \cap {R{(x_{I})}}$ is nonzero as long as $\overline{c} > C^{\ast}$.

Let us now state our main result regarding AO-$A$, which is the planner defined as Asymptotically-Optimal($P,A,\infty$).

### Theorem 4

If $A$ is a probabilistically complete, exponentially convergent planner, then AO-$A$ is asymptotically optimal in total running time $t$.

### Proof

Define $c{(t)}$ as the cost of the best path found so far in AO-$A$ after time t has elapsed. We will show that it converges almost surely toward C\* as t increases. Let Z$(t)$ be the random variable denoting the suboptimality ${c{(t)}} - C^{\ast}$ during a run of Asymptotically-optimal($A,\infty$). We wish to prove that ${\lim_{t\rightarrow\infty}{P{({{Z{(t)}} \geq \epsilon})}}} = 0$ for any $\epsilon > 0$.

Let $T{(x)}$ be the random variable denoting the time at which the cost of the best path found so far decreases below $x + C^{\ast}$. It is evident that ${P\left( {{Z{(t)}} \geq \epsilon} \right)} = {P\left( {{T{(\epsilon)}} \geq t} \right)}$. We wish to show that ${E\left\lbrack {T{(\epsilon)}} \right\rbrack} < \infty$, which would in turn imply the claim due to the Markov inequality ${P\left( {{T{(\epsilon)}} \geq t} \right)} \leq {{E\left\lbrack {T{(\epsilon)}} \right\rbrack}/t}$.

If the current cost bound is greater than $\epsilon$, then the expected time to find a path for any iteration is upper-bounded by the expected time it would take to find a path to $G_{C^{\ast} + \epsilon}$, which is some finite value $t_{\epsilon}$ since $A$ is exponentially convergent. Specifically, $t_{\epsilon} = \frac{\epsilon}{\delta\epsilon^{2}}$ for kinodynamic EST as shown above. So, if Asymptotically-optimal first finds a path with suboptimality no more than $\epsilon$ on the i'th iteration, then the cost expended is no more than $it_{\epsilon}$.

If we let $N$ denote the random variable of the iteration on which Asymptotically-optimal first finds a path with suboptimality no more than $\epsilon$, then we can bound $E\left\lbrack {T{(\epsilon)}} \right\rbrack$ as follows:

To show that $E{\lbrack N\rbrack}$ is finite, we will take a variant of the proof of Theorem 3. Again let $X_{0},\ldots,X_{n}$ be the nonnegative random variables denoting the suboptimality ${C\left( y_{i} \right)} - C^{\ast}$ during a run of the algorithm. $N$ is the index of the first $X_{i}$ that decreases below $\epsilon$. Hence,

We will use the cumulative probability function definition:

and begin by conditioning on $X_{i - 1}$.

Where we have applied the bound ${\varphi{(x;y)}} \leq 1$ which holds because $\varphi$ is a CDF.

We can now apply equation derived in Theorem 3 to obtain ${P{({N = i})}} \leq {{E\left\lbrack X_{0} \right\rbrack{({1 - w})}^{i - 1}}/\epsilon}$ where ${({1 - w})} < 1$ is defined as before. This upper bound has the form of a geometric distribution with parameter $w$. So, ${E{\lbrack N\rbrack}} \leq {{\frac{({1 - w})}{w}E{\lbrack X_{0}\rbrack}}/\epsilon}$ which is finite. ∎

To be specific, if we were to use the exponential convergence bound for kinodynamic EST, we may conclude that $E\left\lbrack {T{(\epsilon)}} \right\rbrack$ is $O\left( {\frac{1}{\epsilon^{2}}{\ln{\ln\frac{1}{\epsilon}}}} \right)$.

We note that this convergence bound is rather loose; earlier iterations will likely terminate much faster than $t_{\epsilon}$.

### III-F Complexity Discussion

The computational complexity of AO-$x$ is affected by several aspects of problem structure. As remarked before, the visibility characteristics of the problem affect the running time of the feasible planning subroutine $x$. As a result, the optimal parameters of $x$, such as the expansion distance in RRT, are problem dependent.

We also note that planner performance in state space may be different from performance in (state, cost) space. Adding a dimension of cost may increase both time and space complexity, and it also adds drift to problems that may originally be driftless. We note, however, that the control space remains unchanged, and the performance of many planners are governed chiefly by control complexity.

Lastly, we observe that problem dimensionality does not have a direct relationship to the order of convergence of AO-$x$. However, it does have a large impact in the running time of $x$, which is manifest in the terms $t_{\epsilon}$ and $w$ in the proof above. Problems of higher dimension will tend to have a larger value of the term $t_{\epsilon}$, although it is easy to construct hard low dimensional problems. The expected cost reduction $w$ is also dimensionality-dependent; for example, if the reachable goal region in (state, cost) space is locally shaped at the optimum like a convex cone of dimension $d$, then a goal configuration sampled at random will achieve an average cost reduction of $O{({1/{({d + 1})}})}$.

## Implementations and Experiments

This section describes the application of AO-$x$ to several example problems using the feasible kinodynamic planners EST and RRT. We will refer to the implementations as AO-EST and AO-RRT. All planners are implemented in the Python programming language, and hence could be sped up greatly by the use of a compiled language.

### IV-A Implementations using RRT and EST

Both kinodynamic EST and kinodynamic RRT are tree-growing planners that perform random extensions to a state-space tree, rooted at the start, by sampling a node in the tree and a control at random, and then integrating the dynamics forward over a short time horizon. They differ by sampling strategy. EST attempts to sample an extension so that its terminal state is uniformly distributed over the reachable set of the current tree. RRT attempts to sample an extension so that it is pulled toward a randomly-sampled state in state space (a Voronoi bias). Both methods can also incorporate goal biasing strategies to avoid excessive exploration of the state space in directions that are not conducive to reaching the goal.

EST Implementation. EST can be applied directly to state-cost planning. To approximate sampling over a uniform distribution over the tree's reachable set, it samples extensions with probability proportional to the inverse density of existing states in the tree. We use the standard method to approximate density by defining a grid of resolution $h$ and low dimension $k$ over randomly chosen orthogonal projections of the state-cost space. The density of a state $x$ is estimated as proportional to the number of nodes in the tree $N{(x)}$ contained in the same grid cell as $x$. In a manner similar to locality sensitive hashing, we choose several grids and count the total number of nodes sharing the same cell as $x$ across all grids. For our experiments, we use $\binom{{dim{(X)}} + 1}{k}$ grids, $h = 0.1$, and $k = 3$, and scale the configuration space $X$ to the range ${\lbrack 0,1\rbrack}^{{dim{(X)}} + 1}$ before performing the random projection. To extend the tree we sample 10 candidate extensions by choosing 10 source states uniformly from the set of occupied grid cells, and drawing one random control sample. Among those extensions that are feasible, we select one with probability proportional to $1/{({{N{(x_{t})}} + 1})}^{2}$ where $x_{t}$ is its terminal state.

RRT Implementation. RRT can also be applied almost directly, but there are some issues to be resolved regarding the definition of a suitable distance metric. RRT relies on a distance metric to guide the exploration toward previously unexplored regions of state space, and is rather sensitive to the choice of this metric, with better performance as the metric approximates the true cost-to-go. However, cost-to-go is usually difficult to estimate accurately particularly in the presence of complex obstacles and dynamic constraints. Below, we empirically investigate the effects of the distance metric. Nearest node selection is accelerated using a KD-tree data structure.

Performance considerations. In both cases, rather than planning from scratch each iteration, we maintain trees from iteration to iteration, which leads to some time savings. We also save time by pruning the portion of the tree with cost more than $\overline{c}$ whenever a new path to the goal is found. Specifically, smaller trees make EST density updates and RRT nearest neighbor queries computationally cheaper, although RRT benefits more from this optimization because a larger fraction of its running time is spent in nearest neighbor queries. We also prune more aggressively if a heuristic function $h{(x)}$ is available. If $h{(x)}$ underestimates the cost-to-go, then we can prune all nodes such that ${c + {h{(x)}}} > \overline{c}$. Other sampling heuristics could also be employed to bias the search toward low-cost paths.

### IV-B Example Problems

Figure 4: The Kink and Bugtrap problems ask to find the shortest path between the two indicated configurations.

Kink. The Kink problem (Fig. 4.a) is a kinematically-constrained problem in a unit square ${\lbrack 0,1\rbrack}^{2}$ in which the optimal solution must pass through a narrow corridor of width 0.02 with two kinks. The objective is to minimize path length. Most planners very easily find a suboptimal homotopy class, but it takes longer to discover the optimal one. The maximum length of each expansion of the tree is limited to 0.15 units.

Bugtrap. The Bugtrap problem (Fig. 4.b) is a kinematically-constrained problem in a unit square ${\lbrack 0,1\rbrack}^{2}$ that asks the robot to escape a local minimum. The objective function is path length. This is a challenging problem for RRT planners due to their reliance on the distance metric as a proxy of cost. The maximum length of each expansion of the tree is limited to 0.15 units.

Figure 5: Planning a sideways maneuver for a Dubins car using AO-RRT (top row) and AO-EST (bottom row). Numbers indicate total number of planning iterations. Green curve indicates best path found so far. Iteration counts are not directly comparable because RRT spends more time per iteration.

Dubins. This problem asks to move a standard Dubins car sideways while keeping orientation relatively fixed (Fig. 5). The state is $(x,y,\theta)$ and the control is $(v,\phi)$ where $\theta$ is the heading, $v$ is the forward velocity, and $\phi$ is the steering angle. State constraints include ${(x,y)} \in {\lbrack 0,1\rbrack}^{2}$, $v \in {\{{- 1},{+ 1}\}}$, and $\phi \in {\lbrack{- \pi},\pi\rbrack}$. For planning, time steps are drawn at random from $\lbrack 0,0.25\rbrack$ s. The metric is ${d{({(x,y,\theta)},{(x^{\prime},y^{\prime},\theta^{\prime})})}} = \sqrt{{({x - x^{\prime}})}^{2} + {({y - y^{\prime}})}^{2} + {{d_{\theta}{(\theta,\theta^{\prime})}^{2}}/{({2\pi})}}}$ where $d_{\theta}$ measures the absolute angular difference. The goal is to move the car sideways 0.4 units with a tolerance of 0.1 units in state space, with minimal execution time (equivalent to minimum path length).

Double Integrator. This asks to move a point with bounded velocities and accelerations to a target location. The state space includes $x = {(q,v)}$ includes configuration $q$ and velocity $v$, with constraints $q \in {\lbrack 0,1\rbrack}^{2}$, $v \in {\lbrack{- 1},{- 1}\rbrack}^{2}$, and $u \in {\lbrack{- 5},5\rbrack}^{2}$, with $\overset{˙}{q} = v$ and $\overset{˙}{v} = u$. The start is 0.06 units from the left and the goal is 0.06 units from the right, which must be reached with a tolerance of 0.2 units in state space. Distance is euclidean distance. Time steps are drawn from $\lbrack 0,0.05\rbrack$ s.

Pendulum. The pendulum swing-up problem places a point mass of $m =$`<!-- -->`{=html}1 kg at the end of a $L =$`<!-- -->`{=html}1 m massless rod. The state space is $x = {(\theta,\omega)}$. The goal is the set of states such that the rod is within $10^{\circ}$ of inverted and absolute angular velocity less than 0.5 rad/s, and the cost is the total time required to complete the task. We take gravitational acceleration to be $g =$`<!-- -->`{=html}9.8 N$\cdot$s^2^, and a motor can exert a torque at the fixed end of the rod with bang-bang magnitudes $\tau \in {\{{- 2},0,2\}}$ N$\cdot$m. The dynamics of the system are described by:

The difficulty in this task arises from the fact that the exerted torque cannot make the pendulum complete a full rotation. In fact, the torque will be canceled by gravity at about $11.5^{\circ}$. Therefore, the only way to achieve an inverted position is to take the advantage of gravity by swinging back and forth and accumulating angular momentum. For planning, constant torques are applied for a uniformly chosen duration between 0 and 0.5 s, and trajectories are numerically integrated using a time step of 0.01 s. Figure 6 shows the first 5 paths obtained by AO-RRT.

Figure 6: Plot of angle vs. time for the first five trajectories found by AO-RRT on the pendulum example. Shorter execution times (rightmost point on each curve) are preferred. The execution time decreases from 8.46 seconds in the first solution to 5.51 seconds in the fifth solution. (Best viewed in color)

Flappy. We devised a simplified version of the once-popular game Flappy Bird. The "bird" has a constant horizontal velocity, and can choose to fall freely under gravity, or apply a sharp upward thrust. The trajectory is a piecewise-parabolic curve. In the original game the objective is simply to avoid obstacles as long as possible, but in our case we consider other cost functions. The goal is to traverse from the left of the screen to a goal region on the right. The screen domain is $1000 \times 600$ pixels with fixed horizontal velocity of $v_{x} = {{5px}/s}$. The gravitational acceleration is $g = {{1px}/s^{2}}$ downward. The control $u$ is binary, and provides an upward thrust of either $0$ or ${4px}/s^{2}$. Fig. 7 shows an example solution path obtained by our planner.

Figure 7: Example solution path for Flappy. The planner finds a path that goes from the starting point on the left to the green goal region on the right while avoiding obstacles represented by gray rectangles.

We represent the state by

where $(x,y)$ is the bird position and $v_{y}$ is vertical velocity. The state evolves according to $\overset{˙}{x} = 5$, $\overset{˙}{y} = v_{y}$, and $\overset{˙}{v_{y}} = {{- 1} + {4u}}$ where $u \in {\{ 0,1\}}$ is the binary control. Time steps are sampled uniformly from the range $\lbrack 0,1\rbrack$, and the time evolution of the state is solved for analytically. The experiments below illustrate the ability of AO-$x$ to accept unusual cost functions.

### IV-C Experiments

Comparing AO-EST and AO-RRT. Fig. 5 illustrates AO-EST and AO-RRT applied to the Car example. Qualitatively, RRTs tend to explore more widely at the beginning of planning, while ESTs tend to focus more densely on regions already explored. As a result, in this example, AO-RRT finds a first path quicker, while AO-EST converges more quickly to the optimum (each iteration of EST is cheaper). Like in feasible planning, the best planner is largely problem-dependent, and we could find no clear winner on our other experiments.

Figure 8: Results of benchmark tests. Curves measure solution cost vs computation time, averaged over 10 runs. (Lower is better)

Benchmarking against comparable planners. We compare against the simpler meta-planner M-$x$ which simply runs the feasible planner $x$ multiple times, keeping the lowest-cost path found so far. We also experimented with a variant, M-$x$-Prune, which prunes search nodes whose cost is greater than the cost of the best path found so far. In the 2D problems, we compare against RRT\*, and for fair comparison we provide the other RRT-based planners with the straight-line a steering function as well. We also compare against Anytime-RRT and Stable-Sparse-RRT (SS-RRT). We also compared SST\*, but it performed worse than SS-RRT in all of our tests.

For fair comparison, all algorithms were implemented in Python using the same subroutines for feasibility checking, visibility checking, and distance metrics. All planners used the same parameters as AO-$x$ where applicable. For Anytime-RRT we used $\epsilon = 0.01$ and $\delta_{c} = 0.1$, and found performance was relatively insensitive to these parameters. For SS-RRT, we used parameters $\delta_{BN} = 0.1$ and $\delta_{s} = 0.03$. Tuning of these parameters did not seem to have a consistent effect on performance. KD-trees were used for closest node selection in all of the RRT-based algorithms except Anytime-RRT, in which brute-force selection must be used because it does not select nodes using a true distance metric.

Fig. LABEL:Benchmarks displays computation time vs solution cost, averaged over 10 runs for all of the benchmark problems. These results suggest that AO-EST consistently outperforms M-EST and M-EST-Prune, while AO-RRT sometimes outperforms M-RRT and M-RRT-Prune, but sometimes performs roughly the same. We find that Anytime-RRT and SS-RRT typically do not perform even as well as the simpler $M - {RRT}$ algorithm, although Anytime-RRT did perform well on Flappy, and SS-RRT did perform well on Bugtrap. Surprisingly, RRT\* performed excellently on Bugtrap but poorly on Kink despite the fact that it uses rewiring via a steering function. This drop in performance is explained by the fact that it spends excessive amounts of time building a detailed roadmap of the open homotopy class, rather than exploring the narrow passage.

Overall, we observe that AO-EST is best or near-best performer in most problems. AO-RRT sometimes is the best performer, but is more inconsistent. A possible explanation is the well-known metric sensitivity of RRTs: when the distance metric becomes a poor approximation to cost-to-go, then RRT performance deteriorates. This property is inherited by AO-RRT.

RRT distance metric. We empirically studied the influence of distance metric on planning time and quality for AO-RRT. For the pendulum example, we use a weighted Euclidean metric

where $w_{c}$ trades off between the state-space distance and the cost-space distance. For each value of $w_{c} =$ 0.1, 0.3, 1, 3, and 10, we ran AO-RRT 10 times using a 60 s time limit. Fig. 9 shows that for this example, higher cost weights have a minor effect on solution cost but a detrimental effect on running time per iteration.

Figure 9: The influence of cost weight in the RRT distance metric for the Pendulum example showing average cost (left) and planning time (right) over successive iterations.

Figure 10: Experiments comparing the cost weight on a planar kinematic problem suggests that estimating the true cost leads to faster convergence.

We found a very different effect on a second problem. This one is a kinematically-constrained, planar minimum path length problem with obstacles. The "ideal" cost weight is 1, since it perfectly measures the cost-to-go. Experiments in Fig. 10 justify this choice, showing that it converges quicker toward the optimum.

Adaptation to different costs. Using the Flappy problem, we demonstrate the fast adaptability of the AO method to different cost functions, even those that are non-differentiable. AO-RRT is used here. First, we set cost equal to path length. The second cost metric penalizes the distance traveled only in the lower half of the screen. The optimal path prefers high altitudes and passes through the two upper openings and one lower opening. Fig. 11, shows the results.

Figure 11: Convergence of Flappy with two different cost metrics. Brighter paths are of lower cost. Top: Penalizing path length. The first path is high cost (1866 px), passing through both upper openings, and eventually converges to a path that passes both lower openings (1234 px). Below: Penalizing low altitude paths. The first path passes through most of the lower openings (cost 1330), and the planner converges to a path that passes through upper openings (cost 321).

## Conclusion

This paper presents an equivalence between optimal motion planning problems (either kinodynamic or kinematic) and feasible kinodynamic motion planning problems using a state-cost space transformation. Despite the simplicity of the transformation, it is a powerful tool; we use it to develop an easily implemented, asymptotically-optimal, sampling-based meta-planner that accepts a sampling-based kinodynamic feasible planner as input. It purely uses control-based sampling, making it suitable for problems with general differential constraints and cost functions that do not admit a steering function. The expected convergence rate of the meta-planner is proven to be related to the goal-dependent running time of the underlying feasible planner. Using RRT and EST as feasible planning subroutines, we demonstrate that the proposed method attains state-of-the-art performance on a number of benchmarks.

We hope this new formulation will provide inspiration and theoretical justification for new approaches to optimal motion planning. As an example, an obvious way to improve convergence rate would be to run local optimizations on each trajectory found by the underlying planner; this method has been shown to work well for kinematic optimal path planning. We also obtained curious results regarding state-space vs cost-space weighting in the RRT distance metric. Following up on this work may also open up avenues of research in sampling strategies for state-cost space planning, e.g., in appropriate biasing strategies.
