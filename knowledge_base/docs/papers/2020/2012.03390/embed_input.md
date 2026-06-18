<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On Infusing Reachability-Based Safety Assurance within Planning Frameworks for Human-Robot Vehicle Interactions

Topics include Model predictive control, Predictive control, Robotics, Autonomous driving, Vehicles, Safety, Uncertainty, Real-time systems, Planning, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Action anticipation, intent prediction, and proactive behavior are all desirable characteristics for autonomous driving policies in interactive scenarios. Paramount, however, is ensuring safety on the road - a key challenge in doing so is accounting for uncertainty in human driver actions without unduly impacting planner performance. This paper introduces a minimally-interventional safety controller operating within an autonomous vehicle control stack with the role of ensuring collision-free interaction with an externally controlled (e.g., human-driven) counterpart while respecting static obstacles such as a road boundary wall. We leverage reachability analysis to construct a real-time (100Hz) controller that serves the dual role of (i) tracking an input trajectory from a higher-level planning algorithm using model predictive control, and (ii) assuring safety by maintaining the availability of a collision-free escape maneuver as a persistent constraint regardless of whatever future actions the other car takes. A full-scale steer-by-wire platform is used to conduct traffic weaving experiments wherein two cars, initially side-by-side, must swap lanes in a limited amount of time and distance, emulating cars merging onto/off of a highway.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We demonstrate that, with our control stack, the autonomous vehicle is able to avoid collision even when the other car defies the planner's expectations and takes dangerous actions, either carelessly or with the intent to collide, and otherwise deviates minimally from the planned trajectory to the extent required to maintain safety.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Decision-making and control for mobile robots is typically stratified into levels. A high-level planner, informed by representative yet simplified dynamics of a robot and its environment, might be responsible for selecting an optimal, yet coarse trajectory plan, which is then implemented through a low-level controller that respects more accurate models of the robot's dynamics and control constraints. While additional components may be required to flesh out a robot's full control stack from model to motor commands, selecting the right "division of responsibilities" is fundamental to system design.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

One consideration that defies clear classification, however, is how to ensure a mobile robot's safety when operating in close proximity with a rapidly evolving and stochastic environment. Safety is a function of uncertainty in both the robot's dynamics and those of its surroundings; high-level planners typically do not replan sufficiently rapidly to ensure split-second reactivity to threats, yet low-level controllers are typically too short-sighted to ensure safety beyond their local horizon.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Human-robot interactions are an unavoidable aspect of many modern robotic applications and ensuring safety for these interactions is critical, especially in applications such as autonomous driving where collisions may lead to life-threatening injury. However, ensuring safety within the planning and control framework can be very challenging due to the uncertainty in how humans may behave. To quantify this uncertainty, robots often rely on generative models of human behavior in order to inform their planning algorithms, thereby enabling more efficient and communicative interactions. In general, under nominal operating conditions that reflect the modeling assumptions, these model-based probabilistic planners can offer high performance (e.g., minimizing time and control effort for the robot). However, these planners alone are typically insufficient for ensuring absolute safety because (i) they depend on *probabilistic* models of human behavior and thus safety is not enforced deterministically, (ii) dangerous but low-likelihood events may not be adequately captured in the human behavior prediction model, and (iii) reasoning about these probabilistic behavior models is typically too computationally expensive for the planners to react in real time when humans strongly defy expectations and/or diverge from modeling assumptions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work we implement a control stack for a full-scale autonomous car (the "robot") engaging in close proximity interactions with a human-controlled vehicle (the "human"). Our control stack aims to stay true to planned trajectories from a high-level planner since freedom of motion is essential for the planner to carry out the driving task while conveying future intent to the other vehicle. At the same time, we allow the robot to deviate from the desired trajectory to the point that is necessary to maintain safety. Our primary tool for designing a controller that does not needlessly impinge upon the planner's choices is *Hamilton-Jacobi (HJ) backward reachability*. We provide a brief overview of the reachability analysis literature relevant to our work in Section 3.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Overview: Reachability Analysis", "weight": 1.0} -->

Given a dynamics model governing a robotic system incorporating control and disturbance inputs, reachability analysis is the study of the set of states that the system can reach from its initial conditions. It is often used for formal verification as it can give guarantees on whether or not the evolution of the system will be safe, i.e., whether the reachable set includes undesirable outcomes. Reachability analysis can be divided into two main paradigms: (i) forward reachability and (ii) backward reachability.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Overview: Reachability Analysis", "weight": 1.0} -->

*Forward Reachability Analysis:* The *forward reachable set* (FRS) is the set of states that the system could potentially be in after some time horizon $t$. This is computed by propagating the dynamics combined with all feasible control sequences and disturbances forward in time. When considering the interaction between two agents, for example a human and a robot, the forward reachable set is computed for the human and the robot plans to avoid this set to ensure collision-free trajectories (see Figure 1a). This *open-loop* mentality, however, leads to an overly-conservative robot outlook. That is, while considering actions in the present, the robot does not incorporate the possibility that its future observations of where the human goes might influence how much it actually needs to take avoidance actions; in short the robot's plan to avoid the FRS does not incorporate closed-loop feedback. To reduce the over-conservative nature of forward reachability, the time horizon $t$ for which the FRS is computed over is typically kept small and is recomputed frequently.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Overview: Reachability Analysis", "weight": 1.0} -->

This approach has been found to be effective in finding collision-free trajectories, but it is difficult to extend to interactive scenarios where there are more uncertainties in the rapidly changing environment. Aside from the overly-conservative nature of FRS, the key drawback with using forward reachability is that safety (i.e., avoiding the FRS) hinges on the planner's capabilities and operating frequency. Even if computing the FRS is instantaneous, the planner may still be unable to react to split-second threats.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Overview: Reachability Analysis", "weight": 1.0} -->

*Backward Reachability Analysis:* Let the target set represent a set of undesirable states (e.g., collision states of the system). The *backward reachable set* (BRS) is the set of states that could result in the system being in the target set, assuming worst-case disturbances, after some time horizon $t$. Specifically, the BRS represents the set of states from which there does not exist a controller that can prevent the robot dynamics from being driven into the target set under worst-case disturbances within a time horizon $t$. As such, to rule out such an eventuality, the BRS is treated as the "avoid set". Critical differences between the FRS and BRS are that (i) the BRS is computed *backwards* in time, and (ii) the BRS is computed assuming *closed-loop* reactions to the disturbances.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Overview: Reachability Analysis", "weight": 1.0} -->

Illustrated in Figure 1b, for the case of relative dynamics between human- and robot-controlled vehicles, computation of the BRS takes into account the fact that the robot is able to react to the human at any time and in any state configuration (if the human was to swerve into the robot, the robot can swerve too to avoid a collision). This leads to the BRS being less overly-conservative than the FRS. In practice, the results of the BRS computation are cached via a look-up table, and at run-time, the optimal robot policy can be computed via a near-instant lookup of the reachability cache. As such, we can always compute optimal actions for the robot at any state configuration and *regardless* of the high-level planner used.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Overview: Reachability Analysis", "weight": 1.0} -->

We elect to use backward reachability because (i) its non-overly conservative nature stemming from the closed-loop computation ensures that safe controls will be used only when necessary and not unduly impact planner performance, (ii) safety is defined intrinsically in the BRS computation whereas safety using FRS-based approaches depends on whether the robot's planned trajectory intersect the FRS, and (iii) it provides a computational handle on safe controls which can be evaluated at high operating frequencies to react to split-second threats.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Overview: Reachability Analysis", "weight": 1.0} -->

