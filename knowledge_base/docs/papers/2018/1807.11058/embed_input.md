<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust Distributed Planar Formation Control for Higher-Order Holonomic and Nonholonomic Agents

Topics include Multi-agent systems, Robotics, Aerial robotics, Robustness, Online algorithms, Distributed systems, Control, BCB.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a distributed formation control strategy for agents with a variety of dynamics to achieve a desired planar formation. Our approach is based on the barycentric-coordinate-based (BCB) control, which is fully distributed, does not require inter-agent communication or a common sense of orientation, and can be implemented using relative position measurements acquired by agents in their local coordinate frames. This removes the need for global positioning or alignment of local coordinate frames, which are required across several existing strategies. We show how the BCB control for agents with the simplest dynamical model, i.e., the single-integrator dynamics, can be extended to agents with higher-order dynamics such as quadrotors, and nonholonomic agents such as unicycles and cars. Specifically, our extension preserves the desired convergence and robustness guarantees of the BCB approach and is provably robust to saturations in the input and unmodeled linear actuator dynamics for unicycle and car agents. We further show that under our proposed BCB control design, the agents can move along a rotated and scaled control direction without affecting the convergence to the desired formation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This observation is used to design a fully distributed collision avoidance strategy, which is often not considered in the formation control literature. We demonstrate the proposed approach in simulations and further present a distributed robotic platform to test the strategy experimentally. Our experimental platform consists of off-the-shelf equipment that can be used to test and validate other multi-agent algorithms. The code and implementation instructions for this platform are available online.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Technological advances in recent years has made it increasingly possible to deploy a large fleet of agents to cooperatively map and monitor an environment, deliver goods, or manipulate objects. In these applications, the ability to bring the agents to a desired geometric shape is a fundamental building block upon which more sophisticated maneuvering and navigation policies are constructed. By assigning local control laws to individual agents, distributed formation control strategies ensure that a desired geometric shape emerge from the collective behavior of agents. Compared to the centralized methods, distributed strategies have better scalability, naturally parallelized computation, resilience to communication loss and hardware failure, and robustness to uncertainty and lack of global measurements.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we present a unified, distributed control strategy for planar formations of agents with a variety of dynamics. In particular, we consider agents with linear or input-to-state linearizable dynamics, and further extend the results to agents with nonholonomic unicycle and car dynamics. Our approach is based on the barycentric-coordinate-based (BCB) control, which is fully distributed, does not require inter-agent communication or a common sense of orientation, and can be implemented using relative position measurements acquired by agents in their local coordinate frames. We start by formulating a semidefinite program (SDP) to compute the control gains needed for agents with the single-integrator model. Thanks to this design strategy, convergence to the desired formation is invariant to any (strictly) positive scaling of the control vector and any rotation amounting up to $\pm 90^{\circ}$. This observation leads to provable robustness guarantees such as robustness to saturations in the input and disturbances in the control direction. This observation is further exploited to design a fully distributed collision avoidance strategy, which is often not considered in the formation control literature.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The control for single-integrator agents is extended subsequently to agents with higher-order linear, feedback-to-state linearizable, nonholonomic unicycle, and nonholonomic car dynamics. The main challenges addressed in these extensions are to 1) ensure convergence guarantees to the desired formation are preserved; 2) ensure robustness properties are preserved (e.g., robustness to input saturations and unmodeled/unknown linear actuator dynamics); 3) have a unified design by using the same control gains computed from the SDP approach for single-integrator agents. To vet the theoretical results, several simulations are presented for quadrotors, differential drive robots with unicycle dynamics, and cars, where it is shown that agents achieve a desired formation without collision. To typify the results further, the proposed control strategy is tested experimentally on a distributed differential-drive wheeled robotic platform with different numbers of robots and desired formations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A Related Work and Contributions", "weight": 1.0} -->

There exists a notable body of work on distributed formation control (see survey papers ). These works can be differentiated by the assumed sensing and measurements (e.g., global versus relative/local) and the use of inter-agent communication (e.g., allowed versus limited). Examples of methods that require global measurements (e.g., GPS) are. Consensus-based methods, such as, or techniques based on distributed pose estimation, on the other hand, do not require global sensing. However, agents must communicate to peers during the mission to estimate their pose, synchronize their orientation, or register their local coordinate frames with respect to a common heading direction.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Related Work and Contributions", "weight": 1.0} -->

Unlike the aforementioned methods, certain class of formation control strategies are concerned with the most challenging case: when measurements are local/relative and inter-agent communication is limited or not allowed. Examples of the latter class include distance-based, bearing-based, and the BCB formation control strategies. Due to challenging nonlinear dynamics, no distance-based formation control algorithm with global convergence to the desired formation (in the general setting) is known to this day in the literature. Moreover, bearing-based formation control methods with global convergence guarantees require alignment of local coordinate frames. Unlike the aforementioned methods, convergence guarantees of the BCB control to the desired shape are global (except for a measure zero set, which is inconsequential for the implementation).

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A Related Work and Contributions", "weight": 1.0} -->

The BCB control strategy was introduced by Lin et al., who presented the general theory for agents with single-integrator dynamics and derived the (almost) global convergence guarantees. As these guarantees hold for agents with linear dynamics, it is therefore essential to extend them to agents with nonlinear and nonholonomic dynamics that are commonly encountered in robotics applications. In this paper, we leverage the gradient-descent control framework developed by Zhao et al. for agents with nonholonomic dynamics and show that for a subclass of sensing topologies that are undirected and universally rigid, the global convergence guarantees extend to agents with higher-order, input-to-state feedback linearizable, and nonholonomic unicycle and car dynamics. We further show that under the proposed SDP design, robustness guarantees of the BCB control for single-integrator agents extend to agents with unicycle and car dynamics, and the proposed control is provably robust to saturation of the input and unmodeled linear actuator dynamics.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-A Related Work and Contributions", "weight": 1.0} -->

A contribution of this work is a fully distributed collision avoidance strategy that naturally arises from the robustness properties of the control and preserves the stability of the closed-loop system. Much of the distributed formation control literature do not consider collision avoidance (e.g., in the original BCB approach ), and existing collision avoidance approaches are often centralized. Furthermore, an ad hoc augmentation of a distributed formation control strategy with collision avoidance, e.g., using potential functions, can lead to undesired behaviors or even instability (e.g., robots may drift or move in a limit cycle indefinitely).

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-A Related Work and Contributions", "weight": 1.0} -->

We further present a portable and low-cost distributed robotic platform that consists of off-the-shelf components (see Fig. 1). This platform is used to validate our proposed formation control experimentally and can be used to test other multi-agent control strategies. Since the platform is distributed, the number of robots used for an experiment is only limited by the available resources. The code and technical implementation details related to this platform are made available online, and are accessible in the Supplementary Material section.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-A Related Work and Contributions", "weight": 1.0} -->

