## INTRODUCTION

In logistics, goods are commonly transported using articulated commercial vehicles, such as a tractor-semitrailer. During typical logistics driving scenarios, the vehicle not only drives forward through cities, industrial zones, and highways, but also reverses to load and unload the semitrailer at a dock. The introduction of autonomous vehicles into the logistics chain has the potential to improve efficiency and safety and address driver shortages. A crucial element is a trajectory planner that needs to plan vehicle maneuvers in the aforementioned driving scenarios while avoiding collisions, offering predictable driving to other road users, and maintaining passenger and payload comfort.

Trajectory planning algorithms for passenger cars have been extensively researched. However, developing a planner for a tractor-semitrailer poses additional challenges. Cars in Europe measure 2.5 to 5.5 meters in length and 1.6 to 2.0 meters in width, while European tractor-semitrailer combinations typically are 16.5 meters long and 2.55 meters wide. Furthermore, the semitrailer follows a different path than the tractor due to the articulation point, which is called offtracking. Moreover, articulated vehicles are unstable while driving in reverse, risking jackknifing. The effect of vehicle dimensions and offtracking is illustrated in Fig. 1, where a car and a tractor-semitrailer negotiate a 90° degree turn on a typical urban street. The car remains in its lane, while the tractor's front extends into the opposite lane, and the semitrailer's inner wheel exits the road on the inside. The example illustrates the need to explicitly consider the dimensions of the vehicle and the offtracking of the semitrailer during trajectory planning.

Figure 1: A car and a tractor-semitrailer navigate a 90° turn with a 15-meter radius on a dual-lane road, where each lane is 3.5 meters wide. The car and tractor follow the center of the right lane with the center of the rear axle. The swept path illustrates the covered area by the vehicles when driving.

Any autonomous vehicle should behave in a predictable way. Other road users expect that an autonomous vehicle generally follows the middle of the lane at approximately the speed limit. We assume that a local geometric road model is available, which is a simplified, high-resolution map of the road geometry (e.g., lanes) including speed limits within the vehicle's immediate vicinity. We rely on HD-maps to create the road model but it could also be constructed from onboard sensor data (e.g., LiDAR, camera) and vehicle-to-everything (V2X) communication. A trajectory planner can leverage the information from the local road model to plan a trajectory that the tractor-semitrailer must follow and match the expectations of the other road users. The trajectory should be:

safe, i.e. avoid collisions with static and dynamic obstacles and prevent rollover of the vehicle,

comfortable for the passengers and payload,

efficient in terms of travel time.

These requirements can conflict. For example, a longer travel time may result from the vehicle slowing down to prevent rollover while cornering. Furthermore, the planner must generate trajectories that are kinematically and dynamically feasible for a tractor-semitrailer for both forward and backward motion (e.g., no instantaneous 90° turns).

A trajectory planner for an articulated commercial vehicle should be able to prioritize one or more vehicle anchor points based on the driving scenario, where vehicle anchor points are specific physical locations on the vehicle. For example, the semitrailer's rear-door position is most important during docking, the tractor's charging-port location is crucial when charging, and both the tractor and the semitrailer should remain close to the lane center during highway driving.

In this paper, we propose a trajectory planner that meets these requirements to plan a safe, comfortable, and efficient trajectory. The remainder of this paper is structured as follows. First, related work is discussed in Section II and Section III presents the necessary preliminaries. The approach itself is formulated in Section IV, followed by its application to a common logistics scenario in simulation and a first real-life test in Section V. Finally, conclusions and future work are provided in Section VI.

## RELATED WORK

A variety of vehicle trajectory planning approaches have been developed, including graph search, sampling-based methods, interpolation, and optimization. As noted in the introduction, a trajectory planner for tractor-semitrailers requires handling potentially conflicting objectives while ensuring that constraints related to safety and comfort are met. This renders graph-based, sampling, and interpolation methods unsuitable, while optimization-based motion planning techniques are particularly suitable for these requirements. These methods can also ensure the kinematic and dynamic feasibility of the trajectory through explicit use of vehicle model constraints.

