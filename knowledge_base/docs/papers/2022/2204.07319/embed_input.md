<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Review of Path Following Control Strategies for Autonomous Robotic Vehicles: Theory, Simulations, and Experiments

Topics include Robotics, Vehicles, Control, Frenet-serret, F-S, Parallel transport, P-T, Reference frame, MATLAB.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This article presents an in-depth review of the topic of path following for autonomous robotic vehicles, with a specific focus on vehicle motion in two dimensional space (2D). From a control system standpoint, path following can be formulated as the problem of stabilizing a path following error system that describes the dynamics of position and possibly orientation errors of a vehicle with respect to a path, with the errors defined in an appropriate reference frame. In spite of the large variety of path following methods described in the literature we show that, in principle, most of them can be categorized in two groups: stabilization of the path following error system expressed either in the vehicle's body frame or in a frame attached to a "reference point" moving along the path, such as a Frenet-Serret (F-S) frame or a Parallel Transport (P-T) frame. With this observation, we provide a unified formulation that is simple but general enough to cover many methods available in the literature. We then discuss the advantages and disadvantages of each method, comparing them from the design and implementation standpoint. We further show experimental results of the path following methods obtained from field trials testing with under-actuated and fully-actuated autonomous marine vehicles.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In addition, we introduce open-source Matlab and Gazebo/ROS simulation toolboxes that are helpful in testing path following methods prior to their integration in the combined guidance, navigation, and control systems of autonomous vehicles.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Path-following (PF) is one of the most fundamental tasks to be executed by autonomous vehicles. It consists of driving a vehicle to and maintaining it on a pre-defined path while tracking a path-dependent speed profile. Unlike trajectory tracking, the path is not parameterized by time but rather by any other useful parameter that in some cases may be the path length. Thus, there is more flexibility in making the vehicle first converge to the path smoothly then move along it while tracking a given speed assignment. Path following is useful in many applications where the main objective is to accurately traverse the path, while maintaining a certain speed is a secondary task. Stated in simple terms, it is not required for the vehicle to be at specific positions at specific instants of time, a strong requirement in trajectory tracking. All that is required is for the vehicle to go through specific points in space while trying to meet speed assignments, but absolute time is not of overriding importance. From a technical standpoint, when compared with trajectory tracking, path following has the potential to exhibit smoother convergence properties and reduced actuator activity.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For these reasons, in a vast number of applications path-following is performed by a variety of heterogeneous vehicles, of which marine vehicles \[RHJ^+^19 \], ground vehicles such as Mars rovers \[HCC^+^04 \], fixed wing aerial vehicles, autonomous cars \[GCC^+^19, S^+^09 \], and quad-rotors are representative examples.\The task of deriving control strategies to solve the PF problem is technically challenging, specially in the presence of non-holonomic constraints, and often involves the use of a nonlinear control techniques such as backstepping, feedback linearization, sliding mode control, vector field, linear model predictive control (MPC) \[RGNR^+^09, \], and nonlinear MPC (NMPC) \[GCC^+^19, \]. Other path following algorithms exploit learning-based methods such as Learning-based MPC (LB-MPC), reinforcement learning-based control, among others. Due to the proliferation of robotic vehicles and their applications, the past decades have witnessed the development of a multitude of path-following methods.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Therefore, in order to provide a critical assessment of the collective work done, this paper contains a comprehensive survey, aimed at comparing different PF methods from the design and implementation standpoint and discussing the advantages and disadvantages of each method. In particular, we show that an important classification of path-following algorithms is given by the choice of reference frame in which the path-following error is defined. In general, the latter is defined either in the vehicle's body frame or in a frame attached to a *"reference point"* moving along the path such as the Frenet--Serret (F-S) frame or the Parallel Transport (P-T) frame.\In the literature, one can find other survey papers of path following methods such as for fixed-wing aerial vehicles, for quadrotors, or autonomous car-like robot. However, the aforementioned survey papers do not describe in detail the theory that supports the methods described and, while they contain simulation results, they do not present a comparison of the performance of the methods in field tests with real vehicles.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, the above surveys focus on specific types of autonomous vehicles, and do not consider some of the unique characteristics of under-actuated marine vehicles such as non-holonomic constraints or the requirement that a vehicle track a desired speed profile along the path. In the current review paper, instead of focusing on a particular type of vehicle, we emphasize the common principle underlying path following methods, that can be applied and extended to a large class of vehicles, the simplified motion of which can be described by the same class of kinematic models. Furthermore, the present paper also provides a rigorous theoretical proof of the methods reviewed that is absent in the previous surveys. We introduce simulation toolboxes written in Matlab and ROS/Gazebo that are helpful in testing the path following methods and integrating them in guidance, navigation, and control systems. To conclude, we report experimental results with a Medusa class autonomous marine vehicles \[ABG^+^16\] that have been widely used in EU projects such as WiMust \[AMP^+^16\] and MORPH \[CBB^+^15\].

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In short, the main contributions of this paper include An in-depth review of standard path-following methods in two dimensional space (2D) explaining in detail the theoretical principles of the different methods.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A discussion of the advantages and disadvantages of each method, comparing them from the design and implementation standpoint.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A Matlab simulation toolbox and ROS/Gazebo simulation packages of path-following methods.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

