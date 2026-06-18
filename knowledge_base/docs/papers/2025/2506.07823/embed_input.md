<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Primal-Dual iLQR for GPU-Accelerated Learning and Control in Legged Robots

Topics include Graphics processing unit acceleration, Model predictive control, Legged robots, Primal-dual optimization, Trajectory optimization, Parallel computing, iLQR.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Implements Primal-Dual iLQR on GPU using parallel associative scans, reducing complexity from O(N(n+m)³) to O(log²(n)log(N)) per solve. Achieves up to 700% runtime improvement over acados and Crocoddyl for legged robot MPC, enabling centralized control of 16 robots and direct GPU-based learning-in-the-loop.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper introduces a novel Model Predictive Control (MPC) implementation for legged robot locomotion that leverages GPU parallelization. Our approach enables both temporal and state-space parallelization by incorporating a parallel associative scan to solve the primal-dual Karush-Kuhn-Tucker (KKT) system. In this way, the optimal control problem is solved in O(log²(n)log(N) + log²(m)) complexity, instead of O(N(n + m)³), where n, m, and N are the dimension of the system state, control vector, and the length of the prediction horizon. We demonstrate the advantages of this implementation over two state-of-the-art solvers (acados and crocoddyl), achieving up to a 60% improvement in runtime for Whole Body Dynamics (WB)-MPC and a 700% improvement for Single Rigid Body Dynamics (SRBD)-MPC when varying the prediction horizon length. The presented formulation scales efficiently with the problem state dimensions as well, enabling the definition of a centralized controller for up to 16 legged robots that can be computed in less than 25 ms.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Furthermore, thanks to the JAX implementation, the solver supports large-scale parallelization across multiple environments, allowing the possibility of performing learning with the MPC in the loop directly in GPU.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Among the many well-known control approaches available, Model Predictive Control (MPC) has proven to be highly effective in generating and controlling complex dynamic behaviors in robotic systems, especially legged robots, as shown by \[Mpc\] and \[Perceptive_based_MPC\]. At the core of an MPC is the transcription of a task we want the robot to perform into an Optimal Control Problem (OCP) and the ability to solve it fast enough to be used in a closed-loop controller.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the most widely used methods in robotics for solving such OCP is Differential Dynamic Programming (DDP), which gained renewed attention through the work of Todorov et al.\[ilqr\], who introduced a variant known as Iterative Linear Quadratic Regulator (iLQR). iLQR discards the second-order terms of the dynamics in the Hessian, sacrificing the local quadratic convergence of DDP in favor of faster update rates. However, a key limitation of this method is its single-shooting nature, which requires a feasible initial guess as a starting point and often exhibits critical numerical issues. \[GNSM\] overcame such limitation presenting a multiple shooting variant of the iLQR algorithm. More recently, \[crocoddyl\] proposed a feasibility-driven multiple shooting approach to DDP with notable results also on real hardware \[talosWholeBody\].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another common approach to the solution of the OCP is Sequential quadratic Programming (SQP). Compared to DDP-like algorithms, SQP has been more extensively developed for general-purpose solvers due to its flexibility in handling a broader range of constraints and objectives, as well as its robustness in dealing with infeasible iterations. Solvers like OCS2 \[ocs2\] and acados \[acados\] also showed relevant results on real hardware as demonstrated in \[tamols\] and \[mpc_acados\], thanks to the tailoring of the solver to the structure of OCP. Recent work like \[sqp_lqr\] highlights the connection between SQP and DDP, describing how the sparsity structure of the OCP can be exploited not only in DDP-like solvers but also in other solver types, such as SQP or interior point-based solvers.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

