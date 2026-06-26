<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Vectorizing Projection in Manifold-Constrained Motion Planning for Real-Time Whole-Body Control

Topics include Motion planning, Robotics, Real-time systems, Planning, Control, Humanoid robot.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Many robot planning tasks require satisfaction of one or more constraints throughout the entire trajectory. For geometric constraints, manifold-constrained motion planning algorithms are capable of planning collision-free path between start and goal configurations on the constraint submanifolds specified by task. Current state-of-the-art methods can take tens of seconds to solve these tasks for complex systems such as humanoid robots, making real-world use impractical, especially in dynamic settings. Inspired by recent advances in hardware accelerated motion planning, we present a CPU SIMD-accelerated manifold-constrained motion planner that revisits projection-based constraint satisfaction through the lens of parallelization. By transforming relevant components into parallelizable structures, we use SIMD parallelism to plan constraint satisfying solutions. Our approach achieves up to 100-1000x speed-ups over the state-of-the-art, making real-time constrained motion planning feasible for the first time. We demonstrate our planner on a real humanoid robot and show real-time whole-body quasi-static plan generation. Our work is available at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Constrained motion planning problems arise commonly in many robotic tasks. Consider the problem of transporting a cup of water; the robot must find a trajectory in which the mug remains upright throughout to prevent spillage. Or, consider a humanoid robot transporting a large object. The robot must maintain balance at all times and keep both arms attached to the box to preserve feasible motion. Many of these constraints can be represented as implicit functions, which give rise to a submanifold of valid configurations in the robot's configuration space. Manifold-constrained motion planning is thus the problem of finding feasible, collision-free trajectories that satisfy a constraint imposed by a desired task from a start configuration to a goal region.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite their prevalence, manifold-constrained problems remain difficult to solve in real-time. The primary bottleneck lies in the ability to find constraint satisfying configurations quickly, as they typically are not explicitly defined. This problem is also exacerbated by the dimensionality of the system, the number of constraints that must be simultaneously satisfied, and the number of obstacles in the scene. For example, consider the Digit robot (shown in Fig.˜1), a 30 degree-of-freedom (DoF) humanoid with a 6-DoF floating base. In this quasi-static whole-body coordination problem, the robot must maintain balance, have both feet on the ground at all times, and preserve the closed-chain constraint to keep both arms holding the box during transport. Consequently, most constrained motion planning works take anywhere in the order of hundreds of milliseconds to tens of seconds to solve, which limits real-time planning and execution.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent advances in accelerating motion planning have made real-time motion planning feasible; many approaches have used CPU and GPU acceleration to bring planning time to the millisecond time scale \[undef, undefa, undefb\]). Most relevant to our approach is the Vector-Accelerated Motion Planning (VAMP) library \[undefc\], which exploits CPU "Single Instruction, Multiple Data" (SIMD) parallelism and data parallelism to achieve multiple orders-of-magnitude speed-ups by parallelizing forward kinematics and collision checking in motion validation, bringing planning times for unconstrained geometric planning problems into the realm of microseconds. However, while promising, these approaches either do not consider task constraints nor scale to very high-DoF systems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, we revisit the problem of samping-based manifold-constrained motion planning through the lens of vector acceleration. The primary bottleneck---beyond collision checking---is the manifold-constrained extension step, i.e., tracing a geodesic between configurations on a manifold. We tackle this with *fine-grained parallelization* of the projection of configurations in a geodesic onto the manifold. Altogether, we present the Manifold-Constrained Vector Accelerated Motion Planner (McVAMP) which is capable of planning on the order of microseconds to milliseconds for a wide range of manifold-constrained systems including whole-body manipulation. We believe this is a categorical shift in capabilities of planning for constrained high-DoF systems, as planning in real-time enables reactive global planning which could be used both for high-level task planning as well as low-level control.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Thus, our contribution is as follows We present a single-core CPU-only SIMD-accelerated sampling-based manifold-constrained motion planner that is capable of planning in the order of microseconds to milliseconds.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

