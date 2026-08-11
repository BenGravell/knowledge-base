<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Real-Time Capable Decision Making for Autonomous Driving Using Reachable Sets

Topics include Autonomous driving, Decision-making, Motion planning, Reachability analysis, Reachable sets, Driving corridors, Lane changes, Reference trajectories, CommonRoad.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces a real-time decision module that enumerates reachable driving corridors over a lanelet network, selects a corridor using lane-change and velocity costs, and generates a reference trajectory for downstream planners. Experiments on CommonRoad and CARLA show that the module accelerates both motion-primitive and optimization-based planning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Despite large advances in recent years, real-time capable motion planning for autonomous road vehicles remains a huge challenge. In this work, we present a decision module that is based on set-based reachability analysis: First, we identify all possible driving corridors by computing the reachable set for the longitudinal position of the vehicle along the lanelets of the road network, where lane changes are modeled as discrete events. Next, we select the best driving corridor based on a cost function that penalizes lane changes and deviations from a desired velocity profile. Finally, we generate a reference trajectory inside the selected driving corridor, which can be used to guide or warm start low-level trajectory planners. For the numerical evaluation we combine our decision module with a motion-primitive-based and an optimization-based planner and evaluate the performance on 2000 challenging CommonRoad traffic scenarios as well in the realistic CARLA simulator. The results demonstrate that our decision module is real-time capable and yields significant speed-ups compared to executing a motion planner standalone without a decision module.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A typical architecture for an autonomous driving system consists of a navigation module that plans a route (e.g. a sequence of roads that lead to the destination), a decision module that makes high-level choices like when to do a lane change or overtake another car, a motion planning module that constructs a collision-free and dynamically feasible trajectory, and a controller that counteracts disturbances like wind, model uncertainty, or a slippery road to keep the car on the planned trajectory. This paper presents a novel approach for decision making, which is based on reachable sets.

<!-- chunk {"id": "body-0005", "role": "body", "section": "I-A State of the Art", "weight": 1.0} -->

Let us first review the state of the art for decision making and motion planning for autonomous road vehicles. Motion planning approaches can be classified into the four groups graph search planners, sampling-based planners, optimization-based planners, and interpolating curve planners. Graph search planners represent the search space by a finite grid, where the grid cells represent the nodes and transitions between grid cells the edges of a graph. Motion planning then reduces to the task of finding the optimal path through the graph, which can be efficiently realized using graph search algorithms such as Dijkstra and A\*. The main disadvantage of this approach is the often large number of grid cells required to cover the search space, especially if spatio-temporal lattices are used as a grid. While for graph search planners the discrete motion primitives are deterministically defined by the grid, sampling-based planners choose motions randomly to explore the search space. For autonomous driving, this is often implemented using rapidly exploring random trees. Disadvantages are that sampling based planners in general do not find the optimal solution in finite time, and that the determined trajectories are often jerky and therefore have low driving comfort.

<!-- chunk {"id": "body-0006", "role": "body", "section": "I-A State of the Art", "weight": 1.0} -->

Optimization-based planners determine trajectories by minimizing a specific cost function with respect to the constraints of dynamic feasibility with the vehicle model and avoiding collisions with other traffic participants and the road boundary. The main challenge is to incorporate the non-convex collision avoidance constraints, which is often realized using mixed-integer programming, nonlinear programming with a suitable initial guess, or via successive convexification. However, all these methods are either computationally expensive or have the risk of getting stuck in local minima. Finally, interpolating curve planners construct trajectories by interpolating between a sequence of desired waypoints using clothoids, polynomial curves, Bezier curves, or splines. Obstacle avoidance can be realized by modifying the waypoints accordingly. While interpolating curve planners are able to create smooth trajectories with high comfort, the solutions might not be optimal with respect to a given cost function. A more detailed overview of different motion planning approaches is provided.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A State of the Art", "weight": 1.0} -->