In order to make the paper self-contained, this comprehensive work contains a summary of the relevant results derived in our previous papers and subsequent extensions after the submission of this manuscript. Specifically, studied the BCB control design under arbitrary switching sensing typologies, presented the initial extension of the BCB control to agents with higher order linear dynamics, presented an augmentation of the BCB control to fix the formation scale with convergence guarantees, and presented the extension to agents with a kinematic unicycle model, particularly for fixed-wing aerial vehicles. Contributions of this work include extension of the BCB control to agents with dynamic unicycle and car models with convergence guarantees even in the presence of unmodeled linear actuator dynamics, and collision avoidance with stability guarantees. These contributions are accompanied by thorough simulation and experimental evaluations on an open-source robotic platform. Our latest extensions expand the BCB control to 3D formations and leverage task assignment to mitigate gridlock scenarios that arise due to the distributed collision avoidance, respectively.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-A Related Work and Contributions", "weight": 1.0} -->

In summary, the main contributions of this paper are

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-A Related Work and Contributions", "weight": 1.0} -->

A distributed, provably convergent and robust formation control strategy for vehicles with a large variety of holonomic and nonholonomic dynamics, which eliminates the need for global position measurements, common heading direction, inter-agent communication, and complete sensing graph required in existing formation control literature.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-A Related Work and Contributions", "weight": 1.0} -->

A fully distributed collision avoidance algorithm naturally incorporated in the formation control strategy with stability guarantees.

<!-- chunk {"id": "body-0016", "role": "body", "section": "I-A Related Work and Contributions", "weight": 1.0} -->

A low-cost distributed robotic platform with off-the-shelf components for validation of formation control pipeline.

<!-- chunk {"id": "body-0017", "role": "body", "section": "I-B Paper Organization", "weight": 1.0} -->

The notation and assumptions used throughout the paper are introduced in Section II. In Section III, the control strategy for agents with single-integrator dynamics is introduced, the SDP gain design algorithm is presented, and robustness of the proposed approach to perturbations and saturated input is proven. Gains designed for single-integrator agents are used in Section IV to extend the control to agents with higher order linear or linearizable holonomic dynamics such as quadrotors. In Sections V and VI, the control is further extended to agents with nonholonomic unicycle and car dynamics, where robustness to saturations in the input and unmodeled dynamics is shown. Additional topics such as collision avoidance, time-varying sensing topologies, scale of the formation, and extension to 3D case are discussed in Section VII. Lastly, in Sections VIII and IX simulation and experimental results are presented to typify the proposed strategy.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Formation Control for Single-integrator Dynamics", "weight": 1.0} -->

In this section, we present the distributed formation control strategy introduced in for agents with single-integrator dynamics. We then propose a novel design approach for finding stabilizing control gains by formulating a convex optimization problem. The results of this section are a cornerstone for formation control of agents with more complicated dynamic models that are discussed in the subsequent sections.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Control Strategy", "weight": 1.0} -->

The single-integrator dynamics can be described as

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Control Strategy", "weight": 1.0} -->

where $q_{i}:={\lbrack x_{i},y_{i}\rbrack}^{\top} \in {\mathbb{R}}^{2}$ is the coordinate of agent $i \in {\mathbb{N}}_{n}$ in a common global coordinate frame (unknown to the agent), and $u_{i} \in {\mathbb{R}}^{2}$ is the control law. To bring the agents to a desired formation, the control law for each agent can be chosen as

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Control Strategy", "weight": 1.0} -->

where $A_{ij} \in {\mathbb{R}}^{2 \times 2}$ are constant control gain matrices that will be designed later, and each has the form

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Control Strategy", "weight": 1.0} -->

Thanks to the commutativity property of the $A_{ij}$ matrices, the closed-loop dynamics with coordinates $q_{i}$ and $q_{j}$ expressed in agents' local coordinate frames is identical to the case that coordinates are expressed in a global coordinate frame (for more details see ). The geometric intuition behind the control strategy is explained in the following example.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example 1", "weight": 1.0} -->

Consider three agents in Fig. 2, where agents 2 and 3 are neighbors of agent 1. Let $q_{2} = {\lbrack 2,\, 3\rbrack}^{\top}$ and $q_{3} = {\lbrack 3,\, 1\rbrack}^{\top}$ denote the position of neighbors in agent 1's local coordinate frame, and assume that control gains for agent 1 are given as

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example 1", "weight": 1.0} -->

From, the control vector for agent 1 is computed as

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example 1", "weight": 1.0} -->

which is shown in the figure and can be interpreted geometrically as follows. At any instance of time, agent 1 moves along the control vector with the speed equal to the vector's magnitude. Note that due to the special structure of gain matrices $A_{12},A_{13}$, they can be interpreted as scaled rotation matrices that rotate and scale vectors connecting agent 1 to its neighbors. One can see that this action is independent of agent 1's local coordinate frame position and orientation, hence, $q_{1}$ and $q_{2}$ can replaced by their coordinates in a global coordinate frame for analysis.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example 1", "weight": 1.0} -->

Let $q:={\lbrack q_{1}^{\top},q_{2}^{\top},\ldots,q_{n}^{\top}\rbrack}^{\top} \in {\mathbb{R}}^{2n}$ denote the aggregate state vector of all agents. Using this notation, the closed-loop dynamics under the control strategy can be expressed as

<!-- chunk {"id": "body-0027", "role": "body", "section": "Example 1", "weight": 1.0} -->

where for $j \notin \mathcal{N}_{i}$ the $A_{ij}$ block is defined as a zero matrix. Note that the $2 \times 2$ diagonal blocks of $A$ are the negative sum of the rest of the blocks on the same row. Hence, $A$ has block Laplacian structure, and it follows that vectors

<!-- chunk {"id": "body-0028", "role": "body", "section": "Example 1", "weight": 1.0} -->

Let $q^{\ast} \in {\mathbb{R}}^{2n}$ denote the coordinates of agents at the desired formation (the orientation, translation, and scale of the desired formation can be chosen arbitrarily). Further, let ${\overline{q}}^{\ast} \in {\mathbb{R}}^{2n}$ denote the coordinates of agents when the desired formation is rotated by $90$ degrees about the origin. The following theorem states the conditions that guarantee the convergence of agents to the desired formation.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The topological conditions that guarantee the existence of a symmetric matrix $A$ satisfying the conditions of Theorem 1 are studied in \[25, Thm. 3.2\], which presents the necessary and sufficient condition^22^2To be specific, the necessary and sufficient condition is for a generic desired formation. For certain desired formations matrix $A$ exists even when the graph is not universally rigid. that the sensing graph is undirected and universally rigid. Throughout this paper, we assume that this condition is met.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Motion of the ensemble set of agents, during and after getting into formation, can be addressed in various ways. We have previously employed leader-follower strategies and preassigned high-level control tasks. Such a task may require global information and is not discussed further here.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B Control Gain Design", "weight": 1.0} -->