Optimization-based methods developed for cars, such as, are generally not suitable for large articulated vehicles due to their size, offtracking, and jackknifing. Existing optimization-based approaches for articulated vehicles typically use either Cartesian or road-aligned (Frenet) coordinate frames, both illustrated in Fig. 2. The Cartesian frame is used by Bos et al. in a Model Predictive Control (MPC) approach, where the free space is decomposed into convex polyhedrons to constrain the tractor and semitrailer positions. The Cartesian frame enables straightforward obstacle representation using convex shapes, facilitating efficient obstacle avoidance constraints in an optimization problem. In contrast, the road-aligned frame allows a simple definition of road boundaries and reference paths, since these curves are typically aligned with the road or lane center. This frame is employed in Duijkeren et al., where nonlinear MPC is applied for highway scenarios. However, their approach is limited to low-curvature environments due to underlying assumptions. Oliveira et al. also use a road-aligned frame for scenarios involving narrow passages and sharp turns, focusing solely on forward driving. Although the road-aligned frame facilitates the straightforward integration of the information from the local road model, it requires complex approximations of the position of the semitrailer axle. Additionally, it complicates obstacle avoidance constraints, which potentially introduces conservative constraints and restricts feasible maneuvers.

Figure 2: Driving scenario with a car and a longer vehicle on a road with varying curvature, illustrated in Cartesian (left) and Frenet (right) frames. Due to the nonlinear transformation between the frames, obstacles that are convex in Cartesian coordinates may become non-convex in Frenet coordinates, with their shapes depending on the local path curvature.

We leverage the advantages of both coordinate frames by using Model Predictive Contouring Control (MPCC). MPCC integrates both coordinate frames by employing a vehicle prediction model in Cartesian coordinates, augmented with an additional state that represents the transformation between the two coordinate systems. This enables obstacle avoidance constraints to be expressed in Cartesian coordinates and road boundary constraints in Frenet coordinates. Within the domain of vehicle trajectory planning, MPCC has so far only been applied to passenger cars. Most of these approaches simplify the vehicle to a single point for boundary constraints, although Pauls et al. constrain multiple vehicle anchor points. Because their method assumes a car that stays close to a reference path, it cannot be applied to articulated commercial vehicles. Moreover, existing MPCC methods cannot ensure that the wheels of articulated vehicles remain within the road boundaries.

Therefore, in this study, we extend the existing MPCC framework by introducing additional augmented states. This enables the explicit formulation of road boundary constraints for the front and rear tractor axles, as well as the semitrailer axle, ensuring that all considered wheels remain within the drivable space. Furthermore, this extension allows to prioritize vehicle anchor points based on the driving scenario and prevent jackknifing.

## PRELIMINARIES

We denote vectors in bold. The global Cartesian coordinate frame is denoted by ${\overset{\rightarrow}{e}}^{\, 0}$, the body-fixed coordinate frames of the tractor and the semitrailer are ${\overset{\rightarrow}{e}}^{\, 1}$ and ${\overset{\rightarrow}{e}}^{\, 2}$, respectively, as illustrated in Fig. 3.

The subscript $k \in {\mathbb{N}}$ denotes the discrete timestep, where each timestep corresponds to a discrete time instance $t_{k} = {k\Deltat}$, with $\Deltat$ being a fixed sampling time. The subscript $i$ refers to the index of the anchor points of the vehicle, where $i \in {\{ 0,1,2\}}$ corresponds to the front axle of the tractor ($i = 0$), the rear axle of the tractor ($i = 1$) and the semitrailer axle ($i = 2$), as depicted in Fig. 3.

