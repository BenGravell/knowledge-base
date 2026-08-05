<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness

Topics include Kinodynamic planning, Differential flatness, Steering function, Parallelization, Manipulators, Quadrotors.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Exploits differential flatness to obtain closed-form analytical BVP solutions in a flat output space. Planning is done in the flat space (concatenation of flat outputs and several time derivatives thereof). Kinodynamic constraints and collision checking can be done very efficiently/quickly by using SIMD instructions on CPU. Closely related to the linear-systems approach of Webb & van den Berg (1205.5088) but extended to the broader class of differentially flat systems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Motion planning under dynamics constraints, i.e, kinodynamic planning, enables safe robot operation by generating dynamically feasible trajectories that the robot can accurately track. For high-DOF robots such as manipulators, sampling-based motion planners are commonly used, especially for complex tasks in cluttered environments. However, enforcing constraints on robot dynamics in such planners requires solving either challenging two-point boundary value problems (BVPs) or propagating robot dynamics, both of which cause computational bottlenecks that drastically increase planning times. Meanwhile, recent efforts have shown that sampling-based motion planners can generate plans in microseconds using parallelization, but are limited to geometric paths. This paper develops FLASK, a fast parallelized sampling-based kinodynamic motion planning framework for a broad class of differentially flat robot systems, including manipulators, ground and aerial vehicles, and more. Differential flatness allows us to transform the motion planning problem from the original state space to a flat output space, where an analytical time-parameterized solution of the BVP problem can be obtained.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A trajectory in the flat output space is then converted back to a closed-form dynamically feasible trajectory in the original state space, enabling fast validation via ``single instruction, multiple data" parallelism. Our framework is fast, exact, and compatible with any sampling-based motion planner, while offering theoretical guarantees on probabilistic exhaustibility and asymptotic optimality based on the closed-form BVP solutions. We extensively verify the effectiveness of our approach in both simulated benchmarks and real experiments with cluttered and dynamic environments, requiring mere microseconds to milliseconds of planning time.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning is critical for safe and accurate robot operation in many applications, *e.g.*, transportation \[claussmann2020review\], environment monitoring \[honig2018trajectory, zhou2022swarm\], warehouses \[eppner2016lessons\], healthcare \[riek2017healthcare\], and home assistance \[jenamani2025feast\]. In such applications, the robot has to react quickly to changes in its environment, promptly (re)plan a collision-free trajectory, and safely track the trajectory to reach a goal state, using a controller. This task requires fast motion planning, subject to both collision avoidance and robot dynamics constraints, to generate a dynamically feasible trajectory from a start to a goal that the robot is able to follow.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While recent advances have significantly reduced motion planning times for geometric planning via parallelization techniques \[thomason2024vamp, ramsey2024-capt\], sampling-based motion planning under dynamics constraints, *i.e.*, kinodynamic planning, remains a challenge for real-time applications especially for high degree-of-freedom (d o f) robots such as manipulators. In this paper, we address this problem by leveraging the *differential flatness* property of many common robot systems, such as ground and aerial vehicles, manipulators, and more, to enable ultrafast sampling-based kinodynamic motion planning via parallelization techniques.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

