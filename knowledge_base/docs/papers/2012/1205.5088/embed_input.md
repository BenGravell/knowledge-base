<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Kinodynamic RRT*: Optimal Motion Planning for Systems with Linear Differential Constraints

Topics include Kinodynamic planning, Rapidly-exploring random tree star, Linear systems, Optimal control, Double integrator.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Uses a fixed-final-state-free-final-time controller that exactly and optimally connects any pair of states in RRT*, where cost trades off trajectory duration against control effort. Dynamics are restricted to linear (or linearized) systems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present Kinodynamic RRT*, an incremental sampling-based approach for asymptotically optimal motion planning for robots with linear differential constraints. Our approach extends RRT*, which was introduced for holonomic robots, by using a fixed-final-state-free-final-time controller that exactly and optimally connects any pair of states, where the cost function is expressed as a trade-off between the duration of a trajectory and the expended control effort. Our approach generalizes earlier work on extending RRT* to kinodynamic systems, as it guarantees asymptotic optimality for any system with controllable linear dynamics, in state spaces of any dimension. Our approach can be applied to non-linear dynamics as well by using their first-order Taylor approximations. In addition, we show that for the rich subclass of systems with a nilpotent dynamics matrix, closed-form solutions for optimal trajectories can be derived, which keeps the computational overhead of our algorithm compared to traditional RRT* at a minimum.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We demonstrate the potential of our approach by computing asymptotically optimal trajectories in three challenging motion planning scenarios: (i) a planar robot with a 4-D state space and double integrator dynamics, (ii) an aerial vehicle with a 10-D state space and linearized quadrotor dynamics, and (iii) a car-like robot with a 5-D state space and non-linear dynamics.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Much progress has been made in the area of motion planning in robotics over the past decades, where the basic problem is defined as finding a trajectory for a robot between a start state and a goal state without collisions with obstacles in the environment. The introduction of incremental sampling-based planners, such as probabilistic roadmaps (PRM) and rapidly-exploring random trees (RRT) enabled solving motion planning problems in high-dimensional state spaces in reasonable computation time, even though the problem is known to be PSPACE-hard. PRM and RRT are asymptotically complete, which means that a solution will be found (if one exists) with a probability approaching 1 if one lets the algorithm run long enough. More recently, an extension of RRT called RRT\* was developed that achieves *asymptotic optimality*, which means that an *optimal* solution will be found with a probability approaching 1.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While RRT\* has successfully been applied in practice, a key limitation of RRT\* is that it is applicable only to systems with simple dynamics, as it relies on the ability to connect any pair of states with an optimal trajectory (e.g. holonomic robots, for which straight lines through the state space represent feasible motions). For *kinodynamic* systems, however, straight-line connections between pairs of states are typically not valid trajectories due to the system's *differential constraints*. Finding a feasible trajectory between two states for differentially constrained systems is known as the *two-point boundary value problem*, and is non-trivial to solve in general. Numerical approaches, such as the shooting method, are computationally intensive and their solutions may not satisfy any notion of optimality. Prior works on extending RRT\* for kinodynamic systems have therefore focused on simple specific instances of kinodynamic systems, or have serious limitations as they do not in fact succeed to compute an optimal trajectory between any pair of states (see our discussion in Section II).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present Kinodynamic RRT\*, an extension of RRT\* that overcomes the above limitations by introducing into the algorithm a fixed-final-state-free-final-time controller that exactly and optimally connects any pair of states for any system with controllable linear dynamics in state spaces of arbitrary dimension. Our approach finds asymptotically optimal trajectories in environments with obstacles and bounds on the state and control input, with respect to a cost function that is expressed as a tunable trade-off between the duration of the trajectory and the expended control effort. Moreover, we show that for the rich subclass of systems with a nilpotent dynamics matrix, expressions for optimal connections between pairs of states can be derived in closed-form, and can hence be computed quickly. This means that our algorithm computes asymptotically optimal trajectories for such kinodynamic systems at little additional computational cost compared to RRT\* for holonomic robots. Also, our approach can handle non-linear dynamics by linearizing them about the state that is sampled in each iteration of the algorithm.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We note that while we focus our presentation on extending RRT\* to kinodynamic systems, also the application of PRM and path *smoothing* by iterative shortcutting have thus far been limited to holonomic systems, for these methods too require connecting pairs of states by feasible trajectories. Our approach is equally suited for making PRM and smoothing applicable to robots with differential constraints, and may particularly align well with recent interest in constructing roadmaps containing near-optimal trajectories.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate the potential of our approach by computing asymptotically optimal trajectories in three challenging motion planning scenarios: (i) a planar robot with a 4-D state space and double integrator dynamics, (ii) an aerial vehicle with a 10-D state space and linearized quadrotor dynamics (see Fig. 1), and (iii) a car-like robot with a 5-D state space and non-linear dynamics.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows. We begin by discussing related work in Section II and formally defining the problem we discuss in this paper in Section III. Section IV describes how an optimal trajectory is computed between any pair of states, and Section V describes our adapted RRT\* algorithm. We describe the extension to non-linear dynamics in Section VI, discuss experimental results in Section VII, and conclude in Section VIII.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

