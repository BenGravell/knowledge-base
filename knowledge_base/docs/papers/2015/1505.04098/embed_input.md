<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Asymptotically Optimal Planning by Feasible Kinodynamic Planning in State-Cost Space

Topics include Kinodynamic planning, Asymptotic optimality, Meta algorithm.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

AO-x meta-algorithm turns any feasible kinodynamic planner into an asymptotically optimal planner by lifting planning into a state-cost space.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents an equivalence between feasible kinodynamic planning and optimal kinodynamic planning, in that any optimal planning problem can be transformed into a series of feasible planning problems in a state-cost space, whose solutions approach the optimum. This transformation yields a meta-algorithm that produces an asymptotically optimal planner, given any feasible kinodynamic planner as a subroutine. The meta-algorithm is proven to be asymptotically optimal and a formula is derived relating expected running time and solution suboptimality. It is directly applicable to a wide range of optimal planning problems because it does not resort to the use of steering functions or numerical boundary-value problem solvers. On a set of benchmark problems, it is demonstrated to perform, using the expansive space tree (EST) and rapidly-exploring random tree (RRT) algorithms as subroutines, at a level that is superior or comparable to related planners.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimal motion planning is a highly active research topic in robotics, due to the pervasive need to compute paths that simultaneously avoid complex obstacles, satisfy dynamic constraints, and are high quality according to some cost function. Recent advances in sampling-based optimal motion planning build on decades of work in the topic of feasible motion planning, in which costs are ignored. However, the field is still some ways away from general-purpose optimal planning algorithms that accept arbitrary black-box constraints and costs as input. In particular, optimality under kinematic and differential constraints remains a major challenge for sampling-based planners.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper presents a new state-cost space formulation that transforms optimal motion planning problems into feasible kinodynamic (both kinematically- and differentially-constrained) motion planning problems. Using this formulation, we introduce a meta-algorithm, AO-$x$, to adapt any feasible kinodynamic planner $x$ into an asymptotically-optimal motion planner, provided that $x$ satisfies some relatively unrestrictive conditions, e.g., expected running time is finite. The meta-algorithm accepts arbitrary cost functions, including non-differentiable ones, and handles whatever kinematic and differential constraints are handled by the underlying feasible planner.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The formulation is rather straightforward: $n$-dimensional state is augmented with an auxiliary cost variable, which measures the cost-to-come (i.e., accumulated cost from the start state), yielding a $({n + 1})$-dimensional, dynamically-constrained feasible problem in (state, cost) space (Fig. 1). The meta-algorithm proceeds by generating a series of feasible trajectories in state-cost space with progressively lower costs. This is accomplished by first generating a feasible trajectory in state space, then progressively shrinking an upper bound on cost according to the cost of the best path found so far. This meta-algorithm is proven to converge toward an optimal path under relatively unrestrictive conditions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The AO-$x$ meta-algorithm is demonstrated on practical examples using the RRT and EST algorithms as subroutines for feasible kinodynamic planning. Due to prior theoretical work on the running time of EST, we are able to prove that the expected running time of the meta-algorithm is $O{({\epsilon^{- 2}{\ln{\ln\epsilon^{- 1}}}})}$, where $\epsilon$ is the solution suboptimality. Critically, this is one of the few asymptotically-optimal planners that exclusively uses control-sampling to handle dynamic constraints, rather than resorting to a steering function or a numerical two-point boundary value problem solver. The new method outperforms prior planners in several toy scenarios including both dynamic constraints and complex cost functions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Theoretical Formulation", "weight": 1.0} -->

This section presents the state-cost space formulation, the meta-algorithms, and theoretical results regarding asymptotically-optimality.

<!-- chunk {"id": "body-0009", "role": "body", "section": "III-A Terminology", "weight": 1.0} -->

First we define key concepts of feasible, optimal, and boundedly-suboptimal planning problems, as well as complete, probabilistically complete, and asymptotically optimal planners. Let $X$ denote the state space.

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-B State-cost space equivalence", "weight": 1.0} -->

Our first contribution is to demonstrate an equivalence of any optimal planning problem with that of a canonical state-cost form in which the dependence on the incremental cost $L$ is eliminated. In particular, we augment each state $x$ with the cost $c$ taken to reach it from $x_{I}$ to derive an expanded state $z = {(x,c)}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-C Bounded-suboptimality meta-planning with a complete feasible planner", "weight": 1.0} -->

