<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimization-Based Collision Avoidance

Topics include Collision avoidance, Trajectory optimization, Autonomous vehicles, Nonlinear optimization, Augmented Lagrangian.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents an optimization-based collision avoidance formulation using differentiable signed distance functions. Optimization problems are solved with general nonlinear solver IPOPT. Proposes using A* for warm-starting.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a novel method for reformulating non-differentiable collision avoidance constraints into smooth nonlinear constraints using strong duality of convex optimization. We focus on a controlled object whose goal is to avoid obstacles while moving in an n-dimensional space. The proposed reformulation does not introduce approximations, and applies to general obstacles and controlled objects that can be represented in an n-dimensional space as the finite union of convex sets. Furthermore, we connect our results with the notion of signed distance, which is widely used in traditional trajectory generation algorithms. Our method can be used in generic navigation and trajectory planning tasks, and the smoothness property allows the use of general-purpose gradient- and Hessian-based optimization algorithms. Finally, in case a collision cannot be avoided, our framework allows us to find "least-intrusive" trajectories, measured in terms of penetration. We demonstrate the efficacy of our framework on a quadcopter navigation and automated parking problem, and our numerical experiments suggest that the proposed methods enable real-time optimization-based trajectory planning problems in tight environments. Source code of our implementation is provided at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Maneuvering autonomous systems in an environment with obstacles is a challenging problem that arises in a number of practical applications including robotic manipulators and trajectory planning for autonomous systems such as self-driving cars and quadcopters. In almost all of those applications, a fundamental feature is the system's ability to avoid collision with obstacles which are, for example, humans operating in the same area, other autonomous systems, or static objects such as walls.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimization-based trajectory planning algorithms such as Model Predictive Control (MPC) have received significant attention recently, ranging from (unmanned) aircraft to robots to autonomous cars. This can be attributed to the increase in computational resources, the availability of robust numerical algorithms for solving optimization problems, as well as MPC's ability to systematically encode system dynamics and constraints inside its formulation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

One fundamental challenge in optimization-based trajectory planning is the appropriate formulation of collision avoidance constraints, which are known to be non-convex and computationally difficult to handle in general. While a number of formulations have been proposed in the literature for dealing with collision avoidance constraints, they are typically limited by one of the following features: $(i)$ The collision avoidance constraints are approximated through linear constraint, and it is difficult to establish the approximation error; $({ii})$ Existing formulations focus on point-mass controlled objects, and are not applicable to full-dimensional objects; $({iii})$ When the obstacles are polyhedral, then the collision avoidance constraints are often reformulated using integer variables. While this reformulation is attractive for linear systems with convex constraints since in this case a mixed-integer convex optimization problem can be solved, integer variables should generally be avoided when dealing with nonlinear systems when designing real-time controllers for robotic systems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we focus on a *controlled object* that moves in a general $n$-dimensional space while avoiding obstacles, and propose a novel approach for modeling obstacle avoidance constraints that overcomes the aforementioned limitations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that if the controlled object and the obstacles are described by convex sets such as polytopes or ellipsoids (or can be decomposed into a finite union of such convex sets), then the collision avoidance constraints can be exactly and non-conservatively reformulated as a set of smooth non-convex constraints. This is achieved by appropriately reformulating the *distance*-function between two convex sets using strong duality of convex optimization.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide a second formulation for collision avoidance based on the notion of *signed distance*, which characterizes not only the distance between two objects but also their penetration. This reformulation allows us to compute "least-intrusive" trajectories in case collisions cannot be avoided.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate the efficacy of the proposed obstacle avoidance reformulations on a quadcopter trajectory planning problem and autonomous parking application, where the controlled vehicles must navigate in tight environments. We show that both the distance reformulation and the signed distance reformulation enable real-time path planning and find trajectories even in challenging circumstances.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, since both our formulations allow the incorporation of system dynamics and input constraints, the generated trajectories are *kinodynamically feasible*, and hence can be tracked by simple low-level controllers.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper is organized as follows: Section 2 introduces the problem setup. Section 3 presents the collision avoidance and minimum-penetration formulations for the case when the controlled object is a point mass. These results are then extended to full-dimensional controlled objects in Section 4. Numerical experiments demonstrating the efficacy of the proposed method are given in Sections 5 and 6, and conclusions are drawn in Section 7. The Appendix contains auxiliary results needed to prove the main results of the paper. The source code of a quadcopter navigation example and autonomous parking example described in Sections 5 and 6 is provided at

