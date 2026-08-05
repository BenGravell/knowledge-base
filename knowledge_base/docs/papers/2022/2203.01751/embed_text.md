<!-- arxiv-full-text:v1 {"arxiv_id": "2203.01751", "source": "arxiv-latex"} -->

## Introduction

Generating optimal motions plans is crucial for almost any robotic tasks ranging from typical manipulation tasks such as bin-picking to autonomous navigation of mobile robots. To solve such tasks, the robotics community relies on two powerful motion planning frameworks: Sampling-based planners and trajectory optimization.

Sampling-based planners like RRT* [karaman2010optimal], BIT*[gammell2015batch] or FMT*[janson2015fast] converge asymptotically to optimal solutions and almost surely provide a solution if one exists[Lavalle2006]. However, these planners are slow at converging to the optimal trajectory, because improvements to the current best solution only arise when we sample a state nearby[salzman2016asymptotically], and often provide non-smooth trajectories that may require post-processing[geraerts2007creating].

Trajectory optimization methods like KOMO [toussaint2014newton], CHOMP[ratliff2009chomp], STOMP[kalakrishnan2011stomp] and TrajOpt[schulman2014motion] use optimization methods and can exploit gradient and second order information to converge to a local optimal solution. These optimization-based methods are typically fast at converging to the local optimum, however, due to the non-convexity of the problem, the optimizer might converge to a locally optimal or even an infeasible trajectory. These methods therefore do not have convergence guarantees, i.e. they may not converge to a solution even if one exists, and the feasibility of the solution often depends heavily on the initial trajectory[merkt2018leveraging, lembono2020memory, ichnowski2020deep]. Hence, these methods usually work well in environments with few obstacles or when provided with good initial guesses[liu2017planning], e.g. for post-processing paths produced by sampling-based planners.

In order to combine the benefits of both frameworks, we propose to integrate the asymptotically optimal Batch Informed Trees (BIT*) [gammell2015batch] planner with K-Order Markov Optimization (KOMO)[toussaint2014newton, toussaint2015IJCAI]. Combining sampling and optimization helps us play on the strengths of each framework and mitigate their weaknesses. Our novel algorithm, BITKOMO, uses BIT* to iteratively generate non-optimal initial paths that are then optimized by KOMO, which results in quick convergence to local minima. The cost of the optimized path is then used by BIT* to carry a more informed search. With this method, we maintain the asymptotic global optimality guarantees by BIT* while also benefiting from the fast convergence of KOMO (Fig.[fig:pullfigure]).

At the core of BITKOMO lies a new relaxed edge collision checking method. Relaxed edge collision is an intermediate approach between full and lazy [hauser2015lazy] collision checking, where we allow partially-valid edges to remain, because the trajectory optimizer KOMO can often push invalid paths out of collision[toussaint2015IJCAI] to converge to feasible solutions. Even though this modification allows for invalid edges, we do not sacrifice any of the asymptotic guarantees provided by BIT*.

Aggregate plot over all our experiments, showing how BITKOMO converges faster than BIT*, while keeping a similar success rate. KOMO is not included, because it fails to find solutions on more than half of our experiments.

To summarize, we make two major contributions:

- Relaxed edge collision checking: A method for BIT* that allows edges partially in collision to be included in the motion tree. - BITKOMO: A planner integrating BIT* and KOMO. We integrate sampling and optimization to obtain fast convergence to the global optimum while maintaining the guarantees provided by the sampler.

## Related Work

Combining both asymptotically-optimal planners[karaman2011sampling, salzman2016asymptotically, gammell2021asymptotically, strub2021ait] and trajectory optimization[toussaint2014newton, ratliff2009chomp, kalakrishnan2011stomp, schulman2014motion, mukadam2018continuous] into one concise algorithm is an important long-term goal of the robotics community[hartmann2020planning]. There exist three main approaches. The two-step approach, where we run a sampling-based planner like the rapidly-exploring random tree (RRT)[Lavalle2006], or the probabilistic roadmap (PRM)[kavraki1996probabilistic] until a valid solution path is found. In a post-processing step[kim2003extracting, geraerts2007creating], we call a trajectory optimizer which optimizes the path to find a (local) optimal solution. This method is the most common approach, but does not hold guarantees on optimality, and does not allow the sampling-based planner to find improved solutions by leveraging information acquired by the optimizer. Our BITKOMO approach improves upon this methodology by tightly integrating sampling and optimization in an iterative fashion. Moreover, we use relaxed collision checking to quickly find partially-valid paths. Optimizers like KOMO[toussaint2014newton]can often repair those paths to quickly find a solution.

