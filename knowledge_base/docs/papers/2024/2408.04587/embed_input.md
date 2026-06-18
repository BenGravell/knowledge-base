<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

FORGE: Force-Guided Exploration for Robust Contact-Rich Manipulation under Uncertainty

Topics include Robotics, Safety, Robustness, Uncertainty, Control, Learning, FORGE.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present FORGE, a method for sim-to-real transfer of force-aware manipulation policies in the presence of significant pose uncertainty. During simulation-based policy learning, FORGE combines a force threshold mechanism with a dynamics randomization scheme to enable robust transfer of the learned policies to the real robot. At deployment, FORGE policies, conditioned on a maximum allowable force, adaptively perform contact-rich tasks while avoiding aggressive and unsafe behaviour, regardless of the controller gains. Additionally, FORGE policies predict task success, enabling efficient termination and autonomous tuning of the force threshold. We show that FORGE can be used to learn a variety of robust contact-rich policies, including the forceful insertion of snap-fit connectors. We further demonstrate the multistage assembly of a planetary gear system, which requires success across three assembly tasks: nut threading, insertion, and gear meshing. Project website can be accessed at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We are interested in developing *sim-to-real* techniques for learning assembly primitives (e.g., low-clearance insertion or nut-threading). Over the past decade, sim-to-real techniques have led to advances in dexterous manipulation and legged locomotion. However, similar results have only recently been achieved for robotic assembly, which requires efficient and accurate simulation of the detailed, low-clearance parts. Even with these advances, successful sim-to-real deployment remains challenging for contact-rich tasks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Naively, policies can be too aggressive, leading to catastrophic part slip or damage that makes the task difficult or impossible to complete. This is particularly pronounced when there is pose uncertainty and search behaviours that rely on contact are necessary. The required contact between parts can lead to undesirable outcomes if the forces are too high. Heuristic approaches, such as spiral search, can limit the applied force but these approaches are task-specific and can be inefficient.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning offers a general paradigm for developing more flexible search behaviours. However, previous works typically rely on additional procedures to ensure policies are deployed safely with desirable force profiles. For example, policies trained using the *IndustReal* framework do not observe or adapt to contact forces. Instead, as our experiments show, forceful behaviour is determined by careful controller design and gain tuning. Other works provide methods to optimize or adapt gains online. Importantly, the desired force profile of a policy depends on the task at hand. For example, threading a nut may fail if the applied force is too high, while a snap-fit connector might require large forces to ensure proper insertion. Therefore, it is important to have simple and efficient methods to tune the policy's force profile.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose FORGE: a framework for developing force-aware sim-to-real policies for assembly tasks. FORGE policies, trained solely in simulation, use external force observations to achieve efficient and gentle behaviour. Additionally, policies are trained without precise knowledge of part poses, leading to emergent search behaviours that are robust to significant levels of pose uncertainty.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

FORGE has two complementary components to ensure policies are robust to contact. First, we propose to condition policies on a *force threshold* that should not be exceeded during task execution. Second, policies are trained to maintain this threshold under a wide range of dynamics randomizations (we randomize *robot*, *controller*, and *part* properties). Together, these components result in policies that can modulate their actions to achieve a force profile that respects the interpretable scalar force threshold. By randomizing this threshold during training, we are able to tune it at deployment time without retraining the policy.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

For tasks with high enough clearance, a small force threshold is sufficient and no tuning is necessary. However, tasks that require significant force to succeed (e.g., snap-fit connectors) may fail if the threshold is set too low. When the required force is not known a priori, we present an automatic tuning procedure which leverages a notion of *success prediction*. Based on the outcome of a policy execution, the threshold can be iteratively adjusted for future trials. To automate this tuning, FORGE policies are trained to predict whether an episode succeeded or failed. We validate this procedure by showing successful sim-to-real transfer on a snap-fit connector requiring $15N$ for insertion.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, we show how success prediction can lead to more efficient policy termination. Standard practice in *sim-to-real* assembly is to execute policies for a fixed duration which can lead to premature termination or delays. Instead, the policy can terminate when it believes it is in a successful state. We show that success prediction, also trained in simulation, robustly transfers to the real world and does so more reliably when using force observations.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A method to specify maximum allowable contact-force during policy execution. This results in policies that exhibit safe search behaviour even with significant levels of position estimation error (up to $5mm$).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

