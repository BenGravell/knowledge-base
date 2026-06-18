<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Agile Autonomous Driving Using End-to-End Deep Imitation Learning

Topics include Imitation learning, End-to-end learning, Reinforcement learning, Deep learning, End-to-end, Trajectory optimization, Autonomous driving, Differential dynamic programming, Model-based.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Uses a "traditional" autonomy stack (trajectory optimization with learned dynamics, Kalman filter state estimation, and an handcrafted cost function) as the expert policy, then trains a neural network to imitate it end-to-end, from pixels to torques. Demonstrates that a full autonomy stack can be "compressed into" or "represented by" a single neural network. Notably, the trained neural network can be deployed with less expensive compute hardware and a lower fidelty sensor suite than the original autonomy stack.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present an end-to-end imitation learning system for agile, off-road autonomous driving using only low-cost on-board sensors. By imitating a model predictive controller equipped with advanced sensors, we train a deep neural network control policy to map raw, high-dimensional observations to continuous steering and throttle commands. Compared with recent approaches to similar tasks, our method requires neither state estimation nor on-the-fly planning to navigate the vehicle. Our approach relies , and experimentally validates, recent imitation learning theory. Empirically, we show that policies trained with online imitation learning overcome well-known challenges related to covariate shift and generalize better than policies trained with batch imitation learning. Built on these insights, our autonomous driving system demonstrates successful high-speed off-road driving, matching the state-of-the-art performance.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

High-speed autonomous off-road driving is a challenging robotics problem (Fig. 1). To succeed in this task, a robot is required to perform both precise steering and throttle maneuvers in a physically-complex, uncertain environment by executing a series of high-frequency decisions. Compared with most previously studied autonomous driving tasks, the robot here must reason about minimally-structured, stochastic natural environments and operate at high speed. Consequently, designing a control policy by following the traditional model-plan-then-act approach becomes challenging, as it is difficult to adequately characterize the robot's interaction with the environment *a priori*.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This task has been considered previously, for example, by Williams et al. using model-predictive control (MPC). While the authors demonstrate impressive results, their internal control scheme relies on expensive and accurate Global Positioning System (GPS) and Inertial Measurement Unit (IMU) for state estimation and demands high-frequency online replanning for generating control commands. Due to these costly hardware requirements, their robot can only operate in a rather controlled environment, which limits the applicability of their approach.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We aim to relax these requirements by designing a reflexive driving policy that uses only *low-cost, on-board* sensors (e.g. monocular camera, wheel speed sensors). Building on the success of deep reinforcement learning (RL), we adopt deep neural networks (DNNs) to parametrize the control policy and learn the desired parameters from the robot's interaction with its environment. While the use of DNNs as policy representations for RL is not uncommon, in contrast to most previous work that showcases RL in simulated environments, our agent is a high-speed physical system that incurs real-world cost: collecting data is a cumbersome process, and a single poor decision can physically impair the robot and result in weeks of time lost while replacing parts and repairing the platform. Therefore, direct application of model-free RL techniques is not only sample inefficient, but costly and dangerous in our experiments.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Single image &amp; laser
Real &amp;simulated

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Single image + wheel speeds
Batch &amp; online
Model predictive controller
Real &amp; simulated

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

These real-world factors motivate us to adopt *imitation learning* (IL) to optimize the control policy instead. A major benefit of using IL is that we can leverage domain knowledge through *expert* demonstrations. This is particularly convenient, for example, when there already exists an autonomous driving platform built through classic system engineering principles. While such a system (e.g. ) usually requires expensive sensors and dedicated computational resources, with IL we can train a lower-cost robot to behave similarly, without carrying the expert's hardware burdens over to the learner. Here we assume the expert is given as a black box oracle that can provide the desired actions when queried, as opposed to the case considered in where the expert can be modified to accommodate the learning progress.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we present an IL system for real-world high-speed off-road driving tasks. ^11^1Test run videos. By leveraging demonstrations from an algorithmic expert, our system can learn a driving policy that achieves similar performance compared to the expert. The system was implemented on a 1/5-scale autonomous AutoRally car. In real-world experiments, we show the AutoRally car---without any state estimator or online planning, but with a DNN policy that directly inputs measurements from a low-cost monocular camera and wheel speed sensors---could learn to perform high-speed driving at an average speed of $\sim$`<!-- -->`{=html}6 m/s and a top speed of $\sim$`<!-- -->`{=html}8 m/s (equivalently 108 km/h and 144 km/h on a full-scale car), matching the state-of-the-art.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Imitation Learning for Autonomous Driving", "weight": 1.0} -->

