<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Urban Driver: Learning to Drive from Real-world Demonstrations Using Policy Gradients

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this work we are the first to present an offline policy gradient method for learning imitative policies for complex urban driving from a large corpus of real-world demonstrations. This is achieved by building a differentiable data-driven simulator on top of perception outputs and high-fidelity HD maps of the area. It allows us to synthesize new driving experiences from existing demonstrations using mid-level representations. Using this simulator we then train a policy network in closed-loop employing policy gradients. We train our proposed method on 100 hours of expert demonstrations on urban roads and show that it learns complex driving policies that generalize well and can perform a variety of driving maneuvers. We demonstrate this in simulation as well as deploy our model to self-driving vehicles in the real-world. Our method outperforms previously demonstrated state-of-the-art for urban driving scenarios - all this without the need for complex state perturbations or collecting additional on-policy data during training. We make code and data publicly available.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Self-driving has the potential to revolutionize transportation and is a major field of AI applications. Even though already in 1990 there were prototypes capable of driving on highways, technology is still not widespread, especially in the context of urban driving. In the past decade, the availability of large datasets and high-capacity neural networks has enabled significant progress in perception and the vehicles' ability to understand their surrounding environment. Self-driving decision making, however, has seen very little benefit from machine learning or large datasets. State-of-the-art planning systems used in industry still heavily rely on trajectory optimisation techniques with expert-defined cost functions. These cost functions capture desirable properties of the future vehicle path. However, engineering these cost functions scales poorly with the complexity of driving situations and the long tail of rare events.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Due to this, learning a driving policy directly from expert demonstrations is appealing, since performance scales to new domains by adding data rather than via additional human engineering effort. In this paper we focus specifically on learning rich driving policies for urban driving from large amounts of real-world collected data. Unlike highway driving, urban driving requires performing a variety of maneuvers and interactions, e.g., traffic lights, other cars and pedestrians.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, rich mid-level representations powered by large-scale datasets, HD-maps and high-performance perception systems enabled capturing nuances of urban driving. This led to new methods achieving high performance for motion prediction. Furthermore, demonstrated that leveraging these representations and behavioral cloning with state perturbations leads to learning robust driving policies. While promising, difficulty of this approach lies in engineering the perturbation noise mechanism required to avoid covariate shift between training and testing distribution.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inspired by this approach, we present the first results on offline learning of imitating driving policies using mid-level representations, a closed-loop simulator and a policy gradient method. This formulation has several benefits: it can successfully learn high-complexity maneuvers without the need for perturbations, implicitly avoid the problem of covariate shift, and directly optimize imitation as well as auxiliary costs. The proposed simulator is constructed directly from the collected logs of real-world demonstrations and HD maps of the area, and can synthesize new realistic driving episodes from past experiences (see Figure 1 for an overview of our method). Furthermore, for training on large datasets reducing the computational complexity is paramount. We leverage vectorized representations and show how this allows for computing policy gradients quickly using backpropagation through time. We demonstrate how these choices lead to superior performance of our method over the existing state-of-the-art in imitation learning for real-world self-driving planning in urban areas.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The first demonstration of policy gradient learning of imitative driving policies for complex urban driving from a large corpus of real-world demonstrations. We leverage a closed-loop simulator and rich, mid-level vectorized representations to learn policies capable of performing a variety of maneuvers.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A new differentiable simulator that enables efficient closed-loop simulation of realistic driving experiences based on past demonstrations, and quickly compute policy gradients by backpropagation through time, allowing fast learning.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A comprehensive qualitative and quantitative evaluation of the method and its performance compared to existing state-of-the-art. We show that our approach, trained purely in simulation can control a real-world self-driving vehicle, outperforms other methods, generalizes well and can effectively optimize both imitation and auxiliary costs.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Source code and data are made available to the public^11^1Code and video available at

<!-- chunk {"id": "body-0011", "role": "body", "section": "Data-driven simulation", "weight": 1.0} -->

A realistic simulator is useful for both training and validation of ML models. However, many current simulators (e.g. ) depend on heuristics for vehicle control and do not capture the diversity of real world behaviours. Data-driven simulators are designed to alleviate this problem. created a photo-realistic simulator for training an end-to-end RL policy. simulated a bird's-eye view of dense traffic on a highway. Finally, two recent works developed data-driven simulators and showed their usefulness for training and validating ML planners. In this work we show that a simpler, differentiable simulator based on replaying logs is effective for training.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Differentiable Traffic Simulator from Real-world Driving Data", "weight": 1.0} -->

