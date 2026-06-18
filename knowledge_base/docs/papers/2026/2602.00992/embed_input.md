<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Geometry-Aware Sampling-Based Motion Planning on Riemannian Manifolds

Topics include Natural gradients, Motion planning, Robotics, Accuracy, Scalability, Sampling-based methods, Planning, Sampling, Riemannian manifold, Euclidean geometry.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In many robot motion planning problems, task objectives and physical constraints induce non-Euclidean geometry on the configuration space, yet many planners operate using Euclidean distances that ignore this structure. We address the problem of planning collision-free motions that minimize length under configuration-dependent Riemannian metrics, corresponding to geodesics on the configuration manifold. Conventional numerical methods for computing such paths do not scale well to high-dimensional systems, while sampling-based planners trade scalability for geometric fidelity. To bridge this gap, we propose a sampling-based motion planning framework that operates directly on Riemannian manifolds. We introduce a computationally efficient midpoint-based approximation of the Riemannian geodesic distance and prove that it matches the true Riemannian distance with third-order accuracy. Building on this approximation, we design a local planner that traces the manifold using first-order retractions guided by Riemannian natural gradients.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Experiments on a two-link planar arm and a 7-DoF Franka manipulator under a kinetic-energy metric, as well as on rigid-body planning in SE with non-holonomic motion constraints, demonstrate that our approach consistently produces lower-cost trajectories than Euclidean-based planners and classical numerical geodesic-solver baselines.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robotic motion planning is often posed as a search for collision-free paths through a configuration space. For many robotic systems, the configuration space is a non-Euclidean manifold. For example, rigid-body poses live on Lie groups such as ${SE}{}$ and ${SE}{}$, while articulated manipulators live on products of circles (tori). More generally, closed-chain or task constraints induce implicit manifolds embedded in a higher-dimensional ambient space. In these settings, planning feasibility and optimality have clear geometric interpretations: feasibility is governed by the intrinsic manifold structure and constraints, while optimality depends on how we measure the cost of motion along the manifold.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A natural way to encode such costs is via a Riemannian metric on the appropriate configuration manifold. This metric induces a notion of distance on the manifold, and the resulting shortest paths, called geodesics, generalize straight lines in Euclidean spaces to curved manifolds. This abstraction recovers classical shortest-path planning in Euclidean configuration spaces as a special case, while also capturing costs that vary smoothly with configuration. Examples of configuration-dependent metrics include the kinetic-energy metric commonly used in manipulation, as well as group-invariant metrics on Lie groups. In these settings, optimal motion planning becomes the problem of finding collision-free paths that minimize Riemannian arc length under either a constant or smoothly varying metric.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We study the problem of computing minimum-length geodesics on Riemannian manifolds arising in robotic motion planning. Finding such paths in high dimensions is computationally expensive. Classical approaches either directly solve the geodesic ordinary differential equations as a boundary value problem or minimize a variational energy functional. While effective in low dimensions, these methods scale poorly to high-dimensional robotic systems, struggling to satisfy feasibility and optimality while respecting constraints like joint limits and obstacles in real-time. Sampling-based motion planning offers a scalable alternative. Algorithms such as the Rapidly-exploring Random Tree (RRT) and its anytime variants have been widely adopted in robotic motion planning and shown to scale well in high dimensions. Most existing sampling-based approaches measure distances and interpolate motions using an ambient Euclidean metric. Consequently, they may ignore the intrinsic geometry of the configuration manifold, leading to motions that violate manifold constraints or are infeasible. Constrained motion planning techniques combine numerical continuation with sampling-based planning to address these feasibility problems by searching directly on the manifold. However, optimality is usually expressed through a fixed Euclidean metric, leaving a gap between manifold-aware feasibility and metric-aware optimality.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we develop geometry-aware subroutines that allow anytime sampling-based planners to optimize Riemannian path length directly on configuration manifolds. This generalizes prior approaches by supporting both constant and smoothly varying Riemannian metrics (Figure 1). Our contributions are summarized as follows.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a midpoint-based approximation of the Riemannian geodesic distance and prove that its approximation error vanishes asymptotically with third-order accuracy.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We design a geometry-aware local planner that traces the manifold using retraction steps along the Riemannian natural gradient under a configuration-dependent metric.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We empirically validate our approach on energy-minimizing motion planning problems for serial manipulators and on non-holonomic planning tasks on ${SE}{}$, demonstrating consistently lower-cost paths compared to baselines.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Riemannian Metrics and Manifolds", "weight": 1.0} -->