The above corollary suggests that bounded-suboptimality planning is equivalent to feasible kinodynamic planning; however, $C^{\ast}$ is a priori unknown. Hence, we present a bounded-suboptimality meta-planner that repeatedly invokes a feasible planner while lowering an upper bound on cost. This idea builds some intuition for the asymptotically-optimal planner presented in the following section.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-C Bounded-suboptimality meta-planning with a complete feasible planner", "weight": 1.0} -->

1:Run A (P∞) to obtain a first path y0. If no solution exists, then report ‘P has no solution’.
4: Run A (Pci − 1 − ϵ) to obtain a new solution yi. If no solution to Pci − 1 − ϵ exists, then stop.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-C Bounded-suboptimality meta-planning with a complete feasible planner", "weight": 1.0} -->

Step 1 solves for a feasible solution to the original problem, with no limit on cost. In practice, it may be solved in the original state space simply by discarding the cost function. In the loop, Step 4 establishes a new cost upper bound by lowering the best cost found so far $c_{i - 1}$ by $\epsilon$. The following theorem proves correctness of this meta-algorithm.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-D Asymptotically-optimal meta-planning with a randomized feasible planner", "weight": 1.0} -->

The need for a complete planner is too restrictive for practical use on high-dimensional problems, where only probabilistically complete planners are practical. Here, we relax this restriction while also eliminating the dependence on the parameter $\epsilon$, under the unrestrictive assumption that the cost is lowered by a nonnegligible fraction whenever $A$ finds a feasible path.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-D Asymptotically-optimal meta-planning with a randomized feasible planner", "weight": 1.0} -->

We will need to make some assumptions such that $A$ is "well-behaved" so that it has a significant chance of finding a path that shrinks the best cost found so far regardless of $\overline{c}$. Given some cost upper bound $\overline{c}$, define the cost of the next produced solution follow a cumulative density function $\varphi{({C{(y)}};\overline{c})}$. This function ranges from 0 to 1 on the support $\lbrack C^{\ast},\overline{c}\rbrack$, i.e., ${P\left( {{C{(y)}} \leq z} \right)} = {\varphi{(z;\overline{c})}}$. We do not prescribe any form for this distribution, however, we do require one condition for its moment.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-D Asymptotically-optimal meta-planning with a randomized feasible planner", "weight": 1.0} -->

If there exists a feasible solution and $\overline{c} > C^{\ast}$, then $A$ terminates in finite time.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-D Asymptotically-optimal meta-planning with a randomized feasible planner", "weight": 1.0} -->

Given a cost bound $\overline{c}$ expected suboptimality of the computed path is shrunk toward $C^{\star}$ by a non-negligible amount each iteration. (In practice, this means that there is a nonzero chance that the planner does not produce the worst-possible path).

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-D Asymptotically-optimal meta-planning with a randomized feasible planner", "weight": 1.0} -->

for some $w > 0$ (the $w$ is required for technical reasons; for most cases this condition enforces that ${E{\lbrack\left. {C{(y)}} \middle| \overline{c} \right.\rbrack}} < {({\overline{c} - C^{\ast}})}$). This condition is not overly restrictive for most randomized planners; the set of paths with ${C{(y)}} = \overline{c}$ is a set with measure zero in the space of paths, and is unlikely to be sampled at random.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-D Asymptotically-optimal meta-planning with a randomized feasible planner", "weight": 1.0} -->

We are now ready to present the main algorithm, AO-$x$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-D Asymptotically-optimal meta-planning with a randomized feasible planner", "weight": 1.0} -->

1:Run A (P∞) to obtain a first path y0. If no solution exists, report ‘P has no solution’.
4: Run A (Pci − 1) to obtain a new solution yi.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-E Convergence rate with respect to time", "weight": 1.0} -->

We now take a more detailed analysis of the case in which the feasible planner is probabilistically complete, and study the convergence of Asymptotically-Optimal in terms of running time $t$ rather than the number $n$ of planner calls. We show again, under relatively weak assumptions, that Asymptotically-Optimal is asymptotically optimal in terms of time, even though each call to the planner takes increasingly longer to complete as $n$ increases because the reachable portion of the goal set shrinks (Fig. 2.c).

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-E Convergence rate with respect to time", "weight": 1.0} -->

A planner is probabilistically complete if the probability that it finds a feasible path, if one exists, approaches 1 as more time is spent planning. Note that a probabilistically complete planner will not necessarily terminate if no feasible path exists.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-E Convergence rate with respect to time", "weight": 1.0} -->

