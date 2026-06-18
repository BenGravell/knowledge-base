<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SafetyNet: Safe Planning for Real-world Self-driving Vehicles Using Machine-learned Policies

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we present the first safe system for full control of self-driving vehicles trained from human demonstrations and deployed in challenging, real-world, urban environments. Current industry-standard solutions use rule-based systems for planning. Although they perform reasonably well in common scenarios, the engineering complexity renders this approach incompatible with human-level performance. On the other hand, the performance of machine-learned (ML) planning solutions can be improved by simply adding more exemplar data. However, ML methods cannot offer safety guarantees and sometimes behave unpredictably. To combat this, our approach uses a simple yet effective rule-based fallback layer that performs sanity checks on an ML planner's decisions (e.g. avoiding collision, assuring physical feasibility). This allows us to leverage ML to handle complex situations while still assuring the safety, reducing ML planner-only collisions by 95%. We train our ML planner on 300 hours of expert driving demonstrations using imitation learning and deploy it along with the fallback layer in downtown San Francisco, where it takes complete control of a real vehicle and navigates a wide variety of challenging urban driving scenarios.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Self-Driving Vehicles (SDVs) have the promise to revolutionize several industries including people and goods transportation. However, the development of L4+ SDVs has proved to be a significant challenge. Today, the main bottleneck is the vehicle's ability to safely handle the 'long tail' of driving events. World-class SDVs can handle common situations, but can behave unsafely in the many, rarely-occurring scenarios that are encountered on the road.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the self-driving stack, the *planning* module is most responsible for this bottleneck. It determines what the SDV should do in any given situation. A traditional *rule-based* planning approach selects a trajectory that minimizes a hand-engineered loss function. In order to improve its performance, engineers must design new terms in that loss function or re-tune their respective weights, for each driving scenario. This process is expensive and scales poorly to new geographies. Unlike perception, planning has benefited little from modern machine learning techniques, which leverage large quantities of data in order to avoid the hand-engineering of rules.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, the work of has demonstrated the first machine-learned policies for autonomous driving learned directly from human demonstrations. These approaches, although they scale much better than the hand-engineering method, do not provide the interpretability and safety guarantees required to safely deploy these systems in production.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work we propose SafetyNet: the first autonomous driving system to combine the strengths of an ML planner with the interpretable safety of a rule-based system, road-tested in busy San Francisco. The ML component is a high-capacity planning policy trained from expert demonstrations, and its performance scales with the amount of training data without the need for costly behavior engineering. To improve system safety, decisions of the ML planner pass through a lightweight *fallback layer*: a simple, rule-based system that tests the decisions against a small set of checks, and can minimally modify them to improve safety if required. This allows SafetyNet to transparently enforce safety and legality constraints, such as avoiding collisions, road rules violations, while simultaneously maximizing comfort metrics.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This combination outperforms ML-only systems and allows us to *safely* deploy an ML planning system in the busy streets of San Francisco, constituting the first demonstration of its kind. Our system exhibits a variety of maneuvers such as lane-following, keeping the distance to other vehicles, and navigating intersections without impeding the safety of the vehicle and other traffic participants.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The first combination of machine learning and a lightweight hand-engineered system to control a self-driving vehicle that learns from data while offering safety and legality guarantees.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The first evaluation of such a system in the challenging, real-world, urban environment of downtown San Francisco.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The source code will be provided to the public to encourage the advancement of the field^11^1The source code for the ML planner and a reference implementation of the fallback layer will be available at [safety.l5kit.org](safety.l5kit.org)..

<!-- chunk {"id": "body-0011", "role": "body", "section": "Related works", "weight": 1.0} -->

Trajectory optimization-based planning. Traditional trajectory optimization-based planning systems are widely used in both academia and industry. Here the motion planning task is formulated as an optimization problem, usually by hand-engineering a cost function. The optimal trajectory is then generated by minimizing this cost using optimization algorithms, such as A\* search-based methods, sampling-based methods, dynamic programming or combinations thereof that decompose the problem in a hierarchical fashion.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Related works", "weight": 1.0} -->

However, it is very difficult to hand-craft an objective function that provides a human-like trade-off between comfort, safety, and route progress over a wide variety of driving situations. In comparison, encoding certain hard constraints, e.g. obstacles avoidance, physical feasibility, requires far less engineering. Therefore, building a lightweight hand-engineered system whose only purpose is to detect and correct infeasible trajectories is much simpler and more scalable.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Related works", "weight": 1.0} -->

