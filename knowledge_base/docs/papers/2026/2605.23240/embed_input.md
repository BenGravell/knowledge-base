<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Signal Temporal Logic Motion Planning via Graphs of Convex Sets

Topics include Motion planning, Graphs of convex sets, Temporal logic planning, Formal methods, Convex optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Combines timed-automata reasoning with graphs of convex sets to generate smooth trajectories satisfying continuous-time signal temporal logic specifications. The contribution is a planning formulation that keeps high-level temporal requirements and low-level convex trajectory constraints in the same optimization pipeline.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper investigates continuous-time motion planning under Signal Temporal Logic (STL) specifications. The goal is to generate smooth robot trajectories that satisfy high-level logical and timing requirements while respecting low-level motion constraints. To this end, we propose an efficient framework that combines timed-automata reasoning with graphs of convex sets (GCS). An STL specification is first represented by a timed automaton, which is then coupled with a convex decomposition of the configuration space to form a joint transition system encoding both task progress and region occupancy. Based on this joint transition system, the STL motion-planning problem is reformulated as a shortest-path problem over a GCS, whose solution induces a smooth Bézier-spline trajectory satisfying the STL specification, smoothness requirements, and velocity bounds. We establish the soundness of the proposed formulation and analyze its computational complexity, showing that, once the timed automaton and convex decomposition are fixed, the convex relaxation scales polynomially with the configuration-space dimension and the Bézier degree. We further develop a compact timed-automaton construction for an expressive STL fragment using dedicated templates and Boolean composition.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Numerical experiments on low-dimensional benchmarks, a 3-D quadrotor, a 30-DoF humanoid, and a hardware experiment on a UR-3 robot arm demonstrate that the proposed method efficiently solves complex STL motion-planning problems and produces smooth executable trajectories.

<!-- chunk {"id": "body-0005", "role": "body", "section": "I-A Motivation", "weight": 1.0} -->

Task and motion planning is a fundamental problem in robotics, where a robot must generate physically feasible motions while accomplishing high-level tasks. Unlike classical motion planning, which mainly focuses on geometric or dynamical feasibility, task and motion planning must also jointly reason about task-level constraints such as logical ordering and timing requirements. This coupling makes the problem particularly challenging: low-level motion feasibility is typically defined over a continuous configuration space, whereas high-level task specifications are often discrete, logical, and combinatorial.

<!-- chunk {"id": "body-0006", "role": "body", "section": "I-A Motivation", "weight": 1.0} -->

In recent years, formal languages have attracted increasing attention as a principled way to describe high-level robotic tasks. Among them, Signal Temporal Logic (STL) has emerged as an expressive specification language for temporal behaviors of real-valued physical signals. STL can naturally encode requirements such as ordered visits, deadlines, dwell-time constraints, persistent surveillance, and safety conditions. This makes it well suited for robotic applications in which task satisfaction depends not only on where the robot moves, but also on when and for how long certain conditions hold. Recent applications in aerial robotics, robotic manipulation, and legged locomotion further demonstrate the practical relevance of STL-based planning.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A Motivation", "weight": 1.0} -->

Despite its expressive power, STL motion planning remains difficult to scale. A common approach is to encode STL constraints over time-discretized trajectories and solve the resulting optimization problem. Such methods are attractive because they can directly incorporate system dynamics, input bounds, and logical constraints within a single optimization problem. However, they usually lead to large mixed-integer programs, whose complexity grows rapidly with the planning horizon, the number of logical constraints, and the dimension of the system. Moreover, fine time discretization is often needed to reduce inter-sample violations, such as passing through an obstacle between two sampled states, which further increases the number of decision variables. Consequently, discretization-based STL planning becomes especially challenging for long-horizon tasks and high-dimensional robotic systems.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Motivation", "weight": 1.0} -->

An alternative is to decouple the full dynamic optimization from the high-level planning problem by generating continuous trajectories. For many robotic systems, especially differentially flat systems, smooth reference trajectories can be executed by low-level controllers and therefore provide a practical route to dynamic feasibility. Graphs of convex sets (GCS) have recently emerged as a powerful framework for this purpose, combining discrete path selection with continuous trajectory optimization over convex regions. GCS-based methods can generate smooth continuous-time trajectories and have shown favorable scalability in high-dimensional motion-planning problems. However, existing GCS formulations mainly focused on classical objectives such as obstacle avoidance, and reach-avoid navigation, with limited treatment of rich temporal-logic tasks. How to retain the scalability and smooth-trajectory advantages of GCS while enforcing the logical and timing requirements of STL specifications remains the key challenge addressed in this paper.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-B Our Contributions", "weight": 1.0} -->

In this paper, we address the task-and-motion-planning problem under signal temporal logic specifications. Our objective is to synthesize a continuous-time smooth trajectory that satisfies a given STL task while respecting geometric, timing, smoothness, and velocity constraints. To this end, we develop a unified planning framework that combines timed-automata reasoning with graphs of convex sets. Starting from an STL specification, we first represent the temporal task by a timed automaton, which captures the logical and timing progress required for task satisfaction. We then combine this timed automaton with a convex decomposition of the configuration space to construct a joint transition system that records both the task progress and the convex region occupied by the trajectory. Based on this joint transition system, we build a GCS instance and reformulate STL motion planning as a shortest-path problem over convex sets, where each selected path induces a smooth Bézier-spline trajectory satisfying the STL specification, and the imposed motion constraints.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-B Our Contributions", "weight": 1.0} -->

In this way, the proposed framework provides a bridge between formal temporal reasoning and continuous trajectory optimization. The timed automaton handles the logical structure and real-time requirements of STL specifications, while the GCS formulation exploits convex optimization to generate smooth trajectories efficiently over continuous configuration spaces.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-B Our Contributions", "weight": 1.0} -->

We propose a GCS-based formulation for STL motion planning. Given an STL specification represented by a timed automaton, the proposed construction converts logical task satisfaction, region occupancy, smoothness constraints, and velocity bounds into a shortest-path problem over convex sets. The resulting solution directly yields a continuous-time Bézier-spline trajectory.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-B Our Contributions", "weight": 1.0} -->

In addition to the general formulation, we identify an expressive STL fragment that covers many robotic tasks and provide a compact timed-automaton construction for this fragment. The construction is based on constant-size templates for elementary temporal patterns and union/product operations for Boolean composition, which substantially reduces the complexity compared with classical general-purpose timed-automaton constructions.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-B Our Contributions", "weight": 1.0} -->

We establish the soundness of the proposed GCS formulation, showing that every feasible solution of the constructed GCS problem yields a trajectory satisfying the original STL task together with the smoothness and velocity constraints. We also analyze the computational complexity and show that, once the timed automaton and convex decomposition are fixed, the convex relaxation scales polynomially with the configuration-space dimension and the Bézier degree.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-B Our Contributions", "weight": 1.0} -->

