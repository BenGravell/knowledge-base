<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Motion Planning and Control for Multi Vehicle Autonomous Racing at High Speeds

Topics include Model predictive control, Predictive control, Motion planning, Vehicles, Kalman filtering, Online algorithms, Offline algorithms, Optimization, Planning, Control, Kalman filter.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a multi-layer motion planning and control architecture for autonomous racing, capable of avoiding static obstacles, performing active overtakes, and reaching velocities above 75 m/s. The used offline global trajectory generation and the online model predictive controller are highly based on optimization and dynamic models of the vehicle, where the tires and camber effects are represented in an extended version of the basic Pacejka Magic Formula. The proposed single-track model is identified and validated using multi-body motorsport libraries which allow simulating the vehicle dynamics properly, especially useful when real experimental data are missing. The fundamental regularization terms and constraints of the controller are tuned to reduce the rate of change of the inputs while assuring an acceptable velocity and path tracking. The motion planning strategy consists of a Frenét-Frame-based planner which considers a forecast of the opponent produced by a Kalman filter. The planner chooses the collision-free path and velocity profile to be tracked on a 3 seconds horizon to realize different goals such as following and overtaking. The proposed solution has been applied on a Dallara AV-21 racecar and tested at oval race tracks achieving lateral accelerations up to 25 m/s^.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In the literature, several approaches for motion planning and control have been developed and tested on high-performance autonomous vehicles. Hierarchical methods which exploit different levels of model complexity at different stages of the motion planner/controller are the current state of the art. The strength of this approach has been shown, where a hierarchical method with a Nonlinear Model Predictive Control (NMPC) at its core was able to outperform a top driver on a formula student race car at lateral accelerations of over 20 m/s^2^.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

For the task of multi-vehicle racing, the gap between human expert drivers and autonomous systems is still significant. This is also related to the fundamental challenges that must be solved to tackle this task, which include perception, rule-based interaction with other agents and the infrastructure, motion prediction, generation, and tracking of optimal trajectories for overtakes in unstructured environments. Most related works in this field focus on racing video games, simulations, and RC cars, and very limited work is done on full-scale race cars. In, the authors use an NMPC algorithm with a 4-wheel vehicle model with additional states for the nearest obstacle. The solution has been tested in simulation with a control rate of 25 Hz and a maximum speed of 40 m/s. For RC cars several groups have tackled the problem using game-theoretical planners, however, these methods focus on one-vs-one racing and do not scale well to full size racetracks. Several algorithms based on Deep Neural Networks (DNN) have also been proposed.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

A curriculum reinforcement learning-based method using an off-policy algorithm has been evaluated on Gran Turismo Sports, an arcade racing simulation, outperforming the built-in game AI and reaching similar performance to experienced sim-racing drivers. A different approach is to implement the obstacle avoidance and overtaking tasks in a motion planning module, letting the controller solve only the tracking problem. In, the authors present a multi-layered graph-based planning architecture in which the trajectory is chosen considering a cost function representing the feasibility of the vehicle to follow the path segments of the graph built offline. The method has been tested in a real-world overtaking maneuver at low speeds in a simplified adversarial context.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this article, we present a framework for planning and control in head-to-head autonomous racing conditions evaluated during the Indy Autonomous Challenge events at the Indianapolis Motor Speedway (IMS) and Las Vegas Motor Speedway (LVMS) on a full-scale open-wheel racecar. It has been reached a top speed of 75 m/s in a single vehicle scenario, and a speed of 63 m/s during an overtaking maneuver. The authors participated in the competition as part of the TII EuroRacing team (TII-ER).

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In Section II we describe the vehicle model used for the optimization-based problems and introduce our model identification and validation approach. In Section III the lap time optimization strategy is presented before describing the motion forecasting and the Frenét-Frame-based method for the local planning. Constraints, cost function, and tuning strategies applied on the controller are reported and explained in Section IV. The experimental results are described in section V, while final conclusions and future works are discussed in Section VI.

<!-- chunk {"id": "body-0008", "role": "body", "section": "VEHICLE MODEL", "weight": 1.0} -->

The vehicle considered in this paper is a Dallara AV-21, shown in Figure 1, based on the Indy Lights chassis IL-15 with a 390hp engine. The suspensions and aerodynamics are adjusted for oval racing with an asymmetrical setup to exploit highly banked tracks.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Curvilinear Single Track Model", "weight": 1.0} -->

