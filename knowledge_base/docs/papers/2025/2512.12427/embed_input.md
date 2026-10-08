<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Temporal Cascading of Planning and Control for Quadrotor MPC

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Many aerial tasks involving quadrotors demand both instant reactivity and long-horizon planning for obstacle avoidance, energy efficiency, or trajectory tracking. High-fidelity models enable accurate control but are too slow for long horizons. Low-fidelity planners scale but cannot directly control the system, necessitating cascaded architectures. Prevailing hierarchical approaches plan with a simplified model and use a high-fidelity controller for tracking, yet this decomposition is inherently suboptimal. The controller is limited by the coarse plan, and conventional MPC alternatives shorten the horizon to stay real-time feasible. We present UNIQUE, an MPC architecture that replaces this hierarchical stacking with temporal cascading. The planning problem is formulated as the second-tail horizon of a single multi-phase MPC, rather than being solved separately. We align costs across horizons, derive feasibility constraints for the point-mass planning model, and introduce transition constraints that convert high-fidelity states into meaningful low-fidelity states. Parallel point-mass and mixed-integer solvers address nonconvexities while incorporating progressive 3D obstacle smoothing over the planning horizon.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In simulations and real flights, under equal computational budgets, UNIQUE improves closed-loop tracking by up to 75% compared with standard MPC and hierarchical baselines. Ablations and Pareto analyses confirm performance gains across variations in horizon, constraint approximations, and smoothing schedules.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fast and safe autonomous quadrotor flight depends on two competing requirements: *fast feedback* to disturbances and dynamics, and *planning* to reason over long horizons for obstacle avoidance, efficiency, and mission objectives. Optimizing a high-fidelity quadrotor model over such horizons is typically intractable in real time, causing the long-standing separation between planning and control for quadrotors.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fig. 1: Conceptual sketch of Unique. We employ a multi-phase MPC with two horizons: a high-fidelity control horizon and a long horizon with a lower-fidelity point-mass model, enabling long-horizon planning. Local minima of the gradient-based optimizer are avoided by (i) smoothing obstacle shapes along the horizon, and (ii) running parallel planners solely for the computationally cheap low-fidelity model on the second horizon. Whenever the cost on the low-fidelity planning horizon of such a parallel MPC is lower, the second horizon of the multi-phase MPC is reinitialized by the corresponding optimization variables.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hierarchical architectures compute a long-horizon plan using a simplified model, such as a point mass or a polynomial model, and track it with an MPC. This hierarchical decomposition is inherently suboptimal. The asynchronously computed low-fidelity plan cannot account for the true vehicle dynamics, leading to (i) performance limitations imposed by the coarse plan, (ii) redundant optimization in the initial horizon, and (iii) conflicting inner or outer loops that may create infeasibilities or unstable behavior. Pure MPC alternatives retain the high-fidelity model but shorten the horizon to remain real-time feasible, relying on a terminal cost and set that are difficult to obtain for complex scenes involving moving obstacles or nonlinear constraints and are prone to local minima in nonsmooth environments. Remarkably, the planning problem remains NP-hard, yet heuristics and tailored algorithms often make it computationally tractable.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our pivotal idea is to replace the conventional hierarchical planner-controller decomposition with a *temporal cascading* of planning and control inside a single MPC. Rather than computing a plan separately and tracking it, we embed the planning problem as the second tail horizon of a multi-phase MPC, as sketched in Fig. 1. This is motivated by the fact that an MPC, in general, aims to optimize the same underlying task objective and aims to satisfy the same constraints as the planning problem. We observe that (i) the geometric planning around obstacles is predominantly a long-horizon problem with negligible influence on the short control horizon, and (ii) a point-mass planner can be solved very fast within each closed-loop iteration. Therefore, we formulate the planning problem as finding the optimal tail trajectory on the second horizon, given that we can effectively convert high-fidelity states into meaningful low-fidelity states and map constraints from the high- to the low-fidelity model, which we show to be possible for quadrotors. The two phases are coupled by transition constraints that align (i) position and velocity, (ii) thrust-induced acceleration, and (iii) jerk/body-rate relations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Cost terms are aligned across horizons, allowing the controller to optimize a consistent objective. To improve numerical robustness over long horizons with sharp geometry, we adapt progressive smoothing of norm-based obstacle models for 3D shapes, morphing cube-like sets to ellipsoids with increasing prediction time, which improves RTI ([RTI]) convergence.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The two-phase formulation alone converges well around local minima, but planning problems often involve severe nonconvexities. Therefore, we propose a parallel computation strategy in which we compare the tail trajectory of the main MPC with alternative solutions that may achieve a lower predicted cost. Randomly initialized point-mass solvers run in parallel and, as we show, finish faster than the two-phase MPC, enabling synchronous cost comparison after each [RTI] step. For harder combinatorial problems, we additionally deploy a potentially slower global planner, in our case a mixed-integer planner as used by many state-of-the-art planning algorithms, which first initializes a guaranteed fast parallel point-mass solver. Only the latter's converged cost is compared to the main MPC, ensuring synchronous evaluation. Once the cost of one parallel MPC is lower than the cost along the second horizon of the multi-phase MPC, the solver variables are initialized with the lower-cost solution of the corresponding parallel MPC. In summary, our contributions are as follows: Temporal planning paradigm.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose to formulate the planning problem not hierarchically but as the tail horizon of an MPC, yielding a sequential controller-planner structure within a single optimization.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Two-phase MPC architecture for quadrotors. A single optimization that couples a high-fidelity quadrotor model with a long-horizon point-mass model via equality constraints on position/velocity, thrust-acceleration, and jerk-body-rate mappings, with cost alignment across horizons. We show that high-fidelity states can be effectively converted into meaningful low-fidelity states for quadrotors.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Feasibility-preserving low-fidelity constraints. Derivation and tractable inner approximations of thrust and body-rate safe sets for the point-mass model that ensure compatibility with high-fidelity actuator and rate limits.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Parallel tail-horizon re-planning. A parallel computation strategy that compares the tail trajectory of the main MPC against alternative solutions from randomly initialized point-mass solvers.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Pareto-superior control performance. Under equal computational budgets, the two-phase formulation achieves better closed-loop performance than extending the high-fidelity MPC horizon.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Comprehensive evaluation. Simulations and real flights show substantial closed-loop gains over standard MPC and hierarchical baselines under equal compute budgets, including Pareto analyses across horizon variations and feasibility approximations, as well as demonstrations of long-horizon planning with iteration times below $5\,\mathrm{\mathrm{ms}}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Unique framework lowers the planning-control performance gap by treating planning as a tail-horizon problem of MPC rather than a separate hierarchical stage. In obstacle-rich tasks, we observe up to $75\%$ lower closed-loop cost compared to standard MPC and hierarchical designs, while reducing online computation compared to long-horizon, high-fidelity MPC.

<!-- chunk {"id": "body-0017", "role": "body", "section": "I-A Outline", "weight": 1.0} -->

Following the related work in Sec. II, Sec. III formalizes the nominal high-fidelity MPC. Section IV introduces the point-mass planning model and derives feasibility sets. Section V presents the unified formulation, including cost/constraint alignment, transition constraints, progressive smoothing, the parallel MPC framework, and the numerical approximations for real-time efficiency. Section VI describes the experimental setup, Section VII reports real-world experiments, and Section VIII presents simulated ablations. We conclude with limitations and future directions in Section IX.

<!-- chunk {"id": "body-0018", "role": "body", "section": "I-B Notation", "weight": 1.0} -->

For the quaternion rotation of a vector $x\in\mathbb{R}^{3}$ and a quaternion $q\in\mathbb{R}^{4}$, we use $q\odot x$, and for the quaternion multiplication with a second quaternion $p\in\mathbb{R}^{4}$, we use $q\cdot p$. A power $p$ of a vector $x\in\mathbb{R}^{n}$ is taken element wise, with $x^{p}=[x_{1}^{p},\ldots,x_{n}^{p}]^{\top}$. When using different models along an MPC horizon, we refer to the trajectory parts as *phases*.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Nominal Controller", "weight": 1.0} -->

In the following, we describe the nominal nonlinear MPC that serves as a basis for Unique. First, the high-fidelity model is introduced, followed by the essential system constraints, obstacle constraints, and the MPC formulation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A High-Fidelity Control Model", "weight": 1.0} -->

The high-fidelity quadrotor is modeled following as a 6-degree-of-freedom rigid body with mass $m$ and a diagonal moment of inertia matrix ${J}=\mathrm{diag}(\begin{bmatrix}J_{x}&J_{y}&J_{z}\end{bmatrix}).$ The model includes the positions $p\in\mathbb{R}^{3}$, velocities in the world coordinate frame $v\in\mathbb{R}^{3}$, orientation formulated as quaternions $q\in S^{3}\subset\mathbb{R}^{4}$, body rates $\omega\in\mathbb{R}^{3}$, single rotor thrusts $f_{i}^{\top}=\begin{bmatrix}0&0&f_{z,i}\end{bmatrix}$ with $i\in\{1,2,3,4\}$ and the collective z-components of the single rotor thrusts

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A High-Fidelity Control Model", "weight": 1.0} -->

