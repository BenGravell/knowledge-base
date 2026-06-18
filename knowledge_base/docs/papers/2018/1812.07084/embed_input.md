<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Constraints from Demonstrations

Topics include Imitation learning, Learning from demonstrations, Constraints, Integer programming, Hit-and-run sampling, Safe planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Learns shared task constraints from safe demonstrations by synthesizing lower-cost unsafe trajectories and fitting a consistent unsafe set with an integer program. The work adds a safety-oriented inverse-learning angle: demonstrations reveal not only costs or policies but also hidden constraints that transfer across dynamics.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We extend the learning from demonstration paradigm by providing a method for learning unknown constraints shared across tasks, using demonstrations of the tasks, their cost functions, and knowledge of the system dynamics and control constraints. Given safe demonstrations, our method uses hit-and-run sampling to obtain lower cost, and thus unsafe, trajectories. Both safe and unsafe trajectories are used to obtain a consistent representation of the unsafe set via solving an integer program. Our method generalizes across system dynamics and learns a guaranteed subset of the constraint. We also provide theoretical analysis on what subset of the constraint can be learnable from safe demonstrations. We demonstrate our method on linear and nonlinear system dynamics, show that it can be modified to work with suboptimal demonstrations, and that it can also be used to learn constraints in a feature space.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inverse optimal control and inverse reinforcement learning (IOC/IRL) have proven to be powerful tools in enabling robots to perform complex goal-directed tasks. These methods learn a cost function that replicates the behavior of an expert demonstrator when optimized. However, planning for many robotics and automation tasks also requires knowing constraints, which define what states or trajectories are safe. For example, the task of safely and efficiently navigating an autonomous vehicle can naturally be described by a cost function trading off user comfort and efficiency and by the constraints of collision avoidance and executing only legal driving behaviors. In some situations, constraints can provide a more interpretable representation of a behavior than cost functions. For example, in safety critical environments, recovering a hard constraint or an explicit representation of an unsafe set in the environment is more useful than learning a "softened" cost function representation of the constraint as a penalty term in the Lagrangian. Consider the autonomous vehicle, which absolutely must avoid collision, not simply give collisions a cost penalty. Furthermore, learning global constraints shared across many tasks can be useful for generalization.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Again consider the autonomous vehicle, which must avoid the scene of a car accident: a shared constraint that holds regardless of the task it is trying to complete.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While constraints are important, it can be impractical for a user to exhaustively program into a robot all the possible constraints it should obey when performing its repertoire of tasks. To avoid this, we consider in this paper the problem of recovering the latent constraints within expert demonstrations that are shared across tasks in the environment. Our method is based on the key insight that each safe, optimal demonstration induces a set of lower-cost trajectories that must be unsafe due to violation of an unknown constraint. Our method samples these unsafe trajectories, ensuring they are also consistent with the known constraints (system dynamics, control constraints, and start/goal constraints), and uses these unsafe trajectories together with the safe demonstrations as constraints in an "inverse" integer program which recovers a consistent unsafe set.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We pose the novel problem of learning a shared constraint across tasks.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose an algorithm that, given known constraints and boundedly suboptimal demonstrations of state-control sequences, extracts unknown constraints defined in a wide range of constraint spaces (not limited to the trajectory or state spaces) shared across demonstrations of different tasks.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide theoretical analysis on the limits of what subsets of a constraint can be learned, depending on the demonstrations, the system dynamics, and the trajectory discretization. We also show that our method can recover a guaranteed underapproximation of the constraint.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide experiments that justify our theory and show that our algorithm can recover an unsafe set with few demonstrations, across different types of linear and nonlinear dynamics, and can be adapted to work with boundedly suboptimal demonstrations. We also demonstrate that our method can learn constraints in the state space and a feature space.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Forward optimal control problem", "weight": 1.0} -->

Consider an agent described by a state in some state space $x \in \mathcal{X}$. It can take control actions $u \in \mathcal{U}$ to change its state.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem 3.1 (Forward problem / \"task\" $\\Pi$)", "weight": 1.0} -->

$\mathcal{S}$ is an unknown safe set, and the inverse problem aims to recover its complement, $\mathcal{A} \doteq \mathcal{S}^{c}$, the "unsafe" set. In this paper, we focus on constraints separable in time: ${{\phi{(\xi_{x},\xi_{u})}} \in \mathcal{A}}\Leftrightarrow{{\exists t} \in {{\{ 1,\ldots,T\}}\phi{({\xi_{x}{(t)}},{\xi_{u}{(t)}})}} \in \mathcal{A}}$, where we overload $\phi$ so it applies to the instantaneous values of the state and the input. An analogous definition holds for the continuous time case. Our method easily learns non-separable trajectory constraints as well^11^1Write Problem 3.2.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem 3.1 (Forward problem / \"task\" $\\Pi$)", "weight": 1.0} -->

