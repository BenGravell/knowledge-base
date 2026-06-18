<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Bang-Bang Boosting of RRTs

Topics include Kinodynamic planning, Rapidly-exploring random tree, Bang-bang control, Steering function, Double integrator, Time-optimal control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Derives a complete, exact bang-bang time-optimal steering method for synchronized double integrators, using it to boost RRT performance via better BVP solving, improved Voronoi bias metrics, and post-hoc trajectory time-optimization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents methods for dramatically improving the performance of sampling-based kinodynamic planners. The key component is the first-known complete, exact steering method that produces a time-optimal trajectory between any states for a vector of synchronized double integrators. This method is applied in three ways: 1) to generate RRT edges that quickly solve the two-point boundary-value problems, 2) to produce a (quasi)metric for more accurate Voronoi bias in RRTs, and 3) to iteratively time-optimize a given collision-free trajectory. Experiments are performed for state spaces with up to 2000 dimensions, resulting in improved computed trajectories and orders of magnitude computation time improvements over using ordinary metrics and constant controls.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Rapidly exploring random trees were originally introduced as an approach to motion planning with differential constraints and dynamics. The idea was to incrementally grow a space-filling tree by applying controls so that two-point boundary-value problems could be avoided if popular methods such as probabilistic roadmaps were applied to these problems. Curiously, RRTs have found more success over the past decades for basic path planning (no differential constraints and dynamics), rather than their intended target, the kinodynamic planning problem.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Although this phenomenon is partly due to larger mainstream interest since the 1990s in basic path planning, it is primarily due to the additional challenges posed by the harder problems. Computational performance depends greatly how well the RRT nearest-neighbor metric approximates the true, optimal cost-to-go function, which is presumably unattainable. Furthermore, efficient steering methods or motion primitives are often needed to enhance performance, rather than applying constant controls as. Indeed, the most successful kinodynamic RRT planning methods have exploited the existence of simple cost-to-go functions and steering methods (ignoring obstacles) for special classes of systems or have relied on numerical solutions computed offline for more general systems and optimization objectives. Learning-based approaches to estimate the cost-to-go function have also been proposed. Inspired by all of these works, we enhance RRT performance by using metrics and steering methods based on bang-bang time-optimal controls. It was already shown that RRT exploration seems to improve with bang-bang metrics.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We continue in this direction by developing a steering method that completely solves the problem of time-optimally steering a vector of double integrators from any initial state to any goal state with a synchronized arrival time. To the best of our knowledge, this is the first such solution to this problem, and optimal solutions are easily and exactly computed as two- to four-piece constant controls for each double integrator, resulting in piecewise-constant controls for the whole system, and trajectories as parabolic arcs in the configuration and state (phase) spaces. The challenge is to ensure that all double integrators arrive at their goal states at the same time, which is often impossible due to momentum, unless some form of time-stretching or waiting is inserted.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We then show experimentally that the steering method improves RRT performance by orders of magnitude when compared to the original method that uses weighted Euclidean metrics and constant controls over fixed time intervals. The study presented here is focused on double integrator dynamics, which lies at the core of fully actuated systems, with the intention of extending it to more general dynamics of arbitrary stabilizable systems (similar to the way it was accomplished in ). As a step in this direction, we also present some preliminary results for a non-double integrator system, representing a vehicle on a curved surface.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This paper also presents methods that rapidly optimize collision-free trajectories by iteratively applying the simple time-optimal steering method to the output of sampling-based planners. We consider two cases: 1) directly optimizing the result of a kinodynamic RRT-based planners, and 2) converting the piecewise-linear path produced by an RRT-based planner for basic path planning into a trajectory by applying bang-bang controls along each segment and then further iteratively optimizing the result. Our experiments indicate that the second method is more efficient; however, it is limited to problems in which the initial and goal states are at zero velocity (if some form of completeness is demanded). An alternative to these optimizations would be to apply asymptotically optimal extensions of RRTs, such as RRT\* or SST\*; however, we are motivated by the evidence that "plan first and optimize later" often produces optimal paths more quickly and consistently than asymptotically optimal planning.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The paper continues as follows. Section II defines the problem. Section III develops the algebraic details of bang-bang time optimal control for single and multiple, parallel double integrators. Section IV presents the new planning and optimization methods. Section V gives implementation details, computed results, and performance analysis. Section VI summarizes the results, their implications, and discusses the logical next steps.

