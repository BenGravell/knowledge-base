<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Scaling Laws of Motion Forecasting and Planning: Technical Report

Topics include Autonomous driving, Motion forecasting, Planning, Scaling laws, Transformers, Training compute, Inference-time compute, Closed-loop evaluation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Studies empirical scaling laws for autoregressive transformer models on joint motion forecasting and planning using a very large driving dataset. The report is useful because it connects training loss, open-loop metrics, closed-loop metrics, data scale, model scale, and inference-time sampling into one scaling-law view of driving model development.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the empirical scaling laws of a family of encoder-decoder autoregressive transformer models on the task of joint motion forecasting and planning in the autonomous driving domain. Using a 500 thousand hours driving dataset, we demonstrate that, similar to language modeling, model performance improves as a power-law function of the total compute budget, and we observe a strong correlation between model training loss and model evaluation metrics. Most interestingly, closed-loop metrics also improve with scaling, which has important implications for the suitability of open-loop metrics for model development and hill climbing. We also study the optimal scaling of the number of transformer parameters and the training data size for a training compute-optimal model. We find that as the training compute budget grows, optimal scaling requires increasing the model size 1.5x as fast as the dataset size. We also study inference-time compute scaling, where we observe that sampling and clustering the output of smaller models makes them competitive with larger models, up to a crossover point beyond which a larger models becomes more inference-compute efficient.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Overall, our experimental results demonstrate that optimizing the training and inference-time scaling properties of motion forecasting and planning models is a key lever for improving their performance to address a wide variety of driving scenarios. Finally, we briefly study the utility of training on general logged driving data of other agents to improve the performance of the ego-agent, an important research area to address the scarcity of robotics data for large capacity models training.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion forecasting and planning are core autonomous vehicle capabilities. The forecasting task typically involves predicting the likely future trajectories of dynamic agents (e.g., pedestrians, cyclists, and vehicles). The planning task predicts trajectories for the autonomous vehicle (the ego-agent) conditioned on the route objective, optimizing for comfortable and safe motion with respect to the likely behaviors of other dynamic agents. The complexity of this task arises from the inherent uncertainty in predicting the dynamic agents' behavior, the complex interactions between them, and the need to reason about the long-term consequences of actions in a continuous state space. Systematically improving the performance on this task requires advances in modeling to account for the interactions between dynamic agents, thoughtful model input design to reduce information bottlenecks due to limitations in the interface with the perception system, and training data scaling to improve the model performance on long-tail scenarios.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The fact that past and future agent trajectories are temporal sequences makes transformers well-suited for the motion forecasting task (Girgis et al. Mercat et al. Ngiam et al. Yu et al. Yuan et al. Nayakanti et al., ). Nayakanti et al. showed that an encoder-decoder transformer setup simplifies the design space and enables its systematic study, especially with regards to the different options for fusing the input modalities. Nayakanti et al. was applied to the marginal a-posteriori trajectory prediction task, i.e., the prediction of multiple possible futures for each agent independent from the futures of the remaining agents. Several works studied autoregressive transformers to jointly predict the future trajectories of multiple or all agents in the scene (Ngiam et al. Seff et al. Jia et al. Shi et al. Zhou et al., ). Jointly predicting multiple agents is a simple form of world modeling, which can be used to study how increasing the scene modeling complexity can benefit the ego-agent planning task.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this report, we study the improvements in the joint prediction task as we systematically increase the compute, data, and model size, using the architecture from Seff et al..

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, it has been repeatedly shown that the performance of deep learning models scales predictably with data and compute, as first highlighted and studied. Kaplan et al. systematically studied the improvements in the cross-entropy loss of next-token prediction language models as the model size, dataset size, and training compute were scaled, and found a power-law relationship that empirically holds for 7 orders of magnitude. This provided strong evidence that warranted calling it an empirical "law". The work also proposed a methodology to find the optimal allocation of a compute budget for increasing the model size versus the training dataset size. Henighan et al. found the same relationship to hold for transformer decoders on the autoregressive generation task in several other modalities, further supporting the idea that these power-law relationships could be universal laws independent of the data modality of the generative task.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most principled studies of scaling laws exist only for language models trained on internet-scale text datasets, with only a few notable exceptions. Without firm theoretical explanations for this empirical phenomenon, it is not immediately clear that these laws should hold for the joint-prediction motion forecasting task, and how such improvement correlate with close-loop and real world models performance.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

How does the cross-entropy loss scale as we increase the model size, dataset size, and compute in tandem?

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

