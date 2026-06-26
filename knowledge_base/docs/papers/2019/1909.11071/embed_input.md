<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Dynamic Landing of an Autonomous Quadrotor on a Moving Platform in Turbulent Wind Conditions

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous landing on a moving platform presents unique challenges for multirotor vehicles, including the need to accurately localize the platform, fast trajectory planning, and precise/robust control. Previous works studied this problem but most lack explicit consideration of the wind disturbance, which typically leads to slow descents onto the platform. This work presents a fully autonomous vision-based system that addresses these limitations by tightly coupling the localization, planning, and control, thereby enabling fast and accurate landing on a moving platform. The platform's position, orientation, and velocity are estimated by an extended Kalman filter using simulated GPS measurements when the quadrotor-platform distance is large, and by a visual fiducial system when the platform is nearby. The landing trajectory is computed online using receding horizon control and is followed by a boundary layer sliding controller that provides tracking performance guarantees in the presence of unknown, but bounded, disturbances. To improve the performance, the characteristics of the turbulent conditions are accounted for in the controller. The landing trajectory is fast, direct, and does not require hovering over the platform, as is typical of most state-of-the-art approaches. Simulations and hardware experiments are presented to validate the robustness of the approach.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Autonomous unmanned aerial vehicles (UAVs) are becoming more and more popular in industry for their flexibility and fast deployment, and have demonstrated their usefulness in applications such as aerial photography for topology and agriculture, search and rescue operations, and mapping. The large recent growth in online shopping has also attracted interest in reducing package shipment time and costs, and UAVs provide an efficient alternative to delivery trucks. However, their payload and flight time is limited, so several researchers have investigated using a truck-drone delivery system. The UAVs in current truck-drone delivery methods can only take off and land when the truck is stopped visiting a customer node, which has substantial synchronization costs. Thus, autonomous landing on a moving truck is a promising research direction. This work presents a system capable of landing a quadrotor on a moving platform, even in the presence of turbulent wind. We demonstrate a boundary layer sliding controller (BLSC) which takes into account these conditions, a planner with changing objectives that allows a fast maneuver, and a vision-based extended Kalman filter (EKF) to estimate the moving platform's state.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The UAV's state estimator currently uses a motion capture system, but the important information in the maneuver we demonstrate (the relative position of the UAV and the moving platform) is estimated onboard by the quadrotor using a vision system.

