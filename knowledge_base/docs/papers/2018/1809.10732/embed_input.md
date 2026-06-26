<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Multimodal Trajectory Predictions for Autonomous Driving Using Deep Convolutional Networks

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous driving presents one of the largest problems that the robotics and artificial intelligence communities are facing at the moment, both in terms of difficulty and potential societal impact. Self-driving vehicles (SDVs) are expected to prevent road accidents and save millions of lives while improving the livelihood and life quality of many more. However, despite large interest and a number of industry players working in the autonomous domain, there still remains more to be done in order to develop a system capable of operating at a level comparable to best human drivers. One reason for this is high uncertainty of traffic behavior and large number of situations that an SDV may encounter on the roads, making it very difficult to create a fully generalizable system. To ensure safe and efficient operations, an autonomous vehicle is required to account for this uncertainty and to anticipate a multitude of possible behaviors of traffic actors in its surrounding. We address this critical problem and present a method to predict multiple possible trajectories of actors while also estimating their probabilities. The method encodes each actor's surrounding context into a raster image, used as input by deep convolutional networks to automatically derive relevant features for the task.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Following extensive offline evaluation and comparison to state-of-the-art baselines, the method was successfully tested on SDVs in closed-course tests.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent years have witnessed unprecedented progress in Artificial Intelligence (AI) applications, with smart algorithms rapidly becoming an integral part of our daily lives. The AI methods are used by hospitals to help diagnose diseases, matchmaking services are using learned models to connect potential couples, and social media feeds are built by algorithmic approaches, to name just a few affecting millions of people. Nevertheless, despite huge strides the AI revolution is far from over, and is likely to further accelerate in the coming years. Interestingly, one of the major industries mostly undisturbed by the ongoing progress is the automobile domain, where thus far AI has seen limited use. Large car-makers made some advances by using AI within Advanced Driver-Assistance Systems (ADAS), however, its full power remains to be harnessed through the advent of new smart technologies, such as self-driving vehicles (SDVs).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Driving a vehicle in traffic is a surprisingly dangerous task considering it is such a common activity of many, even for human drivers with several years of experience. While the car manufacturers are working hard on improving vehicle safety through better design and ADAS systems, grim year-to-year statistics indicate that there is still a lot more to be done in order to revert the negative trends observed on public roads. In particular, car accidents amounted to more than $5\%$ of deaths in the US in 2015, with the human factor to blame in the vast majority of the crashes. This is unfortunately not a recent problem, and researchers have been trying to understand the reasons and causes for several decades. Studies include investigating effect of driver distractions, alcohol and drug use, and driver's age among other factors, as well as how to most effectively impact drivers' behavior accepting that they are fallible. Not surprisingly, a common theme in the existing body of literature is that humans are the most unreliable part of the traffic system, which could be mitigated through the development and wide adoption of SDVs.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This prospect is made possible by the latest breakthroughs in hardware and software technologies, opening doors for the fields of robotics and AI to potentially make their greatest societal impact yet.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Self-driving technology has been under development for a long time, with the earliest attempts going as far back as the 1980s and the work on ALVINN. However, only recently the technological advances reached a point where wider use could be possible, as exemplified by the results of 2007 DARPA Urban Challenge. Here, the participating teams were required to navigate complex urban surroundings and handle conditions commonly encountered on public roads, as well as interact with human- and robot-driven vehicles. These early successes spurred large interest in the autonomous domain that we see today, and a number of industry players (such as Uber or Waymo) and governmental bodies are racing to set up technological and legal scaffolding for SDVs to become a reality. Nevertheless, despite the progress achieved thus far, there remains more to be done to make SDVs operate at the human level and fully commercialize them.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To safely and effectively operate in the real world, a critical piece of the autonomous puzzle is to correctly predict movement of surrounding actors, and a successful system also needs to account for their inherent multimodal nature. We focus on this task and build upon our deployed deep learning-based work, which creates bird's-eye view (BEV) rasters encoding high-definition map and surroundings to predict actor's future, and present the following contributions: we extend the state-of-the-art and propose a method that goes beyond inferring a single trajectory, and instead reasons about multiple trajectories and their probabilities; following extensive offline study of multi-hypothesis methods, the proposed method was successfully tested onboard SDVs in closed-course tests.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Illustrative examples of how multimodality of future $6$-second trajectories is captured by our model are shown in Figure 1. The method uses rasterized vehicle context (including the high-definition map and other actors) as a model input to predict actor's movement in a dynamic environment. As the vehicle is approaching the intersection the multimodal model (where we set the number of modes to $2$) estimates that going straight has slightly less probability than a right turn, see Figure 1a. After three timesteps the vehicle continued to move straight, at which point probability of right turn drops significantly (Figure 1c); note that in actuality the vehicle continued going straight through the intersection. We can see that a single-modal model is not capable of capturing multimodality of the scene, and instead roughly predicts mean of the two modes, as illustrated in Figures 1b and 1d.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Actor motion prediction in self-driving systems", "weight": 1.0} -->

