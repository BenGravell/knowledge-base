<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

db-A*: Discontinuity-bounded Search for Kinodynamic Mobile Robot Motion Planning

Topics include Trajectory optimization, Motion planning, Robotics, Graphs, Benchmarks, Sampling-based methods, Generalization, Optimization, Planning, Sampling, Mobile robots.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider time-optimal motion planning for dynamical systems that are translation-invariant, a property that holds for many mobile robots, such as differential-drives, cars, airplanes, and multirotors. Our key insight is that we can extend graph-search algorithms to the continuous case when used symbiotically with optimization. For the graph search, we introduce discontinuity-bounded A* (db-A*), a generalization of the A* algorithm that uses concepts and data structures from sampling-based planners. Db-A* reuses short trajectories, so-called motion primitives, as edges and allows a maximum user-specified discontinuity at the vertices. These trajectories are locally repaired with trajectory optimization, which also provides new improved motion primitives. Our novel kinodynamic motion planner, kMP-db-A*, has almost surely asymptotic optimal behavior and computes near-optimal solutions quickly. For our empirical validation, we provide the first benchmark that compares search-, sampling-, and optimization-based time-optimal motion planning on multiple dynamical systems in different settings.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Compared to the baselines, kMP-db-A* consistently solves more problem instances, finds lower-cost initial solutions, and converges more quickly.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning for robots with known kinodynamics remains challenging, especially when a time-optimal motion is desired. Consider the example in Fig. 1 of a simple dynamical model in 2D (unicycle, 3-dimensional state space and 2-dimensional control space). Finding the time-optimal solution is surprisingly challenging for state-of-the-art methods when constraining the control space to model a plane with a malfunctioning rudder, i.e., with a positive minimum speed and asymmetric angular velocity limits.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Current planning approaches are sampling-based, search-based, optimization-based, or hybrid. Each of these methods has their strengths and weaknesses. Sampling-based planners can find initial solutions quickly and have strong guarantees for convergence to an optimal solution. However, in practice the initial solutions are far from the optimum, the convergence rate is low, and the solutions typically require some post-processing. Search-based approaches can remedy those shortcomings by connecting precomputed trajectories, so-called *motion primitives*, using A\* or related graph search algorithms. Yet, the seemingly strong theoretical guarantees only hold up to the selected discretization of the state space and the precomputed motions. Moreover, scaling this approach to higher dimensions has proved difficult and requires careful, frequently hand-crafted design of the motion primitives. This curse of dimensionality can be overcome by optimization-based planners, which scale polynomially rather than exponentially with the number of state dimensions. However, these planners are, in the general case, only locally optimal and thus require a good initial guess both for the trajectory and time horizon.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present a new approach for kinodynamic motion planning of mobile robots that combines key ideas and strengths of the aforementioned previous methods. We rely on a graph-search method, because it provides a theoretically grounded exploration/exploitation tradeoff, but we want to remedy its primary shortcoming of a predefined discretization, similar to sampling-based planning. The naive approach of simply increasing the number of primitives is intractable, due to the resulting infinite number of states and infinite branching factor. We solve this challenge with a combination of bounded-discontinuity search with nonlinear optimization. Introducing the discontinuity makes the search tractable: we can reuse the primitives and have a finite number of states to expand. While the resulting trajectory is not feasible, it can be used as initial guess of trajectory optimization that locally repairs the discontinuous trajectory into a valid trajectory. We execute search and optimization in an iterative fashion, where the value of the discontinuity bound decreases in every iteration. For large bounds, the search is very fast, but the optimizer might fail to find a valid solution.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

For very small bounds, the search requires a longer runtime, but the optimizer has an excellent initial guess. This combination results in an efficient anytime planner with probabilistic optimality guarantees.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

