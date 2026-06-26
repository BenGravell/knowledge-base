<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Efficient B-spline-Based Kinodynamic Replanning Framework for Quadrotors

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Trajectory replanning for quadrotors is essential to enable fully autonomous flight in unknown environments. Hierarchical motion planning frameworks, which combine path planning with path parameterization, are popular due to their time efficiency. However, the path planning cannot properly deal with non-static initial states of the quadrotor, which may result in non-smooth or even dynamically infeasible trajectories. In this paper, we present an efficient kinodynamic replanning framework by exploiting the advantageous properties of the B-spline, which facilitates dealing with the non-static state and guarantees safety and dynamical feasibility. Our framework starts with an efficient B-spline-based kinodynamic (EBK) search algorithm which finds a feasible trajectory with minimum control effort and time. To compensate for the discretization induced by the EBK search, an elastic optimization (EO) approach is proposed to refine the control point placement to the optimal location. Systematic comparisons against the state-of-the-art are conducted to validate the performance. Comprehensive onboard experiments using two different vision-based quadrotors are carried out showing the general applicability of the framework.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous navigation for quadrotors in unknown environments has gained significant interest for its practical usage in various inspection and exploration tasks. To fulfill the need of fully autonomous exploration in unknown environments, trajectory replanning is of great significance. Replanning requires a real-time response to unexpected obstacles to guarantee safety while satisfying the low-level feasibility constraints induced by the non-trivial dynamics.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many existing methods tackle this challenging problem using a hierarchical framework, which first finds a geometric path and then locally optimizes the path to a dynamically feasible trajectory with respect to a given time allocation. Although this framework is efficient, inadequacy exists between the path finding and the local path parameterization. Specifically, the parameterization may be restricted by the geometric path to a homotopy class that does not contain a globally optimal (or even feasible) solution, especially when faced with non-static initial states (non-zero velocities or any other higher-order derivatives), as shown in Fig. 1.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

(a) Monocular Vision-Based Quadrotor Testbed (b) Dual-fisheye Vision-Based Quadrotor Testbed Figure 2: Illustration of our (a) monocular vision-based quadrotor testbed and (b) dual-fisheye vision-based quadrotor testbed.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address the limitations of the hierarchical methods, it is essential to use kinodynamic motion planners, which directly find time-parameterized trajectories that are globally optimal with respect to control efforts and dynamical limits. The incorporation of kinodynamic planners into replanning facilitates dealing with non-static initial states and enhances replanning consistency.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sampling-based motion planning algorithms, such as rapidly-exploring random trees (RRTs) and their variants, are popular in the kinematic/kinodynamic planning literature. Asymptotical optimality has been proved for some of them. However, when applied to complex kinodynamic systems, they typically require solving a computationally expensive non-linear two-point boundary value problem (BVP) and cannot run in real-time. Liu et al. explored a search-based counterpart and proposed a heuristic-guided resolution-complete (optimal with respect to discretization) search method using linear quadratic minimum time control. However, for high-order kinodynamic systems or a large dynamic range, the run-time efficiency is inadequate.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present a kinodynamic replanning framework which addresses the efficiency bottleneck. Our framework starts with an efficient B-spline-based kinodynamic (EBK) search algorithm, which finds B-spline control points on a spatial grid. We introduce the novel concept of vertex tuple to keep the search problem simple and analyzable, which enables a thorough theoretical characterization of the problem. Built on top of the structure of the optimal solution, a graph aggregation technique is proposed to minimize the computation time through a controllable discretization of the search space. An offline-computable minimum inflation is adopted to avoid unnecessary collision checking and further accelerate the online search. Compared to state-of-the-art methods (Sect. VIII), our kinodynamic search finds the lowest-cost dynamically feasible trajectories in real time.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To compensate for the discretization in the search, an elastic optimization (EO) approach is proposed to refine the control point placement to the optimal location, by solving a convex quadratically constrained quadratic programming (QCQP) problem. The two components are integrated into a receding horizon replanner based on the local control property of the B-spline.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our replanning framework is not only theoretically analyzed, but also validated in simulated and onboard experiments. Superior performance is shown through comprehensive comparisons against the state-of-the-art kinodynamic planning and trajectory optimization methods. Moreover, the practical impact of our framework is verified through onboard experiments using a monocular vision-based quadrotor and a dual-fisheye vision-based quadrotor in unknown indoor and outdoor environments. We summarize our contributions as follows: An EBK search algorithm which provides an initial-state-aware dynamically feasible time-parameterized trajectory.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

An EO approach that refines the control point placement to the optimal location while preserving the safety and dynamical feasibility.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Systematic comparisons against the state-of-the-art showing the superior performance of the proposed framework.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Integration of our framework into a real monocular vision-based quadrotor and a dual-fisheye vision-based quadrotor as well as extensive experiments demonstrating fully autonomous navigation in unknown, complex indoor and outdoor environments.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

A basic version of our framework was originally presented, where we introduced the real-time B-spline-based kinodynamic (RBK) search. Although the RBK search achieves high computational efficiency, the absence of theoretical optimality analysis in limits confidence in its solution quality and further limits its theoretical impact. In this paper, instead of directly developing efficient methods, we tackle the kinodynamic search problem in a systematic way: 1) We first characterize the complexity and optimal solution of the search problem using a novel vertex tuple structure. 2) We then establish the quality-efficiency tradeoff using a novel graph aggregation technique, which provides a user-specified parameter to control algorithm efficiency and solution quality. The above two theoretical additions render the more flexible and theoretically reliable EBK search. It also turns out that the preliminary version in is perfectly contained in the EBK search. Apart from the theoretical additions, more comprehensive experimental analyses in a wide variety of environments are presented to support the new characteristics.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

The relevant literature is discussed in Sect. II. An overview of the proposed replanning framework is provided in Sect. III. Mathematical background and advantageous properties of B-spline are introduced in Sect. IV. The problem formulation and algorithm detail of the EBK search are elaborated in Sect. V. The EO approach is presented in Sect. VI. Implementation details are given in Sect. VII. Systematic comparisons against the state-of-the-art methods are provided in Sect. VIII, and onboard experimental results are illustrated in Sect. IX. Finally, a conclusion and further possible research directions are provided in Sect. X.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Related Works", "weight": 1.0} -->

There is extensive literature on motion planning techniques for quadrotors from various perspectives, such as control-based methods, search-based methods, sampling-based methods and optimization-based methods. It is difficult to give a full literature review of all these techniques, so in this section, we choose the most relevant and organize them into two categories, namely, hierarchical motion planning techniques and kinodynamic motion planning techniques.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Hierarchical Motion Planning", "weight": 1.0} -->

Hierarchical motion planning refers to a high-level geometric path planner coupled with a low-level time parameterization scheme. The high-level geometric planner is concerned with finding an obstacle-free path, while the low-level parameterization scheme takes care of the vehicle dynamical constraints and generates a time-parameterized trajectory for execution. For quadrotors which have non-trivial dynamics, directly generating a trajectory in the high-dimensional state space is time consuming, while smoothing a given geometric path is computationally efficient (with a suitable relaxation). As such, the hierarchical framework is popular for quadrotors, and it enables a number of online methods.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Hierarchical Motion Planning", "weight": 1.0} -->

Two pioneering works extract waypoints from the geometric path and formulate the trajectory generation problem as quadratic programming (QP) on polynomial coefficients. These methods are based on the differential flatness of the quadrotor. Due to the deviation of the polynomial trajectory from the straight-line collision-free path, an iterative waypoint insertion scheme is adopted. However, how many additional waypoints are needed is not quantified. Chen et al. propose a corridor-based geometric planner based on the octree-based map structure. The control effort can be reduced by generating the trajectory in a series of connected cubes. Apart from that, they propose an iterative process of adding constraints on polynomial extremas to cope with the deviation from the corridor, and prove that a finite number of iterations is needed to guarantee safety. Liu et al. further generalize the corridor representation to a series of connected convex polygons.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A Hierarchical Motion Planning", "weight": 1.0} -->

Although the hierarchical methods have made significant achievements, they suffer from the common problem that the geometric planner is unaware of the vehicle dynamics, resulting in inadequacy between the path planning and path parameterization, especially when faced with non-static initial states. The example in Fig. 1 motivates us to explore the problem from the kinodynamic planning perspective, which is discussed in Sect. II-B.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Kinodynamic Motion Planning", "weight": 1.0} -->

The kinodynamic motion planner directly explores the high-dimensional state space, and outputs a time-parameterized trajectory, which fundamentally avoids the inadequacy between path planning and parameterization. RRTs and their variants were originally designed for kinematic systems and can be easily extended to kinodynamic systems. These methods provide an efficient way of exploring the high-dimensional state space, and some of them possess asymptotical optimality. However, for robots with non-trivial dynamics, the tree expansion typically involves solving the BVP, which is non-linear and challenging. Webb et al. propose a fixed-final-state-free-final-time optimal controller which solves the BVP for linear (or linearized) controllable systems in closed form. Xie et al. propose an efficient BVP solver for general kinodynamic systems using sequential quadratic programming (SQP). Li et al. work in another direction, namely, expanding the tree using random control propagation, for cases where system models are complex and BVP solvers are not available.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Kinodynamic Motion Planning", "weight": 1.0} -->

Despite the fact that the efficiency of the kinodynamic planning techniques keeps improving, it is still prohibitively expensive for replanning. Allen et al. work towards a real-time kinodynamic planning framework by combining FMT\* with a support vector machine (SVM) for the classification of the reachable set. This framework reduces the calling of the BVP solver to gain efficiency. However, the solution quality largely depends on the number of states pre-sampled. On the other hand, Liu et al. explore the search-based kinodynamic planning counterpart and develop efficient heuristics by solving a linear quadratic minimum time problem. Their solution is resolution-complete with respect to the discretization on the control input, and achieves near real-time performance. Note that both and use a simplified system model, i.e., a double or triple integrator, to reduce the computation complexity. However, the resultant trajectory only has limited continuity. To improve the smoothness, both and adopt trajectory reparameterization using the unconstrained QP formulation, which may break the dynamical feasibility and safety.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Kinodynamic Motion Planning", "weight": 1.0} -->

In contrast, the proposed EBK search adopts a high-order B-spline parameterization with continuity up to snap, which can be directly used to control the quadrotor. Moreover, the advantageous properties of the B-spline facilitate the kinodynamic replanning as follows: Local control property for incrementally constructing the B-spline trajectory in the kinodynamic search and local refinement of the trajectory during replanning.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B Kinodynamic Motion Planning", "weight": 1.0} -->