We conduct extensive numerical and hardware experiments to validate the scalability and practicality of the proposed approach. The experiments include low-dimensional STL planning benchmarks, a $3$-D quadrotor example, a $30$-DoF humanoid simulation, and a hardware implementation on a UR-3 robot arm. The results show that our method can efficiently solve complex STL motion-planning problems and generate smooth executable trajectories for both low-dimensional and high-dimensional robotic systems.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-C Related Works", "weight": 1.0} -->

STL Planning via Optimization-Based Approaches: A fundamental approach to STL motion planning is to formulate the problem as a constrained optimization problem. For systems with time-discretizations, both the system dynamics and the satisfaction of STL formulae can be encoded as algebraic constraints, leading to mixed-integer optimization formulations. These methods provide precise optimization-based formulations for the discretized planning problem and can explicitly incorporate dynamics, input constraints, and logical requirements. However, they typically suffer from rapidly growing computational complexity as the planning horizon, the system dimension, the number of logical constraints, and the discretization resolution increase. Moreover, fine time discretization is often needed to avoid inter-sample violations, which further increases the size of the resulting mixed-integer programs.

<!-- chunk {"id": "body-0016", "role": "body", "section": "I-C Related Works", "weight": 1.0} -->

To mitigate the complexity caused by time discretization, continuous-time optimization methods have also been explored. For example, timed-waypoint and piecewise-linear planning methods can handle complex STL specifications without discretizing the entire trajectory into a large number of time samples. However, these methods usually return piecewise-linear trajectories, which require an additional low-level tracking controller for execution and do not directly provide smooth trajectory parameterizations. In contrast, our approach formulates STL motion planning as a GCS-based shortest-path problem over convex sets. The resulting solution directly yields a smooth Bézier-spline trajectory, while the associated convex relaxation scales polynomially with the Bézier degree and the configuration-space dimension once the timed automaton and convex decomposition are fixed.

<!-- chunk {"id": "body-0017", "role": "body", "section": "I-C Related Works", "weight": 1.0} -->

STL Planning via Timed Automata: Automata-based methods have also been widely studied for motion planning and control under timed temporal logics such as MITL and STL. Foundational results in formal methods show that timed specifications can be translated into timed automata or related automaton models. The resulting automata encode the temporal progress of the specification and can then be used as the basis for planning under timed-logic constraints. However, most existing automata-based planning methods require a finite abstraction of the underlying dynamics. Constructing such abstractions becomes increasingly expensive as the system dimension and resolution grow, which limits their scalability to high-dimensional robotic systems. In contrast, our approach avoids building a global abstraction and directly combines timed-automaton reasoning with GCS-based continuous trajectory optimization. Furthermore, although our framework can use timed automata obtained from standard constructions such as, we also provide a more compact construction for an expressive STL fragment, where elementary temporal formulae are handled by dedicated TA templates, and compositional constructions are needed only for conjunction and disjunction. This avoids recursive temporal-operator composition and significantly reduces the automaton size for the considered class of robotic tasks.

<!-- chunk {"id": "body-0018", "role": "body", "section": "I-C Related Works", "weight": 1.0} -->

Sampling-Based STL Planning: Sampling-based methods constitute another important class of motion-planning algorithms, with RRT and its asymptotically optimal variant RRT^∗^ being representative examples. Recent works have extended this paradigm to STL planning by incorporating MILP encodings, STL robustness measures, control barrier functions, or automata-theoretic guidance into the sampling process. These methods are attractive because they are broadly applicable and can provide probabilistic completeness or asymptotic optimality guarantees under suitable assumptions. However, it is well known that sampling-based motion planners often suffer from poor practical scalability in high-dimensional configuration spaces, where the number of samples required to find a feasible or high-quality solution can grow rapidly. This difficulty becomes even more pronounced for STL planning, since the planner must satisfy not only geometric feasibility but also logical ordering and timing constraints. Moreover, sampling-based planners typically return discrete waypoints or piecewise-linear paths, and additional smoothing, post-processing, or tracking control is often needed to obtain executable trajectories.

<!-- chunk {"id": "body-0019", "role": "body", "section": "I-C Related Works", "weight": 1.0} -->

In contrast, our GCS-based approach constructs a convex decomposition of the configuration space and then solves an optimization problem over the resulting graph of convex sets. This allows us to directly generate continuous-time Bézier trajectories and explicitly impose smoothness, velocity, and timing constraints within the planning formulation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "I-C Related Works", "weight": 1.0} -->

Learning-Based STL Planning: Learning-based approaches have also been explored for STL tasks. Reinforcement learning methods typically incorporate STL robustness or progress measures into rewards or value functions and then learn policies from interaction or data. More recently, diffusion-based methods have been used to generate trajectories by sampling from learned models guided by STL-related criteria. These approaches are attractive when accurate system models are unavailable or when data-driven generalization is desired. However, they generally do not provide the same formal task-completion guarantees as synthesis-based methods, since STL satisfaction is usually encouraged through learned rewards, robustness surrogates, or sampling guidance rather than enforced by an explicit formal construction. By contrast, our method uses timed automata and GCS constraints to enforce STL satisfaction in a sound optimization-based framework.

<!-- chunk {"id": "body-0021", "role": "body", "section": "I-C Related Works", "weight": 1.0} -->

Temporal Logic Planning via GCS: Graphs of convex sets have recently emerged as a powerful framework for continuous motion planning. By associating graph vertices with convex sets and edges with convex constraints, GCS formulations combine discrete path selection with continuous trajectory optimization. Recent works have begun to extend GCS-based planning toward temporal-logic specifications. The work is particularly close in spirit to ours. It studies motion planning under LTL specifications by formulating the problem as a shortest-path problem over a GCS and exploiting the strong convex relaxation. Compared, our focus is on STL specifications with explicit real-time intervals and continuous-time semantics. This requires a dedicated treatment of clock variables, timed progress, and STL satisfaction through timed automata. Another closely related work is, which considers STL planning for discrete-time piecewise-affine systems and, inspired by GCS, proposes a logic-network-flow formulation to obtain tighter convex relaxations than logic-tree-based mixed-integer encodings. In contrast, our framework directly constructs a GCS formulation for continuous-time STL motion planning.

<!-- chunk {"id": "body-0022", "role": "body", "section": "I-C Related Works", "weight": 1.0} -->

The selected GCS path induces a smooth Bézier-spline trajectory, and the timing constraints are enforced through the coupled timed-automaton and GCS construction. Thus, our approach combines the scalability of GCS-based continuous trajectory optimization with the formal expressiveness of STL specifications.

<!-- chunk {"id": "body-0023", "role": "body", "section": "I-D Organization", "weight": 1.0} -->

The remainder of this paper is organized as follows. After introducing the necessary background in Section II, Section III formulates the considered STL motion-planning problem. Section IV then shows how to convert STL planning into a GCS-based optimization problem, while Section V develops an efficient timed-automaton construction for an expressive STL fragment. Experimental results are reported in Section VI, and concluding remarks are given in Section VII.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-A Signal Temporal Logic", "weight": 1.0} -->

We use Signal Temporal Logic (STL) formulae to specify high-level temporal requirements for robot trajectories. The syntax of STL formulae is given by

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-A Signal Temporal Logic", "weight": 1.0} -->

