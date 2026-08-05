<!-- arxiv-full-text:v1 {"arxiv_id": "2205.08454", "source": "ar5iv"} -->

## Introduction

Robots increasingly populate dynamic environments. Imagine a robot operating alongside customers in a supermarket. It is requested to perform different tasks, such as cleaning the floor or picking a wide range of products. These different manipulation tasks may vary in their dimension and accuracy requirements, e.g. rotation around a suction gripper does not need to be specified while two-finger grippers require full poses. Thus, it is important for motion planning algorithms to support various goal definitions. Further, the robot is operating alongside humans, it has to constantly react to the changing environment and consequently update an initial plan. As customers move fast, the adaptations must be computed in real time. Therefore, motion planning is often divided into global motion planning and local motion planning, which we will refer to as motion generation in this paper. A global planner generates a first feasible path that is used by a motion generator as global guidance. This paper proposes a novel approach to motion generation, that deals with a variety of different goal definitions.

Motion generation is often solved by formulating an optimization problem over a time horizon. The popularity of this approach is partly thanks to the guaranteed collision avoidance and thus safety. The optimization problem is then assembled from a scalar objective function, encoding the motion planning problem (e.g., the desired final position, path constraints, etc.), the transition function, defining the robot's dynamics, and several inequality constraints, integrating physical limits and obstacle avoidance.

Figure 1: Dynamic fabrics for path (green) following with a non-holonomic mobile manipulator. Dynamic fabrics control all actuators simultaneously to follow the end-effector path while keeping a given orientation and avoiding collision with the environment.

Despite abundant applications of such optimization-based approaches to mobile robots, the computational costs limit applicability when dealing with high-dimensional configuration spaces. Data-driven approaches to speed up the optimization process usually come with reduced generalization abilities, loss of formal guarantees and require prior, often costly, data acquisition. Moreover, due to the scalar objective function, the user must carefully weigh up different parts of the objective function. As a consequence, optimization-based approaches are challenging to tune and inflexible to generic motion planning problems with variable goal objectives.

In the field of geometric control, namely Riemannian motion policies (RMP) and optimization fabrics, all individual parts of the motion planning problem are formulated as differential equations of second order. Applying operations from differential geometry, the individual components are combined in the configuration space to define the resulting motion. This allows to iteratively design the motion of the robot while maintaining explainability over the resulting motion.

These works on optimization fabrics, but also on predecessors, such as RMP and RMP-Flow, have shown the power of designing reactive behavior as second-order differential equations. However, integration of dynamic features, such as moving obstacles and path following, have not been proposed nor have the framework been applied to non-holonomic systems. In this article, we exploit relative coordinate systems in the framework of optimization fabrics by introducing the dynamic pullback operation (Eq. 8). This generalization can then integrate moving obstacles and path following. We show that our generalization maintains guaranteed convergence for path following tasks and improves collision avoidance with moving obstacles. Moreover, we propose a method to incorporate non-holonomic constraints. Lastly, we compare a trajectory optimization formulation, namely a model predictive control formulation, with optimization fabrics to provide the reader with a better understanding of key differences between the two approaches. We analyze computational costs and the quality of resulting trajectories for different robots. Several simulated results and real-world experiments show the practical implications of Dynamic Fabrics ([DF]). The contributions of this paper can be summarized as: We enable the usage of optimization fabrics for dynamic scenarios. Specifically, we propose time parameterized differential maps using up-to second-order predictor models. As a consequence, this enables the integration of moving obstacles and path following tasks.

We extend the framework of optimization fabrics to non-holonomic robots.

We present a quantitative comparison between model predictive control and optimization fabrics. The results reveal that fabrics are an order of magnitude faster, more reliable, and easier to tune for goal-reaching tasks with a robotic manipulator in static environments.

All findings are supported by extensive experiments in both simulation and real-world with a manipulator, a differential drive robot, and a mobile manipulator.

## Related Work

In dynamic environments, global planning methods are not sufficient due to low planning frequencies. Thus, local motion generation methods, like the one presented in this work are employed. These methods typically require guidance to avoid local minima and thus effectively solve planning problems.

### II-A Task constrained global motion planning

Motion planning problems are usually defined by goals in arbitrary task spaces, such as the 3D Euclidean space or end-effector poses. In this context, tasks can be regarded as constraints to the motion planning problem. Conventional approaches to motion planning rely on inverse kinematics to transform task constraints into sets of configurations. The resulting global motion planning problem is then often solved using sampling-based methods.

Sampling-based motion planners generate random configurations until a valid path between an initial configuration and a set of goal configurations is found. Several methods have been proposed to directly integrate task constraints into the sampling phase. proposed a method to iteratively push a random sample to the manifold adhering to the task constraint. The notion of task constraints was later extended to task space regions to define soft constraints for individual task components. proposed scalar-valued functions to represent task constraints for sampling-based planning. As all of the above-mentioned methods rely on implicitly constrained sampling in the joint space, they exhibit high computational time, which is especially harmful to real-world applications and require local motion generation methods for path following and execution in dynamic environments. In the next subsection, recent developments in local motion planning are summarized.

### II-B Receding-horizon trajectory optimization

Methods formulating motion generation as an optimization problem with a finite discrete time horizon are known under the name of receding-horizon trajectory optimization. In line with most literature in robotics, we will refer to such methods as Model Predictive Control ([MPC]). Generally, several objectives are encoded in the scalar cost function, dynamics are formulated as equality constraints and inequality constraints ensure collision avoidance and joint limit avoidance. The dynamics for this problem can include the full dynamics model or simple integrating schemes. By explicitly solving the constrained optimization problem, this approach yields formal guarantees on stability. Stability for [MPC] is proven by formulating an appropriate Lyapunov function and showing that the finite time-horizon formulation with an appropriate terminal cost results in the same stability as the corresponding infinite time-horizon formulation. [MPC] has been applied to various robotic systems in dynamic environments, such as drones, mobile robots, and mobile manipulators. Despite these results, formal stability guarantees in such environments are challenging as appropriate terminal cost functions are often not computable or too conservative. Besides, the computational costs scale with the degrees of freedom restricting real-time applicability to simple dynamics and environment models.

Some [MPC] formulations are non-linear and can be analyzed using methods from non-linear control. When analyzing non-linear control system, Riemannian energies lead to more detailed stability results than Lyapunov functions. By investigating the variation around the generated trajectory and its contracting towards the desired trajectory, some control designs show exponential stabilizing properties. These findings have been applied to tracking control problems.

### II-C Riemannian motion policies and fabrics

Based on the findings of contracting metrics for non-linear control design, geometric control approaches design the motion generation such that convergence is inherent to the problem formulation rather than imposing them on the solution process. Practically, individual constraints to the motion planning problem shape the optimization manifold so that the solution is accessible through the solution of simple differential equation. An example for shaping the optimization manifold is seen in Fig. 2.

Figure 2: Combining different avoidance behaviors using optimization fabrics. The components defining collision avoidance with single obstacles (a,b) are combined in (c). Obstacles are shown in black. Trajectories of the point robot are shown in blue.

Realizing this concept, Riemannian motion policies (RMPs) represent a natural way of combining multiple policies into one joined policy. RMPs define individual sub-tasks of the motion planning as differential equations (spectral semi sprays or specs for short) of second order and propose the pullback and summation operators to combine multiple policies in the configuration space. As subtasks can be defined in arbitrary manifolds of the configuration space, RMP generalize operational space control. The resulting behavior of RMP was reported to be intuitive while keeping computational costs low. The concept of RMP was used in to form RMP-Flow, a motion planning algorithm that is shown to be conditionally stable and invariant across robots. In RMP-Flow, individual tasks are represented as a pair of a motion policy and a corresponding metric defining the importance of individual directions. An RMP adaptation was proposed for non-holonomic robots . By incorporating the kinematic constraint into the root equation of the RMP, the computed policy is applicable to non-holonomic robots. Besides, that work proposed a neural net to learn the collision avoidance task components.