Thrusts are generated by the rotors with the rotor speed $\Omega_{i}$ and the geometric location $r_{\mathrm{p},i}\in\mathbb{R}^{3}$ of the $i$-th rotor in the body frame via $f_{z,i}=\Omega_{i}^{2}c_{l}$ using the thrust coefficient $c_{\mathrm{l}}\in\mathbb{R}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A High-Fidelity Control Model", "weight": 1.0} -->

The residual force $f_{\mathrm{res}}(v_{\mathcal{B}},\Omega^{2})$ models aerodynamic effects and is obtained by fitting selected features of $\Omega^{2}$ and velocities $v_{\mathcal{B}}$ to measured data. The literature proposes either higher-order polynomials or linear features of only the velocity $v_{\mathcal{B}}$. We use a higher-order polynomial for a high-fidelity residual model.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A High-Fidelity Control Model", "weight": 1.0} -->

In addition to translation forces, we compute rotational counter-torques of the rotors via In symmetric setups, the coefficients $\kappa_{i}$ are equal in absolute value and have pairwise the same sign, i.e., $\kappa_{1}=-\kappa_{2}=\kappa_{3}=-\kappa_{4}$. By adding the torque originating from the single rotor thrusts to the counter torques, the collective torque is With the gravity vector $g^{\top}=\begin{bmatrix}0&0&9.81\,\mathrm{m/s^{2}}\end{bmatrix}$ and the high-fidelity state the quadrotor dynamics are finally written as A simplified version of uses linear residual forces, which were shown to be differentially flat, cf. the supplementary material.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Quadrotor System Constraints", "weight": 1.0} -->

Quadrotors are typically constrained by maximum and minimum rotor speeds, resulting in maximum and minimum single rotor thrusts $\overline{f_{z}}$ and $\underline{f_{z}}$. Most quadrotors are equipped with a low-level tracking controller that takes the body rates and collective thrust as inputs. Therefore, constraints are expressed as constraints $\overline{\omega}_{xy}\in\mathbb{R}$ on the body rate for roll and pitch, and the total collective thrust $\overline{f}_{\mathrm{th}}$ and $\underline{f}_{\mathrm{th}}$, written as We constrain the quadrotor to an operating region with a maximum vertical speed of $\overline{v}_{z}\in\mathbb{R}$ and horizontal speed $\overline{v}_{xy}\in\mathbb{R}$, with

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Obstacle Avoidance Constraints", "weight": 1.0} -->

We consider convex obstacle shapes that can be described by $p$-norms, including ellipsoids and cubes. An obstacle is described by the tuple $\theta=(p_{o},R_{o},d_{o},\alpha_{0})$ with the obstacle center $p_{o}\in\mathbb{R}^{3}$, the orientation normal vectors $u_{o},v_{o},w_{o}\in\mathbb{R}^{3}$, with the rotation matrix $R_{o}=\begin{bmatrix}u_{o}&v_{o}&w_{o}\end{bmatrix}$, the obstacle scale parameters $d_{o}^{\top}=\begin{bmatrix}d_{x}&d_{y}&d_{z}\end{bmatrix}$, and the norm or shape parameter $\alpha_{o}\geq 2$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Obstacle Avoidance Constraints", "weight": 1.0} -->

The transformation is used to obtain normalized obstacle coordinates $\eta(p)$ and describe the occupied space via the set where a parameter $\alpha\geq 2$ defines the shape of the obstacle. The smoothness parameter $\alpha=2$ corresponds to an ellipsoid and $\alpha\rightarrow\infty$ to a cuboid, see Fig. 2. Note that is a scaled norm, where lower values of $\alpha$ are always over-approximations of larger $\alpha$, i.e., $2\leq\alpha_{1}\leq\alpha_{2}\Rightarrow\mathcal{O}(\alpha_{2})\subseteq\mathcal{O}(\alpha_{1})$, cf.. Accordingly, $d_{o}$ denotes the scale before the factor $3^{1/\alpha}$ induced by this normalized norm.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Obstacle Avoidance Constraints", "weight": 1.0} -->

Fig. 2: Obstacle representations. Visualization of a cubic obstacle smoothed along the high-fidelity horizon (blue) for α = 100, 8, and 6. Along the low-fidelity horizon, cubic obstacles can be further smoothed, as shown here for α = 6 to 4. The mixed-integer planner requires a polyhedral over-approximation due to the convex decomposition of the free planning space.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-D Convex Configuration Space Decomposition", "weight": 1.0} -->

The collision constraints are most naturally expressed after a decomposition of the collision-free workspace, generally referred to as *exact cell decomposition*. The general procedure is as follows. The boundary primitives of the inflated obstacles represent a partition of the workspace. For polyhedral obstacles, these primitives are supporting hyperplanes of obstacle facets. For curved obstacles, a conservative polyhedral approximation is used. Intersecting this arrangement with the workspace yields a set of cells whose interiors are collision-free. Each cell is convex whenever it is defined as the intersection of half-spaces from one arrangement region, and adjacent cells that share the same active inequalities can be merged to reduce the overall number of convex cells. The resulting free space $\mathcal{F}$ is represented as where $C_{j}$ is a convex polytope, $n_{c}$ are the number of convex sets, and $H_{j}\in\mathbb{R}^{m_{j}\times 3}$ and $h_{j}\in\mathbb{R}^{m_{j}}$ describe $m_{j}$ halfspace constraints.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-D Convex Configuration Space Decomposition", "weight": 1.0} -->

Without loss of generality, we consider axis-aligned box obstacles. After obstacle inflation and clipping to the workspace, all obstacle faces and workspace faces define coordinate-wise cut locations to rectangular voxels. Each elementary box induced by these cuts is classified as free or occupied according to whether its midpoint lies in obstacle-free space; contiguous free boxes are first grouped into maximal connected segments along one coordinate direction and are then merged across shared faces in the remaining directions until no further convex merging is possible. Because all cuts are axis-aligned, each final cell is an axis-aligned box which is a particularly simple polyhedral representation of the exact cell decomposition induced by the inflated obstacles. Additionally, a cell adjacency graph is constructed: two cells $C_{i}$ and $C_{j}$ are adjacent if their axis-aligned bounding boxes touch or overlap on every coordinate axis.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Mixed-integer encoding", "weight": 1.0} -->

Let $\beta_{k_{b},j}\in\{0,1\}$ denote whether the trajectory at binary step $k_{b}$ is assigned to cell $C_{j}$. To reduce the number of binary variables, cell-assignment binaries are introduced only at a subset of nodes $\mathcal{K}_{b}=\{s,\,2s,\,\ldots\}\cup\{N\}\subseteq\{1,\ldots,N\}$ with stride $s\geq 1$. Each node $k$ inherits the assignment from the nearest preceding binary step $\kappa(k)=\max\{k_{b}\in\mathcal{K}_{b}:k_{b}\leq k\}$, so that the total number of binary variables is $|\mathcal{K}_{b}|\,n_{c}$ instead of $N\,n_{c}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Mixed-integer encoding", "weight": 1.0} -->

Exactly one cell is selected at each binary step, and the position at every node is forced into the selected cell via indicator constraints, To ensure spatial consistency across the horizon, cell transitions between consecutive binary steps are restricted to neighboring cells in the adjacency graph, for each pair of successive binary steps $k_{b},k_{b}^{\prime}\in\mathcal{K}_{b}$, where $\mathcal{N}(j)$ denotes the set of cells adjacent to $C_{j}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Online pruning", "weight": 1.0} -->

Before each solve, conservative per-axis reachable position bounds are propagated from the current state $x_{0}$ over the planning horizon. At each binary step $k_{b}$, cells whose bounding boxes do not overlap the reachable region are fixed to $\beta_{k_{b},j}=0$, which substantially reduces the effective number of active binary variables without altering feasibility. For node $p_{k}$ and binary variables $\beta_{\kappa(k)}^{\top}=[\beta_{\kappa(k),1},\ldots,\beta_{\kappa(k),n_{c}}]$ the constraints -- and the reachability fixing are summarized by $({P}^{\mathrm{lf}}_{p}{x}^{\mathrm{lf}}_{k},\beta_{\kappa(k)})\in\mathcal{F}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-E Nominal MPC", "weight": 1.0} -->

With sufficient computational resources and a sufficiently good initial guess, we would solve a nominal MPC problem using the highest-fidelity model available. We formulate a multiple-shooting NLP ([NLP]) to solve the MPC problem with state variables $X=\begin{bmatrix}x_{0}&\ldots&x_{M}\end{bmatrix}$ and control variables $U=\begin{bmatrix}u_{0}&\ldots&u_{M-1}\end{bmatrix}$, and use numerical integration to obtain the consecutive states $x_{k+1}$ at discrete times $kt_{\Delta}$ via $x_{k+1}=F(x_{k},u_{k};t_{\Delta})$, particularly an RK4 scheme with sampling time $t_{\Delta}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-E Nominal MPC", "weight": 1.0} -->

