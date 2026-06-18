<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RAPTOR: Robust and Perception-aware Trajectory Replanning for Quadrotor Fast Flight

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent advances in trajectory replanning have enabled quadrotor to navigate autonomously in unknown environments. However, high-speed navigation still remains a significant challenge. Given very limited time, existing methods have no strong guarantee on the feasibility or quality of the solutions. Moreover, most methods do not consider environment perception, which is the key bottleneck to fast flight. In this paper, we present RAPTOR, a robust and perception-aware replanning framework to support fast and safe flight. A path-guided optimization (PGO) approach that incorporates multiple topological paths is devised, to ensure finding feasible and high-quality trajectories in very limited time. We also introduce a perception-aware planning strategy to actively observe and avoid unknown obstacles. A risk-aware trajectory refinement ensures that unknown obstacles which may endanger the quadrotor can be observed earlier and avoid in time. The motion of yaw angle is planned to actively explore the surrounding space that is relevant for safe navigation. The proposed methods are tested extensively. We will release our implementation as an open-source package for the community.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, progresses on different aspects of unmanned aerial vehicles (UAVs), especially quadrotor autonomy have been achieved and promote autonomous navigation. Nonetheless, high-speed flight in unknown and highly cluttered environments still remains one of the biggest challenges toward full autonomy. To achieve fast flight, trajectory replanning is of vital importance to cope with previously unknown obstacles, guaranteeing smooth and safe navigation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although trajectory replanning has been investigated actively, most presented methods only apply to flights at a moderate speed. Several issues greatly hinder their usage in high-speed scenarios. (a) Flying in unknown environments at a high speed, the quadrotor should replan new trajectories to avoid unexpected obstacles in considerably short time, otherwise it crashes. However, most methods do not guarantee to find feasible trajectories given very limited time. (b) Current methods typically find a locally optimal trajectory confined within a topologically equivalent class, which does not necessarily contains a satisfactory solution for smooth and safe navigation, especially in fast flight. (c) Existing methods are unaware of environment perception, which can be fatal as the flight speed and obstacle density get high. Paying no attention to perception, the planned motions may lead to restricted visibility to the environments, which would in turn result in deficient information of the surrounding space necessary for safe navigation. The consequence of not considering perception in replanning can be better illustrated by Fig.1. To minimize the energy consumption, a trajectory near the wall is generated, along which the visibility toward the unknown space behind the corner is very limited.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

As a result the obstacle right behind the corner is invisible until the quadrotor turns right and gets very close, which 'surprises' or even crashes the quadrotor. Instead of avoiding what are observed passively, actively observing and avoiding possible dangers is critical for safe high-speed flight.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a Robust And Perception-aware TrajectOry Replanning framework called RAPTOR to address these issues systematically. To ensure obtaining feasible trajectories within limited time, we present a path-guided gradient-based optimization method, which utilizes geometric guiding paths to eliminate infeasible local minima and guarantee the success of replanning. Also, to further improve the optimality of the replanning, we introduce an online topological path planning to extract a comprehensive set of paths that capture the structure of the environment. With the guidance of several distinctive paths, multiple trajectories are optimized in parallel, leading to a more thorough exploration of the solution space.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The above mentioned method that address issues (a) and (b) were first proposed in our previous work. However, it adopts the optimistic assumption and lack the awareness of environment perception, which restricts its capability in higher speed and more complex environments. To bridge this gap, we extend it with a perception-aware planning strategy to enable faster and safer flight from two aspects. Firstly, a risk-aware trajectory refinement approach is developed to incorporate with the optimistic planner. It identifies unknown regions along the optimistic trajectories that are potentially dangerous to the quadrotor. Visibility toward such regions along with safe reaction distance are enforced explicitly, ensuring that obstacles in unmapped areas become visible earlier and are avoidable by the quadrotor. Secondly, we incorporate the yaw angle of the quadrotor into a two-step motion planning framework. A optimal sequence of yaw angles that maximizes information gain and smoothness is searched in the discrete state space, which is further smoothed through optimization. The planned motions of yaw angle enable the quadrotor whose field-of-view (FOV) is limited to actively explore the unknown space to gain more relevant knowledge for the future flight.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We conduct systematic evaluations on both the proposed perception-aware planning strategy and the whole planning system, through benchmark comparisons and challenging real-world experiments. For the former, it is able to support fast and safe flight in challenging scenarios where traditional method fail to ensure safety. For the later, our planner outperform state-of-the-art methods in several aspects in fast flight tasks. Extensive indoor and outdoor flight tests in complex environments also validates our planning system.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

1\) A topological paths-guided gradient-based replanning approach, that is capable of generating high-quality trajectories in limited time.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

2\) A risk-aware trajectory refinement approach, which enforces visibility and safe reaction distance to unknown obstacles. It improves the predictability and safety of fast flights.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

3\) A two-step yaw angle planning method, to actively explore the unknown environments and gather useful information for the flight.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

4\) Extensive simulation and real-word tests that validate the proposed method. The source code of our system will be released as an open-source package.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Quadrotor Trajectory Planning", "weight": 1.0} -->

Trajectory planning for quadrotor has been widely investigated. Existing methods can be categorized into hard-constrained methods and gradient-based optimization methods. Hard-constrained methods are pioneered by minimum-snap trajectory, in which piecewise polynomial trajectories are generated through quadratic programming(QP). presented a closed-form solution to minimum snap trajectories. generate trajectories in a two-step pipeline. Safe regions around initial paths are extracted as convex flight corridors, within which QP is solved to generate smooth and safe trajectories. Among these methods, poorly chosen time allocation of piecewise polynomials usually lead to unsatisfying results. To this end, fast marching and kinodynamic search are utilized to search for initial paths with more reasonable time allocation. also proposed to represent trajectories as piecewise Bézier curves so that safety and dynamical feasibility are guaranteed. adopted a mixed integer QP formulation to find a more reasonable time allocation of the trajectory.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Quadrotor Trajectory Planning", "weight": 1.0} -->

