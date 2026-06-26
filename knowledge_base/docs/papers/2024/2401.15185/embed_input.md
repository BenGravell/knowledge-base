<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Towards a Theory of Control Architecture: A Quantitative Framework for Layered Multi-rate Control

Topics include Robotics, Robustness, Control, Architecture.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper focuses on the need for a rigorous theory of layered control architectures (LCAs) for complex engineered and natural systems, such as power systems, communication networks, autonomous robotics, bacteria, and human sensorimotor control. All deliver extraordinary capabilities, but they lack a coherent theory of analysis and design, partly due to the diverse domains across which LCAs can be found. In contrast, there is a core universal set of control concepts and theory that applies very broadly and accommodates necessary domain-specific specializations. However, control methods are typically used only to design algorithms in components within a larger system designed by others, typically with minimal or no theory. This points towards a need for natural but large extensions of robust performance from control to the full decision and control stack. It is encouraging that the successes of extant architectures from bacteria to the Internet are due to strikingly universal mechanisms and design patterns. This is largely due to convergent evolution by natural selection and not intelligent design, particularly when compared with the sophisticated design of components. Our aim here is to describe the universals of architecture and sketch tentative paths towards a useful design theory.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Complex engineered and natural control systems, such as those used in robotics, the power grid, human sensorimotor control, and the internet, are characterized by needing to operate robustly and reliably across many spatiotemporal scales, despite being implemented using highly constrained hardware and software. Remarkably, a universal design pattern centered around layered control architectures (LCAs) has emerged to address these challenges across vastly different domains. These LCAs are the central object of study of this paper.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Before proposing a broad definition of LCAs, we consider a familiar representative example from aerospace engineering, namely the widely used Guidance, Navigation, and Control (GNC) approach to aircraft control. Here, the overall task of flying an aircraft from an initial location to a goal location is decomposed into tractable subproblems, as illustrated in Fig.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

- » Guidance determines a desired trajectory from the aircraft's current location to a goal location, in addition to nominal control actions, e.g., changes in forward and rotational velocity, for following the desired trajectory. - » Navigation is tasked with estimating the aircraft's state from onboard sensors, such as accelerometers and gyroscopes, and external signals, such as GPS. - » Control applies forces directly to the aircraft via actuators, e.g., steering, thrust, aileron deflection, in

<!-- chunk {"id": "body-0006", "role": "body", "section": "Summary", "weight": 1.0} -->

This paper focuses on the need for a rigorous theory of layered control architectures (LCAs) for complex engineered and natural systems, such as power systems, communication networks, autonomous robotics, bacteria, and human sensorimotor control. All deliver extraordinary capabilities, but they lack a coherent theory of analysis and design, partly due to the diverse domains across which LCAs can be found. In contrast, there is a core universal set of control concepts and theory that applies very broadly and accommodates necessary domain-specific specializations. However, control methods are typically used only to design algorithms in components within a larger system designed by others, typically with minimal or no theory. This points towards a need for natural but large extensions of robust performance from control to the full decision and control stack. It is encouraging that the successes of extant architectures from bacteria to the Internet are due to strikingly universal mechanisms and design patterns. This is largely due to convergent evolution by natural selection and not intelligent design, particularly when compared with the sophisticated design of components. Our aim here is to describe the universals of architecture and sketch tentative paths towards a useful design theory.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Summary", "weight": 1.0} -->

We highlight some salient features of the GNC approach that we aim to capture in our broader theory of LCAs. The first, and most important aspect, is that an overall complex task (aircraft control) is decomposed into modular subtasks (Guidance, Navigation, and Control) of different complexity that operate at different frequencies over different spatiotemporal resolutions. These control modules, or as we will call them, layers, are allowed to interact, but only via well defined interfaces. For example, the Control layer must operate at a high-frequency as it is tasked with stabilizing the unstable aircraft dynamics about a nominal trajectory in the face of an uncertain and dynamic environment, and hence is limited to simple feedback laws that can be implemented in real-time (e.g., PD control or LQR). In contrast, the Guidance layer, which must contend with vast spatiotemporal scales in planning an aircraft's route, typically issues commands at a much slower frequency than the Control layer, as it must solve a longer horizon trajectory planning problem. Despite this modularization, the layers are nevertheless coupled via the exchange of a reference trajectory from Guidance to Control, and a tracking error from Control to Guidance.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Summary", "weight": 1.0} -->

Enabling both Guidance and Control is the Navigation layer, which is responsible for aircraft state estimation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "A model LCA", "weight": 1.0} -->

This paper seeks to initiate a quantitative study of LCAs such as the one described above. To ground our discussion of LCAs, we begin with the 'model LCA' shown in Fig. 2, which is composed of three layers which broadly decompose across time-scales and complexity/flexibility: 1

<!-- chunk {"id": "body-0010", "role": "body", "section": "A model LCA", "weight": 1.0} -->

- » Decision making: the top layer operates at the slowest frequency of the architecture, but is tasked with mak- 1 By convention, we place slower more complex layers 'higher' in the stack, and faster more rigid layers 'lower.'

<!-- chunk {"id": "body-0011", "role": "body", "section": "A model LCA", "weight": 1.0} -->

- » Trajectory planning: the intermediate layer, sitting between decision making and feedback control, operates at a moderate frequency to generate trajectories that accomplish the mission objectives specified by the decision making layer. Typical techniques employed at this layer include optimization-based (e.g., model predictive control, mixed integer programming) and sampling-based (e.g., rapidly-exploring random tree search) methods. The generated trajectories, which are constrained to satisfy the mission objectives specified by the decision making layer, are transmitted to the feedback control layer. This is precisely the Guidance layer in GNC. - » Feedback control: the bottom layer operates at the fastest frequency of the architecture, and is tasked with tracking the trajectories generated by the planning layer. This layer is the home of feedback control, and while offline computation to synthesize control gains may be sophisticated and expensive, online evaluation is typically constrained to be simple, fast, and rigid. In addition to ensuring that the system tracks the desired trajectory, feedback control also provides robustness to high-frequency and dynamic disturbance processes. This is the Control layer in GNC.

<!-- chunk {"id": "body-0012", "role": "body", "section": "A model LCA", "weight": 1.0} -->

A small note on terminology is in order before proceeding: although the word feedback only appears in the bottom layer, it should be understood that some degree of feedback, either implicit or explicit, is present at all layers. For example, if trajectory planning is implemented using model predictive control, implicit feedback is provided by measuring the current system state. As such, we ask the reader to interpret the use of the word feedback as indicating real-time explicit feedback control, unless described otherwise.

<!-- chunk {"id": "body-0013", "role": "body", "section": "A model LCA", "weight": 1.0} -->

This architectural pattern or similar ones, which should be familiar to control theorists, appears consistently and broadly across domains despite both extreme diversity in the systems on which it is deployed, and the remarkable advances in sensing, actuation, and computation that have occurred over the past decades. Despite the surprising unviersality of LCAs, they have yet to be a central object of study within the systems and controls community. This paper is motivated by this current gap in the literature.

<!-- chunk {"id": "body-0014", "role": "body", "section": "A brief overview of control architecture research", "weight": 1.0} -->

While we defer more detailed literature reviews to appropriate sections, we pause to highlight that this manuscript builds upon and is inpsired by a rich literature, both academic and industrial, on process control and automation architecture. Work providing a qualitative perspective about control architectures can be found. While these works place a heavier emphasis on industrial applications and implementations, e.g., the use of Programmable Logic controllers to implement distributed control systems, they also touch upon topics core to this paper. An interesting observation is that both papers acknowledge the importance of control architecture, while also recognizing its mercurial and difficult to define nature. Although different terminology is used, a layered and multi-rate perspective is provided in both-indeed using model predictive control (MPC) for planning, and simple feedback control (PD control) for tracking is identified as a common design pattern, and is one that we revisit in great detail in the sequel. We view these important qualitative perspectives as complementary to the frameworks we propose, and as further supporting the need for a more rigorous quantitative framework for reasoning about LCAs.

<!-- chunk {"id": "body-0015", "role": "body", "section": "A brief overview of control architecture research", "weight": 1.0} -->

Domain-specific work centered around control architecture can be found in for smart-grid applications, in for cyber-physical-system (CPS) applications, and in for internet congestion control. Once again, we see the key themes of this manuscript, such as layered multi-rate control implemented using diverse components, discussed. For example, the templates proposed in can be directly mapped to the proposed layered strategies in Layered Control Architectures via Optimal Control Decomposition, Lee et al. propose a five layer architecture (called the 5C architecture), with each layer having different complexity and spatiotemporal scope, and initial quantitative methodologies for layering as optimization decomposition can be found. This latter perspective serves as a key starting point for the framework proposed in this paper. Finally, we note that although not the subject of this manuscript, an important enabling technology for control architecture design will inevitably be appropriate modeling languages and frameworks, which may for instance be inspired by or build upon SysML.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Paper organization", "weight": 1.0} -->

The rest of the paper is broadly organized into three parts. In Part 1, composed of the next two sections, we first propose a framework for deriving Layered Control Architectures via Optimal Control Decomposition. We then provide concrete instantantiations of Layered Control Architectures for Robotic Systems to illustrate the already impressive practical impact of layered control system design. In Part 2, composed of the subsequent two sections, we propose an alternative perspective, and frame Architecture Design as Multi-Criterion Optimization. A key takeaway of this section is that matching diversity across layers with diversity in control tasks can lead to LCAs that perform better than any individual layer could on its own. We illustrate these concepts with A Case Study in Sensorimotor Control. Finally, in Part 3, composed of the penultimate section of the paper, we indulge in a more speculative discussion, and introduce qualitative definitions of what we believe to be other Key Concepts in Control Architecture. Finally, we end with Conclusions.

<!-- chunk {"id": "body-0017", "role": "body", "section": "PART 1.1: LAYERED CONTROL ARCHITECTURES VIA OPTIMAL CONTROL DECOMPOSITION", "weight": 1.0} -->

We propose a minimal quantitative framework for deriving and reasoning about LCAs such as those illustrated in Fig. 2. Our starting point is a control policy synthesis problem which captures the key ingredients of modern complex systems that LCAs have evolved to address, namely: (i) the mix of discrete/logical decision making with continuous dynamics and control, and (ii) the diversity in time-scales at which different layers of a system (and its environment) evolve. Inspired by the Layering as Optimization Decomposition approach to layered architectures, originally applied to network congestion control, our strategy is to systematically decompose the overall synthesis problem into tractable subproblems, each associated with a specific layer.

<!-- chunk {"id": "body-0018", "role": "body", "section": "PART 1.1: LAYERED CONTROL ARCHITECTURES VIA OPTIMAL CONTROL DECOMPOSITION", "weight": 1.0} -->

We consider specifications that the system must meet and safety constraints that the system must obey. We restrict ourselves to specifications expressed using formal logic, although alternative formulations are certainly possible. These specifications describe system goals: for example, in robotic applications, such a goal might be navigate to a target, or to perform a household task. Safety constraints, in contrast, are often expressed in terms of set membership constraints on a system's physical state: for example, in aerospace applications, such safety constraints may be expressed in terms of state/input inequality constraint enforcing the aerodynamic flight envelope. Design problems also typically include auxiliary performance objectives (e.g., fuel efficiency, speed, robustness), which are opti- mized subject to the specification and safety constraints. The goal then is to find the most efficient system design, as measured by the auxiliary performance objectives, that meets the system specifications and safety constraints.

<!-- chunk {"id": "body-0019", "role": "body", "section": "PART 1.1: LAYERED CONTROL ARCHITECTURES VIA OPTIMAL CONTROL DECOMPOSITION", "weight": 1.0} -->

Our framework thus centers around an overall synthesis problem that seeks to find a control policy that satisfies high-level specifications, subject to system dynamics as well as state and input constraints. In the interest of clarity, we omit auxiliary performance objectives in the initial formulation, but highlight natural ways in which they can be incorporated throughout. After defining the overall synthesis problem, we show that through suitable relaxations and decompositions, (i) the three layer architecture described above can be derived, and (ii) familiar optimizationbased trajectory planning and feedback control algorithms emerge naturally in an attempt to minimize the errors induced by these relaxations and decompositions.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The overall synthesis problem", "weight": 1.0} -->

We assume that the system specifications are defined using a form of temporal logic, with Linear Temporal Logic (LTL) and Signal Temporal Logic (STL) being the most commonly used in the controls community-in the sequel, we use *TL to denote such general temporal logics. In particular, we let the system goals be specified by a given *TL formula φ defined over a finite set AP of atomic propositions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The overall synthesis problem", "weight": 1.0} -->

The system state evolves according to the continuoustime dynamics where xt ∈ R n is the system state, and ut ∈ R m is the control input. In order to simplify exposition, we assume nominal dynamics without any model uncertainty or process noise. Of course, real systems are subject to both, and how to systematically account for such uncertainty in LCAs remains an important open problem (see Robust LCAs). The state and control inputs are subject to safety constraints of the form xt ∈ X ⊆ R n and u ∈ U ⊆ R m.

<!-- chunk {"id": "body-0022", "role": "body", "section": "The overall synthesis problem", "weight": 1.0} -->

We also define, for a suitable sampling time τ, the corresponding discrete time model FIGURE 3: A mobile robot (the Gritbot) modeled as a Dubins' car. In this case, the Gritbot that is deployed in the Robotarium which utilizes a LCA to allow for the implementation of user algorithms in a safe fashion. where x (k) = x k τ, u (k) = uk τ, and f d is a discretization of the continuous time dynamics f. Albeit somewhat cumbersome, we introduce both continuous and discrete time dynamics to highlight the multi-rate nature of typical LCAs, wherein the decision making, trajectory planning, and feedback control layers all operate at different loop rates, i.e., each layer recomputes or updates its action at a different frequency. Where the switch from continuous to discrete time models is made in the LCA is often subject to computational constraints and loop rate requirements, which are in turn dictated by system specifications, safety constraints, and dynamics, see Multi-Rate Layered Control Architectures and Continuous Time LCAs.

<!-- chunk {"id": "body-0023", "role": "body", "section": "The overall synthesis problem", "weight": 1.0} -->

Nevertheless, a common design pattern, which we adopt here, is to use continuous time models for real-time feedback control (to emphasize fast loop-rates), and discrete time models for both trajectory planning and decision making.

<!-- chunk {"id": "body-0024", "role": "body", "section": "The overall synthesis problem", "weight": 1.0} -->

To verify the satisfaction of the *TL specifications φ, we assume the existence of a labeling function L: X → 2 AP that associates a label encoding the TRUE atomic propositions at every state x ∈ X. Finally, we define the trace, or run, of system Σ under a control input sequence u to be the sequence: where here the signals x = (x, x,...), u = (u, u,...), are discrete time trajectories from the sampled system Σ d. If such a trace satisfies the specification φ, we write ξ (x, u) | = φ.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The overall synthesis problem", "weight": 1.0} -->

We can now finally pose the overall synthesis problem as finding a possibly time-varying state-feedback policy ut: X → U such that: Example 1 (Running example: robot navigation). We use a simple robot navigation problem as a running example to illustrate the concepts introduced in this section. Suppose the system is the Dubins' car (also called a unicycle) with dynamics and that the state and input constraints are simple box constraints To specify the system goals, we define the sets X 1 = { (x 1, x 2, θ) | x 2 1 + x 2 2 ≤ 0.1 2 } and X 2 = { (x 1, x 2, θ) | x 1 ≥ 0.9, x 2 ≥ 0.9 }. The task specification is for the robot to first visit set X 1, and then visit X 2, i.e., to go to a small circle in the center of the space, and then go to the upper right corner (see Fig 4). This can be expressed in LTL via the specification where ∧ and F are the and and eventually atomic propositions, respectively.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Layering via Problem Decomposition and Relaxation", "weight": 1.0} -->

Towards our goal of deriving a layered control architecture, we strategically rewrite the global problem by introducing redundant variables, and subsequently relaxing consistency constraints between these redundant variables to allow for modularization across layers. We emphasize that while problem is fundamental-in that it is dictated by the physics of the system as well as the specification and safety constraints of the problem-and that the proposed framework of problem decomposition and relaxation is foundational to a theory of LCAs, the particular realization of these ideas that follow are architectural design choices. They are by no means unique, although they are chosen to be broadly representative of approaches taken in the literature.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Layering via Problem Decomposition and Relaxation", "weight": 1.0} -->