In this section we describe a differentiable simulator $S$ that approximates new driving experiences based on an experience $\overline{\tau}$ collected in the real world. This simulator is used during policy learning for the closed-loop evaluation of the current policy's performance and computing the policy gradient. As shown in Section 5, differentiability is an important building block for achieving good results, especially when employing auxiliary costs.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Differentiable Traffic Simulator from Real-world Driving Data", "weight": 1.0} -->

We use a vectorized representation based, in which each state observation ${\overline{s}}_{t}$ consists of a collection of static and dynamic elements $e_{t}^{1},e_{t}^{2},\ldots,e_{t}^{K}$ around the vehicle pose ${\overline{p}}_{t} \in {SE_{2}}$, with $SE_{2}$ denoting the special Euclidean group. Static elements include traffic lanes, stop signs and pedestrian crossings. These elements are extracted from the underlying HD semantic map of the area using the localisation system. The dynamic elements include traffic lights status and traffic participants (other cars, buses, pedestrians and cyclists). These are detected in real-time using the on-board perception system.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Differentiable Traffic Simulator from Real-world Driving Data", "weight": 1.0} -->

Each element $e_{t}^{j}$ includes a pose $q_{t}^{j} \in {SE_{2}}$ relative to the SDV pose $p_{t}$, as well as additional features, such as the element type, time of observation, and other optional attributes, e.g. the color of associated traffic lights, recent history of moving vehicles, etc. The full details of this representation are provided in Appendix C.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Differentiable Traffic Simulator from Real-world Driving Data", "weight": 1.0} -->

Goal of the simulation is to iteratively generate a sequence of state observations $\tau = {\{ s_{1},s_{2},\ldots,s_{T}\}}$ that corresponds to a different sequence of driver actions $a_{1},a_{2},\ldots,a_{N}$ in the scenario. This is done by first computing the corresponding SDV trajectory $p_{1},p_{2},\ldots,p_{N}$ and then locally transforming states ${\overline{s}}_{1},{\overline{s}}_{2},\ldots,{\overline{s}}_{N}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Differentiable Traffic Simulator from Real-world Driving Data", "weight": 1.0} -->

Updated poses of the SDV are determined by a kinematic model $p_{t + 1} = {f{(p_{t},a_{t})}}$, which is assumed to be differentiable.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Differentiable Traffic Simulator from Real-world Driving Data", "weight": 1.0} -->

See Figure 2 for an illustrative example. It is worth noting that this approximation is effective if the distance between the original and generated SDV pose is not too large.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Differentiable Traffic Simulator from Real-world Driving Data", "weight": 1.0} -->

We denote performing these steps in sequence with the step-by-step simulation transition function $s_{t + 1} = {S{(s_{t},a_{t})}}$. Moreover, since both Equation and vehicle dynamics $f$ are fully differentiable, we can compute gradients with respect to both the state ($S_{s}$) and action ($S_{a}$). This is critical for the efficient computation of policy gradients using backpropagation through time as described in the next section.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Imitation Learning Using a Differentiable Simulator", "weight": 1.0} -->

In this part, we detail how we use the simulator $S$ described in the previous section to learn a deterministic policy $\pi$ to drive a car using closed-loop policy learning.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Imitation Learning Using a Differentiable Simulator", "weight": 1.0} -->

We frame the imitation learning problem as minimisation of the L1 pose distance ${L{(s_{t},a_{t})}} = {\|{{\overline{p}}_{t} - p_{t}}\|}_{1}$ between the expert and learner on a sequence of collected real-world demonstrations ${{\overline{\tau}}_{1},{\overline{\tau}}_{2},\ldots,{\overline{\tau}}_{N}} \sim \pi_{E}$. Note that with a slight abuse of notation we use the poses ${\overline{p}}_{t},p_{t}$ here to refer to 3D vectors $(x,y,\theta)$, instead of roto-translation matrices in $SE_{2}$ -- yielding the common L1 norm and loss.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Imitation Learning Using a Differentiable Simulator", "weight": 1.0} -->

Optimising this objective pushes the trajectory taken by the learned policy as close as possible to the one of the expert, as well as limiting the trajectory to the region where the approximation given by the simulator is effective. In Appendix B we further extend this to include auxiliary cost functions with the aim of optimising additional objectives.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Imitation Learning Using a Differentiable Simulator", "weight": 1.0} -->

We can use any policy optimisation method to optimize Equation. However, given that the transition $S{(s_{t},a_{t})}$ is differentiable, we can exploit it for a more effective training that does not require a separate estimation of a value function. As shown, this results into an order of magnitude more efficient training. The optimisation process consists of repeatedly sampling pairs of expert and policy trajectories ${\overline{\tau}}_{i}$, $\tau_{i}$ and computing the policy gradient $J_{\theta}$ for these samples to minimize Equation. We describe both steps in detail in the following subsections.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Sampling from a Policy Distribution $\\pi$", "weight": 1.0} -->

