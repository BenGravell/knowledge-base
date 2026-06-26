<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

How Are Learned Perception-Based Controllers Impacted by the Limits of Robust Control?

Topics include Reinforcement learning, Optimal control, Robustness, System identification, Sample complexity, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The difficulty of optimal control problems has classically been characterized in terms of system properties such as minimum eigenvalues of controllability/observability gramians. We revisit these characterizations in the context of the increasing popularity of data-driven techniques like reinforcement learning (RL), and in control settings where input observations are high-dimensional images and transition dynamics are unknown. Specifically, we ask: to what extent are quantifiable control and perceptual difficulty metrics of a task predictive of the performance and sample complexity of data-driven controllers? We modulate two different types of partial observability in a cartpole "stick-balancing" problem - (i) the height of one visible fixation point on the cartpole, which can be used to tune fundamental limits of performance achievable by any controller, and by (ii) the level of perception noise in the fixation point position inferred from depth or RGB images of the cartpole. In these settings, we empirically study two popular families of controllers: RL and system identification-based H_infinity control, using visually estimated system state.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our results show that the fundamental limits of robust control have corresponding implications for the sample-efficiency and performance of learned perception-based controllers. Visit our project website for more information.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Data-driven techniques for robotic control such as deep reinforcement learning have recently become increasingly popular, especially for settings where input observations are high-dimensional, such as images, and state transition dynamics are not known in advance. These techniques have shown great promise for controlling a variety of robots ranging from manipulators to legged robots, drones, and autonomous cars. However, these techniques have largely been studied and developed within the confines of stylized, often simulated settings, where performance metrics are naturally divorced from important real-world concerns such as safety and robustness. In the light of recent catastrophic failures of learning-based control systems such as fatal autonomous car collisions, we argue that it is imperative to study and characterize the limitations of these approaches in challenging settings that present realistic difficulties for observation and control. In particular, how do such difficulties affect the performance and sample complexity of learned controllers?

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Classical robust control theory provides a rich set of tools characterizing fundamental limits on achievable performance in terms of system properties such as open-loop unstable poles and zeros. However, analogous theoretical results in the learning-based control literature are not nearly as well developed, especially in the context of controllers that involve high-capacity functional approximators such as deep reinforcement learning from pixels. Rather than seeking theoretical limits, we try a different tack, empirically studying various families of learned controllers in a setting where control and observation difficulty can be carefully tuned.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our empirical study focuses on the visuomotor control task of stabilizing a cartpole in the upright position using only the visual observations from a camera with a head-on view. All visuomotor controllers must implicitly or explicitly solve two important and closely intertwined problems. The first is visual perception, i.e., how to map raw high-dimensional visual observations o to their taskrelevant latent causes, denoted as the state representation x ? The second is the task of synthesizing optimal action policies π ( u | x ) conditioned on those state estimates.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In real-world settings, perception is often an underconstrained problem. For example, an autonomous car with on-board cameras cannot see around the corner of a street on a left turn, or a pedestrian occluded behind a parked vehicle, or a pedestrian with dark clothes on a poorly lit street. In all such instances, the observations o are a non-invertible function of the relevant state x, and the estimated states ˆ x output from perception cannot match the state x perfectly, even with the most optimal perception system. This imperfect perception problem may be represented formally as a partially observable Markov decision process (POMDP). The successes of reinforcement learning in the last few years have been largely demonstrated on fully observed tasks, and general methods for tackling POMDPs remain elusive. Even when they are evaluated on real-world robotic systems, robots and environments are typically instrumented to ensure near-complete observability of all relevant state information, which is impractical for in-the-wild applications like autonomous driving.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our visual cartpole balancing task permits the modulation of two realistic sources of partial observability within the context of a well-studied classical control problem. First, a set fraction of the cartpole's length is constantly occluded from the camera. As we will explain, this type of information loss has been shown to induce fundamental limits on the performance of any controller for this system. Second, the sensing abilities of the camera itself may also limit perception. For example, to estimate the distance from the camera of an object in the scene such as the cartpole, a perception system with access to RGB camera observations would be harder to train, and it would produce more noisy estimates than one receiving inputs from a stereo depth camera.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We study the impact of tuning these sources of perception noise on the performance of two families of learned controllers: system identification-based H ∞ control and reinforcement learning, both using visually estimated system state. Our careful empirical studies clearly show that increasing occlusion and deteriorating sensing quality affect both families of controllers in ways that align well with theoretically predicted limits for classical robust controllers. In particular, sample complexity increases and final task performance decreases, and the effect of sensing noise is exacerbated as more of the cartpole is occluded from view.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we investigate the performance of data-driven techniques for learning controllers on a customized cartpole balancing environment in PyBullet, which allows for varying fixation lengths ℓ 0, observation quality, and injecting camera sensing noise. We study two techniques under different measurement models based on learned perception modules: a modelfree RL algorithm and a system identification-based robust H ∞ control algorithm. We simulate and vary the fixation point variable discussed above, as well as measurement models and camera sensing noise, in order to tune them to observe their effects on controller performance. Our experiments aim to demonstrate that the performance of learned perception-based controllers is subject to the fundamental limits on achievable performance specified by Theorem 2, and answer: What effect does incomplete sensing (as measured by fixation length and the corresponding bounds of Theorem 2) and noisy sensing (as measured by the magnitude of simulated camera sensing noise) have on the sample complexity of learning perception-based controllers?

