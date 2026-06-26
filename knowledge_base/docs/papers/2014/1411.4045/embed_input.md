<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Admissible Velocity Propagation: Beyond Quasi-Static Path Planning for High-Dimensional Robots

Topics include Kinodynamic planning, Path-velocity decomposition, Quasi-static planning, Velocity propagation, Dynamic motions.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Starting point is quasi-static (velocity ~= 0) path planning. Then augments state space with velocity and uses propagation of velocity using kinodynamics to determine the reachable set (admissible interval) of velocity, and includes that in the connection check for new nodes. Builds on the foundational TOPP velocity planner. AVP is modularly (re)usable in many sampling-based planners; the authors give a concrete instantiation and numerical experiments with AVP-RRT.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Path-velocity decomposition is an intuitive yet powerful approach to address the complexity of kinodynamic motion planning. The difficult trajectory planning problem is solved in two separate, simpler, steps: first, find a path in the configuration space that satisfies the geometric constraints (path planning), and second, find a time-parameterization of that path satisfying the kinodynamic constraints. A fundamental requirement is that the path found in the first step should be time-parameterizable. Most existing works fulfill this requirement by enforcing quasi-static constraints in the path planning step, resulting in an important loss in completeness. We propose a method that enables path-velocity decomposition to discover truly dynamic motions, i.e. motions that are not quasi-statically executable. At the heart of the proposed method is a new algorithm — Admissible Velocity Propagation — which, given a path and an interval of reachable velocities at the beginning of that path, computes the interval of all reachable and time-parameterizable velocities at the end of that path.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Planning motions for robots with many degrees of freedom and subject to kinodynamic constraints (i.e. constraints that involve higher-order time-derivatives of the robot configuration ) is one of the most important and challenging problems in robotics. Path-velocity decomposition is an intuitive yet powerful approach to address the complexity of kinodynamic motion planning: first, find a *path* in the configuration space that satisfies the geometric constraints, such as obstacle avoidance, joint limits, kinematic closure, etc. (path planning), and second, find a *time-parameterization* of that path satisfying the kinodynamic constraints, such as torque limits for manipulators, dynamic balance for legged robots, etc.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Advantages of path-velocity decomposition", "weight": 1.0} -->

This approach was suggested as early as 1986 -- only a few years after the birth of motion planning itself as a research field -- by Kant and Zucker, in the context of motion planning amongst movable obstacles. Since then, it has become an important tool to address many kinodynamic planning problems, from manipulators subject to torque limits, to coordination of teams of mobile robots, to legged robots subject to balance constraints, etc. In fact, to our knowledge, path-velocity decomposition \[either explicitly or implicitly, as e.g. when only the geometric motion is planned and the time-parameterization is left to the execution phase\] is the only *motion planning* approach that has been shown to work on *actual high-DOF robots* such as humanoids.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Advantages of path-velocity decomposition", "weight": 1.0} -->

Path-velocity decomposition is appealing in that it *exploits the natural decomposition* of the constraints, in most systems, into two categories: those depending uniquely on the robot configuration, and those depending in particular on the velocity, which in turn is related to the energy of the system. Consider for instance a humanoid robot in a multi-contact task. Such a robot must avoid collision with the environment, avoid self-collisions, respect kinematic closure for the parts in contact with the environment (e.g. the stance foot must be fixed with respect to the ground), maintain balance. It can be noted that constraints (1 -- 3) are exclusively related to the configuration of the robot, while constraint, once a path is given, depends mostly on the path velocity.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Advantages of path-velocity decomposition", "weight": 1.0} -->

From a practical viewpoint, the two sub-problems -- geometric path planning and kinodynamic time-parameterization -- have received so much attention from the robotics community in the past three decades that a large body of theory and good practices exist and can be readily combined to yield efficient *trajectory* planners. Briefly, high-dimensional and cluttered geometric path planning problems can now be solved in seconds thanks to sampling-based planning algorithms such as PRM or RRT and to the dozens of heuristics that have been developed for these algorithms. Regarding kinodynamic time-parameterization, two important discoveries about the structure of the problem have led to particularly efficient algorithmic solutions. First, the bang-bang nature of the optimal velocity profile was identified, leading to fast *numerical integration* methods. Second, this problem was shown to be reducible to a *convex optimization* problem, leading to robust and versatile convex-optimization-based solutions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problems with state-space planning and trajectory optimization approaches", "weight": 1.0} -->

Alternative approaches to path-velocity decomposition include planning directly in the state space and trajectory optimization. The first approach deploys traditional path planners such as RRT or PRM directly into the *state space*, that is, the configuration space augmented with velocity coordinates. Three main difficulties are associated with this approach. First, the dimension of the state space is twice that of the configuration space, resulting in higher algorithmic complexity. Second, while connecting two adjacent configurations under geometric constraints is trivial (using e.g. linear segments), connecting two adjacent states under kinodynamic constraints is considerably more challenging and time-consuming, requiring e.g. to solve a two-point boundary value problem or to sample in the control space and to integrate forward the sampled control. Third, especially for state-space RRTs, designing a reasonable *metric* is particularly difficult: Shkolnik et al. showed that, even for the 1-DOF pendulum subject to torque constraints, a state-space RRT with a simple Euclidean metric is doomed to failure. The authors then proposed to construct an efficient metric by solving local optimal control problems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problems with state-space planning and trajectory optimization approaches", "weight": 1.0} -->

In a similar fashion, kinodynamic planners based on locally linearized system dynamics were proposed, such as LQR-Tree or LQR-RRT^∗^. While such methods can be applied to low-DOF systems, the necessity to solve an optimal control problem of the dimension of the system at each tree extension makes it unlikely to scale to higher dimensions. For these reasons, in spite of appealing completeness guarantees, there exist, to our knowledge, few examples of successful application of state-space planning to high-DOF systems with complex nonlinear dynamics and constraints in challenging environments.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problems with state-space planning and trajectory optimization approaches", "weight": 1.0} -->

