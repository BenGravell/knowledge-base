<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Funnel Libraries for Real-Time Robust Feedback Motion Planning

Topics include Convex optimization, Motion planning, Robotics, Aerial robotics, Vehicles, Safety, Robustness, Uncertainty, Real-time systems, Online algorithms, Optimization, Planning, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the problem of generating motion plans for a robot that are guaranteed to succeed despite uncertainty in the environment, parametric model uncertainty, and disturbances. Furthermore, we consider scenarios where these plans must be generated in real-time, because constraints such as obstacles in the environment may not be known until they are perceived (with a noisy sensor) at runtime. Our approach is to pre-compute a library of "funnels" along different maneuvers of the system that the state is guaranteed to remain within (despite bounded disturbances) when the feedback controller corresponding to the maneuver is executed. We leverage powerful computational machinery from convex optimization (sums-of-squares programming in particular) to compute these funnels. The resulting funnel library is then used to sequentially compose motion plans at runtime while ensuring the safety of the robot. A major advantage of the work presented here is that by explicitly taking into account the effect of uncertainty, the robot can evaluate motion plans based on how vulnerable they are to disturbances. We demonstrate and validate our method using extensive hardware experiments on a small fixed-wing airplane avoiding obstacles at high speed (~12 mph), along with thorough simulation experiments of ground vehicle and quadrotor models navigating through cluttered environments.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

To our knowledge, these demonstrations constitute one of the first examples of provably safe and robust control for robotic systems with complex nonlinear dynamics that need to plan in real-time in environments with complex geometric constraints.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Imagine an unmanned aerial vehicle (UAV) flying at high speed through a cluttered environment in the presence of wind gusts, a legged robot traversing rough terrain, or a mobile robot grasping and manipulating previously unlocalized objects in the environment. These applications demand that the robot move through (and in certain cases interact with) its environment with a very high degree of agility while still being in close proximity to obstacles. Such systems today lack guarantees on their safety and can fail dramatically in the face of uncertainty in their environment and dynamics.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The tasks mentioned above are characterized by three main challenges. First, the dynamics of the system are nonlinear, underactuated, and subject to constraints on the input (e.g. torque limits). Second, there is a significant amount of uncertainty in the dynamics of the system due to disturbances and modeling error. Finally, the geometry of the environment that the robot is operating in is unknown until runtime, thus forcing the robot to plan in

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contributions", "weight": 1.0} -->

In this paper, we address these challenges by combining approaches from motion planning, feedback control, and tools from Lyapunov theory and convex optimization in order to perform robust real-time motion planning in the face of uncertainty. In particular, in an offline computation stage, we first design a finite library of open loop trajectories. For each trajectory in this library, we use tools from convex optimization (sums-of-squares (SOS) programming in particular) to design a controller that explicitly attempts to minimize the size of the worst case reachable set of the system given a description of the uncertainty in the dynamics and bounded external disturbances. This control design procedure yields an outer approximation of the reachable set, which can be visualized as a funnel around the trajectory, that the closed-loop system is guaranteed to remain within. A cartoon of such a funnel is shown in Figure [fig:robustness\_b]. Finally, we provide a way of sequentially composingthese robust motion plans at runtime in order to operate in a provably safe manner in previously unseen environments.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contributions", "weight": 1.0} -->

[A plane deviating from its nominal planned trajectory due to a heavy cross-wind.] [The funnel" of possible trajectories.] [The need to account for uncertainty during planning]Not accounting for uncertainty while planning motions can lead to disastrous consequences.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

One of the most important advantages that our approach affords us is the ability to choose between the motion primitives in our library in a way that takes into account the dynamic effects of uncertainty. Imagine a UAV flying through a forest that has to choose between two motion primitives: a highly dynamic roll maneuver that avoids the trees in front of the UAV by a large margin or a maneuver that involves flying straight while avoiding the trees only by a small distance. An approach that neglects the effects of disturbances and uncertainty may prefer the former maneuver since it avoids the trees by a large margin and is therefore safer". However, a more careful consideration of the two maneuvers could lead to a different conclusion: the dynamic roll maneuver is far more susceptible to wind gusts and perturbations to the initial state than the second one. Thus, it may in fact be more robust to execute the second motion primitive. Further, it may be possible that neither maneuver is guaranteed to succeed and it is safer to abort the mission and simply transition to a hover mode. Our approach allows robots to make these critical decisions, which are essential if robots are to move out of labs and operate in real-world environments.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

We demonstrate and validate our approach using thorough simulation experiments of ground vehicle and quadrotor models navigating through cluttered environments, along with extensive hardware experiments on a small fixed-wing airplane avoiding obstacles at high speed ($\sim$12 miles per hour) in an indoor motion capture environment. To the best of our knowledge, the resulting demonstrations constitute one of the first examples of provably safe and robust control for robotic systems with complex nonlinear dynamics that need to plan in real-time in cluttered environments.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Outline", "weight": 1.0} -->

The outline of the paper is as follows. Section [sec:related] discusses prior work; Section [sec:background] provides a brief background on semidefinite and sums-of-squares (SOS) programming, which are used heavily throughout the paper; Section [sec:funnels] shows how to use SOS programming to compute funnels; Section [sec:funnel libraries] introduces the notion of a funnel library; Section [sec:planning] describes our algorithm for using funnel libraries for real-time robust planning in environments that have not been seen by the robot before; Section [sec:examples] presents extensive simulation results on a ground vehicle model and compares our approach with an approach based on trajectory libraries; Section [sec:examples] also considers a quadrotor model and shows how one can use our approach to guarantee collision-free flight in certain environments; Section [sec:hardware] presents hardware experiments on a small fixed-wing airplane in order to demonstrate and validate our approach; Section [sec:conclusion]concludes the paper with a discussion of challenges and open problems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Motion Planning", "weight": 1.0} -->

Motion planning has been the subject of significant research in the last few decades and has enjoyed a large degree of success in recent years. Planning algorithms like the Rapidly-exploring Randomized Tree (RRT) (along with variants that attempt to find optimal motion plans) and related trajectory library approaches can handle large state-space dimensions and complex differential constraints. These algorithms have been successfully demonstrated on a wide variety of hardware platforms. However, an important challenge is their inability to explicitly reason about uncertainty and feedback. Modeling errors, state uncertainty and disturbances can lead to failure if the system deviates from the planned nominal trajectories.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Motion Planning", "weight": 1.0} -->

The motion planning aspect of our approach draws inspiration from the vast body of work that is focused on computing motion primitives in the form of trajectory libraries. For example, trajectory libraries have been used in diverse applications such as humanoid balance control, autonomous ground vehicle navigation, grasping, and UAV navigation. The Maneuver Automaton attempts to capture the formal properties of trajectory libraries as a hybrid automaton, thus providing a unifying theoretical framework. Maneuver Automata have also been used for real-time motion planning with static and dynamic obstacles. Further theoretical investigations have focused on the offline generation of diverse but sparse trajectories that ensure the robot's ability to perform the necessary tasks online in an efficient manner. More recently, tools from sub-modular sequence optimization have been leveraged in the optimization of the sequence and content of trajectories evaluated online. Prior work has also been aimed at learning maneuver libraries in the form of skill trees" from expert demonstrations [konidaris2011robot].

<!-- chunk {"id": "body-0013", "role": "body", "section": "Motion Planning", "weight": 1.0} -->

Robust motion planning has also been a very active area of research in the robotics community. Early work [Lozano-] focused on settings where the dynamics of the system are not dominant and one can treat the system as a kinematic one. The problem is then one of planning paths through configuration space that are robust to uncertainty in the motion of the robot and geometry of the workspace. Our work with funnels takes inspiration from the early work on fine-motion planning, where the notions of funnels and preimage backchaining [Lozano-] (also known as goal regression or sequential composition) were first introduced. The theme of robust kinematic motion planning has persisted in recent work, which deals with uncertainty in the geometry of the environment and obstacles.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Planning under Uncertainty", "weight": 1.0} -->

In settings where the dynamics of the system must be taken into account (e.g., for underactuated systems), the work on planning under uncertainty attempts to address the challenges associated with uncertainty in the dynamics, state, and geometry of the environment. In particular, chance-constrained programming provides an elegant mathematical framework for reasoning about stochastic uncertainty in the dynamics, initial conditions, and obstacle geometry and allows one to generate motion plans with bounds on the probability of collision with obstacles. In settings where the state of the system is partially observable and there is significant uncertainty in the observations, one can extend this framework to plan in the belief space of the system (i.e., the space of distributions over states). While these approaches allow one to explicitly reason about uncertainty in the system, they are typically restricted to handling linear dynamical systems with Gaussian uncertainty. This is due to the computational burden of solving chance constrained problems for nonlinear and non-Gaussian systems.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Planning under Uncertainty", "weight": 1.0} -->

Similarly, other approaches for belief space planning [Agha-] also approximate the belief state as a Gaussian distribution over state space (however, see for an exception to this) for computational efficiency and hence the true belief state is not tracked. Thus, in general, one does not have robustness guarantees. The approach we take in this work is to assume that disturbances/uncertainty are bounded and provide explicit bounds on the reachable set to facilitate safe operation of the nonlinearsystem.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Planning under Uncertainty", "weight": 1.0} -->

More generally, the rich literature on Partially Observable Markov Decision Processes (POMDPs) is also relevant here. POMDPs present an elegant mathematical framework for reasoning about uncertainty in state and dynamics. However, we note that our focus in this work is on dynamical systems with continuous state and action spaces, whereas the POMDP literature typically focuses on discretized state/action spaces for the most part.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Reachable Sets", "weight": 1.0} -->

Reachability analysis for linear and nonlinear control systems has a long history in the controls community. For linear systems subject to bounded disturbances, there exist a number of techniques for efficiently computing (approximations of) backwards and forwards reachable sets. One can apply techniques from linear reachability analysis to conservatively approximate reachable sets of nonlinear systems by treating nonlinearities as bounded disturbances. This idea has been used for performing online safety verification for ground vehicles. A similar idea was used to perform online safety verification for UAVs and to decide when the UAV should switch to an emergency maneuver (a loiter circle"). In this paper we will also compute outer approximations of reachable sets (which we refer to as funnels"). However, the approach we present here is not based on a linearization of the system and thus has the potential to be less conservative for highly nonlinear systems. Further, the scope of our work extends beyond verification; the emphasis here is on safe real-time planningwith funnels.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Reachable Sets", "weight": 1.0} -->

Approximations of reachable sets for nonlinear systems can be computed via Hamilton-Jacobi-Bellman (HJB) differential game formulations This method was used for designing motion primitives for making a quadrotor perform an autonomous backflip in a 2D plane. While this approach handles unsafe sets that the system is not allowed to enter, it is assumed that these sets are specified a priori. In this paper, we are concerned with scenarios in which unsafe sets (such as obstacles) are not specified until runtime and must thus be reasoned about online. Further, techniques for computing reachable sets based on the HJB equation have historically suffered from the curse of dimensionality since they rely on discretizations of the state space of the system. Hence, unless the system under consideration has special structure (e.g., decoupled systems), these methods have difficulty scaling up beyond approximately 5-6 dimensional state spaces.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Reachable Sets", "weight": 1.0} -->

An approach that is closely related to our work is the work presented. The authors propose a randomized planning algorithm in the spirit of RRTs that explicitly reasons about disturbances and uncertainty. Specifications of input to output stability with respect to disturbances provide a parameterization of tubes (analogous to our funnels) that can be composed together to generate motion plans that are collision-free. The factors that distinguish the approach we present in this paper from the one proposed are our focus on the real-time aspect of the problem and use of sums-of-squares programming as a way of computing reachable sets. In, the focus is on generating safe motion plans when the obstacle positions are known a priori. Further, we provide a general technique for computing and explicitly minimizing the size of tubes.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Reachable Sets", "weight": 1.0} -->

Another approach that is closely related to ours is Model Predictive Control with Tubes. The idea is to solve the optimal control problem online with guaranteed tubes" that the trajectories stay. A closely related idea is that of flow-tubes, which have been used for high-level planning for autonomous systems. However, these methods are generally limited to linear systems.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Lyapunov Theory and SOS programming", "weight": 1.0} -->

A critical component of the work presented here is the computation of funnels for nonlinear systems via Lyapunov functions. The metaphor for thinking about Lyapunov functions as defining funnels was introduced to the robotics community, where funnels were sequentially composed in order to produce dynamic behaviors in a robot. However, computational tools for automatically searching for Lyapunov functions were lacking until very recently. In recent years, sums-of-squares (SOS) programming has emerged as a way of checking the Lyapunov function conditions associated with each funnel. The technique relies on the ability to check nonnegativity of multivariate polynomials by expressing them as a sum of squares of polynomials. This can be written as a semidefinite optimization program and is amenable to efficient computational algorithms such as interior point methods. Assuming polynomial dynamics, one can check that a polynomial Lyapunov candidate, $V(x)$, satisfies $V(x) > 0$ and $\dot{V}(x) < 0$ in some region $B_r$. Importantly, the same idea can be used for computing funnels along time-indexed trajectories of a system.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Lyapunov Theory and SOS programming", "weight": 1.0} -->

In this paper, we will use a similar approach to synthesize feedback controllers that explicitly seek to minimize the effect of disturbances on the system by minimizing the size of the funnel computed along a trajectory. Thus, we are guaranteed that if the system starts off in the set of given initial conditions, it will remain in the computed funnel" even if the model of the dynamics is uncertain and the system is subjected to bounded disturbances.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Lyapunov Theory and SOS programming", "weight": 1.0} -->

The ability to compute funnels using SOS programming was leveraged by the LQR-Trees algorithm for feedback motion planningfor nonlinear systems. The algorithm works by creating a tree of locally stabilizing controllers which can take any initial condition in some bounded region in state space to the desired goal. However, LQR-Trees lack the ability to handle scenarios in which the task and environment are unknown till runtime: the offline precomputation of the tree does not take into account potential runtime constraints like obstacles, and an online implementation of the algorithm is computationally infeasible.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Lyapunov Theory and SOS programming", "weight": 1.0} -->

The SOS programming approach has also been used to guarantee obstacle avoidance conditions for nonlinear systems by computing barrier certificates. Barrier functions are similar to Lyapunov functions in spirit, but are used to guarantee that trajectories starting in some given set of initial conditions will never enter an unsafe" region containing obstacles. This approach, however, is limited to settings where the locations and geometry of obstacles are known beforehand since the barrier certificate one computes depends on this data and computing barrier certificates in real-time using SOS programming is not computationally feasible at the present time.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Semidefinite Programming (SDP)", "weight": 1.0} -->

Semidefinite programs (SDPs) form an important class of convex optimization problems. They are optimization problems over the space of symmetric positive semidefinite (psd) matrices. Recall that a $n \times n$ symmetric matrix $Q$ is positive semidefinite if $x^TQx \geq 0, \ \forall x \in \mathbb{R}^n$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Semidefinite Programming (SDP)", "weight": 1.0} -->

Denoting the set of $n \times n$ symmetric matrices as $\mathbf{S}^n$, a SDP in standard form is written as: & & \min_{X \in \mathbf{S}^n} \hspace*{0.5cm} & \langle C, X \rangle && \\& & \text{s.t.} \hspace*{0.5cm} & \langle A_i, X \rangle = b_i \quad \forall i \in \{1,\dots,m\}, && \nonumber \\where $C, A_i \in \mathbf{S}^n$ and $\langle X, Y \rangle:= \textrm{Tr}(X^T Y) = \sum_{i,j} X_{ij} Y_{ij}$. In other words, a SDP involves minimizing a cost function that is linear in the elements of the decision matrix $X$ subject to linear and positive semidefiniteness constraints on $X$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Semidefinite Programming (SDP)", "weight": 1.0} -->

Semidefinite programming includes Linear Programming (LP), Quadratic Programming (QP) and Second-Order Cone Programming (SOCP) as special cases. As in these other cases, SDPs are amenable to efficient numerical solution via interior point methods. The interested reader may wish to consult and for a more thorough introduction to SDPs.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Sums-of-Squares (SOS) Programming", "weight": 1.0} -->

