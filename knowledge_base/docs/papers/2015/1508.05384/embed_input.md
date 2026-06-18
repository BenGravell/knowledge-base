<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Control Principles of Complex Networks

Topics include Online algorithms, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A reflection of our ultimate understanding of a complex system is our ability to control its behavior. Typically, control has multiple prerequisites: It requires an accurate map of the network that governs the interactions between the system's components, a quantitative description of the dynamical laws that govern the temporal behavior of each component, and an ability to influence the state and temporal behavior of a selected subset of the components. With deep roots in nonlinear dynamics and control theory, notions of control and controllability have taken a new life recently in the study of complex networks, inspiring several fundamental questions: What are the control principles of complex systems? How do networks organize themselves to balance control with functionality? To address these here we review recent advances on the controllability and the control of complex networks, exploring the intricate interplay between a system's structure, captured by its network topology, and the dynamical laws that govern the interactions between the components. We match the pertinent mathematical results with empirical findings and applications. We show that uncovering the control principles of complex systems can help us explore and ultimately understand the fundamental laws that govern their behavior.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

To understand the mechanisms governing the behavior of a complex system, we must be able to measure its state variables and to mathematically model the dynamics of each of the system's components. Consequently, the traditional theory of complex systems has predominantly focused on the measurement and the modeling problem. Recently, however, questions pertaining to the control of complex networks became an important research topic in statistical physics. This interest is driven by the challenge to understand the fundamental control principles of an arbitrary self-organized system. Indeed, there is an increasing realization that the design principles of many complex systems are genuinely determined by the need to control their behavior. For example, we cannot divorce the understanding of subcellular networks from questions on how the activity or the concentrations of genes, proteins, and other biomolecules are controlled. Similarly, the structure and the daily activity of an organization is deeply determined by governance and leadership principles. Finally, to maintain the functionality of large technological systems, like the power grid or the Internet, and to adapt their functions to the shifting needs of the users, we must solve a host of control questions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

These and many similar applications have led to a burst of research activity, aiming to uncover to what degree the topology of a real network behind a complex system encodes our ability to control it.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The current advances in controlling complex systems were facilitated by progress in network science, offering a quantitative framework to understand the design principles of complex networks. On one end, these advances have shown that the topologies of most real systems share numerous universal characteristics. Equally important was the realization that these universal topological features are the result of the common dynamical principles that govern their emergence and growth. At the same time we learned that the topology fundamentally affects the dynamical processes taking place on these networks, from epidemic spreading to synchronization. Hence, it is fair to expect that the network topology of a system also affects our ability to control it.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While the term "control" is frequently used in numerous disciplines with rather diverse meanings, here we employ it in the strict mathematical sense of control theory, a highly developed interdisciplinary branch of engineering and mathematics. Control theory asks how to influence the behavior of a dynamical system with appropriately chosen inputs so that the system's output follows a desired trajectory or final state. A key notion in control theory is the *feedback* process: The difference between the actual and desired output is applied as feedback to the system's input, forcing the system's output to converge to the desired output. Feedback control has deep roots in physics and engineering. For example, the centrifugal governor, one of the first practical control devices, has been used to regulate the pressure and distance between millstones in windmills since the 17th century and was used by James Watt to to maintain the steady velocity of a steam engine. The feedback mechanism relies on a system of balls rotating around an axis, with a velocity proportional to the engine velocity. When the rotational velocity increases, the centrifugal force pushes the balls farther from the axis, opening valves to let the vapor escape. This lowers the pressure inside the boiler, slowing the engine (Fig. 1).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The first definitive mathematical description of the centrifugal governor used in Watt's steam engine was provided by James Maxwell in 1868, proposing some of the best known feedback control mechanisms in use today (Maxwell, 1868).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The subsequent need to design well controlled engineered systems has resulted in a mathematically sophisticated array of control theoretical tools, which are today widely applied in the design of electric circuits, manufacturing processes, communication systems, airplanes, spacecrafts and robots. Furthermore, since issues of regulation and control are central to the study of biological and biochemical systems, the concepts and tools developed in control theory have proven useful in the study of biological mechanisms and disease treatment. For example, feedback control by transcranial electrical stimulation has been used to restore the aberrant brain activity during epileptic seizures.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modern control theory heavily relies on the state space representation (also known as the "time-domain approach"), where a control system is described by a set of inputs, outputs and state variables connected by a set of differential (or difference) equations. The concept of *state*, introduced into control theory by Rudolf Kalman in 1960s, is a mathematical entity that mediates between the inputs and the outputs of a dynamical system, while emphasizing the notions of causality and internal structure. Any state of a dynamical system can then be represented as a vector in the state space whose axes are the state variables. The concept of the state space was inspired by the *phase space* concept used in physics, developed in the late 19th century by Ludwig Boltzmann, Henri Poincaré, and Willard Gibbs.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

For a nonlinear dynamical system, we can write the state space model as

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

where the state vector ${\mathbf{x}{(t)}} \in {\mathbb{R}}^{N}$ represents the internal state of the system at time $t$, the input vector ${\mathbf{u}{(t)}} \in {\mathbb{R}}^{M}$ captures the known input signals, and the output vector ${\mathbf{y}{(t)}} \in {\mathbb{R}}^{R}$ captures the set of experimentally measured variables. The functions $\mathbf{f}{( \cdot )}$ and $\mathbf{h}{( \cdot )}$ are generally nonlinear, and $\Theta$ collects the system's parameters. Equations (1a) and (1b) are called the state and output equations, respectively, and describe the dynamics of a wide range of complex systems.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

For example, in metabolic networks the state vector $\mathbf{x}{(t)}$ represents the concentrations of all metabolites in a cell, the inputs $\mathbf{u}{(t)}$ represent regulatory signals modulated through enzyme abundance, and the outputs $\mathbf{y}{(t)}$ are experimental assays capturing the concentrations of a particular set of secreted species or the fluxes of a group of reactions of interest. In communication systems $\mathbf{x}{(t)}$ is the amount of information processed by a node and $\mathbf{y}{(t)}$ is the measurable traffic on selected links or nodes.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

A significant body of work in control theory focuses on linear systems, described by

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

where (2a) and (2b) represent so-called linear time-varying (LTV) systems. Here, ${\mathbf{A}{(t)}} \in {\mathbb{R}}^{N \times N}$ is the state or system matrix, telling us which components interact with each other and the strength or the nature of those interactions; ${\mathbf{B}{(t)}} \in {\mathbb{R}}^{N \times M}$ is the input matrix; ${\mathbf{C}{(t)}} \in {\mathbb{R}}^{R \times N}$ is the output matrix; ${\mathbf{D}{(t)}} \in {\mathbb{R}}^{R \times M}$ is the feedthrough or feedforward matrix.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

In case $\mathbf{A}{(t)}$, $\mathbf{B}{(t)}$, $\mathbf{C}{(t)}$ and $\mathbf{D}{(t)}$ are constant matrices, (2a) and (2b) represent a linear time-invariant (LTI) system, which is the starting point of most control theoretical approaches.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many nonlinear systems like (1a, 1b) can be linearized around their equilibrium points, resulting in an LTI system. For example, in stick balancing, a prototypical control problem, our goal is to balance (or control) the stick in the upright position using the horizontal position of the hand as the control input $u{(t)}$. This mechanical system has a natural state space representation derived from Newton's second law of motion. Consider a stick of length $L$ whose mass $M$ is concentrated at the top. ^11^1 For a more realistic case, treating the stick as a rigid body of uniform desnity, see. Denote the angle between the stick and the vertical direction with $\theta{(t)}$. The hand and the top of the stick have horizontal displacement $u{(t)}$ and $x{(t)}$, respectively (Fig. 2). The nonlinear equation of motion for this system is

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $g$ is the gravitational constant and

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

When the stick is nearly at rest in the upright vertical position ($\theta = 0$, which is an equilibrium point), $\theta$ is small, hence we can linearize Eqs. and, obtaining

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

This form allows us to perform linear controllability analysis. Indeed, as we show in Sec.II.2, the linearized system (6a) is controllable, in line with our experience that we can balance a stick on our palm.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

Linearization of a nonlinear system around its norminal trajectory $\{{\mathbf{x}^{\ast}{(t)}},{\mathbf{u}^{\ast}{(t)}}\}$ generally leads to an LTV system. Consider the motion of a rocket thrust upward, following

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $m{(t)}$ is the mass of the rocket at time $t$ and $h{(t)}$ is its altitute. The thrust force $\overset{˙}{m}{(t)}v_{e}$ follows Newton's third law of motion, where $\overset{˙}{m}{(t)}$ denotes the mass flow rate and $v_{e}$ is the assumed-constant exit velocity of the exhaust (Fig. 2b).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notwithstanding our ability to design such well-controlled systems as a car or an airplane, we continue to lack an understanding of the control principles that govern self-organized complex networked systems. Indeed, if given the wiring diagram of a cell, we do not understand the fundamental principles that govern its control, nor do we have tools to extract them. Until recently the degree of penetration of control theoretical tools in the study of complex systems was limited. The reason is that to extract the predictive power of (1a) and (1b), we need (i) the accurate wiring diagram of the system; (ii) a description of the nonlinear dynamics that governs the interactions between the components; and (iii) a precise knowledge of the system parameters. For most complex systems we lack some of these prerequisites.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Introduction", "weight": 1.5} -->

For example, current estimates indicate that in human cells the available protein-protein interaction maps cover less than 20% of all potential protein-protein interactions; in communication systems we may be able to build an accurate wiring diagram, but we often lack the analytical form of the system dynamics $\mathbf{f}{({\mathbf{x}{(t)}},{\mathbf{u}{(t)}};\Theta)}$; in biochemical reaction systems we have a good understanding of the underlying network and dynamics, but we lack the precise values of the system parameters, like the reaction rate constants. Though progress is made on all three fronts, offering increasingly accurate data on the network structure, dynamics, and the system parameters, accessing them all at once is still infeasible for most complex systems. Despite these difficulties, in the past decade we have seen significant advances pertaining to the control of complex systems. These advances indicate that many fundamental control problems can be addressed without knowing all the details of equations (1a) and (1b). Hence, we do not have to wait for the description of complex systems to be complete and accurate to address and understand the control principles governing their behavior.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Introduction", "weight": 1.5} -->

Graph theoretical methods have been successfully applied to investigate the structural and the qualitative properties of dynamical systems since 1960's. This raises a question: Can the recent renaissance of interest in controlling networked systems offer a better understanding of control principles than previous graph theoretical methods? To answer this we must realize that the current interest in control in the area of complex systems is driven by the need to understand such large-scale complex networks as the Internet, the WWW, wireless communication networks, power grids, global transportation systems, genome-scale metabolic networks, protein interaction networks and gene regulatory networks, to name only a few. Until the emergence of network science in the 21th century we lacked the mathematical tools to characterize the structure of these systems, not even mentioning their control principles. The non-trivial topology of real-world networks, uncovered and characterized in the past two decades, brings an intrinsic layer of complexity to most control problems, requiring us to rely on tools borrowed from many disciplines to address them. A typical example is the structural controllability problem of complex networks. Structural control theory developed in 1970's offered sufficient and necessary conditions to check if any network with LTI dynamics is structurally controllable.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Introduction", "weight": 1.5} -->

Yet, it failed to offer an efficient algorithm to find the minimum set of driver nodes required to control the network, nor an analytical framework to estimate the fraction of driver nodes. Advances on this front became possible by mapping the control problem into well-studied network problems, like matching, and utilizing the notion of thermodynamic limit in statistical physics and the cavity method developed in spin glass theory, tools that were traditionally beyond the scope of control theory.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Introduction", "weight": 1.5} -->

The goal of this article is to review the current advances in controlling complex systems, be they of biological, social, or technological in nature. To achieve this we discuss a series of topics that are essential to understand the control principles of networks, with emphasis on the impact of the network structure on control.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Introduction", "weight": 1.5} -->

\(i\) *Controllability*. Before deciding how to control a system, we must make sure that it is possible to control it. Controllability, a key notion in modern control theory quantifies our ability to steer a dynamical system to a desired final state in finite time. We will discuss the impact of network topology on our ability to control complex networks, and address some practical issues, like the energy or effort required for control.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Introduction", "weight": 1.5} -->

\(ii\) *Observability*. As a dual concept of controllability, observability describes the possibility of inferring the initial state of a dynamical system by monitoring its time-dependent outputs. We will discuss different methods to identify the sensor nodes, whose measurements over time enable us to infer the initial state of the whole system. We also explore a closely related concept --- *identifiability*, representing our ability to determine the system's parameters through appropriate input/output measurements.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Introduction", "weight": 1.5} -->

\(iii\) *Steering complex systems to desired states or trajectories.* The ultimate goal of control is to drive a complex system from its current state/trajectory to some desired final state/trajectory. This problem has applications from ecosystem management, to cell reprogramming. For example, we would like to design interventions that can move a cell from a disease (undesired) to a healthy (desired) state. We discuss different ways of achieving such control: (a) By applying small perturbations to a set of physically or experimentally feasible parameters; (b) Via compensatory perturbations of state variables that exploit the basin of attraction of the desired final state; (c) By mapping the control problem into a combinatorial optimization problem on the underlying network.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Introduction", "weight": 1.5} -->

\(iv\) *Controlling collective behavior.* Collective behavior, a much-studied topic in modern statistical physics, can result from the coordinated local activity of many interdependent components. Examples include the emergence of flocking in mobile agents or synchronization in coupled oscillators. Controlling such processes has numerous potential applications, from the design of flocking robots, to the treatment of Parkinson's disease. We review a broad spectrum of methods to determine the conditions for the emergence of collective behavior and discuss pinning control as an effective control strategy.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Introduction", "weight": 1.5} -->

Control problems are ubiquitous, with direct relevance to many natural, social and technological phenomena. Hence the advances reviewed here truly probe our fundamental understanding of the complexity of the world surrounding us, potentially inspiring advances in numerous disciplines. Consequently, our focus here is on conceptual advances and tools pertaining to control, that apply to a wide range of problems emerging in physical, technological, biological and social systems. It is this diversity of applications that makes control increasingly unavoidable in most disciplines.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Controllability of Linear Systems", "weight": 1.0} -->

A system is *controllable* if we can drive it from any initial state to any desired final state in finite time. Many mechanical problems can be formalized as controllability problems (Fig. 2). Consider, for example, the control of a rocket thrust upward. The rocket is controllable if we can find a continuous control input (thrust force) that can move the rocket from a given initial state (altitute and velocity) to a desired final state. Another example is the balancing of a stick on our hand. We know from our experience that this is possible, suggesting that the system must be controllable. The scientific challenge is to decide for an arbitrary dynamical system if it is controllable or not, given a set of inputs.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Controllability of Linear Systems", "weight": 1.0} -->

The current interest in the control of complex networked systems was induced by recent advances in the controllability of complex networks, offering mathematical tools to identify the driver nodes, a subset of nodes whose direct control with appropriate signals can control the state of the full system. In general controllability is a prerequiste of control, hence understanding the topological factors of the underlying network that determine a system's controllability offers numerous insights into the control principles of complex networked systems. As we discuss below, thanks to a convergence of tools from control theory, network science and statistical physics, our understanding of network controllability has advanced considerably recently.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II.1 Linear Time-Invariant Systems", "weight": 1.0} -->

The starting point of most control theoretical approaches is the linear time-invariant (LTI) control system $(\mathbf{A},\mathbf{B})$

<!-- chunk {"id": "body-0035", "role": "body", "section": "II.1 Linear Time-Invariant Systems", "weight": 1.0} -->

Many mechanical systems can be naturally described by LTI dynamics, where the state vector captures the position and velocity of objects and the LTI dynamics is either directly derived from Newton's Second Law or represents some reasonable linearization of the underlying nonlinear problem, as illustrated by the stick balancing problem.

<!-- chunk {"id": "body-0036", "role": "body", "section": "II.1 Linear Time-Invariant Systems", "weight": 1.0} -->

A significant fraction of the control theory literature deals exclusively with linear systems. There are multiple reasons for this. First, linear systems offer an accurate model for some real problems, like consensus or agreement formation in multi-agent networks, where the state of each agent captures its opinion. Second, while many complex systems are characterized by nonlinear interactions between the components, the first step in any control challenge is to establish the controllability of the locally linearized system. Furthermore, as we show below, for systems near their equilibrium points the linearized dynamics can actually characterize the underlying nonlinear controllability problem. Third, the non-trivial network topology of real-world complex systems brings a new layer of complexity to controllability. Before we can explore the fully nonlinear dynamical setting, which is mathematically much harder, we must understand the impact of the topological characteristics on linear controllability, serving as a prerequisite of nonlinear controllability.

<!-- chunk {"id": "body-0037", "role": "body", "section": "II.1 Linear Time-Invariant Systems", "weight": 1.0} -->

Consider the LTI dynamics on a directed weighted network $G{(\mathbf{A})}$ of $N$ nodes (Fig. 3). The state variable $x_{i}{(t)}$ can denote the amount of traffic that passes through a node $i$ on a communication network, or transcription factor concentration in a gene regulatory network. The state matrix $\mathbf{A}:={(a_{ij})}_{N \times N}$ represents the weighted wiring diagram of the underlying network, where $a_{ij}$ is the strength or weight with which node $j$ affects/influences node $i$: a positive (or negative) $a_{ij}$ means the link ($j\rightarrow i$) is excitatory (or inhibitory), and $a_{ij} = 0$ if node $j$ has no direct influence on node $i$. Consider $M$ independent control signals $\{ u_{1},\cdots,u_{M}\}$ applied to the network.

<!-- chunk {"id": "body-0038", "role": "body", "section": "II.1 Linear Time-Invariant Systems", "weight": 1.0} -->

The input matrix $\mathbf{B}:={(b_{im})}_{N \times M}$ identifies the nodes that are directly controlled, where $b_{im}$ represents the strength of an external control signal $u_{m}{(t)}$ injected into node $i$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "II.1 Linear Time-Invariant Systems", "weight": 1.0} -->

The input signal ${\mathbf{u}{(t)}} = {({u_{1}{(t)}},\cdots,{u_{M}{(t)}})}^{T} \in {\mathbb{R}}^{M}$ can be imposed on all nodes or only a preselected subset of the nodes. In general the same signal $u_{m}{(t)}$ can drive multiple nodes. The nodes directly controlled by $\mathbf{u}{(t)}$ are called *actuator nodes* or simply *actuators*, like nodes $x_{1},x_{2}$ and $x_{5}$ in Fig. 3. The number of actuators is given by the number of non-zero elements in $\mathbf{B}$. The actuators that do not share input signals, e.g. nodes $x_{1}$ and $x_{2}$ in Fig. 3, are called *driver nodes* or simply *drivers*.

<!-- chunk {"id": "body-0040", "role": "body", "section": "II.1 Linear Time-Invariant Systems", "weight": 1.0} -->

The number of driver nodes equals the number of columns in $\mathbf{B}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "II.1 Linear Time-Invariant Systems", "weight": 1.0} -->

Controllability, the ability to steer a system into an arbitrary final state in a finite time, implies that we can move the state variable of each node of a network to a predefined value, corresponding to the system's desired position in the state space. Our ability to do so is greatly determined by the network topology. For example, if the network structure is such that a signal cannot get from our driver nodes to a particular node, that node, and hence the system as a whole, is uncontrollable. Our challenge is to decide when control is possible and when is not. The answer is given by controllability tests described next.

<!-- chunk {"id": "body-0042", "role": "body", "section": "II.2 Kalman's Criterion of Controllability", "weight": 1.0} -->

Controllability tests allow us to check if an LTI system is controllable from a given set of inputs. The best known is Kalman's rank condition, stating that the LTI system $(\mathbf{A},\mathbf{B})$ is controllable if and only if the ${N \times N}M$ controllability matrix

<!-- chunk {"id": "body-0043", "role": "body", "section": "II.2 Kalman's Criterion of Controllability", "weight": 1.0} -->

To understand the origin of, we consider the formal solution of with ${\mathbf{x}{}} = \mathbf{0}$, i.e.

<!-- chunk {"id": "body-0044", "role": "body", "section": "II.2 Kalman's Criterion of Controllability", "weight": 1.0} -->

So if ${{rank}\mathcal{C}} < N$, then even the infinite series of $\{\mathbf{B},{\mathbf{A}\mathbf{B}},{\mathbf{A}^{2}\mathbf{B}},\cdots\}$ will not contain a full basis to span the entire $N$-dimensional state space. In other words, we cannot fully explore the state space, regardless of $\mathbf{u}{(t)}$, indicating that given our inputs the system is stuck in a particular subspace, unable to reach an arbitrary point in the state space (Fig. 4). If, however, ${{rank}\mathcal{C}} = N$, then we can find an appropriate input vector $\mathbf{u}{(t)}$ to steer the system from $\mathbf{x}{}$ to an arbitrary $\mathbf{x}{(t)}$. Hence, the system is controllable.

<!-- chunk {"id": "body-0045", "role": "body", "section": "II.2 Kalman's Criterion of Controllability", "weight": 1.0} -->

One can check that in the stick balancing problem (6a), the controllability matrix has full rank (${{rank}\mathcal{C}} = N = 2$), indicating that both systems are controllable. In the network control problem of Fig. 4a the controllability matrix

<!-- chunk {"id": "body-0046", "role": "body", "section": "II.2 Kalman's Criterion of Controllability", "weight": 1.0} -->

is always rank deficient, as long as the parameters $b_{1}$, $a_{21}$ and $a_{31}$ are non-zero. Hence, the system is uncontrollable. In contrast, for Fig. 4c we have

<!-- chunk {"id": "body-0047", "role": "body", "section": "II.2 Kalman's Criterion of Controllability", "weight": 1.0} -->

which has full rank, as long as the parameters $b_{1}$, $b_{2}$, $a_{21}$ and $a_{31}$ are non-zero. Hence the system is controllable.

<!-- chunk {"id": "body-0048", "role": "body", "section": "II.2 Kalman's Criterion of Controllability", "weight": 1.0} -->

The example of Fig. 4 implies that the topology of the *controlled network*, which consists of both the network itself and the control signals applied to some nodes, imposes some inherent limits on the controllability matrix: some configurations are controllable (Fig. 4c), while others are not (Fig. 4a). Thanks to the Kalman criterion, controllability can be easily tested when the dimension of the controllability matrix is small and its rank test can be done even without knowing the detailed values of its non-zero matrix elements. For large real networks the controllability test is difficult to perform, however. Indeed, there is no scalable algorithm to numerically determine the rank of the controllability matrix $\mathcal{C}$, which has dimension ${N \times N}M$. Equally important, executing an accurate rank test is ill-conditioned and is very sensitive to roundoff errors and uncertainties in the matrix elements.

<!-- chunk {"id": "body-0049", "role": "body", "section": "II.2 Kalman's Criterion of Controllability", "weight": 1.0} -->

Indeed, if we plug the numerical values of $b_{i}$ and $a_{ij}$ into, we may obtain extremely large or small matrix elements, such as $a_{ij}^{N - 1}$, which for large $N$ are rather sensitive to numeric precision. Hence, for large complex systems we need to determine the system's controllability without numerically calculating the rank of the controllability matrix. As we discuss in the next section, this can be achieved in the context of structural control theory.

<!-- chunk {"id": "body-0050", "role": "body", "section": "II.3 Structural Controllability", "weight": 1.0} -->

For many complex networks the system parameters (e.g. the elements in $\mathbf{A}$) are not precisely known. Indeed, we are often unable to measure the weights of the links, knowing only whether there is a link or not. In other cases the links are time dependent, like the traffic on an internet cable or the flux of a chemical reaction. Hence, it is hard, if not conceptually impossible, to numerically verify Kalman's rank condition using fixed weights. Structural control, introduced by C.-T. Lin in 1970s, offers a framework to systematically avoid this limitation.

<!-- chunk {"id": "body-0051", "role": "body", "section": "II.3.1 The power of structural controllability", "weight": 1.0} -->

An LTI system $(\mathbf{A},\mathbf{B})$ is a *structured system* if the elements in $\mathbf{A}$ and $\mathbf{B}$ are either fixed zeros or independent free parameters. The corresponding matrices $\mathbf{A}$ and $\mathbf{B}$ are called *structured matrices*. The system $(\mathbf{A},\mathbf{B})$ is *structurally controllable* if we can set the nonzero elements in $\mathbf{A}$ and $\mathbf{B}$ such that the resulting system is controllable in the usual sense (i.e., ${{rank}\mathcal{C}} = N$).

<!-- chunk {"id": "body-0052", "role": "body", "section": "II.3.1 The power of structural controllability", "weight": 1.0} -->

The power of structural controllability comes from the fact that if a system is structurally controllable then it is controllable for almost all possible parameter realizations. To see this, denote with $\mathcal{S}$ the set of all possible LTI systems that share the same zero-nonzero connectivity pattern as a structurally controllable system $(\mathbf{A},\mathbf{B})$. It has been shown that *almost* all systems that belong to the set $\mathcal{S}$ are controllable except for some pathological cases with Lebesgue measure zero.

<!-- chunk {"id": "body-0053", "role": "body", "section": "II.3.1 The power of structural controllability", "weight": 1.0} -->

This is rooted in the fact that if a system ${(\mathbf{A}_{0},\mathbf{B}_{0})} \in \mathcal{S}$ is uncontrollable, then for every $\epsilon > 0$ there exists a controllable system $(\mathbf{A},\mathbf{B})$ with ${\|{\mathbf{A} - \mathbf{A}_{0}}\|} < \epsilon$ and ${\|{\mathbf{B} - \mathbf{B}_{0}}\|} < \epsilon$ where $|| \cdot ||$ denotes matrix norm. In other words, an uncontrollable system in $\mathcal{S}$ becomes controllable if we slightly alter some of the link weights.

<!-- chunk {"id": "body-0054", "role": "body", "section": "II.3.1 The power of structural controllability", "weight": 1.0} -->

For example, the system shown in Fig. 5d is controllable for almost all parameter realizations, except when the edge weights satisfy the constraint ${a_{32}a_{21}^{2}} = {a_{23}a_{23}^{2}}$. But these pathological cases can be easily avoided by slightly changing one of the edge weights, hence this system is structurally controllable.

<!-- chunk {"id": "body-0055", "role": "body", "section": "II.3.1 The power of structural controllability", "weight": 1.0} -->

Taken together, structural control tells us that we can decide a network's controllability even if we do not know the precise weight of each edge. All we have to make sure is that we have an accurate map of the system's wiring diagram, i.e., know which components are linked and which are not. As we demonstrate in the coming section, this framework considerably expands the practical applicability of control tools to real systems.

<!-- chunk {"id": "body-0056", "role": "body", "section": "II.3.2 Graphical interpretation", "weight": 1.0} -->

Structural control theory allows us to check if a controlled network is structurally controllable by simply inspecting its topology, avoiding expensive matrix operations. This is possible thanks to the graphical interpretation ^22^2The structural controllability theorem also has a pure algebraic meaning, which plays an important role in the characterization of strong structural controllability. of Lin's Structural Controllability Theorem, discussed next.

<!-- chunk {"id": "body-0057", "role": "body", "section": "II.3.2 Graphical interpretation", "weight": 1.0} -->

Consider an LTI system $(\mathbf{A},\mathbf{B})$ represented by a digraph ${G{(\mathbf{A},\mathbf{B})}} = {(V,E)}$ (Fig. 3).

<!-- chunk {"id": "body-0058", "role": "body", "section": "II.3.2 Graphical interpretation", "weight": 1.0} -->

\{{(x_{j},x_{i})} \middle| {a_{ij} \neq 0}\} \right.$, corresponding to the links of network $\mathbf{A}$, and the edges connecting input vertices to state vertices $E_{B} = \left. \{{(u_{m},x_{i})} \middle| {b_{im} \neq 0}\} \right.$. These definitions allow us to formulate a useful statement: The system $(\mathbf{A},\mathbf{B})$ is not structurally controllable if and only if it has *inaccessible nodes* or *dilations*.

<!-- chunk {"id": "body-0059", "role": "body", "section": "II.3.2 Graphical interpretation", "weight": 1.0} -->

Let us consider these two cases separately. A state vertex $x_{i}$ is *inaccessible* if there are no directed paths reaching $x_{i}$ from the input vertices (Fig. 6a). Consequently, an inaccessible node can not be influenced by input signals applied to the driver nodes, making the whole network uncontrollable.

<!-- chunk {"id": "body-0060", "role": "body", "section": "II.3.2 Graphical interpretation", "weight": 1.0} -->

The digraph $G{(\mathbf{A},\mathbf{B})}$ contains a *dilation* if there is a subset of nodes $S \subset V_{A}$ such that the *neighborhood set* of $S$, denoted as $T{(S)}$, has fewer nodes than $S$ itself (see Fig. 6b). Here, $T{(S)}$ is the set of vertices $v_{j}$ for which there is a directed edge from $v_{j}$ to some other vertex in $S$. Note that the input vertices are not allowed to belong to $S$ but may belong to $T{(S)}$. Roughly speaking, dilations are subgraphs in which a small subset of nodes attempts to rule a larger subset of nodes. In other words, there are more "subordinates" than "superiors". A controlled network containing dilations is uncontrollable. For example, in a directed star configuration, where we wish to control via a central node all the leaves, any two leaf-nodes form a dilation with the central hub.

<!-- chunk {"id": "body-0061", "role": "body", "section": "II.3.2 Graphical interpretation", "weight": 1.0} -->

If we control the central hub only, the system remains uncontrollable because we cannot independently control the difference between the two leaf nodes' states (Fig. 4). In other words, we cannot independently control two subordinates if they share the same superior.

<!-- chunk {"id": "body-0062", "role": "body", "section": "II.3.2 Graphical interpretation", "weight": 1.0} -->

