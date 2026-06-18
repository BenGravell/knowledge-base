## Introduction

In recent years, the emergence of quadrotor online planning methods has greatly pushed the boundary of aerial autonomy, making drones fly out of laboratories and appear in numerous real-world applications. Among these methods, gradient-based ones, which smooth a trajectory and utilize the gradient information to improve its clearance, have shown great potential and gain more and more popularity.

Traditionally, gradient-based planners rely on a pre-built ESDF map to evaluate the gradient magnitude and direction, and use numerical optimization to generate a local optimal solution. Although the optimization programs enjoy fast convergence, they suffer a lot from constructing the required ESDF beforehand. As the statistics (TABLE II from EWOK) states, the ESDF computation takes up to about 70% of total processing time for conducting local planning. Therefore, we can safely claim that, building ESDF has become the bottleneck of gradient-based planners, preventing the method from being applied to resource-limited platforms.

Though ESDF is widely used, few works analyze its necessity. Typically, there are two ways to build an ESDF. As detailed in Sec.II, methods can be categorized as the incremental global updating ones, and the batch local calculation ones. However, neither of them focuses on the trajectory itself. Consequently, too much computation is spent on calculating ESDF values that make no contribution to the planning. In other words, current ESDF-based methods do not serve the trajectory optimization solely and directly. As shown in Fig.1, for a general autonomous navigation scenario where the drone is expected to avoid collisions locally, the trajectory covers only a limited space of the ESDF updating range. In practice, although some handcrafted rules can decide a slim ESDF range, they lack theoretical rationality and still induce unnecessary computations.

Figure 1: Trajectory during optimizing just covers a very limited space of the ESDF updating range.

In this paper, we design an ESDF-free Gradient-based lOcal planning framework called EGO, and we incorporate careful engineering considerations to make it lightweight and robust. The proposed algorithm is composed of a gradient-based spline optimizer and a post-refinement procedure. Firstly, we optimize the trajectory with smoothness, collision, and dynamical feasibility terms. Unlike traditional approaches that query pre-computed ESDF, we model the collision cost by comparing the trajectory inside obstacles with a guiding collision-free path. We then project the forces onto the colliding trajectory and generate estimated gradient to wrap the trajectory out of obstacles. During the optimization, the trajectory will rebound a few times between nearby obstacles and finally terminate in a safe region. In this way, we only calculate the gradient when necessary, and avoid computing ESDF in regions irrelevant to the local trajectory. If the resulted trajectory violates dynamical limits, which is usually caused by unreasonable time allocation, the refinement process is activated. During the refinement, trajectory time is reallocated when the limits are exceeded. With the enlarged time allocation, a new B-spline that fits the previous dynamical infeasible one while balancing the feasibility and fitting accuracy is generated. To improve robustness, the fitting accuracy is modeled anisotropically with different penalties on axial and radial directions.

To the best knowledge of us, this method is the first to achieve gradient-based local planning without an ESDF. Compared to existing state-of-the-art works, the proposed method generates safe trajectories with comparable smoothness and aggressiveness, but lower computation time of over an order of magnitude by omitting the ESDF maintenance. We perform comprehensive tests in simulation and real-world to validate our method. Contributions of this letter are:

We propose a novel and robust gradient-based quadrotor local planning method, which evaluates and projects gradient information directly from obstacles instead of a pre-built ESDF.

We propose a lightweight yet effective trajectory refinement algorithm, which generates smoother trajectories by formulating the trajectory fitting problem with anisotropic error penalization.

We integrate the proposed method into a fully autonomous quadrotor system, and release our software for the reference of the community^11^1https://github.com/ZJU-FAST-Lab/ego-planner.

Figure 2: The trajectory gets stuck into a local minimum, which is very common since the camera has no vision of the back of the obstacle.

## Related Work

### II-A Gradient-based Motion Planning

