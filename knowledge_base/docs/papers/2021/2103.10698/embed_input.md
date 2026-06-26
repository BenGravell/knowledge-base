<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

AutoTune: Controller Tuning for High-Speed Flight

Topics include Sampling-based methods, Optimization, Control, Sampling, AutoTune.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Due to noisy actuation and external disturbances, tuning controllers for high-speed flight is very challenging. In this paper, we ask the following questions: How sensitive are controllers to tuning when tracking high-speed maneuvers? What algorithms can we use to automatically tune them? To answer the first question, we study the relationship between parameters and performance and find out that the faster the maneuver, the more sensitive a controller becomes to its parameters. To answer the second question, we review existing methods for controller tuning and discover that prior works often perform poorly on the task of high-speed flight. Therefore, we propose AutoTune, a sampling-based tuning algorithm specifically tailored to high-speed flight. In contrast to previous work, our algorithm does not assume any prior knowledge of the drone or its optimization function and can deal with the multi-modal characteristics of the parameters' optimization space. We thoroughly evaluate AutoTune both in simulation and in the physical world. In our experiments, we outperform existing tuning algorithms by up to 90% in trajectory completion. The resulting controllers are tested in the AirSim Game of Drones competition, where we outperform the winner by up to 25% in lap-time.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finally, we show that AutoTune improves tracking error when flying a physical platform with respect to parameters tuned by a human expert.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Flying high-speed trajectories with a quadrotor requires the platform's controller to be meticulously tuned,. The Manuscript received: September, 9th, 2021; Revised December, 9th, 2021; Accepted January, 11th, 2022. This paper was recommended for publication by Editor Tamim Asfour upon evaluation of the Associate Editor and Reviewers' comments. The first two authors contributed equally. The work was done at the Robotics and Perception Group, University of Zurich, Switzerland and was supported by the National Centre of Competence in Research (NCCR) Robotics, through the Swiss National Science Foundation (SNSF), and the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation programme (Grant agreement No. 864042).

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Fig. 2: Trajectory completion (%) as a function of two parameters of a model-predictive controller. The trajectory completion measures the percentage of trajectory successfully tracked by the controller. The high speed and high angular accelerations required by time-optimal trajectories make the controller extremely sensitive to its parameters. complex relationship between parameters and performance, empirically shown in Fig. 2, is caused by unavoidable factors such as imperfect modeling and external disturbances. This work is motivated by the following questions: What are the characteristics of this optimization space? How can we automatically find controller parameters for high-speed flight?

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Tuning controller parameters to fly high-speed maneuvers is difficult due to three main challenges: (i) the objective function (i.e. the relationship between controller parameters and performance) is highly non-convex (See Fig. 2); (ii) the tuning process only relies on noisy evaluations 1 of the objective function at adaptively chosen parameters, but not to the function itself or its gradients; (iii) different parts of the trajectory, e.g. a sharp turn or a straight-line acceleration, generally require different controller behaviors, hence dynamically changing parameters.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The traditional approach for automatic tuning and adaptive control, generally known as MIT rule, requires to express the desired performance metric, e.g. the average tracking error over the entire maneuver, as a quadratic function of controller parameters, and then optimizes the controller with gradient-based optimization. However, expressing the long-term performance on a high-speed maneuver with respect to the parameters of a receding horizon controller ( i.e. the optimization function depicted in Fig. 2) is generally intractable. Indeed, it requires to know a priori the exact model of the quadrotor and the disturbances acting on it during flight, e.g. noisy actuation and aerodynamic effects. Instead of analytically computing it, another line of work proposes to iteratively estimate the optimization function, and use the estimate to find optimal parameters. However, these methods make over-simplifying assumptions on the objective function, e.g. convexity or relative Gaussianity between observations. Such assumptions are generally not suited for controller tuning to high-speed flight, where the function is highly non-convex (c.f. Fig. 2). To remove any assumption, model-free methods propose to directly search for optimal parameters using sampling.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Such methods are however built on heuristics not necessarily suited to high-speed flight and generally require thousands of iterations to converge.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

