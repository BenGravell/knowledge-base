<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

cuRobo: Parallelized Collision-Free Minimum-Jerk Robot Motion Generation

Topics include Motion planning, Trajectory optimization, Compute unified device architecture, Graphics processing unit, Parallelized, Inverse kinematics, Robot manipulation, Open source, Software.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

CUDA-accelerated library for collision-free robot motion generation. Formulates trajectory generation as a global optimization problem solved across thousands of parallel seeds on GPU. Combines L-BFGS with a novel parallel noisy line search and particle-based optimization to produce minimum-jerk, collision-free trajectories within ~50ms. Also includes a parallel geometric planner (~20ms) and a batched IK solver (>7000 queries/s). An earlier version without minimum-jerk optimization was published at ICRA 2023.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper explores the problem of collision-free motion generation for manipulators by formulating it as a global motion optimization problem. We develop a parallel optimization technique to solve this problem and demonstrate its effectiveness on massively parallel GPUs. We show that combining simple optimization techniques with many parallel seeds leads to solving difficult motion generation problems within 53ms on average, 62x faster than SOTA trajectory optimization methods. We achieve SOTA performance by combining L-BFGS step direction estimation with a novel parallel noisy line search scheme and a particle-based optimization solver. To further aid trajectory optimization, we develop a parallel geometric planner that is atleast 28x faster than SOTA RRTConnect implementations. We also introduce a collision-free IK solver that can solve over 9000 queries/s. We are releasing our GPU accelerated library CuRobo that contains core components for robot motion generation. Additional details are available at sites.google.com/nvidia.com/curobo.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Safe navigation is fundamental to robotics, requiring robots to have a robust global motion generation system to traverse any environment structure encountered at deployment. Motion generation for high-dimensional systems is extremely challenging as satisfying complex constraints and minimizing cost terms in a very large C-Space is computationally expensive. Manipulators, for instance, can have many articulations, complex link geometries, entire goal regions beyond a single configuration, task constraints, and nontrivial kinematic and torque limitations. There has been a long history of problem decomposition in this field to mitigate complexity, leading to standard approaches that often first plan collision-free geometric paths and then smooth those paths for dynamic efficiency. But increasingly, research into the interconnections between optimization and planning has shown that optimization can be a powerful tool well beyond trajectory smoothing, and trajectory optimization alone now has a breadth of applications. Our modern understanding of this robot navigation problem is that it is a large *global* motion optimization problem.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The global optimization literature suggests that finding the true global minimum is usually impractical, but strategies for robustly finding high-performing local minima can be effective. Many strategies follow the simple pattern of selecting many seed candidates and performing a local optimization for each. This sample and optimize process can often realize substantial gains by leveraging distributed computation. However, most motion generation systems today remain sequential and slow, following a CPU-based design. State-of-the-art motion generation solutions take 0.5s to 10s depending on the task's complexity on modern CPUs. This run-time is even slower on edge devices that operate under limited power budgets. This slow and sequential process has resulted in pipelined systems that compute only a single best candidate seed, which is then passed to an optimizer for local optimization. Such systems fundamentally limit their ability to find better local optima by betting on a single seed.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The insights used to improve the speed and quality of the solution for global optimization problems may apply well to the problem of global motion generation. In this work, we present a collection of techniques and implementations that leverage parallel processing to accelerate motion planning and optimization, and for running many optimization instances in parallel to robustly address these global optimization problems. Existing literature supports these algorithmic principles and has shown that the heuristic initialization for the problem can be effective, and many restarts with randomized noise of the initial seed can dramatically improve performance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the realm of global motion generation, massively parallel compute is already being used to accelerate Probabilistic Road Map (PRM) pruning by using an FPGA with special circuits, leading to many orders of magnitude speedup. However, instead of designing special circuits for motion generation, we leverage the massively parallel compute available on graphical processing units (GPUs). GPUs have become pervasive in both high- and low-powered configurations as they offer energy-efficient and high-throughput computation platforms, an important requirement for solving parallelizable compute intensive problems. We show how GPUs also offer programmability and flexibility to map sophisticated computations of motion optimization to hardware, allowing us to parallelize the entire motion generation pipeline. We achieve high speedups using GPUs compared to serial implementations in motion generation. While we demonstrate the benefits of using parallel compute for motion generation using NVIDIA GPUs, the approach is applicable to other parallel architectures.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our effort to solve global motion generation starts with parallelizing the core blocks in a robotics stack -- robot kinematics, robot self signed distance (i.e., between a robot's links), and robot world signed distance (i.e., world represented by cuboids, meshes, and a depth camera stream). We formalize these functions to use many threads per query, implement them efficiently in CUDA, and provide them as differentiable functions in pyTorch, enabling others to also use these functions as the backbone for their own robotic tasks. We then formulate a continuous collision checking algorithm that only requires a point signed distance function from the world representation. We then introduce parallel algorithms for numerical optimization and geometric planning, that aid in solving global motion generation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our main contributions are summarized as follows:\
Performant Kinematics and Signed Distance Kernels: We develop high-performance CUDA kernels for robot kinematics and signed distance computation which are up to 10,000x faster than existing CPU based methods.\
Differentiable Continuous Collision Checking: Formulate continuous collision checking algorithm that only needs a point signed distance function (and closest point for gradients) to perform swept collision checks, enabling use across different world representations from primitives and meshes to occupancy maps.\
Parallel Optimization: We develop a GPU batched L-BFGS optimizer, that uses an approximate parallel line search scheme, and a particle-based optimizer to solve difficult motion generation problems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our solver is 23$\times$, 80$\times$, and 87$\times$ faster for inverse kinematics, collision-free inverse kinematics, and collision-free trajectory optimization respectively when compared to existing CPU based solvers.\ SOTA IK Solver: Leveraging our performant kernels, we have developed a world-leading inverse kinematic solver, that can solve 37000 IK problems per second (23$\times$ faster than TracIK ) and also solve 7600 collision-free IK problems per second (80$\times$ faster than using TracIK + Bullet ).\ Parallel Geometric Planner: We develop a geometric planner with a parallel steering algorithm to generate collision-free paths within 20 ms on a modern desktop machine with NVIDIA RTX 4090 and AMD Ryzen 9 7950x.\ Global Motion Generation: Combining our above contributions, we have a global motion generation pipeline that can plan within 50ms, 60$\times$ faster than existing methods (Tesseract).\ Validation on a Low-Power Device: We evaluate our GPU-accelerated motion generation stack and existing CPU-based methods on an NVIDIA Jetson AGX Orin at

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Results show that our approach is 28$\times$ and 21$\times$ faster on average for motion generation problems when the device was set to 60W and 15W budgets, respectively.\
cuRobo Library: We developed *cuRobo*, a suite of GPU-accelerated robotics algorithms, providing SOTA implementations of robot kinematics, signed distance functions, optimization solvers, geometric planning, trajectory optimization, and model predictive control. We are releasing this library to enrich roboticists with the necessary tools to explore large-scale problems in robotics.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Motion Generation as Optimization", "weight": 1.0} -->

We define the problem of motion generation as the task of moving from an initial joint configuration $\theta_{0}$ to a final joint configuration $\theta_{T}$, at which state a task cost $C{(\theta_{T})}$ is below a desired threshold. Additionally, the transition states from $\theta_{0}$ to $\theta_{T}$ must also satisfy system constraints. In this work, we focus on the task of collision-free motion generation to reach a goal Cartesian pose $X_{g} \in {{\mathbb{S}}{\mathbb{E}}{}}$ with the robot's end-effector. Specifically, we want to obtain a joint-space trajectory $\theta_{\lbrack 0,T\rbrack}$ that satisfies the robot's joint limits (position, velocity, acceleration, jerk), doesn't collide with itself or the environment, and reaches the goal pose $X_{g}$ by the last timestep $T$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Motion Generation as Optimization", "weight": 1.0} -->

We formulate this continuous-time motion problem as a time discretized trajectory optimization problem,

<!-- chunk {"id": "body-0014", "role": "body", "section": "Motion Generation as Optimization", "weight": 1.0} -->