Another category is the gradient-based trajectory optimization (GTO) methods, which typically formulate trajectory generation as non-linear optimization problems trading off smoothness, safety and dynamic feasibility. Recently works revealed that they are particularly effective for local replanning, which is a key component for high-speed flight in unknown environments. proposed to optimize discrete-time trajectory through covariant gradient descent, reviving the community's interest in such methods. presented a similar formulation, but solves the problem by sampling neighboring candidates iteratively. The stochastic sampling strategy partially overcomes the local minima issue but is computationally intensive. extended it to continuous-time quadrotor trajectories and also adopted random optimization restarts to slightly relieve the typical local minima issue of such methods. In, the optimization is combined with an informed sampling-based path searching to improve the success rate. proposed to parameterize trajectories as uniform B-splines, showing the usefulness of continuity and locality properties of B-spline for replanning. However, due to insufficient success rate and efficiency, only apply to flight at a moderate speed.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Quadrotor Trajectory Planning", "weight": 1.0} -->

To this end, further exploited B-spline to improve the efficiency and robustness. GTO methods are preferable for replanning due to high efficiency. However, their local minima issue may lead to undesired solutions. Our method lies in this category, and we resolve local minima by introducing topologically distinctive paths to guide optimization in parallel.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Topological Path Planning", "weight": 1.0} -->

There are works utilizing the idea of topologically distinct paths for planning, in which paths belonging to different homotopy (homology) or visibility deformation classes are sought. constructs a variant of probabilistic roadmap (PRM) to capture homotopy classes, in which path searching and redundant path filtering are conducted simultaneously. In contrast, firstly creates a PRM or Voronoi diagram, after which a homology equivalence relation based on complex analysis is adopted to filter out redundant paths. These methods only apply to 2D scenarios. To seek for 3D homology classes, exploit the theory of electromagnetism and propose a 3D homology equivalence relation. However, it requires occupied space to be decomposed into "genus 1" obstacles, which is usually impractical. Besides, capturing only homotopy classes in 3D space is insufficient to encode the set of useful paths, as indicated, since 3D homotopic paths may be too hard to deform into each other. To this end, leverages a visibility deformation roadmap to search for a richer set of useful paths. convert maps built from SLAM systems into sparse graphs representing the topological structure of the environments.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Topological Path Planning", "weight": 1.0} -->

focus on global offline planning and is too time-consuming for online usage. Our topological path searching is conceptually closest to, but with a reinvented algorithm for real-time performance.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-C Navigation in Unknown Environments", "weight": 1.0} -->

To deal with unknown environments in navigation, different strategies have been used. Many methods adopt the optimistic assumption, which treats the unknown space as collision-free. This strategy improves the chance of reaching goals, but may not guarantee safety. On the contrary, some other methods regard unknown space as unsafe and only allow motions within the known-free space or sensor FOV. In the sensor FOV constraint is partially relaxed by choosing safe motion primitives generated in the past. Although these restrictions ensure safety, they lead to conservative motion. Recently proposed a strategy that plans in both the known-free and unknown space. Instead of being over optimistic about the unknown space, it always maintains back-up trajectories to ensure safety.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-C Navigation in Unknown Environments", "weight": 1.0} -->

The limitation of the above mentioned strategies is the lack of environment perception awareness, which is of significant necessity in fast flight. Although much attention has been paid to planning with the awareness of localization and target tracking, less emphasis is put on environment perception. proposed a learned heuristic function to guide the path searching into areas with greater visibility to unknown space, but it may not generalize well to complex 3D environments. showed an integrated mapping and planning framework for active perception. The planner iteratively simulates future measurements after executing specific motions, predicts uncertainty of the map, and minimizes the replanning risk. Its main drawback is the prohibited runtime for online usage. In, a local planner is coupled with local exploration to safely navigate a cluttered environment. However, it conservatively selects intermediate goals within known-free space, which restricts the flight speed. In this paper, we present a perception-aware strategy to ensures that unknown dangers can be discovered and avoided early. It guarantees safety and does not lead to conservative behaviors.

<!-- chunk {"id": "body-0020", "role": "body", "section": "System Overview", "weight": 1.0} -->

The proposed replanning system is illustrated in Fig.3. It takes the outputs of the global planning, dense mapping and state estimation modules, and deforms the global reference trajectory locally to avoid previously unknown obstacles. The replanning works in two steps. Firstly, the robust optimistic replanning generates multiple locally optimal trajectories in parallel through the path-guided optimization (Sect.IV). The optimization is guided by topologically distinctive paths extracted and carefully selected from the topological path searching, which will be detailed in Sect.V. Optimistic assumption is adopted in this step. Secondly, the perception-aware planning strategy is utilized. The best trajectory among the locally optimal ones is further polished by a risk-aware trajectory refinement, in which its safety and visibility to the unknown and dangerous space is improved, as presented in Sect.VI. Based on the refined trajectory, the yaw angle is planned to actively explore the unknown environments (Sect.VII). The global planning, mapping, estimation and controller are introduced briefly in Sect.VIII-A.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Path-Guided Trajectory Optimization", "weight": 1.0} -->

As showed in Sect.II-A, GTO methods are effective for replanning, but suffer from local minima. To further improve the robustness of replanning and ensure flight safety, we present PGO, which utilizes a geometric guiding path in the optimization to guarantee its success.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Optimization Failure Analysis", "weight": 1.0} -->

Previous work showed that failure of GTO is relevant to unfavorable initialization, i.e., initial paths that pass through obstacles in certain ways usually get stuck. Underlying reason for this phenomenon is illustrated in Fig.4. Typical GTO methods incorporate the gradients of a Euclidean signed distance field (ESDF) in a collision cost to push the trajectory out of obstacles. Yet there are some "valleys" or "ridges" in the ESDF, around which the gradients differ greatly. Consequently, if a trajectory is in collision and crosses such regions, the gradients of ESDF will change abruptly at some points. This can make gradients of the collision cost push different parts of the trajectory in opposing directions and fail the optimization.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-A Optimization Failure Analysis", "weight": 1.0} -->

Normally, such "valleys" and "ridges", which corresponds to the space that has an identical distance to the surfaces of nearby obstacles, are difficult to avoid, especially in complex environments. Therefore, optimization depending solely on the ESDF fails inevitably at times. To solve the problem, it is essential to introduce extra information that can produce an objective function whose gradients consistently deform the trajectory to the free space.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Problem Formulation", "weight": 1.0} -->

