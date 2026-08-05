<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

TamedPUMA: Safe and Stable Imitation Learning with Geometric Fabrics

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Using the language of dynamical systems, Imitation learning (IL) provides an intuitive and effective way of teaching stable task-space motions to robots with goal convergence. Yet, IL techniques are affected by serious limitations when it comes to ensuring safety and fulfillment of physical constraints. With this work, we solve this challenge via TamedPUMA, an IL algorithm augmented with a recent development in motion generation called geometric fabrics. As both the IL policy and geometric fabrics describe motions as artificial second-order dynamical systems, we propose two variations where IL provides a navigation policy for geometric fabrics. The result is a stable imitation learning strategy within which we can seamlessly blend geometrical constraints like collision avoidance and joint limits. Beyond providing a theoretical analysis, we demonstrate TamedPUMA with simulated and real-world tasks, including a 7-DoF manipulator.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

As robotic solutions rapidly enter unstructured environments such as the agriculture sector and homes, there is a critical need for methods that allow non-experts to easily adapt robots for new tasks. Currently, experts manually program these tasks, a method that is costly and not scalable for widespread use. Moreover, these sectors demand that robots safely interact with dynamic environments where humans are present.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A possible solution to this societal challenge comes from Imitation Learning ([IL]). Using this technique, robots can learn motion profiles from demonstrations provided by non-expert users. Furthermore, by encoding the learned trajectories as solutions of a dynamical system, established mathematical tools from dynamical system theory can be used to guarantee convergence to the task's goal state, as we discuss more in detail in Sec. 1.1. In a robotics context, these learned dynamical systems commonly encode the navigation policy towards a goal within a task space - such as the evolution of the end-effector pose of a manipulator while pouring water in a glass from all possible initial locations. However, this focus on task space motions renders [IL] fundamentally limited when considering physical constraints involving the robot's body impacting itself or interacting with the external environment. Substantial recent research has looked into the problem but, as we discuss in Sec. 1.1, to the best of our knowledge, no [IL] method can simultaneously ensure stability and real-time fulfillment of physical constraints for systems with many degrees of freedom.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work contributes to the state of the art by introducing TamedPUMA, a learning framework that builds on IL and geometric fabrics to obtain inherently stable and safe motion primitives from demonstrations. By leveraging the recently introduced geometric framework for motion generation called geometric fabrics, our approach learns stable motion profiles while considering online whole-body collision-avoidance and joint limits. To make this possible, the learned task-space policy has to be formulated as a $2^{nd}\text{-order}$ (neural) dynamical system as fabrics operate within the Finsler Geometry framework where vector fields must be defined at the acceleration level. Also, the learned policy must admit an aligned potential, which roughly means a scalar function whose gradient is aligned with the acceleration field when the velocity is null. In this paper, we formally assess how we can ensure that both conditions are met. The performance of our approach is evaluated with a simulated and real-world 7-DoF manipulator, where we also benchmark it against vanilla geometric fabrics, vanilla learned stable motion primitives and a modulation-based IL approach leveraging collision-aware IK.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Configuration and task spaces", "weight": 1.0} -->

The configuration of the robot is denoted by ${\mathbf{q}} \in \mathcal{C}$ with its time derivatives $\overset{˙}{\mathbf{q}}$ and $\overset{¨}{\mathbf{q}}$. Here, $\mathcal{C}$ indicates the configuration space of the robot, which has a dimension of $n$. *Tasks* can be defined in different task spaces $\mathcal{X}_{j}$. For instance, collision avoidance of a manipulator's end effector can be a task defined in the end-effector's space. Additionally, to address whole-body obstacle avoidance, multiple tasks can be defined for various coordinates along the robot's body. Furthermore, other tasks, such as reaching behaviors, can also be included.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Configuration and task spaces", "weight": 1.0} -->

A task variable ${\mathbf{x}}_{j} \in \mathcal{X}_{j}$ denotes the value of the state representation for the $j$-th task space, where $j \in {\lbrack M\rbrack}$, $M$ denotes the number of task spaces, and ${\lbrack M\rbrack} = {\{{j \in {\mathbb{Z}}^{+}}:{j \leq M}\}}$. The relation between the configuration space and a given task space is stated via a twice-differential map $\phi_{j}:{\mathcal{C}\rightarrow\mathcal{X}_{j}}$, and the map's Jacobian as ${\mathbf{J}}_{\phi_{j}} = \frac{\partial\phi_{j}}{\partial{\mathbf{q}}}$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Geometric fabrics", "weight": 1.0} -->

