<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Comfort by Construction: Adaptive, Comfort-Bounded Action Spaces for Learned Driving Policies

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Data-driven driving simulators command accelerations and steering rates from a fixed grid without constraining the realized accelerations and jerks. As a result, reinforcement-learning policies inflate safety metrics through abrupt, last-second maneuvers that lie far outside the range of human driving and would be unacceptable to occupants of a real vehicle, so the metrics measure simulator permissiveness rather than policy quality. Enforcing comfort bounds naively is not enough: lateral limits shrink quadratically with speed, so clamping a static grid saturates it and destroys fine-grained control ("grid collapse"). We propose an adaptive action parameterization that rediscretizes the grid at every step to span exactly the per-step feasible control set, via closed-form inversion of the lateral-jerk constraint. We further present PufferDrive-Editor, a browser-based tool to audit realized kinematics and author kinematically challenging scenes. On the Waymo Open Motion Dataset and a hand-authored slalom, our adaptive model holds comfort violations below 1% while outperforming clipped-grid and direct-jerk baselines in navigability.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learned driving policies are increasingly trained in data-driven simulators like Nocturne, Waymax, or GPUDrive. These simulators are built for closed-loop reinforcement learning (RL): RL trains on policy-induced states, enabling learning from rare safety-critical situations. While achieving high goal completion, their behavior is shaped by the kinematic bicycle model translating actions into motion. Standard interfaces use a fixed grid of accelerations and steering rates that does not constrain the *realized* accelerations and jerks. Consequently, RL policies learn to avoid collisions through abrupt, last-second maneuvers (sharp braking combined with hard steering) whose realized accelerations and, especially, jerks fall well outside the comfort envelope of even aggressive human driving. Safety metrics thus measure the permissiveness of the simulator's kinematics rather than policy quality, crediting evasions that no comfort-respecting vehicle would reproduce. This work studies the problem in PufferDrive, whose actuation interface is representative of the simulators above; the analysis and the proposed parameterization carry over to any simulator built on the same kinematic bicycle model.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Naively enforcing comfort bounds is difficult because the feasible action set depends nonlinearly on the vehicle state. In particular, the admissible steering range shrinks rapidly with speed, alongside additional nonlinearities from the vehicle kinematics. A static grid tuned for low speed then falls largely outside this range at higher speeds, and clamping collapses many grid points onto the constraint boundary, degrading fine-grained control ("grid collapse"). Because widely used data-driven simulators expose *discrete* action grids, we focus on maintaining a feasible discrete grid without collapse. To inspect these failure modes, we present PufferDrive-Editor, a browser-based tool for visualizing kinematic violations and authoring challenging scenarios. It lets us trace where policies breach the comfort envelope: qualitatively, most often just before sharp turns and narrow gaps. To keep control feasible in exactly these situations without collapsing the grid, we propose an adaptive action parameterization that computes the exact feasible control set at each step via closed-form inversion of the lateral-jerk constraint, re-discretizing the grid over it.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our reference points are the established kinematics models used in PufferDrive: Classic, which commands acceleration and steering from a fixed grid and enforces no comfort limits at all, and Jerk, which commands jerk and integrates it into bounded accelerations. We take the steering *rate* as the default steering command, as every constrained model below uses it, and report the original steering-angle parameterization as Classic (steer angle) alongside it. Against them we put three improved variants: Jerk equipped with realistic comfort bounds, and two versions of Classic that resolve their commands against the per-step feasible set: one by *clipping* the fixed grid into it (Clipped), one by *re-discretizing* the grid over it (Adaptive).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contributions are as follows: We show that unconstrained action spaces let learned policies inflate safety metrics through maneuvers that leave the comfort envelope of even aggressive human driving, and that naive clamping leads to grid collapse.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a constraint-aware action parameterization that adaptively re-discretizes the per-step feasible control set.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present PufferDrive-Editor, a browser-based tool for auditing realized kinematics and authoring targeted scenarios, providing a general debugging tool for exposing and analyzing failure cases in PufferDrive.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Description", "weight": 1.0} -->

