<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimal Sampling-Based Motion Planning under Differential Constraints: The Drift Case with Linear Affine Dynamics

Topics include Motion planning, Sampling-based methods, Planning, Control, Sampling, Constraints.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we provide a thorough, rigorous theoretical framework to assess optimality guarantees of sampling-based algorithms for drift control systems: systems that, loosely speaking, can not stop instantaneously due to momentum. We exploit this framework to design and analyze a sampling-based algorithm (the Differential Fast Marching Tree algorithm) that is asymptotically optimal, that is, it is guaranteed to converge, as the number of samples increases, to an optimal solution. In addition, our approach allows us to provide concrete bounds on the rate of this convergence. The focus of this paper is on mixed time/control energy cost functions and on linear affine dynamical systems, which encompass a range of models of interest to applications (e.g., double-integrators) and represent a necessary step to design, via successive linearization, sampling-based and provably-correct algorithms for non-linear drift control systems. Our analysis relies on an original perturbation analysis for two-point boundary value problems, which could be of independent interest.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key problem in robotics is how to compute an obstacle-free and dynamically-feasible trajectory that a robot can execute. The problem, in the simplest setting where the robot does not have kinematic/dynamical (in short, differential) constraints on its motion and the problem becomes one of finding an obstacle-free "geometric" path, is reasonably well-understood and sound algorithms exist for most practical scenarios. However, robotic systems *do* have differential constraints (e.g., momentum), which most often cannot be neglected. Despite the long history of robotic motion planning, the inclusion of differential constraints in the planning process is currently considered an open challenge, in particular with respect to guarantees on the quality of the obtained solution and class of dynamical systems that can be addressed. Arguably, the most common approach in this regard is a decoupling approach, whereby the problem is decomposed in steps of computing a collision-free path (neglecting the differential constraints), smoothing the path to satisfy the motion constraints, and finally reparameterizing the trajectory so that the robot can execute it.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This approach, while oftentimes fairly computationally efficient, presents a number of disadvantages, including computation of trajectories whose cost (e.g., length or control effort) is far from the theoretical optimum or even failure in finding any solution trajectory due to the decoupling scheme itself. For these reasons, it has been advocated that there is a need for planning algorithms that solve the differentially-constrained motion planning problem (henceforth referred to as the DMP problem) *in one shot*, i.e., without decoupling.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Broadly speaking, the DMP problem can be divided into two categories: (i) DMP for driftless systems, and (ii) DMP for drift systems. Intuitively, systems with drift constraints are systems where from some states it is impossible to stop instantaneously (this is typically due to momentum). More rigorously, a system $\overset{˙}{\mathbf{x}} = {f{(\mathbf{x},\mathbf{u})}}$ is a drift system if for some state $\mathbf{x}$ there does not exist any admissible control $\mathbf{u}$ such that ${f{(\mathbf{x},\mathbf{u})}} = 0$. For example the basic, yet representative, double integrator system $\overset{¨}{\mathbf{x}} = \mathbf{u}$ (modeling the motion of a point mass under controlled acceleration) is a drift system.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