<!-- chunk {"id": "body-0011", "role": "body", "section": "Environment", "weight": 1.0} -->

We developed a custom 'stick-balancing' environment in PyBullet, illustrated in Fig. 2. A cartpole system is actuated by moving the cart along a sliding track (in cyan) along the x -axis of the world frame. The mass of the cart M = 1kg, the mass of the pole m = 0. 1kg, and the length of the pole l = 1m.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Environment", "weight": 1.0} -->

The camera has a head-on view of the cartpole, as depicted in Fig 2(Right, a). To simulate varying fixation points, we occlude a fixed fraction of the pole starting from its top, by setting it to be invisible in PyBullet. This is depicted in black in the simulator view in Fig 2(a). In our experiments, the controller's observations are either direct depth measurements of the fixation point (labeled z in Fig. 2), depth images (Fig 2(b)), or RGB images (Fig 2(c)). We simulate the parameters of an Intel RealSense D415 camera 1, and downsample and crop images to 120 × 100 pixels in all our experiments.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Environment", "weight": 1.0} -->

At the beginning of every episode of training and testing, the configuration variables ( x, ˙ x, θ, ˙ θ ) of the cartpole are all initialized randomly from a uniform distribution over [ -0. 05, 0. 05] (respectively m, m / s, rad and rad / s for the four variables). This environment is simulated at 50Hz (each time step equals 0.02 s ) for 500 steps (10 s ) in an OpenAI Gym framework. The episode terminates and resets after 500 steps, or when x goes outside [ -0. 6m, 0. 6m] or θ goes outside [ -15 ◦, 15 ◦ ].

<!-- chunk {"id": "body-0014", "role": "body", "section": "Methods", "weight": 1.0} -->

Learning Perception Models. When dealing with images from the camera as input, the role of the perception system is to 'invert' the observations into an estimate of the depth z of the fixation point, as depicted in Fig 3. Input images are either depth images or RGB images to allow us to tune partial observability from sensing limitations: we expect that depth images will enable more reliable estimates of z than RGB images.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Methods", "weight": 1.0} -->

Fig. 3: Perception-based feedback control diagram.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Methods", "weight": 1.0} -->

For each value of the fixation point, and each of depth / RGB images, we train a convolutional neural network (see Appendix G for architecture details) to minimize a mean squared error regression loss on target z labels, using stochastic gradient descent with the Adam optimizer. Our training set contains 40K images with associated z labels, collected by uniformly sampling x and θ from the allowable range. Each model is trained up to 1K epochs with early stopping.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Methods", "weight": 1.0} -->

As expected, the error in perceiving z from camera images is significantly higher with RGB cameras than with depth cameras. Specifically, the normalized root mean squared errors (RMSE) for estimating the fixation point depth z, normalized by the range of z, are 0.03% and 0.25% for depth and RGB respectively, consistent across different fixation lengths.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Methods", "weight": 1.0} -->

Robust Control with System Identification. Here we take a classical system identification and robust control approach which consists of first fitting a model to data collected from the system, and then synthesizing an H ∞ controller.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Methods", "weight": 1.0} -->

System Identification: We first randomly generate system trajectories starting from initial state satisfying ‖ x ‖ ∞ ≤. 05, and record the resulting depth measurement outputs. We excite the system with control inputs drawn as u (t) iid ∼ U until the horizontal position of the cart deviates by more than 0. 6 m from its initial position, or the pole deviates more than 15 ◦ from the vertical. This data-collection step is repeated for differing numbers of trajectories, for fixation values of ℓ 0 = 1. 0, 0. 9, 0. 8, 0. 7, and for outputs consisting of true depth measurements, depth estimates produced by a perceptionmap acting on depth images, and depth estimates produced from a perception-map acting on RGB images. We Fig. 4: The H ∞ controller K minimizes the worst case H ∞ norm of the closed loop system over all uncertainties || ∆ || ∞ < 1. also record the full system state, as this will be used to identify a 'baseline' system model for comparison.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Methods", "weight": 1.0} -->