Additionally, these hand-engineered approaches do not improve with data, and their performance does not generalize well in highly unstructured urban scenarios. Therefore, tremendous engineering efforts are needed to fine-tune them, in particular when expanding to a new operational design domain (ODD) or new geographies.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Related works", "weight": 1.0} -->

Machine-learned planning. Recently, ML planning has gained attention due to successes in deep learning. This approach has the advantage of avoiding hand-crafted rules and scales well with data, thus performing better and better as more data is used for training. Therefore, this approach has great potential to handle a wide variety of driving situations. Next, we introduce the two most commonly used ML paradigms for motion planning.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Related works", "weight": 1.0} -->

\(1\) Imitation learning (IL). IL is a supervised learning approach in which a model is trained to mimic expert behavior. The first application of IL to autonomous driving was the seminal ALVINN back in 1989, which mapped the sensor data to steering and performed rural road following. More recently, demonstrated end-to-end driving using multiple-camera input alone, but the real-world driving results are limited to simple tasks such as lane follow or urban driving with light traffic. ChauffeurNet proposed to apply IL on a bird's eye view of a scene and use synthetic perturbations to alleviate the covariate shift problem, but it is yet to be tested in real-world urban environments.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Related works", "weight": 1.0} -->

\(2\) RL & IRL. Reinforcement learning (RL) is well-suited for sequential decision processes such as self-driving as it handles the interaction between the agent and the environment. Several methods have been proposed to apply RL to autonomous driving. In particular proposes combining learned and rule-based components, similarly to us, but the reported results are only from simulation. On the other hand, inverse reinforcement learning (IRL) is another popular ML paradigm applied to autonomous driving, which infers the underlying reward function based on expert demonstrations as well as a model of the environment. However, all these methods are yet to be evaluated in real-world urban driving.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Related works", "weight": 1.0} -->

The ML planning approaches introduced above, although very promising, do not provide safety guarantees, which prevent them to be deployed at scale in the real world. We are inspired by this paradigm but aim to mitigate this limitation by the SafetyNet proposed in this paper.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Related works", "weight": 1.0} -->

Hybrid approaches. The combination of ML and traditional motion planning techniques falls mostly into two categories: *ML-based heuristics*, which are leveraged to improve traditional planning algorithms, e.g. in terms of speed up. *Modular approaches*, where expert planners are leveraged to generate the trajectory candidates, e.g., by evaluating trajectories against a ML-based cost volume. The latter of these works, also provides safety guarantees based on imposing a very high cost on trajectories leading to a potential collision. These safety guarantees were not however verified in the real world.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Related works", "weight": 1.0} -->

Another specific area of research that has emerged in this field is the study of safety frameworks. While this work is relevant, our goal is not to propose a comprehensive framework for safety, but rather a simple yet effective method that allows for the deployment of a powerful neural network planner that learns and improves with data while ensuring certain safety and legality constraints.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Related works", "weight": 1.0} -->

SafetyNet leverages the strengths of the expert system to guarantee certain determinism, legality, and safety rules for specific scenarios while relying on the machine-learned motion planner for nominal trajectory generation.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Hybrid ML planning system", "weight": 1.0} -->

In this section we describe SafetyNet, our system for combining a machine-learned motion planner with an effective fallback layer to deliver a trajectory planning system for SDVs. Instead of relying on hand-engineered driving rules, this system learns to drive from expert driving demonstrations while guaranteeing certain interpretable safety constraints, such as avoidance of collisions and adherence to traffic rules.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Hybrid ML planning system", "weight": 1.0} -->

The SafetyNet system is outlined in Fig. 1. It is composed of an ML neural policy network ("ML Planner") $\mathcal{M}$ that takes as input $I$ the environment state around the SDV and produces an intended trajectory $\overline{\tau}$ to be taken by SDV. This trajectory is validated to obey the required constraints and in the case it does not satisfy them the closest trajectory $\tau^{i}$ is taken from a set of safe trajectory candidates.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Input and Output", "weight": 1.0} -->

Input representation. The input data is encoded in an ego-centric frame of reference where the SDV is always at a fixed location relative to a frame. As shown in Fig.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Input and Output", "weight": 1.0} -->

SDV: the current and past poses of the SDV and its size.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Input and Output", "weight": 1.0} -->