(a) Tracking our trajectory (b) Tracking a geometric path Figure 1: Motion planning for a “pick and place” task in a cluttered environment: a dynamically feasible trajectory (a) generated from our FLASK framework can be accurately tracked by a UR5 robot. Meanwhile, tracking a geometric path (b) leads to collisions (shown in red) that topple the nearby boxes. Multiple intermediate states are overlaid to illustrate the robot’s motion. Our planning framework is real-time and generates trajectories in ∼ 90μs by leveraging differential flatness and “single instruction, multiple data” (simd) parallelism.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Kinodynamic planning \[lavalle2001randomized, hsu2022randomizekinodynamic, lavalle2006planning\] generates dynamically feasible trajectories by directly enforcing dynamics constraints in the planner. Without such constraints, controllers often struggle to accurately track motion plans, especially with high-speed maneuvers, potentially leading to unsafe behavior. Optimization-based approaches, *e.g.*, \[augugliaro2012generation, schulman2014trajopt, bonalli2019gusto, tassa2012synthesis, Mastalli2020Crocoddyl, ortizharo2025iDbAstar\], formulate kinodynamic planning as a nonlinear optimization problem and solve for the solution by minimizing a trajectory cost subject to constraints such as collision avoidance, robot dynamics, and joint angle and velocity limits. While these approaches can work well in high-dimensional state spaces, they are often susceptible to local minima and are sensitive to initial solutions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Meanwhile, search-based approaches, *e.g.*, \[pivtoraiko2005efficient, pivtoraiko2011kinodynamic, cohen2010search, liu2017search, ajanovic2018searchbased\], build a graph in the state space on a grid or lattice and search for a sequence of motion primitives that connects the start and the goal. Search-based methods provide optimality guarantees but suffer from the curse of dimensionality, thus requiring complex heuristics or domain knowledge to guide the search. On the other hand, sampling-based approaches randomly sample to expand from the start to the goal, constructing a tree \[lavalle2001randomized, webb2013kinodynamicRRT, karaman2010kinorrt, hauser2016aorrt, li2016sst, verginis2023kdf\] or sometimes a graph for simple systems \[vandenberg2007kinoroadmap\].

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key challenge in enforcing dynamics constraints in sampling-based planning is to solve challenging two-point boundary value problems (BVPs) for dynamically feasible *local paths* between robot states. Many planners \[lavalle2001randomized, hsu2022randomizekinodynamic, li2016sst\] avoid this by instead sampling an often sub-optimal control input and then propagating the dynamics forward using numerical integration \[butcher2016numerical\]. Dynamic propagation with randomly sampled control often causes the planner to "wander" to irrelevant parts of the state space and might lead to longer paths and longer planning times. Other works solve the BVP problem for simple systems \[karaman2010kinorrt\] and linearized robot dynamics \[webb2013kinodynamicRRT, Perez2012LQRRRT\], or approximate the solution using a neural network \[wolfslag2018rrt, chiang2019rl, zheng2021sampling\].

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Instead, we obtain an *exact analytical solution* of the BVP, thanks to the *differential flatness* of many robot platforms such as mobile robots and manipulators \[murray1995differential, mellinger2011minimumsnap\].

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Differential flatness \[murray1995differential\] is a powerful system property that, similar to feedback linearization \[khalil2002nonlinear\], simplifies motion planning and control designs by converting the nonlinear robot dynamics to an equivalent linear system. For differentially flat systems, the robot states and control inputs can be described by a set of carefully chosen flat outputs and their derivatives (see Def. 1. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness") for more details). A trajectory in the flat output space can be converted to a dynamically feasible trajectory in the robot's original state space, allowing us to simplify motion planning problems via a change of variables. This technique has been used mainly to plan trajectories for mobile robots, most notably quadrotors \[mellinger2011minimumsnap, mellinger2012_trajgen, liu2017search\].

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, the planning time is still hindered by computationally expensive subroutines such as forward kinematics and collision checking, which are particularly worse with high-d o f robots such as manipulators.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, advances in parallelization \[sundaralingam2023curobo, thomason2024vamp\] have improved planning time to the range of microseconds and milliseconds. However, these works focus on either geometric \[thomason2024vamp\] or kinematic \[sundaralingam2023curobo\] planning problems. One family of these techniques uses "fine-grained" parallelism via "single instruction, multiple data" (simd) instructions, available on consumer CPUs, to perform collision checking on multiple samples at the same time \[thomason2024vamp, ramsey2024-capt\]. However, directly enforcing dynamics constraints in parallel is non-trivial, as it requires sampling a trajectory at different time steps in advance while obeying robot dynamics. We address this problem by transforming the kinodynamic planning problem from the original state space to a flat output space, where closed-form *local paths* are time-parameterized polynomials and hence, amenable to simd parallelization for fast collision checking.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

The resulting flat output trajectory is converted to a dynamically feasible collision-free trajectory in the original state space for the robot to execute. Our approach is fast, exact and general for most sampling-based planners.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, we develop FLASK ^11^1The code will be made publicly available., a "Differential Flatness-based Accelerated Sampling-based Kinodynamic Planning" framework that: generates dynamically feasible trajectories in the range of milliseconds for nonlinear differentially-flat robot systems, such as manipulators, and mobile robots, constructs a planning tree or graph by solving the boundary value problem or dynamics propagation for continuous closed-form trajectories in the flat output space, performs fast collision checking of the closed-form trajectories using fine-grained simd parallelism.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide a theoretical analysis on our approach's probabilistic exhausitivity, a concept stronger than completeness introduced in \[schmerling2015optimal_driftless, kavraki1998analysis\], and optimality guarantees. We extensively verify our approach with challenging motion planning problems on low- and high-d o f, fully- and under-actuated robot systems in both simulated and real experiments. FLASK is shown to achieve planning times of merely a few milliseconds, even on high-d o f robot platforms in cluttered environments, while respecting dynamics constraints by design. Our framework is general and can be integrated in the context of many common sampling-based motion planners, such as RRT-Connect \[kuffner2000rrtconnect\], SST\* \[li2016sst\] and others, effectively turning geometric planners into kinodynamic planners with theoretical guarantees.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Motion Planning with Dynamics Constraints", "weight": 1.0} -->

Kinodynamic motion planning \[schmerling2019kinodynamic\], *i.e.*, motion planning under dynamics constraints, is a challenging task where the robot plans a dynamically feasible trajectory from a start, *e.g.*, a robot state, containing its joint angles and derivatives, to a goal region while satisfying the robot dynamics and avoiding collision with obstacles in the environment. There are three main approaches: optimization-based, search-based, and sampling-based kinodynamic planning.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A Motion Planning with Dynamics Constraints", "weight": 1.0} -->

*Optimization-based kinodynamic planning*, such as TrajOpt \[schulman2014trajopt\], GuSTO \[bonalli2019gusto\], and Crocoddyl \[Mastalli2020Crocoddyl\], generates robot trajectories by formulating and solving an optimization problem, subject to dynamics and collision-avoidance constraints, with an objective function measuring the cost of the trajectory. This optimization problem is often nonlinear and can be solved via sequential convex programming \[augugliaro2012generation, schulman2014trajopt, chen2015decoupled, bonalli2019gusto\], iterative linear quadratic regulators \[tassa2012synthesis\], differential dynamic programming \[Howell2019Altro, Mastalli2020Crocoddyl\], augmented Lagrangian methods \[toussaint2017tutorial\], or general solvers \[l2022whole, beck2025vitro\].

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A Motion Planning with Dynamics Constraints", "weight": 1.0} -->

In general, optimization-based trajectory planners provide smooth trajectories, but often get stuck in a local minimum and require good initialization. While trajectory optimization with a graph of convex sets \[marcucci2023motion, vonwrangel2024gcs, graesdal2024_contactplanning\] can avoid local minima, it requires expensive precomputation of the graph in the state space.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A Motion Planning with Dynamics Constraints", "weight": 1.0} -->

*Search-based kinodynamic planning* \[pivtoraiko2005efficient, pivtoraiko2011kinodynamic, cohen2010search, liu2017search, ajanovic2018searchbased, mishani2025srmp\] instead constructs a graph, often on a predefined grid or lattice, where each edge is chosen from a precomputed, discrete set of motion primitives, generated by propagating the robot dynamics for a short period of time under a set of control inputs. A motion primitive is valid if it does not collide with an obstacle. A search algorithm, such as $A^{*}$ \[hart1968formal\], can be used to find the shortest path on the graph, providing a trajectory as a sequence of motion primitives connecting the start with the goal. A major challenge of search-based approaches is the need to precompute dynamics propagation, where a numerical approximation with fine lattice resolution is required for high accuracy. They also suffer from the curse of dimensionality and require a good heuristic to guide the search.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A Motion Planning with Dynamics Constraints", "weight": 1.0} -->

*Sampling-based kinodynamic planning* \[orthey2024-review-sampling, webb2013kinodynamicRRT, karaman2010kinorrt, lavalle2001randomized, hsu2022randomizekinodynamic, hauser2016aorrt, li2016sst, verginis2023kdf\] uses sampling to discretize the high-dimensional state space and build a tree (or, less often, a graph for simple systems such as car-like robots \[vandenberg2007kinoroadmap\]), growing from the start towards the goal region. To find a feasible trajectory connecting two samples, a difficult *two-point boundary value problem* (BVP) has to be solved \[lavalle2006planning\], posing a major challenge for sampling-based kinodynamic planning.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A Motion Planning with Dynamics Constraints", "weight": 1.0} -->

A common approach to avoid solving a BVP problem for tree expansion is to sample the control input space, and propagate the robot dynamics, *e.g.*, using a numerical integrator \[lavalle2001randomized, hsu2022randomizekinodynamic, li2016sst\] or physics-based models \[gao2025parallel\], for a short period of time, with asymptotic optimality guarantees analyzed in \[li2016sst\]. Other approaches only solve the BVP problem for simple robot dynamics with low-dimensional state space \[karaman2010kinorrt, webb2013kinodynamicRRT\], or linearized dynamics \[webb2013kinodynamicRRT, Perez2012LQRRRT\]. Meanwhile, learning-based kinodynamic motion planning uses neural networks to approximate the control input and the steering cost of expanding the tree towards a new node \[wolfslag2018rrt, chiang2019rl, zheng2021sampling, ichter2019latentspacemp, li2021mpc-mpnet\].

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-A Motion Planning with Dynamics Constraints", "weight": 1.0} -->

BVPs and dynamics propagation cause major computational bottlenecks for kinodynamic planning. While BVPs can be analytically solved for linear or simple systems \[webb2013kinodynamicRRT, Perez2012LQRRRT\], this is not true in general for most nonlinear systems and it is computationally expensive to obtain an approximate solution. Kinodynamic RRT^∗^ \[webb2013kinodynamicRRT, Perez2012LQRRRT\] linearizes the dynamics around an operating point and demonstrates that BVPs can be solved in closed form for certain robots, *e.g.*, quadrotors around a hovering position. However, the approximated solution only works well around the operating point, limiting aggressive maneuvers. To avoid solving difficult BVPs, most existing kinodynamic planners \[li2016sst\] resort to dynamics propagation, where a constant value of the control is sampled instead. A numerical integrator such as Euler's or Runge-Kutta methods \[butcher2016numerical\] is then used to sequentially calculate the next robot state over multiple small time steps to maintain high accuracy.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-A Motion Planning with Dynamics Constraints", "weight": 1.0} -->

Typically, the sampled control is suboptimal, and therefore, causes the planner to wander in the state space before reaching the goal. Existing planners often mitigate this "wandering" effect via best-state selection and tree pruning \[li2016sst\], but still require long planning times to find a dynamically feasible trajectory.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-A Motion Planning with Dynamics Constraints", "weight": 1.0} -->

Optimization-based, search-based and sampling-based approaches can be combined to improve trajectory generation \[ortizharo2024iDbRRT, ortizharo2025iDbAstar, natarajan2024pinsat, natarajan2023torque, natarajan2021interleaving, sakcak2019sampling, shome2021asymptotically, kamat2022bitkomo, choudhury2016regionally, alwala2021joint\]. For example, a path or trajectory from sampling-based or search-based planners can be used as an initial solution for optimization-based ones \[ortizharo2024iDbRRT, ortizharo2025iDbAstar\]. INSAT planners \[natarajan2024pinsat, natarajan2023torque, natarajan2021interleaving\] interleave between search-based planning on a low-dimensional subspace and optimization-based planning on the full-dimensional space to improve planning times and success rates.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-A Motion Planning with Dynamics Constraints", "weight": 1.0} -->

Meanwhile, a library of precomputed motion primitives from search-based planning can be sampled to expand the planning tree in sampling-based motion planning \[sakcak2019sampling, shome2021asymptotically\]. Furthermore, optimized local paths can be used to generate collision-free edges and bias the sampling regions in a sampling-based planner \[kamat2022bitkomo, choudhury2016regionally\]. Another approach is to fit a geometric path with a time-parameterized trajectory using trajectory optimization such as TOPP-RA \[pham2018toppra\] or Ruckig \[berscheid2021ruckig\], typically without considering collision avoidance constraints.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-A Motion Planning with Dynamics Constraints", "weight": 1.0} -->

Our method performs fast sampling-based kinodynamic planning by leveraging simd parallelism (Sec. II-B) and the differential flatness of the dynamics of common robot platforms \[allen2019real, liu2017search, bascetta2017flat, welde2021dynamically\] to directly tackle the BVP problems. A system is called *differentially flat* if there exist variables, called flat outputs, whose values and derivatives dictate the robot state and control inputs (see Def. 1. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness") for details).

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-A Motion Planning with Dynamics Constraints", "weight": 1.0} -->

This approach has been applied to sampling-based \[bascetta2017flat, ye2022efficient, wang2024differential, seemann2014exact\], search-based \[liu2017search\], and optimization-based motion planning \[mellinger2011minimumsnap, welde2021dynamically, han2023efficient, hao2005differential, beaver2024optimal\], but primarily for low-dimensional robot platforms (often with simple geometry shapes such as spheres or boxes for collision checking), *e.g.*, quadrotors \[mellinger2011minimumsnap\], unicycles and 2-link arms \[beaver2024optimal\], or for a specific system, *e.g.*, gantry cranes \[vu2022sampling\]. Instead, we integrate differential flatness with sampling-based kinodynamic planning for generic high-d o f robots, where forward kinematics and collision checking are complex and time-consuming besides enforcing dynamics constraints.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-A Motion Planning with Dynamics Constraints", "weight": 1.0} -->

While most existing methods approximate a solution to the BVP problems, differential flatness allows us to obtain a closed-form fixed- or minimum-time polynomial BVP solution. Such closed-form trajectories are amenable to parallelized collision checking using *fine-grained* parallelization based on simd instructions (Sec. II-B), enabling trajectory generation in microseconds to milliseconds. It is also important to note that existing flatness-based sampling-based planners either do not prove completeness and optimality or loosely mention the existing guarantees of geometric planners, *e.g.*, those of RRT\* \[bascetta2017flat, vu2022sampling, wang2024differential, seemann2014exact, ye2022efficient\]. Achieving such theoretical guarantees with closed-form BVP solutions is nontrivial as it requires careful consideration of nonlinear local paths rather than linear edges on the graph. We address this by offering a theoretical analysis of probabilistic exhaustivity, which is stronger than completeness, and asymptotic optimality of our approach in Sec. VI.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-B Hardware-accelerated Motion Planning", "weight": 1.0} -->

Motion planning can be time-consuming as it relies on multiple computationally expensive subroutines, such as forward kinematics (fk), collision checking (cc) and nearest neighbor (nn) search. With recent advances in parallel computing, much progress has been made to improve these subroutines and enhance planning performances via both *coarse-grained* and *fine-grained* parallelization.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-B Hardware-accelerated Motion Planning", "weight": 1.0} -->

*Coarse-grained* parallelization techniques typically run multiple subroutines or even multiple instances of the planners at the thread or process levels. Early work focuses on improving motion plans by merging and averaging out the paths from different instances of the planners \[raveh2011little\], or by adapting existing planners to run their subroutines in parallel \[amato1999probabilistic, ichnowski2012parallel\]. Parallelized motion planning can also be achieved by partitioning the configuration space \[jacobs2012scalable, werner2025gcs\] or the planning tree construction \[plaku2005sampling, vu2022sampling, perrault2025kino\]. Closely related to our work, \[vu2022sampling\] also employs differential flatness to generate dynamically feasible trajectories, however, by coarsely growing multiple planning subtrees in parallel for a specific gantry crane system.

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-B Hardware-accelerated Motion Planning", "weight": 1.0} -->

Recently, the prevalence of GPUs enables impressive improvements in motion planning \[bhardwaj2022storm, sundaralingam2023curobo, fishman2023motion, le2025global, le2025model\] but suffers from costly GPU resources and communication overhead between CPUs and GPUs. GPU-based planning methods often grow a planning tree in parallel by propagating the robot dynamics, *e.g.*, Kino-PAX \[perrault2025kino\], or via approximate dynamic programming recursion, *e.g.*, GMT\* \[ichter2017gmt\], and are shown to generate a robot trajectory in milliseconds for low-d o f systems with simple forward kinematics. For high-d o f robots, cuRobo \[sundaralingam2023curobo\] generates geometric paths as seeds for a parallelized trajectory optimization solver under kinematics constraints such as velocity, acceleration and jerk limits.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-B Hardware-accelerated Motion Planning", "weight": 1.0} -->

*Fine-grained* parallelization techniques focus on parallelizing primitive operations in a motion planning algorithm, *e.g.*, via "single instruction/multiple data" (simd) instructions on consumer-grade CPUs. This has been shown to provide extremely fast geometric motion planning subject to collision avoidance constraints, with planning times ranging from microseconds to milliseconds \[thomason2024vamp, ramsey2024-capt, wilson2024nearest\]. To check an edge (a line segment) for collision, VAMP \[thomason2024vamp\] uses simd instructions to efficiently perform parallelized forward kinematics and collision checking on multiple configurations, generated via linear interpolation. While this approach is promising, it is challenging to enforce additional requirements via parallelized primitive operations such as dynamics and non-holonomic constraints.

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-B Hardware-accelerated Motion Planning", "weight": 1.0} -->

Particularly, enforcing nonlinear dynamics constraints with fine-grained parallelism is non-trivial due to the intractability of BVP problems, as mentioned in Sec. II-A. We instead leverage the differential flatness property to obtain time-parameterized solutions that can be discretized at arbitrary times and hence, amenable to SIMD-based primitive operations. Our deliberate fusion of differential flatness and SIMD parallelism effectively brings the benefits of "fine-grained" parallelized forward kinematics and collision checking to kinodynamic planning. Thanks to the closed-form BVP solution in the flat output space, we will later show that our approach achieves planning times of merely a few milliseconds.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Consider a robot with state $\mathbf{x}\in{\cal X}$ and control $\mathbf{u}\in{\cal U}$. For example, the state of a manipulator can include the joint configuration $\mathbf{q}$ and possibly its derivatives, while the control input can be the torques being applied on the robot joints. Let ${\cal X}_{free}$ and ${\cal X}_{obs}={\cal X}\setminus{\cal X}_{free}$ be the free and occupied spaces, respectively, which can be generated from robot constraints such as collision avoidance or joints limits.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The robot motion is governed by a nonlinear dynamics function $\mathbf{f}$ of the state $\mathbf{x}$ and the control $\mathbf{u}$ as follows: A time-parameterized trajectory $\boldsymbol{\sigma}:\rightarrow{\cal X}$ for time $t\in$ is called dynamically feasible if there exists a time-parameterized control input $\mathbf{u}:\rightarrow{\cal U}$ such that the robot dynamics is satisfied by the trajectory: Given an initial robot state $\mathbf{x}_{s}$ and a goal region ${\cal G}{\subset{\cal X}}$, as a subset of ${\cal X}$, the kinodynamic motion planning problem aims to find a dynamically feasible trajectory $\boldsymbol{\sigma}(t)$ with control input $\mathbf{u}(t)$, connecting the initial state $\mathbf{x}_{s}$ to the goal region ${\cal G}$ in the free space ${\cal

<!-- chunk {"id": "body-0038", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

X}_{free}$ as described in Problem 1. The goal region ${\cal G}$ commonly represents a desired state or a region that a goal state can be sampled.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Problem 1", "weight": 1.0} -->

| In the remainder of the paper, we solve Problem 1 by developing FLASK, a parallelized kinodynamic motion planning framework for differential flat robot systems, including common platforms such as ground and aerial vehicles, and manipulators.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Our approach offers ultrafast planning time and exact dynamically feasible trajectory solution without the need to approximate the robot dynamics. Occasionally, we will drop the notation of time dependence for readability.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A Sampling-based Kinodynamic Motion Planning", "weight": 1.0} -->

Most sampling-based geometric planners, such as RRT-connect \[kuffner2000rrtconnect\] and PRM \[kavraki2002probabilistic\] consider the robot configuration $\mathbf{q}$ as the state $\mathbf{x}$ and approximate the robot's configuration space with a tree or graph $\mathbb{G}$ with a set of nodes $\mathbb{V}$ and a set of edges $\mathbb{E}$. Though individual sampling-based planners differ wildly in their exact approach, they all have roughly the same structure for their main search loop. At each iteration, such planners attempt to add a new sample $\mathbf{x}_{f}$ to $\mathbb{V}$, then connect $\mathbf{x}_{f}$ to some existing $\mathbf{x}_{0}\in\mathbb{V}$, and if successful, add the resulting edge to $\mathbb{E}$. This is called a Connect or Extend subroutine.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A Sampling-based Kinodynamic Motion Planning", "weight": 1.0} -->

To construct edges, all geometric sampling-based planners require a *local planner* to produce a local path between configurations.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-A Sampling-based Kinodynamic Motion Planning", "weight": 1.0} -->

However, in kinodynamic motion planning, where robots are subjected to dynamics constraints, finding a local path $\mathbf{x}_{loc}(t)$ to reach $\mathbf{x}_{f}$ with control input $\mathbf{u}_{loc}(t)$ in duration $T$, requires solving a *boundary value problem* (BVP), subject to the robot dynamics with initial state $\mathbf{x}_{0}$ and terminal state $\mathbf{x}_{f}$ as follows: Solving the BVP in practice is often computationally intractable, so most kinodynamic planners (*e.g.*, \[lavalle2001randomized, hsu2022randomizekinodynamic, li2016sst\]) instead take a propagation-based approach: they integrate a sampled control input $\mathbf{u}_{0}$ from a reachable state for a short time $T$ to generate a new state $\mathbf{x}_{f}$ rather than connecting sampled states.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 1", "weight": 1.0} -->

Consider a *fully-actuated manipulator* with joint angles $\mathbf{q}$, and control input $\mathbf{u}$, *e.g.*, the joint torques. This is typically the case for common manipulators such as Franka or KUKA platforms. The robot dynamics is described by the Euler-Lagrange equation of motions: where the control gain matrix $\mathbf{B}(\mathbf{q})$ is typically invertible, *i.e.*, the system is fully actuated. The robot dynamics can be expressed in the form of Eq. with the robot state $\mathbf{x}=(\mathbf{q},\dot{\mathbf{q}})$. For this system, the flat output is the same as the configuration: $\mathbf{y}=\mathbf{q}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example 1", "weight": 1.0} -->

| | | As the control gain $\mathbf{B}(\mathbf{q})$ is invertible, the control input $\mathbf{u}$ in is guaranteed to exist.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Example 2", "weight": 1.0} -->

Consider a *unicyle* robot whose state $\mathbf{x}$ is defined as $\mathbf{x}=(x,y,\theta)$ where $(x,y)$ is the position and $\theta$ is the heading angle of the vehicle. The control input $\mathbf{u}=(v,\omega)$ includes the speed $v$ and angular velocity $\omega$. The flat output $\mathbf{y}$ is defined as the position: $\mathbf{y}=(x,y)$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Example 3", "weight": 1.0} -->

Consider an *under-actuated quadrotor* whose state $\mathbf{x}$ is defined as $\mathbf{x}=(\mathbf{p},\mathbf{R},\mathbf{v},\boldsymbol{\omega})$, where $\mathbf{p}=(x,y,z)\in\mathbb{R}^{3}$ is the position of the center of mass, $\mathbf{R}\in SO$ is the rotation matrix, $\mathbf{v}$ is the linear velocity, and $\boldsymbol{\omega}$ is the angular velocity. The control input $\mathbf{u}=(f,\boldsymbol{\tau})$ consists of a thrust $f\in\mathbb{R}_{\geq 0}$ and a torque $\boldsymbol{\tau}\in\mathbb{R}^{3}$, generated from the motors.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Example 3", "weight": 1.0} -->

The flat output for quadrotor systems is $\mathbf{y}=(\mathbf{p},\psi)\in\mathbb{R}^{4}$, where $\psi$ is the yaw angle of the robot \[mellinger2011minimumsnap\].

<!-- chunk {"id": "body-0049", "role": "body", "section": "Example 3", "weight": 1.0} -->

(a) Samples from a linear path [thomason2024vamp].

<!-- chunk {"id": "body-0050", "role": "body", "section": "Example 3", "weight": 1.0} -->

(b) Samples from a nonlinear local path xloc(t).

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-C CPU fine-grained parallelism", "weight": 1.0} -->

Fine-grained parallelization techniques such as "single instruction, multiple data" (simd) are ubiquitous on consumer CPUs and have recently shown significant improvement in sampling-based geometric motion planning by performing forward kinematics and collision checking on multiple configurations in parallel. Vectorization via simd allows simultaneously applying the same primitive operations on multiple variables. VAMP \[thomason2024vamp\], a simd-accelerated planning method, uses this technique to perform parallelized collision checking of multiple robot configurations, evenly sampled along a line segment (Fig. 2(a)) connecting two nodes on a planning tree or graph. Given the set of configurations, the robot's geometric shape, described by a set of SIMD-compatible shapes such as capsules or spheres in the workspace, is calculated via branchless forward kinematics and checked for collision against the obstacle geometry. simd-based collision checking requires access to all the states along a local path, typically through an analytical form of the motion.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-C CPU fine-grained parallelism", "weight": 1.0} -->

However, under dynamics constraints, the nonlinear local path $\mathbf{x}_{loc}(t)$ that solves the BVP problem (Sec. IV-A) is computationally intractable, prohibiting configuration sampling at multiple arbitrary times in advance. In the next section, we address this problem by deriving a closed-form time-parameterized local path $\mathbf{x}_{loc}(t)$ based on the differential flatness property and sampling multiple states at different times, as illustrated in Fig. 2(b).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Technical Approach", "weight": 1.0} -->

In this section, we present our kinodynamic planning framework, FLASK, by showing that the flat output evolves as a linear system (Sec. V-A), and hence, allows us to convert Problem 1 from the original state space ${\cal X}$ to a flat state space (Problem 2 in Sec. V-B). In the flat state space, we develop primitive subroutines, FlaskExtend for planning graph construction in Sec. V-C and FlaskCC for parallelized forward kinematics and collision checking in Sec. V-D, that work with any sampling-based planning method. These subroutines are the core of our framework in Alg. 1, which effectively turns any geometric motion planner into a kinodynamic version. As a result, instead of being tied to a specific planner, our general framework gives rise to a new class of ultrafast kinodynamic planners for a broad class of differentially flat robot systems. Finally, we discuss trajectory postprocessing in our approach in Sec. V-E.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-A Flat Output Dynamics as a Linear System", "weight": 1.0} -->

Consider the $n$-dimensional flat output $\mathbf{y}$ in Def. 1. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness"), that can be used to recover the state $\mathbf{x}$ and control input $\mathbf{u}$ via Eq. (7. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")). Let $\mathbf{w}\in{{\cal W}\subset\mathbb{R}^{n}}$ be a pseudo-control input, defined as the $r$th derivative of the output $\mathbf{y}$: where the derivative orders $l,m$ are defined in Eq. 7. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness").

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-A Flat Output Dynamics as a Linear System", "weight": 1.0} -->

Let $\mathbf{z}~\in~{\cal Z}\subset\mathbb{R}^{rn}$ be the flat state, defined as: The state $\mathbf{z}$ satisfies linear dynamics with the pseudo-control input $\mathbf{w}$ as follows: with $\mathbf{A}\in\mathbb{R}^{rn\times rn}$, $\mathbf{B}\in\mathbb{R}^{rn\times n}$, and the identity matrix $\mathbf{I}_{n}~\in~\mathbb{R}^{n\times n}$. Instead of enforcing the nonlinear dynamics constraint in a motion planning problem, we can implicitly enforce a much simpler linear dynamics in the flat state space via the conversion (7. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")).

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-A Flat Output Dynamics as a Linear System", "weight": 1.0} -->

Note that the matrix $\mathbf{A}$ is nilpotent with index $r$, *i.e.*, $\mathbf{A}^{r}=0$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-B Sampling-based Kinodynamic Planning in Flat State Space", "weight": 1.0} -->

Due to the non-linearity of the robot dynamics, it is challenging to plan robot motions in the original state space ${\cal X}$, as most sampling-based motion planning algorithms require a challenging Extend subroutine that either solves a boundary value problem to connect two states $\mathbf{x}_{0}$ and $\mathbf{x}_{f}$ or propagates the dynamics to predict the next state $\mathbf{x}_{f}$ given a constant control input $\mathbf{u}_{0}$. As shown in Sec. V-A, the flat state $\mathbf{z}$ satisfies a linear dynamics in with a nilpotent matrix $\mathbf{A}$, potentially leading to much simpler BVP problem and dynamics propagation. This motivates us to perform motion planning in the flat state space ${\cal Z}$ instead of the original state space ${\cal X}$, thanks to the conversions (6.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-B Sampling-based Kinodynamic Planning in Flat State Space", "weight": 1.0} -->

‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")) and (7. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")). Our approach is illustrated in Fig. 3.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-B Sampling-based Kinodynamic Planning in Flat State Space", "weight": 1.0} -->

Note that in many common robot systems such as Examples 1, 2 and 3, the flat output $\mathbf{y}$ does not depend on $\mathbf{u}$ and therefore, the values of $\mathbf{u}_{s}$ and $\mathbf{u}_{\cal G}$ need not be specified. The original kinodynamic motion planning (Problem 1) becomes finding a dynamically feasible trajectory $\boldsymbol{\sigma}_{\mathbf{z}}(t)$ in the flat state space ${\cal Z}$ that connects the start $\mathbf{z}_{s}$ to the goal region ${\cal G}_{\mathbf{z}}$, and satisfies the linear dynamics, as summarized in Problem 2.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Problem 2", "weight": 1.0} -->

To solve Problem 2, we develop primitive subroutines in the flat state space ${\cal Z}$ for a sampling-based kinodynamic planning framework proposed in Alg. 1, which is consistent with most existing sampling-based motion planners \[karaman2010kinorrt, webb2013kinodynamicRRT, li2016sst\].

<!-- chunk {"id": "body-0061", "role": "body", "section": "Problem 2", "weight": 1.0} -->

Leveraging the linear dynamics, we develop an efficient FlaskExtend subroutine (see Sec. V-C) to construct a graph or tree $\mathbb{G}_{\mathbf{z}}=(\mathbb{V}_{\mathbf{z}},\mathbb{E}_{\mathbf{z}})$ in the flat state space ${\cal Z}$, where $\mathbb{V}_{\mathbf{z}}$ and $\mathbb{E}_{\mathbf{z}}$ denote the sets of nodes and edges, respectively, by solving the BVP and dynamics propagation problems for a polynomial local "flat" path $\mathbf{z}_{loc}(t)$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Problem 2", "weight": 1.0} -->

pseudo-control $\mathbf{w}_{i}(t)$ is applied in the time interval $[t_{i-1},t_{i}]$, for $i=1,\ldots,M$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Problem 2", "weight": 1.0} -->

The trajectory $\boldsymbol{\sigma}_{\mathbf{z}}(t)$ is converted back to a trajectory $\boldsymbol{\sigma}(t)$ with control $\mathbf{u}(t)$ as follows: | | $\displaystyle\boldsymbol{\sigma}(t)$ | $\displaystyle=\boldsymbol{\alpha}(\boldsymbol{\sigma}_{\mathbf{z}}(t),\mathbf{w}(t)),$ | | \(19\) | | | $\displaystyle\mathbf{u}(t)$ | $\displaystyle=\boldsymbol{\beta}(\boldsymbol{\sigma}_{\mathbf{z}}(t),\mathbf{w}(t)),$ | | | which is possible because the pseudo-control input $\mathbf{w}$ is the $r$-th order derivative of $\mathbf{y}$ with

<!-- chunk {"id": "body-0064", "role": "body", "section": "Problem 2", "weight": 1.0} -->

/* Grow 𝔾z on the flat state space *//* Return σ(t) if reaching ${\cal G}_{\mathbf{z}}$ */11 if Goal region ${\cal G}_{\mathbf{z}}$ is reached then 12 Find the trajectory σz(t) with pseudo-input w(t) from 𝔾z.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Problem 2", "weight": 1.0} -->

/* Convert the trajectory σz(t) to the original state space */16 return Trajectory σ(t) with control u(t). return Trajectory not found. Algorithm 1 FLASK: Sampling-based Kinodynamic Motion Planning via Differential Flatness

<!-- chunk {"id": "body-0066", "role": "body", "section": "V-C FlaskExtend Subroutine on Flat Output Space", "weight": 1.0} -->

The goal of the FlaskExtend subroutine, described in Alg. 2, is to find a collision-free dynamically feasible local "flat" path $\mathbf{z}_{loc}(t),t\in[0,T]$ with a time duration $T$, that connects an existing node $\mathbf{z}_{0}\in\mathbb{V}$ to a new node $\mathbf{z}_{f}$. A motion $\mathbf{z}_{loc}(t)$ can be generated by either sampling $\mathbf{z}_{f}$ and solving a BVP problem (Sec. V-C1) or sampling a pseudo-control input $\mathbf{w}_{0}$ and integrating the flat state dynamics (Sec. V-C2).

<!-- chunk {"id": "body-0067", "role": "body", "section": "V-C FlaskExtend Subroutine on Flat Output Space", "weight": 1.0} -->

For either case, we show that a closed-form expression of $\mathbf{z}_{loc}(t)$ can be obtained for parallelized collision checking in FlaskCC subroutine in Sec. V-D. If $\mathbf{z}_{loc}(t)$ is valid, the node $\mathbf{z}_{f}$ is added to $\mathbb{V}_{\mathbf{z}}$ while the edge $(\mathbf{x}_{0},\mathbf{x}_{f})$ associated with the local "flat" path $\mathbf{z}_{loc}(t)$ is added to $\mathbb{E}_{\mathbf{z}}$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "V-C FlaskExtend Subroutine on Flat Output Space", "weight": 1.0} -->

