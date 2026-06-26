<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

FATROP: A Fast Constrained Optimal Control Problem Solver for Robot Trajectory Optimization and Control

Topics include Trajectory optimization, Constrained optimization, Optimal control, Riccati factorization, Real-time, CasADi, Acados.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents FATROP, a fast OCP solver based on Riccati factorization of the KKT conditions, achieving sub-2ms solve times with C++ code generation via CasADi integration (ships with CasADi ≥3.6.7 which is also accessible from acados).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Trajectory optimization is a powerful tool for robot motion planning and control. State-of-the-art general-purpose nonlinear programming solvers are versatile, handle constraints effectively and provide a high numerical robustness, but they are slow because they do not fully exploit the optimal control problem structure at hand. Existing structure-exploiting solvers are fast, but they often lack techniques to deal with nonlinearity or rely on penalty methods to enforce (equality or inequality) path constraints. This work presents FATROP: a trajectory optimization solver that is fast and benefits from the salient features of general-purpose nonlinear optimization solvers. The speed-up is mainly achieved through the integration of a specialized linear solver, based on a Riccati recursion that is generalized to also support stagewise equality constraints. To demonstrate the algorithm's potential, it is bench-marked on a set of robot problems that are challenging from a numerical perspective, including problems with a minimum-time objective and no-collision constraints. The solver is shown to solve problems for trajectory generation of a quadrotor, a robot manipulator and a truck-trailer problem in a few tens of milliseconds.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The algorithm's C++-code implementation accompanies this work as open source software, released under the GNU Lesser General Public License (LGPL). This software framework may encourage and enable the robotics community to use trajectory optimization in more challenging applications.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nonlinear optimal control problems (OCP) are used in a wide range of engineering applications. In robotics, they provide a powerful tool for optimizing robot trajectories and controlling robotic systems. Trajectory optimization involves finding a control and state trajectory that is (locally) optimal in some metric while satisfying certain equality and inequality path constraints. This metric, or objective, can, for example, be related to total execution time, safety, energy use or user comfort, while the stagewise path constraints can enforce state and control limits, as well as encode a robot task, such as a path-following task with bounded allowable deviation for a robot end effector. Trajectory optimization has been applied to many robotics applications such as drone racing [foehn2021time,bos2022multistage], airborne wind energy systems [horn2013numerical], legged locomotion [mastalliquadruped] and collision-free robot motion planning [schulman2014motion].

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Apart from trajectory optimization, nonlinear OCPs are building blocks of model predictive control (MPC), which is a control strategy that has gained widespread popularity in the robotics community because of its ability to control complex, underactuated and highly-dynamical systems. MPC's potential in robotics has been demonstrated, for example, the control of autonomous racing cars [liniger2015racing] and legged robots [GrandiaMPClegged].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The computational efficiency of the nonlinear OCP solver is of critical importance for many applications, particularly in reactive sensor-based control applications, where robots have to rapidly adapt their actions to respond to disturbances or unpredictable changes in environment. Apart from being fast, the solver should also provide a high robustness due to the numerically challenging nature of the considered optimization problems.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