where $C_{smooth}{( \cdot )}$ is a cost term that encourages smooth robot behavior. Joint limit constraints are enabled by Eq.2-5. We also constrain the robot to have zero velocity, acceleration and jerk at the final timestep by constraints in Eq. 6. A detailed discussion on this optimization problem and the formulation of cost terms is available in Appendix. A. We discuss the collision avoidance constraints Eq.7, and Eq.8 in Sec. 3.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Motion Generation as Optimization", "weight": 1.0} -->

A good initial seed can speedup convergence in the above defined trajectory optimization problem. One common way to initialize the seed is to first optimize only for the terminal joint configuration $\theta_{T}$ and then initialize the trajectory with a linear interpolation from the start configuration $\theta_{0}$ to the solved terminal configuration (interpolating through a predefined waypoint has also shown to be helpful ). In our problem setting of reaching a goal pose $X_{g}$, the terminal state optimization problem boils down to a collision-free inverse kinematics (IK) problem containing the pose cost, the collision constraints Eq. 8-Eq. 7 and the joint limit constraint Eq. 2. We hence first solve for collision-free IK, followed by seed generation, and then trajectory optimization. Once we run trajectory optimization, we find an optimal dt by scaling the trajectory's velocity, acceleration, or jerk to the robot's limits and rerun trajectory optimization with this new dt to get the final result (see A.4). Our overall approach is illustrated in Figure 2.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Kinematics & Collision Avoidance", "weight": 1.0} -->

Collision avoidance is a critical component of motion generation as the robot needs to be able to avoid colliding with itself (self-collision) and with the world for safe operation. A standard approach to computing collisions involves transforming the robot's geometries (often represented as meshes) based on the current joint configuration (forward kinematics) and computing mesh-mesh distances. Since we know the geometry of the robot, we can reduce the computation required for collision checking by representing the robot's volume with a set of spheres as shown in Figure 3. With this sphere representation for the robot, our collision avoidance cost terms only need to check the distance between the origin of each sphere and the world, then subtract the radius to get the sphere distance. Similarly, for self collisions, we only have to compute the distance between pairs of spheres (i.e. compute point distance and subtract the radii of the two spheres). This enables our approach to scale to low-power edge devices and also accommodate very large batch queries. We discuss some techniques to approximate a mesh with spheres in Appendix D. We will next discuss how we map between the robot joint configuration and the location of the spheres.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Robot Kinematics", "weight": 1.0} -->

Robot kinematics $K_{s}{( \cdot )}$ enables mapping between a robot's joint configuration and the Cartesian pose (${SE}{}$) of all geometries attached to the robot. This mapping is done by computing a sequence of transformations from the base link of the robot to the different links attached through joints. Each actuated joint adds an additional transformation based on it's value and type. Hence, traversing the robot's kinematic tree by design is sequential for serial manipulators. To overcome the sequential nature of computation, we represent the transformations as homogeneous matrices (4x4), enabling us to use four parallel threads to compute matrix multiplications. Once we build the pose of all links of the robot, we perform matrix vector products to compute the position of the spheres. We also output the pose of the end-effector as a position and quaternion. For computing the backward, we use 16 threads to read and project the gradients from the Cartesian space to the joint space. By using many threads for a single kinematics query, we overcome some of the memory overhead that comes with parallel compute devices.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Robot Kinematics", "weight": 1.0} -->

Our kinematics function supports single axis actuation across all three linear and three angular spaces. Extensive details are available in Appendix E.1. Figure 3-a shows the output of our forward kinematic function, given a joint configuration of the robot.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Self-Collision Avoidance", "weight": 1.0} -->

For avoiding self-collisions, we formulate a distance cost that computes the largest penetration distance between spheres from all links. Since most robots allow for safe contact between consecutive links and some link pairs will never be in collision due to kinematic limits, we build a set of sphere pairs $S$ for which self-collision needs to be checked. We empirically found only 50% of the sphere pairs end up in this collision pair set across many widely used manipulators. We scale the largest penetration distance by a scalar weight $\beta_{1}$. Our self-collision term can be written as,

<!-- chunk {"id": "body-0020", "role": "body", "section": "Self-Collision Avoidance", "weight": 1.0} -->

(a) Sphere representation of Franka Panda
(b) Quadratic collision cost profile

<!-- chunk {"id": "body-0021", "role": "body", "section": "World Collision Avoidance", "weight": 1.0} -->

Generating smooth obstacle avoidance behavior has been studied extensively in the the literature. We highlight common pitfalls in collision-free motion optimization and how our approach overcomes them by leveraging existing techniques and introducing novel contributions below,\
Discontinuity at surface boundary: Discontinuity in the collision cost term near an obstacle surface leads to poor conditioning of the optimization problem, especially when collision cost term is non-convex. To mitigate this issue, we add a buffer distance $\eta$ and change the cost to be quadratic when within $\eta$ distance to the obstacle surface similar to as shown in Fig. 3-(b). This modification of the collision distance $d_{c}$, given the signed distance $d$ can be written as,

<!-- chunk {"id": "body-0022", "role": "body", "section": "World Collision Avoidance", "weight": 1.0} -->

Speeding through obstacles: When a collision cost term only penalizes the position of the sphere, the optimization can attempt to move through obstacles (i.e., high penalty region) very fast to reach a lower cost region compared to being in collision for many timesteps (see our website for a visualization of this phenomenon). To mitigate this issue, we implement a speed metric, similar to, that scales the collision cost of a sphere by it's velocity $\overset{dot}{s}$ (calculated through finite-difference). This encourages the optimization to move around the obstacle instead of speeding through an high penalty region.

<!-- chunk {"id": "body-0023", "role": "body", "section": "World Collision Avoidance", "weight": 1.0} -->

Collision at real-robot execution: Tuning a robot's control box to track a planned kinematic trajectory with millimeter accuracy at high speeds can be very time consuming. In addition, most manufacturers do not provide many parameters to tune their control box. Any Path deviation near obstacles could lead to catastrophic collisions with the world. To be robust to path deviations, we penalize the robot's velocity when within $\eta$ distance to obstacles as robots can track with higher accuracy at slower speeds. This penalization is performed by enabling our speed metric when within $\eta$ distance instead of only enabling at collision. This brings our collision term to $d_{s} = {\overset{dot}{s}d_{c}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "World Collision Avoidance", "weight": 1.0} -->

Collision with thin obstacles: Motion optimization is commonly done by discretizing the trajectory by some timesteps and computing collisions at these timesteps. However, if the trajectory does not have a fine resolution of discretization, collisions with very thin obstacles could be missed. To overcome this issue, we develop a novel formulation of continuous collision checking that only requires a point query signed distance function from the world representation, enabling continuous collision checking with a variety of world representations. We discuss this formulation in the next Section 3.4.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Continuous Collision Checking", "weight": 1.0} -->

Continuous collision checking is a well studied problem, with many methods building a swept volume followed by checking collision between the swept volume and the obstacles. However, collision checking using swept volumes requires the world representation to be able to compute signed distance between complex geometry (i.e., the swept volume) and the obstacles in the world. This is only possible for worlds represented by primitive shapes or meshes. Worlds represented using neural networks or voxels will require special mechanisms to work with swept volumes. To avoid this complexity, we introduce a novel formulation of continuous collision checking that only requires a point signed distance query function from a world representation. We hope that this reduces the barrier for the perception community to deploy their world representations into cuRobo for global collision-free motion generation. Our method is related the iterative method from Bruce and loosely related to the bubbles concept from Quinlan and Khatib. The difference between our approach and Bruce's approach is we not only compute the signed distance but also the gradients. We also formulate the computation to run in parallel threads for each time step in the trajectory.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Continuous Collision Checking", "weight": 1.0} -->