Most of the deployed self-driving systems use well-established engineered approaches for actors' motion prediction. The common approach consists of computing object's future motion by propagating its state over time based on assumptions of underlying physical system and using techniques such as Kalman filter (KF). While this approach works well for short-term predictions, its performance degrades for longer horizons as the model ignores surrounding context (e.g., roads, other actors, traffic rules). Addressing this issue, method proposed by Mercedes-Benz uses map information as a constraint to compute vehicle's future position at longer term. The system first associates each detected vehicle with one or more lanes from the map. Then, all possible paths are generated for each (vehicle, associated lane) pair based on map topology, lane connectivity, and vehicle's current state estimate. This heuristic provides reasonable predictions in common cases, however it is sensitive to errors in association of vehicles and lanes. As an alternative to existing deployed engineered approaches, the proposed method automatically learns from the data that vehicles typically obey road and lane constraints, while generalizing well to various situations observed on the roads. In addition, we propose an extension of our method that incorporates existing lane-association ideas.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-B Machine-learned prediction models", "weight": 1.0} -->

Manually engineered models fail to scale to many different traffic scenarios, which motivated the use of machine learning models as alternatives, such as Hidden Markov Model, Bayesian networks, or Gaussian Processes. In recent work researchers focused on how to model environmental context using Inverse Reinforcement Learning (IRL). Kitani et al. used inverse optimal control to predict pedestrian paths by considering scene semantics, however the existing IRL methods are inefficient for real-time applications.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Machine-learned prediction models", "weight": 1.0} -->

There exists a number of studies addressing the problem of modeling multimodality. Mixture Density Networks (MDNs) are conventional neural networks which solve multimodal regression tasks by learning parameters of a Gaussian mixture model. However, MDNs are often difficult to train in practice due to numerical instabilities when operating in high-dimensional spaces. To overcome this problem researchers proposed training an ensemble of networks, or a single network to produce $M$ different outputs for $M$ different hypotheses using a loss that only accounts for the closest prediction to ground truth labels. Due to good empirical results our work builds upon these efforts. Furthermore, in the authors introduced a method for multimodal trajectory prediction for highway vehicles by learning a model that assigns probabilities to six maneuver classes. The approach requires a predefined discrete set of possible maneuvers, which may be hard to define for complex city driving. Alternatively, in the authors proposed to generate multimodal predictions through sampling, which requires repeated forward passes to generate multiple trajectories. On the other hand, our proposed approach computes multimodal predictions directly, in a single forward-pass of a CNN model.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Proposed approach", "weight": 1.0} -->

In this section we discuss the proposed method for predicting multimodal trajectories of traffic actors. We introduce the problem setting and notation, followed by the discussion of our CNN architecture and the considered loss functions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Problem setting", "weight": 1.0} -->

Let us assume that we have access to real-time data streams coming from sensors such as lidar, radar, or camera, installed aboard a self-driving vehicle. In addition, assume that these inputs are used by an existing detection and tracking system, outputting state estimates $\mathcal{S}$ for all surrounding actors (state comprises the bounding box, position, velocity, acceleration, heading, and heading change rate). Denote a set of discrete times at which tracker outputs state estimates as $\mathcal{T} = {\{ t_{1},t_{2},\ldots,t_{T}\}}$, where time gap between consecutive time steps is constant (e.g., the gap is equal to $0.1s$ for tracker running at a frequency of $10Hz$).

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Problem setting", "weight": 1.0} -->

