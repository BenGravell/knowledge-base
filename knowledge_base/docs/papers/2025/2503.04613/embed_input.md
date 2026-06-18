<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Whole-Body Model-Predictive Control of Legged Robots with MuJoCo

Topics include Predictive control, Robotics, Real-time systems, Online algorithms, Control, Model predictive control, Humanoid robot.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We demonstrate the surprising real-world effectiveness of a very simple approach to whole-body model-predictive control (MPC) of quadruped and humanoid robots: the iterative LQR (iLQR) algorithm with MuJoCo dynamics and finite-difference approximated derivatives. Building upon the previous success of model-based behavior synthesis and control of locomotion and manipulation tasks with MuJoCo in simulation, we show that these policies can easily generalize to the real world with few sim-to-real considerations. Our baseline method achieves real-time whole-body MPC on a variety of hardware experiments, including dynamic quadruped locomotion, quadruped walking on two legs, and full-sized humanoid bipedal locomotion. We hope this easy-to-reproduce hardware baseline lowers the barrier to entry for real-world whole-body MPC research and contributes to accelerating research velocity in the community.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Enabling legged robots to achieve human and animal-level agility has been a decades-long challenge for robotics researchers. In addition to the challenges faced by other non-legged mobile robots (e.g., drones, autonomous vehicles, etc.), legged systems are generally high-dimensional and must effectively reason about making and breaking contact with the world. Advancements in model-based control and reinforcement learning (RL) methods have unlocked tremendous in-the-wild legged robot capabilities over the last $10$-$15$ years. Over the same period, robotics simulation has seen significant growth in terms of physical accuracy, differentiability, and parallelization performance. Thanks to these advances in simulation technologies combined with incredible tools supported by the broader machine learning community such as PyTorch and JAX, sim-to-real RL has enjoyed accelerated progress and become the standard approach for solving challenging problems like humanoid whole-body control.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Interestingly, in comparison, model-based control researchers have generally favored novel, custom implementations of robot models and optimization solvers, in part due to the online computation requirements of model-predictive control (MPC) paradigm, making these works relatively more difficult to reproduce which, so far, has resulted in slower community adoption.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper aims to reduce this gap by providing an open-sourced baseline MPC algorithm and real-world legged robot implementation built on the MuJoCo physics engine, a standard, easy-to-use open-source robotics simulator. We show that a standard gradient-based MPC algorithm, in particular the iterative LQR (iLQR) algorithm, based on MuJoCo is surprisingly capable of solving a variety of challenging *real-world* tasks such as bipedal locomotion on a quadruped and full-sized humanoid robot in *real time*. By leveraging the efficient C implementation of MuJoCo as the backend for the forward model and derivative computations, our real-time MPC approach reasons about both whole-body dynamics and collision detection in the model, something difficult to achieve in previous open-source whole-body MPC algorithms. Additionally, we design an interactive GUI system that enables users to quickly modify key MPC parameters and observe *real-world* robot behaviors alongside a simulated twin. We hope that this effort lowers the barrier to entry for further model-based control research on legged robot hardware and eventually leads to accelerated research momentum.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A simple-yet-surprisingly-effective baseline whole-body predictive control algorithm for real-world legged robot locomotion.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

An open-source interactive GUI system for real-world predictive control of legged robots.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A set of hardware experiments demonstrating the effectiveness of the baseline algorithm on both quadruped and humanoid robots across a variety of tasks.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows: We begin by reviewing relevant literature on iLQR, whole-body MPC, and open-source efforts for model-based control in Sec. II. Next, we briefly introduce the MuJoCo contact model and iLQR in Sec. III, followed by key considerations and implementation details for transferring iLQR policies to hardware in IV. Then, we cover the hardware setup and experimental results in Sec. V. Finally, we conclude in Sec. VI by discussing current limitations of our system and directions for future work.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Iterative Linear-Quadratic Regulator", "weight": 1.0} -->

by iteratively solving the an locally approximated problem with Dynamic Programming.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Iterative Linear-Quadratic Regulator", "weight": 1.0} -->

where $\overline{u}$ and $\overline{x}$ are the current solution, $K_{t}$ is the feedback gain matrix at time index $t$, $k$ is an improvement to the current nominal control, and $\alpha$ is the line search step size. This single-shooting formulation only optimizes over the controls $u_{0:{T - 1}}$ and recovers the corresponding states $x_{0:T}$ by rollingout the discrete-time dynamics $x_{t + 1} = {f{(x_{t},u_{t})}}$. $l{(x_{t},u_{t})}$ and $l_{f}{(x_{T})}$ are the running and terminal costs, respectively. In each iteration, derivatives of cost and dynamics w.r.t to the control sequence are computed around the current solution points in a process called linearization to form a subproblem with quadratic cost and linear constraints.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Iterative Linear-Quadratic Regulator", "weight": 1.0} -->

