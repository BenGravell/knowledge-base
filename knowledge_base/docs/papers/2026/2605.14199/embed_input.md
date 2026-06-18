<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Motion Planning for Autonomous Vehicles Using Optimization over Graphs of Convex Sets

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Motion planning for autonomous vehicles requires generating collision-free and dynamically feasible trajectories in complex environments under real-time constraints. While nonlinear optimal control formulations provide high-fidelity solutions, they are computationally demanding and sensitive to initialization, whereas geometric planning methods scale well but often decouple path selection from trajectory optimization. This paper studies the extent to which optimization over Graphs of Convex Sets (GCS) can approximate solutions of nonlinear optimal control problems in the context of autonomous driving. The free space is represented as a finite union of convex regions organized as a directed graph, allowing nonconvex geometry to be handled through discrete connectivity decisions while maintaining convex trajectory constraints within each region. Vehicle motion is parameterized using Bezier curves for the spatial path and a polynomial time-scaling function for temporal evolution. Under small-slip and linear tire assumptions, a simplified dynamic bicycle model enables approximate enforcement of dynamic feasibility through convex constraints on trajectory derivatives. The approach is evaluated in CommonRoad scenarios involving static obstacle avoidance and lane-changing maneuvers, and is compared against a nonlinear discrete-time optimal control formulation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The results indicate that the GCS-based method generates collision-free and dynamically consistent trajectories that closely match those obtained from the nonlinear program, while exhibiting improved computational efficiency and reduced sensitivity to initialization. These findings suggest that GCS provides a structured approximation of nonlinear motion planning problems, capturing dominant geometric and dynamic effects while preserving convexity in the continuous relaxation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Autonomous driving requires motion planning algorithms capable of generating collision-free and dynamically feasible trajectories in geometrically complex, uncertain, and time-varying environments. Although substantial advances have been achieved in perception, control, and learning-based components of autonomous systems, ensuring safe and reliable decision-making under strict real-time constraints remains challenging. Motion planning plays a central role in this architecture, as it must reconcile vehicle dynamics, obstacle avoidance, traffic rules, and computational tractability within a unified framework.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The motion planning problem consists of determining a trajectory that connects a start and a goal configuration while satisfying kinematic and dynamic constraints and avoiding collisions. Obstacle avoidance induces a nonconvex admissible configuration set, while vehicle dynamics introduce nonlinear constraints, increasing problem difficulty.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing approaches can be broadly categorized as search-based, sampling-based, optimization-based, and learning-based methods. Search-based planners discretize the configuration space and rely on motion primitives, often limiting optimality and smoothness. Sampling-based planners such as Rapidly Exploring Random Trees (RRT) and its variants provide probabilistic completeness and scale well to high-dimensional spaces, but typically require post-processing to ensure dynamic feasibility. Learning-based methods leverage data-driven models to generate trajectories, but generally lack formal safety guarantees and remain sensitive to distributional shift.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimization-based methods encode vehicle models, safety constraints, and performance objectives within a unified mathematical formulation. These include optimal control formulations, which lead to nonconvex Nonlinear Program (NLP) s solved via direct transcription and numerical optimization, and parametric trajectory representations based on curves such as Bézier curves or clothoids, which enable dimensionality reduction and direct enforcement of smoothness. However, obstacle avoidance remains nonconvex, and many approaches rely on local methods such as iterative linearization or sequential convex programming. While computationally efficient, these methods do not capture the combinatorial structure associated with alternative homotopy classes and are often sensitive to initialization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

An alternative perspective is provided by optimization over Graphs of Convex Sets (GCS), where the free space is decomposed into convex regions organized as a graph. Motion planning is then formulated as a mixed-integer convex optimization problem in which binary variables select a sequence of regions while continuous variables describe trajectories within them. This formulation represents geometric nonconvexity through graph connectivity while preserving convexity of trajectory constraints within each region. In contrast to methods based on precomputed safe corridors, GCS integrates region selection and trajectory optimization within a single optimization problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nevertheless, GCS was originally developed for general motion planning and does not directly account for structural aspects specific to autonomous driving. Vehicle models introduce kinematic and dynamic constraints, and dynamic obstacles induce time-dependent modifications of feasible regions. Incorporating these elements requires careful modeling to preserve convexity while maintaining computational tractability.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A central question addressed in this work is the extent to which a GCS-based formulation can reproduce solutions of the corresponding nonlinear optimal control problem. In this context, approximation is understood in terms of trajectory geometry, dynamic profiles, and feasibility with respect to vehicle constraints, rather than strict optimality guarantees. This perspective positions the proposed approach as a structured relaxation rather than a direct substitute for nonlinear optimal control.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, the GCS framework is specialized to autonomous driving by incorporating approximate vehicle dynamics and introducing a structured mechanism to account for dynamic obstacles within the graph-based formulation. The goal is to assess its ability to approximate trajectories obtained from nonlinear optimal control formulations. While the results are encouraging, the approach should be regarded as an initial investigation whose theoretical and practical properties require further analysis.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