Then, we denote state output of a tracker for the $i$-th actor at time $t_{j}$ as $\mathbf{s}_{ij}$, where $i = {1,\ldots,N_{j}}$ with $N_{j}$ being a number of unique actors tracked at $t_{j}$. Note that in general the actor counts vary for different time steps as new actors appear within and existing ones disappear from the sensor range. Moreover, we assume access to detailed, high-definition map information $\mathcal{M}$ of the SDV's operating area, including road and crosswalk locations, lane directions, and other relevant map information.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Modeling multimodal trajectories", "weight": 1.0} -->

Following our previous work, we first rasterize an actor-specific BEV raster image encoding the actor's map surrounding and neighboring actors (e.g., other vehicles and pedestrians), as exemplified in Figure 1. Then, given $i$-th actor's raster image and state estimate $\mathbf{s}_{ij}$ at time step $t_{j}$, we use a CNN model to predict a multitude of $M$ possible future state sequences ${\{{\lbrack{\overset{\sim}{\mathbf{s}}}_{im{({j + 1})}},\ldots,{\overset{\sim}{\mathbf{s}}}_{im{({j + H})}}\rbrack}\}}_{m = {1,\ldots,M}}$, as well as each sequence's probability $p_{im}$ such that ${\sum_{m}p_{im}} = 1$, where $m$ indicates mode index and $H$ denotes the number of future

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B Modeling multimodal trajectories", "weight": 1.0} -->

consecutive time steps for which we predict states (or prediction horizon).

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Modeling multimodal trajectories", "weight": 1.0} -->

For a detailed description of the rasterization method, we refer the reader to our previous work. Without the loss of generality, in this work we simplify the task to infer $i$-th actor's future $x$- and $y$-positions instead of full state estimates, while the remaining states can be derived by considering $\mathbf{s}_{ij}$ and the future position estimates. Both past and future positions at time $t_{j}$ are represented in the actor-centric coordinate system derived from actor's state at time $t_{j}$, where forward direction is $x$-axis, left-hand direction is $y$-axis, and actor's bounding box centroid is the origin.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Modeling multimodal trajectories", "weight": 1.0} -->

The proposed network is illustrated in Figure 2. It takes an actor-specific $300 \times 300$ RGB raster image with $0.2m$ resolution and actor's current state (velocity, acceleration, and heading change rate) as input, and outputs $M$ modes of future $x$- and $y$-positions ($2H$ outputs per mode) along with their probabilities (one scalar per mode). This results in ${({{2H} + 1})}M$ outputs per actor. Probability outputs are passed through a softmax layer to ensure they sum to $1$. Note that any CNN architecture can be used as the base network; following results in we use MobileNet-v2.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-C Multimodal optimization functions", "weight": 1.0} -->

In this section we discuss loss functions that we proposed to model the inherent multimodality of the trajectory prediction problem. First, let us define a single-mode loss $L$ of the $i$-th actor's $m$-th mode at time $t_{j}$ as average displacement error (or $\ell_{2}$-norm) between the points of ground-truth trajectory ${\mathbf{τ}}_{ij}$ and predicted trajectory of the $m$-th mode ${\overset{\sim}{\mathbf{τ}}}_{imj}$, where $\tau_{ij}^{h}$ and ${\overset{\sim}{\tau}}_{imj}^{h}$ are $2$-D vectors representing $x$- and $y$-positions at horizon $h$ of ${\mathbf{τ}}_{ij}$ and ${\overset{\sim}{\mathbf{τ}}}_{imj}$, respectively.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-C Multimodal optimization functions", "weight": 1.0} -->

One straightforward multimodal loss function we can use is the *Mixture-of-Experts* (ME) loss, defined as corresponding to the expected displacement loss. However, as shown by our evaluation results in Section IV, the ME loss is not suitable for the trajectory prediction problem due to the mode collapse problem. To address this issue, we propose to use a novel *Multiple-Trajectory Prediction* (MTP) loss, motivated, that explicitly models the multimodality of the trajectory space. In the MTP method, for the $i$-th actor at time $t_{j}$ we first run the forward pass of the neural network to obtain $M$ output trajectories.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-C Multimodal optimization functions", "weight": 1.0} -->