We assume that an upstream module in the autonomous driving pipeline generates a drivable corridor using the local road model. This corridor is defined by a reference path, representing the path the vehicle is expected to follow, and by the lateral distances from this path to the left and right boundaries. These boundaries indicate the area within which the vehicle's wheels should remain and can be based on the ego lane edges, road boundaries, or other relevant boundaries. The reference path is parameterized by its arc length $s$ using spline parametrization, which allows obtaining any point $\left( {x_{r}{(s)}},{y_{r}{(s)}} \right)$ on the reference path as a function of $s$. The angle $\psi_{r}{(s)}$ of the tangent to the path is given by

where $y_{r}^{\prime}{(s)}$ and $x_{r}^{\prime}{(s)}$ are the derivatives of $y_{r}$ and $x_{r}$ with respect to $s$, respectively. Similarly, it is possible to obtain the perpendicular lateral distance from the reference path to the left boundary $b_{l}{(s)}$ and the right boundary $b_{r}{(s)}$.

Figure 3: Visualization of the kinematic tractor-semitrailer vehicle model, where L1 is the wheelbase of the tractor measured in ${\overset{\rightarrow}{e}}^{\, 1}$, L1 b is the articulation joint position w.r.t. the rear axle in ${\overset{\rightarrow}{e}}^{\, 1}$, and L2 is the wheelbase of the semitrailer measured in ${\overset{\rightarrow}{e}}^{\, 2}$. Additionally, the augmented states θi and the corresponding contour errors Êic for i ∈ {0, 1, 2} are shown. In the illustration, the articulation joint is positioned behind the rear axle for clarity, while, in practice, it is commonly positioned in front of the rear axle.

A kinematic bicycle model for the tractor-semitrailer is used, as illustrated in Fig. 3. Here, the position of the tractor rear axle is given by ${x_{1}{\overset{\rightarrow}{e}}_{1}^{\, 0}} + {y_{1}{\overset{\rightarrow}{e}}_{2}^{\, 0}}$, with $x_{1}$ and $y_{1}$ being the respective components along ${\overset{\rightarrow}{e}}_{1}^{\, 0}$ and ${\overset{\rightarrow}{e}}_{2}^{\, 0}$. The heading angles of the tractor and the semitrailer are denoted by $\psi_{1}$ and $\psi_{2}$, respectively. The longitudinal velocity of the tractor is represented by $v_{1}$, and $\delta_{0}$ denotes the steering angle of the tractor's front wheel. The state and input vectors are ${\mathbf{x}} = \left\lbrack x_{1},y_{1},\psi_{1},\psi_{2} \right\rbrack^{\top}$ and ${\mathbf{u}} = \left\lbrack v_{1},\delta_{0} \right\rbrack^{\top}$, the continuous time kinematic equations are given by

where $\gamma_{1} = {\psi_{1} - \psi_{2}}$ is the articulation angle, and $L_{1},L_{1b}$ and $L_{2}$ represent vehicle dimensions as defined in Fig. 3. Note that we assume that the three (non-steered) semitrailer axles can be approximated by a single axle.

## PLANNING PROBLEM FORMULATION

The planning problem is formulated as a constrained nonlinear optimization problem, where an objective function (3a) is minimized while being subject to vehicle model dynamics (3b), inequality constraints concerning road boundaries, comfort, and safety (3d), and state and input bounds (3e)-(3f):

$\min\limits_{U_{k}}\mspace{21mu}$ ${J\left( X_{k},U_{k} \right)},$ (3a)
s.t. ${\mathbf{x}}_{j + {1|k}}^{m} = {f\left( {\mathbf{x}}_{j|k}^{m},{\mathbf{u}}_{j|k}^{m} \right)}$ $j$ ${= {0,\ldots,{N - 1}}},$ (3b)
${{\mathbf{g}}\left( {\mathbf{x}}_{j|k}^{m},{\mathbf{u}}_{j|k}^{m} \right)} \leq 0$ $j$ ${= {0,\ldots,N}},$ (3d)
$\underset{¯}{\mathbf{x}} \leq {\mathbf{x}}_{j|k}^{m} \leq \overline{\mathbf{x}}$ $j$ ${= {0,\ldots,N}},$ (3e)
$\underset{¯}{\mathbf{u}} \leq {\mathbf{u}}_{j|k}^{m} \leq \overline{\mathbf{u}}$ $j$ ${= {0,\ldots,{N - 1}}}.$ (3f)