What is the optimal model and dataset scaling as we scale training compute?

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Do downstream metrics relevant to driving follow improvements in the cross-entropy loss?

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Closed-loop Scaling Laws: Do closed-loop planning metrics (within a realistic simulated environment) correlate with pre-training cross-entropy? In other words, are larger models safer and more competent drivers?

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inference Scaling Laws: How does performance change as we increase inference-time model sampling? Can smaller models be competitive with larger models?

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Cross-Agent Skills Transfer: Can training on "passive" driving logs help train larger models that translate to better AV ego-agents?

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Following Hoffmann et al., we conduct an iso-FLOP analysis to find the compute-optimal models across various fixed training compute budgets. We find that the cross-entropy loss for our joint prediction formulation of motion forecasting also follows a power-law relationship as a function of the training compute. Furthermore, the optimal allocation of compute should grow 1.5x as fast as the dataset size. Interestingly, at the same training compute budget, an optimal LLM is $\sim 50$ times larger than an optimal motion forecasting model. We hypothesize that this, at least in part, can be attributed to driving data distributions; i.e. models need more training data to capture less common driving modes. To our knowledge, this is the first comprehensive study showing that the optimal number of model parameters could be drastically different for driving tasks compared to language models -- potentially suggesting the importance of collecting more data, or perhaps improving the training data sampling techniques for this domain. This finding also indicates that improvement in model performance by scaling training compute can be directly leveraged to improve the performance of onboard systems, as the optimal models are relatively small in size.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

We validate that the improvement in the model training loss leads to consistent improvements in the open-loop precision and coverage metrics. For autonomous driving, while open-loop metrics are important indicators of model performance, it is unclear if they are an unbiased estimator of closed-loop simulation performance for driving agents navigating in real scenarios. Conventional wisdom in the field, as well as previous studies such as, suggest that open- and closed-loop evaluations are misaligned. To study the correlation between cross-entropy loss, open-loop metrics, and closed-loop simulation, we also conduct a scaling analysis showing improvements in closed-loop metrics that are consistent with the loss improvements. These evaluation results suggest that performance on the driving task can be improved by pursuing compute and data scaling for the supervised training task.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

We study inference scaling to answer questions about model performance as a function of the inference FLOPs. We observe that increasing the inference compute by scaling the sampling of smaller models makes them competitive with larger models, up to a crossover point where even limited sampling from a larger model is more inference compute-efficient.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the major challenges to scaling robotic manipulation deep learning models is the difficulty and cost of collecting human demonstration data. There are many ongoing investigations to leverage generic internet-scale video datasets to scale pre-training (Ye et al. Cheang et al. Wu et al., ). For driving, it might be relatively easier to passively collect driving logs, which can be used to scale training. At the end of this report, we present a preliminary study of skills transfer from observed driving logs to the AV ego-agent.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section, we briefly present the motion forecasting problem formulation and model architecture. For further details, we refer the reader to more detailed works on this topic (Nayakanti et al. Seff et al. Ettinger et al., ). Section introduces the training dataset. In Section, we present our scaling laws analysis, followed by open-loop and closed-loop evaluations in Section. The inference scaling study is presented in Section, and Section presents the cross-agent skills transfer study. We conclude with a review of related work in Section and a discussion of the limitations and implications of the results in Section.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We formulate the problem of motion forecasting as a conditional sequence generation problem similar to modern language models. Given a set of perception features representing the scene context over the past few seconds, the task is to generate the future motion tokens for $M$ agents in the scene, which we refer to as agents of interest or modeled agents. An agent of interest can be the autonomous vehicle, another vehicle, a pedestrian, or a cyclist.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The scene context $S$ consists of multi-modal data including road information, traffic light state history, and agent state history. The histories are provided for $T_{\text{history}}$ time steps (the current time step and $T_{\text{history}} - 1$ past time steps).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Agent History contains sequences of past states for $S_{a}$ contextual agents. This input has shape $\lbrack S_{a},T_{\text{history}},D_{a}\rbrack$. For each time step, we consider features that define the state of the agent: $xyz$ position, heading, velocity, and bounding box extents. Note that the $M$ modeled agents are a subset of the $S_{a}$ contextual agents.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Roadgraph represents the road shape around the autonomous vehicle with a collection of $S_{r}$ line segments specified by their endpoints and annotated with type information. This input has shape $\lbrack S_{r},1,D_{r}\rbrack$. Each polyline has endpoint $xyz$ position, direction, type and validity features. Note that there is no time dimension for the road features, but we include a time dimension of 1 for homogeneity with the other modalities.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Traffic Light State History describes the position, state, and confidence of the state estimation over time for $S_{tls}$ traffic lights, in a feature tensor of shape $\lbrack S_{tls},T_{\text{history}},D_{tls}\rbrack$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The motion forecasting task is to generate joint agent actions $A_{t} = {\{ a_{t}^{1},a_{t}^{2},\ldots,a_{t}^{M}\}}$ for $M$ agents of interest at future timesteps $t = {1,\ldots,T}$. Each agent action $a_{t}^{m}$ is a discrete motion token representing a two-dimensional Verlet-wrapped displacement in Bird's-Eye-View, as described. From these actions, agent trajectories $Y = {\{ Y_{1},\ldots,Y_{T}\}}$ can be calculated easily via integration of the displacements over the discrete time steps.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Modeling", "weight": 1.0} -->