The second approach, trajectory optimization, starts with an initial trajectory, which may not be valid (for example the trajectory may not reach the goal configuration, the robot may collide with the environment or may lose balance at some time instants, etc.) One then iteratively modifies the trajectory so as to decrease a cost -- which encodes in particular how much the constraints are violated -- until it falls below a certain threshold, implying in turn that the trajectory reaches the goal and all constraints are satisfied. Many interesting variations exist: the iterative modification step may be deterministic or stochastic, the optimization may be done *through* contact, etc. However, for long time-horizon and high-DOF systems, this approach requires solving a large nonlinear optimization problem, which is computationally challenging because of the huge problem size and the existence of many local minima.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The quasi-static condition and its limitations", "weight": 1.0} -->

Coming back to path-velocity decomposition, a fundamental requirement here is that the path found in the first step must be time-parameterizable. A commonly-used method to fulfill this requirement is to consider, in that step, the *quasi-static* constraints that are derived from the original kinodynamic constraints by assuming that the motion is executed at zero velocity. Indeed, the so-derived quasi-static constraints can be expressed using only configuration-space variables, in such a way that planning with quasi-static constraints is purely a geometric path planning problem. In the context of legged robots for example, the balance of the robot at zero velocity is guaranteed when the projection of the center of gravity lies in the support area -- a purely geometric condition. This quasi-static condition is assumed in most works dedicated to the planning of complex humanoid motions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The quasi-static condition and its limitations", "weight": 1.0} -->

This workaround suffers however from a major limitation: the quasi-static condition may be too restrictive and one thus may overlook many possible solutions, i.e. incurring an important *loss in completeness*. For instance, legged robots walking with ZMP-based control are dynamically balanced but almost never satisfy the aforementioned quasi-static condition on the center of gravity. Another example is provided by an actuated pendulum subject to severe torque limits, but which can still be put into the upright position by swinging back and forth several times. It is clear that such solutions make an essential use of the system dynamics and can in no way be discovered by quasi-static methods, nor by any method that considers only configuration-space coordinates.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Planning truly dynamic motions", "weight": 1.0} -->

Here we propose a method to overcome this limitation. At the heart of the proposed method is a new algorithm -- Admissible Velocity Propagation (AVP) -- which is based in turn on the classical Time-Optimal Path Parameterization (TOPP) algorithm first introduced by Bobrow et al.; Shin and McKay and later perfected by many others. In contrast with TOPP, which determines *one* optimal velocity profile along a given path, AVP addresses *all* valid velocity profiles along that path, requiring only slightly more computation time than TOPP itself. Combining AVP with usual sampling-based path planners, such as RRT, gives rise to a family of new trajectory planners that can appropriately handle kinodynamic constraints while retaining the advantages associated with path-velocity decomposition.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Planning truly dynamic motions", "weight": 1.0} -->

The remainder of this article is organized as follows. In Section 2, we briefly recall the fundamentals of TOPP before presenting AVP. In Section 3, we show how to combine AVP with usual sampling-based path planners such as RRT. In Section 4, we demonstrate the efficiency of the new AVP-based planners on some challenging kinodynamic planning problems -- in particular, those where the quasi-static approach is *guaranteed* to fail. In one of the applications, the planned motion is executed on an actual 6-DOF robot. Finally, in Section 5, we discuss the advantages and limitations of the proposed approach (one particular limitation is that the approach does not *a priori* apply to under-actuated systems) and sketch some future research directions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Admissible Velocity Propagation (AVP)", "weight": 1.0} -->

This section presents the Admissible Velocity Propagation algorithm (AVP), which constitutes the heart of our approach.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Admissible Velocity Propagation (AVP)", "weight": 1.0} -->

This algorithm takes as inputs: a path $\mathcal{P}$ in the configuration space, and an interval $\lbrack{\overset{˙}{s}}_{beg}^{\min},{\overset{˙}{s}}_{beg}^{\max}\rbrack$ of initial path velocities; and returns the *interval* (cf. Theorem 1 ‣ 2 Propagating admissible velocities along a path ‣ Admissible Velocity Propagation: Beyond Quasi-Static Path Planning for High-Dimensional Robots")) $\lbrack{\overset{˙}{s}}_{end}^{\min},{\overset{˙}{s}}_{end}^{\max}\rbrack$ of *all* path velocities that the system can reach *at the end* of $\mathcal{P}$ after traversing $\mathcal{P}$ while respecting the system constraints ^44^4Johnson and Hauser also introduced a velocity interval propagation algorithm along a path but for pure kinematic constraints and moving

<!-- chunk {"id": "body-0017", "role": "body", "section": "Admissible Velocity Propagation (AVP)", "weight": 1.0} -->

The algorithm comprises the following three steps:: Compute the limiting curves;: Determine the *maximum* final velocity ${\overset{˙}{s}}_{end}^{\max}$ by integrating *forward* from $s = 0$;: Determine the *minimum* final velocity ${\overset{˙}{s}}_{end}^{\min}$ by bisection search and by integrating *backward* from $s = s_{end}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Admissible Velocity Propagation (AVP)", "weight": 1.0} -->

We now detail each of these steps.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Computing the limiting curves", "weight": 1.0} -->

We first compute the Concatenated Limiting Curve (CLC) as shown in Section 2.1 ‣ 2 Propagating admissible velocities along a path ‣ Admissible Velocity Propagation: Beyond Quasi-Static Path Planning for High-Dimensional Robots"). From Lemma 2 ‣ 2.1 Background: Time-Optimal Path Parameterization (TOPP) ‣ 2 Propagating admissible velocities along a path ‣ Admissible Velocity Propagation: Beyond Quasi-Static Path Planning for High-Dimensional Robots"), either one of the $LC$'s reaches 0 or the $CLC$ is continuous. The former case is covered by A1 below, while the latter is covered by A2--5.: One of the $LC$'s hits the line $\overset{˙}{s} = 0$. In this case, the path cannot be traversed by the system without violating the kinodynamic constraints: AVP returns Failure. Indeed, assume that a backward ($\alpha$) profile hits $\overset{˙}{s} = 0$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Computing the limiting curves", "weight": 1.0} -->

