<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Trajectory Planning for an Articulated Commercial Vehicle Using Model Predictive Contouring Control

Topics include Model predictive contouring control, Articulated vehicles, Tractor-semitrailer, Trajectory planning, Autonomous driving, Road boundary constraints.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends MPCC to tractor-semitrailer vehicles by adding scenario-dependent anchor-point weighting and explicit road-boundary constraints for all axles. Validates forward and reverse navigation including docking and parking-to-charge, with full-scale prototype tests.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a trajectory planning method for articulated commercial vehicles, specifically tractor-semitrailers, based on Model Predictive Contouring Control (MPCC). Although MPCC has proven effective for passenger cars, it is generally ill-suited for tractor-semitrailers. These vehicles are significantly larger, the semitrailer follows a different path than the tractor, and reversing maneuvers are unstable and prone to jackknifing. Furthermore, practical driving scenarios often require scenario-dependent prioritization of different vehicle "anchor points", e.g., prioritizing the semitrailer position during docking or the tractor position when parking to charge. Therefore, we extend MPCC to enable scenario-dependent weighting of these anchor points and incorporate explicit road-boundary constraints for the front and rear tractor axles and the semitrailer axle, thereby ensuring that all considered wheels remain within the drivable area. The simulation results demonstrate the successful navigation of a representative logistic scenario in both forward and reverse direction. Furthermore, the influence of the optimization parameters on the trajectories is analyzed, providing insights into controlling the vehicle behavior.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, first tests using a full-scale prototype vehicle show the practical applicability of the approach.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In logistics, goods are commonly transported using articulated commercial vehicles, such as a tractor-semitrailer. During typical logistics driving scenarios, the vehicle not only drives forward through cities, industrial zones, and highways, but also reverses to load and unload the semitrailer at a dock. The introduction of autonomous vehicles into the logistics chain has the potential to improve efficiency and safety and address driver shortages. A crucial element is a trajectory planner that needs to plan vehicle maneuvers in the aforementioned driving scenarios while avoiding collisions, offering predictable driving to other road users, and maintaining passenger and payload comfort.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Trajectory planning algorithms for passenger cars have been extensively researched. However, developing a planner for a tractor-semitrailer poses additional challenges. Cars in Europe measure 2.5 to 5.5 meters in length and 1.6 to 2.0 meters in width, while European tractor-semitrailer combinations typically are 16.5 meters long and 2.55 meters wide. Furthermore, the semitrailer follows a different path than the tractor due to the articulation point, which is called offtracking. Moreover, articulated vehicles are unstable while driving in reverse, risking jackknifing. The effect of vehicle dimensions and offtracking is illustrated in Fig. 1, where a car and a tractor-semitrailer negotiate a 90° degree turn on a typical urban street. The car remains in its lane, while the tractor's front extends into the opposite lane, and the semitrailer's inner wheel exits the road on the inside. The example illustrates the need to explicitly consider the dimensions of the vehicle and the offtracking of the semitrailer during trajectory planning.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Any autonomous vehicle should behave in a predictable way. Other road users expect that an autonomous vehicle generally follows the middle of the lane at approximately the speed limit. We assume that a local geometric road model is available, which is a simplified, high-resolution map of the road geometry (e.g., lanes) including speed limits within the vehicle's immediate vicinity. We rely on HD-maps to create the road model but it could also be constructed from onboard sensor data (e.g., LiDAR, camera) and vehicle-to-everything (V2X) communication. A trajectory planner can leverage the information from the local road model to plan a trajectory that the tractor-semitrailer must follow and match the expectations of the other road users.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

safe, i.e. avoid collisions with static and dynamic obstacles and prevent rollover of the vehicle,

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

comfortable for the passengers and payload,

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

These requirements can conflict. For example, a longer travel time may result from the vehicle slowing down to prevent rollover while cornering. Furthermore, the planner must generate trajectories that are kinematically and dynamically feasible for a tractor-semitrailer for both forward and backward motion (e.g., no instantaneous 90° turns).

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

A trajectory planner for an articulated commercial vehicle should be able to prioritize one or more vehicle anchor points based on the driving scenario, where vehicle anchor points are specific physical locations on the vehicle. For example, the semitrailer's rear-door position is most important during docking, the tractor's charging-port location is crucial when charging, and both the tractor and the semitrailer should remain close to the lane center during highway driving.