Given a desired formation for agents with a universally rigid sensing topology, we present a novel algorithm to find control gain matrices that meet the conditions of Theorem 1. Let $N:={\lbrack q^{\ast},{\overline{q}}^{\ast},\, 1,\overline{\mathbf{1}}\rbrack} \in {\mathbb{R}}^{{2n} \times 4}$ be the set of bases for the kernel of $A$, where $\mathbf{1},\overline{\mathbf{1}}$ are given, $q^{\ast} \in {\mathbb{R}}^{2n}$ is the coordinates of agents at the desired formation, and ${\overline{q}}^{\ast}{\mathbb{R}}^{2n}$ is the $90^{\circ}$ rotated coordinates about the origin.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B Control Gain Design", "weight": 1.0} -->

Let ${USV^{\top}} = N$ be the (full) singular value decomposition (SVD) of $N$, where

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-C Robustness to Perturbations", "weight": 1.0} -->

An important characteristic of the proposed design approach is that the gains found via lead to significant robustness to perturbations. For instance, noise and disturbances can cause an agent to move in a direction that is different from the desired control vector. The following theorem shows that by using the gains computed from positive scaling and rotation of the control vectors (up to $\pm 90^{\circ}$) does not affect the convergence.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-D Robustness to Saturated Input", "weight": 1.0} -->

In practice, the velocity of an agent cannot take arbitrary large values. Thus, any large control input will be saturated by a maximum feasible/allowed speed. This, however, does not affect convergence of agents to the desired formation.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 3", "weight": 1.0} -->

To reject steady state errors, the control law can be augmented by an integrator term as

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 3", "weight": 1.0} -->

where ${k_{0},k_{1}} \in {\mathbb{R}}$ are scalar control gains. It can be shown that if ${k_{0},k_{1}} > 0$, this augmented control rejects constant input/output disturbances (see \[38, Sec. III-D\] for more details).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 4", "weight": 1.0} -->

The robustness properties of control, such as robustness to positive scaling and rotations up to $\pm 90^{\circ}$, are similar to the properties of the first-order consensus methods. This originates from the structure of the Lyapunov analysis that is similar in both approaches. However, consensus-based methods require alignment of agents' local coordinate frames, whereas the formation control strategy studied in this work does not have this constraint.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Formation Control for Agents with Higher-order Dynamics", "weight": 1.0} -->

In this section, we extend the single-integrator control strategy to agents with higher-order dynamics. We show how the control gains designed for single-integrator agents in Section III-B can be used directly to control higher-order agents without having to find a new control strategy or redesign the gains by solving a new optimization problem. This means the same formation can be regulated for any type of vehicle using the same gains. We assume that the aggregate higher-order dynamics of all agents can be expressed in the controllable canonical form

<!-- chunk {"id": "body-0039", "role": "body", "section": "Formation Control for Agents with Higher-order Dynamics", "weight": 1.0} -->

where $q \in {\mathbb{R}}^{2n}$ is the aggregate position vector of all agents, $q^{(j)} \in {\mathbb{R}}^{2n}$ denotes the $j$'th derivative of $q$, and $I \in {\mathbb{R}}^{n \times n}$ is the identity matrix. Although at first sight may seem restrictive, in fact, it encompasses a large class of agents. This is because by coordinate transformation techniques such as feedback linearization, or approximation techniques such as linearization and gain scheduling, dynamics of many systems can be expressed as.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Formation Control for Agents with Higher-order Dynamics", "weight": 1.0} -->

Given the gain matrix $A$ designed for agents with the single-integrator model, the control for agents with dynamics can be chosen as

<!-- chunk {"id": "body-0041", "role": "body", "section": "Formation Control for Agents with Higher-order Dynamics", "weight": 1.0} -->

where ${k_{0},k_{1},\ldots,k_{m}} \in {\mathbb{R}}$ are scalar control gains, and $u:={\lbrack u_{1}^{\top},u_{2}^{\top},\ldots,u_{n}^{\top}\rbrack}^{\top} \in {\mathbb{R}}^{2n}$ denote the aggregate control vector. Note that can be implemented locally using only the relative measurements (due to the special structure of $A$). Under this control, the closed-loop dynamics is given by

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 5", "weight": 1.0} -->

In the above analysis, the control can alternatively be chosen as

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 5", "weight": 1.0} -->

In this case, agents do not need measurements of states $q^{},\ldots,q^{(m)}$ for their neighbors (since $A$ is replaced by the identity matrix). Note that can also be implemented using only the local relative measurements.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 6", "weight": 1.0} -->

There are several methods that can be used to determine the relative position of agents; e.g., our previous work used vision sensors. LIDAR could be used to augment vision for accurate displacement measurements. In what was discussed above, relative velocity, acceleration, etc., can be computed by taking time derivatives of the measured relative position and using appropriate filtering when measurements are noisy.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example 2", "weight": 1.0} -->

where, as illustrated in Fig. 4, ${x,y,z} \in {\mathbb{R}}$ are coordinates of the quadrotor's center of mass in the world frame, $\varphi,\theta,\psi$ are roll, pitch, yaw angles that describe the orientation of the quadrotor body frame in the world frame, $\omega_{x},\omega_{y},\omega_{z}$ are the angular body rates about associated body axes, $g$ is the gravitational constant, $u^{a}$ is a mass-normalized thrust input, and $u^{x},u^{y},u^{z}$ are moment inputs applied to the airframe about corresponding body axes. Further, $J \in {\mathbb{R}}^{3 \times 3}$ is the mass moment of inertia matrix, $R \in {{SO}{}}$ is the rotation matrix parameterized in terms of $z$-$x$-$y$ Euler angles as

<!-- chunk {"id": "body-0046", "role": "body", "section": "Example 2", "weight": 1.0} -->

where $c,s$ are respectively shorthand notations for ${\cos{( \cdot )}},{\sin{( \cdot )}}$ functions, and

<!-- chunk {"id": "body-0047", "role": "body", "section": "Example 2", "weight": 1.0} -->

is the transformation matrix that relates the roll, pitch, yaw derivatives to the angular velocities in the body frame.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Example 2", "weight": 1.0} -->

where $\delta$ represents a small displacement about the equilibrium/linearization point. Since we are interested in 2D formations, we only consider the lateral dynamics along the $x$-$y$ axes, and separately control the quadrotor's altitude by setting $u^{a} = \frac{g}{c_{\varphi}c_{\theta}}$ to stabilize it at a constant altitude.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Example 2", "weight": 1.0} -->

To represent the dynamics in the canonical form, we define

<!-- chunk {"id": "body-0050", "role": "body", "section": "Example 2", "weight": 1.0} -->