Let $\mathcal{M}$ be an $n$-dimensional manifold embedded in an ambient linear space $\mathcal{E}$ (e.g., $\mathcal{M} \subseteq {\mathbb{R}}^{d}$ with $d \geq n$). By definition, $\mathcal{M}$ is a topological space that is locally Euclidean, meaning that each point $q \in \mathcal{M}$ has a neighborhood homeomorphic to an open subset of ${\mathbb{R}}^{n}$. The tangent space $\mathcal{T}_{q}\mathcal{M}$ at a point $q \in \mathcal{M}$ consists of the velocity vectors of all smooth curves on $\mathcal{M}$ passing through $q$. When $\mathcal{M}$ is embedded in $\mathcal{E}$, the tangent space $\mathcal{T}_{q}\mathcal{M}$ may be identified with a linear subspace of $\mathcal{E}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Riemannian Metrics and Manifolds", "weight": 1.0} -->

The collection of all tangent spaces forms the tangent bundle, defined as the disjoint union

<!-- chunk {"id": "body-0013", "role": "body", "section": "Riemannian Metrics and Manifolds", "weight": 1.0} -->

Since each tangent space is a vector space, we can define an inner product on $\mathcal{T}_{q}\mathcal{M}$, given by a bilinear, symmetric and positive definite map ${\langle \cdot, \cdot \rangle}_{q}:{{{{\mathcal{T}_{q}\mathcal{M}} \times \mathcal{T}_{q}}\mathcal{M}}\rightarrow{\mathbb{R}}}$. This inner product induces a norm $\left\| v \right\|_{q} = {\langle v,v\rangle}_{q}^{1/2}$ on tangent vectors. A Riemannian metric $G_{q}$ on $\mathcal{M}$ is a smoothly varying choice of such inner products for each $q \in \mathcal{M}$ acting on $\mathcal{T}\mathcal{M}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Riemannian Metrics and Manifolds", "weight": 1.0} -->

In local coordinates, the Riemannian inner product between two tangent vectors ${u,v} \in {\mathcal{T}_{q}\mathcal{M}}$ can be written as

<!-- chunk {"id": "body-0015", "role": "body", "section": "Riemannian Metrics and Manifolds", "weight": 1.0} -->

where $G_{q}$ is a symmetric positive definite matrix representing the metric at $q$. A manifold $\mathcal{M}$ equipped with a Riemannian metric is called a Riemannian manifold.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Distances and Geodesics", "weight": 1.0} -->

Given a Riemannian manifold $\mathcal{M}$, the metric induces a natural notion of length for smooth curves on $\mathcal{M}$, and consequently defines a distance function, making $\mathcal{M}$ into a metric space. For a piecewise smooth curve $\pi:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{M}}$, its length is defined as the integral of its speed under the Riemannian metric,

<!-- chunk {"id": "body-0017", "role": "body", "section": "Distances and Geodesics", "weight": 1.0} -->

This induces the *Riemannian distance* between two points on the manifold

<!-- chunk {"id": "body-0018", "role": "body", "section": "Distances and Geodesics", "weight": 1.0} -->

where the infimum is taken over all piecewise smooth curves $\pi$ such that ${\pi{}} = q_{x}$ and ${\pi{}} = q_{y}$. Geodesics are curves that locally minimize this distance, generalizing the notion of straight lines in Euclidean space. Equivalently, geodesics between two fixed endpoints minimize the curve energy

<!-- chunk {"id": "body-0019", "role": "body", "section": "Distances and Geodesics", "weight": 1.0} -->

They satisfy the geodesic ordinary differential equation (ODE)

<!-- chunk {"id": "body-0020", "role": "body", "section": "Distances and Geodesics", "weight": 1.0} -->

where ${q{(t)}} = {({q^{1}{(t)}},\ldots,{q^{n}{(t)}})}$ denotes the local coordinate representation of $\pi{(t)}$.^11^1We use the Einstein summation convention here. Here, $\Gamma_{ij}^{k}$ are the Christoffel symbols of the second kind, computed directly from the Riemannian metric and given by

<!-- chunk {"id": "body-0021", "role": "body", "section": "Distances and Geodesics", "weight": 1.0} -->

which describe how the coordinate basis varies across the manifold. Computing geodesics from requires solving a boundary value problem, which becomes computationally challenging in high-dimensional spaces. For this reason, rather than solving the geodesic ODEs directly, we consider minimizing the curve length in under the intrinsic Riemannian metric (see Section 3.3).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Motion Planning Problem Formulation", "weight": 1.0} -->

