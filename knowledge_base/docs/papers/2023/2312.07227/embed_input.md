<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Scalarizing Multi-Objective Robot Planning Problems Using Weighted Maximization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

When designing a motion planner for autonomous robots there are usually multiple objectives to be considered. However, a cost function that yields the desired trade-off between objectives is not easily obtainable. A common technique across many applications is to use a weighted sum of relevant objective functions and then carefully adapt the weights. However, this approach may not find all relevant trade-offs even in simple planning problems. Thus, we study an alternative method based on a weighted maximum of objectives. Such a cost function is more expressive than the weighted sum, and we show how it can be deployed in both continuous- and discrete-space motion planning problems. We propose a novel path planning algorithm for the proposed cost function and establish its correctness, and present heuristic adaptations that yield a practical runtime. In extensive simulation experiments, we demonstrate that the proposed cost function and algorithm are able to find a wider range of trade-offs between objectives (i.e., Pareto-optimal solutions) for various planning problems, showcasing its advantages in practice.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

(a) Ground set of feasible trajectories. Pareto-optimal solutions are highlighted in colour.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

(b) Attainable solutions for weighted sum (WS) optimization.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

(c) Attainable solutions for the proposed weighted maximum (WM) optimization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Automated planning and decision making plays a central role in designing intelligent robotic systems. In many real-world settings, autonomous robots are faced with complex scenarios that require them to balance between different objectives simultaneously. For instance, autonomous vehicles need to navigate to a goal, while ensuring safety, passenger comfort and ideally fuel-efficiency. Similarly, mobile robots navigating in human-centered spaces such as offices, hospitals or public areas need to consider task efficiency and conforming to social norms.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In multi-objective optimization (MOO) problems -- such as finding trajectories trading off different objectives -- the optimal solution is usually not unique, but rather there is a set of Pareto-optimal solutions. A solution is Pareto-optimal when none of the individual objectives can be improved without worsening at least one other objective. Thus, an important challenge in motion planning remains the design of objective functions that balance between several potentially competing objectives and allow for computing Pareto-optimal solutions. A common approach is to formulate a weighted sum of the objective functions. Often, the weights on the objectives are tuning-parameters, requiring careful calibration. In human-robot interaction (HRI) user preferences for robot behaviour is commonly modelled as a weighted sum of features. The linear structure allows for designing efficient algorithms for both motion planning and learning from human feedback making this approach very popular.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, it can fail to describe all optimal trade-offs since it is unable to explore non-convex regions of Pareto-fronts. This issue persists even in simple planning problems, as illustrated in Figure 1. Here we compute trajectories between a fixed start and goal position around two static obstacles. To optimize for trajectory length and the minimal distance to an obstacle we can inflate the obstacles and then plan paths on visibility graphs. Subplot 0(a) ‣ Figure 1 ‣ I Introduction ‣ Scalarizing Multi-Objective Robot Planning Problems using Weighted Maximization") shows the ground set of feasible trajectories together with the corresponding Pareto-front. Subplot 0(b) ‣ Figure 1 ‣ I Introduction ‣ Scalarizing Multi-Objective Robot Planning Problems using Weighted Maximization") shows the trajectories that can be computed with the weighted sum (WS) method for different weights.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We observe that the trajectories found by the WS method are only a small subset of the Pareto-optimal solutions from 0(a) ‣ Figure 1 ‣ I Introduction ‣ Scalarizing Multi-Objective Robot Planning Problems using Weighted Maximization"): While there are numerous trajectories available that pass between the two obstacles, there are only few that go around. It is important to notice that this is not due to the choice or resolution of the weights. Rather, *there does not exist any tuning of weights* such that the motion planner returns a more intermediate trade-off, since parts of the Pareto-front are non-convex. This problem occurs when parts of the Pareto-front are non-convex: the solutions of the weighted sum method do only cover the convex hull of the Pareto-front.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We study an alternative form of scalar objective function, the weighted maximum (WM) of objectives, also known as Chebyshev scalarization. This allows for finding a richer set of trade-offs between the two objectives as shown in subplot 0(c) ‣ Figure 1 ‣ I Introduction ‣ Scalarizing Multi-Objective Robot Planning Problems using Weighted Maximization"), covering all parts of the Pareto-front. Indeed, this approach is able to find all Pareto-optimal solutions, i.e., is Pareto-complete. Despite the theoretical foundations established in the optimization literature, more expressive scalarization methods such as the WM have not found much attention in robot motion planning. To demonstrate the potential of WM optimization in robot motion planning we discuss fundamental shortcomings of widely used WS cost functions, independent of how weights are selected. We revisit established results from optimization to describe theoretical differences between WS and WM cost functions: WM cost is a provably more expressive tool for motion planning, yet only requires the same number of parameters. We show how WM costs can be used in continuous and discrete space planning problems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