We propose PGO built upon our previous work that represents trajectories as B-splines for more efficient cost evaluation. For a trajectory segment in collision, we reparameterize it as a $p_{b}$ degree uniform B-spline with control points $\left\{ \mathbf{q}_{0},\mathbf{q}_{1},\ldots,\mathbf{q}_{N} \right\}$ and knot span $\Deltat$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Problem Formulation", "weight": 1.0} -->

PGO consists of two different phases. The first phase generates an intermediate warmup trajectory. As concluded above, external information should be included to effectually deform the trajectory, since solely applying the ESDF could be futile. We employ a geometric guiding path to attract the initial trajectory to the free space (depicted in Fig. 5(a)) since collision-free paths are readily available from standard methods like A\* and RRT\*. In our work, the paths are provided by the sampling-based topological path searching (Sect. V).

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Problem Formulation", "weight": 1.0} -->

where $f_{s}$ is the smoothness term, while $f_{g}$ penalize the distance between the guiding path and the B-spline trajectory. As, $f_{s}$ is designed as a elastic band cost function^22^2Only the subset of control points $\{\mathbf{q}_{p_{b}},\mathbf{q}_{p_{b} + 1},\cdots,\mathbf{q}_{N - p_{b}}\}$ is optimized due to the boundary state constraints of the trajectory. $\mathbf{q}_{p_{b} - 2}$, $\mathbf{q}_{p_{b} - 1}$, $\mathbf{q}_{{N - p_{b}} + 1}$ and $\mathbf{q}_{{N - p_{b}} + 2}$ are needed to evaluate the smoothness. that simulates the elastic forces of a sequence of springs.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B Problem Formulation", "weight": 1.0} -->

To simplify the design of $f_{g}$, we utilize the property that the shape of a B-spline is finely controlled by its control points. Each control point $\mathbf{q}_{i}$ is assigned with an associated point $\mathbf{g}_{i}$ on the guiding path, which is uniformly sampled along the guiding path. Then $f_{g}$ is defined as the sum of the squared Euclidean distance between these point pairs.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Problem Formulation", "weight": 1.0} -->

Notably, minimizing $f_{p1}$ yields an unconstrained quadratic programming problem, so its optimal solution can be obtained in closed form. It outputs a smooth trajectory in the vicinity of the guiding path. Since the path is already collision-free, usually the warmup trajectory is also so. Even though it is not completely collision-free, its major part will be attracted to the free space. At this stage, the gradients of ESDF along the trajectory vary smoothly, and the gradients of the objective function push the trajectory to the free space in consistent directions. Hence, standard GTO methods can be utilized to improve the trajectory.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Problem Formulation", "weight": 1.0} -->

$v_{\text{max}}$ and $a_{\text{max}}$ are single-axis maximum velocity and acceleration. The formulations of $f_{c}$, $f_{v}$, and $f_{a}$ are based on the convex hull property of B-spline, thanks to which it suffices to constrain the control points of the B-spline to ensure safety and dynamic feasibility. For brevity, we refer the readers to for more details.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Problem Formulation", "weight": 1.0} -->

Although PGO has one more step of optimization compared with previous methods, it can generate better trajectories within shorter time. The first-phase takes only negligible time, but generate a warmup trajectory that is easier to be further refined, which improve the overall efficiency.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Problem Formulation", "weight": 1.0} -->

(a) The green, blue and yellow trajectories are equivalent under the definition of homotopy, but represent substantially different motions.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Problem Formulation", "weight": 1.0} -->

(b) An illustration of UVD. The purple trajectory is distinctive to the yellow one, but is equivalent to the blue one.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Topological Path Searching", "weight": 1.0} -->

Given a geometric guiding path, our PGO method can obtain a locally optimal trajectory. However, this trajectory is restricted within a topologically equivalent class and not necessarily satisfactory, even with the guidance of the shortest path, as seen in Fig. 8(e) and 8(f). Actually, it is difficult to determine the best geometric path, since the paths do not contain high order information (velocity, acceleration, etc.), and can not completely reflect the true motion. Searching a kinodynamic path may suffice, but it takes excessive time to obtain a promising path with boundary state constraints at the start and end of the replanned trajectory.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Topological Path Searching", "weight": 1.0} -->

For a better solution, a variety of guiding paths are required. We propose a sampling-based topological path searching to find a collection of distinctive paths. Although methods are for this problem, none of them runs in real-time in complex 3D environments. We redesign the algorithm carefully to solve this challenging problem in real time.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A Topology Equivalence Relation", "weight": 1.0} -->

Although the concept of homotopy is widely used, it captures insufficient useful trajectories in 3D environments, as shown in Fig. 6(a). proposes a more useful relation in 3D space named visibility deformation (VD), but it is computationally expensive for equivalence checking. Based on VD, we define uniform visibility deformation (UVD), which also captures abundant useful trajectories, and is more efficient for equivalence checking.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-A Topology Equivalence Relation", "weight": 1.0} -->

Fig. 6(b) gives an example of three trajectories belonging to two UVD classes. The relation between VD and UVD is depicted in Fig. 7. Both of them define a continuous map between two paths $\tau_{1}{(s)}$ and $\tau_{2}{(s)}$, in which a point on $\tau_{1}{(s)}$ is transformed to a point on $\tau_{2}{(s)}$ through a straight-line. The major difference is that for UVD, point $\tau_{1}{(s_{1})}$ is mapped to $\tau_{2}{(s_{2})}$ where $s_{1} = s_{2}$, while for VD $s_{1}$ does not necessarily equals $s_{2}$. In concept, UVD is less general and characterizes subsets of VD classes.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-A Topology Equivalence Relation", "weight": 1.0} -->

Practically, it captures slightly more classes of distinct paths than VD, but is far less expensive ^33^3To test VD relation, one should compute a visibility diagram and do path searching within it, which has higher complexity than testing UVD. for equivalence checking.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A Topology Equivalence Relation", "weight": 1.0} -->