Even though many of the above motion planners already have the ability to make decisions, it is still a common practice to separate high-level decision making from low-level trajectory planning since this usually simplifies the motion planning problems and therefore improves computational efficiency. One frequently applied method is rule-based decision making, which is often realized using state-machines. Another approach is topological trajectory grouping, which selects topological patterns from a pool of trajectories. Also hybrid automata can be used for decision making, where the discrete modes of the automaton represent the high-level decisions. Yet another strategy is to apply reinforcement learning for high-level decision making. Finally, some recent approaches use set-based reachability analysis to identify potential driving corridors. These methods linearize the system around a given reference path to construct the drivable area by computing the reachable set in longitudinal and lateral direction. However, this has the disadvantage that the linearization can become very inaccurate or conservative if the vehicle significantly deviates from the reference path. Our approach avoids this problem since we only compute the reachable set for the longitudinal position along the lanelet, and model changes in lateral position as discrete events.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We represent the dynamics of the vehicle with a kinematic single track model \[38, Chapter 2.2\]: where the vehicle state consists of the position of the rear axis represented by $x$, $y$, the velocity $v$, and the orientation $\varphi$. The parameter $\ell_{\text{wb}}$ is the length of the vehicle's wheelbase, and the control inputs are the acceleration $a$ and the steering angle $s$, which are bounded by $a \in {\lbrack{- a_{\text{max}}},a_{\text{max}}\rbrack}$ and $s \in {\lbrack{- s_{\text{max}}},s_{\text{max}}\rbrack}$. Moreover, an additional constraint is given by the friction circle \[38, Chapter 13\] which models the maximum force that can be transmitted by the tires.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

lanelet, and a polygon $\mathcal{L} \subset {\mathbb{R}}^{2}$ representing the shape of the lanelet.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In addition to the road network, one also has to consider the other traffic participants such as cars or pedestrians for motion planning. We denote the space occupied by traffic participant $j$ at time $t$ by ${\mathcal{O}_{j}{(t)}} \subset {\mathbb{R}}^{2}$. For simplicity, we assume that $\mathcal{O}_{j}{(t)}$ is known for all surrounding traffic participants. In practice, the current positions of the surrounding traffic participants are obtained via perception using computer vision, LiDAR, radar, or combinations, and the future positions of the traffic participants can be determined using probabilistic or set-based prediction.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

A motion planning problem is defined by an initial state $x_{0}$, $y_{0}$, $v_{0}$, $\varphi_{0}$ for the vehicle and a goal region \\rsfsG $= {(\mathcal{G},\tau_{goal})}$ consisting of a goal set for the vehicle state ${\lbrack{xyv\varphi}\rbrack} \in \mathcal{G} \subseteq {\mathbb{R}}^{4}$ and a time interval $\tau_{\text{goal}} = {\lbrack t_{\text{start}},t_{\text{end}}\rbrack}$ at which this goal set should be reached.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

An exemplary motion planning problem is visualized at the top of Fig. 1. The task for motion planning is to determine control inputs $a{(t)}$ and $s{(t)}$ that drive the car from the initial state to the goal region under consideration of the vehicle dynamics in and such that the vehicle stays on the road and does not collide with other traffic participants at all times. In this paper we propose to solve motion planning problems with a novel decision making module that determines a suitable driving corridor that leads to the goal set and generates a desired reference trajectory inside this driving corridor. Our decision module can then be combined with a low-level trajectory planner that tracks the reference trajectory and generates the control input trajectories $a{(t)}$ and $s{(t)}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Input: Lanelet L = (id, left, right, S, ℓlane, ℒ), list of initial sets X = (𝒳 (tiinit), …, 𝒳 (tifin)), space occupied by the other traffic participants 𝒪1 (t), …, 𝒪o (t) Output: Drivable area D = (𝒟 (tiinit), …, 𝒟 (tiend)), lists Tleft, Tright, Tsuc with possible transitions to the left, right, and successor lanelets 1:𝒟 (tiinit)← set 𝒳 (tiinit) with the smallest time from X 2:Tleft, Tright, Tsuc ← ⌀ 3:F (t)← compute free space on current, left, right, and 4: successor lanelets from 𝒪1 (t), …, 𝒪o (t) (see) 5:// loop over all time steps 6:for i ← iinit to ⌈tend/Δ t⌉ do 7: // compute reachable set at next time step (see) 9: // unite with initial set for this time step 12: // intersect with free space on the lanelet 16: // terminate if

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

