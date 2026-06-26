<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks

Topics include Model predictive control, Predictive control, Vehicles, Robustness, Uncertainty, Accuracy, Real-time systems, Online algorithms, Control, Vehicle dynamics.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a robust nonlinear model predictive control (MPC) scheme for trajectory-tracking control of autonomous vehicles at the limits of handling on non-planar road surfaces. We derive the dynamics from first principles and selectively omit terms with negligible dynamic influence to maintain real-time capability. The resulting MPC with a three-dimensional (3D) dynamic single-track model integrates relevant dynamic effects directly into the prediction model and leverages them to improve prediction accuracy and therefore control performance. Even if the influence of terrain-induced vertical loads on the total acceleration potential is modeled, tire-road interactions are subject to uncertainty and disturbance. The uncertainty-aware constraint tightening scheme introduces a margin to constraint bounds to keep the vehicle controllable and stable in this environment. To validate our proposed approach, we perform high-fidelity dynamic double-track vehicle dynamics simulations on a model of a real circuit. We find that our algorithm can improve trajectory-tracking accuracy while maintaining low computation times.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Abstract", "weight": 1.5} -->

We propose a robust nonlinear model predictive control (MPC) scheme for trajectory-tracking control of autonomous vehicles at the limits of handling on non-planar road surfaces. We derive the dynamics from first principles and selectively omit terms with negligible dynamic influence to maintain real-time capability. The resulting MPC with a three-dimensional (3D) dynamic single-track model integrates relevant dynamic effects directly into the prediction model and leverages them to improve prediction accuracy and therefore control performance. Even if the influence of terrain-induced vertical loads on the total acceleration potential is modeled, tire-road interactions are subject to uncertainty and disturbance. The uncertainty-aware constraint tightening scheme introduces a margin to constraint bounds to keep the vehicle controllable and stable in this environment. To validate our proposed approach, we perform high-fidelity dynamic double-track vehicle dynamics simulations on a model of a real circuit. We find that our algorithm can improve trajectory-tracking accuracy while maintaining low computation times.

<!-- chunk {"id": "body-0004", "role": "body", "section": "I-A Introduction", "weight": 1.0} -->

Autonomous racing series like the *A2RL* and the *IAC* (see Figure 1) push algorithms for Autonomous Driving ([AD]) to the limits in pursuit of lap times and competitive racing maneuvers as shown by expert drivers \[hoffmann2025a2rl, Betz2022TUMAutonomousMotorsport\]. This paper focuses on the trajectory tracking module, developed to accurately follow a pre-planned path and velocity while maintaining vehicle stability and adherence to path and dynamics constraints. Model Predictive Control ([MPC]) offers a powerful, optimization-based control framework that balances competing objectives and handles coupled constraints typical in [AD] applications. However, the effectiveness of [MPC] relies on the accuracy of the prediction model in determining how current and future inputs influence future states. Model mismatch degrades performance and can result in a loss of closed-loop stability \[Rawlings2020MPC\]. While a Constraint Tightening ([CT]) can help to avoid constraint violations from model mismatch, it is usually only feasible for simple models that offer poor predictive quality at the limits \[Stano2023\].

<!-- chunk {"id": "body-0005", "role": "body", "section": "I-A Introduction", "weight": 1.0} -->

While the effects of the Three-Dimensional ([3D]) geometry of road surfaces are often neglected in the design of tracking control modules, their explicit consideration has proven advantageous in related [AD] modules, such as trajectory planning \[Rowold2023\] and state estimation \[Goblirsch2024\]. Therefore, this paper studies the potential benefits of integrating dynamic [3D] effects in the prediction model for robust [MPC].

<!-- chunk {"id": "body-0006", "role": "body", "section": "I-B Related Work", "weight": 1.0} -->

[MPC] has emerged as the de facto standard for high-performance trajectory tracking in [AD] applications, particularly racing, offering a flexible framework for approximately optimal control of nonlinear dynamics under constraints \[Rawlings2020MPC, Stano2023, Betz2022\].

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-B Related Work", "weight": 1.0} -->