Decision making layer *TL specifications φ are defined over a discrete state and input spaces, whereas the global problem is defined over continuous state and input spaces. Towards bridging this gap, we assume that the continuous state space X admits a partitioning S. Ideally such a partition is such that for any cell s ∈ S, we have that L (x) = L (y) for all x, y ∈ s, i.e., all states in a partition satisfy the same atomic propositions and are 'semantically equivalent.' However, if the partition of the state space is coarse, this may not hold true and partitionning may introduce conservatism. It is natural to consider this partition as defining a discrete state space for a Markov Decision Process (MDP), and with slight abuse of notation, we use s ∈ S to denote such a discrete state as well. Similarly, a discrete action space A is induced by this partition and the system Σ, allowing us to define the MDP dynamics s (i + 1) = fMDP (s (i), a (i)). The MDP dynamics evolve in discrete-time, with dynamics defined to be consistent with traces of the sampled system Σ d.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Layering via Problem Decomposition and Relaxation", "weight": 1.0} -->

However, the MDP dynamics typically correspond to a sub-sampling of Σ d, i.e., s (i) is determined by x (k δ), for δ ∈ N + a discrete sampling time. In general, this subsampling may be irregular, e.g., if each time-step of the MDP is associated with a change in discrete state, but note that our model can capture this phenomena by including the null action ∅ such that s (i + 1) = fMDP (s (i), ∅) = s (i) for all s (i) ∈ S.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Layering via Problem Decomposition and Relaxation", "weight": 1.0} -->

Example 2 (Running example: robot navigation). A possible discrete state space S with |S| = 14 2 is shown in Fig. 4(right), wherein each square corresponds to a discrete state s ∈ S. This induces corresponding discrete actions A = {↑, ↓, ←, →, ∅ } and MDP dynamics corresponding to those of a typical grid world problem (for clarity of exposition, we assume diagonal movement is not allowed). In particular, letting s = (s 1, s 2) denote the (x 1, x 2) grid position, we then have where we only show dynamics for allowable actions a that would not take the system outside of the state space S. Note that due to the resolution of state space discretization, the set S 1 is an under-approximation of the corresponding continuous set X 1.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Layering via Problem Decomposition and Relaxation", "weight": 1.0} -->

Given this definition and towards the goal of isolating a decision making layer we introduce redundant discrete planning variables s and a, which are subject to the MDP dynamics fMDP: Slightly abusing notation, here the first line replaces the trace over continuous variables (x, u) with one defined over discrete variables (s, a) satisfying the MDP dynamics, and we write s ∋ x to emphasize that the discrete state initial condition s must be consistent with the continuous state initial condition x = x 0. The second line enforces consistency between the remainder of the discrete plan of the first line and the underlying continuous control system Σ. In particular, the constraint x (k) ∈ s (⌊ k / δ ⌋) ensures that the continuous state discrete time trace (x, x,...) induces the correct discrete state trace (s, s,...). Similarly, the constraint x (k) = x k τ ensures consistency between the continuous state discrete time trace (x, x,...) and the continuous state trajectory xt ≥ 0.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Layering via Problem Decomposition and Relaxation", "weight": 1.0} -->

Our first relaxation is to decompose problem by isolating the discrete planning problem which we view as the decision making layer problem. Here, the decision making layer assumes that any discrete plan (s, a) can be realized by the underlying continuous control system Σ. Solving the decision layer problem, e.g., using *TL synthesis methods, yields a discrete state and action plan (s, a) that satisfies the specification φ. We show next how this high-level plan can be used to define a trajectory planning problem using a similar decomposition and relaxation technique. We note that *TL synthesis methods are computationally expensive, and hence replanning at this layer is typically done at a slower time-scale, with the faster lower layers used to mitigate unexpected disturbances in the interim.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Layering via Problem Decomposition and Relaxation", "weight": 1.0} -->

Example 3 (Running example: robot navigation). The decision making layer problem for this example becomes one of finding a state/action trace ( s, a ) that satisfies the specification subject to the discrete time discrete state dynamics.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Trajectory planning layer", "weight": 1.0} -->

Removing the decision making layer problem from problem leaves us with Towards the goal of isolating a trajectory planning layer, we introduce a redundant continuous state discrete time trajectory variable r = (r, r,...), constrained to be consistent with the discrete time state x = (x, x,...). The resulting strategically rewritten equivalent problem is then given by The first line isolates a trajectory generation problem, defined now over the reference trajectory variable r (k), ensuring that (a) the trajectory is consistent with the discrete plan, as enforced by r (k) ∈ s (⌊ k / δ ⌋), and (b) the trajectory is safe, as enforced by r (k) ∈ X. As above, the second line enforces coupling between different layers: r (k) = x (k) ensures that the trajectory and system states are consistent, and once again x (k) = x k τ ensures consistency between the discrete time system Σ d and the continuous time system Σ.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Trajectory planning layer", "weight": 1.0} -->

Our next relaxation is to decompose problem by isolating a middle layer trajectory planning problem, which takes the form of the feasibility problem: Here we drop all consistency constraints that r (k) = x (k) = x k τ except for those enforcing the initial condition r = x, and a reference trajectory r that satisfies the state constraint r (k) ∈ X and specification constraints r (k) ∈ s (⌊ k / δ ⌋) is searched. Due to this decomposition and relaxation of the constraints, the reference trajectory produced by solving feasibility problem is not guaranteed to be dynamically feasible, and therefore the tracking error between the true system state x (k) and the planned trajectory r (k) should be accounted for when enforcing the specification and safety constraints r (k) ∈ X ∩ s (⌊ k / δ ⌋). Letting C (k): = X ∩ s (⌊ k / δ ⌋) denote the intersection of the specification and safety constraints at discrete time step k, define the tightened constraint set C (k), and replace the specification and safety constraints with r (k) ∈ C (k).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Trajectory planning layer", "weight": 1.0} -->

How to appropriately tighten this constraint set depends on the feedback control layer, but once tracking error has been characterized, standard tools can be used.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Trajectory planning layer", "weight": 1.0} -->

In order to promote reference trajectories that are easy to track by the underlying continuous system Σ, the feasibility problem is often modified to produce approximately dynamically feasible solutions. For example, it is common to decompose the control policy into a feedforward term uff, depending on the reference trajectory, and a feedback term ufb, depending on the system state (or more specifically, on the tracking error). For example, a typical such decomposition is to simply set ut ( xt ) = uff ( r ( ⌊ t / τ ⌋ )) + ufb ( et ), for tracking error et: = xt -r ( ⌊ t / τ ⌋ )). Another standard approach is to assume that the reference trajectory obeys simplified planning dynamics r ( k + 1 ) = f plan ( r ( k ), uff ( k )). A common choice for these simplified planning dynamics is to use a reduced order model defined by y ( k + 1 ) = from ( y ( k ), v ( k )), where y ∈ R p and v ∈ R s, with p ≤ n and s ≤ m.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Trajectory planning layer", "weight": 1.0} -->

This case can be integrated into the proposed framework by replacing the consistency constraint r ( k ) = x ( k ) with a reduced order consistency constraint y ( k ) = π x ( x ( k )), for π x: R n → R p some projection map encoding the model order reduction. To distinguish this important special case, in the sequel we reserve r ( k ) for full order reference trajectories, i.e., reference trajectories defined over the entire state with both r ( k ), x ( k ) ∈ R n, and use y ( k ) to denote reduced order model states, as these are often used as tracked outputs at the feedback control layer.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Trajectory planning layer", "weight": 1.0} -->

Finally, we make the following additional modifications. First, towards employing a receding horizon control approach, we restrict the trajectory planning problem to be over a finite horizon N. Second, we encode additional desirable properties of the trajectory, e.g., smoothness, via a running cost function C (r, u) and a terminal cost CN (r). Integrating these elements with those described above yields the planning problem solved at discrete time step k: The planning problem is typically solved and implemented in a receding-horizon fashion, e.g., via model predictive control (MPC), and as such is limited to being resolved at an intermediate frequency (i.e., more frequently than the decision layer problem, but less frequently than the feedback control layer).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Trajectory planning layer", "weight": 1.0} -->

We end by noting that this is but one approach to defining a planning problem given a discrete state plan s. Alternative approaches consider, for example, loss functions that penalize deviations of the reference trajectory r from particular waypoints that are consistent with the discrete state plan s. It is hopefully clear that problem is equivalent to such an approach, up to hard/soft constraints.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Trajectory planning layer", "weight": 1.0} -->

Example 4 (Running example: robot navigation). By converting the state trace ( s, s,... ) computed by the decision making layer from discrete ( s 1, s 2 ) coordinates to continuous ( x 1, x 2 ) coordinates, e.g., by choosing the centroid of cell ( s 1, s 2 ), these can be used to define a sequence of waypoints (( p 1, p 2 ), ( p 1, p 2 ),... ), with ( p 1 ( i ), p 2 ( i )) ∈ R 2, that can be used as stateconstraints within the planning layer. These waypoints are illustrated with blue circles in Fig. 4: on the left, we illustrate their use as waypoints for continuous trajectory planning, and on the right, we illustrate their use as a feasible state trace in the discretized state space S.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Trajectory planning layer", "weight": 1.0} -->

We formulate the planning problem using a reduced order linear model composed of decoupled singleintegrator dynamics in the x 1 and x 2 directions, i.e., we set y (k) = (y 1 (k), y 2 (k)), v (k) = (v 1 (k), v 2 (k)), and from (y (k), v (k)) = (y 1 (k) + τ v 1 (k), y 2 (k) + τ v 2 (k)). In this case, we are using a reduced order model that projects out the angle θ and that introduces feedforward linear velocity inputs (v 1, v 2).

<!-- chunk {"id": "body-0042", "role": "body", "section": "Trajectory planning layer", "weight": 1.0} -->

We use the waypoints ((p 1, p 2), (p 1, p 2),...) to define constraints on the trajectory of the form | y 1 (k) -p 1 (⌊ k / δ ⌋) | ≤ ∆ for ∆ half the length of the square cells defining the discrete state space, and idem for the x 2 -coordinate, i.e., we ask that the reference trajectory follow the sequence of discrete cells defined by the discrete state trace (s 1 (i), s 2 (i)), but allowing appropriate time within each cell as dictated by the sampling rate δ used at the decision making layer. We additionally impose smoothness and control effort penalties in the objective, and constrain the reference trajectory to satisfy tightened state constraints (here we assume that the feedback control layer can guarantee a tracking error of at most.05 in either of the (x 1, x 2) coordinates). The resulting planning problem solved at time step k over a horizon N is then given: An illustrative example of the resulting reference trajectory is shown in red in Fig. 4(left).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Real-time feedback control layer", "weight": 1.0} -->

Finally, we consider the feedback control layer. At discrete time step k, given a solution (r (k: k + N), uff (k: k + N)) to the planning layer problem, we must contend with the remaining constraints, now truncated to the planning horizon N: We relax this problem by (a) removing the state constraint xt ∈ X, as this is addressed within the planning problem, and (b) allowing for the state x to deviate from the reference trajectory r, as the reference trajectory r is not expected to be dynamically feasible: In the above, for a positive semi-definite matrix P, we let ∥ z ∥ 2 P: = z T Pz, define the tracking error et: = xt -r (⌊ t / τ ⌋), and slightly abuse notation by letting uff, t = uff (⌊ t / τ ⌋) be the zero-order holds of their corresponding discrete time signal. This problem can be viewed as a 'best-effort' tracking controller.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Real-time feedback control layer", "weight": 1.0} -->

Loop rate constraints lead to either offline computed feedback policies that approximately solve the problem (e.g., LQR tracking), to simple to implement approaches such as PD control, or to myopic simplifications that can be solved in real-time via e.g., quadratic programming. All of these approaches can be viewed as further relaxations of the above tracking problem. While widely used, the proposed relaxation and its extensions typically lack tracking error guarantees. To address this concern, recent work has leveraged Lyapunov-based techniques to certify tracking error bounds, which in turn allow for a principled tightening of the constraints used in the planning layer. We highlight some of these techniques, as applied to robotic LCAs, in the next section.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Real-time feedback control layer", "weight": 1.0} -->

Example 5 (Running example: robot navigation). While many feedback control approaches are possible here, we take this opportunity to briefly introduce differential flatness-based control and show how it can be used in this context. To synthesize a feedback controller that tracks the reduced order model reference trajectory (yt, vt) = (y (⌊ t / τ ⌋), v (⌊ t / τ ⌋)), we first identify the fl at outputs such that the state and inputs can be written as a function of these flat outputs and derivatives.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Real-time feedback control layer", "weight": 1.0} -->

For the unicycle dynamics, a flat output is ξ = (x 1, x 2), as verified by the relationship In order to synthesize a feedback controller, it is convenient to define the flat state z: = (ξ 1, ξ 2, ˙ ξ 1, ˙ ξ 2) = (x 1, x 2, ˙ x 1, ˙ x 2) ∈ R 4 and flat control input a: = (¨ ξ 1, ¨ ξ 2) = (¨ x 1, ¨ x 2) ∈ R 2, resulting in the linear dynamics for zt ∈ R 4 and at ∈ R 2. With slight abuse of notation, we may then write xt = x ♭ (zt) and ut = u ♭ (zt, at) by making the appropriate identifications between (ξ t, ˙ ξ t, ¨ ξ t) and (zt, at).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Real-time feedback control layer", "weight": 1.0} -->

We can then synthesize a feedforward plus feedback policy using, for example, PD control by setting for appropriately tuned positive definite matrices K ♭ p and K ♭ D. Note that in this case, the feedforward term ˙ vt can be approximated via a finite difference, i.e., ˙ vt ≈ (v (⌊ t / τ ⌋) -v (⌊ t / τ ⌋ -1)) / τ.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Real-time feedback control layer", "weight": 1.0} -->

We now discuss how to translate the flat state zt and flat input at to a control input ut composed of feedforward and feedback terms given current measurements of zt = (x 1, x 2, ˙ x 1, ˙ x 2) t. We define the feedforward term to be given precisely by the mapping from flat state and input to control input: If the mapping u ♭ exactly captures the system dynamics, then no additional feedback term would be required. However, in practice, the Dubins' car is often used as a reduced order model for planning trajectories for more complex systems such as quadrupeds (see Fig. S1 in Multi-Rate LCAs in Practice and Ex. 6). As such, a feedback term to ensure that flat and actual states match is additionally required. One such option is again a PD controller: for positive definite matrices KP and KD. Note here that the flat lookahead state zt + τ is obtained by forward integrating the flat dynamics with the at given as in and zt = (x 1, x 2, ˙ x 1, ˙ x 2) t obtained from hardware measurements.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Real-time feedback control layer", "weight": 1.0} -->

The final control input is then the sum of both the feedforward and feedback terms, i.e., as suggested in the feedback control problem. A conceptual illustration of the resulting evolution of the actual system state is shown with a dashed black line in Fig. 4.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Discussion", "weight": 1.5} -->

We obtained a LCA by introducing redundant variables and suitable relaxations to decompose the overall synthesis problem into tractable decision making, trajectory generation, and feedback control subproblems, as specified in equations and, respectively. This highlights another key feature of LCAs: they allow for intractable global problems to be decomposed into tractable subproblems, often with minimal loss in performance or efficiency. We note that the proposed decomposition is only one of certainly many approaches, and is chosen to be consistent with the rest of the manuscript. Indeed, while the above framework provides a more formal perspective on LCAs, it still has an element of 'art' to it. In particular, how to relax the overall synthesis problem, as well as how to bridge the simplifications between the different layers of the resulting architecture is still up to the designer. Nevertheless, by posing the problem in this way, there is a natural nested optimization structure that emerges that may allow for more principled methods of LCA design to be defined. We highlight next some key open questions and concepts that we do not treat in depth, but certainly deserve more investigation.

<!-- chunk {"id": "body-0051", "role": "body", "section": "What about the hardware?", "weight": 1.0} -->

Each layer described above delineates a functional component of an overall decision and control stack. Equally important are the physical substrates used to implement these functional layers. For example, a motor used in a robotic system to actuate a joint is composed of different scales of components, ranging from circuit elements to microprocessors to motor components. While these physical substrates are closely related to the layers they are used to implement, they are distinct: to make this explicit we use the term levels for physical substrates, and reserve layers for functional components. We expand on this idea, and introduce other key concepts of LCAs not touched upon here, in Key Concepts in Control Architecture. Furthermore, in Architecture Design as Multi-Criterion Optimization, we present a quantitative framework to inform how to choose diverse hardware to implement diverse functionality as a function of diversity in the control task at hand, and instantiate this perspective in A Case Study in Sensorimotor Control.

