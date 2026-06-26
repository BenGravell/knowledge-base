<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

AcroMonk: A Minimalist Underactuated Brachiating Robot

Topics include Reinforcement learning, Trajectory optimization, Robotics, Robustness, Uncertainty, Optimization, Control, Learning, AcroMonk, TVLQR, Model-free proportional derivative, PD, Linear quadratic regulator.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Brachiation is a dynamic, coordinated swinging maneuver of body and arms used by monkeys and apes to move between branches. As a unique underactuated mode of locomotion, it is interesting to study from a robotics perspective since it can broaden the deployment scenarios for humanoids and animaloids. While several brachiating robots of varying complexity have been proposed in the past, this paper presents the simplest possible prototype of a brachiation robot, using only a single actuator and unactuated grippers. The novel passive gripper design allows it to snap on and release from monkey bars, while guaranteeing well defined start and end poses of the swing. The brachiation behavior is realized in three different ways, using trajectory optimization via direct collocation and stabilization by a model-based time-varying linear quadratic regulator (TVLQR) or model-free proportional derivative (PD) control, as well as by a reinforcement learning (RL) based control policy. The three control schemes are compared in terms of robustness to disturbances, mass uncertainty, and energy consumption. The system design and controllers have been open-sourced.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Due to its minimal and open design, the system can serve as a canonical underactuated platform for education and research.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Brachiation is a complex dynamic maneuver involving a continuous swing motion and a discontinuity when switching the support arm. Apes brachiate with ease through unstructured environments with flexible or rigid handholds at variable distances, making this motion challenging and interesting to study for roboticists. Brachiating robots can be beneficial for inspection, agriculture, search and rescue applications, etc., since they can perform agile movements in hard to traverse terrains. Hence, there has been extensive research on brachiation robots in the past three decades.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model Predictive Control Input/output linearization Energy based controller Table I: Overview of brachiation robots. (L, J, A, G) indicate the number of links, joints and actuators, and type of grippers respectively.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While several brachiating robots of varying complexity, along with a range of control strategies, have already been proposed, most robots include active grippers which leads to a complex system design prone to high maintenance and electro-mechanical failure points. The only system with passive grippers proposed so far is fully actuated with two motors and was not able to execute more than two continuous brachiation maneuvers. Thus, there is a lack of a robust minimalist system which allows the study of underactuated brachiation. To fill this gap, we propose AcroMonk, a novel underactuated brachiation robot with a single motor (see Figure 1). A quasi-direct drive (QDD) is chosen as the actuator with a gear ratio of 6:1 which offers low friction and high backdriveability essential for dynamic locomotion. Its unique passive grippers feature a double grooved design, which results in a large region of attraction for grasping a target bar and a well defined rotation point for swing maneuvers.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that AcroMonk is able to robustly brachiate continuously over a horizontal ladder with a wide range of controller types, using direct collocation for trajectory optimization and trajectory stabilization, either with model-based TVLQR or model-free PD control, or a RL-based policy. All three control methods are compared in terms of robustness against disturbances, modeling inaccuracies, and energy consumption. The simplicity of the robot's design, low maintenance requirements, and ease of controllability makes it a suitable platform for underactuated robotics education and research. The platform has been open-sourced\\githubLink (in the spirit of ), to encourage its use in research and education. The performance of the AcroMonk in hardware tests is shown in the accompanying video\\videoLink.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Organization", "weight": 1.0} -->

Section II outlines the mechatronics system design of the AcroMonk robot. Section III addresses behavior generation methods using trajectory optimization and RL. Section IV details the behavior controllers for the robot and Section V the controller comparison results in hardware experiments. Finally, Section VI concludes the paper and addresses future research directions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Mechatronics System Design", "weight": 1.0} -->

The motivation of the mechatronic system design of the AcroMonk was to achieve a minimalist system to study dynamic brachiation. Additionally, we aimed for a compact design which fits in a backpack and can be operated as a self-sustained system for classroom teaching.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Mechanical Design", "weight": 1.0} -->