Large Language Models (LLMs) are pre-trained to maximize the probability of the next token conditioned on the previous text (Brown et al. Hoffmann et al., ). This approach has found success in continuous domains such as speech and image generation, as well. Leveraging the flexibility of arbitrary categorical distributions, we can represent continuous data with a set of discrete tokens, reminiscent of language model vocabularies.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Modeling", "weight": 1.0} -->

In driving scenarios, road users may be likened to participants in a constant dialogue, continuously exchanging a dynamic series of actions and reactions mirroring the fluidity of communication. Navigating this rich web of interactions requires the ability to anticipate the likely maneuvers and responses of the involved actors. Just as today's language models can capture sophisticated distributions over conversations, we leverage similar sequence models to forecast the behavior of road agents. We follow the design to model the task of trajectory prediction as an auto-regressive sequence prediction problem over discrete action spaces much like the objective of large language models.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Joint agent modeling", "weight": 1.0} -->

The task of the motion prediction model is to produce joint future actions $A_{t}$ of the modeled agents, as explained above. Given the future is inherently multi-modal depending on complex interactions between scene elements, extending the problem definition to predict full future joint rollouts of all scene elements (world modeling) allows the model to reason about richer representations. It is also a general, foundational representation which can be readily adapted to a variety of important related tasks including marginal, joint or conditional predictions for behavior prediction, sim agents or planning applications.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Joint agent modeling", "weight": 1.0} -->

In our modeling framework, we sample a predicted action for each modeled agent at each future time step. These actions are formulated as discrete motion tokens from a finite vocabulary.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Joint agent modeling", "weight": 1.0} -->

Equation represents the fact that we treat agent actions as conditionally independent at time $t$, given the previous actions and scene context. During training, we use teacher forcing and minimize the cross entropy loss between the predicted and target discrete motion tokens, thus maximizing the likelihood of multi-agent actions expressed above. We train all models in this study with $M = 8$ agents.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Model Architecture", "weight": 1.0} -->

We follow the setup from MotionLM. We prioritize design choices that maximize the scalability of our model development process. Our model consists of two main networks: an encoder which processes initial scene elements, and a motion decoder which performs both cross-attention to the scene encodings and self-attention along agent motion tokens.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Scene Encoder", "weight": 1.0} -->

The scene encoder processes information from multiple input modalities, including the roadgraph, traffic light states, and agents trajectory histories. Here, we follow the design of the early fusion network proposed by as the backbone of our scene encoder. Early fusion is favored for its flexibility to process all modalities together with minimal inductive bias. For additional details, refer to. The scene encoder encodes all the modalities in a global frame of reference defined by the autonomous vehicle pose. This stands in contrast to Wayformer and MotionLM, where the scene encoding was done for each modeled agent in its own local frame of reference.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Motion Decoder", "weight": 1.0} -->

Our motion decoder is tasked with generating sequences of motion tokens for multiple agents by cross-attending to the outputs of the scene encoder.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Motion Decoder", "weight": 1.0} -->

Discrete motion tokens: We elect to transform trajectories comprised of continuous waypoints into sequences of discrete tokens $a_{t}^{m}$. This enables treating sampling purely as a classification task at each timestep. Discretizing continuous targets in this manner has proven effective in other inherently continuous domains, e.g., in audio generation, mesh generation and robotic manipulation. We suspect that discrete motion tokens also naturally hide some precision from the model, possibly mitigating compounding error effects that could arise from imperfect continuous value prediction.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Motion Decoder", "weight": 1.0} -->

Flattened agent-time self-attention: While separate passes of factorized agent and time attention are also possible (Ngiam et al. Nayakanti et al. Jia et al., ), we use a single pass of joint agent-time self-attention here for simplicity. So, given a target sequence of length $T$ for each of $M$ agents, we perform self-attention over $MT$ elements, with appropriate causal masking to avoid future leakage.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Motion Decoder", "weight": 1.0} -->

This motion decoder follows that of MotionLM closely, with the exception that here all motion tokens cross-attend to the shared scene encoder tokens, and in MotionLM tokens from different agents cross-attended separate scene encoder tokens as the scene encoding was done per agent.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Dataset", "weight": 1.0} -->

Data is a key enabler for scaling. Models scale with compute and capacity only when unconstrained by amount of data. More so, recently publicly available research finds that more data for a fixed amount of training compute, or overtraining of models of a fixed capacity results in further improvements. In addition, improvements to both the quantity and quality of the data results in significant improvements across foundation model generations. For example, the number of tokens used increased from 1.8T to 14T tokens from Llama2 to Llama3 family of models for training the flagship 405B parameter model. These improvements include the development of more careful pre-processing and curation pipelines for pre-training data and the development of more rigorous quality assurance and filtering approaches for post-training data.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Dataset", "weight": 1.0} -->