The second approach is the optimizer-as-steering method, where the integration of sampling and optimization is done using the steering function from the planner. The regionally-accelerated BIT* (RABIT*)[choudhury2016regionally] is an extension of BIT* that uses an optimizer to push infeasible edges out of collision. However, while the obtained solution cost is often better than BIT*, calls to an optimizer are often expensive and slow down the algorithm. It is also possible to integrate such an approach into a roadmap planner[alwala2020joint], to interleave edge creation and optimization steps. We differ by postponing optimization to the point where a full partially-valid path has been found, which reduces the number of unnecessary calls to the nonlinear optimizer. path-proposal method, where the planner proposes solution paths, which are then sent to the optimizer[kuntz2020fast, xanthidis2020navigation]. An important aspect of this method is to propose many diverse solution paths, so that the optimizer has a lesser chance to converge to similar solutions. This can be accomplished by leveraging sparse roadmaps[Orthey2020RAL], to generate diverse initial trajectories which we can then send to the trajectory optimizer[dai2018improving, park2015parallel, Orthey2020WAFR]. The closest work to ours is[hartmann2020planning], where RRT* is integrated with a nonlinear optimizer in an iterative fashion.

Our method is complementary, in that we also use the path-proposal method. However, we differ from previous works by our choice of the underlying components (BIT* and KOMO) and/or the interface. Further, the novel collision checking improves the performance in problems involving narrow passages, when the sampling-based planner fails to find a path in the first place.

## Problem Definition

We consider a motion planning problem in a configuration space $\mathcal{X} \subset \mathbb{R}^n$ of the form ($\mathcal{X}_{\text{free}}, x_{\text{start}}, x_{\text{goal}}, c$) where $\mathcal{X}_{\text{free}}\subseteq\mathcal{X}$ is the free configuration space, $x_{\text{start}} \in \mathcal{X}_{\text{free}}$ is the start configuration, $x_{\text{goal}} \in \mathcal{X}_{\text{free}}$ is the goal configuration and $c: \mathcal{P} \to \mathbb{R}$ is the cost functional mapping a trajectory $p \in \mathcal{P}$ in the free configuration space to a real number. Our goal is to find a trajectory $p: \to \mathcal{X}_{\text{free}}$ from $p = x_{\text{start}}$, to $p = x_{\text{goal}}$ that is optimal, i.e. the value of $c(p)$is the lowest among all possible paths.

\text{s.t.}\quad & p = x_{\text{start}}, p = x_{\text{goal}}\\& \forall t \, p(t) \in \mathcal{X}_{\text{free}} ~.

In this paper, we focus on path-length optimization, i.e. $c(p) = \int_0^1{||\dot{p}(t)||~dt}$. Typical examples of alternative cost functionals are the sum of the velocities squared $\int_0^1{||\dot{p}(t)||^2~dt}$, and smoothness $\int_0^1{||\ddot{p}(t)||^2~dt}$.

## BITKOMO

BITKOMO integrates two state-of-the-art motion planners: BIT* and KOMO. BIT* is an anytime, asymptotically-optimal planner that samples collision-free configurations in batches and generates paths using the A* graph search algorithm. KOMO is a non-linear trajectory optimizer that locally optimizes an initial trajectory (possibly in collision) to minimize a cost and fulfil collision avoidance and goal constraints. Our planner maintains the asymptotic optimality guarantees of BIT* while converging faster to the global minimum by leveraging trajectory optimization. Since KOMO uses the Augmented Lagrangian algorithm for constrained optimization, it can sometimes push partially invalid paths out of collision. To exploit this feature, we introduce relaxed edge checking, which allows BIT* to produce partially infeasible paths for subsequent optimization with KOMO when necessary.

### The BITKOMO Algorithm: An overview

Overview of BITKOMO, which combines the BIT* architecture with our custom relaxed edge checking for path planning, and the KOMO optimizer for path optimization.