\mathbf{U}_K, \\& \mathbf{h}_k(\mathbf{u}_k, \mathbf{x}_k) =\mathbf{0}, \\& \mathbf{h}_K(\mathbf{x}_K) = \mathbf{0}, for $k = 0, 1, \dots, K-1$, with $K$ the horizon length, $\mathbf{x}_k$ the state variables, $\mathbf{u}_k$ the control or input variables, $l_k$, $\mathbf{f}_k$, $\mathbf{g}_k$ and $\mathbf{h}_k$ the functions representing the stage cost, the discrete dynamics, the inequality and equality path constraints, respectively.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Note that, because of the general stagewise equality constraints [eq:COCPeq1]-[eq:COCPeq2], this is a broader formulation than common in MPC where, usually, only one stagewise equality constraint is used, namely a constraint at the first time step that fixes the full state vector. An important problem class, incorporated by this COCP formulation is the boundary value problem where the initial and terminal states are fixed. The formulation [eq:COCP]also directly supports moving horizon estimation problems and furthermore, using helper states, the formulation can encode OCPs with minimum total time objective, multi-stage problems with unknown stage durations as well as periodic systems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Apart from a difference in formulation, nonlinear MPC and trajectory optimization problems have different solver requirements. In MPC, approximate optimal control inputs have to be computed within a specified sampling time, due to hard real-time requirements. An estimate of the solution is available from the previous control step, and only a local neighborhood of this approximate solution has to be explored, which is exploited in MPC-solvers to achieve higher sampling times [verschueren2022acados]. In trajectory optimization, in contrast, the optimization problem has to be solved to a high accuracy and an estimate of the solution is often not available. This requires advanced nonlinear programming techniques that provide robustness to cope with the numerically challenging nature of these problems. General-purpose nonlinear optimization algorithms, such as ipopt [wachter2006implementation], snopt [gill2005snopt] and knitro [knitro]provide this numerical robustness but they are slow because they do not fully exploit the COCP problem structure at hand.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contribution", "weight": 1.0} -->

The major contribution of this work is the development of a constrained nonlinear optimal control solver that fast and achieves a high numerical robustness. A high performance is achieved by exploiting the COCP structure, mainly by the integration of a specialized linear solver introduced in [generalizationriccati]. A high numerical robustness is obtained by implementing advanced nonlinear programming techniques. The algorithm is inspired ipopt and handles equality and inequality path constraints in the same way. The approach uses the multiple shooting formulation which naturally enables initialization from any, possibly infeasible, solution estimate. Furthermore, the the potential of the approach is demonstrated on a number of benchmark problems from a varying challenging nature. Finally, the fatrop open source software package that provides an efficient -implementation of the proposed algorithm is released under the LGPL.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Outline", "weight": 1.0} -->

The remainder of this paper is organized as follows. Section [sec:notation] introduces the notation used throughout this paper. and discusses preliminaries on nonlinear primal-dual interior point algorithms and direct shooting formulations. Section [sec:implementation] describes the implementation of the proposed algorithm and how the optimal control problem structure is exploited. Section [sec:benchmarks] introduces the considered benchmark problems. Section [sec:implementationdetails] deals with some details on how these problems are translated into optimal control problems and how the benchmark is performed. Finally, Section [sec:results] presents the results of the benchmark while Section [sec:conclusion] concludes the paper. Readers who are less familiar with or less interested in the details of the numerical algorithms can skip Sections I-III and jump immediately to Section IV to appreciate the improved performance of the presented solver compared to existing solvers when applied to trajectory optimization problems in robot motion planning and control.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Primal-Dual interior-point algorithm", "weight": 1.0} -->

In this section a concise introduction to primal-dual interior-point methods is given.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Primal-Dual interior-point algorithm", "weight": 1.0} -->

no convergence of full problem no convergence of barrier subproblem compute PD system at current iterate not reduced Hessian positive definite modify full space Hessian by adding scaled identity matrix find search direction (solve primal-dual system) find step size (line search) and compute next iterate decrease barrier parameter $\mu_j$ sketch of the primal-dual interior-point method Without loss of generality we consider a slack variable formulation optimization problem of the form: \minimize_{\mathbf{x}, \mathbf{s}} & \quad {f}(\mathbf{x}) \\\text{subject to} & \quad \mathbf{h}(\mathbf{x}) = \mathbf{0}, \\& \quad \mathbf{g}(\mathbf{x}) - \mathbf{s} = \mathbf{0}, \\& \quad \mathbf{s} \geq \mathbf{0}, where $\mathbf{x}$ and $\mathbf{s}$ are the decision and slack variables, respectively.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Primal-Dual interior-point algorithm", "weight": 1.0} -->