In this section, we give a concise introduction to IL, and discuss the strengths and weakness of deploying a batch or an online IL algorithm to our task. Our presentation is motivated by the realization that the connection between online IL and DAgger-like algorithms has not been formally introduced in continuous domains. To our knowledge, DAgger has only been used heuristically in these domains. Here we simplify the derivation of and extend it to continuous action spaces as required in the autonomous driving task.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Problem Definition", "weight": 1.0} -->

To mathematically formulate the autonomous driving task, we consider a discrete-time continuous-valued RL problem. Let $\mathbb{S}$, $\mathbb{A}$, and $\mathbb{O}$ be the state, action, and the observation spaces. In our setting, the state space is unknown to the agent; observations consist of on-board measurements, including a monocular RGB image from the front-view camera and wheel speeds from Hall effect sensors; actions consist of continuous-valued steering and throttle commands.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Problem Definition", "weight": 1.0} -->

The goal is to find a stationary, reactive policy^22^2While we focus on reactive policies in this section, the same derivations apply to history-dependent policies. $\pi:{{\mathbb{O}}\mapsto{\mathbb{A}}}$ (e.g. a DNN policy) such that $\pi$ achieves low accumulated cost over a finite horizon of length $T$,

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-B Imitation Learning", "weight": 1.0} -->

Directly optimizing is challenging for high-speed off-road autonomous driving. Since our task involves a physical robot, model-free RL techniques are intolerably sample inefficient and have the risk of permanently damaging the car when applying a partially-optimized policy in exploration. Although model-based RL may require fewer samples, it can lead to suboptimal, potentially unstable results, because it is difficult for a model that uses only on-board measurements to fully capture the complex dynamics of off-road driving.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B Imitation Learning", "weight": 1.0} -->

Considering these limitations, we propose to solve for policy $\pi$ by IL. We assume the access to an oracle policy or *expert* $\pi^{\ast}$ to generate demonstrations during the training phase. This expert can rely on resources that are unavailable in the testing phase, like additional sensors and computation. For example, the expert can be a computationally intensive optimal controller that relies on exteroceptive sensors (e.g. GPS for state estimation), or an experienced human driver.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Imitation Learning", "weight": 1.0} -->

The goal of IL is to perform as well as the expert with an error that has at most linear dependency on $T$. Formally, we introduce a lemma due to Kakade and Langford and define what we mean by an *expert*.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B1 Online Imitation Learning", "weight": 1.0} -->

We now present the objective function for the online learning approach to IL. Assume $\pi^{\ast}$ is an expert to and suppose $\mathbb{A}$ is a normed space with norm $\parallel \cdot \parallel$. Let $D_{W}{( \cdot, \cdot )}$ denote the Wasserstein metric: for two probability distributions $p$ and $q$ defined on a metric space $\mathcal{M}$ with metric $d$,

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B1 Online Imitation Learning", "weight": 1.0} -->

where $\Gamma$ denotes the family of distributions whose marginals are $p$ and $q$. It can be shown by the Kantorovich-Rubinstein theorem that the above two definitions are equivalent. These assumptions allow us to construct a surrogate problem, which is relatively easier to solve than.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B1 Online Imitation Learning", "weight": 1.0} -->

The problem in is called the *online* IL problem. This surrogate problem is comparatively more structured than the original RL problem, so we can adopt algorithms with provable performance guarantees. In this paper, we use the meta-algorithm DAgger, which reduces to a sequence of supervised learning problems: Let $\mathcal{D}$ be the training data. DAgger initializes $\mathcal{D}$ with samples gathered by running $\pi^{\ast}$. Then, in the $i$th iteration, it trains $\pi_{i}$ by supervised learning,

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B1 Online Imitation Learning", "weight": 1.0} -->

