<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Convex Optimization Approach to Smooth Trajectories for Motion Planning with Car-Like Robots

Topics include Smooth trajectory, Car-like, Optimization, Heuristic, Optimal, Real-time, Smoothing, Path planning, Convex optimization, Self driving, Bicycle model, Bubble, Ground vehicles, Collision-free, Vehicle dynamics, Speed profile.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

CES takes a reference trajectory as input, then re-plans both the path shape and speed profile within a sequence of obstacle-free "bubble" regions along the trajectory using convex programming. This makes it a powerful post-processor, reportedly outperforming traditional path shortcutting heuristics as well as elastic band approaches.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In the recent past, several sampling-based algorithms have been proposed to compute trajectories that are collision-free and dynamically-feasible. However, the outputs of such algorithms are notoriously jagged. In this paper, by focusing on robots with car-like dynamics, we present a fast and simple heuristic algorithm, named Convex Elastic Smoothing (CES) algorithm, for trajectory smoothing and speed optimization. The CES algorithm is inspired by earlier work on elastic band planning and iteratively performs shape and speed optimization. The key feature of the algorithm is that both optimization problems can be solved via convex programming, making CES particularly fast. A range of numerical experiments show that the CES algorithm returns high-quality solutions in a matter of a few hundreds of milliseconds and hence appears amenable to a real-time implementation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The problem of planning a collision-free and dynamically-feasible trajectory is fundamental in robotics, with application to systems as diverse as ground, aerial, and space vehicles, surgical robots, and robotic manipulators. A common strategy is to decompose the problem in steps of computing a collision-free, but possibly highly-suboptimal or not even dynamically-feasible trajectory, smoothing it, and finally reparameterizing the trajectory so that the robot can execute it. In other words, the first step provides a strategy that explores the configuration space efficiently and decides "where to go," while the subsequent steps provide a refined solution that specifies "how to go."

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The first step is often accomplished by running a sampling-based motion planning algorithm, such as PRM or RRT. While these algorithms are very effective for quickly finding collision-free trajectories in obstacle-cluttered environments, they often return jerky, unnatural paths. Furthermore, sampling-based algorithms can only handle rather simplified dynamic models, due to the complexity of exploring the state space while retaining dynamic feasibility of the trajectories. The end result is that the trajectory returned by sampling-based algorithms are characterized by jaggedness and are often dynamically-infeasible, which requires the subsequent use of algorithms for trajectory smoothing and reparametrization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Accordingly, the objective of this paper is to design a fast and simple *heuristic* algorithm for trajectory smoothing and reparametrization that is amenable to a real-time implementation, with a focus on mobile robots, in particular robotic cars. Specifically, we seek an algorithm that within a few hundreds of milliseconds can turn a jerky trajectory returned by a sampling-based motion planner into a smooth, speed-optimized trajectory that fulfills strict dynamical constraints such as friction, bounded acceleration, or turning radius limitations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A Literature Review", "weight": 1.0} -->

The problem of smoothing a trajectory returned by a sampling-based planner is not new and has been studied since the introduction of sampling-based algorithms. For planning problems that do not involve the fulfillment of dynamic constraints (e.g., limited turning radius), efficient smoothing algorithms are already available. In this case, the most widely applied method is the Shortcut heuristic, because of its effectiveness and simple implementation. In a typical implementation, this algorithm considers two random configurations along the trajectory. If these two configurations can be connected with a new shorter trajectory (as computed via a local planner), then the original connection is replaced with the new one.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Literature Review", "weight": 1.0} -->

For planning problems with dynamic constraints, however, the situation is more contentious. While several works have studied sampling-based algorithms for kinodynamic planning, relatively few works have addressed the issues of trajectory smoothing with dynamic constraints. Broadly speaking, current techniques can be classified into two categories, namely shortcut methods and optimization-based methods. Shortcut methods strive to emulate the Shortcut algorithm in a kinodynamic context. Specifically, jerky portions of a path are replaced with curve segments such as parabolic arcs, clothoids, Bézier curves, Catmull-Rom splines, cubic B-splines, or Dubins curves. Such methods are rather fast (they usually complete in a few seconds), but handle dynamic constraints only implicitly, for example, by constraining the curvature of the trajectories and/or ensuring $C^{2}$ continuity. Also, they usually do not involve speed optimization along the computed trajectory. Notably, two of the main teams in the DARPA Grand Challenge, namely team Stanford and team CMU, applied shortcut methods as their smoothing procedure.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A Literature Review", "weight": 1.0} -->

