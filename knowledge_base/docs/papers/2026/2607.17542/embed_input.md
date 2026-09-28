<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Accurately steering a robot to a target configuration is fundamental in engineering, yet remains challenging for nonholonomic mobile robots. Vector fields (VFs) provide a natural framework by specifying desired motion directions throughout the workspace and enabling direct integration with feedback control. However, most existing VF-based methods cannot explicitly generate trajectories satisfying curvature constraints. Actuator limits are therefore often enforced by input saturation, which may invalidate stability guarantees and degrade closed-loop performance when not considered in controller design. In addition, these methods usually ensure only asymptotic convergence without an explicit settling-time bound. To address these issues, we propose a generalized motion planning and control framework consisting of a finite-time curvature-constrained vector field (FT-C2VF) and a saturation-free control law. Depending on the motion objective, the framework drives the robot to the target configuration in finite time or through it periodically. First, the FT-C2VF is constructed using complementary gains to achieve finite-time convergence while ensuring that the curvature of its integral curves is continuous, bounded, and monotonically decreasing with the radial ratio.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Second, an almost globally C1-smooth, saturation-free controller is developed to track the FT-C2VF without Jacobian information, while keeping all control inputs within prescribed actuator limits. Third, dynamical-systems analysis establishes almost-global finite-time stability of the target equilibrium. Numerical simulations show improved performance over representative VF-based methods, and outdoor experiments on an Ackermann-steered vehicle confirm the effectiveness and robustness of the proposed approach.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Several robot motion planning tasks, including the autonomous navigation of unmanned ground vehicles, the aerial cruising of fixed-wing aircraft, and environmental monitoring by underwater vehicles, require feasible reference trajectories and corresponding control inputs to guide these robots to target configurations. However, such robots are subject to nonholonomic constraints, which typically manifest as an inability to move instantaneously in arbitrary directions, thereby limiting their maneuverability within the configuration space.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, actuator limits impose physical bounds on the kinematics of robots. For example, the maximum angular velocity of differential-drive vehicles is constrained by the rotational speed limits of their motors, whereas the minimum turning radius of the Ackermann-steered vehicle is determined by the maximum front-wheel steering angle. Similarly, the minimum turning radius of fixed-wing aircraft is restricted by the maximum achievable roll angle and flight speed, while the steering capabilities of underwater vehicles are limited by the maximum available yaw moment. These physical limits establish an upper bound on the trajectory curvature, commonly referred to as the curvature constraint. Nonholonomic constraints couple the robot's position and orientation kinematics, while curvature constraints further restrict the set of admissible trajectories, thereby increasing the complexity of motion-planning design.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Among various motion planning methods, sampling-based and search-based approaches have been extensively studied. However, these approaches typically impose significant computational overhead, and the generated trajectories often require post-processing to satisfy kinematic constraints. Geometric approaches, including Dubins curves and Reeds-Shepp curves, can produce reference trajectories with bounded curvature, but the resulting curvature is discontinuous. Moreover, such methods generally do not integrate control input design for trajectory tracking and are usually implemented in an open-loop manner, rendering them sensitive to disturbances and necessitating frequent replanning. Although some optimization-based methods offer feedback capability and can explicitly incorporate multiple constraints, they are susceptible to local minima and often incur high online computational costs. Taken together, the simultaneous presence of nonholonomic and curvature constraints exposes the limitations of these approaches, making it difficult to achieve a favorable trade-off between closed-loop robustness and computational efficiency.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, VF-based methods impose minimal computational overhead and provide closed-loop feedback through the construction of reference direction fields, making them particularly effective for handling nonholonomic constraints. An instance of a non-gradient vector field is the dipole-like VF, whose normalized form exhibits favorable finite-time convergence properties. Furthermore, this field is naturally suited for tasks requiring simultaneous position and heading planning, as illustrated in Fig. 1(a) ‣ Fig. 1 ‣ I Introduction ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots"). Building upon this foundation, subsequent studies extended this framework to unicycle models and multi-robot coordination. Additionally the dipole-like VF was generalized to three-dimensional motion planning, enabling nonholonomic robots to reach a target position with a specified heading from almost all initial states (excluding a singular set of measure zero). Nonetheless, the geometric construction of the dipole-like VF may produce unnecessarily circuitous reference trajectories, resulting in excessively long paths.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, since the target position is a singular point of the dipole-like VF, the field direction becomes ill-defined near the goal, complicating controller design and implementation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