Our continuous collision checking algorithm is illustrated in Fig. 4. Given a trajectory of a sphere discretized by three timesteps $S_{\lbrack 0,1,2\rbrack}$, we first check if the sphere $S_{1}$ is in collision. If it is in collision, we compute the collision cost and move by sphere radius. If it's not in collision, we compute the signed distance to the nearest obstacle and move this distance along the direction of motion between $S_{0}$ and $S_{1}$, which we term as *sweep backward*. If we hit a collision, then we compute the collision cost and then continue sweeping until we reach the midpoint between $S_{0}$ and $S_{1}$. Similarly, we *sweep forward* until midpoint between $S_{1}$ and $S_{2}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Continuous Collision Checking", "weight": 1.0} -->

For every sphere location in the trajectory, we *sweep forward* and *sweep backward* upto the mid distance as this enables our gradient computations to be parallelizable (i.e., gradient for a sphere location does not depend on the collisions at other sphere sweeps).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Continuous Collision Checking", "weight": 1.0} -->

Our implementation of the algorithm assumes that the sphere is moving linearly between waypoints which is not true for links attached through a revolute joint. Empirically, we found that even with this assumption, the optimization was able to find paths in tight spaces. We leave incorporating exact movement path between sphere waypoints for future work and discuss the implementation of this algorithm in Appendix E.3.

<!-- chunk {"id": "body-0029", "role": "body", "section": "World Representation", "weight": 1.0} -->

To compute the world collision cost term, we only require the ability to compute the closest point $c_{r} \in {\mathbb{R}}^{3}$ to a query point and also if the query point is inside or outside an obstacle $s_{r} \in {\lbrack{- 1},1\rbrack}$. These quantities can be obtained from a differentiable point query signed distance function or through geometric processing. We implement three different world representations that output these quantities through geometric processing,

<!-- chunk {"id": "body-0030", "role": "body", "section": "World Representation", "weight": 1.0} -->

: We implement an efficient cuboid query function as we found cuboids to be a common representation for collision avoidance in many real-world deployments. For this world representation, we assume the world is made of only oriented bounding boxes (i.e., cuboids with a ${SE}{}$ pose).

<!-- chunk {"id": "body-0031", "role": "body", "section": "World Representation", "weight": 1.0} -->

: Leveraging NVIDIA warp's bounding volume hierarchy (BVH), which stores mesh's faces and vertices in an accelerated framework for fast closest point and inside/outside queries. This representation assumes the world is represented by watertight meshes.

<!-- chunk {"id": "body-0032", "role": "body", "section": "World Representation", "weight": 1.0} -->

: Third, we write a wrapper to NVIDIA nvblox which integrates Euclidean Signed Distance (ESDF) from truncated Signed Distance Fields (TSDF) streaming from a depth camera. This representation enables us to build a ESDF voxel representation of the world using a depth camera and use this for computing collision distance. This representation assumes that we have access to a depth camera and accurate pose of the camera with respect to the robot's base at each frame for integrating into nvblox.

<!-- chunk {"id": "body-0033", "role": "body", "section": "World Representation", "weight": 1.0} -->

Our implementation of the collision cost also allows for using a combination of the three world representations as we sum over all collisions in the world. In addition to these representations, our robot sphere representation allows for interfacing with other methods that can output a differentiable signed distance. For example, Tang *et al.* integrated a learned SDF representation of the world for collision avoidance in cuRobo.

<!-- chunk {"id": "body-0034", "role": "body", "section": "World Representation", "weight": 1.0} -->

The overall world collision term can be written as,

<!-- chunk {"id": "body-0035", "role": "body", "section": "World Representation", "weight": 1.0} -->

where $\beta_{2}$ scales the cost by a large penalty to act as a soft constraint, $\text{sweep}{( \cdot )}$ computes the collision distance using our continuous collision checking algorithm from Sec. 3.4. The function $\text{smooth}{( \cdot )}$ adds the quadratic smoothing over the collision distance using Eq. 10, which is then scaled by the velocity of the sphere $\text{speed}{( \cdot )}$. We sum this term across all spheres that represent the robot.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Parallel Optimization Solver", "weight": 1.0} -->

There are several techniques to solve the optimization problem defined in Section 2, from particle-based optimization to gradient-based optimization methods. In particular many trajectory optimization methods have approximated hard constraints as soft constraints by treating them as cost terms with large weights to transform the optimization problem from one with nonconvex constraints to a box-constrained nonconvex optimization problem. Motivated by these successes, we also approximate our constraints as cost terms and implement a quasi-newton solver to solve this nonconvex optimization problem.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Parallel Optimization Solver", "weight": 1.0} -->

L-BFGS, a quasi-newton optimization method that can solve very large optimization problems, is a common method shown to achieve superlinear convergence by estimating the Hessian using evaluated gradients. Our optimizers are built around L-BFGS because of its combined performance and relative simplicity that aids parallelization. Gauss-Newton solvers are also ubiquitous and important in robotics, but after an initial exploration we decided to focus our experiments on L-BFGS. Many formulations of Gauss-Newton restrict their presentation to the nonlinear least-squares problem where performance is best understood, but that's unduly restrictive in our setting. These methods can be generalized as a form of natural gradient descent and related formulations of iLQG demonstrate their empirical utility on more general costs using quadratic approximations. However, appropriately leveraging the problem structure within a GPU is not straightforward and the band-diagonal solve commonly used is inherently sequential leaving a number of open questions we would need to resolve. Our benchmarks indicate that even the simpler L-BFGS shows significant improvement over the state-of-the-art when GPU compute is properly leveraged; we leave a full exploration of Gauss-Newton to future work.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Parallel L-BFGS Optimization", "weight": 1.0} -->

Our L-BFGS optimizer has two steps, we first compute the step direction given the current optimization variables $\Theta = \theta_{t \in {\lbrack 0,T\rbrack}}$ and the gradient $\Delta\Theta$ with respect to the sum of the cost terms using the standard L-BFGS steps as described in Nocedal and Wright. Given this step direction $\Delta\Theta$, we perform line search by scaling the step direction with a discrete set of magnitudes $\alpha \in \mathbf{R}^{n}$ and computing the best magnitude from this set using Armijo and Wolfe conditions as shown in Alg. 4.1. Extensive details on our solver is available in Appendix A.7.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Parallel L-BFGS Optimization", "weight": 1.0} -->

Our approach of trying a predefined discrete set of magnitudes instead of iteratively searching for the largest magnitude that satisfies the condition enables us to more effectively use parallel compute as the cost and gradient for the discrete set can be computed in parallel. For the case where none of the values in our discrete set satisfies the line search conditions, we use a very small magnitude (0.01) which acts as a noisy step update. This noisy step update also prevents NaN values in the the step direction computation as there is always a perturbation in the optimization variables between iterations. After every optimization iteration, we update our best estimate as the optimization could diverge due to noisy perturbation in line search. Empirically, we found that the use of a noisy perturbation instead of stopping the optimization when line search fails to find a magnitude that satisfied the conditions greatly increased the convergence rate on trajectory optimization problems as shown in Section 7.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Particle-Based Optimization", "weight": 1.0} -->

To encourage L-BFGS to reach a local optima, we devise a strategy combining particle and gradient-based optimization. This is inspired by strong theoretical results in stochastic gradient Markov Chain Monte Carlo, and sampling-based MPC controllers such as MPPI. In our method, we first run a few iterations of particle-based optimization over the initialization before sending to L-BFGS. Given an initial mean trajectory of joint configurations $\Theta_{\mu} = \theta_{\lbrack 1,T\rbrack}$ and a covariance $\Theta_{\sigma}$, we sample $n$ particles $\theta_{n,{\lbrack 1,T\rbrack}}$ from a zero mean Gaussian and then update $\theta_{n,{\lbrack 1,T\rbrack}} = {\Theta_{\mu} + {\sqrt{\Theta_{\sigma}} \ast \theta_{s}}}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Particle-Based Optimization", "weight": 1.0} -->

We found that the use of particle-based optimization to initialize L-BFGS led to better convergence as empirically validated in Sec. 7. To tackle very hard problems and further reduce the number of seeds required to converge, we develop a parallelized geometric planner that generates collision-free geometric paths between start and goal in the next section.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Parallel Geometric Planner", "weight": 1.0} -->

