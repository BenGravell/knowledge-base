## Abstract

We propose a robust nonlinear model predictive control (MPC) scheme for trajectory-tracking control of autonomous vehicles at the limits of handling on non-planar road surfaces. We derive the dynamics from first principles and selectively omit terms with negligible dynamic influence to maintain real-time capability. The resulting MPC with a three-dimensional (3D) dynamic single-track model integrates relevant dynamic effects directly into the prediction model and leverages them to improve prediction accuracy and therefore control performance. Even if the influence of terrain-induced vertical loads on the total acceleration potential is modeled, tire-road interactions are subject to uncertainty and disturbance. The uncertainty-aware constraint tightening scheme introduces a margin to constraint bounds to keep the vehicle controllable and stable in this environment. To validate our proposed approach, we perform high-fidelity dynamic double-track vehicle dynamics simulations on a model of a real circuit. We find that our algorithm can improve trajectory-tracking accuracy while maintaining low computation times.

## Preliminaries

### I-A Introduction

Autonomous racing series like the *A2RL* and the *IAC* (see Figure 1) push algorithms for Autonomous Driving (AD) to the limits in pursuit of lap times and competitive racing maneuvers as shown by expert drivers \[hoffmann2025a2rl, Betz2022TUMAutonomousMotorsport\]. This paper focuses on the trajectory tracking module, developed to accurately follow a pre-planned path and velocity while maintaining vehicle stability and adherence to path and dynamics constraints. Model Predictive Control (MPC) offers a powerful, optimization-based control framework that balances competing objectives and handles coupled constraints typical in AD applications. However, the effectiveness of MPC relies on the accuracy of the prediction model in determining how current and future inputs influence future states. Model mismatch degrades performance and can result in a loss of closed-loop stability \[Rawlings2020MPC\]. While a Constraint Tightening (CT) can help to avoid constraint violations from model mismatch, it is usually only feasible for simple models that offer poor predictive quality at the limits \[Stano2023\]. While the effects of the Three-Dimensional (3D) geometry of road surfaces are often neglected in the design of tracking control modules, their explicit consideration has proven advantageous in related AD modules, such as trajectory planning \[Rowold2023\] and state estimation \[Goblirsch2024\]. Therefore, this paper studies the potential benefits of integrating dynamic 3D effects in the prediction model for robust MPC.

Figure 1: Autonomous vehicles Dallara of TUM Autonomous Motorsport and Unimore in a banked turn at the IAC.

### I-B Related Work

MPC has emerged as the de facto standard for high-performance trajectory tracking in AD applications, particularly racing, offering a flexible framework for approximately optimal control of nonlinear dynamics under constraints \[Rawlings2020MPC, Stano2023, Betz2022\].

The prediction model is one of the fundamental components defining the behavior of an MPC \[Schwenzer2021\]. Linear time invariant \[Wischnewski2021TubeMPC\], linear time-varying \[Wang2021\], and linear parameter-varying \[Alcala2020\] prediction models are computationally light and can be simple to parametrize. Conversely, nonlinear models allow utilization of more dynamic potential through better predictive quality at the dynamic limits \[Raji2022, Bongard2025IVRMPC\]. While more computationally demanding, MPC schemes based on the Dynamic Single Track Model (DSTM) have become widely adopted for AD in recent years for driving at the dynamic limits due to their accurate representation of tire and vehicle nonlinearities \[Stano2023\]. While several works have demonstrated the effectiveness of this model formulation in high-speed racing, most rely on simplified planar models that neglect the influence of 3D racetrack geometry entirely \[Bongard2025IVRMPC\] or only treat banking and slope as static disturbances \[Raji2022\].

Recent works in the adjacent field of raceline planning have shown that explicitly considering the accelerations from the rotating vehicle reference frame on the uneven racetrack can reduce lap times by making the prediction of vertical forces and therefore acceleration potential in turns more accurate \[Rowold2023, Lovato2022, Limebeer2015\]. A similar improvement was observed for the state estimation of autonomous race cars, where inclusion of the rotating reference frame in the dynamics of the Extended Kalman Filter led to a significant reduction in positional error on banked oval tracks \[Goblirsch2024\].

Despite these advances, many MPC designs for AD show performance degradation on 3D racetracks by neglecting the dynamic effects of 3D road geometries in their prediction models. Some MPC schemes account for roll dynamics on banked surfaces \[Liu2018\] or roll- and pitch from compliant suspension on planar surfaces \[Taghavifar2019\]. However, terrain-induced combined roll- and pitch dynamics are mostly unexplored in MPC plant models for autonomous racing and AD in general.