Input: The planning graph/tree 𝔾z = (𝕍z, 𝔼z) 2if Sample $\mathbf{z}_{f}\in{\cal Z}$ then 3 Pick an existing node Z0 ∈ 𝕍z /* Solve BVP in closed form */4 zloc(t)← Eq. with a sampled T or an optimal T = T*.

<!-- chunk {"id": "body-0069", "role": "body", "section": "V-C FlaskExtend Subroutine on Flat Output Space", "weight": 1.0} -->

/* Analytically propagate dynamics */9if not FlaskCC(zloc(t), wloc(t)) then

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-C1 Solving the BVP Problem in Closed Forms", "weight": 1.0} -->

Given an existing node $\mathbf{z}_{0}$ and a sampled $\mathbf{z}_{f}$, we find a local "flat" path $\mathbf{z}_{loc}(t),t\in[0,T]$ that connects $\mathbf{z}_{0}$ and $\mathbf{z}_{f}$ and satisfies the flat state dynamics. Consider a cost function of a motion $\mathbf{z}(t),t\in[0,T]$ with pseudo-control $\mathbf{w}(t)$ that accounts for the total control effort and the time duration $T$ as follows: where $\mathbf{R}\succ 0$ is a user-defined positive definite weight matrix, and $\rho$ controls the trade-off between the control effort and the time it takes to finish the trajectory.

