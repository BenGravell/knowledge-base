<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Becoming a Fruit Ninja: Real-Time Probabilistic Kinodynamic Planning for Manipulator Projectile Interception

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Projectile interception is a challenging dynamic manipulation problem. Intercepting a thrown object with a robot arm requires reaching a point on the object's path as the object passes through it. Slicing also fixes the blade's velocity and orientation at contact. The goal is therefore a subset of the states of the robot and arrival times that moves as the object falls, and the arm must reach it within its actuator limits in milliseconds. We present FRUITNINJA, an anytime sampling-based planner that grows a tree on the GPU in batches toward the interception manifold. Each edge is an exact cubic whose travel time is found by a parallel search against the arm's dynamics, so every edge satisfies the actuator limits. Plans are ranked by a risk-aware objective over the uncertainty in the object's position and the arm's arrival time. We evaluate on a Franka Research 3 against six baselines in a calibrated real-time simulator, where FRUITNINJA cuts 96.7% of tosses in the open and 68.3% among five obstacles, versus the best baseline's 68.3% and 35.0% respectively.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Catching a thrown object is a long-standing benchmark for dynamic manipulation, and striking one, as in table tennis, adds a terminal velocity to the goal. We consider slicing, which adds the blade's velocity and orientation at contact. These problems couple the goal to the plan: the arm must reach the object where it will be, so the intercept point depends on the arrival time, which depends on the trajectory. The goal is therefore a manifold of configurations, joint velocities, and arrival times. On an arm such as the Franka Research 3 (FR3), the plan must also respect torque, power, and position-dependent velocity limits, since exceeding any one can damage the hardware. The object is only within the robots reach for under a second and its predicted position is uncertain, so the planner has milliseconds to react and generate a trajectory.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent planners intercept a projectile with an industrial arm, but start from a fixed configuration and reach a pose with zero terminal velocity. Sampling-based motion planners (SBMPs) can solve the full problem, since kinodynamic variants handle general goal regions and differential constraints, but interception imposes hard real-time constraints. Two compatible advances bring SBMPs to millisecond speeds, enough for full planning inside the interception loop: GPU-parallel SBMPs batch tree growth into single kernels, and FLASK steers exactly between arm states with closed-form cubic edges.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present FRUITNINJA, an anytime batched kinodynamic sampling-based motion planner for real-time interception of airborne objects. At $50\text{\,}\mathrm{Hz}$, it samples batches of candidate states, both uniformly and from an explicit nine-dimensional chart of the goal manifold over arrival time, contact point, blade orientation, and speed, and connects each to its nearest tree nodes by a minimum-time cubic. Each edge is timed by a parallel search against a dynamics model of the FR3, and edges that violate its limits are discarded. An anytime outer loop keeps the incumbent plan and prunes nodes that cannot reach the object in time, and a $1\text{\,}\mathrm{kHz}$ controller refits a cubic to the planner's rendezvous every cycle. Since the arrival point is an estimate, plans are ranked by a risk-aware objective that trades cut speed against the probability of contact under uncertainty that grows with the arrival time. We evaluate on hardware and in a simulator calibrated on the physical arm, against six baselines.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

FRUITNINJA cuts $96.7\text{\,}\mathrm{\%}$ of tosses in the open and $68.3\text{\,}\mathrm{\%}$ among five obstacles, against $68.3\text{\,}\mathrm{\%}$ and $35.0\text{\,}\mathrm{\%}$ for the best baseline, and ablations show that the cubic edge and the dynamics model are both necessary.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Let $x:\mathbb{R}_{\geq 0}\to\mathbb{R}^{3}$ be the object's flight, estimated online from its initial position $x_{0}$ and velocity $v_{0}$ under the ballistic model The object is within the arm's reach for $t\in[t_{\mathrm{enter}},t_{\mathrm{fall}}]$, a window of under a second.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The arm has configuration $q\in\mathcal{C}\subset\mathbb{R}^{7}$ and state $(q,\dot{q})$, $\dot{q}\in\mathbb{R}^{7}$. A trajectory $\sigma:[0,T]\to\mathcal{C}$ over travel time $T$ requires joint torques $\tau(t)$ given by the arm's inverse dynamics (Sec. IV-C). The FR3 bounds each joint's position, velocity, and torque and the total mechanical power, $W$, where the velocity bound $\bar{\dot{q}}_{i}(q_{i})$ tapers with position.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Method", "weight": 1.0} -->