<!-- chunk {"id": "body-0010", "role": "body", "section": "PROBLEM DEFINITION", "weight": 1.0} -->

Let $\mathcal{C}$ be the robot configuration space, assumed to be an $n$-dimensional smooth manifold with points referenced using local coordinates on ${\mathbb{R}}^{n}$. Geometric models (typically piecewise-linear) are given for the robot and its (static) environment, and the robot model transforms for each $q$ depending on robot kinematics. Let $\mathcal{C}_{free}$ be the open subset of $\mathcal{C}$ in which the robot does not intersect obstacles. See for more details.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem 1 (Basic path planning)", "weight": 1.0} -->

This problem ignores kinematic constraints and dynamics, leading to a second, harder problem that takes these into account. Building upon $\mathcal{C}$ and $\mathcal{C}_{free}$, let $x = {(q,\overset{˙}{q})}$ be a $2n$-dimensional state vector for every configuration $q \in \mathcal{C}$. The set of all $x$ forms $X$, the state space, which is the tangent bundle $T{(\mathcal{C})}$. Assume $\mathcal{C}_{free}$ is lifted into $X$ as $X_{free} = \left. \{{{(q,\overset{˙}{q})} \in X} \middle| {q \in \mathcal{C}_{free}}\} \right.$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem 1 (Basic path planning)", "weight": 1.0} -->

Let $\overset{˙}{x} = {f{(x,u)}}$ define a standard control system on $X$, in which $u$ belongs to a compact action set $U \subset {\mathbb{R}}^{m}$. For convenience in this paper, we will equivalently define the control system in terms of the accelerations that actions $u \in U$ induce at a particular $q \in \mathcal{C}$. Thus, let ${A{(x)}} = {A{(q,\overset{˙}{q})}}$ be the set of all accelerations $\overset{¨}{q}$ that can be obtained at $(q,\overset{˙}{q})$ by applying an action $u \in U$ for the system $f$. Let $a \in {A{(x)}}$ denote a particular acceleration vector ($a = \overset{¨}{q}$) that may be applied.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem 2 (Kinodynamic planning)", "weight": 1.0} -->

We also consider time optimality in some cases, which means that a solution is chosen for which $t_{F}$ is as small as possible among all possible solutions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem 2 (Kinodynamic planning)", "weight": 1.0} -->

Stabilizable: For all $x \in X$, $A{(x)}$ contains an open set that contains the origin $\mathbf{0}$. This implies that for any $x_{I}$, $x_{G}$, there exists a finite-time acceleration control that solves the kinodynamic planning problem if $X_{free} = X$ (no obstacles).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem 2 (Kinodynamic planning)", "weight": 1.0} -->

nD-double-integrator: Each $q_{i}$ is independently actuated within global acceleration bounds $a_{{min},i} < 0$ and $a_{{max},i} > 0$. In this case, $A{(x)}$ is an axis-aligned rectangle that contains the origin, fixed for all $x \in X$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "TIME-OPTIMAL ACCELERATIONS", "weight": 1.0} -->

The task in this section is to calculate time-optimal solutions to the kinodynamic problem for the $n$D double integrator model and no obstacles: $X_{free} = X = {\mathbb{R}}^{2n}$. The solutions will work out so that controls are piecewise-constant,

<!-- chunk {"id": "body-0017", "role": "body", "section": "TIME-OPTIMAL ACCELERATIONS", "weight": 1.0} -->