A terminal value function $\Phi(x)$ and a terminal set $h_{M}(x_{M})$ approximate the infinite horizon and can establish recursive feasibility under the standard terminal-set invariance assumptions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-E Nominal MPC", "weight": 1.0} -->

With state selection matrices $P_{p}\in\mathbb{R}^{3\times 17}$, $P_{f}\in\mathbb{R}^{4\times 17}$, $P_{v}\in\mathbb{R}^{3\times 17}$ and $P_{\omega}\in\mathbb{R}^{3\times 17}$ that select the states $p$, $f_{z}$, $v$ and $\omega$ of the full state $x$, the nominal MPC problem is defined as We define the nonlinear least-squares cost with the tracking states $y^{\top}(x,u)=\begin{bmatrix}p&\phi(q,\tilde{q})&v&\omega&f_{z}&u\end{bmatrix}\in\mathbb{R}^{20}$ that includes the quaternion error $\phi:\mathbb{R}^{4\times

<!-- chunk {"id": "body-0036", "role": "body", "section": "Low-Fidelity Model", "weight": 1.0} -->

For long-horizon trajectory planning, low-fidelity models are inevitable due to the necessary trade-off between accuracy and computation time per planner iteration. Due to the differential flatness of the quadrotor motion, a chain of integrators is often used to approximately describe the quadrotor motion. In this work, we use a chain of three integrators to model the trajectory of a quadrotor, as proposed in for rapid planning of feasible trajectories. Three integrators, combined with specific constraints, are necessary to generate feasible trajectories for quadrotors.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Low-Fidelity Model", "weight": 1.0} -->

For readability, we overload the notation for positions $p$ and velocities $v$ as for the quadrotor model, and add acceleration states $a\in\mathbb{R}^{3}$ and jerk inputs ${u}^{\mathrm{lf}}:=j\in\mathbb{R}^{3}.$ to obtain the low-fidelity model with the low-fidelity state ${x}^{\mathrm{lf}}=\begin{bmatrix}p&v&a\end{bmatrix}^{\top}.$

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Relation to High-Fidelity Model", "weight": 1.0} -->

Due to the differential flatness of the quadrotor model, all quadrotor states of a simple model with linear residuals can be obtained from derivatives of the position and the orientation of the quadrotor model. The point-mass model, which is a chain of integrators, can be seen as a lower-fidelity model from which we can derive the most important states for motion planning. We are particularly interested in the quadrotor position $p$, velocity $v$, body rate $\omega$, and thrust $T$. These states are typically associated with the optimization objective and constraints related to physical feasibility and safety, as in (2a), (2b) and. A point-mass model formulates derivatives of the position, in our case, up to the jerk. These physical quantities are aligned with the quadrotor motion. From the quadrotor model, the acceleration can be directly obtained via and the jerk via the derivative of the acceleration with details in the supplementary material.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Point-Mass System Constraints", "weight": 1.0} -->

The authors in derived constraints on a third-order point mass model that guarantees feasible trajectories for a quadrotor model with constraints defined in but without residual forces. We extend these constraints to include feasibility for the residual model by utilizing the upper bound $\overline{f}_{\mathrm{res}}$ from Ass. 1. While required decoupled constraints per axis due to their computationally efficient planning algorithm, we utilize nonlinear programming and successive linearization, which allows for coupled, less restrictive constraints. Particularly, the constraint $\mathbb{S}_{\mathrm{f}}$ on the collective thrust (2b) can be formulated with the individual acceleration components $a_{x},a_{y}$ and $a_{z}$ per axis in the world frame for the low-fidelity planning model.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Point-Mass System Constraints", "weight": 1.0} -->

The collective constraint for the low-fidelity model is therefore Body rate constraints $\mathbb{S}_{\omega}$ formulated in (2a) for the high-fidelity model can be incorporated in the low-fidelity point mass model via constraints on the time derivative of the unit vector of the gravity-shifted acceleration, i.e., Resolving the time derivative in and utilizing the explicit notation of jerk with $j=\dot{a}+\dot{g}=\dot{a}$, a conservative sufficient body rate feasibility constraint for the low-fidelity model can be written as The auxiliary constraints on the thrust and the body rate are highly nonlinear. However, they can be conservatively reformulated into more optimization-friendly subsets, as shown in the following, with details.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Point-Mass System Constraints", "weight": 1.0} -->

First, we simplify the lower bound of the thrust constraint $\mathbb{S}_{\mathrm{f}}^{\mathrm{lf}}$ defined. The lower bound of is satisfied if the simpler inequality holds, where $\underline{a}_{z}$ is an auxiliary, more restrictive, bound that is also used in the following to shape the simplified constraints. We refer to for a proof.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B Point-Mass System Constraints", "weight": 1.0} -->

Second, the upper bound of can be simplified, where a more restrictive constraint guarantees the feasibility of. The simplified constraint involves two design parameters $\alpha_{x},\alpha_{z}\in$ that shape and trade off the more optimization-friendly constraints. Define the available thrust margin as $\overline{f}_{\mathrm{av}}:=\overline{f}_{\mathrm{th}}-\overline{f}_{\mathrm{res}}$. By utilizing the design parameters, box-constraints for $\overline{a}^{\top}=\begin{bmatrix}\overline{a}_{x}&\overline{a}_{y}&\overline{a}_{z}\end{bmatrix}$ can be computed iteratively by The simplified box constraints, expressed as a set constraining the acceleration states of the low-fidelity model, can finally be written as which is a subset of the thrust constraints.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B Point-Mass System Constraints", "weight": 1.0} -->

Next, we simplify the constraints of ${\mathbb{S}}^{\mathrm{lf}}_{\omega}$, defined. A more optimization-friendly subset of can be found by exploiting the lower bound on the acceleration to obtain simplified convex constraints on the jerk $j$ Arbitrary box constraints for each individual component of the jerk can be computed, forming a subset of and, therefore, decoupling the constraints. A valid choice would be $\overline{j}_{xyz}=\frac{\underline{a}_{z}+g}{\sqrt{3}}\overline{\omega}_{xy}$ to obtain the convex decoupled box constraints

<!-- chunk {"id": "body-0044", "role": "body", "section": "Unique: The Temporal Cascading MPC Formulation", "weight": 1.0} -->

In the following, we propose Unique, a multi-phase MPC framework that embeds the planning problem as the tail horizon of the controller. Rather than solving the planning problem hierarchically on a separate model and tracking the result, we append the low-fidelity point-mass model from Sect. IV as a second phase after the high-fidelity MPC from Sect. III-E, forming a single optimization that jointly plans and controls. The merging of two different models along the MPC horizons requires (i) the alignment of the cost function, (ii) recursive feasible constraint formulations, (iii) a transition function between the models. Very long prediction horizons result in MPC optimization problems with ubiquitous local minima, which may degrade the performance of the multi-phase MPC, particularly in cluttered environments with nonsmooth obstacle shapes. Two proposed strategies effectively improve performance as part of the Unique framework, i.e., progressive smoothing and parallel low-fidelity optimization from random initial seeds. These strategies and the requirements for merging the two models over the horizon are detailed below.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A Cost Alignment", "weight": 1.0} -->

The high fidelity weights of the nonlinear-least square cost are split into groups for physical states, with $w_{p}\in\mathbb{R}^{3}$ for positions, $w_{v}\in\mathbb{R}^{3}$ for velocities, $w_{\phi}\in\mathbb{R}^{3}$ for Euler angles, $w_{\omega}\in\mathbb{R}^{3}$ for body rates, $w_{f}\in\mathbb{R}^{4}$ for single rotor thrusts and $w_{u}\in\mathbb{R}^{4}$ for its derivatives. The cost for the low-fidelity model is formulated as a linear least-squares cost for the full low-fidelity state via with ${y}^{\mathrm{lf}}=[{x}^{\mathrm{lf}},{u}^{\mathrm{lf}}]^{\top}$ and the weights that are partially aligned with the high-fidelity weights.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A Cost Alignment", "weight": 1.0} -->

In particular, the weights $w_{p}$ and $w_{v}$ are associated with the same physical states and are therefore chosen to be identical.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-A Cost Alignment", "weight": 1.0} -->

In the high-fidelity cost, single-rotor vertical thrusts are penalized by a weighted sum of squares. For equal rotor-thrust component weights $w_{f,0}$ and equal sharing of a collective-thrust variation, $\sum_{i=1}^{4}(\Delta f_{z,i})^{2}=m^{2}\|\Delta a\|^{2}/4$. We therefore use the approximate acceleration-weight alignment $w_{a}:=m^{2}w_{f,0}/4$; attitude, gravity, and residual forces prevent an exact global equivalence.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-A Cost Alignment", "weight": 1.0} -->

The jerk weight $w_{j}$ is related to the body rate weight $w_{\omega}$ and the force derivative input weight $w_{u}$. Similar to the acceleration weight, we take the input weight relation $w_{j}\approx m^{2}w_{u}$ as an approximation and increase it in closed-loop experiments to account for the body rate weight.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-A Cost Alignment", "weight": 1.0} -->

With the simple assumption of considering hovering as a safe state, we can use the corresponding low-level states $P_{va}{x}^{\mathrm{lf}}$, with the projection matrix $P_{va}\in\mathbb{R}^{6\times 9}$ selecting velocities and accelerations, to establish a simple safe terminal constraint ${h}^{\mathrm{lf}}({x}^{\mathrm{lf}})=P_{va}{x}^{\mathrm{lf}}=0.$

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B Constraint Alignment", "weight": 1.0} -->

As shown in Sect. IV-B, we can find constraint sets ${\mathbb{S}}^{\mathrm{lf}}_{\omega}$ and ${\mathbb{S}}^{\mathrm{lf}}_{f}$ for the low-fidelity model that guarantee a feasible trajectory of the high-fidelity model that is constrained via the feasible sets $\mathbb{S}_{\omega}$ and $\mathbb{S}_{f}$. We propose two subset variants of the low-fidelity set ${\mathbb{S}}^{\mathrm{lf}}_{\omega}$ that are more tightly constrained yet numerically easier to solve.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-B Constraint Alignment", "weight": 1.0} -->

The set ${\hat{\mathbb{S}}}^{\mathrm{lf}}_{\omega}$ assumes a lower bound $\underline{a}_{z}$, leading to a convex quadratic constraint on the jerk $j$ and the set $\widehat{\mathbb{S}}_{\mathrm{\omega}}^{\mathrm{lf}}$ decouples the jerk components to box constraints. The constraint alignment guarantees that the plan in the second horizon is a feasible plan for the higher-fidelity drone model.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-C Transition Function", "weight": 1.0} -->

The conditions on the low-fidelity model of the previous Sect. V-B provide necessary conditions on the position trajectory and its derivatives of the high-fidelity model for feasibility. In this section, we develop necessary conditions for the final state of the high-fidelity model $x_{M}$, such that the low-fidelity plan for future times $t\geq Mt_{\Delta}$ can be tracked. Our approach explicitly couples all derivatives of the low-fidelity trajectory, up to and including jerk, to the corresponding high-fidelity states. First, we require the state and velocities of both fidelity models to be aligned via Next, we require the acceleration obtained from the rotor thrusts to be aligned with the acceleration of the low-fidelity model, via Finally, the body rates need to be aligned with the jerk and the acceleration.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-C Transition Function", "weight": 1.0} -->

This follows from the positive lower collective-thrust bound. Additionally, the jerk-related constraint can be interpreted as a constraint to the preceding jerk control before the initial transition state ${x}^{\mathrm{lf}}_{0}$, thus it is not required for the feasibility of the quadrotor model. Finally, we summarize the relevant coupling conditions of and by

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-D Progressive Smoothing", "weight": 1.0} -->

Within Unique, we aim to plan long-horizon trajectories via numerical optimization, which is inherently prone to getting stuck in local minima, particularly when encountering non-smooth obstacles, such as cubes. To improve convergence, we adapt the progressive smoothing method proposed by for autonomous driving to the three-dimensional planning domain. In progressive smoothing, potentially non-smooth obstacle shapes $\mathcal{O}(\alpha)$ from are progressively smoothed along the MPC planning horizon by scheduling the smoothing parameter $\alpha$ towards a smooth 2-norm. Particularly, a monotonically decreasing scheduling function $\lambda(t)$ with $\lambda:\mathbb{R}^{+}\rightarrow\mathbb{R}^{+}$ depending on the MPC prediction time $t$ is used, with $\lambda=\alpha_{0}$ and $\lambda(t_{f})=2$, where $t_{f}$ is the total prediction horizon and $\alpha_{0}$ describes the actual obstacle shape. The smoothing improves numerical behavior of the [RTI] scheme.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-D Progressive Smoothing", "weight": 1.0} -->

Recursive feasibility additionally requires the usual shift, terminal-set, and hard-constraint assumptions.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-E Multi-Phase MPC formulation", "weight": 1.0} -->

The multi-phase formulation optimizes the short-horizon high-fidelity states $(X,U)$ together with the long-horizon low-fidelity states $({X}^{\mathrm{lf}},{U}^{\mathrm{lf}})$ in the single NLP: The cost function accumulates stage costs from both phases and a terminal cost on the long horizon. System dynamics are enforced by the respective discrete-time integration functions $F$ and ${F}^{\mathrm{lf}}$, and the transition constraint $\pi(x_{M},{x}^{\mathrm{lf}}_{0})=0$ guarantees consistency of position, velocity, and thrust-induced acceleration.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-E Multi-Phase MPC formulation", "weight": 1.0} -->

Actuator and body-rate feasibility is maintained through the sets $\mathbb{S}_{f},\mathbb{S}_{\omega}$ for the high-fidelity model and their inner-approximated counterparts ${\mathbb{S}}^{\mathrm{lf}}_{f},{\mathbb{S}}^{\mathrm{lf}}_{\omega}$ for the low-fidelity model. Both horizons are kept collision-free by enforcing position constraints against the obstacle set $\mathbb{O}(\lambda(\cdot))$, whose recursive feasibility is guaranteed. Finally, the terminal equality ${h}^{\mathrm{lf}}({x}^{\mathrm{lf}}_{N})=0$ enforces a simple safe set at the goal. The influence of the terminal safe set would be much larger when applied directly after the high-fidelity horizon.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-F Parallel Low-Fidelity MPCs", "weight": 1.0} -->

Above, we introduced the multi-phase formulation with progressive smoothing to plan for long horizons. In cluttered environments, solving the nonlinear program is still prone to getting stuck in local minima due to the long planning horizon and the gradient-based local optimization of MPC solvers. Dealing with such nonconvexities is the pivotal point of many planning algorithms discussed in Section II. Since the planning-relevant decision variables are tied dominantly to the second (tail) phase of our formulation, we can exploit this structure. A key design goal is to keep the main controller fast: the high-fidelity first phase must not be delayed by the combinatorial complexity of planning. Therefore, we offload the search for better tail trajectories to parallel asynchronous solvers that run concurrently with the main MPC. Formulating this subproblem as a separate [NLP] allows us to optimize parallel instances from different initial guesses and escape local minima of the dominant second planning horizon while sacrificing only minor computational resources.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-F Parallel Low-Fidelity MPCs", "weight": 1.0} -->

As an initialization strategy, we roll out $M_{\mathrm{p,ini}}=64$ trajectories from ${\hat{x}}^{\mathrm{lf}}_{0}$ by simulating the low-fidelity model with an RK4 integrator and applying random jerks sampled from a uniform distribution $j\sim\mathcal{U}(\underline{j},\overline{j})$. We then select $N_{p}$ candidates, prioritizing feasible trajectories and otherwise using low-cost infeasible ones.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-F Parallel Low-Fidelity MPCs", "weight": 1.0} -->

To guarantee continuity, we start from the same initial point-mass state ${\hat{x}}^{\mathrm{lf}}_{0}$ obtained from the multi-phase MPC; the parallel MPC subproblems are Crucially for planning problems with severe nonconvexities, we add a particular parallel point-mass MPC variant that explicitly considers the nonconvexities in the free planning space by a decomposition into convex cells linked via binary indicator variables. The resulting MIQP formulation requires a dedicated solver.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-F Parallel Low-Fidelity MPCs", "weight": 1.0} -->

Due to the feasibility of the initial state, all MPC subproblems provide recursive feasibility when combined with the high-fidelity horizon of. A proof under the standard shift and terminal-set assumptions is provided in the supplementary material. Once any of the MPC subproblems initialized with random primal variables $({}^{0}{X}^{\mathrm{lf}},{}^{0}{U}^{\mathrm{lf}})^{i}$ exhibits a feasible lower cost $J_{\mathrm{lf}}\big(({}^{0}{X}^{\mathrm{lf}},{}^{0}{U}^{\mathrm{lf}})^{i},{\hat{x}}^{\mathrm{lf}}_{0}\big)$ than the second horizon of, the second horizon of is reinitialized with the optimal lower cost decision variables of $i$-th parallel MPC subproblem.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-F Parallel Low-Fidelity MPCs", "weight": 1.0} -->

Therefore, the accepted initialization has a lower evaluated tail cost before the next RTI step. Since the first horizon is unchanged during reinitialization, this reduces the evaluated objective at that instant; subsequent RTI steps and closed-loop shifts need not preserve a monotonic decrease. See for details on parallel initialization and evaluation strategies.

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-G Algorithm and Numerical Efficiency", "weight": 1.0} -->

The complete Unique algorithm is stated in Alg. 1. We use the notation $I_{k}={k,k+1,\ldots,N+M+1}$ for the prediction indexes of the MPC.

<!-- chunk {"id": "body-0064", "role": "body", "section": "V-G Algorithm and Numerical Efficiency", "weight": 1.0} -->

1: Inputs: HF state x̂0, reference ỹ(t), obstacles {𝒪i}, smoothing schedule λ(t), number of parallel MPC restarts S, number of RTI P before reinitializing 2: Set αi = λ(ti) at each prediction time ti, i ∈ I0 3: Decompose obstacles {𝒪i} to free space ℱ 4: Repeat at each control step k: 6: Set obstacle param. θi for prediction steps i ∈ Ik 7: 2. Main multi-phase MPC: 8: Solve QP of multi-phase MPC at xk = x̂k 9: Evaluate second horizon cost: (Jlf, k)0 10: Get initial l.f.

<!-- chunk {"id": "body-0065", "role": "body", "section": "V-G Algorithm and Numerical Efficiency", "weight": 1.0} -->

state x̂0lf ← x0lf 11: 3. Parallel Mixed-Integer Planner: 12: Preprocess binary variables 13: Solve MIQP of point-mass planner at (x0lf)mi:= x̂0lf 14: Evaluate second horizon cost: (Jlf, k)mi 15: 4. Parallel Point-Mass MPCs: 16: Solve j = 1: S point-mass MPCs at (x0lf)j:= x̂0lf 17: Evaluate parallel point-mass MPC costs: (Jlf, k)j 19: Get lowest cost λ⋆ = arg minλ ∈ 0, …, S, mi(Jlf, k)λ 20: Reinitialize multi-phase MPC 24: Randomly reini. parallel p.m. MPCs j = 1: S − 1 25: Reini. S-th parallel p.m.

<!-- chunk {"id": "body-0066", "role": "body", "section": "V-G Algorithm and Numerical Efficiency", "weight": 1.0} -->

MPC with MIQP solution 26: 6. Apply and shift: 27: Execute first main multi-phase control u0 28: Shift primal variables of all MPCs Algorithm 1 Unique: Unified Multi-Fidelity MPC In order to solve numerically efficiently, we use the solver acados with the interior-point QP ([QP]) solver HPIPM without condensing, and deploy the [RTI] scheme. We do not use condensing, since for the considered problem size we did not observe an improvement.

<!-- chunk {"id": "body-0067", "role": "body", "section": "V-G Algorithm and Numerical Efficiency", "weight": 1.0} -->

In particular, we use a dodecahedron with 12 surfaces instead of the six surfaces of a cube approximation as in $\widehat{\mathbb{S}}_{\mathrm{\omega}}^{\mathrm{lf}}$ and $\hat{\mathbb{S}}_{\mathrm{f}}^{\mathrm{lf}}$ to reduce the conservatism of the inner approximation by adding more constraints, as shown in Fig. 3. The approximation via a polyhedron allows the QP solver to safely handle the norm constraints, which is not possible when linearizing the constraints within a single QP subroutine of [SQP]. Notably, the velocity constraint $\mathbb{S}_{v}$ spans the whole practical operating region of the quadrotor and can therefore be removed. Remarkably, we normalize quaternions before using them to initialize the MPC problem, but do not explicitly constrain them to the unit sphere within the MPC, as we observed convergence problems and no performance benefit for converged solutions.

<!-- chunk {"id": "body-0068", "role": "body", "section": "V-G Algorithm and Numerical Efficiency", "weight": 1.0} -->

Fig. 3: Visualization of inner-norm approximation. An inscribed cube covers less volume than the dodecahedron with 12 flat faces.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

The proposed algorithm is evaluated in both real-world and simulation environments using a realistic model that accounts for aerodynamic effects, as detailed in and the supplementary material. For both real-world experiments and simulations, we utilize the high-end *Offboard* drone. The specifications are summarized in Tab. I. The drone is controlled from a ground station via the low-latency Crossfire protocol (CRSF). The overall latency of the pipeline, from state estimate to control command, is typically around 20 ms, including all processing and transmission delays with CRSF. The drone is equipped with the Betaflight lowest-level onboard controller, which tracks input body rates and total thrust. Therefore, the total thrust obtained from the rotor-thrust states is used as the reference for the lowest-level controller. The flight experiments are conducted in a large industrial hall equipped with a motion-capture system providing state estimation with millimeter accuracy at 400 Hz across a volume spanning $25\times 12\times 4\,\mathrm{m}$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Constant Velocity Environment. In this simulation environment, we evaluate the control performance, including eight randomly moving dynamic obstacles, when aiming to fly at a constant speed of 15 $\frac{\mathrm{m}}{\mathrm{s}}$ at a specific height. The environment evaluates how early adaptation towards long-horizon prediction and short-horizon adaptation due to moving obstacles affect the closed-loop performance of maintaining a reference speed. More details on the environment are given in the supplementary material.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Reference Tracking Environment. In contrast to the previous environment, where the path is of minor importance, the reference-tracking environment requires the drone to track periodic trajectories that are occluded by varying numbers of static objects, with obstacle counts ranging from 3 to 34. The trajectory resembles shapes such as a triangle, a rounded rectangle, a figure-eight, a butterfly, or a sinusoidal wave. The tracking environment cost emphasizes the position tracking of the reference and, due to its periodic flight structure, can be readily evaluated in real-world experiments. More details on the environment are given in the supplementary material.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Motion Planning Maze Environment. The motion planning environments require the consideration of major nonconvexities that cannot be handled by smoothing alone. The goal is to traverse a $6\times 6$ m tunnel at a target speed of $1~\frac{\mathrm{m}}{\mathrm{s}}$ with stage costs defined by $x_{k}^{\top}Qx_{k}$ and $u_{k}^{\top}Ru_{k}$. The tunnel has a length of $17$ m for real-world experiments and $40$ m for simulated experiments. We place up to $14$ random axis-aligned walls, see Fig. 14, thereby forming a maze-like configuration space.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Real-World Experiments", "weight": 1.0} -->

We evaluate and ablate our approach by comparing it against two benchmarks: the *hierarchical approach* and the high-fidelity *standard MPC* formulation, which uses a longer horizon without utilizing the point-mass model. The hierarchical formulation first plans a trajectory using only a point-mass model, formulating it as an MPC problem, and then employs a high-fidelity MPC tracking controller. The planner updates the trajectory every tenth lower-level tracking iteration. Remarkably, all parameters of the point-mass planning MPC, the tracking MPC, and the extended-horizon MPC are set to the corresponding phases of Unique for a fair comparison, except for the position-tracking weight, which is adapted for the hierarchical lower-level tracking MPC.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Real-World Experiments", "weight": 1.0} -->

The comparison in Sect. VII-A involves real-world experiments in the reference-tracking environment. We analyze performance on four different tracks with varying numbers of obstacles. Additionally, we evaluate progressive smoothing for cubic obstacles and parallel MPCs within the proposed initialization strategy to avoid local minima. In the first comparison, we consider a use case with many obstacles and few local minima, so random initial guesses can escape them reliably.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Real-World Experiments", "weight": 1.0} -->

In Sect. VII-B, we compare the three variants in the maze environment with randomly placed horizontal and vertical walls.

<!-- chunk {"id": "body-0076", "role": "body", "section": "VII-A Real-World Tracking Comparison", "weight": 1.0} -->

The real-world flights are performed across three representative trajectory shapes, with varying numbers of obstacles and different track periods, resulting in both agile and slower flight speeds.

<!-- chunk {"id": "body-0077", "role": "body", "section": "VII-A Real-World Tracking Comparison", "weight": 1.0} -->

The evaluations involve (i) the flat $15\times 8\,\mathrm{\mathrm{m}}$ Agile Sinusoidal track with seven obstacles, a period of $10\,\mathrm{\mathrm{s}}$ and accelerations of $20\,\mathrm{\frac{\mathrm{m}}{\mathrm{s}^{2}}}$, (ii) the flat $15\times 8\,\mathrm{\mathrm{m}}$ Agile Butterfly track with seven obstacles and accelerations of $35\,\mathrm{\frac{\mathrm{m}}{\mathrm{s}^{2}}}$, (iii) the flat $15\times 8\,\mathrm{\mathrm{m}}$ Cluttered Figure-Eight-Track-1 with $30$ obstacles and a period of $40\,\mathrm{\mathrm{s}}$ and (iv) a second similar Cluttered Figure-Eight-2 track with $34$ obstacles. The evaluations shown in Tab.

<!-- chunk {"id": "body-0078", "role": "body", "section": "VII-A Real-World Tracking Comparison", "weight": 1.0} -->

II and Fig. 4 demonstrate that Unique consistently achieves a lower tracking error while requiring comparable or even reduced online computation time. The hierarchical approach increases the tracking error by up to $274.4\%$ and standard MPC by up to $301.2\%$, corresponding to a reduction of the evaluation cost by $75\%$ using Unique. The significant increase in tracking error of the standard MPC formulation in cluttered environments stems from the abundance of local minima, which necessitate long-horizon planning. The hierarchical approach particularly struggles in the most agile Butterfly scenario, as the point-mass model can only approximate agile flight due to its conservative bounds.

<!-- chunk {"id": "body-0079", "role": "body", "section": "VII-A Real-World Tracking Comparison", "weight": 1.0} -->

Fig. 4: Comparison between Unique, the standard MPC formulation, and the hierarchical MPC formulation regarding the online computation time and the tracking error (position). The tracking error is significantly reduced by Unique, with online computation time either unchanged or slightly reduced. mean/med/max mean/med/max TABLE II: Tracking Error in Real-World Experiments.

<!-- chunk {"id": "body-0080", "role": "body", "section": "VII-A Real-World Tracking Comparison", "weight": 1.0} -->

The trajectory visualizations in Fig. 5 show that Unique tracks tighter paths with fewer deviations, especially in high-curvature segments where the hierarchical approach struggles. These results confirm that cascading models within a single optimization not only improve accuracy but also avoid the overhead of long-horizon high-fidelity MPC, leading to superior closed-loop performance in practice.

<!-- chunk {"id": "body-0081", "role": "body", "section": "VII-A Real-World Tracking Comparison", "weight": 1.0} -->

Fig. 5: Visualization and rendered images of trajectories from different controllers in real-world experiments in a flying arena. We compare the proposed Unique framework with the hierarchical and MPC settings. The top plots show agile flights with seven smooth obstacles, therefore, less susceptible to local minima. Yet, Unique still outperforms the two baselines due to the increased long-horizon prediction. Standard MPC struggles once an obstacle appears on the horizon, attempting to evade it with more costly maneuvers. The hierarchical MPC planner and controller setting is limited by the coarse path of the higher-level planner (point mass model), which is apparent in the agile flight of the Butterfly track. The lower plots illustrate the cluttered environment, which exhibits numerous local minima. The standard MPC is not even capable of following the reference coarsely, as it gets stuck in the Figure-Eight-2 track on the left. The hierarchical framework escapes some local minima due to the long-horizon planning, but still exhibits a large tracking error. Only the Unique framework is able to track the cluttered Figure-Eight tracks due to its reinitialization strategy, which utilizes parallel and long-horizon planning. The axes are labeled in SI units.

<!-- chunk {"id": "body-0082", "role": "body", "section": "VII-A Real-World Tracking Comparison", "weight": 1.0} -->

Progressive Smoothing. The influence of progressive smoothing and its significance for cubic obstacles is evaluated on the Sinusoidal track. We compare variants of Unique with fixed L2-norm, infinity norm, or progressive smoothing. The trajectories are shown in Fig. 6 and reveal a superior performance of Unique with progressive smoothing (mean/max tracking error of $0.6/1.4\,\mathrm{\mathrm{m}}$), compared to the conservative L2-norm approximation (mean/max tracking error of $0.8/2.0\,\mathrm{\mathrm{m}}$) and the numerically unstable but tight infinity norm. Remarkably, the computation time is not increased by progressive smoothing, since the norms and related parameters along the horizon are fixed. More details on progressive smoothing with different schedules and the plotted MPC predictions are shown in the supplementary material.

<!-- chunk {"id": "body-0083", "role": "body", "section": "VII-A Real-World Tracking Comparison", "weight": 1.0} -->

Fig. 6: Real-world comparison of Unique with different formulations of cubic virtual obstacles. We compare the proposed progressive smoothing against a standard L2 norm and a tight infinity norm. The L2 norm is conservative, while the infinity norm leads to numerically unstable behavior. Progressive smoothing allows for a numerically stable, tight cubic obstacle representation. The lower rendering visualizes the L2 norm and progressive smoothing variant in a particular snapshot.

<!-- chunk {"id": "body-0084", "role": "body", "section": "VII-A Real-World Tracking Comparison", "weight": 1.0} -->

Parallel Point-Mass MPC. We evaluate the influence of a parallel point-mass MPC in the Cluttered-Figure-Eight-2 track, where we activate or deactivate the parallel point-mass MPC. We perform 7 RTI steps on the parallel point-mass MPC before we randomly reinitialize. An active re-initialization and the related costs are plotted in Fig. 7. Notably, the parallel point-mass MPC computation time is evaluated assuming parallel cores, i.e., the total Unique computation time is $\max(t_{\mathrm{comp,0}},\ldots,t_{\mathrm{comp,S}})$, where $t_{\mathrm{comp,0}}$ is the computation time of the multiphase MPC and $t_{\mathrm{comp,1}},\ldots,t_{\mathrm{comp,S}}$ are the computation times of the parallel point-mass MPCs. The mean and median computation times do not increase in our experiments compared to the multi-phase MPC without parallelization.

<!-- chunk {"id": "body-0085", "role": "body", "section": "VII-A Real-World Tracking Comparison", "weight": 1.0} -->

However, the maximum computation time is increased from $10.9\,\mathrm{\mathrm{ms}}$ to $21.9\,\mathrm{\mathrm{ms}}$, which is still below the benchmark approaches compared, cf. Fig. 5 and Tab. II. Considering the tracking error, the difference when using parallel point-mass MPCs is remarkable in this obstacle-rich environment, as the mean tracking error decreases by $77.1\%$ from $3.5/2.0/8.3$ (mean/median/max, in meters) when using Unique without parallel roll-outs to $0.8/0.8/1.7$ when using the parallel roll-outs. This is due to the multi-phase MPC getting trapped in the local minima, similarly to the MPC in Fig. 5. In the Agile Sinusoidal or Agile Butterfly tracks, the influence of the parallel point-mass MPCs was evaluated to be negligible due to the absence of dominant local minima.

<!-- chunk {"id": "body-0086", "role": "body", "section": "VII-A Real-World Tracking Comparison", "weight": 1.0} -->

Fig. 7: Comparison of the parallel point-mass MPC initialization approach. One parallel point-mass MPC is structurally identical to the second phase of the main multi-phase MPC and is randomly initialized every seventh step. Once the parallel MPC cost is lowest, the second phase of the main MPC is initialized with the corresponding lower-cost decision variables (at 0.6 s). Due to the random initialization and RTI, the parallel MPC cost decreases significantly over the seven iterations, which are clearly visible as “stairs”.

<!-- chunk {"id": "body-0087", "role": "body", "section": "VII-B Real-World Planning Comparison", "weight": 1.0} -->

We evaluate the three navigation algorithms (std., hier., Unique) in a maze environment built from virtual obstacles in a flying arena equipped with a Vicon motion-capture system. As before, the hierarchical framework uses the same hyperparameters as the second horizon of Unique to provide a reference for a tracking MPC, whose hyperparameters match the first horizon of Unique except for a stronger position-tracking cost. We start at the position $p_{0}=$ m and aim to traverse the tunnel in the positive $x$ direction until $x_{T}\geq 12$ m. Various obstacles block the tunnel, requiring planners with an 8-second horizon to find low-cost detours, as shown in Fig. 8. The standard MPC formulation is excluded from the comparison because it does not finish. Figure 8 shows rapid cost increases for the hierarchical planner when a parallel point-mass planner finds a lower-cost trajectory that deviates from the previous plan and the tracking controller attempts to follow it. This replanning is much smoother when it is integrated into the second horizon of Unique.

<!-- chunk {"id": "body-0088", "role": "body", "section": "VII-B Real-World Planning Comparison", "weight": 1.0} -->

Scene 2 reveals a failure case for Unique: the parallel planners found a lower-cost trajectory around the blocking obstacle, but the slack variables were violated, preventing switching. As shown in Fig. 9, this increased the accumulated cost over the baseline. In the other scenarios, however, the sequential planning framework reduced the cost.

<!-- chunk {"id": "body-0089", "role": "body", "section": "VII-B Real-World Planning Comparison", "weight": 1.0} -->

Fig. 8: Real-world evaluation showing trajectories and cumulative closed-loop costs on four randomly generated scenes for the hierarchical controller and Unique.

<!-- chunk {"id": "body-0090", "role": "body", "section": "VII-B Real-World Planning Comparison", "weight": 1.0} -->

Fig. 9: Real-world evaluation on four randomly generated scenes. Unique achieves a 70.8%, 40.9%, and 28.7% lower accumulated closed-loop cost than the hierarchical approach in three scenarios, and a 10.9% higher cost in one scenario, corresponding to a 34.2% reduction after aggregating the costs across all four scenarios.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Simulated Experiments", "weight": 1.0} -->

In the following simulation experiments, we ablate different hyperparameters in the constant-velocity and maze environments to assess the robustness and scaling properties of Unique. First, we focus on control-oriented evaluations, emphasizing the closed-loop performance gains, feasibility, and computation time achieved via the multi-phase formulation. In Sect. VIII-B, we evaluate the different constraint approximations of the second horizon and provide some qualitative insights into progressive smoothing and the parallel initialization strategy. Secondly, we focus on the performance gain achieved via the parallel planning framework using the point-mass and MIQP planners. Specifically, in Sect. VIII-C, we evaluate how the computational burden scales with the number of obstacles in the mixed-integer planner, how different combinations of parallel solvers influence performance, and how Unique compares against the hierarchical formulation when both use equal planners.

<!-- chunk {"id": "body-0092", "role": "body", "section": "VIII-A Control-Focused Evaluation of Hyperparameters", "weight": 1.0} -->

The proposed Unique formulation comprises numerous hyperparameters, which we compare in simulated experiments within a constant velocity environment by evaluating their closed-loop cost. The most critical hyperparameters are the particular horizon lengths, number of shooting nodes of the short and long horizon, and the choice of the low-fidelity force constraint approximation $\mathbb{S}^{\mathrm{lf}}_{f}$ or $\hat{\mathbb{S}}^{\mathrm{lf}}_{f}$ and the low-fidelity body rate constraint approximation $\mathbb{S}^{\mathrm{lf}}_{\omega},\hat{\mathbb{S}}^{\mathrm{lf}}_{\omega}$ or $\widehat{\mathbb{S}}^{\mathrm{lf}}_{\omega}$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "VIII-A Control-Focused Evaluation of Hyperparameters", "weight": 1.0} -->