‣ 3.2 Inverse constraint learning problem ‣ 3 Preliminaries and Problem Statement ‣ Learning Constraints from Demonstrations") constraints as sums over partially separable/inseparable feature components instead of completely separable components..

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem 3.1 (Forward problem / \"task\" $\\Pi$)", "weight": 1.0} -->

A demonstration, $\xi_{xu} \doteq {(\xi_{x},\xi_{u})}$, is a state-control trajectory which is a boundedly suboptimal solution to Problem 1. ‣ 3.1 Forward optimal control problem ‣ 3 Preliminaries and Problem Statement ‣ Learning Constraints from Demonstrations"), i.e. the demonstration satisfies all constraints and its cost is at most a factor of $\delta$ above the cost of the optimal solution $\xi_{xu}^{\ast}$, i.e. ${c{(\xi_{x}^{\ast},\xi_{u}^{\ast})}} \leq {c{(\xi_{x},\xi_{u})}} \leq {{({1 + \delta})}c{(\xi_{x}^{\ast},\xi_{u}^{\ast})}}$. Furthermore, let $T$ be a finite time horizon which is allowed to vary.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem 3.1 (Forward problem / \"task\" $\\Pi$)", "weight": 1.0} -->

If $\xi_{xu}$ is a discrete-time trajectory ($\xi_{x} = {\{ x_{1},\ldots,x_{T}\}}$, $\xi_{u} = {\{ u_{1},\ldots,u_{T}\}}$), Problem 3.1. ‣ 3.1 Forward optimal control problem ‣ 3 Preliminaries and Problem Statement ‣ Learning Constraints from Demonstrations") is a finite-dimensional optimization problem, while Problem 3.1. ‣ 3.1 Forward optimal control problem ‣ 3 Preliminaries and Problem Statement ‣ Learning Constraints from Demonstrations") becomes a functional optimization problem if $\xi_{xu}$ is a continuous-time trajectory ($\xi_{x}:{{\lbrack 0,T\rbrack}\rightarrow\mathcal{X}}$, $\xi_{u}:{{\lbrack 0,T\rbrack}\rightarrow\mathcal{U}}$).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem 3.1 (Forward problem / \"task\" $\\Pi$)", "weight": 1.0} -->

We emphasize this setup does not restrict the unknown constraint to be defined on the trajectory space; it allows for constraints to be defined on any space described by the range of some known feature function $\phi$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem 3.1 (Forward problem / \"task\" $\\Pi$)", "weight": 1.0} -->

We assume the trajectories are generated by a dynamical system $\overset{˙}{x} = {f{(x,u,t)}}$ or $x_{t + 1} = {f{(x_{t},u_{t},t)}}$ with control constraints $u_{t} \in \mathcal{U}$, for all $t$, and that the dynamics, control constraints, and start/goal constraints are known. We further denote the set of state-control trajectories satisfying the unknown shared constraint, the known shared constraint, and the known task-dependent constraint as $\mathcal{T}_{\mathcal{S}}$, $\mathcal{T}_{\overline{\mathcal{S}}}$, and $\mathcal{T}_{\mathcal{S}_{\Pi}}$, respectively. Lastly, we also denote the set of trajectories satisfying all known constraints but violating the unknown constraint as $\mathcal{T}_{\mathcal{A}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Inverse constraint learning problem", "weight": 1.0} -->

The goal of the inverse constraint learning problem is to recover an unsafe set, $\mathcal{A} \subseteq \mathcal{C}$, using $N_{s}$ provided safe demonstrations ${{\xi_{s_{j}}^{\ast},j} = 1},{\ldots,N_{s}}$, known constraints, and $N_{\neg s}$ inferred unsafe trajectories, ${{\xi_{\neg s_{k}},k} = 1},{\ldots,N_{\neg s}}$, generated by our method, which can come from multiple tasks. These trajectories can together be thought of as a set of constraints on the possible assigments of unsafe elements in $\mathcal{C}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Inverse constraint learning problem", "weight": 1.0} -->

To recover a gridded approximation of the unsafe set $\mathcal{A}$ that is consistent with these trajectories, we first discretize $\mathcal{C}$ into a finite set of $G$ discrete cells $\mathcal{Z} \doteq {\{ z_{1},\ldots,z_{G}\}}$ and define an occupancy function, $\mathcal{O}{( \cdot )}$, which maps each cell to its safeness: ${\mathcal{O}{( \cdot )}}:{\mathcal{Z}\rightarrow{\{ 0,1\}}}$, where ${\mathcal{O}{(z_{i})}} = 1$ if $z_{i} \in \mathcal{A}$, and $0$ otherwise.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Inverse constraint learning problem", "weight": 1.0} -->

Continuous space trajectories are gridded by concatenating the set of grid cells $z_{i}$ that ${\phi{(x_{1})}},\ldots,{\phi{(x_{T})}}$ lie, which is graphically shown in Figure 1 with a non-uniform grid.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem 3.2 (Inverse feasibility problem)", "weight": 1.0} -->

Inferring unsafe trajectories, i.e. obtaining ${{\xi_{\neg s_{k}},k} = 1},{\ldots,N_{\neg s}}$, is the most difficult part of this problem, since finding lower-cost trajectories consistent with known constraints that complete a task is essentially a planning problem. Much of the next section shows how to efficiently obtain $\xi_{\neg s_{k}}$. Further details on Problem 3.2. ‣ 3.2 Inverse constraint learning problem ‣ 3 Preliminaries and Problem Statement ‣ Learning Constraints from Demonstrations"), including conservativeness guarantees, incorporating a prior on the constraint, and a continuous relaxation can be found in Section 4.4.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Method", "weight": 1.0} -->