Here, $N \in {\mathbb{N}}_{\geq 1}$ is the prediction horizon. The states and inputs at time $k + j$ are denoted by ${\mathbf{x}}_{j|k}^{m}$ and ${\mathbf{u}}_{j|k}^{m}$, where the superscript $m$ refers to the states and inputs in the MPCC formulation, which will be defined later. $X_{k}$ is the sequence of predicted states defined as $X_{k} = \left\{ {\mathbf{x}}_{1|k},\ldots,{\mathbf{x}}_{N|k} \right\}$, which depends on the initial condition ${\mathbf{x}}_{0|k}^{m}$, the discretized vehicle kinematics represented by $f{( \cdot )}$, and the predicted input sequence defined as $U_{k} = \left\{ {\mathbf{u}}_{0|k},\ldots,{\mathbf{u}}_{N - {1|k}} \right\}$. The objective function is denoted by $J{( \cdot )}$. The inequality constraints are collectively represented by $g{( \cdot )}$, and the lower and upper bounds on the states and inputs are denoted by ${\underset{¯}{\mathbf{x}},\overline{\mathbf{x}},\underset{¯}{\mathbf{u}}},$ and $\overline{\mathbf{u}}$, respectively.

Figure 4: Conceptual sketch of the MPCC approach for an arbitrary point (x,y), where the dashed line represents the reference path. The red arrows are the contour and lag errors in the Frenet frame and the green arrows are the approximation of those errors used in the MPCC formulation.

In general, the goal of MPCC is to steer a point $(x,y)$ along a reference path, as visualized in Fig. 4. This is achieved by minimizing the contour error $E_{k}^{c}$ and the lag error $E_{k}^{l}$, while maximizing the path speed. The errors are a function of $s$, which is the traveled distance by $(x,y)$ along the reference path. The calculation of $s$ requires the orthogonal projection of $(x,y)$ onto the reference path, which would lead to a nested optimization problem. The resulting computational load is typically too high to be used in dynamic, fast-changing contexts like city driving. Therefore, in MPCC, the state vector $\mathbf{x}$ is augmented with the progress state $\theta$. The dynamics of $\theta$ are given by

where the velocity of the progress state $v^{\theta}$ is added to the input vector $\mathbf{u}$. By adjusting the virtual velocity $v^{\theta}$, it is ensured that $E_{k}^{l}$ is minimized such that the progress variable $\theta$ approximates $s$. This allows to approximate the lag and contour error by ${\hat{E}}^{l}$ and ${\hat{E}}^{c}$:

{{\hat{E}}^{c} = -} & {{\left( {x - {x_{r}(\theta)}} \right){\sin\left( {\psi_{r}(\theta)} \right)}} +} \\
& {{\left( {y - {y_{r}(\theta)}} \right){\cos\left( {\psi_{r}(\theta)} \right)}},}
{{\hat{E}}^{l} =} & {{\left( {x - {x_{r}(\theta)}} \right){\cos\left( {\psi_{r}(\theta)} \right)}} +} \\
& {{\left( {y - {y_{r}(\theta)}} \right){\sin\left( {\psi_{r}(\theta)} \right)}}.}

From Fig. 4, it can be observed that $\theta \approx s$ if ${\hat{E}}^{l} \approx 0$. In contrast, ${\hat{E}}^{c}$ must be allowed to be comparably large to, for example, avoid obstacles on the reference path. These two conditions will be enforced in the objective function, which will be discussed in Section IV-B.