A dynamical system describes the behavior of a system using differential equations. In *geometric fabrics*, these dynamical systems describe an *artificial* system generating desired trajectories for a robotic system. The desired motions are described using second-order nonlinear time-invariant dynamical systems, $\overset{¨}{\mathbf{x}} = {f{({\mathbf{x}},\overset{˙}{\mathbf{x}})}}$. In this framework, dynamical systems consist of two parts: one that conserves a *Finsler energy* and another that is energy-decreasing. The energy-conservative part takes care of all *avoidance tasks*, e.g., joint limit avoidance and obstacle avoidance, while the energy-decreasing part drives the system towards the goal.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Learning stable motion primitives via PUMA", "weight": 1.0} -->

Similarly to geometric fabrics, Policy via neUral Metric leArning ([PUMA]) models a desired motion as a nonlinear time-invariant dynamical system. This method represents the dynamical system ${\mathbf{f}}_{\theta}^{\mathcal{T}}$ in one of the task spaces $\mathcal{X}_{j}$ (commonly the robot's end effector's space), denoted as $\mathcal{T}$, as a [DNN] with weights $\theta$. The weights are optimized to imitate a set of demonstrations while ensuring convergence to a goal state ${\mathbf{x}}_{\text{g}} \in \mathcal{T}$. In other words, ${\mathbf{x}}_{\text{g}}$ must be a globally asymptotically stable equilibrium in the region of interest.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Learning stable motion primitives via PUMA", "weight": 1.0} -->

To enforce stability under minimization of the loss function, a specialized loss is introduced and optimized alongside an imitation loss. To design this loss, it is necessary first to define a latent space $\mathcal{L}$ as the output of a hidden layer $l$ of the [DNN], such that where ${\mathbf{ρ}}_{\theta}:{\mathcal{T}\rightarrow\mathcal{L}}$ encodes the first $1,\ldots,l$ layers and ${\mathbf{φ}}_{\theta}:{\mathcal{L}\rightarrow{d\mathcal{T}}}$ the last ${l + 1},\ldots,L$ layers with $d\mathcal{T}$ representing the tangent bundle of $\mathcal{T}$, capturing the derivatives and tangent spaces associated with $\mathcal{T}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "TamedPUMA: Combining learned stable motion primitives and fabrics", "weight": 1.0} -->

With learned stable motion primitives, complex tasks can be learned from demonstrations, while converging to the goal. In TamedPUMA, these learned dynamical systems are incorporated into the framework of geometric fabrics, generating stable and safe motions while respecting whole-body collision avoidance and physical constraints of the robot. In Section 3.1, the problem formulation is discussed, followed by the two variations of TamedPUMA, the Forcing Policy Method ([FPM]) and Compatible Potential Method ([CPM]), in Section 3.2 ‣ 3 TamedPUMA: Combining learned stable motion primitives and fabrics ‣ TamedPUMA: safe and stable imitation learning with geometric fabrics") and 3.3 ‣ 3 TamedPUMA: Combining learned stable motion primitives and fabrics ‣ TamedPUMA: safe and stable imitation learning with geometric fabrics") respectively.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Consider there exists a dynamical system $\overset{\sim}{\mathbf{f}}$ that describes a desired motion profile for a robot, which induces the distribution of trajectories $\overset{\sim}{p}{(\tau)}$. For a given task variable ${\mathbf{x}} \in \mathcal{T}$, such as the robot's end-effector pose, we assume we can sample trajectories from this distribution. Then, if the dynamical system ${\mathbf{f}}_{\theta}^{\mathcal{T}}$ represents the evolution of the robot's state in $\mathcal{T}$, our objective is to minimize the distance between the distribution of trajectories induced by this system $p_{\theta}{(\tau)}$ and $\overset{\sim}{p}{(\tau)}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Furthermore, ${\mathbf{f}}_{\theta}^{\mathcal{T}}$ must always reach a desired state ${\mathbf{x}}_{g} \in \mathcal{T}$ while accounting for region avoidance constraints, namely, self-collisions, obstacles, and joint limits for M tasks defined in multiple task spaces $\mathcal{X}_{j}$. More formally, This objective minimizes the Kullback-Leibler divergence between the estimated dynamical system and the target system (5a). This divergence is often used as a distance measure between distributions as it is minimized through maximum likelihood estimation using distribution samples.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Moreover, the problem is subject to two constraints: (5b) the dynamical system should converge to a task-space goal ${\mathbf{x}}_{g}$ in $\mathcal{T}$, and (5c) task-space states ${{\mathbf{x}}_{j},{\forall j}} \in {\lbrack M\rbrack}$, should remain within the free space $\mathcal{X}_{j}^{\text{free}}$ where the dynamical system is well-defined, which could be the collision-free space or the space within the joint limits.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