We curate a dataset following the trends above. As a quality measure, we utilize a dataset consisting of safety driver demonstrations; no semi- or fully- autonomous miles were used in this study. We sample nearly 6 million unique runs, and sample 30 second run segments within those. As part of this sampling, we perform simple filtering and deduplication to ensure the data is valid, interesting and diverse. These scenarios are composed of a rich mixture of real world driving situations like driving through busy intersections in dense urban cities (e.g., San Francisco, Phoenix, Los Angeles), dealing with construction zones and road closures, interacting and safely navigating around emergency vehicles, driving on higher speed limit areas like freeways, complex you-go-I-go interactions with pedestrians and cyclists. We summarize some interesting statistics of the dataset in table.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Dataset", "weight": 1.0} -->

As explained in Section 2 our training examples consist of driving history and future prediction. For this study we use 5 seconds history to predict for 11 seconds of future. The long horizon prediction, while challenging for the task of motion prediction, allows for modeling complex inter-agent dynamic and static interactions. We use overlapping sliding windows to construct multiple training examples from the 30 second run segments. We currently use a sliding window of 1.5 seconds to create multiple examples from each run segment.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Scaling Laws", "weight": 1.0} -->

We investigate the scaling behavior of our transformer model on the multi-agent joint future trajectory prediction task. We systematically vary the model size, dataset size, and training compute to address two key questions: 1) Does the cross-entropy loss follow power-law scaling as observed in language and other domains? 2) With a fixed compute budget, what is the optimal allocation between increasing model size and dataset size?

<!-- chunk {"id": "body-0042", "role": "body", "section": "Scaling Laws", "weight": 1.0} -->

Following Kaplan et al.; Hoffmann et al., we parameterize the training loss as $L{(N,D)}$, where $N$ represents the total number of transformer parameters (excluding embedding layers, see A) and $D$ is the number of training examples. Our model employs an encoder to transform the model inputs into a scene embedding, as well as a decoder for auto-regressive prediction of motion action tokens for the dynamic agents. Since the scene embedding dimensions and motion tokens are fixed per training example, we parameterize the loss using the number of training examples, deviating from the common practice in decoder-only models which use the total number of training tokens.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Scaling Laws", "weight": 1.0} -->

To determine the optimal model and data scaling, we follow Hoffmann et al.; Kaplan et al. and aim to minimize the loss function subject to a fixed compute budget constraint, FLOPs${(N,D)} = C$,

<!-- chunk {"id": "body-0044", "role": "body", "section": "Scaling Laws", "weight": 1.0} -->

We observe that, for our symmetric encoder-decoder models, $N_{opt} \propto C^{0.63}$ and $D_{opt} \propto C^{0.44}$. This indicates that for optimal training compute efficiency, the optimal model size should grow $\sim 1.5$ times as fast as the number of training examples. We report the analysis details next.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Estimating Optimal Model and Data Scaling", "weight": 1.0} -->

The cross-entropy loss for encoder-decoder transformer models can be parameterized in terms of their number of encoder and decoder parameters,

<!-- chunk {"id": "body-0046", "role": "body", "section": "Estimating Optimal Model and Data Scaling", "weight": 1.0} -->

where $N_{e}$ and $N_{d}$ are the number of encoder and decoder parameters, respectively. $\alpha_{e}$ and $\alpha_{d}$ are encoder and decoder-specific exponents. $F$, $G$ and $B$ are normalization constants. $E$ is interpreted as the entropy of the data distribution. As mentioned earlier, $D$ is the number of training examples.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Estimating Optimal Model and Data Scaling", "weight": 1.0} -->

We train models that are symmetric in their number of encoder and decoder layers. Consequently, our decoders hold $\frac{4}{7}$ of the total number of non-embedding parameters (see Appendix A for parameter estimates).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Estimating Optimal Model and Data Scaling", "weight": 1.0} -->

This allows us to study model size in terms of the total number of model parameters, analogous to decoder-only models. As explained in the previous section, $D$ in our case represents the total number of training examples. $A$ and $B$ are normalization constants which can also be obtained empirically by fitting direct fit to the data (see approach 3 in Hoffmann et al. ).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Estimating Optimal Model and Data Scaling", "weight": 1.0} -->

We train 84 models ranging in size from 900K to 118M parameters across seven compute budgets spanning more than two orders of magnitude. To obtain models with different sizes, we vary parameter counts by equally increasing the number of encoder and decoder layers, while keeping width-to-depth ratio at either 8 or 16. To get iso-FLOP bands, we vary training compute via number of model parameters and training steps. The batch-size was fixed to 512 examples. With 673 context tokens and 176 predicted action tokens, the batch has 434K tokens. We employ AdamW optimization with a fixed batch size throughout our study. A cosine learning rate schedule is used, with 3000 warmup steps, a peak value of $2 \times 10^{- 4}$, and a decay to $2 \times 10^{- 5}$ fixed to the total number of training steps. Training is performed using a cross-entropy loss as previously described. Figure presents the training loss curves for all experiments as a function of the training budget.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Estimating Optimal Model and Data Scaling", "weight": 1.0} -->

In order to find out the optimal number of model parameters and training examples, we plot the final losses on a validation dataset grouped in iso-FLOP bands in Figure.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Estimating Optimal Model and Data Scaling", "weight": 1.0} -->

