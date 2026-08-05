<!-- arxiv-full-text:v1 {"arxiv_id": "2010.10190", "source": "ar5iv"} -->

## INTRODUCTION

Applications where autonomous ground vehicles (AGVs) closely navigate with humans in complex environments require the AGV to safely avoid static and moving obstacles while making progress towards its goal. Motion planning and control for AGVs are typically addressed as two independent problems. In particular, the motion planner generates a collision-free path and the motion controller tracks such a path by directly commanding the AGV's actuators. Our method combines both motion planning and control in one module, relying on constrained optimisation techniques, to generate kinematically feasible local trajectories with fast replanning cycles. More specifically, we rely on a Model Predictive Controller (MPC) to compute an optimal control command for the controlled system, which directly incorporates the predicted intentions of dynamic obstacles. Consequently, it reacts in advance to smoothly avoid moving obstacles. We propose a practical reformulation of the Model Predictive Contouring Control ([[MPCC]](#id7.7.id7)) approach, namely, a Local Model Predictive Contouring Control ([[LMPCC]](#id3.3.id3)) approach, suitable for real-time collision-free navigation of AGVs in complex environments with several agents. Our design is fully implemented on board of the robot including localization and environment perception, i.e., detection of static obstacles and pedestrians. Our design runs in real time thanks to its lightweight implementation. The method relies on an open-source solver and will be released with this paper as a ROS module. Our method can be adapted to other robot morphologies, such as cars.

Figure 1: The faculty corridor was the scenario used to evaluate the capabilities of our method to avoid dynamic obstacles.

### I-A Related Work

Collision avoidance in static and dynamic environments can be achieved via reactive methods, such as time-varying artificial potential fields, the dynamic window, social forces and velocity obstacles. Although these approaches work well in low speed scenarios, or scenarios of low complexity, they produce highly reactive behaviours. More complex and predictive behaviour can be achieved by employing a motion planner. Our method relies on model predictive control (MPC) to obtain smooth collision-free trajectories that optimize a desired performance index, incorporate the physical constraints of the robot and the predicted behavior of the obstacles.

Due to the complexity of the motion planning problem, path planning and path following were usually considered as two separate problems. Many applications of MPC for path-following control are found in the literature, e.g.,. These methods assume the availability of a collision-free smooth path to follow. In contrast, we use MPC for local motion planning and control in the presence of static and dynamic obstacles.

Several approaches exist for integrated path following and control for dynamic environments. These include: employing a set of motion primitives and optimizing the control commands to execute them and offline computation of tracking error bounds via reachability analysis that ensures a safety region around the robot for online planning. These approaches, however, do not allow to incorporate the predicted intentions of the dynamic obstacles and consequently, can lead to reactive behaviors. To overcome the latter issue, proposed the model predictive contouring control (MPCC) that allows to explicitly penalize the deviation from the path (in terms of contouring and lateral errors) and include additional constraints. Later, designed a MPC for path following within a stable handling envelope and an environmental envelope. While is tailored to automotive applications without dynamic obstacles, MPCC has been employed to handle static and dynamic obstacles in structured driving scenarios. There, static collision constraints were formulated as limits on the reference path and thus limited to on-the-road driving scenarios. The previous approaches do not account for the interaction effects between the agents and may fail in crowded scenarios, a problem known as the freezing robot problem (FRP). Interaction Gaussian Processes (IGP) can be used to model each individual's path. The interactions are modeled with a nonlinear potential function. The resulting distribution, however, is intractable, and sampling processes are required to approximate a solution, which requires high computational power and is only real-time for a limited number of agents. Learning-based approaches address this issue by learning the collision-avoidance strategy directly from offline simulation data, or the complex interaction model from raw sensor readings. Yet, both methods learn a reactive collision avoidance policy and do not account for the kinodynamic constraints of the robot.

Without explicitly modeling interaction, we propose a method for local motion planning, which is real-time, incorporates the robot constraints and optimizes over a prediction horizon. Our approach relies on MPCC and extends it to mobile robots operating in unstructured environments. Similar to, among others, we employ polyhedral approximations of the free space, which can provide larger convex regions than safety bubbles.

### I-B Contribution