From this formulation, [PUMA] *softly* addresses (5a) using the loss $\ell_{\text{IL}}$, while fabrics addresses (5c) through their geometric-aware formulation. Both approaches tackle the problem of stability; however, it remains challenging to combine both methods while ensuring convergence to the goal (5b). In the following subsections, we propose two approaches to address this.

<!-- chunk {"id": "body-0016", "role": "body", "section": "The Forcing Policy Method (FPM)", "weight": 1.0} -->

First, we introduce the [FPM]. For this purpose, we define the dynamical system ${\mathbf{f}}_{\theta}^{\mathcal{C}}$ in configuration space resulting from applying a pullback operation, via [PUMA], in $\mathcal{T}$: where the task variable ${\mathbf{x}}_{\text{ee}}$ is the end-effector position and orientation of the robot as illustrated in Fig. 1 ‣ 3 TamedPUMA: Combining learned stable motion primitives and fabrics ‣ TamedPUMA: safe and stable imitation learning with geometric fabrics").

<!-- chunk {"id": "body-0017", "role": "body", "section": "The Forcing Policy Method (FPM)", "weight": 1.0} -->

Then, leveraging the definition of a forced system from Eq., in the [FPM] we propose to use the pulled system obtained via [PUMA] as the forcing policy, Assuming $\ell_{\text{PUMA}}$ has already been minimized, the system ${\mathbf{f}}_{\theta}^{\mathcal{T}}$ comes to rest at ${\mathbf{x}}_{g}$, implying that ${\mathbf{f}}_{\theta}^{\mathcal{C}}$ converges to ${\mathbf{q}}_{g}$ where multiple values of ${\mathbf{q}}_{g}$ may exist in the case of a redundant system. This collection of states ${\mathbf{q}}_{g}$ corresponds to the *zero set* of ${\mathbf{f}}_{\theta}^{\mathcal{C}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "The Forcing Policy Method (FPM)", "weight": 1.0} -->

From Proposition II.17 in Ratliff and Van Wyk, we know that if the system in Eq. (7 ‣ 3 TamedPUMA: Combining learned stable motion primitives and fabrics ‣ TamedPUMA: safe and stable imitation learning with geometric fabrics")) reaches the zero set of ${\mathbf{f}}_{\theta}^{\mathcal{C}}$, it will stay there (which comes from the observation that fabrics are conservative). However, convergence of Eq. (7 ‣ 3 TamedPUMA: Combining learned stable motion primitives and fabrics ‣ TamedPUMA: safe and stable imitation learning with geometric fabrics")) to the zero set of ${\mathbf{f}}_{\theta}^{\mathcal{C}}$ is not formally assessed. Re-evaluating the problem formulation suggests that the constraint in Eq (5b), stating that the system should converge to the desired minimum ${\mathbf{q}}_{g}$, is therefore not guaranteed.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The Forcing Policy Method (FPM)", "weight": 1.0} -->

In Sec. 3.3 ‣ 3 TamedPUMA: Combining learned stable motion primitives and fabrics ‣ TamedPUMA: safe and stable imitation learning with geometric fabrics"), we propose a method with stronger convergence guarantees.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The Compatible Potential Method (CPM)", "weight": 1.0} -->