Note that probabilistic completeness is not a sufficient condition for a planner to be useful, since the convergence rate may be so slow that it is impractical. As an example, let $A$ be a probabilistically complete planner, and $f{(t)}$ denote $P{({\text{A fails given~}t\text{~seconds of planning}})}$. If ${f{(t)}} = {1/t}$, then expected running time is infinite.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-E Convergence rate with respect to time", "weight": 1.0} -->

We will assume that for the given $X$, $x_{I}$, $F$, and $\hat{D}$ the planner $A$ satisfies an exponential convergence bound, in which ${f{(t)}} \leq {\max\left( 1,{\alphae^{- {\betat}}} \right)}$ for some positive values $\alpha$ and $\beta$. In practice, an exponential convergence bound implies expected running time is finite.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-E Convergence rate with respect to time", "weight": 1.0} -->

A more refined analysis gives a tighter bound

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-E Convergence rate with respect to time", "weight": 1.0} -->

Convergence rate varies, however, depending on the reachable portion of the goal region $G_{\overline{c}} \cap {R{(x_{I})}}$ where $R{(x)}$ is the reachability set of $x$ in state-cost-space (Fig. 2.c). In particular, a small goal region makes it rare to $A$ to sample a configuration in it at random, which slows convergence.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-E Convergence rate with respect to time", "weight": 1.0} -->

The following theorem gives an example of such a bound when the EST algorithm is used as the underlying feasible planner.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-E Convergence rate with respect to time", "weight": 1.0} -->

Theorem. Assuming the space is expansive, the Kinodynamic EST planner satisfies an exponential convergence bound with constants ${\alpha{(g)}} = {\gamma{\ln\frac{1}{g}}}$ and ${\beta{(g)}} = {\deltag}$ for positive constants $\gamma$ and $\delta$, where $g$ is the volume of the reachable goal region. Moreover, $E{\lbrack t\rbrack}$ is $O\left( {\frac{1}{g}{\ln{\ln\frac{1}{g}}}} \right)$ as $g$ approaches 0.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-F Complexity Discussion", "weight": 1.0} -->

The computational complexity of AO-$x$ is affected by several aspects of problem structure. As remarked before, the visibility characteristics of the problem affect the running time of the feasible planning subroutine $x$. As a result, the optimal parameters of $x$, such as the expansion distance in RRT, are problem dependent.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-F Complexity Discussion", "weight": 1.0} -->

We also note that planner performance in state space may be different from performance in (state, cost) space. Adding a dimension of cost may increase both time and space complexity, and it also adds drift to problems that may originally be driftless. We note, however, that the control space remains unchanged, and the performance of many planners are governed chiefly by control complexity.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-F Complexity Discussion", "weight": 1.0} -->

Lastly, we observe that problem dimensionality does not have a direct relationship to the order of convergence of AO-$x$. However, it does have a large impact in the running time of $x$, which is manifest in the terms $t_{\epsilon}$ and $w$ in the proof above. Problems of higher dimension will tend to have a larger value of the term $t_{\epsilon}$, although it is easy to construct hard low dimensional problems. The expected cost reduction $w$ is also dimensionality-dependent; for example, if the reachable goal region in (state, cost) space is locally shaped at the optimum like a convex cone of dimension $d$, then a goal configuration sampled at random will achieve an average cost reduction of $O{({1/{({d + 1})}})}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Implementations and Experiments", "weight": 1.0} -->

This section describes the application of AO-$x$ to several example problems using the feasible kinodynamic planners EST and RRT. We will refer to the implementations as AO-EST and AO-RRT. All planners are implemented in the Python programming language, and hence could be sped up greatly by the use of a compiled language.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Implementations using RRT and EST", "weight": 1.0} -->

Both kinodynamic EST and kinodynamic RRT are tree-growing planners that perform random extensions to a state-space tree, rooted at the start, by sampling a node in the tree and a control at random, and then integrating the dynamics forward over a short time horizon. They differ by sampling strategy. EST attempts to sample an extension so that its terminal state is uniformly distributed over the reachable set of the current tree. RRT attempts to sample an extension so that it is pulled toward a randomly-sampled state in state space (a Voronoi bias). Both methods can also incorporate goal biasing strategies to avoid excessive exploration of the state space in directions that are not conducive to reaching the goal.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Implementations using RRT and EST", "weight": 1.0} -->