where subscript $i$ is used to distinguish agents. Using this notation, can be described in the vector form as

<!-- chunk {"id": "body-0051", "role": "body", "section": "Example 2", "weight": 1.0} -->

are respectively the state and control vectors, and $I \in {\mathbb{R}}^{2 \times 2}$ is the identity matrix. Note that by defining the aggregate position vector as $q = {\lbrack{\deltax_{1}},{\deltay_{1}},\ldots,{\deltax_{n}},{\deltay_{n}}\rbrack}^{\top}$, dynamics of agents can be expressed in the form. This model will be used in the Simulations section to achieve a desired formation.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Formation Control for Agents with Unicycle Dynamics", "weight": 1.0} -->

Motion profile of many vehicles, e.g., differential drive robots or fixed-wing aerial vehicles, can be described via the unicycle model. In this section, we introduce the unicycle model and propose a formation control strategy to achieve the desired formation using the control gains that were designed for single-integrator agents. We then show that the desired formation is achieved even if the input is saturated, and the control strategy is robust to unknown dynamics that are not considered in the kinematic unicycle model. We assume henceforth that a symmetric negative semidefinite gain matrix $A$ is designed for the desired formation by solving the optimization problem.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-A Unicycle Dynamics", "weight": 1.0} -->

Consider a unicycle agent located at position ${\lbrack x_{i},y_{i}\rbrack}^{\top} \in {\mathbb{R}}^{2}$ in a global coordinate frame (unknown to the agent), and assume that the unicycle's heading direction makes angle $\theta_{i} \in {\lbrack 0,{\, 2\pi})}$ with the $x$-axis of the global coordinate frame. This scenario is illustrated in Fig. 5. The unicycle dynamics can be described in the global coordinate frame by

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-A Unicycle Dynamics", "weight": 1.0} -->

where scalars ${v_{i},\omega_{i}} \in {\mathbb{R}}$ are respectively the linear and angular velocities of the agent. In the unicycle kinematic model, it is assumed that $v_{i}$ and $\omega_{i}$ are control variables and can be changed instantaneously.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-A Unicycle Dynamics", "weight": 1.0} -->

In the global coordinate frame, the unit norm heading vector of the unicycle, $h_{i} \in {\mathbb{R}}^{2}$, and its perpendicular vector $h_{i}^{\perp} \in {\mathbb{R}}^{2}$, are given by

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-A Unicycle Dynamics", "weight": 1.0} -->

Let $q:={\lbrack q_{1}^{\top},q_{2}^{\top},\ldots,q_{n}^{\top}\rbrack}^{\top} \in {\mathbb{R}}^{2n}$ be the aggregate position vector of all agents, and similarly let $h \in {\mathbb{R}}^{2n}$, $v \in {\mathbb{R}}^{n}$, $\omega \in {\mathbb{R}}^{n}$ be the aggregate heading, linear velocity, and angular velocity vectors, respectively. Using this notation, the motion of all agents can be collectively expressed as

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-B Control Strategy", "weight": 1.0} -->

Consider a team of $n$ unicycle agents with dynamics. We seek to assign controls $v_{i}$ and $\omega_{i}$ such that agents autonomously achieve a desired formation. Let $A \in {\mathbb{R}}^{{{2n} \times 2}n}$ be a symmetric gain matrix designed in Section III-B for agents with single-integrator model to achieve the desired formation. Further, let $u_{i}$ given in be the desired holonomic control direction for agent $i$. The proposed control strategy is as follows. Each agent computes the control vector $u_{i}$ and projects it on its local heading and perpendicular heading directions. The projected vectors are then used as the linear and angular velocity commands. In the global coordinate frame, which is unknown to agent, this strategy can be described by

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-B Control Strategy", "weight": 1.0} -->

as illustrated in Fig. 5. Implementation of does not rely on a global coordinate system. This is because $h_{i}$ is a unit vector along the direction of vehicle, which is known by the agent locally, and $u_{i}$ is the single-integrator control given in the agent's local coordinate frame.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 7", "weight": 1.0} -->

From the closed-loop dynamics one can see that when agents are at the desired formation, i.e., ${Aq} = 0$, we have $\overset{˙}{h} = 0$ and hence the heading directions do not vary. This implies that the controller drives agents to the desired formation, however their heading at the desired formation is not controlled and can take an arbitrary value. If desired, a supplementary control can be added to regulate heading angles after convergence.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Remark 8", "weight": 1.0} -->

It is worth pointing out that the control can drive unicycle agents with a cart attached to the desired formation. In this case the position and orientation of the attached carts are not controlled. The dynamics of a unicycle agent with cart attached is similar to the dynamics of a car, which is studied in the next section.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-C Robustness to Saturated Input", "weight": 1.0} -->

In practice, the linear and angular velocities that an agent can execute are often limited to a certain range. We show that under a saturated input, convergence of agents to the desired formation is not affected.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-D Robustness to Unmodeled Linear Actuator Dynamics", "weight": 1.0} -->

In practice, the linear and angular velocities of a vehicle cannot change instantaneously. The dynamic behavior of these velocities, which is not accounted for in the unicycle model, can be modeled by

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-D Robustness to Unmodeled Linear Actuator Dynamics", "weight": 1.0} -->

where ${s_{i},r_{i}} \in {\mathbb{R}}$ are controls to adjust the linear and angular velocities, and ${a,b,c,d} \in {\mathbb{R}}$ are strictly positive scalars, which depend on the vehicle's inertia, motor dynamics, friction, etc., and are in general unknown. We show that unmodeled velocity dynamics does not affect the convergence of the unicycle control strategy. That is, applying the control

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 9", "weight": 1.0} -->

In, we assumed that $a,b,c,d$ have the same value for all agents. This assumption was made to simplify the notation and does not affect the generality of the results. One can assign a different value to these parameters for each agent and use the same analysis to prove the convergence.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 10", "weight": 1.0} -->

In, the assumption ${a,c} > 0$ implies that agents are zero-input stable, which often holds in practice. However, for ${a,c} < 0$ the control can be modified using the velocity feedback as

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 10", "weight": 1.0} -->

where $k_{s} \in {\mathbb{R}}$ is a positive control gain. Using similar analysis to the proof of Theorem 7, one can show that if $k_{s}$ is chosen such that ${a + {k_{s}b}} > 0$, the agents converge to the desired formation. Lastly, with multiplying $s_{i},r_{i}$ by the sign of $b,d$, respectively, the assumption ${b,d} > 0$ can be relaxed to only knowing the sign of these parameters.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Formation Control for Agents with Car Dynamics", "weight": 1.0} -->

Cars are another common platform for which attaining a desired formation is often of interest (e.g., in intelligent transportation systems). In this section, we present a control strategy for agents with both front and rear-wheel drive car model. We then show that the convergence is not affected when the input is saturated, and the control is robust to unmodeled dynamics. Similar to previous section, henceforth we assume that a symmetric negative semi-definite control gain matrix $A$ is designed by solving the optimization problem.