Taken together, Lin's structural controllability theorem states that an LTI system $(\mathbf{A},\mathbf{B})$ is structurally controllable if and only if the digraph $G{(\mathbf{A},\mathbf{B})}$ does not contain inaccessible nodes or dilations. These two conditions can be accurately checked by inspecting the topology of the digraph $G{(\mathbf{A},\mathbf{B})}$ without dealing with floating-point operations. Hence, this bypasses the numerical issues involved in evaluating Kalman's controllability rank test, and also our lack of detailed knowledge on the edge weights in $G{(\mathbf{A},\mathbf{B})}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "II.3.2 Graphical interpretation", "weight": 1.0} -->

An alternative graph theoretical formulation of Lin's structural controllability theorem is often useful in practice. A general graph is *covered* or *spanned* by a subgraph if the subgraph and the graph have the same vertex set. Typically the spanning subgraph has only a subset of links of the original graph. For a digraph, a sequence of oriented edges $\{{({v_{1}\rightarrow v_{2}})},\cdots,{({v_{k - 1}\rightarrow v_{k}})}\}$, where the vertices $\{ v_{1},v_{2},\cdots,v_{k}\}$ are distinct, is called an *elementary path*. When $v_{k}$ coincides with $v_{1}$, the sequence of edges is called an *elementary cycle*.

<!-- chunk {"id": "body-0064", "role": "body", "section": "II.3.2 Graphical interpretation", "weight": 1.0} -->

For the digraph $G{(\mathbf{A},\mathbf{B})}$, we define the following subgraphs (Fig. 6c): (i) a *stem* is an elementary path originating from an input vertex; (ii) a *bud* is an elementary cycle $C$ with an additional edge $e$ that ends, but does not begin, in a vertex of the cycle; (iii) a *cactus* is defined recursively: A stem is a cactus. Let $C$, $O$, and $e$ be, respectively, a cactus, an elementary cycle that is disjoint with $C$, and an arc that connects $C$ to $O$ in $G{(\mathbf{A},\mathbf{B})}$. Then, $C \cup {\{ e\}} \cup O$ is also a cactus. $G{(\mathbf{A},\mathbf{B})}$ is spanned by cacti if there exists a set of disjoint cacti that cover all state vertices.

<!-- chunk {"id": "body-0065", "role": "body", "section": "II.3.2 Graphical interpretation", "weight": 1.0} -->

Note that a cactus is a *minimal* structure that contains neither inaccessible nodes nor dilations. That is, for a given cactus, the removal of any edge will result in either inaccessibility or dilation, hence the controllability of the cactus is lost (Fig. 6). We can now formulate Lin's *structural controllability theorem* as follows: An LTI system $(\mathbf{A},\mathbf{B})$ is structurally controllable if and only if $G{(\mathbf{A},\mathbf{B})}$ is spanned by cacti. Later we show that this formulation helps us design an efficient algorithm to identify a minimum set of inputs that guarantee structural controllability.

<!-- chunk {"id": "body-0066", "role": "body", "section": "II.3.3 Strong structural controllability", "weight": 1.0} -->

The fundamental assumption of structural control is that the entries of the matrices A and B are either zeros or independent free parameters. Therefore structural control does not require knowledge of the exact values of parameters, any by avoiding floating-point operations, it is not subject to numerical errors. However, some systems have interdependent parameters, making it uncontrollable despite the fact that it is structurally controllable. For example, Fig. 5d displays an LTI system that is structurally controllable, but becomes uncontrollable when the parameters satisfy the constraint ${a_{32}a_{21}^{2}} = {a_{23}a_{31}^{2}}$. This leads to the notion of *strong structural controllability* (SSC): A system is strongly structurally controllable if it remains controllable for any value (other than zero) of the indeterminate parameters. In other words, there is no combination of non-zero link weights that violates Kalman's criterion. For example, the LTI systems shown in Fig. 5a and c are strongly structurally controllable.

<!-- chunk {"id": "body-0067", "role": "body", "section": "II.3.3 Strong structural controllability", "weight": 1.0} -->

Both graph-theoretic and algebraic conditions for SSC have been studied. Unfortunately, those conditions do not lead to efficient algorithms. Recently, necessary and sufficient graph-theoretical conditions involving constrained matchings were derived. Denote a matching of size $t$ in the bipartite representation $H{(\mathbf{A})}$ of the digraph $G{(\mathbf{A})}$ as $t$-matching. A $t$-matching is *constrained* if it is the only $t$-matching in $H{(\mathbf{A})}$. A matching is called $V_{s}$-less if it contains no edges corresponding to self-loops. Let $\mathcal{S}$ be an input set with cardinality $M \leq N$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "II.3.3 Strong structural controllability", "weight": 1.0} -->

The corresponding structured pair $(\mathbf{A},\mathbf{B})$ is strongly structurally controllable if and only if $H{(\mathbf{A})}$ has a constrained $({N - M})$-matching with $\mathcal{S}$ unmatched and $H{(\mathbf{A}_{\times})}$ has a constrained $V_{s}$-less $({N - M})$-matching with $\mathcal{S}$ unmatched. Here $H{(\mathbf{A}_{\times})}$ is formed by adding self-loops to all nodes if they don't have one. The constrained matching conditions can be applied to check if an input set is strongly structural controllable in $\mathcal{O}{(N^{2})}$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "II.3.3 Strong structural controllability", "weight": 1.0} -->

Though finding a minimum cardinality input set is proven to be NP-complete, a greedy $\mathcal{O}{(N^{2})}$ algorithm has been developed to provide a strongly structural controllable input set, which is not-necessarily minimal.

<!-- chunk {"id": "body-0070", "role": "body", "section": "II.4 Minimum Input Problem", "weight": 1.0} -->

If we wish to control a networked system, we first need to identify the set of driver nodes that, if driven by different signals, can offer full control over the network. Any system is fully controllable if we control each node individually. Yet, such full control is costly and typically impractical. Hence, we are particularly interested in identifying a minimum driver node set (MDNS), whose control is sufficient to make the whole system controllable. In other words, we want to control a system with minimal inputs.