The term iterative LQR, or iLQR, generally refers to the Gauss-Newton approximations of the original DDP algorithm that is often more computationally efficient. The iLQR algorithm can also be modified to handle control limits, state constraints, and contact.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Iterative Linear-Quadratic Regulator", "weight": 1.0} -->

As a single-shooting algorithm, iLQR maintains dynamically feasible state trajectories without convergence requirements, is amenable to warm starting, and naturally handles unstable systems, since the rollouts are performed with a feedback policy, all of these features make it appealing as an online controller. However, this method generally assumes the dynamics are smooth and differentiable. For robots with contact, the dynamics are non-smooth and the derivatives become nontrivial to compute. Our empirical results show that the combination of the MuJoCo soft contact model and its finite difference derivative approximation is sufficient for iLQR and, somewhat surprisingly, transfers well to robot hardware despite obvious model mismatch.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Whole-body MPC for Legged Robots", "weight": 1.0} -->

Whole-body nonlinear MPC presents challenges to legged robots primarily because of the real-time requirements of reasoning over possible contact modes and computation of the high-degree-of-freedom dynamics and its derivatives. Traditionally, real-time MPC has been achieved by simplifying models and heuristically choosing the contact modes. Older works at whole-body MPC have been deployed on humanoid robots, they generally fall short of the real-time requirements as an online controller, limiting their real-world capabilities. Thanks to advances in computer performance and increasingly mature implementations of dynamics libraries, real-time whole-body MPC has become much more computationally trackable on quadruped and humanoid robots in recent years. Another interesting thread of research explores enabling whole-body MPC through GPU parallelization, but is so far limited to a single dynamics linearization of the model.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Whole-body MPC for Legged Robots", "weight": 1.0} -->

Still, these methods generally require custom modeling of the robot dynamics, non-trivial analytical derivatives of the discontinuous contact dynamics, and custom optimization solvers to run in real time, making these prior works difficult to reproduce and iterate upon. This paper shows that a much simpler and more straightforward approach, modeling the robot using an off-the-shelf simulator and approximating the derivatives via finite differencing, can also be very effective for quadruped and humanoid locomotion *without* specifying contact modes.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-C Open-Source Tooling for Model-Based Control", "weight": 1.0} -->

It is important to acknowledge previous open-source efforts to accelerate model-based control. In particular, MuJoCo MPC implements a variety of derivative-based and derivative-free algorithms for predictive control and shows their effectiveness in simulation. successfully demonstrates the sim-to-real transfer of sampling-based MPC using the MuJoCo dynamics on open-loop stable tasks like quadruped walking. Similar to, this work builds on with a focus on sim-to-real of the derivative-based iterative LQR (iLQR) algorithm. Unlike sampling-based MPC, we show that iLQR can successfully tackle inherently open-loop unstable tasks such as bipedal walking.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-C Open-Source Tooling for Model-Based Control", "weight": 1.0} -->

Outside the MuJoCo ecosystem, Pinocchio has become a popular toolbox in the community for efficiently computing rigid body dynamics and its derivatives. This dynamics toolbox has also enabled a variety of nonlinear trajectory optimization libraries designed for contact-rich robotics tasks like legged locomotion. For example, OCS2 offers open-source software for quadruped locomotion with fixed contact modes, while Crocoddyle and Aligator offer more versatile control for quadruped and humanoid robots. However, these works do not leverage off-the-shelf simulators widely used in the robotics community and have a steep learning curve, which limits their reach and impact. On the other hand, Drake provides advanced modeling and simulation features for accurate contact and friction dynamics for verification but is typically not fast enough for real-time control.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-C Open-Source Tooling for Model-Based Control", "weight": 1.0} -->

In comparison to prior projects (Table I), our approach bridges the current gap in tooling for model-based robotic control by enabling general controllers for both quadruped and humanoid robots using a popular, off-the-shelf, and fast robotics simulator. An additional advantage for using a mature simulator is the readily available collision detection algorithms that we can leverage during contact-rich planning and control. Additionally, we provide an interactive GUI for real-time control that enables rapid developments of robot behaviors in the real world.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Iterative LQR with MuJoCo", "weight": 1.0} -->

This section provides a brief description of the MuJoCo soft contact model, the MuJoCo MPC toolbox, the details of the MuJoCo iLQR implementation, and sim-to-real considerations.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A MuJoCo Soft Contact Model and Derivatives", "weight": 1.0} -->