To test UVD relation, one can uniformly discretize $s \in {\lbrack 0,1\rbrack}$ to ${s_{i} = {i/K}},{i = {0,1,\ldots,K}}$ and check collision for lines $\overline{\tau_{1}{(s_{i})}\tau_{2}{(s_{i})}}$. For the piece-wise straight line paths (as in Alg. 1, Equivalent), we simply parameterize it uniformly, so that for any $s$ except $\tau{(s)}$ is the join points of two straight lines, $\left\| \frac{d\tau{(s)}}{ds} \right\| = {const}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B Topological Roadmap", "weight": 1.0} -->

Alg.1 is used to construct a UVD roadmap $\mathcal{G}$ capturing an abundant set of paths from different UVD classes. Unlike standard PRM containing many redundant loops, our method generates a more compact roadmap where each UVD class contains just one or a few paths (displayed in Fig.8(a)-8(c)).

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B Topological Roadmap", "weight": 1.0} -->

We introduce two different kinds of graph nodes, namely guard and connector, similar to the Visibility-PRM. The guards are responsible for exploring different part of the free space, and any two guards $g_{1}$ and $g_{2}$ are not visible to each other (line $\overline{g_{1}g_{2}}$ is in collision). Before the main loop, two guards are created at the start point $s$ and end point $g$. Every time a sampled point is invisible to all other guards, a new guard is created at this point (Line 6-7). To form paths of the roadmap, connectors are used to connect different guards (Line 7-19). When a sampled point is visible to exactly two guards, a new connector is created, either to connect the guards to form a topologically distinct connection (Line 19-20), or to replace an existing connector to make a shorter path (Line 16-17). Limits of time ($t_{max}$) or sampling number ($N_{max}$) are set to terminate the loop.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-B Topological Roadmap", "weight": 1.0} -->

With the UVD roadmap, a depth-first search augmented by a visited node list is applied to search for the paths between $s$ and $g$, similar to.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-C Path Shortening & Pruning", "weight": 1.0} -->

As shown in Fig. 8(d), some paths obtained from Alg. 1 may be detoured. Such paths are unfavorable, since in the first phase of PGO it can deform a trajectory excessively and make it unsmooth. Hence, Alg. 2 find a topologically equivalent shortcut path $\text{P}_{s}$ for each $\text{P}_{r}$ found by the depth-first search (illustrated in Fig. 9). The algorithm uniformly Discretizes $\text{P}_{r}$ to a set of points $\text{P}_{d}$. In each iteration, if a point $p_{d}$ in $\text{P}_{d}$ is invisible from the last point in $\text{P}_{s}$ (Line 3, 4), the center of the first occupied voxel blocking the view of $\text{P}_{s}.{\text{back}{}}$ is found (Line 5).

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-C Path Shortening & Pruning", "weight": 1.0} -->

This point is then pushed away from obstacles in the direction orthogonal to $l_{d}$ and coplanar to both $l_{d}$ and the ESDF gradient at $p_{b}$ (Line 6), after which it is appended to $\text{P}_{s}$ (Line 7). The process continues until the last point is reached.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-C Path Shortening & Pruning", "weight": 1.0} -->

Although in Alg. 1, redundant connection between two guards are avoided, there may exist a small number of redundant paths between $s$ and $g$ (Fig. 8(d)). To completely exclude repeated ones, we check the equivalence between any two paths and only preserve topologically distinct ones. Also note that the number of distinctive paths grows exponentially with the number of obstacles. In case of complex environments, it is computationally intractable to use all paths to guide parallel optimization. For this reason, we only select the first $K_{max}$ shortest paths. Paths more than $r_{max}$ times longer than the shortest one are also pruned away. Such strategies bound the complexity and will not miss the potentially optimal solution, because a very long path is very unlikely to result in the optimal trajectory.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-C Path Shortening & Pruning", "weight": 1.0} -->

10Ps.push_back(Pd.back)
Algorithm 2 Finding a topologically equivalent shortcut path Ps for Pr.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Risk-aware Trajectory Refinement", "weight": 1.0} -->

Our trajectory refinement takes the best trajectory from the parallel PGO $\mathbf{p}_{i}{(t)}$ as input, modifies it in its vicinity and outputs the refined trajectory $\mathbf{p}_{r}{(t)}$ (detailed in Alg.3). It starts by checking the visibility status of $\mathbf{p}_{i}{(t)}$, after which the visibility to relevant unknown space and the safe reaction distance are enforced in the iterative refinement.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VI-A Checking Visibility Status", "weight": 1.0} -->

The visibility status is encoded by several variables: $t_{f},\mathbf{p}_{f}$, $t_{c},\mathbf{p}_{c},\mathbf{v}_{c}$, which are important information about the unknown space passed through by $\mathbf{p}_{i}{(t)}$. Some of the involved variables are illustrated in Fig.10.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VI-A1 Frontier Intersecting Point", "weight": 1.0} -->

As the unknown environment is only partially observed, at some time $t_{f}$ the trajectory $\mathbf{p}_{i}{(t)}$ exits the known-free space and enters the unknown space. The position $\mathbf{p}_{f} = {\mathbf{p}_{i}{(t_{f})}}$, should be prioritized for observation due to three reasons: First, it is highly relevant for the future flight, because it belongs to a promising trajectory going toward the goal. Second, it may be dangerous to the flight. In the worst case an unknown obstacle can be right adjacent to it. Third, it will be reached earlier compared to other unknown position along $\mathbf{p}_{i}{(t)}$. Therefore in $\text{FrontierIntersection}{}$ we search along $\mathbf{p}_{i}{(t)}$ with a discrete time step, recording the first unknown point and the corresponding time.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VI-A2 Visibility Metric", "weight": 1.0} -->

During the flight, it is preferred that $\mathbf{p}_{f}$ becomes visible to some preceding positions on $\mathbf{p}_{i}{(t)}$. Quantitatively, we want some visibility level $\psi$ of $\mathbf{p}_{f}$ to be not less than an expected level $\psi_{min}$, so that not only $\mathbf{p}_{f}$ is visible but also the visibility level is tolerant to external disturbance.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VI-A2 Visibility Metric", "weight": 1.0} -->