A dynamics randomization scheme that reduces tuning to an interpretable scalar force-threshold parameter (instead of controller gains).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

A method for success prediction that enables automatic force-threshold tuning and efficient policy termination, reducing delay times up to $66\%$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

A demonstration of multi-part assembly of a planetary gearbox requiring a diverse set of skills, including the challenging task of fastening nuts and bolts.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Results are shown for over $1000$ real-world trials and multiple tasks. We plan to release the code with the paper.

<!-- chunk {"id": "body-0015", "role": "body", "section": "RL for Contact-Rich Assembly", "weight": 1.0} -->

We want to learn policies for tasks with tight tolerances and detailed geometry. We first describe the problem formulation before introducing FORGE in the next section.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A Assembly Tasks", "weight": 1.0} -->

Each task involves mating two parts: one grasped and another fixed to the workspace. For our main evaluations, we consider all three tasks from *Factory* and demonstrate the first sim-to-real transfer for threading a small M16 nut. We also consider forceful snap-fit insertion and multi-step assembly in Sec. V-D and Sec. V-E respectively.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A Assembly Tasks", "weight": 1.0} -->

Peg Insertion: A round peg with $8mm$ diameter needs to be inserted into a socket with $0.5mm$ diametrical clearance.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A Assembly Tasks", "weight": 1.0} -->

Gear Meshing: A gear needs to be inserted onto a peg with $0.5mm$ clearance. Other gears are present and the teeth of adjacent gears must be aligned for successful meshing.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A Assembly Tasks", "weight": 1.0} -->

Nut Threading: Instead of fully lowering a nut onto a bolt as in *Factory*, we define the *nut threading* task as successfully threading the nut such that it cannot be lifted by a vertical motion (we find lowering by a quarter-thread is sufficient). Because our robot has joint limits, and to prevent the need to regrasp, we assume the nut and bolt are initially oriented^11^1We leave the more challenging, yet realistic, scenario involving completely unobserved thread orientation to future work. such that success can be achieved with a single revolution of the wrist joint. We consider nuts with a relatively small size (M16) compared to previous sim-to-real work (M48). A successful search behaviour will resolve lateral uncertainty and place the nut on the bolt before rotating the wrist (otherwise the threads may not mesh).

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B POMDP Formulation", "weight": 1.0} -->

We formulate our problem as a *Partially Observable Markov Decision Process* (*POMDP*).The goal is to learn a policy, $\pi_{\theta}{(\left. a_{t} \middle| {o_{1},\ldots,o_{t}} \right.)}$,

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B POMDP Formulation", "weight": 1.0} -->

where $\tau = {(s_{0},a_{0},o_{0},s_{1},a_{1},o_{1},\ldots)}$ is the trajectory of states, actions, and observations resulting from the robot following policy $\pi_{\theta}$. Below, we further specify the components of the POMDP for contact-rich tasks.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B POMDP Formulation", "weight": 1.0} -->

States ($\mathcal{S}$): A state, $s_{t} \in \mathcal{S}$ consists of the pose and velocities of the end-effector (EE), fixed part, and held part: ${p^{ee},p^{fixed},p^{held}} \in {SE{}}$ and ${v^{ee},v^{held}} \in {\mathbb{R}}^{6}$.We also include the contact force experienced by the end-effector, $F^{ee} \in {\mathbb{R}}^{3}$, and time-invariant information about the dynamics properties of the robot, controller, and parts (e.g., mass or joint-friction): $\Psi = {(\psi_{robot},\psi_{control},\psi_{parts})}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B POMDP Formulation", "weight": 1.0} -->

We do not include pose or velocity of the held part because it can move in the gripper and be difficult to track.Likewise, we do not observe $\Psi$, but include the previous action, $a_{t - 1}$, to help infer dynamics. See App. -A for noise models.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B POMDP Formulation", "weight": 1.0} -->

Actions ($\mathcal{A}$): Control targets for a task-space impedance controller. As in previous work, we assume all parts are in an upright orientation. Thus it is sufficient for the policy to only have control authority over the ($x,y,z,{yaw}$)-dimensions: $a_{t} \in \mathcal{A} = {\mathbb{R}}^{4}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B POMDP Formulation", "weight": 1.0} -->