<!-- chunk {"id": "body-0071", "role": "body", "section": "V-C1 Solving the BVP Problem in Closed Forms", "weight": 1.0} -->

We formulate the following Linear Quadratic Minimum Time (LQMT) problem \[Verriest1991QuadMinTime\] to solve for our local "flat" path $\mathbf{z}_{loc}(t)$ and control $\mathbf{w}_{loc}(t)$: | | | $\displaystyle\min_{\mathbf{w}(t),T}{{\cal C}(\mathbf{z}(t),\mathbf{w}(t),T)}$ | | \(21\) | | | s.t.

<!-- chunk {"id": "body-0072", "role": "body", "section": "V-C1 Solving the BVP Problem in Closed Forms", "weight": 1.0} -->

Given a sample $\mathbf{z}_{f}$, the cost ${\cal C}_{loc}$ of the local path $\mathbf{z}_{loc}(t)$ is commonly used to choose an existing node $\mathbf{z}_{0}$ on the graph $\mathbb{G}_{\mathbf{z}}$, *e.g.*, those in the neighborhood of $\mathbf{z}_{f}$ with ${\cal C}_{loc}$ smaller than a threshold $\zeta$ (see Sec. VI for how to choose the value of $\zeta$ as the number of nodes $N=|\mathbb{V}_{\mathbf{z}}|$ increases).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Fixed-time Optimal Local Paths", "weight": 1.0} -->

For a fixed time duration $T$, the LQMT problem has a closed-form solution, by following \[Verriest1991QuadMinTime\], for the optimal pseudo-control input: with the optimal cost: and the optimal local "flat" path: Since the matrix $\mathbf{A}$ is nilpotent, *i.e.,* $\mathbf{A}^{r}=0$, we have $e^{\mathbf{A}t}~=~\sum_{j=0}^{r-1}\frac{\mathbf{A}^{j}t^{j}}{j!}$. Therefore, the Grammian $\mathbf{G}_{T}$ and $\mathbf{d}_{T}$ become polynomials of the time duration $T$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Fixed-time Optimal Local Paths", "weight": 1.0} -->