Additionally, the discretization time can be spaced by a factor $c_{\mathrm{space}}$ for future horizons, for example by $t_{\Delta,i+1}=c_{\mathrm{space}}t_{\Delta,i}$. The following section aims to answer crucial hyperparameter evaluation questions.

<!-- chunk {"id": "body-0094", "role": "body", "section": "VIII-A Control-Focused Evaluation of Hyperparameters", "weight": 1.0} -->

How do hyperparameters affect the closed-loop performance gains? Fig. 10 shows a comparison of the Pareto front of closed-loop performance and online computation time for the [RTI] scheme and the fully converged solvers, with parameters shown in Tab. III. The comparison includes a standard MPC with increasing spacing of the high-fidelity horizon, which constitutes an alternative method for planning more coarsely in the distant future. However, due to the nonlinearity of the high-fidelity model, the spacing leads to convergence problems. The three different horizons of the standard MPC hint a barrier in the Pareto plot in Fig. 10 and also, the hierarchical approach clusters in a specific region. Both benchmarks are clearly outperformed by Unique.

<!-- chunk {"id": "body-0095", "role": "body", "section": "VIII-A Control-Focused Evaluation of Hyperparameters", "weight": 1.0} -->

Fig. 10: Pareto comparison of closed-loop cost and average per-iteration computation time in the constant-velocity environment. We compare different hyperparameter settings for the hierarchical, the standard MPC, and the unified formulation. The top plot shows a comparison for the real-time iteration scheme, while the bottom plot shows a comparison for the fully converged solver, which is nearly an order of magnitude slower. The numerically challenging long-horizon standard MPC formulations require comparably much higher computation times to fully converge than Unique, which is also Pareto optimal in both plots.

