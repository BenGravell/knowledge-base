<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Model Predictive Trajectory Optimization and Tracking for On-Road Autonomous Vehicles

Topics include Autonomous driving, Model predictive control, Trajectory optimization, Trajectory tracking.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Combines trajectory optimization with a feedback-feedforward tracking controller for on-road autonomous vehicles. The main contribution is the coupling of model-predictive feedforward planning with a stability-oriented tracking design for dynamic-obstacle scenarios.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Motion planning for autonomous vehicles requires spatio-temporal motion plans (i.e. state trajectories) to account for dynamic obstacles. This requires a trajectory tracking control process which faithfully tracks planned trajectories. In this paper, a control scheme is presented which first optimizes a planned trajectory and then tracks the optimized trajectory using a feedback-feedforward controller. The feedforward element is calculated in a model predictive manner with a cost function focusing on driving performance. Stability of the error dynamic is then guaranteed by the design of the feedback-feedforward controller. The tracking performance of the control system is tested in a realistic simulated scenario where the control system must track an evasive lateral maneuver. The proposed controller performs well in simulation and can be easily adapted to different dynamic vehicle models. The uniqueness of the solution to the control synthesis eliminates any nondeterminism that could arise with switching between numerical solvers for the underlying mathematical program.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Autonomous vehicles often decompose the selection of steering, throttle, and braking control signals into a planning process which generates a feasible motion through the perceived scene. This is followed by a control process which executes a local trajectory tracking control policy robust to process noise and load disturbances. Motion planning algorithms for autonomous driving usually simplify the planning task by first planning a geometric path followed by planning a longitudinal velocity profile along the geometric path. Since all motion planning algorithms with approximate completeness guarantees have exponential complexity with respect to state dimension, this decomposition affords significant reduction in computational requirements and planning latency. The decomposition is inherited by the control system which generally has separate lateral and longitudinal control policies. The subtleties of designing controllers in this case have been well studied.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The downside to this decomposition is that it implicitly discards effective options available to the planner. For example, if a dynamic obstacle suddenly crosses the vehicle's path, a geometric planner will not reason about the motion of that object and will have to assume a fixed location, or neglect the dynamic obstacle completely; the subsequent longitudinal planner must find a safe option restricted to the selected geometric path. This motivates spatio-temporal motion planning that accounts for predicted states of dynamic obstacles. However, the prohibitive complexity of motion planning for high fidelity models forces motion planning modules to use simplified dynamic models with low dimensional continuous state spaces, sometimes further approximated by finite state models. This places a greater burden on the control process which must execute a trajectory tracking control policy that not only compensates for load disturbances and accounts for sensor noise, but has to account for model difference between the planner and the vehicle's dynamics.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

To address such issue, one approach attracting increasing attention is Model Predictive Control (MPC) which incorporates a sophisticated dynamic model to recursively optimize tracking errors over the reference trajectory. MPC approaches for trajectory tracking have been widely investigated for both autonomous driving and semi-autonomous driving cases. Furthermore, if the cost function can be proved as a Lyapunov function, stability of the nominal closed-loop system is guaranteed. However, the cost function for trajectory tracking of autonomous vehicles typically need to account for riding performance such as small yaw rate and smooth change of acceleration, which makes proof of the cost function as a Lyapunov function very difficult, even intractable.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

This paper discusses a particular control system design for trajectory tracking which utilizes a feedforward MPC to optimize the reference trajectory with respect to a cost function that does not need to be a Lyapunov function of the closed-loop error dynamic. The proposed feedforward MPC, discussed in Section III, is formulated as a strictly convex optimization problem (SCOP), which results in unique solutions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Then, a feedback-feedforward controller is proposed based on a time-varying Linear Quadratic Regulator (TVLQR), where the feedforward element and the nominal trajectory are obtained from the feedforward MPC. The reduced computational requirements to run a TVLQR allows the feedback loop to be run at higher frequency than the feedforward path. Moreover, stability of the error dynamic of the nominal system is ensured by carefully choosing coefficients of the cost function in the TVLQR.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Simulations results in Section IV suggest the approach produces satisfactory tracking results in realistic driving scenarios, and with computation times well within the sample rate of the controller. We conclude in Section V that this control system design is a promising approach worth further study including in our research teams repertoire of control systems to be tested on or experimental autonomous driving platform.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Trajectory Optimization", "weight": 1.0} -->