<!-- chunk {"id": "body-0013", "role": "body", "section": "Dynamics, Objective and Constraints", "weight": 1.0} -->

We assume that the dynamics of the controlled object takes the form

<!-- chunk {"id": "body-0014", "role": "body", "section": "Dynamics, Objective and Constraints", "weight": 1.0} -->

Throughout this paper, we assume that the functions $f{( \cdot, \cdot )}$, $h{( \cdot, \cdot )}$ and $\ell{( \cdot, \cdot )}$ are smooth. Smoothness is assumed for simplicity, although all forthcoming statements apply equally to cases when those functions are twice continuously differentiable.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Obstacle and Controlled Object Modeling", "weight": 1.0} -->

Given the state $x_{k}$, we denote by ${{\mathbb{E}}{(x_{k})}} \subset {\mathbb{R}}^{n}$ the "space" occupied by the controlled object at time $k$, which we assume is a subset of ${\mathbb{R}}^{n}$. The collision avoidance constraint at time $k$ is now given by^11^1In this paper, we only consider collision avoidance constraints that are associated with the position and geometric shape of the controlled object, which are typically defined by its position $p_{k}$ and angles $\theta_{k}$. This is not a restriction of the theory as the forthcoming approaches can be easily generalized to collision avoidance involving other states, but done to simplify exposition of the material.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Obstacle and Controlled Object Modeling", "weight": 1.0} -->

Constraint is non-differentiable in general, e.g., when the obstacles are polytopic. In this paper, we will remodel in such a way that both continuity and differentiability are preserved. To this end, we assume that the obstacles ${\mathbb{O}}^{(m)}$ are convex compact sets with non-empty relative interior^22^2Non-convex obstacles can often be approximated/decomposed as the union of convex obstacles, and can be represented as

<!-- chunk {"id": "body-0017", "role": "body", "section": "Obstacle and Controlled Object Modeling", "weight": 1.0} -->

where $A^{(m)} \in {\mathbb{R}}^{l \times n}$, $b^{(m)} \in {\mathbb{R}}^{l}$, and $\mathcal{K} \subset {\mathbb{R}}^{l}$ is a closed convex pointed cone with non-empty interior. Representation is entirely generic since any compact convex set admits a conic representation of the form \[40, p.15\]. In particular, polyhedral obstacles can be represented as by choosing $\mathcal{K} = {\mathbb{R}}_{+}^{l}$; in this case $\preceq_{\mathcal{K}}$ corresponds to the well-known element-wise inequality $\leq$. Likewise, ellipsoidal obstacles can be represented by letting $\mathcal{K}$ be the second-order cone, see for details.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Obstacle and Controlled Object Modeling", "weight": 1.0} -->

To simplify the upcoming exposition, the same cone $\mathcal{K}$ is assumed for all obstacles; the extension to obstacle-specific cones $\mathcal{K}^{(m)}$ is straight-forward.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Obstacle and Controlled Object Modeling", "weight": 1.0} -->

In this paper, we will consider controlled objects ${\mathbb{E}}{(x_{k})}$ that are modeled as *point-masses* as well as *full-dimensional* objects. In the former case, ${\mathbb{E}}{(x_{k})}$ simply extracts the position $p_{k}$ from the state $x_{k}$, i.e.,

<!-- chunk {"id": "body-0020", "role": "body", "section": "Optimal Control Problem with Collision Avoidance", "weight": 1.0} -->

By combining --, the constrained finite-horizon optimal control problem with collision avoidance constraint is given by

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimal Control Problem with Collision Avoidance", "weight": 1.0} -->

