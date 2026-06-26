<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-World Environments

Topics include Motion planning, Autonomous driving, Trajectory optimization, Safety, Real-world deployment, Experimentation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Optimization-based wrapper that converts any planner's trajectory sketch into a safe, comfortable, dynamically feasible trajectory, enabling rapid real-world testing of experimental ML and classical planners on self-driving vehicles without full safety-stack integration.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Human-level autonomous driving is an ever-elusive goal, with planning and decision making - the cognitive functions that determine driving behavior - posing the greatest challenge. Despite a proliferation of promising approaches, progress is stifled by the difficulty of deploying experimental planners in naturalistic settings. In this work, we propose Lab2Car, an optimization-based wrapper that can take a trajectory sketch from an arbitrary motion planner and convert it to a safe, comfortable, dynamically feasible trajectory that the car can follow. This allows motion planners that do not provide such guarantees to be safely tested and optimized in real-world environments. We demonstrate the versatility of Lab2Car by using it to deploy a machine learning (ML) planner and a classical planner on self-driving cars in Las Vegas. The resulting systems handle challenging scenarios, such as cut-ins, overtaking, and yielding, in complex urban environments like casino pick-up/drop-off areas. Our work paves the way for quickly deploying and evaluating candidate motion planners in realistic settings, ensuring rapid iteration and accelerating progress towards human-level autonomy.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Self-driving cars have achieved remarkable progress towards human-level autonomous driving. Much of this success is owed to progress in ML-based perception and prediction, which can attain a human-like understanding of the scene around the autonomous vehicle (AV). Classical motion planners relying on handcrafted rules have similarly given way to ML-based motion planners that learn the rules of driving from data. ML planning is thought to be more scalable and better positioned to capture the ineffable nuances of human driving behavior than classical planning.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, deploying ML planners in the real world comes with its own set of challenges, which are often overcome using techniques from classical planning. For one, naïve trajectory regression does not ensure comfort or even basic kinematic feasibility, necessitating post-hoc smoothing or hand-engineered trajectory generation. Ensuring safety poses an even greater challenge, as ML solutions tend to fail on edge cases that compose the long tail of the data distribution. Since the opacity of the implicitly learned rules makes it difficult to predict when such failures would occur, it is of paramount importance to institute interpretable guardrails when deploying ML planners in the real world. Previous authors have achieved this by projecting the ML trajectory onto a restricted set of lane-follow trajectories pre-filtered based on hand-engineered rules, an ad-hoc approach which does not scale to complex, unstructured scenarios. Other authors have proposed applying differentiable model predictive control (MPC) as the final layer of a neural AV stack to simultaneously ensure safety, comfort, and feasibility. However, these approaches were not deployed in the real world and come at the cost of increased complexity and tight coupling between the MPC and the planning module.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In all instances, making ML planners or even naïve classical planners deployable requires substantial engineering investment, which can only be justified if there is strong signal that they will drive well. Such signal could in principle be obtained in simulation; however, there is often a substantial gap between performance in simulation and on the road. As a result, few experimental planners get evaluated in the real world, and those that do are often part of bespoke deployment systems that cannot be readily extended to other planners.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this problem, we present Lab2Car, an optimization-based wrapper that takes a rough trajectory sketch and transforms it into a set of interpretable spatiotemporal constraints -- a maneuver -- which is then solved using MPC to obtain a safe, comfortable, and dynamically feasible trajectory (Fig. 1). The initial trajectory sketch captures the high-level behavioral intent, while the final trajectory captures the low-level sequence of commands that the robot must execute. This division of labor mirrors hierarchical motor control in biological brains and allows for robust and safe deployment of a wide range of experimental planners.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contributions are as follows: A simple yet powerful maneuver extraction algorithm that converts a trajectory sketch -- even a really poor one -- into constraints that preserve the underlying driving intent while ensuring safety.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Integration with multiple ML/classical planners and a state-of-the-art MPC solver as part of a full AV stack.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Evaluation on 2000+ resimulated scenarios from real-world drive logs using a high-fidelity simulator.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deployment on a real AV and evaluation on the road.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Maneuver definition", "weight": 1.0} -->

