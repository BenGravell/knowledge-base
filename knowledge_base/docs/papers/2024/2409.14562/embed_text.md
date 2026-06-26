## Introduction

Achieving dexterity comparable to human hands has been a longstanding challenge in robotics. While even simple robots can produce dynamic, contact-rich behavior, general methods for doing so are still scarce. For contact-rich tasks, reinforcement learning (RL) has been the dominant paradigm due to its ability to generate real-world robust plans. One well-studied task is in-hand cube reorientation, where a hand must rotate a cube to match consecutive goal orientations. Pioneered by OpenAI and extended by others, RL policies trained with massively-parallelized, domain-randomized simulations have achieved remarkably robust sim-to-real transfer for cube rotation. But, this offline simulation-based approach requires substantial pre-execution computation and is inflexible to changing task specifications.

Figure 1: The DROP architecture. DROP consists of (i) a vision-based cube pose estimator (composed of the Keypoint Predictor, Smoother, and Corrector), and (ii) a sampling-based planner that selects control actions by conducting model-based rollouts and iteratively improving the sampling distribution online based on the costs J(i).

Leveraging recent advances in real-time parallel simulation (e.g., MJPC), we instead study the online approach of sampling-based predictive control (SPC) methods for in-hand manipulation, which continuously replan by simulating parallel rollouts and applying optimal control actions over short time horizons. In contrast with RL, such online planning methods can adjust the task or model without re-training, but may demand expensive online computation. While tools like MJPC have made SPC feasible for many simulated contact-rich tasks, their real-world utility remains largely unproven.

Our main contribution is DROP (Dexterous Reorientation via Online Planning), a system architecture (Fig. 1) that consists of (i) a simple sampling-based planner and (ii) a vision-based state estimator comprising a keypoint detection model, a pose smoother, and a collision-aware state corrector. Our aim is not to design the best cube reorientation policy, but to test the viability of sampling-based strategies by thoroughly assessing DROP's real-world performance, architectural design, and key factors for robustness. Still, DROP is the first online planning method for cube reorientation on hardware, and we find that its performance is comparable with prior RL-based methods. For reproducibility, we provide open-source code, estimator weights, and hardware setup^11^1Project website:..

## Background and Preliminaries

### II-A Related Work

The first viable methods for in-hand cube reorientation employed *reinforcement learning (RL)*, starting with Dactyl, which popularized domain randomization for sim-to-real transfer of RL policies. Subsequent research built on Dactyl with improved domain randomization, tactile-only sensing, and "palm-down" rotations for various objects. While typically limited to specific robots or object classes, RL's robust hardware performance has established it as the standard for in-hand manipulation.

Others have explored model-based approaches to contact-rich manipulation via *contact-implicit trajectory optimization* (CITO). Originally used in locomotion, recent work shows that such planners can generate motions for simple contact-rich tasks like bimanual lifting or real-time planar rolling and sliding. Other approaches have combined CITO with learned signed distance fields, global search, or smoothed dynamics.

*Sampling-based planning* has a long history in manipulation, starting with methods like RRT, PRM, and STOMP. Recent advances in SPC have enabled simple contact-rich manipulation like pushing, sliding, and pick and place, while new tools for real-time parallel simulation of contact-rich tasks, have made SPC viable for simulated contact-rich tasks with remarkably simple controllers. Still, little evidence exists for the viability of SPC for real-world contact-rich manipulation (concurrently, some works have studied it for locomotion ), and overall, model-based methods (like SPC or CITO) have seldom studied tasks as hard as cube reorientation, which exhibits many simultaneous unpredictable contact modes.

Lastly, high-quality *object tracking* is key for most of these methods, especially model-based online search. RL approaches usually use single-object pose estimation networks, but recent computer vision advances suggest that more general tracking pipelines like frame-to-frame point trackers and foundation models for rigid body pose prediction may boost performance.

### II-B Mathematical Notation

We model the continuous-time cube-in-hand dynamics as where $x$ is the state and $u$ are control inputs. We do not assume access to a closed-form expression for $f$, but instead to a simulator (MuJoCo) that generates state trajectories $x{(t)}$ given an initial state $x_{0}$ and a control sequence $u{(t)}$.