A reference trajectory, denoted as ${\hat{\mathcal{T}}}_{t}:={\{{\hat{\mu}}_{0},{\hat{\mu}}_{1},\ldots,{\hat{\mu}}_{N}\}}$ with $t \in {\mathbb{N}}$, published by the planner at instant $t$ is consists of $N + 1$ reference states to be reached at uniformly spaced time intervals of duration $\Deltat$. The trajectory optimization process is to generate a sequence of control-state pairs satisfying the dynamic model of the vehicle. We refer to the state sequence and the control sequence as the nominal trajectory and the feedforward term if the trajectory optimization problem is feasible. Given the initial state, the vehicle is expected to track the nominal trajectory without error using the feedforward control if no disturbances and model uncertainty appear. Fig. 1 shows the connections of the trajectory optimization to the motion planner and the feedback controller. Instead of the reference trajectory, the optimized nominal trajectory is used by the feedback controller to calculate tracking state-error and to generate the feedback term.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Trajectory Optimization", "weight": 1.0} -->

The feedforward control together with the feedback term formulates the control input that actuates the vehicle. The state of the vehicle and feedforward control are denoted $x$ and $u_{ff}$ respectively. When comparing states in $\hat{\mathcal{T}}$ and $\mathring{\tau}$ is required, we augment $\hat{\mu}$ to ${\mathbb{R}}^{\dim{(x)}}$ with the values of the augmented states set to the equilibrium point, and denote the augmented state as $\hat{x}$. Let $\hat{\tau} \triangleq {\lbrack{\hat{x}{(t)}^{T}},\ldots,{\hat{x}{({t + N})}^{T}}\rbrack}^{T}$ be the augmented vector of states from the reference trajectory. The trajectory optimization problem is defined,

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Trajectory Optimization", "weight": 1.0} -->

where $f_{ff}{( \cdot, \cdot )}$ is the feedforward model of the vehicle, $U_{ff}$ is the vector of all feedforward terms over the samples from $t$ to $t + N$. $\mathcal{X}$ and $\mathcal{U}$ are the state constraint set and the feedforward input constraint set, respectively.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Trajectory Optimization", "weight": 1.0} -->

While tracking performance requirements can imposed with an inequality constraint on error $\|{\hat{\tau} - \mathring{\tau}}\|$, this can make the optimization infeasible. Thus, we focus on formulating tracking performance in the cost function as a soft constraint. Detailed construction of the cost function (1a) and constraints (1b-d) to a strictly convex quadratic program will be discussed in the following two subsections.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Vehicle Dynamics", "weight": 1.0} -->

The trajectory optimization problem formulated in II-A relies on the equality constraint (1b) to predict future states and satisfying the differential constraints of the vehicle. The trajectory optimization estimates (1b) from the same dynamic model used in the feedback controller, which is defined as follows

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Vehicle Dynamics", "weight": 1.0} -->

where $s$, $y$, $\theta$ are the pose at the center point of the rear axle of the vehicle in an inertial coordinate system. $\delta$, $v$, $\alpha$, $L$ are the steering-wheel angle, the longitudinal speed, the longitudinal acceleration, and the wheel base of the vehicle, respectively. $\delta_{in}$ and $\alpha_{in}$ are the control input of steering angle and the control input of acceleration/deceleration, respectively. A first order inertial response is added to both steering control and acceleration/deceleration control to formulate the system lag, where $\lambda_{1} > 0$ and $\lambda_{2} > 0$ are response coefficients.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Vehicle Dynamics", "weight": 1.0} -->

Direct implementation of the nonlinear model in the optimization results in a non-convex problem making real-time trajectory optimization intractable. It can be easily verified that even the one-step quadratic cost ${x^{T}Qx} + {u_{ff}^{T}Ru_{ff}}$ with is non-convex in $u_{ff}$ with both $Q$ and $R$ positive definite. In order to obtain a convex cost in $U_{ff}$, an LTV model is used to approximate. The linearized discrete-time LTV equation of with $x \triangleq {\lbrack s,y,\theta,\delta,v,\alpha\rbrack}^{T}$ is given as follows.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Vehicle Dynamics", "weight": 1.0} -->

where $\beta \in {\lbrack 0,1\rbrack}$ is a weighting coefficient. The input matrix $B$ is time-invariant. Values of states in $A{(t)}$ are assigned using the corresponding states in $\hat{\tau}{(t)}$. Fig. 2 shows numerical forward simulation of the LTV model compared to.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-C Convexity of Quadratic Functions", "weight": 1.0} -->

In the interest of formulating as a SCOP, we focus on the quadratic programming formulations with strictly convex cost functions admitting unique solutions. Uniqueness of the optimal solution ensures that the optimized nominal trajectory is reproducible and solver-invariant^11^1within the resolution tolerance set by the numerical solver.. Quadratic programs are well understood and various numerical solvers are available. While the focus is on quadratic programs, the synthesis approach proposed in this paper is applicable to SCOPs with cost functions of different categories. For instance, a SCOP with self-concordant barrier functions available on the constraints can be solved by a generic interior point method.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-C Convexity of Quadratic Functions", "weight": 1.0} -->

