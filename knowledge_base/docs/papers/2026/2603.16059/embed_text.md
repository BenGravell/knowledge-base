## Introduction

Motion planning is critical for safe and accurate robot operation in many applications, *e.g.*, transportation \[claussmann2020review\], environment monitoring \[honig2018trajectory, zhou2022swarm\], warehouses \[eppner2016lessons\], healthcare \[riek2017healthcare\], and home assistance \[jenamani2025feast\]. In such applications, the robot has to react quickly to changes in its environment, promptly (re)plan a collision-free trajectory, and safely track the trajectory to reach a goal state, using a controller. This task requires fast motion planning, subject to both collision avoidance and robot dynamics constraints, to generate a dynamically feasible trajectory from a start to a goal that the robot is able to follow. While recent advances have significantly reduced motion planning times for geometric planning via parallelization techniques \[thomason2024vamp, ramsey2024-capt\], sampling-based motion planning under dynamics constraints, *i.e.*, kinodynamic planning, remains a challenge for real-time applications especially for high degree-of-freedom (d o f) robots such as manipulators. In this paper, we address this problem by leveraging the *differential flatness* property of many common robot systems, such as ground and aerial vehicles, manipulators, and more, to enable ultrafast sampling-based kinodynamic motion planning via parallelization techniques.

(a) Tracking our trajectory

(b) Tracking a geometric path

Figure 1: Motion planning for a “pick and place” task in a cluttered environment: a dynamically feasible trajectory (a) generated from our FLASK framework can be accurately tracked by a UR5 robot. Meanwhile, tracking a geometric path (b) leads to collisions (shown in red) that topple the nearby boxes. Multiple intermediate states are overlaid to illustrate the robot’s motion. Our planning framework is real-time and generates trajectories in ∼ 90 μ s by leveraging differential flatness and “single instruction, multiple data” (simd) parallelism.

Kinodynamic planning \[lavalle2001randomized, hsu2022randomizekinodynamic, lavalle2006planning\] generates dynamically feasible trajectories by directly enforcing dynamics constraints in the planner. Without such constraints, controllers often struggle to accurately track motion plans, especially with high-speed maneuvers, potentially leading to unsafe behavior. Optimization-based approaches, *e.g.*, \[augugliaro2012generation, schulman2014trajopt, bonalli2019gusto, tassa2012synthesis, Mastalli2020Crocoddyl, ortizharo2025iDbAstar\], formulate kinodynamic planning as a nonlinear optimization problem and solve for the solution by minimizing a trajectory cost subject to constraints such as collision avoidance, robot dynamics, and joint angle and velocity limits. While these approaches can work well in high-dimensional state spaces, they are often susceptible to local minima and are sensitive to initial solutions. Meanwhile, search-based approaches, *e.g.*, \[pivtoraiko2005efficient, pivtoraiko2011kinodynamic, cohen2010search, liu2017search, ajanovic2018searchbased\], build a graph in the state space on a grid or lattice and search for a sequence of motion primitives that connects the start and the goal. Search-based methods provide optimality guarantees but suffer from the curse of dimensionality, thus requiring complex heuristics or domain knowledge to guide the search. On the other hand, sampling-based approaches randomly sample to expand from the start to the goal, constructing a tree \[lavalle2001randomized, webb2013kinodynamicRRT, karaman2010kinorrt, hauser2016aorrt, li2016sst, verginis2023kdf\] or sometimes a graph for simple systems \[vandenberg2007kinoroadmap\].

A key challenge in enforcing dynamics constraints in sampling-based planning is to solve challenging two-point boundary value problems (BVPs) for dynamically feasible *local paths* between robot states. Many planners \[lavalle2001randomized, hsu2022randomizekinodynamic, li2016sst\] avoid this by instead sampling an often sub-optimal control input and then propagating the dynamics forward using numerical integration \[butcher2016numerical\]. Dynamic propagation with randomly sampled control often causes the planner to "wander" to irrelevant parts of the state space and might lead to longer paths and longer planning times. Other works solve the BVP problem for simple systems \[karaman2010kinorrt\] and linearized robot dynamics \[webb2013kinodynamicRRT, Perez2012LQRRRT\], or approximate the solution using a neural network \[wolfslag2018rrt, chiang2019rl, zheng2021sampling\]. Instead, we obtain an *exact analytical solution* of the BVP, thanks to the *differential flatness* of many robot platforms such as mobile robots and manipulators \[murray1995differential, mellinger2011minimumsnap\].

Differential flatness \[murray1995differential\] is a powerful system property that, similar to feedback linearization \[khalil2002nonlinear\], simplifies motion planning and control designs by converting the nonlinear robot dynamics to an equivalent linear system. For differentially flat systems, the robot states and control inputs can be described by a set of carefully chosen flat outputs and their derivatives (see Def. 1. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness") for more details). A trajectory in the flat output space can be converted to a dynamically feasible trajectory in the robot's original state space, allowing us to simplify motion planning problems via a change of variables. This technique has been used mainly to plan trajectories for mobile robots, most notably quadrotors \[mellinger2011minimumsnap, mellinger2012_trajgen, liu2017search\]. However, the planning time is still hindered by computationally expensive subroutines such as forward kinematics and collision checking, which are particularly worse with high-d o f robots such as manipulators.

Recently, advances in parallelization \[sundaralingam2023curobo, thomason2024vamp\] have improved planning time to the range of microseconds and milliseconds. However, these works focus on either geometric \[thomason2024vamp\] or kinematic \[sundaralingam2023curobo\] planning problems. One family of these techniques uses "fine-grained" parallelism via "single instruction, multiple data" (simd) instructions, available on consumer CPUs, to perform collision checking on multiple samples at the same time \[thomason2024vamp, ramsey2024-capt\]. However, directly enforcing dynamics constraints in parallel is non-trivial, as it requires sampling a trajectory at different time steps in advance while obeying robot dynamics. We address this problem by transforming the kinodynamic planning problem from the original state space to a flat output space, where closed-form *local paths* are time-parameterized polynomials and hence, amenable to simd parallelization for fast collision checking. The resulting flat output trajectory is converted to a dynamically feasible collision-free trajectory in the original state space for the robot to execute. Our approach is fast, exact and general for most sampling-based planners.

In summary, we develop FLASK ^11^1The code will be made publicly available., a "Differential Flatness-based Accelerated Sampling-based Kinodynamic Planning" framework that:

generates dynamically feasible trajectories in the range of milliseconds for nonlinear differentially-flat robot systems, such as manipulators, and mobile robots,

constructs a planning tree or graph by solving the boundary value problem or dynamics propagation for continuous closed-form trajectories in the flat output space,

performs fast collision checking of the closed-form trajectories using fine-grained simd parallelism.

We provide a theoretical analysis on our approach's probabilistic exhausitivity, a concept stronger than completeness introduced in \[schmerling2015optimal_driftless, kavraki1998analysis\], and optimality guarantees. We extensively verify our approach with challenging motion planning problems on low- and high-d o f, fully- and under-actuated robot systems in both simulated and real experiments. FLASK is shown to achieve planning times of merely a few milliseconds, even on high-d o f robot platforms in cluttered environments, while respecting dynamics constraints by design. Our framework is general and can be integrated in the context of many common sampling-based motion planners, such as RRT-Connect \[kuffner2000rrtconnect\], SST\* \[li2016sst\] and others, effectively turning geometric planners into kinodynamic planners with theoretical guarantees.

## Related Work

### II-A Motion Planning with Dynamics Constraints

Kinodynamic motion planning \[schmerling2019kinodynamic\], *i.e.*, motion planning under dynamics constraints, is a challenging task where the robot plans a dynamically feasible trajectory from a start, *e.g.*, a robot state, containing its joint angles and derivatives, to a goal region while satisfying the robot dynamics and avoiding collision with obstacles in the environment. There are three main approaches: optimization-based, search-based, and sampling-based kinodynamic planning.

*Optimization-based kinodynamic planning*, such as TrajOpt \[schulman2014trajopt\], GuSTO \[bonalli2019gusto\], and Crocoddyl \[Mastalli2020Crocoddyl\], generates robot trajectories by formulating and solving an optimization problem, subject to dynamics and collision-avoidance constraints, with an objective function measuring the cost of the trajectory. This optimization problem is often nonlinear and can be solved via sequential convex programming \[augugliaro2012generation, schulman2014trajopt, chen2015decoupled, bonalli2019gusto\], iterative linear quadratic regulators \[tassa2012synthesis\], differential dynamic programming \[Howell2019Altro, Mastalli2020Crocoddyl\], augmented Lagrangian methods \[toussaint2017tutorial\], or general solvers \[l2022whole, beck2025vitro\]. In general, optimization-based trajectory planners provide smooth trajectories, but often get stuck in a local minimum and require good initialization. While trajectory optimization with a graph of convex sets \[marcucci2023motion, vonwrangel2024gcs, graesdal2024_contactplanning\] can avoid local minima, it requires expensive precomputation of the graph in the state space.

*Search-based kinodynamic planning* \[pivtoraiko2005efficient, pivtoraiko2011kinodynamic, cohen2010search, liu2017search, ajanovic2018searchbased, mishani2025srmp\] instead constructs a graph, often on a predefined grid or lattice, where each edge is chosen from a precomputed, discrete set of motion primitives, generated by propagating the robot dynamics for a short period of time under a set of control inputs. A motion primitive is valid if it does not collide with an obstacle. A search algorithm, such as $A^{\ast}$ \[hart1968formal\], can be used to find the shortest path on the graph, providing a trajectory as a sequence of motion primitives connecting the start with the goal. A major challenge of search-based approaches is the need to precompute dynamics propagation, where a numerical approximation with fine lattice resolution is required for high accuracy. They also suffer from the curse of dimensionality and require a good heuristic to guide the search.

*Sampling-based kinodynamic planning* \[orthey2024-review-sampling, webb2013kinodynamicRRT, karaman2010kinorrt, lavalle2001randomized, hsu2022randomizekinodynamic, hauser2016aorrt, li2016sst, verginis2023kdf\] uses sampling to discretize the high-dimensional state space and build a tree (or, less often, a graph for simple systems such as car-like robots \[vandenberg2007kinoroadmap\]), growing from the start towards the goal region. To find a feasible trajectory connecting two samples, a difficult *two-point boundary value problem* (BVP) has to be solved \[lavalle2006planning\], posing a major challenge for sampling-based kinodynamic planning. A common approach to avoid solving a BVP problem for tree expansion is to sample the control input space, and propagate the robot dynamics, *e.g.*, using a numerical integrator \[lavalle2001randomized, hsu2022randomizekinodynamic, li2016sst\] or physics-based models \[gao2025parallel\], for a short period of time, with asymptotic optimality guarantees analyzed in \[li2016sst\]. Other approaches only solve the BVP problem for simple robot dynamics with low-dimensional state space \[karaman2010kinorrt, webb2013kinodynamicRRT\], or linearized dynamics \[webb2013kinodynamicRRT, Perez2012LQRRRT\]. Meanwhile, learning-based kinodynamic motion planning uses neural networks to approximate the control input and the steering cost of expanding the tree towards a new node \[wolfslag2018rrt, chiang2019rl, zheng2021sampling, ichter2019latentspacemp, li2021mpc-mpnet\].

BVPs and dynamics propagation cause major computational bottlenecks for kinodynamic planning. While BVPs can be analytically solved for linear or simple systems \[webb2013kinodynamicRRT, Perez2012LQRRRT\], this is not true in general for most nonlinear systems and it is computationally expensive to obtain an approximate solution. Kinodynamic RRT^∗^ \[webb2013kinodynamicRRT, Perez2012LQRRRT\] linearizes the dynamics around an operating point and demonstrates that BVPs can be solved in closed form for certain robots, *e.g.*, quadrotors around a hovering position. However, the approximated solution only works well around the operating point, limiting aggressive maneuvers. To avoid solving difficult BVPs, most existing kinodynamic planners \[li2016sst\] resort to dynamics propagation, where a constant value of the control is sampled instead. A numerical integrator such as Euler's or Runge-Kutta methods \[butcher2016numerical\] is then used to sequentially calculate the next robot state over multiple small time steps to maintain high accuracy. Typically, the sampled control is suboptimal, and therefore, causes the planner to wander in the state space before reaching the goal. Existing planners often mitigate this "wandering" effect via best-state selection and tree pruning \[li2016sst\], but still require long planning times to find a dynamically feasible trajectory.

Optimization-based, search-based and sampling-based approaches can be combined to improve trajectory generation \[ortizharo2024iDbRRT, ortizharo2025iDbAstar, natarajan2024pinsat, natarajan2023torque, natarajan2021interleaving, sakcak2019sampling, shome2021asymptotically, kamat2022bitkomo, choudhury2016regionally, alwala2021joint\]. For example, a path or trajectory from sampling-based or search-based planners can be used as an initial solution for optimization-based ones \[ortizharo2024iDbRRT, ortizharo2025iDbAstar\]. INSAT planners \[natarajan2024pinsat, natarajan2023torque, natarajan2021interleaving\] interleave between search-based planning on a low-dimensional subspace and optimization-based planning on the full-dimensional space to improve planning times and success rates. Meanwhile, a library of precomputed motion primitives from search-based planning can be sampled to expand the planning tree in sampling-based motion planning \[sakcak2019sampling, shome2021asymptotically\]. Furthermore, optimized local paths can be used to generate collision-free edges and bias the sampling regions in a sampling-based planner \[kamat2022bitkomo, choudhury2016regionally\]. Another approach is to fit a geometric path with a time-parameterized trajectory using trajectory optimization such as TOPP-RA \[pham2018toppra\] or Ruckig \[berscheid2021ruckig\], typically without considering collision avoidance constraints.

Our method performs fast sampling-based kinodynamic planning by leveraging simd parallelism (Sec. II-B) and the differential flatness of the dynamics of common robot platforms \[allen2019real, liu2017search, bascetta2017flat, welde2021dynamically\] to directly tackle the BVP problems. A system is called *differentially flat* if there exist variables, called flat outputs, whose values and derivatives dictate the robot state and control inputs (see Def. 1. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness") for details). This approach has been applied to sampling-based \[bascetta2017flat, ye2022efficient, wang2024differential, seemann2014exact\], search-based \[liu2017search\], and optimization-based motion planning \[mellinger2011minimumsnap, welde2021dynamically, han2023efficient, hao2005differential, beaver2024optimal\], but primarily for low-dimensional robot platforms (often with simple geometry shapes such as spheres or boxes for collision checking), *e.g.*, quadrotors \[mellinger2011minimumsnap\], unicycles and 2-link arms \[beaver2024optimal\], or for a specific system, *e.g.*, gantry cranes \[vu2022sampling\]. Instead, we integrate differential flatness with sampling-based kinodynamic planning for generic high-d o f robots, where forward kinematics and collision checking are complex and time-consuming besides enforcing dynamics constraints. While most existing methods approximate a solution to the BVP problems, differential flatness allows us to obtain a closed-form fixed- or minimum-time polynomial BVP solution. Such closed-form trajectories are amenable to parallelized collision checking using *fine-grained* parallelization based on simd instructions (Sec. II-B), enabling trajectory generation in microseconds to milliseconds. It is also important to note that existing flatness-based sampling-based planners either do not prove completeness and optimality or loosely mention the existing guarantees of geometric planners, *e.g.*, those of RRT\* \[bascetta2017flat, vu2022sampling, wang2024differential, seemann2014exact, ye2022efficient\]. Achieving such theoretical guarantees with closed-form BVP solutions is nontrivial as it requires careful consideration of nonlinear local paths rather than linear edges on the graph. We address this by offering a theoretical analysis of probabilistic exhaustivity, which is stronger than completeness, and asymptotic optimality of our approach in Sec. VI.

### II-B Hardware-accelerated Motion Planning

Motion planning can be time-consuming as it relies on multiple computationally expensive subroutines, such as forward kinematics (fk), collision checking (cc) and nearest neighbor (nn) search. With recent advances in parallel computing, much progress has been made to improve these subroutines and enhance planning performances via both *coarse-grained* and *fine-grained* parallelization.

*Coarse-grained* parallelization techniques typically run multiple subroutines or even multiple instances of the planners at the thread or process levels. Early work focuses on improving motion plans by merging and averaging out the paths from different instances of the planners \[raveh2011little\], or by adapting existing planners to run their subroutines in parallel \[amato1999probabilistic, ichnowski2012parallel\]. Parallelized motion planning can also be achieved by partitioning the configuration space \[jacobs2012scalable, werner2025gcs\] or the planning tree construction \[plaku2005sampling, vu2022sampling, perrault2025kino\]. Closely related to our work, \[vu2022sampling\] also employs differential flatness to generate dynamically feasible trajectories, however, by coarsely growing multiple planning subtrees in parallel for a specific gantry crane system. Recently, the prevalence of GPUs enables impressive improvements in motion planning \[bhardwaj2022storm, sundaralingam2023curobo, fishman2023motion, le2025global, le2025model\] but suffers from costly GPU resources and communication overhead between CPUs and GPUs. GPU-based planning methods often grow a planning tree in parallel by propagating the robot dynamics, *e.g.*, Kino-PAX \[perrault2025kino\], or via approximate dynamic programming recursion, *e.g.*, GMT\* \[ichter2017gmt\], and are shown to generate a robot trajectory in milliseconds for low-d o f systems with simple forward kinematics. For high-d o f robots, cuRobo \[sundaralingam2023curobo\] generates geometric paths as seeds for a parallelized trajectory optimization solver under kinematics constraints such as velocity, acceleration and jerk limits.

*Fine-grained* parallelization techniques focus on parallelizing primitive operations in a motion planning algorithm, *e.g.*, via "single instruction/multiple data" (simd) instructions on consumer-grade CPUs. This has been shown to provide extremely fast geometric motion planning subject to collision avoidance constraints, with planning times ranging from microseconds to milliseconds \[thomason2024vamp, ramsey2024-capt, wilson2024nearest\]. To check an edge (a line segment) for collision, VAMP \[thomason2024vamp\] uses simd instructions to efficiently perform parallelized forward kinematics and collision checking on multiple configurations, generated via linear interpolation. While this approach is promising, it is challenging to enforce additional requirements via parallelized primitive operations such as dynamics and non-holonomic constraints. Particularly, enforcing nonlinear dynamics constraints with fine-grained parallelism is non-trivial due to the intractability of BVP problems, as mentioned in Sec. II-A. We instead leverage the differential flatness property to obtain time-parameterized solutions that can be discretized at arbitrary times and hence, amenable to SIMD-based primitive operations. Our deliberate fusion of differential flatness and SIMD parallelism effectively brings the benefits of "fine-grained" parallelized forward kinematics and collision checking to kinodynamic planning. Thanks to the closed-form BVP solution in the flat output space, we will later show that our approach achieves planning times of merely a few milliseconds.

## Problem Formulation

Consider a robot with state $\mathbf{x} \in \mathcal{X}$ and control $\mathbf{u} \in \mathcal{U}$. For example, the state of a manipulator can include the joint configuration $\mathbf{q}$ and possibly its derivatives, while the control input can be the torques being applied on the robot joints. Let $\mathcal{X}_{free}$ and $\mathcal{X}_{obs} = {\mathcal{X} \smallsetminus \mathcal{X}_{free}}$ be the free and occupied spaces, respectively, which can be generated from robot constraints such as collision avoidance or joints limits. The robot motion is governed by a nonlinear dynamics function $\mathbf{f}$ of the state $\mathbf{x}$ and the control $\mathbf{u}$ as follows:

A time-parameterized trajectory ${\mathbf{σ}}:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{X}}$ for time $t \in {\lbrack 0,1\rbrack}$ is called dynamically feasible if there exists a time-parameterized control input $\mathbf{u}:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{U}}$ such that the robot dynamics is satisfied by the trajectory:

Given an initial robot state $\mathbf{x}_{s}$ and a goal region $\mathcal{G} \subset \mathcal{X}$, as a subset of $\mathcal{X}$, the kinodynamic motion planning problem aims to find a dynamically feasible trajectory ${\mathbf{σ}}{(t)}$ with control input $\mathbf{u}{(t)}$, connecting the initial state $\mathbf{x}_{s}$ to the goal region $\mathcal{G}$ in the free space $\mathcal{X}_{free}$ as described in Problem 1. The goal region $\mathcal{G}$ commonly represents a desired state or a region that a goal state can be sampled from.

### Problem 1

Given an initial robot state $\mathbf{x}_{s}$ and a goal region $\mathcal{G} \subset \mathcal{X}$, find a control input $\mathbf{u}{(t)}$ that generates a dynamically feasible trajectory ${\mathbf{σ}}{(t)}$ such that:

In the remainder of the paper, we solve Problem 1 by developing FLASK, a parallelized kinodynamic motion planning framework for differential flat robot systems, including common platforms such as ground and aerial vehicles, and manipulators. Our approach offers ultrafast planning time and exact dynamically feasible trajectory solution without the need to approximate the robot dynamics. Occasionally, we will drop the notation of time dependence for readability.

## Preliminaries

In this section, we provide a brief review and necessary background on sampling-based kinodynamic planning, differential flatness and fine-grained parallelization that will be useful for the derivation of our approach in Sec. V.

### IV-A Sampling-based Kinodynamic Motion Planning

Most sampling-based geometric planners, such as RRT-connect \[kuffner2000rrtconnect\] and PRM \[kavraki2002probabilistic\] consider the robot configuration $\mathbf{q}$ as the state $\mathbf{x}$ and approximate the robot's configuration space with a tree or graph $\mathbb{G}$ with a set of nodes $\mathbb{V}$ and a set of edges $\mathbb{E}$. Though individual sampling-based planners differ wildly in their exact approach, they all have roughly the same structure for their main search loop. At each iteration, such planners attempt to add a new sample $\mathbf{x}_{f}$ to $\mathbb{V}$, then connect $\mathbf{x}_{f}$ to some existing $\mathbf{x}_{0} \in {\mathbb{V}}$, and if successful, add the resulting edge to $\mathbb{E}$. This is called a Connect or Extend subroutine. To construct edges, all geometric sampling-based planners require a *local planner* to produce a local path between configurations.

However, in kinodynamic motion planning, where robots are subjected to dynamics constraints, finding a local path $\mathbf{x}_{loc}{(t)}$ to reach $\mathbf{x}_{f}$ with control input $\mathbf{u}_{loc}{(t)}$ in duration $T$, requires solving a *boundary value problem* (BVP), subject to the robot dynamics with initial state $\mathbf{x}_{0}$ and terminal state $\mathbf{x}_{f}$ as follows:

Solving the BVP in practice is often computationally intractable, so most kinodynamic planners (*e.g.*, \[lavalle2001randomized, hsu2022randomizekinodynamic, li2016sst\]) instead take a propagation-based approach: they integrate a sampled control input $\mathbf{u}_{0}$ from a reachable state for a short time $T$ to generate a new state $\mathbf{x}_{f}$ rather than connecting sampled states. In this case, the local path $\mathbf{x}_{loc}{(t)}$ and the new state $\mathbf{x}_{f}$ are defined as:

### IV-B Differential Flatness

### Definition 1 (Differential Flatness)

A dynamical system is called "*differentially flat*" \[murray1995differential\] if there exists an $n$-dimensional output:

such that the robot state $\mathbf{x}$ and control input $\mathbf{u}$ can be described in terms of the output $\mathbf{y}$ and its derivatives $\mathbf{y}^{( \cdot )}$:

for non-negative derivative orders $k,l$ and $m$. The output $\mathbf{y}$ must be differentially independent, *i.e.*, there does not exist any differential relationship among the components of $\mathbf{y}$. The exact form of the functions $\mathbf{α}$ and $\mathbf{β}$ depends on the robot system, several of which can be found in \[murray1995differential, mellinger2011minimumsnap\].

We provide three common examples of differentially flat fully-actuated and under-actuated robot platforms, as follows.

### Example 1

Consider a *fully-actuated manipulator* with joint angles $\mathbf{q}$, and control input $\mathbf{u}$, *e.g.*, the joint torques. This is typically the case for common manipulators such as Franka or KUKA platforms. The robot dynamics is described by the Euler-Lagrange equation of motions:

where the control gain matrix $\mathbf{B}{(\mathbf{q})}$ is typically invertible, *i.e.*, the system is fully actuated. The robot dynamics can be expressed in the form of Eq. with the robot state $\mathbf{x} = {(\mathbf{q},\overset{˙}{\mathbf{q}})}$. For this system, the flat output is the same as the configuration: $\mathbf{y} = \mathbf{q}$. The state $\mathbf{x}$ and the control input $\mathbf{u}$ can be derived from the flat output $\mathbf{y}$ as follows,

As the control gain $\mathbf{B}{(\mathbf{q})}$ is invertible, the control input $\mathbf{u}$ in is guaranteed to exist.

### Example 2

Consider a *unicyle* robot whose state $\mathbf{x}$ is defined as $\mathbf{x} = {(x,y,\theta)}$ where $(x,y)$ is the position and $\theta$ is the heading angle of the vehicle. The control input $\mathbf{u} = {(v,\omega)}$ includes the speed $v$ and angular velocity $\omega$. The flat output $\mathbf{y}$ is defined as the position: $\mathbf{y} = {(x,y)}$. The yaw angle $\theta$ and the control input $\mathbf{u}$ can be determined from $\mathbf{y}$ as follows:

where $\kappa \in {\{ 0,1\}}$ depends on whether the vehicle is moving forward or backward, respectively.

### Example 3

Consider an *under-actuated quadrotor* whose state $\mathbf{x}$ is defined as $\mathbf{x} = {(\mathbf{p},\mathbf{R},\mathbf{v},{\mathbf{ω}})}$, where $\mathbf{p} = {(x,y,z)} \in {\mathbb{R}}^{3}$ is the position of the center of mass, $\mathbf{R} \in {SO{}}$ is the rotation matrix, $\mathbf{v}$ is the linear velocity, and $\mathbf{ω}$ is the angular velocity. The control input $\mathbf{u} = {(f,{\mathbf{τ}})}$ consists of a thrust $f \in {\mathbb{R}}_{\geq 0}$ and a torque ${\mathbf{τ}} \in {\mathbb{R}}^{3}$, generated from the motors. The flat output for quadrotor systems is $\mathbf{y} = {(\mathbf{p},\psi)} \in {\mathbb{R}}^{4}$, where $\psi$ is the yaw angle of the robot \[mellinger2011minimumsnap\].

The state $\mathbf{x} = {{\mathbf{α}}{(\mathbf{p},\overset{˙}{\mathbf{p}},\overset{¨}{\mathbf{p}},\mathbf{p}^{},\psi,\overset{˙}{\psi})}}$ can be expressed in terms of the flat outputs and their derivatives as follows. Clearly, the position $\mathbf{p}$ is already part of the flat output $\mathbf{y}$, and hence the linear velocity is calculated as $\mathbf{v} = \overset{˙}{\mathbf{p}}$. Let $m$ and $\mathbf{J}$ be the mass and inertia matrix of the quadrotor, respectively. Let $\mathbf{t} = {m{({\overset{¨}{\mathbf{p}} + {g\mathbf{e}_{z}}})}}$ be the thrust vector applied on the quadrotor's center of mass, which coincides with the $z -$axis of the body frame where $g$ is the gravitational acceleration, and $\mathbf{e}_{z} = \begin{bmatrix}
\end{bmatrix}^{\top}$ is the $z -$axis unit vector in the world frame. The rotation matrix $\mathbf{R} = \begin{bmatrix}
\mathbf{r}_{x} & \mathbf{r}_{y} & \mathbf{r}_{z}
\end{bmatrix}$ can be calculated as:

where $\mathbf{r}_{\psi} = {\lbrack{- {\sin\psi}},{\cos\psi},0\rbrack}$. The derivative of the rotation matrix is $\overset{˙}{\mathbf{R}} = \begin{bmatrix}
{\overset{˙}{\mathbf{r}}}_{x} & {\overset{˙}{\mathbf{r}}}_{y} & {\overset{˙}{\mathbf{r}}}_{z}
\end{bmatrix}$ with:

The angular velocity $\mathbf{ω}$ is calculated as: ${\mathbf{ω}} = {({\mathbf{R}^{\top}\overset{˙}{\mathbf{R}}})}^{\vee}$, where the ${( \cdot )}^{\vee}$ operator maps a skew-symmetric vector $\hat{\mathbf{ω}} \in {{\mathfrak{s}}{\mathfrak{o}}{}}$ to a vector ${\mathbf{ω}} \in {\mathbb{R}}^{3}$. Meanwhile, the control input $\mathbf{u} = {{\mathbf{β}}{(\mathbf{p},\overset{˙}{\mathbf{p}},\overset{¨}{\mathbf{p}},\mathbf{p}^{},\mathbf{p}^{},\psi,\overset{˙}{\psi},\overset{¨}{\psi})}}$ is described as:

We refer the readers to \[mellinger2011minimumsnap, zhou2014vectorfield, liu2018search\] for the detailed derivation.

(a) Samples from a linear path [thomason2024vamp].

(b) Samples from a nonlinear local path xl o c (t).

Figure 2: Configuration samples a, b, c and d, discretized from a linear path (a), as in VAMP [thomason2024vamp], and from our closed-form time-parameterized motions (b), can be efficiently checked for collision using simd parallelism.

### IV-C CPU fine-grained parallelism

Fine-grained parallelization techniques such as "single instruction, multiple data" (simd) are ubiquitous on consumer CPUs and have recently shown significant improvement in sampling-based geometric motion planning by performing forward kinematics and collision checking on multiple configurations in parallel. Vectorization via simd allows simultaneously applying the same primitive operations on multiple variables. VAMP \[thomason2024vamp\], a simd-accelerated planning method, uses this technique to perform parallelized collision checking of multiple robot configurations, evenly sampled along a line segment (Fig. 2(a)) connecting two nodes on a planning tree or graph. Given the set of configurations, the robot's geometric shape, described by a set of SIMD-compatible shapes such as capsules or spheres in the workspace, is calculated via branchless forward kinematics and checked for collision against the obstacle geometry.

simd-based collision checking requires access to all the states along a local path, typically through an analytical form of the motion. However, under dynamics constraints, the nonlinear local path $\mathbf{x}_{loc}{(t)}$ that solves the BVP problem (Sec. IV-A) is computationally intractable, prohibiting configuration sampling at multiple arbitrary times in advance. In the next section, we address this problem by deriving a closed-form time-parameterized local path $\mathbf{x}_{loc}{(t)}$ based on the differential flatness property and sampling multiple states at different times, as illustrated in Fig. 2(b).

## Technical Approach

In this section, we present our kinodynamic planning framework, FLASK, by showing that the flat output evolves as a linear system (Sec. V-A), and hence, allows us to convert Problem 1 from the original state space $\mathcal{X}$ to a flat state space (Problem 2 in Sec. V-B). In the flat state space, we develop primitive subroutines, FlaskExtend for planning graph construction in Sec. V-C and FlaskCC for parallelized forward kinematics and collision checking in Sec. V-D, that work with any sampling-based planning method. These subroutines are the core of our framework in Alg. 1, which effectively turns any geometric motion planner into a kinodynamic version. As a result, instead of being tied to a specific planner, our general framework gives rise to a new class of ultrafast kinodynamic planners for a broad class of differentially flat robot systems. Finally, we discuss trajectory postprocessing in our approach in Sec. V-E.

### V-A Flat Output Dynamics as a Linear System

Consider the $n$-dimensional flat output $\mathbf{y}$ in Def. 1. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness"), that can be used to recover the state $\mathbf{x}$ and control input $\mathbf{u}$ via Eq. (7. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")). Let $\mathbf{w} \in \mathcal{W} \subset {\mathbb{R}}^{n}$ be a pseudo-control input, defined as the $r$th derivative of the output $\mathbf{y}$:

where the derivative orders $l,m$ are defined in Eq. 7. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness"). Let $\mathbf{z} \in \mathcal{Z} \subset {\mathbb{R}}^{rn}$ be the flat state, defined as:

The state $\mathbf{z}$ satisfies linear dynamics with the pseudo-control input $\mathbf{w}$ as follows:

with $\mathbf{A} \in {\mathbb{R}}^{{{rn} \times r}n}$, $\mathbf{B} \in {\mathbb{R}}^{{rn} \times n}$, and the identity matrix $\mathbf{I}_{n} \in {\mathbb{R}}^{n \times n}$. Instead of enforcing the nonlinear dynamics constraint in a motion planning problem, we can implicitly enforce a much simpler linear dynamics in the flat state space via the conversion (7. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")). Note that the matrix $\mathbf{A}$ is nilpotent with index $r$, *i.e.*, $\mathbf{A}^{r} = 0$.

### V-B Sampling-based Kinodynamic Planning in Flat State Space

Due to the non-linearity of the robot dynamics, it is challenging to plan robot motions in the original state space $\mathcal{X}$, as most sampling-based motion planning algorithms require a challenging Extend subroutine that either solves a boundary value problem to connect two states $\mathbf{x}_{0}$ and $\mathbf{x}_{f}$ or propagates the dynamics to predict the next state $\mathbf{x}_{f}$ given a constant control input $\mathbf{u}_{0}$. As shown in Sec. V-A, the flat state $\mathbf{z}$ satisfies a linear dynamics in with a nilpotent matrix $\mathbf{A}$, potentially leading to much simpler BVP problem and dynamics propagation. This motivates us to perform motion planning in the flat state space $\mathcal{Z}$ instead of the original state space $\mathcal{X}$, thanks to the conversions (6. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")) and (7. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")). Our approach is illustrated in Fig. 3.

Figure 3: Formulating the kinodynamic planning problem in the flat state space with linear dynamics.

Given an initial state $\mathbf{x}_{s}$ with an initial control input $\mathbf{u}_{s}$, and a goal region $\mathcal{G}$ with a desired control $\mathbf{u}_{\mathcal{G}}$, the initial flat output and goal region are calculated as $\mathbf{y}_{s} = {\mathbf{h}{(\mathbf{x}_{s},\mathbf{u}_{s},{\overset{˙}{\mathbf{u}}}_{s},\ldots,\mathbf{u}_{s}^{(k)})}}$ and $\mathcal{G}_{\mathbf{y}} = \left. \{{\mathbf{h}{(\mathbf{x},\mathbf{u}_{\mathcal{G}},{\overset{˙}{\mathbf{u}}}_{\mathcal{G}},\ldots,\mathbf{u}_{\mathcal{G}}^{(k)})}} \middle| {\mathbf{x} \in \mathcal{G}}\} \right.$, respectively. Note that in many common robot systems such as Examples 1, 2 and 3, the flat output $\mathbf{y}$ does not depend on $\mathbf{u}$ and therefore, the values of $\mathbf{u}_{s}$ and $\mathbf{u}_{\mathcal{G}}$ need not be specified. The original kinodynamic motion planning (Problem 1) becomes finding a dynamically feasible trajectory ${\mathbf{σ}}_{\mathbf{z}}{(t)}$ in the flat state space $\mathcal{Z}$ that connects the start $\mathbf{z}_{s}$ to the goal region $\mathcal{G}_{\mathbf{z}}$, and satisfies the linear dynamics, as summarized in Problem 2.

### Problem 2

Given an initial flat state $\mathbf{z}_{s}$ and a goal region $\mathcal{G}_{\mathbf{z}}$, calculated from $\mathbf{y}_{s}$ and $\mathcal{G}_{\mathbf{y}}$ via, the original kinodynamic motion planning (Problem 1) is equivalent to finding a control input function $\mathbf{w}{(t)}$ that generates a dynamically feasible trajectory ${\mathbf{σ}}_{\mathbf{z}}{(t)}$:

where the matrices $\mathbf{A}$ and $\mathbf{B}$ are defined in.

To solve Problem 2, we develop primitive subroutines in the flat state space $\mathcal{Z}$ for a sampling-based kinodynamic planning framework proposed in Alg. 1, which is consistent with most existing sampling-based motion planners \[karaman2010kinorrt, webb2013kinodynamicRRT, li2016sst\]. Leveraging the linear dynamics, we develop an efficient FlaskExtend subroutine (see Sec. V-C) to construct a graph or tree ${\mathbb{G}}_{\mathbf{z}} = {({\mathbb{V}}_{\mathbf{z}},{\mathbb{E}}_{\mathbf{z}})}$ in the flat state space $\mathcal{Z}$, where ${\mathbb{V}}_{\mathbf{z}}$ and ${\mathbb{E}}_{\mathbf{z}}$ denote the sets of nodes and edges, respectively, by solving the BVP and dynamics propagation problems for a polynomial local "flat" path $\mathbf{z}_{loc}{(t)}$. The resulting trajectory ${\mathbf{σ}}_{\mathbf{z}}{(t)}$ is a continuous piecewise-polynominal, consisting of $M$ local "flat" paths found on ${\mathbb{G}}_{\mathbf{z}}$:

with $0 = t_{0} < t_{1} < \ldots < t_{M}$ where the pseudo-control $\mathbf{w}_{i}{(t)}$ is applied in the time interval $\lbrack t_{i - 1},t_{i}\rbrack$, for $i = {1,\ldots,M}$. The trajectory ${\mathbf{σ}}_{\mathbf{z}}{(t)}$ is converted back to a trajectory ${\mathbf{σ}}{(t)}$ with control $\mathbf{u}{(t)}$ as follows:

which is possible because the pseudo-control input $\mathbf{w}$ is the $r$-th order derivative of $\mathbf{y}$ with $r \geq {\max{(l,m)}}$ in Eq..