where $x$ is either number of parameters or number of data points. $a$, $x_{C}^{opt}$, and $L_{C}^{opt}$ are the fit parameters. The latter two are the optimal values we are extracting for each compute budget $C$. We report the 3 standard deviations in $N_{opt}$, $D_{opt}$, and $L_{opt}$ directly from the fit parameter variances. Figure shows the $N_{opt}{(C)}$ and $D_{opt}{(C)}$ obtained from the parabola fits, along with a power-law fit of the form $ax^{b}$. Finally, we derive the exponents $N_{opt} \propto C^{0.63 \pm 0.08}$ and $D_{opt} \propto C^{0.44 \pm 0.06}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Estimating Optimal Model and Data Scaling", "weight": 1.0} -->

As discussed in the introduction, in Figure (Left), we observe that the optimal models required for the motion forecasting task are 50 times smaller in the number of parameters than a large-language model at the same compute budget, for example, see Hoffmann et al.. Other studies of autoregressive model scaling on non-language domains have observed similar trends, notably Henighan et al., where they systematically studied scaling on different modalities. There we observe a 1-2 orders of magnitude difference in the optimal model size between different domains. Language seems to require the most parameters and is trained on less data at a fixed compute. Understanding whether this is a property of the data modality or the data mixture and distribution could improve the data efficiency of our models.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Cross-Entropy Loss Scaling", "weight": 1.0} -->

From the iso-FLOP bands, we obtain the optimal loss $L_{opt}{(C)}$ for a fixed compute budget. As illustrated in Figure, the optimal loss improves as a power-law when we scale the model size, data, and compute in tandem. This demonstrates that the empirical power-law scaling trend studied in Kaplan et al. for autoregressive language models, and shown in Henighan et al. to hold for autoregressive generative models across a wide range of modalities, also applies to the task of motion forecasting in the autonomous vehicles domain. However, we also observe a curvature in the data points, indicating, that we could be close to an irreducible term.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Cross-Entropy Loss Scaling", "weight": 1.0} -->

where $a$, $b$ and $L_{\infty}$ are the fit constants. The right panel of Figure compares the fit with a constant to a pure power-law fit. We observe that adding a constant explains the data significantly better. This raises the question of whether we are close to the epistemic irreducible loss of the problem, i.e., the entropy of the true data distribution, or if it is an artifact of other factors. These factors could include the limited dataset size of this study; training with multiple data passes (epochs), and overlap between examples. The geographic data and complexity of driving scenarios mixture used is another area that is interesting to investigate. We also suspect that any lossiness of the interface with the perception system (we only include a limited set of perception features following the Waymo Open Motion Dataset configuration in this study) could also contribute to this irreducibility. We leave definitive answers to these questions to future studies.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Cross-Entropy Loss Scaling", "weight": 1.0} -->

Our models are trained on all dynamic agents in the scenes. Different agent types have varying degrees of freedom, speed profiles, and on-road behavior, resulting in different data distributions and predictability. Therefore, studying the trends of these agent types is useful. The main agent types are: the ego-agent (manually driven AV), other vehicles, pedestrians, and cyclists. Top panel of Figure compares the autonomous vehicle (AV) loss to that of other vehicles. Both losses follow a power-law fit, but with different exponents. The scales align with our intuition that AV trajectories are easier to predict due to the lack of perception noise and full observability. The exponents also indicate that improving AV trajectory predictions is easier than for other vehicles, consistent with the latter being a harder task. Figure also shows the losses and exponents for pedestrian and cyclist predictions.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Scaling of Open-loop Distance Metrics", "weight": 1.0} -->

In this section, we assess how well improvements in cross-entropy loss, driven by scale, correlate with improvements in the model's driving skills using common open-loop distance metrics.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Scaling of Open-loop Distance Metrics", "weight": 1.0} -->

Rollout Aggregation is required to evaluate in standard motion forecasting benchmarks, such as WOMD. These often require representing predicted trajectories as a small set of distinct "modes" with associated probabilities, per agent. These modes can capture different maneuver outcomes (like yielding or passing) or subtle variations in speed and path. To achieve this compact representation, we aggregate 64 predicted trajectories (rollouts) into 12 representative trajectories using NMS and K-means clustering, following Varadarajan et al. and Seff et al.. This technique can be thought of as a soft version of majority voting, a common technique in aggregating samples in LLMs. The following metrics then evaluate these 12 clustered trajectories.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Scaling of Open-loop Distance Metrics", "weight": 1.0} -->

Minimum Average Displacement Error (minADE) computes the Euclidean distance error of the trajectory closest to the ground truth.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Scaling of Open-loop Distance Metrics", "weight": 1.0} -->

where $y^{k}$ is the $k$-th predicted trajectory for a given agent, $\hat{y}$ is the ground truth trajectory for the agent, and T is the number of time steps per trajectory. The final metric is averaged over the total number of agents predicted over the evaluation dataset.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Scaling of Open-loop Distance Metrics", "weight": 1.0} -->