At the heart of our planner is a SIMD-parallel manifold-constrained extension step, which projects multiple configurations in parallel to satisfy constraints, and then evaluates for collision building upon VAMP's existing primitives.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate the ability of our planner to compose multiple constraints and develop a quasi-static whole-body motion planner for a humanoid capable of producing stable, feasible motion plans that a robot with a classical controller can execute without modification.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate our planner on a number of challenging problems in simulation and reality with a 7-DoF arm, a 14-DoF bimanual system, and a 28-DoF humanoid. Our approach outperforms the existing state-of-the-art baselines by orders of magnitude in terms of speed, while obtaining a better success rate and similar path quality.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-A Parallelized Motion Planning", "weight": 1.0} -->

There are many approaches to parallelizing motion planning; multiple aspects of planning are trivially parallelizable such as running many searches \[undefn\] or many iterations in parallel \[undefo, undefp\]. GPU approaches \[undefp\] merge multiple parallelism levels. The cuRobo \[undef\] planner uses GPU-parallel multi-seed trajectory optimization, imposing soft penalties for constraint adherence as is typical \[undefq, undefr\] However, soft formulations do not guarantee strict manifold adherence.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Parallelized Motion Planning", "weight": 1.0} -->

Our approach builds off of VAMP \[undefc\], which performs vectorized collision checking through CPU SIMD, showing tremendous speedup. Another recent work, cPRRTC \[undefs\], showed that parallelizing projection can accelerate constrained motion planning. Our approach demonstrates that VAMP's insight of batching validation across an edge holds also for manifold projection, providing order-of-magnitude speedups over baseline approaches.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-B Whole Body Planning", "weight": 1.0} -->

Whole-body humanoid planning must satisfy multiple constraints (balance, collision avoidance, task poses) for high-DoF systems (\>25 DoF), making these spaces highly non-convex. For multiple constraint satisfaction, \[undeft\] use hierarchical null-space projection, which does not handle conflicting constraints well. \[undefu\] introduce the Constellation technique for conflicting constraints, which \[undefv\] build upon by proposing constrained nonlinear Kaczmarz for large constraint sets. We use cyclic projection in our approach to handle many constraints simultaneously.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-B Whole Body Planning", "weight": 1.0} -->

Specific to humanoids, planners such as CBiRRT \[undefd\] have tackled the problem, but are not fast enough for real-time scenarios. \[undefw\] speed up planning by learning feasible configurations of the system, but require large amounts of training data. IK-based reactive control such as \[undefx\] are fast but often get stuck in local minima.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Methodology", "weight": 1.0} -->

In manifold-constrained sampling-based motion planning, local connections between configurations should satisfy constraints. Typically, these are approximations of a geodesic on the constraint submanifold, and are computationally expensive to generate. Our primary contribution is vectorizing the generation of constraint satisfying motion by parallelizing the projection step that maps configurations onto the constraint manifold. The key insight is that multiple configurations along an extension can be projected and checked in parallel using SIMD operations, dramatically reducing the overall cost of constraint satisfaction. We first present the complete manifold-constrained RRT-Connect algorithm, then detail the vectorized projection mechanism, and finally discuss the choices that went into the design of our planner.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Methodology", "weight": 1.0} -->

3: while iter < MaxIterations do 5: qneara ← Nearest(Ta, qrand) 6: $q^{a}_{\text{proj}}\leftarrow{\color[rgb]{0.25390625,0.41015625,0.8828125}\definecolor[named]{pgfstrokecolor}{rgb}{0.25390625,0.41015625,0.8828125}\text{ParallelConstrainedExtend}}(T_{\text{a}},q^{a}_{\text{near}},q_{\text{rand}})$

<!-- chunk {"id": "body-0017", "role": "body", "section": "Methodology", "weight": 1.0} -->