Input: Initial state xs, initial control us, goal region 𝒢 with control input u𝒢, maximum iterations I
Output: A collision-free dynamically feasible trajectory σ (t) with control input u (t).
/* Convert to the flat state space */
2 $\mathbf{y}_{0}\leftarrow{\mathbf{h}{(\mathbf{x}_{0},\mathbf{u}_{0},{\overset{˙}{\mathbf{u}}}_{0},\ldots,\mathbf{u}_{0}^{(k)})}}$
3 $\mathcal{G}_{\mathbf{y}}\leftarrow{\{{\mathbf{h}{(\mathbf{x},\mathbf{u}_{\mathcal{G}},{\overset{˙}{\mathbf{u}}}_{\mathcal{G}},\ldots,\mathbf{u}_{\mathcal{G}}^{(k)})}}:{\mathbf{x} \in \mathcal{G}}\}}$
4 $\mathbf{z}_{0}\leftarrow{(\mathbf{y}_{0},{\overset{˙}{\mathbf{y}}}_{0},\ldots,\mathbf{y}_{0}^{({r - 1})})}$
5 $\mathcal{G}_{z} = {\{{(\mathbf{y},\overset{˙}{\mathbf{y}},\ldots,\mathbf{y}^{({r - 1})})}:{\mathbf{y} \in \mathcal{G}_{\mathbf{y}}}\}}$
7Create a planning graph or tree 𝔾z = (𝕍z,𝔼z) with set of vertices 𝕍z and set of edges 𝔼z.

/* Grow 𝔾z on the flat state space */

11 if Goal region 𝒢z is reached then
12 Find the trajectory σz (t) with pseudo-input w (t) from 𝔾z.

/* Convert the trajectory σz (t) to the original state space */
16 return Trajectory σ (t) with control u (t).
return Trajectory not found.
Algorithm 1 FLASK: Sampling-based Kinodynamic Motion Planning via Differential Flatness

### V-C FlaskExtend Subroutine on Flat Output Space

The goal of the FlaskExtend subroutine, described in Alg. 2, is to find a collision-free dynamically feasible local "flat" path ${{\mathbf{z}_{loc}{(t)}},t} \in {\lbrack 0,T\rbrack}$ with a time duration $T$, that connects an existing node $\mathbf{z}_{0} \in {\mathbb{V}}$ to a new node $\mathbf{z}_{f}$. A motion $\mathbf{z}_{loc}{(t)}$ can be generated by either sampling $\mathbf{z}_{f}$ and solving a BVP problem (Sec. V-C1) or sampling a pseudo-control input $\mathbf{w}_{0}$ and integrating the flat state dynamics (Sec. V-C2). For either case, we show that a closed-form expression of $\mathbf{z}_{loc}{(t)}$ can be obtained for parallelized collision checking in FlaskCC subroutine in Sec. V-D. If $\mathbf{z}_{loc}{(t)}$ is valid, the node $\mathbf{z}_{f}$ is added to ${\mathbb{V}}_{\mathbf{z}}$ while the edge $(\mathbf{x}_{0},\mathbf{x}_{f})$ associated with the local "flat" path $\mathbf{z}_{loc}{(t)}$ is added to ${\mathbb{E}}_{\mathbf{z}}$.

Input: The planning graph/tree 𝔾z = (𝕍z,𝔼z)
3 Pick an existing node Z0 ∈ 𝕍z

/* Solve BVP in closed form */
4 zl o c (t)← Eq. with a sampled T or an optimal T = T* from.

/* Analytically propagate dynamics */

### V-C1 Solving the BVP Problem in Closed Forms

Given an existing node $\mathbf{z}_{0}$ and a sampled $\mathbf{z}_{f}$, we find a local "flat" path ${{\mathbf{z}_{loc}{(t)}},t} \in {\lbrack 0,T\rbrack}$ that connects $\mathbf{z}_{0}$ and $\mathbf{z}_{f}$ and satisfies the flat state dynamics. Consider a cost function of a motion ${{\mathbf{z}{(t)}},t} \in {\lbrack 0,T\rbrack}$ with pseudo-control $\mathbf{w}{(t)}$ that accounts for the total control effort and the time duration $T$ as follows:

where $\mathbf{R} \succ 0$ is a user-defined positive definite weight matrix, and $\rho$ controls the trade-off between the control effort and the time it takes to finish the trajectory. We formulate the following Linear Quadratic Minimum Time (LQMT) problem \[Verriest1991QuadMinTime\] to solve for our local "flat" path $\mathbf{z}_{loc}{(t)}$ and control $\mathbf{w}_{loc}{(t)}$:

where the matrices $\mathbf{A}$ and $\mathbf{B}$ are defined in. Let us define $\mathbf{d}_{T} = {\mathbf{z}_{f} - {e^{\mathbf{A}T}\mathbf{z}_{0}}}$ and the Gramian matrix

The duration $T$ can be either a) set to a fixed or sampled value or b) optimized for a minimum-time trajectory, as shown next. Given a sample $\mathbf{z}_{f}$, the cost $\mathcal{C}_{loc}$ of the local path $\mathbf{z}_{loc}{(t)}$ is commonly used to choose an existing node $\mathbf{z}_{0}$ on the graph ${\mathbb{G}}_{\mathbf{z}}$, *e.g.*, those in the neighborhood of $\mathbf{z}_{f}$ with $\mathcal{C}_{loc}$ smaller than a threshold $\zeta$ (see Sec. VI for how to choose the value of $\zeta$ as the number of nodes $N = {|{\mathbb{V}}_{\mathbf{z}}|}$ increases).

### Fixed-time Optimal Local Paths

For a fixed time duration $T$, the LQMT problem has a closed-form solution, by following \[Verriest1991QuadMinTime\], for the optimal pseudo-control input:

with the optimal cost:

and the optimal local "flat" path:

Since the matrix $\mathbf{A}$ is nilpotent, *i.e.,* $\mathbf{A}^{r} = 0$, we have $e^{\mathbf{A}t} = {\sum_{j = 0}^{r - 1}\frac{\mathbf{A}^{j}t^{j}}{j!}}$. Therefore, the Grammian $\mathbf{G}_{T}$ and $\mathbf{d}_{T}$ become polynomials of the time duration $T$. The optimal control input $\mathbf{w}_{loc}{(t)}$ becomes a $({r - 1})$th order polynomial while the optimal flat output trajectory $\mathbf{y}_{loc}{(t)}$ is a $({{2r} - 1})$th order polynomial, which is compatible with simd-based collision checking in Sec. V-D.

### Minimum-time Optimal Local Paths

If we have the freedom to choose the duration $T$, we can solve the following equation for a minimum time $T = T^{\ast}$ \[Verriest1991QuadMinTime\]:

For an arbitrary value of the pseudo-control order $r$, the minimum-time condition can be solved for a positive $T^{\ast}$ using a numerical root-finding solver \[nocedal1999numerical\], that is amenable to simd parallelization such as L-BFGS \[zhu1997lbfgsb\]. More notably, many common systems such as manipulators (Example 1) or unicycles (Example 2) have $r = 2$ while systems with higher $r$, such as quadrotors (Example 3), can reduce the pseudo-control order to $r = 2$ to simplify motion planning in practice, as shown in \[liu2017search\]. For such cases, Example 4. ‣ Minimum-time Optimal Local Paths ‣ V-C1 Solving the BVP Problem in Closed Forms ‣ V-C FlaskExtend Subroutine on Flat Output Space ‣ V Technical Approach ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness") below shows the optimal local "flat" path, pseudo-control input, and optimal duration, where the condition is equivalent to solving a $4$th-order polynomial in (28. ‣ Minimum-time Optimal Local Paths ‣ V-C1 Solving the BVP Problem in Closed Forms ‣ V-C FlaskExtend Subroutine on Flat Output Space ‣ V Technical Approach ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")) for a positive root, which can also be done in closed forms. As a result, solving for an optimal time $T = T^{\ast}$ is suitable for simd parallelization.

### Example 4 (Fixed-time and minimum-time local paths)

We consider a *special case with $r = 2$* and $\mathbf{R} = \mathbf{I}_{n}$, *e.g.*, for a fully-actuated manipulator or a unicycle. Given a flat output $\mathbf{y}$, the flat state is $\mathbf{z} = {(\mathbf{y},\overset{˙}{\mathbf{y}})}$ with the pseudo-control input $\mathbf{w}$ defined as the acceleration: $\mathbf{w} = \overset{¨}{\mathbf{y}}$. Similar to \[liu2017search\] (for $n = 3$), the flat state $\mathbf{z}$ follows the linear dynamics with:

Since $\mathbf{A}^{j} = 0$ for all $j \geq 2$, we have $e^{\mathbf{A}t} = {\mathbf{I}_{2n} + {\mathbf{A}t}}$ and $e^{\mathbf{A}^{\top}t} = {\mathbf{I}_{2n} + {\mathbf{A}^{\top}t}}$, leading to:

The matrix inverse of $\mathbf{G}_{T}$ can be derived using the Schur complement \[petersen2008matrix\]: ${\mathbf{G}_{T}^{- 1} = \begin{bmatrix}
{\frac{12}{T^{3}}\mathbf{I}_{n}} & {- {\frac{6}{T^{2}}\mathbf{I}_{n}}} \\
{- {\frac{6}{T^{2}}\mathbf{I}_{n}}} & {\frac{4}{T}\mathbf{I}_{n}}
\end{bmatrix}}.$ The optimal control input becomes:

This leads to a minimum-acceleration local "flat" path $\mathbf{z}_{loc}{(t)}$ as follows:

In other words, the optimal flat output is:

The optimal cost function is calculated as:

To find a minimum time $T$, we solve ${{d\mathcal{C}_{loc}}/d}T$ for a positive real root $T^{\ast}$:

which is equivalent to solving a $4$th-order polynomial with closed-form solutions:

The detailed derivation can be found in Sec. X-A.

### Remarks

We note that the closed-form polynomial solution of the LQMT problem is derived without considering additional constraints such as collision avoidance, velocity and acceleration limits. In our approach, such constraints are enforced via collision checking in Sec. V-D. If the trajectory $\mathbf{z}_{loc}{(t)}$ in from $\mathbf{z}_{0}$ to $\mathbf{z}_{f}$ violates a constraint, it will be considered invalid. However, it does not necessarily mean that $\mathbf{z}_{f}$ is unreachable from $\mathbf{z}_{0}$. If there exists a constrained optimal trajectory $\mathbf{z}_{loc}^{\ast}{(t)}$, our Theorem 1. ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness") in Sec. VI shows that as the number of samples $N = {|{\mathbb{V}}_{\mathbf{z}}|}$ goes to infinity, the probability of having a piecewise-polynomial trajectory that is close to $\mathbf{z}_{loc}^{\ast}{(t)}$ (see Def. 2. ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")) tends to $1$, *i.e.*, $\mathbf{z}_{f}$ can still be reached via a sequence of nodes with high probability.

Interestingly, recent results from optimal control \[beaver2024optimal\] find an optimal piecewise-polynomial local path under constraints for differentially flat systems by carefully switching between modes, each of which corresponds to a polynomial motion primitive. This approach solves an optimality condition on the cost function and the constraints to find an optimal mode schedule and is shown to generate an optimal trajectory for low-DOF systems with simple closed-form constraints in a few milliseconds. However, it is challenging to design such a mode-switching mechanism for high-DOF robots with complex geometry due to complicated forward kinematics, especially when the local path generation time is often restricted to the nanosecond range. Intriguingly, from a sampling-based perspective, our Theorem 1. ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness") (see Sec. VI) shows that such an optimal piecewise-polynomial local path can be found on our planning graph with high probability, *i.e.*, a sequence of nodes on our graph is equivalent to the mode-switching schedule from \[beaver2024optimal\]. Nevertheless, this is an exciting direction for generating a constrained local path $\mathbf{z}_{loc}{(t)}$ in our framework that we leave for future work.

### V-C2 Dynamics Propagation in Closed-Forms

As BVP problems are challenging to solve, most existing work \[li2016sst\] resorts to dynamics propagation, where the planning tree is extended by sampling a constant control input and integrating the robot dynamics over small time steps using numerical methods. While our *BVP closed-form solution* in Sec. V-C1 *is the main focus of our paper*, this section shows that transforming the kinodynamic planning problem to the flat state space (Problem 2) also leads to closed-form dynamics propagation, and hence gets rid of numerical approximations with potentially high accumulated errors.

Instead of sampling the original control input, we sample the pseudo-control input ${\mathbf{w}_{loc}{(t)}} = \mathbf{w}_{0}$ and the duration $T$, leading to a closed-form local path:

where ${\mathbf{y}_{loc}{(t)}} = {{\frac{\mathbf{w}_{0}}{r!}t^{r}} + {\sum_{i = 0}^{r - 1}{\frac{\mathbf{y}_{0}^{(i)}}{i!}t^{i}}}}$. These local "flat" paths can be used in tree-based kinodynamic planners such as Stable Sparse RRT \[li2016sst\] and are also suitable for parallelized forward kinematics and collision checking in Sec. V-D. Propagation-based planners tend to "wander" in the state space due to the suboptimality of random control with small time steps $T$. Interestingly, our BVP solutions can help by finding shortcuts to the goal rather than keep expanding the tree, and therefore reduce the planning time significantly as illustrated in Sec. VII-A.

