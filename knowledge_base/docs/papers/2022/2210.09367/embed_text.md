## Introduction

Planning solutions to problems described by high-level specifications requires autonomously deciding both *what* to do (i.e., the sequence of high-level actions) and *how* to do it (i.e., the associated motions). This is difficult since both of these decisions can affect later stages of the planning problem by altering the valid and reachable subsets of the search space. Integrated Task and Motion Planning (TMP) is a holistic approach to solve these high-level planning problems by jointly considering the symbolic (i.e., actions) and geometric (i.e., motion) constraints on the solution.

Solving TMP problems is computationally expensive. Evaluating a candidate sequence of actions (i.e., a *task* or *symbolic* plan) requires the computationally expensive operations of finding compatible action parameters and associated valid motion plans. TMP algorithms typically consider multiple symbolic plans to solve a problem and must be efficient because the set of possible symbolic plans is combinatorially large for most real-world scenarios and the sets of possible action parameters and motion plans are uncountably infinite.

Figure 1: A clutter clearing example. The robot must move the green and blue sticks from their initial positions scattered on two tables to ending positions on the corresponding colored tables. Sticks may occlude others, forcing the robot to reason about a geometrically feasible order of manipulation.

Figure 2: A shelf rearrangement example. The robot must move the green stick from the upper shelf to the lower shelf and the blue stick from the lower shelf to the upper shelf. The red sticks block many grasps of the two target sticks and must be maneuvered around or moved to solve the problem.

The majority of TMP work is focused on improving the computational performance of algorithms instead of finding optimal solutions. Optimal TMP requires joint optimization of candidate symbolic plans and the corresponding action parameters and motion plans, which is more difficult than the independent optimal symbolic and optimal motion planning problems. Existing solution-optimal TMP algorithms have poor initial solution performance, require problem specific samplers and local motion planners, and/or are specific to manipulation planning.

This paper presents Task and Motion Informed Trees (TMIT\*), an optimal sampling-based TMP algorithm that extends results from makespan-optimal symbolic planning and almost-surely asymptotically optimal motion planning. TMIT\* efficiently searches the high-level problem's hybrid state space, which consists of both discrete and continuously valued dimensions. This direct search allows TMIT\* to be informed by both the symbolic and geometric constraints and to reuse motion planning effort as symbolic plans change.

TMIT\* interleaves asymmetric forward and reverse searches to identify geometrically infeasible plans and avoid computationally expensive action-parameter sampling and motion-planning operations. When combined with novel SMT-based (Satisfiability Modulo Theories ) symbolic planning and a differentiable distance-based predicate representation, this allows TMIT\* to quickly find initial solutions to high-level problems and almost-surely converge asymptotically to the optimum with additional computational time. We demonstrate the benefits of this approach on robotic-manipulation benchmark problems (Figs. 1: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning") and 2: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")), where TMIT\* significantly outperforms earlier nonoptimal TMP work in initial solution times and is able to decrease solution costs given additional computational time.

This work contributes methods for almost-surely asymptotically optimal TMP that integrates relaxed SMT-based symbolic planning and sampling-based motion planning, anytime approximation of action-precondition-satisfying state manifolds to avoid state discretization, motion guided deferral of expensive precondition satisfying state sampling, and adaptive prioritization to order the search of a multimodal space.

## Background and Related Work