The optimal control input $\mathbf{w}_{loc}(t)$ becomes a $(r-1)$th order polynomial while the optimal flat output trajectory $\mathbf{y}_{loc}(t)$ is a $(2r-1)$th order polynomial, which is compatible with simd-based collision checking in Sec. V-D.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Minimum-time Optimal Local Paths", "weight": 1.0} -->

If we have the freedom to choose the duration $T$, we can solve the following equation for a minimum time $T=T^{*}$ \[Verriest1991QuadMinTime\]: For an arbitrary value of the pseudo-control order $r$, the minimum-time condition can be solved for a positive $T^{*}$ using a numerical root-finding solver \[nocedal1999numerical\], that is amenable to simd parallelization such as L-BFGS \[zhu1997lbfgsb\]. More notably, many common systems such as manipulators (Example 1) or unicycles (Example 2) have $r=2$ while systems with higher $r$, such as quadrotors (Example 3), can reduce the pseudo-control order to $r=2$ to simplify motion planning in practice, as shown in \[liu2017search\]. For such cases, Example 4.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Minimum-time Optimal Local Paths", "weight": 1.0} -->

‣ Minimum-time Optimal Local Paths ‣ V-C1 Solving the BVP Problem in Closed Forms ‣ V-C FlaskExtend Subroutine on Flat Output Space ‣ V Technical Approach ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness") below shows the optimal local "flat" path, pseudo-control input, and optimal duration, where the condition is equivalent to solving a $4$th-order polynomial in (28. ‣ Minimum-time Optimal Local Paths ‣ V-C1 Solving the BVP Problem in Closed Forms ‣ V-C FlaskExtend Subroutine on Flat Output Space ‣ V Technical Approach ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")) for a positive root, which can also be done in closed forms. As a result, solving for an optimal time $T=T^{*}$ is suitable for simd parallelization.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Remarks", "weight": 1.0} -->

We note that the closed-form polynomial solution of the LQMT problem is derived without considering additional constraints such as collision avoidance, velocity and acceleration limits. In our approach, such constraints are enforced via collision checking in Sec. V-D. If the trajectory $\mathbf{z}_{loc}(t)$ in from $\mathbf{z}_{0}$ to $\mathbf{z}_{f}$ violates a constraint, it will be considered invalid. However, it does not necessarily mean that $\mathbf{z}_{f}$ is unreachable from $\mathbf{z}_{0}$. If there exists a constrained optimal trajectory $\mathbf{z}^{*}_{loc}(t)$, our Theorem 1.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Remarks", "weight": 1.0} -->

‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness") in Sec. VI shows that as the number of samples $N=|\mathbb{V}_{\mathbf{z}}|$ goes to infinity, the probability of having a piecewise-polynomial trajectory that is close to $\mathbf{z}^{*}_{loc}(t)$ (see Def. 2. ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")) tends to $1$, *i.e.*, $\mathbf{z}_{f}$ can still be reached via a sequence of nodes with high probability.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Remarks", "weight": 1.0} -->

Interestingly, recent results from optimal control \[beaver2024optimal\] find an optimal piecewise-polynomial local path under constraints for differentially flat systems by carefully switching between modes, each of which corresponds to a polynomial motion primitive. This approach solves an optimality condition on the cost function and the constraints to find an optimal mode schedule and is shown to generate an optimal trajectory for low-DOF systems with simple closed-form constraints in a few milliseconds. However, it is challenging to design such a mode-switching mechanism for high-DOF robots with complex geometry due to complicated forward kinematics, especially when the local path generation time is often restricted to the nanosecond range. Intriguingly, from a sampling-based perspective, our Theorem 1.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Remarks", "weight": 1.0} -->

‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness") (see Sec. VI) shows that such an optimal piecewise-polynomial local path can be found on our planning graph with high probability, *i.e.*, a sequence of nodes on our graph is equivalent to the mode-switching schedule from \[beaver2024optimal\]. Nevertheless, this is an exciting direction for generating a constrained local path $\mathbf{z}_{loc}(t)$ in our framework that we leave for future work.

<!-- chunk {"id": "body-0081", "role": "body", "section": "V-C2 Dynamics Propagation in Closed-Forms", "weight": 1.0} -->

As BVP problems are challenging to solve, most existing work \[li2016sst\] resorts to dynamics propagation, where the planning tree is extended by sampling a constant control input and integrating the robot dynamics over small time steps using numerical methods. While our *BVP closed-form solution* in Sec. V-C1 *is the main focus of our paper*, this section shows that transforming the kinodynamic planning problem to the flat state space (Problem 2) also leads to closed-form dynamics propagation, and hence gets rid of numerical approximations with potentially high accumulated errors.

<!-- chunk {"id": "body-0082", "role": "body", "section": "V-C2 Dynamics Propagation in Closed-Forms", "weight": 1.0} -->

Instead of sampling the original control input, we sample the pseudo-control input $\mathbf{w}_{loc}(t)=\mathbf{w}_{0}$ and the duration $T$, leading to a closed-form local path: where $\mathbf{y}_{loc}(t)=\frac{\mathbf{w}_{0}}{r!}t^{r}+\sum_{i=0}^{r-1}\frac{\mathbf{y}^{(i)}_{0}}{i!}t^{i}$. These local "flat" paths can be used in tree-based kinodynamic planners such as Stable Sparse RRT \[li2016sst\] and are also suitable for parallelized forward kinematics and collision checking in Sec. V-D. Propagation-based planners tend to "wander" in the state space due to the suboptimality of random control with small time steps $T$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "V-C2 Dynamics Propagation in Closed-Forms", "weight": 1.0} -->

Interestingly, our BVP solutions can help by finding shortcuts to the goal rather than keep expanding the tree, and therefore reduce the planning time significantly as illustrated in Sec. VII-A.

<!-- chunk {"id": "body-0084", "role": "body", "section": "V-C2 Dynamics Propagation in Closed-Forms", "weight": 1.0} -->

Input: Flat state path zloc(t) with pseudo-control w(t) Output: Whether zloc(t) collides with obstacles /* Convert to the original state space */1 xloc(t) ← α(zloc(t), wloc(t)), 2uloc(t) ← β(zloc(t), wloc(t)) 3for $i\in\{0,\ldots,\left\lceil\frac{N}{K}\right\rceil\}$ do /* Parallel checking via simd [thomason2024vamp] */4 if $\exists j\in\mathbf{b}_{i}:\mathbf{x}_{loc}(t_{j})\in{\cal X}_{obs}$ then /* checking other constraints such as state and control limits */6 if ∃j ∈ bi: xloc(tj), uloc(tj) violate other constraints then

<!-- chunk {"id": "body-0085", "role": "body", "section": "V-D Vectorized Collision Checking", "weight": 1.0} -->

To perform collision checking on a local "flat" path $\mathbf{z}_{loc}(t)$ with pseudo-control $\mathbf{w}_{loc}(t)$ (Alg.

<!-- chunk {"id": "body-0086", "role": "body", "section": "V-D Vectorized Collision Checking", "weight": 1.0} -->

3), we convert it back to the original state space ${\cal X}$ and obtain the corresponding closed-form local path and control: | | $\displaystyle\mathbf{x}_{loc}(t)$ | $\displaystyle=\boldsymbol{\alpha}(\mathbf{z}_{loc}(t),\mathbf{w}_{loc}(t))$ | | \(30\) | | | $\displaystyle\mathbf{u}_{loc}(t)$ | $\displaystyle=\boldsymbol{\beta}(\mathbf{z}_{loc}(t),\mathbf{w}_{loc}(t)).$

<!-- chunk {"id": "body-0087", "role": "body", "section": "V-D Vectorized Collision Checking", "weight": 1.0} -->

$t_{1},t_{2},\ldots,t_{N}~\in~[0,T]$, grouped into several spatially distributed batches of size $K$: for $i=0,\ldots,\left\lceil\frac{N}{K}\right\rceil$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "V-D Vectorized Collision Checking", "weight": 1.0} -->

For each batch $\mathbf{b}_{i}$, we obtain a set of samples $\{\mathbf{x}_{loc}(t_{j})\}_{t_{j}\in\mathbf{b}_{i}}$ and perform fast parallelized collision checking via simd instructions, as illustrated in Fig. 2(b). The batch size $K$ is the number of floats that a simd register can store, *e.g.*, $K=8$ for the commonly used AVX2 instruction set. The robot's geometry is represented by a set of SIMD-compatible primitive shapes such as spheres or capsules, whose poses are calculated via forward kinematics for multiple states and checked for collisions with obstacles using simd parallelism. If any state in batch $\mathbf{b}_{i}$ leads to collisions with an obstacle, we terminate the collision checking subroutine early and move on to other local paths.

<!-- chunk {"id": "body-0089", "role": "body", "section": "V-D Vectorized Collision Checking", "weight": 1.0} -->

Similarly, other constraints such as state and control limits can be checked in parallel for each batch $\mathbf{b}_{i}$ to validate $\mathbf{z}_{loc}(t)$. In general, the conversions (6. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")) and (7. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")) are nonlinear and might complicate the exact conversions of state and control limits on $(\mathbf{x},\mathbf{u})$ to corresponding flat state and pseudo-control limits on $(\mathbf{z},\mathbf{w})$. For many common robot systems, an upper bound on the conversions (7.

<!-- chunk {"id": "body-0090", "role": "body", "section": "V-D Vectorized Collision Checking", "weight": 1.0} -->

‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")) can be obtained to estimate the limits in the flat state space as the flat output $\mathbf{y}$ is often part of the original state $\mathbf{x}$ (see Examples 1, 2 and 3). For example, any limits on the joint angles and velocities of a manipulator in Example 1 can be directly translated to the flat state or any limits on the speed $v$ of a unicyle in Example 2 can be used to bound the first derivative of the flat out put $(\dot{x},\dot{y})$. Furthermore, since the flat output describes certain physical properties of the robot, *e.g.*, the position and yaw angle of a quadrotor in Example 3, users can also directly specify the flat state and pseudo-control constraints, *e.g.*, maximum linear velocity and yaw rates.

<!-- chunk {"id": "body-0091", "role": "body", "section": "V-D Vectorized Collision Checking", "weight": 1.0} -->

For general nonlinear systems, this issue can be addressed by using large limits in the flat state space, and checking the local path $(\mathbf{x}_{loc}(t),\mathbf{u}_{loc}(t))$ in against the original state and control limits on $(\mathbf{x},\mathbf{u})$ via sampling. However, there is a trade-off between the size of the flat state space and the risk of missing valid paths, which can be tuned based on the planner's performance, *e.g.*, the larger flat state space may lead to longer planning time but reduce the risk.

<!-- chunk {"id": "body-0092", "role": "body", "section": "V-D Vectorized Collision Checking", "weight": 1.0} -->

Input: A collision-free piecewise-polynomial trajectory σz(t) = {(zi(t), ti)}i = 1M, with control inputs wz(t) = {wi(t), ti)}i = 1M, 4 Calculate zij(t) from Eq. with z0 = zi(ti − 1), zf = zj(tj), and a time Tij = tj − ti − 1 or an optimal Tij. 5 Calculate wij(t) from Eq..