A single track dynamic model, shown in Figure 2, is used for the offline trajectory optimization problem and the NMPC. As, we use curvilinear/Frenét coordinates to describe the state. Therefore, global position and heading are not directly considered, but transformed to a state relative to the reference path.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A1 Equations of Motion", "weight": 1.0} -->

The vehicle state is given by $x = {\lbrack s;n;\mu;v_{x};v_{y};r;\delta;T;B\rbrack}$ and the input as $u = {\lbrack{\Delta\delta};{\DeltaT};{\DeltaB}\rbrack}$, where $s$, $n$ and $\mu$ are the progress along the path, the orthogonal deviation from the path and the local heading. Longitudinal $v_{x}$ and lateral $v_{y}$ velocities are considered as well as the yaw rate $r$. $\delta$, $T$ and $B$ are the steering angle, throttle command and brake command, which are included in the state. The control commands $\Delta\delta$, $\DeltaT$ and $\DeltaB$ are the derivatives of the inputs. Thus, the equations of motion are

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A1 Equations of Motion", "weight": 1.0} -->

where $\kappa{(s)}$ is the curvature at the progress $s$, $l_{f}$ and $l_{r}$ are the distances from the center of gravity to the front and rear wheels, $m$ is the mass and $I_{z}$ the moment of inertia. $F_{y_{f}}$, $F_{y_{r}}$ are the lateral tire forces at the front and rear wheels. $F_{x_{f}}$, $F_{x_{r}}$ are the longitudinal forces at front and rear axles.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A2 Tire Model", "weight": 1.0} -->

The tires effects are modeled using a simplified Pacejka Magic Formula with a combined slip correction. Beyond the usual macro-parameters $B$, $C$, $D$ and $E$, the lateral force offsets $Sv_{yi}$, $i \in {\lbrack f,r\rbrack}$, have been included resulting in

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A2 Tire Model", "weight": 1.0} -->

$Sh_{y_{i}}$ and $Sh_{v_{i}}$ are calculated using Pacejka micro-parameters related to horizontal shifts and variation of the lateral force shift considering the change in the tire load with respect to the reference vertical load and the camber angle.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A3 Longitudinal Forces", "weight": 1.0} -->

The front axle longitudinal forces are modeled as

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A3 Longitudinal Forces", "weight": 1.0} -->

where $C_{ro}$ is the rolling resistance. The braking force is represented as $C_{b_{f}}B$, with $C_{b_{f}}$ the maximum brake pedal pressure and $B \in {\lbrack 0,1\rbrack}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A3 Longitudinal Forces", "weight": 1.0} -->

Considering a rear wheels drive powertrain, the rear longitudinal force is modeled as

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A3 Longitudinal Forces", "weight": 1.0} -->

where $C_{m}$ is a linear engine coefficient and $T \in {\lbrack 0,1\rbrack}$. The turbo-charged combustion engine used on the research vehicle produces a force which is not linear in the whole usable regions since it depends on the engine rpm and gear. In order to represent this behavior, a scale factor $k_{s}$ varying on the speed has been applied to the upper bound constraint of the throttle command, thus $T \in {\lbrack 0,k_{s}\rbrack}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A3 Longitudinal Forces", "weight": 1.0} -->

Gear shifting effects are neglected as well as the gear command which is controlled separately and sent to the low-level controller when reaching the desired engine rpm.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Model Identification", "weight": 1.0} -->

Due to the lack of a steering wheel on the research vehicle, the traditional maneuvers used to collect data for vehicle model identification were not practical. We relied on information provided by the IAC organizers and tire and vehicle manufacturers, initially limiting our model to a static identification.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B1 Multi Body Simulation", "weight": 1.0} -->

Dymola, a physical modeling and simulation tool, has been used to model the AV-21 vehicle dynamics with the VeSyMA - Motorsports Library. The library provides solutions to model open-wheel race-cars components such as suspensions, aerodynamics, tires, and the powertrain. A highly detailed multi body simulation of the vehicle has been developed using the available information on the mechanical components such as the static parameters of the Indy Lights chassis and the engine map retrieved from a test bench. Unknown components or possible setups choices for the suspension have been estimated from IL-15 and IndyCar oval configurations, in particular the camber, caster and toe. The IMS and LVMS tracks have been modeled on Dymola by estimating the banking angle from sim-racing games. The resulting tracks have later been validated using the data from the on-board LiDAR sensors.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B2 Tire Model Identification", "weight": 1.0} -->