The key to our method lies in finding lower-cost trajectories that do not violate the known constraints, given a demonstration with boundedly-suboptimal cost satisfying all constraints. Such trajectories must then violate the unknown constraint. Our goal is to determine an unsafe set in the constraint space from these trajectories using Problem 3.2. ‣ 3.2 Inverse constraint learning problem ‣ 3 Preliminaries and Problem Statement ‣ Learning Constraints from Demonstrations"). In the following, Section 4.1 describes lower-cost trajectories consistent with the known constraints; Section 4.2 describes how to sample such trajectories; Section 4.3 describes how to get more information from unsafe trajectories; Section 4.4 describes details and extensions to Problem 2. ‣ 3.2 Inverse constraint learning problem ‣ 3 Preliminaries and Problem Statement ‣ Learning Constraints from Demonstrations"); Section 4.5 discusses how to extend our method to suboptimal demonstrations. The complete flow of our method is described in Algorithm 2.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Trajectories satisfying known constraints", "weight": 1.0} -->

Consider the forward problem (Problem 1. ‣ 3.1 Forward optimal control problem ‣ 3 Preliminaries and Problem Statement ‣ Learning Constraints from Demonstrations")).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Trajectories satisfying known constraints", "weight": 1.0} -->

In this paper, we deal with the known constraints from the system dynamics, the control limits, and task-dependent start and goal state constraints. Hence, $\mathcal{T}_{\overline{\mathcal{S}}} = {\mathcal{D}^{\xi_{xu}} \cap \mathcal{U}^{\xi_{xu}}}$, where $\mathcal{D}^{\xi_{xu}}$ denotes the set of dynamically feasible trajectories and $\mathcal{U}^{\xi_{xu}}$ denotes the set of trajectories using controls in $\mathcal{U}$ at each time-step. $\mathcal{T}_{\mathcal{S}_{\Pi}}$ denotes trajectories satisfying start and goal constraints. We develop the method for discrete time trajectories, but analogous definitions hold in continuous time.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Sampling trajectories satisfying known constraints", "weight": 1.0} -->

We sample from $\mathcal{T}_{\mathcal{A}}^{\xi_{xu}^{\ast}}$ to obtain lower-cost trajectories obeying the known constraints using hit-and-run sampling over the set $\mathcal{T}_{\mathcal{A}}^{\xi_{xu}^{\ast}}$, a method guaranteeing convergence to a uniform distribution of samples over $\mathcal{T}_{\mathcal{A}}^{\xi_{xu}^{\ast}}$ in the limit; the method is detailed in Algorithm 1 and an illustration is shown in Figure 2. Hit-and-run starts from an initial point within the set, chooses a direction uniformly at random, moves a random amount in that direction such that the new point remains within the set, and repeats.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Sampling trajectories satisfying known constraints", "weight": 1.0} -->

Depending on the convexity of the cost function and the control constraints and on the form of the dynamics, different sampling techniques can be used, organized in Table 1. The following sections describe each sampling method.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Ellipsoid hit-and-run", "weight": 1.0} -->