which means that each $a_{i}$ is applied for duration $t_{i}$, starting at time $t_{1} + {t_{2}\ldotst_{i - 1}}$. Initially, $a_{1}$ is applied at time $t = 0$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Time-optimal control of a double integrator", "weight": 1.0} -->

Consider one double integrator, for which every $q \in {\mathbb{R}}$. The allowable accelerations form a closed interval $A = {\lbrack a_{min},a_{max}\rbrack}$, in which $a_{min} < 0$ and $a_{max} > 0$. It is a control system of the form $\overset{¨}{q} = a$ for $a \in {\lbrack a_{min},a_{max}\rbrack}$ and has an associated phase plane, with coordinates ${(q,\overset{˙}{q})} \in {\mathbb{R}}^{2}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Time-optimal control of a double integrator", "weight": 1.0} -->

Pontryagin's maximum principle provides necessary conditions on the time-optimal trajectory by considering a co-state vector $(\lambda_{1},\lambda_{2})$ that serves as a generalized Lagrange multipliers for the constrained optimization problem. Following the standard theory, the Hamiltonian is defined as

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Time-optimal control of a double integrator", "weight": 1.0} -->

To determine the control timings to go from $x_{I}$ to $x_{switch}$ to $x_{G}$ note that changing velocity by an amount $d$ with constant acceleration $a$ requires time $d/a$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Time-optimal control of a double integrator", "weight": 1.0} -->

There will always be at least one intersection, but sometimes there are both $I^{+}G^{-}$ and $I^{-}G^{+}$. In this case, $t_{1}$ or $t_{2}$ may be negative for one intersection, but the other intersection provides a valid control. It is also possible to obtain valid controls for both cases, in which case the one that requires least time must be selected (Figure 2 will provide more details).

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Time-optimal control of a vector of double integrators", "weight": 1.0} -->

To extend the result to a vector of double integrators, a waiting method is needed so that each double integrator arrives at its goal in its phase plane at the same time. This problem was considered, but only for the limited case in which their final velocities are zero. It was also considered, but the gap problem, introduced shortly, was neglected. In this section, we introduce an explicit, complete, and computationally efficient solution to the general problem of time-optimal steering of $n$ independent integrators for any initial and goal state pairs in their respective phase planes in $O{({n{\lg n}})}$ time.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Time-optimal control of a vector of double integrators", "weight": 1.0} -->

For a fixed $x_{I}$ and $x_{G}$, let $t^{\ast}$ be the time to reach the goal by applying the bang-bang solution of Section III-A. Now consider some $t_{w} > t^{\ast}$. Does a control $\overset{\sim}{u}$ necessarily exist that will cause $x_{G}$ to be reached at exactly time $t_{w}$? The answer is yes if there is only one intersection type ($I^{+}G^{-}$ or $I^{-}G^{+}$). However, if both intersections occur, then the situation depicted in Figure 2 occurs (or its symmetric equivalent for $\overset{˙}{q} < 0$).

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Time-optimal control of a vector of double integrators", "weight": 1.0} -->

The path from $x_{I}$ to $x_{limit} = {(q_{limit},{\overset{˙}{q}}_{limit})}$ to $x_{G}$ corresponds to the slowest trajectory that reaches $x_{G}$ while remaining in the $\overset{˙}{q} > 0$ half-plane. The critical switching point $x_{limit}$ can be calculated using the parabola intersection algebra from Section III-A. The time taken by this trajectory is calculated as

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Time-optimal control of a vector of double integrators", "weight": 1.0} -->

Thus, if $t_{w} \in {\lbrack t^{\ast},t_{limit}\rbrack}$, then a solution exists (and requires only two constant control segments). If $t_{w} > t_{limit}$, then $x_{G}$ can no longer be reached while remaining in the $\overset{˙}{q} > 0$ half-plane. The next available time is obtained by continuing to apply $a = a_{min}$ until the second parabolic intersection point, called $x_{mirror}$ is reached, in the $\overset{˙}{q} < 0$ half-plane. Note that $x_{mirror} = {(q_{limit},{- {\overset{˙}{q}}_{limit}})}$. Once $x_{mirror}$ is reached, $a = a_{max}$ is applied to arrive optimally at $x_{G}$. The time required to traverse this trajectory is

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Time-optimal control of a vector of double integrators", "weight": 1.0} -->