Then any profile that goes from $s = 0$ to $s = s_{end}$ must cross that profile somewhere and *from above*, which violates the $\alpha$ bound (see Figure 2 ‣ 2 Propagating admissible velocities along a path ‣ Admissible Velocity Propagation: Beyond Quasi-Static Path Planning for High-Dimensional Robots")A). Similarly, if a forward ($\beta$) profile hits $\overset{˙}{s} = 0$, then that profile must be crossed somewhere and *from below*, which violates the $\beta$ bound. Thus, no valid profile can go from $s = 0$ to $s = s_{end}$; Figure 2: Illustration for step A (computation of the LC’s). A: illustration for case A1. A profile that crosses an α-CLC violates the α bound. B: illustration for case A3.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Computing the limiting curves", "weight": 1.0} -->

The CLC is now assumed to be continuous and strictly positive. Since it is bounded by $s = 0$ from the left, $s = s_{end}$ from the right, $\overset{˙}{s} = 0$ from the bottom and the MVC from the top, there are only four exclusive and exhaustive cases, listed below.: The $CLC$ hits the $MVC$ while integrating backward and while integrating forward. In this case, let ${\overset{˙}{s}}_{beg}^{\ast}\overset{def}{=}{{MVC}{}}$ and go to B. The situation where there is no switch point is assimilated to this case;: The $CLC$ hits $s = 0$ while integrating backward, and the $MVC$ while integrating forward (see Figure 2 ‣ 2 Propagating admissible velocities along a path ‣ Admissible Velocity Propagation: Beyond Quasi-Static Path Planning for High-Dimensional Robots")B).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Determining the minimum final velocity", "weight": 1.0} -->

Let us integrate backward from $(s_{end},{\overset{˙}{s}}_{test})$ following $\alpha$ and call the resulting profile $\Psi$. We have the following lemma.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Implementation and complexity of AVP", "weight": 1.0} -->

As clear from the previous section, AVP can be readily adapted from the numerical integration approach to TOPP. As a matter of fact, we implemented AVP in about 100 lines of C++ code based on the TOPP library we developed previously.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Implementation and complexity of AVP", "weight": 1.0} -->

In terms of complexity, the main difference between AVP and TOPP lies in the bisection search of step C, which requires $\log{({1/\epsilon})}$ backward integrations. However, in practice, these integrations terminate quickly, either by hitting the MVC or the line $\overset{˙}{s} = 0$. Thus, the actual running time of AVP is only slightly larger than that of TOPP. As illustration, in the bottle experiment of Section 4.2, we considered 100 random paths, discretized with grid size $N = 1000$. TOPP and AVP (with the bisection precision $\epsilon = 0.01$) under velocity, acceleration and balance constraints took the same amount of computation time 0.033 $\pm$ 0.003 s per path.

<!-- chunk {"id": "body-0025", "role": "body", "section": "\"Direct\" velocity bounds", "weight": 1.0} -->