The mechanical design choices were guided by using readily available hardware for ease of reproducibility and achieving a structure that is robust to falls and easy to repair. These goals led to a modular design with one central motor connecting two arms that can be 3D printed with readily available materials (BASF Ultrafuse PLA). Overall, the structure consists of six unique 3D-printed parts highlighted with different colors in Figure 2, connected by screw-nut fasteners for easy assembly, with compartments for electronics, a battery, counterweights, and cable guides. Computing and electrical equipment are mounted on opposite arms to ensure an even mass-inertia distribution between the arms. For continuous brachiation, special deliberation was given to the gripper design. The gripper should provide sufficient error tolerance for grasping during the brachiating maneuvers while providing a defined rotation point for the next swing once connected to the bar.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Mechanical Design", "weight": 1.0} -->

This was realized by a relatively wide opening angle of the hook, an incline towards a groove where the hook comes to rest, and an off-center connection to the arm. As illustrated in Figure 4, the intentional misalignment of the gripper's stable point aids in sliding towards the groove. The slope of the inclined surface is chosen through empirical observations as 20 degrees for angle of attack with overall radius of 35 mm. These values depend on the friction coefficient of the material pairing of the gripper surface (PLA) and monkey bars (wood) and normal force. A higher friction coefficient implies a steeper angle to ensure slipping into the groove with minimal wobbling. Consequently, within the expected deviations from an ideal movement, the hook comes to rest in the groove, providing a defined rotation point for next brachiation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Electrical and Processing Architecture", "weight": 1.0} -->

For the actuator, the mjbots qdd100 Quasi-Direct Drive with a gear ratio of 6:1, a maximum speed of 40 rad/s, maximum continuous torque of 6 Nm, and a peak torque of 16 Nm was used. A Raspberry Pi 4 mounted in the computing compartment was selected as an on-board control computer due to its small form factor. The add-on board pi3hat for Raspberry Pi from mjbots was used to communicate with the motor via the Controller Area Network (CAN) bus. It includes an Inertial Measurement Unit (IMU) for state estimation. Due to the single motor design, only the relative angle between the links can be directly measured. The angle and angular velocity of the support arm with respect to the vertical axis were computed using the IMU, resulting in a full state feedback of the system. The computing setup allows for real-time position, velocity, and torque control at a maximum frequency of 300 Hz with Python3. All electronics are powered by a 6S 1200 mAh LiPo battery.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B Electrical and Processing Architecture", "weight": 1.0} -->

For safety, a wireless emergency stop was implemented using a hobby-grade radio control (RC) remote and receiver combined with a direct current (DC)-DC converter and a relay switch.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Behavior Generation", "weight": 1.0} -->

Assuming that one support arm is always in contact with a bar, AcroMonk has two independent degrees of freedom (DOF) with one passive DOF at the shoulder ($q_{1}$) and one active DOF at the elbow ($q_{2}$).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Behavior Generation", "weight": 1.0} -->

Its system dynamics is similar to acrobot and is given: where $\mathbf{M}{(\mathbf{q})}$ denotes the mass-inertia matrix, $\mathbf{C}{(\mathbf{q},\overset{˙}{\mathbf{q}})}$ denotes the Coriolis and centrifugal matrix, $\tau_{g}{(\mathbf{q})}$ comprises the gravity effects, the actuation matrix is $\mathbf{B} = {\lbrack 0\quad 1\rbrack}^{T}$, and $u \in {\mathbb{R}}$ is the motor torque. The AcroMonk's schematic with the base and end-effector points is depicted in Figure 4.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Behavior Generation", "weight": 1.0} -->

Different colors are used to distinguish the support arm (blue) and the swing arm (green).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Behavior Generation", "weight": 1.0} -->