\cap \mathcal{D}^{\xi_{xu}}}$ is an ellipsoid in the trajectory space, which can be efficiently sampled via a specially-tailored hit-and-run method. Here, the quadratic cost is written as ${c{(\xi_{xu})}} \doteq {\xi_{xu}^{\top}V\xi_{xu}}$, where $V$ is a matrix of cost parameters, and we omit the control and task constraints for now. Without dynamics, the endpoints of the line $\mathcal{L}$, $L_{-},L_{+}$, (c.f. Alg. 1), can be found by solving a quadratic equation ${{({\xi_{xu} + {\betar}})}^{\top}V{({\xi_{xu} + {\betar}})}} = {\xi_{xu}^{\ast^{\top}}V\xi_{xu}^{\ast}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Ellipsoid hit-and-run", "weight": 1.0} -->

We show that this can still be done with linear dynamics by writing $\mathcal{T}_{\mathcal{A}}^{\xi_{xu}^{\ast}}$ in a special way. $\mathcal{D}^{\xi_{xu}}$ can be written as an eigenspace of a singular "dynamics consistency" matrix, $D_{1}$, which converts any arbitrary state-control trajectory to one that satisfies the dynamics, one time-step at a time.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Ellipsoid hit-and-run", "weight": 1.0} -->

that fixes the controls and the initial state and performs a one-step rollout, replacing the second state with the dynamically correct state. In Eq. 5, we denote by ${\overset{\sim}{x}}_{t + 1}$ a state that cannot be reached by applying control $u_{t}$ to state $x_{t}$. Multiplying the one-step corrected trajectory ${\hat{\xi}}_{xu}$ by $D_{1}$ again changes ${\overset{\sim}{x}}_{3}$ to the dynamically reachable state $x_{3}$. Applying $D_{1}$ to the original $T$-time-step infeasible trajectory $T - 1$ times results in a dynamically feasible trajectory, $\xi_{xu}^{\text{feas}} = {D_{1}^{T - 1}\xi_{xu}}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Ellipsoid hit-and-run", "weight": 1.0} -->

Further, note that the set of dynamically feasible trajectories is $\mathcal{D}^{\xi_{xu}} \doteq \left. \{\xi_{xu} \middle| {{D_{1}\xi_{xu}} = \xi_{xu}}\} \right.$, which is the span of the eigenvectors of $D_{1}$ associated with eigenvalue $1$. Thus, obtaining a feasible trajectory via repeated multiplication is akin to finding the eigenspace via power iteration. One can also interpret this as propagating through the dynamics with a fixed control sequence.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Ellipsoid hit-and-run", "weight": 1.0} -->

We deal with control constraints separately, as the intersection of $\mathcal{U}^{\xi_{xu}}$ and Eq. 6 is in general not an ellipsoid. To ensure control constraint satisfaction, we reject samples with controls outside of $\mathcal{U}^{\xi_{xu}}$; this works if $\mathcal{U}^{\xi_{xu}}$ is not measure zero.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Ellipsoid hit-and-run", "weight": 1.0} -->

For task constraints, we ensure all sampled rollouts obey the goal constraints by adding a large penalty term to the cost function: ${\overset{\sim}{c}{( \cdot )}} \doteq {{c{( \cdot )}} + {\alpha_{c}{\|{x_{g} - x_{T}}\|}_{2}^{2}}}$, where $\alpha_{c}$ is a large scalar, which can be incorporated into Eq. 6 by modifying $V$ and including $x_{g}$ in $\xi_{xu}$; all trajectories sampled in this modified set satisfy the goal constraints to an arbitrarily small tolerance $\varepsilon$, depending on the value of $\alpha_{c}$. The start constraint is satisfied trivially: all rollouts start at $x_{s}$. Note the demonstration cost remains the same, since the demonstration satisfies the start and goal constraints; this modification is made purely to ensure these constraints hold for sampled trajectories.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Convex hit-and-run", "weight": 1.0} -->

For general convex cost functions, the same sampling method holds, but $L_{+},L_{-}$ cannot be found by solving a quadratic function. Instead, we solve ${c{({\xi_{xu} + {\betar}})}} = {c{(\xi_{xu}^{\ast})}}$ via a root finding algorithm or line search.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Non-convex hit-and-run", "weight": 1.0} -->

If $\mathcal{T}_{\mathcal{A}}^{\xi_{xu}^{\ast}}$ is non-convex, $\mathcal{L}$ can now in general be a union of disjoint line segments. In this scenario, we perform a "backtracking" line search by setting $\beta$ to lie in some initial range: $\beta \in {\lbrack\underset{¯}{\beta},\overline{\beta}\rbrack}$; sampling $\beta_{s}$ within this range and then evaluating the cost function to see whether or not $\xi_{xu} + {\beta_{s}r}$ lies within the intersection.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Non-convex hit-and-run", "weight": 1.0} -->

If it does, the sample is kept and hit-and-run proceeds normally; if not, then the range of possible $\beta$ values is restricted to $\lbrack\beta_{s},\overline{\beta}\rbrack$ if $\beta_{s}$ is negative, and $\lbrack\underset{¯}{\beta},\beta_{s}\rbrack$ otherwise. Then, new $\beta$s are re-sampled until either the interval length shrinks below a threshold or a feasible sample is found. This altered hit-and-run technique still converges to a uniform distribution on the set in the limit, but has a slower mixing time than for the convex case, where mixing time describes the number of samples needed until the total variation distance to the steady state distribution is less than a small threshold. Further, we accelerate sampling spread by relaxing the goal constraint to a larger tolerance $\hat{\varepsilon} > \varepsilon$ but keeping only the trajectories reaching within $\varepsilon$ of the goal.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Improving learnability using cost function structure", "weight": 1.0} -->

Input: ξs = {ξ1*, …, ξNs*}, cΠ (⋅), known constraints}
3 if lin., quad., conv. then
6 else if lin., conv., conv. then
14 if prior, continuous then
16else if prior, binary then
Algorithm 2 Overall method

<!-- chunk {"id": "body-0037", "role": "body", "section": "Improving learnability using cost function structure", "weight": 1.0} -->