Although RMPs have proven to be a powerful tool for motion generation, it was reported to require intuition and experience during tuning. Optimization fabrics with Finsler structures as metric generators simplify the motion design as the conditions for stability and convergence are inherent to the definition of Finsler structures. Opposed to RMPs, where the metric is typically user-defined, fabrics derive Finsler metrics from artificial energies, similar to approaches from control design using the Euler-Lagrange-Equation from geometric mechanics. Although fabrics generalize the concept of RMPs and make it accessible to a broader audience by decreasing the intuition and expertise required, they have not yet been applied to a wide range of robots.

The reason for this lack of application of fabrics is twofold. First, all the above mentioned methods are reactive and highly local methods, thus making them prone to local minima. As RMPs and optimization fabrics do not incorporate path following, integration of global planning to overcome local minima is not possible to this date. Second, fabrics and RMP do not make use of velocity estimates of obstacles but rely purely on their high reactivity in dynamic environments. As for other trajectory optimization techniques, motion estimates could benefit fabrics (and RMP) to result in even smoother motion and allow applications in such environments.

In this paper, we address these issues by proposing time parameterized differential maps to form Dynamic Fabrics. This generalization integrates path following and velocity estimates of moving obstacles. Together with the extension to non-holonomic robots, our method allows to deploy the promising theory of optimization fabrics to mobile manipulators, operating in dynamic environments.

## Background

In the previous section, we have highlighted that optimization fabrics represent a powerful tool for reactive motion generation. Since we generalize this concept, this section aims at familiarizing the reader with key findings on optimization fabrics and recalling some of the basic notations known from differential geometry. We first give an overview on how optimization fabrics are used for motion generation and how the components are derived and composed. Then the theoretical foundations are summarized .

### III-A Motion generation using optimization fabrics

When using optimization fabrics for motion generation, all components including constraints and goal attraction are designed as second order differential equations. If specific design rules for these equations are respected, all components can be combined to form a converging motion generator. Specifically, the following steps are performed: Design path-consistent geometries in suited manifolds of the configuration space (Eq. 7).

Design corresponding Finsler energies defining the importance metric in this manifold (Section III-F).

Energize all geometries with the associated Finsler energies (Section III-F).

Pull back the energized systems into the configuration space and sum them (Section III-D).

Force the combined system with a differentiable potential. As a composition of optimization fabrics, the resulting trajectory converges towards the potential's minimum (Section III-E).

In the following, we introduce the reader to the theory of optimization fabrics and recall important findings .

### III-B Configurations and task variables

We denote ${\mathbf{q}} \in \mathcal{Q} \subset {\mathbb{R}}^{n}$ a configuration of the robot with $n$ its degrees of freedom; $\mathcal{Q}$ is the configuration space of the generalized coordinates of the system. Generally, ${\mathbf{q}}{(t)}$ defines the robot's configuration at time $t$, so that $\overset{˙}{\mathbf{q}}$, $\overset{¨}{\mathbf{q}}$ define the instantaneous derivatives of the robot's configuration. Similarly, we assume that there is a set of task variables ${\mathbf{x}}_{j} \in \mathcal{X}_{j} \subset {\mathbb{R}}^{m_{j}}$ with variable dimension $m_{j} \leq n$. The task manifold $\mathcal{X}_{j}$ defines an arbitrary manifold of the configuration space $\mathcal{Q}$ in which a robotic task can be represented. Further, we assume that there is a differential map $\phi_{j}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m_{j}}}$ that relates the configuration space to the $j^{th}$ task space. For example, when a task variable is defined as the end-effector position, then $\phi_{j}$ is the positional part of the forward kinematics. On the other hand, if a task variable is defined to be the joint position, then $\phi_{j}$ is the identity function. In the following, we drop the subscript $j$ in most cases for readability when the context is clear.

In this work, we assume that $\phi$ is smooth and twice differentiable so that the Jacobian is defined as or ${\mathbf{J}}_{\phi} = {\partial_{\mathbf{q}}\phi}$ for short. Thus, we can write the total time derivatives of $\mathbf{x}$ as

### III-C Spectral semi-sprays

Inspired by simple mechanics (e.g., the simple pendulum), the framework of optimization fabrics designs motion generation as second-order dynamical systems $\overset{¨}{\mathbf{x}} = {\pi{({\mathbf{x}},\overset{˙}{\mathbf{x}})}}$. While higher-order systems seem feasible, their implementation on robots is much more challenging, as higher order configuration space derivatives would be required. The trajectory generator is defined by the differential equation ${{{\mathbf{M}}\overset{¨}{\mathbf{x}}} + {\mathbf{f}}} = 0$, where ${\mathbf{M}}{({\mathbf{x}},\overset{˙}{\mathbf{x}})}$ and ${\mathbf{f}}{({\mathbf{x}},\overset{˙}{\mathbf{x}})}$ are functions of position and velocity. Besides, $\mathbf{M}$ is symmetric and invertible. Such systems $\mathcal{S} = ({\mathbf{M}},{\mathbf{f}})_{\mathcal{X}}$ are known as spectral semi-sprays, or specs for short. When the space of the task variable is clear from the context, we drop the subscript. Then, the trajectory is computed as the solution to the system $\overset{¨}{\mathbf{x}} = {- {{\mathbf{M}}^{- 1}{\mathbf{f}}}}$.

### III-D Operations on specs

Next, the two fundamental operations for specs, transformation between spaces and summation, are introduced.

Given a differential map $\phi:{\mathcal{Q}\rightarrow\mathcal{X}}$ and a spec $({\mathbf{M}},{\mathbf{f}})_{\mathcal{X}}$, the pullback is defined as The pullback allows converting between two distinct manifolds (e.g. a spec could be defined in the robot's workspace and being pulled into the robot's configuration space using the pullback with $\phi$ being the forward kinematics).

For two specs, $\mathcal{S}_{1} = \left( {\mathbf{M}}_{1},{\mathbf{f}}_{1} \right)_{\mathcal{X}}$ and $\mathcal{S}_{2} = \left( {\mathbf{M}}_{2},{\mathbf{f}}_{2} \right)_{\mathcal{X}}$, their summation is defined :

### III-E Optimization fabrics

Optimization fabrics form a special class of specs, and thus they inherit their properties, specifically the previously defined operations of summation and pullback. First, let us introduce a finite and differentiable potential function ${\mathbf{ψ}}{({\mathbf{x}})}$ defined in a task manifold $\mathcal{X}$. Then, the modified spec $\mathcal{S}_{\mathbf{ψ}} = \left({\mathbf{M}},{{\mathbf{f}} + {\partial_{\mathbf{x}}{\mathbf{ψ}}}} \right)$ is called the forced variant of $\mathcal{S} = ({\mathbf{M}},{\mathbf{f}})_{\mathcal{X}}$. Only if the trajectory ${\mathbf{x}}{(t)}$ generated by the forced spec converges to the minimum of $\mathbf{ψ}$, the spec is said to form an optimization fabric. When the spec only converges to the minimum when equipped with a damping term, $\left({\mathbf{M}},{{\mathbf{f}} + {\partial_{\mathbf{x}}{\mathbf{ψ}}} + {{\mathbf{B}}\overset{˙}{\mathbf{x}}}} \right)$, it forms a frictionless fabric \[9, Definition 4.4\]. Note that the mechanical system of a pendulum forms a frictionless fabric, as it optimizes the potential function defined by gravity when being damped (i.e., it eventually comes to rest at the configuration with minimal potential energy) In the following, methods to construct optimization fabrics, or fabrics for short, are summarized: the definitions of conservative fabrics and energization are introduced.

### III-F Conservative fabrics and energization

While the previous subsection defined what criteria are required for a spec to form an optimization fabric, the theory on conservative fabrics and energization offers a simple way of generating such special specs. As a full summary of the theory on optimization fabrics and their construction is out of scope here, this subsection only provides an outline of the theory and the reader is referred to for detailed derivations.