<!-- chunk {"id": "body-0005", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Autonomous UAV landing has been investigated by several researchers. Ref. landed a drone on a static kayak in a reservoir with mild wind and water ripple conditions, but the image processing was done off-board and the landing time was close to 1 min. Ref. developed a system capable of landing a UAV on a moving platform with PID control, an EKF estimator, and an AprilTag visual fiducial bundle. However, the computation was also done off-board, and there was no relative wind present: the platform's speed was just 0.18m/s and the tests were done indoors. Ref. demonstrated a quadrotor landing on a moving platform using only onboard sensing and computation, but the environment was not turbulent due to the tests being indoors and the platform was moving relatively slowly at 1.2m/s. Furthermore, besides two cameras, a distance sensor was required to estimate the UAV-platform relative pose. Ref. demonstrated an autonomous landing of a quadrotor on a car moving at 14m/s by detecting an AprilTag on its roof. A proportional navigation-based guidance law was used for the approach phase, and a PID controller for the landing phase, with no disturbance rejection considerations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

The landing maneuver consisted of acquiring the tag while hovering, and the descent was initiated once the quadrotor stabilized over it. Additionally, the quadrotor used was large and had a broad sensor suite, including a downward-facing camera, a three-axis gimballed camera to track the target, and an inertial navigation system. Furthermore, besides the ground vehicle's GPS coordinates, the quadrotor also used the ground vehicle's IMU data to improve its estimation of the landing platform's state. Ref. also demonstrated an outdoors landing, but the landing platform's speed was only 0.5m/s and the landing maneuver took 12--20 s to complete. Moreover, the ground vehicle's wheel encoders data was used to estimate its state. Ref. used model predictive control (MPC) to land a quadrotor on a moving ship. Both the UAV and the ship collaborated to reach their goal. The waves were modeled as sinusoidal, but the wind disturbances considered were not turbulent -- this approach only compensated the effects caused by a steady-state wind. Furthermore, the vehicle needed to hover above the platform for at least 5 s, and the ship was simulated.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

A simulated boat landing was also carried out, where the platform's state was estimated fusing GPS and visual measurements. This work incorporated a velocity feed-forward term to the controller to catch the platform, but its only consideration of external wind was an offset of the hovering position to ensure the target was inside the field of view of the downwards-facing camera, and the landing maneuver lasted 24 s. Ref. developed an adaptive controller to track a ground vehicle with only relative position data from ArUco tags, and tested it in outdoor experiments at 5.6m/s. But this approach only considered disturbances due to ground effect, and the landing maneuver needed 20 s for tracking and 10 s for descent.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

In summary, most current approaches for quadrotor landing on moving platforms involve hovering above the platform for a period of time to visually acquire it, which is then followed by a relatively slow descent. In contrast, our approach investigates a direct trajectory to the landing platform, which has the possible advantages of providing faster landings and enabling several UAVs to approach the platform at the same time from different directions (improving the utilization of this limited resource). Additionally, most of current approaches do not make special considerations to reject the turbulent wind present near the target vehicle, and thus safety in challenging conditions cannot be guaranteed.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

This paper demonstrates a vision-based system capable of dynamic landing (i.e., the multirotor does not need to hover above the vehicle before descending) which also accounts for the turbulent conditions that would be present near a rapidly-moving ground vehicle. The resulting framework allows thus a maneuver that will be crucial for efficient truck-drone delivery systems. The contributions of this paper are as follows: Demonstration of a boundary layer sliding controller to incorporate and compensate for turbulence based on a model of the conditions near the landing platform.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

An algorithm for computing fast, vision-based dynamic landing maneuvers, is demonstrated both in simulation and hardware experiments that include challenging steady/turbulent wind conditions.

<!-- chunk {"id": "body-0011", "role": "body", "section": "SYSTEM OVERVIEW", "weight": 1.0} -->

This work addresses the current limitations of landing on a moving platform: 1) using optimization-based trajectory generation to enable dynamic landing; and 2) using robust control to explicitly compensate for turbulent wind conditions. The system that achieves this is comprised of several components, described in this section and shown in Fig. 2.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Finite State Machine", "weight": 1.0} -->

The quadrotor's behavior is determined by a finite state machine (FSM) comprised of four states: Stand By: This is the initial state of the quadrotor, which consists of taking off and hovering at a predefined altitude above the starting point. The FSM then transitions to Search mode.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Finite State Machine", "weight": 1.0} -->

Search: The quadrotor uses simulated GPS coordinates of the unmanned ground vehicle (UGV) ---as explained in Section II-D--- to predict a rendezvous location and flies there. When the front-facing camera detects the landing platform as described in Section II-E, the state automatically switches to Landing.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Finite State Machine", "weight": 1.0} -->

Landing: In this mode, the quadrotor approaches the target following a direct trajectory towards it. When the distance and relative velocity UAV-UGV are below threshold values, the quadrotor switches to the End mode. If the last detection happened more than 0.8s ago, the mode returns to Search.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Finite State Machine", "weight": 1.0} -->

End: motors are stopped, maneuver is finished.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Trajectory Planning: Model Predictive Control", "weight": 1.0} -->