Moreover, we will compute the BRS using Hamilton-Jacobi (HJ) reachability analysis, a particular approach to computing reachable sets. There are many existing approaches, but there is always a trade-off between modeling assumptions, scalability, and representation fidelity (i.e., whether the method computes over- or under-approximations of the reachable set). Compared to alternatives approaches, HJ reachability is the most computationally expensive, but it is able to compute the BRS exactly^11^1With precision dependent on parameters of the numerical solver, e.g., discretization choices in mesh size/time step. for any general nonlinear dynamics with control and disturbance inputs because it essentially uses a brute force computation via dynamic programming. As a result, the BRS solution to the HJ reachability problem represents a constructive proof of the existence of a safety-preserving control policy (i.e., a safety certificate) from states outside the BRS. Despite the apparent computational drawbacks, we note that the BRS may be computed offline, and requires only a near-instant lookup during runtime, allowing it to be used in controllers or planners that run at a very high operational frequency.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Hamilton-Jacobi Backward Reachability Analysis", "weight": 1.0} -->

We briefly review relevant HJ backward reachability definitions for the remainder of this section; see Chen and Tomlin for a more in-depth treatment. HJ reachability casts the reachability problem as an optimal control problem and thus computing the reachable set is equivalent to solving the Hamilton-Jacobi-Isaacs (HJI) partial differential equation (PDE).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Hamilton-Jacobi Backward Reachability Analysis", "weight": 1.0} -->

The general HJ reachability formulation is as follows. Let the system dynamics be given by $\overset{˙}{x} = {f{(x,u,d)}}$ where $x \in {\mathbb{R}}^{n}$ is the state, $u \in \mathcal{U} \subset {\mathbb{R}}^{m}$ is the control, and $d \in \mathcal{D} \subset {\mathbb{R}}^{p}$ is the disturbance. For example, $x$ could be the state of a robot, $u$ be the robot's controls, $d$ be environmental disturbances such as wind, and $f$ be the dynamics of the robot. The system dynamics $f:{{{\mathbb{R}}^{n} \times \mathcal{U} \times \mathcal{D}}\rightarrow{\mathbb{R}}^{n}}$ are assumed to be uniformly continuous, bounded, and Lipschitz continuous in $x$ for a fixed $u$ and $d$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Hamilton-Jacobi Backward Reachability Analysis", "weight": 1.0} -->

Let $\mathcal{T} \subseteq {\mathbb{R}}^{n}$ be the target set that the system wants to avoid at the end of a time horizon $|t|$ (note that $t < 0$ when propagating backwards in time). For collision avoidance, $\mathcal{T}$ typically represents the set of states that are in collision with an obstacle. For brevity, the following description of HJ backward reachability will use notation relevant to the rest of the paper, that is, we are interested in collision avoidance for human-robot interactions. Despite the notation, the following theory is still applicable to general systems $\overset{˙}{x} = {f{(x,u,d)}}$ outside the domain of human-robot interactions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Hamilton-Jacobi Backward Reachability Analysis", "weight": 1.0} -->

In the context of human-robot interactions, $f{( \cdot )}$ describes the *relative dynamics* between the human and the robot (denoted by $f_{_{rel}}{( \cdot )}$ where the subscript $rel$ indicates the relative human-robot system), $u$ corresponds to the robot's controls, and $d$ corresponds to the human's controls since the human actions are treated as disturbance inputs. More concretely, let $(x_{_{R}},u_{_{R}})$ represent the robot state and control, $(x_{_{H}},u_{_{H}})$ represent the human state and control, and $x_{_{rel}}$ be the relative state between the human and the robot.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Hamilton-Jacobi Backward Reachability Analysis", "weight": 1.0} -->

Thus the relative dynamics of the robot and human are given by ${\overset{˙}{x}}_{_{rel}} = {f_{_{rel}}{(x_{_{rel}},u_{_{R}},u_{_{H}})}}$, and $\mathcal{T}$ represents the set of relative states corresponding to when the human and robot are in collision. The formal definition of the BRS, denoted by $\mathcal{A}{(t)}$, for the human-robot relative system is

<!-- chunk {"id": "body-0020", "role": "body", "section": "Hamilton-Jacobi Backward Reachability Analysis", "weight": 1.0} -->