The slack inequality constraint is implemented by introducing a barrier term to the objective function: \minimize_{\mathbf{x}, \mathbf{s}} & \quad {f}(\mathbf{x}) -\mu_j \sum_i \log(s_i) \\\text{subject to} & \quad \mathbf{h}(\mathbf{x}) = \mathbf{0}, \\& \quad \mathbf{g}(\mathbf{x}) - \mathbf{s} = \mathbf{0}.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Primal-Dual interior-point algorithm", "weight": 1.0} -->

After introduction of the additional variables $z_i = \mu_j/s_i$ and some straightforward algebraic manipulation, the first-order necessary optimality conditions associated with [eq:general\_barrier] are: \nabla_{\mathbf{x}} \mathcal{L} = \mathbf{0}, \\\nabla_{\mathbf{s}} \mathcal{L} = \mathbf{0}, \\\mathbf{h}(\mathbf{x}) = \mathbf{0}, \\\mathbf{g}(\mathbf{x}) - \mathbf{s} = \mathbf{0}, \\\text{diag}(\mathbf{z}) \mathbf{s} = \mu_j \mathbf{e}, where the Lagrangian $\mathcal{L}$ is defined as: $$\mathcal{L}:= f(\mathbf{x}) + \boldsymbol{\lambda}_\mathbf{h}^\prime

<!-- chunk {"id": "body-0017", "role": "body", "section": "Primal-Dual interior-point algorithm", "weight": 1.0} -->

\mathbf{h}(\mathbf{x}) + \boldsymbol{\lambda}_\mathbf{g}^\prime (\mathbf{g}(\mathbf{x}) - \mathbf{s}) - \mathbf{z}^\prime \mathbf{s}.$$ Note that these conditions match the first-order optimality conditions of the original problem [eq:general\_opt] as the barrier parameter $\mu_j$ decreases to zero.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Primal-Dual interior-point algorithm", "weight": 1.0} -->

The last equation [eq:primal\_dual\_eqs\_centering], the centering equation, is a perturbed version of the original problem's complementarity condition. This means that the method can be viewed effectively as a homotopy method. The primal-dual interior-point method proceeds by applying Newton's method to this nonlinear system of equations.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Primal-Dual interior-point algorithm", "weight": 1.0} -->

\mathbf{S} & \mathbf{S} \mathbf{z} - \mu_j \mathbf{e} \tikz \draw[densely dotted] (1-|6)--(6-|6); Elimination of $\Delta \mathbf{s}$, $\Delta \boldsymbol{\lambda_g}$ and $\Delta \mathbf{z}$ results in a symmetric indefinite linear system of the form: \begin{bNiceMatrix}[first-row] \Delta \mathbf{x} & \Delta \boldsymbol{\lambda_h} \\\nabla ^2_{\mathbf{x}\mathbf{x}}\mathcal{L} + \mathbf{J_g} ^\prime \mathbf{S}^{-1} \mathbf{Z} \mathbf{J_g} & \mathbf{J_h} ^\prime & \boldsymbol{\gamma} \\\tikz \draw[densely dotted] (1-|3)--(3-|3);

<!-- chunk {"id": "body-0020", "role": "body", "section": "Primal-Dual interior-point algorithm", "weight": 1.0} -->

We will refer to this system as the reduced primal-dual system throughout the remainder of this paper. The iteration steps $\Delta \mathbf{s}$, $\Delta \boldsymbol{\lambda_g}$ and $\Delta \mathbf{z}$ can then be retrieved by the following expressions: & \Delta \mathbf{s} = \mathbf{J_g} \Delta \mathbf{x} + \mathbf{g} - \mathbf{s}, \\& \Delta \boldsymbol{\lambda_g} = - \boldsymbol{\lambda_g} -\mathbf{S}^{-1}(\mu_j \mathbf{e} - \mathbf{Z}\Delta \mathbf{s}), \\& \Delta \mathbf{z} = -\mathbf{z} + \mathbf{S}^{-1} (\mu_j \mathbf{e} - \mathbf{Z} \Delta \mathbf{s}).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Primal-Dual interior-point algorithm", "weight": 1.0} -->