"Direct" velocity bounds in the form of (2 ‣ 2 Propagating admissible velocities along a path ‣ Admissible Velocity Propagation: Beyond Quasi-Static Path Planning for High-Dimensional Robots")) give rise to another maximum velocity curve, say ${MVC}_{D}$, in the $(s,\overset{˙}{s})$ space. When a forward profile intersects ${MVC}_{D}$ (before reaching the "Bobrow's $MVC$"), several cases can happen: If "sliding" along the ${MVC}_{D}$ does not violate the actuation bounds (1 ‣ 2 Propagating admissible velocities along a path ‣ Admissible Velocity Propagation: Beyond Quasi-Static Path Planning for High-Dimensional Robots")), then slide as far as possible along the $MVC$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "\"Direct\" velocity bounds", "weight": 1.0} -->

The "slide" terminates either (a) when the maximum acceleration vector $\beta$ points downward from the ${MVC}_{D}$: in this case follow that vector out of ${MVC}_{D}$ or (b) when the minimum acceleration vector $\alpha$ points upward from the ${MVC}_{D}$: in this case, proceed as in 2; If not, then search forward on the ${MVC}_{D}$ until finding a point from which one can integrate backward. Such a point is guaranteed to exist and the backward profile will intersect the forward profile.

<!-- chunk {"id": "body-0027", "role": "body", "section": "\"Direct\" velocity bounds", "weight": 1.0} -->

For more details, the reader is referred to.

<!-- chunk {"id": "body-0028", "role": "body", "section": "\"Direct\" velocity bounds", "weight": 1.0} -->

This reasoning can be extended to AVP: when integrating the forward or the backward profiles (in steps A, B, C of the algorithm), each time a profile intersects the ${MVC}_{D}$, one simply applies the above steps.

<!-- chunk {"id": "body-0029", "role": "body", "section": "AVP-backward", "weight": 1.0} -->

Consider the "AVP-backward" problem: given an interval of final velocities $\lbrack{\overset{˙}{s}}_{end}^{\min},{\overset{˙}{s}}_{end}^{\max}\rbrack$, compute the interval $\lbrack{\overset{˙}{s}}_{beg}^{\min},{\overset{˙}{s}}_{beg}^{\max}\rbrack$ of all possible initial velocities. As we shall see in Section 3.2, AVP-backward is essential for the *bi-directional* version of AVP-RRT.

<!-- chunk {"id": "body-0030", "role": "body", "section": "AVP-backward", "weight": 1.0} -->

It turns out that AVP-backward can be easily obtained by modifying AVP as follows: step A of AVP-backward is the same as in AVP; in step B of AVP-backward, one integrates *backward* from ${\overset{˙}{s}}_{end}^{\min \ast}$ instead of integrating *forward* from ${\overset{˙}{s}}_{beg}^{\max \ast}$; in the bisection search of step C of AVP-backward, one integrates *forward* from $(0,{\overset{˙}{s}}_{test})$ instead of integrating *backward* from$(s_{end},{\overset{˙}{s}}_{test})$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Convex optimization approach", "weight": 1.0} -->

As mentioned in the Introduction, "convex optimization" is another possible approach to TOPP. It is however unclear to us whether one can modify that approach to yield a "convex-optimization-based AVP" other than sampling a large number of $({\overset{˙}{s}}_{start},{\overset{˙}{s}}_{end})$ pairs and running the "convex-optimization-based TOPP" between $(0,{\overset{˙}{s}}_{start})$ and $(s_{end},{\overset{˙}{s}}_{end})$, which would arguably be very slow.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Combining AVP with sampling-based planners", "weight": 1.0} -->

The AVP algorithm presented in Section 2.2 ‣ 2 Propagating admissible velocities along a path ‣ Admissible Velocity Propagation: Beyond Quasi-Static Path Planning for High-Dimensional Robots") is general and can be combined with various iterative path planners. As an example, we detail in Box 2 and illustrate in Figure 5 a planner we call AVP-RRT, which results from the combination of AVP with the standard RRT path planner.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Combining AVP with sampling-based planners", "weight": 1.0} -->

As in the standard RRT, AVP-RRT iteratively constructs a tree $\mathcal{T}$ in the configuration space. However, in contrast with the standard RRT, a vertex $V$ here consists of a triplet ($V$.config, $V$.inpath, $V$.interval) where $V$.config is an element of the configuration space $\mathcal{C}$, $V$.inpath is a path $\mathcal{P} \subset \mathcal{C}$ that connects the configuration of $V$'s parent to $V$.config, and $V$.interval is the interval of reachable velocities at $V$.config, that is, at the end of $V$.inpath.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Combining AVP with sampling-based planners", "weight": 1.0} -->

At each iteration, a random configuration $\mathbf{q}_{rand}$ is generated. The EXTEND routine (see Box 3) then tries to extend the tree $\mathcal{T}$ *towards* $\mathbf{q}_{rand}$ from the closest -- in a certain metric $d$ -- vertex in $\mathcal{T}$. The algorithm terminates when either A newly-found vertex can be connected to the goal configuration (line 10 of Box 2). In this case, AVP guarantees by recursion that there exists a path from $\mathbf{q}_{start}$ to $\mathbf{q}_{goal}$ and that this path is time-parameterizable; After $N_{maxrep}$ repetitions, no vertex could be connected to $\mathbf{q}_{goal}$. In this case, the algorithm returns Failure.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Combining AVP with sampling-based planners", "weight": 1.0} -->

Input: qstart, qgoal Output: A valid trajectory connecting qstart to qgoal or Failure 2: Vstart← NEW_VERTEX 3: Vstart.config ← qstart; Vstart.inpath ← Null; Vstart.interval ← 5: for rep = 1 to Nmaxrep do 6: qrand← RANDOM_CONFIG 7: Vnew← EXTEND(𝒯, qrand) 8: if EXTEND succeeds then 9: ADD_VERTEX(𝒯, Vnew) 10: if CONNECT(Vnew, qgoal) succeeds then 11: return COMPUTE_TRAJECTORY(𝒯, qgoal) Figure 5: Illustration for AVP-RRT. The horizontal plane represents the configuration space while the vertical axis represents the path velocity space. Black areas represent configuration space obstacles. A vertex in the tree is composed of a configuration (blue disks), the incoming path from the parent (blue curve), and the interval of admissible velocities (bold magenta segments).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Combining AVP with sampling-based planners", "weight": 1.0} -->

At each tree extension step, one interpolates a smooth, collision-free path in the configuration space and propagates the interval of admissible velocities along that path using AVP. The fine magenta line shows one possible valid velocity profile (which is guaranteed to exist by AVP) “above” the path connecting qstart and qnew.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Combining AVP with sampling-based planners", "weight": 1.0} -->

Output: A new vertex Vnew or Null 1: Vnear← NEAREST_NEIGHBOR(𝒯, qrand) 2: (𝒫new, qnew)← INTERPOLATE(Vnear, qrand) 4: ${\lbrack{\overset{˙}{s}}_{\min},{\overset{˙}{s}}_{\max}\rbrack}\leftarrow$ AVP(𝒫new, Vnear.interval) 5: if AVP succeeds then 6: Vnew← NEW_VERTEX 7: Vnew.config ← qnew; Vnew.inpath ← 𝒫new; $V_{new}.{{interval}\leftarrow{\lbrack{\overset{˙}{s}}_{\min},{\overset{˙}{s}}_{\max}\rbrack}}$ The other routines are defined as follows: CONNECT($V,\mathbf{q}_{goal}$) attempts at connecting directly $V$ to the goal configuration

<!-- chunk {"id": "body-0038", "role": "body", "section": "Combining AVP with sampling-based planners", "weight": 1.0} -->