We first describe the vehicle model that turns actions into motion (Sec. 2.1), then the behavioral comfort envelope that a realized trajectory should respect (Sec. 2.2), before reviewing how prior work enforces such constraints (Sec. 2.3) and showing why the two action spaces PufferDrive contains fail to do so (Sec. 2.4).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Kinematic bicycle model", "weight": 1.0} -->

Vehicle motion is commonly abstracted by the *kinematic bicycle model*: the two wheels of each axle are collapsed into a single wheel on the longitudinal axis, tire slip is neglected, and the vehicle is described by its pose, speed, and front-wheel steering angle (Fig. 1). Despite its simplicity it tracks real vehicle trajectories closely in the moderate lateral-acceleration regime of everyday driving, which makes it the standard choice for planning and for driving simulators.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Kinematic bicycle model", "weight": 1.0} -->

We parametrize the model at the *rear axle*. This is the reference point at which the tire-slip-free kinematic bicycle is exact: the rear wheel cannot slip sideways, so the rear axle's velocity always points along the vehicle heading and its speed is simply the state speed $v$ --- no slip angle appears. Choosing it as the reference point makes the comfort quantities of Sec. 2.2 identical across every dynamics model we compare, including those that never model slip at all.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Kinematic bicycle model", "weight": 1.0} -->

All controlled agents follow this model with state $(x_{t},y_{t},\psi_{t},v_{t},\delta_{t})$ as visualized in Fig. 1. Given a commanded acceleration $a_{t}$ and a steering rate $\dot{\delta}_{t}$, one step of length $\Delta t$ reads with yaw rate $\omega$ and wheelbase $L$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Kinematic bicycle model", "weight": 1.0} -->

Comfort is judged on the *realized*, not the commanded, longitudinal and lateral accelerations, and both are read at the rear axle. The longitudinal acceleration is the change in rear-axle speed, and the lateral (centripetal) acceleration is that speed times the rear-axle yaw rate: with the realized jerks the backward differences $j^{\mathrm{lon}}_{t+1}=(a^{\mathrm{lon}}_{t+1}-a^{\mathrm{lon}}_{t})/\Delta t$ and $j^{\mathrm{lat}}_{t+1}=(a^{\mathrm{lat}}_{t+1}-a^{\mathrm{lat}}_{t})/\Delta t$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Comfort bounds on vehicle kinematics", "weight": 1.0} -->

Occupants perceive vehicle motion through acceleration and its time derivative, jerk; abrupt or sustained accelerations can cause discomfort and motion sickness. We adopt the Occupant's Preference Metric (OPM) of Bae *et al*., which defines a behavioral comfort envelope via five parameters: where $a^{\mathrm{lon}}_{\max}$ and $a^{\mathrm{lon}}_{\min}$ denote the throttle and braking thresholds, respectively, while the lateral acceleration and jerk limits are symmetric about zero.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Comfort bounds on vehicle kinematics", "weight": 1.0} -->

anchor the tightest profile in public-transport data, where freestanding passengers lose posture; we show it for reference but drive with the two automotive profiles. The normal profile uses seated-occupant thresholds, and the aggressive profile uses observed human driving extremes; naturalistic driving studies likewise treat sustained high jerk not as a physical impossibility but as the signature of an aggressive driver.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Comfort bounds on vehicle kinematics", "weight": 1.0} -->

These are *behavioral* envelopes, sitting well inside the physical handling limits: leaving the aggressive band is not impossible, only something essentially no human driver would choose and no occupant would accept. We therefore call a control feasible relative to the enforced profile rather than in an absolute physical sense.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Comfort bounds on vehicle kinematics", "weight": 1.0} -->