The tire maker provided a Magic Formula 6.2 model obtained using a test rig. However, the model could not be used to reproduce accurately enough the real tire behavior, which is highly affected by the tire-road grip, wear and suspension setup. A common strategy is to use the provided set of coefficients as a starting point and run an identification procedure to find parameters that better match the experimental data gathered on track.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B2 Tire Model Identification", "weight": 1.0} -->

In our work, the approach presented in has been applied using data obtained by simulating ramp steer maneuvers at different speeds and road conditions in our Dymola simulator.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B3 Validation", "weight": 1.0} -->

First experimental data on the real vehicle have been gathered using a simple Pure Pursuit path tracking algorithm at a maximum speed of 45 m/s at IMS and performing a light warm-up maneuver at 25 m/s in the long straights of the track. The warm-up maneuver consists of a series of $\pm$`<!-- -->`{=html}80deg steering wheel angle reference jumps on top of the lateral controller. An optical sensor has been mounted to get accurate measurements of speeds and angles in addition to the data obtained from the GNSS RTK-corrected system available on the Dallara AV-21. The tire model fitted on real data is depicted in Figure 3. In Figure 4, a comparison of the real and simulated data of the warm-up maneuver is shown. The first set of simplified Pacejka coefficients estimated from Dymola has been used during the tests and races at IMS and LVMS in the MPC described in Section IV.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Offline Global Trajectory Generation", "weight": 1.0} -->

A global path is generated as the main reference for the local planner. The resulting global path should consider the dynamic model, constraints on the inputs and tires, but should also give the possibility to incorporate rules related to track limits, such as keeping an inner or outer line.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Offline Global Trajectory Generation", "weight": 1.0} -->

Following, the solution is found by solving an optimal control problem using the dynamics transformed in the spatial domain $f_{s}\left( {x{(s)}},{u{(s)}} \right)$, with the progress $s$ as running variable. The continuous space model is discretized with a discretization distance $\Delta_{s}$ resulting in $x_{k + 1} = {f_{s}^{d}{(x_{k},u_{k})}} = {x_{k} + {\Delta_{s}f_{s}{(x_{k},u_{k})}}}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Offline Global Trajectory Generation", "weight": 1.0} -->

The cost function maximizes the progress rate $\overset{˙}{s}$ including a regularization term ${B{(x_{k})}} = {q_{B}\alpha_{r}^{2}}$ which penalizes the rear slip angle, and a regularizer on the input rates $u^{T}Ru$ where $R$ is a diagonal weight matrix. In summary, the overall cost function is defined as

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Offline Global Trajectory Generation", "weight": 1.0} -->

Combining the cost, model, and constraints the optimization problem is formulated as

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A Offline Global Trajectory Generation", "weight": 1.0} -->

where $X = {\lbrack x_{0},\ldots,x_{N}\rbrack}$, and $U = {\lbrack u_{0},\ldots,u_{N}\rbrack}$. $X_{ellipse}$ represents velocity dependent friction ellipse constraints similar to, and $X_{track}$ represents a track constraint on the lateral deviation $n$ ensuring that the trajectory stays on the track, considering additional side margin distances $n_{\text{left}}$, $n_{\text{right}}$ to the half length $L_{c}$ and half width $W_{c}$ of the car, and the left and right track width $N_{L/R}$ at a progress $s$,

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Offline Global Trajectory Generation", "weight": 1.0} -->

The physical inputs $a = {\lbrack\delta;T;B\rbrack}$ and their rate of change $u$ are constrained using box constraints $\mathbf{A}$ and $\mathbf{U}$. The problem is formulated in JuMP and solved using IPOPT.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Motion Forecasting", "weight": 1.0} -->

The motion forecasting module receives the position of the moving obstacles from the perception module, which processes the raw information of the sensors and keeps track of the obstacles in time. The module assigns to each obstacle a unique identifier $i$, a position in a Cartesian frame $x_{i},y_{i}$, and a covariance matrix of the position $\Sigma_{{xy},i}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B Motion Forecasting", "weight": 1.0} -->

