## INTRODUCTION

In the literature, several approaches for motion planning and control have been developed and tested on high-performance autonomous vehicles. Hierarchical methods which exploit different levels of model complexity at different stages of the motion planner/controller are the current state of the art. The strength of this approach has been shown in, where a hierarchical method with a Nonlinear Model Predictive Control (NMPC) at its core was able to outperform a top driver on a formula student race car at lateral accelerations of over 20 m/s^2^.

For the task of multi-vehicle racing, the gap between human expert drivers and autonomous systems is still significant. This is also related to the fundamental challenges that must be solved to tackle this task, which include perception, rule-based interaction with other agents and the infrastructure, motion prediction, generation, and tracking of optimal trajectories for overtakes in unstructured environments. Most related works in this field focus on racing video games, simulations, and RC cars, and very limited work is done on full-scale race cars. In, the authors use an NMPC algorithm with a 4-wheel vehicle model with additional states for the nearest obstacle. The solution has been tested in simulation with a control rate of 25 Hz and a maximum speed of 40 m/s. For RC cars several groups have tackled the problem using game-theoretical planners, however, these methods focus on one-vs-one racing and do not scale well to full size racetracks. Several algorithms based on Deep Neural Networks (DNN) have also been proposed. A curriculum reinforcement learning-based method using an off-policy algorithm has been evaluated on Gran Turismo Sports, an arcade racing simulation, outperforming the built-in game AI and reaching similar performance to experienced sim-racing drivers. A different approach is to implement the obstacle avoidance and overtaking tasks in a motion planning module, letting the controller solve only the tracking problem. In, the authors present a multi-layered graph-based planning architecture in which the trajectory is chosen considering a cost function representing the feasibility of the vehicle to follow the path segments of the graph built offline. The method has been tested in a real-world overtaking maneuver at low speeds in a simplified adversarial context.

Figure 1: TII EuroRacing overtaking TUM Autonomous Motorsport during semifinal of the Autonomous Challenge at CES, Las Vegas Motor Speedway. ©Yev Z Photography