The planner solves a convex optimization problem with changing objectives depending on the state of the FSM. In Search mode, the UAV-UGV rendezvous point is predicted by assuming a constant linear velocity and yaw rate for the UGV, and a constant velocity for the UAV. This position is then offset by a small distance backwards in the direction of the UGV to ensure target detection by the front-facing camera, and is used by the planner as the final position of the trajectory, while the final velocity is the UGV's. The time taken to reach the UGV is minimized, to reduce delivery turnarounds. In Landing mode, the planner initially minimizes the jerk to obtain a trajectory which ensures adequate tag acquisition. As the UAV approaches the target, the effect of disturbances increases so the planner minimizes the time spent in the turbulent area. The final position of the planned trajectory is the vertical tag's position (offset a few cm backwards) and predicted ahead (by an amount that depends on the computation time) assuming constant linear/angular velocities. The final velocity of the trajectory is set to match the UGV's.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Trajectory Planning: Model Predictive Control", "weight": 1.0} -->

The minimum jerk approach produces smooth trajectories and has a long heritage for planning quadrotor paths. The trajectory is re-planned using an MPC approach every time a new estimate of the platform's position is obtained.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-B Trajectory Planning: Model Predictive Control", "weight": 1.0} -->

| | | | | $x{\lbrack 0\rbrack}$ | ${= x_{0}},{{x{\lbrack N\rbrack}} = x_{f}}$ | | | | | $\text{for~}t$ | $= {0\ldotsN}$ | | | where $N$ is the timestep when the quadrotor has to reach the final state $x_{f}$, $\ell$ is a quadratic cost function, $\overline{u}$ is the open-loop control input (the jerk of the trajectory), $d$ is the UAV-tag distance, $x$ is the position, velocity, and acceleration of the UAV, $A$ and $B$ are, respectively, the state and input matrices for a triple integrator, and $a$ is the subvector of $x$ representing the acceleration.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-B Trajectory Planning: Model Predictive Control", "weight": 1.0} -->

Note that we can plan using this linear model for a nonlinear system because the nonlinear dynamics of the quadrotor are canceled by the ancillary controller, as explained next.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-C Ancillary Controller: Boundary Layer Sliding Controller", "weight": 1.0} -->

While MPC has been used extensively in industry, the control of systems with nonlinear dynamics requires expensive optimization. Sliding control has proven to be effective in quadrotors. This control strategy guarantees bounds on the tracking error and has been combined with MPC. In our approach, we derive a nonlinear ancillary controller using sliding control that models the disturbances found near the landing platform.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-C Ancillary Controller: Boundary Layer Sliding Controller", "weight": 1.0} -->

In quadrotors, the attitude dynamics are much faster than the position dynamics, and thus control of both can be decoupled: the output of a controller is the setpoint for the other. The position and velocity controller is derived in this section to account for the turbulent wind present near the landing platform, and the attitude control is performed by a quaternion-based controller.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-C Ancillary Controller: Boundary Layer Sliding Controller", "weight": 1.0} -->

The following derives the BLSC. Define the manifold $S{(t)}$ by ${s = {\overset{˙}{\overset{\sim}{x}} + {\lambda\overset{\sim}{x}}} = 0},$ where $\overset{\sim}{x} = {x - x_{d}}$ and $\lambda > 0$. The objective of sliding control is to maintain $s = 0$ at all times. If the control action's frequency is high enough, zero tracking error is guaranteed. This high control action is impractical in many applications because of actuator limits and the excitation of unmodelled dynamics. An approach taken in is BLSC, where the control discontinuity is smoothed in a thin boundary layer of thickness $\Phi$: Consider a system whose dynamics can be expressed as where $d$ is the disturbance.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-C Ancillary Controller: Boundary Layer Sliding Controller", "weight": 1.0} -->

Then, the BLSC strategy is where ${sat}{(\cdot)}$ is the saturation function, $\hat{f}$ is the estimated acceleration caused by drag, and $K$ is determined by the uncertainty in the dynamics and the disturbance of the system. As noted before, we can plan in using linear MPC because of the cancellation of $f$ in and.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-C Ancillary Controller: Boundary Layer Sliding Controller", "weight": 1.0} -->