<!-- chunk {"id": "body-0096", "role": "body", "section": "VIII-A Control-Focused Evaluation of Hyperparameters", "weight": 1.0} -->

How do hyperparameters affect convergence? Although the RTI scheme is the only applicable approach in real-world evaluations, the fully converged evaluation shown in Fig. 10 and Tab. III contrasts the different approaches in terms of their numerical complexity. Across the reported configurations, full convergence increases computation time by factors of approximately 6--7 for Unique and 29--137 for standard MPC relative to RTI. Thus, Unique requires substantially less additional time for full convergence than the long-horizon standard MPC configurations.

<!-- chunk {"id": "body-0097", "role": "body", "section": "VIII-A Control-Focused Evaluation of Hyperparameters", "weight": 1.0} -->

How does the second phase influence control performance? In Fig. 11, we investigate how adding steps of the second phase influences the Pareto performance in comparison to how adding standard MPC steps influences the performance. We take standard MPC with $n_{\mathrm{hf}}=\{10,15,20,30,50\}$ shooting nodes and $t_{\Delta}^{\mathrm{hf}}=40\,\mathrm{\mathrm{ms}}$ (red line in Fig. 11) and append to each standard high-fidelity MPC the low-fidelity part of $n_{\mathrm{lf}}=\{3,5,7\}$ with $t_{\Delta}^{\mathrm{lf}}=400\,\mathrm{\mathrm{ms}}$ (black dotted line). The reference tracking involves three obstacles and shapes of a Triangle, a rounded Rectangle, a Figure Eight, and a Butterfly. Additionally, we add a small sinusoidal z-component.

