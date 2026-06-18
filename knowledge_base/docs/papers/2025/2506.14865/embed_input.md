<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization

Topics include Trajectory optimization, Constrained optimization, Projection methods, Real-time, Robot motion planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Uses geometric projection operations to efficiently handle motion constraints in real-time robot trajectory optimization, avoiding full constraint Jacobian computations and achieving significant speedups over augmented Lagrangian approaches.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Generating motions for robots interacting with objects of various shapes is a complex challenge, further complicated by the robot geometry and multiple desired behaviors. While current robot programming tools (such as inverse kinematics, collision avoidance, and manipulation planning) often treat these problems as constrained optimization, many existing solvers focus on specific problem domains or do not exploit geometric constraints effectively. We propose an efficient first-order method, Augmented Lagrangian Spectral Projected Gradient Descent (ALSPG), which leverages geometric projections via Euclidean projections, Minkowski sums, and basis functions. We show that by using geometric constraints rather than full constraints and gradients, ALSPG significantly improves real-time performance. Compared to second-order methods like iLQR, ALSPG remains competitive in the unconstrained case. We validate our method through toy examples and extensive simulations, and demonstrate its effectiveness on a 7-axis Franka robot, a 6-axis P-Rob robot and a 1:10 scale car in real-world experiments. Source codes, experimental data and videos are available on the project webpage: this https URL

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many robotics tasks are framed as constrained optimization problems. For example, inverse kinematics (IK) seeks a robot configuration that matches a desired pose while respecting constraints like joint limits or stability. Motion planning and optimal control aim to determine trajectories or control commands that satisfy task-specific dynamics and environmental constraints. Model predictive control (MPC) solves real-time optimal control problems by addressing simplified, short-horizon constrained optimization problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Several second-order solvers such as SNOPT, SLSQP, LANCELOT, and IPOPT ---are commonly used to solve general constrained optimization problems. In robotics, however, most research focuses on solvers tailored to specific problems. For instance, constrained versions of differential dynamic programming (DDP), iterative linear quadratic regulator (iLQR), TrajOpt, and CHOMP are used for motion planning. However, many of these solvers are not open-source, making them difficult to benchmark and improve. Moreover, adapting them for real-time feedback applications, such as closed-loop IK and MPC, often requires significant tuning.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We address these challenges by proposing a simple yet powerful solver that can be easily implemented without requiring large memory resources. This solver exploits geometric constraints inherent to many robotic tasks, which can be described using geometric set primitives (see Table I). Examples include joint limits, center-of-mass stability, and avoiding or reaching geometric shapes (e.g., spheres or convex polytopes). These constraints can often be framed as projections rather than full constraint formulations. We argue that leveraging these projections, rather than treating constraints generically, can significantly improve solver performance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the simplest algorithms for handling such projections is projected gradient descent, where the gradient is projected to ensure the next iterate remains inside the constraint set. A more advanced version, spectral projected gradient descent (SPG), has demonstrated strong practical performance and is considered a competitive alternative to second-order solvers in various fields. Extensions of SPG to handle additional constraints using augmented Lagrangian methods have been explored. However, the application of these projection-based methods to popular second-order solvers in robotics has not been widely explored, resulting in a missed opportunity to fully exploit the potential of projections in this domain.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose an efficient projection-based optimization method that leverages geometric constraints in robotics tasks and extend Augmented Lagrangian Spectral Projected Gradient Descent (ALSPG) with a direct shooting method to handle multiple nonlinear constraints.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce and integrate various geometric projections including Euclidean projections, polytopic projections, and learning-based projections, into the ALSPG.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We validate our approach through numerical simulations on planar arm systems, Franka robot arms, humanoid robots, and autonomous vehicles, providing performance benchmarks and analysis against baseline methods. We further assess the effectiveness of our method through real-world experiments on 6-axis and 7-axis robotic arms and a 1:10 scale car.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In this section, we present the definitions of projections used in robotic problems to formulate constraints such as constrained inverse kinematics, obstacle avoidance and other manipulation planning problems.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Euclidean Projections", "weight": 1.0} -->

The solution ${\mathbf{x}}^{\ast}$ to the following constrained optimization problem

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Euclidean Projections", "weight": 1.0} -->