We develop a geometric planner to generate a collision-free path from the start configuration $\theta_{0}$ to the goal configuration $\theta_{T}$. This generated path is specified by a list of $w$ waypoints $\theta_{\lbrack 0,w\rbrack}$ through which the robot passes in a linear fashion. By studying common geometric planning methods, we found three main components in graph building that can benefit from parallel compute. Specifically, sampling collision-free nodes, finding k nearest nodes in graph, and steering from each sampled node to k nearest nodes. We implement algorithms to perform these tasks in parallel on the GPU in our geometric planner.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Parallel Geometric Planner", "weight": 1.0} -->

Our geometric planner as shown in Alg. 5, first performs heuristic planning by checking if we can steer from start to goal configuration directly or through a predefined retract configuration $\theta_{r}$ (lines 1-7). If this heuristic fails, we sample collision-free configurations $v_{new}$ from an informed search region that samples within $c_{max}$ of the straight line distance between start and goal similar to BIT^∗^ (line 11). We then find the $k_{n}$ nearest neighbours from the existing graph and try to steer from the graph nodes to the new vertices (lines 12-13). We repeat these steps until we find a path with only one waypoint (line 16). Between re-attempts we grow the number of sampled nodes $p_{n}$, the number of nearest neighbours $k_{n}$, and the search region $c_{max}$ to grow the exploration space of the geometric planner (lines 19-21).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Parallel Geometric Planner", "weight": 1.0} -->

To efficiently leverage parallel compute in geometric planning, we develop an algorithm to steer from $s$ vertices $\theta_{s,0}$ in a graph with $s$ sampled new configurations $\theta_{s,k}$ in parallel as described in Alg. 5.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Parallel Geometric Planner", "weight": 1.0} -->

We also implement a shortcut_path function that tries to connect each waypoint with every other waypoint in the path to try to find a shorter path. We leverage this geometric planner to also find paths between a batch of start and goal configurations or from a single start to a goal set. We achieve this by randomly choosing a query index (for which a path does not exist yet) and sampling in this query region to expand the graph (lines 10,11).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Results", "weight": 1.0} -->

We validate and compare our approach to existing methods on two motion planning datasets, the motionbenchmaker dataset containing 800 problems and the mpinets dataset containing 1800 problems. Both datasets contain motion planning problems for the Franka Emika Panda robot, which has 7 actuated joints. The datasets span 12 unique scene types, with each problem starting the robot at a collision-free joint configuration and defining the goal as a desired end-effector pose. A few instances of the motion planning problems from this set is shown in Fig. 5. We provide the planning problems along with code to compute different metrics at github.com/fishbotics/robometrics.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Results", "weight": 1.0} -->

We first analyze the quality of solutions in Section 6.1, then compare compute times in Section 6.2. We also analyze our collision-free inverse kinematics solver in Section 6.2.4, followed by an analysis of our kinematics and distance query modules in Section 6.2.5, as they can also be used independently in other manipulation tasks.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Motion Generation Quality", "weight": 1.0} -->

We focus analysis of motion generation quality to metrics that affect the success rate, and execution time of the computed motions. We compute six different metrics that capture geometric and temporal qualities of the generated trajectories. First, we compute the standard metrics from geometric planning methods, specifically *Success* on a dataset within a given time and *C-Space Path Length* which is the distance traveled by the robot's joints to reach the target pose. In addition, we introduce four metrics that evaluates time parameterization of the generated motions. The *Motion Time* metric compares the trajectory times given the number of trajectory points $n$ and the time $dt$ between waypoints (i.e., ${{({n - 1})} \ast d}t$). If a robot perfectly tracks the planned trajectory, then this *Motion Time* would be the execution time. When moving manipulators at high-speed, they become very sensitive to jerk profiles, especially when starting from or ending at zero velocity (i.e., idle). This has prevented motion generation approaches from executing at the full rated speed of a robot.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Motion Generation Quality", "weight": 1.0} -->

We hence introduce a metric that measures the maximum jerk across the trajectory, which we call *Maximum Jerk* metric. We also measure the *Maximum Acceleration* and *Mean Velocity* across the trajectory to draw further comparisons between methods.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Motion Generation Quality", "weight": 1.0} -->

We compare our method to Tesseract which uses Bullet's continuous collision detector, Open Motion Planning Library (OMPL) for geometric planning, and TrajOpt for trajectory optimization. We use two motion planning methods from Tesseract, one that only performs geometric planning with RRTConnect which we call *Tesseract-GP* and one that uses the geometric plan as a seed to Trajopt for trajectory optimization which we call *Tesseract*.^11^1We also tried Tesseract's TrajOpt integration with a linear seed but it failed to find solutions on most problems. We compare these baselines to two versions of motion generation from cuRobo, one that only does geometric planning *cuRobo-GP* using our algorithm from Section 5 and the other that does Trajectory Optimization *cuRobo*. For all methods, we timeout at 60 seconds and allow random restarts until this timeout is reached. More details on the baselines and the evaluation methods are available in Appendix B.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Motion Generation Quality", "weight": 1.0} -->

We report the success across the 2600 motion planning problems in Figure 6. We count a trajectory as *Success* when it is collision-free, it doesn't violate any joint limits, and is within 5mm and 5% of desired position and orientation respectively. We found our geometric planner *cuRobo-GP* to find a path on 99.8% of the dataset compared to *Tesseract-GP*'s 98.6%. Our geometric planner only failed on 5 problems compared to *Tesseract-GP* failing on 36 problems. When we compare trajectory optimization methods, *cuRobo* only failed on 5 problems while *Tesseract* failed on 38 problems, giving a success rate of 99.8% and 98.53% respectively. *cuRobo* and *cuRobo-GP* failed on the same set of five problems. When we look at these problems in Fig. 7, we see that 3 problems have their goal pose in collision with the world, 1 problem as the start configuration in collision, and one problem does not have a collision-free IK solution to the goal pose.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Motion Generation Quality", "weight": 1.0} -->

The reason for these problems to be invalid for *cuRobo* is because we evaluate *cuRobo* with our cuboid collision checker which approximates the obstacles represented by cylinders as cuboids. While *cuRobo* also has mesh-based collision checking and depth camera based collision checking, we leave evaluating these collision checkers for a future work.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Motion Generation Quality", "weight": 1.0} -->

No Collision-free IK for Goal Pose
Start Config in Collision

<!-- chunk {"id": "body-0054", "role": "body", "section": "Motion Generation Quality", "weight": 1.0} -->

Next, we plot *C-Space Path Length* across the four methods in Figure 8. First, we observe that our geometric planner *cuRobo-GP* has shorter path length than *Tesseract-GP* which uses RRTConnect. *cuRobo-GP*'s path lengths are \[5.39, 7.13, 13.45\] radians on mean, 75$^{\text{th}}$, and 98$^{\text{th}}$ percentile of the dataset compared to *Tesseract-GP*'s \[7.1, 8, 17.2\] radians. We then observe methods that use trajectory optimization, *cuRobo* and *Tesseract* have shorter path length than geometric planning methods *cuRobo-GP* and *Tesseract-GP*. *Tesseract* reduces paths on average by 48% when compared to *Tesseract-GP*. *cuRobo* reduces the path length by 53% on average when compared with *Tesseract-GP*.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Motion Generation Quality", "weight": 1.0} -->

*cuRobo* reduces path length by 53%, 39%, and 10% on average when compared to *Tesseract-GP*, *cuRobo-GP*, and *Tesseract* respectively. When we compare *cuRobo* with *Tesseract*, we found that *cuRobo*'s paths are 26% shorter than *Tesseract* on the $98^{\text{th}}$percentile of the dataset.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Motion Generation Quality", "weight": 1.0} -->