where ${\mathbb{E}}{(x_{k})}$ is either given by (5a) (point-mass model) or (5b) (full-dimensional set), $\mathbf{x}:={\lbrack x_{0},x_{1},\ldots,x_{N + 1}\rbrack}$ is the collection of all states, and $\mathbf{u}:={\lbrack u_{0},u_{1},\ldots,u_{N}\rbrack}$ is the collection of all inputs. A key difficulty in solving problem, even for linear systems with convex objective function and convex state/input constraints, is the presence of the collision-avoidance constraints ${{{\mathbb{E}}{(x_{k})}} \cap {\mathbb{O}}^{(m)}} = \varnothing$, which in general are non-convex and non-differentiable.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Optimal Control Problem with Collision Avoidance", "weight": 1.0} -->

In the following, we present two novel approaches for modeling collision avoidance constraints that preserve continuity and differentiability, and are amendable for use with existing off-the-shelf gradient- and Hessian-based optimization algorithms.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Collision Avoidance", "weight": 1.0} -->

A popular way of formulating collision avoidance is based on the notion of *signed distance*

<!-- chunk {"id": "body-0024", "role": "body", "section": "Collision Avoidance", "weight": 1.0} -->

where $\text{dist}{( \cdot, \cdot )}$ and $\text{pen}{( \cdot, \cdot )}$ are the distance and penetration function, and are defined as

<!-- chunk {"id": "body-0025", "role": "body", "section": "Collision Avoidance", "weight": 1.0} -->

Roughly speaking, the signed distance is positive if ${\mathbb{E}}{(x)}$ and $\mathbb{O}$ do not intersect, and negative if they overlap. Therefore, collision avoidance can be ensured by requiring ${\text{sd}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} > 0$. Unfortunately, directly enforcing ${\text{sd}{({{\mathbb{E}}{(x)}},{\mathbb{O}})}} > 0$ inside the optimization problem is generally difficult since it is non-convex and non-differentiable in general. Furthermore, for optimization algorithms to be numerically efficient, they require an explicit representation of the functions they are dealing, in this case $\text{sd}{( \cdot, \cdot )}$. This, however, is difficult to obtain in practice since $\text{sd}{( \cdot, \cdot )}$ itself is the solution of the optimization problems (8a) and (8b).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Collision Avoidance", "weight": 1.0} -->

As a result, existing algorithms approximate through local linearization, for which it is difficult to establish bounds on approximation errors.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Collision Avoidance", "weight": 1.0} -->

In the following, we propose two reformulation techniques for obstacles avoidance that overcome the issues of non-differentiability and that do not require an explicit representation of the signed distance. We begin with point-mass models in Section 3, and treat the general case of full-dimensional controlled objects in Section 4.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Collision Avoidance for Point-Mass Models", "weight": 1.0} -->

In this section, we first present a smooth reformulation of when ${{\mathbb{E}}{(x_{k})}} = p_{k}$ in Section 3.1, and then extend the approach in Section 3.2 to generate minimum-penetration trajectories in case collisions cannot be avoided. To simplify notation, the time indices $k$ are omitted in the remainder of this section.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Without further assumptions on the norm $\parallel \cdot \parallel$ and the cone $\mathcal{K}$, the last two constraints in are not guaranteed to be smooth, a property that many general-purpose non-linear optimization algorithms require^33^3Strictly speaking, these solvers often require the cost function and constraints to be twice continuously differentiable only. Smoothness is assumed in this paper for the sake of simplicity.. Fortunately, it turns out that these constraints are smooth for the practically relevant cases of $\parallel \cdot \parallel$ being the Euclidean distance and $\mathcal{K}$ either the standard cone or the second-order cone, which allows us to model polyhedral and ellipsoidal obstacles. In these cases, and under the assumption that the functions $f{( \cdot, \cdot )}$, $h{( \cdot, \cdot )}$ and $\ell{( \cdot, \cdot )}$ are smooth, is a smooth nonlinear optimization problem that is amendable to general-purpose non-linear optimization algorithms such as IPOPT.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Without going into details, we point out that smoothness is retained when $\parallel \cdot \parallel = \parallel \cdot \parallel_{p}$ is a general $p$-norm, with $p \in {(1,\infty)}$, and $\mathcal{K}$ is the cartesian product of $p$-order cones $\mathcal{K}_{p}:={\{{(s,z)}:{{\| z\|}_{p} \leq s}\}}$, with $p \in {(1,\infty)}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In this case, the dual norm is given by $\parallel \cdot \parallel_{\ast} = \parallel \cdot \parallel_{q}$ and the dual cone is ${(\mathcal{K}_{p})}^{\ast} = \mathcal{K}_{q}$, where $q$ satisfies ${{1/p} + {1/q}} = 1$, see for details on dual norms and dual cones.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 1", "weight": 1.0} -->