Transition Function ($T_{\Psi}:{{\mathcal{S} \times \mathcal{A}}\rightarrow\mathcal{S}}$): $T$ is parameterized by the dynamics parameters, $\Psi$ and is specified using the *IsaacGym* simulator. The sim-to-real gap comes from the mismatch between $\Psi^{sim}$ and $\Psi^{real}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B POMDP Formulation", "weight": 1.0} -->

Observation Function ($O:{{\mathcal{S} \times \mathcal{A}}\rightarrow\Omega}$): The position of the fixed part is assumed to have up to $5mm$ error. Gaussian noise is assumed for each of the other observations.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B POMDP Formulation", "weight": 1.0} -->

Reward Function ($R:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$): Each task is described using a keypoint reward: $R_{kp}{(p^{fixed},p_{t}^{held})}$, which is modified to account for small, threaded geometries (see App. -B for more details).

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B POMDP Formulation", "weight": 1.0} -->

We found the bonuses led to more robust learning when there is significant pose uncertainty.

<!-- chunk {"id": "body-0029", "role": "body", "section": "FORGE: Robust Search under Uncertainty", "weight": 1.0} -->

FORGE uses on-policy RL to learn search behaviours in simulation. A *force threshold* (Sec. III-A) and *dynamics randomization* (Sec. III-B) are introduced for robust sim-to-real transfer. FORGE also introduces *success prediction* (Sec. III-C) for efficient termination and force threshold tuning.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Force Threshold", "weight": 1.0} -->

During policy execution, excessive force can cause parts to slip or become damaged.Although it may be possible to recover from small amounts of slip with the right sensors (e.g., wrist camera or tactile), we prefer to avoid these scenarios. Instead, we propose to condition the policy on a *force threshold*, $F_{th}$: $\pi{(\left. a \middle| {o,F_{th}} \right.)}$. During training, the policy is penalized if the contact force, $F_{t}^{ee}$, exceeds the threshold.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Force Threshold", "weight": 1.0} -->

Note this is related to which conditions the policy on a *desired force* instead of an *excessive force*.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Force Threshold", "weight": 1.0} -->

At deployment time, $F_{th}$ can be set or tuned based on task requirements. Most of the tasks we consider have positive clearance and do not require much force to succeed. A relatively low force threshold is sufficient to prevent slip and tuning the threshold is not necessary. For forceful insertion, nominal insertion forces are often speficied on part datasheets and the threshold should be higher than this value. We also present an automatic tuning procedure in Sec. III-C.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B Dynamics Randomization", "weight": 1.0} -->

To successfully deploy policies trained in simulation, it is important that the trajectory distribution experienced during training is similar to what it would be when deployed: ${p{(\left. \tau^{real} \middle| {\pi_{\theta},\Psi^{real}} \right.)}} \approx {p{(\left. \tau^{sim} \middle| {\pi_{\theta},\Psi^{sim}} \right.)}}$. The difference between these distributions is usually referred to as the *sim-to-real gap*. This gap is usually handled by system identification (Sys-ID) or dynamics randomization (DR). The goal of Sys-ID is to tune $\Psi^{sim}$ to be close to $\Psi^{real}$. This itself is a complicated tuning procedure that may need to be redone for every new set of parts.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B Dynamics Randomization", "weight": 1.0} -->

Instead, we follow the DR approach which learns policies that are *robust* to a wide range of dynamics parameters. Concretely, we optimize a version of Eq.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Dynamics Randomization", "weight": 1.0} -->

The integral is approximated with Monte Carlo samples from a randomization distribution. We now describe the variables that are randomized (see App. -A for values).

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B Dynamics Randomization", "weight": 1.0} -->

Controller Randomization: The controller has a large impact on contact forces.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-B Dynamics Randomization", "weight": 1.0} -->