<!-- chunk {"id": "body-0098", "role": "body", "section": "VIII-A Control-Focused Evaluation of Hyperparameters", "weight": 1.0} -->

The evaluation on the Pareto front reveals that it is more efficient to add the low-fidelity horizon of Unique than to increase the MPC horizon. This confirms that, even from a pure control perspective, the two-phase structure yields superior closed-loop performance under the same computational budget.

<!-- chunk {"id": "body-0099", "role": "body", "section": "VIII-A Control-Focused Evaluation of Hyperparameters", "weight": 1.0} -->

Fig. 11: Pareto comparison between increasing the horizon of the standard MPC formulation (red line), as opposed to increasing the horizon with the planner formulation (green markers and dashed gray line) on different test tracks. Remarkably, adding the second low-fidelity horizon outperforms MPC with increased horizons.

<!-- chunk {"id": "body-0100", "role": "body", "section": "VIII-B Evaluation of Constraint Approximation", "weight": 1.0} -->

In this Section, we evaluate the influence of the different constraint formulations on the low-fidelity model phase.

<!-- chunk {"id": "body-0101", "role": "body", "section": "VIII-B Evaluation of Constraint Approximation", "weight": 1.0} -->

Particularly, we assess the rise time, i.e., the time it takes to reach $90\%$ of the set velocity of $14\,\mathrm{\frac{\mathrm{m}}{\mathrm{s}}}$ from hovering using the different low-fidelity force constraint approximation $\mathbb{S}^{\mathrm{lf}}_{f}$ (polyhedral) or $\hat{\mathbb{S}}^{\mathrm{lf}}_{f}$ (box) and the low-fidelity body rate constraint approximation $\mathbb{S}^{\mathrm{lf}}_{\omega}$ (nonlinear), $\hat{\mathbb{S}}^{\mathrm{lf}}_{\omega}$ (polyhedral) or $\widehat{\mathbb{S}}^{\mathrm{lf}}_{\omega}$ (box)^11^ 1 We use a color coding for body rate constraint types to simplify the reading..