CT is a common method to enhance the robustness of constraint satisfaction under model mismatch by forcing a predictive back-off from constraint bounds. While this back-off is necessary for safety, it is detrimental to AD tracking performance by reducing the available path or acceleration potential. The closer the prediction model is to the real vehicle, the smaller the back-off can be.\
Tightening constraints by propagating uncertainties through prediction models is a challenging task to do non-conservatively and requires approximations, mostly explored for linear time-invariant models \[Wischnewski2022TubeMPCApproachHighSpeedOvals\]. A computationally efficient uncertainty-aware CT was previously proposed for a purely Two-Dimensional (2D) prediction, but its impact on 3D schemes was not explored \[Bongard2025IVRMPC\].

### I-C Contribution

This paper presents a robust MPC scheme that exploits 3D racetrack geometry to improve stability and tracking performance. Compared to previous work \[Bongard2025IVRMPC\], the main contributions are:

*Dynamic 3D model:* We combine uncertainty-aware CT with an extended DSTM defined in a rotating reference frame, enabling prediction of terrain-induced dynamics.

*Tire force modeling:* We extend the tire model to a load-dependent combined Pacejka formulation to capture terrain-induced dynamics and longitudinal load-transfer.

*System-level validation:* We implement the controller within a C++/ROS2 autonomous racing software stack and benchmark it in high-fidelity simulation against two relevant baselines, demonstrating improved tracking accuracy and robustness on a 3D racetrack.

### I-D Notation

We write derivatives of $x$ in time $t$ and path progress $s$ as $\overset{˙}{x} = \frac{dx}{dt}$ and $x^{\prime} = \frac{dx}{ds}$. Prefix subscripts indicate the reference frame, e. g., ${}_{}^{}{}_{\mathcal{B}\mathcal{C}}^{}$ is the angular velocity of $\mathcal{B}$ relative to $\mathcal{C}$ denoted in $\mathcal{A}$. We abbreviate $\sin x$ by $s_{x}$ (not to be confused with progress $s$) and $\cos x$ by $c_{x}$ where appropriate. For discrete-time dynamics, the signal $x$ at prediction step $k$ is written as $x_{k}$. ${\mathbb{I}}_{\lbrack a,b\rbrack}$ is the set of integers in the closed interval between $a$ and $b$.

## Methodology

### II-A Vehicle Model

The prediction model extends the Dynamic Single Track Model (DSTM) of \[Raji2022, Bongard2025IVRMPC\] with 3D racetrack rotations and a simplified load-dependent combined-slip Pacejka Magic Formula (MF) tire model. The DSTM lumps the wheels of each axle into one virtual wheel. Compared to the double-track vehicle model, with roll dynamics and individual tires, this simplified model reduces complexity while retaining the dominant lateral and longitudinal dynamics.

Figure 2: Vehicle on banked and slope racetrack with relevant frames: Inertial frame ℐ, trajectory frame 𝒯, and vehicle frame 𝒱. Note, the path deviation d is shown negative (positive is to the left of the reference line).

### II-A1 3D-DSTM

To describe the motion of the vehicle on a 3D surface, we employ three reference frames, shown in Figure 2: the inertial frame $\mathcal{I}$, the trajectory frame $\mathcal{T}$, and the body-fixed vehicle frame $\mathcal{V}$.

$\mathcal{T}$ is defined with the x-axis $x_{\mathcal{T}}$ in the direction of the planner reference velocity $v_{ref}$ and the z-axis $z_{\mathcal{T}}$ facing upwards, perpendicular to the road plane. $\mathcal{V}$ is fixed to the Center of Gravity (COG) of the vehicle with $x_{\mathcal{V}}$ pointing towards the center of the front axle, and $z_{\mathcal{V}}$ parallel to $z_{\mathcal{T}}$.

### Relative kinematics

The orientation of $\mathcal{T}$ relative to $\mathcal{I}$ is defined by three angles: heading $\chi$ (yaw), slope $\theta$ (pitch), and banking $\phi$ (roll). A position vector in the inertial frame $\mathcal{I}$ is transformed to the trajectory frame via:

where $\mathbf{R}_{x}{( \cdot )}$, $\mathbf{R}_{y}{( \cdot )}$, $\mathbf{R}_{z}{( \cdot )}$ are rotation matrices about the $x$, $y$, $z$ axes respectively, and ${}_{}^{}{}_{\mathcal{I}\mathcal{T}}^{}$ is the translation offset of the trajectory frame origin in $\mathcal{I}$. The rotation rate over path progress ${}_{}^{}{}_{\mathcal{T}\mathcal{I}}^{}$ can be evaluated in the $\mathcal{T}$-frame as

This is derived from the three successive frame rotations: yaw ($\chi^{\prime}$ in $z$), pitch ($\theta^{\prime}$ in $y$), and then roll ($\phi^{\prime}$ in $x$). The values $\phi,\theta,\chi,{\hat{\phi}}^{\prime},{\hat{\theta}}^{\prime},{\hat{\chi}}^{\prime}$ are properties of the reference trajectory, provided by the planning module \[Rowold2023\].