The input to Lab2Car is a path or trajectory sketch $\tau=\{(x_{k},y_{k},t_{k})\}_{k=0}^{K-1}$ consisting of a sequence of $K$ Cartesian waypoints $(x_{k},y_{k})$ with optional timestamps $t_{k}$. The trajectory is then converted to a maneuver: a set of spatiotemporal constraints (continuous in the spatial domain and discrete in the temporal domain) that define the feasible space of trajectories over the planning horizon (Fig. 2, left). Similarly to control barrier functions, the maneuver implicitly defines a safe region, while also optimizing for comfort and similarity to the trajectory sketch.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Maneuver definition", "weight": 1.0} -->

The baseline trajectory is modeled as a 2D quartic cardinal B-spline (Fig. 2 and Fig. 3, blue curve). The spline is defined by a set of $N$ control points and corresponding knot vectors. The knot vectors are placed at spline progress values $p$ from $0$ to $N$, The spline basis functions are valid within the domain spanning from $1.5$ to $N-2.5$, ensuring that the spline is smooth and well-defined across this range.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Maneuver definition", "weight": 1.0} -->

This baseline spline serves as the reference axis of a curvilinear coordinate system which defines all subsequent trajectory constraints in terms of longitudinal (along the spline) and lateral (orthogonal to the spline) components.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Maneuver definition", "weight": 1.0} -->

Tracking references are defined as a time series $(p_{\text{ref}}(t),v_{\text{ref}}(t),a_{\text{ref}}(t))$, specifying the progress, longitudinal velocity, and longitudinal acceleration, respectively, that the AV should aim to achieve at each time point $t$ of the discretized planning horizon (Fig. 2, blue arrows). These do not apply if $\tau$ is a path (i.e., has no timestamps).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Maneuver definition", "weight": 1.0} -->

Lateral constraints are formulated as 1D spline functions extending along the baseline spline, representing the driveable space boundaries at each time point $t$ (Fig. 2 and Fig. 3, green curves). These constraints are segmented into "hard" and "soft" constraints for both the left and right boundaries, indexed by spline progress: $\gamma_{\text{left,hard}}(p),\gamma_{\text{left,soft}}(p),\gamma_{\text{right,hard}}(p),\gamma_{\text{right,soft}}(p)$. A separate set of constraints is defined for each time point $t$ (omitted).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Maneuver definition", "weight": 1.0} -->

Longitudinal constraints are defined as a time series $(p_{\text{lower}}(t),p_{\text{upper}}(t))$ specifying the lower and upper bound on progress, respectively, at each time point $t$ of the planning horizon (Fig. 2 and Fig. 3, yellow and red lines).

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Baseline fitting", "weight": 1.0} -->

Fitting the baseline proceeds in two steps.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Baseline fitting", "weight": 1.0} -->

Step 1: Determining spline progress: Initially, the progress value $\hat{p}_{k}$ for each waypoint point along the spline is calculated to reflect the cumulative distance along the path: Here, $\mathbf{w}_{k}=\begin{bmatrix}x_{k},y_{k}\end{bmatrix}$ are waypoint vectors and $\text{dist}_{\text{max}}$ is the target distance between control points on the spline.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Baseline fitting", "weight": 1.0} -->

Step 2: Control point optimization: The control points $C$ of the spline are computed using a least squares method by solving: where $C$ is a $N\times 2$ matrix of control points, $\mathbf{b}$ is the spline basis function, $R$ is a second-order regularization matrix which penalizes excessive curvature, and $c_{reg}$ is the regularization coefficient.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Projection of dynamic obstacles onto baseline", "weight": 1.0} -->

Detections and predictions for other dynamic road entities, such as vehicles and pedestrians, are represented by time series of convex hulls subsampled to sets of $(x,y)$ points. The sampled points are then transformed into a curvilinear coordinate system aligned with the baseline, referred to as "spline-space" (Fig. 2, right). In this coordinate system, each point is expressed as $(p,n)$, where $p$ denotes progress of the closest point along the spline and $n$ represents the lateral deviation from the spline. The resulting $(p,n)$-points determine the dynamic constraints.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-C Projection of static obstacles onto baseline", "weight": 1.0} -->

The map is represented by a raster in which each voxel is labeled as "drivable" or "non-drivable". At uniformly sampled points along the baseline, a ray cast perpendicular to the baseline in both directions finds the nearest non-drivable voxels in the map raster (Fig. 2, right). The resulting $(p,n)$-points determine the static constraints.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Projection of static obstacles onto baseline", "weight": 1.0} -->