Inspired by the typical brachiation of a monkey depicted in Figure 1, we define four atomic sub-behaviors, the sequential composition of which can give rise to robust bidirectional brachiation over horizontal bars. In the following, we discuss the behavior state machine and methods to generate atomic behaviors including releases, swings, and grasps. For a better understanding, also refer to corresponding sections of the accompanying video.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Behavior State Machine", "weight": 1.0} -->

Considering a system that comprises the robot and bars, we denote three fixed points as Z (single support, hanging), B (double support with swing arm on backward bar), and F (double support with swing arm on forward bar). The four atomic sub-behaviors are transitions between these fixed points, i.e. Zero-to-Back (ZB), Zero-to-Front (ZF), Front-to-Back (FB), and Back-to-Front (BF). Because of the passive gripper choice, additional behaviors have to be considered to release the swing arm from a bar, which is denoted as Back Release (BR) and Front Release (FR) to initiate a BF or FB atomic behavior, respectively. To ensure that the hook rests in the groove before changing the support arm, Front Catch (FC) and Back Catch (BC) are necessary for grasping the bar from above and below. Schematic evolutions of the BR and FR motions are depicted in Figure 3, where the arrows illustrate the frame progression. Forward and backward brachiations result from a given sequence of the described swing and gripper behaviors.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Behavior State Machine", "weight": 1.0} -->

Finally, ZF and ZB transitions can either serve as the starting or recovery phase. As an example, consider the sequence ZB $\rightarrow$ BC $\rightarrow$ BR $\rightarrow$ BF $\rightarrow$ FC $\rightarrow$ BR $\rightarrow$ BF $\rightarrow$ FC resulting in two forward brachiation (not to be confused with FB) maneuvers starting from zero configuration of the robot, which includes switching of the swing and support arm and the motor's axis of rotation. If the system experiences a disturbance such that it cannot reach the desired fixed point F or B, it will eventually come to rest in the Z configuration. Here, it can perform a ZB or ZF behavior to continue the forward brachiation via BF.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Realization of Release & Catch Behaviors", "weight": 1.0} -->

The passive gripper design was empirically optimized such that the gripper's interactions with the monkey bars can be achieved with a control heuristic on the elbow motor, which depends on contact friction but is largely invariant to distance between the bars ($0.22 - 0.58$m). The anti-clockwise rotation of the motor is referenced as positive as depicted in Figure 4.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B1 Release", "weight": 1.0} -->

To simplify the control, BF and FB controllers are only engaged once the swing arm releases the bar. For BR, a constant positive torque of 2.5 Nm is applied for at least 0.05 seconds. After this, if the elbow velocity surpasses 1.45 rad/s, the controller switches to BF brachiation. Empirical state data $\mathbf{x} = {\lbrack\mathbf{q},\overset{˙}{\mathbf{q}}\rbrack}^{T}$ was collected over 20 trials at the point of controller transition.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B1 Release", "weight": 1.0} -->

The state standard deviations ${\mathbf{σ}}_{0}^{\text{BR}} = {\lbrack 0.03,0.03,0.08,0.11\rbrack}^{T}$ were found to be relatively low, thus the trial mean values of the state $\mathbf{x}_{0}^{\text{BR}} = {\lbrack{- 0.63},{- 1.87},{- 0.63},1.45\rbrack}^{T}$ at this transition point were used as a reliable initial condition for controller generation for BF. For FB swing, which starts with FR, a constant torque approach was insufficient due to the different contact angles of the hook on the bar. In order to clear the front bar, an initial high negative torque and a subsequent lower sustained positive torque is applied to lift the hook groove off the bar.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B1 Release", "weight": 1.0} -->

Similar to BR, state data was collected at this transition point, analyzed, and used as the initial condition $\mathbf{x}_{0}^{\text{FR}} = {\lbrack 0.51,2.21,{- 0.63},4.68\rbrack}^{T}$ for the FB controllers with ${\mathbf{σ}}_{0}^{\text{FR}} = {\lbrack 0.03,0.002,0.42,0.72\rbrack}^{T}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B2 Catch", "weight": 1.0} -->