As a second approach, we propose the [CPM] leveraging *compatible potentials* to obtain a stronger notion of convergence. For a potential function compatible with a dynamical system, its negative gradient generally points in the same direction as the system's vector field.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In this section, we explore TamedPUMA's capabilities in constructing stable and collision-free motions for a 7-DOF manipulator. Details regarding the [DNN], differential mappings, a discussion on the limitations, code and videos are included in the attached material^11^footnotemark: 1.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experimental setup and performance metrics", "weight": 1.0} -->

To show the performance of the two variations of TamedPUMA, [FPM] and [CPM], simulations using the Pybullet physics simulation and real-world experiments are performed on a 7-DoF KUKA iiwa manipulator. Two tasks are analyzed, picking a tomato from a crate and pouring liquid from a cup, where a [DNN] is trained for each task using 10 demonstrations, recording end-effector positions, velocities and accelerations. The proposed [FPM] and [CPM], are compared against vanilla geometric fabrics, vanilla [PUMA] and *modulation-IK*. Modulation-IK modifies PUMA to be obstacle-free within the task space using a modulation matrix. Then, whole-body collision avoidance is achieved by tracking the modified desired pose using a collision-aware [IK]. All methods are evaluated based on their success rate and time-to-success, which respectively indicate the ratio of successful scenarios and the time required for the robot to reach the goal pose. Successful scenarios ensure collision-free motions with an end pose satisfying $\left.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experimental setup and performance metrics", "weight": 1.0} -->

\parallel{{\mathbf{x}}_{\text{ee}} - {\mathbf{x}}_{\text{g}}}\parallel \right._{2} < {0.05m}$. In addition, the computation time is denoted, and the path difference to the desired path by PUMA as $\frac{1}{P}{\sum\left. \parallel{{\mathbf{x}}_{\text{ee}} - {\mathbf{x}}_{\text{PUMA}}}\parallel \right._{2}}$ where ${\mathbf{x}}_{\text{ee}}$ and ${\mathbf{x}}_{\text{PUMA}}$ correspond to the end-effector poses along the path with length $P$ of the analyzed method and PUMA respectively. The path difference is computed in obstacle-free scenarios, where we aim to track the DNN as closely as possible, and in obstacle-rich allowing for deviations from this path.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Simulation experiments on a 7-DOF manipulator", "weight": 1.0} -->

Path difference to PUMA Table 1: Statistics for 30 simulated scenarios. The path difference to PUMA is measured in an obstacle-free environment, while all other metrics are compared in an obstacle-rich environment.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Simulation experiments on a 7-DOF manipulator", "weight": 1.0} -->

In simulation, 30 realistic scenarios are explored, including 15 scenarios of a tomato-picking task and 15 scenarios of a pouring task. In each task, the initial robot configuration and obstacle locations change. Moreover, 10 scenarios included moving goals, and 7 scenarios included moving obstacles. For each scenario, at least one obstacle is situated between the initial configuration and the goal pose. The last five links on the robotic chain are considered for collision avoidance, given that the first three links have restricted movement due to the base being mounted to the table. The shape of the last five links is approximated using spheres with a radius of 9 $cm$, and 7 $cm$ for the final link.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Simulation experiments on a 7-DOF manipulator", "weight": 1.0} -->

As depicted in Table 1, the two TamedPUMA variations improve the success rate over PUMA by enabling whole-body obstacle avoidance. In contrast to geometric fabrics, [FPM] and [CPM] can track the desired motion profile leading to a smaller path difference with [PUMA] of 0.02 $\pm$ 0.04 and 0.04 $\pm$ 0.06 respectively, compared to geometric fabrics, 0.22 $\pm$ 0.27, in an obstacle-free environment. In an obstacle-rich environment, geometric fabrics result in a deadlock in 6 of the 30 scenarios where the robot does not reach the goal as it is unable to move around the edge of the crate or object. The benchmark Modulation-IK is also unable to achieve all tasks due to collisions or deadlocks, as it cannot find a feasible solution converging towards the goal.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Simulation experiments on a 7-DOF manipulator", "weight": 1.0} -->