The MuJoCo physics engine implements a soft contact model that is a convex approximation of the non-convex, discontinuous contact and friction models. While the interpenetration phenomena between objects (for example, the robot's foot and the floor) may be considered physically unrealistic, this convex formulation is fast, efficient, and provides a guaranteed solution, something difficult to do when solving non-convex problems. Additionally, in theory, the soft contact model offers smooth derivatives through contact. While the analytical derivatives are not yet provided, the finite different derivatives can be computed with little additional effort from the original time-stepping simulation problem.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A MuJoCo Soft Contact Model and Derivatives", "weight": 1.0} -->

To approximate the model derivatives, we use the forward difference method

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A MuJoCo Soft Contact Model and Derivatives", "weight": 1.0} -->

as it requires only one additional simulation evaluation per dimension compared to two in centered difference, where $f$ is an arbitrary function with input $x$ and $\epsilon$ is the finite different tolerance.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Derivative Computation with MuJoCo", "weight": 1.0} -->

To solve a single iteration iLQR problem from Eq. 1, we take a second-order Taylor expansion and solve the resulting subproblem via Dynamic Programming.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Derivative Computation with MuJoCo", "weight": 1.0} -->

where $r$ is a residual vector to be reduced when solving the problem, $n$ is the norm function that returns a non-negative scaler, and $w$ is non-negative scaler weight defining the importance of a residual term.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Derivative Computation with MuJoCo", "weight": 1.0} -->

where the derivatives of the norm n (i.e. $\frac{\partial\text{n}}{\partial\text{r}}$, $\frac{\partial^{2}\text{n}}{\partial\text{r}^{2}}$) are computed analytically and the Jacobians of the residual r (i.e. $\frac{\partial\text{r}}{\partial x}$, $\frac{\partial\text{r}}{\partial u}$) are computed via finite difference, Eq. 3.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Derivative Computation with MuJoCo", "weight": 1.0} -->

where dynamics Jacobians $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial u}$ are computed via finite difference, Eq. 3. Note the because residuals in Eq. 4 are implemented as MuJoCo sensors, we can efficiently compute all the Jacobians $\frac{\partial f}{\partial x}$, $\frac{\partial f}{\partial u}$, $\frac{\partial\text{r}}{\partial x}$, and $\frac{\partial\text{r}}{\partial u}$ via a *single* call to the MuJoCo finite difference utilities function.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Derivative Computation with MuJoCo", "weight": 1.0} -->

Once all derivatives are computed, we solve the resulting problem using the Riccati-recursion that produces the updated nominal controls $u$ and a time-varying linear feedback policy $K$, Eq. 2. We perform this update once before returning the current-best nominal trajectories and feedback policy without convergence checks. We then use the previous solution to warm start a new iLQR iteration with the latest state estimation, Fig. 2. Additionally, our interactive GUI allows the user to update the residual terms such as target height, goal positions, etc and adjust the weights assigned to each residual term in real-time on the robot, Fig. 3.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

This section documents several implementation details for successfully deploying real-time MuJoCo iLQR on hardware.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Contact Modeling", "weight": 1.0} -->

While the MuJoCo default contact parameters are fast and physically reasonable, they also often lead to contact slipping due to the solver's inability to enforce friction constraints. This slipping dynamics from the planner model results in jerky control trajectories (Fig. 4 top left) that are difficult to execute on the hardware. We address this issue by increasing the `impratio` value, which roughly corresponds to the solver's ability to trade off sliding versus penetration, from the default $1$ to $100$. This change also has the added effect of increasing the solve times of the simulation problem and, as a result, the iLQR iteration times. For our quadruped system, the time for a single iLQR iteration increases from $\sim 10$ ms to $\sim 20$ ms on a $12$th-gen Intel i7 CPU. We do not find the added compute time to be an issue during real-world deployment. Interestingly, the moderate ground penetration from the softness of the contact model does not cause issues in the sim-to-real transfer in our experience.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B State and Action Representation", "weight": 1.0} -->

We represent the state $x$ of the robot in the standard way, with a floating base position and attitude quaternion, followed by joint angles and corresponding linear, angular, and joint-angle velocities. We include a low-level joint-space PD controller in the dynamics model of the robot such that the inputs to the model that are optimized by iLQR are joint angle references. As a result, our approach achieves direct *whole-body control* of the robot without the model hierarchies commonly seen in traditional model-based MPC algorithms. By leveraging a fast off-the-shelf simulator, our method is simpler and more accessible than methods relying reduced-order models and hierarchical control approaches.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-C Time-Varying Linear Feedback", "weight": 1.0} -->