The catch behavior is executed at the end of each atomic sub-behavior during continuous brachiation to provide a defined rotation point for the next brachiation. This is realized by applying a negative torque for 0.1 seconds with a magnitude of 0.8 Nm. Duration and magnitude were chosen empirically such that the bar slides into the groove if the hook is slightly misplaced, but no movement is caused if the bar is already resting in the groove.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Swing Behavior Generation", "weight": 1.0} -->

To complete the prerequisites for continuous brachiation, the atomic swing behaviors are generated using two different methods, namely trajectory optimization and RL.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C1 Trajectory Optimization", "weight": 1.0} -->

Finding the four atomic swing behaviors (ZF, ZB, FB, BF) for the AcroMonk system can be casted as a trajectory optimization problem: where the final cost term includes minimization of total trajectory time $T$ with weight $W$, and the running costs include a state regularization cost $\mathbf{x}^{T}{\mathbf{Q}\mathbf{x}}$ with $\mathbf{Q} = \mathbf{Q}^{T} \succeq 0$ and an effort regularization cost $u^{T}Ru$ with $\mathbf{R} = \mathbf{R}^{T} \succ 0$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C1 Trajectory Optimization", "weight": 1.0} -->

The set of constraints include first order ODE (2b) form of system dynamics given, state and effort limits (2c), initial and final values of the state (2d), and collision avoidance constraints (2e) where $\mathbf{p}$ is the current position of the end-effector (EE) obtained via forward kinematics and $\mathbf{p}_{\text{bar}}^{\text{B}},\mathbf{p}_{\text{bar}}^{\text{F}},r_{\text{bar}}$ denote the space-fixed position of the left and right bars and their radii as shown in Figure 4. Direct Collocation was used to find the optimal trajectories for the atomic behaviors using the Drake framework with SNOPT as the backend solver. The input trajectories are represented using a first-order hold trajectory while state trajectories are represented using a cubic spline interpolation.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-C1 Trajectory Optimization", "weight": 1.0} -->

The hyperparameters of the running cost evaluated over $N = 20$ knot points were empirically selected as ${\mathbf{Q} = {\text{diag}{}}},{R = 100}$ for all behaviors. The state and effort limits were conservatively chosen as $\mathbf{x}_{\text{lim}} = {({2.09\text{rad}},{2.88\text{rad}},{10\text{rad/s}},{10\text{rad/s}})}^{T}$ and $u_{\text{lim}} = 3$ Nm to limit the search space of decision variables $(\mathbf{x},u)$. The remaining hyperparameters are summarized in Table II for the four atomic behaviors.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C1 Trajectory Optimization", "weight": 1.0} -->

The final state $\mathbf{x}_{f}$ for reaching the backward bar (valid for ZB and FB movements) is chosen via the (position and velocity level) inverse kinematics map such that the EE reaches the cartesian point $\mathbf{p}_{f}^{B}$ with velocity ${\overset{˙}{\mathbf{p}}}_{f}^{B}$, following which the passive dynamics of the system brings the bar into gripper's region of attraction (shown in orange in Figure 4) and settles the system to its stable fixed point. A similar argument holds for choosing $\mathbf{x}_{f}$ for reaching the front bar in case of ZF and BF movements. It is crucial to minimize time in case of ZF and BF movements so that the EE reaches the point $\mathbf{p}_{f}^{F}$ (with velocity ${\overset{˙}{\mathbf{p}}}_{f}^{F}$) above the front bar with minimum number of swings.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C2 Reinforcement Learning", "weight": 1.0} -->

A BF controller was realized with model free RL, generating a policy $\pi$ which maps the observation $\mathbf{x} = {\lbrack\mathbf{q},\overset{˙}{\mathbf{q}}\rbrack}^{T}$ to the torque $u$ directly applied to the motor, such that a reward function $r$ is maximized. The full reward $r$ is the sum of the terms detailed in Table III.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-C2 Reinforcement Learning", "weight": 1.0} -->