While the above methods have been shown to exploit the structure of the OCP, they have struggled to exploit new hardware accelerators like GPUs. Compared to CPUs, graphics cards can massively parallelize computation and are specifically designed for high-throughput linear algebra operations. Jeon et al. \[cusadi\] tried to bridge the gap by developing Cusadi, a tool to convert expressions written in the well-known framework CasADI \[casadi\] to GPU. Cusadi only translates closed-form expressions into GPU-compatible code, lacking the branching and looping capabilities necessary for most solvers. Bishop et al., \[reluQP\] introduced a GPU accelerated Quadratic Programming (QP) solver, Relu-QP, leveraging the Alternating Direction Method of Multipliers (ADMM) algorithm, achieving performance superior to state-of-the-art CPU-based solutions. However, its applicability to Nonlinear Programming (NLP) is constrained by the need to pre-compute part of the algorithm offline.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Lee et al. \[gpu_lqr_limited_parallelization\] implements an iLQR controller on GPU but only partially leverages its capabilities, limiting parallelization to the line search and gradient computation. In contrast, \[gpu_lqr_batched\] focuses only on batching, solving multiple OCP s in parallel without exploiting state or temporal parallelism. \[gpu_ddp\] extends the approach of \[gpu_lqr_limited_parallelization\] by incorporating the temporal parallelization strategy introduced in \[Mpc\]. However, \[Mpc\] requires introducing approximations in the backward pass and performing a consensus sweep to maintain consistency. Frasch et al. \[moritz_parallel\], proposed a method to iteratively solve linear quadratic control exploiting parallel computation, while Wright et al. \[partitioned_dynamics\] showed how to partition dynamic programming for parallel computation. However, none of the mentioned methods achieved at the same time logarithmic time complexity and an exact formulation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, Särkkä et al. \[TemporalParallelizationLQR\] showed how parallel associative scan operations can be utilized to improve the computational complexity of LQR. When parallelized on a GPU, associative scans can compute the optimal control policy in $\mathcal{O}{({{{\log^{2}{(n)}}{\log N}} + {\log^{2}{(m)}}})}$ instead of the $\mathcal{O}{({N{({n + m})}^{3}})}$ of the classical Riccati Recursion, where $n$ and $m$ are the dimensions of the system state and control input, and $N$ is the prediction horizon length.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we designed an SQP method that uses an associative scan-based LQR solver to solve the primal-dual Karush-Kuhn-Tucker (KKT) system efficiently. The solver avoids the offline precalculation necessary for Relu-QP \[reluQP\]. Our method benefits from a multiple shooting implementation, instead of the single shooting approach presented in \[gpu_ddp\]. Our algorithm fully exploits the parallelization capabilities of GPUs in the temporal, state, and control dimensions, while maintaining, in contrast to \[gpu_ddp\], an exact backward pass. We tailored the formulation for the deployment as a receding horizon controller for legged robot locomotion and analyzed its impact on learning and control.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Control: At first, the reduction in the computational complexity of the solver may appear to have limited significance in a practical application. Some of the already described methods, like OCS2 \[ocs2\] and crocoddyl \[crocoddyl\], have been successfully used for whole-body MPC even for experiments, as shown in \[inverse_dynamics_mpc\] and \[Perceptive_based_MPC\]. To ensure that such an MPC formulation can run online on real hardware, the prediction horizon length and the number of robots that can be controlled simultaneously are constrained by the time complexity of the underlying algorithm. In particular, for solvers like OCS2, acados, and crocoddyl, the complexity scales linearly with the horizon length and cubically with the state dimension. In contrast, our approach scales with the square-log of the horizon length and logarithmically with the state and control dimensions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