EST Implementation. EST can be applied directly to state-cost planning. To approximate sampling over a uniform distribution over the tree's reachable set, it samples extensions with probability proportional to the inverse density of existing states in the tree. We use the standard method to approximate density by defining a grid of resolution $h$ and low dimension $k$ over randomly chosen orthogonal projections of the state-cost space. The density of a state $x$ is estimated as proportional to the number of nodes in the tree $N{(x)}$ contained in the same grid cell as $x$. In a manner similar to locality sensitive hashing, we choose several grids and count the total number of nodes sharing the same cell as $x$ across all grids. For our experiments, we use $\binom{{dim{(X)}} + 1}{k}$ grids, $h = 0.1$, and $k = 3$, and scale the configuration space $X$ to the range ${\lbrack 0,1\rbrack}^{{dim{(X)}} + 1}$ before performing the random projection.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Implementations using RRT and EST", "weight": 1.0} -->

To extend the tree we sample 10 candidate extensions by choosing 10 source states uniformly from the set of occupied grid cells, and drawing one random control sample. Among those extensions that are feasible, we select one with probability proportional to $1/{({{N{(x_{t})}} + 1})}^{2}$ where $x_{t}$ is its terminal state.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Implementations using RRT and EST", "weight": 1.0} -->

RRT Implementation. RRT can also be applied almost directly, but there are some issues to be resolved regarding the definition of a suitable distance metric. RRT relies on a distance metric to guide the exploration toward previously unexplored regions of state space, and is rather sensitive to the choice of this metric, with better performance as the metric approximates the true cost-to-go. However, cost-to-go is usually difficult to estimate accurately particularly in the presence of complex obstacles and dynamic constraints. Below, we empirically investigate the effects of the distance metric. Nearest node selection is accelerated using a KD-tree data structure.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Implementations using RRT and EST", "weight": 1.0} -->

Performance considerations. In both cases, rather than planning from scratch each iteration, we maintain trees from iteration to iteration, which leads to some time savings. We also save time by pruning the portion of the tree with cost more than $\overline{c}$ whenever a new path to the goal is found. Specifically, smaller trees make EST density updates and RRT nearest neighbor queries computationally cheaper, although RRT benefits more from this optimization because a larger fraction of its running time is spent in nearest neighbor queries. We also prune more aggressively if a heuristic function $h{(x)}$ is available. If $h{(x)}$ underestimates the cost-to-go, then we can prune all nodes such that ${c + {h{(x)}}} > \overline{c}$. Other sampling heuristics could also be employed to bias the search toward low-cost paths.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Example Problems", "weight": 1.0} -->

Kink. The Kink problem (Fig. 4.a) is a kinematically-constrained problem in a unit square ${\lbrack 0,1\rbrack}^{2}$ in which the optimal solution must pass through a narrow corridor of width 0.02 with two kinks. The objective is to minimize path length. Most planners very easily find a suboptimal homotopy class, but it takes longer to discover the optimal one. The maximum length of each expansion of the tree is limited to 0.15 units.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Example Problems", "weight": 1.0} -->

Bugtrap. The Bugtrap problem (Fig. 4.b) is a kinematically-constrained problem in a unit square ${\lbrack 0,1\rbrack}^{2}$ that asks the robot to escape a local minimum. The objective function is path length. This is a challenging problem for RRT planners due to their reliance on the distance metric as a proxy of cost. The maximum length of each expansion of the tree is limited to 0.15 units.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Example Problems", "weight": 1.0} -->

Dubins. This problem asks to move a standard Dubins car sideways while keeping orientation relatively fixed (Fig. 5). The state is $(x,y,\theta)$ and the control is $(v,\phi)$ where $\theta$ is the heading, $v$ is the forward velocity, and $\phi$ is the steering angle. State constraints include ${(x,y)} \in {\lbrack 0,1\rbrack}^{2}$, $v \in {\{{- 1},{+ 1}\}}$, and $\phi \in {\lbrack{- \pi},\pi\rbrack}$. For planning, time steps are drawn at random from $\lbrack 0,0.25\rbrack$ s.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Example Problems", "weight": 1.0} -->

The metric is ${d{({(x,y,\theta)},{(x^{\prime},y^{\prime},\theta^{\prime})})}} = \sqrt{{({x - x^{\prime}})}^{2} + {({y - y^{\prime}})}^{2} + {{d_{\theta}{(\theta,\theta^{\prime})}^{2}}/{({2\pi})}}}$ where $d_{\theta}$ measures the absolute angular difference. The goal is to move the car sideways 0.4 units with a tolerance of 0.1 units in state space, with minimal execution time (equivalent to minimum path length).

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B Example Problems", "weight": 1.0} -->