More specifically, our first contribution is the introduction of *kMP-db-A\**, a new kinodynamic motion planner that combines a novel search algorithm, discontinuity-bounded A\* (db-A\*), and trajectory optimization in an iterative fashion. Db-A\* generalizes A\* with ideas from sampling-based planning to obtain solution trajectories that may have discontinuities up to a user-specified bound. Our second contribution is the, to our knowledge, first benchmark that compares the three major kinodynamic motion planning techniques on the same problem instances with the identical objective of computing time-optimal trajectories. While we focus in our evaluation on the challenging case of time-optimality, our approach supports arbitrary cost functions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Description", "weight": 1.0} -->

We consider a robot with state $\mathbf{x} = {\lbrack\mathbf{x}^{t},\mathbf{x}^{r}\rbrack} \in \mathcal{X} \subset {{\mathbb{R}}^{d_{w}} \times {\mathbb{R}}^{d_{x} - d_{w}}}$, where the first $d_{w}$ dimensions indicate the translation in the workspace ($d_{w} \in {\{ 2,3\}}$) of the robot and the remaining $d_{x} - d_{w}$ dimensions may contain orientation or derivatives. The robot can be actuated by controlling actions $\mathbf{u} \in \mathcal{U} \subset {\mathbb{R}}^{d_{u}}$. We consider dynamics that are *translation invariant*, with

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Description", "weight": 1.0} -->

where $\mathbf{f}$ only depends on $\mathbf{x}^{r}$ and not on $\mathbf{x}^{t}$. In order to employ gradient-based optimization, we assume that we can compute the Jacobian of $\mathbf{f}$ with respect to $\mathbf{x}^{r}$ and $\mathbf{u}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Description", "weight": 1.0} -->

Almost all generic kinodynamic motion planners assume a discrete-time formulation with zero-order hold, i.e., the applied action remains constant during a timestep. We can then frame the dynamics Eq. 1 as

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Description", "weight": 1.0} -->

using a small timestep $\Deltat$ so that the Euler approximation holds sufficiently well.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Description", "weight": 1.0} -->

where $\mathbf{x}_{s} \in \mathcal{X}$ is the start state and $\mathbf{x}_{f} \in \mathcal{X}$ is the goal state. The objective function $J$ is application specific; we will focus on time-optimal trajectories, i.e., ${J{(\mathbf{U},\mathbf{X},T)}} = {T\Deltat}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Example 1", "weight": 1.0} -->

Consider a unicycle robot with state $\mathbf{x} = {\lbrack x,y,\theta\rbrack} \in \mathcal{X} = {SE{}} \subset {{\mathbb{R}}^{2} \times {\mathbb{R}}^{1}}$, i.e., $x,y$ are the position and $\theta$ is the orientation. The actions are $\mathbf{u} = {\lbrack v,\omega\rbrack} \in \mathcal{U} \subset {\mathbb{R}}^{2}$, i.e., the speed and angular velocity can be controlled directly. The dynamics are translation invariant: $\overset{˙}{\mathbf{x}} = {\lbrack{v{\cos\theta}},{v{\sin\theta}},\omega\rbrack}$. The choice of $\mathcal{U}$ can make this low-dimensional problem challenging to solve.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Example 1", "weight": 1.0} -->

For example, Fig. 1 shows a plane-like case (positive minimum speed, i.e., $0.25 \leq v \leq {0.5\ {m/s}}$) with a malfunctioning rudder (asymmetric angular speed, i.e., ${- 0.25} \leq \omega \leq {0.5\ {{rad}/s}}$).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Approach", "weight": 1.0} -->

Our general approach is shown in Algorithm 1. We assume that we have access to a set of *motion primitives*, which are valid trajectories according to our dynamics.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A db-A\\*: Discontinuity-bounded A\\*", "weight": 1.0} -->

In the following, we rely on a user-specified *metric* $d:{{\mathcal{X} \times \mathcal{X}}\rightarrow{\mathbb{R}}}$, which measures the distance between two states. This is analogous to sampling-based planners, and we assume that $\langle\mathcal{X},d\rangle$ is a metric space in order to use efficient nearest neighbor data structures, such as k-d trees.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Db-A\* is incomplete and suboptimal if $\delta > 0$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-B Kinodynamic Optimization", "weight": 1.0} -->

