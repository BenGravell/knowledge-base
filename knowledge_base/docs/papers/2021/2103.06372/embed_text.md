## Introduction and Related Work

PA with additional hardware

Reduce state estimation uncertainty

Record/chase a target

Avoidance of dynamic obstacles

Table I: Classification of the related work, together with a (nonexhaustive) list of references.

While the last decade has seen an increase on the number of successful deployments of multirotor-UAVs in different real-world scenarios, their applicability is often limited by two common assumptions, namely the fact that the environment is static, and/or the omnidirectional coverage of the sensor(s) of the UAV. Indeed, many UAVs have a limited FOV, and many applications (delivery, aerial videography, emergency response, etc.) have non-static environments due to the presence of cars, people, and/or other UAVs. Hence, relaxing these assumptions is critical to fully exploit the potential of the UAVs and expand the range of their possible applications.

Figure 1: UAV planning perception-aware trajectories in a dynamic unknown environment, with relative velocities of up to 6.3 m/s. All the computation runs onboard, and the UAV does not have any prior knowledge of the trajectories or specific shape/size of the dynamic obstacles.

When a UAV equipped with a limited FOV sensor is flying in an unknown environment (e.g., Fig 1), it is crucial to plan both the position and orientation of the UAV to maximize the detection and the tracking accuracy of the unknown obstacles while at the same time doing obstacle avoidance. This perception-aware (PA) component is especially important when flying in dynamic environments, because a consistent detection of the moving obstacles is necessary to obtain a good estimate of their locations and prediction of their future trajectories.

Perception-awareness for UAVs has been studied thoroughly in the literature, and, as shown in Table I, the related work could be classified according to the formulation used and the goal itself. From the point of view of the formulation used, there are approaches that are not PA, which typically plan the translation and then have either a constant yaw or a yaw such that the FOV of the camera points in the direction of travel (e.g., see ). For instance, used potential fields to avoid dynamic obstacles, but without taking into account perception-awareness, which can degrade the detection and prediction of the trajectories of the obstacles.

Other approaches are PA by including additional hardware: For example, by gimbal-mounting the camera, some of its degrees of freedom can be controlled independently of the rotation of the UAV. Another option is to mount omni-directional sensors. However, these approaches usually require additional hardware and mechanical complexity, which is typically undesirable on small UAVs.

PA planning has received increased attention over the last few years due to its inherent ability to leverage the trajectory planned to maximize the PA objective. The related works could be subclassified according to whether or not the translation and yaw of the UAV are jointly optimized. On one hand, there are approaches that decouple translation and yaw by optimizing them separately. For instance, in, a yaw trajectory is obtained for a fixed translational path to gain information about unknown static obstacles. For features or landmarks whose locations are known a priori, optimizes the time parametrization on a fixed spatial and yaw path to maximize their visibility. In, translation is optimized first, and then yaw is optimized to guarantee the co-visibility of the features. While this decoupling of translation and yaw has computational advantages, it can lead to conservative results, since the translational trajectory (and consequently two degrees of freedom of the rotation as well) is fixed in the yaw optimization. Other works assume a downward-facing camera, and hence only translation (not yaw) is planned to keep a specific target in the FOV of the camera.

Another approach taken is to jointly optimize translation and yaw, which enables the planner to fully exploit *both* the position trajectory and the yaw angle. This joint optimization leads to less conservative results than the approaches that decouple translation and yaw, but it typically comes at the expense of much higher computation times, especially when done in combination with dynamic obstacle avoidance constraints. For example, proposed an on-manifold trajectory optimization approach that couples together translation with the full rotation, but the computation times required (up to $30$ s) are not real time. Ref. successfully presented a real-time MPC formulation that keeps the centroid of the VIO features in the center of the image while minimizing its projected velocity. However, this formulation does not include collision avoidance of static (or dynamic) obstacles, which greatly simplifies the complexity of the optimization problem. In, translation and yaw are optimized jointly, but only static obstacle avoidance is performed. The technical gap then is how to jointly optimize the full pose of the UAV, satisfy its underactuated dynamics, and guarantee safety in dynamic environments while maintaining real-time computational tractability.

The underactuated dynamics of the UAV (caused by the total thrust of the UAV being fixed in the body frame) makes this joint optimization especially hard, since a given spatio-temporal path fixes two degrees of freedom of the rotation, leaving only one extra degree of freedom in the rotation^11^1Usually referred to as *yaw*, *heading*, or simply $\psi$. A typical way to impose this constraint is via the dynamic equations of the UAV. However, this comes at the expense of having differential equations as constraints in the optimization.

An alternative is to leverage the differential flatness of the UAVs and make use of the map ${({{\mathbf{a} \in {{\mathbb{R}}^{3} \smallsetminus \left\lbrack {0\;0 - g} \right\rbrack^{T}}},{\psi \in S^{1}}})}\rightarrow\mathbf{R}_{b}^{w} \in {\text{SO}{}}$ that maps $\psi$ and the acceleration $\mathbf{a}$ to the rotation of the body. However, and due to the *hedgehog theorem* in $S^{2}$, there is no single continuous function that defines this map for all possible accelerations $\mathbf{a}$. For the most common definitions of this map, the singularity appears for each $\psi$ at two antipodal points in the unit sphere of possible normalized relative accelerations, which means that there is at least one singularity with a great-circle distance $\leq 90^{\circ}$ with respect to the hovering condition. This closeness between the hovering condition and the singularity can limit the set of possible accelerations in aggressive flights, since an optimal solution that passes through or close to this singularity can provoke numerical instabilities and/or lead to artificial large changes in orientation. Recently, the Hopf map was leveraged in to place the singularity in the inverted ("upside-down") configuration, which is independent of $\psi$ and has the farthest possible angle away from the hovering condition. Although flying highly aggressive trajectories is not the main goal of this work, we decide to use the Hopf map (as opposed to the commonly-used maps presented in ) since it automatically maximizes the distance to the singularity by simply changing the definition of the map. In, however, the Hopf fibration was only used in the controller to track predefined trajectories. It was also leveraged in to find the set of charts for a previously-optimized position trajectory, which are then used for the controller and to obtain the $\psi$ trajectory. In this work, we propose instead to embed the Hopf fibration in the joint (translation *and* yaw) coupled planning optimization as a way to directly obtain trajectories in $\text{SE}{}$ that, by construction, satisfy the underactuated dynamics of the UAV.

From the point of view of the goal of the perception awareness, most of the related works focus on reducing the state estimation uncertainty, usually by keeping specific features/landmarks in the FOV, and/or choosing high-textured areas. These features are typically static in the world frame. Some of these approaches also leverage the Observability Gramian, especially when trying to ease the estimation of an unknown parameter of the dynamical system.

Further relevant work addresses the problem of having a UAV record or chase a target. For example, focused on tracking a moving target with a downward-facing camera, while proposed a way to follow a moving target while avoiding other static obstacles in the environment. Most of these works focus therefore on chasing a static or dynamic target, not on avoiding it.