which represents the the smallest Euclidean signed distance between the line segment $l{(\mathbf{p},\mathbf{p}_{f})}$ and obstacles. The evaluation of Equ.5 requires traversing $l{(\mathbf{p},\mathbf{p}_{f})}$ and checking the Euclidean signed distance for each point. Fortunately, an ESDF derived from the occupancy grid map is maintained by our mapping module for supporting the trajectory optimization (Sect.IV), so minimal distance can be queried in constant time.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VI-B Iterative Refinement", "weight": 1.0} -->

As is the worst case, an unknown obstacle may be revealed right behind $\mathbf{p}_{f}$ and block the trajectory. To ensure safety, we refine $\mathbf{p}_{i}{(t)}$ so that under the worst case the quadrotor will be able to avoid collision by taking some maneuvers whose single-axis acceleration does not exceed the limit $a_{max}$. We first check whether $\mathbf{p}_{i}{(t)}$ satisfies the worst-case safety criteria (Line 5-7). If it does not, the critical view and safe reaction distance constraints are enforced (Line 8-15).

<!-- chunk {"id": "body-0052", "role": "body", "section": "VI-B1 Worst-case Safety Criteria", "weight": 1.0} -->

As showed in Sect.VI-A3, initially $\mathbf{p}_{f}$ will not become reliably viewable until $t_{c}$ at $\mathbf{p}_{c}$. Suppose at $\mathbf{p}_{c}$ the speed is $v_{c}$, while the distance to $\mathbf{p}_{f}$ is $d_{cf}$. Similar to, we check if Equ.6

<!-- chunk {"id": "body-0053", "role": "body", "section": "VI-B1 Worst-case Safety Criteria", "weight": 1.0} -->

which means that if at $\mathbf{p}_{c}$ the quadrotor sees an obstacle, it can decelerate to a stop before colliding with the obstacle right behind $\mathbf{p}_{f}$. $R_{q}$ compensates the quadrotor size and disturbance. If it is not true, extra constraints are added to meet this criteria.

<!-- chunk {"id": "body-0054", "role": "body", "section": "VI-B2 View and Safety Constraints", "weight": 1.0} -->

If initially it would be too late for collision avoidance, $\mathbf{p}_{f}$ should be viewed at an earlier stage $t_{s} < t_{c}$, so that maneuvers to avoid collision can be taken in advance.

<!-- chunk {"id": "body-0055", "role": "body", "section": "VI-B2 View and Safety Constraints", "weight": 1.0} -->

where $d_{s}$ is the safe reaction distance that depends on the speed $v_{s}$ at the refined trajectory $\mathbf{p}_{r}{(t_{s})}$: $d_{s} = {{{v_{s}^{2}/2}a_{max}} + R_{q}}$. However, since the refined trajectory is not obtained yet, $v_{s}$ is not available at this stage. To solve this chicken-and-egg problem, we introduce an iterative strategy. At the beginning we use the average speed of the segment of $\mathbf{p}_{i}{(t)}$ between $\left\lbrack t_{0},t_{f} \right\rbrack$ as an estimate of $v_{s}$ (Line 8), where $t_{0}$ is the start time of $\mathbf{p}_{i}{(t)}$. Then the trajectory is refined with the view and safety constraints (Line 10-12).

<!-- chunk {"id": "body-0056", "role": "body", "section": "VI-B2 View and Safety Constraints", "weight": 1.0} -->

After the refinement we check whether the new trajectory satisfies the safety criteria. If it does not, we increased the estimated speed ${\hat{v}}_{s}$ with a factor $\alpha$ slightly larger than 1 and redo the refinement (Line 13-15). This strategy is complete because it only terminates after the safety criteria is indeed met. It also terminates quickly, since the speed along the smooth trajectory varies slightly and it only takes one or a few steps to find a good estimate of $v_{s}$ in practice.

<!-- chunk {"id": "body-0057", "role": "body", "section": "VI-B2 View and Safety Constraints", "weight": 1.0} -->

$\text{RefineTrajectory}{}$ is essentially optimizing the trajectory with the newly introduced view and safety constraints. To incorporate them into our gradient-based optimization (Sect.IV-B), Equ.7-9

<!-- chunk {"id": "body-0058", "role": "body", "section": "VI-B2 View and Safety Constraints", "weight": 1.0} -->

Here $\mathcal{F}{}$ is the penalty function (Equ.3).

<!-- chunk {"id": "body-0059", "role": "body", "section": "VI-B2 View and Safety Constraints", "weight": 1.0} -->

where $f_{p2}$ is exactly the same as Equ.2. Note that applying the constraints to different $t_{s}$ generates different results. However, including $t_{s}$ into the optimization to find its best value would make the problem too difficult to be solved quickly. For simplicity, we first determine $t_{s}$ as the time that minimizes $f_{\mathbf{d}_{v}} + {w_{r}f_{\mathbf{d}_{sf}}}$ for the initial $\mathbf{p}_{i}{(t)}$ and use it for the refinement (Line 11-12). Quantitatively, the selected $t_{s}$ leads to minimal violation of the constraints, therefore enforcing the constraints at $t_{s}$ also requires less modification to $\mathbf{p}_{i}{(t)}$, which is a reasonably good choice.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Yaw Angle Planning", "weight": 1.0} -->

Quadrotors typically have limited sensor FOVs. To improve flight safety, we plan the trajectory of yaw angle to actively observe the environments. Inspired by the recent two-step quadrotor motion planning paradigm, we also decompose the yaw angle planning into a graph search problem and a trajectory optimization.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VII-A1 Problem Modeling", "weight": 1.0} -->

We model a graph search problem to seek for an sequence of yaw angles $\Xi:=\left\{ \xi_{0},\xi_{1},\cdots,\xi_{M} \right\}$ along the refined trajectory that trades off the smoothness and information gain (IG, detailed in Sect.VII-A2) of the unknown space. Given the quadrotor trajectory $\mathbf{p}_{r}{(t)}$ (Sect.VI), a set of positions ${\mathbf{p}_{r,i},i} \in \lbrack 0,1,\cdots,M\rbrack$ uniformly distributed along the trajectory at $\left\{ t_{0},t_{1},\cdots,t_{M} \right\}$ are selected.

<!-- chunk {"id": "body-0062", "role": "body", "section": "VII-A1 Problem Modeling", "weight": 1.0} -->

