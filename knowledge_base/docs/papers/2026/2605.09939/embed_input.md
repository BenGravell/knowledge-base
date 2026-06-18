<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Neural Distance-Guided Path Integral Control for Tractor-Trailer Navigation

Topics include Vehicles, Safety, Real-time systems, Online algorithms, Control, Model predictive path integral control, Collision avoidance.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous and safe navigation of tractor-trailer systems requires accurate, real-time collision avoidance and dynamically feasible control, particularly in cluttered and complex agricultural environments. This is challenging due to their articulated, deformable geometries and nonlinear dynamics. Traditional methods oversimplify vehicle geometry or rely on precomputed distance fields that assume a known map, limiting their applicability in dynamic, partially unknown environments. To address these limitations, we propose a geometric neural encoder that provides fast and accurate distance estimates between the full tractor-trailer body and raw LiDAR perception, enabling real-time, map-free geometric reasoning. These learned distances are integrated into a Model Predictive Path Integral (MPPI) controller, allowing the system to incorporate true articulated geometry directly into its cost evaluation and enabling more responsive navigation in challenging agricultural settings. Simulation results demonstrate that the proposed framework generates dynamically feasible and safe trajectories for navigating tractor-trailer systems in cluttered and complex environments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Articulated tractor--trailer vehicles are widely used in agricultural operations for transporting crops, towing implements, and maneuvering within orchards, vineyards, and open farmlands. Compared with single-body agricultural vehicles, articulated systems introduce additional complexity due to multi-body coupling, off-axle hitching, articulation constraints, and the potential for unstable reversing behavior. These challenges are further amplified in cluttered agricultural settings that feature narrow spaces, static obstacles such as tree rows and storage bins, and dynamic objects including farm workers and other machinery. Ensuring safe and reliable navigation in such environments is therefore essential for enabling fully autonomous operation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prior research has examined the stability and controllability of articulated tractor--trailer systems used not only in agricultural settings but also in industrial and heavy-duty transport applications, highlighting issues such as jackknifing and degraded reversing performance. Various path-tracking and optimal control approaches have been explored, including optimal control formulations for headland turning, hybrid control strategies with global attractors, model predictive control for coordinated tractor--trailer regulation, and safety-governed articulation control for reverse motion. Additional efforts focus on minimizing swept path during reversing or applying reinforcement learning to obtain robust control policies. However, these methods primarily address path following and control tasks in simple geometric environments and do not explicitly handle dense obstacle fields from the environment.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Trajectory planning methods that explicitly account for environmental obstacles have also advanced for articulated systems. The progressively constrained nonlinear programming framework in Li et al. and the hierarchical optimization strategy in Li et al. demonstrate safe navigation capabilities, but both approaches rely on accurate prior maps and remain computationally demanding. More recent trajectory deformation method by Xu et al. offers improved efficiency, yet require maintaining an Euclidean Signed Distance Field (ESDF), which is costly to update in dynamic or occluded agricultural environments.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Navigating articulated vehicles in cluttered environments requires accurately computing distances between the vehicle body and surrounding obstacles. This is particularly challenging for tractor--trailer systems, whose articulated geometries make collision checking expensive. Moreover, simple occupancy checks are insufficient for safe navigation, as they provide only binary collision information and cannot indicate how close the vehicle is to nearby obstacles---information that is essential for predictive avoidance and smooth control. Simplified representations such as circles or inflated bounding boxes reduce computation but produce inaccurate distance estimates and can make navigation unnecessarily conservative or even infeasible in tightly constrained environments. Safe-corridor--based methods depend on a known map and can become overly restrictive when the calculated corridor is conservative. ESDF--based approaches provide better distance information without explicit corridor construction, but maintaining an ESDF in dynamic or partially occluded agricultural environments is costly. Optimization-based Collision Avoidance (OBCA) enables exact polygon-to-polygon distance queries through a duality-based formulation, but solving the associated optimization problem when many obstacles are present is too slow for real-time navigation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