We present FRUITNINJA (Free-terminal-time Rendezvous, Uncertainty-aware Interception Tree, aNytime, INcumbent-pruned, JAX-Accelerated), a sampling-based planner that solves Def. III.3. ‣ III Problem Statement ‣ Becoming a Fruit Ninja: Real-Time Probabilistic Kinodynamic Planning for Manipulator Projectile Interception") from the measured state at $50\text{\,}\mathrm{Hz}$. Each batch samples the goal manifold through an explicit chart and free states near the chord to it, connects every sample to its nearest tree nodes by a minimum-time cubic, and keeps the edges that satisfy the arm's actuator limits and clearance. Samples on the manifold are scored by a risk-aware objective over the uncertainty in the object's flight. An anytime outer loop keeps the best rendezvous found so far, prunes nodes that cannot reach the object before it, and sends the first edge of that plan to the controller when the cycle's time-limit is exceeded. We describe the chart, the objective, the dynamics model, the cubic edge, the planner, and the controller in turn.

<!-- chunk {"id": "body-0010", "role": "body", "section": "IV-A The goal chart", "weight": 1.0} -->

Def. III.2. ‣ III Problem Statement ‣ Becoming a Fruit Ninja: Real-Time Probabilistic Kinodynamic Planning for Manipulator Projectile Interception") defines $\mathcal{M}$ implicitly. Given the flight $x(\cdot)$, however, a rendezvous is fixed by a small number of choices, so $\mathcal{M}$ has an explicit chart and can be sampled directly.

<!-- chunk {"id": "body-0011", "role": "body", "section": "IV-B Objective", "weight": 1.0} -->

| The first term rewards the relative speed at contact, clipped at $v_{\mathrm{target}}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "IV-B Objective", "weight": 1.0} -->

$P_{\mathrm{object}}$ is the probability that the object lies within the catch radius $r$ of $x(T)$, and $P_{\mathrm{inrange}}$, with $\Phi$ the standard normal cumulative distribution function, is the probability that the object has not yet left reach. $P_{\mathrm{arm}}$ penalizes a peak joint-velocity fraction $\nu$ above the reflex threshold $\nu_{0}$, in proportion to the time spent above it. Because $\sigma(T)$ grows with the arrival time, the score trades cut speed against arriving before the estimate's uncertainty grows.

<!-- chunk {"id": "body-0013", "role": "body", "section": "IV-C Dynamics model", "weight": 1.0} -->

Both the planner's feasibility check and the $1\text{\,}\mathrm{kHz}$ controller require the joint torque needed to follow a given trajectory. For a state $(q,\dot{q},\ddot{q})$ along an edge, the required torque at joint $i$ is where $M(q)\ddot{q}+c(q,\dot{q})+g(q)$ is the rigid-body inverse dynamics (recursive Newton--Euler, RNEA), $I_{m,i}$ is the reflected rotor inertia of joint $i$, and $\tau_{f,i}(\dot{q}_{i})$ is a friction model. We adopt the identification of, who fit both terms on the Panda arm, the FR3's mechanical predecessor.

<!-- chunk {"id": "body-0014", "role": "body", "section": "IV-C Dynamics model", "weight": 1.0} -->

The reflected rotor inertia $I_{m,i}=J_{m,i}\cdot n_{i}^{2}$ (motor inertia times squared gear ratio) is the torque needed to accelerate the rotor itself. RNEA models only the link-side bodies, and omitting this term under-predicts the torque required for fast motions by up to $12\text{\,}\mathrm{\%}$ of peak torque on the proximal joints. The friction model is a per-joint sigmoid, where $\psi_{1,i}$ sets the saturation amplitude, $\psi_{2,i}$ the transition sharpness, and $\psi_{3,i}$ a velocity offset, and the second term enforces $\tau_{f,i}=0$. We choose the same values for these constants as those provided by Gaz et al. The FR3 firmware adds friction compensation to commanded torques, and its safety reflexes are checked against the arm's internal torque estimates, so the friction model is needed to predict and avoid reflex triggers.

<!-- chunk {"id": "body-0015", "role": "body", "section": "IV-D Cubic edges and minimum-time search", "weight": 1.0} -->