A formulation of motion planning using optimization over GCS that incorporates approximate vehicle dynamics through differential flatness, enabling convex constraints on dynamically relevant quantities.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

An analysis of the extent to which GCS-based trajectories approximate those obtained from a nonlinear optimal control formulation, across multiple driving scenarios.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

A structured, though heuristic, mechanism for incorporating time-dependent obstacle avoidance within the GCS framework, highlighting both its applicability and limitations.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Vehicle Dynamics", "weight": 1.0} -->

Different vehicle models are adopted in the literature depending on the required fidelity. Here, a simplified dynamic bicycle model consistent with is used. The steering angle is assumed to be small, lateral tire forces are linear in the slip angles, and longitudinal slip is neglected. These assumptions are reasonable for highway and mild urban driving, where curvature and longitudinal transients remain moderate.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Vehicle Dynamics", "weight": 1.0} -->

With small-slip approximations, the slip angles become

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Vehicle Dynamics", "weight": 1.0} -->

Under the stated assumptions, the system can be approximated as differentially flat with respect to the position coordinates $(p_{x},p_{y})$ in the sense that the remaining states and inputs can be expressed as functions of these outputs and a finite number of their derivatives, up to modeling approximations. This justifies planning directly in the geometric space while maintaining dynamic consistency.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Vehicle Dynamics", "weight": 1.0} -->

Substituting into the lateral dynamics and linear tire model yields the approximate side-slip dynamics

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A Vehicle Dynamics", "weight": 1.0} -->

For typical passenger vehicle parameters, the lateral dynamics, governed by the cornering stiffness coefficients $C_{f}$ and $C_{r}$, induce a characteristic time constant on the order of $m/{({C_{f} + C_{r}})}$, which is typically in the range of tens of milliseconds. This is significantly smaller than the time scales associated with longitudinal motion and path evolution in motion planning problems (on the order of seconds).

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A Vehicle Dynamics", "weight": 1.0} -->

Differentiating $\theta = {\psi + \beta}$ gives $\overset{˙}{\theta} = {\omega + \overset{˙}{\beta}}$. Under the time-scale separation assumption, $\overset{˙}{\beta}$ is small relative to $\omega$, yielding the approximation $\omega \approx \overset{˙}{\theta}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A Vehicle Dynamics", "weight": 1.0} -->

Thus $\beta$ and $\omega$ can be expressed approximately in terms of $v$, $k$, and $\delta$, all of which depend on derivatives of $(p_{x},p_{y})$. The remaining states follow from

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A Vehicle Dynamics", "weight": 1.0} -->

and the longitudinal input from

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A Vehicle Dynamics", "weight": 1.0} -->

Under the small-slip and linear-tire assumptions, the relations above establish an *approximate* differential flatness property of the dynamic bicycle model with flat outputs $(p_{x},p_{y})$. In particular, the quasi--steady-state approximation ${{v\overset{˙}{\beta}} + {\overset{˙}{v}\beta}} \approx 0$ assumes that the side-slip dynamics evolve on a faster time scale than the longitudinal and yaw dynamics, allowing $\beta$, $\omega$, and the corresponding inputs to be recovered algebraically from derivatives of the position trajectory.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-A Vehicle Dynamics", "weight": 1.0} -->

This approximation is not exact and is introduced to obtain a tractable relation between the flat outputs and the remaining states and inputs. While it enables reconstruction of dynamically consistent trajectories, it introduces modeling error in quantities such as $\beta$ and $\delta$. These deviations affect reconstruction fidelity but not the geometric feasibility of the trajectory, which remains defined by $({p_{x}{(t)}},{p_{y}{(t)}})$ and its derivatives.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B Bézier Curves", "weight": 1.0} -->

Bézier curves are widely used in motion planning algorithms that rely on parametric trajectory representations due to their favorable geometric and analytical properties. In particular, Bézier curves provide a compact polynomial parameterization of trajectories in terms of a finite set of control points, which makes them especially suitable for optimization-based formulations.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-C Optimization over Graphs of Convex Sets", "weight": 1.0} -->

Using the trajectory representation introduced previously, the motion planning problem can be formulated directly in terms of the time-parameterized position trajectory ${{\mathbf{q}}{(t)}} = {{\mathbf{r}}{({g{(t)}})}}$. Under the previously stated assumptions regarding the operating conditions of the vehicle, planning is carried out in the output space without explicitly introducing control inputs. The problem can therefore be written as

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-C Optimization over Graphs of Convex Sets", "weight": 1.0} -->