Weighted Average Displacement Error (wADE) computes the average distance error weighted by the probability of each trajectory cluster. This metric is more sensitive to the model's coverage of different maneuver modes.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Scaling of Open-loop Distance Metrics", "weight": 1.0} -->

where $K$ is the total number of predictions (clusters) per agent, and $p_{k}$ is the probability of that prediction. Similar to minADE, the final metric is averaged over the total number of agents predicted over the evaluation dataset.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Scaling of Open-loop Distance Metrics", "weight": 1.0} -->

Instead of evaluating the optimal models identified in the loss scaling law study, we repeat the iso-FLOP procedure for each metric to obtain their respective scaling trends. Figure displays the power-law fits for both the minADE and wADE metrics. We observe that the power-law improvement in the loss translates to these open-loop metrics. While we show power-law fits in our figures, we caution that establishing a power-law relationship would require a study spanning many more orders of magnitude of compute and more rigorous statistical methodology. We use power-law fits here as the simplest hypothesis suggesting that a monotonically decreasing cross-entropy would also minimize the distance of the closest predicted trajectory to the ground truth. In fact, a parabolic form fits our observed data better, but would likely introduce high variance if the study were extended to higher compute. We defer establishing whether an empirical "law" governs the scaling of distance metrics to future studies with larger data and compute budgets.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Closed-loop scaling", "weight": 1.0} -->

While other domains also show improvements in open-loop model performance from scaling up models, closed-loop performance is a relatively unexplored area of research. In many domains---and of particular interest, in robotics---it is an active debate whether improvements on open-loop metrics (e.g., cross-entropy or distance from expert demonstration) translate to improvements in closed-loop performance. Showing that open-loop scaling studies translate to closed-loop performance can be highly promising for safety-critical applications like autonomous vehicles and embodied AI robotics in general.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Closed-loop scaling", "weight": 1.0} -->

We study closed-loop scaling trends by transferring the scaling series of multi-agent motion forecasting models to an autonomous vehicle (AV) policy that is route-conditioned. To achieve this transfer, we fine-tune the models to output plans only for the autonomous driving agent ($M$=1), with an additional input of a planning route. This planning route is a coarse definition of the path the autonomous vehicle is expected to follow to reach its destination, which we represent as polylines similar to the roadgraph input explained in Section. All models were fine-tuned to do planning route conditioning using the same compute budget of $10^{15}$ FLOPs. Note that this finetuning is very short compared to pretraining, which is many orders of magnitude larger. Even for the smallest model in the series, this fine-tuning requires 3 orders of magnitude less compute than its pretraining.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Closed-loop scaling", "weight": 1.0} -->

In our setup, the closed-loop simulation environment contains a mix of logged agent playback and imitation-learned simulated agents which can interact with the AV planning model. A simulated scenario is run for a fixed time duration of $30$s at a time discretization of $10$Hz. At every simulated step, we need to execute a single action from the AV policy. To obtain this action, we first compute $R$=128 trajectory rollouts, then select one of the rollouts as a plan $y^{\ast}$ according to the equation below, and finally provide only the first 0.1 seconds of the plan as the action to the simulator.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Closed-loop scaling", "weight": 1.0} -->

where $i \in {1,\ldots,R}$ and $j \in {1,\ldots,R}$, $\text{Progress}{(y)}$ denotes the progress along the route of a trajectory, and $\alpha$ is a hyperparameter calibrating the progress bias (higher $\alpha$ indicates a stronger preference for trajectories that progress more).

<!-- chunk {"id": "body-0067", "role": "body", "section": "Closed-loop scaling", "weight": 1.0} -->

Calibrating the progress bias is important because different driving policies may have different driving styles in terms of assertiveness. Using a separate closed-loop validation set mined for interestingness and diversity (non-overlapping with the validation set used in previous sections), we tune $\alpha$ for each model in the scaling law analysis such that all models have roughly the same assertiveness. This is done by ensuring that the ratio between the number of scenarios where the policy progresses significantly more than manual driving and the number of scenarios where the policy progresses significantly less than manual driving is similar across models.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Closed-loop scaling", "weight": 1.0} -->

We define our closed-loop metric $\eta$ as the number of failed scenarios, and consider a scenario to fail if it does not imitate well the manual driving according to any of these three conditions: the policy progresses significantly more than manual driving, the policy progresses significantly less than manual driving, or the policy causes a collision. Note that even though all policies have been calibrated to have a similar assertiveness, better models will be able to achieve a lower $\eta$ by being closer to the manual driving (i.e., less events of the three types above).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Closed-loop scaling", "weight": 1.0} -->

In Figure 10 we show closed-loop results when evaluating the calibrated policies of different sizes in the closed-loop validation set. We see that similar to the scaling law fits for both loss and open loop metrics, closed loop performance also follows a similar scaling trend, with the number of failures $\eta$ decreasing as a power law when scaling pretraining compute. This suggests that open loop performance can serve as a good proxy for closed loop.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Closed-loop scaling", "weight": 1.0} -->