where subscript $\mathcal{D}$ denotes empirical data distribution. Next it runs $\pi_{i}$ to collect more data, which is then added into $\mathcal{D}$ to train $\pi_{i + 1}$. The procedure is repeated for $O{(T)}$ iterations and the best policy, in terms of, is returned. Suppose the policy is linearly parametrized. Since our instantaneous cost $\hat{c}{(s_{t}, \cdot )}$ is strongly convex, the theoretical analysis of DAgger applies. Therefore, together with the assumption that $\pi^{\ast}$ is an expert, running DAgger to solve finds a policy $\pi$ with performance ${J{(\pi)}} \leq {{J{(\pi^{\ast})}} + {O{(T)}}}$, achieving our initial goal.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B1 Online Imitation Learning", "weight": 1.0} -->

We note here the instantaneous cost $\hat{c}{(s_{t}, \cdot )}$ can be selected to be any suitable norm according the problem's property. In our off-road autonomous driving task, we find $l_{1}$-norm is preferable (e.g. over $l_{2}$-norm) for its ability to filter outliers in a highly stochastic environment.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B2 Batch Imitation Learning", "weight": 1.0} -->

where we use again Lemma 1 for the equality and the property of Wasserstein distance for inequality.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B2 Batch Imitation Learning", "weight": 1.0} -->

In contrast to the surrogate problem in online IL, batch IL reduces to a supervised learning problem, because the expectation is defined by a fixed policy $\pi^{\ast}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C Comparison of Imitation Learning Algorithms", "weight": 1.0} -->

Comparing and, we observe that in batch IL the Lipschitz constant $C_{\pi}^{t}{(s^{\ast})}$, without $\pi$ being an expert as in Definition 1, can be on the order of $T - t$ in the worst case. Therefore, if we take a uniform bound and define $C_{\pi} = {\sup_{{t \in {\lbrack 0,{T - 1}\rbrack}},{s \in {\mathbb{S}}}}{C_{\pi}^{t}{(s)}}}$, we see $C_{\pi} \in {O{(T)}}$. In other words, under the same assumption in online imitation (i.e. is minimized to an error in $O{(T)}$), the difference between $J{(\pi)}$ and $J{(\pi^{\ast})}$ in batch IL actually grows quadratically in $T$ due to error compounding.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Comparison of Imitation Learning Algorithms", "weight": 1.0} -->

This problem manifests especially in stochastic environments. Therefore, in order to achieve the same level of performance as online IL, batch IL requires a more expressive policy class or more demonstration samples. As shown, the quadratic bound is tight.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Comparison of Imitation Learning Algorithms", "weight": 1.0} -->

Therefore, if we can choose an expert policy $\pi^{\ast}$ that is stable in the sense of Definition 1, then online IL is preferred theoretically. This is satisfied, for example, when the expert policy is an algorithm with certain performance characteristics. On the contrary, if the expert is human, the assumptions required by online IL become hard to realize in real-road driving tasks. This is especially true in off-road driving tasks, where the human driver depends heavily on instant feedback from the car to overcome stochastic disturbances. Therefore, the frame-by-frame labeling approach, for example, can lead to a very counter-intuitive, inefficient data collection process, because the required dynamics information is lost in a single image frame. Overall, when using human demonstrations, online IL can be as bad as batch IL, simply due to inconsistencies introduced by human nature.

<!-- chunk {"id": "body-0027", "role": "body", "section": "The Autonomous Driving System", "weight": 1.0} -->

Building on the previous analyses, we design a system that can learn to perform fast off-road autonomous driving with only on-board measurements. The overall system architecture for learning end-to-end DNN driving policies is illustrated in Fig. 2. It consists of three high-level controllers (an expert, a learner, and a safety control module) and a low-level controller, which receives steering and throttle commands from the high-level controllers and translates them to pulse-width modulation (PWM) signals to drive the steering and throttle actuators of a vehicle.

<!-- chunk {"id": "body-0028", "role": "body", "section": "The Autonomous Driving System", "weight": 1.0} -->

On the basis of the analysis in Section III-C, we assume the expert is algorithmic and has access to expensive sensors (GPS and IMU) for accurate global state estimates^44^4Global position, heading and roll angles, linear velocities, and heading angle rate. and resourceful computational power. The expert is built on multiple hand-engineered components, including a state estimator, a dynamics model of the vehicle, a cost function of the task, and a trajectory optimization algorithm for planning (see Section IV-A). By contrast, the learner is a DNN policy that has access to only a monocular camera and wheel speed sensors and is required to output steering and throttle command directly (see Section IV-B).