The maximum primal and dual step size is chosen in such a way that the fraction-to-boundary rule is satisfied for every slack and dual bound variable, i.e. $s_{i} + \alpha_{\text{primal}}^{\text{max}} \Delta s_i \geq (1-\mu_j) s_{i}$ and $z_{i} + \alpha_{\text{dual}}^{\text{max}} \Delta z_i \geq (1-\mu_j) z_{i}$. For a more detailed introduction and analysis of primal-dual interior-point methods we refer to the textbook of Nocedal & Wright [nocedal2006numerical].

<!-- chunk {"id": "body-0022", "role": "body", "section": "Direct Multiple Shooting Formulation", "weight": 1.0} -->

In direct single shooting, all but the first state variable are eliminated by substituting the (discrete-time) dynamics equations. Multiple shooting, on the other hand, retains all state variables as decision variables, maintaining the dynamics equations as constraints of the nonlinear program. The latter approach is known to have superior convergence properties over the former in Newton-type optimization algorithms [albersmeyer2010lifted,giftthaler2018family]. Additionally, multiple shooting allows for initialization from a dynamically infeasible guess, unlike single shooting. The block-sparse structure of the primal-dual system, arising from the multiple shooting formulation, is exploited in the algorithm's linear solver.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Implementation", "weight": 1.0} -->

The nonlinear programming algorithm is heavily inspired by the primal-dual interior-point algorithm ipopt [wachter2006implementation], applied to the multiple shooting problem formulation. In this section an overview of the main implementation features of the proposed algorithm is given.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Filter Line Search Globalization", "weight": 1.0} -->

A filter line search procedure is used to promote global convergence [fletcher2002nonlinear]. The advantage of using a filter over a merit function acceptance criterion is that the filter's performance is not heavily dependent on the choice of algorithm parameters, such as the merit function's constraint violation penalty parameter.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Exact Hessian Information and Hessian Regularization", "weight": 1.0} -->

Exact Hessian information represents a problem better locally than Hessian approximations, hence it can drastically lower the number of required iterations and improve the numerical robustness. A difficulty with using exact Hessian information over Hessian approximation methods like Gauss-Newton and BFGS is that the exact Hessian is not guaranteed to be positive definite. It is common in line-search methods to require the reduced Hessian approximation, used for the computation of the search direction, to be positive definite. This guarantees that the computed search direction satisfies some descent properties for the filter line search criterion. Note that fatrop requires the reduced Hessian, this is the full space Hessian projected on the null-space of the constraint Jacobian, to be positive definite. This is a weaker requirement than positive definiteness of the full space Hessian. If the reduced Hessian is not positive definite, the full space Hessian is regularized by adding a multiple of the identity matrix.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Structure-Exploiting Linear Solver", "weight": 1.0} -->

At each iteration, the search direction is computed by solving the reduced primal-dual system [eq:reduced\_system]. Usually this is the most time consuming step of the algorithm. The stagewise structure of the COCP [eq:COCP] results in a block-sparse structure in the reduced primal-dual system. This block-sparse structure is the same as the KKT system of an equality-constrained OCP and can be exploited by a Riccati recursion that is generalized to also support stagewise equality constraints [generalizationriccati].

<!-- chunk {"id": "body-0027", "role": "body", "section": "Structure-Exploiting Linear Solver", "weight": 1.0} -->