<!-- chunk {"id": "body-0012", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this paper, we propose a trajectory planner that meets these requirements to plan a safe, comfortable, and efficient trajectory. The remainder of this paper is structured as follows. First, related work is discussed in Section II and Section III presents the necessary preliminaries. The approach itself is formulated in Section IV, followed by its application to a common logistics scenario in simulation and a first real-life test in Section V. Finally, conclusions and future work are provided in Section VI.

<!-- chunk {"id": "body-0013", "role": "body", "section": "PLANNING PROBLEM FORMULATION", "weight": 1.0} -->

Here, $N \in {\mathbb{N}}_{\geq 1}$ is the prediction horizon. The states and inputs at time $k + j$ are denoted by ${\mathbf{x}}_{j|k}^{m}$ and ${\mathbf{u}}_{j|k}^{m}$, where the superscript $m$ refers to the states and inputs in the MPCC formulation, which will be defined later.

<!-- chunk {"id": "body-0014", "role": "body", "section": "PLANNING PROBLEM FORMULATION", "weight": 1.0} -->

The inequality constraints are collectively represented by $g{( \cdot )}$, and the lower and upper bounds on the states and inputs are denoted by ${\underset{¯}{\mathbf{x}},\overline{\mathbf{x}},\underset{¯}{\mathbf{u}}},$ and $\overline{\mathbf{u}}$, respectively.

<!-- chunk {"id": "body-0015", "role": "body", "section": "PLANNING PROBLEM FORMULATION", "weight": 1.0} -->

In general, the goal of MPCC is to steer a point $(x,y)$ along a reference path, as visualized in Fig. 4. This is achieved by minimizing the contour error $E_{k}^{c}$ and the lag error $E_{k}^{l}$, while maximizing the path speed. The errors are a function of $s$, which is the traveled distance by $(x,y)$ along the reference path. The calculation of $s$ requires the orthogonal projection of $(x,y)$ onto the reference path, which would lead to a nested optimization problem. The resulting computational load is typically too high to be used in dynamic, fast-changing contexts like city driving. Therefore, in MPCC, the state vector $\mathbf{x}$ is augmented with the progress state $\theta$. The dynamics of $\theta$ are given by

<!-- chunk {"id": "body-0016", "role": "body", "section": "PLANNING PROBLEM FORMULATION", "weight": 1.0} -->

where the velocity of the progress state $v^{\theta}$ is added to the input vector $\mathbf{u}$. By adjusting the virtual velocity $v^{\theta}$, it is ensured that $E_{k}^{l}$ is minimized such that the progress variable $\theta$ approximates $s$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "PLANNING PROBLEM FORMULATION", "weight": 1.0} -->

From Fig. 4, it can be observed that $\theta \approx s$ if ${\hat{E}}^{l} \approx 0$. In contrast, ${\hat{E}}^{c}$ must be allowed to be comparably large to, for example, avoid obstacles on the reference path. These two conditions will be enforced in the objective function, which will be discussed in Section IV-B.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A Equality Constraints", "weight": 1.0} -->

The equality constraints consider the vehicle model. We extend the vehicle model in with integrators for inputs $v_{1}$ and $\delta_{0}$ to be able to impose limits on their rate of change, which is a common approach in Model Predictive Control. This ensures that the planned trajectory can actually be executed by a tractor‑semitrailer, given its limits on steering speed and acceleration capabilities. Therefore, the vehicle model in is extended with

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Equality Constraints", "weight": 1.0} -->

where $a_{1}$ is longitudinal acceleration of the tractor and ${\overset{˙}{\delta}}_{0}^{u}$ is the steering rate. The model is discretized using a multiple shooting approach with fourth-order Runge-Kutta integration. Consequently, the vehicle model is formulated as a general discrete dynamical system as given in (3b).

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-B Objective Function", "weight": 1.0} -->

where $J^{m}$ represents the MPCC objective function and $J^{c}$ is the objective function representing passenger and payload comfort. We do not explicitly include energy consumption, despite its importance to truck manufacturers and logistics organizations, but it can be added to the cost function if desired.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Objective Function", "weight": 1.0} -->

Each anchor point is associated by a dedicated set of weights, allowing prioritizing different parts of the vehicle, such as the semitrailer during docking maneuvers or both the tractor and the semitrailer during highway driving. By assigning driving scenario‑specific weights, this general approach can realize distinct behaviors (e.g., prioritizing the semitrailer during docking) across diverse driving scenarios without the need to develop specific methods for each scenario.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-C Inequality Constraints", "weight": 1.0} -->

The states and control inputs have to adhere to the limits given in (3e) and (3f).

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-C Inequality Constraints", "weight": 1.0} -->

To keep the vehicle within the given corridor, the contour error ${\hat{E}}_{i}^{c}$ is constrained using $b_{l}{(\theta_{i})}$ and $b_{r}{(\theta_{i})}$ in (3d), as visualized in Fig. 5. This constraint is denoted for vehicle anchor point $i$ as

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-C Inequality Constraints", "weight": 1.0} -->

where $w$ is the vehicle width. We assume that the tractor and the semitrailer have the same width that remains constant along the vehicle. The constraints ensure that considered axle positions remain within boundaries, while overhanging sections may extend beyond. The left and right boundaries are assumed to account for vehicle overswaying.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-C Inequality Constraints", "weight": 1.0} -->

where $a_{y,\text{max}}$ is the maximum absolute lateral acceleration.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Results", "weight": 1.0} -->