Convex hull property for enforcing collision-free constraints and providing a dynamical feasibility guarantee for the entire trajectory.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Kinodynamic Motion Planning", "weight": 1.0} -->

Given the same run-time budget according to the real-time requirement, the EBK search finds a lower-cost trajectory, as validated by the comprehensive comparisons against the state-of-the-art in Sect. VIII. Apart from this, the proposed refinement module, namely, the EO approach, can preserve the safety and dynamical feasibility by taking advantage of the convex hull property of the B-spline.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Overview", "weight": 1.0} -->

The structure of the proposed framework is shown in Fig. 3. The replanning framework is built on top of the state estimation and dense mapping module, which are discussed in Sec. VII. The frequency of the grid map update is $10$ Hz. As such, the real-time requirement in this paper refers to a run-time of less than $100$ ms. The updated map and the initial state of the quadrotor are fed to the EBK search module (Sect. II-B), and the replanning strategy is elaborated in Sect. VII. The control points are constantly refined by the proposed EO approach (Sect. VI), which consists of an elastic tube expansion module (Sec. VI-A) for free space characterization and a convex optimization formulation (Sec. VI-B) for trajectory refinement. The confirmed control points are evaluated, and position commands are generated accordingly.

<!-- chunk {"id": "body-0026", "role": "body", "section": "B-spline Curve and Replanning", "weight": 1.0} -->

For the proposed kinodynamic planning framework, we adopt a B-spline parameterization for its advantageous properties, namely, local control and convex hull property, and we further adopt the uniform B-spline for its convenient closed-form evaluations. In this section, we elaborate these properties and explain how they can be applied to the replanning system.

<!-- chunk {"id": "body-0027", "role": "body", "section": "B-spline Curve and Replanning", "weight": 1.0} -->

Given $n + 1$ control points $\mathbf{p}_{0},\mathbf{p}_{1},\ldots,\mathbf{p}_{n}$ and knot vector $\{ t_{0},t_{1},\ldots,t_{m}\}$, the B-spline curve $\mathbf{s}{(t)}$ of degree $k$ is defined as follows: where $N_{i,k}{(t)}$ is the B-spline blending function of degree $k$, which can be evaluated recursively as follows: The total number of knots should satisfy ${m + 1} = {n + k + 2}$. The uniform B-spline is a special type of B-spline whose knot vector is uniformly distributed. Suppose the knot vector is separated with equidistance $\Delta_{t}$. The half-open interval $\lbrack t_{i},t_{i + 1})$ is called the $i -$th knot span.

<!-- chunk {"id": "body-0028", "role": "body", "section": "B-spline Curve and Replanning", "weight": 1.0} -->

We normalize each knot span using $u = {{({t - t_{i}})}/\Delta_{t}}$, and for the $i$-th knot span, only $k + 1$ blending functions are non-zero, corresponding to $k + 1$ control points $\mathbf{p}_{i - k},\ldots,\mathbf{p}_{i}$. We stack the $k + 1$ control points and call the stacked coordinate matrix a control point span $\mathbf{P}_{i - k} ≔ \left\lbrack {\mathbf{p}_{i - k}\mathbf{p}_{{i - k} + 1}\cdots\mathbf{p}_{i}} \right\rbrack^{\intercal} \in {\mathbb{R}}^{{({k + 1})} \times 3}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "B-spline Curve and Replanning", "weight": 1.0} -->

Since the blending functions $N_{i,k}{(t)}$ are shifted versions of each other for the uniform B-spline, we have closed-form matrix representations for parametric evaluation.

<!-- chunk {"id": "body-0030", "role": "body", "section": "B-spline Curve and Replanning", "weight": 1.0} -->