The state $x$ consists of the generalized positions and velocities of both the cube ($q^{c},v^{c}$) and hand ($q^{h},v^{h}$): In this work, the control actions $u$ are position setpoints for the hand, which are tracked by a lower-level PD controller internal to the model $f$. Following, we represent a control trajectory $u{(t)}$ on $t \in {\lbrack 0,T\rbrack}$ with $K$ spline knots, which constitute the decision variables for online planning. The control objective is encoded by a cost functional where querying $J{(U;x_{0})}$ requires simulating $f$ using an open-loop control signal $u{(t)}$ from initial condition $x_{0}$.

Throughout the paper, we use the following notation to denote "subtraction" of two quaternions ${a,b} \in {\mathbb{H}}$: and similarly, when ${a,b} \in {SE{}}$, ${a \ominus b} \in {{\mathfrak{s}}{\mathfrak{e}}{}}$.

## The DROP Algorithm

DROP consists of (i) a sampling-based planner and (ii) a keypoint-based cube pose estimator (see Fig. 1). The planner continually updates the control spline $U$ via SPC. We use MJPC to handle both parallel rollouts and policy updates.

### III-A Sampling-Based Planning and Control

Algorithm 1 describes a generic SPC procedure. At time $t \in {\mathbb{R}}$, the planner receives a state estimate $\hat{x}{(t)}$ and rolls out a batch of $N$ open-loop control sequences $U^{(i)}$ drawn from some parametric distribution $\pi_{\theta}(U)$. Each control trajectory is simulated (in parallel) to obtain a cost $J^{(i)}$, and all costs are jointly used to update the sampling parameters $\theta$. The control input $u{(t)}$ can be obtained for any time $t$ from the spline parameters $U$. This allows planning to proceed asynchronously, with the parameters $\theta$ updated as quickly as computational limits allow.

Input: θ, N, planner-specific parameters. // estimate curr state Algorithm 1 Sampling-based Predictive Control In our experiments, we test two simple planning strategies that both use a diagonal Gaussian distribution ${\pi_{\theta}(U)} = {\mathcal{N}\left({\Delta 111U},\Sigma \right)}$ with parameters $\theta = \left({\Delta 111U},\Sigma \right)$. In Algorithm 1, ${\mathtt{g}\mathtt{e}\mathtt{t}}_{\mathtt{a}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{o}\mathtt{n}}{(\theta,t)}$ is a spline interpolation with knots ${}\Delta{}{}{}{}111U$.

Predictive sampling (PS) repeatedly updates ${}\Delta{}{}{}{}111U$ to be the best sample, fixing $\Sigma = {\sigma^{2}I}$. Despite its simplicity, PS has demonstrated surprisingly effective performance on complex robot manipulation and locomotion tasks in simulation.

The cross-entropy method (CEM) instead fits both ${}\Delta{}{}{}{}111U$ and $\Sigma = {\operatorname{diag}{(s)}}$ to the sample mean and variance of the $M$ best elite samples, where $s$ is a vector of covariances. CEM is only marginally more complex than PS, but has long been used for general gradient-free optimization.

As in prior work, the task considered in this paper is to use a dexterous hand to rotate a cube to within 0.4 \\unit of as many goal orientations in a row as possible without dropping. The goals are uniformly randomly sampled over $SO{}$. In contrast , to ensure sufficient task difficulty, each new goal must be at least $90^{\circ}$ from the prior one.

Mathematically, the DROP cube reorientation problem is expressed as the optimal control problem where $\lambda_{(\cdot)}$ denote weights, the dynamics $f{(x,u)}$ are only available through simulation, and are running costs. The variables $p^{c}$ and $r^{c}$ denote the positional and rotational components of the cube pose $q^{c} = \left\lbrack p^{c},r^{c} \right\rbrack$, which are extracted from the simulated state $x{(t)}$. $\ell_{\text{g}}$ penalizes rotational distance from the goal, while $\ell_{\text{p}}$ penalizes the cube leaving a "safe" region $\mathcal{S}$ in Cartesian space.