For discrete planning, we consider a general monotonic utility function to combine objective values of discrete actions (e.g., edges in graphs), allowing for complex planning.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-A Contributions", "weight": 1.0} -->

Our contributions are as follows: First, we consider continuous-space planning problems and show how existing optimization techniques can be used to solve planning problems with WM cost functions. Further, show NP-hardness of graph based path planning with a WM cost. Second, we present a novel optimal path planning algorithm for the WM cost and establish its correctness. Further, we show how our algorithm can be enhanced with a cost-to-go heuristic and discuss a budgeted suboptimal version that runs in polynomial time. Third, in a series of simulations, we demonstrate that the proposed WM method finds a substantially richer set of trade-offs in various motion planning problems, and showcase that the proposed graph search finds optimal solutions within a practical runtime.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-B Related work", "weight": 1.0} -->

Many robot planning problems consider multiple, potentially competing objectives. The most prominent approach is to formulate a weighted sum of a given set of objective functions and then solve the resulting scalar optimization problem. This approach is used in trajectory planning for autonomous driving, local planning in cluttered environments or social spaces, trajectory generation for manipulators, and multi-robot planning.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-B Related work", "weight": 1.0} -->

Researcher in HRI use weighted sums of objective functions -- usually referred to as features -- to model how users evaluate robot behaviour. In human-in-the-loop learning frameworks users provide feedback to a robot in form of demonstrations, choice, labels, critic, and others, allowing the robot to learn weights for the objective functions and thus adapt their behaviour to the user's preferences.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-B Related work", "weight": 1.0} -->

Different approaches that address the shortcomings of WS objectives include alternative scalar functions such as the WM approach, or incremental algorithms that iteratively explore the entire Pareto-front. A popular approach that can explore non-convex Pareto-fronts is the Adapt Weighted Sum Method. Here solutions are sampled iteratively using equality constraints to force new samples to close gaps in the Pareto-front. Yet, this approach is solving a slightly different problem than we are addressing: The method iteratively creates a set of potential solutions that cover the Pareto-front. Thus, it does not have tuning parameters such that carefully choosing them allows for obtaining the desirable solution. Further, the approach does not come with a completeness guarantee and can get stuck when the Pareto-front is discontinuous. Lastly, satisfying the added equality constraints can be infeasible or computationally hard in practice, especially in discrete-space planning. In our work, we propose using a WM cost function which has tunable weights such that any Pareto-optimal solution can be attained for a specific weight vector.

<!-- chunk {"id": "body-0016", "role": "body", "section": "I-B Related work", "weight": 1.0} -->

Further, we explicitly address the challenges in discrete space planning and propose a novel graph search for minimizing WM costs for different types of individual objective functions.

<!-- chunk {"id": "body-0017", "role": "body", "section": "I-B Related work", "weight": 1.0} -->

Overall, the limitations of WS costs find less discussion in the context of robot planning. Recently, compared different scalar objective functions. Our work focuses on the WM cost function only, yet provides a theoretical analysis of its expressiveness and presents a novel algorithm for discrete space planning. Other works directly address MOO for specific problems. For instance, the authors of studied weighted sum and weighted minimum approach for exploring Pareto-fronts of sampling based motion planning problems, while addresses the problem of simultaneously optimizing for path length and clearance in the plane, proposing a complete and efficient algorithm. WM cost functions also found attention in multi-objective Reinforcement Learning (RL). The works of and study hierarchical frameworks based on a multi-objective Probabilistic Roadmap (MO-PRM) and explicitly consider two objectives: path length and risk, and path length and state-estimation error. The MO-PRM separates objectives in primary and secondary costs, and then plans using a discretization of values for the secondary costs, similar to the $\epsilon$-constrained method.