Let $j = {i - k}$, and the position and the derivatives of the B-spline curve corresponding to the $j$-th control point span can be evaluated as follows: where $l$ denotes the order of the derivative ($l = 0$ means the position), $\mathbf{b} = \left\lbrack {1uu^{2}\cdotsu^{k}} \right\rbrack^{\intercal} \in {\mathbb{R}}^{k + 1}$ denotes the basis vector, and $\mathbf{M}_{k} = {(m_{i,j})} \in {\mathbb{R}}^{{({k + 1})} \times {({k + 1})}}$ denotes the blending matrix, where $m_{i,j} = {\frac{1}{k!}\binom{k}{k - i}{\sum_{s = j}^{k}{{({- 1})}^{s -

<!-- chunk {"id": "body-0031", "role": "body", "section": "B-spline Curve and Replanning", "weight": 1.0} -->

According to Eq. 3, the evaluation of the derivatives of the B-spline curve can be expressed by a linear matrix multiplication in terms of the control point span $\mathbf{P}_{j}$. The paper uses a quintic uniform B-spline ($k = 5$) to ensure the continuity up to snap for controlling quadrotors.

<!-- chunk {"id": "body-0032", "role": "body", "section": "B-spline Curve and Replanning", "weight": 1.0} -->

As described by Mellinger, the control cost of a quadrotor is closely related to the integral over squared derivatives of the planned trajectory, which can also be evaluated in closed form in the case of the uniform B-spline. The total control cost $E_{j}^{l}$ of the $j$-th control point span can be expressed by the integral over the squared derivatives of degree $l$ (e.g., for the min-snap trajectory, $l = 4$) as follows: where $\mathbf{Q}_{l} = {\int_{0}^{1}{{\left(\frac{d\mathbf{b}}{d^{l}u} \right)\left(\frac{d\mathbf{b}}{d^{l}u} \right)^{\intercal}{du}}/{(\Delta_{t})}^{{2l} - 1}}}$ is the Hessian matrix of the $l$-th squared derivative, which is constant for the uniform B-spline.

<!-- chunk {"id": "body-0033", "role": "body", "section": "B-spline Curve and Replanning", "weight": 1.0} -->

The control cost $E_{j}^{l}$ is quadratic with respect to the control point span $\mathbf{P}_{j}$. Note that the cost evaluation of a span only depends on the stacked control point coordinates of this span.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Local Control Property and Replanning", "weight": 1.0} -->

The local control is one of the important properties of B-spline, making it suitable for replanning. Specifically, the evaluation of any point of the B-spline curve is controlled by a single control point span containing $k + 1$ control points, and any control point only affects $k + 1$ control point spans. We incorporate the local control property into a receding horizon (re-)planner, and we divide the planned trajectory into three types, namely, executed trajectory, executing trajectory and optimizing trajectory. The executed trajectory means the part of the trajectory which has already been executed, the executing trajectory means the part of the trajectory corresponding to the control point span being executed, and the optimizing trajectory means the part of the trajectory whose supporting control points are potentially under optimization.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Local Control Property and Replanning", "weight": 1.0} -->

Thanks to the local control property, modification of the supporting control points of the optimizing trajectory will not affect the evaluation of the executing trajectory, as shown in Fig. 4. Unlike and where local reshaping may cause the violation of dynamical constraints, the dynamical feasibility of the executing trajectory can be preserved by leveraging the local control property. Moreover, the locality also makes it possible to optimize any subset of control points without re-generation of the whole trajectory, which is computationally efficient. The locality also helps to preserve a smooth trajectory since the next executing control point span always shares $k$ control points with the current executing control point span, yielding $k$-th-order continuity and a consistent trajectory.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Convex Hull Property and Dynamical Feasibility", "weight": 1.0} -->

Another important property of the B-spline is the convex hull property. A B-spline (or Bèzier ) trajectory is strictly bounded inside the convex hull supported by the corresponding control point span. Strictly speaking, dynamical feasibility should be induced by the robot's kinematic and dynamical constraints. Given polynomial/spline parameterization, a common practice to enforce dynamical feasibility is to use maximum velocity and maximum acceleration bounds. We follow this practice in this paper. Note that for piecewise polynomial parameterization methods, the dynamical feasibility constraints are enforced on a finite number of checkpoints. Denser checkpoints will enhance the robustness but yield higher computation complexity. In contrast, by using the convex hull property, the entire velocity and acceleration profile can be strictly bounded.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Convex Hull Property and Dynamical Feasibility", "weight": 1.0} -->

We utilize the fact that the derivative of the B-spline of degree $k$ is a B-spline of degree $k - 1$, which also enjoys the convex hull property. Therefore, if the supporting control points are bounded inside the convex hull expanded by the allowed maximum derivative, the derivative spline is subsequently bounded, as elaborated in Prop. 1. Note that Prop. 1 is a sufficient but not necessary condition. A toy example illustrating the relation between the convex hull property and dynamical feasibility is shown in Fig. 5.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A Motivating Example", "weight": 1.0} -->

As shown in the motivating example in Fig. 1, hierarchical motion planners may produce sub-optimal or even dynamically infeasible trajectories given a non-static initial state of the quadrotor. The reason is that the geometric planner has no knowledge about the vehicle dynamics and restricts the solution space of path parameterization to a homotopy class of the geometric shortest path. The inadequacy motivates us to propose an efficient kinodynamic planning algorithm which can work in real-time. However, kinodynamic planning is typically time consuming. The major computation of the traditional kinodynamic planning lies in three tasks, namely, covering the large state space, solving the BVP and collision checking.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-A Motivating Example", "weight": 1.0} -->

Given the advantageous properties of the B-spline introduced in Sect. IV, we propose using uniform B-spline parameterization in kinodynamic planning, which facilitates reducing the computation time for the above three tasks. Specifically, we propose a spatial-grid-based deterministic graph search to place B-spline control points. The proposed search algorithm has three major features as follows: Controllable discretization of the state space: Due to the locality of the B-spline, it is possible to incrementally sample the B-spline control points during the search. A vertex tuple structure is proposed to recover the Markovian assumption and make the problem analyzable. A novel graph aggregation technique is proposed to control the discretization of the state space, which achieves a speed-quality tradeoff.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-A Motivating Example", "weight": 1.0} -->

Closed-form evaluations of control cost and dynamical feasibility: The control cost and feasibility of the B-spline can be evaluated in closed forms efficiently.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A Motivating Example", "weight": 1.0} -->

Offline-computable inflation to avoid collision checking: The maximum deviation of uniform B-spline from the free-cells can be characterized offline and compensated for by workspace inflation.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A Motivating Example", "weight": 1.0} -->

The kinodynamic search accounts for the total control efforts and dynamical limits, which is a systematic way to deal with the non-static initial states in replanning.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-B Problem Formulation", "weight": 1.0} -->

In this section, we formally present the problem of the B-spline-based kinodynamic search on a spatial grid. The problem is formalized as a deterministic graph search where the action is the placement of the control points. Suppose the topological graph associated with the grid map is denoted as $\mathcal{G} ≔ {(V,E)}$, where $V$ is the set of vertices denoting the collection of free cells and $E$ denotes the set of edges ${(i,j)} \subset {V \times V}$ between all adjacent vertices $i$ and $j$. The adjacency of the vertices depends on the grid connectivity adopted. In this paper, every cell in the 3-D grid has 26 neighbors which are cells connected to this cell at a Chebyshev distance of 1.^22^2Note that the connectivity can also be defined based on a Chebyshev distance larger than one, which will result in a non-uniform control point placement and a higher computational complexity.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-B Problem Formulation", "weight": 1.0} -->

The sequence $\pi$ possibly contains repetition since we allow placing the control points at the same cell. $\pi_{s}$ and $\pi_{g}$ are two tuples, both containing $k + 1$ vertices which form the control point span according to the definition of the B-spline in Sect. IV. Therefore, $\pi_{s}$ and $\pi_{g}$ actually represent two short trajectories, different from the initial and goal positions used in geometric planners and the position-velocity-acceleration state vector used in these kinodynamic planners.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-B Problem Formulation", "weight": 1.0} -->

Since the B-spline is evaluated in terms of the control point span, we re-organize $\pi$ by combining neighboring $k + 1$ vertices as one vertex tuple. Combining the sequence $\pi$ with $\pi_{s}$ and $\pi_{g}$, the overall sequence can be formalized as $\overset{\sim}{\pi} = {(v_{s}^{0},\ldots,v_{s}^{k},v_{0},\ldots,v_{T},v_{g}^{0},\ldots,v_{g}^{k})}$. We define the ordered sub-sequence containing consecutive $k + 1$ vertices of $\overset{\sim}{\pi}$ as a $k$-degree vertex tuple, which is denoted by ${\lbrack\overset{\sim}{\pi}\rbrack}^{k}$. We provide a toy example in Fig. 6 showing how $3$-degree vertex tuples can be constructed.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B Problem Formulation", "weight": 1.0} -->

Each vertex tuple represents a short trajectory, and a sequence of neighboring vertex tuples represents a continuous trajectory. We associate with each $k$-degree tuple $\lbrack\overset{\sim}{\pi}\rbrack$ a strictly positive cost function $f_{k,\Delta_{t}}:{{\lbrack\overset{\sim}{\pi}\rbrack}^{k}\rightarrow{\mathbb{R}}_{+}}$. Note that the cost function has to be strictly positive to cope with the possible repetition in $\pi$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Given a uniform B-spline of degree $k$ and knot separation $\Delta_{t}$, initial state $\pi_{s}$ and goal state $\pi_{g}$, find admissible control point placement $\pi = {(v_{0},v_{1},\ldots,v_{T})}$ on $\mathcal{G}$ such that the following cost function is minimized: where ${\lbrack\overset{\sim}{\pi}\rbrack}_{j}^{k}$ is a $k$-degree vertex tuple, whose corresponding trajectory should satisfy collision-free and dynamical feasibility requirements.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Problem 1", "weight": 1.0} -->

We adopt a cost function following the idea of the linear quadratic minimum time control problem, where the control cost is represented by Eq. 4 with a tradeoff penalty on the execution time $\Delta_{t}$. Mathematically, the cost function $f_{k,\Delta_{t}}$ is represented as follows: where ${\lbrack\overset{\sim}{\pi}\rbrack}_{j}^{k}$ can be rewritten into matrix form, as in Sect. IV; the integral can be evaluated according to Eq. 4; and $\lambda$ is the weight for the trajectory execution time. The criterion to check the collision-free and dynamical feasibility of the vertex tuple is introduced in Sect. V-D.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-C Optimal B-spline-Based Kinodynamic Search", "weight": 1.0} -->

The difficulty of solving Prob. 1 is that the placement of any control point depends on the placed $k$ control points (not only the predecessor) within the vertex tuple. Regarding the placement of a single control point as an action, the Markovian assumption does not hold, which makes traditional graph search algorithms inapplicable. However, we find that Problem 1 can be transformed into an equivalent standard shortest path problem on a higher dimensional directed graph $\mathcal{G}_{H} = {(V_{H},E_{H})}$ induced by $\mathcal{G}$ by regarding the whole vertex tuple as a "vertex". Since the vertex tuple is the basic evaluation unit of the B-spline, the placement of the next vertex tuple will only depend on its predecessor, which follows the Markovian assumption. The transformation enables the usage of well-characterized shortest path search algorithms, such as Dijkstra's and A\*. In the following, we elaborate the transformation.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-C Optimal B-spline-Based Kinodynamic Search", "weight": 1.0} -->

The construction of $\mathcal{G}_{H}$ groups the associated control point coordinates into a high-dimensional state. Note that each dimension of the combined state has the same physical meaning, i.e., the spatial coordinates of the control point. This observation motivates us to come up with a low-dispersion search algorithm, as presented in Sect. V-E.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-C Optimal B-spline-Based Kinodynamic Search", "weight": 1.0} -->

In Fig. 7(a), we show an example of how the trace of control points on $\mathcal{G}$ can be mapped to the path on $\mathcal{G}_{H}$. The initial vertex tuple ${\hat{v}}_{s}$ is shown by squares. Starting from ${\hat{v}}_{s}$, we consider two directions of the next-step placement, which form ${\hat{v}}_{0}$ and ${\hat{v}}_{1}$, respectively. In a similar way, starting from ${\hat{v}}_{0}$, two expansion directions are considered, forming ${\hat{v}}_{3}$ and ${\hat{v}}_{4}$, while for ${\hat{v}}_{1}$, one direction (${\hat{v}}_{5}$) is considered.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-C Optimal B-spline-Based Kinodynamic Search", "weight": 1.0} -->

Note that although the last vertex of ${\hat{v}}_{4}$ and ${\hat{v}}_{5}$ are in the same spatial cell, in the induced high-dimensional graph $\mathcal{G}_{H}$, they are two distinct vertex tuples. Following the expansion of control points, we form a tree of vertex tuples on $\mathcal{G}_{H}$. From the expansion process, we observe that, given the initial and goal vertex tuple, the problem of finding the optimal control point placement is equivalent to finding the shortest path on the graph $\mathcal{G}_{H}$. We refer interested readers to Appendix -B for further details.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-C Optimal B-spline-Based Kinodynamic Search", "weight": 1.0} -->

15: if not Visited (n, ℒ) then 17: if ${g{({\hat{v}}_{j})}} > {{g{({\hat{v}}_{i})}} + \underset{¯}{f_{k,\Delta_{t}}{({\hat{v}}_{j})}}}$ then Algorithm 1 Optimal B-spline-Based Kinodynamic Search Recall that in Sect. V-B, we allow the repetition of vertices since some necessary vertex tuples rely on repetition; for instance, the same vertex being repeated $k + 1$ times actually represents a static state (for $\Delta_{t}$). According to the definition of $f_{k,\Delta_{t}}{({\lbrack\overset{\sim}{\pi}\rbrack}^{k})}$, the cost of $\mathcal{G}_{H}$ is defined on vertices $V_{H}$ instead of the edges.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-C Optimal B-spline-Based Kinodynamic Search", "weight": 1.0} -->

Although repetition is allowed, each vertex $\hat{v} \in V_{H}$ of $\mathcal{G}_{H}$ is associated with a strictly positive cost so that repetition is properly penalized.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-C Optimal B-spline-Based Kinodynamic Search", "weight": 1.0} -->

Note that any path on $\mathcal{G}_{H}$ is a time-parameterized B-spline trajectory instead of a geometric path. The dynamical feasibility and control cost are taken into account by evaluating the corresponding short trajectories of the nodes of $\mathcal{G}_{H}$. Problem 1 can be solved optimally using traditional label-correcting algorithms such as Dijkstra's and A\* on the induced graph $\mathcal{G}_{H}$. The optimal control point placement $\pi^{\ast}$ can then be re-constructed. The optimal B-spline-based kinodynamic (OBK) search algorithm is outlined in Algo. 1.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-C Optimal B-spline-Based Kinodynamic Search", "weight": 1.0} -->

Typically, label-correcting algorithms maintain one or multiple sets of vertices as so-called fringes. For example, A\* maintains two fringes (known as the OPEN set and the CLOSED set) to reduce the expansion of nodes and save computation. Similarly, Algo. 1 maintains two fringes, namely, the OPEN set (as denoted by $\mathcal{O}$) and the VISITED set (as denoted by $\mathcal{L}$). The visited set $\mathcal{L}$ provides query and retrieving functions for vertices. We use Index$(\hat{v})$ (Algo. 2) to assign a unique integer index to each distinct vertex tuple. Specifically, Algo. 2 collects the extracted coordinates $\mathcal{I}{(\hat{v})}$ (using the Coord$(v)$ function) for each vertex $v$ in the tuple $\hat{v}$, and uses the UniqueEncode$( \cdot )$ function to generate a unique hash encoding for a series of integer coordinates $\mathcal{I}{(\hat{v})}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-C Optimal B-spline-Based Kinodynamic Search", "weight": 1.0} -->

We construct the nodes of $\mathcal{G}_{H}$ only on demand during the search process as the graph size may be prohibitively large. At the beginning of the search, the whole $\mathcal{G}_{H}$ is not explicitly constructed, and the visited set $\mathcal{L}$ and the open set $\mathcal{O}$ are both initialized to empty. After the insertion of the initial state $\pi_{s}$, a tree of nodes is gradually expanded based on the $\text{FeasibleSuccs}{( \cdot )}$ function and the priority queue structure maintained by $\mathcal{O}$. Every time a new node is found (whether or not a successor node is a new node is identified by $\mathcal{L}$, which is implemented using a hash map structure), the node is added to $\mathcal{L}$ to trace its open/closed status. In practice, only a small proportion of the nodes of $\mathcal{G}_{H}$ are constructed before the search succeeds.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-C Optimal B-spline-Based Kinodynamic Search", "weight": 1.0} -->

A toy example^33^3The setup of this example is the same as the qualitative experiment in Fig. 10, where the grid size is $51 \times 51 \times 5$ and the B-spline degree is five. which compares the number of actual expanded nodes with the estimated graph size is shown in Tab. I. Note that the EBK method used in Tab. I is an efficient version of Algo. 1, which is discussed in detail in Sect. V-E. The estimated graph size is computed based on the graph aggregation technique introduced in Sect. V-F.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-C Optimal B-spline-Based Kinodynamic Search", "weight": 1.0} -->

Actual # of Exp. Nodes Total # of Nodes (Esti.)

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-C Optimal B-spline-Based Kinodynamic Search", "weight": 1.0} -->

Note that there are three functions making Algo. 1 different from the traditional geometric path search: 1) the cost function $f_{k,\Delta_{t}}{( \cdot )}$ evaluates the control effort of the k-degree vertex tuple, instead of a simple path length measure; 2) the function Index$( \cdot )$ regards the k-degree vertex tuple as the "state", which expands the high-dimensional state space supported by the control point coordinates, while the geometric path search typically regards positions as states; and 3) the function FeasibleSuccs$( \cdot )$ will expand to the neighboring k-degree tuples with dynamical feasibility checking, while the geometric path search cannot check feasibility without parameterization. As for the heuristic function $\text{Heuristic}{( \cdot )}$, we adopt the admissible minimum time heuristic.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-C Optimal B-spline-Based Kinodynamic Search", "weight": 1.0} -->

Algorithm 2 Given a k-degree vertex tuple v̂ ∈ VH, assign a unique index to each distinct tuple.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-C Optimal B-spline-Based Kinodynamic Search", "weight": 1.0} -->

It is worth noting that the design of Algo. 1 heavily relies on the properties of the B-spline. Thanks to the local control property, the cost evaluation and feasibility checking can be done locally based on the k-degree vertex tuple. Instead of solving the BVP, the proposed search method expands to new states on the high-dimensional graph $\mathcal{G}_{H}$ by expanding low-dimensional control point coordinates, which are associated with closed forms for cost evaluation. Moreover, checking for collision is time consuming in traditional kinodynamic planners. By using B-spline parameterization, the process can be avoided by characterizing the B-spline deviation, as introduced in Sect. V-D. The limitation of our method is that the expansion of control points is restricted by the resolution and connection of the grid, which results in limited representations of B-spline trajectories.

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-D Feasibility Condition", "weight": 1.0} -->

The dynamical feasibility of the k-degree vertex tuple can be validated via checking the extrema of the derivative of the B-spline. Since the derivative of the B-spline is another B-spline with decreasing degree, the velocity spline is of degree $k - 1$ and the acceleration spline is of degree $k - 2$. Considering that the convex hull property in Prop. 1 is a sufficient but not necessary condition, directly using Prop. 1 for feasibility checking may be conservative. Actually, there is a non-conservative approach for feasibility checking by using the closed-form solutions of the extremas of the uniform B-spline. Take the fifth-degree uniform B-spline as an example. The B-spline can be rewritten in a monomial basis according to Eq. 3. The velocity profile is a degree-$4$ polynomial whose extremas can be checked by finding the roots of its derivative (degree-$3$) in closed form.

<!-- chunk {"id": "body-0064", "role": "body", "section": "V-D Feasibility Condition", "weight": 1.0} -->

For traditional kinodynamic planners, collision checking is an expensive process and may become the computation bottleneck of the algorithm. Position-only shortest path search on the graph of the cell decompositions does not require collision checking since the piecewise linear connection between cell centers is restricted to collision-free cells. For the proposed method, given the B-spline parameterization of degree $k$ and cell size of the decomposed environment, the B-spline may deviate from the piecewise linear connection due to the fact that it does not exactly pass through the control points. However, the maximum distance that the B-spline curve deviates from the piecewise linear collection can be characterized offline, which is compensable by moderate obstacle inflation. The inflation needed is characterized in Appendix -C. In practice, since the degree of the B-spline is fixed and the cell size is not tuned frequently, the inflation can be calculated once and then used for many experiments.

<!-- chunk {"id": "body-0065", "role": "body", "section": "V-D Feasibility Condition", "weight": 1.0} -->

(a) Mapping from the traces on 𝒢 to 𝒢H Figure 7: Illustration of the mapping process to 𝒢H and the graph aggregation process used by the EBK search.

<!-- chunk {"id": "body-0066", "role": "body", "section": "V-E Efficient Low Dispersion Search", "weight": 1.0} -->

Before proposing the efficient methods, we present a complexity analysis of the OBK search. According to the definition of the k-degree vertex tuple, the total number of vertices $V_{H}$ of the graph $\mathcal{G}_{H}$ grows exponentially w.r.t. the degree $k$ of B-spline parameterization, i.e., ${|V_{H}|} = {O{({|V|}^{k + 1})}}$. Note that according to Prop. 2, Algo. 1 shares a similar complexity with the execution of Dijkstra's algorithm on the graph $\mathcal{G}_{H}$ if the heuristic is set to zero. According to the known result that each vertex is expanded at most once for Dijkstra's algorithm (see ), the maximum number of iterations of Algo. 1 is upper bounded by ${|V_{H}|} = {O{({|V|}^{k + 1})}}$, which characterizes the worst-case execution time of the OBK search.

<!-- chunk {"id": "body-0067", "role": "body", "section": "V-E Efficient Low Dispersion Search", "weight": 1.0} -->

Actually, since $|V_{H}|$ and $|E_{H}|$ grow exponentially with $k$, the worst-case execution time of any algorithm that optimally solves Problem 1 scales exponentially with $k$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "V-E Efficient Low Dispersion Search", "weight": 1.0} -->