These limitations highlight the need for a map-free, accurate, and computationally efficient geometric distance model that operates directly on raw sensor data. To address this need, we develop a geometric neural encoder that computes fast, accurate minimum distances between a tractor--trailer body and raw LiDAR point clouds. Using the dual optimization formulation of point-to-polygon distance, the encoder learns to predict dual variables efficiently, enabling real-time geometric reasoning without prior maps or geometric simplifications.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

For motion planning, we adopt the Model Predictive Path Integral (MPPI) control framework, a sampling-based optimal control method well suited for the nonlinear articulated dynamics of tractor--trailer systems and the discontinuous collision penalties arising from raw distance queries. MPPI has demonstrated strong performance in aggressive, real-time autonomous driving tasks when implemented on modern GPUs. By incorporating neural distance estimates directly into the MPPI cost evaluation, the controller can react responsively to LiDAR observations and generate safe, dynamically feasible trajectories through narrow and cluttered agricultural fields.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop a geometric neural encoder that provides fast and accurate signed-distance estimates between articulated tractor--trailer geometries and raw LiDAR point clouds, enabling real-time geometric reasoning without requiring a pre-built map.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We integrate these distance estimates into a Model Predictive Path Integral framework, enabling perception-driven local planning and collision avoidance for articulated agricultural vehicles operating under nonlinear dynamics and complex cost structures.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate the proposed pipeline in simulations and demonstrate its effectiveness in navigating tractor--trailer systems safely and autonomously through cluttered and complex environments.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Tractor--Trailer Kinematic Model", "weight": 1.0} -->

In this work, we model the tractor--trailer system using a simplified kinematic formulation. Because agricultural machinery typically operates at low speeds in field environments, lateral inertial effects are small, and a no-slip kinematic bicycle model is adopted as a first-order approximation. Although slip and model mismatch can still arise from soft soil, uneven terrain, tight maneuvers, and towing loads, the kinematic model remains widely used in agricultural robotics for its tractability and accurate representation of the tractor--trailer geometric coupling. The trailer considered here is a single off-axle semi-trailer, where the hitch point is located at a distance behind the tractor's rear axle.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Tractor--Trailer Kinematic Model", "weight": 1.0} -->

Let the state of the system be described by the tractor rear-axle position $(x,y)$, tractor heading $\theta$, and the articulation angle $\phi = {\theta_{1} - \theta}$ between the trailer heading $\theta_{1}$ and tractor heading $\theta$. Under these assumptions, the kinematic model of the articulated vehicle is

<!-- chunk {"id": "body-0014", "role": "body", "section": "Tractor--Trailer Kinematic Model", "weight": 1.0} -->

where $v$ is the tractor's longitudinal velocity and $\psi$ is the tractor steering angle. $L_{0}$ is the tractor wheelbase, $L_{1}$ is the distance from the hitch point to the trailer axle, and $L_{h}$ is the hitch offset from the tractor rear axle. The state is ${\lbrack x,y,\theta,\phi\rbrack}^{T}$, and the control input is ${\lbrack v,\psi\rbrack}^{T}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Tractor--Trailer Kinematic Model", "weight": 1.0} -->

Given the tractor pose $(x,y,\theta)$ and articulation angle $\phi$, the trailer heading can be recovered as $\theta_{1} = {\theta + \phi}$. The global coordinate of the trailer axle center $(x_{1},y_{1})$ is obtained by first computing the hitch position,

<!-- chunk {"id": "body-0016", "role": "body", "section": "Geometric Neural Encoder for Efficient Distance Computation", "weight": 1.0} -->

Safe navigation of the articulated tractor--trailer system requires maintaining sufficient clearance between the vehicle body and surrounding obstacles. Traditional methods either approximate the vehicle using simplified geometric primitives or inflate the environmental obstacles to simplify collision checking. Although computationally convenient, these approaches often lead to inaccurate distance estimates and overly conservative navigation, especially for vehicles with complex articulated geometries. To address this limitation, we leverage a geometric neural encoder that accelerates minimum-distance computation directly from raw LiDAR point clouds to the full tractor--trailer body geometry.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Geometric Neural Encoder for Efficient Distance Computation", "weight": 1.0} -->