$H$ denotes the Heaviside function, $\mathbf{p}$ are coordinates of the swing arm end effector, $\langle\rangle$ denotes the scalar product, $\mathbf{n}$ defines a linear separatrix trough $\mathbf{p}_{bar}$, $d = {\|{\mathbf{p} - \mathbf{p}_{bar}}\|}$, and $d_{\max}$ controls the region of influence of the term.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-C2 Reinforcement Learning", "weight": 1.0} -->

In addition, reward terms are used in configuration space ($r_{tc}^{+}$), and dynamics penalties on the torque, velocity, and first derivative of effort ($r_{u}^{-},r_{vel}^{-},r_{\overset{˙}{u}}^{-}$) to generate controllers that can be safely executed on the hardware. Finally, reaching the target configuration $\mathbf{q}^{\text{F}}$ with an error smaller than ${\Deltaq} = 0.05$ was rewarded ($r_{tar}^{+}$).

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-C2 Reinforcement Learning", "weight": 1.0} -->

Reward/Penalty term Close approximation of back bar Close approximation of support bar Approaching the target bar from below Approaching the target bar from above with d = [30 rbar, 15 rbar, 10 rbar] Hardware torque limit Hardware velocity limit $r_{vel}^{-} = {- {H\left({\left| \overset{˙}{q_{2}} \right| - 6} \right)\left({\left| \overset{˙}{q_{2}} \right| - 6} \right)^{2}}}$ $r_{\overset{˙}{u}}^{-} = {- {0.001\left| {u_{t} - u_{t - 1}} \right|}}$ Reach final configuration Table III: Reward (+) and penalty (-) terms Whereas calculating the reward requires information about the task space position $\mathbf{p}$ of the end effector, the observation of the policy only includes joint configurations and velocities. The reward function is visualized in Figure 5.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-C2 Reinforcement Learning", "weight": 1.0} -->

An episode was terminated if a collision occurred, or the maximal episode length of 2s or the target configuration with an error less than $\Deltaq$ was reached. The system dynamics were simulated with MuJoCo for training, at a simulation and control frequency of 250 Hz. Proximal Policy Optimization was used in the stable baselines implementation with default parameters. To account for realistic measurement noise, normally distributed noise with $\sigma = 0.025$ was added to the state observations. Similar reward setups can be used to train controllers for all other atomic behaviors.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Behavior Control", "weight": 1.0} -->

Having generated optimal trajectories, these have to be tracked and stabilized during execution. In the case of RL, some deliberation is usually needed in tuning the simulation parameters for the policy to perform well on the real system. The following section details the steps taken to realize the atomic swing behaviors and enable continuous and robust brachiation on the real robot.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Trajectory Tracking with PD", "weight": 1.0} -->

As a first method, we consider tracking the generated trajectories from Section III-C1 with PD control for all atomic behaviors. The commanded torque from the state feedback for the actuated joint is computed using: Here, ^∗^ denotes the nominal trajectories. We chose the controller gains $K_{p} = 100$ and $K_{d} = 2$ empirically at a control frequency of 300 Hz. An idling time of 0.1 seconds was used before engaging any Catch behavior to leave enough time for the catching hook to make contact with the target bar.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Trajectory Tracking with TVLQR", "weight": 1.0} -->

As an alternative, Time-Varying Linear Quadratic Regulator (TVLQR) control was also used to stabilize the nominal trajectories. TVLQR aims to minimize the error coordinates $\overline{\mathbf{x}} = {({\mathbf{x} - \mathbf{x}^{\ast}})}$ and $\overline{\mathbf{u}} = {({\mathbf{u} - \mathbf{u}^{\ast}})}$, where ^∗^ denote states of the nominal trajectory.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Trajectory Tracking with TVLQR", "weight": 1.0} -->