Agents: the current and past poses of perceived agents, their sizes, and object type (e.g. vehicle, pedestrian, cyclist) produced by the SDV's perception system.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Input and Output", "weight": 1.0} -->

Static map elements: road network from High Definition (HD) maps including lanes, cross-walks, stop lines, localized using the SDV's localization system.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Input and Output", "weight": 1.0} -->

Dynamic map elements: traffic light states, and static obstacles detected by the perception system (e.g. construction zones).

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-A Input and Output", "weight": 1.0} -->

Route: the intended global route that the SDV should follow.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Input and Output", "weight": 1.0} -->

We use a vectorized input representation based on to encode the perception outputs and map elements to vector sets. Each element includes a pose relative to the SDV pose, as well as additional features, such as the element type, time of observation.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Input and Output", "weight": 1.0} -->

Output representation. We define a trajectory $\tau$ as a sequence of $T$ discrete states separated uniformly in time by $\Deltat$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Input and Output", "weight": 1.0} -->

where $x_{t},y_{t},\theta_{t}$ correspond to the pose of the rear axle of the SDV w.r.t. a fixed coordinate frame at time $t$ and $v_{t},a_{t},k_{t},j_{t}$ correspond to the velocity, longitudinal acceleration, curvature and jerk respectively.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B ML planner", "weight": 1.0} -->

The ML planning component of our system takes the input $I$ capturing the states around the SDV and outputs the trajectory $\overline{\tau}$ to be executed.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B ML planner", "weight": 1.0} -->

Model architecture. Inspired, our model is built on a hierarchical graph network-based architecture as shown in Fig. 2. It consists of a PointNet-based local subgraph for processing local information from vectorized inputs and a global graph using a Transformer encoder for reasoning about interactions over agents and map features.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-B ML planner", "weight": 1.0} -->

To ensure the predicted trajectories are physically feasible, we introduce a kinematic decoder, which models the vehicle kinematic using a unicycle model. First, a 3-layer multilayer perceptron (MLP) is added after the Transformer encoder, which predicts longitudinal jerk $j_{1:T}$ and curvature $k_{1:T}$ for each time step within the prediction horizon $T$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B ML planner", "weight": 1.0} -->

where $f$ is the update function of the kinematic model, $\gamma$ comprises a set of parameters for vehicle kinematic constraint, including the maximum allowed jerk, acceleration, curvature and steering angle, which are used to clip controls to ensure physical feasibility.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B ML planner", "weight": 1.0} -->

Training framework. We use imitation learning to train a driving policy that mimics expert driving behavior by minimizing the L1 loss between the poses generated by the model and the ground truth poses. Following, we include perturbations to extend the distribution of states seen during the training and thus reduce the impact of the covariate shift. Although previous work used a pre-solver to smooth the target trajectory after applying perturbations, we can skip that thanks to the fact that we are using a kinematic decoder. Instead, we can simply penalize large values of jerk and curvature to reduce jerk and improve driving comfort.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-C Fallback Layer", "weight": 1.0} -->

After generating an ML trajectory, our system evaluates it along several dimensions for dynamic feasibility, legality, and collision probability, and determines a trajectory label {Feasible, Infeasible}. We describe these next.

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-C Fallback Layer", "weight": 1.0} -->

Dynamic feasibility. We evaluate whether the input trajectory remains within a feasible envelope characterized by the SDV's dynamics limits. Concretely, we evaluate each trajectory state and check whether the parameters, including longitudinal jerk, longitudinal acceleration, curvature, curvature rate, lateral acceleration, and steering jerk (curvature rate $\times$ velocity) are within reasonable bounds.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-C Fallback Layer", "weight": 1.0} -->

The bounds for those parameters were obtained from real-world vehicle testing. In practice, we typically use more conservative limits for jerk, longitudinal acceleration, and lateral acceleration to remain within comfortable limits.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-C Fallback Layer", "weight": 1.0} -->

Legality. For a given trajectory, we evaluate whether it is violating the traffic rules.

<!-- chunk {"id": "body-0041", "role": "body", "section": "III-C Fallback Layer", "weight": 1.0} -->

Collision likelihood. We check each state in the given trajectory for collisions with predicted poses of other agents from an in-house prediction module. Collision detection is performed by rasterizing future agent predictions and checking for overlaps with planned ego poses. Additionally, we also check for longitudinal distance, time-to-collision, and time headway violations along the trajectory. If any of the collision likelihood checks fail, the trajectory is labeled as Infeasible.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-C Fallback Layer", "weight": 1.0} -->