Naïvely, the sampled unsafe trajectories may provide little information. Consider an unsafe, length-$T$ discrete-time trajectory $\xi$, with start and end states in the safe set. This only says there exists at least one intermediate unsafe state in the trajectory, but says nothing directly about which state was unsafe. The weakness of this information can be made concrete using the notion of a version space. In machine learning, the version space is the set of consistent hypotheses given a set of examples. In our setting, hypotheses are possible unsafe sets, and examples are the safe and unsafe trajectories. Knowing $\xi$ is unsafe only disallows unsafe sets that mark every element of the constraint space that $\xi$ traverses as safe: ${({{\mathcal{O}{(z_{2})}} = 0})} \land \ldots \land {({{\mathcal{O}{(z_{T - 1})}} = 0})}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Improving learnability using cost function structure", "weight": 1.0} -->

If $\mathcal{C}$ is gridded into $G$ cells, this information invalidates at most $2^{{G - T} + 2}$ out of $2^{G}$ possible unsafe sets. We could do exponentially better if we reduced the number of cells that $\xi$ implies could be unsafe.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Improving learnability using cost function structure", "weight": 1.0} -->

We can achieve this by sampling sub-segments (or sub-trajectories) of the larger demonstrations, holding other portions of the demonstration fixed. For example, say we fix all but one of the points on $\xi$ when sampling unsafe lower-cost trajectories. Since only one state can be different from the known safe demonstration, the unsafeness of the trajectory can be uniquely localized to whatever new point was sampled: then, this trajectory will reduce the version space by at most a factor of $2$, invalidating at most ${2^{G} - 2^{G - 1}} = 2^{G - 1}$ unsafe sets. One can sample these sub-trajectories in the full-length trajectory space by fixing appropriate waypoints during sampling: this ensures the full trajectory has lower cost and only perturbs desired waypoints.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Improving learnability using cost function structure", "weight": 1.0} -->

However, to speed up sampling, sub-trajectories can be sampled directly in the lower dimensional sub-trajectory space if the cost function $c{( \cdot )}$ that is being optimized is strictly monotone: for any costs ${c_{1},c_{2}} \in {\mathbb{R}}$, control $u \in \mathcal{U}$, and state $x \in \mathcal{X}$, $c_{1} < c_{2}\Rightarrow{h{(c_{1},x,u)}} < {h{(c_{2},x,u)}}$, for all $x,u$, where $h{(c,x,u)}$ represents the cost of starting with initial cost $c$ at state $x$ and taking control $u$. Strictly monotone cost functions include separable cost functions with additive or multiplicative stage costs, which are common in motion planning and optimal control.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Improving learnability using cost function structure", "weight": 1.0} -->

If the cost function is strictly monotone, we can sample lower-cost trajectories from sub-segments of the optimal path; otherwise it is possible that even if a new sub-segment with lower cost than the original sub-segment were sampled, the full trajectory containing the sub-segment could have a higher cost than the demonstration.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Integer program formulation", "weight": 1.0} -->

After sampling, we can solve Problem 3.2. ‣ 3.2 Inverse constraint learning problem ‣ 3 Preliminaries and Problem Statement ‣ Learning Constraints from Demonstrations") to find an unsafe set consistent with the safe and unsafe trajectories. We now discuss the details of this process. Conservative estimate: One can obtain a conservative estimate of the unsafe set $\mathcal{A}$ from Problem 3.2. ‣ 3.2 Inverse constraint learning problem ‣ 3 Preliminaries and Problem Statement ‣ Learning Constraints from Demonstrations") by intersecting all possible solutions: if the unsafeness of a cell is shared across all feasible solutions, that cell must be occupied. In practice, it may be difficult to directly find all solutions to the feasibility problem, as in the worst case, finding the set of all feasible solutions is equivalent to exhaustive search in the full gridded space. A more efficient method is to loop over all $G$ grid cells and set each one to be safe, and see if the optimizer can still find a feasible solution. Cells where there exists no feasible solution are guaranteed unsafe. This amounts to solving $G$ binary integer feasibility problems, which can be trivially parallelized.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Integer program formulation", "weight": 1.0} -->

Furthermore, any cells that are known safe (from demonstrations) do not need to be checked. We use this method to compute the "*learned guaranteed unsafe set*", $\mathcal{A}_{l}^{\text{rec}}$, in Section 6.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Integer program formulation", "weight": 1.0} -->

A prior on the constraint: As will be further discussed in Section 5.1, it may be fundamentally impossible to recover a unique unsafe set. If we have some prior on the nature of the unsafe set, such as it being simply connected, or that certain regions of the constraint space are unlikely to be unsafe, we can make the constraint learning problem more well-posed. Assume that this prior knowledge can be encoded in some "energy" function ${E{( \cdot,\ldots, \cdot )}}:{{\{ 0,1\}}^{G}\rightarrow{\mathbb{R}}}$ mapping the set of binary occupancies to a scalar value, which indicates the desirability of a particular unsafe set configuration. Using $E$ as the objective function in Problem 3.2. ‣ 3.2

<!-- chunk {"id": "body-0045", "role": "body", "section": "Problem 4.1 (Inverse binary minimization constraint recovery)", "weight": 1.0} -->