From a planning perspective, DMP for drift systems is more challenging than its driftless counterpart, due, for example, to the inherent lack of symmetries in the dynamics and the presence of regions of inevitable collision (that is, sets of states from which obstacle collision will eventually occur, regardless of applied controls).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To date, the state of the art for one-shot solutions to the DMP problem (both for driftless and drift systems) is represented by sampling-based techniques, whereby an explicit construction of the configuration space is avoided and the configuration space is probabilistically "probed" with a sampling scheme. Arguably, the most successful algorithm for DMP to date is the rapidly-exploring random tree algorithm (RRT), which incrementally builds a tree of trajectories by randomly sampling points in the configuration space. However, the RRT algorithm lacks optimality guarantees, in the sense that one can prove that the cost of the solution returned by RRT converges to a suboptimal cost as the number of sampled points goes to infinity, almost surely. An asymptotically-optimal version of RRT for the geometric (i.e., without differential constraints) case has been recently presented. This version, named RRT^∗^, essentially adds a rewiring stage to the RRT algorithm to counteract its greediness in exploring the configuration space.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prompted by this result, a number of works have proposed extensions of RRT^∗^ to the DMP problem, with the goal of retaining the asymptotic optimality property of RRT^∗^. Care must be taken in arguing optimality for drift systems in particular, as the control asymmetry requires a consideration of both forward-reachable and backward-reachable trajectory approximations. Even in the driftless case, the matter of assessing optimality is quite subtle, and hinges upon a careful characterization of a system's locally reachable sets in order to ensure that a planning algorithm examines "enough volume" in its operation, and thus enough sample points, to ensure asymptotic optimality. Another approach to asymptotically optimal DMP planning is given by STABLE SPARSE RRT which achieves optimality through random control propagation instead of connecting sampled points using a steering subroutine. This paper, like the RRT^∗^ variations, is based on a steering function, although it may be considered less general, as it is our view that leveraging as much knowledge as possible of the differential constraints while planning is necessary for the goal of planning in real-time.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In our related work we provide a theoretical framework to study optimality guarantees of sampling-based algorithms for the DMP problem by focusing on *driftless* control-affine dynamical systems of the form ${\overset{˙}{\mathbf{x}}{(t)}} = {\sum_{i = 1}^{m}{g_{i}{({\mathbf{x}{(t)}})}\mathbf{u}_{i}{(t)}}}$. While this model is representative for a large class of robotic systems (e.g., mobile robots with wheels that roll without slipping and multi-fingered robotic hands), it is of limited applicability in problems where momentum (i.e., drift) is a key feature of the problem setup (e.g., for a spacecraft or a helicopter).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Statement of Contributions*: The objective of this paper is to provide a theoretical framework to study optimality guarantees of sampling-based algorithms for the DMP problem with *drift*. Specifically, as, we focus on linear affine systems of the form

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $\mathcal{M}$ and $\mathcal{U}$ are the configuration and control spaces, respectively, and it is of interest to find an obstacle-free trajectory $\pi$ that minimizes the mixed time/energy criterion

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $R$ is a positive definite matrix that weights control energy expenditure versus traversal time. Henceforth, we will refer to a DMP problem involving linear affine dynamics and a mixed time/energy cost criterion as Linear Quadratic DMP (LQDMP). The LQDMP problem is relevant to applications for two main reasons: (i) it models the "essential" features of a number of robotic systems (e.g., spacecraft in deep space, helicopters, or even ground vehicles), and (ii) its theoretical study forms the backbone for sampling-based approaches that rely on linearization of more complex underlying dynamics. From a theoretical and algorithmic standpoint, the LQDMP problem presents two challenging features: (i) dynamics are not symmetric, which makes forward and backward reachable sets different and requires a more sophisticated analysis of sampling volumes to prove asymptotic optimality, and (ii) not all directions of motion are equivalent, in the sense that some motions incur dramatically higher cost than others due to the algebraic structure of the constraints.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Indeed, these are the very same challenges that make the DMP problem with drift difficult in the first place, and they make approximation arguments (e.g., those needed to prove asymptotic optimality) more involved. Fortunately, for LQDMP an explicit characterization for the optimal trajectory connecting two sampled points in the absence of obstacles is available, which provides a foothold to begin the analysis. Specifically, the contribution of this paper is threefold. First, we show that *any* trajectory in an LQDMP problem may be "traced" arbitrarily well, with high probability, by connecting randomly distributed points from a sufficiently large sample set covering the configuration space. We will refer to this property as *probabilistic exhaustivity*, as opposed to probabilistic completeness, where the requirement is that *at least* one trajectory is traced with a sufficiently large sample set. Second, we introduce a sampling-based algorithm for solving the LQDMP problem, namely the Differential Fast Marching Tree algorithm (DFMT^∗^), whose design is enabled by our analysis of the notion of probabilistic exhaustivity.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, we are able to give a precise characterization of neighborhood radius, an important parameter for many asymptotically optimal motion planners, in contrast with previous work on LQDMP. Third, by leveraging probabilistic exhaustivity, we show that DFMT^∗^ is asymptotically optimal. This analysis framework builds upon, and elements of our approach are inspired. We note that, the authors present an excellent extension of RRT^∗^ that successfully solves the LQDMP problem in simulations, even when extended to linearized systems. The asymptotic optimality claim, however, relies only on a near-neighbor set size argument: we aim to put the analysis of the LQDMP problem on more rigorous theoretical footing.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Organization*: This paper is structured as follows. In Section II we formally define the DMP problem we wish to solve. In Section III we review known results about the problem of optimally connecting fixed initial and terminal states under linear affine dynamics with a quadratic cost function. Furthermore, we provide a simple, yet novel (to the best of our knowledge) asymptotic characterization of the spectrum of the weighted controllability Gramian, which is instrumental to our analysis. In Section IV we prove the aforementioned probabilistic exhaustivity property for drift systems with linear affine dynamics. In Section V we present the DFMT^∗^ algorithm, and in Section VI we discuss its asymptotic optimality (together with a convergence rate characterization). Section VII contains proof-of-concept simulations. Finally, in Section VIII we discuss several features of our analysis, we draw some conclusions, and we discuss directions for future work.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Let $\mathcal{M} \subseteq {\mathbb{R}}^{n}$ and $\mathcal{U} \subseteq {\mathbb{R}}^{m}$ be the configuration space and control space, respectively, of a robotic system. Within this space let us assume the dynamics of the robot are given by the linear affine system

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