drivable area is empty 19: // check if a lane change to the right is possible 22: Tright← add set 𝒟 (ti + 1) ∩ ℱ to Tright 23: // check if a lane change to the left is possible 26: Tleft← add set 𝒟 (ti + 1) ∩ ℱ to Tleft 27: // check if a lane change to a successor is possible 32: Tsuc← add set 𝒟shift ∩ ℱ to Tsuc 33:// combine sets for successive steps into one transition 34:Tleft, Tright, Tsuc← group successive sets together Algorithm 1 Compute drivable area for a single lanelet

<!-- chunk {"id": "body-0015", "role": "body", "section": "Algorithm", "weight": 1.0} -->

We now present our novel approach for decision making.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Simplified Vehicle Dynamics", "weight": 1.0} -->

For the sake of computational efficiency, it is common practice to use a simplified version of the vehicle dynamics in for decision making. To obtain such a simplified model, we introduce a curvilinear coordinate frame that follows the lanelet centerline, and in which $\xi$ denotes the longitudinal position of the vehicles center along the corresponding lanelet. Moreover, we represent the vehicle as a discrete-time system with time step size $\Deltat$, where $t_{i} = {i\Deltat}$ are the corresponding time points and we assume without loss of generality that the initial time is $t_{0} = 0$. Our simplified model for decision making is then given by the following double integrator for the longitudinal position $\xi$ where $v$ is the velocity and $a_{i}$ is the constant acceleration of the vehicle during time step $i$. In the remainder of the paper we will use notation ${z{(t)}} = {\lbrack{\xi{(t)}v{(t)}}\rbrack}^{T}$ for the state of the simplified vehicle dynamics.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B Drivable Area", "weight": 1.0} -->

To determine all possible driving corridors, we use reachability analysis. The reachable set $\mathcal{R}{(t)}$ for system is defined as the set of longitudinal positions and velocities reachable under consideration of the bounded acceleration $\lbrack{- a_{\text{max}}},a_{\text{max}}\rbrack$. This set can be computed by the following propagation rule: where we represent sets by polygons. To avoid collisions with other traffic participants, we have to consider their occupied space $\mathcal{O}_{j}{(t)}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Drivable Area", "weight": 1.0} -->

Given a lanelet ${\text{L}} = {(\text{id},\text{left},\text{right},\mathbf{S},\ell_{\text{lane}},\mathcal{L})}$, we therefore first compute the set ${\mathcal{O}_{\text{long},\text{id},j}{(t)}} \subset {\mathbb{R}}$ of longitudinal lanelet positions occupied by obstacle $j$ at time $t_{i}$ from the occupied space $\mathcal{O}_{j}{(t_{i})}$ in the global coordinate frame. Using this set, we can compute the free space on the lanelet as follows: where we subtract the occupied space for all $o$ traffic participants and bloat the obstacles by the length of the ego vehicle $\ell_{\text{car}}$ as well as by a user-defined minimum distance $d_{\text{min}}$ we want to keep to the other traffic participants.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Drivable Area", "weight": 1.0} -->

In addition, we take the Cartesian product with the set of legal velocities $\lbrack 0,v_{\text{max},\text{id}}\rbrack$, where $v_{\text{max},\text{id}}$ is the speed limit for the current lanelet. Since the free space $\mathcal{F}_{\text{id}}{(t_{i})}$ in general consists of multiple disjoint regions, we introduce the list $\mathbf{F}_{\text{id}}{(t_{i})}$ that stores all these disjoint regions. The drivable area is finally given by the intersection of the reachable set with the free space on the lanelet: While equations enable us to compute the drivable area for a single lanelet, we additionally have to consider transitions between the lanelets to obtain the drivable area for the whole road network. This procedure is summarized in Alg. 1, which computes the drivable area for a single lanelet under consideration of transitions.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Drivable Area", "weight": 1.0} -->

The algorithm takes as input a list of drivable areas that correspond to transitions to the given lanelet and computes the drivable area for the lanelet as well as all possible transitions to left, right, or successor lanelets.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-C Driving Corridor Selection", "weight": 1.0} -->