Thus, there may generally be a gap interval $(t_{limit},t_{mirror})$ for which no solution exists.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Time-optimal control of a vector of double integrators", "weight": 1.0} -->

while satisfying ${a_{1},a_{2}} \in {\lbrack a_{min},a_{max}\rbrack}$. Note that $t_{2} = {t_{w} - t_{1}}$ and ${0 \leq t_{1}},{t_{2} \leq t_{w}}$. The solution is usually not unique, and can be selected either arbitrarily or by optimizing a relevant optimization objective, such as energy.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A Kinodynamic RRT with bang-bang metric and steering", "weight": 1.0} -->

BANG_BANG_RRT_BIDIRECTIONAL(xI, xG)
1 Ta.init(xI); Tb.init(xG) 2 for i = 1 to K do 3 xn←bang-bang-nearest(Sa, α (i)) 4 xs←bang-bang-steer(xn,α (i)) 5 if xs ≠ xn then 6 Ta.add_vertex(xs) 7 Ta.add_edge(xn, xs) 8 xn′← bang-bang-nearest(Sb, xs) 9 xs′← bang-bang-steer(xn′,xs) 10 if xs′ ≠ xn′ then 11 Tb.add_vertex(xs′) 12 Tb.add_edge(xn′, xs′) 13 if xs′ = xs then return SOLUTION 14 if |Tb| &gt; |Ta| then SWAP(Ta,Tb) 15 return FAILURE

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Kinodynamic RRT with bang-bang metric and steering", "weight": 1.0} -->

Suppose a kinodynamic planning problem is given for an $n$D-double integrator system. Figure 3 presents an outline of a balanced bidirectional RRT-based planning algorithm that uses bang-bang methods for both the metric and the steering method. A single-tree goal-bias algorithm could alternatively be made. Let ${\alpha{(i)}} \in X$ denote the random state obtained in iteration $i$ ($\alpha$ could alternatively be a deterministic sequence that is dense in $X$ ). Line 3 returns the nearest state $x_{n}$ among all points $S_{a}$ visited by tree $T_{a}$. Using the tools from Section III, there are two natural choices for the (quasi)metric, $\rho{(x,x^{\prime})}$, which is an estimate of the distance from $x$ to $x^{\prime}$. Note it is not symmetric for our problem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Kinodynamic RRT with bang-bang metric and steering", "weight": 1.0} -->

The first choice $\rho_{1}{(x,x^{\prime})}$ is the maximum time $t_{1} + t_{2}$ from and, taken over all $n$ double integrators. A slower and more accurate metric is $\rho_{2}{(x,x^{\prime})}$ is the time with waiting, $t_{w}$, from Section III-B, which is the time it takes for every double integrator to arrive at $x^{\prime}$. Note that these metrics are expected to produce a better Voronoi-bias because they are closer to the true optimal cost-to-go function.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Kinodynamic RRT with bang-bang metric and steering", "weight": 1.0} -->

Line 4 is the time-optimal steering method from Section III-B. Collision checking is performed along the trajectory, and the steering stops at $x_{s}$ if an obstacle is hit or $\alpha{(i)}$ is reached. The new trajectory is added to $T_{a}$ (and $S_{a}$). In practice, this was accomplished in our experiments by inserting into $T_{a}$ nodes and edges along the trajectory; an exact method could alternatively be developed for representing and computing nearest points in $S_{a}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Kinodynamic RRT with bang-bang metric and steering", "weight": 1.0} -->