An important application of SDPs is to check nonnegativity of polynomials. The decision problem associated with checking polynomial nonnegativity is NP hard in general. However, the problem of determining whether a polynomial is a sum-of-squares (SOS), which is a sufficient condition for nonnegativity, is amenable to efficient computation. A polynomial $p$ in indeterminates Throughout this paper, the variables $x$ that a polynomial $p(x)$ depend on will be referred to as indeterminates". This is to distinguish these variables from decision variables in our optimization problems, which will typically be the coefficients of the polynomial. $x_1,x_2,\dots,x_n$ is SOS if it can be written as $p(x)=\sum_{i=1}^m q_i^2(x)$ for a set of polynomials $\{q_i\}_{i=1}^m$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Sums-of-Squares (SOS) Programming", "weight": 1.0} -->

This condition is equivalent to the existence of a positive semidefinite (psd) matrix $Q$ that satisfies: where $v(x)$ is the vector of all monomials with degree less than or equal to half the degree of $p$. Note that the equality constraint [eq:sos\_sdp] imposes linear constraints on the elements of the matrix $Q$ that come from matching coefficients of the polynomials on the left and right hand sides. Thus, semidefinite programming can be used to certify that a polynomial is a sum of squares. Indeed, by allowing the coefficients of the polynomial $p$ to be decision variables, we can solve optimization problems over the space of SOS polynomials of some fixed degree. Such optimization problems are referred to as sums-of-squares (SOS) programs. The interested reader is referred to and for a more thorough introduction to SOS programming.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Sums-of-Squares (SOS) Programming", "weight": 1.0} -->

In addition to being able to prove global nonnegativity of polynomials, the SOS programming approach can also be used to demonstrate nonnegativity of polynomials on basic semialgebraic sets (i.e., sets described by a finite number of polynomial inequalities and equalities). Suppose we are given a set $$\mathcal{B} = \{x \in \mathbb{R}^n \ | \ g_{eq,i}(x) = 0, \ g_{ineq,j}(x) \geq 0 \},$$ where $g_{eq,i}$ and $g_{ineq,j}$ are polynomials for $i \in \{1,...,N_{eq}\}, j \in \{1,...,N_{ineq}\}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Sums-of-Squares (SOS) Programming", "weight": 1.0} -->

We are interested in showing that a polynomial $p$ is nonnegative on the set $\mathcal{B}$: $$x \in \mathcal{B} \implies p(x) \geq 0.$$ We can write the following SOS constraints in order to impose [eq:nonnegative\_on\_set]: q(x):= p(x)\overbrace{- \sum_{i=1}^{N_{eq}} L_{eq,i}(x) g_{eq,i}(x) - \sum_{j=1}^{N_{ineq}} L_{ineq,j}(x) g_{ineq,j}(x)}^{r(x)} \ \textrm{is SOS}&, \\L_{ineq,j}(x) \ \textrm{is SOS}&, \forall j \in \{0,...,N_{ineq}\}.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Sums-of-Squares (SOS) Programming", "weight": 1.0} -->

Here, the polynomials $L_{eq,i}$ and $L_{ineq,j}$ are multiplier" polynomials analogous to Lagrange multipliers in constrained optimization. In order to see that [eq:s\_proc\_1] and [eq:s\_proc\_2] are sufficient conditions for [eq:nonnegative\_on\_set], note that when a point $x$ satisfies $g_{eq,i}(x) = 0$ and $g_{ineq,j}(x) \geq 0$ for $i \in \{1,...,N_{eq}\}, j \in \{1,...,N_{ineq}\}$ (i.e., when $x \in \mathcal{B}$) then the term $r(x)$ is non-positive.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Sums-of-Squares (SOS) Programming", "weight": 1.0} -->

Hence, for $q(x)$ to be nonnegative (which must be the case since $q$ is SOS), $p(x)$ must be nonnegative. Thus, we have the desired implication in [eq:nonnegative\_on\_set]. This process for using multipliers to impose nonnegativity constraints on sets is known as the generalized S-procedure and will be used extensively in Section [sec:funnels]for computing funnels.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Computing Funnels", "weight": 1.0} -->

In this section we describe how the tools from Section [sec:background] can be used to compute outer approximations of reachable sets (funnels") around trajectories of a nonlinear system. The approach in Section [sec:funnels\_sos] builds on the work presented in while Sections [sec:funnels\_uncertainty] and [sec:funnels\_controller] are based and respectively. In contrast to this prior work however, we consider the problem of computing outer approximations of forwards reachable sets as opposed to inner approximations of backwards reachable sets. This leads to a few subtle differences in the cost functions of our optimization problems.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Computing Funnels", "weight": 1.0} -->

Consider the following dynamical system: where $x(t) \in \mathbb{R}^n$ is the state of the system at time $t$ and $u(t) \in \mathbb{R}^m$ is the control input. Let $x_0: [0,T] \rightarrow \mathbb{R}^n$ be the nominal trajectory that we would like the system to follow and $u_0:[0,T] \rightarrow \mathbb{R}^m$ be the nominal open-loop control input.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Computing Funnels", "weight": 1.0} -->

Defining new coordinates $\bar{x} = x - x_0(t)$ and $\bar{u} = u - u_0(t)$, we can rewrite the dynamics [eq:nonlinear\_dynamics] in these variables as: $$\dot{\bar{x}} = \dot{x} - \dot{x}_0 = f(x_0(t)+\bar{x}(t),u_0(t)+\bar{u}(t)) - \dot{x}_0.$$ We will first consider the problem of computing funnels for a closed-loop system subject to no uncertainty. To this end, we assume that we are given a feedback controller $\bar{u}_f(t,\bar{x})$ that corrects for deviations around the nominal trajectory (we will consider the problem of designing feedback controllers later in this section).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Computing Funnels", "weight": 1.0} -->

We can then write the closed-loop dynamics of the system as: $$\dot{\bar{x}} = f_{cl}(t,\bar{x}(t)).$$ Given a set of initial conditions $\mathcal{X}_0 \subset \mathbb{R}^n$ with $x_0 \in \mathcal{X}_0$, our goal is to find a tight outer approximation of the set of states the system may evolve to at time $t \in [0,T]$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Computing Funnels", "weight": 1.0} -->

In particular, we are concerned with finding sets $F(t) \subset \mathbb{R}^n$ such that: $$\bar{x} \in \mathcal{X}_0 \implies \bar{x}(t) \in F(t), \ \forall t \in [0,T].$$ A funnel associated with a closed-loop dynamical system $\dot{\bar{x}} = f_{cl}(t,\bar{x}(t))$ is a map $F: [0,T] \rightarrow \mathcal{P}(\mathbb{R}^n)$ from the time-interval $[0,T]$ to the power set (i.e., the set of subsets) of $\mathbb{R}^n$ such that the sets $F(t)$ satisfy the condition [eq:invariance] above.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Computing Funnels", "weight": 1.0} -->

Thus, with each time $t \in [0,T]$, the funnel associates a set $F(t) \subset \mathbb{R}^n$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Computing Funnels", "weight": 1.0} -->

We will parameterize the sets $F(t)$ as sub-level sets of nonnegative time-varying functions $V:[0,T] \times \mathbb{R}^n \rightarrow \mathbb{R}^+$: $$F(t) = \{\bar{x}(t) \in \mathbb{R}^n | V(t,\bar{x}(t)) \leq \rho(t) \}.$$ Letting $\mathcal{X}_0 \subset F(0,\bar{x})$, the following constraint is a sufficient condition for [eq:invariance]: $$V(t,\bar{x}) = \rho(t) \implies \dot{V}(t,\bar{x}) < \dot{\rho}(t), \ \forall t \in [0,T].$$ Here, $\dot{V}$ is computed as: $$\dot{V}(t,\bar{x}) = \frac{\partial

<!-- chunk {"id": "body-0041", "role": "body", "section": "Computing Funnels", "weight": 1.0} -->

V(t,\bar{x})}{\partial \bar{x}}f_{cl}(t,\bar{x}) + \frac{\partial V(t,\bar{x})}{\partial t}.$$ Intuitively, the constraint [eq:Vdot condition] says that on the boundary of the funnel (i.e., when $V(t,\bar{x}) = \rho(t)$), the function $V$ grows slower than $\rho$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Computing Funnels", "weight": 1.0} -->

Hence, states on the boundary of the funnel remain within the funnel. This intuition is formalized. any function that satisfies [eq:Vdot condition] provides us with a valid funnel, we are interested in finding tight outer approximations of the reachable set. A natural cost function for encouraging tightness is the volume of the sets $F(t)$. Combining this cost function with our constraints, we obtain the following optimization problem: & & \underset{V,\rho}{\text{inf}} \hspace*{1cm} & \int_0^T vol(F(t)) \ \textrm{dt} && \\& & \text{s.t.} \hspace*{1cm} & V(t,\bar{x}) = \rho(t) \implies \dot{V}(t,\bar{x}) < \dot{\rho}(t), \ \forall t \in [0,T], \nonumber \\& & & \mathcal{X}_0 \subset F(0,\bar{x}).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Computing Funnels", "weight": 1.0} -->

\nonumber Note that our formulation for computing funnels differs in an important respect from a number of prior approaches on feedback motion planning and sequential composition using funnels. In particular, the formulation presented here considers a given set of initial conditions and attempts to bound the effects of uncertainty going forwards in time. This leads to the volume of funnels being minimized rather than maximized. This is in contrast to, which consider a fixed goal set and seek to maximize the set of initial conditions that are stabilized to this set (which leads to a formulation where the volume of funnels is maximized). The minimization strategy here is better suited to the use of funnels for real-time planning in previously unseen environments since one is interested in bounding the effect of uncertainties on the system in order to prevent collisions with obstacles.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Numerical implementation using SOS programming", "weight": 1.0} -->

Since the optimization problem [eq:funnel\_no\_uncertainty] involves searching over spaces of functions, it is infinite dimensional and hence not directly amenable to numerical computation. However, we can use the SOS programming approach described in Section [sec:background] to obtain finite-dimensional optimization problems in the form of semidefinite programs (SDPs). We first concentrate on implementing the constraints in [eq:funnel\_no\_uncertainty].

<!-- chunk {"id": "body-0045", "role": "body", "section": "Numerical implementation using SOS programming", "weight": 1.0} -->

We will assume that the initial condition set $\mathcal{X}_0$ is a semi-algebraic set (i.e., described in terms of polynomial inequalities): $$\mathcal{X}_0 = \{\bar{x} \in \mathbb{R}^n \ | \ g_{0,i}(\bar{x}) \geq 0, \ \forall i = 1,\dots,N_0\}.$$ Then the constraints in [eq:funnel\_no\_uncertainty] can be written as: V(t,\bar{x}) = \rho(t) \implies \dot{\rho}(t) - \dot{V}(t,\bar{x}) &> 0 \\g_{0,i}(\bar{x}) \geq 0 \ \forall i \in \{1,\dots,N_0\} \implies \rho - V(0,\bar{x}) &\geq 0.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Numerical implementation using SOS programming", "weight": 1.0} -->

If we restrict ourselves to polynomial dynamics and polynomial functions $V$ and $\rho$, these constraints are precisely in the form of [eq:nonnegative\_on\_set] in Section [sec:background\_sos].

<!-- chunk {"id": "body-0047", "role": "body", "section": "Numerical implementation using SOS programming", "weight": 1.0} -->

We can thus apply the procedure described in Section [sec:background\_sos] and arrive at the following sufficient conditions for [eq:funnel\_poly\_1] and [eq:funnel\_poly\_2]: \dot{\rho}(t) - \dot{V}(t,\bar{x}) - L(t,\bar{x}) [V(t,\bar{x}) - \rho(t)] - L_t(t,\bar{x})[t(T-t)] \ \textrm{is SOS}&, \\\rho - V(0,\bar{x}) - \sum_i^{N_0} L_{0,i}(\bar{x}) g_{0,i}(\bar{x}) \ \textrm{is SOS}&, \\L_t(t,\bar{x}), L_{0,i}(\bar{x}) \ \textrm{are SOS}&, \forall i \in

<!-- chunk {"id": "body-0048", "role": "body", "section": "Numerical implementation using SOS programming", "weight": 1.0} -->

As in Section [sec:background\_sos], the polynomials $L, L_t$ and $L_{0,i}$ are multiplier" polynomials whose coefficients are decision variables.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Numerical implementation using SOS programming", "weight": 1.0} -->

Next, we focus on approximating the cost function in [eq:funnel\_no\_uncertainty] using semidefinite programming. This can be achieved by sampling in time and replacing the integral with the finite sum $\sum_{k = 1}^N vol(F(t_k))$. In the special case where the function $V$ is quadratic in $\bar{x}$: $$V(t_k,\bar{x}) = \bar{x}^T S_k \bar{x}, \ S_k \succeq 0,$$ the set $F(t_k)$ is an ellipsoid and we can use semidefinite programming (SDP) to directly minimize the volume by maximizing the determinant of $S_k$ (recall that the volume of the ellipsoid $F(t_k)$ is a monotonically decreasing function of the determinant of $S_k$).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Numerical implementation using SOS programming", "weight": 1.0} -->

Note that while the problem of maximizing the determinant of a psd matrix is not directly a problem of the form [eq:sdp], it can be transformed into such a form [Ben-]. Further note that the fact that our cost function can be handled directly in the SDP framework is in distinction to the approaches for computing inner approximations of backwards reachable sets. This is because the determinant of a psd matrix is a concave function and hence minimizingthe determinant is not a convex problem. Hence, in the previous work, the authors used heuristics for maximizing volume.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Numerical implementation using SOS programming", "weight": 1.0} -->

In the more general case, we can minimize an upper bound on the cost function $\sum_{k = 1}^N vol(F(t_k))$ by introducing ellipsoids $\mathcal{E}(t_k)$: $$\mathcal{E}(t_k) = \{\bar{x} \in \mathbb{R}^n | \bar{x}^T S_k \bar{x} \leq 1, \ S_k \succeq 0\}$$ such that $F(t_k) \subset \mathcal{E}(t_k)$ and minimizing $\sum_{k=1}^N vol(\mathcal{E}(t_k))$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Numerical implementation using SOS programming", "weight": 1.0} -->

The containment constraint can be equivalently expressed as the constraint: $$V(t_k,\bar{x}) \leq \rho(t_k) \implies \bar{x}^T S_k \bar{x} \leq 1,$$ and can thus be imposed using SOS constraints: 1 - \bar{x}^T S_k \bar{x} - L_{\mathcal{E},k}(\bar{x}) [\rho(t_k) - V(t_k,\bar{x})] \ &\textrm{is SOS}, \\L_{\mathcal{E},k}(\bar{x}) \ &\textrm{is SOS}.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Numerical implementation using SOS programming", "weight": 1.0} -->

\nonumber While this optimization problem is finite dimensional, it is non-convex in general since the first constraints are bilinear in the decision variables (e.g., the coefficients of the polynomials $L$ and $V$ are multiplied together in the first constraint). To apply SOS programming, we require the constraints to be linear in the coefficients of the polynomials we are optimizing. However, note that when $V$ and $\rho$ are fixed, the constraints are linear in the other decision variables. Similarly, when the multipliers $L$ and $L_{\mathcal{E},k}$ are fixed, the constraints are linear in the remaining decision variables. Thus, we can efficiently perform this optimization by alternating between the two sets of decision variables $(L, L_t, L_{0,i},S_k,L_{\mathcal{E},k})$ and $(V,\rho,L_t,L_{0,i},S_k)$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Numerical implementation using SOS programming", "weight": 1.0} -->

In each step of the alternation, we can optimize our cost function $\sum_{k=1}^N vol(\mathcal{E}(t_k))$. These alternations are summarized in Algorithm [a:funnel\_computation]. Note that Algorithm a:funnel\_computation requires an initialization for $V$ and $\rho$. We will discuss how to obtain these in Section sec:funnel\_implementation.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Numerical implementation using SOS programming", "weight": 1.0} -->