is called an Euclidean projection of the point ${\mathbf{x}}_{0}$ onto the set $\mathcal{C}$ and is denoted as ${\mathbf{x}}^{\ast} = {\Pi_{\mathcal{C}}{({\mathbf{x}}_{0})}}$. This operation determines the point ${\mathbf{x}} \in \mathcal{C}$ that is closest to ${\mathbf{x}}_{0}$ in Euclidean sense. For many sets $\mathcal{C}$, $\Pi_{\mathcal{C}}{( \cdot )}$ admits analytical expressions that are given in Table I. Even though, usually, these sets are convex (e.g. bounded domains), some nonconvex sets also admit analytical solution(s) that are easy to compute (e.g. being outside of a sphere). In cases $\mathcal{C}$ is non-convex, multiple feasible solutions may exist.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Euclidean Projections", "weight": 1.0} -->

In such situations, either a strategy for selecting the solution or a convex decomposition method may be required. Note that many of these sets are frequently used in robotics, from joint/torque limits and avoiding spherical/square obstacles to satisfying virtual fixtures defined in the task space of the robot.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B Polytopic Projections", "weight": 1.0} -->

The geometries of mobile robots often vary, and they can be represented as polytopes defined by hyperplanes. When considering the robot's geometry, Euclidean projections may not always be applicable. It becomes necessary to account for projections between the robot (modeled as a polytope) and obstacles. Let the robot's shape be convex, with its occupied space denoted as the set $\mathcal{C}_{r}$. The geometric center of the polytopic robot, denoted ${\mathbf{p}} \in {\mathbb{R}}^{n}$, serves as the point of interest for control and collision avoidance. We consider the obstacles or goal regions as convex polytopes in ${\mathbb{R}}^{n}$ (with $n = 2$ or $3$). If the shapes are not convex, the convex-hulls or convex-decomposition can be employed to approximate them as a collection of convex polytopes.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Polytopic Projections", "weight": 1.0} -->

where $\mathcal{M}$ is the configuration space obstacle for translation movements of robots. If the geometric center $p \in \mathcal{M}$, the robot and the polytope object intersect. The problem of projections between two polytopic sets then reduces to projections between the geometric center $\mathbf{p}$ and the Minkowski sum $\mathcal{M}$, since $\mathcal{M}$ is composed of hyperplanes, projecting a point out of a polytope, ${\mathbf{x}}^{\ast} = {\Pi_{\mathcal{M}}{({\mathbf{x}}_{0})}}$, can be resolved using the method outlined I, as shown in Fig. 2. The robot's rotational movements can be accounted for by augmenting the Minkowski set with an additional dimension.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-C Implicit Projections", "weight": 1.0} -->

When the shape of the object is implicit and cannot be expressed using hyperplanes, learning-based techniques can be employed to design the projections. Bernstein polynomial basis functions are efficient for learning the implicit shape. The advantage of this approach lies in the availability of analytical and smooth gradient information. Assuming the order of the polynomials is $r$ and there are $c$ control points, the matrix form of the implicit shape is $\mathcal{S}:={{\mathbf{t}}^{\top}{\mathbf{M}}\Phi}$, where ${\mathbf{t}} \in {\mathbb{R}}^{r}$ is the time vector, and ${\mathbf{M}} \in {\mathbb{R}}^{r \times c}$ is the characteristic matrix and $\Phi \in {\mathbb{R}}^{c}$ represents the control points. The analytical gradient $\nabla_{t}\mathcal{S}$ can be computed efficiently. The implicit projection is demonstrated in Fig. 2.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Augmented Lagrangian Spectral Projected Gradient Descent for Robotics", "weight": 1.0} -->

This section gives the SPG algorithm along with the non-monotone line search procedure. These algorithms are easy to implement without big memory requirements and yet result in powerful solvers. Next, we give the ALSPG algorithm based on geometric projections. Finally, the direct shooting approach is adopted to formulate the constrained optimization problems for robotics.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Spectral Projected Gradient Descent", "weight": 1.0} -->

SPG is an improved version of a vanilla projected gradient descent using spectral stepsizes. Its excellent numerical results even in comparison to second-order methods have been a point of attraction in the optimization literature. SPG tackles constrained optimization problems in the form of

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Spectral Projected Gradient Descent", "weight": 1.0} -->

by constructing a local quadratic model of the objective function

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Spectral Projected Gradient Descent", "weight": 1.0} -->

and by minimizing it subject to the constraints as

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Spectral Projected Gradient Descent", "weight": 1.0} -->