Lines 8 and 9 are similar to Lines 3 and 4, except that an attempt is made to connect the newest visited point $x_{s}$ to the nearest point $S_{b}$ in the other tree, $T_{b}$. Line 14 swaps the roles of the tree so that the smaller one explores toward $\alpha{(i)}$ and the larger one attempts to connect to the newly reached point.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Kinodynamic RRT with bang-bang metric and steering", "weight": 1.0} -->

If a more general, stabilizable system (recall from Section II) is given, then it can be converted into an $n$D-double integrator by restricting $A$ to an compact, axis-aligned rectangular region that contains the origin. Such a subset of $A$ always exists, and lies in the intersection of the open subsets of $A{(x)}$ that contain $\mathbf{0}$, for all $x \in X$. If the rectangle is small relative to $A{(x)}$ at each $x$, then we expect the solutions produced by the algorithm in Figure 3 to be further from their potential optima; a step toward investigating this problem is taken at the end of Section V.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Bang-bang trajectory optimization", "weight": 1.0} -->

For a given control, $\overset{\sim}{a}$, let $\overset{\sim}{a}{\lbrack t_{1},t_{2}\rbrack}$ denote its restriction to the interval $\lbrack t_{1},t_{2}\rbrack$. Thus, ${\overset{\sim}{a}{\lbrack t_{1},t_{2}\rbrack}}:{{\lbrack t_{1},t_{2}\rbrack}\rightarrow A}$.^11^1The restrictions will be closed intervals that allow single-point overlaps, but this will not affect the resulting trajectories.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Bang-bang trajectory optimization", "weight": 1.0} -->

Since the method is time-optimal, it is known that $t_{2}^{\prime} \leq t_{2}$ (they are equal only if $\overset{\sim}{a}{\lbrack t_{2},t_{F}\rbrack}$ is already time-optimal). The new control must satisfy

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Bang-bang trajectory optimization", "weight": 1.0} -->

Choose $t_{1}$ and $t_{2}$ according to a random or deterministic rule.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Bang-bang trajectory optimization", "weight": 1.0} -->

Go to Step 1, unless a termination criterion is met based on the number of iterations without any significant time reduction.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Bang-bang trajectory optimization", "weight": 1.0} -->

The rule of choosing $t_{1}$ and $t_{2}$ should produce a dense sequence of intervals in the following sense: the points of the form ${(t_{1},t_{2})} \in {\mathbb{R}}^{2}$ must be dense in the triangular region satisfying $0 \leq t_{1} \leq t_{2} \leq t_{F}$ (this ignores the fact that $t_{F}$ decreases in each iteration, and such out-of-bounds intervals can be rejected in the analysis). A simple but effective rule is to first pick $t_{1}$ and $t_{2}$ uniformly at random. If $t_{1} < t_{2}$, then replace $\overset{\sim}{a}{\lbrack t_{1},t_{2}\rbrack}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Bang-bang trajectory optimization", "weight": 1.0} -->

Otherwise, toss an unbiased coin to replace either $\overset{\sim}{a}{\lbrack 0,t_{2}\rbrack}$ or $\overset{\sim}{a}{\lbrack t_{1},t_{F}\rbrack}$. This extra consideration over purely random pairs (e.g., as in ) helps focus on the ends. Alternatively, $t_{1}$ and $t_{2}$ could be picked according to deterministic sequences to ensure convergence.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Bang-bang trajectory optimization", "weight": 1.0} -->

The termination criterion could be based on a hard limit on the number of iterations, or failure statistics (for example, no significant improvement more than $\epsilon > 0$ has occurred in the past 50 iterations). Note that the approach is not a variational optimization as in a gradient descent in trajectory space; it more resembles path shortening for basic path planning (called shortcutting in ). Thus, local time-optimality is gradually reached in the sense that the solution cannot be further improved by replacing trajectory segments with time-optimal alternatives, but it is not equivalent to a time optimum in the sense of local perturbations in trajectory space.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-C Basic path planning with bang-bang state-space lifting", "weight": 1.0} -->