In this work, we prioritize drop reduction by setting $\lambda_{\text{p}}$ high and choosing a conservative region $\mathcal{S}$ (for details, see ). In practice, we use a relatively low $\lambda_{\text{g}}$, which slows down the planner but also amplifies differences in rotation rate across methods, allowing easier quantitative comparison.

### III-B The Pose Estimation Pipeline

Our pose estimator consists of three parts: a keypoint predictor, a fixed-lag smoother, and a collision-aware corrector.

Keypoint Prediction. The estimator takes in images $I_{c} \in {\mathbb{R}}^{C \times H \times W}$ from $n_{c}$ cameras. We first train a vision model $g_{\varphi}$ that predicts 8 fixed keypoints on the cube corresponding to its corners, $p_{\text{kp}} = {g_{\varphi}{(I_{c})}}$. The keypoint prediction task is supervised from a training dataset of 686,000 images of a simulated cube rendered by `Blender`, which includes ground-truth pixel locations for all keypoints, even those that are outside the frame or occluded. We generate randomized background scenes using `kubric`, which spawns the cube along with other random assets in a `pybullet` simulation. Similar datasets are commonly used to train "track-any-point" models which exhibit strong sim-to-real transfer for similar keypoint tracking tasks.

Crucially, we then augment these images with random affine transforms; visual effects like color, shadow, and contrast; and randomized backgrounds. We also found that pruning images where the cube was nearly occluded, or too close for a reliable pose estimate, was essential for good performance. Figure 2 shows some of the resulting images.

To train $g_{\varphi}$, we fine-tuned an ImageNet-pretrained `resnet18` using `AdamW` with an MSE loss. The only model adjustments were the number of input channels (depending on RGB or RGBD inputs) and the dimension of the output layer. For finer details, see \[7, Extended Version\].

Pose Smoothing. We use GTSAM, a factor graph-based state estimation package, to convert keypoints into a cube pose estimate via fixed-lag smoothing. Given a fixed pinhole camera model with known camera poses and cube size, we derive keypoint measurement factors that relate keypoints $p_{\text{kp}}$ to a cube pose $q^{c}$. This allows GTSAM to fuse keypoint predictions from an arbitrary number of cameras in real-time to yield a smoothed cube pose estimate ${\overset{\sim}{q}}^{c}$. See our open-source implementation for exact details.

In both simulation and hardware, we estimate velocities by numerically differentiating position estimates (drawn from the smoother for the cube and joint encoders for the hand) and applying an exponential moving average filter with parameter $\alpha = 0.1$ to compute a smooth velocity estimate $\overset{\sim}{v}$.

Figure 2: Image augmentations. To train the keypoint predictor, we augmented simulated images of the cube with random crops, affine transformations, spliced backgrounds, random deletions, and visual adjustments in color, contrast, brightness, and reflectivity.

Collision-Aware Correction. While the smoother's cube pose estimate ${\overset{\sim}{q}}^{c}$ is usually accurate within 1\\unit, it may not always be physically compatible with the hand configuration ${\overset{\sim}{q}}^{h}$ from the encoders, as the smoother has no knowledge of collision dynamics. Thus, $\overset{\sim}{q} = {\lbrack{\overset{\sim}{q}}^{c},{\overset{\sim}{q}}^{h}\rbrack}$ often corresponds to non-negligible interpenetration between cube and hand, which (i) leads to inaccurate plans that destabilize the closed-loop system, and (ii) decreases the planning rate, as stiff MuJoCo models with high interpenetration are poorly-conditioned, requiring more solver iterations.

To remedy this, we adapt the method of by using a corrector, which maintains an asynchronous internal model with state $\hat{x} = {\lbrack{\hat{q}}^{c},{\hat{q}}^{h},{\hat{v}}^{c},{\hat{v}}^{h}\rbrack}$.

Figure 3: Examples of rotations. CEM can discover many contact-rich plans for cube reorientation. The red arrows show where forces are primarily applied to achieve rotations. (A) The middle finger pushes down on a cube edge while the base of the thumb lifts the opposite corner, rotating the Q face up. (B) The ring finger and base of the index finger push on opposite corners to rotate the T face up. (C) The thumb pulls down on the W face while the base of the ring finger pushes on the opposite corner to rotate the Y face up. (D) The index finger pushes down on the edge of the T face while the ring finger swipes left on the E face to rotate it up. (E) The ring finger first swipes inwards, then the thumb quickly follows to pull the W face up. (F) The thumb and the ring finger pinch and lift the cube, then the index finger pushes on an edge to rotate the Y face up. The cube is calmly lowered onto the palm.