<!-- chunk {"id": "body-0052", "role": "body", "section": "How many layers should there be?", "weight": 1.0} -->

This section presented an approach to deriving an LCA with three layers, each operating at different spatiotemporal resolutions. While these three layers, namely decision making, trajectory generation, and feedback control, are commonly found in complex engineered systems, this pattern is by no means the only one possible. Indeed, all of the concepts introduced above can be applied recursively, leading to layers of layers. For example, there can be several layers of trajectory planning, operating at different loop rates, using different planning models, and planning over different horizons, see for example Continuous Time LCAs. Similarly, nested control loops are a standard control design pattern that can be interpreted as different layers of real-time feedback control. While we present a framework for deriving layers given an overall problem formulation, we still lack quantitative tools for deciding how many layers there should be, as well as what information should be exchanged between them. This is undoubtedly a key open question.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Multi-rate control", "weight": 1.0} -->

In the above, we hint at the role of multi-rate control in LCAs that seeks to address implicit timing constraints. Low layer feedback control operates in (near) realtime, trajectory generation at a slower rate, and decision making at a slower rate still. This suggests that ideas from singular perturbation analysis and timescale separation (see for example and references therein) may also be used to provide further rigor to the approach. We further explore Multi-Rate Layered Control Architectures in robotic systems in the next section.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Robust LCAs", "weight": 1.0} -->

We omit uncertainty due to process noise and modeling errors in our development. However, practical LCAs must be robust to these effects. Promising approaches to tackling uncertainty between layers include the use of robust Lyapunov certificates for guaranteeing bounded tracking error of a reference trajectory by the feedback control layer (see for example Continuous Time LCAs), and more generally, the use of assume-guarantee contracts. These approaches are intuitive and effective, but it is nevertheless of interest to investigate whether such certificates can be derived by applying similar decompositions and relax- ations to a robust overall synthesis problem that explicitly acknowledges uncertainty in its initial formulation.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Layered sensing architectures", "weight": 1.0} -->

We also emphasize that although our focus in this section has been on fully-observed state-feedback control problems, analogous layered decompositions for sensing and output feedback problems need to be developed. A promising starting point is to recognize that different sensors, ranging from semantically rich and complex sensors (e.g., cameras and LIDAR) to simple single output sensors (e.g., IMUs and gyroscopes), are naturally assigned to each of the decision making (e.g., computer vision, semantic segmentation), trajectory generation (e.g., VIO + SLAM), and feedback (e.g., IMUs) layers.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Learning in LCAs", "weight": 1.0} -->

The use of rich perceptual sensors such as cameras invariably introduces learning into the resulting LCAs, which is a topic we cannot hope to do justice to within the scope of this paper. This is however an exciting and important direction to be explored, with learning and data-driven techniques poised to make significant impact in designing effective LCAs.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Layering as optimization decomposition", "weight": 1.0} -->

The layering as optimization decomposition (cf. and references therein) and the reverse/forward engineering (cf. and references therein) paradigms have been particularly fruitful in tackling internet and power-grid control problems, respectively. Both of these frameworks can be loosely viewed as using the dynamics of the system to implement a distributed optimization algorithm through vertical (layering) and horizontal (distributed) decomposition. These methods ensure that the state of the system converges to a set-point that optimizes a utility function. These approaches can scale to large systems by taking advantage of the structure underlying the utility optimization problem, and can simultaneously identify and guarantee stability around an optimal equilibrium point. Nevertheless, they do not explicitly consider optimal control, and in particular transients, in their analysis, making them an important but incomplete first step towards a theory of LCAs.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Decision making and continuous control", "weight": 1.0} -->

This line of work seeks to make explicit that although formal specifications are inherently discrete, in order to ensure that a system satisfies them, designers must account for continuous dynamics and control. One line of work seeks to reformulate *TL specifications into continuous control tasks through the use of control Lyapunov functions (CLFs) and control barrier functions (CBFs), see for example. An alternative approach is to encode *TL constraints via mixed integer linear constraints in robust/optimal control problems, or to abstract the continuous control problem into an uncertain finitestate MDP and use robust dynamic programming. Closely related is the work of Fan et al., wherein decision making is done via SAT-based trajectory planning methods which solve a satisfiability (SAT) problem over quantifier free linear real arithmetic. Other representative works that explicitly acknowledge the inherently hybrid (discrete/continuous) nature of the decision making and control problem, and that seeks to bridge them in a principled way, include reactive planning approaches and the use of CBFs for determining the magnitude of disturbance that a system can be subject to while still ensure satisfaction of STL specifications.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Decision making and continuous control", "weight": 1.0} -->

Barrier functions have also been applied to POMDPs in the context of distribution temporal logic (DTL) and coherent risk measures (e.g., CVaR) to enforce safety constraints at a planning level. More broadly, risk-aware planning and control is considered. Implicit in all of the above is a layered architecture wherein the high-layer decision making component operates on a discrete abstraction of the underlying continuous time system, and similarly, the underlying continuous time system implements planning/control layers in order to meet the plan specified by the top decision making layer.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Trajectory generation and continuous control", "weight": 1.0} -->

Approaches to dynamics aware trajectory generation typically follow a classic two phase approach, wherein first a graph is constructed whose nodes are collision free configurations and whose edges correspond to feasible paths between these configurations, see for example and references therein. More recent approaches based on graphs of convex sets, motion primitives, optimization-based methods, control lyapunov, barrier, and contraction metrics, and reachability techniques have also been proposed to bridge the gap between low-layer fast-time scale control and middle-layer intermediate-time scale trajectory generation. The common theme in all of these approaches is the use of simplified dynamics in the trajectory generation layer, allowing for fast replanning, and a low-layer feedback controller that provides certifiable guarantees on tracking error. Finally, most closely related to the framework presented in the previous discussion are the results found, wherein it is shown that a two-layer trajectory generation/feedback control LCA can be obtained by suitably relaxing consistency constraints between the state and reference trajectory. A key feature of this approach is that the trajectory planning problem is augmented with a tracking penalty regularizer that promotes dynamic feasibility of the synthesized reference signal.

<!-- chunk {"id": "body-0061", "role": "body", "section": "PART 1.2: LAYERED CONTROL ARCHITECTURES FOR ROBOTIC SYSTEMS", "weight": 1.0} -->

LCAs have long found use on robotic systemsempirically, it is well-known that this is the best (and arguably only) way to implement controllers in practice. Yet, despite this empirical evidence there is very little analysis of LCAs. Conversely, while the control community applies rigorous approaches to controller synthesis, it is often only applied to a single layer. This points to a unique opportunity for the controls community: reverseengineering and analyzing the LCAs deployed on robotic systems that have proven useful in practice.

<!-- chunk {"id": "body-0062", "role": "body", "section": "PART 1.2: LAYERED CONTROL ARCHITECTURES FOR ROBOTIC SYSTEMS", "weight": 1.0} -->

To put the central role of LCAs on robotic systems in context, one should first consider the hardware itself. A robotic system, broadly defined, typically consists of three main components: sensors used for perception, a central processor, and motor controllers used for driving actuators. Concrete examples of this include: cameras mounted on a legged robot for localization and mapping, or proximity sensors on a vehicle for advanced driver assistance. In this context, LCAs (as shown in Fig. 5) are often deployed relative to these physical levels on hardware (see Key Concepts in Control Architecture for more examples of how levels and layers interact in LCAs). Perception leads to a decision making layer operating at a discrete/semantic level of abstraction, the central processor leads to reference signal generation using reduced order models, and finally at the actuator level real-time algorithms instantiate feedback control. 2 This section gives concrete instantiations of LCAs for robotic systems. We start by defining robotic system dynamics, and subsequently work our way up the layers of a typical instantiantion of LCAs for robotic control. A goal of this section is to highlight the importance of multi-rate control in the context of LCAs.

<!-- chunk {"id": "body-0063", "role": "body", "section": "PART 1.2: LAYERED CONTROL ARCHITECTURES FOR ROBOTIC SYSTEMS", "weight": 1.0} -->

We start with the feedback control layer-termed the real-time feedback control layer herein to highlight the fast loop rate at which it is implemented. We then discuss trajectory planning paradigms, and end by highlighting approaches to their integration with the real-time feedback control layer. We forego a discussion on the decision making layer for the sake of brevity. See for a formal inclusion of decision making with the methods presented in this section.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Robot Dynamics", "weight": 1.0} -->

Robotic systems are inherently governed by nonlinear equations of motion. These represent the physical evolu- 2 The robotics literature refers to these different layers as highlevel, mid-level, and low-level control. We however argue that these are better viewed through the lens of LCAs, and hence use the layered terminology defined in the previous sections. tion of the system and are typically obtained from the Euler-Lagrange equations: where here qt ∈ Q are the configuration variables of the system, ˙ qt ∈ TqQ is a vector of velocities (which take values in the tangent space to the configuration space), D (qT) is the inertia matrix, C (qt, ˙ qt) the Coriolis matrix, G (qt) contains the gravity related terms, and B is the actuation matrix.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Robot Dynamics", "weight": 1.0} -->

Defining the state vector: xt = (qt, ˙ qt) ∈ TQ, where for simplicity we can work with a local coordinate chart of Q wherein TQ ∼ = R n for n even, allows for the formulation of a control system affine in the control input: where f: R n → R n and g: R n → R n × R m can be directly obtained. The end result is a control system of the form with the additional structural property that the control input appears in an affine fashion, an observation which has important ramifications for controller synthesis.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Real-Time Feedback Control Layer", "weight": 1.0} -->

We begin by tackling the feedback control problem for robotic systems. We assume that a trajectory, containing both a (reduced order) reference trajectory and a feedforward control term, is available. We discuss approaches to solving this trajectory problem after addressing the feedback control problem. An emphasis is placed throughout on the need for real-time feedback control.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Linear Control", "weight": 1.0} -->

For robotic systems, the most common form of real-time controller 3 is a simple linear feedback controller acting on the error, e.g., a PD controller implemented at the motor control layer. These controllers are highly effective in practice when implemented properly. It is important to stress that this is not due to the dynamics being linear (they are not), nor does it imply that the dynamics are even locally linear (again, they are not). Rather, these controllers work well exactly because of their use within a LCA, running at a fast loop rate and actuating as a function of tracking error. This second observation, that linear control actuates only on the error (and thus is independent of model information) is critical. To provide a precise instantiation of real-time linear controllers, consider a continuous time reference signal r = (r q, ˙ r q) that we wish to track (decomposed into a reference position and velocity) and an associated feedforward control input u ff. Then the simplest form of feedforward and feedback control becomes: 3 Historically called 'low-level control.'

<!-- chunk {"id": "body-0068", "role": "body", "section": "Linear Control", "weight": 1.0} -->

That linear controllers can stabilize the nonlinear dynamics associated with a robotic system can be made rigorous in certain cases. To this end, assume that the robotic system is fully actuated, i.e., B is invertible, and for simplicity take B = I. Then Picking uff, t = G (qt) in equation results in asymptotic stability of the tracking of the reference signal r. To see this, let e q = q -r q and ˙ e q = ˙ q -˙ r q be the position and velocity error in tracking the reference signal r. Define the error signal e: = (e q, ˙ e q) and consider the Lyapunov function candidate: which is positive definite since D (q) is symmetric positive definite. Then differentiating V along solutions of yields: as ˙ D (q, ˙ q) -2 C (q, ˙ q) is skew symmetric. Invoking LaSalle's Principle then shows asymptotic stability of (eq, ˙ eq) =, i.e., shows that the reference signal is asymptotically tracked.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Nonlinear Control", "weight": 1.0} -->

The use of Lyapunov functions in certifying linear controllers' ability to asymptotically track reference signals points to nonlinear controllers, based on Lyapunov functions, that can achieve improved performance. Indeed, to maximize performance on robotic systems it is necessary to exploit the full nonlinear dynamics of the system, which can only be done with nonlinear controllers. These controllers must however be synthesized in a way that yields both theoretical guarantees while also being deployable in practice, i.e., they must be implementable at fast loop rates ( > 1 KHz ). With this in mind, a key attribute of the nonlinear controllers we define next is that they can be expressed as convex optimization problems that can be solved quickly, e.g., linear and quadratic programs.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Nonlinear Control", "weight": 1.0} -->

With the goal of driving the error signal e = (e q, ˙ e q) to zero exponentially, consider a CLF V satisfying: for c, k 1, k 2, λ > 0. Importantly, due to the affine nature of the dynamics, ˙ V is affine in the input u: and can therefore be expressed as a quadratic program (QP) when U = R p: which computes a minimal deviation from the desired feedforward control input uff, t while tracking the reference signal exponentially: et = xt -rt → 0. Importantly, there are many variations of QP-based controllers that are used for real-time control in robotic systems, i.e., those utilizing the dynamics as a constraint and can, therefore, account for constraints on forces and moments in real-time. In all cases, the fact that these are QPs means that they can be implemented in real-time at loop rates of 1 kHz or greater, even on complex robotic systems like walking robots.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Multi-Rate Layered Control Architectures", "weight": 1.0} -->

In LCAs, planning layers typically operate using reduced order models. These are simpler, usually lower dimensional, representations of the components of the full order dynamics of interest, designed to capture essential behavior needed for the control task. As such, reduced order models are often application dependent, and their generation is often heuristic in nature: some of the most common reduced order models used for robotic control are the single integrator, double integrator, and unicycle. These are often leveraged for control synthesis in the context of kinematic models, e.g., for mobile robots. The overarching goal in the design of these reduced order models is the ability to generate reference signals that are (approximately) dynamically feasible and can be tracked well by a real-time feedback controller.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Multi-Rate Layered Control Architectures", "weight": 1.0} -->

This trajectory generation is typically performed over a longer horizon, requiring more computation time: it is therefore natural to view the interplay of trajectory generation and feedback control through the lens of multi-rate layered control architectures i.e., through the lens of LCAs for which the controllers at different layers operate at different frequencies or rates. This can be captured using continuous models (e.g., singular perturbation theory ). Yet in the case of robotic systems it is advantageous to be more concrete about the time scale separations present between layers. One way to explicitly capture this is through the use of discrete time reduced order models at the planning layer, and continuous time full order models at the realtime feedback control layer. An additional advantage of discrete time models at the planning layer is that they can provide an effective means of generating reference trajectories-this discrete instantiation better allows for planning forward in time, e.g., through MPC.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Multi-Rate Layered Control Architectures", "weight": 1.0} -->

To that end, consider a linear discrete time reduced order model that will be used by the trajectory planning layer, where the reduced order model state y ∈ R p and inputs v ∈ R s are typically (but not necessarily) of a lower dimension than full order state x ∈ R n and inputs u ∈ R m, i.e., p ≤ n and s ≤ m. The reduced order state is often related to the full system state via a projection map: π x (x) = y. For robotic systems a commonly used projection is π x (x) = π x (q, ˙ q) = q, i.e., one considers reduced order models on the configuration variables only. Additionally, v ∈ R s is an auxiliary input to the reduced order model that is used to generate a reference signal sent to the real-time controllerwe use v to denote this auxiliary input, as they can often be interpreted as velocity commands. Analogously, we typically require an embedding of the auxiliary input v into the full order dynamics via π v (v) = u. While this subsection focuses on discrete time linear reduced order models, neither feature (discrete time, linear) is essential.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Multi-Rate Layered Control Architectures", "weight": 1.0} -->

In the next subsection Continuous Time LCAs, we explore the use of nonlinear continuous time reduced order models within multi-rate LCAs.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Multi-Rate Layered Control Architectures", "weight": 1.0} -->

Proceeding with the discrete time linear reduced order model, we follow the approach proposed in intermediate subproblem to couple the discrete time reduced order model state y (k) and the underlying continuous time dynamics. As, we model the dynamics of the combined multi-rate LCA composed of a planning layer operating in discrete time with sampling period τ together with the full order control system defined on T: = ⋃ k ∈ N ≥ 0 T k, with T k: = (k τ, (k + 1) τ), as follows: Here the planning layer operates at a slow loop rate, defined by the sampling rate τ, in discrete time on a reduced order model, while the real-time feedback controller operates at a fast time scale (represented by a continuous time evolution). Analogous to the coupling constraints in subproblem, the reduced and full order models are coupled via π x and π v where π v (v (k)) is held constant over the interval (k τ, (k + 1) τ) on which the 'fast' low layer feedback controller operates, and π x (x k τ) is used to update the current state of the reduced order model every discrete step.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Multi-Rate Layered Control Architectures", "weight": 1.0} -->