For this, a time-varying linearization using a Taylor series approximation is performed, resulting in a time-varying linear system in the error coordinates: The quadratic cost function is defined as: where $\mathbf{Q} = \mathbf{Q}^{T} \succeq 0$, $\mathbf{Q}_{f} = \mathbf{Q}_{f}^{T} \succeq 0$ and $\mathbf{R} = \mathbf{R}^{T} \succ 0$. The optimal cost-to-go can be written as a time-varying quadratic term and the controller gain $\mathbf{K}{(t)}$ be found by solving the differential Riccati Equation.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Trajectory Tracking with TVLQR", "weight": 1.0} -->

The final control law is then of the form: The hyperparameters for the TVLQR-stabilized BF behavior were empirically selected as $Q = {\lbrack 0.01,5,0.01,0.1\rbrack}$, $Q_{f} = {\lbrack 0.04,20,0.04,0.4\rbrack}$, and $R = 5$. These parameters worked for both swing arms. TVLQR stabilization was run at 260 Hz, slightly slower than PD, due to the extra computational step to find the closest point of the current state to the target trajectory. For continuous brachiation, in addition to the 0.1 second idling time before each catch, an additional 0.1 s pause between successive BF behaviors was introduced, since the method was more susceptible to deviations in the initial condition after BR. All other atomic behaviors can be stabilized by TVLQR, but we focus here on BF without loss of generality.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C Model Free RL Control", "weight": 1.0} -->

In contrast to the previous methods, RL trains the mapping of observations to torque control directly in simulation, not following a precomputed target trajectory. For direct torque control, there is a high demand on simulation accuracy for successful simulation to reality transfer. To ensure realistic damping losses, trajectories of $\mathbf{q},\overset{˙}{\mathbf{q}},\tau$ from a BF swing via trajectory tracking with PD were recorded. Simulated trajectories $\mathbf{q}_{\text{sim}},{\overset{˙}{\mathbf{q}}}_{\text{sim}}$ were obtained by replaying the recorded torques in simulation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-C Model Free RL Control", "weight": 1.0} -->

The damping parameters of the support hook contact on the bar and the motor were optimized such that the deviations ${\mathbf{q} - \mathbf{q}_{\text{sim}}},{\overset{˙}{\mathbf{q}} - {\overset{˙}{\mathbf{q}}}_{\text{sim}}}$ are minimized, following. The SHGO global optimizer (SciPy) yielded damping values of $\approx 0.044$ for the hook contact and $\approx 0.06$ for the motor. Furthermore, the BF controller was trained only for the swing arm connected to the motor housing. For BF with the other arm, the torque commands were scaled empirically by a factor of 0.92. The trained policy network was converted to a numpy function for deployment on the on-board computer. The controller was run at 80 Hz on the real system. Although capable to run faster, higher frequencies made the policy less stable, probably due to a higher impact of sensor noise.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-C Model Free RL Control", "weight": 1.0} -->

For continuous brachiation, the idling time before Catch was set to 0.2 s and the pause between subsequent BF behaviors to 0.5 s, both to the same end of giving the system enough time to settle and ensure low deviations from the expected initial condition after hook release.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Results & Discussion", "weight": 1.0} -->

Whereas in principle all behaviors can be achieved by different control methods (see Section III), we use the example of BF to benchmark the performance of Traj Opt + PD, Traj Opt + TVLQR, and RL policy-based control. All methods achieved high repeatability of the single BF behavior with a 100% success rate over five different trials. To simulate instantaneous disturbances due to collisions with the environment, a cardboard box (with dimensions $13 \times 8 \times 28$ cm and weight $160$ g) was placed on the ground in the swing path of the arm, roughly below the target bar. Here, only Traj Opt + PD could reliably recover with a success rate of 100%. Traj Opt + TVLQR recovered in 4/5 cases and the RL controller in 1/5 cases. Robustness to mass uncertainty was assessed by attaching a 200 g weight to the swing arm. The Traj Opt + PD controller compensated for this mismatch reliably, whereas both Traj Opt + TVLQR and RL failed in 5/5 tests.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Results & Discussion", "weight": 1.0} -->