In this article, we present a framework for planning and control in head-to-head autonomous racing conditions evaluated during the Indy Autonomous Challenge (IAC^11^1[https://www.indyautonomouschallenge.com/](https://www.indyautonomouschallenge.com/)) events at the Indianapolis Motor Speedway (IMS) and Las Vegas Motor Speedway (LVMS) on a full-scale open-wheel racecar. It has been reached a top speed of 75 m/s in a single vehicle scenario, and a speed of 63 m/s during an overtaking maneuver. The authors participated in the competition as part of the TII EuroRacing team (TII-ER).

In Section II we describe the vehicle model used for the optimization-based problems and introduce our model identification and validation approach. In Section III the lap time optimization strategy is presented before describing the motion forecasting and the Frenét-Frame-based method for the local planning. Constraints, cost function, and tuning strategies applied on the controller are reported and explained in Section IV. The experimental results are described in section V, while final conclusions and future works are discussed in Section VI.

## VEHICLE MODEL

The vehicle considered in this paper is a Dallara AV-21, shown in Figure 1, based on the Indy Lights chassis IL-15 with a 390hp engine. The suspensions and aerodynamics are adjusted for oval racing with an asymmetrical setup to exploit highly banked tracks.

### II-A Curvilinear Single Track Model

A single track dynamic model, shown in Figure 2, is used for the offline trajectory optimization problem and the NMPC. As in, we use curvilinear/Frenét coordinates to describe the state. Therefore, global position and heading are not directly considered, but transformed to a state relative to the reference path.

### II-A1 Equations of Motion

The vehicle state is given by $x = {\lbrack s;n;\mu;v_{x};v_{y};r;\delta;T;B\rbrack}$ and the input as $u = {\lbrack{\Delta\delta};{\DeltaT};{\DeltaB}\rbrack}$, where $s$, $n$ and $\mu$ are the progress along the path, the orthogonal deviation from the path and the local heading. Longitudinal $v_{x}$ and lateral $v_{y}$ velocities are considered as well as the yaw rate $r$. $\delta$, $T$ and $B$ are the steering angle, throttle command and brake command, which are included in the state. The control commands $\Delta\delta$, $\DeltaT$ and $\DeltaB$ are the derivatives of the inputs. Thus, the equations of motion are

Figure 2: Dynamic single track vehicle model on curvilinear coordinates.

where $\kappa{(s)}$ is the curvature at the progress $s$, $l_{f}$ and $l_{r}$ are the distances from the center of gravity to the front and rear wheels, $m$ is the mass and $I_{z}$ the moment of inertia. $F_{y_{f}}$, $F_{y_{r}}$ are the lateral tire forces at the front and rear wheels. $F_{x_{f}}$, $F_{x_{r}}$ are the longitudinal forces at front and rear axles. $F_{b_{x}}$ and $F_{b_{y}}$ model the forces on the x and y-axis due to the road bank angle $\theta$, and are given by $F_{b_{x}} = {mg{\sin{(\theta)}}{\sin{(\mu)}}}$ and $F_{b_{y}} = {mg{\sin{(\theta)}}{\cos{(\mu)}}}$. $F_{d}$ represents the aerodynamic effects considering the air density $\rho$, the frontal area $S$ and the drag coefficient $C_{d}$,

### II-A2 Tire Model

The tires effects are modeled using a simplified Pacejka Magic Formula with a combined slip correction. Beyond the usual macro-parameters $B$, $C$, $D$ and $E$, the lateral force offsets $Sv_{yi}$, $i \in {\lbrack f,r\rbrack}$, have been included resulting in

where $\alpha_{y_{i}} = {\alpha_{i} + {Sh_{y_{i}}}}$ is the resulting slip angle obtained by applying a shift $Sh_{y_{i}}$ to the front slip angle $\alpha_{f}$ and the rear slip angle $\alpha_{r}$

$Sh_{y_{i}}$ and $Sh_{v_{i}}$ are calculated using Pacejka micro-parameters related to horizontal shifts and variation of the lateral force shift considering the change in the tire load with respect to the reference vertical load and the camber angle.

To consider the combined slip, we propose a combined slip weighting factor. Thus, the pure lateral forces $F_{y_{f},{lat}}$ and $F_{y_{r},{lat}}$ are weighted with $G_{y_{i}}$, such that we get the final forces, $F_{y_{f}} = {G_{y_{f}}F_{y_{f},{lat}}}$ and $F_{y_{r}} = {G_{y_{r}}F_{y_{r},{lat}}}$, with $G_{y_{i}}$ given by

where $F_{\max_{i}} = {D_{i}\epsilon_{i}}$ and $\epsilon_{i}$ is an ellipse shape parameter. Note that we clip the force fraction $F_{x_{i}}/F_{\max_{i}}$ at 0.98 to avoid singularity issues.

### II-A3 Longitudinal Forces

The front axle longitudinal forces are modeled as

where $C_{ro}$ is the rolling resistance. The braking force is represented as $C_{b_{f}}B$, with $C_{b_{f}}$ the maximum brake pedal pressure and $B \in {\lbrack 0,1\rbrack}$.

Considering a rear wheels drive powertrain, the rear longitudinal force is modeled as

where $C_{m}$ is a linear engine coefficient and $T \in {\lbrack 0,1\rbrack}$. The turbo-charged combustion engine used on the research vehicle produces a force which is not linear in the whole usable regions since it depends on the engine rpm and gear. In order to represent this behavior on, a scale factor $k_{s}$ varying on the speed has been applied to the upper bound constraint of the throttle command, thus $T \in {\lbrack 0,k_{s}\rbrack}$.

Gear shifting effects are neglected as well as the gear command which is controlled separately and sent to the low-level controller when reaching the desired engine rpm.

### II-B Model Identification

Due to the lack of a steering wheel on the research vehicle, the traditional maneuvers used to collect data for vehicle model identification were not practical. We relied on information provided by the IAC organizers and tire and vehicle manufacturers, initially limiting our model to a static identification.

### II-B1 Multi Body Simulation

Dymola, a physical modeling and simulation tool, has been used to model the AV-21 vehicle dynamics with the VeSyMA - Motorsports Library. The library provides solutions to model open-wheel race-cars components such as suspensions, aerodynamics, tires, and the powertrain. A highly detailed multi body simulation of the vehicle has been developed using the available information on the mechanical components such as the static parameters of the Indy Lights chassis and the engine map retrieved from a test bench. Unknown components or possible setups choices for the suspension have been estimated from IL-15 and IndyCar oval configurations, in particular the camber, caster and toe. The IMS and LVMS tracks have been modeled on Dymola by estimating the banking angle from sim-racing games. The resulting tracks have later been validated using the data from the on-board LiDAR sensors.

### II-B2 Tire Model Identification

The tire maker provided a Magic Formula 6.2 model obtained using a test rig. However, the model could not be used to reproduce accurately enough the real tire behavior, which is highly affected by the tire-road grip, wear and suspension setup. A common strategy is to use the provided set of coefficients as a starting point and run an identification procedure to find parameters that better match the experimental data gathered on track.

In our work, the approach presented in has been applied using data obtained by simulating ramp steer maneuvers at different speeds and road conditions in our Dymola simulator.

### II-B3 Validation

Figure 3: The estimated tire model, lateral force on the front (left) and rear (right) axles, over the real data gathered at LVMS at a speed of 62 m/s.

First experimental data on the real vehicle have been gathered using a simple Pure Pursuit path tracking algorithm at a maximum speed of 45 m/s at IMS and performing a light warm-up maneuver at 25 m/s in the long straights of the track. The warm-up maneuver consists of a series of $\pm$`<!-- -->`{=html}80deg steering wheel angle reference jumps on top of the lateral controller. An optical sensor has been mounted to get accurate measurements of speeds and angles in addition to the data obtained from the GNSS RTK-corrected system available on the Dallara AV-21. The tire model fitted on real data is depicted in Figure 3. In Figure 4, a comparison of the real and simulated data of the warm-up maneuver is shown. The first set of simplified Pacejka coefficients estimated from Dymola has been used during the tests and races at IMS and LVMS in the MPC described in Section IV.

Figure 4: Comparison of real and simulated data of the warm-up maneuver.

## MOTION PLANNING DESIGN

### III-A Offline Global Trajectory Generation

A global path is generated as the main reference for the local planner. The resulting global path should consider the dynamic model, constraints on the inputs and tires, but should also give the possibility to incorporate rules related to track limits, such as keeping an inner or outer line.

Following, the solution is found by solving an optimal control problem using the dynamics transformed in the spatial domain $f_{s}\left( {x{(s)}},{u{(s)}} \right)$, with the progress $s$ as running variable. The continuous space model is discretized with a discretization distance $\Delta_{s}$ resulting in $x_{k + 1} = {f_{s}^{d}{(x_{k},u_{k})}} = {x_{k} + {\Delta_{s}f_{s}{(x_{k},u_{k})}}}$.

The cost function maximizes the progress rate $\overset{˙}{s}$ including a regularization term ${B{(x_{k})}} = {q_{B}\alpha_{r}^{2}}$ which penalizes the rear slip angle, and a regularizer on the input rates $u^{T}Ru$ where $R$ is a diagonal weight matrix. In summary, the overall cost function is defined as

Combining the cost, model, and constraints the optimization problem is formulated as

where $X = {\lbrack x_{0},\ldots,x_{N}\rbrack}$, and $U = {\lbrack u_{0},\ldots,u_{N}\rbrack}$. $X_{ellipse}$ represents velocity dependent friction ellipse constraints similar to, and $X_{track}$ represents a track constraint on the lateral deviation $n$ ensuring that the trajectory stays on the track, considering additional side margin distances $n_{\text{left}}$, $n_{\text{right}}$ to the half length $L_{c}$ and half width $W_{c}$ of the car, and the left and right track width $N_{L/R}$ at a progress $s$,

The physical inputs $a = {\lbrack\delta;T;B\rbrack}$ and their rate of change $u$ are constrained using box constraints $\mathbf{A}$ and $\mathbf{U}$. The problem is formulated in JuMP and solved using IPOPT.

### III-B Motion Forecasting

The motion forecasting module receives the position of the moving obstacles from the perception module, which processes the raw information of the sensors and keeps track of the obstacles in time. The module assigns to each obstacle a unique identifier $i$, a position in a Cartesian frame $x_{i},y_{i}$, and a covariance matrix of the position $\Sigma_{{xy},i}$.

Starting from the position of the $i$-th obstacle in a Cartesian frame ${x_{i}{(k)}},{y_{i}{(k)}}$ at step $k$, the position of the obstacle in the Frenét frame ${s_{i}{(k)}},{n_{i}{(k)}}$ is computed. Then, we define the model of the obstacle as

Equation states that the longitudinal speed of the obstacle is constant, whereas equation indicates that the lateral displacement to the reference path is constant.

This simple model exploits the fact that the only obstacles in the track are other cars that will follow a racing line similar to the one that the ego car is following, and that the speed on an oval race track is almost constant. This insight is perfectly represented by modeling objects in a Frenét frame that uses the race line as the reference path, combined with our motion model.

From the equations the following state space model is derived

where $T_{s}$ is the sampling period of the filter, $\mathcal{X}_{i}{(k)}$ is the state of the model and $\mathcal{Y}_{i}{(k)}$ is the output.

Thus, at each time step for every obstacle, the Frenét frame measurements ${{\hat{s}}_{i}{(k)}},{{\hat{n}}_{i}{(k)}}$ are computed from ${{\hat{x}}_{i}{(k)}},{{\hat{y}}_{i}{(k)}}$. Using these measurements, the Kalman filter is updated with a prediction step, followed by a correction phase in which $\Sigma_{sn}$, the covariance matrix of the position converted in the Frenét frame, is used. The future trajectory of the obstacle ${\mathcal{O}_{i}{({k + \left. 1 \middle| k \right.})}},\ldots,{\mathcal{O}_{i}{({k + \left. m \middle| k \right.})}}$ is predicted by applying $m$ consecutive prediction steps.

### III-C Frenét-Frame-based Planner

The planner module implemented is an extended version of adding further considerations to the moving obstacles' collision check and racing scenarios.

### III-C1 Trajectories Generation

Given a race line computed offline, a Frenét frame is defined and used to generate multiple trajectories, which for example merge to the reference line, follow a vehicle or perform an overtake. Each single trajectory is defined as a combination of a lateral movement $n{(t)}$ and a longitudinal movement $s{(t)}$ at time $t$ with respect to the reference path.

Starting from the lateral movements, let $N_{0} = {\lbrack n_{0},{\overset{˙}{n}}_{0},{\overset{¨}{n}}_{0}\rbrack}$ be the start state and $N_{1} = {\lbrack n_{1},{\overset{˙}{n}}_{1},{\overset{¨}{n}}_{1}\rbrack}$ be the end state. As we want to move parallel to the reference line, we generate the set of lateral movements by changing $n_{1}$ in an interval $\lbrack n_{\text{min}},n_{\text{max}}\rbrack$ and set ${\overset{˙}{n}}_{1} = {\overset{¨}{n}}_{1} = 0$. Given $N_{0}$, $N_{1}$ and the time interval $T$ between them, a quadratic polynomial is fully defined, and its coefficients can be calculated. For each lateral movement, we then assign a cost based on the following cost function:

This cost function penalizes the solutions with slow convergence to the reference, i.e. the ones that at the end of the trajectory are off from the reference path $n = 0$. Unlike what is proposed in, we decided to keep $T$ constant for all the trajectories in the set in order to provide to the controller a trajectory with a fixed time horizon.

A similar approach has been used for the longitudinal movement generating trajectories that bring the car to a desired velocity ${\overset{˙}{s}}_{n}$, while minimizing the jerk. As shown in, quartic polynomials can be found to minimize the cost function

for a given start state $S_{0} = {\lbrack s_{0},{\overset{˙}{s}}_{0},{\overset{¨}{s}}_{0}\rbrack}$ at $t_{0}$ and $\lbrack{\overset{˙}{s}}_{1},{\overset{¨}{s}}_{1}\rbrack$ of the end state $S_{1}$ at some $t_{1} = {t_{0} + T}$. This means that we can generate a set of optimal longitudinal trajectories by varying the end constraints ${\overset{˙}{s}}_{1} = {{\overset{˙}{s}}_{n} + {\Delta\overset{˙}{s}}}$ and $T$.

The set of lateral movements $\mathcal{T}_{\text{lat}}$ and longitudinal movements $\mathcal{T}_{\text{lon}}$ are then combined, resulting in a set $\mathcal{T} = {\mathcal{T}_{\text{lat}} \times \mathcal{T}_{\text{lon}}}$ of complete trajectories.

### III-C2 Trajectory Selection

All the trajectories $\tau_{i} \in \mathcal{T}$ are checked to evaluate whether they exceed the track boundaries or collide with an obstacle. We decided to perform these checks in the Frenét frame, to avoid converting the trajectories to a Cartesian frame. Furthermore, rather than doing the checks on the polynomials, we sampled each trajectory in a finite number of points. The sampling is done by fixing a time interval $\Deltat$ and evaluating the trajectory in ${\Deltat},{2\Deltat},\ldots,{M\Deltat}$. Thus, the trajectory is converted to a set of points, where each point is associated with a time instant:

Given the track width in every point of the reference path, it is trivial to check if a trajectory ${\overline{\tau}}_{i}$ goes out of the track boundaries.

From the Motion Forecasting module, an obstacle $\mathcal{O}_{j}$ is defined as a set of points. Each point is associated with a time instant:

To account for the safety margins, a rectangle is built around every point of the predicted trajectory of the obstacle. A trajectory ${\overline{\tau}}_{i}$ collides with an obstacle $\mathcal{O}_{j}$ if ${\exists k} \in {\{ 1,\ldots,M\}}$ such that $(s_{\tau_{i},k},n_{\tau_{i},k})$ is inside the rectangle built around $(s_{o_{i},k},n_{o_{i},k})$. The described collision check treats the obstacle as a hard constraint for the planning algorithm. This approach could lead to undesired behavior in the scenarios in which an obstacle is blocking the race line, because the best trajectory will be the nearest one to the obstacle that does not collide with the obstacle itself. Following such a trajectory could bring the car to the edge of the obstacle safety margins. This can be critical if we consider the possible noise in the detection module. To overcome this issue, the collision check method is improved by adding a soft constraint. For each trajectory $\tau_{i}$, a collision coefficient $\gamma_{i} \in {\lbrack 0,1\rbrack}$ is computed, where $\gamma_{i} = 0$ indicates that the trajectory is not colliding with any obstacle, whereas $\gamma_{i} = 1$ indicates that the trajectory is violating the safety margins (hard constraint). Given this change, the cost becomes

with ${k_{\text{lat}},k_{\text{lon}},k_{\text{soft}}} > 0$.

To compute $\gamma_{i}$ we decided to exploit the Euclidean distance from the safety margin. For every trajectory $\tau_{i}$ the minimum distance $n_{i}$ from the safety margin is computed. Then, $\gamma_{i}$ is defined as

where $\Delta_{soft} > 0$ is a parameter to enlarge or reduce the effect of the soft constraint. In Figure 5 a graphical representation of the soft constraint is given.

Figure 5: Graphical representation of the collision coefficient as defined in. The black rectangle indicates the safety margin from the obstacle (hard constraint).

The final step of our planner is to select the trajectory with the minimal cost which does stay inside the track margins.

### III-C3 Following Mode

A following mode is implemented in the planner to keep a desired distance to the opponent when it is not allowed to perform an overtake by the rules of the competition. Differently from, given the position ${\mathbf{P}}_{\text{opp}} = {\lbrack s_{\text{opp}},n_{\text{opp}}\rbrack}$ and speed ${\overset{˙}{s}}_{\text{opp}}$ of the car to keep the distance from and the desired distance $\Delta_{\text{des}}$, the desired speed of the ego car ${\overset{˙}{s}}_{\text{des}}$ is regulated by a simple proportional controller:

where $\Delta_{\text{gap}} > 0$ is the current distance between the ego and the opponent car, and $k > 0$ is the gain of the controller. The computed desired speed is then used in for the longitudinal movement generation.

## MODEL PREDICTIVE CONTROL DESIGN

### IV-A MPC Problem

In the control problem, the model is discretized in time $f_{t}^{d}{(x_{t},u_{t})}$ using a fourth-order Runge Kutta method. As in, the MPC cost function combines the progress optimization with the regularization terms in order to penalize the rate of change of the physical inputs and rear slip angle:

In addition to, the cost function includes path following weights $q_{n}$ and $q_{\mu}$, as well as a velocity tracking weight $q_{v}$ on the slack variable $s_{v,t}$ of the upper velocity constraint. Note that the reference path is given by the Frenét-planner.

The MPC problem is formulated as

where $\hat{x}$ is the current curvilinear state, $\overline{v}$ the upper velocity bound and T is the prediction horizon. The main difference to is the more complex model and the integration with the Frenét-planner.

The optimization problem is solved using a custom sequential quadratic programming framework, which uses HPIPM, a high-performance quadratic programming framework for MPC, and CppADCodeGen, a code generation automatic differentiation library.

### IV-B Tuning

The regularization weights and constraints have been chosen in order to manage the trade-off between low path tracking error and input commands smoothness. Due to the uncertainty of the actuation performance and the model mismatch at high speeds, it has been decided to set the regularization term related to the steering wheel rate of change one order of magnitude higher than the value used in simulation and in other autonomous racing platforms in which the controller has been tested.

## RESULTS

The algorithms presented have been executed on a computing platform equipped with an 8 core Intel Xeon E 2278 GE, an NVIDIA RTX Quadro 8000 GPU, and 64 GB DDR4 RAM.

The vehicle position was provided by a localization module based on an Extended Kalman Filter (EKF) using data produced by two GNSS RTK systems with Inertial Measurement Units (IMU) and wheel speed sensors. The perception module exploited the three solid-state LiDAR sensors, one frontal radar, and six cameras mounted on the racecar in order to estimate the obstacles and opponent position. Further details on the whole autonomous software stack will be presented in a future work.

Both the Frenét-Frame-based planner and the motion forecasting module run at a frequency of 20Hz. The planner uses a time horizon of 3s, a sampling time of $\Deltat$ = 50ms, and lateral node sampling of 0.5m. The hard lateral safe distance is set to 3m, and the additional soft margin to 1.5m. The same $\Deltat$ is used in the MPC with a prediction horizon of $T = 50$ resulting in a time horizon of 2.5s. However, the MPC is executed at a frequency of 100Hz.

Experimental results have been produced in different scenarios at Lucas Oil Raceway (LOR), IMS and LVMS.

Figure 6: Experimental results for path tracking during high speed laps. See https://youtu.be/ERTffn3IpIs?t=2013 for the time trial laps at LVMS.

### V-A High Speed Laps

The capability of the designed MPC to control the vehicle at high speeds has been tested during the time trial part of the IAC events. At the IMS track, TII-ER achieved the fastest time reaching an average speed of 62.5 m/s over a lap. The tracking performance at the LVMS is shown in Figure 6, where a top speed of 75.5 m/s has been reached. The maximum lateral error is 1m, whereas the RMS value is 0.5m. The heading error is maintained between 0.7deg and -1.0deg. A limited heading error despite a not negligible lateral error is the expected effect of the strategy applied to the MPC regularization terms explained in IV. The positive lateral error could be related to a not accurate force offset $Sh_{v_{i}}$ used in (II-A2), which should be investigated using the experimental data. Figure 7 presents the g-g diagram, showing that the racecar reached lateral accelerations up to 25 m/s^2^.

Figure 7: The g-g diagram of the fastest lap at LVMS.

In both events, the top speed has been limited by hardware and engine malfunctions. In particular, Figure 8 shows the case in which the research vehicle was not able to reach the target speed despite a fully saturated throttle command due to a detached cable in the powertrain wiring.

Figure 8: From Figure 6: powertrain issue during the high speed laps. A top speed of 75.5 m/s has been reached instead of the target speed of 77.7 m/s.

### V-B Static Obstacle Avoidance

Figure 9 depicts a scenario in which static obstacles have been added to the LOR track. The AV-21 racecar was able to safely avoid the obstacles at a velocity of 34 m/s. The safe sensor range for the LiDAR-based detection was set at 60m. Thus, the planner received the obstacle position 1.7s before the potential collision.

Figure 9: Static obstacles test at LOR. See https://youtu.be/LIzb-_8vrI8 for a video of the test.

Figure 10: Experimental results for path tracking during the head-to-head race. The four steps are depicted with different colors. Closing the gap (red). Following mode (yellow). Overtake (green). Defending (blue). See https://youtu.be/ERTffn3IpIs?t=10469 for a video of the complete match.

Figure 11: Frame sequence during the overtake at 63 m/s. The solid blue line is the planner trajectory. The dashed green line is the motion prediction of the opponent.

### V-C Head-to-Head Racing

A passing competition was held at LVMS where the racecars had to perform overtakes at increasingly higher velocities respecting the race format composed of four steps. The attacker should first reduce the gap from the defender, keep a longitudinal safety distance and overtake once reaching a passing zone. Then, the roles can be switched. If the new attacker succeeds in the four steps, a new round at higher speed is started. Figure 10 shows the performance of our solution during the last four rounds of the semifinal. Similar results of the time trial have been obtained with a higher lateral and heading error during the initial portion of the overtaking maneuvers. Figure 11 shows a frame sequence of the overtake at the highest speed achieved. It should be mentioned that the experimental data in the head-to-head scenario ends at a top speed of 63 m/s due to a wrong hard brake command triggered by a module separated from the motion planner and controller, causing the TII-ER vehicle to collide with the track borders.

## CONCLUSIONS

A multi-body model of the racecar has been implemented in simulation and used to examine and identify non negligible dynamics prior to the tests on track. This approach combined with a higher weight on the steering rate of change term demonstrated to be a successful strategy in making the controller robust enough at velocities of 75.5 m/s and accelerations of up to 25 m/s^2^, which were never explored before the final racing events. The planner has been capable of generating a path and velocity profile in order to follow the opponent, maintaining a defined distance, and producing a safe trajectory for active overtakes at speeds up to 63 m/s. Experimental data gathered during the tests will be used to improve the model identification and regularization terms, aiming to explore the dynamics and tire friction limit of the vehicle, as well as reduce the path tracking error. More challenging scenarios, such as racing in complex road courses and competing against multiple agents, will be explored in future applications. Further research will focus on new approaches for online trajectory generation to accomplish more aggressive maneuvers to adapt to racing conditions while keeping into consideration safety and computational limitations.