Given the observation that the state in the OBK search is homogeneous (i.e., all the dimensions are control point coordinates), we can aggregate the nodes of $\mathcal{G}_{H}$ based on the proximity of the coordinates to gain efficiency. Specifically, according to Algo. 2, each vertex $\hat{v} \in V_{H}$ is marked with a unique integer index. In the modified Index$( \cdot )$ function in Algo. 3, we encode the vertex $\hat{v}$ only based on the coordinates for the last $d$ vertices such that the vertices which share the same partial coordinates will be regarded as the same node. By aggregating the nodes of $\mathcal{G}_{H}$, the dimension of the search space is directly controlled by the user-specified parameter $d$. The modification essentially conducts a low dispersion search on the high-dimensional graph $\mathcal{G}_{H}$ with a control on the number of expanded nodes.

<!-- chunk {"id": "body-0069", "role": "body", "section": "V-E Efficient Low Dispersion Search", "weight": 1.0} -->

Different $d$ values will determine how the vertex tuples are aggregated, which in turn affects the solution quality and algorithm efficiency. Note that although the search space is reduced, the continuity and smoothness of the resultant trajectory is maintained since the modification preserves the sharing of the B-spline coordinates. The resultant search method is called EBK search and a formal analysis of the EBK search is provided in Sect. V-F.

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-E Efficient Low Dispersion Search", "weight": 1.0} -->

Algorithm 3 Given a k-degree vertex tuple v̂ ∈ VH, assign an integer index based on the selected coordinates of the tuple.

<!-- chunk {"id": "body-0071", "role": "body", "section": "V-F Analysis of the EBK Search", "weight": 1.0} -->

As introduced in Sect. V-E, the user-specified parameter $d$ determines how vertex tuples in the graph $\mathcal{G}_{H}$ are aggregated. We provide a toy example of $d = 1$ in Fig. 7(b) to understand the graph aggregation. When choosing $d = 1$, as in Fig. 7(b), vertex tuples are aggregated based on the last vertex of the tuple. For instance, ${\hat{v}}_{4}$ and ${\hat{v}}_{5}$ share the same last vertex and are aggregated into the same node, as marked in purple. In the same way, the three distinct nodes ${\hat{v}}_{6}$, ${\hat{v}}_{7}$ and ${\hat{v}}_{8}$ are aggregated into the same cyan node.

<!-- chunk {"id": "body-0072", "role": "body", "section": "V-F Analysis of the EBK Search", "weight": 1.0} -->

The edges of $\mathcal{G}_{H}$ are also reduced accordingly. For example, the edges $({\hat{v}}_{4},{\hat{v}}_{7})$ and $({\hat{v}}_{5},{\hat{v}}_{8})$ are aggregated since they are connecting the same two aggregated nodes. Note that once a path to the aggregated node is determined, such as the path blue-yellow-purple-cyan, the vertex tuple associated with each aggregated node is determined. In this example, the purple node is associated with ${\hat{v}}_{5}$ and the cyan node is associated with ${\hat{v}}_{8}$. Therefore, given the initial vertex tuple, any path on the aggregated graph, can be uniquely transformed to a path on the graph $\mathcal{G}_{H}$. And, apparently, a path on the graph $\mathcal{G}_{H}$ can be transformed to a path of aggregated nodes.

<!-- chunk {"id": "body-0073", "role": "body", "section": "V-F Analysis of the EBK Search", "weight": 1.0} -->

The equivalence states that we are actually conducting a graph search on the aggregated graph with a controllable number of vertices, i.e., a low-dispersion search on the original high dimensional graph $\mathcal{G}_{H}$. The resultant path on the aggregated graph can be reconstructed as an admissible path on $\mathcal{G}_{H}$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "V-F Analysis of the EBK Search", "weight": 1.0} -->

For the simple case of $d = 1$, as illustrated in Fig. 7(b), the size of the aggregated graph is the same as the original graph $\mathcal{G}$. Therefore, the EBK search can be as efficient as a shortest path search on the spatial grid by choosing a small $d$. And the advantage of the EBK search is that it directly outputs a time-parameterized dynamically feasible trajectory. It turns out that the EBK search is resolution complete with respect to the aggregated graph, and we refer interested readers to a detailed analysis of the EBK search in Appendix -D.

<!-- chunk {"id": "body-0075", "role": "body", "section": "V-F Analysis of the EBK Search", "weight": 1.0} -->

By choosing a small $d < {k + 1}$, a large number of vertex tuples are aggregated into one group, and the "resolution" of the graph becomes large. Due to the aggregation, the representation of the trajectory is limited. An intuitive example is that, when choosing $d = 1$, the search process will never choose to place the same control point in the same grid cell due to the strictly positive cost. As a result, the trajectory obtained may fail to reach the exact end state, such as a static state. However, the issue can be addressed by choosing a larger $d$ and sacrificing efficiency.

<!-- chunk {"id": "body-0076", "role": "body", "section": "V-F Analysis of the EBK Search", "weight": 1.0} -->

Compared to the preliminary version, i.e., the RBK search, the EBK search is more flexible and allows for control of the algorithm efficiency and solution quality. The connection is that the RBK search is essentially the EBK search using $d = 1$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Elastic Optimization", "weight": 1.0} -->

To compensate for the discretization introduced by the EBK search and further improve the trajectory quality, we present the EO approach, which refines the control point placement to the optimal location w.r.t. the free space. Our approach is motivated by the seminal work, in which a collision-free "tube" around the initial path is identified and the path is "stretched" within the tube so that the shape is optimized. Mathematically, the tube is defined as a series of balls, with the ball centers denoted as $\mathcal{P} ≔ \left\{ \mathbf{p}_{0},\mathbf{p}_{1},\ldots,\mathbf{p}_{T} \right\}$ and corresponding radiuses denoted as $\mathcal{R} ≔ \left\{ r_{0},r_{1},\ldots,r_{T} \right\}$, where $\mathbf{p}_{i}$ denotes the ball center and $r_{i}$ denotes the radius.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Elastic Optimization", "weight": 1.0} -->