Let $\mathcal{Q} \subseteq \mathcal{M}$ denote the configuration manifold (for example, a constrained lower-dimensional submanifold), with each $q \in \mathcal{Q}$ representing a configuration of the system. In this work, we restrict attention to the unconstrained case $\mathcal{Q} = \mathcal{M}$, while retaining the notation $\mathcal{Q}$ for generality. Let $\mathcal{Q}_{\text{obs}} \subsetneq \mathcal{Q}$ denote the set of configurations in collision with obstacles. The obstacle-free configuration space is defined as $\mathcal{Q}_{\text{free}} = {\mathcal{Q} \smallsetminus \mathcal{Q}_{\text{obs}}}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Motion Planning Problem Formulation", "weight": 1.0} -->

where $\Sigma$ denotes the set of all piecewise smooth feasible paths.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Motion Planning Problem Formulation", "weight": 1.0} -->

In this work, we address the planning problem in by adopting sampling-based motion planning methods. Specifically, we search for solutions by incrementally constructing a rapidly-exploring random tree through random sampling, and refining it via incremental rewiring to asymptotically approach shortest paths in $\mathcal{Q}_{\text{free}}$. This strategy enables scalability to high-dimensional configuration spaces while respecting the intrinsic geometry of the manifold. Because the Riemannian metric generally distorts the space, shortest paths are no longer straight lines in the ambient space $\mathcal{E}$ (e.g., ${\mathbb{R}}^{d}$), and it is therefore critical that distance computations and interpolations within the planner remain consistent with the underlying manifold structure. We address geometric consistency in Section 4.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Geodesic Motion Planning on Riemannian Manifolds", "weight": 1.0} -->

This section develops the geometry-aware subroutines that enable sampling-based motion planning algorithms to find geodesic paths on Riemannian manifolds. We first introduce a computationally efficient approximation of geodesic distance between configurations (Section 4.1). We then describe a gradient-based interpolation procedure that uses this distance to extend the search tree while respecting the underlying geometry of the manifold (Section 4.2).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Distance Between Configurations", "weight": 1.0} -->

The distance between two configurations on a Riemannian manifold is defined as the length of the shortest connecting curve under the intrinsic metric. Exact evaluation of this distance requires solving a geodesic boundary value problem, which is impractical for online use due to the repeated calls required by nearest-neighbour queries and tree rewiring in sampling-based planners. Accordingly, we approximate the geodesic distance by evaluating the Riemannian metric at the midpoint of the two configurations and computing the length of a piecewise path in the midpoint tangent space. This approximation is computationally 'cheap' since it requires only a single metric evaluation per subroutine call. We later show that this midpoint-based approximation converges to the true geodesic distance as the configurations become arbitrarily close to each other (Theorem 4.1).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Distance Between Configurations", "weight": 1.0} -->

We begin by analyzing the geometry of the geodesic midpoint and establish that this formulation yields an exact distance identity.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Vertex Expansion", "weight": 1.0} -->

Sampling-based motion planning methods typically require a fast and efficient procedure for connecting two configurations, a process often referred to as local planning. In the case of RRTs, for example, this operation attempts to connect the nearest neighbour to a randomly sampled configuration using an edge of bounded length, thereby generating a new candidate configuration. In Euclidean spaces, such connections are typically implemented using straight-line interpolation. On curved configuration spaces, however, this task requires finding geodesics that locally minimize distance while respecting the intrinsic geometry of the manifold.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Vertex Expansion", "weight": 1.0} -->

At a high level, our method performs this interpolation by constructing a discrete approximation to a geodesic that follows the natural gradient of the squared Riemannian distance potential. Rather than solving for a continuous curve in closed form, we generate a sequence of configurations by iteratively descending along this gradient. Such descent requires moving around the manifold along a specified direction, for which we make use of retractions (Definition 2 ‣ 4.1 Distance Between Configurations ‣ 4 Geodesic Motion Planning on Riemannian Manifolds ‣ Geometry-Aware Sampling-Based Motion Planning on Riemannian Manifolds")). A retraction maps a configuration $q \in \mathcal{M}$ and a tangent vector $v \in {\mathcal{T}_{q}\mathcal{M}}$ to a new point on the manifold, thereby allowing local movement while remaining on $\mathcal{M}$.^22^2For example, on a linear manifold, the mapping ${\mathcal{R}_{q}{(v)}} = {q + v}$ is a valid retraction.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Vertex Expansion", "weight": 1.0} -->