A tuple $\pi = {({\mathbf{x}{\lbrack\rbrack}},{\mathbf{u}{\lbrack\rbrack}},T)}$ defines a *dynamically feasible* trajectory, alternatively path, if the state evolution $\mathbf{x}:{{\lbrack 0,T\rbrack}\rightarrow\mathcal{M}}$ and control input $\mathbf{u}:{{\lbrack 0,T\rbrack}\rightarrow\mathcal{U}}$ satisfy equation for all $t \in {\lbrack 0,T\rbrack}$. We define the cost of a trajectory $\pi$ by the function

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

where $R \in {\mathbb{R}}^{m \times m}$ is symmetric positive definite, constant, and given. We may rewrite this cost function as ${c{\lbrack\pi\rbrack}} = {T + {c_{u}{\lbrack\pi\rbrack}}}$, where ${c_{u}{\lbrack\pi\rbrack}} = {\int_{0}^{T}{\mathbf{u}{\lbrack t\rbrack}^{T}R\mathbf{u}{\lbrack t\rbrack}{dt}}}$, with the interpretation that this cost function penalizes both trajectory duration $T$ and control effort $c_{u}$. The matrix $R$ determines the relative costs of the control inputs, as well as their costs relative to the duration of the trajectory. We denote this linear affine dynamical system with cost by $\Sigma = {(A,B,\mathbf{c},R)}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Let $\Pi$ be the set of all feasible paths. The objective is to find the feasible path with minimum associated cost.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Our analysis will rely on two key sets of assumptions, relating, respectively, to the system $\Sigma$ and the problem-specific parameters $\mathcal{M}_{\text{free}},\mathbf{x}_{\text{init}},\mathcal{M}_{\text{goal}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

*Assumptions on system*: We assume that the system $\Sigma$ is controllable, (i.e., the pair $(A,B)$ is controllable) so that even disregarding obstacles there exist dynamically feasible trajectories between states.^11^1This system controllability assumption is why we do not fold the constant drift term $\mathbf{c}$ into the state $\mathbf{x}$. Also, we assume that the control space is unconstrained, i.e. $\mathcal{U} = {\mathbb{R}}^{m}$, and that the cost weight matrix $R$ is symmetric positive definite, so that every control direction has positive cost. These assumptions will be collectively referred to as $A_{\Sigma}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

*Assumptions on problem parameters*: We require that the configuration space is a compact subset of ${\mathbb{R}}^{n}$ so that we may sample from it. Furthermore, we require that the goal region $\mathcal{M}_{\text{goal}}$ has *regular boundary*, that is there exists $\xi > 0$ such that for almost all $\mathbf{y} \in {\partial\mathcal{M}_{\text{goal}}}$, there exists $\mathbf{z} \in \mathcal{M}_{\text{goal}}$ with ${B{\lbrack\mathbf{z},\xi\rbrack}} \subseteq \mathcal{M}_{\text{goal}}$ and $\mathbf{y} \in {\partial{B{\lbrack\mathbf{z},\xi\rbrack}}}$, where $B$ denotes the Euclidean 2-norm ball.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

This requirement that the boundary of the goal region has bounded curvature almost everywhere ensures that a sampling procedure may expect to select points in the goal region near any point on the region's boundary. We make requirements on the *clearance* of the optimal trajectory, i.e., its "distance" from $\mathcal{M}_{\text{obs}}$. For a given $\delta > 0$, the $\delta$-interior of $\mathcal{M}_{\text{free}}$ is the set of all states that are at least a Euclidean distance $\delta$ away from any point in $\mathcal{M}_{\text{obs}}$. A collision-free path $\pi$ is said to have strong $\delta$-clearance if its state trajectory $\mathbf{x}$ lies entirely inside the $\delta$-interior of $\mathcal{M}_{\text{free}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

A collision-free path $\pi$ is said to have weak $\delta$-clearance if there exists a path $\pi^{\prime}$ that has strong $\delta$-clearance and there exists a homotopy $\psi$, with ${\psi{\lbrack 0\rbrack}} = \pi$ and ${\psi{\lbrack 1\rbrack}} = \pi^{\prime}$ that satisfies the following three properties: (a) $\psi{\lbrack\alpha\rbrack}$ is a dynamically feasible trajectory for all $\alpha \in {(0,1\rbrack}$, (b) ${\lim_{\alpha\rightarrow 0}{c{\lbrack{\psi{\lbrack\alpha\rbrack}}\rbrack}}} = {c{\lbrack\pi\rbrack}}$, and (c) for all $\alpha \in {(0,1\rbrack}$ there exists $\delta_{\alpha} >

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

0$ such that $\psi{\lbrack\alpha\rbrack}$ has strong $\delta_{\alpha}$-clearance.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Properties (a) and (b) are required since pathological obstacle sets may be constructed that squeeze all optimum-approximating homotopies into undesirable motion. In practice, however, as long as $\mathcal{M}_{\text{free}}$ does not contain any passages of infinitesimal width, the fact that $\Sigma$ is controllable will allow every trajectory to be weak $\delta$-clear. We claim that these assumptions about the problem parameters are mild, and can be regarded as "minimum" regularity assumptions.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

All trajectories discussed in this paper are dynamically feasible unless otherwise noted. The symbol $\parallel \cdot \parallel$ denotes the 2-norm, induced or otherwise. The asymptotic notations $O,\Omega,\Theta,o$ mean bounded above, bounded below, bounded both above and below, and asymptotically dominated, respectively.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Optimal Control in the Absence of Obstacles", "weight": 1.0} -->

The goal of this section is twofold: to review results about two-point boundary value problems for linear affine systems, and to present a simple, yet novel asymptotic characterization of the spectrum of the controllability Gramian. Both results will be instrumental to our analysis of LQDMP.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Two Point Boundary Value Problem", "weight": 1.0} -->

The material in this section is standard, we provide it to make the paper self-contained. Our presentation follows the treatment. Specifically, this section is concerned with local steering between states in the absence of environment boundaries and obstacles. Given a start state $\mathbf{x}_{0} \in \mathcal{M}$ and an end state $x_{1} \in \mathcal{M}$, the *two point boundary value problem* (2BVP) is to find a trajectory $\pi = {(\mathbf{x},\mathbf{u},\tau^{\ast})}$ between ${\mathbf{x}{\lbrack 0\rbrack}} = \mathbf{x}_{0}$ and ${\mathbf{x}{\lbrack\tau^{\ast}\rbrack}} = \mathbf{x}_{1}$ that satisfies the system $\Sigma$ and minimizes its cost function.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Two Point Boundary Value Problem", "weight": 1.0} -->

Let us define the weighted controllability Gramian $G{\lbrack t\rbrack}$ as the solution of the Lyapunov equation

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Two Point Boundary Value Problem", "weight": 1.0} -->

which has the closed form expression

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Two Point Boundary Value Problem", "weight": 1.0} -->

Under the assumptions $A_{\Sigma}$ (in particular, system is controllable), we have that $G{\lbrack t\rbrack}$ is symmetric positive definite for all $t > 0$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A Two Point Boundary Value Problem", "weight": 1.0} -->

Let $\overline{\mathbf{x}}{\lbrack t\rbrack}$ be the zero input response of system, that is the solution of the differential equation

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A Two Point Boundary Value Problem", "weight": 1.0} -->

which has the closed form expression

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A Two Point Boundary Value Problem", "weight": 1.0} -->

which corresponds to the minimal cost (as a function of travel time $\tau$)

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A Two Point Boundary Value Problem", "weight": 1.0} -->

The optimal connection time $\tau^{\ast}$ may be computed by minimizing over $\tau$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-B Small-Time Characterization of the Spectrum of the Controllability Gramian", "weight": 1.0} -->

We begin by briefly reviewing the concept of *controllability indices*^22^2See \[14, p. 431\] or \[12, p. 150\] for a more detailed treatment. for a controllable system $(A,B)$. Let $\mathbf{b}_{k}$ denote the $k$th column of $B$. Consider searching the columns of the controllability matrix ${\mathcal{C}{\lbrack A,B\rbrack}} = \begin{bmatrix}
\end{bmatrix}$ from left to right for a set of $n$ linearly independent vectors. This process is well-defined for a controllable pair $(A,B)$ since ${\text{rank}\left\lbrack {\mathcal{C}{\lbrack A,B\rbrack}} \right\rbrack} = n$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-B Small-Time Characterization of the Spectrum of the Controllability Gramian", "weight": 1.0} -->

The $\nu_{k}$ give a fundamental notion of how difficult a system is to control in various directions; indeed these indices are a property of the system invariant with respect to similarity transformation, e.g. permuting the columns of $B$. We may also label the vectors of $\mathcal{S}$ as $\mathbf{v}_{1},\ldots,\mathbf{v}_{n}$ in the order that they come up in $\mathcal{C}{\lbrack A,B\rbrack}$. That is, $\mathbf{v}_{i} = {A^{e_{i}}\mathbf{b}_{k_{i}}}$ and $e_{i} \leq e_{j}$ iff $i \leq j$ (note: $e_{n} = {\nu - 1}$).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Probabilistic Exhaustivity", "weight": 1.0} -->

In this section we prove a key result characterizing random sampling schemes for the LQDMP problem: *any* feasible trajectory through the configuration space $\mathcal{M}$ is "traced" arbitrarily well by connecting randomly distributed points from a sufficiently large sample set covering the configuration space. We will refer to this property as probabilistic exhaustivity. The same notion of probabilistic exhaustivity (clearly much stronger than the usual notion of probabilistic completeness) was introduced in the related paper in the context of DMP for *driftless* systems. The result proven in that work does not carry over to the drift case as it relies on the metric inequality to bound the cost of approximate paths; the drift case lacks the control symmetry to make such estimates. Thus in order to prove probabilistic exhaustivity in the case of linear affine systems, we first provide a result analogous to the metric inequality characterizing the effect that perturbations of the endpoints of a path have on its cost and state trajectory. The idea, then, is that tracing waypoints may be selected as small perturbations of points along the trajectory to be approximated, provided the sample density is high enough.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark IV.2 (Bounding Perturbation Ball Volume)", "weight": 1.0} -->

where $\zeta_{n}$ denotes the volume of the unit ball in ${\mathbb{R}}^{n}$. Given our asymptotic characterization of $\det{\lbrack{G{\lbrack\tau\rbrack}}\rbrack}$ in Lemma III.4. ‣ III-B Small-Time Characterization of the Spectrum of the Controllability Gramian ‣ III Optimal Control in the Absence of Obstacles ‣ Optimal Sampling-Based Motion Planning under Differential Constraints: the Drift Case with Linear Affine Dynamics"), there is a threshold $\tau_{\mu} > 0$ and constant $C_{\mu} > 0$ such that

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark IV.2 (Bounding Perturbation Ball Volume)", "weight": 1.0} -->

To ensure that the $\tau^{D/2}$ term above does not become vanishingly small in application with Lemma IV.1. ‣ IV Probabilistic Exhaustivity ‣ Optimal Sampling-Based Motion Planning under Differential Constraints: the Drift Case with Linear Affine Dynamics"), we also lower bound connection time in terms of connection cost.

<!-- chunk {"id": "body-0042", "role": "body", "section": "DFMT^∗^ Algorithm", "weight": 1.0} -->

The algorithm presented here is based on FMT^∗^, from the recent work of, which can be thought of as an accelerated version of PRM^∗^. Briefly, PRM^∗^ first samples all the vertices, then constructs a fully *locally* connected graph, and then performs shortest path search (e.g., Dijkstra's algorithm) on the graph to obtain a solution. FMT^∗^ also samples all vertices first, but instead of a graph, lazily builds a tree *via dynamic programming* that very closely approximates the shortest-path tree for PRM^∗^, but saves a multiplicative factor of $O{\lbrack{\log{(n)}}\rbrack}$ collision-checks by not constructing the full graph. The algorithm given by Algorithm 1, DFMT^∗^, is not fundamentally different from the original FMT^∗^ algorithm, but mainly changes what "local" means under differential constraints (similar to, but now with drift).

<!-- chunk {"id": "body-0043", "role": "body", "section": "DFMT^∗^ Algorithm", "weight": 1.0} -->

One more difference of DFMT^∗^ presented here, even from the algorithm, is that the edges are now directed, reflecting the fundamental asymmetry of differential constraints with drift.

<!-- chunk {"id": "body-0044", "role": "body", "section": "DFMT^∗^ Algorithm", "weight": 1.0} -->

Membership in either reachable set may be checked by minimizing the explicit cost function over travel time. The set of samples to check for membership may be pruned by considering the form of $G{\lbrack t\rbrack}$, as suggested. Let $\text{CollisionFree}{\lbrack\mathbf{x}_{1},\mathbf{x}_{2}\rbrack}$ denote the boolean function which returns true if and only if $\pi^{\ast}{\lbrack\mathbf{x}_{1},\mathbf{x}_{2}\rbrack}$ lies within $\mathcal{M}_{\text{free}}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "DFMT^∗^ Algorithm", "weight": 1.0} -->

Given a directed graph $G = {(V,E)}$, where $V$ is the vertex set and $E$ is the edge set, and a vertex $\mathbf{x} \in V$, let $\text{Cost}{\lbrack\mathbf{x},G\rbrack}$ be the function that returns the cost of the shortest (directed) path in the graph $G$ between the vertices $\mathbf{x}_{\text{init}}$ and $\mathbf{x}$. Let $\text{Path}{\lbrack\mathbf{x},G\rbrack}$ be the function that returns the path achieving that cost. The DFMT^∗^ algorithm is given in Algorithm 1. The algorithm uses two mutually exclusive sets, namely $H$ and $W$. The *unexplored* set $W$ stores all samples in the sample set $V$ that have not yet been considered for addition to the tree of paths.

<!-- chunk {"id": "body-0046", "role": "body", "section": "DFMT^∗^ Algorithm", "weight": 1.0} -->

The *wavefront* set $H$, on the other hand, tracks in sorted order (by cost from the root) only those nodes which have already been added to the tree that are near enough to tree leaves to actually form better connections. A detailed description of the algorithm would parallel the one provided in and is omitted due to space limitations, we refer the interested reader to. An extension of PRM^∗^, which we denote by DPRM^∗^, may also be defined in a straightforward manner as, although we omit the full description here. Briefly, DPRM^∗^ searches the graph of all local collision-free connections that appear in any Near set (as opposed to the tree subgraph constructed by DFMT^∗^) for the least cost trajectory.

<!-- chunk {"id": "body-0047", "role": "body", "section": "DFMT^∗^ Algorithm", "weight": 1.0} -->

2 W ← V ∖ {xinit}; H ← {xinit}; z ← xinit
8 ymin ← arg miny ∈ Ynear{Cost [y, T = (V,E)] + c* [y, x]}
9 if CollisionFree [ymin, x] then
17 return Algorithm Failure
19 z ← arg miny ∈ HCost [y, T = (V,E)]

<!-- chunk {"id": "body-0048", "role": "body", "section": "DFMT^∗^ Algorithm", "weight": 1.0} -->

Algorithm 1 Differential Fast Marching Tree (DFMT∗)

<!-- chunk {"id": "body-0049", "role": "body", "section": "Asymptotic Optimality of DFMT^∗^", "weight": 1.0} -->

In this section, we state the asymptotic optimality of DFMT^∗^, for which the asymptotic optimality of DPRM^∗^ is a corollary. We note that in contrast to the work required to establish probabilistic exhaustivity for this class of differentially constrained systems and cost functions, the argument that DFMT^∗^ recovers paths at least as good as any waypoint-traced trajectory is essentially equivalent to the proofs presented in and. That is, the idea that DFMT^∗^ (or DPRM^∗^) can connect closely spaced sample points at a resolution sufficiently fine that every connection takes place away from the influence of the obstacle set is not a feature specific to the LQDMP problem. Thus we state the following theorem and, in the interest of brevity, refer the reader to the proofs of Theorems VI.1 and VI.2 presented. We note that the following optimality result for DFMT^∗^ also provides a *convergence rate* bound, but to avoid confusion we emphasize that this bound is given in terms of sample size $N$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Asymptotic Optimality of DFMT^∗^", "weight": 1.0} -->

For a discussion of how sample size relates to run time for FMT^∗^-style algorithms see.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The DFMT^∗^ and DPRM^∗^ algorithms were implemented in Julia and run using a Unix operating system with a 2.0 GHz processor and 8 GB of RAM. We tested DFMT^∗^ and DPRM^∗^ on the double integrator system, a standard LQDMP formulation as studied. We also implemented variants of DFMT^∗^ and DPRM^∗^ where the local connection cost is computed with respect to a fixed time $\tau$, instead of optimizing $c^{\ast}{\lbrack\tau\rbrack}$ over all arrival times. This is less computationally intensive than searching for the optimal $\tau^{\ast}$, and can be proven asymptotically optimal as well using a similar probabilistic exhaustivity approach.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The intuition is that for a fixed cost radius, the algorithm is searching over a "donut" -- the band of states in which the fixed $\tau$ is a valid approximation for $\tau^{\ast}$ -- instead of a "ball." Provided the sample count $N$ is sufficiently large, this donut has enough volume to support the desired tracing connections. We denote the optimal-connection algorithms presented in this paper $\tau^{\ast}$ DFMT^∗^ and $\tau^{\ast}$ DPRM^∗^ to differentiate the two approaches. The simulation results are summarized in Figure 1. A maze was used for $\mathcal{M}_{\text{obs}}$, and our algorithm implementations were run 50 times each on sample sizes up to $N = 12000$ for fixed $\tau$ and $N = 6000$ for the $\tau^{\ast}$ variants.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We plot results for both versions of DFMT^∗^ run with and without a cache of near neighbor sets and local connection costs; as discussed in this information, which does not depend on the problem-specific obstacle configuration, may be precomputed for batch-processing algorithms such as DFMT^∗^ and DPRM^∗^ -- the price to pay is a moderate increase in memory requirements. We see that the extra time for optimizing over local connection duration $\tau$ is significant (DFMT^∗^ -- no cache vs. $\tau^{\ast}$ DFMT^∗^ -- no cache), but may be mitigated by precomputation (DFMT^∗^ vs. $\tau^{\ast}$ DFMT^∗^).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Discussion and Conclusions", "weight": 1.5} -->

In this paper we have provided a thorough and rigorous theoretical framework to assess optimality guarantees of sampling-based algorithms for linear affine systems with a mixed time/energy cost function. In particular, we leveraged the study of small-cost perturbations to show that optimum-approximating waypoints may be found among randomly sampled state sets with high probability. We applied this analysis to design and theoretically validate an asymptotically optimal algorithm, DFMT^∗^, for the LQDMP problem.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Discussion and Conclusions", "weight": 1.5} -->

Although this work is nominally limited to linear affine drift systems, it not only provides a good model for many real systems, but is a crucial first step towards modelling nonlinear systems as well. Indeed, since DFMT^∗^ can be applied to a nonlinear system by linearizing the dynamics, an important next step will be to assess the theoretical guarantees of DFMT^∗^ applied to such a linearized approximation. Given suitable smoothness assumptions on the system linearization (sufficiently powerful, but still encompassing a useful class of dynamics), it seems likely that the perturbation analysis and probabilistic exhaustivity may follow identically to that presented in this paper, up to an additional term quantifying the "perturbation on the perturbation." A similar linearization approach has been experimentally validated by Kinodynamic RRT^∗^. We are also note the similarities in analysis evident between the linear affine drift systems studied in this paper and the (possibly non-linear) control-affine driftless systems studied.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Discussion and Conclusions", "weight": 1.5} -->

In particular, the parallel notions of controllable/bracket-generating systems and controllability index/Hausdorff dimension give hope that a unifying theory for non-linear systems with drift may be achieved. There are a number of additional directions open for further research. In particular, we plan to deploy DFMT^∗^ on robotic platforms, specifically helicopters and floating platforms emulating the dynamics of spacecraft. Also, it is of interest to study a bidirectional version of DFMT^∗^. Finally, it is of interest to devise strategies whereby the radius tuning parameter is self regulating, with the objective of making the algorithm parameter-free.