The tube is defined to be "well-connected" if and only if ${{\parallel{\mathbf{p}_{i} - \mathbf{p}_{i + i}}\parallel}_{2} \leq {r_{i} + r_{i + 1}}},{{\forall i} \in {\{ 0,\ldots,{T - 1}\}}}$. Compared to which cannot handle dynamical feasibility constraints for complex kinodynamic systems such as quadrotors, we propose a convex optimization formulation based on B-spline parameterization, which uses the convex hull property to enforce feasibility.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Elastic Optimization", "weight": 1.0} -->

Note that Zhu et al. also propose a convex elastic smoothing formulation for car-like robots. There are two major differences: 1) The formulation in is based on the dynamics of car-like robots and cannot be applied to complex dynamic systems, while our formulation uses high-order B-spline parameterization, which can be directly used to control quadrotors. 2) In, the smoothed trajectory may collide with obstacles due to the geometric incompleteness of the tube constraint (as shown in Fig. 9(a)) and only a heuristic waypoint insertion/obstacle inflation scheme is provided, while the EO approach has a theoretical safety guarantee, which is achieved by a two-level inflation scheme to ensure the connectivity of the tube and a finite iterative control point insertion process.

<!-- chunk {"id": "body-0080", "role": "body", "section": "VI-A Elastic Tube Expansion", "weight": 1.0} -->

In and, the elastic tube is a series of connected balls which are centered at the waypoints of the reference path. Intuitively, the tube generated in this way cannot fully utilize the free space around it, as shown in Fig. 8(a). We therefore propose a lightweight tube expansion algorithm so that the tube can roughly represent the locally largest free space. Given the initial control point placement $\pi = {(v_{0},\ldots,v_{T})}$ provided by Algo. 1, we first extract the coordinates of $\pi$, and denote the collection of coordinates as $\mathcal{P} ≔ \left\{ \mathbf{p}_{0},\mathbf{p}_{1},\ldots,\mathbf{p}_{T} \right\}$ following the notation used in Sect. IV.

<!-- chunk {"id": "body-0081", "role": "body", "section": "VI-A Elastic Tube Expansion", "weight": 1.0} -->

1:function TubeExpansion(𝒫, 𝒞ELAS) 2: Initializes: dinflmin, dinflmax, dthres.ℛ = ℛ′ = 𝒬 = ⌀; 5: $\overset{\rightarrow}{n} = {{{({\mathbf{p}_{i} - \mathbf{n}_{i}})}/\text{norm}}{({\mathbf{p}_{i} - \mathbf{n}_{i}})}}$; 6: while dinflmax − dinflmin > dinfltol do 7: d ← (dinflmax + dinflmin)/2, $\mathbf{p}_{i,\text{infl}}\leftarrow{\mathbf{p}_{i} + {d \cdot \overset{\rightarrow}{n}}}$; 8: (ni′, ri′) ← NNSearch (pi, infl, 𝒞ELAS); 9: if Abs (ri′ − d − ri) > dthres then Algorithm 4 Expand elastic tube in configuration

<!-- chunk {"id": "body-0082", "role": "body", "section": "VI-A Elastic Tube Expansion", "weight": 1.0} -->

The elastic tube expansion algorithm (Algo. 4) can be divided into two steps: First, we construct the initial tube, by conducting a radius search for the initial placement $\mathcal{P}$, and obtain the nearest obstacle position $\mathbf{n}_{i}$. Second, we push the center of the bubbles in the direction $\overset{\rightarrow}{n}$ (away from the nearest obstacle) while satisfying the criterion that the new bubble contains the original bubble, as required by condition Abs${({r_{i}' - d - r_{i}})} \leq d_{\text{thres}}$, as shown in Fig. 8(a). The inflation process is implemented in a binary search manner. Algo. 4 will finally find a series of local maximum volume bubble centers $\mathcal{Q} ≔ \left\{ \mathbf{q}_{0},\mathbf{q}_{1},\ldots,\mathbf{q}_{T} \right\}$ based on the initial tube $\mathcal{P}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "VI-A Elastic Tube Expansion", "weight": 1.0} -->

For the parameter settings, $d_{\text{infl}}^{\max}$ and $d_{\text{infl}}^{\min}$ are the maximum and minimum inflation distance, respectively; $d_{\text{thres}}$ is the threshold for checking whether the new bubble contains the original one, and should be set to a small value, e.g., less than the map resolution; and $d_{\text{infl}}^{\text{tol}}$ is the binary search end condition, which can be set to the resolution of the map. The function NNSearch is the nearest neighborhood search, which can be done efficiently if a KD-tree is maintained. The efficiency of Algo. 4 is verified in Section. VIII.

<!-- chunk {"id": "body-0084", "role": "body", "section": "VI-B Elastic Optimization Formulation", "weight": 1.0} -->

Given the inflated ball centers $\mathcal{Q} = \left\{ \mathbf{q}_{0},\mathbf{q}_{1},\ldots,\mathbf{q}_{T} \right\}$ and corresponding radiuses $\mathcal{R}' = \left\{ r_{0}',r_{1}',{\ldotsr_{T}'} \right\}$, the EO formulation minimizes the total control effort by finding the optimal placement $\mathcal{P}^{\ast} = \left\{ \mathbf{p}_{0}^{\ast},\mathbf{p}_{1}^{\ast},\ldots,\mathbf{p}_{T}^{\ast} \right\}$ while satisfying the safety and dynamical feasibility constraints. The safety constraints are enforced by constraining the control point position inside the 3-D balls, and in Sect. VI-C, we will discuss how to theoretically guarantee the safety of the resultant trajectory.

<!-- chunk {"id": "body-0085", "role": "body", "section": "VI-B Elastic Optimization Formulation", "weight": 1.0} -->

The dynamical feasibility constraints are enforced using Prop. 1.

<!-- chunk {"id": "body-0086", "role": "body", "section": "VI-C Enforcing Safety Guarantee", "weight": 1.0} -->

Restricting control points inside the balls is not a sufficient condition for safety, for the following two reasons: 1) the balls are placed with a finite density and constraining the control points in the balls cannot preserve the collision-free characteristic even for straight-line segments between control points (Fig. 9(a)), and 2) the B-spline does not exactly pass the control points and deviates from the straight-line segments. The first issue is also observed, which proposes using waypoint insertion/obstacle inflation to handle the problem. However, there is no quantification of how much inflation or how many insertions are needed and only a heuristic is given. The second issue is inherently similar to one common issue faced by piecewise polynomial parameterization: the polynomial may deviate from the collision-free straight-line segments between waypoints or exceed the safe flight corridor. Chen et al. propose a finite iterative process by adding constraints on polynomial extremas based on a cube corridor (linear constraints), but this is not directly applicable to B-spline parameterization with quadratic constraints.

<!-- chunk {"id": "body-0087", "role": "body", "section": "VI-C Enforcing Safety Guarantee", "weight": 1.0} -->

In our case, the issues can be resolved using a two-level inflation scheme and an iterative convex hull shrinking process. The two-level inflation scheme is to ensure the connectivity of the elastic tube, and furthermore, the inflation needed is quantified in the scheme. For simplicity, we first consider the original tube before applying the tube expansion algorithm (Algo. 4). The two-level obstacle inflation scheme is as follows: the configuration space in which we conduct kinodynamic search with larger obstacle inflation $\delta^{\text{BK}}$ is $\mathcal{C}^{\text{BK}}$, while we generate the elastic tube and optimize the control points in the configuration space $\mathcal{C}^{\text{ELAS}}$ with smaller obstacle inflation $\delta^{\text{ELAS}}$, as shown in Fig. 9(b). The difference adds additional clearance to any point in the configuration space $\mathcal{C}^{\text{BK}}$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "VI-C Enforcing Safety Guarantee", "weight": 1.0} -->

Without the difference, the minimum radius of the ball at the grid center is $\min{(c_{x},c_{y},c_{z})}$, where $c_{x}$, $c_{y}$ and $c_{z}$ are the grid size. Denote the maximum separation distance of two neighboring control points in the 3-D grid as $h_{\max}$. It follows that, if the difference ${\delta^{\text{BK}} - \delta^{\text{ELAS}}} > {{h_{\text{max}}/2} - {\min{(c_{x},c_{y},c_{z})}}}$ holds, the additional clearance will ensure that the two neighboring balls overlap, thus ensuring the connectivity of the elastic tube. Note that Algo. 4 maintains the connectivity of the tube by ensuring that the inflated ball contains the original ball while keeping the same support point on the obstacle.

<!-- chunk {"id": "body-0089", "role": "body", "section": "VI-C Enforcing Safety Guarantee", "weight": 1.0} -->

For the low-level inflation, given $h_{\max}$, $\delta^{\text{ELAS}} \geq {\frac{\sqrt{2} - 1}{2}h_{\max}}$ is sufficient for the straight-line segments to be contained in the free space.

<!-- chunk {"id": "body-0090", "role": "body", "section": "VI-C Enforcing Safety Guarantee", "weight": 1.0} -->

Based on the two-level inflation scheme, we propose an iterative convex hull shrinking process, which pulls the B-spline trajectory back to the free space in the case of collision. The idea of the process is to iteratively add control points to the original B-spline control point sequence. The newly added control points are constrained in the intersection of two consecutive balls. ^44^4According to the introduction in Sect. IV, the total number of knots should satisfy ${m + 1} = {{({n + 1})} + k + 1}$. Since uniform B-spline is used, when a new control point is inserted, the number of knots is increased by one, while the knot separation $\Delta_{t}$ remains the same. The new control point sequence still matches the new knot vector. The process is built upon the convex hull property of the B-spline and constrains the B-spline trajectory by shrinking the convex hull. We highlight that only a finite number of control points are needed to enforce the safety of the B-spline trajectory.

<!-- chunk {"id": "body-0091", "role": "body", "section": "VI-C Enforcing Safety Guarantee", "weight": 1.0} -->

This could save a significant amount of computation power compared to the methods which apply dense constraint points based on a conservative heuristic. We conclude this feature in Theorem 1.

<!-- chunk {"id": "body-0092", "role": "body", "section": "VII-A Receding Horizon Replanner Using Local Control", "weight": 1.0} -->