The reduced primal-dual system structure for a horizon length of two $(K=2)$ is shown below: \begin{bNiceMatrix}[first-row] \mathbf{x}_2 & \mathbf{v}_2 & \boldsymbol{\pi}_2 & \mathbf{u}_1 & \mathbf{x}_1 & \boldsymbol{\lambda}_1 & \boldsymbol{\pi}_1 & \mathbf{u}_0 & \mathbf{x}_0 & \boldsymbol{\lambda}_0 & \\\mathbf{Q}_2 & \mathbf{H}_2^\prime & -\identm{} & & & & & & & & \mathbf{q}_2 \\-\identm{} & & & \mathbf{B}_1 & \mathbf{A}_1 & & & & & & \mathbf{b}_1 \\& & \mathbf{B}_1^\prime & \mathbf{R}_1 &

<!-- chunk {"id": "body-0028", "role": "body", "section": "Structure-Exploiting Linear Solver", "weight": 1.0} -->

\mathbf{r}_0 \\& & & & & & \mathbf{A}_0^\prime & \mathbf{S}_0 & \mathbf{Q}_0 & \mathbf{H}_{0,x}^\prime & \mathbf{q}_0 \\& & & & & & & \mathbf{H}_{0,u} & \mathbf{H}_{0,x} & & \mathbf{h}_0 \\\tikz \draw[densely dotted] (1-|11)--(11-|11); where $\mathbf{x}_k$ and $\mathbf{u}_k$ represent state and input variables, respectively, $\boldsymbol{\pi}_{k}$ represents the dual variables of the discretized dynamics equality constraints, while $\mathbf{v}_K$ and $\boldsymbol{\lambda}_k$ are the dual variables of the stagewise equality constraints.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Structure-Exploiting Linear Solver", "weight": 1.0} -->

\mathbf{S}_k^{-1}(\mu_j \mathbf{e} - \mathbf{Z}_k(\mathbf{g}_k-\mathbf{s}_k))), where $\mathbf{w}_k$ is the concatenation of $\mathbf{u}_k$ and $\mathbf{x}_k$ while $\mathbf{S}_k$ and $\mathbf{Z}_k$ represent the diagonal matrices of the slack variables and dual bound multipliers related to time step $k$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Structure-Exploiting Linear Solver", "weight": 1.0} -->

The used solution scheme only requires a full-rank constraint Jacobian and positive definite reduced Hessian. These conditions are required by the filter line search anyway. Moreover, the recursion is used as well to test the positive definiteness of the reduced Hessian at no extra cost, see Step 4 of the Algorithm Sketch. The computational complexity is linear in the horizon length. To achieve a high numerical accuracy, iterative refinement is deployed. For a more detailed overview we refer the reader to [generalizationriccati]. The blasfeo [frison2018blasfeo] library is used for the linear algebra operations in the algorithm. This library is optimized for the small-scale matrices that fit in cache memory, appearing in the proposed algorithm. The kernel routines of this library are optimized for many relevant target CPU architectures and use available CPU capabilities such as SIMD and FMA instruction set extensions.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Stagewise Function Evaluation", "weight": 1.0} -->

For the problems considered in this paper, the stagewise quantities of the primal-dual system are often the same functions for different time steps. This means that the code to evaluate these quantities can be re-used. This way the algorithm has a smaller instruction memory footprint, resulting in a better instruction locality. Because the code is kept small, it is feasible to apply aggressive compiler optimization levels. Furthermore, since all block submatrices are independent, they can be evaluated in parallel. This can be beneficial for problems with expensive function evaluation, for example multi-body problems with forward dynamics. A preliminary implementation using OpenMP is available in fatrop.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Other Algorithm Features", "weight": 1.0} -->

Other nonlinear programming features coming from ipopt that are currently implemented in the algorithm are: initialization procedure for the dual and the slack variables, second-order corrections, handling of degenerate constraint Jacobian, watchdog procedure, filter reset heuristic, handling of lower and upper bounds, handling of problems without a strict relative interior and handling of very small search directions. We refer to the ipopt implementation paper [wachter2006implementation] for a detailed description of these features. We emphasize that at the moment of writing, the algorithm does not support all features implemented ipopt, such as the feasibility restoration phase, automatic problem scaling and other features that are not described in the original implementation paper [wachter2006implementation], such as the adaptive barrier parameter update strategy. Ipopt did not invoke these algorithm features in the experiments of this paper.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Benchmark problems", "weight": 1.0} -->