The choice of $\gamma_{k}$ affects the convergence properties significantly since it introduces curvature information to the solver. Note that when choosing $\gamma_{k} = 1$, SPG is equivalent to the widely known projected gradient descent. SPG uses spectral stepsizes obtained by a least-square approximation of the Hessian matrix by $\gamma_{k}{\mathbf{I}}$. These spectral stepsizes are computed by proposals

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Augmented Lagrangian spectral projected gradient descent", "weight": 1.0} -->

SPG alone is usually not sufficient to solve problems in robotics with complicated nonlinear constraints. In, Jia *et al.* provides an augmented Lagrangian framework to solve problems with constraints ${{\mathbf{g}}{({\mathbf{x}})}} \in \mathcal{C}$ and ${\mathbf{x}} \in \mathcal{D}$, where ${\mathbf{g}}{( \cdot )}$ is a convex function, $\mathcal{C}$ is a convex set, and $\mathcal{D}$ is a closed nonempty set, both equipped with easy projections.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Augmented Lagrangian spectral projected gradient descent", "weight": 1.0} -->

In this section, we build on the work with the extension of multiple projections and additional general equality and inequality constraints. The general optimization problem that we are tackling here is

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Augmented Lagrangian spectral projected gradient descent", "weight": 1.0} -->

where ${\mathbf{g}}_{i}{( \cdot )}$ are assumed to be arbitrary nonlinear functions. Note that even though the convergence results apply to the case when these are convex functions and convex sets, we found in practice that the algorithm is powerful enough to extend to more general cases.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Augmented Lagrangian spectral projected gradient descent", "weight": 1.0} -->

We use the following augmented Lagrangian function

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-C Optimal Control with ALSPG", "weight": 1.0} -->

We consider the following generic constrained optimization problem

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we perform extensive simulations and real-world experiments on multiple robotic tasks, including IK problems, motion planning, MPC for a contact-rich pushing task, autonomous navigation and parking tasks. Real-world evaluations were conducted on a 7-axis Franka robot, a 6-axis P-Rob robot, and a 1:10 scale car. The motivation behind these experiments is to show that: 1) the proposed way of solving these robotics problems can be faster than the second-order methods such as iLQR and IPOPT; and 2) exploiting projections whenever we can, instead of leaving the constraints for the solver to treat them as generic constraints, increases the performance significantly.

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-A Inverse kinematics", "weight": 1.0} -->

We first evaluate the performance of SPG compared to iLQR^11^1The implementation and code of iLQR can refer to RCFS. in a reach planning task using a 7-axis manipulator without constraints. iLQR is implemented with dynamic programming. SPG is implemented as detailed in the previous section. Both implementations are in Python. The control input is $\overset{¨}{q} \in {\mathbb{R}}^{7}$ and the states are joint velocities and positions ${(\overset{˙}{q},q)} \in {\mathbb{R}}^{14}$. The results on Fig. 3(b) show that the convergence time scales linearly with the planning horizons due to the growing number of decision variables. Notably, SPG scales more efficiently than iLQR, demonstrating its potential for real-time applications.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-A Inverse kinematics", "weight": 1.0} -->

Num. of fun. eval.
Num of Jac. eval.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-A Inverse kinematics", "weight": 1.0} -->

A Constrained inverse kinematics problem can be described in many ways using projections. One typical way is to find a feasible ${\mathbf{q}} \in \mathcal{C}_{\mathbf{q}}$ that minimizes a cost to be away from a given initial configuration ${\mathbf{q}}_{0}$ while respecting general constraints ${{\mathbf{h}}{({\mathbf{q}})}} = \mathbf{0}$ and projection constraints ${{\mathbf{f}}{({\mathbf{q}})}} \in \mathcal{C}_{\mathbf{x}}$

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-A Inverse kinematics", "weight": 1.0} -->

where ${\mathbf{f}}{( \cdot )}$ can represent entities such as the end-effector pose or the center of mass for which the constraints are easier to be expressed as projections onto $\mathcal{C}_{\mathbf{x}}$, and $\mathcal{C}_{\mathbf{q}}$ can represent the configuration space within the joint limits. Fig. 4 shows a 3-axis planar manipulator with ${\mathbf{f}}{( \cdot )}$ representing the end-effector position and $\mathcal{C}_{\mathbf{x}}$ denoting feasible regions.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-A Inverse kinematics", "weight": 1.0} -->