At $\mathbf{p}_{i}$ expect $i = 0$, where the yaw angle is already determined by the current quadrotor's state, several graph nodes ${n_{i,j},j} \in \lbrack 0,1,\cdots,J\rbrack$ are created, each of which associates a different angle $\xi_{i,j}$ and the IG $g_{i,j}$ at the state $\left( \mathbf{p}_{r,i},\xi_{i,j} \right)$. For each pair of nodes $n_{i,j_{1}},n_{{i + 1},j_{2}}$ associated with adjacent positions, a graph edge from $n_{i,j_{1}}$ to $n_{{i + 1},j_{2}}$ is created.

<!-- chunk {"id": "body-0063", "role": "body", "section": "VII-A1 Problem Modeling", "weight": 1.0} -->

This process construct a directed graph as shown in Fig.12.

<!-- chunk {"id": "body-0064", "role": "body", "section": "VII-A1 Problem Modeling", "weight": 1.0} -->

where $\mu$ is used to adjust the weighting of smoothness.

<!-- chunk {"id": "body-0065", "role": "body", "section": "VII-A2 Information Gain", "weight": 1.0} -->

We employ a similar method to which assesses potential IG as the number of unmapped voxels that comply with the camera model and are visible (not blocked by occupied voxels). However, the original method does raycasting for every voxels inside the camera FOV to validate their visibility, which is too expensive to function online. Therefore, we adapt it to better suit the real-time planning in several ways: (a) As is, voxels inside the FOV are subsampled to approximate the actual gain, which leads to only slight error but great run time reduction. (b) The gains of different $\xi_{i,j}$ are evaluated in parallel. (c) We borrow the techniques from to avoid repeated raycasting. As depicted in Fig.13(a), we notice that at one position $\mathbf{p}_{r,i}$ where different $\xi_{i,j}$ are assessed, many voxels are in overlapping areas and are checked for visibility more than once.

<!-- chunk {"id": "body-0066", "role": "body", "section": "VII-A2 Information Gain", "weight": 1.0} -->

To avoid unnecessary repetition, we store the visibility of each voxel when it is checked for the first time, so that in subsequent check the visibility and be queried directly. In these ways, the overall IG evaluation time is reduced by over two orders of magnitude.

<!-- chunk {"id": "body-0067", "role": "body", "section": "VII-A2 Information Gain", "weight": 1.0} -->

In the context of exploration, every voxel contributes equally to the IG of one quadrotor configuration, ensuring that all space can be covered by the sensors uniformly. However, in a point-to-point navigation we do not aim at full coverage but prefer focusing on space relevant to the flight. In particular, unknown voxels closer to the trajectory and the current position have higher influence to the flight. Therefore, we use Equ.16

<!-- chunk {"id": "body-0068", "role": "body", "section": "VII-B Yaw Angle Optimization", "weight": 1.0} -->

Given the optimal path $\Xi$ searched through the graph, we compute the trajectory of yaw angle $\phi{(t)}$ that is smooth, dynamically feasible and passes through the sequential angles $\xi_{j}$. We parameterize $\phi{(t)}$ as a uniform B-spline with control points $\Phi:=\left\{ \phi_{c,0},\phi_{c,1},\cdots,\phi_{c,N_{c}} \right\}$ and knot span $\deltat_{\phi}$. In this way, the convex hull property can be employed to ensure dynamic feasibility.

<!-- chunk {"id": "body-0069", "role": "body", "section": "VII-B Yaw Angle Optimization", "weight": 1.0} -->

Here the first term represents smoothness and the second term is a soft waypoint constraint enforcing $\phi{(t)}$ to pass through $\Xi$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "VII-B Yaw Angle Optimization", "weight": 1.0} -->

Thanks to the convex hull property of B-spline, the entire trajectory is guaranteed to be feasible given that the control points do not exceed the dynamic limits ${\overset{˙}{\phi}}_{max},{\overset{¨}{\phi}}_{max}$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "VIII-A Implementation Details", "weight": 1.0} -->

We present tests in both real world and simulation. In real-world experiments, a customized quadrotor platform equipped with an Intel RealSense Depth Camera D435 is used. All the state estimation, mapping, planning and control modules run on an Intel Core i7-8550U CPU. For simulation, we use a simulating tool containing the quadrotor dynamics model, random map generator and depth image renderer. The dynamics model relies on a numeric ODE solver odeint^44^4www.boost.org/doc/libs/1_73_0/libs/numeric/odeint/doc/html/index.html. The depth images are rendered in GPU by projecting point cloud of the surrounding obstacles onto the image plane. Random noises are added to them to better mimic the real measurements. All simulations run on an Intel Core i7-8700K CPU and GeForce GTX 1080 Ti GPU. The trajectory optimization is solved by a general non-linear optimization solver NLopt^55^5

<!-- chunk {"id": "body-0072", "role": "body", "section": "VIII-A1 Global Planning", "weight": 1.0} -->

We use the approach to compute global reference trajectories. Note that we focus on evaluating the local replanning system, therefore, naive global trajectories are given, such as straight-line trajectory connecting the start and goal positions.

<!-- chunk {"id": "body-0073", "role": "body", "section": "VIII-A2 Volumetric Mapping", "weight": 1.0} -->

In all tests, the quadrotor starts with no prior knowledge of the environments. A volumetric mapping framework fuses the depth images from the stereo camera into a occupancy grid map. An ESDF is derived from the occupancy grid map using an efficient distance transform algorithm to support the gradient-based optimization (Sect.IV) and visibility evaluation (Sect.VI-A2). Trilinear interpolation is also used to reduce the distance error induced by the discrete grid map.

<!-- chunk {"id": "body-0074", "role": "body", "section": "VIII-A3 State Estimation and Control", "weight": 1.0} -->

We localize the drone by a robust visual-inertial state estimator in real-world tests. In simulation, ground truth odometry is generated by the quadrotor dynamics model. We use a geometric controller to track both the position and yaw trajectory.

<!-- chunk {"id": "body-0075", "role": "body", "section": "VIII-A3 State Estimation and Control", "weight": 1.0} -->

The following evaluation is divided into two parts. The first part evaluates the perception-aware planning strategy, the second part tests the whole replanning framework.