We build, with the following contributions to make the design applicable to mobile robots navigating in unstructured environments with humans: A static obstacle avoidance strategy that explicitly constrains the robot's positions along the prediction horizon to a polyhedral approximation of the collision-free area around the robot.

A closed-form bound to conservatively approximate collision avoidance constraints that arise from ellipsoidal moving obstacles.

A fully integrated MPCC approach that runs in real-time on-board of the robot and with on-board perception.

We present experimental results with a mobile robot navigating in indoor environments among static and moving obstacles and compare them with three state-of-art planners, namely the dynamic window, a classical MPC for tracking and a socially-aware motion planner. Finally, to illustrate the generality of the proposed MPCC framework, we present results with a simulated car.

## PRELIMINARIES

### II-A Robot description

Let $B$ denote an AGV on the plane $W = {\mathbb{R}}^{2}$. The AGV dynamics are described by the discrete-time nonlinear system where ${\mathbf{z}}{(t)}$ and ${\mathbf{u}}{(t)}$ are the state and the input of the robot, respectively, at time $t \geq 0$^11^1In the remainder of the paper we omit the time dependency when it is clear from the context.. For the case of our mobile robot we consider the state to be equal to the configuration, that is, ${{\mathbf{z}}{(t)}} \in C = {{\mathbb{R}}^{2} \times S}$. For the case of a car (Sec. IV-E), the state space includes the speed of the car. The area occupied by the robot at state $\mathbf{z}$ is denoted by $B{(\mathbf{z})}$. which is approximated by a union of $n_{c}$ circles, i.e., ${B{(\mathbf{z})}} \subseteq {\bigcup_{c \in {\{ 1,\ldots,n_{c}\}}}{B_{c}{(\mathbf{z})}}} \subset W$. The center of each circle, in the inertial frame, is given by ${\mathbf{p}} + {R_{B}^{W}{({\mathbf{z}})}{\mathbf{p}}_{c}^{B}}$. Where $\mathbf{p}$ is the position of the robot (extracted from $\mathbf{z}$), $R_{B}^{W}{({\mathbf{z}})}$ is the rotation matrix given by the orientation of the robot, and ${\mathbf{p}}_{c}^{B}$ is the center of circle $c$ expressed in the body frame.

### II-B Static obstacles

The static obstacle environment is captured in an occupancy grid map, where the area occupied by the static obstacles is denoted by $O^{\text{static}} \subset W$. In our experiments we consider both a global map, which is built a priori and used primarily for localization, and a local map from the current sensor readings. Therefore, the static map is continuously updated locally. Dynamic obstacles, such as people, that are recognized and tracked by the robot are removed from the static map and considered as moving obstacles.

### II-C Dynamic obstacles

Each moving obstacle $i$ is represented by an ellipse of area $A_{i} \subset W$, defined by its semi-major axis $a_{i}$, its semi-minor axes $b_{i}$, and a rotation matrix $R_{i}{(\psi)}$. We consider a set of moving obstacles $i \in I:={\{ 1,\ldots,n\}}$, where $n$ can vary over time. The area occupied by all moving obstacles at time instant $t$ is given by $O_{t}^{\text{dyn}} = {\bigcup_{i \in {\{ 1,\ldots,n\}}}{A_{i}{({\mathbf{z}_{i}{(t)}})}}}$, where ${\mathbf{z}}_{i}{(t)}$ denotes the state of moving obstacle $i$ at time $t$. In this work, and without a loss of generality, we assume a constant velocity model with Gaussian noise ${\omega_{o}{(t)}} \sim {\mathcal{N}{(0,{Q_{o}{(t)}})}}$ in acceleration, that is, ${{\overset{¨}{\mathbf{p}}}_{i}{(t)}} = {\omega_{i}{(t)}}$, where $\mathbf{p}_{i}{(t)}$ is the position of obstacle $i$ at time $t$. Given the measured position data of each obstacle, we estimate their future positions and uncertainties with a linear Kalman filter.

### II-D Global Reference Path