In the original OPM system, bounds are soft constraints enforced at the path-planning level. Data-driven traffic simulators also evaluate these comfort quantities *post hoc* using metrics or Wasserstein distance penalties. In contrast, we use the comfort envelope to constrain the policy's action space directly: at each step, we analytically compute the feasible set of controls whose realized body-frame quantities stay inside the envelope (Figure 2) and re-discretize the action grid over this set (Section 3.1), guaranteeing comfort by construction.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Kinematic models in driving simulators", "weight": 1.0} -->

Data-driven simulators such as Nocturne, Waymax, and GPUDrive share a common actuation interface: a kinematic bicycle model driven from a fixed grid of controls that is clamped only to static input ranges. Nothing bounds the realized accelerations or jerks, the gap our work targets in Section 3.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Feasibility in learned models", "weight": 1.0} -->

Prior works build kinematic constraints into learned motion models, such as routing trajectories through a bicycle-model layer (e.g., Deep Kinematic Models, Trajectron++ ) or propagating uncertainty through stochastic kinematic layers. While these methods make *predicted trajectories* dynamically consistent by construction, they act downstream of action selection: a policy remains free to command an out-of-envelope maneuver that the layer then realizes rather than forbids. We instead constrain selection itself, bounding the feasible action set of a *closed-loop policy* at every simulation step under a behavioral comfort envelope. We expect this to matter most for the adaptive variant: by re-discretizing a full-resolution grid over the feasible set, it lets the policy optimize entirely within the envelope, so the constraint is reflected in what the policy learns rather than corrected after the fact.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Constrained reinforcement learning", "weight": 1.0} -->

The simplest approach leaves the action space untouched and penalizes violations in the reward, as Gigaflow does for harsh acceleration and jerk. Comfort then competes with progress through a tunable weight: violations get rarer but are never ruled out. Hard enforcement is typically done via external layers that mask or project actions. However, when the feasible set shrinks (e.g., quadratically with speed), these methods suffer from grid collapse, where distinct discrete actions alias to the same boundary values. While action mapping and jerk-bounded generators address constrained action selection, our approach analytically computes a per-step feasible action region and adaptively re-discretizes the action grid onto it, preserving action resolution across varying vehicle speeds while guaranteeing feasible commands.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Default models and their failure modes", "weight": 1.0} -->

PufferDrive provides two kinematics models by default. Classic commands an acceleration and a steering command directly from a fixed $7\times 13$ grid, applied unchanged. Nothing ties consecutive commands together: within one step of $\Delta t=0.1\,\mathrm{s}$ the policy may switch from full braking to full throttle or slew the steering across its whole range, producing jerks orders of magnitude beyond any human comfort envelope. As a result, Classic learns effective but kinematically implausible driving.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Default models and their failure modes", "weight": 1.0} -->

The steering command comes in two parameterizations: the steering *angle* $\delta_{t}$, as originally implemented, or the steering *rate* $\dot{\delta}_{t}$, which integrates to the angle and therefore low-pass filters the steering without bounding anything. Every constrained model in this work commands the rate (Sec. 6), so we treat it as the default parameterization: Classic denotes the steer-rate model throughout, and the original is written Classic (steer angle).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Default models and their failure modes", "weight": 1.0} -->

Jerk sits at the opposite end: the policy commands longitudinal and lateral *jerk*, which the environment integrates into accelerations clamped to the comfort band, so the limits hold by rule. It is not a separate dynamics model: the same kinematic bicycle model of Sec. 2.1 runs underneath, only re-parameterized one derivative up. The longitudinal jerk integrates to the speed, while the lateral jerk integrates to a lateral acceleration that is mapped back to a steering angle through the bicycle curvature relation $\delta=\arctan(\kappa L)$ with $\kappa=a^{\mathrm{lat}}/v^{2}$. The disadvantage is that the action now operates on the second derivative of the velocity: credit assignment must propagate through $j\to a\to v\to x$, and the same jerk action produces different motion depending on the accumulated acceleration state. A single action barely changes the trajectory, and exploration in jerk space is much harder.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Method", "weight": 1.0} -->