$\mathbf{q}_{goal}$, using the same algorithm as in lines 2 to 10 of Box 3, but with the further requirement that the goal velocity is included in the final velocity interval; COMPUTE_TRAJECTORY($\mathcal{T},\mathbf{q}_{goal}$) reconstructs the entire path $\mathcal{P}_{\text{total}}$ from $\mathbf{q}_{start}$ to $\mathbf{q}_{goal}$ by recursively concatenating the $V$.inpath. Next, $\mathcal{P}_{\text{total}}$ is time-parameterized by applying TOPP. The existence of a valid time-parameterization is guaranteed by recursion by AVP.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Combining AVP with sampling-based planners", "weight": 1.0} -->

NEAREST_NEIGHBOR($\mathcal{T},\mathbf{q}$) returns the vertex of $\mathcal{T}$ whose configuration is closest to configuration $\mathbf{q}$ in the metric $d$, see Section 3.2 for a more detailed discussion.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Combining AVP with sampling-based planners", "weight": 1.0} -->

INTERPOLATE($V,\mathbf{q}$) returns a pair $(\mathcal{P}_{new},\mathbf{q}_{new})$ where $\mathbf{q}_{new}$ is defined as follows if $d{(V}$.config,$\mathbf{q}) \leq R$ where $R$ is a user-defined extension radius as in the standard RRT algorithm, then $\mathbf{q}_{new}\leftarrow\mathbf{q}$; otherwise, $\mathbf{q}_{new}$ is a configuration "in the direction of" $\mathbf{q}$ but situated within a distance $R$ of $V$.config (contrary to the standard RRT, it might not be wise to choose a configuration laying exactly on the segment connecting $V$.config and $\mathbf{q}$ since here one has also to take care of $C^{1}$-continuity, see below).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Combining AVP with sampling-based planners", "weight": 1.0} -->

The path $\mathcal{P}_{new}$ is a smooth path connecting $V$.config and $\mathbf{q}_{new}$, and such that the concatenation of $V$.inpath and $\mathcal{P}_{new}$ is $C^{1}$ at $V$.config, see Section 3.2 for a more detailed discussion.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Implementation and variations", "weight": 1.0} -->

As in the standard RRT, some implementation choices influence substantially the performance of the algorithm.: In state-space RRTs, the most critical choice is that of the metric $d$, in particular, the *relative weighting* between configuration-space coordinates and velocity coordinates. In our approach, since the whole interval of valid path velocities is considered, the relative weighting does not come into play. In practice, a simple Euclidean metric on the configuration space is often sufficient. However, in some applications, one may also include the *final orientation* of $V$.inpath in the metric.: In geometric path planners, the interpolation between two configurations is usually done using a straight segment. Here, since one needs to propagate velocities, it is necessary to enforce $C^{1}$-continuity at the junction point. In the examples of Section 4, we used third-degree polynomials to do so.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Implementation and variations", "weight": 1.0} -->

Other interpolation methods are possible: higher-order polynomials, splines, etc. The choice of the appropriate method depends on the application and plays an important role in the performance of the algorithm.: Attempting connection from $K$ nearest neighbors, where $K > 1$ is a judiciously chosen parameter, has been found to improve the performance of RRT. To implement this, it suffices to replace line 2 of Box 3 with a FOR loop that enumerates the $K$ nearest neighbors. Note that this procedure is geared towards reducing the search time, not at improving the trajectory quality as in RRT^∗^, see also below.: After finding a solution trajectory, one can improve its quality (e.g. trajectory duration, trajectory smoothness, etc.), by repeatedly applying the following shortcutting procedure: select two random configurations on the trajectory; interpolate a smooth shortcut path between these two configurations; time-parameterize the shortcut using TOPP; if the time-parameterized shortcut has shorter duration than the initial segment, then replace the latter by the former.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Implementation and variations", "weight": 1.0} -->

Instead of shortcutting, one may also give the trajectory found by AVP-RRT as initial guess to a trajectory optimization algorithm, or implement a re-wiring procedure as in RRT^∗^, which has been shown to be asymptotically optimal in the context of state-based planning (note however that such re-wiring is not straightforward and might require additional algorithmic developments).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Implementation and variations", "weight": 1.0} -->

Another significant benefit of AVP is that one can readily adapt heuristics that have been developed for geometric path planners. We discuss two such heuristics below.: Kuffner and LaValle remarked that growing simultaneously two trees, one rooted at the initial configuration and one rooted at the goal configuration yielded significant improvement over the classical uni-directional RRT. This idea can be easily implemented in the context of AVP-RRT as follows: The start tree is grown normally as in Section 3.1; The goal tree is grown similarly, but using AVP-backward (see Section 2.3) for the velocity propagation step; Assume that one finds a configuration where the two trees are *geometrically* connected. If the forward velocity interval of the start tree and the backward velocity interval of the goal tree have a non-empty intersection at this configuration, then the two trees can be connected *dynamically*.: If two nearby configurations are in the obstacle space but their midpoint $\mathbf{q}$ is in the free space, then most probably $\mathbf{q}$ is in a narrow passage.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Implementation and variations", "weight": 1.0} -->

This idea enables one to find a large number of such configurations $\mathbf{q}$, which is essential in problems involving narrow passages. This idea can be easily implemented in AVP-RRT by simply modifying RANDOM_CONFIG in line 6 of Box 2 to include the bridge test.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Implementation and variations", "weight": 1.0} -->

One can observe from the above discussion that powerful heuristics developed for geometric path planning can be readily used in AVP-RRT, precisely because the latter is built on the idea of path-velocity decomposition. It is unclear how such heuristics can be integrated in other approaches to kinodynamic motion planning such as the trajectory optimization approach discussed in the Introduction.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Examples of applications", "weight": 1.0} -->