where ${y{(t)}} = {{\mathbf{q}}{(t)}}$ and $Y_{diff}$ encodes algebraic constraints on trajectory derivatives. While inputs are eliminated, the geometric constraint ${y{(t)}} \in Y_{a}$ remains nonconvex.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-C Optimization over Graphs of Convex Sets", "weight": 1.0} -->

Following, the free region is approximated as a finite union of convex polytopes,

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-C Optimization over Graphs of Convex Sets", "weight": 1.0} -->

and represented by a directed graph $\mathcal{G} = {(\mathcal{V},\mathcal{E})}$, where each vertex corresponds to a region $\mathcal{C}_{v}$ and each edge encodes an admissible transition. If the trajectory within region $\mathcal{C}_{v}$ is represented by a Bézier curve with control points $P_{k,v}$, enforcing $P_{k,v} \in \mathcal{C}_{v}$ guarantees containment of the entire segment.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-C Optimization over Graphs of Convex Sets", "weight": 1.0} -->

To capture connectivity, binary variables $y_{ij} \in {\{ 0,1\}}$ are introduced, indicating whether the edge ${(i,j)} \in \mathcal{E}$ is selected to compose the path.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-C Optimization over Graphs of Convex Sets", "weight": 1.0} -->

with appropriate boundary conditions at source and target vertices.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-C Optimization over Graphs of Convex Sets", "weight": 1.0} -->

In this formulation, constraints of the form

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-C Optimization over Graphs of Convex Sets", "weight": 1.0} -->

are enforced only when $y_{ij} = 1$. The constraints above introduce bilinear terms involving products of binary and continuous variables. To recover a convex formulation, a standard lifting technique is employed, introducing auxiliary variables that represent these products and allow the constraints to be expressed linearly in the lifted space. Define

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-C Optimization over Graphs of Convex Sets", "weight": 1.0} -->

which eliminates explicit products and yields

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-C Optimization over Graphs of Convex Sets", "weight": 1.0} -->

When $y_{ij} = 0$, the lifted variables vanish; when $y_{ij} = 1$, the original trajectory variables are recovered.

<!-- chunk {"id": "body-0036", "role": "body", "section": "II-C Optimization over Graphs of Convex Sets", "weight": 1.0} -->

Let ${s,t} \in \mathcal{V}$ denote the source and target vertices. The lifted formulation becomes the mixed-integer convex program

<!-- chunk {"id": "body-0037", "role": "body", "section": "II-C Optimization over Graphs of Convex Sets", "weight": 1.0} -->

where $D$ is a differentiation operator for the Bézier curve.

<!-- chunk {"id": "body-0038", "role": "body", "section": "II-C Optimization over Graphs of Convex Sets", "weight": 1.0} -->

Relaxing the binary constraints to $y_{ij} \in {\lbrack 0,1\rbrack}$ yields a convex program that provides a lower bound on the original problem. The resulting solution can be interpreted as a fractional flow over the graph, which does not correspond to a single feasible path but can be used to guide the selection of a discrete solution through rounding procedures. It should be noted that the rounding step is not guaranteed to preserve optimality or feasibility with respect to the relaxed solution, and its effectiveness depends on the structure of the graph and the tightness of the relaxation.

<!-- chunk {"id": "body-0039", "role": "body", "section": "II-D Nonlinear Discrete-Time Optimal Control", "weight": 1.0} -->

To provide a baseline for comparison, the motion planning problem is also formulated and solved as a nonlinear discrete-time optimal control problem. In contrast to the proposed GCS formulation, the NLP retains the full nonlinear vehicle dynamics and enforces obstacle avoidance and dynamic constraints directly in the original state space.

<!-- chunk {"id": "body-0040", "role": "body", "section": "II-D Nonlinear Discrete-Time Optimal Control", "weight": 1.0} -->

Let the state vector $\mathbf{x}$ and the control input $\mathbf{u}$ be defined as

<!-- chunk {"id": "body-0041", "role": "body", "section": "II-D Nonlinear Discrete-Time Optimal Control", "weight": 1.0} -->

For numerical optimization, the system is discretized over a finite horizon of length $T$ using a fixed sampling time $\Deltat$, with $N = {{T/\Delta}t}$ steps. A forward Euler discretization is adopted for simplicity. While higher-order integration schemes could improve accuracy, the chosen discretization is sufficient for the comparative purposes of this study.

<!-- chunk {"id": "body-0042", "role": "body", "section": "II-D Nonlinear Discrete-Time Optimal Control", "weight": 1.0} -->

The stage cost penalizes control effort and aggressive maneuvers and is chosen as

<!-- chunk {"id": "body-0043", "role": "body", "section": "II-D Nonlinear Discrete-Time Optimal Control", "weight": 1.0} -->