Here, $\mathbf{x}_{{l - k}:l}$ denotes the sequence $\mathbf{x}_{l - k},\mathbf{x}_{{l - k} + 1},\ldots,\mathbf{x}_{l}$ and the inequality constraints $\mathbf{g}_{l}$ and equality constraints $\mathbf{h}_{l}$ only depend on the current and up to $k$ prior states. This $k$-order Markov assumption allows us to solve the nonlinear optimization problem efficiently e.g., using the augmented Lagrangian method, because $k$ is typically small (1 to 3).

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-B Kinodynamic Optimization", "weight": 1.0} -->

When using the Euler approximation in Eq. 2, we can transform Eq. 3 for a given $T$ into Eq. 6 by encoding the dynamics, start, and goal constraints using $\mathbf{h}_{l}$ and the action and state constraints into $\mathbf{g}_{l}$. Since $\mathbf{U}$ is not a decision variable in this formulation, the dynamics constraint has to be encoded by using state constraints or by augmenting the state space. We note that if $T$ and $\Deltat$ are fixed and $J = {T\Deltat}$, we can use any $\hat{J}$ to optimize in the nullspace of $J$. This allows us to include arbitrary regularization terms (in our case, smoothness) to guide the optimization and improve the convergence and success rate of the optimizer.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Kinodynamic Optimization", "weight": 1.0} -->

Some optimization methods may refine the given $T_{d}$ in Algorithm 1 of Algorithm 1 either by adding $\Deltat$ as an optimization variable (which introduces additional nonlinearities), or by applying a linear search over multiple potential values of $T$ that are around $T_{d}$, e.g., $T \in {\langle{0.8T_{d}},T_{d},{1.2T_{d}}\rangle}$. We use the latter approach for Algorithm 1.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Kinodynamic Optimization", "weight": 1.0} -->

When no estimate of $T$ is available, we can use a linear search over $T$. For some dynamics, e.g., differentially-flat systems, it is also possible to use a modified binary search, where the first exponential search identifies an upper bound and the following binary search finds the optimal $T$. We use the latter approach for our baseline.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-C Motion Primitive Generation", "weight": 1.0} -->

Instead of sampling control sequences at random, we solve two-point boundary value problems with random start and goal configurations in free space with nonlinear optimization, which results in a superior primitive distribution. Specifically, we generate motion primitives offline using the following steps. First, random sampling of a start and goal configuration in free space; second, solving Eq. 6 using linear search over $T$; and third, splitting the resulting motion into multiple pieces of a desired length. We sort the primitives using an iterative greedy method that approximately minimizes the dispersion. Let $\mathcal{M}$ be the set of all motions, $\mathcal{M}_{s}$ be the set of sorted motions, and $\mathcal{M}_{r} = {\mathcal{M} \smallsetminus \mathcal{M}_{s}}$ be the set of remaining motions.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-C Motion Primitive Generation", "weight": 1.0} -->

We initialize $\mathcal{M}_{s} = {\{{{\operatorname{argmax}_{m \in \mathcal{M}}d}{(m^{0},m^{f})}}\}}$, where $m^{0}$ refers to the initial state of the motion and $m^{f}$ to the final state of the motion. Then, we add an element to $\mathcal{M}_{s}$ in each iteration selected by

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-C Motion Primitive Generation", "weight": 1.0} -->

Thus, we pick the motion in each iteration that maximizes the minimum distance to other, already picked motions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-C Motion Primitive Generation", "weight": 1.0} -->

For AddPrimitives we add motions from the precomputed sequence $\mathcal{M}_{s}$. Additional motions can be generated online using the same procedure.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-C Motion Primitive Generation", "weight": 1.0} -->

