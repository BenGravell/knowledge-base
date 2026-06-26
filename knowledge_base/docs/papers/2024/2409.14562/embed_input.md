<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DROP: Dexterous Reorientation via Online Planning

Topics include Reinforcement learning, Predictive control, Robotics, Robustness, Real-time systems, Online algorithms, Offline algorithms, Sampling-based methods, Planning, Control, Learning, Sampling, DROP.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Achieving human-like dexterity is a longstanding challenge in robotics, in part due to the complexity of planning and control for contact-rich systems. In reinforcement learning (RL), one popular approach has been to use massively-parallelized, domain-randomized simulations to learn a policy offline over a vast array of contact conditions, allowing robust sim-to-real transfer. Inspired by recent advances in real-time parallel simulation, this work considers instead the viability of online planning methods for contact-rich manipulation by studying the well-known in-hand cube reorientation task. We propose a simple architecture that employs a sampling-based predictive controller and vision-based pose estimator to search for contact-rich control actions online. We conduct thorough experiments to assess the real-world performance of our method, architectural design choices, and key factors for robustness, demonstrating that our simple sampling-based approach achieves performance comparable to prior RL-based works.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Achieving dexterity comparable to human hands has been a longstanding challenge in robotics. While even simple robots can produce dynamic, contact-rich behavior, general methods for doing so are still scarce. For contact-rich tasks, reinforcement learning (RL) has been the dominant paradigm due to its ability to generate real-world robust plans. One well-studied task is in-hand cube reorientation, where a hand must rotate a cube to match consecutive goal orientations. Pioneered by OpenAI and extended by others, RL policies trained with massively-parallelized, domain-randomized simulations have achieved remarkably robust sim-to-real transfer for cube rotation. But, this offline simulation-based approach requires substantial pre-execution computation and is inflexible to changing task specifications.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Leveraging recent advances in real-time parallel simulation (e.g., MJPC), we instead study the online approach of sampling-based predictive control (SPC) methods for in-hand manipulation, which continuously replan by simulating parallel rollouts and applying optimal control actions over short time horizons. In contrast with RL, such online planning methods can adjust the task or model without re-training, but may demand expensive online computation. While tools like MJPC have made SPC feasible for many simulated contact-rich tasks, their real-world utility remains largely unproven.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our main contribution is DROP (Dexterous Reorientation via Online Planning), a system architecture (Fig. 1) that consists of (i) a simple sampling-based planner and (ii) a vision-based state estimator comprising a keypoint detection model, a pose smoother, and a collision-aware state corrector. Our aim is not to design the best cube reorientation policy, but to test the viability of sampling-based strategies by thoroughly assessing DROP's real-world performance, architectural design, and key factors for robustness. Still, DROP is the first online planning method for cube reorientation on hardware, and we find that its performance is comparable with prior RL-based methods. For reproducibility, we provide open-source code, estimator weights, and hardware setup^11^1Project website:..

<!-- chunk {"id": "body-0006", "role": "body", "section": "II-A Related Work", "weight": 1.0} -->

The first viable methods for in-hand cube reorientation employed *reinforcement learning (RL)*, starting with Dactyl, which popularized domain randomization for sim-to-real transfer of RL policies. Subsequent research built on Dactyl with improved domain randomization, tactile-only sensing, and "palm-down" rotations for various objects. While typically limited to specific robots or object classes, RL's robust hardware performance has established it as the standard for in-hand manipulation.

<!-- chunk {"id": "body-0007", "role": "body", "section": "II-A Related Work", "weight": 1.0} -->

Others have explored model-based approaches to contact-rich manipulation via *contact-implicit trajectory optimization* (CITO). Originally used in locomotion, recent work shows that such planners can generate motions for simple contact-rich tasks like bimanual lifting or real-time planar rolling and sliding. Other approaches have combined CITO with learned signed distance fields, global search, or smoothed dynamics.

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-A Related Work", "weight": 1.0} -->

*Sampling-based planning* has a long history in manipulation, starting with methods like RRT, PRM, and STOMP. Recent advances in SPC have enabled simple contact-rich manipulation like pushing, sliding, and pick and place, while new tools for real-time parallel simulation of contact-rich tasks, have made SPC viable for simulated contact-rich tasks with remarkably simple controllers. Still, little evidence exists for the viability of SPC for real-world contact-rich manipulation (concurrently, some works have studied it for locomotion ), and overall, model-based methods (like SPC or CITO) have seldom studied tasks as hard as cube reorientation, which exhibits many simultaneous unpredictable contact modes.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Related Work", "weight": 1.0} -->