First, the policy outputs a relative pose, $a_{t}$, which is applied to the fixed part's pose to get an absolute target pose, $p_{t}^{targ}$. This pose is clipped by an action scale, $\lambda$, to ensure that the target is not too far from the EE's current pose. As in previous work, we use critically damped gains to ensure stable controllers: $k_{d} = {2\sqrt{k_{p}}}$. The controller thus depends on two parameters which govern how much force can be commanded: $\lambda \times k_{p}$. We randomize both quantities so that the range of maximum commandable forces is in ${\lbrack 6.4,20.0\rbrack}N$. Note that the control parameters are not included in the observations, so the policy must adjust its behavior based on force measurements. This reduces the policy's dependence on a particular controller implementation.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-B Dynamics Randomization", "weight": 1.0} -->

Controller tuning or optimization is a costly and often complex procedure. Randomization has the additional benefit that the policy is robust to a range of control parameters, greatly simplifying deployment.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-B Dynamics Randomization", "weight": 1.0} -->

Part Randomization: As parts slide against each other, material friction will affect lateral forces. To ensure policies can work across a range of materials, we randomize part mass and friction.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-B Dynamics Randomization", "weight": 1.0} -->

Robot Dynamics Randomization: Due to phenomena such as joint friction, the applied force may be smaller than the commanded force. We implement a simple way to account for this: inducing a randomized *dead-zone* in simulation. Each episode, a dead-zone is selected for each dimension, $F_{i}^{DZ}$, where commanded forces below this value are clamped to zero: ${|F_{i}^{applied}|} = {\max{(0,{{|F_{i}^{targ}|} - F_{i}^{DZ}})}}$. This enables the policy to increase its target which can help apply more force when needed or reduce steady-state error.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-B Dynamics Randomization", "weight": 1.0} -->

These randomizations lead to a policy that is robust to a wide range of dynamics parameters. Combined with the force threshold, the policy can modulate its actions to achieve safe interaction. For example, with higher gains, the policy will output smaller actions to limit the contact force.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-C Success Prediction", "weight": 1.0} -->

Although success is clearly defined in simulation where we have access to noiseless poses, it is difficult to reliably predict in the real world. Consider the nut-threading task, where the distance between a successfully threaded nut and a loose nut is a fraction of a millimeter. We propose to train a success predictor which can robustly transfer from sim-to-real. Concretely, we share the weights of the policy network with the success predictor by expanding the action space of the policy to include an early termination action: $a_{t}^{ET} \in {\lbrack 0,1\rbrack}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-C Success Prediction", "weight": 1.0} -->

where $y_{t}$ is the true success label at time $t$. This reward can also encourage behaviours that elicit the underlying success state (e.g., pull upwards on the nut to check if it is threaded).

<!-- chunk {"id": "body-0044", "role": "body", "section": "III-C Success Prediction", "weight": 1.0} -->

Early Termination: Efficient termination is a desirable property for industrial applications where cycle times matter. We want the policy to terminate as soon as the task has succeeded and no sooner. During training, episodes are executed for the maximum length. At deployment, a confidence threshold, $p_{term}$, can be used to terminate the episode: $a_{t}^{ET} > p_{term}$. See App. -D for analysis on the performance trade-offs for choosing $p_{term}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "III-C Success Prediction", "weight": 1.0} -->

Force Threshold Tuning: For forceful insertion tasks, we may not know how much force is required. Consider snap-fit connectors which require deformation. The required force depends on material properties that may be unknown and could change with extended use. To tune the force threshold, we leverage success prediction. Conservatively, we start with a low threshold of $7.5N$, which helps avoid slip and damage. If policy execution reaches a timeout before success is predicted, we increase the threshold and try again. This can be done automatically, without manual resets, until success occurs.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A Robot System", "weight": 1.0} -->

We use a *Franka Panda* robot with the *FrankaPy* library for impedance control. All policies send control targets at $15Hz$ while the controller operates at $1000Hz$. The Panda has joint-torque sensing, which is projected to EE-frame forces when needed by the policy. Alternatively, a force-torque sensor could be used.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-A Robot System", "weight": 1.0} -->

For the majority of our experiments, we calibrate the poses of each fixed object and artificially add noise. This allows us to analyze performance under known levels of position estimation error. The calibration is done by guiding the arm to a successful pose for the respective task from which a nominal initial pose can be backed out. Unless otherwise reported, our real experiments use the same initial state randomization as in simulation (see App. -A). For our last experiment, we assemble a planetary gear box (Sec. V-E) using the perception system from *IndustReal* (see App. -F for more details).

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-B Policy Training", "weight": 1.0} -->