Starting from the position of the $i$-th obstacle in a Cartesian frame ${x_{i}{(k)}},{y_{i}{(k)}}$ at step $k$, the position of the obstacle in the Frenét frame ${s_{i}{(k)}},{n_{i}{(k)}}$ is computed. Then, we define the model of the obstacle as

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B Motion Forecasting", "weight": 1.0} -->

Equation states that the longitudinal speed of the obstacle is constant, whereas equation indicates that the lateral displacement to the reference path is constant.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B Motion Forecasting", "weight": 1.0} -->

This simple model exploits the fact that the only obstacles in the track are other cars that will follow a racing line similar to the one that the ego car is following, and that the speed on an oval race track is almost constant. This insight is perfectly represented by modeling objects in a Frenét frame that uses the race line as the reference path, combined with our motion model.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B Motion Forecasting", "weight": 1.0} -->

From the equations the following state space model is derived

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Motion Forecasting", "weight": 1.0} -->

where $T_{s}$ is the sampling period of the filter, $\mathcal{X}_{i}{(k)}$ is the state of the model and $\mathcal{Y}_{i}{(k)}$ is the output.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B Motion Forecasting", "weight": 1.0} -->

Thus, at each time step for every obstacle, the Frenét frame measurements ${{\hat{s}}_{i}{(k)}},{{\hat{n}}_{i}{(k)}}$ are computed from ${{\hat{x}}_{i}{(k)}},{{\hat{y}}_{i}{(k)}}$. Using these measurements, the Kalman filter is updated with a prediction step, followed by a correction phase in which $\Sigma_{sn}$, the covariance matrix of the position converted in the Frenét frame, is used. The future trajectory of the obstacle ${\mathcal{O}_{i}{({k + \left. 1 \middle| k \right.})}},\ldots,{\mathcal{O}_{i}{({k + \left. m \middle| k \right.})}}$ is predicted by applying $m$ consecutive prediction steps.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-C Frenét-Frame-based Planner", "weight": 1.0} -->

The planner module implemented is an extended version of adding further considerations to the moving obstacles' collision check and racing scenarios.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-C1 Trajectories Generation", "weight": 1.0} -->

Given a race line computed offline, a Frenét frame is defined and used to generate multiple trajectories, which for example merge to the reference line, follow a vehicle or perform an overtake. Each single trajectory is defined as a combination of a lateral movement $n{(t)}$ and a longitudinal movement $s{(t)}$ at time $t$ with respect to the reference path.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-C1 Trajectories Generation", "weight": 1.0} -->

Given $N_{0}$, $N_{1}$ and the time interval $T$ between them, a quadratic polynomial is fully defined, and its coefficients can be calculated.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-C1 Trajectories Generation", "weight": 1.0} -->

This cost function penalizes the solutions with slow convergence to the reference, i.e. the ones that at the end of the trajectory are off from the reference path $n = 0$. Unlike what is proposed, we decided to keep $T$ constant for all the trajectories in the set in order to provide to the controller a trajectory with a fixed time horizon.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-C1 Trajectories Generation", "weight": 1.0} -->

A similar approach has been used for the longitudinal movement generating trajectories that bring the car to a desired velocity ${\overset{˙}{s}}_{n}$, while minimizing the jerk. As shown, quartic polynomials can be found to minimize the cost function

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-C1 Trajectories Generation", "weight": 1.0} -->

The set of lateral movements $\mathcal{T}_{\text{lat}}$ and longitudinal movements $\mathcal{T}_{\text{lon}}$ are then combined, resulting in a set $\mathcal{T} = {\mathcal{T}_{\text{lat}} \times \mathcal{T}_{\text{lon}}}$ of complete trajectories.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-C2 Trajectory Selection", "weight": 1.0} -->

All the trajectories $\tau_{i} \in \mathcal{T}$ are checked to evaluate whether they exceed the track boundaries or collide with an obstacle. We decided to perform these checks in the Frenét frame, to avoid converting the trajectories to a Cartesian frame. Furthermore, rather than doing the checks on the polynomials, we sampled each trajectory in a finite number of points. The sampling is done by fixing a time interval $\Deltat$ and evaluating the trajectory in ${\Deltat},{2\Deltat},\ldots,{M\Deltat}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-C2 Trajectory Selection", "weight": 1.0} -->

Given the track width in every point of the reference path, it is trivial to check if a trajectory ${\overline{\tau}}_{i}$ goes out of the track boundaries.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-C2 Trajectory Selection", "weight": 1.0} -->