Since any nonconvex geometry can be expressed as union of convex sets, we represent the tractor and trailer bodies as collections of convex polygons, $\{{\mathbb{V}}_{1},{\mathbb{V}}_{2},\ldots,{\mathbb{V}}_{K}\}$, where ${\mathbb{V}}_{1},\ldots,{\mathbb{V}}_{k}$ belongs to the tractor body and ${\mathbb{V}}_{k + 1},\ldots,{\mathbb{V}}_{K}$ belong to the trailer body.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Geometric Neural Encoder for Efficient Distance Computation", "weight": 1.0} -->

The same transformation applies to all polygons on both the tractor and the trailer, with the rotation matrix ${\overset{\rightarrow}{R}}_{1}$ and translation vector ${\overset{\rightarrow}{t}}_{1}$ for the trailer polygons defined by the pose $(x_{1},y_{1},\theta_{1})$ of the trailer body (formulation omitted here for simplicity).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Geometric Neural Encoder for Efficient Distance Computation", "weight": 1.0} -->

By leveraging the strong duality result in Zhang et al.,

<!-- chunk {"id": "body-0020", "role": "body", "section": "Geometric Neural Encoder for Efficient Distance Computation", "weight": 1.0} -->

where $w_{p}$ is a sufficiently large penalty coefficient. Due to strong convexity, can be efficiently solved using inexact block coordinate descent optimization, alternating between updates of ${\overset{\rightarrow}{\mu}}_{t}^{i}$ and ${\overset{\rightarrow}{\lambda}}_{t}^{i}$. However, evaluating this optimization for a large number of LiDAR points remains slow.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Geometric Neural Encoder for Efficient Distance Computation", "weight": 1.0} -->

To achieve real-time performance while retaining accuracy, we use a geometric neural encoder that learns to approximate the solution of. As observed in Han et al., each iteration of the dual optimization consists primarily of linear operations and simple nonlinearities, making it suitable for unrolled neural architectures.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Geometric Neural Encoder for Efficient Distance Computation", "weight": 1.0} -->

The architecture of the geometric neural encoder network is shown in Fig. 2. The network processes a batch of $M \times N$ transformed points expressed in the polygon's local frame, where $N$ represents an additional dimension, such as a receding horizon sequence along a predicted trajectory, allowing the encoder to output dual variables and distance estimates across multiple future steps. The encoder begins with a fully connected layer of size $n \times 16$, followed by layer normalization and a $\tanh$ activation. A second fully connected layer of size $16 \times 16$ with a ReLU nonlinearity is then applied. The depth of the network is constructed by repeatedly stacking these two types of layers, each maintaining 16 hidden units. The architecture concludes with a final linear layer of size $16 \times l_{i}$ that outputs the estimated dual variable ${\hat{\overset{\rightarrow}{\mu}}}_{t}^{i}$. Note that the network only predicts ${\hat{\overset{\rightarrow}{\mu}}}_{t}^{i}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Geometric Neural Encoder for Efficient Distance Computation", "weight": 1.0} -->

which follows directly from the equality constraint in the dual formulation. Since the encoder depends only on the polygon geometry, it only needs to be trained once for each polygon component.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Geometric Neural Encoder for Efficient Distance Computation", "weight": 1.0} -->

For each polygon defined by $({\overset{\rightarrow}{G}}_{i},{\overset{\rightarrow}{h}}_{i})$, we generate 100,000 random points within a range of $\lbrack{- 30},30\rbrack$ in both $x$ and $y$ directions. For each sampled point, the dual optimization problem in is solved using CVXPY with the ECOS solver (Domahidi et al. ). By slightly abusing the notation, the ECOS solver produces ground-truth optimal dual variables ${\overset{\rightarrow}{\mu}}_{j}^{i \ast}$, where the index $j$ denotes the $j$-th training point associated with polygon $i$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Geometric Neural Encoder for Efficient Distance Computation", "weight": 1.0} -->