A description of experimental results of field trials at sea with the Medusa under-actuated and fully-actuated robotic vehicles, followed by an assessment of the performance obtained in real-life situations.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is organized as follows. The path following problem is formulated in Section 2. Section 3 describes path following methods for under-actuated vehicles. Section 4 extends the path following methods to the case where external unknown disturbances occur. Section 5 reviews a path following method developed for fully-actuated vehicles with arbitrary heading. The implementation in Matlab and Gazebo/ROS simulation toolboxes for testing path following methods are introduced in Section 6. Experimental results with autonomous marine vehicles are presented in Section 7. Section 8 provides a discussion on advantages and disadvantages of the path following methods and practical issues when the vehicles dynamics are taken into account. Finally, Section 9 contains the main conclusions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Vehicle kinematic models", "weight": 1.0} -->

Path following refers to the problem of making a vehicle converge to and follow a spatial path while asymptotically tracking a desired speed profile along the path; see Fig. 2.1 that shows an ASV executing a path following maneuver. From a control system standpoint, the structure of a complete path following system is captured in Fig. 2.2(a). In this architecture, the outer-loop path following controller implements a guidance strategy, in charge of computing desired references (e.g. linear and angular speeds, or orientations) to steer the vehicle along the path with a desired speed profile $U_{d}$. These references act as inputs to autopilots that play the role of inner-loop controllers, in charge of generating suitable forces and torque for the vehicle in order to track the desired references, thus achieving the path following objectives.\In practice, to simplify the design of a path following controller, it is commonly assumed that the responses the inner-loops are sufficiently fast so that the influence of the latter in the complete system can be neglected.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Vehicle kinematic models", "weight": 1.0} -->

Under these ideal conditions, the path following control system can be simplified by considering the kinematics model only, as shown in Fig. 2.2(b). Our purpose in the present paper is to review the core ideas behind existing path following methods in the literature, therefore we primarily focus on those designed for the vehicle kinematics only. We then treat the effect of the inner-loops as an internal disturbances and analyze the robustness of the path following methods under these disturbances accordingly.\a) A complete path following control system b) A simplified path following system for PF controller design Figure 2.2: Path following control systems; ud: reference inputs (e.g. desired linear and angular speeds, orientations) for the autopilots; p and η: the vehicle’s position and orientation, respectively, τ: force and torque, Ud: desired speed profile that the vehicle must track.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Vehicle kinematic models", "weight": 1.0} -->