Gradient-based motion planning is the mainstream for UAV local trajectory generation, which formulates the problem as unconstrained nonlinear optimization. ESDF is first introduced in robotic motion planning by Ratliff et al.. Utilizing its abundant gradient information, many planning frameworks directly optimize trajectories in the configuration space. Nevertheless, optimizing the trajectory in discrete-time is not suitable for drones, because it is much more sensitive to dynamical constraints. Thereby, proposes a continuous-time polynomial trajectory optimization method for UAV planning. However, the involved integral of the potential function causes a heavy computation burden. Besides, the success rate of this method is around $70\%$, even with random restarts. For these drawbacks, introduces a B-spline parameterization of the trajectory which takes good advantage of the convex hull property. In, the success rate is significantly increased by finding a collision-free initial path as the front-end. Moreover, the performance is further improved when the generation of the initial collision-free path takes into account kinodynamic constraints. Zhou et al. incorporate perception awareness to make the system more robust. Among the above approaches, ESDF plays a vital role in evaluating distance with gradient magnitude and direction to nearby obstacles.

### II-B Euclidean Signed Distance Field (ESDF)

ESDF has long been used to construct objects from noisy sensor data for over two decades, and revive interests in robotics motion planning since. Felzenszwalb et al. propose an envelope algorithm that reduces the time complexity of ESDF construction to $O{(n)}$ with $n$ denoted as voxel numbers. This algorithm is not suitable for incremental building of ESDF, while dynamic updating of the field is often needed during quadrotor flight. To solve this problem, Oleynikova and Han propose incremental ESDF generation methods, namely Voxblox and FIESTA. Although these methods are highly efficient in dynamic updating cases, the generated ESDF almost always contains redundant information that may not be used in the planning procedure at all. As is shown in Fig.1, this trajectory only sweeps over a very limited subspace of the whole ESDF updating range. Therefore, it is valuable to design a more intelligent and lightweight method, instead of maintaining the whole field.

(c) Distance Field of A {p, v} Pair

Figure 3: a) A trajectory Φ passing through an obstacle generates several {p, v} pairs for control points. p are the points at the obstacle surface and v are unit vectors pointing from control points to p. b) A plane Ψ which is perpendicular to a tangent vector Ri intersects Γ forming a line l, from which a {p, v} pair is determined. c) Slice visualization of distance field definition di j = (Qi−pi j) ⋅ vi j. The color indicates the distance and the arrows are identical gradients equal to v. p is at the zero distance plane.

1:Notation: Environment ℰ, Control Points Struct Q, Anchor Points p, Repulsive Direction Vector v, Colliding Segments S
5: S.push_back(GetCollisionSegment())
10: for Si.begin ≤ j ≤ Si.end do

## Collision Avoidance Force Estimation

In this paper, the decision variables are control points $\mathbf{Q}$ of a B-spline curve. Each $\mathbf{Q}$ possesses its own environment information independently. Initially, a naive B-spline curve $\mathbf{\Phi}$ satisfying terminal constraints is given, regardless of collision. Then, the optimization procedure starts. For each colliding segment detected in an iteration, a collision-free path $\mathbf{\Gamma}$ is generated. Each control point $\mathbf{Q}_{i}$ of the colliding segment, after that, will be assigned an anchor point $\mathbf{p}_{ij}$ at the obstacle surface with a corresponding repulsive direction vector $\mathbf{v}_{ij}$, as shown in Fig.3(a) ‣ II Related Work ‣ EGO-Planner: An ESDF-free Gradient-based Local Planner for Quadrotors"). Denote by $i \in {\mathbb{N}}_{+}$ the index of control points, and $j \in {\mathbb{N}}$ the index of $\{\mathbf{p},\mathbf{v}\}$ pair. Note that each $\{\mathbf{p},\mathbf{v}\}$ pair only belongs to one specific control point. For brevity, we omit the subscript $ij$ without causing ambiguity. The detailed $\{\mathbf{p},\mathbf{v}\}$ pair generation procedure in this paper is summarized in Alg.1 ‣ II Related Work ‣ EGO-Planner: An ESDF-free Gradient-based Local Planner for Quadrotors") and is illustrated in Fig.3(b) ‣ II Related Work ‣ EGO-Planner: An ESDF-free Gradient-based Local Planner for Quadrotors"). Then the obstacle distance from $\mathbf{Q}_{i}$ to the $j^{th}$ obstacle is defined as

In order to avoid duplicative $\{\mathbf{p},\mathbf{v}\}$ pair generation before the trajectory escapes from the current obstacle during the first several iterations, we adopt a criterion that considers an obstacle which the control point $\mathbf{Q}_{i}$ lies in as newly discovered, only if the current $\mathbf{Q}_{i}$ satisfies $d_{ij} > 0$ for all valid $j$. Besides, this criterion allows only necessary obstacles that contribute to the final trajectory to be taken into optimization. Thus, the operation time is significantly reduced.