<!-- chunk {"id": "body-0018", "role": "body", "section": "I-B Related work", "weight": 1.0} -->

A drawback of that method is that it depends on the resolution of the constraint on the secondary cost and can require solving multiple optimization problems in order to verify Pareto-optimality. In contrast to these works, our paper does not address a specific multi-objective motion planning problem, but rather proposes an alternative to weighted sums for any collection of objective functions.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

In this section, we revisit some preliminary concepts before introducing our formal problem statement.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Pareto-optimality", "weight": 1.0} -->

Consider a multi-objective optimization problem where the domain is some vector space $\mathcal{X}$. We want to find a solution ${\mathbf{x}} \in \mathcal{X}$ that simultaneously minimizes $n$ different functions, i.e., that solves $\min_{\mathbf{x}}{\{{f_{1}{({\mathbf{x}})}},\ldots,{f_{n}{({\mathbf{x}})}}\}}$. In general, the solution to a MOO problem is not a unique vector $\mathbf{x}$, but a set of Pareto-optimal solutions. We briefly review the definitions of dominated solutions and the Pareto-front.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Problem Formulation", "weight": 1.0} -->

We consider a planning problem described by a robot's state and action space $(\mathcal{X},\mathcal{A})$, a start state $x_{s}$ and a set of goal states $X_{g} \subset \mathcal{X}$. Let $\mathcal{T}$ be the set of all feasible trajectories starting at $x_{s}$ and ending at some state $x_{g} \in X_{g}$. Note that the set $\mathcal{T}$ is typically defined implicitly as set of constraints on the robot's state and actions, such as kinodynamic constraints on motion, or spatial constraints for obstacle avoidance. We keep this set abstract at this point, but give specific examples in Section V.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Problem Formulation", "weight": 1.0} -->

To define the desired robot behaviour the designer of a motion planner considers a set objectives to be minimized. Let these objectivess be denoted by $f_{1},\ldots,f_{n}$ where $f_{i}:{\mathcal{T}\rightarrow{\mathbb{R}}_{\geq 0}}$ for $i = {1,\ldots,n}$. The optimal solution to the motion planning problem is some trajectory $T^{*} \in \mathcal{T}$. Assuming that the objectives $f_{1},\ldots,f_{n}$ contain all aspects under consideration, $T^{*}$ is a Pareto-optimal solution to the problem Let $\mathcal{T}' \subseteq \mathcal{T}$ denote the set of all Pareto-optimal solutions. Given above definitions, we can pose our main problem.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem 1 (Parametric single objective planning)", "weight": 1.0} -->

Given state and action space $(\mathcal{X},\mathcal{A})$, initial state $x_{s}$ and goal states $X_{g}$, and objectives $f_{1},\ldots,f_{n}$ find an algorithm such that, for any Pareto-optimal solution $T^{*} \in \mathcal{T}'$, there exists algorithm parameters for which the algorithm returns $T^{*}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem 1 (Parametric single objective planning)", "weight": 1.0} -->

Our approach to Problem 1. ‣ II-B Problem Formulation ‣ II Problem Statement ‣ Scalarizing Multi-Objective Robot Planning Problems using Weighted Maximization") is writing as a scalar function where tuning weights $\mathbf{w}$ define the balance between objectives. The scalar function needs to be solvable, and for any Pareto-optimal trajectory $T^{*} \in \mathcal{T}$ there exist a choice of weights such that $T^{*}$ is the solution to the scalar optimization problem.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Approach", "weight": 1.0} -->

A common approach to tackle Problem 1. ‣ II-B Problem Formulation ‣ II Problem Statement ‣ Scalarizing Multi-Objective Robot Planning Problems using Weighted Maximization") is solving the MOO problem from via means of linear scalarization, also referred to as the weighted sum (WS) method or cost. This yields the following cost function where ${\mathbf{w}} \in {\lbrack 0,1\rbrack}^{n}$ is a vector of tunable weights. While this approach has been widely used and been proven to be effective, its simplicity limits the expressiveness. In this paper, we offer an alternative model-based approach. We propose a weighted maximum approach for a scalar cost functions, where the summation is replaced by taking the maximum: The cost of a trajectory is now given by the objective that attains the largest value when multiplied by its weight. That is, a trajectory is evaluated only based on the most prominent weighted objective value, and disregards other objectives. We notice that when the solution to is unique, it is Pareto-optimal.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Approach", "weight": 1.0} -->