In the context of fabrics, the term energy describes a scalar quantity that changes as the system evolves over time. Although this quantity has a physical meaning in natural systems (e.g., kinetic energy), it can be arbitrarily defined for motion generation. Generally, specs and optimization fabrics do not conserve an energy, but when they do, we call them conservative specs. A stationary Lagrangian \[9, Definition 4.11\] is one definition for an energy for which the corresponding spec, known as the Lagrangian spec $\mathcal{S}_{\mathcal{L}_{e}} = \left( {\mathbf{M}}_{\mathcal{L}_{e}},{\mathbf{f}}_{\mathcal{L}_{e}} \right)$, is obtained by applying the Euler-Lagrange equations. Importantly, Lagrangian specs conserve energy and do thus belong to the class of conservative specs. It was proven that an unbiased (\[9, Definition 4.11\]) Lagrangian spec forms a frictionless fabric \[9, Proposition 4.18\]. Such fabrics are analogously called conservative fabrics. There are two classes of conservative fabrics: Lagrangian fabrics (i.e., the defining energy is a Lagrangian) and the more specific subclass of Finsler fabrics (i.e., the defining energy is a Finsler structure \[9, Definition 5.4\]).

The operation of energization transforms a given differential equation into a conservative spec. Specifically, given an unbiased energy Lagrangian $\mathcal{L}_{e}$ with boundary conforming ${\mathbf{M}}_{\mathcal{L}_{e}}$ \[9, Definition 4.6\] and lower bounded energy $\mathcal{H}_{e}$, an unbiased spec of form $\mathcal{S}_{\mathbf{h}} = {({\mathbf{I}},{\mathbf{h}})}$ is transformed into a frictionless fabric using energization as where ${\mathbf{P}}_{\mathcal{L}_{e}} = {{\mathbf{M}}_{\mathcal{L}_{e}}\left({{\mathbf{M}}_{\mathcal{L}_{e}}^{- 1} - \frac{\overset{˙}{\mathbf{x}}{\overset{˙}{\mathbf{x}}}^{T}}{{\overset{˙}{\mathbf{x}}}^{T}{\mathbf{M}}_{\mathcal{L}_{e}}\overset{˙}{\mathbf{x}}}} \right)}$ is an orthogonal projector. Energized specs maintain the energy of the Lagrangian and generally change the trajectory of the underlying spec $\mathcal{S}_{\mathbf{h}}$. However, if $\mathcal{S}_{\mathbf{h}} = {({\mathbf{I}},{\mathbf{h}})}$ is homogeneous of degree 2, the energizing Lagrangian is a Finsler structure, the resulting energized spec forms a frictionless fabric for which the trajectory matches the original trajectory of $\mathcal{S}_{\mathbf{h}}$. We refer to energized fabrics with that property as geometric fabrics. Geometric fabrics form the building blocks for motion generation with optimization fabrics. Practically, energization equips the individual components of the planning problem with a metric when being combined with other components.

### III-G Experimental results fabrics

The theory explained above was tested on several simple kinematic chains . As fabrics design motion as a summation of several differential equations, each representing a specific constraint to the motion, it is possible to sequentially design motion. This procedure allows to carefully tune individual components without harming the others. The application to a planar arm in a goal-reaching setup was successfully tested . Here, the authors illustrated how the resulting motion can be modified arbitrarily by the user by adding additional constraints or preferences.

Although important concepts and findings on optimization fabrics were summarized in this section, we refer to for a more in-depth presentation of optimization fabrics. In the following, we generalize the framework of optimization fabrics to dynamic settings.

## Derivation of dynamic fabrics

We extend the framework of optimization fabrics to Dynamic Fabrics ([DF]). including dynamic environments and path following tasks. We prove that [DF] converge to moving goals and can be combined with previous approaches in geometric control. This section first introduces the notion of reference trajectory, dynamic Lagrangians and the dynamic pullback. These notations allow then to formulate [DF]. As [DF] generalize the concept of optimization fabrics to dynamic scenarios, we refer to the non-dynamic fabrics as Static Fabrics ([SF]) to explicitly distinguish between the work presented in and our work.

### IV-A Motion design using dynamic fabrics

The method explained in this paper generalizes the concept of [SF] from and can then be extended from the procedure outlined in Section III-A.

Design path-consistent geometries in a suited, time-parameterized (Definition IV.2) manifold of the configuration Design corresponding Finsler energies defining the importance metric in this manifold.

Energize all geometries with the associated Finsler energies.

If necessary, pull back the energized system from the time-parameterized manifold into the corresponding fixed manifold (Eq. 8).

Pull back the energized system into the configuration space and combine it with all components using summation.

Force the system with a time-parameterized potential. As a composition of [DF], the resulting trajectory converges towards the potential's minimum (Lemma IV.11. ‣ IV-E Dynamic fabrics ‣ IV Derivation of dynamic fabrics ‣ Dynamic Optimization Fabrics for Motion Generation")).

In the following, we explain our proposed changes to the framework of [SF] so that it remains valid in dynamic environments.

### IV-B Reference trajectories

To enable the definition of dynamic convergence and dynamic energy we introduce a reference trajectory that remains inside a domain $\mathcal{X}$ as boundary conforming. This term is chosen in accordance to \[9, Definition 4.6\].

### Definition IV.1

A reference trajectory $\overset{\sim}{\mathbf{x}}{(t)}$, with its corresponding time derivatives $\overset{˙}{\overset{\sim}{\mathbf{x}}}$ and $\overset{¨}{\overset{\sim}{\mathbf{x}}}$, is boundary conforming on the manifold $\mathcal{X}$ if ${\overset{\sim}{\mathbf{x}}{(t)}} \in {\mathcal{X},{\forall t}}$.

In the following, the reference trajectory will be used to define dynamic Lagrangians and dynamic fabrics. In this context, the word 'dynamic' can often be read as 'relative to the reference trajectory'. With the notion of reference trajectories we formulate a mapping to the relative coordinate system.

### Definition IV.2

Given a reference trajectory $\overset{\sim}{\mathbf{x}}$ on $\mathcal{X}$, the dynamic mapping $\phi_{d}:{{\mathcal{X} \times \mathcal{X}}\rightarrow\mathcal{X}_{\text{rel}}}$ represents the relative coordinate system $\mathbf{x}_{\text{rel}} = {\mathbf{x} - \overset{\sim}{\mathbf{x}}}$.

Figure 3: The two implications of Dynamic Fabrics. In (a), it can be seen that the trajectory obtained with DF (green) converges towards the reference trajectory (black) while the trajectory with Static Fabrics (red) does not converge. In (b), the top part visualizes collision avoidance as suggested . Here, the trajectory and obstacle are expressed in a relative system xrel. Using the dynamic pull, Eq. 8, this can be transformed into the static reference frame x, bottom part. Together with dynamic energization, the framework of optimization fabrics is leveraged for dynamic environments. The motion of the obstacle, xrel (t) is visualized with an arrow, future positions of the obstacle are shown in lighter color. The resulting trajectory obtained with DF is shown in green.

### IV-C Dynamic pullback

The theory of optimization fabrics also applies to relative coordinates ${\mathbf{x}}_{\text{rel}}$, specifically, specs and potentials can be formulated in moving coordinates. However, there is no theory to combine specs defined in relative coordinates with specs in fixed coordinates. In most cases, individual components of the behavior design are not formulated in the same relative coordinates. Specificially, the configuration space is always static, so we introduce a transformation of a relative spec into the static space $\mathcal{X}$. We call this operation dynamic pullback.

Two specs $\mathcal{S}_{\mathcal{X}_{\text{rel,1}}}$ and $\mathcal{S}_{\mathcal{X}_{\text{rel,2}}}$ defined in two different relative coordinate systems are then combined by first applying the dynamic pullback to both individually and then applying the summation operation for specs. The dynamic pullback is the natural extension to optimization fabrics for relative coordinate systems. It cannot directly be integrated into the framework of optimization fabrics as it breaks the algebra. In the following, we derive several generalizations so that the theory remains valid even in the presence of reference trajectories for individual components, such as moving obstacles or reference trajectories.

### IV-D Dynamic Lagrangians