An alternative approach that circumvents the aforementioned limitations is the guiding vector field (GVF). By superimposing the normal and tangent orthogonal vectors of a manifold, GVFs generate control inputs for robot kinematic models such as single-integrator and double-integrator models. Although initially developed for path-following tasks, GVFs can be adapted for motion planning by constructing a desired manifold (e.g., a circle ) tangent to the target configuration and designing appropriate tracking controllers (see Fig. 1(b) ‣ Fig. 1 ‣ I Introduction ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots")). Furthermore, recent research has demonstrated that singularities within GVFs can be completely eliminated through dimensional lifting. However, in contrast to the finite-time convergence properties offered by dipole-like VFs, most GVF formulations guarantee only asymptotic convergence. This implies that exact convergence of the generated trajectories to the desired manifold is achieved only as time approaches infinity, precluding an explicit settling-time guarantee and potentially limiting the temporal predictability of the motion-planning process.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fig. 1: Schematic of robot motion planning based on the dipole-like VF in (a) and the GVF in (b). Red points denote the singular points of the corresponding vector fields.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although VF-based methods are advantageous in handling nonholonomic constraints, the design of vector fields with explicit curvature guarantees remains relatively underexplored and presents substantial theoretical and practical challenges. For instance a dipole-like VF is partitioned into two regions with separate control laws. However, this partitioning introduces curvature discontinuities at the boundaries, causing discontinuous control efforts. In practice, ensuring both a bounded trajectory curvature and continuous control inputs requires the integral curves of the vector field itself to have continuous and bounded curvature. While the GVFs developed in satisfy continuity and prescribed curvature bounds, the associated control laws fail to account for actuator limitations, causing tracking deviations that may still violate curvature constraints. Therefore, to guarantee the existence of feasible control laws under curvature constraints, the vector field and the control law must be co-designed. However, existing co-design approaches still exhibit important limitations. For example, the method in constructs a bounded and continuous vector field and introduces a dynamic-gain feedback term to ensure a monotonic decrease in the orientation error. Nevertheless, it guarantees only asymptotic convergence, which can result in long convergence times in high-precision motion-planning tasks.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Therefore, it remains an open problem to design a guiding vector field and an associated control law that enable a nonholonomic robot to reach a desired configuration in finite time while maintaining continuous and bounded trajectory curvature. Addressing this problem entails at least two key challenges.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

The first challenge is the construction of a finite-time curvature-constrained vector field (FT-C2VF). Achieving finite-time convergence typically requires nonlinear terms that are non-Lipschitz near the desired manifold. Although these terms accelerate convergence, they may compromise the smoothness of the vector field and render its associated Jacobian singular (i.e., undefined or unbounded) in the vicinity of the manifold. Because the curvature of the vector field depends on the Jacobian matrix, these singularities make it difficult to guarantee continuous and bounded curvature.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

The second challenge concerns the design of the control law based on the designed vector field, which is critical for vector field tracking and the maintenance of closed-loop stability. Many existing control laws for vector field tracking incorporate feedforward terms that correspond to directional changes of the vector field. The introduction of finite-time properties may induce abrupt changes in the control inputs due to Jacobian singularities. For example, frequent jumps in the angular velocity near the desired manifold have been reported. Additionally, curvature constraints impose upper bounds on the angular velocities that depend on the linear velocities. The physical limitations of the actuators further restrict the angular velocity, which limits the ability of the robot to align with the FT-C2VF and potentially causes input saturation. Crucially, existing methods often employ input saturation to enforce curvature constraints, which may compromise theoretical stability guarantees and degrade closed-loop performance within the saturated region. Consequently, the design of a control law that guarantees almost global stability remains a critical challenge.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this article, we address the two aforementioned challenges, namely the construction of finite-time curvature-constrained vector field (FT-C2VF) and the design of control laws that ensure almost global closed-loop stability. Specifically, based on a circle manifold, we refine the original guiding vector field proposed in by introducing a carefully designed pair of complementary gains to regulate its directional changes, guaranteeing that the integral curves of the vector field converge to the desired manifold in finite time, and that their curvature remains bounded and continuous. Building upon this FT-C2VF, we jointly design a saturation-free control law that eliminates the need for feedforward terms, thereby preventing input saturation and achieving almost global closed-loop stability. Furthermore, we propose a unified motion planning framework for heterogeneous nonholonomic robots, guiding them to either converge to the target configuration in finite time or periodically pass through it.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here, we summarize the major contributions of our article.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

First, we construct a novel guiding vector field based on a circle manifold by introducing a pair of complementary gains. By appropriately selecting the radius and the associated parameter, we show that this vector field addresses the first challenge. Namely, the integral curves of the vector field, serving as the reference trajectory for the robot, converge to the circle manifold in finite time and exhibit a continuous, bounded, and monotonically decreasing curvature (see Propositions 2 ‣ Proof: ‣ Proof: ‣ III Design of Finite-Time Curvature-Constrained Vector Field ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots") and 3 ‣ Proof: ‣ Proof: ‣ Proof: ‣ III Design of Finite-Time Curvature-Constrained Vector Field ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots")). Furthermore, an analytical expression for the curvature is provided to facilitate the co-design of the vector field and the control law (see Section III).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, in contrast to conventional controllers that rely on the Jacobian information (i.e., the change rate of the vector field orientation), we propose an almost globally $C^{1}$-smooth saturation-free control law without using Jacobian information. The proposed control law guarantees bounded trajectory curvature while preventing control input saturation (see Theorem 2 ‣ IV Design of Saturation-Free Control Law and Convergence Results ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots")). Specifically, we first design a state-dependent feedback gain to generate a bounded commanded curvature, which directly dictates the actual curvature of the trajectory. In addition, a parallel-resistance structure is introduced to establish a dynamic upper bound on the linear velocity, allowing the controller to adaptively accommodate variations in trajectory curvature (see Section IV).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

Third, we rigorously establish that the closed-loop system admits an almost globally finite-time stable equilibrium under appropriate parameter design (see Theorem 3). This property holds for all initial configurations, excluding two sets of measure zero. The heading error between the robot and the vector field first vanishes in finite time, after which the robot reaches the circle manifold and converges exactly, rather than asymptotically, to the target configuration (see Theorem 4).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we carry out numerical simulations to validate the theoretical results (see Sections V-A and V-B). In addition, Monte Carlo comparisons with existing VF-based motion-planning methods demonstrate the superior performance of the proposed algorithm in terms of saturation time and the total variation of angular velocity (see Section V-C). Moreover, we conduct hardware experiments using an Ackermann-steered vehicle, achieving fast, stable, and high-precision convergence to the target configuration (see Section VI).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this article is organized as follows. Section II introduces the curvature-constrained nonholonomic kinematic model and formalizes the finite-time generalized motion planning problem as a co-design problem involving a vector field and a control law. In Section III, we present the structure of the FT-C2VF and rigorously prove its finite-time convergence while guaranteeing continuous and bounded curvature. To track the FT-C2VF, Section IV details the saturation-free control law and establishes almost-global finite-time convergence for the closed-loop system. In Section V, we validate the theoretical results through numerical simulations and provide comparisons with existing VF-based methods. Section VI further validates the framework via hardware experiments on an Ackermann-steered vehicle. Finally, Section VII concludes the article and outlines future research. Before proceeding, some standard notations and basic concepts used throughout this article are introduced.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notations: Given a positive integer $n$, we use boldface letters to denote vectors $\boldsymbol{v}\in\mathbb{R}^{n}$. The transpose and Euclidean norm of $\boldsymbol{v}$ are denoted by $\boldsymbol{v}^{\top}$ and $\|\boldsymbol{v}\|$, respectively. The symbol $:=$ denotes "is defined as". The distance between a point $\boldsymbol{p}_{0}\in\mathbb{R}^{n}$ and a nonempty set $\mathcal{A}\subseteq\mathbb{R}^{n}$ is defined as $\mathrm{dist}(\boldsymbol{p}_{0},\mathcal{A}):=\inf\{\|\boldsymbol{p}-\boldsymbol{p}_{0}\|:\boldsymbol{p}\in\mathcal{A}\}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Introduction", "weight": 1.5} -->

If $\boldsymbol{f}$ is a differentiable function of time $t$, then its time derivative is denoted by $\dot{\boldsymbol{f}}$, while the derivative of a univariate scalar function $f$ is denoted by $f^{\prime}$. The notation $f(x)=O(g(x))$ as $x\to x_{0}$ means that there exist constants $C>0$ and $\delta>0$ such that $|f(x)|\leq C|g(x)|$ for all $x$ satisfying $0<|x-x_{0}|<\delta$. Let $\mathbb{S}^{1}:=\mathbb{R}/(2\pi\mathbb{Z})$ denote the unit circle viewed as the quotient group. Whenever convenient, elements of $\mathbb{S}^{1}$ are represented by their principal values in $(-\pi,\pi]$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Introduction", "weight": 1.5} -->

Basic concepts: A point $\boldsymbol{\xi}$ satisfying $\boldsymbol{\chi}(\boldsymbol{\xi})=\mathbf{0}$ is a singular point of the vector field $\boldsymbol{\chi}:\mathbb{R}^{n}\to\mathbb{R}^{n}$ \[41, p.219\], which corresponds to an equilibrium point of the corresponding autonomous ordinary differential equation $\dot{\boldsymbol{\xi}}=\boldsymbol{\chi}(\boldsymbol{\xi})$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Introduction", "weight": 1.5} -->

A trajectory $\boldsymbol{\xi}:\left0,+\infty\right)\to\mathbb{R}^{n}$ asymptotically converges to a nonempty set $\mathcal{B}$ if for any $\epsilon>0$, there exists $T>0$ such that $\mathrm{dist}(\boldsymbol{\xi}(t),\mathcal{B})<\epsilon$ for all $t>T$ \[[42, Def. 4.1\].

<!-- chunk {"id": "body-0026", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given an initial condition $\boldsymbol{\xi}=\boldsymbol{\xi}_{0}\in\mathcal{N}$ within a domain $\mathcal{N}\subseteq\mathbb{R}^{n}$, the trajectory finite-time converges to $\mathcal{B}$ if there exists a settling-time function $T:\mathcal{N}\to\left0,+\infty\right)$ such that $\mathrm{dist}(\boldsymbol{\xi}(t),\mathcal{B})=0$ for all $t\geq T(\boldsymbol{\xi}_{0})$ \[[43, Def. 2.2\].

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-A Kinematic Modeling and Curvature Constraints", "weight": 1.0} -->

The configuration of a two-dimensional nonholonomic mobile robot is defined as $\boldsymbol{q}=[\boldsymbol{\xi}^{\top},\theta]^{\top}\in\mathcal{C}=\mathbb{R}^{2}\times\mathbb{S}^{1}$, where $\boldsymbol{\xi}=[x,y]^{\top}$ is the position, $\theta$ is the heading angle, and $\mathcal{C}$ denotes the configuration space. We define the heading and normal vectors as $\boldsymbol{d}(\theta)=[\cos\theta,\sin\theta]^{\top}$ and $\boldsymbol{n}(\theta)=[-\sin\theta,\cos\theta]^{\top}$, respectively.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-A Kinematic Modeling and Curvature Constraints", "weight": 1.0} -->

Assuming pure rolling without lateral slip, the robot is subject to the Pfaffian constraint $\boldsymbol{n}(\theta)^{\top}\dot{\boldsymbol{\xi}}=0$, i.e., the lateral velocity is zero \[44, Ch. 13.3\]. Therefore, the nonholonomic kinematics can be expressed as where the control input $\boldsymbol{u}=[v,\omega]^{\top}$ consists of the forward speed $v$ and the angular velocity $\omega$, with $v\in[v_{-},v_{+}]$, $|\omega|\leq\bar{\omega}$, $0\leq v_{-}\leq v_{+}$, and $\bar{\omega}>0$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-A Kinematic Modeling and Curvature Constraints", "weight": 1.0} -->

The trajectory curvature is mathematically defined as $\kappa=\omega/v$, where $\kappa\to\infty$ as $v\to 0$ for $\omega\neq 0$\[45, Ch. 11.5\]. To account for the aforementioned actuator limitations, we prescribe $\bar{\kappa}>0$ as the maximum allowable curvature. Accordingly, the admissible control input set of the robot is defined as Notably, the admissible set $\mathcal{U}$ is highly versatile, providing a unified representation of the kinematic requirements of heterogeneous nonholonomic robots in the following two aspects.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-A Kinematic Modeling and Curvature Constraints", "weight": 1.0} -->

1\) Maximum Angular Velocity $\bar{\omega}$: For differential drive robots, the maximum angular velocity $\bar{\omega}$ depends on the rotational speed difference between the two driving wheels. In this context, $\bar{\kappa}$ serves as a user-defined parameter satisfying $\bar{\kappa}v_{-}<\bar{\omega}$; otherwise, $\mathcal{U}$ degenerates to $[v_{-},v_{+}]\times[-\bar{\omega},\bar{\omega}]$. In contrast, Ackermann-steered vehicles and fixed-wing aircraft are subject to a physical minimum turning radius $\rho$, which imposes a curvature bound $\bar{\kappa}=1/\rho$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-A Kinematic Modeling and Curvature Constraints", "weight": 1.0} -->

In such cases, $\bar{\omega}\geq\bar{\kappa}v_{-}$ serves as a predefined upper bound for the angular velocity; otherwise, the set $\mathcal{U}$ similarly degenerates to $[v_{-},v_{+}]\times[-\bar{\omega},\bar{\omega}]$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-A Kinematic Modeling and Curvature Constraints", "weight": 1.0} -->

2\) Minimum Forward Speed $v_{-}$: Ground robots, such as differential drive robots and Ackermann-steered vehicles, can come to a complete stop, rendering $v_{-}=0$ permissible. Conversely, fixed-wing aircraft must maintain forward flight to generate sufficient lift, requiring $v_{-}>0$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-A Kinematic Modeling and Curvature Constraints", "weight": 1.0} -->