We compare the real-world performance of the iLQR policy with and without TV-LQR feedback on an H1 humanoid robot trotting-in-place task. The TV-LQR policy improves task performance but only *marginally* compared to directly executing the nominal open-loop control sequence on the robot, resulting in an average of $30.1\%$ improved tracking performance over an $8$ second window, Fig. 5. Note that the cost spike around $1.5$s in the red line (without feedback) in Fig. 5 indicates a temporary policy failure recovered with gantry support. The trial with feedback policy does not fail during the same window. Our empirical results are aligned with prior work which showed linear feedback on smoothed dynamics seems unsatisfactory for stabilizing contact-rich plans.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-D Dynamics Derivative Approximation", "weight": 1.0} -->

Computing the dynamics derivatives at every knot point is often the most computationally expensive step in iLQR, Fig. 4. We implement an optional heuristic by skipping dynamics derivative evaluations at some knot points along the planning horizon and instead interpolate from nearby evaluations. This heuristic is motivated by the fact that robot dynamics are approximately linear locally and, therefore, do not change much between nearby knot points. This is implemented as `skip_deriv` in the GUI, where the integer value corresponds to the number of knot points to skip before computing the next derivative. In the tasks we consider in this paper, we find the iLQR update frequency to be sufficient when paired with TV-LQR policy. However, this option can still be beneficial for enabling iLQR in real time on more articulated systems or when compute is limited.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-D Dynamics Derivative Approximation", "weight": 1.0} -->

Note that while we choose to use forward difference approximation for computation reasons, we find that the centered difference method does not work on locomotion tasks, even in simulation without real-time requirements. We hypothesize that the derivative information into the contact (this can happen when perturbing the robot state in the negative height direction) is not informative during locomotion but leave further investigation for future work.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments and Results", "weight": 1.0} -->

This section presents the interactive GUI setup on robot hardware platforms and a variety of hardware experiments. We start by demonstrating our system on basic quadrupedal locomotion on Go1 and Go2 robots in Sec. V-B. Next, we show that MuJoCo iLQR naturally extends to open-loop unstable tasks like quadruped walking on two legs in Sec. V-C. Finally, we deploy our system on a human-sized Unitree H1 humanoid robot in Sec. V-D.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A Interactive GUI for Real-World Legged Robots", "weight": 1.0} -->

We interface with the MuJoCo MPC GUI and iLQR planner via Python for robot hardware deployment. The interface takes the latest state estimation and receives the current control. The state estimation is computed by fusing Optitrack MoCap position and attitude measurements at $100$Hz via ROS and the robot joint angle position and velocity measurements at $500$Hz. The floating base linear and angular velocities in the body frame are calculated by applying a low-pass filter to finite difference values of position and attitude measurements. The planner's actions are communicated to the robot via Unitree SDK for the Go1 robot and Unitree SDK 2 for the Go2 and H1 robots. All robot controls are represented as joint targets and tracked using Unitree internal low-level PD controllers. We compute the MPC policies on a desktop equipped with a $13$th generation Intel i$9$ CPU chip with $20$ cores, a different CPU from earlier in the paper. We update the iLQR policy at $\sim 50$Hz and use the TV-LQR policy to stabilize the robots between solves at $\sim 300$ Hz.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-A Interactive GUI for Real-World Legged Robots", "weight": 1.0} -->

Unless otherwise noted, we use a default prediction horizon of $0.35$s and discretize the dynamics at $100$Hz in the iLQR planner.Note that, while we use a desktop-level CPU in our experiments, we see similar policy update frequencies from recent top-end laptop Arm-based CPUs such as the M-series chips from Apple, but leave deployment for future work.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-A Interactive GUI for Real-World Legged Robots", "weight": 1.0} -->

Since the MPC planners are implemented in C++ and update asynchronously, using the Python interface does not affect the planning frequency. While we observe a $\sim 3$ms message passing overhead from the Python API, the planner is robust to this unmodeled delay for the tasks presented in this paper.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-B Quadruped Locomotion", "weight": 1.0} -->

We first validate our system using a simple quadruped locomotion task. The task is designed for the robot to follow a reference gait and walk to the target locations. We successfully deploy the policy to the Unitree Go1 and Go2 robots with $12$ degrees of freedom (DoF) joint actuators. The GUI allows the user to move the target interactively and the real-world robot can follow the virtual target, as illustrated in Fig. 3. Note that while we keep the whole-body collision geometry in the planner model, generally only the $4$ spherical contact points are active during the locomotion tasks considered.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B Quadruped Locomotion", "weight": 1.0} -->