The vehicle kinematic models that will be used to derive path following control laws in the present paper will be described next. The vehicle's motion with respect to a path is illustrated Fig.2.3. The following notation and nomenclature will be used. The symbol ${\{\mathcal{I}\}} = {\{ x_{\mathcal{I}},y_{\mathcal{I}}\}}$ denotes an inertial (global) North-East (NE) frame, where the axis $x_{\mathcal{I}}$ points to the North and the axis $y_{\mathcal{I}}$ points to the East. Let $Q$ be the center of mass of the vehicle and denote by $\mathbf{p} = {\lbrack x,y\rbrack}^{\top} \in {\mathbb{R}}^{2}$ the position of $Q$ in $\left\{ \mathcal{I} \right\}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Vehicle kinematic models", "weight": 1.0} -->

Let also ${\{\mathcal{B}\}} = {\{ x_{\mathcal{B}},y_{\mathcal{B}}\}}$ be a body-fixed frame whose origin is located at $Q$. In addition, denote by $\mathbf{v} = {\lbrack u,v\rbrack}^{\top} \in {\mathbb{R}}^{2}$ the vehicle's velocity vector with respect to the fluid, measured in $\left\{ \mathcal{B} \right\}$, where $u,v$ are the surge/longitudinal and sway/lateral speeds, respectively.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Vehicle kinematic models", "weight": 1.0} -->

With the above notation, the *"general"* 3-DOF vehicle's kinematic model is described by where $\psi$ is the vehicle's heading/yaw angle and $r$ is its heading/yaw rate, $v_{cx}$ and $v_{cy}$ are components of vector $\mathbf{v}_{c} = {\lbrack v_{cx},v_{cy}\rbrack}^{\top} \in {\mathbb{R}}^{2}$ that represents the effect of external unknown disturbances (e.g. ocean current in the case of marine vehicles and wind in the case of aerial vehicles) in $\left\{ \mathcal{I} \right\}$. For the sake of clarity, in the present paper we consider the following three separate subcases of.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Scenario 1: under-actuated vehicle without external disturbances", "weight": 1.0} -->

In this scenario we assume that the vehicle is under-actuated and that the vehicle's lateral motion and external disturbances are so small so that they can be neglected, that is, making $v,v_{cx},v_{cy}$ zero we obtain We also assume that the longitudinal speed ($u$) and the heading ($\psi$) or heading rate ($r$) can be tracked with good accuracy by inner-loop controllers. Although is a significant simplification of it still captures sufficiently well the behavior of a large class of under-actuated vehicles, including unicycle mobile robots, fixed-wing UAVs undergoing planar motion \[YLC^+^21, RAF^+^15\], and a wide class of under-actuated autonomous marine vehicles (AMVs). The later include the Medusa and Delfim \[ABG^+^16\] and Charlie vehicles, for which the sway speed is in practice so small that it can be neglected.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Scenario 1: under-actuated vehicle without external disturbances", "weight": 1.0} -->

Snapshots of several vehicles mentioned above are shown in Fig.2.4. In the literature, most path following methods are proposed for the kinematic model; in accordance, a large part of this paper presented in Section 3 is devoted to their review. a) Under-actuated Medusa [ABG+16] b) Delfim [AOO+06] c) Turtlebot Burger d) X8 fixed-wing UAV [YLC+21] Figure 2.4: Under-actuated robotic vehicles

<!-- chunk {"id": "body-0020", "role": "body", "section": "Scenario 2: under-actuated vehicle with external disturbances", "weight": 1.0} -->

In this scenario the vehicle motion is influenced significantly by external disturbances that can not be neglected; however, the lateral sway is still small enough to be ignored (i.e. $v = 0$). Given these assumptions, the vehicle kinematics model is given by Note also that similar to *Scenario 1*, the vehicle is under-actuated. Path following methods developed for this model will be discussed in Section 4.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Scenario 3: fully or over-actuated vehicle", "weight": 1.0} -->

In this scenario we assume that the lateral speed is significant and can not be neglected. However, for simplicity we neglect the effect of external disturbances. With these assumptions, the vehicle kinematic model is given by In this scenario we assume further that the vehicle is fully or over-actuated in that its longitudinal and lateral speeds and heading rate can be controlled simultaneously. Fig.2.5 shows snapshots of several fully-actuated vehicles that meet these assumptions. For this scenario we are interested the path following problem in which the vehicle is not only required to follow a predefined path but also to maneuver such that its heading tracks an arbitrary heading reference. This scenario will be presented in Section 5.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Path parameterization and path frames", "weight": 1.0} -->