It is worth comparing this result with previous works that found a lack of transfer between open-loop and closed-loop performance, especially for imitation learning based approaches Casas et al.; Dauner et al.; Li et al.; Cheng et al.; Bouzidi et al.; Li et al.. One important difference is that those studies compared the performance of different models across open-loop and closed-loop benchmarks. In that setup, there are many confounders that could create differing transfer properties: model architecture, model size, objective function, etc. Our study, in contrast, is much more controlled. We use a simple architecture with minimal inductive biases, a simple loss, and study the sole effect of scaling up the model compute-optimally. We are glad to identify scale as a key lever to improve performance in both open-loop and closed-loop. We believe this is an important takeaway for the field of autonomous driving. We hypothesize that having a simple architecture with minimal inductive biases is an important piece to achieve this result.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Inference Scaling Laws", "weight": 1.0} -->

Scaling the amount of compute used to train models has dramatically improved their capabilities, as described in previous sections. Here, we explore inference compute as another axis for scaling by increasing the number of generated samples to more accurately represent the trajectory distribution. Similar have done for LLMs as shown in Brown et al.; Snell et al.. To explore the trade-off between inference compute and model size, we compute the metrics defined in the Waymo Open Motion Dataset (WOMD) Motion Prediction Challenge described in Ettinger et al. while varying the number of samples generated by the models.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Inference Scaling Laws", "weight": 1.0} -->

Minimum Final Displacement Error (minFDE) is equivalent to the minADE computed only at step T.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Inference Scaling Laws", "weight": 1.0} -->

Miss Rate computes the proportion of predictions within tolerance bounds. A miss is defined as the state when none of the individual $K$ predictions for an agent are within a given lateral and longitudinal threshold of the ground truth trajectory at a given time $T$. The thresholds are scaled with both time and speed following Ettinger et al.. The miss rate is calculated as the total number of misses divided by the total number of agents predicted.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Inference Scaling Laws", "weight": 1.0} -->

mAP computes the mean average precision of predictions bucketed by behavior. Following Ettinger et al., ground truth trajectories are grouped into behavior buckets including straight, straight-left, straight-right, left, right, left u-turn, right u-turn, and stationary. Using the same definition of a miss defined above, all misses are assigned a false positive and non-misses a true positive and stored per bucket. An average precision value is computed from the P/R curve for each bucket. The final metric is the mean average precision across all buckets.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Inference Scaling Laws", "weight": 1.0} -->

The number of trajectories sampled from each model was varied from 8 to 1024 increasing by a multiple of 2. All metrics were computed using $K = 6$ by applying Non-Maximal Suppression(NMS) clustering on the output trajectories using the aggregation algorithm, the same as described in Section 5.1.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Inference Scaling Laws", "weight": 1.0} -->

To simplify the analysis and the plot, we choose three models of increasing capacity to do this analysis. Figures 11 and show the computed metrics on these models. We use the pretrained models without any further post-training. We observe that coverage -- as measured by the mAP metric -- improves as inference compute increases over three orders of magnitude. In addition, distance based metrics like minFDE/minADE which measure precision, also continue to scale as inference compute increases. The improvement in each individual model is bounded however, and increasing inference compute beyond a cross-over point has diminishing returns. At this point a model with larger capacity becomes more inference compute optimal. As such, each model has a distinct range over the inference FLOPs domain for which it is the optimal model as shown in Figures 11 and.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Cross-agent Skills Transfer", "weight": 1.0} -->

One of the main challenges in advancing machine learning for robotics is the amount of data needed to train modern, high-capacity deep learning models. Data collection is a slow, human-driven process that requires platforms, logistics, and time, all of which pose significant challenges to scalability. To address this challenge, there is a growing body of research focusing on pretraining on passive robotic video data without robotic-action labels Ye et al., and even pretraining on internet-collected video datasets Wu et al.; Cheang et al.. Similarly, for autonomous vehicle (AV) applications, determining whether we can leverage videos of observed agents to train AV planner models could help us train larger foundation models and improve generalizability to new geographic areas without extensive data collection operations. In this brief study, we aim to shed light on two questions: 1) Does training on observed trajectories of other agents transfer to the AV agent? 2) If so, how much is a human-demonstrated mile worth compared to an observed mile?

<!-- chunk {"id": "body-0078", "role": "body", "section": "Cross-agent Skills Transfer", "weight": 1.0} -->

To answer these questions, we trained compute-optimal models from our main study on joint 8-agent prediction, excluding the AV agent. We then zero-shot evaluated these models on 8 agents, including the AV agent. We compared the AV cross-entropy loss from these models to models trained with AV trajectories^22^2Note that these models were trained at a later time than the main scaling laws run and used a different action space configuration. Thus, the difference in the absolute value of the loss compared to Figure.. Figure compares these losses as a function of training compute FLOPs. It is clear that models trained without the AV exhibit reasonable zero-shot generalization to the AV agent and follow a similar scaling trend as we increase training compute.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Cross-agent Skills Transfer", "weight": 1.0} -->