<!-- chunk {"id": "body-0102", "role": "body", "section": "VIII-B Evaluation of Constraint Approximation", "weight": 1.0} -->

Fig. 12 shows the corresponding velocity state $v_{y}$, the related body rate $\omega_{x}$, and the evaluation of the three different constraint functions that approximate the body rates. In addition, all MPC predictions of both phases are plotted, as well as one particular prediction at step $k=5$ equal to $0.2\,\mathrm{\mathrm{s}}$. As anticipated, the more conservative constraints lead to an increased rise time. Conservatism can be verified in the lower three rows, which show their constraint function evaluations. Yet, despite the visible larger conservatism in the second horizon, the re-optimization along the first high-fidelity horizon can improve the closed-loop performance.

<!-- chunk {"id": "body-0103", "role": "body", "section": "VIII-B Evaluation of Constraint Approximation", "weight": 1.0} -->

Fig. 12: Visualization of different safe set approximations for body rates (three columns: box constraints $\widehat{\mathbb{S}}_{\omega}^{\mathrm{lf}}$, polyhedral $\hat{\mathbb{S}}_{\omega}^{\mathrm{lf}}$, nonlinear 𝕊ωlf) for a step response to a horizontal set speed ($14\frac{\mathrm{m}}{\mathrm{s}}$, first row). The second row shows the body rates and the respective constraints for the high-fidelity model. The lower three rows show the different constraint function evaluations on the lower-fidelity part, with the lower white region being feasible. The third row shows the most accurate nonlinear constraints. It reveals that these are satisfied for all formulations, however, more conservatively, for the box constraints and the polyhedral constraints. The lower off-diagonal plots show the respective active constraint evaluation.

<!-- chunk {"id": "body-0104", "role": "body", "section": "VIII-B Evaluation of Constraint Approximation", "weight": 1.0} -->

Trivially, if the first horizon is increased, the second horizon and the related constraints become less relevant. We evaluated this dependency in Fig. 13, where we increased the first high-fidelity horizon and evaluated the rise time and computation time for RTIs and the fully converged solution. If the first horizon is increased beyond 20 shooting nodes ($0.8\,\mathrm{s}$), the constraint formulation on the second horizon becomes irrelevant for the particular maneuver. Both the converged and the RTI evaluations show an increasing difference in the constraint formulation for shorter horizons of the first phase. Using box constraints on body rates with $\widehat{\mathbb{S}}^{\mathrm{lf}}_{\omega}$ and thrust $\hat{\mathbb{S}}^{\mathrm{lf}}_{f}$ shows the lowest computation time, particularly for RTI. The constraint formulation for the thrust shows no difference in the evaluation.

<!-- chunk {"id": "body-0105", "role": "body", "section": "VIII-B Evaluation of Constraint Approximation", "weight": 1.0} -->

Fig. 13: Comparison of the rise time (90% of the set value) and computation time for a horizontal velocity step regarding different high-fidelity horizons using a large low-fidelity horizon. The horizontal axis reports the number of high-fidelity shooting nodes. The experiments reveal the diminishing influence of the different safe set formulations on the closed-loop performance when the first high-fidelity model horizon is increased. More accurate safe set formulations require longer computation times but improve performance, particularly for the shorter high-fidelity model phase.

<!-- chunk {"id": "body-0106", "role": "body", "section": "VIII-C Planning evaluations in the maze environment", "weight": 1.0} -->

In the following, we evaluate the planning capabilities of Unique in the simulated randomized maze environment. We examine how the computation time of the potentially slow MIQP planner scales with the number of obstacles, how the parallel synchronization can be satisfied, and how the typical hierarchical decomposition compares in different configurations against Unique.