In contrast, optimization-based methods handle dynamic constraints explicitly, as needed, for example, for high-performance mobile vehicles. Two common approaches are gradient-based methods and elastic bands or elastic strip planning, which model a trajectory as an elastic band. These works, however, are mostly geared toward robotic manipulators, may still require several seconds to find a solution, and generally do not address speed optimization along the trajectory.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-B Statement of Contributions", "weight": 1.0} -->

In this paper, leveraging recent strides in the field of convex optimization, we design a novel algorithm, named Convex Elastic Smoothing (CES) algorithm, for trajectory smoothing and speed optimization. The focus is on mobile robots with car-like dynamics. Our algorithm is inspired by the elastic band approach, in that we identify a collision-free "tube" around the trajectory returned by a sampling-based planner, within which the trajectory is "stretched" and speed is optimized. The stretching and speed optimization steps rely on convex optimization. In particular, the stretching step draws inspiration, while the speed optimization step is essentially an implementation of the algorithm. In contrast, our algorithm uses convex optimization for the stretching process, performs speed optimization, and handles a variety of constraints (e.g., friction) that were not considered. As compared to, our algorithm handles more general workspaces and removes the assumption of a constant speed.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-B Statement of Contributions", "weight": 1.0} -->

Specifically, the CES algorithm divides the trajectory smoothing process into two steps: given a fixed velocity profile along a reference trajectory, optimize the shape of the trajectory, and given a fixed shape for the trajectory, optimize the speed profile along the trajectory. We show that each of the two steps can be readily solved as a convex optimization problem. The two steps are then repeated until a termination criterion is met (e.g., timeout). In this paper, the initial reference trajectory is computed by running the differential FMT^∗^ algorithm, a kinodynamic variant of the FMT^∗^ algorithm. Numerical experiments on a variety of scenarios show that in a few *hundreds of milliseconds* the CES algorithm outputs a "high-quality" trajectory, where the jaggedness of the original trajectory is eliminated and speed is optimized. Coupled with differential FMT^∗^, the CES algorithm is able to find high-quality solutions to rather complicated planning problems in well under a second, which appears promising for a real-time implementation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-B Statement of Contributions", "weight": 1.0} -->

We mention that the reference trajectory used as an input to the CES algorithm can be the output of any sampling-based motion planner, and indeed of any motion planning algorithm. In particular, the CES algorithm appears to perform well even when the reference trajectory is not collision-free or does not fulfill some of the dynamic constraints (see Section IV for more details). Also, while in this paper we mostly focus on vehicles with second-order, car-like dynamics, the CES algorithm can be generalized to a variety of other mobile systems such as aerial vehicles and spacecraft.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-C Organization", "weight": 1.0} -->

This paper is structured as follows. In Section II we formally state the problem we wish to solve. In Section III we present the CES algorithm, a novel algorithm for trajectory smoothing that relies on convex optimization and runs in a few hundreds of milliseconds. In Section IV we present results from numerical experiments highlighting the speed of the the CES algorithm and the quality of the returned solutions. Finally, in Section V, we draw some conclusions and discuss directions for future work.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Let $\mathcal{W} \subset {\mathbb{R}}^{2}$ denote the two-dimensional work space for a car-like vehicle. Let $\mathcal{O} = {\{ O_{1},O_{2},\ldots,O_{m}\}}$, with $O_{i} \subset \mathcal{W}$, $i = {1,\ldots,m}$, denote the set of obstacles. For simplicity, we assume that the obstacles have polygonal shape. In this paper we primarily focus on a unicycle dynamic model for the vehicle. Extensions to more sophisticated car-like models are discussed in Section IV. Specifically, following, let $\mathbf{q} \in \mathcal{W}$ represent the position of the vehicle, and $\overset{˙}{\mathbf{q}}$ and $\overset{¨}{\mathbf{q}}$ its velocity and acceleration, respectively.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