We therefore introduce an action space in between: the policy commands an *acceleration and a steering rate* $(a_{t},\dot{\delta}_{t})$ --- one derivative closer to the trajectory than jerk control --- and the comfort limits are enforced inside the environment step by restricting each command to the set feasible from the current state (Sec. 3.1). Two variants of this restriction are compared (Sec. 3.2): *clipping*, which keeps Classic's absolute action semantics, and *adaptive re-discretization*, which re-maps the action grid onto the feasible set at each step so that actions never collapse onto the limit values.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Per-step feasible set", "weight": 1.0} -->

Combining the jerk and absolute limits yields per-axis target bands $\mathcal{A}^{\mathrm{lon}}_{t}$ and $\mathcal{A}^{\mathrm{lat}}_{t}$. The longitudinal band directly bounds the commanded acceleration $a_{t}$ via $v_{t+1}=v_{t}+a_{t}\Delta t$. In contrast, the lateral band couples both control inputs: Thus, the realized lateral acceleration depends on both the next speed, determined by $a$, and the next steering angle, determined by $\dot{\delta}$. The jointly feasible action set is and is generally not separable into independent intervals.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Per-step feasible set", "weight": 1.0} -->

A key observation is that $\omega_{t+1}$ depends only on the steering-rate command and the known current speed $v_{t}$. Consequently, for fixed $\dot{\delta}_{t}$, $a^{\mathrm{lat}}_{t+1}$ is linear in $v_{t+1}$, allowing the lateral band $\mathcal{A}^{\mathrm{lat}}_{t+1}$ to be inverted analytically into an interval on $v_{t+1}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Constructing the feasible box", "weight": 1.0} -->

The box is a deterministic function of the current state. We first intersect the actuator-rate limits with the mechanical angle constraint $|\delta_{t}+\dot{\delta}_{t}\Delta t|\leq\delta_{\max}$. Sampling this entire interval uniformly is ineffective at speed: the lateral band permits only a narrow interval of rates. We therefore invert $\mathcal{A}^{\mathrm{lat}}_{t+1}$ at the nominal next speed $v_{\mathrm{nom}}=v_{t}+a^{\mathrm{lon}}_{t}\Delta t$, which yields candidate rates The nominal-speed approximation only guides sampling: we widen the resulting rate window, intersect it with the hard rate and angle limits, and retain the full hard interval at low speed. We sample $17$ rates centered on the prior rate and test each against the exact reachable acceleration interval.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Constructing the feasible box", "weight": 1.0} -->

For each sampled rate, $\omega_{t+1}$ is known. Intersecting the speed interval reachable through the longitudinal band with the interval obtained by dividing $\mathcal{A}^{\mathrm{lat}}_{t+1}$ by $\omega_{t+1}$ gives the exact feasible acceleration interval for that rate: a vertical slice of $\mathcal{F}_{t}$ (Fig. 3(a) ‣ Figure 3 ‣ Adaptive. ‣ 3.2 Clipped and adaptive action mapping ‣ 3 Method ‣ Comfort by Construction: Adaptive, Comfort-Bounded Action Spaces for Learned Driving Policies")). For every contiguous feasible run, we intersect its acceleration intervals to form a rectangle. The retained box $[\underline{a}_{t},\bar{a}_{t}]\times[\underline{\dot{\delta}}_{t},\overline{\dot{\delta}}_{t}]$ is the candidate with the largest normalized area; when the anchor sample is feasible, candidates must contain it.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Constructing the feasible box", "weight": 1.0} -->

Its middle discrete action therefore repeats the last action whenever compatible with comfort. The box is an inner approximation of $\mathcal{F}_{t}$, recomputed at every control step, and every command it contains is feasible by construction.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Clipped and adaptive action mapping", "weight": 1.0} -->