Throughout the paper, the robot configuration space is ${\mathbb{R}}^{n}$. Given a trajectory $\xi \in {\mathcal{C}_{n}{(T)}}$ and an STL formula $\Phi$, we write ${(\xi,t)} \models \Phi$ if $\xi$ satisfies $\Phi$ at time $t$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-A Signal Temporal Logic", "weight": 1.0} -->

The reader is referred to for further details on STL semantics.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B Bézier Curves", "weight": 1.0} -->

In this work, we use Bézier curves to parameterize robot trajectories. Given $K \in {\mathbb{Z}}_{\geq 0}$, the Bernstein polynomials of degree $K$ are defined by

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B Bézier Curves", "weight": 1.0} -->

We recall several standard properties of Bézier curves that will be used later. The reader is referred to for further details.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-B Bézier Curves", "weight": 1.0} -->

Derivative: The derivative $\overset{˙}{\Gamma}$ of a Bézier curve $\Gamma$ is a Bézier curve of degree $K - 1$ whose control points satisfy

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-B Bézier Curves", "weight": 1.0} -->

We denote by $\Gamma^{(i)}$ and $\gamma^{(i)}$ the $i$-th derivative of the Bézier curve and its control points, respectively.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-B Bézier Curves", "weight": 1.0} -->

Endpoint: The Bézier curve starts at its first control point and ends at its last control point, i.e.,

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-B Bézier Curves", "weight": 1.0} -->

Convex hull: The Bézier curve remains in the convex hull of its control points, i.e.,

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-C Graphs of Convex Sets", "weight": 1.0} -->

A graph of convex sets (GCS) is described by the tuple

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-C Graphs of Convex Sets", "weight": 1.0} -->

where $(\mathcal{V},\mathcal{E})$ is a directed graph with vertex set $\mathcal{V}$ and edge set $\mathcal{E} \subset {\mathcal{V} \times \mathcal{V}}$. Each vertex $v \in \mathcal{V}$ is associated with a convex set $\mathcal{X}_{v}$, and each edge $e = {(u,w)} \in \mathcal{E}$ is associated with a convex set $\mathcal{X}_{e} \subseteq {\mathcal{X}_{u} \times \mathcal{X}_{w}}$. The function $l_{e}:{\mathcal{X}_{e}\rightarrow{\mathbb{R}}_{\geq 0}}$ is a convex nonnegative length function associated with edge $e$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-C Graphs of Convex Sets", "weight": 1.0} -->

A path $\mathbf{p}$ is a sequence of distinct vertices in $\mathcal{V}$. We denote by $\mathcal{E}_{\mathbf{p}}$ the set of edges traversed by $\mathbf{p}$. Given a GCS, the associated optimization problem is to find a shortest path from a source vertex $s \in \mathcal{V}$ to a target vertex $t \in \mathcal{V}$. This problem can be written as

<!-- chunk {"id": "body-0036", "role": "body", "section": "II-C Graphs of Convex Sets", "weight": 1.0} -->

Here, $\mathcal{P}_{s,t}$ denotes the set of paths from $s$ to $t$, and $x_{v} \in \mathcal{X}_{v}$ is the continuous variable associated with vertex $v$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "II-C Graphs of Convex Sets", "weight": 1.0} -->

Problem can be encoded exactly as a mixed-integer convex program (MICP). Although solving the resulting MICP is NP-hard in general, it often admits a tight convex relaxation. In many instances, a globally optimal solution to can be obtained by solving the convex relaxation followed by a low-cost rounding step on the integer variables. The reader is referred to for more details on GCS. In this work, we use the GCS framework to formulate the STL motion-planning problem in a computationally efficient manner.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We consider the STL motion-planning problem for a robot operating under temporal task requirements and motion constraints. The objective is to compute a trajectory that satisfies a given STL specification while respecting a prescribed velocity bound. Although we do not explicitly impose the full system dynamics, we require the trajectory to satisfy a smoothness condition, which supports dynamically feasible execution for differentially flat systems. The problem is formally stated as follows.

<!-- chunk {"id": "body-0039", "role": "body", "section": "STL Motion Planning via GCS", "weight": 1.0} -->

This section presents the proposed procedure for converting the STL motion-planning problem in Problem 1 into a shortest-path optimization problem over a graph of convex sets.

<!-- chunk {"id": "body-0040", "role": "body", "section": "STL Motion Planning via GCS", "weight": 1.0} -->

First, we represent the STL specification by a timed automaton (TA), whose accepting runs provide a timed symbolic description of task satisfaction.

<!-- chunk {"id": "body-0041", "role": "body", "section": "STL Motion Planning via GCS", "weight": 1.0} -->

Second, we combine the TA with a convex decomposition of the configuration space to construct a joint transition system (JTS), which simultaneously records task progress and the convex region occupied by the trajectory.

<!-- chunk {"id": "body-0042", "role": "body", "section": "STL Motion Planning via GCS", "weight": 1.0} -->

Third, based on the JTS, we construct an instance of GCS in which vertices encode Bézier-curve segments, timing variables, and clock values, while edges encode continuity, smoothness, velocity, and timing constraints.

<!-- chunk {"id": "body-0043", "role": "body", "section": "STL Motion Planning via GCS", "weight": 1.0} -->

Finally, we solve the resulting GCS shortest-path problem, either exactly as a mixed-integer convex program or through its convex relaxation followed by rounding, and reconstruct a continuous-time Bézier-spline trajectory from the solution.

<!-- chunk {"id": "body-0044", "role": "body", "section": "STL Motion Planning via GCS", "weight": 1.0} -->

We also establish soundness of the formulation and analyze its computational complexity and completeness-related limitations. Hereafter, Section IV-A introduces timed automata and joint transition systems. Section IV-B constructs the corresponding GCS. Section IV-C provides the theoretical analysis.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-A Timed Automata and Joint Transition System", "weight": 1.0} -->

We first introduce timed automata and joint transition systems, which will be used to encode the temporal progress of an STL task and its coupling with the geometric decomposition of the configuration space.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A Timed Automata and Joint Transition System", "weight": 1.0} -->

We begin with the notion of a time constraint. Let $c$ be a clock variable. A time constraint on $c$, denoted by ${\theta{(c)}} \subseteq {\lbrack 0,T\rbrack}$, is a closed interval of the form $a \leq c \leq b$. The set of all time constraints on $c$ is denoted by $\Theta{(c)}$. Given a set of clock variables $C = {\{ c_{1},\ldots,c_{n}\}}$, we define

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-A Timed Automata and Joint Transition System", "weight": 1.0} -->

That is, each $\theta \in {\Theta{(C)}}$ assigns a time constraint to every clock variable in $C$. We say that a clock variable has *no constraint* if ${\theta{(c)}} = {\lbrack 0,T\rbrack}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