Input: Flat state path zl o c (t) with pseudo-control w (t)
Output: Whether zl o c (t) collides with obstacles
/* Convert to the original state space */
3for $i \in {\{ 0,\ldots,\left\lceil \frac{N}{K} \right\rceil\}}$ do

/* Parallel checking via simd [thomason2024vamp] */

/* checking other constraints such as state and control limits */
6 if ∃j ∈ bi: xl o c (tj), ul o c (tj) violate other constraints then

### V-D Vectorized Collision Checking

To perform collision checking on a local "flat" path $\mathbf{z}_{loc}{(t)}$ with pseudo-control $\mathbf{w}_{loc}{(t)}$ (Alg. 3), we convert it back to the original state space $\mathcal{X}$ and obtain the corresponding closed-form local path and control:

We next discretize $\mathbf{x}_{loc}{(t)}$ and $\mathbf{u}_{loc}{(t)}$ at $N$ times: ${t_{1},t_{2},\ldots,t_{N}} \in {\lbrack 0,T\rbrack}$, grouped into several spatially distributed batches of size $K$:

for $i = {0,\ldots,\left\lceil \frac{N}{K} \right\rceil}$. For each batch $\mathbf{b}_{i}$, we obtain a set of samples ${\{{\mathbf{x}_{loc}{(t_{j})}}\}}_{t_{j} \in \mathbf{b}_{i}}$ and perform fast parallelized collision checking via simd instructions, as illustrated in Fig. 2(b). The batch size $K$ is the number of floats that a simd register can store, *e.g.*, $K = 8$ for the commonly used AVX2 instruction set. The robot's geometry is represented by a set of SIMD-compatible primitive shapes such as spheres or capsules, whose poses are calculated via forward kinematics for multiple states and checked for collisions with obstacles using simd parallelism. If any state in batch $\mathbf{b}_{i}$ leads to collisions with an obstacle, we terminate the collision checking subroutine early and move on to other local paths.

Similarly, other constraints such as state and control limits can be checked in parallel for each batch $\mathbf{b}_{i}$ to validate $\mathbf{z}_{loc}{(t)}$. In general, the conversions (6. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")) and (7. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")) are nonlinear and might complicate the exact conversions of state and control limits on $(\mathbf{x},\mathbf{u})$ to corresponding flat state and pseudo-control limits on $(\mathbf{z},\mathbf{w})$. For many common robot systems, an upper bound on the conversions (7. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")) can be obtained to estimate the limits in the flat state space as the flat output $\mathbf{y}$ is often part of the original state $\mathbf{x}$ (see Examples 1, 2 and 3). For example, any limits on the joint angles and velocities of a manipulator in Example 1 can be directly translated to the flat state or any limits on the speed $v$ of a unicyle in Example 2 can be used to bound the first derivative of the flat out put $(\overset{˙}{x},\overset{˙}{y})$. Furthermore, since the flat output describes certain physical properties of the robot, *e.g.*, the position and yaw angle of a quadrotor in Example 3, users can also directly specify the flat state and pseudo-control constraints, *e.g.*, maximum linear velocity and yaw rates. For general nonlinear systems, this issue can be addressed by using large limits in the flat state space, and checking the local path $({\mathbf{x}_{loc}{(t)}},{\mathbf{u}_{loc}{(t)}})$ in against the original state and control limits on $(\mathbf{x},\mathbf{u})$ via sampling. However, there is a trade-off between the size of the flat state space and the risk of missing valid paths, which can be tuned based on the planner's performance, *e.g.*, the larger flat state space may lead to longer planning time but reduce the risk.

Input: A collision-free piecewise-polynomial trajectory σz (t) = {(zi (t),ti)}i = 1M, with control inputs wz(t)={wi(t),ti)}i = 1M,
4 Calculate zi j (t) from Eq. with z0 = zi (ti − 1), zf = zj (tj), and a time Ti j = tj − ti − 1 or an optimal Ti j from.

/* Bypass unnecessary motions if the trajectory zi j (t) does not violates any constraints */
Algorithm 4 Trajectory Postprocessing

### V-E Trajectory Postprocessing

Our kinodynamic planning approach in Sec. V-B returns a piecewise-polynomial trajectory: ${{\mathbf{σ}}_{\mathbf{z}}{(t)}} = \left\{ {({\mathbf{z}_{i}{(t)}},t_{i})} \right\}_{i = 1}^{M}$, for $0 = t_{0} < t_{1} < \ldots < t_{M}$ where the polynomial ${{\mathbf{z}_{i}{(t)}},t} \in {\lbrack t_{i - 1},t_{i}\rbrack}$ corresponds to the pseudo-control $\mathbf{w}_{i}{(t)}$ and time duration $T_{i} = {t_{i} - t_{i - 1}}$. Due to the sampling-based nature of our approach, the trajectory might contain unnecessary local paths and often requires further postprocessing, *e.g.*, by seeking shortcuts between nodes. For completeness, a simple trajectory postprocessing scheme is provided in Alg. 4 such that if there exists a collision-free trajectory $\mathbf{z}_{ij}{(t)}$ that connects two nodes $\mathbf{z}_{i}{(t_{i - 1})}$ and $\mathbf{z}_{j}{(t_{j})}$, the local paths $\mathbf{z}_{k}$, $i \leq k \leq j$ in between can simply be bypassed by $\mathbf{z}_{ij}{(t)}$. We note that our approach is general and therefore, compatible with other complex trajectory shortening schemes such as \[geraerts2007creating, hauser2010trajsim\].

## Probabilistic Exhaustivity and Optimality Analysis

In this section, we will examine the *probabilistic exhaustivity* of our FLASK framework (Sec. VI-A), which is a key concept for proof of optimality common among asymptotically optimal planners \[bekris2020AOSurvey, karaman2011optimalmp, janson2015fmt\]. As our approach is general and compatible with most sampling-based motion planners, we provide an outline of the *optimality analysis* in Sec. VI-B based on the proven probabilistic exhaustivity property.

### VI-A Probabilistic Exhaustivity

The probabilistic exhaustivity property, introduced in \[kavraki1998analysis, schmerling2015optimal_driftless\], is stronger than probabilistic completeness \[lavalle2006planning\]. While probabilistic completeness only requires *one* solution to be found, *probabilistic exhaustivity* requires that *any* trajectory $\mathbf{π}$, with a $\delta$-clearance to the occupied regions of the state space (see Def. 2. ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")), can be approximated arbitrarily well with high probability by a piecewise trajectory $\mathbf{σ}$, composed of BVP solutions ${{\mathbf{σ}}{(t)}} = \left\{ {({\mathbf{x}_{i}{(t)}},t_{i})} \right\}_{i = 1}^{M}$ connecting $M + 1$ nodes ${\{{\overline{\mathbf{x}}}_{i}\}}_{i = 0}^{M}$ on the graph, as the number of nodes tends to infinity. Our analysis relies on the following assumptions and definitions.

### Assumption 1

The pseudo-control input $\mathbf{w} = \mathbf{y}^{(r)}$ in Eq. 14 has $r$ strictly larger than $l$ (defined in Eq. 7. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")). This is the common case as seen in Examples 1, 2, and 3. As a result, the original state $\mathbf{x}$ can be recovered using Eq. 7. ‣ IV-B Differential Flatness ‣ IV Preliminaries ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness") solely from the flat state $\mathbf{z}$: $\mathbf{x} = {{\mathbf{α}}{(\mathbf{z})}}$.

### Definition 2 ($\delta$-clearance trajectory \[bekris2020AOSurvey, schmerling2015optimal_driftless\])

A trajectory $\mathbf{π}$ with duration $T_{\mathbf{π}}$ in the state space $\mathcal{X}$ is called "$\delta$-clearance" if the state $\mathbf{x}{(t)}$ stays in the $\delta$-interior of the free space $\mathcal{X}_{free}$:

### Definition 3 ($(\varepsilon,\zeta,\eta)$-close piecewise trace \[schmerling2015optimal_drift\])

Given a trajectory ${\mathbf{π}}{(t)}$ with control $\mathbf{u}_{\mathbf{π}}{(t)}$ and duration $T_{\mathbf{π}}$, a piecewise trajectory ${{\mathbf{σ}}{(t)}} = \left\{ {({\mathbf{x}_{i}{(t)}},t_{i})} \right\}_{i = 1}^{M}$ with control ${\mathbf{u}_{\mathbf{σ}}{(t)}} = \left\{ {({\mathbf{u}_{i}{(t)}},t_{i})} \right\}_{i = 1}^{M}$ and duration $T_{\mathbf{σ}}$, connecting $M + 1$ points ${\{{\overline{\mathbf{x}}}_{i}\}}_{i = 0}^{M}$, is called an "$(\varepsilon,\zeta,\eta)$-close piecewise trace" of $\mathbf{π}$ if:

The cost of $\mathbf{σ}$ is $\varepsilon$-close to that of $\mathbf{π}$:

The cost of the $i$-th segment is bounded by $\zeta$:

The maximum distance from a point on $\mathbf{σ}$ to ${\mathbf{π}}{(t)}$ is bounded by $\eta$:

### Theorem 1 (Probabilistic Exhausitivity)

Consider our sampling-based kinodynamic planning framework, FLASK, in Alg. 1 where the FlaskExtend subroutine in Alg. 2 uses the BVP solution with optimal time $T^{\ast}$ (lines 1-4) and the cost function in Eq. 20. Under 1, let $\mathcal{Z}_{free} = {\{{\mathbf{z} \in \mathcal{Z}}:{{{\mathbf{α}}{(\mathbf{z})}} \in \mathcal{X}_{free}}\}}$ and $\mathcal{Z}_{obs} = {\mathcal{Z} \smallsetminus \mathcal{Z}_{free}}$ denote the free and occupied flat state space, respectively. Let ${\mathbf{π}}_{\mathbf{z}}$ be a $\delta$-clearance trajectory for a $\delta > 0$ with respect to $\mathcal{Z}_{free}$. Let $N = {|{\mathbb{V}}_{\mathbf{z}}|}$ denote the number of nodes/samples in our planning graph ${\mathbb{G}}_{\mathbf{z}} = {({\mathbb{V}}_{\mathbf{z}},{\mathbb{E}}_{\mathbf{z}})}$. Given a constant $C_{\mu}$, define $C_{\mathcal{Z}_{free}} = {C_{\mu}^{- 1}D^{- 1}6^{{rn} + {{r^{2}n}/2}}2^{{rn}/2}\mu{(\mathcal{Z}_{free})}}$ with the volume of the free space $\mu{(\mathcal{Z}_{free})}$, a constant $D = {{({{rn} + {r^{2}n}})}/2}$ and a user-defined parameter $\kappa \geq 0$.

In the flat state space, let $\mathcal{A}_{N}$ define the event that there exists an $(\varepsilon,\zeta_{N},\eta_{N})$-close piecewise trace of ${\mathbf{π}}_{\mathbf{z}}$, denoted as ${{\mathbf{σ}}_{\mathbf{z}}{(t)}} = \left\{ {({\mathbf{z}_{i}{(t)}},t_{i})} \right\}_{i = 1}^{M}$ with:

for some constant $M$ and $C_{p}$. There exists a constant $C_{\mu}$ such that as $N\rightarrow\infty$, the probability that $\mathcal{A}_{N}$ does not occur is bounded as:

Under 1, let ${\mathbf{π}} = {{\mathbf{α}}{({\mathbf{π}}_{\mathbf{z}})}}$ be the corresponding trajectory of ${\mathbf{π}}_{\mathbf{z}}$ in the original state space $\mathcal{X}$. If the conversion ${\mathbf{α}}:{\mathcal{Z}\rightarrow\mathcal{X}}$ is Lipschitz-continuous on $\mathcal{Z}$ with a Lipschitz constant $L_{\mathbf{α}}$, we define an event $\mathcal{B}_{N}$ that there exists a $(\varepsilon,\zeta_{N},{L_{\mathbf{α}}\eta_{N}})$-close piecewise trace of $\mathbf{π}$ where the bounds $\zeta_{N}$ $\eta_{N}$ are calculated in (32 ‣ Theorem 1 (Probabilistic Exhausitivity). ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")). Then, the probability that $\mathcal{B}_{N}$ does not occur is bounded as:

### Proof

Our proof follows a common intuition in geometric motion planning \[kavraki1998analysis, bekris2020AOSurvey\], that as the number of samples increases, there exists a sequence of spheres with high probability that covers the trajectory ${\mathbf{π}}_{\mathbf{z}}$ and contains a piecewise-linear path arbitrarily $\varepsilon$-close to ${\mathbf{π}}_{\mathbf{z}}$. However, this is not trivial in our case due to the dynamics constraints. Unlike a linear edge that can be bounded easily by a sphere, the nonlinear local path $\mathbf{z}_{loc}$ is bounded by an ellipsoid in our proof instead, as shown below.

Probabilistic exhaustivity in the flat state space: Consider our linear system in the flat state space $\mathcal{Z} \subset {\mathbb{R}}^{rn}$ with matrices $\mathbf{A} \in {\mathbb{R}}^{{{rn} \times r}n}$, $\mathbf{B} \in {\mathbb{R}}^{{rn} \times n}$. Consider the controllability matrix:

Clearly, we have ${{rank}{({\mathbf{C}{(\mathbf{A},\mathbf{B})}})}} = {rn}$ with $rn$ linearly independent column vectors: $\left\{ {\{\mathbf{b}_{i},{\mathbf{A}\mathbf{b}}_{i},\ldots,{\mathbf{A}^{r - 1}\mathbf{b}_{i}}\}}_{i = 1}^{n} \right\}$, where $\mathbf{b}_{i}$ denotes the $i$-th column of the matrix $\mathbf{B}$ in. Therefore, our linear system is controllable with the following controllability indices:

The controllability indices, as shown later, allow us to bound the volume of an ellipsoid containing our local path $\mathbf{z}_{loc}{(t)}$.

Figure 4: Our theoretical analysis: (a) Probabilistic exhaustivity: as N → ∞, the probability that there exists an (ε,ζN,ηN)-close piecewise trace σz (t) (magenta), on our planning graph 𝔾, of any trajectory πz (green) with δ-clearance approaches 1; (b) Optimality: our approach will find an (ε,ζN,ηN)-close piecewise trace σz(N) (t) (magenta) of a δN-clearance trajectory ${\hat{\mathbf{σ}}}_{\mathbf{z}}^{(N)}{(t)}$ (green). As δN → 0, the trajectory ${\hat{\mathbf{σ}}}_{\mathbf{z}}^{(N)}{(t)}$ converges to the optimal trajectory σz* (t) (red). Since ζN → 0, ηN → 0 and δN → 0 as N → ∞, our piecewise trajectory σz(N) (t) converges to σz* (t) in probability.

As the number of samples $N$ goes to infinity, the duration $T$ of a local path $\mathbf{z}_{loc}$ approaches $0$ with high probability due to the higher sample density. Therefore, we are interested in how the cost $\mathcal{C}_{loc}{(T)}$ in Eq. 24 behaves near $T = 0$. As the Gramian matrix $\mathbf{G}_{T} \succ 0$, we consider an ellipsoid $\mathcal{E}_{\psi}$ around a point $\mathbf{z}$, defined as

which can be used to bound the quadratic component $\mathbf{d}_{T}^{\top}\mathbf{G}_{T}^{- 1}\mathbf{d}_{T}$ of $\mathcal{C}_{loc}{(T)}$. The volume of this ellipsoid is ${\mu{(\mathcal{E}_{\psi})}} = {\psi^{rn}\mu{(\mathcal{S}_{rn})}\sqrt{\det{(\mathbf{G}_{T})}}}$, where $\mu{(\mathcal{S}_{rn})}$ is the volume of a unit ball $\mathcal{S}_{rn}$ in ${\mathbb{R}}^{rn}$. As $T\rightarrow 0$, the value of $\det{(\mathbf{G}_{T})}$ determines how fast the volume of $\mathcal{E}_{\psi}$ goes to $0$. Due to the controllability indices in Eq. 36 ‣ Proof. ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness"), the determinant of the Gramian matrix $\mathbf{G}_{T}$ is ${\Theta{(T^{\sum_{i}^{n}\nu_{i}^{2}})}} = {\Theta{(T^{r^{2}n})}}$ as $T\rightarrow 0$ according to Lemma III.4 in \[schmerling2015optimal_drift\], *i.e.*, there exist constants ${T_{0},C_{1},C_{2}} > 0$ such that

Denote $C_{\mu} = {\sqrt{C_{1}}\mu{(\mathcal{S}_{rn})}}$. Eq. 37 ‣ Proof. ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness") allows us to lower bound the rate of the quadratic cost component of the optimal cost in Eq. 24 as the local path duration $T\rightarrow 0$. The lower bound (37 ‣ Proof. ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")) specifies the minimum coverage of the state space by the ellipsoid $\mathcal{E}_{\psi}$, and therefore dictates a finite number of ellipsoids that can cover the entire trajectory ${\mathbf{π}}_{\mathbf{z}}$ (illustrated in Fig. 4(a) ‣ Proof. ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")). This key condition allows us to apply Theorem IV.6 in \[schmerling2015optimal_drift\], which uses random geometric graph theory \[penrose2003random\] to show that the probability that there *does not* exist a sequence of ellipsoids with an $(\varepsilon,\zeta_{N},\eta_{N})$-close piecewise trace ${\mathbf{σ}}_{\mathbf{z}}$ inside is bounded by $O\left( {N^{- {\kappa/D}}{\log^{- {1/D}}N}} \right)$ with $\zeta_{N},\eta_{N}$ defined in Eq. 32 ‣ Theorem 1 (Probabilistic Exhausitivity). ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness") and $D = {{({{rn} + {\sum_{i = 1}^{n}\nu_{i}^{2}}})}/2} = {{({{rn} + {r^{2}n}})}/2}$. In other words, as $N\rightarrow\infty$, the probability that the event $\mathcal{A}_{N}$ does not occur is bounded by:

Probabilistic exhaustivity in the original state space: As the conversion $\mathbf{x} = {{\mathbf{α}}{(\mathbf{z})}}$ is Lipschitz-continuous on $\mathcal{Z}$ with a Lipschitz constant $L_{\mathbf{α}}$, we have:

for all ${\mathbf{z}_{1},\mathbf{z}_{2}} \in \mathcal{Z}$.

Let ${\mathbf{σ}} = {{\mathbf{α}}{({\mathbf{σ}}_{\mathbf{z}})}}$ be the corresponding trajectory in the original state space of the $(\varepsilon,\zeta_{N},\eta_{N})$-close piecewise trace ${\mathbf{σ}}_{\mathbf{z}}$. Given a time $t_{\mathbf{σ}} \in {\lbrack 0,T_{\mathbf{σ}}\rbrack}$, define $t_{\mathbf{π}}^{\ast} = {{argmin}_{t_{\mathbf{π}} \in {\lbrack 0,T_{\mathbf{π}}\rbrack}}{\|{{{\mathbf{σ}}_{\mathbf{z}}{(t_{\mathbf{σ}})}} - {{\mathbf{π}}_{\mathbf{z}}{(t_{\mathbf{π}})}}}\|}}$. Then, we have:

since ${\mathbf{σ}}_{\mathbf{z}}$ is a $(\varepsilon,\zeta_{N},\eta_{N})$-close piecewise trace. Let $\tau_{\mathbf{π}}^{\ast} = {{argmin}_{\tau_{\mathbf{π}} \in {\lbrack 0,T_{\mathbf{π}}\rbrack}}{\|{{{\mathbf{σ}}{(t_{\mathbf{σ}})}} - {{\mathbf{π}}{(\tau_{\mathbf{π}})}}}\|}}$. Clearly, we have the following bound that holds *for all $t_{\mathbf{σ}} \in {\lbrack 0,T_{\mathbf{σ}}\rbrack}$*:

By maximizing over $t_{\mathbf{σ}} \in {\lbrack 0,T_{\mathbf{σ}}\rbrack}$, the maximum distance between a point on $\mathbf{σ}$ to $\mathbf{π}$ in the state space $\mathcal{X}$ satisfies:

As the cost function is defined in the flat state space, the trajectory $\mathbf{σ}$ has the same cost as ${\mathbf{σ}}_{\mathbf{z}}$. Therefore, an $(\varepsilon,\zeta_{N},\eta_{N})$-close piecewise trace ${\mathbf{σ}}_{\mathbf{z}}$ implies an $(\varepsilon,\zeta_{N},{L_{\mathbf{α}}\eta_{N}})$-close piecewise trace $\mathbf{σ}$ or in other words, the event $\mathcal{A}_{N}$ implies the event $\mathcal{B}_{N}$, *i.e.*, ${P{(\mathcal{A}_{N})}} \leq {P{(\mathcal{B}_{N})}}$. Therefore, we have:

Theorem 1. ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness") shows that given any trajectory $\mathbf{π}$ with $\delta$ clearance, as the number of samples/nodes $N\rightarrow\infty$, there exists, with high probability, an $(\varepsilon,\zeta_{N},\eta_{N})$-close piecewise trace $\mathbf{σ}$ of the trajectory $\mathbf{π}$. More importantly, the bounds $\zeta_{N}$ and $\eta_{N}$ are $O\left( \left( \frac{\log N}{N} \right)^{1/D} \right)$, which will be shown later to be critical for our asymptotical optimality analysis.

### VI-B Optimality Analysis

As our FLASK framework in Sec. V (Alg. 1) is compatible with any sampling-based motion planners \[orthey2024-review-sampling\], the optimality guarantees of our trajectory depend on the optimality guarantees of the specific planner that integrates our FlaskExtend subroutine. However, we provide an outline of an optimality analysis based on random geometric graphs \[penrose2003random\] which many asymptotically optimal sampling-based motion planners follow (see \[karaman2011optimalmp, webb2013kinodynamicRRT, janson2015fmt\] for an example and \[bekris2020AOSurvey\] for an excellent review of this topic). Therefore, our framework not only transforms any sampling-based motion planner into its kinodynamic version but also preserves its optimality guarantees.

We define an optimal trajectory solution of Problem 2 with respect to the cost in Def. 4. ‣ VI-B Optimality Analysis ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness"). We note that while our cost function Eq. is defined in the flat state space, it bears physical meaning in the original space as the flat output $\mathbf{y}$ often describes certain physical properties of the robot, *e.g.*, the position and yaw angle of a quadrotor in Example 3. For example, if the pseudo-control input $\mathbf{w} = \mathbf{y}^{(r)}$ in has $r = {2,3,4,\ldots}$, the cost means that we would like to find a minimum acceleration-time, jerk-time, or snap-time trajectory, respectively (*e.g.*, in \[mellinger2011minimumsnap, liu2017search, liu2018search\]).

### Definition 4 (Optimal Trajectory)

Denote $\mathcal{C}_{{\mathbf{σ}}_{\mathbf{z}}} = {\mathcal{C}{({{\mathbf{σ}}_{\mathbf{z}}{(t)}},{\mathbf{w}{(t)}},T)}}$. Assume that there exists a minimum cost $\mathcal{C}^{\ast} = {\min_{{\mathbf{σ}}_{\mathbf{z}}}\mathcal{C}_{{\mathbf{σ}}_{\mathbf{z}}}}$, defined in Eq., over all trajectories ${\mathbf{σ}}_{\mathbf{z}}{(t)}$ that solve Problem 2. A trajectory ${\mathbf{σ}}_{\mathbf{z}}^{\ast}{(t)}$ with control $\mathbf{w}^{\ast}{(t)}$ and its corresponding trajectory ${{\mathbf{σ}}^{\ast}{(t)}} = {{\mathbf{α}}{({{\mathbf{σ}}_{\mathbf{z}}^{\ast}{(t)}},{\mathbf{w}^{\ast}{(t)}})}}$ with control ${\mathbf{u}^{\ast}{(t)}} = {{\mathbf{β}}{({{\mathbf{σ}}_{\mathbf{z}}^{\ast}{(t)}},{\mathbf{w}^{\ast}{(t)}})}}$ in the original state space are called optimal if they achieve the minimum cost $\mathcal{C}^{\ast}$.

In the flat space, the optimal trajectory ${\mathbf{σ}}_{\mathbf{z}}^{\ast}{(t)}$, defined in Def. 4. ‣ VI-B Optimality Analysis ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness"), might have $0$ clearance as illustrated in Fig. 4(b) ‣ Proof. ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness"), *i.e.*, it might touch the boundary of $\mathcal{Z}_{obs}$. However, we assume that there exists a sequence of $\delta_{N}$-clearance trajectories ${\hat{\mathbf{σ}}}_{\mathbf{z}}^{(N)}{(t)}$ with control ${\hat{\mathbf{w}}}^{(N)}$ and duration $T^{(N)}$ such that its cost $\mathcal{C}_{{\hat{\mathbf{σ}}}_{\mathbf{z}}^{(N)}} = {\mathcal{C}{({{\hat{\mathbf{σ}}}_{\mathbf{z}}^{(N)}{(t)}},{{\hat{\mathbf{w}}}^{(N)}{(t)}},T^{(N)})}}$ satisfies:

where $N = {|{\mathbb{V}}_{\mathbf{z}}|}$ denotes the number of nodes/samples in our planning graph ${\mathbb{G}}_{\mathbf{z}} = {({\mathbb{V}}_{\mathbf{z}},{\mathbb{E}}_{\mathbf{z}})}$. This is a common assumption in sampling-based motion planning as the $\delta_{N}$ clearance allows a region around ${\hat{\mathbf{σ}}}_{\mathbf{z}}^{(N)}{(t)}$ with nonzero measure for sampling.

For each $\delta_{N}$-clearance trajectory ${\hat{\mathbf{σ}}}_{\mathbf{z}}^{(N)}{(t)}$, Theorem 1. ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")(i) shows that as $N\rightarrow\infty$, the probability that there is an $(\varepsilon,\zeta_{N},\eta_{N})$-close piecewise trace ${\mathbf{σ}}_{\mathbf{z}}^{(N)}{(t)}$ of ${\hat{\mathbf{σ}}}_{\mathbf{z}}^{(N)}{(t)}$ goes to $1$. This allows us to cover ${\hat{\mathbf{σ}}}_{\mathbf{z}}^{(N)}{(t)}$ by a sequence of ellipsoids of extent $\zeta_{N}$ so that the piecewise trace ${\mathbf{σ}}_{\mathbf{z}}^{(N)}{(t)}$ will stay inside, as illustrated in Fig. 4(b) ‣ Proof. ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness"). Meanwhile, to maintain connectivity around ${\hat{\mathbf{σ}}}_{\mathbf{z}}^{(N)}{(t)}$, the bound $\zeta_{N}$ can be used as thresholds for expanding (*e.g.*, for picking $\mathbf{z}_{0}$ in FlaskExtend in Alg. 2) and rewiring the planning graph ${\mathbb{G}}_{\mathbf{z}}$ to find a better cost for each neighboring node, similar to RRT\* \[karaman2011optimalmp\] or for recursive cost updates via dynamic programming as in FMT\* \[janson2015fmt, schmerling2015optimal_drift\].

More importantly, as $N\rightarrow\infty$, the upper bounds $\zeta_{N},\eta_{N}$ in (32 ‣ Theorem 1 (Probabilistic Exhausitivity). ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")), proportional to $\left( \frac{\log N}{N} \right)^{1/D}$, go to $0$. Therefore, the probability that the piecewise trace ${\mathbf{σ}}_{\mathbf{z}}^{(N)}{(t)}$ converges to ${\hat{\mathbf{σ}}}_{\mathbf{z}}^{(N)}{(t)}$ with cost $\mathcal{C}_{{\mathbf{σ}}_{\mathbf{z}}^{(N)}} \leq {{({1 + \varepsilon})}\mathcal{C}_{{\hat{\mathbf{σ}}}_{\mathbf{z}}^{(N)}}}$ also approaches $1$. Furthermore, by choosing a decreasing clearance $\delta_{N}$ so that $\delta_{N}\rightarrow 0$ as $N\rightarrow\infty$, *e.g.*, $\delta_{N} = {O{(\eta_{N})}}$, we have:

for an arbitrarily small $\varepsilon > 0$, *i.e.*, our kinodynamic planning framework maintains asymptotic optimality. This is illustrated in Fig. 4(b) ‣ Proof. ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness") with denser samples (higher $N$) and smaller clearance $\delta_{N}$ than those of Fig. 4(a) ‣ Proof. ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness"), making our piecewise trajectory ${\mathbf{σ}}_{\mathbf{z}}^{(N)}$ closer to the optimal one as $N$ increases.

Finally, the asymptotical optimality of our approach can also be transformed to the original state space following similar steps due to Theorem 1. ‣ VI-A Probabilistic Exhaustivity ‣ VI Probabilistic Exhaustivity and Optimality Analysis ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")(ii). This analysis importantly affirms that our FLASK framework can be applied to any existing sampling-based motion planners to create a new class of kinodynamic planners without breaking their asymptotic optimality guarantees.

## Evaluation

(a) Unicycle: Bugtrap (top) and Wall (bottom).

(b) 2D quadrotor: Bugtrap (top) and Hole (bottom).

(c) 3D quadrotor: Window (top) and Obstacle (bottom).

Figure 5: Visualization of our trajectories with DynoBench [ortizharo2025iDbAstar] benchmarking problems: the trajectories from our kinodynamic FLASK-RRTConnect and our BVP-augmented FLASK-SST∗ are plotted as blue and magenta solid curves, respectively, while those from the iDb-A* and SST* baselines are shown as orange dashed and green dotted curves, respectively, and the Kino-PAX trajectories are plotted as purple dash-dotted curves.

In this section, we will evaluate the effectiveness of our FLASK framework, applied on different planners and on different robot platforms, from low to high dimensional state spaces in both simulation and real experiments. As our method focuses on fast kinodynamic planning on CPUs, the results from our planners and the baselines are reported on an Intel i7-6900K CPU for a fair comparison. As a reference, we also provide the results from the GPU-based Kino-PAX \[perrault2025kino\] planner, which is run on a GeForce RTX 4070 GPU.

### VII-A Kinodynamic planning for low-d o f systems

In this section, we compare our approach with other kinodynamic planning algorithms provided by the *DynoBench* benchmark \[ortizharo2025iDbAstar\], which contains multiple low-d o f robots and benchmarking environments. We consider $3$ robot platforms: a *unicycle* (Example 2), a $2$D *quadrotor*, and a $3$D *quadrotor* (Example 3). The *unicycle* robot has the following constraints: maximum linear velocity $v \leq v_{max} = {1.0}$, maximum angular velocity $\omega \leq {1.5}$. The $3D$ *quadrotor* has the following parameters: mass $m = {1}$, inertia matrix $\mathbf{J} = {\text{diag}{({\lbrack 0.1,0.1,0.2\rbrack})}}$, maximum linear velocity ${\|\mathbf{v}\|} \leq {4}$, maximum angular velocity ${\|{\mathbf{ω}}\|} \leq {8}$, maximum thrust $f = {1.5mg}$, and maximum torque ${\mathbf{τ}} \leq {2}$, where $g \approx {9.81}$ is the gravitational acceleration. The $2$D *quadrotor*'s dynamics is a special case of the $3$D *quadrotor*'s with position $\mathbf{p} = {\lbrack 0,y,z\rbrack}$, yaw angle $\psi = 0$, and the rotation matrix $\mathbf{R} = \mathbf{R}_{\phi}$ of a pitch angle $\phi$, leading to a simplified flat output $\mathbf{y} = {\lbrack y,z\rbrack} \in {\mathbb{R}}^{2}$. The $2$D *quadrotor* is modeled after a Crazyflie \[giernacki2017crazyflie\] with mass $m = {0.034}$, inertia $J = {{1e} - {4}}$, and arm length $\ell = {0.1}$. The thrusts $f_{1}$ and $f_{2}$, generated from the two onboard motors, satisfy the following constraint: ${0 \leq f_{1}},{f_{2} \leq {0.65mg}}$. The thrust and torque applied on the $2$D quadrotor's center of mass are calculated as: $f = {f_{1} + f_{2}}$ and $\tau = {\ell{({f_{1} - f_{2}})}}$.

TABLE I: Planning performance with DynoBench benchmarks [ortizharo2025iDbAstar].

Figure 6: Visualization of trajectories generated by our FLASK-RRTConnect (top) and by the baseline planner, geometric RRTConnect + TOPP-RA (bottom), for a Franka Emika Panda robot in: (a) cage, (b) box, (c) bookshelf thin, and (d) table pick environments. For each environment, the top image shows a trajectory from the baseline with collided configurations in red, while the bottom image demonstrates that our trajectory is collision-free.

For each platform, we consider $2$ DynoBench environments, shown in Fig. 5: *Bugtrap* and *Wall* for the unicycle, *Bugtrap* and *Hole* for the $2$D quadrotor, and *Window* and *Obstacle* for the $3$D quadrotor. To be compatible with simd-only collision checking, *e.g.*, \[thomason2024vamp\], the obstacles in each environment are represented by a set of spheres, while the unicycle and quadrotor's geometries are both modeled as single spheres.

We apply our FLASK framework to obtain two planners: FLASK-RRTConnect with BVP solutions in Sec. V-C1 and three variants of FLASK-SST^∗^ with dynamics propagation in Sec. V-C2. Our kinodynamic FLASK-RRTConnect replaces a line segment connecting two nodes in an RRT tree by our closed-form BVP solution (local "flat" path) in the FlaskExtend subroutine (Alg. 2), using Eq. 25 with an optimal $T^{\ast}$ from Eq. 26 and $\rho = 1$. For FLASK-SST^∗^, our first variant, BVP-augmented FLASK-SST^∗^, uses Eq. 29 to propagate robot dynamics in closed forms and takes advantage of our minimum-time local "flat" path in to check whether there is a direct connection from an existing node to the goal. Meanwhile, our second variant is a SIMD-only FLASK-SST^∗^ that keeps expanding the tree using vectorized collision checking via SIMD, *without* leveraging the BVP solutions. To highlight the "wandering" effect in propagation-based planners, our third variant disables best-state selection and tree pruning in SST\*, effectively leading to a DP-based FLASK-RRT, where dynamics propagation (DP) with a sampled control is used to extend the RRT tree. The resulting trajectories are simplified by skipping unnecessary local paths using Alg. 4. We compare our approach with three baseline planners: iDb-A\* \[ortizharo2025iDbAstar\], SST\* \[li2016sst\] from OMPL \[sucan2012the-open-motion-planning-library\], both without parallelized collision checking, and a GPU-based coarse-grained parallelized kinodynamic planner, Kino-PAX \[perrault2025kino\]. We maintain the aforementioned robot state and control constraints in our planners, enforced via our parallelized collision checking algorithm in Alg. 3, and in the baselines for a fair comparison.

As each method has its own definition of trajectory costs, it is challenging to compare the quality of the trajectories. However, most cost functions describe a combination of trajectory duration, length, control efforts, and even velocity, acceleration, or higher-order terms, all of which intuitively and indirectly prioritize shorter trajectories. Therefore, we choose the trajectory length and planning time as common metrics for comparison, shown in Table I. For anytime planners such as iDb-A\* \[ortizharo2025iDbAstar\], SST\* \[li2016sst\], we report the time of the first solution and the length of the final solution within a $180$-second limit. Qualitatively, Fig. 5 plots the trajectories generated by our FLASK-RRTConnect (blue solid curves), our BVP-augmented FLASK-SST^∗^ (magenta solid curves), iDb-A\* (orange dashed curves), SST\* (green dotted curves), and Kino-PAX (dash-dotted purple curves).

### VII-A1 Comparison to the baselines

The baselines iDb-A\* and SST\* generate shorter trajectories but often take several seconds to plan, especially for complicated robot dynamics such as quadrotors. Kino-PAX \[perrault2025kino\] achieves planning times in the millisecond range by parallelizing the tree expansion *on GPUs* but returns much longer trajectories, possibly due to the "wandering" effect" from dynamics propagation with sampled suboptimal control. While it achieves similar planning times for simple dynamics such as unicycles, it is $\sim$`<!-- -->`{=html}8--300 times slower than our FLASK-RRTConnect for more complicated systems such as quadrotors. For all $3$ robot platforms, our FLASK-RRTConnect achieves significantly faster planning times than the baselines, in just a few milliseconds, offering the capability of real-time kinodynamic planning. Our BVP-augmented FLASK-SST^∗^ variant is slightly slower than our FLASK-RRTConnect since it is restricted to a constant control input for each local "flat" path instead of directly calculating a time-parameterized optimal control value. However, it is still significantly faster than the baselines in most cases. Meanwhile, our methods maintain comparable trajectory lengths, within 10--20% of the shortest length across the benchmarking problems. Intuitively, this is because the cost function prioritizes shorter trajectories, which leads to lower total control effort and trajectory time. While our generated trajectories can be further optimized by combining with other optimization-based motion planners, *e.g.*, as initial solutions, this is out of the scope of our paper and left for future work.

Our kinodynamic FLASK-RRTConnect
Geometric RRTConnect (VAMP) + TOPP-RA

Total planning time (ms)

⊳Post./TOPP-RA time

Final traj. length (rad)

Total planning time (ms)

⊳Post./TOPP-RA time

Final traj. length (rad)

Total planning time (ms)

⊳Post./TOPP-RA time

Final traj. length (rad)

Total planning time (ms)

⊳Post./TOPP-RA time

Final traj. length (rad)

Total planning time (ms)

⊳Post./TOPP-RA time

Final traj. length (rad)

Table under pick
Total planning time (ms)