<!-- chunk {"id": "body-0068", "role": "body", "section": "VI-A Control Strategy for Front-Wheel Drive Car", "weight": 1.0} -->

Consider an agent with the front-wheel drive car model as illustrated in Fig. 6. The motion of this agent can be described by the dynamics

<!-- chunk {"id": "body-0069", "role": "body", "section": "VI-A Control Strategy for Front-Wheel Drive Car", "weight": 1.0} -->

where ${x_{i},y_{i}} \in {\mathbb{R}}^{2}$ are the coordinates of the front axle's center, $v_{i} \in {\mathbb{R}}$ is the driving velocity, $\theta_{i} \in {\lbrack 0,{\, 2\pi})}$ is the heading angle, $\varphi_{i} \in {\lbrack 0,{\, 2\pi})}$ is the steering angle, $\omega_{i}$ is the steering velocity, and $l \in {\mathbb{R}}$ is the wheelbase. In this kinematic model, it is assumed that $v_{i}$ and $\omega_{i}$ are inputs and can be controlled directly. By defining

<!-- chunk {"id": "body-0070", "role": "body", "section": "VI-A Control Strategy for Front-Wheel Drive Car", "weight": 1.0} -->

Note that to simplify the notation, we have assumed that $l$ is identical for all agents. This does not affect the generality of the following results, and one can carry the following analysis with a different $l$ for each agent.

<!-- chunk {"id": "body-0071", "role": "body", "section": "VI-A Control Strategy for Front-Wheel Drive Car", "weight": 1.0} -->

From, the dynamics of all agents can be collectively expressed in the vector form

<!-- chunk {"id": "body-0072", "role": "body", "section": "VI-A Control Strategy for Front-Wheel Drive Car", "weight": 1.0} -->

where ${q,g,h} \in {\mathbb{R}}^{2n}$ are aggregate state, steering, and heading vectors, and ${v,\omega} \in {\mathbb{R}}^{n}$ are aggregate control vectors. Further, $H,H^{\perp}$ are defined according to, and $G,G^{\perp}$ are defined by replacing $h_{i}$'s by $g_{i}$'s.

<!-- chunk {"id": "body-0073", "role": "body", "section": "VI-A Control Strategy for Front-Wheel Drive Car", "weight": 1.0} -->

Using a similar strategy to the unicycle agents in Section V, we define the driving and steering velocity controls as the projections of the holonomic control vector along the steering direction and its perpendicular by

<!-- chunk {"id": "body-0074", "role": "body", "section": "VI-A Control Strategy for Front-Wheel Drive Car", "weight": 1.0} -->

where $u_{i}$ is given. We emphasize that can be implemented using only the local relative position measurements.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Remark 11", "weight": 1.0} -->

Similar to the unicycle agents, the final heading and steering angles of agents with car dynamics at the the desired formation are not controlled and can take arbitrary values.

<!-- chunk {"id": "body-0076", "role": "body", "section": "VI-B Control Strategy for Rear-Wheel Drive Car", "weight": 1.0} -->

The dynamics of a rear-wheel drive car is identical to the front-wheel drive car except that the front wheels' driving velocity $v_{i}$ is indirectly controlled via the rear wheels' driving velocity $v_{i}^{r}$. The relation between the front and rear wheels' driving velocities is given by

<!-- chunk {"id": "body-0077", "role": "body", "section": "VI-B Control Strategy for Rear-Wheel Drive Car", "weight": 1.0} -->

To set $v_{i}$ to the desired value defined, from we have that the rear wheels' driving velocity should be

<!-- chunk {"id": "body-0078", "role": "body", "section": "VI-B Control Strategy for Rear-Wheel Drive Car", "weight": 1.0} -->

The main difference between the rear and front-wheel drive car is that when $\varphi_{i} = {\pm \frac{\pi}{2}}$, from $v_{i}^{r}$, and hence $v_{i}$, become zero. On the contrary, $v_{i}$ in a front-wheel drive car can take any desired value in this case (one can interpret this as the car pivoting about its rear wheels).

<!-- chunk {"id": "body-0079", "role": "body", "section": "Remark 12", "weight": 1.0} -->

Due to noise, unmodeled dynamics, disturbances, etc., in practice agents cannot stay on a measure zero set of trajectories. Furthermore, as we will show subsequently, the steering angle of a car can be bounded to remain less than $\pm \frac{\pi}{2}$ and avoid the undesired case (ii) in the proof. Consequently, the "almost\" global convergence of rear-wheel drive car in Theorem 9 does not affect the applicability of the control strategy.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Remark 12", "weight": 1.0} -->

Due to the similarity of the dynamics and analysis for the front and rear-wheel drive car models, we only consider the front-wheel drive car model throughout the rest of this section.

<!-- chunk {"id": "body-0081", "role": "body", "section": "VI-C Robustness to Saturated Input and Bounded Steering Angle", "weight": 1.0} -->

The steering angle and the driving and steering velocities of a car often cannot take arbitrary values and must be bounded by practical limits. This, however, does not affect the convergence of the agents to the desired formation.

<!-- chunk {"id": "body-0082", "role": "body", "section": "VI-D Robustness to Unmodeled Linear Actuator Dynamics", "weight": 1.0} -->

Since in practice the driving and steering velocities of a car cannot change instantaneously, the car dynamics can be modified as

<!-- chunk {"id": "body-0083", "role": "body", "section": "VI-D Robustness to Unmodeled Linear Actuator Dynamics", "weight": 1.0} -->

to incorporate the dynamics of these velocities. In, ${s_{i},r_{i}} \in {\mathbb{R}}$ are control inputs to adjust the driving and steering velocities. Further, we assume that ${a,b,c,d} \in {\mathbb{R}}$ are strictly positive, but unknown. The following theorem shows that the unmodeled velocity dynamics does not affect the convergence of the control strategy. That is, applying the control

<!-- chunk {"id": "body-0084", "role": "body", "section": "Remark 13", "weight": 1.0} -->

On a similar note to Remarks 9 and 10, in parameters $a,b,c,d$ can take different values for each agent. Further, if $k_{s} \in {\mathbb{R}}$ is chosen such that ${a + {k_{s}b}} > 0$, the modified control

<!-- chunk {"id": "body-0085", "role": "body", "section": "Remark 13", "weight": 1.0} -->

can bring agents with ${a,c} < 0$ to the desired formation.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Extensions and Variations", "weight": 1.0} -->

In this section, we briefly address additional topics such as collision avoidance, stability under a time-varying sensing topology, and formation scale adjustment, which are important in a practical implementation.

<!-- chunk {"id": "body-0087", "role": "body", "section": "VII-A Collision Avoidance", "weight": 1.0} -->