Simulator: All policies are trained using the *Factory* simulation methods within IsaacGym. In simulation, we have access to external contact forces experienced by the end-effector (akin to what we have access to on the Panda). Noisy forces are used as policy input, whereas ground-truth forces are used to compute the excessive-force penalty. We use recurrent PPO with asymmetric actor-critic to handle partial observability. Details on initial state and observation randomization can be found in App. -A.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-B Policy Training", "weight": 1.0} -->

Checkpoint Selection: For all tasks and models, we train three policies with separate random seeds. On the real-robot, results are averaged across the three policies.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-B Policy Training", "weight": 1.0} -->

Observation and Action Frames: For generalization across the workspace, we assume actions and observations are relative to the fixed part. Specifically, the policy outputs a $4D$ relative transform from the tip of the fixed part (we assume upright parts). The control target is computed from the fixed part's pose estimate and the relative pose from the policy. The policy output is bounded, limiting the operational volume of the end-effector (targets can be up to $5cm$ away in all directions). Similar to the action space, all position observations are relative to the tip of the fixed part.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-C Baselines and Ablations", "weight": 1.0} -->

IndustReal: Policies trained using the IndustReal framework do not have velocity or force observations. A full description of the differences can be found in App. -C. The PLAI parameters from IndustReal are set to achieve similar maximum forces to what FORGE policies can command.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-C Baselines and Ablations", "weight": 1.0} -->

Baseline: Similar to FORGE but does not use force observations, dynamics randomization, or an excessive force penalty. However, it is trained with success prediction so that meaningful episode durations can be reported.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-C Baselines and Ablations", "weight": 1.0} -->

Ablations: In addition to the baselines, we also ablate each of the main components of FORGE for our sim-to-real analysis: Force (No Force), Dynamics Randomization (No DR), and Excessive Force Penalty (No FP). For the FORGE (No FP) model, which ablates the contact penalty reward term, we evaluate using two P-gain levels. Note that FORGE (No FP) results are not reported for nut threading as we found that the nut always slipped out of the gripper.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-A Baseline Comparisons", "weight": 1.0} -->

(Q1) Does FORGE lead to more robust sim-to-real transfer? (Q2) Do FORGE policies have more desirable behavioural properties?

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-A Baseline Comparisons", "weight": 1.0} -->

Duration (s): For successful episodes, time to reach a successful state (independent of success prediction).

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-A Baseline Comparisons", "weight": 1.0} -->

Each reported metric represents $45$ trials spread across $5$ workspace locations for the fixed part, and $3$ position-estimation error levels ranging from $0 - {5mm}$. Similar randomization ranges were used as in simulation except for the in-hand part randomization where the part was centered in the gripper. Results are reported in Table I.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-A Baseline Comparisons", "weight": 1.0} -->

One conclusion for Q1 is that FORGE outperformed the *Baseline* method for all tasks and *IndustReal* for both the gear meshing and nut threading tasks. Ablations show that that the primary performance gains of FORGE come from including force observations and the excessive force penalty. Although dynamics randomization did not significantly affect success rate, we later show it is important for robustness across controller gains.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-A Baseline Comparisons", "weight": 1.0} -->

Examining the behavioural metrics for Q2, we notice that FORGE used less force than both baselines and had significant improvements in trial durations when compared to *IndustReal*. During experiments, we observed FORGE led to gentler interactions between the parts (see accompanying video). The reduced force produced by this policy was especially helpful for the M16 Nut which was more susceptible to slipping than the peg or gear.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-A Baseline Comparisons", "weight": 1.0} -->

For FORGE, the main failure cases occurred when there was high position estimation error (above $1\sigma$ of the training noise, see next section). Parts got stuck on each other (peg insertion) or the nut was rotated before alignment with the bolt, causing the threads to miss. However, we found training unstable with noise above $\sigma = {2.5mm}$. Adopting a curriculum or adding additional sensing modalities (e.g., tactile sensors or wrist-cameras) may help address this.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-B Noise Analysis", "weight": 1.0} -->