### IV-A Equality Constraints

The equality constraints consider the vehicle model. We extend the vehicle model in with integrators for inputs $v_{1}$ and $\delta_{0}$ to be able to impose limits on their rate of change, which is a common approach in Model Predictive Control. This ensures that the planned trajectory can actually be executed by a tractor‑semitrailer, given its limits on steering speed and acceleration capabilities. Therefore, the vehicle model in is extended with

where $a_{1}$ is longitudinal acceleration of the tractor and ${\overset{˙}{\delta}}_{0}^{u}$ is the steering rate. The model is discretized using a multiple shooting approach with fourth-order Runge-Kutta integration. Consequently, the vehicle model is formulated as a general discrete dynamical system as given in (3b).

Figure 5: Visualization of the corridor boundary constraints for each vehicle anchor point i.

### IV-B Objective Function

The objective function in (3a) is given by

where $J^{m}$ represents the MPCC objective function and $J^{c}$ is the objective function representing passenger and payload comfort. We do not explicitly include energy consumption, despite its importance to truck manufacturers and logistics organizations, but it can be added to the cost function if desired.

The objective function $J_{i}^{m}$ for one vehicle anchor point $i$ quadratically weights the lag and contour error, combined by a linear progress maximization reward to maximize path speed:

where ${\mathbf{e}}_{i,j} = {\lbrack{{\hat{E}}_{i}^{c}{({\mathbf{x}}_{j|k}^{m})}},{{\hat{E}}_{i}^{l}{({\mathbf{x}}_{j|k}^{m})}}\rbrack}^{\top}$ and ${\hat{E}}_{i}^{c}$ and ${\hat{E}}_{i}^{l}$ are defined . $Q_{i} = {\text{diag}{(q_{i}^{c},q_{i}^{l})}}$, which is a diagonal matrix with entries $q_{i}^{c}$ and $q_{i}^{l}$ on the diagonal and zeros elsewhere. The weights $q_{i}^{c}$, $q_{i}^{l}$, and $q_{i}^{v}$ weigh the contour error, the lag error, and the progress velocity, respectively, for vehicle anchor point $i$. The separate lag and contour weights ensure that ${\hat{E}}_{i}^{l}$ remains sufficiently small such that $\theta_{i} \approx s$, while allowing ${\hat{E}}_{i}^{c}$ to be large enough to leave the reference path if necessary.

In our research, we consider three vehicle anchor points $i \in {\{ 0,1,2\}}$, which are visualized in Fig. 3. As a result, there are three augmented states $\theta_{i}$ with corresponding velocity $v_{i}^{\theta}$, so we define ${\mathbf{x}}^{m} = \left\lbrack x_{1},y_{1},\psi_{1},\psi_{2},v_{1},\delta_{0},\theta_{0},\theta_{1},\theta_{2} \right\rbrack^{\top}$ and ${\mathbf{u}}^{m} = {\lbrack a_{1},{\overset{˙}{\delta}}_{0}^{u},v_{0}^{\theta},v_{1}^{\theta},v_{2}^{\theta}\rbrack}^{\top}$. The MPCC objective function in is then equal to

Each anchor point is associated by a dedicated set of weights, allowing prioritizing different parts of the vehicle, such as the semitrailer during docking maneuvers or both the tractor and the semitrailer during highway driving. By assigning driving scenario‑specific weights, this general approach can realize distinct behaviors (e.g., prioritizing the semitrailer during docking) across diverse driving scenarios without the need to develop specific methods for each scenario.

The comfort term $J^{c}$ quadratically penalizes large acceleration and steering rate values as a measure of passenger and payload comfort:

where $R = {\text{diag}{(q^{a},q^{\overset{˙}{\delta}},0,0,0)}}$ is a weight matrix.

### IV-C Inequality Constraints