This improved scaling enables the use of more nodes at the same update rate, allowing for finer integration steps for a better approximation of the robot dynamic or, more critically, the inclusion of a Moving Horizon Estimator (MHE), such as those presented by \[Invariant_moother\] or \[inertial_estimationlocalization\], within the same optimization loop, opening the pace for "end-to-end" MPC s capable of adapting and reacting to system changes directly using the sensor data. The reduction in complexity with respect to the state dimension enables better scalability across different robot morphologies. While other methods, such as the one presented by \[AcceleratingMPC\], use an approximate approach in the form of consensus ADMM to parallelize over the system state, our implementation leverages the inherent parallelism of matrix operations provided by the GPU. State space scaling becomes crucial when a centralized controller for collaborative tasks is considered. As demonstrated by \[CentralizedMPC\] and \[LayeredMPC\], centralized controllers can handle complex tasks involving multiple collaborating agents.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, while these approaches achieve notable performances, the complexity of the task and the number of agents involved are constrained by their capability to solve the increasingly large OCP s at a reasonable control frequency. Our framework overcomes such barriers, as shown in Sec. IV-C.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning: In recent years, Reinforcement Learning (RL) has demonstrated remarkable performance, enhancing the robustness and capabilities of legged robots. RL controllers have surpassed model-based controllers in robustness against model mismatches and sensor noise. Cheng et al. \[parkour\] also demonstrated agile movements involving jumps on unstructured terrains with a real robot. However, RL policies have shown limitations in scenarios that involve crossing gaps and stepping stones, since the learning process efficiency is significantly affected due to the sparse reward signals typical of such tasks. Giftthaler et al. \[DTC\] proposed a solution to bridge the gap between learning-based and model-based controllers by incorporating MPC as a bias for the RL-policy. In contrast, works such as \[safesteps\] and \[learning2closethegap\] integrated learned behaviors directly into the optimization process. Despite the noticeable results, all of the aforementioned methods that mix model-based controllers and RL suffered from a slower training process due to the dependency on CPU-based solvers.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, our implementation is entirely developed in JAX \[jaxgithub\], and it can be coupled with GPU-based simulators such as IsaacLab \[orbit\] or Mujoco XLA \[mujoco\] to achieve a significant speed-up in simulation throughput.

<!-- chunk {"id": "body-0017", "role": "body", "section": "I-A Contribution", "weight": 1.0} -->

a novel GPU-accelerated MPC for legged robots that achieves logarithmic scaling in computation complexity on the horizon length, squared-logarithmic scaling in the state and control dimensions, and can easily be parallelized for use with data-driven approaches;

<!-- chunk {"id": "body-0018", "role": "body", "section": "I-A Contribution", "weight": 1.0} -->

a detailed analysis of the performance benefits and limitations of the proposed algorithm with respect to state-of-the-art solvers;

<!-- chunk {"id": "body-0019", "role": "body", "section": "I-A Contribution", "weight": 1.0} -->

an open-source code repository for the rapid prototyping of MPC for legged robots and loco-manipulation, written in JAX; the code provides tools for controlling legged robots and also supports large-scale parallelization.

<!-- chunk {"id": "body-0020", "role": "body", "section": "I-B Outline", "weight": 1.0} -->

This paper is organized as follows. Sec. II describes the details of the proposed solver. Sec. III presents the dynamical models used in our formulation. Sec. IV shows the benefits of our approach on comparative simulations against state-of-the-art solutions. Finally, Sec. V draws the final conclusions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A Optimal Control Problem", "weight": 1.0} -->

We start describing the OCP at the base of the MPC formulation we are presenting. In a OCP, we transcribe not only the task we want to be performed but also the physical limits the system needs to respect.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A Optimal Control Problem", "weight": 1.0} -->

where ${\mathbf{x}}_{i}$ is the system state and ${\mathbf{u}}_{i}$ is the control input. ${\mathbf{l}}{({\mathbf{x}}_{\mathbf{i}},{\mathbf{u}}_{\mathbf{i}})}$ is the stage cost made of a quadratic tracking and regularization terms, while ${\mathbf{l}}{({\mathbf{x}}_{\mathbf{N}})}$ is the terminal cost, and $h{({\mathbf{x}}_{i},{\mathbf{u}}_{i})}$ is the system dynamics. Finally, $\text{X}_{i}$ and $\text{U}_{i}$ are, respectively, the set of feasible system states and control inputs. The remainder of this section will describe the methods we use to solve the optimization problem posed by the OCP formulation presented.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A Optimal Control Problem", "weight": 1.0} -->