We consider a non-drifting and non-reversible car model so that the heading of the vehicle is the same as the direction of the instantaneous velocity vector, and we denote by $\phi{(\overset{˙}{\mathbf{q}})}$ the mapping from vehicle's speed to its heading. The control input $\mathbf{u} = {\lbrack u^{long},u^{lat}\rbrack}$ is two-dimensional, with the first component, $u^{long}$, representing longitudinal force and the second component, $u^{lat}$, representing lateral force. The dynamics of the vehicle are given by

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

where $m$ is the vehicle's mass, see Figure 1. We consider a friction circle constraint for $\mathbf{u}$, namely

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

where $\mu$ is the friction coefficient and $g$ is the gravitational acceleration (in this paper, norms should be interpreted as 2-norms). The longitudinal force is assumed to be upper bounded as

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

where ${\overline{U}}^{long} \in {\mathbb{R}}_{> 0}$ encodes the force limit from the wheel drive. Finally, we assume a minimum turning radius $R_{\min}$ for the vehicle, which, in turn, induces a constraint on the lateral force according to

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The minimum turning radius ($R_{\min}$) depends on specific vehicle parameters such as wheelbase and maximum steering angle for steering wheels.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Some comments are in order. First, the unicycle model assumes that the heading of the vehicle is the same as the direction of the instantaneous velocity vector. This is a reasonable assumption in most practical situations, but becomes a poor approximation at high speeds when significant under-steering takes place, or at extremely low speeds when the motion is determined by Ackermann steering geometry. We will show, however, that the results presented in this paper can be extended to more complex car models, e.g., half-car models, by leveraging differential flatness of the dynamics. Second, we assume that the actual control inputs such as steering and throttle opening angles can be mapped to $\mathbf{u}$ via a lower-level control algorithm. This is indeed true for most ground vehicles, see, e.g.,. Third, the friction circle model captures the dependency between lateral and longitudinal forces in order to prevent sliding. Fourth, constraint might yield unbounded speeds. This issue could be addressed by conservatively choosing a smaller value of ${\overline{U}}^{long}$ that guarantees an upper bound of the achievable speed within the planning distance.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

An alternative formulation is to set a limit on the total traction power ${u^{long}{\|\overset{˙}{\mathbf{q}}\|}} \leq W$, where $W$ denotes the maximum power provided by the engine. This form is closer to the real constraint on traction force, but it makes the constraint non-convex -- this is a topic left for future research. Finally, the model -, with minor modifications, can be applied to a variety of other vehicles and robotic systems, e.g., spacecraft, robotic manipulators, and aerial vehicles. Hence, the algorithm presented in this paper may be applied to a rather large class of systems -- this is a topic left for future research.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

We are now in a position to state the problem we wish to solve in this paper. Consider a collision-free *reference trajectory* computed, for example, by running a sampling-based motion planner. Let this trajectory be discretized into a set of waypoints $\mathcal{P}:={\{ P_{0},P_{1},\ldots,P_{n}\}}$, where, by construction, $P_{i} \in {\mathcal{W} \smallsetminus \mathcal{O}}$ for $i = {1,\ldots,n}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The goal is to design a heuristic *smoothing algorithm* that uses the information about the vehicle's model -, obstacle set $\mathcal{O}$, and (discretized) reference trajectory $\mathcal{P}$ to compute a dynamically-feasible (with respect to model -), collision-free, and smooth trajectory that goes from $P_{0}$ to $P_{n}$ and has an optimized speed profile, see Figure 1. Our proposed algorithm is named CES and is presented in the next section.

<!-- chunk {"id": "body-0024", "role": "body", "section": "The CES Algorithm", "weight": 1.0} -->

At a high level, the CES algorithm performs the following operations. First, a sequence of "bubbles" is placed along the reference trajectory in order to identify a region of the workspace that is collision free. Such a region can be thought of as a collision-free "tube" within which the reference trajectory, imagined as an elastic band, can be stretched so as to obtain a smoother trajectory. Assuming that a speed profile along the reference trajectory is given, such stretching procedure can be cast as a convex optimization problem, as it will be shown in Section III-B ‣ III The CES Algorithm ‣ A Convex Optimization Approach to Smooth Trajectories for Motion Planning with Car-Like Robots"). Furthermore, optimizing the speed profile along a stretched trajectory can also be cast as a convex optimization problem. However, jointly stretching a trajectory and optimizing the speed profile is a non-convex problem. Hence, the CES algorithm proceeds by alternating trajectory stretching and speed optimization. Simulation results, presented in Section IV, show that such a procedure is amenable to a real-time implementation and yields suboptimal, yet high-quality trajectories. Our CES algorithm is inspired by the elastic band and bubble method.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The CES Algorithm", "weight": 1.0} -->