where $w_{a}$, $w_{\delta}$, and $w_{\overset{˙}{\delta}}$ are positive weights. This structure penalizes large longitudinal accelerations, large steering angles, and rapid steering variations, promoting smoothness and passenger comfort. A terminal cost $\ell_{f}{({\mathbf{x}}_{N})}$ penalizes deviation from the goal configuration. It should be noted that the objective functions in the GCS and NLP formulations are not identical. While the NLP directly penalizes control inputs and their variations, the GCS formulation penalizes higher-order derivatives of the trajectory as convex surrogates for these quantities. Therefore, the comparison focuses on the resulting trajectory properties rather than exact optimality with respect to a common cost function.

<!-- chunk {"id": "body-0044", "role": "body", "section": "II-D Nonlinear Discrete-Time Optimal Control", "weight": 1.0} -->

Obstacle avoidance is enforced in configuration space by approximating the ego vehicle with two circles aligned with its longitudinal axis and representing each obstacle as an ellipse. Using the Minkowski sum, denoted by $\oplus$, each obstacle is inflated by the ego geometry.

<!-- chunk {"id": "body-0045", "role": "body", "section": "II-D Nonlinear Discrete-Time Optimal Control", "weight": 1.0} -->

Resulting in constraints that are nonlinear and nonconvex in the state variables.

<!-- chunk {"id": "body-0046", "role": "body", "section": "II-D Nonlinear Discrete-Time Optimal Control", "weight": 1.0} -->

The NLP is solved using a general-purpose solver, optimizing the full state and control trajectories simultaneously. It serves as a baseline representing a direct transcription of the nonlinear optimal control problem against which the approximate GCS-based formulation is compared under consistent modeling assumptions.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

This section formalizes the motion planning problem for autonomous vehicles as a finite-dimensional mixed-integer convex optimization problem. The formulation integrates geometric path parameterization, polynomial time scaling, and a graph-of-convex-sets representation of the free space.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The admissible space is modeled as a finite union of convex polytopes,

<!-- chunk {"id": "body-0049", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

where each $\mathcal{C}_{v} \subset {\mathbb{R}}^{2}$ is a convex set associated with a vertex $v$ of the graph of convex sets $\mathcal{G} = {(\mathcal{V},\mathcal{E})}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The control points $P_{l,v}$ parameterize the geometric Bézier segment associated with region $\mathcal{C}_{v}$, while $\tau_{l,v}$ parameterize the corresponding time-scaling polynomial.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The motion planning problem over the GCS framework is therefore formulated by imposing constraints and objective terms directly on the polynomial coefficients attached to each vertex. These constraints encode geometric feasibility, dynamic feasibility, and temporal consistency, thereby transforming the original infinite-dimensional optimal control problem into a finite-dimensional mixed-integer convex program, as detailed in the subsequent sections.

<!-- chunk {"id": "body-0052", "role": "body", "section": "III-A Representations for velocity and acceleration", "weight": 1.0} -->

The geometric path and the time-scaling are represented by two separate Bézier curves, ${\mathbf{r}} = {{\mathbf{r}}{(s)}}$ and $t = {h{(s)}}$, which can be composed to produce a time-domain representation of the trajectory ${\mathbf{q}}{(t)}$. Since $h$ is assumed to be strictly increasing, it is invertible and admits an inverse $s = {h^{- 1}{(t)}} = {g{(t)}}$. The trajectory can therefore be written equivalently as

<!-- chunk {"id": "body-0053", "role": "body", "section": "III-A Representations for velocity and acceleration", "weight": 1.0} -->

Noting that $s = {g{(t)}}$ and denoting differentiation of a function $f{(s)}$ with respect to $s$ by $f^{\prime}{(s)}$, this expression simplifies to

<!-- chunk {"id": "body-0054", "role": "body", "section": "III-A Representations for velocity and acceleration", "weight": 1.0} -->

A useful relation between $\overset{˙}{g}{(t)}$ and $h^{\prime}{(s)}$ is obtained by differentiating the identity $t = {h{(s)}}$ with respect to $t$. Applying the chain rule yields

<!-- chunk {"id": "body-0055", "role": "body", "section": "III-A Representations for velocity and acceleration", "weight": 1.0} -->

Substituting this relation into the expression for $\overset{˙}{\mathbf{q}}{(t)}$ gives the compact representation for the velocity vector of the curve

<!-- chunk {"id": "body-0056", "role": "body", "section": "III-A Representations for velocity and acceleration", "weight": 1.0} -->

Differentiating once more with respect to time yields the acceleration

<!-- chunk {"id": "body-0057", "role": "body", "section": "III-A Representations for velocity and acceleration", "weight": 1.0} -->

The acceleration vector $\overset{¨}{\mathbf{q}}{(t)}$ can be decomposed into tangential and normal components relative to the geometric path. The unit tangent vector is defined as

<!-- chunk {"id": "body-0058", "role": "body", "section": "III-A Representations for velocity and acceleration", "weight": 1.0} -->

The tangential component of the acceleration is therefore

<!-- chunk {"id": "body-0059", "role": "body", "section": "III-A Representations for velocity and acceleration", "weight": 1.0} -->

To characterize the normal component, consider the derivative of the unit tangent vector,

<!-- chunk {"id": "body-0060", "role": "body", "section": "III-A Representations for velocity and acceleration", "weight": 1.0} -->

The squared norm of this vector is

<!-- chunk {"id": "body-0061", "role": "body", "section": "III-A Representations for velocity and acceleration", "weight": 1.0} -->

the normal component of the acceleration can therefore be written as

<!-- chunk {"id": "body-0062", "role": "body", "section": "III-A Representations for velocity and acceleration", "weight": 1.0} -->

where the unit normal vector $\hat{\mathbf{N}}{(s)}$ is defined as the normalized derivative of ${\mathbf{T}}{(s)}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "III-A Representations for velocity and acceleration", "weight": 1.0} -->