As shown in Fig. 4, B-spline has the local control property which facilitates the receding horizon (re)planning. Specifically, all the control points are organized in a sliding window. The control points corresponding to the executed and executing trajectory are committed and fixed. The disturbance caused by the optimization will not affect the feasibility of the executing trajectory due to the local control. A stopping policy will be activated if no feasible solution is found before the end of the executing trajectory.

<!-- chunk {"id": "body-0093", "role": "body", "section": "VII-A Receding Horizon Replanner Using Local Control", "weight": 1.0} -->

When replanning is activated, the EBK search is called to update the placement for the control points under optimization. Note that the initial and goal state of the EBK search can be determined by the control points inside the window according to the local planning range. Note that the control points from the sliding window are in the continuous space after reshaping. However, the EBK search should use the discretized control points as the reference initial/ goal state to preserve optimality. The strategy of getting the reference states for the EBK search are to find the closest span pattern in terms of position and velocity error while matching the last control point to the grid cell. We constantly gather a fixed number of control points (e.g., twelve) for EO as the window moves forward.

<!-- chunk {"id": "body-0094", "role": "body", "section": "VII-A Receding Horizon Replanner Using Local Control", "weight": 1.0} -->

There are two modes for the activation of replanning, namely, active mode and passive mode. For the passive mode, the EBK search is only called when collision is detected, while for the active mode, the EBK search is constantly activated as the sliding window moves forwards. Since the active mode can constantly improve the trajectory quality, it is more robust when the mapping quality is limited, but it is more computationally expensive.

<!-- chunk {"id": "body-0095", "role": "body", "section": "VII-B Monocular Vision-Based Testbed", "weight": 1.0} -->

The monocular quadrotor testbed is equipped with a monocular camera (30 Hz), one IMU (100 Hz), an Intel i7 processor and an NVIDIA Jetson TX1 (Fig. 2(a)). The localization, mapping and planning modules are all running onboard. The localization module is based on our Monocular Visual Inertial Navigation System (VINS-Mono), and the mapping module is based on our monocular dense mapping method and truncated signed distance field (TSDF) fusion. No prior knowledge of the environment is required.

<!-- chunk {"id": "body-0096", "role": "body", "section": "VII-C Dual-Fisheye Vision-Based Testbed", "weight": 1.0} -->

The dual-fisheye quadrotor testbed is equipped with two fisheye cameras (30 Hz), one IMU (100 Hz), an Intel i7 processor and an NVIDIA Jetson TX2 (Fig. 2(b)). All modules are running onboard. It is worth noting that by using the two fisheye cameras, the system can provide omnidirectional perception and the quadrotor is able to fly a round-trip with a fixed yaw angle. The mapping module is based on our dual-fisheye omnidirectional stereo system. Also no prior knowledge of the environment is required.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Analysis", "weight": 1.0} -->

In this section, we present an analysis of the proposed kinodynamic planning framework. We begin with two individual analyses for the EBK search and the EO approach, respectively. To analyze the EBK search, we compare the proposed method with two kinodynamic planning algorithms, namely, search-based motion primitive (SMP) and kinodynamic RRT\* (kRRT\*), representing both the search-based method and sampling-based method, respectively. For the EO, we compare the EO approach with two state-of-the-art trajectory optimization techniques, namely, continuous trajectory (CT) optimization and gradient-based safe (GS) trajectory optimization, which are popular non-linear optimization techniques for trajectory refinement. After the individual tests, we analyze the run-time efficiency of the proposed replanning framework, and compare the whole replanning system with the SMP method. We run all the simulations on a desktop computer equipped with an Intel I7-8700K CPU.

<!-- chunk {"id": "body-0098", "role": "body", "section": "VIII-A Analysis of the B-spline-Based Kinodynamic Search", "weight": 1.0} -->

Recall that the motivation for introducing kinodynamic search to replanning is to facilitate dealing with the non-static initial states of the quadrotors. To this end, we analyze the performance of the kinodynamic search by planning from a given non-static initial state to varying goal states in a $10 \times 10 \times 2$ m test field. We compare our results with SMP and kinodynamic RRT\* in terms of the trajectory quality and time efficiency, under the same planning setup. At the same time, we also illustrate the results of a hierarchical geometric planner as a common baseline. Specifically, the geometric planner first uses A\* under the Euclidean distance measure to find the shortest path, and then parameterizes the path using the unconstrained QP formulation introduced.

<!-- chunk {"id": "body-0099", "role": "body", "section": "VIII-A Analysis of the B-spline-Based Kinodynamic Search", "weight": 1.0} -->

The kinodynamic planners, and our method all have a tuning parameter to control the algorithm complexity and solution quality. For instance, SMP can control the discretization resolution for the control input. To further investigate the optimality-efficiency tradeoff achieved by each algorithm, we also demonstrate the results for these algorithms under different parameter setups. Note that we focus on the real-time replanning scenario, so we are concerned with the operation region where the run-time efficiency is close to real-time. Specifically, we compare the following methods: $\text{Geometric}^{\dagger}$: A path finder using A\* and a fifth-degree polynomial parameterization using the unconstrained QP formulation by minimizing the average integral of acceleration. $\text{kRRT*-T100}^{\dagger}$: The kinodynamic RRT\* planner using a 3-D acceleration-controlled double integrator system under a 100 ms termination condition for the sampling. kRRT\*-T600: The kinodynamic RRT\* planner under a 600 ms termination condition.

<!-- chunk {"id": "body-0100", "role": "body", "section": "VIII-A Analysis of the B-spline-Based Kinodynamic Search", "weight": 1.0} -->

$\text{SMP-U3}^{\dagger}$: The SMP planner using a 3-D acceleration-controlled double integrator system with three discrete control inputs for each axis.

<!-- chunk {"id": "body-0101", "role": "body", "section": "VIII-A Analysis of the B-spline-Based Kinodynamic Search", "weight": 1.0} -->

SMP-U5: The SMP planner with five discrete control inputs for each axis. $\text{EBK-D1}^{\dagger}$: Our EBK planner using fifth-degree B-spline parameterization and $d = 1$.

<!-- chunk {"id": "body-0102", "role": "body", "section": "VIII-A Analysis of the B-spline-Based Kinodynamic Search", "weight": 1.0} -->

EBK-D2: The EBK planner using $d = 2$.

<!-- chunk {"id": "body-0103", "role": "body", "section": "VIII-A Analysis of the B-spline-Based Kinodynamic Search", "weight": 1.0} -->

The reason for using the acceleration-controlled double integrator system for kinodynamic RRT\* and SMP is that if a higher-order system were used, the run-time would be too large, making it inapplicable to replanning. For a similar reason, a termination time larger than $600$ ms for kRRT\* and number of control inputs larger than five for SMP are not considered. The methods marked with $\dagger$ are amenable to real-time, and the other methods serve as showcases illustrating how the trajectory quality can be improved given a larger computation time budget.

<!-- chunk {"id": "body-0104", "role": "body", "section": "VIII-A Analysis of the B-spline-Based Kinodynamic Search", "weight": 1.0} -->

All the kinodynamic planners have a similar form of the cost function according to Eq. 4. Since both kRRT\* and SMP adopt the acceleration-controlled double integrator system, the order of the derivative $l$ we can take is $2$ for all the experiments. The weight $\lambda$ of the trajectory time is set to $20$. We consider two additional metrics, namely, average acceleration and maximum acceleration, which represent the smoothness and feasibility of the resultant trajectory.

<!-- chunk {"id": "body-0105", "role": "body", "section": "VIII-A Analysis of the B-spline-Based Kinodynamic Search", "weight": 1.0} -->

For the methods where cell decomposition is needed, such as A\* for the geometric method and EBK, the environment is decomposed into cells with a fixed size of 0.2 $m$ for each dimension. The geometric planner requires a time allocation module since the path does not contain any time information. Generating the optimal time profile for a path is actually not a trivial problem, and the common practice is based on a heuristic allocation method, such as a trapezoid velocity profile. We follow this practice and set the average speed to achieve a similar trajectory duration to the kinodynamic planners. Time allocation is not needed for kinodynamic planners since they directly produce time-profiled trajectories. The initial state is set to a fixed position with non-zero velocity 1.2 $m/s$ and zero acceleration, as shown in Fig. 10. The goal state is static, and its position is regularly sampled with a distance separation of $0.7$ m. In total, there are $136$ collision-free goals available. The velocity and acceleration limit are set to 2 $m/s$ and 4.7 $m/s^{2}$ for each axis.

<!-- chunk {"id": "body-0106", "role": "body", "section": "VIII-A Analysis of the B-spline-Based Kinodynamic Search", "weight": 1.0} -->

The $\Delta_{t}$ for the EBK method is set to $0.17$ s. The statistics averaged over the $136$ rounds of planning are shown in Tab. II, and the qualitative results for the planning to the same goal state are shown in Fig. 10.

<!-- chunk {"id": "body-0107", "role": "body", "section": "VIII-A Analysis of the B-spline-Based Kinodynamic Search", "weight": 1.0} -->

According to the qualitative results in Fig. 10, there is a significant difference in the performance. For the geometric method (Fig. 10(a)), since the shortest path diverges from the initial velocity direction, the parameterization is jerky at the beginning. Moreover, as the unconstrained QP cannot enforce the dynamical feasibility, the generated trajectory is infeasible due to the non-static initial state. As for the kRRT\* with a $100$ ms time budget (Fig. 10(b)), it can respect the initial state of the quadrotor since the control effort is directly considered in the sampling process. It also guarantees the dynamical feasibility of the resultant trajectory by constraining the control input and states along the tree edges. However, the trajectory quality is unsatisfactory due to the limited sampling. We also observe some unpredictable randomized behavior as shown by the three rounds of planning with exactly the same initial state and goal state in Fig. 10(b).

<!-- chunk {"id": "body-0108", "role": "body", "section": "VIII-A Analysis of the B-spline-Based Kinodynamic Search", "weight": 1.0} -->

Meanwhile, for the SMP method, the shape of the trajectory of SMP-U3 is not natural since the resolution of the control input is large.^55^5The acceleration bound we use is larger than that. Some maneuvers such as flying over the little step in the middle are not included in the solution space of SMP-U3. SMP-U5 performs better than SMP-U3 due to finer discretization. Finally, EBK-D1 and EBK-D2 both generate an initial-state-aware smooth trajectory. EBK-D2 finds a slightly better trajectory than EBK-D1 according to the acceleration profile.

<!-- chunk {"id": "body-0109", "role": "body", "section": "VIII-A Analysis of the B-spline-Based Kinodynamic Search", "weight": 1.0} -->