Consider that a reference path is available. In its simplest form, the reference path can be a straight line to the goal position or a straight line in the direction of preferred motion. But it could also be given by a global planner. We consider a global reference path $P$ consisting of a sequence of path segments connecting $M$ way-points ${\mathbf{p}}_{m}^{r} = {\lbrack x_{m}^{p},y_{m}^{p}\rbrack} \in W$ with $m \in M:={\{ 1,\ldots,M\}}$. For smoothness, we consider that each path segment $\varsigma_{m}{(\theta)}$ is defined by a cubic polynomial. We denote by $\theta$ a variable that (approximately) represents the traveled distance along the reference path, and which is described in more detail in Sec. III-C3. We do not require the reference to be collision free, therefore, the robot may have to deviate from it to avoid collisions.

### II-E Problem Formulation

The objective is to generate, for the robot, a collision free motion for $N$ time-steps in the future, while minimizing a cost function $J$ that includes a penalty for deviations from the reference path. This is formulated in the optimization problem Where $v_{k}$ is the forward velocity of the robot (for the mobile robot it is part of the input and for the car it is part of the state), $\tau$ is the time-step and $Z$ and $U$ are the set of admissible states and inputs, respectively. ${\mathbf{z}}_{1:N}$ and ${\mathbf{u}}_{0:{N - 1}}$ are the set of states and control inputs, respectively, over the prediction horizon $T_{\text{horizon}}$, which is divided into $N$ prediction steps. $\theta_{k}$ denotes the predicted progress along the reference path at time-step $k$. By solving the optimization problem, we obtain a locally optimal sequence of commands ${\lbrack{\mathbf{u}}_{t}^{\ast}\rbrack}_{t = 0}^{t = {N - 1}}$ to guide the robot along the reference path while avoiding collisions with static and moving obstacles.

## METHOD

The proposed method consists of the following steps, which are executed in every planning loop.

### 1

Search for a collision-free region in the updated static map centered on the robot and constrain the control problem such that the robot remains inside (Section III-A).

### 2

Predict the future positions of the dynamic obstacles and use the corrected bound to ensure dynamic collision avoidance (Section III-B).

### 3

Solve a modified MPCC formulation applicable to mobile robots (Section III-C).

### III-A Static collision avoidance

Given the static map of the environment, we compute a set of convex four-sided polygons in free space. This representation can provide larger collision-free areas compared with other approximations such as circles.

To obtain the set of convex regions at time $t$, we first shift the optimal trajectory computed at time $t - 1$, namely, ${\mathbf{q}}_{0:N} = {\lbrack{\mathbf{p}}_{1:{N|{t - 1}}}^{\ast},{\mathbf{q}}_{N}\rbrack}$, where ${\mathbf{q}}_{N}$ is a extrapolation of the last two points, that is, ${\mathbf{q}}_{N} = {{2{\mathbf{p}}_{N|{t - 1}}^{\ast}} - {\mathbf{p}}_{N - {1|{t - 1}}}^{\ast}}$.

Figure 2: Representation of the convex free space (orange squares) around each prediction step on the prediction horizon (purple line) with respect to the inflated static environment and the collision space of the dynamic obstacle (green ellipses) with respect to the vehicle representing discs (blue).

Then, for each point ${\mathbf{q}}_{k}$ ($k = {1,\ldots,N}$) we compute a convex region in free space, given by a set of four linear constraints ${c_{k}^{\text{stat}}{({\mathbf{p}}_{k})}} = {\bigcup_{l = 1}^{4}{c_{k}^{\text{stat},l}{({\mathbf{p}}_{k})}}}$. This region separates ${\mathbf{q}}_{k}$ from the closest obstacles. In our implementation we compute a rectangular region aligned with the orientation of the trajectory at ${\mathbf{q}}_{k}$, where each linear constraint is obtained by a search routine and reduced by the radius of the robot circles $r_{\text{disc}}$. Figure 2 shows the collision-free regions along the prediction horizon defined as yellow boxes. At prediction step $k$ for a robot with state $\mathbf{z}$ the resulting constraint for disc $j$ and polygon side $l$ is | | {{c^{\text{stat},l,j}{({\mathbf{z}})}} = {h^{l} -}} & {{{{\overset{\rightarrow}{n}}^{l} \cdot \left({{\mathbf{p}} - {R_{B}^{W}{({\mathbf{z}})}{\mathbf{p}}_{j}^{B}}} \right)} > 0},} | | | where $h^{l}$ and ${\overset{\rightarrow}{n}}^{l}$ define each side of the polygons.

### III-B Dynamic collision avoidance