We next aim to answer (Q3): How is policy performance, in terms of success rate, affected by position-estimation error? We use the same trials from the previous section, but show a breakdown of the results across different error levels. During each trial, artificial perception error was added to the fixed part's position (calibrated as described in Section IV-A^22^2Adding artificial noise allows us to better characterize performance across error level compared to a perception system whose bias and variance can be difficult to estimate and control.). A third of the trials fell in each of the three considered error levels: Low (0-1mm), Medium (1-2.5mm), and High (2.5-5mm). We considered $3D$ position error by sampling a perturbation vector with a radius uniformly sampled in the desired error range and a direction uniformly sampled from the unit-sphere.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-B Noise Analysis", "weight": 1.0} -->

Although performance is comparable for the peg insertion task, FORGE outperformed *IndustReal* for the gear meshing and nut threading tasks at all noise levels. This demonstrates that force is a useful modality to robustly recover from larger amounts of position estimation error. Performance generally degraded with error $> {2.5mm}$ which is beyond $1\sigma$ of the observation noise added in simulation. With high error, the effects of contact are more pronounced because the robot may need to search longer before the task is complete.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-C Force Analysis", "weight": 1.0} -->

Next, we investigate how FORGE limits forceful interactions. (Q4) How important is the excessive-force penalty for safe interactions? (Q5) Can FORGE limit the applied force without extensive controller tuning?

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-C Force Analysis", "weight": 1.0} -->

Excessive-Force Penalty (Q4): In Table I, we compare to an ablation, *No FP*, that was trained without the excessive-force penalty of FORGE (but still used force observations and dynamics randomization). We used the same evaluation procedure as for FORGE but deployed with two different controller gains (we chose values at the lower and middle of the gain randomization range). We found that policies deployed with the lower gains achieved similar average forces to FORGE while those deployed with higher gains naturally experienced more force. Both policies had lower success rates than FORGE which was deployed with controller gains at the middle of the randomization range.

<!-- chunk {"id": "body-0064", "role": "body", "section": "V-C Force Analysis", "weight": 1.0} -->

Gains Robustness (Q5): To measure how robust FORGE is to controller gains, we performed an additional experiment where we varied the gains at deployment time and measured success rate. We compare FORGE to *IndustReal* and multiple ablations. The experiment was carried out for the $8mm$ peg task at a single workspace location, with medium position estimation error and limited initial-state randomization. We considered $5$ proportional gain levels across the randomization range (corresponding to an $8N$ range in the maximum force the controller could apply) and each condition was evaluated $9$ times ($3$ runs per checkpoint).

<!-- chunk {"id": "body-0065", "role": "body", "section": "V-C Force Analysis", "weight": 1.0} -->

In Fig., we see that FORGE achieves high success rates while respecting the force threshold across a wide range of controller gains. However, performance is less consistent without force observations or dynamics randomization. In Fig. (top), we use a box plot to show the spread of $F_{mean}$ across the $9$ trials of each condition. The dotted line shows the deployment force-threshold: $F_{th} = {7.5N}$. We see that when the force observation was included, contact force was consistently low across gains. However, without force observations, the spread of forces across episodes was high, often exceeding the threshold at higher gains. Similarly, the force exerted by *IndustReal* policies increased with controller gains. As *IndustReal* is not force-aware, achieving desired forceful properties requires tuning controller gains. Overall, these results highlight the importance of force sensing to enable the policy to effectively modulate the contact force.

<!-- chunk {"id": "body-0066", "role": "body", "section": "V-D Success Prediction Analysis", "weight": 1.0} -->

To evaluate success prediction, we ask: (Q6) Does success prediction, trained in simulation, transfer to the real world? (Q7) Can success prediction be used to tune the force-threshold for tasks that require forceful insertion?

<!-- chunk {"id": "body-0067", "role": "body", "section": "V-D Success Prediction Analysis", "weight": 1.0} -->

Early Term. Precision: The fraction of early-terminated trials that were actually successful.

<!-- chunk {"id": "body-0068", "role": "body", "section": "V-D Success Prediction Analysis", "weight": 1.0} -->

Early Term. Recall: The fraction of successful trials which were terminated correctly with $a^{ET} > p_{term}$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "V-D Success Prediction Analysis", "weight": 1.0} -->