Talos IK: We tested our algorithm on a high-dimensional (32 DoF) IK problem for the TALOS robot (see Fig. 5(a)), subject to the following constraints: i) the center of mass must remain inside a box; ii) the end-effector must lie within a sphere; and iii) the foot position and orientation are fixed. We compared two versions of the ALSPG algorithm: 1) by casting these constraints as projections onto $\mathcal{C}_{\mathbf{x}}$; and 2) by embedding all constraints within the function ${\mathbf{h}}{( \cdot )}$ to assess the direct advantages of exploiting projections in ALSPG. The algorithm was run from 1000 different random initial configurations for both versions, and we compared the number of function and Jacobian evaluations. The results, shown in Table II, demonstrate that using projections significantly improves efficiency.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A Inverse kinematics", "weight": 1.0} -->

Robust IK: In this experiment, we would like to achieve a task of reaching and staying in the half-space under a plane whose slope is stochastic because, for example, of the uncertainties in the measurements of the vision system. The constraint can be written as ${{\mathbf{a}}^{\top}{\mathbf{f}}{({\mathbf{q}})}} \leq 0$, where ${\mathbf{a}} \sim {\mathcal{N}{({\mathbf{μ}},\mathbf{\Sigma})}}$. We can transform it into a chance constraint to provide some safety guarantees probabilistically. The idea is to find a joint configuration $\mathbf{q}$ such that it will stay under a stochastic hyperplane with a probability of $\eta \geq 0.5$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A Inverse kinematics", "weight": 1.0} -->

which can be solved efficiently without using second-order cone (SOC) gradients, by using the proposed algorithm. We tested the algorithm on the 3-axis robot shown in Fig. 5(b) by optimizing for a joint configuration with a probability of $\eta = 0.8$ and then computing continuously the constraint violation for the last 1000 time steps by sampling a line slope from the given distribution. We obtained a constraint violation percentage of around 80%, as expected.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-B Motion planning and MPC on planar push", "weight": 1.0} -->

Non-prehensile manipulation has been widely studied as a challenging task for model-based planning and control, with the pusher-slider system as one of the most prominent examples (see Fig. 6). The reasons include hybrid dynamics with various interaction modes, underactuation and contact uncertainty. In this experiment, we study motion planning and MPC on this planar push system, without any constraints, to compare to a standard iLQR implementation. The cost function includes the control effort and the $L2$ norm measuring the difference between the final and target configurations. Fig. 6(b) illustrates the cost convergence for iLQR and ALSPG across 10 different targets for statistical analysis. Although iLQR seems to converge to medium accuracy faster than ALSPG, because of the difficulties in the task dynamics, it seems to get stuck at local minima very easily. On the other hand, ALSPG performs better in terms of variance and local minima. We applied MPC with iLQR and ALSPG with a horizon of 60 timesteps and stopped the MPC as soon as it reached the goal position with a desired precision.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-B Motion planning and MPC on planar push", "weight": 1.0} -->

Table III shows this comparison in terms of convergence time (s), number of function evaluations and number of Jacobian evaluations. According to these findings, ALSPG performs better than a standard iLQR, even when there are no constraints in the problem.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-B Motion planning and MPC on planar push", "weight": 1.0} -->

Num. of fun. eval.
Num. of Jac. eval.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B Motion planning and MPC on planar push", "weight": 1.0} -->

(a) Pusher-slider system path optimized by the proposed algorithm to go from the state to (0.1,0.1,π/3). Optimal control solved with SPG results in a smooth path for the pusher-slider system.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B Motion planning and MPC on planar push", "weight": 1.0} -->

(b) Convergence error mean and variance plot for iLQR and ALSPG motion planning algorithm for 10 different goal conditions starting from the same initial positions and control commands.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-C Motion planning with obstacle avoidance", "weight": 1.0} -->

Num. of fun. eval.
Num. of Jac. eval.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-C Motion planning with obstacle avoidance", "weight": 1.0} -->

Obstacle avoidance problems are usually described using geometric constraints. In autonomous parking tasks, obstacles and cars are usually described as 2D rectangular objects. In this experiment, we take a 2D double integrator point car reaching a target pose in the presence of rectangular obstacles (see Fig. 5(c)). We apply the ALSPG algorithm with and without projections to illustrate the main advantages of having an explicit projection function over direct constraints. The main difference is without projections, the solvers need to compute the gradient of the constraints, whereas with projections, this is not necessary. In order to understand the differences between first-order and second-order methods, we also compared ALSPG-Proj to AL-SLSQP with projections (SLSQP-Proj.), which is the same algorithm except the subproblem is solved by a second-order solver SLSQP from Scipy. The box obstacles allow analytical projections and distance computation. We performed 5 experiments, each with different settings of 4 rectangular obstacles and compared the convergence properties. The results are given in Table IV. The comparison, with and without projections, reports a clear advantage of using projections instead of plain constraints in the convergence properties.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-C Motion planning with obstacle avoidance", "weight": 1.0} -->