Our planner (Fig. [fig:overview]) requires a valid start state ($x_{\text{start}}$), a goal state ($x_{\text{goal}}$) and the full information about the environment ($\mathcal{X}_{\text{free}}$). We also need to provide the Planner Termination condition ($PTC$) and the edge relaxation number ($\delta$). To begin, the BIT* planner samples a batch of configurations $x \in \mathcal{X}_{\text{free}}$ and builds an edge-implicit Random Geometric Graph (RGG)[penrose2003random][Block A in Fig. [fig:overview]]. The best edge that can possibly improve the cost to goal (as in A*) is then chosen and passed to the Relaxed Edge Checker[B] to carry out the collision checking. The Relaxed Edge Checker performs a validity check and returns the collision penalty ($\mathcal{CP}$), an integer that provides a proxy measure for the fraction of the edge that is in collision. The planner uses this integer to decide regarding the addition of the edge to the tree. If an improved path to the goal is found, it is passed to the KOMO optimizer[D] which locally optimizes the path and, if valid, returns the new cost to the BIT* planner. BIT* uses this path cost to prune the unnecessary vertices and edges and carry out a more focused search. When no new edges can be expanded, the Sample function[C] is called, which adds another batch of samples to the RGG.

Input $\mathcal{X}_{\text{free}},x_{\text{start}},x_{\text{goal}},PTC,\delta$ $\mathcal{V} \gets \{x_{\text{start}}\}$; $\mathcal{E} \gets \emptyset$; $\mathcal{T} \gets (\mathcal{V},\mathcal{E})$; [overlay,remember picture] (top1); $\mathcal{Q}_V \gets V$; $\mathcal{Q}_E \gets \emptyset$; $X_{\text{uc}} \gets x_\text{goal}$; $c_i \gets \infty$; $c_{\text{best}} \gets \infty$; $c_\text{max} \gets \Call{GetDiagonalLength}{\mathcal{X}} \times 3$; [overlay,remember picture] (bottom1); $\mathcal{Q}_E \equiv \emptyset$ and $\mathcal{Q}_V \equiv \emptyset$ [overlay,remember picture] (top2); $X_{\text{uc}} \overset{\mathrm{+}}{\gets} \Call{Prune\&Sample}{\mathcal{T}, X_{\text{uc}}, m, c_i}$; [overlay,remember picture] (bottom2); $\Call{BestValue}{\mathcal{Q}_V} \le \Call{BestValue}{\mathcal{Q}_E}$ [overlay,remember picture] (top3); $\Call{ExpandNextVertex}{\mathcal{Q}_V,\mathcal{Q}_E,c_i}$; $E = \{v_\text{min},x_\text{min}\} \gets \Call{PopBestInQueue}{\mathcal{Q}_E}$; [overlay,remember picture] (bottom3); $\Call{EdgeAdditionHelps}{E,c_i}$ [overlay,remember picture] (top4); $\mathcal{CP} \gets \Call{CheckEdgeRelaxed}{E}$; $\mathcal{CP} \le \delta$ If true, Edge is used[overlay,remember picture] (right); $c_\text{edge} \gets \hat{c}(E) + \mathcal{CP} \times c_\text{max}$; $\Call{EdgeImprovesCost}{E,c_i, c_{\text{edge}}}$ $\Call{AddEdgeToTree}{E}$; [overlay,remember picture] (bottom4); $c_i \gets \Call{GetCostToGo}{v_{\text{goal}}}$; [overlay,remember picture] (top5); $c_{\text{best}} \gets c_i$; $path \gets \Call{GetBestPath}{v_{\text{goal}}}$; $optiPath \gets \Call{Optimize}{path}$; $\Call{isValid}{optiPath}$ $c_i \gets \Call{GetCost}{optiPath}$; $c_{\text{best}} \gets c_i$; [overlay,remember picture] (bottom5); [overlay, remember picture] [decoration=brace,amplitude=0.5em,decorate,ultra thin,black] ($(right)!(top1.north)!($(right)-$)$) ($(right)!(bottom1.south)!($(right)-$)$) node [align=center, text width=.5cm, pos=0.5, anchor=west] A; [overlay, remember picture] [decoration=brace,amplitude=0.5em,decorate,ultra thin,black] ($(right)!(top2.north)!($(right)-$)$) ($(right)!(bottom2.south)!($(right)-$)$) node [align=center, text width=.5cm, pos=0.5, anchor=west] B; [overlay, remember picture] [decoration=brace,amplitude=0.5em,decorate,ultra thin,black] ($(right)!(top3.north)!($(right)-$)$) ($(right)!(bottom3.south)!($(right)-$)$) node [align=center, text width=.5cm, pos=0.5, anchor=west] C; [overlay, remember picture] [decoration=brace,amplitude=0.5em,decorate,ultra thin,black] ($(right)!(top4.north)!($(right)-$)$) ($(right)!(bottom4.south)!($(right)-$)$) node [align=center, text width=.5cm, pos=0.5, anchor=west] D; [overlay, remember picture] [decoration=brace,amplitude=0.5em,decorate,ultra thin,black] ($(right)!(top5.north)!($(right)-$)$) ($(right)!(bottom5.south)!($(right)-$)$) node [align=center, text width=.5cm, pos=0.5, anchor=west] E; [Algo:BITKOMO] describes in more detail the different parts of the planner. The highlighted lines are our addition to the BIT* planner. Blue the Relaxed edge collision checking, Orange the interface between BIT* and KOMO.