<!-- chunk {"id": "body-0076", "role": "body", "section": "VIII-A3 State Estimation and Control", "weight": 1.0} -->

(c) Trajectories generated by the proposed method (red), FASTER (green), EWOK (cyan) and RE Traj. (yellow). Obstacles are set as gray transparent for clarity.

<!-- chunk {"id": "body-0077", "role": "body", "section": "VIII-B1 Real-world Tests", "weight": 1.0} -->

We conduct comparative experiments to show the importance of introducing active perception. Specifically we compare the proposed strategy: the risk-aware refinement (Sect.VI) and active exploration yaw (Sect.VII) with the commonly used ones: the optimistic assumption and the velocity-tracking yaw. Optimistic assumption treats all unknown space as collision-free, which is frequently adopted such as. The velocity-tracking yaw relates the desired yaw angle to the velocity: ${\phi{(t)}} = {\text{arctan}{(\frac{v_{y}{(t)}}{v_{x}{(t)}})}}$, to increase the chance of seeing obstacles. Four local planners listed in Tab.I are tested in two scenes. Each planner is tested 3 times in both scenes and we record the number of successful flights. The maximum velocity and acceleration are set as ${3m}/s$ and ${2.5m}/s^{2}$. Whenever collision along the trajectory is detected and the collision point is closer than $0.5m$, emergency stop is conducted immediately for safety.

<!-- chunk {"id": "body-0078", "role": "body", "section": "VIII-B1 Real-world Tests", "weight": 1.0} -->

In the first scene, a straight-line global reference trajectory is given (Fig.14(a)). A large obstacle consisting of several boxes and boards are placed on the way. When the quadrotor approaches the obstacle, boxes in the front row will be revealed first, while others behind them are occluded and invisible at the beginning. Planners with optimistic assumption (A & B) are unaware of the potential danger behind. They simply replan trajectories to avoid the viewed boxes, along which there is low visibility to the boxes in the back, as showed in Fig.16(a). As a result, the quadrotor gets 'surprised' by the occluded boxes afterwards and pauses in emergency, as showed in Fig.15(a) and 15(b). In contrast, planners with risk awareness (C & D) generate trajectories that deviate a bit more laterally, along which visibility toward the unknown area in the back is higher (Fig.16(b)). Therefore in both cases the quadrotor reach the goal more times.

<!-- chunk {"id": "body-0079", "role": "body", "section": "VIII-B1 Real-world Tests", "weight": 1.0} -->

However, with the velocity-tracking yaw (planner C), the quadrotor does not face toward the unknown area in the back quickly, which postpones the discovery of occluded boxes and causes 1 failure. In comparison, with the active exploration yaw (planner D) the quadrotor quickly turns toward the unknown area and observes the previously occluded boxes, enabling itself to take action earlier. This comparison is displayed in Fig.17.

<!-- chunk {"id": "body-0080", "role": "body", "section": "VIII-B1 Real-world Tests", "weight": 1.0} -->

In the second scene, an obstacle is placed right behind the corner, which is invisible to the quadrotor until it turns right. The reference trajectory is set to pass through the obstacles deliberately (Fig.14(b)). In this scene, the quadrotor can only reach the goal safely with planner D. For other three planners, the quadrotor collides with the obstacle behind the corner, due to either the poor visibility of the replanned trajectories (planner A & B), or the delay of perception caused by the velocity-tracking yaw (planner C). Note that even emergency stop is conducted, the quadrotor fail to avoid collision in time (Fig.18). The comparisons of the replanned trajectories and yaw angle are displayed in Fig.19 and Fig.20 respectively.

<!-- chunk {"id": "body-0081", "role": "body", "section": "VIII-B1 Real-world Tests", "weight": 1.0} -->

The experiments demonstrate two critical factors to survive in high-speed flights: (a) having good visibility toward the unknown regions that will influence the flight and (b) looking toward the relevant direction to eliminate those unknown regions actively. The proposed method takes into account these factors and guarantees safety for fast flight. More details about the experiments are presented in the attached video.

<!-- chunk {"id": "body-0082", "role": "body", "section": "VIII-B2 Benchmark Comparisons", "weight": 1.0} -->

We compare the proposed strategy with the safe local exploration (SLE) presented in in simulation. This strategy originated from the "next-best-view" planner in the exploration literature, but is adapted for online functioning in goal reaching tasks. It repeatedly selects intermediate goals that are closer to the final goal and have higher information gain, after which a local planner replans new trajectories toward the goals. It also adopts the velocity-tracking yaw, as is detailed in Sect.VIII-B1. To compare the strategies fairly, we integrated both of them with our robust optimistic replanning (Sect.IV, V). They are tested in $10$ random maps with $5$ different obstacle densities, $5$ trials are conducted for each map. We compare the number of successful flight, flight time and flight distance. Samples of the maps are displayed in Fig.22(a), 22(b).

<!-- chunk {"id": "body-0083", "role": "body", "section": "VIII-B2 Benchmark Comparisons", "weight": 1.0} -->

As is shown in Tab.II, the proposed strategy achieves higher number of successful flights when the scene gets more cluttered. Our strategy enforces visibility to dangerous unknown areas, and control the yaw angle to observe those areas actively. Therefore it can guarantee safety even the environment becomes very complex. For SLE, the velocity-tracking yaw is the major cause of failure, as it may not face toward dangerous unknown regions in time, as has been shown in Sect.VIII-B1.

<!-- chunk {"id": "body-0084", "role": "body", "section": "VIII-B2 Benchmark Comparisons", "weight": 1.0} -->

(a) The quadrotor passes a horizontal cardboard, after which it will avoid the vertical pillar.

<!-- chunk {"id": "body-0085", "role": "body", "section": "VIII-B2 Benchmark Comparisons", "weight": 1.0} -->

(b) Composite image of the flight experiment.

<!-- chunk {"id": "body-0086", "role": "body", "section": "VIII-B2 Benchmark Comparisons", "weight": 1.0} -->

(c) The quadrotor flies in the narrow passages and avoids boxes.

<!-- chunk {"id": "body-0087", "role": "body", "section": "VIII-B2 Benchmark Comparisons", "weight": 1.0} -->