<!-- chunk {"id": "body-0093", "role": "body", "section": "V-D Vectorized Collision Checking", "weight": 1.0} -->

/* Bypass unnecessary motions if the trajectory zij(t) does not violates any constraints */6 if not FlaskCC(zij(t), wij(t)) then 7 Replace {(zi(t), ti)}k = ij by (zij(t), ti − 1 + Tij). 8 Replace {(wi(t), ti)}k = ij by (wij(t), ti − 1 + Tij). Algorithm 4 Trajectory Postprocessing

<!-- chunk {"id": "body-0094", "role": "body", "section": "V-E Trajectory Postprocessing", "weight": 1.0} -->

Our kinodynamic planning approach in Sec. V-B returns a piecewise-polynomial trajectory: $\boldsymbol{\sigma}_{\mathbf{z}}(t)=\left\{(\mathbf{z}_{i}(t),t_{i})\right\}^{M}_{i=1}$, for $0=t_{0}<t_{1}<\ldots<t_{M}$ where the polynomial $\mathbf{z}_{i}(t),t\in[t_{i-1},t_{i}]$ corresponds to the pseudo-control $\mathbf{w}_{i}(t)$ and time duration $T_{i}=t_{i}-t_{i-1}$. Due to the sampling-based nature of our approach, the trajectory might contain unnecessary local paths and often requires further postprocessing, *e.g.*, by seeking shortcuts between nodes. For completeness, a simple trajectory postprocessing scheme is provided in Alg.

<!-- chunk {"id": "body-0095", "role": "body", "section": "V-E Trajectory Postprocessing", "weight": 1.0} -->

4 such that if there exists a collision-free trajectory $\mathbf{z}_{ij}(t)$ that connects two nodes $\mathbf{z}_{i}(t_{i-1})$ and $\mathbf{z}_{j}(t_{j})$, the local paths $\mathbf{z}_{k}$, $i\leq k\leq j$ in between can simply be bypassed by $\mathbf{z}_{ij}(t)$. We note that our approach is general and therefore, compatible with other complex trajectory shortening schemes such as \[geraerts2007creating, hauser2010trajsim\].

<!-- chunk {"id": "body-0096", "role": "body", "section": "Probabilistic Exhaustivity and Optimality Analysis", "weight": 1.0} -->

In this section, we will examine the *probabilistic exhaustivity* of our FLASK framework (Sec. VI-A), which is a key concept for proof of optimality common among asymptotically optimal planners \[bekris2020AOSurvey, karaman2011optimalmp, janson2015fmt\]. As our approach is general and compatible with most sampling-based motion planners, we provide an outline of the *optimality analysis* in Sec. VI-B based on the proven probabilistic exhaustivity property.

<!-- chunk {"id": "body-0097", "role": "body", "section": "VI-A Probabilistic Exhaustivity", "weight": 1.0} -->

The probabilistic exhaustivity property, introduced in \[kavraki1998analysis, schmerling2015optimal_driftless\], is stronger than probabilistic completeness \[lavalle2006planning\]. While probabilistic completeness only requires *one* solution to be found, *probabilistic exhaustivity* requires that *any* trajectory $\boldsymbol{\pi}$, with a $\delta$-clearance to the occupied regions of the state space (see Def. 2.

<!-- chunk {"id": "body-0098", "role": "body", "section": "VI-A Probabilistic Exhaustivity", "weight": 1.0} -->

‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")), can be approximated arbitrarily well with high probability by a piecewise trajectory $\boldsymbol{\sigma}$, composed of BVP solutions $\boldsymbol{\sigma}(t)=\left\{(\mathbf{x}_{i}(t),t_{i})\right\}^{M}_{i=1}$ connecting $M+1$ nodes $\{\bar{\mathbf{x}}_{i}\}_{i=0}^{M}$ on the graph, as the number of nodes tends to infinity. Our analysis relies on the following assumptions and definitions.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The pseudo-control input $\mathbf{w}=\mathbf{y}^{(r)}$ in Eq. 14 has $r$ strictly larger than $l$ (defined in Eq. 7. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")). This is the common case as seen in Examples 1, 2, and 3. As a result, the original state $\mathbf{x}$ can be recovered using Eq. 7. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness") solely from the flat state $\mathbf{z}$: $\mathbf{x}~=~\boldsymbol{\alpha}(\mathbf{z})$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "VI-B Optimality Analysis", "weight": 1.0} -->

As our FLASK framework in Sec. V (Alg. 1) is compatible with any sampling-based motion planners \[orthey2024-review-sampling\], the optimality guarantees of our trajectory depend on the optimality guarantees of the specific planner that integrates our FlaskExtend subroutine. However, we provide an outline of an optimality analysis based on random geometric graphs \[penrose2003random\] which many asymptotically optimal sampling-based motion planners follow (see \[karaman2011optimalmp, webb2013kinodynamicRRT, janson2015fmt\] for an example and \[bekris2020AOSurvey\] for an excellent review of this topic). Therefore, our framework not only transforms any sampling-based motion planner into its kinodynamic version but also preserves its optimality guarantees.

<!-- chunk {"id": "body-0101", "role": "body", "section": "VI-B Optimality Analysis", "weight": 1.0} -->

We define an optimal trajectory solution of Problem 2 with respect to the cost in Def. 4. ‣ VI-B Optimality Analysis ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness"). We note that while our cost function Eq. is defined in the flat state space, it bears physical meaning in the original space as the flat output $\mathbf{y}$ often describes certain physical properties of the robot, *e.g.*, the position and yaw angle of a quadrotor in Example 3. For example, if the pseudo-control input $\mathbf{w}=\mathbf{y}^{(r)}$ in has $r=2,3,4,\ldots$, the cost means that we would like to find a minimum acceleration-time, jerk-time, or snap-time trajectory, respectively (*e.g.*, in \[mellinger2011minimumsnap, liu2017search, liu2018search\]).

<!-- chunk {"id": "body-0102", "role": "body", "section": "Evaluation", "weight": 1.0} -->

(a) Unicycle: Bugtrap (top) and Wall (bottom).

<!-- chunk {"id": "body-0103", "role": "body", "section": "Evaluation", "weight": 1.0} -->

(b) 2D quadrotor: Bugtrap (top) and Hole (bottom).

<!-- chunk {"id": "body-0104", "role": "body", "section": "Evaluation", "weight": 1.0} -->

(c) 3D quadrotor: Window (top) and Obstacle (bottom).

<!-- chunk {"id": "body-0105", "role": "body", "section": "Evaluation", "weight": 1.0} -->

In this section, we will evaluate the effectiveness of our FLASK framework, applied on different planners and on different robot platforms, from low to high dimensional state spaces in both simulation and real experiments. As our method focuses on fast kinodynamic planning on CPUs, the results from our planners and the baselines are reported on an Intel i7-6900K CPU for a fair comparison. As a reference, we also provide the results from the GPU-based Kino-PAX \[perrault2025kino\] planner, which is run on a GeForce RTX 4070 GPU.

<!-- chunk {"id": "body-0106", "role": "body", "section": "VII-A Kinodynamic planning for low-d o f systems", "weight": 1.0} -->

In this section, we compare our approach with other kinodynamic planning algorithms provided by the *DynoBench* benchmark \[ortizharo2025iDbAstar\], which contains multiple low-d o f robots and benchmarking environments. We consider $3$ robot platforms: a *unicycle* (Example 2), a $2$D *quadrotor*, and a $3$D *quadrotor* (Example 3). The *unicycle* robot has the following constraints: maximum linear velocity $v\leq v_{max}=\qty{1.0}{\per}$, maximum angular velocity $\omega\leq\qty{1.5}{\per}$.

<!-- chunk {"id": "body-0107", "role": "body", "section": "VII-A Kinodynamic planning for low-d o f systems", "weight": 1.0} -->

The $3D$ *quadrotor* has the following parameters: mass $m=\qty{1}{}$, inertia matrix $\mathbf{J}~=~\text{diag}([0.1,0.1,0.2])\unit{\squared}$, maximum linear velocity $\|\mathbf{v}\|\leq\qty{4}{\per}$, maximum angular velocity $\|\boldsymbol{\omega}\|\leq\qty{8}{\per}$, maximum thrust $f=1.5mg\;\unit{}$, and maximum torque $\boldsymbol{\tau}~\leq~\qty{2}{}$, where $g\approx\qty{9.81}{\per\squared}$ is the gravitational acceleration.

<!-- chunk {"id": "body-0108", "role": "body", "section": "VII-A Kinodynamic planning for low-d o f systems", "weight": 1.0} -->

The $2$D *quadrotor*'s dynamics is a special case of the $3$D *quadrotor*'s with position $\mathbf{p}=[0,y,z]$, yaw angle $\psi=0$, and the rotation matrix $\mathbf{R}~=~\mathbf{R}_{\phi}$ of a pitch angle $\phi$, leading to a simplified flat output $\mathbf{y}=[y,z]\in\mathbb{R}^{2}$. The $2$D *quadrotor* is modeled after a Crazyflie \[giernacki2017crazyflie\] with mass $m=\qty{0.034}{}$, inertia $J=\qty{1e-4}{\squared}$, and arm length $\ell=\qty{0.1}{}$.

<!-- chunk {"id": "body-0109", "role": "body", "section": "VII-A Kinodynamic planning for low-d o f systems", "weight": 1.0} -->