Double Integrator. This asks to move a point with bounded velocities and accelerations to a target location. The state space includes $x = {(q,v)}$ includes configuration $q$ and velocity $v$, with constraints $q \in {\lbrack 0,1\rbrack}^{2}$, $v \in {\lbrack{- 1},{- 1}\rbrack}^{2}$, and $u \in {\lbrack{- 5},5\rbrack}^{2}$, with $\overset{˙}{q} = v$ and $\overset{˙}{v} = u$. The start is 0.06 units from the left and the goal is 0.06 units from the right, which must be reached with a tolerance of 0.2 units in state space. Distance is euclidean distance. Time steps are drawn from $\lbrack 0,0.05\rbrack$ s.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B Example Problems", "weight": 1.0} -->

Pendulum. The pendulum swing-up problem places a point mass of $m =$`<!-- -->`{=html}1 kg at the end of a $L =$`<!-- -->`{=html}1 m massless rod. The state space is $x = {(\theta,\omega)}$. The goal is the set of states such that the rod is within $10^{\circ}$ of inverted and absolute angular velocity less than 0.5 rad/s, and the cost is the total time required to complete the task. We take gravitational acceleration to be $g =$`<!-- -->`{=html}9.8 N$\cdot$s^2^, and a motor can exert a torque at the fixed end of the rod with bang-bang magnitudes $\tau \in {\{{- 2},0,2\}}$ N$\cdot$m.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-B Example Problems", "weight": 1.0} -->

The difficulty in this task arises from the fact that the exerted torque cannot make the pendulum complete a full rotation. In fact, the torque will be canceled by gravity at about $11.5^{\circ}$. Therefore, the only way to achieve an inverted position is to take the advantage of gravity by swinging back and forth and accumulating angular momentum. For planning, constant torques are applied for a uniformly chosen duration between 0 and 0.5 s, and trajectories are numerically integrated using a time step of 0.01 s. Figure 6 shows the first 5 paths obtained by AO-RRT.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-B Example Problems", "weight": 1.0} -->

Flappy. We devised a simplified version of the once-popular game Flappy Bird. The "bird" has a constant horizontal velocity, and can choose to fall freely under gravity, or apply a sharp upward thrust. The trajectory is a piecewise-parabolic curve. In the original game the objective is simply to avoid obstacles as long as possible, but in our case we consider other cost functions. The goal is to traverse from the left of the screen to a goal region on the right. The screen domain is $1000 \times 600$ pixels with fixed horizontal velocity of $v_{x} = {{5px}/s}$. The gravitational acceleration is $g = {{1px}/s^{2}}$ downward. The control $u$ is binary, and provides an upward thrust of either $0$ or ${4px}/s^{2}$. Fig. 7 shows an example solution path obtained by our planner.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-B Example Problems", "weight": 1.0} -->

where $(x,y)$ is the bird position and $v_{y}$ is vertical velocity. The state evolves according to $\overset{˙}{x} = 5$, $\overset{˙}{y} = v_{y}$, and $\overset{˙}{v_{y}} = {{- 1} + {4u}}$ where $u \in {\{ 0,1\}}$ is the binary control. Time steps are sampled uniformly from the range $\lbrack 0,1\rbrack$, and the time evolution of the state is solved for analytically. The experiments below illustrate the ability of AO-$x$ to accept unusual cost functions.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-C Experiments", "weight": 1.0} -->

Comparing AO-EST and AO-RRT. Fig. 5 illustrates AO-EST and AO-RRT applied to the Car example. Qualitatively, RRTs tend to explore more widely at the beginning of planning, while ESTs tend to focus more densely on regions already explored. As a result, in this example, AO-RRT finds a first path quicker, while AO-EST converges more quickly to the optimum (each iteration of EST is cheaper). Like in feasible planning, the best planner is largely problem-dependent, and we could find no clear winner on our other experiments.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-C Experiments", "weight": 1.0} -->

Benchmarking against comparable planners. We compare against the simpler meta-planner M-$x$ which simply runs the feasible planner $x$ multiple times, keeping the lowest-cost path found so far. We also experimented with a variant, M-$x$-Prune, which prunes search nodes whose cost is greater than the cost of the best path found so far. In the 2D problems, we compare against RRT\*, and for fair comparison we provide the other RRT-based planners with the straight-line a steering function as well. We also compare against Anytime-RRT and Stable-Sparse-RRT (SS-RRT). We also compared SST\*, but it performed worse than SS-RRT in all of our tests.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-C Experiments", "weight": 1.0} -->