Both variants draw from the same nominal $7\times 13$ grid of accelerations and steering rates; they differ in what an action index *means* (Fig. 3(b) ‣ Figure 3 ‣ Adaptive. ‣ 3.2 Clipped and adaptive action mapping ‣ 3 Method ‣ Comfort by Construction: Adaptive, Comfort-Bounded Action Spaces for Learned Driving Policies")).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Clipped", "weight": 1.0} -->

Action indices keep fixed physical values, and the requested command is clipped componentwise into the box. Semantics are stable, but whenever the box is smaller than the grid span --- the typical regime for steering at speed --- many indices collapse onto the same box border: effectively only the extreme commands remain distinguishable, and the policy cannot tell from the action alone what will actually be executed.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Adaptive", "weight": 1.0} -->

To ensure a fair comparison with the Classic model in PufferDrive, we use the same number of discrete actions ($7\times 13$), while remapping them to acceleration and steering-rate commands. These discrete actions are mapped to acceleration and steering-rate commands and re-discretized onto the current feasible box at every step using a piecewise-linear *anchored map*: for an interval $[\ell_{t},h_{t}]$ and anchor $c_{t}$, the middle index maps exactly to $c_{t}$, the extreme indices to the borders, and intermediate indices interpolate linearly on each side. The anchor is chosen as the previous step's *realized* action whenever it remains feasible under the current box; otherwise, the interval is mapped without an anchor. When used, the anchor gives the middle action the semantics "repeat what you just did". All $7\times 13$ actions remain distinct and feasible by construction --- nothing saturates --- at the price of *relative* semantics: the same index denotes different physical commands in different states.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Adaptive", "weight": 1.0} -->

(b) Action Resolution Overlay Figure 3: Construction and utilization of the feasible action space. (a) Per-step construction of the feasible action box (computed from an actual vehicle state; see text for parameters). The orange band denotes the longitudinal target interval 𝒜t + 1lon, while the blue region contains all (, δ̇t) pairs satisfying the lateral target band 𝒜t + 1lat. Their intersection (purple) is the feasible set ℱt + 1, from which the largest axis-aligned rectangle (black) is retained. (b) Comparison of action resolution strategies against the feasible interval [ℓt, ht]. In the Clipped approach (purple arrows and dark purple dots), fixed grid values saturate at the borders, causing multiple indices to collapse. In the Adaptive approach (teal line and dots), the grid is directly re-discretized onto the interval, locking the middle index to the anchor ct (circled) and spreading extremes exactly to the borders so that all indices stay distinct and feasible.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Observations", "weight": 1.0} -->

The feasible box depends on the previous realized accelerations and steering rate, which are not visible in the instantaneous pose --- a policy without this information would face a partially observed problem, since identical observations could resolve the same action differently. Both variants therefore observe, in addition to the standard ego features, the previous realized action (the anchor) and the four box edges, normalized by the profile limits. The two variants share the identical observation layout, so their comparison isolates the action-mapping strategy alone.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate our comfort-bounded kinematic models against unconstrained and naively bounded baselines. Our experiments are designed to address two key questions: Limit Compliance: does enforcing the comfort envelope actually eliminate envelope-violating motion? Navigation Cost: what, if any, is the cost of these comfort constraints on navigation performance?

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We evaluate our models in PufferDrive, a data-driven 2D bird's-eye view simulator built on the Waymo Open Motion Dataset (WOMD) and parallelized via PufferLib. All vehicles in a scene are controlled simultaneously for episodes of $9.1\,$s ($\Delta t=0.1\,$s), with agents removed upon collision, leaving the drivable area, or reaching their goal. We train on $80{,}000$ WOMD scenarios and evaluate on the held-out validation split of $10{,}000$ scenarios.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Policies are trained using Proximal Policy Optimization (PPO) for $2$ billion steps across three seeds, using a recurrent actor-critic network and simple reward terms such as collision, offroad and goal reaching. All configurations share identical hyperparameters and training budgets, differing only in their action spaces and bound enforcements.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Model Configurations", "weight": 1.0} -->