Instead of letting users manually specify $\delta$, we use the automatic procedure ComputeDelta, which estimates $\delta$ given a desired branching factor $b_{d}$. First, we initialize a k-d tree $\mathcal{T}_{m}$ of all motions, as in Algorithm 2 of Algorithm 2. Second, we randomly sample a state $\mathbf{x}_{rand}$. Third, we use $\mathcal{T}_{m}$ to find the $b_{d}$-closest motions that could be applied from $\mathbf{x}_{rand}$. Fourth, we record the distance $\delta_{r} = {{\max d}{(m,\mathbf{x}_{rand})}}$, where $m$ is one of the $b_{d}$-closest motions. The estimated value of $\delta$ is the average over multiple $\delta_{r}$ values. This procedure reduces $\delta$ as the number of motion primitives increases in expectation and is easy to tune at the same time.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-C Motion Primitive Generation", "weight": 1.0} -->

Motion primitives can also be extracted online in Algorithm 1. The ExtractPrimitives procedure uses the output of the optimization regardless of the constraint satisfaction and works as follows. First, intervals of valid sub-trajectories are computed by checking if all the constraints are fulfilled. Longer intervals can be split up as in the offline computation. The resulting primitives can be particularly useful for the planning problem at hand, because they are computed using the full knowledge of the environment.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-D Properties", "weight": 1.0} -->

We conjecture that the approach in Algorithm 1 will eventually compute the optimal solution, because as the number of iterations $n$ increases, we add more primitives $\mathcal{M}$, which, by definition of ComputeDelta, reduces $\delta$. Thus, as $n\rightarrow\infty$, we have $\delta\rightarrow 0$. For $\delta = 0$, db-A\* as described in Algorithm 2 becomes regular A\*, which is known to be complete and optimal. The major flaw of this argument is that, in the limit, we also have an infinite number of motion primitives and thus an infinite branching factor.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-D Properties", "weight": 1.0} -->

Formally, we can follow \[6, Th. 3\] to establish almost surely asymptotic optimality (which also implies probabilistic completeness) under the assumption that we have a non-zero probability of our Optimization method to find a solution if one exists. This assumption is justified by the fact that the nonlinear trajectory optimization has a region of attraction $\Delta > 0$ and for small $\delta > 0$ our initial guess will fall in this region of attraction, allowing the optimization method to eventually compute a solution if one exists.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We compare different motion planners, including ours, on the same problem scenarios. For fair comparison, we share code and data structures as much as possible, use the respective state-of-the-art open-source implementations, and focus on settings where the dynamics and not the collision-checking create challenges.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-A Dynamical Systems", "weight": 1.0} -->

Unicycle ($1^{\text{st}}$ order) has a 3-dimensional state space ${\lbrack x,y,\theta\rbrack} \in {SE{}}$ and a 2-dimensional ${\lbrack v,\omega\rbrack} \in \mathcal{U} \subset {\mathbb{R}}^{2}$ control space with dynamics defined in \[30, Eq. (13.18)\]. The simplest version (v0) uses bounds $v \in {{\lbrack{- 0.5},0.5\rbrack}{m/s}}$ and $\omega \in {{\lbrack{- 0.5},0.5\rbrack}{{rad}/s}}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-A Dynamical Systems", "weight": 1.0} -->

More interesting variants are a plane-like version (v1) using a positive minimum speed of $0.25\ {m/s}$, and a plane-like version with a rudder damage (v2) ($\omega \in {{\lbrack{- 0.25},0.5\rbrack}{{rad}/s}}$).

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A Dynamical Systems", "weight": 1.0} -->

Car with trailer has a 4-dimensional state space ${\lbrack x,y,\theta_{0},\theta_{1}\rbrack} \in \mathcal{X} \subset {\mathbb{R}}^{4}$, a 2-dimensional ${\lbrack v,\phi\rbrack} \in \mathcal{U} \subset {\mathbb{R}}^{2}$ control space, and dynamics and visualization given in \[30, Eq. (13.19), Fig. 13.6\]. We add an additional constraint ${|{\angle{(\theta_{0},\theta_{1})}}|} < {\pi/4}$ that avoids that the angle between the car and the trailer exceeds a threshold.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A Dynamical Systems", "weight": 1.0} -->