The corrector receives an un-adjusted estimate $\overset{\sim}{x}$ from the smoother and encoders, and computes a "corrective wrench" that is added to as a generalized force. Since the corrector starts in a feasible state, simulating results in a corrected estimate $\hat{x}$ that is always physically feasible, but pulled toward the (possibly infeasible) vision-based estimate $\overset{\sim}{x}$. We also add a constant corrective force in the direction of gravity to counteract any smoother estimates that may unrealistically pull the cube upwards due to high corrector gains $C_{P}$, overwhelming the natural gravitational forces of.

## Experiments

For the remainder of the paper, we thoroughly evaluate the DROP architecture via hardware and simulation experiments designed to answer the following questions: Can DROP perform robust and dynamic cube reorientation in hardware (Sec. IV-B)?

How do different components of DROP contribute to its overall performance and reliability (Sec. IV-C)?

How do modeling and state estimation error affect DROP's performance (Sec. IV-D)?

Overall, we find that DROP can reliably perform cube reorientation in hardware, achieving performance comparable with RL-based methods while exhibiting surprising robustness and dexterity. We emphasize that the goal of our experiments is not to design the best-possible control strategy, but to assess the viability of sampling-based online planning for the cube reorientation task via thorough evaluations of the DROP architecture. Thus, we leave systematic comparisons of DROP with other methods for future work.

### IV-A Hardware Setup and Experimental Details

For all experiments, we perform in-hand rotation of a 3D-printed cube with 7\\unit side lengths and a fixed-base LEAP hand with palm angled downwards at 20^∘^ so that the cube slides off without intervention (see Fig. 1 and 3). We use a 128-thread Ryzen Threadripper Pro 5995wx CPU to plan rollouts in parallel. To capture images, we use three ZED Mini cameras with RGBD channels and perform keypoint estimation on 256x256 center-cropped images at VGA resolution. The estimator runs at about 90\\unit, while the planner frequency fluctuates between 25-50\\unit.

For our trials, we compare three planners: PS and CEM (the two sampling-based methods discussed in Sec. III-A), as well as iLQR, a gradient-based method. PS and CEM use $N = 120$ rollouts while iLQR devotes 120 threads to parallel line search. CEM uses $M = 4$ elite samples. When tuning hyperparameters (such as cost weights), we prioritize robustness at the expense of rotation speed. For all experiments, we used identical costs, code, and hyperparameters for performing simulation rollouts, state estimation, and communicating with hardware. Unlike previous work, we did not observe any significant degradation of our hardware stack (e.g., overheating) during testing.

Num Rots (Sorted) Mean Rot/\unit ↑ Median Rot/\unit ↑ TABLE I: Hardware experiments. (A) Prior works using RL for cube reorientation. Note that performs axis-aligned rotations. Best results are shown. (B) Among online planners, CEM clearly performs the best. All planners use 120 threads, RGBD images, and the cube pose corrector. We note that when ignoring the 80\unit timeout imposed, CEM achieves higher mean and median rotation counts than Dactyl and Dextreme. (C) Hardware ablations show that using depth images slightly improves rotation rate, but using the corrector and as many threads as possible substantially boosts performance.

### IV-B Main Hardware Results

We begin by presenting results of hardware trials using the full stack shown in Fig. 1 and discussed in Sec. III. We study each planner by running 10 trials of the cube reorientation task and analyzing the associated rotation and timing statistics. For examples of interesting rotations, see Fig. 3, and for quantitative results, see Table IB. Following prior work, we report statistics assuming the run ends if 80\\unit have elapsed without reaching a goal. Since this cutoff is arbitrary and we used a fairly conservative cost that slows rotation rate, we also report results for the same runs while ignoring the timeout period, ending only when the cube is dropped. For iLQR and PS, this did not change the results.