TMP is an active area of research drawing from advancements in the motion planning and task planning literatures. TMIT\* frames TMP as multimodal motion planning (Sec. II-A: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")). It offers almost-surely asymptotically optimal TMP (Sec. II-B: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")) with practical performance by extending work on batch-sampling-based motion planning (Sec. II-C: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")) and incremental symbolic planning (Sec. II-D: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")). TMIT\* uses deferred sampling of continuous action parameters to improve its computational efficiency (Sec. II-E: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")).

### II-A Multimodal Motion Planning and TMP

Multimodal motion planning finds valid motions through sequences of *modes*, or discrete variations of a continuous configuration space, each imposing different constraints on the valid configurations. Manipulation planning is often modeled as multimodal motion planning, where modes correspond to choices of object grasps and placements. TMP problems also have multimodal structure with modes corresponding to different symbolic states that constrain the continuous (i.e., geometric) state components. Mode transitions are defined by symbolic high-level actions and link the task planning and motion planning subproblems. Framing TMP as multimodal motion planning allows approaches to avoid the backtracking necessary in most other formulations.

### II-B Almost-Surely Asymptotically Optimal TMP

Most TMP work focuses on efficiently finding initial solutions. Cost-aware or optimal TMP has only recently become a topic of interest to the field. Earlier optimal TMP work frames TMP as a nonlinear optimization problem and globally optimizes choices of action parameters and motions. This optimization-based approach does not scale well with plan length, action space size, and geometric complexity. \\Citetschmitt_optimal_sampling-based_2017 offer almost-surely asymptotically optimal manipulation planning based on a precomputed roadmap and domain-specific samplers for mode transitions. \\Citetgarrett_pddlstream_integrating_2020 produce TMP solutions that are optimal in symbolic action cost, but assume domain-specific samplers and do not jointly optimize their motions and action parameter choices. Recent results have shown that almost-sure asymptotic optimality results from pure motion planning are preserved for multimodal TMP under realistic assumptions on the measure of mode transition sets.

TMIT\* uses almost-surely asymptotically optimal sampling based motion planning for performant planning in high dimensional state spaces. It does not require any precomputation or domain-specific samplers, and solves both manipulation and more general TMP problems.

### II-C Batch-Sampling-Based Motion Planning

BIT\* approaches sampling-based motion planning by viewing batches of valid samples as vertices in a series of edge-implicit *random geometric graphs* (RGGs). This perspective allows planners to order their search in a principled manner and incorporate problem-specific information, such as cost heuristics. AIT\* builds on this idea with an asymmetric bidirectional search. The reverse search computes an accurate cost heuristic without edge validation to guide the forward search for a solution, focusing the forward search and reducing the number of fully evaluated edges.

TMIT\* extends AIT\* to plan in multimodal spaces. AIT\*'s lazy reverse search allows TMIT\* to check the geometric feasibility of actions in a candidate symbolic plan before committing to computing its full motion plan. \\Citettoussaint_logic-geometric_programming_2015 uses a similar hierarchy of feasibility checks to filter the space of symbolic plans.

### II-D Symbolic Planning for TMP

TMP solvers adapt advances in standalone symbolic planning to the TMP context. Symbolic planning for TMP is uniquely challenging since valid symbolic plans may not correspond to valid motion plans. TMP symbolic planners must be able to efficiently incorporate geometric feasibility constraints to generate alternative plans. TMP solvers have addressed this need with custom action formulations, top-$k$ symbolic planning with Monte Carlo tree search, and incremental constraint construction.

TMIT\* extends the incremental Boolean-satisfiability-based (SAT-based) symbolic planner proposed by and adapted for TMP by. Compared to this original adaptation, we neither include symbolic representations of continuous scenegraphs nor prediscretize the continuous problem state. We also solve a relaxed symbolic planning problem, do not require a translation step between discrete and continuous state, and use a new feature of the Z3 SMT solver to improve planner performance and extensibility. Other work has encoded the full Planning Domain Definition Language+ (PDDL+) symbolic language into SMT. TMIT\* uses a subset of the simpler, more common PDDL 2.1.

### II-E Deferred Action Parameter Sampling

Finding geometrically valid values for continuous action parameters (e.g., grasps and placement poses) is one of the core challenges of TMP. Recent work attempts to reduce the computational burden of finding valid parameters by validating actions incrementally.

TMIT\* adopts the differentiable distance function predicate representation of. This representation allows us to directly sample continuous states satisfying symbolic action preconditions and guide the motion planner toward these states. This guidance lets TMIT\* defer sampling action parameters until it has evidence from the motion planner that an action is both geometrically feasible and likely to be part of a valid solution.

## Problem formulation

A robot, $R$, comprises a kinematic tree of joint-connected links, $l \in \mathcal{L}$, and a mobile base with pose ${P{(R)}} \in {{SE}{}}$^11^1TMIT\* is not limited to planar mobile robots.. An object, $o \in \mathcal{O}$, is a physical entity in the robot's environment with an associated 3D geometry and pose, ${P{(o)}} \in {{SE}{}}$.

A predicate defines a property of the combined robot and object configuration (Def. 1: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")) as a relation. A symbol is a predicate applied to specific arguments (Def. 2: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")).

### Definition 1: Predicate