The result is a collection of input/output trajectories { z (i) (0: T i), u (i) (0: T i) } N i =1 to be used by a system identification algorithm.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Methods", "weight": 1.0} -->

We fit a strictly causal linear time invariant model with parameters (ˆ A, ˆ B, ˆ C) from the collected trajectories { z (i) (0: T i), u (i) (0: T i) } N i =1. We apply two system identification methods to the collected data: (i) N4SID, and (ii) a standard two step procedure we refer to as ARXHK. This latter approach consists of first fitting an auto-regressive model ˆ G of order p by solving the least squares problem and then applying the Ho-Kalman algorithm to obtain state-space parameters (ˆ A, ˆ B, ˆ C). We refer to this latter approach as ARXHK. Exploiting our prior knowledge of the underlying physics of the system, we set the state-dimension (dimension of ˆ A) to n = 4. We set the auto-regressive order p = 10 for ARXHK.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Methods", "weight": 1.0} -->

For the collected data consisting of full state, we fit the state transition matrices (ˆ A, ˆ B) by solving a least-squares problem Robust Control Synthesis: Once parameters (ˆ A, ˆ B, ˆ C) are identified, we use tools from robust control to synthesize a controller that can mitigate the effects of uncertainty in the learned model. and setting C = [1, 0, ℓ 0, 0] such that z = h + ℓ 0 θ. For further details, see Appendix B.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Methods", "weight": 1.0} -->

These uncertainties are caused by noise in the measurements and by approximating nonlinear dynamics with a linear time invariant model. To find our controller, we first introduce unstructured uncertainty in feedback with the learned model, as shown in Fig. 4. We then synthesize an H ∞ controller by drawing on tools from structured singular value, or µ, synthesis (see Appendix C for more details). The parameter ε in Fig. 4, which penalizes control effort, is chosen by cross-validation to achieve a suitably high-performing but robust controller. Once a value of ε has been found to work at the fixation point of 1. 00 for a perception map it is kept fixed throughout the remaining experiments with the perception map.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Methods", "weight": 1.0} -->

Reinforcement Learning from Estimated State. Weuse Soft Actor-Critic for training our RL agents. SAC is a widely used state-of-the-art model-free RL algorithm that has been demonstrated to work well in continuous control settings. The state of the RL agent is the sequence of estimates of the fixation depth value z from the past H steps. At each time step, a new z estimate output by the perception model is appended to the history buffer and the oldest one is abandoned. We set history size H = 200 based on validation performance. The reward is structured as a survival reward: the agent earns a unit reward for every timestep survived in the environment without episode termination. Since the maximum length of an episode is T = 500, the maximum achievable reward is 500. Each agent is trained up to 10K episodes with early stopping. We report results based on 100 trials. See Appendix F for implementation details.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Methods", "weight": 1.0} -->

Performance Metrics. At each fixation depth, for each type of sensor (noise-free observations of the true z, depth image observations, RGB image observations), and for each family of learned controller, we report the average reward earned per episode (same as the survival time), over 100 episodes, and also the success rate, which is the fraction of episodes in which the agent survived successfully up to T = 500.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Results", "weight": 1.0} -->

Fig. 5 shows the performance of RL and H ∞ controllers as the fixation height and observation quality are varied. Each RL controller is trained for a maximum of 10K episodes with early convergence, and each H ∞ controller is trained with up to 20K data points used for system identification.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Results", "weight": 1.0} -->

Fig. 5 presents two main trends. First, performance uniformly deteriorates as the fixation height decreases and more of the pole is occluded from view. This is true for both RL and H ∞ controllers, and at all observation qualities. Next, not only does the performance uniformly worsen as the observation quality deteriorates (from noise-free to depth images to RGB images), but the impact of poorer observation Fig. 5: The average reward is plotted for both RL and H ∞ learned perception-based controllers, as a function of fixation height and observation quality. The data is available in Tab. 2 in Appendix D. quality is higher at low fixation heights, as can be seen by comparing fixations of 1.0 and 0.8 in the plot. Both these experimental findings are closely aligned with the robustness limitations predicted by Theorem 2, which predicts that sensing noise (which is larger when observation quality is poorer) will be amplified more (as measured by ‖ T (ζ) ‖ ∞) at lower fixation points ℓ 0. This suggests that incomplete and noisy sensing act synergistically to further compound the difficulty of the control task when they co-occur.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Results", "weight": 1.0} -->