Our work differs from these two previous approaches because it proposes the use of PA planning to enhance the avoidance of dynamic obstacles. Compared to or, PA planning to avoid unknown dynamic obstacles comes with many additional challenges, such as the coupling of *both* the ego-motion and the motion of the obstacle in the visibility cost and blur of the image, the inclusion of dynamic obstacle avoidance constraints in the optimization, the need to predict the future trajectories of the obstacles, and the consideration of the uncertainty of these predicted trajectories, just to name a few.

Element-wise absolute value, element-wise inequality.

${\mathbf{e}}_{z}:=\begin{bmatrix}
\end{bmatrix}^{T}$, $\mathbf{1}:=\begin{bmatrix}

Field of View, Axis-Aligned Bounding Box.

Special orthogonal group, Special Euclidean group.

Inverse of the standard normal cumulative distribution function.

Set of clamped uniform splines with dimension d, degree p, and m + 1 knots.

n:= m − p − 1 n + 1 is the number of control points of the spline.

Position, Velocity, Acceleration, and Jerk of the UAV, ∈ ℝ3. All of them are of the body w.r.t. the world frame, and expressed in the world frame.

Relative acceleration, expressed in the world frame: ${\mathbf{ξ}}:=\begin{bmatrix}
\mathbf{a}_{x} &amp; \mathbf{a}_{y} &amp; {\mathbf{a}_{z} + g}
\end{bmatrix}^{T}$. We will assume ξ ≠ 0.

Angle (and its derivative) such that ${\mathbf{q}}_{b}^{w} = {{\mathbf{q}}_{\mathbf{ξ}} \circ \begin{bmatrix}
c_{\psi/2} &amp; 0 &amp; 0 &amp; s_{\psi/2}
\end{bmatrix}^{T}}$ (see section II-D1).

State vector: $\mathbf{x}:=\begin{bmatrix}
\mathbf{p}^{T} &amp; \mathbf{v}^{T} &amp; \mathbf{a}^{T} &amp; \psi &amp; \overset{˙}{\psi}
\end{bmatrix}^{T} \in {\mathbb{R}}^{11}$.

Point expressed in the frame a. For the definitions of this table that include the sentence “expressed in the world frame”, the notation of the frame is omitted.

$\overset{\sim}{\mathbf{p}}$, $\overline{\mathbf{p}}$
$\overset{\sim}{\mathbf{p}}:=\begin{bmatrix}
\end{bmatrix}^{T}$, $\overline{\mathbf{p}}:=\frac{\mathbf{p}}{\left\| {\mathbf{p}} \right\|}$

${\mathbf{T}}_{b}^{a} = \begin{bmatrix}
{\mathbf{R}}_{b}^{a} &amp; {\mathbf{t}}_{b}^{a} \\
Transformation matrix: ${\overset{\sim}{\mathbf{p}}}^{a} = {{\mathbf{T}}_{b}^{a}{\overset{\sim}{\mathbf{p}}}^{b}}$. Analogous definition for the quaternion qba.

Rotation matrix associated with the quaternion q.

Set of indexes of all the intervals J = {0, 1, …, m − 2 p − 1}.

Index of the interval of the trajectory, j ∈ J.

Set of indexes of the tracked obstacles.

Index of the obstacle, i ∈ I.

Index of the obstacle used in the PA term of the cost function.

Mean of the predicted position of obstacle i, expressed in frame a

The predicted trajectory of the obstacle i, in the world frame, is ∼ N ((pi)w (t),(diag (σi (t)))2).

Focal length of the camera in meters.

Opening angle of the cone that approximates the FOV.

q_{w} &amp; q_{x} &amp; q_{y} &amp; q_{z}
Components of a unit quaternion.

1(pi)w ∈ FOV ≈ 1((pi)c)z/∥(pi)c∥ ≥ cθ/2 ≈ σ (γ (−cθ/2+((pi)c)z/∥(pi)c∥)). γ is a positive parameter.

Index of the control point. l ∈ Lp for p (t), l ∈ Lp ∖ {np} for v (t), l ∈ Lp ∖ {np − 1, np} for a (t), l ∈ Lψ for ψ and l ∈ Lψ ∖ {nψ} for $\overset{˙}{\psi}$

Position, velocity, and acceleration control points, (∈ℝ3), ψ and $\overset{˙}{\psi}$ control points (∈ℝ).

Set of position control points of the interval j using the MINVO basis. Analogous definition for the velocity control points 𝒱jMV.

∈, percentile of the standard normal distribution (see next row).

Set of vertexes of the convex hull of the set obtained by inflating (𝒬jMV)obs i with norminv (δ) ⋅ σi (tend j), half of the sides of the AABB of the obstacle i and half of the sides of the AABB of the agent.

Plane ni jT x + di j = 0 that separates (𝒬jMV)agent from 𝒞i jMV.

Hopf fibration, stereographic projection.

Snapshot at t = t1 (current time):

gterm ( ) is the terminal goal, and is the current position of the UAV.

is the trajectory the UAV is currently executing.

is the trajectory the UAV is currently optimizing, t ∈ [tin,tf]

d ( ) is a point in, used as the initial position of

ℳ is a sphere of radius r around d.

g ( ) is the projection of gterm ( ) onto the sphere ℳ.

d, g, and gterm are expressed in the world frame.

Table II: Notation used in this paper.

In summary, the proposed contributions of this work are as follows:

Real-time PA planning formulation that jointly optimizes the translation and the full rotation to maximize the visibility of unknown dynamic obstacles, while simultaneously avoiding them. Compared to non-PA approaches and PA decoupled approaches, our proposed coupled solution leads to a presence of the obstacle in the FOV 7.9 and 1.5 times more frequent, respectively. The success rates achieved are on average $2.98$ times larger than other state-of-the-art approaches when flying in multi-obstacle dynamic environments.

We show how the Hopf fibration can be embedded in the planning optimization to jointly optimize translation and yaw while implicitly imposing the underactuated dynamics that couples acceleration and orientation. This avoids the need to explicitly impose the dynamics of the UAV as differential constraints, while automatically guaranteeing the largest possible great-circle distance between the hovering condition and the differential flatness singularity. Dynamic obstacle avoidance constraints are imposed by leveraging the MINVO basis to reduce conservatism.

Extensive set of hardware experiments in unknown dynamic environments, with everything (navigation, perception, planning, and control) executed onboard the UAV, and without any prior knowledge of the trajectories or specific shape/size of the obstacles. The UAV achieves velocities of up to 5.8 m/s and relative velocities (with respect to the obstacles) of up to 6.3 m/s. The replanning times achieved onboard are $\approx 53$ ms.

The code has also been released open source for the community.

This paper uses the notation shown in Table II.

## PANTHER