A predicate, $p \in \mathcal{P}$, is a function from a set of objects and/or robot links, $p_{\mathcal{O} \cup \mathcal{L}} \subseteq {\mathcal{O} \cup \mathcal{L}}$, to a Boolean domain, defining a problem-dependent property. Formally, $p:{{\prod_{n_{p}}p_{\mathcal{O} \cup \mathcal{L}}}\rightarrow{\mathbb{B}}}$, where $n_{p}$ is the arity of $p$, and $\prod$ is the Cartesian product. Predicates may define properties with *geometric* or *discrete* interpretations (Sec. IV-A ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")).

### Definition 2: Symbol

A symbol, $s \in \mathcal{S}$, is the application of a predicate, $p$, to specific arguments (also known as a proposition or ground predicate). A symbol is true in a state if the resulting values of its arguments satisfy the associated predicate's property, and is false otherwise^22^2TMIT\* extends to other SMT-encodable discrete symbolic domains.. Some symbols correspond to differences in the free configuration space, e.g., a symbol representing the robot's manipulator holding a specific object.

The state space for our problem is the combination of the discrete and continuously valued dimensions (Def. 3: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")). A mode is a subset of the state space with a unique, fixed setting of the discrete state and poses of ungrasped movable objects, and a *mode family* refers to an infinite set of modes which share their discrete state setting (Def. 4: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")). A motion is a continuous path through the state space (Def. 5: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")).

### Definition 3: State Space

The state space of the planning problem is the Cartesian product of the continuous robot configuration and object poses and the discrete symbolic state,

where $\mathcal{Q}_{R}$ is the robot configuration space, $\mathcal{Q}_{\mathcal{O}}$ is the space of all the objects' poses, and ${\mathbb{B}}^{|S|}$ is a Boolean domain representing the value of the discrete symbols.

### Definition 4: Modes and Mode Families

A mode family, ${\mathbb{M}} \subseteq \mathcal{Q}$, of a specific setting of the discrete state, $\xi \in {\mathbb{B}}^{|S|}$, is defined as:

A mode, $\mathcal{M} \subseteq {\mathbb{M}}$, for a specific set of movable object poses, $\rho \in \mathcal{Q}_{\mathcal{O}}$, is defined as:

### Definition 5: Motion

A motion between two states, ${{\mathbf{q}}_{i},{\mathbf{q}}_{f}} \in \mathcal{Q}$, is a sequence of states described by a function, $\sigma:{\lbrack 0,1\rbrack\rightarrow\mathcal{Q}}$, that starts at the initial state, ${\sigma} = {\mathbf{q}}_{i}$, ends at the final state, ${\sigma} = {\mathbf{q}}_{f}$, and is continuous at all points, ${{\forall t},{\lim_{\tau\rightarrow t}{\sigma{(\tau)}}}} = {\sigma{(t)}}$. By definition, a motion cannot change the discrete symbolic state.

Discrete actions are defined by their necessary preconditions and their resulting effects (Defs. 6: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning"), 7: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning") and 8: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")).

### Definition 6: Precondition

A precondition or constraint, $\phi:{\mathcal{Q}\rightarrow{\mathbb{B}}}$, is a function that evaluates a Boolean propositional logic formula at a state.

### Definition 7: Effect

An effect, $\psi:{\mathcal{Q}\rightarrow\mathcal{Q}}$, is a deterministic function that possibly modifies a state in a discontinuous manner. An effect may alter the continuous and discrete parts of a state, but many TMP action effects only modify the discrete part.

### Definition 8: Action

An action, $\alpha \in \mathcal{A}$, $\alpha = \left( \phi_{\alpha},\psi_{\alpha} \right)$, comprises the preconditions, $\phi_{\alpha}$, necessary to execute the action and the effects, $\psi_{\alpha}$, of the action on the state when successfully executed, as in symbolic planning. The set of actions, $\mathcal{A}$, includes the *null action*, $\bot$, defined such that, ${{\forall{\mathbf{q}}} \in \mathcal{Q}},{{\phi_{\bot}({\mathbf{q}})} = \text{true}}$, and, ${{\forall{\mathbf{q}}} \in \mathcal{Q}},{{\psi_{\bot}({\mathbf{q}})} = {\mathbf{q}}}$. An action can be considered an abstraction of a specific high-level robot skill (e.g., grasping, pushing, pouring, etc.).

The TMP problem is then formally defined as the search for a plan of actions and motions (Def. 9 Problem ‣ III Problem formulation ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")).

### Definition 9: Task and Motion Planning (TMP) Problem

Let ${\mathbf{q}}_{0} \in \mathcal{Q}$ be an initial state, $\phi_{\text{g}}$ be a goal specified as a constraint, and $\mathcal{A}$ be a set of discrete actions executable by a robot. The TMP problem is then formally defined as the search for motions, $\sigma_{i} \in \Sigma$, and symbolic actions, $\alpha_{i} \in \mathcal{A}$, that can be interleaved into a task-and-motion plan, $(\sigma_{1},\alpha_{1},\sigma_{2},\alpha_{2},\ldots,\sigma_{n},\alpha_{n})$, such that:

The plan begins at the initial state, ${\sigma_{1}{}} = {\mathbf{q}}_{0}$.

Robot and object motions are valid (e.g., collision free),

The final state of each motion, $\sigma_{i}{}$, satisfies the requirements to execute the following action, $\alpha_{i}$,

The effect of each intermediate action, $\alpha_{i}$, results in the initial state of the following motion, $\sigma_{i + 1}{}$, and

The effect of the final action, $\psi_{\alpha_{n}}$, meets the specified goal constraint, ${\phi_{\text{g}}{({\psi_{\alpha_{n}}{({\sigma_{n}{}})}})}} = \text{true}$.

Optimal TMP finds TMP solutions which optimize a given cost function (Def. 10: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")).

### Definition 10: Optimal TMP

Let $\Theta$ be the set of all valid solutions to a TMP problem (Def. 9 Problem ‣ III Problem formulation ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")) and $\gamma:{\Theta\rightarrow{\mathbb{R}}^{\geq 0}}$ be a cost function. The optimal TMP problem is the search for a lowest cost solution, $\theta^{\ast} \in \Theta$, such that $\theta^{\ast} = {{{\arg\min}_{\theta \in \Theta}\gamma}{(\theta)}}$

Solving TMP as independent symbolic and motion planning problems is commonly infeasible; TMIT\* presents a holistic approach that solves the integrated problem.

## Task and Motion Informed Trees (TMIT\*)

TMIT\* (Fig. 3 ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")) plans in a multimodal hybrid state space in which any valid path, annotated with symbolic actions at certain states, is a valid task-and-motion plan. It uses an incremental SMT-based symbolic planner inspired by on a relaxed problem to find a candidate symbolic plan, defining a sequence of hybrid state space modes. It samples batches of states along this mode sequence and uses a distance-based geometric predicate representation to detect when samples are within the connection radius of precondition-satisfying states for an action in the plan. Sampling these precondition-satisfying states corresponds to choosing continuous action parameters (e.g., grasps) and allows TMIT\* to connect to the next reachable modes.

If this marched sampling procedure does not reach the goal mode then the symbolic plan is infeasible at the current resolution and TMIT\* uses knowledge of the modes in which it failed to inform the search for a new symbolic plan. Sampling resumes without discarding old symbolic plans or samples to reuse motion planning effort and allow increased sample resolution to prove symbolic plan feasibility. If the sampling procedure does reach the goal mode then the symbolic plan is validated further via an asymmetric bidirectional search. This search process continues until a solution is found and almost-surely converges asymptotically towards the jointly optimal task-and-motion solution.

Figure 3: The TMIT* planning loop. TMIT* cycles between generating candidate symbolic plans, (Sec. IV-B), sampling batches of states in the modes traversed by the candidate plans (Sec. IV-C), and the reverse and forward search stages of AIT*. If it fails to reach the goal mode, it adds constraints (Sec. IV-B5) and returns to the symbolic planner for a new candidate. This process continues until it finds a valid path to the goal.

### IV-A Predicate representation

TMIT\* uses a split predicate representation to simplify the symbolic planning subproblem and guide the motion plan search toward action-precondition-satisfying states.

We partition the set of predicates into those with *geometric* properties, $\mathcal{P}_{\text{G}} \subseteq \mathcal{P}$, and those with *discrete* properties, $\mathcal{P}_{\text{D}} = {\mathcal{P} \smallsetminus \mathcal{P}_{\text{G}}}$. Some predicates have natural categorizations, e.g., a discrete predicate representing a light's state or a geometric predicate describing distance to an object. For others, the correct interpretation may be problem specific, e.g., a predicate for an object being on a specific surface. This distinction aids in representing and solving TMP problems.

Discrete predicates comprise the discrete part of the state space (Def. 3: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")). Geometric predicates have associated differentiable functions defining the distance from a given state to a nearest predicate-satisfying state. The distance for a geometric predicate, $p \in \mathcal{P}_{\text{G}}$, is zero at a given state, ${\mathbf{q}} \in \mathcal{Q}$, if and only if the state, $\mathbf{q}$, satisfies the predicate, $p$. We project uniform-randomly sampled states onto the zero-level set of this function via gradient-based optimization.

Predicate distance functions can be defined in different ways. We automatically derive distance functions for symbolic formulae with "unsatisfaction semantics".

### IV-B Symbolic planning

TMIT\* solves the symbolic planning subproblem with an incremental SMT-based symbolic planning algorithm inspired by. SMT solvers generalize SAT by extending the variable types (to include integers, real numbers, arrays, etc.) and relations, which are backed by efficient solvers for the corresponding formal theories.

Basic SAT-based symbolic planning 1. creates Boolean variables for each action and symbol, 2. adds constraints encoding the initial and goal state, 3. constrains variables to remain consistent between steps (i.e., the "frame axioms"), 4. constrains actions to imply their preconditions and effects, and 5. iteratively increases the number of plan steps until the resulting formula is satisfiable. \\Citetdantam_incremental_constraint-based_2018 extend this core approach by encoding discretized geometric state and using the Z3 SMT solver's incremental constraint stack to reuse solver effort when adding plan steps.

We further extend the approach of with a custom theory that improves performance and expressivity. We specificially 1. enforce the frame axioms, precondition constraints, and other planning constraints implicitly via Z3's *user propagator*, reducing the number of long-lived clauses, 2. relax the symbolic planning problem by omitting geometric propositions from precondition formulae, and 3. do not discretize the continuous state. We outline TMIT\*'s symbolic planner in Secs. IV-B1 ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning"), IV-B2 ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning"), IV-B3 ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning"), IV-B4 ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning") and IV-B5 ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning").

### IV-B1 State encoding

In contrast to, we create Boolean indicator variables only for each *discrete* symbol (i.e., those corresponding to predicates in $\mathcal{P}_{\text{D}}$) at each step of the plan and omit the geometric symbols. We also do not discretize or symbolically represent the geometric state in the symbolic planning problem, relaxing the symbolic planning problem by optimistically ignoring constraints from geometric predicates. This frees the SMT solver from explicitly considering geometric relations.

### IV-B2 Action encoding

We create a Boolean indicator variable, $a_{\alpha}^{j} \in {\mathbb{B}}$, for each action, $\alpha$, at each step $j$. This indicator variable is true if the plan takes the associated action at step $j$ and false otherwise. Our custom theory implicitly enforces the precondition and effect constraints, $a_{\alpha}^{j}\Longrightarrow{\phi_{\alpha}^{j - 1} \land \psi_{\alpha}^{j}}$, where $\phi_{\alpha}^{j - 1}$ is the precondition of $\alpha$ encoded using the variables for the relevant discrete symbols at step $j - 1$, and $\psi_{\alpha}^{j}$ is the effect of $\alpha$ applied at step $j$. When Z3 assigns a value to an action indicator variable, we assert any unsatisfied clauses in the relevant precondition and effect constraints. This improves performance by reducing the number of clauses for the SMT solver to validate.

### IV-B3 Frame axioms and action mutexes

We also implicitly enforce the frame axioms and action mutex constraints. The frame axioms specify that a symbol's value at step $j$ is the same as at the preceding step unless an action that modifies it is chosen at step $j$. This ensures that variable values remain consistent between steps. When Z3 assigns a symbol indicator variable's value at a step, we assert the relevant frame axiom. Action mutex constraints force Z3 to choose only a single action per step.

### IV-B4 The symbolic planning loop

The symbolic planning loop is a typical incremental SAT-based planner. We first assert the initial discrete state and add plan steps up to a heuristically determined minimum plan length^33^3Zero, unless we have a better estimate for a problem.. Each step adds constraints asserting the discrete state at the step and the action transition constraints and frame axioms (Secs. IV-B2 ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning") and IV-B3 ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")). We then assert the goal constraint and invoke the Z3 SMT solver to attempt to find a solution. We add new steps and reinvoke the solver until a satisfying assignment exists. We extract a plan from a solution by checking which action indicator variables are true at each step.

### IV-B5 Generating alternative plan candidates

TMIT\* has two methods of generating alternative symbolic plan candidates. The first enumerates all candidate symbolic plans by requiring new plans to differ from previous plans by at least one action, ensuring completeness. This method adds constraints:

for a current solution with length $n$, and where $\text{value}_{k}$ returns the value of a variable in the $k$-th candidate plan.

A *prefix* of a symbolic plan is a subsequence of the actions in the plan starting with the initial action. The second method forces new plans to avoid *failing prefixes* of symbolic plan candidates by adding constraints of the same form as Eq. 4 ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning"), but only until the first step for which precondition-satisfying state sampling failed. Precondition-satisfying state sampling may fail if sample projection (Sec. IV-A ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")) fails to converge, if it converges to a local minimum off the precondition-satisfying manifold, or if the resulting state is invalid (i.e., in collision). This can quickly eliminate broader groups of candidate symbolic plans and find a solution more efficiently, but may remove prefixes that would prove feasible with more computation. We use this prefix-blocking method in the experiments of Sec. VI: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning").

### IV-C Motion Planner Integration

TMIT\* solves the motion planning subproblem by building upon AIT\*, an almost-surely asymptotically optimal batch-sampling-based motion planner, to find geometrically valid instantiations of candidate symbolic plans. We extend AIT\*'s batch sampling to 1. sample states in each reachable mode and 2. sample action precondition-satisfying states only if a uniform sample is within a tunable distance threshold (e.g., the connection radius ) of the precondition-satisfying region.

A mode is *reachable* if either it is the initial mode (i.e., the initial discrete state and scene) or we have sampled a precondition-satisfying state for an action that transitions to it from a reachable mode. Sampling batches across the reachable modes uniformly increases the resolution of AIT\*'s RGG (Sec. II-C: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")) and allows TMIT\* to implicitly reevaluate old candidate symbolic plans without backtracking.

The set of precondition-satisfying states for an action is often a manifold of measure zero in the ambient configuration space due to dimensionality-reducing constraints and therefore has zero probability of being sampled with uniform-random sampling. Computing precondition-satisfying states is computationally expensive relative to uniform-random sampling, and many such states are challenging to reach with a motion plan (e.g., states close to objects being manipulated).

We avoid wasted effort by projecting uniform-random samples onto precondition-satisfying manifolds only when the samples are within a tunable distance threshold (e.g., ) of the manifold^44^4Sampling a precondition-satisfying state takes on the order of 10--100 optimizer iterations; testing the distance takes less than one., which effectively *inflates* the manifold to positive measure. This strategy avoids computing unusable precondition-satisfying samples by only invoking this process starting from states that are 1. in the RGG and 2. close enough to a precondition region to improve the solution cost. Starting from valid states close to a precondition region may additionally improve the likelihood that the resulting precondition-satisfying sample will be valid.

Input: Mode queue ω, connection radius μ, goal ϕg
Output: Batch of samples B
2 while |ω| &gt; 0: // All reachable modes
16 if not AtGoal() or NoActions(): NewTaskPlan()
Algorithm 1 Multimodal batch sampling

Alg. 1 ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning") shows the multimodal batch sampling function. SampleValid draws each state uniformly at random from the valid configuration space of a given mode. The viable actions (Alg. 1 ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")) of a mode, $\mathcal{M} \in {\mathbb{M}}$, are symbolic actions that are used at $\mathbb{M}$ in a candidate symbolic plan and have been attempted less than a heuristically determined number of times. Attempting an action means trying to sample a valid state satisfying its precondition constraint. The heuristic limit on attempts per action provides a budget of computation per candidate symbolic plan; IncreaseBudget increments this heuristic threshold. NoActions tests if any actions in any reachable mode are viable, and $d{( \cdot, \cdot )}$ returns the distance from a state to the nearest precondition-satisfying state. SamplePrecond projects the given state onto the manifold of precondition-satisfying states by gradient-based optimization. UpdateModes adds newly reached modes to the mode queue, AtGoal checks if the total set of samples contains goal mode states, and NewTaskPlan invokes the task planner (Secs. IV-B4 ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning") and IV-B5 ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")).