To incorporate necessary environmental awareness into the local planner, we need to explicitly construct an objective function that keeps the trajectory away from obstacles. ESDF provides this vital collision information but with the price of a heavy computation burden. In addition, as shown in Fig.2, ESDF-based planners can easily fall into a local minimum and fail to escape from obstacles, due to the insufficient or even wrong information from ESDF. To avoid such situations, an additional front-end is always needed to provide a collision-free initial trajectory. The above methodology outperforms ESDF in providing the vital information for collision avoidance, since the explicitly designed repulsive force can be fairly effective regarding various missions and environments. Moreover, the proposed method has no requirement for collision-free initialization.

## Gradient-Based Trajectory Optimization

### IV-A Problem Formulation

In this paper, the trajectory is parameterized by a uniform B-spline curve $\mathbf{\Phi}$, which is uniquely determined by its degree $p_{b}$, $N_{c}$ control points $\left\{ \mathbf{Q}_{1},\mathbf{Q}_{2},\cdots,\mathbf{Q}_{N_{c}} \right\}$, and a knot vector $\left\{ t_{1},t_{2},\cdots,t_{M} \right\}$, where $\mathbf{Q}_{i} \in {\mathbb{R}}^{3}$, $t_{m} \in {\mathbb{R}}$ and $M = {N_{c} + p_{b}}$. For simplicity and efficiency of trajectory evaluation, the B-spline used in our method is uniform, which means each knot is separated by the same time interval ${\bigtriangleupt} = {t_{m + 1} - t_{m}}$ from its predecessor. The problem formulation in this paper is based on the current state-of-the-art quadrotor local planning framework Fast-Planner.

Figure 4: Convex hull property of the B-spline curve. Gray points represent control points. The whole curve stays inside the feasibility bounding box(black dotted box) as long as all the control points are in that box. Without loss of generality, each convex hull consists of four vertexes.

B-spline enjoys convex hull property. This property indicates that a single span of a B-spline curve is merely controlled by $p_{b} + 1$ successive control points and lies within the convex hull of these points. For example, a span within $(t_{i},t_{i + 1})$ lies inside the convex hull formed by $\{\mathbf{Q}_{i - p_{b}},\mathbf{Q}_{{i - p_{b}} + 1},\cdots,\mathbf{Q}_{i}\}$. Another property is that the $k^{th}$ derivative of a B-spline is still a B-spline with order $p_{b,k} = {p_{b} - k}$. Since $\bigtriangleupt$ is identical alone $\mathbf{\Phi}$, the control points of the velocity $\mathbf{V}_{i}$, acceleration $\mathbf{A}_{i}$, and jerk $\mathbf{J}_{i}$ curves are obtained by

We follow the work of to plan the control points $\mathbf{Q} \in {\mathbb{R}}^{3}$ in a reduced space of differentially flat outputs. The optimization problem is then formulated as follows:

where $J_{s}$ is the smoothness penalty, $J_{c}$ is for collision, and $J_{d}$ indicates feasibility. $\lambda_{s},\lambda_{c},\lambda_{d}$ are weights for each penalty terms.

### IV-A1 Smoothness penalty

In, the smoothness penalty is formulized as the time integral over square derivatives of the trajectory (acceleration, jerk, etc.). In, only geometric information of the trajectory is taken regardless of time allocation. In this paper, we combine both methods to penalize squared acceleration and jerk without time integration.

Benefiting from the convex hull property, minimizing the control points of second and third order derivatives of the B-spline trajectory is sufficient to reduce these derivatives along the whole curve. Therefore, the smoothness penalty function is formulated as

which minimizes high order derivatives, making the whole trajectory smooth.

### IV-A2 Collision penalty

Collision penalty pushes control points away from obstacles. This is achieved by adopting a safety clearance $s_{f}$ and punishing control points with $d_{ij} < s_{f}$. In order to further facilitate optimization, we construct a twice continuously differentiable penalty function $j_{c}$ and suppress its slope as $d_{ij}$ decreases, which yields the piecewise function