Thus, various nonholonomic robots with curvature constraints can be modeled by specifying $v_{-},v_{+},\bar{\omega}$ and $\bar{\kappa}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-B Finite-Time Generalized Motion Planning", "weight": 1.0} -->

Most VF-based motion-planning methods, such as those, only guarantee asymptotic convergence to the target configuration without providing an explicit upper bound on the convergence time. To address heterogeneous kinematic constraints uniformly and achieve finite-time convergence, we formally define the finite-time generalized motion planning (FT-GMP) problem as follows.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Problem 1 (FT-GMP problem)", "weight": 1.0} -->

Given an initial configuration $\boldsymbol{q}_{0}\in\mathcal{C}$ and a target configuration $\boldsymbol{q}_{d}\in\mathcal{C}$ with a desired terminal speed $v_{d}\in[v_{-},v_{+}]$, the objective is to design control inputs $\boldsymbol{u}=[v,\omega]^{\top}\in\mathcal{U}$ such that the trajectory $\boldsymbol{q}(t)$ of system satisfies the following two conditions.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Problem 1 (FT-GMP problem)", "weight": 1.0} -->

There exist a settling-time function $T_{a}:\mathcal{C}\to\left[0,+\infty\right)$ and a finite constant $\Delta T\geq 0$ such that for all $t\geq T_{a}(\boldsymbol{q}_{0})$, there exists at least one time instant $t^{*}\in[t,t+\Delta T]$ satisfying $\boldsymbol{q}(t^{*})=\boldsymbol{q}_{d}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Problem 1 (FT-GMP problem)", "weight": 1.0} -->

The speed matches the terminal speed whenever the trajectory $\boldsymbol{q}(t)$ reaches the target configuration $\boldsymbol{q}_{d}$, i.e., $v(t)=v_{d}$ for all $t\geq T_{a}(\boldsymbol{q}_{0})$ such that $\boldsymbol{q}(t)=\boldsymbol{q}_{d}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Problem 1 (FT-GMP problem)", "weight": 1.0} -->

This formulation unifies two representative robotic tasks by adjusting the terminal speed $v_{d}$ as follows.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Problem 1 (FT-GMP problem)", "weight": 1.0} -->

1\) Stationary Operation ($v_{d}=0$): The curvature constraint (i.e., $|\omega|\leq\bar{\kappa}|v|$) strictly enforces $\omega=0$ whenever $v=v_{d}=0$. Consequently, it follows that $\Delta T=0$, $\boldsymbol{q}(t)\equiv\boldsymbol{q}_{d}$, and $v(t)\equiv 0$ for all $t\geq T_{a}(\boldsymbol{q}_{0})$, meaning the robot remains stationary at the target configuration.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Problem 1 (FT-GMP problem)", "weight": 1.0} -->