We then identify mode $m^{\ast}$ that is closest to the ground-truth trajectory according to an arbitrary trajectory distance function $dist{({\mathbf{τ}}_{ij},{\overset{\sim}{\mathbf{τ}}}_{imj})}$, After selecting the best matching mode $m^{\ast}$, the final loss function can be defined as follows, where $I_{c}$ is a binary indicator function equal to $1$ if the condition $c$ is true and 0 otherwise, $\mathcal{L}_{ij}^{class}$ is a classification cross-entropy loss defined as follows, and $\alpha$ is a hyper-parameter used to trade-off the two losses. In other words, we force the probability of the best matching mode $m^{\ast}$ to be as close as possible to $1$, and push probabilities of the other modes to $0$. Note that during training the position outputs are updated only for the winning mode, while the probability outputs are updated for all the modes.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Multimodal optimization functions", "weight": 1.0} -->

This causes each mode to specialize for a distinct class of actor behavior (e.g., going straight or turning), and successfully addresses the mode collapse problem as shown later in the experiments.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C Multimodal optimization functions", "weight": 1.0} -->

Lastly, for both losses and we train the CNN parameters $\theta$ to minimize loss over the training data, Note that that our multimodal loss functions are agnostic to the choice of the per-mode loss function $L{({\mathbf{τ}}_{ij},{\overset{\sim}{\mathbf{τ}}}_{imj})}$, and it is straightforward to extend our method to predict trajectory point uncertainties by using the negative Gaussian log-likelihood, as proposed.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-D Lane-following multimodal predictions", "weight": 1.0} -->

Previously we described an approach that explicitly predicts multiple modes in a single forward pass. Following approach in where each vehicle is associated to a lane (referred to as a lane-following vehicle), we propose a method that implicitly outputs multiple trajectories. In particular, assuming a knowledge of the possible lanes that can be followed and a lane-scoring system that filters unlikely lanes, we add another rasterization layer that encodes this information and train the network to output a lane-following trajectory. Then, for one scene we can generate multiple rasters with various lanes to be followed, effectively inferring multiple trajectories. To generate training data we first identify lanes that a vehicle actually followed and use that information to create input rasters. We then train the Lane-Following (LF) model using the losses introduced previously by setting $M = 1$ (ME and MTP are equal in that case). In practice, LF and other approaches can be used together, separately processing lane-following and remaining actors, respectively.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-D Lane-following multimodal predictions", "weight": 1.0} -->

Note that we introduce this approach solely for completeness, as practitioners may find it useful to combine our rasterization ideas with the existing deployed lane-following approaches to obtain multimodal predictions, as described.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-D Lane-following multimodal predictions", "weight": 1.0} -->

In Figure 4 we show rasters for the same scene but using two different following lanes marked in light pink, one going straight and one turning left. The method outputs trajectories that follow the intended paths well, and can be used to generate multitude of trajectories for lane-following vehicles.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments", "weight": 1.0} -->

We collected 240 hours of data by manually driving SDV in Pittsburgh, PA and Phoenix, AZ in various traffic conditions (e.g., varying times of day, days of the week). Traffic actors were tracked using Unscented Kalman filter (UKF) with kinematic vehicle model, taking raw sensor data from the camera, lidar, and radar and outputting state estimates for each tracked vehicle at the rate of $10Hz$. The filter is highly optimized and trained on a large amount of labeled data, and has been extensively tested on large-scale, real-world data. Each actor at each discrete tracking time step amounts to a single data point, with overall data comprising $7.8$ million data points after removing static actors. We considered prediction horizon of $6$ seconds (i.e., $H = 60$), set $\alpha = 1$, and used $3$:$1$:$1$ split to obtain train/validation/test data.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

We compared the proposed methods to several baselines: UKF that forward propagates estimated state in time; Single-trajectory predictor (STP); MDN, as Gaussian mixture over trajectory space, where ${\overset{\sim}{\mathbf{\Sigma}}}_{imj}^{h}$ is a $2 \times 2$ covariance matrix measuring uncertainty at horizon $h$, inferred by the network.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

The models were implemented in TensorFlow and trained on 16 Nvidia Titan X GPU cards. We used open-source distributed framework Horovod for training, completing in around 24 hours. We used a per-GPU batch size of $64$ and trained with Adam optimizer, setting initial learning rate to $10^{- 4}$ further decreased by a factor of $0.9$ every 20 thousand iterations. All models were trained end-to-end from scratch, and deployed to an SDV with a GPU onboard performing batch inference in about $10ms$ on average.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Empirical results", "weight": 1.0} -->