Fig. 6: Mean and standard deviation of running episode reward from five runs. Plus / minus one standard deviation is shaded. As the fixation length ℓ 0 decreases from 1. 0 through 0. 7 and the quality of perception deteriorates from noise-free true fixation point depth to depth images to RGB images, the reinforcement learning agent finds it harder to stabilize the cartpole. It takes longer to train, and also achieves lower eventual reward at convergence. Furthermore, the effect of perception noise is higher at lower fixation lengths. There is less variance in the rewards as the perception noise increases. We conjecture that the small perception noise introduced is acting as a regularizer for training.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Results", "weight": 1.0} -->

Overall, Fig. 5 establishes that fixation height and observation quality are very effective at modulating the achievable performance levels for both families of learned controllers. Next, we ask: do these factors also predict the learning speeds for these controllers? Fig. 6 shows the training plots (running average of rewards vs. the number of training episodes) for the RL agent in each setting. The agent takes longer to learn at lower Tab. 1: Maximum initial angle stabilized by a controller synthesized using a model fit to full states from 100 trajectories and tested on the three observation scenarios (left) a model fit to true depth measurements from 100 trajectories using the N4SID algorithm (right).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Results", "weight": 1.0} -->

| Model fit | True state | True state | True state | Noise-free z | fixation heights and lower observation quality, and in keeping with the results in Fig. 5, it also eventually converges to worse performance. We conjecture that the increased difficulty in the underlying control problem leads to systems for which only near-optimal policies provide meaningful reward signals, which manifests itself in the increased learning times observed in Fig. 6: we leave a formal investigation of this phenomenon to future work.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Results", "weight": 1.0} -->

Finally, we investigate why the performance of the H ∞ controller almost uniformly lags behind that of the RL agent in Fig. 5. A clue lies in the performance of H ∞ controllers at fixation 0.9, with depth images. We see an average reward of 228.63, with a success rate of 0.31 (see Tab. 2). This happens because H ∞ controllers tend to perfectly stabilize the cartpole when it is initialized with small deviations from the vertical, but they fail almost immediately outside this basin of attraction.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Results", "weight": 1.0} -->

Fig. 7: The maximum angles stabilized by the H ∞ controller fit to a model using ARXHK with varying amounts of data. In contrast to Fig. 6, the x axis here is the number of data samples used by the identification algorithm. For more details on this difference, see Appendix H. Each curve corresponds to a different fixation point. For RGB images, the green and blue curves overlap.The shaded regions represent the 25th and 75th quartiles across seven random datasets.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Results", "weight": 1.0} -->

To illustrate, the 50th and 75th percentile of H ∞ controller rewards at fixation point 0. 9 using depth images are 3, and 500 respectively.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Results", "weight": 1.0} -->

To better understand this phenomenon, we estimate the maximum initial angles (in degrees) for which the H ∞ controllers stabilize the systems. First, Tab. 1 considers the maximum angle for which a controller fit to the full state or the true z observations successfully stabilizes our system. As these models use full state observations, these quantities serve as a rough upper bound for the maximum initial angles stabilized by controllers synthesized from only noisy observations.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Results", "weight": 1.0} -->

Now, we measure the stabilizing range of our H ∞ controllers synthesized using ARXHK and noisily perceived z from depth and RGB images. For each type of observation, we plot the maximum stabilized angle vs. the amount of data used to fit the model in Fig. 7. As the perception problem becomes more difficult with lower fixation points and noisier z measurements, the maximum stabilized angle becomes smaller. Also of note is the step-like response in the sample-complexity curves of Fig. 7: the ARXHK and H ∞ based method required only a few hundred data points to saturate the performance achievable by their model class. This further suggests that by fitting a slightly richer model (e.g., piecewise linear) and relying on a slightly more sophisticated robust control method (e.g., gain scheduling), the regions of attractions could be expanded to match those of the RL controllers while still requiring much less data.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Discussion", "weight": 1.5} -->

Through the use of a theoretical model of a simple cartpole system and corresponding customized experimental environment, we have empirically evaluated the consequences of well understood fundamental limits of control on the performance achievable by learned perception-based controllers. In particular, we examined the effects of limits imposed by unstable dynamics combined with realistic sources of partial observability through incomplete or noisy visual perception. Our results suggest that these fundamental limits propagate through to other aspects of the learning and control pipeline. For example, Fig. 6 suggests that training time required to achieve a given level of performance is negatively affected by both poor (low fixation point ℓ 0 ) and noisy sensing. We also observed similar trends in performance (see Tab. 2), as measured by reward and success rate for the RL controller, and success rate for the robust H ∞ controller. We believe that our results are not the consequences of phenomenological behavior unique to the simple system studied in this paper, but that they rather hint at a deeper, more fundamental interplay between how difficult it is to sense and control a system, and how difficult it is to learn to control it.