As AVP-RRT is based on the classical Time-Optimal Path Parameterization (TOPP) algorithm, it can be applied to any type of systems and constraints TOPP can handle, from double-integrators subject to velocity and acceleration bounds, to manipulator subject to torque limits, to wheeled vehicles subject to balance constraints, to humanoid robots in multi-contact tasks, etc. Furthermore, the overhead for addressing a new problem is minimal: it suffices to reduce the system constraints to the form of inequality (1 ‣ 2 Propagating admissible velocities along a path ‣ Admissible Velocity Propagation: Beyond Quasi-Static Path Planning for High-Dimensional Robots")), and *le tour est joué!* In this section, we present two examples where AVP-RRT was used to address planning problems in which *no quasi-static solution exists*. In the first example, the task consisted in swinging a double pendulum into the upright configuration under severe torque bounds.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Examples of applications", "weight": 1.0} -->

While this example does not fully exploit the advantages associated with path-velocity decomposition (no configuration-space obstacle nor kinematic closure constraint was considered), we chose it since it was simple enough to enable a careful comparison with the usual state-space planning approach. In the second example, the task consisted in transporting a bottle placed on a tray through a small opening using a commercially-available manipulator (6 DOFs). This example demonstrates the full power of path-velocity decomposition: geometric constraints (going through the small opening) and dynamics constraints (the bottle must remain on the tray) could be addressed separately. To the best of our knowledge, this is the first successful demonstration on a non custom-built robot that kinodynamic planning can succeed where quasi-static planning is guaranteed to fail.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Double pendulum with severe torque bounds", "weight": 1.0} -->

We first consider a fully-actuated double pendulum (see Figure 6B), subject to torque limits Such a pendulum can be seen as a 2-link manipulator, so that the reduction to the form of (1 ‣ 2 Propagating admissible velocities along a path ‣ Admissible Velocity Propagation: Beyond Quasi-Static Path Planning for High-Dimensional Robots")) is straightforward, see Pham.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Obstruction to quasi-static planning", "weight": 1.0} -->

Any trajectory that achieves the task must pass through a configuration where $\theta_{1} = {\pi/2}$. Note that the configuration with $\theta_{1} = {\pi/2}$ that requires the smallest torque at the first joint to stay still is ${(\theta_{1},\theta_{2})} = {({\pi/2},\pi)}$. Let then $\tau_{1}^{qs}$ be this smallest torque. It is clear that, if $\tau_{1}^{\max} < \tau_{1}^{qs}$, then *no quasi-static trajectory* can achieve the task.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Obstruction to quasi-static planning", "weight": 1.0} -->

In our simulations, we used the following lengths and masses for the links: $l = 0.2$ m and $m = 8$ kg, yielding $\tau_{1}^{qs} = 15.68$ N$\cdot$m. For information, the smallest torque at the second joint to keep the configuration ${(\theta_{1},\theta_{2})} = {(0,{\pi/2})}$ stationary was $7.84$ N$\cdot$m. We carried experiments in the following scenarii: ${(\tau_{1}^{\max},\tau_{2}^{\max})} \in {\{{},{},{}\}}$ (N$\cdot$m).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Solution using AVP-RRT", "weight": 1.0} -->

Regarding the number of nearest neighbors to consider, we chose $K = 10$. The maximum number of repetitions was set to $N_{maxrep} = 2000$. Random configurations were sampled uniformly in ${\lbrack{- \pi},\pi\rbrack}^{2}$. A simple Euclidean metric in the configuration space was used. Inverse Dynamics computations (required by the TOPP algorithm) were performed using OpenRAVE. We ran 40 simulations for each value of $(\tau_{1}^{\max},\tau_{2}^{\max})$ on a 2 GHz Intel Core Duo computer with 2 GB RAM. The results are given in Table 1 and Figure 6. A video of some successful trajectories are shown at Table 1: Results for the pendulum simulations Figure 6: Swinging up a fully-actuated double pendulum. A typical solution for the case (τ1max, τ2max) = N⋅m, with trajectory duration 1.88 s (see also the attached video). A: The tree in the (θ1, θ2) space. The final path is highlighted in magenta.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Solution using AVP-RRT", "weight": 1.0} -->

B: snapshots of the trajectory, taken every 0.1 s. Snapshots taken near the beginning of the trajectory are lighter. A video of the movement is available at C: Velocity profiles in the $(s,\overset{˙}{s})$ space. The MVC is in cyan. The various velocity profiles (CLC, Φ, Ψ, cf. Section 2.2) are in black. The final, optimal, velocity profile is in dashed blue. The vertical dashed red lines correspond to vertices where 0 is a valid velocity, which allowed a discontinuity of the path tangent at that vertex. D: Torques profiles. The torques for joint 1 and 2 are respectively in red and in blue. The torque limits are in dotted line. Note that, in agreement with time-optimal control theory, at each time instant, at least one torque limit was saturated (the small overshoots were caused by discretization errors).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Comparison with state-space RRT", "weight": 1.0} -->

We compared our implementation of AVP-RRT with the standard state-space RRT including the $K$-nearest-neighbors heuristic ($K$NN-RRT). More complex kinodynamic planners have been applied to low-DOF systems like the double pendulum, in particular those based on locally linearized dynamics. However, such planners require delicate tunings and have not been shown to scale to systems with DOF $\geq$ 4. The goal of the present section is to compare the behavior of AVP-RRT to its RRT counterpart on a low-DOF system. (In particular, we do not claim that AVP-RRT is the best planner for a double pendulum.)