2\) Periodic Monitoring ($v_{d}>0$): The robot passes through $\boldsymbol{q}_{d}$ at speed $v_{d}$ and revisits this configuration periodically, with the recurrence period upper-bounded by $\Delta T$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "II-C Problem Reformulation Based on Vector Field", "weight": 1.0} -->

To characterize curvature constraints on the integral curves of a vector field, we first introduce the following notion.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Problem 2 (VF-CL Co-Design problem)", "weight": 1.0} -->

(Heading Alignment): There exists a settling-time function $T_{c}:\mathcal{C}\to\left[0,+\infty\right)$ such that the heading of the robot aligns with the direction of the vector field; that is, $\theta(t)=\angle\boldsymbol{\chi}(\boldsymbol{\xi}(t))$ for all $t\geq T_{c}(\boldsymbol{q}_{0})$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Problem 2 (VF-CL Co-Design problem)", "weight": 1.0} -->

(Speed Matching): There exists a settling-time function $T_{d}:\mathcal{C}\to\left0,+\infty\right)$ such that the speed matches the terminal speed whenever the trajectory $\boldsymbol{q}(t)$ reaches the target configuration $\boldsymbol{q}_{d}$ after $T_{d}(\boldsymbol{q}_{0})$, and maintains a positive speed otherwise; that is, $v(t)=v_{d}$ for all $t\geq T_{d}(\boldsymbol{q}_{0})$ when $\boldsymbol{q}(t)=\boldsymbol{q}_{d}$, and $v(t)>0$ for all $t\geq 0$ whenever $\boldsymbol{q}(t)\neq\boldsymbol{q}_{d}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Problem [2 ‣ Proof: ‣ II-C Problem Reformulation Based on Vector Field ‣ II Problem Formulation ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots") serves as a constructive sufficient condition for solving Problem 1 ‣ II-B Finite-Time Generalized Motion Planning ‣ II Problem Formulation ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots"). This reformulation decouples the complex FT-GMP problem into sequential and tractable subtasks. C1 ensures that the heading of the robot aligns with the FT-C2VF in finite time. Upon alignment, the trajectory of the robot is governed by the vector field, which naturally guides the robot to converge to the circle manifold $\mathcal{M}_{r}$. Meanwhile, C2 guarantees a positive speed before reaching the target configuration to prevent premature stalling.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Furthermore, because $\mathcal{M}_{r}$ is a closed manifold, this continuous motion with a positive speed ensures the robot inevitably reaches $\boldsymbol{q}_{d}$, remaining stationary if $v_{d}=0$, or repeatedly passing through $\boldsymbol{q}_{d}$ if $v_{d}>0$. By default, it is assumed that $v_{d}=v_{-}$; otherwise, a new lower bound of the linear velocity can simply be defined as $v^{\prime}_{-}=v_{d}$. $\blacktriangleleft$

<!-- chunk {"id": "body-0046", "role": "body", "section": "Design of Finite-Time Curvature-Constrained Vector Field", "weight": 1.0} -->

In this section, we construct a guiding vector field based on the circle manifold in and show that it is an FT-C2VF by appropriately selecting its parameters and radius.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Design of Finite-Time Curvature-Constrained Vector Field", "weight": 1.0} -->

Without loss of generality, the coordinate frame can be translated such that the center of $\mathcal{M}_{r}$ coincides with the origin. Subsequently, the manifold can be expressed as $\mathcal{M}_{r}=\{\boldsymbol{\xi}\in\mathbb{R}^{2}:\phi(\boldsymbol{\xi})=0\}$, where the level set function $\phi:\mathbb{R}^{2}\to\mathbb{R}$ is defined as $\phi(\boldsymbol{\xi})=\|\boldsymbol{\xi}\|^{2}-r^{2}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Design of Finite-Time Curvature-Constrained Vector Field", "weight": 1.0} -->

The guiding vector field $\boldsymbol{\chi}:\mathbb{R}^{2}\to\mathbb{R}^{2}$ is designed as follows: where $\boldsymbol{E}\in SO$ is the $90^{\circ}$ rotation matrix $\left[\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right]$, and $\nabla\phi\in\mathbb{R}^{2}$ is the gradient of $\phi$ with respect to $\boldsymbol{\xi}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Design of Finite-Time Curvature-Constrained Vector Field", "weight": 1.0} -->

The *radial ratio function* $\eta:\mathbb{R}^{2}\to\left[0,+\infty\right)$ is defined as $\eta(\boldsymbol{\xi})=\|\boldsymbol{\xi}\|/r$, which ensures that $\mathrm{dist}(\boldsymbol{\xi}(t),\mathcal{M}_{r})=0$ when $\eta(\boldsymbol{\xi})=1$. Furthermore, $\psi_{\tau}:[0,+\infty)\to$ is a non-negative *tangential gain function* satisfying $\psi_{\tau}>0$, and $\psi_{\nu}:[0,+\infty)\to$ is a decreasing *normal gain function* satisfying $\psi_{\nu}=0$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Design of Finite-Time Curvature-Constrained Vector Field", "weight": 1.0} -->

For all $\eta\in\left0,+\infty\right)$, these two functions are designed to satisfy which indicates that $\boldsymbol{\xi}=\boldsymbol{0}$ is the unique singular point; that is, the singular set in this translated frame is $\mathcal{W}=\{\boldsymbol{0}\}$. Similar to classical guiding vector fields \[[26, eq. \], \[30, eq. \], \[46, eq. \], the first term of the proposed vector field is tangent to the desired manifold $\mathcal{M}_{r}$, thereby enabling the robot to move along it. The second term is perpendicular to the first, driving the robot toward the desired manifold. Consequently, the combined vector field simultaneously forces the robot to move toward and along the desired manifold. Unlike existing methods, the gain functions in our approach are specifically designed to yield a tractable analytical expression for the curvature of the vector field, as shown in Lemma 2.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Example 1", "weight": 1.0} -->

We compare two first-order scalar autonomous systems describing the evolution of a nonnegative error magnitude $e(t)\in\mathbb{R}_{\geq 0}$: the exponentially convergent system $\dot{e}=-\lambda e$ and the finite-time convergent system $\dot{e}=-\lambda e^{u}$, where $\lambda>0$ and $0<u<1$. The target is the origin, where $e(t)=0$ represents exact convergence. For a tolerance $\epsilon>0$, define the error neighborhood $\mathcal{B}_{\epsilon}:=\{e\in\mathbb{R}_{\geq 0}:e\leq\epsilon\}$. Given $e=e_{0}>\epsilon$, define the entrance time into $\mathcal{B}_{\epsilon}$ as $T_{\epsilon}:=\inf\{t\geq 0:e(s)\leq\epsilon,\ \forall s\geq t\}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Example 1", "weight": 1.0} -->

However, for a tighter tolerance $\epsilon=10^{-4}$, $T_{10^{-4}}^{\rm exp}\approx 5.76$ and $T_{10^{-4}}^{\rm ft}\approx 3.15$. Moreover, the finite-time system exactly reaches the origin at $T_{0}^{\rm ft}\approx 3.16$, whereas the exponential system never reaches it in finite time. $\blacktriangleleft$ The preceding example can be extended to practical robotic tasks. By defining the target configuration set as $\mathcal{Q}_{\epsilon}=\{\boldsymbol{q}\in\mathcal{C}:\|\boldsymbol{q}-\boldsymbol{q}_{d}\|\leq\epsilon\}$, the convergence time of the robot to $\mathcal{Q}_{\epsilon}$ is guaranteed to be upper bounded by some constant value, regardless of how small the tolerance $\epsilon$ is chosen.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Example 1", "weight": 1.0} -->

Building upon Propositions 2 ‣ Proof: ‣ Proof: ‣ III Design of Finite-Time Curvature-Constrained Vector Field ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots") and 3 ‣ Proof: ‣ Proof: ‣ Proof: ‣ III Design of Finite-Time Curvature-Constrained Vector Field ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots"), we establish the following sufficient condition for $\boldsymbol{\chi}$ to be an FT-C2VF.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Design of Saturation-Free Control Law and Convergence Results", "weight": 1.0} -->