By leveraging both the knowledge of the problem structure and exploiting modern hardware accelerators, we are able to obtain logarithmic time complexity in horizon length $N$ as well as square-log for the state $x$ and input $u$ dimensions. For simplicity, in this section, we avoid treating the inequality constraint in (1d) and (1c). These details will be treated separately in Sec. II-F. We now focus on the solution of the equality-constrained optimization problem, which only presents the initial condition (1e) and dynamics (1b) as constraints. In particular, we are going to derive a multiple-shooting approach, which, in contrast to the single-shooting one, keeps both the state and control as optimization variables. We first derive an efficient SQP algorithm that exploits the Riccati recursion to solve the equality constrained QP Sec. II-C, and then we focus on the temporal parallelization of the solver through the use of parallel associative scan, Sec. II-D.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Sequential Quadratic Programming", "weight": 1.0} -->

We start by defining the Lagrangian of problem in as

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B Sequential Quadratic Programming", "weight": 1.0} -->

where ${\mathbf{λ}}_{i}$ for $i = {{1\ldotsN} + 1}$ are the Lagrangian multipliers associated with the dynamics constraints (also known as costates). In an SQP method, we iteratively solve the QP derived from the quadratic approximation of the Lagrangian and the linearization of the constraints at the current guess, ${\mathbf{x}}^{k}$, ${\mathbf{u}}^{k}$, where $k$ represents the last iterate. The QP is then written as

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B Sequential Quadratic Programming", "weight": 1.0} -->

The linear terms in the objective function are defined as

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B Sequential Quadratic Programming", "weight": 1.0} -->

Finally, the Quadratic terms are defined as

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-C Primal & dual problem solution", "weight": 1.0} -->

As shown by \[fastGeneration\], such QPs can be efficiently solved by exploiting the problem structure. By applying the Riccati Recursion, starting from the last (i.e.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-C Primal & dual problem solution", "weight": 1.0} -->

where ${\mathbf{K}}_{i}$ and ${\mathbf{k}}_{i}$ are, respectively, the feedback and feed-forward term of the optimal control policy.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-D Parallel Associative Scan", "weight": 1.0} -->

In this section, we will briefly recap how parallel associative scans can be used to solve the primal problem as shown for the first time by \[TemporalParallelizationLQR\].

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-D Parallel Associative Scan", "weight": 1.0} -->

in $\mathcal{O}{({\log N})}$ as shown by \[scan\]. This is possible since $\otimes$ is an associative operation, allowing the computation to be reorganized into smaller interdependent subproblems. To make use of this property, we first define the Conditional Value Function (CVF) $V_{i\rightarrow j}{({\mathbf{x}}_{i},{\mathbf{x}}_{j})}$ as the minimal cost related to the optimal trajectory that goes from state ${\mathbf{x}}_{i}$ at node $i$ in the horizon to state ${\mathbf{x}}_{j}$ at node $j$, with $i < j$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-D Parallel Associative Scan", "weight": 1.0} -->

where ${\mathbf{x}}_{k}$ is a third intermediate state between $i$ and $j$. Note that this operator is associative since the $\min$ operator is associative. We can now perform an associative scan on the CVF to obtain $V_{i\rightarrow{N + 1}}$ in a single pass, thus $V_{i}{({\mathbf{x}}_{i})}$ for all $i$ in the horizon.

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-D Parallel Associative Scan", "weight": 1.0} -->

where the tilde $\overset{\sim}{\cdot}$ is used to distinguish the values related to the conditional value function from the one, while the subscripts are used to specify the initial and final state considered. It can be proved that, given $V_{i\rightarrow k}$ and $V_{k\rightarrow j}$ in the form of, $V_{i\rightarrow j}$ will still have the form of and is characterized by the combination rule

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-D Parallel Associative Scan", "weight": 1.0} -->

We now initialize the values $a_{i}$ of a reverse associative scan, using the conditional value function $V_{i\rightarrow{i + 1}}$ characterized by

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-D Parallel Associative Scan", "weight": 1.0} -->

From the solution of the parallel associative scan using the combination rule, we obtain $V_{i\rightarrow{N + 1}}{({\mathbf{x}}_{i},{\mathbf{x}}_{N + 1})}$ for $i = {0,\ldots,{N + 1}}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "II-D Parallel Associative Scan", "weight": 1.0} -->