$cost = \sum_{k=1}^N vol(\mathcal{E}(t_k))$; $\frac{cost_{prev} - cost}{cost_{prev}} < \epsilon$ $cost_{prev} = cost$; It is easy to see that Algorithm [a:funnel\_computation] converges (though not necessarily to an optimal solution). Each iteration of the alternations is guaranteed to achieve a cost function that is at least as good as the previous iteration (since the solution from the previous iteration is a valid one). Hence, the sequence of optimal values in each iteration form a monotonically non-increasing sequence. Combined with the fact that the cost function is bounded below by 0, we conclude that this sequence converges and hence that Algorithm [a:funnel\_computation] terminates.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Approximation via time-sampling", "weight": 1.0} -->

in practice it is often the case that the nominal trajectory $x_0:[0,T] \rightarrow \mathbb{R}^n$ is difficult to approximate with a low degree polynomial in time. This can lead to the constraint [eq:funnel\_no\_uncertainty\_sos\_1] in the problem [eq:funnel\_no\_uncertainty\_sos] having a high degree polynomial dependence on $t$. Thus it is often useful to implement an approximation of the optimization problem [eq:funnel\_no\_uncertainty\_sos] where the condition [eq:funnel\_poly\_1] is checked only at a finite number of sample points $t_k \in [0,T], \ k \in \{1,\dots,N\}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Approximation via time-sampling", "weight": 1.0} -->

We can use a piecewise linear parameterization of $\rho$ and can thus compute: $$\dot{\rho}(t_k) = \frac{\rho(t_{k+1}) - \rho(t_k)}{t_{k+1} - t_k}.$$ Similarly we can parameterize the function $V$ by polynomials $V_k(\bar{x})$ at each time sample and compute: $$\frac{\partial{V(t,\bar{x})}}{\partial{t}} \approx \frac{V_{k+1}(\bar{x}) - V_k(\bar{x})}{t_{k+1} - t_k}.$$ We can then write the following modified version of the problem [eq:funnel\_no\_uncertainty\_sos]: & &

<!-- chunk {"id": "body-0058", "role": "body", "section": "Approximation via time-sampling", "weight": 1.0} -->

\nonumber This program does not have any algebraic dependence on the variable $t$ and can thus provide significant computational gains over [eq:funnel\_no\_uncertainty\_sos]. However, it does not provide an exact funnel certificate. One would hope that with a sufficiently fine sampling in time, one would recover exactness. Partial results in this direction are provided along with numerical examples showing that the loss of accuracy from the sampling approximation can be quite small in practice. [eq:funnel\_no\_uncertainty\_sampling] is again bilinear in the decision variables. It is linear in the two sets of decision variables $(L_k, L_{0,i},S_k,L_{\mathcal{E},k})$ and $(V_k,\rho,L_{0,i},S_k)$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Approximation via time-sampling", "weight": 1.0} -->

Thus, Algorithm [a:funnel\_computation] can be applied directly to [eq:funnel\_no\_uncertainty\_sampling] with the minor modification that $V$ and $\rho$ are replaced by their time-sampled counterparts and the multipliers $(L,L_t)$ are replaced by the multipliers $L_k$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Extensions to the basic algorithm", "weight": 1.0} -->

Next we describe several extensions to the basic framework for computing funnels described in Section [sec:funnels\_sos]. Section [sec:funnels\_uncertainty] discusses the scenario in which the dynamics of the system are subject to bounded disturbances/uncertainty, Section [sec:funnels\_controller] considers the problem of synthesizing feedback controllers that explicitly attempt to minimize the size of the funnel, Section [sec:funnels\_saturations] demonstrates how to handle input saturations, and Section [sec:funnels\_costs]considers a generalization of the cost function.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Uncertainty in the dynamics", "weight": 1.0} -->

Suppose that the dynamics of the system are subject to an uncertainty term $w(t) \in \mathbb{R}^d$ that models external disturbances or parametric model uncertainties. The closed-loop dynamics [eq:dynamics\_cl] can then be modified to capture this uncertainty: $$\dot{\bar{x}} = f_{cl}(t,\bar{x}(t),w(t)).$$ We will assume that the dynamics $f_{cl}$ depend polynomially on $w$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Uncertainty in the dynamics", "weight": 1.0} -->

Given an initial condition set $\mathcal{X}_0 \subset \mathbb{R}^n$ as before, our goal is to find sets $F(t)$ such that $x(t)$ is guaranteed to be in $F(t)$ for any valid disturbance profile: $$\bar{x} \in \mathcal{X}_0 \implies \bar{x}(t) \in F(t), \forall t \in [0,T],\forall w:[0,T] \rightarrow \mathcal{W}.$$ Parameterizing the sets $F(t)$ as sub-level sets of nonnegative time-varying functions $V: [0,T] \times \mathbb{R}^n \rightarrow \mathbb{R}^+$ as before, the following condition is sufficient to ensure [eq:invariance\_disturbance]: $$V(t,\bar{x}) = \rho(t) \implies \dot{V}(t,\bar{x},w) <

<!-- chunk {"id": "body-0063", "role": "body", "section": "Uncertainty in the dynamics", "weight": 1.0} -->

\dot{\rho}(t), \forall t \in [0,T], \forall w(t) \in \mathcal{W},$$ where $\dot{V}$ is computed as: $$\dot{V}(t,\bar{x},w) = \frac{\partial V(t,\bar{x})}{\partial \bar{x}}f_{cl}(t,\bar{x},w) + \frac{\partial V(t,\bar{x})}{\partial t}.$$ This is almost identical to the condition [eq:Vdot condition], with the exception that the function $V$ is required to decrease on the boundary of the funnel for every choice of disturbance.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Uncertainty in the dynamics", "weight": 1.0} -->

Assuming that the set $\mathcal{W}$ is a semi-algebraic set $\mathcal{W} = \{w \in \mathbb{R}^d \ | \ g_{w,j}(w) \geq 0, \forall j = 1,\dots,N_w\}$, the optimization problem [eq:funnel\_no\_uncertainty\_sos] is then easily modified by replacing condition [eq:funnel\_no\_uncertainty\_sos\_1] with the following constraints: \dot{\rho}(t) - \dot{V}(t,\bar{x},w) - L(t,\bar{x},w) [V(t,\bar{x}) - \rho(t)] - L_t(t,\bar{x},w)[t(T-t)] \dots \nonumber \\\dots \ - \sum_{j=1}^{N_w}

<!-- chunk {"id": "body-0065", "role": "body", "section": "Uncertainty in the dynamics", "weight": 1.0} -->

L_{w,j}(t,\bar{x},w)g_{w,j}(w) \ \textrm{is SOS},& \nonumber \\L_{w,j}(t,\bar{x},w) \ \textrm{is SOS}, \forall j = \{1,\dots,N_w\}.& \nonumber These SOS constraints now involve polynomials in the indeterminates $t,\bar{x}$ and $w$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Uncertainty in the dynamics", "weight": 1.0} -->

Since these constraints are linear in the coefficients of the newly introduced multipliers $L_{w,j}$, Algorithm [a:funnel\_computation] can be directly applied to the modified optimization problem by adding $L_{w,j}$ to the list of polynomials to be searched for in both Step 1 and Step 2 of the iterations. Similarly, the time-sampled approximation described in Section [sec:funnels\_time\_sampling] can also be applied to [eq:sos\_constraints\_uncertainty].

<!-- chunk {"id": "body-0067", "role": "body", "section": "Feedback control synthesis", "weight": 1.0} -->

So far we have assumed that we have been provided with a feedback controller that corrects for deviations around the nominal trajectory. We now consider the problem of optimizing the feedback controller in order to minimize the size of the funnel. We will assume that the system is control affine: and parameterize the control policy as a polynomial $\bar{u}_f(t,\bar{x})$. We can thus write the dynamics in the $\bar{x}$ coordinates as: $$\dot{\bar{x}} = f(x_0(t)+\bar{x}(t)) + g(x(t))[u_0(t) + \bar{u}_f(t,\bar{x})] - \dot{x}_0.$$ The feedback controller can then be optimized by adding the coefficients of the polynomial $\bar{u}_f(t,\bar{x})$ to the set of decision variables in the optimization problem [eq:funnel\_no\_uncertainty\_sos] while keeping all the constraints unchanged.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Feedback control synthesis", "weight": 1.0} -->

Note that $\bar{u}_f$ appears in the constraints only through $\dot{V}$, which is now bilinear in the coefficients of $V$ and $\bar{u}_f$ since: $$\dot{V}(t,\bar{x}) = \frac{\partial V(t,\bar{x})}{\partial \bar{x}}\dot{\bar{x}} + \frac{\partial V(t,\bar{x})}{\partial t}.$$ With the (coefficients of) the feedback controller $\bar{u}_f$ as part of the optimization problem, note that the constraints of the problem [eq:funnel\_no\_uncertainty\_sos] are now bilinear in the two sets of decision variables $(L, L_t, L_{0,i},S_k,L_{\mathcal{E},k}, \bar{u}_f)$ and

<!-- chunk {"id": "body-0069", "role": "body", "section": "Feedback control synthesis", "weight": 1.0} -->

Thus, in principle we could use a bilinear alternation scheme similar to the one in Algorithm [a:funnel\_computation] and alternatively optimize these two sets of decision variables. However, in this case we would not be searching for a controller that explicitly seeks to minimize the size of the funnel (since the controller would not be searched for at the same time as $V$ or $\rho$, which define the funnel). To get around this issue, we add another step in each iteration where we optimize our cost function $\sum_{k=1}^N vol(\mathcal{E}(t_k))$ by searching for $(\bar{u}_f,\rho, L_t,L_{0,i},S_k)$ while keeping $(V,L,L_{\mathcal{E},k})$ fixed. This allows us to search for $\bar{u}_f$ and $\rho$ at the same time, which can significantly improve the quality of the controllers and funnels we obtain. These steps are summarized in Algorithm [a:control\_design].

<!-- chunk {"id": "body-0070", "role": "body", "section": "Feedback control synthesis", "weight": 1.0} -->

By a reasoning identical to the one in Remark [rem:convergence] it is easy to see that the sequence of optimal values produced by Algorithm [a:control\_design]converges.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Feedback control synthesis", "weight": 1.0} -->

$\bf{STEP}$ $\bf{3}:$ Minimize $\sum_{k=1}^N vol(\mathcal{E}(t_k))$ by searching for $(V,\rho,L_t,L_{0,i},S_k)$ while fixing $(L,L_{\mathcal{E},k},\bar{u}_f)$. $cost = \sum_{k=1}^N vol(\mathcal{E}(t_k))$; $\frac{cost_{prev} - cost}{cost_{prev}} < \epsilon$ $cost_{prev} = cost$; We note that the approach for taking into account uncertainty described in Section [sec:funnels\_uncertainty] can easily be incorporated into Algorithm [a:control\_design].

<!-- chunk {"id": "body-0072", "role": "body", "section": "Feedback control synthesis", "weight": 1.0} -->

Similarly, by parameterizing the controller $\bar{u}_f$ as polynomials $u_{f,k}(\bar{x})$ at the times $t_k$, we can also apply the time-sampled approximation described in Section [sec:funnels\_time\_sampling].

<!-- chunk {"id": "body-0073", "role": "body", "section": "Actuator saturations", "weight": 1.0} -->

Our approach also allows us to incorporate actuator limits into the verification procedure. Although we examine the single-input case in this section, this framework is easily extended to handle multiple inputs. Let the control input $u(t)$ at time $t$ be mapped through the following control saturation function: $$s(u(t)) = \begin{cases} u_{max} & \mbox{if $u(t) \geq u_{max}$} \\u_{min} & \mbox{if $u(t) \leq u_{min}$} \\Then, in a manner similar to, a piecewise analysis of $\dot{V}(t,\bar{x})$ can be used to check the Lyapunov conditions are satisfied even when the control input saturates.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Actuator saturations", "weight": 1.0} -->

\dot{\rho}(t), where $u_0$ is the open-loop control input and $\bar{u}_f$ is the feedback controller as before.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Actuator saturations", "weight": 1.0} -->

These conditions can be enforced by adding additional multipliers to the optimization program [eq:funnel\_no\_uncertainty\_sos] or its time-sampled counterpart [eq:funnel\_no\_uncertainty\_sampling].

<!-- chunk {"id": "body-0076", "role": "body", "section": "Actuator saturations", "weight": 1.0} -->

Although one can handle multiple inputs via the above method, the number of SOS conditions grows exponentially with the number of inputs ($3^m$ conditions for $\dot{V}$ are needed in general to handle all possible combinations of input saturations). Thus, for systems with a large number of inputs, an alternative formulation was proposed that avoids this exponential growth in the size of the SOS program at the cost of adding conservativeness to the size of the funnel. Given limits on the control vector $u \in \mathbb{R}^m$ of the form $u_{min} < u < u_{max}$, we can ask to satisfy: $$\bar{x} \in F(t) \implies u_{min} < u_0(t) + \bar{u}_f(t,\bar{x}) < u_{max}, \ \forall t \in [0,T].$$ This constraint implies that the applied control input remains within the specified bounds inside the verified funnel (a conservative condition).

<!-- chunk {"id": "body-0077", "role": "body", "section": "Actuator saturations", "weight": 1.0} -->

The number of extra constraints grows linearly with the number of inputs (since we have one new condition for every input), thus leading to smaller optimization problems.

<!-- chunk {"id": "body-0078", "role": "body", "section": "A more general cost function", "weight": 1.0} -->

We end our discussion of extensions to the basic algorithm for computing funnels presented in Section [sec:funnels\_sos] by considering a generalization of the cost function (volume of the funnel) we have used so far. In particular, it is sometimes useful to minimize the volume of the funnel projected onto a subspace of the state space. Suppose this projection map is given by $\pi: \mathbb{R}^n \rightarrow \mathbb{R}^{n_p}$ with a corresponding $n_p \times n$ projection matrix $P$.

<!-- chunk {"id": "body-0079", "role": "body", "section": "A more general cost function", "weight": 1.0} -->

For an ellipsoid $\mathcal{E} = \{\bar{x} \in \mathbb{R}^n \ | \ \bar{x}^T S_k \bar{x} \leq 1\}$, the projected set $\pi(\mathcal{E})$ is also an ellipsoid $\mathcal{E}_p = \{\bar{x} \in \mathbb{R}^{n_p} \ | \ \bar{x}^T S_k^{(p)} \bar{x} \leq 1\}$: Recall that the ability to minimize the volume of the ellipsoid $\mathcal{E}$ using SDP relied on being able to maximize the determinant of $S_k$. In order to minimize the volume of $\mathcal{E}_p$, we would have to maximize det$(S_k^{(p)})$, which is a complicated (i.e. nonlinear) function of $S_k$.

<!-- chunk {"id": "body-0080", "role": "body", "section": "A more general cost function", "weight": 1.0} -->

Hence, in each iteration of Algorithm [a:funnel\_computation] we linearize the function det$(S_k^{(p)})$ with respect to $S_k$ at the solution of $S_k$ from the previous iteration and maximize this linearization instead. The linearization of det($S_k^{(p)}$) with respect to $S_k$ at a nominal value $S_{k,0}$ can be explicitly computed as: where Tr refers to the trace of the matrix.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Implementation details", "weight": 1.0} -->

We end this section on computing funnels by discussing a few important implementation details.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Trajectory generation", "weight": 1.0} -->

An important step that is necessary for the success of our approach to computing funnels is the generation of a dynamically feasible open-loop control input $u_0: [0,T] \mapsto \mathbb{R}^m$ and corresponding nominal trajectory $x_0: [0,T] \mapsto \mathbb{R}^n$. A method that has been shown to work well in practice and scale to high dimensions is the direct collocation trajectory optimization method. While this is the approach we use for the results in Section [sec:examples], other methods like the Rapidly Exploring Randomized Tree (RRT) or its asymptotically optimal version, RRT$^{\star}$ can be used too.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Initializing $V$ and $\\rho$", "weight": 1.0} -->

[a:funnel\_computation] and [a:control\_design] require an initial guess for the functions $V$ and $\rho$. In, the authors use the Lyapunov function candidate associated with a time-varying LQR controller. The control law is obtained by solving a Riccati differential equation: with final value conditions $S(t) = S_f$. Here $A(t)$ and $B(t)$ describe the time-varying linearization of the dynamics about the nominal trajectory $x_0$. The matrices $Q$ and $R$ are positive-definite cost-matrices. The function: $$V_{guess}(t,\bar{x}) = (x-x_0(t))^T S(t) (x - x_0(t)) = \bar{x}^TS(t)\bar{x}$$ is our initial Lyapunov candidate. Setting $\rho$ to a quickly increasing function such as an exponential is typically sufficient to obtain a feasible initialization.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Initializing $V$ and $\\rho$", "weight": 1.0} -->