A *trajectory* of the robot is defined by a tuple $\pi = {({\mathbf{x}{\lbrack\rbrack}},{\mathbf{u}{\lbrack\rbrack}},\tau)}$, where $\tau$ is the arrival time or duration of the trajectory, $\mathbf{u}:{{\lbrack 0,\tau\rbrack}\rightarrow\mathcal{U}}$ defines the control input along the trajectory, and $\mathbf{x}:{{\lbrack 0,\tau\rbrack}\rightarrow\mathcal{X}}$ are the corresponding states along the trajectory given $\mathbf{x}{\lbrack 0\rbrack}$ with ${\overset{˙}{\mathbf{x}}{\lbrack t\rbrack}} = {{A\mathbf{x}{\lbrack t\rbrack}} + {B\mathbf{u}{\lbrack

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

which penalizes both the duration of the trajectory and the expended control effort, where $R \in {\mathbb{R}}^{m \times m}$ is positive-definite, constant, and given, and weights the cost of the control inputs relative to each other and to the duration of the trajectory.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

Let $\mathcal{X}_{free} \subset \mathcal{X}$ define the *free* state space of the robot, which consists of those states that are within user-defined bounds and are collision-free with respect to obstacles in the environment. Similarly, let $\mathcal{U}_{free} \subset \mathcal{U}$ define the free control input space of the robot, consisting of control inputs that are within bounds placed on them.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Optimally Connecting a Pair of States", "weight": 1.0} -->

A critical component of our approach to solve the problem as defined in Eq. (III) is to be able to compute the optimal trajectory $\pi^{\ast}{\lbrack\mathbf{x}_{0},\mathbf{x}_{1}\rbrack}$ (and its cost $c^{\ast}{\lbrack\mathbf{x}_{0},\mathbf{x}_{1}\rbrack}$) between any two states $\mathbf{x}_{0} \in \mathcal{X}$ and $\mathbf{x}_{1} \in \mathcal{X}$, as defined in Eqs. and. In this section we discuss how to compute these. It is known from what the optimal control policy is in case a *fixed* arrival time $\tau$ is given, as we review in Section IV-A. We extend this analysis to find the optimal free arrival time in Section IV-B and show how to compute the corresponding optimal trajectory in IV-C. We discuss practical implementation in Section IV-D.

<!-- chunk {"id": "body-0015", "role": "body", "section": "IV-A Optimal Control for Fixed Final State and Fixed Final Time", "weight": 1.0} -->

We note that $G{\lbrack t\rbrack}$ is a positive-definite matrix for $t > 0$ if the dynamics system of Eq. is controllable.

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-A Optimal Control for Fixed Final State and Fixed Final Time", "weight": 1.0} -->

which is an *open-loop* control policy. We refer the reader to for details on the derivation of this equation.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-B Finding the Optimal Arrival Time", "weight": 1.0} -->

To find an optimal trajectory $\pi^{\ast}{\lbrack\mathbf{x}_{0},\mathbf{x}_{1}\rbrack}$ between $\mathbf{x}_{0}$ and $\mathbf{x}_{1}$ as defined by Eq., we extend the above analysis to solve the fixed final state, *free* final time optimal control problem, in which we can choose the arrival time $\tau$ freely to minimize the cost function of Eq..

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-B Finding the Optimal Arrival Time", "weight": 1.0} -->

To find the optimal arrival time $\tau^{\ast}$, we proceed as follows. By filling in the control policy of Eq. into the cost function of Eq.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-B Finding the Optimal Arrival Time", "weight": 1.0} -->

The optimal arrival time $\tau^{\ast}$ is found by taking the derivative of $c{\lbrack\tau\rbrack}$ with respect to $\tau$ (which we denote $\overset{˙}{c}{\lbrack\tau\rbrack}$), and solving ${\overset{˙}{c}{\lbrack\tau\rbrack}} = 0$ for $\tau$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-B Finding the Optimal Arrival Time", "weight": 1.0} -->

It should be noted that the function $c{\lbrack\tau\rbrack}$ may have multiple local minima. Also, note that ${c{\lbrack\tau\rbrack}} > \tau$ for all $\tau > 0$, since $G{\lbrack\tau\rbrack}$ is positive-definite (see Fig. 2).

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-C Computing the Optimal Trajectory", "weight": 1.0} -->

such that the optimal control policy (see Eq.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-C Computing the Optimal Trajectory", "weight": 1.0} -->

Filling in this optimal control policy into Eq.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-D Practical Implementation", "weight": 1.0} -->

For the implementation of the above computations in practice, we distinguish the special case in which matrix $A$ is *nilpotent*, in which case we can derive a closed-form solution for the optimal trajectory, from the general case, in which case we can find the optimal trajectory numerically.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-D Practical Implementation", "weight": 1.0} -->

If matrix $A \in {\mathbb{R}}^{n \times n}$ is *nilpotent*, i.e. $A^{n} = 0$, which is not uncommon as we will see in Section VII, $\exp{\lbrack{At}\rbrack}$ has a closed-form expression in the form of an $({n - 1})$-degree matrix polynomial in $t$. As a result, the integrals of Eqs. and can be evaluated exactly to obtain closed-form expressions for $G{\lbrack\tau\rbrack}$ and $\overline{\mathbf{x}}{\lbrack\tau\rbrack}$. Solving ${\overset{˙}{c}{\lbrack\tau\rbrack}} = 0$ for $\tau$ to find the optimal arrival time $\tau^{\ast}$ then amounts to finding the roots of a (high-degree) polynomial in $\tau$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-D Practical Implementation", "weight": 1.0} -->

Various methods exist to find all roots of a polynomial, which gives us the global minimum of $c{\lbrack\tau\rbrack}$ and the corresponding optimal arrival time $\tau^{\ast}$. Subsequently, the nilpotence of $A$ implies that the matrix $\begin{bmatrix}
\end{bmatrix}$ is nilpotent as well, which means that Eq. can be evaluated exactly to obtain a closed form expression for the optimal trajectory (states and control inputs) between any two states $\mathbf{x}_{0}$ and $\mathbf{x}_{1}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-D Practical Implementation", "weight": 1.0} -->

For a general (not nilpotent) matrix $A$, we integrate $\overset{˙}{G}{\lbrack t\rbrack}$ and $\overset{˙}{\overline{\mathbf{x}}}{\lbrack t\rbrack}$ forward in time according to Eqs. and using the 4th-order Runge-Kutta method, which gives us $G{\lbrack\tau\rbrack}$, $\overline{\mathbf{x}}{\lbrack\tau\rbrack}$, and $c{\lbrack\tau\rbrack}$ for increasing $\tau > 0$. We keep track of the minimal cost $c^{\ast} = {c{\lbrack\tau\rbrack}}$ we have seen so far and the corresponding arrival time, as we perform the forward integration for increasing $\tau > 0$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-D Practical Implementation", "weight": 1.0} -->

Since ${c{\lbrack\tau\rbrack}} > \tau$ for all $\tau > 0$, it suffices to terminate the forward integration at $\tau = c^{\ast}$ to guarantee that a global minimum $c^{\ast}$ of $c{\lbrack\tau\rbrack}$, and the corresponding optimal arrival time $\tau^{\ast}$, has been found. This procedure also gives us $\mathbf{d}{\lbrack\tau^{\ast}\rbrack}$, which we use to subsequently reconstruct the optimal trajectory between $\mathbf{x}_{0}$ and $\mathbf{x}_{1}$, by integrating the differential equation backward in time for $\tau^{\ast} > t > 0$ using 4th-order Runge-Kutta.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Kinodynamic RRT\\*", "weight": 1.0} -->

To find the optimal collision-free trajectory $\pi_{free}^{\ast}$ as defined in Eq. (III), given the ability to find an optimal trajectory between any pair of states as described above, we use an adapted version of RRT\*, since RRT\* is known to achieve *asymptotic optimality*; that is, as the number of iterations of the algorithm approaches infinity, the probability that an optimal path has been found approaches 1. The algorithm is given in Fig. 3.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Kinodynamic RRT\\*", "weight": 1.0} -->

The algorithm builds a tree $\mathcal{T}$ of trajectories in the free state space rooted in the start state. In each iteration $i$ of the algorithm, a state $\mathbf{x}_{i}$ is sampled from the free state space $\mathcal{X}_{free}$ (line 3) to become a new node of the tree (line 10). For each new node a parent is found among neighboring nodes already in the tree, i.e. the nodes $\mathbf{x}$ for which ${c^{\ast}{\lbrack\mathbf{x},\mathbf{x}_{i}\rbrack}} < r$ for some neighbor radius $r$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Kinodynamic RRT\\*", "weight": 1.0} -->

The node $\mathbf{x}$ that is chosen as parent is the node for which the optimal trajectory $\pi{\lbrack\mathbf{x},\mathbf{x}_{i}\rbrack}$ to the new node is collision-free (i.e. the states and control inputs along the trajectory are in the respective free spaces) and results in a minimal cost between the root node ($\mathbf{x}_{start}$) and the new node (lines 4-6). Subsequently, it is attempted to decrease the cost from the start to other nodes in the tree by connecting the new node to neighboring nodes in the tree, i.e. the nodes $\mathbf{x}$ for which ${c^{\ast}{\lbrack\mathbf{x}_{i},\mathbf{x}\rbrack}} < r$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Kinodynamic RRT\\*", "weight": 1.0} -->

For each state $\mathbf{x}$ for which the connection is collision-free and results in a lower cost to reach $\mathbf{x}$ from the start, the new node $\mathbf{x}_{i}$ is made the parent of $\mathbf{x}$ (lines 7-9). Then, the algorithm continues with a new iteration. If this is repeated indefinitely, an optimal path between $\mathbf{x}_{start}$ and $\mathbf{x}_{goal}$ will emerge in the tree.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Kinodynamic RRT\\*", "weight": 1.0} -->

KinodynamicRRT*[xstart ∈ 𝒳free, xgoal ∈ 𝒳free]
3: Randomly sample xi ∈ 𝒳free.
4: x ← argmin {x ∈ 𝒯|c*[x, xi] &lt; r∧ CollisionFree[π*[x, xi]]}(cost[x]+c*[x, xi]).
7: for all {x ∈ 𝒯 ∪ {xgoal}|c*[xi, x] &lt; r ∧ cost[xi] + c*[xi, x] &lt; cost[x]∧CollisionFree[π*[xi, x]]} do
Figure 3: The adapted RRT* algorithm. The tree 𝒯 is represented as a set of states. Each state x in the tree has two attributes: a pointer parent [x] to its parent state in the tree, and a number cost [x] which stores the cost of the trajectory in the tree between the start state and x. Further, we define CollisionFree[x, u, τ] = ∀{t ∈ [0, τ]} (x [t]∈𝒳free ∧ u [t]∈𝒰free).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Kinodynamic RRT\\*", "weight": 1.0} -->

The algorithm as given in Fig. 3 differs subtly from the standard RRT\* algorithm. First of all, we have defined our problem as finding a trajectory that exactly arrives at a goal state, rather than a goal region as is common in RRT\*. As a consequence, we explicitly add the goal state to the set of states that is considered for a forward connection from a newly sampled node in line 7, even if the goal is not (yet) part of tree. Also, typical RRT\* implementations include a "steer" module, which lets the tree grow *towards* a sampled state (but not necessarily all the way), and adds the endpoint of a partial trajectory as node to the tree. Since it is non-trivial given our formulation to compute a partial trajectory of a specified maximum cost, our algorithm attempts a full connection to the sampled state, and adds the sampled state itself as a node to the tree. These changes do not affect the asymptotic optimality guarantee of the algorithm.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Kinodynamic RRT\\*", "weight": 1.0} -->

In the original RRT\* algorithm, the neighbor radius $r$ can be decreased over the course of the algorithm as a function $r = {({{{({\gamma/\zeta_{d}})}{\log{\lbrack i\rbrack}}}/i})}^{1/d}$ of the number of nodes $i$ currently in the tree, without affecting the asymptotic optimality guarantee, where $d$ is the dimension of the state space, $\zeta_{d}$ is the volume of a $d$-dimensional unit ball, $\gamma > {2^{d}{({1 + {1/d}})}\mu{\lbrack\mathcal{X}_{free}\rbrack}}$, and $\mu{\lbrack\mathcal{X}_{free}\rbrack}$ is the volume of the state space.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Kinodynamic RRT\\*", "weight": 1.0} -->

Then the neighbor radius $r$ must be set such that a ball of volume ${\gamma{\log{\lbrack i\rbrack}}}/i$ is contained within $\mathcal{R}{\lbrack\mathbf{x},r\rbrack}$. A finite radius $r$ always exists in our case such that this holds, since we require that the system's dynamics are formally controllable.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Systems with Non-Linear Dynamics", "weight": 1.0} -->

We have presented our algorithm for linear dynamics systems of the type of Eq., but we can apply our algorithm to non-linear dynamics as well through linearization.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Systems with Non-Linear Dynamics", "weight": 1.0} -->

We can locally approximate the dynamics by linearizing the function $\mathbf{f}$ to obtain a system of the form of Eq.,:

<!-- chunk {"id": "body-0038", "role": "body", "section": "Systems with Non-Linear Dynamics", "weight": 1.0} -->

where $\hat{\mathbf{x}}$ is the state and $\hat{\mathbf{u}}$ is the control input about which the dynamics are linearized. The resulting linear system is a first-order Taylor approximation of the non-linear dynamics, and is approximately valid only in the vicinity of $\hat{\mathbf{x}}$ and $\hat{\mathbf{u}}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Systems with Non-Linear Dynamics", "weight": 1.0} -->

We adapt the algorithm of Fig. 3 to non-linear dynamics by (re)linearizing $\mathbf{f}$ in each iteration of the algorithm about $\hat{\mathbf{x}} = \mathbf{x}_{i}$ and $\hat{\mathbf{u}} = \mathbf{0}$ after a new state $\mathbf{x}_{i}$ is sampled in line 3. The resulting linear dynamics are then used in the subsequent computations of the functions $c^{\ast}$ and $\pi^{\ast}$ (note that this only works if the linearized dynamics are controllable). We choose $\hat{\mathbf{x}} = \mathbf{x}_{i}$ since it is either the start or the end point of any trajectory computed in that iteration of the algorithm, and we choose $\hat{\mathbf{u}} = \mathbf{0}$ since the cost function (see Eq. ) explicitly penalizes deviations of the control input from zero.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Systems with Non-Linear Dynamics", "weight": 1.0} -->

The linearization is only a valid approximation if the computed trajectories do not venture too much away from the linearization point. As over the course of the algorithm the distances between states get shorter (due to a decreasing neighbor radius $r$) and the trajectories in the tree get more optimal (hence having control inputs closer to zero), this approximation becomes increasingly more reasonable. It can be helpful, though, to let the neighbor radius $r$ not exceed a certain maximum within which the linearizations can be assumed valid.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We experimented with our implementation on three kinodynamic systems; a double integrator disk robot operating in the plane, a quadrotor robot operating in three space, and a non-holonomic car-like robot operating in the plane, which are discussed in detail in Sections VII-A, VII-B, and VII-C, respectively. Simulation results are subsequently analyzed in Section VII-D.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VII-A Linear Double Integrator Model", "weight": 1.0} -->

The double integrator robot is a circular robot capable of moving in any direction by controlling its acceleration.

<!-- chunk {"id": "body-0043", "role": "body", "section": "VII-A Linear Double Integrator Model", "weight": 1.0} -->

$\mathbf{u} = \mathbf{a}$, and $\mathbf{c} = \mathbf{0}$, where $\mathbf{p}$ describes its position in the plane, $\mathbf{v}$ its velocity, and $\mathbf{a}$ its acceleration. Further, we set bounds such that $\mathbf{p} \in {{\lbrack 0,200\rbrack} \times {\lbrack 0,100\rbrack}}$ (m), $\mathbf{v} \in {\lbrack{- 10},10\rbrack}^{2}$ (m/s), and $\mathbf{u} = \mathbf{a} \in {\lbrack{- 10},10\rbrack}^{2}$ (m/s^2^). The control penalty $r$ was set to 0.25 as this permitted the robot to reach velocities near its bounds but not frequently exceed them.

<!-- chunk {"id": "body-0044", "role": "body", "section": "VII-A Linear Double Integrator Model", "weight": 1.0} -->

We experimented with this model in the environment of Fig. 4. Clearly, $A$ is nilpotent as $A^{2} = 0$, so we can use both the closed-form and the numerical method for computing connections between states.

<!-- chunk {"id": "body-0045", "role": "body", "section": "VII-B Linearized Quadrotor Model", "weight": 1.0} -->

The quadrotor helicopter was modeled after the Ascending Technologies' ResearchPilot. Its state $\mathbf{x} = {(\mathbf{p}^{T},\mathbf{v}^{T},\mathbf{r}^{T},\mathbf{w}^{T})}^{T}$ is 12-dimensional, consisting of three-dimensional position $\mathbf{p}$, velocity $\mathbf{v}$, orientation $\mathbf{r}$ (rotation about axis $\mathbf{r}$ by angle $\|\mathbf{r}\|$), and angular velocity $\mathbf{w}$. Its dynamics are non-linear, but are well-linearizable about the hover point of the quadrotor. The linearization is (very) sensitive though to deviations in the yaw. Fortunately, the yaw is a redundant degree of freedom, so in our linearization, we constrain the yaw (and its derivative) to zero.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VII-B Linearized Quadrotor Model", "weight": 1.0} -->

where $\mathbf{r}$ and $\mathbf{w}$ are two-dimensional (with their third component implicitly zero), $g = 9.8$m/s^2^ is the gravity, $m$ is the mass of the quadrotor (kg), $\ell$ the distance between the center of the vehicle and each of the rotors (m), and $j$ is the moment of inertia of the vehicle about the axes coplanar with the rotors (kg m^2^). The control input $\mathbf{u}$ consists of three components: $u_{f}$ is the total thrust of the rotors relative to the thrust needed for hovering, and $u_{x}$ and $u_{y}$ describe the relative thrust of the rotors producing roll and pitch, respectively.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VII-B Linearized Quadrotor Model", "weight": 1.0} -->

The quadrotor simulations were performed in the environment of Fig. 5 for the linearized dynamics. Clearly, $A$ is nilpotent as it is strictly upper diagonal, so we can use both the closed-form and the numerical method for computing connections between states.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VII-C Non-Linear Car-Like Model", "weight": 1.0} -->

The car-like robot has a five-dimensional state $\mathbf{x} = {(x,y,\theta,v,\kappa)}^{T}$, consisting of its planar position $(x,y)$ (m), its orientation $\theta$ (rad), speed $v$ (m/s), and curvature $\kappa$ (m^-1^). The control input $\mathbf{u} = {(u_{v},u_{\kappa})}^{T}$ is two-dimensional and consists of the derivatives of speed and curvature, respectively.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VII-C Non-Linear Car-Like Model", "weight": 1.0} -->

For this system, we repeatedly linearize the dynamics about the last sampled state, as described in Section VI.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VII-C Non-Linear Car-Like Model", "weight": 1.0} -->

and $\mathbf{c} = {{\mathbf{f}{\lbrack\hat{\mathbf{x}},\mathbf{0}\rbrack}} - {A\hat{\mathbf{x}}}}$, where bounds were set such that $p_{x} \in {\lbrack 0,200\rbrack}$, $p_{y} \in {\lbrack 0,100\rbrack}$, $\theta \in {\lbrack{- \pi},\pi\rbrack}$, $v \in {(0,10\rbrack}$, $\kappa \in {\lbrack{- 0.25},0.25\rbrack}$. We note that the velocity must be non-zero, otherwise the resulting linear dynamics are not controllable.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VII-C Non-Linear Car-Like Model", "weight": 1.0} -->

The car-like robot experiments were performed in the environment of Fig. 6, the same environment as the double integrator. Also in this case, the dynamics matrix $A$ is nilpotent for all linearizations, so we can use both the closed-form and the numerical method for computing connections between states.

<!-- chunk {"id": "body-0052", "role": "body", "section": "VII-D Analysis of Results", "weight": 1.0} -->

We used our algorithm to compute asymptotically optimal trajectories for the double integrator, the quadrotor, and the car-like robots. They are shown in Figs. 4, 5, and 6. While the paths found for the double integrator and quadrotor robots appear continuous and smooth, in the case of the car-like robot effects of linearization are clearly visible; the robot appears to skid sideways to some extent, as if drifting through the curves.

<!-- chunk {"id": "body-0053", "role": "body", "section": "VII-D Analysis of Results", "weight": 1.0} -->

Table I shows the time required to expand the first 5,000 nodes for all three systems using both the closed form method and the numerical 4th-order Runge-Kutta (RK4) method for computing connections between states. It is clear that the closed-form method executed much more quickly than the RK4 method in all cases. On average, we see a factor of 45 (!) difference in running time. Using either of the two methods resulted in solutions with comparable costs after expanding the same number of nodes; variations that occurred were a result of numerical errors.

<!-- chunk {"id": "body-0054", "role": "body", "section": "VII-D Analysis of Results", "weight": 1.0} -->

We also see that nodes were less quickly processed for the double integrator than for the car-like robot, despite a lower dimensionality. This is because for the double integrator and quadrotor experiments, we used a neighbor radius of $r = \infty$, while in the case of the non-holonomic car-like robot only connections to states within a tight radius (approximately corresponding to connections within one width of the road) were accepted. This radius was imposed on the car-like system to ensure short connections as the linearization breaks down over large distances, but it also demonstrates the positive effect of using a reduced radius on performance. Processing nodes for the quadrotor experiment appeared most computationally intensive. This is a result of the high-dimension of its state space. The numbers of Table I also highlight the quadratic nature of the algorithm: the total accumulated running time is a quadratic function of the number of nodes that have been added to the tree.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Discussion, Conclusion, and Future Work", "weight": 1.5} -->

We have presented Kinodynamic RRT\*, an incremental sampling-based approach that extends RRT\* for asymptotically optimal motion planning for robots with differential constraints. Our approach achieves asymptotically optimality by using a fixed-final-state-free-final-time optimal control formulation that connects any pair of states exactly and optimally for systems with controllable linear dynamics. We have shown that tor the rich subclass of systems with a nilpotent dynamics matrix, such trajectories can be computed efficiently, making asymptotically optimal planning computationally feasible for kinodynamic systems, even in high-dimensional state spaces. We plan to make the source code of our implementation publicly available for download.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Discussion, Conclusion, and Future Work", "weight": 1.5} -->

For our experiments, we have not fully optimized our implementation, and we believe that running times can be further improved. In particular, extensions suggested in earlier work, such as using an admissible heuristic that can be quickly computed and provides a conservative estimate of the true cost of moving between two states may prune many (relatively costly) attempts to connect pairs of states. Such a heuristic can then also be used in a branch-and-bound technique to prune parts of tree of which one knows it will never contribute to an optimal solution. Further, the constant involved in the rate by which the neighbor radius is allowed to decrease is difficult to estimate for kinodynamic systems, which prompted us to use very conservative radii. Further analysis of the reachable set is needed to establish reasonable estimations. This would potentially also aid in developing a form of efficient neighbor searching for non-Euclidean state spaces (we currently use a brute-force approach), which is still largely an unexplored area.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Discussion, Conclusion, and Future Work", "weight": 1.5} -->

Other areas of potential improvement include studying non-uniform sampling to accelerate the convergence to optimal solutions. One could sample more heavily around the current optimal solution, or use stochastic techniques to infer distributions of samples that are likely to contribute to an optimal trajectory. For a quadrotor helicopter for instance, one can imagine that there is a strong correlation between its velocity and orientation, which should be reflected in the sampling. In addition, we note that, as mentioned in the introduction, the ability to connect any pair of states can be used to perform trajectory smoothing by iterative shortcutting as post-processing step. This may improve the quality of solutions further and provide better estimates of the convergence rate of the algorithm.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Discussion, Conclusion, and Future Work", "weight": 1.5} -->

Lastly, we plan to apply our planner to real-world robots, in particular quadrotors. This would require constructing a stabilizing controller around the computed trajectory, either using traditional techniques such as LQR, or by repeatedly computing reconnections between the current state of the robot and a state on the trajectory.