We generate turbulence using leaf blowers as shown in Figs. 1 and 5. The turbulent wind parameters are the mean ${\mathbf{v}}_{\mathbf{w}}$ and standard deviation $\sigma$ of the speed. Define ${\mathbf{V}} = {{\mathbf{v}} + {\mathbf{v}}_{\mathbf{w}}}$ where $\mathbf{v}$ is the quadrotor's speed. Then, $\mathbf{V}$ is the total wind speed relative to the UAV and $\hat{f}$ is ${\hat{f} = {\hat{c}\left. \parallel{\mathbf{V}}\parallel \right.V}},$ where $\hat{c}$ is the estimated drag coefficient of the quadrotor.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-C Ancillary Controller: Boundary Layer Sliding Controller", "weight": 1.0} -->

The quadrotor plans a trajectory to approach the UGV in the direction it is facing to match its speed, and thus is never outside the wind field generated by the leaf blowers during the landing maneuver. Therefore, it is reasonable to assume that this wind field is constant in the directions perpendicular to where the leaf blowers point to. The true acceleration caused by drag is where ${\mathbf{u}}_{\mathbf{w}}$ is a unit vector in the direction of the wind.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-C Ancillary Controller: Boundary Layer Sliding Controller", "weight": 1.0} -->

The variation of $b$ is very small for a UAV with constant weight. Therefore, $\beta = \left({b_{max}/b_{min}} \right)$ is approximately 1, where $b_{max}$ and $b_{min}$ are the maximum and minimum control gains respectively (or throttle gains in the context of quadrotors). Thus, $K$ is simplified as ${K = {\overline{F} + \eta}},$ where $\eta > 0$ is a constant in the sliding condition The larger the $\eta$, the faster the system will reach the sliding surface. Nevertheless, $K$ should only be as large as the disturbance magnitude requires to avoid a high-frequency control signal. $\overline{F}$ is where $\overset{\sim}{c} > 0$ is a bound on the absolute value of the drag coefficient error $|{c - \hat{c}}|$. By taking the sign that makes this coefficient larger, we have defined $K$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-C Ancillary Controller: Boundary Layer Sliding Controller", "weight": 1.0} -->