Next, we show that energy conservation commutes with the dynamic pullback. This allows us to transfer findings on conservative fabrics to dynamic fabrics. We call a Lagrangian that is defined using relative coordinates a dynamic Lagrangian and write $\mathcal{L}_{d}{({\mathbf{x}}_{\text{rel}},{\overset{˙}{\mathbf{x}}}_{\text{rel}})}$. In this relative coordinate system, the dynamic Lagrangian has the same properties as the Lagrangian defined , specifically it induces the Lagrangian spec through the Euler-Lagrange equation, ${{\partial_{{\overset{˙}{\mathbf{x}}}_{\text{rel}}{\overset{˙}{\mathbf{x}}}_{\text{rel}}}^{2}{\mathcal{L}_{d}{\overset{¨}{\mathbf{x}}}_{\text{rel}}}} + {\partial_{{\overset{˙}{\mathbf{x}}}_{\text{rel}}{\mathbf{x}}_{\text{rel}}}^{2}{\mathcal{L}_{d}{\overset{˙}{\mathbf{x}}}_{\text{rel}}}}} - {\partial_{{\mathbf{x}}_{\text{rel}}}\mathcal{L}_{d}}$, as $({\mathbf{M}}_{de},{\mathbf{f}}_{de})$. The system's Hamiltonian $\mathcal{H}_{d} = {{\partial_{{\overset{˙}{\mathbf{x}}}_{\text{rel}}}{\mathcal{L}_{d}^{T}{\overset{˙}{\mathbf{x}}}_{\text{rel}}}} - \mathcal{L}_{d}}$ is conserved by the equation of motion as proven .

Applying the dynamic pullback to the dynamic Lagrangian we obtain the transformed Lagrangian $\mathcal{L}_{d}{({\mathbf{x}},\overset{˙}{\mathbf{x}},\overset{\sim}{\mathbf{x}},\overset{˙}{\mathbf{x}})}$ in the static coordinate system.

### Theorem IV.3

Let $\mathcal{L}_{d}{(\mathbf{x}_{\text{rel}},{\overset{˙}{\mathbf{x}}}_{\text{rel}})}$ be a dynamic Lagrangian and let $\phi_{d}$ be the dynamic mapping to $\mathbf{x}_{\text{rel}}$. Then, the application of the Euler-Lagrange equation commutes with the dynamic pullback.

### Proof

We will show the equivalence by calculation. As shown above, the induced spec is defined in the relative system as $({\mathbf{M}}_{de},{\mathbf{f}}_{de})$. It can be dynamically pulled to form We can dynamically pull the Lagrangian $\mathcal{L}_{d}{({\mathbf{x}}_{\text{rel}},{\overset{˙}{\mathbf{x}}}_{\text{rel}})}$ to form $\mathcal{L}_{d}{({\mathbf{x}},\overset{˙}{\mathbf{x}},\overset{\sim}{\mathbf{x}},\overset{˙}{\overset{\sim}{\mathbf{x}}})}$, where only the first two variables are system variables. Using the generalized Euler-Lagrange equation, the equations of motion of the pulled Lagrangian are obtained as The obtained equations of motion match the one obtained by applying the dynamic pullback, see Eq. 9. ∎ Hence, independently of the coordinates, the system conserves the energy $\mathcal{H}_{d}$ computed with the Hamiltonion in relative coordinates. Next, we adapt the operation of energization to dynamic Lagrangians. Dynamic Lagrangians are a necessary step to allow for collision avoidance with dynamic obstacles in the framework of optimization fabrics. Specifically, the metric for a moving obstacle is computed using the Euler-Lagrange equation in the relative coordinate system. Importantly, in this system, the same energies as with [SF] can be employed. Using the dynamic pullback, the energy defining the metric for the moving obstacle is then maintained according to Theorem IV.3. Concretely, this means that collision avoidance can be achieved in a similar manner as with [SF] with the added advantage of integrated motion estimates of obstacles.

### Proposition IV.4 (Dynamic Energization)

Let ${\overset{¨}{\mathbf{x}} + {\mathbf{h}{(\mathbf{x},\overset{˙}{\mathbf{x}})}}} = \mathbf{0}$ be a differential equation and suppose $\mathcal{L}_{d}$ is a dynamic Lagrangian with the induced spec $(\mathbf{M}_{de},\mathbf{f}_{de})$ and dynamic energy $\mathcal{H}_{d}$. Then the dynamically energized system ${\overset{¨}{\mathbf{x}} + {\mathbf{h}{(\mathbf{x},\overset{˙}{\mathbf{x}})}} + {\alpha_{\mathcal{H}_{d}}{\overset{˙}{\mathbf{x}}}_{\text{rel}}}} = \mathbf{0}$ with conserves the dynamic energy $\mathcal{H}_{d}$.

### Proof

From the derivations, we can compute the rate of change of the dynamic energy as $\overset{˙}{\mathcal{H}_{d}} = {{\overset{˙}{\mathbf{x}}}_{\text{rel}}^{T}{({{{\mathbf{M}}_{de}{\overset{¨}{\mathbf{x}}}_{\text{rel}}} + {\mathbf{f}}_{de}})}}$. The equations of motion can be plugged in through the definition of the reference trajectory Definition IV.1, ${\overset{¨}{\mathbf{x}}}_{\text{rel}} = {\overset{¨}{\mathbf{x}} - \overset{¨}{\overset{\sim}{\mathbf{x}}}}$ to obtain: The energized system conserves the dynamic energy. ∎ Proposition IV.4. ‣ IV-D Dynamic Lagrangians ‣ IV Derivation of dynamic fabrics ‣ Dynamic Optimization Fabrics for Motion Generation") allows to combine dynamic components of the motion generator with static components. Effectively, the dynamic component bends the underlying geometry according to the motion of the dynamic components (e.g., a moving obstacle).

While dynamic Lagrangians and the corresponding energization operation are similar to the methods described , the operation of the standard pull to the dynamically energized system must be slightly modified. Specifically, the reference velocity must be pulled. We show that dynamic energization also commutes with the standard pullback.

### Theorem IV.5

Let $\mathcal{L}_{d}$ be a dynamic Lagrangian to the reference trajectory $\overset{\sim}{\mathbf{x}}$, and let ${\overset{¨}{\mathbf{x}} + {\mathbf{h}{(\mathbf{x},\overset{˙}{\mathbf{x}})}}} = \mathbf{0}$ be a second order differential equation with a metric $\mathbf{M}_{d}$ such that $\mathbf{J}_{\phi}^{T}\mathbf{M}_{d}\mathbf{J}_{\phi}$ has full rank that can be written as spec $(\mathbf{M}_{d},{\mathbf{M}_{d}\mathbf{h}})$. Suppose $x = {\phi{(\mathbf{q})}}$ is a differential map with $\mathbf{J}_{\phi}$ its Jacobian. Then when the reference velocity is being pulled as $\overset{˙}{\overset{\sim}{\mathbf{q}}} = {\mathbf{J}_{\phi}^{\dagger}\overset{˙}{\overset{\sim}{\mathbf{x}}}}$. $\mathbf{J}_{\phi}^{\dagger}$ denotes the pseudo-inverse of $\mathbf{J}_{\phi}$. We say that the dynamic energization operation commutes with the pullback transform.

### Proof

The commutation can be proven by calculation. First, we compute the right side of the equivalence. According to Proposition IV.4. ‣ IV-D Dynamic Lagrangians ‣ IV Derivation of dynamic fabrics ‣ Dynamic Optimization Fabrics for Motion Generation"), the energized system (that maintains the dynamic energy $\mathcal{H}_{d}$) writes as with $\alpha_{\mathcal{H}_{d}}$ as defined in Proposition IV.4. ‣ IV-D Dynamic Lagrangians ‣ IV Derivation of dynamic fabrics ‣ Dynamic Optimization Fabrics for Motion Generation"). Applying the pull-operation, we obtain As the equation expressed in $\mathcal{X}$, this equation in $\mathcal{Q}$ maintains the energy $\mathcal{H}_{d}$. Next, we compute the left hand side. The equation of motion of the pulled dynamic Lagrangian $\mathcal{L}_{d}$ computes as The original spec is pulled accordingly We energize the pulled system according to Proposition IV.4. ‣ IV-D Dynamic Lagrangians ‣ IV Derivation of dynamic fabrics ‣ Dynamic Optimization Fabrics for Motion Generation") Thus, we have shown equivalence between $\alpha_{\mathcal{H}_{d}}$ and $\alpha_{\text{pull}_{\phi}\mathcal{H}_{d}}$. As $\alpha$ is scalar we can can rewrite the energization term in Eq. 12 as With the equivalence of the energization terms, we conclude the proof that dynamic energization commutes with the standard pullback. ∎