<!-- chunk {"id": "body-0071", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

Kalman's rank condition does not offer us the MDNS--- it only tells us if we can control a system through a given set of potential driver nodes that we must guess or select. Furthermore, to numerically check Kalman's rank condition, we have to know all the entries in $\mathbf{A}$ and $\mathbf{B}$, which are often unknown for complex networks. Even if we know all the weights (parameters) exactly, a brute-force search for the MDNS would require us to compute the rank of almost $2^{N}$ distinct controllability matrices, a combinatorially prohibitive task for any network of reasonable size. Yet, as we show next, we can identify the MDNS by mapping the control problem into a purely graph theoretical problem called maximum matching.

<!-- chunk {"id": "body-0072", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

Matching is a widely studied problem in graph theory, with many practical applications. On undirected graphs, where it was originally defined, a matching represents a set of edges without common vertices (red edges in Fig. 7g). Maximum matching is a matching of the largest size. For most graphs we can find multiple maximum matchings (Fig. 7h1-h3). The end vertices of a matching edge are called *matched*, the remaining vertices are *unmatched*. If all vertices are matched, then the matching is *perfect* (Fig. 7g).

<!-- chunk {"id": "body-0073", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

Many real world problems can be formalized as a maximum matching problem on bipartite graphs (Fig. 7c). Consider, for example, $M$ job applicants applying for $N$ openings. Each applicant is interested in a subset of the openings. Each opening can only accept one applicant and an applicant can only accept one job offer. Finding an assignment of openings to applicants such that as many applicants as possible get a job is a classical maximum matching problem.

<!-- chunk {"id": "body-0074", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

In structural control theory, the role of matching is well studied and matching was originally defined in the bipartite representation of a digraph. The extended definition of matching on a digraph connects more naturally to the cactus structure (Fig. 8), which is a fundamental notion in structural control theory. In a directed graph (digraph), a matching is defined to be a set of directed edges that do not share common start or end vertices. Hence, a vertex can be the starting or the end point of a red link, but we cannot have two red links pointing to the same vertex. A vertex is *matched* if it is the end vertex of a matching edge. Otherwise, it is *unmatched*. For example, in a directed path, all but the starting vertex are matched (Fig. 7d,j). A matching of maximum size is called a *maximum matching*. A maximum matching is called *perfect* if all vertices are matched, like in a directed elementary cycle (Fig. 7f,l). We can prove that a matching of a digraph can be decomposed into a set of directed paths and/or directed cycles (Fig. 8b).

<!-- chunk {"id": "body-0075", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

Note that directed paths and cycles are also the basic elements of the cactus structure (Fig. 8d). Hence, matching in digraphs connects naturally to the cactus structure.

<!-- chunk {"id": "body-0076", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

The usefulness of matching in network control comes from a theorem that provides the minimum number of driver nodes in a network.

<!-- chunk {"id": "body-0077", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

*Minimum input theorem*: To fully control a directed network $G{(\mathbf{A})}$, the minimum number of inputs, or equivalently the minimum number of driver nodes, is

<!-- chunk {"id": "body-0078", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

where $|M^{\ast}|$ is the size of the maximum matching in $G{(\mathbf{A})}$. In other words, the driver nodes correspond to the unmatched nodes. If all nodes are matched (${|M^{\ast}|} = N$), we need at least one input to control the network, hence $N_{D} = 1$. We can choose any node as our driver node in this case.

<!-- chunk {"id": "body-0079", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

The minimum input theorem maps an inherently dynamical problem, i.e. our ability to control a network from a given subset of nodes, into a purely graph theoretical problem of finding the maximum matching of a directed network. Most important, it bypasses the need to search all node combinations for a minimum driver node set, as the driver nodes are provided by the solution of the underlying matching problem.

<!-- chunk {"id": "body-0080", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

*Maximum matching: algorithmic solution*. The mapping of the MDNS problem to a matching problem via seems to map a problem of high computational complexity --- an exhaustive search for the MDNS --- into another just as complicated problem, that of finding the maximum matching for a digraph. The real value of this mapping, however, comes from the fact that the maximum matching problem in a digraph in not NP-hard, but can be solved in polynomial time. Indeed, the maximum matching for a digraph can be identified by mapping the digraph to its bipartite representation, as illustrated in Fig. 9. Consider a digraph $G{(\mathbf{A})}$, whose bipartite representation is ${H{(\mathbf{A})}} \equiv {({V_{A}^{+} \cup V_{A}^{-}},\Gamma)}$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

We then place an edge $(x_{j}^{+},x_{i}^{-})$ in the bipartite graph if there is a directed edge $({x_{j}\rightarrow x_{i}})$ in the original digraph. Note that since we allow self-loops $({x_{i}\rightarrow x_{i}})$ in the original digraph, there can be edges of this type $(x_{i}^{+},x_{i}^{-})$ in the bipartite graph. A maximum matching of a bipartite graph can be found efficiently using the Hopcroft-Karp algorithm, which runs in $O{({\sqrt{V}E})}$ time.

<!-- chunk {"id": "body-0082", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

After running the algorithm, we can map the maximum matching in the bipartite representation, e.g. ${(x_{1}^{+},x_{2}^{-})},{(x_{3}^{+},x_{3}^{-})}$ in Fig. 9b, back to the maximum matching in the original diagraph, e.g. ${(x_{1},x_{2})},{(x_{3},x_{3})}$ in Fig. 9a, obtaining the desired maximum matching and hence the corresponding MDNS.

<!-- chunk {"id": "body-0083", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

Taken together, the maximum matching algorithm allows the efficient identification of the MDNS using the following steps (Fig. 10): (i) Start from the directed network we wish to control and generate its bipartite representation (Fig. 9). Next identify a maximum matching on the underlying bipartite graph using the Hopcroft-Karp algorithm. (ii) To each unmatched node add a unique control signal, as unmatched nodes represent the driver nodes. (iii) As there could be multiple maximum matchings for a general digraph, multiple MDNSs exist, with the same size $N_{D}$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

Recently, several algorithmic approaches have been developed to optimize the network controllability (in the sense of decreasing $N_{D}$) via minimal structural perturbations, like adding a minimum number of edges at judiciously chosen locations in the network, rewiring redundant edges, and assigning the direction of edges.

<!-- chunk {"id": "body-0085", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

*Maximum matching: analytical solution based on the cavity method*. While the maximum matching allows us to efficiently identify the MDNS, the algorithmic approach provides no physical insights about the impact of the network topology on $N_{D}$. For example, what network characteristics influence $N_{D}$, and how does $N_{D}$ depend on them? Which networks are easier to control and which are harder? To answer these questions we can turn to the cavity method, a versatile tool of statistical physics. We illustrate this approach by analytically calculating ${\overline{n}}_{D}$, representing the fraction of driver nodes $n_{D}$ ($\equiv {N_{D}/N}$) averaged over all network realizations compatible with the network's degree distribution $P{(k_{in},k_{out})}$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

According to the definition of matching in a digraph, matching edges do not share starting or end nodes, formally resulting in two constraints for each vertex $i \in {V{(G)}}$: (i) ${\sum_{j \in {\partial^{+}i}}s_{({i\rightarrow j})}} \leq 1$; (ii) ${\sum_{k \in {\partial^{-}i}}s_{({k\rightarrow i})}} \leq 1$ with $\partial^{-}i$ and $\partial^{+}i$ indicating the sets of nodes that point to $i$ or are pointed by $i$, respectively.

<!-- chunk {"id": "body-0087", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

We define the Boltzmann probability in the space of matchings as

<!-- chunk {"id": "body-0088", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

where $\beta$ is the inverse temperature and $\mathcal{Z}_{G}{(\beta)}$ is the partition function

<!-- chunk {"id": "body-0089", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

In the limit $\beta\rightarrow\infty$ (i.e. the zero temperature limit), the internal energy $\mathcal{E}_{G}{(\beta)}$ and the entropy $\mathcal{S}_{G}{(\beta)}$ provide the ground state properties, i.e. the properties of the maximum matchings. In particular, $\mathcal{E}_{G}{(\infty)}$ represents the number of unmatched vertices (with respect to any maximum matching), and the entropy $\mathcal{S}_{G}{(\infty)}$ yields the logarithm of the number of maximum matchings.

<!-- chunk {"id": "body-0090", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

In the zero temperature limit, the average fraction of driver nodes is given by

<!-- chunk {"id": "body-0091", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

While the cavity method does not offer a closed-form solution, Eq. allows us to systematically study the impact of key network characteristics, like the average degree $\langle k\rangle$ or the degree exponent $\gamma$, on ${\overline{n}}_{D}$ in the thermodynamic limit ($N\rightarrow\infty$). For example, for directed Erdős-Rényi random networks, both $P{(k_{in})}$ and $P{(k_{out})}$ follow a Poisson distribution, i.e. ${e^{- {{\langle k\rangle}/2}}{({{\langle k\rangle}/2})}^{k}}/{k!}$. In the large $\langle k\rangle$ limit we have

<!-- chunk {"id": "body-0092", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

One can show that as $\gamma\rightarrow 2$, we have $n_{D}\rightarrow 1$. This means one has to control almost all the nodes to achieve full control over the network. Therefore $\gamma = 2$ is the critical value for the controllability of scale-free networks, as only for $\gamma > 2$ can we obtain full controllability by controlling only a subset of the nodes. Note that for $\gamma\rightarrow 2$ super-hubs emerge that connect to almost all nodes in the network. We know that for a star-like digraph with one central hub and $N - 1$ leaves, one has to control $N_{D} = {N - 1}$ nodes (the central hub and any $N - 2$ leaves). In the large $N$ limit, ${N - 1} \approx N$, which explains intuitively why we have to control almost all nodes when $\gamma\rightarrow 2$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

For scale-free networks with degree exponent $\gamma_{in} = \gamma_{out} = \gamma$ generated from the static model, the parameters $\langle k\rangle$ and $\gamma$ are independent. In the thermodynamic limit the degree distribution is ${P{(k)}} = {\frac{{\lbrack{m{({1 - \alpha})}}\rbrack}^{1/\alpha}}{\alpha}\frac{\Gamma{({k - {1/\alpha}},{m{\lbrack{1 - \alpha}\rbrack}})}}{\Gamma{({k + 1})}}}$ where $\Gamma{(s)}$ is the gamma function and $\Gamma{(s,x)}$ the upper incomplete gamma function.

<!-- chunk {"id": "body-0094", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

If $\gamma_{in} \neq \gamma_{out}$, the smaller of the two exponents, i.e. $\min{\lbrack\gamma_{in},\gamma_{out}\rbrack}$ determines the asymptotic behavior of $n_{D}$. Equation indicates that as $\gamma\rightarrow 2$, $n_{D}\rightarrow 1$, which is consistent with the result that $\gamma_{c} = 2$ for a purely SF network.

<!-- chunk {"id": "body-0095", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

The systematic dependence of $n_{D}$ on $\langle k\rangle$ and $\gamma$ prompts us to ask: How do other network characteristics, like degree correlations, clustering, modularity, or the fraction of low degree nodes, influence $n_{D}$. A combination of analytical and numerical results indicate that the clustering coefficient and modularity have no discernible effect on $n_{D}$. At the same time the symmetries of the underlying matching problem generate linear, quadratic or no dependence on degree correlation coefficients, depending on the nature of the underlying degree correlations.

<!-- chunk {"id": "body-0096", "role": "body", "section": "II.4.1 Solution based on structural control theory", "weight": 1.0} -->

For uncorrelated directed networks, the density of nodes with ${k_{in},k_{out}} = 1$ or 2 determine the size of maximum matchings. This suggests that random networks whose minimum $k_{in}$ and $k_{out}$ are greater than two typically have perfect matchings and hence can be fully controlled via a single control input (i.e. $N_{D} = 1$), regardless of the other properties of the degree distribution.

<!-- chunk {"id": "body-0097", "role": "body", "section": "II.4.2 Solution based on PBH controllability test", "weight": 1.0} -->

In structural control theory we assume that the system parameters, like the link weights in $G{(\mathbf{A},\mathbf{B})}$, are either fixed zeroes or independent free parameters. This framework is ideal for many systems for which we only know the underlying wiring diagram (i.e. zero/nonzero values, indicating the absence/presence of physical connections) but not the link characteristics, like their weights. Yet, the independent free parameter assumption is very strong, and it is violated in some systems, like in undirected networks, where the state matrix $\mathbf{A}$ is symmetric, or unweighted networks, where all link weights are the same. In such cases structural control theory could yield misleading results on the minimum number of driver nodes $N_{D}$. Hence, it is important to move beyond structural control as we explore the controllability and other control related issues.

<!-- chunk {"id": "body-0098", "role": "body", "section": "II.4.2 Solution based on PBH controllability test", "weight": 1.0} -->

For LTI systems with exactly known system parameters the minimum input problem can be efficiently solved using the Popov-Belevitch-Hautus (PBH) controllability test. The PBH controllability test states that the system $(\mathbf{A},\mathbf{B})$ is controllable if and only if

<!-- chunk {"id": "body-0099", "role": "body", "section": "II.4.2 Solution based on PBH controllability test", "weight": 1.0} -->

Since the first $N \times N$ block of the $N \times {({N + M})}$ matrix $\lbrack{{s\mathbf{I}} - \mathbf{A}},\mathbf{B}\rbrack$ has full rank whenever $s$ is not an eigenvalue of $\mathbf{A}$, we only need to check each eigenvalue of $\mathbf{A}$, i.e. $s \in {\lambda{(\mathbf{A})}}$, when running the PBH test.

<!-- chunk {"id": "body-0100", "role": "body", "section": "II.4.2 Solution based on PBH controllability test", "weight": 1.0} -->

Note that the PBH test and Kalman's rank condition are equivalent. Yet, the advantage of the PBH test comes from the fact that it connects the controllability of $(\mathbf{A},\mathbf{B})$ to the eigenvalues and eigenvectors of the state matrix $\mathbf{A}$. This can be used to solve the minimum input problem exactly. Indeed, the PBH controllability test suggests that $(\mathbf{A},\mathbf{B})$ is controllable if and only if there is no left eigenvector of $\mathbf{A}$ orthogonal to all the columns of $\mathbf{B}$. In other words, the columns of $\mathbf{B}$ must have a component in each eigendirection of $\mathbf{A}$.

<!-- chunk {"id": "body-0101", "role": "body", "section": "II.4.2 Solution based on PBH controllability test", "weight": 1.0} -->

Recall that for an eigenvalue $\lambda_{0} \in {\lambda{(\mathbf{A})}}$, its *algebraic multiplicity* is the multiplicity of $\lambda_{0}$ as a root of the characteristic polynomial ${p{(\lambda)}} = {\det{({\mathbf{A} - {\lambda\mathbf{I}}})}}$. Its *geometric multiplicity* is the maximal number of linearly independent eigenvectors corresponding to it. Hence, the number of control inputs must be greater than or equal to the largest geometric multiplicity of the eigenvalues of $\mathbf{A}$. In other words, the minimum number of control inputs (or equivalently the minimum number of driver nodes) is determined by the maximum geometric multiplicity of the eigenvalues of $\mathbf{A}$, i.e.

<!-- chunk {"id": "body-0102", "role": "body", "section": "II.4.2 Solution based on PBH controllability test", "weight": 1.0} -->

Based, we can develop an efficient algorithm to identify the minimum set of driver nodes for arbitrary LTI systems (Fig. 12), allowing us to explore the impact of the network topology and link-weight distributions on $N_{D}$. For undirected and unweighted ER networks of connectivity probability $p$, the results indicate that for small $p$, $n_{D}$ decreases with $p$, while for sufficiently large $p$, $n_{D}$ increases to ${({N - 1})}/N$, which is exact for $p = 1$ (complete graph, see Table. 1). This approach has been recently extended to multiplex networks.

<!-- chunk {"id": "body-0103", "role": "body", "section": "II.5 Minimal Controllability Problems", "weight": 1.0} -->

Any networked system with LTI dynamics is fully controllable if we control each node individually with an independent signal, i.e. $M = N$. But this is costly and typically impractical for large complex systems. Hence, we are particularly interested in fully controlling a network with minimum number of nodes. Depending on the objective function and the way we "inject" input signals, we can formalize different types of *minimal controllability problems* (MCPs).

<!-- chunk {"id": "body-0104", "role": "body", "section": "II.5 Minimal Controllability Problems", "weight": 1.0} -->

(MCP0): One scenario is that we try to minimize the number of independent control signals, corresponding to the number of columns in the input matrix $\mathbf{B}$, or equivalently, the number of *driver nodes* whose control is sufficient to fully control the system's dynamics (Fig. 13a). This is nothing but the minimum inputs problem discussed in the previous subsection.

<!-- chunk {"id": "body-0105", "role": "body", "section": "II.5 Minimal Controllability Problems", "weight": 1.0} -->

(MCP1): We assume dedicated inputs, i.e. each control input $u_{i}$ can only directly control one node (state variable). In the matrix form, this amounts to finding a diagonal matrix $\mathbf{B} \in {\mathbb{R}}^{N \times N}$ that has as few nonzero entries as possible so that the LTI system $\overset{˙}{\mathbf{x}} = {{\mathbf{A}\mathbf{x}} + {\mathbf{B}\mathbf{u}}}$ is controllable (Fig. 13b).

<!-- chunk {"id": "body-0106", "role": "body", "section": "II.5 Minimal Controllability Problems", "weight": 1.0} -->

(MCP2): We set ${u_{i}{(t)}} = {u{(t)}}$ and aim to find a vector $\mathbf{b}$ that has as few nonzero entries as possible such that the system $\overset{˙}{\mathbf{x}} = {{\mathbf{A}\mathbf{x}} + {\mathbf{b}u}}$ is controllable (Fig. 13c).

<!-- chunk {"id": "body-0107", "role": "body", "section": "II.5 Minimal Controllability Problems", "weight": 1.0} -->

Note that in solving MCP0, one signal can be applied to multiple nodes. The number of *actuator nodes* (corresponding to those non-zero entries in $\mathbf{B}$) is not necessarily minimized. In MCP1 $\mathbf{u}{(t)}$ is a vector of control inputs, i.e. we have multiple input signals, while in MCP2, $u{(t)}$ is a scalar, i.e. there is only one input signal. In both cases, we try to minimize the number of *actuator nodes* that are directly controlled by input signals.

<!-- chunk {"id": "body-0108", "role": "body", "section": "II.5 Minimal Controllability Problems", "weight": 1.0} -->

Though MCP0 for a general LTI system is easy to solve, MCP1 and MCP2 are NP-hard. Yet, if we need to guarantee only structural controllability, MCP1 can be easily solved. For a directed network $G$ with LTI dynamics the minimum number of dedicated inputs (or actuators), $N_{da}$, required to assure structural controllability, is

<!-- chunk {"id": "body-0109", "role": "body", "section": "II.5 Minimal Controllability Problems", "weight": 1.0} -->

where $N_{D}$ is the minimum number of driver nodes; $\beta$ is the number of *root* strongly connected components (rSCCs), which have no incoming links from other SCCs; and $\alpha$ is the *maximum assignability index* of the bipartite representation $\mathcal{B}{(G)}$ of the directed network $G$. An rSCC is said to be a top assignable SCC if it contains at least one driver node with respect to a particular maximum matching $M^{\ast}$. The maximum assignability index of $\mathcal{B}{(G)}$ is the maximum number of top assignable SCCs that a maximum matching $M^{\ast}$ may lead to. The minimum set of actuators can be found with polynomial time complexity.

<!-- chunk {"id": "body-0110", "role": "body", "section": "II.6 Role of Individual Nodes and Links", "weight": 1.0} -->

As we have seen in Sec.7, a system with $N_{D}$ driver nodes can be controlled by multiple driver node configurations, each corresponding to a different maximum matching (Fig. 10). Some links may appear more often in the maximum matchings than other links. This raises a fundamental question: What is the role of the individual node (or link) in control? Are some nodes (or links) more important for control than others? To answer these questions, in this section we discuss the classification of nodes and links based on their role and importance in the control of a given network.

<!-- chunk {"id": "body-0111", "role": "body", "section": "II.6.1 Link classification", "weight": 1.0} -->

In both natural and technological systems we need to quantify how robust is our ability to control a network under unavoidable link failure. To adress this question, we can use structural controllability to classify each link into one of the following three categories: a link is *critical* if in its absence we must increase the number of driver nodes to maintain full control over the system. In this case the link is part of *all* maximum matchings of the network; a link is *redundant* if it can be removed without affecting the current set of driver nodes (i.e. it does not appear in any maximum matching); a link is *ordinary* if it is neither critical nor redundant (it appears in some but not all maximum matchings). Note that this classification can be efficiently done with a polynomial-time algorithm based on Berge's property, rather than enumerating all maximum matchings, which is infeasible for large networks.

<!-- chunk {"id": "body-0112", "role": "body", "section": "II.6.1 Link classification", "weight": 1.0} -->

We can compute the density of critical ($l_{c} = {L_{c}/L}$), redundant ($l_{r} = {L_{r}/L}$) and ordinary ($l_{o} = {L_{o}/L}$) links for a wide range of real-world networks. It turns out that most real networks have few or no critical links. Most links are ordinary, meaning that they play a role in some control configurations, but the network can be still controlled in their absence.

<!-- chunk {"id": "body-0113", "role": "body", "section": "II.6.1 Link classification", "weight": 1.0} -->

For model networks (ER and SF), we can calculate $l_{c}$, $l_{r}$, and $l_{o}$ as functions of $\langle k\rangle$ (Fig. 14). The behavior of $l_{c}$ is easy to understand: for small $\langle k\rangle$ all links are essential for control ($l_{c} \approx 1$). As $\langle k\rangle$ increases the network's redundancy increases, decreasing $l_{c}$. The increasing redundancy suggests that the density of redundant links, $l_{r}$, should always increase with $\langle k\rangle$, but it does not: it reaches a maximum at ${\langle k\rangle}_{c}$, after which it decays. This non-monotonic behavior results from a structural transition driven by core percolation.

<!-- chunk {"id": "body-0114", "role": "body", "section": "II.6.1 Link classification", "weight": 1.0} -->

Here, the *core* represents a compact cluster of nodes left in the network after applying a *greedy leaf removal* procedure: Recursively remove in-leaf (with $k_{in} = 1$) and out-leaf (with $k_{out} = 1$) nodes' neighbors' all outgoing (or incoming) links. The core emerges through a percolation transition (Fig. 14b,d): for $k < {\langle k\rangle}_{c}$, $n_{core} = {N_{core}/N} = 0$, so the system consists of leaves only. At ${\langle k\rangle}_{c}$ a small core emerges, decreasing the number of leaves. For ER random networks, the analytical calculations predict ${\langle k\rangle}_{c} = {2e} \approx 5.436564$, in agreement with the numerical result (Fig. 14b), a value that coincides with $\langle k\rangle$ where $l_{r}$ reaches its maximum.

<!-- chunk {"id": "body-0115", "role": "body", "section": "II.6.1 Link classification", "weight": 1.0} -->

Indeed, $l_{r}$ starts decaying at ${\langle k\rangle}_{c}$ because after ${\langle k\rangle}_{c}$ the number of distinct maximum matchings increases exponentially, which can be confirmed by calculating the ground state entropy using the cavity method. Consequently, the chance that a link does *not* participate in *any* control configurations decreases. For SF networks we observe the same behavior, with the caveat that ${\langle k\rangle}_{c}$ decreases with $\gamma$ (Fig. 14c, d).

<!-- chunk {"id": "body-0116", "role": "body", "section": "II.6.2 Node Classification", "weight": 1.0} -->

Given the existence of multiple driver node configurations, we can classify nodes based on their likelihood of being included in the minimum driver node set (MDNS): a node is *critical* if that node must always be controlled to control the system, implying that it is part of all MDNSs; *redundant* if it is never required for control, implying that it never participates in an MDNS; and *intermittent* if it is a driver node in some control configurations, but not in others.

<!-- chunk {"id": "body-0117", "role": "body", "section": "II.6.2 Node Classification", "weight": 1.0} -->

For model networks with symmetric in- and out-degree distributions, we find that the fraction of redundant nodes ($n_{r}$) undergoes a *bifurcation* at a critical mean degree ${\langle k\rangle}_{c}$: for low $\langle k\rangle$ the fraction of redundant nodes ($n_{r}$) is uniquely determined by $\langle k\rangle$, but beyond ${\langle k\rangle}_{c}$ two different solutions for $n_{r}$ coexist, one with very high and the other with very low value, leading to a bimodal behavior (Fig. 15a). Hence for large $\langle k\rangle$ (after the bifurcation) two control modes coexist: (i) *Centralized control*: In networks that follow the upper branch of the bifurcation diagram most of the nodes are redundant, as in this case $n_{r}$ is very high.

<!-- chunk {"id": "body-0118", "role": "body", "section": "II.6.2 Node Classification", "weight": 1.0} -->

This means that in these networks only a small fraction of the nodes are involved in control ($n_{c} + n_{i}$ is very low), hence control is guaranteed by a few nodes in the network. A good analogy would be a company involved in manufacturing whose leadership is concentrated in the hands of a few managers and the rest of the employees are only executors. (ii) *Distributed control*: In networks on the lower branch $n_{c} + n_{i}$ can exceed 90%. Hence, most nodes participate as driver nodes in some MDNSs, implying that one can engage most nodes in control. A good analogy would be an innovation-based horizontal organization, where any employee can take a leadership role, as the shifting tasks require.

<!-- chunk {"id": "body-0119", "role": "body", "section": "II.6.2 Node Classification", "weight": 1.0} -->

For ER random networks this bifurcation occurs at ${\langle k\rangle}_{c} = {2e}$, corresponding to the core percolation threshold.

<!-- chunk {"id": "body-0120", "role": "body", "section": "II.6.2 Node Classification", "weight": 1.0} -->

Another way to assess a node's importance for control is to quantify the impact of its removal on controllability. Consider a network with minimum number of driver nodes $N_{D}$. After a node is removed (deleted), denote the minimum number of driver nodes with $N_{D}^{\prime}$. Once again, each node can belong to one of three categories: A node is *deletion critical* if in its absence we have to control more driver nodes, i.e. $N_{D}^{\prime} > N_{D}$. For example, removing a node in the middle of a directed path will increase $N_{D}$. A node is *deletion redundant* if in its absence we have $N_{D}^{\prime} < N_{D}$. For example, removing a leaf node in a star will decrease $N_{D}$ by 1. A node is *deletion ordinary* if in its absence $N_{D}^{\prime} = N_{D}$.

<!-- chunk {"id": "body-0121", "role": "body", "section": "II.6.2 Node Classification", "weight": 1.0} -->

For example, removing the central hub in a star will not change $N_{D}$. The above node classification has been applied to directed human protein-protein interaction networks, whose directions indicate signal flow. In this context critical nodes tend to correspond to disease genes, viral tagets, through which a virus takes control over its host, and targets of FDA approved drugs, indicating that control-based classification can select biologically relevant proteins.

<!-- chunk {"id": "body-0122", "role": "body", "section": "II.6.3 Driver node classification", "weight": 1.0} -->

To understand why a node is a driver node, we decompose the driver nodes ($N_{D}$) into three groups: *source nodes* ($N_{s}$) that have no incoming links, hence they must be directly controlled, being always driver nodes; *external dilations* ($N_{e}$) arise due to a surplus of sink nodes ($N_{t}$) that have no outgoing links. Since each source node can control one sink node, the number of external dilation is $N_{e} = {\max{(0,{N_{t} - N_{s}})}}$; *internal dilations* ($N_{i}$) occur when a path must branch into two or more paths in order to reach all nodes (or equivalently a subgraph has more outgoing links than incoming links).

<!-- chunk {"id": "body-0123", "role": "body", "section": "II.6.3 Driver node classification", "weight": 1.0} -->

This classification leads to the control profile of a network defined as ${(\eta_{s},\eta_{e},\eta_{i})} = {({N_{s}/N},{N_{e}/N},{N_{i}/N})}$, which quantifies the different proportions of control-inducing structures present in a network. The measurements indicate that random network models do not reproduce the control profiles of real-world networks and that the control profiles of real networks group into three well-defined clusters, dominated by external-dilations, sources, or internal-dilations.

<!-- chunk {"id": "body-0124", "role": "body", "section": "II.6.3 Driver node classification", "weight": 1.0} -->

These results offer insight into the high-level organization and function of complex networks. For example, neural and social network are source dominated, which allow relatively uncorrelated behavior across their agents and are thus suitable to distributed processing. Food webs and airport interconnectivity networks are internal-dilation dominated. They are mostly closed systems and obey some type of conservation laws. In contrast, trust hierarchies and transcriptional systems are external-dilation dominated. With their surplus sink nodes, these systems display correlated behavior across their agents that are downstream neighbors of a common source.

<!-- chunk {"id": "body-0125", "role": "body", "section": "II.7 Controllable Subspace, Control Centrality, and Structure Permeability", "weight": 1.0} -->

Lin's structural controllability theorem can tell us whether an LTI system $(\mathbf{A},\mathbf{B})$ is structurally controllable or not. If, however, the system is not structurally controllable, the theorem does not provide further information about controllability. Even if we are unable to make the system reach any point in the state space, we would like to understand which region of the state space is accessible to it, i.e., what region of the state space can we control it. For example, in the network of Fig. 4a the control input $u_{1}$ is applied to the central hub $x_{1}$ of the directed star with $N = 3$ nodes. The system is therefore stuck in the plane described by ${a_{31}x_{2}{(t)}} = {a_{21}x_{3}{(t)}}$, shaded in Fig. 4b. Consequently, the network is not controllable in the whole state space, but it is controllable within the subspace defined by the plane.

<!-- chunk {"id": "body-0126", "role": "body", "section": "II.7 Controllable Subspace, Control Centrality, and Structure Permeability", "weight": 1.0} -->

When we control a single node $i$, the input matrix $\mathbf{B}$ reduces to a vector $\mathbf{b}{(i)}$ with a single non-zero entry, and the controllability matrix $\mathbf{C} \in {\mathbb{R}}^{N \times N}$ becomes $\mathbf{C}{(i)}$. We can use ${rank}{({\mathbf{C}{(i)}})}$ as a natural measure of node $i$'s ability to control the system. If ${{rank}{({\mathbf{C}{(i)}})}} = N$, then node $i$ alone can control the whole system. Any ${rank}{({\mathbf{C}{(i)}})}$ less than $N$ yields the dimension of the subspace $i$ can control.

<!-- chunk {"id": "body-0127", "role": "body", "section": "II.7 Controllable Subspace, Control Centrality, and Structure Permeability", "weight": 1.0} -->

For example, if ${{rank}{({\mathbf{C}{(i)}})}} = 1$, then node $i$ can only control itself.

<!-- chunk {"id": "body-0128", "role": "body", "section": "II.7 Controllable Subspace, Control Centrality, and Structure Permeability", "weight": 1.0} -->

In reality the system parameters (i.e. the entries of $\mathbf{A}$ and $\mathbf{B}$) are often not known precisely, except the zeros that mark the absence of connections, rendering the calculation of ${rank}{({\mathbf{C}{(i)}})}$ difficult. This difficulty can be again avoided using structural control theory. Assuming $\mathbf{A}$ and $\mathbf{B}$ are structured matrices, i.e., their elements are either fixed zeros or independent free parameters, then ${rank}{({\mathbf{C}{(i)}})}$ varies as a function of the free parameters of $\mathbf{A}$ and $\mathbf{B}$. However, it achieves its maximum for almost all sets of values of the free parameters except for some pathological cases with Lebesgue measure zero.

<!-- chunk {"id": "body-0129", "role": "body", "section": "II.7 Controllable Subspace, Control Centrality, and Structure Permeability", "weight": 1.0} -->

This maximal value is called the *generic rank* of the controllability matrix $\mathbf{C}{(i)}$, denoted as ${rank}_{g}{({\mathbf{C}{(i)}})}$, which also represents the *generic dimension* of the controllable subspace.

<!-- chunk {"id": "body-0130", "role": "body", "section": "II.7 Controllable Subspace, Control Centrality, and Structure Permeability", "weight": 1.0} -->

We define the control capacity of a single node $i$, or *control centrality*, as the *generic dimension* of the controllable subspace

<!-- chunk {"id": "body-0131", "role": "body", "section": "II.7 Controllable Subspace, Control Centrality, and Structure Permeability", "weight": 1.0} -->

Here ${rank}_{g}\mathbf{C}$ is the *generic rank* of the controllability matrix $\mathbf{C}$ associated with the structured system $(\mathbf{A},\mathbf{b})$, where we control node $i$ only. This definition can also be extended to the case when we control via a group of nodes. The above definition corresponds directly to our intuition of how powerful a single node is (or a group of nodes are) in controlling the whole network. For example, if the control capacity of a single node is $N$, then we can control the whole system through it.

<!-- chunk {"id": "body-0132", "role": "body", "section": "II.7 Controllable Subspace, Control Centrality, and Structure Permeability", "weight": 1.0} -->

The calculation of $d_{c}{(\mathbf{A},\mathbf{B})}$ has a graph-theoretic interpretation. Consider a structured system $(\mathbf{A},\mathbf{B})$, in which all state vertices are accessible, and let us denote with $\mathcal{G}$ the set of subgraphs of $G{(\mathbf{A},\mathbf{B})}$ which can be spanned by a collection of vertex-disjoint cycles and stems. In this case, the generic dimension of the controllable subspace is

<!-- chunk {"id": "body-0133", "role": "body", "section": "II.7 Controllable Subspace, Control Centrality, and Structure Permeability", "weight": 1.0} -->

where $|{E{(G)}}|$ is the number of edges in the subgraph $G$. This is called Hosoe's *controllable subspace theorem*. Essentially, Hosoe's theorem tells us that to calculate the generic dimension of the controllable subspace we need to find the cactus that contains as many edges as possible. Note that Hosoe's theorem applies only to a structured system $(\mathbf{A},\mathbf{B})$ that has no inaccessible state vertices. In calculating $d_{c}{(\mathbf{A},\mathbf{B})}$ for a general system $(\mathbf{A},\mathbf{B})$, we should only consider the accessible part of the network.

<!-- chunk {"id": "body-0134", "role": "body", "section": "II.7 Controllable Subspace, Control Centrality, and Structure Permeability", "weight": 1.0} -->

For a digraph with no directed cycles Hosoe's theorem further simplifies: the controllability of any node equals its layer index: ${{C_{s}{(i)}} = l_{i}}.$ Here the layer index of a node is calculated from the unique hierarchical structure of the digraph following a recursive labeling procedure. For general networks, we can use linear programming to calculate $d_{c}{(\mathbf{A},\mathbf{B})}$.

<!-- chunk {"id": "body-0135", "role": "body", "section": "II.7 Controllable Subspace, Control Centrality, and Structure Permeability", "weight": 1.0} -->

A collection of node-disjoint cycle in $G^{\prime}{(\mathbf{A},\mathbf{B})}$ covering all nodes will be called a *cycle partition*.

<!-- chunk {"id": "body-0136", "role": "body", "section": "II.7 Controllable Subspace, Control Centrality, and Structure Permeability", "weight": 1.0} -->

Hosoe's theorem also allows us to address a problem complementary to the notion of control centrality: identify an optimal set of driver nodes of fixed cardinality $M$, denoted as $\Omega_{D}{(M)}$, for a network of size $N$ such that the dimension of the controllable subspace, denoted as $|{\mathcal{C}{(M)}}|$, is maximized. If we solve this problem for each $M \in {\lbrack 1,N\rbrack}$, we obtain a sequence of $|{\mathcal{C}{(M)}}|$. To quantify the readiness or propensity of a network to be controllable, we can calculate the so-called *network permeability* measure

<!-- chunk {"id": "body-0137", "role": "body", "section": "II.7 Controllable Subspace, Control Centrality, and Structure Permeability", "weight": 1.0} -->

Note that $\mu \in {\lbrack 0,1\rbrack}$: 0 for $N$ disconnected nodes, and 1 for networks that are completely controllable by one driver node. Generally, for a network with a high permeability, a large controllable subspace can be obtained with a reasonable small set of driver nodes.

<!-- chunk {"id": "body-0138", "role": "body", "section": "II.8 Controlling Edges", "weight": 1.0} -->

So far we focused on nodal dynamics, where we monitored and controlled the state of nodes. The sole purpose of the edges was to pass information or influence between the nodes. In social or communication networks nodes constantly process the information received from their upstream neighbors and make decisions that are communicated to their downstream neighbors. Most importantly, in these systems nodes can communicate different information along different edges. Hence the information received and passed on by a node can be best represented by state variables defined on the incoming and outgoing edges, respectively. In this section we ask how to control systems characterized by such edge dynamics.

<!-- chunk {"id": "body-0139", "role": "body", "section": "II.8 Controlling Edges", "weight": 1.0} -->

To model such systems we place the state variables on the edges. Let $\mathbf{y}_{i}^{-}{(t)}$ and $\mathbf{y}_{i}^{+}{(t)}$ represent vectors consisting of the state variables associated with the incoming and outgoing edges of node $i$, respectively. Let $\mathbf{M}_{i}$ denote the ${{k_{out}{(i)}} \times k_{in}}{(i)}$ matrix. The equations governing the edge dynamics can be written as

<!-- chunk {"id": "body-0140", "role": "body", "section": "II.8 Controlling Edges", "weight": 1.0} -->

where ${\mathbf{τ}}_{i}$ is a vector of damping terms associated with the outgoing edges, $\otimes$ denotes the entry-wise product of two vectors of the same size, and $\sigma_{i} = 1$ if node $i$ is a driver node and 0 otherwise. Note that even though the state variables and the control inputs are defined on the edges, we can still designate a node to be a driver node if its outgoing edges are directly controlled by the control inputs. Equation states that the state variables of the outgoing edges of node $i$ are determined by the state variables of the incoming edges, modulated by a decay term. For a driver node, the state variables of its outgoing edges will also be influenced by the control signals $\mathbf{u}_{i}$. Since each node $i$ acts as a small switchboard-like device mapping the signals of the incoming edges to the outgoing edges using a linear operator $\mathbf{M}_{i}$, Eq. is often called the *switchboard dynamics*.

<!-- chunk {"id": "body-0141", "role": "body", "section": "II.8 Controlling Edges", "weight": 1.0} -->

There is a mathematical duality between edge dynamics on a network $G$ and nodal dynamics on its *line graph* $\mathcal{L}{(G)}$, which represents the adjacencies between edges of $G$. Each node of $\mathcal{L}{(G)}$ corresponds to an edge in $G$, and each edge in $\mathcal{L}{(G)}$ corresponds to a length-two directed path in $G$. By applying the minimum input theorem directly to this line graph, we obtain the minimum number of edges we must drive to control the original network. However, this procedure does not minimize the number of driver nodes in the original network. This edge control problem can be mapped to a graph theoretical problem as follows.

<!-- chunk {"id": "body-0142", "role": "body", "section": "II.8 Controlling Edges", "weight": 1.0} -->

Define node $i$ to be (i) *divergent*, if ${k_{out}{(i)}} > {k_{in}{(i)}}$; (ii) *convergent*, if ${k_{out}{(i)}} < {k_{in}{(i)}}$; (iii) *balanced*, if ${k_{out}{(i)}} = {k_{in}{(i)}}$. A connected component in a directed network is called a *balanced component* if it contains at least one edge and all the nodes are balanced. We can prove that the minimum set of driver nodes required to maintain structural controllability of the switchboard dynamics on a directed network $G$ can be determined by selecting the divergent nodes of $G$ and an arbitrary node from each balanced component.

<!-- chunk {"id": "body-0143", "role": "body", "section": "II.8 Controlling Edges", "weight": 1.0} -->

The controllability properties of this edge dynamics significantly differ from simple nodal dynamics. For example, driver nodes prefer hubs with large out-degree and heterogeneous networks are more controllable, i.e., require fewer driver nodes, than homogeneous networks. Moreover, positive correlations between the in- and out-degree of a node enhances the controllability of edge dynamics, without affecting the controllability of nodal dynamics. Conversely, adding self-loops to individual nodes enhances the controllability of nodal dynamics, but leaves the controllability of edge dynamics unchanged.

<!-- chunk {"id": "body-0144", "role": "body", "section": "II.9 Self-Dynamics and its Impact on Controllability", "weight": 1.0} -->

The nodes of networked systems are often characterized by some self-dynamics, e.g. a term of the form ${\overset{˙}{x}}_{i} = {a_{ii}x_{i}}$, which captures the node's behavior in the absence of interactions with other nodes. If we naively apply structural control theory to systems where each node has a self-dynamic term we obtain a surprising result --- a single control input can make an arbitrarily large linear system controllable. This result represents a special case of the minimum input theorem: The self-dynamics contributes a self-loop to each node, hence each node can be matched by itself. Consequently, $G{(\mathbf{A})}$ has a perfect matching, independent of the network topology, and one input signal is sufficient to control the whole system.

<!-- chunk {"id": "body-0145", "role": "body", "section": "II.9 Self-Dynamics and its Impact on Controllability", "weight": 1.0} -->

To understand the true impact of self-dynamics on network controllability, we must revisit the validity of the assumption that the system parameters are independent of each other. As we show next, relaxing this assumption offers a more realistic characterization of real systems, for which not all system parameters are independent.

<!-- chunk {"id": "body-0146", "role": "body", "section": "II.9 Self-Dynamics and its Impact on Controllability", "weight": 1.0} -->

Assuming prototypical linear form of self-dynamics, e.g., first-order $\overset{˙}{x} = {a_{0}x}$, second-order $\overset{¨}{x} = {{a_{0}x} + {a_{1}\overset{˙}{x}}}$, etc, we can incorporate the linear self-dynamics with the LTI dynamics of the network in a unified matrix form, as illustrated in Fig. 18. An immediate but counterintuitive result states that in the absence of self-dynamics $n_{D}$ is exactly the same as in the case when each node has a self-loop with identical weight $w$, i.e. each node is governed by precisely the same self-dynamics. This is a direct consequence of the identity

<!-- chunk {"id": "body-0147", "role": "body", "section": "II.9 Self-Dynamics and its Impact on Controllability", "weight": 1.0} -->

where on the left we have the rank of controllability matrix in the absence of self-loops, and on the right the same for a network where each node has an identical self-loop. For more general cases the minimum number of driver nodes $N_{D}$ can be calculated, i.e. the maximum geometric multiplicity of $\mathbf{A}$'s eigenvalues.

<!-- chunk {"id": "body-0148", "role": "body", "section": "II.9 Self-Dynamics and its Impact on Controllability", "weight": 1.0} -->

Note a remarkable symmetry in network controllability: If we exchange the fractions of any two types of self-loops with distinct weights, the system's controllability, as measured by $n_{D}$, remains the same (Fig. 19). For example, consider a network without self-loops. Equivalently, we can assume that each node contains a self-loop with weight zero. Then we systematically add more non-zero self-loops with identical weights to the network. Equivalently, we are replacing the zero-weight self-loops with non-zero self-loops. $n_{D}$ will first decrease as the fraction $\rho$ of non-zero self-loops increases, reaching a minimum at $\rho = \frac{1}{2}$. After that, $n_{D}$ increases, reaching its maximum at $\rho = 1$, which coincides with $n_{D}$ observed for $\rho = 0$ (Fig. 19a). We can introduce more types of self-loops with different weights.

<!-- chunk {"id": "body-0149", "role": "body", "section": "II.9 Self-Dynamics and its Impact on Controllability", "weight": 1.0} -->

If we exchange the fractions of any two types of self-loops, $n_{D}$ remains the same. This exchange-invariant property gives rise to a global symmetry point, where all the different types of self-loops have equal densities and the system displays the highest controllability (i.e., lowest number of driver nodes). This symmetry-induced optimal controllability holds for any network topology and various individual dynamics.

<!-- chunk {"id": "body-0150", "role": "body", "section": "II.10 Control Energy", "weight": 1.0} -->

Indentifying the minimum number of driver or actuator nodes sufficient for control is only the first step of the control problem. Once we have that, we need to ask an equally important question: How much effort is required to control a system from a given set of nodes? The meaning of the term "control effort" depends upon the particular application. In the case of a rocket being thrust upward, the control input $u{(t)}$ is the thrust of the engine, whose magnitude $|{u{(t)}}|$ is assumed to be proportional to the rate of fuel consumption. In order to minimize the total expenditure of fuel, the control effort can be defined as $\int_{0}^{T}{{|{u{(t)}}|}{dt}}$, which is related to the energy consumed by the rocket. In the case of a voltage source driving a circuit containing no energy storage elements, the source voltage is the control input $u{(t)}$ and the source current is directly proportional to $u{(t)}$.

<!-- chunk {"id": "body-0151", "role": "body", "section": "II.10 Control Energy", "weight": 1.0} -->

If the circuit is to be controlled with minimum energy dissipation, we can define the control effort as $\int_{0}^{T}{u^{2}{(t)}{dt}}$, which is proportional to the energy dissipation. If there are several control inputs, the general form of control effort can be defined as $\int_{0}^{T}{\mathbf{u}^{T}{(t)}\mathbf{R}{(t)}\mathbf{u}{(t)}{dt}}$, where $\mathbf{R}{(t)}$ is a real symmetric positive-definite weighting matrix.

<!-- chunk {"id": "body-0152", "role": "body", "section": "II.10 Control Energy", "weight": 1.0} -->

Consider the LTI system driven from an arbitrary initial state $\mathbf{x}_{i}$ towards a desired final state $\mathbf{x}_{f}$ by the external signal $\mathbf{u}{(t)}$ in the time interval $t \in {\lbrack 0,T\rbrack}$. We define the associated control effort in the quadratic form

<!-- chunk {"id": "body-0153", "role": "body", "section": "II.10 Control Energy", "weight": 1.0} -->

called the "control energy" in the literature. Note that may not have the physical dimension of energy, i.e., M L^2^ T^-2^, in real control problems. But for physical and electronic systems we can always assume there is an hidden constant in the right-hand side of with proper dimension, which ensures that $\mathcal{E}{(T)}$ has the dimension of energy. In many systems, like biological or social systems, where does not correspond to energy, it captures the effort needed to control a system.

<!-- chunk {"id": "body-0154", "role": "body", "section": "II.10 Control Energy", "weight": 1.0} -->

For a fixed set of driver nodes the control input $\mathbf{u}{(t)}$ that can drive the system from $\mathbf{x}_{i}$ to $\mathbf{x}_{f}$ can be chosen in many different ways, resulting in different trajectories followed by the system. Each of these trajectories has its own control energy. Of all the possible inputs, the one that yields the minimum control energy is

<!-- chunk {"id": "body-0155", "role": "body", "section": "II.10 Control Energy", "weight": 1.0} -->

where $\mathbf{W}{(t)}$ is the *gramian matrix*

<!-- chunk {"id": "body-0156", "role": "body", "section": "II.10 Control Energy", "weight": 1.0} -->

which is nonsingular for any $t > 0$. Note that $\mathbf{W}{(\infty)}$ is known as the *controllability Gramian*, often denoted with $\mathbf{W}_{c}$. The energy associated with the optimal input is ${\mathcal{E}{(T)}} = {\mathbf{v}_{f}^{T}\mathbf{W}^{- 1}{(T)}\mathbf{v}_{f}}$, where $\mathbf{v}_{f} \equiv {\mathbf{x}_{f} - {{\exp{({\mathbf{A}T})}}\mathbf{x}_{i}}}$ represents the difference between the desired state under control and the final state during free evolution without control. Without loss of generality, we can set the final state at the origin, $\mathbf{x}_{f} = \mathbf{0}$, and write the control energy as

<!-- chunk {"id": "body-0157", "role": "body", "section": "II.10 Control Energy", "weight": 1.0} -->

When $\mathbf{x}_{i}$ is parallel to the direction of one of H's eigenvectors, the inverse of the corresponding eigenvalue corresponds to normalized energy associated with controlling the system along the particular eigen-direction.

<!-- chunk {"id": "body-0158", "role": "body", "section": "II.10 Control Energy", "weight": 1.0} -->

Using the Rayleigh-Ritz theorem, the normalized control energy obeys the bounds

<!-- chunk {"id": "body-0159", "role": "body", "section": "II.10 Control Energy", "weight": 1.0} -->

where $\eta_{\max}$ and $\eta_{\min}$ the maximum and minimum eigenvalues of $\mathbf{H}$, respectively.

<!-- chunk {"id": "body-0160", "role": "body", "section": "II.10 Control Energy", "weight": 1.0} -->

Assuming linear individual dynamics characterized by the self-loop $a_{ii} = {- {({a + s_{i}})}}$ where $s_{i} = {\sum_{j \neq i}s_{ij}}$ is the strength of node $i$ and $a$ is a parameter that can make the symmetric $\mathbf{A}$ (describing an undirected network) either positive or negative definite, we can choose a single node with index $c$ as the driver node. In this case, the lower and upper energy bounds follow

<!-- chunk {"id": "body-0161", "role": "body", "section": "II.10 Control Energy", "weight": 1.0} -->

Here $\lambda_{1} > \lambda_{2} > \cdots > \lambda_{N}$ are the eigenvalues of $\mathbf{A}$, and $\varepsilon{(\mathbf{A},c)}$ is a positive energy that depends on the matrix $\mathbf{A}$ and the choice of the controlled node $c$. PD (or ND) means positive-definite (or negative-definite), respectively. The scaling laws and can be generalized to directed networks, in which case the decay exponents $\lambda_{1}$ and $\lambda_{N}$ are replaced by ${Re}\lambda_{1}$ and ${Re}\lambda_{N}$, respectively.

<!-- chunk {"id": "body-0162", "role": "body", "section": "II.10 Control Energy", "weight": 1.0} -->

Equations and suggest that the scaling of the control energy is rather sensitive to the control time $T$. For small $T$, in which case we wish to get our system very fast to its destination, both $E_{\min}$ and $E_{\max}$ decay with increasing $T$, implying that setting a somewhat longer control time requires less energy. For large $T$, however, we reach a point where we cannot reduce the energy by waiting for longer time. This occurs when the system has its equilibrium point in the origin, then any attempt to steer the system away from the origin must overcome a certain energy barrier.

<!-- chunk {"id": "body-0163", "role": "body", "section": "II.10 Control Energy", "weight": 1.0} -->

The control energy is rather sensitive to the direction of the state space in which we wish to move the system. To see this, consider a scale-free network with degree exponent $\gamma$. If we drive the system through all its nodes ($N_{D} = N$), the control energy spectrum, describing the probability that moving in a randomly chosen eigen-direction will require energy $\mathcal{E}$, follows the power law ${P{(\mathcal{E})}} \sim \mathcal{E}^{- \gamma}$. Consequently, the maximum energy required for control depends sublinearly on the system size, $\mathcal{E}_{\max} \sim N^{1/{({\gamma - 1})}}$, implying that even in the most costly direction the required energy grows slower than the system size. In other words, if we control each node, there are no significant energetic barriers for control.

<!-- chunk {"id": "body-0164", "role": "body", "section": "II.10 Control Energy", "weight": 1.0} -->

If, however, we aim to control the system through a single node ($N_{D} = 1$), the control spectrum follows a power law with exponent $- 1$, i.e., ${P{(\mathcal{E})}} \sim \mathcal{E}^{- 1}$, which only weakly depends on the network structure. Therefore the maximum energy required for control increases as $\mathcal{E}_{\max} \sim e^{N}$. This exponential increase means that steering the network in some directions is energetically prohibitive. Finally, if we drive a finite fraction of nodes ($1 < N_{D} < N$), the control spectrum has multiple peaks and the maximum energy required for control scales as $\mathcal{E}_{\max} \sim e^{N/N_{D}}$. Hence, as we increase the number of driver nodes, the maximum energy decays exponentially.

<!-- chunk {"id": "body-0165", "role": "body", "section": "II.10 Control Energy", "weight": 1.0} -->

These results raise an important question: in case of $1 < N_{D} < N$, how to choose the optimal set of $N_{D}$ driver nodes such that the control energy is minimized? Such a combinatorial optimization problem (also known as the actuator placement problem) has not been extensively studied in the literature. Only recently has it been shown that several objective functions, i.e. energy-related controllability metrics associated with the controllability Gramian $\mathbf{W}_{c}$ of LTI systems (e.g. ${{Tr}{(\mathbf{W}_{c}^{- 1})}},{\log{({\det\mathbf{W}_{c}})}},{{rank}{(\mathbf{W}_{c})}}$), are actually *submodular*.

<!-- chunk {"id": "body-0166", "role": "body", "section": "II.10 Control Energy", "weight": 1.0} -->

$f$ has the so-called diminishing returns property that the difference in the function value that a single element $x$ makes when added to an input set $\mathcal{X}$ decreases as the size of the input set increases. The submodularity of objective functions allows for either an efficient global optimization or a simple greedy approximation algorithm with certain performance guarantee to solve the combinatorial optimization problems. In particular, the submodularity of those energy-related controllability metrics has been explored to address the actuator placement problem in a model of the European power grid.

<!-- chunk {"id": "body-0167", "role": "body", "section": "II.11 Control Trajectories", "weight": 1.0} -->

So far we have focused on the minimization of driver/actuator nodes and the energy cost of controlling LTI systems. The characteristics of the resulting control trajectories are also interesting and worthy of exploration. A state $\mathbf{x}^{}$ of the LTI system is called *strictly locally controllable* (SLC) if for a ball $B{(\mathbf{x}^{},\varepsilon)}$ centered at $\mathbf{x}^{}$ with radius $\varepsilon > 0$ there is a constant $\delta > 0$ such that any final state $\mathbf{x}^{}$ inside the ball $B{(\mathbf{x}^{},\delta)}$ can be reached from $\mathbf{x}^{}$ with a control trajectory entirely inside the ball $B{(\mathbf{x}^{},\varepsilon)}$ (see Fig. 21a).

<!-- chunk {"id": "body-0168", "role": "body", "section": "II.11 Control Trajectories", "weight": 1.0} -->

Figure 21b shows that in a two-dimensional LTI system ${\overset{˙}{x}}_{1} = {x_{1} + {u_{1}{(t)}}}$, ${\overset{˙}{x}}_{2} = x_{1}$, for any state in the $x_{1} > 0$ half-plane, the minimal-energy control trajectories to any neighboring final state with a smaller $x_{2}$-component will necessarily cross into the $x_{1} < 0$ half-plane.

<!-- chunk {"id": "body-0169", "role": "body", "section": "II.11 Control Trajectories", "weight": 1.0} -->

It has been shown that for a general LTI system whenever the number of control inputs is smaller than the number of state variables (i.e., $N_{D} < N$), then almost all the states are not SLC. Therefore, the minimal-energy control trajectory is generally nonlocal and remains finite even when the final state is brought arbitrarily close to the initial state. The length $\int_{0}^{t_{f}}{{\|{\overset{˙}{\mathbf{x}}{(t)}}\|}{dt}}$ of such a trajectory generally increases with the condition number of the Gramian. Furthermore, the optimal control input that minimizes the energy cost $\int_{0}^{t_{f}}{{\|{\mathbf{u}{(t)}}\|}^{2}{dt}}$ will fail in practice if the controllability Gramian is ill conditioned. This can occur even when the controllability matrix is well conditioned.

<!-- chunk {"id": "body-0170", "role": "body", "section": "II.11 Control Trajectories", "weight": 1.0} -->

There is a sharp transition, called the controllability transition, as a function of the number of control inputs, below which numerical control always fails and above which it succeeds. These results indicate that even for the simplest LTI dynamics, the disparity between theory and practice poses a fundamental limit on our ability to control large networks.

<!-- chunk {"id": "body-0171", "role": "body", "section": "II.11 Control Trajectories", "weight": 1.0} -->

Indeed, we usually don't use the minimum-energy control input to steer the system to desired final states, simply because it is an open-loop (or non-feedback) controller ^44^4An *open-loop* control system does not use feedback. The control input to the system is determined using only the current state of the system and a model of the system, and is totally independent of the system's output. In contrast, in a *closed-loop* control system, the output has an effect on the input (through feedback) so that the input will adjust itself based on the output., which tends to be very sensitive to noise. A more practical and robust strategy is to use a simple linear feedback control to bring the system asymptotically towards a certain state, while minimizing the energy cost. This is a typical objective of optimal control theory, which aims to design control signals that will cause a process to satisfy some physical constraints and maximize (or minimize) a chosen performance criterion (or cost function).

<!-- chunk {"id": "body-0172", "role": "body", "section": "Controllability of Nonlinear Systems", "weight": 1.0} -->

So far we focused on the controllability of linear systems. Yet, the dynamics of most real complex systems is nonlinear, prompting us to review the classical results on nonlinear controllability and their applications to networked systems.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Controllability of Nonlinear Systems", "weight": 1.0} -->

Consider a control system of the form

<!-- chunk {"id": "body-0174", "role": "body", "section": "Controllability of Nonlinear Systems", "weight": 1.0} -->

where the state vector $\mathbf{x}$ is in a smooth connected manifold $\mathcal{M}$ of dimension $N$, and the control input $\mathbf{u} \in \mathcal{U}$ is a subset of ${\mathbb{R}}^{M}$. Note that has been frequently used to model the behavior of physical, biological and social systems. Roughly speaking, is *controllable* if one can steer it from any point $\mathbf{x}_{0} \in \mathcal{M}$ to any other point $\mathbf{x}_{1} \in \mathcal{M}$ by choosing $\mathbf{u}$ from a set of admissible controls $\mathbb{U}$, which is a subset of functions mapping ${\mathbb{R}}^{+}$ to $\mathcal{U}$.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Controllability of Nonlinear Systems", "weight": 1.0} -->

The controllability of nonlinear systems has been extensively studied since the early 1970s. The goal was to derive results of similar reach and generality as obtained for linear time-invariant systems. However, this goal turned out to be too ambitious, suggesting that a general theory on nonlinear controllability may not be feasible. Fortunately, as we discuss in this section, the concerted effort on nonlinear control has led to various weaker notions of nonlinear controllability, which are easier to characterize and often offer simple algebraic tests to explore the controllability of nonlinear systems.

<!-- chunk {"id": "body-0176", "role": "body", "section": "III.1 Accessibility and Controllability", "weight": 1.0} -->

As we will see in the coming sections, we can rarely prove or test controllability of an arbitrary nonlinear system. Instead, we prove and test weaker versions of controllability called local accessibility and local strong accessibility. We start by defining these notions.

<!-- chunk {"id": "body-0177", "role": "body", "section": "III.1 Accessibility and Controllability", "weight": 1.0} -->

Accessibility concerns the possibility to reach or access an open set of states in the state space from a given initial state. If the system is *locally accessible* from an initial state $\mathbf{x}_{0}$ then we can reach or access the neighborhood of $\mathbf{x}_{0}$ through trajectories that are within the neighborhood of $\mathbf{x}_{0}$. Mathematically, the system is called *locally accessible from* $\mathbf{x}_{0}$ if for any non-empty neighborhoods $\mathcal{V} \subset \mathcal{M}$ of $\mathbf{x}_{0}$ and any $t_{1} > 0$, the *reachable set* $\mathcal{R}^{\mathcal{V}}{(\mathbf{x}_{0}, \leq t_{1})}$ contains a non-empty open set. The system is called *locally accessible* if this holds for any $\mathbf{x}_{0}$.

<!-- chunk {"id": "body-0178", "role": "body", "section": "III.1 Accessibility and Controllability", "weight": 1.0} -->

Here, the reachable set $\mathcal{R}^{\mathcal{V}}{(\mathbf{x}_{0}, \leq t_{1})}$ includes all states that can be reached from $\mathbf{x}_{0}$ within a time $t_{1}$, following trajectories that are within the neighborhood of $\mathbf{x}_{0}$.

<!-- chunk {"id": "body-0179", "role": "body", "section": "III.1 Accessibility and Controllability", "weight": 1.0} -->

If we look at states that can be reached *exactly* at time $t_{1}$, then we have a stronger version of local accessibility. System is said to be *locally strongly accessible* from $\mathbf{x}_{0}$ if at any small time $t_{1} > 0$ the system can reach or access the neighborhood of $\mathbf{x}_{0}$ through trajectories that are within the neighborhood of $\mathbf{x}_{0}$. Mathematically, this means that for any non-empty neighborhoods $\mathcal{V}$ of $\mathbf{x}_{0}$ and any $t_{1} > 0$ sufficiently small, the reachable set $\mathcal{R}^{\mathcal{V}}{(\mathbf{x}_{0},t_{1})}$ contains a non-empty open set. If this holds for any $\mathbf{x}_{0}$, then the system is called *locally strongly accessible*.

<!-- chunk {"id": "body-0180", "role": "body", "section": "III.1 Accessibility and Controllability", "weight": 1.0} -->

Clearly, local strong accessibility from $\mathbf{x}_{0}$ implies local accessibility from $\mathbf{x}_{0}$. The converse is generally not true.

<!-- chunk {"id": "body-0181", "role": "body", "section": "III.1 Accessibility and Controllability", "weight": 1.0} -->

Local controllability asks whether the system is controllable in some neighborhood of a given state. Mathematically, the system is called *locally controllable* from $\mathbf{x}_{0}$ if for any neighborhood $\mathcal{V}$ of $\mathbf{x}_{0}$, the reachable set $\mathcal{R}^{\mathcal{V}}{(\mathbf{x}_{0}, \leq t_{1})}$ is also a neighborhood of $\mathbf{x}_{0}$ for any $t_{1}$ small enough. The system is called *locally controllable* if this holds for any $\mathbf{x}_{0}$. Clearly, local controllability implies local accessibility. It turns out that for a large class of systems local controllability implies local strong accessibility. But the converse is not always true.

<!-- chunk {"id": "body-0182", "role": "body", "section": "III.1 Accessibility and Controllability", "weight": 1.0} -->

If we do not require the trajectories of the system to remain close to the starting point, i.e., we allow excursions, then we have the notion of global controllability. System is *globally controllable* from $\mathbf{x}_{0}$ if the reachable set from $\mathbf{x}_{0}$ is $\mathcal{M}$ itself, i.e., ${\mathcal{R}{(\mathbf{x}_{0})}} \equiv {\cup_{t_{1} \geq 0}{\mathcal{R}^{\mathcal{M}}{(\mathbf{x}_{0},t_{1})}}} = \mathcal{M}$.

<!-- chunk {"id": "body-0183", "role": "body", "section": "III.1 Accessibility and Controllability", "weight": 1.0} -->

Complete algebraic characterizations of global controllability of nonlinear systems have proved elusive. Weaker notions of controllability are easier to characterize than controllability. For example, it can be proven that for some nonlinear systems, accessibility can be decided in polynomial time, while controllability is NP-hard. For complex networked systems we expect that only weaker notions of controllability can be characterized.

<!-- chunk {"id": "body-0184", "role": "body", "section": "III.2 Controllability of Linearized Control System", "weight": 1.0} -->

It is typically difficult to test the controllability of a nonlinear system. Yet, as we discuss next, studying the controllability properties of its linearization around an equilibrium point or along a trajectory can often offer an efficient test of local nonlinear controllability.

<!-- chunk {"id": "body-0185", "role": "body", "section": "III.2.1 Linearization around an equilibrium point", "weight": 1.0} -->

If the linearized control system is controllable (in the sense of a linear time-invariant system), then for any $\epsilon > 0$ the original nonlinear system is locally controllable from $\mathbf{x}^{\ast}$, where the control functions $\mathbf{u}{( \cdot )}$ are taken from the set ${\mathbb{U}}_{\epsilon}$.

<!-- chunk {"id": "body-0186", "role": "body", "section": "III.2.1 Linearization around an equilibrium point", "weight": 1.0} -->

In other words, many real systems operate near some equilibrium points and in the vicinity of such points, controllability can be decided using the tools developed for linear systems, discussed in the previous sections.

<!-- chunk {"id": "body-0187", "role": "body", "section": "III.2.2 Linearization around a trajectory", "weight": 1.0} -->

If the linearized control system along the trajectory ${(\overline{\mathbf{x}},\overline{\mathbf{u}})}:{{\lbrack T_{0},T_{1}\rbrack}\rightarrow\mathcal{O}}$ is controllable in the sense of a linear time-varying system, then the original nonlinear system is locally controllable along the trajectory. Once again, this means that we can use linear control theory to explore the controllability of nonlinear systems.

<!-- chunk {"id": "body-0188", "role": "body", "section": "III.2.3 Limitations of linearization", "weight": 1.0} -->

The linearization approaches described above may sound powerful, but they have severe limitations. First, they only provide information about controllability in the immediate vicinity of an equilibrium point or a trajectory. Second and most important, it may be the case that the linearized control system is not controllable, but the original nonlinear system is actually controllable.

<!-- chunk {"id": "body-0189", "role": "body", "section": "III.2.3 Limitations of linearization", "weight": 1.0} -->

Consider, for example, a model of a front-wheel drive car with four state variables: the positions ($x_{1},x_{2}$) of the center of the front axle, the orientation $\phi$ of the car, and the angle $\theta$ of the front wheels relative to the car orientation (Fig. 22). There are two control inputs $(u_{1},u_{2})$, where $u_{1}$, the steering velocity, represents the velocity with which the steering wheel is turning, and $u_{2}$ is the driving velocity. Assuming that the front and rear wheels do not slip and that the distance between them is $l = 1$, the car's equations of motion have the form

<!-- chunk {"id": "body-0190", "role": "body", "section": "III.2.3 Limitations of linearization", "weight": 1.0} -->

The linearization of around the origin is

<!-- chunk {"id": "body-0191", "role": "body", "section": "III.2.3 Limitations of linearization", "weight": 1.0} -->

which is uncontrollable, because $x_{2}$ and $\phi$ are time-invariant and not controlled by any of the system's inputs. Yet, from our driving experience we know that a car is controllable. We will prove that this system is indeed globally controllable in Sec. III.5.

<!-- chunk {"id": "body-0192", "role": "body", "section": "III.2.3 Limitations of linearization", "weight": 1.0} -->

System belongs to an especially interesting class of nonlinear systems, called control-affine systems, where $\mathbf{f}{(\mathbf{x},\mathbf{u})}$ is linear in the control signal $\mathbf{u}$

<!-- chunk {"id": "body-0193", "role": "body", "section": "III.2.3 Limitations of linearization", "weight": 1.0} -->

Here, $\mathbf{f}$ is called the *drift vector field*, or simply *drift*; and $\mathbf{g}_{1},\cdots,\mathbf{g}_{M}$ are called the *control vector fields*. The system is called *driftless* if ${\mathbf{f}{(\mathbf{x})}} \equiv \mathbf{0}$, which arises in kinematic models of many mechanical systems, e.g.,. Control-affine systems are natural generalization of linear time-invariant systems. Many nonlinear controllability results were obtained for them. Hereafter, we will focus on control-affine systems, referring the reader to for more general nonlinear systems.

<!-- chunk {"id": "body-0194", "role": "body", "section": "III.3 Basic concepts in differential geometry", "weight": 1.0} -->

Before we discuss the nonlinear tests for accessibility and controllability, we need a few concepts in differential geometry, like Lie brackets and distributions.

<!-- chunk {"id": "body-0195", "role": "body", "section": "III.3.1 Lie brackets", "weight": 1.0} -->

For nonlinear control systems, both controllability and accessibility are intimately tied to Lie brackets. The reason is simple. In the nonlinear framework, the directions in which the state may be moved around an initial state $\mathbf{x}_{0}$ are those belonging to the Lie algebra generated by vector fields $\mathbf{f}{(\mathbf{x}_{0},\mathbf{u})}$, when $\mathbf{u}$ varies in the set of admissible controls $\mathbb{U}$. Here the Lie algebra $\mathcal{A}$ generated by a family $\mathcal{F}$ of vector fields is the set of Lie brackets $\lbrack\mathbf{f},\mathbf{g}\rbrack$ with ${\mathbf{f},\mathbf{g}} \in \mathcal{F}$, and all vector fields that can be obtained by iteratively computing Lie brackets. In turn, a Lie bracket is the derivative of a vector field with respect to another.

<!-- chunk {"id": "body-0196", "role": "body", "section": "III.3.1 Lie brackets", "weight": 1.0} -->

Consider two vector fields $\mathbf{f}$ and $\mathbf{g}$ on an open set $D \subset {\mathbb{R}}^{N}$. The Lie bracket operation generates a new vector field $\lbrack\mathbf{f},\mathbf{g}\rbrack$, defined as

<!-- chunk {"id": "body-0197", "role": "body", "section": "III.3.1 Lie brackets", "weight": 1.0} -->

where $\frac{\partial\mathbf{g}}{\partial\mathbf{x}}$ and $\frac{\partial\mathbf{f}}{\partial\mathbf{x}}$ are the Jacobian matrices of $\mathbf{g}$ and $\mathbf{f}$, respectively. Higher order Lie brackets can be recursively defined as

<!-- chunk {"id": "body-0198", "role": "body", "section": "III.3.1 Lie brackets", "weight": 1.0} -->

To understand the physical meaning of the Lie bracket, consider the following piece-wise constant control inputs

<!-- chunk {"id": "body-0199", "role": "body", "section": "III.3.1 Lie brackets", "weight": 1.0} -->

applied onto a two-inputs control-affine system

<!-- chunk {"id": "body-0200", "role": "body", "section": "III.3.1 Lie brackets", "weight": 1.0} -->

with initial state ${\mathbf{x}{}} = \mathbf{x}_{0}$. The piece-wise constant control inputs can be considered as a sequence of "actions" applied for example to a car ($\mathbf{g}_{1}$, $\mathbf{g}_{2}$, reverse-$\mathbf{g}_{1}$, reverse-$\mathbf{g}_{2}$). In the limit $\tau\rightarrow 0$ the final state reached at $t = {4\tau}$ is

<!-- chunk {"id": "body-0201", "role": "body", "section": "III.3.1 Lie brackets", "weight": 1.0} -->

We see that up to terms of order $\tau^{2}$, the state change is exactly along the direction of the Lie bracket ${\lbrack\mathbf{g}_{1},\mathbf{g}_{2}\rbrack}{(\mathbf{x}_{0})}$ (see Fig. 23).

<!-- chunk {"id": "body-0202", "role": "body", "section": "III.3.1 Lie brackets", "weight": 1.0} -->

Consider two examples that demonstrate the meaning of Lie brackets. First, the Brockett system is one of the simplest driftless control-affine systems

<!-- chunk {"id": "body-0203", "role": "body", "section": "III.3.1 Lie brackets", "weight": 1.0} -->

Note that for the Brockett system we have ${{\lbrack\mathbf{g}_{1},{\lbrack\mathbf{g}_{1},\mathbf{g}_{2}\rbrack}\rbrack}{(\mathbf{x})}} = {{\lbrack\mathbf{g}_{2},{\lbrack\mathbf{g}_{1},\mathbf{g}_{2}\rbrack}\rbrack}{(\mathbf{x})}} = \mathbf{0}$. A similar three-dimensional Lie algebra, called the Heisenberg algebra, also arises in quantum mechanics. Hence the Brockett system is also known as the Heisenberg system. Note, however, that the commutation relations obeyed by the Heisenberg algebra do not always apply to general nonlinear systems.

<!-- chunk {"id": "body-0204", "role": "body", "section": "III.3.1 Lie brackets", "weight": 1.0} -->

To see this consider again the model of a front-wheel drive car, representing another two-input control-affine system, where the two control vector fields $\mathbf{g}_{1} = {}^{T}$ and $\mathbf{g}_{2} = {({\cos{({\theta + \phi})}},{\sin{({\theta + \phi})}},{\sin\theta},0)}^{T}$ can be interpreted as the actions $steer$ and $drive$, respectively. Some Lie brackets from $\mathbf{g}_{1}{(\mathbf{x})}$ and $\mathbf{g}_{2}{(\mathbf{x})}$ are

<!-- chunk {"id": "body-0205", "role": "body", "section": "III.3.1 Lie brackets", "weight": 1.0} -->

Equation can be interpreted as ${\lbrack{steer},{drive}\rbrack} = {wriggle}$, arising from the sequence of actions $({steer},{drive},{reversesteer},{reversedrive})$, which is what we do in order to get a car out of a tight parking space. Similarly, can be interpreted as ${\lbrack{wriggle},{drive}\rbrack} = {slide}$, arising from the sequence of actions $({wriggle},{drive},{reversewriggle},{reversedrive})$, which is what we do during parallel parking. Equations indicate that starting from only two control inputs: *steer* and *drive*, we can "generate" other actions, e.g., *wriggle* and *slide*, which allows us to fully control the car.

<!-- chunk {"id": "body-0206", "role": "body", "section": "III.3.1 Lie brackets", "weight": 1.0} -->

The above two examples demonstrate that by applying the right sequence of control inputs we can steer the system along a direction that the system does not have direct control over. In general, by choosing more elaborate sequences of control inputs we can steer a control-affine system in directions precisely captured by higher-order Lie brackets, e.g., $\lbrack\mathbf{g}_{2},{\lbrack\mathbf{g}_{1},\mathbf{g}_{2}\rbrack}\rbrack$, $\lbrack{\lbrack\mathbf{g}_{1},\mathbf{g}_{2}\rbrack},{\lbrack\mathbf{g}_{2},{\lbrack\mathbf{g}_{1},\mathbf{g}_{2}\rbrack}\rbrack}\rbrack$, etc. If the system of interest has a drift term $\mathbf{f}$, we also have to consider Lie brackets involving $\mathbf{f}$.

<!-- chunk {"id": "body-0207", "role": "body", "section": "III.3.1 Lie brackets", "weight": 1.0} -->

This is the reason why nonlinear controllability is closely related to the Lie brackets.

<!-- chunk {"id": "body-0208", "role": "body", "section": "III.3.2 Distributions", "weight": 1.0} -->

To discuss the nonlinear tests of accessibility and controllability, we need the notion of *distribution* in the sense of differential geometry. A distribution can be roughly considered as the nonlinear version of the controllability matrix of a linear system.

<!-- chunk {"id": "body-0209", "role": "body", "section": "III.3.2 Distributions", "weight": 1.0} -->

as the vector space spanned by the vectors ${\mathbf{g}_{1}{(\mathbf{x})}},{\mathbf{g}_{2}{(\mathbf{x})}},\cdots,{\mathbf{g}_{m}{(\mathbf{x})}}$ at any fixed $\mathbf{x} \in \mathcal{D}$. Essentially, we assign a vector space $\Delta{(\mathbf{x})}$ to each point $\mathbf{x}$ in the set $\mathcal{D}$. The collection of vector spaces $\Delta{(\mathbf{x})}$, $\mathbf{x} \in \mathcal{D}$ is called a *distribution* and referred to by

<!-- chunk {"id": "body-0210", "role": "body", "section": "III.4.1 Accessibility", "weight": 1.0} -->

Roughly speaking, accessibility concerns whether we can access all directions of the state space from any given state. The accessibility of control-affine systems can be checked using a simple algebraic test based on Lie brackets.

<!-- chunk {"id": "body-0211", "role": "body", "section": "III.4.1 Accessibility", "weight": 1.0} -->

For control-affine systems, we denote $\mathcal{C}$ as the linear combinations of recursive Lie brackets of the form

<!-- chunk {"id": "body-0212", "role": "body", "section": "III.4.1 Accessibility", "weight": 1.0} -->

where $\mathbf{X}_{i}$ is a vector field in the set $\{\mathbf{f},\mathbf{g}_{1},\cdots,\mathbf{g}_{M}\}$. As the linear space $\mathcal{C}$ is a Lie algebra, it is closed under the Lie bracket operation. In other words, ${\lbrack\mathbf{f},\mathbf{g}\rbrack} \in \mathcal{C}$ whenever $\mathbf{f}$ and $\mathbf{g}$ are in $\mathcal{C}$. Hence $\mathcal{C}$ is called as the *accessibility algebra*.

<!-- chunk {"id": "body-0213", "role": "body", "section": "III.4.1 Accessibility", "weight": 1.0} -->

Consider a control-affine system and a state $\mathbf{x}_{0} \in \mathcal{M} \subset {\mathbb{R}}^{N}$. If

<!-- chunk {"id": "body-0214", "role": "body", "section": "III.4.1 Accessibility", "weight": 1.0} -->

then the system is *locally accessible* from $\mathbf{x}_{0}$. Equation is often called the *accessibility rank condition* (ARC) at $\mathbf{x}_{0}$. If it holds for any $\mathbf{x}_{0}$, then the system is called locally accessible.

<!-- chunk {"id": "body-0215", "role": "body", "section": "III.4.1 Accessibility", "weight": 1.0} -->

Interestingly, the sufficient ARC is "almost" necessary for accessibility. Indeed, if the system is accessible then ARC holds for all $\mathbf{x}$ in an open and dense subset of ${\mathbb{R}}^{N}$.

<!-- chunk {"id": "body-0216", "role": "body", "section": "III.4.1 Accessibility", "weight": 1.0} -->

The computation of the accessibility distribution $C$ is nontrivial, because it is not known a priori how many (nested) Lie brackets of the vector fields need to be computed until the ARC holds. In practice, a systematic search must be performed by starting with $\{\mathbf{f},\mathbf{g}_{1},\cdots,\mathbf{g}_{M}\}$ and iteratively generating new, independent vector fields using Lie brackets. This can be achieved by constructing the Philip Hall basis of the Lie algebra, which essentially follows a breadth-first search and the search depth is defined to be the number of nested levels of bracket operations.

<!-- chunk {"id": "body-0217", "role": "body", "section": "III.4.1 Accessibility", "weight": 1.0} -->

In general, accessibility does not imply controllability, which is why accessibility is a weaker version of controllability. Consider a simple dynamical system

<!-- chunk {"id": "body-0218", "role": "body", "section": "III.4.1 Accessibility", "weight": 1.0} -->

where ${Im}{}$ stands for the image or column space of a matrix. Note that the term ${span}{\{{\mathbf{A}\mathbf{x}}_{0}\}}$ does not appear in Kalman's controllability matrix. Only at $\mathbf{x}_{0} = \mathbf{0}$, Eq. reduces to Kalman's controllability matrix. This shows that accessibility is indeed weaker than controllability, because the former does not imply the latter while the latter induces the former.

<!-- chunk {"id": "body-0219", "role": "body", "section": "III.4.2 Strong accessibility", "weight": 1.0} -->

A nonlinear test for strong accessibility tells us whether we can reach states in the neighborhood of the initial state exactly at a given small time. Define $\mathcal{C}_{0}$ as the *strong accessibility algebra*, i.e., the smallest algebra which contains $\mathbf{g}_{1},\mathbf{g}_{2},\cdots,\mathbf{g}_{M}$ and satisfies ${\lbrack\mathbf{f},\mathbf{w}\rbrack} \in \mathcal{C}_{0}$, ${\forall\mathbf{w}} \in \mathcal{C}_{0}$. Note that $\mathcal{C}_{0} \subset \mathcal{C}$ and $\mathcal{C}_{0}$ does not contain the drift vector field $\mathbf{f}$. Define the corresponding *strong accessibility distribution*

<!-- chunk {"id": "body-0220", "role": "body", "section": "III.4.2 Strong accessibility", "weight": 1.0} -->

If ${\dimC_{0}{(\mathbf{x}_{0})}} = N$ then the system is locally strongly accessible from $\mathbf{x}_{0}$. If this holds for any $\mathbf{x}_{0}$, then the system is called *locally strongly accessible*. If we compute the strong accessibility distribution $C$ for a linear system $(\mathbf{A},\mathbf{B})$, we will find that

<!-- chunk {"id": "body-0221", "role": "body", "section": "III.4.2 Strong accessibility", "weight": 1.0} -->

Then ${\dimC_{0}{(\mathbf{x}_{0})}} = N$ is equivalent with Kalman's rank condition. In other words, strong accessibility and controllability are equivalent notions for linear systems.

<!-- chunk {"id": "body-0222", "role": "body", "section": "III.5 Nonlinear Tests for Controllability", "weight": 1.0} -->

For general nonlinear systems, we lack conditions that are both sufficient and necessary for controllability. Yet, as we discuss next, we have some sufficient conditions that are believed to be almost necessary as well.

<!-- chunk {"id": "body-0223", "role": "body", "section": "III.5 Nonlinear Tests for Controllability", "weight": 1.0} -->

is identically equal to 1, regardless of $\mathbf{x}$, implying that ${\dimC{(\mathbf{x}_{0})}} = N = 4$ for all $\mathbf{x}_{0} \in {\mathbb{R}}^{4}$. Hence the front-wheel drive car systems is globally controllable, in line with our physical intuition and experience.

<!-- chunk {"id": "body-0224", "role": "body", "section": "III.5 Nonlinear Tests for Controllability", "weight": 1.0} -->

For control-affine systems that do not fall into the above two classes, Sussmann provided a general set of sufficient conditions. We call a Lie bracket computed from $\{\mathbf{f},\mathbf{g}_{1},\cdots,\mathbf{g}_{M}\}$ *bad* if it contains an odd number of $\mathbf{f}$ factors and an even number of each $\mathbf{g}_{k}$ factors. Otherwise we call it *good*. The degree of a bracket is the total number of vector fields from which it is compuated. Denote with $\sum_{M}$ the permutation group on $M$ symbols.

<!-- chunk {"id": "body-0225", "role": "body", "section": "III.6.1 Neuronal network motifs", "weight": 1.0} -->

While most complex systems are described by nonlinear *continuous-time* dynamics defined over a network, there has been little attention paid so far to the controllability of such systems, due to obvious mathematical challenges. Controllability studies of continuous-time nonlinear dynamics are still limited to very simple networks consisting of a few nodes, like neuronal network motifs governed by Fitzhugh-Nagumo dynamics. These offered an opportunity to study the impact of structural symmetries on nonlinear controllability. The three-node neuronal motifs shown in Fig. 24 can have multiple symmetries. Yet, not all symmetries have the same effect on network controllability. For example, with identical nodal and coupling parameters, Motif 1 has a full $\mathbf{S}_{3}$ symmetry, rendering the poorest controllability over the entire range of coupling strengths. Similarly, no controllability is obtained from node 2 in Motif 3, which has a reflection $\mathbf{S}_{2}$ symmetry across the plane through node 2. Surprisingly, the rotational $\mathbf{C}_{3}$ symmetry in Motif 7 does not cause loss of controllability at all.

<!-- chunk {"id": "body-0226", "role": "body", "section": "III.6.1 Neuronal network motifs", "weight": 1.0} -->

Note that symmetries have an impact on network controllability in linear systems as well. For example, in the case of a directed star with LTI dynamics for which we control the central hub (Fig. 4), a symmetry among the leaf nodes renders the system uncontrollable.

<!-- chunk {"id": "body-0227", "role": "body", "section": "III.6.1 Neuronal network motifs", "weight": 1.0} -->

Extending this analysis to larger networks with symmetries remains a challenge, however. Group representation theory might offer tools to gain insights into the impact of symmetries on the controllability of nonlinear networked systems. Note, however, that for large real networks such symmetries are less frequent.

<!-- chunk {"id": "body-0228", "role": "body", "section": "III.6.2 Boolean networks", "weight": 1.0} -->

The controllability of Boolean networks, a class of *discrete-time* nonlinear systems that are often used to model gene regulations, has been intensively studied. We can prove that finding a control strategy leading to the desired final state is NP-hard for a general Boolean network and this problem can be solved in polynomial time only if the network has a tree structure or contains at most one directed cycle. Interestingly, based on semi-tensor product of matrices and the matrix expression of Boolean logic, the Boolean dynamics can be exactly mapped into the standard discrete-time linear dynamics. Necessary and sufficient conditions to assure controllability of Boolean networks can then be proved. Despite the formally simplicity, the price we need to pay is that the size of the discrete-time linear dynamical system is $2^{N}$, where $N$ is the number of nodes in the original Boolean network. Hence, the controllability test will be computationally intractable for large Boolean networks.

<!-- chunk {"id": "body-0229", "role": "body", "section": "Observability", "weight": 1.0} -->

Before controlling a system, it is useful to know its position in the state-space, allowing us to decide in which direction we should steer it to accomplish the control objective. The position of a system in the state-space can be identified only if we can measure the state of all components separately, like the concentration of each metabolite in a cell, or the current on each transmission line of a power grid. Such detailed measurements are often infeasible and impractical. Instead, in practice we must rely on a subset of well-selected accessible variables (outputs) which can be used to observe the system, i.e. to estimate the state of the system. A system is said to be *observable* if it is possible to recover the state of the whole system from the measured variables inputs and outputs). This is a fundamental and primary issue in most complex systems.

<!-- chunk {"id": "body-0230", "role": "body", "section": "Observability", "weight": 1.0} -->

In general, we can observe a system because its components form a network, hence the state of the nodes depend on the state of their neighbors'. This offers the possibility to estimate all unmeasured variables from the measured ones. If the inputs and model of the system are known, observability can be equivalently defined as the possibility to recover the initial state $\mathbf{x}{}$ of the system from the output variables.

<!-- chunk {"id": "body-0231", "role": "body", "section": "Observability", "weight": 1.0} -->

To be specific, let us assume that we have no knowledge of a system's initial state $\mathbf{x}{}$, but we can monitor some of its outputs $\mathbf{y}{(t)}$ in some time interval. The observability problem aims to establish a relationship between the outputs $\mathbf{y}{(t)}$, the state vector $\mathbf{x}{(t)}$, and the inputs $\mathbf{u}{(t)}$ such that the system's initial state $\mathbf{x}{}$ can be inferred. If no such relation exists, the system's initial state cannot be estimated from the experimental measurements, i.e., the system is not observable. In other words, if the current value of at least one state variable cannot be determined through the outputs sensors, then it remains unknown to the controller. This may disable feedback control, which requires reliable real-time estimates of the system's state.

<!-- chunk {"id": "body-0232", "role": "body", "section": "Observability", "weight": 1.0} -->

Note that observability and controllability are mathematically dual concepts. Both concepts were first introduced by Rudolf Kalman for linear dynamical systems, and were extensively explored in nonlinear dynamical systems by many authors.

<!-- chunk {"id": "body-0233", "role": "body", "section": "Observability", "weight": 1.0} -->

In this section, we first discuss methods that test the observability of linear and nonlinear control systems. We also discuss the parameter identifiability problem, which is a special case of the observability problem. Finally, we introduce a graphical approach to identify the minimum set of sensor nodes that assure the observability of nonlinear systems and its application to metabolic networks.

<!-- chunk {"id": "body-0234", "role": "body", "section": "IV.1.1 Linear systems", "weight": 1.0} -->

For linear systems there is an exact duality between controllability and observability. To see this, consider an LTI control system

<!-- chunk {"id": "body-0235", "role": "body", "section": "IV.1.1 Linear systems", "weight": 1.0} -->

The duality principle states that an LTI system $(\mathbf{A},\mathbf{B},\mathbf{C})$ is observable if and only if its dual system $(\mathbf{A}^{T},\mathbf{C}^{T},\mathbf{B}^{T})$ is controllable. Mathematically, the duality can be seen and proved from the structure of the controllability Gramian and the observability Gramian. In terms of network language the duality principle has a straightforward interpretation: The linear observability of a network $\mathbf{A}$ can be addressed by studying the controllability of the transposed network $\mathbf{A}^{T}$, which is obtained by flipping the direction of each link in $\mathbf{A}$ (Fig. 25).

<!-- chunk {"id": "body-0236", "role": "body", "section": "IV.1.1 Linear systems", "weight": 1.0} -->

Thanks to the duality principle, many observability tests can be mapped into controllability tests. For example, according to Kalman's rank condition, the system $(\mathbf{A},\mathbf{B},\mathbf{C})$ is observable if and only if the *observability matrix*

<!-- chunk {"id": "body-0237", "role": "body", "section": "IV.1.1 Linear systems", "weight": 1.0} -->

has full rank, i.e., ${{rank}\mathbf{O}} = N$. This rank condition is based on the fact that if the $N$ rows of $\mathbf{O}$ are linearly independent, then each of the $N$ state variables can be determined by linear combinations of the output variables $\mathbf{y}{(t)}$.

<!-- chunk {"id": "body-0238", "role": "body", "section": "IV.1.2 Nonlinear systems", "weight": 1.0} -->

where $\mathbf{f}{( \cdot )}$ and $\mathbf{h}{( \cdot )}$ are some nonlinear functions.

<!-- chunk {"id": "body-0239", "role": "body", "section": "IV.1.2 Nonlinear systems", "weight": 1.0} -->

Mathematically, we can quantify observability from either an algebraic viewpoint or a differential geometric viewpoint. Here we focus on the former. If a system is *algebraically observable*, then there are algebraic relations between the state variables and the successive derivatives of the system's inputs and outputs. These algebraic relations guarantee that the system is observable and forbid symmetries. A family of symmetries is equivalent to infinitely many trajectories of the state variables that fit the same specified input-output behavior, in which case the system is not observable. If the number of such trajectories is finite, the system is called *locally observable*. If there is a unique trajectory, the system is *globally observable*.

<!-- chunk {"id": "body-0240", "role": "body", "section": "IV.1.2 Nonlinear systems", "weight": 1.0} -->

Consider, for example, the dynamical system defined by the equations

<!-- chunk {"id": "body-0241", "role": "body", "section": "IV.1.2 Nonlinear systems", "weight": 1.0} -->

The system has a family of symmetries $\sigma_{\lambda}$: $\{ x_{1},x_{2},x_{3},x_{4}\}$ $\rightarrow$ $\{ x_{1},{\lambdax_{2}},x_{3},{x_{4}/\lambda}\}$, so that the input $u$ and the output $y$ and all their derivatives are independent of $\lambda$. This means that we cannot distinguish whether the system is in state ${(x_{1},x_{2},x_{3},x_{4})}^{T}$ or its symmetric counterpart ${(x_{1},{\lambdax_{2}},x_{3},{x_{4}/\lambda})}^{T}$, because they are both consistent with the same input-output behavior. Hence we cannot uncover the system's internal state by monitoring $x_{1}$ only.

<!-- chunk {"id": "body-0242", "role": "body", "section": "IV.1.2 Nonlinear systems", "weight": 1.0} -->

The algebraic observability of a rational system is determined by the dimension of the space spanned by the gradients of the Lie-derivatives

<!-- chunk {"id": "body-0243", "role": "body", "section": "IV.1.2 Nonlinear systems", "weight": 1.0} -->

of its output functions $\mathbf{h}{(t,{\mathbf{x}{(t)}},{\mathbf{u}{(t)}})}$. The observability problem can be further reduced to the so-called rank test: the system is *algebraically observable* if and only if the ${NM} \times N$ Jacobian matrix

<!-- chunk {"id": "body-0244", "role": "body", "section": "IV.1.2 Nonlinear systems", "weight": 1.0} -->

Note that for an LTI system (73a,73b), the Jacobian matrix reduces to the observability matrix.

<!-- chunk {"id": "body-0245", "role": "body", "section": "IV.1.2 Nonlinear systems", "weight": 1.0} -->

For rational dynamic systems, the algebraic observability test can be performed using an algorithm developed by Sedoglavic. The algorithm offers a generic rank computation of the Jacobian matrix using the techniques of symbolic calculation, allowing us to test local algebraic observability for rational systems in polynomial time. This algorithm certifies that a system is locally observable, but its answer for a non-observable system is probabilistic with high probability of success. A system that is found non-observable can be further analyzed to identify a family of symmetries, which can confirm the system is truly non-observable.

<!-- chunk {"id": "body-0246", "role": "body", "section": "IV.2 Minimum sensor problem", "weight": 1.0} -->

In complex systems, the state variables are rarely independent of each other. The interactions between the system's components induce intricate interdependencies among them.

<!-- chunk {"id": "body-0247", "role": "body", "section": "IV.2 Minimum sensor problem", "weight": 1.0} -->

Hence a well-selected subset of state variables can contain sufficient information about the remaining variables to reconstruct the system's complete internal state, making the system observable.

<!-- chunk {"id": "body-0248", "role": "body", "section": "IV.2 Minimum sensor problem", "weight": 1.0} -->

We assume that we can monitor a selected subset of state variables, i.e. ${\mathbf{y}{(t)}} = {(\cdots,{x_{i}{(t)}},\cdots)}^{T}$, corresponding to the states of several nodes that we call *sensor nodes* or just *sensors*. Network observability can then be posed as follows: Identify the minimum set of sensors from whose measurement we can infer all other state variables. For linear systems, this problem can be solved using the duality principle and solving the minimum input problem of the transposed network $\mathbf{A}^{T}$. For general nonlinear systems this trick does not work. While offers a formal answer to the observability issue and can be applied to small engineered systems, it has notable practical limitations for large and complex systems. First, it can only confirm if a specific set of sensors can be used to observe a system or not, without telling us how to identify them.

<!-- chunk {"id": "body-0249", "role": "body", "section": "IV.2 Minimum sensor problem", "weight": 1.0} -->

Therefore, a brute-force search for a minimum sensor set requires us to inspect via about $2^{N}$ sensor combinations, a computationally prohibitive task for large systems. Second, the rank test of the Jacobian matrix via symbolic computation is computationally limited to small systems. Hence, the fundamental question of identifying the minimum set of sensors through which we can observe a large complex system remains an outstanding challenge.

<!-- chunk {"id": "body-0250", "role": "body", "section": "IV.2 Minimum sensor problem", "weight": 1.0} -->

To resolve these limitations, we can exploit the dynamic interdependence of the system's components through a graphical representation.

<!-- chunk {"id": "body-0251", "role": "body", "section": "IV.2 Minimum sensor problem", "weight": 1.0} -->

\(i\) *Inference diagram:* Draw a directed link $x_{i}\rightarrow x_{j}$ if $x_{j}$ appears in $x_{i}$'s differential equation (i.e., if $\frac{\partial f_{i}}{\partial x_{j}}$ is not identically zero), implying that one can retrieve some information on $x_{j}$ by monitoring $x_{i}$ as a function of time. Since the constructed network captures the information flow to infer the state of individual variables, we call it the *inference diagram* (Fig. 26c).

<!-- chunk {"id": "body-0252", "role": "body", "section": "IV.2 Minimum sensor problem", "weight": 1.0} -->

\(ii\) *Strongly connected component (SCC) decomposition:* Decompose the inference diagram into a unique set of maximal SCCs (dashed circles in Fig. 26c), i.e. the largest subgraphs chosen such that in each of them there is a directed path from every node to every other node. Consequently, each node in an SCC contains some information about all other nodes within the SCC.

<!-- chunk {"id": "body-0253", "role": "body", "section": "IV.2 Minimum sensor problem", "weight": 1.0} -->

\(iii\) *Sensor node selection:* Those SCCs that have no incoming edges are referred to as *root SCCs* (shaded circles in Fig. 26c). We must choose at least one node from each root SCC to ensure the observability of the whole system. For example, the inference diagram of Fig. 26c contains three root SCCs; hence we need at least three sensors to observe the system.

<!-- chunk {"id": "body-0254", "role": "body", "section": "IV.2 Minimum sensor problem", "weight": 1.0} -->

The graphical approach (GA) described above can be used to determine whether a variable provides full observability of small dynamic systems. As these systems have only a few state variables, steps (ii) and (iii) are often not necessary. For large networked systems, the GA is very powerful because it reduces the observability issue, a dynamical problem of a nonlinear system with many unknowns, to a property of the static graph of the inference diagram, which can be accurately mapped for an increasing number of complex systems, from biochemical reactions to ecological systems.

<!-- chunk {"id": "body-0255", "role": "body", "section": "IV.2 Minimum sensor problem", "weight": 1.0} -->

We can prove that monitoring the root SCCs identified by the GA are *necessary* for observing any nonlinear dynamic system. In other words, the number of root SCCs yields a strict lower bound for the size of the minimum sensor set. Consequently, any state observer (i.e. a dynamical device that aims to estimate the system's internal state) will fail if it doesn't monitor these sensors.

<!-- chunk {"id": "body-0256", "role": "body", "section": "IV.2 Minimum sensor problem", "weight": 1.0} -->

If the dynamics is linear, the duality principle maps the minimum sensor problem into the minimum input problem and predicts not only the necessary, but also the sufficient sensor set for observability. Numerical simulations on model networks suggest that for linear systems the sufficient sensor set is noticeably larger than the necessary sensor set predicted by GA. This is because that any symmetries in the state variables leaving the inputs, outputs, and all their derivatives invariant will make the system unobservable. For structured linear systems, the symmetries correspond to a particular topological feature, i.e., dilations, which can be detected from the inference diagram. Yet, for general nonlinear systems, the symmetries can not be easily detected from the inference diagram only.

<!-- chunk {"id": "body-0257", "role": "body", "section": "IV.2 Minimum sensor problem", "weight": 1.0} -->

For linear systems the minimum sensor set predicted by the GA is generally not sufficient for full observability. Yet, for large nonlinear dynamical systems the symmetries in state variables are extremely rare, especially when the number of state variables is big, hence the sensor set predicted by GA is often not only necessary but also sufficient for observability.

<!-- chunk {"id": "body-0258", "role": "body", "section": "IV.2 Minimum sensor problem", "weight": 1.0} -->

To better understand network observability, next we apply the developed tools to biochemical and technological networks.

<!-- chunk {"id": "body-0259", "role": "body", "section": "IV.2.1 Biochemical reaction systems", "weight": 1.0} -->

where $\alpha_{ji} \geq 0$ and $\beta_{ji} \geq 0$ are the stoichiometry coefficients. For example, captures the reaction 2 H~2~ + O~2~ = 2 H~2~O with $\alpha_{11} = 2$, $\alpha_{12} = 1$ and $\beta_{11} = 2$.

<!-- chunk {"id": "body-0260", "role": "body", "section": "IV.2.1 Biochemical reaction systems", "weight": 1.0} -->

Under the continuum hypothesis and the well-mixed assumption the system's dynamics is described, where $x_{i}{(t)}$ is the concentration of species $\mathcal{S}_{i}$ at time $t$, the input vector $\mathbf{u}{(t)}$ represents regulatory signals or external nutrient concentrations, and the vector $\mathbf{y}{(t)}$ captures the set of experimentally measurable species concentrations or reaction fluxes. The vector ${\mathbf{v}{(\mathbf{x})}} = {({v_{1}{(\mathbf{x})}},{v_{2}{(\mathbf{x})}},\cdots,{v_{R}{(\mathbf{x})}})}^{T}$ is often called the flux vector, which follows the mass-action kinetics

<!-- chunk {"id": "body-0261", "role": "body", "section": "IV.2.1 Biochemical reaction systems", "weight": 1.0} -->

with rate constants $k_{j} > 0$. The system's dynamics is therefore described by the balance equations

<!-- chunk {"id": "body-0262", "role": "body", "section": "IV.2.1 Biochemical reaction systems", "weight": 1.0} -->

where $\Gamma_{ij} = {\beta_{ji} - \alpha_{ji}}$ are the elements of the $N \times R$ stoichiometric matrix $\mathbf{\Gamma}$. The RHS of represents a sum of all fluxes $v_{j}$ that produce and consume the species $\mathcal{S}_{i}$.

<!-- chunk {"id": "body-0263", "role": "body", "section": "IV.2.1 Biochemical reaction systems", "weight": 1.0} -->

Assuming that the outputs $\mathbf{y}{(t)}$ are just the concentrations of a particular set of sensor species that can be experimentally measured, then observability problem aims to identify *a minimum set of sensor species from whose measured concentrations we can determine all other species' concentrations*. In this context, the advantage of GA is that it does not require the system's kinetic constants (which are largely unknown *in vivo*), relying only on the topology of the inference diagram. For a metabolic network or an arbitrary biochemical reaction system, the topology of the inference diagram is uniquely determined by the full reaction list, which is relatively accurately known for several model organisms.

<!-- chunk {"id": "body-0264", "role": "body", "section": "IV.2.1 Biochemical reaction systems", "weight": 1.0} -->

a\) Species that are not reactants in any reaction, being instead *pure products*, will be root SCCs of size one. Consequently, they are always sensors, and must be observed by the external observer (e.g., $x_{6}$ in Fig. 26c).

<!-- chunk {"id": "body-0265", "role": "body", "section": "IV.2.1 Biochemical reaction systems", "weight": 1.0} -->

b\) For root SCCs of size larger than one (e.g. $\{ x_{4},x_{5}\}$ and $\{ x_{7},x_{8},x_{9}\}$ in Fig. 26c), *any* node could be chosen as a sensor. Given that some root SCCs are quite large, and typically we only need to monitor one node for each root SCC, the number of sensor nodes is thus considerably reduced.

<!-- chunk {"id": "body-0266", "role": "body", "section": "IV.2.1 Biochemical reaction systems", "weight": 1.0} -->

c\) A minimum set of sensors consists of all pure products and one node from each root SCC of size larger than one (e.g. $\{ x_{5},x_{6},x_{7}\}$ in Fig. 26c).

<!-- chunk {"id": "body-0267", "role": "body", "section": "IV.2.1 Biochemical reaction systems", "weight": 1.0} -->

d\) Since any node in a root SCC can be selected as a sensor node, there are $\Omega_{s} = {\prod_{i = 1}^{N_{{root} - {SCC}}}n_{i}}$ equivalent sensor node combinations, representing the product of all root SCCs' sizes. For example, in Fig. 26c we have three root SCCs with sizes $n_{i} = {1,2,3}$, hence $\Omega_{s} = {1 \times 2 \times 3} = 6$. This multiplicity offers significant flexibility in selecting experimentally accessible sensors.

<!-- chunk {"id": "body-0268", "role": "body", "section": "IV.2.1 Biochemical reaction systems", "weight": 1.0} -->

It turns out that the minimum set of sensors obtained by GA almost always achieve full observability for the whole system, except in some pathological cases. The sufficiency of the sensors predicted by GA is unexpected because substantial details about the system's dynamics are ignored in GA, hence offering an exact proof that the *sufficiency* of the predicted sensors for observability is a difficult, if not an impossible, task. Note, however, that the rigorous proof of sufficiency and the systematic search for exceptional cases making a system unobservable remain open questions.

<!-- chunk {"id": "body-0269", "role": "body", "section": "IV.2.2 Power grid", "weight": 1.0} -->

In the power grid, the state variables represent the voltage of all nodes, which in practice can be determined by phasor measurement units (PMUs). Since a PMU can measure the real time voltage and line currents of the corresponding node, a PMU placed on a node $i$ will determine the state variables of both node $i$ and all of its first nearest neighbors. In this case the observability problem can be mapped to a purely graph theoretical problem. The random placement of PMUs leads to a network observability transition, which is a new type of percolation transition that characterizes the emergence of macroscopic observable components in the network as the number of randomly placed PMUs increases (Fig. 27). Using the generating function formalism, we can analytically calculate the expected size of the largest observable component for networks with any prescribed degree distribution. This has been demonstrated for real power grids. Moreover, it has been found that the percolation threshold decreases with the increasing average degree or degree heterogeneity.

<!-- chunk {"id": "body-0270", "role": "body", "section": "IV.2.2 Power grid", "weight": 1.0} -->

The random placement of PMUs apparently will not solve the minimum sensor problem. For a power grid, the problem of identifying the minimum set of sensor nodes is reduced to the minimum dominating set (MDS) problem: Identify a minimum node set $D \subseteq V$ for a graph $G = {(V,E)}$ such that every node not in $D$ is adjacent to at least one node in $D$ (Fig. 28a,b). Consider a undirected network $G$. Node $i$ is either empty (with occupation state $c_{i} = 0$) or occupied by sensors (with $c_{i} = 1$). In other words, if $c_{i} = 1$ then node $i$ can be considered a sensor node. Node $i$ is called observed if it is a sensor node itself or it is not a sensor node but adjacent to one or more sensor nodes. Otherwise node $i$ is unobserved. The MDS problem requires us to occupy a minimum set $D$ of nodes so that all $N$ nodes of $G$ are observed.

<!-- chunk {"id": "body-0271", "role": "body", "section": "IV.2.2 Power grid", "weight": 1.0} -->

^55^5Interestingly, the MDS problem can also be formalized as a control problem on a undirected network by assuming that every edge in a network is bi-directional and every node in the MDS can control all of its outgoing links separately. This formulation has recently been applied to analyze biological networks.

<!-- chunk {"id": "body-0272", "role": "body", "section": "IV.2.2 Power grid", "weight": 1.0} -->

The MDS problem for a general graph is NP-hard, and the best polynomial algorithms can only offer dominating sets with sizes not exceeding $\log N$ times of the minimum size of the dominating sets. If the underlying network has no core, we can solve exactly the MDS problem in polynomial time using a generalized leaf-removal (GLR) process (Fig. 28c,d). The GLR process can be recursively applied to simplify the network $G$. If eventually all the nodes are removed, then the set of nodes occupied during this process must be an MDS and choosing them as sensor nodes will make the whole network observable. If, however, the final simplified network is non-empty, then there must be some nodes that are still unobserved after the GLR process. The subnetwork induced by these unobserved nodes is referred to as the *core* of the original network $G$. For networks with an extensive core, a belief-propagation algorithm, rooted in spin glass theory, can offer nearly optimal solutions, which also performs well on real-world networks. Recently, probabilistic methods have been developed to approximate the size of the MDS in scale-free networks.

<!-- chunk {"id": "body-0273", "role": "body", "section": "IV.3 Target observability", "weight": 1.0} -->

In many applications it is overkill to observe the full system, but it is sufficient to infer the state of a subset of *target variables*. Such target variables could for example correspond to the concentrations of metabolites whose activities are altered by a disease, representing potential biomarkers. In case those target variables cannot be directly measured, we can invoke *target observability*, and aim to identify the optimal sensor(s) that can infer the state of the target variables. These could represent the optimal experimentally accessible biomarkers for a disease. The graphical approach discussed above helps us select such optimal sensors: a) The state of a target node $x_{t}$ can be observed from a sensor node $x_{s}$ only if there is a directed path from $x_{s}$ to $x_{t}$ in the inference diagram. For example, in Fig. 26c, $x_{4}$ can only be inferred from $x_{5}$ while $x_{1}$ can be inferred from any other nodes.

<!-- chunk {"id": "body-0274", "role": "body", "section": "IV.3 Target observability", "weight": 1.0} -->

b) There are important differences in the complexity of the inference process, which depends on the size of the subsystem we need to infer for a given sensor choice. The SCC decomposition of the inference diagram indicates that to observe $x_{t}$ from $x_{s}$, we need to reconstruct $\mathcal{N}_{s} = {\sum_{n_{i} \subset \mathcal{S}_{s}}n_{i}}$ metabolite concentrations, where $\mathcal{S}_{s}$ denotes the set of all SCCs that are reachable from $x_{s}$, and $n_{i}$ is the size of the $i$-th SCC. This formula can be extended to multiple targets. c) To identify the optimal sensor node for any target node, we can minimize $\sum_{n_{i} \subset \mathcal{S}_{s}}n_{i}$, which is the minimum amount of information required for the inference process.

<!-- chunk {"id": "body-0275", "role": "body", "section": "IV.3 Target observability", "weight": 1.0} -->

For example, if $x_{t}$ is inside an SCC of size larger than one (e.g., $x_{1}$ in Fig. 26c), then the optimal sensor can be any other node in the same SCC (e.g., $x_{2}$ or $x_{3}$ in Fig. 26c). If all other nodes in the same SCC is experimentally inaccessible, then the optimal sensor node belongs to the smallest SCC that points to $x_{i}$ (e.g., $x_{6}$ in Fig. 26c). Note that this minimization procedure can be implemented for any inference diagram in polynomial time. Hence the graphical approach can aid the efficient selection of optimal sensors for any targeted node, offering a potentially indispensable tool for biomarker design.

<!-- chunk {"id": "body-0276", "role": "body", "section": "IV.4 Observer Design", "weight": 1.0} -->

The observability test and the graphical approach mentioned above do not tell us how to reconstruct the state of the system from measurements. To achieve this we must design an *observer*, a dynamic device that runs a replica of the real system, adjusting its state from the available outputs to uncover the missing variables.

<!-- chunk {"id": "body-0277", "role": "body", "section": "IV.4 Observer Design", "weight": 1.0} -->

For an LTI system (73a, 73b), we can easily design the so-called *Luenberger observer*

<!-- chunk {"id": "body-0278", "role": "body", "section": "IV.4 Observer Design", "weight": 1.0} -->

where the $N \times K$ matrix $\mathbf{L}$ is to be specified later. Note that with initial condition ${\mathbf{z}{}} = {\mathbf{x}{}}$, the Luenberger observer will follow ${\mathbf{z}{(t)}} = {\mathbf{x}{(t)}}$ exactly for all $t > 0$. Because $\mathbf{x}{}$ is typically unaccessible, we start from ${\mathbf{z}{}} \neq {\mathbf{x}{}}$ and hope that $\mathbf{z}{(t)}$ will asymptotically converge to $\mathbf{x}{(t)}$, i.e. the state of the observer tracks the state of the original system.

<!-- chunk {"id": "body-0279", "role": "body", "section": "IV.4 Observer Design", "weight": 1.0} -->

For nonlinear systems the observer design is rather involved and still an open challenge.

<!-- chunk {"id": "body-0280", "role": "body", "section": "IV.4.1 Parameter Identification", "weight": 1.0} -->

Most modeling efforts assume that the system parameters, like the rate constants of biochemical reactions, are known. Yet, for most complex systems, especially in biological context, the system parameters are usually unknown or are only known approximately. Furthermore, the known parameters are typically estimated in vitro, and their in vivo relevance is often questionable. This raises a natural question: Can we determine the model parameters through appropriate input/output measurements, like monitoring the concentrations of properly selected chemical species? This problem is called *parameter identification* (PI) in control theory.

<!-- chunk {"id": "body-0281", "role": "body", "section": "IV.4.1 Parameter Identification", "weight": 1.0} -->

We can formalize the parameter identifiability problem as the observability problem of an extended system as follows. For this we consider the system parameters $\Theta$ as special state variables with time-derivative zero (${{{d\Theta}/d}t} = 0$). We can extend the state vector to include a larger set of state variables, i.e., $({\mathbf{x}{(t)}},\Theta)$, allowing us to formally determine whether/how the system parameters can be identified from the input-output behavior by checking the observability of the extended system. Consequently, PI can be considered as a special observer design problem.

<!-- chunk {"id": "body-0282", "role": "body", "section": "IV.4.2 Network Reconstruction", "weight": 1.0} -->

When the system parameters contain information about the network structure, the corresponding PI problem can be generalized to a network reconstruction (NR) problem. Consider a network whoe state variables are governed by a set of ODEs

<!-- chunk {"id": "body-0283", "role": "body", "section": "IV.4.2 Network Reconstruction", "weight": 1.0} -->

There are three principally different NR approaches, which assume various levels of a priori knowledge about the system Timme and Casadiego.

<!-- chunk {"id": "body-0284", "role": "body", "section": "IV.4.2 Network Reconstruction", "weight": 1.0} -->

*Driving-response*. Here we try to measure and evaluate the collective response of a networked system to external perturbations or driving. As the response depends on both the external driving signal (which unit is perturbed, when and how strong is the perturbation, etc.), and the (unknown) structural connectivity of the network, sufficiently many driving-response experiments should reveal the entire network. This approach is relatively simple to implement and the required computational effort scales well with the system size. It has been well established for the reconstruction of gene regulatory networks Gardner *et al.*; Tegner *et al.*; Yu and Parlitz; Yu. Yet, this approach requires us to measure and drive the dynamics of all units in the system, which is often infeasible. The collective dynamics suitable for the driving-response experiments also needs to be simple (i.e., to exhibit a stable fixed point or periodic orbits, or to allow the system to be steered into such a state). For systems exhibiting more complex features, e.g. chaos, bifurcations, multi-stability, this approach is not applicable.

<!-- chunk {"id": "body-0285", "role": "body", "section": "IV.4.2 Network Reconstruction", "weight": 1.0} -->

If the system exhibits the same fixed point for different constant inputs (as some biological systems that have "perfect adaptation"), it is impossible to reconstruct the network using driving-response experiments Prabakaran *et al.*.

<!-- chunk {"id": "body-0286", "role": "body", "section": "IV.4.2 Network Reconstruction", "weight": 1.0} -->

*Copy-synchronization*: This approach sets up a copy of the original system and updates its interaction matrix continuously until the copy system synchronizes its trajectories with the original system Yu *et al.*. We expect the final interaction matrix of the copy system to converge to that of the original system. Unfortunately, sufficient conditions for the convergence of this approach have not been fully understood and the approach is model dependent. Knowing the details of the coupling functions $f_{ij}{(x_{i},x_{j})}$ is crucial to set up the copy system. Furthermore, $f_{ij}{(x_{i},x_{j})}$ needs to be Lipschitz continuous. These constraints significantly narrow the applicability of this approach.

<!-- chunk {"id": "body-0287", "role": "body", "section": "IV.4.2 Network Reconstruction", "weight": 1.0} -->

*Direct approach*: This approach relies on the evaluation of temporal derivatives from time series data Shandilya and Timme. Exploiting smoothness assumptions, it finds the unknown interaction matrix by solving an optimization problem (e.g., $\ell_{1}$ or $\ell_{2}$-norm minimization). The rationale is as follows. If the time derivatives of the state variables are evaluated, and if the system coupling functions are also known, then the only remaining unknown parameters are the edge weights or interaction strengths $a_{ij}$'s. Repeated evaluations of at different sufficiently closely spaced times $t_{m} \in {\mathbb{R}}$ comprise a simple and implicit restriction on the interaction matrix $A$. This approach serves as a simple starting strategy of NR. Yet, it has an fundamental drawback --- there is no reason why the true interaction matrix should be optimal in some a priori metric. Moreover, it may suffer from the poor evaluation of time derivatives of noisy time series data.

<!-- chunk {"id": "body-0288", "role": "body", "section": "IV.4.2 Network Reconstruction", "weight": 1.0} -->

All three approaches suffer from one common issue: The necessary and sufficient conditions under which they succeed are unknown. An important exception is the *Modular Response Analysis* method Kholodenko *et al.*; Sontag, which is a special driving-response approach, and guarantees to recover the interaction matrix using steady-state data collected from sufficiently many perturbation experiments. One drawback of this method is that it assumes the system is not *retroactive* Sontag. Here, retroactivity manifests as "load" or "impedance" effects that might be hard to anticipate if we have no a-priori knowledge of the system dynamics.

<!-- chunk {"id": "body-0289", "role": "body", "section": "IV.4.2 Network Reconstruction", "weight": 1.0} -->

Recently, two classes of fundamental limitations of NR were characterized by deriving necessary (and in some cases sufficient) conditions to reconstruct any desired property of the interaction matrix. The first class of fundamental limitations is due to our uncertainty about the coupling functions $f_{ij}{(x_{i},x_{j})}$, leading to a natural trade-off: the more information we want to reconstruct about the interaction matrix the more certain we need to be about the coupling functions. For example, it is possible to reconstruct the adjacency pattern $\mathbf{K}$ without knowing exactly the coupling functions. But, in order to reconstruct the interaction matrix $\mathbf{A}$ itself, it is necessary to know these functions exactly. In this sense, if we are uncertain about the coupling functions, NR is easier than PI.

<!-- chunk {"id": "body-0290", "role": "body", "section": "IV.4.2 Network Reconstruction", "weight": 1.0} -->

The second class of fundamental limitations originates solely from uninformative temporal data, i.e. ${\{{x_{i}{(t)}},{u_{i}{(t)}}\}}_{i = 1}^{N}$, ${\forall t} \in {\lbrack t_{0},t_{1}\rbrack}$. This leads to a rather counterintuitive result: regardless of how much information we aim to reconstruct (e.g. edge weights, sign pattern or connectivity pattern), the measured temporal data needs to be equally informative. This happens even if we know the coupling functions exactly. Hence, in the sense of informativeness of the measured data, reconstructing any property of the interaction matrix is as difficult as reconstructing the interaction matrix itself, i.e. NR is as difficult as PI.

<!-- chunk {"id": "body-0291", "role": "body", "section": "IV.4.2 Network Reconstruction", "weight": 1.0} -->

A practical solution to circumvent this limitation without acquiring more temporal data (i.e. performing more experiments, which are sometime either infeasible to too expensive), prior knowledge of the interaction matrix, e.g. the bounds of the edge weights, is extremely useful.

<!-- chunk {"id": "body-0292", "role": "body", "section": "Towards Desired Final States or Trajectories", "weight": 1.0} -->

A significant body of work in control theory deals with the design of control inputs that can move the system from a given initial state to a desired final state in the state space. For linear dynamics, Equation provides the optimal input signal to take an arbitrary linear system into an arbitrary final state using the minimum control energy $\int_{0}^{T}{{\|{\mathbf{u}{(t)}}\|}^{2}{dt}}$. For nonlinear dynamics we lack a ready-to-use solution, and finding one can be very difficult. Yet, solving such nonlinear control problems has important applications from robotics to ecosystem management, and from cell reprogramming to drug discovery. For example, in robotics engineers frequently encounter the so-called motion- or path-planning problem, needing to decompose a desired movement into discrete motions that satisfy specific movement constraints and possibly optimize some aspect of the trajectory. The parallel parking problem is a typical example, requiring us to determine the sequence of motions a car must follow in order to parallel park into a parking space.

<!-- chunk {"id": "body-0293", "role": "body", "section": "Towards Desired Final States or Trajectories", "weight": 1.0} -->

In many cases, we are interested in steering the system towards a desired trajectory or attractor, instead of a desired final state. A trajectory or an orbit of a dynamical system is a collection of points (states) in the state space. For example, a *periodic orbit* repeats itself in time with period $T$, so that ${\mathbf{x}{(t)}} = {\mathbf{x}{({t + {nT}})}}$ for any integer $n \geq 1$. Roughly speaking, an attractor is a closed subset $\mathcal{A}$ of a dynamical system's state space such that for "many" choices of initial states the system will evolve towards states in $\mathcal{A}$. Simple attractors correspond to fundamental geometric objects, like points, lines, surfaces, spheres, toroids, manifolds, or their simple combinations. Fixed (or equilibrium) point and limit cycle are common simple attractors.

<!-- chunk {"id": "body-0294", "role": "body", "section": "Towards Desired Final States or Trajectories", "weight": 1.0} -->

Fixed points are defined for mappings $x_{n + 1} = {f{(x_{n})}}$, where $x$ is a fixed point if $x = {f{(x)}}$, whereas equilibrium points or equilibria are defined for flows (ODEs) $\overset{˙}{\mathbf{x}} = {\mathbf{f}{(\mathbf{x})}}$, where $\mathbf{x}$ is an equilibrium point if ${\mathbf{f}{(\mathbf{x})}} = 0$. A limit cycle is a periodic orbit of the dynamic system that is isolated. An attractor is called *strange* if it has a fractal structure that cannot be easily described as fundamental geometric objects or their simple combinations. A strange attractor often emerges in chaotic dynamics.

<!-- chunk {"id": "body-0295", "role": "body", "section": "Towards Desired Final States or Trajectories", "weight": 1.0} -->

In this section we briefly review progress made in several directions with the common goal of controlling some dynamical systems: (a) Control of chaos, which requires us to transform a chaotic motion into a periodic trajectory using open-loop control, Poincaré map linearization or time-delayed feedback. (b) Systematic design of compensatory perturbations of state variables that take advantage of the full basin of attraction of the desired final state. (c) Construction of the attractor network; (d) Mapping the control problem into a combinatorial optimization problem on the underlying networks.

<!-- chunk {"id": "body-0296", "role": "body", "section": "Controlling Chaos", "weight": 1.0} -->

A deterministic dynamical system is said to be *chaotic* if its evolution is highly sensitive to its initial conditions. This sensitivity means that arbitrary small measurement errors in the initial conditions grow exponentially with time, destroying the long-term predictability of the system's future state. This phenomenon, known as the *butterfly effect*, is often considered troublesome. Chaotic behavior commonly emerges in natural and engineered systems, being encountered in chemistry, nonlinear optics, electronics, fluid dynamics, meteorology, and biology.

<!-- chunk {"id": "body-0297", "role": "body", "section": "Controlling Chaos", "weight": 1.0} -->

It has been realized that well-designed control laws can overcome the butterfly effect, forcing chaotic systems to follow some desired behavior. Next, we review several key methods devised for the control of chaotic systems from the control theoretical perspective.

<!-- chunk {"id": "body-0298", "role": "body", "section": "Open-loop Control", "weight": 1.0} -->

Since the late 1980s, a series of methods have emerged to manipulate chaotic systems towards a desired "goal dynamics" $\mathbf{g}{(t)}$. Consider a controlled system

<!-- chunk {"id": "body-0299", "role": "body", "section": "Open-loop Control", "weight": 1.0} -->

where $\mathbf{x} \in {\mathbb{R}}^{N}$ is the state vector, ${\mathbf{u}{(t)}} \in {\mathbb{R}}^{M}$ is the control input. In contrast with the network-based problems discussed earlier, here we assume that all state variables are controlled ($M = N$) and ${\det\mathbf{B}} \neq 0$. The goal is to design $\mathbf{u}{(t)}$ so that $\mathbf{x}{(t)}$ converges to a desired trajectory $\mathbf{g}{(t)}$, i.e., ${|{{\mathbf{x}{(t)}} - {\mathbf{g}{(t)}}}|}\rightarrow 0$ as $t\rightarrow\infty$. We can use open-loop control for this purpose, using the control input called the *Hubler action*,

<!-- chunk {"id": "body-0300", "role": "body", "section": "Open-loop Control", "weight": 1.0} -->

We call the regions of the state space from which the controlled orbits converge to the goal trajectory $\mathbf{g}{(t)}$ *entrainment regions*.

<!-- chunk {"id": "body-0301", "role": "body", "section": "Open-loop Control", "weight": 1.0} -->

Note that the method - is not tailored to chaotic systems, but potentially works for any nonlinear system. It has several disadvantages, though: (i) the open-loop control requires a priori knowledge of the dynamics, which is often not precisely known for complex systems; (ii) the applied controls are not always small, requiring high control energy; (iii) the convergence of ${|{{\mathbf{x}{(t)}} - {\mathbf{g}{(t)}}}|}\rightarrow 0$ for $t\rightarrow\infty$ depends on the detailed functional form of $\mathbf{F}{(\mathbf{x})}$ and the initial condition $\mathbf{x}{}$, hence this method is not guranteed to work for arbitrary systems.

<!-- chunk {"id": "body-0302", "role": "body", "section": "Linearization of the Poincaré map: OGY method", "weight": 1.0} -->

The OGY method proposed by Ott, Grebogi and Yorke exploits the observation that typically an infinite number of unstable periodic orbits (UPOs) are embedded in a chaotic attractor (Fig. 29). Therefore we can obtain a desired periodic motion by making only small perturbations to an accessible system parameter.

<!-- chunk {"id": "body-0303", "role": "body", "section": "Linearization of the Poincaré map: OGY method", "weight": 1.0} -->

The OGY method can be summarized as follows: First, we determine and examine some of the low-period UPOs embedded in the chaotic attractor. Second, we choose a desired UPO. Finally, we design small time-dependent parameter perturbations to stabilize this pre-existing UPO.

<!-- chunk {"id": "body-0304", "role": "body", "section": "Linearization of the Poincaré map: OGY method", "weight": 1.0} -->

This method is not only very general and practical, but also suggests that in some systems the presence of chaotic behavior can be an advantage for control. Indeed, if the attractor of a system is not chaotic but has a stable periodic orbit (SPO), then small parameter perturbations can only slightly change the existing orbit. Therefore, given that any one of the infinite number of UPOs can be stabilized, we can always choose the UPO that achieves the best system performance. Hence, chaotic behavior offers us a diverse and rich landscape for the desired dynamic behavior of the system.

<!-- chunk {"id": "body-0305", "role": "body", "section": "Linearization of the Poincaré map: OGY method", "weight": 1.0} -->

To demonstrate this method, let us consider a nonlinear continuous-time dynamical system

<!-- chunk {"id": "body-0306", "role": "body", "section": "Linearization of the Poincaré map: OGY method", "weight": 1.0} -->

where $\mathbf{x} \in {\mathbb{R}}^{N}$ is the state vector and $u \in {\mathbb{R}}$ represents a tunable parameter, which can be considered as a control input. Our task is to reach a desired trajectory $\mathbf{x}^{\ast}{(t)}$ that satisfies with $u = 0$. To achieve that we first construct a surface $S$, called a Poincaré section, which passes through the point $\mathbf{x}_{0} = {\mathbf{x}^{\ast}{}}$ transversally to the trajectory $\mathbf{x}^{\ast}{(t)}$ (see Fig. 30).

<!-- chunk {"id": "body-0307", "role": "body", "section": "Linearization of the Poincaré map: OGY method", "weight": 1.0} -->

Consider a map $\mathbf{x}\mapsto{\mathbf{F}{(\mathbf{x},u)}}$, where $\mathbf{F}{(\mathbf{x},u)}$ is the point of first return to the Poincaré section of the solution of that begins at the point $\mathbf{x}$ and was obtained for the constant input $u$. Since we can integrate forward in time from $\mathbf{x}$, the map $\mathbf{x}\mapsto{\mathbf{F}{(\mathbf{x},u)}}$, called the *Poincaré map*, must exist. Note that even though we may not be able to write down the map $\mathbf{F}$ explicitly, the knowledge that it exists is still useful. By considering a sequence of such maps, we get a discrete system

<!-- chunk {"id": "body-0308", "role": "body", "section": "Linearization of the Poincaré map: OGY method", "weight": 1.0} -->

A key step in the OGY method is to linearize the discrete system as

<!-- chunk {"id": "body-0309", "role": "body", "section": "Linearization of the Poincaré map: OGY method", "weight": 1.0} -->

To stabilize the linear system and hence steer the original system to a desired periodic orbit that passes through $\mathbf{x}_{0}$, the OGY method employs a linear state feedback control law

<!-- chunk {"id": "body-0310", "role": "body", "section": "Linearization of the Poincaré map: OGY method", "weight": 1.0} -->

where $\delta > 0$ is a sufficiently small parameter. Note that the control is only applied in some neighborhood of the desired trajectory, which ensures the smallness of the control action. This piecewise-constant small action control is a key feature of the OGY method. To guarantee the efficiency of the method, the matrix $\mathbf{C}$ must be chosen so that in the linear closed-loop system $\mathbf{z}_{k + 1} = {{({\mathbf{A} + {\mathbf{B}\mathbf{C}}})}\mathbf{z}_{k}}$, the norm ${|{{({\mathbf{A} + {\mathbf{B}\mathbf{C}}})}\mathbf{z}}|} \leq {\rho{|\mathbf{z}|}}$ decreases, where $\rho < 1$.

<!-- chunk {"id": "body-0311", "role": "body", "section": "Linearization of the Poincaré map: OGY method", "weight": 1.0} -->

Extensive numerical simulations have corroborated the practical utility of the OGY method. Furthermore, the OGY method was proven to be effective in experimental systems as well, allowing the stabilization of unstable periodic orbits in a chaotically oscillating magnetoelastic ribbon, a driven diode circuit, a multimode laser with an intracavity crystal, a thermal convection loop, and the Belousov-Zhabotinsky reaction. Slow convergence was often reported, a price we must pay to achieve global stabilization of a nonlinear system with small control action.

<!-- chunk {"id": "body-0312", "role": "body", "section": "Linearization of the Poincaré map: OGY method", "weight": 1.0} -->

The advantage of the OGY method is that it does not require prior knowledge of the system's dynamics. Instead, we just rely on the system's behavior to learn the necessary small perturbation to nudge it towards a desired trajectory. This is similar to the balancing of a stick on our palm, which can be achieved without knowing Newton's second law of motion and the stick's detailed equation of motion. Indeed, in the OGY method, both $\mathbf{A}$ and $\mathbf{B}$ in can be extracted purely from observations of the trajectory on the chaotic attractor. Finally, the OGY method can be extended to arbitrarily high dimensional systems, without assuming knowledge of the underlying dynamics.

<!-- chunk {"id": "body-0313", "role": "body", "section": "Time-delayed feedback: Pyragas method", "weight": 1.0} -->

The Pyragas method employs continuous feedback to synchronize the current state of a system with a time-delayed version of itself, offering an alternative approach to stabilizing a desired UPO embedded in a chaotic attractor. Consider the nonlinear system. If it has a desired UPO $\Gamma = {\{{\mathbf{x}^{\ast}{(t)}}\}}$ with period $T$ for $\mathbf{u} = \mathbf{0}$, then we can use the feedback control

<!-- chunk {"id": "body-0314", "role": "body", "section": "Time-delayed feedback: Pyragas method", "weight": 1.0} -->

where $K$ is the feedback gain and $\tau$ is the delay time, to stabilize the desired UPO. If $\tau = T$ and the solution $\mathbf{x}{(t)}$ of the closed-loop system begins on the UPO, then it remains on the UPO for all $t \geq 0$. Surprisingly, $\mathbf{x}{(t)}$ can converge to the UPO even if initially is not on the UPO, i.e., ${\mathbf{x}{}} \notin \Gamma$.

<!-- chunk {"id": "body-0315", "role": "body", "section": "Time-delayed feedback: Pyragas method", "weight": 1.0} -->

Considering that not all the state variables are experimentally accessible, we can rewrite as

<!-- chunk {"id": "body-0316", "role": "body", "section": "Time-delayed feedback: Pyragas method", "weight": 1.0} -->

for a desired UPO of period $T$. Here ${y{(t)}} = {\mathbf{h}{({x{(t)}})}} \in {\mathbb{R}}$ is an experimentally accessible output signal. The advantage of the time-delayed feedback control law is that it does not require rapid switching or sampling, nor does it require a reference signal corresponding to the desired UPO. Unfortunately, the domain of system parameters over which control can be achieved via is limited. Furthermore, the method fails for highly unstable orbits. Note, however, that an extended variant of the Pyragas method, using a control law whose form is closely related to the amplitude of light reflected from a Fabry-Pérot interferometer can stabilize highly unstable orbits.

<!-- chunk {"id": "body-0317", "role": "body", "section": "Time-delayed feedback: Pyragas method", "weight": 1.0} -->

Despite the simple form of the control signal, the analytical study of the closed-loop system is challenging. Indeed, while there are extensive numerical and experimental results pertaining to the properties and application of the Pyragas method, the sufficient conditions that guarantee its applicability remain unknown.

<!-- chunk {"id": "body-0318", "role": "body", "section": "Time-delayed feedback: Pyragas method", "weight": 1.0} -->

Note that similar to the Pyragas method, a geometric method of stabilizing UPOs also uses time-delays. This method is based on some observations about the geometry of the linearized dynamics around these orbits in the phase space. It does not require explicit knowledge of the dynamics (which is similar to the OGY method), but only experimentally accessible state information within a short period of the system's immediate past. More specifially, it requires a rough location of the UPO and a single parameter easily computed from four data points. This geometric method does not have the problems of the Pyragas method in stabilizing UPOs. The drawback of this geometric method is that it has only been formulated for 2D maps and 3D flows.

<!-- chunk {"id": "body-0319", "role": "body", "section": "Compensatory Perturbations of State Variables", "weight": 1.0} -->

The control tools described above were mainly designed for low dimensional dynamical systems with a simple structure. Most complex systems are high-dimensional, however, consisting of a network of components connected by nonlinear interactions. We need, therefore, tools to bring a networked system to a desired target state. A recently proposed method can work even when the target state is not directly accessible due to certain constraints. The basic insight of the approach is that each desirable state has a "basin of attraction", representing a region of initial conditions whose trajectories converge to it. For a system that is in an undesired state, we need to identify perturbations to the state variables that can bring the system to the basin of attraction of the desired target state. Once there, the system will evolve spontaneously to the target state. Assume that a physically admissible perturbation fulfills some constraints that can be represented by vector expressions of the form

<!-- chunk {"id": "body-0320", "role": "body", "section": "Compensatory Perturbations of State Variables", "weight": 1.0} -->

where the equality and inequality apply to each component individually. To iteratively identify compensatory perturbations we use the following procedure: Given the current initial state of the network, $\mathbf{x}_{0}^{\prime}$, we integrate the system's dynamics over a time window $t_{0} \leq t \leq {t_{0} + T}$ to identify the time when the orbit is closest to the target, $t_{c} \equiv {\arg{\min{|{\mathbf{x}^{\ast} - {\mathbf{x}{(t)}}}|}}}$.

<!-- chunk {"id": "body-0321", "role": "body", "section": "Compensatory Perturbations of State Variables", "weight": 1.0} -->

We then integrate the variational equation up to $t_{c}$ to obtain the corresponding variational matrix, $\mathbf{M}{(t_{c})}$, which maps a small change $\delta\mathbf{x}_{\mathbf{0}}$ in the initial state of the network to a change $\delta\mathbf{x}{(t_{c})}$ in the resulting perturbed orbit at $t_{c}$ according to ${\delta\mathbf{x}{(t_{c})}} = {{{\mathbf{M}{(t_{c})}} \cdot \delta}\mathbf{x}_{\mathbf{0}}}$.

<!-- chunk {"id": "body-0322", "role": "body", "section": "Compensatory Perturbations of State Variables", "weight": 1.0} -->

This mapping is used to select an incremental perturbation $\delta\mathbf{x}_{\mathbf{0}}$ that minimizes the distance between the perturbed orbit and the target at time $t_{c}$, subject to the constraints and additional constraints on $\delta\mathbf{x}_{\mathbf{0}}$ to ensure the validity of the variational approximation.

<!-- chunk {"id": "body-0323", "role": "body", "section": "Compensatory Perturbations of State Variables", "weight": 1.0} -->

The selection of $\delta\mathbf{x}_{\mathbf{0}}$ is performed via a nonlinear optimization that can be efficiently solved using sequential quadratic programming. The initial condition is then updated $\mathbf{x}_{0}^{\prime}\rightarrow{\mathbf{x}_{0}^{\prime} + {\delta\mathbf{x}_{0}}}$, and we test whether the new initial state lies in the target's basin of attraction by integrating the system dynamics over a long time $\tau$. If the system's orbit reaches a small ball of radius $\kappa$ around $\mathbf{x}^{\ast}$ within this time, we declare success and recognize $\mathbf{x}_{0} - \mathbf{x}_{0}^{\prime}$ as a compensatory perturbation (for the updated $\mathbf{x}_{0}^{\prime}$). If not, we calculate the time of closest approach of the new orbit and repeat the procedure.

<!-- chunk {"id": "body-0324", "role": "body", "section": "Compensatory Perturbations of State Variables", "weight": 1.0} -->

Similar to the open-loop control of chaos discussed in Sec. V.1.1, the approach based on compensatory perturbation potentially works for any nonlinear system. It has been successfully applied to the mitigation of cascading failures in a power grid and the identification of drug targets in a cancer signaling network. Yet, the approach requires a priori knowledge of the detailed model describing the dynamics of the system we wish to control, a piece of knowledge we often lack in complex systems. With an imperfect model, a compensatory perturbation may steer the system into a different basin of attraction than the desired one. Studying the dependence of the success rate of this approach on the parameter uncertainty and system noise remains an analytically challenging issue. Moreover, it is unclear how to choose the optimal control set consisting of one or more nodes accessible to compensatory perturbations so that some control objectives, like the number of control nodes or the amount of control energy, are minimized.

<!-- chunk {"id": "body-0325", "role": "body", "section": "Small Perturbations to System Parameters", "weight": 1.0} -->

The control tool described above perturbs the state variables of a networked system. In analogy with the OGY method, we can also control a networked system via small perturbations to its parameters. Note that networked systems are typically high-dimensional, to which the control methodologies developed for chaotic system do not immediately apply. Yet, we can control complex networked systems via perturbations to the *system parameters*, an approach complementary to the approaches based on perturbations of the *state variables*. The key step of this approach is to choose a set of experimentally adjustable parameters and determine whether small perturbations to these parameters can steer the system towards the desired attractor. Depending on the physical constraints the control parameters obey, the directed control path from the undesired attractor to the desired attractor can either be via a direct connection or via intermediate attractors along the control path. If there are no feasible control paths reaching the desired attractor, then we can not steer the system to that attractor, hence control is not possible.

<!-- chunk {"id": "body-0326", "role": "body", "section": "Small Perturbations to System Parameters", "weight": 1.0} -->

Considering each attractor as a node, and the control paths as directed edges between them, we can construct an "attractor network", whose properties determine the controllability of the original dynamic network. For a given nonlinear system, the attractor network can be constructed as follows. First, we identify all possible attractors and choose a set of system parameters that can be experimentally perturbed. Second, we set the system into a specific attractor $a$, and determine the set of attractors into which the system can evolve from the original attractor $a$ with a reasonable combination of the adjustable parameters. This effectively draws a link from attractor $a$ to all other attractors reachable by feasible parameter perturbations. Finally, we repeat this procedure for all attractors, obtaining the attractor network.

<!-- chunk {"id": "body-0327", "role": "body", "section": "Small Perturbations to System Parameters", "weight": 1.0} -->

To illustrate the construction of such an attractor network, consider the epigenetic state network (ESN) that describes the phenotypic transitions on the epigenetic landscape of a cell (Fig. 33). In the epigenetic landscape, two neighboring fixed-point attractors, corresponding to stable cell phenotypes, are connected by a minimal energy path through an unstable transition point (first-order saddle point). The number of fixed points (nodes) and saddle points (edges) grows exponentially with the number of genes (dimensionality). We can rely on a conditional root-finding algorithm to construct this epigenetic state network (ESN). The obtained ESN captures the global architecture of stable cell phenotypes, helping us translate the metaphorical Waddington epigenetic landscape concept into a mathematical framework of cell phenotypic transitions.

<!-- chunk {"id": "body-0328", "role": "body", "section": "Dynamics and Control at Feedback Vertex Sets", "weight": 1.0} -->

For regulatory networks described as a digraph of dependencies, it has been recently shown that open-loop control applied to a feedback vertex set (FVS) will force the remaining network to stably follow the desired trajectories. An FVS is a subset of nodes in the absence of which the digraph becomes acyclic, i.e., contains no directed cycles (Fig. 34). Unlike the approaches discussed in Sec. V.2 and Sec. V.3, this approach has rigorous analytical underpinnings.

<!-- chunk {"id": "body-0329", "role": "body", "section": "Dynamics and Control at Feedback Vertex Sets", "weight": 1.0} -->

Consider a general non-autonomous nonlinear networked system

<!-- chunk {"id": "body-0330", "role": "body", "section": "Dynamics and Control at Feedback Vertex Sets", "weight": 1.0} -->

where $i = {1,\cdots,N}$, and $\mathcal{I}_{i}$ denotes the set of upstream or incoming neighbors of node $i$, i.e., $j \in \mathcal{I}_{i}$ if there is directed edge $({j\rightarrow i})$ in the network. The corresponding network is often called the *system digraph*, which is a transpose of the *inference diagram* introduced in observability (see Sec. IV.2).

<!-- chunk {"id": "body-0331", "role": "body", "section": "Dynamics and Control at Feedback Vertex Sets", "weight": 1.0} -->

An open-loop control applied to the nodes of an FVS will completely control the dynamics of those nodes and hence effectively remove all the incoming links to them. Consequently, those nodes will not be influenced by other nodes. They will, however, continue to influence other nodes and drive the whole system to a desired attractor. Consider, for example, the gene regulatory network of circadian rhythms in mice, consisting of 21 nodes (Fig. 35a). In general there can be multiple minimal FVS's for a given digraph. One such minimal FVS of size seven, i.e. $\mathcal{F} = \{$PER1, PER2, CRY1, CRY2, RORc, CLK, BMAL1$\}$, is highlighted in red in Fig. 35a. The associated dynamical system can be described by a set of ODEs involving 21 variables and hundreds of parameters.

<!-- chunk {"id": "body-0332", "role": "body", "section": "Dynamics and Control at Feedback Vertex Sets", "weight": 1.0} -->

Under a particular choice of parameters, the system has several invariant sets: (i) two stable periodic oscillations (P1 and P2); (ii) one unstable periodic oscillation (UP); and (iii) one unstable stationary point (USS) (Fig. 35b,c). Let us aim to steer the system from P1 to P2. To achieve this, we first need to calculate the time tracks of the seven FVS nodes on the desired invariant set P2, denoted as ${x_{i}^{P2},i} \in \mathcal{F}$, which can be done by numerically integrating the ODEs. Then we prescribe the time tracks of the seven nodes in $\mathcal{F}$ to follow their desired values $x_{i}^{P2}$. This way, we effectively remove any influence from the other 14 nodes to the nodes in $\mathcal{F}$.

<!-- chunk {"id": "body-0333", "role": "body", "section": "Dynamics and Control at Feedback Vertex Sets", "weight": 1.0} -->

The dynamics of the remaining 14 nodes ${x_{i},i} \notin \mathcal{F}$, are determined by the remaining 14 ODEs of the system, where the initial state of these remaining nodes is chosen to coincide with an arbitrary point on the P1 trajectory. As shown in Fig. 35d, the trajectories of the remaining 14 nodes deviate from the original stable periodic orbit P1 and quickly converge to the competing orbit P2. The whole system eventually displays periodic oscillation on the P2 orbit.

<!-- chunk {"id": "body-0334", "role": "body", "section": "Dynamics and Control at Feedback Vertex Sets", "weight": 1.0} -->

In the above example, the identified FVS is a minimal one, i.e., any subset of $\mathcal{F}$ is not an FVS. Yet, a *minimal* FVS is not guaranteed to be the *minimum* one that contains the least number of nodes. Naturally, it will be more desirable to identify and control the nodes in the minimum FVS. Unfortunately, finding the minimum FVS of a general digraph is an NP-hard problem.

<!-- chunk {"id": "body-0335", "role": "body", "section": "Dynamics and Control at Feedback Vertex Sets", "weight": 1.0} -->

This FVS-based open-loop control can be applied to a wide range of nonlinear dynamical systems. It requires only a few conditions (e.g. continuous, dissipative and decaying) on the nonlinear functions $F_{i}$ that are very mild and satisfied by many real systems.

<!-- chunk {"id": "body-0336", "role": "body", "section": "Dynamics and Control at Feedback Vertex Sets", "weight": 1.0} -->

For systems associated with a digraph $G{(V,E)}$, we can rigorously prove that clumping the dynamics of a subset of nodes $S \subseteq V$ will control the rest of the network towards the desired attractor for *all* choices of nonlinearities $F_{i}$ that satisfy the above-mentioned conditions *if and only if* $S$ is an FVS in $G$. Yet, there do exist specific systems (with certain nonlinearity $F_{i}$) where clumping a reduced FVS (i.e. removing one or more nodes from an FVS) is sufficient to control the system to a desired attractor. In other words, for a specific system, clumping an FVS might be not necessary. It would be a natural starting point, though.

<!-- chunk {"id": "body-0337", "role": "body", "section": "Dynamics and Control at Feedback Vertex Sets", "weight": 1.0} -->

Note that to apply the two approaches discussed in the previous subsections, namely the compensatory perturbations of state variables (Sec. V.2), and attractor network based on small perturbations of system parameters (Sec. V.3), we need a detailed knowledge of the system dynamics, including all system parameters. In many cases, we lack such a piece of knowledge. In contrast, to apply the FVS-based open-loop control (Sec. V.4), we just need the trajectories of FVS nodes on the desired attractors. We do not have to know full dynamics, nor the exact parameter values. We just need to assure a few mild conditions on the nonlinear functions $F_{i}$ are satisfied.

<!-- chunk {"id": "body-0338", "role": "body", "section": "Controlling Collective Behavior", "weight": 1.0} -->

Dynamical agents interacting through complex networks can display a wide range of collective behavior, from synchronization to flocking among many interacting agents. In particular the study of network-mediated synchronization has a long history, with applications from biology to neuroscience, engineering, computer science, economy and social sciences. Flocking has also gained significant attention in the past two decades, capturing phenomena from the coordinated motion of birds or fish to self-organized networks of mobile agents. Applications range from massive distributed sensing using mobile sensor networks to the self-assembly of connected mobile networks, and military missions such as reconnaissance, surveillance, and combat using cooperative unmanned aerial vehicles. These problems pose, however, a number of fundamental questions pertaining to the control of self-organized networks.

<!-- chunk {"id": "body-0339", "role": "body", "section": "Controlling Collective Behavior", "weight": 1.0} -->

If we aim to achieve a desired collective behavior, it is often infeasible to directly control all nodes of a large network. This difficulty is partially alleviated by the notion of *pinning control*, which relies heavily on feedback processes. In pinning control a feedback control input is applied to a small subset of nodes called pinned nodes, which propagates to the rest of the network through the edges. The design and implementation of feedback control must take into account both the individual dynamics of the components and the network topology. Conceptually, pinning control is similar to the minimum controllability problem of a linear system discussed in Sec. II. The key difference is that, instead of fully controlling a system, pinning control aims to control only the system's collective behavior, like synchronization or flocking. Pinning control has been extensively applied to the synchronization of coupled oscillators and flocking of interacting agents.

<!-- chunk {"id": "body-0340", "role": "body", "section": "Controlling Collective Behavior", "weight": 1.0} -->

In this section we review some fundamental results on controlling the collective behavior of complex networked systems. We pay particular attention to the pinning control of synchronization and flocking. Synchronization of coupled oscillators is typically studied on fixed network topology. We build on the master stability formalism to explore pinning synchronization, focusing on local and global stability conditions and adaptive strategies. Flocking of multi-agent systems are typically associated with switching or time-varying network topology, because the agents, like robots, vehicles or animals, are often mobile. To illustrate this we discuss the Vicsek model of flocking behavior, emphasizing its control theoretical interpretation. Finally, we review key protocols that can induce flocking in multi-agent systems.

<!-- chunk {"id": "body-0341", "role": "body", "section": "VI.1 Synchronization of coupled oscillators", "weight": 1.0} -->

where $\mathbf{x}_{i} \in {\mathbb{R}}^{d}$ is the $d$-dimensional state vector of the $i$th node, ${\mathbf{f}{(\mathbf{x}_{i})}}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$ determines the individual dynamics of each node, $\sigma$ is the coupling strength, also called the *coupling gain*, $\mathbf{A} = {(a_{ij})}$ is the $N \times N$ adjacency matrix of the network, $w_{ij} \geq 0$ is the weight of link $(i,j)$.

<!-- chunk {"id": "body-0342", "role": "body", "section": "VI.1 Synchronization of coupled oscillators", "weight": 1.0} -->

The output function ${\mathbf{h}{(\mathbf{x})}}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$ is used to couple the oscillators and is identical for all oscillators. For example, if we use ${\mathbf{h}{(\mathbf{x})}} = {(x,0,0)}^{T}$ for a three-dimensional oscillator, like the Lorenz or Rössler oscillator, it means that the oscillators are coupled only through their $x$-components. In general, $\mathbf{h}{(\mathbf{x})}$ can be any linear or nonlinear mapping of the state vector $\mathbf{x}$.

<!-- chunk {"id": "body-0343", "role": "body", "section": "VI.1 Synchronization of coupled oscillators", "weight": 1.0} -->

The system is synchronized when the trajectories of all nodes converge to a common trajectory, i.e.

<!-- chunk {"id": "body-0344", "role": "body", "section": "VI.1 Synchronization of coupled oscillators", "weight": 1.0} -->

for all ${{i,j} = 1},{\cdots,N}$. Such synchronization behavior describes a continuous system that has a uniform movement, used to model synchronized neurons, lasers and electronic circuits.

<!-- chunk {"id": "body-0345", "role": "body", "section": "VI.1 Synchronization of coupled oscillators", "weight": 1.0} -->

Due to the diffusive coupling, the completely synchronized state ${\mathbf{x}_{1}{(t)}} = {\mathbf{x}_{2}{(t)}} = \cdots = {\mathbf{x}_{N}{(t)}} = {\mathbf{s}{(t)}}$ is a natural solution of Eq.. This also defines a linear invariant manifold, called the *synchronization manifold*, where all the oscillators evolve synchronously as $\overset{˙}{\mathbf{s}} = {\mathbf{f}{(\mathbf{s})}}$. Note that $\mathbf{s}{(t)}$ may be an equilibrium point, a periodic orbit, or even a chaotic solution.

<!-- chunk {"id": "body-0346", "role": "body", "section": "VI.1 Synchronization of coupled oscillators", "weight": 1.0} -->

Despite the fact that the completely synchronized state is a natural solution of Eq., it may not emerge spontaneously. For example, if the coupling gain $\sigma$ is close to zero, the oscillators tend to behave independently. If the coupling gain $\sigma$ is too strong, the oscillators may not synchronize either. Our goal is to identify the conditions under which the system can synchronize. A broad spectrum of methods allows us to address this question. The best-known method, discussed next, is based on the calculation of the eigenvalues of the coupling matrix.

<!-- chunk {"id": "body-0347", "role": "body", "section": "VI.1.1 Master stability formalism and beyond", "weight": 1.0} -->

where $\mathbf{I}$ is the $N \times N$ identity matrix and $\otimes$ is the Kronecker product (a.k.a. matrix direct product).

<!-- chunk {"id": "body-0348", "role": "body", "section": "VI.1.1 Master stability formalism and beyond", "weight": 1.0} -->

The key idea of the master stability formalism is that we need to consider only variations that are transverse to the synchronization manifold, as variations along $\mathbf{s}{(t)}$ leave the system in the synchronized state. If these transverse variations damp out, then the synchronization manifold is stable. To separate out the transverse variations, we can project $\delta\mathbf{X}$ into the eigenspace spanned by the eigenvectors $\mathbf{e}_{i}$ of the coupling matrix $\mathbf{G}$, i.e., ${\delta\mathbf{X}} = {{({\mathbf{P} \otimes \mathbf{I}_{d}})}\mathbf{\Xi}}$ with ${\mathbf{P}^{- 1}\mathbf{G}\mathbf{P}} = \hat{\mathbf{G}} = {{Diag}{(\lambda_{1},\lambda_{2},\cdots,\lambda_{N})}}$.

<!-- chunk {"id": "body-0349", "role": "body", "section": "VI.1.1 Master stability formalism and beyond", "weight": 1.0} -->

which results in a block diagonalized variational equation with $N$ blocks, corresponding to $N$ decoupled eigenmodes. Each block has the form

<!-- chunk {"id": "body-0350", "role": "body", "section": "VI.1.1 Master stability formalism and beyond", "weight": 1.0} -->

where ${\mathbf{ξ}}_{i}$ is the eigenmode associated with the eigenvalue $\lambda_{i}$ of $\mathbf{G}$. Note that in deriving we have implicitly assumed that the coupling matrix $\mathbf{G}$ is diagonalizable, which is always true for symmetric $\mathbf{G}$. Thus each eigenmode of the perturbation is decoupled from the others, and will damp out independently and simultaneously. If $\mathbf{G}$ is not diagonalizable, we can transform $\mathbf{G}$ into the Jordan canonical form. In this case, some eigenmodes of the perturbation may suffer from a long transient.

<!-- chunk {"id": "body-0351", "role": "body", "section": "VI.1.1 Master stability formalism and beyond", "weight": 1.0} -->

We can order the eigenvalues of $\mathbf{G}$ such that $0 = \lambda_{1} \leq {{Re}\lambda_{2}} \leq \cdots \leq {{Re}\lambda_{N}}$. Because the row sum of $\mathbf{G}$ is zero, the minimal eigenvalue $\lambda_{1}$ is always zero with the corresponding eigenvector $\mathbf{e}_{1} = {(1,1,\ldots,1)}^{T}$. Hence the first eigenmode ${\overset{˙}{\mathbf{ξ}}}_{1} = {\mathcal{J}{(\mathbf{s})}{\mathbf{ξ}}_{1}}$ corresponds to the perturbation parallel to the synchronization manifold. Due to the Gerschgorin Circle Theorem, all other eigenvalues must have non-negative real parts.

<!-- chunk {"id": "body-0352", "role": "body", "section": "VI.1.1 Master stability formalism and beyond", "weight": 1.0} -->

The corresponding $({N - 1})$ eigenmodes are transverse to the synchronization manifold and must decay to have a stable synchronization manifold.

<!-- chunk {"id": "body-0353", "role": "body", "section": "VI.1.1 Master stability formalism and beyond", "weight": 1.0} -->

The form of each block in is the same up to the scalar multiplier $\sigma\lambda_{i}$. This leads to the variational equation, called the *master stability equation*,

<!-- chunk {"id": "body-0354", "role": "body", "section": "VI.1.1 Master stability formalism and beyond", "weight": 1.0} -->

For small $\mathbf{ξ}$ we have ${\|{{\mathbf{ξ}}{(t)}}\|} \sim {\exp{\lbrack{\Lambda{(\alpha,\beta)}t}\rbrack}}$, which decays exponentially if the maximum Lyapunov characteristic exponent ${\Lambda{(\alpha,\beta)}} < 0$. Consequently, $\Lambda{(\alpha,\beta)}$ is called the *master stability function* (MSF). Given a coupling strength $\sigma$, the sign of the MSF in the point $\sigma\lambda_{i}$ in the complex plane reveals the stability of that eigenmode. If all eigenmodes are stable (i.e. ${\Lambda{({\sigma\lambda_{i}})}} < 0$ for all $i$'s), then the synchronization manifold is stable at that coupling strength.

<!-- chunk {"id": "body-0355", "role": "body", "section": "VI.1.1 Master stability formalism and beyond", "weight": 1.0} -->

Note that since the master stability formalism only assesses the linear stability of the synchronized state, it only yields the necessary, but not the sufficient condition for synchronization.

<!-- chunk {"id": "body-0356", "role": "body", "section": "VI.1.1 Master stability formalism and beyond", "weight": 1.0} -->

For undirected and unweighted networks, the coupling matrix $\mathbf{G}$ is symmetric and all its eigenvalues are real, simplifying the stability analysis.

<!-- chunk {"id": "body-0357", "role": "body", "section": "VI.1.1 Master stability formalism and beyond", "weight": 1.0} -->

\(i\) Bounded: ${\Lambda{(\alpha)}} < 0$ for $\alpha_{1} < \alpha < \alpha_{2}$. This usually happens when ${\mathbf{h}{(\mathbf{x})}} \neq \mathbf{x}$. The linear stability of the synchronized manifold requires that $\alpha_{1} < {\sigma\lambda_{2}} \leq \cdots \leq {\sigma\lambda_{N}} < \alpha_{2}$. This condition can be only fulfilled for $\sigma$ when the eigenratio $R$ satisfies

<!-- chunk {"id": "body-0358", "role": "body", "section": "VI.1.1 Master stability formalism and beyond", "weight": 1.0} -->

The beauty of this inequality comes from the fact that its r.h.s. depends only on the dynamics while its l.h.s. depends only on the network structure. If $R > {\alpha_{2}/\alpha_{1}}$, for any $\sigma$ the synchronization manifold is unstable, indicating that it is impossible to synchronize the network. If $R < {\alpha_{2}/\alpha_{1}}$, the synchronization manifold is stable for ${\sigma_{\min} = {\alpha_{1}/\lambda_{2}} < \sigma < \sigma_{\max} = {\alpha_{2}/\lambda_{N}}}.$ The *synchronizability* of the network can be quantified by the relative interval ${\sigma_{\max}/\sigma_{\min}} = {\alpha_{2}/{({\alpha_{1}R})}}$.

<!-- chunk {"id": "body-0359", "role": "body", "section": "VI.1.1 Master stability formalism and beyond", "weight": 1.0} -->

A network is more synchronizable for higher $\sigma_{\max}/\sigma_{\min}$ (or smaller $R$).

<!-- chunk {"id": "body-0360", "role": "body", "section": "VI.1.1 Master stability formalism and beyond", "weight": 1.0} -->

\(ii\) Unbounded: ${\Lambda{(\alpha)}} < 0$ for $\alpha > \alpha_{1}$. The stability criteria of the synchronized manifold is $\alpha_{1} < {\sigma\lambda_{2}} \leq \cdots \leq {\sigma\lambda_{N}}$, which is true if

<!-- chunk {"id": "body-0361", "role": "body", "section": "VI.1.1 Master stability formalism and beyond", "weight": 1.0} -->

The larger is $\lambda_{2}$ the smaller is the synchronization threshold $\sigma_{\min}$, hence the more synchronizable is the network.

<!-- chunk {"id": "body-0362", "role": "body", "section": "VI.1.1 Master stability formalism and beyond", "weight": 1.0} -->

Inequalities and demonstrate that the MSF framework provides an objective criteria ($R$ or $\lambda_{2}$) to assess the synchronizability of complex networks based on the spectrum of the coupling matrix $\mathbf{G}$ only, without referring to specific oscillators and output functions. The MSF framework allows us to address the impact of the network topology and edge weights on synchronizability. Consequently, there have been numerous numerical attempts to relate the spectral properties of network models to a single structural characteristic of networks, like mean degree, degree heterogeneity, path lengths, clustering coefficient, degree-degree correlations, etc.. The outcome of these analyses is occasionally confusing, because in a networked environment it is usually impossible to isolate a single structural characteristic while keeping the others fixed. Overall, several network characteristics can influence synchronizability, but none of them is an exclusive factor in the observed dependencies.

<!-- chunk {"id": "body-0363", "role": "body", "section": "VI.1.1 Master stability formalism and beyond", "weight": 1.0} -->

The fundamental limitation of MSF is that it only assesses the *linear* or *local* stability of the synchronized state, which is a *necessary*, but not a *sufficient* condition for synchronization. To obtain a sufficient condition, one can use global stability analysis, like Lyapunov's direct method or contraction theory.

<!-- chunk {"id": "body-0364", "role": "body", "section": "VI.1.2 Pinning synchronizability", "weight": 1.0} -->

If a network of coupled oscillators can not synchronize spontaneously, we can design controllers that, applied to a subset of *pinned* nodes $\mathcal{C}$, help synchronize the network. Hence the pinned nodes behave like *leaders*, forcing the remaining *follower* nodes to synchronize. This procedure, known as *pinning synchronization*, is fundamentally different from *spontaneous synchronization* of coupled oscillators, where we don't specify the synchronized trajectory $\mathbf{s}{(t)}$, hence the system "self-organizes" into the synchronized trajectory under appropriate conditions. In pinning synchronization, we choose the desired trajectory $\mathbf{s}{(t)}$, aiming to achieve some desired control objective, and this trajectory must be explicitly taken into account in the feedback controller design. Note that in literature pinning synchronizability is often called pinning controllability. Here we use the term synchronizability to avoid confusion with the classical notion of controllability discussed in Secs. II and III.

<!-- chunk {"id": "body-0365", "role": "body", "section": "VI.1.2 Pinning synchronizability", "weight": 1.0} -->

where $\delta_{i} = 1$ for pinned nodes and 0 otherwise, and

<!-- chunk {"id": "body-0366", "role": "body", "section": "VI.1.2 Pinning synchronizability", "weight": 1.0} -->

The form of the linear feedback controller implies that the completely synchronized state is a natural solution of the controlled network.

<!-- chunk {"id": "body-0367", "role": "body", "section": "VI.1.2 Pinning synchronizability", "weight": 1.0} -->

Similar to spontaneous synchronization, we must derive the necessary and sufficient conditions for pinning synchronization. These conditions are more important from the control perspective, because they are the prerequisite for the design of any practical controller. If we focus on the *local* (or *global*) stability of the synchronized manifold of the controlled network, we obtain the *necessary* (or *sufficient*) condition for pinning synchronization, describing the *local* (or *global*) pinning synchronizability.

<!-- chunk {"id": "body-0368", "role": "body", "section": "VI.1.2 Pinning synchronizability", "weight": 1.0} -->

*Local pinning synchronizability*: Given the presence of inhomogeneous dynamics at the controlled and uncontrolled nodes, the MSF approach can not be directly applied to the controlled network. Instead, we first introduce a virtual node whose dynamics follows ${\overset{˙}{\mathbf{s}}{(t)}} = {\mathbf{f}{({\mathbf{s}{(t)}})}}$, representing the desired synchronization solution. The extended system now has $N + 1$ nodes: ${\mathbf{y}_{i}{(t)}} = {\mathbf{x}_{i}{(t)}}$ for $i = {1,\cdots,N}$; and ${\mathbf{y}_{N + 1}{(t)}} = {\mathbf{s}{(t)}}$. The virtual node is connected to each pinned node.

<!-- chunk {"id": "body-0369", "role": "body", "section": "VI.1.2 Pinning synchronizability", "weight": 1.0} -->

with *control gains* $\kappa_{i} > 0$, parameters that capture the relationship between the magnitude of $\mathbf{h}{(\mathbf{x})}$ and $\mathbf{p}_{i}{(\mathbf{x})}$. By defining the pinning function via we can then rewrite in the form of, with an effective coupling matrix satisfying the zero row-sum condition, allowing us to apply the MSF approach. Indeed, plugging into, we have ${\mathbf{u}_{i}{(t)}} = {\sigma\kappa_{i}{\lbrack{{\mathbf{h}{({\mathbf{s}{(t)}})}} - {\mathbf{h}{({\mathbf{x}_{i}{(t)}})}}}\rbrack}}$ and becomes

<!-- chunk {"id": "body-0370", "role": "body", "section": "VI.1.2 Pinning synchronizability", "weight": 1.0} -->

is the effective coupling matrix of the $({N + 1})$-dimensional extended system. Apparently, $\mathbf{M}$ is a zero row-sum matrix, hence we can sort its eigenvalues as $0 = \lambda_{1} \leq {{Re}\lambda_{2}} \leq \cdots \leq {{Re}\lambda_{N + 1}}$. We can now apply the MSF approach to numerically explore the local stability of the synchronization manifold of the controlled network.

<!-- chunk {"id": "body-0371", "role": "body", "section": "VI.1.2 Pinning synchronizability", "weight": 1.0} -->

The role of the control gain ($\kappa_{i}$), coupling gain ($\sigma$), and the number and locations of the pinned nodes, on local pinning synchronizability has been systematically studied. Consider for example a Barabási-Albert (BA) scale-free network of $N$ identical Rössler oscillators coupled in $x$ and $z$ directions. By assuming $\kappa_{1} = \cdots = \kappa_{N} = \kappa$, it was found that for a wide range of coupling gain $\sigma$, the eigenratio $R^{N + 1} \equiv {{{\text{Re}\lambda_{N + 1}}/\text{Re}}\lambda_{2}}$ of the new coupling matrix $\mathbf{M}$ is minimized and hence the local pinning synchronizability is maximized around a specific $\sigma$-dependent value of the control gain $\kappa$.

<!-- chunk {"id": "body-0372", "role": "body", "section": "VI.1.2 Pinning synchronizability", "weight": 1.0} -->

In other words, too large or too small control gain can reduce the network pinning synchronizability (Fig. 36a,b). In contrast, the number of pinned nodes, regardless if they are chosen randomly or selectively within the network, has a monotonic impact on pinning synchronizability: Controlling more nodes always enhances the network pinning synchronizability, in line with our intuition (Fig. 36c,d). Furthermore, selective pinning, when the nodes are chosen in the order of decreasing degree, yields better synchronizability than random pinning.

<!-- chunk {"id": "body-0373", "role": "body", "section": "VI.1.2 Pinning synchronizability", "weight": 1.0} -->

*Global pinning synchronizability*: By describing the time evolution of the controlled network in terms of the error dynamics, we can map the global pinning synchronizability of to the global asymptotic stability of the synchronized manifold, which can be studied via Lyapunov stability theory.

<!-- chunk {"id": "body-0374", "role": "body", "section": "VI.1.2 Pinning synchronizability", "weight": 1.0} -->

If the desired asymptotic trajectory is an equilibrium point ($\overset{˙}{\mathbf{s}} = {\mathbf{f}{(\mathbf{s})}} = \mathbf{0}$), we can derive sufficient conditions for globally stabilizing the pinning controlled network. For a more general desired trajectory, it has been shown that a single feedback controller can pin a complex network to a homogenous solution, without assuming symmetry, irreducibility, or linearity of the couplings.

<!-- chunk {"id": "body-0375", "role": "body", "section": "VI.1.2 Pinning synchronizability", "weight": 1.0} -->

If the oscillator dynamics $\mathbf{f}{(\mathbf{x})}$ fulfills

<!-- chunk {"id": "body-0376", "role": "body", "section": "VI.1.2 Pinning synchronizability", "weight": 1.0} -->

where $\mathcal{F}_{\mathbf{z}_{1},\mathbf{z}_{2}} \in {\mathbb{R}}^{d \times d}$ is bounded, i.e., there exists a positive constant $\alpha$ such that for any ${\mathbf{z}_{1},\mathbf{z}_{2}} \in {\mathbb{R}}^{d}$, ${\|\mathcal{F}_{\mathbf{z}_{1},\mathbf{z}_{2}}\|} \leq \alpha$, then we can derive tractable sufficient conditions for global pinning synchronizability in terms of the network topology, the oscillator dynamics, and the linear state feedback. Note that condition applies to a large variety of chaotic oscillators. The results indicate that for a connected network, even for a limited number of pinned nodes, global pinning synchronizability can be achieved by properly selecting the coupling strength and the feedback gain.

<!-- chunk {"id": "body-0377", "role": "body", "section": "VI.1.2 Pinning synchronizability", "weight": 1.0} -->

for a constant matrix $\mathbf{K}$, sufficient conditions for global pinning synchronizability can also be derived. Note that the condition is so mild that many systems, from Lorenz system to Chen system, Lü system, recurrent neural networks, Chua's circuit satisfy this condition. Counterintuitively, it was found that for undirected networks, the small-degree nodes, instead of hubs, should be pinned first when the coupling strength $\sigma$ is small. For directed networks, nodes with very small in-degree or large out-degree should be pinned first. This result can be understood by realizing that low in-degree nodes receive less information from other nodes and hence are less "influenced" by others. In the extreme case, nodes with zero in-degree will not be "influenced" by any other nodes, hence they must be pinned first. On the other hand, large out-degree nodes can influence many other nodes, hence it makes sense to pin them first.

<!-- chunk {"id": "body-0378", "role": "body", "section": "VI.1.3 Adaptive pinning control", "weight": 1.0} -->

Implementing the linear feedback pinning controller requires detailed knowledge of the global network topology. This is because we have to check whether there are possible coupling and control gains that ensure pinning synchronizability. Yet, in practice we do not always have access to the global network topology. Given this limitation, recently adaptive control has been proposed for pinning synchronization, in which case a controller adapts to a controlled system with parameters that vary in time, or are initially uncertain, without requiring a detailed knowledge of the global network topology. As we discuss next, many different strategies have been designed to tailor the control gains, coupling gains, or to rewire the network topology to ensure pinning synchronizability.

<!-- chunk {"id": "body-0379", "role": "body", "section": "VI.1.3 Adaptive pinning control", "weight": 1.0} -->

\(i\) *Adaptation of control gains:* To adapt the control gain $\kappa_{i}$, representing the ratio between the pinning function and output function, we choose the control input ${\mathbf{u}_{i}{(t)}} = {- {\delta_{i}\kappa_{i}{(t)}{({{\mathbf{x}_{i}{(t)}} - \mathbf{s}})}}}$, and the control gains as

<!-- chunk {"id": "body-0380", "role": "body", "section": "VI.1.3 Adaptive pinning control", "weight": 1.0} -->

In other words, the control gain $\kappa_{i}$ varies in time and adapts to the error vector ${\mathbf{e}_{i}{(t)}} \equiv {{\mathbf{s}{(t)}} - {\mathbf{x}_{i}{(t)}}}$, that describes the deviation of the oscillator $i$ from the reference signal $\mathbf{s}{(t)}$. If the individual dynamics $\mathbf{f}{(\mathbf{x})}$ satisfies the Lipschitz condition, then the global stability of this adaptive strategy can be assured.

<!-- chunk {"id": "body-0381", "role": "body", "section": "VI.1.3 Adaptive pinning control", "weight": 1.0} -->

\(ii\) *Adaptation of coupling gains:* The coupling gain $\sigma_{ij}$, defining the mutual coupling strength between node pair $(i,j)$, can also be adapted using

<!-- chunk {"id": "body-0382", "role": "body", "section": "VI.1.3 Adaptive pinning control", "weight": 1.0} -->

Note that the adaptive strategies and are based on the local error vectors of nodes or between neighboring nodes, hence they avoid the need for a prior tuning of the control or coupling gains. This is attractive in many circumstances. However, these adaptive strategies still require a prior selection of the pinned nodes based on some knowledge of the network topology. This limitation can be avoided by choosing pinned nodes in an adaptive fashion, as we discuss next.

<!-- chunk {"id": "body-0383", "role": "body", "section": "VI.1.3 Adaptive pinning control", "weight": 1.0} -->

\(iii\) *Adaptive selection of pinning nodes:* Adaptive pinning can be achieved by assuming the pinning node indicator $\delta_{i}$ to be neither fixed nor binary. A common approach is to introduce

<!-- chunk {"id": "body-0384", "role": "body", "section": "VI.1.3 Adaptive pinning control", "weight": 1.0} -->

In other words, $b_{i}{(t)}$ follows the dynamics of a unitary mass in a potential $U{(b_{i})}$ subject to an external force $g$ that is a function of the pinning error $\mathbf{e}_{i}$ and a linear damping term described by $\zeta{\overset{˙}{b}}_{i}$. This is termed as the *edge-snapping mechanism*. For convenience, $U{( \cdot )}$ can be chosen as a double-well potential: ${U{(z)}} = {kz^{2}{({z - 1})}^{2}}$, where the parameter $k$ defines the height of the barrier between the two wells. Then has only two stable equilibria, $0$ and $1$, describing whether node $i$ is pinned or not, respectively. Sufficient conditions for the edge snapping mechanism to drive the network to a steady-state pinning configuration have been derived.

<!-- chunk {"id": "body-0385", "role": "body", "section": "VI.1.3 Adaptive pinning control", "weight": 1.0} -->

The key advantage of the adaptive selection of pinning nodes is that we don't have to choose the nodes we need to pin before we design the controller. Instead, we can select them as we go in an adaptive fashion.

<!-- chunk {"id": "body-0386", "role": "body", "section": "VI.1.3 Adaptive pinning control", "weight": 1.0} -->

\(iv\) *Adaptation of the network topology:* We can ensure synchronization by adapting the network topology. Specially, we can set each off-diagonal element of the Laplacian matrix of the network as

<!-- chunk {"id": "body-0387", "role": "body", "section": "VI.1.3 Adaptive pinning control", "weight": 1.0} -->

where $\sigma_{ij}{(t)}$ is the mutual coupling strength between node pair $(i,j)$, which is adapted as. The weight $\alpha_{ij}{(t)}$ is associated to every undirected edge of the target pinning edge and is adapted as

<!-- chunk {"id": "body-0388", "role": "body", "section": "VI.1.3 Adaptive pinning control", "weight": 1.0} -->

where ${\mathbf{e}_{ij}{(t)}} = {{\mathbf{e}_{j}{(t)}} - {\mathbf{e}_{i}{(t)}}}$, and $U{( \cdot )}$ can be again chosen as a double-well potential so that has only two stable equilibria, 0 and 1. In this case, the target network topology evolves in a decentralized way. The local mismatch of the trajectories can be considered as an external forcing on the edge dynamics, inducing the activation of the corresponding link, i.e. $\alpha_{ij} = 1$.

<!-- chunk {"id": "body-0389", "role": "body", "section": "VI.1.3 Adaptive pinning control", "weight": 1.0} -->

The above adaptive strategies cope better when pinning controllability using a non-adaptive or static approach is initially not feasible. They are also successful in ensuring network synchronization in the presence of perturbations or deterioration, like link failures.

<!-- chunk {"id": "body-0390", "role": "body", "section": "VI.1.3 Adaptive pinning control", "weight": 1.0} -->

Taken together, we have multiple strategies to force a networked system to synchronize. The discussed tools have a wide range of applications for systems in which a synchronized state is desired. In some cases synchronization can be harmful, like in the case of synchronized clients or routers that cause congestion in data traffic on the Internet, or in schizophrenia. In this case the synchronized state can be destroyed by the addition of a single link with inhibitory coupling.

<!-- chunk {"id": "body-0391", "role": "body", "section": "VI.2 Flocking of multi-agent dynamic systems", "weight": 1.0} -->

The flocking of birds, shoaling of fish, swarming of insects, and herding of land animals are spectacular manifestations of coordinated collective behavior of multi-agent systems. These phenomena have fascinated scientists from diverse disciplines, from ecologists to physicists, social and computer scientists. Many models have been proposed to reproduce the behavior of such self-organized systems. The first widely-known flocking simulation was primarily motivated by the visual appearance of a few dozen coherently flying objects, e.g., imaginary birds and spaceships. Yet, the quantitative interpretation of the emerging behavior of huge flocks in the presence of perturbations was possible only following the development of a statistical physics-based interpretation of flocking obtained through the Vicsek model. As we discussed next, the Vicsek model and its variants can be interpreted as decentralized feedback control system with time-varying network structure, offering a better understanding of the origin of collective behavior.

<!-- chunk {"id": "body-0392", "role": "body", "section": "VI.2.1 Vicsek Model and the Alignment Problem", "weight": 1.0} -->

The Vicsek model explains the origin of *alignment*, a key feature of flocking behavior. It is a discrete-time stochastic model, in which autonomous agents move in a plane with a constant speed $v_{0}$, initially following randomly chosen directions. The position $\mathbf{x}_{i}$ of agent $i$ changes as

<!-- chunk {"id": "body-0393", "role": "body", "section": "VI.2.1 Vicsek Model and the Alignment Problem", "weight": 1.0} -->

where the velocity of each agent has the same absolute value $v_{0}$. The direction of agent $i$ is updated using a local rule that depends on the average of its own direction and the directions of its "neighbors", i.e. all agents within a distance $r$ from agent $i$ (Fig.37). In other words,

<!-- chunk {"id": "body-0394", "role": "body", "section": "VI.2.1 Vicsek Model and the Alignment Problem", "weight": 1.0} -->

Here ${\langle{\theta_{i}{(t)}}\rangle}_{r} \equiv {\arctan\left\lbrack {{\langle{{\sin\theta}{(t)}}\rangle}_{r}/{\langle{{\cos\theta}{(t)}}\rangle}_{r}} \right\rbrack}$ denotes the average direction of the agents (including agent $i$) within a circle of radius $r$. The interaction radius $r$ can be set as the unit distance, $r = 1$. The origin of the alignment rule can be the stickiness of the agents, hydrodynamics, could be pre-programmed, or based on information processing. The perturbations are contained in $\Delta_{i}{(t)}$, which is a random number taken from a uniform distribution in the interval $\lbrack{- {\eta/2}},{\eta/2}\rbrack$.

<!-- chunk {"id": "body-0395", "role": "body", "section": "VI.2.1 Vicsek Model and the Alignment Problem", "weight": 1.0} -->

Therefore the final direction of agent $i$ is obtained after rotating the average direction of the neighbors with a random angle. These random perturbations can be rooted in any stochastic or deterministic factors that affect the motion of the flocking agents.

<!-- chunk {"id": "body-0396", "role": "body", "section": "VI.2.1 Vicsek Model and the Alignment Problem", "weight": 1.0} -->

The Vicsek model has three parameters: (i) the agent density $\rho$ (number of agents in the area $L^{2}$); (ii) the speed $v_{0}$ and (iii) the magnitude of perturbations $\eta$. The model's order parameter is the normalized average velocity

<!-- chunk {"id": "body-0397", "role": "body", "section": "VI.2.1 Vicsek Model and the Alignment Problem", "weight": 1.0} -->

For small speed $v_{0}$, if we decrease the magnitude of perturbations $\eta$, the Vicsek model displays a continuous phase transition from a disordered phase (zero average velocity $\phi$, implying that all agents move independently of each other, Fig. 38b) to an ordered phase when almost all agents move in the same direction, through a spontaneous symmetry breaking of the rotational symmetry (Fig. 38d). This much studied kinetic phase transition takes place despite the fact that each agent's set of nearest neighbors change with time as the system evolves and the absence of centralized coordination.

<!-- chunk {"id": "body-0398", "role": "body", "section": "VI.2.1 Vicsek Model and the Alignment Problem", "weight": 1.0} -->

Numerical results indicate that the phase transition is second-order and the normalized average velocity $\phi$ scales as

<!-- chunk {"id": "body-0399", "role": "body", "section": "VI.2.1 Vicsek Model and the Alignment Problem", "weight": 1.0} -->

where the critical exponent $\beta \approx 0.45$ and $\eta_{c}{(\rho)}$ is the critical noise for $L\rightarrow\infty$. Many studies have explored the nature of the above phase transition (whether it is first or second order), finding that two factors play an important role: (i) the precise way that the noise is introduced into the system; and (ii) the speed $v_{0}$ with which the agents move.

<!-- chunk {"id": "body-0400", "role": "body", "section": "VI.2.1 Vicsek Model and the Alignment Problem", "weight": 1.0} -->

The Vicsek model raises a fundamental control problem: Under what conditions can the multi-agent system display a particular collective behavior? Behind each flock of collectively moving agents, like biological organisms or robots, there is a dynamically changing or temporal network, where two agents are connected if they interact, e.g. if their distance is under a certain threshold. Since the agents are moving, the network of momentarily interacting units evolves in time in a complicated fashion.

<!-- chunk {"id": "body-0401", "role": "body", "section": "VI.2.1 Vicsek Model and the Alignment Problem", "weight": 1.0} -->

Though the scalar average in is fundamentally different from the vectorial average, this updating rule still captures the essence of the Vicsek model in the absence of perturbation. More importantly, can be considered as a decentralized feedback control system

<!-- chunk {"id": "body-0402", "role": "body", "section": "VI.2.1 Vicsek Model and the Alignment Problem", "weight": 1.0} -->

Here $\mathbf{L}_{p} = {\mathbf{D}_{p} - \mathbf{A}_{p}}$ is the Laplacian matrix of graph $G_{p}$ with $p \in \mathcal{P}$. $\mathbf{A}_{p}$ is the adjacency matrix of graph $G_{p}$ and $\mathbf{D}_{p}$ is a diagonal matrix whose $i$th diagonal element is the degree of node $i$ in the graph $G_{p}$. ${\sigma{(t)}}:{{0,1,\cdots}\rightarrow\mathcal{P}}$ is a switching signal whose value at time $t$ is the index of the interaction graph at time $t$, i.e., $G{(t)}$.

<!-- chunk {"id": "body-0403", "role": "body", "section": "VI.2.1 Vicsek Model and the Alignment Problem", "weight": 1.0} -->

If $r$ is small, some agents/nodes are always isolated, implying that $G{(t)}$ is never connected. If $r$ is large, then $G{(t)}$ is always a complete graph. The situation of interest is between the two extremes. The goal is to show that for any initial set of agent directions ${\mathbf{θ}}{}$ and for a large class of switching signals the directions of all agents will converge to the same steady state $\theta_{ss}$, reaching alignment asymptotically. Mathematically, this means that the state vector ${\mathbf{θ}}{(t)}$ converges to a vector of the form $\theta_{ss}\mathbf{1}$ with $\theta_{ss}$ the steady state direction, i.e.,

<!-- chunk {"id": "body-0404", "role": "body", "section": "VI.2.1 Vicsek Model and the Alignment Problem", "weight": 1.0} -->

where $\mathbf{1} \equiv {(1,\cdots,1)}_{N \times 1}^{T}$, representing the case when all agents move in the same direction.

<!-- chunk {"id": "body-0405", "role": "body", "section": "VI.2.1 Vicsek Model and the Alignment Problem", "weight": 1.0} -->

If $G{(t)}$ is connected for all $t \geq 0$, then we can prove that alignment will be asymptotically reached. But this condition is very stringent. It can be relaxed by considering that the agents are linked together across a time interval, i.e., the collection or union of graphs encountered along the interval is *connected*. It has been proven that if the $N$ agents are linked together for each time interval, then the alignment will be asymptotically reached. This result has been further extended by proving that if the collection of graphs is *ultimately connected*, i.e., there exists an initial time $t_{0}$ such that over the infinite interval $\lbrack t_{0},\infty)$ the union graph $\mathcal{G} = {\cup_{t = t_{0}}^{\infty}G_{t}}$ is connected, then the alignment is asymptotically reached.

<!-- chunk {"id": "body-0406", "role": "body", "section": "VI.2.1 Vicsek Model and the Alignment Problem", "weight": 1.0} -->

Though the control theoretical analysis is deterministic, ignoring the presence of noise, it offers rigorous theoretical explanations, based on the connectedness of the underlying graph, for some fundamental aspects of the Vicsek model. For example, by applying the nearest neighbor rule, all agents tend to align the same direction despite the absence of centralized coordination and despite the fact that each agent's set of nearest neighbors changes in time. These control theoretical results suggest that to understand the effect of additive noise, we should focus on how noise inputs effect connectivity of the associated neighbor graphs. For example, the numerical finding that, for a fixed noise beyond a critical agent density all agents eventually become aligned, can be adequately explained by percolation theory of random graphs.

<!-- chunk {"id": "body-0407", "role": "body", "section": "VI.2.2 Alignment via pinning", "weight": 1.0} -->

While the virtue of the Vicsek model is its ability to spontaneously reach an ordered phase, we can also ask if such a phase can be induced externally. Therefore, we consider an effective pinning control strategy in which a single pinned node (agent) facilitates the alignment of the whole group. This is achieved by adding to the Vicsek model an additional agent, labeled 0, which acts as the group's *leader*. Agent 0 moves at the same constant speed $v_{0}$ as its $N$ *followers* but with a fixed direction $\theta_{0}$, representing the desired direction for the whole system. Each follower's neighbor set includes the leader whenever it is within the follower's circle of radius $r$. Hence we have

<!-- chunk {"id": "body-0408", "role": "body", "section": "VI.2.2 Alignment via pinning", "weight": 1.0} -->

where ${b_{i}{(t)}} = 1$ whenever the leader is a neighbor of agent $i$ and 0 otherwise. It has been proved that if the $({N + 1})$ agents are *linked together* for each time interval, then alignment will be asymptotically reached. In other words, if the union of graphs of the $({N + 1})$ agents encountered along each time interval is *connected*, then eventually all the follower agents will align with the leader.

<!-- chunk {"id": "body-0409", "role": "body", "section": "VI.2.3 Distributed flocking protocols", "weight": 1.0} -->

Alignment, addressed by the Vicsek model, is only one component of flocking behavior. Indeed, there are three heuristic rules for flocking: (i) *Cohesion*: attempt to stay close to nearby flockmates; (ii) *Separation*: avoid collisions with nearby flockmates; and (iii) *Alignment*: attempt to match velocity with nearby flockmates.

<!-- chunk {"id": "body-0410", "role": "body", "section": "VI.2.3 Distributed flocking protocols", "weight": 1.0} -->

We therefore need a general theoretical framework to design and analyze distributed flocking algorithms or protocols that embody these three rules. The formal approach described next extracts the interaction rules that can ensure the emergence of flocking behavior.

<!-- chunk {"id": "body-0411", "role": "body", "section": "VI.2.3 Distributed flocking protocols", "weight": 1.0} -->

Consider a gradient-based flocking protocol equipped with a velocity consensus mechanism, where each agent is steered by the control input

<!-- chunk {"id": "body-0412", "role": "body", "section": "VI.2.3 Distributed flocking protocols", "weight": 1.0} -->

is gradient-based and regulates the distance between agent $i$ and its neighbors, avoiding the collision and cohesion of the agents. This term is derived from a smooth collective potential function $V_{i}{(\mathbf{q})}$, which has a unique minimum when each agent is at the same distance from all of its neighbors on the proximity graph $G{(\mathbf{q})}$, representing the ideal case for flocking. The second term

<!-- chunk {"id": "body-0413", "role": "body", "section": "VI.2.3 Distributed flocking protocols", "weight": 1.0} -->

regulates the velocity of agent $i$ to match the average velocity of its neighbors, being responsible for the velocity alignment. Here the weighted spatial adjacency matrix ${\mathbf{A}{(t)}} = {\lbrack{a_{ij}{(t)}}\rbrack}$ is calculated from the proximity network $G{(\mathbf{q})}$. The flocking protocol embodies all three rules of Reynolds. However, for a generic initial state and a large number of agents (e.g., $N > 100$), the protocol leads to fragmentation, rather than flocking, meaning that the agents spontaneously form several groups, where different groups move in different directions (Fig. 40c). To resolve this fragmentation issue, we introduce a navigational feedback term to the control input of each agent

<!-- chunk {"id": "body-0414", "role": "body", "section": "VI.2.3 Distributed flocking protocols", "weight": 1.0} -->

drives agent $i$ to follow a group objective.

<!-- chunk {"id": "body-0415", "role": "body", "section": "VI.2.3 Distributed flocking protocols", "weight": 1.0} -->

where ${\mathbf{q}_{\gamma},\mathbf{p}_{\gamma},{\mathbf{f}_{\gamma}{(\mathbf{q}_{\gamma},\mathbf{p}_{\gamma})}}} \in {\mathbb{R}}^{D}$ are the position, velocity, and acceleration (control input) of the virtual leader, respectively. By taking into account the navigational feedback, the protocol enables a group of agents to track a virtual leader that moves at a constant velocity, and hence leads to flocking behavior.

<!-- chunk {"id": "body-0416", "role": "body", "section": "VI.2.3 Distributed flocking protocols", "weight": 1.0} -->

Note that protocol requires all agents to be *informed*, i.e., to know the group objective, or equivalently, the current state $(\mathbf{q}_{\gamma},\mathbf{p}_{\gamma})$ of the virtual leader. It turns out that this is not necessary for flocking. Motivated by the idea of pinning control, it has been shown that, even when only a fraction of agents are informed (or pinned), the flocking protocol still enables all the informed agents to move with the desired constant velocity. An *uninformed* agent will also move with the desired velocity if it can be influenced by the informed agents from time to time. Numerical simulations suggest that the larger the informed group is, the bigger fraction of agents will move with the desired velocity.

<!-- chunk {"id": "body-0417", "role": "body", "section": "VI.2.3 Distributed flocking protocols", "weight": 1.0} -->

If the virtual leader travels with a varying velocity $\mathbf{p}_{\gamma}{(t)}$, the flocking protocol enables all agents to eventually achieve a common velocity. Yet, this common velocity is not guaranteed to match $\mathbf{p}_{\gamma}{(t)}$. To resolve this issue, we can incorporate the acceleration of the virtual leader into the navigational feedback as follows

<!-- chunk {"id": "body-0418", "role": "body", "section": "VI.2.3 Distributed flocking protocols", "weight": 1.0} -->

The resulting protocol enables the asymptotic tracking of the virtual leader with a varying velocity, ensuring that the position and velocity of the center of mass of all agents will converge exponentially to those of the virtual leader.

<!-- chunk {"id": "body-0419", "role": "body", "section": "VI.2.3 Distributed flocking protocols", "weight": 1.0} -->

In summary, the combination of control theoretical and network science approaches can help us understand the emergence of order in multi-agent systems. These tools are indispensable if we wish to understand how to induce order externally, aiming to control the collective behavior of the system.

<!-- chunk {"id": "body-0420", "role": "body", "section": "Outlook", "weight": 1.0} -->

Given the rapid advances in the control of complex networks, we have chosen to focus on a group of results that will likely stay with us for many years to come. The process of organizing the material has also exposed obvious gaps in our knowledge. Therefore, next we highlight several research topics that must be addressed to realize the potential of the control of complex systems. Some of these may be addressed shortly, others, however, may continue to challenge the community for many years to come.

<!-- chunk {"id": "body-0421", "role": "body", "section": "VII.1 Stability of Complex Systems", "weight": 1.0} -->

Stability is a fundamental issue in the analysis and the design of a control system, because an unstable system is extremely difficult and costly to control, and such a system can also be potentially dangerous. Loosely speaking, a system is stable if its trajectories do not change too much under small perturbations.

<!-- chunk {"id": "body-0422", "role": "body", "section": "VII.1 Stability of Complex Systems", "weight": 1.0} -->

The stability of a nonlinear dynamical systems $\overset{˙}{\mathbf{x}} = {\mathbf{f}{(\mathbf{x},t)}}$ can be analyzed by the Lyapunov Stability Theory (LST), without explicitly integrating the differential equation. LST includes two methods: (i) The indirect (or linearization) method, concerned with small perturbation around a system's equilibrium points $\mathbf{x}^{\ast}$ and the stability conclusion is inferred from a linear approximation of the nonlinear systems around this equilibrium point. This justifies the use of linear control for the design and analysis of weakly nonlinear systems. (ii) The direct method is based on the so-called Lyapunov function--- an "energy-like" scalar function whose time variation can be viewed as "energy dissipation". It is not restricted to small perturbations and in principle can be applied to any dynamical system. Yet, we lack a general theory to find a suitable Lyapunov function for an arbitrary system.

<!-- chunk {"id": "body-0423", "role": "body", "section": "VII.1 Stability of Complex Systems", "weight": 1.0} -->

We have to rely on our experience and intuition to formulate Lyapunov functions, like exploiting physical properties (such as energy conservation) and physical insights.

<!-- chunk {"id": "body-0424", "role": "body", "section": "VII.1 Stability of Complex Systems", "weight": 1.0} -->

For a wide range of complex systems certain diagonal-type Lyapunov functions are useful for stability analysis. More importantly, in many cases the necessary and sufficient conditions for the stability of nonlinear systems are also the necessary and sufficient conditions for the diagonal stability of a certain matrix associated to the nonlinear system. This matrix naturally captures the underlying network structure of the nonlinear dynamical system.

<!-- chunk {"id": "body-0425", "role": "body", "section": "VII.1 Stability of Complex Systems", "weight": 1.0} -->

Matrix diagonal stability is a well-known notion in stability analysis since its introduction by Volterra around 1930 in the context of ecological systems. Yet, its usefulness is limited by the difficulty of characterizing the class of large diagonally stable matrices. Though there are efficient optimization-based algorithms to numerically check if a given matrix is diagonally stable, there are no effective theoretical tools to characterize *general* large diagonally stable matrices. Recently, however, necessary and sufficient diagonal stability conditions for matrices associated with *special* interconnection or network structures were studied, improving our understanding of the stability of gene regulatory and ecological networks. More research is required to understand stability, an important prerequisite for control.

<!-- chunk {"id": "body-0426", "role": "body", "section": "VII.1 Stability of Complex Systems", "weight": 1.0} -->

The stability concepts we discussed above consider perturbations of initial conditions for a *fixed* dynamical system. There is another important notion of stability, i.e. *structural stability*, which concerns whether the qualitative behavior of the system trajectories will be affected by small perturbations of the system model itself.

<!-- chunk {"id": "body-0427", "role": "body", "section": "VII.1 Stability of Complex Systems", "weight": 1.0} -->

To formally define structural stability, we introduce the concept of topologically equivalence of dynamical systems. Two dynamical systems are called *topologically equivalent* if there is a homeomorphism $h:{{\mathbb{R}}^{N}\rightarrow{\mathbb{R}}^{N}}$ mapping their phase portraits, preserving the direction of time. Consider two smooth continuous-time dynamical systems $\overset{˙}{\mathbf{x}} = {\mathbf{f}{(\mathbf{x})}}$; and $\overset{˙}{\mathbf{x}} = {\mathbf{g}{(\mathbf{x})}}$. Both and are defined in a closed region $D \in {\mathbb{R}}^{N}$ (see Fig. 42).

<!-- chunk {"id": "body-0428", "role": "body", "section": "VII.1 Stability of Complex Systems", "weight": 1.0} -->

System is called *structurally stable* in a region $D_{0} \subset D$ if for any system that is sufficiently $C^{1}$-close to system there are regions ${U,V} \subset D$, and $D_{0} \subset U$, $D_{0} \subset V$ such that system is topologically equivalent in $U$ to system in $V$ (see Fig. 42a).

<!-- chunk {"id": "body-0429", "role": "body", "section": "VII.1 Stability of Complex Systems", "weight": 1.0} -->

For a two-dimensional continuous-time dynamical system, the Andronov-Pontryagin criterion offers sufficient and necessary conditions for structural stablility. A smooth dynamical system ${\overset{˙}{\mathbf{x}} = {\mathbf{f}{(\mathbf{x})}}},{\mathbf{x} \in {\mathbb{R}}^{2}}$, is structurally stable in a region $D_{0} \subset {\mathbb{R}}^{2}$ if and only if (i) it has a finite number of equilibrium points and limit cycles in $D_{0}$, and all of them are hyperbolic; (ii) there are no saddle separatrices returning to the same saddle (see Fig. 42 b,c) or connecting two different saddles in $D_{0}$ (see Fig. 42d). It has been proven that a typical or generic two-dimensional system always satisfies the Andronov-Pontryagin criterion and hence is structurally stable. In other words, structural stability is a generic property for planar systems.

<!-- chunk {"id": "body-0430", "role": "body", "section": "VII.1 Stability of Complex Systems", "weight": 1.0} -->

Yet, this is not true for high-dimensional systems.

<!-- chunk {"id": "body-0431", "role": "body", "section": "VII.1 Stability of Complex Systems", "weight": 1.0} -->

For $N$-dimensional dynamical systems, Morse and Smale established the sufficient conditions of structural stability Smale. Such systems, often called Morse-Smale systems, have only a finite number of equilibrium points and limit cycles, all of which are hyperbolic and satisfy a transversaility condition on their stable and unstable invariant manifolds.

<!-- chunk {"id": "body-0432", "role": "body", "section": "VII.1 Stability of Complex Systems", "weight": 1.0} -->

The notion of structural stability has not been well explored in complex networked systems.

<!-- chunk {"id": "body-0433", "role": "body", "section": "VII.2 Controlling Adaptive Networks", "weight": 1.0} -->

Adaptability, representing a system's ability to respond to changes in the external conditions, is a key characteristic of complex systems. Indeed, the structure of many real networks co-evolves with the dynamics that takes place on them, naturally adapting to shifting environments.

<!-- chunk {"id": "body-0434", "role": "body", "section": "VII.2 Controlling Adaptive Networks", "weight": 1.0} -->

Adaptive networks, also known as state-dependent dynamic networks in control theory, are collections of units that interact through a network, whose topology evolves as the state of the units changes with time. Adaptive networks are a special class of *temporal networks*, whose edges are not continuously active. If the temporal order of the network snapshots at different time points depend on the states of the nodes, then the temporal network is adaptive. A special case of adaptive networks are *switched systems*, which consist of a family of subsystems and a switching law that orchestrates the switching among them. For switching systems, we can design the switching signal among different subsystems and hence the switching law may be independent from the states of the nodes.

<!-- chunk {"id": "body-0435", "role": "body", "section": "VII.2 Controlling Adaptive Networks", "weight": 1.0} -->

Mycelial fungi and acellular slime molds grow as self-organized networks that explore new territory for food sources, whilst maintaining an effective internal transport system to resist continuous attacks or random damage. Honed by evolution, these biological networks are examples of adaptive transportation networks, balancing real-world compromises between search strategy and transport efficiency.

<!-- chunk {"id": "body-0436", "role": "body", "section": "VII.2 Controlling Adaptive Networks", "weight": 1.0} -->

The genome is also an intriguing example of an adaptive network, where the chromosomal geometry directly relates to the genomic activity, which in turn strongly correlates with geometry. Similarly, neuronal connections (synapses) in our brains can strengthen or weaken, and form in response to changes in brain activity, a phenomenon called *synaptic plasticity*.

<!-- chunk {"id": "body-0437", "role": "body", "section": "VII.2 Controlling Adaptive Networks", "weight": 1.0} -->

A comprehensive analytical framework is needed to address the control of adaptive, temporal and co-evolutionary networks. This framework must recognize the network structure itself as a dynamical system, together with the nodal or edge dynamics on the network, capturing the feedback mechanisms linking the structure and dynamics. Studying the controllability of such systems would be a natural starting point because seemingly mild limitations on either the network structure or the dynamical rules may place severe constraints on the controllability of the whole system. Identifying these constraints is crucial if we want to refrain from improving systems that already operate close to their fundamental limits.

<!-- chunk {"id": "body-0438", "role": "body", "section": "VII.3 Controlling Networks of Networks", "weight": 1.0} -->

Many natural and engineered systems are composed of a set of coupled layers or a network of subsystems, characterized by different time scales and structural patterns. New notions, from *multiplex networks* to *networks of networks*, have been recently proposed to explore the properties of these systems, focusing mainly on their structural integrity and robustness. Consider a multiplex network, i.e. a set of coupled layered networks, whose different layers have different characteristics. We can model such a system as a layered network, whose interconnections between layers capture the interactions between a node in one layer and its counterpart in another layer. Similarly, in a network of networks each node itself is a network or a multi-input/multi-output (MIMO) subsystem. Different nodes/subsystems could have totally different dimensions and dynamics. This is rather different from the control framework discussed in much of this paper, where we typically assumed that all the nodes share the same type of dynamics or even just scalar dynamics (with state variables $x_{i} \in {\mathbb{R}}$ for all nodes).

<!-- chunk {"id": "body-0439", "role": "body", "section": "VII.3 Controlling Networks of Networks", "weight": 1.0} -->

Developing a framework to control networks of networks is a necessary step if we wish to understand the control principles of complex systems. Early attempts have focused on the issues of controllability or observability with linear dynamics. For example, some controllability conditions on the overall network topology, the node dynamics, the external control inputs and the inner interactions have been derived for a networked MIMO system. Interestingly, the controllability of the networked MIMO system is an integrated result of multiple factors, which cannot be decoupled into the controllability of the individual subsystem or the properties solely determined by the network topology. Despite these efforts, we lack a general framework to systematically explore the control of networks of networks. Yet, the problem's importance will likely trigger more research in both network science and control theory.

<!-- chunk {"id": "body-0440", "role": "body", "section": "VII.4 Noise", "weight": 1.0} -->

Complex systems, especially biological systems, are noisy. They are affected by two kinds of noise: the intrinsic randomness of individual events and the extrinsic influence of changing environments. Consider, for example, regulatory processes in a cell. The intrinsic noise is rooted in the low copy number of biomolecules or diffusive cellular dynamics. In particular, if $N$ is the number of molecules in the system, fluctuations in $N$ lead to statistical noise with intensity in the order of $N^{- {1/2}}$. For large $N$, we can assume that a continuous deterministic dynamics effectively describes the changes of the average concentrations. However, for small $N$ the statistical noise cannot be ignored. For example, gene regulation may be affected by large fluctuations due to the low copy number of transcription factors. The extrinsic noise of a biological system is mainly due to the changing environments experienced by the system. The environmental change may have microscopic origin (like cellular age/cell cycle stage and organelle distributions) or can be related to the macroscopic physical or chemical environment (like illumination conditions, temperature, pressure and pH level).

<!-- chunk {"id": "body-0441", "role": "body", "section": "VII.4 Noise", "weight": 1.0} -->

To infer or reconstruct the states of a biological system, we also need to deal with the measurement error, which is independent of the biological system and can also be considered as extrinsic noise.

<!-- chunk {"id": "body-0442", "role": "body", "section": "VII.4 Noise", "weight": 1.0} -->

Both internal and external noises are known to affect the control of complex systems. At this time we lack a full understanding on the role of noise or stochastic fluctuations on the control of complex systems.

<!-- chunk {"id": "body-0443", "role": "body", "section": "VII.5 Controlling Quantum Networks", "weight": 1.0} -->

Quantum control theory aims to offer practical methods to control quantum systems. Despite recent progress, quantum control theory is still in its infancy, for several reasons. First, in classical control it is assumed that the measurement does not affect the measured system. In contrast, in quantum control it is difficult, if not impossible, to acquire information about quantum states without destroying them. Second, some classes of quantum control tasks, like controlling quantum entanglement and protecting quantum coherence, are unique for quantum systems. In other words, there are no corresponding tasks in classical control theory.

<!-- chunk {"id": "body-0444", "role": "body", "section": "VII.5 Controlling Quantum Networks", "weight": 1.0} -->

The notion of quantum networks has been recently proposed by the quantum information community, offering fresh perspectives in the field of complex networks. In a quantum network, each node possesses exactly one qubit for each of its neighbors. Since nodes can act on these qubits, they are often called "stations". The edge between two nodes represents the *entanglement* between two qubits. The degree of entanglement between two nodes can be considered as the *connection probability* ($p$) in the context of classical random graphs.

<!-- chunk {"id": "body-0445", "role": "body", "section": "VII.5 Controlling Quantum Networks", "weight": 1.0} -->

In a classical random graph if we let $p$ scale with the graph size as $p \sim N^{z}$, increasingly complex subgraphs appear as $z$ exceeds a series of thresholds. For example, for $z \leq {- 2}$ almost all graphs contain only isolated nodes and edges. When $z$ passes through $- {3/2}$ (or $- {4/3}$), trees of order 3 (or 4) suddenly appear. As $z$ approaches $- 1$, trees and cycles of all orders appear. Surprisingly, in quantum networks any subgraph can be generated by local operations and classical communication, provided that the entanglement between pairs of nodes scales with the graph size as $p \sim N^{- 2}$. In other words, thanks to the superposition principle and the ability to coherently manipulate the qubits at the stations, even for the lowest non-trivial connection probability that is just sufficient to get simple connections in a classical graph, we obtain quantum subgraphs of any complexity.

<!-- chunk {"id": "body-0446", "role": "body", "section": "VII.5 Controlling Quantum Networks", "weight": 1.0} -->

This result illustrates that quantum networks have unique properties that are impossible in their classical counterparts. Hence, the control of quantum complex networks will require new methodologies.

<!-- chunk {"id": "body-0447", "role": "body", "section": "VII.6 Conclusion", "weight": 1.0} -->

Revealing the control principles of complex networks remains a challenging problem that, given its depth and applications, will probably engage multiple research communities for the next decade. In this review we aimed to summarize in a coherent fashion the current body of knowledge on this fascinating topic. This forced us to explore key notions in control theory, like controllability and observability, but also to explore how to steer a complex networked system to a desired final state/trajectory or a desired collective behavior. There are many outstanding open questions to be addressed, advances on which will require interdisciplinary collaborations. We hope that this review will catalyze new interdisciplinary approaches, moving our understanding of control forward and enhancing our ability to control complex systems.