Fallback trajectory generation. Assuming the ML trajectory is labeled as Feasible, we will directly execute it. If the trajectory is labeled as Infeasible, we select a feasible fallback trajectory as close as possible to the ML trajectory.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-C Fallback Layer", "weight": 1.0} -->

For this we use a trajectory generation method based, generating a number of lane-aligned trajectory candidates $\tau^{i}$. These candidates consist of speed keeping, distance keeping, and emergency stopping maneuvers. Our implementation can be easily adapted to specific scenarios of interest.

<!-- chunk {"id": "body-0044", "role": "body", "section": "events per 1k miles", "weight": 1.0} -->

In this section we evaluate our system across several dimensions: (a) the performance of the ML planner in simulation when trained on an increasing amount of data (no fallback layer), (b) the effectiveness of the fallback layer in simulation, and (c) the performance of SafetyNet in the real world when controlling a real vehicle in San Francisco. We start by describing the datasets and metrics used during the evaluation.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-A Data", "weight": 1.0} -->

We created an in-house dataset to train and evaluate our system: 380 hours of urban driving collected in Palo Alto and San Francisco. It contains a wide range of driving scenarios in a densely populated urban environment. The dataset consists of 25 second *scenes*, which capture the perception output, the SDV trajectory, and HD maps. We partition the dataset into 300h for training and 80h for testing.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-B Metrics", "weight": 1.0} -->

We validate our planner using large-scale real-world driving dataset with closed-loop simulation. During simulation, we execute the planner and motion controller modules and simulate the SDV motion. The vehicle model is calibrated to the real-world SDV. Since the simulated SDV pose can diverge significantly from the logged pose in the dataset, we allow the other road *agents* to be reactive in their longitudinal behavior, avoiding collisions while preserving their trajectories from the dataset.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B Metrics", "weight": 1.0} -->

*Collisions*: the simulated SDV is $<$`<!-- -->`{=html}5cm from the road boundaries, static obstacles, or agents.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-B Metrics", "weight": 1.0} -->

*Close-calls*: the simulated SDV has no collision, but either gets within 25cm of another agent, has a time-to-collision $<$`<!-- -->`{=html}1.5s, or has a time headway to another agent $<$`<!-- -->`{=html}1s.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-B Metrics", "weight": 1.0} -->

*Discomfort braking*: the simulated SDV's jerk drops below $- 5$m/s^3^.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-B Metrics", "weight": 1.0} -->

*Passiveness*: the simulated SDV travels slower than its behavior in the dataset by $< -$`<!-- -->`{=html}5m/s and it is spatially behind its dataset position.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-B Metrics", "weight": 1.0} -->

*Off road events*: the simulated SDV deviates from the dataset route center line by $>$`<!-- -->`{=html}10m.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-B Metrics", "weight": 1.0} -->

After identifying the events in each scene, we aggregate them, normalizing by the number of miles driven in the simulations. All metrics are reported as the total number of events per 1000 miles.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-B Metrics", "weight": 1.0} -->

Additionally, to evaluate the open-loop performance, we compute the Average Displacement Error (ADE) between the position of the simulated SDV and the dataset position. This gives us insight into trajectory similarity between simulation and the dataset (see Table I).

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-B Metrics", "weight": 1.0} -->

Finally, we test how the system performs in the real world by deploying it in downtown San Francisco. We evaluate the ML planner performance via how often the fallback trajectory is used and we provide qualitative examples.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-C Effect of dataset size", "weight": 1.0} -->

For this experiment, the fallback layer is disabled, and the ML planner's trajectory is always executed. We evaluate the performance of various ML planners trained with varying dataset sizes: {5, 50, 150, 300} hours in simulation.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-C Effect of dataset size", "weight": 1.0} -->

Looking at the dashed lines in Fig. 3 (w/o fallback) we observe that the closed-loop performance across all safety and comfort metrics increases with training set size, and that more data should continue improving performance, albeit slowly. Models trained on $<$`<!-- -->`{=html}50h produce unstable driving policies that have significantly more collisions, off-route events, or even cases where the SDV remains completely still (passiveness). When dataset size is increased to 300 hours, performance improves significantly and the learned driving policy is able to reduce collisions, close-call and discomfort brakes, and reliably follows the route. In terms of passiveness, performance plateaus, which we attribute to causal confusion inherent to open-loop training. Similarly, the average displacement error (ADE) of the open-loop predictions keeps improving when trained with more data, as shown in Table I.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-D Effect of fallback layer", "weight": 1.0} -->