where $j_{c}{(i,j)}$ is the cost value produced by ${\{\mathbf{p},\mathbf{v}\}}_{j}$ pairs on $\mathbf{Q}_{i}$. The cost on each $\mathbf{Q}_{i}$ is evaluated independently and accumulated from all corresponding ${\{\mathbf{p},\mathbf{v}\}}_{j}$ pairs. Thus, a control point obtains a higher trajectory deformation weight if it discovers more obstacles. Specifically, the cost value added to the $i^{th}$ control point is ${j_{c}{(\mathbf{Q}_{i})}} = {\sum_{j = 1}^{N_{p}}{j_{c}{(i,j)}}}$, $N_{p}$ is the number of ${\{\mathbf{p},\mathbf{v}\}}_{j}$ pairs belonging to $\mathbf{Q}_{i}$. Combining costs on all $\mathbf{Q}_{i}$ yields the total cost $J_{c}$, i.e.,

Unlike traditional ESDF-based methods, which compute gradient by trilinear interpolation on the field, we obtain gradient by directly computing the derivative of $J_{c}$ with respect to $\mathbf{Q}_{i}$, which gives

### IV-A3 Feasibility penalty

Feasibility is ensured by restricting the higher order derivatives of the trajectory on every single dimension, i.e., applying ${|{\mathbf{\Phi}_{r}^{(k)}{(t)}}|} < \mathbf{\Phi}_{r,{max}}^{(k)}$ for all $t$, where $r \in {\{ x,y,z\}}$ indicates each dimension. Thanks to the convex hull property, constraining derivatives of the control points is sufficient for constraining the whole B-spline. Therefore, the penalty function is formulated as

where $w_{v},w_{a},w_{j}$ are weights for each terms and $F{( \cdot )}$ is a twice continuously differentiable metric function of higher order derivatives of control points.

where $c_{r} \in \mathbf{C} \in {\{\mathbf{V}_{i},\mathbf{A}_{i},\mathbf{J}_{i}\}}$, $a_{1},b_{1},c_{1},a_{2},b_{2},c_{2}$ are chosen to meet the second-order continuity, $c_{m}$ is the derivative limit, $c_{j}$ is the splitting points of the quadratic interval and the cubic interval. $\lambda < {1 - \epsilon}$ is an elastic coefficient with $\epsilon \ll 1$ to make the final results meet the constraints, since the cost function is a tradeoff of all weighted terms.

### IV-B Numerical Optimization

The formulated problem in this paper features in two aspects. Firstly, the objective function $J$ alters adaptively according to the newly found obstacles. It requires the solver to be able to restart fast. Secondly, quadratic terms dominate the formulation of the objective function, making $J$ approximate quadratic. It means that the utilization of Hessian information can significantly accelerate the convergence. However, obtaining the exact inverse Hessian is prohibitive in real-time applications since it consumes nonnegligible massive computation. To circumvent this, quasi-Newton methods that approximate the inverse Hessian from gradient information are adopted.

Since the performance of a solver is problem dependent, we compare three algorithms belonging to quasi-Newton methods. They are Barzilai-Borwein method which is capable of fast restart with most crude Hessian estimation, truncated Newton method which estimates Hessian by adding multiple tiny perturbations to a given state, L-BFGS method which approximates Hessian from previous objective function evaluations but requires a serial of iterations to reach a relatively accurate estimation. Comparison in Sec.VI-B states that L-BFGS outperforms the other two algorithms with appropriately selected memory size, balancing the loss of restart and the accuracy of inverse Hessian estimation. This algorithm is briefly explained as follows. For an unconstrained optimization problem ${min}_{\mathbf{x} \in {\mathbb{R}}^{n}}{f{(\mathbf{x})}}$, the updating for $\mathbf{x}$ follows the approximated Newton step

where $\alpha_{k}$ is the step length and $\mathbf{H}_{k}$ is updated at every iteration by means of the formula

where ${\rho_{k} = {({\mathbf{y}_{k}^{T}\mathbf{s}_{k}})}^{- 1}},{{\mathbf{V}_{k} = {\mathbf{I} - {\rho_{k}\mathbf{y}_{k}\mathbf{s}_{k}^{T}}}},{\mathbf{s}_{k} = {\mathbf{x}_{k + 1} - \mathbf{x}_{k}}}}$ and $\mathbf{y}_{k} = {{\nabla\mathbf{f}_{k + 1}} - {\nabla\mathbf{f}_{k}}}$.