<!-- chunk {"id": "body-0029", "role": "body", "section": "The Autonomous Driving System", "weight": 1.0} -->

In this setting, the sensors that the learner uses can be significantly cheaper than those of the expert; specifically on our experimental platform, the AutoRally car (see Section IV-C), the IMU and the GPS sensors required by the expert in Section IV-A together cost more than \$6,000, while the sensors used by the learner's DNN policy cost less than \$500. The safety control module has the highest priority among all three controllers and is used prevent the vehicle from high-speed crashing.

<!-- chunk {"id": "body-0030", "role": "body", "section": "The Autonomous Driving System", "weight": 1.0} -->

The software system was developed based on the Robot Operating System (ROS) in Ubuntu. In addition, a Gazebo-based simulation environment was built using the same ROS interface but without the safety control module; the simulator was used to evaluate the performance of the software before real track tests.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A An Algorithmic Expert: Model-Predictive Control", "weight": 1.0} -->

We use an MPC expert based on an incremental Sparse Spectrum Gaussian Process (SSGP) dynamics model (which was learned from 30 minute-long driving data) and an iSAM2 state estimator. To generate actions, the MPC expert solves a finite horizon optimal control problem for every sampling time: at time $t$, the expert policy $\pi^{\ast}$ is a locally optimal policy such that

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A An Algorithmic Expert: Model-Predictive Control", "weight": 1.0} -->

where $T_{h}$ is the length of horizon it previews.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A An Algorithmic Expert: Model-Predictive Control", "weight": 1.0} -->

The computation is realized by Differential Dynamic Programming (DDP): in each iteration of DDP, the system dynamics and the cost function are approximated quadratically along a nominal trajectory; then the Bellman equation of the approximate problem is solved in a backward pass to compute the control law; finally, a new nominal trajectory is generated by applying the updated control law through the dynamics model in a forward pass. Upon convergence, DDP returns a locally optimal control sequence $\{{\hat{a}}_{t}^{\ast},\ldots,{\hat{a}}_{{t + T_{h}} - 1}^{\ast}\}$, and the MPC expert executes the first action in the sequence as the expert's action at time $t$ (i.e. $a_{t}^{\ast} = {\hat{a}}_{t}^{\ast}$). This process is repeated at every sampling time (see the Appendix for details).

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A An Algorithmic Expert: Model-Predictive Control", "weight": 1.0} -->

In view of the analysis in Section III-B, we can assume that the MPC expert satisfies Definition 1, because it updates the approximate solution to the original RL problem in high-frequency using global state information. However, because MPC requires replanning for every step, running the expert policy online consumes significantly more computational power than what is required by the learner.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Learning a DNN Control Policy", "weight": 1.0} -->

The learner's control policy $\pi$ is parametrized by a DNN containing $\sim$`<!-- -->`{=html}10 million parameters. As illustrated in Fig. 3, the DNN policy, consists of two sub-networks: a convolutional neural network (CNN) with 6 convolutional layers, 3 max-pooling layers, and 2 fully-connected layers, that takes $160 \times 80$ RGB monocular images as inputs,^55^5The raw images from the camera were re-scaled to $160 \times 80$. and a feedforward network with a fully-connected hidden layer that takes wheel speeds as inputs. The convolutional and max-pooling layers are used to extract lower-dimensional features from images. The DNN policy uses $3 \times 3$ filters for all convolutional layers, and rectified linear unit (ReLU) activation for all layers except the last one. Max-pooling layers with $2 \times 2$ filters are integrated to reduce the spatial size of the representation (and therefore reduce the number of parameters and computation loads).

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Learning a DNN Control Policy", "weight": 1.0} -->

The two sub-networks are concatenated and then followed by another fully-connected hidden layer. The structure of this DNN was selected empirically based on experimental studies of several different architectures.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B Learning a DNN Control Policy", "weight": 1.0} -->

In construction of the surrogate problem for IL, the action space $\mathbb{A}$ is equipped with $\parallel \cdot \parallel_{1}$ for filtering outliers, and the optimization problem, or, is solved using ADAM, which is a stochastic gradient descent algorithm with an adaptive learning rate. Note while $s_{t}$ or $s_{t}^{\ast}$ is used in or, the neural network policy does not use the state, but rather the synchronized raw observation $o_{t}$ as input. Note that we did not perform any data selection or augmentation techniques in any of the experiments. ^66^6Data collection or augmentation techniques such as can be used in conjunction with our method. The only pre-processing was scaling and cropping of raw images.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-C The Autonomous Driving Platform", "weight": 1.0} -->