From the geometric planning metrics, we find that trajectory optimization methods have comparable success percentage to geometric planning methods while also providing shorter path lengths than RRTConnect-like planners. While optimal geometric planners can generate shorter paths than RRTConnect, they require either more planning time or task-specific heuristics as shown in Appendix C.1. Our goal is not only to get shorter paths, but also trajectories that can be executed on robots with minimal post-processing. Geometric planning methods require time parameterization as a post-processing step to be able to execute on robots. Kunz and Stilman developed a bounded velocity and acceleration time-parameterization technique that is extensively used in the robotics community, including MoveIt. However, this time parameterization technique does not bound the jerk along the trajectory and as such can have very large jerks. We could not find any accessible software library that can post process geometric paths while bounding jerks, making geometric path planning not directly deploy-able on jerk sensitive manipulators. We hence only compare between *Tesseract* and *cuRobo* on the time parameterization metrics.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Motion Generation Quality", "weight": 1.0} -->

We additionally take the trajectories obtained from *Tesseract* and post process with Kunz and Stilman's method, which we call *Tesseract-TG*. We add this to our comparisons to highlight the improvements we can get with trajectory optimization techniques, especially with *cuRobo*'s minimum jerk formulation.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Motion Generation Quality", "weight": 1.0} -->

The first in time parameterization metrics is *Motion Time* which we plot in Figure 9. *cuRobo*'s trajectories take \[1.59, 1.89, 3\] seconds compared to Tesseract's \[1.96, 2.17, 4.86\] seconds on the mean, $75^{\text{th}}$, and $98^{\text{th}}$ percentiles. *cuRobo* produces trajectories that have a 1.23x lower mean and 1.62x lower $98^{\text{th}}$ percentile motion time when compared to motions generated by *Tesseract*. This large reduction in motion time leads to *cuRobo*'s $98^{\text{th}}$ percentile being 2.86 seconds quicker than *Tesseract*.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Motion Generation Quality", "weight": 1.0} -->

When we compare *cuRobo*'s solutions to *Tesseract-TG* which uses time-optimal reparameterization, *cuRobo* generates trajectories that are 0.3 seconds slower both on average and $98^{\text{th}}$percentile of the dataset. This slow down is because *cuRobo* also optimizes for minimum-jerk, leading to trajectories with 12x lower jerk on average compared to *Tesseract-TG* as shown in Fig. 10. When comparing to *Tesseract*, we generate trajectories that have 4x lower jerk on average as *Tesseract* doesn't minimize jerk.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Motion Generation Quality", "weight": 1.0} -->

We compare the mean velocity and maximum acceleration between methods in Figure 11. *Tesseract-TG* has the largest values in mean velocity and maximum acceleration as Kunz and Stilman's time parameterization technique by design attempts to reach peak velocity by instantly jumping to maximum acceleration. *Tesseract* has larger max acceleration when compared to *cuRobo* as it doesn't have to optimize for jerk and as such can instantaneously change acceleration along the trajectory without any penalties. We also observed that *Tesseract* has a $98^{\text{th}}$ percentile maximum acceleration of 23.9 rad.s^-2^ which is beyond the 15 rad.s^-2^ acceleration limit we set for the Franka Panda robot. *cuRobo* has the smallest maximum acceleration across the dataset as we minimize jerk across the trajectory, which penalizes instantaneous changes to acceleration.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Motion Generation Quality", "weight": 1.0} -->

Even with the smallest maximum acceleration, *cuRobo*'s mean velocity is comparable to *Tesseract*, slightly higher in the mean by 0.02 rad.s^-1^ and 0.01 rad.s^-1^ in the $75^{\text{th}}$ percentile.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Motion Generation Quality", "weight": 1.0} -->

Summarizing across these metrics, *cuRobo* produces paths that are shorter in path length than any other method while also succeeding on all feasible problems in the dataset. In addition, *cuRobo* generates trajectories that have the least jerk, 4x lower than existing trajectory optimization techniques, and 12x lower than existing time parameterization methods. Trajectories generated with *cuRobo* also have motion times 1.23x lower than existing trajectory optimization techniques and is within 0.3 seconds of high-jerk time parameterization methods. We will next analyze the compute time taken by *cuRobo* to obtain these trajectories.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Compute Time", "weight": 1.0} -->

We calculate the compute time on three platforms, a PC with an AMD Ryzen 9 7950x CPU and NVIDIA RTX 4090 GPU, and an NVIDIA Jetson AGX Orin 64GB system configured to operate at MAXN (60W) and 15W power budgets. We measure runtime using Python's time utility after synchronizing device and host.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Motion Generation", "weight": 1.0} -->

The time it takes to compute motions using *cuRobo* is compared to *Tesseract* in Figure 12 across all three platforms. We observed that *Tesseract* takes on average 2.95 seconds compared to *cuRobo* taking 50ms, leading to a 60$\times$ speedup in motion planning. The gap in planning time increases at the $75^{\text{th}}$ percentile of evaluation set, *cuRobo* taking 30ms to plan while *Tesseract* takes 2.47 seconds, leading to a 72$\times$ speedup in planning with our proposed method. On the $98^{\text{th}}$ percentile of the dataset, *cuRobo* takes 260 milliseconds while *Tesseract* takes 22 seconds, giving *cuRobo* 83$\times$ speedup in planning. The difference in planning time across the mean, $75^{\text{th}}$, and $98^{\text{th}}$is because *cuRobo* calls the geometric planner only after three failed attempts with linear seeds.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Motion Generation", "weight": 1.0} -->

The speedup over *Tesseract* scales to the NVIDIA Jetson ORIN as well, in both power modes as shown in Figure 12. *cuRobo* takes 0.22 seconds and 0.48 seconds on average on at MAXN and 15w while *Tesseract* takes 6.13 seconds and 10.3 seconds respectively. On average, *cuRobo* is 28$\times$ and 21$\times$ faster than *Tesseract* at MAXN and 15W respectively. We also oberved that *cuRobo* is faster on a NVIDIA Jetson ORIN at 15W than *Tesseract* running on a desktop PC as shown in Figure 13.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Motion Generation", "weight": 1.0} -->

Our approach is implemented in python with key compute kernels in CUDA C++ called through python wrappers. We reduced the python overhead and the overhead of repeatedly launching CUDA kernels by recording optimization iterations and the mask_samples function in geometric planning (see Algorithm 5) in CUDA Graphs. We then replay the recorded CUDA Graphs with data from new planning problems. This use of CUDA Graphs reduced our planning time by 10x compared to calling the kernels individually from python. Our implementation still has some components in python, calling many small cuda kernels to setup the optimization problems, and also to get the final result from the many parallel seeds. We timed these parts and found that *cuRobo* spent 8ms, 5ms, and 30ms on the mean, $75^{\text{th}}$, and $98^{\text{th}}$ percentile as shown in Figure 14. The percentage of time spent in these steps compared to the solver time was 15%, 15%, and 12% on average, $75^{\text{th}}$, and $98^{\text{th}}$ percentiles.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Motion Generation", "weight": 1.0} -->

We leave speeding up these components by rewriting directly in C++ and fusing the CUDA kernels to future work. We do share the speedup that could be gained if these components are optimized by only comparing the iterations time and geometric planning time to *Tesseract* in Figure 14. We see that our speedup of 60$\times$ becomes 69$\times$ on mean, 72$\times$ becomes 84$\times$ on $75^{\text{th}}$ percentile, and 83$\times$ becomes 93$\times$ on the $98^{\text{th}}$ percentile.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Geometric Planning", "weight": 1.0} -->

We compare the compute time in geometric planning between our GPU accelerated geometric planner introduced in Section 5 which we call *cuRobo-GP* to OMPL's RRTConnect implementation in Tesseract, which we call *Tesseract-GP* in Figure 15. *Tesseract-GP* takes 1.5 seconds on average while *cuRobo-GP* takes 0.02 seconds leading to a 101$\times$ speedup in geometric planning with *cuRobo-GP*. Looking at the $98^{\text{th}}$ percentile planning time, *Tesseract-GP* takes 20 seconds while *cuRobo-GP* takes 0.04 seconds, giving us a 581$\times$ speedup. A very recent work from Thomason *et al.* that explores vectorized geometric planning leveraging SIMD on CPU. The results from their paper show that it takes 0.1ms (mean) to plan on the motion benchmaker dataset. However, their code is not available at the time of this publication and we leave comparing to it for a future work.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Trajectory Optimization", "weight": 1.0} -->