To answer the data equivalency question, we first fit the loss results as a function of the number of training data miles, as shown in Figure (Left). We then used these fits to perform an iso-loss analysis, determining the number of observed miles needed to achieve the same loss as demonstrated miles. The comparison is limited to the common loss range between the two curves to reduce extrapolation errors. The trend indicates that every 10 observed miles are equivalent to 2 to 3 demonstrated miles.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Cross-agent Skills Transfer", "weight": 1.0} -->

One important caveat to this analysis is that all training data was obtained on the same AV-agent platform, so the examples generally correlate with the AV ego-agent. An interesting future direction would be to conduct this study on purely passive observed driving miles or data pooled from different driving platforms. Despite this correlation caveat, we include this analysis to contribute to the discussion of how to address data challenges for robotics applications in general, and as a possible direction to improve the generalizability of AV foundation models to new geographic areas and driving behavior.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this report, we presented our scaling laws study of an encoder-decoder transformer model for a joint prediction task in the autonomous driving domain. Like the case for LLMs, we observe that improvements in the cross-entropy loss follow a power-law as we scale the training compute, while jointly scaling the model and dataset sizes. However, unlike the case for LLMs, the optimal models for this task tend to be relatively smaller in size, while requiring significantly more data to train. We believe that this finding, if it holds for similar robotic planning tasks, has important implications for data collection and the sizes of models that should be trained. Furthermore, the smaller sizes of these models result in lower latency, which implies that improvements in onboard system performance can be directly driven by scaling training dataset size and compute.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Discussion", "weight": 1.5} -->

We know that, while driving data is highly multi-modal, the distribution of the training data is dominated by less interesting modes, like driving straight. We also hypothesize that, unlike the case for language, driving intuitively requires less knowledge building and retrieval and more spatial reasoning, so the optimal models for this planning task would likely have relatively fewer parameters in the feed-forward network layers. An interesting research direction is to understand which of these observations could help explain the relatively smaller sizes of the optimal models.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Discussion", "weight": 1.5} -->

Another interesting direction is to investigate what changes would make these models more data-efficient on this task. For example, would sampling more challenging driving scenarios require spending more compute per example and help the model learn more from less data? How would using richer perception inputs, such as vision tokens, or moving to an end-to-end paradigm affect the data efficiency of these models? On the model output side, would increasing the complexity of the world-modeling, e.g., the action space, the number of modeled agents, or the model output modality, make the models learn more from each example? These are all interesting questions that we hope to see answered as we learn more about the nature of these empirical scaling laws, especially for domains beyond language.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Discussion", "weight": 1.5} -->

While we show that improvements in the cross-entropy loss lead to improvements in open and closed-loop metrics, our current computational budget does not span enough orders of magnitude to establish whether they, too, follow a power-law relationship with training compute. We hope that future studies will help obtain a predictive relation, if one exists.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Discussion", "weight": 1.5} -->

We observe that cross-entropy and all metrics are better explained by a power-law plus a constant. It is important for future studies to understand whether this is measuring the epistemic irreducible loss of the problem, i.e., the entropy of the true data distribution, or if is an artifact of other factors. Our leading hypotheses are that the limited dataset size, systematic duplication of features by overlapping examples, and the basic set of scene-level perception features used are the leading contributors to the observed constants.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Discussion", "weight": 1.5} -->

The improvement of models by scaling inference-time compute is a particularly interesting result. First, we see that improving models only by increasing sampling has a point of diminishing returns, at which point it is better to sample a larger and more expensive model, confirming the need for training larger models with larger compute budgets and datasets. Second, the improvement itself calls for more adaptive strategies for how to choose inference-time compute to solve more challenging scenarios. There are recent proposals for how to do this for LLMs Snell et al.. Similarly, for planning tasks in robotics, different scenarios vary drastically in their complexity, and onboard systems could adapt the compute needed to solve them.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Discussion", "weight": 1.5} -->

There is also the question of how to train inference-time compute-optimal models De Vries. These are smaller models trained past the Chinchilla-optimal point, which makes them cheaper for onboard applications. There are proposals for directly optimizing to find the corresponding optimal model and training dataset sizes Sardana and Frankle. In the future, we can also investigate adding the number of samples per prompt as another parameter in the optimization. Another exciting direction would be, instead of training a suite of models of different sizes, to train a nested architecture that allows us to elastically choose the model capacity to use at inference time Kudugunta et al.. It would be very interesting to see how to combine such architectures with more adaptive test time sampling techniques.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Discussion", "weight": 1.5} -->

Finally, an important question for the field of robotic manipulation is devising scalable data collection methodologies that can unlock the pre-training of larger foundation models. We hypothesize that for driving, one such source can be passively observed driving logs. While all of our data is collected from our platform, so it is not truly passive, nevertheless, we conduct a brief study to investigate whether training on observed trajectories of other agents zero-shots transfers to the AV ego-agent. We hope this study can help spur more research in this area.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Discussion", "weight": 1.5} -->

We believe this is a very rich area of research for robotics, and we are looking forward to learning more about the model scaling laws for modalities and tasks beyond natural language.