It is notable that the trajectory provided by the EBK method has continuity up to snap, which is good for controlling quadrotors. We can observe from Fig. 10 that the kRRT\* trajectory only has continuity up to acceleration and that of the SMP has continuity up to velocity, due to the restriction of computation complexity and order of the system model.

<!-- chunk {"id": "body-0110", "role": "body", "section": "VIII-A Analysis of the B-spline-Based Kinodynamic Search", "weight": 1.0} -->

From the quantitative results in Tab. II, among the real-time methods (with $\dagger$), EBK-D1 finds the lowest cost trajectory, achieving a $15.2$ $m^{2}/s^{3}$ total cost within $0.034$ s. Our method shows superior performance given the real-time requirement. It is of interest to examine the situation where we have a time budget in the range of seconds. In that case, SMP-U5 achieves a lower cost than EBK-D1 and EBK-D2. The reason is that the trajectory duration of EBK-D2 cannot be efficiently reduced since the control points have to be expanded step by step on the discrete grid. This illustrates the limitation induced by the discretization for the EBK method. However, the difference between the SMP method and EBK method is minor, meaning the EBK method can provide competitive solutions given a run-time budget of seconds.

<!-- chunk {"id": "body-0111", "role": "body", "section": "VIII-B Analysis of the Elastic Optimization", "weight": 1.0} -->

To evaluate the performance of EO, we compare our method with two state-of-the-art trajectory optimization methods: the CT method and GS method. Two test environments are provided, namely, a random map (shown in Fig. 11(c)) and a Perlin noise map^66^6 (shown in Fig. 11(d)). The map size is fixed to ${{{{20m} \times 20}m} \times 4}m$ for both maps. The start location is fixed to the center of the test field for the qualitative experiments in Fig. 11(a) and Fig. 11(b), and is fixed to the left bottom corner for all the experiments in Tab. III to test the performance for long trajectories. The goal location is regularly sampled in the test field with a distance separation of $1$ m. We vary the obstacle density of the random map from 0.1 pillars/$m^{2}$ to 0.4 pillars/$m^{2}$, where the pillar size is set to ${{0.5m} \times 0.5}m$.

<!-- chunk {"id": "body-0112", "role": "body", "section": "VIII-B Analysis of the Elastic Optimization", "weight": 1.0} -->

The qualitative results are provided in Fig. 11 and the quantitative statistics of the optimization performance are organized in Tab. III. Note that we omit the statistics for the Perlin noise map in Tab. III since the trend is similar to that of the random map. All the optimization methods can handle high-order parameterization and they are set to minimizing the integral of the squared jerk. According to Eq. 4, the jerk cost listed in Tab. III has unit $m^{2}/s^{5}$ and represents the accumulated integral of the squared change rate of the acceleration, which represents the total control efforts.

<!-- chunk {"id": "body-0113", "role": "body", "section": "VIII-B Analysis of the Elastic Optimization", "weight": 1.0} -->

The CT method uses a gradient-based non-linear optimization process to optimize the polynomial coefficients such that the resultant trajectory is collision free. It requires a Euclidean signed distance field (ESDF) to evaluate the collision cost. Following the practice, we provide an initial polynomial trajectory as an initial guess, which is parameterized by a straight-line guiding path. The number of segments is determined by a $3$ m distance separation. The GS method shares a similar formulation to the CT method, with the difference being that the GS method starts from a collision-free initial guess, which is provided by A\* search in the experiment. Both the CT method and GS method require time allocation, and in the experiment, we use the trapezoid velocity profile and scale the total allocated time such that different optimization methods achieve a similar average velocity, as shown in Tab. III. The CT method has a larger average velocity due to the cases where it fails to resolve collision and the trajectory does not contain necessary deceleration. The success fraction is calculated by counting the collision-free and dynamically feasible trajectories among the total number of rounds.

<!-- chunk {"id": "body-0114", "role": "body", "section": "VIII-B Analysis of the Elastic Optimization", "weight": 1.0} -->

Firstly, we examine the optimization reliability, i.e., the success fraction for the different methods. As shown in Tab. III, the CT method is sensitive to the obstacle density. For a density of $0.1$ pillars/$m^{2}$, the success fraction of the CT method is 95$\%$, which means that in obstacle-sparse environments, the CT method can resolve collision efficiently. However, when the density increases to $0.4$ pillars/$m^{2}$, we observe that the success fraction drops significantly to $46\%$. The reason is that the CT method easily gets stuck in the infeasible local minimum when the trajectory is inside the cluttered obstacle. As shown in Fig. 11(c), the trajectory of the CT method gets stuck between two pillars where there is not enough clearance considering the quadrotor size. On the other hand, we do not observe a drop in the success fraction for either the GS method or EO method. The reason is that the GS method starts from a collision-free initial guess and has a dominant collision penalty compared to its smoothness cost.

<!-- chunk {"id": "body-0115", "role": "body", "section": "VIII-B Analysis of the Elastic Optimization", "weight": 1.0} -->

The EO method has a high success fraction according to its theoretical guarantee.

<!-- chunk {"id": "body-0116", "role": "body", "section": "VIII-B Analysis of the Elastic Optimization", "weight": 1.0} -->

(a) Random map (0.2 pillars/m2) (b) Perlin noise map (c) Random map (0.2 pillars/m2) (d) Perlin noise map Figure 11: Comparisons of different trajectory optimization methods on two different maps. The EO method is shown in purple, the CT method is shown in red and the GS method is shown in blue.

<!-- chunk {"id": "body-0117", "role": "body", "section": "VIII-B Analysis of the Elastic Optimization", "weight": 1.0} -->

Secondly, we focus on the two reliable methods, namely, the GS method and EO method, and further investigate the trajectory statistics. As shown in Tab. III, the average trajectory durations of the two methods are close, so the comparison of the jerk cost is fair. For an obstacle density of $0.2$ pillars/$m^{2}$, averaged over the $135$ rounds, the jerk cost of the EO method is $181.2$ $m^{2}/s^{5}$, which is smaller than that of the GS method. Similar results are also observed for different densities. The reason is that the GS method is sensitive to the time allocation, since it also starts with an unparamterized path. However, for unknown environments, the shape of the initial path may vary and there is no systematic way to allocate the time. The heuristic trapezoid velocity profile may fail to provide a good initial guess when the initial path is not in a regular shape. For the EO method, since it starts from a time-parameterized B-spline trajectory, there is no need for time allocation.

<!-- chunk {"id": "body-0118", "role": "body", "section": "VIII-B Analysis of the Elastic Optimization", "weight": 1.0} -->

From the efficiency perspective, for the GS method to achieve a similar jerk cost to the EO method, it needs run-times of $0.062$ s, $0.075$ s and $0.206$ s on average for the three densities, which are significantly longer than the EO method. Note that the GS method is based on a non-linear optimization formulation. In the experiments, the non-linear optimization of the GS method is terminated when the non-linear solver (NLOPT ) reports convergence. For the GS method to converge to a compatible solution to that of our EO method, it requires a significantly longer run-time. Moreover, the run-time of the GS method is sensitive to the density, since for cluttered environments, more segments of the polynomial are needed, which may affect the convergence rate of the GS method. However, the EO method has lower run-times for the three different densities. The efficiency of the EO method is affected by the total number of control points, but we observe that the efficiency difference is minor for the different densities.

<!-- chunk {"id": "body-0119", "role": "body", "section": "VIII-C Analysis of the Run-Time Efficiency", "weight": 1.0} -->

In this section, we test our replanning system, combining the EBK search with EO refinement. For the EBK search, we adopt EBK-D1 since it is the most efficient and the trajectory quality is satisfactory as verified in Sect. VIII-A. We provide two different maps, namely, the random map and Perlin noise map. We evaluate the run-time efficiency of our replanning system, and list the statistics of all components in Tab. IV. The overall trajectory illustrating the whole round trip is shown in Fig. 12.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Opt", "weight": 1.0} -->

Random map (0.25 pillars/m2) Avg Max Std Avg Max Std Avg Max Std Avg Max Std TABLE IV: Run-time analysis on different maps As shown in Tab. IV, on the random map, the EBK-D1 method consumes an average computing time of $0.017s$ with a standard deviation of $0.01s$. The elastic tube expansion method can be finished in $0.002s$, and the optimization can be done in $0.021s$. On the Perlin noise map, which contains unstructured 3D obstacles, our method has a similar performance, showing that our method works well in complex 3-D environments.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Opt", "weight": 1.0} -->

(a) Replan on the random map (b) Replan on the Perlin noise map Figure 12: Illustration of our replanning system on different maps.

<!-- chunk {"id": "body-0122", "role": "body", "section": "VIII-D Comparison of the Replanning Framework", "weight": 1.0} -->

In this section, we conduct a system comparison with the SMP method. We use SMP-U3 since SMP-U5 cannot work in real-time. Moreover, we conduct an ablation test, which excludes the initial-state aware EBK search and adopts the naive position-only A\* search combined with EO local reshaping. We call the method for the ablation test A\*-EO. The ablation test validates the critical role of the kinodynamic search in replanning.

<!-- chunk {"id": "body-0123", "role": "body", "section": "VIII-D Comparison of the Replanning Framework", "weight": 1.0} -->

We set up a challenging obstacle-cluttered 3-D complex simulation environment containing walls, 3-D steps (free space below) and pillars, as shown in Fig. 13. The replanning strategy is choosing a local goal state on a given straight-line guiding path with a local replanning range of 5 $m$. The simulated quadrotor is equipped with a depth camera which has a sensing range of $4$ m. The maximum velocity and acceleration bound are set to 2 $m/s$ and 3.2 $m/s^{2}$ for each axis. For SMP-U3, we use a conservative bound with maximum acceleration 1.0 $m/s^{2}$ for each axis since SMP-U3 can only work with a narrow velocity and acceleration range. Using a large dynamic range for SMP-U3 will result in a very sparse primitive graph, which does not even contain one feasible solution. For the EBK search of our method, we use EBK-D1 with a $60 \times 60 \times 20$ uniform grid. For the EO approach, 12 control points are refined as the window moves forward.

<!-- chunk {"id": "body-0124", "role": "body", "section": "VIII-D Comparison of the Replanning Framework", "weight": 1.0} -->

We evaluate the replanning system from the trajectory statistics and time efficiency perspectives, as shown in Tab. V.

<!-- chunk {"id": "body-0125", "role": "body", "section": "VIII-D Comparison of the Replanning Framework", "weight": 1.0} -->