Quadrotor has a 13-dimensional state space (pose and first order derivatives using a Quaternion representation), a 4-dimensional control space (force for each of the four motors), and dynamics defined in \[31, Eq. \]. We use the parameters of the Crazyflie quadrotor with limits on the motor forces, velocity, and angular velocity. Note that the low thrust-to-weight ratio of $1.4$ is very challenging for kinodynamic motion planning and that problem settings with a harsh initial condition prevent the use of specialized methods.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-A Dynamical Systems", "weight": 1.0} -->

We use ${\Deltat} = {0.1\ s}$ for all dynamical systems except the quadrotor, which uses ${\Deltat} = {0.01\ s}$ due to the fast rotational dynamics.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-B Environments", "weight": 1.0} -->

For most of the dynamical systems, we consider three environments (see Fig. 2), which are inspired by the common use-cases in the related literature. For the v2 unicycle, we use the *wall* environment as shown in Fig. 1. For the quadrotor, we use an *empty* environment without obstacles. The scenario requires the quadrotor to recover from a harsh initial condition with an upside-down initial rotation and nonzero initial first derivatives. All environments only use simple geometric box shapes for efficient collision checking. The environments are bounded, where the bounds only limit the translational part of the state, i.e., parts of the robots are allowed to be outside. One such example is visible in the park solution of Fig. 2.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-C Algorithms", "weight": 1.0} -->

For a search-based approach, we rely on SBPL^11^1 (Search-based Planning Library), a commonly used C++ library with integration in the Robot Operating System (ROS). SBPL contains an example for unicycles, although the used dynamics do not match the ones from \[30, eq. 13.18\]. Thus, we generate our own primitives using the formulation in Section IV-B. Moreover, we make minor adjustments to the heuristic to enable time-optimal anytime planning using the provided implementation of ARA\* in SBPL. Due to limits in SBPL^22^2The official documentation states: "\[For custom scenarios\], you will have to implement your own environment (a very involved topic that might be covered in the future)." we limit our evaluation to the v0 first order unicycle.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-C Algorithms", "weight": 1.0} -->

For a sampling-based approach, we rely on OMPL (Open Motion Planning Library), a widely used C++ library with integration in ROS through MoveIt. OMPL implements several kinodynamic planners, including SST\*, which we use. As part of this work, we contribute minor changes to allow time as an optimization objective. Since sampling-based kinodynamic approaches cannot reach a goal state, we use a goal region instead that we verify to be small enough such that an optimizer can find an exact solution.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-C Algorithms", "weight": 1.0} -->

For an optimization-based approach, we rely on RAI^33^3 (Robotic AI), a C++ library that implements KOMO and nonlinear optimization algorithms. For each of the dynamical systems, we implement the appropriate constraints and their derivative computation. In case of the trailer and the quadrotor, we add parts of the actions as decision variables (angle $\phi$ and motor forces, respectively); otherwise the decision variables are the state sequences only. As an initial guess, we use a geometric solution as found by RRT\* of OMPL. We then use the modified binary search method as outlined in Section IV-B. This combination of *geometric RRT\*+KOMO* is anytime like the other approaches we compare to.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-C Algorithms", "weight": 1.0} -->

For db-A\*, we implement Algorithm 2 in C++ using the data structures provided in OMPL to represent states and for nearest neighbor computation. Algorithm 1 is implemented in Python that executes C++ binaries for subroutines when necessary. As heuristic $h$, we use Euclidean distance divided by the upper bound of the speed. For the AddPrimitives function, we precompute $10\, 000$ motion primitives for most dynamical systems ($30\, 000$ for the quadrotor) and only add a subset per iteration. Generating the primitives took about $8\ h$ per dynamical system utilizing all CPU cores.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-C Algorithms", "weight": 1.0} -->