Recall that each moving obstacle $i$ is represented by its position ${\mathbf{p}}_{i}{(t)}$ and an ellipse of semi-axis $a_{i}$ and $b_{i}$ and a rotation matrix $R_{i}{(\psi)}$. For each obstacle $i \in {\{ 1,\ldots,n\}}$, and prediction step $k$, we impose that each circle $j$ of the robot does not intersect with the elliptical area occupied by the obstacle. Omitting $i$ for simplicity, the inequality constraint on each disc of the robot with respect to the obstacles is where the distance between disc $j$ and the obstacle is separated into its $\Deltax^{j}$ and $\Deltay^{j}$ components (Fig. 2). The parameters $\alpha$ and $\beta$ are the semi-axes of an enlarged ellipse that includes the union of the original ellipse and the circle.

Figure 3: Safety boundary computation. The ellipsoid with semi-major axis and semi-minor axis, a and b respectively, is represented in green, the ellipsoid with axis enlarged by rdisc is represented in gray, the Minkowsky sum is represented in black and the ellipsoid enlarged by δ is represented in red.

While previous approaches approximated the Minkowski sum of the ellipse with the circle as an ellipse of semi-major $\alpha = {a + r_{\text{disc}}}$ and semi-minor axis $\beta = {b + r_{\text{disc}}}$, this assumption is not correct and collisions can still occur. We now describe how to compute the values for $\alpha$ and $\beta$ such that collision avoidance is guaranteed, represented by the larger in light red ellipsoid in Fig. 3.

Consider two ellipsoids $E_{1} = {{Diag}{({\frac{1}{a^{2}}\frac{1}{b^{2}}})}}$ and $E_{2} = {{Diag}\left( \frac{1}{{({a + \delta})}^{2}},\frac{1}{{({b + \delta})}^{2}} \right)}$. $E_{1}$ is an ellipsoid with $a$ and $b$ as semi-major and semi-minor axes, respectively. $E_{2}$ represents the ellipsoid $E_{1}$ enlarged by $\delta$ in both axis. The goal is to find the smallest ellipsoid that bounds the Minkowsky sum. This is equivalent to find the minimum value of $\delta$ such that the minimum distance between ellipsoid $E_{1}$ and $E_{2}$ is bigger than $r$^22^2Note we use $r$ instead of $r_{\text{disc}}$ in the reminder of the section to simplify the notation., the radius of the circle bounding the robot.

### Lemma 1

Let ${X^{\text{T}}A_{1}X} = 1$ and ${X^{\text{T}}A_{2}X} = 1$ be two quadratics in $R^{n}$. Iff the matrix $A_{1} - A_{2}$ is sign definite, then the square of the distance between the quadratic ${X^{\text{T}}A_{1}X} = 1$ and the quadratic ${X^{\text{T}}A_{2}X} = 1$ equals the minimal positive zero of the polynomial. where $D$ stands for the discriminant of the polynomial treated with respect to $\lambda$.

Considering $A_{1} = E_{1}$, $A_{2} = E_{2}$ and ${\{\delta,a,b,\}} \in R^{+}$ this ensures that $E_{1} - E_{2}$ is sign definite. Hence, we can apply Lemma 1. ‣ III-B Dynamic collision avoidance ‣ III METHOD ‣ Model Predictive Contouring Control for Collision Avoidance in Unstructured Dynamic Environments") to determine the polynomial $F{(z)}$ and its roots. For the two ellipsoids $E_{1}$ and $E_{2}$, the roots $\lambda$ of $F{(z)}$ are: The first two roots have multiplicity two. The minimum distance equation is the square root of the minimal positive zero of $F{(z)}$. Thus, the minimum enlargement factor is found by solving for the value of $\delta$ that satisfies ${{\min_{j}\lambda}{(j)}} = r^{2}$.

A closed form formula can be obtained by noting that the ${\min_{j}\lambda}{(j)}$ is achieved for the first root and solving this equation. Due to its length, it is not presented in this paper but can be found at ^33^3A Mathemathica notebook with the derivation of the bound and a Matlab script as example of its computation can be found in This value of semi-axis $\alpha = {a + \delta}$ and $\beta = {b + \delta}$ guarantee that the constraint ellipsoid entirely bounds the collision space.

### III-C Model Predictive Contouring Control