However, if there are multiple solutions, then one is Pareto-optimal, while all others are only weakly Pareto-optimal. In order to only attain Pareto-optimal solutions, we add $\rho{\sum_{i = 1}^{n}{f_{i}{(T)}}}$ as a tie-break in the cost function, where $\rho > 0$ is a sufficiently small constant: We refer to this as the weighted maximum (WM), or augmented Chebyshev problem. Next, we characterize its expressiveness compared to the WS. Given a planning problem with the ground set of feasible trajectories $\mathcal{T}$, let $\mathcal{T}' \subseteq \mathcal{T}$ be the set of all Pareto-optimal trajectories.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Approach", "weight": 1.0} -->

Further, let $\mathcal{T}^{\mathtt{s}\mathtt{u}\mathtt{m}} \subseteq \mathcal{T}$ be the set of trajectories that are optimal for some weight in and let $\mathcal{T}^{\mathtt{m}\mathtt{a}\mathtt{x}} \subseteq \mathcal{T}$ be the set of trajectories that are optimal for some weights. In detail, we have $\mathcal{T}^{\mathtt{s}\mathtt{u}\mathtt{m}} = \left.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Motion planning with weighted maximum cost", "weight": 1.0} -->

We now consider the problem of finding an optimal trajectory for the proposed WM cost for given weights $\mathbf{w}$. Thus, we study how the WM cost can be used in continuous space motion planners such as Model-Predictive Control (MPC), and in discrete, graph-based planners such as state-lattices.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Continuous space planning", "weight": 1.0} -->

We consider a discrete time, continuous space planning problem to find an optimal trajectory $T$, subject to kinodynamical constraints ${g{(T)}} \leq 0$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Continuous space planning", "weight": 1.0} -->

We observe that this removes the maximization from the problem, such that the objective and constraints are linear compositions of the individual objective $f_{i}$. In case constraints $g{(T)}$ are non-convex, solving for the weighted maximum does not make the problem fundamentally harder than optimizing for the weighted sum. However, the same does not hold for graph-based planners as we will show next.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Graph based planning", "weight": 1.0} -->

We now consider the WM cost for discrete space motion planners such as graph or lattice based methods and characterize the hardness of the problem. Let $G = {(V,E)}$ be a graph where we associate each edge $e \in E$ with non-negative and bounded trajectory costs ${f_{1}'{(e)}},\ldots,{f_{n}'{(e)}}$.\

<!-- chunk {"id": "body-0032", "role": "body", "section": "LP formulation", "weight": 1.0} -->

We briefly consider the simple case where the costs of a path are the sum of the edge costs ${f_{i}{(P)}} = {\sum_{e \in {E{(P)}}}{f_{i}{(e)}}}$. We recall the linear program (LP) formulation of a shortest path problem, i.e., a path minimizing. Thus, the cost of an edge $e$ is given by ${{\mathbf{f}}{(e)}} \cdot {\mathbf{w}}$, and the network flow constraints are summarized as ${F{({\mathbf{x}})}} \leq {\mathbf{b}}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "LP formulation", "weight": 1.0} -->