This means that we obtained all ${\mathbf{P}}_{i}$ and ${\mathbf{p}}_{i}$ for $i = {0,\ldots,{N + 1}}$ that can then be used in (II-C) to calculate $\mathbf{K}$ and $\mathbf{k}$ in on pass in parallel. Thanks to a GPU-accelerated scan implementation, we can obtain the control policy over the entire horizon with an overall computational complexity of $\mathcal{O}{({{{\log^{2}{(n)}}{\log N}} + {\log^{2}{(m)}}})}$. This follows from the fact that both computing and initializing the scan involve a matrix inversion, which can be performed in parallel with complexity $\mathcal{O}{({\log^{2}{(n)}})}$ \[parallel_matrix_inv\].

<!-- chunk {"id": "body-0037", "role": "body", "section": "II-D Parallel Associative Scan", "weight": 1.0} -->

The parallel associative scan can also be used to retrieve the optimal trajectory in $\mathcal{O}{({{\log{n{\log N}}} + {\log m}})}$. We start by plugging into the linearized dynamics the optimal control law we evaluated, obtaining

<!-- chunk {"id": "body-0038", "role": "body", "section": "II-D Parallel Associative Scan", "weight": 1.0} -->

\[TemporalParallelizationLQR\] showed that from the combination of two conditional optimal trajectory ${\mathbf{h}}_{i\rightarrow k}$ and ${\mathbf{h}}_{k\rightarrow j}$ we obtain ${\mathbf{h}}_{i\rightarrow j}$ that can be written in the same form as with

<!-- chunk {"id": "body-0039", "role": "body", "section": "II-E Parallel Line Search", "weight": 1.0} -->

Once we update the optimal directions ${\mathbf{δ}}{\mathbf{x}}$, ${\mathbf{δ}}{\mathbf{u}}$, and ${\mathbf{δ}}{\mathbf{λ}}$, we can perform a backtracking line search to calculate the step length $\alpha$ to finally get the new guess as

<!-- chunk {"id": "body-0040", "role": "body", "section": "II-E Parallel Line Search", "weight": 1.0} -->

The SQP linear rollout allows for the computation to be easily performed in parallel for the horizon. To evaluate $\alpha$, we implemented a filter line search similar to the one implemented in \[ipopt\]. The filter line search ensures that the step taken in the iteration reduces the constraint violation or the cost. Such a method has already been successfully deployed for legged robot control in \[Perceptive_based_MPC\]. We measure the satisfaction of the dynamics constraints as

<!-- chunk {"id": "body-0041", "role": "body", "section": "II-E Parallel Line Search", "weight": 1.0} -->

As for \[Perceptive_based_MPC\], when the constraint violation $\theta$ is higher than a threshold, we reject the step if it further increases $\theta$. If the violation is below the threshold and the current step is a descent direction, then we apply an Armijo condition \[armijo\]. On the other hand, if the current iterate is not in a descent direction, we require that at least the cost or $\theta$ is decreased to accept the step. To leverage GPU parallelism, we evaluate the line-search in parallel (at a fixed grid of ten step sizes, i.e. $\alpha \in {\{ 2^{0},\ldots,2^{- 9}\}}$) and select the largest $\alpha$ that satisfies one of the line-search conditions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "II-F Practical Implementation", "weight": 1.0} -->

As it is commonly done in practice, we also perform a Gauss-Newton approximation, ignoring the second-order term of the dynamics in (II-B). We can further consider that in our case, the cost for the MPC can be expressed as a non-linear least squares problem in the form $\frac{1}{2}{\sum_{i = 0}^{N}{\|{\epsilon{(x,u)}}\|}_{W}}$, where $W$ is a weight matrix.