Let $\mathcal{P}$ be a spatial path defined in an inertial frame and parametrized by a scalar variable $\gamma$ (eg. arc-length of the path). Normally, $\gamma \in \Omega:={\lbrack a,b\rbrack}$ where ${a,b} \in {\mathbb{R}}$ are values of $\gamma$ corresponding to the points at beginning and end of the path. The position of a generic point $P$ on the path in the inertial frame $\{\mathcal{I}\}$ is described by vector At $P$, there are two frames adopted in the literature to formulate the path following problem, that is, to describe the position error between the vehicle and the path. Namely, the *Frenet--Serret* (F-S) and the *Parallel Transport* (P-T) frames that are described next.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Frenet--Serret frame,", "weight": 1.0} -->

The F-S frame is used in the path following methods described in \[KYD^+^\]. A detailed description of this frame for 3D curves can be found. In the present paper, because we only consider path following in 2D we simplify the frame for 2D curves as follows, see Fig.2.6. Formally, let be the basis vectors defining the F-S frame at the point $\mathbf{p}_{d}{(\gamma)}$ where, for every differentiable $\mathbf{f}{(x)}$, ${\mathbf{f}'{(x)}} \triangleq {\partial{{\mathbf{f}{(x)}}/{\partial x}}}$. These vectors define the unit tangent and *principle* unit normal respectively to the path at the point determined by $\gamma$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Frenet--Serret frame,", "weight": 1.0} -->

The curvature $\kappa{(\gamma)}$ of the path at that point is given by As can be seen in the formula for computing the normal vector, the main technical problem with the F-S frame is that it is not well-defined for paths that have a vanishing second derivative (i.e. zero curvature) such as straight lines or non-convex curves. The other alternative frame, called Parallel-Transport frame, overcomes this limitation and is presented next.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Parallel--Transport frame,", "weight": 1.0} -->

This frame was introduced and used for the first time in the path following method of \[KPX^+^10\]. The P-T frame is based on the observation that, while the tangent vector for a given curve is unique, we may choose any convenient arbitrary normal vector so as to make it perpendicular to the tangent and vary smoothly throughout the path regardless of the curvature.\In 2D, a simple way to define the P-T frame is as follows. First, specify the tangent basic vector t as. The second basic vector, called normal vector $\mathbf{n}_{1}$, is obtained by rotating the tangent vector $90$ degree clockwise. This, as shown, is equivalent to translating $\left\{ \mathcal{I} \right\}$ to the "reference point" $P$ and then rotating it about the z-axis by the angle The difference between the F-S frame and the P-T frame is illustrated in Fig. 2.6. With the F-S frame the normal component always points to the center of curvature thus, its direction switches at inflection points, while the P-T frame has no such discontinuities.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Parallel--Transport frame,", "weight": 1.0} -->

From a path following formulation standpoint, with the F-S frame, the path following error is not well-defined at inflection points because the cross-track error (the position error projected on the normal vector) switches sign, which is not the case with the P-T frame.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Another way of propagating a P-T frame along the path is to use the algorithm proposed. While this algorithm is general and efficient for 3D, it is unnecessarily complicated for 2D curves.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Path following formulation", "weight": 1.0} -->

With the concepts and notation described above, the path following problem is stated next, see also Fig.2.3.\Path following problem in 2D: Given the 2-D spatial path $\mathcal{P}$ described by and a vehicle with the kinematics model described, derive a feedback control law for the vehicle's inputs $(u,r)$ and possibly for $\overset{˙}{\gamma}$ or $\overset{¨}{\gamma}$ so as to fulfill the following tasks: Geometric task: steer the position error $\mathbf{e} \triangleq {\mathbf{p} - \mathbf{p}_{d}}$ s.t. where $\mathbf{p}_{d}$ is the inertial position of a *"reference point"* $P$ on the path, the temporal evolution of which can be chosen in a number of ways as discussed later.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Path following formulation", "weight": 1.0} -->

Dynamic task: ensure that the vehicle's forward speed tracks a positive desired speed profile $U_{d} = {U_{d}{(\gamma,t)}}$, i.e.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Path following formulation", "weight": 1.0} -->

In what follows, let $u_{\mathcal{P}}$ be the speed of the *"reference point"* $P$ with respect to the inertial frame, that is, Should the vehicle achieve precise path following, both the vehicle and the point $P$ will move with the desired speed profile $U_{d}$, i.e. $u = u_{\mathcal{P}} = U_{d}$. In this case the dynamics task in is equivalent to requiring where $v_{d}$ is the desired speed profile for $\overset{˙}{\gamma}$, defined by In path following, the point $P$ on the path plays the role of a *"reference point"* for the vehicle to track. This point can be chosen as the nearest point to the vehicle, i.e. the orthogonal projection of the vehicle on the path (in case it is well defined), or can be initialized arbitrarily anywhere on the path with its evolution controlled through $\overset{˙}{\gamma}$ or $\overset{¨}{\gamma}$ to achieve the path following objectives.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Path following formulation", "weight": 1.0} -->

In the latter cases, $\overset{˙}{\gamma}$ or $\overset{¨}{\gamma}$ are considered as the controlled input of the dynamics of the *"reference point"*, affording an extra freedom in the design of path following controllers.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Common principles of path following methods", "weight": 1.0} -->

Although there are a variety of path following methods described in the literature, most of them can be categorized as in Table 1. The first category includes the methods that aimed to stabilize the position error in a frame attached to a *reference point* point moving along the path (e.g. F-S or P-T frames), whereas the second category consists of the methods that aim to stabilize the position error in the vehicle's body frame. The origin of the first method can be traced back to the work of addressing the path following problem of unicycle-type and two-steering-wheels mobile robots. The core idea in this work was then adopted to develop more advanced path following algorithms. Later, we shall see that Line-of-Sight (LOS), a well-known path following method and widely used in marine craft can be categorized in this group as well. The second approach was proposed and further developed to handle the vehicle's input and state constraints.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Common principles of path following methods", "weight": 1.0} -->

Stabilizing e in path frames Stabilizing e in the body frame Table 1: Principles of path following methods

<!-- chunk {"id": "body-0034", "role": "body", "section": "Basic path following methods", "weight": 1.0} -->

In this section we study path following methods for vehicles whose motion is described by the kinematic model. In Section 4 we will extend the methods to the cases when the vehicle motion is subjected to external disturbances.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Methods based on stabilizing the path following error in the path frame", "weight": 1.0} -->

In this section we present a *"unified formulation"* that is simple but general enough to cover the path following methods. The common principle behind these methods can be summarized in two steps: step 1: derive the dynamics of the path following error between the vehicle and the path in a path frame (e.g. F-S or P-T frame) step 2: drive these errors to zero using nonlinear control techniques to achieve path following, i.e. make the vehicle converge to and move along the path with a desired speed profile.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Methods based on stabilizing the path following error in the path frame", "weight": 1.0} -->

In order to have a *unified formulation*, instead of using the F-S frame as we use the P-T frame. The main advantage of the P-T frame in comparison with the F-S frame was discussed in Section 2.2, i.e. it avoids the singularity when the path has a vanishing second derivative, e.g. concave paths. Furthermore, the approach that we describe here is different from the one in that the formulation in this section applies to any path that is not necessarily parameterized by the arc-length.\Figure 3.1: A geometric illustration of the methods in Section 3.1. P is the “reference point” that the vehicle must track to achieve path following.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Derivation of the path following error", "weight": 1.0} -->

We now derive the dynamics of the path following errors (position and possibly orientation errors) between the vehicle and the path to be stabilized in order to achieve path following. The formulation is inspired by the work and is presented next. Let $P$ be a point moving along the path that plays the role of a "*reference point*" for the vehicle to track so as to achieve path following.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Derivation of the path following error", "weight": 1.0} -->

Let $\{\mathcal{P}\}$ be the P-T frame attached to this point defined by rotating the inertial frame by angle $\psi_{\mathcal{P}}$, where $\psi_{\mathcal{P}}$ is the angle that the tangent vector at $P$ makes with $x_{\mathcal{I}}$; see Fig. 3.1. Let $\mathbf{e}_{\mathcal{P}} \triangleq {\lbrack s_{1},y_{1}\rbrack}^{\top} \in {\mathbb{R}}^{2}$ be a vector defining the position error between the vehicle and the *referene point* $P$, where $s_{1}$ and $y_{1}$ are called *along-track* and *cross-track* errors, respectively. This vector can be viewed as the position vector of the vehicle expressed in $\{\mathcal{P}\}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Derivation of the path following error", "weight": 1.0} -->

It is obvious that if $\mathbf{e}_{\mathcal{P}}\rightarrow\mathbf{0}$, then the geometrical task in the path following problem will be solved. Taking the time derivative of yields Applying Lemma 5.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Derivation of the path following error", "weight": 1.0} -->

‣ 10.1 Basic results ‣ 10 Appendix ‣ A review of path following control strategies for autonomous robotic vehicles: theory, simulations, and experiments") (in the Appendix) for the first term of the previous equation we obtain where ${S{({\mathbf{ω}}_{\mathcal{P}})}} \in {\mathbb{R}}^{2 \times 2}$ is a skew symmetric matrix parameterized by ${\mathbf{ω}}_{\mathcal{P}} = {\lbrack r_{\mathcal{P}},0\rbrack}^{\top} \in {\mathbb{R}}^{2}$ which is the angular velocity vector of $\{\mathcal{P}\}$ respect to $\left\{ \mathcal{I} \right\}$, expressed in $\{\mathcal{P}\}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Derivation of the path following error", "weight": 1.0} -->