Algorithm 1 Imitation learning from expert demonstrations

<!-- chunk {"id": "body-0024", "role": "body", "section": "Sampling from a Policy Distribution $\\pi$", "weight": 1.0} -->

In this subsection we detail sampling pairs of expert ($\overline{\tau}$) and corresponding policy trajectory ($\tau$) drawn from policy $\pi$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Sampling from a Policy Distribution $\\pi$", "weight": 1.0} -->

Sampling expert trajectories $\overline{\tau}$ consists of simply sampling from the collected dataset of expert demonstrations. To generate the policy sample $\tau$ we acquire an expert state ${\overline{s}}_{1} \in \overline{\tau}$, and then unroll the current policy $\pi$ for $T$ steps using the simulator $S$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Sampling from a Policy Distribution $\\pi$", "weight": 1.0} -->

This naive method, however, introduces bias, as the initial state of the trajectory is always drawn from the expert $\pi_{E}$ and not from the policy distribution $\pi$. As shown in Appendix B, this results in the under-performance of the method. To remove this bias we discard the first $K$ timesteps from both trajectories and use only the remaining $T - K$ timesteps to estimate the policy gradient $J_{\theta}$ as described next (see Figure 3 for a visualization).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Computing Policy Gradient $J_{\\theta}$", "weight": 1.0} -->