We compute the time it takes to perform trajectory optimization in Figure 16 between *cuRobo*'s GPU accelerated approach and TrajOpt implementation leveraged by *Tesseract*. We see that *cuRobo* is 87$\times$ and 145$\times$ faster in optimization than TrajOpt on average and $75^{\text{th}}$ percentile respectively. *cuRobo* takes a mere 10ms to perform trajectory optimization compared to TrajOpt taking 1.79 seconds on $75^{\text{th}}$ percentile of the evaluation set. We get speedups of 23$\times$ and 17$\times$ on Jetson device as well, taking 0.09 and 0.17 seconds on average on ORIN at MAXN and 15W respectively. These speedups are interesting because numerical optimization is predominantly iterative where we run many sequential iterations until convergence. These sequential iterations can make the entire computation graph memory access heavy. Our efficient parallelization of compute across the whole pipeline enables us to get these speedups.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Trajectory Optimization", "weight": 1.0} -->

We not only run each seed of optimization in seperate threads but also split many of our workload heavy kernels across many threads on a per seed basis.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Trajectory Optimization", "weight": 1.0} -->

While these timings are based on optimizing collision-free trajectories, we hope that these speedups encourage roboticists to leverage *cuRobo*'s trajectory optimization implementation for other robotics tasks.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Inverse Kinematics", "weight": 1.0} -->

We compare the performance of our inverse kinematics solver against TracIK. We perform two sets of experiments: without collision checking and with self and environment collision checking. We chose an instance of the *bookshelf-small-panda* scene from motion benchmaker for the collision checking experiment. We sample feasible joint configs from a Halton Sequence and average the results across 5 trials for different batch sizes. Since TracIK does not account for collisions, we perform rejection sampling with PyBullet, allowing 10 reattempts. For all cuRobo IK queries, we run 30 seeds in parallel and return the best solution from these seeds. We evaluate IK with 5 different batch sizes -- 1, 10, 100, 500, and 1000. For a single query (batch size=1), cuRobo takes 2.7ms while TracIK only takes 0.9ms. However, as we increase the batch size of IK queries, we see a speedup starting from a batch size of 10.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Inverse Kinematics", "weight": 1.0} -->

For the standard IK problem, we can generate 37134 solutions per second when we use a batch size of 1000 while TracIK can only generate 1590 solutions, 23.4$\times$ slower than our method. When we compare collision-free IK, our method (*cuRobo-Coll-Free*) can compute 7611 compared to rejection sampled Trac-IK (*TracIK-Coll-Free*) which can only obtain 95 collision-free solutions per second in our experiments, 80x slower than our approach to collision-free IK as shown in Fig. 37-B. We also found that rejection sampling approach to collision-free IK failed on 20% of the problems tested. BioIK reports that their approach can solve IK in 0.7ms (1428 solutions per second), it is not clear from their paper whether the runtime includes collision-free IK. Even if we consider their timing to be for collision-free IK, our method is still faster starting from a batch size of 10, taking 0.48ms per solution.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Kinematics and Distance Queries", "weight": 1.0} -->

One of the major breakthroughs in accelerating our motion generation approach was on developing a parallel compute friendly implementation of robot kinematics. Most common manipulators have many serially connected links, making computation of kinematics a largely serial operation. Existing SOTA methods for forward kinematics on CPUs such as pinnochio take 1$\mu$s on average for 7-dof robots while GPU accelerated kinematics implemented in PyTorch such as STORM outmatch CPU methods only at a batch size of 1000. STORM improves upon implementation from Meier *et al.* by keeping buffers in memory between calls without recreating them. This slowdown in GPU based kinematics is because existing implementations use many CUDA kernels to perform kinematics, e.g., STORM runs through 125 CUDA kernels to compute kinematics. In *cuRobo*, we implement the entire kinematics in a single CUDA kernel, discussed in Appendix E. This enables our approach to outmatch pinnochio's performance at a batch size of 100 as shown in Figure 19.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Kinematics and Distance Queries", "weight": 1.0} -->

We also compare our kinematics implementation with KDL's implementation which is used by traciky. We additionally show the improvement with CUDA Graphs in calling GPU methods by adding a suffix "-CG".

<!-- chunk {"id": "body-0076", "role": "body", "section": "Kinematics and Distance Queries", "weight": 1.0} -->

For signed distance queries, we compare with two prior methods -- PyBullet which uses Bullet to compute the signed distance and STORM. We are faster beginning at a batch size of 1 as our approach uses many parallel threads on the GPU for a single query.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Summary", "weight": 1.0} -->

We summarize the median compute time across the different modules in *cuRobo* in Figure 20. *cuRobo*'s implementation of kinematics and collision checking can compute within 1 nanosecond and 10 nanoseconds respectively when using a batch size of 100k. For general inverse kinematics and collision-free inverse kinematics, *cuRobo* can compute within 27 $\mu$seconds and 130 $\mu$seconds. This low computation time can accelerate existing robotics pipelines that use inverse kinematics such as reachability analysis and placement planning. Geometric planning has been used in verifying transition feasibility in hierarchical planning and task and motion planning (TAMP), where the quality of solutions is not critical and knowing if a path exists is sufficient. For these applications, leveraging *cuRobo*'s geometric planning can lead to a 101$\times$ speedup compared to using OMPL's RRTConnect algorithm. Our implementation of collision-free trajectory optimization takes 10ms, which could accelerate other robotics problems. The full motion generation pipeline already runs at 30ms on median on a modern PC.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Summary", "weight": 1.0} -->

In addition, *cuRobo*'s motion generation scales well to a NVIDIA AGX Orin running at 60W, taking only 100ms enabling deployment of motion generation on edge devices. *cuRobo* obtains these low compute times while having most of it's stack in Python and with components implemented as separate modules. One could get even better compute times by fusing the modules at the CUDA kernel level, however that can make the library very rigid and inaccessible to robot practitioners.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Real Robot Tracking Performance", "weight": 1.0} -->

We study the tracking performance between the generated motions and executed motions by running *cuRobo* on two Universal Robots, an UR5e robot and an robot. We connect the robots to a NVIDIA Jetson ORIN AGX which is running a PREEMPT RT kernel and uses the ros driver from universal robots for communication. We run *cuRobo* on the same Jetson device and send the generated trajectories to Universal Robot's trajectory tracking controller. For both robots, we setup an obstacle and selected seven random poses scattered around the robot's workspace, which are shown in Figure 21. We then run motion generation to reach these seven poses in sequence five times, leading to a total of 35 reaching motion trials. The robots use an absolute magnetic encoder and an optical encoder together to measure the joint position. The accuracy of the magnetic encoder is +-0.0017 radians as obtained. We could not obtain the accuracy of the optical encoder and also the overall accuracy of the joint position measurement. We hence assume for all discussion below that the joint position is accurate up to 0.0017 radians.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Real Robot Tracking Performance", "weight": 1.0} -->

We generate motions using *cuRobo* in two different modes, starting with *min-acc* where *cuRobo* performs trajectory optimization with acceleration minimization, without any jerk minimization, followed by *min-jerk* where we minimize jerk along with acceleration. In both these modes, the trajectory is optimized over 32 timesteps, interpolated to a 0.01 second resolution, and sent to the robot. We found no difference between sending an interpolated trajectory (at a 0.01 resolution) and the optimized coarse trajectory (32 steps) to the and the UR5e. However, when executing trajectories with a low-level controller on many common robots, it might be necessary to interpolate the trajectory to a finer resolution before execution. We hence run all our experiments with interpolated trajectories.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Real Robot Tracking Performance", "weight": 1.0} -->

We first measure the error in tracking the position and velocity across the trajectories. Deviations from the planned path can lead to critical failure as the robot could hit obstacles in the world. Poor velocity tracking can lead to the robot taking more motion time than planned, creating uncertainty in cycle time for tasks. As reported in our results in Figure 22, *min-jerk* has lower tracking errors in both position and velocity across both the robots. We observed a mean position error of 0.00117 radians and 0.00085 radians for *min-acc* and *min-jerk* on the UR5e robot, both within the 0.0017 radians accuracy margin of the joint encoders. On the robot, we found the mean position error to be 0.00250 radians and 0.00133 radians for *min-acc* and *min-jerk* respectively. We suspect the the larger position error on the to be because of the robot being physically larger, thereby requiring more dynamics compensation at high speeds compared to the UR5e. The position error for *min-acc* is also larger than the accuracy margin of the encoder.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Real Robot Tracking Performance", "weight": 1.0} -->