Now we evaluate the effectiveness of the fallback layer in simulation by comparing the SafetyNet performance, and without the fallback layer enabled. Here the ML planner is trained on the full 300h dataset. As shown in Tab. II, collisions are reduced by 95%, close call events by 40%, and discomfort braking by 92% when the fallback layer is enabled. This clearly demonstrates the value of the fallback layer and its importance for real world deployment. Crucially, we see that the solid lines in Fig. 3 (w/ fallback) are close to zero regardless of the maturity of the ML planner. This indicates that, with our method, we can safely deploy not only well-performing ML planners, but even immature ones (trained on $<$`<!-- -->`{=html}50h of data), thus facilitating faster development and evaluation cycle.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-D Effect of fallback layer", "weight": 1.0} -->

We note that there is also a 29.5% increase in passive behavior when the fallback layer is enabled, due to the fact that the SDV drives more conservatively. We see this as a necessary trade-off for reducing collisions and close calls.

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-D Effect of fallback layer", "weight": 1.0} -->

In Fig. 4 we show the distribution of events that trigger the fallback trajectory to be used during simulation. The main causes for fallback behaviors are the ML trajectory leaving the drivable surface, contacting dynamic agent predictions, infeasible distance gap with other agents, infeasible steering jerk, and contact with static obstacles. By manually triaging these ML planner failure cases, we see (a) contact lane boundary issues are a result of the ML planner cutting corners too closely, and (b) collisions are caused by the network not paying enough attention to the size of the large vehicles and assuming that vehicles are of similar size (Fig. 5, *top*). Moreover, near traffic light intersections the ML planner occasionally generates trajectories that do not properly yield to oncoming traffic (Fig. 5, *bottom*). It is caused by the synthetic perturbations applied to the ego poses during training. Note that in all these examples, the fallback layer successfully prevented collisions from happening.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-E Failure cases", "weight": 1.0} -->

There is still a small proportion of the ML planner failures that are not caught by SafetyNet. This is mostly because the current fallback layer implementation does not limit the proximity of the SDV to lane boundaries, and does not fully compensate for the uncertainty in the prediction of behavior of other agents. In Fig. 6 we see that the most recent feasible ML trajectory has brought the SDV close to the lane boundary and simultaneously the oncoming vehicle has a sudden change of velocity. With this combination of factors, the fallback trajectory fails to assure a comfortable lateral distance from the oncoming vehicle.

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-F Real world testing", "weight": 1.0} -->

Finally, we extensively tested SafetyNet with ML planner (trained on 300 hours), in the real world, in densely populated downtown San Francisco, under the supervision of human safety drivers. During the 150+ mile public road testing, the model successfully performed a wide variety of challenging maneuvers including lane-following, merging, yielding to pedestrians or nudging around parked cars (Fig. 7). At the same time, the fallback layer assured the safety of the overall system, taking control for around 7.9% of the total driving time. This confirms our hypothesis that although the ML planner is able to perform complex maneuvers and drive safely for most of the time ($>$`<!-- -->`{=html}90%), an additional layer of safety is required in certain situations. We refer the reader to the accompanying video for a more thorough analysis.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We present SafetyNet, a method for combining ML planners with a rule-based system fallback layer to provide safe driving in challenging, real-world urban environments. We have demonstrated the very significant improvements in safety and comfort metrics compared to a purely machine-learning-based system, both in simulation as well as in challenging San Francisco streets. This approach makes it possible to safely use learned planners in the real world, and benefit from their ability to improve with the data and handle more complex situations than their purely rule-based counterparts. We believe that teams starting to explore ML planning methods, and even those with state-of-the-art ML planning solutions would benefit from incorporating a SafetyNet system. In effect, SafetyNet may facilitate the development of machine-learning-based planners and their wider adoption in the AV industry.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We see many exciting opportunities for further development. The fallback layer can be refined to be less conservative and not increase passiveness. In terms of the ML planner, the presented approach is relatively simple, based on imitation learning. It can be improved by drawing from recent advancements in model-based Reinforcement Learning (RL), offline RL, or closed-loop training in a data-driven simulation.