Early Term. Delay (s): For successful episodes, how long after success occurred did the policy terminate.

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-D Success Prediction Analysis", "weight": 1.0} -->

Results show that success prediction transferred well to the real world. The termination method correctly identified successes (high precision and recall) and worked best when using force observations for all tasks. We also see that delay times are shortest when using force observations. This shows the benefit of force for sensing task completion: when the gear has been fully meshed or the nut threads successfully engaged. Using success prediction also leads to shorter delays than *IndustReal* which uses a fixed duration.

<!-- chunk {"id": "body-0071", "role": "body", "section": "V-D Success Prediction Analysis", "weight": 1.0} -->

Force Threshold Tuning (Q7): To evaluate the utility of *success prediction* for force threshold tuning, we introduced a new *snap-fit* task. In simulation, the snap-fit buckle was implemented with torsion springs for each of the clips. The stiffness of the springs was randomized to vary the amount of force needed for insertion. We also ensured the robot's gains and force-threshold were randomized such that success was possible. In the real world, we used a snap-fit buckle that required $15N$ of force for insertion. We report real world results from running the automatic tuning procedure described in Sec. III-C. The initial force threshold was set to $7.5N$ and increased by $5N$ each policy execution until the policy predicted success. No initial state randomization or noise were added for these experiments.

<!-- chunk {"id": "body-0072", "role": "body", "section": "V-D Success Prediction Analysis", "weight": 1.0} -->

Out of $10$ trials for the complete tuning procedure (each consisting of up to $3$ policy executions with increasing force thresholds), the tuning procedure succeeds $8$ times while successful insertion occurred $10$ times. The two failures were instances where the insertion succeeded, but the policy failed to predict success. Success occurred on the third execution $9/10$ times (it once occurred on the second trial), meaning the policy generally respected the force threshold (success should not occur until the force threshold exceeds $15N$). Furthermore, of the $29$ policy executions, the success prediction by the policy was correct $27$ times.

<!-- chunk {"id": "body-0073", "role": "body", "section": "V-D Success Prediction Analysis", "weight": 1.0} -->

We also evaluated the task using a sufficiently high threshold and on a larger initial state distribution, similar to what was used during training in simulation. Here the success rate dropped to $6/10$, which we attribute to an unstable grasp leading to part slippage during contact. This reveals a limitation of having a single force threshold: for certain tasks, the optimal force threshold may vary depending on the phase of the task. For example, low forces are required until the buckle is aligned with the socket, only then is it safe to use high forces.

<!-- chunk {"id": "body-0074", "role": "body", "section": "V-E Multi-Stage Assembly", "weight": 1.0} -->

To culminate this work, we show that FORGE enables the multi-stage assembly of a planetary gearbox using a simple perception system. We assume the assembly sequence is known a priori and train FORGE policies for *Small Gear*, *Large Gear*, and *M16 Nut* tasks. We additionally introduce a new *Ring Insertion* task, which must also be robust to orientation estimation noise such that the three bolts align with the holes in the outer ring. Successfully assembling the planetary gearbox requires executing $8$ contact-rich primitives.

<!-- chunk {"id": "body-0075", "role": "body", "section": "V-E Multi-Stage Assembly", "weight": 1.0} -->

We ran $5$ trials resulting in the following success rates: Ring Insertion ($5/5$), Small Gear ($15/15$), Large Gear ($3/5$), M16 Nut ($15/15$). Early terminations saved on average $65s$ in a single trial compared to executing policies for a fixed duration. Overall, the complete assembly succeeded in $3/5$ trials where the failures correspond to the large gear insertion (which has to align the teeth of three already inserted small gears). Please see the accompanying video for a demonstration of the multi-stage assembly and App. -F for more experimental details.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In conclusion, we present FORGE, a force-aware method to train robust sim-to-real policies with pose estimation uncertainty. FORGE uses a force threshold and dynamics randomization to learn *safe* exploration behaviours, enabling successful policy execution with up to $5mm$ of position estimation error. In addition, FORGE can predict task success, allowing efficient policy execution and force threshold tuning. In future work, we plan to investigate torque sensing for more efficient search strategies. We also believe research in *real-to-sim* will help automatically tune simulation models for more adaptive behaviours.