### IV-E Dynamic fabrics

With the previous results, we formulate a new class of fabrics that converge to a reference trajectory. We call this class of fabrics Dynamic Fabrics. First, some notations are introduced to eventually show that dynamically energized specs form dynamic fabrics. Analogously to unbiased specs, we define dynamically unbiased specs (i.e., specs whose solutions do not diverge from the reference $\overset{\sim}{\mathbf{x}}$ when starting on the reference).

### Definition IV.6

A spec is said to be dynamically unbiased with respect to $\overset{\sim}{\mathbf{x}}{(t)}$ if ${\mathbf{f}{(\mathbf{x},\overset{˙}{\mathbf{x}})}} = {- {\mathbf{M}\overset{¨}{\overset{\sim}{\mathbf{x}}}}}$, for ${\mathbf{x}{(t)}} = {\overset{\sim}{\mathbf{x}}{(t)}}$ and ${\overset{˙}{\mathbf{x}}{(t)}} = {\overset{˙}{\overset{\sim}{\mathbf{x}}}{(t)}}$.

Beside being dynamically unbiased, some specs will converge to the reference trajectory independently from their initial conditions.

### Definition IV.7

A spec is dynamically rough with respect to $\overset{\sim}{\mathbf{x}}{(t)}$ if all its integral curves $\mathbf{x}{(t)}$ converge dynamically with respect to $\overset{\sim}{\mathbf{x}}{(t)}$.

As for [SF], [DF] can be formed by specs when they are being forced by a potential function $\mathbf{ψ}$. Such a forcing potential is generally a function of $\mathbf{x}$ and $\overset{\sim}{\mathbf{x}}$ and has at least one minimum. A spec that converges to a minimum of the forcing potential then forms a dynamic fabrics.

### Definition IV.8

A spec forms a dynamically rough fabric if it is dynamically rough with respect to $\overset{\sim}{\mathbf{x}}{(t)}$ when forced by a dynamic potential and ${\exists t_{1}} > 0$ such that ${\forall t} > {t_{1},{\mathbf{x}{(t)}}}$ satisfies the Karush-Kuhn-Tucker (KKT) conditions for the optimization problem $\text{min}_{\mathbf{x} \in \mathcal{X}}{\mathbf{ψ}}{(\mathbf{x},{\overset{\sim}{\mathbf{x}}{(t)}})}$. If a spec does not form a dynamically rough fabric but all its damped variants do, it forms a dynamically frictionless fabric.

### Theorem IV.9 (Dynamic Fabrics)

Suppose $S = {(\mathbf{M},\mathbf{f})}_{\mathcal{X}}$ is a spec. Then $S$ forms a dynamically rough fabric with respect to $\overset{\sim}{\mathbf{x}}$ if and only if it is dynamically unbiased with respect to $\overset{\sim}{\mathbf{x}}$ and it converges dynamically when being forced by a dynamic potential ${\mathbf{ψ}}{(\mathbf{x},\overset{\sim}{\mathbf{x}})}$ with $\left. \parallel{\partial_{\mathbf{x}}{\mathbf{ψ}}}\parallel \right. < \infty$ on $\mathcal{X}$.

### Proof

We can write the corresponding differential equation Assume that $S$ is dynamically unbiased. Since the spec converges with respect to $\overset{\sim}{\mathbf{x}}{(t)}$, we have ${\overset{˙}{\mathbf{x}}\rightarrow\overset{˙}{\overset{\sim}{\mathbf{x}}}},{{\mathbf{x}}\rightarrow\overset{\sim}{\mathbf{x}}}$. Because it is dynamically unbiased we also have ${\mathbf{f}}\rightarrow{- {{\mathbf{M}}\overset{¨}{\overset{\sim}{\mathbf{x}}}}}$. Thus, the left hand side of Eq. 13, approaches $\mathbf{0}$. Consequently, the right hand side must also approach $\mathbf{0}$ and hence ${\partial_{\mathbf{x}}{\mathbf{ψ}}}\rightarrow\mathbf{0}$. The last satisfies the Karush--Kuhn--Tucker (KKT) conditions of $\mathbf{ψ}$.

To prove the converse, assume $\mathbf{f}$ dynamically biased. That implies that Hence, there exist a $t > 0$ for which the left hand side does not vanish. As $\mathbf{ψ}$ satisifies the KKT conditions at ${\mathbf{x}} = \overset{\sim}{\mathbf{x}}$, its derivative equals zero at ${\mathbf{x}} = \overset{\sim}{\mathbf{x}}$ which contradicts Eq. 13 with ${{\mathbf{M}}{\mathbf{a}}{(\overset{\sim}{\mathbf{x}},\overset{˙}{\overset{\sim}{\mathbf{x}}})}} = \mathbf{0}$. ∎ Hence, the spec is required to be unbiased and convergent when forced. While the former can be verified using straight-forward computation, convergence is difficult to verify in the general case.

### Lemma IV.10 (Dynamically energized fabrics)

Suppose $S$ is a dynamically unbiased energized spec. Then $S$ forms a dynamically frictionless fabric if ${\partial_{\mathbf{x}}{\mathbf{ψ}}} = {- {\partial_{\overset{\sim}{\mathbf{x}}}{\mathbf{ψ}}}}$.

### Proof

The equation of motion for the energized, forced and damped system writes as The systems energy (dynamic Hamiltonian) is used as a Lyapunov function to show convergence. The rate of change is computed as As the system energy is lower bounded with ${\mathcal{H}_{d} + {\mathbf{ψ}}} \geq 0$ and $\overset{˙}{\mathcal{H}_{d}^{\mathbf{ψ}}} \leq 0$, when $\mathbf{B}$ stricly positive definite, we must have $\overset{˙}{\mathcal{H}_{d}^{\mathbf{ψ}}}\rightarrow 0$. Thus, ${\overset{˙}{\mathbf{x}}}_{\text{rel}}$ goes to zero. We can conclude that the system is dynamically converging. As it it also said to be dynamically unbiased, the damped energized system forms a dynamic fabric by Theorem IV.9. ‣ IV-E Dynamic fabrics ‣ IV Derivation of dynamic fabrics ‣ Dynamic Optimization Fabrics for Motion Generation"). ∎

### Lemma IV.11 (Dynamic Lagrangian fabrics)

An unbiased, dynamic Lagrangian spec forms a dynamically frictionless fabric if ${\partial_{\mathbf{x}}{\mathbf{ψ}}} = {- {\partial_{\overset{\sim}{\mathbf{x}}}{\mathbf{ψ}}}}$ holds for the forcing term.

### Proof

The equations of motion induced by the dynamic Lagrangian including damping and forcing are defined by the spec and can be written explicitly as In the following we use the Hamiltonian and the potential function as Lyapunov function to show convergence of the damped spec.