Given a joint transition system ${\mathbb{T}} = {(Q,Q_{0},Q_{F},C,\delta^{i},\delta^{o})}$ in (13. ‣ IV-A Timed Automata and Joint Transition System ‣ IV STL Motion Planning via GCS ‣ Signal Temporal Logic Motion Planning via Graphs of Convex Sets")), an initial state $x_{0} \in {\mathbb{R}}^{n}$, a final time $T \in {\mathbb{R}}_{\geq 0}$, a convex velocity bound $\text{vel} \subseteq {\mathbb{R}}^{n}$, a smoothness order $d \in {\mathbb{Z}}_{\geq 0}$, and a Bézier degree $K \in {\mathbb{Z}}_{\geq 0}$ with $K \geq d$, we construct a graph of convex sets (GCS)

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

whose components are defined as follows.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

\(1\) Vertex set: The vertex set is defined as

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

where $s$ and $t$ are virtual source and target vertices, respectively. Each vertex $q \in Q$ corresponds to a state of the joint transition system and therefore records both the progress of the timed automaton and the convex region occupied by the trajectory. The virtual source and target vertices are introduced to unify the treatment of multiple initial and accepting JTS states.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

\(2\) Edge set: The edge set is defined as

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

where $\mathcal{E}^{i} = \delta^{i}$, $\mathcal{E}^{o} = \delta^{o}$, and ${\mathcal{E}^{s} = {{\{ s\}} \times Q_{0}}},{\mathcal{E}^{t} = {Q_{F} \times {\{ t\}}}}$. Here, $\mathcal{E}^{i}$ and $\mathcal{E}^{o}$ correspond to the inner and outer transitions of the JTS, respectively. An inner edge allows the trajectory to move between adjacent convex regions while keeping the same TA state. An outer edge advances the TA state and enforces the corresponding clock constraints. The edge sets $\mathcal{E}^{s}$ and $\mathcal{E}^{t}$ connect the virtual source and target vertices to the initial and accepting JTS states.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

\(3\) Associated convex sets for vertices: For each JTS state $q = {(s,D)} \in Q$, the associated convex set satisfies

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

$\nu_{0},\nu_{1},\ldots,\nu_{K}$ are the control points of a Bézier curve $\Gamma_{q}^{r}$ that describes the geometric path segment;

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

$t_{0},t_{1},\ldots,t_{K}$ are the control points of a scalar Bézier curve $\Gamma_{q}^{h}$ that describes the time parameterization of this segment;

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

$c_{1},c_{2},\ldots,c_{|C|}$ record the clock values when the trajectory starts visiting the JTS state $q$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

In numerical implementation, this strict inequality can be replaced by ${t_{k + 1} - t_{k}} \geq \varepsilon$ for a small $\varepsilon > 0$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

To enforce the velocity bound in (8e), we further impose

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

Since vel is convex and the time increments are positive, these constraints define a convex feasible set. Therefore, $\mathcal{X}_{q}$ is characterized by and.

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

First, to ensure that the concatenated trajectory is $d$-times continuously differentiable, we impose

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

where $\nu^{(m)}$ and $t^{(m)}$ denote the control points of the $m$-th derivatives of the corresponding Bézier curves. When $m = 0$, these constraints enforce continuity of the geometric path and the time parameterization. When $m \geq 1$, they enforce matching derivatives up to order $d$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

Second, we impose clock-evolution constraints. The form of these constraints depends on whether $e$ is an inner edge or an outer edge. Let the clock variables in $C$ be indexed as $C = {\{\chi_{1},\ldots,\chi_{|C|}\}}$, and let $c_{i}$ and $c_{i}^{\prime}$ denote the values of clock $\chi_{i}$ at the beginning of vertices $q$ and $q^{\prime}$, respectively. If ${(q,q^{\prime})} \in \mathcal{E}^{i}$, then the TA state does not change.

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

These are affine equality constraints. If ${(q,q^{\prime})} \in \mathcal{E}^{o}$, then the edge corresponds to an outer transition of the TA. Let ${\delta^{o}{(q,q^{\prime})}} = {(\theta,\gamma)}$, where $\theta$ is the time constraint and $\gamma \subseteq C$ is the set of clocks reset by this transition. For each clock, we impose

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

Since each $\theta{(\chi_{i})}$ is a closed interval, the constraints in are convex.

<!-- chunk {"id": "body-0066", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

\(5\) Source and target constraints: The virtual source and target vertices do not carry continuous trajectory variables. Instead, they impose boundary constraints on their adjacent JTS vertices.

<!-- chunk {"id": "body-0067", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

Thus, the trajectory starts from the prescribed initial state $x_{0}$ at time $0$, and all clock variables are initialized to zero.

<!-- chunk {"id": "body-0068", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

Hence, the reconstructed trajectory is defined over the entire time horizon $\lbrack 0,T\rbrack$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

The use of virtual source and target vertices has two advantages. First, it provides a unified way to handle multiple initial TA states, multiple convex regions containing the initial state, and multiple accepting JTS states. Second, the vertex and edge constraints associated with the JTS are independent of the initial state. Thus, when the initial state changes, only the constraints associated with the source edges need to be modified.

<!-- chunk {"id": "body-0070", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

\(6\) Length function and trajectory reconstruction: Finally, we define the edge length function $l_{e}:{\mathcal{X}_{e}\rightarrow{\mathbb{R}}_{\geq 0}}$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

If the $\ell_{2}$ norm is used, then gives a convex upper approximation of the actual curve length, and the resulting convex programs are second-order cone programs (SOCPs). If the $\ell_{1}$ norm is used, the approximation is generally looser but the resulting programs become linear programs (LPs), which are more suitable for large-scale instances. Since derivatives of Bézier curves are also Bézier curves, derivative-dependent costs can be incorporated in the same manner.

<!-- chunk {"id": "body-0072", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

After constructing the GCS, we solve the corresponding shortest-path problem. Suppose that the solution returns a path

<!-- chunk {"id": "body-0073", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

from the virtual source $s$ to the virtual target $t$. For each $i = {1,2,\ldots,n}$, the solution provides a point

<!-- chunk {"id": "body-0074", "role": "body", "section": "IV-B Construction of GCS", "weight": 1.0} -->

This reconstructed trajectory is the candidate solution to the original STL motion-planning problem.

<!-- chunk {"id": "body-0075", "role": "body", "section": "IV-C Theoretical Analysis of the GCS", "weight": 1.0} -->

We now analyze the theoretical properties of the GCS formulation constructed in Section IV-B. We first establish soundness: every feasible solution of the GCS shortest-path problem yields a trajectory that satisfies the original STL motion-planning problem.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Remark 1", "weight": 1.0} -->

A desirable property of a planning method is completeness, namely, that the method returns a solution whenever Problem 1 is feasible. However, the proposed approach is not complete in this full sense as the following cases may occur. First, a feasible trajectory $\xi$ satisfying the STL formula $\Phi$ may not be accepted by the chosen TA $A_{\Phi}$, i.e., $\xi \models \Phi$ while $\xi\operatorname{\models\not{}}A_{\Phi}$. Second, a feasible trajectory may leave the constructed convex decomposition $\mathbb{D}$. Also, a feasible trajectory may not admit a Bézier-spline representation with the prescribed degree $K$ and the prescribed segmentation. Therefore, the proposed GCS optimization is complete only with respect to the restricted class of trajectories that are accepted by the TA, lie inside the chosen convex decomposition, and admit the prescribed Bézier-spline parameterization satisfying the imposed control-point constraints. Moreover, when the solution is obtained through convex relaxation and rounding, the rounding procedure may fail to recover a feasible integer path even if one exists.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Nevertheless, as shown in the experiments, this relaxation-and-rounding strategy is effective in practice.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Efficient Timed Automata Construction for an Expressive STL Fragment", "weight": 1.0} -->

In principle, a timed automaton can be constructed for a general STL formula by using standard STL-to-TA translations, such as that. However, directly using such general-purpose constructions in the proposed GCS framework is challenging for two reasons. First, standard constructions are designed to handle arbitrary nesting of temporal operators. As a result, the automaton must retain sufficient timing information to support future temporal compositions, which can lead to a very large state space even for seemingly simple specifications. Second, the size of the resulting automaton may depend not only on the syntactic size of the formula, but also on the temporal constants appearing in the formula. This dependence is particularly undesirable for long-horizon robotic tasks, where large time intervals are common.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Efficient Timed Automata Construction for an Expressive STL Fragment", "weight": 1.0} -->

To improve scalability, this section identifies a restricted but still expressive STL fragment that covers many robotic motion-planning tasks, including reachability, invariance, reach-and-stay, recurrence, and their Boolean combinations. For each temporal pattern in this fragment, we directly provide a compact TA template. General formulae in the fragment are then handled by composing these templates through union and product constructions, which correspond to disjunction and conjunction, respectively. In this way, compositional construction is only needed for Boolean operators, while temporal operators are handled directly by templates.

<!-- chunk {"id": "body-0080", "role": "body", "section": "V-A Considered STL Fragment", "weight": 1.0} -->

Here, $\varphi_{1}$ and $\varphi_{2}$ are formulae of class $\varphi$, while $\Phi_{1}$ and $\Phi_{2}$ are formulae of class $\Phi$. Formulae in class $\varphi$ describe time-independent Boolean combinations of atomic predicates. Formulae in class $\phi$ describe elementary temporal patterns applied to such Boolean predicates. Finally, formulae in class $\Phi$ are obtained by taking conjunctions and disjunctions of elementary temporal specifications.

<!-- chunk {"id": "body-0081", "role": "body", "section": "V-A Considered STL Fragment", "weight": 1.0} -->

The fragment in is expressive enough to encode many common robotic tasks. For example, $\mathbf{F}_{\lbrack a,b\rbrack}\varphi$ represents reaching a desired region within a time window; $\mathbf{G}_{\lbrack a,b\rbrack}\varphi$ represents remaining in a safe region over a time window; $\varphi_{1}\mathbf{U}_{\lbrack a,b\rbrack}\varphi_{2}$ represents maintaining one condition until another condition is reached; $\mathbf{F}_{\lbrack a,b\rbrack}\mathbf{G}_{\lbrack c,d\rbrack}\varphi$ represents reaching a region and staying there for a prescribed duration; and $\mathbf{G}_{\lbrack a,b\rbrack}\mathbf{F}_{\lbrack c,d\rbrack}\varphi$ represents recurrent satisfaction within a sliding time window.

<!-- chunk {"id": "body-0082", "role": "body", "section": "V-A Considered STL Fragment", "weight": 1.0} -->

However, this fragment does not include arbitrary nesting of temporal operators. For instance, formulae such as $\mathbf{G}_{\lbrack a,b\rbrack}\left( {\pi^{\mu_{1}} \land {\mathbf{F}_{\lbrack c,d\rbrack}\pi^{\mu_{2}}}} \right)$ are not directly included. This restriction is intentional: it allows each temporal pattern in (38b) to be handled by a small dedicated TA template, thereby avoiding the state-space explosion caused by repeatedly composing temporal operators.

<!-- chunk {"id": "body-0083", "role": "body", "section": "V-B Timed Automata Templates and Boolean Composition", "weight": 1.0} -->

In this subsection, we first introduce compact TA templates for the elementary temporal formulae $\phi$ in (38b). We then define two Boolean composition operators, namely union and product, which are used to construct TAs for formulae in (38c).

<!-- chunk {"id": "body-0084", "role": "body", "section": "V-B Timed Automata Templates and Boolean Composition", "weight": 1.0} -->

We begin with several common conventions used throughout this subsection. Let $\Omega = {\mathbb{R}}^{n}$ denote the whole configuration space. For a Boolean formula $\varphi$ in (38a), let $\lbrack\varphi\rbrack$ denote its satisfaction region. Since the subsequent GCS construction requires convex regions, the regions used in the TA templates may be conservative subsets of satisfaction regions. Specifically, we use $R_{\varphi} \subseteq {\lbrack\varphi\rbrack}$ to denote a region in which $\varphi$ is guaranteed to hold. For conjunctions, we similarly use $R_{\varphi_{1} \land \varphi_{2}} \subseteq {\lbrack{\varphi_{1} \land \varphi_{2}}\rbrack}$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "V-B Timed Automata Templates and Boolean Composition", "weight": 1.0} -->

For the template of $\mathbf{G}_{\lbrack a,b\rbrack}\mathbf{F}_{\lbrack c,d\rbrack}\varphi$, we additionally use a region $R_{\neg\varphi}$ satisfying ${\lbrack{\neg\varphi}\rbrack} \subseteq R_{\neg\varphi}$, which represents a region where $\varphi$ is not enforced.

<!-- chunk {"id": "body-0086", "role": "body", "section": "V-B Timed Automata Templates and Boolean Composition", "weight": 1.0} -->

The elementary TA templates are summarized as follows.

<!-- chunk {"id": "body-0087", "role": "body", "section": "V-B Timed Automata Templates and Boolean Composition", "weight": 1.0} -->

The intuition behind these templates is as follows. For $\mathbf{F}_{\lbrack a,b\rbrack}\varphi$, the automaton enters a $\varphi$-enforcing state at some time within $\lbrack a,b\rbrack$. For $\mathbf{G}_{\lbrack a,b\rbrack}\varphi$, the automaton enters the $\varphi$-enforcing state no later than $a$ and leaves it no earlier than $b$. For $\varphi_{1}\mathbf{U}_{\lbrack a,b\rbrack}\varphi_{2}$, the state $s_{0}$ enforces $\varphi_{1}$ until a switching time in $\lbrack a,b\rbrack$, and the state $s_{1}$ certifies that $\varphi_{2}$ also holds at that switching time.

<!-- chunk {"id": "body-0088", "role": "body", "section": "V-B Timed Automata Templates and Boolean Composition", "weight": 1.0} -->

For $\mathbf{F}_{\lbrack a,b\rbrack}\mathbf{G}_{\lbrack c,d\rbrack}\varphi$, the first transition selects the start of an interval on which $\varphi$ must hold, while the auxiliary clock $\eta$ enforces the required dwell time $d - c$. For $\mathbf{G}_{\lbrack a,b\rbrack}\mathbf{F}_{\lbrack c,d\rbrack}\varphi$, the automaton repeatedly returns to the $\varphi$-enforcing state $s_{2}$ within every duration of length $d - c$, ensuring that each window $\lbrack{\tau + c},{\tau + d}\rbrack$ with $\tau \in {\lbrack a,b\rbrack}$ contains a time instant satisfying $\varphi$. Therefore, each elementary temporal formula in (38b) is represented by a constant-size TA.

<!-- chunk {"id": "body-0089", "role": "body", "section": "V-B Timed Automata Templates and Boolean Composition", "weight": 1.0} -->

Only one clock is needed for non-nested temporal operators, and two clocks are sufficient for the nested templates $\mathbf{F}\mathbf{G}$ and $\mathbf{G}\mathbf{F}$. The templates are illustrated in Figs. 1 and 2.

<!-- chunk {"id": "body-0090", "role": "body", "section": "V-B Timed Automata Templates and Boolean Composition", "weight": 1.0} -->

The templates above handle only the elementary temporal formulae in (38b). To construct TAs for Boolean combinations in (38c), we use two standard composition operators: union for disjunction and product for conjunction. Before applying these operators, we rename states and clocks if necessary so that the automata to be composed have disjoint state sets and disjoint clock sets.

<!-- chunk {"id": "body-0091", "role": "body", "section": "V-C Correctness and Complexity", "weight": 1.0} -->

We now prove that the proposed construction is sound. That is, every trajectory accepted by the constructed TA satisfies the corresponding STL formula.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Remark 2 (Complexity of the Proposed Construction)", "weight": 1.0} -->

We briefly analyze the complexity of the proposed TA construction. For an STL formula $\Phi$ in (38c), let $|\Phi|$ denote the number of elementary temporal subformulae $\phi$ of the form in (38b) contained in $\Phi$. Each elementary template introduced above has at most five states and uses at most two clock variables. Therefore, before any optional clock-sharing simplification, the number of clocks in the composed TA satisfies ${|C|} \leq {2{|\Phi|}}$, and hence grows linearly with $|\Phi|$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Remark 2 (Complexity of the Proposed Construction)", "weight": 1.0} -->

The number of states depends on how these elementary templates are combined. The union operator, used for disjunction, adds the state spaces of the component automata. In contrast, the product operator, used for conjunction, multiplies the state spaces of the component automata. Therefore, the state space may grow exponentially with the number of elementary temporal subformulae. In the worst case, if $N = {|\Phi|}$ elementary templates are combined through conjunctions, the resulting product automaton has at most ${|S|} \leq 5^{N}$ states. Thus, the proposed construction has linear clock growth and, in the worst case, exponential state growth with respect to the number of elementary temporal subformulae. This exponential dependence is mainly caused by Boolean conjunctions, rather than by the temporal templates themselves.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Remark 3 (Comparison with Standard STL-to-TA Constructions)", "weight": 1.0} -->

We now compare the proposed template-based construction with standard STL-to-TA translations. For a general STL formula $\Phi$, let $N$ denote the total number of propositions, Boolean operators, and temporal operators in $\Phi$, and let $K$ denote the largest integer constant appearing in $\Phi$. Classical constructions, such as, may yield timed automata whose number of states is exponential in $NK$, while the number of clock variables is linear in $NK$. This is because such constructions are designed for arbitrary STL formulae and must support recursive composition with temporal operators. Although our construction still has worst-case exponential state growth due to Boolean products, it has two practical advantages for the fragment. First, each elementary temporal pattern in (38b) is represented by a constant-size template. Therefore, the construction avoids recursively composing automata with temporal operators. Second, the size of each template does not depend on the numerical lengths of the temporal intervals. Thus, long time horizons or large interval bounds do not by themselves increase the size of the elementary automata.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Remark 3 (Comparison with Standard STL-to-TA Constructions)", "weight": 1.0} -->

This distinction is important for robotic motion-planning tasks. For example, consider

<!-- chunk {"id": "body-0096", "role": "body", "section": "Remark 3 (Comparison with Standard STL-to-TA Constructions)", "weight": 1.0} -->

Under the proposed fragment-level counting, the outer temporal structure corresponds to a single elementary temporal subformula, so ${|\Phi|} = 1$. The Boolean formula inside the predicate only affects the geometric satisfaction region used in the corresponding template. By contrast, a general syntactic count includes all propositions and Boolean operators inside the predicate, which can be much larger. Therefore, the proposed construction is particularly suitable for long-horizon robotic tasks whose temporal structure is simple but whose geometric predicates may be rich.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Remark 4 (Implementation Simplifications)", "weight": 1.0} -->

Several implementation-level simplifications can further reduce the size of the constructed automaton. First, the physical-time clock $\kappa$ used in each elementary template records the same global time and is never reset. Thus, instead of assigning a separate physical-time clock to each template, all templates can share a single global clock. With this simplification, the final automaton only needs one global clock, together with one auxiliary clock for each nested temporal template. Second, unreachable or inconsistent product states can be pruned. For example, if the clock constraints associated with two component states are mutually incompatible, then the corresponding product state or transition cannot appear in any feasible run and can be safely removed. Such pruning can substantially reduce the size of the product automaton before constructing the GCS. Third, when the full product automaton is still too large, one may select a particular accepting path, or a small set of promising accepting paths, from the TA and construct the GCS only over the selected paths. This heuristic reduces the size of the resulting optimization problem but sacrifices completeness.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Remark 4 (Implementation Simplifications)", "weight": 1.0} -->

Nevertheless, soundness is preserved: whenever the resulting GCS problem is feasible, the reconstructed trajectory is still guaranteed to satisfy the STL specification.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Experiment Results", "weight": 1.0} -->

This section evaluates the proposed STL motion-planning framework in both simulation and hardware experiments. The experiments are designed to examine three aspects of the proposed approach: its performance on standard low-dimensional STL planning benchmarks, its scalability to high-dimensional robotic systems, and its practicality on a real robot platform. Section VI-A first reports simulation experiments on $2$-D and $3$-D STL planning problems, including comparisons with existing STL motion-planning methods. Section VI-B then evaluates the proposed method on a $30$-DoF humanoid robot in simulation. Finally, Section VI-C presents a hardware experiment on a UR-3 robot arm.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Experiment Results", "weight": 1.0} -->

All experiments are performed on a Linux workstation. We use Mosek to solve the convex relaxation of the GCS optimization problem. The reported runtime of our method is divided into three parts: the time for constructing the TA from the STL specification, the time for forming the GCS, and the time for solving the resulting convex optimization problem. Among these steps, only the final optimization step needs to be performed online. The TA construction and GCS construction can be performed offline and reused for different initial conditions whenever the task structure and workspace decomposition remain unchanged.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Experiment Results", "weight": 1.0} -->

The runtime results are summarized in Table I. For the $2$-D benchmarks, the table also reports the solve times of the comparison methods. In addition, for the $3$-D quadrotor example, we compare our method with the PWL method. A timeout, denoted by "TO", means that the solve time exceeds $7200$ seconds.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Experiment Results", "weight": 1.0} -->

GCS PWL stlpy_MICP
(a) stlcg (b) puzzle-1 (c) puzzle-2 (d) rover (e) either-or (f) deliver

<!-- chunk {"id": "body-0103", "role": "body", "section": "VI-A Simulation Experiments on 2-D/3-D STL Planning", "weight": 1.0} -->

Benchmarks: We first evaluate the proposed method on six $2$-D STL motion-planning benchmarks, as shown in Figure 3. The first four benchmarks are adopted from the STL motion-planning literature, while the last two are newly designed to test disjunctive tasks and more complex combinations of temporal requirements. In all benchmarks, the black region, denoted by $W$, represents a wall that the robot must avoid at all times. For readability, when presenting the STL specifications below, we omit the common safety constraint $\mathbf{G}_{\lbrack 0,T\rbrack}{\neg W}$.

<!-- chunk {"id": "body-0104", "role": "body", "section": "VI-A Simulation Experiments on 2-D/3-D STL Planning", "weight": 1.0} -->

In stlcg, shown in Figure 3(a), the robot is required to stay in the red region $R$ and the green region $G$ for $5$ seconds each, while always avoiding the blue region $B$. The STL task can be described as follows

<!-- chunk {"id": "body-0105", "role": "body", "section": "VI-A Simulation Experiments on 2-D/3-D STL Planning", "weight": 1.0} -->

In puzzle-1, shown in Figure 3(b), the robot must reach the goal region. The environment contains several doors, shown in red. Each door can be crossed only after the robot visits the corresponding numbered green region to collect the key. Let $G$ denote the goal, $D_{1},\ldots,D_{5}$ the doors, and $K_{1},\ldots,K_{5}$ the keys. The STL task is given by

<!-- chunk {"id": "body-0106", "role": "body", "section": "VI-A Simulation Experiments on 2-D/3-D STL Planning", "weight": 1.0} -->

The benchmark puzzle-2, shown in Figure 3(c), is similar to puzzle-1 but contains six doors. The corresponding STL task is given by

<!-- chunk {"id": "body-0107", "role": "body", "section": "VI-A Simulation Experiments on 2-D/3-D STL Planning", "weight": 1.0} -->

The benchmark rover, shown in Figure 3(d), is used to demonstrate that our framework can also handle STL tasks outside the fragment in by introducing additional TA templates. In this scenario, the robot must visit each green goal region $G_{i}$. Moreover, after arriving at any goal region, it must reach the yellow region $S$ within the following time interval. The task is

<!-- chunk {"id": "body-0108", "role": "body", "section": "VI-A Simulation Experiments on 2-D/3-D STL Planning", "weight": 1.0} -->

Since $\Phi_{4}$ is not directly contained in the STL fragment, we construct a new TA template for this task, as discussed in the appendix.

<!-- chunk {"id": "body-0109", "role": "body", "section": "VI-A Simulation Experiments on 2-D/3-D STL Planning", "weight": 1.0} -->

(b) Projection of the trajectories computed by our approach and the PWL method in

<!-- chunk {"id": "body-0110", "role": "body", "section": "VI-A Simulation Experiments on 2-D/3-D STL Planning", "weight": 1.0} -->

The benchmark either-or, shown in Figure 3(e), considers an STL task with disjunctions. There are three target pairs $(a_{i},b_{i})$, $i = {1,2,3}$.

<!-- chunk {"id": "body-0111", "role": "body", "section": "VI-A Simulation Experiments on 2-D/3-D STL Planning", "weight": 1.0} -->

Finally, the benchmark deliver, shown in Figure 3(f), requires the robot to recharge in the yellow region $c$ and reach targets $t_{1}$ and $t_{2}$ within their corresponding time intervals. In addition, the robot must collect keys $k_{1}$ and $k_{2}$ to open doors $g_{1}$ and $g_{2}$, respectively. The STL task is

<!-- chunk {"id": "body-0112", "role": "body", "section": "VI-A Simulation Experiments on 2-D/3-D STL Planning", "weight": 1.0} -->

Comparison methods: We compare our approach with two representative trajectory-optimization-based methods for STL motion planning. The first baseline is the piecewise-linear (PWL) method, which computes a piecewise-linear path satisfying the STL task and assumes the availability of a tracking controller for execution. The second baseline is the MPC-based method, which considers STL specifications under discrete-time semantics and solves an MPC problem with STL constraints to compute control inputs. Among these two baselines, only the MPC method explicitly incorporates dynamic-feasibility constraints.

<!-- chunk {"id": "body-0113", "role": "body", "section": "VI-A Simulation Experiments on 2-D/3-D STL Planning", "weight": 1.0} -->

In contrast, for differentially flat systems, our method can enforce dynamic feasibility by imposing smoothness constraints on the generated Bézier trajectory. Although both comparison methods also lead to MICPs, their convex relaxations are generally weak because they rely on big-$M$ encodings of logical constraints. Moreover, these MICPs do not admit an inexpensive rounding procedure comparable to the GCS relaxation-and-rounding strategy. In the experiments, the MPC method is implemented based on stlpy.

<!-- chunk {"id": "body-0114", "role": "body", "section": "VI-A Simulation Experiments on 2-D/3-D STL Planning", "weight": 1.0} -->

Results on 2-D benchmarks: The computed trajectories are shown in Figure 3, and the runtime results are reported in Table I. For the MPC baseline, we use a single-integrator model. Under the same setting, our method enforces dynamic feasibility by requiring the generated trajectory to be once differentiable.

<!-- chunk {"id": "body-0115", "role": "body", "section": "VI-A Simulation Experiments on 2-D/3-D STL Planning", "weight": 1.0} -->

The MPC method is the fastest on stlcg, but it performs poorly on the more complex benchmarks. It fails to find a solution within $7200$ seconds for puzzle-2, either-or, and deliver. On puzzle-1 and rover, it returns a trajectory only after substantially longer computation times than both our method and the PWL method. Moreover, because the MPC baseline uses discrete-time STL semantics, the resulting trajectory may violate the continuous-time specification between sampling instants, for example by passing through wall regions.

<!-- chunk {"id": "body-0116", "role": "body", "section": "VI-A Simulation Experiments on 2-D/3-D STL Planning", "weight": 1.0} -->

Compared with the PWL method, our approach successfully solves all benchmarks with comparable or better runtime in most cases. In particular, on puzzle-1, puzzle-2, rover, and deliver, our method is substantially faster than the PWL method. The PWL method is faster on stlcg and either-or. In terms of trajectory quality, our method produces smoother continuous-time trajectories and performs better on puzzle-2, either-or, and deliver, where the PWL method produces noticeably longer paths. Overall, these results show that the proposed GCS formulation is competitive on low-dimensional STL planning problems while providing continuous-time smooth trajectories.

<!-- chunk {"id": "body-0117", "role": "body", "section": "VI-A Simulation Experiments on 2-D/3-D STL Planning", "weight": 1.0} -->

Results on a 3-D quadrotor: We next extend the deliver benchmark to a $3$-D setting. For each feasible region in deliver, we assign a valid interval along the $z$-axis. The wall regions remain obstacles regardless of the $z$ coordinate. The resulting scenario is shown in Figure 4. For clarity, the wall regions are omitted from the $3$-D visualization. The STL specification is the same as $\Phi_{6}$.

<!-- chunk {"id": "body-0118", "role": "body", "section": "VI-A Simulation Experiments on 2-D/3-D STL Planning", "weight": 1.0} -->

We solve this problem for a quadrotor with fixed yaw using our method and the PWL method. When using our approach, we require the trajectory to be four times differentiable. This requirement ensures dynamic feasibility for the quadrotor because the quadrotor dynamics are differentially flat. As shown in Table I, our method solves the problem in $15.68$ seconds, whereas the PWL method requires $489$ seconds. Moreover, the PWL method only returns a piecewise-linear path, so an additional tracking controller is required for execution.

<!-- chunk {"id": "body-0119", "role": "body", "section": "VI-A Simulation Experiments on 2-D/3-D STL Planning", "weight": 1.0} -->

To isolate the effect of the smoothness constraint, we also tested our method without the smoothness requirement. In this case, the solve times of our method on the $2$-D deliver benchmark and the $3$-D quadrotor benchmark are $0.86$ seconds and $4.8$ seconds, respectively. By comparison, the PWL method requires $2.76$ seconds and $489$ seconds on the same two problems. These results indicate that the proposed GCS formulation scales favorably with the configuration-space dimension and is well suited for continuous-time STL motion planning of robotic systems.

<!-- chunk {"id": "body-0120", "role": "body", "section": "VI-B Simulation Experiments on High-Dimensional Humanoid", "weight": 1.0} -->

We next consider STL motion planning for the $30$-DoF Atlas humanoid model from Drake. This experiment is designed to demonstrate the scalability of the proposed method in a high-dimensional configuration space. As shown in Figure 5, the environment contains four target boxes colored green, blue, red, and black. The humanoid must reach these boxes under different temporal constraints. Specifically, over the time interval $\lbrack 0,6\rbrack$, the robot must reach the upper-right green box at least once every $3$ seconds. In addition, the blue and red boxes must be touched during the time interval $\lbrack 3,6\rbrack$. Finally, the robot must remain in the black box for $2$ seconds, with the stay starting at some time in $\lbrack 7,8\rbrack$. The STL task is

<!-- chunk {"id": "body-0121", "role": "body", "section": "VI-B Simulation Experiments on High-Dimensional Humanoid", "weight": 1.0} -->

where $g$, $b$, $r$, and $l$ denote the regions in which the robot reaches the green, blue, red, and black targets, respectively.

<!-- chunk {"id": "body-0122", "role": "body", "section": "VI-B Simulation Experiments on High-Dimensional Humanoid", "weight": 1.0} -->

We use inverse kinematics and C-IRIS to compute convex regions of the configuration space. The green and red targets correspond to left-hand reaching constraints, while the blue and black targets correspond to right-hand reaching constraints. We also construct an additional convex region without kinematic target constraints. As, we do not model contact interactions with the ground or the contact wrench cone. The pelvis pose is fixed in the world frame, so the robot is treated as a $30$-DoF system.

<!-- chunk {"id": "body-0123", "role": "body", "section": "VI-B Simulation Experiments on High-Dimensional Humanoid", "weight": 1.0} -->

We use Bézier splines of degree $K = 3$ and impose a $\mathcal{C}_{2}$ continuity constraint. By solving the convex relaxation, the proposed method obtains a feasible trajectory in $10.2$ seconds, as reported in Table I. The resulting trajectory, shown in Figure 5, satisfies the STL task. This experiment demonstrates that the proposed framework can handle STL motion-planning problems for high-dimensional robotic systems with complex temporal requirements.

<!-- chunk {"id": "body-0124", "role": "body", "section": "VI-C Hardware Experiment on Robot Arm", "weight": 1.0} -->

Finally, we validate the proposed approach on a hardware platform using a $6$-DoF model of a UR-3 robot arm. The experimental setup is shown in Figure 6. The right side contains a shelf from which the manipulator must pick up two items in sequence, namely the green and red items. The middle part contains an obstacle that must be avoided throughout the task. The left side contains a conveyor belt on which the items must be placed within prescribed time intervals.

<!-- chunk {"id": "body-0125", "role": "body", "section": "VI-C Hardware Experiment on Robot Arm", "weight": 1.0} -->

Here, regions $a$ and $c$ are the grasping locations for the green and red items, respectively. Region $b$ is the placement location for both items. Regions $e$ and $f$ are auxiliary positions that allow the manipulator to approach and grasp the green and red items more reliably. The STL formula requires the robot arm to visit auxiliary regions before and after grasping, and to remain in the grasping and placement regions for prescribed durations so that the end effector can reliably grasp and release the items.

<!-- chunk {"id": "body-0126", "role": "body", "section": "VI-C Hardware Experiment on Robot Arm", "weight": 1.0} -->

We use inverse kinematics and C-IRIS to compute convex regions of the configuration space corresponding to each task region. We then search for a trajectory satisfying the STL task using Bézier splines of degree $K = 8$ under a $\mathcal{C}_{4}$ continuity constraint. By solving the convex relaxation, the proposed method obtains a feasible trajectory in $9.65$ seconds. As shown in Figure 6, the computed trajectory satisfies the STL specification and can be executed on the hardware platform.

<!-- chunk {"id": "body-0127", "role": "body", "section": "VI-C Hardware Experiment on Robot Arm", "weight": 1.0} -->

For comparison, the method in considers the STL task $\mathbf{G}_{\lbrack 40,50\rbrack}{({a \vee b})}$ for a $7$-DoF robot arm and requires $160$ seconds to find a solution. In contrast, our approach handles a more complex STL task on a real robot platform while finding a solution in substantially less time. This hardware experiment further demonstrates the practical efficiency of the proposed GCS-based STL motion-planning framework.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presented a continuous-time STL motion-planning framework based on timed automata and graphs of convex sets. The proposed approach converts logical task progress, real-time constraints, convex-region occupancy, smoothness requirements, and velocity bounds into a unified GCS shortest-path formulation. The resulting solution directly reconstructs a Bézier-spline trajectory, thereby avoiding dense time discretization while retaining continuous-time satisfaction guarantees. We proved the soundness of the construction. We also analyzed the computational efficiency of the framework. To improve the scalability of the automaton layer, we further introduced a compact timed-automaton construction for an expressive STL fragment based on constant-size temporal templates and Boolean composition. The effectiveness of the proposed framework was validated through extensive experiments. On low-dimensional STL planning benchmarks, the method achieved competitive or better runtime compared with existing optimization-based approaches while generating smooth continuous-time trajectories. The $3$-D quadrotor, $30$-DoF humanoid, and UR-3 robot arm experiments demonstrated favorable scalability to higher-dimensional systems.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Future work will investigate richer STL fragments, robustness under uncertainty, and extensions to multi-agent robotic systems.