### Initialize (A)

Vertex set ($\mathcal{V}$), Edge set ($\mathcal{E}$), Tree ($\mathcal{T}$), Vertex queue ($\mathcal{Q}_V$), Edge queue ($\mathcal{Q}_E$), Set of unconnected vertices ($X_{\text{uc}}$). Also initialize three important cost parameters: 1) $c_i$ cost used by the BIT* tree, it includes infeasible paths; 2) $c_{\text{best}}$ the cost of the best feasible path; 3) $c_\text{max}$ a penalty cost higher than any feasible path BIT* could converge to.

### Batch Addition (B)

When we run out of the batch samples (line[Algo:BITKOMO:BathAdditionCondition]), we prune our graph using the ellipsoid method and add a new batch of samples[gammell2020batch].

### Edge Selection (C)

(The A* search) If expanding a vertex can help improving the cost of our solution, it is expanded, i.e., relevant vertices and edges are added to their respective queues (line[Algo:BITKOMO:ExpandNextVertex])

### Edge processing (D)

Decides whether to add new edge to the tree. If the new edge can improve the overall cost to goal (line[Algo:BITKOMO:EdgeAdditionHelps]), and the edge is collision free / partially in collision (line[Algo:BITKOMO:RelaxedCollisionChecking],[Algo:BITKOMO:collisionThreshold]) such that it still is a good edge to add (line[Algo:BITKOMO:EdgeImprovesCost]), it is added to the tree (line[Algo:BITKOMO:AddEdgeToTree]). $\Call{AddEdgeToTree}$rewires the tree if necessary.

### KOMO Optimization (E)

If the addition of the new edge provides us with a better path to goal, this solution path is optimized using KOMO (line[Algo:BITKOMO:optiPath]). The resulting path($optiPath$) is then checked for validity and the costs ($c_i$ and $c_{\text{best}}$) are updated accordingly. For completeness, we also check if the initial guess is valid by checking if the path cost is less than $c_\text{max}$ (line[Algo:BITKOMO:isPathFeasible]) and update $c_{\text{best}}$ if valid. The working of KOMO is explained in [KOMO].

Levels in Edge Checking The edge is first subdivided into $n_d$ points and these points are then checked for collision level by level. The number on the nodes represent the level of the node. This example has 3 levels.

### Relaxed Edge Checking

High dimensional spaces containing narrow passages are challenging for sampling based planners. This is because it is difficult to sample collision free edges through narrow passages. Since KOMO can push paths out of obstacles, we could allow paths partially in collision into the BIT* tree. However, these edges need to be added with sufficient collision penalty to ensure that BIT* does not mistake a path in collision to be of a lower cost than the true minima. We also want our collision checker to quickly guess the extent of collision so as to be quick in finding a solution for BIT*. We solve this problem by introducing Relaxed Edge Checking which returns a number instead of a Boolean which is used to assign a collision penalty (line[Algo:BITKOMO:AddingCollisionCost]). It returns 0-if edge is collision free, 1-if it fails at the last level, 2-if it fails on the second to last level, and so. Adding the collision penalty this way also helps our planner to prefer collision free initial paths for optimization as the likelihood of finding a feasible trajectory from a collision-free path is higher.