As discussed in Section III-C, by using the control gains computed from Algorithm 1, positive scaling and rotation of the the control vectors up to $\pm 90^{\circ}$ does not affect convergence of agents to the desired formation. This observation can be used to implement a distributed collision avoidance strategy. Fig. 7 illustrates a scenario where the desired control direction of agent $i$ can potentially cause collision with an adjacent agent. Tangent lines from agent $i$ to circles of radius $r \in {\mathbb{R}}$ centered at the adjacent agents define collision avoidance cones, where by rotating the control vector to a direction outside of these cones the collision is prevented. To preserve the stability properties, the rotation is limited to $\pm 90^{\circ}$ of the original control direction, e.g., in Fig. 7 the control $u_{i}$ cannot be rotated below the solid black line. In a case where there is no possible direction of motion within the allowed rotation range the control is set to zero, and the agent stops until a feasible control direction is available.

<!-- chunk {"id": "body-0088", "role": "body", "section": "VII-A Collision Avoidance", "weight": 1.0} -->

To alter the control direction as little as possible, one can define a distance threshold $d_{c} \in {\mathbb{R}}$ such that the collision avoidance strategy is triggered only when the distance to an adjacent agent is less than this threshold. The above collision avoidance strategy is outlined in Algorithm 2. Note that this strategy is distributed and does not required inter-agent communication.

<!-- chunk {"id": "body-0089", "role": "body", "section": "VII-A Collision Avoidance", "weight": 1.0} -->

If the initial inter-agent distances are greater than $r$, it is straightforward to show that collision avoidance is guaranteed for single-integrator agents under Algorithm 2 (this follows by showing that inter-agent distances cannot become less than $r$). For agents with higher-order dynamics, $r$ should be chosen large enough to accommodate for the maximum braking distance. We should point out that convergence to the desired formation under the proposed strategy is heuristic and not always guaranteed. In particular, one can construct counter examples where agents are caught in a gridlock due to unavailability of feasible control direction. However, in our simulation and experimental studies we observed that if agents are initially spaced far apart, they can resolve gridlocks and converge to the desired formation. We are not aware of any existing collision avoidance strategy that is distributed, does not require communication, and can guarantee convergence of agents to the desired formation. Commonly used distributed strategies such as safety barrier functions and traffic circles have similar gridlock situations. We point out that in scenarios where inter-agent communication is possible, distributed task assignment techniques can be leveraged to resolve gridlocks (see our recent work ).

<!-- chunk {"id": "body-0090", "role": "body", "section": "VII-A Collision Avoidance", "weight": 1.0} -->

On the other hand, under the proposed strategy, stability of the overall system is guaranteed by Theorem 2. This distinguishes the proposed strategy from an ad hoc augmentation of the control to avoid collision, e.g., via potential functions. Such augmentations may lead to undesired behavior or instability of the overall system. For example, they may cause the robots to drift along a direction or circle in a limit cycle indefinitely. Such behaviors are not present in the proposed approach, and if the robots do not go to a gridlock, convergence to the desired shape is guaranteed.

<!-- chunk {"id": "body-0091", "role": "body", "section": "VII-A Collision Avoidance", "weight": 1.0} -->

input: Desired control direction ui ∈ ℝ2
Collision circle radius r ∈ ℝ
output: Modified control direction ui′ ∈ ℝ2
step 1: Construct collision cones with circles of radius r centered at agents closer than dc.
step 2: Find rotation R (θ) ∈ SO with minimum |θ| such that R ui is outside of collision cones.
step 3: If step 2 is infeasible or |θ| ≥ 90∘ set ui′ = 0, otherwise set ui′ = R (θ) ui.
Algorithm 2 Distributed collision avoidance.

<!-- chunk {"id": "body-0092", "role": "body", "section": "VII-B Time-Varying Sensing Topology", "weight": 1.0} -->

In a time-varying or switching sensing topology, the agents can lose or acquire sensing capability of other agents in the group. For example, if a vision sensor is used to provide position measurements, sensing capability is lost when a neighbor agent is obstructed by another agent and acquired when an agent moves in the line of sight. The following theorem shows that by using the proposed gain design approach a switching sensing topology does not affect the convergence of single-integrator agents to the desired formation.

<!-- chunk {"id": "body-0093", "role": "body", "section": "VII-C Scale Adjustment", "weight": 1.0} -->

To fix the scale of the final formation, control law can be augmented by a bounded smooth map $f:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ as

<!-- chunk {"id": "body-0094", "role": "body", "section": "VII-C Scale Adjustment", "weight": 1.0} -->

where $d_{ij}:={\|{q_{j} - q_{i}}\|}$ denote the distance between agent $i$ and $j$, $d_{ij}^{\ast} \in {\mathbb{R}}$ is its desired value, and $f$ is chosen such that ${xf{(x)}} > 0$ for $x \neq 0$, and ${f{}} = 0$. Possible choices for $f$ are $f:{x\mapsto{\frac{1}{k}{\arctan{(x)}}}}$ or $f:{x\mapsto{\frac{1}{k}{\tanh{(x)}}}}$, where $k > 0$ is an arbitrary constant. The role of $f$ in is to pull agents toward their neighbors when the distance between them is larger than the desired value, and vice versa. For agents with single-integrator dynamics, we have shown that agents almost globally converge to the desired formation.

<!-- chunk {"id": "body-0095", "role": "body", "section": "VII-C Scale Adjustment", "weight": 1.0} -->

The study of global asymptotic stability for agents with higher order dynamics is a topic of future research.

<!-- chunk {"id": "body-0096", "role": "body", "section": "VII-D 3D Formations", "weight": 1.0} -->

The proposed control approach, together with the convergence and robustness properties, can be extended to 3D formations. This extension has been done in our recent work, where experimental validations on a fleet of Crazyflie quadrotors are performed to demonstrate the strategy.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Simulations", "weight": 1.0} -->

To validate the proposed approach, we present several simulations for planar formation of quadrotors, unicycles, and cars. Links to simulation code and videos are provided in the Supplementary Material section.

<!-- chunk {"id": "body-0098", "role": "body", "section": "VIII-A Quadrotors", "weight": 1.0} -->

Based on the quadrotor dynamics described in Example 2, a simulation with 9 quadrotors and a scale-free square grid desired formation is performed. Although the control design is based on the linearized dynamics about the quadrotor's hover point, the original nonlinear quadrotor dynamics given in is used for the simulation. To demonstrate robustness to switches in the inter-agent sensing topology, the sensing graph is switched among the topologies illustrated in Fig. 8 based on a randomly generated switching signal shown in the figure. We further performed simulations in which the topology changes are based on the robots' proximity. Since performance was similar to the results presented here, we do not report the results, however, they can be viewed in the supplemental video available at The control gains associated with the desired formation are computed from Algorithm 1, where we used to obtain gains that jointly stabilize all topologies. The nonzero eigenvalues of computed $A \in {\mathbb{R}}^{18 \times 18}$ matrices range from $- 0.035$ to $- 0.497$.