PANTHER comprises four modules: Tracker and predictor, selector of the obstacle in the PA term, planes and initial guess generator, and optimization (see Fig. 2). A summary of how all these modules work together is as follows: First the incoming point clouds of the onboard depth sensor are clustered and tracked using the Hungarian algorithm to obtain the trajectory, as a probability distribution, of each of the obstacles (section II-A). The obstacle $i^{\ast}$ that the UAV is most likely to collide with is then selected to be included in the PA term of the cost function (section II-B). Then, a kinodynamic search-based planner (Octopus Search Algorithm ) is run to find a initial guess of the translational trajectory $\mathbf{p}{(t)}$ that avoids the probabilistic trajectories of the obstacles found before (section II-C1). This translational guess and the obstacle $i^{\ast}$ selected are then used to run a graph search algorithm to find the $\psi{(t)}$ guess (section II-C2). Finally, the $\mathbf{p}{(t)}$ and $\psi{(t)}$ guesses are used for the nonconvex optimization to obtain the optimized trajectory, that is sent to the controller of the UAV (section II-D). In this framework, the coupling between rotation and acceleration is imposed implicitly using the Hopf fibration. All these modules are described in detail in the following subsections.

Figure 2: (A) Different modules of PANTHER. (B) Predicted trajectories of the obstacles and convex representation of each segment of the trajectory of the agent and the obstacles. (C) World, body, and camera frames. (D) Hopf fibration and its stereographic projection, partly inspired from. Given a specific relative acceleration ξ (with $\overline{\mathbf{ξ}} \neq {- {\mathbf{e}}_{z}}$), the quaternion qbw = qξ ∘ qψ is a fiber (specifically a circle) in S3 parameterized by ψ. On the bottom right, the body frames for different values of ψi for each ξi are shown.

### II-A Tracking and Prediction

We create a k-d tree representation of the point clouds coming from the onboard depth sensor, and perform Euclidean clustering to group the points that are more likely to belong to the same obstacle (see Fig. 2). For each cluster found, we compute the AABB (Axis-Aligned Bounding Box) centered on the centroid of that cluster^22^2Regardless of whether or not the obstacle is convex, this produces an outer convex approximation of the visible part of the obstacle.. Then, to assign each cluster to a specific track, we minimize the total assignment cost using the Hungarian algorithm, where the cost is the pairwise distance between the centroid of each cluster and the prediction of the tracks at the time the point cloud was produced. If this distance is above a specific threshold (usually $\approx 1$--2 m), we create a new track for it. If a cluster is not assigned to any track (which can happen if there are more clusters than tracks), then a new track is created for it. Finally, given a sliding window history of all the observations associated with a track, we fit a polynomial for each coordinate $\{ x,y,z\}$. To capture the stochasticity of the prediction problem, the predicted position at time $t$ is then approximated by a 3D Gaussian distribution (mean from the value of the fitted polynomial and a diagonal covariance matrix obtained from the prediction intervals \[44, section 5.7\]).

### II-B Selection of the obstacle in the PA term

When there are several predicted trajectories, and to maintain computational tractability, the agent needs to choose which one of them to include in the PA term of the cost function. It does so by choosing the most likely obstacle to collide with in the future, using a simple heuristic of the probability of collision based on Boole's inequality:

where $U$ is the number of samples taken, $t_{u}:={t_{\text{in}} + {\frac{u}{U}{({t_{f} - t_{\text{in}}})}}}$ and ${{\mathbf{κ}}{(u)}}:={{\mathbf{d}} + {\frac{u}{U}{({{\mathbf{g}}_{\text{term}} - {\mathbf{d}}})}}}$ is a point in a straight line from $\mathbf{d}$ to ${\mathbf{g}}_{\text{term}}$. Note that although only one obstacle is included in the PA objective function, all the predictions of the tracked obstacles are included in the collision avoidance constraints.

Additionally, and to address the trade-off between gathering information about the obstacle, and gathering information about the direction of travel, the UAV will include the obstacle $i^{\ast}$ in the PA term if the angle between $\left( {{\mathbf{g}}_{\text{term}} - {\mathbf{d}}} \right)$ and $\left( {{\left( {\mathbf{p}}_{i^{\ast}} \right)^{w}{(t_{\text{in}})}} - {\mathbf{d}}} \right)$ is smaller than a predefined angle $\alpha_{0}$ (typically $\approx 90^{\circ}$). Otherwise the UAV will try to align the FOV of the camera with the direction of travel.

### II-C Planes and Initial guesses

### II-C1 Separability planes and initial guess for position

We use the Octopus Search Algorithm (OSA), which is a search-based algorithm that operates directly on the control points of the position spline. It ensures collision-free constraints between the agent and the dynamic obstacles by finding the planes that separate the inflated MINVO polyhedral representation of each interval $j$ of the trajectory of the obstacle $i$ (denoted as $\mathcal{C}_{ij}^{\text{MV}}$) and the MINVO polyhedral representation of that interval $j$ of the trajectory of the agent, denoted as $\left( \mathcal{Q}_{j}^{\text{MV}} \right)_{\text{agent}}$ (see Fig. 2). The outputs of this algorithm are both the position control points and the planes ${\mathbf{π}}_{ij}$ (given by ${{{\mathbf{n}}_{ij}^{T}{\mathbf{x}}} + d_{ij}} = 0$) ${\forall i},{\forall j}$. The position control points are then used as initial guess in the optimization, while the planes ${\mathbf{π}}_{ij}$ are held fixed in the optimization. The reader is referred to our previous work for a more in-depth explanation of the OSA.

### II-C2 Initial guess for $\psi$

To obtain the initial guess for $\psi$, we uniformly sample the position guess spline obtained through the OSA, and for each of these position samples, we uniformly sample several values of $\psi \in {\lbrack{- \pi},\pi)}$. Each one of these $\mathbf{p}$-$\psi$ samples will be a node, and all the nodes associated with the same position sample, but with different $\psi$, will constitute a *layer* (see Fig. 2). Then, we create a graph connecting with directed edges all the nodes of one layer to the nodes of the next layer. Each node has therefore a time, position, acceleration, and yaw associated with it, and all the nodes of the same layer have the same time, position, and acceleration. The cost of the edge between two nodes $n_{1}$ and $n_{2}$ of the graph is then given by