TamedPUMA thereby inherits the efficient scalability to multi-object environments from fabrics, as computation time in an environment with 1000 obstacles is only 5.9 $\pm$ 0.8 $ms$ and 7.0 $\pm$ 1.1 $ms$ for FPM and CPM respectively, a neglectable increase with respect to the two obstacles considered in Table 1, while optimization-based methods like Modulation-IK scale poorly with large numbers of obstacles with a computation time of 3.5$\cdot 10^{3}$ $\pm$ 10.7$\cdot 10^{3}$ $ms$ in an environment with 1000 obstacles. Although [CPM] offers stronger theoretical guarantees than [FPM], performance is similar (see Table 1). Even though we do not optimize over the time-to-success, both [FPM] and [CPM] achieve the task within a reasonable time while remaining collision-free. Computation times are 4-7 $ms$ on a standard laptop (i7-12700H) making the methodologies well suitable for real-time reactive motion generation in dynamic environments.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Real-world experiments on a 7-DOF manipulator", "weight": 1.0} -->

Experiments are performed on the real 7-DOF for the tomato-picking and pouring task where all obstacles, e.g. a bowl, a person's hand and a helmet, are dynamically tracked in real-time via an optitrack system and modeled as spheres. In addition to the collision spheres considered during simulation, a collision sphere is added to the collision geometry on the center of the robotic hand with a diameter of 14 $cm$. The desired actions by TamedPUMA are sent at 30 Hz to a joint impedance controller running at 1000 Hz. Snapshots of a real-world experiment of the [CPM] are illustrated in Fig. 2, Fig. 3 and Fig 4, and the videos in the attached material show several movements for the simulated and real-world experiments using [FPM] and [CPM]. If the obstacles are not blocking the trajectory of the robot, the observed behavior of the proposed methods, [FPM] and [CPM], are similar to [PUMA] and showcases clearly the learned behavior as demonstrated by the human. The user can push the robot away from the goal or change the goal online (Fig. 4), and TamedPUMA recovers from this disturbance.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Real-world experiments on a 7-DOF manipulator", "weight": 1.0} -->

In the presence of obstacles, [FPM] and [CPM] achieve collision avoidance between the considered links on the robot and the obstacles while reaching the goal pose, as illustrated in Fig. 2, and Fig. 3. [Initial pose] \subfigure[Bowl approaches] \subfigure[Avoid the bowl] \subfigure[Avoid the hand] \subfigure[Goal reached] Figure 2: Selected time frames of CPM during a tomato-picking task with the bowl and hand as dynamic obstacles. [Initial pose] \subfigure[Avoid the helmet] \subfigure[Avoid the helmet] \subfigure[Avoid the helmet] \subfigure[Goal reached] Figure 3: Selected time frames of CPM during a pouring task with the yellow helmet as a static obstacle. [Initial pose] \subfigure[Move to goal] \subfigure[Goal reached] \subfigure[Goal moved] \subfigure[Goal reached] Figure 4: Selected time frames of CPM during a pouring task where the goal is changed online by the user.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Real-world experiments on a 7-DOF manipulator", "weight": 1.0} -->

A low-level joint impedance controller tracks the desired velocities and positions, outputting torque commands. This might decrease tracking performance compared to the simulated experiments, but allows users to push the robot away. If the user is no longer applying force to the robot, the system will converge to the goal pose, as illustrated in the videos in the attached material.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Imitation learning via stable motion primitives is a suitable approach for learning motion profiles from demonstrations while providing convergence to the goal. We introduced TamedPUMA, a safe and stable extension of learned stable motion primitives augmented with the recently developed geometric fabrics for safe and stable operations in the presence of obstacles. We proposed two variations, the Forcing Policy Method and Compatible Potential Method, ensuring respectively that the goal is stable, or the stronger notion that the system converges towards the reachable goal. Experiments were carried out both in simulation and in the real world. When trained on a tomato-picking task or pouring task, the proposed TamedPUMA generates a desired motion profile using a [DNN] while taking whole-body collision avoidance and joint limits into account, with a computation time of just 4-7 $ms$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This project has received funding from the European Union through ERC, INTERACT, under Grant 101041863, and by the NXTGEN national program. Views and opinions expressed are however those of the authors only and do not necessarily reflect those of the European Union or the NXTGEN national program. Neither the European Union nor the granting authority can be held responsible for them.