<!-- chunk {"id": "body-0107", "role": "body", "section": "VIII-C Planning evaluations in the maze environment", "weight": 1.0} -->

How do planning hyperparameters affect the closed-loop performance? The main planning hyperparameters are the use of the MIQP solver as an initializer and the number of parallel, randomly initialized point-mass solvers. We vary the hyperparameters in the maze environment and compare the closed-loop cost, which is mainly the progress in the maze-tunnel, with a constant velocity. Fig. 14 shows a top view of two maze environments (denser on the left and sparser on the right) for different configurations. The plots qualitatively show the benefit of the MIQP solver, which finds gaps more reliably than randomly initialized point-mass solvers. In the simpler, sparser environment, the parallel point-mass solvers can find an equally good solution. Figure 15 shows a quantitative comparison across 40 randomized mazes and different configurations. Remarkably, with 10 parallel randomly initialized solvers, a solution of similar quality to that of the MIQP solver was found.

<!-- chunk {"id": "body-0108", "role": "body", "section": "VIII-C Planning evaluations in the maze environment", "weight": 1.0} -->

Fig. 14: Top view of simulation comparisons of Unique with different hyperparameters. The left column shows a denser maze and the right column a sparser maze. The first row shows that Unique without parallel planning gets easily stuck in local minima. The second row shows successful planning in the simpler right-hand scenario with parallel randomly initialized point-mass planners. The plots show how the free space is explored by alternating RTI and reinitialization with initial guesses. The third row shows successful planning with the MIQP parallel planner, and the last row shows successful planning for all scenarios with additional point-mass planners.

<!-- chunk {"id": "body-0109", "role": "body", "section": "VIII-C Planning evaluations in the maze environment", "weight": 1.0} -->

Fig. 15: Closed-loop cost comparison on randomized instances of the maze environment. Including the mixed-integer planner yields the lowest closed-loop cost, provided sufficient computational resources. The hierarchical planner/controller architecture has a significantly larger closed-loop cost, despite also being able to navigate the mazes toward the goal.

<!-- chunk {"id": "body-0110", "role": "body", "section": "VIII-C Planning evaluations in the maze environment", "weight": 1.0} -->

How does Unique compare against the hierarchical configuration with the same hyperparameters? In Fig. 15, we evaluate, for some configurations, the hierarchical setting, i.e., a planner with equal parameters and parallel evaluations together with a tracking MPC controller. The figure shows that, in terms of closed-loop cost, Unique clearly outperforms the hierarchical baseline. Remarkably, if only progress is considered, the hierarchical configuration also achieves comparable performance, yet in a suboptimal way.

<!-- chunk {"id": "body-0111", "role": "body", "section": "VIII-C Planning evaluations in the maze environment", "weight": 1.0} -->

Can real-time control be achieved? In Fig. 16 the computation times of the parallel point-mass solvers, the main multi-phase MPC, and the MIQP are compared statistically. The time-critical solvers finish in time, while the MIQP has to run asynchronously because it exceeds the time budget.

<!-- chunk {"id": "body-0112", "role": "body", "section": "VIII-C Planning evaluations in the maze environment", "weight": 1.0} -->

Fig. 16: Timing comparison of the different solvers in the maze environment. Remarkably, the parallel, randomly initialized point-mass solvers can be solved much faster than the main multi-phase MPC and can therefore be synchronized after each iteration. However, the MIQP solver must be executed asynchronously due to its longer computation time.

<!-- chunk {"id": "body-0113", "role": "body", "section": "VIII-C Planning evaluations in the maze environment", "weight": 1.0} -->

Can the parallel evaluations finish on time? Since our algorithm assumes the parallel point-mass solver completes after each iteration of the main multi-phase MPC, we evaluate the share of iterations in which the parallel solver finishes before the main multi-phase MPC in the maze environment over 200 iterations. We report a success rate of 99.5%. Moreover, we evaluate the same metric for a reinitialized full multi-phase MPC with randomized initial guesses and find that only 12% of the runs finish in time, highlighting the advantage of the considerably cheaper point-mass evaluations.

<!-- chunk {"id": "body-0114", "role": "body", "section": "VIII-C Planning evaluations in the maze environment", "weight": 1.0} -->

How does MIQP computation time scale with the number of obstacles? Most critically, the MIQP planner uses binary indicator constraints for obstacle-free convex cells, the number of which grows with the number of obstacles. In principle, this scales an NP-hard problem and could lead to a large increase in computation time. However, we show that, even with many obstacles, our pruning, preprocessing, and Gurobi's internal optimization strategies keep computation times below one second, even for 50 obstacles, as detailed in the supplementary material.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

The proposed Unique framework introduces a temporal cascading paradigm that formulates the planning problem along the tail horizon of an MPC, replacing the conventional hierarchical planner-controller decomposition with a sequential controller-planner structure within a single optimization. A long-horizon, low-fidelity point-mass model provides prospective planning, while a short-horizon, high-fidelity model ensures precise control, achieving real-time performance without hierarchical decomposition. This is enabled by the observation that the planning subproblem, primarily geometric obstacle avoidance, is a long-horizon concern that can be solved very efficiently with a point-mass model at each closed-loop iteration. By coupling both models through feasibility-preserving transition constraints, Unique maintains recursive feasibility across phases. This integration avoids the redundancy and limitations of the point-mass model typical of planner-tracker pipelines and mitigates the limited long-horizon planning of single-model MPCs.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

The key mechanisms of *progressive obstacle smoothing* and *parallel low-fidelity MPCs* enhance convergence in cluttered environments, preventing convergence to highly suboptimal local minima while preserving computational speed. Experiments show a reduction of up to 75% in closed-loop cost compared to hierarchical and standard MPC baselines. Both mechanisms still cannot guarantee finding the global optimal solution, as is common in NMPC. However, the experiments reveal the practical low-cost closed-loop performance. Notably, evaluating the multiple shooting cost of an RTI trajectory is nontrivial due to infeasible gaps in the dynamics. We simply use the cost of the potentially infeasible trajectory as it resembles the closed-loop cost sufficiently in our experiments. More advanced cost evaluation strategies are presented.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

Another limitation is that tuning the cost of the point-mass model remains task-dependent. Because the transformation between point-mass and quadrotor states is not bijective, generic, task-independent tuning of the costs is impossible. Extending the framework to automatically tune costs for specific tasks is considered for future work.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

Notably, motion planning for even simple models is NP-hard, which was also shown for [MIQP] in general and can even be undecidable for nonconvex MINLP. However, motion planning with linear models, formulated as [MIQP] or similar programs, performs sufficiently well in practice, as shown by various algorithms, highlighting the focus on planning particularly along the second horizon of the proposed algorithm. For motion-planning problems of increasing complexity, such as larger mazes, the proposed approach cannot be applied without modifications. The main limiting factors are that the MPC horizon cannot be made arbitrarily long under a fixed computational budget and that numerical stability decreases as the horizon grows. Moreover, highly nonconvex planning costs such as time-optimal flight remain challenging to include in a numerically stable nonlinear program, although recent advances also aim to include more nonconvex costs. A possible direction for future extensions would be to condense the long-horizon plan into a value function, potentially combined with the two stages.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

The temporal cascading paradigm builds on two observations that hold well for quadrotors but may not transfer directly to all robotic systems: (i) that geometric planning around obstacles is predominantly a long-horizon concern with negligible influence on the short control horizon, and (ii) that meaningful state mappings from the high-fidelity to the low-fidelity model exist. For platforms where these conditions are less clear, e.g., legged robots with hybrid contact dynamics or manipulators with joint-space obstacles, the paradigm may still apply in principle, but the design of the transition function and the feasibility-preserving constraints require platform-specific analysis. Moreover, the effectiveness of temporal cascading relies on the low-fidelity planning model converging quickly once it reaches a good local minimum during closed-loop iteration. This property, which we empirically confirm for point-mass models solved via RTI, makes the second horizon computationally cheaper than the first. If the local planning model were too expensive to solve, as would be the case for a high-fidelity model on the tail horizon, the computational advantage over simply extending the MPC horizon would vanish.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

Importantly, when any parallel solver, including the MIQP, cannot finish within the main cycle, the algorithm degrades non-critically: the main multi-phase MPC retains its own feasible tail trajectory, and only completed, lower-cost solutions trigger reinitialization. This ensures that the real-time control loop is never blocked by the combinatorial planning search. A central design principle is to keep the high-fidelity controller fast and delegate the computationally harder planning search to parallel asynchronous tasks. By the principle of optimality, any improvement found on the tail trajectory reduces the overall cost without affecting the first-phase controller iteration time. The Pareto analyses confirm that this decomposition is beneficial not only for planning but also for control: under the same computational budget, the two-phase structure consistently outperforms a longer, high-fidelity MPC horizon.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

Unique is a real-time MPC that treats planning as a tail-horizon problem rather than a hierarchical stage, including long-horizon planning as an extension to short-horizon control in a single computationally efficient [NLP] through temporal cascading of planning and control.