The goal is to synthesize controllers u and v for the fast and slow dynamics in a synergistic fashion to achieve an overall control objective. In particular, suppose we synthesize a controller, v (k) = v fb (y (k)), that achieves a control objective for the reduced order linear model, i.e., the closed loop system y (k + 1) = Aromy (k) + Bromv fb (y (k)) drives y (k) → yg for a desired goal state yg. The evolution of the discrete time system can also be used to give a set of tracking goals for the real-time feedback controller expressed by the error 4 terms: e k, t = (π x (xt) -y (k + 1)).

<!-- chunk {"id": "body-0077", "role": "body", "section": "Multi-Rate Layered Control Architectures", "weight": 1.0} -->

A controller can be synthesized that ideally drives this error to zero, e.g., a linear controller as in which here takes 4 Note that this causes a discrete jump in the error every discrete step-to avoid this, a smooth function of time rt (k) on T k can be defined such that r k τ (k) = y (k) and r (k + 1) τ (k)(k) = y (k + 1) wherein the error term becomes e k = (π x (x) -r k). This can be achieved by converting the discrete time system y (k + 1) = Aromy (k) + Bromv (k) into a continuous time system ˙ y = A c rom y + B c rom v with v implemented in a sample and hold fashion, i.e., A c rom and B c rom are defined: when the log and inverse are well defined.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Multi-Rate Layered Control Architectures", "weight": 1.0} -->

In the case when they are not, one can assume the discrete time system came from Euler integration, Arom = (I + A c romT) and Brom = B c romT, to obtain A c rom = (Arom -I) / T and B c rom = Brom / T. In either case, the result is therefore a continuous reference signal: Alternatively, the discrete time system can be replaced by a continuous time system at the slow control layer, as was done, to generate a smooth reference signal a priori. or using the Lyapunov controller in with e replaced by e k, t and uff replaced by uff (x (k τ)) for t ∈ T k. The end result is the closed loop multi-rate system: Here the state x k τ at the beginning of the sampling period informs the next iteration of the slow dynamics, while the slow dynamics informs the fast dynamics through the feedforward input (which depends on v fb) and e k, t which drives the system to the next desired setpoint y (k + 1) over the interval T k.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Multi-Rate Layered Control Architectures", "weight": 1.0} -->

To provide a specific example of the generation of closed-loop policies, we begin with slow controller synthesis viewed as a planning problem.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Slow trajectory generation", "weight": 1.0} -->

We view trajectory generation as a planning problem which can be solved using MPC. In particular, consider a goal state yg for the reduced order model, obtained for example from a higher decision layer, with the objective of synthesizing a controller that achieves this objective subject to a safety constraint expressed as state constraints S = { y ∈ R p: h (y) ≥ 0 } and input constraints V, i.e., the system must evolve such that y (k) ∈ S and v (k) ∈ V for all k ≥ 0. To this end, we can formulate a MPC problem resembling that proposed in equation with a N ≥ 1 planning horizon and positive (semi)definite cost matrices Q, QK ⪰ 0 and R ≻ 0 as a QP: with ∥ y ∥ 2 Q = y T Qy. At each discrete time step k ≥ 0, problem is solved to produce a sequence of nominal reduced order model states y ⋆ = y ⋆ (k: k + N) and inputs v ⋆ = v ⋆ (k: k + N -1).

<!-- chunk {"id": "body-0081", "role": "body", "section": "Slow trajectory generation", "weight": 1.0} -->

The planning layer controller is then chosen as v (k) = vMPC (y (k)): = v ⋆ (k), as is the standard approach in MPC.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Fast and safe feedback control", "weight": 1.0} -->

The solution (y ⋆, v ⋆) to each MPC subproblem solved at discrete time step k can further be leveraged to synthesize a lower layer real-time feedback controller. In particular, we can transmit these solutions to the fast lower layer to define the error signal e k, t = (π x (xt) -y ⋆ (k + 1)), which can in turn be driven to zero using the Lyapunov controller (replacing e with e k, t) and using uff (k) = π v (vMPC (y (k))). While this will drive π x (x) → y ⋆ (k + 1)) (the next step produced by the MPC problem) with the input from the MPC problem vMPC (y (k)) as a reference, there is no guarantee that the safety constraints will be satisfied over the time interval T k. To address this shortcoming, we can combine the Lyapunov controller with the CBF controller into an optimization problem that resembles optimization problem.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Fast and safe feedback control", "weight": 1.0} -->

However, in this case we can exploit the control-affine structure of the dynamics to obtain a QP through the use of Lyapunov and barrier functions: with h π x: = h ◦ π x assumed to be a valid CBF: Here p > 0 is a penalty associated with the relaxation term δ > 0, which can be interpreted as an instantaneous analog to the tracking cost that penalizes ∥ x -r ∥ 2 Q. Note that input constraints can also be added to the QP, but this would require a relaxation of the CBF condition or the input constraints to ensure feasibility (see which considers the interplay between continuous and discrete dynamics in the context of input constraints).

<!-- chunk {"id": "body-0084", "role": "body", "section": "Fast and safe feedback control", "weight": 1.0} -->

The solution ufb ( e k, t ) to the QP can be used in the multi-rate dynamics, which when combined with the MPC problem, yields a closed loop multi-rate controller instantiated via a LCA. The power of the closed loop multi-rate LCA, as opposed to a single layer feedback controller using Lyapunov and barrier functions, is that information from the MPC problem encodes knowledge of future system behavior via the reduced order model. Conversely, the fast layer accounts for the full nonlinear dynamics of the system that are not present in the slow layer. Thus, we are able to synthesize a LCA that leverages the nonlinear dynamics of the system at the real-time feedback control layer, while looking ahead to future behaviors defined in the trajectory planning layer, via a synergistic coupling of the two. Formal guarantees for the multi-rate LCA presented here can be found.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Multi-Rate LCAs in Practice", "weight": 1.0} -->

To highlight the practical impact of the multi-rate LCAs we presented, we provide an overview of successful experimental implementations in safe navigation, safe locomotion, and datadriven locomotion. In all cases, a multi-rate LCA facilitates the ability to realize controllers in practice. The commonality of approaches, and architectures more specifically, in these disparate applications on different hardware platforms shows the broad applicability of LCAs for robot control.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Safe Navigation", "weight": 1.0} -->

Consider the problem of safe navigation with a ground robot -in this case, both a wheeled vehicle and a quadruped. Following Example 6, differential flatness of the Dubins' car is utilized to create a linear system that is discretized as in equation. Using this discrete time linear reduced order model, an MPC problem is formulated as in equation, wherein safety is enforced (avoiding obstacles) while planning a path towards a goal. This generates a discrete time reference trajectory that is sent to the Dubins' car and tracked with a realtime controller as in equation. This paradigm is illustrated in Fig. S1. In particular, the discretely updated reference signals are shown (in red) along with the tracking of these reference signals by the real-time controller (in green). Importantly, the input to the Dubins' car model can be viewed as a reference velocity that can be tracked on hardware with onboard controllers. This further layering allows for the experimental deployment on both a wheeled vehicle and a quadruped, as again shown in Fig. S1.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Safe Navigation", "weight": 1.0} -->

FIGURE S1: Experimental demonstration of a multi-rate LCA using the Dubins' car and differential flatness (from ). Reference trajectories are generated with a discrete time linear reduced order model and tracked by the Dubins' car model (top left). Additionally, these signals can be passed to hardware and tracked onboard with real-time controllers, both on a wheeled vehicle (top right) and a quadruped (bottom).

<!-- chunk {"id": "body-0088", "role": "body", "section": "Safe Locomotion", "weight": 1.0} -->

As noted throughout this section, LCAs provide an effective paradigm for enforcing safety constraints on complex robotic systems by enforcing safety (framed as set invariance) at both the planning layer (e.g, in the MPC problem as a state constraint), and at the real-time control layer via a CBF (e.g., as in the QP ). T o demonstrate this, consider the stepping stone problem where the goal is for a legged robot to precisely place its feet on a series of stepping stones. This is safety-critical in that if this foot placement target is missed by the feet, the robot will fall. Additionally, it requires a layered approach, in that the system must maintain safety while also remaining dynamically balanced.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Safe Locomotion", "weight": 1.0} -->

In, a LCA formulation was implemented on a quadrupedal robot (ANYmal) to realize stepping stone behavior experimentally. This is illustrated in Fig. S2. In particular, a safety constraint is implemented at the planning layer via a CBF (via MPC with a kinematic reduced order model), and at the real-time control level (as a CBF constraint in a whole body controller). Implementing CBFs at both layers resulted in no failures (missing the stepping stone) over 140 steps. Without the LCA framework more failures were observed, i.e., just enforcing a CBF constraint at the real-time layer leads to 5 failures, while implementing CBFs at only the planning layer leads to 6 failures. This demonstrates the practical utility of LCAs for safety-critical systems.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Safe Locomotion", "weight": 1.0} -->

FIGURE S2: Experimental demonstration of an LCA (top left) used to realize dynamic walking on stepping stones (from ). This framework was implemented on ANYmal (top right) with the results being walking of the form illustrated (bottom).

<!-- chunk {"id": "body-0091", "role": "body", "section": "Data-Driven Locomotion", "weight": 1.0} -->

Finding reduced order models on which to instantiate multirate control can be challenging, often requiring domain specific knowledge. This can be addressed by learning reduced order models via data-driven methods. To provide an example of this paradigm, consider again the problem of legged locomotion where reduced order models are used at the planning layerthe goal is to learn this model and deploy the learned model experimentally. (continued on next page)

<!-- chunk {"id": "body-0092", "role": "body", "section": "Multi-rate LCAs in Practice", "weight": 1.0} -->

Following, we learn a linear reduced order model at the planning layer and leverage this model to pose an MPC problem. In particular, given sufficiently rich (persistently excited) data collected from the robot, Hankel matrices can be used to exactly determine the forward evolution of linear time invariant systems. Following, given a user defined reduced order model state y ∈ R p and input v ∈ R s, one can define the datadriven state transition matrix G (data) over N-steps: Here, v ini and y ini are the reduced order inputs and state observed in the past over an estimation horizon T ini. Equation (S1), which defines linear relationships between the control input and state over the next N steps,can be used as a constraint in the MPC problem instead of the explicit dynamic constraint y (k + 1) = Aromy (k) + Bromv (k).

<!-- chunk {"id": "body-0093", "role": "body", "section": "Multi-rate LCAs in Practice", "weight": 1.0} -->

This approach was experimentally deployed on a quadruped robot, as shown in Fig. S3. The robot considered has 18 degrees of freedom, and thus the state is 36 dimensional (x ∈ R 36). A reduced order model is considered with a 10 dimensional state y ∈ R 10 consisting of select body positions, velocities, and orientations. The reduced order input v ∈ R 12 consists of ground reaction forces (GRFs). With this reduced order model, data is collected, G (data) is computed and equation (S1) is leveraged in a LCA via an MPC problem at the planning layer, which is subsequently implemented on the robot Example 6 (Running example: robot navigation). Consider again the Dubins' car which, for the moment, we view as the full order dynamics. We aim to instantiate a discrete time planning layer via MPC.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Multi-rate LCAs in Practice", "weight": 1.0} -->

To determine the corresponding reduced order model, we leverage that the dynamics of the Dubins' car ˙ qt = from (qt) ut with q = (x 1, x 2, θ) and u = (u 1, u 2), as given, are differentially flat per Example 5. For the flat output ξ = (x 1, x 2), denote the relationships between the states, inputs and flat outputs: q = q ♭ (ξ, ˙ ξ) and u = u ♭ (ξ, ˙ ξ, ¨ ξ). Note we make a slight deviation from the notation used in Example 5 to be consistent with the configuration space notation defined in this section, and use q to denote the state rather than x.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Multi-rate LCAs in Practice", "weight": 1.0} -->

To apply the approach outlined in this section, we can forward integrate the flat continuous time linear dynamics over the time interval T k = [ k τ, ( k + 1 ) τ ] to obtain via a nonlinear real-time controller similar to. The end result is robust data-driven dynamic walking.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Multi-rate LCAs in Practice", "weight": 1.0} -->

FIGURE S3: Realization of a data-driven LCA on a quadrupedal robot (from). Data is collected from the robot (bottom) to determine the data-driven state transition matrix G (data), which is then used in an MPC problem to plan trajectories (middle). The reduced order model state and input is passed to a nonlinear optimization based controller at the real-time layer to control the robot. The result is dynamic walking (top) that is robust to pushes (a), external pulls (b), rough terrain (c), and natural terrain (d). the discrete time reduced order model Here y (k) = (ξ (k), ˙ ξ (k)) ∈ R 4 and v (k) = ¨ ξ (k) ∈ R 2. We note that here the reduced order model is actually higher dimensional but is 'reduced' in complexity by being linear. Utilizing this system, a feedback controller v fb (y (k)) can be synthesized. For example, this can be chosen to be the result of the MPC problem, i.e., v fb (y (k)) = vMPC (y (k)).

<!-- chunk {"id": "body-0097", "role": "body", "section": "Multi-rate LCAs in Practice", "weight": 1.0} -->

The result is the error e k, t = (qt -q ♭ (y (k + 1))) and a feedforward input uff (y (k)) = u ♭ (y (k), v fb (y (k))). This can be used to synthesize a linear feedback controller of the form, modified slightly to exploit differential flatness, as: for KP a positive definte matrix.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Multi-rate LCAs in Practice", "weight": 1.0} -->

The final feedback controller is given by setting y ( k ) = ( x 1, k τ, x 2, k τ, ˙ x 1, k τ, ˙ x 2, k τ ). This paradigm is deployed ex- perimentally in Multi-Rate LCAs in Practice. Alternatively, in the expression above, we could consider a continuous reference signal e t = ( qt -q ♭ ( yt )) where yt is the solution to given a feedback controller v = Kfb y, i.e., by solving ˙ y = ( A + BKfb ) y with initial condition y ( k τ ) = ( x 1, k τ, x 2, k τ, ˙ x 1, k τ, ˙ x 2, k τ ). This paradigm in deployed experimentally as described in Continuous Time LCAs in Practice, and is discussed in more detail in the next subsection.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Continuous Time LCAs", "weight": 1.0} -->

We observe that we can further layer the control architecture defined in Example 6 by viewing the unicycle as a reduced order model wherein continuous multi-rate control can be applied. That is, we can view µ fb ( e k, t, y ( k )) as a reference velocity (see Example 7 below) which we want a more complex robot to track, i.e., a quadruped or drone as described in Continuous Time LCAs in Practice. The end result is a three layer architecture with two planning layers and one feedback control layer: a slower discrete time planning layer using a linear model, an intermediate reference signal generation layer using a continuous time unicycle model, and a fast feedback control layer for tracking of the reference signal by the underlying complex robotic system. This observation highlights that layers can often be added in a fairly modular fashion, allowing for the benefits of each layer to be enjoyed. This subsection explores the bottom two layers of the LCA described above, namely the interplay between a continuous time reference signal generation layer and a real-time feedback control layer, in more detail. Implicit throughout is the assumption that the loop rates at each layer, and the communication between layers, happens sufficiently fast.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Continuous Time LCAs", "weight": 1.0} -->

We focus on safety-critical systems, wherein safe reference signals are generated by the trajectory generation layer to be tracked by the real-time control layer. We show that formal guarantees of safety can be obtained for these LCAs and, importantly, this architecture enables theory to be widely deployed in practice.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Safe reference signal generation", "weight": 1.0} -->

To that end, consider a continuous time reduced order model where as above, the reduced order dynamics, state yt ∈ R p, and auxiliary input vt ∈ R s, are chosen to be simpler than the full equations of motion, while nevertheless capturing the essential features of the control problem at hand. We recall that we assume that the reduced order state y is related to the full system state x via the projection π x (x) = y, and that the auxiliary input v can be embedded into the full dimensional input space via the embedding π v (v).

<!-- chunk {"id": "body-0102", "role": "body", "section": "Safe reference signal generation", "weight": 1.0} -->

Assume now that the reduced order model is used to generate a desired reduced order state trajectory y d and a corresponding feedback law v d (yt) for the auxiliary input, e.g., via the techniques described in the previous subsection. Now consider the objective of ensuring the reference signal satisfies a safety constraint, encoded by making the set S = { y ∈ R p: h (y) ≥ 0 } forward invariant, for some differentiable function h: R p → R. We can leverage CBFs if h satisfies the CBF condition with respect to the reduced-order dynamics: where α > 0 is a positive constant. 5 If from is affine in the auxiliary control input v this inequality can be expressed as a QP of the form, with the result being a safety filter operating on the reduced order model within the reference signal generating layer: This safety filter can then be integrated into reference signal generation in a variety of ways.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Safe reference signal generation", "weight": 1.0} -->