Besides, our strategy is also more beneficial to achieve lower flight distance and time than SLE. SLE only selects intermediate goals and plans within the known unoccupied space, which is conservative. Besides, since the selection of intermediate goals takes information gain into account, the quadrotor tends to take some detours to gather more information, which leads to longer flight distance and time. In contrast, our strategy plans in both the known and unknown space, allowing more aggressive behaviors under the premise of safety. Moreover, instead of treating all unknown areas equally, it only focus on observing areas that are more relevant to the flight, which eliminates many unnecessary detours and improve the overall flight efficiency.

<!-- chunk {"id": "body-0088", "role": "body", "section": "VIII-C1 Benchmark Comparisons", "weight": 1.0} -->

We compare our replanning framework with several state-of-the-art methods, FASTER, EWOK and RE Traj.. FASTER belongs to the hard-constrained category (Sect.II-A), and features maintaining a feasible and safe back-up trajectory in the free-known space at each replanning step to improve safety. It also adopts a mixed integer quadratic program (MIQP) formulation to obtain a more reasonable time allocation of the trajectories. Both belong to the gradient-based methods. They utilize a uniform B-spline trajectory representation to replan efficiently. further exploits the convex hull property of B-spline and introduces a kinodynamic path searching to find more promising initial trajectories. We also test the four methods in 10 random maps with 5 obstacle densities. Note that all benchmarked methods are open-source and we use their default parameter settings. The number of successful flights, average flight distance, flight time, energy (integral of squared jerk), computation time of each replanning, and total replan number in each flight are recorded. Samples of the maps and the trajectories generated by the four methods are shown in Fig.22.

<!-- chunk {"id": "body-0089", "role": "body", "section": "VIII-C1 Benchmark Comparisons", "weight": 1.0} -->

As displayed in Fig.21, our method outperform others in the aspects of flight distance, flight time and energy consumption, with competitive computation efficiency. FASTER rarely fails in the tests, thanks to the back-up trajectories. However, due to the computationally demanding MIQP formulation, its overhead is higher. The other two benchmarked methods are more efficient. However, EWOK suffers from the local minima issue, so it usually fails or outputs low-quality solutions in dense environments. The kinodynamic path searching and B-spline optimization adopted by RE Traj. relieve the local minima significantly. Nonetheless, due to the lack of perception consideration, the succuss number is mediocre in dense environments. Compared to them, the proposed method search the solution space effectively with the guidance of topologically distinctive paths, and generates high-quality trajectories consistently. Safety is also reenforced by introducing perception awareness.

<!-- chunk {"id": "body-0090", "role": "body", "section": "VIII-C1 Benchmark Comparisons", "weight": 1.0} -->

(b) The quadrotor flies up the slope to the first goal (green circle), after which it flies toward the second goal.

<!-- chunk {"id": "body-0091", "role": "body", "section": "VIII-C2 Indoor Flight Test", "weight": 1.0} -->

We conduct aggressive flight experiments in three indoor scenes (Fig.2, 23) to validate our planning system. Various types of obstacles are placed randomly and densely to make up the challenging flight environments. Distance of neighboring obstacles are only around 1 meter, making the space for safe navigation very limited. Besides, the high obstacle density makes visibility to the environment very restricted, since many obstacles are occluded by others, which poses greater challenges to the replanning algorithm.

<!-- chunk {"id": "body-0092", "role": "body", "section": "VIII-C2 Indoor Flight Test", "weight": 1.0} -->

In each experiment, the final goal is set to 14$m$ away from the quadrotor. Straight-line global reference trajectories are given and local replanning is conducted within a horizon of 7 $m$. Samples of the online generated map and executed trajectories are presented in Fig.24. The velocity profile of one flight are showed in Fig.25(a), in which the maximum speed is ${2.90m}/s$ and average speed is ${1.77m}/s$. The flight distance and time are $14.12m$ and $8.0s$ respectively. We refer the readers to the attached video for more tests.

<!-- chunk {"id": "body-0093", "role": "body", "section": "VIII-C3 Outdoor Flight Test", "weight": 1.0} -->

Finally, we conduct fast flight tests in three different outdoor scenes, as displayed in in Fig.26, to validate our planning method in natural environments. The outdoor environments are typically unstructured and irregular, where the quadrotor should perform agile 3D maneuvers to avoid obstacles such as rocks and branches and leaves of trees. Note that despite the outdoor environments, we do not use external devices for localization.

<!-- chunk {"id": "body-0094", "role": "body", "section": "VIII-C3 Outdoor Flight Test", "weight": 1.0} -->

Results of the online generated map and executed trajectories are presented in Fig.27. In the first scene, the quadrotor flies through the forest to the goal $39m$ away from the initial position. The velocity profile is showed in Fig.25(b). The maximum speed is ${3.19m}/s$ and average speed is ${2.29m}/s$. The flight takes $40.78m$ and $17.83s$. In the second scene, the quadrotor flies up a slope to the first goal, after which it flies to the second goal. The first goal is $30m$ away and the change in height is $7m$. The second goal is $17m$ far. The whole flight takes $48.71m$ and $23.19s$. The third scene is a larger forest, where the goal is set to $45m$ away. The flight distance is $46.85m$, which takes $21.91s$ to finish. The maximum and average speed are ${3.41m}/s$ and ${2.14m}/s$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "VIII-C3 Outdoor Flight Test", "weight": 1.0} -->

More details of the flights are showed in the attached video.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper, we propose a robust and perception-aware replanning method for high-speed quadrotor autonomous navigation. The path-guided optimization and topological path searching are devised to escape from local minima and explore the solution space more thoroughly, through which higher robustness and optimality guarantee are obtained. The robust planner is further enhanced by the perception-aware strategy, which takes special caution about regions that may be dangerous to the quadrotor. The yaw angle of the quadrotor is also planned to actively explore the environments, especially areas that are relevant to the future flight. The planning system is evaluated comprehensively through benchmark comparisons. We integrate the planning method with global planning, state estimation, mapping, and control into a quadrotor platform and conduct extensive challenging indoor and outdoor flight tests. Results show that the proposed method is robust and capable of supporting fast and safe flights. We release the implementation of our system to the community.