Probabilistic setting and continuous relaxation: A similar problem can be posed for a probabilistic setting, where grid cell occupancies represent beliefs over unsafeness: instead of the occupancy of a cell being an indicator variable, it is instead a random variable $Z_{i}$, where $Z_{i}$ takes value $1$ with probability $\overset{\sim}{\mathcal{O}}{(Z_{i})}$ and value $0$ with probability $1 - {\overset{\sim}{\mathcal{O}}{(Z_{i})}}$. Here, the occupancy probability function maps cells to occupancy probabilities ${\overset{\sim}{\mathcal{O}}{( \cdot )}}:{\mathcal{Z}\rightarrow{\lbrack 0,1\rbrack}}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Problem 4.1 (Inverse binary minimization constraint recovery)", "weight": 1.0} -->

Trajectories can now be unsafe with some probability. We obtain analogous constraints from the integer program in Section 4.4 in the probabilistic setting. Known safe trajectories traverse cells that are unsafe with probability 0; we enforce this with the constraint ${\sum_{Z_{i} \in {\phi{(\xi_{s_{j}}^{\ast})}}}{\overset{\sim}{\mathcal{O}}{(Z_{i})}}} = 0$: if the unsafeness probabilities are all zero along a trajectory, then the trajectory must be safe.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Problem 4.2 (Inverse continuous minimization constraint recovery)", "weight": 1.0} -->

When $p_{k} = 1$, for all $k$ (i.e. all unsafe trajectories are unsafe for sure), this probabilistic formulation coincides with the continuous relaxation of Problem 4.1. ‣ 4.4 Integer program formulation ‣ 4 Method ‣ Learning Constraints from Demonstrations"). This justifies interpreting the solution of the continuous relaxation as occupancy probabilities for each cell. Note that Problem 4.1. ‣ 4.4 Integer program formulation ‣ 4 Method ‣ Learning Constraints from Demonstrations") and 4.2. ‣ 4.4 Integer program formulation ‣ 4 Method ‣ Learning Constraints from Demonstrations") have no conservativeness guarantees and use prior assumptions to make the problem more well-posed. However, we observe that they improve constraint recovery in our experiments.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Bounded suboptimality of demonstrations", "weight": 1.0} -->

If we are given a $\delta$-suboptimal demonstration $\hat{\xi}$, where ${c{(\xi^{\ast})}} \leq {c{(\hat{\xi})}} \leq {{({1 + \delta})}c{(\xi^{\ast})}}$, where $\xi^{\ast}$ is an optimal demonstration, we can still apply the sampling techniques discussed in earlier sections, but we must ensure that sampled unsafe trajectories are truly unsafe: a sampled trajectory $\xi^{\prime}$ of cost ${c{(\xi^{\prime})}} \geq {c{(\xi^{\ast})}}$ can be potentially safe. Two options follow: one is to only keep trajectories with cost less than $\frac{c{(\hat{\xi})}}{1 + \delta}$, but this can cause little to be learned if $\delta$ is large.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Bounded suboptimality of demonstrations", "weight": 1.0} -->

Instead, if we assume a distribution on suboptimality, i.e. given a trajectory of cost $c{(\hat{\xi})}$, we know that a trajectory of cost ${c{(\xi^{\prime})}} \in {\lbrack\frac{c{(\hat{\xi})}}{1 + \delta},{c{(\hat{\xi})}}\rbrack}$ is unsafe with probability $p_{k}$, we can then use these values of $p_{k}$ to solve Problem 4.2. ‣ 4.4 Integer program formulation ‣ 4 Method ‣ Learning Constraints from Demonstrations"). We implement this in the experiments.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Analysis", "weight": 1.0} -->

Due to space, the proofs/more remarks can be found in the appendix.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Learnability", "weight": 1.0} -->

We provide analysis on the learnability of unsafe sets, given the known constraints and cost function. Most analysis assumes unsafe sets defined over the state space: $\mathcal{A} \subseteq \mathcal{X}$, but we extend it to the feature space in Corollary 5.9. ‣ 5.2 Conservativeness ‣ 5 Analysis ‣ Learning Constraints from Demonstrations"). We provide some definitions and state a result bounding $\mathcal{A}_{l}$, the set of all states that can be learned guaranteed unsafe.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conservativeness", "weight": 1.0} -->

We discuss conditions on $\mathcal{A}$ and discretization which ensure our method provides a conservative estimate of $\mathcal{A}$. For analysis, we assume $\mathcal{A}$ has a Lipschitz boundary. We begin with notation (explanatory illustrations are in Section A.2):

<!-- chunk {"id": "body-0053", "role": "body", "section": "Evaluations", "weight": 1.0} -->

We provide an example showing the importance of using unsafe trajectories, and experiments showing that our method generalizes across system dynamics, that it works with discretization and suboptimal demonstrations, and that it learns a constraint in a feature space from a single demonstration. See Appendix B for parameters, cost functions, the dynamics, control constraints, and timings.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Evaluations", "weight": 1.0} -->