<!-- chunk {"id": "body-0099", "role": "body", "section": "VIII-A Quadrotors", "weight": 1.0} -->

The control law used for each quadrotor is chosen according to, where gains are set as ${k_{0} = 2},{{k_{1} = 2},{{k_{2} = 3},{k_{3} = 3}}}$ to make the closed-loop state matrix $\overline{A}$ stable for all topologies. Using these gains, the real part of nonzero eigenvalues of $\overline{A}$ matrices range from $- 0.038$ to $- 2.0$. To avoid collision among quadrotors, the distributed collision avoidance strategy in Algorithm 2 with $d_{c} = 8$ and $r = 4$ units of length is employed.

<!-- chunk {"id": "body-0100", "role": "body", "section": "VIII-A Quadrotors", "weight": 1.0} -->

Fig. 9(a)-(e) shows the top view of quadrotors at different time instances. The sensing graph among agents is shown by gray lines connecting the quadrotors. This sensing graph switches throughout the simulation according to Fig. 8. The initial positions of the quadrotors are chosen randomly, and are shown in Fig. 9(a). As can be seen in Figs. 9(b)-(e), the proposed control strategy brings the agents to the desired formation. Note that when the distance between two quadrotors becomes less than 8 units of length, the collision avoidance strategy is engaged to rotate the control direction outside of the collision cone. Consequently, none of the quadrotors collide during the simulation. Further notice that since the control only uses the local relative position measurements, the desired formation is achieved up to a rotation and translation. That is, the orientation of the square formation is not controlled.

<!-- chunk {"id": "body-0101", "role": "body", "section": "VIII-A Quadrotors", "weight": 1.0} -->

We point out that in the quadrotor Example 2, the inputs are $u^{x},u^{y}$ and the outputs are the $x$-$y$ positions (since we are concerned with planar formations). The input $u^{a}$ affects the $x$-$y$ positions through $R$ due to the coupled dynamics, and the zero dynamics consists of the state variables $z,\psi,\omega_{z}$, which are unobservable from the outputs, however, are asymptotically stable. The theoretical convergence guarantees of the proposed control are based on the assumption of input-to-state feedback linearizability. Nonetheless, as can be seen from the simulation results which are based on the original nonlinear dynamics, the quadrotors achieve the desired formation. This suggests potential applicability of the proposed control to systems with asymptotically stable zero dynamics, which can be expected due to the robustness properties.

<!-- chunk {"id": "body-0102", "role": "body", "section": "VIII-B Unicycles", "weight": 1.0} -->

The control strategy for agents with unicycle dynamics is considered in a simulation with 9 unicycles and a square grid desired formation. The unicycle dynamics are used to test the performance of control in the presence of unmodeled dynamics, where values of parameters $a,b,c,d$ are chosen randomly for each agent with uniform distribution in the interval $\lbrack 5,\, 10\rbrack$. All linear and angular velocities are saturated by the maximum allowed velocities of $v_{\max} = 3$ units of length per second and $\omega_{\max} = {\pi/4}$ radians per second, respectively. The control gain matrices designed for quadrotors in the previous section are used for unicycle agents, showing that the control gains found from Algorithm 1 can be used for vehicles with a variety of dynamics to achieve the same desired formation.

<!-- chunk {"id": "body-0103", "role": "body", "section": "VIII-B Unicycles", "weight": 1.0} -->

To allow a better comparison between trajectories of agents with different dynamics, the unicycle agents start from the same initial condition as quadrotors, as can be seen in Fig. 10(a), and the sensing topology among them switches according to Fig. 8. The position of agents at other time instances are shown in Figs. 10(b)-(e), where by using the collision avoidance strategy in Algorithm 2 with $d_{c} = 8$ and $r = 4$ units of length, no collisions occur as the unicycles converge to the desired formation. Similar to quadrotors, the desired formation is scale-free and achieved up to a rotation and translation with respect to the global coordinate frame that is unknown to agents.

<!-- chunk {"id": "body-0104", "role": "body", "section": "VIII-C Cars", "weight": 1.0} -->

The control strategy for agents with front-wheel drive car dynamics is considered in a simulation with 9 cars and a square grid desired formation. The car dynamics is used to test the performance of control in the presence of unmodeled dynamics, where values of parameters $a,b,c,d$ are chosen as the same values for unicycle agents to allow a better comparison. The driving and steering velocities of cars are saturated by the maximum allowed velocities of $v_{\max} = 3$ units of lengths per second and $\omega_{\max} = {\pi/4}$ radians per second, respectively. Furthermore, all steering angles are confined to the interval of $\lbrack{- {\pi/4}},{\pi/4}\rbrack$ radians to model the practical bounds on the steering angle of wheels in cars. The control gain matrices used for quadrotors and unicycles are used in the simulation.

<!-- chunk {"id": "body-0105", "role": "body", "section": "VIII-C Cars", "weight": 1.0} -->

The sensing topology switches according to Fig. 8, and the initial position of cars is shown in Fig. 11(a), which is the same as quadrotors and unicycles to allow a better comparison. The position of cars at other instances of time are shown in Figs. 11(b)-(e), where by using the collision avoidance strategy with $d_{c} = 8$ and $r = 4$ units of length no collisions occur as the cars converge to the desired formation. Note that the attained square grid formation is with respect to the front axle's center of each car, i.e., the origin of car's local coordinate frame in Fig. 6. Furthermore, the heading of the cars at the final formation is not specified and can take an arbitrary value.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In this section, we validate the proposed control strategies experimentally on a distributed multi-robot platform. Our experimental study is limited to the cases of single-integrator and unicycle dynamics, as we do not have a fleet of autonomous cars. Links to the implementation code and technical details is provided in the Supplementary Material section.

<!-- chunk {"id": "body-0107", "role": "body", "section": "IX-A Experimental Platform", "weight": 1.0} -->

Our experimental platform consists of the Sphero 2.0 robots, laptop computers with Bluetooth adapters to control the robots, and Logitech C920 webcams to provide vision feedback. As illustrated in Fig. 12, a group of Sphero robots are placed in an arena that is overseen by webcams. The video stream provided by each webcam is used in an image processing script to detect and track the Spheros via blob detection \[55, Sec.13.1\]. The coordinates of each robot are estimated by mapping the pixel position of the robot in the image to the $x$-$y$ Euclidean coordinates on the arena floor. This is done by initially placing a checkerboard at an arbitrary location on the floor and using PnP algorithm to estimate the relative orientation of the ground plane in the camera's coordinate frame. The coordinates are then given by finding the intersection of the ray through the robot image and the ground plane generated by PnP.