The proposed MPCC algorithm is implemented in Python using a receding horizon scheme, where the optimal control problem is repeatedly solved over a moving time window using CasADi and the HSL_MA57 solver in IPOPT \[Wächter2006\]. The relevant parameters are given in Table I. The prediction time $T$ is a tradeoff between computational complexity and sufficient prediction distance in both driving directions. The computation time is in the order of 100 ms per iteration (Intel i7-11800H CPU, Ubuntu 20.04). The horizon time combined with the maximum velocity of 15 km/h provides the trajectory planner with a forward look-ahead distance equivalent to approximately three tractor-semitrailer lengths. At a reverse-driving speed limit of 5 km/h, the look-ahead distance corresponds to approximately one tractor-semitrailer length.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Results", "weight": 1.0} -->

We apply the MPCC method in simulation to a common logistics scenario illustrated in Fig. 7, where a vehicle must enter the premises of a customer through a gate or an industrial roll-up door from a city road. Fig. 7 also shows the drivable corridor. This scenario lets us demonstrate that the proposed MPCC algorithm plans a safe, comfortable, and efficient trajectory by ensuring the vehicle's wheels stay within the corridor boundaries and preventing jackknifing during reverse maneuvers. Additionally, we show that by adjusting the weight $q_{2}^{c}$, the semitrailer's position can be prioritized.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Results", "weight": 1.0} -->

The vehicle successfully enters the premises in both forward and reverse directions, as shown in Fig. 8, using the same set of optimization weights. In both cases, the tractor adjusts its trajectory to keep the semitrailer axle within the corridor while negotiating the corner. During forward entry, the vehicle slows to 12 km/h to comply with the lateral acceleration limit, as shown in Fig. 9. The swept path visualizes the necessary maneuver space and highlights how the vehicle body extends beyond the corridor boundaries. This emphasizes the importance of accounting for vehicle size and kinematics when defining the corridor. Videos of the simulations are available at

<!-- chunk {"id": "body-0029", "role": "body", "section": "Results", "weight": 1.0} -->

Fig. 10 presents the forward and reverse driving results when the corridor constraints in for $i = 2$ are disabled and $q_{2}^{l} = q_{2}^{c} = 0$. This means that the semitrailer axle is ignored during optimization, resulting in (self-)collisions as visualized in Fig. 10. In the forward maneuver, the semitrailer exits the corridor, while in the reverse maneuver, the vehicle jackknifes. These results highlight the importance of considering the semitrailer in trajectory planning to obtain safe trajectories.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Results", "weight": 1.0} -->

To demonstrate the effect of prioritizing a vehicle anchor point, we vary the weight of the semitrailer axle $q_{2}^{c} \in {\{ 10,100,1000\}}$, while keeping all other parameters unchanged. As illustrated in Fig. 11(a), increasing $q_{2}^{c}$ reduces the maximum lateral deviation of the semitrailer axle from the reference path, as expected. As a result, the tractor trajectory and the swept path are also influenced, as shown in Fig. 11(b) to 11(d). Since a higher $q_{2}^{c}$ reduces the lateral deviation of the semitrailer, the tractor extends less into the opposite lane. As a result, the steering angle must increase to complete the turn, leading to a lower velocity in the corner to satisfy the lateral acceleration constraint, as visualized in Fig. 12. The semitrailer trajectories converge approximately halfway through the corner into the narrower section of the corridor for each $q_{2}^{c}$. This suggests that this specific corridor primarily governs the trajectory of the vehicle.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Results", "weight": 1.0} -->

Despite this, the influence of the variation in $q_{2}^{c}$ remains evident from the results. This shows that the proposed approach effectively changes the behavior of the vehicle by adjusting the individual weights and allows the prioritization of specific vehicle anchor points depending on the driving scenario.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Results", "weight": 1.0} -->

Next to the simulations, the MPCC approach has been successfully implemented on a prototype tractor-semitrailer, which is visualized in Fig. 7. A video of the first implementation results can be found at and a screenshot of this video is given in Fig. 13. The planned trajectory is provided to the vehicle, where a controller is used to follow the trajectory. A new trajectory is planned once the vehicle has driven 10% of the previous trajectory.

<!-- chunk {"id": "body-0033", "role": "body", "section": "CONCLUSIONS AND FUTURE WORK", "weight": 1.0} -->

This paper presented a trajectory planning method for articulated commercial vehicles using Model Predictive Contouring Control (MPCC). The main contribution is the integration of multiple progress states, one for each vehicle anchor point, into the optimization framework. This approach allows to ensure that the considered wheels remain within the drivable corridor and enables prioritization of vehicle anchor points based on driving scenarios. The simulation results show that the vehicle successfully navigates a given drivable corridor in both forward and reverse directions, highlighting the need to consider the semitrailer to avoid exiting the corridor or jackknifing. In addition, the influence of a single optimization weight on the trajectories is analyzed, providing insights into controlling vehicle behavior. Finally, the first full-scale prototype test demonstrates the practical applicability of the method.

<!-- chunk {"id": "body-0034", "role": "body", "section": "CONCLUSIONS AND FUTURE WORK", "weight": 1.0} -->

In future work, our objective is to evaluate the proposed method in various driving scenarios through real-world testing, including dynamic environments with other (vulnerable) road users. Although constructing a drivable corridor, which incorporates vehicle size and oversway, from the local road model is central to our method, doing so robustly in all driving scenarios is not trivial and requires further investigation.