Note that $r_{\mathcal{P}}$ satisfies the relation where $u_{\mathcal{P}}$ is the total speed of $P$ given by and $\kappa{(\gamma)}$ is the "*signed*" curvature of the path at $P$, given by Note also that if $\gamma$ is the arc-length of the path then $\left\| {\mathbf{p}_{d}'{(\gamma)}} \right\| = 1$. In this case, $u_{\mathcal{P}} = \overset{˙}{\gamma}$, i.e. the speed of the "*reference point*" equals the rate of change of the path length. Define as the orientation error between the vehicle's heading and the tangent to the path.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Derivation of the path following error", "weight": 1.0} -->

Then, Furthermore, letting $\mathbf{v}_{\mathcal{P}} \triangleq {\lbrack u_{\mathcal{P}},0\rbrack}^{\top} \in {\mathbb{R}}^{2}$ be the velocity of $P$ with respect to $\left\{ \mathcal{I} \right\}$, expressed in $\{\mathcal{P}\}$, yields Substituting and in we obtain the dynamics of the position error as Furthermore, from the dynamics of the orientation error are given by At this point, it should be clear that the geometric task in the path following problem, stated in Section 2.3, is equivalent to the problem of stabilizing the position error system, i.e. making ${\mathbf{e}_{\mathcal{P}}{(t)}}\rightarrow\mathbf{0}$ as $t\rightarrow\infty$. In what follows we will describe a number of path following methods available in the literature that solve this problem.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Derivation of the path following error", "weight": 1.0} -->

These methods are categorized in Table 2. In *Methods 1* and *3*, the "*reference point*" is chosen as the orthogonal projection of the center of mass of the vehicle on the path, thus the *along-track* error ${s_{1}{(t)}} = 0$ for all $t$. In this case, only the *cross-track* $y_{1}$ needs to be stabilized to fulfill the geometrical task. In contrast, in the other methods the "*reference point*" is initialized arbitrarily anywhere on the path and its evolution is controlled by assigning a proper law for $\overset{˙}{\gamma}$ so as to make the *cross-track* and *along-track* errors converge to zero. In all of the methods, in order to fulfill the dynamics task in the path following problem (see), the linear speed of the vehicle is assigned with the desired speed profile, i.e. $u = U_{d}$.