Version space example: Consider a simple $5 \times 5$ 8-connected grid world in which the tasks are to go from a start to a goal, minimizing Euclidean path length while staying out of the unsafe "U-shape", the outline of which is drawn in black (Fig. 3). Four demonstrations are provided, shown in Fig. 3 on the far left. Initially, the version space contains $2^{25}$ possible unsafe sets. Each safe trajectory of length $T$ reduces the version space at most by a factor of $2^{T}$, invalidating at most $2^{25} - 2^{25 - T}$ possible unsafe sets. Unsafe trajectories are computed by enumerating the set of trajectories going from the start to the goal at lower cost than the demonstration. The numbers of unsafe sets consistent with the safe and unsafe trajectories for varying numbers of safe trajectories are given in Table 2.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Evaluations", "weight": 1.0} -->

Ultimately, it is impossible to distinguish between the three unsafe sets on the right in Fig. 3. This is because there exists no task where a trajectory with cost lower than the demonstration can be sampled which only goes through one of the two uncertain states. Further, though the uncertain states are in the $\Deltax$ shell of the constraint, due to the limitations of the cost function, we can only learn a subset of that shell (c.f. Theorem 5.2). ‣ 5.1 Learnability ‣ 5 Analysis ‣ Learning Constraints from Demonstrations")).

<!-- chunk {"id": "body-0056", "role": "body", "section": "Evaluations", "weight": 1.0} -->

There are two main takeaways from this experiment. First, by generating unsafe trajectories, we can reduce the uncertainty arising from the ill-posedness of constraint learning: after 4 demonstrations, using unsafe demonstrations enables us to reduce the number of possible constraints by nearly a factor of 100, from 256 to 3. Second, due to limitations in the cost function, it may be impossible to recover a unique unsafe set, but the version space can be reduced substantially by sampling unsafe trajectories.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Evaluations", "weight": 1.0} -->

Dynamics and discretization: Experiments in Fig. 4 show that our method can be applied to several types of system dynamics, can learn non-convex/multiple unsafe sets, and can use continuous trajectories. The dynamics, control constraints, and cost functions for each experiment are given in Table 5 in Appendix B. All unsafe sets $\mathcal{A}$ are open sets. We solve Problems 4.1. ‣ 4.4 Integer program formulation ‣ 4 Method ‣ Learning Constraints from Demonstrations") and 4.2.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Evaluations", "weight": 1.0} -->

‣ 4.4 Integer program formulation ‣ 4 Method ‣ Learning Constraints from Demonstrations"), with an energy function promoting smoothness by penalizing squared deviations of the occupancy of a grid cell $z_{i}$ from its 4-connected neighbors $N{(z_{i})}$: $\sum_{i = 1}^{G}{\sum_{z_{j} \in {N{(z_{i})}}}{\|{{\mathcal{O}{(z_{i})}} - {\mathcal{O}{(z_{j})}}}\|}_{2}^{2}}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Evaluations", "weight": 1.0} -->

In all experiments, the mean squared error (MSE) is computed as $\frac{1}{G}\sqrt{\sum_{i = 1}^{G}{\|{{\mathcal{O}{(z_{i})}^{\ast}} - {\mathcal{O}{(z_{i})}}}\|}_{2}^{2}}$, where $\mathcal{O}{(z_{i})}^{\ast}$ is the ground truth occupancy. The demonstrations are color-matched with their corresponding number on the $x$-axis of the MSE plots. For experiments with more demonstrations, only those causing a notable change in the MSE were color-coded. The learned guaranteed unsafe states $\mathcal{A}_{l}^{\text{rec}}$ are colored red on the left column.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Evaluations", "weight": 1.0} -->

We recover a non-convex "U-shaped" unsafe set in the state space using trivial 2D single-integrator dynamics (row 1 of Fig. 4). The solutions to both Problems 4.2. ‣ 4.4 Integer program formulation ‣ 4 Method ‣ Learning Constraints from Demonstrations") and 4.1. ‣ 4.4 Integer program formulation ‣ 4 Method ‣ Learning Constraints from Demonstrations") return reasonable results, and the solution of Problem 4.1. ‣ 4.4 Integer program formulation ‣ 4 Method ‣ Learning Constraints from Demonstrations") achieves zero error. The second row shows learning two polyhedral unsafe sets in the state space with 4D double integrator linear dynamics, yielding similar results. We note the linear interpolation of some demonstrations in row 1 and 2 enter $\mathcal{A}$; this is because both sets of dynamics are in discrete time and only the discrete waypoints must stay out of $\mathcal{A}$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Evaluations", "weight": 1.0} -->