The work, however, mostly focuses on geometric (i.e., without differential constraints) planning, and does not consider speed optimization, as opposed to our problem setup.

<!-- chunk {"id": "body-0026", "role": "body", "section": "The CES Algorithm", "weight": 1.0} -->

In the remainder of this section we present the different steps of the CES algorithm, namely, bubble generation, elastic stretching and speed optimization. Finally the overall CES algorithm is presented.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Bubble Generation", "weight": 1.0} -->

The first step is to compute a sequence of bubbles, one for each waypoint $P_{i}$, so as to identify a collision-free tube along the reference trajectory for subsequent optimization. Since the problem is two-dimensional, each bubble is indeed a circle. As discussed, extensions to systems in higher dimensions (e.g., airplanes or quadrotors) are possible, but are left for future research. The bubble generation algorithm is shown in Algorithm 1.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A Bubble Generation", "weight": 1.0} -->

0 Reference trajectory 𝒫, obstacle set 𝒪, bubble bounds rl and ru
Algorithm 1 Bubble generation

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Bubble Generation", "weight": 1.0} -->

Let $\mathcal{B}_{i}$ denote the bubble associated with waypoint $P_{i}$, $i = {1,\ldots,n}$, and $A_{i}$ and $r_{i}$ denote, respectively, its center and radius. According to this notation, $\mathcal{B}_{i} = \left. \{{x \in \mathcal{W}} \middle| {{\|{x - A_{i}}\|} \leq r_{i}}\} \right.$. For each waypoint $P_{i}$, Algorithm 1 attempts to compute a bubble such that: its radius is upper bounded by $r_{u} \in {\mathbb{R}}_{> 0}$, *whenever possible*, its radius is no less than $r_{l} \in {\mathbb{R}}_{> 0}$, and its center is as close as possible to $P_{i}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Bubble Generation", "weight": 1.0} -->