Using the approach for computing the drivable area for a single lanelet together with possible transitions to other lanelets in Alg. 1, we can formulate the identification of possible driving corridors as a standard tree search problem, where each node consists of a lanelet and a corresponding drivable area. This procedure is summarized in Alg. 2 and visualized for an exemplary traffic scenario in Fig. 1. Once we identified all driving corridors that reach the goal set, we finally have to select the best driving corridor in Line 20 of Alg. 2. For this, we use the cost function where $n_{\text{change}}$ is the number of lane changes for the driving corridor, $d_{\text{profile}}$ is the average deviation from a desired position-velocity-profile $z_{\text{des}}{(t)}$, and ${w_{\text{change}},w_{\text{profile}}} \in {\mathbb{R}}_{\geq 0}$ are user-defined weighting factors.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-C Driving Corridor Selection", "weight": 1.0} -->

For the desired position-velocity-profile, we choose to accelerate to the current speed limit $v_{\text{max},\text{id}}$ with a user-defined desired acceleration $a_{\text{des}}$: with ${z{(t_{0})}} = {\lbrack{\xi_{0}v_{0}}\rbrack}^{T}$ and The deviation $d_{\text{profile}}$ is given as the minimum deviation inside the drivable area $\mathcal{D}{(t_{i})}$ averaged over all time steps: If the driving corridor contains multiple drivable areas on different lanelets for the same time step, we take the minimum deviation from all these areas. Moreover, we shift the desired position-velocity-profile by the lanelet length $\ell_{\text{lane}}$ when moving on to a successor lanelet.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Driving Corridor Selection", "weight": 1.0} -->

Input: Initial state x0, y0, v0, φ0 of the vehicle, road network given as a list of lanelets L = (L1, …, Lq), goal region \rsfsG = (𝒢, τgoal), space occupied by the other traffic participants 𝒪1 (t), …, 𝒪o (t) Output: Best driving corridor given by a sequence of lanelets Lfin = (L1, …, Lp) and the corresponding drivable areas Dfin = (D1, …, Dp), with Dk = (𝒟 (tkinit), … 𝒟 (tkend)) 1:L0← find lanelet for the initial state x0, y0, φ0 2:ξ0← transform x0, y0 into curvilinear coordinate system 3:Lgoal← find lanelet for the goal region 𝒢 4:𝒢long← transform 𝒢 into curvilinear coordinate system 5:Q← initialize queue with set [ξ0 v0]T and lanelet L0 7: X, L← list of initial sets and the corresponding 8: lanelet for first element from the queue Q 9: D,

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C Driving Corridor Selection", "weight": 1.0} -->

Tleft, Tright, Tsuc← compute drivable area for 10: lanelet \rsfsL starting from X using Alg.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Driving Corridor Selection", "weight": 1.0} -->

1 11: Tleft, Tright, Tsuc← remove entries that are already 12: covered by an existing drivable area 13: Q← add entries in Tleft, Tright, Tsuc and the 14: corresponding lanelets to the queue Q 16: if L = Lgoal ∧ ti ∈ τgoal ∧ 𝒟 (ti) ⊆ 𝒢long then 17: Ffin← add current driving corridor to Ffin 19:Lfin, Dfin← select driving corridor with the lowest 20: cost according to from Ffin Algorithm 2 Determine best driving corridor Figure 2: Trajectory planned by our decision module in combination with the optimization-based planner for the CommonRoad scenario DEU_Flensburg-73_1_T-1 visualized at times 0s, 3s, and 6s, where the ego vehicle is shown in red, the other traffic participants in blue, and the goal set in yellow.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-D Driving Corridor Refinement", "weight": 1.0} -->