CEM greatly outperforms PS and iLQR. While iLQR is unable to achieve any rotations and PS only achieves single-digit rotations in hardware, CEM is able to achieve dozens of rotations. Moreover, the rate that it can rotate the cube is also nearly 50% faster than PS, suggesting that it can discover and/or execute contact-rich plans much more effectively.

CEM discovers nontrivial contact sequences. CEM finds contact-rich plans that leverage contacts with all parts of the hand. Many rotations are only feasible when the hand first partially rotates the cube using an initial contact sequence, then completes the rotation by gaiting the cube to a different set of contacts. For example, in Fig. 3D, the cube is first pushed forward and continually supported by the thumb, allowing the index and ring fingers to then swipe in opposite directions to rotate the cube. Similarly, in Fig. 3F, the thumb and ring finger first pinch and lift the entire cube, which allows the index finger to rotate it about the pinched axis before the cube is safely lowered back onto the palm.

Moreover, many discovered plans exploit contact modes that are traditionally challenging to find, like sliding on edges and corners. To execute these motions, the planner employs intuitive strategies like maximizing torque by levering the cube close to a corner or edge. Lastly, our conservative cost function also induced safeguarding behavior, where fingers preemptively blocked the cube from the palm's edges or carefully supported the cube during risky rotations.

The gradient-based iLQR planner is not viable. Corroborating recent work, we find that the stiff dynamics of the cube reorientation task prevent gradient-based methods from effectively finding good plans most likely due to poor numerical conditioning, causing jerky, erratic behaviors that do not lead to coherent rotation sequences.

DROP performs comparably to RL. While it is challenging to compare our results to prior RL-based methods like Dactyl or Dextreme due to many factors distinguishing each setup, like hand morphology, cube size, physical properties, camera type, or vision model, Table IA/B shows that our simple CEM planner approaches the performance of RL-based rotation policies (outperforming them when ignoring timeouts) with similar dexterity (see Fig. 3).

Figure 4: CEM ablation rotation rates. We use rotation rate as a proxy for planner robustness, as slower rates correspond to “stuck” plans or repeatedly failed moves. Markers are all rotations vs. times for CEM and all ablations. The dashed lines show the mean rotation rates: it is clear that all ablations decrease the rate, which justifies our design of the DROP architecture. The solid lines show individual rotations for each method’s longest streak. The long, flat regions correspond to the planner getting “stuck” in local minima.

### IV-C Hardware Ablations

To understand the impact of key design choices in the DROP architecture, we conducted a series of single-variable ablations with the CEM planner on hardware (Table IC).

Depth improves performance, but only marginally. We compared keypoint detection models trained on RGB versus RGBD images. While RGBD slightly improved rotation rates, it did not significantly outperform RGB, which still achieved 128 rotations, the longest sequence ever observed for DROP. Despite this noisy result, RGB's median rotations (28.5) were still slightly lower than RGBD's (30.5), and overall, the relative rotation rates suggest that depth provides a minor improvement in state estimation accuracy.

The corrector is key for performance. We tested DROP when ablating the corrector, passing raw smoother estimates $\overset{\sim}{q}$ directly to the planner. This significantly reduced performance, with mean rotations decreasing by 33%, median rotations by 60%, and rotation rate by 25%. Without the corrector, the planner often became trapped in local minima and long periods of inactivity (flat regions of rollouts in Fig. 4). This was caused by the exploitation of non-physical forces in rollouts arising from non-physical hand-cube interpenetration, leading to unrealistic predictions.

DROP is sensitive to the number of rollouts. We reduced the number of rollouts from 120 to 60 and elite samples from 4 to 3, resulting in a 20% decrease in mean rotation count and an over 25% reduction in rotation rate. This highlights the importance of variance reduction via sufficiently-high sample quantity in SPC, and suggesting that improving search efficiency could significantly boost performance.

All ablations increased rotation rate variance. This consistent pattern demonstrates that depth measurements, the corrector, and sufficient rollout quantity all contribute significantly to the planner's reliability and consistency, which justifies the design of the DROP architecture.

### IV-D Simulated Robustness Study