In this section, we develop a saturation-free control law for the linear and angular velocities based on the FT-C2VF to solve Problem 2 ‣ Proof: ‣ II-C Problem Reformulation Based on Vector Field ‣ II Problem Formulation ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots"). To this end, we introduce the closed-loop autonomous system under this control strategy and derive related convergence results.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Design of Saturation-Free Control Law and Convergence Results", "weight": 1.0} -->

For a robot with configuration $\boldsymbol{q}=[\boldsymbol{\xi}^{\top},\theta]^{\top}$, where $\boldsymbol{\xi}\notin\mathcal{W}$, the heading error with respect to the FT-C2VF is defined as $\theta_{e}=\theta-\angle\boldsymbol{\chi}(\boldsymbol{\xi})$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Design of Saturation-Free Control Law and Convergence Results", "weight": 1.0} -->

Clearly, $\Xi(\boldsymbol{q})=0$ if and only if $\boldsymbol{q}=\boldsymbol{q}_{d}$; i.e., the robot configuration $\boldsymbol{q}$ coincides with the desired configuration $\boldsymbol{q}_{d}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Design of Saturation-Free Control Law and Convergence Results", "weight": 1.0} -->

To ensure that the trajectory curvature of the robot under the control input is bounded by $\bar{\kappa}$, the commanded curvature is formulated as follows: where $\kappa_{\chi}$ is the curvature of the FT-C2VF in (13 ‣ Proof: ‣ Proof: ‣ III Design of Finite-Time Curvature-Constrained Vector Field ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots")), and $k_{\omega}=\bar{\kappa}-\kappa_{\chi}>0$ is a state-dependent gain.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Design of Saturation-Free Control Law and Convergence Results", "weight": 1.0} -->

The operator $\lceil x\rfloor^{\alpha}:=|x|^{\alpha}\operatorname{sgn}(x)$ denotes the generalized fractional-power sign function with $\alpha>0$, where $\operatorname{sgn}(\cdot)$ is the signum function (i.e., $\operatorname{sgn}(x)=1$ for $x>0$, $0$ for $x=0$, and $-1$ for $x<0$).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Design of Saturation-Free Control Law and Convergence Results", "weight": 1.0} -->

Then, we have the following inequalities In, the first term ensures trajectory alignment with the integral curve of the vector field when $\theta_{e}=0$, causing the robot to move along it, while the second term provides feedback correction for heading errors. Once the commanded curvature $\kappa_{c}$ and the speed $v$ are determined, the angular velocity is given by $\omega=v\kappa_{c}$. This design decouples the geometric and temporal kinematics: the angular velocity is adaptively scaled by the speed $v$, ensuring consistent trajectory generation across varying speed profiles.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Design of Saturation-Free Control Law and Convergence Results", "weight": 1.0} -->

Fig. 2: Parallel-resistance-like structure for the adaptive speed upper bound.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Design of Saturation-Free Control Law and Convergence Results", "weight": 1.0} -->

Given $\kappa_{c}$, the speed must satisfy $v\leq\bar{\omega}/|\kappa_{c}|$ to avoid violation of the angular velocity constraint $|\omega|\leq\bar{\omega}$ when $|\kappa_{c}|$ is large. Conversely, when $|\kappa_{c}|$ is small, the speed is primarily restricted by its nominal upper bound $v_{+}$. If the kinematic velocity bounds satisfy $v_{+}>v_{-}$, an adaptive velocity upper bound is designed as Under the premise that $\bar{\kappa}<\bar{\omega}/v_{-}$, this adaptive bound gracefully accounts for variations in trajectory curvature, ensuring deceleration during sharp turns and higher speeds along gentle curves. This structure can be interpreted by analogy with parallel resistance in circuit theory \[47, Ch.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Design of Saturation-Free Control Law and Convergence Results", "weight": 1.0} -->

2.6\], as illustrated in Fig. 2. Specifically, the nominal maximum velocity $v_{+}$ and the maximum feasible turning velocity $\bar{\omega}/|\kappa_{c}|$ jointly dictate the upper bound, ensuring that $v_{r}$ is less than the minimum of $v_{+}$ and $\bar{\omega}/|\kappa_{c}|$. To achieve the motion planning objectives, we synthesize the linear and angular velocity control laws as follows: where $k_{v},\beta>0$ are constant gains. The design of the speed controller in ensures that if the robot is far from the target configuration (i.e., $\Xi\gg 0$), $v\to v_{r}$, while upon reaching the target configuration (i.e., $\Xi=0$), $v=v_{-}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Remark 2", "weight": 1.0} -->

It is worth noting that for nonholonomic mobile robots, especially Dubins car-like models described, the underlying principle of differs from most existing VF-based approaches. For example, in \[30, eq. \], \[29, eq. \], \[40, eq. \], \[31, eq. \], \[26, eq. \], \[24, eq. \], and \[32, eq. \], the angular velocity control law is deliberately designed as the sum of a feedforward and a feedback term.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The feedforward term provides the angular velocity required to follow the vector field and is usually formulated as the time derivative of the vector field direction, e.g., $\dot{\angle\boldsymbol{\chi}}=\frac{-1}{\|\boldsymbol{\chi}\|}\hat{\boldsymbol{\chi}}^{\top}\boldsymbol{E}\boldsymbol{J}(\boldsymbol{\chi})\dot{\boldsymbol{\xi}}$, where $\boldsymbol{J}(\boldsymbol{\chi})$ is the Jacobian of $\boldsymbol{\chi}$ with respect to the position $\boldsymbol{\xi}$. The feedback term compensates for the heading error $\theta_{e}$. Although such control laws enable vector field tracking, they typically do not explicitly account for curvature constraints, and thus must employ input saturation to enforce feasibility.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Moreover, under finite-time convergence requirements, the Jacobian $\boldsymbol{J}(\boldsymbol{\chi})$ may become unbounded near the desired manifold, which may render the control law infeasible. In contrast, satisfies Theorem 2 ‣ IV Design of Saturation-Free Control Law and Convergence Results ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots"), it relies only on the curvature of the FT-C2VF and does not involve the Jacobian of the vector field. $\blacktriangleleft$ To analyze the closed-loop error system, we study the evolution of the heading error $\theta_{e}$ and the radial ratio $\eta$. As detailed in Appendix B-B, the dynamics is given by Before the robot converges to the target configuration, we have $v>0$. By applying orbital equivalence in \[48, Def. 2.4\], we introduce the time reparameterization $\mathrm{d}\tau=v\mathrm{d}t$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 2", "weight": 1.0} -->

