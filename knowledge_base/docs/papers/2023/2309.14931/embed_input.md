<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Interaction-Aware Sampling-Based MPC with Learned Local Goal Predictions

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Motion planning for autonomous robots in tight, interaction-rich, and mixed human-robot environments is challenging. State-of-the-art methods typically separate prediction and planning, predicting other agents' trajectories first and then planning the ego agent's motion in the remaining free space. However, agents' lack of awareness of their influence on others can lead to the freezing robot problem. We build upon Interaction-Aware Model Predictive Path Integral (IA-MPPI) control and combine it with learning-based trajectory predictions, thereby relaxing its reliance on communicated short-term goals for other agents. We apply this framework to Autonomous Surface Vessels (ASVs) navigating urban canals. By generating an artificial dataset in real sections of Amsterdam's canals, adapting and training a prediction model for our domain, and proposing heuristics to extract local goals, we enable effective cooperation in planning. Our approach improves autonomous robot navigation in complex, crowded environments, with potential implications for multi-agent systems and human-robot interaction.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Cities characterized by dense networks of urban canals, such as Amsterdam, could greatly benefit from deploying Autonomous Surface Vessels (ASVs) for various tasks including deliveries, transportation of people, and garbage collection. However, navigating autonomously in urban canals amidst mixed human-robot crowds presents a significant challenge. Urban canals are typically narrow, frequently congested, and lack the structured nature of roads. While not as strictly enforced as on roads, navigation principles like right-of-way and right-hand conventions should still be considered. Thus, akin to autonomous ground robots among pedestrian crowds, successful navigation in urban canals relies on cooperation and awareness of interactions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, a sampling-based Model Predictive Control (MPC) called Interaction-Aware Model Predictive Path Integral (IA-MPPI) control has been developed for generating cooperative motion plans in urban canals among multiple non-communicating vessels while maintaining awareness of navigation rules. This algorithm assumes rational and homogeneous agents, exact sensing of states, and knowledge of local goals. In real-time, the algorithm samples thousands of input sequences to approximate the optimal input sequence that enables all agents to progress toward their goals cooperatively. In scenarios where the local goals of other vessels are unavailable, such as in mixed human-robot environments or due to lack of communication, this previous approach has approximated these goals using a constant velocity model over a given horizon. However, in narrow and crowded environments, vessels often need to execute complex maneuvers to navigate tight intersections and avoid collisions while adhering to navigation rules. In such situations, relying solely on a constant velocity approximation can lead to inaccurate predictions, which can adversely affect the performance of the motion planner in terms of deadlocks, collisions, navigation rule violations, traveled distance, and travel time.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present a framework (see Fig. 1) that utilizes a learning-based trajectory prediction method to improve the estimation of agents' intended destinations. We introduce heuristics to extract local goals from the predicted trajectories and provide the motion planner with the flexibility to influence the behavior of other agents while expecting cooperation in collision avoidance.