However, note that since Algorithms a:funnel\_computation and a:control\_design are not guaranteed to converge to globally optimal solutions, their initialization can impact the quality of the resulting solutions. Thus, standard strategies such as multiple (possibly random) initializations can help address issues related to local solutions. Another strategy that can be used when computing libraries of funnels (Section sec:funnel libraries) is to initialize a funnel computation with the solution computed from a neighboring maneuver in the library.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Sequential composition", "weight": 1.0} -->

One can think of funnels computed using the machinery described in Section [sec:funnels] as robust motion primitives (the robustness is to initial conditions and uncertainty in the dynamics). While we could define a funnel library simply as a collection $\mathcal{F}$ of funnels and associated feedback controllers, it will be fruitful to associate some additional structure with $\mathcal{F}$. In particular, it is useful to know how funnels can be sequenced together to form composite robust motion plans. In order to consider this more formally, we will first introduce the notion of sequential composition of funnels. We note that our definition of sequential composition below differs slightly from the one proposed, which considers infinite-horizon control policies in contrast to the finite-horizon funnels we consider here. In this regard, our notion of a funnel (and corresponding notion of sequential composition) is akin to that of conditional invariance considered.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Sequential composition", "weight": 1.0} -->

An ordered pair $(F_1,F_2)$ of funnels $F_1:[0,T_1] \rightarrow \mathcal{P}(\mathbb{R}^n)$ and $F_2:[0,T_2] \rightarrow \mathcal{P}(\mathbb{R}^n)$ is sequentially composable if $F_1(T_1) \subset F_2$.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Sequential composition", "weight": 1.0} -->

In other words, two funnels are sequentially composable if the outlet" of one is contained within the inlet" of the other. A pictorial depiction of this is provided in Figure [fig:funnel\_seq\_comp]. We note that the sequential composition of two such funnels is itself a funnel. [Sequential composition of funnels] The ordered pair of funnels $(F_1,F_2)$ is sequentially composable. The outlet of $F_1$ is contained within the inlet of $F_2$, i.e., $F_1(T_1) \subset F_2$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Exploiting invariances in the dynamics", "weight": 1.0} -->

For our purposes here, it is useful to introduce a slightly generalized notion of sequential composability that will allow us to exploit invariances (continuous symmetries) in the dynamics. In particular, the dynamics of large classes of mechanical systems such as mobile robots are often invariant under certain transformations of the state space. For Lagrangian systems, the notion of cyclic coordinates" captures such invariances. A cyclic coordinate is a (generalized) coordinate of the system that the Lagrangian does not depend. We can then write the dynamics of the system $\dot{x} = f(x(t),u(t))$ as a function of a state vector $x = [x_c, x_{nc}]$ which is partitioned into cyclic coordinates $x_c$ and non-cyclic coordinates $x_{nc}$ in such a way that the dynamics only depend on the non-cyclic coordinates: For example, the dynamics of a quadrotor or fixed-wing airplane (expressed in an appropriate coordinate system) do not depend on the $x-y-z$position of the system or the yaw angle.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Exploiting invariances in the dynamics", "weight": 1.0} -->

Invariance of the dynamics of the system also implies that if a curve $t \mapsto (x(t),u(t))$ is a valid solution to the dynamics $\dot{x} = f(x(t),u(t))$, then so is the transformed solution: where $\Psi_{c}$ is a mapping from the state space to itself that shifts (i.e., translates) the state vector along the cyclic coordinates (and does not transform the non-cyclic coordinates).This allows us to make the following important observation.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Exploiting invariances in the dynamics", "weight": 1.0} -->

Suppose we are given a system whose dynamics are invariant to shifts $\Psi_c$ along cyclic coordinates $x_c$. Let $F:[0,T] \rightarrow \mathcal{P}(\mathbb{R}^n)$ given by $t \mapsto F(t)$ be a funnel associated with this system. Then the transformed funnel given by $t \mapsto \Psi_c(F(t))$ is also a valid funnel. Hence, one can in fact think of invariances in the dynamics giving rise to an infinite family of funnels parameterized by shifts $\Psi_c(F)$ of a funnel $F$ along cyclic coordinates of the system.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Exploiting invariances in the dynamics", "weight": 1.0} -->

Note that here we have implicitly assumed that the feedback controller: $$u_f(t,x) = u_0(t) + \bar{u}_f(t,\bar{x}) = u_0(t) + \bar{u}_f(t,x-x_0(t))$$ associated with the funnel has also been transformed to: In other words, we have shifted the reference trajectory we are tracking by $\Psi_c$. Henceforth, when we refer to transformations of funnels along cyclic coordinates we will implicitly assume that the feedback controller has also been appropriately modified in this manner.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Exploiting invariances in the dynamics", "weight": 1.0} -->

These observations allow us to define a generalized notion of sequential composition that exploits invariances in the dynamics. We will refer to this notion as sequential composition An ordered pair $(F_1,F_2)$ of funnels $F_1:[0,T_1] \rightarrow \mathcal{P}(\mathbb{R}^n)$ and $F_2:[0,T_2] \rightarrow \mathcal{P}(\mathbb{R}^n)$ is sequentially composable modulo invariances (MI) if there exists a shift $\Psi_c$ of the state along cyclic coordinates such that $F_1(T_1) \subset \Psi_c\big{(}F_2\big{)}$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Exploiting invariances in the dynamics", "weight": 1.0} -->

Informally, two funnels $F_1$ and $F_2$ are sequentially composable in this generalized sense if one can shift $F_2$ along the cyclic coordinates of the system and ensure that its inlet contains the outlet of $F_1$ (note that the definition requires the entire inlet of the shifted funnel to contain the outlet of $F_1$, i.e., not just containment in the cyclic coordinates). Figure [fig:funnel\_seq\_comp\_invariance]provides a pictorial depiction of this. [Sequential composition modulo invariances] Sequential composition modulo invariances. The top row of the figure shows two funnels that are not sequentially composable in the sense of Definition [def:seq\_comp]. However, as shown in the bottom row of the figure, they are sequentially composable in the more general sense of Definition [def:seq\_comp\_inv].

<!-- chunk {"id": "body-0094", "role": "body", "section": "Exploiting invariances in the dynamics", "weight": 1.0} -->

By shifting the funnel $F_2$ (whose outline is plotted using dotted lines for reference) in the cyclic coordinate ($x_c$), we can ensure that the outlet of $F_1$ lies in the inlet of this shifted funnel $\Psi_c(F_2)$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Exploiting invariances in the dynamics", "weight": 1.0} -->

One may think of sequential composability MI of funnels as being analogous to the compatibility condition required for sequencing trajectories in the library of a Maneuver Automaton. Let $\pi_{nc}$ denote the projection operator that maps a state $x = [x_c,x_{nc}]$ to the non-cyclic coordinates $x_{nc}$. In order to be able to sequence together two trajectories $x_{1}:[0,T_1] \rightarrow \mathbb{R}^n$ and $x_2:[0,T_2] \rightarrow \mathbb{R}^n$, one requires: Note, however that imposing this compatibility condition on the nominal trajectories associated with two funnels is neither necessary nor sufficient for the funnels being sequentially composable MI. Sequentially composability MI is concerned with the compatibility between funnels themselves and not the underlying nominal trajectories, which distinguishes our notion of compatibility between maneuvers from that of.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Runtime composability", "weight": 1.0} -->

The two notions of sequential composability we have considered so far allow us to produce new funnels from a given set of funnels by stitching them together appropriately in an offline preprocessing stage. We now introduce another notion of composability that is particularly important for reasoning about how funnels can be executed sequentially at runtime. We will refer to this notion as An ordered pair $(F_1,F_2)$ of funnels $F_1:[0,T_1] \rightarrow \mathcal{P}(\mathbb{R}^n)$ and $F_2:[0,T_2] \rightarrow \mathcal{P}(\mathbb{R}^n)$ is runtime composable if for all $x_{out} \in F_1(T_1)$, there exists a shift $\Psi_c$ of the state along cyclic coordinates such that $x_{out} \in \Psi_c\big{(}F_2\big{)}$.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Runtime composability", "weight": 1.0} -->

In other words, for any state $x_{out}$ in the outlet of $F_1$, one can shift $F_2$ along cyclic coordinates and ensure that its inlet contains $x_{out}$. Hence, we can guarantee that it will be possible to execute the funnel $F_2$ (after appropriate shifting in the cyclic coordinates) once the funnel $F_1$ has been executed (though the particular shift $\Psi_c$ required depends on $x_{out}$and thus will not be known until runtime). Hence, runtime composability of funnels allows us to exploit invariances in the dynamics of the system at runtime and effectively reuse our robust motion plans in different scenarios. As a simple example, a UAV flying through a cluttered environment can reuse a funnel computed for a certain starting position by shifting the funnel so its inlet contains the UAV's current state.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Runtime composability", "weight": 1.0} -->

It is easy to see from Definition [def:runtime composability] that two funnels $F_1$ and $F_2$ are runtime composable if and only if: & \forall x_{out} = [x_c,x_{nc}] \in F_1(T_1), \ \exists x_{0,c} \ s.t. \ [x_{0,c}, x_{nc}] \in F_2.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Runtime composability", "weight": 1.0} -->

This condition is simply stating that we can shift the point $x_{out}$ along cyclic coordinates in such a way that it is contained in the inlet of $F_2$. This condition in turn is equivalent to: where as before $\pi_{nc}$ denotes the projection onto the non-cyclic coordinates of the state space.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Runtime composability", "weight": 1.0} -->

We end our discussion on composability of funnels by noting the following relationship between the three notions of sequential composability we have discussed.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Runtime composability", "weight": 1.0} -->

The three notions of sequential composability we have discussed are related as follows: $$\textrm{Sequential composability} \implies \textrm{Sequential composability MI} \implies \textrm{Runtime composability}.\nonumber$$ The first implication is immediate from Definitions [def:seq\_comp] and [def:seq\_comp\_inv]. The second implication follows from the following reasoning: & F_1(T_1) \subset \Psi_c\big{(}F_2\big{)} \ &\textrm{(Sequential composability MI, ref. Definition def:seq_comp_inv)} \nonumber \\& \implies \pi_{nc} (F_1(T_1)) \subset \pi_{nc} \big{(}\Psi_c(F_2)\big{)} = \pi_{nc} (F_2) \ &\textrm{(Runtime composability, ref. Remark rem:runtime_comp_condition)}.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Checking composability", "weight": 1.0} -->

Given two funnels $F_1:[0,T_1] \rightarrow \mathcal{P}(\mathbb{R}^n)$ and $F_2:[0,T_2] \rightarrow \mathcal{P}(\mathbb{R}^n)$ defined as $F_1(t) = \{\bar{x} \in \mathbb{R}^n \ | \ V_1(t,\bar{x}) \leq \rho_1(t) \}$ and $F_2(t) = \{\bar{x} \in \mathbb{R}^n \ | \ V_2(t,\bar{x}) \leq \rho_2(t) \}$ for polynomials $V_1$ and $V_2$, this section describes how we can check sequential composability, sequential composability MI and runtime composability in an offline preprocessing stage.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Sequential composability", "weight": 1.0} -->

$(F_1,F_2)$ is equivalent to the following condition: $$V_1(T_1,\bar{x}) \leq \rho_1(T_1) \implies V_2(0,\bar{x}) \leq \rho_2.$$ We can thus apply the generalized S-procedure (described in Section [sec:background\_sos]) and check sequential composability using the following simple SOS program: & & \text{Find} \hspace*{1cm} & L(\bar{x}) & \\& & \text{s.t.} \hspace*{1cm} & \rho_2 - V_2(0,\bar{x}) - L(\bar{x}) (\rho_1(T_1) - V_1(T_1,\bar{x})) \ \textrm{is SOS}, & \nonumber \\& & & L(\bar{x}) \ \textrm{is SOS}. & \nonumber

<!-- chunk {"id": "body-0104", "role": "body", "section": "Sequential composition MI", "weight": 1.0} -->

In order to check sequential composability MI, we need to search for a shift $\Psi_c$ along cyclic coordinates of the state such that $F_1(T_1) \subset \Psi_c(F_2)$. For the important special case in which the sets $F_1(T_1)$ and $F_2$ are ellipsoids (corresponding to $V_1(T_1,\bar{x})$ and $V_2(0,\bar{x})$ being quadratic Note that the restriction to quadratic $V_1(T_1,\bar{x})$ and $V_2(0,\bar{x})$ is a relatively mild one. We are not imposing any conditions on the degree of $V_1$ and $V_2$ at times other than the endpoints. in $\bar{x}$), we can cast this search as a semidefinite program (SDP).

<!-- chunk {"id": "body-0105", "role": "body", "section": "Sequential composition MI", "weight": 1.0} -->

Suppose the sets $F_1(T_1)$ and $F_2$ are given: F_2 &= \{x \in \mathbb{R}^n \ | \ (x-x_2)^T S_2 (x-x_2) \leq 1\}, where $x_1:[0,T_1] \rightarrow \mathbb{R}^n$ and $x_2:[0,T_2] \rightarrow \mathbb{R}^n$ are the nominal trajectories around which the funnels were computed and $S_1$ and $S_2$ are positive definite matrices.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Sequential composition MI", "weight": 1.0} -->

We would like to search for a shift $\Delta_c \in \mathbb{R}^n$ (where the components of $\Delta_c$ corresponding to the non-cyclic coordinates are set to zero) such that the ellipsoid: $$\Psi_c(F_2) = \{x \in \mathbb{R}^n \ | \ [x-(x_2+\Delta_c)]^T S_2 [x-(x_2+\Delta_c)] \leq 1\}$$ is contained within the ellipsoid $F_1(T_1)$. The first step in obtaining the desired SDP is to note that the set $\Psi_c(F_2)$ can be represented equivalently as the image of the unit ball under an affine map: $$\Psi_c(F_2) = \{Bu + x_2+\Delta_c \ | \ \|u\|_2 \leq 1 \},$$ where $B = \textrm{chol}(S_2))^{-1}$.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Sequential composition MI", "weight": 1.0} -->

Here, $\textrm{chol}(S_2)$ is the Cholesky factorization of $S_2$ (guaranteed to exist and be invertible since $S_2$ is positive definite). Such a representation is a standard trick in semidefinite programming (see for example).

<!-- chunk {"id": "body-0108", "role": "body", "section": "Sequential composition MI", "weight": 1.0} -->

Introducing the notation the condition that the ellipsoid $F_1(T_1)$ is a subset of the ellipsoid $\Psi_c(F_2)$ is then equivalent to being able to find a scalar $\lambda > 0$ such that the following matrix semidefiniteness constraint holds: $$\left[\begin{array}{ccc} -\lambda-c+b^TS_1^{-1}b & 0_{1\times n} & (x_2+\Delta_c+S_1^{-1}b)^T \\0_{n \times 1} & \lambda I_{n \times n} & B \\\end{array} \right] \succeq 0.$$ Here, the matrices $I$ and $0$ represent the identity matrix and the all-zeros matrix respectively.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Sequential composition MI", "weight": 1.0} -->

Since this semidefiniteness condition is linear in $\lambda$ and $\Delta_c$, the problem of searching for these decision variables subject to $\lambda > 0$ and [eq:seq\_comp\_inv\_sdp] is a SDP. This SDP will be feasible if and only if $F_1$ and $F_2$are sequentially composable MI.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Sequential composition MI", "weight": 1.0} -->

The problem of checking sequential composability MI in the more general non-ellipsoidal case is not directly amenable to such a SDP based formulation. However, if we fix $\Psi_c$, then the problem of checking sequential composability MI reduces to the problem of checking sequential composability. Thus, we can use the SOS program [eq:seq\_comp\_sos] to verify if a given $\Psi_c$ yields the desired containment constraint $F_1(T_1) \subset \Psi_c(F_2)$. One natural choice is to set $\Psi_c$ such that $\pi_c(\Psi_c(x_2)) = \pi_c(x_1(T_1))$, where $\pi_c$ is the projection of the state onto the cyclic coordinates. Intuitively, this corresponds to shifting the funnel $F_2$ so that the start of its nominal trajectory is lined up along cyclic coordinates with the end of the nominal trajectory of $F_1$.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Sequential composition MI", "weight": 1.0} -->