$\mathcal{A}{(t)}$ represents the set of "avoid states" at time $t$ from which if the human followed an adversarial *policy* $u_{_{H}}{( \cdot )}$, any robot *policy* $u_{_{R}}{( \cdot )}$ would lead to the relative state trajectory $x_{_{rel}}{( \cdot )}$ being inside $\mathcal{T}$ within a time horizon $|t|$. Assuming optimal (i.e.,

<!-- chunk {"id": "body-0021", "role": "body", "section": "Hamilton-Jacobi Backward Reachability Analysis", "weight": 1.0} -->

The HJI PDE is solved starting from the boundary condition $V{(0,x_{_{rel}})}$, the sign of which reflects set membership of $x_{_{rel}}$ in $\mathcal{T}$.^22^2See Section 8 for discussion of specific choices of $V{(0,x_{_{rel}})}$. Thus computing the BRS is equivalent to solving the HJI PDE with boundary condition $V{(0,x_{_{rel}})}$; we cache the solution $V{(t,x_{_{rel}})}$ to be used online as a look-up table.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Hamilton-Jacobi Backward Reachability Analysis", "weight": 1.0} -->

For the case of the vehicle-vehicle interactions investigated in this work, when the control and maximum velocity capabilities of the human car are no greater than those of the robot car, one can take the limit $t\rightarrow{- \infty}$ and obtain the infinite time horizon BRS $\mathcal{A}_{\infty}$ with corresponding value function $V_{\infty}{(x_{_{rel}})}$.^33^3For ease of notation going forward we will often write $V:=V_{\infty}$. Intuitively, this prescribed parity in control authority ensures that if the human and robot start sufficiently far apart, then the human will never be able to "catch" the robot. This holds even if the human car may have transient maneuverability advantages over the robot as we assume later in this work. That is, we expect that the BRS will not encompass the entire state space as $t\rightarrow{- \infty}$, and in practice we compute the BRS over a sufficiently large finite time horizon to the point where it appears that the BRS has converged.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Hamilton-Jacobi Backward Reachability Analysis", "weight": 1.0} -->

We recognize that we make a strong assumption on the human and robot's control authority in enabling this computation. In reality, the human and robot car may have very different control authority (e.g., different engines resulting in different acceleration and velocity capabilities) and the infinite BRS may not be bounded. In such cases, practitioners may compute the BRS over a horizon suitable for the interaction where guarantees afforded by HJ reachability only hold over that time horizon. Illustrative slices of the value function and the BRS for the vehicle-vehicle relative dynamics with equal control and velocity capabilities considered in this work are shown in Figure 2 while Figure 3 illustrates the human-robot relative frame used to define the relative dynamics involved in the BRS computation (the mathematical details are given in Section 5.3). In Figure 2 (left), the pear-shaped BRS stems from the fact the robot car can swerve its front more rapidly than its rear to avoid collision. In Figure 2 (middle), if the robot car is traveling faster, it is unsafe for the robot car to be in the region behind the human car because a collision may be unavoidable if the human brakes abruptly.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Hamilton-Jacobi Backward Reachability Analysis", "weight": 1.0} -->

In Figure 2 (right), if the human car is traveling faster, in this case at an angle, it is unsafe for the robot to be in the region in front of the human car because the robot car may not be able to maneuver out of the way before the human catches up.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Hamilton-Jacobi Backward Reachability Analysis", "weight": 1.0} -->

We can compute the optimal robot collision avoidance control

<!-- chunk {"id": "body-0026", "role": "body", "section": "Hamilton-Jacobi Backward Reachability Analysis", "weight": 1.0} -->

which offers the greatest increase in $V{(x_{_{rel}})}$ assuming optimal (worst-case) actions by the human. For general nonlinear systems, computing the optimal collision avoidance control in Equation may be nontrivial as there could be multiple local maxima. For control/disturbance affine systems, however, the solutions to the optimal control/disturbance are bang-bang.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Hamilton-Jacobi Backward Reachability Analysis", "weight": 1.0} -->

Recall from Equation that when the system is outside of the avoid set $\mathcal{A}{(t)}$ (i.e., $V > 0$), there exists a robot policy (e.g., Equation ) that keeps the robot safe over a time horizon $|t|$ regardless of any (including adversarial) policy taken by the human. Previous applications of HJI solutions switch to the optimal control (Equation ) when near the boundary of the BRS, i.e., when safety is nearly violated This reflects the goal of HJ reachability-based safety which is to ensure that the system stays outside of the avoid set $\mathcal{A}{(t)}$, that is, the value function should always stay positive.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Hamilton-Jacobi Backward Reachability Analysis", "weight": 1.0} -->

In an interactive scenario where, for example, we may want to let a robot planner convey intent by nudging towards the human car to the extent that is safe, we prefer a less extreme control strategy. In the next section, we describe in detail how to infuse reachability-based safety assurance within a multi-tiered control framework that consists of different planning objectives.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Control Stack Architecture", "weight": 1.0} -->

In this section, we propose using a safety-preserving HJI controller, rather than switching to the optimal HJI controller defined in Equation, and describe how to incorporate it within an existing control stack---a high-level planner feeding desired trajectories to a low-level tracking controller---to enable safe human-robot interactions that minimally impinges on the high-level planning performance objective. The control stack architecture is illustrated in Figure 4. The proposed control stack is applicable to general human-robot interactions (e.g., an autonomous car interacting with a human-driven car, an autonomous manipulator arm working alongside a human, wheeled mobile robots navigating a crowded sidewalk). However, in this work, we focus on the traffic-weaving scenario, wherein two cars initially side-by-side must swap lanes in a limited amount of time and distance, because it is a representative interactive scenario that encapsulates many challenging characteristics inherent to human-robot interaction. Successful and smooth traffic-weaves rely on action anticipation, intent prediction, and proactive behavior from each vehicle, and ensuring safety is critical because collisions may lead to life-threatening injury.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Interaction Planner", "weight": 1.0} -->

Our proposed control framework is agnostic to the interaction planner used. The only assumption for the planner is that it outputs desired trajectories (which presumably reflect high-performance goal-oriented nominal behavior) for the robot car to track. In general, high-level planners often optimize objectives that weigh safety considerations (e.g., distance between cars) relative to other concerns (e.g., control effort), and typical to human-robot interactive scenarios, they may reason anticipatively with respect to a *probabilistic* interaction dynamics model. That is, although the planner is encouraged to select safer plans, safety is not enforced as a deterministic constraint at the planning level.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Interaction Planner", "weight": 1.0} -->

In this work, we use the traffic-weaving interaction planner from Schmerling et al.. It uses a predictive model of future human behavior to select desired trajectories for the robot car to follow, updated at $\sim$`<!-- -->`{=html}3Hz. We extend this work by using a hindsight optimization policy instead of the limited-lookahead action policy in order to encourage more information-seeking actions from the robot.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Tracking Controller", "weight": 1.0} -->

Given a desired trajectory from the interaction planner, the tracking controller computes optimal controls to track the desired trajectory. We assume that the outputs of the low-level tracking controller are directly usable by the robot's actuators (e.g., steering and longitudinal force commands for a vehicle, torque commands for each joint on a manipulator arm). As such, the tracking controller typically uses a more accurate dynamics model and operates at a much higher frequency ($\sim 100$Hz) than the interaction planner, often at the expense of environmental awareness. To ensure safety with respect to a dynamic obstacle (i.e., a human-driven vehicle) we incorporate additional constraints computed from HJ reachability analysis into the tracking optimization problem. These constraints are designed to ensure that at each control step the robot car does not enter an unsafe set of relative states that may lead to collision.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Tracking Controller", "weight": 1.0} -->

In this work, we are concerned with vehicle trajectory tracking. We adapt the real-time model predictive control (MPC) tracking controller from Brown et al. by modifying it to include an additional invariant set constraint detailed in the next section. This MPC tracking controller, operating at 100Hz, computes optimal controls to track a desired trajectory by solving an optimization problem at each iteration. The optimization problem is based on a single track vehicle model (also known as the bicycle model) and incorporates friction and stability control constraints (in addition to control and state constraints) while minimizing a combination of tracking error and control derivatives. A more in-depth treatment of this combined MPC and HJI controller is given in Section 6.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Safety-Preserving HJI Control", "weight": 1.0} -->

Rather than switching to the optimal avoidance controller defined in Equation when nearing safety violation, we propose adding containment in the *set of safety-preserving controls* as an additional constraint to the low-level MPC tracking controller. The set of safety-preserving controls

<!-- chunk {"id": "body-0035", "role": "body", "section": "Safety-Preserving HJI Control", "weight": 1.0} -->

represent the set of robot controls that ensure the value function is nondecreasing. This constraint can be computed online since the BRS is computed offline and the value function $V$ and its gradient $\nabla V$ are cached. Online we employ a safety buffer $\epsilon > 0$ so that when the condition ${V{(x_{_{rel}})}} \leq \epsilon$ holds, indicating that the robot is nearing safety violation, we add the constraint $u_{_{R}} \in {\mathcal{U}_{_{R}}{(x_{_{rel}})}}$ to the list of tracking controller constraints. By adding this additional safety-preserving constraint when near safety violation, the MPC tracking controller selects control actions that prevent the robot from further violating the safety threshold while simultaneously optimizing for tracking performance and obeying additional constraints. This results in a *minimally interventional safety controller*---the MPC tracking controller will only minimally deviate from the desired trajectory to the extent necessary to maintain safety for the robot car.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Safety-Preserving HJI Control", "weight": 1.0} -->

For the traffic-weaving scenario investigated in this paper, the MPC problem for vehicle trajectory tracking is formulated as a quadratic program (QP) (to enable fast solve time amenable to a 100Hz operating frequency) and hence requires the constraints to be linear. As such, we instead apply the constraint $u_{_{R}} \in {{\overset{\sim}{\mathcal{U}}}_{R}{(x_{_{rel}})}}$ where

<!-- chunk {"id": "body-0037", "role": "body", "section": "Safety-Preserving HJI Control", "weight": 1.0} -->

is a linearized approximation of $\mathcal{U}_{_{R}}{(x_{_{rel}})}$. Specifically, for the current relative state ${\overset{\sim}{x}}_{_{rel}}$, current robot control ${\overset{\sim}{u}}_{_{R}}$, and optimal, i.e., worst-case, human action defined analogously to Equation $u_{_{H}}^{\ast}$, the terms in the linearization are

<!-- chunk {"id": "body-0038", "role": "body", "section": "Safety-Preserving HJI Control", "weight": 1.0} -->

In general, $\mathcal{U}_{_{R}}{(x_{_{rel}})}$ may not be a half-space, leading to the linear approximation ${\overset{\sim}{\mathcal{U}}}_{_{R}}{(x_{_{rel}})}$ including controls outside of $\mathcal{U}_{_{R}}{(x_{_{rel}})}$. However, since we bound the change in the control inputs across each time step, feasible controls remain close to the linearization point where the approximation error is small.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Dynamics", "weight": 1.0} -->

In this section, we detail the vehicle dynamics model used to model the robot and human car, the relative dynamics model between the human and the robot necessary for computing the BRS, and the tracking dynamics used for the MPC tracking controller. We use a six-state nonlinear single track model to describe the robot car's dynamics and assume the human car obeys a four-state dynamically extended nonlinear unicycle model with longitudinal acceleration and yaw rate as control inputs. As a result, the relative dynamics model has seven states. This represents a compromise between model fidelity and the number of state dimensions in the relative dynamics; increasing the former reduces the amount of model mismatch with the real system while reducing the latter is essential since solving the HJI PDE suffers greatly from the curse of dimensionality. The computation becomes notoriously expensive past five or more state dimensions without compromising on grid discretization or employing some decoupling strategy.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Robot Vehicle Dynamics", "weight": 1.0} -->

The robot car (denoted by subscript $R$) will be modeled using the single track vehicle model illustrated in Figure 5. Let $(p_{x_{R}},p_{y_{R}})$ be the position of the robot car's center of mass defined in an inertial reference frame and $\psi_{_{R}}$ be the yaw angle (heading) of the robot car relative to the horizontal axis. $U_{x_{R}}$ and $U_{y_{R}}$ are the velocities in the robot car's body frame, and $r_{_{R}}$ is the yaw rate. The state for the single track model is $x_{_{R}} = \begin{bmatrix}
\end{bmatrix}^{T}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Robot Vehicle Dynamics", "weight": 1.0} -->

The control input $u_{_{R}} = \begin{bmatrix}
\end{bmatrix}^{T}$ consists of the steering command $\delta$ and longitudinal tire force $F_{x}$ which is distributed between the front and rear tires $F_{x} = {F_{x_{f}} + F_{x_{r}}}$ via a fixed mapping. Assuming a quadratic model of longitudinal drag force $({F_{x_{drag}} = {{- C_{d_{0}}} - {C_{d_{1}}U_{x_{R}}} - {C_{d_{2}}U_{x_{R}}^{2}}}})$ and for vehicle mass $(m)$ and moment of inertia $(I_{zz})$, and the distances from the center of mass to the front and rear axles ($d_{f}$, $d_{r}$), the equations of motion for the robot car are

<!-- chunk {"id": "body-0042", "role": "body", "section": "Robot Vehicle Dynamics", "weight": 1.0} -->

The controls are assumed to be limited by the steering system, friction limits, and power capacity of the vehicle. Using the brush coupled tire model by Pacejka, the lateral tire force $F_{y_{f}}$ and $F_{y_{r}}$ at the front and rear tires is a function of slip angle ($\alpha_{f},\alpha_{r}$), tire cornering stiffness ($C_{\alpha_{f}},C_{\alpha_{r}}$), longitudinal tire forces ($F_{x_{f}},F_{x_{r}}$), coefficient of friction ($\mu$), and normal tire forces ($F_{x_{f}},F_{z_{r}}$). As such, the lateral tire force for either the front or rear tires (denoted by $i \in {\{ f,r\}}$) is

<!-- chunk {"id": "body-0043", "role": "body", "section": "Human Vehicle Dynamics", "weight": 1.0} -->

The human car (denoted by subscript $H$) will be modeled using the dynamically extended unicycle model illustrated in Figure 6. Let $(p_{x_{H}},p_{y_{H}})$ be the position of the center of the human car's rear axle defined in an inertial reference frame and $\psi_{_{H}}$ be the yaw angle (heading) of the human car relative to the horizontal axis. The velocity of the human car in the vehicle frame is $v_{_{H}}$. The state for the dynamically extended unicycle model is $x_{_{H}} = \begin{bmatrix}
\end{bmatrix}^{T}$. The control input $u_{_{H}} = \begin{bmatrix}
\end{bmatrix}^{T}$ consists of the yaw rate $\omega$ and longitudinal acceleration $a$. The control limits of the human car are chosen such that the robot and human car share the same power, steering, and friction limits.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Human Vehicle Dynamics", "weight": 1.0} -->

The equations of motion for the human car are

<!-- chunk {"id": "body-0045", "role": "body", "section": "Human Vehicle Dynamics", "weight": 1.0} -->

Due to its simpler dynamics representation, the human car has a transient advantage in control authority over the robot car (it may change its path curvature discontinuously, while the robot may not), but by equating the steady-state control limits we ensure that the infinite time horizon BRS computation converges.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Relative Dynamics", "weight": 1.0} -->

The relative state (denoted by subscript $rel$) between the robot car and human car is defined with respect to a coordinate system centered on and aligned with the robot car's vehicle frame. We define the relative position $(p_{x_{rel}},p_{y_{rel}})$ as

<!-- chunk {"id": "body-0047", "role": "body", "section": "Relative Dynamics", "weight": 1.0} -->

Since the velocity states are defined with respect to the vehicle frame, we cannot define analogous relative velocity states and must include the individual velocity states of each vehicle. As such, the relative state for the human-robot vehicle system is $x_{_{rel}} = \begin{bmatrix}
\end{bmatrix}^{T}$. In the language of HJ reachability, the disturbance input of the system is the human car's control $d = u_{_{H}} = \begin{bmatrix}
\end{bmatrix}^{T}$ and the control input is the robot car's control $u = u_{_{R}} = \begin{bmatrix}
\end{bmatrix}^{T}$. Combining Equations and, the equations of motion for the relative system are

<!-- chunk {"id": "body-0048", "role": "body", "section": "Tracking Dynamics", "weight": 1.0} -->

The tracking MPC controller relies on an error dynamics model. Define a path (see Figure 5) through space where $s$ is the distance along the path and at any distance $s$, we know the path heading $\psi{(s)}$, the curvature $\kappa{(s)}$, and a coordinate system $(\hat{s},\hat{e})$ tangential and normal to the path. Given the position and heading of the robot car, we can project the car to the closest point on the path. Let the lateral error $e$ be the lateral distance along direction $\hat{e}$ and ${\Delta\psi} = {\psi_{_{R}} - \psi_{path}}$ be the robot car's heading relative to the path computed from this closest point. Using this projection and the robot car's dynamics from Equation, we can compute the error dynamics relative to the desired path.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Tracking Dynamics", "weight": 1.0} -->

Using the same notation defined previously in Equation, the state for the robot car tracking a desired path is $\hat{x} = \begin{bmatrix}
\end{bmatrix}^{T}$ and the controls $u = u_{_{R}} = \begin{bmatrix}
\end{bmatrix}^{T}$. The tracking dynamics are

<!-- chunk {"id": "body-0050", "role": "body", "section": "The MPC+HJI Trajectory Tracking Controller", "weight": 1.0} -->

In this section, we detail the optimization problem used in the MPC+HJI tracking controller, describe how this problem can be adapted to accommodate collision avoidance for static obstacles, and provide numerical details about the BRS computation used in this formulation. Central to an MPC controller is an optimization problem; at each time step, the controller solves an optimization problem to find an optimal control sequence, passes the first control input to the actuator, and then repeats this process. To be amenable to real-time applications, the optimization problem requires a fast solve time ($\sim 0.01$s). In this work, the MPC tracking problem is formulated as a convex optimization problem, namely a QP, enabling the use of efficient solvers which are capable of solving the QP within the tight operating frequency.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Optimization Problem", "weight": 1.0} -->

Both the trajectory tracking objective and safety-preserving control constraint rely on optimizing over the robot steering and longitudinal force inputs simultaneously. Let $q_{k} = \begin{bmatrix}
\end{bmatrix}^{T}$ be the state of the robot car with respect to a nominal trajectory at discrete time step $k$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Optimization Problem", "weight": 1.0} -->

We adopt the varying time steps method ($N_{short}$ time steps of size $\Deltat_{short}$ and $N_{long}$ time steps of size $\Deltat_{long}$) and stable handling envelope constraint from Brown et al. (expressed as $H_{k}$ and $G_{k}$ in the problem formulation below). To ensure the existence of a feasible solution, we use slack variables $\sigma_{\beta,k}$, $\sigma_{r,k}$, and $\sigma_{{}_{}^{}k}$ on the stability and HJI constraints. The HJI reachability constraint ${{M_{_{HJI}}u_{k}} + b_{_{HJI}}} \geq {- \sigma_{_{HJI}}}$ is activated only when ${V{(x_{_{rel}})}} \leq \epsilon$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Optimization Problem", "weight": 1.0} -->

Although HJI theory suggests that applying this constraint on the next action alone is sufficient, we apply it over the next $N_{_{HJI}} = 3$ timesteps (30ms lookahead) to account for the approximations inherent in our QP formulation. The MPC tracking problem is a quadratic program of the form

<!-- chunk {"id": "body-0054", "role": "body", "section": "Optimization Problem", "weight": 1.0} -->

The objective strives to minimize a combination of tracking error (longitudinal, lateral and angular), control rates (steering and longitudinal tire forces), and magnitude of the slack variables. The constraints ensure (i) continuity with the current and next state and control, (ii) the change in controls across each time step is bounded, (iii) the positivity of slack variables, (iv) the (linearized) dynamics are satisfied, (v) the vehicle stability constraints are satisfied, and (vi) the HJI safety-preserving half-plane constraint is satisfied when ${V{(x_{_{rel}})}} \leq \epsilon$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Optimization Problem", "weight": 1.0} -->

The time-discretization and linearizations (dynamics and constraints) we apply amount to an approximate variant of sequential quadratic programming (SQP). In particular, however, we solve one QP at each MPC step rather than the usual iteration until convergence. Since the tracking problems are so similar from one MPC step to the next, we find that this approach yields sufficient performance for our purposes. We interpolate along each solution trajectory to compute the linearization nodes for the QP at the next MPC step.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Optimization Problem", "weight": 1.0} -->

We use the `ForwardDiff.jl` automatic differentiation (AD) package implemented in the Julia programming language to linearize the trajectory tracking dynamics as well as the HJI relative dynamics for the safety-preserving constraint. We call the Operator Splitting Quadratic Program (OSQP) solver through the `Parametron.jl` modeling framework; this combination of software enables us to solve the following MPC optimization problem at 100Hz.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Adding Static Obstacles", "weight": 1.0} -->

The current formulation does not prevent the robot from driving very far from its nominal trajectory (e.g., completely off the road) in order to avoid the human. In more realistic road settings, there could be environmental constraints such as a concrete road boundary. In the same way that collision avoidance with a human-controlled vehicle is formulated as an additional constraint to the robot's MPC problem, we can add another safety constraint to account for a static wall to prevent the robot from swerving completely off the road. We consider two approaches for deriving this constraint: the first based on an additional HJI computation and giving rise to a similar control constraint applied over the first $N_{_{HJI}}$ timesteps, and the second treating the wall as a static obstacle with associated state constraints that apply over the whole duration of the MPC trajectory optimization.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Adding Static Obstacles", "weight": 1.0} -->

For the first approach, we can compute a value function $V_{_{WALL}}{(x_{_{R}})}$ describing the interaction between the robot and the wall by using Equation without the $p_{x_{R}}$ state (we only care about the distance from the wall and not how far along the wall the robot is). Two slices of the robot-wall BRS projected on the $p_{y_{R}} - \psi_{_{R}}$ plane are illustrated in Figure 7. Intuitively, if the robot is moving towards the wall, the faster it is moving, the further away it needs to be away from the wall in order for there to exist an optimal collision avoidance control. Note that since the wall is static, there is no disturbance input. The robot-wall HJI control constraint ${{M_{_{WALL}}u_{_{R}}} + b_{_{WALL}}} \geq 0$ becomes active when ${V_{_{WALL}}{(x_{_{R}})}} \leq \epsilon$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Adding Static Obstacles", "weight": 1.0} -->

This means that it is possible for both HJI-safety constraints to be active simultaneously. We note that theoretically we could consider the robot, human, and wall simultaneously by computing the BRS for the joint system. However, naively increasing the state size without any decomposition would be computationally undesirable even offline. Thus we treat the human-robot and robot-wall systems separately, but will discuss later the impact of this design choice.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Adding Static Obstacles", "weight": 1.0} -->

Alternatively, we can account for a static wall by adding lateral error bound constraints into the MPC tracking problem---this is the approach taken in Brown et al.. This involves always adding a left and right lateral error constraint ($e_{\min,k} \leq e_{k} \leq e_{\max,k}$) on each node point along the MPC trajectory such that the lateral deviation from the desired trajectory does not exceed the lateral distance to the wall.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Adding Static Obstacles", "weight": 1.0} -->

as well as a slack penalty, $W_{e}\sigma_{e}$ to the cost function. This approach ensures no collision with the wall over the MPC time horizon only (in contrast to HJI which is over an infinite time horizon) and in general provides higher tracking performance because the MPC controller can optimize tracking states and controls over the entire tracking trajectory. We investigate both these approaches and provide more discussion in Section 8.

<!-- chunk {"id": "body-0062", "role": "body", "section": "BRS Computation", "weight": 1.0} -->

We use the BEACLS toolkit implemented in C++ to compute the BRS. Since HJ reachability suffers from the curse of dimensionality, this is, to the best of our knowledge, the first attempt to use HJ reachability to compute the BRS for a seven-state relative system, especially with such high modeling fidelity. We, however, do sacrifice on grid size and use a relatively coarse grid compared to other literature standards. We linearly interpolate between grid points in order to evaluate the value function and its gradient at any given state (human-robot relative state or robot-wall state).

<!-- chunk {"id": "body-0063", "role": "body", "section": "BRS Computation", "weight": 1.0} -->

discretization takes approximately 70 hours on a 3.0GHz octocore AMD Ryzen 1700 CPU.

<!-- chunk {"id": "body-0064", "role": "body", "section": "BRS Computation", "weight": 1.0} -->

Computing the BRS requires computing the optimal control and disturbance defined in Equation. For the relative dynamics model, the optimal disturbance (i.e., human actions) is a bang-bang solution since the disturbance is affine. Due to the highly nonlinear nature of the dynamics, we use a uniform grid search across $\delta$ and $F_{x}$ to calculate optimal actions (i.e., robot actions).

<!-- chunk {"id": "body-0065", "role": "body", "section": "BRS Computation", "weight": 1.0} -->

For the robot-wall system, we compute the optimal control actions in the same fashion. We use a grid size of $21 \times 9 \times 9 \times 9 \times 9$ uniformly spaced over ${(p_{y_{R}},\psi_{_{R}},U_{x_{R}},U_{y_{R}},r_{_{R}})} \in {{\lbrack{- 3},7\rbrack} \times {\lbrack{- {\pi/2}},{\pi/2}\rbrack} \times {\lbrack 1,12\rbrack} \times {\lbrack{- 2},2\rbrack} \times {\lbrack{- 1},1\rbrack}}$; computing the BRS with this system and discretization takes approximately 40 minutes.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Results", "weight": 1.0} -->

(a) Controller comparison on experimental data where the robot car uses the MPC+HJI controller.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Results", "weight": 1.0} -->

(b) Controller comparison on experimental data where the robot car uses the switching controller.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Experimental Vehicle Platform", "weight": 1.0} -->

X1 is a flexible steer-by-wire, drive-by-wire, and brake-by-wire experimental vehicle developed by the Stanford Dynamic Design Lab (see Figure 8). It is equipped with three LiDARs (one 32-beam and two 16-beam), a differential GPS/INS which provides 100Hz pose estimates accurate to within a few centimeters as well as high fidelity velocity, acceleration, and yaw rate estimates. To control X1, desired steering ($\delta$) and longitudinal tire force ($F_{x_{f}},F_{x_{r}}$) commands are sent to the dSpace MicroAutoBox (MAB) which handles all sensor inputs except LiDAR (handled by the onboard PC) and implements all low level actuator controllers. Similarly, state information about the vehicle is obtained from the MAB.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Experimental Vehicle Platform", "weight": 1.0} -->

We use the Robot Operating System (ROS) to communicate with the MAB which handles sensing and control at the hardware level; the planning/control stack described in this work is running onboard X1 on a consumer desktop PC running Ubuntu 16.04 equipped with a quadcore Intel Core i7-6700K CPU and an NVIDIA GeForce GTX 1080 GPU. X1 parameters used in the equations of motion (Equation ) are listed in Appendix A.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Experimental Vehicle Platform", "weight": 1.0} -->

We also perform experiments using a LiDAR-visible 1/10-scale RC car (Figure 8 right) as the human-driven car to investigate the robustness of our proposed control stack with perception uncertainty.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Experimental Vehicle Platform", "weight": 1.0} -->

(a) Trade-off between total safety and average efficiency.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Experimental Vehicle Platform", "weight": 1.0} -->

(b) Trade-off between worst-case safety and worst-case efficiency.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Experiments", "weight": 1.0} -->

To evaluate our proposed control stack---a synthesis of a high-level probabilistic interaction planner with the MPC+HJI tracking controller---we perform full-scale human-in-the-loop traffic-weaving trials with X1 taking on the role of the robot car. To ramp up towards testing with two full-scale vehicles in the near future, we investigate two types of human car: (i) a virtual human-driven car and (ii) a 1/10-scale LiDAR-visible human-driven RC car. We scale the highway traffic-weaving scenario (mean speed $\sim$`<!-- -->`{=html}28m/s) in Schmerling et al. down to a mean speed of $\sim$`<!-- -->`{=html}8m/s by shortening the track (reducing longitudinal velocity by a constant) and scaling time by a factor of 4/3 (with the effect of scaling speeds by 3/4 and accelerations by 9/16). The value of the parameters in the MPC tracking problem are listed in Appendix B.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Experiments", "weight": 1.0} -->

We investigate and evaluate the effectiveness of our control stack by allowing the human car to act carelessly (i.e., swerving blindly towards the robot car) during the experiments. In Sections 7.2.1 and 7.2.2 we compare our proposed controller (MPC+HJI) against a tracking-only MPC controller (MPC) and a controller that switches to the HJI optimal avoidance controller when near safety violation (switching). In Section 7.2.3 we compare the two static obstacle avoidance approaches developed in Section 6.2 to a scenario with a virtual wall constraining the robot's trajectory. We investigate applying an extension of the same state-constraint-based static obstacle avoidance strategy to the problem of collision with a dynamic obstacle (the human) in Section 7.2.4 and discuss its shortcomings. Finally, in Section 7.2.5 we present experiments with the human car physically embodied by an RC car.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Virtual Human-Driven Vehicle", "weight": 1.0} -->

To ensure a completely safe experimental environment, our first tier of experimentation uses a joystick-controlled virtual vehicle for the human car and allows the robot control stack to have perfect observation of the human car state. Experimental trials of the probabilistic planning framework using (i) our proposed approach (MPC+HJI) and (ii) switching to the optimal HJI controller (switching) are shown in Figure 9, along with a simulated comparison between the two safety controllers and the tracking-only controller (MPC). For comparative purposes, the controllers were simulated with the displayed nominal trajectory held fixed, but in reality, the nominal trajectory in these experiments was updated at $\sim {3Hz}$. As expected, we see that when safety violation occurs, the MPC+HJI controller represents a middle ground between the tracking-only MPC which does not react to the human car's intrusion, and the switching controller which arguably overreacts with a large excursion outside the lane boundaries. Evidently, our proposed controller tries to be minimally interventional---the robot car swerves/brakes but only to an extent that is necessary.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Virtual Human-Driven Vehicle", "weight": 1.0} -->

Looking at the value function, we see that, as expected, the MPC+HJI controller aims to keep the value positive, but does not necessarily strive to increase it, while the switching controller aims to increase the value as much as possible. The MPC (tracking only) controller fails to increase the value at all when safety violation occurs. All controllers however, experience a period where the value is negative, even the two HJI-based controllers which theoretically guarantee safety. We believe this is due to model mismatch; we will discuss this point in more depth in Section 8.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Virtual Human-Driven Vehicle", "weight": 1.0} -->

Additionally, in some trials when the robot car was traveling faster, the activation of the HJI constraint resulted in the robot car performing a large but smooth swerve that traversed completely outside the lane boundaries. We address this limitation by adding a wall constraint into the MPC formulation discussed in Section 7.2.3.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Safety and Efficiency Trade-off", "weight": 1.0} -->

Our MPC+HJI controller considers the set of safety-preserving controls while optimizing its tracking performance when it is near safety violation. In contrast, the HJI switching controller uses the optimal avoidance control policy and as a result neglects to track the desired trajectory that was selected by the planner for interaction performance. As such, there is a trade off between safety, defined with respect to the value function, and efficiency.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Safety and Efficiency Trade-off", "weight": 1.0} -->

For use as a comparison metric, we define the notion of *total safety* of an interaction of time length $T$ as

<!-- chunk {"id": "body-0080", "role": "body", "section": "Safety and Efficiency Trade-off", "weight": 1.0} -->

which is the integral of the value function when it is negative. Total safety considers not only the magnitude of the safety violation, but also the duration of the violation. We can also define the *worst-case safety* as

<!-- chunk {"id": "body-0081", "role": "body", "section": "Safety and Efficiency Trade-off", "weight": 1.0} -->

which does not consider the duration of safety violation, but rather the worst-case safety violation with respect to the value function over the interaction.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Safety and Efficiency Trade-off", "weight": 1.0} -->

Efficiency of the interaction is more difficult to quantify. In this analysis, we define efficiency with respect to the $g$-forces experienced by the vehicle as this is a proxy for control effort and passenger comfort. Alternative metrics include time taken to complete the interaction, and friction available in the tires. We define *average efficiency* as

<!-- chunk {"id": "body-0083", "role": "body", "section": "Safety and Efficiency Trade-off", "weight": 1.0} -->

where $a_{x}{(t)}$ and $a_{y}{(t)}$ are the $x$ and $y$ acceleration of the robot car; larger $E_{avg}$values correspond to better efficiency. $g$-forces should not exceed one as this is beyond the physical limits of a vehicle. We also define the *worst-case efficiency* as

<!-- chunk {"id": "body-0084", "role": "body", "section": "Safety and Efficiency Trade-off", "weight": 1.0} -->

which considers the largest $g$-force experienced during the interaction.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Safety and Efficiency Trade-off", "weight": 1.0} -->

Given these quantities, we can compare the safety and efficiency trade-offs between the MPC, MPC+HJI, and switching controllers. Multiple experimental trials using X1 were carried out using each controller, and Figure 10a compares the average/total metrics while Figure 10b compares the worst-case metrics. We see that in both cases, the MPC+HJI controller provides a good balance between safety and efficiency; the safety almost equaling that of the optimal switching controller, and efficiency almost equaling that of the MPC controller. The switching controller provides the highest level of safety (with respect to the value function) but experiences lower efficiency since it often results in heavy braking and sharp swerving. The MPC controller provides lower safety scores but with larger variations as the resulting safety score is scenario dependent rather than controller dependent.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Safety and Efficiency Trade-off", "weight": 1.0} -->

(a) Comparison of steering angle. The plot begins when the robot car is planning autonomously.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Safety and Efficiency Trade-off", "weight": 1.0} -->

(b) Comparison of longitudinal force. The plot begins when the robot car is planning autonomously.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Safety and Efficiency Trade-off", "weight": 1.0} -->

constraint, and no constraints to avoid a static road boundary.
Figure 11: Comparison of control sequences from using MPC lateral error state constraints, robot-wall HJI control

<!-- chunk {"id": "body-0089", "role": "body", "section": "Static wall", "weight": 1.0} -->

We investigate two methods, (i) persistently adding lateral error state constraints into the MPC problem and (ii) adding an additional HJI-based control constraint for a robot-wall relative system into the MPC problem when ${V_{_{WALL}}{(x_{_{R}})}} \leq \epsilon$, for avoiding a static (virtual) road boundary wall when the robot car is swerving off the road to avoid a collision with the human car.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Static wall", "weight": 1.0} -->

Around 20 meters from the start of the roadway in Figure 12, the robot car begins to plan autonomously. Before then, the cars are following a straight line in order to speed up from $\approx {{1m}/s}$ to the desired interaction speed. To provide the cleanest comparison, all results in this subsection are derived from simulation. Starting in the right lane, we see in all cases that when safety is violated the robot car swerves to the right ($\delta < 0$). When using the lateral error constraints (Figure 12, top), the robot car essentially has a "look-ahead" capability because it is able to optimize its steering commands over the MPC tracking horizon, essentially distributing the responsibility of avoiding the wall across the entire tracking MPC horizon. As a result, the robot car is able to successfully and smoothly steer back onto the road and avoid the wall.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Static wall", "weight": 1.0} -->

When using the robot-wall HJI control constraint (Figure 12, center), the robot car does not preemptively swerve back onto the road and instead only reacts to the wall when ${V_{_{WALL}}{(x_{_{R}})}} \leq \epsilon$ as designed. The robot car performs a hard brake to the point of almost stopping^44^4Since the dynamic bicycle model is ill-defined for low speeds (thus explaining the oscillations in $F_{x}$), the experiment (when using the robot-wall HJI control constraint) is essentially over around $t = 9$. In general, the MPC problem can switch to the kinematic model at low speeds which is well defined in that speed region. and then begins to eventually command a maximum steering angle (18 deg). The sharp and abrupt behavior stems from the HJI formulation assuming the robot can and will take extreme actions, including cases when using the safety-preserving control set.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Static wall", "weight": 1.0} -->

As a result, the responsibility for evasive action is triggered at the very latest possible instance and compressed into a control constraint over a single (in practice 3) MPC timestep. This is in contrast to the other approach of always having MPC lateral error state constraints over the entire MPC horizon. The MPC+HJI controller is effective in avoiding dynamic obstacles, but for static obstacles, HJI is not suitable because it is unnecessary to reason about the dynamics of something that is static. With no wall constraints (Figure 12, bottom), the robot car swerves completely off the road, and in order to quickly get to the left lane before the end of the road (inscribed as an objective in the high-level planner), it overshoots to the other side of the road and also drives beyond the road boundary on the other side.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Static wall", "weight": 1.0} -->

(a) Simulation trial of using MPC+HJI for human car collision avoidance (including lateral error constraints for wall collision avoidance).

<!-- chunk {"id": "body-0094", "role": "body", "section": "Static wall", "weight": 1.0} -->

(b) Simulation trial of using lateral error constraints for both human car and wall collision avoidance.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Comparison to baseline dynamic obstacle avoidance", "weight": 1.0} -->

Motivated by the success of applying state constraints in the previous section, we compare our proposed framework (MPC+HJI for safe human-robot interaction) with a baseline approach of avoiding collision with the human car using lateral error constraints. In order to define safety state constraints over the duration of the robot trajectory, we must however make some assumption on the human's future trajectory. For this baseline, at each MPC iteration, we assume that the human car will continue moving at its current heading and with its current velocity.^55^5Alternatively, one could use a sample or a *maximum a posteriori* estimate from the interaction planner's prediction model. The lateral error constraint at each MPC time step is computed between the robot's desired trajectory and the human's projected trajectory---this is analogous to applying the approach taken in Brown et al. but with (deterministic) dynamic obstacles. A simulation of our proposed approach and the baseline approach is shown in Figure 13. Notably, in this simulation, the human car defies the baseline's linear-extrapolation-based prediction model and curves into the other lane towards the robot car.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Comparison to baseline dynamic obstacle avoidance", "weight": 1.0} -->

We see in Figure 13a that when using the MPC+HJI controller (with lateral error state constraints for wall avoidance), we are able to successfully avoid a collision with the human car and the wall, and maintain relative states outside the BRS. The baseline approach demonstrated in Figure 13b, on the other hand, collides with the human because its consideration of only one possible future (i.e., human trajectory) at each MPC step leads the robot into a region of inevitable collision (defined against all, including worst-case, human controls). In particular we see that as the human trajectory increases its curvature towards the middle of the lane change, the lateral error bounds (based on an assumption of constant velocity) are not stringent enough to maintain robot safety. The utility of the MPC+HJI approach is that it distills safety considerations with respect to all possible realizations of the human trajectory into a single control constraint. Moreover, this constraint is not overly conservative (to improve the state-constraint-based approach one might imagine defining lateral error constraints to avoid the entire forward reachable set of the human), because it incorporates the concept of closed-loop feedback into its BRS computation.

<!-- chunk {"id": "body-0097", "role": "body", "section": "1/10-Scale Human-Driven Vehicle", "weight": 1.0} -->

To begin investigating the effects of perception uncertainty on our safety assurance framework, we use three LiDARs onboard X1 to track a human-driven RC car, and implement a Kalman filter for human car state estimation (position, velocity, and acceleration). Even with imperfect observations, we show some successful preliminary results (an example is shown in Figure 14) at mean speeds of 4m/s, close to the limits of the RC car + LiDAR-visible mast in crosswinds at the test track. We observe similar behavior as in the virtual human car experiments, including the fact that the value function dips briefly below zero before the MPC+HJI controller is able to arrest its fall; we discuss this behavior in the next section.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Discussion", "weight": 1.5} -->

Beyond the qualitative and quantitative confirmation of our design goals, our experimental results reveal three main insights.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Discussion", "weight": 1.5} -->

*Takeaway 1: The reachability cache is underly-conservative with respect to robot car dynamics and overly-conservative with respect to human car dynamics.*

<!-- chunk {"id": "body-0100", "role": "body", "section": "Discussion", "weight": 1.5} -->

In all cases---hardware experiments as well as simulation results---the HJI value function $V$ dips below zero, indicating that neither the HJI+MPC nor even the optimal avoidance switching controller are capable of guaranteeing safety in the strictest sense. The root of this apparent paradox is in the computation of the reachability cache used by both controllers as the basis of their safety assurance. Though the 7-state relative dynamics model (Equation ) subsumes a single-track vehicle model that has proven successful in predicting the evolution of highly dynamic vehicle maneuvers, the way it is employed in computing the value function $V$ omits relevant components of the dynamics. In particular, when computing the optimal avoidance control (Equation ) as part of solving the HJI PDE, we assume total freedom over the choice of robot steering angle $\delta$ and longitudinal force command $F_{x}$, up to maximum control limits.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Discussion", "weight": 1.5} -->

This does not account, e.g., limits on the steering slew rate (traversing $\lbrack\delta_{\min},\delta_{\max}\rbrack$ takes approximately 2 seconds), and thus the value function is computed under the assumption that the robot can brake/swerve far faster than it actually can.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Discussion", "weight": 1.5} -->

We note that simply tuning the safety buffer $\epsilon$ is insufficient to account for these unmodeled dynamics. In Figure 9a we see that $V$ may drop from approximately 0.5 (the value when the two cars traveling at 8m/s start side-by-side in lanes) to -0.3 in the span of a few tenths of a second. Selecting $\epsilon > 0.5$ might give enough time for the steering to catch up, but such a selection would prevent the robot car from accomplishing the traffic weaving task even under nominal conditions, i.e., when the human car is equally concerned about collision avoidance. Even for $\epsilon = 0.05$, we see that the human car can cause the robot to swerve by just staying in its lane but with a small offset towards the robot's lane (see Figure 12). This is because the safety controller would push the robot car outside of its lane from the outset to maintain the buffer.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Discussion", "weight": 1.5} -->

This behavior follows from wide level sets associated with the transient control authority asymmetry (recall that in the HJI relative dynamics the human car may adjust its trajectory curvature discontinuously), assumed as a conservative safety measure as well as a way to keep the relative state dimension manageable.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Discussion", "weight": 1.5} -->

The simplest remedy for both of these issues is to increase the fidelity of the relative dynamics model by incorporating additional integrator states $\overset{˙}{\delta}$ for the robot and $\overset{˙}{\omega}$ for the human. Naively increasing the state dimension to 8 or 9, however, might not be computationally feasible (even offline) without devising more efficient HJI solution techniques or choosing an extremely coarse discretization over the additional states. By literature standards we already use a relatively coarse discretization grid for solving the HJI PDE; associated numerical inaccuracies may be another source of the observed safety mismatch and alternate grid choices are a possible subject of future investigation. We believe that simulation, accounting for slew rates, could be a good tool to prototype such efforts, noting that as it stands we have relatively good agreement between simulation and the experimental platform in our testing.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Discussion", "weight": 1.5} -->

*Takeaway 2: Interpretability of the value function $V$ should be a key consideration in future work.*

<!-- chunk {"id": "body-0106", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this work the terminal value function $V{(0,x_{_{rel}})}$ is specified as the separation/penetration distance between the bounding boxes of the two vehicles, a purely geometric quantity dependent only on $p_{x_{rel}}$, $p_{y_{rel}}$, and $\psi_{_{rel}}$. Recalling that V ($:=V_{\infty}$) represents the worst-case eventual outcome of a differential game assuming optimal actions from both robot and human, we may interpret the above results through the lens of worst-case outcomes, i.e., a value of -0.3 may be thought of as 30cm of collision penetration assuming optimal collision seeking/avoidance from human/robot. When extending this work to cases with environmental obstacles (e.g., concrete highway boundaries that preclude large deviations from the lane), or multi-agent settings where the robot must account for the uncertainty in multiple other parties' actions, for many common scenarios it may be the case that guaranteeing absolute safety is impossible.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Discussion", "weight": 1.5} -->

Instead of avoiding a BRS of states that might lead to collision, we should instead treat the value function inside the BRS as a cost. In particular we should specify more contextually relevant values of $V{(0,x_{_{rel}})}$ for states in collision, e.g., negative kinetic energy or another notion of collision severity as a function of the velocity states $U_{x_{R}}$, $U_{y_{R}}$, $v_{_{H}}$, and $r_{_{R}}$ in addition to the relative pose. This would lead to a controller that prefers, in the worst case, collisions at lower speed, or perhaps "glancing blows" where the velocities of the two cars are similar in magnitude and direction.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Discussion", "weight": 1.5} -->

*Takeaway 3: Static obstacles should be accounted for using MPC tracking state constraints and not HJI control constraints.*

<!-- chunk {"id": "body-0109", "role": "body", "section": "Discussion", "weight": 1.5} -->

It is natural to use HJI when reasoning about potential dangers from a dynamic, unpredictable agent, but for static obstacles there is no uncertainty in how the obstacle may act. That is, when the other agent is deterministic, there is no notion of optimizing robot safety policies over all worst-case actions by the other agent. Indeed, in this case it is possible to confidently extend the safety constraint along the entire MPC horizon, as demonstrated in Section 7.2.3. This is as opposed to deriving a safety constraint to be applied at the first step (on the present control action; the HJI+MPC approach), as must be done with a nondeterministic agent with unknown future trajectory. Spreading the collision avoidance constraint over the problem horizon allows for the MPC optimization to more smoothly accomplish its objectives (i.e., control smoothness and tracking performance) while maintaining safety. We note, however, that naive extensions of this approach to nondeterministic agents (recall Section 7.2.4) do not similarly provide strong safety assurances.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have investigated a control scheme for providing real-time safety assurance to underpin the guidance of a probabilistic planner for human-robot vehicle-vehicle interactions. By essentially projecting the planner's desired trajectory into the set of safety-preserving controls whenever safety is threatened, we preserve more of the planner's intent than would be achieved by adopting the optimal control with respect to separation distance. Our experiments show that with our proposed minimally interventional safety controller, we accomplish the high level objective (traffic weaving) despite the human car swerving directly onto the path of the robot car, and accomplish this relatively smoothly compared to using a switching controller that results in the robot car swerving more violently off the road. Further, we investigate the addition of a road boundary wall to our formulation to prevent the robot car from swerving completely out of the lane which could be dangerous in realistic road settings, and compare against a baseline approach using state constraints to avoid dynamic obstacles to show that our framework is better designed to keep the robot car safe even in the face of worst-case human car behaviors.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We note that this work represents only a promising first step towards the integration of reachability-based safety guarantees into a probabilistic planning framework. Future work includes investigating this framework for cases where the human and robot have very different dynamics, such as a pedestrian or cyclist interacting with a car, or a human interacting with a robotic manipulator, and for interactions involving multiple (more than two) agents. We may also consider adapting our approach to ensure high planning performance while guaranteeing satisfaction of constraints other than safety, e.g., task requirements specified by temporal logic constraints as considered in Chen et al.. In the context of human-robot vehicle interactions, we have already discussed the concrete modifications to this controller we believe are necessary to improve the practical impact of our theoretical guarantees; further study should also consider better fitting of the planning objective at the controller level. That is, instead of performing a naive projection, i.e., the one that minimizes trajectory tracking error, it is likely that a more nuanced selection informed by the planner's prediction model would represent a better "backup choice" in the case that safety is threatened.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We recognize that ultimately, guaranteeing absolute safety on a crowded roadway may not be realistic, but we believe that in such situations value functions derived from reachability may provide a useful metric for near-instantly evaluating the future implications of a present action choice.