The network is trained in a supervised manner to match both the dual variables and the induced signed distances.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Geometric Neural Encoder for Efficient Distance Computation", "weight": 1.0} -->

where Adam optimizer is used to update the network parameters.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Model Predictive Path Integral Control", "weight": 1.0} -->

Model Predictive Path Integral (MPPI) control is a sampling-based optimal control framework that solves a stochastic formulation of the finite-horizon control problem without requiring gradient information or convexity assumptions. This property makes MPPI particularly suitable for articulated agricultural vehicles, where nonlinear tractor-trailer dynamics, nonconvex obstacle geometries, and discontinuous distance-based penalties pose challenges for classical optimization-based MPC formulations.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Model Predictive Path Integral Control", "weight": 1.0} -->

where $\Deltat$ is the sampling period and $\mathcal{F}{( \cdot )}$ corresponds to the continuous-time kinematic model introduced in Section 2. To promote smoother motions and incorporate actuator limits, we augment the state with the tractor's longitudinal velocity and steering angle, and command their derivatives instead.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Model Predictive Path Integral Control", "weight": 1.0} -->

where $a_{t}$ is longitudinal acceleration and $\zeta_{t}$ is the steering rate.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Model Predictive Path Integral Control", "weight": 1.0} -->

for $\tau = {t,\ldots,{t + N}}$. The superscript $(s)$ denotes the $k$-th sampled rollout, with $k = {1,\ldots,K}$ and $K$ is the number of rollouts. Each perturbed control sequence generates a simulated trajectory through tractor-trailer dynamics, producing $\{{\overset{\rightarrow}{s}}_{t}^{(k)},\ldots,{\overset{\rightarrow}{s}}_{t + N}^{(k)}\}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Model Predictive Path Integral Control", "weight": 1.0} -->

Each simulated trajectory is evaluated using a running cost that captures goal tracking, smooth motion, articulation feasibility, and collision avoidance.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Model Predictive Path Integral Control", "weight": 1.0} -->

A crucial component of the cost function is obstacle avoidance. At each predicted state ${\overset{\rightarrow}{s}}_{\tau}^{(k)}$, the minimum distance between the articulated tractor-trailer body and surrounding obstacles is computed using the geometric neural encoder introduced in Section 3. The pretrained encoder takes LiDAR points transformed into the polygon's local frame and outputs estimated dual variables, from which accurate point-to-polygon distances can be reconstructed.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Model Predictive Path Integral Control", "weight": 1.0} -->

where $\varepsilon$ is a small positive constant. This formulation enables the controller to reason about complex articulated geometries and obstacles directly from raw sensor measurements.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Model Predictive Path Integral Control", "weight": 1.0} -->

After that, MPPI applies an importance-sampling update inspired by path integral control theory.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Model Predictive Path Integral Control", "weight": 1.0} -->

where $\lambda > 0$ is a temperature parameter that regulates sensitivity to high-cost trajectories.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Model Predictive Path Integral Control", "weight": 1.0} -->

The first control input ${\overset{\rightarrow}{u}}_{\tau = t}$ is then applied to the tractor-trailer system, and the prediction horizon is shifted forward, yielding a receding-horizon scheme suitable for real-time use. The complete framework is summarized in Algorithm 1.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Model Predictive Path Integral Control", "weight": 1.0} -->