To closely examine the difference in position error between *min-acc* and *min-jerk* on the, we plot one executed trajectory from the trials in Figure 23. We observe that the robot with *min-acc*, the robot has a large spike in position error at the start of the trajectory while in *min-jerk* there is no steep increase in error at the start. We suspect this spike in *min-acc* at the start to be because of the robot not being able to instantly accelerate to the maximum acceleration limit. With *min-jerk*, we gradually increase the acceleration, thereby minimizing tracking error due to delay in robot's acceleration. While one could feed a feed forward torque to help the robot accelerate more quickly, sending torque commands is not possible in many industrial robots including the and UR5e.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Real Robot Tracking Performance", "weight": 1.0} -->

Our motion times for *min-jerk* were \[0.98, 1.57, 2.45\] seconds and \[0.87, 1.34, 2.16\] seconds on the UR5e and respectively, where the numbers map to mean, $75^{\text{th}}$ percentile and $98^{\text{th}}$ percentile. Our motion times for *min-acc* were \[1.02, 1.59, 2.83\] and \[0.92, 1.52, 2.49\] on the UR5e and respectively.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Real Robot Tracking Performance", "weight": 1.0} -->

As part of our real robot experiments, we also timed the whole pipeline, starting with when *cuRobo* gets a planning query and completes computing a plan, followed by when the robot starts moving, and finally when the robot completes trajectory execution. We found *cuRobo* to complete planning within 100ms on average for both UR5e and robots. We observed on average a delay of 58ms and 68ms between when a trajectory is sent to the UR ROS driver and when the robot starts moving on the UR5e and respectively. We plot the time it takes overall reach a target pose and the split between planning, delay, and execution in Figure 24. We see that *cuRobo* takes \[6.02%, 6.62%, 9.12%\] and \[6.67%, 7.93%, 9.13%\] of the time in the full pipeline on the UR5e and respectively in *min-jerk* mode. The delay accounts for 5% and 6% of the time on $98^{\text{th}}$ percentile on UR5e and respectively.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Real Robot Tracking Performance", "weight": 1.0} -->

The robot is in motion \[90%, 92%, 94%\] and \[89%, 90%, 92%\] on UR5e and respectively. A common technique to reduce planning overhead in cycle time is to plan for the next sequence of targets while the robot is executing it's current trajectory. This has been leveraged with existing planners as they can take significantly longer planning times, in the range of 2.5 seconds. However, this can prevent the robot from reacting to any world or task changes between motions. With *cuRobo* we can plan the next motion after executing the current trajectory as we only take 6% of the cycle time on average. This also simplifies the robot programming pipeline, as computational tasks can be executed in serial.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Deployment on different Robot Platforms", "weight": 1.0} -->

We deployed *cuRobo* on few different robot platforms as shown in Figure 25, with no changes to parameters in trajectory optimization. We created the robot spheres for these robots along with a collision-free rest configuration. We then called the inverse kinematics, geometric planning, and trajectory optimization methods.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Deployment on different Robot Platforms", "weight": 1.0} -->

First, we deployed *cuRobo* on a with nvblox to perform collision checking between the world and the robot as shown in Figure 25. We use nvblox to generate a euclidean signed distance field (ESDF) map of the world, by scanning with a realsense D-415 camera attached to the end-effector. We then generate motions for the robot to go around obstacles. Next, we deployed on a Kinova Jaco arm as shown in Figure 25, where we implemented a PD controller in the velocity space to command the generated trajectory. We also tested coordinated motion generation for a dual arm robot setup in NVIDIA Isaac Sim and preliminary results are promising as *cuRobo* finds collision-free paths to move both arms to their targets as shown in Figure 25.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Summary", "weight": 1.0} -->

We first compared the quality of motions generated from *cuRobo* in Section 6.1 and showed that *cuRobo* generates better solutions than existing techniques. We then showed in Section 6.2 that *cuRobo* generates these high quality solutions in a fraction of the time taken by existing methods across different computing platforms including a 15W NVIDIA Jetson device. We then compared the compute time across sub-components, inverse kinematics, geometric planning, and trajectory optimization and showed double digit speedups compared to existing implementations. We validated our motion generation approach on two robots in Section 6.3, a UR5e and robot, both tracking the minimum jerk high-speed trajectories from *cuRobo* with position errors below the accuracy margin of the joint encoders. We also showed our approach working on different robot platforms in Section 6.4.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Component Analysis", "weight": 1.0} -->

We study the effect of different components in *cuRobo*'s trajectory optimization, starting with collision cost formulation, followed by the effect of number of parallel seeds in trajectory optimization, and then the effect of different parameters in our numerical optimization solvers.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Collision Cost Formulation", "weight": 1.0} -->

We first analyze the impact of different collision cost formulations on success of the optimization problem in Figure 26. We ran our motion generation pipeline without geometric planning and 500 IK seeds. We ran experiments without particle-based optimization, with particle-based optimization, and with 1 and many seeds.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Collision Cost Formulation", "weight": 1.0} -->

Increasing activation distance from 0cm to 2.5cm improves success rate by 27%, having the largest impact in success rate.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Collision Cost Formulation", "weight": 1.0} -->

Using continuous collision checking (swept) improves success rate further by 4% when compared to only using an activation distance of 2.5cm.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Collision Cost Formulation", "weight": 1.0} -->

Speed metric improves success rate further by 2% across the dataset.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Collision Cost Formulation", "weight": 1.0} -->

We found activation distance is critical in improving success rate as we perform trajectory optimization at a coarse scale of a few timesteps(32-50) and then interpolate the trajectory to a fixed dt of 0.025 to validate success. After this interpolation, a collision-free trajectory can move into regions of collision and lead to failure. In addition, having an activation distance adds smoothness to the cost term, making it easier for an optimization solver to minimize collisions. Our continuous collision checker checks collisions between timesteps by linearly interpolating in the task space, approximating linear interpolation in the joint space. This improves the success rate by 7% with tuned TO seeds and zero activation distance. The improvement diminishes with activation distance where it only improves by 3%.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Collision Cost Formulation", "weight": 1.0} -->

The effect of speed metric is observable at an activation distance of 0.0 cm on trajectory optimization with 1 seed, where it provides a 5% improvement over LBFGS and also over particle+LBFGS. This effect diminishes when we use many parallel seeds as a collision-free path is obtained through other seeds. We visualize the effect of speed metric in Figure 27, where the use of speed metric enables the optimization solver to find a path that is collision-free while without the metric, the solver ends up speeding through the high cost region.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Collision Cost Formulation", "weight": 1.0} -->

From the results in Figure 26, we see that a naive implementation of collision cost with a gradient based optimizer and 1 seed achieves a success rate of 38%. Adding an activation distance, as introduced by would bring this to 65%, followed by addition of a continuous collision checking would bring this to 69%. Addition of the speed metric from would increase this further to 71%. Adding a particle-based optimizer to initialize gradient-based solver would increase the success to 76%. Finally, running trajectory optimization across many seeds would increase the success rate to 85%.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Collision Cost Formulation", "weight": 1.0} -->

Overall, our application of existing techniques from in combination with our continuous collision checking module and many parallel seeds for trajectory optimization improves the success rate from 38% to 85%, enabling *cuRobo* to solve 85% of the motion generation problems within 1 attempt.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Effect of Parallel Seeds", "weight": 1.0} -->