While reformulation can be used for obstacle avoidance, it is limited to finding collision-free trajectories. Indeed, in case collisions cannot be avoided, the above formulation is not able to find "least-intrusive" trajectories by softening the constraints. Intuitively speaking, this is because is based on the notion of distance, and the distance between two overlapping objects (as is in the case of collision), is always zero, regardless of the penetration. From a practical point of view, this implies that slack variables cannot be included in the constraints of, because the optimal control problem is not able to distinguish between "severe" and "less severe" colliding trajectories. Furthermore, in practice, it is often desirable to soften constraints and include slack variables to ensure feasibility of the (non-convex) optimization problem, since (local) infeasibilities in non-convex optimization problem are known to cause numerical difficulties. In the following, we show how the above limitations can be overcome by considering the notion of penetration and softening the collision avoidance constraints.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Minimum-Penetration Trajectory Generation", "weight": 1.0} -->

In this section, we consider the design of *minimum-penetration* trajectories for cases when collision cannot be avoided and the goal is to find a "least-intrusive" trajectory. Following the literature, we measure "intrusion" in terms of *penetration* as defined in (8b).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Collision Avoidance for Full-Dimension Controlled Objects", "weight": 1.0} -->

The previous section provided a framework for computing collision-free and minimum-penetration trajectories for controlled objects that are described by point-mass models. While such models can be used to generate trajectories for "ball-shaped" controlled objects, done by setting the minimum distance $d_{\min}$ equal to the radius of the controlled object (see Section 5 for such an example), it can be restrictive in other cases. For example, modeling a car in a parking lot as a Euclidean ball can be very conservative, and prevent the car from finding a parking spot. To alleviate this issue, we show in this section how the results of Section 3 can be extended to full-dimensional controlled objects.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Minimum-Penetration Trajectory Generation", "weight": 1.0} -->

We overcome the above limitation by considering again the notion of penetration.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example 1: Quadcopter Path Planning", "weight": 1.0} -->

In this section, we illustrate reformulations and on a quadcopter navigation problem, where the quadcopter must find a path from one end of the room to the other end, while avoiding a low-hanging wall and passing through a small window hole, see Fig. 1.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Environment and Obstacle Modeling", "weight": 1.0} -->

The size of the room is $10.5 \times 10.5 \times 5.5$ m, and we see from Fig. 1 that the direct path between the start and end position is blocked by two obstacles. The first obstacle, a low-hanging wall, blocks the entire upper part of the room, and can only be passed from below. The second obstacle, another wall, blocks the entire room, but has a small window through which the quadcopter must pass to reach its target position. We approximate the shape of the quadcopter by a (Euclidean) sphere of radius 0.25 m. In the framework of and, the shape of the quadcopter can be taken into account by requiring a safety distance of $\mathsf{d}_{\text{min}} = 0.25$ m.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Environment and Obstacle Modeling", "weight": 1.0} -->

The first wall, which can only be passed from below, is placed at $X$ = 2 m, and the passage below is 0.85 m high. The second wall is placed at $X$ = 7 m, and the window (size $1 \times 1$m) is placed in the middle of the second wall at a height of $Z = 2.5$ m. Finally the depth of both walls is 0.5 m. This obstacle formation can be formally formulated using five axis-aligned rectangles, where the first obstacle is represented by one such rectangle and the window can be modeled as the union of four rectangles, see Fig. 1. The collision avoidance constraints with respect to the four outer walls of the room are achieved by appropriately upper- and lower-bounding the ${(X,Y,Z)} -$coordinates of the quadcopter.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Quadcopter Model", "weight": 1.0} -->

We consider the standard quadcopter model as used, which is derived by finding the equation of motion of the center of gravity (CoG) and summarized next. In this model, $X,Y,Z$ denote the position of the CoG in the world frame, and we use the $Z$-$X$-$Y$ Euler angles do describe the rotation of the quadcopter, where $\phi$ is the pitch angle, $\theta$ is the roll angle, and $\psi$ is the yaw angle. The rotation matrix that translates from the world to the body frame, which is defined with respect to the CoG, is hence given by