Note that a similar procedure could be used for the dynamic obstacles if they were rasterized rather than vectorized.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-D Constraint computation", "weight": 1.0} -->

Tracking references are computed by projecting each waypoint $(x_{k},y_{k})$ onto the baseline to obtain $p_{\text{ref}}(t_{k})$. Longitudinal velocity $v_{\text{ref}}(t)$ and acceleration $a_{\text{ref}}(t)$ references are approximated using finite differences.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-D Constraint computation", "weight": 1.0} -->

Dynamic constraints are determined as follows: Dynamic obstacles farther than a certain threshold (i.e., whose closest point has $n$ greater than the threshold) impose lateral constraints only.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-D Constraint computation", "weight": 1.0} -->

Dynamic obstacles closer than the threshold can impose both lateral and longitudinal constraints, determined separately for each point based on another threshold.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-D Constraint computation", "weight": 1.0} -->

Static constraints are lateral by default, unless $n$ is below a certain threshold, in which case they are longitudinal.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-D Constraint computation", "weight": 1.0} -->

Stay-behind or stay-ahead: Longitudinal constraints can be imposed differently depending on the assumptions about the experimental planner. We consider two regimes: Stay-behind: the initial position of the AV must always fall within the longitudinal bounds. Formally, $p_{\text{lower}}(t)<p_{\text{rear}}<p_{\text{front}}<p_{\text{upper}}(t)\,\,\,\forall t$, where $p_{\text{rear}}(t),p_{\text{front}}(t)$ are the progress values of the rear bumper and the front bumper of the AV at time $t$, respectively. In other words, the AV always stays behind (i.e. yields for) dynamic obstacles predicted to cross its path. This is suitable for planners that output a path (i.e., no timestamps) or that do not take dynamic road actors into consideration.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-D Constraint computation", "weight": 1.0} -->

Stay-ahead: the planned position of the AV must always fall within the longitudinal bounds. Formally, $p_{\text{lower}}(t)<p_{\text{rear}}(t)<p_{\text{front}}(t)<p_{\text{upper}}(t)\,\,\,\forall t$. In this regime, the AV may stay behind or stay ahead of other actors, depending on its predicted relative position along the baseline. This is suitable for planners that output trajectories and take other road actors into consideration.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-E Lateral constraint fitting", "weight": 1.0} -->

The lateral splines are fitted to the samples using quadratic programming, which maximizes the available space within the lateral constraints, subject to $\gamma_{\text{left,hard}}(p_{i})<n_{i}$ and $\gamma_{\text{right,hard}}(p_{i})>n_{i}$ for every laterally constraining sample point $(p_{i},n_{i})$. Regularization penalizes excessive curvature, ensuring smoothness of the resulting splines.

<!-- chunk {"id": "body-0031", "role": "body", "section": "MPC formulation", "weight": 1.0} -->

The dynamical system is defined by the state $\mathbf{x}(t)=[p(t),n(t),\omega(t),v(t),a(t),\beta(t)]$ and the control inputs $\mathbf{u}(t)=[j(t),\Delta\beta(t)]$, where the components are: | $p(t)$ | Progress along the baseline | | $n(t)$ | Lateral error from the baseline | | $\omega(t)$ | Local heading relative to the baseline | | $\beta(t)$ | Steering angle | | $j(t)$ | Jerk (rate of acceleration change) | | $\Delta\beta(t)$ | Change in steering angle | The MPC problem can be formulated as follows: subject to $\mathbf{x}(t+1)=f(\mathbf{x}(t),\mathbf{u}(t))$, $\mathbf{C}(\mathbf{x})\leq\mathbf{0}$,

<!-- chunk {"id": "body-0032", "role": "body", "section": "MPC formulation", "weight": 1.0} -->

$\mathbf{u}_{\text{min}}\leq\mathbf{u}(t)\leq\mathbf{u}_{\text{max}}$, and $\mathbf{x}=\mathbf{x}_{0}$, $\ell(\mathbf{x}(t+k),\mathbf{u}(t+k))$ is the non-linear stage cost function, $\ell_{f}(\mathbf{x}(t+N))$ is the non-linear terminal cost function, $N$ is the prediction horizon, $f(\mathbf{x}(t),\mathbf{u}(t))$ represents the state transition model -- in this case, a kinematic bicycle model, $\mathbf{C}(\mathbf{x})$ represents the non-linear state constraints, $\mathbf{u}_{\text{min}},\mathbf{u}_{\text{max}}$ are the control constraints,