While the driving corridor computed using Alg. 2 is guaranteed to contain at least one state sequence that leads to the goal set, it usually also contains states that do not reach the goal. To remove those states, we refine the computed driving corridor by propagating the reachable sets backward in time starting from the intersection of the final set $\mathcal{D}{(t_{\text{end}})}$ with the goal set $\mathcal{G}_{\text{long}}$ from Alg. 2. The refined drivable area is then given by the intersection of the backpropagated sets with the original drivable area, which corresponds to the following propagation rule: where ${\mathcal{D}{(t_{\text{end}})}} = {{\mathcal{D}{(t_{\text{end}})}} \cap \mathcal{G}_{\text{long}}}$. Again, we shift the drivable area by the lanelet length $\ell_{\text{lane}}$ when moving on to a predecessor lanelet.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-D Driving Corridor Refinement", "weight": 1.0} -->

III-E Reference Trajectory Generation As the last step of our approach, we generate a suitable reference trajectory inside the selected driving corridor. Optimally, we would like to drive with the desired position-velocity-profile zdes (t). However, this position-velocity-profile might not be located inside the driving corridor. We therefore generate the reference trajectory by choosing for each time step the point z (ti + 1) inside the drivable area 𝒟 (ti + 1) that is closest to zdes (ti + 1) and reachable from the previous state z (ti) given the dynamics: $${z{(t_{i + 1})}} = {\underset{z \in \mathcal{I}}{\text{argmin}}{\|{z - {z_{\text{des}}{(t_{i + 1})}}}\|}_{2}}$$ After generating the reference trajectory z (t) in the curvilinear coordinate frame, we have to transform it to the global coordinate frame.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-D Driving Corridor Refinement", "weight": 1.0} -->