Suppose for a given resolution, we need to check $n_d$ equally spaced points to confirm the edge to be collision-free. The Relaxed Edge Checker conducts a level wise collision checking (see Fig.[fig:levels]) whereby the resolution of checking is increased until the required resolution is reached or a collision is detected. We first check the mid point (level 1), then the quarter points (level 2) and so on by slowly doubling the resolution of checking. If a point fails in the validity check, an integer, collision penalty($\mathcal{CP} = \mathcal{L} - \mathcal{L}_c + 1$) is returned. Where $\mathcal{L} = \ceil{\log_2n_d}$ is the total number of levels, and $\mathcal{L}_c$is the level of the failed point. This number provides a proxy measure for the fraction of the edge that is in collision.

### KOMO

K-Order Markov Optimization (KOMO) is a trajectory optimization framework that represents a path with a discrete sequence of waypoints $\langle x_0 \ldots x_T \rangle$. Cost and constraints are evaluated, up to $k+1$ consecutive waypoints (Markov assumption) \min_{x_{0:T}}\quad & \sum_{t=0}^T f_t(x_{t-k:t})^\top f_t(x_{t-k:t})\\\text{s.t.}\quad &\forall t: g_t(x_{t-k:t}) \le 0, h_t(x_{t-k:t}) = 0 ~, where $x_{t-k:t}$ is a $k+1$ tuple of consecutive states. In our setting, where the goal is to minimize the path length, $k=1$, and we use, as cost, the sum of squared distances $\sum || x_t - x_{t-1} ||^2$, which corresponds to $f_t(x_{t-1},x_{t}) = x_{t}-x_{t-1}$.

Inequality constraints correspond to collision avoidance and joint limits and equality constraints model the terminal goal condition The optimization problem [eq:KOMO] is solved with the Augmented Lagrangian algorithm for constrained optimization. The Markov structure, together with second order information, enables very efficient solving, with complexity linear on the number of waypoints and polynomial on the dimension of the configuration space [toussaint2014newton].

### Convergence and Optimality Guarantees

BITKOMO maintains the convergence and optimality guarantees of BIT* [gammell2015batch]. The additional trajectory optimization can only improve the solution proposed by BIT* (lines 26-30 in Alg. [Algo:BITKOMO]). The relaxed edge checking assigns cost $c>c_{\text{max}}$ (line 18 in Alg. [Algo:BITKOMO]) to any edge in collision (recall that $c_{\text{max}}$ is an upper bound on the optimal solution cost, that can be chosen arbitrarily large). Even if the subsequent optimization fails, the edge cost does not prevent BIT* and hence BITKOMO from finding a solution with cost $c<c_{\text{max}}$.

## Evaluation

Kuka from shelf Kuka into box Two Mobile Pandas One Mobile Panda Scenarios used in our experimental evaluation. See the supplementary video for the solution trajectories.

Disc Robot in Rooms Kuka from shelf Kuka into the box Two Mobile Pandas One Mobile Panda Success rates and best cost plots for 0.1cm BITKOMO, 0.1cm BIT*, 0.1cm FMT* and 0.1cm KOMO on the 6 different example environments.

### Scenarios

We evaluate our algorithm on 6 different robotic scenarios. In all scenarios, the robot moves from the initial configuration (solid color) to the goal configuration (translucent color) (Fig.[fig:Scenarios]). The trajectories computed by BITKOMO and the baseline algorithms are shown in the supplementary video We emphasize the challenges of each problem with the keywords: narrow passage, not informative heuristic and high-dimensional.

- Disc Robot in Rooms: A Disc Robot needs to move from the center of one room to another (Fig. [fig:Scene\_DiscRooms]). The difficulty is that, to go to the other room, the robot first needs to come out of the starting room and then move to the target room. Challenges: narrow passages and not informative heuristic. - Kuka to reach onto the shelf: The Kuka robot needs to reach the red object at level 1 from it's current position where the end-effector is at level 2 (Fig.[fig:Scene\_KukaShelf]). - Kuka to reach into a box: The Kuka Robot needs to reach to the object inside the box that is located under a table while avoiding collision with the table or the box (Fig. [fig:Scene\_KukaBox]). Challenges: Narrow Passage, High Dimensional. - Two Fixed Pandas: The robotic manipulators (Pandas) need to get to the base of the opposite robot while avoiding hitting each other (Fig. [fig:Scene\_Pandas]). Challenges: High Dimensional. - Two Mobile Pandas in cluttered environment: Two mobile panda robots need to move to the other side of the room while avoiding obstacles and also avoiding each other (Fig. [fig:Scene\_twoMobilePandas]). Challenges: High Dimensional, Narrow Passages. - One Mobile Panda to avoid large obstacle: The mobile panda needs to move to catch an object on the other side of the scene, with a large obstacle blocking it's way (Fig. [fig:Scene\_oneMobilePanda]). Challenges: High Dimensional, Narrow Passages.