Several dynamical systems are considered for which we set up different optimal control problems. The benchmark problems are of varying dimensions and complexity. Every problem of the benchmark can be classified either as a model predictive control or as a minimum-time problem. an unactuated pendulum is mounted on a cart, which is controlled by a horizontal force, with bounds on the cart position, velocity and control force. Model Predictive Control Problem: a disturbance is applied while the pendulum is in the upward equilibrium position. A quadratic objective encodes the task of stabilizing the pendulum while minimizing the total force input over the control horizon. Swing Minimum Total Time Problem: the pendulum starts in the downward configuration at a given cart position. The goal is to swing the pendulum to an upward position in minimum total time. Apart from the goal angle, also the translational velocity of the cart and the angular velocity of the pendulum are constrained to be zero at the beginning and end. this nonlinear model predictive control benchmark problem was introduced in [wirsching2006fast]. The dynamical system consists of a hanging chain of six masses that are connected by springs.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Benchmark problems", "weight": 1.0} -->

The leftmost mass is rigidly attached to the world and the velocity of the rightmost mass is controlled. The objective enforces stabilization of the system and the control inputs are limited. We consider both a 2D and a 3D version of this problem.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Benchmark problems", "weight": 1.0} -->

Quadrotor no-collision minimum total time problem with three obstacles. the orientation is represented by Euler angles. The control inputs are the acceleration in the upward direction of the drone and the Euler angle rates. The control inputs are limited. Model Predictive Control Problem: the quadrotor starts in horizontal equilibrium position. It is disturbed by a velocity and change in orientation. The quadratic objective encodes the task to stabilize the quadrotor and go back to the reference position and orientation. Point-to-point Minimum Total Time Problem: the task is to move the quadrotor from a given initial position and orientation to a given final position and orientation in minimum total time. The quadrotor has to start and end in equilibrium position. No-collision Minimum Total Time Problem: the task is the same as the point-to-point minimum total time problem, but now the quadrotor has to avoid cylindrical obstacles. There is a variant with a single obstacle and a variant with three obstacles. The latter task is shown in Figure [fig:drone]. Seven Degree of Freedom Robot Manipulator: the control inputs are the (seven) joint velocity setpoints of the robot.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Benchmark problems", "weight": 1.0} -->

The robot's joint position and joint velocity limits are taken into account.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Benchmark problems", "weight": 1.0} -->

Seven degree of freedom robot manipulator with a spherical obstacle.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Benchmark problems", "weight": 1.0} -->

The robot has to move from a given position in joint space to a target XYZ position of the end effector in minimum-time. The robot should avoid collision with a spherical object as shown in Figure [fig:robot]. The collision model is based on a capsule-based collision model provided by the robot manufacturer. Truck with Two Trailers: Optimal trajectory for truck with two trailers task, the truck and trailer are drawn in the terminal position. The colored lines indicate the trajectory of the coupling of truck and trailers. as indicated in Figure [fig:truck\_trailer], the task involves a truck with two trailers that starts with truck and trailer horizontally aligned and has to park truck and trailer aligned vertically at a given target location in minimum-time. A kinematic model is used with the control inputs being the steering angular velocities and the velocity of front wheels.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

#1$#2$[0.9]