If the SOS program is infeasible, a local search around this $\Psi_c$could yield the desired shift.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Runtime composability", "weight": 1.0} -->

In order to check runtime composability of $F_1$ and $F_2$, we need to check the inclusion $\pi_{nc} (F_1(T_1)) \subset \pi_{nc} (F_2)$. For the important special case where the sets $F_1(T_1)$ and $F_2$ are ellipsoids, we can compute the projections exactly. This is because the projection of an ellipsoid onto a linear subspace is also an ellipsoid (see equation [eq:ellipsoid projection] for the exact formula for the projected ellipsoid). Checking if a given ellipsoid contains another is a straightforward application of semidefinite programming.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Runtime composability", "weight": 1.0} -->

For the more general case, one might hope for a SOS programming based condition for checking $\pi_{nc} (F_1(T_1)) \subset \pi_{nc} (F_2)$. However, the existential quantifier inherent in the projection (see the equivalent condition [eq:runtime\_comp\_condition\_1]) makes it challenging to formulate such SOS conditions. Nevertheless, there exist general purpose tools such as quantifier elimination for checking quantified polynomial formulas such as [eq:runtime\_comp\_condition\_1]. While the worst-case complexity of doing general purpose quantifier elimination is poor, software packages such as QEPCAD (or dReal, which is based on a different theoretical framework) can often work well in practice for specialized problems. We note however that in the examples considered in Sections [sec:examples] and [sec:hardware]we will only be using funnels with ellipsoidal inlets and outlets and thus will not be concerned with this complexity.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Funnel library", "weight": 1.0} -->

A simple but useful generalization of the notions of composability introduced above can be obtained by checking the associated containment conditions at a given time $\tau_1$ rather than at time $T_1$. For example, we will say that the ordered pair of funnels $(F_1,F_2)$ is sequentially composable at time $\tau_1$ if $F_1(\tau_1) \subset F_2$. We will use similar terminology for the other notions of composability. Given a collection $\mathcal{F}$ of funnels associated with a dynamical system, we will associate a directed graph $\mathcal{G}(\mathcal{F})$ whose vertices correspond to funnels $F \in \mathcal{F}$. Two vertices corresponding to funnels $F_i$ and $F_j$ are connected by a directed edge $(F_i,F_j)$ if and only if the ordered pair $(F_i,F_j)$ is runtime composable at some specified time $\tau_i$.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Funnel library", "weight": 1.0} -->

We will sometimes refer to $\tau_i$ as the execution time of funnel $F_i$.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Funnel library", "weight": 1.0} -->

We now introduce the primary data structure that will be used for robust real-time planning (Section A funnel library FL associated with a given dynamical system is a tuple FL = $(\mathcal{F}, \mathcal{G}(\mathcal{F}), \mathcal{C}, \{\tau_i\})$, where $\mathcal{F}$ is a set of funnels for the dynamical system, $\mathcal{G}(\mathcal{F})$ is the directed graph representing which funnels are runtime composable, $\mathcal{C}$ is the set of feedback controllers associated with the funnels in $\mathcal{F}$, and $ \{\tau_i\}$ is the set of execution times.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Funnel library", "weight": 1.0} -->

We note that while the definition of funnel libraries only makes explicit reference to runtime composability of funnels, we are implicitly exploiting the notion of sequential composability (MI) since each funnel in $\mathcal{F}$ may be constructed from simpler funnels that have been sequentially composed. It is also important to note that while we do not impose restrictions such as connectedness or strong connectedness on the graph $\mathcal{G}(\mathcal{F})$, it may be useful to impose such conditions based on the task at hand. For example, for tasks which require continuous operation (such as a UAV navigating indefinitely through a forest or a factory arm continuously placing objects onto a conveyor belt), we should require that $\mathcal{G}(\mathcal{F})$ be strongly connected (since if $\mathcal{G}(\mathcal{F})$ is not strongly connected, we are ruling out the possibility of executing certain funnels in the future). On a similar note, properties of the graph such as its diameter or girth may be related to the efficiency with which a certain task can be accomplished.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Funnel library", "weight": 1.0} -->

Identifying which graph theoretic properties should be imposed on $\mathcal{G}(\mathcal{F})$for different tasks is an interesting research avenue, but we do not pursue this in the present work.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Real-time Planning with Funnels", "weight": 1.0} -->

Given a funnel library FL = $(\mathcal{F}, \mathcal{G}(\mathcal{F}), \mathcal{C}, \{\tau_i\})$computed offline, we can proceed to use it for robust real-time planning in previously unseen environments. The robot's task specification may be in terms of a goal region that must be reached (as in the case of a manipulator arm grasping an object), or in terms of a nominal direction the robot should move in while avoiding obstacles (as in the case of a UAV flying through a forest or a legged robot walking over rough terrain). For the sake of concreteness, we adopt the latter task specification although one can adapt the contents of this section to the former specification. We further assume that the robot is provided with regions in the configuration space that obstacles are guaranteed to lie in and that the robot's sensors only provide this information up to a finite spatial horizon around the robot. Our task is to choose funnels from our library in a way that avoids obstacles while moving forward in the nominal direction.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Real-time Planning with Funnels", "weight": 1.0} -->

The key step in our real-time planning approach is the selection of a funnel from the funnel library that doesn't intersect any obstacles in the environment. This selection process is sketched in the ReplanFunnel algorithm (Algorithm [a:replan\_funnel]). Given the current state $x$ of the robot and the locations and geometry of obstacles $\mathcal{O}$ in the environment, the algorithm searches through the funnels in the library that are runtime composable with the previous funnel that was executed. We assume that for any given funnel, the set of funnels in the library that are runtime composable with it (easily computed given the graph $\mathcal{G}(\mathcal{F})$) is (totally) ordered in a preference list. This ordering may be prespecified offline or generated online based on the current state of the robot. For example, this ordering can be based on aggressiveness of the maneuvers for a UAV (less aggressive maneuvers are given preference) or likely progress towards the goal.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Real-time Planning with Funnels", "weight": 1.0} -->

For each funnel $F_i$, the algorithm tries to find a shift $\Psi_c$ along cyclic coordinates of the system such that the shifted funnel $\Psi_c(F_i)$ satisfies two properties: (i) the current state $x$ is contained in the inlet of the shifted funnel, (ii) the projection of the shifted funnel onto the coordinates of the state space corresponding to the configuration space Note that these projections can be computed in the offline computation stage. doesn't intersect any obstacles in $\mathcal{O}$. If we are able to find such a shift, we are guaranteedthat the system will remain collision-free when the funnel is executed despite the uncertainties and disturbances that the system is subjected to.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Real-time Planning with Funnels", "weight": 1.0} -->

The simplest way to try to choose $\Psi_c$ is to set it such that the nominal trajectory $x_i$ associated with the funnel lines up with the current state in the cyclic coordinates (i.e., using the notation of Section [sec:funnel libraries], $\pi_c(\Psi_c(x_i)) = \pi_c(x)$). Intuitively, this corresponds to shifting the funnel so that it is executed from the current location of the robot. We can then use standard collision-checking libraries such as the Bullet Collision Detection & Physics Library to check if $\Psi_c(F_i)$ (projected onto the configuration space) intersects any obstacles. We will discuss more sophisticated ways of finding $\Psi_c$ in Section [sec:shifting funnels].

<!-- chunk {"id": "body-0123", "role": "body", "section": "Real-time Planning with Funnels", "weight": 1.0} -->

If the search for a collision-free funnel in Algorithm [a:replan\_funnel] doesn't succeed, we assume the existence of a failsafe maneuver ($F_{\textrm{failsafe}}$ in Algorithm a:replan\_funnel) that can be executed in order to keep the robot safe (we assume that the failsafe is verified to be executable from any state the robot may find itself in when replanning). For a ground vehicle, this could entail coming to a stop while for a quadrotor or fixed-wing airplane this may involve transitioning to a hover or propellor-hang mode. In certain cases, it is possible to derive geometric conditions on the environment that the robot will operate in (e.g., constraints on obstacle size and gaps between obstacles) that guarantee that a collision-free funnel will always be found by Algorithm [a:replan\_funnel] if the environment satisfies these conditions. We will see an example of this in Section [sec:quadrotor] for a quadrotor system navigating through a forest of polytopic obstacles.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Real-time Planning with Funnels", "weight": 1.0} -->

Inputs: $x$ (current state of system), $\mathcal{O}$ (reported obstacles in environment), previousFunnel (previous funnel that was executed) $i=1,\dots,\#(\mathcal{F})$ such that $($previousFunnel$, F_i) \in \mathcal{G}(\mathcal{F})$ success $\Leftarrow$ Find a shift $\Psi_c$ along cyclic coordinates such that $x$ is contained in the inlet of $\Psi_c(F_i)$ and $\Psi_c(F_i)$ is collision-free w.r.t. $\mathcal{O}$ [a:online\_planning] provides a sketch of the real-time planning and control loop, which applies the ReplanFunnel algorithm in a receding-horizon manner. At every control cycle, the robot's sensors provide it with a state estimate and report the locations and geometry of the set of obstacles $\mathcal{O}$ in the sensor horizon.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Real-time Planning with Funnels", "weight": 1.0} -->

The algorithm triggers a replanning of funnels if any of the following three criteria are met: (i) if the system has executed the current funnel $F_i$ for the associated execution time $\tau_i$, (ii) if the current state of the system is no longer in the funnel being executed, or (iii) if the current funnel being executed is no longer collision-free. In principle, (ii) should not happen. However, in practice this can happen if the system received a disturbance that was larger than the ones taken into account for the funnel computations. Option (iii) can happen if the robot's sensors report new obstacles that were previously unseen.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Real-time Planning with Funnels", "weight": 1.0} -->

Real-time planning loop $x \Leftarrow$ Initialize current state of the robot $\mathcal{O} \Leftarrow$ Initialize obstacles in sensor horizon $F_i \in \mathcal{F} \Leftarrow$ Initialize current planned funnel $x \Leftarrow$ Update current state of robot $\mathcal{O} \Leftarrow$ Update obstacles in sensor horizon replan $\Leftarrow$ Check if we have finished executing current funnel $F_i$ for the associated execution time $\tau_i$ insideFunnel $\Leftarrow$ Check if current state is still inside the current funnel $F_i$ being executed collisionFree $\Leftarrow$ Check if current funnel $F_i$ is still collision-free with $\mathcal{O}$ replan $\neg$insideFunnel $\neg$collisionFree $F_i \Leftarrow$ ReplanFunnels($x, \mathcal{O}$, $F_i$) apply feedback control input $u$ associated with current funnel $F_i$

<!-- chunk {"id": "body-0127", "role": "body", "section": "Shifting funnels at runtime", "weight": 1.0} -->

The main step in Algorithm [a:replan\_funnel] is the search for a shift $\Psi_c$ along cyclic coordinates such that the shifted funnel $\Psi_c(F_i)$ will be collision-free with respect to the obstacles in $\mathcal{O}$ while containing the current state $x$in its inlet: & & \text{Find} \hspace*{1cm} & \Psi_c & \\& & \text{s.t.} \hspace*{1cm} & x \in \Psi_c(F_i), & \\& & & \pi_{conf}(\Psi_c(F_i)) \cap \mathcal{O} = \O. & \nonumber Here, $\pi_{conf}$ is the projection onto the configuration space variables of the state space. This optimization problem is non-convex in general since the free-space of the environment is non-convex. However, the number of decision variables is very small.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Shifting funnels at runtime", "weight": 1.0} -->

In particular, if we parameterize the shift $\Psi_c$ by a vector $\Delta_c \in \mathbb{R}^n$ (where the coordinates of $\Delta_c$ corresponding to the non-cyclic coordinates are set to zero) such that $\Psi_c(x) = x + \Delta_c$, the number of decision variables is equal to the number of cyclic coordinates of the system.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Shifting funnels at runtime", "weight": 1.0} -->

We can thus apply general-purpose nonlinear optimization tools such as gradient-based methods to solve this problem. In particular, the first constraint is equivalent to checking that the value of the Lyapunov function $V(0,\bar{x}) = V(0,x - (x_i + \Delta_c))$ at time 0 is less than or equal to $\rho$ (recall that the funnel is described as the $\rho(t)$ sub-level set of the function $V(t,\bar{x})$). As in Section [sec:funnels], $x_i$ here is the nominal trajectory corresponding to the funnel $F_i$. The second constraint can be evaluated using off-the-shelf collision-checking libraries. [Shifting funnels out of collision by exploiting invariances in dynamics] The two red regions are obstacles. The shaded green region represents the set in which the funnel segment must be entirely contained in order to satisfy the linear constraints given by the collision normals and collision distances.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Shifting funnels at runtime", "weight": 1.0} -->

Despite the small number of decision variables, for some applications general-purpose nonlinear optimization may be too slow to run in real-time. For the important special case where the cyclic coordinates form a subset of the configuration space variables (e.g., for a UAV), we propose another approach that allows us to search over a restricted family of shifts $\Psi_c$ but has the advantage of being posed using convex quadratic constraints. The first observation is that the containment constraint [eq:containment constraint] is a convex quadratic constraint for the case where the inlet of the funnel is an ellipsoid (i.e., the function $V(0,\bar{x})$is a positive definite quadratic). If the inlet is not an ellipsoid, we can find an ellipsoidal inner approximation by solving a simple SOS program offline.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Shifting funnels at runtime", "weight": 1.0} -->

Next, we seek to find a set of convex constraints that will guarantee non-collision of the funnel. We will assume that $\pi_{conf}(F_i)$ is represented as a union of convex segments $\mathcal{S}_k$ and that the obstacles in the environment are also convex (we assume that non-convex obstacles have been decomposed into convex segments). For each funnel segment, we can find collision normals $n_{jk}$ and collision distances $d_{jk}$ to each obstacle $o_j \in \mathcal{O}$ (these are easily extracted from a collision-checking software). Figure [fig:qcqp shifting] provides an illustration of this for a single convex segment $\mathcal{S}_1$. The two regions colored in red are obstacles. The collision normals are $n_{11}$ and $n_{21}$.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Shifting funnels at runtime", "weight": 1.0} -->

By definition, collision normals provide us with constraints such that any shift $\Delta_c$ of the segment $\mathcal{S}_1$ satisfying the linear constraint $n_{jk}^T \Delta_c < d_{jk}$will be collision-free. The region corresponding to this is shaded in green in the figure.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Shifting funnels at runtime", "weight": 1.0} -->

The constraints described above (containment of the current state in an ellipsoid and the linear constraints given by the collision normals) form a special case of convex Quadratically Constrained Quadratic Programs (QCQPs), for which there exist very mature software packages. For our examples in Section [sec:examples], we use the FORCES Pro package. The package generates solver code tailored to the specific optimization problem at hand and is faster in our experience than using general-purpose convex QCQP solvers.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Global Planning", "weight": 1.0} -->

[a:online\_planning] employed a receding horizon strategy for real-time planning. For tasks such as robot navigation through previously unmapped environments, such a replanning-based strategy is unavoidable since the robot's sensors will only report obstacles in the environment in some finite sensor horizon around the robot. Thus, the robot will need to replan as it makes progress through the environment and more obstacles are reported by its sensors. However, in certain scenarios where the robot has access to a larger portion of the environment, a planning strategy that is more globalin nature may be appropriate. In general, the funnel primitives provide a discrete action space which can be searched by any heuristic planner - the primary considerations here are the additional constraint of containment of the current state in the inlet and the moderately more significant cost of collision checking. Here we briefly mention a few ways in which global planning may be achieved.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Global Planning", "weight": 1.0} -->

Grid-based planners: One can build on existing trajectory library-based planning approaches to quickly find collision-free sequences of funnels that minimize a certain performance criterion (e.g., distance traversed by the nominal trajectories in the sequence). For example, uses a variant of the grid-based planning algorithm $A^\star$to search through possible sequences of trajectories in a library. The additional cost of extending such an approach for planning with funnels is the cost that comes from pruning sequences of funnels that are in collision with obstacles in the environment.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Global Planning", "weight": 1.0} -->

Maneuver automata: The Maneuver Automaton provides an alternative trajectory library-based approach that exploits continuous symmetries (such as shift invariance for ground vehicles or UAVs) to achieve efficient planning. The approach relies on having a number of trim trajectories" and maneuvers that transition between them. One can then efficiently plan sequences of trims and maneuvers that start and end at prescribed points in space by solving a set of equations that has the same structure as an inverse kinematics problem. In order to extend this approach for real-time planning with funnels, one needs to (potentially approximately) solve the inverse kinematics problem subject to the constraint that the funnel sequence is collision-free.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Global Planning", "weight": 1.0} -->