$q^{a}_{\text{proj}}\leftarrow{\color[rgb]{0.25390625,0.41015625,0.8828125}\definecolor[named]{pgfstrokecolor}{rgb}{0.25390625,0.41015625,0.8828125}\text{ParallelConstrainedExtend}}(T_{\text{a}},q^{a}_{\text{proj}},q^{b}_{\text{near}})$ 10: if qproja = qnearb then Algorithm 1 Vectorized Manifold-Constrained RRT-Connect 1: T, qs, qtarget, ℱ, r, σ, n= SIMD width (e.g.,

<!-- chunk {"id": "body-0018", "role": "body", "section": "Methodology", "weight": 1.0} -->

$v_{\text{extend}}\leftarrow\frac{q_{\text{target}}-q_{s}}{\|q_{\text{target}}-q_{s}\|}$ 5: qsteer ← qs + dist ⋅ vextend 6: qparticles(i) ← qsteer + ϵivextend, ϵi ∼ 𝒩(0, σ2), i = 1, …, n 7: qproj ← ParallelProject(qparticles) 8: if $q_{\text{proj}}=\textsc{NULL}$ then 10: if ¬CollisionFree(qproj)∨∥qproj − qs∥ > 2 ⋅ dist then 12: qinterp ← n interpolated points between qs and qproj 13: qint_proj ← ParallelProject(qinterp) 14: if $\exists

<!-- chunk {"id": "body-0019", "role": "body", "section": "Methodology", "weight": 1.0} -->

i:\big\|q_{\text{int_proj}}^{(i)}-q_{\text{int_proj}}^{(i+1)}\big\|>\frac{r}{n}$ then 15: return NULL ⊳ Projected points too far apart 16: ⊳ Recursively interpolate and project until resolution δ is met ⊲ 24: return qparticles ⊳ All particles converged 25: step ← getDescentStep(qparticles) 26: if ∃i: ∥step(i)∥ > MaxDistance then 27: return NULL ⊳ Projection diverging 28: qparticles ← qparticles + step 34: Δq ← αJiT(JiJiT + λI)−1d (or α(JiTJi + λI)−1JiTd) 36: return qparticles − qinit

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Vectorized Projection-Based Sampling-Based Planning", "weight": 1.0} -->

[width=0.99]svg-inkscape/methodology_horizontal_svg-tex.pdf_tex Figure 2: Methodology. (a) RRT-Extend Step: A random configuration in ambient space is sampled. (b) qsteer is computed at a fixed distance from qnear and samples around qsteer are projected onto the manifold until any one succeeds. (c) Interpolated samples along the vector connecting the start and the initial projected point are projected in parallel. (d) Configurations are interpolated between the projected particles and are projected and validated recursively until desired resolution is achieved. n = 4 here for illustrative purposes, each represented by a different color.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Vectorized Projection-Based Sampling-Based Planning", "weight": 1.0} -->

Our parallel vectorized manifold-constrained RRT-Connect algorithm is presented in Alg.˜1. This is a variant of the RRT-Connect algorithm \[undeff\] where all nodes and edges lie on the manifold $\mathcal{M}_{\text{free}}$ up to some discretization resolution $\delta$. In practice, we also use the dynamic-domain \[undefy\] and balancing heuristics \[undefz\], but have elided these from the pseudocode for clarity.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Vectorized Projection-Based Sampling-Based Planning", "weight": 1.0} -->

First, a $q_{rand}$ is sampled from the ambient space, and its nearest neighbor $q_{near}$ is found ( Alg 1, Line 5). The ParallelConstrainedExtend method attempts to connect $q_{near}$ to $q_{rand}$ ( Alg 1, Line 6). If the extension is successful, the planner repeatedly attempts to grow the projected configuration toward the goal tree using the same ParallelConstrainedExtend method with a fixed extension step size.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-A Vectorized Projection-Based Sampling-Based Planning", "weight": 1.0} -->

The key contribution of our work is the vectorized ParallelConstrainedExtend method (Alg.˜2). Following the intuition and empirical results from VAMP \[undefc\] we focus on the constrained motion validation step, and parallelize the projection and validation of interpolated configurations. However, this is not trivial since each point along the extension vector (i) could be at different distances from the manifold, and (ii) have to be projected such that there is a continuous path on the manifold between the projected points. To deal with these issues, we present a two step vectorized approach. Throughout the rest of the discussion, $n$ denotes the number of parallelized operations.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-A Vectorized Projection-Based Sampling-Based Planning", "weight": 1.0} -->

First, $q_{steer}$ (Alg 2, Line 5) is computed at a fixed distance away from $q_{near}$ along the vector $q_{nr}$. Then we sample $n$ points around $q_{steer}$ (Alg 2, Line 6) on direction vector, and attempt to project all points onto the manifold. We exit if any of them succeed and record the particle that succeeds the earliest, as $q_{proj}$ (Alg 2, Line 7). Then, $n$ points are linearly interpolated between $q_{near}$ and $q_{proj}$ and projected onto the manifold (Alg 2, Line 12) in parallel. The next batch of $n$ points are recursively interpolated and projected between adjacent projected points until the desired motion validation resolution is achieved. Collision checking is performed in parallel after projection, and we exit early if any projected point is in collision.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-A Vectorized Projection-Based Sampling-Based Planning", "weight": 1.0} -->

Sine the number of points to check along the motion vector is typically small (on the order of 8--64), this is perfectly suited to SIMD parallelization, which provides a high throughput without significant overhead, and allows flexible interleaving of sequential and parallel code, something that an iterative optimization method benefits. To support data parallelism necessary for SIMD instructions, all configurations, function evaluations, and Jacobians are stored in a structure-of-arrays layout.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-A Vectorized Projection-Based Sampling-Based Planning", "weight": 1.0} -->

The critical component of the parallel extend method is parallel projection of multiple points onto the manifold. To be able to perform this, a few pieces are needed.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A Vectorized Projection-Based Sampling-Based Planning", "weight": 1.0} -->

Tracing Compiler for Constraints In a manner similar to VAMP, we generate SIMD parallel code for evaluating constraint functions using a tracing compiler to *trace* the low-level operations needed to compute the distanceToConstraint (Alg 2, Line 22). We use build upon the existing tracing compiler used by VAMP which uses Pinocchio \[undefaa\] and CppAD \[undefab\] to generate efficient, branch-free, loop-unrolled code for robot kinematics, which is amenable to SIMD operations. By using automatic differentiation during the tracing process, we efficiently compute the corresponding Jacobian matrices of the constraint functions. To enable gradient-based optimization, we implement a differentiable version of $\operatorname{log}(R_{s^{\prime}}^{w})^{\vee}$ by using a first order Taylor Series approximation of the sinc function at singularities.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A Vectorized Projection-Based Sampling-Based Planning", "weight": 1.0} -->

Vectorized Levenberg--Marquardt: In addition to tracing the constraint functions and Jacobians, we also subsequently trace one step of the Levenberg-Marquardt (LM) algorithm to be able to more efficiently perform the gradient descent in projection. We exploit the known dimensionality of the robot and the constraint functions by using a second-order LM algorithm. To achieve this, we trace compile the Jacobian matrix pseudoinversion for each constraint. Given the semipositive definite (SPD) formulation of the LM step, we implement a custom Cholesky decomposition method \[undefac\], which also follows the SIMD principle of branchless control flow, and the fixed dimensionality allows us to perform loop-unrolled Cholesky solve expressions that can be parallelized. This subroutine is compiled for each constraint and allows us to perform one LM step in parallel for multiple particles. We provide both the inner and outer matrix pseudoinversions, the former is bounded by the dimension of the manifold function while the latter is bounded by the dimension of the robot.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Design Choices", "weight": 1.0} -->

Vectorized projection provides a twofold benefit. First, we can quickly project and evaluate multiple configurations in parallel, which provides naively an $n$-times speed-up compared to the sequential counterpart. More importantly, the parallel step also allows us to invalidate infeasible configurations very quickly, reducing wasted computations, which leads to the empirical 100-times speed-up we see in our experiments. By checking future configurations further along the validate step, we can cheaply invalidate the entire motion if any particle fails to project or is in collision. This follows the ethos of sampling-based planning by quickly invalidating infeasible motion to focus search elsewhere.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Design Choices", "weight": 1.0} -->

Early Exits The independent parallel nature of projection can cause inconsistencies where the interpolated points project to different parts of the manifold. Validating the connection between these points requires further interpolation, which may become unbounded. We avoid this altogether by exiting projection early if any particle has a large descent step, which likely indicates that the particles may be quite far from each other. Alg 2, Line 10 perform this early exit at different levels and invalidate the entire motion validation if any particle violates a projection distance threshold.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Design Choices", "weight": 1.0} -->

Two-Stage Projection While the two-stage projection may seem unnecessary at first (as prior projection-based planners simply interpolate towards $q_{steer}$), for hard constraints this reduces the likelihood of interpolated points projecting far away from each other during descent, as they are already quite close to the manifold. We provide an ablation study of this in Sec.˜V-B. The two-step projection also behaves as an adaptive range parameter for extension step: by sampling points around $q_{steer}$, depending on the difficulty of the constraint, a point that is either closer or farther away from the manifold could be projected the earliest, and overall provides higher chance of successful extension.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Design Choices", "weight": 1.0} -->

Consequently, our tree growth approach is built with the following principles: (i) stay close to the manifold while extending to limit the amount of computationally expensive projection iterations, and (ii) employ particle-based optimization to improve the success of manifold sampling, as even when the initial seeds are proximal in the ambient space the local gradient landscape can lead to divergent behavior. [width=0.7]svg-inkscape/manifold_intersection_svg-tex.pdf_tex Figure 3: Cyclic Projection to intersection of manifolds. At each iteration, we take one step towards each manifold in a pre-determined order, and the algorithm stops when we reach their intersections

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-C Composition of Constraints", "weight": 1.0} -->

Some problems require satisfying multiple constraints, e.g., a humanoid carrying an object, as we explore in Sec.˜V-C. Thus, we need to be able to support multiple constraints, which translates to projecting onto the intersection of the manifolds, as seen in Fig.˜3. Naively, these constraints can be combined into one large system of equations, but this scales poorly, as noted by \[undefv\]. We use a cyclic projection technique \[undefad\], described in Alg 2, Line 31. During each iteration of optimization, we compute the descent direction of one constraint and takes a step in that direction. Constraints are cycled through in a predetermined order, and this step is repeated until we converge onto the intersection of all constraint manifolds. Although it is a simple approach, it empirically works well, since its simplicity allows parallelization at no additional cost.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experimental Evaluation", "weight": 1.0} -->

We evaluate our planner on a wide suite of problems with different types and complexities of constraints. We test it out on 3 different robots: the Franka Emika Panda Arm (7-DoF), a bimanual Kuka IIWA system (14-DoF), and the Digit Robot (36-Dof, including a 6-DoF floating base). We primarily evaluate our planner against the projection-based manifold-constrained RRT-Connect implementation from OMPL \[undefae, undefaf\] and CuRobo \[undef\] for the Panda arm. We perform hyperparameter sweeps on all planners on each problem and choose the best performing configuration. For fair comparison, OMPL uses the collision checking of VAMP; constraint evaluation is done using Pinocchio \[undefaa\]. For the Bimanual KUKA IIWA arm, we compare against the approach of \[undefl\]. All algorithms were tested on an 5.4Ghz Intel i7-13700K CPU with 64GB of RAM and an NVIDIA RTX 4090 GPU with 24GB VRAM (for CuRobo).

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A End-Effector Constraint for a Single Arm", "weight": 1.0} -->

\includeinkscape[width=]svg-inkscape/line_plane_problems_cdf_svg-tex.pdf_tex Figure 5: CDF plot benchmarking planner performance for the line and plane constrained problems, binned by number of environment obstacles. 1. LP - Line with Position Constraint only, 2. LPO - Line with Position and Orientation Constraint, 3. PP - Plane with Position Constraint, 4. PPO - Plane with Position and Orientation Constraint For most problems, McVAMP is 1000 times faster than the baselines achieving a 100% success rates, while the other planners suffer in the success rate as the number of obstacles increases.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-A End-Effector Constraint for a Single Arm", "weight": 1.0} -->

We first evaluate our constrained planner on the 7-DoF Franka Emika Panda arm. We test on 4 constraints: keeping the end-effector on a plane (i) without an orientation constraint and (ii) with a fixed orientation, and keeping the end-effector on a line (iii) without and (iv) with an orientation constraint. An example problem can be seen in Fig.˜4. To generate the problems, we sample from a set of pre-defined lines and planes as constraints and sample valid start and goal configurations on the constraint. For each start-goal pair we incrementally add obstacles in the task space. Finally, we run our planner with many different hyperparameters and retain the problem even if any succeed. Note that CuRobo's constrained planner does not allow providing joint space configurations goals; we provide the end-effector pose of the goal configuration. We set a timeout of 10 seconds for OMPL after which the planner reports failure.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-A End-Effector Constraint for a Single Arm", "weight": 1.0} -->

Fig.˜5 shows the results for each class of constraint problem over a range of obstacle densities. In general, across all benchmarks we obtain superior performance in terms of planning time, with 100% success even as the difficulty increases. Most plans are under 1ms, which is anywhere from 100--2000$\times$ faster than the OMPL and CuRobo baselines.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A End-Effector Constraint for a Single Arm", "weight": 1.0} -->

(a) Generated plan to solve the maze (b) Real-time replanning for dynamic environments Figure 6: Solving a Maze. Here the tip of the marker is constrained to the floor of the maze. Consequently, the robot has to solve the maze to find a plan from start to goal. Planning is done at 20Hz. (b) when a dynamic obstacle blocks the path (red sphere here), the planner can compute a new path due to the high motion validation and planning throughput Next, we evaluate the effectiveness of our planner to navigate complex environments while respecting constraints using a maze (shown in Fig.˜6). We initialize 100 random start goal pairs at different points on the maze a minimum distance apart. We attach a marker to the end effector of the robot, whose tip is constrained to the bottom plane of the maze. In addition, we also impose an orientation constraint, such that only the yaw is free (i.e., the marker is free to rotate about its axis). We benchmark our algorithm against OMPL. As an ablation study, we replace the Pinocchio-based projection of OMPL with our compiled projection. For OMPL, we set the timeout to 100 seconds.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-A End-Effector Constraint for a Single Arm", "weight": 1.0} -->

From the results in Table˜I, our planner shows a remarkable improvement on planning times and success rates, achieving over a 1000$\times$ speed-up in some cases, opening the door to real-time planning for hard manifold constraint problems. We illustrate this in Fig.˜6(b) where the planner is able to avoid a dynamic obstacle that blocks its current path.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B Bimanual Arm Constraint", "weight": 1.0} -->

To test the scalability of the planner to higher dimensions, we evaluate it on a box transport problem with a bimanual system. In this task, the 14-Dof arms are constrained such that the relative transform between the left and the right arm must be fixed throughout the motion, i.e., holding the box. To enforce this constraint, we formulate it as a TSR constraint: Following \[undefl\], we evaluate our planner on the same problem of moving the arms between shelves while maintaining the relative pose and avoiding collisions. For baselines, we use compare against both their IK-BiRRT planner as well as the IK-GCS approach; these both use a pre-computed analytic representation of the manifold constraint.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-B Bimanual Arm Constraint", "weight": 1.0} -->

As this problem is more complex and higher-dimensional, we evaluate an ablation our two stage projection approach to prove its value. We test a single-stage projection, where points are interpolated between $q_{near}$ and $q_{steer}$ (McVAMP 1-step). Table˜II shows the results of the planners.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-B Bimanual Arm Constraint", "weight": 1.0} -->

Our approach provides 30--60$\times$ speed-up for solving the task compared to IK-BiRRT, and more than a 10$\times$ speed-up compared to IK-GCS. This result is interesting as IK-GCS requires pre-processing (about 70 seconds) to compute the graph of convex sets, which we do not count for benchmarking. However, IK-GCS produces shorter paths, owing to their optimization-based formulation. Our 2-step projection also outperforms the 1-step parallel projection approach, which indicates that it is beneficial as the complexity of the constraints increase.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-C Whole Body Planning", "weight": 1.0} -->

In this scenario, we scale beyond beyond constraints on just the end-effector of a fixed-based manipulator and evaluate the ability to tackle composition of constraints. We implement our planner for the Digit robot to perform quasi-static whole body planning to transport a box. The Digit robot has 30 joints and 6-DoF floating base. Of these 30 joints, 4 are high-stiffness springs, while another 6 are passive and constrained by closed-loop linkages. By assuming rigidity of the 4 spring joints and relying on the low-level tracking controller to handle the 4 closed-loop linkages associated with the ankles, we model it as a 28-Dof system, composed of 22 joints and a 6-Dof floating base, where 2 joints are passive and constrained by 2 closed-loop linkages. To generate a feasible motion plan for the Digit, the motion must respect the following four constraints (equations detailed in Fig.˜7): Stability Constraint: To maintain balance, the $xy$-projection of the center of mass (CoM), $\mathbf{x}_{com}^{xy}$, must remain within the convex hull of the support polygon $P$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-C Whole Body Planning", "weight": 1.0} -->

The error is to the nearest point in the hull.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-C Whole Body Planning", "weight": 1.0} -->

Feet Constraint (TSR): For fixed feet placement, we stack the 6-DoF pose errors for both feet ($f\in\{l,r\}$) into a 12-element vector.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-C Whole Body Planning", "weight": 1.0} -->

Closed Link Constraint: The closed loop linkages between the hip and the tarsus joint are enforced as fixed lengths between the two links.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-C Whole Body Planning", "weight": 1.0} -->

Bimanual Constraint: The relative pose between the hands is fixed, same as in Sec.˜V-B.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-C Whole Body Planning", "weight": 1.0} -->

Satisfying the first three constraints is essential for the Digit, as they are required for stability and real-world operation. To control the robot to track the planned joint trajectory, a passivity-based controller \[undefag\] is used to generate feedforward motor torque commands that compensate for the ground reaction forces, and uses proportional-derivative feedback to correct tracking error.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-C Whole Body Planning", "weight": 1.0} -->

We evaluate our planner in two real-world experiments. In additional to planning time, we also verify successful planning by reporting the tracking errors of relevant joints. A small tracking error indicates that the motion plan is more dynamically feasible, as the controller does not need to adjust motion to respect the stability, feet, and closed-link constraints. For these tasks, the planner was run on a 4.8GHz Intel Core Ultra 7 258V device with 32GB of RAM.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-C1 Box Transport", "weight": 1.0} -->

For this task, the robot is required to transport the box between three levels of the shelf, shown in Fig.˜1. Each task is repeated 3 times; Table˜III shows the planning times for each task. For motion segment, we show the distribution of the tracking error of the highest offending joints (the knee and the tarsus joints). Errors range less than 10 degrees on average, with a max error across all joints of 12 degrees at a single point for the left tarsus joint.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-C1 Box Transport", "weight": 1.0} -->

Tracking error (deg) Left Knee Joint Left Tarsus Joint Right Knee Joint Right Tarsus Joint Note: S: Standing Pose, T: Top, B: Bottom, M: Middle.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-C2 Dynamic Obstacle Avoidance", "weight": 1.0} -->

Here, the humanoid robot is tasked to repeatedly plan and execute a box transport task between fixed locations. A dynamic obstacle is introduced, and we test the ability of the robot to react and avoid the obstacles. Fig.˜8(a) illustrates the motion of the robot, while Fig.˜8(b) shows the tracking error and planning times.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-C2 Dynamic Obstacle Avoidance", "weight": 1.0} -->

(a) Whole-body trajectory execution in dynamic environment. During the upward motion, an obstacle is detected, the robot plans a feasible trajectory around the obstacle.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-C2 Dynamic Obstacle Avoidance", "weight": 1.0} -->

(b) Tracking error and planning times for the repeated start-goal-start motions for the bimanual Figure 8: Experimental results for dynamic environment obstacle avoidance.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-C2 Dynamic Obstacle Avoidance", "weight": 1.0} -->

Our planner is able to generate feasible trajectories in under 40ms, with the majority of planning times taking under 10ms, thereby enabling quick reactions to changing environments. All trajectories generated were feasible, and tracking errors remained under 8 degrees for the worst offending joints.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this work, we present a vectorized manifold-constrained sampling-based motion planner that is capable of generating constraint-satisfying motion plans on the order of milliseconds, achieving over 500$\times$ speedup in challenging, cluttered, and high-dimensional problems. We also demonstrate the scalability of our approach by tackling a real-time, whole body control problem with a 28-DoF Digit humanoid, demonstrating reactive real-time constraint-satisfying planning in dynamic environments. We believe that this capability opens up many possibilities for real-world tasks, and potentially for tackling more complex planning problems such as whole-body task and motion planning for humanoid robots.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

For future work, we are interested in investigating extensions to the manifold-constrained formulation that could be extended to kinodynamic planning, moving beyond the limitations of quasi-static planning. There are also improvements to the current planner that could be explored that are known in the literature, such as more sophisticated optimization techniques and integrating with continuation based methods. We also plan to investigate dynamic constraint and robot compilation, as currently our approach requires knowledge of constraints *a priori* to generate efficient SIMD kernels.