Here $\mathbf{H}_{k}$ is not calculated explicitly. The algorithm right multiplies $\nabla\mathbf{f}_{k}$ to Equ.12 and recursively expands for $m$ steps and then yields the efficient two-loop recursion updating method, resulting in linear time/space complexity. The weight of Barzilai-Borwein step is used as the initial inverse Hessian $\mathbf{H}_{k}^{0}$ for L-BFGS updating, which is

A monotone line search under strong Wolfe condition is used to enforce convergence.

## Time Re-allocation and Trajectory Refinement

Allocating an accurate time profile before the optimization is unreasonable, since the planner knows no information about the final trajectory then. Therefore, an additional time re-allocation procedure is vital to ensure dynamical feasibility. Previous works parameterize the trajectory as a non-uniform B-spline and iteratively lengthen a subset of knot spans when some segments exceed derivative limits.

However, one knot span $\bigtriangleupt_{n}$ influences multiple control points and vice versa, leading to high-order discontinuity to the previous trajectory when adjusting knot spans near the start state. In this section, a uniform B-spline trajectory $\mathbf{\Phi}_{f}$ is re-generated with reasonable time re-allocation according to the safe trajectory $\mathbf{\Phi}_{s}$ from IV. Then, an anisotropic curve fitting method is proposed to make $\mathbf{\Phi}_{f}$ freely optimize its control points to meet higher order derivative constraints while maintaining a nearly identical shape to $\mathbf{\Phi}_{s}$.

Figure 5: Optimizing trajectory Φf to fit trajectory Φs while adjusting smoothness and feasibility. Black and green dots are sample points on the trajectory. The displacement between Φf (α T′) and Φs (α T) breaks down into da and dr along two ellipse principal axes. Points at the red ellipse surface produce identical penalties.

Firstly, as Fast-Planner does, we compute the limits exceeding ratio,

where $i \in {\{ 1,\cdots,{N_{c} - 1}\}}$, $j \in {\{ 1,\cdots,{N_{c} - 2}\}}$, $k \in {\{ 1,\cdots,{N_{c} - 3}\}}$ and $r \in {\{ x,y,z\}}$ axis. A notion with subscript $m$ represents the limitation of a derivative. $r_{e}$ indicates how much we should lengthen the time allocation for $\mathbf{\Phi}_{f}$ relative to $\mathbf{\Phi}_{s}$. Note that $\mathbf{V}_{i}$, $\mathbf{A}_{j}$ and $\mathbf{J}_{k}$ are inversely proportional to $\bigtriangleupt$, the square of $\bigtriangleupt$ and the cubic of $\bigtriangleupt$, respectively, from Equ.2. Then we obtain the new time span of $\mathbf{\Phi}_{f}$

$\mathbf{\Phi}_{f}$ of time span $\bigtriangleupt^{\prime}$ is initially generated under boundary constraints while maintaining the identical shape and control points number to $\mathbf{\Phi}_{s}$, by solving a closed-form min-least square problem. The smoothness and feasibility are then refined by optimization. The penalty function $J^{\prime}$ formulated by linear combinations of smoothness (Sec.IV-A1), feasibility (Sec.IV-A3) and curve fitting (introduced later) is

where $\lambda_{f}$ is the weight of fitness term.

The fitting penalty function $J_{f}$ is formulated as the integral of anisotropic displacements from points $\mathbf{\Phi}_{f}{({\alphaT^{\prime}})}$ to the corresponding $\mathbf{\Phi}_{s}{({\alphaT})}$, where $T$ and $T^{\prime}$ are the trajectory duration of $\mathbf{\Phi}_{s}$ and $\mathbf{\Phi}_{f}$, $\alpha \in {\lbrack 0,1\rbrack}$. Since the fitted curve $\mathbf{\Phi}_{s}$ is already collision-free, we assign the axial displacement of two curves with low penalty weight to relax smoothness adjustment restriction, and radial displacement with high penalty weight to avoid collision. To achieve this, we use the spheroidal metric, shown in Fig.5, such that displacements at the same spheroid surface produce identical penalties. The spheroid we use for $\mathbf{\Phi}_{f}{({\alphaT^{\prime}})}$ is obtained by rotating an ellipse centering at $\mathbf{\Phi}_{s}{({\alphaT})}$ about one of its principal axes, the tangent line ${\overset{˙}{\mathbf{\Phi}}}_{s}{({\alphaT})}$. So the axial displacement $d_{a}$ and radial displacement $d_{r}$ can be calculated by