The vehicle $\mathcal{V}$ is positioned at a lateral offset $d$ from the trajectory reference line (positive to the left) and a heading offset $\Delta\psi$ from the racetrack heading. Thus, the angular velocity of the vehicle in the inertial frame is:

where $\overset{˙}{s}$ is the rate of progress along the path. For small heading deviations (${\Delta\psi} \ll 1$) and using $\overset{˙}{\psi} = {{\Delta\overset{˙}{\psi}} + {{\hat{\chi}}^{\prime}\overset{˙}{s}}}$, this simplifies to:

For compact notation we define ${{}_{}^{}{}_{\mathcal{V}\mathcal{I}}^{}} = \begin{bmatrix}
{\hat{\omega}}_{x} & {\hat{\omega}}_{y} & {\hat{\omega}}_{z}
\end{bmatrix}^{\top}$.

### Rigid-body dynamics

The law of conservation of angular and linear momentum applied to the system yields

with vehicle moment of inertia ${}_{}^{} = {{diag}{(0,I_{y},I_{z})}}$, mass $m$ and velocities $v_{x},v_{y},v_{z}$ of the COG projected in the road plane, i. e. ${}_{}^{} = \begin{bmatrix}
{v_{x} + {{\hat{\omega}}_{y}h}} & {v_{y} - {{\hat{\omega}}_{x}h}} & v_{z}
\end{bmatrix}^{\top}$. We neglect roll dynamics and, therefore, the rolling moment of inertia. Substituting into and evaluating the torque balance with the forces from Figure 2, we obtain

Evaluating the force balance yields

$m\begin{bmatrix} $= \begin{bmatrix} (8a)
{\hat{a}}_{x} \\ {m{({{{\overset{˙}{v}}_{x} + {{\overset{˙}{\hat{\omega}}}_{y}h} + {{\hat{\omega}}_{y}v_{z}}} - {{\hat{\omega}}_{z}v_{y}}})}} \\
{\hat{a}}_{y} \\ {m{({{{{\overset{˙}{v}}_{y} - {{\overset{˙}{\hat{\omega}}}_{x}h}} + {{\hat{\omega}}_{z}v_{x}}} - {{\hat{\omega}}_{x}v_{z}}})}} \\
{\hat{a}}_{z} {m{({{{\overset{˙}{v}}_{z} + {{\hat{\omega}}_{x}v_{y}}} - {{\hat{\omega}}_{y}v_{x}}})}}
\end{bmatrix}$ \end{bmatrix}$
\end{bmatrix} + \begin{bmatrix}
\end{bmatrix} + \begin{bmatrix}
& {{+ {\mathbf{R}_{z}{({\Delta\psi})}\mathbf{R}_{x}{(\phi)}\mathbf{R}_{y}{(\theta)}\mathbf{R}_{z}{(\chi)}{({- {mg}})}{\mathbf{e}}_{z}}}.}

Based on Table I, we neglect the gray-marked terms in and. These are approximately three to four orders smaller than the dominant terms over the considered operating range. Hence, removing these terms has a minor impact on the dynamics while reducing model complexity.

${\hat{\omega}}_{x},{\hat{\omega}}_{y},{\overset{˙}{\hat{\omega}}}_{x},{\overset{˙}{\hat{\omega}}}_{y},h,{\Deltah},{\Deltal},\delta,{\Delta\psi},\theta,\phi$

${\hat{\omega}}_{z},{\overset{˙}{\hat{\omega}}}_{z},v_{y},v_{z},l_{F},l_{R},d,\overset{˙}{d}$

Conservation of angular momentum

$I_{y}{\overset{˙}{\hat{\omega}}}_{y}$
$I_{z}{\overset{˙}{\hat{\omega}}}_{z}$

Conservation of linear momentum

${m{\overset{˙}{v}}_{z}} = {m{({{{\overset{˙}{\hat{\omega}}}_{x}d} + {{\hat{\omega}}_{x}\overset{˙}{d}}})}}$
$m{\overset{˙}{\hat{\omega}}}_{y}h$

$m{\overset{˙}{\hat{\omega}}}_{x}h$

TABLE I: Order of magnitude of terms in and

### Equations of motion

The equations of motion are given by the state and input vectors

$\mathbf{x}$ ${= \begin{bmatrix} (9a)
d & {\Delta\psi} & v_{x} & v_{y} & \overset{˙}{\psi} & \delta & T & B
\end{bmatrix}^{\top}},$
$\mathbf{u}$ ${= \begin{bmatrix} (9b)
\end{bmatrix}^{\top}},$

and state dynamics