To assess continuous brachiation performance, we benchmark timing and energy expenditure of five consecutive forward brachiations with all three control methods. Figure 7 shows the full maneuver's positions, velocity, and torque trajectories. Table IV summarizes benchmark values for maximum torque usage, trajectory tracking performance, overall energy consumption, and duration. The root-mean-square error of trajectory tracking is low for TVLQR and PD. This metric does not apply to RL since the policy does not track a trajectory. The peak torque is the lowest for TVLQR and highest for RL. The lowest energy consumption was achieved by RL for the whole maneuver, whereas PD had a considerably higher energy demand. The total time of transport is highest for RL, even though the controller needs the shortest time to complete one swing. The reason lies in the RL-based controller's sensitivity to disturbances and uncertainties during the maneuver. Therefore, longer pauses in comparison to the other methods between each brachiation maneuver are introduced to let the system settle down.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Results & Discussion", "weight": 1.0} -->

Max. Abs. Torque (Nm) Average RMS Error Total Energy (Joule) Table IV: Performance characteristics of controllers The results show that AcroMonk is an easily controllable system, despite its underactuation and passive gripper design. Realizing all atomic dynamics behaviors leads to successful and robust brachiation, while the system can recover from disturbances. The relative ease of controllability can be attributed to the balanced design and the novel, grooved grippers, that provide a well-determined starting point for each behavior.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Results & Discussion", "weight": 1.0} -->

The successful performance of five forward brachiation motions with all three control strategies is a novelty in the literature for a system with passive grippers and only one motor. The various controller types in this experiment showcase the advantages and disadvantages of different state of the art strategies. Simple PD trajectory stabilization performed well and indeed proved to be most robust to external disturbances. Given the design choices, this is not surprising since PD control will always force the trajectory back on track, provided enough torque is available. TVLQR incorporates a model of the system to track the desired trajectory, which, if it does not match the actual setup, e.g., when an unknown mass is added, will lead to sub-optimal performance. On the other hand, it can be more energy efficient due to incorporation of model knowledge. Combining an optimized simulation model with RL resulted in the most energy efficient controller, which is however also most susceptible to deviations from trained states, resulting in longer necessary pauses between behaviors and poor generalization to disturbances or long traversals.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

With AcroMonk, we present a novel canonical underactuated system for studying brachiation. Due to the grooved gripper design, it is easily and reliably controllable, making it the first system of such a low complexity to achieve multiple consecutive brachiation motions. The readily available components and straightforward assembly make it a suitable reference system for underactuated robotics research. Our future work will focus on the following issues. Despite some success, we were not yet able to produce reliable backward brachiation. The release behavior in this configuration is much harder to perform since it requires lifting the swing arm hook up from the bar leading to a mean initial condition of front release with higher standard deviation $({{\mathbf{σ}}_{0}^{\text{FR}} > {\mathbf{σ}}_{0}^{\text{BR}}})$. Also, due to the single-motor design, the desired support arm may seldomly unhook instead during this maneuver. To solve this problem, we are working on an improved gripper design with beveled edges to reduce the force required for unhooking.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We are also working on realizing even more dynamic behavior such as automatic release during continuous brachiation and ricocheting exploiting impacts during the kinodynamic planning. We already observed that a well adjusted impact force on the target bar can directly unhook the support arm, resulting in even smoother and more dynamic brachiation. Considering ricocheting, we could also generate brachiation in a single swing with a short flight phase when removing the torque limits of the controller. While this was not yet safely reproducible, it shows that the system is in principle capable of such behavior. Finally, brachiation over irregularly placed bars is another challenge to be tackled in future. The design and controllers discussed in this paper have been open-sourced to support education and research of brachiation with easy to implement hardware.