The prediction model is one of the fundamental components defining the behavior of an [MPC] \[Schwenzer2021\]. Linear time invariant \[Wischnewski2021TubeMPC\], linear time-varying \[Wang2021\], and linear parameter-varying \[Alcala2020\] prediction models are computationally light and can be simple to parametrize. Conversely, nonlinear models allow utilization of more dynamic potential through better predictive quality at the dynamic limits \[Raji2022, Bongard2025IVRMPC\]. While more computationally demanding, [MPC] schemes based on the Dynamic Single Track Model ([DSTM]) have become widely adopted for [AD] in recent years for driving at the dynamic limits due to their accurate representation of tire and vehicle nonlinearities \[Stano2023\]. While several works have demonstrated the effectiveness of this model formulation in high-speed racing, most rely on simplified planar models that neglect the influence of 3D racetrack geometry entirely \[Bongard2025IVRMPC\] or only treat banking and slope as static disturbances \[Raji2022\].

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-B Related Work", "weight": 1.0} -->

Recent works in the adjacent field of raceline planning have shown that explicitly considering the accelerations from the rotating vehicle reference frame on the uneven racetrack can reduce lap times by making the prediction of vertical forces and therefore acceleration potential in turns more accurate \[Rowold2023, Lovato2022, Limebeer2015\]. A similar improvement was observed for the state estimation of autonomous race cars, where inclusion of the rotating reference frame in the dynamics of the Extended Kalman Filter led to a significant reduction in positional error on banked oval tracks \[Goblirsch2024\].

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-B Related Work", "weight": 1.0} -->

Despite these advances, many [MPC] designs for [AD] show performance degradation on [3D] racetracks by neglecting the dynamic effects of [3D] road geometries in their prediction models. Some [MPC] schemes account for roll dynamics on banked surfaces \[Liu2018\] or roll- and pitch from compliant suspension on planar surfaces \[Taghavifar2019\]. However, terrain-induced combined roll- and pitch dynamics are mostly unexplored in [MPC] plant models for autonomous racing and [AD] in general. [CT] is a common method to enhance the robustness of constraint satisfaction under model mismatch by forcing a predictive back-off from constraint bounds. While this back-off is necessary for safety, it is detrimental to [AD] tracking performance by reducing the available path or acceleration potential.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-B Related Work", "weight": 1.0} -->

The closer the prediction model is to the real vehicle, the smaller the back-off can be.\Tightening constraints by propagating uncertainties through prediction models is a challenging task to do non-conservatively and requires approximations, mostly explored for linear time-invariant models \[Wischnewski2022TubeMPCApproachHighSpeedOvals\]. A computationally efficient uncertainty-aware [CT] was previously proposed for a purely Two-Dimensional ([2D]) prediction, but its impact on [3D] schemes was not explored \[Bongard2025IVRMPC\].

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-C Contribution", "weight": 1.0} -->

This paper presents a robust [MPC] scheme that exploits [3D] racetrack geometry to improve stability and tracking performance. Compared to previous work \[Bongard2025IVRMPC\], the main contributions are: *Dynamic [3D] model:* We combine uncertainty-aware [CT] with an extended [DSTM] defined in a rotating reference frame, enabling prediction of terrain-induced dynamics.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-C Contribution", "weight": 1.0} -->

*Tire force modeling:* We extend the tire model to a load-dependent combined Pacejka formulation to capture terrain-induced dynamics and longitudinal load-transfer.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-C Contribution", "weight": 1.0} -->

*System-level validation:* We implement the controller within a C++/ROS2 autonomous racing software stack and benchmark it in high-fidelity simulation against two relevant baselines, demonstrating improved tracking accuracy and robustness on a [3D] racetrack.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-D Notation", "weight": 1.0} -->

We write derivatives of $x$ in time $t$ and path progress $s$ as $\dot{x}=\frac{\mathrm{d}x}{\mathrm{d}t}$ and $x^{\prime}=\frac{\mathrm{d}x}{\mathrm{d}s}$. Prefix subscripts indicate the reference frame, e. g., ${}_{\mathcal{A}}\bm{\omega}_{\mathcal{BC}}$ is the angular velocity of $\mathcal{B}$ relative to $\mathcal{C}$ denoted in $\mathcal{A}$. We abbreviate $\sin{x}$ by $\mathrm{s}_{x}$ (not to be confused with progress $s$) and $\cos{x}$ by $\mathrm{c}_{x}$ where appropriate. For discrete-time dynamics, the signal $x$ at prediction step $k$ is written as $x_{k}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-D Notation", "weight": 1.0} -->