The role of the upper bound $r_{u}$ is to limit the smoothing procedure within a relatively small portion of the workspace, say 10% (in other words, to make the optimization "local"). In turn, the minimum bubble radius $r_{l}$ is set according to the maximum distance between adjacent waypoints, so that every bubble overlaps with its neighboring bubbles and the placement of new waypoints for trajectory stretching (see Section III-B ‣ III The CES Algorithm ‣ A Convex Optimization Approach to Smooth Trajectories for Motion Planning with Car-Like Robots")) does not have any "gaps".

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Bubble Generation", "weight": 1.0} -->

First, in lines -, the algorithm checks whether $P_{i}$ is "too close" to the center of bubble $\mathcal{B}_{i - 1}$. If this is the case, bubble $\mathcal{B}_{i}$ is made equal to bubble $\mathcal{B}_{i - 1}$. Otherwise, the algorithm considers as candidate center for bubble $\mathcal{B}_{i}$ the waypoint $P_{i}$ (that is collision-free) and computes, via function GenerateBubble($P_{i}$), the largest bubble centered at $P_{i}$ that is collision-free (with maximum radius $r_{u}$), see lines -. For rectangular-shaped obstacles, this is a straightforward geometrical procedure. If the obstacles have more general polygonal shapes, a bisection search is performed with respect to the bubble radius.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Bubble Generation", "weight": 1.0} -->

Should the resulting radius be lower than the threshold $r_{l}$, an attempt is made to translate $A_{i}$ so that a larger (collision-free) bubble can be placed, lines -. Specifically, function $\text{TranslateBubble}{(A_{i},r_{i})}$ first identifies the edge of the obstacle closest to $A_{i}$ (recall that the obstacles are assumed of polygonal shape). Then, the outward normal direction to the edge is computed and the center of the bubble is moved along such direction until a ball of radius $r_{l}$ can be placed. Should this not be possible, then $\text{TranslateBubble}{(A_{i},r_{i})}$ returns the ball of largest radius among the balls whose centers lie on the aforementioned normal direction.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A Bubble Generation", "weight": 1.0} -->

By construction, the bubble regions are collision-free and represent the feasible space for the placement of new optimized waypoints during the elastic stretching process. Note that in some cases trajectories connecting points in adjacent bubbles may be in collision with obstacles, as shown in Figure 2. This issue is mitigated in practice by considering a "large enough" number of reference waypoints (possibly adding them iteratively) and/or inflating the obstacles. A principled way to select the number of waypoints would rely on a reachability analysis for the unicycle model -. However, to minimize computation time, we rely on a heuristic choice for the waypoint number. Specifically, the spacing between the waypoints is roughly equal to a quarter of the car length.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B Elastic Stretching (aka Shape Optimization)", "weight": 1.0} -->

The key insight of the elastic stretching procedure is to view a trajectory as an elastic band, with $n$ nodal points whose positions can be adjusted within the respective (collision-free) bubbles. Such nodal points represent the new waypoints for the smoothed trajectory, which replace the original waypoints in $\mathcal{P}$. Within this perspective, the dynamic constraints on the shape of a trajectory are mimicked by the bending stiffness of the band.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Elastic Stretching (aka Shape Optimization)", "weight": 1.0} -->

Specifically, consider Figure 4 ‣ III The CES Algorithm ‣ A Convex Optimization Approach to Smooth Trajectories for Motion Planning with Car-Like Robots"). Let $Q_{k}$ and $Q_{k + 1}$ be points, respectively, in bubbles $k$ and $k + 1$, with $k = {1,\ldots,{n - 1}}$. We consider an *artificial* tensile force $\mathbf{F}_{k}$ between $Q_{k}$ and $Q_{k + 1}$ given by

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B Elastic Stretching (aka Shape Optimization)", "weight": 1.0} -->

Accordingly, the balancing force at point $Q_{k}$, $k = {1,\ldots,n}$ is

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-B Elastic Stretching (aka Shape Optimization)", "weight": 1.0} -->

As, the physical interpretation is a series of springs between the bubbles. From a geometric standpoint, the balancing force $\mathbf{N}_{k}$ captures curvature information along a trajectory. Note that if all balance forces are equal to zero, the trajectory is a straight line, which, clearly, has "ideal smoothness." To smooth a trajectory, the goal is then to place new waypoints $Q_{1},\ldots,Q_{n}$ within the bubbles so as to minimize the sum of the norms of the balance forces subject to constraints due to the vehicle's dynamics. In this way, the trajectory is "bent" as little as possible in order to avoid collisions with obstacles.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-B Elastic Stretching (aka Shape Optimization)", "weight": 1.0} -->

The constraints for the placement of the new waypoints rely on a number of approximations to ensure convexity of the optimization problem. Specifically, assume the longitudinal force $u_{k}^{long}$ and velocity $\mathbf{v}_{\mathbf{k}}$ are given at each waypoint in $\mathcal{P}$ (their optimization will be discussed in the next section). We define $R_{k}$ as the instantaneous turning radius for the car at the $k$th waypoint. The lateral acceleration $\mathbf{a}^{lat}$ for waypoints $Q_{k}$, $k = {2,\ldots,{n - 1}}$ can be upper bounded as

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-B Elastic Stretching (aka Shape Optimization)", "weight": 1.0} -->

Lastly, to make the above inequality a quadratic constraint in the $Q_{k}$'s variables, we approximate the length of each *band* $Q_{k + 1} - Q_{k}$ as the average length $d$ along the reference trajectory, i.e.,

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-B Elastic Stretching (aka Shape Optimization)", "weight": 1.0} -->

Note that the minimization of $\|\mathbf{N}_{k}\|$ as the optimization objective inherently reduces the non-uniformity of the lengths of each *band*, which justifies the above approximation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-B Elastic Stretching (aka Shape Optimization)", "weight": 1.0} -->

In summary, we obtain the *friction* constraint

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-B Elastic Stretching (aka Shape Optimization)", "weight": 1.0} -->

Also, again leveraging equation (7 ‣ III The CES Algorithm ‣ A Convex Optimization Approach to Smooth Trajectories for Motion Planning with Car-Like Robots")), we obtain the *turning radius* constraint

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-B Elastic Stretching (aka Shape Optimization)", "weight": 1.0} -->

This is a convex optimization problem with quadratic objective and quadratic constraints (QCQP), where the decision variables are the intermediate waypoints $Q_{k}$, $k = {3,\ldots,{n - 2}}$, which can be placed anywhere within the collision-free regions $\{\mathcal{B}_{3},\ldots,\mathcal{B}_{n - 2}\}$,

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-B Elastic Stretching (aka Shape Optimization)", "weight": 1.0} -->

Note that any feasible solution to the above QCQP, output as a sequence of discrete waypoints, represents a continuous-time trajectory satisfying the unicycle model -. This full trajectory may be recovered by interpolating between adjacent waypoints $Q_{k}$,$Q_{k + 1}$ using circular arcs centered at the intersection of $\mathbf{v}_{k}^{\perp},\mathbf{v}_{k + 1}^{\perp}$, or a straight line if the two velocity vectors are parallel. The speed profile along this continuous trajectory may be taken as piecewise linear, and the discrete constraints (8 ‣ III The CES Algorithm ‣ A Convex Optimization Approach to Smooth Trajectories for Motion Planning with Car-Like Robots")) and (9 ‣ III The CES Algorithm ‣ A Convex Optimization Approach to Smooth Trajectories for Motion Planning with Car-Like Robots")) ensure that the continuous constraints - are satisfied. The quality of such trajectories will be investigated in Section IV.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-C Speed Optimization", "weight": 1.0} -->

The speed optimization over a fixed trajectory relies on the convex optimization algorithm presented. The inputs to this algorithm are a sequence of waypoints $\{ Q_{1},\ldots,Q_{n}\}$ (representing the trajectory to be followed), the friction coefficient $\mu$ for the friction circle constraint in equation, and the maximum traction force ${\overline{U}}^{long}$ defined in equation. The outputs are the sequence of velocity vectors $\{\mathbf{v}_{1},\ldots,\mathbf{v}_{n}\}$ and the sequence of longitudinal control forces $\{ u_{1}^{long},\ldots,u_{n}^{long}\}$, one for each waypoint $Q_{k}$, $k = {1,\ldots,n}$. We refer the reader to for details about the algorithm.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-D Overall Algorithm", "weight": 1.0} -->

The CES algorithm alternates between elastic stretching (Section III-B ‣ III The CES Algorithm ‣ A Convex Optimization Approach to Smooth Trajectories for Motion Planning with Car-Like Robots")) and speed optimization (Section III-C), until a given tolerance on length reduction, traversal time reduction, or a timeout condition are met. Note that at iteration $i \geq 2$, the elastic stretching algorithm should use as estimate for the average band length the quantity

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-D Overall Algorithm", "weight": 1.0} -->

where the $Q_{k}^{\lbrack{i - 1}\rbrack}$'s are the waypoints computed at iteration $i - 1$. According to our discussion in Section III-B ‣ III The CES Algorithm ‣ A Convex Optimization Approach to Smooth Trajectories for Motion Planning with Car-Like Robots"), at iteration $i = 1$ one should set $Q_{k}^{\lbrack 0\rbrack} = P_{k}$, for $k = {1,\ldots,n}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this section we investigate the effectiveness of the CES algorithm along two main dimensions: quality of the smoothed trajectory, measured in terms of traversal time reduction with respect to the reference trajectory, and computation time. We consider three sets of experiments. In the first set, we consider 24 random mazes with rectangular-shaped obstacles, similar to the example in Figure 3. The reference trajectory is computed by running the differential FMT^∗^ algorithm. In the second set, to test the robustness of the algorithm, we consider a scenario where the reference trajectory is computed disregarding the vehicle's dynamics. This could be the case when, to minimize computation time as much as possible, the use of a motion planner is avoided. Finally, we consider a scenario where a robotic car is modeled according to a more sophisticated bicycle (equivalently, half-car) model. The reference trajectory is computed by running differential FMT^∗^ on the unicycle model -. By leveraging the differential flatness of the bicycle model, the CES algorithm is then applied to the trajectory returned by differential FMT^∗^ (computed on a different model).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

This scenario represents the typical case whereby one seeks to run a motion planner on a simpler model of a vehicle, and then a smoothing algorithm on a more refined model. Furthermore, this scenario shows how to apply the CES algorithms to vehicle models more general than -. For all scenarios, the algorithm is stopped whenever the traversal time at the current iteration is no longer reduced with respect to the previous iteration. For the bubble generation method, we chose $r_{u} = {10m}$ and $r_{l} = {1m}$, consistent with the workspace dimensions discussed below.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

All numerical experiments were performed on a computer with an Intel(R) Core(TM) i7-3632QM, 2.20GHz processor and 12GB RAM. The CES algorithm was implemented in Matlab with an interface to FORCES Pro for elastic stretching and MTSOS for speed optimization.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-A Random Mazes", "weight": 1.0} -->

In this scenario the workspace is a ${{100m} \times 100}m$ square with rectangular-shaped obstacles randomly placed within (the obstacle coverage was roughly 50%). The parameters for the model in equations - are $m = 833$ $kg$, $\mu = 0.8$, and ${\overline{U}}^{long} = 0.5$ $\mumg$. The reference trajectories, computed via differential FMT^∗^ by using 1,000 samples, were discretized into 257 waypoints with an average segment length equal to $0.56$ $m$. On average, each iteration (consisting of bubble generation, shape optimization, and speed optimization) required 119 ms, with a standard deviation of 14 ms. Specifically, the bubble generation algorithm required, on average, 26ms. The shape optimization algorithm required 74 ms. Finally, the speed optimization required 19 ms.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-A Random Mazes", "weight": 1.0} -->

A typical smoothed trajectory is portrayed in Figure 5. The traversal time reduction, which is computed according to the formula $\frac{t_{initial} - t_{final}}{t_{initial}} \cdot {100\%}$, ranges from a minimum of 0.2% to a maximum of 18%, with the average value being $3.54\%$. Figure 5 shows the smoothed trajectory for one of the 24 random mazes. We note that, apart from the benefit of reduction of traversal time, a smoothed trajectory may be easier to track for a lower-level controller.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-B Lane Changing", "weight": 1.0} -->

For this scenario, we consider a road lane 50 $m$ long with rectangular-shaped obstacles in it. The parameters for the model in equations - are $m = {1,725}$ $kg$, $\mu = 0.5$, and ${\overline{U}}^{long} = 0.3$ $\mumg$. The reference trajectory is generated by simply computing the center line of the collision-free "tube" along the road. This corresponds to the case where, to minimize computation time as much as possible, a reference trajectory is computed disregarding vehicle's dynamics. Figure 6 shows the smoothed trajectory and speed profile. The computation time was $100$ ms. This scenario illustrates that algorithm CES can also smooth reference trajectories that are not dynamically-feasible. Of course, in this case the traversal time for the smoothed trajectory is longer, due to the dynamic constraints.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-C Smoothing with Bicycle Model", "weight": 1.0} -->

In this scenario, we assume a more sophisticated model for the vehicle, namely a half-car (or bicycle) model, see Figure 7. This model is widely used when local vehicle states such as sideslip angle and yaw rate are of primary interest. In Figure 7, $\mathbf{p}_{cg}$ denotes the center of gravity (CG) of the car, $\psi$ denotes vehicle's orientation, and $v_{x}$ and $v_{y}$ denote components of speed $\mathbf{v}$ in a body-fixed axis system. Also, $l_{f}$ and $l_{r}$ denote the distances from the CG to the front and rear wheels, respectively. Finally, $F_{\alpha\beta}$, with ${\alpha \in {\{ f,r\}}},{\beta \in {\{ x,y\}}}$ denotes the frictional forces of front and rear wheels.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-C Smoothing with Bicycle Model", "weight": 1.0} -->

The control input is represented by the triple $\zeta = {\lbrack\delta,s_{fx},s_{rx}\rbrack}$, where $\delta$ denotes the steering angle of the front wheel, and $s_{fx}$ and $s_{rx}$ denote the longitudinal slip angles of the front and rear tires, respectively. See for more details. Referring to Figure 7, the position $\mathbf{p}_{co}$ can be used as a *differentially flat output*. Specifically, let $m$ be the mass of the vehicle, $I_{z}$ the yaw moment of inertia, and $l_{co}:={{I_{z}/m}l_{r}}$. One can show that

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-C Smoothing with Bicycle Model", "weight": 1.0} -->

where $R{( \cdot )}$ is the 2D rotation matrix and $\mathbf{u} = {\lbrack u^{long},u^{lat}\rbrack}$ is the flat input comprising longitudinal force $u^{long}$ and latitudinal force $u^{lat}$. Note that the flat dynamics are formally identical to those of the unicycle model -. By leveraging differential flatness, the idea is then to smooth a trajectory in the flat output space and then map the flat input $\mathbf{u}$ to the input $\zeta = {\lbrack\delta,s_{fx},s_{rx}\rbrack}$. Constraints for the flat input $\mathbf{u}$ take the same form as in equations - -- the details can be found.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-C Smoothing with Bicycle Model", "weight": 1.0} -->

When mapping $\mathbf{u}$ into $\lbrack\delta,s_{fx},s_{rx}\rbrack$, under a no-drift assumption, only two real inputs can be uniquely determined, while the third is effectively a "degree of freedom," see \[31, Section II\]. In this paper, we consider as degree of freedom the real input $s_{rx}$. Its value is set equal to the solution of an optimization problem aimed at minimizing the tracking error with respect to the trajectory obtained with the flat input $\mathbf{u}$ (the tracking error is due to the no-drift assumption).

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-D Elastic Stretching Moose Test", "weight": 1.0} -->

In order to study in isolation the behavior of the Elastic Stretching algorithm, which is one of the main contributions of this paper, we compare our result with a trajectory consisting of clothoid splines. We note that the objective in the shape optimization step is not simply minimum length (which, for a unicycle model, produces paths consisting only of segments with maximum or zero curvature ), but instead encodes a notion of minimum overall curvature more compatible with dynamic considerations and speed optimization. To simplify the problem for finding a optimal solution with clothoid splines, we assume a constant vehicle speed along the trajectory. Fig. 10(a) illustrates a scenario of a simple Moose test (S shape turn). Here we consider a turning radius lower bound of $5m$, and an upper bound on the path curvature rate of change of $1m^{- 1}s^{- 1}$. Fig. 10(b) shows the piecewise linear curvature profile for the clothoid trajectory. The results of the Elastic Stretching approach and the clothoid trajectory are very close in this illustrative example, with an error of $0.17\%$ on the total path length.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-E Discussion", "weight": 1.0} -->

Overall, the above numerical experiments show three major trends. First, the smoothed trajectory often results in a noticeable length and traversal time reduction and, in general, a sequence of waypoints that may be easier to track for a lower-level controller. Second, the CES algorithm appears robust with respect to the model used to generate the initial reference trajectory. This is a fundamental property, as in practice one would use a motion planner on a simpler model (e.g., unicycle), and then run a smoothing algorithm with a more sophisticated model. Third, computation times are consistently below one second and in general appear compatible with a real-time implementation.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-E Discussion", "weight": 1.0} -->

(b) Curvature profile of the clothoid trajectory

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper we presented a novel algorithm, Convex Elastic Smoothing, for trajectory smoothing which alternates between shape and speed optimization. We showed that both optimization problems can be solved via convex programming, which makes CES particularly fast and amenable to a real-time implementation.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusions", "weight": 1.0} -->

This paper leaves numerous important extensions open for further research. First, it is of interest to extend the CES algorithm to other dynamic systems, such as aerial vehicles or spacecraft. Second, we plan to investigate more thoroughly the robustness of the algorithm when the reference trajectory is not collision-free or dynamically-feasible and the "typical" factor of suboptimality for a number of representative scenarios. Third, for shape optimization, this paper considered smoothness as the objective function. It is of interest to consider alternative objectives, which, for example, could reproduce the trajectories performed by race car drivers (such trajectories may involve significant curvature variations). Fourth, in an effort to make the proposed algorithm "trustworthy," we plan to characterize upper bounds for computation times under suitable assumptions on the obstacle space. Finally, we plan to deploy the CES algorithm on real self-driving cars.