<!-- chunk {"id": "body-0033", "role": "body", "section": "MPC formulation", "weight": 1.0} -->

The non-linear constraint function $\mathbf{C}(\mathbf{x})$ includes terms that ensure the AV remains within the spline constraints throughout the planning horizon. It also includes terms balancing various objectives, such as maintaining comfort, ensuring the AV stays within its operational boundaries, and minimizing perceived risks.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A Experimental motion planners", "weight": 1.0} -->

Urban Driver is a regression-based ML planner which learns to imitate human trajectories from expert demonstrations. We trained an open-source version of Urban Driver on lane follow and ACC scenarios from the nuPlan dataset.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A Experimental motion planners", "weight": 1.0} -->

Proximal policy optimization (PPO) is a reinforcement learning method for training an agent to maximize a reward function based on simulated experience. We trained an open-source PPO implementation on lane follow and ACC scenarios using a custom simulator.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-A Experimental motion planners", "weight": 1.0} -->

Intelligent driver model (IDM) is a classical car-following model which computes longitudinal acceleration in closed form.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-A Experimental motion planners", "weight": 1.0} -->

A\* search is a classical search-based planner which finds an unobstructed path to a goal pose, avoiding stationary vehicles and obstacles. It respects road boundaries but ignores lanes, making it suitable for unstructured environments like casino pick-up/drop-off (PUDO) areas.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A Experimental motion planners", "weight": 1.0} -->

Urban Driver, PPO, and IDM take both static and dynamic obstacles into account and output trajectories, making them suitable for deployment either in the Stay-behind or Stay-ahead configuration. In contrast, A\* ignores dynamic obstacles and outputs a path, instead relying on Lab2Car to stay-behind other road actors.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B Ablations", "weight": 1.0} -->

In addition to Stay-behind and Stay-ahead, we compared several control Lab2Car configurations (Fig. 5): Baseline: Follow the baseline spline, ignoring waypoints and static/dynamic obstacles.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B Ablations", "weight": 1.0} -->

Tracking: Track the waypoints, ignoring static/dynamic obstacles. Only applicable if $\tau$ is a trajectory with timestamps.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-B Ablations", "weight": 1.0} -->

Map: Track the waypoints (if applicable) and avoid static obstacles, ignoring dynamic obstacles.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-C Simulation results", "weight": 1.0} -->

Lab2Car + Urban Driver (lane follow) Lab2Car + PPO (lane follow) Lab2Car + IDM (lane follow) Lab2Car + A* (unstructured) Coll, front collisions. Road, off-road violations. Accel, longitudinal acceleration violations. Dist, total distance travelled. Values averaged across 1602 lane follow scenarios and 413 unstructured PUDO scenarios. TABLE I: Closed-loop simulation results We first evaluated closed-loop performance on 30-s snippets of real-world drive logs generated by Motional AVs in Las Vegas (Tab. I). We used 1602 lane follow/ACC scenarios for Urban Driver, PPO, and IDM, and 413 unstructured PUDO scenarios for A\*. We used the Object Sim simulator from Applied Intuition, which performs realistic high-fidelity physics simulation of the entire AV stack.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-C Simulation results", "weight": 1.0} -->

As expected, more advanced configurations of Lab2Car consistently improved safety across all planners. Stay-ahead improved progress over Stay-behind while maintaining and, in some cases, improving safety. Note that collisions cannot be reduced to zero, since the constraints rely on predictions, which maybe inaccurate.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-C Simulation results", "weight": 1.0} -->

In most cases, improvements in safety came at the expense of progress and comfort. We hypothesized that this is related to contradictory and occasionally unsatisfiable constraints, such as tracking an accelerating trajectory while braking for an obstacle. To investigate this, we evaluated Stay-ahead without the tracking references (Tab. II). This resulted in improved progress with small reductions in safety, suggesting that this trade-off can be navigated by relaxing constraints.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-C Simulation results", "weight": 1.0} -->

Lab2Car + Urban Driver, Stay-ahead Lab2Car + PPO, Stay-ahead Lab2Car + IDM, Stay-ahead TABLE II: Closed-loop simulations with/without tracking

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-D Real-world driving", "weight": 1.0} -->