The third row shows learning a polyhedral unsafe set in the state space, with time-discretized continuous, nonlinear Dubins' car dynamics, which has a 3D state $x \doteq \begin{bmatrix}
\end{bmatrix}^{\top}$. These dynamics are more constrained than the previous cases, so sampling lower cost trajectories becomes more difficult, but despite this we can still achieve near zero error solving Problem 4.1. ‣ 4.4 Integer program formulation ‣ 4 Method ‣ Learning Constraints from Demonstrations"). Some over-approximation results from some sampled unsafe trajectories entering regions not covered by the safe trajectories. For example, the cluster of red blocks to the top left of $\mathcal{A}$ is generated by lower-cost trajectories that trade off the increased cost of entering the top left region by entering $\mathcal{A}$. This phenomenon is consistent with Theorem A.16.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Evaluations", "weight": 1.0} -->

‣ A.2 Conservativeness ‣ Appendix A Analysis ‣ Learning Constraints from Demonstrations"); we recover a set that is contained within $\mathcal{A}{(f_{\Deltax}{\lbrack{(0,T_{\text{max}}\rbrack})}}$ (the maximum trajectory length $T_{\text{max}}$ was 14.1 seconds). Learning curve spikes occur when overapproximation occurs. Overall, we note $\mathcal{A}_{l}^{\text{rec}}$ tends to be a significant underapproximation of $\mathcal{A}$ due to the chosen cost function and limited demonstrations. For example, in row 1 of Fig. 4, $\mathcal{A}_{l}^{\text{rec}}$ cannot contain the portion of $\mathcal{A}$ near long straight edges, since there exists no shorter path going from any start to any goal with only one state within that region.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Evaluations", "weight": 1.0} -->

For row 3 of Fig. 4, we learn less of the bottom part of $\mathcal{A}$ due to most demonstrations' start and goal locations making it harder to sample feasible control trajectories going through that region; with more demonstrations, this issue becomes less pronounced.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Evaluations", "weight": 1.0} -->

Suboptimal human demonstrations: We demonstrate our method on suboptimal demonstrations collected via a driving simulator, using a car model with CT Dubins' car dynamics. Human steering commands were recorded as demonstrations, where the task was to navigate around the orange box and drive between the trees (Fig. 5). For a demonstration of cost $c$, trajectories with cost less than $0.9c$ were believed unsafe with probability 1. Trajectories with cost $c^{\prime}$ in the interval $\lbrack{0.9c},c\rbrack$ were believed unsafe with probability $1 - {({{{({c^{\prime} - {0.9c}})}/0.1}c})}$. MSE for Problem 4.2. ‣ 4.4 Integer program formulation ‣ 4 Method ‣ Learning Constraints from Demonstrations") is shown in Fig. 5 (Problem 4.1. ‣ 4.4 Integer program formulation ‣ 4 Method ‣ Learning Constraints from Demonstrations") is not solved since the probabilistic interpretation is needed).

<!-- chunk {"id": "body-0065", "role": "body", "section": "Evaluations", "weight": 1.0} -->

The maximum trajectory length $T_{\text{max}}$ is $19.1$ seconds; hence, despite suboptimality, the learned guaranteed unsafe set is a subset of $\mathcal{A}{(f_{\Deltax}{({\lbrack 0,T_{\text{max}}\rbrack})}}$. While the MSE is highest here of all experiments, this is expected, as trajectories may be incorrectly labeled safe/unsafe with some probability.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Evaluations", "weight": 1.0} -->

Feature space constraint: We demonstrate that our framework is not limited to the state space by learning a constraint in a feature space. Consider the scenario of planning a safe path for a mobile robot with continuous Dubins' car dynamics through hilly terrain, where the magnitude of the terrain's slope is given as a feature map (i.e. ${\phi{(x)}} = {\|{\partial{{H{(\hat{x})}}/{\partial\hat{x}}}}\|}_{2}$, where $\hat{x} = {\lbrack{\chiy}\rbrack}^{\top}$ and $H{(\hat{x})}$ is the elevation map). The robot will slip if the magnitude of the terrain slope is too large, so we generate a demonstration which obeys the ground truth constraint ${\phi{(x)}} < 0.05$; hence, the ground truth unsafe set is $\mathcal{A} \doteq \left.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Evaluations", "weight": 1.0} -->

\{ x \middle| {{\phi{(x)}} \geq 0.05}\} \right.$. From one safe trajectory (Fig. 6) generated by RRT\* and gridding the feature space as $\{ 0,0.005,\ldots,0.145,0.15\}$, we recover the constraint ${\phi{(x)}} < 0.05$ exactly.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper we propose an algorithm that learns constraints from demonstrations, which acts as a complementary method to IOC/IRL algorithms. We analyze the properties of our algorithm as well as the theoretical limits of what subset of an unsafe set can be learned from safe demonstrations. The method works well on a variety of system dynamics and can be adapted to work with suboptimal demonstrations. We further show that our method can also learn constraints in a feature space. The largest shortcoming of our method is the constraint space gridding, which yields a complex constraint representation and causes the method to scale poorly to higher dimensional constraints. We aim to remedy this issue in future work by developing a grid-free counterpart of our method for convex unsafe sets, which can directly describe standard pose constraints like task space regions.