<!-- chunk {"id": "body-0006", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Robot motion planning in dynamic environments is a challenging problem for which a series of classical and heuristic-based approaches have been developed, such as the Dynamic Window Approach or Reciprocal Velocity Obstacles. Despite their successful applications, e.g. to non-holonomic robots or vessels in open waters, the motions planned by this class of methods are often reactive. This, especially in crowded environments, can lead to unsafe and unpredictable behaviors.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Model Predictive Control (MPC) has become a popular approach to trajectory planning for autonomous vehicles because of its ability to optimize accounting for the system's dynamics and constraints. Moreover, by planning over a sufficiently large horizon, MPC can anticipate dynamic obstacles resulting in trajectories that are less reactive. To anticipate other agents, however, the free space over the entire planning horizon needs to be computed, which requires knowledge about other agents' positions in the future. If all the agents in the environment are autonomous, communication and distributed optimization can be used to plan trajectories in multi-agent environments. In mixed human-robot environments, however, such communication is not possible and predictions of the future motion of the other agents have to be employed. For instance, recent work on MPC for rule-aware navigation in urban canals uses constant velocity to model the future behavior of other vessels.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

In interaction-rich scenarios, however, constant velocity can be an inaccurate approximation which may lead to unsafe motion plans. Therefore, several works rely on learning-based models to predict the future motion of other agents and can include prediction confidence and multimodality. These methods, however, decouple prediction and planning which, in high-interaction environments, may lead the ego agent to wrongly assume that no collision-free path exists. To avoid the so-called freezing robot problem the robot has to expect cooperation in collision avoidance from the other agents. Coupled prediction and planning can be done with MPC by modeling the interacting agents as a system, but it quickly becomes expensive to solve via constrained optimization leading to long computation times and short planning horizons.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A Related Work", "weight": 1.0} -->

Building upon a novel sampling-based Model Predictive Control (MPC) framework, Interaction-Aware Model Predictive Path Integral (IA-MPPI) control has successfully demonstrated decentralized coupled predictions and planning in real-time, accommodating long prediction horizons, nonlinear dynamics, and discontinuous cost functions in multi-agent environments. While IA-MPPI has exhibited superior performance compared to optimization-based MPC approaches that rely on fixed predictions of other agents' motion, it necessitates knowledge of their near-term local goals, which can either be communicated or estimated.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

This paper presents a novel framework for interaction-aware decentralized motion planning in urban canals without relying on communication. Our framework encompasses the following contributions: Realistic Dataset: We generate and publish a realistic dataset of simulated rule-abiding vessel trajectories in real sections of Amsterdam's urban canals.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

Learning-Based Trajectory Prediction: We adapt a pedestrian prediction model to vessels and train it specifically for urban canals. This approach enables us to generate trajectory predictions for other agents.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

Local Goal Extraction: We propose heuristics to extract local goals from the predicted trajectories, thereby providing the motion planner with information about where agents intend to go.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

Communication-Free Coupled Prediction and Planning: By combining the local goal extraction with the IA-MPPI control, we achieve coupled prediction and planning without the need for communication. This approach ensures that the ego agent can influence the behavior of other agents while anticipating cooperation in collision avoidance.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

We validate our planning framework through extensive simulated experiments, comparing it against baseline approaches and providing insights into the benefits of coupled prediction and planning over decoupled methods. The framework can be adapted to other robot types beyond vessels.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Interaction-Aware MPPI", "weight": 1.0} -->

In this section, we introduce the main ideas of IA-MPPI, upon which our proposed framework is built. For details on the method, models used and cost function please refer to the original paper. For insights on the underlying sampling-based MPC, one can refer to the work on Information-Theoretic MPC. In short, IA-MPPI assumes that all the agents are homogenous and rational, i.e. have the same model and cost function. Under this assumption, we can create a large multi-agent system and plan input sequences resulting in cooperative trajectories for the ego agent as well as all the obstacle agents. This being a decentralized planning framework, we then apply the first input of the sequence to our ego agent, observe the environment and plan again. In more detail, IA-MPPI models the ego-agent $i$ as a discrete-time dynamical system, where $\mathbf{q}_{i,t}$ and $\mathbf{u}_{i,t}$ are, respectively, the state and the input of the ego-agent at timestep $t$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Interaction-Aware MPPI", "weight": 1.0} -->

The state $\mathbf{q}_{i,t} = {\lbrack\mathbf{p}_{i,t},\mathbf{v}_{i,t}\rbrack}$ contains the position and velocity of the agent. IA-MPPI assumes that all agents in the environment are homogenous. The state and the input of the multi-agent system consisting of the ego-agent and the obstacle agents can therefore be stacked, resulting, where $\left(. \right)_{j}$ is a variable that the ego-agent $i$ estimates of agent $j$ and $\mathcal{M} = {\{ 0,1,\ldots,m\}}$ is the set of all agents in the scene. By also stacking the state transition functions $\mathcal{F}$ over all agents, we obtain a model for the multi-agent system $\mathbf{q}_{t + 1} = {\mathcal{G}{(\mathbf{q}_{t},\mathbf{u}_{t})}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Interaction-Aware MPPI", "weight": 1.0} -->

Given a planning horizon $T$ and a prior input sequence $\mathbf{U} = {\lbrack\mathbf{u}_{0},\mathbf{u}_{1},\ldots,\mathbf{u}_{T - 1}\rbrack}$, IA-MPPI samples $K$ input sequences for the entire multi-agent system, with $k = {1,\ldots,K}$, variance $\Sigma$ and scaling parameter $\nu$. At the first iteration, the prior input sequence $\mathbf{U}$ is initialized at zero. By the end of this section, it will become clear how this prior input sequence is updated in subsequent iterations. Having a model for the multi-agent system, we can forward simulate the $K$ input sequences into $K$ state trajectories $\mathbf{Q}_{k}$ for the multi-agent system, Each of the resulting state trajectories is evaluated with respect to both an agent-centric cost as well as a system-wide cost, resulting in a total sample cost $S_{k}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Interaction-Aware MPPI", "weight": 1.0} -->

The reader can refer to the original publication for details on the cost function. For the scope of our paper, it is important to know that the agent-centric cost includes a tracking cost to encourage progress towards a local goal $p_{g}$ computed as, where $p_{t}$ is the position of the agent at timestep $t$, $p_{t_{0}}$ is the position of the agent at the beginning of the planning horizon and $k_{tracking}$ is a tuning parameter. Notice that we need to know the position of the local goal of each agent. For the ego agent, the local goal is extracted from a global plan. For all the other agents, the local goal has to be either communicated or estimated. We propose in the following section how this goal can be estimated.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Interaction-Aware MPPI", "weight": 1.0} -->

Once $S_{k}$, ${\forall k} \in {\lbrack 1,\ldots,K\rbrack}$ has been computed, importance sampling weights $w_{k}$ can be calculated as, where $S_{min}$ is the minimum sampled cost, $\eta$ a normalization factor and $\lambda$ a tuning parameter. We then compute an approximation of the optimal control sequence through a weighted average of the sampled control sequences, and apply the first input $\mathbf{u}_{i,0}^{\ast}$ to the ego-agent. We can now use a time-shifted version of $\mathbf{U}^{\ast}$ as the prior input sequence $\mathbf{U}$ to warm-start the sampling strategy at the next iteration.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Predicting goal positions", "weight": 1.0} -->

In Fig. 1 we provide an overview of the proposed framework. In Section III-A, we outline the prediction model. In Section III-B, we describe the dataset we have collected to train a prediction model that is interaction and rule-aware. In Section III-C, we present the steps taken to port the prediction model to urban vessel environments. In Section III-D, we propose a heuristic to extract a local goal suitable for IA-MPPI using the predicted trajectories.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Interaction-aware trajectory prediction method", "weight": 1.0} -->

Our approach leverages interaction-aware trajectory prediction for goal estimation. We employ an adapted version of Social-VRNN, which was originally designed for pedestrians, to obtain trajectory predictions. However, we remark that our framework is agnostic to the choice of trajectory predictor as long as it accounts for obstacles and interactions between agents in the environment.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Interaction-aware trajectory prediction method", "weight": 1.0} -->

Social-VRNN is an interaction-aware trajectory prediction method that leverages a generative model based on Variational Recurrent Neural Networks (VRNNs). The model combines three types of contextual cues to define a joint representation of an agent's current state: information on the past trajectory of the agent of interest, environment context, and agent-agent interactions. The input to predict the trajectory of agent $i$ is denoted as: where $\text{v}_{{- T_{0}}:0}^{i}$ corresponds to the sequence of velocity states over the previous observed horizon $T_{O}$ of the agent of interest $i$. The environment information $\text{O}_{env}^{i}$ is represented in the form of a grid map extracted around the agent of interest. Then, $\text{O}_{int}^{- i}$ represents the information on agent-agent interactions. It is a vector with the relative positions and velocities of all other agents from agent $i$'s perspective, listed in ascending order based on the absolute distance to it.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Interaction-aware trajectory prediction method", "weight": 1.0} -->

The output of the model is a sequence of velocity probability distributions represented by $T_{H}$ diagonal gaussian distributions $\mathcal{N}{(\mu_{\text{v},k},{\text{diag}{(\sigma_{\text{v},k}^{2})}})}$. For details on the method and its architecture, please refer to the original paper.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Artificial Dataset", "weight": 1.0} -->

In the absence of a publicly available dataset for short-term vessel trajectory prediction, an artificial dataset of vessel interactions is collected in a simulation environment. In order to obtain trajectories that resemble those of real vessels in urban canals, four real canal section maps in Amsterdam: the Herengracht (HG), the Prinsengracht (PG) and the Bloemgracht (BG) are used to collect data. The Open Crossing (OC) environment is created to collect vessel interactions in open water. Data on an additional environment, the Amstel (AM), is included only for testing our framework's generalization to environments not seen during training. Figure 2 depicts two of these canal sections. The yellow rectangles correspond to the areas in which start and goal locations are randomly initialized. These areas are placed around the entire map and in each canal section to improve the diversity of the trajectories and interactions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Artificial Dataset", "weight": 1.0} -->

To collect the data, more than four thousand experiments are conducted by initializing up to four vessels simultaneously in the mentioned environments. Each vessel is assigned a randomized start and goal location in one of the predefined areas. All sampled locations are ensured to be collision-free. The vessels run a centralized IA-MPPI to sail toward their respective goals while accounting for navigation rules. This ensures that the recorded trajectories are safe, interaction-aware, and mostly rule-abiding.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Artificial Dataset", "weight": 1.0} -->

For each experiment and vessel in the environment we record the current timestamp, the vessel ID, its position and velocity in the global frame. Each timestamp is unique across timesteps and experiments, which enables to identify vessels belonging to the same scene. The specifications of the artificial vessel dataset can be found in Table I. In order to evaluate the prediction model, 10% of the dataset is used as the test set. The remaining data is used for training and is split into a training set (72%) and a validation set (18%). The distribution of data from each scenario is ensured to be equal in all splits.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Model Training and Adaptation", "weight": 1.0} -->

We adapt the variational inference architecture presented in to generate unimodal trajectory probability predictions of vessels. In contrast to humans, vessels are slower and have lower-order dynamics, which results in less reactive behaviors and smoother trajectories. To take this into account and avoid overfitting to the dataset, we reduce the dimensionality of the method's latent space. We also add an L2-regularization term to the loss function and weight it with a hyperparameter we define as $\gamma$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-C1 Hyperparameters", "weight": 1.0} -->

The model is trained using backpropagation through time and the RMSProp optimizer. With a time step of ${\DeltaT} = 0.4$ seconds, the prediction horizon is set to $T_{H} = 24$ steps (9.6 seconds) and the previous horizon to $T_{O} = 14$ steps (5.6 seconds). Furthermore, we employ learning rate starting at $\alpha$ = ${1e} - 4$ that decays by a factor of 0.9 after every gradient step. The regularization weight is kept at $\gamma = 0.0001$. Finally, the model is trained for $4e4$ training steps, using early stopping.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-D Local Goal Extraction", "weight": 1.0} -->

In eq. we show that the IA-MPPI needs to know the local goal $p_{g}$ of each agent. There are two requirements for a goal to be suitable: it has to lie within a radius $r_{p_{g}}$ from the agent it corresponds to and cannot be in space occupied by static obstacles. Therefore, we first search the predicted trajectory backward until we obtain a position $p_{\leq r_{p_{g}}}$ within the desired radius. If $p_{\leq r_{p_{g}}}$ is in collision with a static obstacle, we construct a circle centered on the agent's position $p_{a}$ with radius $p_{a} - p_{\leq r_{p_{g}}}$ and find the point on the circle closest to $p_{\leq r_{p_{g}}}$ which is not in collision with static obstacles.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-D Local Goal Extraction", "weight": 1.0} -->

This goal extraction method is illustrated in Fig. 3. Once the goals for all agents are predicted, IA-MPPI can plan interaction-aware trajectories in a decentralized fashion.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

The experiments are conducted in real maps of Amsterdam's canals, namely the Herengracht (HG), Bloemgracht (BG), Prinsengracht (PG), and the Amstel (AM). In addition, experiments are conducted in an Open Crossing (OC) map without static obstacles. In Section IV-A we evaluate the prediction model, in Section IV-B we show the performances of the proposed framework for motion planning, and in Section IV-C we highlight the benefits of coupled prediction and planning with respect to a decoupled approach.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Prediction Accuracy", "weight": 1.0} -->

In Fig. 4 we compare the proposed Learning-Based Model (LBM) to a Constant Velocity Model (CVM) on test data. We evaluate the methods against the displacement error at each prediction step, which is defined as the Euclidean distance between a prediction and the ground truth. In all maps the LBM outperforms the CVM, showing a lower average displacement error and a smaller standard deviation. Note that the Amstel map was previously unseen during training, demonstrating generalization capabilities.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B Interaction-Aware Motion Planning with Predictions", "weight": 1.0} -->

In this study, we evaluate the performance of the proposed decentralized framework that uses a Learning-Based prediction Model to extract local goals (IA-MPPI-LBM), by comparing it against a decentralized approach that extracts local goals from a Constant Velocity Model (IA-MPPI-CVM) and decentralized with communication (IA-MPPI-w/comm.), which assumes perfect knowledge of other agents' local goals. It is important to stress that, in similar experiments, the IA-MPPI-CVM which serves as the communication-free baseline in our comparisons has already been demonstrated to outperform an optimization-based Model Predictive Control (MPC) approach that relies on fixed predictions.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Interaction-Aware Motion Planning with Predictions", "weight": 1.0} -->

In the simulated experiments taking place in real sections of the canals of Amsterdam, we randomize the initial positions and goals of four interacting agents, all running the same algorithm. To challenge each method, we design regions within which each agent's start and goal position are randomly initialized in a way that forces all four agents to interact in a narrow section of the map. These high-interaction scenarios are discussed in Section IV-B1.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B Interaction-Aware Motion Planning with Predictions", "weight": 1.0} -->

For completeness, we also design experiments where agents' starting and goal positions are randomized across much larger spaces. In these experiments, however, vessels don't often interact and usually have larger free spaces to avoid each other. These low-interaction scenarios are discussed in Section IV-B2.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Interaction-Aware Motion Planning with Predictions", "weight": 1.0} -->

An example of experiments in low- and high-interaction scenarios is shown in Fig. 5. The IA-MPPI plans with a time horizon $T$ of 100 time steps with step size ${\deltaT} = {0.1s}$ and $K = 4500$ samples. Each method is evaluated on the same set of randomly initialized experiments. For fairness, metrics such as rule violations, goal displacement error, total traveled distance, and time are only displayed for experiments that ended successfully with all methods.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B1 High-Interaction Scenario", "weight": 1.0} -->

The experiments in high-interaction scenarios are conducted in narrow intersections in the Bloemgracht, Herengracht, and Prinsengracht. Since the Amstel canal is very wide and the Open Crossing has no static map constraints, it is difficult to generate experiments with high-interactions, and thus these two maps are excluded from this experiment section. The results of the experiments are summarized in Table II and Figure 6. It can be seen that in these high-interaction scenarios, the LBM consistently outperforms the CVM in terms of the goal displacement error (Goal DE). As a consequence, the motion planning framework that estimates other agents' local goals using predictions from the LBM outperforms the framework that uses the CVM on all the metrics. Moreover, we demonstrate our framework with the LBM has negligible performance losses compared to the method with perfect communication.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B2 Low-Interaction Scenarios", "weight": 1.0} -->

Table III and Fig. 7 summarize the results in low-interaction scenarios. Note that we here also test on the Open Crossing maps and the Amstel, which the LBM has not previously seen in training. The results show that also when the start and goal positions of all agents are randomly initialized over large areas, our proposed communication-free framework with the LBM performs just as well as the baseline with full communication, even in a map unseen in training. However, perhaps unsurprisingly, the framework that approximates the local goals with a CVM can also achieve the same performance as the framework with full communication. Intuitively, in low-interaction scenarios where agents mostly navigate straight to their goal, CVM is a reasonably good approximator.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-C Decoupled Prediction and Planning", "weight": 1.0} -->

The framework we proposed utilizes a Learning-Based Model (LBM) to predict trajectories for obstacle agents and extract local goals while employing Interaction-Aware Model Predictive Path Integral (IA-MPPI) for coupled predictions and planning. To assess the advantages of this framework, we compare it to a planner without interaction awareness (MPPI-LBM), which decouples prediction and planning. Like other state-of-the-art methods, MPPI-LBM treats the predicted future trajectories of obstacle agents as occupied space and plans the ego agent's motion without considering interaction awareness. This approach reduces the system size and computational burden by minimizing the space to be sampled. However, apart from this difference, MPPI-LBM shares the same sampling strategy and cost function as the proposed IA-MPPI-LBM. We conducted 100 low-interaction experiments across the Amstel, Bloemgracht, Herengracht, Open Crossing, and Prinsengracht, comparing different methods. Table IV presents the outcomes, including total successes, deadlocks, collisions, and rule violations.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C Decoupled Prediction and Planning", "weight": 1.0} -->

Again, the proposed IA-MPPI-LBM shows similar performances to the method with communication (IA-MPPI-w/comm).

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-C Decoupled Prediction and Planning", "weight": 1.0} -->

However, MPPI-LBM exhibited a significantly lower success rate and a higher number of rule violations. The LBM, while trained to be somewhat rule- and interaction-aware in its predictions, occasionally struggles to capture complex reciprocal collision avoidance maneuvers when agents are in close proximity. This, combined with the motion planner's unawareness of the ego agent's influence on other agents' motion and their cooperation in collision avoidance, often led the MPPI-LBM to wrongly assume that no feasible solution existed. Consequently, this resulted in agents drifting into collisions due to their large inertia.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper, we introduced a framework that combines a learning-based trajectory prediction model with Interaction Aware MPPI, enabling decentralized and communication-free coupled prediction and planning. Our experimental results demonstrated the superiority of our Learning-Based Model (LBM) over the Constant Velocity Model (CVM) in accurately predicting the trajectories of interacting vessels, even in unseen maps. Through simulated experiments in Amsterdam's canals, we showed that our motion planning framework achieved comparable performance to a method with ground truth knowledge of local goals, which was shown to outperform classical optimization-based MPC approaches with decoupled prediction and planning in previous work. Additionally, we highlighted the limitations of the CVM in tight environments with multiple interacting agents. Finally, by comparing our approach with a non-interactive planner, we emphasized the advantages of coupled planning and predictions.