The representations for velocity and acceleration derived above directly motivate the dynamic constraints introduced in the optimization problem. Moreover, when the angle $\beta$ is small, the tangential and normal components derived here provide approximations of the longitudinal and lateral accelerations of the vehicle.

<!-- chunk {"id": "body-0064", "role": "body", "section": "III-B Constraints on Bézier Curves", "weight": 1.0} -->

For each vertex $v \in \mathcal{V}$ and edge ${(u,v)} \in \mathcal{E}$ in the graph of convex sets $\mathcal{G} = {(\mathcal{V},\mathcal{E})}$, constraints are imposed directly on the control points of the associated Bézier curves. These constraints encode temporal consistency, geometric feasibility, and dynamic plausibility.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Admissible space constraints", "weight": 1.0} -->

The admissible space constraints follow directly from the convex-hull property of Bézier curves. Let the convex region associated with vertex $v \in \mathcal{V}$ be represented in half-space form as $\mathcal{C}_{v} = {\{{x \in {\mathbb{R}}^{2}}\mid{{A_{v}x} \leq b_{v}}\}}$, where $A_{v} \in {\mathbb{R}}^{p_{v} \times 2}$ and $b_{v} \in {\mathbb{R}}^{p_{v}}$ define the supporting half-spaces of the polytope. Since a Bézier curve lies entirely within the convex hull of its control points, it suffices to impose

<!-- chunk {"id": "body-0066", "role": "body", "section": "Time-scaling plausibility", "weight": 1.0} -->

To ensure that the time-scaling function remains physically meaningful, two conditions are imposed on its control points $\{\tau_{0,v},\ldots,\tau_{m,v}\}$, which imply $\tau_{l,v} \geq 0$ for ${l = {0,\ldots,m}}.$

<!-- chunk {"id": "body-0067", "role": "body", "section": "Time-scaling plausibility", "weight": 1.0} -->

While $h_{\min}^{\prime} = 0$ is sufficient for monotonicity, velocity and acceleration are rational functions of $h^{\prime}{(s)}$, therefore, small values of $h^{\prime}{(s)}$ amplify both velocity and acceleration.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Velocity constraints", "weight": 1.0} -->

To ensure bounds on the magnitude of the velocity along the entire trajectory, note that the constraint ${\|{\overset{˙}{\mathbf{q}}{(t)}}\|} \leq v_{\max}$ is equivalent to

<!-- chunk {"id": "body-0069", "role": "body", "section": "Velocity constraints", "weight": 1.0} -->

This nonlinear constraint can be approximated by a polyhedral inner approximation of the unit ball. Let $a_{k} \in {\mathbb{R}}^{2}$, $k = {1,\ldots,F}$, denote the outward normals of a polygon inscribed in the unit circle. The norm inequality can then be conservatively enforced through the set of linear constraints

<!-- chunk {"id": "body-0070", "role": "body", "section": "Velocity constraints", "weight": 1.0} -->

Since ${\mathbf{r}}^{\prime}{(s)}$ and $h^{\prime}{(s)}$ are Bézier curves of degree $m - 1$, their control points are proportional to the forward differences of the original control points, namely ${\mathbf{P}}_{{l + 1},v} - {\mathbf{P}}_{l,v}$ and $\tau_{{l + 1},v} - \tau_{l,v}$, respectively. Using a polyhedral inner approximation of the unit circle with facet normals $a_{k}$, the constraint is enforced through linear inequalities of the form

<!-- chunk {"id": "body-0071", "role": "body", "section": "Velocity constraints", "weight": 1.0} -->

for all relevant indices $l$ and $k$. This construction corresponds to an inner polyhedral approximation of the Euclidean unit ball, and therefore provides a conservative enforcement of the velocity constraint.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Continuity constraints", "weight": 1.0} -->