For example, forward integrating the closed loop dynamics ˙ yt = from (yt, v safe (yt)) to generate a reference signal r y with corresponding error: ey, t = yt -ry, t, which can then be tracked with a linear or nonlinear controller, i.e., replacing e in equation with ey. Alternatively, the safe input v safe can be tracked by the real-time controller as described below.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Real-time feedback control", "weight": 1.0} -->

To provide a concrete example of the use of continuous time reduced order models at the planning layer being coupled with real-time feedback controllers, consider the case when we have a kinematic reduced order model 5 Note that, more generally, α can be chosen to be an extended class K function-we opt for a positive constant for simplicity of exposition with y = q, i.e., our reduced order model operates on the configuration variables, ˙ qt = from (qt, vt), where now the auxiliary input vt is naturally associated with the generalized velocities ˙ qt. Consider a safe velocity, v safe (q), generated from the QP. Following, assume that this velocity is passed to a real-time controller via the error signal ˙ e safe, t: = ˙ qt -v safe (qt), i.e., the real-time controller takes the safe velocity from the reduced order model as a reference with the goal of tracking this reference signal.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Real-time feedback control", "weight": 1.0} -->

Assume a real-time feedback controller ut = ufb (xt, v safe (qt)) that can exponentially track this reference velocity, e.g., via the controller with et replaced by ˙ e safe, t, resulting in exponentially fast tracking: for M, λ > 0, with the error calculated along solutions of the closed loop system: ˙ xt = f (xt) + g (xt) ufb (xt, v safe (qt)). The following theorem adapted from provides formal guarantees for the reduced order model-based LCA applied to the full order dynamics. For experimental implementations related to this formal result, see Continuous Time LCAs in Practice.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Real-time feedback control", "weight": 1.0} -->

Theorem 1. Consider a control system, where x = (q, ˙ q), and a safe set S = { q ∈ Q: h (q) ≥ 0 }. Assume that h has bounded gradient, i.e., there exists K h > 0 s.t. ∥ ∥ ∥ ∂ h ∂ q ∥ ∥ ∥ 2 ≤ Kh for all q ∈ S. Let v safe (q) be the safe velocity given by the QP, with corresponding error ˙ e safe = ˙ q -v safe (q) satisfying. If λ > α, safety is achieved for the full-order dynamics: Note that to certify 'fast-enough' tracking by the realtime controller, a Lyapunov certificate can be used (see Fig. 9): assume the real-time feedback controller tracks the error ˙ e safe per a Lyapunov function as in equation: ˙ V (˙ e safe) ≤ -λ V (˙ e safe).

<!-- chunk {"id": "body-0107", "role": "body", "section": "Real-time feedback control", "weight": 1.0} -->

Then, for any differentiable v safe (q) satisfying the CBF condition, safety for the full-order dynamics is achieved if λ > α: Interestingly, this result is established by synthesizing a CBF for the full system dynamics, hV, using the CBF for the reduced order model, h, together with the Lyapunov function for the tracking controller, V.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Real-time feedback control", "weight": 1.0} -->

Example 7 (Running example: robot navigation). Returning to the running example, we can view the Dubins' car as a reduced order model used to enforce safety constraints on a complex mobile robot, e.g., a quadruped. Recall that the Dubins' car dynamics take the form: ˙ qt = from (qt) ut where q = (x 1, x 2, θ) and u = (u 1, u 2). Consider a barrier function defined on the Dubins' car dynamics aimed at avoiding collisions with obstacles: where d 0 = ∥ (x 1 -x 0 1, x 2 -x 0 2) ∥ with (x 0 1, x 0 2) the position of the obstacle, θ 0 = arctan ((x 0 2 -x 2) / (x 0 1 -x 1)), and κ > 0 a tunable parameter.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Real-time feedback control", "weight": 1.0} -->

Let u d (q) be the feedback controller synthesized in the previous section for tracking a nominal trajectory. Then the safety filter yields a QP on the Dubins' car: where ∥ u ∥ 2 = u T Γ u with Γ = diag (1, R) where R > 0 is a control cost parameter. The result is a reference velocity usafe (q) = (u 1, safe (q), u 2, safe (q)) on the forward velocity and change in heading. These reference signals can be sent to a robot with more complex dynamics as if they were joystick commands. Theorem 1 guarantees safety for the more complex system under the assumption of good tracking.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Discussion", "weight": 1.5} -->

An underlying principle in designing LCAs for robotic systems is to synergistically leverage the strengths at each layer. For example, the lowest layer can handle high dimensional nonlinear systems (e.g., via Lyapunov and barrier functions), yet model uncertainty and 'looking ahead' in nonlinear systems is challenging. Adding a reference signal generation layer that uses continuous time reduced order models mitigates model uncertainty while still yielding formal guarantees, e.g., on safety. Adding a discrete planning layer above the reference signal generating layer allows for longer horizon planning, e.g., via MPC with a discrete time linear reduced order model. Combining these together mitigates the weaknesses at each layer while enjoying their strengths. This use of diverse models, timescales, and control approaches was highlighted through experimental demonstration on a wide variety of robotic systems. We return to the idea of diversity across layers enabling behavior that cannot be achieved by any single layer in Architecture Design as Multi-Criterion Optimization, where we introduce a quantitative notion of a diversity enabled sweet spot in LCAs.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Continuous Time LCAs in Practice", "weight": 1.0} -->

To illustrate the practical consequences of Theorem 1, we highlight how a common reduced order model can be used to achieve safety across a variety of robotic systems, including a drone, quadrupedal robot, manipulator, and full-scale automotive system. This diverse set of robotic systems have very different underlying dynamics, and yet deploying a well designed LCA does not require direct knowledge of these dynamics, rather only 'good' onboard tracking controllers that allow planning layers to operate on reduced order models rather than on the underlying complex system dynamics (as illustrated in Fig. 9).

<!-- chunk {"id": "body-0112", "role": "body", "section": "Drones and Quadrupeds", "weight": 1.0} -->

We wish to enforce collision avoidance to obstacles in the environment. To begin, consider the 'simplest' kinematic model of a robot, a single integrator: obtained by setting yt = qt. Collision avoidance is encoded by the safety constraint S = { q ∈ R n: h (q) ≥ 0 } for Here q 0 ∈ R n is the centroid of the obstacle and r its radius. The safety filter can be expressed as the QP: where v d (q) = -KP (q -qg) is a desired velocity which drives the system to a goal position qg ∈ R n. In the case of planar collision avoidance q, q 0, qg ∈ R 2 (representing the spacial position in the plane)-this is the case that will be considered in the context of the experimental implementation on a drone and quadruped.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Drones and Quadrupeds", "weight": 1.0} -->