$\overset{˙}{d}$ ${= {{v_{x}s_{\Delta\psi}} + {v_{y}c_{\Delta\psi}}}},$ (10a)
$\Delta\overset{˙}{\psi}$ ${= {\overset{˙}{\psi} - {{\hat{\chi}}^{\prime}\overset{˙}{s}}}},$ (10b)
${\overset{˙}{v}}_{x}$ ${= {{{{\overset{\sim}{a}}_{x} + {gs_{\theta}c_{\Delta\psi}}} - {gc_{\theta}s_{\phi}s_{\Delta\psi}} - {{\hat{\theta}}^{\prime}\overset{˙}{s}v_{z}}} + {\overset{˙}{\psi}v_{y}}}},$ (10c)
${\overset{˙}{v}}_{y}$ ${= {{{\overset{\sim}{a}}_{y} - {gs_{\theta}s_{\Delta\psi}} - {gc_{\theta}s_{\phi}c_{\Delta\psi}} - {\overset{˙}{\psi}v_{x}}} + {{\hat{\phi}}^{\prime}\overset{˙}{s}v_{z}}}},$ (10d)
$\overset{¨}{\psi}$ ${= {\frac{1}{I_{z}}{({{{l_{F}F_{yF}c_{\delta}} + {l_{F}F_{xF}s_{\delta}}} - {l_{R}F_{yR}}})}}},$ (10e)
$\overset{˙}{\delta}$ ${{= u_{d\delta}},{{\overset{˙}{T} = u_{dT}},{\overset{˙}{B} = u_{dB}}}},$ (10f)

where $\delta$ is the steering angle, $T \in {\lbrack 0,1\rbrack}$ is the normalized throttle, and $B \in {\lbrack 0,1\rbrack}$ is the normalized brake. The progress rate $\overset{˙}{s}$ is approximated as $\overset{˙}{s} \approx \frac{{v_{x}c_{\Delta\psi}} - {v_{y}s_{\Delta\psi}}}{1 - {d{\hat{\chi}}^{\prime}}}$, which follows from Frenet-frame kinematics: the numerator is the vehicle velocity projected onto the trajectory tangent, while the denominator accounts for the vehicle position relative to path curvature. $v_{z}$ is given by $v_{z} \approx {d{\hat{\phi}}^{\prime}\overset{˙}{s}}$, as $\mathcal{V}$ is offset by $d$ in the $\phi$-banked $\mathcal{T}$-frame. $F_{l}$ and $F_{d}$ are aerodynamic lift and drag forces, respectively, that are quadratically proportional to $v_{x}$. The apparent accelerations in the body frame are given by

${\overset{\sim}{a}}_{x}$ ${= {\frac{1}{m}\left( {{{{F_{xF}c_{\delta}} - {F_{yF}s_{\delta}}} + F_{xR}} - F_{d}} \right)}},$ (11a)
${\overset{\sim}{a}}_{y}$ ${= {\frac{1}{m}\left( {{F_{yF}c_{\delta}} + {F_{xF}s_{\delta}} + F_{yR}} \right)}}.$ (11b)

The longitudinal $F_{xF},F_{xR}$, lateral $F_{yF},F_{yR}$, and vertical $F_{zF},F_{zR}$ tire forces depend on the vehicle state $\mathbf{x}$, orientation, and rotation on the uneven racetrack, as outlined in section II-A2.

### II-A2 Tire forces

In the following, we describe the calculation of longitudinal and vertical tire loads, and how they affect the lateral traction force via a load-dependent slip angle formulation of the Pacejka MF tire model.

### Longitudinal and vertical load

To represent rear-wheel drive with braking on both axles, we utilize normalized throttle and brake inputs ${T,B} \in {\lbrack 0,1\rbrack}$ that determine the longitudinal tire forces on the front and rear axles via the throttle $C_{T}$, brake $C_{BF},C_{BR}$, and rolling resistance $C_{rr}$ constants \[Raji2022\]

The vertical axle load is given by the balance of angular momentum in $y_{\mathcal{V}}$ and the balance of linear momentum in $z_{\mathcal{V}}$ with the assumption $\delta \ll 1$. The small-angle assumption is used only to remove lateral-force dependence from the load-transfer expression in (14a). This simplification avoids an algebraic loop, as lateral force also depends on vertical load. The full steering dependence is retained in the main prediction dynamics and lateral-tire-force computation. Vertical load is given by

$F_{zF}$ ${= {{F_{z,{tot}}\frac{l_{R}}{l_{wb}}} + {\DeltaF_{z}}}},$ (14a)
$F_{zR}$ ${= {{F_{z,{tot}}\frac{l_{F}}{l_{wb}}} - {\DeltaF_{z}}}},$ (14b)

where ${\overset{˙}{v}}_{z}$ is approximated by ${\overset{˙}{v}}_{z} = {{\overset{˙}{d}{\hat{\phi}}^{\prime}\overset{˙}{s}} + {d{\hat{\phi}}^{\operatorname{\prime\prime}}{\overset{˙}{s}}^{2}} + {d{\hat{\phi}}^{\prime}\overset{¨}{s}}}$ and $\overset{¨}{s}$ is approximated by

which is valid for ${{\Delta\psi},{d{\hat{\chi}}^{\prime}},\delta} \ll 1$.