The following is a brief review of some useful facts and also introduces some of the notation that will be used in subsequent sections. Throughout this work, let $\mathcal{S}_{+}^{n}$ (respectively, $\mathcal{S}_{+ +}^{n}$) be the set of positive semi-definite (respectively, positive definite) symmetric matrices in ${\mathbb{R}}^{n \times n}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Cost Function Construction", "weight": 1.0} -->

The dynamics of the LTV system over an $N$-step planning horizon is written compactly as

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Cost Function Construction", "weight": 1.0} -->

The idea of trajectory optimization is to construct a cost function to meet objectives leveraged by the motion planner and the feedback control system (refer to the connections in Fig. 1). For instance, the motion planner could have riding comfort as an objective and the feedback controller prefers slow changes over the nominal trajectory. It is observed that derivatives of control input are required in the objectives of optimization in addition to control input itself. Therefore, we focus on constructing the cost function of (4 ‣ II-C Convexity of Quadratic Functions ‣ II PROBLEM FORMULATION ‣ Model Predictive Trajectory Optimization and Tracking for On-Road Autonomous Vehicles")) that extends a generic MPC cost function with penalties on differentiation of control input in trajectory optimization. The difference matrix $E \in {\mathbb{R}}^{{{2N} \times 2}N}$ over the feedforward sequence $U_{ff}$ is as follows

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Cost Function Construction", "weight": 1.0} -->

then the change of the control sequence is represented as

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Cost Function Construction", "weight": 1.0} -->

Here we focus on various differences of control input since the changes of the state are encoded in the equations for the system dynamics. Given $R_{i} \in \mathcal{S}_{+ +}^{2N}$, we have

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Cost Function Construction", "weight": 1.0} -->

The cost function comprising system state and control input is constructed as follows

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Cost Function Construction", "weight": 1.0} -->

where $M \geq 0$ is the difference order of interest. $Q \in \mathcal{S}_{+ +}^{6{({N + 1})}}$ is the weight coefficient of trajectory tracking deviation. ${{R_{i} \in \mathcal{S}_{+ +}^{2N}},{0 \leq i \leq M}},$ is the weight coefficient of the $i$-th order control input. If $M$ is set to $0$, is equivalent to the cost function of an MPC scheme for tracking. In particular, we have the quadratic program of trajectory optimization as minimizing subject to dynamic constraints, (1c), and (1d). Furthermore, we assume that the constraint sets $\mathcal{U}$ and $\mathcal{X}$ are polyhedra formulated by half planes generated by linear inequalities.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Cost Function Construction", "weight": 1.0} -->

With the cost function designed in the form of, we have the following result on uniqueness.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Feedback and Feedforward Control", "weight": 1.0} -->

When a new reference trajectory $\hat{\mathcal{T}}$ is available from the motion planner, the trajectory optimization takes the reference trajectory to set up the SCOP with and (1c-d). The solution to the SCOP, $U_{ff}^{\ast}$, and the corresponding nominal trajectory together with a feedback controller form the feedback-feedforward control scheme. State update of the closed-loop system implementing the feedback-feedforward scheme is given as follows

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Feedback and Feedforward Control", "weight": 1.0} -->

The state feedback controller follows the scheme of TVLQR. First, the system is augmented to include the integral of tracking error.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Feedback and Feedforward Control", "weight": 1.0} -->

where ${U_{fb}{(t)}} = {\lbrack{u_{fb}^{T}{(t)}},\ldots,{u_{fb}^{T}{({{t + N} - 1})}}\rbrack}^{T}$. $\overline{Q} \in \mathcal{S}_{+}^{12}$, $\overline{R} \in \mathcal{S}_{+ +}^{2}$, $\overline{P} \in \mathcal{S}_{+ +}^{12}$. Closed-loop stability and disturbance rejection properties of the feedback system can be found. The trajectory optimization is called when a new trajectory from the motion planner is available. In general, the controller updates at a higher rate than the motion planner. Multiple samples in $U_{ff}$ are used in the feedback-feedforward scheme, which is different from solving a quadratic program per control step implemented in an MPC scheme.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Feedback and Feedforward Control", "weight": 1.0} -->

The TVLQR is responsible for disturbance rejection of the closed-loop system, which requires less computation resource.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Trajectory Optimization Results", "weight": 1.0} -->

A sample trajectory is used to test the trajectory optimization. The trajectory consists of states ${\lbrack s,y,\theta,v\rbrack}^{T}$ over a 5-second horizon. The update interval of the trajectory optimization is set to $0.1s$ with the optimization horizon set to $5s$. The cost function is designed to minimize a weighted norm of the tracking error, the feedforward input, and the rate of change of feedforward input. In particular, $Q = {\text{diag}{}}$, $R_{0} = {\text{diag}{(0.1,0.1)}}$, $R_{1} = {\text{diag}{}}$. The constraint set $\mathcal{U}$ is set as ${- 4.0} \leq \alpha_{in} \leq 2.5$, and ${- 0.1} \leq \delta_{in} \leq 0.1$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Trajectory Optimization Results", "weight": 1.0} -->

Using the state model with a 50 time-step horizon, the resulting quadratic program has 100 decision variables and 200 inequality constraints. The optimization problem is solved in MATLAB using $\mathbf{q}\mathbf{u}\mathbf{a}\mathbf{d}\mathbf{p}\mathbf{r}\mathbf{o}\mathbf{g}$ on a Windows laptop with an Intel Core i5 CPU at 2.50GHz in 43.65 milliseconds averaged over 150 tests.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Trajectory Optimization Results", "weight": 1.0} -->

The reference trajectory from the planner is piecewise constant in steering angle and velocity consisting of 5 piecewise constant segments. The reference velocity and steering angle over each sub-segment are constant and only change at the starting point of each sub-segment, denoted as blue dots in Fig. 3. Fig. 3 shows the optimized trajectory in the $s - y - v$ space, depicted as the green curve. It is observed that the velocity over the optimized trajectory is adjusted in order to track the s-y position in the reference trajectory.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Feedback-feedforward Performance", "weight": 1.0} -->

In order to test the effectiveness of the proposed feedforward-feedback approach for motion trajectory tracking, a test scenario is designed considering an evasion maneuver. The host vehicle in the scenario needs to change lane to avoid a pulled-over vehicle while keeping safe inter-vehicle distance to the car in the target lane. The relative position of vehicles in the simulation is sequentially depicted in Fig. 4.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Feedback-feedforward Performance", "weight": 1.0} -->

The reference trajectory is obtained from the motion planner that minimizes deviations to a desired velocity profile calculated using time-headway and speed limits with forward kinematic simulation. The first 15-second of the planned trajectory is saved and is used as the reference trajectory. The dashed grey line in Fig. 5 shows the estimated feedforward input derived from the reference trajectory using without the first order lag. Steep changes of steering angle and acceleration are observed during $t = 7$ and $t = 10$ where the host vehicle needs to adjust longitudinal velocity while changing to the adjacent lane. Parameters of the trajectory optimization are set as the same to IV-A. Parameters of the TVLQR feedback controller is set as $\overline{Q} = {{diag}{(10,5,10,1,10,{{1e} - 4},{{1e} - 4},0,0,0,0)}}$, $\overline{R} = {{diag}{}}$. The sampling interval of the TVLQR is set to $0.02s$ with the horizon set equal to the trajectory optimization horizon.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Feedback-feedforward Performance", "weight": 1.0} -->

The feedback-feedforward scheme is then tested on a nonlinear vehicle model that takes into account acceleration saturation of the powertrain, aero dynamics, and noises on steering and acceleration measurements.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Feedback-feedforward Performance", "weight": 1.0} -->

Fig. 3 shows the tracking result of the feedback-feedforward scheme in $s - y$ plane. The corresponding input generated for the closed-loop system is shown in Fig. 5 together with the feedforward term from the trajectory optimization. The feedforward term has been smoothed out during the evasion maneuver as the trajectory optimization takes into account i) change rates of the feedforward term, and ii) a vehicle model sharing the same state space as the feedback controller. Fig. 7 shows the tracking error over longitudinal position, lateral position, vehicle heading, and longitudinal velocity.

<!-- chunk {"id": "body-0038", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

This paper proposes a trajectory tracking control approach for autonomous vehicles based on a model predictive trajectory optimization to generate a feedforward control and a time varying linear quadratic regulator for feedback. Optimization of a reference trajectory is formulated as a strictly convex quadratic program by leveraging a linearization about the reference trajectory, polyhedral constraints, and a family of strictly convex quadratic cost functions. Additionally, the quadratic cost function is developed taking into account the rate of change of the feedforward input. A feedback-feedforward control scheme is proposed to actuate the vehicle by combining the optimized feedforward input and the feedback input generated by a TVLQR. The trajectory optimization and tracking scheme has been tested in simulation with an evasive maneuver. The proposed approach shows satisfactory tracking results in realistic driving scenarios, and with computation times well within the sample rate of the controller.