FLASK plans in the flat output space of a differentially flat system, where the boundary value problem has a closed-form solution. A fully actuated arm is flat in its joint positions, $y=q$, and with joint acceleration as the pseudo-control, the minimum-time, minimum-effort trajectory between two boundary states is a per-joint cubic. We refer the reader to the original paper for details on the construction of the cubic.

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-E The FRUITNINJA planner", "weight": 1.0} -->

FRUITNINJA (Alg. 1) grows a tree of cubic edges (Def. IV.2. ‣ IV-D Cubic edges and minimum-time search ‣ IV Method ‣ Becoming a Fruit Ninja: Real-Time Probabilistic Kinodynamic Planning for Manipulator Projectile Interception")) from the measured state. The tree is expanded in batches on the GPU and stored in a preallocated struct-of-arrays layout. An anytime outer loop repeats the expansion and keeps the rendezvous node with the highest score $J$ of. The tree $\mathcal{T}$ is a set of nodes $n=(q_{n},\dot{q}_{n},t_{n})$, each joined to its parent by a feasible cubic edge, where $t_{n}$ is the time-to-come along the edges from the root $(q_{0},\dot{q}_{0},0)$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-E The FRUITNINJA planner", "weight": 1.0} -->

*Collision checking.* The arm's collision geometry is a set of spheres covering each link. Self-collision pairs that the joint limits make unreachable are removed offline. An edge is checked by a discrete set of configurations along its cubic and computing the minimum clearance between the arm spheres and the obstacle capsules at each sample. An edge whose minimum clearance is below a safety margin is rejected. Because the check is per edge, a goal whose direct cubic is in collision can still be reached through an intermediate node, which a single-cubic planner cannot do. During the search, clearance is checked at a coarse resolution, and the plan sent to the controller is rechecked at full resolution, since checking every candidate edge at full resolution would be the largest cost in the cycle.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-E The FRUITNINJA planner", "weight": 1.0} -->

*Batched expansion.* Each round samples $B$ candidate states. A fraction $p_{\mathrm{goal}}$ of them are goal candidates: parameters drawn from a density $p_{\theta}$ over the chart and decoded by $\phi$ (Alg. 1). Each goal candidate has a required arrival time $T_{\mathrm{req}}$, set by its $z_{0}$. These samples bias growth toward the reachable part of $\mathcal{M}$. The density $p_{\theta}$ is a Gaussian mixture over $\mathcal{Z}$ mixed with a uniform component. It is refit between anytime iterations to the parameters that produced the best plans, and it persists across planning cycles. The mixture concentrates samples near previously found rendezvous; the uniform component keeps every point of the chart reachable. The remaining candidates are free states (Alg. 1). The configuration of a free state is a Gaussian perturbation of a point on the chord in joint space from the root to a decoded goal, again mixed with a uniform component over the joint box.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-E The FRUITNINJA planner", "weight": 1.0} -->

Its velocity is drawn from a fraction of the joint-velocity limits at that configuration.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-E The FRUITNINJA planner", "weight": 1.0} -->

Each candidate has $M$ parent candidates: the root and its $M-1$ nearest tree nodes (Alg. 1), found by a brute-force parallel scan. The root is always included because it could potentially find cheaper and smoother paths in early iterations, in comparison to connecting with the nearest neighbor set, which produces segmented paths that are jerky and require more iterations to smooth out.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-E The FRUITNINJA planner", "weight": 1.0} -->

A goal candidate must arrive at $T_{\mathrm{req}}$, so its edge duration from parent $p$ is fixed at $T_{\mathrm{req}}-t_{p}$ and the check is evaluated once (Alg. 1). A free candidate has no required arrival time, but is still bounded by $T_{\mathrm{best}}$. To efficiently compute an admissible bound for this time, we rely on one iteration of an $N$-ary search. Edges that fail the check of Def. IV.3. ‣ IV-D Cubic edges and minimum-time search ‣ IV Method ‣ Becoming a Fruit Ninja: Real-Time Probabilistic Kinodynamic Planning for Manipulator Projectile Interception") or the clearance check are discarded (Alg. 1). Each candidate is attached to the remaining parent that gives it the smallest time-to-come (Alg. 1). Multiple parents are needed for detours: if the edge from the nearest node is in collision, the edge from another parent may be clear.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-E The FRUITNINJA planner", "weight": 1.0} -->