Critical snapshots of the three methods are shown in Fig. 14. For SMP-U3 (Conservative) in Fig. 14(a), when the quadrotor observes the 3-D step, it chooses to circle around instead of directly flying through the space below since the latter action requires a large acceleration range. This phenomenon demonstrates that SMP-U3 (Conservative) sacrifices maneuverability due to the restriction of the dynamic range. SMP-U3 takes the initial state into account, as shown in the middle snapshot in Fig. 14(a). The necessity of using the kinodynamic search instead of the position-only A\* search is identified by the totally different maneuvers in Fig. 14(b) and Fig. 14(c). When the quadrotor enters the region of the pillars, it has two distinct choices, namely, "pass on the left" or "pass on the right". For the A\*-EO method, as shown in the middle snapshot in Fig. 14(b), the quadrotor tends to choose the direction purely based on the shortest path.

<!-- chunk {"id": "body-0126", "role": "body", "section": "VIII-D Comparison of the Replanning Framework", "weight": 1.0} -->

So there are cases where the quadrotor is passing in one direction and suddenly switches to the opposite direction due to finding a new shortest path, which results in an inconsistent and non-smooth replanning trajectory. Compared to A\*-EO, the kinodynamic EBK search provides an initial-state-aware trajectory for the local reshaping, as shown in Fig. 14(c). With the EBK search, the overall trajectory is clearly more natural and the replanning is more consistent.

<!-- chunk {"id": "body-0127", "role": "body", "section": "VIII-D Comparison of the Replanning Framework", "weight": 1.0} -->

As shown in Tab. V, SMP-U3 (Conservative) is efficient and has an average computation time of $0.010$ s. However, since the acceleration bound is conservative, the maneuverability is sacrificed and the trajectory duration is $33.3$ s, longer than the other two methods. Note that we use acceleration-controlled SMP with unconstrained QP reparameterization. Since the unconstrained QP has no dynamical feasibility guarantee, the maximum acceleration is 1.3 $m/s^{2}$, which exceeds its designed maximum acceleration (1 $m/s^{2}$). Compared to SMP-U3 and A\*-EO, our method has the lowest total jerk cost and the improvement is achieved by incorporating the kinodynamic search. The average velocity of our method is 1.37 $m/s$, slightly higher than the A\*-EO, due to the fact that the kinodynamic search can reduce sharp decelerations. The maximum acceleration of our method is 3.18 $m/s^{2}$, which obeys the dynamical feasibility constraint.

<!-- chunk {"id": "body-0128", "role": "body", "section": "VIII-D Comparison of the Replanning Framework", "weight": 1.0} -->

Compared to the position-only A\*-EO method, the jerk cost is reduced by $10\%$ by using the kinodynamic search. Considering that the advantages of the EBK search are outstanding for part of the trajectory where potential inconsistency exists, this quantitative improvement still faithfully identifies the gain of using the kinodynamic search. Note that navigating through this challenging environment with enough agility already requires considerable control efforts, and the $10\%$ cost reduction represents a reasonable overall improvement.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We conduct onboard experiments^77^7 with the two vision-based testbeds to show the general applicability of the proposed framework. For onboard testing, the parameters are as follows: the time step $\Delta_{t}$ is set to $0.35s$; the maximum velocity and maximum acceleration are set to 1.2 $m/s$ and 2.0 $m/s^{2}$, respectively; ^88^8The speed limit and acceleration limit are set to be slightly conservative considering the perception delay in onboard experiments. and the local planning range is set to ${{{{10m} \times 6}m} \times 1.1}m$. (The corresponding grid size is $55 \times 35 \times 6$.)

<!-- chunk {"id": "body-0130", "role": "body", "section": "IX-A1 Monocular-vision-based indoor navigation", "weight": 1.0} -->

As shown in Fig. 15, our replanning system works in complex 3-D environments with only a local map. The quadrotor is commanded to navigate to a 3-D position where the environment is previously unknown. The whole trajectory and the final accumulated map is shown in Fig. 16. The trajectory length of the final trajectory is $18.6m$ and total trajectory execution time is 43.4 $s$. The average velocity of the quadrotor is 0.45 $m/s$ with a maximum velocity of 0.79 $m/s$. The maximum acceleration of the trajectory is 0.58 $m/s^{2}$, the whole trajectory is dynamically feasible, and there are a total $125$ calls of the EBK search (active mode), with an average computation time of 0.010 $s$. There are $105$ calls of EO. The average computation times of the elastic tube expansion and the optimization are 0.001 $s$ and 0.031 $s$, respectively.

<!-- chunk {"id": "body-0131", "role": "body", "section": "IX-A2 Dual-fisheye-based indoor round-trip navigation", "weight": 1.0} -->

As shown in Fig. 17 and Fig. 18, with omnidirectional perception, our quadrotor testbed is able to fly a round-trip without controlling the yaw angle. Online mapping using the dual-fisheye cameras is challenging due to the high distortion of the images acquired from the fisheye cameras. Although the uncertainty of the map is larger than the monocular case, our replanning system is still able to robustly avoid the unexpected obstacles and navigate in the unstructured cluttered environment.

<!-- chunk {"id": "body-0132", "role": "body", "section": "IX-B Outdoor Replanning Performance", "weight": 1.0} -->

As shown in Fig. 19, we demonstrate outdoor experiments using the monocular vision testbed. For Fig. 19(a), the trajectory length is $19.6m$ and total execution time is $41.3s$. The average velocity of the quadrotor is ${0.49m}/s$. The maximum acceleration of the trajectory is ${1.06m}/s^{2}$, and the whole trajectory is dynamically feasible. There are a total $35$ calls of EBK search (passive mode) with an average computation time of $0.025s$. The average computation times of the elastic tube expansion and optimization are $0.001s$ and $0.030s$, respectively. For the experiment shown in Fig. 19(b), the performance and trajectory statistics are similar.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this paper, we present an efficient kinodynamic replanning framework by exploiting the advantageous properties of the B-spline. The proposed EBK search algorithm is flexible and provides a user-specified parameter which can be used to control the algorithm efficiency and solution quality. The problem of the B-spline-based kinodynamic search on a spatial grid is characterized in detail, and the theoretical performance of the EBK search is analyzed. To compensate for the discretization, we propose an elastic optimization process. We combine the two components into a receding horizon framework. Detailed analysis and comprehensive experiments are carried out to validate the performance. Systematic comparisons against the state-of-the-art are provided to verify the claims. The replanning framework is efficient and complete, and can be used in various kinds of exploration tasks and different kinds of quadrotor testbeds. The current limitation of the framework lies in the fact that for EBK search we are using the uniform B-spline on the spatial grid, which will result in limited B-spline patterns.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In the future, we expect to explore NURBS for kinodynamic search, which will allow for various motion patterns in the kinodynamic search.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Characterization of the inflation for the B-spline-based kinodynamic search", "weight": 1.0} -->

We denote by $\mathcal{C}^{\text{BK}}$ the configuration space in which we conduct the B-spline-based kinodynamic search. The configuration space $\mathcal{C}^{\text{BK}}$ is generated by inflating all the obstacles by $\delta^{\text{BK}}$ in the workspace. We take a 26-connected 3-D grid with fixed cell size $d_{\text{x}} \times d_{\text{y}} \times d_{\text{z}}$ and a fifth-degree B-spline as an example. There is a finite number of possible span patterns ($27^{5}$ in total).

<!-- chunk {"id": "body-0136", "role": "body", "section": "Characterization of the inflation for the B-spline-based kinodynamic search", "weight": 1.0} -->

The minimum clearance $c_{\min}^{\text{BK}}$ of the configuration space $\mathcal{C}^{\text{BK}}$ can be expressed by the cell size and obstacle inflation $\delta_{\text{BK}}$ according to $c_{\min}^{\text{BK}} = {\min\left( {{d_{\text{x}}/2} + \delta^{\text{BK}}},{{d_{\text{y}}/2} + \delta^{\text{BK}}},{{d_{\text{z}}/2} + \delta^{\text{BK}}} \right)}$. The problem of finding the sufficient condition such that the overall trajectory is collision free is equivalent to finding the minimum inflation $\delta^{\text{BK}}$ such that the trajectories for all the B-spline patterns are completely bounded inside the inflated cells.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Characterization of the inflation for the B-spline-based kinodynamic search", "weight": 1.0} -->

Since the total number of patterns is finite, $\delta^{\text{BK}}$ can be found by enumerating all the possible span patterns and picking out the one with the largest deviation. The script is available.^99^9The corresponding script can be found at Note that the process of finding the sufficient inflation is one-time work prior to the planning process. Therefore, it does not affect the EBK search efficiency. Typically, for a 26-connected 3-D grid with fixed cell size ${{{{0.16m} \times 0.16}m} \times 0.16}m$, the inflation needed is less than $0.03m$, which is easy to satisfy in practice.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Performance analysis of the EBK search", "weight": 1.0} -->

To analyze the performance of the EBK search, we show than the modified Index function in Algo. 3 induces another search graph. The characterization of the search graph unveils the complexity of the EBK search. In the following, we give a formal definition of the search graph given by the modified Index function.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Performance analysis of the EBK search", "weight": 1.0} -->

We begin with the definition of the nodes which are called virtual nodes. Specifically, given the encoding level $d$ and encoding index $e$, we denote by $\mathcal{H}_{e}^{d} ≔ \left. \{{\hat{v} \in V_{H}} \middle| {{\text{Index}{(\hat{v},d)}} = e}\} \right.$ the virtual node aggregating all the vertex tuples which share the same encoding, i.e., the same last $d$ coordinates. It follows that each vertex tuple $\hat{v} \in V_{H}$ belongs to exactly one virtual node due to the uniqueness induced by the function UniqueEncode$( \cdot )$. For each vertex tuple ${\hat{v}}_{i} \in \mathcal{H}_{e_{i}}^{d}$, we can obtain the set of neighboring virtual nodes $\left.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Performance analysis of the EBK search", "weight": 1.0} -->

We define the cost to the virtual node to be ${c{\lbrack\mathcal{H}_{e}^{d}\rbrack}} = {\min{\{{\left. {c{\lbrack\pi_{s},\hat{v}\rbrack}} \middle| {\forall\hat{v}} \right. \in \mathcal{H}_{e}^{d}}\}}}$, where $c{\lbrack\pi_{s},\hat{v}\rbrack}$ is the minimum cost from the start vertex tuple $\pi_{s}$ to $\hat{v}$ according to Eq. 5. The EBK search cannot reach the exact goal state $\pi_{g}$, and instead it can only reach the virtual node $\mathcal{H}_{e_{g}}^{d}$. In other words, the EBK search can only reach the relaxed goal state.