We next formalize the notion of gradients on a Riemannian manifold (Definition 3 ‣ 4.2 Vertex Expansion ‣ 4 Geodesic Motion Planning on Riemannian Manifolds ‣ Geometry-Aware Sampling-Based Motion Planning on Riemannian Manifolds")).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

We validate our proposed approach through two use cases to demonstrate the versatility of geometry-aware sampling-based planners for robot motion planning problems. First, we evaluate the planner's ability to find minimum-energy motions for serial-link manipulators (Section 5.1). Second, we apply the method to rigid-body planning on ${SE}{}$ under nonholonomic constraints (Section 5.2 ‣ 5 Experiments ‣ Geometry-Aware Sampling-Based Motion Planning on Riemannian Manifolds")). We compare against standard numerical optimization baselines, including a boundary value problem (BVP) solver and a variational energy minimization method, as well as a sampling-based planner using a Euclidean metric. To enforce obstacle avoidance in the optimization-based methods, we reshape the metric using standard exponential barrier functions and tune the corresponding parameters to achieve the best performance possible. To account for the sensitivity of variational solvers to initial conditions and the stochasticity of sampling-based methods, we conduct all experiments over $50$ trials with start and goal configurations perturbed by Gaussian noise, running each sampling-based planner $10$ times per trial.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

In all experiments, we use the Open Motion Planning Library (OMPL) implementation of RRT\* as the underlying sampling-based planner.^33^3Code is publicly available at For geodesic computation with the variational solvers, we use the StochMan Python library to represent geodesics as cubic splines with a fixed number of control points and optimize them to minimize the Riemannian energy functional, following.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

Throughout our analysis, we evaluate path quality using geodesic length and energy, both measured under the Riemannian metric specific to each experiment. To ensure consistent reporting, we reparameterize all solution paths to unit-speed curves prior to evaluation and then report the geometric length (which is invariant to parameterization) and the Dirichlet energy functional defined, which quantifies the smoothness of the geodesic.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Serial Link Manipulators", "weight": 1.0} -->

This section presents experimental results assessing the effectiveness of our approach for motion planning with configuration-dependent Riemannian metrics for serial manipulators. In all experiments, we define the Riemannian metric using the manipulator's mass-inertia matrix, computed via the composite rigid body algorithm implemented in the Pinocchio library. Under this metric, geodesics correspond to motions that minimize kinetic energy for a given traversal time.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Two-Link Planar Arm", "weight": 1.0} -->

We first consider a simple 2-DoF planar manipulator in an obstacle-free environment. The arm consists of two identical links, each with a length of $1.0$ m and a mass of $1.0$ kg^44^4Links are modelled as uniform slender rods with centres of mass at the midpoints.. The task is to plan a motion from an initial configuration of $q_{\text{start}} = {\lbrack{- {\pi/4}},{- {\pi/4}}\rbrack}^{\mathsf{T}}$ to a goal configuration of $q_{\text{goal}} = {\lbrack{{3\pi}/4},{{3\pi}/4}\rbrack}^{\mathsf{T}}$. Unlike the Euclidean baseline, which yields a straight-line path in configuration space, our approach correctly recovers the curved Riemannian geodesic (Figure 3).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Two-Link Planar Arm", "weight": 1.0} -->

Even with identical link masses, the effective inertia at the base joint is higher than at the elbow joint; our planner naturally captures this property, generating trajectories that minimize the mechanical work. We also observe that classical numerical baselines (both BVP and variational solvers) are highly sensitive to the initial guess; when initialized with a standard straight-line path, they frequently converge to suboptimal solutions. In contrast, our geometry-aware sampling-based planner consistently recovers the globally optimal geodesic without requiring any prior knowledge of the solution geometry, successfully navigating the nonlinear energy landscape where optimization methods struggle. This behavior highlights the strong dependence of classical numerical methods on initialization in highly nonconvex energy landscapes. By contrast, the sampling-based formulation instead leverages geometric structure to explore multiple homotopy classes, enabling reliable convergence to the global geodesic without requiring problem-specific initialization.

<!-- chunk {"id": "body-0037", "role": "body", "section": "7-DoF Franka", "weight": 1.0} -->

To evaluate scalability in high-dimensional spaces, we apply our planner to a 7-DoF Franka Emika robot operating in a cluttered environment. We utilize the table pick environment from the MotionBenchMaker dataset, where the robot must navigate from a start configuration to a grasp pose while avoiding collisions with the table and surrounding obstacles (Figure 1). Because of the dimensionality and complexity of this problem, we exclude the BVP solver from the set of baselines due to its poor scaling behavior. Table 1 summarizes the results over 50 trials. From the data, we observe that all methods achieved high success rates in this setting. Since we employ a single-tree RRT\* as the underlying sampling-based planner, some trials fail to reach the goal due to sampling stochasticity; this limitation could be mitigated by adopting a bidirectional search strategy, for example. While the Euclidean approach reliably finds feasible paths, it does not account for the robot's configuration-dependent inertia, often producing high-energy motions that unnecessarily excite the heavy base joints.

<!-- chunk {"id": "body-0038", "role": "body", "section": "7-DoF Franka", "weight": 1.0} -->

Conversely, although the variational solver explicitly minimizes energy, the reshaping of the metric induces a complex, non-convex landscape, making the method sensitive to local minima and requiring careful tuning of barrier parameters. In contrast, our geometry-aware planner consistently produces lower kinetic-energy paths than both baselines, effectively handling obstacle avoidance constraints implicitly without the need for explicit metric design.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Planning on ${SE}{}$", "weight": 1.0} -->

We next apply our framework to rigid-body planning on the special Euclidean group ${SE}{}$ to demonstrate how metric design can enforce specific kinematic behaviors without explicitly encoding them as nonholonomic constraints, as is common in kinodynamic motion planners. We evaluate our approach on a large-scale navigation environment from the literature, the Willow Garage map, considering two distinct scenarios, Doorway and Corridor (Figure 4 ‣ 5 Experiments ‣ Geometry-Aware Sampling-Based Motion Planning on Riemannian Manifolds")). To examine the effect of metric shaping, we employ left-invariant Riemannian metrics defined by a diagonal weight matrix in the body frame, $G = {\text{diag}{(w_{x},w_{y},w_{\theta})}}$, which assigns independent costs to longitudinal translation, lateral translation, and rotation \[3")\]. In this experiment, we penalize lateral translation by making the metric highly anisotropic (i.e., $w_{y} \gg w_{x}$), effectively creating a 'soft' nonholonomic constraint.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Planning on ${SE}{}$", "weight": 1.0} -->