<!-- chunk {"id": "body-0043", "role": "body", "section": "II-F Practical Implementation", "weight": 1.0} -->

Such an approximation also guarantees that II-B is convex. As described in Sec., the inequality constraints in (1c) and (1d) were not explicitly included in the solver formulation. However, these constraints are critical for MPC as they represent the physical limitations of the system, such as friction cones or joint limits.

<!-- chunk {"id": "body-0044", "role": "body", "section": "II-F Practical Implementation", "weight": 1.0} -->

where ${\xi{({\mathbf{x}},{\mathbf{u}})}} < 0$ is the considered constraint, and $\mu$ and $\delta$ are parameters tuned for each constraint. Following the example of \[Perceptive_based_MPC\], to maintain the convexity of II-B the Hessian approximation of the constraints is constructed as

<!-- chunk {"id": "body-0045", "role": "body", "section": "II-F Practical Implementation", "weight": 1.0} -->

As a common practice, while using the MPC in closed-loop with the robot, we perform one iteration only of the algorithm described in Sec. per control loop. To increase the robustness of the method, we warm-start each call of the solver with the previous prediction just shifted by one time-step as shown by \[rti\].

<!-- chunk {"id": "body-0046", "role": "body", "section": "II-F Practical Implementation", "weight": 1.0} -->

Finally, to guarantee the differentiability of the solver through JAX-based automatic differentiation, we avoided the use of $while$ loop in the code. Especially in line-search, we evaluate a fixed number of alpha values in parallel.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Model Predictive Control", "weight": 1.0} -->

In this section, we describe briefly the dynamics model ${\mathbf{h}}{({\mathbf{x}}_{i},{\mathbf{u}}_{i})}$ presented in (1b), introducing two different models used for the formulation of the OCP presented in the result Sec. IV. The efficacy of the control input obtained from a MPC strategy is directly related to the rate at which such a control strategy can be re-planned and to the accuracy of its predictions, as shown by \[solution_accuracy\]. Therefore, we consider two main formulations from the literature: one based on the Single Rigid Body Dynamics (SRBD) model and one based on the Whole Body (WB) model. The first approximates the system as a single body with constant inertia, discarding the limb joint positions and the inertial variation from different limb configurations. This model is particularly effective in quadruped robots, where the limb mass is, in most cases, designed to be less than 10% of the total mass \[cheeta_design\].

<!-- chunk {"id": "body-0048", "role": "body", "section": "Model Predictive Control", "weight": 1.0} -->

On the other hand, the latter completely captures the dynamics of the robot, enabling the maximum exploitation of the system's capabilities. This benefit comes at the cost of handling a larger state space and highly non-convex models, thus affecting the maximum frequency at which the optimization problem can be solved. Moreover, the SRBD-MPC state is limited to the center of mass linear and angular positions and velocities. This means that, when representing the robot's orientation using quaternions, the state lies in ${\mathbb{R}}^{7}$. For such model, the control input consists only of the Ground Reaction Forces (GRF), and thus lies in ${\mathbb{R}}^{3n_{c}}$, where $n_{c}$ is the number of contact points, meaning that, for the evaluations with the quadruped, in Sec. IV $n$ is in ${\mathbb{R}}^{13}$ and $m$ in ${\mathbb{R}}^{12}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Model Predictive Control", "weight": 1.0} -->

In contrast, the WB-MPC also includes joint positions and velocities in the state, and joint torques in the control input. This increases the state dimensionality to ${\mathbb{R}}^{13 + {2n_{\text{joint}}}}$ and the control input dimensionality to ${\mathbb{R}}^{{3n_{c}} + n_{\text{joint}}}$, that translate for the quadruped model in Sec. IV in $n$ in ${\mathbb{R}}^{37}$ and $m$ in ${\mathbb{R}}^{24}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Model Predictive Control", "weight": 1.0} -->

Beyond the difference in dimensionality, the WB model also introduces greater complexity. While the SRBD model features bilinear terms only in the angular dynamics, the WB model has highly nonlinear dependencies on the joint configuration. As a result, the overall OCP becomes significantly harder to solve.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Results", "weight": 1.0} -->