We deployed Urban Driver and A\* using Lab2Car on Motional IONIQ 5 self-driving cars in Las Vegas. Perception, prediction, and mapping inputs were provided by the corresponding modules of the Motional AV stack. All drive tests were conducted with an experienced safety driver ready to take over in case of unsafe behavior. Representative scenarios are included in the supplementary video.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-D Real-world driving", "weight": 1.0} -->

Lab2Car + Urban Driver (private track) Lab2Car + A* (private track) Lab2Car + A* (public road) Abbreviations as in Tab. I. CPTO, collision-preventative takeover by the safety driver. Values totaled for each configuration. TABLE III: On-road results Lab2Car + Urban Driver on private track: We staged 8 ACC and 9 cut-in scenarios on a private test track (Tab. III, top). As a baseline, we used the Map configuration, which resulted in two safety-related takeovers as the planner failed to stop for the vehicle ahead (Fig. 6, top row). Resimulations (resims) confirmed that the ML trajectory would have indeed resulted in a collision, which the Stay-behind configuration would have prevented (Fig. 6, top right). Accordingly, repeating the scenarios in the Stay-behind configuration resulted in safe stopping behind the lead vehicle (Fig. 6, middle row). Performance was similar using the Stay-ahead configuration (Fig. 6, bottom row). Overall, the planner slowed and/or stopped successfully for 6/8 ACC and 9/9 cut-in scenarios.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-D Real-world driving", "weight": 1.0} -->

While Lab2Car corrected the unsafe behavior of Urban Driver, the planner had comfort issues and repeatedly got stuck outputting stationary trajectories after stopping, for reasons unrelated to Lab2Car. We therefore chose not to deploy Lab2Car + Urban Driver on public roads.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-D Real-world driving", "weight": 1.0} -->

Lab2Car + A\* on private track: We similarly staged 4 overtake, 5 yield-then-overtake, and 9 narrow gap scenarios using the Stay-behind configuration (Tab. III, middle; Fig. 7, top two rows). The planner performed successfully in all scenarios, with the exception of getting stuck in one narrow gap scenario. There were no safety-related takeovers.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-D Real-world driving", "weight": 1.0} -->

Lab2Car + A\* on public roads: After rigorously evaluating Lab2Car + A\* in simulation and on the private test track, we deployed it on the Las Vegas strip. The experimental planner was geofenced to casino PUDO areas -- dense, unstructured environments with pedestrians, slowly moving and parked vehicles, traffic cones, and obstacles. It was deployed as part of a larger planning system that included an additional lane-based planner and a selection mechanism for arbitrating between the two. We only report results for periods when Lab2Car + A\* was driving the AV.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-D Real-world driving", "weight": 1.0} -->

On public roads, Lab2Car + A\* showed performance similar to the private test track (Tab. III, bottom; Fig. 7, bottom two rows). It handled scenarios with multiple lane changes, jaywalking pedestrians, and multiple passing vehicles (see video). There were no safety-related takeovers.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we introduced Lab2Car, an optimization-based method for safely deploying experimental planners in real self-driving cars. We demonstrated the versatility of our approach by using it to deploy a ML-based planner and a classical search-based planner, neither of which could provide safety, comfort, or even kinematic feasibility on its own. Results from large-scale closed-loop simulations showed that Lab2Car can improve safety for a wide range of experimental planners.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We envision two use cases for Lab2Car: as training wheels and as a planning component in its own right. For example, an under-trained Urban Driver can be initially deployed with the Stay-behind configuration. This can provide early signal for on-road issues that would be difficult to detect in simulation, such as issues with comfort or starting from stop. Unsafe behavior masked by Lab2Car can be revealed by examining discrepancies between the trajectory sketch and the final trajectory, as well as by resimulation. As Urban Driver matures, the configuration can be relaxed to Stay-ahead, Map, and finally Tracking, allowing Lab2Car to support the capabilities of a powerful ML planner. Alternatively, Lab2Car can become part of the final planning system. For example, our A\* planner outputs a path and does not take dynamic actors into account, which means it has to be deployed with the Stay-behind configuration.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Lab2Car streamlines the path from incubating an idea in the lab to testing it on the car, offering early insights into the real-world performance of experimental planners at the initial stages of prototyping. This can allow researchers in academia and industry to focus on promising ideas and rule out dead ends before investing too much effort in polishing them. We believe this can dramatically accelerate progress towards resolving the planning bottleneck in autonomous driving and making a driverless future for all a reality.