To ensure smooth trajectories, continuity constraints are imposed on every edge ${(u,v)} \in \mathcal{E}$ of the graph of convex sets. In autonomous driving applications, continuity up to the third derivative is enforced for both the spatial curve ${\mathbf{r}}{(s)}$ and the time-scaling function $h{(s)}$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Continuity constraints", "weight": 1.0} -->

Let the forward difference operators on the control points be defined as

<!-- chunk {"id": "body-0074", "role": "body", "section": "Continuity constraints", "weight": 1.0} -->

Then continuity across edge $(u,v)$ is enforced by

<!-- chunk {"id": "body-0075", "role": "body", "section": "Continuity constraints", "weight": 1.0} -->

The same construction is applied to the control points $\tau_{l,v}$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Continuity constraints", "weight": 1.0} -->

These conditions enforce $C^{3}$ continuity across adjacent segments, ensuring that position, velocity, acceleration, and jerk remain continuous along the composed trajectory.

<!-- chunk {"id": "body-0077", "role": "body", "section": "III-C Cost Function on Bézier Curves", "weight": 1.0} -->

In autonomous driving, excessive accelerations degrade safety and passenger comfort. Although the tangential and normal acceleration expressions depend rationally on $h^{\prime}{(s)}$ and do not admit direct convex bounds, their dominant components can be controlled through convex penalties on higher-order derivatives of the spatial and temporal Bézier curves.

<!-- chunk {"id": "body-0078", "role": "body", "section": "III-C Cost Function on Bézier Curves", "weight": 1.0} -->

In continuous form, the cost density can be written as

<!-- chunk {"id": "body-0079", "role": "body", "section": "III-C Cost Function on Bézier Curves", "weight": 1.0} -->

where $\alpha_{i} \geq 0$ are tuning parameters. The terms $\|{r^{\operatorname{\prime\prime}}{(s)}}\|$ and $h^{\operatorname{\prime\prime}}{(s)}$ act as convex surrogates for lateral and longitudinal acceleration components, respectively, and the third-order terms penalize acceleration variations, suppressing oscillatory behavior. In the finite-dimensional formulation, these quantities are expressed directly in terms of forward differences of the control points.

<!-- chunk {"id": "body-0080", "role": "body", "section": "III-C Cost Function on Bézier Curves", "weight": 1.0} -->

The total objective of the optimization problem is obtained by summing $J_{v}$ over all active vertices selected by the graph flow variables.

<!-- chunk {"id": "body-0081", "role": "body", "section": "III-C Cost Function on Bézier Curves", "weight": 1.0} -->

This construction preserves computational tractability while promoting smooth, dynamically consistent trajectories but without explicit bounds on acceleration. A formulation that includes explicit bounds on acceleration, though, is of major interest in the context of vehicle dynamics and is an important research direction for future work.

<!-- chunk {"id": "body-0082", "role": "body", "section": "III-D Dynamic obstacle avoidance", "weight": 1.0} -->

Although the graph-of-convex-sets formulation assumes a static free space, dynamic obstacle avoidance can be incorporated when coarse predictions of obstacle motion are available. If an obstacle is expected to occupy a convex region $\mathcal{C}_{v}$ during an interval $\lbrack T_{in},T_{out}\rbrack$, collision avoidance can be enforced through temporal separation: the ego vehicle must either leave the region before $T_{in}$ or enter it after $T_{out}$. Since the entry and exit times correspond to the first and last control points of the time-scaling polynomial $h_{v}{(s)}$, these conditions are linear in the decision variables and remain compatible with the formulation.

<!-- chunk {"id": "body-0083", "role": "body", "section": "III-D Dynamic obstacle avoidance", "weight": 1.0} -->

In highway lane-following scenarios, where the ego and a leading vehicle share the same geometric path, collision avoidance reduces to regulating longitudinal timing. Heuristically, the traversal time of a segment is related to its arc length and average velocity. Based on this relation, constraints on entry and exit times can be used to regulate longitudinal separation from dynamic obstacles. Thus, bounding the time at which the ego exits a region implicitly bounds the average longitudinal speed, allowing safe separation from a leading vehicle without modifying the spatial curve ${\mathbf{r}}{(s)}$. It should be emphasized that this approach provides a heuristic approximation of dynamic obstacle avoidance and does not guarantee safety under arbitrary obstacle motion.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Case Studies", "weight": 1.0} -->

This section evaluates the proposed GCS formulation in representative autonomous driving scenarios and compares the resulting trajectories with those obtained from a discrete-time optimal control formulation solved as a NLP using IPOPT. The NLP formulation is used as a baseline, as it closely approximates a direct solution of the nonlinear optimal control problem. The purpose of this comparison is not to claim that the GCS approach is universally superior to existing methods, but rather to assess whether it can produce trajectories comparable to those obtained with a more exact formulation while offering a tractable alternative for motion planning. To mitigate the sensitivity of the NLP formulation to local minima, the optimization was performed in successive stages, with each stage initialized from the solution of a simpler problem. This continuation strategy improves convergence robustness.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Case Studies", "weight": 1.0} -->