*Anytime outer loop.* After every round, the incumbent is set to the highest-scoring rendezvous node in the tree (Alg. 1). At the end of each anytime iteration, the tree is pruned (Alg. 1). Informed pruning needs a cost-to-go bound, which has no closed form here. We instead prune on arrival time. Let $\sigma^{\star}=\argmax_{c}J(c)$ over the rendezvous nodes of $\mathcal{T}$ and $t_{\mathrm{best}}=t_{\sigma^{\star}}$. For a node $n$ with blade position $p_{n}$, let be the earliest time at which the blade can reach the object from $n$, where $V_{\mathrm{tip}}$ bounds the end-effector speed. The node is pruned if $T_{n}$ does not exist or $T_{n}>t_{\mathrm{best}}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-E The FRUITNINJA planner", "weight": 1.0} -->

Input: root (q0, q̇0); flight x(⋅); batch B; parents M; rounds R; anytime iterations A Output: rendezvous (qg, q̇g, T) for the 1 kHz controller Xfree← ChordSample(q0, Xgoal, (1 − pgoal)B) foreach x ∈ Xgoal ∪ Xfree in parallel do okp ← okp∧ Clear(p, x, Tp) $p^{\star}\leftarrow\argmin_{p\,:\,\mathrm{ok}_{p}}t(p)+T_{p}$ $\sigma^{\star}\leftarrow\argmax_{c\,\in\,\mathcal{T}\cap\mathcal{M}}J(c)$ return first segment of σ⋆ Algorithm 1 FRUITNINJA: one planning cycle

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-F Controller and execution architecture", "weight": 1.0} -->

The system operates at two rates (Fig. 1). An incumbent plan is a path of one or more cubic edges, the planner only uses the endpoint of the first, which is sent to the $1\text{\,}\mathrm{kHz}$ tracking controller $(q_{g},\dot{q}_{g},T)$, and the tree is rebuilt at the next planning cycle. Each control cycle, the controller fits its own cubic from the measured state $(q,\dot{q})$ to the rendezvous over horizon $T$, extracts the desired acceleration where $[\ell,u]$ taper the velocity toward zero near the joint limits, and applies the dynamics model to obtain a torque command $\tau\in\mathbb{R}^{7}$, clipped to the FR3's torque, slew, and power limits. Because the refit starts from the measured state every cycle, the controller needs only the current rendezvous and no knowledge of the tree. The controller runs at $1\text{\,}\mathrm{kHz}$ in step with the FR3's required control rate.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-F Controller and execution architecture", "weight": 1.0} -->

The planner runs at $50\text{\,}\mathrm{Hz}$ on a separate thread. Unlike the controller, this requires compensation for its own latency: a plan produced at time $t$ targets the predicted object state at $t+\Delta t_{\text{plan}}$, where $\Delta t_{\text{plan}}\approx$20\text{\,}\mathrm{ms}$$ is the measured planning time. Without this compensation, the trajectory no longer intersects the object and the success rate drops to nearly $0\text{\,}\mathrm{\%}$. Our GPU-based algorithm makes use of a unified kernel with static memory requirements, producing a highly predictable runtime with only $\pm$1\text{\,}\mathrm{ms}$$ of range.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate FRUITNINJA against six baselines in simulation, in a clear workspace and under clutter, ablate its design choices, and validate on hardware. All simulated experiments run on an NVIDIA RTX 4090 GPU with an AMD Threadripper CPU. FRUITNINJA is implemented in JAX.

<!-- chunk {"id": "body-0027", "role": "body", "section": "V-A Methodology", "weight": 1.0} -->

The simulator runs the same planner, controller, and communication stack as the physical system, as separate processes over UDP; only the physics and perception are simulated. Every noise source is fitted from hardware recordings. The simulator synthesises raw marker detections and feeds them through the estimator that runs on hardware, applies a correlated disturbance torque to the arm calibrated so that tracking divergence matches hardware replay to within $8\text{\,}\mathrm{\%}$. The arm uses a torque and safety model fitted from $300$ total real swings.

<!-- chunk {"id": "body-0028", "role": "body", "section": "V-A Methodology", "weight": 1.0} -->