Lastly, high-quality *object tracking* is key for most of these methods, especially model-based online search. RL approaches usually use single-object pose estimation networks, but recent computer vision advances suggest that more general tracking pipelines like frame-to-frame point trackers and foundation models for rigid body pose prediction may boost performance.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-B Mathematical Notation", "weight": 1.0} -->

We model the continuous-time cube-in-hand dynamics as where $x$ is the state and $u$ are control inputs. We do not assume access to a closed-form expression for $f$, but instead to a simulator (MuJoCo) that generates state trajectories $x{(t)}$ given an initial state $x_{0}$ and a control sequence $u{(t)}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-B Mathematical Notation", "weight": 1.0} -->

The state $x$ consists of the generalized positions and velocities of both the cube ($q^{c},v^{c}$) and hand ($q^{h},v^{h}$): In this work, the control actions $u$ are position setpoints for the hand, which are tracked by a lower-level PD controller internal to the model $f$. Following, we represent a control trajectory $u{(t)}$ on $t \in {\lbrack 0,T\rbrack}$ with $K$ spline knots, which constitute the decision variables for online planning. The control objective is encoded by a cost functional where querying $J{(U;x_{0})}$ requires simulating $f$ using an open-loop control signal $u{(t)}$ from initial condition $x_{0}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Mathematical Notation", "weight": 1.0} -->

Throughout the paper, we use the following notation to denote "subtraction" of two quaternions ${a,b} \in {\mathbb{H}}$: and similarly, when ${a,b} \in {SE{}}$, ${a \ominus b} \in {{\mathfrak{s}}{\mathfrak{e}}{}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "The DROP Algorithm", "weight": 1.0} -->

DROP consists of (i) a sampling-based planner and (ii) a keypoint-based cube pose estimator (see Fig. 1). The planner continually updates the control spline $U$ via SPC. We use MJPC to handle both parallel rollouts and policy updates.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Sampling-Based Planning and Control", "weight": 1.0} -->

Algorithm 1 describes a generic SPC procedure. At time $t \in {\mathbb{R}}$, the planner receives a state estimate $\hat{x}{(t)}$ and rolls out a batch of $N$ open-loop control sequences $U^{(i)}$ drawn from some parametric distribution $\pi_{\theta}(U)$. Each control trajectory is simulated (in parallel) to obtain a cost $J^{(i)}$, and all costs are jointly used to update the sampling parameters $\theta$. The control input $u{(t)}$ can be obtained for any time $t$ from the spline parameters $U$. This allows planning to proceed asynchronously, with the parameters $\theta$ updated as quickly as computational limits allow.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Sampling-Based Planning and Control", "weight": 1.0} -->

Input: θ, N, planner-specific parameters. // estimate curr state Algorithm 1 Sampling-based Predictive Control In our experiments, we test two simple planning strategies that both use a diagonal Gaussian distribution ${\pi_{\theta}(U)} = {\mathcal{N}\left({\Delta 111U},\Sigma \right)}$ with parameters $\theta = \left({\Delta 111U},\Sigma \right)$. In Algorithm 1, ${\mathtt{g}\mathtt{e}\mathtt{t}}_{\mathtt{a}\mathtt{c}\mathtt{t}\mathtt{i}\mathtt{o}\mathtt{n}}{(\theta,t)}$ is a spline interpolation with knots ${}\Delta{}{}{}{}111U$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Sampling-Based Planning and Control", "weight": 1.0} -->

Predictive sampling (PS) repeatedly updates ${}\Delta{}{}{}{}111U$ to be the best sample, fixing $\Sigma = {\sigma^{2}I}$. Despite its simplicity, PS has demonstrated surprisingly effective performance on complex robot manipulation and locomotion tasks in simulation.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Sampling-Based Planning and Control", "weight": 1.0} -->

The cross-entropy method (CEM) instead fits both ${}\Delta{}{}{}{}111U$ and $\Sigma = {\operatorname{diag}{(s)}}$ to the sample mean and variance of the $M$ best elite samples, where $s$ is a vector of covariances. CEM is only marginally more complex than PS, but has long been used for general gradient-free optimization.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Sampling-Based Planning and Control", "weight": 1.0} -->