Consider taking the output of a basic path planning, lifting it into the state space using bang-bang control, and then applying the bang-bang optimization method of Section IV-B. Suppose we are given a kinodynamic planning problem for $n$D double integrators for which $x_{I}$ and $x_{G}$ are both at rest (zero velocity). Thus, $x_{I} = {(q_{I},\mathbf{0})}$ and $x_{G} = {(q_{G},\mathbf{0})}$. The first step is to compute a piecewise-linear path $\tau:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{C}_{free}}$, in which $\mathcal{C}_{free}$ is the projection of $X_{free}$ onto the configuration space. This could, for example, be computed by RRT-Connect, but the particular planner is unimportant.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-C Basic path planning with bang-bang state-space lifting", "weight": 1.0} -->

We then introduce the bang-bang transform, described here for ${\mathbb{R}}^{n}$ and $a_{max} = {- a_{min}} = 1$ (it easily generalizes; see also ). For each vertex $q$ along the path $\tau$, extend it to $x = {(q,\mathbf{0})} \in X_{free}$. For each edge between consecutive vertices, $q$, $q^{\prime}$, execute a bang-bang control; we require that it is constrained to the edge and steers from $(q,\mathbf{0})$ to $(q^{\prime},\mathbf{0})$. Let $v = {q^{\prime} - q}$, normalized as $\hat{v} = {v/{\| v\|}}$. Let $s = {\max_{i}{({|{\hat{v}}_{i}|})}}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-C Basic path planning with bang-bang state-space lifting", "weight": 1.0} -->

Let $a_{i} = {{\hat{v}}_{i}/s}$ and $t = \sqrt{s{\| v\|}}$. The bang-bang control is $({(a,t)},{({- a},t)})$. This transform is applied to each edge of the path and the resulting controls are concatenated.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Basic path planning with bang-bang state-space lifting", "weight": 1.0} -->

The following propositions support the approach of lifting any piecewise-linear collision-free path (which are the typical output of sampling-based planners) into the state space via the bang-bang transform.

<!-- chunk {"id": "body-0045", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

The algorithms were implemented in Python 3.9.5 on a Windows 10 PC with an AMD Ryzen 7 5800X CPU and 32GB 3200MHz RAM. Naive methods were used for nearest neighbor searching and collision detection because they are not critical to the experimental analysis. All results are shown in a high-resolution video available at

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A Kinodynamic planning for a 2D vehicle (4D state space)", "weight": 1.0} -->

These examples use a four-dimensional state space corresponding to a 2D workspace in which a planar vehicle moves with double integrator dynamics. Let $a_{max} = {- a_{min}} = 1$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-A Kinodynamic planning for a 2D vehicle (4D state space)", "weight": 1.0} -->

The BB-RRT has the advantage, much like RRT-Connect, in that there are no parameters to tune. RRT-Bi has parameters for the step size, the set of actions, and the connection distance (the trees do not exactly meet). For the example in Figure 4 ‣ V EXPERIMENTS ‣ Bang-Bang Boosting of RRTs").a, we used 24 constant acceleration actions, ${\Deltat} = 5$, and connection distances of ${\Deltaq} = 5$ and ${\Delta\overset{˙}{q}} = 2$; in the weighted-Euclidean metric, the velocity components were weighted 17.32 times more than the configuration components. Figures 4 ‣ V EXPERIMENTS ‣ Bang-Bang Boosting of RRTs").e and 4 ‣ V EXPERIMENTS ‣ Bang-Bang Boosting of RRTs").f show two more examples under the same conditions, for which BB-RRT took on average 0.0368s and 0.4072s, respectively, over 1000 runs. The speedup factors over RRT-Bi were 837.6 and 368.5.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-A Kinodynamic planning for a 2D vehicle (4D state space)", "weight": 1.0} -->