The time derivative is composed of the time derivative of the Hamiltonian, $\overset{˙}{\mathcal{H}_{e}} = {{\overset{˙}{\mathbf{x}}}_{\text{rel}}^{T}{({{{\mathbf{M}}_{\mathcal{L}_{d}}{\overset{¨}{\mathbf{x}}}_{\text{rel}}} + {\mathbf{f}}_{\mathcal{L}_{d}}})}}$, and the time derivative of the forcing potential, $\overset{˙}{\mathbf{ψ}} = {{{\overset{˙}{\mathbf{x}}}^{T}{\partial_{\mathbf{x}}{\mathbf{ψ}}}} + {{\overset{˙}{\overset{\sim}{\mathbf{x}}}}^{T}{\partial_{\overset{\sim}{\mathbf{x}}}{\mathbf{ψ}}}}}$. Thus, the system's total energy varies over time: Plugging in the equations of motion Eq. 15 gives For ${\partial_{\mathbf{x}}{\mathbf{ψ}}} = {- {\partial_{\overset{\sim}{\mathbf{x}}}{\mathbf{ψ}}}}$ and $\mathbf{B}$ strictly positive definite, $\overset{˙}{\mathcal{H}_{d}}$ is strictly negative for ${({\overset{˙}{\mathbf{x}} - \overset{˙}{\overset{\sim}{\mathbf{x}}}})} \neq 0$. Since $\mathcal{H}_{d}^{\mathbf{ψ}}$ is lower bounded as composition of lower bounded function and ${\overset{˙}{\mathcal{H}_{d}}}^{\mathbf{ψ}} \leq 0$, ${\overset{˙}{\mathcal{H}_{d}}}^{\mathbf{ψ}}\rightarrow 0$ and thus, $\overset{˙}{\mathbf{x}}\rightarrow\overset{˙}{\overset{\sim}{\mathbf{x}}}$ and ${\mathbf{x}}\rightarrow\overset{\sim}{\mathbf{x}}$. Hence, the spec converges dynamically with respect to $\overset{\sim}{\mathbf{x}}$. As the spec is further said to be dynamically unbiased, the damped spec forms a dynamic fabric by Theorem IV.9. ‣ IV-E Dynamic fabrics ‣ IV Derivation of dynamic fabrics ‣ Dynamic Optimization Fabrics for Motion Generation"). ∎ Concretely, Lemma IV.11. ‣ IV-E Dynamic fabrics ‣ IV Derivation of dynamic fabrics ‣ Dynamic Optimization Fabrics for Motion Generation") allows for trajectory following with guaranteed convergence with [DF]. For example, a reference trajectory for the robot's end-effector is defined as $\overset{\sim}{\mathbf{x}}{(t)}$. Then, the potential can be designed as $\psi = {{\overset{\sim}{\mathbf{x}}{(t)}} - {\mathbf{x}}}$ (respecting the construction rule required for Lemma IV.11. ‣ IV-E Dynamic fabrics ‣ IV Derivation of dynamic fabrics ‣ Dynamic Optimization Fabrics for Motion Generation")). In contrast to [SF], where the static potential function is simply updated at every time step, [DF] makes use of the dynamics of the reference trajectory through the dynamic pullback.

### IV-F Construction procedure

From the high-level procedure explained in Section IV-A, we can derive the algorithm using the formal findings in this section, see Algorithm 1.

Define basic inertia as spec ${{{\mathbf{M}}\overset{¨}{\mathbf{q}}} + {{\mathbf{M}}{\mathbf{h}}}} = 0$ for avoidance in avoidances do Define differential map between 𝒬 and 𝒳i: ϕ or ϕt Design geometry on 𝒳i: ${{\overset{¨}{\mathbf{x}}}_{i} + {\mathbf{h}}_{2,i}} = \mathbf{0}$ Design Finsler energy for behavior on 𝒳i: ℒi Energize geometry with Finsler energy IV.4 Apply dynamic pullback to energized system Apply standard pullback Add pulled avoidance component to root fabric Force root system with (time-parameterized) potential Algorithm 1 Motion design with dynamic fabrics Methods to design the individual components, such as geometry and Finsler structures, are introduced. As these design patterns do not vary for [DF], they are not repeated here. In the result section, we show some experimental examples highlighting the comparative advantage of optimization fabrics over model predictive schemes and the advantage of [DF] over [SF] for dynamic environments.

## Extension to non-Holonomic Constraints

Mobile manipulators are often equipped with a non-holonomic base (e.g., a differential drive mobile robot). In contrast to revolute joints for manipulators, non-holonomic bases imply non-holonomic constraints. Based on ideas presented , we propose a method to integrate such constraints in optimization fabrics, including [DF].

We assume that the non-holonomic constraint at hand can be expressed as an equality of form where ${\mathbf{J}}_{\text{nh}}$ is the Jacobian of the constraint, $\overset{˙}{\mathbf{q}}$ is the velocity of the controlled joints of the system and $\overset{˙}{\mathbf{x}}$ is the root velocity of the fabric. For a differential drive $\overset{˙}{\mathbf{x}}$ is the velocity of the system in the Cartesian plane ($\overset{˙}{x},\overset{˙}{y},\overset{˙}{\theta}$) and $\overset{˙}{\mathbf{q}}$ is the velocity of the actuated wheels ($u_{\text{left}},u_{\text{right}}$). Moreover, we assume that Eq. 16 is smooth and differentiable so that we can write The theory of optimization fabrics allows to pull a tree of fabrics back into one fabric expressed in its root-coordinates of form ${{{\mathbf{M}}\overset{¨}{\mathbf{x}}} + {\mathbf{f}}} = 0$ with its solution as Plugging Eq. 17 into the root fabric we obtain the non-holonomic fabric of form | | ${{\mathbf{M}}{\mathbf{J}}_{\text{nh}}\overset{¨}{\mathbf{q}}} + {{\mathbf{M}}{\overset{˙}{\mathbf{J}}}_{\text{nh}}\overset{˙}{\mathbf{q}}} + {\mathbf{f}}$ | $= 0$ | | | | ${{\mathbf{M}}_{\text{nh}}\overset{¨}{\mathbf{q}}} + {\mathbf{f}}_{\text{nh}}$ | $= 0$ | | Note that ${\mathbf{M}}_{\text{nh}}$ is not necessarily a square matrix and thus not invertible as it was in the original fabric. To find the best actuation for the wheels, we formulate motion generation with fabrics as an unconstrained optimization problem In this approach, we minimize the error of the final equation. We could equally derive Eq. 19 with the objective of minimizing the error between $\overset{¨}{\mathbf{x}} = {{{\mathbf{J}}_{\text{nh}}\overset{¨}{\mathbf{q}}} + {{\overset{˙}{\mathbf{J}}}_{\text{nh}}\overset{˙}{\mathbf{q}}}}$ and the original fabric's solution $\overset{¨}{\mathbf{x}} = {- {{\mathbf{M}}{\mathbf{f}}}}$. The mimization of the difference leads to similar result. This optimization problem replaces Eq. 18 and is solved by The solutions to this problem makes optimization fabrics, and thus dynamic fabrics, applicable to non-holonomic robots, such as differential drive robots or cars. A qualitative comparison between a trajectory generated for a holonomic and a non-holonomic robot is shown in Fig. 4.

Figure 4: Path (green) following with a holonomic and a non-holonomic robot using DF with the extension to non-holonomic robots The theory of optimization fabrics is built upon energy conservation of artificial energies that design the motion. Eq. 19 does not solve the resulting spec exactly, but minimizes the deviation according to the least square objective function. For many kinematic systems, e.g., differential drive model, bicycle model, the non-holonomic constraint additionally reduces the number of degrees of freedom, ${\dim q} < {\dim x}$. As a consequence, the least square solution has a non-zero residuum. Then, some fundamental properties of optimization fabrics, such as energy conservation and convergence can no longer be guaranteed. Despite this theoretical shortcoming, we show that this approach leads to good performance in practical applications.

## Experimental results

Figure 5: Dynamic Fabrics in the presence of a human. The human hand’s state is estimated with a motion capture system. The robot smoothly and in advance avoids the human operator and allows for safe coexistence.

In this section, the performance of optimization fabrics is assessed on various robotic platforms. Although suggested performance benefits over optimization-based methods to local motion planning, no quantitative comparisons have been presented to this date. The scenarios that we have chosen here (especially in the first two experiments) are intentionally simple to identify the specific differences. In the real world experiments, we show the differences on more dynamic scenarios, where the limited frequency of a global planning method, such as RRT, justifies the need for a local planning method. To give a general idea of the performance differences between [SF] and receding-horizon trajectory optimization, we compare the performance of an [MPC] formulation, adapted , with [SF], as proposed . The second experiment compares performance between [SF] and [DF] for trajectory following tasks. In the third experiment, moving obstacles are added to the scene to form a dynamic environment. Our extension to non-holonomic systems is tested in the fourth experiment. Then, everything is combined in an experiment with a differential drive mobile manipulator. Finally, we present a possible application of a robot sharing the environment with a human. The experiments described here are supported by videos accompanying this paper.

### VI-A Settings & performance metrics

We present a detailed analysis of the experimental results for two commonly used setups, namely the Franka Emika Panda, a Clearpath Boxer, and a mobile manipulator composed of both components see. Note, that these robots are representative of commonly used robots in dynamic environments. The Franka Emika Panda is a 7 degree-of-freedom robot with joint torque sensors, comparable to the Kuka Iiwa. Mobile manipulators equipped with differential drives are widely used by other manufacturers, see Pal Robotics Tiago or the Fetch Robotics Mobile Manipulator.

Compared to, we propose a more extensive list of metrics. With regards to safety, we measure the Clearance, the minimum distance between the robot and any obstacle along the path. For static goals, solver planner performance is measured in terms of Path Length, euclidean length of the end-effector trajectory, and Time-to-Goal, time to reach the goal. For trajectory following tasks, this measure is replaced by Summed Error, the normed sum of deviation from the desired trajectory. Computational costs are measured by the average Solver Time in each time step. Most important, binary success is measured by the Success Rate, where failure indicates that either the goal was not reached or a collision occurred during execution. Performance metrics are only evaluated if the concerned motion generator succeeded. More information on the testbed can be found .

In static, industrial environments the time to reach the goal can be considered the one single most important metric, but we argue that dynamic environments require a more nuanced performance evaluation and thus a set of metrics. Intentionally, we do not give general weights to the individual metrics, as their corresponding importance highly depends on the application. As a consequence, we tuned the compared planners in such a way that they reach the goal in a similar time. Note that the general speed for all planners compared in this article can be adjusted by choosing a different parameter setup.

As this work does not focus on obstacle detection, we simplify obstacles to spheres. Thus, we assume that an operational perception pipeline detects obstacles and constructs englobing spheres. The experiments are randomized in either the location of the obstacles, the location of the goal, the initial configuration, or in a combination of all three aspects. For every experiment, the type and level of randomization are stated.

### VI-B Experiment 1: Static fabrics vs. [MPC]

In the first experiment, we compare the performance of an [MPC] formulation with [SF]. Compared to the formulation used , we use a workspace goal rather than a configuration space goal, and apply a second order integration scheme so that the control outputs are accelerations instead of velocities. We clarify that the formulation deployed for the following tests is geometric as the model used is a second order integrator and does not include the dynamics of the robots. The main reason lies in the reduced computational costs and the inaccessibility of a highly accurate model.

### Parameters

The low-level controller of the robot runs at $1$ kHz. The fabrics are running at $100$ Hz and the [MPC] at $10$ Hz. The time horizon for the [MPC] planner was set to $T = 3$s spread equally over $H = 30$ stages. Based on the findings , we are confident that the [MPC] planner is close to its optimal settings. Moreover, we used the implementations , which are reported to have improved performance over open-source libraries like acado.

Figure 6: Examples for simulation setups with panda robot. Initial configuration are shown in white and final configurations in light green. Obstacles are visualized in red. In (a), only static obstacles are considered. In (b), the trajectories of two moving obstacles are visualized in light red.

### Simulation

A series of $N = 50$ runs was evaluated with the panda robot in simulation. Randomized end-effector positions were set for every run, while the initial configuration remained unchanged. One to five spherical obstacles of radius $r = 0.15$ m were placed in the workspace at random. An example setup is shown in Fig. 6(a). The results are summarized in Fig. 7. Solver times with fabrics averaged at $1$ ms while the [MPC] solver took around $50$ ms in every time step. Although the path length is similar with both solvers, the minimum clearance from obstacles is increased with [SF] ($0.183$ m) compared to [MPC] ($0.138$ m). This means that the trajectories are safer and thus more suitable for dynamic environments. Both motion generation methods fail in 6 cases. However, the [SF] produce only one collision while [MPC] creates 5 collisions. The remaining failures are deadlocks. For both methods, deadlocks result from local minima, highlighting the need for supportive global plans. Collisions are caused by numerical inaccuracies, which are generally higher with [MPC] due to the lower frequency.

(a) Metrics evaluation for successful experiments Figure 7: Results for randomized motion planning problems with the panda robot in simulation. Lower values represent an improved performance of SF over MPC.

### Real World

For the experiments with the real robot, we limited the number of test runs to $N = 20$. In contrast to the simulated results, [MPC] has significantly more collisions than [SF], Fig. 8(b). This is likely to be caused by the lower frequency at which the [MPC] is running. While in simulation the model matches the actual behaviour perfectly and the time interval between two computations can be accuratly predicted, more uncertainty in the model is present in the real world. This leads to prediction errors that cause collisions. For the collision free cases, the real world experiments confirm that optimization fabrics tend to be more conservative with respect to obstacles, see Clearance in Fig. 8(a). Similar to the simulated results, the solving time is reduced by a factor of around $50$ with fabrics. This allows to run the planner at a higher frequency and thus generating smoother motions.

(a) Metrics evaluation for successful experiments Figure 8: Results for randomized motion planning problems with the real panda robot. SF are more conservative around obstacles, improving on safety, while reducing the computational cost by a factor of ≈ 50. As a result of the increased clearance, collisions are more reliably avoided with SF.

### Discussion

The difference in performance (except for solver time) is likely caused by the different objective metrics. The objective function in the [MPC] formulation is mainly governed by the Euclidean distance to the goal while control inputs and velocity magnitude are given a relative small weight. Avoidance behaviors, such as joint limit avoidance and obstacle avoidance, are respected through inequality constraints. In contrast, [SF] design the objective in a purely geometric manner including all avoidance behaviors. Thus the manifold for the motion is directly altered by the avoidance behaviors, i.e., the manifold is bent so that the notion of shortest path changes with the addition of obstacles. This shaping of the manifold leads to improved canvergence compared to the combination of Euclidean distance objective function and inequality constraints used with [MPC].

### VI-C Experiment 2: Static fabrics vs. Dynamic fabrics

In motion planning for dynamic environments, global and local planning methods work together to achieve efficient and safe motion of the robot. However, [SF] are not designed to follow global paths. Path following can only be achieved using a pseudo-dynamic approach where the forcing potential is shifted in every time step without considering the dynamics of the trajectory. Therefore, we propose [DF] to allow smoother path following tasks, where the speed of the goal is also considered during execution. In this second experiment, we investigate how [DF] compare to [SF] for path following tasks. Specifically, we show that [DF] outperform [SF] when following a path generated by a global planner.

### Simulation

We evaluated [DF] on the panda robot robot in simulation with an analytic, time-parameterized curve and a path generated by a global planner, namely RRT (Fig. 9). In the case of the analytic trajectory, the three obstacles were randomized across all runs. For the experiment with the global planner, the goal position and the obstacles were randomized across all runs. A total of $N = 50$ experiments were executed for this experiment. The reduced summed error for dynamic fabrics verifies the theoretical finding that dynamic fabrics can follow paths more closely. The average error over all runs with the analytic trajectory is $0.0792$m ([DF]) and $0.136$m ([SF]), see Fig. 11(a) for the comparison. For the spline path generated with RRT, the average error over all runs is $0.145$m ([DF]) and $0.240$m ([SF]), see Fig. 11(b) for the comparison.

Figure 9: Path generated with RRT from OMPL.

Figure 10: Trajectory following tasks with Dynamic Fabrics. In (a), the trajectory is a time-parameterized analytic curve. In (b), the trajectory is described by a spline.

(a) Analytic, user-specified global path (b) Global path generated by RRT using OMPL Figure 11: Comparison between static and dynamic fabrics for trajectory following tasks in simulation. Lower values in a metric indicate that DF performed better than SF.

### Real-World

Path following was also assessed with the real panda robot in similar settings. Quantitative results are only presented for $N = 20$ different paths with splines where up to three obstacles were added to the workspace, see Fig. 10. The results in real-world confirm the findings from the simulation. By exploiting the velocity information of the trajectory, the integration error can be effectively reduced, Fig. 12. In contrast to the simulation we see a higher fluctuation in solver times, which can be caused by a generally lower capacity of the computing unit on the robot.

Figure 12: Comparison between SF and DF when following a path defined by a basic spline in the real world. The splines and the obstacles are different for the N = 20 case. DF achieve lower deviation errors that SF.

### VI-D Experiment 3: Moving Obstacles

Next, we compare the different methods in the presence of dynamic obstacles. All experiments in this section consist of at least one moving obstacle that follows either an analytic trajectory or a spline. Here, we use stationary goals to isolate the results from the behavior investigated in the previous section.

### Simulation

For this series with the simulated panda robot, only the goal position was randomized. The initial configuration and the two moving obstacles with the trajectories were kept constant throughout all experiments. The environment is visualized in Fig. 6(b). The comparison between [SF] and [DF] shows that [DF] are more conservative in terms of collision avoidance with dynamic obstacles. Specifically, the distance between the robot and the obstacles is increased (Fig. 13(a)). The success rate with [DF] compared to [SF] is significantly improved, see Fig. 13(b). Thus showing the need for using [DF] in dynamic environments.

(a) Metrics evaluation for sucessful experiments Figure 13: Comparison between SF and DF for scenarios with dynamic obstacles. While path length and solver time is not increased, clearance is increased and the time to reach the goal is reduced with DF compared to SF.

### Real-World

In a series of $N = 20$ experiments, performance on the real panda arm was assessed. The same trend for more conservative behavior with [DF] compared to [SF] can be observed, Fig. 14. However, [DF] take longer on average to reach the goal as they keep larger clearance from obstacles. Note that collisions are effectively eliminated with [DF] compared to [SF].

(a) Metrics evaluation for successful experiments Figure 14: Comparison between SF and DF for real-world scenarios with dynamic obstacles.

By investigating one example out of the series, see trajectories in Fig. 15, the reason for the large number of collisions with [SF] can be explained. Both methods initially drive the end-effector to the goal position. As the moving obstacle is approaching the robot, the [DF] are starting to react while [SF] are not changing its behavior resulting in a very sudden motion at around $t = 30$s. [SF] treat moving obstacles as pseudo-static (i.e., the position of the obstacle is updated at every time step, but the information on its velocity is discarded). As a result, the relative velocity between obstacle and robot is only a function of the velocity of the robot. Geometries and energies for collision avoidance with fabrics are, by design, a function of this velocity and therefore fail to avoid moving obstacles when the robot moves slowly or not at all. This behavior is most visible when the goal has already been reached but an obstacle is approaching. [DF] on the other hand take the velocity of the moving obstacles into account and can therefore avoid them.

Figure 15: Trajectories for real panda robot in the presence of a dynamic obstacle. DF show a smoother and in-advance reaction to the approaching obstacle while SF can only react in sudden motion.

### VI-E Experiment 4: Nonholonomic robots

### Simulation

This experiment assesses the performance of the proposed method to compute trajectories for non-holonomic robots with fabrics. Specifically, we run experiments for a Clearpath Boxer for position. As for the first experiment, we compare the performance to [MPC]. In this experiment, the initial position, the goal location, and the position of five obstacles were randomized. The results reveal that our extension of optimization fabrics to non-holonomic robots maintains similar results as with a robotic arm. Specifically, computational time can be reduced to optimization-based methods while maintaining good performance in terms of safety and goal-reaching, Fig. 16. We can also observe that success rate with [SF] is lower compare to [MPC] due to a high number of unreached goals.

(a) Metrics evaluation for successful experiments Figure 16: Results for randomized cased with the Clearpath Boxer robot. Similar performance in terms of safety and goal-reaching can be combined with very fast computation using optimization fabrics.

### VI-F Experiment 5: Mobile manipulators

In the final experiment, we assess the applicability of [SF] and [DF] to a non-holonomic mobile manipulator. In an environment that is densely occluded by obstacles, the motion planning problem is defined by a desired end-effector position and additional path constraints (e.g. desired orientation of the end-effector).

### Simulation

In simulation, we evaluate the performance of our extension to non-holonomic mobile manipulators with [SF]. In this series, the positions of 8 obstacles are randomized for $N = 50$ cases. The workspace was limited to a 7mx7m square, so that random obstacles are ensured to be actually hindering the motion planner. The results reveal that properties shown in the previous experiments transfer to more complex systems without loss of the computational benefit, Fig. 17. In this series, there were 1 unreached goals and 4 collisions which are, similar to the previous experiments, caused by local minima. Local minima are more likely for mobile manipulators as their workspace is larger.

Figure 17: Quantitative results with static fabrics for a non-holonomic mobile manipulator in simulation. Fabrics solve planning problems in randomized environments in low planning time. This allows whole-body control and highly reactive behavior.

Combining our contributions, [DF] and the extension to non-holonomic robots, we achieve reactive and safe behavior in dynamic environments. Moving obstacles are avoided in a natural way using our method, see Fig. 18.

Figure 18: Sequence of trajectory computed with DF for a mobile manipulator in simulation with moving obstacles (red sphere with line indicating the past trajectory) and one end-effector goal (green). The trajectory of the end-effector are visualized in (e) as x and the desired end-effector position as $\overset{\sim}{\mathbf{x}}$.

### Real-World

We present qualitative results for a non-holonomic mobile manipulator using [DF]. In Fig. 1, the robot follows a trajectory defined by a basic spline, while additionally respecting an orientation constraints on its end-effector and avoiding the shelves and an obstacle on the ground. The end-effector trajectory is plotted in Fig. 19.

Figure 19: Real-world experiment for path following with a mobile manipulator. The global path can be tracked accurately by DF including the extension to non-holonomic robots. The scene is visualized in Fig. 1.

### VI-G Experiment 6: Dynamic fabrics in supermarkets

In this experiment, we show qualitatively how [DF] could be used in collaborative environments where humans and robots coexist. For this experiment, we give the robot a static goal pose similar to a pickup setup. The same environment is shared with a co-worker who restocks a shelf. The right hand of the human is tracked with a motion capture system. The hand is then avoided by the robot using [DF], see Fig. 19. In this experiment, the minimum distance between the robot and the hand was $0.062$m. This real-world experiment showcases potential applications of the proposed method.

## Conclusion

In this paper, we have generalized optimization fabrics to dynamic environments. We have proven that our proposed Dynamic Fabrics are convergent to reference paths and can thus compute motion for path following tasks (Lemma IV.10. ‣ IV-E Dynamic fabrics ‣ IV Derivation of dynamic fabrics ‣ Dynamic Optimization Fabrics for Motion Generation")). Besides, we have proposed an extension to optimization fabrics (and thus also [DF]) for non-holonomic robots. This allows the application of this framework to a wider range of robotic applications and ultimately allows the deployment to many mobile manipulators in dynamic environments.

These theoretical findings were confirmed in various experiments. First, the quantitative comparisons showed that Static Fabrics outperforms [MPC] in terms of solver time while maintaining similar performance in terms of goal-reaching and success rate. The improved performance with optimization fabrics might be caused by the different metric for goal reaching compared to Model Predictive Control. An integration of non-Riemannian metrics into an MPC formulation should be further investigated in the future.

Verifying our theoretical derivations for [DF], the experiments showed that the deviation error for path following tasks is decreased compared to [SF]. Similarly, environments with moving obstacles and humans showed increased clearance while maintaining low computational costs and execution times. Thus, [DF] overcome an important drawback of [SF], where collision avoidance with moving obstacle is solved purely by the high frequency at which optimization fabrics can be computed. Moreover, the generalization did not increase the solving time compared to [SF]. Unlike the original work on optimization fabrics, this generalization allows the deployment to dynamic environments where velocity estimates of moving obstacles are available.

Direct sensor integration in optimization fabrics might be feasible in future works to overcome the shortcomings of perception pipelines for collision avoidance. For the trajectory path tasks in this paper, we used a simple global path generated in workspace. As [DF] integrate global path in arbitrary manifolds, improving the global planning phase could be further investigated. We expect this to be beneficial when robotics tasks are constantly changing and task planning is required.