The coupling of longitudinal and vertical tire loads creates a problematic incentive: when the rear tire sideslip angle saturates, increasing the throttle raises the predicted rear axle vertical load and thus apparent lateral capability. While this is plausible for the idealized rigid DSTM (10a), the real vehicle includes a suspension and thus pitch dynamics. This means the system reacts more slowly than the prediction model anticipates. In practice, the vertical load on the rear axle cannot increase quickly enough to offset the loss in lateral stiffness caused by longitudinal slip. Thus, increasing the throttle does not raise rear axle traction but triggers wheel spin and traction control intervention. To avoid optimistic load transfer prediction in this situation, we define $T_{eff} = T$ in for body sideslip angle $\beta = {\arctan{(\frac{v_{y}}{v_{x}})}} \in {{\lbrack{- 0.06},0.06\rbrack}{rad}}$ but set $T_{eff} = 0$ for sideslip values outside this range. While including pitch dynamics in the prediction model would be a more *physical* and less heuristic solution, it introduces additional states (body pitch) and parameters (pitch stiffness, inertia). Thus, the presented solution with $T_{eff}$ targets a pragmatic trade-off between complexity and accuracy.

### Pacejka model and lateral force

The lateral acceleration is generated by the front and rear axle slip angles $\alpha_{i}$ given by

We use a modification of the MF tire force law by Pacejka \[Pacejka2012TireAndVehicleDynamics\] to describe how axle sideslip angle generates lateral force, dependent on vertical and longitudinal load:

where $i \in {\{ F,R\}}$, and ${dF_{zi}} = \frac{F_{zi} - F_{{z0},i}}{F_{{z0},i}}$ with nominal load $F_{{z0},i}$. $G_{{y\kappa},i} = {\cos{({\arctan{({C_{{Gy},i}F_{xi}})}})}}$ couples longitudinal force to lateral dynamics. $p_{{Dy1},i}$ and $p_{{Dy2},i}$ represent the affine dependence on the axle load, and $\lambda_{\mu,i}$ is an overall scaling factor. $B_{i}$, $C_{i}$ and $E_{i}$ are empirical shape parameters.

### II-B Control Design

### II-B1 MPC Setup

The Nonlinear Program (NLP) solved at each controller update step is given . It is similar to \[Bongard2025IVRMPC\], with a cost that balances tracking and time optimality, prioritizes vehicle stability, and accounts for unmodeled dynamics.

${\min\limits_{\substack{{\mathbf{x}}_{0},\ldots,{\mathbf{x}}_{N} \\ {\mathbf{u}}_{0},\ldots,{\mathbf{u}}_{N - 1} \\ {\mathcal{s}}_{0},\ldots,{\mathcal{s}}_{N - 1}}}{\sum\limits_{k = 0}^{N - 1}{\mathbf{y}_{k}^{\top}{\mathbf{Q}\mathbf{y}}_{k}}}} + {\mathbf{u}_{k}^{\top}{\mathbf{R}\mathbf{u}}_{k}} + {\rho{({\mathcal{s}}_{k})}} + {\mathbf{y}_{N}^{\top}\mathbf{Q}_{N}\mathbf{y}_{N}}$ (22a)
s. t. ${\mathbf{x}_{k + 1} = {\mathbf{f}_{d}{(\mathbf{x}_{k},\mathbf{u}_{k},\mathbf{p}_{k})}}},$ (22b)
${{d_{lb} - {\mathcal{s}}_{k}^{1}} \leq d_{k} \leq {d_{ub} + {\mathcal{s}}_{k}^{2}}},$ (22c)
${{\delta_{lb} - {\mathcal{s}}_{k}^{3}} \leq \delta_{k} \leq {\delta_{ub} + {\mathcal{s}}_{k}^{4}}},$ (22d)
${{\mathbf{u}_{lb} - {\mathcal{s}}_{k}^{7}} \leq \mathbf{u}_{k} \leq {\mathbf{u}_{ub} + {\mathcal{s}}_{k}^{8}}},$ (22f)
${{{{\overset{\sim}{a}}_{x,k} + {m_{r,k}{\overset{\sim}{a}}_{y,k}}} \leq {C_{r,k} + {\mathcal{s}}_{k}^{9,r}}}\quad{r \in {\mathbb{I}}_{\lbrack 1,\, 8\rbrack}}},$ (22g)
${{{\alpha_{i,{lb}} - {\mathcal{s}}_{k}^{10,i}} \leq \alpha_{i,k} \leq {\alpha_{i,{ub}} + {\mathcal{s}}_{k}^{11,i}}}\quad{i \in {\{ F,R\}}}},$ (22h)
${\mathbf{0} \leq {\mathcal{s}}_{k}},$ (22i)

The constraints (22b) to (22i) are imposed for $k \in {\mathbb{I}}_{\lbrack 0,{N - 1}\rbrack}$.