Here, $c_{\psi}$, $c_{\Psi_{\text{max}}}$, and $c_{\text{FOV}}$ are nonnegative weights, while $\psi_{n_{u}}$, $t_{n_{u}}$, and $\left( {{\mathbf{T}}_{n_{u}}\left( t_{n_{u}} \right)} \right)_{c}^{w}$ are the angle $\psi$, the time, and the transformation matrix associated with node $n_{u}$. Note that the edge cost is guaranteed to be nonnegative at all times. The transformation matrix can be directly obtained from the position, acceleration, and yaw of the node. The first term in the cost penalizes the distance between two $\psi$ angles, the second term penalizes edges that do not satisfy the limit $\Psi_{\text{max}}$, and the last one rewards the visibility of the obstacle. The units of the weights above are such that the corresponding term is dimensionless (see section III). To choose these weight values, we first set $c_{\Psi_{\text{max}}}$ to a large value to guarantee the $\Psi_{\text{max}}$ constraint. Then, $c_{\psi}$ and $c_{\text{FOV}}$ are selected as a trade-off between smoothness and inclusion of the obstacle $i^{\ast}$ in the FOV of the UAV. The root node of the graph corresponds to the state $\mathbf{d}$ (see last row of Table II). We solve the search problem using Dijkstra's algorithm, with early termination when the search reaches a node of the last layer. Letting $\Lambda$ denote the indexes of the nodes of the path found, we shift the angles ${\psi_{n_{\lambda}}{\forall\lambda}} \in \Lambda$ (by adding or subtracting $2\pir$, $r \in {\mathbb{Z}}$) such that the absolute difference between two consecutive angles is $\leq \pi$. Using ${\hat{\psi}}_{n_{\lambda}}$ to denote these shifted angles, a spline is fitted to these angles by solving the following constrained least square problem:

Note that, as this problem is a quadratic program with linear equality constraints, its solution can be easily found by simply solving the linear Karush-Kuhn-Tucker (KKT) conditions associated with it ^33^3For a detailed explanation of the derivation of the resulting linear system of equations, see, e.g., \[49, Example 5.1\].. The control points of this fitted spline are then used as the initial guess for $\psi{(t)}$ in the optimization.

### II-D Optimization

Definition 3 (Hopf fibration)