From the Motion Forecasting module, an obstacle $\mathcal{O}_{j}$ is defined as a set of points.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-C2 Trajectory Selection", "weight": 1.0} -->

To account for the safety margins, a rectangle is built around every point of the predicted trajectory of the obstacle. A trajectory ${\overline{\tau}}_{i}$ collides with an obstacle $\mathcal{O}_{j}$ if ${\exists k} \in {\{ 1,\ldots,M\}}$ such that $(s_{\tau_{i},k},n_{\tau_{i},k})$ is inside the rectangle built around $(s_{o_{i},k},n_{o_{i},k})$. The described collision check treats the obstacle as a hard constraint for the planning algorithm. This approach could lead to undesired behavior in the scenarios in which an obstacle is blocking the race line, because the best trajectory will be the nearest one to the obstacle that does not collide with the obstacle itself. Following such a trajectory could bring the car to the edge of the obstacle safety margins. This can be critical if we consider the possible noise in the detection module.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-C2 Trajectory Selection", "weight": 1.0} -->

To overcome this issue, the collision check method is improved by adding a soft constraint. For each trajectory $\tau_{i}$, a collision coefficient $\gamma_{i} \in {\lbrack 0,1\rbrack}$ is computed, where $\gamma_{i} = 0$ indicates that the trajectory is not colliding with any obstacle, whereas $\gamma_{i} = 1$ indicates that the trajectory is violating the safety margins (hard constraint). Given this change, the cost becomes

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-C2 Trajectory Selection", "weight": 1.0} -->

To compute $\gamma_{i}$ we decided to exploit the Euclidean distance from the safety margin. For every trajectory $\tau_{i}$ the minimum distance $n_{i}$ from the safety margin is computed. Then, $\gamma_{i}$ is defined as

<!-- chunk {"id": "body-0049", "role": "body", "section": "III-C2 Trajectory Selection", "weight": 1.0} -->

where $\Delta_{soft} > 0$ is a parameter to enlarge or reduce the effect of the soft constraint. In Figure 5 a graphical representation of the soft constraint is given.

<!-- chunk {"id": "body-0050", "role": "body", "section": "III-C2 Trajectory Selection", "weight": 1.0} -->

The final step of our planner is to select the trajectory with the minimal cost which does stay inside the track margins.

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-C3 Following Mode", "weight": 1.0} -->

A following mode is implemented in the planner to keep a desired distance to the opponent when it is not allowed to perform an overtake by the rules of the competition.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-C3 Following Mode", "weight": 1.0} -->

where $\Delta_{\text{gap}} > 0$ is the current distance between the ego and the opponent car, and $k > 0$ is the gain of the controller. The computed desired speed is then used in for the longitudinal movement generation.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-A MPC Problem", "weight": 1.0} -->

In the control problem, the model is discretized in time $f_{t}^{d}{(x_{t},u_{t})}$ using a fourth-order Runge Kutta method.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-A MPC Problem", "weight": 1.0} -->

In addition to, the cost function includes path following weights $q_{n}$ and $q_{\mu}$, as well as a velocity tracking weight $q_{v}$ on the slack variable $s_{v,t}$ of the upper velocity constraint. Note that the reference path is given by the Frenét-planner.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-A MPC Problem", "weight": 1.0} -->

where $\hat{x}$ is the current curvilinear state, $\overline{v}$ the upper velocity bound and T is the prediction horizon. The main difference to is the more complex model and the integration with the Frenét-planner.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-A MPC Problem", "weight": 1.0} -->

The optimization problem is solved using a custom sequential quadratic programming framework, which uses HPIPM, a high-performance quadratic programming framework for MPC, and CppADCodeGen, a code generation automatic differentiation library.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-B Tuning", "weight": 1.0} -->

The regularization weights and constraints have been chosen in order to manage the trade-off between low path tracking error and input commands smoothness. Due to the uncertainty of the actuation performance and the model mismatch at high speeds, it has been decided to set the regularization term related to the steering wheel rate of change one order of magnitude higher than the value used in simulation and in other autonomous racing platforms in which the controller has been tested.

<!-- chunk {"id": "body-0058", "role": "body", "section": "RESULTS", "weight": 1.0} -->

The algorithms presented have been executed on a computing platform equipped with an 8 core Intel Xeon E 2278 GE, an NVIDIA RTX Quadro 8000 GPU, and 64 GB DDR4 RAM.