In this section, we present the results of various analyses that highlight the strength of the proposed approach. We evaluate the performance of our algorithm using the two models introduced in Sec. III (the SRBD and WB models). To benchmark our implementation against state-of-the-art solvers, we used acados \[acados\] (SQP) for comparisons on the SRBD model and crocoddyl \[crocoddyl\] (DDP) for the WB model. We used acados for the SRBD comparison, as it could be easily adapted for the evaluations with multiple robots, shown in Fig. and. On the other hand, we used crocoddyl for the horizon length comparison with the WB model, as it showed significantly better performance than acados with the more complex model as shown in Fig..

<!-- chunk {"id": "body-0052", "role": "body", "section": "Results", "weight": 1.0} -->

Our analysis includes investigating how the average solving time scales with the horizon length across all models and solvers. Additionally, we assess the solver's performance as the system state dimension increases, as well as the vectorization capabilities of our approach. All the solving time comparisons consider a single iteration for each algorithm. The tests were conducted on a desktop computer equipped with an Intel Core i7-13700KF and an NVIDIA RTX 3080. We used Mujoco XLA, to evaluate the WB dynamics. In all the presented benchmarks, if not stated differently, we used the 15 kg Unitree Go2 robot, a torque-controlled quadruped platform, with a horizon length N of 50 nodes. As Fig. and the accompanying video show, our WB-MPC can also be implemented for real-time control of other robot morphologies, like humanoids.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-A Performance evaluation", "weight": 1.0} -->

First, we evaluate the ability of our solver to generate complex dynamic maneuvers. In this scenario, we are generating a barrel roll motion with the Aliengo robot, as shown in Fig.. Thanks to its multiple shooting formulation, we can initialize the solver with an infeasible initial guess, and the solver converges in just $27$ iterations to a solution that completes the task. We also assess the performance of the proposed solver in terms of solution optimality. In Fig., we compared the values of the cost from the optimal solution given by our implementation against the one given by acados, which is chosen for this comparison because it allows using the same cost function as the one in our formulation. In this scenario, we are using the whole-body model and are controlling the robot in simulation at 50Hz. The robot is tasked to trot with a forward speed of $0.3$ m/s while being randomly pushed by an external disturbance of $50$N for $0.25$s. At every control loop, we record the value of the cost functional from both solvers, comparing solutions that start from the same initial condition.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-A Performance evaluation", "weight": 1.0} -->

Figure reports the values recorded during a $2.5$s time span. Although the two solutions are comparably similar, our implementation results in a $20\%$ reduction in the average cost along the trajectory.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-A Performance evaluation", "weight": 1.0} -->

To finally validate the MPC, we also performed experiments on the real hardware, as shown in Fig. and in the accompanying video. For the real experiments, the solver runs on an Nvidia RTX 4050 laptop GPU. Figure shows snapshots of the robot walking blindly up the steps and through uneven terrain using only proprioceptive data for state estimation \[muse\]. We also evaluated the proposed approach when used to control two different robots at the same time in a centralized control implementation in simulation. In this example, the two robots are controlled by the same MPC that evaluates the control input for both systems at $50$Hz. The MPC also includes a collision avoidance constraint, in the form of a quadratic penalty term. In the tested scenario, the two robots are tasked to track two perpendicular trajectories that cross each other and would lead to a collision. Figure shows the resulting path of the two robots, where the dashed grey lines represent the distance between the two robots. As shown, both robots deviate from their desired paths to avoid collisions, demonstrating coordinated behavior. While being just a simple example, this result highlights the potential of our MPC in solving collaborative tasks.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-A Performance evaluation", "weight": 1.0} -->