MPCC is a formulation specially tailored to path-following problems. This section presents how to modify the baseline method and make it applicable to mobile robots navigating in unstructured environments with on-board perception.

### III-C1 Progress on reference path

Eq. 2 approximates the evolution of the path parameter by the travelled distance of the robot. In each planning stage we initialize $\theta_{0}$. We find the closest path segment, denoted by $m$, and compute the value of $\theta_{0}$ via a line search in the neighborhood of the previously predicted path parameter.

### III-C2 Selecting the number of path segments

As detailed in Section II-D, the *global* reference is composed of $M$ path segments. To lower the computational load, only $\eta \leq M$ path segments are used to generate the *local* reference that is incorporated into the optimization problem. The number of path segments $\eta$ cannot be arbitrarily small, and there is a minimum number of segments to be selected to ensure the robot follows the reference path along a prediction horizon. The number of path segments $\eta$ in the local reference path is a function of the prediction horizon length, the individual path segment lengths, and the speed of the robot at each time instance. We select a conservative $\eta$ by considering the maximum longitudinal velocity $v_{\max}$ and imposing that the covered distance is lower than a lower bound of the travelled distance along the reference path, namely, where $m$ is the index of the closest path segment to the robot, $\tau$ is the length of the discretization steps along the horizon, and $s_{i}$ the length of each path segment.

### III-C3 Maintaining continuity over the local reference path

We concatenate the $\eta$ reference path segments into a differentiable local reference path ${\mathbf{L}}^{r}$, which will be tracked by the LMPCC, as follows where ${\sigma_{i, -}{(\theta_{k})}} = {1/{({1 + e^{{({\theta - {\sum_{j = m}^{i}s_{i}}})}/\epsilon}})}}$ and ${\sigma_{i, +}{(\theta_{k})}} = {1/{({1 + e^{{({{- \theta} + {\sum_{j = m}^{i - 1}s_{i}}})}/\epsilon}})}}$ are two sigmoid activation functions for each path segment and $\epsilon$ is a small design constant. This representation ensures a continuous representation of the local reference path needed to compute the solver gradients.

### III-C4 Cost function