To validate our IL approach to off-road autonomous driving, the system was implemented on a custom-built, 1/5-scale autonomous AutoRally car (weight 22 kg; LWH 1m$\times$`<!-- -->`{=html}0.6m$\times$`<!-- -->`{=html}0.4m), shown in the top figure in Fig. 4. The car was equipped with an ASUS mini-ITX motherboard, an Intel quad-core i7 CPU, 16GB RAM, a Nvidia GTX 750 Ti GPU, and a 11000mAh battery. For sensors, two forward facing machine vision cameras,^77^7In this work we only used one of the cameras. a Hemisphere Eclipse P307 GPS module, a Lord Microstrain 3DM-GX4-25 IMU, and Hall effect wheel speed sensors were instrumented. In addition, an RC transmitter could be used to remotely control the vehicle by a human, and a physical run-stop button was installed to disable all motions in case of emergency.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-C The Autonomous Driving Platform", "weight": 1.0} -->

The source code used in this work is availalbe ^88^8GitHub repos: Imitation learning, AutoRally platform..

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C The Autonomous Driving Platform", "weight": 1.0} -->

In the experiments, all computation was executed on-board the vehicle in real-time. In addition, an external laptop was used to communicate with the on-board computer remotely via Wi-Fi to monitor the vehicle's status. The observations were sampled and action were executed at 50 Hz to account for the high-speed of the vehicle and the stochasticity of the environment. Note this control frequency is significantly higher than (10 Hz), (12 Hz), and (15 Hz).

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A High-speed Driving Task", "weight": 1.0} -->

We tested the performance of the proposed IL system in Section IV in a high-speed driving task with a desired speed of 7.5 m/s (an equivalent speed of 135 km/h on a full-scale car). The performance index of the task was formulated as the cost function in the finite-horizon RL problem with

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A High-speed Driving Task", "weight": 1.0} -->

in which $c_{\text{pos}}$ favors the vehicle to stay in the middle of the track, $c_{\text{spd}}$ drives the vehicle to reach the desired speed, $c_{\text{slip}}$ stabilizes the car from slipping, and $c_{\text{act}}$ inhibits large control commands (see the Appendix for details).

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A High-speed Driving Task", "weight": 1.0} -->

The goal of the high-speed driving task to minimize the accumulated cost function over one-minute continuous driving. That is, under the 50-Hz sampling rate, the task horizon was set to 60 seconds ($T = 3000$). The cost information was given to the MPC expert in Fig. 2 to perform online trajectory optimization with a two-second prediction horizon ($T_{h} = 100$). In the experiments, the weighting in were set as $\alpha_{1} = 2.5$, $\alpha_{2} = 1$, $\alpha_{3} = 100$ and $\alpha_{4} = 60$, so that the MPC expert in Section IV-A could perform reasonably well. The learner's policy was tuned by online/batch IL in attempts to match the expert's performance.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-B Test Track", "weight": 1.0} -->

All the experiments were performed on an elliptical dirt track, shown in the bottom figure of Fig. 4, with the AutoRally car described in Section IV-C. The test track was $\sim$`<!-- -->`{=html}3m wide and $\sim$`<!-- -->`{=html}30m long and built with fill dirt. Its boundaries were surrounded by soft HDPE tubes, which were detached from the ground, for safety during experimentation. Due to the changing dirt surface, debris from the track's natural surroundings, and the shifting track boundaries after car crashes, the track condition and vehicle dynamics can change from one experiment to the next, adding to the complexity of learning a robust policy.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-C Data Collection", "weight": 1.0} -->