1 Due to noise the same controller parameters can yield different performance on multiple runs.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this paper, we propose a novel sampling-based algorithm specifically tailored to the problem of high-speed flight, rooted in statistical theory: AutoTune. Given an initial, lowperformance controller, AutoTune optimizes its parameters to maximize a user-defined metric, e.g. track completion. In contrast to traditional adaptive control, e.g. the MIT rule, it does not require to analytically express the optimization function with respect to the controller parameters, nor assumptions about the optimization function. Similarly to modelfree sampling-based methods, AutoTune does neither require prior knowledge of the platform model and external disturbances. However, to make sampling computationally tractable, our approach uses Metropolis-Hastings sampling (M-H) and several strategies specifically tailored to the problem of high-speed flight. Specifically, motivated by the observation that different parts of a trajectory require different controller behaviors, we propose a strategy to break down a trajectory into components with different behaviors, e.g. sharp descent or planar acceleration. Despite controller parameters being different for each component, they are all optimized jointly to favor optimality over the entire trajectory.

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In addition, to speed up convergence, we train a regressor to predict good initialization parameters.

<!-- chunk {"id": "body-0012", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We perform an extensive evaluation in two simulators and in the physical world in a large tracking arena of 30 × 30 × 8m volume. In these experiments, we find out that: (i) the faster a maneuver is, the more sensitive a controller becomes to its parameters, and (ii) the optimization function is multi-modal, i.e. multiple controller configurations lead to the desired performance. We empirically show that our approach can tune controllers up to 90 percentage points better than previous work in terms of trajectory completion. We then validate the controller parameters found by AutoTune in simulation on a physical platform. These parameters decrease the tracking error with respect to the ones tuned by a human expert, enabling the quadrotor to achieve speeds over 50 kmh -1.

<!-- chunk {"id": "body-0013", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

- We present a novel sampling-based method for tuning quadrotor controllers on the task of high-speed flight. - We show that our method outperforms existing methods for automatic controller tuning and enables quadrotors to fly time-optimal trajectories both in simulation and in the physical world in one of the world's largest motioncapture systems. - We provide interesting insights into the relationship between the parameters of a receding horizon controller and its flight performance on high-speed maneuvers.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Metropolis-Hastings Sampling", "weight": 1.0} -->

In statistics, the Metropolis-Hastings (M-H) algorithm is used to obtain a sequence of random samples from a desired distribution P (w) which can't be directly accessed. To generate the samples, the M-H algorithm requires a score function d (w) which is proportional to the density P (w). Samples are produced in an iterative fashion: the next sample w t +1 comes from a distribution t (w t +1 | w t), referred to as transition model, which only depends on the current sample w t. As transition model t (w t +1 | w t) we select a Gaussian with constant variance σ = 5 centered on w t. We keep this transition model fixed for all experiments. The next sample w t +1 is then accepted and used for the next iteration, or it is rejected, discarded, and the current sample w t is re-used for the next iteration. Specifically, the sample is accepted with probability equal to Therefore, M-H always accepts a sample with a higher score. However, the move to a sample with a smaller score will sometimes be rejected, and the higher the drop in score 1 α, the smaller the probability of acceptance.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Metropolis-Hastings Sampling", "weight": 1.0} -->

Therefore, many samples come from the high-density regions of P (w), while relatively few from the low-density regions. Intuitively, this is why the empirical sample distribution ˆ P (w) approximates the target distribution P (w).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Metropolis-Hastings Sampling", "weight": 1.0} -->

2 Parameters are equivalent up to scale. To account for this effect, we keep the cost on inputs R constant Fig. 3: We compute a minimum-time trajectory passing through all waypoints. The trajectory is then segmented in parts that require different controller behaviors, and initial parameters for each segment are predicted with a regressor. The parameters are then jointly optimized with M-H sampling over multiple rollouts.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Metropolis-Hastings Sampling", "weight": 1.0} -->

In this work, we use the M-H algorithm to find the parameters of a controller flying time-optimal trajectories. In this case, P (w) = 1 /Zd (w), where w are MPC parameters, Z is an unknown normalization factor, and d (w) is the score function: where m (w) is a metric measuring the performance (e.g. time) the controller accumulates over the entire trajectory. According to P (w), the points with maximum probability are the ones with higher score. However, in the task of controller tuning, we are not interested in approximating the distribution of controller parameters ˆ P (w), but to find, with as few samples as possible, parameters that enable tracking a trajectory accurately. We continue the sampling procedure up to when we find a solution satisfying some user-defined performance metrics, e.g. tracking error or trajectory completion. When found, we re-evaluate the solution for four times to account for the randomness of the simulation.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Metropolis-Hastings Sampling", "weight": 1.0} -->

This setup makes the use of Metropolis-Hasting sampling equivalent to simulated annealing with constant temperature. Despite varying-temperature simulated annealing providing the asymptotic guarantee of global optimality, it generally requires a significantly larger number of samples with respect to its constant-temperature counterpart and a specifically designed heuristic to define the cooling function. Therefore, since we are not interested in the global optimum but only in a controller configuration satisfying a user-defined performance metric, we keep the temperature to a constant value. In addition, due to the temperature-based sampling, simulated annealing does not provide the possibility to approximate the distribution of controller parameters (c.f. Fig. 2). Conversely, MH can approximate the distribution and used to study the characteristics of the optimization space.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Scoring Performance with Time", "weight": 1.0} -->

According to Eq., we define the metric m ( w ) in Eq. to be the time t to pass all waypoints, i.e. m ( w ) = J ( π ( w )). However, it is not clear how to define this metric when the drone misses a waypoint or crashes before the end of the trajectory. To solve this problem, we propose to stop the experiment whenever the drone misses a waypoint or crashes.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Scoring Performance with Time", "weight": 1.0} -->

Fig. 4: Before starting the sampling, AutoTune segments a trajectory according to the gradient of z. The above maneuver was split into flat (blue), ascent (red), drop (green, steep descent), and descent (purple).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Scoring Performance with Time", "weight": 1.0} -->

In this case, a penalty equal to the shortest path between the drone position and all further waypoints is added to the time. In such a way, it is possible to distinguish between parameters w that make the drone crash in the early stage of a trajectory and the ones that can complete the trajectory to the end.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Trajectory Segmentation", "weight": 1.0} -->

Complex high-speed trajectories require different controller behaviors along the track. For example, consider the reference trajectory illustrated in Fig. 4. The initial segment, depicted in blue, is approximately planar but has a large curvature in the x-y plane. In contrast, the drop segment, depicted in green in Fig. 4, has a large gradient in height, but little motion in the xy plane. Clearly, these two segments need different controller behaviors to be successfully tracked. The blue planar segment requires the controller to be very precise on x-y tracking, but less controller authority is needed on the z-plane. Conversely, the large drop in altitude of the green segment necessitates very accurate tracking of the reference on the z plane, but less on the x-y one. Accounting for this behavior is important for time-optimal trajectories, where the drone is always close to its physical limits. Therefore, global parameters are likely to fail to track the entire trajectory, no matter how many samples are generated.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Trajectory Segmentation", "weight": 1.0} -->

Motivated by this observation, we split the trajectory into multiple segments according to the height gradient of the reference. In each segment different parameters are assigned to the controller. Specifically, we assign each point to the class fl, ascent, or descent if the difference in height g z = z [ k ] -z [ k +1] with its successor is | g z | < 1 m,g z ≥ 1 m,g z ≤ -1 m, respectively. This segmentation condition is kept fixed for all experiments and ablated in the appendix. The resulting segments are then clustered such that the minimum segment duration is 2 seconds. Eventually, all the descent and ascent segments with a slope higher than 45 ° are recursively split into two equal parts, where the first is assigned to the class steep and the second remains assigned to the original class. Fig. 4 shows the result of the segmentation algorithm in one of our testing maneuvers. To account for the strong correlations between segments and keep the optimization global over the trajectory, the controller parameters associated with each segment are updated jointly. More details about the joint optimization process and other segmentation examples are available in the appendix.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Trajectory Segmentation", "weight": 1.0} -->

| Track | Max Vel [ ms - 1 ] | Random Search | Bayesian Optimization | Bayesian Optimization | Bayesian Optimization | Bayesian Optimization | Bayesian Optimization | PSO | CMA-ES | Gradient Boosting | AutoTune |

<!-- chunk {"id": "body-0025", "role": "body", "section": "Sampler Initialization", "weight": 1.0} -->

The Metropolis-Hastings algorithm requires an initial parameter configuration w 0 to initialize the sampling. Instead of using a random initialization, we propose to use an informed guess for w 0. Specifically, we use a Gradient Boosting regressor with default parameters to predict initial controller parameters for each trajectory segment. The training data for this regressor are controller parameters found to be optimal on 5 training trajectories different in layout from the testing ones. A different regressor is trained for each type of trajectory segment, i.e. flat, ascent, descent, and steep. Five features including information about the reference trajectory are used for prediction: the number of points in the segment, the slope of the line connecting the first and last point of the segment, as well as their height difference, and the mean velocity and acceleration. These features have been selected with a crossvalidation procedure.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Sampler Initialization", "weight": 1.0} -->

Overall, the idea of predicting an initial guess w 0 with a regressor trained on previously seen trajectory experimentally shows to drastically reduce the number of samples (up to 88%) to find controller parameters for flying a time-optimal trajectory. More details about the training data, the training procedure, and an ablation study of the features are available in the supplementary material.

<!-- chunk {"id": "body-0027", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

We design our evaluation procedure to address the following questions: Can AutoTune find controller parameters to fly high-speed trajectories? What are the characteristics of the optimization space of controller parameters for the task of high-speed flight? Do the tuned controllers improve performance on a physical platform? Furthermore, we validate our design choices with ablation studies. We encourage the reader to watch the supplementary video for qualitative results.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We use for our experiments two simulators known for their physical and visual realism: Microsoft AirSim, and Flightmare. Our sampling procedure is strongly favored by the high speed at which they can simulate physics (up to 10K times real-time). We test AutoTune on six trajectories selected to evaluate controller performance under strong accelerations and high-speed on all axes.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

For comparison, we use four baselines for controller tuning. A naive one ( Random Sampling ) which randomly samples parameters independently and uniformly on all axis with a variance of 5. Moreover, we compare to the strong baselines of Bayesian Optimization with multiple choices of the Gaussian kernel; Particle Swarm Optimization (PSO), with 10 particles and using 0. 5, 1, 2 as, respectively, inertia weight, cognitive constant, and social constant; and Covariance Matrix Adaptation Evolution Strategy (CMA-ES).. All baselines start tuning from the same point as ours: the trajectory is divided into parts and the regressor predicts initial parameters. Note that the traditional tuning methods based on gradientbased optimization are impractical for this task, given the difficulty to explicitly find the relationship between the parameters of our receding-horizon MPC controller and the tracking performance over the entire maneuver.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

We define the metric of Trajectory Completion (TC) to compare the different approaches. Formally, this metric is defined as: where the indicator function for waypoint i is and t r (i) is the time when the reference τ r predicts the quadrotor to pass the waypoint i. Whenever a waypoint is missed by more than d = 1. 3 m (gate radius for our drone racing experiments) or the drone crashes, the experiment is stopped and the metric calculated. We use this metric in our experiment since it is easy to interpret and can be compared across different experiments.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Tracking Minimum-Time Trajectories", "weight": 1.0} -->

We first evaluate the performance of AutoTune compared to the baselines. The results are summarized in Table I. AutoTune is consistently the best across all maneuvers. For easy maneuvers, e.g. the slow circle or the flip, almost any controller configurations can complete the track, and all methods can find a viable solution. However, for more difficult maneuvers, the gap between our approach and the baselines widens, reaching up to 90% in the Spiral track. On the most difficult tracks, the Bayesian baseline has difficulties fitting the optimization function, while PSO generally gets stuck into a local minimum after few samples. Given enough samples, CMA-ES achieves very good results, with the exception of the Spiral trajectory, where it consistently fails to pass through the second gate.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Tracking Minimum-Time Trajectories", "weight": 1.0} -->

| Team | Qualification Round | Qualification Round | Qualification Round | Final Round | Final Round | Final Round | Fig. 5: Comparison between AutoTune and a set of human experts on the Qualifier track (Fig. 4) in simulation. Despite having access to more information than AutoTune, no human was able to find suitable parameters.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Tracking Minimum-Time Trajectories", "weight": 1.0} -->

Fig. 5 shows the comparison between the tuning performance of AutoTune and four human experts over time. All humans are graduate students expert in quadrotor research and not authors of this paper. They have additional sources of information with respect to our algorithm, i.e. the 3D trajectory flown by the drone. The results show that tuning parameters by hand is extremely challenging for humans, given the nonintuitive relationship between parameters and performance.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Tracking Minimum-Time Trajectories", "weight": 1.0} -->

We additionally compare our approach to the top three methods in the 2019 AirSim Game of Drones competition. We compare the methods both on the qualification and final round of the competition. The results of this experiment are summarized in Table II. On the qualifier track flying AutoTune achieves a lap-time of 24. 05 s, while the winner only reaches the goal in 30. 11 s, with a lap-time 25% longer than ours. Also in the final round, AutoTune outperforms the winner of the competition with a 1. 7 s margin, completing the track in approximately 5% less time. Interestingly, our approach converges to a policy with a maximum speed not necessarily higher than others. However, we achieve an average velocity higher than baselines, and therefore a faster lap-time. This experiment shows that tuning controller parameters with an automated procedure allow quadrotors to fly faster trajectories.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Application in the Real World", "weight": 1.0} -->

AutoTune can be used to tune the controller of a physical platform. To do so, we compute a minimum-time trajectory double Split-S trajectory of 21 waypoints. This trajectory is used to tune the controller in the Flightmare simulator. The resulting controller is then evaluated on a physical platform in a tracking arena of volume 30 × 30 × 8m, where the quadrotor achieves speeds over 50 kmh -1. Figure 6 shows the results of this experiment. AutoTune improves average tracking error by 6% and decreases the maximum displacement from the reference by 12%. In addition, our controller parameters give more consistent performance over multiple runs than the baseline.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Robustness to Changes in Mass, Velocity, and Track Layout", "weight": 1.0} -->

In this section, we study the robustness of the parameters found by AutoTune to changes in drone's mass, flight speed, and track layout. All experiments are made on the Qualifier track. Figure 7 show the results of these experiments. The parameters are overall robust to changes in the quadrotor mass and can complete the task even for very different settings. When changing the maximum speed achieved during flight (Fig. 7-b), we observe that a faster trajectory requires more precise tuning. Finally, we test whether parameters generalize between different maneuvers. To favor generalization, we copy parameters for each segment independently. The results (Fig. 7-c) show that, when the maneuver used for tuning is different from the testing one, the performance generally drops. One possible solution to this problem would be to do automatic fine-grained segmentation of trajectories. Indeed, we hypothesize that smaller trajectory segments, despite being more difficult to optimize, would transfer better between different layouts.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Robustness to Initial Conditions", "weight": 1.0} -->

In this section, we study the evolution of the controller parameters during optimization for different initialization conditions. Specifically, we start the sampling procedure from 3 random initializations and tune the controller with our approach in the Flightmare simulator on the Qualifier track (Fig. 4). Figure 8 shows the results of this experiment. AutoTune finds parameters to reach 100% of trajectory completion for all initial conditions. However, while some require as little as 50 samples, others require up to 1 K to converge. Interestingly, the approach follows different paths in the optimization space for every initialization. In addition, the sampling converges to a different local optimum for each initial condition. This behavior empirically shows that the relationship between parameters and performance at high-speed is multi-modal, i.e. different controller parameters have the same performance. These characteristics of the optimization function represent a challenge for gradient-based and Bayesian methods which tend to converge to the mean between different optima. Conversely, since Metropolis-Hastings sampling can approximate any probability distribution under relatively mild assumptions, our approach does not suffer from the multimodal nature of the optimization function.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Robustness to Initial Conditions", "weight": 1.0} -->

Fig. 6: Results in the real world. After tuning the parameters in simulation, we evaluate the best configuration found by AutoTune on a physical platform. We compare the performance with the parameters tuned by a human. We perform three runs for each parameter set. We also report the error as a function of time (c) for the best run of each approach.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Robustness to Initial Conditions", "weight": 1.0} -->

Fig. 7: Performance analysis when parameters used for tuning (Training) is different to the one used during execution (Testing). Overall, the parameters are robust to imperfect identification of the mass, and the faster the maneuver, the more sensitive the controller is to the parameters. However, the controllers require to be tuned specifically to the maneuver. When the training and testing maneuvers are different, performance generally drops.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Robustness to Initial Conditions", "weight": 1.0} -->

Fig. 8: Robustness to different initial conditions. The parameters' values are divided by their maximum value achieved over all runs. AutoTune converges to a configuration with 100% trajectory completion for all initial conditions. Initialization strongly affects the converge speed. All runs converge to a different optimum, demonstrating the multi-modal characteristic of the optimization function.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Ablation Studies", "weight": 1.0} -->

AutoTune is based on several components to reduce the sample complexity of Metropolis-Hastings sampling. We now validate our design with an ablation study. In particular, we ablate the following components: (i) the use of a regressor for predicting an initial controller to initialize sampling, (ii) the segmentation of the trajectory in different parts. The results in Table III show that all components are important, but some have a larger impact than others. The initial guess produced by the regressor drastically reduces the number of samples to convergence, making the sampler find a solution in 88% less time. However, the most important contribution comes from the trajectory segmentation. Without this component, the sampler cannot find parameters to complete more than 65% of the trajectory in less than 300 samples. This is because global parameters do not allow the controller to dynamically adapt to different parts of the trajectory.

<!-- chunk {"id": "body-0042", "role": "body", "section": "DISCUSSION AND CONCLUSIONS", "weight": 1.5} -->

This paper shows the importance of an automated tuning procedure to fly high-speed maneuvers. While the effect of tuning is less prominent at low speeds, it acquires a fundamental role when the quadrotor flies at the limits of handling. In such cases, the relation between the parameters and flight performance (measured, for example, in terms of trajectory completion or tracking error) is non-convex, not injective, and multi-modal. In this paper, we propose a sampling-based approach specifically tailored to the task of high-speed flight.

<!-- chunk {"id": "body-0043", "role": "body", "section": "DISCUSSION AND CONCLUSIONS", "weight": 1.5} -->

One limitation of the proposed approach is that it does not consider closed-loop stability during optimization. While prior work proposed a series of techniques to guarantee stability during tuning such techniques either require a very accurate model of the platform or very conservative parameters exploration strategies. These makes them suited for tasks like hovering or low-speed flight but not to high-speed flight, where model mismatch makes the parameter's optimization landscape very complex. Similar to previous work on agile flight, we have addressed this problem by tuning the controller exclusively in simulation and directly using the tuned controller on a physical platform. However, such a strategy strongly depends on the quality of the simulation environment. Therefore, combining existing techniques for safe tuning with our approach, to either tune from scratch or only finetune the controller on the physical platform, is a very exciting venue for future work.