&amp; {{\mathbf{b}}_{1} = {{\mathbf{b}}_{2} \times {\mathbf{b}}_{3}}} \\
&amp; {{\mathbf{b}}_{2} = \left( {{\mathbf{b}}_{3} \times \begin{bmatrix}
c_{\psi} &amp; s_{\psi} &amp; 0
\end{bmatrix}^{T}} \right)_{n}} \\
&amp; {{\mathbf{b}}_{3} = \overline{\mathbf{ξ}}} \\
&amp; {{\mathbf{R}}_{b}^{w} = \begin{bmatrix}
{\mathbf{b}}_{1} &amp; {\mathbf{b}}_{2} &amp; {\mathbf{b}}_{3}
&amp; {{\mathbf{b}}_{1} = \left( {\begin{bmatrix}
{- s_{\psi}} &amp; c_{\psi} &amp; 0
\end{bmatrix}^{T} \times {\mathbf{b}}_{3}} \right)_{n}} \\
&amp; {{\mathbf{b}}_{2} = {{\mathbf{b}}_{3} \times {\mathbf{b}}_{1}}} \\
&amp; {{\mathbf{b}}_{3} = \overline{\mathbf{ξ}}} \\
&amp; {{\mathbf{R}}_{b}^{w} = \begin{bmatrix}
{\mathbf{b}}_{1} &amp; {\mathbf{b}}_{2} &amp; {\mathbf{b}}_{3}
{\mathbf{q}}_{b}^{w} &amp; {= {\underset{:={\mathbf{q}}_{\mathbf{ξ}}}{\underbrace{\frac{1}{\sqrt{2{({1+{\overline{\mathbf{ξ}}}_{z}})}}}\begin{bmatrix}
\end{bmatrix}}} \circ \underset{:={\mathbf{q}}_{\psi}}{\underbrace{\begin{bmatrix}
{\mathbf{R}}_{b}^{w} &amp; {= {\text{rot}\left( {\mathbf{q}}_{b}^{w} \right)}}

$\overline{\mathbf{ξ}} \parallel \begin{bmatrix}
c_{\psi} &amp; s_{\psi} &amp; 0
\end{bmatrix}^{T}$. When ψ = 0:
$\overline{\mathbf{ξ}} \parallel \begin{bmatrix}
{- s_{\psi}} &amp; c_{\psi} &amp; 0
\end{bmatrix}^{T}$. When ψ = 0:
$\overline{\mathbf{ξ}} = \begin{bmatrix}

• Singularity=f (a,ψ) • For a given ψ, singularity appears for two $\overline{\mathbf{ξ}}$ • UAV is differentially flat, with flat outputs {p, ψ}
• Singularity=f (a,ψ) • For a given ψ, singularity appears for two $\overline{\mathbf{ξ}}$ • UAV is differentially flat, with flat outputs {p, ψ}
• Singularity=f (a) • Singularity appears for one $\overline{\mathbf{ξ}}$ • UAV is differentially flat, with flat outputs {p, ψ}

Table III: Some commonly-used definitions for the differential flatness map (a ∈ ℝ3 ∖ [0 0−g]T,ψ ∈ S1) → Rbw ∈ SO. The colormap represents the great-circle distance to the closest singularity (yellow is closer), (⋅)n denotes the normalization of a vector, and $\overline{\mathbf{ξ}}:={(\left\lbrack {{\mathbf{a}_{x}\mathbf{a}_{y}\mathbf{a}_{z}} + g} \right\rbrack^{T})}_{n}$ is the normalized relative acceleration, expressed in the world frame. See also for more possible definitions, which are usually rotations of the first two definitions of this table.

### II-D1 Coupling rotation and acceleration with the Hopf fibration

In a standard multirotor-UAV, the perpendicularity of the total thrust with respect to the plane spanned by ${\mathbf{b}}_{1}$ and ${\mathbf{b}}_{2}$ (see the coordinate frames shown in Fig. 2) makes the UAV underactuated by imposing the following constraint:

where $\overline{\mathbf{ξ}}$ is the normalized relative acceleration expressed in the world frame (see Table II). In a planning optimization problem where rotation and translation are jointly optimized, needs to be satisfied at all times. A very common way to guarantee is via direct imposition of the dynamic equations of the UAV as explicit constraints. However, these differential equations in the optimization problem typically lead to computationally-expensive problems, due to the fine sampling needed in the discretization methods (shooting or collocation).

The direct imposition of the dynamic equations can be avoided by leveraging the differential flatness map ${({{\mathbf{a} \in {{\mathbb{R}}^{3} \smallsetminus \left\lbrack {0\;0 - g} \right\rbrack^{T}}},{\psi \in S^{1}}})}\rightarrow\mathbf{R}_{b}^{w} \in {\text{SO}{}}$, which takes the acceleration $\mathbf{a}$ and $\psi$ and maps them to the rotation of the body frame. Due to the *hedgehog theorem*^44^4Also known as the *hairy ball theorem* in the literature. in $S^{2}$, this map is guaranteed to have at least one singularity when tried to be defined with a single continuous function. Several possible definitions of this differential flatness map are shown in Table III, all of which satisfy by construction. In the first two definitions, one body axis is obtained as the cross product of ${\mathbf{b}}_{3} \equiv \overline{\mathbf{ξ}}$ with a vector lying in the $xy$ world plane, and the remaining body axis is such that the resulting body frame is right-handed. These two definitions present a singularity whenever the normalized relative acceleration $\overline{\mathbf{ξ}} \in S^{2}$ is parallel to a vector defined by $\psi$ which lies in the $xy$ world plane. This means that, for a given $\psi$, the singularity appears for two $\overline{\mathbf{ξ}}$ that have a great-circle distance of $90^{\circ}$ with respect to the hovering condition. In aggressive flights, and due to numerical instabilities and artificial large changes of orientations near the singularity, this closeness between the hovering condition and the singularity can limit the set of possible accelerations for the planner.

The third definition of Table III leverages the Hopf fibration ${\mathbf{h}}{( \cdot )}$, which can be defined as a map $S^{3}\rightarrow S^{2}$ that takes a unit quaternion $\mathbf{q}$ and produces the resulting rotation of the vector ${\mathbf{e}}_{z}:=\begin{bmatrix}
\end{bmatrix}^{T}$ (see Fig. 2):

Making use now of the inverse image of the Hopf fibration, we have that ${\mathbf{q}}_{b}^{w}$ will be a composition of two rotations^55^5Note that ${\mathbf{q}}_{\psi}$, ${\mathbf{q}}_{\mathbf{ξ}}$, and ${\mathbf{q}}_{b}^{w}$ are guaranteed to be unit quaternions by construction.: ${\mathbf{q}}_{\mathbf{ξ}}$, that aligns ${\mathbf{b}}_{3}$ with $\mathbf{ξ}$, followed by ${\mathbf{q}}_{\psi}$, which is a rotation around $\mathbf{ξ}$ by an angle $\psi$. Given a specific $\mathbf{ξ}$ (with $\overline{\mathbf{ξ}} \neq {- {\mathbf{e}}_{z}}$), the quaternion ${\mathbf{q}}_{b}^{w} = {{\mathbf{q}}_{\mathbf{ξ}} \circ {\mathbf{q}}_{\psi}}$ will then be a fiber (specifically a circle) in $S^{3}$ parametrized by $\psi$. The main advantage of the Hopf fibration over the previous two definitions is that the singularity only occurs when the UAV is inverted (i.e., when $\overline{\mathbf{ξ}} = {- {\mathbf{e}}_{z}}$), which is the orientation that has the largest possible great-circle distance from the hovering configuration, and hence much less likely to happen. Although the goal of this paper is not to plan highly aggressive trajectories, and hence any of the singularities shown in Table III are unlikely to be reached, we use the Hopf map to automatically ensure the maximum distance to the singularity. Note also that, with the Hopf fibration, a second chart could be used to cover the inversion point $\overline{\mathbf{ξ}} = {- {\mathbf{e}}_{z}}$, but the use of multiple charts, while computationally cheap in the controller level or in an intermediate check step in a decoupled $\mathbf{p}$--$\psi$ optimization, would significantly increase the computation time when embedded in the $\mathbf{p}$--$\psi$ joint planning optimization. This fact, together with the improbability of an upside-down configuration as being PA optimal, led us to the inclusion of only the first chart.

Our work differs from other works that have used the Hopf fibration for UAVs as follows: Ref. uses the Hopf fibration only in a controller to track predefined trajectories. In, the Hopf fibration is used in the planner to find the charts in a step after the $\mathbf{p}$ optimization and before the $\psi$ optimization, and does not optimize $\psi$. We instead propose to embed the Hopf fibration map directly on the $\mathbf{p}$--$\psi$ *joint* optimization, as a way to directly obtain trajectories in $\text{SE}{}$ that are dynamically feasible by construction, and with the crucial advantage of not needing to explicitly impose the dynamic equations as constraints in the optimization.

### II-D2 Cost function

A PA term in the objective function should maximize the presence in the FOV of the predicted position of the obstacle $i^{\ast} \in I$. However, this alone is not enough to guarantee good PA trajectories, since a fast moving projected obstacle in the image plane may cause significant blur, which can lead to stereo matching failure and consequently tracking failure. To take into account both the presence in the FOV and the blur, we use $\frac{\text{inFOV}{( \cdot )}}{\epsilon_{1} + {\epsilon_{2}\left\| \overset{˙}{\mathbf{s}} \right\|^{2}}}$ as the running reward, where $\overset{˙}{\mathbf{s}}$ is the projected velocity in the image plane, and where $\epsilon_{1}$ and $\epsilon_{2}$ are nonnegative parameters such that ${\epsilon_{1} + \epsilon_{2}} > 0$. Note how this reward is high if the predicted position of the obstacle is in the FOV with a small projected velocity, and it is approximately zero if the predicted position of the obstacle is not in the FOV, regardless of the value of the projected velocity. The position in the image plane of the projection of the obstacle can be obtained using the pinhole camera model as ${{\mathbf{s}}{(t)}}:={\frac{f}{\left\lbrack \left( {{\overset{\sim}{\mathbf{p}}}_{i^{\ast}}{(t)}} \right)^{c} \right\rbrack_{z}}\begin{matrix}
\left\lbrack \left( {{\overset{\sim}{\mathbf{p}}}_{i^{\ast}}{(t)}} \right)^{c} \right\rbrack_{x:y}
\end{matrix}}$ (where each component of $\mathbf{s}$ is expressed in meters, not in pixels), and

As detailed in Table II, the discontinuity of the function $\text{inFOV}{( \cdot )}$ is addressed by approximating it with a sigmoid function.

In addition to the PA term explained above, we also add two terms in the cost function to maximize the smoothness in position (by minimizing jerk) and $\psi$ (by minimizing $\overset{¨}{\psi}$), and a terminal cost that penalizes the distance between $\mathbf{p}{(t_{f})}$ and $\mathbf{g}$.

### II-D3 Collision avoidance and dynamic limits constraints

For the obstacle avoidance of dynamic obstacles, we first create a polyhedral outer representation of both the trajectory of the agent and of the obstacle (see Fig. 2): For the agent, we make use of the MINVO basis (a polynomial basis that finds the simplex with minimum volume enclosing a polynomial curve) to obtain the set of control points $\left( \mathcal{Q}_{j}^{\text{MV}} \right)_{\text{agent}}$ whose convex hull encloses each segment $j$ of the agent. Similarly, for each obstacle $i$, we first compute the MINVO control points of the segment $j$ of the predicted mean $\left( \mathbf{p}_{i} \right)^{w}{(t)}$, and then we inflate it with ${{\text{norminv}{(\delta)}} \cdot {\mathbf{σ}}_{i}}\left( t_{\text{end~}j} \right)$, half of the sides the AABB (axis-aligned bounding box) of the obstacle $i$ and half of the sides of the AABB of the agent. Here, $\delta \in {\lbrack 0,1\rbrack}$ is the percentile of the standard normal distribution, and hence it encodes the desired level of conservativeness in the inflation. The resulting polyhedron is denoted as $\mathcal{C}_{ij}^{\text{MV}}$.

To ensure safety between the agent and the obstacle $i$, we then impose linear separability constraints (via planes) between $\left( \mathcal{Q}_{j}^{\text{MV}} \right)_{\text{agent}}$ and $\mathcal{C}_{ij}^{\text{MV}}$. The separating planes are found during the initial guess search for the position spline (see section II-C1), and are held fixed in the optimization. The MINVO basis is used in a similar way to impose low-conservative constraints in the velocity space. In the acceleration and jerk spaces, the MINVO control points are the same as the B-Spline control points. These constraints on $\mathbf{v}$, $\mathbf{a}$, $\mathbf{j}$, and $\overset{˙}{\psi}$ serve as a conservative approximation of the real actuator constraints of the motors of the UAV, while allowing us to reduce the complexity of the optimization problem.

### II-D4 Optimization problem

Including the initial state and the final hovering condition, the optimization problem is^66^6Time dependence of the variables in the cost function has been omitted for simplicity.:

Here, $\mathbf{x}:=\begin{bmatrix}
\mathbf{p}^{T} & \mathbf{v}^{T} & \mathbf{a}^{T} & \psi & \overset{˙}{\psi}
\end{bmatrix}^{T}$, $\left\{ \alpha_{\mathbf{j}},\alpha_{\psi},\alpha_{\text{FOV}},\alpha_{\mathbf{g}} \right\}$ are nonnegative weights, and the decision variables are the control points of the splines $\mathbf{p}{(t)}$ and $\psi{(t)}$. The degrees chosen for the splines $\mathbf{p}{(t)}$ and $\psi{(t)}$ are, respectively, 3 and 2, which are a good trade-off between computation time and dynamic feasibility for a UAV. The units of the weights are such that the corresponding term is dimensionless (see section III). An empirical method to select these weight values is as follows: First set $\alpha_{\mathbf{g}}$ to a large value to ensure that the final location is near $\mathbf{g}$. Then, $\alpha_{\text{FOV}}$, together with $\epsilon_{1}$ and $\epsilon_{2}$, are tuned to obtain a good presence of the obstacle $i^{\ast}$ in the FOV. Finally, $\alpha_{\mathbf{j}}$ and $\alpha_{\psi}$ are progressively increased to improve the smoothness of $\mathbf{p}{(t)}$ and $\psi{(t)}$, without significantly deteriorating the FOV cost.

To solve this optimization problem, we utilize the Interior Point Optimizer Ipopt ^77^7We classify an Ipopt solution as successful when Ipopt returns Solve_Succeeded (locally optimal solution) or Solved_To_Acceptable_Level (solution satisfying the acceptable tolerance level). For more details, see. interfaced through CasADi with and as the linear solvers of Ipopt. All these optimization tools were installed and run onboard the UAV in the real-world experiments (section III-B). We approximate the PA term of the cost function using the composite Simpson's rule for numerical integration.

## Results and Discussion

[] \sidesubfloat[]\sidesubfloat[]\sidesubfloat[] \sidesubfloat[]\sidesubfloat[]\sidesubfloat[]
Figure 3: (A) Projections of the obstacle onto the image plane in the single-obstacle simulation experiments. The red square is the image plane, so any projection out of this region is not in the FOV of the camera. (B) Percentage of the time the obstacle was not in the FOV but in front of the camera ( ), not in the FOV and behind the camera ( ), and in the FOV ( ). (C) Velocity of the projection of the centroid of the obstacle onto the image plane. Higher projected velocities produce larger blur in the image. (D) Number of frames for each continuous detection. (E) Corridor simulation with five dynamic obstacles following random trefoil-knot trajectories. The green pyramid represents the FOV of the camera. (F, G) Results for the corridor simulations with slow and fast obstacles, respectively. The algorithms considered are no PA ( ), PA dec ( ), ψ sweep ( ), Wang ( ), and PANTHER ( ). In the left plot of both subfigures, represents the number of infeasible stops of algorithm. The other algorithms have zero infeasible stops.

### III-A Simulation experiments

All the simulation experiments are run in an AlienWare Aurora r8 desktop running Ubuntu 20.04 and equipped with an Intel^®^ Core^TM^ i9-9900K CPU, 3.60GHz$\times$`<!-- -->`{=html}16 and 62.6 GiB. Moreover, and to focus the comparisons on the properties of the trajectories obtained by the planner, we assume, for all the algorithms benchmarked in simulation, that the UAV can perfectly track the trajectories obtained by the planner.

### III-A1 Single obstacle

We first test PANTHER in an environment with a box-shaped obstacle of size $0.2 \times 0.2 \times 0.2$ m^3^ that follows a trefoil-knot trajectory. During 60 s, the UAV is commanded to continuously fly between two different locations whose centroid is the area where the obstacle is moving. The camera has an image size of ${120 \times 120}\text{px}^{2}$, a limited FOV of $60^{\circ} \times 60^{\circ}$, and runs at a rate of $60$ Hz. The weights used for this simulation are $c_{\Psi_{\text{max}}} = 10^{6}$, $c_{\text{FOV}} = 1$, $c_{\psi} = 0$ $\text{rad}^{- 2}$, $\alpha_{\mathbf{j}} = 10^{- 6}$ $\text{s}^{5}/\text{m}^{2}$, $\alpha_{\psi} = 0$ $\text{s}^{3}/\text{rad}^{2}$, $\alpha_{\text{FOV}} = 20$, $\alpha_{\mathbf{g}} = 70$ $\text{m}^{- 2}$, $\epsilon_{1} = 0.3$, and $\epsilon_{2} = 0.45$ $\text{s}^{2}/\text{m}^{2}$. To focus this comparison on the capabilities of the planner, we let the agent perfectly know the trajectory of the obstacle in these simulations. We compare the following three approaches:

No PA: $\psi$ is held constant and only the smoothness in position and terminal goal costs are optimized. Works that do not plan $\psi$ include, e.g.,.

PA with position and $\psi$ decoupled: Translation $\mathbf{p}$ is optimized first (as in the method no PA) and then it is held fixed while $\psi$ is optimized with the PA term. We will refer to this algorithm as PA dec. This decoupling is done in, e.g.,.

PANTHER (ours): Joint optimization of $\mathbf{p}$ and $\psi$.

As will be explained in section II-D2, two important metrics that characterize a good PA trajectory are the presence of the obstacle in the FOV and the norm of the projected velocity, which quantifies the blur. The percentage of time the obstacle was in the FOV of the camera is shown in Fig. 3. PANTHER is able to keep the obstacle inside the FOV 7.9 and 1.5 times more than the algorithms no PA and PA dec, respectively. As PA dec decouples position and $\psi$ in the optimization, the UAV lacks the ability to modify the spatial path (only $\psi$) to generate a better overall trajectory.

To qualitatively show the area of the projection, we apply a Gaussian filter to the histogram of the projection of the centroid of the obstacle onto each ${10 \times 10}\text{px}^{2}$ cell of the image plane. The results are shown in Fig. 3, where we can see that PANTHER is able to keep the obstacle inside the FOV limits much better, and more frequently, than methods no PA and PA dec.

The velocity of the projection of the centroid of the obstacle onto the image plane is shown in Fig. 3, which highlights that PANTHER is able to obtain a $18$% and $34$% decrease in the mean of the norm of the projected velocity with respect to no PA and PA dec, respectively, achieving, therefore, a much less blurred projection of the obstacle than those two methods.

Finally, and as a continuous detection of the dynamic obstacle is crucial to achieve a good tracking and prediction, we show in Fig. 3 the boxplot of the number of frames of each continuous detection for the different algorithms. A continuous detection is defined as a set of consecutive frames for which the obstacle stayed in the FOV of the camera. On average, PANTHER is able to achieve continuous detections of $155$ frames, while the mean number of frames per continuous detection for methods no PA and PA dec are $39$ and $46$ frames, respectively.

### III-A2 Several obstacles

We now test PANTHER in a simulation with several obstacles. The environment consists of a corridor of length of $39$ m along the $x$ direction with five dynamic obstacles that move following random trefoil-knot trajectories, see Fig. 3. In all these simulations, the agent only has access to the size, current position, and velocity of the obstacles that are inside the FOV of the camera. The FOV of the camera is $70^{\circ} \times 70^{\circ}$, and has a sensing range of 5 m. The dynamic limits are ${\mathbf{v}}_{\text{max}} = {2.6 \cdot \mathbf{1}}$ m/s, ${\mathbf{a}}_{\text{max}} = {15.5 \cdot \mathbf{1}}$ m/s^2^, ${\mathbf{j}}_{\text{max}} = {50.0 \cdot \mathbf{1}}$ m/s^3^, and $\Psi_{\text{max}} = \pi$ rad/s. The weights used for PANTHER in these simulations are $c_{\Psi_{\text{max}}} = 10^{6}$, $c_{\text{FOV}} = 1$, $c_{\psi} = 0$ $\text{rad}^{- 2}$, $\alpha_{\mathbf{j}} = 10^{- 7}$ $\text{s}^{5}/\text{m}^{2}$, $\alpha_{\psi} = 0$ $\text{s}^{3}/\text{rad}^{2}$, $\alpha_{\text{FOV}} = 40$, $\alpha_{\mathbf{g}} = 25$ $\text{m}^{- 2}$, $\epsilon_{1} = 0.3$, and $\epsilon_{2} = 10^{- 5}$ $\text{s}^{2}/\text{m}^{2}$. The UAV is constrained to remain in $y \in {\lbrack{- 4},4\rbrack}$ m and $z \in {\lbrack{- 4},4\rbrack}$ m at all times.

For the benchmark, we use the algorithms explained before (no PA, PA dec, and PANTHER), and the two additional algorithms:

Algorithm, proposed by Wang et al. This approach is not perception aware, but $\psi$ tries to make the FOV of the camera point to the direction of travel. We will refer to this algorithm as Wang. Note also that this algorithm does not have constraints on ${\mathbf{j}}_{\text{max}}$ and that it has a different $\psi$ convention (it uses definition 1 of Table III).

$\psi$ sweep: $\psi$ follows a sinusoidal trajectory that varies in $\lbrack{- 90^{\circ}},90^{\circ}\rbrack$ as follows:

Figure 4: Computational analysis of different parts of the replanning step of PANTHER as a function of the number of obstacles. From left to right, and top to bottom: computation time of the generation of the convex hulls, number of linear programs (LPs) run by the OSA, computation time of the OSA, computation time of the nonconvex optimization, and total replanning time.

We test two scenarios with different maximum velocities of the obstacles. In the slow scenario, the obstacles move with velocities up to 2.12 m/s, while in the fast scenario, the obstacles move with velocities up to 4.07 m/s. In the results, we compare the number of collisions, infeasible stops, success rate, flight time, and flight distance. An infeasible stop happens when the drone passes instantly from a nonstop condition ($\mathbf{v} \neq \mathbf{0}$ or $\mathbf{a} \neq \mathbf{0}$) to a stop condition ($\mathbf{v} = \mathbf{0}$ and $\mathbf{a} = \mathbf{0}$). A run is considered successful if the UAV is able to reach the end of the corridor while not colliding with any of the obstacles. To make these simulations closer to real-world applications, where no prior information about the trajectories of the obstacles may be available, a simple constant velocity model is used in the predictor. The obstacles themselves are moving along trefoil-knot trajectories.

The results, for 30 different runs per algorithm, are shown in Figs. 3 and 3 for the slow and fast environments, respectively. In the slow scenario, PANTHER is able to succeed $87\%$ of the runs, while the other algorithms have a success rate below $47\%$. None of the algorithms present infeasible stops except Wang, that has a mean of 0.2 infeasible stops per run (light purple in Fig. 3). In the fast scenario, PANTHER succeeds $70\%$ of the runs, while all the other algorithms have a success rate below $27\%$. In terms of flight times and flight distances, most of the algorithms achieve very similar results in both scenarios, with a total flight time of approximately $20$ s, and an approximate total flight distance of $41$ m. The total flight distance for PANTHER is approximately $3$ m more than the rest of the algorithms. This is expected, because PANTHER has the ability to modify the spatial path to maximize the visibility of the obstacles. Even with this longer flight distance, the flight time of PANTHER is very similar (and sometimes even shorter) than the rest of the algorithms.

Figure 5: (A) Composite images of all the nine experiments. For visualization purposes, only the second half of Experiment 7 is shown. The table below every image shows the number of obstacles, flight distance, maximum velocity, maximum relative velocity (with respect to the obstacles), and flight time of each experiment. The number of obstacles is one, two, and three for the experiments 1-2, 3, and 4-9 respectively. (B) Relative distances between the agent and each one of the obstacles. Any relative distance above the dashed line guarantees safety.

Figure 6: Snapshots of the onboard camera in experiments 3 (A), 6 (B), and 9 (C). (D) Computation times for each part of a replanning step, measured on the onboard Intel® NUC i7DNK. The tracker, predictor, and the depth camera were also running on this computer at the same time these times were measured. The notation used is: CHs (convex hull computation for the polyhedral outer representations), Gp (generation of the planes and the guess for the position p (t)), Gψ (generation of the guess for ψ (t)) and Opt (Optimization time).

### III-A3 Computational analysis of the replanning step as a function of the number of obstacles

We now compare the computational cost of different parts of the replanning step of PANTHER. As the computational cost of each part highly depends on the specific position of the obstacles relative to the UAV, we perform a Monte Carlo analysis by randomly deploying obstacles (which follow trefoil-knot trajectories) in the spherical shell limited by two spheres of radii $2$ m and $5$ m. The starting location $\begin{bmatrix}
\end{bmatrix}^{T}$ m and ${\mathbf{g}}_{\text{term}} = \begin{bmatrix}
\end{bmatrix}^{T}$ m are held fixed for every replanning iteration. The number of obstacles tested are $\{ 4,\;6,\ldots,\;18,\;20\}$, and, for each number of obstacles, we run 10 simulations of $5.0$ s each. For these simulations, the UAV includes all the deployed obstacles in the planning problem (i.e., the set $I$ contains the indexes of all the obstacles deployed), and we let the UAV know the trajectory of the obstacles perfectly. The weights used are the same as the ones used in section III-A2. The results are shown in Fig. 4, where can see that the computation time required for the convex hull generation, the OSA, the optimization, and the total replanning time change approximately linearly with the number of obstacles. Similarly, the number of linear programs run by the OSA also changes approximately linearly with the number of obstacles. The average solve time of one of these linear programs is $0.09$ ms.

To obtain the $\psi$ initial guess (section II-C2), the average runtime of the Dijkstra's algorithm on the $\psi$ graph is $0.137$ ms, and the average runtime to fit a spline to the $\psi$ samples (Eq. 1) is $0.048$ ms.

These results above show the computational analysis for the different parts of the replanning step of PANTHER (convex hull computation, generation of the $\mathbf{p}{(t)}$ and $\psi{(t)}$ initial guesses, and nonconvex optimization). For the computational cost of the tracker and predictor using real point clouds, see section III-B. The well-known results regarding the complexity analysis of the Hungarian algorithm are given in.

### III-B Real-world experiments

We run an extensive set of hardware experiments, where a UAV needs to go from a starting point to a goal location while avoiding unknown dynamic obstacles. The UAV used is equipped with a Qualcomm^®^ SnapDragon Flight, an Intel^®^ NUC i7DNK, and an Intel^®^ RealSense Depth camera D435i. The tracker, planner, and the camera run on the Intel^®^ NUC, while the control and state estimation run on the Qualcomm^®^ SnapDragon Flight. Note that the main onboard computer (Intel^®^ NUC) has similar computational power to the onboard hardware used in the recent literature (e.g., ). For the controller, we run the approach presented in at 100 Hz to generate the desired orientation and angular rates from $\mathbf{p}{(t)}$ and $\psi{(t)}$. The commanded thrusts for the motors are then found from these attitude commands using a geometric controller, which is run at IMU rate (500 Hz). For state estimation, we use a visual inertial odometry (VIO) package running at 30 Hz that leverages an extended Kalman filter to fuse the IMU measurements of the SnapDragon and the images of its downward-facing camera. To obtain a high-rate state estimate, we then integrate forward the IMU (which runs at 500 Hz) between consecutive VIO estimates.

The IMU of the RealSense camera is not used. All the computation of this UAV is running onboard, and it does not have any prior knowledge of the trajectories and specific shape/size of the obstacles. The weights used for these experiments are $c_{\Psi_{\text{max}}} = 10^{6}$, $c_{\text{FOV}} = 1$, $c_{\psi} = 0$ $\text{rad}^{- 2}$, $\alpha_{\mathbf{j}} = 0.05$ $\text{s}^{5}/\text{m}^{2}$, $\alpha_{\psi} = 0.1$ $\text{s}^{3}/\text{rad}^{2}$, $\alpha_{\text{FOV}} = 1$, $\alpha_{\mathbf{g}} = {2 \cdot 10^{4}}$ $\text{m}^{- 2}$, $\epsilon_{1} = 0.1$, and $\epsilon_{2} = 1$ $\text{s}^{2}/\text{m}^{2}$.

To generate the dynamic obstacles, we use three other UAVs with a Qualcomm^®^ SnapDragon Flight, and equip them with a box-shaped frame of $\approx {0.6 \times 0.6 \times 0.3}$ m^3^. The obstacles are following trefoil-knot trajectories.

A total of 9 experiments were performed (see attached video). The composite images of the trajectories flown by the agent and by the obstacles, together with the number of obstacles, distance flown, maximum velocity, maximum relative velocity with respect to the obstacles, and total flight time of each one of the experiments are shown in Fig. 5. Experiments 1 and 2 were done with one obstacle, experiment 3 with two obstacles, and experiments 4-9 with three obstacles. The maximum velocity achieved by the agent, 5.77 m/s, happened in experiment 7. In that same experiment, the maximum relative velocity (6.28 m/s) with respect to the obstacles is also achieved. The relative distances between the UAV and the obstacles are shown in Fig. 5. Any relative distance above the dashed horizontal line guarantees safety between the agent and the corresponding obstacle. For experiments 3, 6, and 9, different snapshots of the onboard camera are shown in Figs. 6, 6, and 6, respectively. Note how the planned trajectories try to keep an obstacle in the FOV at all times to aid in obstacle tracking and prediction.

The computation times are shown in Fig. 6. All these computation times were measured onboard, with the UAV flying, and with the depth camera node and the tracker running on the same computer (Intel^®^ NUC i7DNK). The mean total replanning times are 48.70, 51.66, and 58.59 ms for the experiments with 1, 2, and 3 obstacles respectively. The point cloud of the camera is generated at $90$ Hz, and the tracker (clustering, assignment, and prediction) is able to process each point cloud in $\approx 8.6$ ms.

## Conclusion

This work derived PANTHER, a perception-aware (PA) trajectory planner in dynamic environments. PANTHER is able to couple together the translation and the full rotation in the optimization, leading to PA trajectories computed in real time that maximize the presence of the obstacles in the FOV while minimizing their projected velocity. Extensive hardware experiments in unknown dynamic environments, with all the computation running onboard, and with relative velocities of up to 6.3 m/s have shown its effectiveness.

Our approach has also some limitations. Specifically, in the hardware experiments we observed the importance of the choice of the obstacle to include in the optimization (i.e., the choice of $i^{\ast}$, see Table II and section II-B): when should the UAV include a specific (already tracked) obstacle in the PA term of the optimization, in order to predict its trajectory more accurately to be able to avoid it, and when should the UAV turn around to explore unknown space? This highlights the trade-off between exploration and exploitation: too much focus on exploitation may lead to collision with obstacles that were never detected, and too much focus on exploration may lead to a very poor trajectory prediction, and hence to a collision as well. Optimally solving this trade-off is a promising direction for future work.

Another possible direction of future work is to solve the trade-off between visibility and time optimality. This would entail adding the time minimization in the optimization problem of section II-D4, and would also allow to highlight the advantages of the Hopf fibration when flying aggressive trajectories that pass close to the singularity produced by the commonly-used maps presented in (first two definitions of Table III).

Finally, another interesting research direction is how to incorporate disturbances in the planning problem, while still guaranteeing that the tracking error of the UAV remains bounded. The incorporation of such disturbance information is especially important when flying outdoors under windy conditions, since a large deviation between the planned trajectory and the actual trajectory can provoke a collision with the obstacles.