<!-- chunk {"id": "body-0108", "role": "body", "section": "IX-A Experimental Platform", "weight": 1.0} -->

The estimated coordinates of Spheros are used by each computer to calculate the control according to the specified distributed formation control strategy. The desired control action is then communicated to each robot over Bluetooth. The experimental setup is distributed in the sense that each computer is responsible for controlling a subset of robots, and computers do not communicate during the experiment. Furthermore, the control computed by each computer respects the sensing graph specified by the user and does not use any additional information that may be available.

<!-- chunk {"id": "body-0109", "role": "body", "section": "IX-A Experimental Platform", "weight": 1.0} -->

The schematics of a Sphero robot are shown in Fig. 13. The robot consists of a differential-wheeled internal platform that is enclosed in a spherical shell. Rotation of the internal wheels induces a roll motion of the outer shell. To test the control strategy proposed for single-integrator agents, a low-level PID controller is employed to first orient the internal platform along the desired direction, and then roll the robot forward at the desired speed. For the unicycle agents, the low-level PID controller adjusts the wheel velocities such that the internal differential drive platform have the desired angular and linear velocities.

<!-- chunk {"id": "body-0110", "role": "body", "section": "IX-B Triangle Formation", "weight": 1.0} -->

Our first set of experiments correspond to an equilateral triangle formation with 6 robots. For this experiment only two computers are used, where the first computer controls robots numbered 1 to 3, and the remaining robots are controlled by the second computer. The sensing topology among the robots is illustrated by gray lines in Fig. 14 and is fixed throughout the experiment. Nonzero eigenvalues of the computed gain matrix $A \in {\mathbb{R}}^{12 \times 12}$ range from $- 1.52$ to $- 0.22$. Collision avoidance strategy in Algorithm 2 is used with the activation threshold $d_{c} = 400$ mm and $r = 100$ mm. The speed of each robot is bounded to $1/3$ of its upper limit, which gives the maximum speed of around $200$ mm/s.

<!-- chunk {"id": "body-0111", "role": "body", "section": "IX-B Triangle Formation", "weight": 1.0} -->

The trajectory of robots under the single-integrator control strategy is shown in Fig. 14(a). These trajectories are reconstructed from the images provided by the first webcam. The sensing topology among robots is illustrated by gray lines in the figure. At their initial position, the robots roughly form a line. Starting from this initial position, they achieve the desired formation as can be further seen from the snapshots of experiment video at different instances of time in Fig. 17.

<!-- chunk {"id": "body-0112", "role": "body", "section": "IX-B Triangle Formation", "weight": 1.0} -->

In a similar experiment with robots starting roughly from the same initial positions, the unicycle control strategy is used to achieve the desired formation. Estimated trajectory of robots under this control strategy is shown in Fig. 14(b). As the robots get closer to the desired formation, the magnitude of their control vectors become smaller. Once the desired speed is small enough, the floor friction prevents the robots from moving further. This can cause an small steady state error, which can be observed in Fig. 14. Note that no collisions occur as the robots converge to the desired formation.

<!-- chunk {"id": "body-0113", "role": "body", "section": "IX-C Hexagon Formation", "weight": 1.0} -->

Using the same experimental setup for the triangle formation, we repeat a new set of experiments with the desired formation defined as a hexagon. The inter-agent sensing topology is chosen as a cyclic graph, as illustrated by gray lines in Fig. 15, and is fixed throughout the experiment. The nonzero eigenvalues of matrix $A$ for this desired formation range from $- 2$ to $- 1$. The reconstructed trajectories from webcam images are shown in Fig. 15(a) for the single-integrator control, and in Fig. 15(b) for the unicycle control. Snapshots of the experiment video corresponding to the single-integrator controller are shown in Fig. 18. As can be seen from the figures, starting from the initial positions, agents converge to the desired formation.

<!-- chunk {"id": "body-0114", "role": "body", "section": "IX-D Square-Grid Formation", "weight": 1.0} -->

In our last set of experiments we consider a square-grid desired formation of 9 robots with the sensing topology chosen as a complete graph and fixed throughout the experiment. Here, 3 computers are used to control the robots, where the first computer controls robots numbered 1 to 3, the second computer controls robots 4 to 6, and the third computer controls the remaining robots. The parameters used for collision avoidance strategy and the maximum allowed speed of the robots remain the same as previous experiments.

<!-- chunk {"id": "body-0115", "role": "body", "section": "IX-D Square-Grid Formation", "weight": 1.0} -->

The trajectory of robots reconstructed from the images of the first webcam is shown in Fig. 16(a) for the single-integrator control strategy, and snapshots of experiment video is shown in Fig. 19. If the distance between two robots is less than the collision avoidance threshold $d_{c}$, the collision avoidance strategy rotates the control direction outside of the collision cones. However, if the required rotation is more than $\pm 90^{\circ}$ of the original control direction, the control is set to zero and the robot stops until a feasible direction becomes available. The effect of collision avoidance strategy is most notable for robot 2, which is initially surrounded by robots 1, 3, and 4. Consequently, due to the lack of a feasible direction robot 2 remains stationary initially until the surrounding robots move further and a feasible direction becomes available. Similar experiments are performed by using the unicycle control strategy, where the reconstructed trajectory of robots are shown in Fig. 16(b). Due to using different PID gains for the low-level controllers implemented on robots 4 to 9, their trajectories are more distinguished than their corresponding trajectories in Fig. 16(a).

<!-- chunk {"id": "body-0116", "role": "body", "section": "Concluding Remarks and Future Work", "weight": 1.0} -->

We presented a distributed formation control strategy for a team of agents with a variety of dynamics to autonomously achieve a desired planar formation. Under the assumption that the sensing graph is undirected and universally rigid, we showed that formation control gains can be designed by solving a SDP problem. This design enjoys several robustness properties, such as robustness to positive scaling and rotation (up to $\pm 90^{\circ}$) of the control vector, saturations in the input, and switches in the sensing topology. The control was extended to agents with higher-order linear (or linearizable) holonomic dynamics, such as quadrotors, followed by further extension to agents with nonholonomic unicycle and car dynamics. An important outcome of this work was to show that under the proposed control the convergence and robustness guarantees hold for agents with more complex dynamics. Further, a fully distributed collision avoidance algorithm emerged naturally from the robustness properties. To typify the control, simulations for vehicles with different dynamics were presented, and experiments on a distributed robotic platform where performed.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Concluding Remarks and Future Work", "weight": 1.0} -->

Future work includes investigating additional requirements, such as inter-agent communication, to guarantee that the collision avoidance algorithm can overcome gridlock scenarios. Moreover, inter-agent communication can be exploited in a distributed optimization scheme to solve the SDP problem in a decentralized way. Other possible research avenues include formation control of heterogeneous vehicles and time-varying formations.