The thrusts $f_{1}$ and $f_{2}$, generated from the two onboard motors, satisfy the following constraint: $0\leq f_{1},f_{2}\leq 0.65mg\;\unit{}$. The thrust and torque applied on the $2$D quadrotor's center of mass are calculated as: $f=f_{1}+f_{2}$ and $\tau=\ell(f_{1}-f_{2})$.

<!-- chunk {"id": "body-0110", "role": "body", "section": "VII-A Kinodynamic planning for low-d o f systems", "weight": 1.0} -->

For each platform, we consider $2$ DynoBench environments, shown in Fig. 5: *Bugtrap* and *Wall* for the unicycle, *Bugtrap* and *Hole* for the $2$D quadrotor, and *Window* and *Obstacle* for the $3$D quadrotor. To be compatible with simd-only collision checking, *e.g.*, \[thomason2024vamp\], the obstacles in each environment are represented by a set of spheres, while the unicycle and quadrotor's geometries are both modeled as single spheres.

<!-- chunk {"id": "body-0111", "role": "body", "section": "VII-A Kinodynamic planning for low-d o f systems", "weight": 1.0} -->

We apply our FLASK framework to obtain two planners: FLASK-RRTConnect with BVP solutions in Sec. V-C1 and three variants of FLASK-SST^∗^ with dynamics propagation in Sec. V-C2. Our kinodynamic FLASK-RRTConnect replaces a line segment connecting two nodes in an RRT tree by our closed-form BVP solution (local "flat" path) in the FlaskExtend subroutine (Alg. 2), using Eq. 25 with an optimal $T^{*}$ from Eq. 26 and $\rho=1$. For FLASK-SST^∗^, our first variant, BVP-augmented FLASK-SST^∗^, uses Eq. 29 to propagate robot dynamics in closed forms and takes advantage of our minimum-time local "flat" path in to check whether there is a direct connection from an existing node to the goal. Meanwhile, our second variant is a SIMD-only FLASK-SST^∗^ that keeps expanding the tree using vectorized collision checking via SIMD, *without* leveraging the BVP solutions.

<!-- chunk {"id": "body-0112", "role": "body", "section": "VII-A Kinodynamic planning for low-d o f systems", "weight": 1.0} -->

To highlight the "wandering" effect in propagation-based planners, our third variant disables best-state selection and tree pruning in SST\*, effectively leading to a DP-based FLASK-RRT, where dynamics propagation (DP) with a sampled control is used to extend the RRT tree. The resulting trajectories are simplified by skipping unnecessary local paths using Alg. 4. We compare our approach with three baseline planners: iDb-A\* \[ortizharo2025iDbAstar\], SST\* \[li2016sst\] from OMPL \[sucan2012the-open-motion-planning-library\], both without parallelized collision checking, and a GPU-based coarse-grained parallelized kinodynamic planner, Kino-PAX \[perrault2025kino\]. We maintain the aforementioned robot state and control constraints in our planners, enforced via our parallelized collision checking algorithm in Alg. 3, and in the baselines for a fair comparison.

<!-- chunk {"id": "body-0113", "role": "body", "section": "VII-A Kinodynamic planning for low-d o f systems", "weight": 1.0} -->

As each method has its own definition of trajectory costs, it is challenging to compare the quality of the trajectories. However, most cost functions describe a combination of trajectory duration, length, control efforts, and even velocity, acceleration, or higher-order terms, all of which intuitively and indirectly prioritize shorter trajectories. Therefore, we choose the trajectory length and planning time as common metrics for comparison, shown in Table I. For anytime planners such as iDb-A\* \[ortizharo2025iDbAstar\], SST\* \[li2016sst\], we report the time of the first solution and the length of the final solution within a $180$-second limit. Qualitatively, Fig. 5 plots the trajectories generated by our FLASK-RRTConnect (blue solid curves), our BVP-augmented FLASK-SST^∗^ (magenta solid curves), iDb-A\* (orange dashed curves), SST\* (green dotted curves), and Kino-PAX (dash-dotted purple curves).

<!-- chunk {"id": "body-0114", "role": "body", "section": "VII-A1 Comparison to the baselines", "weight": 1.0} -->

The baselines iDb-A\* and SST\* generate shorter trajectories but often take several seconds to plan, especially for complicated robot dynamics such as quadrotors. Kino-PAX \[perrault2025kino\] achieves planning times in the millisecond range by parallelizing the tree expansion *on GPUs* but returns much longer trajectories, possibly due to the "wandering" effect" from dynamics propagation with sampled suboptimal control. While it achieves similar planning times for simple dynamics such as unicycles, it is $\sim$`<!-- -->`{=html}8--300 times slower than our FLASK-RRTConnect for more complicated systems such as quadrotors. For all $3$ robot platforms, our FLASK-RRTConnect achieves significantly faster planning times than the baselines, in just a few milliseconds, offering the capability of real-time kinodynamic planning.

<!-- chunk {"id": "body-0115", "role": "body", "section": "VII-A1 Comparison to the baselines", "weight": 1.0} -->

Our BVP-augmented FLASK-SST^∗^ variant is slightly slower than our FLASK-RRTConnect since it is restricted to a constant control input for each local "flat" path instead of directly calculating a time-parameterized optimal control value. However, it is still significantly faster than the baselines in most cases. Meanwhile, our methods maintain comparable trajectory lengths, within 10--20% of the shortest length across the benchmarking problems. Intuitively, this is because the cost function prioritizes shorter trajectories, which leads to lower total control effort and trajectory time. While our generated trajectories can be further optimized by combining with other optimization-based motion planners, *e.g.*, as initial solutions, this is out of the scope of our paper and left for future work.

<!-- chunk {"id": "body-0116", "role": "body", "section": "VII-A1 Comparison to the baselines", "weight": 1.0} -->

Our kinodynamic FLASK-RRTConnect Geometric RRTConnect (VAMP) + TOPP-RA Total planning time (ms) ⊳Post./TOPP-RA time Final traj. length (rad) Total planning time (ms) ⊳Post./TOPP-RA time Final traj. length (rad) ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}1}$ ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}1}$ Total planning time (ms) ⊳Post./TOPP-RA time Final traj.

<!-- chunk {"id": "body-0117", "role": "body", "section": "VII-A1 Comparison to the baselines", "weight": 1.0} -->

length (rad) ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}1}$ ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}1}$ Total planning time (ms) ⊳Post./TOPP-RA time Final traj. length (rad) ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}1}$ ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}1}$ Total planning time (ms) ⊳Post./TOPP-RA time Final traj.

<!-- chunk {"id": "body-0118", "role": "body", "section": "VII-A1 Comparison to the baselines", "weight": 1.0} -->

length (rad) ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}1}$ Table under pick Total planning time (ms) ⊳Post./TOPP-RA time Final traj. length (rad) ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}1}$ ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}1}$ Total planning time (ms) ⊳Post./TOPP-RA time Final traj.

<!-- chunk {"id": "body-0119", "role": "body", "section": "VII-A1 Comparison to the baselines", "weight": 1.0} -->

length (rad) ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}1}$ ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}1}$ Total planning time (ms) ⊳ Post./TOPP-RA time Final traj. length (rad) ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}1}$ ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}1}$ TABLE II: Planning performance with a Franka Emika Panda robot over 100 runs of our FLASK-RRTConnect with different environments in MotionBenchMaker [chamzas2022-motion-bench-maker].

<!-- chunk {"id": "body-0120", "role": "body", "section": "VII-A1 Comparison to the baselines", "weight": 1.0} -->

For a baseline, we use a collision-free geometric path, provided by a SIMD-parallelized geometric RRTConnect [thomason2024vamp], followed by time parameterization (TOPP-RA [pham2018toppra]). Overall, our kinodynamic FLASK-RRTConnect generates a dynamically feasible trajectory faster than the baseline in almost all environments. Our trajectory is slightly longer but verified to be collision-free while the baseline’s trajectory is colliding in approximately 30% of the cases, due to the time parameterization. Better metrics are shown in bold, while the collision risk is marked as red if positive.

<!-- chunk {"id": "body-0121", "role": "body", "section": "VII-A1 Comparison to the baselines", "weight": 1.0} -->

(a) Tracking our trajectory (b) Tracking a geometric path Figure 7: Our trajectory is smoother and dynamically feasible, leading to better tracking performance. For example, the third joint angle q3 in the our UR5’s configuration stays close to the desired value from our trajectory (a) while there are overshoots and fluctuates with a geometric path [thomason2024vamp] (b), causing collision in Fig. 8(b). The tracking error ∥qactual − qdesired∥ also shows two overshooting peaks with the geometric path in Fig. 7(c).

<!-- chunk {"id": "body-0122", "role": "body", "section": "VII-A2 The roles of BVP solutions and parallelized collision checking", "weight": 1.0} -->

All of our planners in the experiments use parallelized collision checking but integrate the BVP solution at different levels: *(i)* our FLASK-RRTConnect uses the BVP solution to find all the local paths; *(ii)* our BVP-augmented FLASK-SST^∗^ only uses the BVP solution to find a shortcut to the goal; *(iii)* our SIMD-only FLASK-SST^∗^ only leverages the vectorized collision checking without using the BVP solution; and *(iv)* our DP-based FLASK-RRT simply expands the planning tree using dynamics propagation without best-state selection and pruning benefits from SST\*.

<!-- chunk {"id": "body-0123", "role": "body", "section": "VII-A2 The roles of BVP solutions and parallelized collision checking", "weight": 1.0} -->

Parallelized collision checking clearly improves the planning times. Compared to iDb-A\* \[ortizharo2025iDbAstar\] and the original SST\* \[li2016sst\], checking the local path for collision in parallel reduces the planning times from tens of seconds to a few seconds (see Table I) for robots with complicated dynamics such as quadrotors. This is the case even when the BVP solution is not used as in our SIMD-only FLASK-SST^∗^ or there is no best-state selection and tree pruning as in our DP-based FLASK-RRT. As propagation-based planners, our SIMD-only FLASK-SST^∗^ and DP-based FLASK-RRT still wander through the state space, a few small time steps at a time, causing longer planning times and trajectory lengths, as shown in Table I. This effect is even worse in DP-based FLASK-RRT as the best-state selection and pruning techniques used in SST\* are not available.

<!-- chunk {"id": "body-0124", "role": "body", "section": "VII-A2 The roles of BVP solutions and parallelized collision checking", "weight": 1.0} -->