Training data was collected in two ways. In batch IL, the MPC expert was executed, and the camera images, wheel speed readings, and the corresponding steering and throttle commands were recorded. In online IL, a mixture of the expert and learner's policy was used to collect training data (camera images, wheel speeds, and expert actions): in the $i$th iteration of DAgger, a mixed policy was executed at each time step ${\hat{\pi}}_{i} = {{\beta^{i}\pi^{\ast}} + {{({1 - \beta^{i}})}\pi_{i - 1}}}$, where $\pi_{i - 1}$ is learner's DNN policy after $i - 1$ DAgger iterations, and $\beta^{i}$ is the probability of executing the expert policy. The use of a mixture policy was suggested in for better stability. A mixing rate $\beta = 0.6$ was used in our experiments. Note that the probability of using the expert decayed exponentially as the number of DAgger iterations increased.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-C Data Collection", "weight": 1.0} -->

Experimental data was collected on an outdoor track, and consisted of changing lighting conditions and environmental dynamics. In the experiments, the rollouts about to crash were terminated remotely by overwriting the autonomous control commands with the run-stop button or the RC transmitter in the safety control module; these rollouts were excluded from the data collection.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-D Policy Learning", "weight": 1.0} -->

In online IL, three iterations of DAgger were performed. At each iteration, the robot executed one rollout using the mixed policy described above (the probabilities of executing the expert policy were 60%, 36%, and 21%, respectively). For a fair comparison, the amount of training data collected in batch IL was the same as all of the data collected over the three iterations of online IL.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-D Policy Learning", "weight": 1.0} -->

At each training phase, the optimization problem or was solved by ADAM for 20 epochs, with mini-batch size 64, and a learning rate of 0.001. Dropouts were applied at all fully connected layers to avoid over-fitting (with probability 0.5 for the firstly fully connected layer and 0.25 for the rest). See Section IV-B for details. Finally, after the entire learning session of a policy, three rollouts were performed using the learned policy for performance evaluation.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VI-A Empirical Performance", "weight": 1.0} -->

We first study the performance of training a control policy with online and batch IL algorithms. Fig. 5 illustrates the vehicle trajectories of different policies. Due to accumulating errors, the policy trained with batch IL crashed into the lower-left boundary, an area of the state-action space rarely explored in the expert's demonstrations. In contrast to batch IL, online IL successfully copes with corner cases as the learned policy occasionally ventured into new areas of the state-action space.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VI-A Empirical Performance", "weight": 1.0} -->

Fig. 6 shows the performance in terms of distance traveled without crashing^99^9We used the safe control module shown in Fig. 2 to manually terminate the rollout when the car crashed into the soft boundary. and Table II shows the statistics of the experimental results. Overall, DNN policies trained with both online and batch IL algorithms were able to achieve speeds similar to the MPC expert. However, with the same amount of training data, the policies trained with online IL in general outperformed those trained with batch IL. In particular, the policies trained using online IL achieved better performance in terms of both completion ratio and imitation loss.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VI-A Empirical Performance", "weight": 1.0} -->

In addition, we found that, when using online IL, the performance of the policy monotonically improves over iterations as data are collected, which is opposed to what was found by Laskey et al.. The discrepancy can be explained with a recent theoretical analysis by Cheng and Boots, which provides a necessary and sufficient condition for the convergence of the policy sequence. In particular, the authors show that adopting a non-zero mixing (as used in our experiment) is sufficient to guarantee the convergence of the learned policy sequence. Our autonomous driving system is a successful real-world demonstration of this IL theory.

<!-- chunk {"id": "body-0052", "role": "body", "section": "VI-A Empirical Performance", "weight": 1.0} -->

Finally, it is worth noting that the traveled distance of the batch learning policy, learned with 3,000 samples, was longer than that of other batch learning policies. This is mainly because this policy achieved better steering performance than throttle performance (cf. Steering/Throttle loss in Table II). That is, although the vehicle was able to navigate without crashing, it actually traveled at a much slower speed. By contrast, the other batch learning policies that used more data had better throttle performance and worse steering performance, resulting in faster speeds but also higher chances of crashing.

<!-- chunk {"id": "body-0053", "role": "body", "section": "VI-B Generalizability of the Learned Policy", "weight": 1.0} -->

To further analyze the difference between the DNNs trained using online and batch IL, we embed the data in a two-dimensional space using t-Distributed Stochastic Neighbor Embedding (t-SNE), as shown in Fig. 7 and Fig. 8. These figures visualize the data in both batch and online IL settings, where "train" denotes the data collected to train the policies and "test" denotes the data collected to evaluate the performance of the final policies after the learning phase.^1010^10For the online setting, the train data include the data in all DAgger iterations; for the batch setting, the train data include the same amount of data but collected by the expert policy. The figures plot a subset of 3,000 points from each data set.