As in prior work, the task considered in this paper is to use a dexterous hand to rotate a cube to within 0.4 \\unit of as many goal orientations in a row as possible without dropping. The goals are uniformly randomly sampled over $SO{}$. In contrast, to ensure sufficient task difficulty, each new goal must be at least $90^{\circ}$ from the prior one.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Sampling-Based Planning and Control", "weight": 1.0} -->

Mathematically, the DROP cube reorientation problem is expressed as the optimal control problem where $\lambda_{(\cdot)}$ denote weights, the dynamics $f{(x,u)}$ are only available through simulation, and are running costs. The variables $p^{c}$ and $r^{c}$ denote the positional and rotational components of the cube pose $q^{c} = \left\lbrack p^{c},r^{c} \right\rbrack$, which are extracted from the simulated state $x{(t)}$. $\ell_{\text{g}}$ penalizes rotational distance from the goal, while $\ell_{\text{p}}$ penalizes the cube leaving a "safe" region $\mathcal{S}$ in Cartesian space.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Sampling-Based Planning and Control", "weight": 1.0} -->

In this work, we prioritize drop reduction by setting $\lambda_{\text{p}}$ high and choosing a conservative region $\mathcal{S}$ (for details, see ). In practice, we use a relatively low $\lambda_{\text{g}}$, which slows down the planner but also amplifies differences in rotation rate across methods, allowing easier quantitative comparison.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B The Pose Estimation Pipeline", "weight": 1.0} -->

Our pose estimator consists of three parts: a keypoint predictor, a fixed-lag smoother, and a collision-aware corrector.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B The Pose Estimation Pipeline", "weight": 1.0} -->

Keypoint Prediction. The estimator takes in images $I_{c} \in {\mathbb{R}}^{C \times H \times W}$ from $n_{c}$ cameras. We first train a vision model $g_{\varphi}$ that predicts 8 fixed keypoints on the cube corresponding to its corners, $p_{\text{kp}} = {g_{\varphi}{(I_{c})}}$. The keypoint prediction task is supervised from a training dataset of 686,000 images of a simulated cube rendered by `Blender`, which includes ground-truth pixel locations for all keypoints, even those that are outside the frame or occluded. We generate randomized background scenes using `kubric`, which spawns the cube along with other random assets in a `pybullet` simulation. Similar datasets are commonly used to train "track-any-point" models which exhibit strong sim-to-real transfer for similar keypoint tracking tasks.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B The Pose Estimation Pipeline", "weight": 1.0} -->

Crucially, we then augment these images with random affine transforms; visual effects like color, shadow, and contrast; and randomized backgrounds. We also found that pruning images where the cube was nearly occluded, or too close for a reliable pose estimate, was essential for good performance. Figure 2 shows some of the resulting images.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B The Pose Estimation Pipeline", "weight": 1.0} -->

To train $g_{\varphi}$, we fine-tuned an ImageNet-pretrained `resnet18` using `AdamW` with an MSE loss. The only model adjustments were the number of input channels (depending on RGB or RGBD inputs) and the dimension of the output layer. For finer details, see \[7, Extended Version\].

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B The Pose Estimation Pipeline", "weight": 1.0} -->

Pose Smoothing. We use GTSAM, a factor graph-based state estimation package, to convert keypoints into a cube pose estimate via fixed-lag smoothing. Given a fixed pinhole camera model with known camera poses and cube size, we derive keypoint measurement factors that relate keypoints $p_{\text{kp}}$ to a cube pose $q^{c}$. This allows GTSAM to fuse keypoint predictions from an arbitrary number of cameras in real-time to yield a smoothed cube pose estimate ${\overset{\sim}{q}}^{c}$. See our open-source implementation for exact details.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B The Pose Estimation Pipeline", "weight": 1.0} -->

In both simulation and hardware, we estimate velocities by numerically differentiating position estimates (drawn from the smoother for the cube and joint encoders for the hand) and applying an exponential moving average filter with parameter $\alpha = 0.1$ to compute a smooth velocity estimate $\overset{\sim}{v}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B The Pose Estimation Pipeline", "weight": 1.0} -->