The cost terms in (22a) are given by

$\mathbf{y}_{k}$ ${= \begin{bmatrix} (23a)
{d_{k},{\overset{˙}{d}}_{k},{\Deltav_{k}},{T_{k}B_{k}},{\overset{˙}{a}}_{y,{kin},k},\frac{v_{k}}{{\overset{˙}{s}}_{k}}}
\end{bmatrix}^{\top}},$
$\mathbf{y}_{N}$ ${= {\lbrack{\overset{˙}{d}}_{N}\rbrack}}.$ (23c)

The NLP uses reference trajectory information ${\mathbf{p}}_{k}$ comprised of velocity $v_{{ref},k}$, banking, slope, curvature, and acceleration limits (in the form of $m_{r,k}$, $C_{r,k}$ as in (22g)) provided by the higher-level planning module. The reference trajectory signals are treated as purely time-varying under the assumption that the reference is tracked closely enough.

The stage cost (23a) is chosen such that $d$, $\overset{˙}{d}$, and ${\Deltav} = {v_{k} - v_{{ref},k}}$ incentivize tracking of the reference path and velocity. By including $\overset{˙}{d}$, we penalize lateral motion relative to the reference line, not just the absolute offset $d$. As a result, the controller is incentivized to minimize heading errors, especially at higher speeds, which improves tracking performance and stability. The product $TB$ penalizes simultaneous braking and throttle application, which is possible in the model but not intended in our overall hierarchical controller concept. Adding costs on the kinematic jerk ${\overset{˙}{a}}_{y,{kin}} = {\frac{d}{dt}\left( {\deltav_{x}^{2}} \right)} \approx {{\overset{˙}{\delta}v_{x}^{2}} + {2\delta{\overset{\sim}{a}}_{x}v_{x}}}$ incentivizes smooth lateral acceleration especially at higher velocities which helps to account for unmodeled dynamics.

The terminal cost term in (23c) penalizes lateral path error velocity at the end of the horizon. By driving ${\overset{˙}{d}}_{N}\rightarrow 0$, the predicted terminal state approaches motion parallel to the longer-term planner trajectory. Thus, we improve recursive feasibility for the short-term MPC prediction horizon.

For computational efficiency, the coupled acceleration envelope is represented as an octagon in the apparent-acceleration plane. Compared to an elliptic formulation, this yields eight linear inequalities in $({\overset{\sim}{a}}_{x},{\overset{\sim}{a}}_{y})$ and simpler derivatives, while also being compatible with the message interface between planning and control modules. Note that the resulting constraints (22g) are still nonlinear in the optimization variables through the mapping ${({\mathbf{x}},{\mathbf{u}})}\mapsto{({\overset{\sim}{a}}_{x},{\overset{\sim}{a}}_{y})}$.

The axle slip angle constraints (22h) are imposed as additional stability constraints. They discourage excessive tire sideslip angles by restricting the controller from using the nonlinear tire curve beyond its lateral traction force peak.

The constraints (22i) on the slacks ${\mathcal{s}}_{k} \in {\mathbb{R}}^{n_{\mathcal{s}}}$ represent element-wise non-negativity constraints ensuring slacks only relax selected constraints, which improves NLP feasibility under unforeseen circumstances. Meanwhile, linear and quadratic costs (23b) on the slacks keep the NLP close to the constrained solution when it is feasible.

The terminal constraint (22j) incentivizes keeping below the terminal target velocity, intended for recursive feasibility and safety.

### II-B2 Constraint Tightening (CT)

In autonomous racing, it is critical not to stress tires beyond their capabilities of longitudinal and lateral traction. Exceeding these limits results in excessive slip, a drop-off of tire forces, and ultimately a loss of vehicle stability in the form of critical over- or under-steer. Stability constraints in the form of coupled acceleration bounds at the center of mass can be added to the optimization problem as a proxy for tire friction potential \[Stano2023\]. However, a nominal MPC with stability constraints does not consider that real-world vehicle behavior, especially tire-road interaction, is inherently uncertain. Robust tube-MPC approaches extend nominal MPC by considering the propagation of uncertainty through the prediction model and introducing a margin to constraint bounds, with the aim of keeping the vehicle controllable and stable. In the following, we recall the previously introduced dynamic CT approach based on Control Contraction Metric (CCM) analysis for a two-dimensional single-track model under bounded uncertainty \[Bongard2025IVRMPC\].

The constraints (22c) to (22g) as well as the terminal speed constraint (22j) are formulated as one-sided constraints of the form ${h_{j}{({\mathbf{x}},{\mathbf{u}})}} \leq 0$ (ignoring slack variables for notational ease). Constraint Tightening (CT) is applied with a time-dependent scalar *tube size* $\sigma{(t)}$ and corresponding tightening constant $c_{j}$

The dynamics of the tube size $\sigma$ is then given as a function of nominal state and input