We compare the six kinematic models introduced above. The three *unconstrained* baselines, Classic, Classic (steer angle) and Jerk (Section 2.4), check no action against the comfort envelope (Figure 2). The first two differ only in whether the policy commands the steering rate or the steering angle. The pair isolates the effect of that interface choice from the effect of enforcing the envelope. The other three enforce the envelope, in increasing order of how much of the feasible set they preserve: Jerk (bounded grid) restricts the jerk grid a priori with a single static conservative grid; Clipped Classic clips each command into the per-step feasible box axis by axis; and Adaptive Classic (ours) re-discretizes its grid onto that box, so every selectable action is feasible by construction (Section 3.2). Every Classic model except the one qualified as (steer angle) commands steering *rate* rather than angle (Section 6).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Model Configurations", "weight": 1.0} -->

The comfort envelope is a property of the simulator, not the model: each constrained model builds its feasible set from either the aggressive or the tighter normal band (Figure 2). Unless stated otherwise, results enforce the aggressive band.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Evaluation Protocol", "weight": 1.0} -->

Each trained policy is evaluated on the validation split, and we report mean $\pm$ standard deviation over the three seeds.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Evaluation Protocol", "weight": 1.0} -->

We report three navigation metrics (the share of agents reaching their goal, the share colliding, and the share leaving the drivable area) and, for each of the four kinematic quantities ($a^{\mathrm{lon}},a^{\mathrm{lat}},j^{\mathrm{lon}},j^{\mathrm{lat}}$), the share of steps that violate the comfort envelope. Two properties of this tally matter for reading the results. First, we measure the *realized* quantity, not the commanded one: a model that bounds its inputs but still drives outside the envelope through the coupling terms is counted as violating, which is precisely the failure mode naive clamping exhibits. Second, the tally covers only the steps an agent actually drives (steps after removal or goal completion are excluded), so the rate is a share of driving rather than of episode length, which would otherwise reward a model for finishing early.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Qualitative Analysis and PufferDrive-Editor", "weight": 1.0} -->

Aggregate metrics over the validation split average away the rare, safety-critical moments in which the limits actually bind. To inspect behavior near those limits we present PufferDrive-Editor, a browser-based scene editor and policy-debugging interface that runs locally on the map and scenario binaries loaded by PufferDrive. Although motivated by the analysis of our constraint-aware kinematic models, PufferDrive-Editor is a general tool for understanding learned driving policies in PufferDrive, enabling researchers to identify policy strengths, weaknesses, and failure modes beyond aggregate metrics. It combines three functions. A *scenario and track editor* loads road layouts from scenario binaries and lets researchers author stress tests by moving or inserting static obstacles and placing dynamic vehicles with custom poses, velocities, trajectories, and goals (e.g., narrow corridors or parked cars); this isolates skills such as slalom maneuverability and short-distance emergency braking. A *real-time kinematics dashboard* plots the realized metrics at every step against the OPM boundaries (Fig. 4), highlighting comfort exceedances in red so it is immediately visible whether a breach occurred in acceleration or jerk.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Qualitative Analysis and PufferDrive-Editor", "weight": 1.0} -->

Finally, *multi-model auditing* compares two rollouts either side by side, with synchronized timelines and feasible action boxes $\mathcal{F}(s)$, or overlaid on a single map, making visible where a policy under naive clamping saturates its steering and leaves the lane while the adaptive model preserves the authority to negotiate the obstacle.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Results", "weight": 1.0} -->

We now return to the two questions that motivated our experiments: whether enforcing the comfort envelope actually eliminates envelope-violating motion, and what it costs in navigation performance. We first report the aggregate numbers across all six kinematic models (Section 5.1), then turn to the stress-test scenes that expose the mechanism behind those numbers (Section 5.2).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Quantitative Performance on PufferDrive", "weight": 1.0} -->