<!-- chunk {"id": "body-0056", "role": "body", "section": "Comparison with state-space RRT", "weight": 1.0} -->

We equipped the state-space RRT with generic heuristics that we tuned to the problem at hand, see Appendix A. In particular, we selected the best number of neighbors $K$ for $K \in {\{ 1,10,40,100\}}$. Figure 7 and Table 2 summarize the results.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Non-prehensile object transportation", "weight": 1.0} -->

Here we consider the non-prehensile (i.e. without grasping) transportation of a bottle, or "waiter motion". Non-prehensile transportation can be faster and more efficient than prehensile transportation since the time-consuming grasping and un-grasping stages are entirely skipped. Moreover, in many applications, the objects to be carried are too soft, fragile or small to be adequately grasped (e.g. food, electronic components, etc.)

<!-- chunk {"id": "body-0058", "role": "body", "section": "Obstruction to quasi-static planning", "weight": 1.0} -->

A plastic milk bottle partially filled with sand was placed (without any fixation device) on a tray. The mass of the bottle was 2.5 kg, its height was 24 cm (the sand was filled up to 16 cm) and its base was a square of size 8 cm $\times$ 8 cm. The tray was mounted as the end-effector of a 6-DOF serial manipulator (Denso VS-060). The task consisted in bringing the bottle from an initial configuration towards a goal configuration, these two configurations being separated by a small opening (see Fig. 8A).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Obstruction to quasi-static planning", "weight": 1.0} -->

For the bottle to remain stationary with respect to the tray, the following three conditions must be satisfied: (Unilaterality) The normal component $f_{n}$ of the reaction force must be non-negative; (Non-slippage) The tangential component $\mathbf{f}_{t}$ of the reaction force must satisfy ${\|\mathbf{f}_{t}\|} \leq {\muf_{n}}$, where $\mu$ is the static friction coefficient between the bottle and the tray. In our experimental set-up, the friction coefficient was set to a high value ($\mu = 1.7$), such that the non-slippage condition was never violated before the ZMP condition; (ZMP) The ZMP of the bottle must lie inside the bottle base.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Obstruction to quasi-static planning", "weight": 1.0} -->

The height of the opening was designed so that, for the bottle to go through the opening, it must be tilted by at least an angle $\theta^{qs}$. However, when the bottle is tilted by that angle, the center of mass (COM) of the bottle projects outside of the bottle base. As the projection of the COM coincides with the ZMP in the quasi-static condition, tilting the bottle by the angle $\theta^{qs}$ thus violates the ZMP condition and as a result, the bottle will tip over. One can therefore conclude that *no quasi-static motion* can bring the bottle through the opening without tipping it over.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Solution using AVP-RRT", "weight": 1.0} -->

We first reduced the three aforementioned conditions to the form of (1 ‣ 2 Propagating admissible velocities along a path ‣ Admissible Velocity Propagation: Beyond Quasi-Static Path Planning for High-Dimensional Robots")). Details of this reduction can be found in Lertkultanon and Pham. We next used the bi-directional version of AVP-RRT presented in Section 3.2. All vertices in the tree were considered for possible connection from a new random configuration, but they were sorted by increasing distance from the new configuration (a simple Euclidean metric in the configuration space was used for the distance computation). As the opening was very small (narrow passage), we made use of the bridge test in order to automatically sample a sizable number of configurations inside or close to the opening. Note that the use of the bridge test was natural thanks to path-velocity decomposition.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Solution using AVP-RRT", "weight": 1.0} -->

Because of the discrepancy between the planned motion and the motion actually executed on the robot (in particular, actual acceleration switches cannot be infinitely fast), we set the safety boundaries to be a square of size 5.5 cm $\times$ 5.5 cm (the actual base size was 8 cm $\times$ 8 cm), which makes the planning problem even harder. Nevertheless, our algorithm was able to find a feasible movement in about 3 hours on a 3.2 GHz Intel Core computer with 3.8 GB RAM (see Fig. 8B--E), and this movement could be successfully executed on the actual robot, see Fig. 9 and the video at Note that the computation time of 3 hours was for a particularly difficult problem instance: if the opening was only 5 cm higher, computation time would be about 2 minutes, see Fig. 8F.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Comparison with OMPL-KPIECE", "weight": 1.0} -->

We were interested in comparing AVP-RRT with a state-of-the-art planner on this bottle-and-tray problem. We chose KPIECE since it is one of the most generic and powerful existing kinodynamic planners. Moreover, a robust open-source implementation exists as a component of the widely-used Open Motion Planning Library (OMPL).

<!-- chunk {"id": "body-0064", "role": "body", "section": "Comparison with OMPL-KPIECE", "weight": 1.0} -->

The methods and results of the comparison are reported in detail in Appendix C. Briefly, we first fine-tuned OMPL-KPIECE on the same 6-DOF manipulator model as above. At this stage, we considered only bounds on velocity and accelerations, the bottle and the tray were ignored for simplicity. Next, we compared AVP-RRT (Python/C++) and OMPL-KPIECE (pure C++, with the best possible tunings obtained previously) in an environment similar to that of Fig. 8. Here, we considered bounds on velocity and accelerations and collisions with the environment. We ran each planner 20 times with a time limit of 600 seconds. AVP-RRT had a success rate of $100\%$ and an average running time of $68.67$ s, while OMPL-KPIECE failed to find any solution in any run. Based on this decisive result, we decided not to try OMPL-KPIECE on the full bottle-and-tray problem.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Comparison with OMPL-KPIECE", "weight": 1.0} -->