Lastly, we study DROP's robustness to model and estimation errors by conducting controlled trials in simulation, letting us isolate the planner from the estimation pipeline. We compared iLQR, PS, and CEM under various corrupted conditions, simulating system physics with a 2\\unit timestep while planner threads utilized a separate physics model with a 10\\unit timestep. Each configuration underwent five trials, ending upon cube drop, 80\\unit timeout, or 150 rotations.

Specifically, we intentionally induce two types of errors that we believe contribute to real-world brittleness: (i) mis-tuning the planners' internal value of the hand $K_{p}$ gains, and (ii) corrupting pose estimates from the simulation with a 0.1\\unit lag and additive noise (simulated using a bounded random walk to mimic asymmetric state estimation error). When corrupting $K_{p}$, we study two cases: multiplying the true value by 1.25x and 1.5x, as the results were enlightening for comparing different planners. We also study the effect of the estimator and $K_{p}$ errors together.

CEM is the most robust planner. Table II shows that CEM is the best planner under all error conditions. For example, while PS achieves a higher mean rotation count under perfect conditions than CEM, when $K_{p}$ is mildly corrupted up to 1.25x, PS immediately achieves fewer mean rotations than CEM while suffering an over 2x decrease in rotation rate. At 1.5x, PS hardly rotates the cube at all, while CEM achieves 32.2 mean rotations, and even with the most aggressive errors, CEM was able to achieve dozens of rotations. CEM's superiority can be attributed to its strategy of recomputing $\pi_{\theta}$ from multiple rollouts, in contrast to PS's single-rollout approach. This strategy appears to be key for robustness, providing a plausible explanation for CEM's markedly better performance in hardware.

Rot/\\unit is a good proxy for robustness. Based on empirical observation, we find that low rotation rates are typically caused by the failure to execute precisely-planned motions or the inability of the planner to escape local minima, resulting in the cube being "stuck," which can be attributed to model or estimation error. CEM's superior speed in these simulations supports our assessments of its robustness on hardware.

Error types have distinct failure modes. While incorrect $K_{p}$ values primarily resulted in timeouts, corrupted estimates typically caused cube drops. This suggests that perfect state estimates allow for safe "caging" even with poor actuation models, but estimation errors during precise maneuvers often cause drops, as the planner underestimates rollout risk.

Mean Rot/\unit ↑ TABLE II: Simulated robustness tests. We intentionally degrade planners to test their robustness by (i) tuning the hand proportional gain Kp too high, and (ii) corrupting the estimator with noise and lag (denoted “Est.”). iLQR failed to achieve any rotations even with perfect information. We observe that PS degrades substantially more than CEM in the presence of model and estimation error, which suggests that CEM may transfer well to hardware.

## Conclusion and Future Directions

This work presents DROP, a minimalist online planning method for in-hand manipulation via sampling-based predictive control that achieves robust cube rotations in hardware. While promising, there are many avenues for future research.

Better planners. While we found that vanilla CEM already achieved impressive results, many more sophisticated algorithms exist, such as CMA-ES, MPPI, etc.

Robustness. DROP often plans "risky" actions, possibly due to differences between real-world and simulated physics. Incorporating domain randomization or risk-sensitivity into search-based planners, like successful RL approaches, remains an open challenge, especially due to the extra computation required to simulate randomized physics online.

Object generality. As in prior RL-based works, we first focus on robustly reorienting a single, simple object. While DROP can easily adapt to new objects in simulation, our current vision pipeline requires retraining for new objects. Recent advancements in general pixel-space tracking and video-based mask propagation suggest more avenues for pose estimation that could generalize our search-based approach without extensive retraining.

Enhanced, data-driven search. As noted in our ablations, finding good plans via search demands many threads; indeed, our work relies on a server-grade CPU, since dynamics simulation is about an order of magnitude slower on GPUs. Thus, improving efficiency is key for better performance. Promising directions include sampling from imitation-learned policies, learning value functions for rollout evaluation, and exploring alternate spline parameterizations or action spaces. Searching for high-level commands for a lower-level RL policy could perhaps yield systems with both the flexibility of search and robustness of RL.

DROP opens many paths for contact-rich manipulation. It is our hope that algorithms like DROP can generalize to more real-world tasks than cube reorientation, unlocking tool use, enhanced human-robot collaboration, and more.