When now considering the WM cost, the objective is ${{\min_{\mathbf{x}}{\max_{i}w_{i}}}{\sum_{(v,u)}{{x_{vu} \cdot f_{i}'}{(e_{vu})}}}} + {\rho{\sum_{i = 1}^{n}{f_{i}{(e_{vu})}}}}$. In principle, we can apply the same re-formulation technique as in equation and still obtain an LP. However, the solution will not have integer values since the constraints are no longer totally-unimodular. Hence, the LP solution will not solve the shortest path problem.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Formal problem analysis", "weight": 1.0} -->

Given that the LP-formulation for shortest paths does not work for the WM cost, we study the problem of finding a path that minimizes in more detail. We consider the general case where the costs of a path $P$ are not necessarily the sum of the edge costs in the path. Instead, the cost for a path $P$ with edges $E{(P)}$ is We refer to $\beta$ as the composition function and assume that $\beta$ is monotonically increasing. This captures two widely used concepts of defining costs over a robot's trajectory: i) summation or integration over the trajectory to compute its length, time, integral square jerk, accumulated risk or similar costs, and ii) taking the maximum value over a trajectory such as the maximum jerk or maximum risk. Thus, we can state the problem of finding a path of minimal maximum weighted cost.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Problem 2 (Min-max cost path (MMCP))", "weight": 1.0} -->

Given a strongly connected graph $G = {(V,E)}$ with start and goal vertices $s,g$ in $V$, edge cost functions ${f_{1}'{(e)}},\ldots,{f_{n}'{(e)}}$, a composition function $\beta$, and weights $w_{1},\ldots,w_{n}$, find a path that solves The problem is closely related to the multi-objective shortest path (MOSP) problem, which is NP-hard for two or more objectives.. The main difference is that MOSP considers that $\beta$ is taking the sum over different edge cost, which makes it a special case of Problem 2). ‣ Formal problem analysis ‣ IV-B Graph based planning ‣ IV Motion planning with weighted maximum cost ‣ Scalarizing Multi-Objective Robot Planning Problems using Weighted Maximization"). We formally establish hardness of our problem.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

We now present a complete algorithm for MMCP, detailed in Algorithm 1. Our approach is a modification to Dijkstra's algorithm where we record all paths to a vertex, similar to the Martin algorithm for MOSP. To that end, the elements in our ${\mathtt{o}\mathtt{p}\mathtt{e}\mathtt{n}}_{\mathtt{l}\mathtt{i}\mathtt{s}\mathtt{t}}$ are tuples consisting of a cost, a vertex, and a path (i.e., a sequence of preceding vertices) from the start to this vertex. Similar to Dijkstra's our algorithm retrieves the lowest cost element from the ${\mathtt{o}\mathtt{p}\mathtt{e}\mathtt{n}}_{\mathtt{l}\mathtt{i}\mathtt{s}\mathtt{t}}$ (line 3).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

We then expand the neighbouring vertices $u$ (line 7) and ensure that the path to the neighbour is not in the ${\mathtt{o}\mathtt{p}\mathtt{e}\mathtt{n}}_{\mathtt{l}\mathtt{i}\mathtt{s}\mathtt{t}}$, is not dominated by another path to $u$, and does not contain cycles (lines 8-10). We then add the path to $u$ with its WM cost to the ${\mathtt{o}\mathtt{p}\mathtt{e}\mathtt{n}}_{\mathtt{l}\mathtt{i}\mathtt{s}\mathtt{t}}$ (line 12-13). Algorithm 1 is able to handle any monotonically increasing composition function $\beta$ (see equation) as opposed to the sum of edge costs considered in MOSP. Opposed to MOSP, we are only interested in finding one solution for a given weight instead of the set of all Pareto-optimal paths.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Algorithm description", "weight": 1.0} -->

Thus, Algorithm 1 terminates once the goal is reached (lines 4-5).\Input: Graph G = (V, E), start and goal s, g in V, cost functions on edges f = [f1, …, fn], composition function β, weight w Output: Path from s to g with minimal WM cost 2 while |open_list| > 0 do 3 (cost, v, P) ← open_list.pop // get by min cost 7 Create tentative path Pu = P ∪ {u} 8 𝒫← all paths in open_list that end at u 9 if Any P′ ∈ 𝒫 dominates Pu or Pu contains cycles then 11 Delete tuples from open_list where P′ is dominated by Pu 12 Comp. WM cost cmax(Pu, w) // Using, 13 Add (cmax(Pu, w), u, Pu) to open_list Algorithm 1 Min-Max Cost Path

<!-- chunk {"id": "body-0039", "role": "body", "section": "Theoretical properties", "weight": 1.0} -->

First, we characterize the runtime. In the worst case, Algorithm 1 explores all paths from $s$ to any vertex $u$, leading to $2^{|V|}$ (the size of the power set for all sequences of vertices) executions of the while loop. For each subpath, we compute its cost only once in line 12, which requires evaluating $f_{i}{(e)}$ for all its edges and all $n$ objective functions. The number of edges is upper bound by ${|V|}^{2}$. Assuming that the evaluation of the costs $f_{i}{(e)}$ takes constant time, the total runtime is $O{(2^{|V|} \cdot |V|^{2} \cdot n}$). While the runtime only grows linearly with the number of objective functions, it can scale exponentially with the number of vertices. However, due to the stopping criteria in line 4, the algorithm does not enumerate all $2^{|V|}$ solutions in practice.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Theoretical properties", "weight": 1.0} -->

In our simulations we show that it is able to solve instances with ${|V|} = 2000$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Theoretical properties", "weight": 1.0} -->

Next we will establish correctness of the algorithm. We begin by considering the subpath elimination in line 9.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Cost-to-go heuristic", "weight": 1.0} -->

While Algorithm 1 is optimal, its runtime scales exponentially with the size of the graph. The runtime can be improved with a cost-to-go heuristic as in an A$^{*}$ or D$^{*}$ algorithms. To use a heuristic, we augment the path $P^{u}$ with a virtual edge to the goal. This virtual edge allows for including an estimate for the cost-to-go. An A$^{*}$ algorithm simply adds a heuristic value for the cost-to-go to the current cost. In contrast, our problem considers a maximization in the cost as well as a potentially non-linear composition function. Thus, we explicitly add an edge and then calculate the WM cost in line 12 for the augmented path. The objective values of the virtual edge must be chosen such that the WM cost of the augmented path is an underestimate of the optimal path to the goal. For instance, if one objective is length, we can set the length of virtual edge to the Euclidean distance while other objective values are zero.\

<!-- chunk {"id": "body-0043", "role": "body", "section": "Runtime Budgeting", "weight": 1.0} -->

Finally, we can modify Algorithm 1 to find potentially suboptimal solutions in polynomial runtime, similar to anytime algorothms such as ARA\*. To that end, we introduce a budget $b$ for the number of predecessor paths leading to every vertex that we can store. We then only add a new tuple in line 13 when the number of tuples with a path ending at $u$ in the open list is below $b$. This prevents the ${\mathtt{o}\mathtt{p}\mathtt{e}\mathtt{n}}_{\mathtt{l}\mathtt{i}\mathtt{s}\mathtt{t}}$ to grow exponentially, yet might prevent the algorithm from finding an optimal solution.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Runtime Budgeting", "weight": 1.0} -->

In summary, we have shown how the WM cost can be incorporated in continuous- and discrete-space planning problems. For graph based planning we provided hardness results together with a complete algorithm.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

To illustrate the advantages of the WM method, we consider several motion planning problems with multiple objectives and compare the attainable solutions when using either WS and WM. Further, we investigate the runtime of Algorithm 1.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A Comparison of WS and WM cost functions", "weight": 1.0} -->

We use three quantitative measures to compare $\mathcal{S}^{\mathtt{s}\mathtt{u}\mathtt{m}}$ and $\mathcal{S}^{\mathtt{m}\mathtt{a}\mathtt{x}}$: dispersion, coverage and number of unique solutions on the Pareto-fronts.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Simple Obstacles", "weight": 1.0} -->

First, we revisit the example from Figure 1 and provide numerical results in Table I (labelled Obstacles). We observe that WM outperforms WS on all three metrics, and with a large margin on dispersion on and number of solutions. This highlights the significant shortcomings of the WS even in very simple planning problems.\

<!-- chunk {"id": "body-0048", "role": "body", "section": "Continuous space motion planning", "weight": 1.0} -->

The second experiments considers a continuous space motion planner. We use the driver experiment that is popular in numerous studies on reward learning in HRI, for instance. An autonomous car navigates on a three lane road in the presence of a human-driven vehicle. The problem considers four objectives: heading, position in the lane, speed and distance to the other car. We solve the problem numerically using a numerical solver for constrained non-convex optimization. The min-max objective is implemented as in equation.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Continuous space motion planning", "weight": 1.0} -->

Qualitative results are shown in Figure 2. Since the numerical solver may return suboptimal solutions, we filtered all trajectories that were dominated by another trajectory. Overall, the WM yields a larger variety of solutions. In particular, the solutions for the WS method are only variations of few types of trajectories, while WM offers more nuanced solutions. On the evaluation measures, the WM clearly outperforms the WS with respect to dispersion and the number of unique solutions, yet by a smaller margin than in the Obstacles experiment. For coverage WM has only a small benefit.\Figure 2: Results for the driver experiments. White shows the human driven car, red trajectories show solutions for the autonomous car.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Graph-based motion planning", "weight": 1.0} -->

In the third setup we consider a probabilistic roadmap (PRM) with $1000$ vertices, shown in Figure 3. Similar to the first experiment, the objectives are path length and closeness to obstacles. We consider two problem variations for closeness: the summed closeness, labelled as Graph-1 in Table I with an example shown in Figure 3, and minimum closeness, labelled as Graph-2.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Graph-based motion planning", "weight": 1.0} -->

In Figure 3 we observe that the WM finds a larger variety of paths, some falling into a homotopy class for which the WS method does not find any path. In the Pareto-fronts WS exhibits several large gaps, while the WM covers the Pareto-front more densely. The gaps of the WS correspond to non-convex parts of the Pareto-front, implying that these parts cannot be covered by the WS for any choice of weights. The measures in Table I show again a substantially smaller dispersion, slightly higher coverage and higher number of solutions for WM compared to WS in both graph problems.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Graph-based motion planning", "weight": 1.0} -->

In summary, in all three planning problems the proposed method is able to find better sets of Pareto-optimal trade-offs compared to the weighted sum method.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-B Performance of WM planning on graphs", "weight": 1.0} -->

In a second experiment, we investigate the performance of Algorithm 1 when using the computation budget and the cost-to-go heuristic. As a heuristic, we add a virtual edge where the length equals the Euclidean distance to the goal and the closeness is zero. We use a PRM with $2000$ vertices, similar to the one in Figure 3. In $1000$ trials, we randomise start and goal locations, as well as the weights in the cost function. Figure 4 shows the cost ratio compared to optimal and the computation time for various computation budgets $b$. For the standard implementation without heuristic, we observe that for $b = 50$, all returned solutions are almost optimal (ratio $< 1.001$). This comes with an increase in computation time by a factor of $250$ on average, but still remains below $3$ seconds (Hardware specification: Intel i7-11800H \@2.3GHz, 32Gb RAM.). Using the cost-to-go heuristic keeps average the runtime increase below a factor of $35$ (or $<.5$ seconds).

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-B Performance of WM planning on graphs", "weight": 1.0} -->

Moreover, the heuristic also allows for finding close-to-optimal solutions with a very small budget of $b = 5$, where the runtime increase is negligible. Only for $b = 1$ the heuristic can misguide the search and yield suboptimal solutions. Yet, this does not invalidate the admissibility of the chosen heuristic: For small $b$ the algorithm has no guarantee for finding an optimal solution, independent of the heuristic. In conclusion, the cost-to-go heuristic and computation budget allow for finding paths with minimal WM cost within a practical runtime.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Discussion", "weight": 1.5} -->

We studied WM cost functions as an alternative to commonly used WS costs in motion planning problems with multiple objectives. We showed that while the WS method is widely used, it might only represent a small subset of all optimal trade-offs when at least one of the objectives is non-convex. We proposed a WM approach as an alternative cost function, which is Pareto-complete. Further, we showed how the WM cost can be used in continuous-space planning, characterized the hardness for graph-based planning and presented a novel path planning algorithm. Our simulations showed that the proposed WM cost is substantially more expressive than the WS across different motion planning problems, and that our proposed path planning algorithm can efficiently find close-to-optimal solutions. While the WM formulation makes path planning on graphs NP-hard, our simulation results show that it allows for finding substantially richer sets of solutions, recovering all parts of the Pareto-front. Further, using runtime budgeting and the cost-to-go heuristic allows for computing close-to-optimal solutions within a practical computation time.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Discussion", "weight": 1.5} -->

Future work should consider how WM costs can used for learning user preferences in human-in-the-loop learning problems. Given its advantageous expressiveness the WM allows for designing user models that represent a wider variety of user preferences with the same number of parameters. Another research direction is investigating how robot complex multi-robot routing problems can be solved for a WM cost. Further, for discrete space planning we assumed a monotonic composition function. Future work could include non-monotonic cost functions to broaden the range of applications. Lastly, finding suitable parameters for the WM cost remains a challenge. Thus, we plan to adapt our earlier work to find sets of representative weights for the WM cost.