The residual terms for the locomotion task include tracking position and orientation while keeping balance and maintaining a desired torso height. Control efforts are penalized to minimize energy usage. We also include a nominal gait pattern in the residual, but note that this is not implemented as a constraint. As a result, the iLQR solver is free to discover new contact modes if they reduce the overall cost. More detailed descriptions of the residual terms can be found in Tab. II. Bipedal locomotion and humanoid tasks follow a similar structure.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-C Bipedal Locomotion for Quadruped Robots", "weight": 1.0} -->

Next, we show that the iLQR policies naturally handles open-loop unstable tasks, such as a quadruped walking on two legs (Fig. 1). In comparison, MPPI can tackle locomotion tasks that are stable, but fails under unstable dynamics such as during bipedal walking. In Fig. 1, we successfully enable a quadruped robot to walk gracefully on its back legs alone while using front legs to main balance and getting up to a hand stand pose from an initial quadruped configuration with the MuJoCo iLQR policy.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-C Bipedal Locomotion for Quadruped Robots", "weight": 1.0} -->

Keeps torso orientation upright (z-axis pointing up)

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-C Bipedal Locomotion for Quadruped Robots", "weight": 1.0} -->

Controls torso height relative to average foot position

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-C Bipedal Locomotion for Quadruped Robots", "weight": 1.0} -->

Tracks head position to target location (x, y, z)

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-C Bipedal Locomotion for Quadruped Robots", "weight": 1.0} -->

Controls foot lifting patterns during gait cycles (one per foot)

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-C Bipedal Locomotion for Quadruped Robots", "weight": 1.0} -->

Keeps capture point within support polygon (x, y components)

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-C Bipedal Locomotion for Quadruped Robots", "weight": 1.0} -->

Penalizes actuator forces to minimize energy consumption

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-C Bipedal Locomotion for Quadruped Robots", "weight": 1.0} -->

Keeps joints near home configuration

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-C Bipedal Locomotion for Quadruped Robots", "weight": 1.0} -->

Controls heading direction (x, y components of heading vector)

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-D Humanoid Locomotion", "weight": 1.0} -->

Finally, we deploy the iLQR policy on an H1 full-sized humanoid robot to track a periodic trotting gait, as shown in Fig. 6. Similar to the quadruped locomotion task in Fig. 3, we ask the robot to walk to a position defined as the green sphere. To achieve real-time control on a more complex system, we disable collision checking in the robot body other than two spherical contact points on each foot. Additionally, we disable the DoFs in the robot upper body equipped with only relative encoders that provide unreliable joint angle estimates since they are not critical for locomotion. While this reduces the iLQR computation time, we do not believe it to be necessary for the success of the task. Overall, the system has $10$ DoF joint actuators and $4$ contact points. We use a prediction horizon of $0.5$s.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

We present a very simple but surprisingly capable approach to whole-body MPC of quadrupeds and humanoid robots using MuJoCo. We hope that the successful hardware validation of this baseline method by leveraging a widely adopted physics engine can encourage researchers to leverage existing tooling for model-based control research. Despite the promising results, several key limitations remain for future work.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

First, reliable state estimation remains a key challenge for model-based planning and control of legged robots. For this reason, many researchers prefer the RL paradigm which easily supports learning control policies directly from a history of sensor measurements. Our current system relies on marker-based motion capture to obtain good robot position measurements. Future work should develop easy-to-use tooling for full-state estimation from the robot's onboard sensors alone to enable our robots to walk outside controlled laboratory environments. Second, the community also needs additional tooling for rigorous system identification of the robot's joint actuation and contact dynamics to overcome the significant sim-to-real gap.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

There are also several fundamental limitations of the iLQR algorithm. First, iLQR struggles with contact mode exploration. As a second-order derivative-based local planner, iLQR excels when the reference contact model schedule is provided in the task specification (cost function), which is typically the case for locomotion. However, for more contact-rich whole-body loco-manipulation tasks, derivative-free sampling-based methods have shown much more promise at discovering useful contact modes without prespecification. Furthermore, iLQR rollouts and backward passes are both fundamentally serial operations. As computers become more parallelizable given the rise of multi-core CPUs and massively parallel GPUs, research on MPC algorithms that can leverage this computation paradigm becomes increasingly important. Finally, iLQR suffers from other issues tied to its single-shooting nature, such as sensitivity to the initial guess, numerical instability, and poor convergence over longer horizons. Future work should extend the current MPC libraries to make multiple-shooting and collocation methods more accessible to the community.