Each evaluation is $180$ tosses across three seeds. Tosses are ballistic arcs that sweep laterally across the arm's reachable workspace with transit times of $0.750.95\text{\,}\mathrm{s}$, drawn from three launch azimuths and two launch radii.

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-A Methodology", "weight": 1.0} -->

We report *cut rate*, the percentage of tosses where the blade contacts the object with alignment and speed above the thresholds of Def. III.2. ‣ III Problem Statement ‣ Becoming a Fruit Ninja: Real-Time Probabilistic Kinodynamic Planning for Manipulator Projectile Interception"); *catch rate*, where the blade contacts the object at all; *cut speed* $\bar{v}$, the mean relative normal blade--object speed at contact; and, under clutter, *thru*, the fraction of plans whose executed motion passes through an obstacle. Cut rate is the primary metric; the gap to catch rate separates tosses that miss the object from those that reach it without cutting.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-A Methodology", "weight": 1.0} -->

The baselines are *CEM* and *CMA-ES*, which sample and refine collocations points and intercept configurations in the rendezvous space; *TrajOpt*, sequential convex optimization over a collocated trajectory; *MPPI*, which samples control sequences and takes their exponentially weighted mean; *cuRobo*, a GPU planner over B-spline trajectories; and *RRTC*, a CPU bidirectional RRT with the same cubic steering as FRUITNINJA, which separates the effect of the tree from that of the GPU. Every baseline output is converted to the controller's native format $(T,q_{g},\dot{q}_{g})$, a single cubic to the rendezvous.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-B Interception in the open", "weight": 1.0} -->

Fig. 2 plots cut rate against median solve time for every configuration of every planner. FRUITNINJA cuts $96.7\text{\,}\mathrm{\%}$ of tosses at a median solve time of $12\text{\,}\mathrm{ms}$, inside the $20\text{\,}\mathrm{ms}$ planning cycle. No single-cubic baseline exceeds $70\text{\,}\mathrm{\%}$ at any solve time ($N=0$ in Table I).

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-B Interception in the open", "weight": 1.0} -->

RRTC catches as many tosses as FRUITNINJA ($98.3\text{\,}\mathrm{\%}$) but cuts only $73.3\text{\,}\mathrm{\%}$, at $4.76\text{\,}\mathrm{m}\text{/}\mathrm{s}$ against $5.35\text{\,}\mathrm{m}\text{/}\mathrm{s}$: the CPU tree lacks the time budget to give a solution on every solve, leaving the controller executing stale rendezvous. CEM misses the object on a quarter of tosses, indicating that naive search over the collocation and intercept space is too slow for realtime use.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-C Clutter", "weight": 1.0} -->

Table I adds three and five $750\text{\,}\mathrm{mm}$ capsule obstacles to the workspace, shown in Fig. 3, with every planner at its best open-workspace configuration and any obstacle-aware option enabled. FRUITNINJA falls from $96.7\text{\,}\mathrm{\%}$ to $81.7\text{\,}\mathrm{\%}$ and $68.3\text{\,}\mathrm{\%}$; the best baseline, CMA-ES, falls from $68.3\text{\,}\mathrm{\%}$ to $65.0\text{\,}\mathrm{\%}$ and $35.0\text{\,}\mathrm{\%}$. The obstacles illustrate the power of search, so direct optimization methods become stuck once the direct path is blocked, whereas FRUITNINJA routes through intermediate waypoints and checks each edge for collision (Sec. IV-E).

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-C Clutter", "weight": 1.0} -->

RRTC also builds an obstacle avoiding tree but falls to $21.7\text{\,}\mathrm{\%}$ at five capsules, because it often fails to find a solution within the time budget. MPPI never plans ahead to a rendezvous and cuts nothing; cuRobo is too slow to finish a run even at its fastest setting. Contact with a capsule is not eliminated: thru scores the executed motion, and tracking error under the disturbance torque carries FRUITNINJA through a capsule on $7.3\text{\,}\mathrm{\%}$ and $11.5\text{\,}\mathrm{\%}$ of plans, against $24.1\text{\,}\mathrm{\%}$ and $27.0\text{\,}\mathrm{\%}$ for RRTC.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-D Ablations", "weight": 1.0} -->

We ablate the trajectory parameterization, the probability model, and the arm dynamics model.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-D Ablations", "weight": 1.0} -->