As reported in Table 1, both the Euclidean baseline and our proposed method achieve a 100$\%$ success rate in finding collision-free paths within the available planning time. The variational method, however, often struggles with the complex geometry of the environment, particularly in the Corridor scenario, where it attains only an $8\%$ success rate. This behavior reflects the sensitivity of variational solvers to initialization and the difficulty of tuning barrier-function weights to navigate narrow passages without becoming trapped in local minima or violating collision constraints. Although the Euclidean planner reliably finds feasible paths, the quality of its solutions is poor, incurring substantially higher geodesic length and energy costs compared to our method. As shown in Figure 4 ‣ 5 Experiments ‣ Geometry-Aware Sampling-Based Motion Planning on Riemannian Manifolds"), the geodesics found by the Euclidean planner ignore the anisotropic nature of the underlying metric, resulting in unnatural skidding or screw motions where the rigid body translates laterally.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Planning on ${SE}{}$", "weight": 1.0} -->

Conversely, our geometry-aware planner naturally recovers the soft nonholonomic behavior implied by the intrinsic Riemannian metric, aligning the orientation with the direction of travel to minimize energy and producing significantly shorter geodesics than the baselines.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This work presents a geometry-aware sampling-based planning framework for robot configuration spaces equipped with a Riemannian metric. Our main contribution is a midpoint-based distance approximation on Riemannian manifolds that can be evaluated using only retractions and local metric information, yet matches the true Riemannian distance with third-order accuracy. This approximation makes the distance-based subroutines of sampling-based planners more consistent with the intrinsic motion costs than those of Euclidean baselines, while avoiding the expense of solving geodesic boundary-value problems. We further show how the same ingredients enable a geometry-aware local interpolation approach based on discrete retraction steps and Riemannian natural gradients. Across manipulation and ${SE}{}$ problems under anisotropic metrics, our method consistently produces higher-quality solutions under the target metric, especially in settings where Euclidean or isotropic assumptions are misleading. Future work will explore the full implications of our approach. In particular, we plan to investigate the design of heuristic functions in curved spaces to focus search on promising regions of the configuration space.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We are also interested in studying tighter theoretical guarantees when our proposed geometry-aware subroutines are used within asymptotically optimal planners.