All scenarios were generated using the CommonRoad framework, which provides standardized road geometries and obstacle representations and closely follows those considered in to ensure comparability with established benchmarks. Although automated methods exist for decomposing free space into convex regions, the convex sets used in this study were defined manually to isolate the performance of the proposed GCS formulation from the decomposition procedure.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Case Studies", "weight": 1.0} -->

All experiments were conducted on a MacBook Pro equipped with an M2 Pro Max processor and 32 GB of RAM. Both formulations were implemented in Python using identical vehicle parameters, dynamic limits, and planning horizons (${\Deltat} = 100$ ms, $T = 10$ s) to ensure a fair comparison. Execution time measurements over 500 runs, sufficient for convergence of statistics, are reported in Table I.

<!-- chunk {"id": "body-0087", "role": "body", "section": "IV-A Static Obstacle Avoidance", "weight": 1.0} -->

The first scenario considers static obstacle avoidance on a structured two-lane roadway. Each lane has width $3.5m$, and the two lanes span the interval $\lbrack{- {1.75m}},{\, 5.25m}\rbrack$ along the $y$-axis. The ego vehicle and the obstacles are modeled with length $4.8m$ and width $2.0m$. Two static obstacles are placed at $({15m},{- {0.5m}})$ and $({30m},{- {0.5m}})$, respectively.

<!-- chunk {"id": "body-0088", "role": "body", "section": "IV-A Static Obstacle Avoidance", "weight": 1.0} -->

The ego vehicle starts at $({0m},{0m})$ with velocity ${5m}/s$ and must reach the target region while achieving a final velocity of ${8m}/s$. The environment consists of two lane-aligned corridors with a two obstacles.

<!-- chunk {"id": "body-0089", "role": "body", "section": "IV-B Lane-Changing", "weight": 1.0} -->

The second scenario evaluates a highway lane-changing maneuver in the presence of dynamic obstacles. The road geometry and structural assumptions follow those used. The first obstacle starts at $({20.0m},{0.0m})$ with constant velocity ${3m}/s$. The second obstacle starts at $({3.0m},{3.5m})$ with constant velocity ${5m}/s$. The ego vehicle begins at $({0m},{0m})$ with velocity ${8m}/s$ and must reach the target region with velocity ${10m}/s$. The maneuver requires transitioning from the initial lane to the adjacent lane while satisfying dynamic constraints and avoiding collisions.

<!-- chunk {"id": "body-0090", "role": "body", "section": "IV-B Lane-Changing", "weight": 1.0} -->

The selected free-space decomposition for the GCS formulation, shown in Figure 3a, restricts lane transitions to an intermediate convex region (highlighted in green). Based on the predicted obstacle trajectories, a safe upper bound of $2.4s$ is imposed on the time at which the ego vehicle must enter the intermediate region to pass ahead of the second obstacle without collision. The ego vehicle must then traverse this region within $4s$ to ensure safe separation.

<!-- chunk {"id": "body-0091", "role": "body", "section": "IV-C Overtaking", "weight": 1.0} -->

The third scenario considers an overtaking maneuver on a highway segment. The first obstacle starts at $({35.0m},{0.0m})$ with velocity ${3m}/s$, accelerates linearly to ${8m}/s$, and subsequently decelerates back to ${3m}/s$. The second obstacle starts at $({5.0m},{3.5m})$ with constant velocity ${10m}/s$. The ego vehicle starts at $({0m},{0m})$ with velocity ${15m}/s$ and must reach the target region while maintaining ${15m}/s$. The maneuver requires overtaking the leading vehicle while respecting dynamic limits and avoiding collisions with both obstacles.

<!-- chunk {"id": "body-0092", "role": "body", "section": "IV-C Overtaking", "weight": 1.0} -->

The free-space decomposition adopted for the GCS formulation, shown in Figure 5a, again confines lane changes to an intermediate convex region. From the predicted obstacle trajectories, a safe upper bound of $2.7s$ is derived for the instant at which the ego vehicle must enter this region to pass the leading vehicle while avoiding the second obstacle.

<!-- chunk {"id": "body-0093", "role": "body", "section": "IV-D Discussion", "weight": 1.0} -->

The case studies indicate that the trajectories obtained using the GCS and NLP formulations are both qualitatively and quantitatively similar. Despite relying on convex free-space decomposition and polynomial trajectory parameterizations, the GCS formulation produces solutions that roughly approximate those obtained from the nonlinear optimal control problem, which directly enforces the full vehicle dynamics and exact obstacle geometry. This suggests that, under the assumptions considered, the proposed formulation captures the dominant geometric and dynamic features relevant for motion planning.