Planning backwards: The real-time planning approaches we have discussed so far all plan forward in time. However, in cases where there is a well-defined goal set that one needs to reach, it may be more efficient to plan backwards. This kind of planning is a direct analog of the preimage backchaining approach [Lozano-] in the motion planning literature. One way to perform this backwards search would be to employ a randomized strategy similar to the Rapidly-exploring Randomized Tree (RRT). In particular, we can grow a tree of funnels backwards from the goal set by using the funnels in our funnel library as primitives for the extension operator for the RRT. One can again exploit invariances in the dynamics when performing this extension operation by randomly sampling shifts/rotations of funnels (while still maintaining sequential composability and non-collision of funnels). The termination criterion for this RRT-like algorithm is the containment of the current state of the robot in the tree of funnels.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Global Planning", "weight": 1.0} -->

This is very similar to the LQR-Trees approach, with the following differences: (i) one would only use a pre-computed library of funnels in the tree rather than computing new funnels (which would be computationally infeasible for real-time implementation), and (ii) the extension operator for the tree would take into account possible collisions of funnels with obstacles in the environment.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Examples", "weight": 1.0} -->

In this section we apply the techniques presented in this paper on two simulation examples. We will consider a hardware example in Section [sec:hardware]. An example implementation of our approach for a model of the quadrotor system (Section sec:quadrotor) is available as part of the Drake toolbox.The computations in this section were performed on a 3.4 GHz desktop computer with 16 GB RAM and 4 cores.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Ground Vehicle Model", "weight": 1.0} -->

Illustration of the ground vehicle model.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Ground Vehicle Model", "weight": 1.0} -->

As our first example we consider a ground vehicle model based on the Dubins car navigating an environment of polytopic obstacles. A pictorial depiction of the model is provided in Figure [fig:dubins\_cartoon]. The vehicle is constrained to move at a fixed forward speed and can control the second derivative of its yaw angle $\psi$. We introduce uncertainty into the model by assuming that the speed of the vehicle is only known to be within a bounded range and is potentially time-varying. The full non-linear dynamics of the system are then given: $$\bf{x} = \left[\begin{array}{c} \dot \psi \end{array} \right], \dot{\bf{x}} = \left[\begin{array}{c} u \end{array} \right]% + \left[\begin{array}{c}%0 \end{array} \right].$$ with the speed of the plane $v(t) \in [9.0,11.0]$ m/s. The control input is bounded in the range $$ rad/s$^2$.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Ground Vehicle Model", "weight": 1.0} -->

[Trajectory and funnel libraries for ground vehicle model]The plot on the left shows the trajectory library for the ground vehicle model. The plot on the right shows a selection of funnels from the funnel library projected onto the $x-y$ plane.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Ground Vehicle Model", "weight": 1.0} -->

The trajectory library, $\mathcal{T}$, computed for the ground vehicle consists of 20 trajectories and is shown in Figure [fig:dubins\_traj\_library]. The trajectories $x_i(t): [0,T_i] \mapsto \mathbb{R}^4$ and the corresponding nominal open-loop control inputs were obtained via the direct collocation trajectory optimization method for the vehicle dynamics in [eq:dubins\_dynamics] with $v(t) = 10$ m/s. The initial state $x_i$ was constrained to be $$ and the final state $x_i(T_i)$ was varied in the x direction while keeping the y component fixed. We locally minimized a cost of the form: where $R$ is a positive-definite matrix. We constrained the nominal control input to be in the range $$ rad/s$^2$ to ensure that feedback controllers computed around the nominal trajectories do not immediately saturate.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Ground Vehicle Model", "weight": 1.0} -->

$x_i(t)$ in $\mathcal{T}$ we obtain controllers and funnels using the method described in Section [sec:funnels]. In order to obtain polynomial dynamics, we computed a (time-varying) degree 3 Taylor expansion of the dynamics of the system around the nominal trajectory. We note that with the right change of coordinates, one can express the dynamics of this system directly as a polynomial. In particular, we can introduce new indeterminates $s$ and $c$ for $\sin(\psi)$ and $\cos(\psi)$, and impose the constraint that $s^2 + c^2 = 1$(this equality constraint is easily imposed in the sums-of-squares programming framework). However, this increases the dimensionality of the state space and in practice we find that the time-varying Taylor approximation accurately captures the nonlinearities of the system.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Ground Vehicle Model", "weight": 1.0} -->

The approach from Section [sec:funnels\_controller] along with the time-sampled approximation described in Section [sec:funnels\_time\_sampling] (with 15 time samples) was used to synthesize a (time-varying) linear feedback controller around each trajectory. The methods described in Section [sec:funnels\_uncertainty] and [sec:funnels\_saturations] were used to take into account the parametric uncertainty and input saturations that the system is subject to. As described in Section [sec:initialization], we used a time-varying LQR controller to initialize the funnel computations. The computation time for each funnel was approximately 5-10 minutes. A subset of the funnels is shown in Figure [fig:dubins\_funnel\_library]. Note that the four-dimensional funnels have been projected down to the $x-y$ dimensions for the purpose of visualization; the true funnels take into account variations in all four state dimensions. The directed graph $\mathcal{G}(\mathcal{F})$ that encodes real-time composability between funnels (ref.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Ground Vehicle Model", "weight": 1.0} -->

Section [sec:funnel library definition]) is fully connected. [Ground vehicle model navigating through a cluttered environment using funnel library] This plot shows the funnels that were executed in order for the ground vehicle model to traverse a randomly generated obstacle environment using the funnel library based real-time planning approach.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Ground Vehicle Model", "weight": 1.0} -->

The resulting funnel library was employed by Algorithm [a:online\_planning] for planning in real-time through environments with randomly placed obstacles. Figure [fig:dubins\_example\_run] shows the funnels that were executed in order to traverse a representative environment. The obstacle positions were randomly generated from a spatial Poisson process (with a density/rate parameter of 0.6 obstacles per $m^2$). Two further barrier" obstacles were placed on the sides of the environment to prevent the vehicle from leaving the region containing obstacles. The planner was provided with a sensor horizon of 3m in the $y$ direction (forward) and $\pm 2$m in the $x$ direction (side-to-side) relative to the position of the vehicle. Only obstacles in this sensor window were reported to the planner at every instant in time. The execution times ${\tau_i}$ for each funnel were set such that replanning occurred once $80\%$ of the funnel was executed.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Ground Vehicle Model", "weight": 1.0} -->