<!-- chunk {"id": "body-0059", "role": "body", "section": "RESULTS", "weight": 1.0} -->

The vehicle position was provided by a localization module based on an Extended Kalman Filter (EKF) using data produced by two GNSS RTK systems with Inertial Measurement Units (IMU) and wheel speed sensors. The perception module exploited the three solid-state LiDAR sensors, one frontal radar, and six cameras mounted on the racecar in order to estimate the obstacles and opponent position. Further details on the whole autonomous software stack will be presented in a future work.

<!-- chunk {"id": "body-0060", "role": "body", "section": "RESULTS", "weight": 1.0} -->

Both the Frenét-Frame-based planner and the motion forecasting module run at a frequency of 20Hz. The planner uses a time horizon of 3s, a sampling time of $\Deltat$ = 50ms, and lateral node sampling of 0.5m. The hard lateral safe distance is set to 3m, and the additional soft margin to 1.5m. The same $\Deltat$ is used in the MPC with a prediction horizon of $T = 50$ resulting in a time horizon of 2.5s. However, the MPC is executed at a frequency of 100Hz.

<!-- chunk {"id": "body-0061", "role": "body", "section": "RESULTS", "weight": 1.0} -->

Experimental results have been produced in different scenarios at Lucas Oil Raceway (LOR), IMS and LVMS.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-A High Speed Laps", "weight": 1.0} -->

The capability of the designed MPC to control the vehicle at high speeds has been tested during the time trial part of the IAC events. At the IMS track, TII-ER achieved the fastest time reaching an average speed of 62.5 m/s over a lap. The tracking performance at the LVMS is shown in Figure 6, where a top speed of 75.5 m/s has been reached. The maximum lateral error is 1m, whereas the RMS value is 0.5m. The heading error is maintained between 0.7deg and -1.0deg. A limited heading error despite a not negligible lateral error is the expected effect of the strategy applied to the MPC regularization terms explained in IV. The positive lateral error could be related to a not accurate force offset $Sh_{v_{i}}$ used in (II-A2), which should be investigated using the experimental data. Figure 7 presents the g-g diagram, showing that the racecar reached lateral accelerations up to 25 m/s^2^.

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-A High Speed Laps", "weight": 1.0} -->

In both events, the top speed has been limited by hardware and engine malfunctions. In particular, Figure 8 shows the case in which the research vehicle was not able to reach the target speed despite a fully saturated throttle command due to a detached cable in the powertrain wiring.

<!-- chunk {"id": "body-0064", "role": "body", "section": "V-C Head-to-Head Racing", "weight": 1.0} -->

A passing competition was held at LVMS where the racecars had to perform overtakes at increasingly higher velocities respecting the race format composed of four steps. The attacker should first reduce the gap from the defender, keep a longitudinal safety distance and overtake once reaching a passing zone. Then, the roles can be switched. If the new attacker succeeds in the four steps, a new round at higher speed is started. Figure 10 shows the performance of our solution during the last four rounds of the semifinal. Similar results of the time trial have been obtained with a higher lateral and heading error during the initial portion of the overtaking maneuvers. Figure 11 shows a frame sequence of the overtake at the highest speed achieved. It should be mentioned that the experimental data in the head-to-head scenario ends at a top speed of 63 m/s due to a wrong hard brake command triggered by a module separated from the motion planner and controller, causing the TII-ER vehicle to collide with the track borders.

<!-- chunk {"id": "body-0065", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

A multi-body model of the racecar has been implemented in simulation and used to examine and identify non negligible dynamics prior to the tests on track. This approach combined with a higher weight on the steering rate of change term demonstrated to be a successful strategy in making the controller robust enough at velocities of 75.5 m/s and accelerations of up to 25 m/s^2^, which were never explored before the final racing events. The planner has been capable of generating a path and velocity profile in order to follow the opponent, maintaining a defined distance, and producing a safe trajectory for active overtakes at speeds up to 63 m/s. Experimental data gathered during the tests will be used to improve the model identification and regularization terms, aiming to explore the dynamics and tire friction limit of the vehicle, as well as reduce the path tracking error. More challenging scenarios, such as racing in complex road courses and competing against multiple agents, will be explored in future applications. Further research will focus on new approaches for online trajectory generation to accomplish more aggressive maneuvers to adapt to racing conditions while keeping into consideration safety and computational limitations.