<!-- chunk {"id": "body-0040", "role": "body", "section": "Quadcopter Model", "weight": 1.0} -->

where $s_{\phi}:={\sin{(\phi)}}$ and $c_{\phi}:={\cos{(\phi)}}$. The accelerations of the CoG can be derived by considering the sum of the forces produced by the four rotors $F_{i}$ which point in positive z-direction in the body frame, and the gravity force which acts on the negative z-direction in the world frame, resulting in the following equation of motion,

<!-- chunk {"id": "body-0041", "role": "body", "section": "Quadcopter Model", "weight": 1.0} -->

\end{bmatrix}} = {\begin{bmatrix}
\end{bmatrix} + {R_{WB}\begin{bmatrix}
where $m$ is the mass of the quadcopter and $\overset{¨}{X}$, $\overset{¨}{Y}$ and $\overset{¨}{Z}$ are the second time derivatives of $X$, $Y$ and $Z$, respectively. The attitude dynamics of the quadcopter is derived in the body rates $p$, $q$, and $r$ which are related to the Euler angles through the following rotation matrix,

<!-- chunk {"id": "body-0042", "role": "body", "section": "Quadcopter Model", "weight": 1.0} -->

\end{bmatrix} = {\begin{bmatrix}
{s_{\theta}t_{\phi}} & 1 & {- {c_{\theta}t_{\phi}}} \\
{- {s_{\theta}/c_{\phi}}} & 0 & {c_{\theta}/c_{\phi}}
\end{bmatrix}\begin{bmatrix}
The body rates are given by the following equation of motion, which is driven by the four rotor forces $F_{i}$, as well as the corresponding moments $M_{i}$ and has the following form,

<!-- chunk {"id": "body-0043", "role": "body", "section": "Quadcopter Model", "weight": 1.0} -->

\end{bmatrix}} = {\begin{bmatrix}
\end{bmatrix} - {{\begin{bmatrix}
\end{bmatrix} \times I}\begin{bmatrix}
where $I$ is the inertia matrix which in our case is diagonal and $L$ is the distance from the CoG to the rotor. The rotor forces and moments depend quadratically on the motor speed $\omega_{i}$, which are the control inputs and are defined as follows,

<!-- chunk {"id": "body-0044", "role": "body", "section": "Quadcopter Model", "weight": 1.0} -->

where, $k_{F}$ and $k_{M}$ are constants depending on the rotor blades. Hence, the state of the quadcopter is $x = {\lbrack X,Y,Z,\phi,\theta,\psi,\overset{˙}{X},\overset{˙}{Y},\overset{˙}{Z},p,q,r\rbrack}$ and the inputs are the four rotor speeds $u = {\lbrack\omega_{1},\omega_{2},\omega_{3},\omega_{4}\rbrack}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Quadcopter Model", "weight": 1.0} -->

The parameters of the model, as well as the bounds on the inputs, are taken, which corresponds to a quadcopter which weighs 0.5 kg and has a diameter of half a meter. Bounds on the angles, velocities and body rates are considered, and the dynamics can be brought into the form using a (forward) Euler discretization, such that $x_{k + 1} = {x_{k} + {T_{\text{opt}}\overset{\sim}{f}{(x_{k},u_{k})}}}$, where $T_{\text{opt}}$ is the sampling time, and $\overset{\sim}{f}{( \cdot, \cdot )}$ is the continuous-time dynamics that can be obtained from (19a)--(19d).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Cost function", "weight": 1.0} -->

Our control objective is to navigate the quadcopter as fast as possible, while avoiding excessive control inputs. We combine these competing goals as a weighted sum of the form $J = {{q\tau_{F}} + {\sum_{k = 0}^{N - 1}{u_{k}^{T}Ru_{k}}}}$, where $\tau_{F}$ is the final time and $R = R^{\top} \succeq 0$, and $q \geq 0$ are weighting factors. Motivated, we do not directly minimize $\tau_{F}$; instead, observing that $\tau_{F} = {NT_{\text{opt}}}$, we will treat the discretization time $T_{\text{opt}}$ as a decision variable. This allows the use of the slightly modified cost function

<!-- chunk {"id": "body-0047", "role": "body", "section": "Cost function", "weight": 1.0} -->

which will be used in the numerical simulations later.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Cost function", "weight": 1.0} -->

Treating $T_{\text{opt}}$ as an optimization variable has the additional benefit that the duration of the maneuver does not need to be fixed a priori, allowing us to avoid feasibility issues caused by a too short maneuver lengths. We point out that having $T_{\text{opt}}$ as a decision variable comes at the cost of introducing an additional decision variable $T_{\text{opt}}$, which renders the dynamics "more non-linear", which can be seen when looking at the Euler discretization in the previous section.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Choice of Initial Guess", "weight": 1.0} -->

Recall that and are non-convex optimization problems, and hence computationally challenging to solve in general. In practice, one has to content oneself with a locally optimal solution that, for instance, satisfied the Karush-Kuhn-Tucker (KKT) conditions, since most numerical solvers operate locally. Furthermore, it is well-known that the solution quality critically depends on the initial guess ("warm starting point") that is provided to the solvers, and that different initial guesses can lead to different (local) optima. Unfortunately, computing a good initial guess is often difficult and highly problem dependent; ideally, the initial guess should be obstacle-free and approximately satisfy the system dynamics.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Choice of Initial Guess", "weight": 1.0} -->

For the quadcopter example, we have observed that the well-known A^⋆^ algorithm is able to provide good initial guesses. A^⋆^ is a graph search algorithm that is able to find obstacle-free paths by gridding the position space. It is similar to Dijkstra's algorithm, but uses a so-called heuristic function to perform a "best-first" search, see for details. In our quadcopter example, we use the A^⋆^ algorithm to find an obstacle-free path in the position space, which we use to initialize the states that correspond to the quadcopter's position. The remaining states are initialized with zero, while inputs are initialized with the steady state input that keeps the quadcopter in a hoovering position.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Choice of Initial Guess", "weight": 1.0} -->

The dual variables $\lambda_{k}^{(m)}$ are initialized with 0.05, and the discretization time $T_{\text{opt}}$ with 0.25. Fig. 2 depicts the initial guess used to generate the trajectory shown in Fig. 1. Notice that, due to gridding, the path in Fig. 2 exhibits a zigzag pattern.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

To verify the performance and robustness of our approach, we considered 36 path planning scenarios, each starting and ending in a hovering position. The starting point is always located at ${(X,Y,Z)} = {}$ m, and the finishing point is always located behind the wall with the window at $X = 9$ m, but with varying $Y$ and $Z$ coordinates. The final positions are generated by gridding the $(Y,Z)$ space with nine points in the $Y$ direction and four points in the $Z$ direction as shown in Fig. 3. We tested both the distance formulation as well as the signed distance formulation. The horizon $N$ equals the number of steps performed by the $A^{\star}$ algorithm, and takes values between 100 and 129 for the given setup and a grid size of 0.1 m. The sampling time $T_{\text{opt}}$ is restricted to lie between $0.125$ s and $0.375$ s. The optimization problems are implemented with the modeling toolbox JuMP in the programming language Julia, and solved using the general purpose nonlinear solver IPOPT.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

The problems are solved on a 2013 MacBook Pro with an i7 processor clocked at 2.6 GHz.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

Table 1 lists the minimum, maximum and average computation time of the A^⋆^ algorithm, and the time required to solve problems and. Fig. 3 reports the solution time as a function of the finishing position, where a circle indicates that IPOPT has successfully found a solution. We see from Fig. 3 that both the distance and signed distance formulation are able to compute all paths successfully. Interestingly, however, the computation time pattern of these two approaches are not correlated; in other words, a "difficult" scenario for the distance formulation might be "easy" for the signed distance formulation, and vice versa. In practice, this implies that to obtain feasible trajectories as fast as possible, the navigation problem should be solved with both obstacle avoidance formulations, and the first solution should be taken. In our setup, such an approach would result in a worst case computation time of 28.9 s, as opposed to 48.0 s and 59.1 s if the distance and signed distance reformulation are considered individually.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We close this section by pointing out that, with a maximum computation time of 2.8 s, the time for A^⋆^ to find an initial guess is considerably lower than that for solving the optimization problems, see Table 1. This is not surprising since A^⋆^ only plans a path in the $(X,Y,Z)$-space and ignores the system dynamics which leads to zigzag behavior, see Fig. 2. A dynamically feasible path is only obtained after solving the optimal control problems and which, by explicitly taking into account system dynamics, smoothen and locally optimize the path provided by the A^⋆^ algorithm.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Example 2: Autonomous Parking", "weight": 1.0} -->

As a second application for our collision avoidance formulation, we consider the autonomous parking problem for self-driving cars. In contrast to the quadcopter case, modeling a car as a point-mass and then approximating its shape with a ball can be very conservative and prevent the car from finding a feasible parking trajectory, especially when the environment is tight. In this section, we model the car as a rectangle, and then employ the full-dimensional formulation described in Section 4. We show that our modelling framework allows us to find obstacle-free parking trajectories even in tight environments. Two scenarios are considered: reverse parking (Fig. 4) and parallel parking (Fig. 5).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Environment and Obstacle Modeling", "weight": 1.0} -->

For the reverse parking scenario, the parking spot is assumed 2.6 m wide and 5.2 m long. The width of the road, where the car can maneuver, is 6 m, see Fig. 4 for an illustration. For the parallel parking scenario, the parking spot is 2.5 m deep and 6 m long, and the space to maneuver is 6 m wide (Fig. 5). Note that the obstacles in the reverse parking scenario can be described by three axis aligned rectangles, while the obstacles in the parallel parking scenario can be described by four axis aligned rectangles. In both cases, the controlled vehicle is modeled as a rectangle of size $4.7 \times 2$ m, whose orientation is determined by the car's yaw angle.

<!-- chunk {"id": "body-0058", "role": "body", "section": "System Dynamics and Cost Function", "weight": 1.0} -->

The car is described by the classical kinematic bicycle model, which is well-suited for velocities used in typical parking scenarios. The states $(X,Y)$ correspond to the center of the rear axes, while $\varphi$ is the yaw angle with respect to the X-axis, and $v$ is the velocity with respect to the rear axes. The inputs are the steering angle $\delta$ and the acceleration $a$. Hence, the continuous-time dynamics of the car is given by

<!-- chunk {"id": "body-0059", "role": "body", "section": "System Dynamics and Cost Function", "weight": 1.0} -->

where $L = 2.7$ m is the wheel base of the car. The steering angle is limited between $\pm 0.6$ rad (approximately 34 deg), with rate constraints $\overset{˙}{\delta} \in {\lbrack{- 0.6},0.6\rbrack}$ rad/s; acceleration is limited to be between $\pm 1$ m/s^2^. We limit the car's velocity to lie between $- 1$ and $2$ m/s. Similar as in the quadcopter case, the continuous-time dynamics are discretized using a forward Euler scheme. Finally, the same cost function as in the quadcopter is used, i.e., a weighted sum between the discretization-time and control effort is considered.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Initial Guess", "weight": 1.0} -->

Similar to the previous example, the solution quality of the non-convex optimization problems heavily depends on the initial guess provided to the numerical solvers. Unfortunately, it turns out that the A^⋆^ algorithm used in the quadcopter example generally provides a poor warm start as it is unable to take into account the vehicle's non-holonomic dynamics^44^4Roughly speaking, A^⋆^ will return trajectories that would require the vehicle to move sideways. Simulations indicate that the numerical solvers are typically not able to "correct" such a behavior and unable to recover a feasible solution when initialized with A^⋆^.. To address this issue, we resort to a modified version of A^⋆^, called Hybrid A^⋆^. The main idea behind Hybrid A^⋆^ is to use a simplified vehicle model with states $(X,Y,\varphi)$, and a finite number of steering inputs to generate a coarse parking trajectory. Like A^⋆^, Hybrid A^⋆^ grids the state space and performs a tree search, where the nodes are expanded using the simplified vehicle model. We refer the interested reader to for details on Hybrid A^⋆^.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Initial Guess", "weight": 1.0} -->

Fig. 6 and Fig. 7 depict two trajectories obtained from the Hybrid A^⋆^ algorithm. Notice that, due to discretization of state and input, the paths generated by Hybrid A^⋆^ seems more "bang-bang" and less "smooth" than those shown in Fig. 4 and Fig. 3.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

To evaluate the performance of formulations and, we study the reverse and parallel trajectory planning problem. For both cases, we consider different starting positions but one fixed end position at $X = 0$ m, and investigate the computation time of each method. The starting positions are generated by gridding the maneuvering space within $X \in {\lbrack{- 10},10\rbrack}$ m and $Y \in {\lbrack 6.5,9.5\rbrack}$ m, with 21 grid points in the $X$ direction and 4 grid points in $Y$ direction, see Fig. 8. The orientation for all the starting points is $\varphi = 0$, resulting in a total of 84 starting points. The horizon length $N$ is given by the Hybrid A^⋆^ algorithm. The optimization problems are again implemented with the modeling toolbox JuMP in the programming Julia, and IPOPT is used as the numerical solver. The problems are solved on a 2013 MacBook Pro with a i7 processor clocked at 2.6 GHz. A Julia-based example code can be found at

<!-- chunk {"id": "body-0063", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We begin by considering the reverse parking case, where one specific maneuver is illustrated in Fig. 4. The computation times for the distance and the signed distance formulation are listed in Table 2 (upper half) and shown in Fig. 8, for all 84 initial conditions. Table 2 indicates that the distance formulation is generally faster than the signed-distance formulation, with a mean computation time of 0.60 s compared to 1.03 s. This is not surprising since the signed distance formulation has more decision variables due to the presence of the slack variables $s_{k}^{(m)}$, see. Furthermore, we see from Fig. 8 that both approaches are able to find feasible parking trajectories, for all 84 considered initial conditions. Interestingly, we see that there are no obvious relations between starting positions and solution times.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

The computation times of the parallel parking case is shown in Fig. 9 and Table 2 (lower half). Similar as in the reverse parking case, we see that both approaches have a 100% success rate, and that, again due to the presence of the slack variables, the signed distance formulation requires longer computation time (1.67 s on average) than the distance formulation (0.87 s on average). Compared to reverse parking we see that parallel parking is computationally more demanding. We believe that this is due to the fact that the paths in parallel parking are generally longer than in reverse parking, since the car first needs to drive to the right before it can back into the parking lot, see also Fig. 5.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We close this section with the following two remarks: First, we point out that, while the paths generated by the Hybrid A^⋆^ are collision-free and kinodynamically feasible, they are challenging to track with low-level path following controllers because they do not incorporate information on the velocity and do not take into account the rate constraints in both steering and acceleration, allowing the car to take "aggressive" maneuveures. As demonstrated, this leads, in general, to significantly longer maneuvering times. Second, we notice from Table 2 that the computation time of Hybrid A^⋆^ is comparable to those of (signed) distance. Furthermore, the maximum overall computation time of Hybrid A^⋆^ and signed distance reformulation is 7.7 s (reserve parking), and 9.2 s (parallel parking). This implies that, when initialized with Hybrid A^⋆^, the proposed collision avoidance framework enables real-time autonomous parking in tight environments.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we presented smooth reformulations for collision avoidance constraints for problems where the controlled object and the obstacle can be represented as the finite union of convex sets. We have shown that non-differentiable polytopic obstacle constraints can be dealt with via dualization techniques to preserve differentiability, allowing the use of gradient- and Hessian-based optimization methods. The presented reformulation techniques are exact and non-conservative, and apply equally to point-mass and full-dimensional controlled vehicles. Furthermore, in case collision-free trajectories cannot be generated, our framework allows us to find least-intrusive trajectories, measured in terms of penetration.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our numerical studies, performed on a quadcopter trajectory planning and autonomous car parking example, indicate that, when appropriately initialized, the proposed framework is robust, real-time feasible, and able to generate dynamically feasible trajectories. Furthermore, we have seen that the initialization method is problem-dependent, and should be chosen depending on the system at hand. Current research focuses on appropriately warm starting the discretization time $T_{\text{opt}}$, as well as on methods for further speeding up computation times.