The fitness penalty function is

where $a$ and $b$ are semi-major and semi-minor axis of the ellipse, respectively. The problem is solved by L-BFGS.

## Experiment Results

### VI-A Implementation Details

The planning framework is summarized in Alg.2. We set the B-spline order as $p_{b} = 3$. The number of control points $N_{c}$ alters around 25, which is determined by the planning horizon (about 7m) and the initial distance interval (about 0.3m) of adjacent points. These are empirical parameters that balance the complexity of the problem with degrees of freedom. The time complexity is $O{(N_{c})}$, since one control point only affects nearby segments according to the local support property of B-spline. The complexity of L-BFGS is also linear on the same relative tolerance. For collision-free path searching, we adopt A\*, which has a good advantage that the path $\mathbf{\Gamma}$ always tends to be close to the obstacle surface naturally. Therefore, we can directly select $\mathbf{p}$ at $\mathbf{\Gamma}$ without obstacle surface searching. For vector $\mathbf{R}_{i}$ defined in Fig.3(b) ‣ II Related Work ‣ EGO-Planner: An ESDF-free Gradient-based Local Planner for Quadrotors"), it can be deduced by the property of uniform B-spline parameterization, that the $\mathbf{R}_{i}$ satisfies

which can be efficiently computed. Equ.18 is discretized to a finite number of points $\mathbf{\Phi}_{f}{({k\bigtriangleupt^{\prime}})}$ and $\mathbf{\Phi}_{s}{({k\bigtriangleupt})}$, where ${k \in {\mathbb{N}}},{0 \leq k \leq {\lfloor{{T/\bigtriangleup}t}\rfloor}}$. To further enforce safety, a collision check of a circular pipe with a fixed radius around the final trajectory is performed to provide enough obstacle clearance. The optimizer stops when no collision is detected. Real-world experiments are presented on the same flight platform of with depth acquired by Intel RealSense D435^22^2https://www.intelrealsense.com/depth-camera-d435/. Furthermore, we modify the ROS driver of Intel RealSense to enable the laser emitter strobe every other frame. This allows the device to output high quality depth images with the help of the emitter, and along with binocular images free from laser interference. The modified driver is open-sourced as well.

1:Notation: Goal 𝒢, Environment ℰ, Control Point Struct Q, Penalty J, Gradient G
Algorithm 2 Rebound Planning

### VI-B Optimization Algorithms Comparison

In this section, three different optimization algorithms, including Barzilai-Borwein (BB) method, limited-memory BFGS (L-BFGS) and truncated Newton (T-NEWTON) method, are discussed. Specifically, each algorithm runs for 100 times independently in random maps. All relevant parameters including boundary constraints, time allocation, decision variables initialization, and random seeds, are set identical for different algorithms. The data about success rate, computation time and numbers of objective function evaluations are recorded. Only the successful cases are counted due to the data in failed cases is meaningless. The associated results are shown in Tab.I, which states that L-BFGS significantly outperforms the other two algorithms. L-BFGS characterizes a type of approximation by means of second order Taylor expansions, which is suitable for optimizing the objective function described in Sec.IV-B. Truncated Newton method approximates the second order optimization direction $\mathbf{H}^{- 1}{\nabla\mathbf{f}_{k}}$ as well. However, too many objective function evaluations increase the optimization time. BB-method estimates the Hessian as a scalar $\lambda$ times $\mathbf{I}$. Nevertheless, the insufficient estimation of Hessian still leads to a low convergence rate.

TABLE I: Optimization Algorithms Comparison

TABLE II: ESDF/ESDF-free Methods Comparison

### VI-C Trajectory Generation With & Without ESDF

We use the same setting as Sec.VI-B to perform this comparison. On account of the low success rate explained in when using straight line initialization for an ESDF-based trajectory generator, we adopt a collision-free initialization. Comparison results are in Tab.II.