<!-- chunk {"id": "body-0094", "role": "body", "section": "IV-D Discussion", "weight": 1.0} -->

From a computational standpoint, however, the differences are substantial. The execution times reported in Table I show that the GCS approach consistently outperforms the NLP formulation, typically by approximately one order of magnitude. This improvement stems from the structural decomposition inherent to GCS: combinatorial decisions are handled explicitly through graph variables, while continuous trajectory optimization within each region remains convex. As a result, the method exhibits reduced sensitivity to initialization and improved solver robustness compared to the NLP.

<!-- chunk {"id": "body-0095", "role": "body", "section": "IV-D Discussion", "weight": 1.0} -->

Nevertheless, the dynamic profiles reveal non-negligible differences. In particular, the longitudinal acceleration in the GCS solutions tends to be more aggressive, leading to a more oscillatory longitudinal velocity profile. This behavior is largely attributable to the difficulty of imposing tight convex constraints on acceleration within the GCS framework. Although smoothness penalties on higher-order derivatives improve regularity, they do not fully replicate the direct nonlinear acceleration constraints available in the NLP formulation.

<!-- chunk {"id": "body-0096", "role": "body", "section": "IV-D Discussion", "weight": 1.0} -->

One possible avenue to improve dynamic regulation is a two-stage optimization strategy, in which the spatial curve is computed first and the time-scaling is optimized subsequently. Such a decomposition would decouple path geometry from temporal scaling, potentially enabling stricter convex enforcement of acceleration bounds. The main theoretical challenge lies in guaranteeing that the spatial trajectory obtained in the first stage admits a feasible time-scaling under the imposed dynamic constraints, which remains an open research problem.

<!-- chunk {"id": "body-0097", "role": "body", "section": "IV-D Discussion", "weight": 1.0} -->

The extension of the GCS framework to dynamic obstacle scenarios---via transition regions with associated temporal constraints---proved effective in the evaluated cases. However, the timing bounds used in these studies were derived through scenario-specific heuristic calculations. For deployment in a full autonomous driving architecture, these constraints must be generated algorithmically. In particular, a behavior planning module capable of reasoning about scene structure and predicted obstacle trajectories would be required to derive transition regions and safety timing constraints in a systematic manner. Designing this interface between behavior planning and the GCS optimization layer constitutes an important direction for future work.

<!-- chunk {"id": "body-0098", "role": "body", "section": "IV-D Discussion", "weight": 1.0} -->

Overall, the results highlight a clear trade-off between modeling fidelity and computational structure. The GCS formulation provides trajectories that closely approximate those of the nonlinear optimal control baseline while offering significantly improved computational efficiency and reduced sensitivity to initialization. At the same time, differences in dynamic regulation and the heuristic treatment of timing constraints indicate that further refinement is required to achieve tighter control over acceleration profiles and systematic integration with higher-level planning modules. These observations clarify both the practical advantages of the proposed approach and the key challenges that remain for its deployment in real-world autonomous driving systems.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper presented a motion planning framework for autonomous vehicles based on optimization over GCS combined with polynomial trajectory parameterization and time scaling. The free space was decomposed into convex regions organized as a directed graph, allowing geometric nonconvexity to be treated explicitly through discrete connectivity decisions while preserving convexity of continuous trajectory constraints within each region.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Vehicle dynamics were incorporated through a simplified dynamic bicycle model under small-slip and linear tire assumptions. By exploiting the approximate flatness of the model with respect to the position coordinates, trajectory generation was performed directly in the geometric space while maintaining dynamic consistency. Bézier curves were used to parameterize spatial trajectories and time-scaling functions, enabling convex constraints on velocity, smoothness, and region containment. Continuity constraints up to third order ensured differentiability of position, velocity, and acceleration across region boundaries.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Dynamic obstacle avoidance was addressed through temporal separation constraints and velocity modulation, particularly in structured highway scenarios where geometry and timing can be partially decoupled. The resulting formulation is a finite-dimensional mixed-integer convex program whose continuous relaxation remains convex, providing computational tractability and meaningful lower bounds.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Case studies in static obstacle avoidance and lane-changing scenarios demonstrated that the proposed approach generates collision-free and dynamically feasible trajectories while exhibiting improved robustness with respect to initialization when compared to a nonlinear discrete-time optimal control baseline.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Future work includes extending the formulation to richer vehicle models beyond the small-slip regime, incorporating tighter representations of dynamic obstacles, and investigating the separation of geometric path and time-scaling optimization as a means to obtain tighter bounds on dynamic constraints. Additionally, the integration of the proposed framework with higher-level behavioral planning strategies remains an important direction for further research, specially when it comes to improving the proposed heuristic to handle dynamic obstacles and make the computation of temporal constraints systematic.