The parametric uncertainty in the speed of the vehicle was taken into account in our simulation by randomly choosing a speed $v(t) \in \{9.0,11.0\}$ m/s after every execution time period has elapsed. The real-time planner employs the QCQP-based algorithm from Section [sec:shifting funnels] for shifting funnels in the $x-y$ directions (we did not exploit invariances in the yaw dimension of the state space in order to ensure that the vehicle moves in the forward direction and doesn't veer off to the sides). We use the FORCES Pro solver for our QCQP problems. This resulted in our implementation of the real-time planner running at approximately $50$ Hz in the worst-case (i.e., when all the funnels in the library have to be evaluated for collisions).

<!-- chunk {"id": "body-0149", "role": "body", "section": "Ground Vehicle Model", "weight": 1.0} -->

We performed extensive simulation experiments to compare our funnel library based robust planning approach with a more traditional trajectory library based method. In order to facilitate a meaningful comparison, we used the underlying trajectory library corresponding to our funnel library. The trajectory-based planner employs essentially the same outer-loop as our funnel-based approach (Algorithm [a:online\_planning]). The key difference is that the planner chooses which maneuver to execute by evaluating which trajectory has the maximal clearance from the obstacles (as measured by Euclidean distance): $$% \underset{i,j}{\textrm{argmax}} \ dist(x_i, o_j) \underset{i}{\max} \ \underset{t,j}{\min} \ \textrm{dist}(x_i(t), o_j)$$ where $x_i(t) \in \mathcal{T}$ is a trajectory in the library and $o_j \in \mathcal{O}$is an obstacle in the environment.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Ground Vehicle Model", "weight": 1.0} -->

Once a maneuver is chosen based on this metric, a time-varying LQR feedback controller computed along this trajectory is applied (the same LQR controller that is used to initialize the funnel computations). [Comparison of the funnel library and trajectory library based planning approaches for the ground vehicle model] A bar plot comparing the performance of the funnel library approach with one based on a trajectory library.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Ground Vehicle Model", "weight": 1.0} -->

To compare the two planners, we generated 100 obstacle environments randomly as described previously. For each environment, we ran the different planning algorithms until there was a collision of the vehicle with an obstacle. The distance in the $y$ direction at the time of collision was recorded for each run. Figure [fig:bar\_plot\_dists]compares the performance of the different approaches. For each distance on the x-axis of the plot the height of the bar indicates the number of runs for which the vehicle traveled beyond this distance. As is evident from the plot, our funnel library based approach provides a significant advantage over the trajectory-based method.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Ground Vehicle Model", "weight": 1.0} -->

This advantage can be partially understood by considering a specific example. In particular, Figure [fig:dubins\_traj\_vs\_funnel] demonstrates the utility of explicitly taking into account uncertainty during the planning process. There are two obstacles in front of the vehicle. The two options available to the plane are to fly straight in between the obstacles or to maneuver aggressively to the right and attempt to go around them. If the motion planner didn't take uncertainty into account and simply chose to maximize the clearance in terms of Euclidean distance from the nominal trajectory to the obstacles (see equation [eq:clearance]), it would choose the trajectory that goes right around the obstacles. However, taking the funnels into account leads to a different decision: going straight in between the obstacles is guaranteed to be safe even though the distance to the obstacles is smaller. In contrast, the maneuver that avoids going in between obstacles is less robust to uncertainty and could lead to a collision. The utility of safety guarantees in the form of funnels is especially important when the margins for error are small and making the wrong decision can lead to disastrous consequences. [The utility of making decisions using funnel libraries] This figure shows the utility of explicitly taking uncertainty into account while planning.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Ground Vehicle Model", "weight": 1.0} -->

The intuitively more “risky” strategy of flying in between two closely spaced obstacles is guaranteed to be safe, while the path that avoids going in between obstacles is less robust to uncertainty and could lead to a collision.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

The next example we consider is a model of a quadrotor system navigating through a forest of polygonal obstacles. A visualization of the system is provided in Figure [fig:quad\_visualization]. The goal of this example is to demonstrate that we can derive simple geometric conditions on the environment that guarantee collision-free flight. In other words if the environment satisfies these conditions, the Algorithm [a:replan\_funnel] presented in Section [sec:planning]will always succeed in finding a collision-free funnel from the library and the quadrotor will fly forever through the environment with no collisions. [Visualization of the quadrotor system] Visualization of the quadrotor system.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

The quadrotor model has a 12 dimensional state space consisting of the x-y-z position of the centre of mass, the roll-pitch-yaw of the body, and the time derivatives of these configuration space variables. The dynamics model we use is identical to the one presented in with an additional uncertainty term in the form of a cross wind". We modeled this with a bounded uncertainty term on the acceleration of the $x$ position: $\ddot{x} = \ddot{x}_{nominal} + \Delta$, with $\Delta \in [-0.1,0.1] \ m/s^2$. [fig:quad\_traj\_library] plots the trajectory library we use. The funnel library consists of 20 maneuvers and was created in a manner similar to the ground vehicle example. In particular, the trajectories $x_i(t): [0,T_i] \mapsto \mathbb{R}^{12}$ and the corresponding nominal open-loop control inputs were obtained via the direct collocation trajectory optimization method.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

The initial state $x_i$ was constrained to have a forwards speed of $2 \ m/s$ (i.e, $x_i = $). The final state $x_i(T_i)$ was varied in the x-direction while keeping the y-component fixed to $2$m (all other components of the final state were chosen to be the same as the initial state). We locally minimized a cost of the form: where $R$ is a positive-definite matrix. In addition to the 20 maneuvers, the library also consists of a trim" trajectory corresponding to the quadrotor flying forward at a constant speed of $2 \ m/s$. $x_i(t)$ in $\mathcal{T}$ we obtain controllers and funnels using the method described in Section [sec:funnels]. We obtained time-varying Taylor expansions of degree 3 computed around the nominal trajectory.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

The approach from Section [sec:funnels\_controller] along with the time-sampled approximation described in Section [sec:funnels\_time\_sampling] (with 15 time samples) was used to synthesize a (time-varying) linear feedback controller around each trajectory. The methods described in Section [sec:funnels\_uncertainty] were used to take into account the parametric uncertainty that the system is subject to. The computation time for each funnel was approximately 20-25 minutes. The directed graph $\mathcal{G}(\mathcal{F})$ that encodes real-time composability between funnels (ref. Section [sec:funnel library definition]) is fully connected. Moreover, the funnel corresponding to the trim trajectory is sequentially composable modulo invariances (ref. Section [sec:sqmi]) with the other maneuvers in the library, allowing us to apply the trim trajectory before or after any of the maneuvers. A subset of the funnels is shown in Figure [fig:quad\_funnel\_library].

<!-- chunk {"id": "body-0158", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

Note that the twelve-dimensional funnels have been projected down to the $x-y-z$dimensions for the purpose of visualization. [Trajectory and funnel libraries for quadrotor model]The plot on the left shows the trajectory library for the quadrotor model. The plot on the right shows a selection of funnels from the funnel library projected onto the $x-y-z$ space.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

Given this funnel library $\mathcal{F}$, we will show how one can derive simple geometric conditions on the environment that guarantee that a collision-free funnel will always be found during real-time planning. In order to simplify the analysis, we will assume that the quadrotor is navigating through a 2.5D environment (i.e., the obstacles in the environment are 2D polygons extruded in the z-direction). But, we note that our analysis can be extended to fully three dimensional environments. We will treat the geometry of the quadrotor as a sphere of radius $r_{quad}$.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

Since we are only considering 2.5D environments, it is sufficient to project the environment and funnels down to the $x-y$ plane. Consider (axis aligned) bounding boxes for the 2D obstacles (see Figure [fig:quad\_analysis\_obs]). Denote the center of the bounding box for obstacle $o_i$ as $(o_{i,x,},o_{i,y})$ for $i \in \{1,\dots,N_{obs}\}$ ($N_{obs}$ is the number of obstacles in the robot's sensor horizon). Suppose without loss of generality that the quadrotor's x-y-z position is $$. We will first derive conditions on the distances $o_{i,y}$, $d_{x,ij}:= |o_{i,x} - o_{j,x}|$, and sizes $r_{x,i}$, $r_{y,i}$ (ref.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

Figure [fig:quad\_analysis\_obs]) such that there exists a collision-free funnel in $\mathcal{F}$ assuming the quadrotor's x-y-z position is $$. We will then extend this analysis to derive conditions that guarantee that a collision-free funnel will always be found as the quadrotor applies Algorithm [a:replan\_funnel]in a receding horizon manner to fly continuously through the environment.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

Obstacle bounding boxes and quadrotor radius.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

For each funnel $F_i \in \mathcal{F}$ compute bounding boxes for the inlet and outlet of the funnel (see Figure [fig:quad\_analysis\_funnel]). We will refer to the dimensions of these bounding boxes as depicted in the figure as $f_{i,y}^{out}, f_{i,x}^{out}, f_{i,y}^{in}, f_{i,x}^{in}$. Define where $N$ is the number of funnels in the library (21 in our case). Similarly, define: $\delta$ as shown in Figure [fig:quad\_analysis\_traj] as the distance (in the $x$-dimension) of the endpoints of trajectories in $\mathcal{T}$.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

Denote by $\Delta_x$ the distance (in the $x$-dimension) between the endpoints of the most aggressive trajectories in $\mathcal{T}$ and let $\Delta_y$ be the distance in the $y$-direction that each trajectory in the library covers (see Figure [fig:quad\_analysis\_traj]).

<!-- chunk {"id": "body-0165", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

Define $r_x:= \max(r_{1,x},...,r_{N_{obs},x})$, $r_y:= \max(r_{1,y},...,r_{N_{obs},y})$. Then consider the following conditions on the obstacles: & o_{i,y} > \Delta_y, \ \forall i \in \{1,\dots,N_{obs}\} \\& d_{x,ij} > 2f_x + \delta, \ \forall i,j \in \{1,\dots,N_{obs}\}, \ i \neq j. [Notation for geometry of trajectories and funnels]Notation for geometry of trajectories and funnels.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

It is straightforward to see that these conditions imply the existence of a funnel in $\mathcal{F}$ that is collision-free when executed from the quadrotor's location at $$ (i.e., Algorithm [a:replan\_funnel] will succeed assuming that the full 12 dimensional state of the quadrotor is contained within the inlet of all the funnels in $\mathcal{F}$). In particular, the condition [eq:obs\_cond\_1] ensures that the funnels are not too close to the quadrotor's starting location. Condition [eq:obs\_cond\_2] prevents an obstacle from extending so far in the $y$-direction that it collides with the middle segments of a funnel. Condition [eq:obs\_cond\_3] ensures that obstacles do not extend so far in the $x$-direction that there is no funnel in the library that goes around the obstacle (e.g., imagine a wall in front of the quadrotor).

<!-- chunk {"id": "body-0167", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

And finally [eq:obs\_cond\_4] ensures that the gap in the $x$-direction between any two obstacles is large enough for some funnel in $\mathcal{F}$ to fit through. Then conditions [eq:obs\_cond\_3] and [eq:obs\_cond\_4] ensure that this gap occurs in a portion of the space that is reachable by one of the funnels in the library (and not in some far off location in the $x$-direction where a funnel in $\mathcal{F}$does not extend to). [Quadrotor system navigating through an environment] The plot shows the quadrotor maneuvering through a forest of polytopic obstacles in a collision-free manner. The environment satisfies simple geometric conditions that allow us to guarantee collision-free flight forever. Note that the visualized funnels have been inflated to take into account the size of the quadrotor.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

We can now extend this analysis to the scenario in which the quadrotor is flying along continuously through the environment by applying Algorithm [a:replan\_funnel] in a receding horizon manner. We will assume that the sensor horizon of the quadrotor (i.e., the range in which obstacles are reported) is greater than $\Delta_y$ in the $y$-direction and greater than $\Delta_x/2$ in the $x$-direction. We then need to ensure that when the quadrotor finishes executing a funnel, it does not find itself in a position where there are obstacles that are very close to it. In order to do this, we will first replace the conditions [eq:obs\_cond\_1] and [eq:obs\_cond\_4] with the following condition on the separation between obstacles: This condition ensures that obstacles are separated enough in either the $x$ or $y$ directions. However, this is still not enough to prevent cases where the quadrotor executes a funnel and finds itself too close to an obstacle.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

In particular, suppose that the quadrotor starts off at location $$ and that there is a single obstacle in the environment located at $(0,1.1\Delta_y+f_y)$ (the size of the obstacle will not matter in this example). When the quadrotor applies Algorithm [a:replan\_funnel] at location $$ to find a funnel, all the funnels in the library will be collision-free. Let us suppose that the algorithm chooses the funnel corresponding to the quadrotor flying straight and ends up in location $(0,\Delta_y)$. At this point, the obstacle is too close to the quadrotor and a collision-free funnel will not be found. To prevent cases such as this, we can use the trim maneuver in $\mathcal{F}$ corresponding to the quadrotor flying straight in order to pad" the distance to the obstacles. In particular, we can apply the trim maneuver until the quadrotor is at distance $\Delta_y$ from the obstacle (in the $y$-direction) and then use Algorithm [a:replan\_funnel] to replan.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

This will guarantee that Algorithm [a:replan\_funnel]will succeed and thus our analysis is complete. [fig:quad\_navigation] shows an example of the quadrotor system navigating through an environment that satisfies the geometric conditions derived above. The figure shows the sequence of funnels executed by the quadrotor to traverse the environment. Note that the funnels depicted in the plot have been inflated by $r_{quad}$in order to take into account the physical extent of the quadrotor.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

We end this section by noting that our goal here has been to demonstrate the possibility of imposing geometric conditions on the environment that guarantee collision-free flight.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Quadrotor Model", "weight": 1.0} -->

While fairly straightforward, this analysis may provide a useful starting point for more sophisticated analyses. Going forwards, our analysis may be varied or tightened in many ways. For example, we can extend it in a straightforward manner to fully 3D environments. Further, we have assumed that the quadrotor is only planning a single funnel at a time (in contrast to sequences of funnels). Planning sequences of funnels may help loosen some of the restrictions on the environment that we have made in our analysis. Another avenue is to consider cases where the locations of obstacles in the environment are drawn from a (known) stochastic process. We discuss a few possibilities for handling such settings in Section sec:designing libraries.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Hardware experiments on a fixed-wing airplane", "weight": 1.0} -->

In this section, we will validate the key components of the approach presented in this paper on a small fixed-wing airplane performing a challenging obstacle avoidance task.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Hardware experiments on a fixed-wing airplane", "weight": 1.0} -->

- Can we obtain models of a real-world challenging nonlinear dynamical system that are accurate enough to compute funnels that are valid in reality? - Can we implement the real-time planning algorithm described in Section [sec:planning]to operate at the required rate given realistic computational constraints? - Can we demonstrate our planning algorithm on a realistic and challenging obstacle avoidance task?

<!-- chunk {"id": "body-0175", "role": "body", "section": "Hardware platform", "weight": 1.0} -->

The hardware platform chosen for these experiments is the SBach RC airplane manufactured by E-flite shown in Figure [fig:sbach]. The airplane is very light ($76.6$ g) and highly maneuverable, thus allowing for dramatic obstacle avoidance maneuvers in a tight space. The control inputs to the SBach are raw servo commands to the control surfaces (ailerons, rudder, elevator) and a raw throttle setting. These commands are sent through a modified 2.4 GHz RC transmitter at an update rate of $50$Hz.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Hardware platform", "weight": 1.0} -->

[The E-flite SBach RC airplane used for hardware experiments. [Experimental setup and coordinate system. [Fixed-wing airplane and setup used for hardware experiments] Airplane hardware and experimental setup.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Task and experimental setup", "weight": 1.0} -->

The experimental setup is shown in Figure [fig:experimental\_setup]. The airplane is launched from a simple rubber-band powered launch mechanism at approximately $4-5$ m/s. The goal is to traverse the length of the room while avoiding the obstacles placed in the experimental arena. The airplane's planner is notinformed where the obstacles are beforehand; rather, the obstacle positions and geometry are reported to the planner only once the airplane clears the launcher. This simulates the receding-horizon nature of realistic obstacle avoidance tasks where the obstacle positions are not known beforehand and planning decisions must be taken in real-time. The experiments are performed in a Vicon motion capture arena that reports the airplane and obstacle poses at 120 Hz. All the online computation is performed on an off-board computer with four Intel i7 2.9GHz processors and 16 GB RAM.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Modeling and system identification", "weight": 1.0} -->

Our dynamics model of the airplane is based on the model described in (is also a good reference for modeling fixed-wing airplanes). The model has $12$ states: $${\bf{x}} = [x,y,z,\phi,\theta,\psi,\dot{x},\dot{y},\dot{z},P,Q,R].$$ Here, $+x$ is in the forward direction, $+y$ is to the right and $+z$ is downwards as depicted in Figure [fig:experimental\_setup] (this is the standard North-East-Down coordinate frame used in aeronautics). The states $\phi,\theta,\psi$ are the roll, pitch and yaw angles. The variables $P,Q,R$ are the components of the angular velocity expressed in the body coordinate frame. The control inputs of the model are the angles of the ailerons, rudder and elevator, along with the speed of the propellor. Thus, we have $4$control inputs since the ailerons are coupled to deflect in opposite directions by the commanded magnitude.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Modeling and system identification", "weight": 1.0} -->

The airplane is treated as a rigid body with aerodynamic and gravitational forces acting on it. Here, we provide a brief description of our model of the aerodynamic forces: Propellor thrustThe thrust from the propellor is proportional to the square of the propellor speed. The constant of proportionality was obtained by hanging the airplane (with the propellor pointing downwards) from a digital fish scale and measuring the thrust produced for a number of different throttle settings.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Modeling and system identification", "weight": 1.0} -->

Lift/drag on aerodynamic surfaces The lift and drag forces on the ailerons, rudder, elevator and tail of the airplane were computed using the flat-plate model. The flat-plate model was also used as a baseline for the lift and drag coefficients of the wings, but an angle-of-attack dependent correction term was added. This correction term was fit from experimental data obtained from passive (i.e., unactuated) flights in a manner similar to. Since lift and drag forces are dependent on the airspeed over the aerodynamic surface, we need to take into account the effect of propwash" (i.e. the airflow from the propellor). The relationships between the throttle speed command and the propellor downwash speed over the different control surfaces were measured using a digital anemometer in a manner similar to.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Modeling and system identification", "weight": 1.0} -->

Body dragThe drag on the airplane body is approximated as a quadratic drag term whose drag coefficient is fit from data.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Modeling and system identification", "weight": 1.0} -->

As described above, many of the parameters in the model were obtained directly from physical experiments and measurements. However, some model parameters are more difficult to measure directly. These include the moments of inertia of the airplane and the coefficient of drag associated with the airplane body. The prediction-error minimization method in the Matlab System Identification Toolbox was used to fit these parameters and to fine-tune the measured parameters. In particular, we collected data from 15-20 flights (each lasting approximately $0.5$$0.7$seconds) where the control inputs were excited using sinusoidal signals of varying frequency and amplitude.

<!-- chunk {"id": "body-0183", "role": "body", "section": "Funnel validation", "weight": 1.0} -->

[A depiction of the funnel that was validated on hardware. The funnel has been projected down to the $x-y-z$ coordinates of the state space and then reprojected onto the camera image.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Funnel validation", "weight": 1.0} -->

[The value of the Lyapunov function ($V$) plotted as a function of time for $30$ different trials of the airplane started from different initial conditions in the inlet of the funnel. The 1-sublevel set of the Lyapunov function corresponds to the funnel (i.e., a Lyapunov function of 1 or less corresponds to the airplane being inside the funnel). All 30 of the trajectories remain inside the computed funnel for the entire duration of the maneuver.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Funnel validation", "weight": 1.0} -->

Validating funnels on the fixed-wing airplane.

<!-- chunk {"id": "body-0186", "role": "body", "section": "Funnel validation", "weight": 1.0} -->

The first major goal of our hardware experiments was to demonstrate that our model of the SBach airplane is accurate enough to compute funnels that are truly meaningful for the hardware system. To this end, we computed a funnel (shown in Figure [fig:sbach\_funnel\_hardware]) for the airplane using the approach described in Section [sec:funnels]. We first estimated the set of initial states that the launcher mechanism causes the airplane to start off in (here, by initial state" we mean the state of the airplane as soon as it has cleared the launcher mechanism). This was done by fitting an ellipsoid around the initial states observed from approximately 50 experimental trials. We then used direct collocation trajectory optimization to design an open-loop maneuver that makes the airplane bend towards the left. The initial state of the trajectory is constrained to be equal to the mean of the experimentally observed initial states and the control inputs are constrained to satisfy the limits imposed by the hardware. Next we computed a time-varying LQR (TVLQR) controller around this nominal trajectory. This controller was tuned largely in simulation to ensure good tracking of the trajectory from the estimated initial condition set.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Funnel validation", "weight": 1.0} -->

The resulting closed-loop dynamics were then Taylor expanded around the nominal trajectory to degree 3 in order to obtain polynomial dynamics. Finally, we used SOS programming to compute the funnel depicted in Figure [fig:sbach\_funnel\_hardware] using the time-sampled approximation described in Section [sec:funnels\_time\_sampling](with 10 time samples). The inlet of the funnel was constrained to contain the experimentally estimated set of initial conditions. We observed that the tuned TVLQR controller does not saturate the control inputs for the most part and thus we did not find it necessary to take input saturations into account in our funnel computation. Further, we wanted to assess the validity of our funnel for the nominal dynamics model of the airplane and did not take into account any uncertainty in the model. The funnel computation took approximately 1 hour. [Still images of the airplane flying through a funnel] Still images of the SBach flying through a funnel. The funnel has been projected down to the $x-y-z$ coordinates of the state space and then reprojected onto the camera image.

<!-- chunk {"id": "body-0188", "role": "body", "section": "Funnel validation", "weight": 1.0} -->

A video with a visualization of the funnel and flights through it is available online at We validate the funnel shown in Figure [fig:sbach\_funnel\_hardware] with $30$ experimental trials of the airplane executing the maneuver corresponding to the funnel. The airplane is started off in different initial conditions in the inlet of the funnel and the TVLQR controller is applied for the duration of the maneuver. Figure [fig:sbach\_funnel\_stills] shows still images of a sample flight of the airplane executing the maneuver with the funnel superimposed onto the images. A video with a visualization of the funnel and flights through it is available online at [fig:sbach\_V\_vs\_t] provides a more quantitative perspective on the flights. In particular, the figure shows the value of the Lyapunov function $V(\bar{x},t)$ as a function of time achieved during the $30$ experimental trials. Here, the Lyapunov function has been normalized so that the 1-level set corresponds to the boundary of the funnel.

<!-- chunk {"id": "body-0189", "role": "body", "section": "Funnel validation", "weight": 1.0} -->

As the plot illustrates, all $30$trajectories remain inside the computed 12 dimensional funnel for the entire duration of the maneuver. This suggests that our model of the airplane is accurate enough to produce funnels that are indeed valid for the hardware system.

<!-- chunk {"id": "body-0190", "role": "body", "section": "Obstacle avoidance experiments", "weight": 1.0} -->

The second major goal of our hardware experiments was to demonstrate the funnel library based real-time planning algorithm proposed in Section [sec:planning] on the obstacle avoidance task described in Section [sec:sbach\_task]. Our first step was to design a rich trajectory library consisting of a large number of different maneuvers. We initialized the library with the maneuver from Section [sec:sbach\_funnel] and augmented it by computing trajectories with varying final states. In particular, the library consists of $40$ trajectories which were obtained by discretizing the final state in the $y$ and $z$ coordinates and using direct collocation trajectory optimization to compute locally optimal trajectories for the airplane model described in Section [sec:sbach\_model]. The $x-y-z$ components of this trajectory library are depicted in Figure [fig:sbach\_traj\_library], with the trajectory from Section [sec:sbach\_funnel]highlighted in blue. [Trajectory library for the airplane] Trajectory library for the SBach airplane. The library consists of $40$ different maneuvers.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Obstacle avoidance experiments", "weight": 1.0} -->

The maneuver from Section [sec:sbach\_funnel] is highlighted in blue.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Obstacle avoidance experiments", "weight": 1.0} -->

For each trajectory in our library, we computed a TVLQR controller with the same state/action costs as the controller for the maneuver in Section [sec:sbach\_funnel]. As in Section [sec:sbach\_funnel], we used SOS programming to compute funnels for each trajectory in the library. We note that since our model of the dynamics of the airplane is symmetric with respect to reflection about the $x$axis, we were able to halve the amount of computation involved in constructing the trajectory/funnel library by exploiting this symmetry. [sec:sbach\_task], the positions and geometry of the obstacles are not reported to the planner until the airplane has cleared the launcher. This forces planning decisions to be made in real-time. We use the planning algorithm described in Section [sec:planning] to choose a funnel from our library. The planner employs the QCQP-based algorithm from Section [sec:shifting funnels] for shifting funnels in the $x-y-z$ directions. As in the other examples considered in this paper, we use the FORCES Pro solver for our QCQP problems.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Obstacle avoidance experiments", "weight": 1.0} -->

If no satisfactory funnel is found by the planner, we revert to a failsafe" option which involves switching off the propellor and gliding to a halt. A more sophisticated failsafe would be to transition to a propellor-hang" mode (with a corresponding funnel whose inlet contains the set of initial conditions the airplane may be in when it is launched).However, we found that our failsafe provides adequate protection to the airplane's hardware as it usually glides on to the safety net before colliding with any obstacles. Finally, we note that since the experimental arena is quite limited in space, we do not replan funnels once one has been chosen; the airplane executes the feedback controller corresponding to the chosen funnel for the whole duration of the flight.

<!-- chunk {"id": "body-0194", "role": "body", "section": "Obstacle avoidance experiments", "weight": 1.0} -->

We tested our approach on 15 different obstacle environments of varying difficulty. These environments are shown in Figures [fig:env\_images\_1] and [fig:env\_images\_2]. The obstacles include poles of different lengths in varying orientations and also a hoop of diameter equal to $0.9~m$ (as a reference the airplane's wingspan is $0.44~m$, thus only leaving $0.23~m$ of margin on either side of the airplane assuming it passes through the center of the hoop). We model the poles as cuboids with heights equal to that of the poles and widths equal to the diameter. The hoop is approximated with eight polytopic segments (see Figure [fig:sbach\_planned\_funnels]). [fig:histogram\_object\_distances] presents a more quantitative perspective on the obstacle environments. Here we we have plotted a histogram of the gaps between obstacles in the environment and compared it to the wingspan of the airplane. In particular, for each obstacle in a given environment we consider the distance Here, the distance between obstacles is defined in the usual way for sets.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Obstacle avoidance experiments", "weight": 1.0} -->

In particular, for any pair of obstacles $O_1$ and $O_2$, we define the distance between them as $\underset{x_1 \in O_1,x_2 \in O_2}{\textrm{min}} \ \|x_1 - x_2\|_2$. to the closest obstacle that is at least $5~cm$ away (the $5~cm$ threshold is chosen to prevent obstacles that are right next to each other being considered as having a small gap. For example, the obstacle closest to one of the horizontal poles in the first environment in Figure [fig:env\_images\_1] should be the other horizontal pole and not the adjacent vertical pole). As the histogram illustrates, a significant fraction (approximately $35 \%$) of the gaps are less than the airplane wingspan and about $66\%$ of the gaps are less than two wingspans. Of course, it is worth noting that not all of the gaps greater than the wingspan are in fact negotiable (e.g., obstacles placed far apart along the $x$ direction).

<!-- chunk {"id": "body-0196", "role": "body", "section": "Obstacle avoidance experiments", "weight": 1.0} -->

[Environments 1-8 on which the online planning algorithm was tested] Environments 1-8 on which the online planning algorithm was tested. The obstacles include poles of different lengths in varying orientations and also a hoop of diameter equal to 0.9 m. [Environments 9-15 on which the online planning algorithm was tested] Environments 9-15 on which we tested our planning algorithm. The bottom most image shows the only failure case. Here the airplane brushed one of the obstacles on its way across the room. [Histogram of gaps between obstacles in our test environments] Histogram of gaps between objects in our test environments compared with the airplane's wingspan ($0.44~m$). As the plot shows, a significant number of the gaps between obstacles are less than then wingspan.

<!-- chunk {"id": "body-0197", "role": "body", "section": "Obstacle avoidance experiments", "weight": 1.0} -->

A video of the airplane traversing a few representative environments is available online at For our experiments, we flew the airplane in each of the 15 environments onceThe only exception to this was a small number of occasions during our experiments where we observed the failsafe" option being employed by the planner (i.e., switching off the throttle and gliding to a halt). This was typically caused by failures in the launching mechanism such as the airplane making contact with the operator's hand on its way out of the launcher. Due to the altered initial conditions in these cases the airplane is not in the inlet of most or all of the funnels and thus has to resort to the failsafe. On these occasions we simply repeated the experiment to obtain a successful launch.. Out of the 15 environments the airplane was able to successfully negotiate 14 of them, thus demonstrating the efficacy of our real-time planner on this challenging task. We further performed five more flights on a single environment (the one in the bottom right corner of Figure fig:env\_images\_1). The repeated flights on this environment were all successful, thus demonstrating the robustness of our approach to initial conditions.

<!-- chunk {"id": "body-0198", "role": "body", "section": "Obstacle avoidance experiments", "weight": 1.0} -->

[Planned funnels for different environments traversed by airplane] This figure depicts the planned funnel along with the polygonal obstacle representations for four of our fifteen test environments. Note that the funnels have been inflated to take into account the collision geometry of the airplane (modeled as a sphere of diameter equal to the wingspan). [The importance of shifting funnels by exploiting invariances in dynamics] The QCQP-based algorithm for shifting funnels (Section [sec:shifting funnels]) plays a crucial role in the planner's ability to find collision free funnels. Here we compare the output of the planner with and without applying the QCQP-based algorithm for shifting funnels. The best funnel found in the former case is well in collision with the obstacles while in the latter case the planner is able to find a collision free funnel. Note that the funnels chosen in the different cases correspond to different maneuvers. [fig:sbach\_planned\_funnels] presents the output of our real-time planner on four of the more challenging environments.

<!-- chunk {"id": "body-0199", "role": "body", "section": "Obstacle avoidance experiments", "weight": 1.0} -->

In particular we plot the funnel chosen by the planner (which have been shifted using the QCQP-based algorithm presented in Section [sec:shifting funnels]) alongside an image sequence showing the airplane executing the plan. We note that the increased expressivity afforded to us by the ability to shift funnels in the cyclic coordinates has a large impact on the planner being able to find collision free funnels. Perhaps the best example of this is the environment which contains the hoop (top row of Figure [fig:sbach\_planned\_funnels]). Without the ability to make small adjustments to the funnels, the chances of finding a collision free funnel are extremely low (we would require a funnel that passes almost exactly through the center of the hoop). Figure [fig:sbach\_hoop\_shifting]compares the output of the planner with and without applying the QCQP-based algorithm for shifting funnels. As we can observe, the best funnel found in the former case is well in collision with the obstacles while in the latter case the planner is able to find a collision free funnel. This illustrates the crucial role that exploiting invariances plays in the success of the planner on this task.

<!-- chunk {"id": "body-0200", "role": "body", "section": "Obstacle avoidance experiments", "weight": 1.0} -->

As mentioned before, the airplane was able to successfully negotiate 14 out of our 15 environments. The single failure case occurred on the environment shown at the bottom of Figure [fig:env\_images\_2], where the airplane clipped one of the poles close to the end of its flight. This failure can be attributed to the fact that the planner chose to execute one of a small handful of maneuvers that are more aggressive than the funnel we validated in Section [sec:sbach\_funnel]. The controller saturates the control inputs significantly on this maneuver and hence violates our assumption about input limits not being reached. Hence this funnel is not entirely valid on the hardware system. While we could have taken actuator saturations into account while computing the funnels (see Section [sec:funnels\_saturations]), we chose not to do so in order to reduce the computation time. In hindsight, a more careful treatment of the system would have included saturations when computing funnels.

<!-- chunk {"id": "body-0201", "role": "body", "section": "Implementation details", "weight": 1.0} -->

We end this section by mentioning a few implementation details that were important in achieving the results presented above. First, while the Vicon motion tracking system provides accurate position and orientation estimates at $120$ Hz, a finite difference of these measurements can lead to noisy estimates of the derivative states. For our experiments we filtered the finite differences using a simple Luenberger observer.

<!-- chunk {"id": "body-0202", "role": "body", "section": "Implementation details", "weight": 1.0} -->

Second, we observed a delay of approximately $55~ms$ in our closed-loop hardware system. While there are several ways to explicitly take this into account by adding delay states to our airplane model, we accommodate for the delay during execution by simulating our model forwards by $55~ms$ from the estimated current state and using this simulated future state to compute the current control input. This simple strategy is a common one and has previously been found to be effective in a wide range of applications.

<!-- chunk {"id": "body-0203", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

In this paper we have presented an approach for real-time motion planning in a priori unknown environments with dynamic uncertainty in the form of bounded parametric model uncertainty and external disturbances. The method augments the traditional trajectory library approach by constructing stabilizing controllers around the nominal trajectories in a library and computing outer approximations of reachable sets (funnels) for the resulting closed-loop controllers via sums-of-squares (SOS) programming. The pre-computed funnel library is then used to plan online by sequentially composing them together in a manner that ensures obstacles are avoided.

<!-- chunk {"id": "body-0204", "role": "body", "section": "Discussion and Conclusion", "weight": 1.5} -->

We have demonstrated our approach using extensive simulation experiments on a ground vehicle model. These experiments demonstrate that our approach can afford significant advantages over a trajectory-based approach. We also applied our approach to a quadrotor model and demonstrated how for certain classes of environments we can guarantee that the system will fly forever in a collision-free manner. We have also validated our approach using thorough hardware experiments on a small fixed-wing airplane flying through previously unseen cluttered environments at high speeds. To our knowledge, these simulation and hardware results are among the first examplesof provably safe and robust control for robotic systems with complex nonlinear dynamics that need to plan in real-time in environments with complex geometric constraints. It is also worth noting that while one often associates robustness with very conservative behavior, our hardware experiments demonstrate that this need not be the case. In particular, the airplane performs some very aggressive maneuvers while still being robust.

<!-- chunk {"id": "body-0205", "role": "body", "section": "Numerical difficulties", "weight": 1.0} -->

There are a number of challenges associated with our approach. One of the main difficulties in implementing our method is the relative immaturity of solvers for semidefinite programs (SDPs). While recently released software such as the MOSEK solver have improved the speed with which solutions can be obtained, SDP solvers are still in their infancy as compared to solvers for Linear Programs (LPs). Thus, numerical issues (e.g., due to the scaling of problem data) inevitably arise in practice and must be dealt with in a relatively ad hoc manner (e.g., rescaling problem data or removing redundant decision variables). However, preprocessing of sums-of-squares (SOS) programs and SDPs is an active area of inquiry and solver technology is bound to improve as SDPs are more widely adopted in practice.

<!-- chunk {"id": "body-0206", "role": "body", "section": "Robots with complex geometries", "weight": 1.0} -->

Another challenge associated with our method has to do with implementing the approach on robots with complex kinematics/geometry. One option (as described in Section [sec:planning]) is to project the funnel onto the configuration space (C-space) of the system and perform collision checking against the C-space representation of obstacles. However, computing C-space representations of obstacles is typically challenging for non-trivial geometries, especially since it needs to be done as obstacles are reported in real-time.

<!-- chunk {"id": "body-0207", "role": "body", "section": "Robots with complex geometries", "weight": 1.0} -->

For the examples considered in this paper, the geometry of the robots were approximated relatively accurately by spheres. This allowed us to project the funnel onto the $x-y-z$ space (in contrast to the full configuration space of the system) and inflate this projection by the radius of the corresponding sphere. These inflated funnels were then used for collision-checking during real-time planning. For robots with complex geometries, inflating the funnel in $x-y-z$space in this manner is not an entirely straightforward operation. However, this is potentially a more promising approach than performing collision-checking against C-space obstacles since the inflation can computed in the offline computation stage as it depends only on the geometry of the robot and not the obstacles.

<!-- chunk {"id": "body-0208", "role": "body", "section": "Designing funnel libraries", "weight": 1.0} -->

There is an inherent tradeoff in our approach between the richness of the funnel library and the amount of computation that needs to be performed in real-time in order to be able to search through it. For extremely large funnel libraries, it may be computationally difficult to search through all the funnels while planning online. It is thus important to explore ways in which one could speed up this search. For example, one could exploit the observation that funnels in close proximity to a funnel that is in collision are also likely to be in collision and use this to choose the sequence in which to evaluate funnels for collisions. Further, given certain features of the environment one may be able to predict which funnels are likely to be in collision (without actually performing collision-checking) and evaluate these funnels first. These intuitions have been formalized and exploited using the theory of submodular optimization in the context of trajectory libraries. The approach allows one to optimize the sequence in which trajectories are evaluated and should be generalizable to funnel libraries as well.

<!-- chunk {"id": "body-0209", "role": "body", "section": "Designing funnel libraries", "weight": 1.0} -->

A closely related question is how to choose the funnels in the library in the first place. As we observed in Section [sec:quadrotor] for the quadrotor system, one can derive relatively simple geometric conditions on the environment in order for us to be able to guarantee that the system will be able to navigate through it without collisions. If we know a priori that our environment will satisfy these geometric conditions, this provides a way to check if our funnel library is sufficiently rich. However, for real-world environments (e.g., forests) we may not be able to make such assumptions. Instead, we might have a generative (probabilistic) model of our environments and could use this to evaluate/design our funnel library. For instance, it is known that the locations of trees in a forest are modeled well by spatial Poisson processes. In such settings, it may be possible to design a randomized algorithm for generating the funnel library where one samples different realizations of the environment, searches through the existing library to find a collision-free funnel for the sampled environment, and adds a new funnel to the library when such a funnel doesn't exist.

<!-- chunk {"id": "body-0210", "role": "body", "section": "Designing funnel libraries", "weight": 1.0} -->

In a similar vein, extending the results presented in on flight through ergodic forests to the funnel library setting is an interesting direction to pursue. In particular, uses results from percolation theory to provide bounds on the speed at which a robot can fly safely through a forest in which obstacles have been sampled from an ergodic spatial process. Extending the results from to reason about funnel libraries could allow us to check if a given funnel library is sufficiently rich under the assumption that the spatial process from which obstacles are drawn is ergodic and known.

<!-- chunk {"id": "body-0211", "role": "body", "section": "Probabilistic guarantees", "weight": 1.0} -->

Throughout this paper, we have assumed that all disturbances and uncertainty are bounded with probability one. In practice, this assumption may either not be fully valid or could lead to overly conservative performance. In such situations, it is more natural to provide guarantees of a probabilistic nature. Recently, results from classical super-martingale theory have been combined with sums-of-squares programming in order to compute such probabilistic certificates of finite time invariance, i.e. provide upper bounds on the probability that a stochastic nonlinear system will leave a given region of state space. Combining the techniques presented with the approach presented in this work to perform robust online planning on stochastic systems will be the subject of

<!-- chunk {"id": "body-0212", "role": "body", "section": "Reasoning about perception systems", "weight": 1.0} -->

In this paper, we have focused most of our attention on reasoning about the real-time planning and control systems. In particular, we assumed that the robot is equipped with a perception system that reports (at runtime) regions in which obstacles are guaranteed to lie within. This may not always be a valid assumption; in practice, perceptual systems can often have false negatives and fail to report an obstacle in the environment. In such scenarios, it is unreasonable to expect to guarantee with probability one that the system will remain collision-free and we can only hope for probabilistic guarantees. One could envision modeling this perceptual uncertainty by considering an occupancy map with probabilities of occupancy associated with each voxel. Modeling and reasoning about such perceptual uncertainty remains an important open problem.

<!-- chunk {"id": "body-0213", "role": "body", "section": "Real-time computation of funnels", "weight": 1.0} -->

Due to the computation time associated with funnels, the approach presented in this work had two phases: an offline phase for computing funnels and an online stage for real-time planning with funnels. Recently, more scalable alternatives to SOS programming have been introduced. These alternatives rely on linear and second-order cone programming instead of semidefinite programming. This makes it possible to obtain large computational gains in terms of scalability and running time using DSOS and SDSOS programming as compared to SOS programming (see for comparisons of DSOS/SDSOS with SOS on large-scale controls applications). In addition to the ability to handle higher dimensional robotic systems, this also raises the interesting possibility of being able to dispense with the offline computation stage and compute a funnel and feedback controller in real-timebased on the geometry of the environment. Currently, this would only be feasible for relatively low-dimensional systems but may be an exciting direction to pursue.

<!-- chunk {"id": "body-0214", "role": "body", "section": "Real-time computation of funnels", "weight": 1.0} -->

We believe that the work presented in this paper has the potential to be deployed on real robots to make them operate safely in real-world environments. Our hope is that by building upon this work and pursuing the directions for future research presented above we can make this a reality.