In an ideal setting, we would want to run as many parallel seeds of optimization as possible and pick the best solution. However, as we reduce the compute available for motion generation, the number of parallel seeds used can have a significant impact on compute time. We study the interaction between number of seeds and compute time we ran motion generation on the 100 problems from the *cage-panda* environment with varying number of trajectory optimization seeds across the three compute platforms. We used 500 IK optimization seeds and also run particle based optimization to initialize L-BFGS in these experiments. We observed that on a RTX 4090, the compute time only changes by 8ms from using 4 seeds to 48 seeds while it changes by 158ms and 417ms on the ORIN at MAXN and 15W respectively. We plot these results in Figure 29.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Effect of Parallel Seeds", "weight": 1.0} -->

Next, we study the impact of trajectory optimization seeds on success and motion time in Figure 28. We observed that increasing the number of parallel seeds for trajectory optimization increases the success rate and also decreases the motion time starting at 48 seeds. Initializing trajectory optimization with collision-free paths from our geometric planner also increases the success rate. However, using geometric planner to initialize trajectory optimization doubles the planning time on most problems. In addition, we found that the motion time was higher when trajectory optimization is initialized with a geometric planner. Based on these results, we use 12 trajectory optimization seeds for most environments in our evaluation dataset and increase this up to 28 for harder environments. We discuss the parameters used in Appendix B.3.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Line Search", "weight": 1.0} -->

The role of line search in gradient-based numerical optimization solvers is to find the best magnitude to scale the step direction. A common strategy to find the best magnitude is by backtracking search, where we start with a magnitude of 1 and reduce this value until some conditions are met. Two common conditions used in many modern numerical solver libraries are *weak-wolfe* and *strong-wolfe* which we term *wolfe* and *st-wolfe* in our comparisons. We also compare against no scaling of the step direction which we term *no-ls*. We compare these options with our noisy line search technique introduced in Section 4. We use \[0.01,0.3,0.7,1.0\] as the values for the noisy line search which we term *noisy-ls*. We also compare with only 1 value for noisy line search \[0.01,1.0\] which we term *noisy-ls-1*.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Line Search", "weight": 1.0} -->

For wolfe and strong wolfe, we use the values \[0.0001,0.001,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0\] in the line search. We evaluate these line search techniques across the full dataset with 1 trajectory optimization seed initialized by 2 iterations of particle-based optimization.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Line Search", "weight": 1.0} -->

From Figure 30, we see that *no-ls*, *noisy-ls-1*, and *noisy-ls* all have a success rate higher than 70%, with *noisy-ls* having the highest success rate of 75.69%. While most of these techniques lead to good success rate, the impact of line search is more observable in the position error at the final timestep of the trajectory across the dataset as plotted in Figure 30-(b). We found noisy line search to have the lowest error of 2.86 mm while no line search ends up with an error of 4 mm. We observed wolfe and strong wolfe perform worse in both success and position error across the dataset as for these line search techniques, we use a magnitude scale of 0.0 if none of the chosen line search values satisfy the conditions.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Gradient Descent and Effect of history length in L-BFGS", "weight": 1.0} -->

We ran trajectory optimization with gradient descent as the optimizer, swapping out L-BFGS, but keeping our noisy line search technique and found that it succeeded in 46% of the problems. Using particle-based optimization to initialize gradient descent increased the success to 61%. However, the $98^{\text{th}}$ percentile position error was 4.94cm compared to L-BFGS's 2.72cm. In addition, our efficient implementation of L-BFGS enables us to compute step direction using L-BFGS within similar compute times to using Gradient Descent upto a history length of 12. The gap in performance between gradient descent and L-BFGS is also visualized on one trajectory optimization problem in Figure 32 where we see that L-BFGS with any history length converges to the minimum within 100-200 iterations while gradient descent has not converged even after 500 iterations.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Gradient Descent and Effect of history length in L-BFGS", "weight": 1.0} -->

We also ran experiments to study the impact of history length in L-BFGS. L-BFGS approximates the hessian by using the recent gradients and costs, which are stored in a history buffer. The more history L-BFGS uses to approximate the hessian, the closer the hessian gets to the true hessian. However, with increasing history, the compute required to compute the step direction also increases as shown in Figure 31-(b). To allow for the best chance between methods, we run our method with tuned number of parallel seeds across the dataset. We also compare the improvement we get with particle-based solver for initialization. From Figure 31, we found that increasing history indeed improves convergence as seen by the improvement in success rate and reduction in position error. And increasing history starts having an impact on planning time at a value of 12. We chose a history of 4 for all our evaluations as we observed that the improvement in success rate and position error was not significant.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Effect of Particle Optimization", "weight": 1.0} -->

Across analysis of many of the components, we compare the improvement we obtain with particle optimization. We observed that since we only run 2 iterations of particle-based optimization, it only adds 2 ms to the planning time on average while improving success. We observed that using two iterations of particle-based optimization improved the success by 5% from 71% to 76% when running trajectory optimization with a single seed. With multiple seeds, the success improved by 3%, from 82% to 85%.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

We formulated the global motion generation problem as an optimization problem and introduced techniques from global optimization literature to efficiently solve them with accelerated parallel compute. We empirically validated our approach on a difficult set of motion generation problems for manipulators and showed a 60$\times$ speedup over SOTA motion generation methods on a modern PC and a speedup of 28$\times$ on a NVIDIA Jetson AGX ORIN at 60W. We release our implementations as a high performance CUDA accelerated library *cuRobo* with pytorch and python wrappers for easy integration in robotic pipelines. We will discuss some limitations of our work and potential extensions in the next section.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Limitations & Open Research Problems", "weight": 1.5} -->

There are several open research problems in motion generation that our approach does not solve in it's current form. We hope that our results and framework can be leveraged to solve these problems. We list some key problems below,\
Global Reactive Motion Generation Our approach is currently limited to planning full motions, where the robot starts from a static state. While we can extend our trajectory optimization to start from a non-static state, reactive motion generation requires motions at a fixed solve rate and our approach can take longer time on hard problems as shown by our longer $98^{\text{th}}$ percentile time.\
Constrained Motion Generation Our preliminary evaluation on pose constraints during motion such as maintaining orientation or height by adding a large weight to a running cost showed promise. However, we did not evaluate rigorously and also did not implement constrained graph planning which could be important for getting global guarantees.\
Task Sequencing and Route Planning Finding the optimal sequence of poses to reach given an unordered list is an important problem in the industry, often called Task Sequencing and route planning. We do not explore this task in this work but do see point to point motion generation to be a critical component of finding the optimal sequence.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Limitations & Open Research Problems", "weight": 1.5} -->

Task and motion planning could also leverage our point to point motion generation for faster feasibility checks and finding more optimal sequence of motions.\
Contact-Rich and Full-Dynamics Trajectory Optimization Our current cost terms are focused on kinematic trajectory optimization with limits on position derivatives. Interacting with objects in the world would require optimizing over contacts, e.g. with contact implicit formulations of trajectory optimization. Trajectories that minimize torques or other parts of dynamics would require optimizing over the robot's dynamics. Integrating existing GPU accelerated dynamics implementations into *cuRobo* could potentially solve for trajectories over dynamics.\
Robotics Solvers We implemented MPPI, gradient descent and L-BFGS in our framework to solve motion generation. Robotics focused numerical solvers are showing promise in quicker and better convergence compared to standard numerical solvers on robotics tasks. Formulating parallel compute friendly versions of these solvers could reduce the compute time even further and also enable new features in *cuRobo* such as solving with hard constraints.\
Collision Avoidance from partial world sensing Our approach does not tackle partial perception and instead assumes that we can obtain a complete representation of the world.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Limitations & Open Research Problems", "weight": 1.5} -->

Incorporating learned representations of the world into our collision cost term could extend our motion generation method to work in unknown environments.\
Accelerating Computational Blocks Our approach encapsulates the key components in motion generation into modular components and enables researchers to develop improved algorithms for these components without requiring full expertise on the stack. We hope that this broadens our library's audience to experts in non-robotics fields. We think that this is important as researchers in computer architecture are starting to accelerate manipulator algorithms and providing a reference SOTA implementation along with benchmarks can greatly reduce the entry barrier for researchers to accelerate robotics. As a step in this direction, *cuRobo* has been used by computer architecture researchers to reduce memory bottlenecks in motion generation with reduced precision techniques.