Thus, the tube size $\sigma$, characterizing our uncertainty around the nominal state and input, effectively becomes a state variable in the MPC prediction model. For notational clarity, we keep the robustification scheme with the tube dynamics (25 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")) separate from our nominal NLP defined .

In the tube dynamics (25 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")), $\beta$ and $L_{\mathbb{E}}$ are constants related to the achievable contraction of the uncertain model under external disturbances. $\mathcal{C}_{\sigma}$ is a constant related to the unknown but bounded parameter error vector. The state- and input-dependent *uncertainty* $f_{\sigma}{({\mathbf{x}},{\mathbf{u}})}$ is a worst-case bound over the vertices of the uncertain but bounded parameter and external disturbance vertices according to the CCM analysis \[Bongard2025IVRMPC\]. By design, $f_{\sigma}$ increases with the states relevant to vehicle stability: $v_{x}$, $v_{y}$, $\overset{˙}{\psi}$, and the longitudinal forces via $T$ and $B$. These states drive the uncertainty dynamics (25 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")). We refer to \[Bongard2025IVRMPC\] for the computation of these expressions, which is performed offline.

The tightening of path deviation constraints (22c) and acceleration constraints (22g) leads to a safety distance from path bounds and withheld acceleration potential later in the MPC horizon, respectively. The coupling of constraint and nominal dynamics (24 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")) allows the controller to consider uncertainties within the optimization. This enables the controller to automatically balance the tradeoff between trajectory tracking and vehicle stability \[Bongard2025IVRMPC\].

The proposed CT (24 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")), (25 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")) is intended to assist in keeping problem recursively feasible under uncertainty by covering the assumed set of uncertain trajectories within an uncertainty-dependent *tube*, and using this tube as a back-off from constraint bounds \[Sasfi2022\]. The CT is dependent on the uncertainty in order to tightly cover the set of uncertain trajectories and therefore induce the right amount of caution while avoiding unnecessary conservatism. In practice, the tube dynamics (25 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")) grow during aggressive maneuvers and tend to contract as the vehicle returns to nominal operating conditions. The limited number and interpretability of constants in (24 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")) make the CT tuneable by hand.