For fair comparison, all algorithms were implemented in Python using the same subroutines for feasibility checking, visibility checking, and distance metrics. All planners used the same parameters as AO-$x$ where applicable. For Anytime-RRT we used $\epsilon = 0.01$ and $\delta_{c} = 0.1$, and found performance was relatively insensitive to these parameters. For SS-RRT, we used parameters $\delta_{BN} = 0.1$ and $\delta_{s} = 0.03$. Tuning of these parameters did not seem to have a consistent effect on performance. KD-trees were used for closest node selection in all of the RRT-based algorithms except Anytime-RRT, in which brute-force selection must be used because it does not select nodes using a true distance metric.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-C Experiments", "weight": 1.0} -->

Fig. LABEL:Benchmarks displays computation time vs solution cost, averaged over 10 runs for all of the benchmark problems. These results suggest that AO-EST consistently outperforms M-EST and M-EST-Prune, while AO-RRT sometimes outperforms M-RRT and M-RRT-Prune, but sometimes performs roughly the same. We find that Anytime-RRT and SS-RRT typically do not perform even as well as the simpler $M - {RRT}$ algorithm, although Anytime-RRT did perform well on Flappy, and SS-RRT did perform well on Bugtrap. Surprisingly, RRT\* performed excellently on Bugtrap but poorly on Kink despite the fact that it uses rewiring via a steering function. This drop in performance is explained by the fact that it spends excessive amounts of time building a detailed roadmap of the open homotopy class, rather than exploring the narrow passage.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-C Experiments", "weight": 1.0} -->

Overall, we observe that AO-EST is best or near-best performer in most problems. AO-RRT sometimes is the best performer, but is more inconsistent. A possible explanation is the well-known metric sensitivity of RRTs: when the distance metric becomes a poor approximation to cost-to-go, then RRT performance deteriorates. This property is inherited by AO-RRT.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-C Experiments", "weight": 1.0} -->

RRT distance metric. We empirically studied the influence of distance metric on planning time and quality for AO-RRT. For the pendulum example, we use a weighted Euclidean metric

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-C Experiments", "weight": 1.0} -->

where $w_{c}$ trades off between the state-space distance and the cost-space distance. For each value of $w_{c} =$ 0.1, 0.3, 1, 3, and 10, we ran AO-RRT 10 times using a 60 s time limit. Fig. 9 shows that for this example, higher cost weights have a minor effect on solution cost but a detrimental effect on running time per iteration.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-C Experiments", "weight": 1.0} -->

We found a very different effect on a second problem. This one is a kinematically-constrained, planar minimum path length problem with obstacles. The "ideal" cost weight is 1, since it perfectly measures the cost-to-go. Experiments in Fig. 10 justify this choice, showing that it converges quicker toward the optimum.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-C Experiments", "weight": 1.0} -->

Adaptation to different costs. Using the Flappy problem, we demonstrate the fast adaptability of the AO method to different cost functions, even those that are non-differentiable. AO-RRT is used here. First, we set cost equal to path length. The second cost metric penalizes the distance traveled only in the lower half of the screen. The optimal path prefers high altitudes and passes through the two upper openings and one lower opening. Fig. 11, shows the results.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presents an equivalence between optimal motion planning problems (either kinodynamic or kinematic) and feasible kinodynamic motion planning problems using a state-cost space transformation. Despite the simplicity of the transformation, it is a powerful tool; we use it to develop an easily implemented, asymptotically-optimal, sampling-based meta-planner that accepts a sampling-based kinodynamic feasible planner as input. It purely uses control-based sampling, making it suitable for problems with general differential constraints and cost functions that do not admit a steering function. The expected convergence rate of the meta-planner is proven to be related to the goal-dependent running time of the underlying feasible planner. Using RRT and EST as feasible planning subroutines, we demonstrate that the proposed method attains state-of-the-art performance on a number of benchmarks.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We hope this new formulation will provide inspiration and theoretical justification for new approaches to optimal motion planning. As an example, an obvious way to improve convergence rate would be to run local optimizations on each trajectory found by the underlying planner; this method has been shown to work well for kinematic optimal path planning. We also obtained curious results regarding state-space vs cost-space weighting in the RRT distance metric. Following up on this work may also open up avenues of research in sampling strategies for state-cost space planning, e.g., in appropriate biasing strategies.