*Trajectory parameterization.* In our approach, each edge is a per-joint cubic, the lowest-order polynomial fixed by the four boundary conditions $(q_{0},\dot{q}_{0},q_{1},\dot{q}_{1})$. However, alternative polynomial orders exist; lower orders lack the expressiveness to represent all boundary conditions and higher orders introduce more expressivity but also additional degrees of freedom. In this section we explore the performance of alternate parameterizations. In Table II, orders 4 and 5 match the cubic within a standard deviation. Dropping the terminal velocity $\dot{q}_{1}$ is worst, at $41.7\text{\,}\mathrm{\%}$, as the planner can no longer command a cut speed at the rendezvous. order 5 (min $\dddot{q}$) Table II: Trajectory parameterization. Each variant is three seeds × 60 throws.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-D Ablations", "weight": 1.0} -->

*Scoring model.* Arm and environment state become hard to predict over long horizons. While our model takes this into account, the removal of these terms still leave a valid planner. In Table III we investigate the performance after removing terms from the objective. $\log P_{\mathrm{inrange}}$ dominates: without it the cut rate falls to $28.3\text{\,}\mathrm{\%}$, as the planner picks rendezvous the object has already passed. Removing $\log P_{\mathrm{arm}}$ costs speed rather than contact, with $\bar{v}$ falling from $5.45\text{\,}$ to $4.38\text{\,}\mathrm{m}\text{/}\mathrm{s}$ at unchanged catch rate, indicating that the planner commits to swings that trigger the arm's reflexes. full objective (control) Table III: Probability model ablation. Each row removes one or two terms from the objective; the pairwise rows remove both named terms. “Flat covariance” freezes σ(t) at its initial value. Mean ± std. dev.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-D Ablations", "weight": 1.0} -->

*Arm dynamics model.* Table IV removes components of the dynamics model. Dropping any single constraint other than the velocity limit has little effect beyond the spread, while keeping only friction and armature drops the cut rate to $61.1\text{\,}\mathrm{\%}$. leave one out Table IV: Arm dynamics model ablation (three seeds × 60 throws per variant). Velocity removes the joint-velocity ratio and position-dependent taper; friction and armature are Eq. 4.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-E Real-world Hardware", "weight": 1.0} -->

We ran FRUITNINJA in the real-world with the same planner, controller, and communication stack used in simulation, and with the estimator calibrated to the hardware residuals of Sec. IV-B. 30 baseball-sized objects were hand-tossed into the workspace of the arm. Over the 30 tosses, FRUITNINJA executed a successful cut on 26 (86.7$\mathrm{\%}$) and executed a successful catch on 26 (86.7$\mathrm{\%}$). Of these, 25 successful cuts were performed consecutively. The majority of failures in the real world were due to perception errors, where thrown balls are not reliably detected by the OptiTrack system, and human error, where tosses are not as consistent as compared to simulation.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-E Real-world Hardware", "weight": 1.0} -->

Additionally, we recorded the tossed objects in this trial and played them back in simulation, measuring the baseline planners' performance under the same distribution of tosses. These results, including those for the fully real experiments, are presented in Table V. Small performance differences arise compared to the fully simulated trials (Table I) because the hand-tossed objects explored a smaller portion of the arm workspace and intensified behaviors specific to those regions.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have presented FRUITNINJA, an anytime batched planner that intercepts a thrown object by growing a tree of exact cubic edges on the GPU toward an explicit chart of the interception manifold. Each edge is timed against the arm's torque, power, and velocity limits, and plans are ranked by the probability of contact under uncertainty. In a simulator calibrated on the physical arm, FRUITNINJA cuts $96.7\text{\,}\mathrm{\%}$ of tosses in the open and $68.3\text{\,}\mathrm{\%}$ among five obstacles, against $68.3\text{\,}\mathrm{\%}$ and $35.0\text{\,}\mathrm{\%}$ for the best single-cubic baseline; ablations show the cubic edge, the objective's arrival-time term, and the dynamics model are each necessary.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The main limitations are the ballistic flight model, which omits drag and object deformation, the arrival-time pruning rule, which is a heuristic rather than an admissible bound and so can discard a higher-scoring rendezvous, and the simple uncertainty models used for arm's own kinematics and dynamics. Additionally, checks and the chart decoder are smooth and differentiable in the trajectory parameters, and we believe gradient-based refinement of tree nodes is a direct next step.