Figure 6: Visualization of local trajectory planning over a short period of time with velocity profile.

For clarity, ESDF-based methods with and without collision-free initialization are abbreviated as EI and ENI. This comparison gives that the proposed EGO algorithm achieves a comparable success rate to ESDF-based methods with collision-free initialization. However, trajectory energy (jerk integral) produced by EGO is slightly higher. This happens because the control points of EGO which contain more than one $\{\mathbf{p},\mathbf{v}\}$ pair produce stronger trajectory deformation force than EI does, as described in Sec.IV-A2. On the other hand, stronger force accelerates the convergence procedure, resulting in shorter optimization time. Some statistics of ENI (shown in gray) can be less convincing because ENI tests can only succeed in fewer challenge cases where the resulting trajectories are naturally smoother with less energy cost and lower velocity, compared to EI and EGO. Something noteworthy is that although the ESDF updating size is reduced to ${10 \times 4 \times 2}m^{3}$ with $0.1m$ resolution for a $9m$ trajectory, the ESDF updating still takes up a majority of the computation time.

### VI-D Multiple Planners Comparison

Figure 7: Comparison of the proposed EGO-Planner against two SOTA planners with default parameters.

We compare the proposed planner with two state-of-the-art methods, Fast-Planner and EWOK, which utilize ESDF to evaluate obstacle distance and gradient. Each planner runs for ten times of different obstacle densities from the same starts to ends. The average performance statistics and the ESDF computation time are shown in Tab.III and Fig.7. Trajectories generated by three methods on a map of 0.5 obstacles/$m^{2}$ are illustrated in Fig.8.

From Tab.III we conclude that the proposed method achieves shorter flight time and trajectory length but ends up in higher energy cost compared to Fast-Planner. This is mainly caused by the front-end kinodynamic path searching in. EWOK suffers twisty trajectories in dense environments, since the objective function contains exponential terms, which leads to unstable convergence in optimization. Furthermore, we conclude that a lot of computation time without ESDF updating is saved by the proposed method.

TABLE III: Planners Comparison

Figure 8: Trajectory visualization in simulation.

Figure 9: Trajectory of an outdoor experiment in a forest.

### VI-E Real-world Experiments

We present several experiments in cluttered unknown environments with limited camera FOV. One experiment is to fly by waypoints given in advance. In this experiment, the drone starts from a small office room, passes through the door, flies around in a big cluttered room, and then returns to the office, as illustrated in Fig.10a and Fig.11. The narrowest passage of indoor experiments is less than one meter as shown in Fig.6. By contrast, the drone reaches ${3.56m}/s$ in such a cluttered environment.

Another indoor experiment is to chase goals arbitrarily and abruptly given during the flight, as shown in Fig.10c. In this test, limited FOV puts greater challenges that a feasible trajectory must be generated immediately once a new goal is received or collision threat is detected. Thus, this experiment validates that the proposed planner is capable of performing aggressive flight on the premise of feasibility.

In the outdoor experiments, the drone flies through a forest of massive trees and low bushes, as shown in Fig.10b and Fig.9. Although the wild airflow around the drone causes swinging of the branches and leaves, making the map less reliable, the drone still reaches a speed above ${3m}/s$. Therefore, the proposed planner can tackle both experimental and field environments. We refer readers to the video^33^3https://youtu.be/UKoaGW7t7Dk for more information.

Figure 10: Real-world experiments. a) An indoor test. b) An outdoor test. c) Composite snapshots of indoor flights.

Figure 11: Trajectory of an indoor experiment

## Conclusion and Future Work

In this paper, we investigate the necessity of ESDF for gradient-based trajectory planning and propose an ESDF-free local planner. It achieves comparable performance to some state-of-the-art ESDF-based planners but reduces computation time for over an order of magnitude. Benchmark comparisons and real-world experiments validate that it is robust and highly efficient.

The proposed method still has some flaws, which are the local minimum introduced by A\* search and the conservative trajectories introduced by unified time re-allocation. Therefore, we will work on performing topological planning to escape the local minimum and re-formulating the problem to generate near-optimal trajectories. The planner is designed for static environments and can tackle slowly moving obstacles (below 0.5m/s) without any modification. We will work on dynamic environment navigation by moving object detection and topological planning in the future.