<!-- chunk {"id": "body-0054", "role": "body", "section": "VI-B Generalizability of the Learned Policy", "weight": 1.0} -->

We first observe in Fig. 7 that, while the wheel speed data have similar training and testing distributions, the image distributions are fairly misaligned. The raw images are subject to changing lighting conditions, as the policies were executed at different times and days, and to various trajectories the robot stochastically traveled. Therefore, while the task (driving fast in the same direction) is seemingly monotone, it actually is not. More importantly, the training and testing images were collected by executing different policies, which leads to different distributions of the neural networks inputs. This is known as the covariate shift problem, which can significantly complicate the learning process.

<!-- chunk {"id": "body-0055", "role": "body", "section": "VI-B Generalizability of the Learned Policy", "weight": 1.0} -->

The policy trained with online IL yet still demonstrated great performance in the experiments. To further understand how it could generalize across different image distributions, we embed its feature distribution in Fig. 8 (a) and (b).^1111^11The feature here are the last hidden layer of the neural network. The output layer is a linear function of the features. Interestingly, despite the difference in the raw feature distributions in Fig. 7 (a) and (b), the DNN policy trained with online IL are able to map the train and test data to similar feature distributions, so that a linear combination (the last layer) of those features is sufficient to represent a good policy. On the contrary, the DNN policy trained with batch IL fails to learn a coherent feature embedding, as shown in Fig. 8 (c) and (d). This could explain the inferior performance of batch IL, and its inability to deal with the corner case in Fig. 5 (b). This evidence shows that our online learning system can alleviate the covariate shift issue caused by executing different policies at training and testing time.

<!-- chunk {"id": "body-0056", "role": "body", "section": "VI-B Generalizability of the Learned Policy", "weight": 1.0} -->

(a) Batch data wrt online model

<!-- chunk {"id": "body-0057", "role": "body", "section": "VI-B Generalizability of the Learned Policy", "weight": 1.0} -->

(b) Online data wrt online model

<!-- chunk {"id": "body-0058", "role": "body", "section": "VI-B Generalizability of the Learned Policy", "weight": 1.0} -->

(c) Batch data wrt batch model

<!-- chunk {"id": "body-0059", "role": "body", "section": "VI-B Generalizability of the Learned Policy", "weight": 1.0} -->

(d) Online data wrt batch model

<!-- chunk {"id": "body-0060", "role": "body", "section": "VI-C The Neural Network Policy", "weight": 1.0} -->

Compared with hand-crafted feature extractors, one main advantage of a DNN policy is that it can learn to extract both low-level and high-level features of an image and automatically detect the parts that have greater influence on steering and throttle. We validate this idea by showing in Fig. 9 the averaged feature map at each max-pooling layer (see Fig. 3), where each pixel represents the averaged unit activation across different filter outputs. We can observe that at a deeper level, the detected salient features are boundaries of the track and parts of a building. In contrast, grass and dirt contribute little.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VI-C The Neural Network Policy", "weight": 1.0} -->

We also analyze the importance of incorporating wheel speeds in our task. We compare the performance of the policy based on our DNN policy and a policy based on only the CNN subnetwork (without wheel-speed inputs) in batch IL. The data was collected in accordance with Section V-C. Fig. 10 shows the batch IL loss in of different network architectures. The full DNN policy in Fig. 3 achieved better performance consistently. While images contain position and orientation information, it is insufficient to infer velocities, which are a part of the (hidden) vehicle state. Therefore, we conjecture state-of-the-art CNNs (e.g. ) cannot be directly used to perform both lateral and longitudinal controls, as we do here. By contrast, while without a recurrent architecture, our DNN policy learned to combine wheel speeds in conjunction with CNN to infer hidden state and achieve better performance.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduce an end-to-end system to learn a deep neural network control policy for high-speed driving that maps raw on-board observations to steering and throttle commands by mimicking a model predictive controller. In real-world experiments, our system was able to perform fast off-road navigation autonomously using a low-cost monocular camera and wheel speed sensors. We also provide an analysis of both online and batch IL frameworks, both theoretically and empirically and show that our system, when trained with online IL, learns generalizable features that are more robust to covariate shift than features learned with batch IL.