On the time scale $\tau$, can be rewritten as the following closed-loop autonomous system on the cylindrical manifold $\mathcal{H}=\mathbb{S}^{1}\times\mathbb{R}_{\geq 0}$: where $\kappa_{c}(\eta,\theta_{e})=\kappa_{\chi}(\eta)-k_{\omega}(\eta)\left\lceil\sin\theta_{e}\right\rfloor^{\alpha}$ and $k_{\omega}(\eta)=\bar{\kappa}-\kappa_{\chi}(\eta).$ We first exclude $\eta=0$ from the state space because the direction of the FT-C2VF, and hence the heading error $\theta_{e}$, is not defined at $\boldsymbol{\xi}=0$. Then, we analyze system.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The desired equilibrium point is $\boldsymbol{z}_{d}=$, corresponding to $\theta_{e}=0$ and $\eta=1$. Define $\mathcal{E}=\{\boldsymbol{z}\in\mathcal{H}:\boldsymbol{F}(\boldsymbol{z})=\boldsymbol{0}\}$. For a given equilibrium point $\boldsymbol{z}^{*}=(\theta_{e}^{*},\eta^{*})\in\mathcal{E}$, from $\dot{\eta}^{*}=0$ and, we obtain Substituting and into the condition $\dot{\theta}_{e}^{*}=0$ gives two branch equations: Here, $\eta^{*}$ is a root of the function $\Upsilon_{\pm}$, where the $\pm$ branches correspond to counterclockwise and clockwise orbital motions, respectively. We present the final stability result.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Notably, if the condition on $\gamma$ in Theorem 3 is changed to $\gamma>1$ (while other conditions of $\alpha$ and $r$ remain), the original finite-time convergence of becomes to only almost global asymptotic stability at $\boldsymbol{z}_{d}$. In the existing literature, most VF-based motion-planning algorithms for nonholonomic robots rely heavily on the Jacobian matrix of the vector field (i.e., the change rate of the vector field orientation) to derive the control law, regardless of whether curvature constraints are enforced. It remains largely unexplored whether reliable VF tracking can be achieved using solely geometric curvature feedforward and heading feedback. This work has answered this question by establishing a novel Jacobian-free control law with strict convergence guarantees while satisfying explicit curvature constraints.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Numerical Validation and Method Comparison", "weight": 1.0} -->

In this section, we verify the instability of the non-converging set and the effectiveness of the proposed algorithm using the numerical simulation groups detailed in Table I. Moreover, Monte Carlo experiments demonstrate the advantages of the proposed approach over existing VF-based motion-planning methods. For all simulations, the kinematic parameters are configured as follows: $v_{+}=1$, $\bar{\omega}=1$, $\rho=1$ and $\bar{\kappa}=1$. The parameters of the FT-C2VF are set to $\gamma=0.5$ and $r=4$, while the control law parameters are chosen as $\alpha=0.6$, $\beta=0.4$, $k_{v}=1$, and $\mu=4$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-A Instability of the Non-converging Set", "weight": 1.0} -->

In practical physical environments, disturbances such as sensor noise are inevitable. Even if the initial configuration of the robot satisfies $\boldsymbol{q}_{0}\in\mathcal{Q}_{c}$, minor perturbations force the robot out of this set, triggering the finite-time convergence property. The instability of $\mathcal{Q}_{c}$ is verified through Group 1. As illustrated in Figs. 3(a) ‣ Fig. 3 ‣ V Numerical Validation and Method Comparison ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots") and 3(c) ‣ Fig. 3 ‣ V Numerical Validation and Method Comparison ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots"), under ideal conditions without perturbations, Rob. 1, positioned at the singularity, remains stationary, whereas Rob.

<!-- chunk {"id": "body-0071", "role": "body", "section": "V-A Instability of the Non-converging Set", "weight": 1.0} -->

3, initialized at the repeller, orbits with a radius of $R=r\eta_{s}$ and a heading satisfying $\theta=\theta_{es}+\angle\boldsymbol{\chi}(\boldsymbol{\xi})$. However, when subject to minor perturbations, the corresponding robots (Rob. 2 and Rob. 4) escape these unstable states and successfully converge to the target configuration in finite time. Furthermore, Fig. 3(b) ‣ Fig. 3 ‣ V Numerical Validation and Method Comparison ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots") depicts the phase-plane trajectories governed by the closed-loop system. Theorem 3 confirms that the perturbed trajectories first converge to the forward-invariant manifold $\mathcal{P}$ at time $T_{c}$, and subsequently reach the desired equilibrium $\boldsymbol{z}_{d}$ at time $T_{d}$. Snapshots detailing the dynamic evolution of the trajectories are provided in Figs.

<!-- chunk {"id": "body-0072", "role": "body", "section": "V-A Instability of the Non-converging Set", "weight": 1.0} -->

3(d) ‣ Fig. 3 ‣ V Numerical Validation and Method Comparison ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots")--3(g) ‣ Fig. 3 ‣ V Numerical Validation and Method Comparison ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots").

<!-- chunk {"id": "body-0073", "role": "body", "section": "V-A Instability of the Non-converging Set", "weight": 1.0} -->

Fig. 4: Simulation verification of the effectiveness of the proposed algorithm. Under the proposed control law, the left panels illustrate the motion trajectories of the robots and their corresponding velocity distributions. The right panels of (a) demonstrate that each robot in Group 2 converges to the target configuration qd. The right panels of (b) show that each robot in Group 3 periodically passes through the target configuration qd with a desired velocity vd and a recurrence period of ΔT. Moreover, the heading errors θe and the position errors ∥ξ − ξd∥ of all robots converge to zero in finite time, at Tc and Td, respectively.

<!-- chunk {"id": "body-0074", "role": "body", "section": "V-B Effectiveness of the Proposed Algorithm", "weight": 1.0} -->

Group 2 and Group 3 are utilized to validate the efficacy of the proposed approach. Under the proposed motion planning algorithm, as shown in Figs. 4(a) ‣ Fig. 4 ‣ V-A Instability of the Non-converging Set ‣ V Numerical Validation and Method Comparison ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots") and 4(b) ‣ Fig. 4 ‣ V-A Instability of the Non-converging Set ‣ V Numerical Validation and Method Comparison ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots"), the configuration errors of the nonholonomic robots converge to zero, while the control inputs and trajectory curvatures remain confined within their permissible physical limits, i.e., $|\omega|\leq\min\{\bar{\omega},\bar{\kappa}v\}$ and $|\kappa|\leq\bar{\kappa}$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "V-B Effectiveness of the Proposed Algorithm", "weight": 1.0} -->