For tracking of the reference path, a contour and a lag error are defined, see Fig. 4 and combined in an error vector ${\mathbf{e}}_{k}:={\lbrack{{\overset{\sim}{\epsilon}}^{c}{({\mathbf{z}}_{k},\theta_{k})}},{{\overset{\sim}{\epsilon}}^{l}{({\mathbf{z}}_{k},\theta_{k})}}\rbrack}^{\text{T}}$, with where $\phi{(\theta_{k})} = \arctan{(\partial y^{r}{(\theta_{k})}/\partial x^{r}{(\theta_{k})}}$ is the direction of the path. Consequently, the LMPCC tracking cost is where $Q_{\epsilon}$ is a design weight.

Figure 4: Approximated contour and lag errors on the path segment.

The solution which minimizes the quadratic tracking cost defined in Eq. 9 drives the robot towards the reference path. To make progress along the path we introduce a cost term that penalizes the deviation of the robot velocity $v_{k}$ from a reference velocity $v_{\text{ref}}$, i.e., ${J_{\text{speed}}{({\mathbf{z}}_{k},{\mathbf{u}}_{k})}} = {Q_{v}{({v_{\text{ref}} - v_{k}})}^{2}}$ with $Q_{v}$ a design weight. This reference velocity is a design parameter given by a higher-level planner and can vary across path reference segments.

To increase the clearance between the robot and moving obstacles, we introduce an additional cost term similar to a potential function, where $Q_{R}$ is a design weight, and $\Deltax_{k}$, $\Deltay_{k}$ represent the components of the distance from the robot to the dynamic obstacles. A small value $\gamma \geq 0$ is introduced for numerical stability. Eq. 10 adds clearance with respect to obstacles and renders the method more robust to localization uncertainties.

Additionally, we penalize the inputs with ${J_{\text{input}}{({\mathbf{z}}_{k},\theta_{k})}} = {{\mathbf{u}}_{k}^{T}Q_{u}{\mathbf{u}}_{k}}$, where $Q_{u}$ is a design weight.

The [[LMPCC]](#id3.3.id3) control problem is then given by a receding horizon nonconvex optimization, formally, where the stage cost is ${J{(\mathbf{z}_{k},\mathbf{u}_{k},\theta_{k})}}:={{J_{\text{tracking}}{({\mathbf{z}}_{k},\theta_{k})}} + {J_{\text{speed}}{({\mathbf{z}}_{k},{\mathbf{u}}_{k})}} + {J_{\text{repulsive}}{({\mathbf{z}}_{k})}} + {J_{\text{input}}{({\mathbf{u}}_{k})}}}$ and the terminal cost is ${J{({\mathbf{z}}_{N},\theta_{N})}}:={{J_{\text{tracking}}{({\mathbf{z}}_{N},\theta_{N})}} + {J_{\text{repulsive}}{({\mathbf{z}}_{N})}}}$. Eq. 11c and Eq. 11d are defined by Eq. 3 and Eq. 4, respectively. Algorithm 1 summarizes our method. Note that at each control iteration, cThe selection of $\text{iter}_{\max}$ is empirically based on the maximum number of iterations allowed within the sampling time of our system to guarantee real-time performance.

1:Given zinit, zgoal, Ostatic, O0dyn, and N 4: Estimate θ0 according to Section III-C1 6: Build ${\overline{\mathbf{p}}}^{r}{(\theta_{k})}$, k = 1, …, N, according to Eq. 7 7: Compute ckstat,j (pk) along q0: N 8: Get dynamic-obstacles predicted pose (Sec. III-B) 9: Solve the optimization problem of Eq. 11 Algorithm 1 Local Model Predictive Contouring Control

## RESULTS

This section presents experimental and simulation results for three scenarios with a mobile robot. We evaluate different settings for the parameters in our planner (Section IV-B), as well as compare its performance in static (Section IV-C) and dynamic (Section IV-D) environments against state of art motion planners. A video demonstrating the results accompanies this paper.

### IV-A Experimental setup

### IV-A1 Hardware Setup

Our experimental platform is a fully autonomous Clearpath Jackal ground robot, for which we implemented on-board all the modules used for localization, perception, motion planning, and control. Our platform is equipped with an Intel i5 CPU@2.6GHz, which is used to run the localization and motion planning modules, a Lidar Velodyne for perception, and an Intel i7 NUC mini PC to run the pedestrian tracker.

### IV-A2 Software Setup

To build the global reference path we first define a series of waypoints and we construct a smooth global path by connecting the waypoints with a clothoid. We then sample intermediate waypoints from this global path and connect them with $3$rd order polynomials, which are then used to generate the local reference path.

The robot localizes with respect to a map of the environment, which is created before the experiments. For static collision avoidance the robot utilizes a map that is updated online with data from its sensors and we employ a set of rectangles to model the free space. Our search routine expands the sides of a vehicle-aligned rectangle simultaneously in the occupancy grid environment with steps of $\Delta^{\text{search}} = {0.05\text{m}}$, until either an occupied cell is found or the maximum search distance $\Delta_{\text{max}}^{\text{search}} = {2\text{m}}$ is reached. Once an expanding rectangle side is fixed as a result of an occupied cell, the rest of the rectangle sides are still expanded to search for the largest possible area. This computation runs in parallel to the LMPCC solver, in a different thread, and with the latest available information. Our experiments employ the open-source SPENCER Pedestrian tracker and 2d laser data for detection and tracking of dynamic obstacles. If a pedestrian is detected, it is removed from the static map and treated as a moving ellipse. Our simulations use the open-source ROS implementation of the Social Forces model for pedestrian simulation.

The LMPCC problem of Eq. 11 is nonconvex. Our planner solves this problem online in real time using ACADO and its C-code generation tool. We use a continuous-time kinematic unicycle motion model to describe the robot's kinematics. The model is then discretized directly in ACADO using a multiple-shooting method combined with a Gauss-Legendre integrator of order 4, no Hessian approximations, and a sampling time of 50 ms. We select qpOASES to solve the resulting QP problem and set a KKT tolerance of $10^{- 4}$ and a maximum of 10 iterations. If no feasible solution is found within the maximum number of iterations, then the robot decelerates. The planner computes a new solution in the next cycle. Based on our experience, this allowed to recover the feasibility of the planner quickly. Our motion planner is implemented in C++/ROS and will be released open source.

Figure 5: Experiment for evaluation of performance

### IV-B Parameter evaluation

To evaluate the performance of the planner we performed several experiments at different reference speeds, $v_{\text{ref}} \in {\{{1\text{m/s}},{1.25\text{m/s}},{1.5\text{m/s}}\}}$, and prediction-horizon lengths, $T_{\text{Horizon}} \in {\{{1\text{s}},{3\text{s}},{5\text{s}}\}}$. The robot follows a figure-8 path (red line in Figure 5-(a)) while avoiding two pedestrians (green ellipses) and staying within the collision-free area (yellow rectangles). We use one circle to represent the planned position of the robot (light blue circles). Each pedestrian is bounded by an ellipse of semi-axis 0.3 m and 0.2 m. The predicted positions of the pedestrians are represented by a green line. We align the semi-minor axis to the pedestrian walking direction. For this experiment we rely on a motion capture system to obtain the position of the obstacles and robot. Figure 6 shows the computation time to solve the optimization problem. For $v_{\text{ref}} \in {\{ 1,1.25,1.5\}}$ m/s and $T_{\text{Horizon}} \in {\{ 1,3\}}$ s the computation times are under 50 ms, which is lower than the cycle-time defined for the planner. But, for $T_{\text{Horizon}} = 5$ s the 99th percentile is above the 50ms, not respecting the real-time constraint. The cases in which the planner exceeds the sampling time of the system are the situations in which the pedestrians suddenly step in front of the robot or change their direction of motion, requiring the solver more iterations to find a feasible solution. If not all the constraints can be satisfied, our problem becomes infeasible, and no solution is found. In this case, we reduce the robot velocity, allowing the solver to recover the feasibility after few iterations. Table I summarizes the behavior of the planner in terms of clearance, that is, the distance from the border of the circle of the robot to the border of the ellipse defining the obstacles. It demonstrates that a short horizon leads to lower safety distances and more importantly, that our method was able to keep a safe clearance in most cases.

Based on these results, we selected a reference speed of 1.25 m/s and a horizon length of 3 s for the following experiments.

Figure 6: Computation time required to solve the LMPCC problem online for different velocity references and horizon lengths. The central mark indicates the median. The bottom and top edges of the box indicate the 25th and 75th percentiles, respectively. The red crosses represent the outliers.

Clearance Mean (1st percentile) [m] TABLE I: Clearance between the robot and the dynamic obstacles for different velocity references and horizon lengths.

### IV-C Static collision avoidance

In this experiment we compare the proposed planner with two baseline approaches: *A MPC tracking controller*. We minimize the deviation from positions on the reference path up to $1$ m ahead of the robot.

*The Dynamic Window (DW)*. We use the open-source ROS stack implementation. The DW method receives the next waypoint once the distance to the current waypoint is less than 1 m.

For this and the following experiment, we fully rely on the onboard localization and perception modules. A Velodyne Lidar is used to build and update a local map centered in the robot for static collision avoidance. The prebuilt offline map is only used for localization.

In this experiment the mobile robot navigates along a corridor while tracking a global reference path (red waypoints in Figure 7). When it encounters automatic doors, the robot must wait for them to open. When it encounters the obstacle located near the third upper waypoint from the left, which was not in the map, the robot must navigate around it. Figure 7 shows the results of this experiment. All the three approaches are able to follow the waypoints and interact with the automatic door. When they encounter the second obstacle the classical MPC design fails to proceed towards the next waypoint. The DW and the LMPCC approaches are able to complete the task. Both methods showed similar performance (e.g., the traveled distance was 30.59 m for our LMPCC and 30.61 m for the DW). The time to the goal was relatively higher for the DW (50 s) compared to the LMPCC (41 s). This difference is mainly due to the ability of the LMPCC to follow a reference velocity. In addition, we tested DW and LMPCC in a scenario where half of the first door does not open due to malfunction. In such scenario, the LMPCC was able to traverse around the broken door while the DW gets into a deadlock state due to the narrow opening. A video of the experiments accompanies the paper.

Figure 7: Static collision avoidance scenario. The red crosses depict the path to follow (waypoints) and the colored points are the laser scan data. The blue, green, and magenta lines represent the trajectory obtained with the LMPCC,the MPC tracking controller, and the Dynamic Window, respectively.

### IV-D Dynamic collision avoidance

Our simulations compare our planner with an additional baseline: *a socially-aware motion planner* named Collision Avoidance with Deep RL (CADRL). We employ the open-source ROS stack implementation. The CADRL method receives the same waypoints as the DW method.

### IV-D1 Simulation Results

We compare the performance of the MPCC planner with the DW and CADRL baselines in the presence of pedestrians. Figure 1 shows the setup of our experiment. To avoid the overlap of the static and dynamic collision constraints, the detected pedestrians are removed from the updated map used for static avoidance and modeled as ellipses with a constant velocity estimate. The global path, as described in Section IV-A, consists of a straight line along the corridor. The robot has to follow this path while avoiding collisions with several pedestrians moving in the same or opposite direction. In this experiment, we do not evaluate the MPC tracking controller since it was unable to complete the previous experiment. Aggregated results in Table II show that the LMPCC outperforms the other methods. It achieves a considerably lower failure rate, smaller traveling distances, and maintains larger safety distances to the pedestrians. Only for the four pedestrians case, the DW achieved larger mean clearance, but with larger standard deviation. By accounting for the predictions of the pedestrians, our method can react faster and thus generate safer motion plans. Table II also shows that the number of failures grows with the number of agents. Yet, our method can scale up to six pedestrians with low collision probability and perform real-time. For larger crowds our method would select the closer $6$ pedestrians.

## agents

Clearance Mean (1st percentile) [m]% failures (% collisions / % stuck) Traveled distance Mean (Std.) [m] TABLE II: Statistic results of minimum distance to the pedestrians (where clearance is defined as the border to border distance), traveling distance and percentage of failures obtained for 100 random test cases of the dynamic collision avoidance experiment for n ∈ {2, 4, 6} agents. The pedestrians follow the social forces model.

### IV-D2 Experimental Results

We use the previous setup to compare the LMPCC and DW methods on a real scenario with two pedestrians. We do not test the CADRL method because the current open-source implementation does not allow static collision avoidance for unconstrained scenarios such as the faculty corridor depicted in Figure 8. Figure 8 shows one representative run of our method (top) and the DW (bottom). We observe that the proposed method reacts in advance to avoid the pedestrians, resulting in a larger clearance distance. In contrast, the DW reacts late to avoid the pedestrian, which has to avoid the robot himself actively. Our proposed method was able to navigate safely in all of our experiments with static and two pedestrians.

### IV-E Applicability to an autonomous car

To validate the applicability of our method to more complex robot models, we have performed a simulation experiment with a kinematic bicycle model of an autonomous car.

Figure 8: Dynamic collision avoidance scenario. The red crosses represent the global path to follow (waypoints). The blue and magenta lines represent the trajectory executed by our LMPCC (top) and by the Dynamic Window (bottom), respectively. The trajectories of the two pedestrians are represented by the green and magenta circles. In the lower case (dynamic window) the robot reacts late and the pedestrians must actively avoid it.

The planner commands the acceleration and front steering. The car follows a global reference path while staying within the road boundaries (i.e., the obstacle-free region) and avoiding moving obstacles (such as a simulated cyclist proceeding in the direction of the car and a pedestrian crossing the road in front of the car). The accompanying video shows the results where the autonomous vehicle successfully avoids the moving obstacles, while staying within the road limits. We refer the reader to for more details and results.

## CONCLUSIONS & FUTURE WORK

This paper proposed a local planning approach based on Model Predictive Contouring Control (MPCC) to safely navigate a mobile robot in dynamic, unstructured environments. Our local MPCC relies on an upper bound of the Minkowski sum of a circle and an ellipse to safely avoid dynamic obstacles and a set of convex regions in free space to avoid static obstacles. We compared our design with three baseline approaches (classical MPC, Dynamic Window, and CADRL). The experimental results demonstrate that our method outperforms the baselines in static and dynamic environments. Moreover, the light implementation of our design shows the scalability of our method up to six agents and allowed us to run all algorithms on-board. Finally, we showed the applicability of our design to more complex robots by testing the design in simulation using the model of an autonomous car. As future work, we intend to expand our approach for crowded scenarios, by accounting for the interaction effects between the robot and the other agents.