The states and control inputs have to adhere to the limits given in (3e) and (3f). The limit values are determined considering comfort, actuator constraints, and legislation:

To keep the vehicle within the given corridor, the contour error ${\hat{E}}_{i}^{c}$ is constrained using $b_{l}{(\theta_{i})}$ and $b_{r}{(\theta_{i})}$ in (3d), as visualized in Fig. 5. This constraint is denoted for vehicle anchor point $i$ as

where $w$ is the vehicle width. We assume that the tractor and the semitrailer have the same width that remains constant along the vehicle. The constraints ensure that considered axle positions remain within boundaries, while overhanging sections may extend beyond. The left and right boundaries are assumed to account for vehicle overswaying.

To enforce passenger comfort and to ensure that the vehicle does not tip over, the lateral acceleration is constrained in (3d):

where $a_{y,\text{max}}$ is the maximum absolute lateral acceleration.

${\overset{˙}{\delta}}_{\text{max}}^{u}$

TABLE I: Optimization problem parameters. The velocity limits are given in forward ∣ reverse driving.

Figure 6: Visualization of the common logistics driving scenario, featuring a manually defined drivable corridor.

Figure 7: Prototype vehicle (© DAF Trucks N.V.).

## Results

Figure 8: Simulation results for forward driving and reverse driving scenarios, showing the driven (solid) and predicted (dashed) paths of the rear axle over time. The reference path is plotted as a black dashed line, and the shaded area visualizes the swept path of the full vehicle body during the maneuver. Because the reserve maneuver is infeasible starting from the proper lane, the reverse scenario starts from the opposite side of the road.

The proposed MPCC algorithm is implemented in Python using a receding horizon scheme, where the optimal control problem is repeatedly solved over a moving time window using CasADi and the HSL_MA57 solver in IPOPT \[Wächter2006\]. The relevant parameters are given in Table I. The prediction time $T$ is a tradeoff between computational complexity and sufficient prediction distance in both driving directions. The computation time is in the order of 100 ms per iteration (Intel i7-11800H CPU, Ubuntu 20.04). The horizon time combined with the maximum velocity of 15 km/h provides the trajectory planner with a forward look-ahead distance equivalent to approximately three tractor-semitrailer lengths. At a reverse-driving speed limit of 5 km/h, the look-ahead distance corresponds to approximately one tractor-semitrailer length.

We apply the MPCC method in simulation to a common logistics scenario illustrated in Fig. 7, where a vehicle must enter the premises of a customer through a gate or an industrial roll-up door from a city road. Fig. 7 also shows the drivable corridor. This scenario lets us demonstrate that the proposed MPCC algorithm plans a safe, comfortable, and efficient trajectory by ensuring the vehicle's wheels stay within the corridor boundaries and preventing jackknifing during reverse maneuvers. Additionally, we show that by adjusting the weight $q_{2}^{c}$, the semitrailer's position can be prioritized.

The vehicle successfully enters the premises in both forward and reverse directions, as shown in Fig. 8, using the same set of optimization weights. In both cases, the tractor adjusts its trajectory to keep the semitrailer axle within the corridor while negotiating the corner. During forward entry, the vehicle slows to 12 km/h to comply with the lateral acceleration limit, as shown in Fig. 9. The swept path visualizes the necessary maneuver space and highlights how the vehicle body extends beyond the corridor boundaries. This emphasizes the importance of accounting for vehicle size and kinematics when defining the corridor. Videos of the simulations are available at

Figure 9: The velocity v1, steering angle δ, and lateral acceleration ay are plotted over time for the forward driving results shown in Fig. 8. The horizontal dashed lines indicate the respective limit values. The figure shows that the lateral acceleration reaches its limit of 1.5m/s2 between 16.5s and 20 s. To remain within this limit while achieving the steering angle required to take the turn, the velocity is decreased.