By combining accurate and fast neural distance estimation with sampling-based optimal control, the proposed framework generates dynamically feasible and collision-aware trajectories in cluttered and partially unknown agricultural environments. The neural encoder provides precise obstacle proximity information directly from raw LiDAR measurements, while MPPI efficiently explores perturbations that respect the nonlinear articulated dynamics and operational constraints. Together, these components form a robust and efficient navigation solution for articulated tractor-trailer system operating in complex field settings. The current framework performs goal chasing, but it can be extended to reference-path tracking by replacing ${\overset{\rightarrow}{s}}_{\text{goal}}$ with a time-indexed reference ${\overset{\rightarrow}{s}}_{\text{ref},\tau}$ provided by a high-level planner.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We evaluate the performance of the proposed navigation framework in a simulated environment containing dense obstacles and narrow free-space passages. The articulated tractor--trailer model used in simulation consists of three convex polygons: one for the tractor body and two for the trailer, as shown in Fig. 1a. The tractor measures ${{3.35m} \times 1.48}m$, while the trailer includes a rectangular body of ${{1.2m} \times 3.6}m$ and a triangular connector part. The tractor wheelbase is $L_{0} = {1.9m}$, the hitch offset is $L_{h} = {0.5m}$, and the trailer axle is located $L_{1} = {1.5m}$ behind the hitch point.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

A geometric neural encoder is trained for each convex polygon. Training all three encoders requires approximately 2.2 hours on a machine equipped with an Intel i9-13900KF CPU and an NVIDIA RTX 4090 GPU. Each encoder is trained for 5,000 epochs using 80/20 train-test split of the dataset. After training, the mean squared error (MSE) between predicted and ground-truth dual variables and point-to-polygon distances on the test set drops below $1 \times 10^{- 5}$, indicating strong convergence. Once trained, the encoders are integrated into the MPPI controller and used online without further optimization.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

A simulated 2D LiDAR sensor provides point clouds at every time step, which serve as input to the neural encoders. The robot's state is assumed to be known; on real platforms, this could be provided by a localization module running a Simultaneous Localization and Mapping (SLAM) algorithm. The MPPI controller is configured with a prediction horizon of 50 steps, a time step of ${\Deltat} = {0.1s}$, 1000 sampled trajectories per update, Gaussian exploration noise $\Sigma_{w} = {{diag}{}}$, and a temperature parameter $\lambda = 1$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

The running cost uses the following weights: $W_{g} = {{diag}{(1,1,0.5,0.5,0,0)}}$ for goal tracking, $W_{u} = {{diag}{(0.1,0.1)}}$ for control effort, $W_{\Deltau} = {{diag}{(0.1,0.1)}}$ for smoothness, $w_{\phi} = 1$ for articulation penalty, and $w_{obs} = 5$, $w_{coll} = 50$ for collision. A terminal cost with weight $W_{T} = {10W_{g}}$ is applied to bias the final state toward the goal. These parameters are tuned empirically. The controller is implemented in Python with GPU acceleration.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

This work presented a neural distance--guided Model Predictive Path Integral control framework for real-time navigation of articulated tractor--trailer systems in cluttered environments. By combining a duality-inspired geometric neural encoder with a sampling-based stochastic control method, the proposed pipeline achieves accurate distance estimation and safe, dynamically feasible navigation for tractor-trailer systems without requiring prior maps or geometric simplifications.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

While effective, the current framework requires training a separate neural encoder for each polygon geometry. A promising direction for future work is the development of a universal or geometry-conditioned encoder that can generalize across multiple tractor--trailer configurations without retraining. Since MPPI functions as a local planner, it may become trapped in local minima in highly constrained environments, and integrating our approach with a global planner would provide high-level guidance and improve robustness. Real-world deployment is another important next step, which will require filtering ground returns and overhanging obstacles by selecting 3D LiDAR points within a height band of interest and projecting them onto the 2D plane, together with outlier rejection for sensor noise. The neural encoder processes points in parallel on the GPU and scales favorably with point count, and voxel downsampling can further reduce input size for embedded platforms. Additional future work includes expanded studies across diverse field layouts, more extensive testing in reverse-motion scenarios, evaluation under dynamic and moving obstacles, and quantitative comparisons with state-of-the-art planners.
