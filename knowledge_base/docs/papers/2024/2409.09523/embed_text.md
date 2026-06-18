## Introduction

Self-driving cars have achieved remarkable progress towards human-level autonomous driving. Much of this success is owed to progress in ML-based perception and prediction \[(https://arxiv.org/html/2409.09523v2#bib.bib1), (https://arxiv.org/html/2409.09523v2#bib.bib2), (https://arxiv.org/html/2409.09523v2#bib.bib3), (https://arxiv.org/html/2409.09523v2#bib.bib4), (https://arxiv.org/html/2409.09523v2#bib.bib5), (https://arxiv.org/html/2409.09523v2#bib.bib6), (https://arxiv.org/html/2409.09523v2#bib.bib7)\], which can attain a human-like understanding of the scene around the autonomous vehicle (AV). Classical motion planners relying on handcrafted rules \[(https://arxiv.org/html/2409.09523v2#bib.bib8), (https://arxiv.org/html/2409.09523v2#bib.bib9)\] have similarly given way to ML-based motion planners that learn the rules of driving from data \[(https://arxiv.org/html/2409.09523v2#bib.bib10), (https://arxiv.org/html/2409.09523v2#bib.bib11), (https://arxiv.org/html/2409.09523v2#bib.bib12), (https://arxiv.org/html/2409.09523v2#bib.bib13), (https://arxiv.org/html/2409.09523v2#bib.bib14), (https://arxiv.org/html/2409.09523v2#bib.bib15), (https://arxiv.org/html/2409.09523v2#bib.bib16), (https://arxiv.org/html/2409.09523v2#bib.bib17), (https://arxiv.org/html/2409.09523v2#bib.bib18)\]. ML planning is thought to be more scalable and better positioned to capture the ineffable nuances of human driving behavior than classical planning.

However, deploying ML planners in the real world comes with its own set of challenges, which are often overcome using techniques from classical planning. For one, naïve trajectory regression does not ensure comfort or even basic kinematic feasibility, necessitating post-hoc smoothing \[(https://arxiv.org/html/2409.09523v2#bib.bib19), (https://arxiv.org/html/2409.09523v2#bib.bib20), (https://arxiv.org/html/2409.09523v2#bib.bib21)\] or hand-engineered trajectory generation \[(https://arxiv.org/html/2409.09523v2#bib.bib11), (https://arxiv.org/html/2409.09523v2#bib.bib17)\]. Ensuring safety poses an even greater challenge, as ML solutions tend to fail on edge cases that compose the long tail of the data distribution. Since the opacity of the implicitly learned rules makes it difficult to predict when such failures would occur, it is of paramount importance to institute interpretable guardrails when deploying ML planners in the real world. Previous authors have achieved this by projecting the ML trajectory onto a restricted set of lane-follow trajectories pre-filtered based on hand-engineered rules \[(https://arxiv.org/html/2409.09523v2#bib.bib11), (https://arxiv.org/html/2409.09523v2#bib.bib17)\], an ad-hoc approach which does not scale to complex, unstructured scenarios. Other authors \[(https://arxiv.org/html/2409.09523v2#bib.bib22), (https://arxiv.org/html/2409.09523v2#bib.bib23)\] have proposed applying differentiable model predictive control (MPC) as the final layer of a neural AV stack to simultaneously ensure safety, comfort, and feasibility. However, these approaches were not deployed in the real world and come at the cost of increased complexity and tight coupling between the MPC and the planning module.

In all instances, making ML planners or even naïve classical planners deployable requires substantial engineering investment, which can only be justified if there is strong signal that they will drive well. Such signal could in principle be obtained in simulation; however, there is often a substantial gap between performance in simulation and on the road. As a result, few experimental planners get evaluated in the real world, and those that do are often part of bespoke deployment systems that cannot be readily extended to other planners.

Figure 1: Lab2Car is a plug-and-play wrapper that transforms a rough trajectory sketch into spatiotemporal constraints (a maneuver). The maneuver defines an optimization problem solved by MPC to obtain a final trajectory that is safe, comfortable, and dynamically feasible. This enables rapid deployment and real-world evaluation of planners that lack such properties.

To address this problem, we present Lab2Car, an optimization-based wrapper that takes a rough trajectory sketch and transforms it into a set of interpretable spatiotemporal constraints -- a maneuver -- which is then solved using MPC to obtain a safe, comfortable, and dynamically feasible trajectory (Fig. (https://arxiv.org/html/2409.09523v2#S1.F1 "Figure 1 ‣ I Introduction ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional.")). The initial trajectory sketch captures the high-level behavioral intent, while the final trajectory captures the low-level sequence of commands that the robot must execute. This division of labor mirrors hierarchical motor control in biological brains \[(https://arxiv.org/html/2409.09523v2#bib.bib24)\] and allows for robust and safe deployment of a wide range of experimental planners.

Our contributions are as follows:

A simple yet powerful maneuver extraction algorithm that converts a trajectory sketch -- even a really poor one -- into constraints that preserve the underlying driving intent while ensuring safety.

Integration with multiple ML/classical planners and a state-of-the-art MPC solver as part of a full AV stack.

Evaluation on 2000+ resimulated scenarios from real-world drive logs using a high-fidelity simulator.

Deployment on a real AV and evaluation on the road.

Figure 2: Anatomy of a maneuver (left) and spline-space illustration (right).

Figure 3: Lab2Car in real-world scenario. Gray arrowheads denote initial trajectory sketch from experimental planner. Spatiotemporal constraints denoted as in Fig. 2. Connected dark green circles denote predictions for other agents. Red curve denotes final 8-s open-loop trajectory from MPC.

## Maneuver definition

The input to Lab2Car is a path or trajectory sketch $\tau = {\{{(x_{k},y_{k},t_{k})}\}}_{k = 0}^{K - 1}$ consisting of a sequence of $K$ Cartesian waypoints $(x_{k},y_{k})$ with optional timestamps $t_{k}$. The trajectory is then converted to a maneuver: a set of spatiotemporal constraints (continuous in the spatial domain and discrete in the temporal domain) that define the feasible space of trajectories over the planning horizon (Fig. (https://arxiv.org/html/2409.09523v2#S1.F2 "Figure 2 ‣ I Introduction ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional."), left). Similarly to control barrier functions \[(https://arxiv.org/html/2409.09523v2#bib.bib25), (https://arxiv.org/html/2409.09523v2#bib.bib26), (https://arxiv.org/html/2409.09523v2#bib.bib27)\], the maneuver implicitly defines a safe region, while also optimizing for comfort and similarity to the trajectory sketch.

The baseline trajectory is modeled as a 2D quartic cardinal B-spline \[(https://arxiv.org/html/2409.09523v2#bib.bib28)\] (Fig. (https://arxiv.org/html/2409.09523v2#S1.F2 "Figure 2 ‣ I Introduction ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional.") and Fig. (https://arxiv.org/html/2409.09523v2#S1.F3 "Figure 3 ‣ I Introduction ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional."), blue curve). The spline is defined by a set of $N$ control points and corresponding knot vectors. The knot vectors are placed at spline progress values $p$ from $0$ to $N$, The spline basis functions are valid within the domain spanning from $1.5$ to $N - 2.5$, ensuring that the spline is smooth and well-defined across this range.

This baseline spline serves as the reference axis of a curvilinear coordinate system which defines all subsequent trajectory constraints in terms of longitudinal (along the spline) and lateral (orthogonal to the spline) components.

Tracking references are defined as a time series $({p_{\text{ref}}{(t)}},{v_{\text{ref}}{(t)}},{a_{\text{ref}}{(t)}})$, specifying the progress, longitudinal velocity, and longitudinal acceleration, respectively, that the AV should aim to achieve at each time point $t$ of the discretized planning horizon (Fig. (https://arxiv.org/html/2409.09523v2#S1.F2 "Figure 2 ‣ I Introduction ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional."), blue arrows). These do not apply if $\tau$ is a path (i.e., has no timestamps).

Lateral constraints are formulated as 1D spline functions extending along the baseline spline, representing the driveable space boundaries at each time point $t$ (Fig. (https://arxiv.org/html/2409.09523v2#S1.F2 "Figure 2 ‣ I Introduction ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional.") and Fig. (https://arxiv.org/html/2409.09523v2#S1.F3 "Figure 3 ‣ I Introduction ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional."), green curves). These constraints are segmented into "hard" and "soft" constraints for both the left and right boundaries, indexed by spline progress: ${\gamma_{\text{left,hard}}{(p)}},{\gamma_{\text{left,soft}}{(p)}},{\gamma_{\text{right,hard}}{(p)}},{\gamma_{\text{right,soft}}{(p)}}$. A separate set of constraints is defined for each time point $t$ (omitted).

Longitudinal constraints are defined as a time series $({p_{\text{lower}}{(t)}},{p_{\text{upper}}{(t)}})$ specifying the lower and upper bound on progress, respectively, at each time point $t$ of the planning horizon (Fig. (https://arxiv.org/html/2409.09523v2#S1.F2 "Figure 2 ‣ I Introduction ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional.") and Fig. (https://arxiv.org/html/2409.09523v2#S1.F3 "Figure 3 ‣ I Introduction ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional."), yellow and red lines).

Figure 4: Lab2Car rescuing bad trajectory sketches in synthetic scenarios. Color coding as in Fig. 3

## Maneuver extraction

### III-A Baseline fitting

Fitting the baseline proceeds in two steps.

Step 1: Determining spline progress: Initially, the progress value ${\hat{p}}_{k}$ for each waypoint point along the spline is calculated to reflect the cumulative distance along the path:

Here, $\mathbf{w}_{k} = \begin{bmatrix}
\end{bmatrix}$ are waypoint vectors and $\text{dist}_{\text{max}}$ is the target distance between control points on the spline.

Step 2: Control point optimization: The control points $C$ of the spline are computed using a least squares method by solving:

where $C$ is a $N \times 2$ matrix of control points, $\mathbf{b}$ is the spline basis function, $R$ is a second-order regularization matrix which penalizes excessive curvature, and $c_{reg}$ is the regularization coefficient.

### III-B Projection of dynamic obstacles onto baseline

Detections and predictions for other dynamic road entities, such as vehicles and pedestrians, are represented by time series of convex hulls subsampled to sets of $(x,y)$ points. The sampled points are then transformed into a curvilinear coordinate system aligned with the baseline, referred to as "spline-space" (Fig. (https://arxiv.org/html/2409.09523v2#S1.F2 "Figure 2 ‣ I Introduction ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional."), right). In this coordinate system, each point is expressed as $(p,n)$, where $p$ denotes progress of the closest point along the spline and $n$ represents the lateral deviation from the spline. The resulting $(p,n)$-points determine the dynamic constraints.

### III-C Projection of static obstacles onto baseline

The map is represented by a raster in which each voxel is labeled as "drivable" or "non-drivable". At uniformly sampled points along the baseline, a ray cast perpendicular to the baseline in both directions finds the nearest non-drivable voxels in the map raster (Fig. (https://arxiv.org/html/2409.09523v2#S1.F2 "Figure 2 ‣ I Introduction ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional."), right). The resulting $(p,n)$-points determine the static constraints.

Note that a similar procedure could be used for the dynamic obstacles if they were rasterized rather than vectorized.

### III-D Constraint computation

Tracking references are computed by projecting each waypoint $(x_{k},y_{k})$ onto the baseline to obtain $p_{\text{ref}}{(t_{k})}$. Longitudinal velocity $v_{\text{ref}}{(t)}$ and acceleration $a_{\text{ref}}{(t)}$ references are approximated using finite differences.

Dynamic constraints are determined as follows:

Dynamic obstacles farther than a certain threshold (i.e., whose closest point has $n$ greater than the threshold) impose lateral constraints only.

Dynamic obstacles closer than the threshold can impose both lateral and longitudinal constraints, determined separately for each point based on another threshold.

Static constraints are lateral by default, unless $n$ is below a certain threshold, in which case they are longitudinal.

Stay-behind or stay-ahead: Longitudinal constraints can be imposed differently depending on the assumptions about the experimental planner. We consider two regimes:

Stay-behind: the initial position of the AV must always fall within the longitudinal bounds. Formally, ${p_{\text{lower}}{(t)}} < {p_{\text{rear}}{}} < {p_{\text{front}}{}} < {p_{\text{upper}}{(t)}{\forall t}}$, where ${p_{\text{rear}}{(t)}},{p_{\text{front}}{(t)}}$ are the progress values of the rear bumper and the front bumper of the AV at time $t$, respectively. In other words, the AV always stays behind (i.e. yields for) dynamic obstacles predicted to cross its path. This is suitable for planners that output a path (i.e., no timestamps) or that do not take dynamic road actors into consideration.

Stay-ahead: the planned position of the AV must always fall within the longitudinal bounds. Formally, ${p_{\text{lower}}{(t)}} < {p_{\text{rear}}{(t)}} < {p_{\text{front}}{(t)}} < {p_{\text{upper}}{(t)}{\forall t}}$. In this regime, the AV may stay behind or stay ahead of other actors, depending on its predicted relative position along the baseline. This is suitable for planners that output trajectories and take other road actors into consideration.

### III-E Lateral constraint fitting

The lateral splines are fitted to the samples using quadratic programming \[(https://arxiv.org/html/2409.09523v2#bib.bib29)\], which maximizes the available space within the lateral constraints, subject to ${\gamma_{\text{left,hard}}{(p_{i})}} < n_{i}$ and ${\gamma_{\text{right,hard}}{(p_{i})}} > n_{i}$ for every laterally constraining sample point $(p_{i},n_{i})$. Regularization penalizes excessive curvature, ensuring smoothness of the resulting splines.

## MPC formulation

The dynamical system is defined by the state ${\mathbf{x}{(t)}} = {\lbrack{p{(t)}},{n{(t)}},{\omega{(t)}},{v{(t)}},{a{(t)}},{\beta{(t)}}\rbrack}$ and the control inputs ${\mathbf{u}{(t)}} = {\lbrack{j{(t)}},{\Delta\beta{(t)}}\rbrack}$, where the components are:

The MPC problem can be formulated as follows:

subject to ${\mathbf{x}{({t + 1})}} = {f{({\mathbf{x}{(t)}},{\mathbf{u}{(t)}})}}$, ${\mathbf{C}{(\mathbf{x})}} \leq \mathbf{0}$, $\mathbf{u}_{\text{min}} \leq {\mathbf{u}{(t)}} \leq \mathbf{u}_{\text{max}}$, and ${\mathbf{x}{}} = \mathbf{x}_{0}$,

$\ell{({\mathbf{x}{({t + k})}},{\mathbf{u}{({t + k})}})}$ is the non-linear stage cost function,

$\ell_{f}{({\mathbf{x}{({t + N})}})}$ is the non-linear terminal cost function,

$N$ is the prediction horizon,

$f{({\mathbf{x}{(t)}},{\mathbf{u}{(t)}})}$ represents the state transition model -- in this case, a kinematic bicycle model,

$\mathbf{C}{(\mathbf{x})}$ represents the non-linear state constraints,

$\mathbf{u}_{\text{min}},\mathbf{u}_{\text{max}}$ are the control constraints,

$\mathbf{x}_{0}$ is the initial state.

The non-linear constraint function $\mathbf{C}{(\mathbf{x})}$ includes terms that ensure the AV remains within the spline constraints throughout the planning horizon. It also includes terms balancing various objectives, such as maintaining comfort, ensuring the AV stays within its operational boundaries, and minimizing perceived risks.

Figure 5: Lab2Car configurations (ablations).

Figure 6: Lab2Car + Urban Driver on the road: sequential frames from example scenarios (rows) in different Lab2Car configurations (left) and corresponding open-loop resims (right) at the reference frame (treal = 0 s). Each row is from a unique scenario run. Resims performed with factual (bold) configuration (i.e., the one used on the road) and one counterfactual configuration. In left (on-road) panels, open-loop trajectory denoted in pink. In right (resim) panels, color coding as in Fig. 3. Resim, resimulation. See supplementary video for corresponding clips.

## Experiments

### V-A Experimental motion planners

Urban Driver is a regression-based ML planner which learns to imitate human trajectories from expert demonstrations. We trained an open-source version of Urban Driver \[(https://arxiv.org/html/2409.09523v2#bib.bib30), (https://arxiv.org/html/2409.09523v2#bib.bib31)\] on lane follow and ACC scenarios from the nuPlan dataset \[(https://arxiv.org/html/2409.09523v2#bib.bib31)\].

Proximal policy optimization (PPO) is a reinforcement learning method for training an agent to maximize a reward function based on simulated experience. We trained an open-source PPO implementation \[(https://arxiv.org/html/2409.09523v2#bib.bib32)\] on lane follow and ACC scenarios using a custom simulator.

Intelligent driver model (IDM) is a classical car-following model which computes longitudinal acceleration in closed form \[(https://arxiv.org/html/2409.09523v2#bib.bib33)\].

A\* search is a classical search-based planner \[(https://arxiv.org/html/2409.09523v2#bib.bib34), (https://arxiv.org/html/2409.09523v2#bib.bib8)\] which finds an unobstructed path to a goal pose, avoiding stationary vehicles and obstacles. It respects road boundaries but ignores lanes, making it suitable for unstructured environments like casino pick-up/drop-off (PUDO) areas.

Urban Driver, PPO, and IDM take both static and dynamic obstacles into account and output trajectories, making them suitable for deployment either in the Stay-behind or Stay-ahead configuration. In contrast, A\* ignores dynamic obstacles and outputs a path, instead relying on Lab2Car to stay-behind other road actors.

### V-B Ablations

In addition to Stay-behind and Stay-ahead, we compared several control Lab2Car configurations (Fig. (https://arxiv.org/html/2409.09523v2#S4.F5 "Figure 5 ‣ IV MPC formulation ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional.")):

Baseline: Follow the baseline spline, ignoring waypoints and static/dynamic obstacles.

Tracking: Track the waypoints, ignoring static/dynamic obstacles. Only applicable if $\tau$ is a trajectory with timestamps.

Map: Track the waypoints (if applicable) and avoid static obstacles, ignoring dynamic obstacles.

### V-C Simulation results

Lab2Car + Urban Driver (lane follow)

Lab2Car + PPO (lane follow)

Lab2Car + IDM (lane follow)

Lab2Car + A* (unstructured)

Coll, front collisions. Road, off-road violations. Accel, longitudinal acceleration violations. Dist, total distance travelled. Values averaged across 1602 lane follow scenarios and 413 unstructured PUDO scenarios.
TABLE I: Closed-loop simulation results

We first evaluated closed-loop performance on 30-s snippets of real-world drive logs generated by Motional AVs in Las Vegas (Tab. [I](https://arxiv.org/html/2409.09523v2#S5.T1 "TABLE I ‣ V-C Simulation results ‣ V Experiments ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional.")). We used 1602 lane follow/ACC scenarios for Urban Driver, PPO, and IDM, and 413 unstructured PUDO scenarios for A\*. We used the Object Sim simulator from Applied Intuition \[(https://arxiv.org/html/2409.09523v2#bib.bib35)\], which performs realistic high-fidelity physics simulation of the entire AV stack.

As expected, more advanced configurations of Lab2Car consistently improved safety across all planners. Stay-ahead improved progress over Stay-behind while maintaining and, in some cases, improving safety. Note that collisions cannot be reduced to zero, since the constraints rely on predictions, which maybe inaccurate.

In most cases, improvements in safety came at the expense of progress and comfort. We hypothesized that this is related to contradictory and occasionally unsatisfiable constraints, such as tracking an accelerating trajectory while braking for an obstacle. To investigate this, we evaluated Stay-ahead without the tracking references (Tab. [II](https://arxiv.org/html/2409.09523v2#S5.T2 "TABLE II ‣ V-C Simulation results ‣ V Experiments ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional.")). This resulted in improved progress with small reductions in safety, suggesting that this trade-off can be navigated by relaxing constraints.

Lab2Car + Urban Driver, Stay-ahead

Lab2Car + PPO, Stay-ahead

Lab2Car + IDM, Stay-ahead

TABLE II: Closed-loop simulations with/without tracking

### V-D Real-world driving

Figure 7: Lab2Car + A* on the road: private track (top two rows) and public road (bottom two rows). Notation as in Fig. 6.

We deployed Urban Driver and A\* using Lab2Car on Motional IONIQ 5 self-driving cars in Las Vegas. Perception, prediction \[(https://arxiv.org/html/2409.09523v2#bib.bib36)\], and mapping inputs were provided by the corresponding modules of the Motional AV stack. All drive tests were conducted with an experienced safety driver ready to take over in case of unsafe behavior. Representative scenarios are included in the supplementary video.

Lab2Car + Urban Driver (private track)

Lab2Car + A* (private track)

Lab2Car + A* (public road)

Abbreviations as in Tab. I. CPTO, collision-preventative takeover by the safety driver. Values totaled for each configuration.
TABLE III: On-road results

Lab2Car + Urban Driver on private track: We staged 8 ACC and 9 cut-in scenarios on a private test track (Tab. [III](https://arxiv.org/html/2409.09523v2#S5.T3 "TABLE III ‣ V-D Real-world driving ‣ V Experiments ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional."), top). As a baseline, we used the Map configuration, which resulted in two safety-related takeovers as the planner failed to stop for the vehicle ahead (Fig. (https://arxiv.org/html/2409.09523v2#S4.F6 "Figure 6 ‣ IV MPC formulation ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional."), top row). Resimulations (resims) confirmed that the ML trajectory would have indeed resulted in a collision, which the Stay-behind configuration would have prevented (Fig. (https://arxiv.org/html/2409.09523v2#S4.F6 "Figure 6 ‣ IV MPC formulation ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional."), top right). Accordingly, repeating the scenarios in the Stay-behind configuration resulted in safe stopping behind the lead vehicle (Fig. (https://arxiv.org/html/2409.09523v2#S4.F6 "Figure 6 ‣ IV MPC formulation ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional."), middle row). Performance was similar using the Stay-ahead configuration (Fig. (https://arxiv.org/html/2409.09523v2#S4.F6 "Figure 6 ‣ IV MPC formulation ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional."), bottom row). Overall, the planner slowed and/or stopped successfully for 6/8 ACC and 9/9 cut-in scenarios.

While Lab2Car corrected the unsafe behavior of Urban Driver, the planner had comfort issues and repeatedly got stuck outputting stationary trajectories after stopping, for reasons unrelated to Lab2Car. We therefore chose not to deploy Lab2Car + Urban Driver on public roads.

Lab2Car + A\* on private track: We similarly staged 4 overtake, 5 yield-then-overtake, and 9 narrow gap scenarios using the Stay-behind configuration (Tab. [III](https://arxiv.org/html/2409.09523v2#S5.T3 "TABLE III ‣ V-D Real-world driving ‣ V Experiments ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional."), middle; Fig. (https://arxiv.org/html/2409.09523v2#S5.F7 "Figure 7 ‣ V-D Real-world driving ‣ V Experiments ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional."), top two rows). The planner performed successfully in all scenarios, with the exception of getting stuck in one narrow gap scenario. There were no safety-related takeovers.

Lab2Car + A\* on public roads: After rigorously evaluating Lab2Car + A\* in simulation and on the private test track, we deployed it on the Las Vegas strip. The experimental planner was geofenced to casino PUDO areas -- dense, unstructured environments with pedestrians, slowly moving and parked vehicles, traffic cones, and obstacles. It was deployed as part of a larger planning system that included an additional lane-based planner and a selection mechanism for arbitrating between the two. We only report results for periods when Lab2Car + A\* was driving the AV.

On public roads, Lab2Car + A\* showed performance similar to the private test track (Tab. [III](https://arxiv.org/html/2409.09523v2#S5.T3 "TABLE III ‣ V-D Real-world driving ‣ V Experiments ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional."), bottom; Fig. (https://arxiv.org/html/2409.09523v2#S5.F7 "Figure 7 ‣ V-D Real-world driving ‣ V Experiments ‣ Lab2Car: A Versatile Wrapper for Deploying Experimental Planners in Complex Real-world Environments † – work done while at Motional."), bottom two rows). It handled scenarios with multiple lane changes, jaywalking pedestrians, and multiple passing vehicles (see video). There were no safety-related takeovers.

## Conclusion

In this work, we introduced Lab2Car, an optimization-based method for safely deploying experimental planners in real self-driving cars. We demonstrated the versatility of our approach by using it to deploy a ML-based planner and a classical search-based planner, neither of which could provide safety, comfort, or even kinematic feasibility on its own. Results from large-scale closed-loop simulations showed that Lab2Car can improve safety for a wide range of experimental planners.

We envision two use cases for Lab2Car: as training wheels and as a planning component in its own right. For example, an under-trained Urban Driver can be initially deployed with the Stay-behind configuration. This can provide early signal for on-road issues that would be difficult to detect in simulation, such as issues with comfort or starting from stop. Unsafe behavior masked by Lab2Car can be revealed by examining discrepancies between the trajectory sketch and the final trajectory, as well as by resimulation. As Urban Driver matures, the configuration can be relaxed to Stay-ahead, Map, and finally Tracking, allowing Lab2Car to support the capabilities of a powerful ML planner. Alternatively, Lab2Car can become part of the final planning system. For example, our A\* planner outputs a path and does not take dynamic actors into account, which means it has to be deployed with the Stay-behind configuration.

Lab2Car streamlines the path from incubating an idea in the lab to testing it on the car, offering early insights into the real-world performance of experimental planners at the initial stages of prototyping. This can allow researchers in academia and industry to focus on promising ideas and rule out dead ends before investing too much effort in polishing them. We believe this can dramatically accelerate progress towards resolving the planning bottleneck in autonomous driving and making a driverless future for all a reality.