Further implementation in more complex scenarios, such as collaborative carrying, is left for future work. Figure presents the average solving time breakdown for the three solvers in the quadruped trotting scenario with a horizon of N=100. It highlights the sequential backward pass in crocoddyl, the QP solver call in acados, and the parallel scan in our method for evaluating the search direction. A minor computational overhead of approximately $1ms$ arises from GPU communication, as only the initial state is sent and the commanded torques, joint positions, and velocities are retrieved.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-B Temporal Parallelization", "weight": 1.0} -->

In this subsection, we show the benefit of our implementation against the state-of-the-art solvers acados \[acados\] and crocoddyl \[crocoddyl\], in terms of average solving time for increasing horizon length. For this assessment, we initialized the robot in a feasible random pose and joint configuration and tasked the controller to perform a forward trot at a speed of $0.5$m/s. Acados uses the same cost and dynamics formulation as in our controller, while for the comparison with crocoddyl we adapted our reference generator and cost to match the reference used in the example provided with crocoddyl's libraries. As reported in Fig., our implementation shows faster update rates than both solvers in almost all tested scenarios. For the assesment against acados, with the SRBD model, our implementation is always faster. For the case of the WB formulation, crocoddyl is able to outperform our formulation with a prediction horizon smaller than $80$ nodes. This last outcome is primarily attributed to overhead involved in transferring data to and from the GPU, which, for smaller problems, can be detrimental.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-B Temporal Parallelization", "weight": 1.0} -->

Noticeably, our formulation can achieve an update rate of 50Hz for a horizon length of 200 nodes.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-C State Parallelization", "weight": 1.0} -->

In this subsection, we discuss the benefits of our implementation in the context of centralized controllers. In our tests, we evaluated the average solving times for the MPC while progressively increasing the number of robots included in the same optimization. This approach simulated a centralized controller managing $n$ different robots. For the SRBD model, we compared our implementation against acados. For the WB model comparison, crocoddyl was excluded since its model interface does not allow for a customization that is needed for a fair evaluation. As Fig. shows, our implementation outperformed acados when considering the SRBD model, achieving a computational time of 25 ms in the presence of 16 robots, enough for the real-time control of the systems. When using the WB model, instead, computation becomes significantly more demanding for the implementation with acados and we could not record data for the comparison. As shown in Fig., our algorithm successfully controls up to four robots (WB model case) at 20 Hz. To the best of the authors' knowledge, this level of performance has never been achieved before.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-D Model-Based Learning", "weight": 1.0} -->

In this subsection, we highlight the vectorization capabilities of our controller. Thanks to its full implementation in JAX, we can easily vectorize the computation of the MPC. Such ability is critical in the training scenario as shown in \[DTC\] or at runtime as shown in \[mcts\]. In Fig., we compare our approach to the batched version of acados, which uses OpenMP to parallelize the computation of independent MPC instances on the CPU. As the plot shows, acados is competitive with the proposed MPC only for small batch sizes. This limitation comes from the reduced number of cores available on a CPU compared to the parallelization capabilities of modern GPUs.

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-D Model-Based Learning", "weight": 1.0} -->

Finally, Table I summarizes the performance of our MPC when batched across multiple environments with Mujoco XLA as the simulator. In this setup, we generate 4096 environments, each one running its own MPC. For the SRBD model, we control the robot at an update rate of 50 Hz and we achieve a value of 570 seconds of simulated time per second. Meanwhile, for the WB model, closing the loop at 25 Hz, we achieve a real-time factor of 75x.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This work presents a novel GPU-accelerated MPC framework implemented for legged robot locomotion. By leveraging the parallel processing capabilities of GPUs and implementing a Primal-Dual iLQR solver in JAX, we achieve logarithmic scaling in horizon length and square-log scaling with state and control dimensions. Our approach demonstrates significant improvements over state-of-the-art solvers, achieving higher computational efficiency and scalability. This allows for the optimization of centralized controllers for multiple robots and the integration of large-scale parallel environments, enhancing learning-based control frameworks. Future works will include the exploitation of the presented MPC as a bias in the learning process of a locomotion policy. Furthermore, we would like to include a more sophisticated methodology for dealing with inequality constraints.