These results further validate Theorems 2 ‣ IV Design of Saturation-Free Control Law and Convergence Results ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots")--4 established in Section IV.

<!-- chunk {"id": "body-0076", "role": "body", "section": "V-C Comparison with other VF-based Methods", "weight": 1.0} -->

Same as in Section V-B The parameter notations are adopted from their respective original references.

<!-- chunk {"id": "body-0077", "role": "body", "section": "V-C Comparison with other VF-based Methods", "weight": 1.0} -->

1\) Setup: We conduct Monte Carlo simulations comparing the proposed method with four existing VF-based motion-planning algorithms. By design, only the proposed FT-C2VF and the CVF explicitly incorporate curvature constraints; the baselines (AVF, GVF, and FT-GVF) assume unconstrained kinematics. As summarized in Table II, the parameters of GVF and FT-GVF are manually tuned to ensure a fair comparison, with their vector fields also satisfying the curvature bound $\bar{\kappa}$. However, AVF remains untuned, as its formulation does not permit such curvature constraint enforcement. The evaluations are divided into two distinct scenarios: a variable-speed scenario evaluates the CVF, AVF, and FT-C2VF using an Ackermann-steered model with $v_{+}=1$ and $v_{-}=0$; in contrast, a constant-speed scenario assesses the GVF, FT-GVF, and FT-C2VF using a unicycle model with a fixed speed of $v=1$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "V-C Comparison with other VF-based Methods", "weight": 1.0} -->

To establish a standardized baseline, the target configuration is fixed at $\boldsymbol{q}_{d}=[0,r,\pi]^{\top}$, while the initial configuration $\boldsymbol{q}_{0}=[x_{0},y_{0},\theta_{0}]^{\top}$ is sampled uniformly at random from the configuration space $\mathcal{Q}_{0}=\times\times(-\pi,\pi]$ across $1000$ independent trials.

<!-- chunk {"id": "body-0079", "role": "body", "section": "V-C Comparison with other VF-based Methods", "weight": 1.0} -->

2\) Specifications: To ensure a rigorous and fair comparison, three alignment protocols are enforced across the baselines. First, to simultaneously enforce the curvature constraint, the angular velocity is limited by the saturation function $\operatorname{Sat}_{a}^{b}:\mathbb{R}\to\mathbb{R}$, defined as $\operatorname{Sat}_{a}^{b}(x)=x$ for $x\in[a,b]$, $\operatorname{Sat}_{a}^{b}(x)=a$ for $x\in(-\infty,a)$, and $\operatorname{Sat}_{a}^{b}(x)=b$ for $x\in(b,\infty)$, where $a<b$ are constants. Second, to accommodate the structural constraints of the CVF \[29, eq. \], the circle manifolds $\mathcal{M}_{r}$ are designed as The manifold-free AVF is excluded from this specific formulation.

<!-- chunk {"id": "body-0080", "role": "body", "section": "V-C Comparison with other VF-based Methods", "weight": 1.0} -->

Consequently, the actual control input is given by $\omega_{r}(t)=\operatorname{Sat}_{-\tilde{\omega}(t)}^{\tilde{\omega}(t)}\big(\omega(t)\big)$. Here, $\tilde{\omega}(t)=\bar{\kappa}v(t)$ in the variable-speed scenario, and $\tilde{\omega}(t)=\bar{\omega}$ in the constant-speed scenario. Finally, the task is considered complete if the robot configuration enters this set: $\mathcal{Q}_{\epsilon}=\big\{\boldsymbol{q}\in\mathcal{C}:\|\boldsymbol{\xi}-\boldsymbol{\xi}_{d}\|\leq\epsilon,|\theta-\theta_{d}|\leq 0.05\big\}$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "V-C Comparison with other VF-based Methods", "weight": 1.0} -->

3\) Metrics: The evaluations focus on three primary aspects: convergence performance, trajectory quality, and control performance. Convergence performance is quantified by the convergence time $T_{d}(\epsilon)$ given a specified error tolerance $\epsilon$. Trajectory quality evaluates the path lengths $L$, mean curvatures $\kappa_{a}$, and maximum curvatures $\kappa_{m}$ of both reference and actual trajectories.

<!-- chunk {"id": "body-0082", "role": "body", "section": "V-C Comparison with other VF-based Methods", "weight": 1.0} -->

The bold values represent the best performance among these algorithms.

<!-- chunk {"id": "body-0083", "role": "body", "section": "V-C Comparison with other VF-based Methods", "weight": 1.0} -->

4\) Results: The statistical results for $\epsilon=0.1$ in Fig. 5(a) and Table III reveal three notable properties of FT-C2VF. First, it outperforms the CVF method across all metrics except the mean actual curvature. Second, whereas the baseline methods enforce the curvature bound $\kappa_{m}\leq\bar{\kappa}$ via input saturation, they do so at the cost of control saturation (i.e., a high saturation time $T_{s}$). By contrast, FT-C2VF inherently satisfies the curvature constraints, maintaining $T_{s}\equiv 0$ across all trials. Third, FT-C2VF achieves the smallest median and interquartile range of the angular-velocity variation $\mathrm{TV}_{\omega}$, indicating a smoother control action. This smoothness contrasts with the pronounced input chattering observed in FT-GVF, primarily due to the singularity of the Jacobian near the desired manifold $\mathcal{M}_{r}$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "V-C Comparison with other VF-based Methods", "weight": 1.0} -->

However, curvature constraints limit the maneuverability of the robot, thereby increasing the trajectory length, which consequently leads to longer convergence times and higher control energy in the constant-speed scenario. This represents a reasonable kinematic trade-off. The resultant spatial trajectories generated by each algorithm are depicted in Fig. 5(b) to 5(f) ‣ Fig. 5 ‣ V-C Comparison with other VF-based Methods ‣ V Numerical Validation and Method Comparison ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots"). As illustrated in Fig. 6, the convergence time $T_{d}$ of FT-C2VF, AVF, and FT-GVF remains essentially insensitive to the error tolerance $\epsilon$, whereas that of CVF and GVF increases as $\epsilon$ decreases, reflecting their asymptotic convergence behavior.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Hardware Experiment Results", "weight": 1.0} -->

In this section, we conduct outdoor experiments using an Ackermann-steered vehicle to validate the effectiveness and robustness of the proposed closed-loop motion planning algorithm across different robotic platforms.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Hardware Experiment Results", "weight": 1.0} -->

Fig. 7: Experimental architecture for the Ackermann-steered vehicle.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Hardware Experiment Results", "weight": 1.0} -->