Figure 10: Simulation results for forward driving and reverse driving when semitrailer is ignored in the optimization, resulting in corner cutting during forward driving and jackknifing in reverse driving.

Fig. 10 presents the forward and reverse driving results when the corridor constraints in for $i = 2$ are disabled and $q_{2}^{l} = q_{2}^{c} = 0$. This means that the semitrailer axle is ignored during optimization, resulting in (self-)collisions as visualized in Fig. 10. In the forward maneuver, the semitrailer exits the corridor, while in the reverse maneuver, the vehicle jackknifes. These results highlight the importance of considering the semitrailer in trajectory planning to obtain safe trajectories.

To demonstrate the effect of prioritizing a vehicle anchor point, we vary the weight of the semitrailer axle $q_{2}^{c} \in {\{ 10,100,1000\}}$, while keeping all other parameters unchanged. As illustrated in Fig. 11(a), increasing $q_{2}^{c}$ reduces the maximum lateral deviation of the semitrailer axle from the reference path, as expected . As a result, the tractor trajectory and the swept path are also influenced, as shown in Fig. 11(b) to 11(d). Since a higher $q_{2}^{c}$ reduces the lateral deviation of the semitrailer, the tractor extends less into the opposite lane. As a result, the steering angle must increase to complete the turn, leading to a lower velocity in the corner to satisfy the lateral acceleration constraint, as visualized in Fig. 12. The semitrailer trajectories converge approximately halfway through the corner into the narrower section of the corridor for each $q_{2}^{c}$. This suggests that this specific corridor primarily governs the trajectory of the vehicle. Despite this, the influence of the variation in $q_{2}^{c}$ remains evident from the results. This shows that the proposed approach effectively changes the behavior of the vehicle by adjusting the individual weights and allows the prioritization of specific vehicle anchor points depending on the driving scenario.

Next to the simulations, the MPCC approach has been successfully implemented on a prototype tractor-semitrailer, which is visualized in Fig. 7. A video of the first implementation results can be found at and a screenshot of this video is given in Fig. 13. The planned trajectory is provided to the vehicle, where a controller is used to follow the trajectory. A new trajectory is planned once the vehicle has driven 10% of the previous trajectory.

Figure 11: Simulation results for forward driving with varying q2c ∈ {10, 100, 1000}. The top-left plot shows semitrailer axle paths, while the other three depict the vehicle positions at t = 20 s and complete swept paths.

Figure 12: The velocity v1, steering angle δ, and lateral acceleration ay are plotted over time for the results shown in Fig. 11 for q2c = 10, q2c = 100 and q2c = 1000. The horizontal dashed lines indicate the respective limit values.

Figure 13: Still frame from the experimental testing video showing forward‑facing and side‑view camera feeds of the prototype vehicle negotiating a curve alongside a plot of its driven path (solid blue), reference path (dashed), swept path (shaded) and corridor boundaries (black)

## CONCLUSIONS AND FUTURE WORK

This paper presented a trajectory planning method for articulated commercial vehicles using Model Predictive Contouring Control (MPCC). The main contribution is the integration of multiple progress states, one for each vehicle anchor point, into the optimization framework. This approach allows to ensure that the considered wheels remain within the drivable corridor and enables prioritization of vehicle anchor points based on driving scenarios. The simulation results show that the vehicle successfully navigates a given drivable corridor in both forward and reverse directions, highlighting the need to consider the semitrailer to avoid exiting the corridor or jackknifing. In addition, the influence of a single optimization weight on the trajectories is analyzed, providing insights into controlling vehicle behavior. Finally, the first full-scale prototype test demonstrates the practical applicability of the method.

In future work, our objective is to evaluate the proposed method in various driving scenarios through real-world testing, including dynamic environments with other (vulnerable) road users. Although constructing a drivable corridor, which incorporates vehicle size and oversway, from the local road model is central to our method, doing so robustly in all driving scenarios is not trivial and requires further investigation.