Collision-Aware Correction. While the smoother's cube pose estimate ${\overset{\sim}{q}}^{c}$ is usually accurate within 1\\unit, it may not always be physically compatible with the hand configuration ${\overset{\sim}{q}}^{h}$ from the encoders, as the smoother has no knowledge of collision dynamics. Thus, $\overset{\sim}{q} = {\lbrack{\overset{\sim}{q}}^{c},{\overset{\sim}{q}}^{h}\rbrack}$ often corresponds to non-negligible interpenetration between cube and hand, which (i) leads to inaccurate plans that destabilize the closed-loop system, and (ii) decreases the planning rate, as stiff MuJoCo models with high interpenetration are poorly-conditioned, requiring more solver iterations.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B The Pose Estimation Pipeline", "weight": 1.0} -->

The corrector receives an un-adjusted estimate $\overset{\sim}{x}$ from the smoother and encoders, and computes a "corrective wrench" that is added to as a generalized force. Since the corrector starts in a feasible state, simulating results in a corrected estimate $\hat{x}$ that is always physically feasible, but pulled toward the (possibly infeasible) vision-based estimate $\overset{\sim}{x}$. We also add a constant corrective force in the direction of gravity to counteract any smoother estimates that may unrealistically pull the cube upwards due to high corrector gains $C_{P}$, overwhelming the natural gravitational forces of.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

For the remainder of the paper, we thoroughly evaluate the DROP architecture via hardware and simulation experiments designed to answer the following questions: Can DROP perform robust and dynamic cube reorientation in hardware (Sec. IV-B)?

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

How do different components of DROP contribute to its overall performance and reliability (Sec. IV-C)?

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

How do modeling and state estimation error affect DROP's performance (Sec. IV-D)?

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

Overall, we find that DROP can reliably perform cube reorientation in hardware, achieving performance comparable with RL-based methods while exhibiting surprising robustness and dexterity. We emphasize that the goal of our experiments is not to design the best-possible control strategy, but to assess the viability of sampling-based online planning for the cube reorientation task via thorough evaluations of the DROP architecture. Thus, we leave systematic comparisons of DROP with other methods for future work.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Hardware Setup and Experimental Details", "weight": 1.0} -->

For all experiments, we perform in-hand rotation of a 3D-printed cube with 7\\unit side lengths and a fixed-base LEAP hand with palm angled downwards at 20^∘^ so that the cube slides off without intervention (see Fig. 1 and 3). We use a 128-thread Ryzen Threadripper Pro 5995wx CPU to plan rollouts in parallel. To capture images, we use three ZED Mini cameras with RGBD channels and perform keypoint estimation on 256x256 center-cropped images at VGA resolution. The estimator runs at about 90\\unit, while the planner frequency fluctuates between 25-50\\unit.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Hardware Setup and Experimental Details", "weight": 1.0} -->

For our trials, we compare three planners: PS and CEM (the two sampling-based methods discussed in Sec. III-A), as well as iLQR, a gradient-based method. PS and CEM use $N = 120$ rollouts while iLQR devotes 120 threads to parallel line search. CEM uses $M = 4$ elite samples. When tuning hyperparameters (such as cost weights), we prioritize robustness at the expense of rotation speed. For all experiments, we used identical costs, code, and hyperparameters for performing simulation rollouts, state estimation, and communicating with hardware. Unlike previous work, we did not observe any significant degradation of our hardware stack (e.g., overheating) during testing.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Hardware Setup and Experimental Details", "weight": 1.0} -->

Num Rots (Sorted) Mean Rot/\unit ↑ Median Rot/\unit ↑ TABLE I: Hardware experiments. (A) Prior works using RL for cube reorientation. Note that performs axis-aligned rotations. Best results are shown. (B) Among online planners, CEM clearly performs the best. All planners use 120 threads, RGBD images, and the cube pose corrector. We note that when ignoring the 80\unit timeout imposed, CEM achieves higher mean and median rotation counts than Dactyl and Dextreme. (C) Hardware ablations show that using depth images slightly improves rotation rate, but using the corrector and as many threads as possible substantially boosts performance.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Main Hardware Results", "weight": 1.0} -->

We begin by presenting results of hardware trials using the full stack shown in Fig. 1 and discussed in Sec. III. We study each planner by running 10 trials of the cube reorientation task and analyzing the associated rotation and timing statistics. For examples of interesting rotations, see Fig. 3, and for quantitative results, see Table IB. Following prior work, we report statistics assuming the run ends if 80\\unit have elapsed without reaching a goal. Since this cutoff is arbitrary and we used a fairly conservative cost that slows rotation rate, we also report results for the same runs while ignoring the timeout period, ending only when the cube is dropped. For iLQR and PS, this did not change the results.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Main Hardware Results", "weight": 1.0} -->