FIGURE S1: Experimental results on a drone and quadruped (from ). Both the drone and quadruped use a single integrator ( S1 ) reduced order model and the corresponding QP ( S2 ). Suitable integration into an LCA yields safe behavior. Additionally, a unicycle (Dubins' car) model is used on the quadruped to also achieve safe behavior that is less conservative.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Drones and Quadrupeds", "weight": 1.0} -->

The result of ( S2 ) is a safe velocity vsafe ( q ) that can be tracking with existing onboard tracking controllers. This was implemented on both a drone and a quadruped hardware platform. We highlight that while these platforms have dramatically different underlying dynamics, by leveraging a well designed LCA, the exact same safe reference velocity, vsafe ( q ) can be used and tracked on both platforms. The results can be seen in Fig. S1: safety is achieved (as certified by h ( q ) ≥ 0) for both the drone and quadruped tracking reference signals vsafe ( q ) produced by ( S2 ). For the quadruped, we can also use the Dubins' car as a reduced order model instead of the single integrator, as described in Example 7. In this case, the resulting safe velocity usafe ( q ) produced by the QP is tracked as a reference signal. The resulting behavior is again safe, but is less conservative due to the Dubins' car being a better representation of the movement of the quadruped in the plane, i.e., a better reduced order model produces less conservative behavior while still maintaining safety.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Manipulators", "weight": 1.0} -->

Consider a robot manipulator, as illustrated in Fig. S2. The control task is to achieve collision free behavior between the robot and environment while accomplishing a task (in this case, flipping a burger). Importantly, there is no access to the proprietary onboard real-time controllers of the commercial robot arm, and therefore safety must be achieved through a LCA.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Manipulators", "weight": 1.0} -->

Let A (q) ⊂ R 3 be the set of all points on the robot (which depends on the configuration of the robot q ∈ R n) and B ⊂ R 3 be the set of all points in the environment. Collision free behavior between the robot and environment, captured by A (q) ∩ B = ∅ or A (q) ⊂ B with B the complement of B, is encoded by a barrier function S = { q ∈ R n: sd AB (q) ≥ 0 } defined in terms of the signed distance: The advantage of using the signed distance, as opposed to the distance, is that the addition of the 'penetration' term which gives a negative value when this occurs-as opposed to the distance which is strictly non-negative. This negative value allows for convergence back to the safe set S per the fact that CBFs render S attractive.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Manipulators", "weight": 1.0} -->

The challenge with using the signed distance as a barrier function is that it is discontinuous on a set of measure zero. To accommodate for the discontinuities, consider: which decomposes sd AB (q) into its differentiable and nondifferentiable component, where the gradient of the nondifferentiable component, δ, is viewed as a disturbance that is non-smooth on a set of measure zero; as a result, we can design a controller that is robust to adversarial disturbances of magnitude matching the essential supremum ∥ δ ∥ ∞ = esssup t ≥ 0 ∥ δ (qt) ∥.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Continuous Time LCAs in Practice", "weight": 1.0} -->

For the reduced order model, we consider a kinematic model of the robot arm (S1), i.e., ˙ qt = vt with qt ∈ R n for n the number of degrees of freedom (in this case, n = 6). To enforce a safety filter on the reduced order model, the goal is to leverage a QP of the form. Yet in this case, due to the fact that the signed distance is not continuously differentiable, we leverage the decomposition in (S4) to obtain the QP: with ˙ q max = ∥ ˙ q ∥ ∞, and ∥ δ ∥ ∞ defined as above. Here, vd (q) is obtained from a series of preplanned trajectories that must be executed while avoiding collisions, i.e., vd (q) = KP (q i d -q) with q i d the next waypoint (in time) of the preplanned trajectory.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Continuous Time LCAs in Practice", "weight": 1.0} -->

The QP in ( S5 ) was implemented experimentally on FANUC robotic manipulator in a kitchen scenario, i.e., the robot was required to do a variety of cooking related tasks while avoiding collisions with the environment. As illustrated in Fig. S2, the robot was able to perform a variety of complex tasks while maintaining safety h ( q ) = sd AB ( q ) ≥ 0.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Continuous Time LCAs in Practice", "weight": 1.0} -->

FIGURE S2: Achieving safety on a robot manipulator (from ). The manipulator executes a series of preplanned trajectories, and a safety filter is intantiated via a reduced order model to prevent collisions with the environment. The value of the barrier function is shown, wherein non-negative values imply collision free behavior.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Automotive Systems", "weight": 1.0} -->

For complex real-world applications, domain specific reduced models are needed. Additionally, as in the application to manipulators, real-world settings also require extended notions of safety to account for differences between the reduced and full order dynamics.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Automotive Systems", "weight": 1.0} -->

To provide an example of this, consider adaptive cruise control (ACC) where the control objective is to achieve a desired speed subject to maintaining a safe distance from a lead car. In this setting, consider a reduced order model defined by a point-mass model of a vehicle moving in a straight line: where y 1 (in m) is the position, y 2 = ˙ y 1 (in m / s) the velocity, m is the mass of the car (in kg), the input u (in Newtons) represents the wheel force, Fw, and Fr is the rolling resistance; typically, c 0, c 1 and c 2 are determined empirically. Finally, z is the distance between the vehicles, wherein it is assumed that the lead vehicle is traveling at a constant speed v 0.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Automotive Systems", "weight": 1.0} -->

The key safety constraint is 'keep a safe distance from the car in front of you.' This is generally encoded by the 'half the speedometer' rule which states that D ≥ v 2 (with D in m and v in km / hr), i.e., the distance between the two vehicles should be at least half the current speed. Converting this to m and s results in the safety constraint, z ≥ 1. 8 y 2, which can be translated to a barrier function h (y, z) = z -1. 8 y 2 ≥ 0. It is easy to verify that this is a valid CBF and can be implemented in practice, but we will consider the generalization: for which the parameters, ai, can be determined such that z ≥ 1. 8 y 2 is satisfied while allowing for actuation limits and other practical considerations to be enforced.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Automotive Systems", "weight": 1.0} -->

Let v d (y) be the 'nominal' ACC system, i.e., the current algorithm on the vehicle, that drives the velocity y 2 → vg. We can then instantiate a safety filter in the form of a QP: The added term ϵ (h (y)) is a 'tunable' term that enforces a generalization of input-to-state safety termed tunable inputto-state safety. Here ϵ is a function that can be tuned and must have a positive derivative; we pick ϵ (h (y)) = ϵ 0 e β h (y). The safety filter (S6) was implemented on a class-8 truck without a trailer. As shown in Fig. S3, the nominal ACC controller v d results in a safety violation and, in fact, a collision. Using the safety filter on this nominal controller results in safe system behavior.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Automotive Systems", "weight": 1.0} -->

FIGURE S3: Safety filter implemented on a full-scale truck. Shown is the nominal controller v d which violates the safety condition (bottom). When the safety filter (S6) is implemented safety is achieved (top) The success of LCAs in robotic systems, and the ability to add and remove layers as needed, points to the power of these methods. It also conveys their complexity-different models at different layers, and the interfacing between these models, results in complex and notationally intensive mathematical models, and makes establishing formal guarantees becomes daunting. Yet the fact that these approaches work in practice, and are widely understood as the 'way to control robots,' points to the value in formalizing and analyzing LCAs. It can be argued that this is a central challenge for the control community moving forward: going beyond homogeneous system models, and analyzing heterogeneous models interacting within an LCA.

<!-- chunk {"id": "body-0126", "role": "body", "section": "PART 2.1: ARCHITECTURE DESIGN AS MULTI-CRITERION OPTIMIZATION", "weight": 1.0} -->

The previous sections illustrate how an LCA can be naturally derived from a global decision and control problem, and provide a concrete instantiation of these ideas in the context of robotic systems. These results highlight both the power of LCAs, as well as the art and complexity involved in designing them. We highlight that many idealized assumptions were made in Part 1: we assumed that the control system hardware was already fixed, that we knew how many layers were needed, what each layer should do, and how layers should interact within the LCA. In this section, which marks the start of Part 2 of the paper, we try to address some of these idealized assumptions, and propose a framework rooted in multi-criterion optimization for quantitative reasoning about architecture design choices such those described in the previous two sections. A key theme that we explore in this section is that while each layer may be subject to specific constraints and tradeoffs, by leveraging diversity across layers, these tradeoffs can be mitigated to yield high-performing LCAs such as those highlighted in the previous sections.

<!-- chunk {"id": "body-0127", "role": "body", "section": "PART 2.1: ARCHITECTURE DESIGN AS MULTI-CRITERION OPTIMIZATION", "weight": 1.0} -->

We begin with a familiar illustrative example: longdistance travel. We consider three possible 'travel layers,' namely air travel (implemented via aircraft and airports), public transit (implemented via busses and bus stops), and walking (implemented via human sensorimotor control). Each of these travel layers are subject to speed-accuracy tradeoffs, which are themselves a function of architectural design choices (but we will not focus on these here): air travel is fast but inaccurate since we can only fly between airports, public transit is moderately fast and moderately accurate as we are limited to bus stops, and walking is slow but extremely accurate. These travel layers can be placed in a speed/accuracy plot as shown in Fig. 13.

<!-- chunk {"id": "body-0128", "role": "body", "section": "PART 2.1: ARCHITECTURE DESIGN AS MULTI-CRITERION OPTIMIZATION", "weight": 1.0} -->

However, as we all know, when traveling long distances, it is most efficient to appropriately combine these travel layers: we walk to the bus stop, take the bus to FIGURE 13: Each individual 'travel layer' is subject to speed/accuracy tradeoffs, but combining them appropriately in an LCA enables an overall transportation system with minimal tradeoffs in either speed or accuracy. the airport, fly to the nearest airport to our destination, take the bus to the stop nearest our destination, and then walk to our destination. Although not usually thought of in this way, this is an LCA for travel, with air travel serving as a fast but inaccurate layer, public transit serving as an intermediate layer, and walking as a slow but accurate layer. The resulting LCA, which implements diverse layers using diverse components, is nearly as fast as flying, and just as accurate as walking. We call such an LCA that leads to minimal tradeoffs between speed and accuracy an architectural sweet spot.

<!-- chunk {"id": "body-0129", "role": "body", "section": "PART 2.1: ARCHITECTURE DESIGN AS MULTI-CRITERION OPTIMIZATION", "weight": 1.0} -->

It is our claim that such sweet spots are ubiquitously enabled through diverse layers 6 being appropriately combined in LCAs. Indeed, we see comparable diversity in sensorimotor control, robotics, computer networks, and biology, in order to mitigate what appears to be a universal constraint on individual layers, namely that the lower the layer in the 'stack,' the faster it must operate, but the more limited it is in its capabilities. Nevertheless, by appropriately combining slow decision making with moderate speed trajectory generation and fast feedback control, we are able to design autonomous systems that are as flexible as the decision making layer, and as accurate and fast as the feedback layer. In the remainder of this section, we propose a quantitative framework for reasoning about such Diversity enabled Sweet Spots (DeSS).

<!-- chunk {"id": "body-0130", "role": "body", "section": "PART 2.1: ARCHITECTURE DESIGN AS MULTI-CRITERION OPTIMIZATION", "weight": 1.0} -->

6 Diverse layers typically require diverse hardware, or levels. We discuss levels in more detail in Key Concepts in Control Architecture.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Pareto Surfaces and Pareto Minimax Points", "weight": 1.0} -->

Our goal is to both characterize the fundamental tradeoffs that different control architectures induce, and to determine whether a control architecture enjoys a (diversity enabled) sweet spot. To formalize these concepts, we turn to multi-criterion optimization.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Multi-criterion optimization", "weight": 1.0} -->

Multi-criterion optimization problems seek to minimize a vector-valued objective function. Following [68, Ch. 4], we consider a vector-optimization problem which seeks to minimize the vector-valued objective with respect to the positive orthant R d +. Such an optimization problem should be interpreted as having d different objectives Ci, each of which we would like to make small.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Multi-criterion optimization", "weight": 1.0} -->

In contrast to scalar-valued objectives, we must take care in defining appropriate notions of optimality. In particular, we may define both optimal and Pareto optimal points. A feasible point x ⋆ is optimal if it is unambiguously better than any other feasible point, where better is defined in terms of the partial order induced by the positive orthant, i.e., a feasible x ⋆ is optimal if for any other feasible y, C ( x ⋆ ) ⪯ C ( y ), i.e., if Ci ( x ⋆ ) ≤ Ci ( y ) for all i = 1,..., d. Most engineering design problems are subject to fundamental tradeoffs between optimization criteria Ci, and such an optimal point typically does not exist. Instead, a family of Pareto optimal points can be defined, wherein a feasible point x po is Pareto optimal if for any feasible y, if C ( y ) ⪯ C ( x po ), then C ( y ) = C ( x po ), i.e., a feasible point x po is Pareto optimal if no other point exists that is unambiguously better.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Multi-criterion optimization", "weight": 1.0} -->

Indeed, the existence of multiple Pareto optimal points imply that there is a fundamental tradeoff between the different objectives.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Multi-criterion optimization", "weight": 1.0} -->

The standard approach to solving such a multi-criterion optimization problem is via scalarization. A common approach to scalarization is to take a weighted sum of the objectives, i.e., for λ ∈ R d ++, define the scalarized objective C λ ( x ) = λ T C ( x ) = ∑ d i = 1 λ i Ci ( x ). By sweeping over weighting parameters λ ≻ 0, we obtain a family of Pareto optimal points x po ( λ ), which in turn defines a Pareto surface ( C 1 ( x po ( λ )),..., Cd ( x po ( λ ))) ⊂ R d. 7 An alternative, but also important, scalarization approach is to consider minimizing the the maximum of the objectives, i.e., C max ( x ) = max { C 1 ( x ),..., Cq ( x ) }. The resulting solution x mm is called the minimax Pareto optimal point.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Multi-criterion optimization", "weight": 1.0} -->

A familiar example of bi-criterion optimization in control is LQR optimal control. Indeed, defining the vector-valued objective ( ∑ N k = 0 ∥ x ( k ) ∥ 2 2, ∑ N -1 k = 0 ∥ u ( k ) ∥ 2 2 ), we recognize the LQR objective ∑ N -1 k = 0 ∥ x ( k ) ∥ 2 2 + ρ ∥ u ( k ) ∥ 2 2 + ∥ x ( N ) ∥ 2 2 as a scalarization of the competing objectives of small state and control cost. An alternative, albeit less common, scalarization would be to consider the maximum objective max { ∑ N k = 0 ∥ x ( k ) ∥ 2 2, ∑ N -1 k = 0 ∥ u ( k ) ∥ 2 2 }. See Fig. 14 for an example of a typical Pareto curve for an LQR problem.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Sweet Spots are Nearly Optimal Points", "weight": 1.0} -->

We now have the required concepts to formally define a sweet spot. Intuitively, a sweet spot is a point on the Pareto surface that is nearly optimal. We quantify this notion of near optimality by defining a σ -sweet-spot to be a minimax Pareto optimal point that is σ away from being an optimal point in the following sense: In words, the measure σ characterizes the biggest loss in optimality in any of the criterion Ci of a minimax Pareto optimal point relative to any other Pareto optimal point. Note that if there exists an optimal point x ⋆ then σ = 0, and that σ increases as the tradeoff between objectives becomes more severe. See Fig. 15 for a qualitative illustration of when σ is small or large as a function of the geometry of the Pareto surface.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Diversity Enables σ -Sweet-Spots", "weight": 1.0} -->

One of our key claims, which is broadly supported by examples in engineering, science, and biology, is that diversity enables nearly optimal sweet-spots, despite individual layers being subject to strict and at time severe tradeoffs. We begin with a simple stylized example for which the sub-optimality measure σ can be computed exactly. We then explore A Case Study in Sensorimotor Control in the next section.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Diversity Enables σ -Sweet-Spots", "weight": 1.0} -->

7 Up to boundary points, such an approach is guaranteed to recover all Pareto optimal points if the objective functions Ci are convex in x, see [68, Ch. 4].

<!-- chunk {"id": "body-0140", "role": "body", "section": "Diversity Enables σ -Sweet-Spots", "weight": 1.0} -->

Illustrative Example: Bi-Criterion Least-Squares We study the bi-criterion least-squares problem through the lens of DeSS. We assume that b 1, b 2 ∈ R m A 1, A 2 ∈ R m × 2 m, and x ∈ R 2 m. Our stylized architecture design problem is to design the matrices A 1 and A 2 by selecting their rows, possibly with replacement, from a palette of 2 m linearly independent rows V = { v 1,..., v 2 m } ⊂ R 2 m. Our goal is to quantify how diversity in the row-spaces of A 1 and A 2 affects the resulting σ -sweetspot of the bi-criterion problem.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Diversity Enables σ -Sweet-Spots", "weight": 1.0} -->

- » If we assume that the we design A 1 and A 2 to each respectively have full row rank, then it is clear that each individual objective can be made 0. We make this assumption going forward, and hence we have σ = max {∥ A 1 x mm -b 1 ∥ 2 2, ∥ A 2 x mm -b 2 ∥ 2 2 }. - » If we further assume that the stacked matrix ¯ A = [A T 1, A T 2] T has full row rank, i.e., that A 1 and A 2 do not share any rows selected from V, then σ = 0. This is easily verified by setting x mm = ¯ A -1 ¯ b, with ¯ b = (b 1, b 2).

<!-- chunk {"id": "body-0142", "role": "body", "section": "Diversity Enables σ -Sweet-Spots", "weight": 1.0} -->

Thus, our remaining task is to characterize the σ -sweetspot for optimization problem when A 1 and A 2 share a common row space. Towards that end, we consider the minimax scalarization: and its dual (see Appendix A for details): This allows us to immediately reconfirm that σ = 0 if A 1 and A 2 do not share any rows, as in this case any dual feasible solution has µ 1 = µ 2 = 0. Similarly, when A 1 = A 2, a simple argument shows that σ = 1/4 ∥ b 1 -b 2 ∥ 2 2. A generalization of this argument is presented in the next theorem, proved in the Appendix, which allows us to characterize the solution when A 1 and A 2 share k rows.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Diversity Enables σ -Sweet-Spots", "weight": 1.0} -->

Theorem 2. Consider the bi-criterion least-squares problem. Suppose that A 1 and A 2 are both full row-rank, and assume without loss of generality, reordering rows in Ai and elements in bi if necessary, that A 1 and A 2 share their first k rows. Then the minimax solution x mm to the scalarized problem defines a ( 1 4 ∥ E T k ( b 1 -b 2 ) ∥ 2 2 ) -sweetspot, as defined in equation. Here, E k = [ e 1,..., e k ] with e i ∈ R m the standard basis elements.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Diversity Enables σ -Sweet-Spots", "weight": 1.0} -->

Theorem 2 makes clear that the more diverse the matrices A 1 and A 2, i.e., the smaller the number of shared rows k, the less severe the tradeoff; similarly, the less diverse the matrices A 1 and A 2, i.e., the larger the number of shared rows k, the more severe the tradeoff. We compute a family of the resulting Pareto curves and minimax optimal points for m = 5 in Fig. 16a, and plot the evolution of the suboptimality measure σ as a function of the number of shared rows in Fig. 16b. Parameters are randomly generated so as to ensure the requisite linear independence conditions, and such that | ( b 1 -b 2 ) i | is approximately even for all i: details of how the parameters are generated can be found in the Appendix, and the code used to create these plots can be found here.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Diversity Enables σ -Sweet-Spots", "weight": 1.0} -->

To further gain insight into the LCA design problem, let us view A 1 and A 2 as defining two layers, with layer i aimed at addressing control subtask bi. This analogy FIGURE 16: Increased diversity in row spaces provably leads to less severe tradeoffs, as quantified by a smaller suboptimality measure σ, in the bi-criterion least-squares problem.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Diversity Enables σ -Sweet-Spots", "weight": 1.0} -->

(a) We observe how the Pareto surface for the bicriterion least-squares problem becomes increasingly unfavorable as we decrease the diversity across A 1 and A 2. This is true both in terms of the overall Pareto surface, as well as the sub-optimality measure σ.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Diversity Enables σ -Sweet-Spots", "weight": 1.0} -->

(b) We plot the sub-optimality measure σ as a function of shared rows across A 1 and A 2 for the bi-criterion least-squares problem. We observe that σ deteriorates as we decrease diversity across A 1 and A 2. reinforces that diversity is not enough to ensure a small sub-optimality measure σ: the control subtasks, here characterized by b 1 and b 2, must themselves also be compatible with system diversity (or lack thereof). For example, even if k = 1, a very large (e T 1 (b 1 -b 2)) 2 will nevertheless lead to a severe tradeoff between optimizing the two objectives, resulting in a large σ. Conversely, diversity is only needed in A 1 and A 2 if the control subtasks b 1 and b 2 are also diverse: if b 1 = b 2 then A 1 = A 2 will still yield σ = 0. Connecting this back to the travel example, if a destination is just a block away, then diversity is not required, and just walking is an optimal travel LCA. Conversely, if the destination is extremely remote, then the three layers of commercial air travel, public transit, and walking will still be very slow.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Diversity Enables σ -Sweet-Spots", "weight": 1.0} -->

Thus this simple example hints at an explanation as to why diverse layers are needed by systems that must accomplish diverse tasks across diverse environments at diverse spatiotemporal resolutions. We explore a (still stylized) control problem in the next subsection that further reinforces this concept.

<!-- chunk {"id": "body-0149", "role": "body", "section": "PART 2.2: A CASE STUDY IN SENSORIMOTOR CONTROL", "weight": 1.0} -->

We adapt the following from Nakahira et al. and Nakahira et al.. Our goal in this section is to highlight how diverse layers, and the diverse hardware used to implement them, in the human sensorimotor LCA (see Fig. 18) enable astonishingly efficient DeSS in spite of severe speed/accuracy tradeoffs. To that end, we first derive robust performance limits for a simplified model of sensorimotor control subject to communication that is delayed and quantized due to its implementation using physiological hardware composed of axons. We then identify a simple layered architecture composed of delayed but accurate vision (planning) and fast but inaccurate reflex control (feedback) layers, and show that this architecture is optimal for the aforementioned sensorimotor control model, and leads to a DeSS. Finally, we show that despite the simplicity of the model and analysis, it is shockingly predictive of real-world behavior as confirmed in Experimental Validation in a Biking Simulator.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Simplified Model", "weight": 1.0} -->

Consider an initial minimal model with discrete time dynamics A schematic for this model is shown in Fig. 17, where we use P to denote the plant defined by equation. The where x (k) ∈ R is the state, w (k) ∈ R is the disturbance, u (k) ∈ R is the control action generated by the controller K, and Q: R → S R, for S R ⊂ R a finite set of cardinality 2 R, is a quantizer that limits communication between the controller and the actuator to R bits/sampling interval. The form of the control law in system implies that the controller is Full Information (FI), as the control signal u (k) is allowed to depend on all current and past states x (0: k), current and past disturbances w (0: k) and past control actions u (0: k -1).

<!-- chunk {"id": "body-0151", "role": "body", "section": "Simplified Model", "weight": 1.0} -->

The robust control problem can then be posed as where Q R is the space of control laws defined by the pair of mappings (K, Q), with Q constrained to be a static memoryless quantizer of rate R, i.e., Q: R → S R. This cost function is standard in L 1 robust control, except that a communication channel C, composed of a quantizer Q and a delay Tu, is inserted into the feedback loop. Perhaps surprisingly, this problem formulation still allows for a simple and intuitive analytic solution. Indeed, without quantization or delay, the control law ensures that x (k + 1) = 0. Thus any errors in the state is a direct consequences of quantization and/or delay, or to saturation of the control signal u.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Simplified Model", "weight": 1.0} -->

8 We assume that the channel C is memoryless and stationary with rate R, allowing us to restrict the quantizer Q to be memoryless and static as well. Generalizations that lift this assumption can be found.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Fundamental Limits due to Delay and Quantization", "weight": 1.0} -->

In this subsection, we provide an exact solution to the robust control problem for fixed advanced warning Tw and actuation delay Tu. In particular, we show that the worst-case state deviation can be expressed as a function of the plant pole a, the channel rate R, and the net delay of the system T: = Tu -Tw. The achievable performance takes a different form depending on the net delay regime that the system is operating under. When the net delay T is positive ( T > 0), this corresponds to a system in which the control action u ( k ) can only affect the plant T sampling intervals after the disturbance w ( k ) affects the state. Conversely, when the net delay T is non-positive ( T ≤ 0), this corresponds to a system in which there is advanced warning of the disturbance, allowing the controller to act in advance. These two qualitatively different cases are treated separately. We then use these insights in the next section to pose a LCA design problem that seeks to identify an appropriate combination of fast but inaccurate and slow but accurate neural signaling to enable a DeSS.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Fundamental Limits due to Delay and Quantization", "weight": 1.0} -->

Theorem 3. Suppose that | a | < 2 R. Then the minimal state deviation achievable in robust control problem is Conversely, if | a | ≥ 2 R, then the system cannot be stabilized, and the optimal value to optimization problem is infinite.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Fundamental Limits due to Delay and Quantization", "weight": 1.0} -->

The performance limits are remarkably simple and intuitive. The net warning case ( T ≤ 0) has only one term due to quantization, with the stabilizability condition | a | < 2 R well-known from the networked control system literature. With no dynamics ( a = 0) this reduces to a trivial rate distortion theorem with error 2 -R. The net delayed case ( T < 0) is more interesting, with the first term due to the delay alone, and the second term an additional contribution due to quantization. As expected, both grow rapidly with increased net delay T and unstable a > 1, for reasons familiar and intuitive.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Speed Accuracy Tradeoffs in Neural Signaling", "weight": 1.0} -->

We now add a tradeoff between temporal and spatial resolution in neural signaling to our model via the net delay T and data rate R. We believe this is the first important constraint in explaining the extreme heterogeneity found in the nervous system, and is analogous to the speed/accuracy tradeoff highlighted in the travel example above. The nervous system communicates between components and the body with a variety of nerves, which are bundles of axons. Axons are the wiring by which spiking neurons communicate long range using action potentials, and it is possible to derive some rough tradeoffs from wellknown physiology. Fig. 18 shows some of the tremendous diversity of axon numbers and sizes among the cranial and peripheral nerves. We argue that much of this arises due to hard constraints on speed versus accuracy.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Speed Accuracy Tradeoffs in Neural Signaling", "weight": 1.0} -->

We suppose that our channel C (see Fig. 17) is a single nerve with uniform signaling delay Ts, and assume that the total delay Tu is the sum Tu = Ts + Tc with an additional fixed delay Tc due to grey matter computation and other communications. Initially we assume that Tc is fixed and given, and that Ts is variable and depends on the nerve composition, as in Fig. 18. Following the arguments provided, we use the physiologically plausible yet remarkably simple relationship between data rate R and signalling delay Ts: where λα is a resource measure that scales with the axon area α.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Speed Accuracy Tradeoffs in Neural Signaling", "weight": 1.0} -->

Next we explore the surprisingly rich consequences of the constraint R = λα Ts on our minimal model of sensorimotor control using Theorem 3. For simplicity, we write λ from now on as the resource dependence is understood. One can verify that if R = λ Ts and Tu: = Ts + Tc, then the optimal optimal performance specified in Theorem 3 becomes Fig. 19 shows the system performance when varying delay Ts (and thus channel rate R) for Tc = Tw = 0 and a fixed resource level α. Increased delay increases the delay error term sup ∥ w ∥ ∞ ≤ 1 ∥ x d ∥ ∞: = ∑ T i = 1 | a i -1 | but reduces the quantization error term sup ∥ w ∥ ∞ ≤ 1 ∥ xq ∥ ∞: = (2 λ Ts - | a |) -1. Consequently, the optimal system level performance is achieved at intermediate levels of delay and channel rate. Because of the exponential dependence there is no analytic formula for the optimum, but the error is convex and the minimum easily found numerically. Next we consider in more detail the consequences of these formulas by varying the additional delays and plotting the resulting optimal errors, bits, and delay.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Speed Accuracy Tradeoffs in Neural Signaling", "weight": 1.0} -->

Fig. 20 shows the optimal delays Ts (and resulting net delay T ) and channel rate R = λ Ts that achieves the minimum total error when varying Tw ≥ 0 and Tc ≥ 0 separately in the two special cases (i) T = Tu -Tw ≤ 0 (warned) and (ii) T = Ts + Tc > 0 (delayed). What results are clearly two distinct regimes with distinct physiology. When the computation delay Tc is greater than 0, the system has a net delay T and the delay cost increasingly dominates the total cost, leading to both the data rate R and signaling delay Ts becoming constant (i.e., suggesting axons of a large and constant radius ρ ), independent of Tc. This corresponds to the reflexes on the right half of Fig. 18 with nerves having relatively few large axonsthese are the physiological analogs to aircraft and airports from our travel example. The total error, due mostly to delay, can be much larger than the disturbance.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Speed Accuracy Tradeoffs in Neural Signaling", "weight": 1.0} -->

Concretely, in running or cycling on rough terrain or through heavy traffic, a relatively small but well placed perturbation to the foot or wheel can be amplified into a crash, even a fatal one-this effect gets worse at high speeds when the delay is relatively larger. Our nervous system invests in large nerves, axons, and muscles to avoid such crashes, consistent with the theory.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Speed Accuracy Tradeoffs in Neural Signaling", "weight": 1.0} -->

With increasing advanced warning Tw > 0 the net delay T becomes non-positive, and in this case the errors due to quantization increasingly dominate the total cost. Further, this total cost goes to zero as Tw increases, exactly the opposite of the delayed case. Further, as the advanced warning Tw increases, so does the data rate R, and consequently the axon radius ρ decreases (as α ≈ π R ρ 2 is fixed). This corresponds to the left side of Fig. 18 with many relatively small axons-these are the physiological analogs to walking in our travel example. In running or cycling we can start with huge errors to remotely located objects, and given enough time drive them to zero. Here we are limited largely by the resolution of our vision in accurately locating the object, again consistent with the theory.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Speed Accuracy Tradeoffs in Neural Signaling", "weight": 1.0} -->

Thus we have an extremely simple model that connects the high layer requirements of advanced warning and planning (e.g. as enabled by vision) to the low layer control implemented by fast reflexes. In the sequel we explore further aspects of this model, and introduce additional constraints and generalizations.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Minimal LCA", "weight": 1.0} -->

One of the most important features of a visual system is its distributed nature, in which sensors, actuators, and computational components are interconnected via sparse communication. Fig. 21 sketches a minimal model of this kind that is composed of two copies of each component in Fig. 17. The plant dynamics are given by x ( k + 1 ) = ax ( k ) + u ( k ) + w ( k ) except the disturbance is now composed of two terms w ( k ) = v ( k ) + r ( k -Tr ), as is the control action u ( k ) = uL ( k -TL ) + uH ( k -TH ), each generated by their own sensors, computing, and communication components.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Minimal LCA", "weight": 1.0} -->

Visual trajectory planning is done through the control loop involving QH which is responsible for tracking, via the control signal uH ( k ), a visual target whose change in position is captured by r. We assume a very simplified view of vision whereby remote (in space) sensing means that r ( k ) is seen but it takes Tr for the disturbance to arrive, effectively creating an advanced warning of Tr, though the physical details are all causal.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Minimal LCA", "weight": 1.0} -->

On the other hand, local (reflex) compensation is done through the control loop involving QL. Disturbances such as those caused by body and head motion are captured by v, and are sensed directly by the Vestibular Occular Reflex (VOR), which computes a control action uL ( k ) to compensate. The control commands ( uH ( k ), uL ( k )) from both loops are sent to the plant through different signaling pathways, modeled by channels with rates RH and RL and delays TH and TL, respectively, after which their gains are summed to produced the final previously described control action u ( k ) = uL ( k -TL ) + uH ( k -TH ). Connecting this LCA back to the formalism introduced in Layered Control Architectures via Optimal Control Decomposition and Layered Control Architectures for Robotic Systems, we immediately recognize uH as a feedforward control term computed at the planning layer which provides advanced warning of the coming reference position r, and uL as a feedback control term, computed at the feedback control layer and executing in near real-time to compensate for unforeseen disturbances v.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Minimal LCA", "weight": 1.0} -->

Using the tradeoff in both signaling pathways, and bounding ∥ v ∥ ∞ and ∥ r ∥ ∞ from above by 1 and δ, respectively, the optimal performance is then given by This result follows by noting that the total system can be decomposed into two independent subsystems, corresponding to the QH and QL loops, and thus so can its performance. The first subsystem is a delayed system driven by v and controlled by u L, while the second subsystem is a warned system driven by r and controlled by u H. From our previous analysis, it is expected that the first system achieves better performance when its nerves are composed of a few large and fast axons, whereas the second system achieves better performance when its nerves are composed of many small and slow axons. This phenomena can be indeed observed in the real visual systems. Specifically, the optic nerve has approximately 1M axons of mean diameter 0.64 µ m with CV 0.46 µ m, while the 20K vestibular axons have mean diameter 2.88 µ m with CV 0.41, significantly larger and less numerous and slightly less variable.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Minimal LCA", "weight": 1.0} -->

We conclude by emphasizing that a key enabler for DeSS is diversity in hardware used to implement diverse layers to address diverse system tasks. For example, in the biking example discussed in Experimental Validation in a Biking Simulator, if the trail planning layer had to update the nominal trajectory faster than vision could handle, the LCA would fail to enable a DeSS. It is this multi-rate nature of control tasks, characterized by local fast corrections and global slow updates, and which seems to be ubiquitous across engineered and natural complex systems, that allows for corresponding multi-rate LCAs to be designed that enable DeSS. Developing a general quantitative design framework for multi-rate LCAs that enable DeSS is arguably the most important open problem in engineering today, and one that control theorists are particularly well-suited to tackle.

<!-- chunk {"id": "body-0168", "role": "body", "section": "PART 3: KEY CONCEPTS IN CONTROL ARCHITECTURE", "weight": 1.0} -->

In Parts 1 and 2, we introduced two concepts core to LCAs, namely layers and DeSS, and proposed quantitative frameworks for their analysis and design. In this final part and section, which should be viewed as a glossary of LCA terminology, we highlight that these are but a subset of the components that can be universally found in LCAs across domains. Although we do not have quantitative techniques for reasoning about them, we present qualitative descriptions, and illustrate their importance using various case-studies.

<!-- chunk {"id": "body-0169", "role": "body", "section": "PART 3: KEY CONCEPTS IN CONTROL ARCHITECTURE", "weight": 1.0} -->

Table 1 illustrates concepts we believe essential to the study of universal control architectures in the context of three familiar examples: Clothing, Sensorimotor Control, and the Power-Grid. We also indulge in a more fanciful digression that frames Lego as a Layered Control Architecture. These were introduced and developed, and conceptually underpin much of the previous discussion. Levels. Conceptually, levels can be thought of as the (usually physical) substrates or components used to implement a system. All complex systems have many levels or scales: for example, in biology, levels range from molecules to synapses, cells, circuits, systems, and organisms. Analogous levels can be identified in familiar engineered systems. For example, in circuits, levels range from atoms to wires, resistors, capacitors, transistors, to integrated circuits, to PCB boards. Deducing the levels experimentally is often necessary for understanding (reverse engineering) the design of existing control architectures found in nature and legacy engineered systems.

<!-- chunk {"id": "body-0170", "role": "body", "section": "PART 3: KEY CONCEPTS IN CONTROL ARCHITECTURE", "weight": 1.0} -->

Layers. Layers are complementary to levels, and conceptually describe a functional decomposition of the overall behavior of a system. Layered control architectures typically decompose across complexity and spatiotemporal scales, with more complex functionality implemented in higher global layers at a slower frequency, and more rigid/structured functionality implemented in lower local layers at a higher frequency, see for example Fig. 2. Layers are the main architectural mechanism for taming complexity by breaking down a complex overall task into tractable subtasks (see Layered Control Architectures via Optimal Control Decomposition), and that enable DeSS by matching the spatiotemporal resolution of each layer with a corresponding control subtask (see Architecture Design as Multi-Criterion Optimization).

<!-- chunk {"id": "body-0171", "role": "body", "section": "PART 3: KEY CONCEPTS IN CONTROL ARCHITECTURE", "weight": 1.0} -->

Laws. Almost universally, we observe that hardware components have speed-accuracy tradeoffs (SATs), which impose a law on the low level hardware that can then lead to high level laws or constraints on optimal controllers. In neuroscience, vision is slower and more accurate than reflexes and proprioception. In immunology, adaptive immune responses take several days longer to mount than innate immune responses, but adaptive responses are more specific to the disease-causing pathogen. In computers, different storage components (e.g. registers, cache, RAM, disk) have extremely different speed, size, and cost. Typically there are low level hardware laws from physics that can directly impact higher levels, as well as entirely new ones that arise at higher layers that have no parallel in physics and are associated with names like Turing, Shannon, and Bode. Developing an integrated theory of laws across layers and levels is essential to a theory of architecture.

<!-- chunk {"id": "body-0172", "role": "body", "section": "PART 3: KEY CONCEPTS IN CONTROL ARCHITECTURE", "weight": 1.0} -->

Diversity-enabled Sweet Spots. In engineering, complex system functionality requires diverse hardware, and most hardware is involved in diverse functions. If built out of homogeneous components, the SATs imposed by lower levels would make robust control impossible. However, these SATs allow for extreme diversity in the hardware, which can be leveraged with the right architectures to provide diverse functionality. Highly diverse hardwarelevel components (which are constrained by SATs) enable performance sweet-spots that largely overcome the severe hardware-level SATs of individual components. In computers, such sweet spots include virtual memory management systems. In neuroscience, extreme diversity in axon sizes, receptors, and neurotransmitters is abundant, but largely hidden. By itself, diversity of components only enables sweet spots of function; to achieve these functional sweet spots requires specific architectures to maximize the utility of diverse components, which we call DeSS. We proposed a quantitative theory of DeSS by viewing Architecture Design as Multi-Criterion Optimization and provided examples of these concepts at play.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Bowties, hourglasses, virtualization, and abstraction", "weight": 1.0} -->

Fortunately, some features of LCAs are very familiar, particularly universal bowties and hourglasses that appear in complex highly evolved systems at every scale and context. In both bowties and hourglasses two outer deconstrained stages and layers, with very diverse components that are evolvable and even swappable, are linked in the

<!-- chunk {"id": "body-0174", "role": "body", "section": "Experimental Validation in a Biking Simulator", "weight": 1.0} -->

Sensorimotor control was studied in the context of the multisensory task of mountain bike riding using a video game as the experimental platform. The game captures tunable requirements on player performance which require layered architectures in the nervous system to create DeSS due to the constraints imposed by physiology, see Fig. 21. Naively, success in the biking task seems to require speed and accuracy that the raw hardware lacks, making non-layered solutions infeasible. The layered nervous system breaks the overall biking problem into a high trails (trajectory planning) layer of slow but accurate vision with trail look-ahead for advanced warning, and a low bumps (feedback control) layer that uses fast but inaccurate muscle spindles and proprioception to sense and reject bump disturbances. The motor commands from these two control loops to the muscles simply add in the optimal case, as well as in experiments, though muscles have their own constraints, as demonstrated by Fitts Law.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Experimental Validation in a Biking Simulator", "weight": 1.0} -->

Nakahira et al. developed experimental tasks and corresponding sensorimotor control models that mimicked three aspects of mountain biking: compensation by the spinal cord for the random shaking coming down the trail, the anticipation of turns in the trail by the visual system, and the stabilization of images on the retina by the oculomotor system to compensate bouncing. Two driving experiments were performed: the first is to test the interactions between layers, and the second is to test the errors caused by delays and rate limits in control within a layer. In the two experiments, subjects follow the trail on a computer screen and control a cursor with a wheel to stay on the trail. The goal of the subjects is to minimize the errors between the desired and actual trajectories shown in a computer monitor by moving the steering wheel (see Figs. S1 and S2).

<!-- chunk {"id": "body-0176", "role": "body", "section": "Experimental Validation in a Biking Simulator", "weight": 1.0} -->

In the first experiment, the higher-layer and the lower-layer are coordinated, and the authors compared how subjects' control behaviors and the resulting errors differ in three settings: 1) when there are random force disturbances to the steering wheel due to bumps on the ground (denote as 'Bump only'), 2) when the trail trajectory is curved and changes direction (denote as 'Trail only'), and 3) when both exist (denote as 'Both'). Rejection of bump disturbance in the first and last settings is likely to be middle via a narrow, highly constrained knot/waist with little diversity or evolvability. We call this constraints that deconstrain (as in). The terminology of bowties and hourglasses is not standard and can be confusing, but the distinction between them is useful and important. For a biologically motivated case-study, see Bowties and Hourglasses in Bacterial Metabolism. Both the bowtie and hourglass enable virtualization via universal shared interfaces, like OSes, ATP, wall plugs, this text, ribosomes and performed at the lower layer reflex, while trajectory following in the second and last settings is likely to be performed at the higher layer planning.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Experimental Validation in a Biking Simulator", "weight": 1.0} -->

FIGURE S1: Players see a winding trail scrolling down the screen at a fixed speed, and with a fixed advanced-warning (the visible trial ahead), both of which can be varied widely. The player aims to minimize the error between the desired trajectory and their actual position using a gaming steering wheel.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Experimental Validation in a Biking Simulator", "weight": 1.0} -->

FIGURE S2: Bumps are added using a motor torque in the wheel. Experiments can be done with bumps only or trails only, or both together, and with varying trail speed and/or advanced-warning, and with additional quantization and/or time delay in the map from wheel position to players' actual position.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Experimental Validation in a Biking Simulator", "weight": 1.0} -->

(continued on next page) translation, HTML, TCP/IP, HDMI, membrane potentials, faucets, dashboards, etc.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Experimental Validation in a Biking Simulator", "weight": 1.0} -->

Bowtie. Diversity is the aspect of architectures that is most familiar and easiest to discuss in the stages making up supply chains. Diverse proteins are a produced by highly conserved translation "knot" protocols with amino acid inputs and controlled by a transcription hourglass. In metabolism, diverse carbon sources and molecules are linked via a thin 'knot' of a few metabolic carriers and precursors. Diverse

<!-- chunk {"id": "body-0181", "role": "body", "section": "Experimental Validation in a Biking Simulator", "weight": 1.0} -->

The experimental results are shown in Fig. S3. The observed error in setting 3 (with both bumps and trail curvature) positively correlated with the sum of the errors from the first two settings with either bumps or trail curvature (Pearson correlation coefficient = 0. 57), suggesting the two signals tended to have consistent sign and amplitude. Moreover, the two signals showed no significant difference in the two-side t-test analysis. The results suggest that the two layers could be analyzed separately. This separability motivates the modeling of each layer separately and to further decompose the errors into those caused by neural signaling delays or rate limits in the control loop.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Experimental Validation in a Biking Simulator", "weight": 1.0} -->

The impact of neurophysiological limits was studied in the second experiment. We observed changes in lateral control error in three settings: when external delays are added in the display, when external quantizers are added in the actuation effect of the steering wheel, and when both are added. These manipulations served as noninvasive probes for how component constraints affect system behavior. The lateral errors in the three settings are shown in Fig. S5, and their corresponding theoretical prediction is shown in Fig. S4 (see the modeling details in the next section). The bridge between the constraints at the two levels highlights the benefits of the heterogeneity observed in nerves (Fig. 18) and the advantages of layering in sensorimotor control (as in Fig. 21).

<!-- chunk {"id": "body-0183", "role": "body", "section": "Experimental Validation in a Biking Simulator", "weight": 1.0} -->

FIGURE S3: Errors in the case of bump only, trail only, and both.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Experimental Validation in a Biking Simulator", "weight": 1.0} -->

FIGURE S4: The delay error max ( 0, T ) (blue), rate error ( 2 R -1 ) -1 (red), and the total error max ( 0, T ) + ( 2 R -1 ) -1 (black) are shown with varying component signaling delay Ts and rate R subject to the component constraint T = ( R -5 ) / 20.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Experimental Validation in a Biking Simulator", "weight": 1.0} -->

FIGURE S5: The error under an added delay (blue), the error under added quantization (red), and the error under added delayed plus quantization (black) are shown. In the last case, the added delay T and quantization rate R subject to the component constraint T = ( R -5 ) / 20. The dot shows the averaged error of 4 subjects, and the shadowed area indicates the standard error of the mean for these subjects.

<!-- chunk {"id": "body-0186", "role": "body", "section": "Experimental Validation in a Biking Simulator", "weight": 1.0} -->

| | Levels Physical | Layers Functional | Laws Pareto surface | Diversity Enabled Sweet Spots Near optimal Pareto point |

<!-- chunk {"id": "body-0187", "role": "body", "section": "Clothing as a Layered Control Architecture", "weight": 1.0} -->

Clothing is a familiar example that surprisingly highlights many universal concepts of control architecture. The levels are familiar-from thread to fibers to fabric to garment to outfit and we'll focus on the latter with notation garment \ outfit to denote levels. The layers for making clothing for harsh conditions are the outer/middle/inner garments: Outer layers provide waterand wind-proofing, middle layers are insulating, and inner layers are compatible (soft) for interfacing with skin. So, layers and levels are orthogonal decompositions of outfits, and both can have further decompositions within. This architecture of clothing creates a DeSS so that outfits are weatherproof, warm, and soft when no individual garment or part provides all these features. Of note, skin and the rest of the body contains major evolved controls for thermoregulation, so that clothing can be considered an extension on top of the skin of the complex feedback controls involved in the exquisitely tight control of central temperature characteristic of healthy humans. Adding layers in this way is an important consequence of layered architectures.

<!-- chunk {"id": "body-0188", "role": "body", "section": "Clothing as a Layered Control Architecture", "weight": 1.0} -->

Though clothing layering is usually purely passive, the outer layer provides a barrier function to wind and rain, the mid layer provides a barrier to heat loss, and the inner layer provides a soft barrier between the possibly rough outer layers and the skin. It may seem strange to think of these as layers of passive control, but there is no other discipline that can integrate such passive mechanisms (which abound in engineering) into a full stack theory of active/passive/lossless control layers.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Clothing as a Layered Control Architecture", "weight": 1.0} -->

A basic concept shown in the clothing example for understanding control architecture is 'barriers.' We naturally think of active controllers as creating barriers in the state space of controller/plant feedback interconnection, and the theories of Lyapunov and barrier functions and robust control extensions are explicitly aimed to make this rigorous, useful, and scalable. What barriers in this sense allow for is showing that the set of possible controlled trajectories in state space robustly avoid 'bad' regions. But if we want a more 'full stack' theory of architecture where the higher levels and layers are typically active control, it will be necessary to include lower layer control that is passive or even lossless. 'Barriers' are already familiar in studying passive controllers, but as post hoc analysis and less for design.

<!-- chunk {"id": "body-0190", "role": "body", "section": "Clothing as a Layered Control Architecture", "weight": 1.0} -->

We should probably think of active/passive/lossless as one example where there are both layers, e.g., in a car with active steering and braking, passive nonslip tires, and designed to be as lossless as can be in drag and friction, and levels, e.g., in a car active control is implemented in passive components plus power supplies, and physics tells us everything is microscopically lossless, which can be made rigorous using control theory.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Clothing as a Layered Control Architecture", "weight": 1.0} -->

Even the simplified proximal levels, layers, stages of dressing, and DeSS described here are minimal essentials to creating functional outfits, and nothing simpler will work in a harsh environment. In particular, random piles of garments are vanishingly unlikely to make an outfit. Concretely, consider a small 30 garment wardrobe with 10 each of garments for shell / warm / soft layers. Layering allows potentially 10 3 diverse but functional outfits, which is a much larger n 3 outfits versus 3 n garments. But there is exponentially more 2 30 = 1 e 9 possible piles of garments and the piles/outfits ratio of 2 n / n 3 obviously grows exponentially with n garments in each layer.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Clothing as a Layered Control Architecture", "weight": 1.0} -->

One near universal in architectures is that they select functional but extremely thin and sparse subsets within the set of all possible 'piles.' These thin, sparse subsets are even more extreme in the levels and layers below the garments level. Baking is another familiar example with visible levels of ingredients and layers such as cake, frosting, crusts, filling, etc... The levels and stages of baking are explicit in a recipe, but the supply chains that provide the ingredients are typically hidden behind convenient consumer interfaces. Random piles of ingredients and random stages of baking are extremely unlikely to produce anything even edible.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Clothing as a Layered Control Architecture", "weight": 1.0} -->

There are myriad tradeoffs and laws throughout the layers, levels, and stages that constrain what is possible, most obvielectric power sources and user appliances are linked in a bowtie via standard knot protocols (e.g., 110v 60Hz) in power grids. These examples all involve the flow of materials and energy thru various stages and, with respect to diversity, have a bowtie shape, with diverse sources and products at the edges and highly conserved and less diverse 'knots' in the middle. This enables independent and thus rapid evolution on both ends of the bowtie.

<!-- chunk {"id": "body-0194", "role": "body", "section": "Clothing as a Layered Control Architecture", "weight": 1.0} -->

Hourglass. An hourglass is used to describe the shape of layered communication and computing systems required to control bowties. Diverse app software runs on diverse hardware in an hourglass linked via less diverse 'waist' operating systems (OS) in computers and their networks. Humans have diverse skills and memes and diverse tools, linked in an hourglass by shared languages and a poorly understood brain OS. Genes, apps, memes, words, technologies, and tools are highly modular and swappable, massively accelerating evolvability beyond what is possible with only the slow accumulation of small innovations. Virtualization. Hourglasses rely on virtualization to enable the diversity both above and below the hourglass 'waist.' For example, operating systems in computers act as a protocol that virtualizes the wildly diverse hardware and computer networks in modern computing systems, which in turn has lead to the incredible progress and diversity of ously in the physical constraints on lower level materials and the high level users of the clothing architecture, but also on all the stages of supply chains.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Clothing as a Layered Control Architecture", "weight": 1.0} -->

But many constraints are evolved or designed as part of the architecture, such as the fabric \ garment levels and outfit/garment layers, which were presumably not part of the earliest clothing using animal skins, even though all must obey physical laws. These added constraints in higher layers and levels are 'constraints that deconstrain' in that they are essential to creating the DeSS that is the very goal of architecture. The result is that a limited repertoire of fibers can create enormously diverse garments which are only functional due to the constraints imposed by the universal architecture used by designers, manufacturers, and users. Baking has completely different details but is architecturally essentially the same.

<!-- chunk {"id": "body-0196", "role": "body", "section": "Clothing as a Layered Control Architecture", "weight": 1.0} -->

This clothing architecture in harsh environments might be greatly simplified on others. Outfits in some tropical settings have one or even no layers, and garments can have a fabric made of plastics with low level polymers but no threads or fibers. And so. So, diversity between architectures is as universal as the diversity that any one architecture enables, and once the centrality of this diversity is recognized, both diversities motivate an integrated theory to design and upgrade all important architectures. But this is new and confusing even among experts, which we also hope to change. software and data. In decision and control systems, lowlevel unstable dynamics are virtualized by the feedback control layer, allowing the planning layer to use simple, reduced order, and stable models for trajectory generation. Indeed, a commonly used model for trajectory generation in robotics across a wide variety of platforms (e.g., quadrupeds, quadrotors, mobile robots) is the Dubins' car or unicycle model-we expounded on this particular example of virtualization in robotics in previous sections (see Fig. S1 in Multi-Rate LCAs in Practice and Ex. 6).

<!-- chunk {"id": "body-0197", "role": "body", "section": "Clothing as a Layered Control Architecture", "weight": 1.0} -->

Here, the reference trajectory serves as the protocol between diverse planning and control layers, wherein each can be constructed using a diversity of algorithms, abstractions (see below), hardware, and software.

<!-- chunk {"id": "body-0198", "role": "body", "section": "Clothing as a Layered Control Architecture", "weight": 1.0} -->

Abstraction: Whereas the implementation of layered control architectures is enabled by bowties, hourglasses, and virtualization, the design of layered architectures would be impossible without abstractions. For example, when writing computer software engineers abstract OS/HW as memory and compute, often ignoring for example, device level drivers and timing constraints. Note however that as software approaches the limits of what the underlying hardware can implement, these abstractions may no longer be valid; hence the need, for example, real-time programming languages for embedded systems that directly

<!-- chunk {"id": "body-0199", "role": "body", "section": "Lego as a Layered Control Architecture", "weight": 1.0} -->

Lego is a simple, convenient, and literally toy system that illustrates many essentials of architecture, uses conventional digital control, but has transparent processes for the supply chain to (dis)assemble toys. Consider a familiar scenario where a child is repeatedly assembling, operating, and disassembling Lego robots to build a new one, and further focus on the building of one robot from a box full of old partial robots and isolated basic parts. There are roughly 4000 diverse standard Lego parts which are produced by a manufacturing supply chain that is hidden (virtualized) from the child. There are an infinite variety of possible robots, which are nevertheless a vanishingly small subset of all nonfunctional Lego assemblies.

<!-- chunk {"id": "body-0200", "role": "body", "section": "Lego as a Layered Control Architecture", "weight": 1.0} -->

Focusing on building one robot, the minimal levels would be parts\ robots consisting of the lower level parts that then make up an assembled robot, though additional levels could include various functional subassemblies. The simplest stages would be dissassembly|parts|assembly which form a bowtie with a large but relatively thin knot of parts compared to the infinite variety of robots and assemblies as inputs and outputs. This depends on a universal snap protocol to make both disassembly and assembly easy. Building a Lego toy is a minimal example of the classic thin knot consisting of a set of parts plus the protocols specifying how the parts can be assembled. The most basic Lego has just one snap protocol and thousands of parts in its 'knot.' Most architectures have many more of both, which access hardware resources. In decision and control systems, abstractions abound. At the feedback control layer, the plant and controller are abstracted as mathematical operators operating on continuous- or discrete-time signals. At the trajectory planning layer, the potentially complex low-level closed-loop control system is abstracted using a simple dynamics model, e.g., a unicycle.

<!-- chunk {"id": "body-0201", "role": "body", "section": "Lego as a Layered Control Architecture", "weight": 1.0} -->

This abstraction is valid thanks to the virtualization enabled by the feedback control layer below, but also breaks down if the planned trajectories extend beyond the tracking capabilities of the closed-loop system, again showing that abstractions are useful only within operating ranges that virtualization can be reliably enforced. Because virtualization greatly enables the use of effective abstractions, these two distinct concepts are often confused.

<!-- chunk {"id": "body-0202", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

We introduced a lexicon for key concepts in layered (control) architectures-levels, layers, stages, laws, DeSS, hourglasses, bowties, virtualization, abstraction-and instantiate them in familiar and diverse examples such as clothing, bacteria, GNC, robotics, and human sensorimotor control. These concepts are mostly familiar, but are referred to us- are still tiny compared to the variety of systems with a shared architecture.

<!-- chunk {"id": "body-0203", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

This proximal part of the Lego supply chain would also have a control hourglass where a child builder would take instructions and convert them into step-by-step assembly via the snap protocol. The thin middle waist layer would include the universal snap, here controlled repeatedly to control overall assembly. The top layer would be the infinite possible instructions to assemble working robots, and the bottom layer would be the huge variety of supply chain steps that these instructions would control, and the robots and sub-assemblies this produces.

<!-- chunk {"id": "body-0204", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

A universal feature this illustrates but that can be source of confusion is that the snap protocol is necessarily central to both the bowtie assembly knot and the control hourglass waist. In the bowtie knot it is the physical mechanism that holds parts together and allows robots and their parts to be easily (dis)assembled. This bowtie alone would be useless however, without an additional hourglass control of the snap process to in each step of (dis)assembly of a robot. The bowtie has essentially infinite diversity in the input of old robots or partial assemblies and the output of new robots. The hourglass also has infinite diversity in the top layer of instructions and the low layer of physical assembly steps, with a thin mid-layer waist that performs snap by snap (dis)assembly according to instructions. (continued on next page) ing different terms across domains: thus one primary goal of this manuscript was to establish a common language to unify the study of architecture. Furthermore, for certain concepts, we also proposed quantitative frameworks for the analysis and synthesis of LCAs, grounded in robotics and sensorimotor applications.

<!-- chunk {"id": "body-0205", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

We are very much aware that this paper poses more questions than it answers, and is likely to confuse (and perhaps even anger) applied and theoretical researchers alike. Nevertheless, we believe that underneath the cumbersome jargon and mathematical notation needed to convey our message there is a viable path towards a quantitative and universal theory of layered control architectures that the controls community is particularly well suited to pursue. With that in mind, we hope that if the reader leaves this paper with but one core message, it is that complex systems are composed of diverse levels and layers, and that their analysis and design falls squarely within the skill set and expertise of the controls community. Indeed, the impact in both theory and application of nascent versions of these concepts has already been astounding both within and outside of our community, and we are excited about the potential future impact that this emerging field of study

<!-- chunk {"id": "body-0206", "role": "body", "section": "Lego as a Layered Control Architecture", "weight": 1.0} -->

The Lego snap is a sweet spot in the space of alternative connection and control protocols. One alternative is smooth bricks with no snap, which would be easier to assemble but would not be able to make robots. Another would be adding glue which would make the robot more robust to trauma but make reuse difficult. The snap protocol is highly efficient, reusable, and robust, but fragile to finely targeted attacks such as removing imperceptibly thin and small bits of plastic just at the interface so that the snap would not hold. The process and the built robot however would be largely robust to similar removals away from the snaps, except in the computers controlling the robot. This extreme "robust yet fragile" feature is ubiquitous in real architectures, with one aspect captured in Bode's Integral Formula.

<!-- chunk {"id": "body-0207", "role": "body", "section": "Lego as a Layered Control Architecture", "weight": 1.0} -->

The snap also makes it easy to manufacture new Lego parts that work with existing parts and architecture. The knot and waist utilizing the snap protocol form the 'core' of the architecture 'crux' for the control of assembly, which here is done by a child infinitely more complex than any Lego robot. This process could in principle be replaced by special purpose assembly machines not greatly more complex than the robots it builds but attempts to build a truly self-replication universal Lego robot or machine have proven challenging.

<!-- chunk {"id": "body-0208", "role": "body", "section": "Lego as a Layered Control Architecture", "weight": 1.0} -->

In addition to the parts\ robot levels the functioning robot has, minimally, layers of computer/(sense&actuate)/plant where the 'plant' here would be the uncontrolled raw robot. This control system is distinct from the one doing assembly, and the computer would have sublayers of software/hardware, making this a toy version of a standard digital control system. Note that the software would typically be vastly more complex than the rest of the robot, and computer hardware would introduce vastly more levels including microscopic components like transistors. A robot toy without sensors, actuators, and computers would be infinitely simpler with only minimal functionality but would still have some important architectural features. The complexity of the design process for a new robot would also be dominated by