The benchmark infrastructure is written in Python and all tuning parameters can be found in the open-source repository^44^4 Collision checking is done using FCL (Flexible Collision Library) in all cases. All approaches use the Euler integration Eq. 2, although KOMO uses an implicit formulation by design.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-D Benchmark", "weight": 1.0} -->

We execute our benchmark on a desktop computer with AMD Ryzen 9 3900X ($3.8\ {GHz}$) and $32\ {GB}$ RAM. Our results are summarized in Table I.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-D Benchmark", "weight": 1.0} -->

We summarize the main results as follows. SBPL can compute results very quickly and consistently. The initial solution quality is very high, but due to the limited number of primitives, the solution does not improve much over time (rows 1 -- 3, Table I). The approach is not as general as the other ones, and we were unable to use it for all of our dynamical systems. SST\* can find an initial solution very quickly; however the solution quality is initially poor, especially with higher-dimensional systems (rows 6--11). The convergence is slow -- our $5\ \min$ timeout was not sufficient for SST\* to fully converge in any of the cases. Geometric RRT\*+KOMO can find near-optimal initial solutions, but does not work well in instances that require long trajectories and fails if the geometric initial guess is not close to a dynamically feasible motion. For example, finding an initial solution in the kink and bugtrap examples (rows 7, 8) took significantly longer than parallelpark.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-D Benchmark", "weight": 1.0} -->

Another drawback is that this approach is incomplete, as visible for the v1 and v2 unicycle systems (row 4 and 5) and not globally optimal, e.g., row 10 and 11 show a very poor solution quality after $5\ \min$. kMP-db-A\* converged to the lowest-cost solution during the time limit in all cases. At the same time, it found the highest-quality first solution in all cases, although it often took more time to compute an initial solution than the other algorithms. We found that this is mostly caused by the challenging scenario of time-optimal planning: most motion primitives are time-optimal, i.e., result in bang-bang control. When allowing discontinuities, the estimated time horizon is often too short for the optimizer to find a solution, requiring multiple iterations in Algorithm 1 to report the first solution.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-D Benchmark", "weight": 1.0} -->

For brevity, Table I does not include any standard deviation. In general, we found that SBPL has almost no variance, SST\* has a very high variance, and KOMO and kMP-db-A\* are somewhere in between the two extremes. One example that includes the convergence behavior as well as the variance is shown in Fig. 3.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-D Benchmark", "weight": 1.0} -->

The runtime of the individual components of kMP-db-A\* can vary widely, depending on $\delta$. For example, in the bugtrap example for the trailer (row 11) it takes around $2\ s$ for db-A\* to find a solution with $\delta = 0.33$ and $14\ s$ for the optimization, while during later iterations db-A\* requires $46\ s$ ($\delta = 0.12$) and the optimization only $6\ s$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We present a new kinodynamic motion planning technique, kMP-db-A\*, that uses a novel graph-search method with trajectory optimization in an iterative fashion. For the graph search, we introduce db-A\*, a generalization of A\* that reuses motion primitives to compute trajectories with a bounded discontinuity. Then, we warm-start trajectory optimization using the output of the graph search and compute new motion primitives online. KMP-db-A\* combines ideas and advantages of sampling-based, search-based, and optimization-based kinodynamic motion planners: it converges asymptotically to the optimal solution, directly solves for the time horizon, finds a near-optimal solution quickly, and does not require any additional post-processing.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The major limitation of kMP-db-A\* is that it sometimes requires a long time to compute an initial solution. We believe that this is not a fundamental issue and that it can be improved using the following techniques in the future. First, we are interested in using stronger heuristics and bounded suboptimal and incremental graph search techniques to reuse information between iterations. Second, we plan to investigate the use of optimizers that do not operate over the full trajectory time horizon. Finally, we believe that our work also lays the foundation for novel kinodynamic multi-robot motion planners.