### Baselines

We compare our BITKOMO planner with BIT*[gammell2015batch], KOMO[toussaint2014newton] and FMT*[janson2015fast]. Path length minimization is used as the optimization objective for all the experiments. We used the Open Motion Planning Library (OMPL)[sucan2012open]framework for the implementations of the sampling based planners and for carrying out the benchmarks.

For the KOMO planner we use the sum of squares of the distances between waypoints as optimization objective, and an initialization with random noise around $p(t_i) = x_{\text{start}} ~ \forall t_i$. The trajectory is represented with a constant number of waypoints (20 points). Random initialization and optimization are executed iteratively until timeout, updating the path cost when a better path is found.

### Metrics

We evaluate the planners on 2 different metrics:

- Success rate (%): The % of runs that have found a feasible solution at time $t$. This metric gives information about how fast the planner finds the first feasible path. - Cost: The average best cost of the planner at time $t$. This metric gives us an understanding about how the best cost solution of a planner evolves over time and the practical convergence speed before the timeout.

### Experimental Results

For getting unbiased results, all experiments were conducted on the same machine Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz having 16GB RAM. Every planner was executed 50 times on all the six example scenarios. The maximum execution time however was different for different scenarios depending on the difficulty. The edge relaxation number $\delta$ was set to 1 for all examples. The results of the benchmarks are shown in Fig. [fig:benchmarks].

### Success rate

The success rate of BIT* and BIKOMO were higher compared with other planners in all examples except the Two Mobile Pandas example. This scenario has narrow passages which makes it hard for sampling based planners, however, the optimal solution is very similar to a straight line path in the configurations space, making it very easy for KOMO to find a solution here. The relaxed edge checking helps BITKOMO in having a slightly better success rate than BIT* here. The anomaly in BIKOMO success rate in Fig.[fig:Two\_Pandas] is because of a failed optimization. This failure is because of the thin obstacles in the C-Space arising due to collision between robots. This, however, is not a large time difference. Choosing a smaller edge relaxation number, $\delta$, will fix it. Overall, the success rates of BIT* and BITKOMO were found to be very similar because they generate initial paths using the same base algorithm.

### Cost

BITKOMO decreases the cost significantly faster than BIT*, with better convergence before the timeout. This is because the combination of sampling and optimization converges to the local minima quickly and consistently. We however see an abnormality in Fig.[fig:Disc\_rooms]. This is because 1) KOMO is not much faster than sampling for low dimensions, and 2) The waypoints maintain a certain minimum distance from the obstacles to avoid edge collisions.

Overall, we conclude that our planner is mostly as good as BIT* in finding the first feasible solution and slightly faster in high dimensional narrow passage problems, but much faster at converging to the global optimal solution.

## Discussion and Conclusion

Our planner, BITKOMO, combines BIT* and KOMO to achieve fast convergence to the optimal solution while being anytime and asymptotically converging to the global minimum. Our experiments indicate that BITKOMO converges to the global optima, faster than BIT*. It also provides convergence guarantees which KOMO does not. Using Relaxed Edge Checking, our planner exploits the ability of KOMO to move trajectories away from the obstacles that are in collision by allowing partially infeasible paths as initial guesses to the optimizer. This helps BITKOMO find motions through narrow passages faster than BIT*.

Even though we observe faster convergence than BIT* to optimal paths, our planner does not have a better success rate. A dedicated planner could be developed to generate improved initial guesses to the optimizer, resulting in an increased success rate.

The optimization and sampling modules could also easily be parallelized, providing a higher speed-up. Calling the KOMO optimizer ahead of the BIT* planner could increase the speed further.

Our experiments clearly demonstrate that BITKOMO can robustly achieve fast convergence to optimal motion plans. This is an important step towards making optimal motion planners converge as quickly as trajectory optimizers all while keeping asymptotic optimality guarantees.