<!-- chunk {"id": "body-0040", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Overview of the problem dimensions. The problems with an asterisk (*) are minimum-time problems. Furthermore, $K$ is the control horizon, $n_x$ the number of states, $n_u$ the number of controls, $n_i$ the number of inequality constraints, and $n_e$ and $n_e[K]$ the number of initial and terminal equality constraints, respectively. The slack variables, necessary for the smooth L1 no-collision constraints formulation, are included in the number of control variables (see Section sec:implementationdetails).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

In Table [tab:probdims] the dimensions of each problem are given. Below, we discuss how no-collision constraints and minimum-time problems were handled. in contrast to all other inequality constraints considered in this benchmark set, the no-collision constraints of the Quadrotor and Robot Manipulator were not implemented directly. This was because we observed in our experiments that the no-collision constraints had difficulties with the combination of the interior points method's strictly feasibility requirements of the slack variables and the nonconvex nature of the considered inequality constraints. Sometimes the feasibility restoration phase of ipopt was able to overcome this issue but, it sometimes required many iterations, converged to spurious local minima or even failed. At the moment of writing, fatrop does not implement the feasibility restoration phase, which makes the solver often fail if no-collision constraints are implemented as hard constraints. As a remedy, we formulated the no-collision constraints as L1-penalized soft constraints (for all solvers), using a smooth reformulation similar to TrajOpt, described in the implementation paper [schulman2014motion].

<!-- chunk {"id": "body-0042", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

The slack variable required by this smooth reformulation is implemented as an auxiliary control variable. While more efficient handling of slack variables is possible, see for example acados [verschueren2022acados], this approach was chosen for simplicity of implementation. We observed that, in our experiments with the ipopt solver, this formulation was more stable and faster than the direct hard constraints implementation of the no-collision constraints. Because of exactness of the L1-penalty method, the no-collision constraints were always satisfied to specified precision when a large enough penalty parameter was chosen. Minimum Total Time Problems. To formulate the minimum-time problems in the COCP [eq:COCP] form, we added an auxiliary state $T_k$, representing the total time variable. This state was constant over the whole control horizon $(T_{k+1} = T_k)$ and positiveness was enforced by adding the constraint $T_0 \geq 0$. This $T_k$ variable is then used to determine the integration step $\Delta t = T_k / K$ of the (uniform) integrator grid.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

We used rockit [gillis2020effortless] to formulate the OCPs, this is an optimal control problem framework, built on top of CasADi [andersson2019casadi]. We used the framework's implementation of the Runge-Kutta 4 integrator to transcribe problems' formulations from the continuous time to discrete time. rockit is interfaced to different solvers, including fatrop, ipopt and acados. Installation instructions, examples and the code for reproducing the results of the benchmark of this paper made available with this paper fatrop was compared to ipopt and, if the problem formulation allowed it, to the acados SQP algorithm. ipopt is a state-of-the-art general-purpose nonlinear optimization solver while acados is an OCP framework that implements a variety of algorithms with a strong focus on computation speed. It has some similarities to fatrop as both use blasfeo for linear algebra operations, are able to incorporate exact Hessian information and implement algorithms based on the direct multiple shooting formulation. The framework's SQP algorithm implements a line search globalization technique.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

The problem structure supported by the acados framework is less general (at the time of this writing) than fatrop (and ipopt) as equality path constraints are not supported, except for constraints that fix the initial state. All quantities needed by the algorithms were evaluated from compiled C-code, that was generated using CasADi [andersson2019casadi] SX functions. We used GCC 9.4.0 with compiler flags -Ofast -march=native for this purpose. Parallel function evaluation was not implemented for ipopt, so for fairness of comparison, this feature was turned off for both acados and fatrop. ipopt and fatrop used the same stopping criterion with a tolerance parameter tol of 1e-8. We used the default stopping criterion for acados. ipopt was configured to use the ma57 linear solver (sequential), compiled with metis and intel mkl. Blasfeo, the linear algebra library used by fatrop and acados, was compiled with X64\_INTEL\_HASWELL - HP target.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

For fatrop and ipopt we changed the default values of the algorithm parameters mu\_init to 1e2 and gamma\_theta to 1e-12, because it benefited the time optimal problems for both solvers. For acados, hpipm was used as inner QP solver with EXACT\_HESSIAN and CONVEXIFY presets. We tried out different numbers of partial condensing steps and took the results for the best performing setting. We provided discrete-time CasADi integrator expressions, because it resulted in function evaluation that was roughly two to three times faster than providing the continuous-time dynamics differential equations and using the built-in integrator. Our test machine was a notebook computer equipped with an Intel Core i7-10850H Processor, running Ubuntu 20.04, with Intel Turbo Boost disabled.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

fatrop and ipopt were able to solve all minimum-time benchmark problems to the specified accuracy, even though no initial solution guess was provided. A concern might be that the reduced system can become ill-conditioned when iterates come close to the inequality barriers. We did not observe that this led to numerical issues in our experiments, although many inequality constraints were active at the solution of the minimum-time problems. The benchmark results for the minimum-time problems are shown in Table [tab:walltimeipopt]. Although the iterations for fatrop and ipopt were similar for all problems, they were not exactly the same. This is because of the inexact arithmetic of the linear solvers leading to small step differences that are accumulated over the iterations. In some cases this led to a (small) difference in number of iterations. The linear solver used in ipopt was usually more accurate than the linear solver used in fatrop, but this did not lead to a significant difference in the number of iterations or robustness. We refer to the linear solver's paper [generalizationriccati] for a numerical comparison to some general-purpose sparse linear solvers.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

fatrop always outperformed ipopt, solving all problems in a few tens of milliseconds to about a hundred milliseconds.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

#1$#2$[0.8]

<!-- chunk {"id": "body-0049", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

| 2*problem name | 3c|fatrop | 3c|ipopt | | | | | Number of iterations, total and function evaluation wall time in milliseconds (ms) for the minimum time problems with fatrop and ipopt.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

Only the problems with an MPC formulation were benchmarked with acados, because this solver did not allow the problem formulation of the minimum time problems due to the presence of terminal (or path) equality constraints. The results for these problems are shown in Table [tab:walltimeipopt].

<!-- chunk {"id": "body-0051", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

#1$#2$[0.8]

<!-- chunk {"id": "body-0052", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

| 2*problem name | 3c|fatrop | 3c|acados | 3c|ipopt | | | | | | | Number of iterations, total and function evaluation wall time in milliseconds (ms) for the MPC problems with fatrop, acados and ipopt. For the results with an asterisk (*), function evaluation time is excluded from the total time because the CasADi virtual machine was used instead of compiled generated C-code. For these problems compilation failed due to insufficient available memory on the test machine. fatrop and acados were always faster than ipopt, solving all problems in a few milliseconds. The acados algorithm always converged in fewer iterations than fatrop, which explains why its function evaluation time was always lower than fatrop. The SQP algorithm of acados solves a QP at every (outer) iteration which is computationally more expensive than solving the primal-dual system in a fatrop iteration. This explains why fatrop was faster for the cart pendulum and quadrotor MPC problems, despite the higher number of iterations.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

acados's inner QP solver hpipm benefits from partial condensing [frison2016pcond], as the condensed quantities only have to be computed for every outer iteration. Partial condensing is most beneficial for problems with a large number of states compared to the number of controls ($n_x \gg n_u$). This, together with the lower number of function evaluations, explains why acados is faster than fatropfor the hanging chain problems.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion", "weight": 1.5} -->

fatrop is a novel trajectory optimization framework that is heavily inspired by the ipopt algorithm, but achieves a speed-up by exploiting the optimal control structure at hand. We demonstrated its versatility, numerical robustness and efficiency by solving a variety of benchmark problems. The fatrop software is available at under the LGPL. Future work includes direct handling of no-collision constraints, by means of a specialized feasibility restoration phase, and optimization over Lie manifolds. Additionally, at this moment the fatrop-rockit interface is limited to single stage problems. Another part of future work is the ability to transcribe multi-stage rockit problems to fatrop.