In our application, the quadrotor moves towards the generated wind and therefore this occurs when the $2\sigma$ is increasing the magnitude of ${\mathbf{v}}_{\mathbf{w}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-D Landing Platform Estimation: Extended Kalman Filter", "weight": 1.0} -->

To estimate the state of the moving platform, an extended Kalman filter (EKF) is used. This filtering algorithm minimizes the mean of the squared error and has demonstrated its efficacy in robot localization. The state vector of the platform is ${{\mathbf{x}}_{\mathbf{p}} = {\lbrack p_{x},p_{y},v_{p},\theta,\overset{˙}{\theta}\rbrack}^{\top}},$ where $p_{x},p_{y}$ are the 2D coordinates, $v_{p}$ is the magnitude of the velocity, $\theta$ is the orientation angle with respect to the $x$-axis, and $\overset{˙}{\theta}$ is the angular velocity. Since real-world roads are mostly horizontal and in particular our experiments were carried on completely flat surfaces, the velocity in the $z$-direction is not estimated.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-D Landing Platform Estimation: Extended Kalman Filter", "weight": 1.0} -->

The moving platform is modeled as a unicycle with dynamics where ${\mathbf{w}}{(t)}$ is the process noise, assumed to be a white Gaussian noise. We consider a constant linear and angular velocity, and the UGV dynamics are The measurement vector is ${\mathbf{z}}_{\mathbf{p}} = {\lbrack p_{x},p_{y},\theta\rbrack}^{\top}$, and when a measurement is received, the EKF approach is used to perform an update of the estimated state. The measurements are obtained in two ways. First, when the quadrotor is far from the platform (that is, in the Search state defined in Section II-A), these measurements are obtained by adding a white Gaussian noise to the ground truth pose of the vehicle (obtained from the motion capture data) to simulate inaccurate GPS measurements that a ground vehicle could provide to the UAV for the rendezvous. Note that receiving $\theta$ is not necessary to estimate the orientation of a moving platform because its motion could be used to infer that quantity.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-D Landing Platform Estimation: Extended Kalman Filter", "weight": 1.0} -->

Nevertheless, $\theta$ measurements are used in this work, which enables testing for static platform experiments. The update frequency is 2Hz, which is realistic for UAV applications. These first set of measurements are simply used to help the UAV locate the ground vehicle, but that information could be estimated without requiring a link between the two vehicles.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-D Landing Platform Estimation: Extended Kalman Filter", "weight": 1.0} -->

Second, and most importantly, when the quadrotor is near the ground vehicle and detects the onboard tag, we fuse both the simulated GPS and the visual detection measurements to estimate ${\mathbf{x}}_{\mathbf{p}}$. The vision-based detection is explained in the next subsection, and it provides a far more accurate estimate of the position and orientation of the tag/platform. The 2D positions $p_{x}$ and $p_{y}$ and the heading angle $\theta$ are then used to update the platform's state, and the estimated velocity $v_{p}$ is incorporated into the vector $x_{f}$ in to ensure the quadrotor matches the moving platform's speed at the landing point.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-E Visual detection: AprilTag visual fiducial system", "weight": 1.0} -->

When the UAV is relatively close to the platform, visual estimation provides more accurate UAV-UGV poses than GPS. We used the AprilTag visual fiducial system to obtain them, and a ROS wrapper based on AprilTag 2 to interface with the core detection algorithm. A tag bundle is a set of several coplanar tags used simultaneously by the visual fiducial system: the algorithm extracts the information of all of them to estimate a single "bundle pose". Thus, they are useful when accurate detection is required, which is the case in this paper. Additionally, by using tags of different sizes, detection at various distances is ensured. We used a tag bundle comprised of a 14$\times$`<!-- -->`{=html}14cm tag on top of a 5$\times$`<!-- -->`{=html}5cm tag. Despite the relatively small bundle size, it can be detected at a maximum distance of approximately 3.5m, and a minimum distance of about 5cm. The bundle can be seen in Fig. 5.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A Simulations", "weight": 1.0} -->

Due to the difficulty of accurately modeling the complex turbulent wind effects on a quadrotor, our simulations consider steady wind but serve to test our finite state machine, planner, controller, and estimator. For space constraints, simulation experiments are not analyzed here, but the video accompanying the paper (linked in the Supplementary Material Section) shows a landing simulation.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B Hardware", "weight": 1.0} -->

Static and moving platform landing tests were done (see Figs. 1 and 5), both of which had turbulent wind at the landing site from the leaf blowers. The quadrotor used for the hardware experiments (Fig. 5) weighs 0.564kg including the 1500mAh 3S battery. It is $36 \times 29$cm (approximately half the platform size) and its thrust-to-weight ratio is 1.75. The onboard computer is a Qualcomm Snapdragon Flight APQ8074, whose front-facing camera provides $640 \times 480$ black-and-white images at a rate of 30fps to the AprilTag detection module. Hover tests were carried out to determine $\hat{b}$. To measure the drag coefficient $\hat{c}$ and the bound on its error $\overset{\sim}{c}$, we performed tests with the quadrotor flying in front of a strong wind and the accurate pitch angle was obtained by the motion capture system. By balancing forces, the drag could be determined, yielding $\hat{c}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Hardware", "weight": 1.0} -->

Additionally, we used the IMU utils package to compute the Snapdragon's IMU accelerometer and gyroscope noise density and bias random walk. The Kalibr visual-inertial calibration toolbox then used this IMU intrinsic information to find the camera-IMU transform.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-C1 Experiment Setting", "weight": 1.0} -->

The first set of hardware experiments presents a static platform in front of an array of 5 leaf blowers, as shown in Fig. 5. The leaf blowers are set at two different heights and point to the negative $x$-direction. The platform is composed of a 60$\times$`<!-- -->`{=html}60cm horizontal plate and a 60$\times$`<!-- -->`{=html}30cm vertical plate, which has attached the tag bundle described in II-E.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-C1 Experiment Setting", "weight": 1.0} -->

The parameters $v_{w}$ and $\sigma$ of the turbulent wind were measured at distances $l$ from the vertical platform every $0.5$m until $l = 3.5$m, which is approximately the tag detection range. For every $l$, a measurement of the speed was taken every second for $60$s using a high-precision hot-wire anemometer. Fig. 5 shows the data obtained. Interestingly, at $l = 0.5$m, the mean speed decreases while the standard deviation increases to its maximum value. We believe this is due to the vortices caused when the flow traverses the vertical platform.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-C2 Results", "weight": 1.0} -->

First, we tested a standard BLSC that does not take into account the turbulent wind generated by the leaf blowers, that is, the factors $\hat{f}$ and $K$ only consider the drag generated by the quadrotor's speed relative to the ground. Fig. 6 shows the tracking and estimation performance obtained. The quadrotor starts at ${\mathbf{p}}_{\mathbf{q}} = {({- 3.5},2.0,1.3)}$m, and the platform is located at ${\mathbf{p}}_{\mathbf{p}} = {(1.1,{- 1.1},0.8)}$m. As expected, the tracking performance is poor, and the landing takes a long time: $27.2$s since the first tag detection, which occurs at $t_{d} = 3.3$s (indicated with a vertical dashed line). Also note that the platform's estimation improves after $t_{d}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-C2 Results", "weight": 1.0} -->

In the video, the covariance ellipses for the tag's 2D position can be seen, and decrease abruptly in size at $t_{d}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-C2 Results", "weight": 1.0} -->

Next, we used our BLSC with the same initial conditions as in Fig. 6 to compare its improvement. The results are shown in Fig. 8. It can be seen that the tracking is much better, and it only worsens slightly when the quadrotor is inside the wind field, after the time of the first tag detection $t = 2.5$s. The landing time is just $3.2$s (measured since the first tag detection) even in challenging conditions, which is 8.5 times faster compared to the standard BLSC.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-D1 Experiment Setting", "weight": 1.0} -->

To fully test our approach, we also performed landing experiments on a moving platform that is mounted on top of a dolly. The Clearpath Jackal was used as the ground vehicle that tows the landing platform (see Fig. 1) and carries two of the leaf blowers. This provided turbulent air at the landing pad even though the vehicles were not moving very quickly. The distance from the leaf blowers to the platform is such that this turbulent wind follows the same plot as Fig. 5.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-D2 Results", "weight": 1.0} -->

A standard BLSC was also tested first for this experiment setting. There was considerable tracking error and the quadrotor was not able to land on the platform before the vehicle arrived at the final point (see video linked in the Supplementary Material Section for details). The results obtained using our BLSC are shown in Fig. 8. The quadrotor starts at ${\mathbf{p}}_{\mathbf{q}} = {({- 1.5},2.7,0.9)}$m, and the UGV starts at ${\mathbf{p}}_{\mathbf{p}} = {({- 3.9},0.1,0.4)}$m. When the maneuver begins, the UGV is commanded to move at 1m/s and rotate to its right at a rate of 4^∘^/s. The tag is detected at $t_{d} = 4.7$s, and the landing time is $6.8s$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-D2 Results", "weight": 1.0} -->

Note that the quadrotor is at approximately $4m$ from the moving platform at $t_{d}$, a value larger than for the static experiment (1.5m).

<!-- chunk {"id": "body-0044", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

This paper developed a boundary layer sliding controller to allow a quadrotor to fly in challenging conditions, and demonstrated its effectiveness by performing fast landing experiments. Future work includes incorporating adaptation to allow for more varied flight conditions, and landing on the back of a pickup truck driving outdoors, to test this work's approach in a more realistic setting. This will additionally require visual-inertial odometry (VIO) for onboard-only state estimation.