However, our unique integration of BVP solutions and parallelized collision checking is the key to driving the planning times further down to the (sub-)millisecond range. By employing the BVP solution to find a shortcut from a node to the goal, our BVP-augmented FLASK-SST^∗^ generates a trajectory in just milliseconds, significantly faster than SIMD-only FLASK-SST^∗^. This illustrates the potential of our framework to improve existing propagation-based planners by addressing the common "wandering" effects via our BVP solution. Taking a further step, our FLASK-RRTConnect fully integrates the BVP solution to find all local paths during tree expansion, and therefore, leads to less than a millisecond of planning time in many cases. This illustrates our approach's ability to transform any existing sampling-based geometric planner into an ultrafast kinodynamic planner, requiring only widely available CPUs.

<!-- chunk {"id": "body-0125", "role": "body", "section": "VII-B Kinodynamic planning for high-d o f manipulators", "weight": 1.0} -->

In this section, we evaluate our algorithms with a simulated $7$-d o f Franka Emika Panda robot in PyBullet \[coumans2021pybullet\]. We consider $7$ realistic and challenging environments, including *bookshelf thin*, *bookshelf tall*, *bookshelf small*, *cage*, *box*, *table under pick* and *table pick*, from the MotionBenchMaker benchmark \[chamzas2022-motion-bench-maker\]. For each environment, $100$ motion planning problems with $100$ different pairs of start and goal configurations are generated for our experiments. The obstacles and the robot's geometries are represented by sets of spheres, which are compatible to simd parallelized collision checking as shown in \[thomason2024vamp\]. For each problem, the robot's task is to plan a dynamically feasible trajectory from a start to a goal configuration in the free space.

<!-- chunk {"id": "body-0126", "role": "body", "section": "VII-B Kinodynamic planning for high-d o f manipulators", "weight": 1.0} -->

In our experiments, we use our FLASK-RRTConnect planner, described in Sec. VII-A with trajectory simplification in Alg. 4. Our baseline is a common approach that generates a time-parameterized trajectory, *e.g.*, using TOPP-RA \[pham2018toppra\], from a collision-free geometric path, under kinematic constraints such as velocity and acceleration limits. The geometric path is provided by a simd-parallelized geometric RRTConnect planner from VAMP \[thomason2024vamp\]. For each environment, we use both our planner and the baseline to solve the pre-generated benchmarking problems and report the results in Table II. Our planner's total planning time is calculated as the sum of the RRTConnect time and trajectory simplification time. Meanwhile, the baseline's total planning time includes the RRTConnect time, path simplification time, and TOPP-RA time.

<!-- chunk {"id": "body-0127", "role": "body", "section": "VII-B Kinodynamic planning for high-d o f manipulators", "weight": 1.0} -->

As our trajectory and the baseline's are optimized for different cost functions, we use their length as a common metrics, similar to Sec. VII-A. As TOPP-RA \[pham2018toppra\] only fits a time-parameterized trajectory to geometric path, *i.e.*, a sequence of waypoints, it does not consider any collision avoidance constraints. While the geometric path is collision-free, there is no guarantee that the time-parameterized trajectory from TOPP-RA will be valid. Therefore, we sample the resulting trajectories, check for collision and compare the collision risk, measured by the percentage of collided trajectories.

<!-- chunk {"id": "body-0128", "role": "body", "section": "VII-B Kinodynamic planning for high-d o f manipulators", "weight": 1.0} -->

Table II compares our kinodynamic planner and the baseline, in terms of the total planning time, the final trajectory's length, and the collision risk, for each environment and overall. On average, we are able to generate a valid trajectory in around $3.5ms$, and in less than $1ms$ for $75\%$ of the problems, while the baseline's total planning time is consistently around $4.5ms$ for almost all problems. While VAMP can generate a collision-free geometric path fast, the baseline's total planning time is dominated by the TOPP-RA time. Our approach, instead, spends most of the time in the FLASK-RRTConnect planner, as we directly enforce the dynamics constraints in the RRT tree construction. Across all the problems, the baseline offers a shorter trajectory but, more importantly, poses a collision risk of $\sim 30\%$ on average, highlighting the benefit of our approach with guarantees of collision-free trajectories up to the sampling resolution.

<!-- chunk {"id": "body-0129", "role": "body", "section": "VII-B Kinodynamic planning for high-d o f manipulators", "weight": 1.0} -->

Fig. 6 visualizes the trajectories from our FLASK-RRTConnect (top) with no collisions and from the baseline (bottom) with collided configurations (red).

<!-- chunk {"id": "body-0130", "role": "body", "section": "VII-B Kinodynamic planning for high-d o f manipulators", "weight": 1.0} -->

For the *table under pick* and *table pick* environments, our total planning time is approximately $\sim 15$ times faster than that of the baseline, while maintaining $\sim 4$ times shorter time for the *box*, *bookshelf thin* and *bookshelf tall* environments. For the *bookshelf small* and *cage* environments, our approach is slightly slower on average. Yet, it is still $\sim 8$ times faster for $75\%$ of the *bookshelf small* problems, suggesting that there are certain challenging cases in those environments that our approach takes slightly longer than the baseline to plan, but still achieves milliseconds of planning time. We emphasize that even though the baseline can be faster in those cases, it still leads to a significant risk of collision, around $30\%$ of the *bookshelf small* and *cage* problems, as shown in Table II.

<!-- chunk {"id": "body-0131", "role": "body", "section": "VII-C Real experiments", "weight": 1.0} -->

Finally, we verify the benefit of our approach for online motion planning on a real Universal Robots (UR5) platform in a cluttered environment. The environment consists of multiple static and dynamic objects, perceived by an Intel Realsense camera with a top-down view. The depth image from the camera is used to generate a set of spheres stored in a collision-affording point tree (CAPT) compatible with simd-parallelized motion planning \[ramsey2024-capt\]. The spheres represent the obstacles in the environment in our Alg. 3. Our FLASK-RRTConnect planner in Sec. VII-A is used to find a trajectory from the start configuration to the goal.

<!-- chunk {"id": "body-0132", "role": "body", "section": "VII-C1 Kinodynamic Planning versus Geometric Planning", "weight": 1.0} -->

We first consider a "*pick and place*" scenario in Fig. 1, where the robot generates a motion plan from its start position to a *"pick"* position near a granola box, and then move to a *"place"* position above a basket. The environment is cluttered with multiple objects, creating narrow passages such that a minor deviation from the planned trajectory can cause collisions. Therefore, accurate tracking is crucial for the safe realization of this "*pick and place*" task. The baseline is a geometric path, generated by a SIMD-parallelized RRTConnect planner from VAMP \[thomason2024vamp\]. The path is sampled with a constant open-loop velocity, chosen such that the task's duration is similar to ours for a fair comparison. A closed-loop velocity control input is computed by Ruckig \[berscheid2021ruckig\] and sent to the UR5 robot to execute.

<!-- chunk {"id": "body-0133", "role": "body", "section": "VII-C1 Kinodynamic Planning versus Geometric Planning", "weight": 1.0} -->

Fig. 7 plots the tracking error during the experiments. Our trajectory is dynamically feasible, allowing the robot to smoothly and accurately execute the task without any collisions (Figs. 7(a) and 8(a) ‣ Fig. 8 ‣ VII-A1 Comparison to the baselines ‣ VII-A Kinodynamic planning for low-dof systems ‣ VII Evaluation ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")). Meanwhile, the geometric path has sharp turns, leading to overshoots and fluctuations (Fig. 7(b)). As a result, the robot collides with two nearby boxes while trying to turn, as seen in Fig. 8(b).

<!-- chunk {"id": "body-0134", "role": "body", "section": "VII-C1 Kinodynamic Planning versus Geometric Planning", "weight": 1.0} -->

The overshoots can be observed in Fig. 7(c) with two spikes in total tracking error $\|\mathbf{q}_{actual}-\mathbf{q}_{desired}\|$, at times $t\approx 4$s and $t\approx 9$s, where $\mathbf{q}_{actual}$ and $\mathbf{q}_{desired}$ denote the actual and desired values of the joint angles from the motion plans. Meanwhile, our tracking error stays low without any spikes, highlighting the benefits of having a dynamically feasible trajectory from our kinodynamic planner for accurate task executions.

<!-- chunk {"id": "body-0135", "role": "body", "section": "VII-C2 Reactive Kinodynamic Planning", "weight": 1.0} -->

To examine the reactiveness of our kinodynamic planning approach, we consider a "*pick, place, and reset*" loop, where the robot keeps planning its trajectory to perform a "*pick*" action near a pile of blocks, a "*place*" action above the basket, and then "*reset*" to its original configuration. During the experiment, we move a foam obstacle in the environment and verify that our kinodynamic motion planner is able to quickly react to object changes and safely achieve the task as shown in Fig. 9. On average, our kinodynamic planner takes $\sim 90\mu s$ to plan and $\sim 40\mu s$ to simplify the trajectory (Fig. 10), leading to a total planning time of $0.13ms$. The results illustrate that our approach is fast and suitable for online and reactive planning with dynamic environments, while satisfying the dynamics constraints.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Conclusions", "weight": 1.0} -->

This paper develops FLASK, an ultrafast sampling-based kinodynamic planning framework, by solving the two-point boundary value problem and dynamics propagation in closed forms for a common class of differentially flat robot platforms, and performing extremely fast forward kinematics and collision checking via simd parallelism, available on most consumer CPUs. Our approach is exact, general and can be applied to any sampling-based planners while offering theoretical guarantees on probabilistic exhaustivity and asymptotic optimality. It is able to generate a dynamically feasible trajectory in the range of microseconds to milliseconds, which is suitable for online and reactive planning in dynamic environments. Our method outperforms common sampling-based and optimization-based kinodynamic planners as well as time-parameterization of a geometric path in terms of planning times, offering a fast, reliable, and feasible solution for trajectory generation.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Our approach unfolds a promising and exciting research area where it is possible to transform existing sampling-based motion planners with theoretical guarantees into fast kinodynamic versions while only requiring general-purpose and widely available CPUs. As we have closed-form BVP solutions for a large class of nonlinear differentially flat systems, we can largely bypass the propagation-based planners and can even enable kinodynamic planning in challenging settings, e.g., with graph-based planners. This ability potentially can lead to a wide application of our method on different robots, in different settings, and for various tasks. Our method can quickly bootstrap optimization-based planners with quality and dynamically feasible initial solutions, especially when their objective function differs from our cost. Moreover, the ability to specify a duration for our trajectory offers an exciting potential integration task and motion planning with temporal constraints such as task deadlines.