$\mathbb{I}_{\left[a,\,b\right]}$ is the set of integers in the closed interval between $a$ and $b$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Vehicle Model", "weight": 1.0} -->

The prediction model extends the Dynamic Single Track Model ([DSTM]) of \[Raji2022, Bongard2025IVRMPC\] with [3D] racetrack rotations and a simplified load-dependent combined-slip Pacejka Magic Formula ([MF]) tire model. The [DSTM] lumps the wheels of each axle into one virtual wheel. Compared to the double-track vehicle model, with roll dynamics and individual tires, this simplified model reduces complexity while retaining the dominant lateral and longitudinal dynamics.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A1 3D-DSTM", "weight": 1.0} -->

To describe the motion of the vehicle on a [3D] surface, we employ three reference frames, shown in Figure 2: the inertial frame $\mathcal{I}$, the trajectory frame $\mathcal{T}$, and the body-fixed vehicle frame $\mathcal{V}$. $\mathcal{T}$ is defined with the x-axis $x_{\mathcal{T}}$ in the direction of the planner reference velocity $v_{\mathrm{ref}}$ and the z-axis $z_{\mathcal{T}}$ facing upwards, perpendicular to the road plane. $\mathcal{V}$ is fixed to the Center of Gravity ([COG]) of the vehicle with $x_{\mathcal{V}}$ pointing towards the center of the front axle, and $z_{\mathcal{V}}$ parallel to $z_{\mathcal{T}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Relative kinematics", "weight": 1.0} -->

The orientation of $\mathcal{T}$ relative to $\mathcal{I}$ is defined by three angles: heading $\chi$ (yaw), slope $\theta$ (pitch), and banking $\phi$ (roll). A position vector in the inertial frame $\mathcal{I}$ is transformed to the trajectory frame via: where $\mathbf{R}_{x}(\cdot)$, $\mathbf{R}_{y}(\cdot)$, $\mathbf{R}_{z}(\cdot)$ are rotation matrices about the $x$, $y$, $z$ axes respectively, and ${{}_{\mathcal{T}}\bm{r}_{\mathcal{IT}}}$ is the translation offset of the trajectory frame origin in $\mathcal{I}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Relative kinematics", "weight": 1.0} -->

The rotation rate over path progress ${}_{\mathcal{T}}\bm{\Omega}_{\mathcal{TI}}$ can be evaluated in the $\mathcal{T}$-frame as This is derived from the three successive frame rotations: yaw ($\chi^{\prime}$ in $z$), pitch ($\theta^{\prime}$ in $y$), and then roll ($\phi^{\prime}$ in $x$). The values $\phi,\theta,\chi,\hat{\phi}^{\prime},\hat{\theta}^{\prime},\hat{\chi}^{\prime}$ are properties of the reference trajectory, provided by the planning module \[Rowold2023\].

<!-- chunk {"id": "body-0020", "role": "body", "section": "Relative kinematics", "weight": 1.0} -->

The vehicle $\mathcal{V}$ is positioned at a lateral offset $d$ from the trajectory reference line (positive to the left) and a heading offset $\Delta\psi$ from the racetrack heading. Thus, the angular velocity of the vehicle in the inertial frame is: where $\dot{s}$ is the rate of progress along the path. For small heading deviations ($\Delta\psi\ll 1$) and using $\dot{\psi}=\Delta\dot{\psi}+\hat{\chi}^{\prime}\dot{s}$, this simplifies to: For compact notation we define ${}_{\mathcal{V}}\bm{\omega}_{\mathcal{VI}}=\begin{bmatrix}\hat{\omega}_{x}&\hat{\omega}_{y}&\hat{\omega}_{z}\end{bmatrix}^{\top}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Equations of motion", "weight": 1.0} -->

The equations of motion are given by the state and input vectors and state dynamics where $\delta$ is the steering angle, $T\in$ is the normalized throttle, and $B\in$ is the normalized brake. The progress rate $\dot{s}$ is approximated as $\dot{s}\approx\frac{v_{x}\mathrm{c}_{\Delta\psi}-v_{y}\mathrm{s}_{\Delta\psi}}{1-d\hat{\chi}^{\prime}}$, which follows from Frenet-frame kinematics: the numerator is the vehicle velocity projected onto the trajectory tangent, while the denominator accounts for the vehicle position relative to path curvature. $v_{z}$ is given by $v_{z}\approx d\hat{\phi}^{\prime}\dot{s}$, as $\mathcal{V}$ is offset by $d$ in the $\phi$-banked $\mathcal{T}$-frame.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Equations of motion", "weight": 1.0} -->

$F_{l}$ and $F_{d}$ are aerodynamic lift and drag forces, respectively, that are quadratically proportional to $v_{x}$. The apparent accelerations in the body frame are given by The longitudinal $F_{xF},F_{xR}$, lateral $F_{yF},F_{yR}$, and vertical $F_{zF},F_{zR}$ tire forces depend on the vehicle state $\bm{x}$, orientation, and rotation on the uneven racetrack, as outlined in section II-A2.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A2 Tire forces", "weight": 1.0} -->

In the following, we describe the calculation of longitudinal and vertical tire loads, and how they affect the lateral traction force via a load-dependent slip angle formulation of the Pacejka [MF] tire model.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Longitudinal and vertical load", "weight": 1.0} -->

To represent rear-wheel drive with braking on both axles, we utilize normalized throttle and brake inputs $T,B\in$ that determine the longitudinal tire forces on the front and rear axles via the throttle $C_{T}$, brake $C_{BF},C_{BR}$, and rolling resistance $C_{rr}$ constants \[Raji2022\] with wheelbase $l_{\mathrm{wb}}=l_{F}+l_{R}$.\The vertical axle load is given by the balance of angular momentum in $y_{\mathcal{V}}$ and the balance of linear momentum in $z_{\mathcal{V}}$ with the assumption $\delta\ll 1$. The small-angle assumption is used only to remove lateral-force dependence from the load-transfer expression in (14a). This simplification avoids an algebraic loop, as lateral force also depends on vertical load. The full steering dependence is retained in the main prediction dynamics and lateral-tire-force computation.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Longitudinal and vertical load", "weight": 1.0} -->

The coupling of longitudinal and vertical tire loads creates a problematic incentive: when the rear tire sideslip angle saturates, increasing the throttle raises the predicted rear axle vertical load and thus apparent lateral capability. While this is plausible for the idealized rigid [DSTM] (10a), the real vehicle includes a suspension and thus pitch dynamics. This means the system reacts more slowly than the prediction model anticipates. In practice, the vertical load on the rear axle cannot increase quickly enough to offset the loss in lateral stiffness caused by longitudinal slip. Thus, increasing the throttle does not raise rear axle traction but triggers wheel spin and traction control intervention. To avoid optimistic load transfer prediction in this situation, we define $T_{\mathrm{eff}}=T$ in for body sideslip angle $\beta=\arctan(\frac{v_{y}}{v_{x}})\in[-0.06,0.06]\,$\mathrm{rad}$$ but set $T_{\mathrm{eff}}=0$ for sideslip values outside this range.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Longitudinal and vertical load", "weight": 1.0} -->

While including pitch dynamics in the prediction model would be a more *physical* and less heuristic solution, it introduces additional states (body pitch) and parameters (pitch stiffness, inertia). Thus, the presented solution with $T_{\mathrm{eff}}$ targets a pragmatic trade-off between complexity and accuracy.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Pacejka model and lateral force", "weight": 1.0} -->

The lateral acceleration is generated by the front and rear axle slip angles $\alpha_{i}$ given by We use a modification of the [MF] tire force law by Pacejka \[Pacejka2012TireAndVehicleDynamics\] to describe how axle sideslip angle generates lateral force, dependent on vertical and longitudinal load: where $i\in\{F,R\}$, and $dF_{zi}=\frac{F_{zi}-F_{z0,i}}{F_{z0,i}}$ with nominal load $F_{z0,i}$. $G_{y\kappa,i}=\cos(\arctan(C_{Gy,i}F_{xi}))$ couples longitudinal force to lateral dynamics. $p_{Dy1,i}$ and $p_{Dy2,i}$ represent the affine dependence on the axle load, and $\lambda_{\mu,i}$ is an overall scaling factor.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B1 MPC Setup", "weight": 1.0} -->

The Nonlinear Program ([NLP]) solved at each controller update step is given. It is similar to \[Bongard2025IVRMPC\], with a cost that balances tracking and time optimality, prioritizes vehicle stability, and accounts for unmodeled dynamics.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-B1 MPC Setup", "weight": 1.0} -->

The constraints (22b) to (22i) are imposed for $k\in\mathbb{I}_{\left[0,N-1\right]}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-B1 MPC Setup", "weight": 1.0} -->

The cost terms in (22a) are given by The [NLP] uses reference trajectory information $\bm{p}_{k}$ comprised of velocity $v_{\mathrm{ref,k}}$, banking, slope, curvature, and acceleration limits (in the form of $m_{r,k}$, $C_{r,k}$ as in (22g)) provided by the higher-level planning module. The reference trajectory signals are treated as purely time-varying under the assumption that the reference is tracked closely enough.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-B1 MPC Setup", "weight": 1.0} -->

The stage cost (23a) is chosen such that $d$, $\dot{d}$, and $\Delta v=v_{k}-v_{\mathrm{ref,k}}$ incentivize tracking of the reference path and velocity. By including $\dot{d}$, we penalize lateral motion relative to the reference line, not just the absolute offset $d$. As a result, the controller is incentivized to minimize heading errors, especially at higher speeds, which improves tracking performance and stability. The product $TB$ penalizes simultaneous braking and throttle application, which is possible in the model but not intended in our overall hierarchical controller concept.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-B1 MPC Setup", "weight": 1.0} -->

Adding costs on the kinematic jerk $\dot{a}_{y,\mathrm{kin}}=\frac{d}{dt}\left(\delta v_{x}^{2}\right)\approx\dot{\delta}v_{x}^{2}+2\delta\tilde{a}_{x}v_{x}$ incentivizes smooth lateral acceleration especially at higher velocities which helps to account for unmodeled dynamics.

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-B1 MPC Setup", "weight": 1.0} -->

The terminal cost term in (23c) penalizes lateral path error velocity at the end of the horizon. By driving $\dot{d}_{N}\rightarrow 0$, the predicted terminal state approaches motion parallel to the longer-term planner trajectory. Thus, we improve recursive feasibility for the short-term [MPC] prediction horizon.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-B1 MPC Setup", "weight": 1.0} -->

For computational efficiency, the coupled acceleration envelope is represented as an octagon in the apparent-acceleration plane. Compared to an elliptic formulation, this yields eight linear inequalities in $(\tilde{a}_{x},\tilde{a}_{y})$ and simpler derivatives, while also being compatible with the message interface between planning and control modules. Note that the resulting constraints (22g) are still nonlinear in the optimization variables through the mapping $(\bm{x},\bm{u})\mapsto(\tilde{a}_{x},\tilde{a}_{y})$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-B1 MPC Setup", "weight": 1.0} -->

The axle slip angle constraints (22h) are imposed as additional stability constraints. They discourage excessive tire sideslip angles by restricting the controller from using the nonlinear tire curve beyond its lateral traction force peak.

<!-- chunk {"id": "body-0036", "role": "body", "section": "II-B1 MPC Setup", "weight": 1.0} -->

The constraints (22i) on the slacks $\bm{\mathcal{s}}_{k}\in\mathbb{R}^{n_{\bm{\mathcal{s}}}}$ represent element-wise non-negativity constraints ensuring slacks only relax selected constraints, which improves [NLP] feasibility under unforeseen circumstances. Meanwhile, linear and quadratic costs (23b) on the slacks keep the [NLP] close to the constrained solution when it is feasible.

<!-- chunk {"id": "body-0037", "role": "body", "section": "II-B1 MPC Setup", "weight": 1.0} -->

The terminal constraint (22j) incentivizes keeping below the terminal target velocity, intended for recursive feasibility and safety.

<!-- chunk {"id": "body-0038", "role": "body", "section": "II-B2 Constraint Tightening (CT)", "weight": 1.0} -->

In autonomous racing, it is critical not to stress tires beyond their capabilities of longitudinal and lateral traction. Exceeding these limits results in excessive slip, a drop-off of tire forces, and ultimately a loss of vehicle stability in the form of critical over- or under-steer. Stability constraints in the form of coupled acceleration bounds at the center of mass can be added to the optimization problem as a proxy for tire friction potential \[Stano2023\]. However, a nominal [MPC] with stability constraints does not consider that real-world vehicle behavior, especially tire-road interaction, is inherently uncertain. Robust tube-[MPC] approaches extend nominal [MPC] by considering the propagation of uncertainty through the prediction model and introducing a margin to constraint bounds, with the aim of keeping the vehicle controllable and stable. In the following, we recall the previously introduced dynamic [CT] approach based on Control Contraction Metric ([CCM]) analysis for a two-dimensional single-track model under bounded uncertainty \[Bongard2025IVRMPC\].

<!-- chunk {"id": "body-0039", "role": "body", "section": "II-B2 Constraint Tightening (CT)", "weight": 1.0} -->

The constraints (22c) to (22g) as well as the terminal speed constraint (22j) are formulated as one-sided constraints of the form $h_{j}(\bm{x},\bm{u})\leq 0$ (ignoring slack variables for notational ease). Constraint Tightening ([CT]) is applied with a time-dependent scalar *tube size* $\sigma(t)$ and corresponding tightening constant $c_{j}$ The dynamics of the tube size $\sigma$ is then given as a function of nominal state and input Thus, the tube size $\sigma$, characterizing our uncertainty around the nominal state and input, effectively becomes a state variable in the [MPC] prediction model. For notational clarity, we keep the robustification scheme with the tube dynamics (25 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")) separate from our nominal [NLP] defined.

<!-- chunk {"id": "body-0040", "role": "body", "section": "II-B2 Constraint Tightening (CT)", "weight": 1.0} -->

In the tube dynamics (25 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")), $\beta$ and $L_{\mathbb{E}}$ are constants related to the achievable contraction of the uncertain model under external disturbances. $\mathcal{C}_{\sigma}$ is a constant related to the unknown but bounded parameter error vector. The state- and input-dependent *uncertainty* $f_{\sigma}(\bm{x},\bm{u})$ is a worst-case bound over the vertices of the uncertain but bounded parameter and external disturbance vertices according to the [CCM] analysis \[Bongard2025IVRMPC\]. By design, $f_{\sigma}$ increases with the states relevant to vehicle stability: $v_{x}$, $v_{y}$, $\dot{\psi}$, and the longitudinal forces via $T$ and $B$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "II-B2 Constraint Tightening (CT)", "weight": 1.0} -->

These states drive the uncertainty dynamics (25 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")). We refer to \[Bongard2025IVRMPC\] for the computation of these expressions, which is performed offline.

<!-- chunk {"id": "body-0042", "role": "body", "section": "II-B2 Constraint Tightening (CT)", "weight": 1.0} -->

The tightening of path deviation constraints (22c) and acceleration constraints (22g) leads to a safety distance from path bounds and withheld acceleration potential later in the [MPC] horizon, respectively. The coupling of constraint and nominal dynamics (24 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")) allows the controller to consider uncertainties within the optimization. This enables the controller to automatically balance the tradeoff between trajectory tracking and vehicle stability \[Bongard2025IVRMPC\].

<!-- chunk {"id": "body-0043", "role": "body", "section": "II-B2 Constraint Tightening (CT)", "weight": 1.0} -->

The proposed [CT] (24 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")), (25 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")) is intended to assist in keeping problem recursively feasible under uncertainty by covering the assumed set of uncertain trajectories within an uncertainty-dependent *tube*, and using this tube as a back-off from constraint bounds \[Sasfi2022\]. The [CT] is dependent on the uncertainty in order to tightly cover the set of uncertain trajectories and therefore induce the right amount of caution while avoiding unnecessary conservatism. In practice, the tube dynamics (25 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")) grow during aggressive maneuvers and tend to contract as the vehicle returns to nominal operating conditions. The limited number and interpretability of constants in (24 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")) make the [CT] tuneable by hand.

<!-- chunk {"id": "body-0044", "role": "body", "section": "II-B2 Constraint Tightening (CT)", "weight": 1.0} -->

The [MPC] stability constraints (22g) on the apparent accelerations (11a), provided by the planning module, are strongly influenced by [3D] racetrack geometry \[Rowold2023\]. While the [CT] leads to a more conservative behavior, the withheld acceleration potential is invariant under vertical loads. Instead, [3D] racetrack geometry is indirectly considered through its impact on acceleration limits (see Fig. 3 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Results", "weight": 1.0} -->

Maximum tracking error max |d| across scenarios Planner trajectory acceleration limit scale Figure 5: Maximum absolute path deviation across two laps driven at various levels of planner trajectory aggressiveness, specified by the scaling value of the acceleration limits.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Results", "weight": 1.0} -->

For real-time capability, the presented controller is implemented with C-Code generated by the acados [MPC] framework \[Verschueren2021acados\]. The C-Code is integrated within a C++ node for the ROS2-based software stack used by *TUM Autonomous Motorsport* \[Betz2019SoftwareArchitecture, hoffmann2025a2rl\]. In this architecture, the reference trajectory with [3D] geometry information and constraints is generated by a sampling-based planning algorithm \[gretmen2024\]. The prediction model (22b) is discretized using a Runge-Kutta method of order $4$ with a step size of $60\text{\,}\mathrm{ms}$ and a horizon length of $36$ steps, giving a prediction horizon of $2.16\text{\,}\mathrm{s}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Results", "weight": 1.0} -->

To minimize latency, we use the Real-Time Iteration ([RTI]) scheme \[Diehl2002RTI\]: for each control update, the [NLP] is linearized once around a warm start from the previous solution, one QP subproblem is solved, and the control input is extracted from the result. We employ HPIPM \[Frison2020\] with a fixed number of iterations for solving the resulting Quadratic Program ([QP]) in the intermediate speed setting BALANCE. The controller is running at an update frequency of $100\text{\,}\mathrm{Hz}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Results", "weight": 1.0} -->

The normalized throttle and brake forces optimized in [NLP] are converted to an acceleration request for the low-level longitudinal controller \[Pitschi2025\]. Conversely, the measured longitudinal acceleration is approximately converted to normalized throttle and brake forces as acceleration feedback.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Results", "weight": 1.0} -->

To test the impact of the proposed changes, we evaluate three controller variants on a set of $20$ scenarios in a high-fidelity dynamic double-track vehicle simulation \[Sagmeister2024\]. The *Plane [2D]* variant neglects all [3D] effects. The *Static [3D]* variant considers static banking and slope effects as in \[Raji2022\]. The *Dynamic [3D]* variant considers all [3D] acceleration outlined in II-A. All variants are parameterized with the same set of cost and slack weights.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Results", "weight": 1.0} -->

To illustrate how the lower tracking error can be achieved with the *Dynamic [3D]* variant, we plot the lateral error and predicted vertical tire load in the corners *Lesmo I* and *II* (Figure 4). In the first corner (*Lesmo I*), the racetrack slopes down and then levels for the apex of the corner. As a result of this change in slope, the ground-truth simulation vertical forces on the front and rear axles are significantly higher compared to the predictions of the *Plane 2D* and *Static [3D]* variants (Figure 6 center and bottom). The *Dynamic [3D]* approach with a rotating reference frame captures terrain dynamics more accurately, resulting in tire loads closer to the ground-truth values. Thus, the *Dynamic [3D]* approach ultimately achieves superior tracking-performance on non-planar racetrack pieces (Figure 6 top). A similar effect can be observed to a lesser extent in the second corner (*Lesmo II*).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Discussion", "weight": 1.5} -->

The presented [MPC] scheme addresses two prominent problems in trajectory-tracking control for autonomous racing, especially on highly [3D] racetracks.\The first is that performance is heavily dependent on the predictive quality of the plant model in the controller. This problem is ameliorated by incorporating the dominant forces from racetrack geometry directly into the prediction model. By thus improving the prediction quality (Fig. 6), the [MPC] is able to exploit road topography to increase tracking performance and vehicle stability (Fig. 5) while keeping solving times feasible (Fig. 7).\The second problem is addressing the inevitable model mismatch under uncertainty and constraints, which can lead to constraint violations and, consequently, crashes. The presented [CT] provides an uncertainty-aware dynamic safety margin around constraints and reacts to varying overall normal forces via acceleration limits. However, the design is inherently [2D], and does not incorporate dynamic load changes. This simplification enables a fast update rate while still allowing the controller to incorporate dynamic, state-dependent uncertainty into the prediction.\The consideration of load transfer effects touches on both problems.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Discussion", "weight": 1.5} -->

Longitudinal load transfer significantly influences the tire forces and is thus used by human race drivers \[Velenis2007\]. Its consideration is beneficial for control performance, as it improves the prediction of vertical load and, consequently, tire-ground dynamics. However, in edge cases, it can introduce adverse incentives, such as increasing throttle near the oversteer threshold. A more detailed coupled lateral/longitudinal tire force model \[Weber2024b\] with pitch dynamics could reduce this incentive, but would also be more computationally complex.\The presented controller is developed for racing in the context of the *TUM Autonomous Motorsport* project \[hoffmann2025a2rl\].