CEM greatly outperforms PS and iLQR. While iLQR is unable to achieve any rotations and PS only achieves single-digit rotations in hardware, CEM is able to achieve dozens of rotations. Moreover, the rate that it can rotate the cube is also nearly 50% faster than PS, suggesting that it can discover and/or execute contact-rich plans much more effectively.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B Main Hardware Results", "weight": 1.0} -->

CEM discovers nontrivial contact sequences. CEM finds contact-rich plans that leverage contacts with all parts of the hand. Many rotations are only feasible when the hand first partially rotates the cube using an initial contact sequence, then completes the rotation by gaiting the cube to a different set of contacts. For example, in Fig. 3D, the cube is first pushed forward and continually supported by the thumb, allowing the index and ring fingers to then swipe in opposite directions to rotate the cube. Similarly, in Fig. 3F, the thumb and ring finger first pinch and lift the entire cube, which allows the index finger to rotate it about the pinched axis before the cube is safely lowered back onto the palm.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Main Hardware Results", "weight": 1.0} -->

Moreover, many discovered plans exploit contact modes that are traditionally challenging to find, like sliding on edges and corners. To execute these motions, the planner employs intuitive strategies like maximizing torque by levering the cube close to a corner or edge. Lastly, our conservative cost function also induced safeguarding behavior, where fingers preemptively blocked the cube from the palm's edges or carefully supported the cube during risky rotations.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Main Hardware Results", "weight": 1.0} -->

The gradient-based iLQR planner is not viable. Corroborating recent work, we find that the stiff dynamics of the cube reorientation task prevent gradient-based methods from effectively finding good plans most likely due to poor numerical conditioning, causing jerky, erratic behaviors that do not lead to coherent rotation sequences.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Main Hardware Results", "weight": 1.0} -->

DROP performs comparably to RL. While it is challenging to compare our results to prior RL-based methods like Dactyl or Dextreme due to many factors distinguishing each setup, like hand morphology, cube size, physical properties, camera type, or vision model, Table IA/B shows that our simple CEM planner approaches the performance of RL-based rotation policies (outperforming them when ignoring timeouts) with similar dexterity (see Fig. 3).

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-C Hardware Ablations", "weight": 1.0} -->

To understand the impact of key design choices in the DROP architecture, we conducted a series of single-variable ablations with the CEM planner on hardware (Table IC).

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-C Hardware Ablations", "weight": 1.0} -->

Depth improves performance, but only marginally. We compared keypoint detection models trained on RGB versus RGBD images. While RGBD slightly improved rotation rates, it did not significantly outperform RGB, which still achieved 128 rotations, the longest sequence ever observed for DROP. Despite this noisy result, RGB's median rotations (28.5) were still slightly lower than RGBD's (30.5), and overall, the relative rotation rates suggest that depth provides a minor improvement in state estimation accuracy.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C Hardware Ablations", "weight": 1.0} -->

The corrector is key for performance. We tested DROP when ablating the corrector, passing raw smoother estimates $\overset{\sim}{q}$ directly to the planner. This significantly reduced performance, with mean rotations decreasing by 33%, median rotations by 60%, and rotation rate by 25%. Without the corrector, the planner often became trapped in local minima and long periods of inactivity (flat regions of rollouts in Fig. 4). This was caused by the exploitation of non-physical forces in rollouts arising from non-physical hand-cube interpenetration, leading to unrealistic predictions.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C Hardware Ablations", "weight": 1.0} -->

DROP is sensitive to the number of rollouts. We reduced the number of rollouts from 120 to 60 and elite samples from 4 to 3, resulting in a 20% decrease in mean rotation count and an over 25% reduction in rotation rate. This highlights the importance of variance reduction via sufficiently-high sample quantity in SPC, and suggesting that improving search efficiency could significantly boost performance.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-C Hardware Ablations", "weight": 1.0} -->

All ablations increased rotation rate variance. This consistent pattern demonstrates that depth measurements, the corrector, and sufficient rollout quantity all contribute significantly to the planner's reliability and consistency, which justifies the design of the DROP architecture.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-D Simulated Robustness Study", "weight": 1.0} -->

Lastly, we study DROP's robustness to model and estimation errors by conducting controlled trials in simulation, letting us isolate the planner from the estimation pipeline. We compared iLQR, PS, and CEM under various corrupted conditions, simulating system physics with a 2\\unit timestep while planner threads utilized a separate physics model with a 10\\unit timestep. Each configuration underwent five trials, ending upon cube drop, 80\\unit timeout, or 150 rotations.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-D Simulated Robustness Study", "weight": 1.0} -->