The MPC stability constraints (22g) on the apparent accelerations (11a), provided by the planning module, are strongly influenced by 3D racetrack geometry \[Rowold2023\]. While the CT leads to a more conservative behavior, the withheld acceleration potential is invariant under vertical loads. Instead, 3D racetrack geometry is indirectly considered through its impact on acceleration limits (see Fig. 3 ‣ II-B Control Design ‣ II Methodology ‣ Robust Nonlinear Trajectory Tracking Control for Autonomous Racing on Three-Dimensional Tracks")).

Figure 3: Side-by-side illustration of progressive tightening of acceleration constraints (22g) along the MPC horizon for two different (static) regimes of apparent gravity due to 3D racetrack geometry: Higher apparent gravity on the left, lower on the right. Shading indicates the horizon index, with low saturation at the start and high saturation at the end.

## Results

Figure 4: Layout of the Autodromo Nazionale di Monza circuit overlaid on a 500 m grid. Track elevation is represented by a color gradient. The curves Lesmo I &amp; II, used later, are highlighted.

Maximum tracking error max |d| across scenarios

Planner trajectory acceleration limit scale

Figure 5: Maximum absolute path deviation across two laps driven at various levels of planner trajectory aggressiveness, specified by the scaling value of the acceleration limits.

Figure 6: Path deviation d and vertical loads Fz F, Fz R in the turns Lesmo I and II for the scenario at 0.98 planner acceleration limit scale. The solid lines in the second and third plots show the loads assumed by the MPC prediction model. The dashed lines show the simulation ground-truth axle load values, calculated as the sum of the left and right tire forces.

For real-time capability, the presented controller is implemented with C-Code generated by the acados MPC framework \[Verschueren2021acados\]. The C-Code is integrated within a C++ node for the ROS2-based software stack used by *TUM Autonomous Motorsport* \[Betz2019SoftwareArchitecture, hoffmann2025a2rl\]. In this architecture, the reference trajectory with 3D geometry information and constraints is generated by a sampling-based planning algorithm \[gretmen2024\]. The prediction model (22b) is discretized using a Runge-Kutta method of order $4$ with a step size of $60\ {ms}$ and a horizon length of $36$ steps, giving a prediction horizon of $2.16\ s$. To minimize latency, we use the Real-Time Iteration (RTI) scheme \[Diehl2002RTI\]: for each control update, the NLP is linearized once around a warm start from the previous solution, one QP subproblem is solved, and the control input is extracted from the result. We employ HPIPM \[Frison2020\] with a fixed number of iterations for solving the resulting Quadratic Program (QP) in the intermediate speed setting BALANCE. The controller is running at an update frequency of $100\ {Hz}$.

The normalized throttle and brake forces optimized in NLP are converted to an acceleration request for the low-level longitudinal controller \[Pitschi2025\]. Conversely, the measured longitudinal acceleration is approximately converted to normalized throttle and brake forces as acceleration feedback.

To test the impact of the proposed changes, we evaluate three controller variants on a set of $20$ scenarios in a high-fidelity dynamic double-track vehicle simulation \[Sagmeister2024\]. The *Plane 2D* variant neglects all 3D effects. The *Static 3D* variant considers static banking and slope effects as in \[Raji2022\]. The *Dynamic 3D* variant considers all 3D acceleration outlined in II-A. All variants are parameterized with the same set of cost and slack weights.

Figure 4 shows the *Autodromo Nazionale di Monza* racetrack, which is used for all $20$ evaluation scenarios. The track's unique topology, with an elevation change of $13\ m$, a maximum slope of $2.6\%$, and speeds up to $255\ {{km}\ h^{- 1}}$, makes it a suitable testing ground for investigating the influence of dynamic acceleration. In this environment, vertical acceleration changes are mainly induced by the rotation of the vehicle traveling at high velocity on a curved road surface, rather than the absolute orientation (i.e., banking and slope). Each scenario consists of two laps, one out-lap and one race lap. The different scenarios are characterized by the scaling of the acceleration constraints used to generate the planner trajectories and the MPC acceleration limits (22g).

Figure 5 demonstrates the benefit of using the 3D-DSTM in the MPC across the different scenarios. The proposed control algorithm with the 3D-DSTM outperforms the plane 2D and static 3D variants by giving lower maximum absolute path errors. The *Dynamic 3D* variant is also able to stabilize the vehicle at higher acceleration limits.

To illustrate how the lower tracking error can be achieved with the *Dynamic 3D* variant, we plot the lateral error and predicted vertical tire load in the corners *Lesmo I* and *II* (Figure 4). In the first corner (*Lesmo I*), the racetrack slopes down and then levels for the apex of the corner. As a result of this change in slope, the ground-truth simulation vertical forces on the front and rear axles are significantly higher compared to the predictions of the *Plane 2D* and *Static 3D* variants (Figure 6 center and bottom). The *Dynamic 3D* approach with a rotating reference frame captures terrain dynamics more accurately, resulting in tire loads closer to the ground-truth values. Thus, the *Dynamic 3D* approach ultimately achieves superior tracking-performance on non-planar racetrack pieces (Figure 6 top). A similar effect can be observed to a lesser extent in the second corner (*Lesmo II*).

Figure 7: Overlaid histograms of MPC solve times for different prediction model levels of detail.

Figure 7 compares the distribution of solve times for the three controller variants. The tests were performed on an AMD Ryzen 7 PRO 7840U CPU with AVX2/AVX-512 support, rated to $2.7\ {GHz}$. Across $60\ s$ of runtime, we observe a similar average solve time of approximately $3.4\ {ms}$ for all three variants. Peak solve time is slightly higher in the *Dynamic 3D* variant compared to $5.3\ {ms}$ in the *Static 3D* and $5.6\ {ms}$ in the *Plane 2D* variants. The solve time median is $3.3\ {ms}$ for the *Dynamic 3D*, $3.4\ {ms}$ for the *Static 3D*, and $3.3\ {ms}$ for the *Plane 2D* variants. The distribution of solve times for all three variants indicates that the solve times remain feasible.

## Discussion

The presented MPC scheme addresses two prominent problems in trajectory-tracking control for autonomous racing, especially on highly 3D racetracks.\
The first is that performance is heavily dependent on the predictive quality of the plant model in the controller. This problem is ameliorated by incorporating the dominant forces from racetrack geometry directly into the prediction model. By thus improving the prediction quality (Fig. 6), the MPC is able to exploit road topography to increase tracking performance and vehicle stability (Fig. 5) while keeping solving times feasible (Fig. 7).\
The second problem is addressing the inevitable model mismatch under uncertainty and constraints, which can lead to constraint violations and, consequently, crashes. The presented CT provides an uncertainty-aware dynamic safety margin around constraints and reacts to varying overall normal forces via acceleration limits. However, the design is inherently 2D, and does not incorporate dynamic load changes. This simplification enables a fast update rate while still allowing the controller to incorporate dynamic, state-dependent uncertainty into the prediction.\
The consideration of load transfer effects touches on both problems. Longitudinal load transfer significantly influences the tire forces and is thus used by human race drivers \[Velenis2007\]. Its consideration is beneficial for control performance, as it improves the prediction of vertical load and, consequently, tire-ground dynamics. However, in edge cases, it can introduce adverse incentives, such as increasing throttle near the oversteer threshold. A more detailed coupled lateral/longitudinal tire force model \[Weber2024b\] with pitch dynamics could reduce this incentive, but would also be more computationally complex.\
The presented controller is developed for racing in the context of the *TUM Autonomous Motorsport* project \[hoffmann2025a2rl\].