Again, RRT-Connect on the 2D projection was faster, by factors 6.65 and 12.5, respectively. Original and bang-bang optimized paths are shown green and purple, respectively.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-C Beyond pure double integrator dynamics", "weight": 1.0} -->

As a step toward investigating bang-bang boosting of more general, stabilizable systems, suppose that the planar vehicle from Section V-A ‣ V EXPERIMENTS ‣ Bang-Bang Boosting of RRTs") is instead placed on the interior surface of a level, cylindrical tube of radius $r$ (Figures 7.a-b).

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-C Beyond pure double integrator dynamics", "weight": 1.0} -->

To generate a bang-bang trajectory from some $\theta_{I}$ to $\theta_{G}$, we restrict the system to a double integrator in which $a_{min}$ and $a_{max}$ are set to the minimum and maximum of ${A{(\theta_{I})}} \cap {A{(\theta_{G})}}$. We also test and reject any generated bang-bang trajectory for which ${\overset{¨}{q}}_{1} \notin {A{(\theta)}}$ at any time.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-C Beyond pure double integrator dynamics", "weight": 1.0} -->

Two computed examples of both BB-RRT planning and bang-bang optimization are shown in Figures 7.c-d, in which the vehicle must go from rest-to-rest along the curved surface; a top-down view is given by unrolling the cylinder. The state space $X$ is the same as in Section V-A ‣ V EXPERIMENTS ‣ Bang-Bang Boosting of RRTs"), $r = 300$, and $g = 1$; note that the slope $\theta = {q_{1}/r}$ along the left and right edges reaches $\pm {4/3}$ radians ($76.394$ degrees). The allowable horizontal accelerations at these boundaries are approximately $\lbrack{- 0.028},1.972\rbrack$ and $\lbrack{- 1.972},0.028\rbrack$, respectively (substantially shifted from $\lbrack{- 1},1\rbrack$). The computation times averaged over 1000 runs were $0.02963$s and $1.1184$s, respectively.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-C Beyond pure double integrator dynamics", "weight": 1.0} -->

We also ran 1000 experiments on the geometry of the problem in Figure 4.e, but instead using the tube model, and the resulting average computation time was $0.09594$s (approximately $2.61$ times slower than for the level-surface case). In general, the planning and optimization methods easily overcame the challenges due to the non-double integrator model.

<!-- chunk {"id": "body-0053", "role": "body", "section": "DISCUSSION", "weight": 1.5} -->

We have proposed, analyzed, and implemented methods that accelerate planning performance and optimize solutions. The key is our new steering method that quickly computes bang-bang time-optimal controls using exact, parabolic solutions. Although the study has been limited to RRTs, we expect it could enhance other sampling-based planning methods that rely on distance metrics or steering, such as probabilistic roadmaps or expansive space trees. One of the key observations of our experiments is that plan-and-optimize is superior when applicable: It is more reliable to explore the C-space first, lift the solution into the state space, and then use bang-bang optimization. However, this option applies only for rest-to-rest problems; for more general problems, a bang-bang enhanced RRT could be applied to bring each of $x_{I}$ and $x_{G}$ to zero velocity by biasing samples to the $(q,\mathbf{0})$ plane.

<!-- chunk {"id": "body-0054", "role": "body", "section": "DISCUSSION", "weight": 1.5} -->

The encouraging results of this paper lead naturally to many new questions and further studies. The implementation focused mainly on $n$-double-integrator dynamics; however, with the vehicle-in-the-tube results from Section V-C, we have easily extended it for acceleration bounds that vary with state. This opens exciting directions of research to adapt the method to many more classes of stabilizable systems. Another important direction is to develop bang-bang boosted versions of asymptotically optimal planners, such as RRT\* and SST\*; this would enable stronger comparisons to the plan-and-optimize approach, both in computation time and solution quality. Also, improvements can be made to the iterative bang-bang optimization through strategic interval selection. Finally, efficient nearest-neighbor algorithms should be developed for the bang-bang metric over a tree of parabolic arcs (analogous to ).