The mode queue is ordered to prioritize recently reached modes. This ordering creates behavior akin to the "enforced hill climbing" of the FastForward (FF) task planner by continuing the search in the resulting mode when an action succeeds, effectively following the corresponding task plan candidate as far as possible. Alg. 1 ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning") returns early if it reaches a goal-satisfying state. The mode queue persists across invocations of Alg. 1 ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning") for the same batch.

### IV-D Considerations for Multimodal AIT\*

Computing exact distance in the hybrid configuration space is PSPACE-complete^55^5The distance between two states is a function of the shortest sequence of mode transitions between them, which is an optimal symbolic plan.. We conservatively over-approximate configuration space distance by assuming states in different modes are infinitely far apart if we do not have a successful transition between their modes. This approximation is not a metric, but suffices in practice.

AIT\* uses the reverse search to calculate a heuristic to guide the forward search (see for details). This approximation must account for the conservative over-approximation of intermode distance. The reverse search therefore uses forward-direction transitions and distances between modes (distances are directionally symmetric within a mode).

### IV-E Implementation

We provide a proof-of-concept implementation of TMIT\* in C++^66^6[https://robotic-esp.com/code/tmitstar](https://robotic-esp.com/code/tmitstar). We use the implementation of AIT\* and associated sampling-based motion planning utilities from the Open Motion Planning Library and use Bullet for collision checking. The geometric predicate implementation is an improved version of using the Autodiff library for automatic differentiation, NLOpt for optimization, and a bespoke dual-number automatic differentiation implementation in LuaJIT for predicate functions.

The planner's input is simpler than most other TMP solvers and does not include specialized samplers or planners, or prediscretized state. It requires only a description of the initial scene, a specification of the robot morphology and kinematics, object and robot geometries, the symbolic planning domain and problem, and functions for geometric predicates.

## Analysis

The probabilistic completeness and almost-sure asymptotic optimality of TMIT\* follow from the corresponding properties of AIT\*. We sketch proofs of these properties for TMIT\*. In the following, assume that precondition regions are convex, and that all precondition-satisfying states in a complete feasible plan are surrounded by a valid hyperball.

### Theorem 1: Probabilistic Completeness

Given a TMP problem as in Def. 9 Problem ‣ III Problem formulation ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning"), the probability that TMIT\* does not find a solution goes to zero as the number of samples taken approaches infinity.

### Proof

TMIT\* eventually attempts every possible symbolic plan candidate, since SATPlan (Sec. IV-B ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")) is complete, and the constraints described in Sec. IV-B5 ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning") ensure that candidate symbolic plans are distinct. The symbolic planner will be invoked infinitely often until a TMP solution is found, since Alg. 1 ‣ Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning") requests a new task plan whenever it fails to reach the goal mode or runs out of viable actions. Actions have a finite attempt budget and the mode queue is always emptied before completing a batch. AIT\* is probabilistically complete and will eventually sample within the connection radius of each precondition region infinitely often. Each precondition-satisfying manifold is convex by assumption, so projecting uniform-random samples onto the precondition regions will eventually sample every point in the manifold. Thus, we will find a valid path through our planning space if one exists, and therefore are probabilistically complete. ∎

The sketch of almost-sure asymptotic optimality is similar.

### Theorem 2: Almost-Sure Asymptotic Optimality

Given an optimal TMP problem as in Def. 10: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning"), TMIT\* converges asymptotically to an optimal-cost solution with probability one as the number of samples approaches infinity.

### Proof

AIT\* is asymptotically optimal within each mode and its reverse search heuristic is computed globally across modes. TMIT\* samples precondition-satisfying states whenever a uniform-random sample is within the connection radius of the precondition region. TMIT\*'s symbolic planner is complete, each precondition region is inflated to positive measure, and precondition regions are convex by assumption, so TMIT\* will asymptotically sample better precondition-satisfying states for every viable action. Thus, as the number of uniform-random samples approaches infinity, we asymptotically converge to the optimal action sequence and associated optimal motion plan (the optimal task and motion plan) with probability one. ∎

## Evaluation

Directly comparing TMP solvers is challenging due to differing definitions of the TMP problem. TMIT\* does not assume prediscretization of continuous state or specialized blackbox precondition samplers, which makes its problems harder. We perform a cold-data comparison to Planet, as its problem definition and assumptions are closest to TMIT\*'s. All experiments were run on an AMD Ryzen 7 2700X CPU with 32 GB of RAM and use a PR2 robot model with 14 controllable joints and a planar mobile base (17 total degrees of freedom). We evaluate on two common TMP tasks: clutter clearing and shelf rearrangement. We use batches of 50 samples per mode, a batch budget (the number of batches before requesting a new symbolic plan candidate) of five for clutter clearing and two for shelf rearrangement, and an initial action-attempt budget of one. We use Euclidean distance within modes and optimize path length.

### Clutter Clearing

A set of colored sticks is initially scattered on one of two tables (Fig. 1: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")). The goal is to place each stick on one of two other tables corresponding to its color. Every stick must be manipulated, and sticks occlude others in their initial positions, so solutions require reasoning over a long series of symbolic actions to move the sticks in a geometrically valid order. The action space contains $16 \times {|\mathcal{O}|}$ symbolic actions for each instance size and each symbolic action has an infinite number of possible continuous instantiations. Fig. 4: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning") shows results for clutter clearing.

### Shelf rearrangement

The robot must retrieve and move a set of objects between two stacked shelf surfaces (Fig. 2: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning")). The target objects are initially placed deep within the shelves and are surrounded by increasing numbers of distractor objects. Motions are geometrically constrained by the shelves and the distractor objects must either be moved out of the way or maneuvered around to reach the target objects. The action space contains $6 \times {|\mathcal{O}|}$ symbolic actions for each instance size. Fig. 5: Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning") shows results for shelf rearrangement.

### VI-A Qualitative Discussion

LABEL:fig:clutter.time shows that TMIT\* significantly outperforms Planet in initial solution time, often by an order of magnitude. The results for Planet constitute 10 successful trials of each instance size; in contrast, the TMIT\* results constitute 100 trials where timeouts are considered to have taken infinite time. LABEL:fig:clutter.percent shows that TMIT\* finds initial solutions for most instances quickly but that larger problem instances are more likely to either time out or have higher variance in initial solution times. This distribution reflects the greater geometric and symbolic challenge of the more complex instances. LABEL:fig:clutter.optimizing shows median solution costs for 100 trials of TMIT\* on instances of clutter clearing with 3--5 target objects. While the largest drop in median cost corresponds to initial solution discovery, the trends show that TMIT\* makes consistent progress toward lower-cost solutions.

LABEL:fig:shelves.time demonstrates the relative effect of minimum solution length versus the number of objects in a problem environment on TMIT\*'s initial solution performance. Although there are more objects present in large shelf rearrangement instances than large clutter clearing instances, the number of actions necessary to solve a shelf rearrangement problem is generally lower than the number required for a comparably large clutter clearing problem. This results in TMIT\* finding solutions for large shelf rearrangement instances faster than for large clutter clearing problems. TMIT\*'s motion-planner-guided sampling of continuous action parameters also sometimes allows it to find grasp poses for the target blocks that carefully reach past the distractor objects and reduce the overall plan length. LABEL:fig:shelves.optimizing shows TMIT\* optimizing costs for instances of the shelf rearrangement problem.

## Conclusions

Figure 4: Results for 100 trials of clutter clearing. LABEL:fig:clutter.time and LABEL:fig:clutter.optimizing show median time or cost (respectively); the error bars in LABEL:fig:clutter.time show a 95% confidence interval of the median. Each trial had 600 seconds of planning time; trials which failed to find a solution within this bound were counted as having infinite duration and cost. Trials in LABEL:fig:clutter.optimizing terminated early if their cost converged. LABEL:fig:clutter.percent show the cumulative percentage of problems solved as a function of time for each instance size. Timeouts are more frequent for larger instance sizes, reflecting the greater geometric difficulty of the problem.

Figure 5: Results for 100 trials of the shelf rearrangement problem. LABEL:fig:shelves.time and LABEL:fig:shelves.optimizing show median time or cost (respectively); the error bars in LABEL:fig:shelves.time show a 95% confidence interval of the median. Each trial had 300 seconds of planning time; trials which failed to find a solution within this time were counted as having infinite duration and cost. LABEL:fig:shelves.percent shows the cumulative percentage of problems solved as a function of time for each instance size.

TMIT\* is a novel approach to almost-surely asymptotically optimal TMP. It extends work on constraint-based symbolic planning, distance-based predicate representation, and batch-sampling-based optimal motion planning. TMIT\* solves a relaxed symbolic planning problem with a novel SMT-based makespan-optimal symbolic planner to generate candidate sequences of actions, then attempts to find geometrically valid instantiations of these actions through asymmetric bidirectional batch-sampling-based motion planning in a hybrid multimodal state space. It uses a differentiable distance-based representation of geometric predicates to guide parameter sampling and sample action-precondition-satisfying states through gradient-based optimization. When candidate symbolic plans are not feasible, it generates alternatives by blocking invalid action sequence prefixes; however, it is able to continue to consider older candidate plans without backtracking by continuing the motion planning process.

Asymmetric bidirectional motion planning is well-suited to TMP because it gains information about action feasibility before paying the cost of validating a candidate plan's edges. Incrementally improving a RGG further allows planners to reuse motion planning effort across candidate plans. Future work may investigate using asymmetric bidirectional motion planning algorithms better suited for complex cost functions, such as Effort Informed Trees (EIT\*).

Encoding task planning as SMT via a custom theory offers untapped potential performance improvements for TMP. It provides an easy extension point for a "theory of TMP", incorporating geometric information such as reachability or action feasibility into the symbolic planner. We leave exploration of this capacity for future work.

Future work could also investigate accelerating the discovery of initial solutions by explicitly biasing RGG growth toward task-relevant regions.