Here we describe the computation of the policy gradient $J_{\theta}$ around the rollout trajectory $\tau = {s_{1},a_{1},s_{2},a_{2},\ldots,s_{T},a_{T}}$ given by the current policy. This gradient can be computed for deterministic policies $\pi$ using backpropagation through time leveraging the differentiability of the simulator $S$. Note that we denote partial differentiation with subscripts, i.e. $g_{x} \triangleq {\partial{{g{(x,\ldots)}}/{\partial{(x)}}}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Computing Policy Gradient $J_{\\theta}$", "weight": 1.0} -->

The resulting algorithm is outlined in Algorithm 1 and illustrated in Figure 3. It can be implemented simply as one forward pass of length $T$ and one backward pass of length $T - K$. To compute the policy gradient we use equations and recursively from $t = T$ to $t = K$ and use it to update policy parameters $\theta$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section we evaluate our proposed method and benchmark it against existing state-of-the-art systems. In particular, we are interested: its ability to learn robust policies dealing with various situations observed in the real world; its ability to tailor performance using auxiliary costs; the sensitivity of key hyper-parameters; and the impact on performance with increasing amounts of training data. Additional results can be found in the appendix and the accompanied video.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Dataset", "weight": 1.0} -->

For training and testing our models we use the Lyft Motion Prediction Dataset. This dataset was recorded by a fleet of Autonomous Vehicles and contains samples of real-world driving on a complex, urban route in Palo Alto, California. The dataset captures various real-world situations, such as driving in multi-lane traffic, taking turns, interactions with vehicles at intersections, etc. Data was preprocessed by a perception system, yielding the precise position of nearby vehicles, cyclists and pedestrians over time. In addition, a high-definition map provides locations of lane markings, crosswalks and traffic lights. All models are trained on a 100h subset, and tested on 25h. The training dataset is identical to the publicly available one, whereas for the sake of execution speed for testing we use a random, but fixed, subset of the listed test dataset, which is roughly $\frac{1}{4}$ in size.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Baselines", "weight": 1.0} -->

Naive Behavioral Cloning (*BC*): we implement standard behavioral cloning using our vectorized backbone architecture. We do not use the SDV's history as an input to the model to avoid causal confusion (compare ).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Baselines", "weight": 1.0} -->

Behavioral Cloning + Perturbations (*BC-perturb*): we re-implement a vectorized version of ChauffeurNet using our backbone network. As in the original paper, we add noise in the form of perturbations during training, but do not employ any auxiliary losses. We test two versions: without the SDV's history, and using the SDV's history equipped with history dropout.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Baselines", "weight": 1.0} -->

Multi-step Prediction (*MS Prediction*): we apply the meta-learning framework proposed in to train our vectorized network. We observe that a version of this algorithm can conveniently be expressed within our framework; we obtain it by explicitly detaching gradients between steps (i.e. ignoring the full differentiability of our simulation environment). Differently from the original work, we do not save past unrolls as new dataset samples over time.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Implementation", "weight": 1.0} -->

Inspired, we use a graph neural network for parametrizing our policy. It combines a PointNet-like architecture for local inputs processing followed by an attention mechanism for global reasoning. In contrast to, we use points instead of vectors. Given the set of points corresponding to each input element, we employ 3 PointNet layers to calculate a 128-dimensional feature descriptor. Subsequently, a single layer of scaled dot-product attention performs global feature aggregation, yielding the predicted trajectory. We found $K = 20$ and $T = 32$ to work well, i.e. we use 20 timesteps for the initial sampling and effectively predict 12 trajectory steps. $\gamma$ is set to 0.8. In total, our model contains around 3.5 million trainable parameters, and training takes 30h on 32 Tesla V100 GPUs. For more details we refer to Appendix C.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Implementation", "weight": 1.0} -->

For the vehicle kinematics model $f$ we use an unconstrained model $p_{t + 1} = {p_{t} + a_{t}}$ with $a_{t} \in {SE_{2}}$. This allows for a fair comparisons with the baselines as both BC-perturb and MS Prediction assume the possibility of arbitrary pose corrections. Other kinematics models, such as unicycle or bicycle models, could be used with our method as well.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Implementation", "weight": 1.0} -->

All baseline methods share the same network backbone as ours, with model specific differences as described above -- and BC and BC-perturb predicting a full T-step trajectory with a single forward, while MS Prediction and ours are calling the model $T$ times. To ensure a fair comparison, also for MS Prediction we use our proposed sampling procedure, i.e. use the first $K$ steps for sampling only. We train all models for 61 epochs with a learning rate of $10^{- 4}$, and drop it to $10^{- 5}$ after 54 epochs. We note that we achieve best results for our proposed method by disabling dropout, and hypothesize this is related to similar issues observed for RNNs.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Implementation", "weight": 1.0} -->

We refer the reader to Appendix B for ablations on the influence on data and sampling.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Metrics", "weight": 1.0} -->

We implement the metrics describe below to evaluate the planning performance. These capture key imitation performance, safety and comfort.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Metrics", "weight": 1.0} -->

L2: L2 distance to the underlying expert position in the driving log in meters.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Metrics", "weight": 1.0} -->

Off-road events: we report a failure if the planner deviates more than 2m laterally from the reference trajectory -- this captures events such as running off-road and into opposing traffic.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Metrics", "weight": 1.0} -->

Collisions: collisions of the SDV with any other agent, broken down into front, side and rear collisions w.r.t. the SDV.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Metrics", "weight": 1.0} -->

Comfort: we monitor the absolute value of acceleration, and raise a failure should this exceed 3 m/s^2^.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Metrics", "weight": 1.0} -->

I1K: we accumulate safety-critical failures (collisions and off-road events) into one key metric for ease of comparison, namely *Interventions per 1000 Miles* (I1K).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Imitation Results", "weight": 1.0} -->

We evaluate our method and all the baselines by unrolling the policy on 3600 sequences of 25 seconds length from the test set and measure the above metrics.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Imitation Results", "weight": 1.0} -->

Table 1 reports performance when all methods are trained to optimize the imitation loss alone. Behavioral cloning yields a high number of trajectory errors and collisions. This is expected, as this approach is known to suffer from the issue of covariate shift. Including perturbation during training dramatically improves performance as it forces the method to learn how to recover from drifting. We further observe that MS Prediction yields comparable results for many categories, while yielding less rear collisions. We attribute this to the further reduction of covariate shift when compared to the previous methods: the training distribution is generated on-policy instead of being synthesized by adding noise. Finally, our method yields best results overall. It is worth noting that all models share a high number of comfort failures, due to the fact that they are all trained for imitation performance alone, which does not optimize for comfort, but only positional accuracy of the driven vehicle -- which we address in the appendix.

<!-- chunk {"id": "body-0046", "role": "body", "section": "In-car Testing", "weight": 1.0} -->

In addition to above stated simulation results, we further deployed our planner on SDVs in the real. For this, a Ford Fusion equipped with 7 camera, 3 LiDAR and 11 Radar sensors was employed. The sensor setup thus equals the one used for data collection, and during road-testing our perception and data-processing stack is run in real-time to generate the desired scene representation on the fly. For this, vehicles are equipped with 8 Nvidia 2080 TIs. Experiments were conducted on a private test track, including other traffic participants and reproducing challenging driving scenarios. Furthermore, this track was never shown to the network before, and thus offers valuable insights into generalization performance. Figure 5 shows our model successfully crossing a signaled intersection, for more results we refer to the appendix and our supplementary video.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work we have introduced a method for learning an autonomous driving policy in an urban setting, using closed-loop training, mid-level representations with a data-driven simulator and a large corpus of real world demonstrations. We show this yields good generalization and performance for complex, urban driving. In particular, it can control a real-world self-driving vehicle, yielding better driving performance than other state-of-the-art ML methods.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We believe this approach can be further extended towards production-grade real-world driving requirements of L4 and L5 systems -- in particular, for improving performance in novel or rarely seen scenarios and to increase sample efficiency, allowing further scaling to millions of hours of driving.