Specifically, we intentionally induce two types of errors that we believe contribute to real-world brittleness: (i) mis-tuning the planners' internal value of the hand $K_{p}$ gains, and (ii) corrupting pose estimates from the simulation with a 0.1\\unit lag and additive noise (simulated using a bounded random walk to mimic asymmetric state estimation error). When corrupting $K_{p}$, we study two cases: multiplying the true value by 1.25x and 1.5x, as the results were enlightening for comparing different planners. We also study the effect of the estimator and $K_{p}$ errors together.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-D Simulated Robustness Study", "weight": 1.0} -->

CEM is the most robust planner. Table II shows that CEM is the best planner under all error conditions. For example, while PS achieves a higher mean rotation count under perfect conditions than CEM, when $K_{p}$ is mildly corrupted up to 1.25x, PS immediately achieves fewer mean rotations than CEM while suffering an over 2x decrease in rotation rate. At 1.5x, PS hardly rotates the cube at all, while CEM achieves 32.2 mean rotations, and even with the most aggressive errors, CEM was able to achieve dozens of rotations. CEM's superiority can be attributed to its strategy of recomputing $\pi_{\theta}$ from multiple rollouts, in contrast to PS's single-rollout approach. This strategy appears to be key for robustness, providing a plausible explanation for CEM's markedly better performance in hardware.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-D Simulated Robustness Study", "weight": 1.0} -->

Rot/\\unit is a good proxy for robustness. Based on empirical observation, we find that low rotation rates are typically caused by the failure to execute precisely-planned motions or the inability of the planner to escape local minima, resulting in the cube being "stuck," which can be attributed to model or estimation error. CEM's superior speed in these simulations supports our assessments of its robustness on hardware.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-D Simulated Robustness Study", "weight": 1.0} -->

Error types have distinct failure modes. While incorrect $K_{p}$ values primarily resulted in timeouts, corrupted estimates typically caused cube drops. This suggests that perfect state estimates allow for safe "caging" even with poor actuation models, but estimation errors during precise maneuvers often cause drops, as the planner underestimates rollout risk.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-D Simulated Robustness Study", "weight": 1.0} -->

Mean Rot/\unit ↑ TABLE II: Simulated robustness tests. We intentionally degrade planners to test their robustness by (i) tuning the hand proportional gain Kp too high, and (ii) corrupting the estimator with noise and lag (denoted “Est.”). iLQR failed to achieve any rotations even with perfect information. We observe that PS degrades substantially more than CEM in the presence of model and estimation error, which suggests that CEM may transfer well to hardware.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

This work presents DROP, a minimalist online planning method for in-hand manipulation via sampling-based predictive control that achieves robust cube rotations in hardware. While promising, there are many avenues for future research.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

Better planners. While we found that vanilla CEM already achieved impressive results, many more sophisticated algorithms exist, such as CMA-ES, MPPI, etc.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

Robustness. DROP often plans "risky" actions, possibly due to differences between real-world and simulated physics. Incorporating domain randomization or risk-sensitivity into search-based planners, like successful RL approaches, remains an open challenge, especially due to the extra computation required to simulate randomized physics online.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

Object generality. As in prior RL-based works, we first focus on robustly reorienting a single, simple object. While DROP can easily adapt to new objects in simulation, our current vision pipeline requires retraining for new objects. Recent advancements in general pixel-space tracking and video-based mask propagation suggest more avenues for pose estimation that could generalize our search-based approach without extensive retraining.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

Enhanced, data-driven search. As noted in our ablations, finding good plans via search demands many threads; indeed, our work relies on a server-grade CPU, since dynamics simulation is about an order of magnitude slower on GPUs. Thus, improving efficiency is key for better performance. Promising directions include sampling from imitation-learned policies, learning value functions for rollout evaluation, and exploring alternate spline parameterizations or action spaces. Searching for high-level commands for a lower-level RL policy could perhaps yield systems with both the flexibility of search and robustness of RL.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion and Future Directions", "weight": 1.5} -->

DROP opens many paths for contact-rich manipulation. It is our hope that algorithms like DROP can generalize to more real-world tasks than cube reorientation, unlocking tool use, enhanced human-robot collaboration, and more.