These comparison results thus further suggest that planning directly in the state-space, while interesting from a theoretical viewpoint and successful in simulations and/or on custom-built systems, is unlikely to scale to practical high-DOF problems.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have presented a new algorithm, Admissible Velocity Propagation (AVP) which, given a path and an interval of reachable velocities at the beginning of that path, computes exactly and efficiently the interval of valid final velocities. We have shown how to combine AVP with well-known sampling-based geometric planners to give rise to a family of new efficient kinodynamic planners, which we have evaluated on two difficult kinodynamic problems.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Comparison to existing approaches to kinodynamic planning", "weight": 1.0} -->

Compared to traditional planners based on path-velocity decomposition, our planners remove the limitation of quasi-static feasibility, precisely by propagating admissible velocity intervals at each step of the tree extension. This enables our planner to find solutions when quasi-static trajectories are guaranteed to fail, as illustrated by the two examples of Section 4.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Comparison to existing approaches to kinodynamic planning", "weight": 1.0} -->

Compared to other approaches to kinodynamic planning, our approach enjoys the advantages associated with path-velocity decomposition, namely, the separation of the complex planning problem into two simpler sub-problems: geometric and dynamic, for both of which powerful methods and heuristics have been developed.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Comparison to existing approaches to kinodynamic planning", "weight": 1.0} -->

The bottle transportation example in Section 4.2 illustrates clearly this advantage. To address the problem of the narrow passage constituted by the small opening, we made use of the bridge test heuristics -- initially developed for geometric path planners -- which provides a large number of samples inside the narrow passage. It is unclear how such a method could be integrated into the "trajectory optimization" approach for example. Next, to steer between two configurations, we simply interpolated a geometric path -- and can check for collision at this stage -- and then found possible *trajectories* by running AVP. By contrast, in a "state-space planning" approach, it would be difficult -- if not impossible -- to steer exactly between two *states* of the system, which requires for instance solving a two-point boundary value problem. To avoid solving such difficult problems, LaValle and Kuffner; Hsu et al. propose to sample a large number of time-series of random control inputs and to choose the time-series that steers the system the closest to the target state.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Comparison to existing approaches to kinodynamic planning", "weight": 1.0} -->

However, such shooting methods are usually considerably slower than "exact" methods -- which is the case of AVP --, as also illustrated in our simulation study (see Section 4.1 and Appendices B, C).

<!-- chunk {"id": "body-0071", "role": "body", "section": "Class of systems where AVP is applicable", "weight": 1.0} -->

Since AVP is adapted from TOPP, AVP can handle all systems and constraints that TOPP can handle, and only those systems and constraints. Essentially, TOPP can be applied to a path $\mathbf{q}{(s)}$ in the configuration space if the system can track that path at any velocities $\overset{˙}{s}$ and accelerations $\overset{¨}{s}$, subject only to *inequality constraints* on $\overset{˙}{s}$ and $\overset{¨}{s}$. This excludes -- *a priori* -- all under-actuated robots since, for these robots, most of the paths in the configuration space cannot be traversed at all, or at only *one* specific velocity. Bullo and Lynch identified a subclass of under-actuated robots (including e.g. planar 3-DOF manipulators with one passive joint or 3D underwater vehicles with three off-center thrusters) for which one can compute a large subset of paths that can be TOPP-ed (termed "kinematic motions").

<!-- chunk {"id": "body-0072", "role": "body", "section": "Class of systems where AVP is applicable", "weight": 1.0} -->

Investigating whether AVP-RRT can be applied to such systems is the subject of ongoing research.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Class of systems where AVP is applicable", "weight": 1.0} -->

At the other end of the spectrum, redundantly-actuated robots can track most of the paths in their configuration space (again, subject to actuation bounds). The problem here is that, for a given admissible velocity profile along a path, there exists in general an infinity of combinations of torques that can achieve that velocity profile. Pham and Stasse showed how to optimally exploit actuation redundancy in TOPP, which can be adapted straightforwardly to AVP-RRT.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Further remarks on completeness and complexity", "weight": 1.0} -->

The AVP-RRT planner as presented in Section 3 is likely *not probabilistically complete*. We address in more detail in Appendix A the completeness properties of AVP-RRT, and more generally, of AVP-based planners.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Further remarks on completeness and complexity", "weight": 1.0} -->

We now discuss another feature of AVP-based planners that makes them interesting from a complexity viewpoint. Consider a trajectory or a trajectory segment that is "explored" by a state-space planning or a trajectory optimization method -- either in one extension step for the former, or in an iterative optimization step for the latter. If one considers the *underlying path* of this trajectory, one may argue that these methods are exploring only *one* time-parameterization of that path, namely, that corresponding to the trajectory at hand. By contrast, for a given path that is "explored" by AVP, AVP precisely explores *all* time-parameterizations of that path, or in other words, the whole *"fiber bundle"* of path velocities above the path at hand -- at a computation cost only slightly higher than that of checking *one* time-parameterization (see Section 2.3). Granted that path velocity encodes important information about possible violations of the dynamics constraints as argued in the Introduction, this full and free (as in free beer) exploration enables significant performance gains.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Future works", "weight": 1.0} -->

As just mentioned, we have recently extended TOPP to redundantly-actuated systems, including humanoid robots in multi-contact tasks. This enables AVP-based planners to be applied to multi-contact planning for humanoid robots. In this application, the existence of kinematic closure constraints (the parts of the robot in contact with the environment should remain fixed) makes path-velocity decomposition highly appealing since these constraints can be handled by a kinematic planner independently from dynamic constraints (torque limits, balance, etc.) In a preliminary experiment, we have planned a non-quasi-statically-feasible but dynamically-feasible motion for a humanoid robot. Going further, we are currently investigating how AVP-based planners can enable existing quasi-static multi-contact planning methods to discover truly dynamic motions for humanoid robots with multiple contact changes.