Table 1 reports navigation performance and the realized-kinematics violation rate for all six kinematic models over three seeds; Figure 5 resolves the violation columns into the full driving-zone distribution.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Unconstrained control drives outside the envelope", "weight": 1.0} -->

The unconstrained Classic baselines achieve the highest goal completion performance, but only by driving outside the comfort limits. They exceed even the aggressive comfort envelope on far more than a quarter of their steps, mostly in lateral jerk, followed by longitudinal jerk and lateral acceleration, with maximum violations reaching 4513% for jerk and 93% for acceleration. In comparison, the constrained variants only exceed the bounds when e.g. the physical steering-angle limit prevents their enforcement, with maximum violations of just 0.26% for jerk and $9\times 10^{-4}$% for acceleration. Which steering command the policy holds barely matters for the performance metrics, the steer-rate and steer-angle variants are within noise of each other in goal completion and collisions. Commanding the rate integrates the steering and thereby reduces the violations that a single abrupt angle change can produce. While the unconstrained Jerk baseline removes acceleration violations by construction, it worsens jerk violations because the action space of the jerk model is already partially outside the aggressive bounds.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Enforcing the envelope costs little", "weight": 1.0} -->

Both clipping and adaptive re-discretization reduce comfort violations to essentially zero (Fig. 5), while reducing goal completion by around two percentage points compared to the unconstrained Classic baseline. In contrast, the bounded-grid Jerk baseline achieves lower navigation performance, indicating that a single static action grid is overly restrictive across varying vehicle speeds. Among the per-step projection methods, adaptive re-discretization consistently performs best: it matches clipping's comfort guarantees while achieving slightly higher goal completion and lower collision and off-road rates under the aggressive profile. The same trend is maintained under the tighter normal profile.

<!-- chunk {"id": "body-0048", "role": "body", "section": "The constraint does not make policies drive conservatively", "weight": 1.0} -->

Zero violations alone would be insufficient evidence if the policy simply avoided operating near the limits. Figure 5 shows the opposite: the adaptive model spends $\approx 74\%$ of driven steps in the *aggressive* longitudinal-acceleration band and roughly half in the aggressive jerk bands. It operates at the very edge of the safety envelope without crossing it; in contrast, the unconstrained baselines mostly fluctuate between normal operation and violation states for longitudinal and lateral jerk.

<!-- chunk {"id": "body-0049", "role": "body", "section": "The constraint does not make policies drive conservatively", "weight": 1.0} -->

Classic (steer angle) Jerk (bounded grid) Jerk (bounded grid) Table 1: Navigation performance per dynamics model on the PufferDrive validation split, under the AGGRESSIVE and NORMAL comfort profiles, averaged over three seeds, in percent. Unconstrained baselines do not enforce comfort limits and are reported once. Navigation columns give mean ± std. Bold marks the best value per column within each outer group (Unconstrained, Aggressive, or Normal): the unconstrained baselines buy their navigation numbers with envelope-violating control, so comparing them against constrained models would be unfair.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Tightening the envelope", "weight": 1.0} -->

Table 1 repeats the comparison under the tighter normal comfort profile, where the models may only command actions within the comfortable band. All families degrade by a similar margin ($\approx 4$ points of goal reaching) as the feasible set shrinks, and adaptive re-discretization remains the strongest constrained driver: the adaptive steer-rate model reaches $92.73\%$ goal completion, the best of any constrained model under the normal profile, while keeping violations at zero because it preserves full action resolution inside whatever box remains rather than collapsing a fixed grid onto its boundary.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Qualitative Analysis in Stress-Test Scenes", "weight": 1.0} -->