Here, we obtain x (t), y (t) and φ (t) from the lanelet centerline, and v (t) is directly given by z (t). At lane changes to a left or right lanelet we interpolate between the lanelet centerlines x1 (t), y1 (t) and x2 (t), y2 (t) of the lanelets before and after the lane change as follows: \end{bmatrix} = {{{({1 - {\mu{(t)}}})}\begin{bmatrix} \end{bmatrix}} + {\mu{(t)}\begin{bmatrix} where tinit, tfin are the start and end time for the lane change. We now present several improvements for our algorithm. IV-A Traffic Rules So far, the only traffic rule we considered is the speed limit. However, our approach makes it easy to already incorporate many additional traffic rules on a high-level during driving corridor generation.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-D Driving Corridor Refinement", "weight": 1.0} -->

For example, traffic rules such as traffic lights, no passing rules, or the right-of-way can simply be considered by removing the space that is blocked by the traffic rule from the free space ℱid (t) on the lanelet. Other rules such as keeping a safe distance to the leading vehicle can be considered by adding the corresponding rule violations with a high penalty to the cost function. Incorporating traffic rule violations into the cost function ensures that our decision module can find a solution even if the initial state violates the rule. This can for example happen if another traffic participant performs an illegal cut-in in front of the ego vehicle, which makes it impossible to keep a safe distance at all times. IV-B Partially Occupied Lanelets Often, other traffic participants only occupy a small part of the lateral space on the lanelet, for example if a bicycle drives on one side of the lane. Classifying the whole lanelet as occupied in those cases would be very conservative and prevent the decision module from finding a feasible solution in many cases.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-D Driving Corridor Refinement", "weight": 1.0} -->

A crucial improvement for the basic algorithm in Sec. III is therefore to check how much of the lateral space is occupied by the other traffic participants, and only remove the parts where the remaining free lateral space is too small to drive on from the free space. We additionally correct the final reference trajectory accordingly to avoid intersections with other traffic participants that only partially occupy the lateral space of the lanelet. IV-C Cornering Speed Our algorithm in Sec. III assumes that the vehicle can drive around corners with arbitrary speed, which obviously is a wrong assumption since the vehicle speed in corners is limited by the friction circle. Therefore, we now derive a formula for the maximum corner speed given the lanelet curvature Δ φ/Δ ξ, which we use as an artificial speed limit for all lanelets.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-D Driving Corridor Refinement", "weight": 1.0} -->

Combining and finally yields $$v \leq \sqrt{{{a_{\text{max}}\Delta\xi}/\Delta}\varphi}$$ for the maximum corner velocity. In the implementation we compute Δ φ/Δ ξ for each segment of the lanelet and take the maximum over all segments. IV-D Minimum Lane Change Time Alg. 1 assumes that a single time step is sufficient to perform a lane change, which is unrealistic. We therefore now derive a formula that specifies how many time steps are required to perform a lane change.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-D Driving Corridor Refinement", "weight": 1.0} -->

$$t_{\text{fin}} \geq \sqrt{{4\Delta\eta}/a_{\text{max}}}$$ for the minimum time required for a lane change, where Δ η is the lateral distance between the lanelet centerlines.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-D Driving Corridor Refinement", "weight": 1.0} -->

We implemented our approach in Python, and all computations are carried out on a 3.5GHz Intel Core i9-11900KF processor. Our implementation is publicly available on GitHub111 and we published a repeatability package that reproduces the presented results on CodeOcean222 For the parameter values of our decision module we use ades = 1 m s−1 for the desired acceleration, dmin = 1 m for the minimum safe distance, and wchange = 10, wprofile = 1 for the weights of the cost function. Moreover, the time step size is Δ t = 0.1 s for CommonRoad and Δ t = 0.2 s for CARLA. V-A CommonRoad Scenarios CommonRoad is a database that contains a large number of challenging motion planning problems for autonomous vehicles, and is therefore well suited to evaluate the performance of our decision module. For the experiments, we combine our decision module with two different types of motion planners, namely a motion-primitive-based planner and an optimization-based planner.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-D Driving Corridor Refinement", "weight": 1.0} -->

To obtain the motion-primitive-based planner we used the AROC toolbox to create a maneuver automaton with 12793 motion primitives by applying the generator space control approach. For the optimization-based planner we solve an optimal control problem with the objective to track the reference trajectory generated by our decision module and the constraint of dynamical feasibility with the vehicle model. The results for the evaluation on 2000 CommonRoad traffic scenarios are listed in Tab. III-D, where we aborted the planning if the computation took longer than one minute. The outcome demonstrates that our decision module standalone on average runs about 10 times faster than real-time and can generate feasible driving corridors for all scenarios. Moreover, while the computation times for running the motion-primitive-based planner standalone are very high and the success rate is consequently quite low due to timeouts, in combination with our decision module the planner is real-time capable and can solve a large number of scenarios, which nicely underscores the benefits of using a decision module.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-D Driving Corridor Refinement", "weight": 1.0} -->

Finally, even though we do not consider any collision avoidance constraints, the optimization based planner still produces collision-free trajectories most of the time, which can be attributed to the good quality of the reference trajectories generated by our decision module. The planned trajectory for an exemplary traffic scenario is visualized in Fig. 2, where the ego vehicle overtakes a bicycle that drives at the side of the road. V-B CARLA Simulator In contrast to CommonRoad scenarios which consist of a single planning problem, for the CARLA simulator we use a navigation module to plan a route to a randomly chosen destination on the map. We then follow this route by replanning a trajectory with a duration of 3s every 0.3s until the vehicle reached the destination, where we combine our decision module with the optimization-based planner described in Sec. V-A. Moreover, since we use the high-fidelity vehicle model from CARLA for which the kinematic single track model in is just an approximation, we additionally apply a feedback controller that counteracts model uncertainties and disturbances. For the experiments we consider the Town 1 map and use a constant velocity assumption to predict the future positions of the surrounding traffic participants. Tab.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-D Driving Corridor Refinement", "weight": 1.0} -->

II displays the results for three different routes, and an exemplary snapshot from the CARLA simulator is shown Fig. 3. The outcome demonstrates that our decision module performs very well as part of a full autonomous driving software stack consisting of navigation, prediction, decision making, motion planning, and control, and therefore enables robust motion planning in real-time.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-D Driving Corridor Refinement", "weight": 1.0} -->

We presented a novel approach for decision making in autonomous driving, which applies set-based reachability to identify driving corridors. As we demonstrated with an extensive numerical evaluation on 2000 CommonRoad traffic scenarios, our decision module runs in real-time, can be combined with multiple different motion planners, and leads to significant speed-ups compared to executing a motion planner standalone. Moreover, our experiments in the CARLA simulator, for which we integrated our decision module into a full autonomous driving software stack, showcase that our approach performs well for a lifelike setup close to reality.