We compare the considered methods using error metrics relevant for motion prediction: displacement, as well as along- and cross-track errors measuring longitudinal and lateral deviation from the ground truth, respectively. As multimodal approaches provide probabilities, one possible evaluation setup is to use prediction error of the most probable mode. However, earlier work on multimodal predictions found that such metric favors single-modal models as they explicitly optimize for the averaged prediction error, while outputting unrealistic trajectories (see examples in Figure 1). Mirroring an existing setup from and, we filter out low-probability trajectories (we set the threshold to $0.2$) and use a lowest-error mode from the remaining set to compute a metric. We found results computed in this way to be more aligned with an observed performance onboard an SDV.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Empirical results", "weight": 1.0} -->

In Table I we report errors at horizons of $1s$ and $6s$, as well as the averaged metrics over the entire prediction horizon for different numbers of modes $M$ (we vary the mode count from $2$ to $4$). First, we can see that single-mode models (i.e., UKF and STP) are clearly not suitable for longer-term predictions. While their short-term predictions at $1$ second are reasonable, $6s$-horizon errors are significantly worse than the best multimodal approaches. This is not unexpected, as in the short term traffic actors are constrained by physics and their immediate surroundings, which results in near-unimodal distribution of the ground truth. On the other hand, at longer horizons multimodality of the prediction problem becomes much more apparent (e.g., as an actor is approaching an intersection there are several discrete choices that they can make given exactly the same scene). Single-modal predictions fail to properly account for that and instead predict a distribution mean, as illustrated in Figure 1.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Empirical results", "weight": 1.0} -->

Furthermore, it is interesting to note that MDN and ME gave similar results as STP for a variety of $M$ values. The reason is a well-known problem of mode collapse, where only a single mode provides non-degenerate predictions. Thus, in practice an affected multimodal method falls back to being unimodal, failing to fully capture multiple modes. Authors of reported this issue for MDNs and found multi-hypothesis models to be less affected, as confirmed by our results.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Empirical results", "weight": 1.0} -->

Shifting our focus to the MTP methods, we observe significant improvements over the competing approaches. Both average and $6s$-horizon errors dropped across the board, indicating that the methods are capturing the multimodal nature of the traffic problem. Prediction errors at both short-term $1s$- and long-term $6s$-horizon are lower than for the other methods, although the benefit is greater at longer prediction horizons. Interestingly, the results show that the best performance on all metrics is achieved with $M = 3$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Empirical results", "weight": 1.0} -->

Next, we evaluated different trajectory distance measures for selecting the best matching mode during the MTP training. Table I shows that using displacement as a distance function gives slightly better performance than using angle. However, in order to better understand implications of this choice, we sliced the testing data samples into three categories: turning left, turning right, and going straight ($95\%$ of the test cases are actors going roughly straight, with the remainder evenly split between turns), and report results for $6s$-horizon in Table II. We can see that using angle improved handling of turns, with a very slight degradation of going-straight cases. This confirms our hypothesis that the angle matching policy improves the performance at intersections, which is critical to the safety of an autonomous vehicle. Considering these results, in the remainder of the section we use the MTP model with the angle mode selection policy.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Empirical results", "weight": 1.0} -->

Lastly, we analyzed calibration of the predicted mode probabilities. In particular, using test data we computed the relationship between predicted mode probability and likelihood that the mode is the best matching one to the ground-truth trajectory (i.e., that the mode is equal to $m^{\ast}$ as defined in equation ). We bucketed the trajectories according to their predicted probability and computed the average mode-matching likelihood for each bucket. Figure 6 gives the result when we use $M = 3$, while results for other values of $M$ resemble the ones shown. We can see that the plot closely follows the $y = x$ reference line, indicating the predicted probabilities are well-calibrated.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Due to the inherent uncertainty of traffic behavior, autonomous vehicles need to consider multiple possible future trajectories of the surrounding actors in order to ensure a safe and efficient ride. In this work, we addressed this critical aspect of the self-driving problem and proposed a method to model the multimodality of vehicle movement prediction. The approach first generates a raster image encoding surrounding context of each vehicle actor and uses a CNN model to output several possible trajectories along with their probabilities. We discussed several multimodal models and compared to the current state-of-the-art methods, with the results strongly suggesting practical benefits of the proposed approach. Following extensive offline evaluation, the method was successfully tested onboard SDVs in closed-course tests.