Aggregate metrics conceal what happens where the limits bind. Inspecting rollouts in the hand-authored stress-test scenes (Section 4.4) with PufferDrive-Editor's dashboard (Fig. 4), the unconstrained configurations show acceleration and jerk spikes leaving the envelope just before sharp turns or collisions, while our adaptive model keeps inputs smooth and strictly inside the bounds. Figure 6 makes this concrete on a slalom under four models: the bounded-grid Jerk baseline deviates from the reference and leaves its goals unreached, whereas our adaptive model tracks the route through the slalom and reaches its goals cleanly within the comfort bounds.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Discussion", "weight": 1.5} -->

The quantitative results and qualitative profiles validate our hypotheses regarding RL action spaces under constraints, yielding several insights.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Comfort vs. navigability trade-off", "weight": 1.0} -->

Moving from the aggressive to the normal profile consistently drops goal completion by roughly $4$ percentage points and raises collisions, as the tighter bounds curb aggressive braking and acceleration: passenger comfort directly constrains defensive reactivity. One might worry that bounding the action space removes the emergency maneuvers a policy needs to stay safe, but the envelope is a configurable profile rather than a fixed ceiling. The aggressive band sits at the extremes of human driving, so the policy keeps the full range a human would use and forgoes only motion beyond it, and a deployment wanting a wider margin can enforce a looser profile. Empirically the constraint rarely binds, costing under two points of goal completion against the unconstrained baseline while removing nearly all violations.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Adaptive mapping beats clipping and jerk control", "weight": 1.0} -->

Adaptive mapping outperforms clipped steering and jerk control, mainly in safety-critical navigation. While all constrained methods achieve similar goal completion, adaptive re-discretization preserves steering resolution within the feasible range, improving control authority when avoiding collisions and off-road events. Clipping instead saturates the fixed action grid as the steering range shrinks at high speed. Jerk control is weakest in these hard-navigation settings because second-order actions introduce an additional integration chain ($j\rightarrow a\rightarrow v\rightarrow x$), making the control problem harder to learn and credit assignment more difficult. Thus, while jerk control is simple to constrain, direct first-order control is better suited for precise obstacle avoidance and boundary recovery.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Action-space design: rate vs. angle, hard vs. soft", "weight": 1.0} -->

We command steering rate ($\dot{\delta}$) rather than steering angle ($\delta$) by default, and all constrained Classic variants use it. Rate control provides a useful balance between responsiveness and smoothness: it avoids abrupt steering changes while retaining more control authority than jerk-based control, which introduces an additional integration chain. The two unconstrained variants are compared in Table 1 to isolate the effect of the steering action space where both perform comparably bad. Alternatively, comfort can be encouraged through reward penalties, as Gigaflow does for harsh acceleration and jerk. Such a penalty prices comfort against other objectives through a tunable weight rather than ruling a maneuver out, so the optimal policy still accepts a violation whenever the payoff of an evasive maneuver exceeds its cost. Reward design therefore shapes driving preferences but cannot reliably define which actions should be considered unacceptable. Hard action constraints and reward shaping are complementary: the constraint makes out-of-envelope motion unreachable by construction and so guarantees compliance with the modeled comfort envelope, while the reward can optimize driving style within the feasible region.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced a constraint-aware, adaptive action-mapping framework to address the reliance of learned driving policies on maneuvers no human driver would perform and no occupant would accept. By analytically inverting the lateral-jerk constraint in next-steering-angle space, our approach dynamically scales the control grid to span exactly the comfort envelope at each step. On WOMD and a hand-authored slalom stress test, the proposed adaptive steer-rate Classic model enforced comfort compliance (limiting comfort violations to below $0.01\%$) and outperformed clipped and direct-jerk baselines in navigability. Because every action the policy can select now lies inside the enforced comfort envelope, the resulting safety metrics reflect policy quality rather than the simulator's permissiveness, closing the gap that motivated this work. Interactive audits via PufferDrive-Editor confirmed that adaptive re-discretization preserves steering authority and prevents grid collapse, allowing the policy to negotiate the slalom's tight turns and narrow gaps.