⊳Post./TOPP-RA time

Final traj. length (rad)

Total planning time (ms)

⊳Post./TOPP-RA time

Final traj. length (rad)

Total planning time (ms)

⊳ Post./TOPP-RA time

Final traj. length (rad)

TABLE II: Planning performance with a Franka Emika Panda robot over 100 runs of our FLASK-RRTConnect with different environments in MotionBenchMaker [chamzas2022-motion-bench-maker]. For a baseline, we use a collision-free geometric path, provided by a SIMD-parallelized geometric RRTConnect [thomason2024vamp], followed by time parameterization (TOPP-RA [pham2018toppra]). Overall, our kinodynamic FLASK-RRTConnect generates a dynamically feasible trajectory faster than the baseline in almost all environments. Our trajectory is slightly longer but verified to be collision-free while the baseline’s trajectory is colliding in approximately 30% of the cases, due to the time parameterization. Better metrics are shown in bold, while the collision risk is marked as red if positive.

(a) Tracking our trajectory

(b) Tracking a geometric path

Figure 7: Our trajectory is smoother and dynamically feasible, leading to better tracking performance. For example, the third joint angle q3 in the our UR5’s configuration stays close to the desired value from our trajectory (a) while there are overshoots and fluctuates with a geometric path [thomason2024vamp] (b), causing collision in Fig. 8(b). The tracking error ∥qa c t u a l − qd e s i r e d∥ also shows two overshooting peaks with the geometric path in Fig. 7(c).

Figure 8: The “pick and place” task with UR5 robot in a cluttered environment with narrow passages: (a) our kinodynamic planner successfully finishes the task as it generates a smooth and dynamically feasible trajectory that the robot can track accurately; (b) the robot collides with obstacles when trying to track a geometric path [thomason2024vamp] due to overshoots caused by the lack of dynamics constraints.

### VII-A2 The roles of BVP solutions and parallelized collision checking

All of our planners in the experiments use parallelized collision checking but integrate the BVP solution at different levels: *(i)* our FLASK-RRTConnect uses the BVP solution to find all the local paths; *(ii)* our BVP-augmented FLASK-SST^∗^ only uses the BVP solution to find a shortcut to the goal; *(iii)* our SIMD-only FLASK-SST^∗^ only leverages the vectorized collision checking without using the BVP solution; and *(iv)* our DP-based FLASK-RRT simply expands the planning tree using dynamics propagation without best-state selection and pruning benefits from SST\*.

Parallelized collision checking clearly improves the planning times. Compared to iDb-A\* \[ortizharo2025iDbAstar\] and the original SST\* \[li2016sst\], checking the local path for collision in parallel reduces the planning times from tens of seconds to a few seconds (see Table I) for robots with complicated dynamics such as quadrotors. This is the case even when the BVP solution is not used as in our SIMD-only FLASK-SST^∗^ or there is no best-state selection and tree pruning as in our DP-based FLASK-RRT. As propagation-based planners, our SIMD-only FLASK-SST^∗^ and DP-based FLASK-RRT still wander through the state space, a few small time steps at a time, causing longer planning times and trajectory lengths, as shown in Table I. This effect is even worse in DP-based FLASK-RRT as the best-state selection and pruning techniques used in SST\* are not available.

However, our unique integration of BVP solutions and parallelized collision checking is the key to driving the planning times further down to the (sub-)millisecond range. By employing the BVP solution to find a shortcut from a node to the goal, our BVP-augmented FLASK-SST^∗^ generates a trajectory in just milliseconds, significantly faster than SIMD-only FLASK-SST^∗^. This illustrates the potential of our framework to improve existing propagation-based planners by addressing the common "wandering" effects via our BVP solution. Taking a further step, our FLASK-RRTConnect fully integrates the BVP solution to find all local paths during tree expansion, and therefore, leads to less than a millisecond of planning time in many cases. This illustrates our approach's ability to transform any existing sampling-based geometric planner into an ultrafast kinodynamic planner, requiring only widely available CPUs.

### VII-B Kinodynamic planning for high-d o f manipulators

In this section, we evaluate our algorithms with a simulated $7$-d o f Franka Emika Panda robot in PyBullet \[coumans2021pybullet\]. We consider $7$ realistic and challenging environments, including *bookshelf thin*, *bookshelf tall*, *bookshelf small*, *cage*, *box*, *table under pick* and *table pick*, from the MotionBenchMaker benchmark \[chamzas2022-motion-bench-maker\]. For each environment, $100$ motion planning problems with $100$ different pairs of start and goal configurations are generated for our experiments. The obstacles and the robot's geometries are represented by sets of spheres, which are compatible to simd parallelized collision checking as shown in \[thomason2024vamp\]. For each problem, the robot's task is to plan a dynamically feasible trajectory from a start to a goal configuration in the free space.

In our experiments, we use our FLASK-RRTConnect planner, described in Sec. VII-A with trajectory simplification in Alg. 4. Our baseline is a common approach that generates a time-parameterized trajectory, *e.g.*, using TOPP-RA \[pham2018toppra\], from a collision-free geometric path, under kinematic constraints such as velocity and acceleration limits. The geometric path is provided by a simd-parallelized geometric RRTConnect planner from VAMP \[thomason2024vamp\]. For each environment, we use both our planner and the baseline to solve the pre-generated benchmarking problems and report the results in Table II. Our planner's total planning time is calculated as the sum of the RRTConnect time and trajectory simplification time. Meanwhile, the baseline's total planning time includes the RRTConnect time, path simplification time, and TOPP-RA time. As our trajectory and the baseline's are optimized for different cost functions, we use their length as a common metrics, similar to Sec. VII-A. As TOPP-RA \[pham2018toppra\] only fits a time-parameterized trajectory to geometric path, *i.e.*, a sequence of waypoints, it does not consider any collision avoidance constraints. While the geometric path is collision-free, there is no guarantee that the time-parameterized trajectory from TOPP-RA will be valid. Therefore, we sample the resulting trajectories, check for collision and compare the collision risk, measured by the percentage of collided trajectories.

Table II compares our kinodynamic planner and the baseline, in terms of the total planning time, the final trajectory's length, and the collision risk, for each environment and overall. On average, we are able to generate a valid trajectory in around $3.5ms$, and in less than $1ms$ for $75\%$ of the problems, while the baseline's total planning time is consistently around $4.5ms$ for almost all problems. While VAMP can generate a collision-free geometric path fast, the baseline's total planning time is dominated by the TOPP-RA time. Our approach, instead, spends most of the time in the FLASK-RRTConnect planner, as we directly enforce the dynamics constraints in the RRT tree construction. Across all the problems, the baseline offers a shorter trajectory but, more importantly, poses a collision risk of $\sim {30\%}$ on average, highlighting the benefit of our approach with guarantees of collision-free trajectories up to the sampling resolution. Fig. 6 visualizes the trajectories from our FLASK-RRTConnect (top) with no collisions and from the baseline (bottom) with collided configurations (red).

For the *table under pick* and *table pick* environments, our total planning time is approximately $\sim 15$ times faster than that of the baseline, while maintaining $\sim 4$ times shorter time for the *box*, *bookshelf thin* and *bookshelf tall* environments. For the *bookshelf small* and *cage* environments, our approach is slightly slower on average. Yet, it is still $\sim 8$ times faster for $75\%$ of the *bookshelf small* problems, suggesting that there are certain challenging cases in those environments that our approach takes slightly longer than the baseline to plan, but still achieves milliseconds of planning time. We emphasize that even though the baseline can be faster in those cases, it still leads to a significant risk of collision, around $30\%$ of the *bookshelf small* and *cage* problems, as shown in Table II.

### VII-C Real experiments

Finally, we verify the benefit of our approach for online motion planning on a real Universal Robots (UR5) platform in a cluttered environment. The environment consists of multiple static and dynamic objects, perceived by an Intel Realsense camera with a top-down view. The depth image from the camera is used to generate a set of spheres stored in a collision-affording point tree (CAPT) compatible with simd-parallelized motion planning \[ramsey2024-capt\]. The spheres represent the obstacles in the environment in our Alg. 3. Our FLASK-RRTConnect planner in Sec. VII-A is used to find a trajectory from the start configuration to the goal.

### VII-C1 Kinodynamic Planning versus Geometric Planning

We first consider a "*pick and place*" scenario in Fig. 1, where the robot generates a motion plan from its start position to a *"pick"* position near a granola box, and then move to a *"place"* position above a basket. The environment is cluttered with multiple objects, creating narrow passages such that a minor deviation from the planned trajectory can cause collisions. Therefore, accurate tracking is crucial for the safe realization of this "*pick and place*" task. The baseline is a geometric path, generated by a SIMD-parallelized RRTConnect planner from VAMP \[thomason2024vamp\]. The path is sampled with a constant open-loop velocity, chosen such that the task's duration is similar to ours for a fair comparison. A closed-loop velocity control input is computed by Ruckig \[berscheid2021ruckig\] and sent to the UR5 robot to execute.

Fig. 7 plots the tracking error during the experiments. Our trajectory is dynamically feasible, allowing the robot to smoothly and accurately execute the task without any collisions (Figs. 7(a) and 8(a) ‣ Fig. 8 ‣ VII-A1 Comparison to the baselines ‣ VII-A Kinodynamic planning for low-dof systems ‣ VII Evaluation ‣ Ultrafast Sampling-based Kinodynamic Planning via Differential Flatness")). Meanwhile, the geometric path has sharp turns, leading to overshoots and fluctuations (Fig. 7(b)). As a result, the robot collides with two nearby boxes while trying to turn, as seen in Fig. 8(b). The overshoots can be observed in Fig. 7(c) with two spikes in total tracking error $\|{\mathbf{q}_{actual} - \mathbf{q}_{desired}}\|$, at times $t \approx 4$s and $t \approx 9$s, where $\mathbf{q}_{actual}$ and $\mathbf{q}_{desired}$ denote the actual and desired values of the joint angles from the motion plans. Meanwhile, our tracking error stays low without any spikes, highlighting the benefits of having a dynamically feasible trajectory from our kinodynamic planner for accurate task executions.

Figure 9: Reactive planning with moving obstacles: our UR5 robot successfully performs a “pick, place, and reset” loop with our FLASK-RRTConnect planner without colliding with any of the static or moving obstacles. The obstacles are observed by an overhead Intel Realsense camera.

Figure 10: Planning and simplification time in our “pick, place, and reset” loop: our planner takes ∼ 90 μ s and ∼ 40 μ s for planning and simplification, respectively, illustrating the reactiveness of our approach for real-time applications.

### VII-C2 Reactive Kinodynamic Planning

To examine the reactiveness of our kinodynamic planning approach, we consider a "*pick, place, and reset*" loop, where the robot keeps planning its trajectory to perform a "*pick*" action near a pile of blocks, a "*place*" action above the basket, and then "*reset*" to its original configuration. During the experiment, we move a foam obstacle in the environment and verify that our kinodynamic motion planner is able to quickly react to object changes and safely achieve the task as shown in Fig. 9. On average, our kinodynamic planner takes $\sim {90\mus}$ to plan and $\sim {40\mus}$ to simplify the trajectory (Fig. 10), leading to a total planning time of $0.13ms$. The results illustrate that our approach is fast and suitable for online and reactive planning with dynamic environments, while satisfying the dynamics constraints.

## Conclusions

This paper develops FLASK, an ultrafast sampling-based kinodynamic planning framework, by solving the two-point boundary value problem and dynamics propagation in closed forms for a common class of differentially flat robot platforms, and performing extremely fast forward kinematics and collision checking via simd parallelism, available on most consumer CPUs. Our approach is exact, general and can be applied to any sampling-based planners while offering theoretical guarantees on probabilistic exhaustivity and asymptotic optimality. It is able to generate a dynamically feasible trajectory in the range of microseconds to milliseconds, which is suitable for online and reactive planning in dynamic environments. Our method outperforms common sampling-based and optimization-based kinodynamic planners as well as time-parameterization of a geometric path in terms of planning times, offering a fast, reliable, and feasible solution for trajectory generation.

Our approach unfolds a promising and exciting research area where it is possible to transform existing sampling-based motion planners with theoretical guarantees into fast kinodynamic versions while only requiring general-purpose and widely available CPUs. As we have closed-form BVP solutions for a large class of nonlinear differentially flat systems, we can largely bypass the propagation-based planners and can even enable kinodynamic planning in challenging settings, e.g., with graph-based planners. This ability potentially can lead to a wide application of our method on different robots, in different settings, and for various tasks. Our method can quickly bootstrap optimization-based planners with quality and dynamically feasible initial solutions, especially when their objective function differs from our cost. Moreover, the ability to specify a duration for our trajectory offers an exciting potential integration task and motion planning with temporal constraints such as task deadlines.