Although the convergence time comparison is not necessarily fair for SPG implementations as the SLSQP solver calls C++ functions, the comparison of ALSPG-Proj. and SLSQP-Proj. shows that ALSPG-Proj. still achieves lower convergence time. Additionally, we compare it against the optimization-based collision avoidance (OBCA) algorithm that is based on distance computation and IPOPT. The bicycle model is used ${{\overset{˙}{c}}_{x} = {v{\cos\theta}}},{{{\overset{˙}{c}}_{y} = {v{\sin\theta}}},{{\overset{˙}{\theta} = {\frac{v}{L}{\tan\delta}}},{\overset{˙}{v} = a}}}$. where $L = 2.7$ m is the wheelbase length. The system control inputs ${\mathbf{u}} = \lbrack\delta,a\rbrack$. Other parameters remain the same as the baseline.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-C Motion planning with obstacle avoidance", "weight": 1.0} -->

As shown in Table V, the results further validate the efficiency of our approach.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-D Autonomous Navigation on a 1:10 Scale Car", "weight": 1.0} -->

To further assess the effectiveness of our approach, we tested the ALSPG algorithm on a 1:10 scale vehicle executing a navigation task. The experiment was conducted on a 1:10 car, using an Intel ProU7 as the onboard computer. The sensor suite includes a Hokuyo UST-10LX LiDAR with a maximum scan frequency of 40 Hz. Odometry is provided by the VESC. Sensor fusion combines data from the LiDAR, the IMU embedded in the VESC, and odometry, utilizing the Cartographer to localize the vehicle and obtain its state. A pure-pursuit controller is implemented to track the given trajectory. The projections are constructed through polytopic projections and convex decomposition from section IV. The results shown in Fig. demonstrate the effectiveness of our method.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-E MPC for Real-Time Tracking on 7-axis Manipulator", "weight": 1.0} -->

We tested the ALSPG algorithm on the MPC problem of tracking an object with box constraints on the end-effector position of a Franka robot (see Fig. 9). An Aruco marker on the object is tracked by a camera held by another robot. In this experiment, the goal is to show the real-time applicability of the proposed algorithm for a constrained problem in the presence of disturbances. In Fig. 8, the error of the constraints and the objective function using formulation is given for 1 min. time period of MPC with a short horizon of 50 timesteps. Between 20s and 30s, the robot is disturbed by the user thanks to the compliant torque controller run on the robot. We can see that the algorithm drives smoothly the error to zero, see the accompanying video.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-F Chess Robot", "weight": 1.0} -->

We validated our algorithm through a three-month experimental study using a 6-axis P-Rob robot from F$\&$P Robotics to solve an inverse kinematics problem (position and orientation) with one degree of freedom (DoF) in orientation left unconstrained. The task involved grasping chess pieces, where the robot autonomously determined its orientation around the z-axis using SPG, compensating for workspace limitations that prevented full 6-DoF positioning, as shown in Fig.. The quaternion error, expressed via log-mapping, introduced nonlinearity and complexity, while joint limit projections ensured feasibility. After three months of public demonstrations, the system achieved a $100\%$ success rate.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we presented a fast first-order constrained optimization framework based on geometric projections, and applied it to various robotics problems ranging from inverse kinematics to motion planning. We showed that many of the geometric constraints can be rewritten as a logical combination of geometric primitives onto which the projections admit analytical expressions. We built an augmented Lagrangian method with spectral projected gradient descent as a subproblem solver for constrained optimization. We demonstrated: 1) the advantages of using projections when compared to setting up the geometric constraints as plain constraints with gradient information to the solvers; and 2) the advantages of using spectral projected gradient descent based motion planning compared to a standard second-order iLQR and IPOPT algorithm through different robot experiments. Sample-based MPC have been increasingly popular in recent years thanks to their fast practical implementations, despite their lack of theoretical guarantees. In contrast, second-order methods for MPC require a lot of computational power but with somewhat better convergence guarantees. We argue that ALSPG, being already in between these two methodologies in terms of these properties, promises great future work to combine it with sample-based MPC to further increase its advantages on both sides.