Fig. 8: Results of the multi-waypoint experiment. (a) Spatial distribution of the waypoints qdi = [ξdi⊤, θdi]⊤, i = 0, 1, …, 6 together with the average velocity heat map of the vehicle over loops 2–4. (b) Position and heading errors at each waypoint over three consecutive loops. (c) Average commanded (red) and measured (blue) control inputs. Shaded regions indicate the corresponding 1σ standard-deviation bands. Gray dashed lines denote the input limits, and the green curve denotes the heading error. (d)-(j) Vehicle trajectories for the segments WP 0→WP 1, WP 1→WP 2, WP 2→WP 3, WP 3→WP 4, WP 4→WP 5, WP 5→WP 6, and WP 6→WP 0, respectively. (k) Side view of a representative portion of the vehicle motion.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Hardware Experiment Results", "weight": 1.0} -->

In the experiment, a rear-wheel-drive Ackermann-steered vehicle with a minimum turning radius of $\rho=1.3$ m autonomously executed the FT-C2VF-based motion-planning algorithm. As illustrated in Fig. 7, the hardware setup includes a Bynav X36D Integrated Navigation System for localization and heading estimation, alongside a TZTEK GEACX1 onboard computer. This computer publishes the forward speed $v$ and the front-wheel steering angle $\delta$ to the chassis via Robot Operating System (ROS). The steering angle is mapped to the angular velocity via $\omega=\frac{v}{L}\tan\delta$, where the wheelbase is $L=0.66$ m.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Hardware Experiment Results", "weight": 1.0} -->

Our algorithm runs at a fixed frequency of 50 Hz, and all relevant data, including control commands $\boldsymbol{u}_{cmd}=[v_{cmd},\omega_{cmd}]^{\top}$ and measured chassis states $\boldsymbol{u}_{act}=[v_{act},\omega_{act}]^{\top}$, are recorded locally at 1000 Hz.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Hardware Experiment Results", "weight": 1.0} -->

Since the tracking error in a practical discrete system cannot strictly converge to zero, local smoothing is applied to prevent the fractional-power term from inducing singularities at $\theta_{e}=0$. We introduce a continuous function $h_{\epsilon}(\sin\theta_{e})$ to replace the nonlinear feedback $\sin\theta_{e}$, defined as where $\epsilon_{d}=0.08$. Thus, the commanded curvature becomes $\kappa_{c}=\kappa_{\chi}-k_{\omega}h_{\epsilon}(\sin\theta_{e})$. To generate control inputs that initialize from zero, we modify the linear velocity control law to $v_{cmd}=v_{r}(1-e^{-0.45t})(1-e^{-k_{v}\Xi^{\beta}})$, where $t$ is the runtime.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Hardware Experiment Results", "weight": 1.0} -->

The experiment involves seven waypoints as shown in Fig. 8(a), denoted by WP $i$ ($i=0,1,\dots,6$), where the configuration of the $i$-th waypoint is defined as $\boldsymbol{q}^{i}_{d}=[\boldsymbol{\xi}_{d}^{i\top},\theta^{i}_{d}]^{\top}$, with WP 0 being the initial configuration.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Hardware Experiment Results", "weight": 1.0} -->

We consider convergence to WP $i$ achieved if the vehicle state satisfies $\boldsymbol{q}\in\mathcal{Q}^{i}_{\epsilon}=\big\{\boldsymbol{q}\in\mathcal{C}:\|\boldsymbol{\xi}-\boldsymbol{\xi}^{i}_{d}\|\leq 0.05\text{m},|\theta-\theta^{i}_{d}|\leq\frac{\pi}{180}\text{ rad}\big\}$. Upon reaching a waypoint, the vehicle pauses for $2~\mathrm{s}$ before proceeding to the next waypoint. The vehicle executes four consecutive loops, traversing the sequence WP 0 $\to$ WP 1 $\to\dots\to$ WP 6 $\to$ WP 0. Since the system initializes directly at WP 0, the tracking error at WP 0 during the first loop is zero.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Hardware Experiment Results", "weight": 1.0} -->

To accurately assess the position and heading errors across all waypoints, we discard the data from the first loop and restrict our analysis to the second through fourth loops.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Hardware Experiment Results", "weight": 1.0} -->

The experimental results are presented in Fig. 8. Due to measurement noise, motor response delay, and unmodeled dynamics, minor deviations exist between $\boldsymbol{u}_{cmd}$ and $\boldsymbol{u}_{act}$. As observed in Fig. 8(c), $v_{cmd}$ exhibits continuous fluctuations at high speeds. This phenomenon occurs because the elevated speeds cause $|\kappa_{c}|$ to fluctuate frequently near zero, thereby inducing oscillations in (21a). Nevertheless, despite these real-world disturbances at a maximum speed approaching $5~\mathrm{m/s}$, the vehicle consistently converges to each configuration waypoint with bounded trajectory curvature and without control input saturation, as depicted in the snapshots across Fig. 8(d) to 8(k) ‣ Fig. 8 ‣ VI Hardware Experiment Results ‣ Finite-Time Curvature-Constrained Vector Field for Saturation-Free Motion Planning of Nonholonomic Robots").

<!-- chunk {"id": "body-0095", "role": "body", "section": "Hardware Experiment Results", "weight": 1.0} -->

Furthermore, Fig. 8(b) shows that the average position and heading errors are merely $0.039~\mathrm{m}$ and $0.35^{\circ}$, respectively, which further validates the effectiveness and robustness of the proposed method in hardware implementations.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Additional experiments conducted with a maximum linear velocitiy of $v_{+}=4$ m/s show that reducing $v^{+}$ decreases the fluctuation amplitude of $v_{cmd}$. Furthermore, although the proposed algorithm theoretically eliminates chattering caused by vector field Jacobian singularities, the finite-time convergent controller may still induce high-frequency oscillations when implemented on discrete-time hardware. This observation motivates replacing the original nonlinear feedback term with a continuous approximation, which suppresses the oscillations caused by the unbounded feedback gain as $\theta_{e}\to 0$ and thereby improves the practical implementability of the controller. $\blacktriangleleft$

<!-- chunk {"id": "body-0097", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this paper, we have proposed a new framework that jointly develops the FT-C2VF approach and a saturation-free control law to solve the finite-time generalized motion planning problem for curvature-constrained nonholonomic robots. The proposed method not only guarantees almost-global finite-time convergence of the robot to the desired configuration but also ensures the well-posedness and effectiveness of the closed-loop system at all times, since the control inputs remain within their prescribed bounds, so saturation does not compromise system stability. The effectiveness of the theoretical results has been validated through numerical simulations, comparative experiments, and outdoor experiments on an Ackermann-steered vehicle.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Our work opens up several directions for future research. 1) While $\mathcal{M}_{r}$ is defined as a circle in this study, future efforts could extend it to arbitrary manifolds, thereby facilitating curvature-constrained navigation for more complex tasks. 2) To address collision avoidance under curvature constraints, two potential approaches warrant exploration: (i) constructing composite vector fields (e.g., see ); and (ii) incorporating high-order control barrier functions. 3) Although the current experiments are based on the planar Dubins-car kinematic model, extending the FT-C2VF planning framework to full six-degree-of-freedom models in 3D space remains a compelling subject for further investigation.
